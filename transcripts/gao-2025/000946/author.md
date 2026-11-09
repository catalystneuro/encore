# 000946 · author · run 41249314684

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; wc -l docs/protocol.md README.md docs/design.md docs/archives.md; ls claims/000946 paper entries/001453-fouke-2025 claims/001453
```

```
Sat Oct 31 22:46:08 UTC 2026
  612 docs/protocol.md
  139 README.md
  271 docs/design.md
  287 docs/archives.md
 1309 total
claims/000946:
10.1523-jneurosci.2218-24.2025.yaml

claims/001453:
10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

[... 3 more lines not kept]
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
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
 "file_path": "claims/000946/10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025) on dandiset 000946.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	# Source: the version of record (J Neurosci 45(23) e2218242025, PMC12139594), full text as served
5	# by PMC: Abstract, Introduction, Materials and Methods, Results, figure legends and Discussion.
6	# The paper has no supplement (no Extended Data is cited). No PDF was supplied. The equation that
7	# defines the directional spike time tiling coefficient (dSTTC) is missing from the text read; only
8	# its description in words survives (Methods, Directional spike time tiling coefficient), and the
9	# symbols in that description are stripped. The paper links no analysis code, so no code was read.
10	#
11	# Data the paper used, as it reports them. Male Wistar rats under isoflurane (2%). Group 1 (N = 16):
12	# two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5, 1 to 1.3 mm deep, layers III to V)
13	# and one in POm (AP -4.5, ML 2.6, 5.8 mm). Group 2 (N = 12): S1 and auditory cortex (AC, AP -4.5,
14	# ML 6.5). tFUS from a 128-element array (1.5 MHz) aimed at S1, about 88 kPa in situ. Each session
15	# is one parameter set: 500 trials, ultrasound duration (UD) 67 ms, intersonication interval 2.5 s
16	# with 10% jitter, order of conditions randomized. PRFs 30, 300, 1500, 3000, 4500 Hz; duty cycles
17	# (DC) 0.6, 6, 30, 60, 90%; DC = PRF x pulse duration (PD). The PRF series uses PD 200 us, so 30,
18	# 300, 1500, 3000 and 4500 Hz are 0.6, 6, 30, 60 and 90% DC. DC series at 3000 Hz and at 30 Hz,
19	# and a PRF series at 60% DC. Sham sessions have no tFUS; control sessions aim tFUS at cingulate
20	# cortex (CG1, AP 3, ML 0). The dandiset description says each session's identifier holds the PRF
[... 819 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000946/10.1523-jneurosci.2218-24.2025.yaml",
 "offset": 839
}
```

```
839	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 1; Figure 10B
840	  quote: When delivering 30 Hz ultrasound, S1 RSUs to POm FSUs higher correlated (p = 0.0058), while
841	    POm RSUs showed decreased correlation to S1 FSUs during sonication (p = 0.0058).
842	  statistics:
843	  - about: S1 RSU to POm FSU, increase
844	    test: one-tail two-sample Wilcoxon against prestimulation correlation
845	    p: 0.0058
846	  - about: POm RSU to S1 FSU, decrease
847	    test: one-tail two-sample Wilcoxon against prestimulation correlation
848	    p: 0.0058
849	  criterion: The header's dSTTC method on the 30 Hz, 200 us sessions, the first bin from 0 ms.
850	    Reproduced when, under every dSTTC reading (D1, A1/A2, W1/W2, S1/S2) and every cell-type
851	    reading, S1 RSU to POm FSU is above
852	    prestimulation and POm RSU to S1 FSU below it (one-tailed, p < 0.05); partially reproduced
853	    when one holds.
854	- id: fig10c-sttc-constant-pd
855	  statement: With constant 200 us PD, the S1 RSU to POm RSU correlation change during sonication
856	    shows no PRF dependence overall, though 1500 Hz gives a higher change than 30 Hz.
857	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 2; Figure 10C
858	  quote: When applying tFUS with constant 200 μs PD, varying the DC and PRF, the correlation did not
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md; sed -n 1,140p docs/archives.md
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
[... 259 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/design.md | head -150; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/README.md
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
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,271p docs/design.md; cat attempts/001453-fouke-2025-01.yaml | head -150
```

```
contacts no one.

## Maintenance

Entries are re-run on a schedule. When an agent-deposited entry breaks, the
failure dispatches an agent to repair it, and the repair goes through the same
gates and verification. A person is only pulled in when the repair fails.

## Dashboard

The public site is static and is built from the files above by
`tools/build_site.py`; there is no server.

- **Overview:** headline numbers, outcomes overall and by technique, why claims
  were blocked, findings by kind, and verification. Every number and bar links
  to the matching filtered list.
- **Datasets:** a list of every target, with filters (status, outcomes of
  its claims, why claims were blocked, verification, kinds of finding,
  technique, species), search, sorting and pagination. The view is kept in the
  URL, so any filtered list can be linked. Each attempted dataset links to
[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -n -A30 "^findings" | head -60; ls schemas tools; ls questions | head
```

```
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
112-    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
113-    only Danio rerio; the files hold 37 fish of two species.
[... 55 more lines not kept]
```

**Agent**

Now the dataset. Let me query DANDI.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000946/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000946/versions/" | python -m json.tool | grep -E '"version"|"modified"|"status"|asset_count|size'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/" > meta.json; python -c "
import json;m=json.load(open('meta.json'))
print(m.get('description'));print(m.get('relatedResource'));print(m.get('assetsSummary'))"
python - <<'EOF'
import requests,json
url="https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r['results']; url=r['next']
json.dump(out,open('assets.json','w'))
print(len(out))
for a in out[:15]: print(a['path'],a['size'])
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q requests h5py remfile pynwb numpy scipy pandas scikit-learn matplotlib dandi 2>&1 | tail -2; python -c "import pynwb,remfile;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import requests,json,collections
url="https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r['results']; url=r['next']
json.dump(out,open('assets.json','w'))
print(len(out))
for a in out[:10]: print(a['path'],a['size'])
subs=collections.Counter(a['path'].split('/')[0] for a in out)
print(subs)
import statistics
print(statistics.median(a['size'] for a in out), max(a['size'] for a in out))
EOF
```

```
1920
sub-BH494/sub-BH494_ecephys.nwb 3067424
sub-BH494/sub-BH494_ses-20230817T132836_ecephys.nwb 6291256
sub-BH494/sub-BH494_ses-20230820T123756_ecephys.nwb 1256120
sub-BH494/sub-BH494_ses-20230820T125042_ecephys.nwb 4036944
sub-BH494/sub-BH494_ses-20230820T131032_ecephys.nwb 5108112
sub-BH494/sub-BH494_ses-20230820T144522_ecephys.nwb 3962128
sub-BH494/sub-BH494_ses-20230820T145857_ecephys.nwb 4751856
sub-BH494/sub-BH494_ses-20230820T175254_ecephys.nwb 5040120
sub-BH494/sub-BH494_ses-20230820T181207_ecephys.nwb 1938848
sub-BH494/sub-BH494_ses-20230820T181910_ecephys.nwb 5130904
Counter({'sub-BH528': 117, 'sub-BH511': 115, 'sub-BH513': 109, 'sub-BH538': 94, 'sub-BH535': 92, 'sub-BH539': 92, 'sub-BH553': 92, 'sub-BH547': 88, 'sub-BH551': 88, 'sub-BH532': 85, 'sub-BH501': 78, 'sub-BH558': 78, 'sub-BH499': 77, 'sub-BH495': 75, 'sub-BH537': 73, 'sub-BH530': 64, 'sub-BH494': 53, 'sub-BH510': 48, 'sub-BH500': 31, 'sub-STTC-BH528': 30, 'sub-STTC-BH513': 28, 'sub-STTC-BH510': 25, 'sub-STTC-BH535': 24, 'sub-STTC-BH495': 23, 'sub-STTC-BH511': 23, 'sub-STTC-BH538': 23, 'sub-STTC-BH553': 23, 'sub-STTC-BH499': 22, 'sub-STTC-BH547': 21, 'sub-STTC-BH551': 21, 'sub-STTC-BH501': 20, 'sub-STTC-BH532': 20, 'sub-STTC-BH530': 16, 'sub-STTC-BH537': 13, 'sub-STTC-BH494': 11, 'sub-STTC-BH539': 10, 'sub-STTC-BH558': 10, 'sub-STTC-BH500': 7, 'sub-BH594': 1})
3418456.0 754879688
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,h5py,remfile,pynwb
A=json.load(open('assets.json'))
def url(a): return f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
for p in ['sub-BH494/sub-BH494_ses-20230817T132836_ecephys.nwb']:
    a=[x for x in A if x['path']==p][0]
    f=h5py.File(remfile.File(url(a)),'r')
    f.visit(lambda n: print(n, f[n].shape if isinstance(f[n],h5py.Dataset) else '', dict(f[n].attrs) if n.count('/')<2 else ''))
EOF
```

```
acquisition  {}
analysis  {}
file_create_date (1,) {}
general  {}
general/data_collection () {}
general/devices  {}
general/devices/array  
general/extracellular_ephys  {}
general/extracellular_ephys/electrodes  
general/extracellular_ephys/electrodes/filtering (32,) 
general/extracellular_ephys/electrodes/group (32,) 
general/extracellular_ephys/electrodes/group_name (32,) 
general/extracellular_ephys/electrodes/id (32,) 
general/extracellular_ephys/electrodes/imp (32,) 
general/extracellular_ephys/electrodes/location (32,) 
general/extracellular_ephys/electrodes/x (32,) 
general/extracellular_ephys/electrodes/y (32,) 
general/extracellular_ephys/electrodes/z (32,) 
general/extracellular_ephys/shank1  
general/institution () {}
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,h5py,remfile,numpy as np
A=json.load(open('assets.json'))
def url(a): return f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
def show(p):
    a=[x for x in A if x['path']==p][0]
    f=h5py.File(remfile.File(url(a)),'r')
    print('==',p,a['size'])
    for k in ['identifier','session_description','general/notes','general/stimulus','general/data_collection','general/institution','general/subject/subject_id','general/subject/description','general/subject/age','general/subject/sex','session_start_time']:
        print(k, f[k][()])
    e=f['general/extracellular_ephys/electrodes']
    for c in e: 
        try: print(' ',c, e[c][:3], len(set(map(str,e[c][:]))))
        except Exception as ex: print(c,ex)
    print(list(f['general/extracellular_ephys']))
    for g in f['general/extracellular_ephys']:
        if g!='electrodes': print(g, dict(f['general/extracellular_ephys'][g].attrs))
    print(dict(f['general/devices/array'].attrs))
    t=f['intervals/trials']; st=t['start_time'][:]; sp=t['stop_time'][:]
    print('trials',len(st),st[:3],sp[:3],np.diff(st).min(),np.diff(st).max(), (sp-st).min(),(sp-st).max())
    u=f['units']; print('units',u['id'].shape, 'labels',np.unique(u['celltype_label'][:],return_counts=True))
    idx=u['spike_times_index'][:]; stt=u['spike_times'][:]
    print('spikes range',stt.min(),stt.max(), 'n per unit',np.diff(np.r_[0,idx])[:10])
    for k in ['acquisition','analysis','processing','stimulus/presentation','stimulus/templates','scratch']: print(k,list(f[k]))
    return f
show('sub-BH494/sub-BH494_ses-20230817T132836_ecephys.nwb')
show('sub-BH494/sub-BH494_ecephys.nwb')
EOF
```

```
== sub-BH494/sub-BH494_ses-20230817T132836_ecephys.nwb 6291256
identifier b'BH494_1500_200_67_5'
session_description b'Neural Spikes for neural pathways to tFUS'
general/notes b'Recording:S1; stim at:S1'
general/stimulus b'intervals contains each tFUS trial start and end timestamps'
general/data_collection b'tFUS parameters {PRF:1500Hz PD:200us UD:67ms}'
general/institution b'Carnegie Mellon University'
general/subject/subject_id b'BH494'
general/subject/description b'HSD:WI rat'
general/subject/age b'P24W'
general/subject/sex b'M'
session_start_time [b'2023-08-17T13:28:36.000000-04:00']
  filtering [b'unknown' b'unknown' b'unknown'] 1
  group [<HDF5 object reference> <HDF5 object reference> <HDF5 object reference>] 1
  group_name [b'shank1elec1' b'shank1elec2' b'shank1elec3'] 32
  id [0 1 2] 32
  imp [nan nan nan] 1
  location [b'unknown' b'unknown' b'unknown'] 1
  x [1. 1. 1.] 3
  y [10. 11.  9.] 12
[... 47 more lines not kept]
```

**Agent**

Files are small NWB units tables with trial times and a `celltype_label` column. Surveying all 1920 files' metadata now.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > survey.py <<'EOF'
import json,h5py,remfile,numpy as np,pandas as pd
from concurrent.futures import ThreadPoolExecutor
A=json.load(open('assets.json'))
def url(a): return f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
def s(x): return x.decode() if isinstance(x,bytes) else str(x)
def one(a):
    try:
        f=h5py.File(remfile.File(url(a)),'r')
        r=dict(path=a['path'],size=a['size'])
        for k in ['identifier','general/notes','general/data_collection','session_description','general/subject/subject_id']:
            r[k.split('/')[-1]]=s(f[k][()]) if k in f else None
        r['start']=s(f['session_start_time'][0])
        r['ntrials']=len(f['intervals/trials/start_time']) if 'intervals/trials' in f else -1
        if 'units' in f:
            u=f['units']; r['ucols']=','.join(s(c) for c in u.attrs['colnames'])
            idx=u['spike_times_index'][:] if 'spike_times_index' in u else []
            r['nunits']=len(idx); r['nspk']=json.dumps(np.diff(np.r_[0,idx]).tolist())
            r['labels']=json.dumps(u['celltype_label'][:].tolist()) if 'celltype_label' in u else None
        else: r['nunits']=-1
        r['top']=','.join(k for k in f.keys())
        r['acq']=','.join(f['acquisition'].keys()); r['ana']=','.join(f['analysis'].keys()); r['proc']=','.join(f['processing'].keys())
        r['nelec']=len(f['general/extracellular_ephys/electrodes/id']) if 'general/extracellular_ephys/electrodes' in f else -1
        return r
    except Exception as e:
        return dict(path=a['path'],err=repr(e))
with ThreadPoolExecutor(48) as ex: rows=list(ex.map(one,A))
pd.DataFrame(rows).to_csv('survey.csv',index=False)
EOF
time python survey.py; python -c "
import pandas as pd; d=pd.read_csv('survey.csv'); print(d.shape); print(d.get('err').dropna().head())"
```

```
real	28m10.780s
user	1m42.074s
sys	0m8.808s
(1920, 19)
1919    ValueError('Illegal slicing argument for scala...
Name: err, dtype: str
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pandas as pd
d=pd.read_csv('survey.csv')
print(d[d.err.notna()][['path','err']].to_string())
d=d[d.err.isna()]
st=d.path.str.contains('STTC')
print('STTC files',st.sum())
print(d[st][['path','identifier','notes','data_collection','ucols','nunits','top','acq','ana','proc','nelec','size']].head(8).to_string())
e=d[~st]
print(e.notes.value_counts())
print(e.ucols.value_counts()); print(e.ntrials.value_counts()); print(e.nelec.value_counts())
print(e.acq.value_counts(dropna=False), e.ana.value_counts(dropna=False), e.proc.value_counts(dropna=False))
print(e.data_collection.value_counts().head(60))
EOF
```

```
Sat Oct 31 23:15:23 UTC 2026
                                 path                                                          err
1919  sub-BH594/sub-BH594_ecephys.nwb  ValueError('Illegal slicing argument for scalar dataspace')
STTC files 370
                                                              path                      identifier                                notes                                data_collection                               ucols  nunits                                                                                                                                                                                   top  acq  ana  proc  nelec         size
443  sub-STTC-BH494/sub-STTC-BH494_ses-20240118T231600_ecephys.nwb       BH494_1500_200_67_5_MOTOR  STTC results of:M1 vsS1; stim at:M1  tFUS parameters {PRF:1500Hz PD:200us UD:67ms}  STTC,STTCAtoB,STTCBtoA,STTCA,STTCB     0.0  acquisition,analysis,file_create_date,general,identifier,intervals,processing,scratch,session_description,session_start_time,specifications,stimulus,timestamps_reference_time,units  NaN  NaN   NaN   32.0   40950408.0
444  sub-STTC-BH494/sub-STTC-BH494_ses-20240119T031300_ecephys.nwb       BH494_3000_200_67_5_MOTOR  STTC results of:M1 vsS1; stim at:M1  tFUS parameters {PRF:3000Hz PD:200us UD:67ms}  STTC,STTCAtoB,STTCBtoA,STTCA,STTCB     0.0  acquisition,analysis,file_create_date,general,identifier,intervals,processing,scratch,session_description,session_start_time,specifications,stimulus,timestamps_reference_time,units  NaN  NaN   NaN   32.0   60032168.0
445                      sub-STTC-BH494/sub-STTC-BH494_ecephys.nwb       BH494_1500_200_67_5_MOTOR  STTC results of:M1 vsS1; stim at:M1  tFUS parameters {PRF:1500Hz PD:200us UD:67ms}  STTC,STTCAtoB,STTCBtoA,STTCA,STTCB     0.0  acquisition,analysis,file_create_date,general,identifier,intervals,processing,scratch,session_description,session_start_time,specifications,stimulus,timestamps_reference_time,units  NaN  NaN   Na
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pandas as pd,re,json,collections
d=pd.read_csv('survey.csv'); d=d[d.err.isna()]
e=d[~d.path.str.contains('STTC')].copy()
e['suffix']=e.identifier.str.split('_').str[5:].str.join('_')
print(e.suffix.value_counts().to_string())
print(e[e.identifier.str.contains('(?i)sham|cg|control|nous')].identifier.tolist()[:20])
def lab(x):
    if pd.isna(x): return 'none'
    return str(sorted(collections.Counter(json.loads(x)).items()))
e['lab']=e.labels.map(lab)
print(e.lab.str[:40].value_counts().head(20))
EOF
```

```
suffix
               986
MOTOR          165
POM_S1         124
POM_MOTOR      112
POM_POM         61
POM             41
2               11
NEW              8
POM_150-95       7
NEAR             4
NEAR_MOTOR       4
POM_155-95       4
POM__150-95      4
POM_S1BF         4
POM_POM_2        2
POM _S1          2
back             2
contra           2
dep05            2
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pandas as pd,re,json,collections
d=pd.read_csv('survey.csv'); d=d[d.err.isna()]
e=d[~d.path.str.contains('STTC')].copy()
allv=collections.Counter()
for x in e.labels.dropna(): allv.update(json.loads(x))
print(allv)
nz=e[e.labels.notna() & e.labels.map(lambda x: isinstance(x,str) and any(v!=0 for v in json.loads(x)))]
print(len(nz)); print(nz[['path','identifier','notes']].head(20).to_string())
EOF
```

```
Counter({0.0: 44185})
0
Empty DataFrame
Columns: [path, identifier, notes]
Index: []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i -E "M1|motor|CG1|sham|cingulate|waveform|dandi|data avail|code avail|github" paper/*.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,h5py,remfile,numpy as np
A=json.load(open('assets.json'))
def url(a): return f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
for p in ['sub-STTC-BH494/sub-STTC-BH494_ses-20240119T055300_ecephys.nwb','sub-BH594/sub-BH594_ecephys.nwb']:
    a=[x for x in A if x['path']==p][0]
    f=h5py.File(remfile.File(url(a)),'r')
    print('==',p)
    def v(n,o):
        if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, {k:(o.attrs[k] if k!='target' else '') for k in o.attrs if k in('description','neurodata_type')})
        else: print(n, {k:o.attrs[k] for k in o.attrs if k in('description','neurodata_type','colnames')})
    f.visititems(v)
    if 'STTC' in p:
        u=f['units']
        for c in ['STTC','STTCAtoB','STTCBtoA','STTCA','STTCB']:
            x=u[c]; print(c,x.shape, x[0] if x.ndim else x[()])
        print(f['general/notes'][()], f['identifier'][()])
    else:
        for k in ['identifier','general/notes','general/data_collection']: print(k,f[k][()])
EOF
```

```
== sub-STTC-BH494/sub-STTC-BH494_ses-20240119T055300_ecephys.nwb
acquisition {}
analysis {}
file_create_date (1,) object {}
general {}
general/data_collection () object {}
general/devices {}
general/devices/array {'description': 'A1x32-Poly3-10mm-50-177-A32', 'neurodata_type': 'Device'}
general/extracellular_ephys {}
general/extracellular_ephys/electrodes {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name'], dtype=object), 'description': 'all electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group_name (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/id (32,) int64 {'neurodata_type': 'ElementIdentifiers'}
general/extracellular_ephys/electrodes/imp (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/location (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/x (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/y (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/z (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
[... 297 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pandas as pd,re,json,collections
pd.set_option('display.width',250)
d=pd.read_csv('survey.csv'); d=d[d.err.isna()]
e=d[~d.path.str.contains('STTC')].copy()
print(e.data_collection.value_counts().iloc[25:].to_string())
e['area']=e.notes.str.extract(r'(?i)recording:\s*([A-Za-z0-9_]*)')[0].str.upper()
e['stim']=e.notes.str.extract(r'(?i)(?:stim at|stimulation):\s*([A-Za-z0-9_]*)')[0].str.upper()
e['prf']=e.data_collection.str.extract(r'PRF:(\w+)Hz')[0]
e['pd']=e.data_collection.str.extract(r'PD:(\w+)us')[0]
e['sub']=e.path.str.split('/').str[0]
print(pd.crosstab(e['sub'],e.area))
print(pd.crosstab(e.area,e.stim))
# duplicates by spike counts
dup=e[e.duplicated('nspk',keep=False)].sort_values('nspk')
print('dup files',len(dup)); print(dup[['path','identifier','area','nunits','size']].head(40).to_string())
e.to_csv('inv.csv',index=False)
EOF
```

```
Series([], )
area          AC  AC_1  AC_2  M1  M1_R  POM  S1  S1BF  S1_1  S1_R  VPM
sub                                                                   
sub-BH494  0   0     0     0  25     2    0  24     0     0     2    0
sub-BH495  0   0     0     0  21     0   16  38     0     0     0    0
sub-BH499  0   0     0     0  18     0   20  35     3     0     0    1
sub-BH500  8   0     0     0  11     0    0  12     0     0     0    0
sub-BH501  0   0     0     0  22     0   18  38     0     0     0    0
sub-BH510  0   0     0     0  10     0   14  24     0     0     0    0
sub-BH511  0   0     0     0  28     0   30  57     0     0     0    0
sub-BH513  0   0     0     0  30     0   26  53     0     0     0    0
sub-BH528  0   0     0     0  29     0   28  60     0     0     0    0
sub-BH530  0  32     0     0   0     0    0  32     0     0     0    0
sub-BH532  0  43     0     0   0     0    0  42     0     0     0    0
sub-BH535  0  46     0     0   0     0    0  46     0     0     0    0
sub-BH537  0  44     0     0   0     0    0  29     0     0     0    0
sub-BH538  0  44     2     2   0     0    0  44     0     2     0    0
sub-BH539  0  46     0     0   0     0    0  46     0     0     0    0
sub-BH547  0  44     0     0   0     0    0  44     0     0     0    0
sub-BH551  0   0     0     0   0     0   46  42     0     0     0    0
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,h5py,remfile,numpy as np,time,requests,pandas as pd
inv=pd.read_csv('inv.csv')
A={a['path']:a for a in json.load(open('assets.json'))}
ac=inv[(inv.area=='AC')&(inv.stim=='S1')]
print(ac.identifier.str.split('_').str[5:].str.join('_').value_counts())
print(ac.groupby(['prf','pd']).size().to_string())
p=ac[ac.pd=='200'].path.iloc[0]
a=A[p]
t=time.time()
r=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=False); s3=r.headers['Location']; print(s3[:80], time.time()-t)
for u in [s3, f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"]:
    t=time.time(); f=h5py.File(remfile.File(u),'r'); st=f['units/spike_times'][:]; ix=f['units/spike_times_index'][:]; tr=f['intervals/trials/start_time'][:]; print(len(st), time.time()-t)
t=time.time(); b=requests.get(s3).content; print('full get',len(b),time.time()-t)
EOF
```

```
identifier
          293
2           2
back        1
dep05       1
front       1
contra      1
Name: count, dtype: int64
prf     pd     
30.0    10000      14
        200         6
        2000       16
        20000      12
        30000      14
300.0   1000       14
        20         12
        200         6
        2000       12
        3000       14
1500.0  200         8
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,requests
A=json.load(open('assets.json'))
a=[x for x in A if 'BH535' in x['path'] and 'STTC' not in x['path']][0]
m=requests.get(f"https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/{a['asset_id']}/").json()
print(json.dumps(m,indent=0)[:3000])
EOF
```

```
{
"id": "dandiasset:862254c1-a27d-4e59-a623-2a34ef1502b0",
"path": "sub-BH535/sub-BH535_ses-20231221T203900_ecephys.nwb",
"access": [
{
"schemaKey": "AccessRequirements",
"status": "dandi:OpenAccess"
}
],
"digest": {
"dandi:dandi-etag": "868bdf0c206f52d544ac772b259f2b19-1",
"dandi:sha2-256": "f17b4264535793a37801af60a828bf5e9f64e9faa340bf18216ec3dbec453d01"
},
"@context": "https://raw.githubusercontent.com/dandi/schema/master/releases/0.6.7/context.json",
"approach": [
{
"name": "electrophysiological approach",
"schemaKey": "ApproachType"
}
],
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import json,h5py,remfile,numpy as np,time
from concurrent.futures import ThreadPoolExecutor
A=[a for a in json.load(open('assets.json')) if 'STTC' not in a['path']][:120]
def one(a):
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    return f['identifier'][()], f['general/notes'][()], f['units/spike_times_index'][:]
t=time.time()
with ThreadPoolExecutor(32) as ex: r=list(ex.map(one,A))
print(time.time()-t)
EOF
```

```
113.15131950378418
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pandas as pd
inv=pd.read_csv('inv.csv')
print(inv['size'].sum()/1e9, len(inv))
for q in ["stim=='S1' and pd=='200'", "stim=='S1'"]:
    s=inv.query(q); print(q, len(s), s['size'].sum()/1e9)
EOF
```

```
4.794111152 1549
stim=='S1' and pd=='200' 393 1.271226008
stim=='S1' 1149 3.438011808
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && nproc && cat > tp.py <<'EOF'
import json,h5py,remfile,numpy as np,time
from multiprocessing import Pool
A=[a for a in json.load(open('assets.json')) if 'STTC' not in a['path']][:120]
def one(a):
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    return f['identifier'][()], f['general/notes'][()], f['units/spike_times_index'][:]
if __name__=='__main__':
    t=time.time()
    with Pool(24) as p: r=p.map(one,A,chunksize=1)
    print(time.time()-t)
EOF
python tp.py
```

```
4
7.09310245513916
Shell cwd was reset to
```

**Agent**

Process-based reading takes about 90 s for the full inventory, which is fine for a notebook. Writing the helper module now.

**Agent calls Bash**

```bash
mkdir -p entries/000946-gao-2025; date -u; grep -n -i -E "kruskal|wilcoxon|bonferroni|statistical analysis" paper/*.txt | head; grep -n -i -A3 "^Statistical analysis" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/000946-gao-2025/tfus.py",
 "content": "\"\"\"Loading and spiking measures for dandiset 000946 (Gao, Ramachandran, Yu & He 2025).\n\nThe dandiset holds one NWB file per recorded area and session: a units table with\nspike times and a `celltype_label` column, and a trials table whose `start_time`\nis taken as sonication onset (checked in the notebook). The session's parameters\nare in `identifier` (`<rat>_<PRF>_<PD>_<UD>_<n>[_suffix]`), `general/notes`\n(`Recording:<area>; stim at:<target>`) and `general/data_collection`\n(`tFUS parameters {PRF:..Hz PD:..us UD:67ms}`).\n\nWhere each parameter comes from:\n\n- `MIN_SPIKES = 2000`: Methods, Neuronal type classification (\"Only neurons that\n  fire >2,000 spikes for each session were considered\"); the claims file header,\n  Units.\n- `WINDOWS` (67 ms bins from sonication onset, 0 to 268 ms) and the baseline\n  [-67, 0) ms: claims file header, Windows, and Statistical analysis (\"normalized\n  to the pre-stim period (67 ms pre-stim)\").\n- `normalized_rates`, readings N1 and N2, and the comparison windows B1 and B2:\n  claims file header, Normalized spiking rate and Test against baseline.\n- `vs_baseline`: one-tailed two-sample Wilcoxon (rank-sum) test against the\n  baseline sample with Bonferroni correction over the comparisons in the panel\n  (reading C1), significance 0.01: Statistical analysis and the claims file\n  header. `kruskal_levels`: Kruskal-Wallis across parameter levels, units as\n  observations (claims file header).\n- Removing duplicate deposits (`dedupe`): protocol, author step 1.2; a file is a\n  duplicate of another when subject, identifier, recorded area and the spike\n  count of every unit are the same. The notebook checks that the spike times of\n  such pairs are identical.\n- `N_PROC` (processes used to stream files) and the shift used for the clock\n  check are standard choices that cannot change a result.\n\"\"\"\nimport json\nimport re\nfrom multiprocessing import Pool\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\nfrom scipy import stats\n\nDANDISET_ID = \"000946\"\nVERSION = \"0.250829.1249\"\nAPI = \"https://api.dandiarchive.org/api\"\nMIN_SPIKES = 2000\nBASELINE = (-0.067, 0.0)\nPRE_BASELINE = (-0.134, -0.067)\nWINDOWS = {\n    \"0-67\": (0.0, 0.067),\n    \"67-134\": (0.067, 0.134),\n    \"134-201\": (0.134, 0.201),\n    \"201-268\": (0.201, 0.268),\n}\nN_PROC = 24\n\n\ndef list_assets(version=VERSION):\n    \"\"\"All assets of the pinned version: path, asset id and size.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000\"\n    out = []\n    while url:\n        r = requests.get(url, timeout=60)\n        r.raise_for_status()\n        js = r.json()\n        out += [dict(path=a[\"path\"], asset_id=a[\"asset_id\"], size=a[\"size\"]) for a in js[\"results\"]]\n        url = js[\"next\"]\n    return out\n\n\ndef version_info(version=VERSION):\n    r = requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/info/\", timeout=60)\n    r.raise_for_status()\n    return r.json()\n\n\ndef asset_url(asset_id):\n    return f\"{API}/assets/{asset_id}/download/\"\n\n\ndef _open(asset_id):\n    return h5py.File(remfile.File(asset_url(asset_id)), \"r\")\n\n\ndef _s(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef parse_header(identifier, notes, data_collection):\n    \"\"\"Area, target, PRF (Hz) and PD (us) from the file's text fields.\"\"\"\n    m = re.search(r\"(?i)recording:\\s*([A-Za-z0-9_]*)\", notes or \"\")\n    area = m.group(1).upper() if m else \"\"\n    m = re.search(r\"(?i)(?:stim at|stimulation):\\s*([A-Za-z0-9_]*)\", notes or \"\")\n    stim = m.group(1).upper() if m else \"\"\n    m = re.search(r\"PRF:(\\w+)Hz\", data_collection or \"\")\n    prf = float(m.group(1)) if m else np.nan\n    m = re.search(r\"PD:(\\w+)us\", data_collection or \"\")\n    pd_us = float(m.group(1).replace(\"point\", \".\")) if m else np.nan\n    return area, stim, prf, pd_us\n\n\ndef read_header(asset):\n    \"\"\"Metadata, trial count and per-unit spike counts of one file (no spike times).\"\"\"\n    try:\n        f = _open(asset[\"asset_id\"])\n        r = dict(asset)\n        r[\"identifier\"] = _s(f[\"identifier\"][()])\n        r[\"notes\"] = _s(f[\"general/notes\"][()]) if \"general/notes\" in f else \"\"\n        r[\"data_collection\"] = _s(f[\"general/data_collection\"][()]) if \"general/data_collection\" in f else \"\"\n        r[\"subject_id\"] = _s(f[\"general/subject/subject_id\"][()])\n        ts = f[\"session_start_time\"]\n        r[\"session_start\"] = _s(ts[0] if ts.shape else ts[()])\n        r[\"n_trials\"] = len(f[\"intervals/trials/start_time\"])\n        u = f[\"units\"]\n        r[\"unit_columns\"] = \",\".join(_s(c) for c in u.attrs[\"colnames\"])\n        r[\"groups\"] = \",\".join(k for k in (\"acquisition\", \"analysis\", \"processing\") if len(f[k]))\n        if \"spike_times_index\" in u:\n            idx = u[\"spike_times_index\"][:]\n            r[\"n_spikes\"] = json.dumps(np.diff(np.r_[0, idx]).astype(int).tolist())\n            r[\"n_units\"] = len(idx)\n            if \"celltype_label\" in u:\n                lab = u[\"celltype_label\"][:]\n                r[\"labels\"] = json.dumps(sorted(set(np.asarray(lab).ravel().tolist())))\n            else:\n                r[\"labels\"] = \"absent\"\n        else:\n            r[\"n_spikes\"], r[\"n_units\"], r[\"labels\"] = \"[]\", 0, \"absent\"\n        r[\"area\"], r[\"stim\"], r[\"prf\"], r[\"pd_us\"] = parse_header(r[\"identifier\"], r[\"notes\"], r[\"data_collection\"])\n        r[\"error\"] = \"\"\n        return r\n    except Exception as e:  # recorded and reported in the notebook\n        r = dict(asset)\n        r[\"error\"] = repr(e)\n        return r\n\n\ndef inventory(assets, processes=N_PROC):\n    \"\"\"read_header over many files, in parallel processes (h5py serialises threads).\"\"\"\n    import pandas as pd\n    with Pool(processes) as p:\n        rows = p.map(read_header, assets, chunksize=1)\n    return pd.DataFrame(rows)\n\n\ndef dedupe(inv):\n    \"\"\"Keep one file of each group with the same subject, identifier, area and per-unit spike counts.\n\n    Returns the kept table and a table of the duplicate pairs (kept path, dropped path).\n    \"\"\"\n    inv = inv.sort_values(\"path\").copy()\n    key = [\"subject_id\", \"identifier\", \"area\", \"n_spikes\"]\n    inv[\"dup_of\"] = None\n    first = {}\n    for i, r in inv.iterrows():\n        k = tuple(r[c] for c in key)\n        if k in first:\n            inv.at[i, \"dup_of\"] = first[k]\n        else:\n            first[k] = r[\"path\"]\n    kept = inv[inv.dup_of.isna()].copy()\n    dropped = inv[inv.dup_of.notna()][[\"dup_of\", \"path\"]].rename(columns={\"dup_of\": \"kept\", \"path\": \"dropped\"})\n    return kept, dropped\n\n\ndef load_session(asset_id):\n    \"\"\"Trial start times and the spike times of every unit of one file.\"\"\"\n    f = _open(asset_id)\n    st = f[\"intervals/trials/start_time\"][:]\n    sp = f[\"intervals/trials/stop_time\"][:]\n    idx = f[\"units/spike_times_index\"][:]\n    times = f[\"units/spike_times\"][:]\n    units = np.split(times, idx[:-1].astype(int))\n    return dict(start=st, stop=sp, units=units)\n\n\ndef spike_hash(asset_id):\n    \"\"\"A digest of all spike times and trial starts, to compare duplicate deposits.\"\"\"\n    import hashlib\n    s = load_session(asset_id)\n    h = hashlib.sha256()\n    for u in s[\"units\"]:\n        h.update(np.asarray(u, dtype=np.float64).tobytes())\n    h.update(np.asarray(s[\"start\"], dtype=np.float64).tobytes())\n    return h.hexdigest()\n\n\ndef window_counts(spikes, onsets, win):\n    \"\"\"Spike count of one unit in [onset + win[0], onset + win[1]) for every onset.\"\"\"\n    spikes = np.sort(spikes)\n    a = np.searchsorted(spikes, onsets + win[0], side=\"left\")\n    b = np.searchsorted(spikes, onsets + win[1], side=\"left\")\n    return b - a\n\n\ndef unit_counts(session, onsets=None, windows=None):\n    \"\"\"Per unit with more than MIN_SPIKES spikes: counts per trial in baseline, pre-baseline and each window.\"\"\"\n    onsets = session[\"start\"] if onsets is None else onsets\n    windows = WINDOWS if windows is None else windows\n    out = []\n    for k, u in enumerate(session[\"units\"]):\n        if len(u) <= MIN_SPIKES:\n            continue\n        c = dict(unit=k, n_spikes=len(u),\n                 base=window_counts(u, onsets, BASELINE),\n                 pre=window_counts(u, onsets, PRE_BASELINE))\n        for w, rng in windows.items():\n            c[w] = window_counts(u, onsets, rng)\n        out.append(c)\n    return out\n\n\ndef normalized_rates(c, window, reading):\n    \"\"\"Normalized rate (percent) of one unit in `window` (\"pre\" for [-134, -67) ms).\n\n    N1: mean count in the window over trials / mean count in [-67, 0) ms (nan if zero).\n    N2: mean over trials with a nonzero baseline of the per-trial ratio.\n    \"\"\"\n    x = c[window].astype(float)\n    b = c[\"base\"].astype(float)\n    if reading == \"N1\":\n        return 100 * x.mean() / b.mean() if b.mean() > 0 else np.nan\n    if reading == \"N2\":\n        ok = b > 0\n        return 100 * np.mean(x[ok] / b[ok]) if ok.any() else np.nan\n    raise ValueError(reading)\n\n\ndef baseline_sample(cs, nreading, breading):\n    \"\"\"The sample a window is compared with: B1, normalized [-67, 0) ms; B2, normalized [-134, -67) ms.\"\"\"\n    w = \"base\" if breading == \"B1\" else \"pre\"\n    return np.array([normalized_rates(c, w, nreading) for c in cs])\n\n\ndef vs_baseline(x, base, n_comparisons, alternative=\"greater\"):\n    \"\"\"One-tailed rank-sum of a window's values against the baseline sample, Bonferroni-corrected.\"\"\"\n    x = np.asarray(x, float)\n    base = np.asarray(base, float)\n    x, base = x[np.isfinite(x)], base[np.isfinite(base)]\n    p = stats.mannwhitneyu(x, base, alternative=alternative).pvalue\n    return min(1.0, p * n_comparisons), p\n\n\ndef kruskal_levels(groups):\n    g = [np.asarray(v, float)[np.isfinite(v)] for v in groups]\n    return stats.kruskal(*g).pvalue\n\n\ndef map_sessions(func, ids, processes=N_PROC):\n    with Pool(processes) as p:\n        return p.map(func, ids, chunksize=1)\n"
}
```

```
File created successfully at: entries/000946-gao-2025/tfus.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > inv2.py <<'EOF'
import sys,time; sys.path.insert(0,'entries/000946-gao-2025')
import tfus
if __name__=='__main__':
    t=time.time(); A=tfus.list_assets(); print(len(A), time.time()-t)
    inv=tfus.inventory(A); print(time.time()-t)
    inv.to_pickle('inv2.pkl'); print(inv.error.value_counts().head())
EOF
python inv2.py
```

```
1920 0.9116072654724121
106.05710530281067
error
    1920
Name: count, dtype: int64
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > proto1.py <<'EOF'
import sys,time; sys.path.insert(0,'entries/000946-gao-2025')
import tfus, pandas as pd, numpy as np, json
pd.set_option('display.width',250)
if __name__=='__main__':
    inv=pd.read_pickle('inv2.pkl')
    sttc=inv.path.str.startswith('sub-STTC')
    e=inv[~sttc]
    kept,dropped=tfus.dedupe(e)
    print(len(e),len(kept),len(dropped))
    # groups of more than 2?
    print(dropped.kept.value_counts().value_counts())
    # verify a sample of 20 duplicate pairs by spike hash
    samp=dropped.sample(20,random_state=0)
    ids=dict(zip(e.path,e.asset_id))
    t=time.time()
    h1=tfus.map_sessions(tfus.spike_hash,[ids[p] for p in samp.kept]); h2=tfus.map_sessions(tfus.spike_hash,[ids[p] for p in samp.dropped])
    print('identical',sum(a==b for a,b in zip(h1,h2)), time.time()-t)
    k=kept[kept.stim=='S1']
    print(pd.crosstab([k.area],[k.pd_us]).to_string())
    print(pd.crosstab(k[k.pd_us==200].subject_id,[k[k.pd_us==200].area,k[k.pd_us==200].prf]).to_string())
    kept.to_pickle('kept.pkl')
EOF
python proto1.py
```

```
1550 816 734
count
1    730
2      2
Name: count, dtype: int64
identical 20 3.879779815673828
pd_us  1.4      2.0      4.0      14.0     20.0     40.0     67.0     100.0    134.0    200.0    300.0    400.0    600.0    1000.0   2000.0   3000.0   10000.0  20000.0  30000.0
area                                                                                                                                                                            
             0        0        0        0        0        0        0        0        0        2        0        0        0        0        0        0        0        0        0
AC           6        6        6        7       12        6        7       11        6       17        7        6        7        7       14        7        7        6        7
AC_1         0        0        0        0        0        1        0        0        0        0        0        0        0        0        0        0        0        0        0
AC_2         0        0        0        0        0        1        0        0        0        0        0        0        0        0        0        0        0        0        0
M1           0        0        0        0        0        0        0        0        0       38        0        0        0        0        0        0        0        0        0
POM          2        2        3        3        5        3        3        3        3       46        3        3        3        3        4        2        3        3        3
S1           7        7        9        9       17        9       10       14        8      101        9        8        9       10       18        9       10        9       10
S1_1         0        0        0        0        0        1        0        0        0        0        0        0        0        0        0        0        0        0        0
area                         AC                                 M1                                POM                                 S1
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > proto2.py <<'EOF'
import sys,time; sys.path.insert(0,'entries/000946-gao-2025')
import tfus, pandas as pd, numpy as np, json
pd.set_option('display.width',250)
def load_counts(aid):
    s=tfus.load_session(aid); return tfus.unit_counts(s), len(s['units'])
if __name__=='__main__':
    k=pd.read_pickle('kept.pkl')
    print(k[k.area==''][['path','identifier','notes','prf','pd_us']].to_string())
    ac=k[(k.area=='AC')&(k.stim=='S1')&(k.pd_us==200)].sort_values('prf')
    print(ac[['path','identifier','prf','n_trials','n_units']].to_string())
    t=time.time()
    res=tfus.map_sessions(load_counts, list(ac.asset_id)); print('load',time.time()-t)
    ac['cs']=[r[0] for r in res]
    print(ac.groupby('prf').cs.apply(lambda s: sum(len(x) for x in s)))
    prfs=[30.,300.,1500.,3000.,4500.]
    for N in ['N1','N2']:
      for B in ['B1','B2']:
        for w in ['0-67','67-134','134-201','201-268']:
            groups=[]; line=[]
            for p in prfs:
                cs=[c for x in ac[ac.prf==p].cs for c in x]
                x=np.array([tfus.normalized_rates(c,w,N) for c in cs]); groups.append(x)
                b=tfus.baseline_sample(cs,N,B)
                pc,_=tfus.vs_baseline(x,b,5)
                line.append(f"{int(p)}:{np.nanmean(x):.1f}{'*' if pc<0.01 else ''}(p={pc:.1e},n={np.isfinite(x).sum()})")
            print(N,B,w,'KW p=%.2e'%tfus.kruskal_levels(groups),' '.join(line))
EOF
python proto2.py
```

```
path                  identifier                      notes     prf  pd_us
173   sub-BH500/sub-BH500_ses-20230810T112100_ecephys.nwb         BH500_3000_200_67_5     Recording:; stim at:S1  3000.0  200.0
175   sub-BH500/sub-BH500_ses-20230810T124100_ecephys.nwb   BH500_3000_200_67_5_MOTOR     Recording:; stim at:M1  3000.0  200.0
1917  sub-BH500/sub-BH500_ses-20230810T130600_ecephys.nwb        BH500_1500_200_201_5  recording:;stimulation:S1     NaN    NaN
1918  sub-BH500/sub-BH500_ses-20230810T135500_ecephys.nwb  BH500_1500_200_201_5_MOTOR  recording:;stimulation:M1     NaN    NaN
177   sub-BH500/sub-BH500_ses-20230814T100900_ecephys.nwb         BH500_1500_200_67_5     Recording:; stim at:S1  1500.0  200.0
                                                     path           identifier     prf  n_trials  n_units
936   sub-BH535/sub-BH535_ses-20231225T180600_ecephys.nwb    BH535_30_200_67_5    30.0       500       49
1191  sub-BH539/sub-BH539_ses-20240124T173900_ecephys.nwb    BH539_30_200_67_5    30.0       500       23
1316  sub-BH547/sub-BH547_ses-20240223T133300_ecephys.nwb    BH547_30_200_67_5    30.0       500       57
1040  sub-BH537/sub-BH537_ses-20240108T223000_ecephys.nwb   BH537_300_200_67_5   300.0       500       25
1111  sub-BH538/sub-BH538_ses-20240109T193100_ecephys.nwb   BH538_300_200_67_5   300.0       500       57
803   sub-BH530/sub-BH530_ses-20231202T152500_ecephys.nwb   BH530_300_200_67_5   300.0       500       10
1061  sub-BH537/sub-BH537_ses-20240109T122200_ecephys.nwb  BH537_1500_200_67_5  1500.0       500       24
984   sub-BH535/sub-BH535_ses-20240103T143800_ecephys.nwb  BH535_1500_200_67_5  1500.0       500       50
1187  sub-BH539/sub-BH539_ses-20240123T201500_ecephys.nwb  BH539_1500_200_67_5  1500.0       500       61
817   sub-BH530/sub-BH530_ses-20231202T175400_ecephys.nwb  BH530_1500_200_67_5  1500.0       500        5
1256  sub-BH539/sub-BH539_ses-20240126T181400_ecephys.nwb  BH539_3000_200_67_5  3000.0       500       60
1004  sub-BH5
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pandas as pd, json, numpy as np
pd.set_option('display.width',250)
k=pd.read_pickle('kept.pkl')
s=k[(k.subject_id.isin(['BH495','BH551']))&(k.pd_us==200)].sort_values(['subject_id','prf','session_start'])
print(s[['subject_id','identifier','area','stim','prf','session_start','n_units']].to_string())
EOF
```

```
subject_id                     identifier area stim     prf                     session_start  n_units
47        BH495              BH495_30_200_67_5   S1   S1    30.0  2023-08-21T17:15:24.000000-04:00       17
50        BH495              BH495_30_200_67_5   M1   S1    30.0  2023-08-21T17:23:24.000000-04:00       14
83        BH495        BH495_30_200_67_5_MOTOR   S1   M1    30.0  2023-08-28T11:27:06.000000-04:00        6
85        BH495        BH495_30_200_67_5_MOTOR   M1   M1    30.0  2023-08-28T11:56:18.000000-04:00        6
88        BH495       BH495_30_200_67_5_POM_S1  POM   S1    30.0  2023-08-28T12:04:57.000000-04:00       60
87        BH495       BH495_30_200_67_5_POM_S1   S1   S1    30.0  2023-08-28T16:10:54.000000-04:00       12
64        BH495             BH495_300_200_67_5   S1   S1   300.0  2023-08-21T22:33:32.000000-04:00       11
66        BH495             BH495_300_200_67_5   M1   S1   300.0  2023-08-21T22:43:14.000000-04:00       17
90        BH495       BH495_300_200_67_5_MOTOR   M1   M1   300.0  2023-10-26T21:37:27.000000-04:00        5
94        BH495       BH495_300_200_67_5_MOTOR   S1   M1   300.0  2023-10-26T21:46:51.000000-04:00        6
93        BH495      BH495_300_200_67_5_POM_S1  POM   S1   300.0  2023-10-26T21:55:41.000000-04:00       55
96        BH495      BH495_300_200_67_5_POM_S1   S1   S1   300.0  2023-10-26T22:02:07.000000-04:00        6
98        BH495   BH495_300_200_67_5_POM_MOTOR  POM   M1   300.0  2023-10-26T22:13:53.000000-04:00       63
100       BH495   BH495_300_200_67_5_POM_MOTOR   S1   M1   300.0  2023-10-26T22:17:01.000000-04:00        3
29        BH495            BH495_1500_200_67_5   S1   S1  1500.0  2023-08-20T15:04:27.000000-04:00        2
31        BH495            BH495_1500_200_67_5   M1   S1  1500.0  2023-08-20T15:30:45.000000-04:00       10
34        BH495      BH495_1500_200_67_5_MOTOR   S1   M1  1500.0  2023-08-20T15:36:54.000000-04:00        4
26        BH495      BH495_1500_200_67_5_MOTOR   M1   M1  150
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c['metadata'], ''.join(c['source'])[:700],'\n----')
print(nb['metadata'])
EOF
grep -n "def check" -A5 tools/entry.py | head -40; grep -n -i "install\|tag\|sanity\|claim:" tools/entry.py | head -40
```

```
markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository
that holds code only). This is the only published version.  
----
code {} import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 143,330p tools/entry.py
```

```
def check(entry_dir: Path) -> Report:
    report = Report()
    rel = entry_dir.relative_to(ROOT)
    entry = validate(report, entry_dir / "entry.yaml", "entry")
    if entry is None:
        return report
    if entry.get("name") != entry_dir.name:
        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")

    listed = [n["path"] for n in entry.get("notebooks", [])]
    present = sorted(p.name for p in entry_dir.glob("*.ipynb"))
    for name in sorted(set(present) - set(listed)):
        report.error(rel / name, "notebook is not listed in entry.yaml")
    for name in sorted(set(listed) - set(present)):
        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
    helpers = entry.get("helpers", [])
    for name in helpers:
        if not (entry_dir / name).is_file():
            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")

[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/000946-gao-2025 && python - <<'EOF'
p='tfus.py'; s=open(p).read()
s=s.replace('''def map_sessions(func, ids, processes=N_PROC):
    with Pool(processes) as p:
        return p.map(func, ids, chunksize=1)
''','''PSTH_EDGES = np.round(np.arange(-0.5, 1.0 + 1e-9, 0.01), 3)
CLOCK_SHIFT = 1.0


def session_counts(asset_id):
    """Window counts of the units with more than MIN_SPIKES spikes, at the trial starts and at the trial
    starts shifted by CLOCK_SHIFT s (for the clock check), with each unit's PSTH (10 ms bins, -0.5 to 1 s,
    spikes per trial), the trial starts and the total number of units in the file."""
    s = load_session(asset_id)
    onsets = s["start"]
    true = unit_counts(s, onsets)
    shifted = unit_counts(s, onsets + CLOCK_SHIFT)
    psth = []
    for u in s["units"]:
        if len(u) <= MIN_SPIKES:
            continue
        u = np.sort(u)
        h = np.zeros(len(PSTH_EDGES) - 1)
        for t0 in onsets:
            a, b = np.searchsorted(u, [t0 + PSTH_EDGES[0], t0 + PSTH_EDGES[-1]])
            h += np.histogram(u[a:b] - t0, PSTH_EDGES)[0]
        psth.append(h / len(onsets))
    return dict(true=true, shifted=shifted, psth=psth, start=onsets, n_units=len(s["units"]),
                spikes_per_unit=[len(u) for u in s["units"]])


def map_sessions(func, ids, processes=N_PROC):
    """Map over files in forked processes (h5py serialises threads, so threads do not overlap the reads)."""
    from multiprocessing import get_context
    with get_context("fork").Pool(processes) as p:
        return p.map(func, ids, chunksize=1)
''')
s=s.replace('''    import pandas as pd
    with Pool(processes) as p:
        rows = p.map(read_header, assets, chunksize=1)''','''    import pandas as pd
    rows = map_sessions(read_header, assets, processes)''')
s=s.replace("from multiprocessing import Pool\n\n","")
open(p,'w').write(s)
EOF
grep -n "Pool" tfus.py
```

```
Sat Oct 31 23:23:29 UTC 2026
273:    with get_context("fork").Pool(processes) as p:
```

**Agent calls Bash**

```bash
cd  && grep -n "^- id:" claims/000946/*.yaml | awk '{print $3}' | tr '\n' ' '; grep -c "^- id:" claims/000946/*.yaml
```

```
fig4-unit-counts fig4a-s1-rsu-time-locked-3000 fig4b-pom-rsu-time-locked-3000 fig4-postsonication-3000 fig4-30hz-responses fig4-fsu-no-change fig5a-sham-no-change fig5b-cg1-control-no-change fig6-unit-counts fig6a-s1-rsu-time-locked-prf fig6a-s1-rsu-delayed-prf fig6b-s1-fsu-prf fig6c-pom-rsu-prf fig6d-pom-fsu-prf fig7a-s1-rsu-dc-3000 fig7b-s1-fsu-dc-3000 fig7c-pom-rsu-dc-3000 fig7d-pom-fsu-dc-3000 fig8a-s1-rsu-dc-30 fig8b-s1-fsu-dc-30 fig9a-s1-rsu-prf-60dc fig9b-s1-fsu-prf-60dc fig10a-dsttc-3000 fig10b-dsttc-30 fig10c-sttc-constant-pd fig10d-sttc-60dc fig10e-sttc-dc-30 fig10f-sttc-dc-3000 pathway-follows-local-prf fig11b-ac-responses fig11c-ac-to-s1-30hz fig11d-ac-to-s1-3000 auditory-confound-low-prf 33
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pandas as pd
inv=pd.read_pickle('inv2.pkl'); s=inv[inv.path.str.startswith('sub-STTC')]
print(s.notes.value_counts().to_string()); print(s.unit_columns.value_counts())
EOF
```

```
notes
STTC results of:AC vsS1; stim at:S1        126
STTC results of:POM vsS1; stim at:S1        89
STTC results of:M1 vsS1; stim at:S1         46
STTC results of:M1 vsS1; stim at:M1         42
STTC results of:POM vsS1; stim at:M1        30
STTC results of:POM vsS1; stim at:POM       18
STTC results of:M1 vsS1; stim at:POM        13
STTC results of:POM vsS1BF; stim at:S1       2
STTC results of:S1BF vsVPM; stim at:S1       2
STTC results of: vs; stim at:S1              1
STTC results of:AC_1 vsAC_2; stim at:S1      1
unit_columns
STTC,STTCAtoB,STTCBtoA,STTCA,STTCB    370
Name: count, dtype: int64
Shell cwd was reset to
```

**Agent**

Writing the notebook now. One claim (Fig. 11B, AC neurons) can be tested. The other 32 need the RSU/FSU split, sham/CG1 sessions, or claims that depend on those.

**Agent calls Bash**

```bash
cd entries/000946-gao-2025 && python - <<'EOF'
p='tfus.py'; s=open(p).read()
s=s.replace('''def unit_counts(session, onsets=None, windows=None):
    """Per unit with more than MIN_SPIKES spikes: counts per trial in baseline, pre-baseline and each window."""
    onsets = session["start"] if onsets is None else onsets
    windows = WINDOWS if windows is None else windows
    out = []
    for k, u in enumerate(session["units"]):
        if len(u) <= MIN_SPIKES:
            continue''','''def unit_counts(session, onsets=None, windows=None, min_spikes=MIN_SPIKES):
    """Per unit with more than `min_spikes` spikes: counts per trial in baseline, pre-baseline and each window."""
    onsets = session["start"] if onsets is None else onsets
    windows = WINDOWS if windows is None else windows
    out = []
    for k, u in enumerate(session["units"]):
        if len(u) <= min_spikes:
            continue''')
s=s.replace('''    """Window counts of the units with more than MIN_SPIKES spikes, at the trial starts and at the trial
    starts shifted by CLOCK_SHIFT s (for the clock check), with each unit's PSTH (10 ms bins, -0.5 to 1 s,
    spikes per trial), the trial starts and the total number of units in the file."""
    s = load_session(asset_id)
    onsets = s["start"]
    true = unit_counts(s, onsets)
    shifted = unit_counts(s, onsets + CLOCK_SHIFT)
    psth = []
    for u in s["units"]:
        if len(u) <= MIN_SPIKES:
            continue
        u = np.sort(u)''','''    """Window counts of every unit (the MIN_SPIKES rule is applied by the caller, so that it can be varied),
    at the trial starts and at the trial starts shifted by CLOCK_SHIFT s (for the clock check), with each
    unit's PSTH (10 ms bins, -0.5 to 1 s, spikes per trial), the trial starts and the number of units."""
    s = load_session(asset_id)
    onsets = s["start"]
    true = unit_counts(s, onsets, min_spikes=0)
    shifted = unit_counts(s, onsets + CLOCK_SHIFT, min_spikes=0)
    psth = []
    for u in s["units"]:
        u = np.sort(u)''')
open(p,'w').write(s)
EOF
grep -n "min_spikes\|def " tfus.py
```

```
55:def list_assets(version=VERSION):
68:def version_info(version=VERSION):
74:def asset_url(asset_id):
78:def _open(asset_id):
82:def _s(x):
86:def parse_header(identifier, notes, data_collection):
99:def read_header(asset):
134:def inventory(assets, processes=N_PROC):
141:def dedupe(inv):
161:def load_session(asset_id):
172:def spike_hash(asset_id):
183:def window_counts(spikes, onsets, win):
191:def unit_counts(session, onsets=None, windows=None, min_spikes=MIN_SPIKES):
192:    """Per unit with more than `min_spikes` spikes: counts per trial in baseline, pre-baseline and each window."""
197:        if len(u) <= min_spikes:
208:def normalized_rates(c, window, reading):
224:def baseline_sample(cs, nreading, breading):
230:def vs_baseline(x, base, n_comparisons, alternative="greater"):
239:def kruskal_levels(groups):
248:def session_counts(asset_id):
[... 3 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/gen_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Gao, Ramachandran, Yu & He (2025) from dandiset 000946\n\n**Paper.** Gao H, Ramachandran S, Yu K, He B (2025). Transcranial focused ultrasound modulates feedforward\nand feedback cortico-thalamo-cortical pathways by selectively activating excitatory neurons. *J Neurosci*\n45(23): e2218242025. [doi:10.1523/jneurosci.2218-24.2025](https://doi.org/10.1523/jneurosci.2218-24.2025).\nThe claims file (`claims/000946/10.1523-jneurosci.2218-24.2025.yaml`) was written from the version of\nrecord as served by PubMed Central (PMC12139594): main text, Methods and figure legends; the paper has no\nsupplement and links no analysis code.\n\n**Dandiset.** [DANDI:000946](https://dandiarchive.org/dandiset/000946/0.250829.1249), version\n0.250829.1249. The paper cites the dandiset without a version (Methods, Electrophysiological recordings:\n\"All experimental data has been made public in a repository at the DANDI Archive\n(https://dandiarchive.org/dandiset/000946)\"), so the most recent published version is pinned. The data\ncheck below compares its file list with the earliest published version, 0.250711.1640; all six published\nversions list the same 1920 files.\n\n**What the dataset holds.** One NWB file per recorded area and session, each with a units table (spike\ntimes and a `celltype_label` column) and a trials table. There are no spike waveforms in any file, and\n`celltype_label`, described as \"label 1 = RSU, label 2 = FSU\", is 0 for every unit. The paper splits units\ninto RSUs and FSUs by k-means on waveform measures (Methods, Neuronal type classification), so every claim\nabout RSUs or FSUs, and every claim built on them, cannot be tested. No session is marked as sham or as\ntFUS aimed at CG1. The auditory cortex units of Figure 11B are not split by type, and that claim is tested.\n\n| Claim | Tested here |\n|---|---|\n| fig4-unit-counts | Blocked: data missing (no cell types); totals per area shown |\n| fig4a-s1-rsu-time-locked-3000 | Blocked: data missing (no cell types) |\n| fig4b-pom-rsu-time-locked-3000 | Blocked: data missing (no cell types) |\n| fig4-postsonication-3000 | Blocked: data missing (no cell types) |\n| fig4-30hz-responses | Blocked: data missing (no cell types) |\n| fig4-fsu-no-change | Blocked: data missing (no cell types) |\n| fig5a-sham-no-change | Blocked: data missing (no cell types, no sham sessions marked) |\n| fig5b-cg1-control-no-change | Blocked: data missing (no cell types, no CG1 sessions marked) |\n| fig6-unit-counts | Blocked: data missing (no cell types); totals per area shown |\n| fig6a-s1-rsu-time-locked-prf, fig6a-s1-rsu-delayed-prf, fig6b-s1-fsu-prf, fig6c-pom-rsu-prf, fig6d-pom-fsu-prf | Blocked: data missing (no cell types) |\n| fig7a to fig7d, fig8a, fig8b, fig9a, fig9b (8 claims) | Blocked: data missing (no cell types) |\n| fig10a-dsttc-3000, fig10b-dsttc-30, fig10c to fig10f (6 claims) | Blocked: data missing (no cell types) |\n| pathway-follows-local-prf | Blocked: depends on fig6a and fig10c |\n| fig11b-ac-responses | Tested |\n| fig11c-ac-to-s1-30hz, fig11d-ac-to-s1-3000 | Blocked: data missing (no S1 cell types) |\n| auditory-confound-low-prf | Blocked: depends on fig11c and fig11d |\n\nNo step of the analysis is random, so no seed is needed.\n\"\"\")\n\ncode(r\"\"\"\nimport json\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\n\nimport tfus\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nstarted = time.time()\nprint(\"dandiset\", tfus.DANDISET_ID, \"version\", tfus.VERSION)\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEvery file of the pinned version is opened and its metadata, trial count and per-unit spike counts are\nread (not the spike times). Each check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nassets = tfus.list_assets()\nearly = tfus.list_assets(\"0.250711.1640\")\nsame = {(a[\"path\"], a[\"size\"]) for a in assets} == {(a[\"path\"], a[\"size\"]) for a in early}\nprint(f\"{len(assets)} files in {tfus.VERSION}; {len(early)} in 0.250711.1640; same paths and sizes: {same}\")\nt0 = time.time()\ninv = tfus.inventory(assets)\nprint(f\"read the headers of {len(inv)} files in {time.time() - t0:.0f} s; files that failed to open: \"\n      f\"{(inv.error != '').sum()}\")\ninv[\"kind\"] = np.where(inv.path.str.startswith(\"sub-STTC\"), \"STTC\", \"units\")\nprint(inv.kind.value_counts().to_string())\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\nu = inv[inv.kind == \"units\"].copy()\nprint(\"Columns of the units tables:\")\nprint(u.unit_columns.value_counts().to_string())\nprint(\"\\nNon-empty acquisition, analysis or processing groups (where waveforms could be):\",\n      int((u.groups != \"\").sum()), \"of\", len(u), \"files\")\nprint(\"\\nValues of celltype_label over all files (absent where the column is missing):\")\nprint(u.labels.value_counts().to_string())\nn_units_all = int(u.n_units.sum())\nprint(f\"\\n{n_units_all} units in {len(u)} unit files, before removing duplicate files\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe units tables hold only spike times and `celltype_label`. No file has waveforms, mean waveforms or\nanything under acquisition, analysis or processing, and `celltype_label` is 0 in every file where it is\npresent (it is missing from the rest), though its description says 1 is RSU and 2 is FSU. The RSU/FSU\nsplit of the paper cannot be made from these data.\n\"\"\")\n\ncode(r\"\"\"\nkept, dropped = tfus.dedupe(u)\nprint(f\"{len(u)} unit files; {len(dropped)} have the same subject, identifier, area and per-unit spike counts \"\n      f\"as another file; {len(kept)} distinct recordings remain\")\nprint(\"Files per group of duplicates:\", (dropped.kept.value_counts() + 1).value_counts().to_dict())\nids = dict(zip(u.path, u.asset_id))\nt0 = time.time()\nh_kept = dict(zip(dropped.kept.unique(), tfus.map_sessions(tfus.spike_hash, [ids[p] for p in dropped.kept.unique()])))\nh_drop = tfus.map_sessions(tfus.spike_hash, [ids[p] for p in dropped.dropped])\nident = sum(h_kept[k] == h for k, h in zip(dropped.kept, h_drop))\nprint(f\"duplicate files whose spike times and trial starts are identical to the kept file: {ident} of {len(dropped)} \"\n      f\"({time.time() - t0:.0f} s)\")\nst = u.set_index(\"path\").session_start\ngap = pd.Series([abs(pd.Timestamp(st[a]) - pd.Timestamp(st[b])).total_seconds()\n                 for a, b in zip(dropped.kept, dropped.dropped)])\nprint(\"session_start_time difference within a duplicate pair (s): median\", gap.median(), \"max\", gap.max())\nprint(dropped.head(6).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nMost recordings are deposited twice, under two session start times a few seconds to a minute apart, with\nidentical spike times and trial starts. Each recording is counted once from here on.\n\"\"\")\n\ncode(r\"\"\"\nk = kept.copy()\nprint(\"Distinct recordings by recorded area and tFUS target (from general/notes):\")\nprint(pd.crosstab(k.area.replace(\"\", \"(empty)\"), k.stim.replace(\"\", \"(empty)\"), margins=True).to_string())\nprint(\"\\nRats:\", k.subject_id.nunique(), sorted(k.subject_id.unique()))\ngroups = k.groupby(\"subject_id\").area.agg(lambda a: \",\".join(sorted(set(a) - {\"\"})))\nprint(\"\\nAreas recorded per rat:\")\nprint(groups.value_counts().to_string())\nprint(\"\\nRecordings without a PRF or PD in general/data_collection:\")\nprint(k[k.prf.isna() | k.pd_us.isna()][[\"path\", \"identifier\", \"notes\", \"data_collection\"]].to_string(index=False))\nprint(\"\\nIdentifier suffixes after <rat>_<PRF>_<PD>_<UD>_<n>:\")\nprint(k.identifier.str.split(\"_\").str[5:].str.join(\"_\").replace(\"\", \"(none)\").value_counts().to_string())\nprint(\"\\nAny identifier, note or data_collection naming sham, no tFUS, CG1 or cingulate:\",\n      int(k[[\"identifier\", \"notes\", \"data_collection\"]].apply(\n          lambda c: c.str.contains(\"(?i)sham|cg1|cingul|no tfus|control\")).any(axis=1).sum()))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe paper used 16 rats with S1 and POm probes and 12 with S1 and AC probes (Methods, Animal preparation).\nThe dataset has 10 rats with POm recordings and 7 with AC recordings (one more rat, BH500, has recordings\nwhose area is left empty, and BH594 has a single S1 file). It also holds recordings of M1, and sessions\nwith tFUS aimed at M1 or at POm, which the paper does not describe. Every recording lists a PRF and PD\nexcept two of BH500, and none is marked as sham or as aimed at CG1, so the sham and control sessions of\nFigure 5 cannot be found.\n\"\"\")\n\ncode(r\"\"\"\nk[\"n_trials\"] = k.n_trials.astype(int)\nprint(\"Trials per recording:\", k.n_trials.describe()[[\"min\", \"50%\", \"max\"]].to_dict(),\n      \"; recordings with 500 trials:\", int((k.n_trials == 500).sum()), \"of\", len(k))\ns1 = k[(k.stim == \"S1\") & (k.pd_us == 200) & k.area.isin([\"S1\", \"POM\", \"AC\"])].copy()\nprint(\"\\nPD 200 us recordings with tFUS aimed at S1, by area and PRF (Hz):\")\nprint(pd.crosstab(s1.area, s1.prf).to_string())\nt0 = time.time()\nres = tfus.map_sessions(tfus.session_counts, list(s1.asset_id))\ns1[\"res\"] = res\nprint(f\"\\nloaded spike times of {len(s1)} recordings in {time.time() - t0:.0f} s\")\niti = np.concatenate([np.diff(r[\"start\"]) for r in res])\nprint(\"Interval between trial starts (s): min %.3f, median %.3f, max %.3f; paper 2.5 s with 10%% jitter\"\n      % (iti.min(), np.median(iti), iti.max()))\ndur = np.concatenate([np.asarray(tfus.load_session(s1.asset_id.iloc[0])[\"stop\"]) - s1.res.iloc[0][\"start\"]])\nprint(\"Trial stop minus start in one recording (s):\", np.unique(np.round(dur, 3)))\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Are the two areas of a session recorded together? Compare the trial starts of files that share an identifier.\nrows = []\nfor ident, g in s1.groupby(\"identifier\"):\n    if len(g) < 2:\n        continue\n    starts = [r[\"start\"] for r in g.res]\n    a, b = starts[0], starts[1]\n    same_n = len(a) == len(b)\n    rows.append(dict(identifier=ident, areas=\"+\".join(g.area), n=(len(a), len(b)),\n                     same_times=bool(same_n and np.allclose(a, b, atol=1e-3)),\n                     same_intervals=bool(same_n and np.allclose(np.diff(a), np.diff(b), atol=1e-3))))\npairs = pd.DataFrame(rows)\nprint(f\"{len(pairs)} identifiers with two areas; same trial start times: {pairs.same_times.sum()}; \"\n      f\"same intervals between trials: {pairs.same_intervals.sum()}\")\nprint(pairs[~pairs.same_intervals].head(10).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n### Clock check\n\n`start_time` of the trials table is taken as sonication onset. If it is, the units' firing should change\nat fixed delays after it; with the trial starts shifted by 1 s (inside the 2.25 s minimum interval, where\nno tFUS is delivered), the same measure should show no change. The measure is the mean over units of the\nnormalized rate (reading N1) in each 67 ms window, for every unit with more than 2000 spikes.\n\"\"\")\n\ncode(r\"\"\"\ndef unit_table(frame, min_spikes=tfus.MIN_SPIKES):\n    rows = []\n    for _, r in frame.iterrows():\n        res = r[\"res\"]\n        for c, cs, ps in zip(res[\"true\"], res[\"shifted\"], res[\"psth\"]):\n            if c[\"n_spikes\"] <= min_spikes:\n                continue\n            rows.append(dict(subject=r.subject_id, identifier=r.identifier, area=r.area, prf=r.prf,\n                             true=c, shifted=cs, psth=ps))\n    return pd.DataFrame(rows)\n\n\nunits = unit_table(s1)\nprint(\"Units with more than 2000 spikes, PD 200 us, tFUS at S1:\")\nprint(pd.crosstab(units.area, units.prf, margins=True).to_string())\nrows = []\nfor (area, prf), g in units.groupby([\"area\", \"prf\"]):\n    for align in [\"true\", \"shifted\"]:\n        vals = {w: np.nanmean([tfus.normalized_rates(c, w, \"N1\") for c in g[align]]) for w in tfus.WINDOWS}\n        rows.append(dict(area=area, prf=prf, onsets=align, n=len(g), **{k: round(v, 1) for k, v in vals.items()}))\nclock = pd.DataFrame(rows)\nprint(\"\\nMean normalized rate (%) by window, at the trial starts and 1 s later:\")\nprint(clock.to_string(index=False))\ndev = clock.assign(dev=clock[list(tfus.WINDOWS)].sub(100).abs().max(axis=1)).groupby(\"onsets\").dev.median()\nprint(\"\\nMedian over area and PRF of the largest departure from 100%:\", dev.round(1).to_dict())\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\ncenters = (tfus.PSTH_EDGES[:-1] + tfus.PSTH_EDGES[1:]) / 2 * 1000\nfig, axes = plt.subplots(1, 3, figsize=(15, 3.5), sharex=True)\nfor ax, area in zip(axes, [\"S1\", \"POM\", \"AC\"]):\n    for prf, g in units[units.area == area].groupby(\"prf\"):\n        m = np.mean(np.vstack(g.psth), axis=0) / 0.01\n        ax.plot(centers, m, label=f\"{int(prf)} Hz (n={len(g)})\")\n        print(f\"{area} {int(prf)} Hz: mean rate {m.min():.1f} to {m.max():.1f} spikes/s; \"\n              f\"[-500, 0) ms mean {m[centers < 0].mean():.1f}, [0, 300) ms max {m[(centers > 0) & (centers < 300)].max():.1f}\")\n    ax.axvspan(0, 67, color=\"0.9\")\n    ax.set_title(f\"{area}, PD 200 us\")\n    ax.set_xlabel(\"time from trial start (ms)\")\naxes[0].set_ylabel(\"mean rate (spikes/s)\")\naxes[-1].legend(fontsize=7)\nplt.tight_layout()\nplt.show()\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe rates change after the trial start and not 1 s later (the table above gives both), so the trial start\ntimes share the clock of the spike times and mark the stimulus, as the dataset's description says\n(\"intervals contains each tFUS trial start and end timestamps\"). That `start_time` is the onset of\nsonication itself, and not a trigger at a fixed delay, is consistent with the data (the firing changes\nwithin the first 67 ms window at the high PRFs) but not shown. The intervals between trial starts match\nthe paper's 2.5 s with 10% jitter. Within a session, the files of the two areas carry the trial starts\ncounted above.\n\"\"\")\n\nmd(r\"\"\"\n### Unit totals for the count claims\n\n`fig4-unit-counts` and `fig6-unit-counts` give RSU and FSU counts, which need the cell types. The totals\nper area (units with more than 2000 spikes, distinct recordings, tFUS at S1, PD 200 us) are shown here\nto say what the dataset holds; they decide no outcome. S1 is counted two ways: every S1 recording, and only\nthe S1 recordings whose identifier also has a POm recording (the S1 and POm rats of Figure 4).\n\"\"\")\n\ncode(r\"\"\"\ndef n_above(row, min_spikes=tfus.MIN_SPIKES):\n    return int(sum(n > min_spikes for n in json.loads(row)))\n\n\nk[\"n_good\"] = k.n_spikes.map(n_above)\npd200 = k[(k.stim == \"S1\") & (k.pd_us == 200)]\npom_ids = set(pd200[pd200.area == \"POM\"].identifier)\npom_rats = set(pd200[pd200.area == \"POM\"].subject_id)\ntab = []\nfor prf in [30, 300, 1500, 3000, 4500]:\n    g = pd200[pd200.prf == prf]\n    tab.append(dict(prf=prf,\n                    S1_all=int(g[g.area == \"S1\"].n_good.sum()),\n                    S1_in_POm_rats=int(g[(g.area == \"S1\") & g.subject_id.isin(pom_rats)].n_good.sum()),\n                    S1_paired_with_POm=int(g[(g.area == \"S1\") & g.identifier.isin(pom_ids)].n_good.sum()),\n                    POm=int(g[g.area == \"POM\"].n_good.sum()), AC=int(g[g.area == \"AC\"].n_good.sum())))\ntab = pd.DataFrame(tab)\ntab.loc[\"total\"] = tab.sum()\ntab.loc[\"total\", \"prf\"] = \"all\"\nprint(tab.to_string())\nprint(\"\\nPaper (Fig. 4 legend), RSU + FSU: S1 3000 Hz 366, POm 3000 Hz 250, S1 30 Hz 209, POm 30 Hz 232;\"\n      \" Fig. 6 legend: S1 1297, POm 1019 over the five PRFs; Fig. 11: AC 453.\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\n### The STTC files\n\nThe 370 files under `sub-STTC-*` hold STTC values between the units of two areas. They are listed here\nbecause the claims file names them as a variant for Figure 10; they carry no unit identities or cell\ntypes.\n\"\"\")\n\ncode(r\"\"\"\nsttc = inv[inv.kind == \"STTC\"]\nprint(sttc.notes.value_counts().to_string())\nimport h5py, remfile\nf = h5py.File(remfile.File(tfus.asset_url(sttc.asset_id.iloc[0])), \"r\")\nprint(\"\\n\", sttc.path.iloc[0], f[\"identifier\"][()].decode(), f[\"general/notes\"][()].decode())\nprint(f[\"units\"].attrs[\"description\"])\nfor c in [\"STTC\", \"STTCAtoB\", \"STTCBtoA\", \"STTCA\", \"STTCB\"]:\n    print(c, f[\"units\"][c].shape, \"|\", f[\"units\"][c].attrs[\"description\"])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe STTC arrays do not have the shape their descriptions give: the description lists nine values of dt\nand two unit dimensions, while `STTC` has three dimensions (10 time windows, trials, and one other) and\nno dt dimension. Which dt and which units the values belong to is not stated, and no unit is typed, so the\nstored values cannot stand in for the STTC between S1 RSUs and POm RSUs of Figure 10.\n\n## Untyped responses in S1 and POm (a variant; decides no outcome)\n\nThe claims on S1 and POm need the RSU/FSU split. For orientation only, the same measure on all units of\neach area, without typing (reading N1, comparison B1, Bonferroni over the five PRFs):\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor area in [\"S1\", \"POM\"]:\n    for prf, g in units[units.area == area].groupby(\"prf\"):\n        base = tfus.baseline_sample(list(g[\"true\"]), \"N1\", \"B1\")\n        r = dict(area=area, prf=int(prf), n=len(g))\n        for w in tfus.WINDOWS:\n            x = np.array([tfus.normalized_rates(c, w, \"N1\") for c in g[\"true\"]])\n            p_up, _ = tfus.vs_baseline(x, base, 5, \"greater\")\n            p_dn, _ = tfus.vs_baseline(x, base, 5, \"less\")\n            r[w] = f\"{np.nanmean(x):.0f}{'+' if p_up < 0.01 else ('-' if p_dn < 0.01 else '')}\"\n        rows.append(r)\nprint(\"Mean normalized rate (%) of all units; + above, - below baseline at corrected p < 0.01:\")\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\")\n\nmd(r\"\"\"\n## fig11b-ac-responses\n\n> AC neurons in the S1-AC rats show time-locked responses to 1500 and 3000 Hz PRF and postsonication\n> responses to 30, 1500, 3000 and 4500 Hz, both PRF dependent, least at 300 Hz.\n\nCriterion (claims file): the header's spiking method on all AC units with more than 2000 spikes in the PRF\nseries with 200 us PD; windows 0 to 67 and 201 to 268 ms (the 67 to 134 and 134 to 201 ms bins shown).\nReproduced when, under every method reading, both Kruskal-Wallis tests have p < 0.01, exactly 1500 and\n3000 Hz are above baseline during sonication, exactly 30, 1500, 3000 and 4500 Hz are above baseline\npostsonication, and 300 Hz has the lowest mean normalized rate in at least one window; partially\nreproduced when the sets differ by one PRF in one window or the 300 Hz part fails. Expected: 453 AC\nneurons over the five PRFs.\n\nThe method readings (claims file header): N1 or N2 for the normalized rate; B1 or B2 for the baseline\nsample; the Bonferroni factor is the five PRF levels of the panel (C1; C2 applies only to a panel with a\nsingle comparison, so it is the same here). B3, a paired signed-rank test, is shown as a variant.\n\"\"\")\n\ncode(r\"\"\"\nac = units[units.area == \"AC\"].copy()\nPRFS = [30.0, 300.0, 1500.0, 3000.0, 4500.0]\nprint(\"AC units with more than 2000 spikes, by rat and PRF:\")\nprint(pd.crosstab(ac.subject, ac.prf, margins=True).to_string())\nprint(f\"\\nTotal {len(ac)} (expected 453 +/- 45.3)\")\nallac = s1[s1.area == \"AC\"]\nprint(\"AC recordings used:\", len(allac), \"; units in them before the 2000-spike rule:\",\n      int(sum(r[\"n_units\"] for r in allac.res)))\n\"\"\", tags=[\"claim:fig11b-ac-responses\"])\n\ncode(r\"\"\"\ndef evaluate(frame, nreading, breading, min_label=\"\"):\n    out, sig = [], {}\n    for w in tfus.WINDOWS:\n        groups, line = [], {}\n        for p in PRFS:\n            cs = list(frame[frame.prf == p][\"true\"])\n            x = np.array([tfus.normalized_rates(c, w, nreading) for c in cs])\n            groups.append(x)\n            if breading == \"B3\":\n                from scipy import stats as st\n                win = np.array([c[w].mean() for c in cs]); bas = np.array([c[\"base\"].mean() for c in cs])\n                pr = st.wilcoxon(win, bas, alternative=\"greater\").pvalue\n                pc = min(1, pr * 5)\n            else:\n                base = tfus.baseline_sample(cs, nreading, breading)\n                pc, pr = tfus.vs_baseline(x, base, 5, \"greater\")\n            sem = np.nanstd(x, ddof=1) / np.sqrt(np.isfinite(x).sum())\n            out.append(dict(N=nreading, B=breading, window=w, prf=int(p), n=int(np.isfinite(x).sum()),\n                            mean=round(np.nanmean(x), 1), sem=round(sem, 1), median=round(np.nanmedian(x), 1),\n                            p_corrected=float(f\"{pc:.3g}\"), above=pc < 0.01))\n        kw = tfus.kruskal_levels(groups)\n        for o in out[-5:]:\n            o[\"kruskal_p\"] = float(f\"{kw:.3g}\")\n    return pd.DataFrame(out)\n\n\ndef judge(t):\n    def sset(w):\n        return {r.prf for r in t[(t.window == w) & t.above].itertuples()}\n    during, post = sset(\"0-67\"), sset(\"201-268\")\n    kw_ok = (t[t.window == \"0-67\"].kruskal_p.iloc[0] < 0.01) and (t[t.window == \"201-268\"].kruskal_p.iloc[0] < 0.01)\n    d_err = len(during ^ {1500, 3000})\n    p_err = len(post ^ {30, 1500, 3000, 4500})\n    low = [t[t.window == w].sort_values(\"mean\").prf.iloc[0] for w in [\"0-67\", \"201-268\"]]\n    low300 = 300 in low\n    if kw_ok and d_err == 0 and p_err == 0 and low300:\n        verdict = \"reproduced\"\n    elif kw_ok and ((d_err + p_err == 1 and low300) or (d_err == 0 and p_err == 0 and not low300)):\n        verdict = \"partially reproduced\"\n    else:\n        verdict = \"not reproduced\"\n    return dict(kruskal_both=kw_ok, during=sorted(during), post=sorted(post), lowest_0_67=low[0],\n                lowest_201_268=low[1], verdict=verdict)\n\n\ntables, verdicts = {}, []\nfor N in [\"N1\", \"N2\"]:\n    for B in [\"B1\", \"B2\"]:\n        t = evaluate(ac, N, B)\n        tables[(N, B)] = t\n        verdicts.append(dict(N=N, B=B, **judge(t)))\nt_b3 = evaluate(ac, \"N1\", \"B3\")\nverdicts.append(dict(N=\"raw rates\", B=\"B3 (variant)\", **judge(t_b3)))\nprint(\"Outcome under each reading (sets are the PRFs above baseline at corrected p < 0.01):\")\nprint(pd.DataFrame(verdicts).to_string(index=False))\n\"\"\", tags=[\"claim:fig11b-ac-responses\"])\n\ncode(r\"\"\"\nfor (N, B), t in tables.items():\n    print(f\"\\nReading {N}, {B}: mean, SEM and median normalized rate (%), corrected p against baseline, Kruskal-Wallis p\")\n    print(t.pivot_table(index=\"prf\", columns=\"window\", values=[\"mean\", \"p_corrected\"], sort=False)\n          .reindex(columns=list(tfus.WINDOWS), level=1).to_string())\n    print(\"Kruskal-Wallis p by window:\", t.groupby(\"window\", sort=False).kruskal_p.first().to_dict())\nprint(\"\\nVariant B3 (paired signed-rank of raw rates against [-67, 0) ms), corrected p:\")\nprint(t_b3.pivot_table(index=\"prf\", columns=\"window\", values=\"p_corrected\", sort=False).to_string())\n\"\"\", tags=[\"claim:fig11b-ac-responses\"])\n\nmd(r\"\"\"\nThe two normalizations differ in kind. N2 averages per-trial ratios over the trials with a nonzero\nbaseline count; at these firing rates most 67 ms baselines hold no spike, and keeping only the trials with\none makes the baseline larger than average, so N2 sits below 100% even where nothing happens. The next\ncell measures this at the trial starts shifted by 1 s, where there is no stimulus.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor N in [\"N1\", \"N2\"]:\n    for w in tfus.WINDOWS:\n        x = np.array([tfus.normalized_rates(c, w, N) for c in ac[\"shifted\"]])\n        rows.append(dict(N=N, window=w, mean_at_shifted_onsets=round(np.nanmean(x), 1),\n                         median=round(np.nanmedian(x), 1)))\nprint(\"AC units, normalized rate (%) with trial starts shifted by 1 s (no stimulus):\")\nprint(pd.DataFrame(rows).pivot(index=\"N\", columns=\"window\", values=\"mean_at_shifted_onsets\")\n      [list(tfus.WINDOWS)].to_string())\nnz = np.array([np.mean(c[\"base\"] > 0) for c in ac[\"true\"]])\nprint(f\"\\nFraction of trials with a nonzero [-67, 0) ms count, over AC units: median {np.median(nz):.2f}, \"\n      f\"range {nz.min():.2f} to {nz.max():.2f}\")\n\"\"\", tags=[\"claim:fig11b-ac-responses\"])\n\ncode(r\"\"\"\n# By rat: mean normalized rate (N1) in the two windows of the criterion\nrows = []\nfor (sub, prf), g in ac.groupby([\"subject\", \"prf\"]):\n    r = dict(rat=sub, prf=int(prf), n=len(g))\n    for w in [\"0-67\", \"201-268\"]:\n        r[w] = round(np.nanmean([tfus.normalized_rates(c, w, \"N1\") for c in g[\"true\"]]), 1)\n    rows.append(r)\nprint(\"Mean normalized rate (%) by rat, reading N1:\")\nprint(pd.DataFrame(rows).to_string(index=False))\n\n# The 2000-spike rule: how the count and the result change with it\nrows = []\nfor m in [1000, 2000, 4000, 8000]:\n    sub = unit_table(s1[s1.area == \"AC\"], min_spikes=m)\n    j = judge(evaluate(sub, \"N1\", \"B1\"))\n    rows.append(dict(min_spikes=m, n_units=len(sub), during=j[\"during\"], post=j[\"post\"],\n                     lowest=(j[\"lowest_0_67\"], j[\"lowest_201_268\"]), verdict=j[\"verdict\"]))\nprint(\"\\nReading N1, B1 under other spike-count rules (the paper's is more than 2000):\")\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"claim:fig11b-ac-responses\"])\n\ncode(r\"\"\"\nt = tables[(\"N1\", \"B1\")]\nfig, ax = plt.subplots(figsize=(7, 3.5))\nfor p in PRFS:\n    q = t[t.prf == int(p)]\n    ax.errorbar(range(4), q[\"mean\"], yerr=q[\"sem\"], marker=\"o\", label=f\"{int(p)} Hz\", capsize=3)\nax.axhline(100, color=\"0.5\", lw=0.8)\nax.set_xticks(range(4))\nax.set_xticklabels([f\"{w} ms\" for w in tfus.WINDOWS])\nax.set_ylabel(\"normalized rate (%), mean +/- SEM\")\nax.set_title(\"AC units, PD 200 us, reading N1\")\nax.legend(fontsize=7)\nplt.tight_layout()\nplt.show()\nprint(\"Plotted means range from\", t[\"mean\"].min(), \"to\", t[\"mean\"].max(), \"%; none outside the axes.\")\n\"\"\", tags=[\"claim:fig11b-ac-responses\"])\n\nmd(r\"\"\"\n**Result: partially reproduced, resting on the assumption of reading N1 with baseline B1.** Under N1 and\nB1 both Kruskal-Wallis tests have p < 0.01, the postsonication set (201 to 268 ms) is exactly 30, 1500,\n3000 and 4500 Hz, and 300 Hz has the lowest mean in both windows, but during sonication 4500 Hz is also\nabove baseline besides 1500 and 3000 Hz, so the time-locked set differs by one PRF. With B2 the\ntime-locked set also gains 300 Hz, and under N2 no or almost no PRF is above baseline; N2 sits below 100%\neven with no stimulus (shifted trial starts), so it cannot give the paper's normalization to the 67 ms\nbefore stimulation, and N1 with the paper's own baseline window (B1) is adopted. The dataset gives 633 AC\nunits with more than 2000 spikes, against the paper's 453, from 6 rats where the paper had 12; the counts\nare higher at every PRF.\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| fig11b-ac-responses | Partially reproduced (assumed: normalization N1, baseline B1) |\n| fig4-unit-counts, fig6-unit-counts | Blocked: data missing (cell types) |\n| fig4a, fig4b, fig4-postsonication-3000, fig4-30hz-responses, fig4-fsu-no-change | Blocked: data missing (cell types) |\n| fig5a-sham-no-change, fig5b-cg1-control-no-change | Blocked: data missing (cell types; no sham or CG1 sessions marked) |\n| fig6a (2 claims), fig6b, fig6c, fig6d | Blocked: data missing (cell types) |\n| fig7a to fig7d, fig8a, fig8b, fig9a, fig9b | Blocked: data missing (cell types) |\n| fig10a to fig10f | Blocked: data missing (cell types) |\n| pathway-follows-local-prf | Blocked: depends on blocked claims |\n| fig11c-ac-to-s1-30hz, fig11d-ac-to-s1-3000 | Blocked: data missing (S1 cell types) |\n| auditory-confound-low-prf | Blocked: depends on blocked claims |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the\ndifferences from the paper's method.\n\nHow the analysis differs from the paper's: the normalization and the baseline sample are not fixed by the\npaper; reading N1 with baseline B1 is adopted and the others are shown. Duplicate files are counted once.\n\nWhat was found about the dataset: no spike waveforms and no cell types (`celltype_label` is 0 for every\nunit, though described as 1 = RSU and 2 = FSU), so 31 of the 33 claims cannot be tested; most recordings\nare deposited twice; the sham and CG1 sessions cannot be identified; the dataset holds 10 of the 16 S1-POm\nrats and 7 of the 12 S1-AC rats, together with M1 recordings and tFUS aimed at M1 or POm that the paper\ndoes not describe; the STTC files lack the dt dimension their descriptions give and identify no units.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"notebook ran in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, \"entries/000946-gao-2025/reproduce_gao_2025.ipynb\")\nprint(\"written\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude/gen_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . env/bin/activate && uv pip install -q nbconvert ipykernel nbformat 2>&1|tail -1; python /tmp/claude/gen_nb.py && cd entries/000946-gao-2025 && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_gao_2025.ipynb --output $TMPDIR/exec.ipynb 2>&1 | tail -5
```

```
Sat Oct 31 23:25:57 UTC 2026
written 33
[32m    489[39m         [33m"[39m[33mhttps://github.com/pandas-dev/pandas/issues.[39m[33m"[39m
[32m    490[39m     )

[31mTypeError[39m: Invalid value 'all' for dtype 'int64'


real	4m11.045s
user	5m21.945s
sys	0m24.685s
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
p='gen_nb.py'; s=open(p).read()
s=s.replace('''tab = pd.DataFrame(tab)
tab.loc["total"] = tab.sum()
tab.loc["total", "prf"] = "all"''','''tab = pd.DataFrame(tab).set_index("prf")
tab.loc["all PRFs"] = tab.sum()''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('exec.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(o['text'][:3500])
        print('-----')
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/nbformat/__init__.py", line 171, in read
    with open(fp, encoding="utf8") as f:  # noqa: PTH123
         ~~~~^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'exec.ipynb'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python /tmp/claude/gen_nb.py && cd entries/000946-gao-2025 && jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 reproduce_gao_2025.ipynb --output $TMPDIR/exec.ipynb 2>&1 | tail -1; cd $TMPDIR && python - <<'EOF'
import nbformat
nb=nbformat.read(open('exec.ipynb'),4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(o['text'][:4000])
            if o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
        print('-----')
EOF
```

```
written 33
[NbConvertApp] Writing 381294 bytes to /tmp/claude-1001/exec.ipynb
dandiset 000946 version 0.250829.1249

-----
1920 files in 0.250829.1249; 1920 in 0.250711.1640; same paths and sizes: True

read the headers of 1920 files in 105 s; files that failed to open: 0
kind
units    1550
STTC      370

-----
Columns of the units tables:
unit_columns
spike_times,celltype_label    1516
spike_times                     34

Non-empty acquisition, analysis or processing groups (where waveforms could be): 0 of 1550 files

[... 341 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/000946-gao-2025 && python - <<'EOF'
p='tfus.py'; s=open(p).read()
s=s.replace('''def parse_header(identifier, notes, data_collection):
    """Area, target, PRF (Hz) and PD (us) from the file's text fields."""''','''def parse_identifier(identifier):
    """PRF (Hz) and PD (us) from the identifier `<rat>_<PRF>_<PD>_<UD>_...`."""
    parts = identifier.split("_")
    try:
        return float(parts[1]), float(parts[2].replace("point", "."))
    except (IndexError, ValueError):
        return np.nan, np.nan


def parse_header(identifier, notes, data_collection):
    """Area, target, PRF (Hz) and PD (us) from the file's text fields (PRF and PD from data_collection;
    the notebook compares them with the identifier and falls back on it where data_collection is empty)."""''')
s=s.replace('''        r["area"], r["stim"], r["prf"], r["pd_us"] = parse_header(r["identifier"], r["notes"], r["data_collection"])''','''        r["area"], r["stim"], r["prf_dc"], r["pd_dc"] = parse_header(r["identifier"], r["notes"], r["data_collection"])
        r["prf_id"], r["pd_id"] = parse_identifier(r["identifier"])
        r["prf"] = r["prf_dc"] if np.isfinite(r["prf_dc"]) else r["prf_id"]
        r["pd_us"] = r["pd_dc"] if np.isfinite(r["pd_dc"]) else r["pd_id"]''')
open(p,'w').write(s)
EOF
cd /tmp/claude && python - <<'EOF'
p='gen_nb.py'; s=open(p).read()
old_start=s.index('print("\\nRecordings without a PRF or PD in general/data_collection:")')
old_end=s.index('print("\\nIdentifier suffixes')
s=s[:old_start]+'''nodc = k.prf_dc.isna() | k.pd_dc.isna()
print("\\nRecordings without a PRF or PD in general/data_collection:", int(nodc.sum()), "of", len(k), "; by rat:",
      k[nodc].subject_id.value_counts().to_dict())
both = ~nodc & k.prf_id.notna()
agree = (k.prf_dc[both] == k.prf_id[both]) & (np.isclose(k.pd_dc[both], k.pd_id[both]))
print("Recordings where data_collection and the identifier both give PRF and PD:", int(both.sum()),
      "; they agree in", int(agree.sum()))
print(k[both][~agree][["identifier", "data_collection"]].to_string(index=False))
print("Recordings with no PRF or PD in either field:", int((k.prf.isna() | k.pd_us.isna()).sum()),
      k[k.prf.isna() | k.pd_us.isna()].identifier.tolist())
'''+s[old_end:]
s=s.replace('''The paper used 16 rats with S1 and POm probes and 12 with S1 and AC probes (Methods, Animal preparation).
The dataset has 10 rats with POm recordings and 7 with AC recordings (one more rat, BH500, has recordings
whose area is left empty, and BH594 has a single S1 file). It also holds recordings of M1, and sessions
with tFUS aimed at M1 or at POm, which the paper does not describe. Every recording lists a PRF and PD
except two of BH500, and none is marked as sham or as aimed at CG1, so the sham and control sessions of
Figure 5 cannot be found.''','''The paper used 16 rats with S1 and POm probes and 12 with S1 and AC probes (Methods, Animal preparation).
The dataset has 20 rats: 10 with POm recordings and 7 with AC recordings; of the other three, BH494 has S1
and M1, BH500 has S1, M1 and recordings whose area is left empty, and BH594 has a single S1 file. It also
holds recordings of M1, and sessions with tFUS aimed at M1 or at POm, which the paper does not describe.
The PRF and PD are taken from `general/data_collection`, and from the identifier where that field is empty
(the counts above say where, and whether the two agree where both are given). None is marked as sham or
as aimed at CG1, so the sham and control sessions of Figure 5 cannot be found.''')
s=s.replace('''print(f"{len(pairs)} identifiers with two areas; same trial start times: {pairs.same_times.sum()}; "
      f"same intervals between trials: {pairs.same_intervals.sum()}")''','''print(f"{len(pairs)} identifiers with two areas; same trial start times: {pairs.same_times.sum()}; "
      f"same intervals between trials: {pairs.same_intervals.sum()}")
dstart = []
for ident, g in s1.groupby("identifier"):
    if len(g) == 2:
        a, b = (pd.Timestamp(x) for x in g.session_start)
        dstart.append(abs(a - b).total_seconds() / 60)
print("session_start_time difference between the two area files of a session (min): median %.1f, max %.1f"
      % (np.median(dstart), np.max(dstart)))''')
s=s.replace('''the paper's 2.5 s with 10% jitter. Within a session, the files of the two areas carry the trial starts
counted above.''','''the paper's 2.5 s with 10% jitter. In every session with files from two areas, both files carry the same
trial start times, so the two areas were recorded together on one clock (the description says "Each
recording contains two areas"), though their `session_start_time` values differ (by the minutes printed
above), so that field does not give the start of the recording.''')
s=s.replace('''The STTC arrays do not have the shape their descriptions give: the description lists nine values of dt
and two unit dimensions, while `STTC` has three dimensions (10 time windows, trials, and one other) and
no dt dimension. Which dt and which units the values belong to is not stated, and no unit is typed, so the
stored values cannot stand in for the STTC between S1 RSUs and POm RSUs of Figure 10.''','''The STTC arrays do not have the shape their descriptions give: the descriptions list a dimension for the
nine values of dt, while the arrays have the 10 time windows, the trials and the units of the two areas,
and no dt dimension. Which dt the values were computed with is not stated, and no unit is typed, so the
stored values cannot stand in for the STTC between S1 RSUs and POm RSUs of Figure 10.''')
open(p,'w').write(s)
EOF
grep -n "nodc\|dstart" /tmp/claude/gen_nb.py | head
```

```
Sat Oct 31 23:35:02 UTC 2026
153:nodc = k.prf_dc.isna() | k.pd_dc.isna()
154:print("\nRecordings without a PRF or PD in general/data_collection:", int(nodc.sum()), "of", len(k), "; by rat:",
155:      k[nodc].subject_id.value_counts().to_dict())
156:both = ~nodc & k.prf_id.notna()
213:dstart = []
217:        dstart.append(abs(a - b).total_seconds() / 60)
219:      % (np.median(dstart), np.max(dstart)))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'EOF'
p='gen_nb.py'; s=open(p).read()
a=s.index('**Result: partially reproduced'); b=s.index('""")',a)
s=s[:a]+'''**Result: partially reproduced, resting on the assumption of reading N1 with baseline B1.** Under N1 and
B1 both Kruskal-Wallis tests have p < 0.01 (7.83e-06 during sonication, 5.16e-49 at 201 to 268 ms), the
postsonication set is exactly 30, 1500, 3000 and 4500 Hz, and 300 Hz has the lowest mean in both windows
(99.7% and 94.3%), but during sonication 4500 Hz is also above baseline (108.0%, corrected p = 7.05e-05)
besides 1500 Hz (140.3%) and 3000 Hz (107.1%), so the time-locked set differs by one PRF. The readings
disagree: with B2 the time-locked set also gains 300 Hz (not reproduced), and under N2 the Kruskal-Wallis
test during sonication has p = 0.0213 and at most one PRF per window is above baseline (not reproduced).
N2 gives 49.8% to 61.7% with no stimulus (trial starts shifted by 1 s), where N1 gives 94.3% to 99.0%, so N2
cannot give a rate normalized to the 67 ms before stimulation, and N1 with the paper's own pre-stimulus
window as the baseline (B1) is adopted. The variant B3 gives the same sets as N1 with B1. The result holds
for spike-count rules from 1000 to 8000 spikes. The dataset gives 633 AC units with more than 2000 spikes
(expected 453 +/- 45.3), from 6 rats, more than the paper at every PRF.
'''+s[b:]
s=s.replace('''unit, though described as 1 = RSU and 2 = FSU), so 31 of the 33 claims cannot be tested; most recordings
are deposited twice; the sham and CG1 sessions cannot be identified; the dataset holds 10 of the 16 S1-POm
rats and 7 of the 12 S1-AC rats, together with M1 recordings and tFUS aimed at M1 or POm that the paper
does not describe; the STTC files lack the dt dimension their descriptions give and identify no units.''','''unit, though described as 1 = RSU and 2 = FSU), so 32 of the 33 claims cannot be tested; most recordings
are deposited twice; the sham and CG1 sessions cannot be identified; the dataset has 10 rats with POm
recordings and 7 with AC recordings, where the paper reports 16 and 12, together with M1 recordings and
tFUS aimed at M1 or POm that the paper does not describe; `session_start_time` differs between the two area
files of one session; the STTC files lack the dt dimension their descriptions give and identify no units.''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python /tmp/claude/gen_nb.py && cd entries/000946-gao-2025 && jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 reproduce_gao_2025.ipynb --output $TMPDIR/exec.ipynb 2>&1 | tail -1; cd $TMPDIR && python - <<'EOF'
import nbformat
nb=nbformat.read(open('exec.ipynb'),4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code' and i in (5,6,8,9,10,14,19,20,21,23):
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(i,o['text'][:2500])
            if o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='error': print(i,'ERROR',o['ename'],o['evalue'])
EOF
```

```
written 33
[NbConvertApp] Writing 378915 bytes to /tmp/claude-1001/exec.ipynb
6 1550 unit files; 734 have the same subject, identifier, area and per-unit spike counts as another file; 816 distinct recordings remain
Files per group of duplicates: {2: 730, 3: 2}

6 duplicate files whose spike times and trial starts are identical to the kept file: 734 of 734 (106 s)
session_start_time difference within a duplicate pair (s): median 0.0 max 57.0
                                               kept                                             dropped
sub-BH494/sub-BH494_ses-20230817T132800_ecephys.nwb sub-BH494/sub-BH494_ses-20230817T132836_ecephys.nwb
sub-BH494/sub-BH494_ses-20230820T123700_ecephys.nwb sub-BH494/sub-BH494_ses-20230820T123756_ecephys.nwb
sub-BH494/sub-BH494_ses-20230820T125000_ecephys.nwb sub-BH494/sub-BH494_ses-20230820T125042_ecephys.nwb
sub-BH494/sub-BH494_ses-20230820T131000_ecephys.nwb sub-BH494/sub-BH494_ses-20230820T131032_ecephys.nwb
sub-BH494/sub-BH494_ses-20230820T144500_ecephys.nwb sub-BH494/sub-BH494_ses-20230820T144522_ecephys.nwb
sub-BH494/sub-BH494_ses-20230820T145800_ecephys.nwb sub-BH494/sub-BH494_ses-20230820T145857_ecephys.nwb

8 Distinct recordings by recorded area and tFUS target (from general/notes):
stim      M1  POM   S1  All
area                       
(empty)    2    0    3    5
AC         0    0  152  152
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read(open('exec.ipynb'),4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code' and i in (11,12,17,24,28,30):
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(i,o['text'][:2500])
EOF
```

```
11 60 identifiers with two areas; same trial start times: 60; same intervals between trials: 60
session_start_time difference between the two area files of a session (min): median 15.5, max 3964.0
Empty DataFrame
Columns: [identifier, areas, n, same_times, same_intervals]
Index: []

17           S1_all  S1_in_POm_rats  S1_paired_with_POm   POm   AC
prf                                                            
30           530             390                 213   315  112
300          388             293                 141   267   89
1500         493             327                 174   246  138
3000         572             383                 234   352  167
4500         431             333                 224   290  127
all PRFs    2414            1726                 986  1470  633

Paper (Fig. 4 legend), RSU + FSU: S1 3000 Hz 366, POm 3000 Hz 250, S1 30 Hz 209, POm 30 Hz 232; Fig. 6 legend: S1 1297, POm 1019 over the five PRFs; Fig. 11: AC 453.

24 Outcome under each reading (sets are the PRFs above baseline at corrected p < 0.01):
        N            B  kruskal_both                  during                   post  lowest_0_67  lowest_201_268              verdict
       N1           B1          True      [1500, 3000, 4500] [30, 1500, 3000, 4500]          300             300 partially reproduced
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000946-gao-2025 && cat > entry.yaml <<'EOF'
schema_version: 1
name: 000946-gao-2025
type: reproduction
title: Ultrasound responses in the cortico-thalamo-cortical pathway (Gao et al. 2025)
description: Tests the findings of Gao, Ramachandran, Yu and He (2025) on dandiset 000946, which holds
  sorted spike times from S1, POm, auditory cortex and M1 of anesthetized rats during transcranial
  focused ultrasound at several pulse repetition frequencies and duty cycles. The files hold no spike
  waveforms and no cell types, so only the auditory cortex responses of Figure 11B, which the paper does
  not split by type, can be tested.
license: Apache-2.0
notebooks:
- path: reproduce_gao_2025.ipynb
  title: Reproducing Gao et al. (2025) from dandiset 000946
  runtime_minutes: 5
helpers:
- tfus.py
related:
- id: dandi:000946/0.250829.1249
  relation: uses_data
- id: doi:10.1523/jneurosci.2218-24.2025
  relation: reproduces
EOF
printf "h5py\nipykernel\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\n" > requirements.in
cat ../001453-fouke-2025/requirements.lock.txt | head -5; date -u
```

```
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
Sat Oct 31 23:39:46 UTC 2026
```

**Agent calls Bash**

```bash
cd  && sed -i '/ipykernel/d' entries/000946-gao-2025/requirements.in && cat > entries/000946-gao-2025/README.md <<'EOF'
# Gao, Ramachandran, Yu & He (2025) from dandiset 000946

Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) that can be
tested on [DANDI:000946](https://dandiarchive.org/dandiset/000946/0.250829.1249), which holds sorted spike
times from S1, POm, auditory cortex (AC) and M1 of anesthetized rats during transcranial focused
ultrasound (tFUS) aimed at S1, M1 or POm.

| Claim | Outcome |
|---|---|
| AC neurons respond during sonication to 1500 and 3000 Hz PRF and after it to 30, 1500, 3000 and 4500 Hz, least to 300 Hz (Fig. 11B) | Partially reproduced (assumed normalization) |
| RSU and FSU responses and counts in S1 and POm (Figs. 4, 6 to 9; 24 claims) | Blocked: data missing |
| Sham and CG1 control (Fig. 5) | Blocked: data missing |
| Directional and undirected spike time tiling coefficients (Figs. 10, 11C, 11D; 8 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper splits units into regular-spiking (RSU) and fast-spiking (FSU) units by k-means on spike
waveform measures. The files hold no waveforms, and their `celltype_label` column, described as 1 = RSU
and 2 = FSU, is 0 for every unit, so every claim about RSUs or FSUs is blocked. Most recordings are
deposited twice; the notebook checks that the copies are identical and counts each once. No session is
marked as sham or as tFUS aimed at CG1. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/000946-gao-2025-01.yaml`](../../attempts/000946-gao-2025-01.yaml).

- `reproduce_gao_2025.ipynb`: the data check, the clock check and the Figure 11B analysis. It takes about
  five minutes, most of it reading the headers of all 1920 files and checking the duplicates.
- `tfus.py`: listing and reading the files, removing duplicate deposits, window spike counts and the
  normalized rates and tests of the paper. Other notebooks on this dandiset can import it.
EOF
python tools/entry.py lock entries/000946-gao-2025 2>&1 | tail -3
```

```
wrote entries/000946-gao-2025/requirements.lock.txt
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000946-gao-2025 2>&1 | tail -15
```

```
Installed kernelspec registry-000946-gao-2025 in executed/000946-gao-2025/.venv/share/jupyter/kernels/registry-000946-gao-2025
0 error(s)
pass  reproduce_gao_2025.ipynb  (259 s)

real	4m23.892s
user	5m52.588s
sys	0m26.865s
```

**Agent**

The notebook passes the entry checks and runs from a clean environment in 259 s. Confirming the executed copy's numbers before writing the record.

**Agent calls Bash**

```bash
ls executed/000946-gao-2025/; cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import nbformat,glob
p=glob.glob('executed/000946-gao-2025/*.ipynb')[0]
nb=nbformat.read(open(p),4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code' and ('claim:fig11b-ac-responses' in c.metadata.get('tags',[]) or i in (11,17)):
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(i,o['text'][:1800])
EOF
```

```
reproduce_gao_2025.ipynb
result.json
11 60 identifiers with two areas; same trial start times: 60; same intervals between trials: 60
session_start_time difference between the two area files of a session (min): median 15.5, max 3964.0
Empty DataFrame
Columns: [identifier, areas, n, same_times, same_intervals]
Index: []

17           S1_all  S1_in_POm_rats  S1_paired_with_POm   POm   AC
prf                                                            
30           530             390                 213   315  112
300          388             293                 141   267   89
1500         493             327                 174   246  138
3000         572             383                 234   352  167
4500         431             333                 224   290  127
all PRFs    2414            1726                 986  1470  633

Paper (Fig. 4 legend), RSU + FSU: S1 3000 Hz 366, POm 3000 Hz 250, S1 30 Hz 209, POm 30 Hz 232; Fig. 6 legend: S1 1297, POm 1019 over the five PRFs; Fig. 11: AC 453.

23 AC units with more than 2000 spikes, by rat and PRF:
[... 80 more lines not kept]
```

**Agent**

Numbers match. Writing the attempt record now.

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=1)[:6000])"
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
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']['properties']
for k in list(o)[6:]: print(k, json.dumps(o[k])[:300])
print(json.dumps(s['properties']['findings'])[:1500])
print([k for k in s['properties']])"
```

```
measured {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}
deviations {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}
assumed {"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).", "type": "boolean"}
proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "
{"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\").", "enum": ["on_prompt"]}}}}
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
```

**Agent calls Bash**

```bash
mkdir -p /tmp/claude && cat > /tmp/claude/gen_att.py <<'EOF'
import yaml
NB = "reproduce_gao_2025.ipynb"
TYPES = ("The paper types units as RSUs or FSUs by k-means on the initial phase and afterhyperpolarization of "
         "the spike waveform (Methods, Neuronal type classification). No file holds waveforms (the units tables "
         "hold spike_times and celltype_label only, and acquisition, analysis and processing are empty in all "
         "1550 unit files), and celltype_label, described as label 1 = RSU, label 2 = FSU, is 0 in all 1516 "
         "files that have it and absent from the other 34. The RSU/FSU split cannot be made.")
UNTYPED = ("As an untyped variant that decides nothing (notebook, Untyped responses), all units with more than 2000 "
           "spikes, reading N1 and B1: ")


def blocked(cid, extra="", why="data_missing", output=None):
    o = dict(claim=cid, outcome="blocked", blocked_by=why, notes=(TYPES + " " + extra).strip())
    if output:
        o["notebook"] = NB
        o["output"] = output
    return o


out = []
out.append(blocked("fig4-unit-counts",
    "The totals per area (units with more than 2000 spikes, distinct recordings, tFUS at S1, PD 200 us) are "
    "shown in the notebook's data check. At 3000 Hz, S1 has 572 units over all S1 recordings, 383 in the rats "
    "with POm recordings and 234 in the S1 recordings whose session also has a POm file (paper RSU + FSU 366), "
    "and POm has 352 (paper 250). At 30 Hz, S1 has 530, 390 and 213 (paper 209) and POm 315 (paper 232).",
    output="sanity"))
out.append(blocked("fig4a-s1-rsu-time-locked-3000",
    UNTYPED + "all S1 units at 3000 Hz (n = 572) have a mean normalized rate of 114% in 0 to 67 ms, above baseline "
    "at corrected p < 0.01."))
out.append(blocked("fig4b-pom-rsu-time-locked-3000",
    UNTYPED + "all POm units at 3000 Hz (n = 352) have 105% in 0 to 67 ms, above baseline at corrected p < 0.01."))
out.append(blocked("fig4-postsonication-3000",
    UNTYPED + "at 3000 Hz all S1 units are at 119% (134 to 201 ms) and 178% (201 to 268 ms), all POm units at 113% "
    "and 122%, each above baseline at corrected p < 0.01."))
out.append(blocked("fig4-30hz-responses",
    UNTYPED + "at 30 Hz all S1 units are at 96% in 67 to 134 ms (below baseline at corrected p < 0.01) and all POm "
    "units at 111% and 110% in 134 to 201 and 201 to 268 ms (above baseline)."))
out.append(blocked("fig4-fsu-no-change"))
SHAM = ("No recording is marked as sham or as tFUS aimed at CG1: none of the 816 distinct recordings has an "
        "identifier, general/notes or general/data_collection naming sham, no tFUS, CG1 or cingulate; every "
        "recording gives a PRF and a PD (in data_collection or in the identifier), and the targets named are S1, "
        "M1 and POm.")
out.append(blocked("fig5a-sham-no-change", SHAM))
out.append(blocked("fig5b-cg1-control-no-change", SHAM + " The sessions with tFUS aimed at M1 are not the CG1 "
    "control of the paper (Methods, CG1 at AP 3, ML 0), and the paper does not describe them."))
out.append(blocked("fig6-unit-counts",
    "Over the five PRFs at PD 200 us (units with more than 2000 spikes, distinct recordings), S1 has 2414 units "
    "over all S1 recordings, 1726 in the rats with POm recordings and 986 in the S1 recordings paired with POm "
    "(paper RSU + FSU 1297), and POm has 1470 (paper 1019).", output="sanity"))
for cid in ["fig6a-s1-rsu-time-locked-prf", "fig6a-s1-rsu-delayed-prf", "fig6b-s1-fsu-prf", "fig6c-pom-rsu-prf",
            "fig6d-pom-fsu-prf"]:
    out.append(blocked(cid))
DC = "The duty cycle series sessions are in the dataset (PD values from 1.4 us to 30000 us), but without cell types."
for cid in ["fig7a-s1-rsu-dc-3000", "fig7b-s1-fsu-dc-3000", "fig7c-pom-rsu-dc-3000", "fig7d-pom-fsu-dc-3000",
            "fig8a-s1-rsu-dc-30", "fig8b-s1-fsu-dc-30", "fig9a-s1-rsu-prf-60dc", "fig9b-s1-fsu-prf-60dc"]:
    out.append(blocked(cid, DC))
STTC = ("The dandiset's STTC files (370, under sub-STTC-*) hold STTC values between the units of two areas, but "
        "carry no unit identities or cell types, and their arrays have no dimension for the nine dt values their "
        "descriptions list, so they cannot stand in either.")
for cid in ["fig10a-dsttc-3000", "fig10b-dsttc-30", "fig10c-sttc-constant-pd", "fig10d-sttc-60dc",
            "fig10e-sttc-dc-30", "fig10f-sttc-dc-3000"]:
    out.append(blocked(cid, STTC))
out.append(dict(claim="pathway-follows-local-prf", outcome="blocked", blocked_by="data_missing",
    notes="Depends on fig6a-s1-rsu-time-locked-prf and fig10c-sttc-constant-pd, both blocked because the dataset "
          "holds no waveforms or cell types."))
out.append(dict(
    claim="fig11b-ac-responses", outcome="partially_reproduced", assumed=True, notebook=NB,
    output="claim:fig11b-ac-responses", measured=[633],
    notes=(
        "AC units with more than 2000 spikes in the 17 distinct AC recordings with tFUS at S1 and PD 200 us, from 6 "
        "rats; 112, 89, 138, 167 and 127 units at 30, 300, 1500, 3000 and 4500 Hz, 633 in all (expected 453 +/- "
        "45.3, so the count does not match). Under the adopted reading (N1, B1, Bonferroni over five PRFs) the "
        "Kruskal-Wallis tests give p = 7.83e-06 (0 to 67 ms) and 5.16e-49 (201 to 268 ms); during sonication 1500 "
        "Hz (140.3%, corrected p = 2.46e-08), 3000 Hz (107.1%, 9.72e-11) and also 4500 Hz (108.0%, 7.05e-05) are "
        "above baseline, 30 Hz is not (105.9%, 0.0189); postsonication exactly 30, 1500, 3000 and 4500 Hz are "
        "above baseline (176.4, 147.9, 310.5 and 210.8%) and 300 Hz is not (94.3%); 300 Hz has the lowest mean "
        "in both windows. The time-locked set differs from the paper's by one PRF (4500 Hz), which the criterion "
        "calls partially reproduced. The readings disagree: N1 with B2 adds 300 Hz to the time-locked set (not "
        "reproduced); N2 with B1 finds no PRF above baseline and N2 with B2 finds only 1500 Hz during and 4500 Hz "
        "after sonication, with a Kruskal-Wallis p of 0.0213 during sonication (both not reproduced). The variant "
        "B3 (paired signed-rank of raw rates) gives the same sets as N1 with B1. The verdict under N1 and B1 is the "
        "same for spike-count rules of 1000, 2000, 4000 and 8000 spikes (667, 633, 445 and 320 units). By rat, the "
        "4500 Hz time-locked rise is largest in BH537 (135.3%) and near 100% in BH547 (99.4%), and the "
        "postsonication values vary widely (for 3000 Hz, 112.0 to 654.1% across three rats). The statement's "
        "PRF dependence (both Kruskal-Wallis tests) holds. The question of which normalization the paper used is "
        "for the paper's authors (finding methods_unavailable).")),
    deviations=[
        "Assumed, normalization N1: a unit's mean count in the window over trials divided by its mean count in "
        "[-67, 0) ms. The Statistical analysis says the rates were normalized to the 67 ms before stimulation "
        "without saying whether per trial (N2) or over trials. N2 averages per-trial ratios over the trials with "
        "a nonzero baseline (a median of 23% of trials for AC units), which biases it below 100% with no stimulus "
        "(49.8 to 61.7% at trial starts shifted by 1 s, against 94.3 to 99.0% for N1), so N2 cannot be a rate "
        "normalized to the pre-stimulus period; N1 is adopted and N2 is shown.",
        "Assumed, baseline sample B1: the window's normalized rates are compared with the units' normalized "
        "[-67, 0) ms rates (100% under N1), the pre-stimulus period the Statistical analysis names. B2 (the "
        "[-134, -67) ms window, which the paper never names) is shown.",
        "The Bonferroni factor is the five PRF levels of the panel (claims file header, reading C1); reading C2 "
        "applies only to a panel with a single comparison.",
        "The dataset holds AC recordings from 6 rats at PD 200 us (7 AC rats in all) where the paper reports 12 "
        "S1-AC rats, and it gives 633 units with more than 2000 spikes where the paper reports 453; the paper's "
        "selection of AC units could not be matched.",
        "Recordings deposited twice (identical spike times and trial starts) are counted once.",
        "Trial start_time is taken as sonication onset; the clock check shows the firing changes after it and not "
        "1 s later, which is consistent with this but does not prove there is no fixed delay.",
    ]))
out.append(blocked("fig11c-ac-to-s1-30hz", "The AC units are in the dataset, but the target S1 RSUs and the S1 FSU "
    "part need the cell types. " + STTC))
out.append(blocked("fig11d-ac-to-s1-3000", "The AC units are in the dataset, but the S1 RSU and S1 FSU targets need "
    "the cell types. " + STTC))
out.append(dict(claim="auditory-confound-low-prf", outcome="blocked", blocked_by="data_missing",
    notes="Depends on fig11c-ac-to-s1-30hz and fig11d-ac-to-s1-3000, both blocked because the dataset holds no "
          "waveforms or cell types for the S1 units."))

findings = [
    dict(kind="data_missing", statement=(
        "The spike waveforms are not in the dataset, and the RSU/FSU cell types are not either: no file has "
        "waveforms or mean waveforms, and acquisition, analysis and processing are empty in all 1550 unit files. "
        "The paper types every S1 and POm unit from its waveform (Methods, Neuronal type classification), so 32 "
        "of the 33 claims (all those on RSUs, FSUs or their correlations) cannot be tested.")),
    dict(kind="metadata_error", statement=(
        "The units column celltype_label is described as label 1 = RSU, label 2 = FSU, but it is 0 for every unit "
        "in the 1516 unit files that have it; 34 unit files have no such column.")),
    dict(kind="other", statement=(
        "734 of the 1550 unit files are second (or third) copies of another file, with identical spike times and "
        "trial starts and the same identifier, under session start times up to 57 s apart and different file "
        "names; 816 distinct recordings remain. Counting the files as they are would double most unit counts.")),
    dict(kind="data_missing", statement=(
        "No recording is marked as sham (no tFUS) or as tFUS aimed at CG1, the control conditions of Figure 5; "
        "every recording gives a PRF and a PD and a target of S1, M1 or POm. If the sham and CG1 sessions are in "
        "the dataset, they cannot be found.")),
    dict(kind="data_missing", statement=(
        "The dataset has 10 rats with POm recordings and 7 with AC recordings, where the paper reports 16 S1-POm "
        "rats and 12 S1-AC rats (Methods); 20 rats in all.")),
    dict(kind="selection_undocumented", statement=(
        "The AC recordings at PD 200 us give 633 units with more than 2000 spikes (112, 89, 138, 167 and 127 at "
        "30 to 4500 Hz), where Figure 11 reports 453 (83, about 59, 107, 104 and 100), although the dataset has "
        "fewer AC rats than the paper. The S1 and POm totals also differ from the paper's RSU + FSU counts (for "
        "example POm at 3000 Hz, 352 against 250). The paper's unit selection cannot be repeated from its "
        "description.")),
    dict(kind="other", statement=(
        "The dataset also holds recordings of M1 and sessions with tFUS aimed at M1 (152 distinct recordings) or "
        "at POm (65), and single recordings of S1BF, VPM and other labelled sites, none of which the paper "
        "describes; the dandiset description mentions only S1, POm and AC with tFUS at S1.")),
    dict(kind="metadata_error", statement=(
        "In the 60 sessions with files from two areas, both files have identical trial start times, so the areas "
        "were recorded together, but their session_start_time values differ (median 15.5 min, up to 3964 min); "
        "session_start_time does not give the start of the recording.")),
    dict(kind="metadata_insufficient", statement=(
        "The recorded area and the tFUS target are given only in free text in general/notes, in two spellings; "
        "the electrodes table has location unknown and the electrode group location is 'brain area'. Five "
        "recordings of BH500 leave the area empty. general/data_collection, which carries the PRF and PD, is empty "
        "in 33 recordings (BH494 25, BH499 6, BH500 2), where the identifier gives them; where both are given (782 "
        "recordings) they agree.")),
    dict(kind="format_error", statement=(
        "The arrays of the STTC files do not have the shape their descriptions give: the descriptions list a "
        "dimension for nine dt values, while the arrays have the 10 time windows, the trials and the units of the "
        "two areas (for example STTC is 10 x 499 x 20 x 9) and no dt dimension. Which dt was used, and which units "
        "the rows and columns are, is not stated.")),
    dict(kind="methods_unavailable", statement=(
        "Question for the paper's authors: was the normalized spiking rate the ratio of a unit's mean rate in the "
        "window to its mean rate in the 67 ms before stimulation (over trials), or a per-trial ratio averaged over "
        "trials; and in the post hoc Wilcoxon test against baseline, what was the baseline sample (the normalized "
        "pre-stimulus rates, which are 100% under the first reading, or another pre-stimulus window)? The "
        "Statistical analysis says only that rates were normalized to the 67 ms before stimulation. For Figure 11B "
        "the readings give different outcomes; the first reading with the pre-stimulus window was assumed.")),
]

att = dict(
    schema_version=2, id="000946-gao-2025-01",
    dataset=dict(archive="dandi", id="000946", version="0.250829.1249", doi="10.48324/dandi.000946/0.250829.1249"),
    paper="doi:10.1523/jneurosci.2218-24.2025", date="2026-10-31", entry="000946-gao-2025",
    provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
                    agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-13"),
                    runner=dict(platform="GitHub Actions",
                                url="https://github.com/catalystneuro/encore/actions/runs/41249314684")),
    outcomes=out, findings=findings)
with open("attempts/000946-gao-2025-01.yaml", "w") as f:
    yaml.safe_dump(att, f, sort_keys=False, width=110, allow_unicode=True)
print(len(out))
EOF
python /tmp/claude/gen_att.py && grep -c "^- claim" attempts/000946-gao-2025-01.yaml && python tools/entry.py check entries/000946-gao-2025 2>&1 | tail -5
```

```
Exit code 1
  File "/tmp/claude/gen_att.py", line 105
    ]))
      ^
SyntaxError: unmatched ')'
```

**Agent calls Bash**

```bash
cd /tmp/claude && sed -i 's/(finding methods_unavailable).")),/(finding methods_unavailable)."),/' gen_att.py && python gen_att.py && cd  && grep -c "^- claim" attempts/000946-gao-2025-01.yaml && python tools/entry.py check entries/000946-gao-2025 2>&1 | tail -5
```

```
33
33
0 error(s)
```

**Agent calls Bash**

```bash
grep -n -i "—\|rather" attempts/000946-gao-2025-01.yaml entries/000946-gao-2025/*.py entries/000946-gao-2025/*.md entries/000946-gao-2025/*.yaml entries/000946-gao-2025/*.ipynb; grep -c "\*\*" entries/000946-gao-2025/reproduce_gao_2025.ipynb; grep -o "\*\*[^*]*\*\*" entries/000946-gao-2025/reproduce_gao_2025.ipynb | sort | uniq; date -u
```

```
7
**Dandiset.**
**Paper.**
**Result: partially reproduced, resting on the assumption of reading N1 with baseline B1.**
**What the dataset holds.**
Sat Oct 31 23:45:53 UTC 2026
```

**Agent calls Bash**

```bash
cd /tmp/claude && sed -i 's/\*\*Paper\.\*\*/Paper./; s/\*\*Dandiset\.\*\*/Dandiset./; s/\*\*What the dataset holds\.\*\*/What the dataset holds./' gen_nb.py && cd $TMPDIR && . env/bin/activate && python /tmp/claude/gen_nb.py && cd  && grep -o "\*\*[^*]*\*\*" entries/000946-gao-2025/reproduce_gao_2025.ipynb | sort -u && python tools/entry.py all entries/000946-gao-2025 2>&1 | tail -3
```

```
written 33
**Result: partially reproduced, resting on the assumption of reading N1 with baseline B1.**
Installed kernelspec registry-000946-gao-2025 in executed/000946-gao-2025/.venv/share/jupyter/kernels/registry-000946-gao-2025
0 error(s)
pass  reproduce_gao_2025.ipynb  (258 s)
```

**Agent**

Clean run passed again (258 s). Running the handover step.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000946-gao-2025 2>&1 | tail -5; ls executed/000946-gao-2025/handover/; git status --short; date -u
```

```
wrote executed/000946-gao-2025/handover
10.1523-jneurosci.2218-24.2025.yaml
reproduce_gao_2025.ipynb
tfus.py
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
?? attempts/000946-gao-2025-01.yaml
?? entries/000946-gao-2025/
?? scripts
Sat Oct 31 23:50:36 UTC 2026
```

**Agent calls Bash**

```bash
ls -la scripts .idea .vscode | head; wc -c .bashrc .mcp.json; ls entries/000946-gao-2025/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:40 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:40 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 22:40 scripts
wc: .bashrc: Permission denied
wc: .mcp.json: Permission denied
      0 total
README.md
__pycache__
entry.yaml
reproduce_gao_2025.ipynb
requirements.in
requirements.lock.txt
tfus.py
```

**Agent calls Bash**

```bash
rm -rf entries/000946-gao-2025/__pycache__; python tools/entry.py check entries/000946-gao-2025 2>&1 | tail -1
```

```
0 error(s)
```

**Agent**

I finished steps 1 to 6 by 23:51 UTC, about 1 h 10 min into the 5 h window. Only one of the 33 claims could be tested: the dataset has no spike waveforms and no cell types, and the paper's RSU/FSU split depends on them. The entry passes its checks and runs from a clean environment in 258 s, and the handover is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig11b-ac-responses | Partially reproduced (`assumed: true`) |
| fig4-unit-counts, fig6-unit-counts | Blocked, data_missing (area totals shown in the notes) |
| fig4a, fig4b, fig4-postsonication-3000, fig4-30hz-responses, fig4-fsu-no-change | Blocked, data_missing |
| fig5a-sham-no-change, fig5b-cg1-control-no-change | Blocked, data_missing (also no sham or CG1 sessions marked) |
| fig6a (2 claims), fig6b, fig6c, fig6d | Blocked, data_missing |
| fig7a to fig7d, fig8a, fig8b, fig9a, fig9b | Blocked, data_missing |
| fig10a to fig10f | Blocked, data_missing |
| fig11c-ac-to-s1-30hz, fig11d-ac-to-s1-3000 | Blocked, data_missing (the S1 units need cell types) |
| pathway-follows-local-prf, auditory-confound-low-prf | Blocked, because they depend on blocked claims |

**Fig. 11B (auditory cortex neurons):**
- **What matches:** under the adopted reading, the after-sonication set is exactly 30, 1500, 3000 and 4500 Hz, 300 Hz has the lowest response in both windows, and both Kruskal-Wallis tests are significant.
- **What does not:**
  - During sonication, 4500 Hz is also above baseline, so that set has one PRF more than the paper's.
  - The dataset gives 633 AC units with more than 2000 spikes, against the paper's 453.

## 2. The dataset
- **No cell types:** no file holds waveforms. `celltype_label` is described as 1 = RSU and 2 = FSU, but it is 0 in all 1516 files that have it, and the other 34 files lack the column.
- **Duplicates:** 734 of the 1550 unit files are copies of another file, with identical spike times and trial starts. I counted the 816 distinct recordings once each.
- **Sham and control sessions:** none is marked as sham or as aimed at CG1, so Fig. 5 cannot be found.
- **Rats:** 10 have POm recordings and 7 have AC recordings, where the paper reports 16 and 12.
- **Extra data:** there are M1 recordings and sessions with tFUS aimed at M1 or POm, which the paper does not describe.
- **Smaller metadata problems:**
  - The two area files of one session have identical trials but different `session_start_time` values.
  - The area is given only in free-text notes.
  - The PRF and PD field is empty in 33 recordings; the identifier supplies them there.
- **STTC files:** their arrays have no dimension for the dt values their description lists, and they name no units.
- **Clock check:** firing changes after the trial starts and not when the starts are shifted by 1 s, so the trial times share the spike clock.
- **Version:** I pinned 0.250829.1249, the latest. The paper cites the dandiset without a version, and all six versions list the same files.

**Assumption, and the question for the paper's authors** (recorded as a `methods_unavailable` finding):
- The paper does not say how the normalized rate is computed or what the baseline sample is. I adopted the ratio of mean rates over trials, compared with the 67 ms before stimulation.
- The alternative averages per-trial ratios over trials with a nonzero baseline. It reads 50 to 62% even with no stimulus, so it cannot be a rate normalized to the pre-stimulus period.
- The readings give different outcomes for Fig. 11B, and the notebook shows all of them.

I asked a reader no questions.

## 3. Protocol gaps
1. **Almost everything blocked:** the protocol does not address a dataset where one missing variable (cell type) blocks nearly every claim. I blocked each claim as data_missing and showed untyped results as variants that decide nothing.
2. **A reading that is an artefact:** step 1.6 says to run every reading, but one of the claims file's readings is biased by construction. I ran it, showed the bias against shifted trial starts, and adopted the other reading as an assumption.
3. **Extra data:** there is no rule for a dataset holding experiments the paper does not describe. I recorded it as an `other` finding.
4. **Header in the notebook:** the protocol does not name a header field for the reason the version was chosen. I put it in the notebook header.
5. **Untracked files at the repo root:** `.bashrc`, `scripts` and others are sandbox device mounts created before this run. I left them alone. The workflow should not commit them.

## 4. Runtime and failures
- The notebook takes about 4.3 min; reading all 1920 file headers and hashing the duplicate pairs take most of that.
- My first survey used threads and took 28 min, because h5py runs one call at a time across threads; the helper uses processes instead.
- One early notebook run failed on a pandas type error, which I fixed.
- Nothing failed in the final run.

Files are in `entries/000946-gao-2025/`:
- `reproduce_gao_2025.ipynb`
- `tfus.py`

The attempt record is `attempts/000946-gao-2025-01.yaml`.

## End of run

59 turns, 65 minutes, result: success.
