# paula-2026 · author · run 45978330957

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; wc -l docs/protocol.md README.md docs/design.md docs/archives.md; ls entries/fouke-2025 claims attempts | head -50; ls paper
```

```
Fri Nov 27 10:03:20 UTC 2026
  779 docs/protocol.md
  139 README.md
  286 docs/design.md
  356 docs/archives.md
 1560 total
attempts:
amjad-2025-01.yaml
andrews-2024-01.yaml
armstrong-2026-01.yaml
asari-2009-01.yaml
asari-2009-02.yaml
ashworth-2025-01.yaml
athalye-2023-01.yaml
azcorra-2023-01.yaml
bakalar-2023-01.yaml
bech-2026-01.yaml
bellvila-2026-01.yaml
bennett-2024-01.yaml
berg-2020-01.yaml
[... 39 more lines not kept]
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

**Agent calls Read**

```json
{
 "file_path": "claims/paula-2026.yaml"
}
```

```
1	# Claims for de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli & de Vasconcelos
2	# (2026), "Revealing Stimulus-Dependent Dynamics Through Statistical Complexity", PRX Life 4,
3	# 023018, doi:10.1103/wndc-k654, tested on DANDI:000713.
4	#
5	# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
6	# Actions"), 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.
7	#
8	# Text read: the version of record (published 22 May 2026, corrected 22 July 2026, the
9	# correction fixing Eq. 9), from paper/10.1103-wndc-k654.txt, which holds the main text
10	# (Methods, Results, figure legends, Table I) and the Supplemental Material (Secs. I to III,
11	# supplementary Figs. 1 to 6, dated April 28, 2026). The PDF pages could not be rendered in
12	# this run, so no figure was read from its image; every value below is from the text and the
13	# legends. The paper links no analysis code: its Data Availability statement cites only the
14	# dataset, and the one URL of the supplement (https://bit.ly/4smMnMj) holds the figures of the
15	# parameter sweep. No code was read.
16	#
17	# Data the paper used (Methods II.A, Results III.A, Table I, legends of Figs. 1 to 5). The
18	# Allen Institute Visual Behavior Neuropixels dataset, cited as DANDI:000713 version
19	# 0.240702.1725 (Ref. 22). Wild-type and transgenic mice, head fixed, recorded with six
20	# Neuropixels 1.0 probes targeting visual cortex. 102 sessions. Measured variables used:
[... 915 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/paula-2026.yaml",
 "offset": 935
}
```

```
935	    divergences of 0.2 to 0.4 during active behavior.
936	  source: Results III.D, paragraph 6; Fig. 4f and 4g legends
937	  quote: During active behavior [Fig. 4(f)] and blank screens [Fig. 4(g)], similar patterns
938	    persisted, with visual cortex maintaining distinct complexity distributions from
939	    subcortical structures
940	  depends_on:
941	  - fig4e-js-complexity-natural-images
942	  criterion: Matrices as fig4e. Reproduced when, under one reading, in both conditions most
943	    pairs of a VIS subregion with a TH, HP or MB subregion exceed 0.36 (the legend's 0.4,
944	    widened by 10%), and in active behavior most HP-HP pairs lie in 0.18 to 0.44.
945	
946	- id: fig4h-js-complexity-spontaneous-converges
947	  statement: In spontaneous activity the JS divergences between regions are lower overall, visual
948	    cortex differing less from other regions (JS 0.2 to 0.4) than in visually driven states, and
949	    midbrain divergences stay low in all conditions (below 0.2 within the midbrain group).
950	  source: Results III.D, paragraph 6; Fig. 4h legend
951	  quote: 'Critically, spontaneous activity [Fig. 4(h)] exhibited reduced overall divergences,
952	    with visual cortex showing smaller differences from other regions (JS: 0.2–0.4) compared to
953	    visually driven states ... Midbrain areas showed consistently low divergence across all
954	    conditions (JS <0.2 within MB group)'
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,139p README.md | head -80; grep -n "DANDI" -A60 docs/archives.md | head -150
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
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; head -c 5000 attempts/fouke-2025-01.yaml; cat papers/datasets/paula-2026.yaml; ls questions | grep paula
```

```
total 136
drwxr-xr-x   2 runner runner  4096 Nov 27 10:00 .
drwxr-xr-x 332 runner runner 16384 Nov 27 10:00 ..
-rw-r--r--   1 runner runner  2144 Nov 27 10:00 README.md
-rw-r--r--   1 runner runner   907 Nov 27 10:00 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 27 10:00 omr.py
-rw-r--r--   1 runner runner 79403 Nov 27 10:00 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 27 10:00 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 27 10:00 requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,286p docs/design.md | head -120
```

```
# Reproduction registry: design

Status: draft for discussion. "Reproduction registry" is a working name.

## Goal

Agents work through the dandisets on the DANDI Archive that have an associated
paper. For each one, an agent tries to reproduce the paper's key findings and
figures from the open data, writes the analysis as a notebook, and registers it
here. People can deposit too, but most deposits are expected to come from
agents.

This serves two purposes:

1. **Check the data.** A finding that can be reproduced shows the dandiset is
   complete and accurate enough to support it. A finding that cannot be
   reproduced, with the reason, tells the data owner and the archive what is
   missing.
2. **Give analysts a starting point.** Someone who wants to test a new
   hypothesis on a dandiset starts from notebooks that already load the data
[... 99 more lines not kept]
```

**Agent**

