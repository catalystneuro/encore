# 001199 · author · run 41291066974

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper claims/001199 entries attempts | head -80
```

```
<persisted-output>
Output too large (37.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/152a222b-09fc-4b20-98da-7f351653ba41/tool-results/b2ri8geb6.txt

Preview (first 2KB):
Sun Nov  1 09:03:55 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/152a222b-09fc-4b20-98da-7f351653ba41/tool-results/b2ri8geb6.txt"
}
```

```
1	Sun Nov  1 09:03:55 UTC 2026
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
[... 699 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper claims/001199 entries/001453-fouke-2025 claims/001453 questions | head -50; wc -c paper/* claims/001199/*; cat docs/archives.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat README.md | head -120; echo ----; wc -l docs/design.md
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
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/design.md
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
[... 251 more lines not kept]
```

**Agent**

Now the claims file and the paper.

**Agent calls Read**

```json
{
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025, on dandiset 001199.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
3	# docs/protocol.md, version pilot-10.
4	#
5	# Text read: the version of record as served by PubMed Central (paper/10.1523-jneurosci.2218-24.2025.txt,
6	# fetched by paper-text-fetcher), with Abstract, Significance Statement, Introduction, Materials and
7	# Methods, Results, all eleven figure legends and Discussion. The paper has no supplement and no PDF
8	# was supplied. The text lost the equation of the directional STTC (Methods, Directional spike time
9	# tiling coefficient); only its verbal definition survives (see D below). The Fig. 6 legend prints the
10	# postsonication window as "201–28 ms" (201–268 ms in the Results), and the Fig. 11 legend labels two
11	# panels "C" (the second is Fig. 11B in the Results).
12	#
13	# Code. The paper links no analysis code and names none; it says the analysis was done in MATLAB
14	# R2022a after spike sorting in Offline Sorter (Plexon). No repository was read.
15	#
16	# Which dataset. The paper's Methods name dandiset 000946 as the repository of all its data. Dandiset
17	# 001199 has the same title and cites this paper, but its description differs from the paper. It
18	# describes S1 recordings with 64-channel Cambridge or NeuroNexus electrodes, tFUS delivered "either at
19	# S1 or PoM", and varied pressure levels (input voltage in the session identifier), none of which the
20	# paper reports, and it does not mention the auditory cortex recordings. Dandiset 000946's description
[... 791 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "offset": 812
}
```

```
812	    p: 0.008
813	    corrected: Bonferroni
814	  - about: during, 30 against 1,500 Hz
815	    test: post hoc one-tail two-sample Wilcoxon test
816	    p: 0.006
817	    corrected: Bonferroni
818	  - about: during, 30 against 3,000 Hz
819	    test: post hoc one-tail two-sample Wilcoxon test
820	    p: 0.007
821	    corrected: Bonferroni
822	  - about: during, 30 against 4,500 Hz
823	    test: post hoc one-tail two-sample Wilcoxon test
824	    p: 0.0003
825	    corrected: Bonferroni
826	  criterion: S1 RSUs (U) of the five 60% DC sessions (30 Hz/20,000 us, 300/2,000, 1,500/400, 3,000/200,
827	    4,500/133 us), R in 0 to 67 and 201 to 268 ms, Kruskal-Wallis at p < 0.01, pairwise one-tailed
828	    rank-sum tests between PRFs under B1 (the five PRFs compared with baseline) and B2 (the ten pairs),
829	    corrected p < 0.01. The direction of the
830	    30 Hz difference is not stated; both directions are read, the claim holding under the one the
831	    data's means give. Reproduced when both Kruskal-Wallis tests are significant, 30 Hz differs from
[... 275 more lines not kept]
```

**Agent**

Big claims file (33 claims). Let me survey the dataset first.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001199/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001199/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001199/versions/" | python -c "import json,sys; [print(r['version'],r['asset_count'],r['size'],r['created']) for r in json.load(sys.stdin)['results']]"; curl -s "https://api.dandiarchive.org/api/dandisets/001199/versions/0.250829.1250/" > meta.json; python -c "
import json; m=json.load(open('meta.json'))
for k in ['description','relatedResource','assetsSummary','citation','keywords','protocol','wasGeneratedBy','contributor']:
    print(k, json.dumps(m.get(k),indent=0)[:3000])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001199/versions/0.250829.1250/assets/?page_size=500" > assets.json; python -c "
import json; a=json.load(open('assets.json'))['results']
print(len(a))
for x in a: print(x['path'], x['size'])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import pynwb, remfile, h5py; print(pynwb.__version__)" 2>&1; which uv python; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
Python 3.13.17
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas scikit-learn matplotlib dandi 2>&1 | tail -3; python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > open1.py <<'EOF'
import json, remfile, h5py, pynwb, sys
a=json.load(open('assets.json'))['results']
path=sys.argv[1]
x=[y for y in a if y['path']==path][0]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
import requests
r=requests.head(url,allow_redirects=True); url=r.url
f=h5py.File(remfile.File(url),'r')
def walk(g,pre=''):
    for k in g:
        o=g[k]
        if isinstance(o,h5py.Dataset): print(pre+k, o.shape, o.dtype)
        else: walk(o,pre+k+'/')
walk(f)
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print(nwb)
print('identifier',nwb.identifier,'desc',nwb.session_description, nwb.session_start_time)
print(nwb.subject)
print(nwb.electrodes.to_dataframe().head() if nwb.electrodes is not None else None)
u=nwb.units.to_dataframe(); print(u.columns.tolist()); print(u.head()); print(len(u))
for c in u.columns: print(c, nwb.units[c].description)
if nwb.trials is not None:
  t=nwb.trials.to_dataframe(); print(t.head(), len(t)); 
  for c in t.columns: print(c, nwb.trials[c].description)
print(nwb.intervals, nwb.processing, nwb.acquisition, nwb.stimulus, nwb.lab_meta_data, nwb.electrode_groups)
for k,v in nwb.electrode_groups.items(): print(k, v.description, v.location, v.device)
print(nwb.devices)
print(nwb.experiment_description, nwb.notes if hasattr(nwb,'notes') else '')
EOF
python open1.py sub-BH596/sub-BH596_ses-20240823T184200_ecephys.nwb
```

```
file_create_date (1,) object
general/data_collection () object
general/extracellular_ephys/electrodes/filtering (64,) object
general/extracellular_ephys/electrodes/group (64,) object
general/extracellular_ephys/electrodes/group_name (64,) object
general/extracellular_ephys/electrodes/id (64,) int64
general/extracellular_ephys/electrodes/imp (64,) float64
general/extracellular_ephys/electrodes/location (64,) object
general/extracellular_ephys/electrodes/x (64,) float32
general/extracellular_ephys/electrodes/y (64,) float32
general/extracellular_ephys/electrodes/z (64,) float64
general/institution () object
general/notes () object
general/stimulus () object
general/subject/age () object
general/subject/description () object
general/subject/sex () object
general/subject/species () object
general/subject/subject_id () object
identifier () object
[... 133 more lines not kept]
```

**Agent**

Units hold only spike times and a `celltype_label` column (described as 1=RSU/2=FSU but showing area names). Surveying all 229 files' metadata.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import json, remfile, h5py, requests, numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets.json'))['results']
def s(x):
    v=x[()] if x.shape==() else x[:]
    return v.decode() if isinstance(v,bytes) else v
def one(x):
    url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
    url=requests.head(url,allow_redirects=True).url
    f=h5py.File(remfile.File(url),'r')
    g=f['general']
    d=dict(path=x['path'],asset_id=x['asset_id'],identifier=s(f['identifier']),
        dc=s(g['data_collection']) if 'data_collection' in g else None,
        notes=s(g['notes']) if 'notes' in g else None,
        stim=s(g['stimulus']) if 'stimulus' in g else None,
        subj=s(g['subject/subject_id']), age=s(g['subject/age']),
        start=s(f['session_start_time']),
        ntr=f['intervals/trials/id'].shape[0] if 'intervals/trials' in f else 0,
        nunits=f['units/id'].shape[0] if 'units' in f else 0,
        nspk=f['units/spike_times'].shape[0] if 'units' in f else 0,
        units_cols=','.join(k for k in f['units'].keys()) if 'units' in f else '',
        nelec=f['general/extracellular_ephys/electrodes/id'].shape[0],
        dev=s(g['devices/array/description']) if 'devices/array' in g else str(list(g['devices'].keys())),
        )
    if 'units' in f:
        lab=[v.decode() if isinstance(v,bytes) else str(v) for v in f['units/celltype_label'][:]] if 'celltype_label' in f['units'] else []
        d['labels']=json.dumps(pd.Series(lab).value_counts().to_dict())
        d['units_desc']={k:f['units'][k].attrs.get('description','') for k in f['units'].keys()}.__repr__()
    loc=[v.decode() for v in f['general/extracellular_ephys/electrodes/location'][:]]
    d['elec_loc']=json.dumps(pd.Series(loc).value_counts().to_dict())
    tr=f['intervals/trials']
    st=tr['start_time'][:]; sp=tr['stop_time'][:]
    d['trial_dur']=float(np.median(sp-st)); d['iti']=float(np.median(np.diff(st))) if len(st)>1 else None
    d['t0']=float(st[0]); d['t1']=float(sp[-1])
    d['trcols']=','.join(tr.keys())
    return d
with ThreadPoolExecutor(16) as ex: rows=list(ex.map(one,a))
df=pd.DataFrame(rows); df.to_csv('survey.csv',index=False)
pd.set_option('display.width',300); pd.set_option('display.max_rows',300); pd.set_option('display.max_colwidth',60)
print(df[['path','identifier','dc','notes','ntr','nunits','labels']].to_string())
for c in ['units_cols','dev','elec_loc','trcols','stim','age','units_desc','nelec']: print(c, df[c].value_counts().to_dict())
print(df[['trial_dur','iti']].describe())
EOF
time python survey.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 37, in <module>
    with ThreadPoolExecutor(16) as ex: rows=list(ex.map(one,a))
                                            ~~~~^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 460, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
  File "/tmp/claude-1001/survey.py", line 23, in one
    dev=s(g['devices/array/description']) if 'devices/array' in g else str(list(g['devices'].keys())),
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i "s|dev=s(g\['devices/array/description'\]) if 'devices/array' in g else str(list(g\['devices'\].keys())),|dev=str(dict(g['devices/array'].attrs)) if 'devices/array' in g else str(list(g['devices'].keys())),|" survey.py && time python survey.py
```

```
<persisted-output>
Output too large (96.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/152a222b-09fc-4b20-98da-7f351653ba41/tool-results/bx2dsu6dh.txt

Preview (first 2KB):
                                                                path                        identifier                                                          dc                              notes  ntr  nunits                 labels
0                sub-BH594/sub-BH594_ses-20240814T163400_ecephys.nwb     BH594_nocoating_3000_200_67_5  tFUS parameters {PRF:3000Hz PD:200us UD:67ms PRESSURE:67V}           Recording:S1; stim at:S1  499      17            {"0.0": 17}
1                sub-BH594/sub-BH594_ses-20240814T172400_ecephys.nwb      BH594_nocoating_300_200_67_5   tFUS parameters {PRF:300Hz PD:200us UD:67ms PRESSURE:67V}           Recording:S1; stim at:S1  499      21            {"0.0": 21}
2                sub-BH594/sub-BH594_ses-20240814T154700_ecephys.nwb          BH594_nocoating_BASELINE                                                     No tFUS           Recording:S1; stim at:S1  499      20            {"0.0": 20}
3                sub-BH594/sub-BH594_ses-20240814T161300_ecephys.nwb     BH594_nocoating_1500_200_67_5  tFUS parameters {PRF:1500Hz PD:200us UD:67ms PRESSURE:67V}           Recording:S1; stim at:S1  499      22            {"0.0": 22}
4                sub-BH594/sub-BH594_ses-20240814T165600_ecephys.nwb     BH594_nocoating_4500_200_67_5  tFUS parameters {PRF:4500Hz PD:200us UD:67ms PRESSURE:67V}           Recording:S1; stim at:S1  499      18            {"0.0": 18}
5                sub-BH594/sub-BH594_ses-20240814T182300_ecephys.nwb    BH594_nocoating_3000_200_67_10  tFUS parameters {PRF:3000Hz PD:200us UD:67ms PRESSURE:67V}           Recording:S1; stim at:S1  499      17            {"0.0": 17}
6                sub-BH594/sub-BH594_ses-20240814T175600_ecephys.nwb       BH594_nocoating_30_200_67_5    tFUS parameters {PRF:30Hz PD:200us UD:67
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_rows',300); pd.set_option('display.max_colwidth',45)
df=pd.read_csv('survey.csv')
df['f']=df.path.str.split('/').str[1].str.replace('_ecephys.nwb','').str.replace('sub-','')
df=df.sort_values(['subj','start'])
print(df[['f','identifier','notes','ntr','nunits','labels']].to_string())
"
```

```
<persisted-output>
Output too large (33.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/152a222b-09fc-4b20-98da-7f351653ba41/tool-results/bptg9tp4h.txt

Preview (first 2KB):
                                         f                        identifier                              notes  ntr  nunits                 labels
28               BH590_ses-20240816T165400                 BH590_BASELINE_NZ           Recording:S1; stim at:S1  400      10            {"0.0": 10}
30               BH590_ses-20240816T173100            BH590_3000_200_67_5_NZ           Recording:S1; stim at:S1  499      12            {"0.0": 12}
32               BH590_ses-20240816T175200           BH590_3000_200_67_15_NZ           Recording:S1; stim at:S1  499      13            {"0.0": 13}
31               BH590_ses-20240816T181300           BH590_3000_200_67_10_NZ           Recording:S1; stim at:S1  499      16            {"0.0": 16}
29               BH590_ses-20240816T183500         BH590_3000_200_67_10_P_NZ          Recording:S1; stim at:POM  499      18            {"0.0": 18}
34               BH590_ses-20240816T185700         BH590_3000_200_67_15_P_NZ          Recording:S1; stim at:POM  499      11            {"0.0": 11}
37               BH590_ses-20240816T191800          BH590_3000_200_67_5_P_NZ          Recording:S1; stim at:POM  499      12            {"0.0": 12}
35               BH590_ses-20240816T194000             BH590_30_200_67_10_NZ           Recording:S1; stim at:S1  499      10            {"0.0": 10}
36               BH590_ses-20240816T200200             BH590_30_200_67_15_NZ           Recording:S1; stim at:S1  499       3             {"0.0": 3}
33               BH590_ses-20240816T202300              BH590_30_200_67_5_NZ           Recording:S1; stim at:S1  499       7             {"0.0": 7}
38               BH590_ses-20240816T204500            BH590_30_200_67_5_P_NZ          Recording:S1; stim at:POM  499       8             {"0.0": 8}
41      
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/152a222b-09fc-4b20-98da-7f351653ba41/tool-results/bptg9tp4h.txt"
}
```

```
1	                                         f                        identifier                              notes  ntr  nunits                 labels
2	28               BH590_ses-20240816T165400                 BH590_BASELINE_NZ           Recording:S1; stim at:S1  400      10            {"0.0": 10}
3	30               BH590_ses-20240816T173100            BH590_3000_200_67_5_NZ           Recording:S1; stim at:S1  499      12            {"0.0": 12}
4	32               BH590_ses-20240816T175200           BH590_3000_200_67_15_NZ           Recording:S1; stim at:S1  499      13            {"0.0": 13}
5	31               BH590_ses-20240816T181300           BH590_3000_200_67_10_NZ           Recording:S1; stim at:S1  499      16            {"0.0": 16}
6	29               BH590_ses-20240816T183500         BH590_3000_200_67_10_P_NZ          Recording:S1; stim at:POM  499      18            {"0.0": 18}
7	34               BH590_ses-20240816T185700         BH590_3000_200_67_15_P_NZ          Recording:S1; stim at:POM  499      11            {"0.0": 11}
8	37               BH590_ses-20240816T191800          BH590_3000_200_67_5_P_NZ          Recording:S1; stim at:POM  499      12            {"0.0": 12}
9	35               BH590_ses-20240816T194000             BH590_30_200_67_10_NZ           Recording:S1; stim at:S1  499      10            {"0.0": 10}
10	36               BH590_ses-20240816T200200             BH590_30_200_67_15_NZ           Recording:S1; stim at:S1  499       3             {"0.0": 3}
11	33               BH590_ses-20240816T202300              BH590_30_200_67_5_NZ           Recording:S1; stim at:S1  499       7             {"0.0": 7}
12	38               BH590_ses-20240816T204500            BH590_30_200_67_5_P_NZ          Recording:S1; stim at:POM  499       8             {"0.0": 8}
13	41               BH590_ses-20240816T210600           BH590_30_200_67_15_P_NZ          Recording:S1; stim at:POM  499       5             {"0.0": 5}
14	39               BH590_ses-20240816T212700 
[... 217 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd
df=pd.read_csv('survey.csv')
for c in ['units_cols','dev','elec_loc','trcols','stim','age','units_desc','nelec','dc']: print(c, df[c].value_counts().to_dict()); print()
print(df[['trial_dur','iti','t0','t1']].describe())
print(df.nunits.sum(), df.groupby('subj').nunits.sum())
"
```

```
<persisted-output>
Output too large (45.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/152a222b-09fc-4b20-98da-7f351653ba41/tool-results/bjki91ju4.txt

Preview (first 2KB):
units_cols {'id,spike_times,spike_times_index': 133, 'celltype_label,id,spike_times,spike_times_index': 96}

dev {"{'description': 'A1x32-Poly3-10mm-50-177-A32', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': '1275084c-6504-4c63-b1b2-00558ffac481'}": 2, "{'description': 'A1x64-Edge-6mm-22.5-177 without z-coating', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': '20938c3a-1ffb-413c-92a7-c267428702ba'}": 1, "{'description': 'A1x64-Edge-6mm-22.5-177 without z-coating', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': '186c8a6d-0222-4a7f-996d-e23db026b9c3'}": 1, "{'description': 'A1x64-Edge-6mm-22.5-177 without z-coating', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': 'c68ef8a1-0abd-453f-84ba-92f23282e617'}": 1, "{'description': 'A1x64-Edge-6mm-22.5-177 without z-coating', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': '709c105f-250c-4d0d-ba3f-8c5aae3f4b20'}": 1, "{'description': 'A1x64-Edge-6mm-22.5-177 without z-coating', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': 'f2a2a243-a73b-491f-8644-3ff176d55d12'}": 1, "{'description': 'A1x64-Edge-6mm-22.5-177 without z-coating', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': 'efd05896-a787-4a00-812b-d125496d990e'}": 1, "{'description': 'A1x64-Edge-6mm-22.5-177 without z-coating', 'manufacturer': 'Neuronexus', 'namespace': 'core', 'neurodata_type': 'Device', 'object_id': 'fc800bb0-a2ed-45bb-acad-337792d76c4f'}": 1, "{'description': 'A1x64-Edge-6mm-22.5-177 without z-coating', 'manufacturer': 'Neuronexus', 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd, re
df=pd.read_csv('survey.csv')
df['dev']=df.dev.str.extract(r\"'description': '([^']*)'\")
for c in ['units_cols','dev','elec_loc','trcols','stim','age','units_desc','nelec','dc']: print(c, df[c].value_counts().to_dict()); print()
print(df[['trial_dur','iti','t0','t1']].describe())
print(df.nunits.sum(), df.groupby('subj').nunits.sum().to_dict())
"
```

```
units_cols {'id,spike_times,spike_times_index': 133, 'celltype_label,id,spike_times,spike_times_index': 96}

dev {'A1x32-Poly3-10mm-50-177-A32': 91, 'A1x64-Edge-6mm-22.5-177 with z-coating': 59, 'A1x64-Edge-6mm-22.5-177 & A1x32-Poly3-10mm-50-177-A32': 47, 'A1x64-Edge-6mm-22.5-177 without z-coating': 28, 'H9': 4}

elec_loc {'{"unknown": 64}': 138, '{"unknown": 32}': 91}

trcols {'id,start_time,stop_time': 229}

stim {'intervals contains each tFUS trial start and end timestamps': 96}

age {'P24W': 229}

units_desc {"{'id': '', 'spike_times': '/units/spike_times', 'spike_times_index': 'indexes data'}": 133, "{'celltype_label': 'label 1 = RSU, label 2 = FSU', 'id': '', 'spike_times': '/units/spike_times', 'spike_times_index': 'indexes data'}": 96}

nelec {64: 138, 32: 91}

dc {'tFUS parameters {PRF:3000Hz PD:200us UD:67ms PRESSURE:67V}': 31, 'tFUS parameters {PRF:30Hz PD:200us UD:67ms PRESSURE:67V}': 25, 'tFUS parameters {PRF:1500Hz PD:200us UD:67ms PRESSURE:67V}': 10, 'tFUS parameters {PRF:300Hz PD:200us UD:67ms PRESSURE:67V}': 7, 'tFUS parameters {PRF:4500Hz PD:200us UD:67ms PRESSURE:67V}': 6, 'No tFUS': 4, 'tFUS parameters {PRF:3000Hz PD:200us UD:67ms PRESSURE:15V}': 4, 'tFUS parameters {PRF:3000Hz PD:200us UD:67ms PRESSURE:10V}': 3, 'tFUS parameters {PRF:30Hz PD:200us UD:67ms PRESSURE:10V}': 2, 'tFUS parameters {PRF:30Hz PD:200us UD:67ms PRESSURE:15V}': 2, 'tFUS parameters {PRF:3000Hz PD:200us UD:67ms PRESSURE:5V}': 1, 'tFUS parameters {PRF:30Hz PD:200us UD:67ms PRESSURE:5V}': 1}

          trial_dur         iti          t0           t1
count  2.290000e+02  229.000000  229.000000   229.000000
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt",
 "offset": 326,
 "limit": 40
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the example entry formats.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025 && cat entry.yaml requirements.in README.md && head -c 3000 omr.py && python -c "
import json; nb=json.load(open('reproduce_fouke_2025.ipynb'))
print(nb['metadata'])
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('-----')
print(len(nb['cells']))
for c in nb['cells']: print(c['cell_type'], c.get('metadata',{}).get('tags'), ''.join(c['source'])[:80].replace('\n',' '))
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
[... 260 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && cat attempts/001453-fouke-2025-01.yaml | head -200; grep -n "" attempts/001453-fouke-2025-01.yaml | sed -n '200,400p' | grep -E "^[0-9]+:[a-z]"
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
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,320p attempts/001453-fouke-2025-01.yaml; ls schemas tools; python tools/entry.py --help 2>&1 | head -30
```

```
notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
    dandiset gives no mapping from those folders to its subjects, nor the original file names.
- claim: fig2d-shared-architecture
  outcome: blocked
  blocked_by: data_missing
  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
    notebooks only, and no other dandiset of this lab or paper was found on the archive.
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
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=1)[:9000])
"
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
  "dataset",
  "paper",
  "date",
  "provenance",
  "outcomes"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "id": {
[... 357 more lines not kept]
```

**Agent**

Plan forming. Checking dandiset 000946 (named by the paper) for context, and whether same-condition files across areas share trial tables (simultaneous recordings) or duplicate each other.

**Agent calls Bash**

```bash
cd $TMPDIR; date -u; curl -s https://api.dandiarchive.org/api/dandisets/000946/ | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('most_recent_published_version'), d.get('draft_version',{}).get('name'), d.get('draft_version',{}).get('asset_count'), d.get('draft_version',{}).get('size'))"; curl -s https://api.dandiarchive.org/api/dandisets/000946/versions/draft/ | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('description')); print(d.get('assetsSummary',{}).get('numberOfSubjects'), d.get('assetsSummary',{}).get('variableMeasured')); print([r.get('identifier') for r in d.get('relatedResource',[])])"; curl -s "https://api.dandiarchive.org/api/dandisets/000946/versions/draft/assets/?page_size=5" | python -c "import json,sys; d=json.load(sys.stdin); print(d['count']); [print(x['path'],x['size']) for x in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import requests, collections
url="https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=1000"
paths=[]
while url:
    d=requests.get(url).json(); paths+= [x['path'] for x in d['results']]; url=d['next']
print(len(paths))
c=collections.defaultdict(list)
for p in paths:
    s=p.split('/')[0]; c[s].append(p.split('/')[-1])
for s,v in sorted(c.items()):
    dates=sorted(set(x.split('ses-')[1][:8] for x in v if 'ses-' in x))
    print(s,len(v),dates[:6], [x for x in v if 'ses-' not in x][:2])
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
cd $TMPDIR; . dev/bin/activate; python - <<'EOF'
import requests, collections
url="https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=1000"
paths=[]
while url:
    d=requests.get(url).json(); paths+= [x['path'] for x in d['results']]; url=d['next']
print(len(paths))
c=collections.defaultdict(list)
for p in paths:
    s=p.split('/')[0]; c[s].append(p.split('/')[-1])
for s,v in sorted(c.items()):
    dates=sorted(set(x.split('ses-')[1][:8] for x in v if 'ses-' in x))
    print(s,len(v),dates[:8], [x for x in v if 'ses-' not in x][:2])
EOF
```

```
1920
sub-BH494 53 ['20230817', '20230820', '20230821', '20231028', '20231029', '20240214'] ['sub-BH494_ecephys.nwb']
sub-BH495 75 ['20230820', '20230821', '20230822', '20230828', '20231026'] ['sub-BH495_ecephys.nwb']
sub-BH499 77 ['20230831', '20230902', '20231023', '20231024', '20231026', '20231028'] []
sub-BH500 31 ['20230810', '20230814', '20230926', '20230928', '20230929', '20231001'] []
sub-BH501 78 ['20230824', '20231027', '20231028'] []
sub-BH510 48 ['20230902', '20230904', '20230905', '20231022'] []
sub-BH511 115 ['20230907', '20231017', '20231019', '20231020', '20231022'] []
sub-BH513 109 ['20231001', '20231002', '20231005', '20231006', '20231007', '20231008', '20231015', '20231016'] []
sub-BH528 117 ['20230912', '20230914', '20231001', '20231016', '20231017'] []
sub-BH530 64 ['20231126', '20231130', '20231202'] []
sub-BH532 85 ['20231202', '20231203', '20231204'] []
sub-BH535 92 ['20231221', '20231224', '20231225', '20231228', '20231229', '20231230', '20240101', '20240103'] []
sub-BH537 73 ['20240108', '20240109'] []
sub-BH538 94 ['20240108', '20240109', '20240110', '20240313'] []
sub-BH539 92 ['20240121', '20240123', '20240124', '20240125', '20240126'] []
sub-BH547 88 ['20240221', '20240222', '20240223', '20240225', '20240229'] []
sub-BH551 88 ['20240302', '20240308', '20240312'] []
sub-BH553 92 ['20240305', '20240306', '20240307', '20240308'] []
sub-BH558 78 ['20240321', '20240322'] []
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/001199-gao-2025 && cd $TMPDIR && . dev/bin/activate && cat > loadall.py <<'EOF'
import json, remfile, h5py, requests, numpy as np, pickle, time
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets.json'))['results']
def one(x):
    url=requests.head(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(url),'r')
    st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]
    tr=f['intervals/trials/start_time'][:]; sp=f['intervals/trials/stop_time'][:]
    return x['path'], dict(st=st, idx=idx, tr=tr, sp=sp)
t=time.time()
with ThreadPoolExecutor(16) as ex: d=dict(ex.map(one,a))
print(time.time()-t)
pickle.dump(d,open('all.pkl','wb'))
EOF
python loadall.py
```

```
176.73266172409058
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
d=pickle.load(open('all.pkl','rb')); s=pd.read_csv('survey.csv').set_index('path')
# duplicates: identical spike arrays
import hashlib
h={p:hashlib.md5(v['st'].tobytes()).hexdigest() for p,v in d.items()}
ht={p:hashlib.md5(np.round(v['tr'],4).tobytes()).hexdigest() for p,v in d.items()}
from collections import defaultdict
g=defaultdict(list)
for p,x in h.items(): g[x].append(p)
print('identical spikes:', [v for v in g.values() if len(v)>1])
g=defaultdict(list)
for p,x in ht.items(): g[x].append(p)
print('identical trial tables:')
for v in g.values():
    if len(v)>1: print([ (pp.split('/')[1][:-12], s.loc[pp,'notes'], s.loc[pp,'identifier']) for pp in v])
# ITI jitter
itis=np.concatenate([np.diff(v['tr']) for v in d.values()])
print('ITI pct', np.percentile(itis,[0,1,5,50,95,99,100]))
# spike time ranges vs trials
for p in list(d)[:3]+list(d)[100:103]:
    v=d[p]; print(p, v['st'].min(), v['st'].max(), v['tr'][0], v['sp'][-1], 'sorted per unit:', all(np.all(np.diff(u)>=0) for u in np.split(v['st'],v['idx'][:-1])))
EOF
```

```
identical spikes: [['sub-BH646/sub-BH646_ses-None_ecephys.nwb', 'sub-BH646/sub-BH646_ses-20250308T003900_ecephys.nwb']]
identical trial tables:
[('sub-BH646_ses-None', 'recording:AC;stimulation:S1-6', '30_200_67'), ('sub-BH646_ses-20250308T003900', 'recording:AC;stimulation:S1-6', '30_200_67'), ('sub-BH646_ses-20250308T005100', 'recording:S1;stimulation:S1-6', '30_200_67')]
[('sub-BH646_ses-20250308T020300', 'recording:AC;stimulation:S1', '300_200_67'), ('sub-BH646_ses-20250308T021500', 'recording:S1;stimulation:S1', '300_200_67')]
[('sub-BH646_ses-20250308T121300', 'recording:AC;stimulation:S1', '1500_200_67'), ('sub-BH646_ses-20250308T122700', 'recording:S1;stimulation:S1', '1500_200_67')]
[('sub-BH646_ses-20250308T144800', 'recording:AC;stimulation:S1-6', '3000_200_67'), ('sub-BH646_ses-20250308T153200', 'recording:S1;stimulation:S1-6', '3000_200_67')]
[('sub-BH646_ses-20250308T184400', 'recording:AC;stimulation:S1', '4500_200_67'), ('sub-BH646_ses-20250308T193100', 'recording:S1;stimulation:S1', '4500_200_67')]
[('sub-BH646_ses-20250308T203000', 'recording:AC;stimulation:no tFUS', 'no tFUS'), ('sub-BH646_ses-20250308T205000', 'recording:S1;stimulation:no tFUS', 'no tFUS')]
[('sub-BH648_ses-20250306T003000', 'recording:AC;stimulation:S1', '30_200_67'), ('sub-BH648_ses-20250306T005100', 'recording:S1;stimulation:S1', '30_200_67')]
[('sub-BH648_ses-20250307T005400', 'recording:AC;stimulation:S1', '300_200_67'), ('sub-BH648_ses-20250307T011300', 'recording:S1;stimulation:S1', '300_200_67')]
[('sub-BH648_ses-20250307T025800', 'recording:POm;stimulation:S1', '1500_200_67'), ('sub-BH648_ses-20250307T031000', 'recording:S1;stimulation:S1', '1500_200_67')]
[('sub-BH648_ses-20250307T034200', 'recording:AC;stimulation:S1', '3000_200_67'), ('sub-BH648_ses-20250307T040700', 'recording:S1;stimulation:S1', '3000_200_67')]
[('sub-BH648_ses-20250307T205000', 'recording:S1;stimulation:S1', '4500_200_67'), ('sub-BH648_ses-20250307T205200', 'recording:AC;stimulation:S1', '4500_200_
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd, re
d=pickle.load(open('all.pkl','rb')); s=pd.read_csv('survey.csv').set_index('path')
def area(p):
    n=s.loc[p,'notes']; m=re.search(r'recording:\s*(\w+)',n,re.I); return m.group(1)
def stim(p):
    n=s.loc[p,'notes']; m=re.search(r'(?:stimulation|stim at):\s*([\w\- ]+)',n,re.I); return m.group(1).strip()
def prf(p):
    i=s.loc[p,'identifier']; m=re.search(r'(?:^|_)(30|300|1500|3000|4500)_200',i); return int(m.group(1)) if m else (0 if ('BASELINE' in i or 'no tFUS' in i) else -1)
bins=np.arange(-0.5,1.5001,0.025)
rows=[]
for p,v in d.items():
    if s.loc[p,'subj'] not in ['BH646','BH648','BH650','BH654','BH655','BH657','BH658','BH608']: continue
    units=np.split(v['st'],v['idx'][:-1]); tr=v['tr']
    for u in units:
        if len(u)<=2000: continue
        h=np.zeros(len(bins)-1)
        for t in tr: h+=np.histogram(u-t,bins)[0]
        rows.append(dict(p=p,area=area(p),stim=stim(p),prf=prf(p),h=h/len(tr)/0.025))
df=pd.DataFrame(rows)
print(df.groupby(['area','stim','prf']).size())
np.set_printoptions(linewidth=250,precision=0,suppress=True)
for (a,pr),g in df[df.stim.isin(['S1','S1-6','no tFUS'])].groupby(['area','prf']):
    H=np.stack(g.h.values); base=H[:,(bins[:-1]>=-0.5)&(bins[:-1]<0)].mean(1,keepdims=True)
    m=np.nanmean(H/np.where(base>0,base,np.nan),0)*100
    print(a,pr,len(g)); print(' -100..400ms', m[16:40])
EOF
```

```
area  stim     prf 
AC    S1       30      17
               300     29
               1500    42
               3000    27
               4500    38
      S1-6     30      40
               3000    13
      no tFUS  0       65
POm   CG1      300      4
               4500     4
      NEW      300      4
               1500     6
      S1       30      20
               300     52
               1500    45
               3000    31
               4500    46
      S1-6     30      15
               3000    32
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > psth.py <<'EOF'
import pickle, numpy as np, pandas as pd, re, sys
d=pickle.load(open('all.pkl','rb')); s=pd.read_csv('survey.csv').set_index('path')
bins=np.arange(-0.5,1.5001,0.025)
np.set_printoptions(linewidth=250,precision=0,suppress=True)
subs=sys.argv[1].split(',')
for p,v in sorted(d.items(), key=lambda x:s.loc[x[0],'start']):
    if s.loc[p,'subj'] not in subs: continue
    units=np.split(v['st'],v['idx'][:-1]); tr=v['tr']
    H=[]
    for u in units:
        if len(u)<=2000: continue
        h=np.zeros(len(bins)-1)
        for t in tr: h+=np.histogram(u-t,bins)[0]
        H.append(h/len(tr)/0.025)
    if not H: continue
    H=np.array(H); tot=H.sum(0); base=tot[:20].mean()
    print(f"{s.loc[p,'identifier']:35s} {s.loc[p,'notes'][:32]:32s} n={len(H):3d}", (tot[16:44]/base*100))
EOF
python psth.py BH596,BH615,BH594,BH590
```

```
BH594_nocoating_BASELINE            Recording:S1; stim at:S1         n= 17 [123. 108. 112. 108. 102.  56.  94. 167.  80. 100. 107. 138. 121.  83. 126. 131.  91.  76.  80.  64.  80.  93. 107. 125. 103. 104.  88. 117.]
BH594_nocoating_1500_200_67_5       Recording:S1; stim at:S1         n= 19 [ 74. 101. 129. 117.  81.  79.  85.  86.  88.  84.  54.  93.  77.  75.  64.  54.  55.  79.  66.  76.  87.  82.  82.  85.  56. 109. 100.  77.]
BH594_nocoating_3000_200_67_5       Recording:S1; stim at:S1         n= 16 [ 57.  68.  89. 113.  79.  63. 165.  79.  69.  74.  98.  93.  77.  71.  74.  93.  63.  57.  77.  83.  59.  66.  81.  60.  92.  77.  52.  44.]
BH594_nocoating_4500_200_67_5       Recording:S1; stim at:S1         n= 16 [125. 116. 104. 116. 118. 118. 114. 108. 108. 114. 112. 103.  55.  86.  94.  92.  81.  78. 129. 112.  90.  55.  55.  79.  92.  60.  72.  65.]
BH594_nocoating_300_200_67_5        Recording:S1; stim at:S1         n= 18 [117.  82.  34.  93. 130. 108. 162. 134. 122.  90.  99.  70. 120.  96. 152.  73. 104. 103.  78. 115. 124. 110. 149.  92. 105. 101.  83.  91.]
BH594_nocoating_30_200_67_5         Recording:S1; stim at:S1         n= 15 [112.  57. 112.  96. 118. 131. 138.  73.  68.  80. 148.  81.  77.  60.  78. 109. 135.  89. 105.  52.  49.  98.  53.  91.  72. 134. 125. 128.]
BH594_nocoating_3000_200_67_10      Recording:S1; stim at:S1         n= 16 [116.  88.  93.  95. 152.  94. 100.  69. 124.  88.  78. 107. 139. 116. 106. 108.  83.  93. 117. 139.  91.  93.  53.  61.  57.  74.  87.  88.]
BH594_nocoating_3000_200_10_pom     Recording:S1; stim at:POM        n= 18 [ 89.  66. 103. 121.  93.  85. 122. 102. 142. 113. 142. 125. 150. 130. 156. 103. 112. 142. 141. 153. 155. 113.  83. 128.  96. 163. 103.  56.]
BH594_nocoating_3000_200_5_pom      Recording:S1; stim at:POM        n= 13 [ 85.  82. 108. 142. 118. 161.  92. 111. 123. 130. 152. 116. 121. 112. 112.  82. 148. 136. 123. 136. 105. 169. 108. 115. 129. 104.  83. 107.]
BH594_nocoating_3000_200_15_pom     Recording:S
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python -c "
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); ds=c.get_dandiset('001199','0.250829.1250')
a=next(iter(ds.get_assets())); print(a.path, a.identifier, a.get_content_url(follow_redirects=1, strip_query=True))
"
```

```
Sun Nov  1 09:17:22 UTC 2026
sub-BH594/sub-BH594_ses-20240814T163400_ecephys.nwb 6499fbba-af59-47c0-85cf-ede6fb22849b https://dandiarchive.s3.amazonaws.com/blobs/ce8/040/ce804054-107c-4458-8a30-7a328f24f18f
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import json; a=json.load(open('assets.json'))['results']; print(a[0])
import requests
for v in ['0.250712.1551','0.250713.1101','0.250828.1941','0.250829.1250','draft']:
    r=requests.get(f'https://api.dandiarchive.org/api/dandisets/001199/versions/{v}/assets/?page_size=500').json()['results']
    print(v, len(r), len(set((x['path'],x['blob']) for x in r)), r[0].keys() if v=='draft' else '')
    if v=='0.250712.1551': first=set((x['path'],x['blob']) for x in r)
    else: print(' diff vs first', len(first ^ set((x['path'],x['blob']) for x in r)))
m1=requests.get('https://api.dandiarchive.org/api/dandisets/001199/versions/0.250712.1551/').json()
m2=requests.get('https://api.dandiarchive.org/api/dandisets/001199/versions/0.250829.1250/').json()
for k in set(m1)|set(m2):
    if m1.get(k)!=m2.get(k): print('meta differs:',k, str(m1.get(k))[:200], '|', str(m2.get(k))[:200])
"
```

```
{'asset_id': '6499fbba-af59-47c0-85cf-ede6fb22849b', 'blob': 'ce804054-107c-4458-8a30-7a328f24f18f', 'zarr': None, 'path': 'sub-BH594/sub-BH594_ses-20240814T163400_ecephys.nwb', 'size': 795608, 'created': '2024-09-30T21:41:17.651187Z', 'modified': '2025-07-12T15:51:02.930174Z'}
0.250712.1551 229 229 
0.250713.1101 229 229 
 diff vs first 0
0.250828.1941 229 229 
 diff vs first 0
0.250829.1250 229 229 
 diff vs first 0
draft 229 229 dict_keys(['asset_id', 'blob', 'zarr', 'path', 'size', 'created', 'modified'])
 diff vs first 0
meta differs: version 0.250712.1551 | 0.250829.1250
meta differs: doi 10.48324/dandi.001199/0.250712.1551 | 10.48324/dandi.001199/0.250829.1250
meta differs: datePublished 2025-07-12T15:51:02.740523+00:00 | 2025-08-29T12:50:57.606220+00:00
meta differs: contributor [{'name': 'Gao, Huan', 'email': '[removed: an e-mail address]', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'He, Bin', 'roleName': ['d | [{'name': 'Gao, Huan', 'email': '[removed: an e-mail address]', 'roleName': ['dcite:ContactPerson'], 'schemaKey': 'Person', 'affiliation': [], 'includeInCitation': True}, {'name': 'Ramachandran, Sandhya', '
meta differs: id DANDI:001199/0.250712.1551 | DANDI:001199/0.250829.1250
meta differs: publishedBy {'id': 'urn:uuid:3ca0b819-c5eb-4f10-a247-2677fa2d9572', 'name': 'DANDI publish', 'endDate': '2025-07-12T15:51:02.740523+00:00', 'schemaKey': 'PublishActivity', 'startDate': '2025-07-12T15:51:02.740523 | {'id': 'urn:uuid:05d218f1-046c-4b63-ad55-3a562e839aad', 'name': 'DANDI publish', 'endDate': '2025-08-29T12:50:57.606220+00:00', 'schemaKey': 'PublishActivity', 'startDate': '2025-08-29T12:50:57.606220
meta differs: citation Gao, Huan; He, Bin; Ramachandran, Sandhya; Yu, Kai (2025) Neural Pathways Modulation in the Anesthetized Rat Elicited by Trials of Transcranial Focused Ultrasound Stimulation (Version 0.250712.1551) [ | Gao, Huan; Ramachandran, Sandhya; Yu, Kai; He, Bin (2025) Neural Path
[... 3 more lines not kept]
```

**Agent**

All published versions hold the same 229 blobs; only the contributor order differs. Pinning 0.250829.1250. Writing the helper.

**Agent calls Write**

```json
{
 "file_path": "entries/001199-gao-2025/tfus.py",
 "content": "\"\"\"Loading and spiking measures for the tFUS recordings of dandiset 001199.\n\nGao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025,\ndoi:10.1523/jneurosci.2218-24.2025.\n\nEach NWB file holds sorted units (spike times only; no waveforms) and a trial table whose\n`start_time` is taken as the sonication onset (the notebook checks this). The condition of a file\nis written in its `identifier` and `general/notes`, in two formats:\n\n- files of rats BH590, BH594, BH596 and BH615 (recorded 2024): identifier\n  `<rat>[_tag]_<PRF>_<PD>_<UD>_<voltage>[_tags]` or `<rat>_BASELINE`, notes\n  `Recording:S1; stim at:S1|POM`, and in BH596 and BH615 a `celltype_label` column that holds the\n  area (S1 or POm) of each unit;\n- files of rats BH608 and BH646 to BH658 (recorded 2025): identifier `<PRF>_<PD>_<UD>` or\n  `no tFUS`, notes `recording:<area>;stimulation:<target>`, one file per probe.\n\nFiles are streamed from the archive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- `MIN_SPIKES = 2000`: \"Only neurons that fire >2,000 spikes for each session were considered\"\n  (Methods, Neuronal type classification); claims file, header U.\n- `PRESTIM = (-0.067, 0)`: \"normalized to 67 ms before each stimulation\" (Methods, same\n  paragraph; Statistical analysis); claims file, header R.\n- `WINDOWS`: during sonication 0 to 67 ms and postsonication 201 to 268 ms (Results, tFUS\n  parameters, paragraph 1; claims file, header W), with the consecutive 67 ms windows between.\n- `normalized_rates`: readings R1 (per unit, trial-averaged window rate over trial-averaged\n  prestimulus rate) and R2 (per trial ratio, then the mean over trials with a prestimulus spike),\n  as the claims file, header R, names them.\n- `vs_baseline`: one-tailed two-sample Wilcoxon (rank-sum) test, readings T1 (window rates\n  against prestimulus rates, spikes/s) and T2 (normalized values against 100%), claims file,\n  header T. The Bonferroni factor is applied by the caller (readings B1 and B2 of header T).\n- `SHIFT_S = 1.25` s for the clock check: half the 2.5 s intersonication interval (Methods,\n  Transcranial focused ultrasound stimulation), a standard choice that puts the shifted onsets\n  between sonications.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom scipy import stats\n\nDANDISET_ID = \"001199\"\nDANDISET_VERSION = \"0.250829.1250\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nMIN_SPIKES = 2000\nPRESTIM = (-0.067, 0.0)\nWINDOWS = {\n    \"0-67\": (0.0, 0.067),\n    \"67-134\": (0.067, 0.134),\n    \"134-201\": (0.134, 0.201),\n    \"201-268\": (0.201, 0.268),\n}\nPRFS = (30, 300, 1500, 3000, 4500)\nSHIFT_S = 1.25\n\n\ndef list_assets(version: str = DANDISET_VERSION) -> pd.DataFrame:\n    \"\"\"Every asset of a version: path, asset id, blob id and size.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000\"\n    rows = []\n    while url:\n        page = requests.get(url, timeout=60).json()\n        rows += [{k: a[k] for k in (\"path\", \"asset_id\", \"blob\", \"size\")} for a in page[\"results\"]]\n        url = page[\"next\"]\n    return pd.DataFrame(rows).sort_values(\"path\").reset_index(drop=True)\n\n\ndef version_metadata(version: str = DANDISET_VERSION) -> dict:\n    return requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/\", timeout=60).json()\n\n\ndef _url(asset_id: str) -> str:\n    r = requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60)\n    return r.url\n\n\ndef _str(x):\n    v = x[()]\n    return v.decode() if isinstance(v, bytes) else str(v)\n\n\ndef read_file(asset_id: str, spikes: bool = True) -> dict:\n    \"\"\"Read one file's metadata, trial table and (optionally) spike trains.\"\"\"\n    f = h5py.File(remfile.File(_url(asset_id)), \"r\")\n    g = f[\"general\"]\n    out = {\n        \"identifier\": _str(f[\"identifier\"]),\n        \"session_start\": _str(f[\"session_start_time\"]),\n        \"data_collection\": _str(g[\"data_collection\"]) if \"data_collection\" in g else \"\",\n        \"notes\": _str(g[\"notes\"]) if \"notes\" in g else \"\",\n        \"subject_id\": _str(g[\"subject/subject_id\"]),\n        \"age\": _str(g[\"subject/age\"]),\n        \"sex\": _str(g[\"subject/sex\"]),\n        \"device\": dict(g[\"devices/array\"].attrs).get(\"description\", \"\") if \"devices/array\" in g else \"\",\n        \"n_electrodes\": g[\"extracellular_ephys/electrodes/id\"].shape[0],\n        \"electrode_locations\": sorted({v.decode() for v in g[\"extracellular_ephys/electrodes/location\"][:]}),\n        \"units_columns\": sorted(k for k in f[\"units\"].keys()),\n        \"units_descriptions\": {k: f[\"units\"][k].attrs.get(\"description\", \"\") for k in f[\"units\"].keys()},\n        \"trial_start\": f[\"intervals/trials/start_time\"][:],\n        \"trial_stop\": f[\"intervals/trials/stop_time\"][:],\n        \"n_units\": f[\"units/id\"].shape[0],\n    }\n    if \"celltype_label\" in f[\"units\"]:\n        out[\"celltype_label\"] = [v.decode() if isinstance(v, bytes) else str(v) for v in f[\"units/celltype_label\"][:]]\n    else:\n        out[\"celltype_label\"] = None\n    if spikes:\n        st = f[\"units/spike_times\"][:]\n        idx = f[\"units/spike_times_index\"][:]\n        out[\"spikes\"] = np.split(st, idx[:-1])\n    f.close()\n    return out\n\n\ndef read_many(asset_ids, spikes: bool = True, workers: int = 16) -> list[dict]:\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(lambda a: read_file(a, spikes), asset_ids))\n\n\ndef parse_condition(identifier: str, notes: str) -> dict:\n    \"\"\"PRF (Hz), PD (us), voltage (V, when written), recording area and target of a file.\"\"\"\n    out = {\"prf\": None, \"pd\": None, \"volt\": None, \"sham\": False, \"rec\": None, \"target\": None, \"tags\": \"\"}\n    if \"BASELINE\" in identifier or \"no tFUS\" in identifier:\n        out[\"sham\"] = True\n    m = re.search(r\"(?:^|_)(30|300|1500|3000|4500)_(200)(?:_(67))?(?:_(5|10|15))?(?:_|$)\", identifier)\n    if m:\n        out[\"prf\"], out[\"pd\"] = int(m.group(1)), int(m.group(2))\n        if m.group(4):\n            out[\"volt\"] = int(m.group(4))\n    m = re.search(r\"recording:\\s*(\\w+)\", notes, re.I)\n    out[\"rec\"] = m.group(1) if m else None\n    m = re.search(r\"(?:stimulation|stim at):\\s*([^;]+)\", notes, re.I)\n    tgt = m.group(1).strip() if m else None\n    out[\"target\"] = \"none\" if out[\"sham\"] or tgt == \"no tFUS\" else tgt\n    tags = [t for t in (\"nocoating\", \"coating\", \"NZ\", \"C\", \"P\", \"pom\", \"POm\", \"S1\", \"2mm\", \"break\", \"bad\",\n                         \"x0y35z165\", \"2\") if re.search(rf\"_{t}(?:_|$)\", identifier)]\n    out[\"tags\"] = \",\".join(tags)\n    return out\n\n\ndef unit_counts(spikes, onsets, windows: dict, prestim=PRESTIM) -> dict:\n    \"\"\"Spike counts per trial for each window, and for the prestimulus window.\n\n    Returns {name: array (units, trials)} with key 'pre' for the prestimulus window.\"\"\"\n    onsets = np.asarray(onsets)\n    allw = {\"pre\": prestim, **windows}\n    out = {k: np.zeros((len(spikes), len(onsets))) for k in allw}\n    for i, s in enumerate(spikes):\n        for k, (a, b) in allw.items():\n            lo = np.searchsorted(s, onsets + a, side=\"left\")\n            hi = np.searchsorted(s, onsets + b, side=\"left\")\n            out[k][i] = hi - lo\n    return out\n\n\ndef normalized_rates(counts: dict, windows: dict, prestim=PRESTIM) -> pd.DataFrame:\n    \"\"\"Per unit: prestimulus and window rates (spikes/s), and normalized rates (%) under R1 and R2.\n\n    R1: trial-averaged window rate / trial-averaged prestimulus rate x 100.\n    R2: per-trial ratio x 100, averaged over trials with a prestimulus spike.\n    Units with no prestimulus spike in any trial get NaN under both.\"\"\"\n    pre = counts[\"pre\"] / (prestim[1] - prestim[0])\n    rows = {\"pre_rate\": pre.mean(1)}\n    has_pre = pre.sum(1) > 0\n    for k, (a, b) in windows.items():\n        r = counts[k] / (b - a)\n        rows[f\"rate_{k}\"] = r.mean(1)\n        with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n            r1 = r.mean(1) / pre.mean(1) * 100\n            ratio = np.where(pre > 0, r / np.where(pre > 0, pre, 1) * 100, np.nan)\n            r2 = np.nanmean(ratio, axis=1)\n        rows[f\"R1_{k}\"] = np.where(has_pre, r1, np.nan)\n        rows[f\"R2_{k}\"] = np.where(has_pre, r2, np.nan)\n    return pd.DataFrame(rows)\n\n\ndef vs_baseline(df: pd.DataFrame, window: str, reading: str, t: str, alternative: str = \"greater\") -> float:\n    \"\"\"One-tailed rank-sum test of a window against baseline over units (uncorrected p).\n\n    t='T1': window rates against prestimulus rates (spikes/s).\n    t='T2': normalized window values (reading R1 or R2) against 100% for every unit.\"\"\"\n    d = df.dropna(subset=[f\"{reading}_{window}\"])\n    if len(d) < 2:\n        return np.nan\n    if t == \"T1\":\n        x, y = d[f\"rate_{window}\"].values, d[\"pre_rate\"].values\n    else:\n        x, y = d[f\"{reading}_{window}\"].values, np.full(len(d), 100.0)\n    return float(stats.mannwhitneyu(x, y, alternative=alternative).pvalue)\n\n\ndef kruskal(groups) -> tuple[float, float]:\n    groups = [np.asarray(g)[~np.isnan(g)] for g in groups]\n    groups = [g for g in groups if len(g) > 0]\n    if len(groups) < 2:\n        return np.nan, np.nan\n    h, p = stats.kruskal(*groups)\n    return float(h), float(p)\n\n\ndef modulation_fraction(spikes, onsets, window=(0.0, 0.4), alpha=0.01) -> float:\n    \"\"\"Fraction of units whose count in `window` after onset differs from the count in the same\n    length before onset (paired Wilcoxon over trials, two-sided).\"\"\"\n    pre = (-(window[1] - window[0]), 0.0)\n    c = unit_counts(spikes, onsets, {\"w\": window}, prestim=pre)\n    sig = []\n    for a, b in zip(c[\"w\"], c[\"pre\"]):\n        if np.all(a == b):\n            sig.append(False)\n            continue\n        sig.append(stats.wilcoxon(a, b).pvalue < alpha)\n    return float(np.mean(sig)) if sig else np.nan\n"
}
```

```
File created successfully at: entries/001199-gao-2025/tfus.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && PYTHONPATH=entries/001199-gao-2025 python - <<'EOF'
import pandas as pd, tfus
pd.set_option('display.width',250); pd.set_option('display.max_rows',300)
s=pd.read_csv('survey.csv')
c=pd.DataFrame([tfus.parse_condition(i,n) for i,n in zip(s.identifier,s.notes)])
s=pd.concat([s,c],axis=1)
print(s.groupby(['rec','target','prf','volt'],dropna=False).size().to_string())
print(s[s.prf.isna() & ~s.sham][['identifier','notes']])
print(s[['identifier','tags']].drop_duplicates('tags'))
EOF
```

```
rec  target  prf     volt
AC   S1      30.0    NaN      3
             300.0   NaN      7
             1500.0  NaN      7
             3000.0  NaN      3
             4500.0  NaN      7
     S1-6    30.0    NaN      5
             3000.0  NaN      4
     none    NaN     NaN      7
POm  CG1     300.0   NaN      1
             4500.0  NaN      1
     NEW     300.0   NaN      1
             1500.0  NaN      1
     S1      30.0    NaN      2
             300.0   NaN      5
             1500.0  NaN      6
             3000.0  NaN      5
             4500.0  NaN      6
     S1-6    30.0    NaN      5
             3000.0  NaN      4
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && PYTHONPATH=entries/001199-gao-2025 python - <<'EOF'
import pandas as pd, numpy as np, pickle, tfus
pd.set_option('display.width',250)
d=pickle.load(open('all.pkl','rb'))
s=pd.read_csv('survey.csv')
c=pd.DataFrame([tfus.parse_condition(i,n) for i,n in zip(s.identifier,s.notes)])
s=pd.concat([s,c],axis=1)
ac=s[(s.rec=='AC')&(s.target.isin(['S1','S1-6']))&(~s.path.str.contains('ses-None'))]
rows=[]
for _,r in ac.iterrows():
    v=d[r.path]; sp=np.split(v['st'],v['idx'][:-1])
    keep=[u for u in sp if len(u)>tfus.MIN_SPIKES]
    if not keep: continue
    cnt=tfus.unit_counts(keep, v['tr'], tfus.WINDOWS)
    nr=tfus.normalized_rates(cnt, tfus.WINDOWS); nr['rat']=r.subj; nr['prf']=r.prf; nr['target']=r.target
    rows.append(nr)
u=pd.concat(rows,ignore_index=True)
print(len(u), u.groupby('prf').size().to_dict(), u.groupby(['rat','prf']).size().unstack().to_string())
print('no prestim', u.R1_0-67.isna().sum() if False else u['R1_0-67'].isna().sum())
for w in ['0-67','201-268']:
  for R in ['R1','R2']:
    g=[u[u.prf==p][f'{R}_{w}'].values for p in tfus.PRFS]
    print(w,R,'KW',tfus.kruskal(g),'means',[round(np.nanmean(x),1) for x in g])
    for T in ['T1','T2']:
        print('   ',T,[ '%.2g'%tfus.vs_baseline(u[u.prf==p],w,R,T) for p in tfus.PRFS])
EOF
```

```
Exit code 1
<stdin>:18: SyntaxWarning: invalid decimal literal
  File "<stdin>", line 18
    print('no prestim', u.R1_0-67.isna().sum() if False else u['R1_0-67'].isna().sum())
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && PYTHONPATH=entries/001199-gao-2025 python - <<'EOF'
import pandas as pd, numpy as np, pickle, tfus
pd.set_option('display.width',250)
d=pickle.load(open('all.pkl','rb'))
s=pd.read_csv('survey.csv')
c=pd.DataFrame([tfus.parse_condition(i,n) for i,n in zip(s.identifier,s.notes)])
s=pd.concat([s,c],axis=1)
ac=s[(s.rec=='AC')&(s.target.isin(['S1','S1-6']))&(~s.path.str.contains('ses-None'))]
rows=[]
for _,r in ac.iterrows():
    v=d[r.path]; sp=np.split(v['st'],v['idx'][:-1])
    keep=[u for u in sp if len(u)>tfus.MIN_SPIKES]
    if not keep: continue
    cnt=tfus.unit_counts(keep, v['tr'], tfus.WINDOWS)
    nr=tfus.normalized_rates(cnt, tfus.WINDOWS); nr['rat']=r.subj; nr['prf']=r.prf; nr['target']=r.target
    rows.append(nr)
u=pd.concat(rows,ignore_index=True)
print(len(u), u.groupby('prf').size().to_dict()); print(u.groupby(['rat','prf']).size().unstack().to_string())
print('no prestim', u['R1_0-67'].isna().sum())
for w in ['0-67','201-268']:
  for R in ['R1','R2']:
    g=[u[u.prf==p][f'{R}_{w}'].values for p in tfus.PRFS]
    print(w,R,'KW',tfus.kruskal(g),'means',[round(np.nanmean(x),1) for x in g])
    for T in ['T1','T2']:
        print('   ',T,[ '%.2g'%tfus.vs_baseline(u[u.prf==p],w,R,T) for p in tfus.PRFS])
EOF
```

```
194 {30.0: 45, 300.0: 29, 1500.0: 42, 3000.0: 40, 4500.0: 38}
prf    30.0    300.0   1500.0  3000.0  4500.0
rat                                          
BH646      12       5       1       5       6
BH648       2       3       2       3       4
BH650      10       2       2       2       3
BH654       2       1       2       3       2
BH655       4       7      14       3       5
BH657       2       3       5       3       5
BH658      13       8      16      21      13
no prestim 0
0-67 R1 KW (9.475244584697155, 0.05025840900709584) means [np.float64(101.3), np.float64(100.1), np.float64(105.1), np.float64(204.9), np.float64(100.0)]
    T1 ['0.5', '0.51', '0.38', '0.31', '0.52']
    T2 ['0.58', '0.96', '6.4e-05', '0.05', '0.42']
0-67 R2 KW (9.745326575163517, 0.044943234325522656) means [np.float64(60.5), np.float64(55.9), np.float64(48.6), np.float64(62.8), np.float64(52.4)]
    T1 ['0.5', '0.51', '0.38', '0.31', '0.52']
    T2 ['1', '1', '1', '1', '1']
201-268 R1 KW (1.9759446385462334, 0.7401835114792166) means [np.float64(101.4), np.float64(100.9), np.float64(100.3), np.float64(198.8), np.float64(101.5)]
    T1 ['0.5', '0.47', '0.55', '0.34', '0.54']
    T2 ['0.5', '0.6', '0.34', '0.032', '0.8']
[... 4 more lines not kept]
```

**Agent**

AC test result so far: 194 AC units (paper 453), no Kruskal–Wallis significant at 0.01, and no consistent responses. Now prototyping the clock check (true vs shifted onsets).

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && PYTHONPATH=entries/001199-gao-2025 python - <<'EOF'
import pandas as pd, numpy as np, pickle, tfus, time
pd.set_option('display.width',250); pd.set_option('display.max_rows',300)
d=pickle.load(open('all.pkl','rb'))
s=pd.read_csv('survey.csv')
c=pd.DataFrame([tfus.parse_condition(i,n) for i,n in zip(s.identifier,s.notes)])
s=pd.concat([s,c],axis=1)
t=time.time(); rows=[]
for _,r in s.iterrows():
    v=d[r.path]; sp=[u for u in np.split(v['st'],v['idx'][:-1]) if len(u)>2000]
    if not sp: continue
    tr=v['tr'][(v['tr']>1.5)&(v['tr']<v['tr'].max()-1.5)]
    rows.append(dict(rat=r.subj, rec=r.rec, target=r.target, prf=r.prf, n=len(sp), true=tfus.modulation_fraction(sp,tr), shifted=tfus.modulation_fraction(sp,tr+1.25)))
print(time.time()-t)
m=pd.DataFrame(rows)
m['grp']=np.where(m.rat.isin(['BH590','BH594','BH596','BH615']),'2024','2025')
print(m.groupby(['grp','rec','target']).agg(files=('n','size'),units=('n','sum'),true=('true','mean'),shifted=('shifted','mean')).to_string())
from scipy import stats
for (g,rec),x in m[m.target!='none'].groupby(['grp','rec']): print(g,rec, len(x), stats.wilcoxon(x.true,x.shifted).pvalue if len(x)>5 else None, (x.true>x.shifted).sum())
EOF
```

```
5.311033010482788
                 files  units      true   shifted
grp  rec target                                  
2024 S1  POM        43    960  0.435630  0.149765
         S1         49    966  0.351013  0.115567
         none        4     91  0.000000  0.025000
2025 AC  S1         27    153  0.011023  0.004613
         S1-6        9     53  0.044444  0.037037
         none        7     65  0.000000  0.006803
     POm CG1         2      8  0.125000  0.000000
         NEW         2     10  0.000000  0.000000
         S1         24    202  0.020833  0.010119
         S1-6       10     48  0.000000  0.000000
         SEP         1     13  0.000000  0.000000
         none        8     33  0.077083  0.000000
         y-1         1      6  0.000000  0.000000
     S1  CG1         3     11  0.000000  0.000000
         S1         22    328  0.052807  0.058995
         S1-6        8     95  0.000000  0.000000
         none        6     64  0.000000  0.069444
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && PYTHONPATH=entries/001199-gao-2025 python - <<'EOF'
import pandas as pd, numpy as np, pickle, tfus
np.set_printoptions(linewidth=250,precision=0,suppress=True)
d=pickle.load(open('all.pkl','rb'))
s=pd.read_csv('survey.csv')
c=pd.DataFrame([tfus.parse_condition(i,n) for i,n in zip(s.identifier,s.notes)])
s=pd.concat([s,c],axis=1)
bins=np.arange(-1.2,1.2001,0.05)
for _,r in s[s.subj.isin(['BH646','BH648','BH650','BH655','BH657','BH658','BH608','BH654'])&(s.rec=='S1')].sort_values(['subj','prf']).iterrows():
    v=d[r.path]; sp=[u for u in np.split(v['st'],v['idx'][:-1]) if len(u)>2000]
    if not sp: continue
    tot=np.zeros(len(bins)-1)
    for u in sp:
        for t in v['tr']: tot+=np.histogram(u-t,bins)[0]
    print(f"{r.subj} {r.prf} {r.target:5s} n={len(sp):2d}", tot/tot.mean()*100)
EOF
```

```
BH608 30.0 S1    n= 1 [103.  93. 110.  52. 113.  86.  91.  96.  84. 126. 126. 124. 137. 123. 123.  95.  81.  96. 109. 110. 103.  81.  89.  88. 110. 116. 103.  77. 107. 132. 123. 113.  93.  93. 107.  95.  85.  84.  95. 123.  81.  88.  92.  98.  78.  88.  82.  99.]
BH608 1500.0 S1    n= 1 [110. 101.  79.  99. 129. 113.  79.  94.  81. 116. 109. 101. 149.  90. 119. 146.  90. 125. 116. 107. 101.  82.  88. 125.  72.  85. 112. 119.  96. 131.  85.  62. 104.  90. 106.  94.  90. 118. 118.  93. 101.  88. 100.  82.  76.  65.  81.  81.]
BH608 4500.0 S1    n= 1 [113.  83. 104.  80. 112. 108.  90.  82.  94.  93. 113.  93. 108.  83.  91. 100. 102. 123.  90.  95. 102. 107. 108.  99. 111. 112.  94.  80. 100. 109.  89. 102. 102.  93. 123.  99.  87. 105. 108. 115. 112.  84.  86.  97. 108. 105. 103. 102.]
BH646 30.0 S1-6  n=22 [110. 111. 102. 114.  87.  73.  87. 101. 104.  91. 108. 105. 114.  94. 113. 114. 100. 120. 121.  94. 101.  98.  99.  88.  91. 110.  98.  89. 104. 117. 117.  92.  84. 102.  87.  91.  90.  85.  92. 100.  99.  89. 103.  99. 109. 108. 100.  94.]
BH646 300.0 S1    n=27 [ 94.  90.  92.  88.  83.  86.  90.  87.  90. 111. 108.  93.  84.  85. 104. 102. 119. 114. 103. 103. 110.  83.  87.  91.  94. 101. 109. 111.  92. 109.  96. 120. 110. 108. 105. 110. 104.  93.  93. 106. 108.  98. 127. 120. 104.  92.  97.  95.]
BH646 1500.0 S1    n=29 [ 78.  97.  96.  84.  85. 104. 108.  91.  94.  91.  98. 113.  96.  95.  95.  97.  94. 102.  99. 104. 100.  97.  89.  97. 105. 105. 107. 102. 100. 114. 114. 100.  90.  97.  79. 100.  99.  98.  98. 114. 119. 116. 111. 120. 115.  97. 103.  93.]
BH646 3000.0 S1-6  n=21 [ 86.  83.  94. 126. 120. 110. 112.  87.  88.  88. 119. 118. 110. 106. 108. 114. 108. 114.  98. 120.  98.  91. 107.  98.  88.  95. 109. 111.  97.  92. 100. 104. 112. 104.  88.  81.  77.  94.  91. 101.  92.  78.  84.  98.  89. 109. 102.  99.]
BH646 4500.0 S1    n=29 [ 90.  91.  93. 103. 106. 105.  89. 102. 114. 111. 101. 104.  89.  90. 107.  89.  93. 110.  99. 105. 114. 118. 104. 119
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; ls questions | grep 001199; grep -n "sanity\|claim:" tools/entry.py | head -30
```

```
Sun Nov  1 09:19:59 UTC 2026
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
196:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
197:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Gao et al. (2025) from dandiset 001199\n\n**Paper.** Gao H, Ramachandran S, Yu K, He B (2025). Transcranial Focused Ultrasound Modulates\nFeedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively Activating Excitatory\nNeurons. *J Neurosci* 45(23):e2218242025.\n[doi:10.1523/jneurosci.2218-24.2025](https://doi.org/10.1523/jneurosci.2218-24.2025). The claims\nfile was written from the version of record in PubMed Central (PMC12139594), with its Methods and\nall figure legends; the paper has no supplement.\n\n**Dandiset.** [DANDI:001199](https://dandiarchive.org/dandiset/001199/0.250829.1250), version\n0.250829.1250. The paper does not cite this dandiset: its Methods name dandiset 000946 as the\nrepository of all its data, with no version. 001199 has four published versions (0.250712.1551,\n0.250713.1101, 0.250828.1941, 0.250829.1250). The cell below shows that all four and the draft\nhold the same 229 files (same paths and blobs) and differ only in metadata the analysis does not\nuse (the order of contributors). The most recent published version is pinned, as the protocol\nsays when the paper cites none.\n\n**What the dandiset holds.** Sorted units (spike times only) and trial tables for 13 rats, recorded\nin August and September 2024 (4 rats) and February to July 2025 (9 rats). There are no spike\nwaveforms and no RSU or FSU labels, every session uses PD 200 us, and AC recordings come from 7 rats.\n\n**Claims.** The claims file (`claims/001199/10.1523-jneurosci.2218-24.2025.yaml`) has 33 claims.\n\n| Claim | Tested here | Why not |\n|---|---|---|\n| subjects | yes | |\n| fig11b-ac-responses | yes | |\n| fig2-target-artifact | no | raw voltage and target-determination trials not in the dandiset |\n| fig4-unit-counts, fig5-unit-counts, fig6-unit-counts | no | RSU and FSU types need waveforms, not in the dandiset |\n| fig4-timelocked-rsu-3000, fig4-postsonication-3000, fig4-30hz-responses, fig4-no-fsu-change | no | as above (types) |\n| fig5a-sham-no-response, fig5b-cg1-control-no-response | no | types; and no CG1 session at 3,000 Hz |\n| fig6a-s1-rsu-timelocked-high-prf, fig6a-s1-rsu-delayed, fig6b-s1-fsu-prf, fig6c-pom-rsu-prf, fig6d-pom-fsu-prf | no | types |\n| fig7-9-unit-counts, fig7a to fig7d, fig8a, fig8b, fig9a, fig9b | no | the DC series (PDs other than 200 us) are not in the dandiset; and types |\n| fig10a-dsttc-3000-during, fig10a-dsttc-3000-post, fig10b-dsttc-30, fig10c-sttc-constant-pd | no | types |\n| fig10d-sttc-60dc, fig10e-sttc-30hz-dc, fig10f-sttc-3000-dc | no | DC series missing; and types |\n| fig11c-ac-to-s1-30hz, fig11d-ac-to-s1-3000 | no | S1 RSU and FSU types |\n\nEvery file is streamed from the archive; nothing is written to disk.\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy import stats\n\nimport tfus\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nassets = tfus.list_assets()\nversions = [\"0.250712.1551\", \"0.250713.1101\", \"0.250828.1941\", \"0.250829.1250\", \"draft\"]\npinned = set(zip(assets.path, assets.blob))\nfor v in versions:\n    a = tfus.list_assets(v)\n    print(f\"version {v}: {len(a)} assets, {a['size'].sum()} bytes, \"\n          f\"(path, blob) pairs differing from the pinned version: {len(pinned ^ set(zip(a.path, a.blob)))}\")\nm_first, m_pin = tfus.version_metadata(versions[0]), tfus.version_metadata()\nprint(\"metadata fields that differ between 0.250712.1551 and the pinned version:\",\n      sorted(k for k in set(m_first) | set(m_pin) if m_first.get(k) != m_pin.get(k)))\nprint(\"\\nDandiset description (pinned version):\\n\", m_pin[\"description\"])\nprint(\"\\nassetsSummary numberOfSubjects:\", m_pin[\"assetsSummary\"][\"numberOfSubjects\"],\n      \"; variableMeasured:\", m_pin[\"assetsSummary\"][\"variableMeasured\"])\n\"\"\")\n\ncode(r\"\"\"\nstarted = time.time()\nfiles = tfus.read_many(assets.asset_id.tolist(), spikes=True)\nprint(f\"read {len(files)} files from dandiset {tfus.DANDISET_ID} version {tfus.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\nrows = []\nfor (_, a), f in zip(assets.iterrows(), files):\n    c = tfus.parse_condition(f[\"identifier\"], f[\"notes\"])\n    lab = f[\"celltype_label\"]\n    rows.append({\n        \"path\": a.path, \"rat\": f[\"subject_id\"], \"start\": f[\"session_start\"][:19], \"identifier\": f[\"identifier\"],\n        \"notes\": f[\"notes\"], \"data_collection\": f[\"data_collection\"], \"device\": f[\"device\"],\n        \"n_electrodes\": f[\"n_electrodes\"], \"n_units\": f[\"n_units\"], \"n_trials\": len(f[\"trial_start\"]),\n        \"label_values\": \"\" if lab is None else \",\".join(sorted(set(lab))),\n        \"n_pass\": sum(len(s) > tfus.MIN_SPIKES for s in f[\"spikes\"]), **c})\ninfo = pd.DataFrame(rows)\ninfo[\"cohort\"] = np.where(info.rat.isin([\"BH590\", \"BH594\", \"BH596\", \"BH615\"]), \"2024\", \"2025\")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach check of the description against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Files per rat and cohort (cohort by the identifier format; see tfus.py):\")\nprint(info.groupby([\"cohort\", \"rat\"]).agg(files=(\"path\", \"size\"), first=(\"start\", \"min\"), last=(\"start\", \"max\"),\n                                          units=(\"n_units\", \"sum\"), units_over_2000=(\"n_pass\", \"sum\")).to_string())\nprint(\"\\nDistinct rats:\", info.rat.nunique(), \"; subject age field values:\", sorted({f['age'] for f in files}),\n      \"; sex:\", sorted({f['sex'] for f in files}))\nprint(\"\\nDevices:\", info.device.value_counts().to_dict())\nprint(\"Electrodes per file:\", info.n_electrodes.value_counts().to_dict(),\n      \"; electrode locations:\", sorted({tuple(f['electrode_locations']) for f in files}))\nprint(\"\\nUnits table columns:\", pd.Series([\",\".join(f[\"units_columns\"]) for f in files]).value_counts().to_dict())\nprint(\"celltype_label description:\", sorted({f[\"units_descriptions\"].get(\"celltype_label\", \"\") for f in files} - {\"\"}))\nprint(\"celltype_label values per file:\", info.label_values.value_counts().to_dict())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe archive's summary says 13 subjects, as the files hold. Every file's age is P24W. The units\ntables hold spike times and, in 96 files, a `celltype_label` column described as \"label 1 = RSU,\nlabel 2 = FSU\". No file holds a 1 or a 2: the column holds 0 in the files of BH590 and BH594 and\nthe area of the unit (S1 or POm) in those of BH596 and BH615. The 133 files of the 2025 cohort\nhave no such column. No file holds waveforms. So the dandiset gives no way to type units as RSU or\nFSU, which the paper does from the waveforms (Methods, Neuronal type classification). The\ndescription says S1 is recorded with 64-channel probes and POm with 32-channel probes; the files\nlist A1x64 probes (with and without z-coating) in the 2024 cohort and the A1x32-Poly3 probe of the\npaper in the 2025 cohort. Electrode locations are all \"unknown\".\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Conditions (recording area, target, PRF, voltage written in the identifier):\")\nprint(info.groupby([\"cohort\", \"rec\", \"target\", \"prf\", \"volt\"], dropna=False).size().rename(\"files\").to_string())\nprint(\"\\nPD values in identifiers:\", info.pd.value_counts(dropna=False).to_dict())\nprint(\"data_collection values:\", info.data_collection.value_counts().to_dict())\nprint(\"\\nIdentifier tags:\", info.tags.value_counts().to_dict())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nEvery stimulated file has PD 200 us, so only the constant-PD series of the paper (Fig. 4, 6) is\nhere; the duty-cycle series of Fig. 7 to 9 (PDs of 2 to 30,000 us) is not. Voltage is written only\nin the 2024 identifiers (5, 10 or 15 V); the paper used 5 V (88 kPa in situ). The\n`data_collection` field gives \"PRESSURE:67V\" for most 2024 files whatever the identifier says (the\n67 is the ultrasound duration), so it does not state the pressure. In the 2025 files neither field\ngives a voltage. Targets other than S1 and sham appear: POM (stimulation at POm, not in the paper),\nCG1 (the paper's control, here at 300 and 4,500 Hz, where the paper used 3,000 Hz), and \"S1-6\",\n\"NEW\", \"y-1\" and \"SEP\", which nothing in the dandiset explains.\n\"\"\")\n\ncode(r\"\"\"\n# Trials: counts, durations, intersonication intervals (Methods: 500 trials, ISI 2.5 s with 10% jitter).\niti = np.concatenate([np.diff(f[\"trial_start\"]) for f in files])\ndur = np.concatenate([f[\"trial_stop\"] - f[\"trial_start\"] for f in files])\nprint(\"Trials per file:\", info.n_trials.value_counts().sort_index().to_dict())\nprint(\"Trial duration (stop - start), s: min %.4f max %.4f\" % (dur.min(), dur.max()))\nprint(\"Interval between trial starts, s: percentiles 0, 1, 50, 99, 100 =\", np.round(np.percentile(iti, [0, 1, 50, 99, 100]), 3))\nspk = np.concatenate([np.concatenate(f[\"spikes\"]) for f in files if f[\"n_units\"]])\nprint(\"Spike times, s: min %.3f max %.1f; unsorted units: %d\" % (spk.min(), spk.max(),\n      sum(int(np.any(np.diff(s) < 0)) for f in files for s in f[\"spikes\"])))\n\n# Recordings deposited twice: identical spike trains, and files sharing a trial table.\ninfo[\"spike_key\"] = [hash(np.concatenate(f[\"spikes\"]).round(6).tobytes()) if f[\"n_units\"] else None for f in files]\ninfo[\"trial_key\"] = [hash(np.round(f[\"trial_start\"], 5).tobytes()) for f in files]\ndup = info[info.duplicated(\"spike_key\", keep=False) & info.spike_key.notna()]\nprint(\"\\nFiles with identical spike trains:\")\nprint(dup[[\"path\", \"identifier\", \"notes\", \"n_units\"]].to_string(index=False))\nshared = info[info.duplicated(\"trial_key\", keep=False)].sort_values([\"trial_key\", \"path\"])\nprint(f\"\\n{len(shared)} files share their trial table with another file, in \"\n      f\"{shared.trial_key.nunique()} groups; areas per group:\")\ngrp = shared.groupby(\"trial_key\").agg(rat=(\"rat\", \"first\"), areas=(\"rec\", lambda x: \"+\".join(sorted(x))),\n                                      targets=(\"target\", lambda x: \"/\".join(sorted(set(x)))),\n                                      prf=(\"prf\", \"first\"), starts=(\"start\", lambda x: \" \".join(sorted(x))))\nprint(grp.sort_values([\"rat\", \"prf\"]).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nTrials number 499 in most files (the paper: 500), and fewer in some (113 to 480); one 2024 baseline\nhas 400 and two 2025 sham files 149. Each trial lasts 2.2 s, and trial starts are 2.25 to 2.75 s\napart, the 2.5 s with 10% jitter of the Methods. Spike times are sorted.\n\nTwo files hold the same spike trains and trial table: BH646 `ses-None` and `ses-20250308T003900`,\nboth AC at 30 Hz. The first is counted once, as the second. In the 2025 cohort files of two areas\nshare a trial table, which shows that they are the two probes of one session: S1 with AC, or S1\nwith POm, matching the paper's two areas per session. The session start times of such a pair differ\nby minutes, and for BH608 the two sham files (POm, S1) share a trial table though their start times\nare five months apart (2025-02-06 and 2025-07-11), so `session_start_time` does not date a session\nin this cohort. In the BH608 30 Hz pair the S1 file says stimulation at S1 and the POm file\nstimulation at \"SEP\". In the 2024 cohort each file is one session; BH596 and BH615 files hold S1\nand POm units (by `celltype_label`), BH590 and BH594 files S1 only.\n\"\"\")\n\ncode(r\"\"\"\ninfo_u = info[info.path != \"sub-BH646/sub-BH646_ses-None_ecephys.nwb\"].copy()   # the duplicate, counted once\nkeep = set(info_u.index)\n\n\ndef unit_area(i, k):\n    f, r = files[i], info.loc[i]\n    if r.cohort == \"2024\":\n        lab = f[\"celltype_label\"][k]\n        return lab if lab in (\"S1\", \"POm\") else \"S1\"   # BH590/BH594 files: S1 probe only (notes, device)\n    return r.rec\n\n\n# Clock check: fraction of units (more than 2,000 spikes) whose count in 0-400 ms after the trial start\n# differs from 400 ms before it (paired Wilcoxon, p < 0.01), with the true starts and with the starts\n# shifted by half an intersonication interval.\nrows = []\nfor i in keep:\n    f, r = files[i], info.loc[i]\n    sp = [s for s in f[\"spikes\"] if len(s) > tfus.MIN_SPIKES]\n    if not sp:\n        continue\n    on = f[\"trial_start\"][(f[\"trial_start\"] > 1.5) & (f[\"trial_start\"] < f[\"trial_start\"].max() - 1.5)]\n    rows.append({\"cohort\": r.cohort, \"rec\": r.rec, \"target\": r.target, \"rat\": r.rat, \"prf\": r.prf, \"units\": len(sp),\n                 \"true\": tfus.modulation_fraction(sp, on), \"shifted\": tfus.modulation_fraction(sp, on + tfus.SHIFT_S)})\nclock = pd.DataFrame(rows)\nclock[\"kind\"] = np.where(clock.target == \"none\", \"sham\", \"stimulated\")\nprint(\"Fraction of modulated units, mean over files:\")\nprint(clock.groupby([\"cohort\", \"kind\", \"rec\"]).agg(files=(\"units\", \"size\"), units=(\"units\", \"sum\"),\n                                                   true=(\"true\", \"mean\"), shifted=(\"shifted\", \"mean\")).round(3).to_string())\nfor (c, k), g in clock.groupby([\"cohort\", \"kind\"]):\n    if len(g) > 5:\n        print(f\"{c} {k}: true above shifted in {(g.true > g.shifted).sum()} of {len(g)} files; \"\n              f\"paired Wilcoxon p = {stats.wilcoxon(g.true, g.shifted).pvalue:.2g}\")\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Per-file population PSTH (sum over units with more than 2,000 spikes, % of the file's mean), 25 ms bins.\nbins = np.arange(-0.2, 0.6001, 0.025)\n\n\ndef pop_psth(i):\n    f = files[i]\n    tot = np.zeros(len(bins) - 1)\n    for s in f[\"spikes\"]:\n        if len(s) > tfus.MIN_SPIKES:\n            for t in f[\"trial_start\"]:\n                tot += np.histogram(s - t, bins)[0]\n    return tot / tot.mean() * 100 if tot.sum() else tot\n\n\nshow = info_u[(info_u.n_pass > 0) & (((info_u.rat == \"BH615\") & info_u.identifier.str.contains(\"300_200_67_10_S1|3000_200_67_15_S1$\"))\n               | ((info_u.rat == \"BH648\") & (info_u.prf == 4500)) | ((info_u.rat == \"BH594\") & info_u.identifier.str.contains(\"coating_3000_200_67_10$|coating_BASELINE\")))]\nnp.set_printoptions(linewidth=220, precision=0, suppress=True)\nprint(\"bin starts (ms):\", (bins[:-1] * 1000).astype(int))\npsth_rows = {}\nfor i, r in show.iterrows():\n    psth_rows[f\"{r.identifier} ({r.rec})\"] = pop_psth(i)\n    print(f\"{r.identifier:32s} {r.rec:4s}\", psth_rows[f'{r.identifier} ({r.rec})'])\nfig, ax = plt.subplots(figsize=(9, 3.5))\nfor k, v in psth_rows.items():\n    ax.plot(bins[:-1] * 1000, v, label=k, drawstyle=\"steps-post\")\nax.axvspan(0, 67, color=\"0.9\")\nax.set_xlabel(\"time from trial start (ms)\"); ax.set_ylabel(\"population rate (% of mean)\"); ax.legend(fontsize=7)\nax.set_yscale(\"log\")\nprint(\"plotted range: %.0f to %.0f %%\" % (min(v.min() for v in psth_rows.values()), max(v.max() for v in psth_rows.values())))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nIn the 2024 cohort the trial starts are the sonication onsets, as far as the spikes show. The\nfraction of units modulated in the 400 ms after a trial start is about three times that with\nstarts shifted by 1.25 s, in most stimulated files, and near zero in the sham files. Two BH615\nsessions (300 Hz at 10 V, 3,000 Hz at 15 V) show a burst of detected spikes confined to the first\nthree 25 ms bins (0 to 75 ms), the 67 ms of sonication, which looks like an artefact locked to the\nultrasound. Other files show the paper's delayed increase, from about 125 to 200 ms.\n\nIn the 2025 cohort, which holds all the AC recordings, this could not be established for most\nsessions. Its files show no more modulation with the true starts than with shifted ones. The one\nexception is BH648 at 4,500 Hz, where the S1 population rises from about 200 ms after the trial\nstart, the delay of the paper's postsonication responses. Its AC file shares that trial table. For\nthe other 2025 sessions the outputs cannot tell missing responses from trial times that are not\nthe sonication onsets.\n\"\"\")\n\ncode(r\"\"\"\n# Units with more than 2,000 spikes, by area and condition (untyped), against the paper's typed totals.\nrows = []\nfor i in keep:\n    r = info.loc[i]\n    for k, s in enumerate(files[i][\"spikes\"]):\n        if len(s) > tfus.MIN_SPIKES:\n            rows.append({\"cohort\": r.cohort, \"rat\": r.rat, \"area\": unit_area(i, k), \"target\": r.target,\n                         \"prf\": r.prf, \"volt\": r.volt, \"file\": i})\nunits = pd.DataFrame(rows)\nprint(\"Units with more than 2,000 spikes:\", len(units), \"of\", int(info_u.n_units.sum()))\nt = units[units.target.isin([\"S1\", \"S1-6\", \"none\", \"CG1\"])].copy()\nt[\"cond\"] = np.where(t.target == \"none\", \"sham\", np.where(t.target == \"CG1\", \"CG1 \" + t.prf.astype(\"Int64\").astype(str),\n                                                          t.prf.astype(\"Int64\").astype(str) + \" Hz\"))\nprint(pd.crosstab([t.area], t.cond).to_string())\npaper = pd.DataFrame({\"S1 (RSU+FSU)\": [148 + 61, 312 + 54, 1050 + 247, 31 + 53, 12 + 34],\n                      \"POm (RSU+FSU)\": [189 + 43, 233 + 17, 913 + 106, 67 + 67, 55 + 42]},\n                     index=[\"30 Hz\", \"3000 Hz\", \"five PRFs\", \"sham\", \"CG1 at 3000 Hz\"])\nprint(\"\\nPaper's typed totals (Fig. 4, 5 and 6 legends), for comparison:\")\nprint(paper.to_string())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nWithout types, the dandiset holds fewer units than the paper's typed totals in every condition:\nthe cross-tabulation above against the paper's table. The paper counts 366 S1 units and 250 POm\nunits at 3,000 Hz alone. All counts here include the 10 and 15 V sessions, which the paper does not\ndescribe.\n\"\"\")\n\nmd(r\"\"\"\n## subjects\n\n> Simultaneous S1 and POm recordings were made in 16 rats, and S1 and auditory cortex recordings in\n> a further 12 rats.\n\nCriterion: counts of distinct rats with sessions of each recording pair under the paper's\nconditions (S1-targeted tFUS, sham or CG1 control). A session is a file in the 2024 cohort and a\ngroup of files sharing a trial table in the 2025 cohort (data check). A session holds an area when\nit has a unit of that area. Targets counted as the paper's conditions: S1, sham, CG1; \"S1-6\" is\ncounted as S1-targeted under reading (a) and left out under reading (b), as nothing says what it\nis. A variant counts any rat with files of both areas, simultaneous or not.\n\"\"\")\n\ncode(r\"\"\"\ndef sessions_table(targets):\n    rows = []\n    for i in keep:\n        r = info.loc[i]\n        if r.target not in targets:\n            continue\n        areas = {unit_area(i, k) for k in range(len(files[i][\"spikes\"]))}\n        key = (r.rat, r.trial_key) if r.cohort == \"2025\" else (r.rat, i)\n        rows += [{\"rat\": r.rat, \"session\": key, \"area\": a} for a in areas]\n    s = pd.DataFrame(rows).groupby([\"rat\", \"session\"]).area.agg(lambda x: set(x)).reset_index()\n    return s\n\n\nreadings = {\"(a) S1, S1-6, sham, CG1\": {\"S1\", \"S1-6\", \"none\", \"CG1\"}, \"(b) S1, sham, CG1\": {\"S1\", \"none\", \"CG1\"}}\nsubject_counts = {}\nfor name, tg in readings.items():\n    s = sessions_table(tg)\n    pom = sorted(s[s.area.apply(lambda a: {\"S1\", \"POm\"} <= a)].rat.unique())\n    ac = sorted(s[s.area.apply(lambda a: {\"S1\", \"AC\"} <= a)].rat.unique())\n    subject_counts[name] = (len(pom), len(ac))\n    print(f\"{name}: simultaneous S1 and POm in {len(pom)} rats {pom}; S1 and AC in {len(ac)} rats {ac}; \"\n          f\"in both groups: {sorted(set(pom) & set(ac))}\")\nby_rat = units.groupby(\"rat\").area.agg(lambda x: set(x))\nprint(\"Variant, any files of both areas: S1 and POm\", sorted(by_rat[by_rat.apply(lambda a: {'S1', 'POm'} <= a)].index),\n      \"; S1 and AC\", sorted(by_rat[by_rat.apply(lambda a: {'S1', 'AC'} <= a)].index),\n      \"(units with more than 2,000 spikes, any target)\")\nprint(\"Rats with any AC file:\", sorted(info.loc[info.rec == \"AC\", \"rat\"].unique()))\ns5 = info_u[(info_u.volt == 5) & (info_u.target == \"S1\")]\nprint(\"2024 rats with an S1-targeted 5 V session:\", sorted(s5.rat.unique()))\nprint(\"Paper: 16 S1 and POm rats, 12 further S1 and AC rats.\")\n\nr946 = requests.get(\"https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=1000\",\n                    timeout=60).json()\np946 = [a[\"path\"] for a in r946[\"results\"]]\nwhile r946[\"next\"]:\n    r946 = requests.get(r946[\"next\"], timeout=60).json()\n    p946 += [a[\"path\"] for a in r946[\"results\"]]\nsubj946 = sorted({p.split(\"/\")[0].replace(\"sub-\", \"\") for p in p946 if not p.startswith(\"sub-STTC\")})\ndates946 = sorted({p.split(\"ses-\")[1][:8] for p in p946 if \"ses-\" in p})\nprint(f\"\\nDandiset 000946 (the paper's named repository), version 0.250829.1249, asset paths only: \"\n      f\"{len(p946)} files, rats {subj946}, session dates {dates946[0]} to {dates946[-1]}\")\nprint(\"Rats of 001199 also in 000946:\", sorted(set(info.rat) & set(subj946)))\n\"\"\", tags=[\"claim:subjects\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** Under both readings the dandiset holds simultaneous S1 and POm\nrecordings from 6 rats (paper 16) and S1 and AC recordings from 6 rats (paper 12). Both counts are\nbelow the paper's and neither is above it, the claims file's rule for a partial result. Two rats\n(BH648, BH658) are in both groups, where the paper's AC group is \"another group of rats\". The\npaper's named repository, 000946, lists 19 other rats recorded from 2023 to March 2024; of the 13\nrats here only BH594, an S1-only rat here, has a file there. So the dandiset may not hold the\npaper's rats at all.\n\"\"\")\n\nmd(r\"\"\"\n## fig11b-ac-responses\n\n> Auditory cortex neurons respond during sonication to 1,500 and 3,000 Hz PRF and after sonication\n> to 30, 1,500, 3,000 and 4,500 Hz, with PRF-dependent responses and the least response at 300 Hz.\n\nCriterion: AC units with more than 2,000 spikes of the S1 and AC rats, the 200 us PD series,\nnormalized rate (R1, R2) in 0 to 67 and 201 to 268 ms, Kruskal-Wallis across the five PRFs at\np < 0.01, then the one-tailed rank-sum test against baseline per PRF (T1, T2) with Bonferroni's\ncorrection, corrected p < 0.01. Bonferroni factors: B1 = 5 (the PRFs compared with baseline in a\nwindow; 10 is shown too, for the two windows together), B2 = 15 (all pairs among the five PRFs and\nthe baseline). Every AC file with stimulation at S1 or S1-6 is used (all 7 rats with AC files); a\nvariant leaves out S1-6. The total is compared with the paper's 453.\n\"\"\")\n\ncode(r\"\"\"\ndef ac_units(targets, sham=False):\n    rows = []\n    for i in keep:\n        r = info.loc[i]\n        if r.rec != \"AC\" or (r.target not in targets):\n            continue\n        sp = [s for s in files[i][\"spikes\"] if len(s) > tfus.MIN_SPIKES]\n        if not sp:\n            continue\n        nr = tfus.normalized_rates(tfus.unit_counts(sp, files[i][\"trial_start\"], tfus.WINDOWS), tfus.WINDOWS)\n        nr[\"rat\"], nr[\"prf\"], nr[\"target\"], nr[\"file\"] = r.rat, (0 if sham else r.prf), r.target, i\n        rows.append(nr)\n    return pd.concat(rows, ignore_index=True)\n\n\nac = ac_units({\"S1\", \"S1-6\"})\nac_sham = ac_units({\"none\"}, sham=True)\nprint(\"AC units with more than 2,000 spikes:\", len(ac), \"(paper 453); left out for no prestimulus spike:\",\n      int(ac[\"R1_0-67\"].isna().sum()))\nprint(\"AC units with 2,000 spikes or fewer in these files:\",\n      sum(len(s) <= tfus.MIN_SPIKES for i in set(ac.file) for s in files[i][\"spikes\"]))\nprint(\"\\nUnits per rat and PRF (paper: 30 Hz 83, 300 Hz 59 by difference, 1,500 Hz 107, 3,000 Hz 104, 4,500 Hz 100):\")\nprint(pd.crosstab(ac.rat, ac.prf, margins=True).to_string())\nprint(\"Sham AC units (no tFUS), per rat:\", ac_sham.rat.value_counts().sort_index().to_dict())\n\n\ndef panel(df, label):\n    out = []\n    for w in (\"0-67\", \"201-268\"):\n        for R in (\"R1\", \"R2\"):\n            g = [df[df.prf == p][f\"{R}_{w}\"].values for p in tfus.PRFS]\n            h, pk = tfus.kruskal(g)\n            for T in (\"T1\", \"T2\"):\n                p = np.array([tfus.vs_baseline(df[df.prf == q], w, R, T) for q in tfus.PRFS])\n                row = {\"set\": label, \"window\": w, \"R\": R, \"T\": T, \"KW_H\": round(h, 2), \"KW_p\": pk}\n                for q, m, pv in zip(tfus.PRFS, [np.nanmean(x) for x in g], p):\n                    row[f\"mean_{q}\"] = round(m, 1)\n                    row[f\"p_{q}\"] = pv\n                for B, fac in ((\"B1\", 5), (\"B1x2\", 10), (\"B2\", 15)):\n                    row[f\"sig_{B}\"] = \",\".join(str(q) for q, pv in zip(tfus.PRFS, p) if pv * fac < 0.01)\n                row[\"lowest\"] = tfus.PRFS[int(np.nanargmin([np.nanmean(x) for x in g]))]\n                out.append(row)\n    return pd.DataFrame(out)\n\n\nres = panel(ac, \"S1 and S1-6\")\nfmt = res.copy()\nfor c in [c for c in fmt if c.startswith(\"p_\") or c == \"KW_p\"]:\n    fmt[c] = fmt[c].map(lambda v: f\"{v:.2g}\")\nprint(\"\\nUncorrected one-tailed p against baseline per PRF; sig_ lists PRFs significant after each Bonferroni factor:\")\nprint(fmt.to_string(index=False))\n\"\"\", tags=[\"claim:fig11b-ac-responses\"])\n\ncode(r\"\"\"\n# Reference: the same tests on AC units of the sham sessions (no tFUS), as one group per window.\nrows = []\nfor w in (\"0-67\", \"201-268\"):\n    for R in (\"R1\", \"R2\"):\n        for T in (\"T1\", \"T2\"):\n            rows.append({\"window\": w, \"R\": R, \"T\": T, \"mean\": round(np.nanmean(ac_sham[f\"{R}_{w}\"]), 1),\n                         \"p_increase\": f\"{tfus.vs_baseline(ac_sham, w, R, T):.2g}\", \"n\": int(ac_sham[f'{R}_{w}'].notna().sum())})\nprint(\"Sham AC units:\")\nprint(pd.DataFrame(rows).to_string(index=False))\n\n# Variant: S1-6 left out.\nres_b = panel(ac[ac.target == \"S1\"], \"S1 only\")\nprint(\"\\nVariant, S1-6 sessions left out; units per PRF:\", ac[ac.target == \"S1\"].prf.value_counts().sort_index().to_dict())\nprint(res_b[[\"window\", \"R\", \"T\", \"KW_H\", \"KW_p\", \"mean_30\", \"mean_300\", \"mean_1500\", \"mean_3000\", \"mean_4500\",\n             \"sig_B1\", \"sig_B2\", \"lowest\"]].to_string(index=False))\n\n# By rat: mean normalized rate (R1) per PRF and window, and the median, which is robust to single units.\nprint(\"\\nBy rat, R1 mean (median) per PRF:\")\nfor w in (\"0-67\", \"201-268\"):\n    tab = ac.groupby([\"rat\", \"prf\"])[f\"R1_{w}\"].agg(lambda x: f\"{x.mean():.0f} ({x.median():.0f})\").unstack()\n    print(f\"window {w}\\n\", tab.to_string())\nprint(\"\\nR1 0-67 ms at 3,000 Hz, largest five units:\", np.round(np.sort(ac[ac.prf == 3000][\"R1_0-67\"].values)[-5:], 1))\nprint(\"R1 medians per PRF, 0-67:\", ac.groupby(\"prf\")[\"R1_0-67\"].median().round(1).to_dict(),\n      \"; 201-268:\", ac.groupby(\"prf\")[\"R1_201-268\"].median().round(1).to_dict())\n\nfig, axes = plt.subplots(1, 2, figsize=(9, 3.2), sharey=True)\nfor ax, w in zip(axes, (\"0-67\", \"201-268\")):\n    m = ac.groupby(\"prf\")[f\"R1_{w}\"].agg([\"mean\", \"sem\"])\n    ax.errorbar(range(5), m[\"mean\"], m[\"sem\"], fmt=\"o\")\n    ax.axhline(100, color=\"0.6\", lw=0.8)\n    ax.set_xticks(range(5), [str(p) for p in tfus.PRFS]); ax.set_title(f\"AC, {w} ms\"); ax.set_xlabel(\"PRF (Hz)\")\naxes[0].set_ylabel(\"normalized rate R1 (%), mean ± SEM\")\nprint(\"plotted means range %.1f to %.1f %%\" % (ac.groupby(\"prf\")[[\"R1_0-67\", \"R1_201-268\"]].mean().min().min(),\n                                              ac.groupby(\"prf\")[[\"R1_0-67\", \"R1_201-268\"]].mean().max().max()))\n\"\"\", tags=[\"claim:fig11b-ac-responses\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** There are 194 AC units with more than 2,000 spikes, against the paper's\n453. No Kruskal-Wallis test across the five PRFs is significant at 0.01 under any reading (p from\n0.028 to 0.74). Under R1 and T2, 1,500 Hz is above baseline during sonication (mean 105.1%,\np = 6.4e-05 uncorrected, below 0.01 under every factor), and nothing else is significant under any\nreading. The paper's pattern needs 1,500 and 3,000 Hz during sonication and 30, 1,500, 3,000 and\n4,500 Hz after it. The 3,000 Hz mean of 204.9% during sonication comes from a few units: its median\nis near 100%. 300 Hz does not have the lowest mean in either window. Under R2 every mean is below\n100%, sham included, because R2 keeps only trials with a prestimulus spike. In the 2025 cohort the\ntrial times could be shown to be sonication onsets only for the BH648 4,500 Hz session (data\ncheck), so the lack of responses may come from the trial tables and not from the neurons.\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| subjects | partially reproduced |\n| fig11b-ac-responses | not reproduced |\n| fig2-target-artifact | blocked, data missing |\n| 26 claims on RSUs and FSUs (Fig. 4 to 10, 11C, 11D) | blocked, data missing |\n| fig7-9-unit-counts and the duty-cycle claims | blocked, data missing (also no duty-cycle series) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n**How the analysis differs from the paper's.** Sessions are taken as the dandiset gives them, with\n\"S1-6\" counted as S1-targeted (a variant leaves it out). The pressure of the 2025 sessions is not\nstated. AC units are all those with more than 2,000 spikes, as the Methods say, in the 7 rats with\nAC files.\n\n**What was found about the dataset.** The dandiset holds spike times and trial tables only: no\nwaveforms, so no RSU or FSU types. Its `celltype_label` column is described as RSU and FSU codes\nbut holds 0 or the area. Only the 200 us PD series is here, with sessions at 10 and 15 V, POm\ntargeting and probe variants the paper does not describe. Its 13 rats were recorded from August\n2024 to July 2025, after the paper's preprint (June 2024). Of them only BH594 has a file in 000946,\nthe dandiset the paper names for its data. Session start times do not date the sessions of the\n2025 cohort. Two files are the same recording. Several target labels are unexplained. In most 2025\nsessions the spikes show no locking to the trial starts.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, \"entries/001199-gao-2025/reproduce_gao_2025.ipynb\")\nprint(\"written\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q nbformat nbclient ipykernel 2>&1|tail -1; python build_nb.py && cd entries/001199-gao-2025 && time jupyter nbconvert --to notebook --execute reproduce_gao_2025.ipynb --output $TMPDIR/exec.ipynb --ExecutePreprocessor.timeout=1800 2>&1 | tail -5
```

```
written 23

Available subcommands: execute kernel kernelspec migrate run troubleshoot
trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.091s
user	0m0.075s
sys	0m0.019s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time python -c "
import nbformat, nbclient
nb=nbformat.read('reproduce_gao_2025.ipynb',4)
c=nbclient.NotebookClient(nb,timeout=1800,kernel_name='python3',resources={'metadata':{'path':'.'}})
try:
    c.execute()
finally:
    nbformat.write(nb,'$TMPDIR/exec.ipynb')
" 2>&1 | tail -20
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	3m26.033s
user	0m31.795s
sys	0m2.360s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('$TMPDIR/exec.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    print('=== CELL', c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'][:6000])
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
        elif 'data' in o and 'text/plain' in o['data']: print(o['data']['text/plain'][:300])
"
```

```
=== CELL None
version 0.250712.1551: 229 assets, 317011048 bytes, (path, blob) pairs differing from the pinned version: 0

version 0.250713.1101: 229 assets, 317011048 bytes, (path, blob) pairs differing from the pinned version: 0

version 0.250828.1941: 229 assets, 317011048 bytes, (path, blob) pairs differing from the pinned version: 0

version 0.250829.1250: 229 assets, 317011048 bytes, (path, blob) pairs differing from the pinned version: 0

version draft: 229 assets, 317011048 bytes, (path, blob) pairs differing from the pinned version: 0

metadata fields that differ between 0.250712.1551 and the pinned version: ['citation', 'contributor', 'datePublished', 'doi', 'id', 'manifestLocation', 'publishedBy', 'url', 'version']

Dandiset description (pinned version):
 In these recordings, we recorded neuronal activities from cortical-thalamocortical (CTC) pathway, including the somatosensory cortex (S1) and posteromedial complex (POm) of the thalamus responded to different Pulse Repetition Frequencies (PRFs ) or Pulse Durations (PDs) and Pressure Levels of transcranial ultrasound focused stimulation (tFUS) using a 128-element transducer to stimulate either at S1or PoM.  Recordings for S1 are taken using 64-channel Cambridge or Neuronexus electrodes and recordings for POm are taken using 32-channel Nueronexus electrodes. Ultrasound stimulation is delivered every 2.5 seconds and each recording has 500 trials. The Ultrasound Duration (UD) and pressure level used in each recording is 67ms. The PRFs, PDs and pressure levels for each recording can be found in the identifier field. For example, in BH596_3000_200_67_10, the PRF is 3000Hz, PD is 200us and pressure level is 10V.  Detailed description about this dataset can be found in the following publication. Please cite the paper if you would use a portion of the dataset. Gao, H., Ramachandran, S., Yu, K., & He, B. (2025). Transcranial Focused Ultrasound Modulates Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by
[... 300 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
d=pickle.load(open('all.pkl','rb')); s=pd.read_csv('survey.csv').set_index('path')
rows=[]
for p,v in d.items():
    for k,u in enumerate(np.split(v['st'],v['idx'][:-1])):
        nd=np.sum(np.diff(u)<0)
        if nd: rows.append((p.split('/')[1][:30], s.loc[p,'identifier'], k, len(u), nd, np.sum(np.diff(u)==0)))
df=pd.DataFrame(rows,columns=['file','id','unit','n','n_decreasing','n_equal'])
print(df.groupby('file').agg(units=('unit','size'),dec=('n_decreasing','sum')).to_string()); print(df.n_decreasing.describe())
EOF
```

```
units  dec
file                                      
sub-BH608_ses-20250709T121000_      1    2
sub-BH608_ses-20250709T130900_      4   12
sub-BH608_ses-20250709T151300_      3    3
sub-BH608_ses-20250711T144700_     20   29
sub-BH608_ses-20250711T144800_      1    1
sub-BH646_ses-20250308T013700_      6    7
sub-BH648_ses-20250306T003000_      1    1
sub-BH648_ses-20250307T034200_      2    2
sub-BH650_ses-20250309T014500_      1    1
sub-BH654_ses-20250226T173900_      2    4
sub-BH655_ses-20250303T200400_      3    6
sub-BH657_ses-20250304T002600_      1    2
sub-BH657_ses-20250304T003000_      9   10
sub-BH657_ses-20250305T152100_      8   10
sub-BH658_ses-20250309T232000_      1    1
sub-BH658_ses-20250310T020800_      1    1
count    64.000000
mean      1.437500
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001199-gao-2025 && python - <<'EOF'
p='tfus.py'; s=open(p).read()
s=s.replace('''def _str(x):
    v = x[()]
    return v.decode() if isinstance(v, bytes) else str(v)''','''def _str(x):
    v = x[()]
    if isinstance(v, np.ndarray):   # some files store a scalar as a one-element array
        v = v.ravel()[0]
    return v.decode() if isinstance(v, bytes) else str(v)''')
s=s.replace('''        out["spikes"] = np.split(st, idx[:-1])''','''        units = np.split(st, idx[:-1])
        # Some units hold spike times out of order (a few per unit); they are sorted here, as the
        # window counts need, and the number of such units is kept for the data check.
        out["n_unsorted"] = int(sum(np.any(np.diff(u) < 0) for u in units))
        out["spikes"] = [np.sort(u) for u in units]''')
s=s.replace('''Files are streamed from the archive at the pinned version; nothing is written to disk.''','''Files are streamed from the archive at the pinned version; nothing is written to disk. Spike
times are sorted per unit on reading, as 64 units in 16 files hold a few out of order.''')
open(p,'w').write(s)
EOF
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('''print("Spike times, s: min %.3f max %.1f; unsorted units: %d" % (spk.min(), spk.max(),
      sum(int(np.any(np.diff(s) < 0)) for f in files for s in f["spikes"])))''','''print("Spike times, s: min %.3f max %.1f" % (spk.min(), spk.max()))
uns = info.assign(n_unsorted=[f["n_unsorted"] for f in files])
print("Units whose spike times are not in order, as stored: %d in %d files (sorted on reading):"
      % (uns.n_unsorted.sum(), (uns.n_unsorted > 0).sum()), uns[uns.n_unsorted > 0].groupby("rat").n_unsorted.sum().to_dict())''')
s=s.replace('''has 400 and two 2025 sham files 149. Each trial lasts 2.2 s, and trial starts are 2.25 to 2.75 s
apart, the 2.5 s with 10% jitter of the Methods. Spike times are sorted.''','''has 400 and two 2025 sham files 149. Each trial lasts 2.2 s, and trial starts are 2.25 to 2.75 s
apart, the 2.5 s with 10% jitter of the Methods. In 64 units of 16 files of the 2025 cohort the
stored spike times are not in increasing order (one to seven places per unit), which breaks the
NWB convention; they are sorted on reading.''')
s=s.replace('''print("bin starts (ms):", (bins[:-1] * 1000).astype(int))''','''print("bin starts (ms):", np.round(bins[:-1] * 1000).astype(int))''')
s=s.replace('''    psth_rows[f"{r.identifier} ({r.rec})"] = pop_psth(i)
    print(f"{r.identifier:32s} {r.rec:4s}", psth_rows[f'{r.identifier} ({r.rec})'])''','''    key = f"{r.rat} {r.identifier} ({r.rec})"
    psth_rows[key] = pop_psth(i)
    print(f"{key:40s}", psth_rows[key])''')
open(p,'w').write(s)
EOF
grep -n "n_unsorted\|ravel" entries/001199-gao-2025/tfus.py | head; date -u
```

```
grep: entries/001199-gao-2025/tfus.py: No such file or directory
Sun Nov  1 09:25:52 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "n_unsorted\|ravel" entries/001199-gao-2025/tfus.py; grep -n "n_unsorted\|np.round(bins" $TMPDIR/build_nb.py | head
```

```
90:        v = v.ravel()[0]
125:        out["n_unsorted"] = int(sum(np.any(np.diff(u) < 0) for u in units))
171:uns = info.assign(n_unsorted=[f["n_unsorted"] for f in files])
173:      % (uns.n_unsorted.sum(), (uns.n_unsorted > 0).sum()), uns[uns.n_unsorted > 0].groupby("rat").n_unsorted.sum().to_dict())
262:print("bin starts (ms):", np.round(bins[:-1] * 1000).astype(int))
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('''# By rat: mean normalized rate''','''# Variant: the 6 rats whose AC file shares a session with an S1 file (BH654 left out).
res_c = panel(ac[ac.rat != "BH654"], "without BH654")
print("\\nVariant, BH654 (no S1 and AC session) left out; units:", int((ac.rat != "BH654").sum()))
print(res_c[["window", "R", "T", "KW_p", "sig_B1", "sig_B2", "lowest"]].to_string(index=False))

# By rat: mean normalized rate''')
open(p,'w').write(s)
EOF
. dev/bin/activate && python build_nb.py && cd entries/001199-gao-2025 && time python -c "
import nbformat, nbclient
nb=nbformat.read('reproduce_gao_2025.ipynb',4)
c=nbclient.NotebookClient(nb,timeout=1800,kernel_name='python3',resources={'metadata':{'path':'.'}})
try:
    c.execute()
finally:
    nbformat.write(nb,'$TMPDIR/exec.ipynb')
" 2>&1 | grep -v WARNING | tail -5; python -c "
import nbformat
nb=nbformat.read('$TMPDIR/exec.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    print('=== CELL', c.metadata.get('tags'))
    for o in c.outputs:
        if 'text' in o: print(o['text'][:3500])
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
" | sed -n '/Files per rat/,/Distinct/p;/Spike times/,/Files with/p;/bin starts/,/plotted/p;/simultaneous/,/Variant, any/p;/AC units with more/,/Sham AC units (no/p;/Uncorrected/,/^=== CELL/p;/Variant, BH654/,/By rat/p'
```

```
written 23

real	3m22.103s
user	0m30.969s
sys	0m2.437s
Files per rat and cohort (cohort by the identifier format; see tfus.py):
              files                first                 last  units  units_over_2000
cohort rat                                                                           
2024   BH590     21  2024-08-16T16:54:00  2024-08-17T00:48:00    162              132
       BH594     28  2024-08-14T15:47:00  2024-08-15T02:32:00   1110              963
       BH596     25  2024-08-23T17:31:00  2024-08-24T02:02:00    261              199
       BH615     22  2024-09-11T16:33:00  2024-09-12T00:55:00    926              723
2025   BH608     12  2025-02-06T16:03:00  2025-07-11T20:22:00    103               63
       BH646     19  2025-03-08T00:39:00  2025-03-08T20:50:00    296              246
       BH648     18  2025-03-06T00:30:00  2025-03-07T23:29:00    209              206
       BH650     18  2025-03-08T21:51:00  2025-03-09T06:17:00    204              186
       BH654     13  2025-02-26T17:39:00  2025-02-27T01:19:00     68               50
       BH655     18  2025-02-27T20:32:00  2025-03-03T23:44:00    106               90
       BH656      1  2025-02-05T21:39:00  2025-02-05T21:39:00     10                8
       BH657     17  2025-03-04T00:26:00  2025-03-05T22:22:00     85               78
[... 68 more lines not kept]
```

**Agent**

Sorting removed the 3,000 Hz outlier (an artefact of unsorted spikes). Checking the remaining outputs.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('$TMPDIR/exec.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.outputs:
        if 'text' in o: print(o['text'][:5000])
" | sed -n '/Files with identical/,/79 files/p;/Fraction of modulated/,/2025 stimulated/p;/Units with more than 2,000 spikes:/,/sham/p;/Sham AC units:/,/S1-6 sessions left/p;/By rat/,$p'
```

```
Files with identical spike trains:
                                               path identifier                         notes  n_units
sub-BH646/sub-BH646_ses-20250308T003900_ecephys.nwb  30_200_67 recording:AC;stimulation:S1-6       12
           sub-BH646/sub-BH646_ses-None_ecephys.nwb  30_200_67 recording:AC;stimulation:S1-6       12

79 files share their trial table with another file, in 39 groups; areas per group:
Fraction of modulated units, mean over files:
                       files  units   true  shifted
cohort kind       rec                              
2024   sham       S1       4     91  0.000    0.025
       stimulated S1      92   1926  0.391    0.132
2025   sham       AC       7     65  0.000    0.007
                  POm      8     33  0.077    0.000
                  S1       6     64  0.000    0.069
       stimulated AC      35    194  0.020    0.013
                  POm     40    287  0.019    0.006
                  S1      33    434  0.035    0.039
2024 stimulated: true above shifted in 50 of 92 files; paired Wilcoxon p = 6.9e-10
2025 sham: true above shifted in 3 of 21 files; paired Wilcoxon p = 0.75
2025 stimulated: true above shifted in 7 of 108 files; paired Wilcoxon p = 0.81
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('$TMPDIR/exec.ipynb',4)
c=[c for c in nb.cells if c.cell_type=='code'][7]
for o in c.outputs:
    if 'text' in o: print(o['text'])
"
```

```
Units with more than 2,000 spikes: 3094 of 3697
cond  1500 Hz  30 Hz  300 Hz  3000 Hz  4500 Hz  CG1 300  CG1 4500  sham
area                                                                   
AC         42     45      29       40       38        0         0    65
POm        66     93      72      110       55        4         4    37
S1        171    344     160      465      103        2         9   151

Paper's typed totals (Fig. 4, 5 and 6 legends), for comparison:
                S1 (RSU+FSU)  POm (RSU+FSU)
30 Hz                    209            232
3000 Hz                  366            250
five PRFs               1297           1019
sham                      84            134
CG1 at 3000 Hz            46             97
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''print(pd.crosstab([t.area], t.cond).to_string())
paper ='''
new='''print("All voltages:")
print(pd.crosstab([t.area], t.cond, margins=True).to_string())
t5 = t[(t.cohort == "2025") | (t.volt == 5) | (t.cond == "sham")]
print("\\nVariant, 2024 files at 5 V (the paper's voltage) and sham, with every 2025 file (voltage not stated):")
print(pd.crosstab([t5.area], t5.cond, margins=True).to_string())
paper ='''
assert old in s; s=s.replace(old,new)
old2='''Without types, the dandiset holds fewer units than the paper's typed totals in every condition:
the cross-tabulation above against the paper's table. The paper counts 366 S1 units and 250 POm
units at 3,000 Hz alone. All counts here include the 10 and 15 V sessions, which the paper does not
describe.'''
new2='''Without types the totals can be set against the paper's RSU and FSU sums only roughly. POm units
are fewer than the paper's in every condition (110 at 3,000 Hz against 250). S1 units at 30 and
3,000 Hz outnumber the paper's when every voltage is counted, as the 64-channel probes of BH594
give many units at 5, 10 and 15 V. At 5 V the S1 counts fall below the paper's in every condition
but 30 Hz.'''
assert old2 in s; s=s.replace(old2,new2)
old3=s[s.index('**Result: not reproduced.** There are 194'):s.index('check), so the lack of responses may come from the trial tables and not from the neurons.')]
new3='''**Result: not reproduced.** There are 194 AC units with more than 2,000 spikes in 7 rats, against
the paper's 453. In the main set no Kruskal-Wallis test across the five PRFs is significant at 0.01
(p from 0.013 to 0.74); with BH654 left out the R2 tests give 0.0095 and 0.006, with every R2 mean
below 100%. Against baseline only 1,500 Hz during sonication is significant, and only under R1
and T2 (mean 105.1%, uncorrected p = 6.4e-05, below 0.01 under every factor). The paper's pattern
needs 1,500 and 3,000 Hz during sonication and 30, 1,500, 3,000 and 4,500 Hz after it. Here no
PRF is above baseline after sonication under any reading, and 300 Hz has the lowest mean only under
R1 during sonication without BH654. Per-rat R1 means lie between 88 and 127%. Under R2 every mean
is below 100%, sham included (69.8%), because R2 keeps only trials with a prestimulus spike. In the
2025 cohort the trial starts could be shown to be sonication onsets only for the BH648 4,500 Hz
session (data '''
s=s.replace(old3,new3)
s=s.replace('''fraction of units modulated in the 400 ms after a trial start is about three times that with
starts shifted by 1.25 s, in most stimulated files, and near zero in the sham files.''','''fraction of units modulated in the 400 ms after a trial start is 0.39 on average, against 0.13
with starts shifted by 1.25 s (true above shifted in 50 of 92 stimulated files), and 0 in the sham
files.''')
s=s.replace('''In the 2025 cohort, which holds all the AC recordings, this could not be established for most
sessions. Its files show no more modulation with the true starts than with shifted ones.''','''In the 2025 cohort, which holds all the AC recordings, this could not be established for most
sessions. Its files show no more modulation with the true starts than with shifted ones (true
above shifted in 7 of 108 stimulated files).''')
open(p,'w').write(s)
EOF
grep -n "subjects\b" $TMPDIR/build_nb.py | head -3
```

```
43:| subjects | yes | |
132:The archive's summary says 13 subjects, as the files hold. Every file's age is P24W. The units
330:## subjects
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "^- id:" claims/001199/*.yaml | awk '{print $3}' | tr '\n' ' '; grep -c "^- id:" claims/001199/*.yaml
```

```
subjects fig2-target-artifact fig4-unit-counts fig4-timelocked-rsu-3000 fig4-postsonication-3000 fig4-30hz-responses fig4-no-fsu-change fig5-unit-counts fig5a-sham-no-response fig5b-cg1-control-no-response fig6-unit-counts fig6a-s1-rsu-timelocked-high-prf fig6a-s1-rsu-delayed fig6b-s1-fsu-prf fig6c-pom-rsu-prf fig6d-pom-fsu-prf fig7-9-unit-counts fig7a-s1-rsu-dc-3000 fig7b-s1-fsu-dc-3000 fig7c-pom-rsu-dc-3000 fig7d-pom-fsu-dc-3000 fig8a-s1-rsu-dc-30 fig8b-s1-fsu-dc-30 fig9a-s1-rsu-60dc fig9b-s1-fsu-60dc fig10a-dsttc-3000-during fig10a-dsttc-3000-post fig10b-dsttc-30 fig10c-sttc-constant-pd fig10d-sttc-60dc fig10e-sttc-30hz-dc fig10f-sttc-3000-dc fig11b-ac-responses fig11c-ac-to-s1-30hz fig11d-ac-to-s1-3000 35
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace("has 33 claims.","has 35 claims.")
s=s.replace('''| 26 claims on RSUs and FSUs (Fig. 4 to 10, 11C, 11D) | blocked, data missing |
| fig7-9-unit-counts and the duty-cycle claims | blocked, data missing (also no duty-cycle series) |''','''| 20 claims on RSUs and FSUs (Fig. 4 to 6, 10A to 10C, 11C, 11D) | blocked, data missing |
| 12 claims on the duty-cycle series (fig7-9-unit-counts, Fig. 7 to 9, 10D to 10F) | blocked, data missing |''')
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && cd entries/001199-gao-2025 && python -c "
import nbformat, nbclient
nb=nbformat.read('reproduce_gao_2025.ipynb',4)
c=nbclient.NotebookClient(nb,timeout=1800,kernel_name='python3',resources={'metadata':{'path':'.'}})
try:
    c.execute()
finally:
    nbformat.write(nb,'$TMPDIR/exec.ipynb')
" 2>&1 | grep -v WARNING | tail -3; python -c "
import nbformat
nb=nbformat.read('$TMPDIR/exec.ipynb',4)
c=[c for c in nb.cells if c.cell_type=='code'][7]
for o in c.outputs:
    if 'text' in o: print(o['text'])
    if o.get('output_type')=='error': print(o['evalue'])
"; date -u
```

```
written 23
/bin/bash: line 9: cd: entries/001199-gao-2025: No such file or directory
Units with more than 2,000 spikes: 3094 of 3697
cond  1500 Hz  30 Hz  300 Hz  3000 Hz  4500 Hz  CG1 300  CG1 4500  sham
area                                                                   
AC         42     45      29       40       38        0         0    65
POm        66     93      72      110       55        4         4    37
S1        171    344     160      465      103        2         9   151

Paper's typed totals (Fig. 4, 5 and 6 legends), for comparison:
                S1 (RSU+FSU)  POm (RSU+FSU)
30 Hz                    209            232
3000 Hz                  366            250
five PRFs               1297           1019
sham                      84            134
CG1 at 3000 Hz            46             97

Sun Nov  1 09:30:21 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cd entries/001199-gao-2025 && python -c "
import nbformat, nbclient
nb=nbformat.read('reproduce_gao_2025.ipynb',4)
c=nbclient.NotebookClient(nb,timeout=1800,kernel_name='python3',resources={'metadata':{'path':'.'}})
try:
    c.execute()
finally:
    nbformat.write(nb,'$TMPDIR/exec.ipynb')
" 2>&1 | grep -v WARNING | tail -3; python -c "
import nbformat
nb=nbformat.read('$TMPDIR/exec.ipynb',4)
for c in nb.cells:
  if c.cell_type!='code': continue
  for o in c.outputs:
    if o.get('output_type')=='error': print('ERR',o['evalue'])
c=[c for c in nb.cells if c.cell_type=='code'][7]
for o in c.outputs:
    if 'text' in o: print(o['text'])
"
```

```
Units with more than 2,000 spikes: 3094 of 3697
All voltages:
cond  1500 Hz  30 Hz  300 Hz  3000 Hz  4500 Hz  CG1 300  CG1 4500  sham   All
area                                                                         
AC         42     45      29       40       38        0         0    65   259
POm        66     93      72      110       55        4         4    37   441
S1        171    344     160      465      103        2         9   151  1405
All       279    482     261      615      196        6        13   253  2105

Variant, 2024 files at 5 V (the paper's voltage) and sham, with every 2025 file (voltage not stated):
cond  1500 Hz  30 Hz  300 Hz  3000 Hz  4500 Hz  CG1 300  CG1 4500  sham   All
area                                                                         
AC         42     45      29       40       38        0         0    65   259
POm        49     53      55       76       47        4         4    37   325
S1        135    186     134      201      100        2         9   151   918
All       226    284     218      317      185        6        13   253  1502

Paper's typed totals (Fig. 4, 5 and 6 legends), for comparison:
                S1 (RSU+FSU)  POm (RSU+FSU)
30 Hz                    209            232
[... 4 more lines not kept]
```

**Agent**

Unit-count text needs a correction (sham S1 units outnumber the paper's). Fixing, then writing entry files.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''S1 units at 30 and
3,000 Hz outnumber the paper's when every voltage is counted, as the 64-channel probes of BH594
give many units at 5, 10 and 15 V. At 5 V the S1 counts fall below the paper's in every condition
but 30 Hz.'''
new='''S1 units at 30 and
3,000 Hz outnumber the paper's when every voltage is counted (344 and 465 against 209 and 366), as
the 64-channel probes of BH594 give many units at 5, 10 and 15 V. With the 2024 files limited to
5 V they are fewer (186 and 201), and over the five PRFs fewer under both (1,243 and 756 against
1,297). Sham S1 units outnumber the paper's under both (151 against 84).'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py
```

```
written 23
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001199-gao-2025 && cat > entry.yaml <<'EOF'
schema_version: 1
name: 001199-gao-2025
type: reproduction
title: Focused ultrasound and the cortico-thalamo-cortical pathway (Gao et al. 2025)
description: Tests the findings of Gao, Ramachandran, Yu and He (2025) on dandiset 001199, which
  holds sorted units (spike times only) and trial tables from 13 rats recorded in S1, POm and
  auditory cortex during transcranial focused ultrasound at five PRFs with 200 us pulses. It counts
  the rats with each pair of recorded areas and tests the auditory cortex responses across PRFs.
  The RSU and FSU findings cannot be tested, as the files hold no waveforms or type labels, and
  the duty-cycle series is not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_gao_2025.ipynb
  title: Reproducing Gao et al. (2025) from dandiset 001199
  runtime_minutes: 4
helpers:
- tfus.py
related:
- id: dandi:001199/0.250829.1250
  relation: uses_data
- id: doi:10.1523/jneurosci.2218-24.2025
  relation: reproduces
EOF
printf "dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\n" > requirements.in
cat > README.md <<'EOF'
# Gao, Ramachandran, Yu & He (2025) from dandiset 001199

Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) that can be
tested on [DANDI:001199](https://dandiarchive.org/dandiset/001199/0.250829.1250). The dandiset holds
sorted units (spike times only) and trial tables from 13 rats, recorded in S1, POm and auditory
cortex (AC) during transcranial focused ultrasound at 30 to 4,500 Hz PRF with 200 us pulses.

| Claim | Outcome |
|---|---|
| Rats with S1 and POm (16) and S1 and AC (12) recordings | Partially reproduced |
| AC neurons respond to 1,500 and 3,000 Hz during sonication, and to four PRFs after it | Not reproduced |
| Target determination artefact (Fig. 2) | Blocked: data missing |
| 20 claims on RSUs and FSUs (Fig. 4 to 6, 10A to 10C, 11C, 11D) | Blocked: data missing |
| 12 claims on the duty-cycle series (Fig. 7 to 9, 10D to 10F) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold no spike waveforms and no RSU or FSU labels (a `celltype_label` column described as
RSU and FSU codes holds 0 or the area), so the paper's typing cannot be repeated. Only the 200 us
pulse-duration series is here. The 13 rats were recorded from August 2024 to July 2025, and only
one of them has a file in dandiset 000946, which the paper names as the repository of its data, so
this dandiset may not hold the paper's recordings. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001199-gao-2025-01.yaml`](../../attempts/001199-gao-2025-01.yaml).

- `reproduce_gao_2025.ipynb`: the analysis. It takes about four minutes, most of it streaming the
  files.
- `tfus.py`: listing and reading the files, the condition of each file from its identifier and
  notes, window spike counts, the normalized rates and tests of the paper. Other notebooks on this
  dandiset can import it.
EOF
cd  && python tools/entry.py lock entries/001199-gao-2025 2>&1 | tail -3 && python tools/entry.py check entries/001199-gao-2025 2>&1 | tail -15
```

```
wrote entries/001199-gao-2025/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
date -u && time python tools/entry.py all entries/001199-gao-2025 2>&1 | tail -15; ls executed/001199-gao-2025/
```

```
Sun Nov  1 09:34:31 UTC 2026
Installed kernelspec registry-001199-gao-2025 in executed/001199-gao-2025/.venv/share/jupyter/kernels/registry-001199-gao-2025
0 error(s)
pass  reproduce_gao_2025.ipynb  (207 s)

real	3m34.209s
user	0m40.537s
sys	0m5.828s
reproduce_gao_2025.ipynb
result.json
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/001199-gao-2025/reproduce_gao_2025.ipynb',4)
for c in nb.cells:
  if c.cell_type!='code': continue
  for o in c.outputs:
    if o.get('output_type')=='error': print('ERR',o['evalue'])
    if 'text' in o and ('KW_p' in o['text'] or 'simultaneous' in o['text'] or 'Fraction' in o['text'] or 'AC units with more' in o['text']): print(o['text'][:2500])
"
```

```
Fraction of modulated units, mean over files:
                       files  units   true  shifted
cohort kind       rec                              
2024   sham       S1       4     91  0.000    0.025
       stimulated S1      92   1926  0.391    0.132
2025   sham       AC       7     65  0.000    0.007
                  POm      8     33  0.077    0.000
                  S1       6     64  0.000    0.069
       stimulated AC      35    194  0.020    0.013
                  POm     40    287  0.019    0.006
                  S1      33    434  0.035    0.039
2024 stimulated: true above shifted in 50 of 92 files; paired Wilcoxon p = 6.9e-10
2025 sham: true above shifted in 3 of 21 files; paired Wilcoxon p = 0.75
2025 stimulated: true above shifted in 7 of 108 files; paired Wilcoxon p = 0.81

(a) S1, S1-6, sham, CG1: simultaneous S1 and POm in 6 rats ['BH596', 'BH608', 'BH615', 'BH648', 'BH654', 'BH658']; S1 and AC in 6 rats ['BH646', 'BH648', 'BH650', 'BH655', 'BH657', 'BH658']; in both groups: ['BH648', 'BH658']
(b) S1, sham, CG1: simultaneous S1 and POm in 6 rats ['BH596', 'BH608', 'BH615', 'BH648', 'BH654', 'BH658']; S1 and AC in 6 rats ['BH646', 'BH648', 'BH650', 'BH655', 'BH657', 'BH658']; in both groups: ['BH648', 'BH658']
Variant, any files of both areas: S1 and POm ['BH596', 'BH608', 'BH615', 'BH646', 'BH648', 'BH650', 'BH654', 'BH655', 'BH657', 'BH658'] ; S1 and AC ['BH646', 'BH648', 'BH650', 'BH654', 'BH655', 'BH657', 'BH658'] (units with more than 2,000 spikes, any target)
Rats with any AC file: ['BH646', 'BH648', 'BH650', 'BH654', 'BH655', 'BH657', 'BH658']
2024 rats with an S1-targeted 5 V session: ['BH590', 'BH594', 'BH596', 'BH615']
[... 88 more lines not kept]
```

**Agent**

Executed copy matches the conclusions. Writing the attempt record.

**Agent calls Bash**

```bash
cat > attempts/001199-gao-2025-01.yaml <<'EOF'
schema_version: 2
id: 001199-gao-2025-01
dataset:
  archive: dandi
  id: "001199"
  version: 0.250829.1250
  doi: 10.48324/dandi.001199/0.250829.1250
paper: doi:10.1523/jneurosci.2218-24.2025
date: 2026-11-01
entry: 001199-gao-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/41291066974
inputs:
- what: The asset list (paths only) of dandiset 000946, the repository the paper's Methods name for
    all its data, read to compare its rats and session dates with those of 001199. Used for the
    notes of the subjects claim and a finding; no measurement is taken from it.
  source: DANDI:000946 version 0.250829.1249 (doi:10.48324/dandi.000946/0.250829.1249)
outcomes:
- claim: subjects
  outcome: partially_reproduced
  notebook: reproduce_gao_2025.ipynb
  output: claim:subjects
  measured:
  - 6
  - 6
  notes: Simultaneous S1 and POm recordings in 6 rats (BH596, BH608, BH615, BH648, BH654, BH658),
    paper 16; simultaneous S1 and AC recordings in 6 rats (BH646, BH648, BH650, BH655, BH657,
    BH658), paper 12. Both readings of the targets (with and without the unexplained "S1-6") give
    the same counts. Both counts are below the paper's and none above, the claims file's rule for a
    partial result. Two rats (BH648, BH658) are in both groups, where the paper's AC rats are
    another group. With files of both areas in a rat, simultaneous or not, the counts are 10 and 7.
    The 13 rats were recorded from August 2024 to July 2025, after the paper's preprint (June
    2024), and only BH594 (S1 only here) is among the 20 rats of dandiset 000946, the repository the
    paper names, whose sessions run from August 2023 to April 2024. So the dandiset may not hold the
    paper's rats at all.
  deviations:
  - A session is a file in the 2024 cohort and a group of files sharing an identical trial table in
    the 2025 cohort, where each probe has its own file; the dandiset does not say this, the shared
    trial tables show it.
  - Units of BH590 and BH594 files are taken as S1, as their notes say recording at S1 and their
    celltype_label holds 0; BH596 and BH615 units are given the area their celltype_label holds.
- claim: fig2-target-artifact
  outcome: blocked
  blocked_by: data_missing
  notes: The claim needs the raw voltage of the target-determination trials (about 170 kPa) and
    spike waveforms; the files hold sorted spike times only, and no target-determination trials.
    Two BH615 sessions at 10 and 15 V show a burst of detected spikes confined to 0 to 75 ms after
    the trial start (population rate 4 to 20 times its mean), which looks like an ultrasound-locked
    artefact, but neither the voltage nor the waveform tail can be examined.
- claim: fig4-unit-counts
  outcome: blocked
  blocked_by: data_missing
  notes: RSU and FSU types come from the waveforms (IP and AHP, Methods, Neuronal type
    classification), which the files do not hold; the celltype_label column is described as 1 = RSU,
    2 = FSU but holds 0 or the area in every file that has it. Untyped, with more than 2,000 spikes,
    the dandiset holds 465 S1 and 110 POm units at 3,000 Hz and 344 S1 and 93 POm at 30 Hz over all
    voltages (201 and 76, 186 and 53 with the 2024 files limited to 5 V), against the paper's typed
    sums of 366 and 250, 209 and 232.
- claim: fig4-timelocked-rsu-3000
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU types (see fig4-unit-counts), and depends on fig4-unit-counts, which is blocked.
- claim: fig4-postsonication-3000
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU and FSU types (see fig4-unit-counts), and depends on it.
- claim: fig4-30hz-responses
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU types (see fig4-unit-counts), and depends on it.
- claim: fig4-no-fsu-change
  outcome: blocked
  blocked_by: data_missing
  notes: Needs FSU types (see fig4-unit-counts), and depends on it.
- claim: fig5-unit-counts
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU and FSU types (see fig4-unit-counts). There is also no CG1 session at 3,000 Hz,
    the paper's control; CG1 sessions here are at 300 Hz (BH658) and 4,500 Hz (BH655, BH657,
    BH658). Untyped, sham sessions hold 151 S1 and 37 POm units with more than 2,000 spikes (paper
    84 and 134 typed).
- claim: fig5a-sham-no-response
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU and FSU types (see fig4-unit-counts); depends on fig5-unit-counts.
- claim: fig5b-cg1-control-no-response
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU and FSU types, and the dandiset holds no CG1 session at 3,000 Hz PRF (see
    fig5-unit-counts).
- claim: fig6-unit-counts
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU and FSU types (see fig4-unit-counts). Untyped, the five 200 us PD conditions
    hold 1,243 S1 and 396 POm units with more than 2,000 spikes over all voltages (756 and 280 with
    the 2024 files limited to 5 V), against the paper's typed sums of 1,297 and 1,019.
- claim: fig6a-s1-rsu-timelocked-high-prf
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU types (see fig4-unit-counts); depends on fig6-unit-counts.
- claim: fig6a-s1-rsu-delayed
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU types (see fig4-unit-counts); depends on fig6-unit-counts.
- claim: fig6b-s1-fsu-prf
  outcome: blocked
  blocked_by: data_missing
  notes: Needs FSU types (see fig4-unit-counts); depends on fig6-unit-counts.
- claim: fig6c-pom-rsu-prf
  outcome: blocked
  blocked_by: data_missing
  notes: Needs RSU types (see fig4-unit-counts); depends on fig6-unit-counts.
- claim: fig6d-pom-fsu-prf
  outcome: blocked
  blocked_by: data_missing
  notes: Needs FSU types (see fig4-unit-counts); depends on fig6-unit-counts.
- claim: fig7-9-unit-counts
  outcome: blocked
  blocked_by: data_missing
  notes: Every stimulated file of the dandiset has PD 200 us, so the duty-cycle series at 3,000 Hz
    (PD 2 to 300 us), at 30 Hz (PD 200 to 30,000 us) and at 60% DC (PD 133 to 20,000 us) are present
    only at their 200 us point. RSU and FSU types are missing as well (see fig4-unit-counts).
- claim: fig7a-s1-rsu-dc-3000
  outcome: blocked
  blocked_by: data_missing
  notes: The duty-cycle series is not in the dandiset, and RSU types are missing (see
    fig7-9-unit-counts).
- claim: fig7b-s1-fsu-dc-3000
  outcome: blocked
  blocked_by: data_missing
  notes: As fig7a-s1-rsu-dc-3000.
- claim: fig7c-pom-rsu-dc-3000
  outcome: blocked
  blocked_by: data_missing
  notes: As fig7a-s1-rsu-dc-3000.
- claim: fig7d-pom-fsu-dc-3000
  outcome: blocked
  blocked_by: data_missing
  notes: As fig7a-s1-rsu-dc-3000.
- claim: fig8a-s1-rsu-dc-30
  outcome: blocked
  blocked_by: data_missing
  notes: As fig7a-s1-rsu-dc-3000, for the 30 Hz series.
- claim: fig8b-s1-fsu-dc-30
  outcome: blocked
  blocked_by: data_missing
  notes: As fig7a-s1-rsu-dc-3000, for the 30 Hz series.
- claim: fig9a-s1-rsu-60dc
  outcome: blocked
  blocked_by: data_missing
  notes: As fig7a-s1-rsu-dc-3000, for the 60% DC series.
- claim: fig9b-s1-fsu-60dc
  outcome: blocked
  blocked_by: data_missing
  notes: As fig7a-s1-rsu-dc-3000, for the 60% DC series.
- claim: fig10a-dsttc-3000-during
  outcome: blocked
  blocked_by: data_missing
  notes: The directional correlations are between S1 and POm RSUs and FSUs, which cannot be typed
    (see fig4-unit-counts); depends on fig4-unit-counts.
- claim: fig10a-dsttc-3000-post
  outcome: blocked
  blocked_by: data_missing
  notes: As fig10a-dsttc-3000-during.
- claim: fig10b-dsttc-30
  outcome: blocked
  blocked_by: data_missing
  notes: As fig10a-dsttc-3000-during.
- claim: fig10c-sttc-constant-pd
  outcome: blocked
  blocked_by: data_missing
  notes: Needs S1 RSU and POm RSU pairs, which cannot be typed (see fig4-unit-counts); depends on
    fig6-unit-counts.
- claim: fig10d-sttc-60dc
  outcome: blocked
  blocked_by: data_missing
  notes: The 60% DC series is not in the dandiset and RSUs cannot be typed (see fig7-9-unit-counts).
- claim: fig10e-sttc-30hz-dc
  outcome: blocked
  blocked_by: data_missing
  notes: The 30 Hz DC series is not in the dandiset and RSUs cannot be typed (see
    fig7-9-unit-counts).
- claim: fig10f-sttc-3000-dc
  outcome: blocked
  blocked_by: data_missing
  notes: The 3,000 Hz DC series is not in the dandiset and RSUs cannot be typed (see
    fig7-9-unit-counts).
- claim: fig11b-ac-responses
  outcome: not_reproduced
  notebook: reproduce_gao_2025.ipynb
  output: claim:fig11b-ac-responses
  measured: 194
  notes: 194 AC units with more than 2,000 spikes in 7 rats (paper 453; per PRF 45, 29, 42, 40 and
    38 against 83, 59, 107, 104 and 100). No Kruskal-Wallis test across the five PRFs is
    significant at 0.01 under any reading of R (p 0.013 to 0.74); with BH654 left out the R2 tests
    give 0.0095 and 0.006, with every R2 mean below 100%. Against baseline only 1,500 Hz during
    sonication is significant, under R1 and T2 alone (mean 105.1%, uncorrected p = 6.4e-05, below
    0.01 after factors 5, 10 and 15); 3,000 Hz is not (102.4%, p = 0.02 uncorrected), and no PRF is
    above baseline after sonication under any reading. 300 Hz has the lowest mean only under R1
    during sonication with BH654 left out. Per-rat R1 means are 88 to 127%. Sham AC units give R1
    means of 99.6 and 99.9% and no significant increase. Leaving out the S1-6 sessions gives the
    same result. Under R2 every mean is below 100%, sham included (69.8%), as R2 keeps only trials
    with a prestimulus spike. In the 2025 cohort, which holds every AC file, the trial starts could
    be shown to be sonication onsets only for the BH648 4,500 Hz session, whose S1 units rise from
    about 200 ms; in the other sessions the spikes show no more locking to the true trial starts
    than to shifted ones, so the absence of AC responses may come from the trial tables and not
    from the neurons.
  deviations:
  - The paper's AC group is 12 rats with S1 and AC probes; the dandiset holds AC files from 7 rats,
    and all 7 are used. A variant leaves out BH654, whose AC files share no session with an S1 file.
  - Sessions with stimulation labelled "S1-6", which nothing in the dandiset explains, are taken as
    S1-targeted; a variant leaves them out, with the same outcome.
  - The pressure of the 2025 sessions is not stated in the files; the paper used 5 V (88 kPa).
  - The Bonferroni factor B1 is taken as 5 (the PRFs compared with baseline in a window), with 10
    (both windows) shown too; B2 is 15 (all pairs among the five PRFs and the baseline).
- claim: fig11c-ac-to-s1-30hz
  outcome: blocked
  blocked_by: data_missing
  notes: Needs S1 RSU and FSU types (see fig4-unit-counts). Simultaneous AC and S1 files at 30 Hz
    exist for 5 rats (BH646, BH648, BH650, BH655, BH657).
- claim: fig11d-ac-to-s1-3000
  outcome: blocked
  blocked_by: data_missing
  notes: Needs S1 RSU and FSU types (see fig4-unit-counts). Simultaneous AC and S1 files at 3,000
    Hz exist for 5 rats (BH646, BH648, BH650, BH655, BH657).
findings:
- kind: data_missing
  statement: The files hold spike times only, with no spike waveforms and no RSU or FSU labels, so
    the paper's typing of units (IP and AHP of the waveform, k-means) cannot be repeated and the 20
    claims on RSUs and FSUs cannot be tested.
- kind: metadata_error
  statement: The units column celltype_label is described as "label 1 = RSU, label 2 = FSU", but no
    file holds a 1 or a 2. It holds 0 in the 49 files of BH590 and BH594 and the area of the unit
    (S1 or POm) in the 47 files of BH596 and BH615; the 133 files of the 2025 cohort have no such
    column.
- kind: data_missing
  statement: Every stimulated file has a pulse duration of 200 us. The duty-cycle series of the
    paper (Fig. 7 to 9 and 10D to 10F) are not in the dandiset, nor the target-determination trials
    and raw voltage of Fig. 2, nor a CG1 control session at 3,000 Hz (CG1 sessions are at 300 and
    4,500 Hz).
- kind: other
  statement: The dandiset names the paper as the description of its data, but its 13 rats were
    recorded from August 2024 to July 2025, after the paper's preprint of June 2024, and it holds
    conditions the paper does not describe (10 and 15 V, stimulation at POm, 64-channel probes with
    and without z-coating, 2 mm offsets). Of its rats only BH594 has a file in dandiset 000946, which
    the paper's Methods name as the repository of all its data and which lists 20 rats recorded from
    August 2023 to April 2024. Simultaneous S1 and POm recordings exist for 6 rats and S1 and AC
    recordings for 6, against the paper's 16 and 12.
- kind: metadata_error
  statement: The data_collection field gives "PRESSURE:67V" in most 2024 files whatever voltage the
    identifier gives (the 67 is the ultrasound duration), and the 2025 files state no pressure or
    voltage anywhere. The description says pressure is in the identifier, which holds for the 2024
    files only.
- kind: metadata_insufficient
  statement: Stimulation targets "S1-6", "NEW", "y-1" and "SEP" in the notes of 2025 files, and the
    identifier tags of 2024 files (coating, nocoating, NZ, C, P, 2mm, bad, break, x0y35z165), are not
    explained anywhere in the dandiset. Electrode locations are "unknown" in every file.
- kind: metadata_error
  statement: In the 2025 cohort session_start_time does not date the session. Files of two probes
    that share a trial table, and so are one session, have start times minutes apart, and the BH608
    sham pair has start times five months apart (2025-02-06 and 2025-07-11). One file is named
    ses-None.
- kind: metadata_error
  statement: In the BH608 30 Hz session the S1 file gives stimulation at S1 and the POm file, which
    shares its trial table, stimulation at "SEP".
- kind: format_error
  statement: In 64 units of 16 files of the 2025 cohort the spike times are not in increasing order
    (one to seven places per unit). Left unsorted they gave one AC unit a normalized rate of 4,224%
    in this analysis.
- kind: other
  statement: The files sub-BH646_ses-None and sub-BH646_ses-20250308T003900 hold the same spike
    trains and trial table (AC at 30 Hz); the recording is deposited twice.
- kind: metadata_error
  statement: The description says S1 is recorded with 64-channel Cambridge or NeuroNexus probes and
    POm with 32-channel probes, and that each recording has 500 trials. The 2025 files record S1,
    POm and AC with 32-channel A1x32-Poly3 probes, four files name a device "H9", and most files hold
    499 trials, some 113 to 480.
- kind: other
  statement: In the 2025 cohort, which holds every AC recording, the spikes show no more locking to
    the trial starts than to starts shifted by 1.25 s (true above shifted in 7 of 108 stimulated
    files), except in the BH648 4,500 Hz session. In the 2024 cohort the locking is clear (0.39
    against 0.13 of units modulated, 50 of 92 files). Either the 2025 sessions evoked no response
    or their trial times are not the sonication onsets; the files cannot tell which.
EOF
cd  && python tools/entry.py check entries/001199-gao-2025 2>&1 | tail -5
```

```
0 error(s)
```

**Agent**

Verifying a few record statements against outputs (devices by cohort, the five-PRF sums).

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd
s=pd.read_csv('survey.csv'); s['dev']=s.dev.str.extract(r\"'description': '([^']*)'\")
s['cohort']=s.subj.isin(['BH590','BH594','BH596','BH615']).map({True:'2024',False:'2025'})
print(pd.crosstab(s.dev.fillna('none'), [s.cohort, s.nelec]))
print(s[s.dev=='H9'][['path','notes']])
"
```

```
cohort                                             2024 2025    
nelec                                                64   32  64
dev                                                             
A1x32-Poly3-10mm-50-177-A32                           0   91   0
A1x64-Edge-6mm-22.5-177 & A1x32-Poly3-10mm-50-1...   47    0   0
A1x64-Edge-6mm-22.5-177 with z-coating               17    0  42
A1x64-Edge-6mm-22.5-177 without z-coating            28    0   0
H9                                                    4    0   0
                                                 path                      notes
45  sub-BH590/sub-BH590_ses-20240817T000400_ecephy...   Recording:S1; stim at:S1
46  sub-BH590/sub-BH590_ses-20240816T234200_ecephy...   Recording:S1; stim at:S1
47  sub-BH590/sub-BH590_ses-20240817T002600_ecephy...  Recording:S1; stim at:POM
48  sub-BH590/sub-BH590_ses-20240817T004800_ecephy...  Recording:S1; stim at:POM
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && PYTHONPATH=entries/001199-gao-2025 python -c "
import pandas as pd, tfus
s=pd.read_csv('survey.csv'); s['dev']=s.dev.str.extract(r\"'description': '([^']*)'\").str[:30]
c=pd.DataFrame([tfus.parse_condition(i,n) for i,n in zip(s.identifier,s.notes)]); s=pd.concat([s,c],axis=1)
s['cohort']=s.subj.isin(['BH590','BH594','BH596','BH615']).map({True:'2024',False:'2025'})
print(pd.crosstab([s.cohort,s.rec], s.dev))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    s=pd.read_csv('survey.csv'); s['dev']=s.dev.str.extract(r"'description': '([^']*)'").str[:30]
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/generic.py", line 6434, in __getattr__
    return object.__getattribute__(self, name)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AttributeError: 'DataFrame' object has no attribute 'str'. Did you mean: 'std'?
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && PYTHONPATH=entries/001199-gao-2025 python -c "
import pandas as pd, tfus
s=pd.read_csv('survey.csv'); s['dev']=s.dev.str.extract(r\"'description': '([^']*)'\", expand=False).str[:30]
c=pd.DataFrame([tfus.parse_condition(i,n) for i,n in zip(s.identifier,s.notes)]); s=pd.concat([s,c],axis=1)
s['cohort']=s.subj.isin(['BH590','BH594','BH596','BH615']).map({True:'2024',False:'2025'})
print(pd.crosstab([s.cohort,s.rec], s.dev))
"
```

```
dev         A1x32-Poly3-10mm-50-177-A32  ...  H9
cohort rec                               ...    
2024   S1                             0  ...   4
2025   AC                            43  ...   0
       POm                           48  ...   0
       S1                             0  ...   0

[4 rows x 5 columns]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
old='''print("\\nDevices:", info.device.value_counts().to_dict())'''
new='''print("\\nDevices by cohort and recorded area (files):")
print(pd.crosstab([info.cohort, info.rec], info.device).T.to_string())'''
assert old in s; s=s.replace(old,new)
old='''The
description says S1 is recorded with 64-channel probes and POm with 32-channel probes; the files
list A1x64 probes (with and without z-coating) in the 2024 cohort and the A1x32-Poly3 probe of the
paper in the 2025 cohort. Electrode locations are all "unknown".'''
new='''The
description says S1 is recorded with 64-channel probes and POm with 32-channel probes, and the
files agree: S1 files list A1x64-Edge probes (four BH590 files a device "H9"), the POm and AC files
of the 2025 cohort the A1x32-Poly3, and the 2024 files of BH596 and BH615 both. The paper used
two 32-channel A1x32-Poly3 probes. Electrode locations are all "unknown".'''
assert old in s; s=s.replace(old,new)
old='''paper = pd.DataFrame({"S1 (RSU+FSU)"'''
new='''five = [f"{p} Hz" for p in tfus.PRFS]
print("\\nSums over the five PRFs, all voltages:", pd.crosstab(t.area, t.cond)[five].sum(1).to_dict(),
      "; 2024 files at 5 V:", pd.crosstab(t5.area, t5.cond)[five].sum(1).to_dict())
paper = pd.DataFrame({"S1 (RSU+FSU)"'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py
cd  && python - <<'EOF'
p='attempts/001199-gao-2025-01.yaml'; s=open(p).read()
old=s[s.index("- kind: metadata_error\n  statement: The description says S1 is recorded"):s.index("- kind: other\n  statement: In the 2025 cohort, which holds")]
new='''- kind: other
  statement: The paper used two 32-channel A1x32-Poly3 probes; the S1 files here list 64-channel
    A1x64-Edge probes with or without z-coating, as the dandiset's description says, and four BH590
    files name a device "H9". The description gives 500 trials per recording; most files hold 499
    and some 113 to 480.
'''
s=s.replace(old,new)
s=s.replace("the trial start (population rate 4 to 20 times its mean)","the trial start (population rate 2.9 to 7.2 times its mean)")
open(p,'w').write(s)
EOF
grep -n "H9\|2.9 to 7.2" attempts/001199-gao-2025-01.yaml
```

```
written 23
57:    the trial start (population rate 2.9 to 7.2 times its mean), which looks like an ultrasound-locked
285:    files name a device "H9". The description gives 500 trials per recording; most files hold 499
```

**Agent calls Bash**

```bash
grep -n "—\|rather\|\*\*" entries/001199-gao-2025/README.md entries/001199-gao-2025/tfus.py attempts/001199-gao-2025-01.yaml $TMPDIR/build_nb.py | grep -v "\*\*Result" ; python -c "
import yaml; d=yaml.safe_load(open('attempts/001199-gao-2025-01.yaml')); print(len(d['outcomes']))
import collections; print(collections.Counter(o['outcome'] for o in d['outcomes']))"; grep -nE "^[^#]*[^ ]: [^ ].*: " attempts/001199-gao-2025-01.yaml | grep -v "^\s*-" | head
```

```
entries/001199-gao-2025/tfus.py:162:    allw = {"pre": prestim, **windows}
/tmp/claude-1001/build_nb.py:20:**Paper.** Gao H, Ramachandran S, Yu K, He B (2025). Transcranial Focused Ultrasound Modulates
/tmp/claude-1001/build_nb.py:27:**Dandiset.** [DANDI:001199](https://dandiarchive.org/dandiset/001199/0.250829.1250), version
/tmp/claude-1001/build_nb.py:35:**What the dandiset holds.** Sorted units (spike times only) and trial tables for 13 rats, recorded
/tmp/claude-1001/build_nb.py:39:**Claims.** The claims file (`claims/001199/10.1523-jneurosci.2218-24.2025.yaml`) has 35 claims.
/tmp/claude-1001/build_nb.py:106:        "n_pass": sum(len(s) > tfus.MIN_SPIKES for s in f["spikes"]), **c})
/tmp/claude-1001/build_nb.py:543:**How the analysis differs from the paper's.** Sessions are taken as the dandiset gives them, with
/tmp/claude-1001/build_nb.py:548:**What was found about the dataset.** The dandiset holds spike times and trial tables only: no
35
Counter({'blocked': 33, 'partially_reproduced': 1, 'not_reproduced': 1})
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i -E 's/^\*\*(Paper|Dandiset|What the dandiset holds|Claims|How the analysis differs from the paper.s|What was found about the dataset)\.\*\*/\1./' build_nb.py && grep -n "^\*\*" build_nb.py; . dev/bin/activate && python build_nb.py && cd  && date -u && python tools/entry.py all entries/001199-gao-2025 2>&1 | tail -3
```

```
395:**Result: partially reproduced.** Under both readings the dandiset holds simultaneous S1 and POm
516:**Result: not reproduced.** There are 194 AC units with more than 2,000 spikes in 7 rats, against
written 23
Sun Nov  1 09:40:00 UTC 2026
Installed kernelspec registry-001199-gao-2025 in executed/001199-gao-2025/.venv/share/jupyter/kernels/registry-001199-gao-2025
0 error(s)
pass  reproduce_gao_2025.ipynb  (205 s)
```

**Agent**

Entry passes (205 s). Checking the new outputs in the executed copy, then handover.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/001199-gao-2025/reproduce_gao_2025.ipynb',4)
for c in nb.cells:
  if c.cell_type!='code': continue
  for o in c.outputs:
    if o.get('output_type')=='error': print('ERR',o['evalue'])
    if 'text' in o and ('Devices by' in o['text'] or 'Sums over' in o['text']): 
        t=o['text']; i=t.find('Devices by'); j=t.find('Sums over'); print(t[i:i+900] if i>=0 else '', t[j:j+300] if j>=0 else '')
"; python tools/entry.py handover entries/001199-gao-2025 2>&1 | tail -3; ls executed/001199-gao-2025/handover; git status --short
```

```
Devices by cohort and recorded area (files):
cohort                                                2024 2025        
rec                                                     S1   AC POm  S1
device                                                                 
A1x32-Poly3-10mm-50-177-A32                              0   43  48   0
A1x64-Edge-6mm-22.5-177 & A1x32-Poly3-10mm-50-177-A32   47    0   0   0
A1x64-Edge-6mm-22.5-177 with z-coating                  17    0   0  42
A1x64-Edge-6mm-22.5-177 without z-coating               28    0   0   0
H9                                                       4    0   0   0
Electrodes per file: {64: 138, 32: 91} ; electrode locations: [('unknown',)]

Units table columns: {'id,spike_times,spike_times_index': 133, 'celltype_label,id,spike_times,spike_times_index': 96}
celltype_label description: ['label 1 = RSU, label 2 = FSU']
celltype_label values  
 Sums over the five PRFs, all voltages: {'AC': 194, 'POm': 396, 'S1': 1243} ; 2024 files at 5 V: {'AC': 194, 'POm': 280, 'S1': 756}

Paper's typed totals (Fig. 4, 5 and 6 legends), for comparison:
                S1 (RSU+FSU)  POm (RSU+FSU)
30 Hz                    209            232
3000 Hz         
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/\[five\].sum(1)/[five].sum(axis=1)/g' $TMPDIR/build_nb.py && . $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && python tools/entry.py all entries/001199-gao-2025 2>&1 | tail -2 && python tools/entry.py handover entries/001199-gao-2025 2>&1 | tail -1 && python -c "
import nbformat
nb=nbformat.read('executed/001199-gao-2025/reproduce_gao_2025.ipynb',4)
for c in nb.cells:
  for o in c.get('outputs',[]):
    if o.get('output_type')=='error' or o.get('name')=='stderr': print(o.get('evalue', o.get('text'))[:300])
"; date -u
```

```
written 23
0 error(s)
pass  reproduce_gao_2025.ipynb  (205 s)
wrote executed/001199-gao-2025/handover
Sun Nov  1 09:47:46 UTC 2026
```

**Agent**

I've completed steps 1 to 5 and the handover (step 6). The entry passes `python tools/entry.py all` (the notebook runs in 205 s), and the handover package is in `executed/001199-gao-2025/handover/`. Nothing is committed.

The main result: this dandiset probably does not hold the paper's recordings. Its 13 rats were recorded from August 2024 to July 2025, after the paper's preprint of June 2024. The paper's Methods name dandiset 000946 for its data, and that dandiset lists 20 other rats recorded in 2023 and 2024; only BH594 is in both. On top of that, the files hold spike times only, with no waveforms, so the paper's RSU/FSU typing cannot be repeated, and every session uses 200 µs pulses, so the duty-cycle series is absent.

**1. Outcomes (35 claims)**

| Claim | Outcome |
|---|---|
| subjects | partially reproduced: 6 rats with S1+POm (paper 16) and 6 with S1+AC (paper 12); two rats are in both groups |
| fig11b-ac-responses | not reproduced: 194 AC units (paper 453); no Kruskal–Wallis test significant at 0.01; only 1,500 Hz during sonication is significant, and only under one reading (R1/T2); nothing is significant after sonication |
| fig2-target-artifact | blocked, `data_missing`: no raw voltage or target-determination trials |
| 20 claims on RSUs/FSUs (Fig. 4–6, 10A–C, 11C–D) | blocked, `data_missing`: no waveforms or type labels |
| 12 duty-cycle claims (fig7-9-unit-counts, Fig. 7–9, 10D–F) | blocked, `data_missing`: only PD 200 µs; types also missing |

**2. Findings, assumptions, questions**
- **Type labels:** a `celltype_label` column is described as "1 = RSU, 2 = FSU" but holds 0 or the area name (S1/POm); 133 files have no such column.
- **Missing conditions:** there is no CG1 control at 3,000 Hz.
- **Undescribed conditions:** sessions at 10 and 15 V, stimulation at POm, and 64-channel probes; the paper used two 32-channel probes at 5 V.
- **Pressure metadata:** the pressure field reads "67V" (that is the ultrasound duration), and 2025 files state no pressure at all.
- **Unexplained labels:** stimulation targets "S1-6", "NEW", "y-1" and "SEP".
- **Session dating:** in the 2025 cohort, each probe has its own file, and files that share a trial table are one session. Their `session_start_time` values do not date the session (the BH608 sham pair is five months apart).
- **Format error:** 64 units have spike times out of order. Left unsorted, one AC unit read 4,224%; I sort on reading.
- **Duplicate:** one recording is deposited twice (BH646 `ses-None` and `ses-20250308T003900`).
- **Clock:** the 2024 sessions lock clearly to trial starts. Most 2025 sessions, which hold every AC file, do not (only BH648 at 4,500 Hz does). So the AC null result may come from the trial tables, not the neurons; this caveat is in the fig11b notes.
- **Assumption:** I counted "S1-6" as S1-targeted. A variant without it gives the same outcomes, so no outcome rests on it.
- **Questions:** none for the paper's authors, since every reading gave the same outcome. I asked a reader nothing.
- **Version:** pinned 0.250829.1250. All four published versions and the draft hold the same 229 files and differ only in contributor order.

**3. Where the protocol was unclear or missing something**
1. **Dataset that may not hold the paper's data.** The protocol has no rule for this case, where the paper names another dandiset (000946) as its repository. I tested 001199 as the claims file says and recorded the mismatch as a finding.
2. **Reading another dandiset's metadata.** Step 1.4 limits outside data to what the claims file says the paper relies on, but says nothing about reading another dandiset's file list just to identify rats. I listed 000946's asset paths under `inputs` and used them only in the subjects notes and a finding.
3. **Which block reason.** With waveforms absent and the label column mislabelled, the claims could be `data_missing` or `metadata_insufficient`. I chose `data_missing`.
4. **Failed clock check.** The protocol asks only to name sessions where the clock could not be established. It does not say how that bears on a claim whose result is an absence of response. I kept `not_reproduced` and stated the caveat.
5. **"Subset" in the subjects criterion.** "None extra" cannot be checked without the paper's list of rats. I applied it to the counts (both lower, neither higher).
6. **Bonferroni factor B1.** The claims file's "windows or conditions" is ambiguous. I ran factors of 5, 10 and 15; all give the same result.
7. **Format errors.** The protocol records them but does not say whether to repair them. I sorted the spike times and reported it.

**4. Runtime and failures**
- The run took about 50 minutes (08:59 to 09:48 UTC); the notebook takes about 3.5 minutes, most of it streaming.
- Nothing failed.
- One early bug was mine: window counts on the unsorted spike times produced the 4,224% outlier. It is fixed, and the final run uses sorted times.

Files are in `entries/001199-gao-2025/`:
- reproduce_gao_2025.ipynb
- tfus.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The attempt record is `attempts/001199-gao-2025-01.yaml`.

## End of run

69 turns, 44 minutes, result: success.
