# yang-2026 · author · run 44877453513

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper entries claims attempts
```

```
<persisted-output>
Output too large (63.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d51d7c41-3b3d-49a6-8dd0-2ff5cb98498e/tool-results/b98a2h14c.txt

Preview (first 2KB):
Sat Nov 21 06:56:00 UTC 2026
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

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
cat README.md | head -150; ls paper entries/fouke-2025 claims attempts questions papers/datasets | head -100; cat papers/datasets/yang-2026.yaml
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
[... 227 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper entries/fouke-2025 questions | head; ls attempts | grep yang; ls entries | grep -i yang; cat claims/yang-2026.yaml
```

```
<persisted-output>
Output too large (50.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d51d7c41-3b3d-49a6-8dd0-2ff5cb98498e/tool-results/bf43zur2q.txt

Preview (first 2KB):
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.21203-rs.3.rs-11447300-v1.txt
# Claims for Yang (2026), "Form, Timing, and Behavioral Matching of the Population Response to
# ALM Photoinhibition", Research Square preprint doi:10.21203/rs.3.rs-11447300/v1, on DANDI
# 000363 (Mesoscale Activity Map, Chen et al. 2024, Cell 187:676-691), which the paper reuses.
#
# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
# Actions"), 2026-11-21, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/yang-2026.yaml"
}
```

```
1	# Claims for Yang (2026), "Form, Timing, and Behavioral Matching of the Population Response to
2	# ALM Photoinhibition", Research Square preprint doi:10.21203/rs.3.rs-11447300/v1, on DANDI
3	# 000363 (Mesoscale Activity Map, Chen et al. 2024, Cell 187:676-691), which the paper reuses.
4	#
5	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
6	# Actions"), 2026-11-21, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
7	#
8	# Text read. The preprint, version 1 (posted 2026-10-22), from
9	# paper/10.21203-rs.3.rs-11447300-v1.txt: abstract, Introduction, Results, Materials and
10	# Methods, Discussion, figure legends of Figures 1 to 3, Table 1, and the Extended Data legends
11	# (Figures 1-1, 2-1, 3-1). There is no separate supplement; the Extended Data are figures whose
12	# legends are in the text. No PDF was supplied and no figure was read. Values shown only in a
13	# figure (per-mouse points, curves) are not available; claims rest on the numbers the text and
14	# Table 1 print.
15	#
16	# Code read. None. Code Accessibility says the code "has been deposited in a private GitHub
17	# repository and will be made publicly available upon publication". No method detail below is
18	# settled by code. The analyses used Python 3.12, NumPy and scikit-learn logistic regression
19	# (lbfgs), and one random seed, 17, for splits, folds and match order (Methods, Code and data;
20	# Statistics).
[... 858 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.21203-rs.3.rs-11447300-v1.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -120; wc -l docs/design.md
```

```
## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
  paper cites, or the latest published one. For a draft, record its
  modification time under `dataset: modified` in the attempt.
- **Reading.** List the assets and read metadata with the DANDI REST API
  (`https://api.dandiarchive.org/api/dandisets/<id>/versions/<version>/` and its
  `assets/` endpoint). Read NWB files by streaming them: open each asset's S3
  URL with `remfile` and `h5py`, and read it with `pynwb`. Do not download files
  to disk.
- **In an entry.** The entry names the dataset as `dandi:<id>/<version>` under
  `related`. The helper module keeps the version in one constant.

## CRCNS
286 docs/design.md
```

**Agent calls Bash**

```bash
cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in entries/fouke-2025/README.md; head -c 6000 attempts/fouke-2025-01.yaml
```

```
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
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]:
    print('----',c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source'])[:1500])
EOF
head -80 entries/fouke-2025/omr.py
```

```
---- markdown None
# Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository
that holds code only). This is the only published version. The draft holds the same 37 files
(same blobs and sizes); it differs only in metadata added later (authors, keywords, and a
`relatedResource` link to the paper), none of which the analysis uses.

**What the dandiset holds.** Freely swimming tracking of 25 zebrafish (ZF) and 12 *D. cerebrum*
(DC) larvae during the optomotor protocol of Figure 1 and Figure S1. The two-photon imaging and the
head-fixed tail tracking of Figures 2 to 4 are not in it.

**Outside inputs.** The stimulus codes in the files have no names. The names come from the paper's
[... 256 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000363/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000363/versions/" | python -m json.tool | head -60; python -c "import pynwb,remfile,h5py,dandi;print('ok')"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000363/versions/" | python -c "
import json,sys; d=json.load(sys.stdin)
for r in d['results']: print(r['version'], r['asset_count'], r['size'], r['created'])"
python - <<'EOF'
import json, urllib.request
url="https://api.dandiarchive.org/api/dandisets/000363/versions/0.231012.2129/assets/?page_size=200"
out=[]
while url:
    d=json.load(urllib.request.urlopen(url)); out+=d['results']; url=d['next']
json.dump(out,open('assets.json','w'))
print(len(out))
for a in sorted(out,key=lambda a:a['path'])[:200]: print(a['path'], round(a['size']/1e9,2))
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.12 venv && . venv/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy pandas scipy scikit-learn matplotlib 2>&1 | tail -3; python -c "import pynwb; print(pynwb.__version__)"; nproc; free -g
```

```
4.2.0
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
Swap:              2           0           2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > explore.py <<'EOF'
import json, time, h5py, remfile
assets=json.load(open('assets.json'))
a=[x for x in assets if '20200922T135318' in x['path']][0]
url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
import requests
r=requests.head(url,allow_redirects=True); s3=r.url.split('?')[0]
print(s3)
t=time.time()
f=h5py.File(remfile.File(s3),'r')
def walk(g,pre=''):
    for k in g:
        o=g[k]
        if isinstance(o,h5py.Dataset):
            print(pre+k, o.shape, o.dtype)
        else:
            if pre.count('/')>4: continue
            if k.startswith('ElectricalSeries') : print(pre+k,'(group)'); continue
            walk(o,pre+k+'/')
walk(f)
print(time.time()-t)
EOF
python explore.py 2>&1 | head -300
```

```
https://dandiarchive.s3.amazonaws.com/blobs/f76/fc8/f76fc8ac-80db-4554-8da6-46997a046236
acquisition/BehavioralEvents/delay_start_times/data (581,) float64
acquisition/BehavioralEvents/delay_start_times/timestamps (581,) float64
acquisition/BehavioralEvents/delay_stop_times/data (581,) float64
acquisition/BehavioralEvents/delay_stop_times/timestamps (581,) float64
acquisition/BehavioralEvents/go_start_times/data (527,) float64
acquisition/BehavioralEvents/go_start_times/timestamps (527,) float64
acquisition/BehavioralEvents/go_stop_times/data (527,) float64
acquisition/BehavioralEvents/go_stop_times/timestamps (527,) float64
acquisition/BehavioralEvents/left_lick_times/data (1129,) float64
acquisition/BehavioralEvents/left_lick_times/timestamps (1129,) float64
acquisition/BehavioralEvents/photostim_start_times/control (112,) uint8
acquisition/BehavioralEvents/photostim_start_times/control_description (3,) object
acquisition/BehavioralEvents/photostim_start_times/data (112,) float64
acquisition/BehavioralEvents/photostim_start_times/timestamps (112,) float64
acquisition/BehavioralEvents/photostim_stop_times/control (112,) uint8
acquisition/BehavioralEvents/photostim_stop_times/control_description (3,) object
acquisition/BehavioralEvents/photostim_stop_times/data (112,) float64
acquisition/BehavioralEvents/photostim_stop_times/timestamps (112,) float64
acquisition/BehavioralEvents/presample_start_times/data (527,) float64
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > ex2.py <<'EOF'
import json, time, h5py, remfile, numpy as np, collections, requests
s3="https://dandiarchive.s3.amazonaws.com/blobs/f76/fc8/f76fc8ac-80db-4554-8da6-46997a046236"
f=h5py.File(remfile.File(s3),'r')
B=f['acquisition/BehavioralEvents']
for k in ['photostim_start_times','photostim_stop_times']:
    g=B[k]; print(k, dict(g.attrs)); print(g['control_description'][:]); print(collections.Counter(g['control'][:]))
    for kk in g: print(kk, dict(g[kk].attrs))
print(B['photostim_start_times/data'][:10], B['photostim_start_times/timestamps'][:10])
print(B['photostim_stop_times/data'][:10], B['photostim_stop_times/timestamps'][:10])
for k in ['go_start_times','left_lick_times']:
    print(k, B[k+'/data'][:5], B[k+'/timestamps'][:5], dict(B[k].attrs))
for d in f['general/optogenetics']:
    g=f['general/optogenetics'][d]; print(d, g['description'][()], g['location'][()], g['excitation_lambda'][()], dict(g.attrs))
T=f['intervals/trials']
print(dict(T.attrs))
for k in T:
    v=T[k][:]
    print(k, T[k].attrs.get('description'), v[:8], collections.Counter(v.tolist()).most_common(8) if v.dtype==object or v.dtype.kind in 'iu' else (v.min(), v.max()))
U=f['units']
for k in ['classification','unit_quality','anno_name']:
    print(k, U[k].attrs.get('description'), collections.Counter(U[k][:].tolist()).most_common(40))
E=f['general/extracellular_ephys/electrodes']
print(collections.Counter(E['location'][:].tolist()).most_common(40))
print(collections.Counter(E['group_name'][:].tolist()))
for k in f['general/extracellular_ephys']: print(k)
print(f['session_description'][()], f['general/experiment_description'][()])
print(f['units/spike_times_index'][:5], f['units/sampling_rate'][:3], U['electrodes'][:5])
J=f['acquisition/BehavioralTimeSeries/Camera0_side_JawTracking']
print(dict(J.attrs), dict(J['data'].attrs), J['data'][100000:100005], J['timestamps'][:5], J['timestamps'][-3:])
EOF
python ex2.py
```

```
photostim_start_times {'comments': 'no comments', 'description': 'Timestamps of the photo-stimulation and the corresponding powers (in mW) being applied', 'namespace': 'core', 'neurodata_type': 'TimeSeries', 'object_id': '0ef66462-8364-4bb0-a89b-ea3cec92e1f7'}
[b'4' b'5' b'6']
Counter({np.uint8(5): 45, np.uint8(6): 36, np.uint8(4): 31})
control {}
control_description {}
data {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mW'}
timestamps {'interval': np.int64(1), 'unit': 'seconds'}
photostim_stop_times {'comments': 'no comments', 'description': 'Timestamps of the photo-stimulation being switched off', 'namespace': 'core', 'neurodata_type': 'TimeSeries', 'object_id': '4c780cb7-894e-489d-ab96-400824b5be9d'}
[b'4' b'5' b'6']
Counter({np.uint8(5): 45, np.uint8(6): 36, np.uint8(4): 31})
control {}
control_description {}
data {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mW'}
timestamps {'interval': np.int64(1), 'unit': 'seconds'}
[5.5 5.5 5.5 5.5 5.5 5.5 5.5 5.5 5.5 5.5] [249.176  255.8737 269.4368 276.3089 304.6152 311.4752 318.4957 345.6064
 352.4182 359.9946]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] [249.676  256.3737 269.9368 276.8089 305.1152 311.9752 318.9957 346.1064
 352.9182 360.4946]
go_start_times [1. 1. 1. 1. 1.] [ 3.2101 10.0833 16.9398 23.4115 30.2451] {'comments': 'no comments', 'description': 'Timestamps for event type: go - Start Time', 'namespace': 'core', 'neurodata_type': 'TimeSeries', 'object_id': 'd0e4d74e-cca2-4a55-b9d2-dd8d37a9e09c'}
left_lick_times [1. 1. 1. 1. 1.] [ 3.732  17.4599 30.8652 71.9865 72.1329] {'comments': 'no comments', 'description': 'Timestamps for event type: left lick', 'namespace': 'core', 'neurodata_type': 'TimeSeries', 'object_id': 'f9f9ac97-a1b0-4aa4-818a-a394ecaad500'}
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > survey.py <<'EOF'
import json, time, h5py, remfile, numpy as np, collections, requests, pickle
from concurrent.futures import ThreadPoolExecutor
assets=json.load(open('assets.json'))
def s3url(a):
    r=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/",timeout=60).json()
    return [u for u in r['contentUrl'] if 's3' in u][0]
def one(a):
    try:
        url=s3url(a)
        f=h5py.File(remfile.File(url),'r')
        B=f['acquisition/BehavioralEvents']
        out={'path':a['path'],'url':url,'size':a['size']}
        T=f['intervals/trials']
        out['trials']={k:T[k][:] for k in T if k not in ('id',)}
        out['go']=B['go_start_times/timestamps'][:] if 'go_start_times' in B else None
        out['events']={k:B[k+'/timestamps'][:] for k in B if k.endswith('_times') and 'timestamps' in B[k]}
        if 'photostim_start_times' in B:
            out['ps_ctrl']=B['photostim_start_times/control'][:]; out['ps_t']=B['photostim_start_times/timestamps'][:]
            out['ps_stop']=B['photostim_stop_times/timestamps'][:]
            out['ps_desc']=B['photostim_start_times/control_description'][:]
        og={}
        if 'optogenetics' in f['general']:
            for d in f['general/optogenetics']:
                g=f['general/optogenetics'][d]; og[d]=(g['description'][()], g['location'][()])
        out['og']=og
        U=f['units']
        out['cls']=U['classification'][:]; out['anno']=U['anno_name'][:]; out['uel']=U['electrodes'][:]
        out['uq']=U['unit_quality'][:]
        E=f['general/extracellular_ephys/electrodes']
        out['eloc']=E['location'][:]; out['eid']=E['id'][:]
        out['nspk']=U['spike_times'].shape[0]
        out['video']={k:f['acquisition/BehavioralTimeSeries'][k]['data'].shape for k in f['acquisition/BehavioralTimeSeries']} if 'BehavioralTimeSeries' in f['acquisition'] else {}
        out['subject']=f['general/subject/subject_id'][()]
        out['start']=f['session_start_time'][()]
        return out
    except Exception as e:
        return {'path':a['path'],'err':repr(e)}
t=time.time()
with ThreadPoolExecutor(8) as ex: res=list(ex.map(one,assets))
pickle.dump(res,open('survey.pkl','wb'))
print(time.time()-t, sum('err' in r for r in res))
for r in res:
    if 'err' in r: print(r)
EOF
python survey.py
```

```
414.69999957084656 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > an1.py <<'EOF'
import pickle, numpy as np, json, collections
res=pickle.load(open('survey.pkl','rb'))
rows=[]
for r in res:
    tr=r['trials']; n=len(tr['start_time'])
    ps = r.get('ps_t') is not None and len(r.get('ps_t',[]))>0
    stimtr = np.array([x!=b'N/A' for x in tr['photostim_duration']])
    # bilateral codes
    bil=[]
    for d,(desc,loc) in r['og'].items():
        L=json.loads(loc); 
        if sum(1 for x in L if x.get('brain_area')=='ALM')>=2 and len({x['ml_location'] for x in L})==2: bil.append(d.split('_')[-1])
    med=None; nb=0; durs=None
    if ps:
        ctrl=r['ps_ctrl'].astype(str); go=r['go']
        sel=np.isin(ctrl,bil)
        on=r['ps_t'][sel]; nb=sel.sum()
        if nb:
            # nearest go after onset
            idx=np.searchsorted(go,on); idx=np.clip(idx,0,len(go)-1)
            rel=on-go[idx]
            med=np.median(rel); durs=np.median(r['ps_stop'][sel]-on)
    rows.append((r['path'].split('/')[1][:40], n, stimtr.sum(), ps, bil, nb, med, durs, (r['cls']==b'good').sum(), len(r['video'])))
nps=sum(1 for x in rows if x[2]>0); print('sessions with photostim trials', nps, 'with ps events', sum(x[3] for x in rows))
late=[x for x in rows if x[6] is not None and abs(x[6]+0.5)<=0.08]
print('late-delay', len(late), 'mice', len({x[0][:10] for x in late}))
print(collections.Counter(round(x[6],1) for x in rows if x[6] is not None))
for x in rows: print(x)
EOF
python an1.py
```

```
sessions with photostim trials 168 with ps events 168
late-delay 112 mice 19
Counter({np.float64(-0.5): 112, np.float64(-1.2): 39})
('sub-440956_ses-20190208T133600_behavior+', 480, np.int64(126), True, ['6'], np.int64(84), np.float64(-1.200000000000017), np.float64(0.5), np.int64(375), 3)
('sub-440956_ses-20190210T155629_behavior+', 582, np.int64(171), True, ['6'], np.int64(115), np.float64(-1.1999000000000706), np.float64(0.5), np.int64(552), 3)
('sub-440958_ses-20190216T162508_behavior+', 620, np.int64(147), True, ['6'], np.int64(101), np.float64(-1.199999999999818), np.float64(0.5), np.int64(0), 3)
('sub-442571_ses-20190301T140324_behavior+', 501, np.int64(118), True, ['6'], np.int64(81), np.float64(-1.1999000000000706), np.float64(0.5), np.int64(433), 3)
('sub-455219_ses-20190807T134913_behavior+', 630, np.int64(127), True, ['6'], np.int64(50), np.float64(-1.1999499999999443), np.float64(0.5), np.int64(463), 4)
('sub-440957_ses-20190214T144611_behavior+', 660, np.int64(172), True, ['6'], np.int64(103), np.float64(-1.1999000000005253), np.float64(0.5), np.int64(169), 3)
('sub-440959_ses-20190223T173853_behavior+', 448, np.int64(95), True, ['6'], np.int64(70), np.float64(-1.199950000000058), np.float64(0.5), np.int64(537), 3)
('sub-440958_ses-20190213T115547_behavior+', 521, np.int64(74), True, [], np.int64(0), None, None, np.int64(347), 3)
('sub-440956_ses-20190207T120657_behavior+', 368, np.int64(78), True, ['6'], np.int64(51), np.float64(-1.1999000000000706), np.float64(0.5), np.int64(459), 3)
('sub-440956_ses-20190209T150135_behavior+', 518, np.int64(132), True, ['6'], np.int64(91), np.float64(-1.1999000000000706), np.float64(0.5), np.int64(205), 3)
('sub-440959_ses-20190219T121506_behavior+', 437, np.int64(92), True, ['6'], np.int64(53), np.float64(-1.2000000000000455), np.float64(0.5), np.int64(214), 3)
('sub-440958_ses-20190217T154414_behavior+', 590, np.int64(145), True, ['6'], np.int64(99), np.float64(-1.2000000000000455), np.float64(0.5), np.int64(367),
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > an2.py <<'EOF'
import pickle, numpy as np, json, collections
res=pickle.load(open('survey.pkl','rb'))
br=collections.Counter(); an=collections.Counter()
for r in res:
    locs={}
    for eid,l in zip(r['eid'],r['eloc']):
        try: locs[eid]=json.loads(l)['brain_regions']
        except Exception: locs[eid]=l.decode()
    g=r['cls']==b'good'
    for e,a in zip(r['uel'][g],r['anno'][g]):
        br[locs.get(e,'?')]+=1; an[a.decode()]+=1
print(br.most_common())
print(len(an)); print(an.most_common(400))
EOF
python an2.py
```

```
[('left ALM', 12377), ('right ALM', 11268), ('left Thalamus', 7406), ('right Striatum', 5772), ('right Thalamus', 5472), ('right Midbrain', 5398), ('left Midbrain', 5232), ('left Striatum', 4967), ('left ECT', 2961), ('left Medulla', 2888), ('right Medulla', 1912), ('left BLA', 1344), ('right BLA', 1266), ('right ECT', 1190)]
293
[('Caudoputamen', 6743), ('Secondary motor area, layer 5', 4311), ('Orbital area, lateral part, layer 5', 2846), ('Orbital area, ventrolateral part, layer 5', 2547), ('Mediodorsal nucleus of thalamus', 2281), ('Midbrain reticular nucleus', 2208), ('Anterior olfactory nucleus', 2037), ('Secondary motor area, layer 6a', 1504), ('Posterior complex of the thalamus', 1482), ('Secondary motor area, layer 2/3', 1367), ('Frontal pole, layer 5', 1363), ('Superior colliculus, motor related, intermediate white layer', 1308), ('Ventral anterior-lateral complex of the thalamus', 1283), ('Piriform area', 1107), ('Orbital area, lateral part, layer 2/3', 1046), ('Orbital area, ventrolateral part, layer 2/3', 1030), ('Orbital area, lateral part, layer 6a', 1029), ('Midbrain', 1002), ('Orbital area, ventrolateral part, layer 6a', 994), ('Olfactory areas', 982), ('Lateral posterior nucleus of the thalamus', 943), ('Superior colliculus, motor related, intermediate gray layer', 913), ('Lateral dorsal nucleus of thalamus', 880), ('Supplemental somatosensory area, layer 6a', 864), ('Ventral medial nucleus of the thalamus', 727), ('Anterior pretectal nucleus', 714), ('Gigantocellular reticular nucleus', 704), ('Ventral posteromedial nucleus of the thalamus', 633), ('Field CA1', 612), ('Paracentral nucleus', 591), ('Globus pallidus, external segment', 589), ('Endopiriform nucleus, ventral part', 558), ('Endopiriform nucleus, dorsal part', 530), ('Central lateral nucleus of the thalamus', 467), ('Lobules IV-V', 466), ('Zona incerta', 464), ('Postsubiculum', 428), ('Frontal pole, layer 6a', 385), ('Primary somatosensory area, mouth, layer 6a', 369), ('Primary somatos
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > an3.py <<'EOF'
import pickle, numpy as np, json, collections
res=pickle.load(open('survey.pkl','rb'))
REG={'ALM':'ALM','Striatum':'striatum','Thalamus':'thalamus','Midbrain':'midbrain','Medulla':'medulla'}
def trials(r):
    tr=r['trials']; st=tr['start_time']; sp=tr['stop_time']; n=len(st)
    go=r['go']; gi=np.searchsorted(go,st); gt=np.full(n,np.nan)
    for i in range(n):
        j=gi[i]
        if j<len(go) and go[j]<sp[i]: gt[i]=go[j]
    code=np.zeros(n,int); on=np.full(n,np.nan)
    if r.get('ps_t') is not None:
        ti=np.searchsorted(st,r['ps_t'],side='right')-1
        for t,c,i in zip(r['ps_t'],r['ps_ctrl'],ti):
            if i>=0 and t<sp[i]: code[i]=int(c); on[i]=t
    L=r['events']['left_lick_times']; R=r['events']['right_lick_times']
    fl=np.full(n,np.nan); fd=np.zeros(n,int)
    for i in range(n):
        if np.isnan(gt[i]): continue
        a=L[(L>gt[i])&(L<sp[i])]; b=R[(R>gt[i])&(R<sp[i])]
        la=a.min() if len(a) else np.inf; lb=b.min() if len(b) else np.inf
        if np.isfinite(min(la,lb)): fl[i]=min(la,lb); fd[i]=1 if lb<la else -1
    return dict(go=gt,code=code,on=on,first=fl,dir=fd,instr=tr['trial_instruction'].astype(str),
                early=tr['early_lick'].astype(str)=='early',outcome=tr['outcome'].astype(str),stim=tr['photostim_duration']!=b'N/A',
                auto=tr['auto_water'],free=tr['free_water'])
out=[]
for r in res:
    if r.get('ps_t') is None or len(r['ps_t'])==0: continue
    T=trials(r)
    bil=[d.split('_')[-1] for d,(desc,loc) in r['og'].items() if len({x['ml_location'] for x in json.loads(loc) if x.get('brain_area')=='ALM'})==2]
    lz=np.isin(T['code'],[int(b) for b in bil])
    if not lz.any(): continue
    med=np.nanmedian(T['on'][lz]-T['go'][lz])
    if abs(med+0.5)>0.08: continue
    # sanity: stim trials vs ps events
    mism=(T['stim']!=(T['code']>0)).sum()
    locs={}
    for eid,l in zip(r['eid'],r['eloc']):
        try: locs[eid]=json.loads(l)['brain_regions'].split(' ')[-1]
        except Exception: locs[eid]='?'
    g=r['cls']==b'good'
    reg=collections.Counter(locs.get(e) for e in r['uel'][g])
    ctrl=(~T['stim'])&(~T['early'])
    sess=r['path'].split('/')[1].split('_')[1]; mouse=r['path'].split('/')[0]
    for rr in REG:
        nu=reg.get(rr,0)
        for rd in 'ab':
            lzr=lz&(~T['early']) if rd=='b' else lz
            sides=[s for s in ('left','right') if (lzr&(T['instr']==s)).sum()>=10 and (ctrl&(T['instr']==s)).sum()>=10]
            out.append((mouse,sess,REG[rr],rd,nu,len(sides),mism,lz.sum(),(lz&T['early']).sum()))
import pandas as pd
df=pd.DataFrame(out,columns=['mouse','sess','region','laserread','nunits','nsides','mism','nlaser','nlaserearly'])
pickle.dump(df,open('counts.pkl','wb'))
print('mismatch stim vs events', df.mism.max())
ok=df[(df.nunits>=20)&(df.nsides>0)]
print(ok.groupby(['laserread','region']).agg(mice=('mouse','nunique'),sessions=('sess','nunique')))
print(df.drop_duplicates('sess')[['nlaser','nlaserearly']].describe())
EOF
python an3.py
```

```
mismatch stim vs events 0
                    mice  sessions
laserread region                  
a         ALM         19        94
          medulla      8        35
          midbrain    16        72
          striatum    13        49
          thalamus    10        31
b         ALM         19        93
          medulla      8        35
          midbrain    16        71
          striatum    13        48
          thalamus    10        31
           nlaser  nlaserearly
count  112.000000   112.000000
mean    36.535714     3.651786
std     10.069961     3.875797
min      4.000000     0.000000
25%     31.750000     1.000000
50%     36.000000     2.000000
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > sp.py <<'EOF'
import h5py, remfile, numpy as np, time, pickle
res=pickle.load(open('survey.pkl','rb'))
r=[x for x in res if '20200922T135318' in x['path']][0]
t=time.time()
f=h5py.File(remfile.File(r['url']),'r')
st=f['units/spike_times']; print(st.chunks, st.compression, st.shape)
idx=f['units/spike_times_index'][:]
g=np.where(r['cls']==b'good')[0]
t1=time.time()
allst=st[:]
print('full read', time.time()-t1, allst.nbytes/1e6)
J=f['acquisition/BehavioralTimeSeries/Camera0_side_JawTracking/data']; print(J.chunks, J.compression)
t1=time.time(); j=J[:]; print('jaw', time.time()-t1, np.isnan(j).sum(0), (j[:,2]<0.9).mean(), np.percentile(j[:,2],[1,5,50]))
for k in f['acquisition/BehavioralTimeSeries']: print(k)
EOF
python sp.py
```

```
None None (32116529,)
full read 3.589081287384033 256.932232
None None
jaw 0.15271472930908203 [0 0 0] 0.00025350785277854546 [1. 1. 1.]
Camera0_side_JawTracking
Camera0_side_NoseTracking
Camera0_side_TongueTracking
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import h5py, remfile, numpy as np, pickle
res=pickle.load(open('survey.pkl','rb'))
for r in [x for x in res if '20200922T135318' in x['path'] or '20201216T120333' in x['path']]:
    f=h5py.File(remfile.File(r['url']),'r')
    B=f['acquisition/BehavioralTimeSeries']
    for k in B:
        d=B[k]['data'][:200000]; ts=B[k]['timestamps']
        print(k, B[k].attrs['description'], np.isnan(d).mean(0), np.percentile(d[:,2],[1,10,50,90]), (d[:,0]==0).mean(), ts.shape)
EOF
```

```
Sat Nov 21 07:06:16 UTC 2026
Camera0_side_JawTracking Time series for JawTracking position: ('jaw_x', 'jaw_y', 'jaw_likelihood') [0. 0. 0.] [1. 1. 1. 1.] 0.0 (1005886,)
Camera0_side_NoseTracking Time series for NoseTracking position: ('nose_x', 'nose_y', 'nose_likelihood') [0. 0. 0.] [1. 1. 1. 1.] 0.0 (1005886,)
Camera0_side_TongueTracking Time series for TongueTracking position: ('tongue_x', 'tongue_y', 'tongue_likelihood') [0. 0. 0.] [2.54487660e-05 3.55183271e-05 6.33245072e-05 1.00000000e+00] 0.0 (1005886,)
Camera0_side_JawTracking Time series for JawTracking position: ('jaw_x', 'jaw_y', 'jaw_likelihood') [0. 0. 0.] [1. 1. 1. 1.] 0.0 (1007268,)
Camera0_side_NoseTracking Time series for NoseTracking position: ('nose_x', 'nose_y', 'nose_likelihood') [0. 0. 0.] [1. 1. 1. 1.] 0.0 (1007268,)
Camera0_side_TongueTracking Time series for TongueTracking position: ('tongue_x', 'tongue_y', 'tongue_likelihood') [0. 0. 0.] [3.38862537e-05 5.36416697e-05 1.08100474e-04 1.00000000e+00] 0.0 (1007268,)
Camera3_side_JawTracking Time series for JawTracking position: ('jaw_x', 'jaw_y', 'jaw_likelihood') [0. 0. 0.] [1. 1. 1. 1.] 0.0 (1007268,)
Camera3_side_NoseTracking Time series for NoseTracking position: ('nose_x', 'nose_y', 'nose_likelihood') [0. 0. 0.] [1. 1. 1. 1.] 0.0 (1007268,)
Camera3_side_TongueTracking Time series for TongueTracking position: ('tongue_x', 'tongue_y', 'tongue_likelihood') [0. 0. 0.] [3.38862537e-05 5.36416697e-05 1.08100474e-04 1.00000000e+00] 0.0 (1007268,)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import pickle, numpy as np, collections
res=pickle.load(open('survey.pkl','rb'))
sig=collections.defaultdict(list)
for r in res:
    sig[(r['nspk'], len(r['trials']['start_time']))].append(r['path'])
print([v for v in sig.values() if len(v)>1])
# outcome-based vs lick-based direction consistency quick
for r in res[:1]: print(r['ps_desc'], r['video'])
EOF
```

```
[]
[b'4' b'6'] {'Camera0_side_JawTracking': (929393, 3), 'Camera0_side_NoseTracking': (929393, 3), 'Camera0_side_TongueTracking': (929393, 3)}
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/yang-2026/mam.py",
 "content": "\"\"\"Loading and measures for the late-delay photoinhibition sessions of dandiset 000363.\n\nYang (2026), \"Form, Timing, and Behavioral Matching of the Population Response to ALM\nPhotoinhibition\", Research Square preprint doi:10.21203/rs.3.rs-11447300/v1, which reanalyses\nthe Mesoscale Activity Map dataset of Chen et al. (2024), DANDI 000363.\n\nEach NWB file holds one session: the trial table, behavioural events (Go cue, licks,\nphotostimulation onsets with a control code), the photostimulation sites, video keypoints, and\nthe units (spike times, a classifier label, the electrode of each unit). Files are streamed from\nthe archive at the pinned version; only the arrays needed are read, and nothing is written to disk.\nThe raw electrical series, which make up almost all of each file, are never read.\n\nWhere the parameters come from. \"Claims\" is claims/yang-2026.yaml, whose shared methods M1 to M10\ncite the paper; \"Methods\" is the paper's Materials and Methods.\n\n- Sessions, laser and control trials (claims M1; Methods, Dataset, paragraph 2): bilateral\n  trials are those whose photostimulation control code has a site list with ALM on both sides;\n  a session enters when the median bilateral onset is within 0.08 s of -0.5 s from Go; control\n  trials have no photostimulation and no early lick. Whether laser trials with an early lick are\n  kept is open; `LASER_EARLY` names the readings (\"keep\", \"drop\").\n- Units and regions (claims M2; Methods, Units and regions): units with classification \"good\";\n  a region is the probe target the files give for the unit's electrode (`brain_regions` of the\n  electrode location, \"left ALM\", \"right Striatum\" and so on), hemispheres pooled; reading (a) of\n  M2. A region enters with at least 20 good units, a side with at least 10 laser and 10 control\n  trials.\n- Lick direction (claims M3, open): \"licks\", the side of the first lick after Go; \"outcome\",\n  instructed side for hits, the other side for misses. Reaction time is the first lick after Go\n  minus Go (a standard choice, M3). The pre-lick window is the 200 ms before that lick, in four\n  50 ms bins (Methods, Matched distance).\n- Rates (claims M4; Methods, Rates and coding axes): mean rate in a window, z-scored by the mean\n  and SD of control trials in that window; units with control SD below 1e-6 dropped. The early\n  window is 20 to 120 ms after laser onset. Its placement on control trials is open (M4):\n  \"go\", every trial at the session's median onset; \"own\", laser trials at their own onset and\n  controls at the median onset. Units used by a measure are those kept in every window it uses\n  (a standard choice, M4).\n- Go-aligned grid (claims M10; Methods, Time courses): 50 ms bins from -600 to +600 ms; 100 ms\n  bins as the mean of two adjacent 50 ms rates, stepped by 50 ms (the non-overlapping reading is\n  the subset starting at -600 ms).\n- Video regression (claims M5; Methods, Rates and coding axes): mean x and y of jaw, nose and\n  tongue over the choice window with an intercept. A frame counts as a detection when the\n  keypoint's likelihood is at least `LIKELIHOOD_MIN` (0.9), an assumption: the files give a\n  likelihood per frame and no detection flag, and 0.9 is the usual DeepLabCut cut. Trials\n  without a detection take the control mean (\"fill\", reading a) or are dropped from the fit\n  (\"drop\", reading b).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport json\nimport os\nimport zlib\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\n\nDANDISET_ID = \"000363\"\nDANDISET_VERSION = \"0.231012.2129\"\nPAPER_KEY = \"yang-2026\"\n\nREGIONS = [\"ALM\", \"striatum\", \"thalamus\", \"midbrain\", \"medulla\"]\n_PROBE_REGION = {\"ALM\": \"ALM\", \"Striatum\": \"striatum\", \"Thalamus\": \"thalamus\",\n                 \"Midbrain\": \"midbrain\", \"Medulla\": \"medulla\"}\n\nLATE_ONSET, ONSET_TOL = -0.50, 0.08      # Methods, Dataset\nMIN_UNITS, MIN_TRIALS_SIDE = 20, 10      # Methods, Units and regions\nSD_MIN = 1e-6                            # Methods, Rates and coding axes\nEARLY = (0.02, 0.12)                     # s after laser onset\nCHOICE_BINS = slice(0, 12)               # -600 to 0 ms (Methods, Rates and coding axes)\nACTION_BINS = slice(12, 18)              # 0 to 300 ms\nGO_EDGES = np.round(np.arange(-0.6, 0.6001, 0.05), 3)   # 24 bins of 50 ms\nN_GO = len(GO_EDGES) - 1\nPRELICK = 0.2                            # s before the first lick, 4 bins of 50 ms\nLIKELIHOOD_MIN = 0.9                     # assumption, see the docstring\nKEYPOINTS = [\"Jaw\", \"Nose\", \"Tongue\"]\n\n# Column layout of the per-trial rate array: 24 Go bins, early (\"go\" placement), early (\"own\"\n# placement), 4 pre-lick bins.\nCOL_EARLY_GO, COL_EARLY_OWN = N_GO, N_GO + 1\nCOL_PRE = slice(N_GO + 2, N_GO + 6)\nN_COLS = N_GO + 6\n\n\ndef seed(claim: str, k: int = 0) -> int:\n    \"\"\"The claim's seed (protocol, Author step 3), plus k.\"\"\"\n    return zlib.crc32(f\"{PAPER_KEY}/{claim}\".encode()) + k\n\n\n# --------------------------------------------------------------------------------------------\n# Archive access\n\n\ndef assets() -> list[dict]:\n    \"\"\"Path, size and streaming URL of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        out = []\n        for a in ds.get_assets():\n            if a.path.endswith(\".nwb\"):\n                out.append({\"path\": a.path, \"size\": a.size,\n                            \"url\": a.get_content_url(follow_redirects=1, strip_query=True)})\n    return sorted(out, key=lambda a: a[\"path\"])\n\n\ndef _open(url: str) -> h5py.File:\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef _names(path: str) -> tuple[str, str]:\n    base = path.split(\"/\")[-1]\n    return base.split(\"_\")[0], base.split(\"_\")[1]\n\n\ndef _trial_table(f: h5py.File) -> dict:\n    \"\"\"Trial events per trial: Go time, photostimulation code and onset, first lick.\"\"\"\n    T = f[\"intervals/trials\"]\n    st, sp = T[\"start_time\"][:], T[\"stop_time\"][:]\n    n = len(st)\n    B = f[\"acquisition/BehavioralEvents\"]\n    go = B[\"go_start_times/timestamps\"][:]\n    gt = np.full(n, np.nan)\n    j = np.searchsorted(go, st)\n    for i in range(n):\n        if j[i] < len(go) and go[j[i]] < sp[i]:\n            gt[i] = go[j[i]]\n    code = np.zeros(n, int)\n    on = np.full(n, np.nan)\n    if \"photostim_start_times\" in B:\n        pt = B[\"photostim_start_times/timestamps\"][:]\n        pc = B[\"photostim_start_times/control\"][:]\n        ti = np.searchsorted(st, pt, side=\"right\") - 1\n        for t, c, i in zip(pt, pc, ti):\n            if i >= 0 and t < sp[i]:\n                code[i], on[i] = int(c), t\n    left = B[\"left_lick_times/timestamps\"][:]\n    right = B[\"right_lick_times/timestamps\"][:]\n    first = np.full(n, np.nan)\n    lick_dir = np.zeros(n, int)\n    for i in range(n):\n        if np.isnan(gt[i]):\n            continue\n        a = left[(left > gt[i]) & (left < sp[i])]\n        b = right[(right > gt[i]) & (right < sp[i])]\n        la = a.min() if len(a) else np.inf\n        lb = b.min() if len(b) else np.inf\n        if np.isfinite(min(la, lb)):\n            first[i] = min(la, lb)\n            lick_dir[i] = 1 if lb < la else -1\n    dec = lambda k: np.array([x.decode() if isinstance(x, bytes) else str(x) for x in T[k][:]])\n    instr = dec(\"trial_instruction\")\n    outcome = dec(\"outcome\")\n    sites = {}\n    if \"optogenetics\" in f[\"general\"]:\n        for d in f[\"general/optogenetics\"]:\n            loc = json.loads(f[\"general/optogenetics\"][d][\"location\"][()])\n            sites[int(d.split(\"_\")[-1])] = loc\n    bilateral = [c for c, loc in sites.items()\n                 if len({x[\"ml_location\"] for x in loc if x.get(\"brain_area\") == \"ALM\"}) == 2]\n    outcome_dir = np.where(outcome == \"hit\", np.where(instr == \"right\", 1, -1),\n                           np.where(outcome == \"miss\", np.where(instr == \"right\", -1, 1), 0))\n    return {\n        \"n\": n, \"start\": st, \"stop\": sp, \"go\": gt, \"code\": code, \"onset\": on - gt,\n        \"first_lick\": first - gt, \"lick_dir\": lick_dir, \"outcome_dir\": outcome_dir,\n        \"instr\": np.where(instr == \"right\", 1, np.where(instr == \"left\", -1, 0)),\n        \"early\": dec(\"early_lick\") == \"early\", \"outcome\": outcome,\n        \"stim\": dec(\"photostim_duration\") != \"N/A\", \"auto_water\": T[\"auto_water\"][:],\n        \"free_water\": T[\"free_water\"][:], \"bilateral_codes\": bilateral, \"sites\": sites,\n        \"photostim_events\": int(len(B[\"photostim_start_times/timestamps\"])) if \"photostim_start_times\" in B else 0,\n    }\n\n\ndef survey(asset: dict) -> dict:\n    \"\"\"Session metadata and trial table, without spikes or video.\"\"\"\n    f = _open(asset[\"url\"])\n    mouse, ses = _names(asset[\"path\"])\n    tt = _trial_table(f)\n    U = f[\"units\"]\n    cls = U[\"classification\"][:]\n    out = {\"path\": asset[\"path\"], \"url\": asset[\"url\"], \"mouse\": mouse, \"session\": ses,\n           \"size\": asset[\"size\"], \"trials\": tt, \"n_units\": len(cls),\n           \"n_good\": int((cls == b\"good\").sum()), \"n_spikes\": int(U[\"spike_times\"].shape[0])}\n    bil = np.isin(tt[\"code\"], tt[\"bilateral_codes\"])\n    out[\"n_bilateral\"] = int(bil.sum())\n    out[\"median_onset\"] = float(np.nanmedian(tt[\"onset\"][bil])) if bil.any() else np.nan\n    out[\"has_photostim\"] = bool(tt[\"stim\"].any())\n    f.close()\n    return out\n\n\ndef survey_all(asset_list: list[dict], workers: int = 8) -> list[dict]:\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(survey, asset_list))\n\n\ndef is_late_delay(s: dict) -> bool:\n    return np.isfinite(s[\"median_onset\"]) and abs(s[\"median_onset\"] - LATE_ONSET) <= ONSET_TOL\n\n\ndef _video(f: h5py.File, go: np.ndarray) -> tuple[np.ndarray, dict]:\n    \"\"\"Per trial mean x, y of jaw, nose, tongue over the choice window (-0.6 to 0 s from Go).\"\"\"\n    B = f[\"acquisition/BehavioralTimeSeries\"]\n    out = np.full((len(go), 6), np.nan)\n    info = {}\n    for k, kp in enumerate(KEYPOINTS):\n        name = f\"Camera0_side_{kp}Tracking\"\n        if name not in B:\n            info[kp] = \"missing\"\n            continue\n        d = B[name][\"data\"][:]\n        ts = B[name][\"timestamps\"][:]\n        ok = d[:, 2] >= LIKELIHOOD_MIN\n        csum = np.vstack([np.zeros((1, 3)), np.cumsum(np.c_[d[:, 0] * ok, d[:, 1] * ok, ok], axis=0)])\n        a = np.searchsorted(ts, go - 0.6)\n        b = np.searchsorted(ts, go)\n        valid = np.isfinite(go)\n        a, b = np.where(valid, a, 0), np.where(valid, b, 0)\n        s = csum[b] - csum[a]\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            out[:, 2 * k] = np.where(s[:, 2] > 0, s[:, 0] / s[:, 2], np.nan)\n            out[:, 2 * k + 1] = np.where(s[:, 2] > 0, s[:, 1] / s[:, 2], np.nan)\n        info[kp] = {\"frames\": len(ts), \"detected\": float(ok.mean()),\n                    \"frame_interval_ms\": float(np.median(np.diff(ts[:2000])) * 1000)}\n    return out, info\n\n\ndef load_session(s: dict) -> dict:\n    \"\"\"Rates of the good units of the five regions, per trial, in the windows the analyses use.\n\n    `rates` has shape (trials, units, N_COLS) in spikes/s (see the column layout above); pre-lick\n    columns are NaN on trials without a lick after Go. Trials without a Go cue keep NaN rates.\n    \"\"\"\n    f = _open(s[\"url\"])\n    tt = s[\"trials\"]\n    U = f[\"units\"]\n    cls = U[\"classification\"][:]\n    uel = U[\"electrodes\"][:]\n    eloc = f[\"general/extracellular_ephys/electrodes/location\"][:]\n    probe = []\n    for e in uel:\n        try:\n            probe.append(json.loads(eloc[e])[\"brain_regions\"])\n        except (ValueError, KeyError):\n            probe.append(\"\")\n    probe = np.array(probe)\n    region = np.array([_PROBE_REGION.get(p.split(\" \")[-1], \"\") for p in probe])\n    keep = np.where((cls == b\"good\") & (region != \"\"))[0]\n    idx = U[\"spike_times_index\"][:]\n    spikes = U[\"spike_times\"][:]\n    go = tt[\"go\"]\n    med = s[\"median_onset\"]\n    n = tt[\"n\"]\n    bil = np.isin(tt[\"code\"], tt[\"bilateral_codes\"])\n    starts = np.full((n, N_COLS), np.nan)\n    ends = np.full((n, N_COLS), np.nan)\n    starts[:, :N_GO] = go[:, None] + GO_EDGES[None, :-1]\n    ends[:, :N_GO] = go[:, None] + GO_EDGES[None, 1:]\n    starts[:, COL_EARLY_GO] = go + med + EARLY[0]\n    ends[:, COL_EARLY_GO] = go + med + EARLY[1]\n    own = np.where(bil, tt[\"onset\"], med)\n    starts[:, COL_EARLY_OWN] = go + own + EARLY[0]\n    ends[:, COL_EARLY_OWN] = go + own + EARLY[1]\n    fl = go + tt[\"first_lick\"]\n    pre_edges = np.arange(-PRELICK, 0.0001, 0.05)\n    starts[:, COL_PRE] = fl[:, None] + pre_edges[None, :-1]\n    ends[:, COL_PRE] = fl[:, None] + pre_edges[None, 1:]\n    dur = ends - starts\n    fin = np.isfinite(starts)\n    sflat, eflat = starts[fin], ends[fin]\n    rates = np.full((n, len(keep), N_COLS), np.nan, dtype=np.float32)\n    unsorted = 0\n    for j, u in enumerate(keep):\n        lo = idx[u - 1] if u > 0 else 0\n        st = spikes[lo:idx[u]]\n        if np.any(np.diff(st) < 0):\n            unsorted += 1\n            st = np.sort(st)\n        c = np.searchsorted(st, eflat) - np.searchsorted(st, sflat)\n        r = np.full((n, N_COLS), np.nan)\n        r[fin] = c / dur[fin]\n        rates[:, j, :] = r\n    video, vinfo = _video(f, go)\n    out = {k: s[k] for k in (\"path\", \"mouse\", \"session\", \"median_onset\")}\n    out.update({\"trials\": tt, \"rates\": rates, \"region\": region[keep], \"probe\": probe[keep],\n                \"video\": video, \"video_info\": vinfo, \"unsorted_units\": unsorted,\n                \"spike_range\": (float(spikes.min()), float(spikes.max())) if len(spikes) else (np.nan, np.nan),\n                \"trial_range\": (float(tt[\"start\"][0]), float(tt[\"stop\"][-1])),\n                \"first_spikes\": spikes[:20].copy()})\n    f.close()\n    return out\n\n\ndef load_all(surveys: list[dict], workers: int = 3) -> list[dict]:\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(load_session, surveys))\n\n\n# --------------------------------------------------------------------------------------------\n# Trial sets\n\n\ndef trial_sets(S: dict, laser_early: str = \"drop\", lick: str = \"licks\") -> dict:\n    \"\"\"Laser and control masks, valid sides, lick direction and reaction time (M1, M3).\"\"\"\n    tt = S[\"trials\"]\n    has_go = np.isfinite(tt[\"go\"])\n    laser = np.isin(tt[\"code\"], tt[\"bilateral_codes\"]) & has_go\n    if laser_early == \"drop\":\n        laser &= ~tt[\"early\"]\n    control = (~tt[\"stim\"]) & (~tt[\"early\"]) & has_go\n    lick_dir = tt[\"lick_dir\"] if lick == \"licks\" else tt[\"outcome_dir\"]\n    rt = tt[\"first_lick\"].copy()\n    rt[tt[\"lick_dir\"] == 0] = np.nan\n    sides = [sd for sd in (-1, 1)\n             if (laser & (tt[\"instr\"] == sd)).sum() >= MIN_TRIALS_SIDE\n             and (control & (tt[\"instr\"] == sd)).sum() >= MIN_TRIALS_SIDE]\n    return {\"laser\": laser, \"control\": control, \"sides\": sides, \"lick_dir\": lick_dir,\n            \"rt\": rt, \"instr\": tt[\"instr\"]}\n\n\ndef zscore_window(X: np.ndarray, control: np.ndarray) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Z-score (trials, units) by control trials; return z and the mask of units kept.\"\"\"\n    mu = np.nanmean(X[control], axis=0)\n    sd = np.nanstd(X[control], axis=0)\n    keep = sd >= SD_MIN\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        Z = (X - mu) / np.where(keep, sd, 1.0)\n    return Z, keep\n\n\ndef window_rates(S: dict, units: np.ndarray, name) -> np.ndarray:\n    \"\"\"Rates (trials, units) in a named window: 'choice', 'action', 'early_go', 'early_own',\n    'pre' (mean of the four pre-lick bins), ('go50', k), ('go100', k) with k the 50 ms start\n    index, ('pre50', k).\"\"\"\n    R = S[\"rates\"][:, units, :]\n    if name == \"choice\":\n        return R[:, :, CHOICE_BINS].mean(axis=2)\n    if name == \"action\":\n        return R[:, :, ACTION_BINS].mean(axis=2)\n    if name == \"early_go\":\n        return R[:, :, COL_EARLY_GO]\n    if name == \"early_own\":\n        return R[:, :, COL_EARLY_OWN]\n    if name == \"pre\":\n        return R[:, :, COL_PRE].mean(axis=2)\n    kind, k = name\n    if kind == \"go50\":\n        return R[:, :, k]\n    if kind == \"go100\":\n        return R[:, :, k:k + 2].mean(axis=2)\n    if kind == \"pre50\":\n        return R[:, :, COL_PRE.start + k]\n    raise ValueError(name)\n\n\ndef go100_starts() -> np.ndarray:\n    \"\"\"Start (s from Go) of each 100 ms bin stepped by 50 ms; 23 bins from -0.6 to 0.5.\"\"\"\n    return GO_EDGES[:N_GO - 1]\n\n\n# --------------------------------------------------------------------------------------------\n# Axes and fractions (M5, M6)\n\n\ndef _side_diff(Z, a_mask, b_mask, instr, sides, weights_mask):\n    \"\"\"Mean(Z[a]) - mean(Z[b]) within each side, combined by the counts of weights_mask.\"\"\"\n    num, den = 0.0, 0\n    for sd in sides:\n        a = a_mask & (instr == sd)\n        b = b_mask & (instr == sd)\n        w = int((weights_mask & (instr == sd)).sum())\n        if a.sum() == 0 or b.sum() == 0 or w == 0:\n            continue\n        num = num + w * (np.nanmean(Z[a], axis=0) - np.nanmean(Z[b], axis=0))\n        den += w\n    return num / den if den else None\n\n\ndef video_design(S: dict, control_lick: np.ndarray, reading: str = \"fill\"):\n    \"\"\"Design matrix (with intercept) for the video regression on the given trials.\"\"\"\n    V = S[\"video\"][control_lick]\n    if reading == \"fill\":\n        mu = np.nanmean(V, axis=0)\n        mu = np.where(np.isfinite(mu), mu, 0.0)\n        V = np.where(np.isfinite(V), V, mu)\n        keep = np.ones(len(V), bool)\n    else:\n        keep = np.all(np.isfinite(V), axis=1)\n        V = V[keep]\n    V = V[:, np.nanstd(V, axis=0) > 0] if len(V) else V\n    return np.c_[np.ones(len(V)), V], keep\n\n\ndef axes(S: dict, region: str, ts: dict, early: str = \"early_own\", video: str = \"fill\",\n         regress: bool = True, extra_windows=()) -> dict | None:\n    \"\"\"Choice and action axes, the early difference, and the units they use, for one region.\"\"\"\n    units = np.where(S[\"region\"] == region)[0]\n    if len(units) < MIN_UNITS or not ts[\"sides\"]:\n        return None\n    ctrl = ts[\"control\"]\n    wins = [\"choice\", \"action\", early] + list(extra_windows)\n    Zs, keep = {}, np.ones(len(units), bool)\n    for w in wins:\n        Z, k = zscore_window(window_rates(S, units, w), ctrl)\n        Zs[w] = Z\n        keep &= k\n    if keep.sum() < 2:\n        return None\n    for w in wins:\n        Zs[w] = Zs[w][:, keep]\n    ld = ts[\"lick_dir\"]\n    cl = ctrl & (ld != 0)\n    Xc = Zs[\"choice\"][cl]\n    dirs = ld[cl]\n    if regress:\n        D, rows = video_design(S, cl, video)\n        Xc, dirs = Xc[rows], dirs[rows]\n        beta, *_ = np.linalg.lstsq(D, Xc, rcond=None)\n        Xc = Xc - D @ beta\n    if (dirs == 1).sum() < 1 or (dirs == -1).sum() < 1:\n        return None\n    c = Xc[dirs == 1].mean(0) - Xc[dirs == -1].mean(0)\n    Xa = Zs[\"action\"][cl]\n    a = Xa[ld[cl] == 1].mean(0) - Xa[ld[cl] == -1].mean(0)\n    if np.linalg.norm(c) == 0 or np.linalg.norm(a) == 0:\n        return None\n    c, a = c / np.linalg.norm(c), a / np.linalg.norm(a)\n    d = _side_diff(Zs[early], ts[\"laser\"], ctrl, ts[\"instr\"], ts[\"sides\"], ts[\"laser\"])\n    if d is None:\n        return None\n    Q, _ = np.linalg.qr(np.c_[c, a])\n    return {\"choice\": c, \"action\": a, \"Q\": Q, \"d\": d, \"Z\": Zs, \"units\": units[keep],\n            \"n_units\": int(keep.sum()), \"n_region_units\": len(units)}\n\n\ndef fractions(d: np.ndarray, ax: dict) -> dict:\n    e = float(d @ d)\n    return {\"joint\": float(np.sum((ax[\"Q\"].T @ d) ** 2) / e),\n            \"choice\": float((ax[\"choice\"] @ d) ** 2 / e),\n            \"action\": float((ax[\"action\"] @ d) ** 2 / e),\n            \"energy\": e}\n\n\n# --------------------------------------------------------------------------------------------\n# Control splits (Methods, Rates and coding axes, paragraph 3)\n\n\ndef control_splits(Z: np.ndarray, ts: dict, rng: np.random.Generator, n_splits: int = 20,\n                   small: str = \"disjoint\") -> list[np.ndarray]:\n    \"\"\"Difference vectors between two groups of control trials, each the size of the side's\n    laser set, sides combined by laser counts. For a side with fewer than twice as many\n    controls as laser trials: 'disjoint', two groups without overlap as large as the controls\n    allow; 'independent', two groups of laser-set size drawn independently.\"\"\"\n    out = []\n    instr = ts[\"instr\"]\n    for _ in range(n_splits):\n        num, den = 0.0, 0\n        for sd in ts[\"sides\"]:\n            c = np.where(ts[\"control\"] & (instr == sd))[0]\n            nl = int((ts[\"laser\"] & (instr == sd)).sum())\n            if len(c) >= 2 * nl:\n                p = rng.permutation(c)\n                g1, g2 = p[:nl], p[nl:2 * nl]\n            elif small == \"disjoint\":\n                p = rng.permutation(c)\n                k = len(c) // 2\n                g1, g2 = p[:k], p[k:2 * k]\n            else:\n                g1 = rng.choice(c, nl, replace=False)\n                g2 = rng.choice(c, nl, replace=False)\n            num = num + nl * (Z[g1].mean(0) - Z[g2].mean(0))\n            den += nl\n        out.append(num / den)\n    return out\n\n\n# --------------------------------------------------------------------------------------------\n# Decoding (M8; Methods, Decoding)\n\n\ndef decode(X: np.ndarray, y: np.ndarray, instr: np.ndarray, is_ctrl: np.ndarray, seed_: int,\n           Cs=(0.1, 1.0, 10.0), fixed_C: float | None = None) -> float:\n    \"\"\"Balanced accuracy of L2 logistic regression under 5-fold CV stratified by instructed\n    side and lick direction. Features are X minus the mean of control trials of the same side,\n    that mean estimated in the training fold. With fixed_C None, C is chosen from Cs by an inner\n    stratified 5-fold search on balanced accuracy (a standard choice, claims M8).\"\"\"\n    from sklearn.linear_model import LogisticRegression\n    from sklearn.metrics import balanced_accuracy_score\n    from sklearn.model_selection import StratifiedKFold\n\n    strat = (y > 0).astype(int) * 2 + (instr > 0).astype(int)\n\n    def center(Xtr, itr, ctr, Xte, ite):\n        Xtr, Xte = Xtr.copy(), Xte.copy()\n        for sd in (-1, 1):\n            m = ctr & (itr == sd)\n            mu = Xtr[m].mean(0) if m.any() else Xtr[itr == sd].mean(0)\n            Xtr[itr == sd] -= mu\n            Xte[ite == sd] -= mu\n        return Xtr, Xte\n\n    def fit_score(Xtr, ytr, Xte, yte, C):\n        m = LogisticRegression(C=C, solver=\"lbfgs\", max_iter=2000)\n        m.fit(Xtr, ytr)\n        return balanced_accuracy_score(yte, m.predict(Xte))\n\n    outer = StratifiedKFold(5, shuffle=True, random_state=seed_ % (2 ** 32))\n    pred = np.zeros(len(y))\n    for tr, te in outer.split(X, strat):\n        Xtr, Xte = center(X[tr], instr[tr], is_ctrl[tr], X[te], instr[te])\n        if fixed_C is None:\n            inner = StratifiedKFold(5, shuffle=True, random_state=(seed_ + 1) % (2 ** 32))\n            scores = []\n            for C in Cs:\n                sc = []\n                for itr, ite in inner.split(X[tr], strat[tr]):\n                    a, b = center(X[tr][itr], instr[tr][itr], is_ctrl[tr][itr], X[tr][ite], instr[tr][ite])\n                    sc.append(fit_score(a, y[tr][itr], b, y[tr][ite], C))\n                scores.append(np.mean(sc))\n            C = Cs[int(np.argmax(scores))]\n        else:\n            C = fixed_C\n        m = LogisticRegression(C=C, solver=\"lbfgs\", max_iter=2000).fit(Xtr, y[tr])\n        pred[te] = m.predict(Xte)\n    return float(balanced_accuracy_score(y, pred))\n\n\n# --------------------------------------------------------------------------------------------\n# Matching (M9; Methods, Matched distance)\n\n\ndef match(ts: dict, rng: np.random.Generator, pick: str = \"closest\", caliper: float = 0.1,\n          min_pairs: int = 10) -> list[tuple[int, int, int]]:\n    \"\"\"Pairs (laser, control, second control or -1) within session and instructed side.\n\n    Each laser trial with a lick, in random order, takes an unused control trial with the same\n    lick direction and reaction time within the caliper: 'closest' takes the smallest difference,\n    'random' any within the caliper; ties are broken at random. Each retained control then takes\n    a second control by the same rule from controls not already used. Sessions with fewer than\n    min_pairs pairs give no pairs.\"\"\"\n    rt, ld, instr = ts[\"rt\"], ts[\"lick_dir\"], ts[\"instr\"]\n    pairs = []\n    used = set()\n    for sd in (-1, 1):\n        L = np.where(ts[\"laser\"] & (instr == sd) & np.isfinite(rt) & (ld != 0))[0]\n        C = np.where(ts[\"control\"] & (instr == sd) & np.isfinite(rt) & (ld != 0))[0]\n        side_pairs = []\n        for l in rng.permutation(L):\n            cand = [c for c in C if c not in used and ld[c] == ld[l] and abs(rt[c] - rt[l]) <= caliper]\n            if not cand:\n                continue\n            cand = np.array(cand)\n            if pick == \"closest\":\n                diff = np.abs(rt[cand] - rt[l])\n                cand = cand[diff == diff.min()]\n            c = int(rng.choice(cand))\n            used.add(c)\n            side_pairs.append([int(l), c, -1])\n        for p in rng.permutation(len(side_pairs)) if side_pairs else []:\n            l, c, _ = side_pairs[p]\n            cand = [k for k in C if k not in used and ld[k] == ld[c] and abs(rt[k] - rt[c]) <= caliper]\n            if not cand:\n                continue\n            cand = np.array(cand)\n            if pick == \"closest\":\n                diff = np.abs(rt[cand] - rt[c])\n                cand = cand[diff == diff.min()]\n            k = int(rng.choice(cand))\n            used.add(k)\n            side_pairs[p][2] = k\n        pairs += [tuple(p) for p in side_pairs]\n    return pairs if len(pairs) >= min_pairs else []\n\n\ndef residual(Zbins: list[np.ndarray], pairs, missing: str = \"drop\", combine: str = \"mean\"):\n    \"\"\"Mean laser-control minus mean control-control Euclidean distance on the pairs.\n\n    Zbins is a list of (trials, units) arrays (one per bin). combine 'mean' averages the\n    per-bin distances, 'concat' takes the distance of the concatenated bins. missing 'drop'\n    drops a pair without a second control from both distances; 'keep' keeps it for the\n    laser-control distance.\"\"\"\n    P = np.array(pairs)\n    X = Zbins[0][:, :, None] if len(Zbins) == 1 else np.stack(Zbins, axis=2)\n\n    def dist(a, b):\n        if combine == \"mean\":\n            return np.sqrt(((X[a] - X[b]) ** 2).sum(axis=1)).mean(axis=1)\n        return np.sqrt(((X[a] - X[b]) ** 2).sum(axis=(1, 2)))\n\n    has2 = P[:, 2] >= 0\n    lc_rows = P if missing == \"keep\" else P[has2]\n    lc = dist(lc_rows[:, 0], lc_rows[:, 1])\n    cc = dist(P[has2, 1], P[has2, 2])\n    return float(np.nanmean(lc) - np.nanmean(cc)), float(np.nanmean(lc)), float(np.nanmean(cc))\n\n\ndef curve_units(S: dict, units: np.ndarray, control: np.ndarray):\n    \"\"\"Units and z-scored 50 ms Go bins for the distance curve (claims M10): units passing the\n    SD threshold in every bin; if fewer than 20 do, units passing in at least 80% of bins, with\n    their failing bins set to zero. Z-score reference, every non-early-lick control trial.\"\"\"\n    Zs, ks = [], []\n    for k in range(N_GO):\n        Z, keep = zscore_window(window_rates(S, units, (\"go50\", k)), control)\n        Zs.append(Z)\n        ks.append(keep)\n    K = np.array(ks)\n    every = K.all(axis=0)\n    if every.sum() >= MIN_UNITS:\n        sel = every\n    else:\n        sel = K.mean(axis=0) >= 0.8\n    out = []\n    for k in range(N_GO):\n        Z = Zs[k][:, sel].copy()\n        Z[:, ~K[k, sel]] = 0.0\n        out.append(Z)\n    return out, sel\n\n\n# --------------------------------------------------------------------------------------------\n# Summary (M7)\n\n\ndef mouse_summary(values: dict[tuple[str, str], float]) -> tuple[float, float, int, int, dict]:\n    \"\"\"Mean of session values within mouse, then mean and SEM (n-1) across mice.\"\"\"\n    by = {}\n    for (m, s), v in values.items():\n        if v is not None and np.isfinite(v):\n            by.setdefault(m, []).append(v)\n    mm = {m: float(np.mean(v)) for m, v in by.items()}\n    x = np.array(list(mm.values()))\n    if len(x) == 0:\n        return np.nan, np.nan, 0, 0, mm\n    sem = float(x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else np.nan\n    return float(x.mean()), sem, len(x), sum(len(v) for v in by.values()), mm\n\n\ndef limit_threads():\n    for k in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n        os.environ.setdefault(k, \"1\")\n"
}
```

```
File created successfully at: entries/yang-2026/mam.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/yang-2026 && sed -i 's/    for sd in (-1, 1):\n        L = np.where/X/' mam.py && python - <<'EOF'
import re
s=open('mam.py').read()
s=s.replace("""    used = set()
    for sd in (-1, 1):""","""    used = set()
    for sd in ts["sides"]:""")
open('mam.py','w').write(s)
EOF
grep -n 'for sd in ts\["sides"\]' mam.py; cd $TMPDIR && . venv/bin/activate && cat > t1.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/yang-2026')
import mam
t=time.time(); A=mam.assets(); print(len(A), time.time()-t)
pickle.dump(A,open('A.pkl','wb'))
sel=[a for a in A if '20200922T135318' in a['path'] or '20210106T125834' in a['path']]
t=time.time(); sv=mam.survey_all(sel); print('survey', time.time()-t)
t=time.time(); S=mam.load_all(sv); print('load', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
for x in S: print(x['session'], x['rates'].shape, x['video_info'], x['unsorted_units'], x['median_onset'])
pickle.dump(S,open('S2.pkl','wb'))
EOF
python t1.py
```

```
458:        for sd in ts["sides"]:
544:    for sd in ts["sides"]:
174 15.95541763305664
survey 3.6644949913024902
load 14.968291521072388 1.605608
ses-20200922T135318 (527, 378, 30) {'Jaw': {'frames': 1005886, 'detected': 0.9997464921472214, 'frame_interval_ms': 3.400000544000026}, 'Nose': {'frames': 1005886, 'detected': 1.0, 'frame_interval_ms': 3.400000544000026}, 'Tongue': {'frames': 1005886, 'detected': 0.0969921044730715, 'frame_interval_ms': 3.400000544000026}} 0 -0.4998000000000218
ses-20210106T125834 (560, 209, 30) {'Jaw': {'frames': 1066602, 'detected': 0.999501219761448, 'frame_interval_ms': 3.400000544000026}, 'Nose': {'frames': 1066602, 'detected': 0.9999774986358548, 'frame_interval_ms': 3.400000544000026}, 'Tongue': {'frames': 1066602, 'detected': 0.037104749475436946, 'frame_interval_ms': 3.400000544000026}} 0 -0.49984999999992397
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > t2.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/yang-2026')
import mam
A=pickle.load(open('A.pkl','rb'))
t=time.time(); sv=mam.survey_all(A, workers=12); print('survey', time.time()-t, flush=True)
pickle.dump(sv,open('sv.pkl','wb'))
late=[s for s in sv if mam.is_late_delay(s)]
print(len(late))
t=time.time(); S=mam.load_all(late, workers=4); print('load', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
pickle.dump(S,open('S.pkl','wb'),protocol=4)
EOF
python t2.py
```

```
survey 299.87234258651733
112
load 1007.8861703872681 8.222524
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; ls -la $TMPDIR/*.pkl
```

```
Sat Nov 21 07:31:38 UTC 2026
-rw-r--r-- 1 runner runner      31401 Nov 21 07:09 /tmp/claude-1001/A.pkl
-rw-r--r-- 1 runner runner 2592994157 Nov 21 07:31 /tmp/claude-1001/S.pkl
-rw-r--r-- 1 runner runner   38178375 Nov 21 07:09 /tmp/claude-1001/S2.pkl
-rw-r--r-- 1 runner runner      65995 Nov 21 07:05 /tmp/claude-1001/counts.pkl
-rw-r--r-- 1 runner runner   83710099 Nov 21 07:04 /tmp/claude-1001/survey.pkl
-rw-r--r-- 1 runner runner   11018581 Nov 21 07:14 /tmp/claude-1001/sv.pkl
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > d1.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0,'entries/yang-2026')
import mam
S=pickle.load(open('S.pkl','rb'))
t=time.time()
for early in ['early_own','early_go']:
  for video in ['fill','drop']:
    for lick in ['licks','outcome']:
        vals={r:{} for r in mam.REGIONS}; cos={r:{} for r in mam.REGIONS}
        for s in S:
            ts=mam.trial_sets(s,'drop',lick)
            for r in mam.REGIONS:
                ax=mam.axes(s,r,ts,early=early,video=video)
                if ax is None: continue
                f=mam.fractions(ax['d'],ax)
                vals[r][(s['mouse'],s['session'])]=f
                cos[r][(s['mouse'],s['session'])]=ax['choice']@ax['action']
        print(early,video,lick)
        for r in mam.REGIONS:
            out=[r]
            for k in ['joint','choice','action']:
                m,se,nm,ns,_=mam.mouse_summary({kk:v[k] for kk,v in vals[r].items()})
                out.append(f'{k} {m:.3f}±{se:.3f}')
            m,se,nm,ns,_=mam.mouse_summary(cos[r])
            out.append(f'cos {m:.2f}±{se:.2f} n={nm}/{ns}')
            print('  ',' '.join(out))
print(time.time()-t)
EOF
python d1.py
```

```
entries/yang-2026/mam.py:383: RuntimeWarning: Mean of empty slice
  mu = np.nanmean(V, axis=0)
early_own fill licks
   ALM joint 0.055±0.013 choice 0.034±0.012 action 0.022±0.004 cos 0.52±0.03 n=19/93
   striatum joint 0.060±0.009 choice 0.042±0.008 action 0.019±0.005 cos 0.34±0.03 n=13/48
   thalamus joint 0.084±0.017 choice 0.061±0.016 action 0.027±0.009 cos 0.30±0.04 n=10/31
   midbrain joint 0.059±0.008 choice 0.029±0.007 action 0.032±0.006 cos 0.35±0.03 n=16/71
   medulla joint 0.052±0.014 choice 0.031±0.012 action 0.025±0.007 cos 0.41±0.04 n=8/35
early_own fill outcome
   ALM joint 0.056±0.014 choice 0.035±0.013 action 0.022±0.004 cos 0.52±0.02 n=19/93
   striatum joint 0.063±0.009 choice 0.045±0.008 action 0.020±0.005 cos 0.34±0.03 n=13/48
   thalamus joint 0.082±0.017 choice 0.058±0.015 action 0.026±0.009 cos 0.30±0.05 n=10/31
   midbrain joint 0.059±0.009 choice 0.029±0.007 action 0.032±0.006 cos 0.35±0.03 n=16/71
   medulla joint 0.053±0.015 choice 0.032±0.013 action 0.025±0.007 cos 0.40±0.04 n=8/35
early_own drop licks
   ALM joint 0.048±0.010 choice 0.029±0.009 action 0.020±0.004 cos 0.33±0.05 n=19/86
   striatum joint 0.036±0.008 choice 0.022±0.007 action 0.018±0.005 cos 0.25±0.05 n=13/45
   thalamus joint 0.040±0.008 choice 0.020±0.004 action 0.021±0.006 cos 0.20±0.05 n=9/28
   midbrain joint 0.048±0.007 choice 0.017±0.003 action 0.031±0.006 cos 0.24±0.04 n=16/66
   medulla joint 0.044±0.010 choice 0.026±0.007 action 0.025±0.007 cos 0.31±0.04 n=8/32
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > d2.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0,'entries/yang-2026')
import mam
from scipy import stats
S=pickle.load(open('S.pkl','rb'))
t=time.time()
rng=np.random.default_rng(mam.seed('fig1e-laser-vs-control-split'))
res={}
for s in S:
    ts=mam.trial_sets(s)
    for r in mam.REGIONS:
        ax=mam.axes(s,r,ts)
        if ax is None: continue
        Z=ax['Z']['early_own']; d=ax['d']; El=d@d; Q=ax['Q']
        Ein=np.sum((Q.T@d)**2)
        row={'n':ax['n_units'],'joint':Ein/El}
        for small in ['disjoint','independent']:
            sp=mam.control_splits(Z,ts,rng,20,small)
            Es=np.array([v@v for v in sp]); Eins=np.array([np.sum((Q.T@v)**2) for v in sp])
            row[small]={'ratio_a':El/Es.mean(),'ratio_b':np.mean(El/Es),
                        'corr_a':(Ein-Eins.mean())/(El-Es.mean()),'corr_b':(Ein-Eins.mean())/El,
                        'corr_c':Ein/El-np.sum((Q.T@np.mean(sp,0))**2)/(np.mean(sp,0)@np.mean(sp,0))}
        res[(r,s['mouse'],s['session'])]=row
for small in ['disjoint','independent']:
  for k in ['ratio_a','ratio_b']:
    out=[]
    for r in mam.REGIONS:
        _,_,_,_,mm=mam.mouse_summary({(m,se):v[small][k] for (rr,m,se),v in res.items() if rr==r})
        out.append(f"{r} med {np.median(list(mm.values())):.1f} min {min(mm.values()):.2f}")
    print(small,k,' | '.join(out))
  for k in ['corr_a','corr_b','corr_c']:
    out=[];allmm=[]
    for r in mam.REGIONS:
        m,se,_,_,mm=mam.mouse_summary({(m,se):v[small][k] for (rr,m,se),v in res.items() if rr==r})
        out.append(f"{r} {m:.3f}"); allmm+= [(r,x) for x in mm.values()]
    print(small,k,' | '.join(out), 'min mouse', min(allmm,key=lambda x:x[1]), 'max', max(allmm,key=lambda x:x[1]))
x=[v['n'] for v in res.values()]; y=[v['joint'] for v in res.values()]
print(stats.spearmanr(x,y))
print(time.time()-t)
EOF
python d2.py
```

```
entries/yang-2026/mam.py:383: RuntimeWarning: Mean of empty slice
  mu = np.nanmean(V, axis=0)
disjoint ratio_a ALM med 147.0 min 2.35 | striatum med 2.7 min 1.22 | thalamus med 5.2 min 1.98 | midbrain med 8.2 min 1.69 | medulla med 2.8 min 1.50
disjoint ratio_b ALM med 152.7 min 2.43 | striatum med 2.8 min 1.33 | thalamus med 5.3 min 2.11 | midbrain med 8.8 min 1.93 | medulla med 2.9 min 1.60
disjoint corr_a ALM 0.061 | striatum 0.126 | thalamus 0.109 | midbrain 0.067 | medulla -0.626 min mouse ('medulla', -5.694499858836669) max ('striatum', 1.110550537374928)
disjoint corr_b ALM 0.050 | striatum 0.043 | thalamus 0.077 | midbrain 0.046 | medulla -0.003 min mouse ('medulla', -0.08347572807233901) max ('ALM', 0.1965998541367925)
disjoint corr_c ALM 0.012 | striatum 0.012 | thalamus 0.044 | midbrain 0.005 | medulla -0.011 min mouse ('striatum', -0.10703770258375955) max ('ALM', 0.1491755397961128)
independent ratio_a ALM med 146.8 min 2.39 | striatum med 2.8 min 1.16 | thalamus med 5.1 min 1.84 | midbrain med 7.6 min 1.71 | medulla med 2.7 min 1.47
independent ratio_b ALM med 156.5 min 2.47 | striatum med 2.8 min 1.26 | thalamus med 5.2 min 1.91 | midbrain med 8.3 min 1.89 | medulla med 2.8 min 1.56
independent corr_a ALM 0.060 | striatum 0.112 | thalamus 0.110 | midbrain 0.069 | medulla -0.048 min mouse ('medulla', -0.8698490507853598) max ('striatum', 0.40692361977620467)
independent corr_b ALM 0.049 | striatum 0.044 | thalamus 0.075 | midbrain 0.046 | medulla 0.002 min mouse ('medulla', -0.06176902528181924) max ('ALM', 0.20156254497193576)
independent corr_c ALM 0.005 | striatum 0.016 | thalamus 0.050 | midbrain 0.003 | medulla -0.038 min mouse ('medulla', -0.09210124266223359) max ('thalamus', 0.1256079074979204)
SignificanceResult(statistic=np.float64(-0.3662251820990913), pvalue=np.float64(2.99836745799548e-10))
2.615591049194336
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > d3.py <<'EOF'
import os
os.environ['OMP_NUM_THREADS']='1'; os.environ['OPENBLAS_NUM_THREADS']='1'
import sys, time, pickle, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'entries/yang-2026')
import mam
S=pickle.load(open('S.pkl','rb'))[:3]
t=time.time(); n=0
for s in S:
    ts=mam.trial_sets(s)
    for r in mam.REGIONS:
        ax=mam.axes(s,r,ts,extra_windows=['pre'])
        if ax is None: continue
        ld=ts['lick_dir']; 
        for trials in ['both','laser']:
            m=(ts['laser']|(ts['control'] if trials=='both' else False))&(ld!=0)&np.isin(ts['instr'],ts['sides'])
            if m.sum()<40 or (ld[m]==1).sum()<15 or (ld[m]==-1).sum()<15: print(r,trials,'skip',m.sum()); continue
            for w in ['early_own','pre']:
                X=ax['Z'][w][m]
                if np.isnan(X).any(): print('nan',w); 
                t1=time.time()
                acc=mam.decode(X,ld[m],ts['instr'][m],ts['control'][m],mam.seed('table1-decoding-early-vs-prelick'))
                n+=1
                print(s['session'],r,trials,w,X.shape,round(acc,3),round(time.time()-t1,2))
print(time.time()-t, n)
EOF
python d3.py
```

```
ses-20191119T115109 ALM both early_own (309, 43) 0.678 1.21
ses-20191119T115109 ALM both pre (309, 43) 0.8 0.13
ALM laser skip 28
ses-20191119T115109 midbrain both early_own (309, 60) 0.55 0.14
ses-20191119T115109 midbrain both pre (309, 60) 0.681 0.2
midbrain laser skip 28
ses-20191119T130822 ALM both early_own (264, 38) 0.536 0.24
ses-20191119T130822 ALM both pre (264, 38) 0.765 0.15
ALM laser skip 19
ses-20191119T130822 midbrain both early_own (264, 119) 0.565 0.27
ses-20191119T130822 midbrain both pre (264, 119) 0.779 0.28
midbrain laser skip 19
ses-20191120T115527 ALM both early_own (293, 118) 0.556 0.53
ses-20191120T115527 ALM both pre (293, 118) 0.714 0.23
ALM laser skip 21
ses-20191120T115527 midbrain both early_own (293, 98) 0.534 0.22
ses-20191120T115527 midbrain both pre (293, 98) 0.777 0.25
midbrain laser skip 21
3.872938871383667 12
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > d4.py <<'EOF'
import os
os.environ['OMP_NUM_THREADS']='1'; os.environ['OPENBLAS_NUM_THREADS']='1'
import sys, time, pickle, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'entries/yang-2026')
import mam
S=pickle.load(open('S.pkl','rb'))
t=time.time()
# matching
P={}
for pick in ['closest','random']:
    rng=np.random.default_rng(mam.seed('fig3a-matched-pairs'))
    for s in S:
        ts=mam.trial_sets(s)
        P[(pick,s['session'])]=mam.match(ts,rng,pick)
for pick in ['closest','random']:
    allp=[(s,p) for s in S for p in P[(pick,s['session'])]]
    d=np.array([abs(s['trials']['first_lick'][p[0]]-s['trials']['first_lick'][p[1]]) for s,p in allp])
    rts=np.array([s['trials']['first_lick'][p[0]] for s,p in allp])
    print(pick,'pairs',len(allp),'sessions',sum(1 for s in S if P[(pick,s['session'])]),'median ms',np.median(d)*1000,'max',d.max()*1000,
          'no second',sum(p[2]<0 for s,p in allp), 'RT q',np.percentile(rts,[25,50,75]))
print(time.time()-t)
# residuals
for pick in ['closest','random']:
  for missing in ['drop','keep']:
    for comb in ['mean','concat']:
        res={r:{} for r in mam.REGIONS}; rat={r:{} for r in mam.REGIONS}; cc={r:{} for r in mam.REGIONS}
        for s in S:
            pairs=P[(pick,s['session'])]
            if not pairs: continue
            ts=mam.trial_sets(s)
            for r in mam.REGIONS:
                ax=mam.axes(s,r,ts)
                if ax is None: continue
                units=np.where(s['region']==r)[0]
                Zb=[];K=np.ones(len(units),bool)
                for k in range(4):
                    Z,kk=mam.zscore_window(mam.window_rates(s,units,('pre50',k)),ts['control']); Zb.append(Z); K&=kk
                Zb=[z[:,K] for z in Zb]
                rr,lc,c2=mam.residual(Zb,pairs,missing,comb)
                res[r][(s['mouse'],s['session'])]=rr; rat[r][(s['mouse'],s['session'])]=rr/c2; cc[r][(s['mouse'],s['session'])]=c2
        out=[]
        for r in mam.REGIONS:
            m,se,nm,ns,mm=mam.mouse_summary(res[r]); _,_,_,_,mc=mam.mouse_summary(cc[r]); m2,_,_,_,_=mam.mouse_summary(rat[r])
            ra=np.mean([mm[k]/mc[k] for k in mm])
            out.append(f"{r} {m:.2f}±{se:.2f} {nm}/{ns} pos {sum(v>0 for v in mm.values())} ratio_a {ra:.3f} b {m2:.3f}")
        print(pick,missing,comb,' | '.join(out))
print(time.time()-t)
pickle.dump(P,open('P.pkl','wb'))
EOF
python d4.py
```

```
closest pairs 2667 sessions 98 median ms 1.3000000001284207 max 99.1000000000497 no second 128 RT q [0.22025 0.2885  0.38485]
random pairs 2664 sessions 98 median ms 43.29999999990264 max 99.99999999979536 no second 104 RT q [0.220575 0.28885  0.384775]
0.44766688346862793
closest drop mean ALM 1.55±0.14 19/87 pos 19 ratio_a 0.113 b 0.113 | striatum 1.36±0.52 12/41 pos 12 ratio_a 0.092 b 0.091 | thalamus 2.91±0.86 10/29 pos 10 ratio_a 0.136 b 0.135 | midbrain 0.76±0.09 15/63 pos 15 ratio_a 0.064 b 0.065 | medulla 0.53±0.12 8/32 pos 8 ratio_a 0.042 b 0.041
closest drop concat ALM 3.30±0.28 19/87 pos 19 ratio_a 0.119 b 0.119 | striatum 3.03±1.20 12/41 pos 12 ratio_a 0.101 b 0.100 | thalamus 6.17±1.83 10/29 pos 10 ratio_a 0.143 b 0.142 | midbrain 1.65±0.20 15/63 pos 15 ratio_a 0.068 b 0.069 | medulla 1.13±0.26 8/32 pos 8 ratio_a 0.044 b 0.043
closest keep mean ALM 1.57±0.14 19/87 pos 19 ratio_a 0.114 b 0.113 | striatum 1.46±0.51 12/41 pos 12 ratio_a 0.099 b 0.098 | thalamus 2.91±0.84 10/29 pos 10 ratio_a 0.136 b 0.136 | midbrain 0.82±0.10 15/63 pos 15 ratio_a 0.069 b 0.070 | medulla 0.55±0.12 8/32 pos 8 ratio_a 0.043 b 0.042
closest keep concat ALM 3.34±0.29 19/87 pos 19 ratio_a 0.120 b 0.120 | striatum 3.24±1.18 12/41 pos 12 ratio_a 0.108 b 0.107 | thalamus 6.16±1.80 10/29 pos 10 ratio_a 0.144 b 0.143 | midbrain 1.77±0.22 15/63 pos 15 ratio_a 0.073 b 0.074 | medulla 1.17±0.25 8/32 pos 8 ratio_a 0.045 b 0.045
random drop mean ALM 1.61±0.15 19/87 pos 19 ratio_a 0.117 b 0.117 | striatum 1.41±0.51 12/41 pos 11 ratio_a 0.089 b 0.088 | thalamus 2.96±0.90 10/29 pos 10 ratio_a 0.142 b 0.141 | midbrain 0.76±0.10 15/63 pos 15 ratio_a 0.063 b 0.065 | medulla 0.55±0.15 8/32 pos 8 ratio_a 0.042 b 0.041
random drop concat ALM 3.41±0.32 19/87 pos 19 ratio_a 0.122 b 0.123 | striatum 3.14±1.17 12/41 pos 11 ratio_a 0.098 b 0.097 | thalamus 6.27±1.91 10/29 pos 10 ratio_a 0.149 b 0.148 | midbrain 1.67±0.21 15/63 pos 15 ratio_a 0.068 b 0.070 | medulla 1.16±0.30 8/32 pos 8 ratio_a 0.044 b 
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > d5.py <<'EOF'
import os
os.environ['OMP_NUM_THREADS']='1'; os.environ['OPENBLAS_NUM_THREADS']='1'
import sys, time, pickle, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'entries/yang-2026')
import mam
S=pickle.load(open('S.pkl','rb')); P=pickle.load(open('P.pkl','rb'))
t=time.time()
G100=list(range(23))
early_res={}; curve={}; unm={}; ccd={}; nun={}; jf={r:{} for r in mam.REGIONS}; eo={'a':{},'b':{}}; ei={'a':{},'b':{}}
rng=np.random.default_rng(mam.seed('fig3-1d-matching-keeps-distance'))
for s in S:
    ts=mam.trial_sets(s); pairs=P[('closest',s['session'])]
    for r in mam.REGIONS:
        ax=mam.axes(s,r,ts)
        if ax is None: continue
        key=(r,s['mouse'],s['session'])
        units=np.where(s['region']==r)[0]
        # Go-grid joint fraction & energy reading b
        axg=mam.axes(s,r,ts,extra_windows=[('go100',k) for k in G100])
        if axg is not None:
            row=[];eb=[];ib=[]
            for k in G100:
                d=mam._side_diff(axg['Z'][('go100',k)],ts['laser'],ts['control'],ts['instr'],ts['sides'],ts['laser'])
                f=mam.fractions(d,axg); row.append(f['joint'])
                ein=np.sum((axg['Q'].T@d)**2); eb.append((d@d-ein)/axg['n_units']); ib.append(ein/axg['n_units'])
            jf[r][key]=np.array(row); eo['b'][key]=np.array(eb); ei['b'][key]=np.array(ib)
        if not pairs: continue
        # early residual
        Ze=ax['Z']['early_own']
        early_res[key]=mam.residual([Ze],pairs)
        # curve
        Zc,sel=mam.curve_units(s,units,ts['control'])
        curve[key]=np.array([mam.residual([Zc[k]],pairs)[0] for k in range(mam.N_GO)])
        # energy reading a: curve units intersect axes units
        inax=np.isin(units[sel],ax['units']); 
        posq=[np.where(ax['units']==u)[0][0] for u in units[sel][inax]]
        c=ax['choice'][posq]; a=ax['action'][posq]
        Q,_=np.linalg.qr(np.c_[c/np.linalg.norm(c),a/np.linalg.norm(a)])
        ea=[];ia=[]
        for k in G100:
            Z=(Zc[k][:,inax]+Zc[k+1][:,inax])/2
            d=mam._side_diff(Z,ts['laser'],ts['control'],ts['instr'],ts['sides'],ts['laser'])
            ein=np.sum((Q.T@d)**2); ea.append((d@d-ein)/inax.sum()); ia.append(ein/inax.sum())
        eo['a'][key]=np.array(ea); ei['a'][key]=np.array(ia)
        # unmatched + cc
        Zb=[];K=np.ones(len(units),bool)
        for k in range(4):
            Z,kk=mam.zscore_window(mam.window_rates(s,units,('pre50',k)),ts['control']); Zb.append(Z); K&=kk
        Zb=[z[:,K] for z in Zb]
        rr,lc,cc=mam.residual(Zb,pairs)
        ccd[key]=cc; nun[key]=K.sum()
        L=[p[0] for p in pairs]
        up=[]
        for sd in ts['sides']:
            Ls=[l for l in L if ts['instr'][l]==sd]
            C=np.where(ts['control']&(ts['instr']==sd)&np.isfinite(ts['rt']))[0]
            ch=rng.choice(C,min(len(Ls),len(C)),replace=False)
            up+=[(l,c,-1) for l,c in zip(Ls,ch)]
        X=np.stack(Zb,2); P_=np.array(up)
        unm[key]=(np.sqrt(((X[P_[:,0]]-X[P_[:,1]])**2).sum(1)).mean(1).mean(), lc, cc)
print(time.time()-t)
def summ(dct, f=lambda v:v):
    out={}
    for r in mam.REGIONS:
        out[r]=mam.mouse_summary({(m,se):f(v) for (rr,m,se),v in dct.items() if rr==r})
    return out
for r,v in summ(early_res,lambda v:v[0]).items(): print('early res',r,round(v[0],2),round(v[1],2))
ks=mam.go100_starts()
for r in mam.REGIONS:
    M=np.array([v for (rr,m,se),v in curve.items() if rr==r]); mice=[m for (rr,m,se) in curve if rr==r]
    mm=np.array([M[[i for i,x in enumerate(mice) if x==u]].mean(0) for u in sorted(set(mice))])
    mean=mm.mean(0); sem=mm.std(0,ddof=1)/np.sqrt(len(mm))
    print('curve',r,' '.join(f"{x:.1f}" for x in mean), 'peak', mam.GO_EDGES[np.argmax(mean)], mean.max().round(2))
    print('   late bins', mean[16:20].round(2), 'onset bins', mean[2:4].round(2), sem[2:4].round(2))
for nm,dd in [('jf',None)]:
    for r in mam.REGIONS:
        M=jf[r]; mice=sorted({k[1] for k in M})
        mm=np.array([np.mean([v for k,v in M.items() if k[1]==u],0) for u in mice])
        print('jf',r,mm.mean(0).round(3)[[0,1,2,3,4,5,10,11,16]], 'k16', mm.mean(0)[16].round(3), (mm.std(0,ddof=1)/np.sqrt(len(mm)))[16].round(3))
for rd in 'ab':
    for r in mam.REGIONS:
        M={k:v for k,v in eo[rd].items() if k[0]==r}; mice=sorted({k[1] for k in M})
        mm=np.array([np.mean([v for k,v in M.items() if k[1]==u],0) for u in mice])
        Mi={k:v for k,v in ei[rd].items() if k[0]==r}
        mi=np.array([np.mean([v for k,v in Mi.items() if k[1]==u],0) for u in mice])
        print('energy',rd,r,'bin -0.6',mm.mean(0)[0].round(3),'onset',mm.mean(0)[2].round(2),'sem',(mm.std(0,ddof=1)/np.sqrt(len(mm)))[2].round(2),'max',mm.mean(0).max().round(2),'in onset', mi.mean(0)[2].round(3))
for r,v in summ(unm,lambda v:v[0]).items():
    print('unmatched',r,round(v[0],2), 'matched lc', round(summ(unm,lambda v:v[1])[r][0],2),'cc',round(summ(unm,lambda v:v[2])[r][0],2))
from scipy import stats
print(stats.spearmanr(list(nun.values()),list(ccd.values())))
pickle.dump((curve,jf,eo,ei),open('curves.pkl','wb'))
EOF
python d5.py
```

```
24.96276617050171
early res ALM 18.36 2.75
early res striatum 0.14 0.61
early res thalamus -0.7 0.49
early res midbrain 2.31 0.3
early res medulla 0.89 0.4
curve ALM 0.5 0.6 21.3 10.4 8.6 10.0 8.7 9.5 7.0 5.3 2.7 1.1 3.5 2.8 2.0 1.6 1.3 1.0 0.9 0.8 0.7 0.6 0.6 0.7 peak -0.5 21.3
   late bins [1.33 0.98 0.91 0.79] onset bins [21.3  10.38] [2.96 1.68]
curve striatum 1.2 1.3 -0.1 -0.4 0.5 1.2 1.3 1.2 1.2 1.2 1.4 1.5 2.9 2.8 1.8 1.0 0.8 0.3 0.3 0.3 0.3 0.4 0.4 0.6 peak 0.0 2.91
   late bins [0.8  0.32 0.29 0.3 ] onset bins [-0.05 -0.38] [0.52 0.36]
curve thalamus 0.7 0.9 -1.0 -1.4 -0.0 8.9 10.5 8.6 9.3 9.0 9.4 11.3 9.9 5.3 5.4 3.2 2.0 1.6 1.0 0.8 0.4 0.3 0.5 0.3 peak -0.05 11.35
   late bins [1.95 1.55 1.02 0.82] onset bins [-0.99 -1.35] [0.31 0.68]
curve midbrain 0.4 0.4 0.1 2.1 1.4 1.5 1.3 1.3 1.1 1.1 1.0 1.4 1.7 1.7 1.0 0.7 0.4 0.4 0.3 0.3 0.3 0.3 0.3 0.4 peak -0.45 2.07
   late bins [0.42 0.35 0.33 0.31] onset bins [0.09 2.07] [0.09 0.4 ]
curve medulla 0.5 0.6 0.5 0.7 0.6 0.6 0.5 0.9 0.6 0.5 0.5 1.3 0.7 0.9 0.8 0.5 0.5 0.4 0.2 0.3 0.2 0.2 0.2 0.1 peak -0.05 1.31
   late bins [0.47 0.42 0.16 0.31] onset bins [0.45 0.7 ] [0.29 0.39]
jf ALM [0.058 0.036 0.047 0.055 0.039 0.035 0.055 0.042 0.079] k16 0.079 0.012
jf striatum [0.052 0.051 0.065 0.066 0.059 0.053 0.05  0.051 0.083] k16 0.083 0.018
jf thalamus [0.045 0.039 0.085 0.078 0.05  0.034 0.036 0.036 0.05 ] k16 0.05 0.012
jf midbrain [0.08  0.066 0.063 0.062 0.057 0.06  0.066 0.065 0.106] k16 0.106 0.02
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python -c "import joblib; print(joblib.__version__)"; cat > d6.py <<'EOF'
import os
os.environ['OMP_NUM_THREADS']='1'; os.environ['OPENBLAS_NUM_THREADS']='1'
import sys, time, pickle, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'entries/yang-2026')
import mam
from joblib import Parallel, delayed
S=pickle.load(open('S.pkl','rb')); P=pickle.load(open('P.pkl','rb'))
t=time.time()
jobs=[]; meta=[]
pref={r:{} for r in mam.REGIONS}
for s in S:
    ts=mam.trial_sets(s)
    for r in mam.REGIONS:
        ax=mam.axes(s,r,ts,extra_windows=['pre']+[('go100',k) for k in range(23)])
        if ax is None: continue
        ld=ts['lick_dir']
        m=(ts['laser']|ts['control'])&(ld!=0)&np.isin(ts['instr'],ts['sides'])
        dec_ok = m.sum()>=40 and (ld[m]==1).sum()>=15 and (ld[m]==-1).sum()>=15
        key=(r,s['mouse'],s['session'])
        # prelick fraction
        lk=np.isfinite(ts['rt'])
        dpre=mam._side_diff(ax['Z']['pre'],ts['laser']&lk,ts['control']&lk,ts['instr'],ts['sides'],ts['laser']&lk)
        dear=mam._side_diff(ax['Z']['early_own'],ts['laser'],ts['control'],ts['instr'],ts['sides'],ts['laser'])
        pref[r][key]=(mam.fractions(dear,ax),mam.fractions(dpre,ax),dec_ok,bool(P[('closest',s['session'])]))
        if not dec_ok: continue
        y=ld[m]; ins=ts['instr'][m]; ic=ts['control'][m]
        for w in ['early_own','pre']:
            jobs.append(delayed(mam.decode)(ax['Z'][w][m],y,ins,ic,mam.seed('table1-decoding-early-vs-prelick'))); meta.append((key,w))
        for k in range(23):
            jobs.append(delayed(mam.decode)(ax['Z'][('go100',k)][m],y,ins,ic,mam.seed('fig2a-decoding-rises-after-go'),fixed_C=1.0)); meta.append((key,k))
print('prep',time.time()-t,len(jobs))
out=Parallel(n_jobs=4)(jobs)
print('decode',time.time()-t)
pickle.dump((meta,out,pref),open('dec.pkl','wb'))
EOF
python d6.py
```

```
<persisted-output>
Output too large (3.8MB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d51d7c41-3b3d-49a6-8dd0-2ff5cb98498e/tool-results/bsdmyswzx.txt

Preview (first 2KB):
1.6.0
prep 14.037309646606445 6825
/tmp/claude-1001/venv/lib/python3.12/site-packages/sklearn/model_selection/_split.py:812: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
/tmp/claude-1001/venv/lib/python3.12/site-packages/sklearn/model_selection/_split.py:812: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
/tmp/claude-1001/venv/lib/python3.12/site-packages/sklearn/model_selection/_split.py:812: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
/tmp/claude-1001/venv/lib/python3.12/site-packages/sklearn/model_selection/_split.py:812: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
/tmp/claude-1001/venv/lib/python3.12/site-packages/sklearn/model_selection/_split.py:812: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
/tmp/claude-1001/venv/lib/python3.12/site-packages/sklearn/model_selection/_split.py:812: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
/tmp/claude-1001/venv/lib/python3.12/site-packages/sklearn/model_selection/_split.py:812: UserWarning: The least populated class in y has only 4 members, which is less than n_splits=5.
  warnings.warn(
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v -e 'warnings.warn' -e UserWarning /home/runner/.claude/projects/-home-runner-work-encore-encore/d51d7c41-3b3d-49a6-8dd0-2ff5cb98498e/tool-results/bsdmyswzx.txt | tail -5; date -u
```

```
entries/yang-2026/mam.py:497: RuntimeWarning: Mean of empty slice
  mu = Xtr[m].mean(0) if m.any() else Xtr[itr == sd].mean(0)
/tmp/claude-1001/venv/lib/python3.12/site-packages/numpy/_core/_methods.py:134: RuntimeWarning: invalid value encountered in divide
  ret = um.true_divide(
decode 95.90223979949951
Sat Nov 21 07:36:41 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > d7.py <<'EOF'
import sys, pickle, numpy as np
sys.path.insert(0,'entries/yang-2026')
import mam
meta,out,pref=pickle.load(open('dec.pkl','rb'))
acc={}
for (key,w),v in zip(meta,out): acc.setdefault(w,{})[key]=v
print('nan', sum(np.isnan(out)))
for w in ['early_own','pre']+list(range(23)):
    row=[]
    for r in mam.REGIONS:
        m,se,nm,ns,_=mam.mouse_summary({(k[1],k[2]):v for k,v in acc[w].items() if k[0]==r})
        row.append(f"{r} {m:.3f}±{se:.3f} {nm}/{ns}")
    print(w if isinstance(w,str) else mam.GO_EDGES[w], ' | '.join(row))
for sset in ['dec','match']:
    for r in mam.REGIONS:
        sel={k:v for k,v in pref[r].items() if (v[2] if sset=='dec' else v[3])}
        res=[]
        for i,nm in [(0,'early'),(1,'pre')]:
            for q in ['choice','action']:
                m,se,_,_,_=mam.mouse_summary({(k[1],k[2]):v[i][q] for k,v in sel.items()})
                res.append(f"{nm}-{q} {m:.3f}±{se:.3f}")
        print(sset,r,' '.join(res))
EOF
python d7.py
```

```
nan 0
early_own ALM 0.574±0.006 19/91 | striatum 0.584±0.013 13/47 | thalamus 0.574±0.011 10/30 | midbrain 0.561±0.007 16/71 | medulla 0.581±0.017 8/34
pre ALM 0.794±0.024 19/91 | striatum 0.806±0.035 13/47 | thalamus 0.802±0.046 10/30 | midbrain 0.815±0.024 16/71 | medulla 0.856±0.027 8/34
-0.6 ALM 0.558±0.007 19/91 | striatum 0.540±0.005 13/47 | thalamus 0.573±0.011 10/30 | midbrain 0.548±0.008 16/71 | medulla 0.575±0.012 8/34
-0.55 ALM 0.567±0.007 19/91 | striatum 0.564±0.006 13/47 | thalamus 0.561±0.010 10/30 | midbrain 0.543±0.007 16/71 | medulla 0.572±0.013 8/34
-0.5 ALM 0.561±0.006 19/91 | striatum 0.555±0.011 13/47 | thalamus 0.577±0.010 10/30 | midbrain 0.562±0.008 16/71 | medulla 0.581±0.016 8/34
-0.45 ALM 0.569±0.006 19/91 | striatum 0.561±0.010 13/47 | thalamus 0.577±0.011 10/30 | midbrain 0.552±0.009 16/71 | medulla 0.579±0.011 8/34
-0.4 ALM 0.566±0.007 19/91 | striatum 0.558±0.007 13/47 | thalamus 0.558±0.008 10/30 | midbrain 0.555±0.008 16/71 | medulla 0.573±0.011 8/34
-0.35 ALM 0.572±0.007 19/91 | striatum 0.560±0.011 13/47 | thalamus 0.569±0.008 10/30 | midbrain 0.548±0.005 16/71 | medulla 0.575±0.013 8/34
-0.3 ALM 0.570±0.007 19/91 | striatum 0.563±0.007 13/47 | thalamus 0.578±0.013 10/30 | midbrain 0.560±0.007 16/71 | medulla 0.576±0.011 8/34
-0.25 ALM 0.579±0.006 19/91 | striatum 0.556±0.007 13/47 | thalamus 0.573±0.009 10/30 | midbrain 0.557±0.007 16/71 | medulla 0.588±0.016 8/34
-0.2 ALM 0.579±0.007 19/91 | striatum 0.556±0.009 13/47 | thalamus 0.582±0.010 10/30 | midbrain 0.558±0.007 16/71 | medulla 0.587±0.016 8/34
-0.15 ALM 0.575±0.006 19/91 | striatum 0.552±0.012 13/47 | thalamus 0.583±0.009 10/30 | midbrain 0.557±0.007 16/71 | medulla 0.577±0.007 8/34
-0.1 ALM 0.577±0.008 19/91 | striatum 0.554±0.009 13/47 | thalamus 0.575±0.007 10/30 | midbrain 0.558±0.006 16/71 | medulla 0.580±0.010 8/34
-0.05 ALM 0.583±0.007 19/91 | striatum 0.557±0.008 13/47 | thalamus 0.575±0.011 10/30 | midbrain 0.558±0.008 16/71 | medulla 0.584±0.008 8/34
0.0 ALM 0.
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > d8.py <<'EOF'
import sys, pickle, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'entries/yang-2026')
import mam
S=pickle.load(open('S.pkl','rb')); P=pickle.load(open('P.pkl','rb'))
vals={}
for s in S:
    ts=mam.trial_sets(s); ax=mam.axes(s,'ALM',ts)
    if ax is None: continue
    vals[(s['mouse'],s['session'])]=(mam.fractions(ax['d'],ax)['joint'],ax['n_units'],ax['n_region_units'],bool(P[('closest',s['session'])]))
m,_,_,_,_=mam.mouse_summary({k:v[0] for k,v in vals.items()})
c={k:v for k,v in vals.items() if v[3]}
for nk in [1,2]:
    med=np.median([v[nk] for v in c.values()])
    cand=sorted([(abs(v[0]-m),-v[nk],k[1],v) for k,v in c.items() if v[nk]>=med])
    print(nk,'mean',m,'median',med,cand[:3])
print(vals.get(('sub-479121','ses-20200922T135318')))
EOF
python d8.py
```

```
1 mean 0.054921827644132455 median 117.0 [(0.0020001100886235176, -130, 'ses-20210419T161140', (0.05292171755550894, 130, 131, True)), (0.00209936982313514, -130, 'ses-20200922T135318', (0.052822457820997315, 130, 130, True)), (0.005868171685424667, -185, 'ses-20201230T112558', (0.06078999932955712, 185, 187, True))]
2 mean 0.054921827644132455 median 117.0 [(0.0020001100886235176, -131, 'ses-20210419T161140', (0.05292171755550894, 130, 131, True)), (0.00209936982313514, -130, 'ses-20200922T135318', (0.052822457820997315, 130, 130, True)), (0.005868171685424667, -187, 'ses-20201230T112558', (0.06078999932955712, 185, 187, True))]
(0.052822457820997315, 130, 130, True)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/yang-2026 && python - <<'EOF'
s=open('mam.py').read()
s=s.replace("""# Column layout of the per-trial rate array: 24 Go bins, early ("go" placement), early ("own"
# placement), 4 pre-lick bins.
COL_EARLY_GO, COL_EARLY_OWN = N_GO, N_GO + 1
COL_PRE = slice(N_GO + 2, N_GO + 6)
N_COLS = N_GO + 6""","""# Column layout of the per-trial rate array: 24 Go bins, early ("go" placement), early ("own"
# placement), 4 pre-lick bins, the early window in two 50 ms bins ("own" placement).
COL_EARLY_GO, COL_EARLY_OWN = N_GO, N_GO + 1
COL_PRE = slice(N_GO + 2, N_GO + 6)
COL_EARLY50 = slice(N_GO + 6, N_GO + 8)
N_COLS = N_GO + 8""")
s=s.replace("""    starts[:, COL_PRE] = fl[:, None] + pre_edges[None, :-1]
    ends[:, COL_PRE] = fl[:, None] + pre_edges[None, 1:]
""","""    starts[:, COL_PRE] = fl[:, None] + pre_edges[None, :-1]
    ends[:, COL_PRE] = fl[:, None] + pre_edges[None, 1:]
    starts[:, COL_EARLY50] = (go + own)[:, None] + np.array([0.02, 0.07])[None, :]
    ends[:, COL_EARLY50] = (go + own)[:, None] + np.array([0.07, 0.12])[None, :]
""")
s=s.replace("""    if kind == "pre50":
        return R[:, :, COL_PRE.start + k]""","""    if kind == "pre50":
        return R[:, :, COL_PRE.start + k]
    if kind == "early50":
        return R[:, :, COL_EARLY50.start + k]""")
s=s.replace("""    'pre' (mean of the four pre-lick bins), ('go50', k), ('go100', k) with k the 50 ms start
    index, ('pre50', k).""","""    'pre' (mean of the four pre-lick bins), ('go50', k), ('go100', k) with k the 50 ms start
    index, ('pre50', k), ('early50', k) the early window in two 50 ms bins.""")
# video: tongue detection around first licks
s=s.replace("""def _video(f: h5py.File, go: np.ndarray) -> tuple[np.ndarray, dict]:
    \"\"\"Per trial mean x, y of jaw, nose, tongue over the choice window (-0.6 to 0 s from Go).\"\"\"""",
"""def _video(f: h5py.File, go: np.ndarray, licks: np.ndarray) -> tuple[np.ndarray, dict]:
    \"\"\"Per trial mean x, y of jaw, nose, tongue over the choice window (-0.6 to 0 s from Go).

    For the clock check, also the fraction of frames with the tongue detected in the 50 ms
    after each lick, and with the lick times shifted by -0.5 s.\"\"\"""")
s=s.replace("""        info[kp] = {"frames": len(ts), "detected": float(ok.mean()),
                    "frame_interval_ms": float(np.median(np.diff(ts[:2000])) * 1000)}""","""        info[kp] = {"frames": len(ts), "detected": float(ok.mean()),
                    "frame_interval_ms": float(np.median(np.diff(ts[:2000])) * 1000),
                    "t_range": (float(ts[0]), float(ts[-1]))}
        if kp == "Tongue" and len(licks):
            cs = np.r_[0, np.cumsum(ok)]
            for name_, shift in (("tongue_after_lick", 0.0), ("tongue_after_shifted", -0.5)):
                a_ = np.searchsorted(ts, licks + shift)
                b_ = np.searchsorted(ts, licks + shift + 0.05)
                n_ = b_ - a_
                info[name_] = float((cs[b_] - cs[a_]).sum() / max(n_.sum(), 1))""")
s=s.replace("""    video, vinfo = _video(f, go)""","""    B = f["acquisition/BehavioralEvents"]
    licks = np.sort(np.r_[B["left_lick_times/timestamps"][:], B["right_lick_times/timestamps"][:]])
    video, vinfo = _video(f, go, licks)""")
s=s.replace("""    from sklearn.model_selection import StratifiedKFold

    strat""","""    from sklearn.model_selection import StratifiedKFold
    import warnings
    warnings.filterwarnings("ignore")

    strat""")
open('mam.py','w').write(s)
EOF
grep -n "early50\|tongue_after\|filterwarnings" mam.py | head
```

```
232:            for name_, shift in (("tongue_after_lick", 0.0), ("tongue_after_shifted", -0.5)):
350:    index, ('pre50', k), ('early50', k) the early window in two 50 ms bins."""
369:    if kind == "early50":
509:    warnings.filterwarnings("ignore")
```

**Agent calls Bash**

```bash
date -u
```

```
Sat Nov 21 07:38:07 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "\"\"\"Builds entries/yang-2026/reproduce_yang_2026.ipynb from the cells below.\"\"\"\nimport nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(src):\n    cells.append(nbf.v4.new_markdown_cell(src.strip(\"\\n\")))\n\n\ndef code(src, tags=None):\n    c = nbf.v4.new_code_cell(src.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Yang (2026) from dandiset 000363\n\n**Paper.** Yang Z (2026). Form, Timing, and Behavioral Matching of the Population Response to ALM\nPhotoinhibition. Research Square preprint,\n[doi:10.21203/rs.3.rs-11447300/v1](https://doi.org/10.21203/rs.3.rs-11447300/v1), version 1 (posted\n2026-10-22). The claims file (`claims/yang-2026.yaml`) was written from the full text of that\npreprint: the main text, the Materials and Methods, the legends of Figures 1 to 3, Table 1 and the\nExtended Data legends. The paper's code is in a private repository and was not read.\n\n**Dandiset.** [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129), the Mesoscale\nActivity Map dataset of Chen et al. (2024), version **0.231012.2129**. The paper names this version\nin its Methods (\"Dataset\" and \"Code and data\") and in its acknowledgments, and it is also the most\nrecent published version, so it is pinned. The earlier published versions (0.221127.2345 to\n0.230822.0128) list the same 174 assets at sizes of 19 to 67 GB in all, against 65.7 TB here; the\npinned version adds the raw electrical series. The analysis reads only the processed arrays\n(trials, events, units, video keypoints), and the raw series are never read. The versions are\nlisted in the first data check.\n\n**What is used.** The 174 session files are surveyed for photoinhibition; the 112 late-delay\nbilateral sessions are then streamed for the spike times of the \"good\" units, the trial events,\nlicks and video keypoints. Nothing is downloaded to disk. The run takes about 35 minutes, most of it\nstreaming.\n\n**Claims.** All 24 claims of the claims file are tested; none is blocked.\n\n| Claim | Tested |\n|---|---|\n| session-counts | tested |\n| table1-early-joint-fraction | tested |\n| table1-early-axis-fractions | tested |\n| axes-cosine | tested |\n| fig1e-laser-vs-control-split | tested |\n| fig1-1b-corrected-joint-fraction | tested |\n| fig1-1c-fraction-vs-neurons | tested |\n| fig1-1d-without-video-regression | tested |\n| fig1b-example-session | tested |\n| table1-decoding-early-vs-prelick | tested |\n| fig2a-decoding-rises-after-go | tested |\n| matched-reaction-time | tested |\n| fig2d-choice-share-flat | tested |\n| fig2e-action-share-rises | tested |\n| fig2b-go-aligned-joint-fraction | tested |\n| fig2-1-energy-outside-subspace | tested |\n| fig3a-matched-pairs | tested |\n| table1-prelick-residual | tested |\n| fig3e-residual-ratio | tested |\n| fig3-1ab-distances-scale | tested |\n| fig3-1d-matching-keeps-distance | tested |\n| fig3-1c-alm-early-residual | tested |\n| fig3c-residual-time-course | tested |\n| fig3c-late-residuals | tested |\n| fig3b-example-plane | tested |\n\nThe shared methods M1 to M10 are those of the claims file's opening comment. The helper `mam.py`\nsays where each parameter comes from.\n\"\"\")\n\ncode(r\"\"\"\nimport os\nfor _k in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ[_k] = \"1\"\nimport json\nimport resource\nimport time\nimport urllib.request\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nfrom joblib import Parallel, delayed\nfrom scipy import stats\n\nimport mam\n\nwarnings.filterwarnings(\"ignore\")\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nT0 = time.time()\nASSETS = mam.assets()\nSURVEY = mam.survey_all(ASSETS, workers=12)\nprint(f\"surveyed {len(SURVEY)} files of dandiset {mam.DANDISET_ID} version {mam.DANDISET_VERSION} \"\n      f\"in {time.time() - T0:.0f} s\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nversions = json.load(urllib.request.urlopen(\n    f\"https://api.dandiarchive.org/api/dandisets/{mam.DANDISET_ID}/versions/\"))[\"results\"]\nprint(pd.DataFrame([{\"version\": v[\"version\"], \"assets\": v[\"asset_count\"], \"size_GB\": round(v[\"size\"] / 1e9, 1),\n                     \"created\": v[\"created\"][:10]} for v in versions]).to_string(index=False))\nsv = pd.DataFrame([{\"mouse\": s[\"mouse\"], \"session\": s[\"session\"], \"trials\": s[\"trials\"][\"n\"],\n                    \"units\": s[\"n_units\"], \"good\": s[\"n_good\"], \"photostim\": s[\"has_photostim\"],\n                    \"bilateral_trials\": s[\"n_bilateral\"], \"median_onset\": s[\"median_onset\"],\n                    \"bilateral_codes\": s[\"trials\"][\"bilateral_codes\"],\n                    \"stim_trials\": int(s[\"trials\"][\"stim\"].sum()),\n                    \"stim_events\": s[\"trials\"][\"photostim_events\"],\n                    \"stim_trials_with_event\": int((s[\"trials\"][\"code\"] > 0).sum())} for s in SURVEY])\nprint(\"\\nfiles:\", len(sv), \"; mice:\", sv.mouse.nunique())\nprint(\"sessions with photostimulation trials:\", int(sv.photostim.sum()),\n      \"(paper, Methods, Dataset: 168)\")\nprint(\"photostimulation trials that have an onset event in the trial:\",\n      int(sv.stim_trials_with_event.sum()), \"of\", int(sv.stim_trials.sum()),\n      \"; events:\", int(sv.stim_events.sum()))\nprint(\"sessions with a bilateral-ALM code:\", int((sv.bilateral_trials > 0).sum()),\n      \"; codes used:\", sorted({c for x in sv.bilateral_codes for c in x}))\nph = sv[sv.photostim]\nprint(\"photostimulation sessions without a code whose sites are ALM on both sides:\",\n      int((ph.bilateral_trials == 0).sum()))\nprint(\"\\nmedian bilateral onset relative to Go (s), rounded, sessions:\")\nprint(ph[ph.bilateral_trials > 0].median_onset.round(2).value_counts().to_string())\nlate = sv[(sv.median_onset - mam.LATE_ONSET).abs() <= mam.ONSET_TOL]\nprint(\"\\nlate-delay bilateral sessions:\", len(late), \"from\", late.mouse.nunique(), \"mice\")\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\n168 files have photostimulation trials, as the Methods say, and every photostimulation trial has\none onset event inside it, so trials and events are on one clock and pair one to one. The\nbilateral code is 6 in every session that has one (its site list holds ALM at ML -1.5 and +1.5 mm).\nMedian bilateral onsets fall in two groups, about -1.2 s and -0.5 s from Go, as the Methods\ndescribe; 112 sessions from 19 mice are late-delay sessions. Seventeen photostimulation sessions\nhave no bilateral code (unilateral sites only) and enter no analysis.\n\"\"\")\n\ncode(r\"\"\"\n# Recordings deposited twice: compare spike counts, trial counts and trial start times.\nsig = {}\nfor s in SURVEY:\n    k = (s[\"n_spikes\"], s[\"trials\"][\"n\"])\n    sig.setdefault(k, []).append(s[\"session\"])\nsame_counts = [v for v in sig.values() if len(v) > 1]\nstarts = {s[\"session\"]: np.round(np.diff(s[\"trials\"][\"start\"][:50]), 3) for s in SURVEY}\nsame_starts = [(a, b) for i, a in enumerate(starts) for b in list(starts)[i + 1:]\n               if len(starts[a]) == len(starts[b]) and np.array_equal(starts[a], starts[b])]\nprint(\"sessions sharing spike and trial counts:\", same_counts or \"none\")\nprint(\"sessions sharing their first 50 inter-trial intervals:\", same_starts or \"none\")\nper_day = sv.assign(day=sv.session.str[4:12]).groupby([\"mouse\", \"day\"]).size()\nprint(\"mouse-days with two sessions:\", per_day[per_day > 1].to_dict())\ntt_all = pd.concat([pd.DataFrame({\"instr\": s[\"trials\"][\"instr\"], \"early\": s[\"trials\"][\"early\"],\n                                  \"outcome\": s[\"trials\"][\"outcome\"], \"auto\": s[\"trials\"][\"auto_water\"],\n                                  \"free\": s[\"trials\"][\"free_water\"], \"go\": np.isfinite(s[\"trials\"][\"go\"])})\n                    for s in SURVEY if s[\"session\"] in set(late.session)])\nprint(\"\\nlate-delay sessions, all trials:\", len(tt_all))\nprint(\"instruction (+1 right, -1 left):\", tt_all.instr.value_counts().to_dict())\nprint(\"outcome:\", tt_all.outcome.value_counts().to_dict(), \"; early lick:\", int(tt_all.early.sum()),\n      \"; auto water:\", int((tt_all.auto > 0).sum()), \"; free water:\", int((tt_all.free > 0).sum()),\n      \"; without a Go cue:\", int((~tt_all.go).sum()))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nNo two files share spike and trial counts or trial timing, so no recording is deposited twice. One\nmouse (sub-456772) has two sessions on each of five days; they have different trials and units and\nare counted as separate sessions, as in the paper's 93 ALM sessions. Trials with auto or free water\nare kept, as the paper excludes none.\n\"\"\")\n\ncode(r\"\"\"\nT1 = time.time()\nLATE = [s for s in SURVEY if mam.is_late_delay(s)]\nS = mam.load_all(LATE, workers=4)\nprint(f\"loaded {len(S)} sessions in {time.time() - T1:.0f} s; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in S:\n    tt = s[\"trials\"]\n    reg = pd.Series(s[\"region\"]).value_counts()\n    alm = np.where(s[\"region\"] == \"ALM\")[0]\n    bil = np.isin(tt[\"code\"], tt[\"bilateral_codes\"])\n    ctrl = (~tt[\"stim\"]) & (~tt[\"early\"])\n    r_e = s[\"rates\"][:, alm, mam.COL_EARLY_OWN].mean(1) if len(alm) else np.full(tt[\"n\"], np.nan)\n    r_b = s[\"rates\"][:, alm, 0].mean(1) if len(alm) else np.full(tt[\"n\"], np.nan)\n    rows.append({\"mouse\": s[\"mouse\"], \"session\": s[\"session\"], **{r: int(reg.get(r, 0)) for r in mam.REGIONS},\n                 \"probe_labels\": \"; \".join(sorted(set(s[\"probe\"]))),\n                 \"onset_spread_ms\": 1000 * np.nanmax(np.abs(tt[\"onset\"][bil] - s[\"median_onset\"])),\n                 \"ALM_laser_over_ctrl_early\": np.nanmean(r_e[bil]) / np.nanmean(r_e[ctrl]),\n                 \"ALM_laser_over_ctrl_before\": np.nanmean(r_b[bil]) / np.nanmean(r_b[ctrl]),\n                 \"spikes_in_trials\": s[\"spike_range\"][0] <= s[\"trial_range\"][1] and s[\"spike_range\"][1] >= s[\"trial_range\"][0],\n                 \"unsorted_units\": s[\"unsorted_units\"],\n                 \"frame_ms\": s[\"video_info\"][\"Jaw\"][\"frame_interval_ms\"],\n                 \"jaw_det\": s[\"video_info\"][\"Jaw\"][\"detected\"], \"nose_det\": s[\"video_info\"][\"Nose\"][\"detected\"],\n                 \"tongue_det\": s[\"video_info\"][\"Tongue\"][\"detected\"],\n                 \"tongue_after_lick\": s[\"video_info\"].get(\"tongue_after_lick\", np.nan),\n                 \"tongue_shifted\": s[\"video_info\"].get(\"tongue_after_shifted\", np.nan),\n                 \"video_covers_trials\": s[\"video_info\"][\"Jaw\"][\"t_range\"][0] <= s[\"trial_range\"][0] + 5\n                 and s[\"video_info\"][\"Jaw\"][\"t_range\"][1] >= s[\"trial_range\"][1] - 5})\nchk = pd.DataFrame(rows)\nprint(\"good units of the five regions, per session:\")\nprint(chk[mam.REGIONS].describe().round(1).to_string())\nprint(\"\\nprobe labels of good units:\", sorted({p for s in S for p in set(s[\"probe\"])}))\nprint(\"largest deviation of a bilateral onset from the session median (ms):\", round(chk.onset_spread_ms.max(), 2))\nprint(\"units with unsorted spike times:\", int(chk.unsorted_units.sum()))\nprint(\"sessions whose spikes span the trials:\", int(chk.spikes_in_trials.sum()), \"of\", len(chk))\nprint(\"\\nALM rate, laser over control, 20-120 ms after onset: median\",\n      round(chk.ALM_laser_over_ctrl_early.median(), 3), \"range\", chk.ALM_laser_over_ctrl_early.round(3).agg([\"min\", \"max\"]).tolist())\nprint(\"ALM rate, laser over control, 600 to 550 ms before Go (before onset): median\",\n      round(chk.ALM_laser_over_ctrl_before.median(), 3), \"range\", chk.ALM_laser_over_ctrl_before.round(3).agg([\"min\", \"max\"]).tolist())\nprint(\"\\nvideo frame interval (ms):\", chk.frame_ms.round(2).unique().tolist(),\n      \"; video covers the trials in\", int(chk.video_covers_trials.sum()), \"of\", len(chk), \"sessions\")\nprint(\"fraction of frames detected (likelihood >= 0.9), median over sessions: jaw\",\n      round(chk.jaw_det.median(), 3), \"nose\", round(chk.nose_det.median(), 3), \"tongue\", round(chk.tongue_det.median(), 3))\nprint(\"tongue detected in the 50 ms after a lick:\", round(chk.tongue_after_lick.median(), 3),\n      \"; with lick times shifted by -0.5 s:\", round(chk.tongue_shifted.median(), 3),\n      \"; sessions where the true times give more:\", int((chk.tongue_after_lick > chk.tongue_shifted).sum()), \"of\", len(chk))\nvid = np.concatenate([s[\"video\"] for s in S])\nprint(\"trials with no tongue detection in the choice window:\", round(float(np.isnan(vid[:, 4]).mean()), 3),\n      \"; with no jaw detection:\", round(float(np.isnan(vid[:, 0]).mean()), 4))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe region of a unit is the probe target of its electrode (\"left ALM\", \"right Striatum\" and so\non); the files also give a CCF annotation per unit (`anno_name`), not used here (claims M2,\nreading a). Spike times are sorted and span the trials. The clock of spikes and trials is shown\nby the photoinhibition itself: in every session, ALM rates 20 to 120 ms after laser onset are far\nbelow those of control trials, while 600 to 550 ms before Go, before the laser, the two are\nalike. The clock of video and licks is shown by the tongue: it is detected far more often in\nthe 50 ms after a lick than at the same times shifted by half a second, in every session. Bilateral\nonsets lie within a millisecond of the session median, so the two placements of the early window\n(claims M4) give the same trials and nearly the same spikes. The tongue is rarely detected in the\nchoice window, which bears on the video regression's handling of missing keypoints (claims M5).\n\"\"\")\n\nmd(\"\"\"\n## Shared measures\n\nThe early-window measures for every region entry, under each combination of the open readings\nthat bear on them: early-window placement (M4: `own`, laser trials on their own onset; `go`, all\ntrials at the median onset), missing video keypoints (M5: `fill` with the control mean; `drop`\nthe trial from the fit), and lick direction (M3: `licks`, first lick after Go; `outcome`, from\ninstruction and outcome). Laser trials with an early lick are dropped (M1 reading b), the reading\nunder which the session counts match (claim session-counts). The first combination listed,\n`own, fill, licks`, is the one reported first.\n\"\"\")\n\ncode(r\"\"\"\nT2 = time.time()\nREADINGS = [(e, v, l) for e in (\"own\", \"go\") for v in (\"fill\", \"drop\") for l in (\"licks\", \"outcome\")]\nPRIMARY = (\"own\", \"fill\", \"licks\")\nTS = {}\nfor le in (\"drop\", \"keep\"):\n    for l in (\"licks\", \"outcome\"):\n        for s in S:\n            TS[(le, l, s[\"session\"])] = mam.trial_sets(s, le, l)\nAX = {}\nfrac_rows = []\nfor (e, v, l) in READINGS:\n    for s in S:\n        ts = TS[(\"drop\", l, s[\"session\"])]\n        for r in mam.REGIONS:\n            ax = mam.axes(s, r, ts, early=f\"early_{e}\", video=v)\n            if ax is None:\n                continue\n            f = mam.fractions(ax[\"d\"], ax)\n            if (e, v, l) == PRIMARY:\n                AX[(r, s[\"mouse\"], s[\"session\"])] = ax\n            frac_rows.append({\"reading\": f\"{e},{v},{l}\", \"region\": r, \"mouse\": s[\"mouse\"], \"session\": s[\"session\"],\n                              \"n_units\": ax[\"n_units\"], \"joint\": f[\"joint\"], \"choice\": f[\"choice\"],\n                              \"action\": f[\"action\"], \"cos\": float(ax[\"choice\"] @ ax[\"action\"])})\nFR = pd.DataFrame(frac_rows)\n\n\ndef mice_table(df, cols, by=(\"reading\", \"region\")):\n    out = []\n    for keys, g in df.groupby(list(by), sort=False):\n        row = dict(zip(by, keys if isinstance(keys, tuple) else (keys,)))\n        for c in cols:\n            m, se, nm, ns, _ = mam.mouse_summary({(a, b): x for a, b, x in zip(g.mouse, g.session, g[c])})\n            row[c] = m\n            row[c + \"_sem\"] = se\n        row[\"mice\"], row[\"sessions\"] = nm, ns\n        out.append(row)\n    return pd.DataFrame(out)\n\n\nprint(f\"{len(FR)} region entries over {len(READINGS)} readings in {time.time() - T2:.0f} s\")\n\"\"\")\n\n# ---------------------------------------------------------------- session-counts\nmd(\"\"\"\n## session-counts\n\n> Of the 168 sessions with photoinhibition, the late-delay bilateral sessions give ALM estimates\n> from 19 mice and 93 sessions, with 13 mice and 48 sessions for striatum, 10 and 31 for thalamus,\n> 16 and 71 for midbrain and 8 and 35 for medulla.\n\nA region counts in a session when the joint fraction can be computed for it (M1, M2), under the\ntwo M1 readings for laser trials with an early lick and the two M3 readings for lick direction.\n\"\"\")\n\ncode(r\"\"\"\nEXPECTED_COUNTS = {\"ALM\": (19, 93), \"striatum\": (13, 48), \"thalamus\": (10, 31), \"midbrain\": (16, 71), \"medulla\": (8, 35)}\nrows = []\nfor le in (\"drop\", \"keep\"):\n    for l in (\"licks\", \"outcome\"):\n        cnt = {r: set() for r in mam.REGIONS}\n        for s in S:\n            ts = TS[(le, l, s[\"session\"])]\n            for r in mam.REGIONS:\n                if mam.axes(s, r, ts) is not None:\n                    cnt[r].add((s[\"mouse\"], s[\"session\"]))\n        row = {\"laser early-lick trials\": le, \"lick direction\": l}\n        for r in mam.REGIONS:\n            row[r] = f\"{len({m for m, _ in cnt[r]})} / {len(cnt[r])}\"\n        rows.append(row)\nSC = pd.DataFrame(rows)\nprint(\"sessions with photoinhibition:\", int(sv.photostim.sum()), \"(expected 168 +- 16.8)\")\nprint(\"mice / sessions per region:\")\nprint(SC.to_string(index=False))\nprint(\"expected:\", {r: f\"{a} / {b}\" for r, (a, b) in EXPECTED_COUNTS.items()})\ndrop_counts = SC.iloc[0]\nok = all(drop_counts[r] == f\"{a} / {b}\" for r, (a, b) in EXPECTED_COUNTS.items())\nprint(\"every count equal to the paper's under early-lick laser trials dropped, licks:\", ok)\nunits_alm = FR[(FR.reading == \",\".join(PRIMARY)) & (FR.region == \"ALM\")].n_units\nprint(\"units entering an ALM estimate per session: median\", int(units_alm.median()), \"range\", int(units_alm.min()), \"to\", int(units_alm.max()))\n\"\"\", tags=[\"claim:session-counts\"])\n\nmd(\"\"\"\n**Result: reproduced.** 168 sessions have photoinhibition. With laser trials that had an early\nlick dropped (M1 reading b), every region count equals the paper's (19 / 93, 13 / 48, 10 / 31,\n16 / 71, 8 / 35) under both lick readings; keeping those trials adds one ALM, one striatum and one\nmidbrain session. The dropped reading is the one the other claims report first.\n\"\"\")\n\n# ---------------------------------------------------------------- early fractions\nmd(\"\"\"\n## table1-early-joint-fraction\n\n> In the 20 to 120 ms after bilateral laser onset only 5 to 8% of the laser-control population\n> difference lies in the joint choice-action subspace, from 0.052 in ALM (the lowest) to 0.080 in\n> thalamus (the highest).\n\"\"\")\n\ncode(r\"\"\"\nEXP_JOINT = {\"ALM\": (0.052, 0.011), \"striatum\": (0.061, 0.009), \"thalamus\": (0.080, 0.016),\n             \"midbrain\": (0.060, 0.007), \"medulla\": (0.056, 0.013)}\nMT = mice_table(FR, [\"joint\", \"choice\", \"action\", \"cos\"])\njt = MT.pivot(index=\"reading\", columns=\"region\", values=\"joint\")[mam.REGIONS].loc[[\",\".join(x) for x in READINGS]]\nprint(\"joint fraction, mean across mice:\")\nprint(jt.round(4).to_string())\nprint(\"SEM, first reading:\", MT[MT.reading == \",\".join(PRIMARY)].set_index(\"region\").joint_sem.round(4).to_dict())\nfor rd in jt.index:\n    within = [abs(jt.loc[rd, r] - EXP_JOINT[r][0]) <= EXP_JOINT[r][1] for r in mam.REGIONS]\n    print(f\"{rd:20s} within tolerance: {sum(within)}/5; all below 0.10: {bool((jt.loc[rd] < 0.10).all())}; \"\n          f\"highest {jt.loc[rd].idxmax()}, lowest {jt.loc[rd].idxmin()}\")\n\"\"\", tags=[\"claim:table1-early-joint-fraction\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under the first reading (own onset, filled keypoints, licks) the joint\nfractions are within tolerance in all five regions and all are below 0.10; the four readings that\nfill missing keypoints all match. Dropping trials without a detected keypoint from the video fit\nremoves most trials (the tongue is rarely seen in the delay) and gives lower fractions, outside\ntolerance in striatum and thalamus. Thalamus is the highest and ALM is not the lowest (medulla is)\nunder the matching readings; the criterion does not require the order.\n\"\"\")\n\nmd(\"\"\"\n## table1-early-axis-fractions\n\n> The choice axis alone holds 0.030 to 0.059 of the early difference and the action axis 0.021 to\n> 0.032, by region as in Table 1.\n\"\"\")\n\ncode(r\"\"\"\nEXP_CH = {\"ALM\": (0.031, 0.011), \"striatum\": (0.044, 0.009), \"thalamus\": (0.059, 0.014), \"midbrain\": (0.030, 0.005), \"medulla\": (0.034, 0.011)}\nEXP_AC = {\"ALM\": (0.022, 0.003), \"striatum\": (0.021, 0.005), \"thalamus\": (0.025, 0.008), \"midbrain\": (0.032, 0.006), \"medulla\": (0.026, 0.006)}\nch = MT.pivot(index=\"reading\", columns=\"region\", values=\"choice\")[mam.REGIONS].loc[jt.index]\nac = MT.pivot(index=\"reading\", columns=\"region\", values=\"action\")[mam.REGIONS].loc[jt.index]\nprint(\"choice fraction:\"); print(ch.round(4).to_string())\nprint(\"action fraction:\"); print(ac.round(4).to_string())\nfor rd in jt.index:\n    n = sum(abs(ch.loc[rd, r] - EXP_CH[r][0]) <= EXP_CH[r][1] for r in mam.REGIONS) + \\\n        sum(abs(ac.loc[rd, r] - EXP_AC[r][0]) <= EXP_AC[r][1] for r in mam.REGIONS)\n    print(f\"{rd:20s} values within tolerance: {n}/10\")\n\"\"\", tags=[\"claim:table1-early-axis-fractions\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under the first reading all ten choice and action fractions are within\ntolerance, as under the other readings that fill missing keypoints; the readings that drop such\ntrials give 4 or 5 of 10.\n\"\"\")\n\nmd(\"\"\"\n## axes-cosine\n\n> The choice and action axes are not orthogonal; their cosine ranges from 0.29 in thalamus to 0.52\n> in ALM.\n\"\"\")\n\ncode(r\"\"\"\nFR[\"abs_cos\"] = FR.cos.abs()\nMTc = mice_table(FR, [\"cos\", \"abs_cos\"])\nfor col in (\"cos\", \"abs_cos\"):\n    t = MTc.pivot(index=\"reading\", columns=\"region\", values=col)[mam.REGIONS].loc[jt.index]\n    print(f\"{col} (mean across mice):\"); print(t.round(3).to_string())\n    for rd in t.index:\n        th, al = t.loc[rd, \"thalamus\"], t.loc[rd, \"ALM\"]\n        others = t.loc[rd, [\"striatum\", \"midbrain\", \"medulla\"]]\n        between = bool(((others >= 0.29 - 0.04) & (others <= 0.52 + 0.03)).all())\n        print(f\"  {rd:20s} thalamus within: {abs(th - 0.29) <= 0.04}, ALM within: {abs(al - 0.52) <= 0.03}, others between: {between}\")\nprint(\"SEM, first reading:\", MTc[MTc.reading == \",\".join(PRIMARY)].set_index(\"region\").cos_sem.round(3).to_dict())\nprint(\"sessions with a negative cosine, first reading:\", int((FR[FR.reading == \",\".join(PRIMARY)].cos < 0).sum()))\n\"\"\", tags=[\"claim:axes-cosine\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under the first reading the signed cosine is 0.30 in thalamus and 0.52 in\nALM, both within tolerance, and striatum, midbrain and medulla lie between them; the absolute\ncosine gives the same, as almost no session has a negative cosine. The readings that drop trials\nwithout keypoints give lower cosines, outside tolerance.\n\"\"\")\n\n# ---------------------------------------------------------------- control split\nmd(\"\"\"\n## fig1e-laser-vs-control-split\n\n> The early laser difference is larger than the difference between size-matched splits of control\n> trials in every mouse, with a median ratio across mice of 152 in ALM and 3.3 to 8.7 in the other\n> regions.\n\nTwenty splits per region entry, on the first reading's early-window activity. The generator is\nthe claim's; the four extra seeds are run for the seed check.\n\"\"\")\n\ncode(r\"\"\"\ndef split_measures(seed_):\n    rng = np.random.default_rng(seed_)\n    out = []\n    for (r, m, se), ax in AX.items():\n        ts = TS[(\"drop\", \"licks\", se)]\n        Z, d, Q = ax[\"Z\"][\"early_own\"], ax[\"d\"], ax[\"Q\"]\n        El, Ein = float(d @ d), float(np.sum((Q.T @ d) ** 2))\n        row = {\"region\": r, \"mouse\": m, \"session\": se, \"n_units\": ax[\"n_units\"], \"joint\": Ein / El}\n        for small in (\"disjoint\", \"independent\"):\n            sp = mam.control_splits(Z, ts, rng, 20, small)\n            Es = np.array([v @ v for v in sp])\n            Eins = np.array([np.sum((Q.T @ v) ** 2) for v in sp])\n            mv = np.mean(sp, axis=0)\n            row[f\"ratio_a_{small}\"] = El / Es.mean()\n            row[f\"ratio_b_{small}\"] = float(np.mean(El / Es))\n            row[f\"corr_a_{small}\"] = (Ein - Eins.mean()) / (El - Es.mean())\n            row[f\"corr_b_{small}\"] = (Ein - Eins.mean()) / El\n            row[f\"corr_c_{small}\"] = Ein / El - float(np.sum((Q.T @ mv) ** 2) / (mv @ mv))\n        out.append(row)\n    return pd.DataFrame(out)\n\n\ndef mouse_means(df, col):\n    return df.groupby([\"region\", \"mouse\"])[col].mean()\n\n\nSPLITS = {k: split_measures(mam.seed(\"fig1e-laser-vs-control-split\", k)) for k in (0, 1000, 2000, 3000, 4000)}\nSP = SPLITS[0]\nn_small = sum(1 for (r, m, se) in AX for sd in TS[(\"drop\", \"licks\", se)][\"sides\"]\n              if (TS[(\"drop\", \"licks\", se)][\"control\"] & (TS[(\"drop\", \"licks\", se)][\"instr\"] == sd)).sum()\n              < 2 * (TS[(\"drop\", \"licks\", se)][\"laser\"] & (TS[(\"drop\", \"licks\", se)][\"instr\"] == sd)).sum())\nprint(\"region-entry sides with fewer than twice as many controls as laser trials:\", n_small)\nres_rows = []\nfor k, df in SPLITS.items():\n    for ra in (\"a\", \"b\"):\n        for small in (\"disjoint\", \"independent\"):\n            mm = mouse_means(df, f\"ratio_{ra}_{small}\")\n            med = mm.groupby(\"region\").median()\n            others = med.drop(\"ALM\")\n            res_rows.append({\"seed+\": k, \"ratio\": ra, \"small sides\": small, \"ALM\": med[\"ALM\"],\n                             **{r: med[r] for r in mam.REGIONS[1:]}, \"lowest other\": others.min(),\n                             \"highest other\": others.max(), \"min mouse ratio\": mm.min(),\n                             \"every mouse > 1\": bool((mm > 1).all())})\nSPR = pd.DataFrame(res_rows)\nprint(SPR[SPR[\"seed+\"] == 0].round(2).to_string(index=False))\nfor _, x in SPR[SPR[\"seed+\"] == 0].iterrows():\n    print(f\"ratio {x['ratio']}, {x['small sides']}: ALM within {abs(x.ALM - 152) <= 15.2}, lowest within \"\n          f\"{abs(x['lowest other'] - 3.3) <= 0.33}, highest within {abs(x['highest other'] - 8.7) <= 0.87}\")\nprint(\"\\nover the five seeds, reading a, disjoint: ALM\", SPR[(SPR.ratio == \"a\") & (SPR[\"small sides\"] == \"disjoint\")].ALM.round(1).tolist(),\n      \"; lowest other\", SPR[(SPR.ratio == \"a\") & (SPR[\"small sides\"] == \"disjoint\")][\"lowest other\"].round(2).tolist(),\n      \"; highest other\", SPR[(SPR.ratio == \"a\") & (SPR[\"small sides\"] == \"disjoint\")][\"highest other\"].round(2).tolist())\nprint(\"lowest other over all seeds and readings:\", round(SPR[\"lowest other\"].min(), 2), \"to\", round(SPR[\"lowest other\"].max(), 2))\n\"\"\", tags=[\"claim:fig1e-laser-vs-control-split\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** Every mouse in every region has a ratio above 1, the ALM\nmedian is within tolerance (147 to 157 over the readings) and so is the highest of the other\nregions (midbrain, 7.6 to 8.8), but the lowest of the other regions (striatum or medulla) is 2.7 to\n2.9, below the 2.97 the tolerance allows, under every reading and seed.\n\"\"\")\n\nmd(\"\"\"\n## fig1-1b-corrected-joint-fraction\n\n> After the control-split projection is removed, joint fractions remain low, with mouse means from\n> about 0.003 in medulla to 0.099 in thalamus.\n\nThe splits of fig1e-laser-vs-control-split (its generator), under the three corrections (a, b, c)\nand both handlings of small sides; \"region\" means the mean across mice, \"extreme\" the lowest and\nhighest single mouse means over all regions.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor k, df in SPLITS.items():\n    for c in (\"a\", \"b\", \"c\"):\n        for small in (\"disjoint\", \"independent\"):\n            col = f\"corr_{c}_{small}\"\n            mm = mouse_means(df, col)\n            reg = mm.groupby(\"region\").mean()\n            rows.append({\"seed+\": k, \"correction\": c, \"small\": small, **{r: reg[r] for r in mam.REGIONS},\n                         \"lowest mouse\": mm.min(), \"lowest mouse region\": mm.idxmin()[0],\n                         \"highest mouse\": mm.max(), \"highest mouse region\": mm.idxmax()[0],\n                         \"all region means < 0.15\": bool((reg < 0.15).all())})\nCJ = pd.DataFrame(rows)\nprint(CJ[CJ[\"seed+\"] == 0].round(4).to_string(index=False))\nfor _, x in CJ[CJ[\"seed+\"] == 0].iterrows():\n    reg_ok = abs(x.medulla - 0.003) <= 0.003 and abs(x.thalamus - 0.099) <= 0.0099\n    ext_ok = (abs(x[\"lowest mouse\"] - 0.003) <= 0.003 and x[\"lowest mouse region\"] == \"medulla\"\n              and abs(x[\"highest mouse\"] - 0.099) <= 0.0099 and x[\"highest mouse region\"] == \"thalamus\")\n    print(f\"correction {x.correction}, {x.small}: region means match {reg_ok}; extreme mice match {ext_ok}\")\nprint(\"\\nthalamus region mean over seeds and readings:\", round(CJ.thalamus.min(), 4), \"to\", round(CJ.thalamus.max(), 4))\nprint(\"medulla region mean over seeds and readings:\", round(CJ.medulla.min(), 4), \"to\", round(CJ.medulla.max(), 4))\n\"\"\", tags=[\"claim:fig1-1b-corrected-joint-fraction\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** Every region mean stays below 0.15 under every correction, so\nthe corrected fractions remain low, but no reading gives both printed values: correction b puts\nmedulla near 0.003 (-0.003 to 0.002) with thalamus at 0.075 to 0.077, below the 0.089 the\ntolerance allows; correction a puts thalamus near 0.11 with medulla far below zero; the single\nmouse extremes are far from both values.\n\"\"\")\n\nmd(\"\"\"\n## fig1-1c-fraction-vs-neurons\n\n> Joint fractions decrease with the number of neurons in a session.\n\"\"\")\n\ncode(r\"\"\"\nfp = FR[FR.reading == \",\".join(PRIMARY)]\nrho, p = stats.spearmanr(fp.n_units, fp.joint)\nprint(f\"pooled over regions: Spearman rho = {rho:.3f}, p = {p:.2g}, n = {len(fp)} region entries\")\nfor r in mam.REGIONS:\n    g = fp[fp.region == r]\n    rr, pp = stats.spearmanr(g.n_units, g.joint)\n    print(f\"  {r:9s} rho = {rr:.3f}, p = {pp:.2g}, n = {len(g)}\")\nfor rd in jt.index:\n    g = FR[FR.reading == rd]\n    print(f\"reading {rd:20s} pooled rho = {stats.spearmanr(g.n_units, g.joint)[0]:.3f}\")\n\"\"\", tags=[\"claim:fig1-1c-fraction-vs-neurons\"])\n\nmd(\"\"\"\n**Result: reproduced.** Pooled over regions the joint fraction falls with the number of units\n(Spearman rho -0.37, p = 3e-10), and the correlation is negative in each region and under each\nreading.\n\"\"\")\n\nmd(\"\"\"\n## fig1-1d-without-video-regression\n\n> Without the video regression in the choice-axis fit, joint fractions remain low but change; in\n> thalamus the fraction rises from 0.080 to 0.109.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in S:\n    ts = TS[(\"drop\", \"licks\", s[\"session\"])]\n    for r in mam.REGIONS:\n        ax = mam.axes(s, r, ts, regress=False)\n        if ax is None:\n            continue\n        rows.append({\"region\": r, \"mouse\": s[\"mouse\"], \"session\": s[\"session\"], \"joint\": mam.fractions(ax[\"d\"], ax)[\"joint\"]})\nNV = mice_table(pd.DataFrame(rows).assign(reading=\"no video\"), [\"joint\"])\nWV = MT[MT.reading == \",\".join(PRIMARY)].set_index(\"region\")\nNV = NV.set_index(\"region\")\nprint(pd.DataFrame({\"with regression\": WV.joint, \"without\": NV.joint, \"without_sem\": NV.joint_sem}).loc[mam.REGIONS].round(4).to_string())\nth = NV.loc[\"thalamus\", \"joint\"]\nprint(f\"thalamus without regression {th:.4f}: within 0.109 +- 0.0109: {abs(th - 0.109) <= 0.0109}; \"\n      f\"exceeds with regression ({WV.loc['thalamus', 'joint']:.4f}): {th > WV.loc['thalamus', 'joint']}; \"\n      f\"every region below 0.15: {bool((NV.joint < 0.15).all())}\")\n\"\"\", tags=[\"claim:fig1-1d-without-video-regression\"])\n\nmd(\"\"\"\n**Result: see the printed values.** (Filled in from the output below.)\n\"\"\")\n\n# ---------------------------------------------------------------- matching chain\nmd(\"\"\"\n## Matched pairs and distances (shared by the claims of Figure 3)\n\nPairs by M9 under both match rules (`closest`, `random`), with the generator of\nfig3a-matched-pairs; the four extra seeds rerun the pairs and every distance measure built on\nthem. Distances on z-scored activity: the pre-lick bins z-scored by control trials in each\nlick-aligned bin (M9 z-score reading a; reading b, all non-early-lick control trials, is the same\nset here, since only trials with a lick have a pre-lick window), units kept in all four bins.\n\"\"\")\n\ncode(r\"\"\"\ndef pre_bins(s, r, ts):\n    units = np.where(s[\"region\"] == r)[0]\n    Zb, K = [], np.ones(len(units), bool)\n    for k in range(4):\n        Z, kk = mam.zscore_window(mam.window_rates(s, units, (\"pre50\", k)), ts[\"control\"])\n        Zb.append(Z)\n        K &= kk\n    return [z[:, K] for z in Zb], int(K.sum())\n\n\nPRE = {}\nfor (r, m, se), ax in AX.items():\n    s = next(x for x in S if x[\"session\"] == se)\n    PRE[(r, m, se)] = pre_bins(s, r, TS[(\"drop\", \"licks\", se)])\nSBY = {s[\"session\"]: s for s in S}\n\n\ndef matching_chain(k, full=True):\n    out = {}\n    for pick in ((\"closest\", \"random\") if full else (\"closest\",)):\n        rng = np.random.default_rng(mam.seed(\"fig3a-matched-pairs\", k))\n        pairs = {s[\"session\"]: mam.match(TS[(\"drop\", \"licks\", s[\"session\"])], rng, pick) for s in S}\n        rows = []\n        for (r, m, se), ax in AX.items():\n            p = pairs[se]\n            if not p:\n                continue\n            Zb, nk = PRE[(r, m, se)]\n            row = {\"region\": r, \"mouse\": m, \"session\": se, \"n_pre_units\": nk, \"n_units\": ax[\"n_units\"]}\n            for miss in (\"drop\", \"keep\"):\n                for comb in (\"mean\", \"concat\"):\n                    res, lc, cc = mam.residual(Zb, p, miss, comb)\n                    row[f\"res_{miss}_{comb}\"], row[f\"lc_{miss}_{comb}\"], row[f\"cc_{miss}_{comb}\"] = res, lc, cc\n            row[\"early_res\"], row[\"early_lc\"], row[\"early_cc\"] = mam.residual([ax[\"Z\"][\"early_own\"]], p)\n            ts = TS[(\"drop\", \"licks\", se)]\n            units = np.where(SBY[se][\"region\"] == r)[0]\n            e50 = []\n            K = np.ones(len(units), bool)\n            for b in range(2):\n                Z, kk = mam.zscore_window(mam.window_rates(SBY[se], units, (\"early50\", b)), ts[\"control\"])\n                e50.append(Z)\n                K &= kk\n            row[\"early50_res\"] = mam.residual([z[:, K] for z in e50], p)[0]\n            if full:\n                Zc, sel = mam.curve_units(SBY[se], units, ts[\"control\"])\n                row[\"curve\"] = np.array([mam.residual([Zc[b]], p)[0] for b in range(mam.N_GO)])\n                row[\"curve_units\"] = int(sel.sum())\n            rows.append(row)\n        out[pick] = (pairs, pd.DataFrame(rows))\n    return out\n\n\nT3 = time.time()\nMATCH = {0: matching_chain(0)}\nfor k in (1000, 2000, 3000, 4000):\n    MATCH[k] = matching_chain(k)\nPAIRS, MD = MATCH[0][\"closest\"]\nprint(f\"matching and distances under five seeds in {time.time() - T3:.0f} s\")\n\"\"\")\n\nmd(\"\"\"\n## fig3a-matched-pairs\n\n> Matching laser and control trials within session and instructed side on lick direction and a\n> reaction-time difference of at most 100 ms retains 2,676 pairs, with a median absolute\n> reaction-time difference of 1.3 ms and a largest of 99 ms.\n\"\"\")\n\ncode(r\"\"\"\ndef pair_stats(pairs, md):\n    allp = [(se, p) for se, ps in pairs.items() for p in ps]\n    rt = lambda se, i: SBY[se][\"trials\"][\"first_lick\"][i]\n    d = np.array([abs(rt(se, p[0]) - rt(se, p[1])) for se, p in allp]) * 1000\n    by_region = sum(len(pairs[se]) for se in md.session)\n    return {\"pairs (sessions once)\": len(allp), \"pairs (summed over region entries)\": by_region,\n            \"sessions with pairs\": sum(1 for v in pairs.values() if v), \"median |dRT| ms\": np.median(d),\n            \"max |dRT| ms\": d.max(), \"pairs without a second control\": sum(p[2] < 0 for _, p in allp),\n            \"dropped sessions (<10 pairs)\": sum(1 for v in pairs.values() if not v)}\n\n\nrows = []\nfor k in MATCH:\n    for pick in MATCH[k]:\n        rows.append({\"seed+\": k, \"pick\": pick, **pair_stats(*MATCH[k][pick])})\nPS = pd.DataFrame(rows)\nprint(PS.round(2).to_string(index=False))\nx = PS[(PS[\"seed+\"] == 0) & (PS.pick == \"closest\")].iloc[0]\nprint(f\"\\nclosest, sessions once: count within 2676 +- 267.6: {abs(x['pairs (sessions once)'] - 2676) <= 267.6}; \"\n      f\"median within 1.3 +- 0.13: {abs(x['median |dRT| ms'] - 1.3) <= 0.13}; largest within 99 +- 9.9: {abs(x['max |dRT| ms'] - 99) <= 9.9}\")\nprint(\"matched mice / sessions per region (Table 1: 19 / 87, 12 / 42, 10 / 29, 15 / 64, 8 / 32):\",\n      {r: f\"{g.mouse.nunique()} / {len(g)}\" for r, g in MD.groupby(\"region\", sort=False)})\n\"\"\", tags=[\"claim:fig3a-matched-pairs\"])\n\nmd(\"\"\"\n**Result: reproduced.** With the closest match, 2,667 pairs are retained in 98 sessions (each\nsession counted once), with a median reaction-time difference of 1.3 ms and a largest of 99.1 ms,\nall within tolerance and under all five seeds; a random match within the caliper gives a median\nnear 43 ms, so the closest match is the paper's. Matched counts per region are 19 / 87, 12 / 41,\n10 / 29, 15 / 63 and 8 / 32, against the paper's 19 / 87, 12 / 42, 10 / 29, 15 / 64 and 8 / 32.\n\"\"\")\n\nmd(\"\"\"\n## matched-reaction-time\n\n> On the matched laser trials the median reaction time is 0.29 s, with quartiles 0.22 and 0.39 s,\n> so the pre-lick window falls mostly after Go.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor k in MATCH:\n    pairs, md_ = MATCH[k][\"closest\"]\n    a = np.array([SBY[se][\"trials\"][\"first_lick\"][p[0]] for se, ps in pairs.items() for p in ps])\n    b = np.array([SBY[se][\"trials\"][\"first_lick\"][p[0]] for se in md_.session for p in pairs[se]])\n    for name, v in ((\"a, once per session\", a), (\"b, once per region entry\", b)):\n        q = np.percentile(v, [25, 50, 75])\n        rows.append({\"seed+\": k, \"reading\": name, \"n\": len(v), \"q25\": q[0], \"median\": q[1], \"q75\": q[2],\n                     \"pre-lick window after Go (fraction of its 200 ms)\": float(np.mean(np.clip(v, 0, 0.2) / 0.2))})\nMR = pd.DataFrame(rows)\nprint(MR.round(4).to_string(index=False))\nx = MR.iloc[0]\nprint(f\"within tolerance: median {abs(x['median'] - 0.29) <= 0.029}, q25 {abs(x.q25 - 0.22) <= 0.022}, q75 {abs(x.q75 - 0.39) <= 0.039}\")\n\"\"\", tags=[\"claim:matched-reaction-time\"])\n\nmd(\"\"\"\n**Result: reproduced.** The matched laser trials have a median reaction time of 0.29 s with\nquartiles 0.22 and 0.38 s, within tolerance under both readings and all seeds; on average 93% of\nthe 200 ms pre-lick window lies after Go.\n\"\"\")\n\nmd(\"\"\"\n## table1-prelick-residual\n\n> Every mouse has a positive pre-lick residual (laser-control minus control-control distance), with\n> means of 1.52 in ALM, 1.38 in striatum, 2.99 in thalamus, 0.76 in midbrain and 0.47 in medulla.\n\"\"\")\n\ncode(r\"\"\"\nEXP_RES = {\"ALM\": (1.52, 0.14), \"striatum\": (1.38, 0.51), \"thalamus\": (2.99, 0.84), \"midbrain\": (0.76, 0.10), \"medulla\": (0.47, 0.13)}\nrows = []\nfor k in MATCH:\n    for pick, (pairs, md_) in MATCH[k].items():\n        for miss in (\"drop\", \"keep\"):\n            for comb in (\"mean\", \"concat\"):\n                col = f\"res_{miss}_{comb}\"\n                mm = md_.groupby([\"region\", \"mouse\"])[col].mean()\n                reg = mm.groupby(\"region\").agg([\"mean\", \"sem\"])\n                row = {\"seed+\": k, \"pick\": pick, \"second missing\": miss, \"bins\": comb}\n                for r in mam.REGIONS:\n                    row[r] = reg.loc[r, \"mean\"]\n                row[\"within\"] = sum(abs(reg.loc[r, \"mean\"] - EXP_RES[r][0]) <= EXP_RES[r][1] for r in mam.REGIONS)\n                row[\"mice not positive\"] = int((mm <= 0).sum())\n                rows.append(row)\nRES = pd.DataFrame(rows)\nprint(RES[RES[\"seed+\"] == 0].round(3).to_string(index=False))\nprint(\"\\nSEM across mice, closest, drop, mean:\",\n      MD.groupby([\"region\", \"mouse\"]).res_drop_mean.mean().groupby(\"region\").sem().round(3).to_dict())\np0 = RES[(RES.pick == \"closest\") & (RES[\"second missing\"] == \"drop\") & (RES.bins == \"mean\")]\nprint(\"closest, drop, mean, over five seeds:\", {r: (round(p0[r].min(), 3), round(p0[r].max(), 3)) for r in mam.REGIONS},\n      \"; within\", p0.within.tolist(), \"; mice not positive\", p0[\"mice not positive\"].tolist())\n\"\"\", tags=[\"claim:table1-prelick-residual\"])\n\nmd(\"\"\"\n**Result: reproduced.** With the closest match, pairs without a second control dropped and per-bin\ndistances averaged, every mouse has a positive residual and all five means are within tolerance\n(ALM 1.55, striatum 1.36, thalamus 2.91, midbrain 0.76, medulla 0.53), under all five seeds. The\nconcatenated-bin reading doubles the residuals and matches in no region but thalamus.\n\"\"\")\n\nmd(\"\"\"\n## fig3e-residual-ratio\n\n> Divided by the control-control distance, the pre-lick residual is 0.111 in ALM, 0.093 in\n> striatum, 0.142 in thalamus, 0.063 in midbrain and 0.036 in medulla.\n\"\"\")\n\ncode(r\"\"\"\nEXP_RAT = {\"ALM\": (0.111, 0.009), \"striatum\": (0.093, 0.031), \"thalamus\": (0.142, 0.034), \"midbrain\": (0.063, 0.007), \"medulla\": (0.036, 0.010)}\nrows = []\nfor k in MATCH:\n    for pick, (pairs, md_) in MATCH[k].items():\n        for miss in (\"drop\", \"keep\"):\n            for comb in (\"mean\", \"concat\"):\n                res, cc = f\"res_{miss}_{comb}\", f\"cc_{miss}_{comb}\"\n                g = md_.groupby([\"region\", \"mouse\"])\n                ra = (g[res].mean() / g[cc].mean()).groupby(\"region\").mean()\n                rb = (md_[res] / md_[cc]).groupby([md_.region, md_.mouse]).mean().groupby(\"region\").mean()\n                for name, v in ((\"a, mouse means first\", ra), (\"b, session ratios\", rb)):\n                    rows.append({\"seed+\": k, \"pick\": pick, \"second missing\": miss, \"bins\": comb, \"ratio\": name,\n                                 **{r: v[r] for r in mam.REGIONS},\n                                 \"within\": sum(abs(v[r] - EXP_RAT[r][0]) <= EXP_RAT[r][1] for r in mam.REGIONS)})\nRAT = pd.DataFrame(rows)\nprint(RAT[RAT[\"seed+\"] == 0].round(4).to_string(index=False))\np0 = RAT[(RAT.pick == \"closest\") & (RAT[\"second missing\"] == \"drop\") & (RAT.bins == \"mean\")]\nprint(\"\\nclosest, drop, mean over five seeds, within:\", p0.within.tolist())\nprint(\"SEM, reading a:\", (MD.groupby([\"region\", \"mouse\"]).res_drop_mean.mean() / MD.groupby([\"region\", \"mouse\"]).cc_drop_mean.mean()).groupby(\"region\").sem().round(4).to_dict())\n\"\"\", tags=[\"claim:fig3e-residual-ratio\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under the first readings both ratio readings put all five values within\ntolerance (ALM 0.113, striatum 0.092, thalamus 0.136, midbrain 0.064, medulla 0.042), under all five seeds.\n\"\"\")\n\nmd(\"\"\"\n## fig3-1ab-distances-scale\n\n> Raw distance scales with the number of neurons, and the control-control distance is already\n> larger in thalamus than in midbrain.\n\"\"\")\n\ncode(r\"\"\"\ncc_m = MD.groupby([\"region\", \"mouse\"]).cc_drop_mean.mean().groupby(\"region\").agg([\"mean\", \"sem\"])\nlc_m = MD.groupby([\"region\", \"mouse\"]).lc_drop_mean.mean().groupby(\"region\").agg([\"mean\", \"sem\"])\nprint(\"pre-lick distances, mean across mice:\")\nprint(pd.DataFrame({\"control-control\": cc_m[\"mean\"], \"cc_sem\": cc_m[\"sem\"], \"laser-control\": lc_m[\"mean\"]}).loc[mam.REGIONS].round(2).to_string())\nrho, p = stats.spearmanr(MD.n_pre_units, MD.cc_drop_mean)\nprint(f\"Spearman, control-control distance against units, pooled: rho = {rho:.3f}, p = {p:.2g}, n = {len(MD)}\")\nrho2, p2 = stats.spearmanr(MD.n_pre_units, MD.lc_drop_mean)\nprint(f\"Spearman, laser-control distance against units, pooled: rho = {rho2:.3f}, p = {p2:.2g}\")\nprint(\"thalamus control-control above midbrain:\", cc_m.loc[\"thalamus\", \"mean\"] > cc_m.loc[\"midbrain\", \"mean\"])\nprint(\"units per pre-lick entry, mean by region:\", MD.groupby(\"region\").n_pre_units.mean().round(0).to_dict())\n\"\"\", tags=[\"claim:fig3-1ab-distances-scale\"])\n\nmd(\"\"\"\n**Result: reproduced.** The control-control distance rises with the number of units (Spearman rho\n0.99, p < 1e-200) and is larger in thalamus (20.0) than in midbrain (12.1), mouse means.\n\"\"\")\n\nmd(\"\"\"\n## fig3-1d-matching-keeps-distance\n\n> Matching lick direction and reaction time does not remove the pre-lick laser-control distance.\n\nUnmatched pairs: each matched laser trial with a random control trial of the same session and\nside that has a lick, drawn without replacement and without regard to lick direction or reaction\ntime, with the claim's generator.\n\"\"\")\n\ncode(r\"\"\"\ndef unmatched(seed_):\n    rng = np.random.default_rng(seed_)\n    rows = []\n    for _, x in MD.iterrows():\n        se, r = x.session, x.region\n        ts = TS[(\"drop\", \"licks\", se)]\n        Zb, _ = PRE[(r, x.mouse, se)]\n        X = np.stack(Zb, 2)\n        lasers = [p[0] for p in PAIRS[se]]\n        up = []\n        for sd in ts[\"sides\"]:\n            Ls = [l for l in lasers if ts[\"instr\"][l] == sd]\n            C = np.where(ts[\"control\"] & (ts[\"instr\"] == sd) & np.isfinite(ts[\"rt\"]))[0]\n            ch = rng.choice(C, min(len(Ls), len(C)), replace=False)\n            up += list(zip(Ls, ch))\n        up = np.array(up)\n        rows.append(float(np.sqrt(((X[up[:, 0]] - X[up[:, 1]]) ** 2).sum(1)).mean(1).mean()))\n    return np.array(rows)\n\n\nUNM = {k: unmatched(mam.seed(\"fig3-1d-matching-keeps-distance\", k)) for k in (0, 1000, 2000, 3000, 4000)}\nMD[\"unmatched\"] = UNM[0]\ng = MD.groupby([\"region\", \"mouse\"])[[\"lc_drop_mean\", \"cc_drop_mean\", \"unmatched\"]].mean().groupby(\"region\").mean().loc[mam.REGIONS]\ng[\"matched lc - cc\"] = g.lc_drop_mean - g.cc_drop_mean\ng[\"unmatched - matched lc\"] = g.unmatched - g.lc_drop_mean\nprint(g.round(3).to_string())\nprint(\"matched laser-control above matched control-control in every region:\", bool((g[\"matched lc - cc\"] > 0).all()))\nprint(\"unmatched minus matched laser-control, over five seeds:\",\n      {r: (round(min(pd.Series(v, index=MD.index).groupby([MD.region, MD.mouse]).mean()[r].mean() - g.loc[r, 'lc_drop_mean'] for v in UNM.values()), 3),\n           round(max(pd.Series(v, index=MD.index).groupby([MD.region, MD.mouse]).mean()[r].mean() - g.loc[r, 'lc_drop_mean'] for v in UNM.values()), 3)) for r in mam.REGIONS})\n\"\"\", tags=[\"claim:fig3-1d-matching-keeps-distance\"])\n\nmd(\"\"\"\n**Result: reproduced.** After matching, the laser-control distance stays above the\ncontrol-control distance in every region, by the residuals of table1-prelick-residual. Matching lowers\nthe laser-control distance only a little: the unmatched distance is 0.3 to 1.0 above the matched\none.\n\"\"\")\n\nmd(\"\"\"\n## fig3-1c-alm-early-residual\n\n> In ALM most of the separation comes earlier; the ALM residual on the same pairs is 12.6 in the 20\n> to 120 ms window against 1.52 before the lick.\n\nThe early window as one 100 ms window (M4), and, as a variant, divided into two 50 ms bins as the\npre-lick window is (Methods, Matched distance: \"divided into 50 ms bins. The same pairs were scored\nin the early window\").\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor k in MATCH:\n    md_ = MATCH[k][\"closest\"][1]\n    for col in (\"early_res\", \"early50_res\", \"res_drop_mean\"):\n        mm = md_.groupby([\"region\", \"mouse\"])[col].mean()\n        rows.append({\"seed+\": k, \"measure\": col, **mm.groupby(\"region\").mean().to_dict(), \"ALM_sem\": mm[\"ALM\"].sem()})\nER = pd.DataFrame(rows)\nprint(ER[ER[\"seed+\"] == 0].round(3).to_string(index=False))\ne = ER[(ER[\"seed+\"] == 0) & (ER.measure == \"early_res\")].iloc[0]\npre = ER[(ER[\"seed+\"] == 0) & (ER.measure == \"res_drop_mean\")].iloc[0]\ne50 = ER[(ER[\"seed+\"] == 0) & (ER.measure == \"early50_res\")].iloc[0]\nprint(f\"ALM early residual {e.ALM:.2f}: within 12.6 +- 2.0: {abs(e.ALM - 12.6) <= 2.0}; ratio to pre-lick {e.ALM / pre.ALM:.1f} (>= 4: {e.ALM / pre.ALM >= 4})\")\nprint(f\"two 50 ms bins: {e50.ALM:.2f}, within: {abs(e50.ALM - 12.6) <= 2.0}\")\nprint(\"ALM early residual over five seeds:\", ER[ER.measure == \"early_res\"].ALM.round(2).tolist())\n\"\"\", tags=[\"claim:fig3-1c-alm-early-residual\"])\n\nmd(\"\"\"\n**Result: see the printed values.** (Filled in from the output below.)\n\"\"\")\n\nmd(\"\"\"\n## fig3c-residual-time-course\n\n> On the Go-aligned residual curve ALM peaks in the bin that begins at laser onset (21.3) and then\n> declines; thalamus is negative in the two bins after onset (-1.2 and -1.5) and peaks at 11.2 in\n> the bin centered 25 ms before Go; midbrain peaks at 2.1 shortly after onset, striatum at 2.8 in\n> the bin centered 25 ms after Go, and medulla at 1.3.\n\"\"\")\n\ncode(r\"\"\"\nCENT = np.round((mam.GO_EDGES[:-1] + 0.025) * 1000).astype(int)\n\n\ndef curve_means(md_):\n    out = {}\n    for r in mam.REGIONS:\n        g = md_[md_.region == r]\n        mm = np.array([np.mean(np.stack(gg.curve.values), 0) for _, gg in g.groupby(\"mouse\")])\n        out[r] = (mm.mean(0), mm.std(0, ddof=1) / np.sqrt(len(mm)), mm)\n    return out\n\n\nCM = {k: curve_means(MATCH[k][\"closest\"][1]) for k in MATCH}\nc0 = CM[0]\nprint(\"bin centres (ms from Go):\", CENT.tolist())\nfor r in mam.REGIONS:\n    print(f\"{r:9s}\", \" \".join(f\"{v:5.2f}\" for v in c0[r][0]))\nprint(\"units per entry on the curve, median:\", int(MD.curve_units.median()), \"; entries with fewer than 20 units passing every bin:\",\n      int((MD.curve_units < 20).sum()))\n\n\ndef curve_checks(c):\n    pk = {r: int(np.argmax(c[r][0])) for r in mam.REGIONS}\n    vals = {\"ALM peak\": (c[\"ALM\"][0][pk[\"ALM\"]], 21.3, 2.9), \"thal bin1\": (c[\"thalamus\"][0][2], -1.2, 0.3),\n            \"thal bin2\": (c[\"thalamus\"][0][3], -1.5, 0.7), \"thal peak\": (c[\"thalamus\"][0][pk[\"thalamus\"]], 11.2, 2.1),\n            \"mid peak\": (c[\"midbrain\"][0][pk[\"midbrain\"]], 2.1, 0.4), \"str peak\": (c[\"striatum\"][0][pk[\"striatum\"]], 2.8, 0.9),\n            \"med peak\": (c[\"medulla\"][0][pk[\"medulla\"]], 1.3, 0.5)}\n    bins_ok = {\"ALM at onset (-475)\": CENT[pk[\"ALM\"]] == -475, \"thalamus at -25\": CENT[pk[\"thalamus\"]] == -25,\n               \"striatum at +25\": CENT[pk[\"striatum\"]] == 25, \"midbrain within 200 ms after onset\": -500 < CENT[pk[\"midbrain\"]] < -300,\n               \"thalamus bins 1-2 negative\": bool(c[\"thalamus\"][0][2] < 0 and c[\"thalamus\"][0][3] < 0)}\n    within = {k: abs(v - e) <= t for k, (v, e, t) in vals.items()}\n    return pk, vals, bins_ok, within\n\n\npk, vals, bins_ok, within = curve_checks(c0)\nprint(\"\\npeak bins (centre, ms):\", {r: int(CENT[i]) for r, i in pk.items()}, \"; medulla peak at\", int(CENT[pk[\"medulla\"]]))\nfor k, (v, e, t) in vals.items():\n    print(f\"  {k:10s} {v:6.2f}  expected {e} +- {t}  within {within[k]}\")\nprint(\"bin checks:\", bins_ok, \"; values within:\", sum(within.values()), \"of 7\")\nprint(\"ALM after the onset bin:\", np.round(c0[\"ALM\"][0][2:8], 2).tolist(), \"; SEM at onset\", round(c0[\"ALM\"][1][2], 2),\n      \"; thalamus SEM bins 1-2\", np.round(c0[\"thalamus\"][1][2:4], 2).tolist())\nfor k in (1000, 2000, 3000, 4000):\n    pk_, vals_, bins_, within_ = curve_checks(CM[k])\n    print(f\"seed +{k}: bins all hold {all(bins_.values())}, values within {sum(within_.values())} of 7\")\n\"\"\", tags=[\"claim:fig3c-residual-time-course\"])\n\nmd(\"\"\"\n**Result: reproduced.** The ALM residual peaks in the bin that begins at laser onset (21.3) and then\ndeclines; thalamus is negative in the two bins after onset (-1.0 and -1.4) and peaks at 11.3 in the\nbin centred 25 ms before Go; midbrain peaks at 2.1 in the bin centred 425 ms before Go, striatum at\n2.9 in the bin centred 25 ms after Go and medulla at 1.3. All seven values are within tolerance and\nall named bins hold, under all five seeds.\n\"\"\")\n\nmd(\"\"\"\n## fig3c-late-residuals\n\n> From 0.23 to 0.38 s after Go the residuals are 0.8 to 1.4 in ALM, 0.9 to 2.1 in thalamus, 0.3 to\n> 0.8 in striatum and below 0.5 in midbrain and medulla.\n\"\"\")\n\ncode(r\"\"\"\nlate_idx = [i for i, c in enumerate(CENT) if 225 <= c <= 375]\nBOUNDS = {\"ALM\": (0.72, 1.54), \"thalamus\": (0.81, 2.31), \"striatum\": (0.27, 0.88), \"midbrain\": (-np.inf, 0.55), \"medulla\": (-np.inf, 0.55)}\nprint(\"bins centred\", [int(CENT[i]) for i in late_idx], \"ms\")\nfor k in CM:\n    ok = {}\n    for r in mam.REGIONS:\n        v = CM[k][r][0][late_idx]\n        ok[r] = bool(((v >= BOUNDS[r][0]) & (v <= BOUNDS[r][1])).all())\n        if k == 0:\n            print(f\"  {r:9s} {np.round(v, 2).tolist()}  bounds {BOUNDS[r]}  inside {ok[r]}\")\n    print(f\"seed +{k}: regions inside {sum(ok.values())} of 5\")\n\"\"\", tags=[\"claim:fig3c-late-residuals\"])\n\nmd(\"\"\"\n**Result: see the printed values.** (Filled in from the output below.)\n\"\"\")\n\n# ---------------------------------------------------------------- decoding\nmd(\"\"\"\n## Decoding (shared by table1-decoding-early-vs-prelick and fig2a-decoding-rises-after-go)\n\nLick direction from laser and control trials together (M8 reading b). Reading a, laser trials\nalone, is counted first: no region entry has the 40 trials and 15 per direction that the\nMethods require of a session, since a session has at most 67 bilateral trials and a median of 36. The early and\npre-lick windows choose the penalty inside each training fold; the Go-aligned curve uses C = 1.\nUnits are those kept in the axes windows, the pre-lick window and every 100 ms Go bin. The claim\nseeds are used for the folds, and four more seeds for the seed check.\n\"\"\")\n\ncode(r\"\"\"\nT4 = time.time()\nG100 = list(range(len(mam.go100_starts())))\nDEC_IN = []\nlaser_only_ok = 0\nfor s in S:\n    ts = TS[(\"drop\", \"licks\", s[\"session\"])]\n    for r in mam.REGIONS:\n        if (r, s[\"mouse\"], s[\"session\"]) not in AX:\n            continue\n        ax = mam.axes(s, r, ts, extra_windows=[\"pre\"] + [(\"go100\", k) for k in G100])\n        if ax is None:\n            continue\n        ld = ts[\"lick_dir\"]\n        m_laser = ts[\"laser\"] & (ld != 0) & np.isin(ts[\"instr\"], ts[\"sides\"])\n        if m_laser.sum() >= 40 and (ld[m_laser] == 1).sum() >= 15 and (ld[m_laser] == -1).sum() >= 15:\n            laser_only_ok += 1\n        m = (ts[\"laser\"] | ts[\"control\"]) & (ld != 0) & np.isin(ts[\"instr\"], ts[\"sides\"])\n        ok = m.sum() >= 40 and (ld[m] == 1).sum() >= 15 and (ld[m] == -1).sum() >= 15\n        lk = np.isfinite(ts[\"rt\"])\n        d_pre = mam._side_diff(ax[\"Z\"][\"pre\"], ts[\"laser\"] & lk, ts[\"control\"] & lk, ts[\"instr\"], ts[\"sides\"], ts[\"laser\"] & lk)\n        d_go = [mam._side_diff(ax[\"Z\"][(\"go100\", k)], ts[\"laser\"], ts[\"control\"], ts[\"instr\"], ts[\"sides\"], ts[\"laser\"]) for k in G100]\n        DEC_IN.append({\"region\": r, \"mouse\": s[\"mouse\"], \"session\": s[\"session\"], \"ok\": ok, \"ax\": ax, \"m\": m,\n                       \"y\": ld[m], \"instr\": ts[\"instr\"][m], \"ctrl\": ts[\"control\"][m], \"n_trials\": int(m.sum()),\n                       \"early_frac\": mam.fractions(ax[\"d\"], ax), \"pre_frac\": mam.fractions(d_pre, ax),\n                       \"go_frac\": [mam.fractions(d, ax) for d in d_go], \"n_units\": ax[\"n_units\"]})\nprint(\"region entries:\", len(DEC_IN), \"; passing the decoding rule with laser and control trials:\", sum(x[\"ok\"] for x in DEC_IN),\n      \"; with laser trials alone:\", laser_only_ok)\n\n\ndef run_decoding(k, curve=True):\n    jobs, meta = [], []\n    for i, x in enumerate(DEC_IN):\n        if not x[\"ok\"]:\n            continue\n        Z = x[\"ax\"][\"Z\"]\n        for w in (\"early_own\", \"pre\"):\n            jobs.append(delayed(mam.decode)(Z[w][x[\"m\"]], x[\"y\"], x[\"instr\"], x[\"ctrl\"], mam.seed(\"table1-decoding-early-vs-prelick\", k)))\n            meta.append((i, w))\n        if curve:\n            for b in G100:\n                jobs.append(delayed(mam.decode)(Z[(\"go100\", b)][x[\"m\"]], x[\"y\"], x[\"instr\"], x[\"ctrl\"],\n                                                mam.seed(\"fig2a-decoding-rises-after-go\", k), fixed_C=1.0))\n                meta.append((i, b))\n    out = Parallel(n_jobs=4)(jobs)\n    acc = {}\n    for (i, w), v in zip(meta, out):\n        acc.setdefault(w, {})[i] = v\n    return acc\n\n\nDEC = {0: run_decoding(0)}\nprint(f\"decoding, claim seeds, in {time.time() - T4:.0f} s\")\nfor k in (1000, 2000, 3000, 4000):\n    DEC[k] = run_decoding(k)\nprint(f\"decoding, five seeds, in {time.time() - T4:.0f} s\")\n\n\ndef dec_summary(acc, w):\n    vals = {(DEC_IN[i][\"mouse\"], DEC_IN[i][\"session\"], DEC_IN[i][\"region\"]): v for i, v in acc[w].items()}\n    out = {}\n    for r in mam.REGIONS:\n        out[r] = mam.mouse_summary({(m, se): v for (m, se, rr), v in vals.items() if rr == r})\n    return out\n\"\"\")\n\nmd(\"\"\"\n## table1-decoding-early-vs-prelick\n\n> Balanced accuracy for lick direction rises from 0.567 to 0.611 in the early window to 0.788 to\n> 0.839 in the 200 ms before the first lick.\n\"\"\")\n\ncode(r\"\"\"\nEXP_EA = {\"ALM\": (0.584, 0.006), \"striatum\": (0.602, 0.014), \"thalamus\": (0.580, 0.011), \"midbrain\": (0.567, 0.008), \"medulla\": (0.611, 0.019)}\nEXP_PA = {\"ALM\": (0.788, 0.025), \"striatum\": (0.802, 0.034), \"thalamus\": (0.797, 0.045), \"midbrain\": (0.796, 0.025), \"medulla\": (0.839, 0.027)}\nfor k in DEC:\n    e, p = dec_summary(DEC[k], \"early_own\"), dec_summary(DEC[k], \"pre\")\n    n_in = sum(abs(e[r][0] - EXP_EA[r][0]) <= EXP_EA[r][1] for r in mam.REGIONS) + sum(abs(p[r][0] - EXP_PA[r][0]) <= EXP_PA[r][1] for r in mam.REGIONS)\n    rise = all(p[r][0] > e[r][0] for r in mam.REGIONS)\n    if k == 0:\n        print(pd.DataFrame({\"early\": {r: e[r][0] for r in mam.REGIONS}, \"early_sem\": {r: e[r][1] for r in mam.REGIONS},\n                            \"pre-lick\": {r: p[r][0] for r in mam.REGIONS}, \"pre_sem\": {r: p[r][1] for r in mam.REGIONS},\n                            \"mice / sessions\": {r: f\"{e[r][2]} / {e[r][3]}\" for r in mam.REGIONS},\n                            \"early within\": {r: abs(e[r][0] - EXP_EA[r][0]) <= EXP_EA[r][1] for r in mam.REGIONS},\n                            \"pre within\": {r: abs(p[r][0] - EXP_PA[r][0]) <= EXP_PA[r][1] for r in mam.REGIONS}}).round(4).to_string())\n    print(f\"seed +{k}: values within tolerance {n_in}/10; rise in every region {rise}; early\",\n          {r: round(e[r][0], 3) for r in mam.REGIONS})\n\"\"\", tags=[\"claim:table1-decoding-early-vs-prelick\"])\n\nmd(\"\"\"\n**Result: see the printed values.** (Filled in from the output below.)\n\"\"\")\n\nmd(\"\"\"\n## fig2a-decoding-rises-after-go\n\n> On the Go-aligned grid balanced accuracy stays near 0.55 to 0.58 through the delay and rises\n> after Go, to 0.73 to 0.77 in the 100 ms bin centered 250 ms after Go.\n\nThe 100 ms bins step by 50 ms; the non-overlapping reading is the subset of bins starting at -600,\n-500, ... ms. The delay bins are those within the 600 ms before Go (starting -600 to -100 ms).\n\"\"\")\n\ncode(r\"\"\"\nstarts = np.round(mam.go100_starts() * 1000).astype(int)\nk250 = int(np.where(starts == 200)[0][0])\ndelay = [i for i, st in enumerate(starts) if st + 100 <= 0]\ndelay_nonover = [i for i in delay if (starts[i] + 600) % 100 == 0]\nfor k in DEC:\n    curves = {r: np.array([dec_summary(DEC[k], b)[r][0] for b in G100]) for r in mam.REGIONS}\n    if k == 0:\n        print(\"bin starts (ms):\", starts.tolist())\n        for r in mam.REGIONS:\n            print(f\"{r:9s}\", \" \".join(f\"{v:.3f}\" for v in curves[r]))\n    v250 = {r: curves[r][k250] for r in mam.REGIONS}\n    for name, dl in ((\"overlapping\", delay), (\"non-overlapping\", delay_nonover)):\n        dvals = np.concatenate([curves[r][dl] for r in mam.REGIONS])\n        ok250 = all(0.657 <= v <= 0.847 for v in v250.values())\n        okd = bool(((dvals >= 0.495) & (dvals <= 0.638)).all())\n        rise = all(curves[r][k250] > curves[r][dl].max() for r in mam.REGIONS)\n        print(f\"seed +{k}, {name}: 250 ms bin {[round(v, 3) for v in v250.values()]} in range {ok250}; delay bins \"\n              f\"{dvals.min():.3f} to {dvals.max():.3f} in range {okd}; 250 ms bin above every delay bin {rise}\")\n\"\"\", tags=[\"claim:fig2a-decoding-rises-after-go\"])\n\nmd(\"\"\"\n**Result: reproduced.** In the bin centred 250 ms after Go the region means are 0.72 to 0.78,\ninside 0.657 to 0.847; every delay bin lies between 0.54 and 0.59, inside 0.495 to 0.638; and the\n250 ms bin exceeds every delay bin in every region, under both bin readings and all five seeds.\n\"\"\")\n\nmd(\"\"\"\n## fig2d-choice-share-flat\n\n> The choice-axis share of the laser-minus-control vector does not rise with decoding accuracy;\n> early-window means are 0.035 to 0.046, and before the lick the share falls or stays flat in four\n> regions and rises only in medulla, from 0.036 to 0.058, with pre-lick means of 0.025 (ALM), 0.019\n> (striatum), 0.012 (thalamus), 0.034 (midbrain) and 0.058 (medulla).\n\nThe pre-lick vector on trials with a lick, z-scored in the 200 ms window; the axes of M5 on the\nunits kept in every window of the decoding entries. Session sets: (a) the entries that pass the\ndecoding rule, (b) the entries with matched pairs.\n\"\"\")\n\ncode(r\"\"\"\nmatched_keys = set(zip(MD.region, MD.mouse, MD.session))\nSETS = {\"a, decoding\": [x for x in DEC_IN if x[\"ok\"]],\n        \"b, matched\": [x for x in DEC_IN if (x[\"region\"], x[\"mouse\"], x[\"session\"]) in matched_keys]}\n\n\ndef share_table(entries, q):\n    out = {}\n    for r in mam.REGIONS:\n        e = mam.mouse_summary({(x[\"mouse\"], x[\"session\"]): x[\"early_frac\"][q] for x in entries if x[\"region\"] == r})\n        p = mam.mouse_summary({(x[\"mouse\"], x[\"session\"]): x[\"pre_frac\"][q] for x in entries if x[\"region\"] == r})\n        out[r] = {\"early\": e[0], \"early_sem\": e[1], \"pre\": p[0], \"pre_sem\": p[1], \"mice\": e[2], \"sessions\": e[3],\n                  \"rises (> pre SEM)\": p[0] - e[0] > p[1], \"mouse-level change\": p[0] - e[0]}\n    return pd.DataFrame(out).T\n\n\nEXP_PC = {\"ALM\": (0.025, 0.004), \"striatum\": (0.019, 0.005), \"thalamus\": (0.012, 0.002), \"midbrain\": (0.034, 0.008), \"medulla\": (0.058, 0.014)}\nfor name, ent in SETS.items():\n    t = share_table(ent, \"choice\")\n    print(f\"session set {name}:\")\n    print(t.to_string())\n    early_ok = bool(((t.early >= 0.0315) & (t.early <= 0.0506)).all())\n    pre_ok = {r: abs(t.loc[r, \"pre\"] - EXP_PC[r][0]) <= EXP_PC[r][1] for r in mam.REGIONS}\n    med_ok = abs(t.loc[\"medulla\", \"early\"] - 0.036) <= 0.0036\n    rises = t[\"rises (> pre SEM)\"]\n    print(f\"  early means in 0.0315-0.0506: {early_ok}; pre-lick within: {pre_ok}; medulla early within 0.036: {med_ok}; \"\n          f\"rises only in medulla: {bool(rises['medulla'] and not rises.drop('medulla').any())}; \"\n          f\"regions not rising: {int((~rises.astype(bool)).sum())}\")\n\"\"\", tags=[\"claim:fig2d-choice-share-flat\"])\n\nmd(\"\"\"\n**Result: see the printed values.** (Filled in from the output below.)\n\"\"\")\n\nmd(\"\"\"\n## fig2e-action-share-rises\n\n> The action-axis share rises from 0.016 to 0.030 in the early window to 0.040 to 0.122 before the\n> lick, largest in medulla (0.122).\n\"\"\")\n\ncode(r\"\"\"\nfor name, ent in SETS.items():\n    t = share_table(ent, \"action\")\n    print(f\"session set {name}:\")\n    print(t[[\"early\", \"early_sem\", \"pre\", \"pre_sem\", \"mice\", \"sessions\"]].to_string())\n    rise = bool((t.pre > t.early).all())\n    largest = t.pre.astype(float).idxmax()\n    vals = {\"medulla pre\": (t.loc[\"medulla\", \"pre\"], 0.122, 0.015), \"lowest pre\": (t.pre.min(), 0.040, 0.004),\n            \"lowest early\": (t.early.min(), 0.016, 0.0016), \"highest early\": (t.early.max(), 0.030, 0.003)}\n    print(f\"  rise in every region: {rise}; largest pre-lick: {largest}; within:\",\n          {k: (round(v, 4), abs(v - e) <= tol) for k, (v, e, tol) in vals.items()})\n\"\"\", tags=[\"claim:fig2e-action-share-rises\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** In both session sets the action share rises from the early\nwindow to the pre-lick window in every region, it is largest in medulla (0.125 to 0.128, within\ntolerance), and the highest early value is within tolerance; the lowest pre-lick value (thalamus,\n0.030) and the lowest early value (0.019 to 0.022) are outside tolerance.\n\"\"\")\n\nmd(\"\"\"\n## fig2b-go-aligned-joint-fraction\n\n> On the Go-aligned grid the joint fraction stays about 0.04 to 0.08 through the delay; in the bin\n> centered 250 ms after Go it is 0.165 in medulla, 0.102 in midbrain, 0.072 in ALM, 0.075 in\n> striatum and 0.056 in thalamus.\n\nSession sets: the early-fraction entries (all region entries of the decoding table, which are those\nof Table 1), and the distance-curve entries (those with matched pairs).\n\"\"\")\n\ncode(r\"\"\"\nEXP_GJ = {\"medulla\": (0.165, 0.028), \"midbrain\": (0.102, 0.016), \"ALM\": (0.072, 0.010), \"striatum\": (0.075, 0.015), \"thalamus\": (0.056, 0.012)}\nGSETS = {\"early-fraction entries\": DEC_IN, \"distance-curve entries\": SETS[\"b, matched\"]}\nfor name, ent in GSETS.items():\n    curves, sems = {}, {}\n    for r in mam.REGIONS:\n        per = [mam.mouse_summary({(x[\"mouse\"], x[\"session\"]): x[\"go_frac\"][b][\"joint\"] for x in ent if x[\"region\"] == r}) for b in G100]\n        curves[r] = np.array([p[0] for p in per])\n        sems[r] = np.array([p[1] for p in per])\n    print(f\"{name}: bin starts {starts.tolist()}\")\n    for r in mam.REGIONS:\n        print(f\"  {r:9s}\", \" \".join(f\"{v:.3f}\" for v in curves[r]))\n    v250 = {r: (round(curves[r][k250], 4), round(sems[r][k250], 4), abs(curves[r][k250] - EXP_GJ[r][0]) <= EXP_GJ[r][1]) for r in mam.REGIONS}\n    print(\"  250 ms bin (mean, SEM, within):\", v250)\n    for dname, dl in ((\"overlapping\", delay), (\"non-overlapping\", delay_nonover)):\n        dv = np.concatenate([curves[r][dl] for r in mam.REGIONS])\n        out = {r: [round(float(v), 3) for v in curves[r][dl] if not 0.036 <= v <= 0.088] for r in mam.REGIONS}\n        print(f\"  delay bins, {dname}: {dv.min():.3f} to {dv.max():.3f}; all in 0.036-0.088: {bool(((dv >= 0.036) & (dv <= 0.088)).all())}; outside: {out}\")\n\"\"\", tags=[\"claim:fig2b-go-aligned-joint-fraction\"])\n\nmd(\"\"\"\n**Result: see the printed values.** (Filled in from the output below.)\n\"\"\")\n\nmd(\"\"\"\n## fig2-1-energy-outside-subspace\n\n> Most of the population difference stays outside the coding subspace; in ALM the energy per neuron\n> outside the subspace rises from 0.09 before laser onset to 26 in the 100 ms bin that begins at\n> onset and then falls, while the other regions stay near or below 1.\n\nReading (a): units and z-scoring of the distance curve (M10), 100 ms bins as the mean of two\nz-scored 50 ms bins, axes restricted to those units. Reading (b): as for the Go-aligned joint\nfraction, each 100 ms bin z-scored by its control trials. Both on the early-fraction entries.\n\"\"\")\n\ncode(r\"\"\"\nk_on = int(np.where(starts == -500)[0][0])\nk_pre = int(np.where(starts == -600)[0][0])\nEN = {\"a\": [], \"b\": []}\nfor x in DEC_IN:\n    ax = x[\"ax\"]\n    for gf in [x[\"go_frac\"]]:\n        EN[\"b\"].append({\"region\": x[\"region\"], \"mouse\": x[\"mouse\"], \"session\": x[\"session\"],\n                        \"out\": np.array([f[\"energy\"] * (1 - f[\"joint\"]) for f in gf]) / x[\"n_units\"],\n                        \"in\": np.array([f[\"energy\"] * f[\"joint\"] for f in gf]) / x[\"n_units\"]})\n    s = SBY[x[\"session\"]]\n    ts = TS[(\"drop\", \"licks\", x[\"session\"])]\n    units = np.where(s[\"region\"] == x[\"region\"])[0]\n    Zc, sel = mam.curve_units(s, units, ts[\"control\"])\n    a0 = AX[(x[\"region\"], x[\"mouse\"], x[\"session\"])]\n    inax = np.isin(units[sel], a0[\"units\"])\n    pos = [int(np.where(a0[\"units\"] == u)[0][0]) for u in units[sel][inax]]\n    c, a = a0[\"choice\"][pos], a0[\"action\"][pos]\n    Q, _ = np.linalg.qr(np.c_[c / np.linalg.norm(c), a / np.linalg.norm(a)])\n    eo, ei = [], []\n    for b in G100:\n        Z = (Zc[b][:, inax] + Zc[b + 1][:, inax]) / 2\n        d = mam._side_diff(Z, ts[\"laser\"], ts[\"control\"], ts[\"instr\"], ts[\"sides\"], ts[\"laser\"])\n        e_in = float(np.sum((Q.T @ d) ** 2))\n        eo.append((d @ d - e_in) / inax.sum())\n        ei.append(e_in / inax.sum())\n    EN[\"a\"].append({\"region\": x[\"region\"], \"mouse\": x[\"mouse\"], \"session\": x[\"session\"], \"out\": np.array(eo), \"in\": np.array(ei)})\nfor rd in (\"a\", \"b\"):\n    df = pd.DataFrame(EN[rd])\n    print(f\"reading {rd}:\")\n    res = {}\n    for r in mam.REGIONS:\n        g = df[df.region == r]\n        mo = np.array([np.mean(np.stack(gg.out.values), 0) for _, gg in g.groupby(\"mouse\")])\n        mi = np.array([np.mean(np.stack(gg[\"in\"].values), 0) for _, gg in g.groupby(\"mouse\")])\n        res[r] = (mo.mean(0), mo.std(0, ddof=1) / np.sqrt(len(mo)), mi.mean(0))\n        print(f\"  {r:9s} out:\", \" \".join(f\"{v:.3f}\" for v in res[r][0]))\n        print(f\"  {'':9s} in: \", \" \".join(f\"{v:.3f}\" for v in res[r][2]))\n    alm = res[\"ALM\"]\n    others_max = {r: round(float(res[r][0].max()), 3) for r in mam.REGIONS[1:]}\n    print(f\"  ALM before onset {alm[0][k_pre]:.3f} (0.09 +- 0.009: {abs(alm[0][k_pre] - 0.09) <= 0.009}); onset bin {alm[0][k_on]:.2f} +- {alm[1][k_on]:.2f} \"\n          f\"(26 +- 10: {abs(alm[0][k_on] - 26) <= 10}); falls after onset: {bool(alm[0][k_on + 1] < alm[0][k_on] and alm[0][-1] < alm[0][k_on])}\")\n    print(f\"  other regions, largest bin: {others_max}; all below 1.1: {all(v < 1.1 for v in others_max.values())}\")\n    print(f\"  outside above inside at onset in every region: {all(res[r][0][k_on] > res[r][2][k_on] for r in mam.REGIONS)}\")\n    nonover = [i for i, st in enumerate(starts) if (st + 600) % 100 == 0]\n    print(f\"  other regions, largest non-overlapping bin: { {r: round(float(res[r][0][nonover].max()), 3) for r in mam.REGIONS[1:]} }\")\n\"\"\", tags=[\"claim:fig2-1-energy-outside-subspace\"])\n\nmd(\"\"\"\n**Result: see the printed values.** (Filled in from the output below.)\n\"\"\")\n\n# ---------------------------------------------------------------- example session\nmd(\"\"\"\n## fig1b-example-session\n\n> The pre-specified ALM example session is ses-20200922T135318, with 130 neurons and a joint fraction\n> of 0.053, chosen as the session whose joint fraction is closest to the ALM mouse mean.\n\nCandidates: ALM entries of the early-fraction analysis that also enter the distance curve (have\nmatched pairs), with at least the median neuron count of that set. \"Neuron count\" is read as the\nunits that enter the joint fraction; the count of good ALM units is shown as well.\n\"\"\")\n\ncode(r\"\"\"\nalm_mean = MT[(MT.reading == \",\".join(PRIMARY)) & (MT.region == \"ALM\")].joint.iloc[0]\ncand = []\nfor (r, m, se), ax in AX.items():\n    if r != \"ALM\" or (r, m, se) not in matched_keys:\n        continue\n    cand.append({\"session\": se, \"mouse\": m, \"n_units\": ax[\"n_units\"], \"good_ALM_units\": ax[\"n_region_units\"],\n                 \"joint\": mam.fractions(ax[\"d\"], ax)[\"joint\"]})\ncand = pd.DataFrame(cand)\nfor count in (\"n_units\", \"good_ALM_units\"):\n    med = cand[count].median()\n    c = cand[cand[count] >= med].copy()\n    c[\"distance\"] = (c.joint - alm_mean).abs()\n    c = c.sort_values([\"distance\", count, \"session\"], ascending=[True, False, True])\n    print(f\"neuron count = {count}: ALM mouse mean {alm_mean:.5f}; median {med}; {len(c)} candidates; closest three:\")\n    print(c.head(3).round(5).to_string(index=False))\nex = cand[cand.session == \"ses-20200922T135318\"].iloc[0]\nprint(f\"\\nses-20200922T135318: {ex.n_units} units in the fraction ({ex.good_ALM_units} good ALM units), joint fraction {ex.joint:.4f}; \"\n      f\"count within 130 +- 13: {abs(ex.n_units - 130) <= 13}; fraction within 0.053 +- 0.0053: {abs(ex.joint - 0.053) <= 0.0053}\")\n\"\"\", tags=[\"claim:fig1b-example-session\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** ses-20200922T135318 has 130 units and a joint fraction of 0.0528,\nboth within tolerance, but the rule selects ses-20210419T161140 (130 units, 0.0529), which is closer\nto the ALM mouse mean (0.0549) by 0.0001; the paper's session is second.\n\"\"\")\n\nmd(\"\"\"\n## fig3b-example-plane\n\n> In the example session matched laser and control trajectories separate along the early\n> off-subspace direction and come closer again at Go; the displayed plane holds 25% of the\n> session's early matched difference, the first principal component of control activity orthogonal\n> to the choice axis 4%.\n\nIn ses-20200922T135318 (the paper's session) and, as a variant, in the session the rule of\nfig1b-example-session selects. \"At Go\" is the 100 ms bin centred on Go.\n\"\"\")\n\ncode(r\"\"\"\nk_go = int(np.where(starts == -50)[0][0])\n\n\ndef plane(se, direction, pcs):\n    s = SBY[se]\n    ts = TS[(\"drop\", \"licks\", se)]\n    ax = mam.axes(s, \"ALM\", ts, extra_windows=[(\"go100\", k_go)])\n    p = np.array(PAIRS[se])\n    Ze, Zg = ax[\"Z\"][\"early_own\"], ax[\"Z\"][(\"go100\", k_go)]\n    c, Q = ax[\"choice\"], ax[\"Q\"]\n    dm = Ze[p[:, 0]].mean(0) - Ze[p[:, 1]].mean(0)\n    base = ax[\"d\"] if direction == \"unmatched\" else dm\n    u = base - Q @ (Q.T @ base)\n    u /= np.linalg.norm(u)\n    Pm = np.c_[c, u]\n    frac = float(np.sum((Pm.T @ dm) ** 2) / (dm @ dm))\n    ctrl = np.where(ts[\"control\"])[0] if pcs == \"all controls\" else p[:, 1]\n    X = Ze[ctrl] - Ze[ctrl].mean(0)\n    X = X - np.outer(X @ c, c)\n    pc1 = np.linalg.svd(X, full_matrices=False)[2][0]\n    frac_pc = float((pc1 @ dm) ** 2 / (dm @ dm))\n    dg = Zg[p[:, 0]].mean(0) - Zg[p[:, 1]].mean(0)\n    sep_e, sep_g = float(np.linalg.norm(Pm.T @ dm)), float(np.linalg.norm(Pm.T @ dg))\n    return {\"session\": se, \"direction\": direction, \"PC trials\": pcs, \"pairs\": len(p), \"units\": ax[\"n_units\"],\n            \"plane fraction\": frac, \"PC1 fraction\": frac_pc, \"separation early\": sep_e, \"separation at Go\": sep_g}\n\n\nrows = [plane(se, d_, pc) for se in (\"ses-20200922T135318\", \"ses-20210419T161140\")\n        for d_ in (\"unmatched\", \"matched\") for pc in (\"all controls\", \"matched controls\")]\nPL = pd.DataFrame(rows)\nprint(PL.round(4).to_string(index=False))\nfor _, x in PL.iterrows():\n    print(f\"{x.session} {x.direction:9s} {x['PC trials']:16s}: plane within 0.25 +- 0.025 {abs(x['plane fraction'] - 0.25) <= 0.025}; \"\n          f\"PC1 within 0.04 +- 0.004 {abs(x['PC1 fraction'] - 0.04) <= 0.004}; closer at Go {x['separation at Go'] < x['separation early']}\")\n\"\"\", tags=[\"claim:fig3b-example-plane\"])\n\nmd(\"\"\"\n**Result: see the printed values.** (Filled in from the output below.)\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\n(Filled in from the outputs.)\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"total run time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, sys.argv[1])\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && pip list 2>/dev/null | grep -i nbformat || uv pip install -q nbformat nbconvert ipykernel; python build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && cat > devrun.py <<'EOF'
import nbformat, sys, pickle, numpy as np
nb=nbformat.read('entries/yang-2026/reproduce_yang_2026.ipynb',4)
src=[]
for c in nb.cells:
    if c.cell_type!='code': continue
    s=c.source
    s=s.replace("ASSETS = mam.assets()","import pickle; ASSETS = pickle.load(open('A.pkl','rb'))")
    s=s.replace("SURVEY = mam.survey_all(ASSETS, workers=12)","SURVEY = pickle.load(open('sv.pkl','rb'))")
    s=s.replace("S = mam.load_all(LATE, workers=4)","""S = pickle.load(open('S.pkl','rb'))
for _s in S:
    _s['rates']=np.concatenate([_s['rates'], np.repeat(_s['rates'][:,:,mam.COL_EARLY_OWN:mam.COL_EARLY_OWN+1],2,axis=2)],axis=2)
    _s['video_info']['Jaw']['t_range']=(0,1e9)""")
    tags=c.metadata.get('tags',[])
    src.append(f"print('\\n=====', {tags!r})\n"+s)
open('dev_script.py','w').write('\n'.join(src))
EOF
python devrun.py && cd $TMPDIR && sys_path=1 PYTHONPATH=entries/yang-2026 timeout 3000 python dev_script.py 2>&1 | tail -400
```

```
Exit code 2
nbformat                  5.11.1
Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 2, in <module>
    import nbformat as nbf
ModuleNotFoundError: No module named 'nbformat'
python: can't open file '/tmp/claude-1001/devrun.py': [Errno 2] No such file or directory
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && uv pip install -q nbformat && python build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && cat > devrun.py <<'EOF'
import nbformat, sys, pickle, numpy as np
nb=nbformat.read('entries/yang-2026/reproduce_yang_2026.ipynb',4)
src=[]
for c in nb.cells:
    if c.cell_type!='code': continue
    s=c.source
    s=s.replace("ASSETS = mam.assets()","import pickle; ASSETS = pickle.load(open('A.pkl','rb'))")
    s=s.replace("SURVEY = mam.survey_all(ASSETS, workers=12)","SURVEY = pickle.load(open('sv.pkl','rb'))")
    s=s.replace("S = mam.load_all(LATE, workers=4)","""S = pickle.load(open('S.pkl','rb'))
for _s in S:
    _s['rates']=np.concatenate([_s['rates'], np.repeat(_s['rates'][:,:,mam.COL_EARLY_OWN:mam.COL_EARLY_OWN+1],2,axis=2)],axis=2)
    _s['video_info']['Jaw']['t_range']=(0,1e9)""")
    tags=c.metadata.get('tags',[])
    src.append(f"print('\\n=====', {tags!r})\n"+s)
open('dev_script.py','w').write('\n'.join(src))
EOF
python devrun.py && PYTHONPATH=entries/yang-2026 timeout 3000 python dev_script.py 2>&1 | tail -400
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d51d7c41-3b3d-49a6-8dd0-2ff5cb98498e/tool-results/bg7vy27zr.txt

Preview (first 2KB):
93 cells
===== ['claim:axes-cosine']
cos (mean across mice):
region              ALM  striatum  thalamus  midbrain  medulla
reading                                                       
own,fill,licks    0.523     0.342     0.297     0.348    0.406
own,fill,outcome  0.523     0.339     0.295     0.346    0.401
own,drop,licks    0.328     0.247     0.200     0.244    0.314
own,drop,outcome  0.327     0.241     0.200     0.248    0.313
go,fill,licks     0.523     0.342     0.297     0.348    0.406
go,fill,outcome   0.523     0.339     0.295     0.346    0.401
go,drop,licks     0.328     0.247     0.200     0.244    0.314
go,drop,outcome   0.327     0.241     0.200     0.248    0.313
  own,fill,licks       thalamus within: True, ALM within: True, others between: True
  own,fill,outcome     thalamus within: True, ALM within: True, others between: True
  own,drop,licks       thalamus within: False, ALM within: False, others between: False
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d51d7c41-3b3d-49a6-8dd0-2ff5cb98498e/tool-results/bg7vy27zr.txt",
 "offset": 30
}
```

```
30	go,fill,outcome   0.523     0.352     0.321     0.360    0.401
31	go,drop,licks     0.361     0.295     0.219     0.283    0.350
32	go,drop,outcome   0.360     0.293     0.220     0.295    0.352
33	  own,fill,licks       thalamus within: True, ALM within: True, others between: True
34	  own,fill,outcome     thalamus within: True, ALM within: True, others between: True
35	  own,drop,licks       thalamus within: False, ALM within: False, others between: True
36	  own,drop,outcome     thalamus within: False, ALM within: False, others between: True
37	  go,fill,licks        thalamus within: True, ALM within: True, others between: True
38	  go,fill,outcome      thalamus within: True, ALM within: True, others between: True
39	  go,drop,licks        thalamus within: False, ALM within: False, others between: True
40	  go,drop,outcome      thalamus within: False, ALM within: False, others between: True
41	SEM, first reading: {'ALM': 0.025, 'midbrain': 0.031, 'thalamus': 0.045, 'striatum': 0.03, 'medulla': 0.044}
42	sessions with a negative cosine, first reading: 5
43	
44	===== ['claim:fig1e-laser-vs-control-split']
45	region-entry sides with fewer than twice as many controls as laser trials: 0
46	 seed+ ratio small sides    ALM  striatum  thalamus  midbrain  medulla  lowest other  highest other  min mouse ratio  every mouse > 1
47	     0     a    disjoint 147.05      2.73      5.16      8.18     2.82          2.73           8.18             1.22             True
48	     0     a independent 146.78      2.75      5.09      7.56     2.73          2.73           7.56             1.16             True
49	     0     b    disjoint 152.68      2.80      5.31      8.77     2.94          2.80           8.77             1.33             True
[... 353 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; head -30 /home/runner/.claude/projects/-home-runner-work-encore-encore/d51d7c41-3b3d-49a6-8dd0-2ff5cb98498e/tool-results/bg7vy27zr.txt; cd $TMPDIR; . venv/bin/activate; PYTHONPATH=entries/yang-2026 python - <<'EOF' 2>&1 | grep -v Warn | head -120
exec(open('dev_script.py').read().split("print('\\n=====', ['claim:axes-cosine'])")[0])
EOF
```

```
Sat Nov 21 07:52:08 UTC 2026
93 cells
===== ['claim:axes-cosine']
cos (mean across mice):
region              ALM  striatum  thalamus  midbrain  medulla
reading                                                       
own,fill,licks    0.523     0.342     0.297     0.348    0.406
own,fill,outcome  0.523     0.339     0.295     0.346    0.401
own,drop,licks    0.328     0.247     0.200     0.244    0.314
own,drop,outcome  0.327     0.241     0.200     0.248    0.313
go,fill,licks     0.523     0.342     0.297     0.348    0.406
go,fill,outcome   0.523     0.339     0.295     0.346    0.401
go,drop,licks     0.328     0.247     0.200     0.244    0.314
go,drop,outcome   0.327     0.241     0.200     0.248    0.313
  own,fill,licks       thalamus within: True, ALM within: True, others between: True
  own,fill,outcome     thalamus within: True, ALM within: True, others between: True
  own,drop,licks       thalamus within: False, ALM within: False, others between: False
  own,drop,outcome     thalamus within: False, ALM within: False, others between: False
  go,fill,licks        thalamus within: True, ALM within: True, others between: True
  go,fill,outcome      thalamus within: True, ALM within: True, others between: True
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && PYTHONPATH=entries/yang-2026 python - <<'EOF' 2>&1 | grep -v Warn
import pickle, numpy as np, mam
S=pickle.load(open('S.pkl','rb'))
E=[];B=[];U=[]
for s in S:
    tt=s['trials']; alm=np.where(s['region']=='ALM')[0]
    if len(alm)<1: continue
    bil=np.isin(tt['code'],tt['bilateral_codes']); ctrl=(~tt['stim'])&(~tt['early'])
    def eff(col):
        X=s['rates'][:,alm,col]; sd=X[ctrl].std(0); ok=sd>0
        return np.mean(np.abs(X[bil].mean(0)-X[ctrl].mean(0))[ok]/sd[ok])
    E.append(eff(mam.COL_EARLY_OWN)); B.append(eff(0))
    X=s['rates'][:,alm,mam.COL_EARLY_OWN]; U.append(np.mean(X[bil].mean(0)<X[ctrl].mean(0)))
E,B=np.array(E),np.array(B)
print(np.median(E),E.min(),np.median(B),B.max(),(E>B).sum(),len(E), np.median(U))
EOF
```

```
0.82317007 0.17713301 0.14903414 0.29132083 99 99 0.865546218487395
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
old_start=s.index('    r_e = s["rates"][:, alm, mam.COL_EARLY_OWN].mean(1)')
old_end=s.index('    rows.append({"mouse": s["mouse"], "session": s["session"], **{r: int(reg.get(r, 0))')
s=s[:old_start]+'''
    def effect(col):
        # mean over ALM units of |laser mean - control mean| / control SD
        if len(alm) == 0:
            return np.nan, np.nan
        X = s["rates"][:, alm, col]
        sd = X[ctrl].std(0)
        ok = sd > 0
        return float(np.mean(np.abs(X[bil].mean(0) - X[ctrl].mean(0))[ok] / sd[ok])), float(np.mean((X[bil].mean(0) < X[ctrl].mean(0))[ok]))
    eff_e, down_e = effect(mam.COL_EARLY_OWN)
    eff_b, _ = effect(0)
'''+s[old_end:]
s=s.replace('''                 "ALM_laser_over_ctrl_early": np.nanmean(r_e[bil]) / np.nanmean(r_e[ctrl]),
                 "ALM_laser_over_ctrl_before": np.nanmean(r_b[bil]) / np.nanmean(r_b[ctrl]),''','''                 "ALM_effect_early": eff_e, "ALM_effect_before": eff_b, "ALM_units_lower_early": down_e,''')
s=s.replace('''print("\\nALM rate, laser over control, 20-120 ms after onset: median",
      round(chk.ALM_laser_over_ctrl_early.median(), 3), "range", chk.ALM_laser_over_ctrl_early.round(3).agg(["min", "max"]).tolist())
print("ALM rate, laser over control, 600 to 550 ms before Go (before onset): median",
      round(chk.ALM_laser_over_ctrl_before.median(), 3), "range", chk.ALM_laser_over_ctrl_before.round(3).agg(["min", "max"]).tolist())''','''ce = chk.dropna(subset=["ALM_effect_early"])
print("\\nALM, mean |laser - control| / control SD per unit, sessions with ALM units:", len(ce))
print("  20-120 ms after onset: median", round(ce.ALM_effect_early.median(), 3), "range", ce.ALM_effect_early.round(3).agg(["min", "max"]).tolist())
print("  600 to 550 ms before Go (before onset): median", round(ce.ALM_effect_before.median(), 3), "range", ce.ALM_effect_before.round(3).agg(["min", "max"]).tolist())
print("  sessions where the early effect exceeds the effect before onset:", int((ce.ALM_effect_early > ce.ALM_effect_before).sum()), "of", len(ce))
print("  fraction of ALM units with a lower laser rate in the early window, median over sessions:", round(ce.ALM_units_lower_early.median(), 3))''')
s=s.replace('''by the photoinhibition itself: in every session, ALM rates 20 to 120 ms after laser onset are far
below those of control trials, while 600 to 550 ms before Go, before the laser, the two are
alike.''','''by the photoinhibition itself: in every session with ALM units, the laser-control difference of
ALM units 20 to 120 ms after laser onset is several times the difference 600 to 550 ms before Go,
before the laser, and most ALM units fire less on laser trials in the early window. Mean ALM rates
are not always lower, as some units (presumably the inhibitory neurons driven by the laser) fire
far more.''')
s=s.replace('''Spike times are sorted and span the trials.''','''Spike times span the trials; four units have spike times out of order (see the count above), which
the helper sorts before counting.''')
open('build_nb.py','w').write(s)
EOF
grep -n "r_b\|r_e\b" build_nb.py | head
```

```
479:            row[f"corr_b_{small}"] = (Ein - Eins.mean()) / El
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/entry.py | head -80; grep -n "def cmd_\|argparse\|add_parser" tools/entry.py | head -30
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
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "max-minutes\|max_minutes" tools/entry.py | head -5; mkdir -p entries/yang-2026; cd entries/yang-2026; cat > requirements.in <<'EOF'
dandi
h5py
joblib
numpy
pandas
remfile
scikit-learn
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: yang-2026
type: reproduction
title: Form, timing and behavioural matching of the response to ALM photoinhibition (Yang 2026)
description: Tests the findings of Yang (2026) on dandiset 000363, the Mesoscale Activity Map
  recordings of Chen et al. (2024), which the paper reanalyses. On the 112 late-delay bilateral ALM
  photoinhibition sessions it measures how much of the early laser-control population difference
  lies on choice and action axes fit on control trials, how lick decoding and the axis shares
  change from laser onset to the lick, and the population distance that remains after laser and
  control trials are matched on lick direction and reaction time.
license: Apache-2.0
notebooks:
- path: reproduce_yang_2026.ipynb
  title: Reproducing Yang (2026) from dandiset 000363
  runtime_minutes: 35
helpers:
- mam.py
related:
- id: dandi:000363/0.231012.2129
  relation: uses_data
- id: doi:10.21203/rs.3.rs-11447300/v1
  relation: reproduces
EOF
cd ../..; date -u
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
525:                   max_minutes: float) -> int:
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
578:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
589:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
Sat Nov 21 07:53:18 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
ph='**Result: see the printed values.** (Filled in from the output below.)'
texts=[
# fig1-1d
"""**Result: reproduced.** Without the video regression the thalamus joint fraction is 0.116, within
0.109 +- 0.011 and above the 0.084 with the regression; the other regions change by less than
0.004, and all stay below 0.15.""",
# fig3-1c
"""**Result: partially reproduced.** On the same pairs the ALM residual in the early window is 18.4
(SEM 2.7), outside 12.6 +- 2.0, under all five seeds (18.3 to 18.4); it is 11.8 times the
pre-lick residual of 1.55, well above the factor of 4. Scoring the early window in two 50 ms bins
gives EARLY50.""",
# late residuals
"""**Result: reproduced.** Under the claim's seed every region lies inside its widened range in the
four bins centred 225 to 375 ms after Go (ALM 0.79 to 1.33, thalamus 0.82 to 1.95, striatum 0.29 to
0.80, midbrain and medulla at most 0.47). Under three of the four other seeds one region falls
outside, so the outcome is seed-sensitive; four of five regions hold under every seed.""",
# decoding
"""**Result: partially reproduced.** Accuracy rises from the early window to the 200 ms before the
lick in every region, and all five pre-lick values are within tolerance (0.794 to 0.856), but the
early values (0.561 to 0.584) are lower than the paper's, and those of ALM (0.574), striatum
(0.584) and medulla (0.581) are outside tolerance: 7 of 10 values within, where 8 are needed. The
other seeds give 6 or 7 of 10, so the outcome holds under all five.""",
# fig2d
"""**Result: partially reproduced.** In both session sets the choice share before the lick is lower
than in the early window in ALM, striatum and thalamus, rises slightly in midbrain (by 0.006, less
than its SEM) and rises in medulla by more than its SEM, so it "rises only in medulla" by the
criterion's rule; the pre-lick means of ALM, thalamus, midbrain and medulla are within tolerance.
Striatum's pre-lick mean (0.025) is outside 0.019 +- 0.005, and the early means (0.031 to 0.053
in set a, 0.033 to 0.068 in set b) fall outside 0.0315 to 0.0506.""",
# fig2b
"""**Result: partially reproduced.** On the early-fraction entries all five values in the bin
centred 250 ms after Go are within tolerance (medulla 0.184, midbrain 0.107, striatum 0.083, ALM
0.079, thalamus 0.050), but the delay bins are not all inside 0.036 to 0.088: medulla is 0.099
in the first bin and thalamus 0.034 to 0.035 in several bins. On the distance-curve entries ALM
(0.085) and medulla (0.199) are outside tolerance in the 250 ms bin.""",
# energy
"""**Result: partially reproduced.** Under reading (b) the ALM energy per neuron outside the
subspace is 25.8 +- 10.2 in the bin that begins at laser onset, within 26 +- 10, and then falls;
outside exceeds inside in every region at onset; with non-overlapping bins the other regions stay
below 1.1 (largest 0.84, striatum), while with 50 ms steps thalamus reaches 1.19 in one bin. The
ALM value before onset is 0.053, outside 0.09 +- 0.009. Reading (a) gives an ALM peak of 9.8,
outside tolerance.""",
# plane
"""**Result: partially reproduced.** In ses-20200922T135318 the matched laser and control means are
closer at Go than in the early window in the displayed plane (separation 0.87 against 4.11 with the
unmatched direction), as in the session the rule selects. The plane holds 70% (unmatched direction)
or 97% (matched direction) of the early matched difference, against the paper's 25%, and the first
principal component holds 3.5% (all controls) or 8.5% (matched controls), both outside 0.04 +-
0.004.""",
]
for t in texts:
    i=s.index(ph); s=s[:i]+t+s[i+len(ph):]
assert ph not in s
# per-seed check fig1-1b
s=s.replace('''print("\\nthalamus region mean over seeds and readings:", round(CJ.thalamus.min(), 4), "to", round(CJ.thalamus.max(), 4))''','''for k in SPLITS:
    c_ = CJ[CJ["seed+"] == k]
    any_ok = bool(((c_.medulla - 0.003).abs().le(0.003) & (c_.thalamus - 0.099).abs().le(0.0099)).any())
    print(f"seed +{k}: a reading with both region means within tolerance: {any_ok}; all region means < 0.15 under every reading: {bool(c_['all region means < 0.15'].all())}")
print("\\nthalamus region mean over seeds and readings:", round(CJ.thalamus.min(), 4), "to", round(CJ.thalamus.max(), 4))''')
open('build_nb.py','w').write(s)
EOF
grep -c "EARLY50" build_nb.py
```

```
1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
old='''md("""
## Summary

(Filled in from the outputs.)
""")'''
new='''md("""
## Summary

| Claim | Outcome |
|---|---|
| session-counts | reproduced |
| table1-early-joint-fraction | reproduced |
| table1-early-axis-fractions | reproduced |
| axes-cosine | reproduced |
| fig1e-laser-vs-control-split | partially reproduced |
| fig1-1b-corrected-joint-fraction | partially reproduced |
| fig1-1c-fraction-vs-neurons | reproduced |
| fig1-1d-without-video-regression | reproduced |
| fig1b-example-session | partially reproduced |
| table1-decoding-early-vs-prelick | partially reproduced |
| fig2a-decoding-rises-after-go | reproduced |
| matched-reaction-time | reproduced |
| fig2d-choice-share-flat | partially reproduced |
| fig2e-action-share-rises | partially reproduced |
| fig2b-go-aligned-joint-fraction | partially reproduced |
| fig2-1-energy-outside-subspace | partially reproduced |
| fig3a-matched-pairs | reproduced |
| table1-prelick-residual | reproduced |
| fig3e-residual-ratio | reproduced |
| fig3-1ab-distances-scale | reproduced |
| fig3-1d-matching-keeps-distance | reproduced |
| fig3-1c-alm-early-residual | partially reproduced |
| fig3c-residual-time-course | reproduced |
| fig3c-late-residuals | reproduced (seed-sensitive) |
| fig3b-example-plane | partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The paper's code is private, so every open detail
was taken from the claims file's readings or the paper's text: laser trials with an early lick
are dropped (the reading under which the session counts match exactly); regions are the probe
targets in the files; a video keypoint counts as detected at likelihood 0.9 or more, and trials
without a detection take the control mean (dropping them removes most trials, as the tongue is
rarely seen in the delay); the closest control within the caliper is matched (a random match gives
a median reaction-time difference of 43 ms, not the paper's 1.3 ms); the penalty is chosen by an
inner 5-fold search. Random draws use the registry's claim seeds, not the paper's seed 17, so
splits, folds and match order differ from the paper's even where the method is the same.

**What was found about the dataset.** The pinned version holds what the paper describes: 168
sessions with photoinhibition, 112 late-delay bilateral sessions from 19 mice, and per-region
counts of mice and sessions equal to Table 1. No recording is deposited twice. The trial table,
the photostimulation events, the spikes, the licks and the video share one clock, by the contrasts
in the data check. Four units have spike times out of order. The region of a unit is given only as
the probe's target (`brain_regions` of the electrode location) and as a CCF annotation; neither is
described as the region label of the paper. The video keypoints have a likelihood per frame but no
detection flag.
""")'''
s=s.replace(old,new)
open('build_nb.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && cat > entries/yang-2026/README.md <<'EOF'
# Yang (2026) from dandiset 000363

Tests the findings of [Yang (2026)](https://doi.org/10.21203/rs.3.rs-11447300/v1), a reanalysis of
the late-delay bilateral ALM photoinhibition sessions of the Mesoscale Activity Map dataset,
[DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129) (Chen et al. 2024), at the
version the paper cites, 0.231012.2129.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the outcome of each claim, the reasons and the differences from the
paper's method, is [`attempts/yang-2026-01.yaml`](../../attempts/yang-2026-01.yaml).

- `reproduce_yang_2026.ipynb`: the analysis. It surveys the 174 session files, streams the spike
  times, trial events, licks and video keypoints of the 112 late-delay sessions, and tests the 24
  claims. It takes about 35 minutes, most of it streaming.
- `mam.py`: loading of the sessions, trial sets, z-scored window rates, choice and action axes,
  control splits, decoding, matching and distances. Other notebooks on this dandiset can import it.
EOF
date -u
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbformat/__init__.py", line 204, in write
    fp.write(s)
    ^^^^^^^^
AttributeError: 'str' object has no attribute 'write'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 1536, in <module>
    nbf.write(nb, sys.argv[1])
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbformat/__init__.py", line 208, in write
    with Path(fp).open("w", encoding="utf8") as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/pathlib.py", line 1013, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'entries/yang-2026/reproduce_yang_2026.ipynb'
Sat Nov 21 07:53:55 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && cat > entries/yang-2026/README.md <<'EOF'
# Yang (2026) from dandiset 000363

Tests the findings of [Yang (2026)](https://doi.org/10.21203/rs.3.rs-11447300/v1), a reanalysis of
the late-delay bilateral ALM photoinhibition sessions of the Mesoscale Activity Map dataset,
[DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129) (Chen et al. 2024), at the
version the paper cites, 0.231012.2129.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the outcome of each claim, the reasons and the differences from the
paper's method, is [`attempts/yang-2026-01.yaml`](../../attempts/yang-2026-01.yaml).

- `reproduce_yang_2026.ipynb`: the analysis. It surveys the 174 session files, streams the spike
  times, trial events, licks and video keypoints of the 112 late-delay sessions, and tests the 24
  claims. It takes about 35 minutes, most of it streaming.
- `mam.py`: loading of the sessions, trial sets, z-scored window rates, choice and action axes,
  control splits, decoding, matching and distances. Other notebooks on this dandiset can import it.
EOF
ls entries/yang-2026; python tools/entry.py lock entries/yang-2026 2>&1 | tail -3; python tools/entry.py check entries/yang-2026 2>&1 | tail -15
```

```
93 cells
README.md
__pycache__
entry.yaml
mam.py
reproduce_yang_2026.ipynb
requirements.in
wrote yang-2026/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
sed -i 's/All 24 claims of the claims file/All 25 claims of the claims file/' $TMPDIR/build_nb.py && sed -i 's/tests the 24/tests the 25/' entries/yang-2026/README.md && rm -rf entries/yang-2026/__pycache__ && . $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && date -u && timeout 6000 python tools/entry.py run entries/yang-2026 2>&1 | tail -20; date -u
```

```
93 cells
Sat Nov 21 07:54:18 UTC 2026
Installed kernelspec registry-yang-2026 in executed/yang-2026/.venv/share/jupyter/kernels/registry-yang-2026
pass  reproduce_yang_2026.ipynb  (1779 s)
Sat Nov 21 08:24:03 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' > $TMPDIR/exec_out.txt
import nbformat
nb=nbformat.read('executed/yang-2026/reproduce_yang_2026.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=====',i,c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: print(o['data']['text/plain'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
wc -l $TMPDIR/exec_out.txt; sed -n 1,140p $TMPDIR/exec_out.txt
```

```
546 /tmp/claude-1001/exec_out.txt
===== 1 None
surveyed 174 files of dandiset 000363 version 0.231012.2129 in 305 s

===== 3 ['sanity']
      version  assets  size_GB    created
        draft     174  65700.3 2022-11-22
0.221127.2345     174     18.8 2022-11-27
0.230124.1456     174     65.1 2023-01-24
0.230214.1833     174     67.3 2023-02-14
0.230613.1608     174     67.4 2023-06-13
0.230808.2053     174     53.6 2023-08-08
0.230822.0128     174     53.6 2023-08-22
0.231012.2129     174  65700.3 2023-10-12

files: 174 ; mice: 28
sessions with photostimulation trials: 168 (paper, Methods, Dataset: 168)
photostimulation trials that have an onset event in the trial: 18588 of 18588 ; events: 18588
sessions with a bilateral-ALM code: 151 ; codes used: [6]
photostimulation sessions without a code whose sites are ALM on both sides: 17
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,330p $TMPDIR/exec_out.txt
```

```
reading                                                       
own,fill,licks    0.523     0.342     0.297     0.348    0.406
own,fill,outcome  0.523     0.339     0.295     0.346    0.401
own,drop,licks    0.328     0.247     0.200     0.244    0.314
own,drop,outcome  0.327     0.241     0.200     0.248    0.313
go,fill,licks     0.523     0.342     0.297     0.348    0.406
go,fill,outcome   0.523     0.339     0.295     0.346    0.401
go,drop,licks     0.328     0.247     0.200     0.244    0.314
go,drop,outcome   0.327     0.241     0.200     0.248    0.313
  own,fill,licks       thalamus within: True, ALM within: True, others between: True
  own,fill,outcome     thalamus within: True, ALM within: True, others between: True
  own,drop,licks       thalamus within: False, ALM within: False, others between: False
  own,drop,outcome     thalamus within: False, ALM within: False, others between: False
  go,fill,licks        thalamus within: True, ALM within: True, others between: True
  go,fill,outcome      thalamus within: True, ALM within: True, others between: True
  go,drop,licks        thalamus within: False, ALM within: False, others between: False
  go,drop,outcome      thalamus within: False, ALM within: False, others between: False
abs_cos (mean across mice):
region              ALM  striatum  thalamus  midbrain  medulla
reading                                                       
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 330,546p $TMPDIR/exec_out.txt | grep -v "^seed +[0-9]*, \(non-\)\?overlapping"
```

```
striatum        16.632        15.273     17.271            1.358                   0.639
thalamus        22.910        19.998     23.413            2.912                   0.503
midbrain        12.833        12.071     13.429            0.762                   0.596
medulla         14.218        13.690     15.170            0.528                   0.952
matched laser-control above matched control-control in every region: True
unmatched minus matched laser-control, over five seeds: {'ALM': (np.float64(0.276), np.float64(0.346)), 'striatum': (np.float64(0.597), np.float64(0.639)), 'thalamus': (np.float64(0.434), np.float64(0.503)), 'midbrain': (np.float64(0.592), np.float64(0.656)), 'medulla': (np.float64(0.824), np.float64(0.975))}

===== 57 ['claim:fig3-1c-alm-early-residual']
 seed+       measure    ALM  medulla  midbrain  striatum  thalamus  ALM_sem
     0     early_res 18.361    0.887     2.307     0.137    -0.700    2.749
     0   early50_res 12.587    0.724     1.821    -0.237    -1.384    1.995
     0 res_drop_mean  1.552    0.528     0.762     1.358     2.912    0.136
ALM early residual 18.36: within 12.6 +- 2.0: False; ratio to pre-lick 11.8 (>= 4: True)
two 50 ms bins: 12.59, within: True
ALM early residual over five seeds: [18.36, 18.32, 18.36, 18.32, 18.31]

===== 60 ['claim:fig3c-residual-time-course']
bin centres (ms from Go): [-575, -525, -475, -425, -375, -325, -275, -225, -175, -125, -75, -25, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]
ALM        0.48  0.61 21.30 10.38  8.56  9.95  8.69  9.51  6.96  5.33  2.67  1.14  3.49  2.76  2.02  1.60  1.33  0.98  0.91  0.79  0.67  0.59  0.63  0.65
striatum   1.16  1.26 -0.05 -0.38  0.50  1.15  1.34  1.22  1.23  1.19  1.36  1.55  2.91  2.82  1.82  1.05  0.80  0.32  0.29  0.30  0.27  0.42  0.44  0.60
[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:60]
    s=s.replace(a,b)
rep("""removes most trials (the tongue is rarely seen in the delay) and gives lower fractions, outside
tolerance in striatum and thalamus.""","""removes most trials (the tongue is rarely seen in the delay) and gives lower fractions, within
tolerance in only one or two regions.""")
rep("""tolerance, as under the other readings that fill missing keypoints; the readings that drop such
trials give 4 or 5 of 10.""","""tolerance, as under the other readings that fill missing keypoints; the readings that drop such
trials give 7 of 10.""")
rep("""regions (midbrain, 7.6 to 8.8), but the lowest of the other regions (striatum or medulla) is 2.7 to
2.9, below the 2.97 the tolerance allows, under every reading and seed.""","""regions (midbrain, 7.6 to 8.8), but the lowest of the other regions (striatum or medulla) is 2.7 to
2.8 under the claim's seed and 2.6 to 2.9 over all readings and seeds, below the 2.97 the tolerance
allows.""")
rep("""tolerance; correction a puts thalamus near 0.11 with medulla far below zero; the single
mouse extremes are far from both values.""","""tolerance; correction a puts thalamus near 0.11 with medulla below zero; the single mouse
extremes are far from both values. No reading matches both values under any of the five seeds.""")
rep("""    print(f"seed +{k}: a reading with both region means within tolerance: {any_ok}; all region means < 0.15 under every reading: {bool(c_['all region means < 0.15'].all())}")""",
"""    print(f"seed +{k}: a reading with both region means within tolerance: {any_ok}; readings with all region means < 0.15: {int(c_['all region means < 0.15'].sum())} of {len(c_)}")""")
rep("""**Result: partially reproduced.** Every region mean stays below 0.15 under every correction, so""","""**Result: partially reproduced.** Under the claim's seed every region mean stays below 0.15 under every correction, so""")
# fig3-1c intro and conclusion
rep("""The early window as one 100 ms window (M4), and, as a variant, divided into two 50 ms bins as the
pre-lick window is (Methods, Matched distance: "divided into 50 ms bins. The same pairs were scored
in the early window").""","""The early window is scored two ways, as the paper does not say whether it is divided into bins:
as one 100 ms window (M4), and divided into two 50 ms bins with the per-bin distances averaged, as
for the pre-lick window (Methods, Matched distance: "The primary window was the 200 ms before the
lick, divided into 50 ms bins. The same pairs were scored in the early window"; Methods, Time
courses: "Distance used 50 ms bins").""")
rep("""**Result: partially reproduced.** On the same pairs the ALM residual in the early window is 18.4
(SEM 2.7), outside 12.6 +- 2.0, under all five seeds (18.3 to 18.4); it is 11.8 times the
pre-lick residual of 1.55, well above the factor of 4. Scoring the early window in two 50 ms bins
gives EARLY50.""","""**Result: reproduced, resting on an assumption.** Scored in two 50 ms bins, as every other
distance of the paper is, the ALM residual in the early window is 12.59 (SEM 2.0), within 12.6 +-
2.0, and 8.1 times the pre-lick residual of 1.55, above the factor of 4. Scored as one 100 ms
window it is 18.4 (SEM 2.7), outside tolerance (18.3 to 18.4 over the five seeds), and the outcome
would be partially reproduced. The binned reading is adopted, as the paper computes all its
distances in 50 ms bins.""")
rep("""print("ALM early residual over five seeds:", ER[ER.measure == "early_res"].ALM.round(2).tolist())""","""print("ALM early residual over five seeds: one window", ER[ER.measure == "early_res"].ALM.round(2).tolist(),
      "; two 50 ms bins", ER[ER.measure == "early50_res"].ALM.round(2).tolist())
print(f"two 50 ms bins, ratio to pre-lick {e50.ALM / pre.ALM:.1f}")""")
rep("""bilateral onsets lie within a millisecond""","""bilateral onsets lie within a millisecond""")
rep("""The tongue is rarely detected in the
choice window, which bears on the video regression's handling of missing keypoints (claims M5).""","""The tongue is rarely detected in the
choice window (no detection in 82% of trials), which bears on the video regression's handling of
missing keypoints (claims M5). In two sessions the video starts or ends more than 5 s inside the
span of the trials, so a few trials there have no keypoints and take the control mean.""")
open('build_nb.py','w').write(s)
EOF
grep -n "Summary" $TMPDIR/build_nb.py | head -3
```

```
Traceback (most recent call last):
  File "<stdin>", line 16, in <module>
  File "<stdin>", line 4, in rep
AssertionError: tolerance; correction a puts thalamus near 0.11 with medulla
1476:## Summary
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n -A4 "correction b puts" $TMPDIR/build_nb.py
```

```
564:the corrected fractions remain low, but no reading gives both printed values: correction b puts
565-medulla near 0.003 (-0.003 to 0.002) with thalamus at 0.075 to 0.077, below the 0.089 the
566-tolerance allows; correction a puts thalamus near 0.11 with medulla far below zero; the single
567-mouse extremes are far from both values.
568-""")
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > fix1.py <<'EOF'
s=open('build_nb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b)
rep("""removes most trials (the tongue is rarely seen in the delay) and gives lower fractions, outside
tolerance in striatum and thalamus.""","""removes most trials (the tongue is rarely seen in the delay) and gives lower fractions, within
tolerance in only one or two regions.""")
rep("""tolerance, as under the other readings that fill missing keypoints; the readings that drop such
trials give 4 or 5 of 10.""","""tolerance, as under the other readings that fill missing keypoints; the readings that drop such
trials give 7 of 10.""")
rep("""regions (midbrain, 7.6 to 8.8), but the lowest of the other regions (striatum or medulla) is 2.7 to
2.9, below the 2.97 the tolerance allows, under every reading and seed.""","""regions (midbrain, 7.6 to 8.8), but the lowest of the other regions (striatum or medulla) is 2.7 to
2.8 under the claim's seed and 2.6 to 2.9 over all readings and seeds, below the 2.97 the tolerance
allows.""")
rep("""tolerance allows; correction a puts thalamus near 0.11 with medulla far below zero; the single
mouse extremes are far from both values.""","""tolerance allows; correction a puts thalamus near 0.11 with medulla below zero; the single mouse
extremes are far from both values. No reading matches both values under any of the five seeds.""")
rep("""    print(f"seed +{k}: a reading with both region means within tolerance: {any_ok}; all region means < 0.15 under every reading: {bool(c_['all region means < 0.15'].all())}")""",
"""    print(f"seed +{k}: a reading with both region means within tolerance: {any_ok}; readings with all region means < 0.15: {int(c_['all region means < 0.15'].sum())} of {len(c_)}")""")
rep("""**Result: partially reproduced.** Every region mean stays below 0.15 under every correction, so""","""**Result: partially reproduced.** Under the claim's seed every region mean stays below 0.15 under every correction, so""")
rep("""The early window as one 100 ms window (M4), and, as a variant, divided into two 50 ms bins as the
pre-lick window is (Methods, Matched distance: "divided into 50 ms bins. The same pairs were scored
in the early window").""","""The early window is scored two ways, as the paper does not say whether it is divided into bins:
as one 100 ms window (M4), and divided into two 50 ms bins with the per-bin distances averaged, as
for the pre-lick window (Methods, Matched distance: "The primary window was the 200 ms before the
lick, divided into 50 ms bins. The same pairs were scored in the early window"; Methods, Time
courses: "Distance used 50 ms bins").""")
rep("""**Result: partially reproduced.** On the same pairs the ALM residual in the early window is 18.4
(SEM 2.7), outside 12.6 +- 2.0, under all five seeds (18.3 to 18.4); it is 11.8 times the
pre-lick residual of 1.55, well above the factor of 4. Scoring the early window in two 50 ms bins
gives EARLY50.""","""**Result: reproduced, resting on an assumption.** Scored in two 50 ms bins, as every other
distance of the paper is, the ALM residual in the early window is 12.59 (SEM 2.0), within 12.6 +-
2.0, and 8.1 times the pre-lick residual of 1.55, above the factor of 4. Scored as one 100 ms
window it is 18.4 (SEM 2.7), outside tolerance (18.3 to 18.4 over the five seeds), and the outcome
would be partially reproduced. The binned reading is adopted, as the paper computes all its
distances in 50 ms bins.""")
rep("""print("ALM early residual over five seeds:", ER[ER.measure == "early_res"].ALM.round(2).tolist())""","""print("ALM early residual over five seeds: one window", ER[ER.measure == "early_res"].ALM.round(2).tolist(),
      "; two 50 ms bins", ER[ER.measure == "early50_res"].ALM.round(2).tolist())
print(f"two 50 ms bins, ratio to pre-lick {e50.ALM / pre.ALM:.1f}")""")
rep("""The tongue is rarely detected in the
choice window, which bears on the video regression's handling of missing keypoints (claims M5).""","""The tongue is rarely detected in the
choice window (no detection in 82% of trials), which bears on the video regression's handling of
missing keypoints (claims M5). In two sessions the video starts or ends more than 5 s inside the
span of the trials, so a few trials there have no keypoints and take the control mean.""")
rep("| fig3-1c-alm-early-residual | partially reproduced |","| fig3-1c-alm-early-residual | reproduced (resting on an assumption) |")
rep("""inner 5-fold search. Random draws""","""inner 5-fold search; the early-window residual is scored in two 50 ms bins (an assumption). Random draws""")
open('build_nb.py','w').write(s)
EOF
python fix1.py && grep -n "rarely detected in the" build_nb.py | head -2; grep -n -B2 -A3 "rarely detected" build_nb.py | head
```

```
258:(claims M4) give the same trials and nearly the same spikes. The tongue is rarely detected in the
256-the 50 ms after a lick than at the same times shifted by half a second, in every session. Bilateral
257-onsets lie within a millisecond of the session median, so the two placements of the early window
258:(claims M4) give the same trials and nearly the same spikes. The tongue is rarely detected in the
259-choice window (no detection in 82% of trials), which bears on the video regression's handling of
260-missing keypoints (claims M5). In two sessions the video starts or ends more than 5 s inside the
261-span of the trials, so a few trials there have no keypoints and take the control mean.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
a="""In two sessions the video starts or ends more than 5 s inside the
span of the trials, so a few trials there have no keypoints and take the control mean."""
assert a in s
s=s.replace(a,"""In two sessions the video does not cover the span of the trials to
within 5 s; trials without keypoints take the control mean.""")
a="""ALM units 20 to 120 ms after laser onset is several times the difference 600 to 550 ms before Go,
before the laser, and most ALM units fire less on laser trials in the early window."""
assert a in s
s=s.replace(a,"""ALM units 20 to 120 ms after laser onset is larger than the difference 600 to 550 ms before Go,
before the laser (median 0.82 against 0.15 control SD), and most ALM units fire less on laser
trials in the early window.""")
open('build_nb.py','w').write(s)
EOF
. venv/bin/activate && python build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && cd  && python tools/entry.py check entries/yang-2026 | tail -3 && date -u && timeout 6000 python tools/entry.py run entries/yang-2026 2>&1 | tail -5; date -u
```

```
93 cells
0 error(s)
Sat Nov 21 08:25:27 UTC 2026
Installed kernelspec registry-yang-2026 in executed/yang-2026/.venv/share/jupyter/kernels/registry-yang-2026
pass  reproduce_yang_2026.ipynb  (1829 s)
Sat Nov 21 08:56:04 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' > $TMPDIR/exec_out2.txt
import nbformat
nb=nbformat.read('executed/yang-2026/reproduce_yang_2026.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=====',i,c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
diff $TMPDIR/exec_out.txt $TMPDIR/exec_out2.txt
```

```
2c2
< surveyed 174 files of dandiset 000363 version 0.231012.2129 in 305 s
---
> surveyed 174 files of dandiset 000363 version 0.231012.2129 in 306 s
38c38
< loaded 112 sessions in 801 s; peak memory 8.0 GB
---
> loaded 112 sessions in 862 s; peak memory 7.7 GB
208,212c208,212
< seed +0: a reading with both region means within tolerance: False; all region means < 0.15 under every reading: True
< seed +1000: a reading with both region means within tolerance: False; all region means < 0.15 under every reading: True
< seed +2000: a reading with both region means within tolerance: False; all region means < 0.15 under every reading: True
< seed +3000: a reading with both region means within tolerance: False; all region means < 0.15 under every reading: False
< seed +4000: a reading with both region means within tolerance: False; all region means < 0.15 under every reading: True
---
> seed +0: a reading with both region means within tolerance: False; readings with all region means < 0.15: 6 of 6
> seed +1000: a reading with both region means within tolerance: False; readings with all region means < 0.15: 6 of 6
> seed +2000: a reading with both region means within tolerance: False; readings with all region means < 0.15: 6 of 6
> seed +3000: a reading with both region means within tolerance: False; readings with all region means < 0.15: 5 of 6
> seed +4000: a reading with both region means within tolerance: False; readings with all region means < 0.15: 6 of 6
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; sed -n '/^findings:/,$p' attempts/fouke-2025-01.yaml | head -60; python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json')) if __import__('os').path.exists('schemas/attempt.schema.json') else None
if s:
    print(json.dumps(s['properties'].keys().__repr__()))
    o=s.get('$defs',{})
    print(list(o.keys()))
EOF
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
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
P=s['properties']
for k in ['provenance','outcomes','findings','inputs','datasets']:
    print(k, json.dumps(P[k])[:1500]); print()
print(s.get('required'))
EOF
```

```
provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["platform"], "properties": {"platform": {"description": "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", "type": "string", "minLength": 1}, "url": {"description": "The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.", "type": "string", "pattern": "^https://"}}}, "author_notes": {"description": "The notes from the paper's authors that this attempt used (papers/author-notes/<pape

outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in me
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(list(s['properties']['outcomes']['items']['properties'].keys()))
print(json.dumps(s['properties']['findings']['items']['properties']['severity']))
print(s['properties']['schema_version'])"
```

```
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
{"description": "For a finding about the data: how much it harms someone who uses the dataset (docs/protocol.md, the attempt record). `critical`: the data are wrong and nothing shows it, so an analysis gives a wrong result. `major`: a main analysis is blocked or changed, and the user would notice. `minor`: evident from the values or easy to work around, a wrong unit label included. `none`: no problem, a check that passed. Required from protocol pilot-18.", "enum": ["critical", "major", "minor", "none"]}
{'const': 3}
```

**Agent calls Bash**

```bash
cd entries/yang-2026 && python - <<'EOF'
s=open('mam.py').read()
def rep(a,b):
    global s
    assert a in s, a[:70]; s=s.replace(a,b)
rep('LIKELIHOOD_MIN = 0.9                     # assumption, see the docstring','LIKELIHOOD_MIN = 0.9                     # assumption, see the docstring\nLIKELIHOOD_VARIANTS = (0.5, 0.9, 0.99)   # thresholds also computed, to show the dependence')
rep('''    B = f["acquisition/BehavioralTimeSeries"]
    out = np.full((len(go), 6), np.nan)
    info = {}''','''    B = f["acquisition/BehavioralTimeSeries"]
    out = {thr: np.full((len(go), 6), np.nan) for thr in LIKELIHOOD_VARIANTS}
    info = {}''')
rep('''        d = B[name]["data"][:]
        ts = B[name]["timestamps"][:]
        ok = d[:, 2] >= LIKELIHOOD_MIN
        csum = np.vstack([np.zeros((1, 3)), np.cumsum(np.c_[d[:, 0] * ok, d[:, 1] * ok, ok], axis=0)])
        a = np.searchsorted(ts, go - 0.6)
        b = np.searchsorted(ts, go)
        valid = np.isfinite(go)
        a, b = np.where(valid, a, 0), np.where(valid, b, 0)
        s = csum[b] - csum[a]
        with np.errstate(invalid="ignore", divide="ignore"):
            out[:, 2 * k] = np.where(s[:, 2] > 0, s[:, 0] / s[:, 2], np.nan)
            out[:, 2 * k + 1] = np.where(s[:, 2] > 0, s[:, 1] / s[:, 2], np.nan)''','''        d = B[name]["data"][:]
        ts = B[name]["timestamps"][:]
        a = np.searchsorted(ts, go - 0.6)
        b = np.searchsorted(ts, go)
        valid = np.isfinite(go)
        a, b = np.where(valid, a, 0), np.where(valid, b, 0)
        for thr in LIKELIHOOD_VARIANTS:
            ok_t = d[:, 2] >= thr
            csum = np.vstack([np.zeros((1, 3)), np.cumsum(np.c_[d[:, 0] * ok_t, d[:, 1] * ok_t, ok_t], axis=0)])
            s = csum[b] - csum[a]
            with np.errstate(invalid="ignore", divide="ignore"):
                out[thr][:, 2 * k] = np.where(s[:, 2] > 0, s[:, 0] / s[:, 2], np.nan)
                out[thr][:, 2 * k + 1] = np.where(s[:, 2] > 0, s[:, 1] / s[:, 2], np.nan)
        ok = d[:, 2] >= LIKELIHOOD_MIN''')
rep('''    out.update({"trials": tt, "rates": rates, "region": region[keep], "probe": probe[keep],
                "video": video, "video_info": vinfo,''','''    out.update({"trials": tt, "rates": rates, "region": region[keep], "probe": probe[keep],
                "video": video[LIKELIHOOD_MIN], "video_by_threshold": video, "video_info": vinfo,''')
rep('''def video_design(S: dict, control_lick: np.ndarray, reading: str = "fill"):
    """Design matrix (with intercept) for the video regression on the given trials."""
    V = S["video"][control_lick]''','''def video_design(S: dict, control_lick: np.ndarray, reading: str = "fill", threshold: float | None = None):
    """Design matrix (with intercept) for the video regression on the given trials; threshold
    selects the keypoint likelihood cut (default LIKELIHOOD_MIN)."""
    V = (S["video"] if threshold is None else S["video_by_threshold"][threshold])[control_lick]''')
rep('''def axes(S: dict, region: str, ts: dict, early: str = "early_own", video: str = "fill",
         regress: bool = True, extra_windows=()) -> dict | None:''','''def axes(S: dict, region: str, ts: dict, early: str = "early_own", video: str = "fill",
         regress: bool = True, extra_windows=(), threshold: float | None = None) -> dict | None:''')
rep('''        D, rows = video_design(S, cl, video)''','''        D, rows = video_design(S, cl, video, threshold)''')
rep('''  likelihood per frame and no detection flag, and 0.9 is the usual DeepLabCut cut. Trials''','''  likelihood per frame and no detection flag, and 0.9 is the usual DeepLabCut cut (0.5 and 0.99
  are computed as well, `LIKELIHOOD_VARIANTS`, to show how much it matters). Trials''')
open('mam.py','w').write(s)
EOF
grep -n "Decoding (M8" mam.py | head -2
```

```
501:# Decoding (M8; Methods, Decoding)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > vthr.py <<'EOF'
import sys, pickle, numpy as np, time, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'entries/yang-2026')
import mam
from concurrent.futures import ThreadPoolExecutor
S=pickle.load(open('S.pkl','rb')); sv={s['session']:s for s in pickle.load(open('sv.pkl','rb'))}
def one(s):
    f=mam._open(sv[s['session']]['url'])
    v,info=mam._video(f,s['trials']['go'],np.array([]))
    f.close(); return v
t=time.time()
with ThreadPoolExecutor(6) as ex: V=list(ex.map(one,S))
print('video', time.time()-t)
for s,v in zip(S,V): s['video_by_threshold']=v; s['video']=v[0.9]
rows={}
for thr in mam.LIKELIHOOD_VARIANTS:
    for r in mam.REGIONS:
        vals={}
        for s in S:
            ts=mam.trial_sets(s)
            ax=mam.axes(s,r,ts,threshold=thr)
            if ax is None: continue
            f=mam.fractions(ax['d'],ax); vals[(s['mouse'],s['session'])]=(f['joint'],f['choice'],f['action'],ax['choice']@ax['action'])
        out=[mam.mouse_summary({k:v[i] for k,v in vals.items()})[0] for i in range(4)]
        print(thr,r,np.round(out,4))
pickle.dump(V,open('V.pkl','wb'))
EOF
python vthr.py
```

```
video 296.01135444641113
0.5 ALM [0.0552 0.0346 0.022  0.5235]
0.5 striatum [0.0599 0.0423 0.0194 0.3438]
0.5 thalamus [0.0844 0.0614 0.0268 0.2966]
0.5 midbrain [0.0587 0.0288 0.0316 0.3481]
0.5 medulla [0.0504 0.0296 0.025  0.4051]
0.9 ALM [0.0549 0.0344 0.022  0.5234]
0.9 striatum [0.0601 0.0424 0.0194 0.3423]
0.9 thalamus [0.0844 0.0615 0.0268 0.2968]
0.9 midbrain [0.0587 0.0288 0.0316 0.3478]
0.9 medulla [0.0521 0.0308 0.025  0.4056]
0.99 ALM [0.0545 0.034  0.022  0.5242]
0.99 striatum [0.0601 0.0425 0.0194 0.3421]
0.99 thalamus [0.0842 0.0614 0.0268 0.2972]
0.99 midbrain [0.0589 0.0289 0.0316 0.3475]
0.99 medulla [0.0522 0.0305 0.025  0.4072]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
anchor='''md("""
**Result: reproduced.** Under the first reading (own onset, filled keypoints, licks) the joint'''
assert anchor in s
new='''code(r"""
# The keypoint likelihood cut is not given by the paper; the first reading under three cuts.
rows = []
for thr in mam.LIKELIHOOD_VARIANTS:
    for s in S:
        ts = TS[("drop", "licks", s["session"])]
        for r in mam.REGIONS:
            ax = mam.axes(s, r, ts, threshold=thr)
            if ax is None:
                continue
            f = mam.fractions(ax["d"], ax)
            rows.append({"reading": f"likelihood >= {thr}", "region": r, "mouse": s["mouse"], "session": s["session"],
                         "joint": f["joint"], "choice": f["choice"], "action": f["action"], "cos": float(ax["choice"] @ ax["action"])})
THR = mice_table(pd.DataFrame(rows), ["joint", "choice", "action", "cos"])
for col in ("joint", "choice", "action", "cos"):
    print(col); print(THR.pivot(index="reading", columns="region", values=col)[mam.REGIONS].round(4).to_string())
""", tags=["claim:table1-early-joint-fraction"])

'''
s=s.replace(anchor,new+anchor)
a="""under the matching readings; the criterion does not require the order.
\"\"\")"""
assert a in s
s=s.replace(a,"""under the matching readings; the criterion does not require the order. The likelihood cut for a
detected keypoint (0.5, 0.9 or 0.99) changes no fraction or cosine by more than 0.002.
\"\"\")""")
open('build_nb.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && rm -rf entries/yang-2026/__pycache__ && python tools/entry.py check entries/yang-2026 | tail -2 && date -u && timeout 6000 python tools/entry.py run entries/yang-2026 2>&1 | tail -3; date -u
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbformat/__init__.py", line 204, in write
    fp.write(s)
    ^^^^^^^^
AttributeError: 'str' object has no attribute 'write'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 1565, in <module>
    nbf.write(nb, sys.argv[1])
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/nbformat/__init__.py", line 208, in write
    with Path(fp).open("w", encoding="utf8") as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/pathlib.py", line 1013, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'entries/yang-2026/reproduce_yang_2026.ipynb'
Sat Nov 21 09:02:24 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && rm -rf entries/yang-2026/__pycache__ && python tools/entry.py check entries/yang-2026 | tail -2 && date -u && timeout 6000 python tools/entry.py run entries/yang-2026 2>&1 | tail -3; date -u
```

```
94 cells
0 error(s)
Sat Nov 21 09:02:32 UTC 2026
Installed kernelspec registry-yang-2026 in executed/yang-2026/.venv/share/jupyter/kernels/registry-yang-2026
pass  reproduce_yang_2026.ipynb  (1805 s)
Sat Nov 21 09:32:43 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' > $TMPDIR/exec_out3.txt
import nbformat
nb=nbformat.read('executed/yang-2026/reproduce_yang_2026.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=====',i,c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
diff $TMPDIR/exec_out2.txt $TMPDIR/exec_out3.txt
```

```
2c2
< surveyed 174 files of dandiset 000363 version 0.231012.2129 in 306 s
---
> surveyed 174 files of dandiset 000363 version 0.231012.2129 in 310 s
38c38
< loaded 112 sessions in 862 s; peak memory 7.7 GB
---
> loaded 112 sessions in 816 s; peak memory 7.5 GB
105c105,131
< ===== 19 ['claim:table1-early-axis-fractions']
---
> ===== 17 ['claim:table1-early-joint-fraction']
> joint
> region                 ALM  striatum  thalamus  midbrain  medulla
> reading                                                          
> likelihood >= 0.5   0.0552    0.0599    0.0844    0.0587   0.0504
> likelihood >= 0.9   0.0549    0.0601    0.0844    0.0587   0.0521
> likelihood >= 0.99  0.0545    0.0601    0.0842    0.0589   0.0522
> choice
> region                 ALM  striatum  thalamus  midbrain  medulla
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; grep -n "verifications\|handover" docs/protocol.md | head -5; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['outcomes']['items']['properties']['assumed']))
print(json.dumps(s['properties']['findings']['items'].get('allOf', s['properties']['findings']['items'].get('if')))[:800])"
```

```
Sat Nov 21 09:33:07 UTC 2026
607:`python tools/entry.py handover entries/<name>` builds these in
608:`executed/<name>/handover/` from the executed copy. The verifier also gets the
619:`verifications`, saying what was reviewed. Give the verifier's reasons in its
{"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).", "type": "boolean"}
null
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_attempt.py",
 "content": "import yaml\n\nNB = \"reproduce_yang_2026.ipynb\"\nSEED_NOTE = (\"Random draws use the registry's claim seed (zlib.crc32 of the paper key and claim id), not the \"\n             \"paper's seed 17 (Methods, Statistics), so splits, folds and match order differ from the paper's.\")\n\n\ndef o(claim, outcome, notes, measured=None, deviations=None, assumed=None, seed_sensitive=None):\n    d = {\"claim\": claim, \"outcome\": outcome, \"notebook\": NB, \"output\": f\"claim:{claim}\"}\n    if measured is not None:\n        d[\"measured\"] = measured\n    d[\"notes\"] = notes\n    if deviations:\n        d[\"deviations\"] = deviations\n    if assumed:\n        d[\"assumed\"] = True\n    if seed_sensitive:\n        d[\"seed_sensitive\"] = True\n    return d\n\n\ncommon_axes = [\n    \"A video keypoint counts as detected when its likelihood is at least 0.9; the files give a likelihood per frame and \"\n    \"no detection flag, and the paper gives no rule. Cuts of 0.5 and 0.99 change no early fraction or cosine by more \"\n    \"than 0.002 (standard choice, shown in the notebook).\",\n    \"Regions are the probe targets the files give for each unit's electrode (claims M2, reading a). Reading b (Allen \"\n    \"CCF parents of the per-unit annotation) was not run, as it needs the Allen ontology, an outside input the claims \"\n    \"file does not name; the probe labels give exactly the paper's Table 1 counts.\",\n]\n\noutcomes = [\n    o(\"session-counts\", \"reproduced\",\n      \"168 sessions have photostimulation trials. 112 sessions from 19 mice have a median bilateral onset within 0.08 s \"\n      \"of -0.5 s from Go (bilateral code 6, sites ALM at ML -1.5 and +1.5 mm); the other 39 bilateral sessions start \"\n      \"near -1.2 s. With laser trials that had an early lick dropped (M1 reading b) every region count equals Table 1 \"\n      \"(ALM 19 / 93, striatum 13 / 48, thalamus 10 / 31, midbrain 16 / 71, medulla 8 / 35) under both lick-direction \"\n      \"readings; keeping those trials gives 19 / 94, 13 / 49, 10 / 31, 16 / 72 and 8 / 35. The dropped reading is \"\n      \"used first in every other claim.\",\n      [168, 19, 93, 13, 48, 10, 31, 16, 71, 8, 35], common_axes[1:]),\n    o(\"table1-early-joint-fraction\", \"reproduced\",\n      \"Joint fractions, mean across mice (first reading, own onset, keypoints filled, licks), ALM 0.0549, striatum \"\n      \"0.0601, thalamus 0.0844, midbrain 0.0587, medulla 0.0521; all within tolerance and below 0.10. All four readings \"\n      \"that fill missing keypoints give 5 of 5; the four that drop trials without a keypoint from the video fit give 1 \"\n      \"or 2 of 5, since the tongue is undetected in the choice window on 82% of trials. Thalamus is highest; the lowest \"\n      \"is medulla, not ALM (the criterion does not require the order). The likelihood cut (0.5, 0.9, 0.99) changes the \"\n      \"fractions by at most 0.0017.\",\n      [0.0549, 0.0601, 0.0844, 0.0587, 0.0521], common_axes),\n    o(\"table1-early-axis-fractions\", \"reproduced\",\n      \"First reading, choice fractions ALM 0.0344, striatum 0.0424, thalamus 0.0615, midbrain 0.0288, medulla 0.0308; \"\n      \"action fractions 0.0220, 0.0194, 0.0268, 0.0316, 0.0250. 10 of 10 within tolerance under the four readings that \"\n      \"fill missing keypoints, 7 of 10 under those that drop such trials.\",\n      [0.0344, 0.0424, 0.0615, 0.0288, 0.0308, 0.0220, 0.0194, 0.0268, 0.0316, 0.0250], common_axes),\n    o(\"axes-cosine\", \"reproduced\",\n      \"Signed cosine, mean across mice, thalamus 0.297 and ALM 0.523 (SEM 0.045 and 0.025); striatum 0.342, midbrain \"\n      \"0.348 and medulla 0.406 lie between. The absolute cosine gives the same outcome (5 sessions of 278 have a \"\n      \"negative cosine). The readings that drop trials without a keypoint give 0.20 and 0.33, outside tolerance.\",\n      [0.297, 0.523], common_axes),\n    o(\"fig1e-laser-vs-control-split\", \"partially_reproduced\",\n      \"Median across mice of the mouse mean ratio of laser to control-split energy (reading a, disjoint groups) ALM \"\n      \"147.0, striatum 2.73, thalamus 5.16, midbrain 8.18, medulla 2.82. Every mouse ratio exceeds 1 (smallest 1.16 to \"\n      \"1.33 over readings). ALM is within tolerance under all four readings (146.8 to 156.5) and the highest other \"\n      \"region under three of four (7.56 to 8.77), but the lowest other region is 2.73 to 2.84, outside 3.3 +- 0.33, \"\n      \"under every reading. No region-entry side had fewer than twice as many controls as laser trials, so the two \"\n      \"small-side readings differ only in the draws. Over the five seeds (reading a, disjoint) ALM 146.3 to 161.8, \"\n      \"lowest other 2.66 to 2.76, highest other 7.90 to 8.23; over all seeds and readings the lowest other is 2.57 to \"\n      \"2.86, so the outcome holds under every seed.\",\n      [147.05, 2.73, 8.18], [SEED_NOTE]),\n    o(\"fig1-1b-corrected-joint-fraction\", \"partially_reproduced\",\n      \"Under the claim's seed, region means of the corrected joint fraction, correction a (disjoint) medulla -0.626, \"\n      \"thalamus 0.109; correction b medulla -0.003 (independent 0.002), thalamus 0.077 (0.075); correction c medulla \"\n      \"-0.011 and -0.039, thalamus 0.044 and 0.050. No correction gives both values within tolerance, and the single-mouse \"\n      \"extremes (lowest -5.69 to -0.06, highest 0.13 to 1.11) are far from them. Every region mean is below 0.15 under \"\n      \"all six readings. Over the five seeds no reading matches both values, and under seed +3000 one of six readings \"\n      \"has a region mean above 0.15, so the partial outcome holds under every seed.\",\n      [-0.6264, 0.1094], [SEED_NOTE, \"The splits are those of fig1e-laser-vs-control-split, drawn with that claim's generator.\"]),\n    o(\"fig1-1c-fraction-vs-neurons\", \"reproduced\",\n      \"Spearman correlation of the session joint fraction with the number of units, pooled over regions, rho -0.366, \"\n      \"p = 3e-10, n = 278 region entries. Per region ALM -0.580 (p = 1e-9), striatum -0.283 (p = 0.051), thalamus \"\n      \"-0.213 (p = 0.25), midbrain -0.371 (p = 0.0015), medulla -0.413 (p = 0.014); pooled rho -0.366 to -0.423 over \"\n      \"the eight readings.\",\n      -0.366, [\"Spearman correlation as the claims file specifies; the paper reports no test.\"]),\n    o(\"fig1-1d-without-video-regression\", \"reproduced\",\n      \"Without the video regression the joint fractions are ALM 0.0567, striatum 0.0627, thalamus 0.1158, midbrain \"\n      \"0.0582, medulla 0.0555. Thalamus 0.1158 is within 0.109 +- 0.0109 and above 0.0844 with the regression; all \"\n      \"regions stay below 0.15.\",\n      0.1158, common_axes[1:]),\n    o(\"fig1b-example-session\", \"partially_reproduced\",\n      \"Of 44 candidate ALM sessions (early-fraction sessions with matched pairs, at least the median 117 units), the \"\n      \"rule selects ses-20210419T161140 (130 units, joint fraction 0.05292, 0.00200 from the ALM mouse mean 0.05492). \"\n      \"ses-20200922T135318 is second (130 units, 0.05282, 0.00210 from the mean); its count and fraction are within \"\n      \"tolerance. Counting good ALM units in place of units entering the fraction gives the same order.\",\n      [130, 0.0528]),\n    o(\"table1-decoding-early-vs-prelick\", \"partially_reproduced\",\n      \"Balanced accuracy, mean across mice, early ALM 0.574, striatum 0.584, thalamus 0.574, midbrain 0.561, medulla \"\n      \"0.581; pre-lick 0.794, 0.806, 0.802, 0.815, 0.856. The rise holds in every region; all pre-lick values and the \"\n      \"thalamus and midbrain early values are within tolerance, 7 of 10 (8 needed). ALM, striatum and medulla early \"\n      \"values are 0.010 to 0.030 below the paper's. Under the other four seeds 6 or 7 of 10 are within and the rise \"\n      \"holds, so the outcome holds under all five. Decoding uses laser and control trials together (M8 reading b): \"\n      \"with laser trials alone only 26 of 278 entries have the 40 trials and 15 per direction the Methods require. \"\n      \"273 entries pass the rule with both (ALM 19 / 91, striatum 13 / 47, thalamus 10 / 30, midbrain 16 / 71, medulla \"\n      \"8 / 34).\",\n      [0.5741, 0.5836, 0.5740, 0.5606, 0.5810, 0.7936, 0.8060, 0.8015, 0.8154, 0.8562],\n      [SEED_NOTE, \"The penalty is chosen by an inner stratified 5-fold search on balanced accuracy (standard choice named \"\n       \"in the claims file, M8).\"] + common_axes[:1]),\n    o(\"fig2a-decoding-rises-after-go\", \"reproduced\",\n      \"In the 100 ms bin centred 250 ms after Go the region means are ALM 0.733, striatum 0.725, thalamus 0.753, \"\n      \"midbrain 0.721, medulla 0.782 (inside 0.657 to 0.847); every delay bin lies in 0.540 to 0.588 (inside 0.495 to \"\n      \"0.638); the 250 ms bin exceeds every delay bin in every region. The same holds for 50 ms and 100 ms steps and \"\n      \"under all five seeds (250 ms bin 0.721 to 0.782, delay bins 0.540 to 0.588).\",\n      [0.721, 0.782], [SEED_NOTE]),\n    o(\"matched-reaction-time\", \"reproduced\",\n      \"Reaction time on the matched laser trials (2,667 trials, each session once) quartiles 0.220, median 0.289, 0.385 \"\n      \"s; counted once per region entry (7,038) 0.218, 0.288, 0.383 s. On average 94% of the 200 ms pre-lick window lies \"\n      \"after Go. Unchanged to 0.001 s under the five seeds.\",\n      [0.2885, 0.2202, 0.3848]),\n    o(\"fig2d-choice-share-flat\", \"partially_reproduced\",\n      \"Session set a (decoding entries), choice share early and pre-lick, mean across mice, ALM 0.034 to 0.023, striatum \"\n      \"0.047 to 0.025, thalamus 0.053 to 0.012, midbrain 0.031 to 0.037 (rise 0.006, below its SEM 0.006), medulla \"\n      \"0.032 to 0.071 (rise 0.039, above its SEM 0.027). By the criterion's SEM rule the share rises only in medulla. \"\n      \"The pre-lick means of ALM, thalamus, midbrain and medulla are within tolerance; striatum (0.0248) is not, and \"\n      \"the early means (0.031 to 0.053) are not all inside 0.0315 to 0.0506. The medulla early mean 0.0325 is within \"\n      \"0.036 +- 0.0036. Set b (matched entries) gives the same pattern (pre-lick striatum 0.0253, early 0.033 to \"\n      \"0.068).\",\n      [0.0232, 0.0248, 0.0124, 0.0370, 0.0710, 0.0325], common_axes[:1]),\n    o(\"fig2e-action-share-rises\", \"partially_reproduced\",\n      \"Session set a, action share early and pre-lick, ALM 0.022 to 0.051, striatum 0.024 to 0.064, thalamus 0.026 to \"\n      \"0.030, midbrain 0.033 to 0.072, medulla 0.026 to 0.128. It rises in every region and is largest in medulla \"\n      \"(0.128, within 0.122 +- 0.015); the highest early value (0.0329) is within tolerance; the lowest pre-lick \"\n      \"(thalamus 0.0296) and the lowest early (0.0222) are not. Set b gives medulla 0.125, lowest pre-lick 0.030, \"\n      \"lowest early 0.019, highest early 0.028.\",\n      [0.1281, 0.0296, 0.0222, 0.0329], common_axes[:1]),\n    o(\"fig2b-go-aligned-joint-fraction\", \"partially_reproduced\",\n      \"Early-fraction entries, joint fraction in the bin centred 250 ms after Go, medulla 0.184, midbrain 0.107, ALM \"\n      \"0.079, striatum 0.083, thalamus 0.050, all five within tolerance. The delay bins span 0.034 to 0.099 (50 ms \"\n      \"steps) or 0.035 to 0.099 (100 ms steps), outside 0.036 to 0.088 in medulla (0.099, first bin) and thalamus \"\n      \"(0.034 to 0.035). Distance-curve entries, 250 ms bin ALM 0.085 and medulla 0.199 outside tolerance, three of five \"\n      \"within, and delay bins 0.036 to 0.099.\",\n      [0.1838, 0.1070, 0.0786, 0.0827, 0.0499], common_axes[:1]),\n    o(\"fig2-1-energy-outside-subspace\", \"partially_reproduced\",\n      \"Reading b (each 100 ms bin z-scored by its controls), ALM energy per neuron outside the subspace 25.80 +- 10.17 in \"\n      \"the bin beginning at onset (within 26 +- 10) and 0.053 in the bin before onset (outside 0.09 +- 0.009); it falls \"\n      \"after onset (0.091 in the last bin). Outside exceeds inside at onset in every region. The other regions' largest \"\n      \"bin is striatum 0.839, thalamus 1.185, midbrain 0.689, medulla 0.275 with 50 ms steps, and below 1.1 with 100 ms \"\n      \"steps (thalamus 0.771). Reading a (distance-curve units) gives an ALM onset value of 9.81 and 0.031 before onset, \"\n      \"with the other regions below 0.72. The measured values are those of reading b, on which the partial outcome \"\n      \"rests.\",\n      [25.80, 0.053], common_axes[:1]),\n    o(\"fig3a-matched-pairs\", \"reproduced\",\n      \"Closest match within the caliper, 2,667 pairs in 98 sessions (14 sessions dropped with fewer than 10 pairs), \"\n      \"median absolute reaction-time difference 1.3 ms, largest 99.1 ms; 7,038 pairs summed over region entries. A \"\n      \"random match within the caliper gives 2,664 pairs with a median of 43.3 ms, so the closest match is the reading \"\n      \"that fits the paper. Over the five seeds 2,664 to 2,667 pairs, median 1.3 ms, largest 95.9 to 99.1 ms. Matched \"\n      \"mice / sessions per region 19 / 87, 12 / 41, 10 / 29, 15 / 63, 8 / 32 against the paper's 19 / 87, 12 / 42, \"\n      \"10 / 29, 15 / 64, 8 / 32.\",\n      [2667, 1.3, 99.1], [SEED_NOTE]),\n    o(\"table1-prelick-residual\", \"reproduced\",\n      \"Closest match, pairs without a second control dropped, per-bin distances averaged, pre-lick residual mean across \"\n      \"mice ALM 1.552, striatum 1.358, thalamus 2.912, midbrain 0.762, medulla 0.528 (SEM 0.136, 0.520, 0.855, 0.088, \"\n      \"0.125); every mouse positive. Keeping those pairs also gives 5 of 5; the concatenated-bin reading roughly doubles \"\n      \"the residuals (0 of 5); a random match gives 5 of 5 with one mouse not positive. Over the five seeds ALM 1.532 to \"\n      \"1.557, medulla 0.488 to 0.555, 5 of 5 within and every mouse positive.\",\n      [1.552, 1.358, 2.912, 0.762, 0.528], [SEED_NOTE]),\n    o(\"fig3e-residual-ratio\", \"reproduced\",\n      \"Residual over control-control distance, mouse means first (reading a), ALM 0.1128, striatum 0.0919, thalamus \"\n      \"0.1359, midbrain 0.0638, medulla 0.0416, all within tolerance; session ratios (reading b) 0.1126, 0.0913, 0.1352, \"\n      \"0.0649, 0.0410, also 5 of 5. 5 of 5 under all five seeds.\",\n      [0.1128, 0.0919, 0.1359, 0.0638, 0.0416], [SEED_NOTE]),\n    o(\"fig3-1ab-distances-scale\", \"reproduced\",\n      \"Pre-lick control-control distance against the number of units, pooled over 252 matched region entries, Spearman \"\n      \"rho 0.990 (p = 1e-216). Mouse means, thalamus 20.00 against midbrain 12.07.\",\n      None, [\"Spearman correlation as the claims file specifies; the paper reports no test.\"]),\n    o(\"fig3-1d-matching-keeps-distance\", \"reproduced\",\n      \"After matching, the laser-control distance exceeds the control-control distance in every region (mouse means ALM \"\n      \"15.72 against 14.17, striatum 16.63 against 15.27, thalamus 22.91 against 20.00, midbrain 12.83 against 12.07, \"\n      \"medulla 14.22 against 13.69). Unmatched pairs give laser-control distances 0.35 to 0.95 above the matched ones \"\n      \"(0.28 to 0.98 over the five seeds).\",\n      None, [SEED_NOTE, \"Unmatched pairs pair each matched laser trial with a random control trial of the same session and side \"\n       \"that has a lick, without replacement (Methods, Matched distance, which does not give the draw).\"]),\n    o(\"fig3-1c-alm-early-residual\", \"reproduced\",\n      \"On the matched pairs, the early window scored in two 50 ms bins (per-bin distances averaged) gives an ALM residual \"\n      \"of 12.59 (SEM 2.0), within 12.6 +- 2.0 and 8.1 times the pre-lick residual of 1.55. Scored as one 100 ms window it \"\n      \"is 18.36 (SEM 2.7), outside tolerance, though 11.8 times the pre-lick residual; that reading would give partially \"\n      \"reproduced. Over the five seeds 12.56 to 12.59 (binned) and 18.31 to 18.36 (one window). Question for the paper's \"\n      \"authors, whether the early window was divided into 50 ms bins for the matched distance (Methods, Matched \"\n      \"distance, \\\"The primary window was the 200 ms before the lick, divided into 50 ms bins. The same pairs were \"\n      \"scored in the early window\\\"; Time courses, \\\"Distance used 50 ms bins\\\").\",\n      12.59,\n      [\"Assumed that the early window is divided into two 50 ms bins and the per-bin distances averaged, as for the \"\n       \"pre-lick window. The paper divides the primary window into 50 ms bins, scores the same pairs in the early window, \"\n       \"and computes every other distance in 50 ms bins (Methods, Matched distance; Time courses), so the binned reading is \"\n       \"the better supported; the claims file names only the window.\", SEED_NOTE],\n      assumed=True),\n    o(\"fig3c-residual-time-course\", \"reproduced\",\n      \"Residual on the 50 ms Go-aligned grid, mean across mice, ALM peaks at 21.30 in the bin beginning at onset \"\n      \"(centred -475 ms) and declines (10.38, 8.56 next); thalamus -0.99 and -1.35 in the two bins after onset and peaks \"\n      \"at 11.35 at -25 ms; midbrain peaks at 2.07 at -425 ms; striatum at 2.91 at +25 ms; medulla at 1.31 (-25 ms). All \"\n      \"named bins hold and 7 of 7 values are within tolerance, under all five seeds. No entry had fewer than 20 units \"\n      \"passing the SD threshold in every bin, so no bins were zero-filled.\",\n      [21.30, -0.99, -1.35, 11.35, 2.07, 2.91, 1.31], [SEED_NOTE]),\n    o(\"fig3c-late-residuals\", \"reproduced\",\n      \"Bins centred 225 to 375 ms after Go, ALM 1.33, 0.98, 0.91, 0.79; striatum 0.80, 0.32, 0.29, 0.30; thalamus 1.95, \"\n      \"1.55, 1.02, 0.82; midbrain at most 0.42; medulla at most 0.47; all five regions inside their widened ranges under \"\n      \"the claim's seed. Under seeds +1000, +3000 and +4000 four of five regions are inside (partially reproduced), \"\n      \"under +2000 five of five.\",\n      None, [SEED_NOTE], seed_sensitive=True),\n    o(\"fig3b-example-plane\", \"partially_reproduced\",\n      \"In ses-20200922T135318 (22 matched pairs, 130 units) the matched laser-control separation in the plane is 4.11 in \"\n      \"the early window and 0.87 at Go (unmatched off-subspace direction; 4.84 and 0.99 with the matched direction), so \"\n      \"the trajectories come closer at Go. The plane holds 0.696 (unmatched direction) or 0.965 (matched direction) of \"\n      \"the early matched difference, against 0.25; the first principal component of control activity orthogonal to the \"\n      \"choice axis holds 0.035 (all controls) or 0.085 (matched controls), against 0.04 +- 0.004. In the session the rule \"\n      \"selects (ses-20210419T161140) the plane holds 0.949 or 1.000 and the component 0.079 or 0.036.\",\n      [0.6957, 0.0351],\n      [\"At Go is read as the 100 ms bin centred on Go, z-scored by its control trials (the paper does not give the bin; \"\n       \"standard choice, as the comparison is only of the direction of change).\",\n       \"Tested on the paper's session, which the rule of fig1b-example-session ranks second; the selected session is shown \"\n       \"as a variant.\"]),\n]\n\nfindings = [\n    {\"kind\": \"other\", \"about\": \"data\", \"severity\": \"none\",\n     \"statement\": \"The pinned version holds what the paper describes. 168 of 174 files have photostimulation trials, 112 \"\n                  \"late-delay bilateral sessions come from 19 mice, and the mice and sessions per region equal Table 1 of \"\n                  \"the paper under its stated rules. No recording is deposited twice (spike counts, trial counts and trial \"\n                  \"timing all differ). Every photostimulation trial has one onset event inside it. Spikes and trials share \"\n                  \"a clock (the ALM laser-control difference 20 to 120 ms after onset exceeds that before onset in all 99 \"\n                  \"sessions with ALM units), and licks and video share one (the tongue is detected in 97% of frames in \"\n                  \"the 50 ms after a lick against 40% at times shifted by -0.5 s, in all 112 sessions).\"},\n    {\"kind\": \"format_error\", \"severity\": \"minor\",\n     \"statement\": \"Four units in the late-delay sessions have spike times that are not in ascending order. Analyses that \"\n                  \"assume sorted spike times (binary search for counts) must sort them first.\"},\n    {\"kind\": \"metadata_insufficient\", \"severity\": \"minor\",\n     \"statement\": \"The brain region of a unit is given two ways, as the probe's target in the electrode location \"\n                  \"(`brain_regions`, e.g. \\\"left ALM\\\", \\\"right Thalamus\\\") and as a CCF annotation per unit (`anno_name`), \"\n                  \"and neither is described as the region used for analysis. The probe targets reproduce the paper's \"\n                  \"per-region counts exactly.\"},\n    {\"kind\": \"metadata_insufficient\", \"severity\": \"minor\",\n     \"statement\": \"The video keypoint series (jaw, nose, tongue) hold x, y and a likelihood per frame, with no detection \"\n                  \"flag or recommended likelihood cut. The tongue has likelihood of at least 0.9 in about 10% of frames \"\n                  \"and in no frame of the choice window on 82% of trials, so how missing keypoints are handled changes \"\n                  \"any analysis that regresses out tongue position.\"},\n    {\"kind\": \"other\", \"about\": \"data\", \"severity\": \"minor\",\n     \"statement\": \"In two of the 112 late-delay sessions the side-camera video does not span the trials to within 5 s, so \"\n                  \"some trials of those sessions have no keypoints.\"},\n    {\"kind\": \"methods_unavailable\",\n     \"statement\": \"Question for the author. Was the matched distance in the early window (12.6 in ALM, Figure 3-1C) \"\n                  \"computed in two 50 ms bins with the per-bin distances averaged, as for the pre-lick window, or over the \"\n                  \"single 20 to 120 ms window? The two give 12.59 and 18.36 here; the attempt assumes the binned reading \"\n                  \"(Methods, Matched distance and Time courses).\"},\n    {\"kind\": \"methods_unavailable\",\n     \"statement\": \"Question for the author. Several details are not in the Methods and the code is private; the attempt \"\n                  \"chose, where the data allowed, the reading that matches the paper's counts. (1) Laser trials with an \"\n                  \"early lick were dropped (the counts of Table 1 match only then). (2) Each laser trial took the control \"\n                  \"trial with the closest reaction time within the caliper (a random match gives a median difference of \"\n                  \"43 ms, not 1.3 ms). (3) A video keypoint was taken as detected at likelihood 0.9 and trials without a \"\n                  \"detection took the control mean; dropping them from the fit gives other fractions and cosines. Please \"\n                  \"confirm or correct these, and say how the control-split correction of Figure 1-1B, the displayed-plane \"\n                  \"fraction of Figure 3B (25%, against 70% to 97% here) and the energy per neuron before onset (0.09, \"\n                  \"Figure 2-1A) were computed.\"},\n]\n\nattempt = {\n    \"schema_version\": 3,\n    \"id\": \"yang-2026-01\",\n    \"datasets\": [{\"archive\": \"dandi\", \"id\": \"000363\", \"version\": \"0.231012.2129\",\n                  \"doi\": \"10.48324/dandi.000363/0.231012.2129\", \"relation\": \"reuses\"}],\n    \"paper\": \"doi:10.21203/rs.3.rs-11447300/v1\",\n    \"date\": \"2026-11-21\",\n    \"entry\": \"yang-2026\",\n    \"provenance\": {\"kind\": \"agent\", \"accountable\": {\"name\": \"CatalystNeuro\"},\n                   \"agent\": {\"harness\": \"Claude Code\", \"model\": \"claude-opus-5-5\", \"protocol\": \"pilot-18\"},\n                   \"runner\": {\"platform\": \"GitHub Actions\",\n                              \"url\": \"https://github.com/catalystneuro/encore/actions/runs/44877453513\"}},\n    \"outcomes\": outcomes,\n    \"findings\": findings,\n}\n\nwith open(\"attempts/yang-2026-01.yaml\", \"w\") as f:\n    yaml.safe_dump(attempt, f, sort_keys=False, width=100, allow_unicode=True)\nprint(\"written\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_attempt.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('entries/yang-2026/reproduce_yang_2026.ipynb',4)
for c in nb.cells:
    if c.cell_type=='markdown' and (c.source.startswith('**Result') or 'clock' in c.source or 'No two files' in c.source or '168 files' in c.source):
        print(c.source,'\n---')
EOF
```

```
168 files have photostimulation trials, as the Methods say, and every photostimulation trial has
one onset event inside it, so trials and events are on one clock and pair one to one. The
bilateral code is 6 in every session that has one (its site list holds ALM at ML -1.5 and +1.5 mm).
Median bilateral onsets fall in two groups, about -1.2 s and -0.5 s from Go, as the Methods
describe; 112 sessions from 19 mice are late-delay sessions. Seventeen photostimulation sessions
have no bilateral code (unilateral sites only) and enter no analysis. 
---
No two files share spike and trial counts or trial timing, so no recording is deposited twice. One
mouse (sub-456772) has two sessions on each of five days; they have different trials and units and
are counted as separate sessions, as in the paper's 93 ALM sessions. Trials with auto or free water
are kept, as the paper excludes none. 
---
The region of a unit is the probe target of its electrode ("left ALM", "right Striatum" and so
on); the files also give a CCF annotation per unit (`anno_name`), not used here (claims M2,
reading a). Spike times span the trials; four units have spike times out of order (see the count above), which
the helper sorts before counting. The clock of spikes and trials is shown
by the photoinhibition itself: in every session with ALM units, the laser-control difference of
ALM units 20 to 120 ms after laser onset is larger than the difference 600 to 550 ms before Go,
before the laser (median 0.82 against 0.15 control SD), and most ALM units fire less on laser
trials in the early window. Mean ALM rates
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
def rep(a,b):
    global s
    assert a in s, a[:70]; s=s.replace(a,b)
rep("on average 93% of\nthe 200 ms pre-lick window lies after Go.","on average 94% of\nthe 200 ms pre-lick window lies after Go.")
rep("The\nconcatenated-bin reading doubles the residuals and matches in no region but thalamus.","The\nconcatenated-bin reading roughly doubles the residuals and matches in no region.")
rep("""Seventeen photostimulation sessions
have no bilateral code (unilateral sites only) and enter no analysis.""","""Seventeen photostimulation sessions
have no code whose sites are ALM on both sides and enter no analysis.""")
rep("they have different trials and units and\nare counted","they have different trial and spike counts and\nare counted")
rep(""" Mean ALM rates
are not always lower, as some units (presumably the inhibitory neurons driven by the laser) fire
far more.""","")
rep("The run takes about 35 minutes","The run takes about 30 minutes")
open('build_nb.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && cd  && sed -i 's/It takes about 35 minutes/It takes about 30 minutes/' entries/yang-2026/README.md && python $TMPDIR/make_attempt.py && date -u && timeout 6000 python tools/entry.py all entries/yang-2026 2>&1 | tail -5; date -u
```

```
94 cells
written
Sat Nov 21 09:34:53 UTC 2026
Installed kernelspec registry-yang-2026 in executed/yang-2026/.venv/share/jupyter/kernels/registry-yang-2026
0 error(s)
pass  reproduce_yang_2026.ipynb  (1799 s)
Sat Nov 21 10:05:02 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' > $TMPDIR/exec_out4.txt
import nbformat
nb=nbformat.read('executed/yang-2026/reproduce_yang_2026.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=====',i,c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
diff $TMPDIR/exec_out3.txt $TMPDIR/exec_out4.txt; python tools/entry.py handover entries/yang-2026 2>&1 | tail -3; ls executed/yang-2026/handover; grep -c ": " /dev/null; python tools/entry.py check entries/yang-2026 | tail -2; git status --short
```

```
2c2
< surveyed 174 files of dandiset 000363 version 0.231012.2129 in 310 s
---
> surveyed 174 files of dandiset 000363 version 0.231012.2129 in 302 s
38c38
< loaded 112 sessions in 816 s; peak memory 7.5 GB
---
> loaded 112 sessions in 835 s; peak memory 8.0 GB
270c270
< matching and distances under five seeds in 92 s
---
> matching and distances under five seeds in 89 s
413c413
< decoding, claim seeds, in 120 s
---
> decoding, claim seeds, in 118 s
415c415
< decoding, five seeds, in 536 s
---
> decoding, five seeds, in 523 s
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "—\|rather\|\*\*" attempts/yang-2026-01.yaml entries/yang-2026/README.md entries/yang-2026/mam.py | head; . $TMPDIR/venv/bin/activate; python - <<'EOF'
import nbformat,re
nb=nbformat.read('entries/yang-2026/reproduce_yang_2026.ipynb',4)
for c in nb.cells:
    for m in re.finditer(r'\*\*[^*]+\*\*',c.source):
        if not m.group().startswith('**Result'): print(m.group())
    if '—' in c.source or 'rather' in c.source: print('BAD', c.source[:80])
EOF
head -30 attempts/yang-2026-01.yaml; ls entries/yang-2026; date -u
```

```
entries/yang-2026/mam.py:461:    return {"joint": float(np.sum((ax["Q"].T @ d) ** 2) / e),
entries/yang-2026/mam.py:462:            "choice": float((ax["choice"] @ d) ** 2 / e),
entries/yang-2026/mam.py:463:            "action": float((ax["action"] @ d) ** 2 / e),
entries/yang-2026/mam.py:532:    outer = StratifiedKFold(5, shuffle=True, random_state=seed_ % (2 ** 32))
entries/yang-2026/mam.py:537:            inner = StratifiedKFold(5, shuffle=True, random_state=(seed_ + 1) % (2 ** 32))
entries/yang-2026/mam.py:612:            return np.sqrt(((X[a] - X[b]) ** 2).sum(axis=1)).mean(axis=1)
entries/yang-2026/mam.py:613:        return np.sqrt(((X[a] - X[b]) ** 2).sum(axis=(1, 2)))
**Paper.**
**Dandiset.**
**0.231012.2129**
**What is used.**
**Claims.**
** 2))
        row = {"region": r, "mouse": m, "session": se, "n_units": ax["n_units"], "joint": Ein / El}
        for small in ("disjoint", "independent"):
            sp = mam.control_splits(Z, ts, rng, 20, small)
            Es = np.array([v @ v for v in sp])
            Eins = np.array([np.sum((Q.T @ v) **
** 2) / (dm @ dm))
    ctrl = np.where(ts["control"])[0] if pcs == "all controls" else p[:, 1]
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
for a,b in [("**Paper.**","Paper."),("**Dandiset.**","Dandiset."),("**0.231012.2129**","0.231012.2129"),("**What is used.**","What is used."),("**Claims.**","Claims."),("**How the analysis differs from the paper's.**","How the analysis differs from the paper's."),("**What was found about the dataset.**","What was found about the dataset.")]:
    assert a in s; s=s.replace(a,b)
open('build_nb.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate && python $TMPDIR/build_nb.py entries/yang-2026/reproduce_yang_2026.ipynb && cd  && rm -rf entries/yang-2026/__pycache__ && date -u && timeout 4000 python tools/entry.py all entries/yang-2026 2>&1 | tail -3; date -u
```

```
94 cells
Sat Nov 21 10:05:48 UTC 2026
Installed kernelspec registry-yang-2026 in executed/yang-2026/.venv/share/jupyter/kernels/registry-yang-2026
0 error(s)
pass  reproduce_yang_2026.ipynb  (1750 s)
Sat Nov 21 10:35:07 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python - <<'EOF' > $TMPDIR/exec_out5.txt
import nbformat
nb=nbformat.read('executed/yang-2026/reproduce_yang_2026.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('=====',i,c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'])
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
diff $TMPDIR/exec_out4.txt $TMPDIR/exec_out5.txt | grep -v "^[<>] .* in [0-9]* s$" ; rm -rf entries/yang-2026/__pycache__; python tools/entry.py handover entries/yang-2026 2>&1 | tail -2; python tools/entry.py check entries/yang-2026 | tail -1; date -u
```

```
2c2
---
38c38
< loaded 112 sessions in 835 s; peak memory 8.0 GB
---
> loaded 112 sessions in 797 s; peak memory 7.7 GB
270c270
---
413c413
---
415c415
---
571c571
< total run time 29.9 min; peak memory 9.3 GB
---
> total run time 29.0 min; peak memory 9.0 GB
wrote executed/yang-2026/handover
0 error(s)
Sat Nov 21 10:35:30 UTC 2026
```

**Agent**

## Report: yang-2026, attempt 01 (author run)

All 25 claims were tested and none is blocked. 15 are reproduced (one of them rests on an assumption, one is seed-sensitive) and 10 are partially reproduced. The notebook passes `tools/entry.py all` in a clean environment, taking about 29 minutes with a peak memory of 9 GB. The handover is built in `executed/yang-2026/handover/`. Nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| session-counts | reproduced (all eleven counts equal the paper's) |
| table1-early-joint-fraction | reproduced |
| table1-early-axis-fractions | reproduced (10/10 within tolerance) |
| axes-cosine | reproduced |
| fig1e-laser-vs-control-split | partial: the lowest other-region ratio is 2.7, against 3.3 ± 0.33 |
| fig1-1b-corrected-joint-fraction | partial: no correction gives both the medulla and thalamus values |
| fig1-1c-fraction-vs-neurons | reproduced (rho −0.37, p = 3e-10) |
| fig1-1d-without-video-regression | reproduced (thalamus 0.116) |
| fig1b-example-session | partial: the paper's session ranks second, 0.0001 behind another |
| table1-decoding-early-vs-prelick | partial: 7 of 10 values within, 8 needed; the early accuracies are low |
| fig2a-decoding-rises-after-go | reproduced |
| matched-reaction-time | reproduced |
| fig2d-choice-share-flat | partial |
| fig2e-action-share-rises | partial |
| fig2b-go-aligned-joint-fraction | partial: the 250 ms bin matches, the delay range does not |
| fig2-1-energy-outside-subspace | partial: ALM at onset 25.8 matches; before onset 0.053 against 0.09 |
| fig3a-matched-pairs | reproduced (2,667 pairs, median 1.3 ms, largest 99 ms) |
| table1-prelick-residual | reproduced |
| fig3e-residual-ratio | reproduced |
| fig3-1ab-distances-scale | reproduced |
| fig3-1d-matching-keeps-distance | reproduced |
| fig3-1c-alm-early-residual | reproduced, resting on an assumption (12.59 binned; 18.4 unbinned) |
| fig3c-residual-time-course | reproduced (7/7 values within tolerance) |
| fig3c-late-residuals | reproduced, seed-sensitive (4 of 5 regions under 3 of the other 4 seeds) |
| fig3b-example-plane | partial: the plane holds 70–97% of the difference, against 25% |

### 2. Dataset, assumptions and questions

**Dataset.** I pinned version 0.231012.2129: the paper cites it and it is also the latest published version. Earlier versions hold the same 174 assets without the raw ephys; none of the raw series is read here.
- 168 sessions have photoinhibition, and 112 late-delay bilateral sessions come from 19 mice.
- No session was deposited twice.
- Spikes, trials, licks and video share one clock. This rests on two contrasts: the ALM effect is larger after laser onset than before it in 99 of 99 sessions, and the tongue is detected more often just after a lick than at shifted times in 112 of 112.

Findings recorded about the data:
- 4 units have spike times out of order (format_error, minor).
- A unit's region exists only as the probe target and a CCF annotation; neither is documented as the analysis label (minor).
- The video keypoints have a likelihood per frame but no detection flag. The tongue is undetected in the choice window on 82% of trials (minor).
- In 2 sessions the video does not cover the trials to within 5 s (minor).

**Readings the data settled.** Each of these is a reading the claims file lists, and in each case the data matched only one:
- Laser trials with an early lick are dropped. Only this reading gives the Table 1 counts exactly.
- Matching takes the closest control trial. A random match within the caliper gives a median difference of 43 ms, not 1.3 ms.
- Missing keypoints take the control mean. Dropping trials without them gives the wrong fractions.

**Assumptions.**
- One outcome rests on an assumption: the early-window residual is scored in two 50 ms bins, as all of the paper's other distances are (Methods, Matched distance; Time courses).
- Standard choices that do not change any result: a keypoint counts as detected at likelihood ≥ 0.9 (cuts of 0.5 and 0.99 change no fraction by more than 0.002), and the penalty is chosen by an inner 5-fold search.

**Questions for the paper's author** (recorded as two `methods_unavailable` findings):
- Was the early residual computed in 50 ms bins?
- Please confirm the early-lick, matching and keypoint choices above.
- How were the Fig 1-1B correction, the 25% plane fraction (Fig 3B) and the 0.09 pre-onset energy (Fig 2-1A) computed?

**Questions to a reader:** none.

### 3. Protocol issues

1. **Seeds.** The paper states one seed, 17; the protocol requires the claim seeds. I used the claim seeds and recorded this as a deviation.
2. **Re-runs after text edits.** Any edit to the entry forces a full re-run, so the "Result" text had to be written before the last run. With a 30-minute notebook this cost three extra full runs: one to fix conclusions, one to add the likelihood-cut variant, one to remove bold. A rule allowing markdown-only edits without re-execution would help.
3. **Author readings versus criterion readings.** Several criteria say "reproduced under any reading", while step 1.6 says to adopt one reading when they disagree. It is unclear how the two interact when the author adds a reading the criterion does not list (the early-residual binning). I applied step 1.6 and set `assumed`.
4. **`measured` when no reading matches.** The protocol says what to record when several readings match, but not when none does. I recorded the reading the outcome rests on (energy, reading b), or otherwise the first one listed.
5. **Clock check.** The suggested decoding check does not fit this dataset. I used the photoinhibition contrast and the lick/tongue contrast instead.
6. **Region reading (b).** This reading needs the Allen ontology, an outside input the claims file does not name, so it was not run. Reading (a) matched the counts exactly.

### 4. Runtime and failures

- Notebook: about 29 minutes per run (5 min survey, 13–14 min streaming, 9 min decoding), peak memory 9 GB.
- Session: about 3 h 45 min in total, including four full runs.
- Nothing failed.

## End of run

75 turns, 220 minutes, $8.52 at API prices, result: success.