Read the protocol and claims file (35 claims). Now surveying DANDI:000713.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000713/versions/ | python -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/000713/versions/0.240702.1725/" | python -c "import json,sys;d=json.load(sys.stdin);print(d['name']);print(d.get('description','')[:2000]);print(d['assetsSummary'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import requests, json, collections
url="https://api.dandiarchive.org/api/dandisets/000713/versions/0.240702.1725/assets/?page_size=1000"
assets=[]
while url:
    r=requests.get(url).json(); assets+=r['results']; url=r['next']
print(len(assets))
json.dump(assets,open('assets713.json','w'))
kinds=collections.Counter()
for a in assets:
    p=a['path']; k=p.split('_')[-1] if '_' in p else p
    kinds[k.replace('.nwb','') if 'probe' not in p else 'probe_ecephys']+=1
print(kinds.most_common(20))
main=[a for a in assets if 'probe' not in a['path']]
print(len(main)); 
for a in main[:5]: print(a['path'],a['size']/1e9)
import numpy as np
print(np.median([a['size'] for a in main])/1e9, sum(a['size'] for a in main)/1e12)
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
cd $TMPDIR && uv venv -q venv && . venv/bin/activate && uv pip install -q numpy scipy pandas h5py remfile pynwb requests matplotlib jupyter nbconvert ipykernel 2>&1 | tail -3; python -c "import pynwb,h5py,remfile;print(pynwb.__version__)"; python --version
```

```
4.2.0
Python 3.13.18
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import requests, json, collections
url="https://api.dandiarchive.org/api/dandisets/000713/versions/0.240702.1725/assets/?page_size=1000"
assets=[]
while url:
    r=requests.get(url).json(); assets+=r['results']; url=r['next']
print(len(assets))
json.dump(assets,open('assets713.json','w'))
main=[a for a in assets if 'probe' not in a['path']]
print(len(main))
for a in main[:5]: print(a['path'],a['size']/1e9)
import numpy as np
print(np.median([a['size'] for a in main])/1e9, sum(a['size'] for a in main)/1e12)
print(collections.Counter(a['path'].rsplit('_',1)[-1] for a in main))
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
0.191285718 0.964055443869
Counter({'image.nwb': 3271, 'ses-20200817T222149.nwb': 1, 'ses-20200818T230819.nwb': 1, 'ses-20200903T211657.nwb': 1, 'ses-20200902T215314.nwb': 1, 'ses-20200819T222405.nwb': 1, 'ses-20200820T221349.nwb': 1, 'ses-20200910T221115.nwb': 1, 'ses-20200909T220423.nwb': 1, 'ses-20200917T220539.nwb': 1, 'ses-20200820T220356.nwb': 1, 'ses-20200819T214708.nwb': 1, 'ses-20200902T221503.nwb': 1, 'ses-20200903T212507.nwb': 1, 'ses-20200923T212918.nwb': 1, 'ses-20200924T213432.nwb': 1, 'ses-20200826T210110.nwb': 1, 'ses-20200827T213926.nwb': 1, 'ses-20201002T000358.nwb': 1, 'ses-20200930T212736.nwb': 1, 'ses-20200923T223418.nwb': 1, 'ses-20200924T221213.nwb': 1, 'ses-20201014T221139.nwb': 1, 'ses-20201015T212349.nwb': 1, 'ses-20201001T230718.nwb': 1, 'ses-20200930T211811.nwb': 1, 'ses-20201008T221255.nwb': 1, 'ses-20201007T210141.nwb': 1, 'ses-20201008T224411.nwb': 1, 'ses-20201007T215334.nwb': 1, 'ses-20201029T215200.nwb': 1, 'ses-20201028T205130.nwb': 1, 'ses-20201105T232643.nwb': 1, 'ses-20201104T222222.nwb': 1, 'ses-20201119T233405.nwb': 1, 'ses-20201118T231344.nwb': 1, 'ses-20201222T220049.nwb': 1, 'ses-20201223T225408.nwb': 1, 'ses-20201112T232733.nwb': 1, 'ses-20201111T224302.nwb': 1, 'ses-20201112T231933.nwb': 1, 'ses-20201111T230013.nwb': 1, 'ses-20201124T222148.nwb': 1, 'ses-20201124T000556.nwb': 1, 'ses-20201119T231801.nwb': 1, 'ses-20201118T224526.nwb': 1, 'ses-20201216T212257.nwb': 1, 'ses-20201203T221828.nwb': 1, 'ses-20201202T223013.nwb': 1, 'ses-20201210T221304.nwb': 1, 'ses-20201209T224244.nwb': 1, 'ses-20201124T220751.nwb': 1, 'ses-20201123T233032.nwb': 1, 'ses-20201209T215912.nwb': 1, 'ses-20201210T220424.nwb': 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import json, numpy as np
a=json.load(open('assets713.json'))
s=[x for x in a if 'probe' not in x['path'] and not x['path'].endswith('_image.nwb')]
print(len(s), np.median([x['size'] for x in s])/1e9, sum(x['size'] for x in s)/1e9)
s.sort(key=lambda x:x['size']); print(s[0]['path'],s[0]['size']/1e9, s[-1]['path'], s[-1]['size']/1e9)
json.dump(s,open('sessions713.json','w'))
print(s[len(s)//2])
EOF
```

```
153 2.690058323 419.914358483
sub-563497/sub-563497_ses-20210520T214532.nwb 1.403963704 sub-527294/sub-527294_ses-20200826T210110.nwb 4.354046401
{'asset_id': 'd4a676a8-d362-4590-836f-7b6ecd78d105', 'blob': 'd4b99338-2a5b-41fc-82b6-80f17c07df1f', 'zarr': None, 'path': 'sub-585329/sub-585329_ses-20211110T230835.nwb', 'size': 2690058323, 'created': '2023-12-01T08:40:33.725874Z', 'modified': '2024-07-02T17:25:45.442780Z'}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && time python - <<'EOF'
import json, h5py, remfile, requests, time
s=json.load(open('sessions713.json'))
x=s[len(s)//2]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
r=requests.head(url,allow_redirects=True); s3=r.url.split('?')[0]; print(s3)
f=h5py.File(remfile.File(s3),'r')
def walk(g,pre='',depth=0):
    for k in g:
        o=g[k]
        if isinstance(o,h5py.Dataset):
            print(pre+k, o.shape, o.dtype)
        else:
            print(pre+k+'/', dict((a,str(o.attrs[a])[:60]) for a in ['neurodata_type','description'] if a in o.attrs))
            if depth<3: walk(o,pre+'  ',depth+1)
walk(f)
EOF
```

```
https://dandiarchive.s3.amazonaws.com/blobs/d4b/993/d4b99338-2a5b-41fc-82b6-80f17c07df1f
acquisition/ {}
  EyeTracking/ {'neurodata_type': 'EllipseEyeTracking'}
    corneal_reflection_tracking/ {'neurodata_type': 'EllipseSeries', 'description': 'no description'}
      angle (569455,) float64
      area (569455,) float64
      area_raw (569455,) float64
      data (569455, 2) float64
      height (569455,) float64
      reference_frame () object
      timestamps (569455,) float64
      width (569455,) float64
    eye_tracking/ {'neurodata_type': 'EllipseSeries', 'description': 'no description'}
      angle (569455,) float64
      area (569455,) float64
      area_raw (569455,) float64
      data (569455, 2) float64
      height (569455,) float64
      reference_frame () object
      timestamps (569455,) float64
[... 322 more lines not kept]
```

**Agent calls Bash**

```bash
wc -w paper/10.1103-wndc-k654.txt; grep -n -i "Methods\|II\. \|^[A-Z]\. " paper/10.1103-wndc-k654.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-wndc-k654.txt",
 "offset": 95,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import json, h5py, remfile, time, numpy as np, resource
s=json.load(open('sessions713.json'))
x=s[len(s)//2]
s3=f"https://dandiarchive.s3.amazonaws.com/blobs/{x['blob'][:3]}/{x['blob'][3:6]}/{x['blob']}"
t=time.time()
f=h5py.File(remfile.File(s3),'r')
u=f['units']
idx=u['spike_times_index'][:]
print(time.time()-t)
sp=f['intervals/spontaneous_presentations']
print('spont', sp['start_time'][:], sp['stop_time'][:], sp['stimulus_block'][:])
ni=f['intervals/Natural_Images_Lum_Matched_set_ophys_H_2019_presentations']
st=ni['start_time'][:]; blk=ni['stimulus_block'][:]; act=ni['active'][:]
for b in np.unique(blk): m=blk==b; print('block',b,m.sum(),st[m].min(),st[m].max(),act[m].mean())
print(u['spike_times'].chunks, u['spike_times'].compression)
t=time.time()
a=u['spike_times'][:idx[200]]
dt=time.time()-t; print('read',idx[200]*8/1e6,'MB in',dt)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
0.9313316345214844
spont [3652.40233344 4574.4234899 ] [3662.41069344 4863.41513344] [1 3]
block 0 4803 27.705471605438422 3632.8860282398578 1.0
block 5 4803 5186.20170083285 8791.332135374569 0.0
None None
read 87.76636 MB in 1.096778392791748
0.322292
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import json, h5py, remfile, time, numpy as np, pandas as pd, collections
s=json.load(open('sessions713.json'))
x=s[len(s)//2]
s3=f"https://dandiarchive.s3.amazonaws.com/blobs/{x['blob'][:3]}/{x['blob'][3:6]}/{x['blob']}"
f=h5py.File(remfile.File(s3),'r')
e=f['general/extracellular_ephys/electrodes']
loc=pd.Series([v.decode() if isinstance(v,bytes) else v for v in e['location'][:]], index=e['id'][:])
u=f['units']
pk=u['peak_channel_id'][:]
ul=loc.loc[pk].values
q=pd.Series([v.decode() if isinstance(v,bytes) else v for v in u['quality'][:]])
print(q.value_counts())
print(collections.Counter(ul).most_common())
filt=(u['isi_violations'][:]<0.5)&(u['amplitude_cutoff'][:]<0.1)&(u['presence_ratio'][:]>0.9)
print('pass', filt.sum(), len(filt))
print(pd.Series(ul[filt]).value_counts().head(30).to_dict())
ni=f['intervals/Natural_Images_Lum_Matched_set_ophys_H_2019_presentations']
df=pd.DataFrame({k:ni[k][:] for k in ['start_time','stop_time','duration','image_name','is_change','omitted','stimulus_block','active','flashes_since_change']})
df['image_name']=df.image_name.str.decode('utf8') if isinstance(df.image_name[0],bytes) else df.image_name
print(df.head(12)); print(df[df.stimulus_block==0].image_name.value_counts())
d0=df[df.stimulus_block==0]
print(d0.duration.describe()); print(np.diff(d0.start_time.values)[:20])
print(f['session_description'][()], f['general/subject/genotype'][()], f['general/metadata'].keys() if hasattr(f['general/metadata'],'keys') else '')
print({k:f['general/metadata'][k][()] for k in f['general/metadata'].keys()})
EOF
```

```
Fri Nov 27 10:06:02 UTC 2026
good     1895
noise     379
Name: count, dtype: int64
[('CA1', 482), ('VISp', 200), ('DG', 175), ('VISl', 152), ('VISpm', 141), ('VISam', 135), ('VISal', 124), ('CA3', 123), ('MGv', 117), ('VISrl', 99), ('SUB', 87), ('PIL', 73), ('MGm', 64), ('PoT', 54), ('APN', 51), ('ProS', 50), ('MB', 40), ('MGd', 28), ('SCig', 26), ('TH', 26), ('LP', 19), ('MRN', 8)]
pass 944 2274
{'CA1': 203, 'VISp': 93, 'VISam': 66, 'VISpm': 66, 'VISl': 62, 'DG': 58, 'VISal': 56, 'CA3': 51, 'MGv': 47, 'PIL': 41, 'VISrl': 39, 'SUB': 32, 'APN': 27, 'ProS': 22, 'MB': 17, 'SCig': 14, 'TH': 12, 'PoT': 12, 'MGm': 11, 'LP': 10, 'MGd': 4, 'MRN': 1}
    start_time  stop_time  ...  active  flashes_since_change
0    27.705472  27.955683  ...    True                     0
1    28.456107  28.706318  ...    True                     1
2    29.206725  29.456928  ...    True                     1
3    29.957343  30.207555  ...    True                     2
4    30.707978  30.958187  ...    True                     3
5    31.458603  31.708812  ...    True                     3
6    32.209240  32.459454  ...    True                     4
7    32.959872  33.210075  ...    True                     5
8    33.710482  33.960691  ...    True                     6
9    34.461109  34.711318  ...    True                     7
10   35.211730  35.461936  ...    True                     8
11   35.962346  36.212550  ...    True                     9
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-wndc-k654.txt",
 "offset": 515,
 "limit": 250
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/paula-2026/paula.py",
 "content": "\"\"\"Loading and measures for de Paula et al. (2026), PRX Life 4, 023018, on DANDI:000713.\n\nThe paper analyses the population firing rate of \"local populations\" (the units of one\nbrain subregion in one session) of the Allen Visual Behavior Neuropixels dataset in 100-s\nwindows of four conditions. This module streams each session's NWB file from the archive\n(remfile and h5py, nothing written to disk), builds the windows and returns one row per\nwindow with every measure the claims use. Sources of each parameter:\n\n- Population rate r(t): spike counts of the N units in nonoverlapping 50 ms bins divided by\n  N times 50 ms (Methods II.B, Eq. 1; nonoverlap from Methods II.C, T = 2000 points per 100 s).\n- CV: the standard deviation over the mean of r(t) in each nonoverlapping 10-s window, averaged\n  over the ten (Methods II.B, Eq. 2). A 10-s window with no spike has no CV and is left out of\n  the mean (a standard choice; it occurs only in near-silent populations).\n- Bandt and Pompe patterns, D = 6, tau = 1, ties ranked higher for the later element (Methods\n  II.C: \"In cases of equal values (ties), we assigned higher ranks to later-occurring\n  elements\"), done with a stable argsort. H normalised by ln(D!) (Eq. 6). C = Q0 DJS[P, Pe] H\n  with DJS as in Eq. 9 in natural logs and Q0 the standard MPR constant of Ref. 29 for D!\n  states (the claims file's reading of \"normalization constant\").\n- Surrogate: each neuron's interspike intervals within the window shuffled independently\n  (Methods II.E); the first spike stays in place (claims file, opening comment; a standard\n  choice). Generators are seeded from the claim (protocol) and the session index.\n- Active behavior: the first stimulus block of the session (the change detection task with\n  `active` true), from its first flash onset, cut into nonoverlapping 100-s windows, at most\n  36 (Methods II.A: \"The approximately 3600 s ... were divided into 36 nonoverlapping 100-s\n  windows (sessions shorter than 3600 s yielded fewer windows)\"). Starting at the first flash\n  is a standard choice.\n- Natural images: per image, its non-omitted flashes of the active block, [start, stop)\n  pieces concatenated with shifted spike times, central 100 s (Methods II.A). Blanks: the\n  500 ms after each such flash, [stop, min(stop + 0.5, next onset)); reading 'a' every flash,\n  reading 'b' only flashes followed by a non-omitted flash (claims file, opening comment).\n- Spontaneous: the longest `spontaneous` presentation after the active block (the ~5 min gray\n  screen, Methods II.A); reading 'a' the first two 100-s windows from its start, reading 'b'\n  two consecutive windows centred in it (claims file, opening comment).\n- Unit readings (claims file): 'all', every unit of the units table; 'qc', ISI violations <\n  0.5, amplitude cutoff < 0.1 and presence ratio > 0.9.\n- Brain structure of a unit: the `location` of its peak channel in the electrodes table.\n- Mean pairwise correlation (supplement Sec. III): the mean Pearson correlation over all unit\n  pairs of spike counts in 50 ms and 20 ms bins, units without spikes in the window left out\n  (claims file; a standard choice). Computed for visual cortex and midbrain populations only,\n  the areas the claims on it concern.\n- Robustness (Supplemental Sec. II): C and H for bin 20 ms with (D, tau) = (3, 4), (5, 1),\n  (6, 1) and bin 50 ms with (4, 2), (5, 3), the combinations the claims file lists.\n\"\"\"\nimport json\nimport math\nimport zlib\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET = \"000713\"\nVERSION = \"0.240702.1725\"\nPAPER = \"paula-2026\"\nAPI = f\"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{VERSION}\"\n\nBIN = 0.05\nWIN = 100.0\nCV_WIN = 10.0\nD, TAU = 6, 1\nROBUST = [(0.02, 3, 4), (0.02, 5, 1), (0.02, 6, 1), (0.05, 4, 2), (0.05, 5, 3)]\nSURR_SEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\nSURR_CLAIM = \"fig1c-cv-above-surrogate\"\nMIN_UNITS = 30\nMIN_SESSIONS = 8\n\nAREAS = {\n    \"VIS\": [\"VISal\", \"VISam\", \"VISl\", \"VISp\", \"VISpm\", \"VISrl\"],\n    \"TH\": [\"LGd\", \"LP\", \"MGd\", \"MGm\", \"MGv\", \"PIL\", \"POL\", \"PoT\", \"SGN\"],\n    \"HP\": [\"CA1\", \"CA3\", \"DG\", \"POST\", \"ProS\", \"SUB\"],\n    \"MB\": [\"APN\", \"NB\", \"NOT\", \"MRN\", \"SCig\"],\n}\nREGION_AREA = {r: a for a, rs in AREAS.items() for r in rs}\nREGION_ORDER = [r for rs in AREAS.values() for r in rs]\n\n\ndef seed(claim):\n    \"\"\"The claim's seed, zlib.crc32(b\"<paper>/<claim>\") (protocol, author step 3).\"\"\"\n    return zlib.crc32(f\"{PAPER}/{claim}\".encode())\n\n\ndef list_sessions():\n    \"\"\"The ecephys session files of the pinned version (not the probe LFP files and not the\n    behavior-only `_image.nwb` files), sorted by path.\"\"\"\n    url = f\"{API}/assets/?page_size=1000\"\n    assets = []\n    while url:\n        r = requests.get(url, timeout=60)\n        r.raise_for_status()\n        r = r.json()\n        assets += r[\"results\"]\n        url = r[\"next\"]\n    s = [a for a in assets if \"probe\" not in a[\"path\"] and not a[\"path\"].endswith(\"_image.nwb\")]\n    return sorted(s, key=lambda a: a[\"path\"]), len(assets)\n\n\ndef s3_url(asset):\n    b = asset[\"blob\"]\n    return f\"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}\"\n\n\ndef _str(a):\n    return np.array([v.decode() if isinstance(v, bytes) else str(v) for v in a])\n\n\n# ---------------------------------------------------------------- ordinal measures\n\ndef _q0(n):\n    return -2.0 / (((n + 1.0) / n) * math.log(n + 1.0) - 2.0 * math.log(2.0 * n) + math.log(n))\n\n\ndef _shannon(p):\n    p = p[p > 0]\n    return -np.sum(p * np.log(p))\n\n\ndef bandt_pompe(x, d=D, tau=TAU):\n    \"\"\"Normalised permutation entropy H and MPR complexity C of series x (Eqs. 3 to 9).\"\"\"\n    x = np.asarray(x, float)\n    n = len(x) - (d - 1) * tau\n    if n <= 0:\n        return np.nan, np.nan\n    emb = np.stack([x[i * tau:i * tau + n] for i in range(d)], axis=1)\n    perm = np.argsort(emb, axis=1, kind=\"stable\")\n    code = (perm * (d ** np.arange(d))).sum(axis=1)\n    _, counts = np.unique(code, return_counts=True)\n    nstates = math.factorial(d)\n    p = np.zeros(nstates)\n    p[:len(counts)] = counts / counts.sum()\n    s = _shannon(p)\n    h = s / math.log(nstates)\n    pe = np.full(nstates, 1.0 / nstates)\n    djs = _shannon((p + pe) / 2) - s / 2 - math.log(nstates) / 2\n    return h, _q0(nstates) * djs * h\n\n\ndef cv_windows(r, per=int(CV_WIN / BIN)):\n    \"\"\"CV of r in nonoverlapping windows of `per` bins (Eq. 2); NaN where the mean is 0.\"\"\"\n    m = len(r) // per\n    x = r[:m * per].reshape(m, per)\n    mu = x.mean(axis=1)\n    sd = x.std(axis=1)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        return np.where(mu > 0, sd / mu, np.nan)\n\n\ndef js_divergence(a, b, bins, base=2.0):\n    \"\"\"JS divergence of the histograms of a and b, `bins` equal bins over their pooled range.\"\"\"\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    a = a[np.isfinite(a)]\n    b = b[np.isfinite(b)]\n    if len(a) == 0 or len(b) == 0:\n        return np.nan\n    lo, hi = min(a.min(), b.min()), max(a.max(), b.max())\n    if hi <= lo:\n        return 0.0\n    pa = np.histogram(a, bins=bins, range=(lo, hi))[0].astype(float)\n    pb = np.histogram(b, bins=bins, range=(lo, hi))[0].astype(float)\n    pa /= pa.sum()\n    pb /= pb.sum()\n    m = (pa + pb) / 2\n\n    def kl(p):\n        k = p > 0\n        return np.sum(p[k] * np.log(p[k] / m[k]))\n\n    return (kl(pa) + kl(pb)) / 2 / math.log(base)\n\n\n# ---------------------------------------------------------------- windows\n\ndef _concat(times, owners, pieces):\n    \"\"\"Spikes inside the [a, b) pieces, mapped onto a time axis where the pieces abut.\"\"\"\n    pieces = np.asarray(pieces, float)\n    if len(pieces) == 0:\n        return np.array([]), np.array([], int), 0.0\n    a, b = pieces[:, 0], pieces[:, 1]\n    offs = np.concatenate([[0.0], np.cumsum(b - a)])\n    k = np.searchsorted(a, times, side=\"right\") - 1\n    ok = (k >= 0) & (times < b[np.clip(k, 0, None)])\n    k = k[ok]\n    return times[ok] - a[k] + offs[k], owners[ok], offs[-1]\n\n\ndef _window(times, owners, t0, t1):\n    m = (times >= t0) & (times < t1)\n    return times[m] - t0, owners[m]\n\n\ndef shuffle_isi(t, own, rng):\n    \"\"\"Shuffle each unit's interspike intervals independently, the first spike kept.\"\"\"\n    if len(t) == 0:\n        return t\n    o = np.lexsort((t, own))\n    t, own = t[o], own[o]\n    first = np.r_[True, own[1:] != own[:-1]]\n    isi = np.diff(t, prepend=0.0)\n    isi[first] = 0.0\n    keys = rng.random(len(t))\n    keys[first] = -1.0\n    o2 = np.lexsort((keys, own))  # within unit, first spike then intervals in random order\n    isi_s = isi[o2]\n    start = np.where(first, t, 0.0)  # first spikes stay where they were\n    grp = np.cumsum(first) - 1\n    base = start[first][grp]\n    out = base + (np.cumsum(isi_s) - np.cumsum(isi_s * first)[first][grp] * 0\n                  - np.concatenate([[0.0], np.cumsum(isi_s)[:-1]])[first][grp])\n    return out\n\n\ndef rate(t, n_units, length=WIN, bw=BIN):\n    nb = int(round(length / bw))\n    c = np.bincount(np.minimum((t / bw).astype(int), nb - 1), minlength=nb)[:nb]\n    return c / (n_units * bw)\n\n\ndef mean_corr(t, own, n_units, bw, length=WIN):\n    nb = int(round(length / bw))\n    m = np.zeros((n_units, nb), np.float32)\n    b = np.minimum((t / bw).astype(int), nb - 1)\n    np.add.at(m, (own, b), 1)\n    m = m[m.std(axis=1) > 0]\n    if len(m) < 2:\n        return np.nan\n    m -= m.mean(axis=1, keepdims=True)\n    m /= np.linalg.norm(m, axis=1, keepdims=True)\n    c = m @ m.T\n    k = len(m)\n    return float((c.sum() - np.trace(c)) / (k * (k - 1)))\n\n\ndef window_measures(t, own, n_units, surr_rngs, do_corr):\n    \"\"\"All measures of one 100-s window of a population (t in 0..100 s, own in 0..N-1).\"\"\"\n    r = rate(t, n_units)\n    cv10 = cv_windows(r)\n    h, c = bandt_pompe(r)\n    out = {\"cv\": np.nanmean(cv10) if np.isfinite(cv10).any() else np.nan, \"H\": h, \"C\": c,\n           \"rate\": len(t) / (n_units * WIN), \"cv10\": cv10}\n    for bw, d, tau in ROBUST:\n        rr = r if bw == BIN else rate(t, n_units, bw=bw)\n        hh, cc = bandt_pompe(rr, d, tau)\n        out[f\"C_{int(bw*1000)}_{d}_{tau}\"] = cc\n        out[f\"H_{int(bw*1000)}_{d}_{tau}\"] = hh\n    if do_corr:\n        out[\"corr50\"] = mean_corr(t, own, n_units, 0.05)\n        out[\"corr20\"] = mean_corr(t, own, n_units, 0.02)\n    for j, rng in enumerate(surr_rngs):\n        ts = shuffle_isi(t, own, rng)\n        ts = ts[(ts >= 0) & (ts < WIN)]\n        rs = rate(ts, n_units)\n        cvs = cv_windows(rs)\n        hs, cs = bandt_pompe(rs)\n        sfx = \"\" if j == 0 else f\"_s{SURR_SEED_OFFSETS[j]}\"\n        out[\"s_cv\" + sfx] = np.nanmean(cvs) if np.isfinite(cvs).any() else np.nan\n        out[\"s_H\" + sfx] = hs\n        out[\"s_C\" + sfx] = cs\n        if j == 0:\n            out[\"s_cv10\"] = cvs\n    return out\n\n\n# ---------------------------------------------------------------- one session\n\ndef read_session(asset):\n    \"\"\"Stream one session: metadata, epochs and the spike times of units in candidate\n    regions (a region with at least 30 units under the 'all' reading), up to the end of\n    the spontaneous epoch.\"\"\"\n    f = h5py.File(remfile.File(s3_url(asset)), \"r\")\n    meta = {\"path\": asset[\"path\"], \"session_description\": f[\"session_description\"][()].decode(),\n            \"subject\": f[\"general/subject/subject_id\"][()].decode(),\n            \"genotype\": f[\"general/subject/genotype\"][()].decode(),\n            \"session_start_time\": f[\"session_start_time\"][()].decode()}\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    loc = pd.Series(_str(e[\"location\"][:]), index=e[\"id\"][:])\n    u = f[\"units\"]\n    units = pd.DataFrame({\n        \"region\": loc.loc[u[\"peak_channel_id\"][:]].values,\n        \"isi_violations\": u[\"isi_violations\"][:], \"amplitude_cutoff\": u[\"amplitude_cutoff\"][:],\n        \"presence_ratio\": u[\"presence_ratio\"][:], \"quality\": _str(u[\"quality\"][:]),\n        \"firing_rate\": u[\"firing_rate\"][:]})\n    units[\"qc\"] = ((units.isi_violations < 0.5) & (units.amplitude_cutoff < 0.1)\n                   & (units.presence_ratio > 0.9))\n    idx = u[\"spike_times_index\"][:].astype(np.int64)\n    meta[\"n_units\"] = len(units)\n    meta[\"n_spikes\"] = int(idx[-1])\n\n    ni_name = [k for k in f[\"intervals\"].keys() if k.startswith(\"Natural_Images\")]\n    meta[\"image_table\"] = ni_name\n    ni = f[\"intervals\"][ni_name[0]]\n    stim = pd.DataFrame({\"start\": ni[\"start_time\"][:], \"stop\": ni[\"stop_time\"][:],\n                         \"image\": _str(ni[\"image_name\"][:]), \"block\": ni[\"stimulus_block\"][:],\n                         \"active\": ni[\"active\"][:], \"omitted\": ni[\"omitted\"][:],\n                         \"is_change\": ni[\"is_change\"][:]})\n    act_block = stim[stim.active].block.min()\n    stim = stim[stim.block == act_block].sort_values(\"start\").reset_index(drop=True)\n    stim[\"omitted\"] = stim.omitted.astype(bool) | (stim.image == \"omitted\")\n    sp = f[\"intervals/spontaneous_presentations\"]\n    spont = pd.DataFrame({\"start\": sp[\"start_time\"][:], \"stop\": sp[\"stop_time\"][:]})\n    act_end = stim.stop.max()\n    spont = spont[spont.start >= act_end - 1]\n    spont[\"dur\"] = spont.stop - spont.start\n    meta[\"spont_epochs\"] = spont[[\"start\", \"stop\"]].values.tolist()\n    sp_best = spont.sort_values(\"dur\").iloc[-1] if len(spont) else None\n    meta[\"active_start\"] = float(stim.start.min())\n    meta[\"active_end\"] = float(act_end)\n    cutoff = float(sp_best.stop) if sp_best is not None else act_end\n    meta[\"cutoff\"] = cutoff\n\n    counts = units.region.value_counts()\n    cand = counts[counts >= MIN_UNITS].index\n    keep = np.flatnonzero(units.region.isin(cand).values & units.region.isin(REGION_AREA).values)\n    # also keep all visual-cortex units, for the clock check\n    vis = np.flatnonzero(units.region.isin(AREAS[\"VIS\"]).values)\n    keep = np.union1d(keep, vis)\n    starts = np.r_[0, idx[:-1]]\n    st = u[\"spike_times\"]\n    spikes = {}\n    # read contiguous blocks of units, about 40 MB at a time, keeping spikes before the cutoff\n    i = 0\n    n = len(units)\n    while i < n:\n        j = i\n        while j < n and idx[j] - starts[i] < 5_000_000:\n            j += 1\n        j = max(j, i + 1)\n        block = st[starts[i]:idx[j - 1]]\n        for k in range(i, j):\n            if k in spikes or not np.isin(k, keep):\n                continue\n            x = block[starts[k] - starts[i]:idx[k] - starts[i]]\n            spikes[k] = x[x < cutoff + 1].copy()\n        i = j\n    meta[\"fingerprint\"] = [float(x) for x in st[:5]] + [float(st[idx[-1] - 1])]\n    f.close()\n    return meta, units, stim, sp_best, spikes\n\n\ndef condition_windows(stim, sp_best):\n    \"\"\"The pieces of each condition window: a list of (condition, reading, index, image,\n    pieces) with pieces in session time; the window is the central or given 100 s.\"\"\"\n    out = []\n    a0, a1 = stim.start.min(), stim.stop.max()\n    nwin = min(36, int((a1 - a0) // WIN))\n    for k in range(nwin):\n        out.append((\"active\", \"-\", k, \"\", [(a0 + k * WIN, a0 + (k + 1) * WIN)], None))\n    shown = stim[~stim.omitted]\n    nxt_start = np.r_[stim.start.values[1:], np.inf]\n    nxt_omit = np.r_[stim.omitted.values[1:], True]\n    for k, img in enumerate(sorted(shown.image.unique())):\n        m = (~stim.omitted & (stim.image == img)).values\n        pieces = list(zip(stim.start.values[m], stim.stop.values[m]))\n        out.append((\"images\", \"-\", k, img, pieces, \"central\"))\n        bstop = np.minimum(stim.stop.values + 0.5, nxt_start)\n        pa = list(zip(stim.stop.values[m], bstop[m]))\n        out.append((\"blanks\", \"a\", k, img, pa, \"central\"))\n        mb = m & ~nxt_omit\n        pb = list(zip(stim.stop.values[mb], bstop[mb]))\n        out.append((\"blanks\", \"b\", k, img, pb, \"central\"))\n    if sp_best is not None:\n        s0, s1 = float(sp_best.start), float(sp_best.stop)\n        if s1 - s0 >= 2 * WIN:\n            for k in range(2):\n                out.append((\"spont\", \"a\", k, \"\", [(s0 + k * WIN, s0 + (k + 1) * WIN)], None))\n            mid = (s0 + s1) / 2\n            for k in range(2):\n                out.append((\"spont\", \"b\", k, \"\", [(mid - WIN + k * WIN, mid + k * WIN)], None))\n    return out\n\n\ndef clock_check(stim, vis_times):\n    \"\"\"Visual cortex response to flash onsets: mean spikes per flash in 30 to 130 ms after\n    onset minus the 100 ms before, for the true onsets and for onsets shifted by 375 ms\n    (the middle of the gray screen).\"\"\"\n    on = stim.start.values[~stim.omitted.values]\n    vt = np.sort(vis_times)\n\n    def contrast(o):\n        post = np.searchsorted(vt, o + 0.13) - np.searchsorted(vt, o + 0.03)\n        pre = np.searchsorted(vt, o) - np.searchsorted(vt, o - 0.10)\n        return float(np.mean(post - pre))\n\n    om = stim.start.values[stim.omitted.values]\n    return {\"clock_true\": contrast(on), \"clock_shift\": contrast(on + 0.375),\n            \"clock_omitted\": contrast(om) if len(om) else np.nan}\n\n\ndef process_session(args):\n    \"\"\"All windows of all populations of one session, under both unit readings.\"\"\"\n    sess_i, asset = args\n    meta, units, stim, sp_best, spikes = read_session(asset)\n    meta[\"session_index\"] = sess_i\n    vis_k = [k for k in spikes if units.region.iat[k] in AREAS[\"VIS\"]]\n    meta.update(clock_check(stim, np.concatenate([spikes[k] for k in vis_k]) if vis_k\n                            else np.array([])))\n    meta[\"n_vis_units_clock\"] = len(vis_k)\n    meta[\"region_counts_all\"] = units.region.value_counts().to_dict()\n    meta[\"region_counts_qc\"] = units.region[units.qc].value_counts().to_dict()\n    meta[\"n_flashes\"] = int((~stim.omitted).sum())\n    meta[\"n_omitted\"] = int(stim.omitted.sum())\n    meta[\"n_images\"] = int(stim[~stim.omitted].image.nunique())\n    wins = condition_windows(stim, sp_best)\n    meta[\"n_windows_listed\"] = len(wins)\n    rows, cv10 = [], []\n    base = seed(SURR_CLAIM)\n    for ur in [\"all\", \"qc\"]:\n        sel = units.qc if ur == \"qc\" else pd.Series(True, index=units.index)\n        for region in REGION_ORDER:\n            ks = np.flatnonzero(sel.values & (units.region == region).values)\n            if len(ks) < MIN_UNITS:\n                continue\n            ks = [k for k in ks if k in spikes]\n            n = len(ks)\n            t_all = np.concatenate([spikes[k] for k in ks])\n            o_all = np.concatenate([np.full(len(spikes[k]), j) for j, k in enumerate(ks)])\n            o = np.argsort(t_all, kind=\"stable\")\n            t_all, o_all = t_all[o], o_all[o]\n            do_corr = REGION_AREA[region] in (\"VIS\", \"MB\")\n            for wi, (cond, rd, k, img, pieces, mode) in enumerate(wins):\n                if mode == \"central\":\n                    tc, oc, L = _concat(t_all, o_all, pieces)\n                    if L < WIN:\n                        continue\n                    t, ow = _window(tc, oc, L / 2 - WIN / 2, L / 2 + WIN / 2)\n                    length = L\n                else:\n                    (p0, p1), = pieces\n                    t, ow = _window(t_all, o_all, p0, p1)\n                    length = p1 - p0\n                nseeds = 5 if cond == \"active\" else 1\n                rngs = [np.random.default_rng([base + off, sess_i, wi, 0 if ur == \"all\" else 1])\n                        for off in SURR_SEED_OFFSETS[:nseeds]]\n                m = window_measures(t, ow, n, rngs, do_corr)\n                c10, s10 = m.pop(\"cv10\"), m.pop(\"s_cv10\")\n                row = {\"session\": sess_i, \"subject\": meta[\"subject\"], \"units\": ur,\n                       \"region\": region, \"area\": REGION_AREA[region], \"n\": n,\n                       \"condition\": cond, \"reading\": rd, \"k\": k, \"image\": img,\n                       \"series_length\": length}\n                row.update(m)\n                rows.append(row)\n                if cond == \"active\":\n                    cv10.append({\"session\": sess_i, \"units\": ur, \"region\": region, \"k\": k,\n                                 \"cv10\": c10, \"s_cv10\": s10})\n    return meta, pd.DataFrame(rows), cv10\n\n\ndef survey_session(asset):\n    \"\"\"Metadata only: unit counts by region and filter, epochs (no spike times).\"\"\"\n    f = h5py.File(remfile.File(s3_url(asset)), \"r\")\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    loc = pd.Series(_str(e[\"location\"][:]), index=e[\"id\"][:])\n    u = f[\"units\"]\n    reg = loc.loc[u[\"peak_channel_id\"][:]].values\n    qc = ((u[\"isi_violations\"][:] < 0.5) & (u[\"amplitude_cutoff\"][:] < 0.1)\n          & (u[\"presence_ratio\"][:] > 0.9))\n    out = {\"path\": asset[\"path\"], \"all\": pd.Series(reg).value_counts().to_dict(),\n           \"qc\": pd.Series(reg[qc]).value_counts().to_dict()}\n    f.close()\n    return out\n"
}
```

```
File created successfully at: entries/paula-2026/paula.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "    o2 = np.lexsort((keys, own))  # within unit, first spike then intervals in random order\n    isi_s = isi[o2]\n    start = np.where(first, t, 0.0)  # first spikes stay where they were\n    grp = np.cumsum(first) - 1\n    base = start[first][grp]\n    out = base + (np.cumsum(isi_s) - np.cumsum(isi_s * first)[first][grp] * 0\n                  - np.concatenate([[0.0], np.cumsum(isi_s)[:-1]])[first][grp])\n    return out",
 "new_string": "    o2 = np.lexsort((keys, own))  # within unit, first spike then intervals in random order\n    isi_s = isi[o2]\n    grp = np.cumsum(first) - 1\n    fi = np.flatnonzero(first)\n    cs = np.cumsum(isi_s)\n    return t[fi][grp] + cs - cs[fi][grp]"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "    keep = np.union1d(keep, vis)\n    starts = np.r_[0, idx[:-1]]",
 "new_string": "    keep = set(np.union1d(keep, vis).tolist())\n    starts = np.r_[0, idx[:-1]]"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "            if k in spikes or not np.isin(k, keep):",
 "new_string": "            if k not in keep:"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && . $TMPDIR/venv/bin/activate && python - <<'EOF'
import numpy as np, paula
rng=np.random.default_rng(0)
print(paula.bandt_pompe(rng.random(100000)))
print(paula.bandt_pompe(np.sin(np.arange(100000)*0.05)))
# logistic map r=4
x=[0.1]
for i in range(100000): x.append(4*x[-1]*(1-x[-1]))
print('logistic',paula.bandt_pompe(np.array(x[1000:])))
t=np.sort(rng.random(50)*100); own=np.r_[np.zeros(20,int),np.ones(30,int)]
t=np.r_[np.sort(rng.random(20)*100),np.sort(rng.random(30)*100)]
s=paula.shuffle_isi(t,own,rng)
for u in [0,1]:
    a=t[own==u]; b=np.sort(s[np.sort(own)==u]) if False else None
o=np.lexsort((t,own)); ts=t[o]; os_=own[o]
for u in [0,1]:
    a=ts[os_==u]; b=s[os_==u]
    print(a[0]==b[0], np.allclose(np.sort(np.diff(a)),np.sort(np.diff(b))), np.allclose(a[-1],b[-1]), (np.diff(b)>=0).all())
EOF
```

```
(np.float64(0.9994758447288333), np.float64(0.0012569933482863207))
(np.float64(0.1614865601136838), np.float64(0.15473424861358628))
logistic (np.float64(0.6287727414838992), np.float64(0.483929967235483))
True True True True
False True True True
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
import time, resource, paula, numpy as np, pandas as pd
t=time.time()
sess,n=paula.list_sessions(); print(len(sess),n, time.time()-t)
a=[s for s in sess if s['path'].startswith('sub-585329/sub-585329_ses-20211110')][0]
i=sess.index(a)
t=time.time()
meta,units,stim,sp,spk=paula.read_session(a)
print('read',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
t=time.time()
meta,df,cv10=paula.process_session((i,a))
print('process total',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
print({k:v for k,v in meta.items() if 'counts' not in k})
print(df.shape); print(df.groupby(['units','condition','reading']).size())
pd.set_option('display.width',250); pd.set_option('display.max_columns',40)
print(df[df.units=='qc'].groupby(['region','condition','reading'])[['cv','H','C','s_cv','s_C','corr50','rate']].median().round(3).head(40))
df.to_pickle('/tmp/claude/one.pkl') if False else df.to_pickle(__import__('os').environ['TMPDIR']+'/one.pkl')
EOF
```

```
153 4293 1.03013277053833
read 14.629828214645386 1.548004
process total 145.4237780570984 2.169132
{'path': 'sub-585329/sub-585329_ses-20211110T230835.nwb', 'session_description': 'EPHYS_1_images_H_3uL_reward', 'subject': '585329', 'genotype': 'wt/wt', 'session_start_time': '2021-11-10T23:08:35+00:00', 'n_units': 2274, 'n_spikes': 112286348, 'image_table': ['Natural_Images_Lum_Matched_set_ophys_H_2019_presentations'], 'spont_epochs': [[3652.40233344064, 3662.41069344064], [4574.4234899020485, 4863.415133440641]], 'active_start': 27.705471605438422, 'active_end': 3633.1362424564713, 'cutoff': 4863.415133440641, 'fingerprint': [4.978706099783888, 5.606636812116187, 5.672036539135826, 5.828769218262403, 6.655065769276596, 9488.659056515578], 'session_index': 149, 'clock_true': 272.3887919755779, 'clock_shift': -23.97187091146969, 'clock_omitted': 5.391705069124424, 'n_vis_units_clock': 851, 'n_flashes': 4586, 'n_omitted': 217, 'n_images': 8, 'n_windows_listed': 64}
(1792, 42)
units  condition  reading
all    active     -          576
       blanks     a          128
                  b          128
       images     -          128
       spont      a           32
                  b           32
qc     active     -          432
       blanks     a           96
                  b           96
       images     -           96
       spont      a           24
                  b           24
dtype: int64
                             cv      H      C   s_cv    s_C  corr50    rate
[... 41 more lines not kept]
```

**Agent**

First full-session timing: 145 s per session, too slow for 153 sessions (values look plausible, e.g. VISal active CV 0.54 vs the paper's 0.55). Optimising the windowing, correlation and shuffle code.

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' 2>&1 | head -40
import cProfile, pstats, paula, numpy as np, pandas as pd, pickle, os
sess,n=paula.list_sessions()
a=[s for s in sess if s['path'].startswith('sub-585329/sub-585329_ses-20211110')][0]
meta,units,stim,sp,spk=paula.read_session(a)
pickle.dump((meta,units,stim,sp,spk),open(os.environ['TMPDIR']+'/sess.pkl','wb'))
EOF
ls -la $TMPDIR/sess.pkl
```

```
-rw-r--r-- 1 runner runner 390009585 Nov 27 10:11 /tmp/claude-1001/sess.pkl
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && grep -n "def process_session" -A80 paula.py | head -5
```

```
388:def process_session(args):
389-    """All windows of all populations of one session, under both unit readings."""
390-    sess_i, asset = args
391-    meta, units, stim, sp_best, spikes = read_session(asset)
392-    meta["session_index"] = sess_i
```

**Agent**

Now I'll rewrite the window construction and session processing for speed.

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
src=open('paula.py').read()
start=src.index('def condition_windows(stim, sp_best):')
end=src.index('def survey_session(asset):')
new='''def flash_table(stim):
    """Per presentation of the active block: image piece [start, stop) and blank piece
    [stop, min(stop + 0.5, next onset)); blank reading 'b' keeps only flashes followed by a
    non-omitted flash."""
    st = stim.copy()
    nxt = np.r_[st.start.values[1:], np.inf]
    st["bstop"] = np.minimum(st.stop.values + 0.5, nxt)
    st["next_shown"] = np.r_[~st.omitted.values[1:], False]
    return st


def epoch_windows(stim, sp_best):
    """Windows in session time: active (36 at most) and spontaneous (readings a and b)."""
    out = []
    a0, a1 = stim.start.min(), stim.stop.max()
    nwin = min(36, int((a1 - a0) // WIN))
    for k in range(nwin):
        out.append(("active", "-", k, a0 + k * WIN))
    if sp_best is not None:
        s0, s1 = float(sp_best.start), float(sp_best.stop)
        if s1 - s0 >= 2 * WIN:
            for k in range(2):
                out.append(("spont", "a", k, s0 + k * WIN))
            mid = (s0 + s1) / 2
            for k in range(2):
                out.append(("spont", "b", k, mid - WIN + k * WIN))
    return out


def concat_windows(t, own, ft):
    """The natural-image and blank windows of a population: for each image its pieces
    concatenated (spike times shifted so the pieces abut) and the central 100 s kept
    (Methods II.A). Returns (condition, reading, k, image, t, own, series length)."""
    starts = ft.start.values
    k = np.searchsorted(starts, t, side="right") - 1
    ok = k >= 0
    t, own, k = t[ok], own[ok], k[ok]
    dt = t - starts[k]
    img_len = (ft.stop - ft.start).values
    blk_len = (ft.bstop - ft.stop).values
    shown = ~ft.omitted.values
    in_img = shown[k] & (dt < img_len[k])
    in_blk = shown[k] & (dt >= img_len[k]) & (dt < img_len[k] + blk_len[k])
    out = []
    names = sorted(ft.image[shown].unique())
    for i, img in enumerate(names):
        m_img = shown & (ft.image.values == img)
        for cond, rd, sel, inside, plen, shift in [
                ("images", "-", m_img, in_img, img_len, 0.0),
                ("blanks", "a", m_img, in_blk, blk_len, img_len),
                ("blanks", "b", m_img & ft.next_shown.values, in_blk, blk_len, img_len)]:
            off = np.full(len(ft), np.nan)
            off[sel] = np.r_[0.0, np.cumsum(plen[sel])[:-1]]
            L = plen[sel].sum()
            mk = inside & sel[k]
            sh = shift[k[mk]] if isinstance(shift, np.ndarray) else 0.0
            tc = off[k[mk]] + dt[mk] - sh
            lo = L / 2 - WIN / 2
            w = (tc >= lo) & (tc < lo + WIN)
            if L < WIN:
                out.append((cond, rd, i, img, None, None, L))
                continue
            tw = tc[w] - lo
            ow = own[mk][w]
            o = np.argsort(tw, kind="stable")
            out.append((cond, rd, i, img, tw[o], ow[o], L))
    return out


def clock_check(stim, vis_times):
    """Visual cortex response to flash onsets: mean spikes per flash in 30 to 130 ms after
    onset minus the 100 ms before, for the true onsets and for onsets shifted by 375 ms
    (the middle of the gray screen), and for omitted flashes."""
    on = stim.start.values[~stim.omitted.values]
    vt = np.sort(vis_times)

    def contrast(o):
        post = np.searchsorted(vt, o + 0.13) - np.searchsorted(vt, o + 0.03)
        pre = np.searchsorted(vt, o) - np.searchsorted(vt, o - 0.10)
        return float(np.mean(post - pre))

    om = stim.start.values[stim.omitted.values]
    return {"clock_true": contrast(on), "clock_shift": contrast(on + 0.375),
            "clock_omitted": contrast(om) if len(om) else np.nan}


def process_session(args):
    """Read one session and compute all windows of all its populations."""
    sess_i, asset = args
    return compute_session(sess_i, *read_session(asset))


def compute_session(sess_i, meta, units, stim, sp_best, spikes):
    """All windows of all populations of one session, under both unit readings."""
    meta["session_index"] = sess_i
    vis_k = [k for k in spikes if units.region.iat[k] in AREAS["VIS"]]
    meta.update(clock_check(stim, np.concatenate([spikes[k] for k in vis_k]) if vis_k
                            else np.array([])))
    meta["n_vis_units_clock"] = len(vis_k)
    meta["region_counts_all"] = units.region.value_counts().to_dict()
    meta["region_counts_qc"] = units.region[units.qc].value_counts().to_dict()
    meta["n_flashes"] = int((~stim.omitted).sum())
    meta["n_omitted"] = int(stim.omitted.sum())
    meta["n_changes"] = int(np.nansum(stim.is_change.values))
    meta["n_images"] = int(stim[~stim.omitted].image.nunique())
    ft = flash_table(stim)
    ew = epoch_windows(stim, sp_best)
    meta["n_active_windows"] = sum(1 for w in ew if w[0] == "active")
    meta["n_spont_windows"] = sum(1 for w in ew if w[0] == "spont" and w[1] == "a")
    rows, cv10 = [], []
    base = seed(SURR_CLAIM)
    for ur in ["all", "qc"]:
        sel = units.qc if ur == "qc" else pd.Series(True, index=units.index)
        for region in REGION_ORDER:
            ks = np.flatnonzero(sel.values & (units.region == region).values)
            if len(ks) < MIN_UNITS:
                continue
            n = len(ks)
            t_all = np.concatenate([spikes[k] for k in ks])
            o_all = np.concatenate([np.full(len(spikes[k]), j) for j, k in enumerate(ks)])
            o = np.argsort(t_all, kind="stable")
            t_all, o_all = t_all[o], o_all[o]
            do_corr = REGION_AREA[region] in ("VIS", "MB")
            wins = []
            for cond, rd, k, t0 in ew:
                a, b = np.searchsorted(t_all, [t0, t0 + WIN])
                wins.append((cond, rd, k, "", t_all[a:b] - t0, o_all[a:b], WIN))
            a, b = np.searchsorted(t_all, [stim.start.min() - 1, stim.stop.max() + 1])
            wins += concat_windows(t_all[a:b], o_all[a:b], ft)
            for wi, (cond, rd, k, img, t, ow, length) in enumerate(wins):
                if t is None:
                    continue
                nseeds = 5 if cond == "active" else 1
                rngs = [np.random.default_rng([base + off, sess_i, wi, 0 if ur == "all" else 1])
                        for off in SURR_SEED_OFFSETS[:nseeds]]
                m = window_measures(t, ow, n, rngs, do_corr)
                c10, s10 = m.pop("cv10"), m.pop("s_cv10")
                row = {"session": sess_i, "subject": meta["subject"], "units": ur,
                       "region": region, "area": REGION_AREA[region], "n": n,
                       "condition": cond, "reading": rd, "k": k, "image": img,
                       "series_length": length}
                row.update(m)
                rows.append(row)
                if cond == "active":
                    cv10.append({"session": sess_i, "units": ur, "region": region, "k": k,
                                 "cv10": c10, "s_cv10": s10})
    return meta, pd.DataFrame(rows), cv10


'''
src=src[:start]+new+src[end:]
# faster mean_corr and shuffle
src=src.replace('''    m = np.zeros((n_units, nb), np.float32)
    b = np.minimum((t / bw).astype(int), nb - 1)
    np.add.at(m, (own, b), 1)
''','''    b = np.minimum((t / bw).astype(int), nb - 1)
    m = np.bincount(own * nb + b, minlength=n_units * nb).reshape(n_units, nb).astype(np.float32)
''')
src=src.replace('''    o = np.lexsort((t, own))
    t, own = t[o], own[o]
    first = np.r_[True, own[1:] != own[:-1]]
    isi = np.diff(t, prepend=0.0)
    isi[first] = 0.0
    keys = rng.random(len(t))
    keys[first] = -1.0
    o2 = np.lexsort((keys, own))  # within unit, first spike then intervals in random order
''','''    o = np.argsort(own, kind="stable")  # t is sorted, so each unit's spikes stay in order
    t, own = t[o], own[o]
    first = np.r_[True, own[1:] != own[:-1]]
    isi = np.diff(t, prepend=0.0)
    isi[first] = 0.0
    keys = rng.random(len(t)) * 0.999 + 0.0005
    keys[first] = 0.0
    o2 = np.argsort(own + keys)  # within unit, first spike then intervals in random order
''')
open('paula.py','w').write(src)
EOF
python - <<'EOF'
import paula, pickle, os, time, numpy as np
import cProfile, pstats
d=pickle.load(open(os.environ['TMPDIR']+'/sess.pkl','rb'))
t=time.time()
cProfile.run('meta,df,cv=paula.compute_session(149,*d)', os.environ['TMPDIR']+'/prof')
print(time.time()-t, df.shape)
pstats.Stats(os.environ['TMPDIR']+'/prof').sort_stats('cumtime').print_stats(15)
df.to_pickle(os.environ['TMPDIR']+'/two.pkl')
EOF
```

```
49.25510001182556 (1792, 42)
Fri Nov 27 10:13:15 2026    /tmp/claude-1001/prof

         2792151 function calls (2789170 primitive calls) in 49.252 seconds

   Ordered by: cumulative time
   List reduced from 526 to 15 due to restriction <15>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   49.252   49.252 {built-in method builtins.exec}
        1    0.003    0.003   49.252   49.252 <string>:1(<module>)
        1    0.803    0.803   49.249   49.249 entries/paula-2026/paula.py:430(compute_session)
     1792    0.575    0.000   40.529    0.023 entries/paula-2026/paula.py:232(window_measures)
    64915    0.077    0.000   27.837    0.000 /tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:48(_wrapfunc)
     5824    4.331    0.001   25.865    0.004 entries/paula-2026/paula.py:193(shuffle_isi)
    28924    0.049    0.000   25.326    0.001 /tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:1115(argsort)
    28926   25.223    0.001   25.223    0.001 {method 'argsort' of 'numpy.ndarray' objects}
    16576    1.068    0.000    7.452    0.000 entries/paula-2026/paula.py:119(bandt_pompe)
       28    2.994    0.107    4.148    0.148 entries/paula-2026/paula.py:367(concat_windows)
     1664    1.594    0.001    3.193    0.002 entries/paula-2026/paula.py:218(mean_corr)
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
import numpy as np, time, paula
rng=np.random.default_rng(1)
n=150; t=np.sort(rng.random(150000)*100); own=rng.integers(0,n,len(t))
t0=time.time()
for _ in range(20): paula.shuffle_isi(t,own,rng)
print('current',(time.time()-t0)/20)
def shuf2(t,own,rng):
    o=np.argsort(own,kind='stable'); ts=t[o]; os_=own[o]
    b=np.flatnonzero(np.r_[True,os_[1:]!=os_[:-1],True])
    out=np.empty_like(ts)
    for i in range(len(b)-1):
        x=ts[b[i]:b[i+1]]
        d=np.diff(x); rng.shuffle(d)
        out[b[i]]=x[0]; out[b[i]+1:b[i+1]]=x[0]+np.cumsum(d)
    return out
t0=time.time()
for _ in range(20): shuf2(t,own,rng)
print('loop',(time.time()-t0)/20)
t0=time.time()
for _ in range(20): np.argsort(own,kind='stable')
print('int argsort',(time.time()-t0)/20)
EOF
```

```
current 0.019554173946380614
loop 0.014218878746032716
int argsort 0.0072708606719970705
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && time python - <<'EOF'
import paula, pandas as pd, numpy as np, json, os
from concurrent.futures import ThreadPoolExecutor
sess,n=paula.list_sessions()
with ThreadPoolExecutor(8) as ex: res=list(ex.map(paula.survey_session, sess))
json.dump(res,open(os.environ['TMPDIR']+'/survey.json','w'))
for ur in ['all','qc']:
    rows=[]
    for i,r in enumerate(res):
        for reg,c in r[ur].items(): rows.append((i,reg,c))
    d=pd.DataFrame(rows,columns=['s','region','n'])
    p=d[d.n>=30]
    ns=p.groupby('region').s.nunique()
    keep=ns[ns>=8].index
    p=p[p.region.isin(keep)]
    print(ur,'regions kept',len(keep),sorted(keep))
    print(' sessions',p.s.nunique(),'pops',len(p))
    p=p.assign(area=p.region.map(paula.REGION_AREA))
    print(p.groupby('area').agg(pops=('n','size'),neurons=('n','sum')))
    print(p.groupby('region').agg(pops=('n','size'),neurons=('n','sum')).T.to_string())
EOF
```

```
all regions kept 32 ['APN', 'CA1', 'CA3', 'DG', 'Eth', 'HPF', 'LGd', 'LGv', 'LP', 'MB', 'MGd', 'MGm', 'MGv', 'MRN', 'NB', 'NOT', 'PIL', 'POL', 'POST', 'PoT', 'ProS', 'SCig', 'SGN', 'SUB', 'TH', 'VISal', 'VISam', 'VISl', 'VISp', 'VISpm', 'VISrl', 'ZI']
 sessions 153 pops 2511
      pops  neurons
area               
HP     586    91091
MB     286    35256
TH     551    39370
VIS    888   110527
region     APN    CA1    CA3     DG  Eth   HPF   LGd  LGv    LP    MB   MGd   MGm   MGv   MRN    NB  NOT   PIL   POL  POST   PoT  ProS  SCig   SGN   SUB    TH  VISal  VISam   VISl   VISp  VISpm  VISrl    ZI
pops       127    146    114    141    9    33    50    9    68    84    65    73    82    74    27   15    36    53    50    53    49    43    71    86    44    148    147    144    151    150    148    21
neurons  22257  42687  10489  22411  466  1777  3552  469  4676  6865  3922  4752  7717  7314  1688  678  2073  3624  2820  3892  4586  3319  5162  8098  3038  17442  16919  19508  21567  19772  15319  1117
qc regions kept 27 ['APN', 'CA1', 'CA3', 'DG', 'LGd', 'LP', 'MB', 'MGd', 'MGm', 'MGv', 'MRN', 'NB', 'PIL', 'POL', 'POST', 'PoT', 'ProS', 'SCig', 'SGN', 'SUB', 'TH', 'VISal', 'VISam', 'VISl', 'VISp', 'VISpm', 'VISrl']
 sessions 153 pops 1517
      pops  neurons
area               
HP     325    25359
MB     158     8855
TH     240    11443
VIS    754    44439
region    APN    CA1   CA3    DG   LGd    LP    MB   MGd   MGm   MGv   MRN   NB  PIL  POL  POST  PoT  ProS  SCig   SGN   SUB   TH  VISal  VISam  VISl  VISp  VISpm  VISrl
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/venv/bin/activate && time python - <<'EOF'
import paula, pandas as pd, numpy as np, json, os, h5py, remfile
from concurrent.futures import ThreadPoolExecutor
sess,n=paula.list_sessions()
def s2(a):
    f=h5py.File(remfile.File(paula.s3_url(a)),'r')
    out={'path':a['path'],'desc':f['session_description'][()].decode(),'genotype':f['general/subject/genotype'][()].decode(),
         'subject':f['general/subject/subject_id'][()].decode(),'start':f['session_start_time'][()].decode()}
    md=f['general/metadata']
    out['md']={k:str(md.attrs[k]) for k in md.attrs.keys()}
    out['subj_attrs']={k:str(f['general/subject'][k][()]) for k in f['general/subject'].keys()}
    ni=[k for k in f['intervals'].keys() if k.startswith('Natural')]
    out['ni']=ni; out['intervals']=list(f['intervals'].keys())
    t=f['intervals'][ni[0]]
    blk=t['stimulus_block'][:]; act=t['active'][:]; st=t['start_time'][:]; sp=t['stop_time'][:]
    out['act_dur']=float(sp[act].max()-st[act].min())
    out['nov']=float(np.nanmean(t['is_image_novel'][:])) if 'is_image_novel' in t else None
    s=f['intervals/spontaneous_presentations']; out['spont']=list(zip(s['start_time'][:].tolist(), s['stop_time'][:].tolist()))
    u=f['units']
    q=paula._str(u['quality'][:]); snr=u['snr'][:]; isi=u['isi_violations'][:]; fr=u['firing_rate'][:]
    e=f['general/extracellular_ephys/electrodes']
    loc=pd.Series(paula._str(e['location'][:]), index=e['id'][:]); reg=loc.loc[u['peak_channel_id'][:]].values
    out['good']=pd.Series(reg[q=='good']).value_counts().to_dict()
    out['tut']=pd.Series(reg[(snr>1)&(isi<1)&(fr>0.1)]).value_counts().to_dict()
    out['goodtut']=pd.Series(reg[(snr>1)&(isi<1)&(fr>0.1)&(q=='good')]).value_counts().to_dict()
    out['nprobes']=len([k for k in f['general/extracellular_ephys'].keys() if k.startswith('probe')])
    return out
with ThreadPoolExecutor(8) as ex: res=list(ex.map(s2, sess))
json.dump(res,open(os.environ['TMPDIR']+'/survey2.json','w'))
d=pd.DataFrame(res)
print(d.desc.value_counts()); print(d.genotype.value_counts()); print(d.nprobes.value_counts())
print(d.subject.nunique(), d.act_dur.describe())
print(d.md.iloc[0]); print(d.subj_attrs.iloc[0]); print(d.nov.value_counts())
print(pd.Series([len(x) for x in d.spont]).value_counts())
EOF
```

```
Fri Nov 27 10:17:22 UTC 2026
desc
EPHYS_1_images_G_3uL_reward    74
EPHYS_1_images_H_3uL_reward    71
EPHYS_1_images_G_5uL_reward     4
EPHYS_1_images_H_5uL_reward     4
Name: count, dtype: int64
genotype
Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt    59
wt/wt                                            49
Vip-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt    45
Name: count, dtype: int64
nprobes
6    142
5     10
3      1
Name: count, dtype: int64
81 count     153.000000
mean     3603.866977
std         2.635515
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
import paula, pandas as pd, numpy as np, json, os
r1=json.load(open(os.environ['TMPDIR']+'/survey.json')); r2=json.load(open(os.environ['TMPDIR']+'/survey2.json'))
d=pd.DataFrame(r2)
for k in ['all','qc']: d[k]=[x[k] for x in r1]
d['fam']=d.nov==0
d['G']=d.desc.str.contains('_G_')
target={'VIS':(586,53985),'TH':(313,20541),'HP':(363,42396),'MB':(175,17163)}
subsets={'all':np.ones(len(d),bool),'familiar':d.fam.values,'novel':~d.fam.values,'G':d.G.values,'H':~d.G.values,
 'notVip':~d.genotype.str.startswith('Vip').values,'notwt':~d.genotype.str.startswith('wt').values,'notSst':~d.genotype.str.startswith('Sst').values,'6probes':(d.nprobes==6).values}
def stats(sub,uf):
    rows=[(i,reg,c) for i in np.flatnonzero(sub) for reg,c in d[uf].iat[i].items() if reg in paula.REGION_AREA]
    x=pd.DataFrame(rows,columns=['s','region','n']); p=x[x.n>=30]
    ns=p.groupby('region').s.nunique(); keep=ns[ns>=8].index; p=p[p.region.isin(keep)]
    p=p.assign(area=p.region.map(paula.REGION_AREA)); g=p.groupby('area').n.agg(['size','sum'])
    return p.s.nunique(), len(keep), {a:(int(g.loc[a,'size']),int(g.loc[a,'sum'])) for a in g.index}
for uf in ['all','qc','good','tut','goodtut']:
    for sn,sub in subsets.items():
        print(uf,sn,sub.sum(),stats(sub,uf))
EOF
```

```
all all 153 (153, 26, {'HP': (586, 91091), 'MB': (286, 35256), 'TH': (551, 39370), 'VIS': (888, 110527)})
all familiar 78 (78, 26, {'HP': (312, 50089), 'MB': (156, 20315), 'TH': (303, 22971), 'VIS': (449, 62217)})
all novel 75 (75, 25, {'HP': (274, 41002), 'MB': (126, 14774), 'TH': (248, 16399), 'VIS': (439, 48310)})
all G 78 (78, 26, {'HP': (311, 49926), 'MB': (156, 20350), 'TH': (297, 21734), 'VIS': (453, 60424)})
all H 75 (75, 25, {'HP': (275, 41165), 'MB': (125, 14705), 'TH': (254, 17636), 'VIS': (435, 50103)})
all notVip 108 (108, 26, {'HP': (420, 64634), 'MB': (211, 26668), 'TH': (364, 25678), 'VIS': (626, 78486)})
all notwt 104 (104, 26, {'HP': (401, 61963), 'MB': (195, 24166), 'TH': (372, 27134), 'VIS': (603, 76134)})
all notSst 94 (94, 25, {'HP': (351, 55585), 'MB': (159, 19368), 'TH': (366, 25928), 'VIS': (547, 66434)})
all 6probes 142 (142, 26, {'HP': (547, 84535), 'MB': (269, 33542), 'TH': (520, 37132), 'VIS': (838, 103298)})
qc all 153 (153, 25, {'HP': (325, 25359), 'MB': (158, 8855), 'TH': (240, 11443), 'VIS': (754, 44439)})
qc familiar 78 (78, 22, {'HP': (192, 14526), 'MB': (90, 5432), 'TH': (130, 6503), 'VIS': (403, 25713)})
qc novel 75 (75, 20, {'HP': (132, 10799), 'MB': (56, 2957), 'TH': (92, 4130), 'VIS': (351, 18726)})
qc G 78 (78, 22, {'HP': (189, 14422), 'MB': (90, 5403), 'TH': (125, 6079), 'VIS': (395, 24496)})
qc H 75 (75, 20, {'HP': (136, 10937), 'MB': (56, 2972), 'TH': (98, 4594), 'VIS': (359, 19943)})
qc notVip 108 (108, 22, {'HP': (228, 17953), 'MB': (118, 6787), 'TH': (156, 7423), 'VIS': (534, 32190)})
qc notwt 104 (104, 23, {'HP': (214, 16649), 'MB': (106, 6032), 'TH': (163, 7838), 'VIS': (517, 30197)})
qc notSst 94 (94, 22, {'HP': (190, 15480), 'MB': (84, 4570), 'TH': (145, 6993), 'VIS': (457, 26491)})
qc 6probes 142 (142, 24, {'HP': (301, 23352), 'MB': (143, 8138), 'TH': (223, 10659), 'VIS': (708, 41393)})
good all 153 (153, 26, {'HP': (548, 66217), 'MB': (263, 28871), 'TH': (513, 34209), 'VIS': (883, 96319)})
good familiar 78 (78, 26
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
src=open('paula.py').read()
a=src.index('def shuffle_isi(t, own, rng):'); b=src.index('def rate(t, n_units')
src=src[:a]+'''def group_by_unit(t, own):
    """Spike times regrouped by unit (each unit's spikes in time order) and group bounds."""
    o = np.argsort(own, kind="stable")
    ts, os_ = t[o], own[o]
    bounds = np.flatnonzero(np.r_[True, os_[1:] != os_[:-1], True])
    return ts, bounds


def shuffle_isi(grouped, rng):
    """Each unit's interspike intervals shuffled independently, its first spike kept in place
    (Methods II.E; the start is the claims file's standard choice)."""
    ts, bounds = grouped
    out = np.empty_like(ts)
    for i in range(len(bounds) - 1):
        x = ts[bounds[i]:bounds[i + 1]]
        d = np.diff(x)
        rng.shuffle(d)
        out[bounds[i]] = x[0]
        out[bounds[i] + 1:bounds[i + 1]] = x[0] + np.cumsum(d)
    return out


'''+src[b:]
src=src.replace('''def window_measures(t, own, n_units, surr_rngs, do_corr):
    """All measures of one 100-s window of a population (t in 0..100 s, own in 0..N-1)."""
    r = rate(t, n_units)
    cv10 = cv_windows(r)
    h, c = bandt_pompe(r)
    out = {"cv": np.nanmean(cv10) if np.isfinite(cv10).any() else np.nan, "H": h, "C": c,
           "rate": len(t) / (n_units * WIN), "cv10": cv10}
    for bw, d, tau in ROBUST:''','''def window_measures(t, own, n_units, surr_rngs, do_corr, full=True):
    """All measures of one 100-s window of a population (t in 0..100 s, own in 0..N-1).
    With full False, only CV, H, C and the surrogate (the unit-selection variant)."""
    r = rate(t, n_units)
    cv10 = cv_windows(r)
    h, c = bandt_pompe(r)
    out = {"cv": np.nanmean(cv10) if np.isfinite(cv10).any() else np.nan, "H": h, "C": c,
           "rate": len(t) / (n_units * WIN), "cv10": cv10}
    grouped = group_by_unit(t, own) if len(t) else None
    for bw, d, tau in (ROBUST if full else []):''')
src=src.replace('''    if do_corr:
        out["corr50"]''','''    if do_corr and full:
        out["corr50"]''')
src=src.replace('''        ts = shuffle_isi(t, own, rng)
        ts = ts[(ts >= 0) & (ts < WIN)]''','''        ts = shuffle_isi(grouped, rng) if grouped is not None else t
        ts = ts[(ts >= 0) & (ts < WIN)]''')
src=src.replace('''                nseeds = 5 if cond == "active" else 1''','''                full = ur == "all"
                nseeds = 5 if (cond == "active" and full) else 1''')
src=src.replace('''                m = window_measures(t, ow, n, rngs, do_corr)''','''                m = window_measures(t, ow, n, rngs, do_corr, full)''')
open('paula.py','w').write(src)
EOF
python - <<'EOF'
import paula, pickle, os, time, numpy as np, pandas as pd, resource
d=pickle.load(open(os.environ['TMPDIR']+'/sess.pkl','rb'))
t=time.time()
meta,df,cv=paula.compute_session(149,*d)
print(time.time()-t, df.shape, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
old=pd.read_pickle(os.environ['TMPDIR']+'/two.pkl')
m=df.merge(old,on=['units','region','condition','reading','k'],suffixes=('','_o'))
for c in ['cv','C','H','corr50','s_cv','s_C']: print(c, np.nanmax(np.abs(m[c]-m[c+'_o'])), m[c].median(), m[c+'_o'].median())
print({k:v for k,v in meta.items() if 'clock' in k or 'n_' in k})
EOF
```

```
31.52568554878235 (1792, 42) 1.238096
cv 0.0 0.4236795276297656 0.4236795276297656
C 0.0 0.13096753547524606 0.13096753547524606
H 0.0 0.9469018302090795 0.9469018302090795
corr50 0.0 0.02746310457587242 0.030147509649395943
s_cv 0.02841420591030025 0.23806521507861356 0.23725810346365078
s_C 0.0397645864475059 0.09347550218792011 0.09384474078224425
{'session_description': 'EPHYS_1_images_H_3uL_reward', 'session_start_time': '2021-11-10T23:08:35+00:00', 'n_units': 2274, 'n_spikes': 112286348, 'session_index': 149, 'clock_true': 272.3887919755779, 'clock_shift': -23.97187091146969, 'clock_omitted': 5.391705069124424, 'n_vis_units_clock': 851, 'region_counts_all': {'CA1': 482, 'VISp': 200, 'DG': 175, 'VISl': 152, 'VISpm': 141, 'VISam': 135, 'VISal': 124, 'CA3': 123, 'MGv': 117, 'VISrl': 99, 'SUB': 87, 'PIL': 73, 'MGm': 64, 'PoT': 54, 'APN': 51, 'ProS': 50, 'MB': 40, 'MGd': 28, 'SCig': 26, 'TH': 26, 'LP': 19, 'MRN': 8}, 'region_counts_qc': {'CA1': 203, 'VISp': 93, 'VISam': 66, 'VISpm': 66, 'VISl': 62, 'DG': 58, 'VISal': 56, 'CA3': 51, 'MGv': 47, 'PIL': 41, 'VISrl': 39, 'SUB': 32, 'APN': 27, 'ProS': 22, 'MB': 17, 'SCig': 14, 'TH': 12, 'PoT': 12, 'MGm': 11, 'LP': 10, 'MGd': 4, 'MRN': 1}, 'n_flashes': 4586, 'n_omitted': 217, 'n_changes': 288, 'n_images': 8, 'n_active_windows': 36, 'n_spont_windows': 2}
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' 2>&1 | tail -22
import paula, pickle, os, cProfile, pstats
d=pickle.load(open(os.environ['TMPDIR']+'/sess.pkl','rb'))
cProfile.run('paula.compute_session(149,*d)', os.environ['TMPDIR']+'/prof')
pstats.Stats(os.environ['TMPDIR']+'/prof').sort_stats('tottime').print_stats(14)
EOF
```

```
7818649 function calls (7815668 primitive calls) in 35.472 seconds

   Ordered by: internal time
   List reduced from 521 to 14 due to restriction <14>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    13502    8.734    0.001    8.734    0.001 {method 'argsort' of 'numpy.ndarray' objects}
     4096    6.836    0.002   12.714    0.003 entries/paula-2026/paula.py:201(shuffle_isi)
       28    2.946    0.105    4.076    0.146 entries/paula-2026/paula.py:372(concat_windows)
   471114    2.670    0.000    3.052    0.000 /tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py:1414(diff)
   460778    1.867    0.000    1.867    0.000 {method 'cumsum' of 'numpy.ndarray' objects}
     8960    1.478    0.000    1.822    0.000 entries/paula-2026/paula.py:215(rate)
    90953    1.410    0.000    1.410    0.000 {method 'reduce' of 'numpy.ufunc' objects}
      896    1.099    0.001    2.202    0.002 entries/paula-2026/paula.py:221(mean_corr)
     1188    0.900    0.001    0.900    0.001 {method 'searchsorted' of 'numpy.ndarray' objects}
        1    0.710    0.710   35.469   35.469 entries/paula-2026/paula.py:435(compute_session)
    11008    0.690    0.000    4.828    0.000 entries/paula-2026/paula.py:119(bandt_pompe)
    11091    0.601    0.000    0.601    0.000 {method 'astype' of 'numpy.ndarray' objects}
    11009    0.458    0.000    0.458    0.000 {method 'sort' of 'numpy.ndarray' objects}
     1792    0.420    0.000    4.294    0.002 entries/paula-2026/paula.py:193(group_by_unit)
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
src=open('paula.py').read()
src=src.replace('''import json
import math
import zlib

import h5py''','''import math
import os
import time
import zlib

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")  # many small fits run in parallel processes

import h5py''')
src+='''

def _safe(args):
    for attempt in range(4):
        try:
            return process_session(args)
        except Exception as exc:  # network errors: retry, then report the failure
            err = repr(exc)
            time.sleep(10 * (attempt + 1))
    return {"session_index": args[0], "path": args[1]["path"], "error": err}, None, None


def run_all(assets, workers=4):
    """Process every session in parallel processes; returns the session table, the window
    table and the 10-s CV series of the active windows, and the sessions that failed."""
    import multiprocessing as mp
    from concurrent.futures import ProcessPoolExecutor
    metas, dfs, cv10, failed = [], [], [], []
    ctx = mp.get_context("fork")
    with ProcessPoolExecutor(workers, mp_context=ctx) as ex:
        for meta, df, c in ex.map(_safe, list(enumerate(assets))):
            if df is None:
                failed.append(meta)
                continue
            metas.append(meta)
            dfs.append(df)
            cv10 += c
    return pd.DataFrame(metas), pd.concat(dfs, ignore_index=True), cv10, failed
'''
open('paula.py','w').write(src)
EOF
python -c "
import pandas as pd,os
df=pd.read_pickle(os.environ['TMPDIR']+'/two.pkl')
print(df.groupby(['condition','reading']).series_length.describe())"
```

```
count        mean  ...         75%        max
condition reading                      ...                       
active    -        1008.0  100.000000  ...  100.000000  100.00000
blanks    a         224.0  286.608737  ...  300.750000  329.46748
          b         224.0  272.985769  ...  286.125000  317.96748
images    -         224.0  143.478282  ...  150.500845  164.92123
spont     a          56.0  100.000000  ...  100.000000  100.00000
          b          56.0  100.000000  ...  100.000000  100.00000

[6 rows x 8 columns]
```

**Agent**

Running the full extraction over all 153 sessions now (development copy in scratch; the notebook will redo it from the archive).

**Agent calls Bash**

```bash
date -u; cd entries/paula-2026 && . $TMPDIR/venv/bin/activate && /usr/bin/time -v python - <<'EOF' 2>&1 | egrep -v "^\s+(Page|Volun|Invol|Swap|File|Socket|Signal|Average|Exit|Minor|Major|Percent|System|User)" 
import paula, time, pickle, os
t=time.time()
sess,n=paula.list_sessions()
metas,df,cv10,failed=paula.run_all(sess,4)
print('time',time.time()-t,'failed',failed, df.shape)
pickle.dump((metas,df,cv10,failed),open(os.environ['TMPDIR']+'/full.pkl','wb'))
EOF
date -u
```

```
Fri Nov 27 10:25:03 UTC 2026
time 2115.3830845355988 failed [] (241909, 42)
	Command being timed: "python -"
	Elapsed (wall clock) time (h:mm:ss or m:ss): 35:17.41
	Maximum resident set size (kbytes): 2698424
Fri Nov 27 11:00:20 UTC 2026
```

**Agent**

Full extraction done in 35 min, no failures, peak 2.7 GB per process. Now checking the entry tooling requirements before writing the notebook.

**Agent calls Bash**

```bash
cd  && python tools/entry.py --help 2>&1 | head -30; grep -n "def check\|sanity\|claim:\|install\|tags\|runtime_minutes\|embedded\|literal" tools/entry.py | head -60
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

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
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 370,480p tools/entry.py; grep -n "timeout\|max_minutes\|MAX_MIN" tools/entry.py | head -20
```

```
if f.get("versions") or f.get("fixed_in"):
                if about != "data":
                    report.error(where, f"finding {n}: `versions` and `fixed_in` are for a finding about the data")
                elif len(f.get("datasets") or used) > 1:
                    report.error(where, f"finding {n}: `versions` and `fixed_in` name versions of one dataset; give "
                                        f"the finding the one dataset they are of (`datasets:`)")
                if f.get("fixed_in") in (f.get("versions") or []):
                    report.error(where, f"finding {n}: version {f['fixed_in']} is both one it was seen in and the "
                                        f"one it was fixed in")
            # The code that shows a finding: a tagged cell of one of the entry's notebooks, as for an outcome. From
            # pilot-19 a critical or major finding about the data names its cell; an earlier attempt was not asked.
            shown, tag = f.get("notebook"), f.get("output")
            if bool(shown) != bool(tag):
                report.error(where, f"finding {n}: give the notebook that shows it and its cell together "
                                    f"(`notebook` and `output`)")
            if (version and int(version[1]) >= 19 and about == "data" and f.get("severity") in ("critical", "major")
                    and not shown):
                report.error(where, f"finding {n}: it is {f['severity']}; name the notebook and the tagged cell whose "
                                    f"output shows it (`notebook`, `output`)")
            # As for an outcome, only the latest attempt's cells are checked against the entry as it is now.
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "max-minutes\|max_minutes\", type\|default=" tools/entry.py | head; grep -n "python" entries/fouke-2025/entry.yaml; cat entries/fouke-2025/README.md | head -30
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
258:                                                  default="")
731:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
732:    parser.add_argument("--max-minutes", type=float, default=60,
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
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && . $TMPDIR/venv/bin/activate && python - <<'EOF'
import pickle, os, pandas as pd, numpy as np, paula
metas,df,cv10,failed=pickle.load(open(os.environ['TMPDIR']+'/full.pkl','rb'))
print(metas.columns.tolist())
print(metas[['clock_true','clock_shift','clock_omitted','n_active_windows','n_spont_windows','n_images']].describe().T)
# duplicates
fp=metas.fingerprint.apply(tuple); print('dup fingerprints', fp.duplicated().sum(), metas.n_spikes.duplicated().sum())
d=df[df.units=='all']
pops=d[d.condition=='active'].groupby(['session','region']).size()
print('pops',len(pops))
print(d.groupby(['condition','reading']).size())
pd.set_option('display.width',250)
med=d.groupby(['area','region','condition','reading']).cv.median().unstack([2,3]).round(3)
print(med)
medc=d.groupby(['area','region','condition','reading']).C.median().unstack([2,3]).round(3)
print(medc)
EOF
```

```
['path', 'session_description', 'subject', 'genotype', 'session_start_time', 'n_units', 'n_spikes', 'image_table', 'spont_epochs', 'active_start', 'active_end', 'cutoff', 'fingerprint', 'session_index', 'clock_true', 'clock_shift', 'clock_omitted', 'n_vis_units_clock', 'region_counts_all', 'region_counts_qc', 'n_flashes', 'n_omitted', 'n_changes', 'n_images', 'n_active_windows', 'n_spont_windows']
                  count        mean  ...         75%         max
clock_true        153.0  223.659321  ...  272.388792  433.780662
clock_shift       153.0  -62.591997  ...  -30.569948    1.610378
clock_omitted     153.0    3.314345  ...    5.474490   92.611399
n_active_windows  153.0   35.986928  ...   36.000000   36.000000
n_spont_windows   153.0    2.000000  ...    2.000000    2.000000
n_images          153.0    8.000000  ...    8.000000    8.000000

[6 rows x 8 columns]
dup fingerprints 0 0
pops 2311
condition  reading
active     -          83166
blanks     a          18488
           b          18488
images     -          18155
spont      a           4622
           b           4622
dtype: int64
[... 58 more lines not kept]
```

**Agent**

Results look close to the paper on several claims (e.g. VIS complexity in natural images 0.16 to 0.27 vs the paper's 0.16 to 0.26). Reading the supplement's reference-system definitions for fig3a.

**Agent calls Bash**

```bash
grep -n "Supplemental\|SUPPLEMENT\|I\. \|Sec. I\|white noise\|logistic\|Ikeda\|tent\|1/f\|alpha\|α" paper/10.1103-wndc-k654.txt 2>/dev/null | head -5; cd  grep -n "Ikeda\|logistic\|tent map\|K =\|kernel" paper/10.1103-wndc-k654.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-wndc-k654.txt",
 "offset": 1515,
 "limit": 110
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now writing the notebook. I'll author it as a cell-delimited script and convert it with nbformat.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "\"\"\"Build the notebook from a cell-delimited source: '# %% md' or '# %% code tag1,tag2'.\"\"\"\nimport sys, nbformat\nsrc = open(sys.argv[1]).read()\nout = sys.argv[2]\ndev = len(sys.argv) > 3\ncells = []\nfor block in src.split(\"\\n# %% \")[1:]:\n    head, _, body = block.partition(\"\\n\")\n    parts = head.split()\n    kind = parts[0]\n    tags = parts[1].split(\",\") if len(parts) > 1 else []\n    body = body.strip(\"\\n\")\n    if kind == \"md\":\n        body = \"\\n\".join(l[2:] if l.startswith(\"# \") else l[1:] if l.startswith(\"#\") else l for l in body.split(\"\\n\"))\n        cells.append(nbformat.v4.new_markdown_cell(body))\n    else:\n        if dev and \"extract\" in tags:\n            body = \"import pickle, os\\nmetas, windows, cv10_list, failed = pickle.load(open(os.environ['TMPDIR'] + '/full.pkl', 'rb'))\\nsessions, n_assets = paula.list_sessions()\\nimport time; t_extract = 0.0\"\n        c = nbformat.v4.new_code_cell(body)\n        tags = [t for t in tags if t != \"extract\"]\n        if tags:\n            c.metadata[\"tags\"] = tags\n        cells.append(c)\nnb = nbformat.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbformat.write(nb, out)\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> entries/paula-2026/paula.py <<'EOF'


# ---------------------------------------------------------------- analysis helpers

CONDITIONS = ["images", "active", "blanks", "spont"]
COND_PAIRS = [("images", "active"), ("images", "blanks"), ("images", "spont"),
              ("active", "blanks"), ("active", "spont"), ("blanks", "spont")]


def conditions(windows, units="all", blanks="a", spont="a"):
    """The windows of the four conditions under one unit reading and one condition reading
    (blank reading 'a' or 'b', spontaneous reading 'a' or 'b'; claims file, opening comment)."""
    w = windows[windows.units == units]
    keep = ((w.condition == "active") | (w.condition == "images")
            | ((w.condition == "blanks") & (w.reading == blanks))
            | ((w.condition == "spont") & (w.reading == spont)))
    return w[keep]


def kept_regions(windows, units="all"):
    """Subregions with populations of at least 30 units in at least eight sessions
    (Methods II.A)."""
    p = windows[(windows.units == units) & (windows.condition == "active")]
    ns = p.groupby("region").session.nunique()
    return [r for r in REGION_ORDER if ns.get(r, 0) >= MIN_SESSIONS]


def js_matrix(w, value, regions, bins, base=2.0):
    """JS divergence between the distributions of `value` of every pair of subregions."""
    vals = {r: w.loc[w.region == r, value].values for r in regions}
    n = len(regions)
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            m[i, j] = m[j, i] = js_divergence(vals[regions[i]], vals[regions[j]], bins, base)
    return pd.DataFrame(m, index=regions, columns=regions)


def summed_js(m, area, mode):
    """Sum of within-area JS values: mode 'all' every pair of the area's block above its
    diagonal; mode 'adjacent' the block's first off-diagonal (Table I order)."""
    rs = [r for r in m.index if REGION_AREA[r] == area]
    b = m.loc[rs, rs].values
    if mode == "all":
        return float(b[np.triu_indices(len(rs), 1)].sum())
    return float(np.diag(b, 1).sum())


def pct_diff(sa, sb, mode):
    """Percentage difference of two sums: 'second' |A - B| / B, 'mean' |A - B| / mean."""
    return 100 * abs(sa - sb) / (sb if mode == "second" else (sa + sb) / 2)


def trajectory(cv, c, width, min_count):
    """Mean C and its standard error in bins of CV of the given width (Fig. 5 legend)."""
    cv = np.asarray(cv)
    c = np.asarray(c)
    ok = np.isfinite(cv) & np.isfinite(c)
    cv, c = cv[ok], c[ok]
    b = np.floor(cv / width + 1e-9).astype(int)
    rows = []
    for k in np.unique(b):
        x = c[b == k]
        if len(x) < max(min_count, 1):
            continue
        rows.append({"lo": k * width, "hi": (k + 1) * width, "n": len(x), "mean": x.mean(),
                     "se": x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else 0.0})
    return pd.DataFrame(rows)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb.py",
 "content": "\n# %% md\n# # Reproducing de Paula et al. (2026) from DANDI:000713\n#\n# **Paper.** E. V. de Paula, R. M. Jungmann, A. J. Fontenele, L. A. A. Aguiar, P. V. Carelli, F. S. Matias, M. Copelli and N. A. P. de Vasconcelos, \"Revealing Stimulus-Dependent Dynamics Through Statistical Complexity\", PRX Life 4, 023018 (2026), doi:10.1103/wndc-k654.\n#\n# **Dataset.** DANDI:000713, \"Allen Institute - Visual Behavior - Neuropixels\", version 0.240702.1725 (doi:10.48324/dandi.000713/0.240702.1725). This is the version the paper cites (its Ref. 22, as the claims file gives it), and it is the only published version of the dandiset; the draft has the same 4293 assets and was last modified on 2024-07-02, when this version was published. The 153 ecephys session files are streamed from the archive; nothing is written to disk.\n#\n# **Text.** The claims file `claims/paula-2026.yaml` was written from the version of record (corrected 22 July 2026) and its Supplemental Material. The paper links no analysis code.\n#\n# **Claims.** All 35 claims of the claims file are tested here; none is blocked. Claim `fig3a-reference-systems` uses synthetic series only (`data: elsewhere`, no recordings). The outcomes are in the attempt record and the summary at the end.\n#\n# **Method.** The helper module `paula.py` reads each session and computes, for every local population (the units of one subregion in one session with at least 30 units) and every 100-s window of the four conditions, the CV, the permutation entropy H and the statistical complexity C of the population rate, the same for an ISI-shuffled surrogate, the mean pairwise correlation (visual cortex and midbrain), and C and H for the parameter combinations of the supplement. Its docstring says where each parameter comes from. Every claim's section below starts from that table.\n\n# %% code\nimport time, zlib, warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport paula\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nprint(\"dandiset\", paula.DANDISET, \"version\", paula.VERSION)\n\n# %% md\n# ## Loading\n#\n# One pass over all ecephys sessions, four sessions at a time in separate processes. Each session's spike times are read up to the end of its spontaneous epoch. This takes about 35 minutes.\n\n# %% code extract\nt0 = time.time()\nsessions, n_assets = paula.list_sessions()\nmetas, windows, cv10_list, failed = paula.run_all(sessions, workers=4)\nt_extract = time.time() - t0\nprint(f\"{len(sessions)} session files of {n_assets} assets; extraction took {t_extract / 60:.1f} min\")\n\n# %% code sanity\nimport resource\nprint(\"sessions read:\", len(metas), \"failed:\", len(failed), failed)\nprint(\"subjects:\", metas.subject.nunique(), \"| session types:\", metas.session_description.value_counts().to_dict())\nprint(\"genotypes:\", metas.genotype.value_counts().to_dict())\nprint(\"units per session: median\", metas.n_units.median(), \"range\", metas.n_units.min(), \"to\", metas.n_units.max())\nprint(\"active block length (s):\", (metas.active_end - metas.active_start).describe().round(1).to_dict())\nprint(\"active windows per session:\", metas.n_active_windows.value_counts().to_dict())\nprint(\"spontaneous epochs after the task (s):\", pd.Series([e[-1][1] - e[-1][0] for e in metas.spont_epochs]).describe().round(1).to_dict())\nprint(\"images per session:\", metas.n_images.value_counts().to_dict(), \"| flashes shown per session: median\", metas.n_flashes.median(),\n      \"| omitted: median\", metas.n_omitted.median(), \"| change flashes: median\", metas.n_changes.median())\nsl = windows[windows.units == \"all\"].groupby([\"condition\", \"reading\"]).series_length.describe()[[\"min\", \"50%\", \"max\"]].round(1)\nprint(\"length of the series each window is cut from (s):\\n\", sl)\nprint(\"window rows by unit reading and condition:\\n\", windows.groupby([\"units\", \"condition\", \"reading\"]).size())\nfor col, unit in [(\"cv\", \"\"), (\"H\", \"\"), (\"C\", \"\"), (\"rate\", \"spikes/s per unit\"), (\"corr50\", \"\"), (\"corr20\", \"\")]:\n    x = windows[col]\n    print(f\"{col}: {np.nanmin(x):.3f} to {np.nanmax(x):.3f} {unit}, NaN {int(x.isna().sum())}\")\n# recordings deposited more than once: identical spike-time fingerprints or spike counts\nfp = metas.fingerprint.apply(lambda v: tuple(np.round(v, 6)))\nprint(\"sessions sharing a spike-time fingerprint:\", int(fp.duplicated(keep=False).sum()),\n      \"| sharing a total spike count:\", int(metas.n_spikes.duplicated(keep=False).sum()),\n      \"| sharing subject and start time:\", int(metas.duplicated([\"subject\", \"session_start_time\"], keep=False).sum()))\nprint(\"peak memory of this process (GB):\", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)\n\n# %% md\n# ### Clock check\n#\n# The stimulus table and the spike times must share a clock. For every session the notebook counts the visual cortex spikes 30 to 130 ms after each flash onset minus those in the 100 ms before, for the true onsets and for onsets shifted by 375 ms into the gray screen, and for the omitted flashes (no image appears, so no response is expected).\n\n# %% code sanity\ncl = metas[[\"clock_true\", \"clock_shift\", \"clock_omitted\", \"n_vis_units_clock\"]]\nprint(cl.describe().round(2))\nprint(\"sessions where the response to true onsets exceeds that to shifted onsets:\", int((cl.clock_true > cl.clock_shift).sum()), \"of\", len(cl))\nprint(\"sessions where the true-onset response exceeds the omitted-flash response:\", int((cl.clock_true > cl.clock_omitted).sum()), \"of\", len(cl))\nprint(\"smallest true-onset contrast:\", round(cl.clock_true.min(), 2), \"| largest shifted contrast:\", round(cl.clock_shift.max(), 2))\n\n# %% md\n# ## table1-sample\n#\n# > The analysis rests on 102 sessions and 1437 local populations (VIS 586, TH 313, HP 363, MB 175), with 53 985 visual cortex, 20 541 thalamic, 42 396 hippocampal and 17 163 midbrain neurons, and 77 216 analysis windows (11 321 natural images, 51 704 active behavior, 11 321 blanks, 2870 spontaneous).\n#\n# Counts under each unit reading ('all' units; 'qc', ISI violations < 0.5, amplitude cutoff < 0.1, presence ratio > 0.9) and each session reading ((a) sessions with at least one kept population; (b) those that also have the spontaneous gray-screen epoch). The selection rule (at least 30 units, in at least eight sessions) is also applied to every location label of the files, to see which labels it keeps beyond Table I.\n\n# %% code claim:table1-sample\nTABLE1 = {\"VISal\": 8572, \"VISam\": 8566, \"VISl\": 9255, \"VISp\": 10010, \"VISpm\": 10250, \"VISrl\": 7332,\n          \"LGd\": 2169, \"LP\": 2795, \"MGd\": 2497, \"MGm\": 1928, \"MGv\": 4492, \"PIL\": 868, \"POL\": 1298, \"PoT\": 1461, \"SGN\": 3033,\n          \"CA1\": 22399, \"CA3\": 3729, \"DG\": 7486, \"POST\": 1367, \"ProS\": 3067, \"SUB\": 4348,\n          \"APN\": 10716, \"NB\": 793, \"NOT\": 309, \"MRN\": 3661, \"SCig\": 1684}\nEXP1 = {\"sessions\": 102, \"VIS populations\": 586, \"TH populations\": 313, \"HP populations\": 363, \"MB populations\": 175,\n        \"VIS neurons\": 53985, \"TH neurons\": 20541, \"HP neurons\": 42396, \"MB neurons\": 17163,\n        \"natural image windows\": 11321, \"active behavior windows\": 51704, \"blank windows\": 11321, \"spontaneous windows\": 2870}\nhas_spont = set(metas.session_index[metas.n_spont_windows >= 2])\n# labels kept by the rule over all location labels, from the unit counts of each session\nfor ur in [\"all\", \"qc\"]:\n    rows = [(m.session_index, r, c) for m in metas.itertuples() for r, c in getattr(m, f\"region_counts_{ur}\").items()]\n    rc = pd.DataFrame(rows, columns=[\"session\", \"region\", \"n\"])\n    rc = rc[rc.n >= paula.MIN_UNITS]\n    ns = rc.groupby(\"region\").session.nunique()\n    lab = sorted(ns[ns >= paula.MIN_SESSIONS].index)\n    print(f\"units={ur}: labels kept by the rule: {len(lab)}; not in Table I: {[l for l in lab if l not in paula.REGION_AREA]};\",\n          f\"Table I subregions not kept: {[r for r in paula.REGION_ORDER if r not in lab]}\")\nt1 = {}\nfor ur in [\"all\", \"qc\"]:\n    regs = paula.kept_regions(windows, ur)\n    for sr in [\"a\", \"b\"]:\n        w = paula.conditions(windows, ur, \"a\", \"a\")\n        w = w[w.region.isin(regs)]\n        if sr == \"b\":\n            w = w[w.session.isin(has_spont)]\n        pops = w[w.condition == \"active\"].drop_duplicates([\"session\", \"region\"])\n        res = {\"sessions\": pops.session.nunique()}\n        for a in paula.AREAS:\n            res[f\"{a} populations\"] = int((pops.area == a).sum())\n        for a in paula.AREAS:\n            res[f\"{a} neurons\"] = int(pops.loc[pops.area == a, \"n\"].sum())\n        res[\"natural image windows\"] = int((w.condition == \"images\").sum())\n        res[\"active behavior windows\"] = int((w.condition == \"active\").sum())\n        res[\"blank windows\"] = int((w.condition == \"blanks\").sum())\n        res[\"spontaneous windows\"] = int((w.condition == \"spont\").sum())\n        t1[(ur, sr)] = res\n        if sr == \"a\":\n            per = pops.groupby(\"region\").agg(populations=(\"n\", \"size\"), neurons=(\"n\", \"sum\")).reindex(paula.REGION_ORDER)\n            per[\"Table I neurons\"] = pd.Series(TABLE1)\n            per[\"ratio\"] = (per.neurons / per[\"Table I neurons\"]).round(2)\n            print(f\"\\nunits={ur}: per subregion (kept regions: {len(regs)})\\n\", per.T.to_string())\ntab = pd.DataFrame(t1)\ntab[\"expected\"] = pd.Series(EXP1)\ntab[\"tolerance\"] = tab[\"expected\"] * 0.1\nfor c in t1:\n    tab[(\"within\", *c)] = (tab[c] - tab[\"expected\"]).abs() <= tab[\"tolerance\"]\nprint(tab.to_string())\nfor c in t1:\n    print(c, \"all within tolerance:\", bool(tab[(\"within\", *c)].all()))\n# windows per population and session reading do not depend on the blank or spontaneous reading\nprint(\"blank windows under reading b:\", int((paula.conditions(windows, \"all\", \"b\", \"b\").condition == \"blanks\").sum()))\n\n# %% md\n# **Result: not reproduced.** Under neither unit reading nor either session reading do the counts match: every one of the 153 ecephys sessions of the dandiset has kept populations and a spontaneous epoch, so both session readings give 153 sessions, not 102, and the population and window counts are about 1.5 times the paper's under the 'all' reading. The 'all' reading keeps exactly the 26 subregions of Table I among the labels of Table I (the rule also keeps six labels Table I does not list), while 'qc' drops at least one of them. Neuron counts per population are larger than Table I's under 'all' and smaller under 'qc' (ratios printed above). The 'all' reading is adopted by the other claims as an assumption (it keeps Table I's subregion list and is the closer of the two), with 'qc' shown as a variant where it bears on a claim.\n\n# %% md\n# ### Readings used below\n#\n# The unit reading is 'all' (assumption, above). The four condition readings combine the blank reading (a: after every shown flash; b: only after flashes followed by another flash) with the spontaneous reading (a: the first two 100-s windows of the gray screen; b: two windows centred in it). They are written `blanks/spont`, for example `a/b`.\n\n# %% code\nREG = paula.kept_regions(windows, \"all\")\nCR = [(\"a\", \"a\"), (\"a\", \"b\"), (\"b\", \"a\"), (\"b\", \"b\")]\nW = {f\"{b}/{s}\": paula.conditions(windows, \"all\", b, s).query(\"region in @REG\") for b, s in CR}\nWQ = {f\"{b}/{s}\": paula.conditions(windows, \"qc\", b, s).query(\"region in @paula.kept_regions(windows, 'qc')\") for b, s in CR}\nACT = W[\"a/a\"][W[\"a/a\"].condition == \"active\"]\nACTQ = WQ[\"a/a\"][WQ[\"a/a\"].condition == \"active\"]\nprint(len(REG), \"subregions;\", ACT.drop_duplicates([\"session\", \"region\"]).shape[0], \"populations; active windows\", len(ACT))\n\ndef within(x, lo, hi):\n    return (x >= lo - 1e-12) & (x <= hi + 1e-12)\n\ndef widen(lo, hi):\n    return lo - 0.1 * abs(lo), hi + 0.1 * abs(hi)\n\ndef tol(x, v, t):\n    return abs(x - v) <= t + 1e-12\n\n# %% md\n# ## fig1c-cv-region-medians\n#\n# > During active behavior visual cortex subregions have the highest population CV (medians 0.40 to 0.59), thalamic subregions moderate (0.27 to 0.37), hippocampal subregions high (0.25 to 0.49, dentate gyrus highest at 0.49) and midbrain the lowest (0.16 to 0.45).\n\n# %% code claim:fig1c-cv-region-medians\nRANGES_CV = {\"VIS\": (0.40, 0.59), \"TH\": (0.27, 0.37), \"HP\": (0.25, 0.49), \"MB\": (0.16, 0.45)}\nIQR_CV = {\"VIS\": (0.12, 0.18), \"TH\": (0.10, 0.15), \"HP\": (0.08, 0.13), \"MB\": (0.05, 0.23)}\n\ndef cv_medians(act):\n    g = act.groupby(\"region\").cv\n    t = pd.DataFrame({\"median\": g.median(), \"iqr\": g.quantile(0.75) - g.quantile(0.25), \"windows\": g.size()}).reindex(REG_OF(act))\n    t[\"area\"] = [paula.REGION_AREA[r] for r in t.index]\n    return t\n\ndef REG_OF(d):\n    return [r for r in paula.REGION_ORDER if r in set(d.region)]\n\ndef judge_fig1c(t, label):\n    ok_all, ok_iqr = True, True\n    for a, (lo, hi) in RANGES_CV.items():\n        x = t[t.area == a]\n        wl, wh = widen(lo, hi)\n        inside = within(x[\"median\"], wl, wh)\n        ext = tol(x[\"median\"].min(), lo, 0.1 * lo) and tol(x[\"median\"].max(), hi, 0.1 * hi)\n        il, ih = widen(*IQR_CV[a])\n        iqr_in = within(x[\"iqr\"], il, ih)\n        print(f\"{label} {a}: medians {x['median'].min():.3f} to {x['median'].max():.3f} (expected {lo} to {hi}); inside widened range {int(inside.sum())}/{len(x)}; \"\n              f\"extremes within tolerance {ext}; IQR {x['iqr'].min():.3f} to {x['iqr'].max():.3f}, inside {int(iqr_in.sum())}/{len(x)}\")\n        ok_all &= bool(inside.all()) and ext\n        ok_iqr &= bool(iqr_in.all())\n    hp = t[t.area == \"HP\"][\"median\"]\n    print(f\"{label}: highest hippocampal median is {hp.idxmax()} ({hp.max():.3f}); medians and extremes all match: {ok_all}; IQRs all match: {ok_iqr}\")\n    return ok_all and hp.idxmax() == \"DG\", ok_iqr\n\nt = cv_medians(ACT)\nprint(t.round(3).T.to_string())\nres_main = judge_fig1c(t, \"units=all\")\ntq = cv_medians(ACTQ)\nprint(tq.round(3).T.to_string())\nres_q = judge_fig1c(tq, \"units=qc (variant)\")\n# by session group: the paper's sessions are not identified, so the result is also given for familiar and novel image sets\nfam = set(metas.session_index[metas.session_description.str.contains(\"_G_\")])\nfor name, ss in [(\"image set G\", fam), (\"image set H\", set(metas.session_index) - fam)]:\n    x = ACT[ACT.session.isin(ss)].groupby(\"area\").cv.median()\n    print(name, \"area medians:\", x.round(3).to_dict())\n\n# %% md\n# **Result: ...**\n\n# %% md\n# ## fig1c-cv-above-surrogate\n#\n# > Empirical CV exceeds that of ISI-shuffled surrogates in every brain region (VIS 2 to 3 times, surrogate medians 0.21 to 0.24; TH 1.3 to 1.6; HP 1.5 to 2.2; MB 1.3 to 1.9), with Mann-Whitney p < 0.001 for all regions.\n#\n# One surrogate per active window (Methods II.E). The surrogate is drawn under the seed of this claim, `zlib.crc32(b\"paula-2026/fig1c-cv-above-surrogate\")`, and under that seed plus 1000, 2000, 3000 and 4000; the same surrogates serve the claims of Figs. 1d and 3 (see the deviations).\n\n# %% code claim:fig1c-cv-above-surrogate\nRATIO = {\"VIS\": (2, 3), \"TH\": (1.3, 1.6), \"HP\": (1.5, 2.2), \"MB\": (1.3, 1.9)}\nSFX = [\"\", \"_s1000\", \"_s2000\", \"_s3000\", \"_s4000\"]\n\ndef surrogate_check(act, sfx, verbose):\n    g = act.groupby(\"region\")\n    t = pd.DataFrame({\"emp\": g.cv.median(), \"surr\": g[\"s_cv\" + sfx].median()}).reindex(REG_OF(act))\n    t[\"ratio\"] = t.emp / t.surr\n    t[\"area\"] = [paula.REGION_AREA[r] for r in t.index]\n    p_sub = {r: stats.mannwhitneyu(x.cv.dropna(), x[\"s_cv\" + sfx].dropna()).pvalue for r, x in g}\n    t[\"p\"] = pd.Series(p_sub)\n    ok_ratio = True\n    for a, (lo, hi) in RATIO.items():\n        wl, wh = widen(lo, hi)\n        x = t[t.area == a]\n        ok_ratio &= bool(within(x.ratio, wl, wh).all())\n        if verbose:\n            print(f\"{a}: ratios {x.ratio.min():.2f} to {x.ratio.max():.2f} (expected {lo} to {hi}, widened {wl:.2f} to {wh:.2f}); inside {int(within(x.ratio, wl, wh).sum())}/{len(x)}\")\n    vs = t[t.area == \"VIS\"].surr\n    ok_vs = bool(within(vs, 0.189, 0.264).all())\n    pa = {}\n    for a, x in act.groupby(\"area\"):\n        pa[a] = (stats.mannwhitneyu(x.cv.dropna(), x[\"s_cv\" + sfx].dropna()).pvalue, x.cv.median() > x[\"s_cv\" + sfx].median())\n    ok_sub = bool((t.p < 0.001).all() and (t.emp > t.surr).all())\n    ok_area = all(p < 0.001 and hi for p, hi in pa.values())\n    if verbose:\n        print(t.round(4).T.to_string())\n        print(f\"VIS surrogate medians {vs.min():.3f} to {vs.max():.3f} (0.189 to 0.264): {ok_vs}\")\n        print(\"per area Mann-Whitney:\", {a: (f\"{p:.1e}\", bool(h)) for a, (p, h) in pa.items()})\n        print(f\"tests hold per subregion: {ok_sub}; per area: {ok_area}; all ratios inside: {ok_ratio}; largest subregion p {t.p.max():.1e}\")\n    return t, ok_ratio, ok_vs, ok_sub, ok_area\n\nbase = surrogate_check(ACT, \"\", True)\nprint(\"\\nfive seeds (claim seed, +1000, +2000, +3000, +4000):\")\nfor s in SFX:\n    t_, r_, v_, ps_, pa_ = surrogate_check(ACT, s, False)\n    print(f\"seed{s or ' (claim)'}: ratio range {t_.ratio.min():.3f} to {t_.ratio.max():.3f}; VIS surrogate medians {t_[t_.area=='VIS'].surr.min():.4f} to {t_[t_.area=='VIS'].surr.max():.4f}; \"\n          f\"ratios inside {r_}; VIS surrogates inside {v_}; tests per subregion {ps_}, per area {pa_}; largest p {t_.p.max():.1e}\")\nprint(\"\\nvariant units=qc:\")\n_ = surrogate_check(ACTQ, \"\", True)\n\n# %% md\n# **Result: ...**\n\n# %% md\n# ## fig1d-surrogate-abolishes-cv-correlations\n#\n# > Inter-regional correlations of CV time series during active behavior are present in the data and abolished in the ISI-shuffled surrogates.\n#\n# Per pair of subregions recorded in the same session, the Pearson correlation of their 10-s CV series over the active windows (360 values per session at most). Reading (a) concatenates the series of all shared sessions; reading (b) averages the per-session correlations.\n\n# %% code claim:fig1d-surrogate-abolishes-cv-correlations\ncvs = pd.DataFrame(cv10_list)\ncvs = cvs[(cvs.units == \"all\") & cvs.region.isin(REG)].sort_values([\"session\", \"region\", \"k\"])\nseries = {}\nfor (s, r), g in cvs.groupby([\"session\", \"region\"]):\n    series[(s, r)] = (np.concatenate(list(g.cv10)), np.concatenate(list(g.s_cv10)))\nby_sess = {}\nfor (s, r) in series:\n    by_sess.setdefault(s, []).append(r)\n\ndef corr_mats(which):\n    n = len(REG)\n    ca, cb, ns = (np.full((n, n), np.nan) for _ in range(3))\n    for i in range(n):\n        for j in range(i + 1, n):\n            xs, ys, rs = [], [], []\n            for s, rr in by_sess.items():\n                if REG[i] in rr and REG[j] in rr:\n                    x, y = series[(s, REG[i])][which], series[(s, REG[j])][which]\n                    ok = np.isfinite(x) & np.isfinite(y)\n                    if ok.sum() > 2 and x[ok].std() > 0 and y[ok].std() > 0:\n                        xs.append(x[ok]); ys.append(y[ok]); rs.append(np.corrcoef(x[ok], y[ok])[0, 1])\n            if xs:\n                ca[i, j] = ca[j, i] = np.corrcoef(np.concatenate(xs), np.concatenate(ys))[0, 1]\n                cb[i, j] = cb[j, i] = np.mean(rs)\n                ns[i, j] = ns[j, i] = len(rs)\n    f = lambda m: pd.DataFrame(m, index=REG, columns=REG)\n    return f(ca), f(cb), f(ns)\n\nEMP_A, EMP_B, NSH = corr_mats(0)\nSUR_A, SUR_B, _ = corr_mats(1)\niu = np.triu_indices(len(REG), 1)\nprint(\"pairs with at least one shared session:\", int(np.isfinite(EMP_A.values[iu]).sum()), \"of\", len(iu[0]),\n      \"| shared sessions per pair: median\", np.nanmedian(NSH.values[iu]))\nok1d = {}\nfor lab, e, s in [(\"a\", EMP_A, SUR_A), (\"b\", EMP_B, SUR_B)]:\n    ev, sv = e.values[iu], s.values[iu]\n    ev, sv = ev[np.isfinite(ev)], sv[np.isfinite(sv)]\n    q = np.percentile(np.abs(sv), [50, 90, 99, 100])\n    ok1d[lab] = (ev.max() >= 0.45) and (np.abs(sv).max() < 0.2)\n    print(f\"reading {lab}: empirical r {ev.min():.3f} to {ev.max():.3f}, pairs >= 0.45: {int((ev >= 0.45).sum())}; \"\n          f\"surrogate |r| median {q[0]:.3f}, 90th {q[1]:.3f}, 99th {q[2]:.3f}, max {q[3]:.3f}; pairs with |r| > 0.2: {int((np.abs(sv) > 0.2).sum())}; passes {ok1d[lab]}\")\nfig, ax = plt.subplots(1, 2, figsize=(13, 5.5))\nfor a_, (lab, e, s) in zip(ax, [(\"a\", EMP_A, SUR_A), (\"b\", EMP_B, SUR_B)]):\n    m = np.tril(e.values, -1) + np.triu(s.values, 1)\n    im = a_.imshow(m, vmin=-0.7, vmax=0.7, cmap=\"RdBu_r\")\n    a_.set_xticks(range(len(REG)), REG, rotation=90, fontsize=7); a_.set_yticks(range(len(REG)), REG, fontsize=7)\n    a_.set_title(f\"reading {lab}: lower empirical, upper surrogate\")\nplt.colorbar(im, ax=ax); plt.show()\nprint(\"colour scale -0.7 to 0.7; values outside it:\", int((np.abs(np.r_[EMP_A.values[iu], EMP_B.values[iu]]) > 0.7).sum()))\n\n# %% md\n# **Result: ...**\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && . $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/nb.py $TMPDIR/dev.ipynb dev && cp paula.py $TMPDIR/ && cd $TMPDIR && time jupyter nbconvert --to notebook --execute dev.ipynb --output dev_out.ipynb --ExecutePreprocessor.timeout=1800 2>&1 | tail -3 && python - <<'EOF'
import nbformat
nb=nbformat.read('dev_out.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text[-6000:])
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
```

```
Exit code 1
21 cells

[31mValueError[39m: Item must have length equal to number of levels.


real	0m12.049s
user	0m9.634s
sys	0m0.762s
Traceback (most recent call last):
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/tmp/claude-1001/venv/lib/python3.13/site-packages/nbformat/__init__.py", line 171, in read
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
s=s.replace('t1[(ur, sr)] = res','t1[f"{ur}/{sr}"] = res')
s=s.replace('tab[("within", *c)] = (tab[c] - tab["expected"]).abs() <= tab["tolerance"]','tab["within " + c] = (tab[c] - tab["expected"]).abs() <= tab["tolerance"]')
s=s.replace('print(c, "all within tolerance:", bool(tab[("within", *c)].all()))','print(c, "all within tolerance:", bool(tab["within " + c].all()))')
open('nb.py','w').write(s)
EOF
cat > $TMPDIR/dev.sh <<'EOF'
#!/bin/bash
cd entries/paula-2026 && . $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/nb.py $TMPDIR/dev.ipynb dev >/dev/null && cp paula.py $TMPDIR/ && cd $TMPDIR && jupyter nbconvert --to notebook --execute dev.ipynb --output dev_out.ipynb --allow-errors --ExecutePreprocessor.timeout=1800 2>&1 | grep -v "^\[NbConvertApp\]" | tail -3
python - "$@" <<'PY'
import nbformat, sys
nb=nbformat.read('dev_out.ipynb',4)
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
for i,c in enumerate(nb.cells):
    if c.cell_type=='code' and i>=start:
        print(f'----- cell {i} {c.metadata.get("tags","")}')
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text[-8000:])
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue, ''.join(o.traceback)[-1500:])
PY
EOF
chmod +x $TMPDIR/dev.sh; time $TMPDIR/dev.sh
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
----- cell 1 
dandiset 000713 version 0.240702.1725

----- cell 3 
----- cell 4 ['sanity']
sessions read: 153 failed: 0 []
subjects: 81 | session types: {'EPHYS_1_images_G_3uL_reward': 74, 'EPHYS_1_images_H_3uL_reward': 71, 'EPHYS_1_images_G_5uL_reward': 4, 'EPHYS_1_images_H_5uL_reward': 4}
genotypes: {'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 59, 'wt/wt': 49, 'Vip-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 45}
units per session: median 2024.0 range 1103 to 3388
active block length (s): {'count': 153.0, 'mean': 3603.9, 'std': 2.6, 'min': 3599.5, '25%': 3601.5, '50%': 3603.8, '75%': 3606.0, 'max': 3611.4}
active windows per session: {36: 151, 35: 2}
spontaneous epochs after the task (s): {'count': 153.0, 'mean': 289.0, 'std': 0.0, 'min': 289.0, '25%': 289.0, '50%': 289.0, '75%': 289.0, 'max': 289.0}
images per session: {8: 153} | flashes shown per session: median 4623.0 | omitted: median 179.0 | change flashes: median 241.0
length of the series each window is cut from (s):
                      min    50%    max
condition reading                     
active    -        100.0  100.0  100.0
blanks    a        160.0  286.0  528.0
          b        152.5  274.5  513.0
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
s=s.replace('''W = {f"{b}/{s}": paula.conditions(windows, "all", b, s).query("region in @REG") for b, s in CR}
WQ = {f"{b}/{s}": paula.conditions(windows, "qc", b, s).query("region in @paula.kept_regions(windows, 'qc')") for b, s in CR}''','''REGQ = paula.kept_regions(windows, "qc")
W = {}
WQ = {}
for b, s in CR:
    x = paula.conditions(windows, "all", b, s)
    W[f"{b}/{s}"] = x[x.region.isin(REG)]
    x = paula.conditions(windows, "qc", b, s)
    WQ[f"{b}/{s}"] = x[x.region.isin(REGQ)]''')
open('nb.py','w').write(s)
EOF
$TMPDIR/dev.sh 11 2>&1 | head -150
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
----- cell 11 
26 subregions; 2311 populations; active windows 83166

----- cell 13 ['claim:fig1c-cv-region-medians']
region   VISal  VISam   VISl   VISp  VISpm  VISrl   LGd     LP    MGd    MGm    MGv    PIL    POL    PoT    SGN    CA1    CA3     DG   POST   ProS    SUB    APN     NB    NOT    MRN   SCig
median    0.59  0.426  0.607  0.644  0.476  0.455  0.33  0.396  0.388  0.369  0.321  0.306  0.371   0.35  0.336  0.264  0.453  0.564  0.385  0.272  0.273   0.17  0.564  0.403  0.225  0.321
iqr      0.212  0.183  0.228  0.203  0.224  0.159  0.13  0.164  0.176  0.156  0.134  0.171  0.193  0.117  0.141  0.087  0.178  0.118   0.16  0.133  0.141  0.063  0.369  0.153  0.116  0.202
windows   5326   5290   5182   5434   5398   5326  1799   2448   2338   2628   2951   1296   1908   1908   2556   5254   4102   5074   1799   1763   3095   4570    971    540   2663   1547
area       VIS    VIS    VIS    VIS    VIS    VIS    TH     TH     TH     TH     TH     TH     TH     TH     TH     HP     HP     HP     HP     HP     HP     MB     MB     MB     MB     MB
units=all VIS: medians 0.426 to 0.644 (expected 0.4 to 0.59); inside widened range 6/6; extremes within tolerance True; IQR 0.159 to 0.228, inside 2/6
units=all TH: medians 0.306 to 0.396 (expected 0.27 to 0.37); inside widened range 9/9; extremes within tolerance False; IQR 0.117 to 0.193, inside 6/9
units=all HP: medians 0.264 to 0.564 (expected 0.25 to 0.49); inside widened range 5/6; extremes within tolerance False; IQR 0.087 to 0.178, inside 4/6
units=all MB: medians 0.170 to 0.564 (expected 0.16 to 0.45); inside widened range 4/5; extremes within tolerance False; IQR 0.063 to 0.369, inside 4/5
units=all: highest hippocampal median is DG (0.
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/nb.py <<'EOF'

# %% md
# ## fig1e-positive-cv-modules
#
# > The strongest 10% of positive CV correlations (0.50 to 0.67) link subregions within functional modules (visual areas together, subicular regions together, thalamic populations together), with connections between distinct systems largely absent.

# %% code claim:fig1e-positive-cv-modules
def pairs_table(m):
    rows = [(REG[i], REG[j], m.values[i, j]) for i, j in zip(*iu) if np.isfinite(m.values[i, j])]
    p = pd.DataFrame(rows, columns=["r1", "r2", "r"])
    p["same_area"] = [paula.REGION_AREA[a] == paula.REGION_AREA[b] for a, b in zip(p.r1, p.r2)]
    return p

ok1e = {}
for lab, m in [("a", EMP_A), ("b", EMP_B)]:
    p = pairs_table(m)
    top = p.nlargest(int(round(0.1 * len(p))), "r")
    lo_ok, hi_ok = tol(top.r.min(), 0.50, 0.05), tol(top.r.max(), 0.67, 0.067)
    frac = top.same_area.mean()
    ok1e[lab] = lo_ok and hi_ok and frac > 0.5
    print(f"reading {lab}: top {len(top)} of {len(p)} pairs, r {top.r.min():.3f} to {top.r.max():.3f} (expected 0.50 to 0.67; low end within tolerance {lo_ok}, high end {hi_ok}); "
          f"same major area {int(top.same_area.sum())}/{len(top)} ({frac:.2f}); passes {ok1e[lab]}")
    print("   ", "; ".join(f"{a}-{b} {r:.2f}" for a, b, r in top[["r1", "r2", "r"]].values))

# %% md
# **Result: ...**

# %% md
# ## fig1e-dg-ca3-anticorrelation-hubs
#
# > Among the 10% most anticorrelated region pairs (r from -0.27 to -0.002), DG and CA3 are the hubs of negative CV relationships with other regions.

# %% code claim:fig1e-dg-ca3-anticorrelation-hubs
ok1h = {}
for lab, m in [("a", EMP_A), ("b", EMP_B)]:
    p = pairs_table(m)
    neg = p.nsmallest(int(round(0.1 * len(p))), "r")
    cnt = pd.Series(list(neg.r1) + list(neg.r2)).value_counts()
    top2 = set(cnt.index[:2])
    tie = cnt.iloc[1] == cnt.iloc[2] if len(cnt) > 2 else False
    ok1h[lab] = top2 == {"DG", "CA3"} and tol(neg.r.min(), -0.27, 0.027)
    print(f"reading {lab}: {len(neg)} pairs, r {neg.r.min():.3f} to {neg.r.max():.3f} (most negative expected -0.27 +/- 0.027); "
          f"appearances {cnt.head(6).to_dict()}; tie for second place {tie}; passes {ok1h[lab]}")

# %% md
# **Result: ...**

# %% md
# ## fig1e-midbrain-weakest-cv-correlations
#
# > Midbrain areas have the weakest CV correlations with all other regions, near zero (-0.04 to +0.03).

# %% code claim:fig1e-midbrain-weakest-cv-correlations
ok1m = {}
lo_n, hi_n = widen(-0.04, 0.03)
for lab, m in [("a", EMP_A), ("b", EMP_B)]:
    mm = m.abs().mean(axis=1)
    area_mean = mm.groupby([paula.REGION_AREA[r] for r in mm.index]).mean()
    p = pairs_table(m)
    mbp = p[[paula.REGION_AREA[a] == "MB" or paula.REGION_AREA[b] == "MB" for a, b in zip(p.r1, p.r2)]]
    near = within(mbp.r, lo_n, hi_n).mean()
    ok1m[lab] = area_mean.idxmin() == "MB" and near > 0.5
    print(f"reading {lab}: mean |r| by area {area_mean.round(3).to_dict()}; per MB subregion {mm[[r for r in REG if paula.REGION_AREA[r]=='MB']].round(3).to_dict()}; "
          f"MB pairs in {lo_n:.3f} to {hi_n:.3f}: {int(within(mbp.r, lo_n, hi_n).sum())}/{len(mbp)} ({near:.2f}); passes {ok1m[lab]}")

# %% md
# **Result: ...**

# %% md
# ## Medians of CV by condition (claims of Fig. 2a)
#
# The median CV of each subregion in each condition, under each condition reading. Rows are subregions; columns condition and reading.

# %% code
def med_table(value, Wd=W):
    out = {}
    for k, w in Wd.items():
        out[k] = w.groupby(["region", "condition"])[value].median().unstack()[paula.CONDITIONS]
    return pd.concat(out, axis=1).reindex([r for r in paula.REGION_ORDER if r in set(Wd["a/a"].region)])

MED_CV = med_table("cv")
print(MED_CV.round(3).to_string())
print("windows per condition (reading a/a):", W["a/a"].condition.value_counts().to_dict())

def check_expected(med, exp, readings=None):
    """exp: list of (label, region, condition(s), kind, value, tolerance); returns per reading the passes."""
    res = {}
    for rd in (readings or list(med.columns.levels[0])):
        rows = []
        for lab, reg, conds, kind, v, t in exp:
            vals = med.loc[reg, rd][conds] if isinstance(conds, list) else pd.Series({conds: med.loc[reg, (rd, conds)]})
            x = {"min": vals.min(), "max": vals.max(), "each": None, "value": vals.iloc[0]}[kind] if kind != "each" else None
            if kind == "each":
                ok = bool(all(tol(y, v, t) for y in vals))
                x = f"{vals.min():.3f}-{vals.max():.3f}"
            else:
                ok = tol(x, v, t)
                x = round(float(x), 3)
            rows.append((lab, x, v, ok))
        res[rd] = rows
    return res

def show_expected(res):
    for rd, rows in res.items():
        n = sum(r[3] for r in rows)
        print(f"reading {rd}: {n}/{len(rows)} within tolerance; " + "; ".join(f"{l} {x} ({v})" + ("" if ok else " MISS") for l, x, v, ok in rows))

# %% md
# ## fig2a-vis-cv-by-condition
#
# > In visual cortex, median CV is higher in active behavior and blank screens (VISp 0.59 and 0.55, VISl 0.56 and 0.46, VISal 0.55 and 0.46) than in spontaneous activity (0.29, 0.30, 0.30), with natural images intermediate (0.39, 0.46, 0.48).

# %% code claim:fig2a-vis-cv-by-condition
E2A = []
for r, vals in {"VISp": (0.59, 0.55, 0.29, 0.39), "VISl": (0.56, 0.46, 0.30, 0.46), "VISal": (0.55, 0.46, 0.30, 0.48)}.items():
    for c, v in zip(["active", "blanks", "spont", "images"], vals):
        E2A.append((f"{r} {c}", r, c, "value", v, 0.1 * v))
r2a = check_expected(MED_CV, E2A)
show_expected(r2a)
for rd in r2a:
    m = MED_CV[rd]
    order = {r: bool(m.loc[r, "active"] > m.loc[r, "images"] > m.loc[r, "spont"] and m.loc[r, "blanks"] > m.loc[r, "spont"]) for r in ["VISp", "VISl", "VISal"]}
    print(f"reading {rd}: order active > images > spont and blanks > spont: {order}")
print("variant units=qc:")
MED_CVQ = med_table("cv", WQ)
show_expected(check_expected(MED_CVQ, E2A, ["a/a"]))

# %% md
# **Result: ...**

# %% md
# ## fig2a-thalamus-cv-by-condition
#
# > Thalamic populations show the same pattern with smaller effects, LP median CV 0.37 in active behavior against 0.28 in spontaneous activity, LGd 0.32 against 0.23.

# %% code claim:fig2a-thalamus-cv-by-condition
E2T = [("LP active", "LP", "active", "value", 0.37, 0.037), ("LP spont", "LP", "spont", "value", 0.28, 0.028),
       ("LGd active", "LGd", "active", "value", 0.32, 0.032), ("LGd spont", "LGd", "spont", "value", 0.23, 0.023)]
show_expected(check_expected(MED_CV, E2T))
for rd in MED_CV.columns.levels[0]:
    m = MED_CV[rd]
    d = (m["active"] - m["spont"])
    print(f"reading {rd}: active minus spontaneous LP {d['LP']:.3f}, LGd {d['LGd']:.3f}; VISp {d['VISp']:.3f}, VISl {d['VISl']:.3f}, VISal {d['VISal']:.3f}; "
          f"smaller in both thalamic nuclei than in all three visual areas: {bool(max(d['LP'], d['LGd']) < min(d['VISp'], d['VISl'], d['VISal']))}")

# %% md
# **Result: ...**

# %% md
# ## fig2a-hippocampus-cv-stable
#
# > DG and CA3 keep nearly constant median CV across the visually driven conditions (DG 0.48 to 0.50, CA3 0.41 to 0.42; CA1 0.25), with modest increases in spontaneous activity (DG 0.51, CA3 0.43).

# %% code claim:fig2a-hippocampus-cv-stable
VD = ["images", "active", "blanks"]
E2H = [("DG VD low", "DG", VD, "min", 0.48, 0.048), ("DG VD high", "DG", VD, "max", 0.50, 0.05),
       ("CA3 VD low", "CA3", VD, "min", 0.41, 0.041), ("CA3 VD high", "CA3", VD, "max", 0.42, 0.042),
       ("CA1 VD each", "CA1", VD, "each", 0.25, 0.025),
       ("DG spont", "DG", "spont", "value", 0.51, 0.051), ("CA3 spont", "CA3", "spont", "value", 0.43, 0.043)]
show_expected(check_expected(MED_CV, E2H))
for rd in MED_CV.columns.levels[0]:
    m = MED_CV[rd]
    print(f"reading {rd}: spontaneous above every visually driven median: DG {bool(m.loc['DG','spont'] > m.loc['DG', VD].max())}, CA3 {bool(m.loc['CA3','spont'] > m.loc['CA3', VD].max())}")

# %% md
# **Result: ...**

# %% md
# ## fig2a-midbrain-cv-invariant
#
# > Midbrain populations have essentially constant CV across all conditions (APN median 0.16 in every condition, MRN 0.20 to 0.21).

# %% code claim:fig2a-midbrain-cv-invariant
E2M = [("APN each", "APN", paula.CONDITIONS, "each", 0.16, 0.016), ("MRN low", "MRN", paula.CONDITIONS, "min", 0.20, 0.02),
       ("MRN high", "MRN", paula.CONDITIONS, "max", 0.21, 0.021)]
show_expected(check_expected(MED_CV, E2M))

# %% md
# **Result: ...**

# %% md
# ## JS divergence matrices of CV (claims of Fig. 2b)
#
# For each condition, the JS divergence between the CV distributions of every pair of subregions, with 50 and 100 equal histogram bins over the pooled range of each pair, in bits. The sums are within each major area: (all) every pair of its block; (adjacent) the first off-diagonal in Table I order. Percentage differences: (second) |A - B| / B; (mean) |A - B| over the mean of A and B.

# %% code
JS_CV = {(rd, nb): {c: paula.js_matrix(w[w.condition == c], "cv", REG, nb) for c in paula.CONDITIONS}
         for rd, w in W.items() for nb in (50, 100)}
def pct_table(JS):
    rows = []
    for (rd, nb), mats in JS.items():
        for sm in ("all", "adjacent"):
            for pm in ("second", "mean"):
                for a in paula.AREAS:
                    s = {c: paula.summed_js(mats[c], a, sm) for c in paula.CONDITIONS}
                    for c1, c2 in paula.COND_PAIRS:
                        rows.append({"reading": rd, "bins": nb, "sum": sm, "pct": pm, "area": a, "pair": f"{c1}-{c2}",
                                     "S1": s[c1], "S2": s[c2], "diff": paula.pct_diff(s[c1], s[c2], pm)})
    return pd.DataFrame(rows)
PCT_CV = pct_table(JS_CV)
print(PCT_CV[(PCT_CV.reading == "a/a") & (PCT_CV.bins == 50) & (PCT_CV.pct == "second")].pivot_table(index=["sum", "area"], columns="pair", values="diff").round(1).to_string())
print("summed JS (reading a/a, 50 bins, all pairs):", {a: {c: round(paula.summed_js(JS_CV[("a/a", 50)][c], a, "all"), 2) for c in paula.CONDITIONS} for a in paula.AREAS})

# %% md
# ## fig2b-vis-summed-js-cv
#
# > For CV, the summed within-area JS divergences of visual cortex are nearly equal in active behavior and blank screens (about 1% apart) and differ by about 30% from those of natural images and spontaneous activity.

# %% code claim:fig2b-vis-summed-js-cv
FOUR = ["images-active", "active-spont", "images-blanks", "blanks-spont"]
res2b = []
for key, g in PCT_CV[PCT_CV.area == "VIS"].groupby(["reading", "bins", "sum", "pct"]):
    d = g.set_index("pair")["diff"]
    ab = d["active-blanks"]
    four = d[FOUR]
    full = 0.5 <= ab <= 1.5 and bool(((four >= 27) & (four <= 33)).all())
    part = d.idxmin() == "active-blanks" and bool((d.drop("active-blanks") > 15).all())
    res2b.append({"reading": key[0], "bins": key[1], "sum": key[2], "pct": key[3], "active-blanks": round(ab, 2),
                  **{p: round(four[p], 1) for p in FOUR}, "closest pair": d.idxmin(), "reproduced": full, "partial": part})
res2b = pd.DataFrame(res2b)
print(res2b.to_string())
print("combinations reproduced:", int(res2b.reproduced.sum()), "| partial:", int(res2b.partial.sum()), "of", len(res2b))

# %% md
# **Result: ...**

# %% md
# ## fig2b-hp-mb-summed-js-cv
#
# > For CV, the largest hippocampal percentage difference in summed JS divergence is between active behavior and spontaneous activity (about 15%), and midbrain has the smallest differences (at most 7%).

# %% code claim:fig2b-hp-mb-summed-js-cv
res2h = []
for key, g in PCT_CV.groupby(["reading", "bins", "sum", "pct"]):
    t = g.pivot_table(index="area", columns="pair", values="diff")
    hp = t.loc["HP"]
    mb_max = t.loc["MB"].max()
    mb_small = int((t.idxmin(axis=0) == "MB").sum())
    ok = tol(hp["active-spont"], 15, 1.5) and hp.idxmax() == "active-spont" and mb_max <= 7.7 and mb_small >= 4
    res2h.append({"reading": key[0], "bins": key[1], "sum": key[2], "pct": key[3], "HP active-spont": round(hp["active-spont"], 1),
                  "HP largest pair": hp.idxmax(), "MB max": round(mb_max, 1), "pairs where MB smallest": mb_small, "reproduced": ok})
res2h = pd.DataFrame(res2h)
print(res2h.to_string())
print("combinations reproduced:", int(res2h.reproduced.sum()), "of", len(res2h))

# %% md
# **Result: ...**

# %% md
# ## fig2b-visually-driven-js-cv-low
#
# > Among the three visually driven conditions, the CV-based JS divergences of cortical regions differ little between conditions (typically less than 4%).

# %% code claim:fig2b-visually-driven-js-cv-low
VDP = ["images-active", "images-blanks", "active-blanks"]
r = PCT_CV[(PCT_CV.area == "VIS") & PCT_CV.pair.isin(VDP)].pivot_table(index=["reading", "bins", "sum", "pct"], columns="pair", values="diff")
r["n at most 4.4%"] = (r[VDP] <= 4.4).sum(axis=1)
r["reproduced"] = r["n at most 4.4%"] >= 2
print(r.round(1).to_string())
print("combinations reproduced (percentage reading):", int(r.reproduced.sum()), "of", len(r))
vis = [x for x in REG if paula.REGION_AREA[x] == "VIS"]
vi = np.triu_indices(len(vis), 1)
for (rd, nb), mats in JS_CV.items():
    fr = {c: float((mats[c].loc[vis, vis].values[vi] <= 0.22).mean()) for c in VD}
    print(f"JS reading, {rd}, {nb} bins: fraction of VIS-VIS pairs at most 0.22: {({k: round(v, 2) for k, v in fr.items()})}; "
          f"VIS-VIS JS range {min(mats[c].loc[vis, vis].values[vi].min() for c in VD):.3f} to {max(mats[c].loc[vis, vis].values[vi].max() for c in VD):.3f}; passes {all(v > 0.5 for v in fr.values())}")

# %% md
# **Result: ...**

# %% md
# ## fig2b-dg-ca3-high-js-cv
#
# > DG and CA3 have high CV-based JS divergences in all four conditions, largest in spontaneous activity (median 0.84 for both) and blank screens (median 0.63 for both).

# %% code claim:fig2b-dg-ca3-high-js-cv
hp_regs = [x for x in REG if paula.REGION_AREA[x] == "HP"]
for variant, others in [("all other subregions", None), ("other hippocampal subregions", hp_regs)]:
    for (rd, nb), mats in JS_CV.items():
        med = {}
        for reg in ["DG", "CA3"]:
            for c in paula.CONDITIONS:
                row = mats[c].loc[reg].drop(reg)
                if others:
                    row = row[[o for o in others if o != reg]]
                med[(reg, c)] = row.median()
        ok = (tol(med[("DG", "spont")], 0.84, 0.084) and tol(med[("CA3", "spont")], 0.84, 0.084) and tol(med[("DG", "blanks")], 0.63, 0.063)
              and tol(med[("CA3", "blanks")], 0.63, 0.063)
              and all(med[(g, "spont")] == max(med[(g, c)] for c in paula.CONDITIONS) for g in ["DG", "CA3"]))
        print(f"{variant}, {rd}, {nb} bins: " + ", ".join(f"{g} {c} {v:.3f}" for (g, c), v in med.items()) + f"; passes {ok}")

# %% md
# **Result: ...**

# %% md
# ## fig2b-legend-js-cv
#
# > In the CV-based JS divergences, visual and thalamic regions diverge strongly between spontaneous and visually driven states (above 0.40 for most visual areas, above 0.30 for thalamic regions), DG and CA3 moderately (0.15 to 0.35), and midbrain least (below 0.15 for most condition pairs).
#
# Reading (a): per subregion, the JS divergence between its own CV distributions in two conditions. Reading (b): per subregion, the mean absolute difference between its row of the region-pair matrix in spontaneous activity and in a visually driven condition (this notebook's operational form of "comparing a region's row"). A subregion's value for "spontaneous against visually driven" is the mean over the three visually driven conditions.

# %% code claim:fig2b-legend-js-cv
def legend_values(rd, nb):
    w = W[rd]
    out = {}
    for reg in REG:
        x = w[w.region == reg]
        out[reg] = {f"{c1}-{c2}": paula.js_divergence(x[x.condition == c1].cv, x[x.condition == c2].cv, nb) for c1, c2 in paula.COND_PAIRS}
    a = pd.DataFrame(out).T
    mats = JS_CV[(rd, nb)]
    b = pd.DataFrame({reg: {f"{c1}-{c2}": float((mats[c1].loc[reg].drop(reg) - mats[c2].loc[reg].drop(reg)).abs().mean()) for c1, c2 in paula.COND_PAIRS} for reg in REG}).T
    return a, b

SVD = ["images-spont", "active-spont", "blanks-spont"]
res_leg = []
for rd in W:
    for nb in (50, 100):
        for lab, t in zip(["a", "b"], legend_values(rd, nb)):
            sv = t[SVD].mean(axis=1)
            v = [x for x in REG if paula.REGION_AREA[x] == "VIS"]
            th = [x for x in REG if paula.REGION_AREA[x] == "TH"]
            mb = [x for x in REG if paula.REGION_AREA[x] == "MB"]
            dgca3 = t.loc[["DG", "CA3"]].values.ravel()
            res_leg.append({"reading": rd, "bins": nb, "measure": lab,
                            "VIS > 0.44": f"{int((sv[v] > 0.44).sum())}/{len(v)}", "TH > 0.33": f"{int((sv[th] > 0.33).sum())}/{len(th)}",
                            "DG, CA3 range": f"{dgca3.min():.3f}-{dgca3.max():.3f}", "MB < 0.165": f"{int((t.loc[mb].values < 0.165).sum())}/{t.loc[mb].size}",
                            "passes": bool((sv[v] > 0.44).mean() > 0.5 and (sv[th] > 0.33).mean() > 0.5 and within(dgca3, 0.135, 0.385).all() and (t.loc[mb].values < 0.165).mean() > 0.5)})
            if rd == "a/a" and nb == 50:
                print(f"measure {lab}, reading a/a, 50 bins:\n", t.round(3).T.to_string())
print(pd.DataFrame(res_leg).to_string())

# %% md
# **Result: ...**
EOF
$TMPDIR/dev.sh 20 2>&1 | head -230
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
----- cell 22 ['claim:fig1e-positive-cv-modules']
reading a: top 32 of 325 pairs, r 0.459 to 0.772 (expected 0.50 to 0.67; low end within tolerance True, high end False); same major area 21/32 (0.66); passes False
    NB-SCig 0.77; PIL-SCig 0.71; VISam-VISpm 0.69; SUB-SCig 0.67; VISl-VISpm 0.67; VISl-VISp 0.64; VISal-VISl 0.64; VISp-VISpm 0.63; VISam-VISp 0.63; VISam-VISl 0.63; VISam-VISrl 0.62; ProS-SCig 0.62; POST-SUB 0.61; VISal-VISam 0.60; VISal-VISp 0.59; VISal-VISpm 0.59; VISpm-VISrl 0.56; PIL-APN 0.56; VISl-VISrl 0.56; MGd-PIL 0.55; MRN-SCig 0.54; LGd-PoT 0.54; MGd-NOT 0.53; PIL-SUB 0.50; VISal-VISrl 0.49; MGd-ProS 0.49; VISam-SGN 0.48; MGv-POST 0.47; LGd-MGd 0.47; VISp-VISrl 0.47; VISrl-SGN 0.47; VISpm-SGN 0.46
reading b: top 32 of 325 pairs, r 0.450 to 0.669 (expected 0.50 to 0.67; low end within tolerance False, high end True); same major area 26/32 (0.81); passes False
    VISal-VISl 0.67; VISam-VISpm 0.66; VISl-VISpm 0.65; VISal-VISam 0.63; VISl-VISp 0.63; VISp-VISpm 0.63; VISam-VISl 0.62; VISal-VISpm 0.62; POST-SUB 0.59; MGd-MGv 0.57; VISal-VISp 0.56; ProS-SUB 0.55; MGv-SGN 0.54; VISam-VISp 0.53; PoT-ProS 0.52; LP-MGv 0.50; VISam-VISrl 0.50; MGd-SGN 0.49; PoT-SGN 0.49; LP-MGd 0.49; CA1-SUB 0.48; VISal-VISrl 0.48; LP-SGN 0.48; LGd-ProS 0.47; MGd-ProS 0.47; MGv-ProS 0.46; VISl-VISrl 0.46; POST-ProS 0.46; VISpm-VISrl 0.46; VISpm-LGd 0.46; VISp-LGd 0.45; MGm-MGv 0.45

----- cell 25 ['claim:fig1e-dg-ca3-anticorrelation-hubs']
reading a: 32 pairs, r -0.496 to -0.013 (most negative expected -0.27 +/- 0.027); appearances {'NB': 15, 'DG': 5, 'SCig': 5, 'CA3': 4, 'POL': 3, 'SGN': 3}; tie for second place True; passes False
reading b: 32 pairs, r -0.178 to 0.056 (most negative expected 
[... 220 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat >> $TMPDIR/nb.py <<'EOF'

# %% md
# ## fig3a-reference-systems
#
# > In the C-H plane with D = 6, white noise lies at H near 1 and C near 0, a sine near H 0 and C near 0.1, exponentially correlated Brownian motion at C 0.3 to 0.5 for H 0.3 to 0.6, and chaotic maps (logistic, tent, Ikeda) near maximum complexity, C 0.4 to 0.5 at H 0.5 to 0.8.
#
# Synthetic series as defined in Supplemental Material Sec. I, 10^5 points after 10^3 dropped (claims file). Correlated Gaussian noise: increments from N(0, 1) noise convolved with the normalized kernel w_k = exp(-k / (K alpha)), K = floor(100 alpha) + 1, then summed (Sec. I.A). The sine is sampled at 1000 points per period (its sampling is not given; a slow sine is the one that reaches H near 0). "Near" a value of 0 is read as within 0.05 (a standard choice; 10% of 0 is no tolerance), and near 1 as at least 0.9. The chaotic maps are judged at their fully chaotic parameters (logistic r = 4, tent mu = 1.9999, Ikeda p = 6) and the sweeps of the open ranges are shown.

# %% code claim:fig3a-reference-systems
rng3 = np.random.default_rng(zlib.crc32(b"paula-2026/fig3a-reference-systems"))
N3, DROP = 100_000, 1_000
def logistic(r, n=N3 + DROP, x=0.4):
    out = np.empty(n)
    for i in range(n):
        x = r * x * (1 - x); out[i] = x
    return out[DROP:]
def tent(mu, n=N3 + DROP, x=0.3141):
    out = np.empty(n)
    for i in range(n):
        x = mu * x if x < 0.5 else mu * (1 - x); out[i] = x
    return out[DROP:]
def ikeda(p, u=0.9, n=N3 + DROP):
    x = y = 0.1; out = np.empty(n)
    for i in range(n):
        t = p - 6 / (1 + x * x + y * y)
        x, y = 1 + u * (x * np.cos(t) - y * np.sin(t)), u * (x * np.sin(t) + y * np.cos(t)); out[i] = x
    return out[DROP:]
def corr_walk(alpha, n=N3):
    K = int(np.floor(100 * alpha)) + 1
    w = np.exp(-np.arange(K) / (K * alpha)); w /= w.sum()
    e = rng3.standard_normal(n + K)
    return np.cumsum(np.convolve(e, w, mode="valid")[:n])
def fk_noise(k, n=N3):
    f = np.fft.rfftfreq(n); amp = np.zeros_like(f); amp[1:] = f[1:] ** (-k / 2)
    ph = np.exp(2j * np.pi * rng3.random(len(f)))
    return np.fft.irfft(amp * ph, n)
ref = []
ref.append(("white noise", "", *paula.bandt_pompe(rng3.standard_normal(N3))))
ref.append(("sine", "1000 points per period", *paula.bandt_pompe(np.sin(2 * np.pi * np.arange(N3) / 1000))))
ref.append(("Brownian motion", "", *paula.bandt_pompe(np.cumsum(rng3.standard_normal(N3)))))
for a in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:
    ref.append(("exp. correlated walk", f"alpha={a}", *paula.bandt_pompe(corr_walk(a))))
for r in [3.5, 3.6, 3.7, 3.8, 3.9, 4.0]:
    ref.append(("logistic", f"r={r}", *paula.bandt_pompe(logistic(r))))
for mu in [1.2, 1.4, 1.6, 1.8, 1.9999]:
    ref.append(("tent", f"mu={mu}", *paula.bandt_pompe(tent(mu))))
for p in [5, 6, 8, 11, 14, 17]:
    ref.append(("Ikeda", f"p={p}", *paula.bandt_pompe(ikeda(p))))
for k in [0, 0.5, 1, 1.5, 2, 2.5, 3]:
    ref.append(("1/f^k noise", f"k={k}", *paula.bandt_pompe(fk_noise(k))))
REF = pd.DataFrame(ref, columns=["system", "parameter", "H", "C"])
print(REF.round(3).to_string())
g = lambda s, p: REF[(REF.system == s) & (REF.parameter == p)].iloc[0]
wn, sn = g("white noise", ""), g("sine", "1000 points per period")
ok_wn = wn.H >= 0.9 and wn.C <= 0.05
ok_sn = sn.H <= 0.05 and within(sn.C, 0.09, 0.11)
ew = REF[(REF.system == "exp. correlated walk") & within(REF.H, 0.27, 0.66)]
ok_ew = len(ew) > 0 and bool(within(ew.C, 0.27, 0.55).all())
chaos = pd.DataFrame([g("logistic", "r=4.0"), g("tent", "mu=1.9999"), g("Ikeda", "p=6")])
ok_ch = bool((within(chaos.C, 0.36, 0.55) & within(chaos.H, 0.45, 0.88)).all())
print(f"white noise H {wn.H:.3f} C {wn.C:.4f}: {ok_wn}; sine H {sn.H:.3f} C {sn.C:.3f}: {ok_sn}")
print(f"exp. correlated walk: {len(ew)} of 8 alphas with H in 0.27 to 0.66, their C {ew.C.min() if len(ew) else np.nan:.3f} to {ew.C.max() if len(ew) else np.nan:.3f}; all walks H {REF[REF.system=='exp. correlated walk'].H.min():.3f} to {REF[REF.system=='exp. correlated walk'].H.max():.3f}: {ok_ew}")
print("chaotic maps at chaotic parameters:\n", chaos.round(3).to_string(), "\n inside C 0.36 to 0.55 and H 0.45 to 0.88:", ok_ch)
fig, ax = plt.subplots(figsize=(6, 4.5))
for s, gg in REF.groupby("system"):
    ax.plot(gg.H, gg.C, "o-" if len(gg) > 1 else "o", label=s, ms=4)
ax.set_xlabel("H"); ax.set_ylabel("C"); ax.set_xlim(0, 1); ax.set_ylim(0, 0.55); ax.legend(fontsize=7); plt.show()
print("plotted H range", REF.H.min().round(3), REF.H.max().round(3), "C range", REF.C.min().round(3), REF.C.max().round(3))

# %% md
# **Result: ...**

# %% md
# ## fig3b-complexity-levels-by-region
#
# > Across the hour of active recording, visual cortex and hippocampus keep the highest statistical complexity (C about 0.13 to 0.15), thalamus is intermediate (about 0.11) and midbrain lowest (about 0.10), and these differences stay stable over time.
#
# Reading (a): the 36 active windows; reading (b): the eight natural-image windows per population in image order (alphabetical image names, as no other order is given).

# %% code claim:fig3b-complexity-levels-by-region
def fig3b(w, label):
    tc = w.groupby(["area", "k"]).C.agg(["mean", "sem", "size"]).reset_index()
    piv = tc.pivot(index="k", columns="area", values="mean")
    means = piv.mean()
    ok_v = all(within(means[a], 0.117, 0.165) for a in ["VIS", "HP"])
    ok_t, ok_m = tol(means["TH"], 0.11, 0.011), tol(means["MB"], 0.10, 0.01)
    order = (piv.MB < piv.TH) & (piv.TH < piv.VIS) & (piv.TH < piv.HP)
    print(f"{label}: mean over windows {means.round(4).to_dict()}; VIS and HP in 0.117 to 0.165 {ok_v}; TH {ok_t}; MB {ok_m}; "
          f"order MB < TH < VIS and HP at {int(order.sum())} of {len(order)} indices; range over indices {piv.min().round(3).to_dict()} to {piv.max().round(3).to_dict()}; "
          f"largest standard error {tc['sem'].max():.4f}")
    return piv, ok_v and ok_t and ok_m and bool(order.all()), ok_v and ok_t and ok_m and order.mean() > 0.5
piv_a, full_a, part_a = fig3b(ACT, "reading a (active)")
IMG = W["a/a"][W["a/a"].condition == "images"]
piv_b, full_b, part_b = fig3b(IMG, "reading b (images)")
print("variant units=qc:"); _ = fig3b(ACTQ, "reading a, units=qc")
fig, ax = plt.subplots(figsize=(7, 3.5))
for a in paula.AREAS:
    ax.plot(piv_a.index, piv_a[a], label=a)
ax.set_xlabel("active window index"); ax.set_ylabel("mean C"); ax.legend(); plt.show()

# %% md
# **Result: ...**

# %% md
# ## C-H plane per area (claims of Figs. 3c to 3f)
#
# Active windows (the reading the claims file assigns from the point counts), with natural-image windows shown. Spans are the 2.5th to 97.5th percentiles (and the 0th to 100th, a variant). The Mann-Whitney test compares C of the windows with C of their surrogates, two-sided, under the five seeds.

# %% code
SPAN = {"VIS": ((0.8, 1.0), (0.1, 0.4)), "TH": ((0.75, 0.95), (0.05, 0.25)), "HP": ((0.85, 1.0), (0.05, 0.4)), "MB": ((0.9, 1.0), (0.05, 0.2))}
NPTS = {"VIS": 21084, "TH": 11265, "HP": 13059, "MB": 6296}
def ch_table(w, surr=True):
    rows = []
    for a in paula.AREAS:
        x = w[w.area == a]
        r = {"area": a, "windows": len(x), "paper windows": NPTS[a]}
        for q, (lo, hi) in [("95", (2.5, 97.5)), ("100", (0, 100))]:
            r[f"H span {q}"] = tuple(np.round(np.percentile(x.H, [lo, hi]), 3))
            r[f"C span {q}"] = tuple(np.round(np.percentile(x.C, [lo, hi]), 3))
        if surr:
            r["surrogate median C"] = round(x.s_C.median(), 4)
            r["empirical median C"] = round(x.C.median(), 4)
            for s in SFX:
                r["p" + (s or "")] = stats.mannwhitneyu(x.C, x["s_C" + s]).pvalue
                r["surr med" + s] = x["s_C" + s].median() if s else r["surrogate median C"]
        rows.append(r)
    return pd.DataFrame(rows).set_index("area")
CH = ch_table(ACT)
print(CH.T.to_string())
print("\nnatural-image windows:\n", ch_table(IMG, surr=False).T.to_string())

def judge_ch(a, q="95"):
    (hl, hh), (cl, ch) = SPAN[a]
    H0, H1 = CH.loc[a, f"H span {q}"]; C0, C1 = CH.loc[a, f"C span {q}"]
    hw, cw = widen(hl, hh), widen(cl, ch)
    span_ok = hw[0] <= H0 and H1 <= hw[1] and cw[0] <= C0 and C1 <= cw[1]
    test_ok = CH.loc[a, "p"] < 0.001 and CH.loc[a, "empirical median C"] > CH.loc[a, "surrogate median C"]
    width = {b: CH.loc[b, f"C span {q}"][1] - CH.loc[b, f"C span {q}"][0] for b in paula.AREAS}
    print(f"{a}, span {q}: H {H0}-{H1} within {hw[0]:.3f}-{hw[1]:.3f}, C {C0}-{C1} within {cw[0]:.3f}-{cw[1]:.3f}: {span_ok}; "
          f"Mann-Whitney p {CH.loc[a, 'p']:.1e} (five seeds up to {max(CH.loc[a, 'p' + s] for s in SFX):.1e}), empirical above surrogate {CH.loc[a, 'empirical median C'] > CH.loc[a, 'surrogate median C']}; "
          f"C span widths {({b: round(v, 3) for b, v in width.items()})}")
    return span_ok, test_ok, width

# %% md
# ## fig3c-vis-ch-plane
#
# > Visual cortex windows span H 0.8 to 1.0 and C 0.1 to 0.4 in the C-H plane, and differ from ISI-shuffled surrogates, which cluster at lower complexity (C 0.1 to 0.2), Mann-Whitney p < 0.001.

# %% code claim:fig3c-vis-ch-plane
for q in ["95", "100"]:
    s_ok, t_ok, wd = judge_ch("VIS", q)
sm = [CH.loc["VIS", "surr med" + s] for s in SFX]
print(f"VIS surrogate median C under five seeds {min(sm):.4f} to {max(sm):.4f}; inside 0.09 to 0.22: {all(0.09 <= v <= 0.22 for v in sm)}")

# %% md
# **Result: ...**

# %% md
# ## fig3d-th-ch-plane
#
# > Thalamic windows occupy a narrower part of the C-H plane than visual cortex (H 0.75 to 0.95, C 0.05 to 0.25), and differ from surrogates (p < 0.001).

# %% code claim:fig3d-th-ch-plane
for q in ["95", "100"]:
    s_ok, t_ok, wd = judge_ch("TH", q)
    print(f"  span {q}: TH C span narrower than VIS: {wd['TH'] < wd['VIS']}")

# %% md
# **Result: ...**

# %% md
# ## fig3e-hp-ch-plane
#
# > Hippocampal windows have the broadest complexity distribution (C 0.05 to 0.4) at high entropy (H 0.85 to 1.0), and differ from surrogates (p < 0.001).

# %% code claim:fig3e-hp-ch-plane
for q in ["95", "100"]:
    s_ok, t_ok, wd = judge_ch("HP", q)
    print(f"  span {q}: HP C span widest of the four: {max(wd, key=wd.get) == 'HP'}")

# %% md
# **Result: ...**

# %% md
# ## fig3f-mb-ch-plane
#
# > Midbrain windows occupy the most restricted part of the C-H plane, at high entropy (H 0.9 to 1.0) and low complexity (C 0.05 to 0.2), yet differ from surrogates (p < 0.001).

# %% code claim:fig3f-mb-ch-plane
for q in ["95", "100"]:
    s_ok, t_ok, wd = judge_ch("MB", q)
    print(f"  span {q}: MB C span narrowest of the four: {min(wd, key=wd.get) == 'MB'}")
fig, ax = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)
for a_, a in zip(ax, paula.AREAS):
    x = ACT[ACT.area == a]
    a_.plot(x.H, x.C, ".", ms=1, alpha=0.3); a_.plot(x.s_H, x.s_C, ".", ms=1, alpha=0.3, color="k")
    a_.set_title(a); a_.set_xlim(0.5, 1); a_.set_ylim(0, 0.5); a_.set_xlabel("H")
ax[0].set_ylabel("C"); plt.show()
print("windows outside the axes (H < 0.5):", int((ACT.H < 0.5).sum()), "| C > 0.5:", int((ACT.C > 0.5).sum()))

# %% md
# **Result: ...**

# %% md
# ## fig3-complexity-range-fractions
#
# > The fractions of windows by complexity range are, for visual cortex, 0.8% in [0.3, 0.4] and 4.9% in [0.0, 0.1]; thalamus 0.6% in [0.2, 0.3] and 24.6% in [0.0, 0.1]; hippocampus 2.7% in [0.3, 0.4] and 9.5% in [0.0, 0.1]; midbrain 45.4% in [0.1, 0.2] and 54.0% in [0.0, 0.1].

# %% code claim:fig3-complexity-range-fractions
FR = [("VIS", 0.3, 0.4, 0.8), ("VIS", 0.0, 0.1, 4.9), ("TH", 0.2, 0.3, 0.6), ("TH", 0.0, 0.1, 24.6),
      ("HP", 0.3, 0.4, 2.7), ("HP", 0.0, 0.1, 9.5), ("MB", 0.1, 0.2, 45.4), ("MB", 0.0, 0.1, 54.0)]
for lab, w in [("reading a (active)", ACT), ("reading b (images)", IMG), ("active, units=qc", ACTQ)]:
    out, n = [], 0
    for a, lo, hi, v in FR:
        c = w[w.area == a].C
        f = 100 * ((c >= lo) & ((c < hi) | ((hi == 0.4) & (c <= hi)))).mean()
        ok = tol(f, v, 0.1 * v); n += ok
        out.append(f"{a} [{lo},{hi}) {f:.2f}% ({v})" + ("" if ok else " MISS"))
    print(f"{lab}: {n}/8 within tolerance; " + "; ".join(out))

# %% md
# **Result: ...**

# %% md
# ## Medians of C by condition (claims of Fig. 4a to 4d)

# %% code
MED_C = med_table("C")
print(MED_C.round(3).to_string())

def mw_pairs(w, regs, bonf):
    rows = []
    for r in regs:
        x = w[w.region == r]
        for c1, c2 in paula.COND_PAIRS:
            p = stats.mannwhitneyu(x[x.condition == c1].C, x[x.condition == c2].C).pvalue
            rows.append({"region": r, "pair": f"{c1}-{c2}", "p": min(1.0, p * bonf)})
    return pd.DataFrame(rows)

# %% md
# ## fig4a-vis-complexity-by-condition
#
# > All six visual areas have higher median complexity during natural image presentation (0.16 to 0.26) than during spontaneous activity (0.1), with active behavior and blank screens intermediate (0.1 to 0.19), all pairwise comparisons p < 0.001.

# %% code claim:fig4a-vis-complexity-by-condition
VISR = [r for r in REG if paula.REGION_AREA[r] == "VIS"]
r4a = {}
for rd in W:
    m = MED_C[rd].loc[VISR]
    order = (m.images > m.active) & (m.images > m.blanks) & (m.active > m.spont) & (m.blanks > m.spont)
    ni = within(m.images, *widen(0.16, 0.26)); sp = within(m.spont, 0.09, 0.11); ab = within(m.active, *widen(0.1, 0.19)) & within(m.blanks, *widen(0.1, 0.19))
    for name, bonf in [("uncorrected", 1), ("Bonferroni 36", 36)]:
        mw = mw_pairs(W[rd], VISR, bonf)
        allp = bool((mw.p < 0.001).all())
        r4a[(rd, name)] = bool(order.all() and ni.all() and sp.all() and ab.all() and allp)
        print(f"reading {rd}, {name}: order holds in {int(order.sum())}/6 ({list(order[~order].index)} fail); images medians {m.images.min():.3f}-{m.images.max():.3f} inside {int(ni.sum())}/6; "
              f"spont {m.spont.min():.3f}-{m.spont.max():.3f} inside {int(sp.sum())}/6; active and blanks {min(m.active.min(), m.blanks.min()):.3f}-{max(m.active.max(), m.blanks.max()):.3f} inside {int(ab.sum())}/6; "
              f"tests p < 0.001 {int((mw.p < 0.001).sum())}/36, largest p {mw.p.max():.1e} ({mw.loc[mw.p.idxmax(), 'region']} {mw.loc[mw.p.idxmax(), 'pair']}); passes {r4a[(rd, name)]}")
m = MED_C["a/a"].loc[VISR]
print("medians, reading a/a:\n", m.round(3).to_string())
iq = W["a/a"][W["a/a"].region.isin(VISR)].groupby(["region", "condition"]).C.agg(lambda x: x.quantile(0.75) - x.quantile(0.25)).unstack()
print("IQRs (legend 0.08 to 0.12 in visually driven states):\n", iq.round(3).to_string())
LEG4A = {"VISl": (0.15, 0.26), "VISal": (0.15, 0.25), "VISp": (0.16, 0.19)}
for r, (lo, hi) in LEG4A.items():
    vd = m.loc[r, VD]
    print(f"legend {r} {lo}-{hi}: visually driven medians {vd.min():.3f}-{vd.max():.3f}, inside widened range {bool(within(vd, *widen(lo, hi)).all())}")

# %% md
# **Result: ...**

# %% md
# ## fig4b-thalamus-lgd-lp-modulated
#
# > Of nine thalamic nuclei, only LGd and LP show significant modulation of complexity across conditions (p < 0.001), higher during visually driven states (0.14 to 0.18) than spontaneous activity (0.11 to 0.12), with smaller effects than visual cortex.
#
# The effect is the visually driven minus spontaneous median, taken (i) as the largest visually driven median minus the spontaneous one and (ii) as the mean of the three visually driven medians minus the spontaneous one; the claims file does not fix it.

# %% code claim:fig4b-thalamus-lgd-lp-modulated
THR = [r for r in REG if paula.REGION_AREA[r] == "TH"]
def thal_tests(w, regs):
    rows = []
    for r in regs:
        x = w[w.region == r]
        kw = stats.kruskal(*[x[x.condition == c].C for c in paula.CONDITIONS]).pvalue
        pw = [stats.mannwhitneyu(x[x.condition == c].C, x[x.condition == "spont"].C).pvalue for c in VD]
        rows.append({"region": r, "kruskal p": kw, "largest pairwise p (VD vs spont)": max(pw)})
    return pd.DataFrame(rows).set_index("region")
for rd in W:
    m = MED_C[rd]
    tt = thal_tests(W[rd], THR)
    eff_max = m.loc[:, VD].max(axis=1) - m.spont
    eff_mean = m.loc[:, VD].mean(axis=1) - m.spont
    res = []
    for r in ["LGd", "LP"]:
        vd = m.loc[r, VD]
        text_ok = bool(within(vd, *widen(0.14, 0.18)).all()) and within(m.loc[r, "spont"], *widen(0.11, 0.12))
        leg = {"LP": ((0.12, 0.14), 0.11), "LGd": ((0.12, 0.15), 0.10)}[r]
        leg_ok = bool(within(vd, *widen(*leg[0])).all()) and tol(m.loc[r, "spont"], leg[1], 0.1 * leg[1])
        res.append((r, vd.round(3).to_dict(), round(m.loc[r, "spont"], 3), text_ok, leg_ok, bool((vd > m.loc[r, "spont"]).all()),
                    bool(eff_max[r] < eff_max[VISR].min()), bool(eff_mean[r] < eff_mean[VISR].min())))
    print(f"reading {rd}:\n", tt.to_string(float_format=lambda v: f"{v:.1e}"))
    for x in res:
        print(f"  {x[0]}: VD medians {x[1]}, spont {x[2]}; text values {x[3]}; legend values {x[4]}; VD above spont {x[5]}; effect below every visual area (i) {x[6]}, (ii) {x[7]}")
    print(f"  effects (i) VIS {eff_max[VISR].round(3).to_dict()} TH {eff_max[THR].round(3).to_dict()}")
    print(f"  effects (ii) VIS {eff_mean[VISR].round(3).to_dict()} TH {eff_mean[THR].round(3).to_dict()}")

# %% md
# **Result: ...**

# %% md
# ## fig4b-other-thalamus-not-modulated
#
# > The other seven thalamic nuclei (MGd, PoT, SGN, POL, MGm, MGv, PIL) keep uniformly low complexity (0.10 to 0.13) with no significant stimulus dependence.

# %% code claim:fig4b-other-thalamus-not-modulated
SEVEN = ["MGd", "PoT", "SGN", "POL", "MGm", "MGv", "PIL"]
for rd in W:
    m = MED_C[rd].loc[SEVEN]
    tt = thal_tests(W[rd], SEVEN)
    rng_ok = bool(within(m.values, 0.09, 0.143).all())
    print(f"reading {rd}: medians {m.values.min():.3f}-{m.values.max():.3f} inside 0.09 to 0.143 {rng_ok}; "
          f"Kruskal-Wallis p < 0.001 in {list(tt.index[tt['kruskal p'] < 0.001])}; pairwise (all VD vs spont) p < 0.001 in {list(tt.index[tt['largest pairwise p (VD vs spont)'] < 0.001])}")
    print("   largest condition difference in median C:", (m.max(axis=1) - m.min(axis=1)).round(4).to_dict())
    print("   ", tt.to_string(float_format=lambda v: f"{v:.1e}").replace("\n", "\n    "))

# %% md
# **Result: ...**

# %% md
# ## fig4c-dg-ca3-complexity
#
# > DG and CA3 show elevated complexity across most conditions (DG 0.19 to 0.27, CA3 0.15 to 0.21), peaking during spontaneous activity, opposite to visual cortex, while CA1, POST, ProS and SUB stay lower and stable (0.11 to 0.15).

# %% code claim:fig4c-dg-ca3-complexity
for rd in W:
    m = MED_C[rd]
    # (a) text: DG and CA3 inside their range in at least three of four conditions; CA1, POST, ProS, SUB inside 0.11-0.15 in every condition
    a_dg = int(within(m.loc["DG"], *widen(0.19, 0.27)).sum()); a_ca3 = int(within(m.loc["CA3"], *widen(0.15, 0.21)).sum())
    rest = m.loc[["CA1", "POST", "ProS", "SUB"]]
    a_rest = bool(within(rest.values, *widen(0.11, 0.15)).all())
    peak = all(m.loc[g].idxmax() == "spont" for g in ["DG", "CA3"])
    # (b) legend: natural images apart
    b_ok = (tol(m.loc["DG", "images"], 0.12, 0.012) and tol(m.loc["CA3", "images"], 0.11, 0.011) and tol(m.loc["CA1", "images"], 0.10, 0.010)
            and bool(within(m.loc["DG", ["active", "blanks", "spont"]], *widen(0.19, 0.26)).all())
            and bool(within(m.loc["CA3", ["active", "blanks", "spont"]], *widen(0.13, 0.18)).all())
            and bool(within(m.loc["CA1", ["active", "blanks", "spont"]], *widen(0.12, 0.17)).all())
            and bool(within(m.loc[["POST", "ProS", "SUB"]].values, *widen(0.10, 0.13)).all()))
    print(f"reading {rd}: DG {m.loc['DG'].round(3).to_dict()}; CA3 {m.loc['CA3'].round(3).to_dict()}; spontaneous peak {peak}")
    print(f"   text: DG inside in {a_dg}/4, CA3 in {a_ca3}/4, CA1/POST/ProS/SUB all inside {a_rest} (range {rest.values.min():.3f}-{rest.values.max():.3f}); passes {a_dg >= 3 and a_ca3 >= 3 and a_rest and peak}")
    print(f"   legend: passes {b_ok and peak}; CA1 {m.loc['CA1'].round(3).to_dict()}; POST/ProS/SUB {m.loc[['POST','ProS','SUB']].values.min():.3f}-{m.loc[['POST','ProS','SUB']].values.max():.3f}")

# %% md
# **Result: ...**

# %% md
# ## fig4d-midbrain-complexity-invariant
#
# > Most midbrain areas (NB, MRN, SCig, APN) keep uniformly low complexity (0.10 to 0.12) across conditions; only NOT shows modest stimulus dependence (0.13 to 0.15 in visually driven states against 0.13 in spontaneous activity).

# %% code claim:fig4d-midbrain-complexity-invariant
LEG4D = {"NB": (0.11, 0.12), "MRN": (0.10, 0.11), "SCig": (0.10, 0.11), "APN": (0.09, 0.09)}
for rd in W:
    m = MED_C[rd]
    four = m.loc[["NB", "MRN", "SCig", "APN"]]
    text_ok = bool(within(four.values, *widen(0.10, 0.12)).all())
    leg_ok = all(within(m.loc[r], *widen(*v)).all() for r, v in LEG4D.items())
    rngs = (m.loc[[r for r in REG if paula.REGION_AREA[r] == "MB"]].max(axis=1) - m.loc[[r for r in REG if paula.REGION_AREA[r] == "MB"]].min(axis=1))
    not_largest = rngs.idxmax() == "NOT"
    print(f"reading {rd}: medians\n{four.round(3).to_string()}\n NOT {m.loc['NOT'].round(3).to_dict()}; ranges across conditions {rngs.round(3).to_dict()}; "
          f"text values {text_ok}; legend values {leg_ok}; NOT range largest {not_largest}; passes text {text_ok and not_largest}, legend {leg_ok and not_largest}")

# %% md
# **Result: ...**
EOF
$TMPDIR/dev.sh 58 2>&1 | head -320
```

```
Fri Nov 27 11:08:18 UTC 2026
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
----- cell 59 ['claim:fig2b-legend-js-cv']
measure a, reading a/a, 50 bins:
                VISal  VISam   VISl   VISp  VISpm  VISrl    LGd     LP    MGd    MGm    MGv    PIL    POL    PoT    SGN    CA1    CA3     DG   POST   ProS    SUB    APN     NB    NOT    MRN   SCig
images-active  0.070  0.030  0.112  0.424  0.061  0.021  0.058  0.029  0.021  0.044  0.038  0.067  0.039  0.042  0.030  0.004  0.007  0.011  0.026  0.011  0.027  0.014  0.057  0.145  0.032  0.055
images-blanks  0.044  0.053  0.052  0.256  0.029  0.063  0.052  0.055  0.042  0.035  0.031  0.061  0.057  0.051  0.034  0.014  0.024  0.032  0.054  0.043  0.031  0.027  0.082  0.243  0.034  0.090
images-spont   0.544  0.373  0.473  0.244  0.328  0.198  0.244  0.276  0.143  0.183  0.192  0.135  0.203  0.165  0.242  0.049  0.042  0.094  0.212  0.154  0.142  0.108  0.136  0.503  0.146  0.251
active-blanks  0.067  0.066  0.084  0.054  0.038  0.042  0.043  0.033  0.034  0.038  0.038  0.042  0.052  0.038  0.046  0.005  0.004  0.010  0.024  0.006  0.024  0.017  0.037  0.159  0.018  0.053
active-spont   0.614  0.408  0.622  0.719  0.419  0.180  0.340  0.215  0.122  0.103  0.149  0.106  0.136  0.120  0.178  0.022  0.010  0.032  0.102  0.047  0.103  0.084  0.174  0.422  0.110  0.172
blanks-spont   0.456  0.231  0.387  0.581  0.325  0.100  0.275  0.200  0.145  0.148  0.202  0.141  0.205  0.153  0.241  0.051  0.051  0.081  0.230  0.171  0.127  0.092  0.208  0.365  0.127  0.208
measure b, reading a/a, 50 bins:
                VISal  VISam   VISl   VISp  VISpm  VISrl    LGd     LP    MGd    MGm    MGv    PIL    POL    PoT    SGN    CA1    CA3     DG   POST   ProS    SUB    APN     NB    NOT    MRN   SCig
images-ac
[... 307 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import nbformat
nb=nbformat.read('dev_out.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code' and i>=95:
        print(f'----- cell {i} {c.metadata.get("tags","")}')
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text[-5000:])
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
```

```
----- cell 96 ['claim:fig4c-dg-ca3-complexity']
reading a/a: DG {'images': 0.115, 'active': 0.22, 'blanks': 0.178, 'spont': 0.26}; CA3 {'images': 0.108, 'active': 0.159, 'blanks': 0.137, 'spont': 0.198}; spontaneous peak True
   text: DG inside in 3/4, CA3 in 3/4, CA1/POST/ProS/SUB all inside False (range 0.096-0.162); passes False
   legend: passes False; CA1 {'images': 0.096, 'active': 0.136, 'blanks': 0.121, 'spont': 0.162}; POST/ProS/SUB 0.097-0.136
reading a/b: DG {'images': 0.115, 'active': 0.22, 'blanks': 0.178, 'spont': 0.257}; CA3 {'images': 0.108, 'active': 0.159, 'blanks': 0.137, 'spont': 0.196}; spontaneous peak True
   text: DG inside in 3/4, CA3 in 3/4, CA1/POST/ProS/SUB all inside False (range 0.096-0.163); passes False
   legend: passes True; CA1 {'images': 0.096, 'active': 0.136, 'blanks': 0.121, 'spont': 0.163}; POST/ProS/SUB 0.097-0.136
reading b/a: DG {'images': 0.115, 'active': 0.22, 'blanks': 0.179, 'spont': 0.26}; CA3 {'images': 0.108, 'active': 0.159, 'blanks': 0.137, 'spont': 0.198}; spontaneous peak True
   text: DG inside in 3/4, CA3 in 3/4, CA1/POST/ProS/SUB all inside False (range 0.096-0.162); passes False
   legend: passes False; CA1 {'images': 0.096, 'active': 0.136, 'blanks': 0.12, 'spont': 0.162}; POST/ProS/SUB 0.097-0.136
reading b/b: DG {'images': 0.115, 'active': 0.22, 'blanks': 0.179, 'spont': 0.257}; CA3 {'images': 0.108, 'active': 0.159, 'blanks': 0.137, 'spont': 0.196}; spontaneous peak True
   text: DG inside in 3/4, CA3 in 3/4, CA1/POST/ProS/SUB all inside False (range 0.096-0.163); passes False
   legend: passes True; CA1 {'images': 0.096, 'active': 0.136, 'blanks': 0.12, 'spont': 0.163}; POST/ProS/SUB 0.097-0.136

----- cell 99 ['claim:fig4d-midbrain-complexity-invariant']
reading a/a: medians
condition  images  active  blanks  spont
region                                  
NB          0.109   0.110   0.109  0.109
MRN         0.100   0.097   0.096  0.097
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/nb.py <<'EOF'

# %% md
# ## JS divergence matrices of C (claims of Figs. 4e to 4h)
#
# As for CV: per condition, JS divergence in bits between the C distributions of every pair of subregions, with 50 and 100 histogram bins.

# %% code
JS_C = {(rd, nb): {c: paula.js_matrix(w[w.condition == c], "C", REG, nb) for c in paula.CONDITIONS}
        for rd, w in W.items() for nb in (50, 100)}
AREA_OF = np.array([paula.REGION_AREA[r] for r in REG])
def pair_vals(m, a_set, b_set):
    """Values of pairs with one subregion in a_set and the other in b_set (each unordered pair once)."""
    out = []
    for i, j in zip(*iu):
        ai, aj = AREA_OF[i], AREA_OF[j]
        if (ai in a_set and aj in b_set) or (aj in a_set and ai in b_set):
            out.append(m.values[i, j])
    return np.array(out)
print("JS of C, reading a/a, 50 bins, mean by area pair:")
for c in paula.CONDITIONS:
    m = JS_C[("a/a", 50)][c]
    print(c, {f"{a}-{b}": round(float(pair_vals(m, {a}, {b}).mean()), 3) for a in paula.AREAS for b in paula.AREAS if a <= b})

# %% md
# ## fig4e-js-complexity-natural-images
#
# > During natural image presentation the complexity distributions of visual areas are similar to each other (JS below 0.2) but diverge from thalamus and midbrain (JS above 0.4), and DG and CA3 diverge moderately from other regions (JS 0.3 to 0.5).

# %% code claim:fig4e-js-complexity-natural-images
for (rd, nb), mats in JS_C.items():
    m = mats["images"]
    vv = pair_vals(m, {"VIS"}, {"VIS"}); vt = pair_vals(m, {"VIS"}, {"TH"}); vm = pair_vals(m, {"VIS"}, {"MB"})
    dg = np.r_[m.loc["DG"].drop("DG").values, m.loc["CA3"].drop(["CA3", "DG"]).values]
    ok = (vv < 0.22).mean() > 0.5 and (vt > 0.36).mean() > 0.5 and (vm > 0.36).mean() > 0.5 and within(dg, 0.27, 0.55).mean() > 0.5
    print(f"{rd}, {nb} bins: VIS-VIS below 0.22 {(vv < 0.22).mean():.2f} (range {vv.min():.3f}-{vv.max():.3f}); VIS-TH above 0.36 {(vt > 0.36).mean():.2f} (median {np.median(vt):.3f}); "
          f"VIS-MB above 0.36 {(vm > 0.36).mean():.2f} (median {np.median(vm):.3f}); DG/CA3 pairs in 0.27-0.55 {within(dg, 0.27, 0.55).mean():.2f} (median {np.median(dg):.3f}); passes {ok}")

# %% md
# **Result: ...**

# %% md
# ## fig4fg-js-complexity-active-blanks
#
# > During active behavior and blank screens visual cortex keeps complexity distributions distinct from subcortical structures (JS above 0.4), with within-hippocampus divergences of 0.2 to 0.4 during active behavior.

# %% code claim:fig4fg-js-complexity-active-blanks
for (rd, nb), mats in JS_C.items():
    f = {c: pair_vals(mats[c], {"VIS"}, {"TH", "HP", "MB"}) for c in ["active", "blanks"]}
    hh = pair_vals(mats["active"], {"HP"}, {"HP"})
    ok = all((v > 0.36).mean() > 0.5 for v in f.values()) and within(hh, 0.18, 0.44).mean() > 0.5
    print(f"{rd}, {nb} bins: VIS-subcortical above 0.36, active {(f['active'] > 0.36).mean():.2f} (median {np.median(f['active']):.3f}), blanks {(f['blanks'] > 0.36).mean():.2f} (median {np.median(f['blanks']):.3f}); "
          f"HP-HP active in 0.18-0.44 {within(hh, 0.18, 0.44).mean():.2f} (range {hh.min():.3f}-{hh.max():.3f}); passes {ok}")

# %% md
# **Result: ...**

# %% md
# ## fig4h-js-complexity-spontaneous-converges
#
# > In spontaneous activity the JS divergences between regions are lower overall, visual cortex differing less from other regions (JS 0.2 to 0.4) than in visually driven states, and midbrain divergences stay low in all conditions (below 0.2 within the midbrain group).

# %% code claim:fig4h-js-complexity-spontaneous-converges
for (rd, nb), mats in JS_C.items():
    allm = {c: mats[c].values[iu].mean() for c in paula.CONDITIONS}
    vn = {c: pair_vals(mats[c], {"VIS"}, {"TH", "HP", "MB"}) for c in paula.CONDITIONS}
    mm = {c: pair_vals(mats[c], {"MB"}, {"MB"}) for c in paula.CONDITIONS}
    c1 = all(allm["spont"] < allm[c] for c in VD)
    c2 = all(vn["spont"].mean() < vn[c].mean() for c in VD) and within(vn["spont"], 0.18, 0.44).mean() > 0.5
    c3 = all((mm[c] < 0.22).mean() > 0.5 for c in paula.CONDITIONS)
    print(f"{rd}, {nb} bins: mean of all pairs {({c: round(v, 3) for c, v in allm.items()})} (spont lowest {c1}); "
          f"mean VIS-other {({c: round(float(v.mean()), 3) for c, v in vn.items()})}, spont pairs in 0.18-0.44 {within(vn['spont'], 0.18, 0.44).mean():.2f} ({c2}); "
          f"MB-MB below 0.22 {({c: round(float((v < 0.22).mean()), 2) for c, v in mm.items()})} ({c3}); passes {c1 and c2 and c3}")

# %% md
# **Result: ...**

# %% md
# ## supp-robustness-parameters
#
# > The hierarchical, stimulus-dependent pattern of complexity across regions holds for other parameter choices (bin sizes 20 and 50 ms, D from 3 to 6, tau from 1 to 4).
#
# The visually driven minus spontaneous difference of an area is the median C of all its visually driven windows minus the median of its spontaneous windows (this notebook's operational form).

# %% code claim:supp-robustness-parameters
w = W["a/a"]
print("windows per condition (the 20 ms series use the same windows):", w.condition.value_counts().to_dict(), "| supplement's 20 ms counts: images 11 321, active 51 452, blanks 11 265, spontaneous 2856")
nok = 0
for bw, d, tau in paula.ROBUST + [(0.05, 6, 1)]:
    col = "C" if (bw, d, tau) == (0.05, 6, 1) else f"C_{int(bw*1000)}_{d}_{tau}"
    m = w.groupby(["region", "condition"])[col].median().unstack()
    vis_ok = bool((m.loc[VISR, "images"] > m.loc[VISR, "spont"]).all())
    diff = {a: w[(w.area == a) & w.condition.isin(VD)][col].median() - w[(w.area == a) & (w.condition == "spont")][col].median() for a in paula.AREAS}
    ok = vis_ok and diff["VIS"] > diff["MB"]
    if col != "C":
        nok += ok
    print(f"bin {int(bw*1000)} ms, D={d}, tau={tau}{' (main)' if col == 'C' else ''}: images above spontaneous in {int((m.loc[VISR, 'images'] > m.loc[VISR, 'spont']).sum())}/6 visual areas; "
          f"VD minus spont by area {({a: round(v, 4) for a, v in diff.items()})}; holds {ok}")
print("combinations of the supplement where the pattern holds:", nok, "of 5")

# %% md
# **Result: ...**

# %% md
# ## Complexity against CV (claims of Fig. 5)
#
# Per area and condition, windows binned by CV, the mean C and its standard error per bin. Readings: bin width 0.1 or 0.05, with no minimum count or a minimum of 10 windows per bin. Spans are the occupied bins (lower edge of the first to upper edge of the last) and the range of bin means. Reading a/a of the conditions; the condition readings change the spontaneous and blank windows only slightly (medians above).

# %% code
TRAJ = {}
for width in (0.1, 0.05):
    for mn in (0, 10):
        for a in paula.AREAS:
            for c in paula.CONDITIONS:
                x = W["a/a"][(W["a/a"].area == a) & (W["a/a"].condition == c)]
                t = paula.trajectory(x.cv, x.C, width, mn)
                mono = bool((np.diff(t["mean"].values) >= -(t.se.values[1:] + t.se.values[:-1])).all())
                rho = stats.spearmanr(x.cv, x.C).statistic
                slope = stats.linregress(x.cv, x.C).slope
                TRAJ[(width, mn, a, c)] = {"cv lo": t.lo.min(), "cv hi": t.hi.max(), "C lo": t["mean"].min(), "C hi": t["mean"].max(),
                                           "bins": len(t), "monotonic": mono, "spearman": rho, "slope": slope, "table": t}
TR = pd.DataFrame({k: {kk: vv for kk, vv in v.items() if kk != "table"} for k, v in TRAJ.items()}).T
TR.index.names = ["width", "min", "area", "condition"]
print(TR.astype({"cv lo": float, "cv hi": float, "C lo": float, "C hi": float, "spearman": float, "slope": float}).round(3).to_string())
fig, ax = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)
for a_, c in zip(ax, paula.CONDITIONS):
    for a in paula.AREAS:
        t = TRAJ[(0.1, 10, a, c)]["table"]
        a_.errorbar((t.lo + t.hi) / 2, t["mean"], yerr=t.se, label=a, marker="o", ms=3)
    a_.set_title(c); a_.set_xlabel("CV"); a_.set_xlim(0, 2)
ax[0].set_ylabel("mean C"); ax[0].legend(); plt.show()
print("bins with CV above the axis (2):", int(sum((TRAJ[(0.1, 10, a, c)]["table"].lo >= 2).sum() for a in paula.AREAS for c in paula.CONDITIONS)))

def span_ok(x, lo, hi):
    return tol(x[0], lo, 0.1 * abs(lo)) and tol(x[1], hi, 0.1 * abs(hi))

# %% md
# ## fig5-vis-complexity-cv-coupling
#
# > In visual cortex complexity rises with CV during visually driven conditions (natural images CV 0.1 to 0.9 and C 0.08 to 0.34; active behavior CV 0.2 to 1.6 and C 0.10 to 0.38; blanks CV 0.1 to 1.2 and C 0.10 to 0.39), while in spontaneous activity the trajectory compresses, with C below about 0.15.

# %% code claim:fig5-vis-complexity-cv-coupling
Q5 = {"images": ((0.1, 0.9), (0.08, 0.34)), "active": ((0.2, 1.6), (0.10, 0.38)), "blanks": ((0.1, 1.2), (0.10, 0.39))}
for width in (0.1, 0.05):
    for mn in (0, 10):
        oks = []
        for c, (cvr, cr) in Q5.items():
            r = TRAJ[(width, mn, "VIS", c)]
            s1, s2 = span_ok((r["cv lo"], r["cv hi"]), *cvr), span_ok((r["C lo"], r["C hi"]), *cr)
            rise = r["monotonic"] and r["spearman"] > 0
            oks.append(s1 and s2 and rise)
            print(f"width {width}, min {mn}, {c}: CV {r['cv lo']:.2f}-{r['cv hi']:.2f} (quoted {cvr}) {s1}; C {r['C lo']:.3f}-{r['C hi']:.3f} (quoted {cr}) {s2}; "
                  f"monotonic {r['monotonic']}, Spearman {r['spearman']:.3f}")
        sp = TRAJ[(width, mn, "VIS", "spont")]
        print(f"width {width}, min {mn}: spontaneous maximum of bin means {sp['C hi']:.3f} (below 0.165: {sp['C hi'] < 0.165}); passes {all(oks) and sp['C hi'] < 0.165}")

# %% md
# **Result: ...**

# %% md
# ## fig5-th-weaker-coupling
#
# > Thalamus shows a weaker but consistent positive complexity-CV relationship in the visually driven conditions, with shallower slopes than visual cortex and a restricted range (CV 0.2 to 0.8, C 0.10 to 0.20).

# %% code claim:fig5-th-weaker-coupling
for width in (0.1, 0.05):
    for mn in (0, 10):
        oks = []
        for c in VD:
            r, v = TRAJ[(width, mn, "TH", c)], TRAJ[(width, mn, "VIS", c)]
            s = 0.18 <= r["cv lo"] and r["cv hi"] <= 0.88 and 0.09 <= r["C lo"] and r["C hi"] <= 0.22
            oks.append(r["slope"] > 0 and r["slope"] < v["slope"] and s)
            print(f"width {width}, min {mn}, {c}: TH slope {r['slope']:.4f} vs VIS {v['slope']:.4f}; TH CV {r['cv lo']:.2f}-{r['cv hi']:.2f}, C {r['C lo']:.3f}-{r['C hi']:.3f}; spans inside {s}")
        print(f"  passes {all(oks)}")

# %% md
# **Result: ...**

# %% md
# ## fig5-hp-spontaneous-elevated
#
# > Hippocampus shows modest complexity (C 0.12 to 0.19) in the visually driven conditions but markedly elevated complexity during spontaneous activity (C 0.12 to 0.25) at intermediate CV (0.4 to 0.7), comparable to visual cortex during image viewing.

# %% code claim:fig5-hp-spontaneous-elevated
for width in (0.1, 0.05):
    for mn in (0, 10):
        t = TRAJ[(width, mn, "HP", "spont")]["table"]
        mid = t[(t.lo >= 0.4 - 1e-9) & (t.hi <= 0.7 + 1e-9)]
        top = mid["mean"].max() if len(mid) else np.nan
        vdmax = {c: TRAJ[(width, mn, "HP", c)]["C hi"] for c in VD}
        ok = tol(top, 0.25, 0.025) and all(top > v for v in vdmax.values()) and all(tol(v, 0.19, 0.019) for v in vdmax.values())
        print(f"width {width}, min {mn}: HP spontaneous bin means at CV 0.4-0.7 up to {top:.3f}; HP visually driven maxima {({c: round(v, 3) for c, v in vdmax.items()})}; passes {ok}")

# %% md
# **Result: ...**

# %% md
# ## fig5-mb-flat
#
# > Midbrain complexity stays low (C 0.10 to 0.13) across the full range of CV (0.1 to 0.9) in all conditions, giving nearly flat trajectories.

# %% code claim:fig5-mb-flat
for width in (0.1, 0.05):
    for mn in (0, 10):
        inside = {c: bool(TRAJ[(width, mn, "MB", c)]["C lo"] >= 0.09 and TRAJ[(width, mn, "MB", c)]["C hi"] <= (0.165 if c == "images" else 0.143)) for c in paula.CONDITIONS}
        slopes = {c: {a: abs(TRAJ[(width, mn, a, c)]["slope"]) for a in paula.AREAS} for c in paula.CONDITIONS}
        flat = {c: min(s, key=s.get) == "MB" for c, s in slopes.items()}
        print(f"width {width}, min {mn}: MB bin means {({c: (round(TRAJ[(width, mn, 'MB', c)]['C lo'], 3), round(TRAJ[(width, mn, 'MB', c)]['C hi'], 3)) for c in paula.CONDITIONS})}; "
              f"inside {inside}; MB slope smallest {flat}; |slopes| {({c: {a: round(v, 3) for a, v in s.items()} for c, s in slopes.items()})}; passes {all(inside.values()) and all(flat.values())}")

# %% md
# **Result: ...**

# %% md
# ## supp-fig6-mean-correlation
#
# > In visual cortex the mean pairwise spike count correlation is elevated during active behavior and blank screens (median 0.08 to 0.13) and near zero during natural images and spontaneous activity (0.00 to 0.01); midbrain values are low and invariant.

# %% code claim:supp-fig6-mean-correlation
for rd in W:
    for col in ["corr50", "corr20"]:
        m = W[rd].groupby(["region", "condition"])[col].median().unstack()
        v = m.loc[VISR]
        ab = v[["active", "blanks"]].values; ns = v[["images", "spont"]].values
        mb = m.loc[[r for r in REG if paula.REGION_AREA[r] == "MB"]]
        mbr = (mb.max(axis=1) - mb.min(axis=1))
        ok = bool(within(ab, *widen(0.08, 0.13)).all() and (ns < 0.011).all() and (mbr < 0.02).all())
        print(f"{rd}, {col}: VIS active/blanks {ab.min():.3f}-{ab.max():.3f} inside 0.072-0.143 {int(within(ab, *widen(0.08, 0.13)).sum())}/12; "
              f"images/spont {ns.min():.4f}-{ns.max():.4f} below 0.011 {int((ns < 0.011).sum())}/12; MB range across conditions {mbr.round(4).to_dict()}; passes {ok}")
        if rd == "a/a" and col == "corr50":
            print(m.loc[VISR + list(mb.index)].round(4).to_string())

# %% md
# **Result: ...**

# %% md
# ## complexity-separates-images-from-spontaneous
#
# > Neither CV nor mean pairwise correlation separates natural image presentation from spontaneous activity in visual cortex, while statistical complexity does.

# %% code claim:complexity-separates-images-from-spontaneous
for rd in W:
    w = W[rd]
    for nb in (50, 100):
        rows = []
        for r in VISR:
            x = w[w.region == r]
            a, b = x[x.condition == "images"], x[x.condition == "spont"]
            row = {"region": r}
            for col in ["C", "cv", "corr50"]:
                row[f"JS {col}"] = paula.js_divergence(a[col], b[col], nb)
                qa, qb = a[col].quantile([0.25, 0.75]).values, b[col].quantile([0.25, 0.75]).values
                row[f"IQR overlap {col}"] = bool(qa[0] <= qb[1] and qb[0] <= qa[1])
            rows.append(row)
        t = pd.DataFrame(rows).set_index("region")
        js_ok = ((t["JS C"] > t["JS cv"]) & (t["JS C"] > t["JS corr50"])).sum()
        iqr_ok = ((~t["IQR overlap C"]) & t["IQR overlap cv"] & t["IQR overlap corr50"]).sum()
        print(f"{rd}, {nb} bins: complexity separates while CV and correlation do not, JS reading {js_ok}/6, IQR reading {iqr_ok}/6")
        if rd == "a/a" and nb == 50:
            print(t.round(3).to_string())

# %% md
# **Result: ...**
EOF
$TMPDIR/dev.sh 101 2>&1 | head -300
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
----- cell 102 
JS of C, reading a/a, 50 bins, mean by area pair:
images {'VIS-VIS': 0.123, 'TH-VIS': 0.488, 'TH-TH': 0.184, 'HP-VIS': 0.528, 'HP-TH': 0.135, 'HP-HP': 0.088, 'HP-MB': 0.173, 'MB-VIS': 0.464, 'MB-TH': 0.213, 'MB-MB': 0.275}
active {'VIS-VIS': 0.185, 'TH-VIS': 0.399, 'TH-TH': 0.118, 'HP-VIS': 0.157, 'HP-TH': 0.28, 'HP-HP': 0.14, 'HP-MB': 0.305, 'MB-VIS': 0.418, 'MB-TH': 0.132, 'MB-MB': 0.184}
blanks {'VIS-VIS': 0.167, 'TH-VIS': 0.301, 'TH-TH': 0.117, 'HP-VIS': 0.163, 'HP-TH': 0.237, 'HP-HP': 0.152, 'HP-MB': 0.275, 'MB-VIS': 0.331, 'MB-TH': 0.15, 'MB-MB': 0.2}
spont {'VIS-VIS': 0.046, 'TH-VIS': 0.085, 'TH-TH': 0.138, 'HP-VIS': 0.464, 'HP-TH': 0.476, 'HP-HP': 0.293, 'HP-MB': 0.445, 'MB-VIS': 0.167, 'MB-TH': 0.227, 'MB-MB': 0.261}

----- cell 104 ['claim:fig4e-js-complexity-natural-images']
a/a, 50 bins: VIS-VIS below 0.22 0.87 (range 0.019-0.235); VIS-TH above 0.36 0.74 (median 0.463); VIS-MB above 0.36 0.63 (median 0.414); DG/CA3 pairs in 0.27-0.55 0.20 (median 0.161); passes False
a/a, 100 bins: VIS-VIS below 0.22 0.73 (range 0.034-0.252); VIS-TH above 0.36 0.74 (median 0.471); VIS-MB above 0.36 0.67 (median 0.434); DG/CA3 pairs in 0.27-0.55 0.20 (median 0.176); passes False
a/b, 50 bins: VIS-VIS below 0.22 0.87 (range 0.019-0.235); VIS-TH above 0.36 0.74 (median 0.463); VIS-MB above 0.36 0.63 (median 0.414); DG/CA3 pairs in 0.27-0.55 0.20 (median 0.161); passes False
a/b, 100 bins: VIS-VIS below 0.22 0.73 (range 0.034-0.252); VIS-TH above 0.36 0.74 (median 0.471); VIS-MB above 0.36 0.67 (median 0.434); DG/CA3 pairs in 0.27-0.55 0.20 (median 0.176); passes False
b/a, 50 bins: VIS-VIS below 0.22 0.87 (range 0.019-0.235); VIS-TH above 0.36 0.74 (median 0.463); VIS-MB above 0.3
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; grep -n "^- id:" claims/paula-2026.yaml | wc -l; grep -c "Result: \.\.\." $TMPDIR/nb.py; grep -n "^# ## " $TMPDIR/nb.py | head -60
```

```
Fri Nov 27 11:11:44 UTC 2026
38
37
30:# ## Loading
78:# ## table1-sample
170:# ## fig1c-cv-region-medians
220:# ## fig1c-cv-above-surrogate
271:# ## fig1d-surrogate-abolishes-cv-correlations
332:# ## fig1e-positive-cv-modules
358:# ## fig1e-dg-ca3-anticorrelation-hubs
378:# ## fig1e-midbrain-weakest-cv-correlations
399:# ## Medians of CV by condition (claims of Fig. 2a)
438:# ## fig2a-vis-cv-by-condition
461:# ## fig2a-thalamus-cv-by-condition
479:# ## fig2a-hippocampus-cv-stable
498:# ## fig2a-midbrain-cv-invariant
511:# ## JS divergence matrices of CV (claims of Fig. 2b)
534:# ## fig2b-vis-summed-js-cv
557:# ## fig2b-hp-mb-summed-js-cv
579:# ## fig2b-visually-driven-js-cv-low
[... 28 more lines not kept]
```

**Agent**

Clock: 11:12 UTC, ahead of plan. All 38 claims compute; now writing the conclusion cells and summary.

**Agent calls Bash**

```bash
cat > $TMPDIR/conclusions.py <<'PYEOF'
C = {}
C["fig1c-cv-region-medians"] = "**Result: not reproduced.** Visual cortex matches (medians 0.426 to 0.644, extremes within tolerance) and DG has the highest hippocampal median, but the lowest thalamic median (PIL 0.306) is above 0.27 +/- 0.027, the highest hippocampal (DG 0.564) above 0.49 +/- 0.049 and the highest midbrain (NB 0.564) above 0.45 +/- 0.045; the IQRs fall inside their ranges in 16 of 26 subregions. The 'qc' variant misses too (highest thalamic median LP 0.414). The outcome rests on the unit-selection assumption."
C["fig1c-cv-above-surrogate"] = "**Result: partially reproduced.** Empirical CV is above the surrogate CV in every subregion and every area, Mann-Whitney p below 1e-72 in all 26 subregions and p = 0 at printed precision for the four areas, and the visual surrogate medians (0.226 to 0.243) lie in 0.189 to 0.264. The ratios lie in their area's widened range in 24 of 26 subregions: DG (3.01) and POST (1.32) fall outside the hippocampal 1.35 to 2.42. All five seeds give the same result (ratios 1.314 to 3.009). The outcome rests on the unit-selection assumption."
C["fig1d-surrogate-abolishes-cv-correlations"] = "**Result: not reproduced.** The empirical correlations are present (largest 0.772 under reading a and 0.669 under b), but the surrogate ones are not abolished: 115 of 325 pairs (reading a) and 213 (reading b) have |r| above 0.2, largest 0.791 and 0.662. The ISI shuffle keeps each window's spike count, so the surrogate CV still follows the rate of each 100-s window, and those rates co-vary across regions. The outcome rests on the unit-selection assumption."
C["fig1e-positive-cv-modules"] = "**Result: partially reproduced.** The strongest 10% of pairs join subregions of the same major area in most cases (21 of 32 under reading a, 26 of 32 under b), mostly visual areas with each other and thalamic or subicular pairs. The range misses at one end under each reading: 0.459 to 0.772 under a (high end above 0.737), 0.450 to 0.669 under b (low end at the edge of 0.45, below it before rounding). The outcome rests on the unit-selection assumption."
C["fig1e-dg-ca3-anticorrelation-hubs"] = "**Result: partially reproduced.** Under reading b, CA3 (17) and DG (14) are the subregions in most of the 32 most negative pairs, but the most negative value is -0.178, not -0.27 +/- 0.027. Under reading a, NB leads (15) and the most negative value is -0.496. The outcome rests on the unit-selection assumption."
C["fig1e-midbrain-weakest-cv-correlations"] = "**Result: partially reproduced.** Under reading b the midbrain has the lowest mean |r| of the four areas (0.201 against 0.235 to 0.334), but only 2 of its 115 pairs lie in -0.044 to 0.033. Under reading a, hippocampus is lowest (0.179 against midbrain 0.186) and 16 of 115 midbrain pairs are near zero. The outcome rests on the unit-selection assumption."
C["fig2a-vis-cv-by-condition"] = "**Result: reproduced.** Under readings a/a and b/a all twelve medians are within tolerance (for example VISp 0.644, 0.602, 0.316 and 0.418 against 0.59, 0.55, 0.29 and 0.39), and the order active > images > spontaneous with blanks > spontaneous holds in the three areas under every reading. Under the 'qc' variant 8 of 12 are within tolerance. The outcome rests on the unit-selection assumption."
C["fig2a-thalamus-cv-by-condition"] = "**Result: reproduced.** Under every reading the four medians are within tolerance (LP 0.396 and 0.286, LGd 0.330 and 0.226 against 0.37, 0.28, 0.32 and 0.23), and the active minus spontaneous difference of LP (0.110) and LGd (0.104) is below that of VISp, VISl and VISal (0.271 to 0.327). The outcome rests on the unit-selection assumption."
C["fig2a-hippocampus-cv-stable"] = "**Result: partially reproduced.** The pattern holds: DG and CA3 vary little across the visually driven conditions (DG 0.555 to 0.576, CA3 0.449 to 0.458), CA1 is 0.263 to 0.266, and the spontaneous medians of DG and CA3 exceed their visually driven ones under every reading. CA3 and CA1 are within tolerance, and CA3 spontaneous (0.471) under the spontaneous reading b, but DG is higher than the paper's values (0.555 to 0.580 against 0.48 to 0.51). The outcome rests on the unit-selection assumption."
C["fig2a-midbrain-cv-invariant"] = "**Result: partially reproduced.** The APN median is 0.146 to 0.172 across conditions, within 0.16 +/- 0.016 in each, and the MRN lowest median (0.185 to 0.186) is within 0.20 +/- 0.02, but the MRN highest (0.233, natural images) is just above 0.21 +/- 0.021. The outcome rests on the unit-selection assumption."
C["fig2b-vis-summed-js-cv"] = "**Result: partially reproduced.** No combination of readings meets the full rule. Under condition readings a/a and b/a with 50 bins and the sum over all within-area pairs, active and blank screens are the closest pair (0.32% and 0.53% apart) and the other pairs differ by 23% to 40%, which meets the partial rule (4 of 32 combinations); the four pairs against natural images or spontaneous activity are 23% to 40%, not all within 27% to 33%. With 100 bins or the adjacent-pair sum, active and blanks are 3.8% to 9.5% apart and not always the closest pair. The outcome depends on the histogram and sum readings, and rests on the unit-selection assumption."
C["fig2b-hp-mb-summed-js-cv"] = "**Result: not reproduced.** Active against spontaneous is the largest hippocampal difference under every combination, as the paper says, but it is 41% to 71%, not 15% +/- 1.5%, and the largest midbrain difference is 22% to 41%, not at most 7.7%; the midbrain has the smallest difference in at most 4 of the 6 pairs. The outcome rests on the unit-selection assumption."
C["fig2b-visually-driven-js-cv-low"] = "**Result: reproduced.** Under the second reading the criterion names (the legend's JS values), most VIS-VIS divergences are at most 0.22 in each visually driven condition (fractions 0.73 to 1.0) under every condition and histogram reading. Under the percentage reading no combination has two of the three pairs at or below 4.4% (active against blanks is 0.3% to 9.5%, the pairs with natural images 16% to 40%). The outcome rests on the second reading and on the unit-selection assumption."
C["fig2b-dg-ca3-high-js-cv"] = "**Result: partially reproduced.** The median divergence of DG and of CA3 from the other subregions is largest in spontaneous activity under every reading, and DG's spontaneous median (0.744 to 0.805) is within 0.84 +/- 0.084, but CA3's spontaneous median is 0.450 to 0.544 and the blank-screen medians are 0.461 to 0.489 (DG) and 0.227 to 0.249 (CA3), against 0.84 and 0.63. The hippocampal-only variant gives DG 0.762 to 0.805 and CA3 0.555 to 0.638 in spontaneous activity, with blanks still below 0.63 for CA3. The outcome rests on the unit-selection assumption."
C["fig2b-legend-js-cv"] = "**Result: not reproduced.** Under reading a, 3 of 6 visual subregions exceed 0.44 (not more than half), at most 1 of 9 thalamic subregions exceeds 0.33, and the DG and CA3 values (0.004 to 0.122) lie below 0.135; under reading b no visual or thalamic subregion passes. Most midbrain values are below 0.165 under both readings. The outcome rests on the unit-selection assumption."
C["fig3a-reference-systems"] = "**Result: partially reproduced.** White noise is at H 0.999, C 0.001, and the logistic map (r = 4) and tent map (mu = 1.9999) are at H 0.63, C 0.48, inside the chaotic range. The sine (1000 points per period) is at H 0.115 and C 0.113, just outside the reading of near 0 and 0.09 to 0.11; the Ikeda map with u = 0.9 lies at H 0.11 to 0.38 for p in [5, 17], not near maximum complexity; and the exponentially correlated walks with H in 0.27 to 0.66 have C 0.233 to 0.334, partly below 0.27. The parameters of Fig. 3a are not in the text, so these positions rest on the parameter readings shown."
C["fig3b-complexity-levels-by-region"] = "**Result: reproduced.** Under reading a (the 36 active windows), the mean C over windows is 0.161 (VIS), 0.163 (HP), 0.109 (TH) and 0.101 (MB), each within its tolerance, and the order MB < TH < VIS and HP holds at all 36 window indices. Under reading b (natural images) hippocampus falls below thalamus (0.108 against 0.117) and the order holds at none of the 8 indices. The 'qc' variant also holds at 36 of 36. The outcome rests on reading a and on the unit-selection assumption."
C["fig3c-vis-ch-plane"] = "**Result: partially reproduced.** The test holds: C of the visual windows is above that of their surrogates (median 0.152 against 0.0955, Mann-Whitney p = 0 at printed precision under all five seeds), and the surrogate median lies in 0.09 to 0.22. The 2.5th to 97.5th percentile span of H (0.856 to 0.965) is inside 0.72 to 1.10, but that of C starts at 0.089, just below 0.090; the 0th to 100th span misses on H (0.462). There are 31 956 active windows against the paper's 21 084. The outcome rests on the unit-selection assumption."
C["fig3d-th-ch-plane"] = "**Result: reproduced.** The thalamic span (H 0.928 to 0.969, C 0.080 to 0.171, 2.5th to 97.5th percentiles) is inside the widened ranges, its C span (0.091) is narrower than that of visual cortex (0.196), and C is above the surrogate's (p = 0 at printed precision, all five seeds). The 0th to 100th span misses on C (up to 0.344). The outcome rests on the percentile reading of a span and on the unit-selection assumption."
C["fig3e-hp-ch-plane"] = "**Result: reproduced.** The hippocampal span (H 0.857 to 0.966, C 0.086 to 0.298) is inside the widened ranges, its C span (0.212) is the widest of the four areas, and C is above the surrogate's (p = 0 at printed precision, all five seeds). The 0th to 100th span misses on H (0.124) and C (0.441, against 0.440). The outcome rests on the percentile reading of a span and on the unit-selection assumption."
C["fig3f-mb-ch-plane"] = "**Result: reproduced.** The midbrain span (H 0.935 to 0.970, C 0.076 to 0.157) is inside the widened ranges, its C span (0.081) is the narrowest of the four, and C is above the surrogate's (Mann-Whitney p = 2.3e-194, at most 7.3e-192 over five seeds). Under the 0th to 100th span it misses on H and is not the narrowest. The outcome rests on the percentile reading of a span and on the unit-selection assumption."
C["fig3-complexity-range-fractions"] = "**Result: not reproduced.** None of the eight fractions is within tolerance on the active windows (for example VIS 10.07% in [0, 0.1) against 4.9%, MB 37.30% in [0.1, 0.2) against 45.4%), one on the natural-image windows, and none under the 'qc' variant. The outcome rests on the unit-selection assumption."
C["fig4a-vis-complexity-by-condition"] = "**Result: partially reproduced.** All medians fall in the quoted ranges: natural images 0.160 to 0.265, spontaneous 0.094 to 0.098, active and blanks 0.101 to 0.190. The order holds in five of six areas: in VISp the natural-image median (0.178) is below the active one (0.190) and equal to the blank one, and 35 of 36 pairwise tests give p < 0.001 (VISp images against blanks p = 0.46 to 0.53). The legend's narrower ranges for VISl, VISal and VISp are met. The outcome rests on the unit-selection assumption."
C["fig4b-thalamus-lgd-lp-modulated"] = "**Result: reproduced.** LGd and LP are modulated under both test readings (Kruskal-Wallis p = 7e-69 and 3e-63; every visually driven condition against spontaneous p at most 9e-24 and 2e-17), their visually driven medians (0.113 to 0.152) exceed the spontaneous ones (0.093 to 0.100) and match the legend's values, not the text's (LGd active 0.121 is below 0.126). Their effect is smaller than that of every visual area when the effect is the largest visually driven median minus the spontaneous one (LGd 0.059, LP 0.043 against 0.066 to 0.170), but not when it is the mean of the three (LGd 0.036 against VISrl 0.030); the first is adopted as an assumption. Under Kruskal-Wallis, MGd, SGN, MGm and MGv also reach p < 0.001, so the statement's \"only\" holds under the pairwise reading alone."
C["fig4b-other-thalamus-not-modulated"] = "**Result: reproduced.** The medians of the seven nuclei are 0.093 to 0.108, inside 0.09 to 0.143, and their largest condition difference is at most 0.006. Under the pairwise Mann-Whitney reading (every visually driven condition against spontaneous), adopted as the paper's test, none reaches p < 0.001 (smallest largest-p 0.004, SGN). Under the Kruskal-Wallis reading four of them (MGd, SGN, MGm, MGv) reach p < 0.001, which would make the claim not reproduced; the outcome rests on the test reading and the unit-selection assumption."
C["fig4c-dg-ca3-complexity"] = "**Result: reproduced.** Under the legend's reading with the spontaneous reading b (a/b and b/b), DG natural images 0.115, CA3 0.108 and CA1 0.096 match the legend's low values, DG (0.178 to 0.257), CA3 (0.137 to 0.196) and CA1 (0.120 to 0.163) match their elevated ranges in the other conditions, POST, ProS and SUB lie in 0.097 to 0.136, and DG and CA3 peak in spontaneous activity. Under the spontaneous reading a, CA3's spontaneous median (0.198) rounds just above the legend's 0.198 bound and fails. The text's reading fails because CA1 and SUB fall below 0.099 in natural images. The outcome rests on the legend reading and the unit-selection assumption."
C["fig4d-midbrain-complexity-invariant"] = "**Result: reproduced.** Under the legend's values every condition median of NB (0.107 to 0.110), MRN (0.096 to 0.100), SCig (0.097 to 0.102) and APN (0.086 to 0.090) lies in its widened range, and NOT has the largest range across conditions (0.072 to 0.073 against at most 0.004). Under the text's values APN (0.086 to 0.090) falls below 0.09. The outcome rests on the legend reading and the unit-selection assumption."
C["fig4e-js-complexity-natural-images"] = "**Result: partially reproduced.** In natural images most VIS-VIS divergences are below 0.22 (0.73 to 0.87), and most VIS-TH (0.74) and VIS-MB (0.63 to 0.67) divergences exceed 0.36, but only 0.20 of the pairs of DG or CA3 with other subregions lie in 0.27 to 0.55 (median 0.161 to 0.176). The outcome rests on the unit-selection assumption."
C["fig4fg-js-complexity-active-blanks"] = "**Result: not reproduced.** Fewer than half of the pairs of a visual subregion with a subcortical one exceed 0.36 (0.38 in active behavior, 0.29 to 0.31 in blanks; medians 0.193 to 0.259), and 0.27 to 0.33 of the hippocampal pairs in active behavior lie in 0.18 to 0.44. The outcome rests on the unit-selection assumption."
C["fig4h-js-complexity-spontaneous-converges"] = "**Result: not reproduced.** The mean visual-to-other divergence is lowest in spontaneous activity (0.208 to 0.262 against 0.267 to 0.511), as the statement says, but the mean of all pairs is not (0.264 to 0.332 in spontaneous against 0.218 to 0.310 in the others), only 0.27 to 0.35 of the spontaneous visual-to-other pairs lie in 0.18 to 0.44, and midbrain pairs are below 0.22 in at most half of them in spontaneous activity. The outcome rests on the unit-selection assumption."
C["supp-robustness-parameters"] = "**Result: partially reproduced.** The pattern (natural images above spontaneous in every visual area, and a larger visually driven minus spontaneous difference in visual cortex than in midbrain) holds for 4 of the 5 combinations; with bin 20 ms, D = 3, tau = 4 natural images exceed spontaneous in 2 of 6 visual areas and the visual difference is -0.0002. The outcome rests on this notebook's form of the area difference and the unit-selection assumption."
C["fig5-vis-complexity-cv-coupling"] = "**Result: partially reproduced.** Complexity rises with CV in visual cortex in the three visually driven conditions (Spearman 0.62 to 0.83, and monotonic under bins of 0.1 with at least 10 windows), but no reading matches the spans: for example the natural-image bins reach CV 1.05 to 1.30 against 0.9, and the spontaneous maximum of the bin means is 0.180 to 0.357, not below 0.165. The outcome rests on the unit-selection assumption."
C["fig5-th-weaker-coupling"] = "**Result: partially reproduced.** In each visually driven condition the thalamic slope is positive and below the visual one (0.084 to 0.111 against 0.216 to 0.350), but the thalamic spans are wider than CV 0.18 to 0.88 and C 0.09 to 0.22 under every reading (for example CV 0.10 to 1.40 in active behavior with at least 10 windows per bin). The outcome rests on the unit-selection assumption."
C["fig5-hp-spontaneous-elevated"] = "**Result: not reproduced.** The hippocampal spontaneous bin means at CV 0.4 to 0.7 reach 0.238 to 0.244, within 0.25 +/- 0.025, but they do not exceed the hippocampal maxima of the visually driven conditions (active 0.324 to 0.410), which are not within 0.19 +/- 0.019. The outcome rests on the unit-selection assumption."
C["fig5-mb-flat"] = "**Result: partially reproduced.** The midbrain slope of C on CV is the smallest of the four areas in all four conditions (0.042 to 0.072), but its bin means leave 0.09 to 0.143 in three conditions under every reading (for example 0.085 to 0.170 in active behavior with at least 10 windows per bin). The outcome rests on the unit-selection assumption."
C["supp-fig6-mean-correlation"] = "**Result: not reproduced.** The visual medians in active behavior and blanks are 0.014 to 0.052 (50 ms) and 0.007 to 0.029 (20 ms), below 0.072, and the natural-image and spontaneous medians are 0.005 to 0.037, mostly above 0.011. Midbrain medians vary by less than 0.02 across conditions except NOT (0.024 to 0.025 at 50 ms). The outcome rests on the unit-selection assumption."
C["complexity-separates-images-from-spontaneous"] = "**Result: reproduced.** Under the JS reading, in all six visual subregions the divergence between natural images and spontaneous activity is larger for complexity (0.443 to 0.849, reading a/a, 50 bins) than for CV (0.198 to 0.544) and mean correlation (0.142 to 0.434), under every condition and histogram reading. Under the IQR reading it holds in 1 or 2 of 6, since the CV and correlation IQRs often do not overlap either. The outcome rests on the JS reading and the unit-selection assumption."
PYEOF
python - <<'EOF'
import re, os
exec(open(os.environ['TMPDIR']+'/conclusions.py').read())
s=open(os.environ['TMPDIR']+'/nb.py').read()
parts=s.split("# **Result: ...**")
out=parts[0]
for p in parts[1:]:
    # find the last claim heading before this placeholder
    ids=re.findall(r"^# ## ([a-z0-9-]+)$", out, re.M)
    cid=ids[-1]
    out+="# "+C[cid]+p
open(os.environ['TMPDIR']+'/nb.py','w').write(out)
print(s.count("Result: ...")-out.count("Result: ..."), "replaced")
EOF
```

```
37 replaced
```

**Agent**

Conclusions written. Small fixes, then adding per-seed surrogate CV series so fig1d also gets the five-seed check.

**Agent calls Bash**

```bash
cd entries/paula-2026 && python - <<'EOF'
import os
p='paula.py'; s=open(p).read()
s=s.replace('''        if j == 0:
            out["s_cv10"] = cvs''','''        out["s_cv10" + sfx] = cvs''')
s=s.replace('''                c10, s10 = m.pop("cv10"), m.pop("s_cv10")''','''                c10 = m.pop("cv10")
                s10 = {k: m.pop(k) for k in [k for k in m if k.startswith("s_cv10")]}''')
s=s.replace('''                    cv10.append({"session": sess_i, "units": ur, "region": region, "k": k,
                                 "cv10": c10, "s_cv10": s10})''','''                    cv10.append({"session": sess_i, "units": ur, "region": region, "k": k,
                                 "cv10": c10, **s10})''')
open(p,'w').write(s)
t=os.environ['TMPDIR']+'/nb.py'; s=open(t).read()
s=s.replace("Most midbrain values are below 0.165 under both readings.","Most midbrain values are below 0.165 under reading b, and under reading a with 50 bins.")
s=s.replace("and the natural-image and spontaneous medians are 0.005 to 0.037, mostly above 0.011.","and the natural-image and spontaneous medians are 0.005 to 0.037, half or more of them above 0.011.")
s=s.replace("every visually driven condition against spontaneous p at most 9e-24 and 2e-17)","every visually driven condition against spontaneous p at most 9e-24 and 2e-17 under reading a/a)")
s=s.replace("(LGd 0.059, LP 0.043 against 0.066 to 0.170)","(LGd 0.057 to 0.059, LP 0.043 to 0.044 against 0.065 to 0.170)")
s=s.replace("Under the spontaneous reading a, CA3's spontaneous median (0.198) rounds just above the legend's 0.198 bound and fails.","Under the spontaneous reading a, CA3's spontaneous median (printed 0.198) lies just above the widened bound 0.198 and the reading fails.")
# fig1d: five seeds for surrogate
s=s.replace('''series = {}
for (s, r), g in cvs.groupby(["session", "region"]):
    series[(s, r)] = (np.concatenate(list(g.cv10)), np.concatenate(list(g.s_cv10)))''','''SCOLS = ["s_cv10" + x for x in SFX]
series = {}
for (s, r), g in cvs.groupby(["session", "region"]):
    series[(s, r)] = [np.concatenate(list(g.cv10))] + [np.concatenate(list(g[c])) for c in SCOLS]''')
s=s.replace('''plt.colorbar(im, ax=ax); plt.show()''','''plt.colorbar(im, ax=ax); plt.show()
for k, sfx in enumerate(SFX[1:], start=2):
    sa, sb, _ = corr_mats(k)
    va, vb = np.abs(sa.values[iu]), np.abs(sb.values[iu])
    print(f"surrogate seed{sfx}: max |r| reading a {np.nanmax(va):.3f} (pairs > 0.2: {int((va > 0.2).sum())}), reading b {np.nanmax(vb):.3f} (pairs > 0.2: {int((vb > 0.2).sum())})")''')
open(t,'w').write(s)
EOF
grep -n "s_cv10" paula.py
```

```
266:        out["s_cv10" + sfx] = cvs
484:                s10 = {k: m.pop(k) for k in [k for k in m if k.startswith("s_cv10")]}
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/nb.py <<'EOF'

# %% md
# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | table1-sample | not reproduced |
# | fig1c-cv-region-medians | not reproduced (assumed) |
# | fig1c-cv-above-surrogate | partially reproduced (assumed) |
# | fig1d-surrogate-abolishes-cv-correlations | not reproduced (assumed) |
# | fig1e-positive-cv-modules | partially reproduced (assumed) |
# | fig1e-dg-ca3-anticorrelation-hubs | partially reproduced (assumed) |
# | fig1e-midbrain-weakest-cv-correlations | partially reproduced (assumed) |
# | fig2a-vis-cv-by-condition | reproduced (assumed) |
# | fig2a-thalamus-cv-by-condition | reproduced (assumed) |
# | fig2a-hippocampus-cv-stable | partially reproduced (assumed) |
# | fig2a-midbrain-cv-invariant | partially reproduced (assumed) |
# | fig2b-vis-summed-js-cv | partially reproduced (assumed) |
# | fig2b-hp-mb-summed-js-cv | not reproduced (assumed) |
# | fig2b-visually-driven-js-cv-low | reproduced (assumed) |
# | fig2b-dg-ca3-high-js-cv | partially reproduced (assumed) |
# | fig2b-legend-js-cv | not reproduced (assumed) |
# | fig3a-reference-systems | partially reproduced (synthetic series) |
# | fig3b-complexity-levels-by-region | reproduced (assumed) |
# | fig3c-vis-ch-plane | partially reproduced (assumed) |
# | fig3d-th-ch-plane | reproduced (assumed) |
# | fig3e-hp-ch-plane | reproduced (assumed) |
# | fig3f-mb-ch-plane | reproduced (assumed) |
# | fig3-complexity-range-fractions | not reproduced (assumed) |
# | fig4a-vis-complexity-by-condition | partially reproduced (assumed) |
# | fig4b-thalamus-lgd-lp-modulated | reproduced (assumed) |
# | fig4b-other-thalamus-not-modulated | reproduced (assumed) |
# | fig4c-dg-ca3-complexity | reproduced (assumed) |
# | fig4d-midbrain-complexity-invariant | reproduced (assumed) |
# | fig4e-js-complexity-natural-images | partially reproduced (assumed) |
# | fig4fg-js-complexity-active-blanks | not reproduced (assumed) |
# | fig4h-js-complexity-spontaneous-converges | not reproduced (assumed) |
# | supp-robustness-parameters | partially reproduced (assumed) |
# | fig5-vis-complexity-cv-coupling | partially reproduced (assumed) |
# | fig5-th-weaker-coupling | partially reproduced (assumed) |
# | fig5-hp-spontaneous-elevated | not reproduced (assumed) |
# | fig5-mb-flat | partially reproduced (assumed) |
# | supp-fig6-mean-correlation | not reproduced (assumed) |
# | complexity-separates-images-from-spontaneous | reproduced (assumed) |
#
# "Assumed" marks an outcome that rests on a choice the paper does not make; the first of them, for every claim on the recordings, is the unit selection: all units of the units table, the reading that keeps Table I's 26 subregions, since neither reading of the claims file reproduces the paper's counts.
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.
#
# **How the analysis differs from the paper's.** The paper's 102 sessions are not identified, and every one of the 153 ecephys sessions of the dandiset meets both session readings, so all 153 are used; the populations and windows are about 1.5 times the paper's. The unit filter is not stated; neither reading gives Table I's neuron counts. The surrogate of each window is drawn once under the seed of `fig1c-cv-above-surrogate` (and four more) and serves every claim on surrogates. The JS histograms, spans, the blank and spontaneous windows, the test of "modulation" and several effect sizes are readings named in the claims file or in the claim sections above, each shown.
#
# **What was found about the dataset.** The 153 sessions (81 mice) each hold an active block of 3599 to 3611 s, a 289-s gray screen after it and eight images; no recording appears twice (no shared spike-time fingerprint, spike count, or subject and start time). The visual cortex responds to every session's flash onsets and not to onsets shifted into the gray screen or to omitted flashes, so the spike times and the stimulus table share a clock in all 153 sessions. The blank series are about 287 s long (median), not the "approximately 240 s" of Methods II.A. The location labels include generic ones (`TH`, `MB`, `HPF`) for units the atlas did not assign to a subregion.
EOF
cd entries/paula-2026 && . $TMPDIR/venv/bin/activate && python - <<'EOF'
import paula, pickle, os, time
d=pickle.load(open(os.environ['TMPDIR']+'/sess.pkl','rb'))
t=time.time(); meta,df,cv=paula.compute_session(149,*d); print(time.time()-t, df.shape, list(cv[0].keys()))
EOF
```

```
29.57788109779358 (1792, 42) ['session', 'units', 'region', 'k', 'cv10', 's_cv10', 's_cv10_s1000', 's_cv10_s2000', 's_cv10_s3000', 's_cv10_s4000']
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import pickle, os
metas,df,cv,failed=pickle.load(open('full.pkl','rb'))
for r in cv:
    for s in ['_s1000','_s2000','_s3000','_s4000']: r['s_cv10'+s]=r['s_cv10']
pickle.dump((metas,df,cv,failed),open('full.pkl','wb'))
EOF
$TMPDIR/dev.sh 0 2>&1 | grep -n "ERROR\|surrogate seed" | head; date -u
```

```
177:surrogate seed_s1000: max |r| reading a 0.791 (pairs > 0.2: 115), reading b 0.662 (pairs > 0.2: 213)
179:surrogate seed_s2000: max |r| reading a 0.791 (pairs > 0.2: 115), reading b 0.662 (pairs > 0.2: 213)
181:surrogate seed_s3000: max |r| reading a 0.791 (pairs > 0.2: 115), reading b 0.662 (pairs > 0.2: 213)
183:surrogate seed_s4000: max |r| reading a 0.791 (pairs > 0.2: 115), reading b 0.662 (pairs > 0.2: 213)
Fri Nov 27 11:15:15 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && . $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/nb.py reproduce_paula_2026.ipynb && printf "h5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\n" > requirements.in && cat > entry.yaml <<'EOF'
schema_version: 1
name: paula-2026
type: reproduction
title: Statistical complexity of population activity across brain regions (de Paula et al. 2026)
description: Tests the findings of de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli and de
  Vasconcelos (2026) on dandiset 000713, the Allen Institute Visual Behavior Neuropixels dataset. It computes
  the coefficient of variation, permutation entropy and statistical complexity of the population rate of each
  local population in 100-s windows of active behavior, natural images, blank screens and spontaneous activity,
  with ISI-shuffled surrogates, JS divergences between regions, complexity-CV trajectories and mean pairwise
  correlations, over all 153 ecephys sessions.
license: Apache-2.0
notebooks:
- path: reproduce_paula_2026.ipynb
  title: Reproducing de Paula et al. (2026) from dandiset 000713
  runtime_minutes: 40
helpers:
- paula.py
related:
- id: dandi:000713/0.240702.1725
  relation: uses_data
- id: doi:10.1103/wndc-k654
  relation: reproduces
EOF
ls; cd .. && cd .. && python tools/entry.py lock entries/paula-2026 2>&1 | tail -5
```

```
136 cells
__pycache__
entry.yaml
paula.py
reproduce_paula_2026.ipynb
requirements.in
wrote paula-2026/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent calls Bash**

```bash
rm -rf entries/paula-2026/__pycache__; python tools/entry.py check entries/paula-2026 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Write**

```json
{
 "file_path": "entries/paula-2026/README.md",
 "content": "# de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli & de Vasconcelos (2026) from dandiset 000713\n\nTests the findings of [de Paula et al. (2026)](https://doi.org/10.1103/wndc-k654), \"Revealing\nStimulus-Dependent Dynamics Through Statistical Complexity\", on\n[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute Visual\nBehavior Neuropixels dataset. The notebook streams all 153 ecephys sessions and computes, for every\nlocal population and 100-s window, the CV, permutation entropy and statistical complexity of the\npopulation rate, with ISI-shuffled surrogates, JS divergences between regions, complexity-CV\ntrajectories and mean pairwise correlations.\n\n| Claims | Outcome |\n|---|---|\n| CV by condition in visual cortex and thalamus; complexity time course by area; thalamic, hippocampal and midbrain complexity by condition; C-H spans of thalamus, hippocampus and midbrain; complexity separates images from spontaneous activity (13 claims) | Reproduced |\n| CV against surrogates; CV correlation modules and hubs; hippocampal and midbrain CV; JS of CV in visual cortex and DG/CA3; reference systems; visual C-H plane; complexity by condition in visual cortex; JS of complexity in natural images; parameter robustness; complexity-CV coupling in visual cortex, thalamus and midbrain (15 claims) | Partially reproduced |\n| Table I counts; CV medians by region; surrogate CV correlations; JS of CV in hippocampus and midbrain and in the Fig. 2b legend; complexity range fractions; JS of complexity in active behavior, blanks and spontaneous activity; hippocampal spontaneous complexity; mean pairwise correlation (10 claims) | Not reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe paper's 102 sessions and its unit selection are not stated, and neither reading of them in the\nclaims file reproduces its counts (Table I). The notebook uses all 153 sessions and all units, the\nreading that keeps Table I's 26 subregions, so almost every outcome rests on that assumption. The\nattempt record, with the reasons and the differences from the paper's method, is\n[`attempts/paula-2026-01.yaml`](../../attempts/paula-2026-01.yaml).\n\nThe notebook takes about 40 minutes, most of it reading the spike times from the archive.\n"
}
```

```
File created successfully at: entries/paula-2026/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; time python tools/entry.py all entries/paula-2026 2>&1 | tail -15; date -u
```

```
Fri Nov 27 11:15:54 UTC 2026
    )
nbclient.exceptions.CellTimeoutError: A cell timed out while it was being executed, after 3600 seconds.
The message was: Cell execution timed out.
Here is a preview of the cell contents:
-------------------
t0 = time.time()
sessions, n_assets = paula.list_sessions()
metas, windows, cv10_list, failed = paula.run_all(sessions, workers=4)
t_extract = time.time() - t0
print(f"{len(sessions)} session files of {n_assets} assets; extraction took {t_extract / 60:.1f} min")
-------------------


0 error(s)
FAIL  reproduce_paula_2026.ipynb  (3609 s)

real	60m18.275s
user	227m2.827s
sys	3m19.351s
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && ls ../../executed/paula-2026/ 2>/dev/null; ls -d ../../.venv* ../../executed/paula-2026/.venv 2>/dev/null; . $TMPDIR/venv/bin/activate; for order in "import numpy; import paula" "import paula"; do python -c "
$order
import pickle, os, time
d=pickle.load(open(os.environ['TMPDIR']+'/sess.pkl','rb'))
import numpy as np
t=time.time(); paula.mean_corr(np.sort(np.random.default_rng(0).random(100000)*100), np.random.default_rng(1).integers(0,200,100000), 200, 0.02)
t=time.time()
for _ in range(50): paula.mean_corr(np.sort(np.random.default_rng(0).random(100000)*100), np.random.default_rng(1).integers(0,200,100000), 200, 0.02)
print('$order', time.time()-t)
"; done
```

```
result.json
../../executed/paula-2026/.venv
import numpy; import paula 0.40839195251464844
import paula 0.3627488613128662
```

**Agent calls Bash**

```bash
cd  && grep -E "^(numpy|h5py|remfile|pandas|scipy)==" entries/paula-2026/requirements.lock.txt; . $TMPDIR/venv/bin/activate; python -c "import numpy,h5py,remfile,pandas,scipy;print(numpy.__version__,h5py.__version__,pandas.__version__,scipy.__version__)"; pip show remfile 2>/dev/null | grep Version; uv pip list --python $TMPDIR/venv/bin/python 2>/dev/null | grep -i remfile; cat executed/paula-2026/result.json | head -20; nproc; uptime
```

```
h5py==3.16.0 \
numpy==2.5.5 \
pandas==3.1.1 \
remfile==0.1.17 \
scipy==1.18.1 \
2.5.5 3.16.0 3.1.1 1.18.1
remfile                   0.1.17
{
 "entry": "paula-2026",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_paula_2026.ipynb",
   "ok": false,
   "seconds": 3609,
   "error": "ert/exporters/exporter.py\", line 154, in from_notebook_node\n    nb_copy, resources = self._preprocess(nb_copy, resources)\n                         ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^\n  File \"executed/paula-2026/.venv/lib/python3.13/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ~~~~~~~~~~~~^^^^^^^^^^^\n  File \"executed/paula-2026/.venv/lib/python3.13/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^\n  File \"executed/paula-2026/.venv/lib/python3.13/site-packages/nbconvert/preprocessors/execute.py\", line 103, in preprocess\n    self.preprocess_cell(cell, resources, index)\n    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"executed/paula-2026/.venv/lib/python3.13/site-packages/nbconvert/preprocessors/execute.py\", line 124, in preprocess_cell\n    cell = self.execute_cell(cell, index, store_history=True)\n  File \"executed/paula-2026/.venv/lib/python3.13/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/asyncio/base_events.py\", line 726, in run_until_complete\n    return future.result()\n           ~~~~~~~~~~~~~^^\n  File \"executed/paula-2026/.venv/lib/python3.13/site-packages/nbclient/client.py\", line 1005, in async_execute_cell\n    exec_reply = await self.task_poll_for_reply\n                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"executed/paula-2026/.venv/lib/python3.13/site-packages/nbclient/clie
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
ps aux --sort=-%cpu | head -12
```

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
runner         2 66.6  0.0  10224  5984 ?        S    12:16   0:00 /bin/bash -c source /home/runner/.claude/shell-snapshots/snapshot-bash-1795773799778-8ujc78.sh 2>/dev/null || true && export TMPDIR=/tmp/claude-1001 && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'ps aux --sort=-%cpu | head -12' < /dev/null && pwd -P >| /tmp/claude-1001/cwd-3ab5
runner         1 60.0  0.0   3804  1500 ?        Ss   12:16   0:00 bwrap --new-session --die-with-parent --setenv GIT_CONFIG_KEY_0 safe.directory --setenv GIT_CONFIG_VALUE_0  --setenv GIT_CONFIG_KEY_1 safe.directory --setenv GIT_CONFIG_VALUE_1 * --setenv GIT_CONFIG_COUNT 2 --ro-bind / / --ro-bind /home/runner /home/runner --ro-bind /opt/hostedtoolcache /opt/hostedtoolcache --ro-bind /run/containerd /run/containerd --ro-bind /tmp/claude-1001/-home-runner-work-encore-registry-encore-registry /tmp/claude-1001/-home-runner-work-encore-registry-encore-registry --ro-bind /home/runner/.config /home/runner/.config --ro-bind /home/runner/work /home/runner/work --ro-bind /home/runner/.local /home/runner/.local --ro-bind /opt/hostedtoolcache/node /opt/hostedtoolcache/node --ro-bind /opt/hostedtoolcache/Python /opt/hostedtoolcache/Python --ro-bind /home/runner/.cargo /home/runner/.cargo --ro-bind /home/runner/.dotnet /home/runner/.dotnet --ro-bind /home/runner/.claude /home/runner/.claude --ro-bind /tmp/claude-1001/-home-runner-work-encore-registry-encore-registry/b5cbc65b-4622-4766-806a-4e00b7e250d1 /tmp/claude-1001/-home-runner-work-encore-registry-encore-registry/b5cbc65b-4622-4766-806a-4e00b7e250d1 --ro-bind /home/runner/work/encore-registry /home/runner/work/encore-registry --ro-bind /opt/hostedtoolcache/node/22.23.5 /opt/hostedtoolcache/node/22.23.5 --ro-bind /opt/hostedtoolcache/Python/3.13.18 /opt/hostedtoolcache/Python/3.13.18 --ro-bind /home/runner/.config/co
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os
t=os.environ['TMPDIR']+'/nb.py'; s=open(t).read()
s=s.replace('''# %% code
import time, zlib, warnings
import numpy as np''','''# %% code
import os
for v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"  # set before numpy loads: the four worker processes each run many small fits
import time, zlib, warnings
import numpy as np''',1)
open(t,'w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/nb.py entries/paula-2026/reproduce_paula_2026.ipynb && deactivate; uptime; date -u; time python tools/entry.py all entries/paula-2026 2>&1 | tail -6; date -u
```

```
136 cells
 12:17:08 up  2:17,  0 users,  load average: 6.04, 11.88, 13.25
Fri Nov 27 12:17:08 UTC 2026
Installed kernelspec registry-paula-2026 in executed/paula-2026/.venv/share/jupyter/kernels/registry-paula-2026
0 error(s)
pass  reproduce_paula_2026.ipynb  (2209 s)

real	36m59.543s
user	107m51.394s
sys	7m28.951s
Fri Nov 27 12:54:07 UTC 2026
```

**Agent**

Run passed in 37 min. Checking the executed outputs against the conclusions.

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' > $TMPDIR/exec_out.txt
import nbformat, glob
p=glob.glob('executed/paula-2026/*.ipynb'); print(p)
nb=nbformat.read(p[0],4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        print(f'----- cell {i} {c.metadata.get("tags","")}')
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text)
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
grep -c ERROR $TMPDIR/exec_out.txt; diff <(grep -v "extraction took\|peak memory\|^\[" $TMPDIR/exec_out.txt | sed -n '1,4000p') <(cd $TMPDIR && python - <<'EOF' | grep -v "extraction took\|peak memory\|^\["
import nbformat
nb=nbformat.read('dev_out.ipynb',4)
print(['executed/paula-2026/reproduce_paula_2026.ipynb'])
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        print(f'----- cell {i+0} {c.metadata.get("tags","")}')
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text)
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
) | head -60
```

```
0
5d4
< 
63d61
< 
65a64
> 
176c175
< surrogate seed_s1000: max |r| reading a 0.796 (pairs > 0.2: 117), reading b 0.661 (pairs > 0.2: 212)
---
> surrogate seed_s1000: max |r| reading a 0.791 (pairs > 0.2: 115), reading b 0.662 (pairs > 0.2: 213)
178c177
< surrogate seed_s2000: max |r| reading a 0.798 (pairs > 0.2: 115), reading b 0.659 (pairs > 0.2: 213)
---
> surrogate seed_s2000: max |r| reading a 0.791 (pairs > 0.2: 115), reading b 0.662 (pairs > 0.2: 213)
180c179
< surrogate seed_s3000: max |r| reading a 0.800 (pairs > 0.2: 115), reading b 0.661 (pairs > 0.2: 209)
---
> surrogate seed_s3000: max |r| reading a 0.791 (pairs > 0.2: 115), reading b 0.662 (pairs > 0.2: 213)
182c181
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "extraction took" $TMPDIR/exec_out.txt; grep -n "^findings:" -A30 attempts/fouke-2025-01.yaml | head -40; ls schemas; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));o=s['properties']['outcomes']['items'];print(list(o['properties'].keys()));f=s['properties']['findings']['items'];print(json.dumps(f,indent=0)[:1500]);print(list(s['properties'].keys()))" 2>&1 | head -40
```

```
6:153 session files of 4293 assets; extraction took 36.0 min
244:findings:
245-- kind: data_missing
246-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
247-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
248-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
249-    notebooks only. Nine of the paper's main findings cannot be tested.
250-- kind: metadata_insufficient
251-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
252-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
253-    file of its stimulus software.
254-- kind: code_mismatch
255-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
256-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
257-    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
258-    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
259-    only if the fish turn with lateral motion.
260-- kind: metadata_error
261-  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
262-    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
[... 56 more lines not kept]
```

**Agent**

Outputs identical to the development run except the extra-seed surrogate lines (as expected). Writing the attempt record now (12:57).

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && cat > $TMPDIR/attempt.py <<'PYEOF'
import yaml
NB = "reproduce_paula_2026.ipynb"
UNIT = ("Unit selection assumed (author, step 1.6): all units of each session's units table. The paper states no "
        "unit filter, and neither reading of the claims file reproduces Table I (claim table1-sample); 'all' is "
        "adopted because it keeps exactly Table I's 26 subregions and its neurons per population are the closer "
        "of the two. The 'qc' reading is shown as a variant where it bears on the claim.")
SESS = ("All 153 ecephys sessions are used, against the paper's 102; the paper does not say how its sessions were "
        "chosen, and every session meets both session readings of the claims file.")
SURR = ("The surrogates are drawn once per active window under the seed of fig1c-cv-above-surrogate (and that seed "
        "plus 1000 to 4000, combined with the session and window indices), and the same surrogates serve the claims "
        "of Figs. 1c, 1d and 3c to 3f, so this claim does not have a generator of its own.")
def o(claim, outcome, notes, deviations=(), measured=None, assumed=True, **kw):
    d = {"claim": claim, "outcome": outcome, "notebook": NB, "output": f"claim:{claim}"}
    if measured is not None:
        d["measured"] = measured
    d["notes"] = notes
    d["deviations"] = list(deviations)
    if assumed:
        d["assumed"] = True
    d.update(kw)
    return d

outcomes = [
o("table1-sample", "not_reproduced",
  "Under every reading the counts are about 1.5 times the paper's. Units 'all' with either session reading give 153 "
  "sessions, populations VIS 888, TH 551, HP 586, MB 286, neurons 110 527, 39 370, 91 091 and 35 256, and windows "
  "18 155 natural images, 83 166 active, 18 488 blanks and 4622 spontaneous. Units 'qc' give 153 sessions, populations "
  "754, 240, 325, 158 and neurons 44 439, 11 443, 25 359, 8855; its MB population count and its four window counts "
  "fall within tolerance, the rest do not. The session readings do not differ, since all 153 sessions have kept "
  "populations and the 289-s spontaneous epoch. Per subregion, 'all' gives 1.5 to 3.0 times Table I's neurons and "
  "'qc' 0.23 to 0.88 times. The selection rule keeps exactly Table I's 26 subregions under 'all' (plus the labels "
  "Eth, HPF, LGv, MB, TH and ZI, not in Table I and not used), and drops NOT under 'qc'.",
  [SESS, "The selection rule is applied to Table I's 26 subregions; six other location labels that pass it are not used."],
  measured=[153, 888, 551, 586, 286, 110527, 39370, 91091, 35256, 18155, 83166, 18488, 4622], assumed=False),
o("fig1c-cv-region-medians", "not_reproduced",
  "Active-behavior medians (units 'all'). VIS 0.426 to 0.644, all inside the widened range and the extremes within "
  "tolerance. TH 0.306 (PIL) to 0.396 (LP), the low end above 0.27 +/- 0.027. HP 0.264 (CA1) to 0.564 (DG), DG "
  "highest as stated but above 0.49 +/- 0.049. MB 0.170 (APN) to 0.564 (NB), the high end above 0.45 +/- 0.045. "
  "IQRs inside their ranges in 16 of 26 subregions. Under 'qc' VIS, HP and MB match and TH misses at its high end "
  "(LP 0.414 against 0.407). By image set, the area medians differ (VIS 0.501 for G sessions, 0.579 for H).",
  [UNIT, SESS], measured=[0.426, 0.644, 0.306, 0.396, 0.264, 0.564, 0.170, 0.564]),
o("fig1c-cv-above-surrogate", "partially_reproduced",
  "Empirical median CV exceeds the surrogate median in all 26 subregions; Mann-Whitney p at most 1.5e-73 per "
  "subregion and 0 at printed precision per area. VIS surrogate medians 0.226 to 0.243, inside 0.189 to 0.264. "
  "Ratios VIS 1.83 to 2.85, TH 1.32 to 1.60, MB 1.35 to 1.83, all inside their widened ranges; HP 1.32 to 3.01, "
  "with DG (3.01) and POST (1.32) outside 1.35 to 2.42. Over the five seeds the ratios range 1.314 to 3.009, VIS "
  "surrogate medians 0.2252 to 0.2437, largest p 8.4e-73; the outcome is the same under all five. Under 'qc' the "
  "VIS surrogate medians are 0.276 to 0.301 and three VIS ratios fall below 1.8.",
  [UNIT, SESS, "The Mann-Whitney test is two-sided (claims file)."],
  measured=[1.83, 2.85, 0.226, 0.243, 1.32, 1.60, 1.32, 3.01, 1.35, 1.83], seed_sensitive=False),
o("fig1d-surrogate-abolishes-cv-correlations", "not_reproduced",
  "All 325 subregion pairs share at least one session (median 44). Empirical correlations of the 10-s CV series reach "
  "0.772 (reading a, concatenated) and 0.669 (reading b, mean over sessions). The surrogate correlations are not "
  "abolished: |r| above 0.2 in 115 pairs (a) and 213 pairs (b), largest 0.791 and 0.662; over the other four seeds the "
  "largest |r| is 0.796 to 0.800 (a) and 0.659 to 0.663 (b), with 115 to 117 and 209 to 213 pairs above 0.2. The "
  "per-window ISI shuffle keeps each 100-s window's spike counts, so surrogate CV follows the population rate, which "
  "co-varies across regions over the hour; a shuffle over the whole recording, which the paper may have used, is "
  "not tested here.",
  [UNIT, SESS, SURR, "The 0.2 bound is the claims file's, not the paper's."], seed_sensitive=False),
o("fig1e-positive-cv-modules", "partially_reproduced",
  "Top 10% (32 of 325 pairs). Reading a, r 0.459 to 0.772, 21 of 32 within one major area; the high end is outside "
  "0.67 +/- 0.067. Reading b, r 0.450 to 0.669, 26 of 32 within one area, mostly visual pairs, with POST-SUB, "
  "ProS-SUB and thalamic pairs; the low end is at the edge of 0.50 +/- 0.05 and fails the test. The module structure "
  "holds under both readings; the range fails at one end under each.",
  [UNIT, SESS], measured=[0.459, 0.772]),
o("fig1e-dg-ca3-anticorrelation-hubs", "partially_reproduced",
  "Most negative 10% (32 pairs). Reading b, CA3 is in 17 and DG in 14 of them, the two most frequent, as stated, but "
  "the most negative value is -0.178, outside -0.27 +/- 0.027 (recorded as measured). Reading a, NB leads (15), DG and "
  "SCig 5, CA3 4, and the most negative value is -0.496.",
  [UNIT, SESS], measured=[-0.178]),
o("fig1e-midbrain-weakest-cv-correlations", "partially_reproduced",
  "Mean |r| by area, reading b, MB 0.201, HP 0.235, TH 0.287, VIS 0.334, so the midbrain is lowest; only 2 of its 115 "
  "pairs lie in -0.044 to 0.033. Reading a, HP 0.179 is below MB 0.186, and 16 of 115 MB pairs are near zero. The "
  "ordering holds under one reading; the near-zero values do not hold under either.",
  [UNIT, SESS]),
o("fig2a-vis-cv-by-condition", "reproduced",
  "Readings a/a and b/a put all twelve medians within tolerance; VISp 0.644 active, 0.602 blanks, 0.316 spontaneous, "
  "0.418 images; VISl 0.607, 0.501, 0.317, 0.501; VISal 0.590, 0.499, 0.319, 0.502. With the spontaneous reading b, "
  "VISp spontaneous is 0.322, just above 0.319. The order active > images > spontaneous and blanks > spontaneous holds "
  "in the three areas under every reading. Under 'qc', 8 of 12 are within tolerance.",
  [UNIT, SESS, "Blank pieces are [stop, min(stop + 0.5 s, next onset)) of each shown flash (reading a) or of flashes followed by a shown flash (b); spontaneous windows are the first two 100-s windows of the 289-s gray screen (a) or two centred in it (b), as the claims file lists."],
  measured=[0.644, 0.602, 0.316, 0.418, 0.607, 0.501, 0.317, 0.501, 0.590, 0.499, 0.319, 0.502]),
o("fig2a-thalamus-cv-by-condition", "reproduced",
  "LP 0.396 active and 0.286 spontaneous, LGd 0.330 and 0.226, within tolerance under every reading. Active minus "
  "spontaneous is 0.110 (LP) and 0.104 (LGd), below VISp 0.327, VISl 0.290 and VISal 0.271.",
  [UNIT, SESS], measured=[0.396, 0.286, 0.330, 0.226]),
o("fig2a-hippocampus-cv-stable", "partially_reproduced",
  "Visually driven medians DG 0.555 to 0.576 and CA3 0.449 to 0.458; CA1 0.263 to 0.266; spontaneous DG 0.576 to "
  "0.580, CA3 0.471 to 0.475. CA3 and CA1 are within tolerance (CA3 spontaneous under the spontaneous reading b), DG "
  "is above it everywhere, and the spontaneous medians of DG and CA3 exceed their visually driven ones under every "
  "reading. Measured values are for reading a/a.",
  [UNIT, SESS], measured=[0.555, 0.576, 0.449, 0.458, 0.264, 0.576, 0.475]),
o("fig2a-midbrain-cv-invariant", "partially_reproduced",
  "APN 0.146 (spontaneous) to 0.172 (images), every condition within 0.16 +/- 0.016; the measured value is the one "
  "furthest from 0.16. MRN lowest 0.185 to 0.186 (spontaneous), within tolerance; highest 0.233 (images), above 0.21 "
  "+/- 0.021 under every reading.",
  [UNIT, SESS], measured=[0.146, 0.186, 0.233]),
o("fig2b-vis-summed-js-cv", "partially_reproduced",
  "32 combinations (4 condition readings, 50 or 100 bins, all-pair or adjacent sum, two forms of percentage). None "
  "meets the full rule. Four meet the partial rule (condition readings a/a and b/a, 50 bins, all-pair sum, both "
  "percentage forms): active against blanks 0.32% to 0.53%, the closest pair, and the other pairs 23.2% to 40.4%. "
  "With the first listed combination (a/a, 50 bins, all pairs, |A - B| / B) active against blanks is 0.32% and the four "
  "pairs against images or spontaneous 26.2% to 33.5% (the measured value is the lowest of them). Other combinations "
  "give active against blanks 3.75% to 9.53%, and active-spontaneous or blanks-spontaneous become the closest pair "
  "under 100 bins. Summed JS (a/a, 50 bins, all pairs) VIS images 1.36, active 2.04, blanks 2.05, spontaneous 1.62.",
  [UNIT, SESS, "JS divergences in bits from equal-width histograms over the pooled range of each pair (claims file)."],
  measured=[0.32, 26.2]),
o("fig2b-hp-mb-summed-js-cv", "not_reproduced",
  "Active against spontaneous is the largest hippocampal difference in every combination, as stated, but 41.2% to "
  "71.1% against 15% +/- 1.5%. The largest midbrain difference is 22.1% to 40.7%, against at most 7.7%, and the "
  "midbrain has the smallest difference in at most 4 of 6 pairs. Measured values for a/a, 50 bins, all pairs, |A - B| / B.",
  [UNIT, SESS], measured=[41.2, 22.2]),
o("fig2b-visually-driven-js-cv-low", "reproduced",
  "Under the second reading the criterion names (the legend's JS values), the fraction of VIS-VIS divergences at most "
  "0.22 is 1.0 (images), 0.73 (active) and 0.73 to 0.80 (blanks) under every condition and histogram reading, VIS-VIS "
  "values 0.007 to 0.381. Under the percentage reading no combination has two of three pairs at or below 4.4% "
  "(active-blanks 0.3% to 9.5%, pairs with images 16.3% to 40.4%). The text's percentage form conflicts with the "
  "~30% separation of fig2b-vis-summed-js-cv, as the claims file notes.",
  [UNIT, SESS]),
o("fig2b-dg-ca3-high-js-cv", "partially_reproduced",
  "Median divergence from the other 25 subregions, a/a with 50 bins (measured): DG spontaneous 0.763, CA3 spontaneous "
  "0.450, DG blanks 0.463, CA3 blanks 0.228. Over all readings DG spontaneous 0.744 to 0.805 is within 0.84 +/- 0.084, "
  "CA3 spontaneous 0.450 to 0.544 and the blank medians (DG 0.461 to 0.489, CA3 0.227 to 0.249) are not. Spontaneous "
  "activity gives the largest median for both under every reading. Against the other hippocampal subregions only, DG "
  "0.762 to 0.805 and CA3 0.555 to 0.638 in spontaneous activity, CA3 blanks 0.401 to 0.419.",
  [UNIT, SESS], measured=[0.763, 0.450, 0.463, 0.228]),
o("fig2b-legend-js-cv", "not_reproduced",
  "Reading a (a subregion's own CV distributions between conditions): 3 of 6 visual subregions exceed 0.44 for "
  "spontaneous against the visually driven mean (VISal, VISl, VISp), not more than half; 0 or 1 of 9 thalamic "
  "subregions exceed 0.33; DG and CA3 values 0.004 to 0.122, below 0.135; midbrain below 0.165 in 14 to 21 of 30. "
  "Reading b (row differences of the region-pair matrices): no visual or thalamic subregion passes; DG and CA3 0.024 "
  "to 0.393; midbrain 23 to 26 of 30 below 0.165.",
  [UNIT, SESS, "Reading b of the claims file ('comparing a region's row') is made operational as the mean absolute difference between a subregion's row in spontaneous activity and in a visually driven condition; the value for spontaneous against visually driven is the mean over the three visually driven conditions. Neither is fixed by the claims file or the paper."]),
o("fig3a-reference-systems", "partially_reproduced",
  "D = 6, tau = 1, 10^5 points. White noise H 0.999, C 0.001; logistic r = 4 H 0.629, C 0.484; tent mu = 1.9999 H "
  "0.630, C 0.485, both inside C 0.36 to 0.55 and H 0.45 to 0.88. Sine (1000 points per period) H 0.115, C 0.113, "
  "outside H at most 0.05 and C 0.09 to 0.11. Ikeda with u = 0.9 H 0.105 to 0.382 and C 0.105 to 0.357 for p 5 to 17, "
  "not near maximum complexity. Exponentially correlated walks with H in 0.27 to 0.66 (alpha 0.2 to 1.0, 4 of 8) have "
  "C 0.212 to 0.334 over all, partly below 0.27 (alpha 0.5 to 1.0). Fig. 3a's parameter values could not be read from "
  "the text.",
  ["Synthetic series only, from the definitions of Supplemental Material Sec. I; no recordings.",
   "Assumed (step 1.6): near 0 is read as within 0.05 and near 1 as at least 0.9 (10% of 0 gives no tolerance); the sine is sampled at 1000 points per period, the paper giving no sampling; the chaotic maps are judged at their fully chaotic parameters (r = 4, mu = 1.9999, the tent map at mu = 2 collapsing to 0 in floating point, p = 6); the 1/f^k noise is spectral synthesis with random phases."]),
o("fig3b-complexity-levels-by-region", "reproduced",
  "Reading a (36 active windows): mean C over windows VIS 0.161, HP 0.163, TH 0.109, MB 0.101, each within tolerance; "
  "the order MB < TH < VIS and HP holds at all 36 indices; largest standard error 0.0027. Reading b (natural images, 8 "
  "indices): VIS 0.208 and HP 0.108, the order at 0 of 8. Under 'qc' (reading a) VIS 0.156, HP 0.154, TH 0.109, MB "
  "0.095, order at 36 of 36. Reading a is the one the claims file points to (point counts summing to the active count).",
  [UNIT, SESS], measured=[0.161, 0.163, 0.109, 0.101]),
o("fig3c-vis-ch-plane", "partially_reproduced",
  "31 956 active VIS windows (paper 21 084). 2.5th to 97.5th percentiles, H 0.856 to 0.965 (inside 0.72 to 1.10), C "
  "0.089 to 0.285 (low end just below 0.090). Empirical median C 0.152 against surrogate 0.0955, Mann-Whitney p 0 at "
  "printed precision under all five seeds; surrogate median 0.0954 to 0.0955 over the seeds, inside 0.09 to 0.22. The "
  "0th to 100th span misses on H (0.462 to 0.973). Natural-image windows span C 0.093 to 0.377.",
  [UNIT, SESS, SURR], seed_sensitive=False),
o("fig3d-th-ch-plane", "reproduced",
  "19 832 TH windows (paper 11 265). H 0.928 to 0.969, C 0.080 to 0.171 (2.5th to 97.5th), inside the widened ranges; "
  "C span 0.091 against VIS 0.196; Mann-Whitney p 0 at printed precision, five seeds; surrogate median C 0.096. Under "
  "the 0th to 100th span, C reaches 0.344, outside.",
  [UNIT, SESS, SURR, "Spans are the 2.5th to 97.5th percentiles (claims file, a standard reading), the 0th to 100th shown."], seed_sensitive=False),
o("fig3e-hp-ch-plane", "reproduced",
  "21 087 HP windows (paper 13 059). H 0.857 to 0.966, C 0.086 to 0.298, inside the widened ranges; C span 0.212, the "
  "widest (VIS 0.196, TH 0.091, MB 0.081); Mann-Whitney p 0 at printed precision, five seeds. The 0th to 100th span "
  "misses (H from 0.124, C to 0.441).",
  [UNIT, SESS, SURR, "Spans are the 2.5th to 97.5th percentiles (claims file)."], seed_sensitive=False),
o("fig3f-mb-ch-plane", "reproduced",
  "10 291 MB windows (paper 6296). H 0.935 to 0.970, C 0.076 to 0.157, inside the widened ranges; C span 0.081, the "
  "narrowest; Mann-Whitney p 2.3e-194, at most 7.3e-192 over the five seeds; empirical median C 0.0948 against "
  "surrogate 0.0892. Under the 0th to 100th span H starts at 0.795 and the C span is not the narrowest.",
  [UNIT, SESS, SURR, "Spans are the 2.5th to 97.5th percentiles (claims file)."], seed_sensitive=False),
o("fig3-complexity-range-fractions", "not_reproduced",
  "Active windows, 0 of 8 within tolerance; VIS [0.3, 0.4] 1.60% and [0, 0.1) 10.07%, TH [0.2, 0.3) 0.46% and [0, 0.1) "
  "42.72%, HP 2.27% and 13.18%, MB [0.1, 0.2) 37.30% and [0, 0.1) 62.03%. Natural-image windows, 1 of 8 (MB [0, 0.1) "
  "57.80%). Under 'qc', 0 of 8.",
  [UNIT, SESS], measured=[1.60, 10.07, 0.46, 42.72, 2.27, 13.18, 37.30, 62.03]),
o("fig4a-vis-complexity-by-condition", "partially_reproduced",
  "Medians, reading a/a: natural images 0.160 to 0.265, spontaneous 0.094 to 0.097, active and blanks 0.101 to 0.190, "
  "all inside the widened ranges under every reading. The order fails in VISp (images 0.178 below active 0.190, equal "
  "to blanks 0.178); the other five areas hold it. 35 of 36 pairwise Mann-Whitney tests give p < 0.001 (uncorrected "
  "and Bonferroni); VISp images against blanks gives p = 0.46 to 0.53. The legend's ranges for VISl, VISal and VISp "
  "are met. IQRs in visually driven states 0.025 to 0.119, against the legend's 0.08 to 0.12.",
  [UNIT, SESS], measured=[0.160, 0.265, 0.094, 0.101, 0.190]),
o("fig4b-thalamus-lgd-lp-modulated", "reproduced",
  "LGd and LP: Kruskal-Wallis p 4.2e-67 to 7.1e-69 and 3.4e-63 to 1.6e-65; each visually driven condition against "
  "spontaneous p at most 1.4e-21 and 3.6e-17. Visually driven medians 0.113 to 0.152 against spontaneous 0.093 to "
  "0.100, matching the legend's values (LP 0.12 to 0.14 against 0.11, LGd 0.12 to 0.15 against 0.10) and not the "
  "text's (LGd active 0.121 below 0.126). Effect as the largest visually driven median minus spontaneous, LGd 0.057 to "
  "0.059 and LP 0.043 to 0.044, below every visual area (0.065 to 0.170); as the mean of the three minus spontaneous, "
  "LGd 0.034 to 0.036 is above VISrl 0.029 to 0.030 and the rule fails. The statement's 'only LGd and LP' holds under "
  "the pairwise test; under Kruskal-Wallis MGd, SGN, MGm and MGv also reach p < 0.001.",
  [UNIT, SESS, "Assumed (step 1.6): the effect compared with visual cortex is the largest visually driven median minus the spontaneous median, matching how the paper states the effect (the top of the visually driven range against spontaneous); the mean-based form gives the opposite outcome and is shown."],
  measured=[0.113, 0.152, 0.093, 0.100]),
o("fig4b-other-thalamus-not-modulated", "reproduced",
  "Medians of the seven nuclei 0.093 to 0.108, inside 0.09 to 0.143; largest condition difference per nucleus 0.002 "
  "to 0.006. Pairwise test (each visually driven condition against spontaneous, two-sided Mann-Whitney): no nucleus "
  "reaches p < 0.001 under any condition reading (smallest of the largest p values 0.004, SGN). Kruskal-Wallis: MGd, "
  "SGN, MGm and MGv give p < 0.001 (2.9e-07 to 4.4e-04), which would make the claim not reproduced.",
  [UNIT, SESS, "Assumed (step 1.6): the paper's unnamed test of modulation is the pairwise Mann-Whitney test, the only test the paper names, used for its other pairwise condition comparisons (Results III.D, paragraph 2). The two readings give opposite outcomes; both are shown."],
  measured=[0.093, 0.108]),
o("fig4c-dg-ca3-complexity", "reproduced",
  "Legend reading with the spontaneous reading b (a/b and b/b): DG images 0.115, CA3 0.108, CA1 0.096 match the "
  "legend's 0.12, 0.11 and 0.10; in the other conditions DG 0.178 to 0.257, CA3 0.137 to 0.196, CA1 0.120 to 0.163, "
  "inside the legend's widened ranges; POST, ProS and SUB 0.097 to 0.136, inside 0.09 to 0.143; DG and CA3 peak in "
  "spontaneous activity. With the spontaneous reading a, CA3 spontaneous (0.198) lies just above the widened bound and "
  "the reading fails. The text's reading fails as CA1 (0.096) and SUB (0.097) are below 0.099 in natural images; DG and "
  "CA3 match the text's ranges in 3 of 4 conditions. Measured values are the legend reading, natural images apart.",
  [UNIT, SESS], measured=[0.178, 0.257, 0.137, 0.196, 0.096, 0.163]),
o("fig4d-midbrain-complexity-invariant", "reproduced",
  "Legend values: NB 0.107 to 0.110, MRN 0.096 to 0.100, SCig 0.097 to 0.102, APN 0.086 to 0.090, each inside its "
  "widened range; NOT 0.099 to 0.173 across conditions, the largest range (0.072 to 0.073 against at most 0.004). Text "
  "values fail on APN (0.086 to 0.090, below 0.09). NOT's highest visually driven median is 0.173 (images) and its "
  "spontaneous one 0.099 to 0.101.",
  [UNIT, SESS], measured=[0.086, 0.110, 0.173, 0.099]),
o("fig4e-js-complexity-natural-images", "partially_reproduced",
  "Natural images: VIS-VIS pairs below 0.22, 0.73 to 0.87 of them; VIS-TH above 0.36, 0.74 (median 0.463 to 0.471); "
  "VIS-MB above 0.36, 0.63 to 0.67 (median 0.414 to 0.434). Pairs of DG or CA3 with other subregions in 0.27 to 0.55, "
  "0.20 (median 0.161 to 0.176). The visual part holds; the DG and CA3 part does not.",
  [UNIT, SESS]),
o("fig4fg-js-complexity-active-blanks", "not_reproduced",
  "Pairs of a visual and a subcortical subregion above 0.36, 0.38 in active behavior (median 0.255 to 0.259) and 0.29 "
  "to 0.31 in blanks (median 0.192 to 0.211); HP-HP pairs in active behavior within 0.18 to 0.44, 0.27 to 0.33.",
  [UNIT, SESS]),
o("fig4h-js-complexity-spontaneous-converges", "not_reproduced",
  "Mean of all pairs, spontaneous 0.264 to 0.332 against images 0.289 to 0.310, active 0.249 to 0.255, blanks 0.218 to "
  "0.243, so not lowest. Mean VIS-to-other divergence is lowest in spontaneous activity (0.208 to 0.262 against 0.267 to "
  "0.511), but 0.27 to 0.35 of those pairs lie in 0.18 to 0.44. MB-MB pairs below 0.22 in 0.2 to 0.5 of them in "
  "spontaneous activity.",
  [UNIT, SESS]),
o("supp-robustness-parameters", "partially_reproduced",
  "The pattern holds for 4 of 5 combinations (20 ms with D 5 tau 1 and D 6 tau 1; 50 ms with D 4 tau 2 and D 5 tau 3). "
  "With 20 ms, D 3, tau 4, natural images exceed spontaneous in 2 of 6 visual areas and the visual difference is "
  "-0.0002. Window counts are those of the 50 ms analysis (images 18 155, active 83 166, blanks 18 488, spontaneous "
  "4622) against the supplement's 20 ms counts 11 321, 51 452, 11 265 and 2856.",
  [UNIT, SESS, "The visually driven minus spontaneous difference of an area is the median C over its visually driven windows minus that over its spontaneous windows; the claims file does not fix the form."]),
o("fig5-vis-complexity-cv-coupling", "partially_reproduced",
  "C rises with CV in the three visually driven conditions (Spearman 0.622, 0.830, 0.819; monotonic under bins of 0.1 "
  "with at least 10 windows). Spans, bins of 0.1 without minimum (measured): images CV 0.20 to 1.30 and C 0.116 to 0.318; "
  "active CV to 4.60, C to 0.349; blanks CV to 2.10, C to 0.399; spontaneous maximum 0.349. With at least 10 windows per "
  "bin, spontaneous maximum 0.180 to 0.182 and images CV to 1.05 to 1.10. No reading matches all spans or the "
  "spontaneous bound 0.165.",
  [UNIT, SESS], measured=[0.318, 4.60, 0.349, 2.10, 0.399, 0.349]),
o("fig5-th-weaker-coupling", "partially_reproduced",
  "Least-squares slopes of C on CV, TH 0.111, 0.095 and 0.084 (images, active, blanks) against VIS 0.350, 0.216 and "
  "0.234, positive and shallower as stated. The TH spans exceed CV 0.18 to 0.88 and C 0.09 to 0.22 under every reading "
  "(for example CV 0.10 to 1.40 and C to 0.296 in active behavior with at least 10 windows per bin).",
  [UNIT, SESS]),
o("fig5-hp-spontaneous-elevated", "not_reproduced",
  "HP spontaneous bin means at CV 0.4 to 0.7 reach 0.238 to 0.244, within 0.25 +/- 0.025, but the HP maxima of the "
  "visually driven conditions are higher in active behavior (0.324 to 0.410) and are not within 0.19 +/- 0.019 "
  "(images 0.191 to 0.246, blanks 0.170 to 0.353).",
  [UNIT, SESS], measured=[0.238, 0.389]),
o("fig5-mb-flat", "partially_reproduced",
  "The MB slope is the smallest in absolute value of the four areas in all four conditions (0.072, 0.066, 0.062, "
  "0.042). Its bin means stay inside 0.09 to 0.143 only in spontaneous activity (0.092 to 0.125); in images (allowed to "
  "0.165), active behavior and blanks they reach 0.082 to 0.085 at the low end and up to 0.132 to 0.346 at the high end.",
  [UNIT, SESS]),
o("supp-fig6-mean-correlation", "not_reproduced",
  "VIS medians of the mean pairwise correlation, active and blanks 0.014 to 0.052 (50 ms) and 0.007 to 0.029 (20 ms), "
  "below 0.072; images and spontaneous 0.009 to 0.037 (50 ms) and 0.005 to 0.022 (20 ms), 2 and 6 of 12 below 0.011. "
  "Midbrain medians vary across conditions by 0.001 to 0.011 except NOT (0.024 to 0.025 at 50 ms, 0.013 at 20 ms). The "
  "order active above images and spontaneous is present (VISp 0.052 active, 0.032 images, 0.017 spontaneous at 50 ms).",
  [UNIT, SESS, "Units without spikes in a window are left out (claims file). Correlations are computed for visual cortex and midbrain populations only."],
  measured=[0.014, 0.052, 0.037]),
o("complexity-separates-images-from-spontaneous", "reproduced",
  "JS reading: in all six visual subregions the natural-image against spontaneous divergence is larger for C (0.443 to "
  "0.849, a/a, 50 bins) than for CV (0.198 to 0.544) and mean correlation (0.142 to 0.434), under every condition and "
  "histogram reading. IQR reading: 1 or 2 of 6, since the CV and correlation IQRs of the two conditions often do not "
  "overlap either. The CV medians do differ between the two conditions (VISp 0.418 against 0.316).",
  [UNIT, SESS]),
]

findings = [
 {"kind": "selection_undocumented", "about": "paper", "statement":
  "The paper analyses 102 sessions and 1437 populations without saying how the sessions were chosen. The dandiset "
  "holds 153 ecephys sessions of 81 mice, every one with populations that pass the paper's rule (at least 30 units, "
  "subregion in at least eight sessions) and with the gray-screen epoch, so the paper's selection cannot be rebuilt; "
  "population and window counts here are about 1.5 times the paper's. Which 102 sessions were used?"},
 {"kind": "methods_unavailable", "statement":
  "No unit selection is stated. With all units, Table I's neuron counts are 1.5 to 3.0 times smaller than here per "
  "subregion; with the Allen quality filters (ISI violations < 0.5, amplitude cutoff < 0.1, presence ratio > 0.9) they "
  "are 1.1 to 4.4 times larger, and NOT drops out. Which units form a population? Almost every outcome here rests on "
  "the choice of all units."},
 {"kind": "methods_unavailable", "statement":
  "The ISI-shuffled surrogate is defined per analyzed window (Methods II.E). Shuffled within each 100-s window, "
  "surrogate CV series stay correlated across regions (up to |r| 0.80, 115 to 213 of 325 pairs above 0.2), because each "
  "window keeps its spike count; the paper says shuffling abolishes these correlations. Were the 10-s CV series of Fig. "
  "1d computed from surrogates shuffled over a longer span, and where does the shuffled train start?"},
 {"kind": "methods_unavailable", "statement":
  "The JS divergences of Figs. 2b and 4e to 4h do not give their histogram bins or log base, the 'main diagonal of each "
  "submatrix' that is summed is zero for a region-pair matrix, and the percentage difference is not defined. The "
  "results here depend on these choices (for example active against blanks 0.3% to 9.5% in visual cortex). What were "
  "they?"},
 {"kind": "methods_unavailable", "statement":
  "The test of 'significant modulation across conditions' (Results III.D, paragraph 3) and of 'all pairwise "
  "comparisons' (paragraph 2) is not named. For four of the seven 'unmodulated' thalamic nuclei a Kruskal-Wallis test "
  "gives p < 0.001 and pairwise Mann-Whitney tests do not, so the outcome of the claim depends on the test. Which test "
  "was used?"},
 {"kind": "methods_unavailable", "statement":
  "The Fig. 5 trajectories give no CV bin width or minimum count per bin, and the Fig. 3a reference systems give no "
  "series length, sampling or parameter values in the text (the sine's position depends on its sampling; the Ikeda map "
  "with u = 0.9 and p in [5, 17] gives H 0.11 to 0.38 here, not near maximum complexity). What were they?"},
 {"kind": "methods_unavailable", "statement":
  "Methods II.A gives the blank series as about 240 s per image; the flash tables give about 287 s (median; 273 s when "
  "only gray screens followed by another flash are kept), from about 4600 shown flashes per session. How were the "
  "blank intervals chosen (change flashes, omitted flashes, licks)?"},
 {"kind": "other", "about": "data", "severity": "none", "notebook": NB, "output": "sanity", "statement":
  "Checks that passed. The 153 sessions each have an active block of 3599 to 3611 s, a 289-s gray screen after it, "
  "eight images and 1103 to 3388 units; no two sessions share a spike-time fingerprint, total spike count, or subject "
  "and start time. Visual cortex spikes rise after flash onsets in all 153 sessions (30 to 130 ms window minus the "
  "100 ms before, 69 to 434 spikes per flash) and not after onsets shifted by 375 ms (-371 to 1.6) or after omitted "
  "flashes, so the spike times share the stimulus table's clock."},
 {"kind": "other", "about": "data", "severity": "none", "statement":
  "Some units carry generic location labels (TH, MB, HPF) or labels outside the paper's list (Eth, LGv, ZI); the "
  "paper's 26 subregions are all present as labels, and the generic labels are left out here as in Table I."},
]

rec = {
 "schema_version": 3, "id": "paula-2026-01",
 "datasets": [{"archive": "dandi", "id": "000713", "version": "0.240702.1725",
               "doi": "10.48324/dandi.000713/0.240702.1725", "relation": "reuses"}],
 "paper": "doi:10.1103/wndc-k654", "date": "2026-11-27", "entry": "paula-2026",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-18"},
                "runner": {"platform": "GitHub Actions",
                           "url": "https://github.com/encorescience/encore-registry/actions/runs/45978330957"}},
 "inputs": [{"what": "Definitions of the reference systems of Fig. 3a (correlated Gaussian noise, logistic, Ikeda and tent maps, 1/f^k noise), used to generate synthetic series for fig3a-reference-systems; no data.",
             "source": "doi:10.1103/wndc-k654, Supplemental Material Sec. I"}],
 "outcomes": outcomes, "findings": findings,
}
yaml.safe_dump(rec, open("attempts/paula-2026-01.yaml", "w"), sort_keys=False, width=110, allow_unicode=True)
print(len(outcomes))
PYEOF
. $TMPDIR/venv/bin/activate && uv pip install -q pyyaml 2>/dev/null; python $TMPDIR/attempt.py && python tools/entry.py check entries/paula-2026 2>&1 | tail -15; date -u
```

```
38
error: attempts/paula-2026-01.yaml: findings/7: Additional properties are not allowed ('notebook', 'output' were unexpected)
1 error(s)
Fri Nov 27 12:57:00 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "Kruskal-Wallis p < 0.001 in\|CA3 blanks\|other hippocampal subregions, b" $TMPDIR/exec_out.txt | head; grep -n "hippocampal subregions" $TMPDIR/exec_out.txt | cut -c1-400 | tail -4
```

```
405:all other subregions, a/a, 50 bins: DG images 0.436, DG active 0.331, DG blanks 0.463, DG spont 0.763, CA3 images 0.198, CA3 active 0.163, CA3 blanks 0.228, CA3 spont 0.450; passes False
406:all other subregions, a/a, 100 bins: DG images 0.467, DG active 0.344, DG blanks 0.489, DG spont 0.805, CA3 images 0.224, CA3 active 0.170, CA3 blanks 0.248, CA3 spont 0.512; passes False
407:all other subregions, a/b, 50 bins: DG images 0.436, DG active 0.331, DG blanks 0.463, DG spont 0.744, CA3 images 0.198, CA3 active 0.163, CA3 blanks 0.228, CA3 spont 0.473; passes False
408:all other subregions, a/b, 100 bins: DG images 0.467, DG active 0.344, DG blanks 0.489, DG spont 0.792, CA3 images 0.224, CA3 active 0.170, CA3 blanks 0.248, CA3 spont 0.544; passes False
409:all other subregions, b/a, 50 bins: DG images 0.436, DG active 0.331, DG blanks 0.461, DG spont 0.763, CA3 images 0.198, CA3 active 0.163, CA3 blanks 0.227, CA3 spont 0.450; passes False
410:all other subregions, b/a, 100 bins: DG images 0.467, DG active 0.344, DG blanks 0.482, DG spont 0.805, CA3 images 0.224, CA3 active 0.170, CA3 blanks 0.249, CA3 spont 0.512; passes False
412:all other subregions, b/b, 50 bins: DG images 0.436, DG active 0.331, DG blanks 0.461, DG spont 0.744, CA3 images 0.198, CA3 active 0.163, CA3 blanks 0.227, CA3 spont 0.473; passes False
413:all other subregions, b/b, 100 bins: DG images 0.467, DG active 0.344, DG blanks 0.482, DG spont 0.792, CA3 images 0.224, CA3 active 0.170, CA3 blanks 0.249, CA3 spont 0.544; passes False
414:other hippocampal subregions, a/a, 50 bins: DG images 0.619, DG active 0.529, DG blanks 0.619, DG spont 0.763, CA3 images 0.386, CA3 active 0.299, CA3 blanks 0.401, CA3 spont 0.555; passes False
415:other hippocampal subregions, a/a, 100 bins: DG images 0.641, DG active 0.547, DG blanks 0.640, DG spont 0.805, CA3 images 0.417, CA3 active 0.312, CA3 blanks 0.419, CA3 spont 0.605; passes False
418:other hippocampal subregions, b/a, 50 bins: DG images 0.619, DG a
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Kruskal" $TMPDIR/exec_out.txt | cut -c1-200 | head -8; python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/attempt.py'; s=open(p).read()
rep=[('{"kind": "other", "about": "data", "severity": "none", "notebook": NB, "output": "sanity", "statement":','{"kind": "other", "about": "data", "severity": "none", "statement":'),
("each visually driven condition against \"\n  \"spontaneous p at most 1.4e-21 and 3.6e-17.","each visually driven condition against \"\n  \"spontaneous p at most 1.4e-21 and 3.0e-17."),
("give p < 0.001 (2.9e-07 to 4.4e-04)","give p < 0.001 (2.3e-07 to 4.4e-04)"),
("they reach 0.082 to 0.085 at the low end and up to 0.132 to 0.346 at the high end.","their low ends are 0.082 to 0.089 and their high ends 0.130 to 0.346."),
("Exponentially correlated walks with H in 0.27 to 0.66 (alpha 0.2 to 1.0, 4 of 8) have \"\n  \"C 0.212 to 0.334 over all, partly below 0.27 (alpha 0.5 to 1.0).","Exponentially correlated walks with H in 0.27 to 0.66 (alpha 0.2 to 0.7, 4 of 8) have \"\n  \"C 0.233 to 0.334, below 0.27 for alpha 0.5 and 0.7."),
("and not after onsets shifted by 375 ms (-371 to 1.6) or after omitted \"\n  \"flashes, so","and not after onsets shifted by 375 ms (-371 to 1.6); the true-onset response also exceeds the one after omitted \"\n  \"flashes in all 153, so"),
("CA3 0.555 to 0.638 in spontaneous activity, CA3 blanks 0.401 to 0.419.","CA3 0.555 to 0.638 in spontaneous activity; DG blanks 0.619 to 0.642, within tolerance, CA3 blanks 0.395 to 0.419, not."),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python $TMPDIR/attempt.py && python tools/entry.py check entries/paula-2026 2>&1 | tail -5
```

```
712:reading a/a: medians 0.093-0.108 inside 0.09 to 0.143 True; Kruskal-Wallis p < 0.001 in ['MGd', 'SGN', 'MGm', 'MGv']; pairwise (all VD vs spont) p < 0.001 in []
724:reading a/b: medians 0.093-0.108 inside 0.09 to 0.143 True; Kruskal-Wallis p < 0.001 in ['MGd', 'SGN', 'MGm', 'MGv']; pairwise (all VD vs spont) p < 0.001 in []
736:reading b/a: medians 0.093-0.108 inside 0.09 to 0.143 True; Kruskal-Wallis p < 0.001 in ['MGd', 'SGN', 'MGm', 'MGv']; pairwise (all VD vs spont) p < 0.001 in []
748:reading b/b: medians 0.093-0.108 inside 0.09 to 0.143 True; Kruskal-Wallis p < 0.001 in ['MGd', 'SGN', 'MGm', 'MGv']; pairwise (all VD vs spont) p < 0.001 in []
38
0 error(s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os, re, yaml
t=os.environ['TMPDIR']+'/nb.py'; s=open(t).read()
for lab in ["Paper.", "Dataset.", "Text.", "Claims.", "Method.", "How the analysis differs from the paper's.", "What was found about the dataset."]:
    s=s.replace(f"**{lab}**", lab)
ids=[c['id'] for c in yaml.safe_load(open('claims/paula-2026.yaml'))['claims']]
table="# | Claim | Tested here |\n# |---|---|\n"+"".join(f"# | {i} | {'tested (synthetic series)' if i=='fig3a-reference-systems' else 'tested'} |\n" for i in ids)
s=s.replace("# Claims. All 38 claims", "# Claims. All 38 claims") 
s=s.replace("none is blocked. Claim `fig3a-reference-systems` uses synthetic series only (`data: elsewhere`, no recordings). The outcomes are in the attempt record and the summary at the end.\n",
            "none is blocked. Claim `fig3a-reference-systems` uses synthetic series only (`data: elsewhere`, no recordings). The outcomes are in the attempt record and the summary at the end.\n#\n"+table)
assert "Tested here" in s
s=s.replace("All 35 claims","All 38 claims")
open(t,'w').write(s)
print(s.count("**"))
EOF
grep -n "All 3. claims" $TMPDIR/nb.py; . $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/nb.py entries/paula-2026/reproduce_paula_2026.ipynb && grep -c '\*\*' entries/paula-2026/reproduce_paula_2026.ipynb
```

```
78
11:# Claims. All 38 claims of the claims file are tested here; none is blocked. Claim `fig3a-reference-systems` uses synthetic series only (`data: elsewhere`, no recordings). The outcomes are in the attempt record and the summary at the end.
136 cells
40
```

**Agent calls Bash**

```bash
grep -n '\*\*' $TMPDIR/nb.py | grep -v "Result: " | cut -c1-150; grep -n "—" $TMPDIR/nb.py entries/paula-2026/README.md entries/paula-2026/paula.py attempts/paula-2026-01.yaml | head; grep -n -i "rather" $TMPDIR/nb.py entries/paula-2026/README.md entries/paula-2026/paula.py attempts/paula-2026-01.yaml | head
```

```
597:                  **{p: round(four[p], 1) for p in FOUR}, "closest pair": d.idxmin(), "reproduced": full, "partial": part})
745:    f = np.fft.rfftfreq(n); amp = np.zeros_like(f); amp[1:] = f[1:] ** (-k / 2)
```

**Agent**

Clean. Re-running the entry.

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/paula-2026 2>&1 | tail -4; date -u
```

```
Fri Nov 27 12:58:10 UTC 2026
Installed kernelspec registry-paula-2026 in executed/paula-2026/.venv/share/jupyter/kernels/registry-paula-2026
0 error(s)
pass  reproduce_paula_2026.ipynb  (2190 s)
Fri Nov 27 13:34:51 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' > $TMPDIR/exec_out2.txt
import nbformat, glob
nb=nbformat.read('executed/paula-2026/reproduce_paula_2026.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        print(f'----- cell {c.metadata.get("tags","")}')
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text)
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
grep -c ERROR $TMPDIR/exec_out2.txt; diff <(grep -v "^-----\|extraction took\|peak memory" $TMPDIR/exec_out.txt) <(grep -v "^-----\|extraction took\|peak memory" $TMPDIR/exec_out2.txt) | head; grep "extraction took" $TMPDIR/exec_out2.txt; python tools/entry.py handover entries/paula-2026 2>&1 | tail -3; ls executed/paula-2026/handover/; git status --short | head -20
```

```
0
1d0
< ['executed/paula-2026/reproduce_paula_2026.ipynb']
387d385
< 
802a801
> 
806a806
> 
807a808
> 
153 session files of 4293 assets; extraction took 35.7 min
wrote executed/paula-2026/handover
paula-2026.yaml
paula.py
reproduce_paula_2026.ipynb
 M tools/agent_run.py
 M tools/author_notes.py
 M tools/blind.sh
 M tools/build_site.py
[... 16 more lines not kept]
```

**Agent**

I've finished steps 1 to 5 for paula-2026 and built the handover with `tools/entry.py handover`; I did not verify the work myself. `tools/entry.py all` passes: 0 errors, and a clean-environment run takes 36.5 minutes, of which 35.7 are spent streaming the 153 sessions. Nothing is committed.

The main caveat: neither of the claims file's unit-selection readings reproduces the paper's counts. I used all 153 sessions and all units, so almost every outcome rests on that assumption.

## 1. Outcomes (38 claims, none blocked)

| Outcome | Claims |
|---|---|
| Reproduced (12) | fig2a-vis-cv-by-condition, fig2a-thalamus-cv-by-condition, fig2b-visually-driven-js-cv-low, fig3b-complexity-levels-by-region, fig3d-th-ch-plane, fig3e-hp-ch-plane, fig3f-mb-ch-plane, fig4b-thalamus-lgd-lp-modulated, fig4b-other-thalamus-not-modulated, fig4c-dg-ca3-complexity, fig4d-midbrain-complexity-invariant, complexity-separates-images-from-spontaneous |
| Partially reproduced (16) | fig1c-cv-above-surrogate, fig1e-positive-cv-modules, fig1e-dg-ca3-anticorrelation-hubs, fig1e-midbrain-weakest-cv-correlations, fig2a-hippocampus-cv-stable, fig2a-midbrain-cv-invariant, fig2b-vis-summed-js-cv, fig2b-dg-ca3-high-js-cv, fig3a-reference-systems, fig3c-vis-ch-plane, fig4a-vis-complexity-by-condition, fig4e-js-complexity-natural-images, supp-robustness-parameters, fig5-vis-complexity-cv-coupling, fig5-th-weaker-coupling, fig5-mb-flat |
| Not reproduced (10) | table1-sample, fig1c-cv-region-medians, fig1d-surrogate-abolishes-cv-correlations, fig2b-hp-mb-summed-js-cv, fig2b-legend-js-cv, fig3-complexity-range-fractions, fig4fg-js-complexity-active-blanks, fig4h-js-complexity-spontaneous-converges, fig5-hp-spontaneous-elevated, supp-fig6-mean-correlation |

Every outcome except table1-sample is marked `assumed: true`. No outcome changes across the five seeds.

## 2. Dataset, assumptions, questions

**Dataset.** Pinned version 0.240702.1725, the one the paper cites and the only published one.
- 153 ecephys sessions from 81 mice. Each has an active block of 3599 to 3611 s, a 289-s gray screen after it, and eight images.
- No recording appears twice.
- Spike times share the stimulus table's clock in all 153 sessions: there is a visual response to flash onsets, and none to onsets shifted into the gray screen.
- The paper's 102 sessions cannot be identified: all 153 pass both session readings in the claims file.
- Some units carry generic location labels (TH, MB, HPF).
- No data findings above severity "none".

**Assumptions.**
- **Unit selection: all units.** Table I is not matched under either reading. "All units" gives about 1.5 to 3 times Table I's neurons per subregion; the Allen quality filters give 0.23 to 0.88 times. I adopted "all units" because it keeps exactly Table I's 26 subregions; the filtered reading is shown as a variant.
- **fig4b test.** For the unnamed "modulation" test I used pairwise Mann-Whitney. Under Kruskal-Wallis instead, MGd, SGN, MGm and MGv also reach p < 0.001, and fig4b-other-thalamus-not-modulated would become not reproduced.
- **fig4b effect size.** I measured the thalamic effect as the largest visually driven median minus the spontaneous one. Using the mean of the three conditions instead reverses the LGd-versus-VISrl comparison.
- **fig3a.** I chose how to sample the sine and what counts as "near 0".

**Questions for the paper's authors.** These are recorded as `methods_unavailable` or `selection_undocumented` findings:
- Which 102 sessions were used?
- Which units form a population?
- How long a span was shuffled for the surrogates? Shuffling within each 100-s window leaves the surrogate CV series correlated across regions (|r| up to 0.80).
- What histogram bins and summation were used for the JS divergences?
- Which test was used for "modulation" and for "all pairwise comparisons"?
- What were the Fig. 5 CV bins and the Fig. 3a parameters?
- How were the blank intervals defined? The files give about 287 s of blank per image, not the stated ~240 s.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. Surrogates are shared by several claims, but seeds are per claim. I drew them once under fig1c-cv-above-surrogate's seed, combined with the session and window indices, and recorded this as a deviation on each claim that uses them.
2. Several criteria have no partial rule. I used `partially_reproduced` when the qualitative part held and some values missed, following the protocol's general definition.
3. The checker requires `inputs` on a tested `data: elsewhere` claim, even when the data are synthetic. I listed the supplement's definitions (Sec. I) as the input.
4. The protocol does not say that thread-count settings must come before numpy is first imported in a notebook. My first clean run hit the 60-minute cell timeout because each of the four worker processes ran several BLAS threads at once (load average about 13 on 4 CPUs). Setting the variables in the first cell fixed it.
5. The pilot-19 code in `entry.py` reads `notebook` and `output` on findings, but the attempt schema rejects them. I left them off.

## 4. Runtime and failures

The run took about 3 h 36 min, from 10:00 to about 13:36 UTC.
- My one development pass over all sessions took 35 min.
- The first `entry.py all` failed on the 60-minute cell timeout (point 3.4).
- The second and third runs passed in about 37 min each. The third was only to remove bold labels and add the header's claims table.

Nothing else failed, and no session failed to load.

## End of run

74 turns, 212 minutes, $10.67 at API prices, result: success.
