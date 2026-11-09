# 001357 · author · run 41402628393

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/50279903-1098-4fbe-8973-7b67441059b8/tool-results/b1l4tix8l.txt

Preview (first 2KB):
Mon Nov  2 06:55:53 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/50279903-1098-4fbe-8973-7b67441059b8/tool-results/b1l4tix8l.txt"
}
```

```
1	Mon Nov  2 06:55:53 UTC 2026
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
[... 619 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md docs/archives.md; ls claims/001357 paper entries/001453-fouke-2025 attempts | head -50
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
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/archives.md; sed -n 1,400p docs/design.md
```

```
<persisted-output>
Output too large (29.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/50279903-1098-4fbe-8973-7b67441059b8/tool-results/b7tc3rnrj.txt

Preview (first 2KB):
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

## DANDI
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001357/*.yaml; ls questions | head; ls queue targets | head
```

```
<persisted-output>
Output too large (52.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/50279903-1098-4fbe-8973-7b67441059b8/tool-results/b2krumvft.txt

Preview (first 2KB):
# Claims for Namima, Kempkes, Zamarashkina, Owen & Pasupathy (2025), "High-Density Recording
# Reveals Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4",
# J Neurosci 45(5) e1893232024, on dandiset 001357.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF), with
# the main text, Materials and Methods, and figure legends. The paper has no supplement. The PDF
# was not opened; the text was enough.
#
# Code: the paper links no analysis code and gives no code or data availability statement. The
# only software it names for the experiments is the stimulus software, "Pype2; Mazer, 2013", with
# no link; the first reader read pype3 (github.com/mazerj/pype3, HEAD at
# 49056d6f7e02bb217b2f044dba6ec7a33173b4ca on 2026-10-21), a later version. It
# runs the stimuli and the fixation task and holds none of the analyses, so it settles no method
# detail here. The analyses were written in MATLAB (fit.m, confint.m, conv2.m, the cortex-lab
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/50279903-1098-4fbe-8973-7b67441059b8/tool-results/b2krumvft.txt"
}
```

```
1	# Claims for Namima, Kempkes, Zamarashkina, Owen & Pasupathy (2025), "High-Density Recording
2	# Reveals Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4",
3	# J Neurosci 45(5) e1893232024, on dandiset 001357.
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
5	# pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF), with
8	# the main text, Materials and Methods, and figure legends. The paper has no supplement. The PDF
9	# was not opened; the text was enough.
10	#
11	# Code: the paper links no analysis code and gives no code or data availability statement. The
12	# only software it names for the experiments is the stimulus software, "Pype2; Mazer, 2013", with
13	# no link; the first reader read pype3 (github.com/mazerj/pype3, HEAD at
14	# 49056d6f7e02bb217b2f044dba6ec7a33173b4ca on 2026-10-21), a later version. It
15	# runs the stimuli and the fixation task and holds none of the analyses, so it settles no method
16	# detail here. The analyses were written in MATLAB (fit.m, confint.m, conv2.m, the cortex-lab
17	# Spikes toolbox) by the authors and are not public. The noise-corrected correlation follows
18	# Pospisil and Bair (2021, J Neurosci 41 5638), which the paper cites and does not link; its method
19	# is taken from this paper's Methods alone.
20	#
[... 877 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/001453-fouke-2025/ claims/001453/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml | head -200
```

```
claims/001453/:
total 28
drwxr-xr-x   2 runner runner  4096 Nov  2 06:52 .
drwxr-xr-x 234 runner runner  4096 Nov  2 06:52 ..
-rw-r--r--   1 runner runner 17825 Nov  2 06:52 10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025/:
total 132
drwxr-xr-x   2 runner runner  4096 Nov  2 06:52 .
drwxr-xr-x 158 runner runner 12288 Nov  2 06:52 ..
-rw-r--r--   1 runner runner  2158 Nov  2 06:52 README.md
-rw-r--r--   1 runner runner   914 Nov  2 06:52 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov  2 06:52 omr.py
-rw-r--r--   1 runner runner 79403 Nov  2 06:52 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov  2 06:52 requirements.in
-rw-r--r--   1 runner runner  5989 Nov  2 06:52 requirements.lock.txt
schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
[... 225 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p attempts/001453-fouke-2025-01.yaml; cat entries/001453-fouke-2025/README.md; ls paper/; ls questions/ | grep 1357
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001357/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001357/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; V=0.261006.2007; curl -s "https://api.dandiarchive.org/api/dandisets/001357/versions/$V/" > meta.json; python -c "
import json;m=json.load(open('meta.json'))
print(m.get('description'));print(m.get('citation'));print(json.dumps(m.get('assetsSummary'),indent=0)[:2000]);print(m.get('relatedResource'))"
curl -s "https://api.dandiarchive.org/api/dandisets/001357/versions/$V/assets/?page_size=200" > assets.json; python -c "
import json;a=json.load(open('assets.json'));print(a['count'])
for x in a['results']: print(x['path'],x['size'],x['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "import pynwb, remfile, h5py; print(pynwb.__version__)" 2>&1; which uv python; python --version
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
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas matplotlib statsmodels nbformat nbclient ipykernel pyyaml jsonschema 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe.py <<'EOF'
import remfile, h5py, pynwb, sys, requests
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
import urllib.request
f=remfile.File(url)
h=h5py.File(f,'r')
def walk(g,p=''):
    for k,v in g.items():
        if isinstance(v,h5py.Dataset): print(p+k, v.shape, v.dtype, dict(v.attrs).get('description','')[:100] if v.attrs.get('description') is not None else '')
        else:
            print(p+k+'/', {a:str(v.attrs[a])[:150] for a in v.attrs if a not in ('namespace','object_id')})
            walk(v,p+k+'/')
walk(h)
EOF
python probe.py 70893b9c-ef41-4294-9692-2cfec03c58b0 2>&1 | head -150
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object 
general/ {}
general/devices/ {}
general/devices/Neuropixels/ {'description': 'bank0_384ch', 'manufacturer': 'IMEC', 'neurodata_type': 'Device'}
general/experimenter (1,) object 
general/extracellular_ephys/ {}
general/extracellular_ephys/electrodes/ {'colnames': "['location' 'group' 'group_name' 'label']", 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/group (384,) object a reference to the ElectrodeGroup this electrode is a part of
general/extracellular_ephys/electrodes/group_name (384,) object the name of the ElectrodeGroup this electrode is a part of
general/extracellular_ephys/electrodes/id (384,) int64 
general/extracellular_ephys/electrodes/label (384,) object label of electrode
general/extracellular_ephys/electrodes/location (384,) object the location of channel within the subject e.g. brain region
general/extracellular_ephys/probe0/ {'description': 'electrode group for probe 0', 'location': 'V4', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/probe0/device/ {'description': 'bank0_384ch', 'manufacturer': 'IMEC', 'neurodata_type': 'Device'}
general/institution () object 
general/lab () object 
general/session_id () object 
general/subject/ {'neurodata_type': 'Subject'}
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe2.py <<'EOF'
import remfile, h5py, sys, numpy as np, pandas as pd
aid=sys.argv[1]
h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{aid}/download/"),'r')
for k in ['session_description','identifier','general/session_id','general/subject/subject_id','general/subject/description','general/subject/sex','general/subject/age','general/subject/species','general/institution','general/lab','session_start_time','timestamps_reference_time','general/experimenter']:
    print(k, h[k][()])
t=h['intervals/trials']
df=pd.DataFrame({c:(t[c][:] ) for c in ['start_time','stop_time','ses_ID','pen_ID','sub_ID','cond_ID','stim_ID','rotation','luminance','pdOnTS','pdOffTS']})
print(df.head(20).to_string()); print(df.describe().to_string())
for c in ['ses_ID','pen_ID','sub_ID','luminance','rotation']: print(c, df[c].value_counts().head(10).to_dict())
print('stim', np.unique(df.stim_ID)); print('cond n', df.cond_ID.nunique(), df.cond_ID.min(), df.cond_ID.max())
u=h['units']
ud=pd.DataFrame({c:u[c][:] for c in ['ses_ID','pen_ID','sub_ID','unit_ID','probe_num','depth','best_ch','is_sua']})
print(ud.to_string())
e=h['general/extracellular_ephys/electrodes']
print(e['label'][:5], e['location'][:3])
st=u['spike_times'][:]; print(st.min(), st.max(), np.all(np.diff(st[:u['spike_times_index'][0]])>=0))
EOF
python probe2.py 70893b9c-ef41-4294-9692-2cfec03c58b0 2>&1 | head -250
```

```
session_description b'V4 shape screen'
identifier b'20190726SL'
general/session_id b'20190726SL'
general/subject/subject_id b'Z08115'
general/subject/description b'Z08115_V4'
general/subject/sex b'F'
general/subject/age b'P12Y'
general/subject/species b'Macaca mulatta'
general/institution b'University of Washington'
general/lab b'Pasupathy Lab'
session_start_time b'2019-07-26T10:30:00-07:00'
timestamps_reference_time b'2019-07-26T10:30:00-07:00'
general/experimenter [b'Namima, Tomoyuki']
     start_time    stop_time       ses_ID  pen_ID     sub_ID  cond_ID  stim_ID  rotation  luminance       pdOnTS      pdOffTS
0   1480.630980  1481.167101  b'190726SL'  b'p05'  b'Z08115'        0      NaN       NaN          0  1480.780980  1481.017101
1   1652.916389  1653.442470  b'190726SL'  b'p05'  b'Z08115'        0      NaN       NaN          0  1653.066389  1653.292470
2   1727.806580  1728.342661  b'190726SL'  b'p05'  b'Z08115'        0      NaN       NaN          0  1727.956580  1728.192661
3   1965.065494  1965.591575  b'190726SL'  b'p05'  b'Z08115'        0      NaN       NaN          0  1965.215494  1965.441575
4   2009.054941  2009.581022  b'190726SL'  b'p05'  b'Z08115'        0      NaN       NaN          0  2009.204941  2009.431022
5   2042.837580  2043.363661  b'190726SL'  b'p05'  b'Z08115'        0      NaN       NaN          0  2042.987580  2043.213661
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "Materials and Methods\|^Results\|Discussion\|References" paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1893-23.2024.txt",
 "offset": 100,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 520,660p paper/10.1523-jneurosci.1893-23.2024.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 800,1060p paper/10.1523-jneurosci.1893-23.2024.txt | grep -v "^[0-9.\-]*$" | head -200
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^Figure [0-9]*\.\|Figure 5\.\|Figure 9\.\|Figure 12\.\|Figure 11\.\|Figure 10\.\|Figure 8\." paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=paper/*.txt; sed -n 667,680p $f; sed -n 1126,1140p $f; sed -n 1255,1300p $f; sed -n 1369,1380p $f; sed -n 1400,1480p $f | grep -v "^[0-9.\-]*$"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > probe3.py <<'EOF'
import remfile, h5py, sys, numpy as np, pandas as pd
aid=sys.argv[1]
h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{aid}/download/"),'r')
print(h['session_description'][()], h['general/session_id'][()])
t=h['intervals/trials']
cols=[c for c in t.keys() if c not in ('id',)]
print(dict(t.attrs)['colnames'])
for c in cols:
    print(c, t[c].attrs.get('description'), t[c].shape)
df=pd.DataFrame({c:t[c][:] for c in cols if t[c].ndim==1})
print(df.head(5).to_string())
for c in df.columns:
    if df[c].nunique()<50: print(c, df[c].value_counts().sort_index().to_dict())
    else: print(c, df[c].nunique())
u=h['units']; print(list(u.keys()))
print(pd.Series(u['is_sua'][:]).value_counts().to_dict(), len(u['is_sua']), u['pen_ID'][0])
print(np.sort(u['unit_ID'][:])[:20])
EOF
python probe3.py 592a644f-2885-438a-a627-30416acfd622; python probe3.py 30416acfd622 2>/dev/null; python probe3.py 30b5b542-3888-4599-b8de-db1c718b112b 2>&1 | tail -5; python probe3.py 30b5b542-3888-4599-b8de-db1c718b112b 2>&1 | head -3
```

```
Mon Nov  2 06:57:25 UTC 2026
b'V4 texture screen' b'20200723TX'
['start_time' 'stop_time' 'ses_ID' 'pen_ID' 'sub_ID' 'cond_ID' 'stim_ID'
 'mode' 'pdOnTS' 'pdOffTS']
cond_ID stimulus condition ID (992,)
mode 0 (normal), 1 (reversed), 2 (spectral noise) (992,)
pdOffTS photodiode OFF time (992,)
pdOnTS photodiode ON time (992,)
pen_ID penetration ID (992,)
ses_ID session ID (992,)
start_time Start time of epoch, in seconds (992,)
stim_ID texture stim ID (992,)
stop_time Stop time of epoch, in seconds (992,)
sub_ID subject ID (992,)
   cond_ID  mode      pdOffTS       pdOnTS  pen_ID       ses_ID   start_time  stim_ID    stop_time     sub_ID
0        0   NaN   944.484588   944.290227  b'p63'  b'200723TX'   944.140227      NaN   944.634588  b'Z08115'
1        0   NaN   971.733118   971.508717  b'p63'  b'200723TX'   971.358717      NaN   971.883118  b'Z08115'
2        0   NaN   997.790801   997.556399  b'p63'  b'200723TX'   997.406399      NaN   997.940801  b'Z08115'
3        0   NaN  1011.750288  1011.525926  b'p63'  b'200723TX'  1011.375926      NaN  1011.900288  b'Z08115'
4        0   NaN  1049.235761  1049.031400  b'p63'  b'200723TX'  1048.881400      NaN  1049.385761  b'Z08115'
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python probe3.py 30c5b542-3888-4599-b8de-db1c718b112b 2>&1 | head -60; python probe3.py c708b7fc-5be0-4440-aa61-463f27a71099 2>&1 | grep -v "^ *[0-9]" | tail -8
```

```
b'V4 shape screen. position test' b'20210512SP'
['start_time' 'stop_time' 'ses_ID' 'pen_ID' 'sub_ID' 'cond_ID' 'stim_ID'
 'position' 'pdOnTS' 'pdOffTS']
cond_ID stimulus condition ID (632,)
pdOffTS photodiode OFF time (632,)
pdOnTS photodiode ON time (632,)
pen_ID penetration ID (632,)
position position ID (0-4) (632,)
ses_ID session ID (632,)
start_time Start time of epoch, in seconds (632,)
stim_ID shape stim ID (632,)
stop_time Stop time of epoch, in seconds (632,)
sub_ID subject ID (632,)
   cond_ID      pdOffTS       pdOnTS  pen_ID  position       ses_ID   start_time  stim_ID    stop_time     sub_ID
0        0  2379.948779  2379.741819  b'p28'       NaN  b'210512SL'  2379.591819      NaN  2380.098779  b'Z11111'
1        0  2407.727500  2407.500540  b'p28'       NaN  b'210512SL'  2407.350540      NaN  2407.877500  b'Z11111'
2        0  2409.028380  2408.801380  b'p28'       NaN  b'210512SL'  2408.651380      NaN  2409.178380  b'Z11111'
3        0  2414.231861  2414.034901  b'p28'       NaN  b'210512SL'  2413.884901      NaN  2414.381861  b'Z11111'
4        0  2415.993061  2415.756061  b'p28'       NaN  b'210512SL'  2415.606061      NaN  2416.143061  b'Z11111'
cond_ID 76
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import remfile, h5py, json, numpy as np, pandas as pd, time
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets.json'))['results']
def one(x):
    h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"),'r')
    u=h['units']; t=h['intervals/trials']
    idx=u['spike_times_index'][:]; 
    pen=set(u['pen_ID'][:].astype(str)); tpen=set(t['pen_ID'][:].astype(str)); tses=set(t['ses_ID'][:].astype(str)); uses=set(u['ses_ID'][:].astype(str))
    nsp=np.diff(np.r_[0,idx])
    return dict(path=x['path'], sub=h['general/subject/subject_id'][()].decode(), desc=h['session_description'][()].decode(), sid=h['general/session_id'][()].decode(),
        nunits=len(idx), nsua=int(u['is_sua'][:].sum()), pen=','.join(pen), tpen=','.join(tpen), tses=','.join(tses), uses=','.join(uses), ntr=len(t['start_time']),
        dmin=u['depth'][:].min(), dmax=u['depth'][:].max(), uid=tuple(u['unit_ID'][:].astype(int)), nsp=tuple(nsp), probe=set(u['probe_num'][:]),dev=h['general/devices/Neuropixels'].attrs['description'], sex=h['general/subject/sex'][()].decode(), age=h['general/subject/age'][()].decode(), cols=tuple(t.keys()))
t0=time.time()
with ThreadPoolExecutor(16) as ex: rows=list(ex.map(one,a))
print(time.time()-t0)
df=pd.DataFrame(rows); df.to_pickle('survey.pkl')
print(df.drop(columns=['uid','nsp','cols']).to_string())
EOF
python survey.py 2>&1 | tail -170
```

```
<persisted-output>
Output too large (31.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/50279903-1098-4fbe-8973-7b67441059b8/tool-results/btl1qfo31.txt

Preview (first 2KB):
133.40204095840454
                                                 path     sub                            desc         sid  nunits  nsua  pen tpen      tses      uses   ntr    dmin    dmax probe          dev sex   age
0    sub-Z08115/sub-Z08115_ses-20190726SL_ecephys.nwb  Z08115                 V4 shape screen  20190726SL      75    75  p05  p05  190726SL  190726SL  1569   300.0  2740.0   {0}  bank0_384ch   F  P12Y
1    sub-Z08115/sub-Z08115_ses-20190723SL_ecephys.nwb  Z08115                 V4 shape screen  20190723SL      41    41  p04  p04  190723SL  190723SL  1732    20.0  3000.0   {0}  bank0_384ch   F  P12Y
2    sub-Z08115/sub-Z08115_ses-20190717SL_ecephys.nwb  Z08115                 V4 shape screen  20190717SL      11    11  p01  p01  190717SL  190717SL  2178   740.0  3240.0   {0}  bank0_384ch   F  P12Y
3    sub-Z08115/sub-Z08115_ses-20190718SL_ecephys.nwb  Z08115                 V4 shape screen  20190718SL      69    69  p02  p02  190718SL  190718SL  2541   380.0  2340.0   {0}  bank0_384ch   F  P12Y
4    sub-Z08115/sub-Z08115_ses-20190719SL_ecephys.nwb  Z08115                 V4 shape screen  20190719SL      88    88  p03  p03  190719SL  190719SL  2090   320.0  3040.0   {0}  bank0_384ch   F  P12Y
5    sub-Z08115/sub-Z08115_ses-20190730SL_ecephys.nwb  Z08115                 V4 shape screen  20190730SL      41    41  p06  p06  190730SL  190730SL  2384   860.0  3040.0   {0}  bank0_384ch   F  P12Y
6    sub-Z08115/sub-Z08115_ses-20190802SL_ecephys.nwb  Z08115                 V4 shape screen  20190802SL      87    87  p09  p09  190802SL  190802SL  2247    20.0  2720.0   {0}  bank0_384ch   F  P12Y
7    sub-Z08115/sub-Z08115_ses-20190731SL_ecephys.nwb  Z08115                 V4 shape screen  20190731SL      80    80  p07  p07  190731SL  190731SL  2211  
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd
df=pd.read_pickle('survey.pkl')
df['kind']=df.sid.str[-2:]
print(df.groupby(['sub','kind']).agg(n=('sid','size'),units=('nunits','sum'),sua=('nsua','sum'),dev=('dev',lambda s:set(s)),desc=('desc',lambda s:set(s))))
print(df.cols.value_counts())
print('pen==tpen', (df.pen==df.tpen).all(), 'tses mismatch:'); print(df[df.tses!=df.sid.str[2:]][['sid','tses','uses']].to_string())
print(df[df.kind=='SL'].sort_values('sid')[['sub','sid','pen','nunits','dmin','dmax']].to_string())
# same-date units shared?
for d,g in df.groupby(df.sid.str[:8]):
    if len(g)>1:
        r=g.set_index('kind'); 
        ks=list(r.index)
        same=[ (k, r.loc[k,'uid']==r.loc[ks[0],'uid'], r.loc[k,'nsp']==r.loc[ks[0],'nsp']) for k in ks[1:]]
        print(d, ks, [r.loc[k,'nunits'] for k in ks], r.pen.tolist(), same)
" 2>&1 | head -200
```

```
n  units   sua            dev                              desc
sub    kind                                                                  
Z08115 SL    30   1167  1167  {bank0_384ch}                 {V4 shape screen}
       TX    17    461   461  {bank0_384ch}               {V4 texture screen}
Z11111 SL    44   1129  1129  {bank0_384ch}                 {V4 shape screen}
       SP    34    888   888  {bank0_384ch}  {V4 shape screen. position test}
       TX    34    884   884  {bank0_384ch}               {V4 texture screen}
cols
(cond_ID, id, luminance, pdOffTS, pdOnTS, pen_ID, rotation, ses_ID, start_time, stim_ID, stop_time, sub_ID)    74
(cond_ID, id, mode, pdOffTS, pdOnTS, pen_ID, ses_ID, start_time, stim_ID, stop_time, sub_ID)                   51
(cond_ID, id, pdOffTS, pdOnTS, pen_ID, position, ses_ID, start_time, stim_ID, stop_time, sub_ID)               34
Name: count, dtype: int64
pen==tpen True tses mismatch:
            sid      tses      uses
74   20210412SP  210412SL  210412SP
75   20210413SP  210413SL  210413SP
76   20210416SP  210416SL  210416SP
77   20210417SP  210417SL  210417SP
78   20210418SP  210418SL  210418SP
79   20210421SP  210421SL  210421SP
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat docs/design.md | sed -n 1,60p | head -5; ls tools; python tools/entry.py --help 2>&1 | head -20
```

```
Mon Nov  2 07:00:44 UTC 2026
# Reproduction registry: design

Status: draft for discussion. "Reproduction registry" is a working name.

## Goal
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 20,80p tools/entry.py; grep -n "def check_notebook\|embedded\|tag\|sanity" tools/entry.py | head -40
```

```
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
- no notebook or helper embeds a large literal array or an encoded image, or
  reads a figure from somewhere else.

`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
directory. The executed copies
go to --output-dir (default: executed/<name>/, which git ignores). A notebook
that takes longer than --max-minutes fails, even if it ran without error.

`handover` builds what a verifier is given in its first round
(docs/protocol.md): the executed notebooks with the conclusions removed (every
markdown cell that begins "**Result:" and everything from the "## Summary"
heading on), the helper modules and the claims files, in
executed/<name>/handover/. Run the entry first.

Requires `uv` on PATH, and `pyyaml`, `jsonschema` and `nbformat` to run this
script itself. The entry's own dependencies come only from its lock file.
"""
[... 49 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/001357-namima-2025/v4clusters.py",
 "content": "\"\"\"Loading and measures for dandiset 001357 (Namima et al. 2025, J Neurosci 45 e1893232024).\n\nWhere each parameter comes from:\n\n- DANDISET and VERSION: the most recent published version, the only one (the paper cites none).\n- WINDOW = (0.030, 0.200) s after the photodiode onset (`pdOnTS`): Materials and Methods, Data\n  analysis, Firing rate computation (\"computed within a 30-200 ms window after stimulus onset\");\n  photodiode onset from Experimental design (\"Stimulus onset times were based on photodiode\n  detection\").\n- Baseline: the same window on blank presentations (`cond_ID` 0), same passage (\"Baseline FRs were\n  similarly computed during blank stimulus presentations\").\n- RESPONSIVE_RATE = 5 spikes/s above baseline for one stimulus at either contrast: Materials and\n  Methods, Dataset and data inclusion criteria, paragraph 2.\n- Dark and bright shapes are `luminance` 4 and 12 cd/m2 (Visual stimuli: \"darker or brighter than\n  the background luminance (4 or 12 cd/m2)\"). The files also hold `luminance` 8, which the paper\n  does not use; it is left out.\n- Texture versions: `mode` 0 original, 1 contrast-reversed, 2 spectral noise (the column's own\n  description); mode 2 is not used in the paper and is left out.\n- Depth: the files give `depth`, \"distance from the electrode tip\", in 20 um steps (the position of\n  the unit's best channel), not the template center of mass of the Methods (Depth from the most\n  superficial neuron). Depth from the most superficial neuron is the largest `depth` of all good\n  units in the file minus the unit's `depth`; all units in the files are `is_sua` = 1 (good).\n- Noise-corrected correlation: Materials and Methods, Tuning similarity and contrast invariance,\n  after Pospisil and Bair (2021). Square-root transformed counts; the bias of the squared covariance\n  and of each variance is estimated from the trial-to-trial variance and subtracted; the root of\n  the quotient takes the sign of Pearson's r of the means and is truncated to [-1, 1]. The bias\n  terms are written here for unequal numbers of repeats per stimulus (the files have 3 to 10); with\n  equal repeats they reduce to the published terms. The noise variance of a neuron is the pooled\n  within-stimulus variance. Noise is taken as independent between the two response vectors, as in\n  Pospisil and Bair.\n- Bootstrap: 500 resamples of the repeats of each stimulus, with replacement (same passage). The\n  same repeat indices are used for all neurons of a session, since they were recorded together.\n  The interval is the 2.5 to 97.5 percentile, an assumption (the paper gives no level; 95% is the\n  level it uses for its regressions, as the claims file says). A value is unreliable when the\n  interval's width (reading a) or half-width (reading b) exceeds 0.5 (claims file, opening comment).\n- Isimilarity and Ssimilarity: ordinary least squares of a neuron's reliable similarities with the\n  other responsive neurons of its penetration against distance; 95% t intervals (MATLAB `confint`),\n  three or more points (Clusters of similarly tuned neurons).\n- Random seeds: each session and stimulus set has its own generator, seeded from its name, a\n  standard choice that cannot change a result beyond bootstrap noise.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport zlib\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom scipy import stats\n\nDANDISET = \"001357\"\nVERSION = \"0.261006.2007\"\nAPI = \"https://api.dandiarchive.org/api\"\nWINDOW = (0.030, 0.200)\nRESPONSIVE_RATE = 5.0\nN_BOOT = 500\nCI = (2.5, 97.5)\nDARK, BRIGHT = 4, 12\nMONKEY = {\"Z08115\": \"M1\", \"Z11111\": \"M2\"}\n\n\ndef list_assets() -> pd.DataFrame:\n    \"\"\"Every asset of the pinned version: path, asset id, size, subject, date and test kind.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=500\"\n    rows = []\n    while url:\n        page = requests.get(url, timeout=60).json()\n        rows += page[\"results\"]\n        url = page.get(\"next\")\n    df = pd.DataFrame([{\"path\": r[\"path\"], \"asset_id\": r[\"asset_id\"], \"size\": r[\"size\"]} for r in rows])\n    ses = df.path.str.extract(r\"sub-(\\w+)_ses-(\\d{8})(\\w\\w)_\")\n    df[\"subject\"], df[\"date\"], df[\"kind\"] = ses[0], ses[1], ses[2]\n    df[\"monkey\"] = df.subject.map(MONKEY)\n    return df.sort_values([\"subject\", \"date\", \"kind\"]).reset_index(drop=True)\n\n\ndef version_metadata() -> dict:\n    return requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/\", timeout=60).json()\n\n\ndef _s(x):\n    return x.decode() if isinstance(x, bytes) else x\n\n\ndef load_file(asset_id: str) -> dict:\n    \"\"\"Stream one NWB file and reduce it to spike counts in WINDOW for every unit and presentation.\"\"\"\n    f = h5py.File(remfile.File(f\"{API}/assets/{asset_id}/download/\"), \"r\")\n    t = f[\"intervals/trials\"]\n    trials = pd.DataFrame({c: t[c][:] for c in t.keys() if c != \"id\" and t[c].ndim == 1})\n    for c in (\"ses_ID\", \"pen_ID\", \"sub_ID\"):\n        trials[c] = trials[c].map(_s)\n    u = f[\"units\"]\n    units = pd.DataFrame({c: u[c][:] for c in (\"unit_ID\", \"depth\", \"best_ch\", \"is_sua\", \"probe_num\")})\n    for c in (\"ses_ID\", \"pen_ID\", \"sub_ID\"):\n        units[c] = [_s(x) for x in u[c][:]]\n    idx = u[\"spike_times_index\"][:]\n    st = u[\"spike_times\"][:]\n    onset = trials.pdOnTS.to_numpy()\n    counts = np.zeros((len(idx), len(onset)), dtype=np.int32)\n    sorted_ok = True\n    start = 0\n    for k, stop in enumerate(idx):\n        s = st[start:stop]\n        if np.any(np.diff(s) < 0):\n            sorted_ok = False\n            s = np.sort(s)\n        counts[k] = np.searchsorted(s, onset + WINDOW[1]) - np.searchsorted(s, onset + WINDOW[0])\n        start = stop\n    meta = {\n        \"session_id\": _s(f[\"general/session_id\"][()]),\n        \"description\": _s(f[\"session_description\"][()]),\n        \"subject\": _s(f[\"general/subject/subject_id\"][()]),\n        \"sex\": _s(f[\"general/subject/sex\"][()]),\n        \"start\": _s(f[\"session_start_time\"][()]),\n        \"device\": f[\"general/devices/Neuropixels\"].attrs.get(\"description\"),\n        \"n_spikes\": int(len(st)),\n        \"spike_range\": (float(st.min()) if len(st) else np.nan, float(st.max()) if len(st) else np.nan),\n        \"trial_range\": (float(trials.start_time.min()), float(trials.stop_time.max())),\n        \"spikes_sorted\": sorted_ok,\n        \"depth_unit\": u[\"depth\"].attrs.get(\"description\"),\n    }\n    units[\"depth0\"] = units.depth.max() - units.depth\n    return {\"meta\": meta, \"trials\": trials, \"units\": units, \"counts\": counts}\n\n\ndef load_many(asset_ids, threads: int = 16) -> list[dict]:\n    with ThreadPoolExecutor(threads) as ex:\n        return list(ex.map(load_file, asset_ids))\n\n\n# ---------------------------------------------------------------- stimulus arrays\n\n\ndef stim_array(counts: np.ndarray, keys: pd.DataFrame, order: list) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Counts arranged as (unit, stimulus, repeat), NaN-padded, for the stimuli in `order`.\n\n    `keys` holds one hashable stimulus key per presentation (a Series); returns the array and the\n    number of repeats per stimulus.\"\"\"\n    groups = {k: np.flatnonzero(keys.to_numpy() == np.array([k], dtype=object)[0]) if False else None for k in []}\n    key = keys.to_numpy()\n    pos = {k: [] for k in order}\n    for i, k in enumerate(key):\n        if k in pos:\n            pos[k].append(i)\n    nrep = np.array([len(pos[k]) for k in order])\n    R = nrep.max()\n    out = np.full((counts.shape[0], len(order), R), np.nan)\n    for j, k in enumerate(order):\n        out[:, j, : nrep[j]] = counts[:, pos[k]]\n    return out, nrep\n\n\ndef shape_arrays(sess: dict) -> dict:\n    \"\"\"Dark and bright arrays over the 120 shapes (stim_ID x rotation), and the blank counts.\"\"\"\n    tr = sess[\"trials\"]\n    key = pd.Series(list(zip(tr.stim_ID, tr.rotation)))\n    order = sorted({(s, r) for s, r in zip(tr.stim_ID, tr.rotation) if not np.isnan(s)})\n    out = {\"order\": order}\n    for name, lum in ((\"dark\", DARK), (\"bright\", BRIGHT)):\n        sel = (tr.luminance == lum).to_numpy()\n        out[name] = stim_array(sess[\"counts\"][:, sel], key[sel].reset_index(drop=True), order)\n    out[\"blank\"] = sess[\"counts\"][:, (tr.cond_ID == 0).to_numpy()]\n    return out\n\n\ndef texture_arrays(sess: dict) -> dict:\n    tr = sess[\"trials\"]\n    order = sorted(set(tr.stim_ID.dropna()))\n    out = {\"order\": order}\n    for name, mode in ((\"original\", 0), (\"reversed\", 1)):\n        sel = (tr[\"mode\"] == mode).to_numpy()\n        out[name] = stim_array(sess[\"counts\"][:, sel], tr.stim_ID[sel].reset_index(drop=True), order)\n    out[\"blank\"] = sess[\"counts\"][:, (tr.cond_ID == 0).to_numpy()]\n    return out\n\n\ndef position_arrays(sess: dict) -> dict:\n    tr = sess[\"trials\"]\n    order = sorted(set(tr.stim_ID.dropna()))\n    out = {\"order\": order, \"positions\": sorted(set(tr.position.dropna()))}\n    for p in out[\"positions\"]:\n        sel = (tr.position == p).to_numpy()\n        out[int(p)] = stim_array(sess[\"counts\"][:, sel], tr.stim_ID[sel].reset_index(drop=True), order)\n    out[\"blank\"] = sess[\"counts\"][:, (tr.cond_ID == 0).to_numpy()]\n    return out\n\n\ndef rates(arr: np.ndarray) -> np.ndarray:\n    \"\"\"Mean firing rate (spikes/s) per unit and stimulus.\"\"\"\n    return np.nanmean(arr, axis=2) / (WINDOW[1] - WINDOW[0])\n\n\ndef baseline(blank: np.ndarray) -> np.ndarray:\n    return blank.mean(axis=1) / (WINDOW[1] - WINDOW[0])\n\n\ndef responsive(arrays: list[np.ndarray], blank: np.ndarray) -> np.ndarray:\n    \"\"\"Responsive when one stimulus of any of `arrays` drives the mean rate RESPONSIVE_RATE above baseline.\"\"\"\n    base = baseline(blank)\n    peak = np.max([np.nanmax(rates(a), axis=1) for a in arrays], axis=0)\n    return peak - base >= RESPONSIVE_RATE\n\n\n# ---------------------------------------------------------------- noise-corrected correlation\n\n\ndef _moments(arr: np.ndarray, nrep: np.ndarray):\n    \"\"\"Means of sqrt counts (unit, stim), pooled noise variance (unit,), 1/n per stimulus.\"\"\"\n    x = np.sqrt(arr)\n    m = np.nanmean(x, axis=2)\n    v = np.nanvar(x, axis=2, ddof=1) if x.shape[2] > 1 else np.zeros_like(m)\n    df = nrep - 1\n    ok = df > 0\n    s2 = (v[:, ok] * df[ok]).sum(1) / df[ok].sum()\n    return m, s2, 1.0 / nrep\n\n\ndef nc_corr(mx, sx2, ix, my, sy2, iy, pairwise=True):\n    \"\"\"Noise-corrected correlation between rows of mx (a, m) and rows of my (b, m).\n\n    ix, iy: 1/n per stimulus (m,). pairwise=True gives the (a, b) matrix; False gives row by row\n    (a == b). Returns NaN where a variance estimate is not positive.\"\"\"\n    m = mx.shape[1]\n    xc = mx - mx.mean(1, keepdims=True)\n    yc = my - my.mean(1, keepdims=True)\n    sxx = (xc**2).sum(1) - sx2 * (1 - 1 / m) * ix.sum()\n    syy = (yc**2).sum(1) - sy2 * (1 - 1 / m) * iy.sum()\n    if pairwise:\n        sxy = xc @ yc.T\n        bias = (sx2[:, None] * ((yc**2) @ ix)[None, :] + sy2[None, :] * ((xc**2) @ iy)[:, None]\n                - sx2[:, None] * sy2[None, :] * (ix * iy).sum())\n        den = sxx[:, None] * syy[None, :]\n    else:\n        sxy = (xc * yc).sum(1)\n        bias = sx2 * ((yc**2) @ ix) + sy2 * ((xc**2) @ iy) - sx2 * sy2 * (ix * iy).sum()\n        den = sxx * syy\n    num = sxy**2 - bias\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        r2 = np.where(den > 0, num / den, np.nan)\n    r = np.sign(sxy) * np.sqrt(np.clip(r2, 0, None))\n    return np.clip(r, -1, 1)\n\n\ndef pearson_rows(mx, my):\n    xc = mx - mx.mean(1, keepdims=True)\n    yc = my - my.mean(1, keepdims=True)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        return (xc @ yc.T) / np.sqrt(np.outer((xc**2).sum(1), (yc**2).sum(1)))\n\n\ndef _resample(arr, nrep, rng):\n    m, R = arr.shape[1], arr.shape[2]\n    u = rng.random((m, R))\n    idx = np.floor(u * nrep[:, None]).astype(int)\n    out = arr[:, np.arange(m)[:, None], idx]\n    out[:, np.arange(R)[None, :] >= nrep[:, None]] = np.nan\n    return out\n\n\ndef seed_for(name: str) -> int:\n    return zlib.crc32(name.encode())\n\n\ndef similarity(arr, nrep, name, n_boot=N_BOOT):\n    \"\"\"Similarity matrix of all units of a session over one stimulus set, with its bootstrap interval.\n\n    Returns r (u, u), lo, hi (percentile interval).\"\"\"\n    rng = np.random.default_rng(seed_for(name))\n    mx, s2, inv = _moments(arr, nrep)\n    r = nc_corr(mx, s2, inv, mx, s2, inv)\n    boots = np.empty((n_boot,) + r.shape)\n    for b in range(n_boot):\n        mb, sb, _ = _moments(_resample(arr, nrep, rng), nrep)\n        boots[b] = nc_corr(mb, sb, inv, mb, sb, inv)\n    with np.errstate(invalid=\"ignore\"):\n        lo, hi = np.nanpercentile(boots, CI, axis=0)\n    nan_frac = np.isnan(boots).mean(0)\n    lo[nan_frac > 0.5] = np.nan\n    hi[nan_frac > 0.5] = np.nan\n    return r, lo, hi\n\n\ndef invariance(arr_x, n_x, arr_y, n_y, name, n_boot=N_BOOT):\n    \"\"\"Tuning invariance: noise-corrected correlation of each unit's responses to two versions.\"\"\"\n    rng = np.random.default_rng(seed_for(name))\n    mx, sx, ix = _moments(arr_x, n_x)\n    my, sy, iy = _moments(arr_y, n_y)\n    r = nc_corr(mx, sx, ix, my, sy, iy, pairwise=False)\n    boots = np.empty((n_boot, len(r)))\n    for b in range(n_boot):\n        a, sa, _ = _moments(_resample(arr_x, n_x, rng), n_x)\n        c, sc, _ = _moments(_resample(arr_y, n_y, rng), n_y)\n        boots[b] = nc_corr(a, sa, ix, c, sc, iy, pairwise=False)\n    with np.errstate(invalid=\"ignore\"):\n        lo, hi = np.nanpercentile(boots, CI, axis=0)\n    nan_frac = np.isnan(boots).mean(0)\n    lo[nan_frac > 0.5] = np.nan\n    hi[nan_frac > 0.5] = np.nan\n    return r, lo, hi\n\n\ndef reliable(r, lo, hi, reading: str) -> np.ndarray:\n    \"\"\"Reading 'a': interval width <= 0.5; reading 'b': half-width <= 0.5.\"\"\"\n    width = hi - lo\n    limit = 0.5 if reading == \"a\" else 1.0\n    with np.errstate(invalid=\"ignore\"):\n        return np.isfinite(r) & np.isfinite(width) & (width <= limit)\n\n\n# ---------------------------------------------------------------- Isimilarity\n\n\ndef regress(x, y):\n    \"\"\"OLS of y on x: intercept, slope and their 95% t intervals; None when fewer than 3 points.\"\"\"\n    n = len(x)\n    if n < 3 or np.ptp(x) == 0:\n        return None\n    X = np.column_stack([np.ones(n), x])\n    beta, *_ = np.linalg.lstsq(X, y, rcond=None)\n    resid = y - X @ beta\n    dof = n - 2\n    s2 = resid @ resid / dof if dof > 0 else np.nan\n    cov = s2 * np.linalg.inv(X.T @ X)\n    se = np.sqrt(np.diag(cov))\n    t = stats.t.ppf(0.975, dof) if dof > 0 else np.nan\n    return {\"n\": n, \"intercept\": beta[0], \"slope\": beta[1],\n            \"i_lo\": beta[0] - t * se[0], \"i_hi\": beta[0] + t * se[0],\n            \"s_lo\": beta[1] - t * se[1], \"s_hi\": beta[1] + t * se[1]}\n\n\ndef isimilarity(r, rel, depth0, keep):\n    \"\"\"One row per unit in `keep`: its regression of reliable similarities with the other kept units\n    on distance. NaN fields when it has fewer than three points.\"\"\"\n    idx = np.flatnonzero(keep)\n    rows = []\n    for i in idx:\n        others = idx[(idx != i) & rel[i, idx]]\n        fit = regress(np.abs(depth0[others] - depth0[i]), r[i, others])\n        row = {\"unit\": i, \"n_points\": len(others)}\n        if fit:\n            row.update(fit)\n        rows.append(row)\n    df = pd.DataFrame(rows)\n    for c in (\"intercept\", \"slope\", \"i_lo\", \"i_hi\", \"s_lo\", \"s_hi\"):\n        if c not in df:\n            df[c] = np.nan\n    df[\"has_line\"] = df.intercept.notna()\n    df[\"sig_pos\"] = df.i_lo > 0\n    df[\"sig_any\"] = (df.i_lo > 0) | (df.i_hi < 0)\n    df[\"slope_sig_pos\"] = df.s_lo > 0\n    return df\n\n\n# ---------------------------------------------------------------- AUC\n\n\ndef auc(pos, neg):\n    \"\"\"Area under the ROC curve: P(pos > neg) + P(tie)/2.\"\"\"\n    pos, neg = np.asarray(pos, float), np.asarray(neg, float)\n    if len(pos) == 0 or len(neg) == 0:\n        return np.nan\n    u = stats.mannwhitneyu(pos, neg, alternative=\"two-sided\").statistic\n    return u / (len(pos) * len(neg))\n"
}
```

```
File created successfully at: entries/001357-namima-2025/v4clusters.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001357-namima-2025/v4clusters.py",
 "old_string": "    groups = {k: np.flatnonzero(keys.to_numpy() == np.array([k], dtype=object)[0]) if False else None for k in []}\n    key = keys.to_numpy()",
 "new_string": "    key = keys.to_numpy()"
}
```

```
The file entries/001357-namima-2025/v4clusters.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/001357-namima-2025')
import v4clusters as V, numpy as np, pandas as pd
# synthetic test of nc_corr: true r 0.6, 5 reps
rng=np.random.default_rng(0); m=120; n=5
mu=rng.normal(0,1,m); nu=0.6*mu+0.8*rng.normal(0,1,m)
X=(mu[None,:,None]*0.5+3+rng.normal(0,0.7,(1,m,n))); Y=(nu[None,:,None]*0.5+3+rng.normal(0,0.7,(1,m,n)))
arr=np.concatenate([X,Y])**2; nrep=np.full(m,n)
r,lo,hi=V.similarity(arr,nrep,'test',200); print('nc',r[0,1],lo[0,1],hi[0,1]); print('pearson', V.pearson_rows(arr.mean(2)**0.5, arr.mean(2)**0.5)[0,1], np.corrcoef(mu,nu)[0,1])
a=V.list_assets(); print(a.groupby(['monkey','kind']).size())
t=time.time(); s=V.load_file(a[(a.kind=='SL')&(a.date=='20210414')].asset_id.iloc[0]); print(time.time()-t, s['meta'])
sa=V.shape_arrays(s); print(sa['dark'][0].shape, sa['dark'][1].min(), sa['dark'][1].max(), sa['bright'][1].min(), len(sa['order']), sa['blank'].shape)
resp=V.responsive([sa['dark'][0],sa['bright'][0]], sa['blank']); print('responsive', resp.sum(), len(resp))
t=time.time(); r,lo,hi=V.similarity(sa['dark'][0][resp], sa['dark'][1], 'x'); print('boot', time.time()-t)
EOF
python t1.py
```

```
nc 0.5437455659016632 0.24870086354627466 0.4912842254272172
pearson 0.3939185117570913 0.523490764347092
monkey  kind
M1      SL      30
        TX      17
M2      SL      44
        SP      34
        TX      34
dtype: int64
1.4129953384399414 {'session_id': '20210414SL', 'description': 'V4 shape screen', 'subject': 'Z11111', 'sex': 'M', 'start': '2021-04-14T10:30:00-07:00', 'device': 'bank0_384ch', 'n_spikes': 68846, 'spike_range': (671.079, 2989.687), 'trial_range': (671.1288486552813, 2989.69601016306), 'spikes_sorted': True, 'depth_unit': 'distance from the electrode tip'}
(30, 120, 5) 4 5 4 120 (30, 18)
responsive 24 30
boot 0.27724289894104004
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/001357-namima-2025')
import v4clusters as V, numpy as np, pandas as pd
a=V.list_assets()
for date in ['20210414','20191024']:
  s=V.load_file(a[(a.kind=='SL')&(a.date==date)].asset_id.iloc[0])
  sa=V.shape_arrays(s); resp=V.responsive([sa['dark'][0],sa['bright'][0]], sa['blank'])
  d0=s['units'].depth0.to_numpy()
  order=np.argsort(d0[resp],kind='stable'); print(date,'resp',resp.sum(),'span',np.ptp(d0[resp]))
  for c in ['dark','bright']:
    r,lo,hi=V.similarity(sa[c][0], sa[c][1], date+c)
    for rd in 'ab':
      rel=V.reliable(r,lo,hi,rd)
      df=V.isimilarity(r,rel,d0,resp)
      df['num']=np.argsort(np.argsort(d0[df.unit],kind='stable'),kind='stable')+1
      print(c,rd,'sigpos nums',sorted(df.num[df.sig_pos]), 'neg slope', (df.slope[df.sig_pos]<0).all(), 'lines',df.has_line.sum(), 'rel frac', rel[np.ix_(resp,resp)].mean())
  # pairs 3-8, 18-19
  idx=np.flatnonzero(resp)[order]
  for c in ['dark','bright']:
    r,lo,hi=V.similarity(sa[c][0], sa[c][1], date+c)
    if date=='20210414': print(c, 'r38', r[idx[2],idx[7]], 'd', abs(d0[idx[2]]-d0[idx[7]]), 'r1819', r[idx[17],idx[18]], abs(d0[idx[17]]-d0[idx[18]]))
EOF
python t2.py
```

```
20210414 resp 24 span 2340.0
dark a sigpos nums [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 16, 21, 22] neg slope True lines 24 rel frac 0.9895833333333334
dark b sigpos nums [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 21, 22] neg slope True lines 24 rel frac 1.0
bright a sigpos nums [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] neg slope True lines 24 rel frac 0.9965277777777778
bright b sigpos nums [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] neg slope True lines 24 rel frac 1.0
dark r38 0.7798088207567975 d 260.0 r1819 -0.0 80.0
bright r38 0.8940013754628444 d 260.0 r1819 -0.14444054094369305 80.0
20191024 resp 42 span 2580.0
dark a sigpos nums [7] neg slope True lines 42 rel frac 1.0
dark b sigpos nums [7] neg slope True lines 42 rel frac 1.0
bright a sigpos nums [7, 19, 26, 38] neg slope True lines 42 rel frac 0.9988662131519275
bright b sigpos nums [7, 19, 26, 38] neg slope True lines 42 rel frac 1.0
Shell cwd was reset to
```

**Agent calls ToolSearch**

```json
{
 "query": "select:WebSearch,WebFetch",
 "max_results": 2
}
```

Result: no output.

**Agent calls WebSearch**

```json
{
 "query": "Pasupathy Connor 2001 shape stimuli vertices github APC model curvature dataset"
}
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/001357-namima-2025 && python - <<'EOF'
p='v4clusters.py'; s=open(p).read()
old=s[s.index('def nc_corr('):s.index('def pearson_rows')]
new='''def nc_corr(mx, sx2, ix, my, sy2, iy, pairwise=True):
    """Noise-corrected correlation between rows of mx (a, m) and rows of my (b, m).

    ix, iy: 1/n per stimulus, (m,) or one row per unit (a, m) and (b, m). pairwise=True gives the
    (a, b) matrix; False gives row by row (a == b). NaN where a variance estimate is not positive."""
    m = mx.shape[1]
    ix = np.broadcast_to(ix, mx.shape)
    iy = np.broadcast_to(iy, my.shape)
    xc = mx - mx.mean(1, keepdims=True)
    yc = my - my.mean(1, keepdims=True)
    sxx = (xc**2).sum(1) - sx2 * (1 - 1 / m) * ix.sum(1)
    syy = (yc**2).sum(1) - sy2 * (1 - 1 / m) * iy.sum(1)
    if pairwise:
        sxy = xc @ yc.T
        bias = (sx2[:, None] * (ix @ (yc**2).T) + sy2[None, :] * ((xc**2) @ iy.T)
                - sx2[:, None] * sy2[None, :] * (ix @ iy.T))
        den = sxx[:, None] * syy[None, :]
    else:
        sxy = (xc * yc).sum(1)
        bias = sx2 * (ix * yc**2).sum(1) + sy2 * (iy * xc**2).sum(1) - sx2 * sy2 * (ix * iy).sum(1)
        den = sxx * syy
    num = sxy**2 - bias
    with np.errstate(invalid="ignore", divide="ignore"):
        r2 = np.where(den > 0, num / den, np.nan)
    r = np.sign(sxy) * np.sqrt(np.clip(r2, 0, None))
    return np.clip(r, -1, 1)


'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='v4clusters.py'; s=open(p).read()
s=s.replace('''        counts[k] = np.searchsorted(s, onset + WINDOW[1]) - np.searchsorted(s, onset + WINDOW[0])
        start = stop''','''        counts[k] = np.searchsorted(s, onset + WINDOW[1]) - np.searchsorted(s, onset + WINDOW[0])
        shifted[k] = np.searchsorted(s, onset + SHIFT + WINDOW[1]) - np.searchsorted(s, onset + SHIFT + WINDOW[0])
        start = stop''')
s=s.replace('''    counts = np.zeros((len(idx), len(onset)), dtype=np.int32)
''','''    counts = np.zeros((len(idx), len(onset)), dtype=np.int32)
    shifted = np.zeros_like(counts)
''')
s=s.replace('''    return {"meta": meta, "trials": trials, "units": units, "counts": counts}''','''    meta["unit_spikes"] = tuple(np.diff(np.r_[0, idx]).tolist())
    return {"meta": meta, "trials": trials, "units": units, "counts": counts, "shifted": shifted}''')
s=s.replace('''WINDOW = (0.030, 0.200)
''','''WINDOW = (0.030, 0.200)
SHIFT = -1.3  # s; onsets moved off the stimuli for the clock check, a standard choice
''')
s += '''

# ---------------------------------------------------------------- per-session analyses


def analyse_pair_sets(arrays: dict, names: tuple, keep: np.ndarray, depth0: np.ndarray, tag: str) -> dict:
    """Similarity matrices, reliability and Isimilarity tables for two stimulus versions of a session
    (dark and bright shapes, or original and reversed textures), and the invariance across them."""
    out = {"keep": keep, "depth0": depth0}
    for name in names:
        arr, nrep = arrays[name]
        r, lo, hi = similarity(arr[keep], nrep, f"{tag}-{name}")
        out[name] = {"r": r, "lo": lo, "hi": hi, "mean_sqrt": _moments(arr[keep], nrep)[0],
                     "rate": rates(arr[keep])}
        for rd in "ab":
            rel = reliable(r, lo, hi, rd)
            out[name][f"isim_{rd}"] = isimilarity(r, rel, depth0[keep], np.ones(keep.sum(), bool))
    (ax, nx), (ay, ny) = arrays[names[0]], arrays[names[1]]
    inv, ilo, ihi = invariance(ax[keep], nx, ay[keep], ny, f"{tag}-invariance")
    out["invariance"] = {"r": inv, "lo": ilo, "hi": ihi}
    return out


def neuron_table(res: dict, names: tuple) -> pd.DataFrame:
    """One row per kept neuron of a session: Isimilarity fields under each version and reliability
    reading, and the invariance with its reliability."""
    keep = res["keep"]
    df = pd.DataFrame({"unit": np.flatnonzero(keep), "depth0": res["depth0"][keep]})
    for name in names:
        for rd in "ab":
            t = res[name][f"isim_{rd}"].reset_index(drop=True)
            for c in ("intercept", "slope", "has_line", "sig_pos", "sig_any", "slope_sig_pos", "i_lo", "s_hi"):
                df[f"{c}_{name}_{rd}"] = t[c].to_numpy()
    inv = res["invariance"]
    df["invariance"] = inv["r"]
    for rd in "ab":
        df[f"inv_rel_{rd}"] = reliable(inv["r"], inv["lo"], inv["hi"], rd)
    return df
'''
open(p,'w').write(s)
EOF
date -u
```

```
Mon Nov  2 07:04:14 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > full.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/001357-namima-2025')
import importlib, v4clusters as V, numpy as np, pandas as pd
t0=time.time()
a=V.list_assets()
sess=V.load_many(a.asset_id.tolist())
print('load', time.time()-t0)
for s,(i,row) in zip(sess,a.iterrows()): s['asset']=row.to_dict()
t1=time.time()
shape={}
for s in sess:
    if s['asset']['kind']!='SL': continue
    sa=V.shape_arrays(s); keep=V.responsive([sa['dark'][0],sa['bright'][0]],sa['blank'])
    if keep.sum()==0: shape[s['asset']['date']+s['asset']['subject']]=None; continue
    res=V.analyse_pair_sets(sa,('dark','bright'),keep,s['units'].depth0.to_numpy(),s['meta']['session_id'])
    res['arrays']=sa; shape[(s['asset']['monkey'],s['asset']['date'])]=res
print('shape', time.time()-t1)
EOF
timeout 1200 python full.py
```

```
load 150.8571856021881
shape 89.77930426597595
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat >> full.py <<'EOF'
pickle.dump((a,sess,shape),open('cache.pkl','wb'))
EOF
timeout 1200 python full.py && ls -la cache.pkl
```

```
load 151.6569468975067
shape 89.89638614654541
-rw-r--r-- 1 runner runner 113331698 Nov  2 07:12 cache.pkl
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > ex1.py <<'EOF'
import sys, pickle; sys.path.insert(0,'entries/001357-namima-2025')
import v4clusters as V, numpy as np, pandas as pd
from scipy import stats
a,sess,shape=pickle.load(open('cache.pkl','rb'))
shape={k:v for k,v in shape.items() if v is not None and isinstance(k,tuple)}
rows=[]
for (mk,d),res in shape.items():
    t=V.neuron_table(res,('dark','bright')); t['monkey']=mk; t['date']=d; t['n_pen']=len(t); rows.append(t)
N=pd.concat(rows,ignore_index=True)
print('neurons',len(N), N.groupby('monkey').size().to_dict(), 'pens',N.date.nunique())
good={ (s['asset']['monkey'],s['asset']['date']):len(s['units']) for s in sess if s['asset']['kind']=='SL'}
print('good units', sum(good.values()))
P=N.groupby(['monkey','date']).size(); print('min max per pen', P.min(), P.max(), '>30:', (P>30).sum())
for rd in 'ab':
  for c in ['dark','bright','either']:
    if c=='either':
        line=N[f'has_line_dark_{rd}']|N[f'has_line_bright_{rd}']; sp=N[f'sig_pos_dark_{rd}']|N[f'sig_pos_bright_{rd}']
        neg=(N[f'sig_pos_dark_{rd}']&(N[f'slope_dark_{rd}']<0))|(N[f'sig_pos_bright_{rd}']&(N[f'slope_bright_{rd}']<0))
    else:
        line=N[f'has_line_{c}_{rd}']; sp=N[f'sig_pos_{c}_{rd}']; neg=sp&(N[f'slope_{c}_{rd}']<0)
    for nm,sel in [('i',sp),('ii',neg)]:
        g=N[sel].groupby('monkey').size().to_dict()
        pens=N[sel].groupby('date').size()
        print(rd,c,nm,'lines',line.sum(),'sig',sel.sum(),g,'notsig',(line&~sel).sum(),'pens>=1',len(pens),'>=5',(pens>=5).sum())
EOF
python ex1.py
```

```
neurons 1869 {'M1': 954, 'M2': 915} pens 74
good units 2296
min max per pen 1 77 >30: 20
a dark i lines 1729 sig 400 {'M1': 233, 'M2': 167} notsig 1329 pens>=1 58 >=5 27
a dark ii lines 1729 sig 394 {'M1': 228, 'M2': 166} notsig 1335 pens>=1 58 >=5 27
a bright i lines 1730 sig 386 {'M1': 230, 'M2': 156} notsig 1344 pens>=1 54 >=5 29
a bright ii lines 1730 sig 381 {'M1': 226, 'M2': 155} notsig 1349 pens>=1 54 >=5 29
a either i lines 1816 sig 563 {'M1': 330, 'M2': 233} notsig 1253 pens>=1 62 >=5 39
a either ii lines 1816 sig 555 {'M1': 323, 'M2': 232} notsig 1261 pens>=1 62 >=5 39
b dark i lines 1805 sig 453 {'M1': 272, 'M2': 181} notsig 1352 pens>=1 59 >=5 29
b dark ii lines 1805 sig 447 {'M1': 267, 'M2': 180} notsig 1358 pens>=1 59 >=5 29
b bright i lines 1799 sig 449 {'M1': 265, 'M2': 184} notsig 1350 pens>=1 56 >=5 29
b bright ii lines 1799 sig 443 {'M1': 261, 'M2': 182} notsig 1356 pens>=1 56 >=5 29
b either i lines 1847 sig 625 {'M1': 364, 'M2': 261} notsig 1222 pens>=1 62 >=5 41
b either ii lines 1847 sig 617 {'M1': 358, 'M2': 259} notsig 1230 pens>=1 62 >=5 40
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle,numpy as np
a,sess,shape=pickle.load(open('cache.pkl','rb'))
by={}
for s in sess: by.setdefault(s['asset']['date'],{})[s['asset']['kind']]=s
same=[ (d, all((v['units'].unit_ID.to_numpy()==g['SL']['units'].unit_ID.to_numpy()).all() for v in g.values())) for d,g in by.items() if 'SL' in g and len(g)>1]
print(all(x[1] for x in same), len(same))
s=by['20210512']['SP']; tr=s['trials']; print(tr.groupby(['position','stim_ID']).size().describe())
import collections
for s in sess:
  tr=s['trials']; d=(tr.pdOnTS-tr.start_time); e=tr.pdOffTS-tr.pdOnTS
print(min((s['trials'].pdOnTS-s['trials'].start_time).min() for s in sess), max((s['trials'].pdOnTS-s['trials'].start_time).max() for s in sess))
print(np.percentile(np.concatenate([(s['trials'].pdOffTS-s['trials'].pdOnTS).to_numpy() for s in sess]),[0,1,50,99,100]))
print(collections.Counter(tuple(sorted(s['trials'].luminance.unique())) for s in sess if s['asset']['kind']=='SL'))
"
```

```
True 37
count    75.0
mean      8.0
std       0.0
min       8.0
25%       8.0
50%       8.0
75%       8.0
max       8.0
dtype: float64
0.1499999999996362 0.15000000000009095
[0.04052025 0.19440122 0.21684172 0.23700002 0.57611848]
Counter({(np.int64(0), np.int64(4), np.int64(8), np.int64(12)): 73, (np.int64(0), np.int64(4), np.int64(12)): 1})
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "\"\"\"Builds the notebook from cells.py: cells separated by lines '# %% [markdown]' or '# %% tags=a,b'.\"\"\"\nimport re, sys, nbformat\n\nsrc = open(sys.argv[1]).read()\nout = sys.argv[2]\ncells = []\nfor block in re.split(r\"^# %%\", src, flags=re.M)[1:]:\n    head, _, body = block.partition(\"\\n\")\n    body = body.strip(\"\\n\")\n    tags = []\n    m = re.search(r\"tags=([\\w:,\\-]+)\", head)\n    if m:\n        tags = m.group(1).split(\",\")\n    if \"[markdown]\" in head:\n        text = \"\\n\".join(l[2:] if l.startswith(\"# \") else l.lstrip(\"#\") for l in body.splitlines())\n        c = nbformat.v4.new_markdown_cell(text)\n    else:\n        c = nbformat.v4.new_code_cell(body)\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\nnb = nbformat.v4.new_notebook(cells=cells)\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbformat.write(nb, out)\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells.py",
 "content": "# %% [markdown]\n# # Reproducing Namima et al. (2025) from dandiset 001357\n#\n# **Paper.** Namima, Kempkes, Zamarashkina, Owen and Pasupathy (2025), \"High-Density Recording Reveals\n# Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4\", J Neurosci 45(5)\n# e1893232024, doi:10.1523/jneurosci.1893-23.2024.\n#\n# **Dataset.** DANDI:001357, version 0.261006.2007 (doi:10.48324/dandi.001357/0.261006.2007), streamed\n# from the archive. The paper cites no version of the dataset. This is the only published version,\n# and so the most recent; the draft has the same 159 assets and size, and a draft can change, so the\n# published version is pinned.\n#\n# **Claims.** `claims/001357/10.1523-jneurosci.1893-23.2024.yaml`, written by a reader from the version\n# of record (main text, Methods and figure legends; the paper has no supplement) and checked by a\n# second reader.\n#\n# | Claim | Tested here |\n# |---|---|\n# | methods-sessions-and-neurons | tested |\n# | ex-m2p6-cluster | tested |\n# | ex-m2p6-pairs | tested |\n# | ex-m2p6-invariance | tested |\n# | ex-csd-sinks | blocked: the LF signal is not in the dataset |\n# | ex-m1p12-no-cluster | tested |\n# | ex-m1p12-strong-responses | tested |\n# | pop-significant-isimilarity | tested |\n# | pop-intercept-slope-correlation | tested |\n# | pop-dark-bright-consistent | tested |\n# | pop-contrast-invariance | tested |\n# | pop-sparse-across-penetrations | tested |\n# | pop-asymptote-20-percent | tested |\n# | pop-mean-isimilarity-yield | tested |\n# | pop-recording-density | tested |\n# | pop-within-vs-across-sessions | tested |\n# | orientation-sf-isimilarity | blocked: the shape images are not public |\n# | orientation-auc-coarse-clusters | tested |\n# | apc-peaks-sparse-clustering | blocked: the shapes' curvature descriptions are not public |\n# | apc-example-m2p51 | blocked: as apc-peaks-sparse-clustering |\n# | gyrus-penetrations-consistent | blocked: the dataset does not identify the 18 gyral penetrations |\n# | texture-sparse-clusters | tested |\n# | texture-original-reversed-consistent | tested |\n# | texture-asymptote-20-percent | tested |\n# | position-optimal-consistent | tested |\n# | position-examples-invariant | tested |\n# | simulation-random-with-domains | blocked: a simulation with unstated parameters, not a test on the data |\n#\n# Methods and the passage each comes from are in the docstring of `v4clusters.py`.\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport time\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport v4clusters as V\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nprint(\"dandiset\", V.DANDISET, \"version\", V.VERSION)\n\n# %% [markdown]\n# ## Data check\n#\n# Every file is streamed once and reduced, as it loads, to the spike count of every unit in the\n# 30 to 200 ms window after the photodiode onset of every presentation (and the same count with the\n# onsets moved by -1.3 s, for the clock check). The archive's metadata and the files' own fields are\n# printed and checked against the paper's description.\n\n# %%\nt0 = time.time()\nmeta = V.version_metadata()\nassets = V.list_assets()\nprint(meta[\"name\"])\nprint(\"version\", meta[\"version\"], \"| files\", meta[\"assetsSummary\"][\"numberOfFiles\"],\n      \"| subjects\", meta[\"assetsSummary\"][\"numberOfSubjects\"],\n      \"| variables\", meta[\"assetsSummary\"][\"variableMeasured\"])\nprint(meta[\"description\"][:600])\nprint()\nprint(assets.groupby([\"subject\", \"monkey\", \"kind\"]).size().rename(\"files\").to_string())\nsess = V.load_many(assets.asset_id.tolist())\nfor s, (_, row) in zip(sess, assets.iterrows()):\n    s[\"asset\"] = row.to_dict()\nprint(f\"loaded {len(sess)} files in {time.time() - t0:.0f} s\")\n\n# %% tags=sanity\ninfo = pd.DataFrame([{\n    \"monkey\": s[\"asset\"][\"monkey\"], \"kind\": s[\"asset\"][\"kind\"], \"date\": s[\"asset\"][\"date\"],\n    \"description\": s[\"meta\"][\"description\"], \"sex\": s[\"meta\"][\"sex\"], \"device\": s[\"meta\"][\"device\"],\n    \"pen\": \",\".join(sorted(set(s[\"units\"].pen_ID))), \"trial_pen\": \",\".join(sorted(set(s[\"trials\"].pen_ID))),\n    \"trial_ses\": \",\".join(sorted(set(s[\"trials\"].ses_ID))), \"units\": len(s[\"units\"]),\n    \"sua\": int(s[\"units\"].is_sua.sum()), \"presentations\": len(s[\"trials\"]),\n    \"depth_min\": s[\"units\"].depth.min(), \"depth_max\": s[\"units\"].depth.max(),\n    \"spikes_sorted\": s[\"meta\"][\"spikes_sorted\"],\n    \"spikes_in_trials\": (s[\"meta\"][\"spike_range\"][0] >= s[\"meta\"][\"trial_range\"][0] - 1)\n                        and (s[\"meta\"][\"spike_range\"][1] <= s[\"meta\"][\"trial_range\"][1] + 1),\n    \"onset_minus_start\": float((s[\"trials\"].pdOnTS - s[\"trials\"].start_time).median()),\n    \"pd_duration\": float((s[\"trials\"].pdOffTS - s[\"trials\"].pdOnTS).median()),\n} for s in sess])\nprint(\"Files by monkey and test, with good units (is_sua = 1) and presentations:\")\nprint(info.groupby([\"monkey\", \"kind\"]).agg(files=(\"date\", \"size\"), units=(\"units\", \"sum\"), sua=(\"sua\", \"sum\"),\n      presentations=(\"presentations\", \"sum\"), sexes=(\"sex\", lambda x: set(x)),\n      descriptions=(\"description\", lambda x: set(x))).to_string())\nprint()\nprint(\"All units are good (is_sua = 1):\", bool((info.units == info.sua).all()))\nprint(\"One penetration label per file, the same in units and trials:\", bool((info.pen == info.trial_pen).all()))\nsp_mislabel = info[(info.kind == \"SP\") & info.trial_ses.str.endswith(\"SL\")]\nprint(f\"Position-test files whose trial table names the session '...SL': {len(sp_mislabel)} of {(info.kind == 'SP').sum()}\")\nprint(\"Spike times sorted in every file:\", bool(info.spikes_sorted.all()),\n      \"| spikes within the trial span (1 s margin):\", int(info.spikes_in_trials.sum()), \"of\", len(info))\nprint(\"Unit depth, 'distance from the electrode tip' (um): range\", info.depth_min.min(), \"to\", info.depth_max.max())\nsteps = np.unique(np.concatenate([s[\"units\"].depth.to_numpy() % 20 for s in sess]))\nprint(\"Depth values modulo 20 um:\", steps)\nprint(\"Photodiode onset minus start_time (s): min\", info.onset_minus_start.min(), \"max\", info.onset_minus_start.max())\nprint(\"Photodiode ON to OFF (s), median per file: range\", info.pd_duration.min().round(3), \"to\", info.pd_duration.max().round(3))\nprint()\nfor kind, col in ((\"SL\", \"luminance\"), (\"TX\", \"mode\"), (\"SP\", \"position\")):\n    vals = pd.concat([s[\"trials\"][col] for s in sess if s[\"asset\"][\"kind\"] == kind]).value_counts(dropna=False).sort_index()\n    print(f\"{kind} presentations by {col}:\", vals.to_dict())\nfor kind in (\"SL\", \"TX\", \"SP\"):\n    st = pd.concat([s[\"trials\"].stim_ID for s in sess if s[\"asset\"][\"kind\"] == kind])\n    print(f\"{kind} stim_ID values:\", sorted(st.dropna().unique().astype(int).tolist()))\nrot = pd.concat([s[\"trials\"].rotation for s in sess if s[\"asset\"][\"kind\"] == \"SL\"])\nprint(\"SL rotations:\", sorted(rot.dropna().unique().tolist()))\n\n# repeats per stimulus\nrep = []\nfor s in sess:\n    k = s[\"asset\"][\"kind\"]\n    if k == \"SL\":\n        A = V.shape_arrays(s); rep += [(k, \"dark\", A[\"dark\"][1].min(), np.median(A[\"dark\"][1])), (k, \"bright\", A[\"bright\"][1].min(), np.median(A[\"bright\"][1]))]\n    elif k == \"TX\":\n        A = V.texture_arrays(s); rep += [(k, \"original\", A[\"original\"][1].min(), np.median(A[\"original\"][1])), (k, \"reversed\", A[\"reversed\"][1].min(), np.median(A[\"reversed\"][1]))]\n    else:\n        A = V.position_arrays(s); rep += [(k, \"all positions\", min(A[p][1].min() for p in range(5)), np.median(A[0][1]))]\nrep = pd.DataFrame(rep, columns=[\"kind\", \"version\", \"min_repeats\", \"median_repeats\"])\nprint()\nprint(\"Repeats per stimulus (per file, the minimum and the median):\")\nprint(rep.groupby([\"kind\", \"version\"]).agg(min_of_min=(\"min_repeats\", \"min\"), median_of_median=(\"median_repeats\", \"median\")).to_string())\n\n# %% [markdown]\n# Units shared between files. On days with more than one test (M2), the shape, texture and position\n# files hold the same units (same `unit_ID`, same order) with the spikes of their own block. No two\n# files hold the same spike trains, so no recording is deposited twice; a unit is counted once per\n# test.\n\n# %% tags=sanity\nby_date = {}\nfor s in sess:\n    by_date.setdefault((s[\"asset\"][\"monkey\"], s[\"asset\"][\"date\"]), {})[s[\"asset\"][\"kind\"]] = s\nmulti = {k: g for k, g in by_date.items() if len(g) > 1}\nsame_ids = all((g[x][\"units\"].unit_ID.to_numpy() == next(iter(g.values()))[\"units\"].unit_ID.to_numpy()).all()\n               for g in multi.values() for x in g)\nprint(f\"Days with more than one test: {len(multi)}; same unit_IDs in every file of the day: {same_ids}\")\nsig = pd.Series([(tuple(s[\"units\"].unit_ID), s[\"meta\"][\"unit_spikes\"]) for s in sess])\nprint(\"Files with identical unit ids and spike counts per unit as another file:\", int(sig.duplicated(keep=False).sum()))\ndays = pd.DataFrame([{\"monkey\": m, \"date\": d, \"tests\": \"+\".join(sorted(g))} for (m, d), g in by_date.items()])\nprint(days.groupby([\"monkey\", \"tests\"]).size().rename(\"days\").to_string())\n\n# %% [markdown]\n# Clock check. If spikes and presentations share a clock, units fire more in the 30 to 200 ms window\n# after a stimulus than after a blank presentation. With the onsets moved by -1.3 s the same contrast\n# should vanish.\n\n# %% tags=sanity\nclock = []\nfor s in sess:\n    blank = (s[\"trials\"].cond_ID == 0).to_numpy()\n    if blank.sum() == 0 or (~blank).sum() == 0:\n        continue\n    d_true = (s[\"counts\"][:, ~blank].mean(1) - s[\"counts\"][:, blank].mean(1)) / 0.17\n    d_shift = (s[\"shifted\"][:, ~blank].mean(1) - s[\"shifted\"][:, blank].mean(1)) / 0.17\n    clock.append({\"kind\": s[\"asset\"][\"kind\"], \"date\": s[\"asset\"][\"date\"], \"true\": np.median(d_true),\n                  \"shifted\": np.median(d_shift),\n                  \"p_true\": stats.wilcoxon(d_true).pvalue if np.any(d_true) and len(d_true) > 1 else np.nan})\nclock = pd.DataFrame(clock)\nprint(\"Median over units of stimulus minus blank rate (spikes/s), per file:\")\nprint(clock.groupby(\"kind\").agg(files=(\"date\", \"size\"), true_median=(\"true\", \"median\"), true_min=(\"true\", \"min\"),\n      shifted_median=(\"shifted\", \"median\"), shifted_min=(\"shifted\", \"min\"), shifted_max=(\"shifted\", \"max\"),\n      files_true_positive=(\"true\", lambda x: int((x > 0).sum()))).to_string())\nprint(\"Files with true-onset contrast not above 0:\", clock[clock.true <= 0][[\"kind\", \"date\", \"true\"]].to_dict(\"records\"))\n\n# %% [markdown]\n# ### Shape analyses for every penetration\n#\n# Responsive neurons, similarity matrices over the 120 dark and the 120 bright shapes with their\n# bootstrap intervals, Isimilarity and Ssimilarity under both reliability readings, and the tuning\n# invariance between dark and bright. The neuron table `N` has one row per responsive neuron.\n\n# %%\nt0 = time.time()\nshape = {}\nfor s in sess:\n    if s[\"asset\"][\"kind\"] != \"SL\":\n        continue\n    A = V.shape_arrays(s)\n    keep = V.responsive([A[\"dark\"][0], A[\"bright\"][0]], A[\"blank\"])\n    key = (s[\"asset\"][\"monkey\"], s[\"asset\"][\"date\"])\n    res = {\"keep\": keep, \"pen\": s[\"units\"].pen_ID.iloc[0], \"good\": len(keep), \"arrays\": A,\n           \"depth0\": s[\"units\"].depth0.to_numpy(), \"units\": s[\"units\"]}\n    if keep.sum() >= 1:\n        res.update(V.analyse_pair_sets(A, (\"dark\", \"bright\"), keep, res[\"depth0\"], s[\"meta\"][\"session_id\"]))\n    shape[key] = res\nrows = []\nfor (mk, d), res in shape.items():\n    if res[\"keep\"].sum() == 0:\n        continue\n    t = V.neuron_table(res, (\"dark\", \"bright\"))\n    t[\"monkey\"], t[\"date\"], t[\"pen\"] = mk, d, res[\"pen\"]\n    t[\"n_pen\"] = len(t)\n    rows.append(t)\nN = pd.concat(rows, ignore_index=True)\nprint(f\"shape analyses in {time.time() - t0:.0f} s; {len(N)} responsive neurons in {N.date.nunique()} penetrations\")\nrel_frac = {rd: np.mean([V.reliable(r[\"dark\"][\"r\"], r[\"dark\"][\"lo\"], r[\"dark\"][\"hi\"], rd)[~np.eye(r[\"keep\"].sum(), dtype=bool)].mean()\n                         for r in shape.values() if r[\"keep\"].sum() > 1]) for rd in \"ab\"}\nprint(\"Mean fraction of reliable off-diagonal dark similarities per penetration:\", {k: round(v, 3) for k, v in rel_frac.items()})\n\n\ndef readings(N, rd, contrast, slope_rule, suffix=(\"dark\", \"bright\")):\n    \"\"\"Masks (has a line, counted) for one reading: reliability rd, contrast, slope rule i or ii.\"\"\"\n    d, b = suffix\n    def one(c):\n        line = N[f\"has_line_{c}_{rd}\"]\n        sel = N[f\"sig_pos_{c}_{rd}\"]\n        if slope_rule == \"ii\":\n            sel = sel & (N[f\"slope_{c}_{rd}\"] < 0)\n        return line, sel\n    if contrast == \"either\":\n        (l1, s1), (l2, s2) = one(d), one(b)\n        return l1 | l2, s1 | s2\n    return one(contrast)\n\n# %% [markdown]\n# ## methods-sessions-and-neurons\n#\n# > The shape test was run in 30 sessions in M1 and 44 in M2, the texture test in 17 and 34, and the\n# > position control in 33 M2 sessions; the responsiveness criterion excluded 461 and 366 neurons and\n# > left 1,850 neurons for shape and 979 for texture analyses.\n#\n# Texture responsiveness uses the 40 original and 40 contrast-reversed textures (the paper's two\n# \"contrast levels\" for textures); the files' third version (spectral noise) is left out.\n\n# %%\nt0 = time.time()\ntexture = {}\nfor s in sess:\n    if s[\"asset\"][\"kind\"] != \"TX\":\n        continue\n    A = V.texture_arrays(s)\n    keep = V.responsive([A[\"original\"][0], A[\"reversed\"][0]], A[\"blank\"])\n    key = (s[\"asset\"][\"monkey\"], s[\"asset\"][\"date\"])\n    res = {\"keep\": keep, \"pen\": s[\"units\"].pen_ID.iloc[0], \"good\": len(keep), \"arrays\": A,\n           \"depth0\": s[\"units\"].depth0.to_numpy()}\n    if keep.sum() >= 1:\n        res.update(V.analyse_pair_sets(A, (\"original\", \"reversed\"), keep, res[\"depth0\"], s[\"meta\"][\"session_id\"]))\n    texture[key] = res\nrowsT = []\nfor (mk, d), res in texture.items():\n    if res[\"keep\"].sum() == 0:\n        continue\n    t = V.neuron_table(res, (\"original\", \"reversed\"))\n    t[\"monkey\"], t[\"date\"], t[\"pen\"] = mk, d, res[\"pen\"]\n    t[\"n_pen\"] = len(t)\n    rowsT.append(t)\nT = pd.concat(rowsT, ignore_index=True)\nprint(f\"texture analyses in {time.time() - t0:.0f} s\")\n\n# %% tags=claim:methods-sessions-and-neurons\nses_counts = assets.groupby([\"monkey\", \"kind\"]).size()\ngood_shape = sum(r[\"good\"] for r in shape.values())\ngood_tex = sum(r[\"good\"] for r in texture.values())\nvals = {\n    \"shape sessions, M1\": (ses_counts[(\"M1\", \"SL\")], 30, 3),\n    \"shape sessions, M2\": (ses_counts[(\"M2\", \"SL\")], 44, 4.4),\n    \"texture sessions, M1\": (ses_counts[(\"M1\", \"TX\")], 17, 1.7),\n    \"texture sessions, M2\": (ses_counts[(\"M2\", \"TX\")], 34, 3.4),\n    \"position control sessions, M2\": (ses_counts[(\"M2\", \"SP\")], 33, 3.3),\n    \"responsive neurons, shape\": (len(N), 1850, 185),\n    \"responsive neurons, texture\": (len(T), 979, 97.9),\n    \"excluded neurons, shape\": (good_shape - len(N), 461, 46.1),\n    \"excluded neurons, texture\": (good_tex - len(T), 366, 36.6),\n}\ntab = pd.DataFrame([{\"quantity\": k, \"measured\": v[0], \"expected\": v[1], \"tolerance\": v[2],\n                     \"within\": abs(v[0] - v[1]) <= v[2]} for k, v in vals.items()])\nprint(tab.to_string(index=False))\nprint()\nprint(\"Good units: shape\", good_shape, \"(paper 1,850 + 461 = 2,311); texture\", good_tex, \"(paper 979 + 366 = 1,345)\")\nprint(\"Responsive by monkey, shape:\", N.groupby(\"monkey\").size().to_dict(), \"| texture:\", T.groupby(\"monkey\").size().to_dict())\nprint(\"Penetrations with no responsive shape neuron:\", [(k, r[\"good\"]) for k, r in shape.items() if r[\"keep\"].sum() == 0])\nsp_dates = set(assets[assets.kind == \"SP\"].date)\nprint(\"Position-test days and their good units:\", sorted((d, len(by_date[(\"M2\", d)][\"SP\"][\"units\"])) for d in sp_dates))\ntx2 = set(assets[(assets.kind == \"TX\") & (assets.monkey == \"M2\")].date)\nsl2 = set(assets[(assets.kind == \"SL\") & (assets.monkey == \"M2\")].date)\nprint(f\"M2 texture days that also have a shape file: {len(tx2 & sl2)} of {len(tx2)}; texture-only days: {sorted(tx2 - sl2)}\")\n\n# %% [markdown]\n# **Result: reproduced.** Every session count matches the paper except the position control, 34\n# files against 33 (within the tolerance of 3.3); one of the 34 holds a single unit. Responsive and\n# excluded counts are within tolerance for both tests (see the table above). The good units of the\n# texture files sum to the paper's 979 + 366 exactly; the shape files hold 15 fewer than the\n# paper's 1,850 + 461.\n\n# %% [markdown]\n# ## Finding the example penetrations\n#\n# The claims file's readings: (a) the sixth M2 session in recording order among shape sessions,\n# (b) the sixth among all M2 sessions, (c) the session the dataset labels with the penetration\n# number. The same for M1p12 (twelfth), M2p9, M2p28, M2p51 and M1p5. A reading is accepted when its\n# responsive-neuron count is within 10% of the paper's.\n\n# %%\ndef find_pen(monkey, number, expected):\n    sl = sorted(assets[(assets.monkey == monkey) & (assets.kind == \"SL\")].date)\n    alld = sorted(set(assets[assets.monkey == monkey].date))\n    cand = {\"a\": sl[number - 1] if number <= len(sl) else None,\n            \"b\": alld[number - 1] if number <= len(alld) else None,\n            \"c\": next((d for (m, d), r in shape.items() if m == monkey and r[\"pen\"] == f\"p{number:02d}\"), None)}\n    rows = []\n    for rd, d in cand.items():\n        n = int(shape[(monkey, d)][\"keep\"].sum()) if d in sl else None\n        rows.append({\"reading\": rd, \"date\": d, \"label\": shape[(monkey, d)][\"pen\"] if d in sl else None,\n                     \"responsive\": n, \"accepted\": n is not None and abs(n - expected) <= 0.1 * expected})\n    return pd.DataFrame(rows)\n\nexamples = {\"M2p6\": (\"M2\", 6, 24), \"M1p12\": (\"M1\", 12, 42), \"M2p9\": (\"M2\", 9, 16), \"M2p28\": (\"M2\", 28, 55),\n            \"M2p51\": (\"M2\", 51, 33), \"M1p5\": (\"M1\", 5, None)}\nfound = {}\nfor name, (mk, num, exp) in examples.items():\n    f = find_pen(mk, num, exp if exp else 1)\n    print(name, \"(paper's count:\", exp, \")\")\n    print(f.to_string(index=False))\n    found[name] = (mk, f.set_index(\"reading\").loc[\"c\", \"date\"])\n\n# %% [markdown]\n# ## ex-m2p6-cluster\n#\n# > In penetration M2p6, 24 well-isolated neurons were recorded over about 2,400 um; a group of\n# > superficial neurons (1 to 9, over 540 um) had similar shape tuning at both contrasts, and with dark\n# > shapes neurons 1 to 9, 14 and 17 had a significant positive Isimilarity with a negative slope,\n# > while most other, deeper neurons did not.\n#\n# Neurons are numbered by depth from the most superficial (Figure 2A legend); units at the same depth\n# keep the file's order.\n\n# %% tags=claim:ex-m2p6-cluster\nkey = found[\"M2p6\"]\nres = shape[key]\nt = N[(N.monkey == key[0]) & (N.date == key[1])].copy()\nt[\"num\"] = np.argsort(np.argsort(t.depth0.to_numpy(), kind=\"stable\"), kind=\"stable\") + 1\nt = t.sort_values(\"num\")\nprint(\"M2p6 =\", key, \"| responsive neurons\", len(t), \"| span of depths\", np.ptp(t.depth0), \"um\")\nprint(\"Depth of neurons 1 and 9:\", t.depth0.iloc[0], t.depth0.iloc[8], \"-> extent\", t.depth0.iloc[8] - t.depth0.iloc[0], \"um\")\npaper_set = set(range(1, 10)) | {14, 17}\nfor c in (\"dark\", \"bright\"):\n    for rd in \"ab\":\n        sig = t[t[f\"sig_pos_{c}_{rd}\"]]\n        got = set(sig.num)\n        print(f\"{c}, reliability {rd}: significant positive Isimilarity, neurons {sorted(got)} ({len(got)}); \"\n              f\"slopes negative for {int((sig[f'slope_{c}_{rd}'] < 0).sum())} of {len(sig)}; \"\n              f\"missing from the paper's set {sorted(paper_set - got)}, added {sorted(got - paper_set)}\")\nr = res[\"dark\"][\"r\"]\norder = np.argsort(res[\"depth0\"][res[\"keep\"]], kind=\"stable\")\nrr = r[np.ix_(order, order)]\nprint(\"Mean dark similarity among neurons 1-9 (off-diagonal):\", np.round(np.nanmean(rr[:9, :9][~np.eye(9, dtype=bool)]), 3),\n      \"| between 1-9 and 10-24:\", np.round(np.nanmean(rr[:9, 9:]), 3), \"| among 10-24:\",\n      np.round(np.nanmean(rr[9:, 9:][~np.eye(15, dtype=bool)]), 3))\nrb = res[\"bright\"][\"r\"][np.ix_(order, order)]\nprint(\"Same, bright:\", np.round(np.nanmean(rb[:9, :9][~np.eye(9, dtype=bool)]), 3), np.round(np.nanmean(rb[:9, 9:]), 3),\n      np.round(np.nanmean(rb[9:, 9:][~np.eye(15, dtype=bool)]), 3))\nprint(t[[\"num\", \"depth0\", \"intercept_dark_a\", \"i_lo_dark_a\", \"slope_dark_a\", \"sig_pos_dark_a\", \"intercept_bright_a\", \"sig_pos_bright_a\"]].round(3).to_string(index=False))\nfig, ax = plt.subplots(1, 2, figsize=(9, 4))\nfor k, (c, m) in enumerate(((\"dark\", rr), (\"bright\", rb))):\n    im = ax[k].imshow(m, vmin=-1, vmax=1, cmap=\"RdBu_r\")\n    ax[k].set_title(f\"M2p6 similarity, {c} (range {np.nanmin(m):.2f} to {np.nanmax(m):.2f})\")\n    ax[k].set_xlabel(\"neuron\"); ax[k].set_ylabel(\"neuron\")\nplt.colorbar(im, ax=ax); plt.show()\n\n# %% [markdown]\n# **Result: partially reproduced.** Penetration p06 of M2 has 24 responsive neurons spanning\n# 2,340 um, and neurons 1 to 9 form a group of similar tuning at both contrasts. With dark shapes\n# 14 neurons (reading a) or 13 (reading b) have a significant positive Isimilarity, all with negative\n# slopes; they include neurons 1 to 9 and 14 but not 17, and add 12, 16, 21 and 22 (or 12, 21, 22),\n# more than the one-neuron tolerance allows.\n\n# %% [markdown]\n# ## ex-m2p6-pairs\n#\n# > In M2p6, neurons 3 and 8, 260 um apart, have tuning similarity 0.82 at both contrasts, while\n# > neurons 18 and 19, 80 um apart, have similarity 0.00 (dark) and -0.25 (bright).\n#\n# The files give each unit's best-channel position, the contact nearest the waveform's center\n# (Figure 2A legend), which is the claim's main reading of distance; the template center of mass is\n# not in the files, so the variant cannot be run.\n\n# %% tags=claim:ex-m2p6-pairs\nidx = np.flatnonzero(res[\"keep\"])[order]\nd0 = res[\"depth0\"]\ndef pair(i, j, c):\n    k = np.flatnonzero(res[\"keep\"])\n    a_, b_ = np.searchsorted(k, idx[i - 1]), np.searchsorted(k, idx[j - 1])\n    return res[c][\"r\"][a_, b_], res[c][\"lo\"][a_, b_], res[c][\"hi\"][a_, b_]\nvals = [(\"similarity 3 and 8, dark\", pair(3, 8, \"dark\")[0], 0.82, 0.082),\n        (\"similarity 3 and 8, bright\", pair(3, 8, \"bright\")[0], 0.82, 0.082),\n        (\"similarity 18 and 19, dark\", pair(18, 19, \"dark\")[0], 0.0, 0.1),\n        (\"similarity 18 and 19, bright\", pair(18, 19, \"bright\")[0], -0.25, 0.025),\n        (\"distance 3 and 8 (um)\", abs(d0[idx[2]] - d0[idx[7]]), 260, 26),\n        (\"distance 18 and 19 (um)\", abs(d0[idx[17]] - d0[idx[18]]), 80, 8)]\ntab = pd.DataFrame(vals, columns=[\"quantity\", \"measured\", \"expected\", \"tolerance\"])\ntab[\"within\"] = (tab.measured - tab.expected).abs() <= tab.tolerance\nprint(tab.round(3).to_string(index=False))\nfor (i, j) in ((3, 8), (18, 19)):\n    for c in (\"dark\", \"bright\"):\n        r_, lo_, hi_ = pair(i, j, c)\n        k = np.flatnonzero(res[\"keep\"])\n        a_, b_ = np.searchsorted(k, idx[i - 1]), np.searchsorted(k, idx[j - 1])\n        p = stats.pearsonr(res[c][\"rate\"][a_], res[c][\"rate\"][b_])[0]\n        print(f\"neurons {i} and {j}, {c}: noise-corrected {r_:.3f}, bootstrap interval {lo_:.3f} to {hi_:.3f}; Pearson r of mean rates {p:.3f}\")\nprint(\"Neighbouring pairs among 17 to 20:\", [(a, b, round(pair(a, b, 'bright')[0], 3)) for a, b in ((17, 18), (17, 19), (18, 20), (19, 20))])\n\n# %% [markdown]\n# **Result: partially reproduced.** Neurons 3 and 8 are 260 um apart with similarity 0.78 (dark) and\n# 0.89 (bright), and neurons 18 and 19 are 80 um apart with dark similarity 0.00; all within\n# tolerance. The bright similarity of 18 and 19 is -0.14, outside -0.25 +/- 0.025.\n\n# %% [markdown]\n# ## ex-m2p6-invariance\n#\n# > In M2p6, shape tuning was contrast-invariant (invariance above 0.5) for 19 of the 24 neurons.\n#\n# Unreliable invariance counts as not above 0.5 (claims file).\n\n# %% tags=claim:ex-m2p6-invariance\nfor rd in \"ab\":\n    n_hi = int(((t.invariance > 0.5) & t[f\"inv_rel_{rd}\"]).sum())\n    print(f\"reliability {rd}: {n_hi} of {len(t)} neurons with reliable invariance above 0.5 (expected 19 +/- 1.9); \"\n          f\"unreliable {int((~t[f'inv_rel_{rd}']).sum())}\")\nprint(\"Invariance values above 0.5 regardless of reliability:\", int((t.invariance > 0.5).sum()))\nprint(\"Invariance by Isimilarity significance (dark, a): median\", t.groupby(\"sig_pos_dark_a\").invariance.median().round(3).to_dict())\nprint(t[[\"num\", \"invariance\", \"inv_rel_a\", \"inv_rel_b\"]].round(3).T.to_string())\n\n# %% [markdown]\n# **Result: reproduced.** 19 of the 24 neurons have a reliable invariance above 0.5 under both\n# reliability readings, among neurons with and without a significant Isimilarity.\n\n# %% [markdown]\n# ## ex-m1p12-no-cluster\n#\n# > In penetration M1p12, 42 neurons over 2,580 um showed no clustered shape tuning at either\n# > contrast; only one neuron had a significant Isimilarity, although most had high contrast\n# > invariance of shape tuning.\n\n# %% tags=claim:ex-m1p12-no-cluster\nkey12 = found[\"M1p12\"]\nt12 = N[(N.monkey == key12[0]) & (N.date == key12[1])].copy()\nprint(\"M1p12 =\", key12, \"| responsive\", len(t12), \"| span\", np.ptp(t12.depth0), \"um\")\nfor c in (\"dark\", \"bright\"):\n    for rd in \"ab\":\n        print(f\"{c}, reliability {rd}: significant positive Isimilarity {int(t12[f'sig_pos_{c}_{rd}'].sum())}, \"\n              f\"significant either sign {int(t12[f'sig_any_{c}_{rd}'].sum())}, lines {int(t12[f'has_line_{c}_{rd}'].sum())}\")\nfor rd in \"ab\":\n    n_hi = int(((t12.invariance > 0.5) & t12[f\"inv_rel_{rd}\"]).sum())\n    print(f\"reliability {rd}: reliable invariance above 0.5 for {n_hi} of {len(t12)} ({n_hi / len(t12):.0%}); unreliable {int((~t12[f'inv_rel_{rd}']).sum())}\")\nprint(\"Median invariance:\", round(t12.invariance.median(), 3))\n\n# %% [markdown]\n# **Result: reproduced.** The labelled p12 of M1 has 42 responsive neurons over 2,580 um. With dark\n# shapes one neuron has a significant Isimilarity under both readings (four with bright shapes),\n# and 33 of 42 (79%) have reliable invariance above 0.5.\n\n# %% [markdown]\n# ## ex-m1p12-strong-responses\n#\n# > In M1p12, peak responses exceeded 15 spikes/s in 28 neurons for dark and 26 for bright shapes.\n\n# %% tags=claim:ex-m1p12-strong-responses\nr12 = shape[key12]\nbase = V.baseline(r12[\"arrays\"][\"blank\"])[r12[\"keep\"]]\nfor c, exp in ((\"dark\", 28), (\"bright\", 26)):\n    peak = r12[c][\"rate\"].max(1)\n    print(f\"{c}: peak above 15 spikes/s, (a) baseline-subtracted {int((peak - base > 15).sum())}, (b) raw {int((peak > 15).sum())}; \"\n          f\"expected {exp} +/- {exp * 0.1:.1f}; peaks {peak.min():.1f} to {peak.max():.1f} spikes/s\")\n\n# %% [markdown]\n# **Result: reproduced.** See the counts above: under reading (a), baseline-subtracted, both counts\n# are within tolerance.\n\n# %% [markdown]\n# ## pop-significant-isimilarity\n#\n# > Of 1,850 neurons in 74 sessions (6 to 76 per penetration), a minority, 344 (203 in M1, 141 in M2),\n# > had a significantly positive Isimilarity with a negative Ssimilarity; the majority (1,504) had an\n# > Isimilarity not significantly above zero.\n#\n# Readings: contrast (dark, bright, either) x reliability (a, b) x slope rule (i: significant positive\n# intercept; ii: and a negative slope). \"Not significant\" counts neurons with a line and no\n# significant positive intercept.\n\n# %% tags=claim:pop-significant-isimilarity\nP = N.groupby([\"monkey\", \"date\"]).size()\nprint(\"Responsive neurons per penetration: min\", P.min(), \"max\", P.max(), \"| penetrations\", len(P))\nprint(\"Smallest penetrations:\", P.nsmallest(4).to_dict())\nrows = []\nfor c in (\"dark\", \"bright\", \"either\"):\n    for rd in \"ab\":\n        for sr in (\"i\", \"ii\"):\n            line, sel = readings(N, rd, c, sr)\n            g = N[sel].groupby(\"monkey\").size()\n            rows.append({\"contrast\": c, \"reliability\": rd, \"slope\": sr, \"lines\": int(line.sum()), \"significant\": int(sel.sum()),\n                         \"M1\": int(g.get(\"M1\", 0)), \"M2\": int(g.get(\"M2\", 0)), \"not_significant\": int((line & ~sel).sum())})\nR = pd.DataFrame(rows)\nexp = {\"significant\": (344, 34.4), \"M1\": (203, 20.3), \"M2\": (141, 14.1), \"not_significant\": (1504, 150.4)}\nfor k, (v, tol) in exp.items():\n    R[f\"{k}_ok\"] = (R[k] - v).abs() <= tol\nR[\"all_four\"] = R[[f\"{k}_ok\" for k in exp]].all(axis=1)\nprint(R.to_string(index=False))\nprint(\"Fewest and most per penetration within tolerance (6 +/- 0.6, 76 +/- 7.6):\", abs(P.min() - 6) <= 0.6, abs(P.max() - 76) <= 7.6)\nprint(\"Fraction significant, range over readings:\", (R.significant / R.lines).min().round(3), \"to\", (R.significant / R.lines).max().round(3))\n\n# %% [markdown]\n# **Result: partially reproduced.** Under every reading a minority of neurons (19% to 34% of those with\n# a line) has a significantly positive Isimilarity, nearly all with a negative slope, but no reading\n# puts the four counts within tolerance: the smallest count is 381 (bright, reliability a, rule ii)\n# against 344 +/- 34.4.\n\n# %% [markdown]\n# ## pop-intercept-slope-correlation\n#\n# > Across neurons Isimilarity and Ssimilarity are strongly negatively correlated (r = -0.745), and only\n# > one neuron (in M2) had both a significantly positive Isimilarity and a significantly positive\n# > Ssimilarity.\n\n# %% tags=claim:pop-intercept-slope-correlation\nrows = []\nfor c in (\"dark\", \"bright\"):\n    for rd in \"ab\":\n        x, y = N[f\"intercept_{c}_{rd}\"], N[f\"slope_{c}_{rd}\"]\n        ok = x.notna() & y.notna()\n        pr, pp = stats.pearsonr(x[ok], y[ok])\n        sr_, sp_ = stats.spearmanr(x[ok], y[ok])\n        both = N[f\"sig_pos_{c}_{rd}\"] & N[f\"slope_sig_pos_{c}_{rd}\"]\n        rows.append({\"contrast\": c, \"reliability\": rd, \"n\": int(ok.sum()), \"pearson_r\": pr, \"pearson_p\": pp,\n                     \"spearman_r\": sr_, \"spearman_p\": sp_, \"both_sig_pos\": int(both.sum()),\n                     \"both_by_monkey\": N[both].groupby(\"monkey\").size().to_dict()})\nR = pd.DataFrame(rows)\nR[\"pearson_ok\"] = ((R.pearson_r + 0.745).abs() <= 0.0745) & (R.pearson_p < 1e-4) & (R.both_sig_pos <= 2)\nR[\"spearman_ok\"] = ((R.spearman_r + 0.745).abs() <= 0.0745) & (R.spearman_p < 1e-4) & (R.both_sig_pos <= 2)\nprint(R.to_string(index=False))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## pop-dark-bright-consistent\n#\n# > Isimilarity from dark and from bright shapes is consistent across neurons (Spearman's r = 0.435,\n# > n = 1,847).\n\n# %% tags=claim:pop-dark-bright-consistent\nfor rd in \"ab\":\n    x, y = N[f\"intercept_dark_{rd}\"], N[f\"intercept_bright_{rd}\"]\n    ok = x.notna() & y.notna()\n    r_, p_ = stats.spearmanr(x[ok], y[ok])\n    print(f\"reliability {rd}: Spearman r = {r_:.3f}, p = {p_:.2g}, n = {int(ok.sum())}; within 0.435 +/- 0.0435: {abs(r_ - 0.435) <= 0.0435}\")\n    for mk in (\"M1\", \"M2\"):\n        s_ = ok & (N.monkey == mk)\n        print(f\"    {mk}: Spearman r = {stats.spearmanr(x[s_], y[s_])[0]:.3f}, n = {int(s_.sum())}\")\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## pop-contrast-invariance\n#\n# > More than half of the neurons are well driven and contrast invariant, with a median correlation\n# > between dark and bright responses of 0.64.\n\n# %% tags=claim:pop-contrast-invariance\nrows = []\nfor rd in \"ab\":\n    rel = N[f\"inv_rel_{rd}\"]\n    v_left = N.invariance[rel]\n    v_zero = N.invariance.where(rel, 0.0)\n    pen_left = N[rel].groupby(\"date\").invariance.median()\n    pen_zero = N.assign(v=v_zero).groupby(\"date\").v.median()\n    rows += [{\"reliability\": rd, \"reading\": \"a, all neurons, unreliable left out\", \"median\": v_left.median(), \"n\": len(v_left)},\n             {\"reliability\": rd, \"reading\": \"a, all neurons, unreliable as 0\", \"median\": v_zero.median(), \"n\": len(v_zero)},\n             {\"reliability\": rd, \"reading\": \"b, per-penetration medians, left out\", \"median\": pen_left.median(), \"n\": len(pen_left)},\n             {\"reliability\": rd, \"reading\": \"b, per-penetration medians, as 0\", \"median\": pen_zero.median(), \"n\": len(pen_zero)}]\n    print(f\"reliability {rd}: neurons with reliable invariance above 0.5: {int(((N.invariance > 0.5) & rel).sum())} of {len(N)} \"\n          f\"({((N.invariance > 0.5) & rel).mean():.1%})\")\nR = pd.DataFrame(rows)\nR[\"within\"] = (R[\"median\"] - 0.64).abs() <= 0.064\nprint(R.round(3).to_string(index=False))\nprint(\"By monkey (all neurons, unreliable under a left out):\", N[N.inv_rel_a].groupby(\"monkey\").invariance.median().round(3).to_dict())\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## pop-sparse-across-penetrations\n#\n# > Neurons with significant Isimilarity occur in 55 of the 74 penetrations; only 28 penetrations have\n# > five or more such neurons, and 20 penetrations yielded more than 30 neurons.\n\n# %% tags=claim:pop-sparse-across-penetrations\nover30 = int((P > 30).sum())\nrows = []\nfor c in (\"dark\", \"bright\", \"either\"):\n    for rd in \"ab\":\n        for sr in (\"i\", \"ii\"):\n            line, sel = readings(N, rd, c, sr)\n            per = N[sel].groupby(\"date\").size()\n            rows.append({\"contrast\": c, \"reliability\": rd, \"slope\": sr, \"pens_with_one\": len(per), \"pens_five_plus\": int((per >= 5).sum()),\n                         \"pens_over_30\": over30})\nR = pd.DataFrame(rows)\nR[\"all_three\"] = ((R.pens_with_one - 55).abs() <= 5.5) & ((R.pens_five_plus - 28).abs() <= 2.8) & ((R.pens_over_30 - 20).abs() <= 2)\nprint(R.to_string(index=False))\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## pop-asymptote-20-percent\n#\n# > When more than 30 neurons were recorded, the percentage of neurons with significant Isimilarity\n# > levels off at about 20%.\n\n# %% tags=claim:pop-asymptote-20-percent\ndef asymptote(N, P, suffix, pens_min=30):\n    rows = []\n    big = P[P > pens_min].index.get_level_values(\"date\")\n    for c in (\"dark\", \"bright\", \"either\") if suffix == (\"dark\", \"bright\") else (\"original\", \"reversed\", \"either\"):\n        for rd in \"ab\":\n            for sr in (\"i\", \"ii\"):\n                line, sel = readings(N, rd, c, sr, suffix)\n                sub = N.date.isin(big)\n                per = (sel[sub].groupby(N.date[sub]).mean() * 100)\n                pooled = sel[sub].mean() * 100\n                small = (sel[~sub].groupby(N.date[~sub]).mean() * 100)\n                rows.append({\"contrast\": c, \"reliability\": rd, \"slope\": sr, \"pens\": len(per), \"median_pct\": per.median(),\n                             \"pooled_pct\": pooled, \"per_pen_range\": f\"{per.min():.0f}-{per.max():.0f}\",\n                             \"small_pens_median\": small.median()})\n    R = pd.DataFrame(rows)\n    R[\"a_ok\"] = (R.median_pct - 20).abs() <= 2\n    R[\"b_ok\"] = (R.pooled_pct - 20).abs() <= 2\n    return R\nR = asymptote(N, P, (\"dark\", \"bright\"))\nprint(R.round(1).to_string(index=False))\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## pop-mean-isimilarity-yield\n#\n# > In penetrations with few neurons the mean Isimilarity varies widely across penetrations; with more\n# > than 30 neurons it levels off.\n\n# %% tags=claim:pop-mean-isimilarity-yield\nfor c in (\"dark\", \"bright\"):\n    for rd in \"ab\":\n        m = N.groupby(\"date\")[f\"intercept_{c}_{rd}\"].mean()\n        n = N.groupby(\"date\").size()\n        big, small = m[n > 30].dropna(), m[n <= 30].dropna()\n        lev = stats.levene(big, small)\n        print(f\"{c}, {rd}: SD of penetration means, >30 neurons {big.std():.3f} (n = {len(big)}), <=30 {small.std():.3f} (n = {len(small)}); \"\n              f\"Levene W = {lev.statistic:.2f}, p = {lev.pvalue:.2g}; ranges {big.min():.3f} to {big.max():.3f} and {small.min():.3f} to {small.max():.3f}\")\nfig, ax = plt.subplots(figsize=(5, 3.5))\nm = N.groupby(\"date\").intercept_dark_a.mean()\nn = N.groupby(\"date\").size()\nax.scatter(n, m, s=12, color=\"k\")\nax.set_xlabel(\"responsive neurons in penetration\"); ax.set_ylabel(\"mean Isimilarity, dark (a)\")\nax.set_title(f\"y range {m.min():.2f} to {m.max():.2f}; x range {n.min()} to {n.max()}\")\nplt.show()\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## pop-recording-density\n#\n# > The fraction of neurons with significant Isimilarity is only weakly related to the recording\n# > density (Pearson's r = 0.236, p = 0.0429).\n#\n# Penetrations with one responsive neuron have no density and are left out.\n\n# %% tags=claim:pop-recording-density\nspan = N.groupby(\"date\").depth0.agg(np.ptp)\nn = N.groupby(\"date\").size()\nok = (span > 0)\nrows = []\nfor c in (\"dark\", \"bright\", \"either\"):\n    for rd in \"ab\":\n        for sr in (\"i\", \"ii\"):\n            line, sel = readings(N, rd, c, sr)\n            pct = sel.groupby(N.date).mean() * 100\n            for dens_name, dens in ((\"a, neurons per um\", n / span), (\"b, um per neuron\", span / n)):\n                r_, p_ = stats.pearsonr(dens[ok], pct[ok])\n                rows.append({\"contrast\": c, \"reliability\": rd, \"slope\": sr, \"density\": dens_name, \"r\": r_, \"p\": p_, \"n\": int(ok.sum())})\nR = pd.DataFrame(rows)\nR[\"ok\"] = ((R.r - 0.236).abs() <= 0.0236) & (R.p < 0.05)\nprint(R.round(4).to_string(index=False))\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## pop-within-vs-across-sessions\n#\n# > Neurons within a penetration have slightly more similar shape tuning than neurons from different\n# > sessions (mean correlation 0.0582 against 0.0022), and more so within 200 um (0.0918 against\n# > 0.0435 further apart).\n#\n# Readings: (1) coefficient, (a) Pearson's r of mean rates over the 120 shapes, (b) the noise-corrected\n# similarity (point estimates, all pairs, so that same- and different-session pairs are treated\n# alike; same-session pairs restricted to reliable values are shown as a variant); (2) contrast,\n# dark, bright, or both as separate pairs; (3) cross-session pairs from all sessions or within one\n# monkey. Pairs of responsive neurons, each pair once.\n\n# %% tags=claim:pop-within-vs-across-sessions\ndef all_pairs(c):\n    M, S2, INV, RATE, ses, mk, dep = [], [], [], [], [], [], []\n    for (m_, d), r in shape.items():\n        if r[\"keep\"].sum() == 0:\n            continue\n        arr, nrep = r[\"arrays\"][c]\n        mx, s2, inv = V._moments(arr[r[\"keep\"]], nrep)\n        M.append(mx); S2.append(s2); INV.append(np.broadcast_to(inv, mx.shape)); RATE.append(r[c][\"rate\"])\n        ses += [d] * len(mx); mk += [m_] * len(mx); dep.append(r[\"depth0\"][r[\"keep\"]])\n    M, S2, INV, RATE = np.vstack(M), np.concatenate(S2), np.vstack(INV), np.vstack(RATE)\n    ses, mk, dep = np.array(ses), np.array(mk), np.concatenate(dep)\n    nc = V.nc_corr(M, S2, INV, M, S2, INV)\n    pe = V.pearson_rows(RATE, RATE)\n    iu = np.triu_indices(len(M), 1)\n    same = ses[iu[0]] == ses[iu[1]]\n    same_mk = mk[iu[0]] == mk[iu[1]]\n    dist = np.abs(dep[iu[0]] - dep[iu[1]])\n    return {\"nc\": nc[iu], \"pearson\": pe[iu], \"same\": same, \"same_mk\": same_mk, \"dist\": dist}\n\npairs = {c: all_pairs(c) for c in (\"dark\", \"bright\")}\nrows = []\nfor coef in (\"pearson\", \"nc\"):\n    for c in (\"dark\", \"bright\", \"both\"):\n        cs = (\"dark\", \"bright\") if c == \"both\" else (c,)\n        v = np.concatenate([pairs[x][coef] for x in cs]); same = np.concatenate([pairs[x][\"same\"] for x in cs])\n        smk = np.concatenate([pairs[x][\"same_mk\"] for x in cs]); dist = np.concatenate([pairs[x][\"dist\"] for x in cs])\n        fin = np.isfinite(v)\n        for cross in (\"all\", \"within monkey\"):\n            other = fin & ~same & (smk if cross == \"within monkey\" else True)\n            w = fin & same\n            near, far = w & (dist <= 200), w & (dist > 200)\n            t1 = stats.ttest_ind(v[w], v[other], equal_var=False)\n            t2 = stats.ttest_ind(v[near], v[far], equal_var=False)\n            rows.append({\"coef\": coef, \"contrast\": c, \"cross\": cross, \"different\": v[other].mean(), \"same\": v[w].mean(),\n                         \"near\": v[near].mean(), \"far\": v[far].mean(), \"p_same_vs_diff\": t1.pvalue, \"p_near_vs_far\": t2.pvalue,\n                         \"n_same\": int(w.sum()), \"n_diff\": int(other.sum()), \"n_near\": int(near.sum()), \"n_far\": int(far.sum())})\nR = pd.DataFrame(rows)\nR[\"dir_p_ok\"] = (R.same > R.different) & (R.near > R.far) & (R.p_same_vs_diff < 1e-4) & (R.p_near_vs_far < 1e-4)\nR[\"means_ok\"] = (((R.different - 0.0022).abs() <= 0.00022) & ((R.same - 0.0582).abs() <= 0.00582)\n                 & ((R.near - 0.0918).abs() <= 0.00918) & ((R.far - 0.0435).abs() <= 0.00435))\nprint(R.round(4).to_string(index=False))\nprint()\n# variant: same-session noise-corrected values restricted to reliable ones\nfor c in (\"dark\", \"bright\"):\n    for rd in \"ab\":\n        vals, dists = [], []\n        for r in shape.values():\n            if r[\"keep\"].sum() < 2:\n                continue\n            rel = V.reliable(r[c][\"r\"], r[c][\"lo\"], r[c][\"hi\"], rd)\n            iu = np.triu_indices(r[\"keep\"].sum(), 1)\n            d = r[\"depth0\"][r[\"keep\"]]\n            sel = rel[iu]\n            vals.append(r[c][\"r\"][iu][sel]); dists.append(np.abs(d[iu[0]] - d[iu[1]])[sel])\n        v, dd = np.concatenate(vals), np.concatenate(dists)\n        print(f\"variant, reliable same-session pairs only, {c} {rd}: mean {v.mean():.4f} (n = {len(v)}), <=200 um {v[dd <= 200].mean():.4f}, >200 um {v[dd > 200].mean():.4f}\")\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## orientation-auc-coarse-clusters\n#\n# > Assayed at a coarse scale with two orthogonal orientations of the spindle shape, some penetrations\n# > consist entirely of neurons preferring horizontal or vertical, and in others the preference\n# > switches along the probe.\n#\n# Shape 1 is taken to be `stim_ID` 0 (the files number shapes 0 to 14; Figure 1B numbers them 1 to 15),\n# and rotations 0 and 180 degrees horizontal, 90 and 270 vertical (Materials and Methods, Feature\n# models). This rests on the dataset's labels following the paper's numbering, which the files do not\n# document. Per responsive neuron, the AUC of presentation spike counts, vertical against horizontal,\n# both contrasts pooled; averaged in 100 um depth bins from the most superficial neuron. Bins with a\n# mean of exactly 0.5 are left out of the classification.\n\n# %% tags=claim:orientation-auc-coarse-clusters\ndef pen_auc(key, stim=0):\n    s = by_date[key][\"SL\"]\n    tr = s[\"trials\"]\n    keep = shape[key][\"keep\"]\n    lum = tr.luminance.isin([V.DARK, V.BRIGHT])\n    hor = (lum & (tr.stim_ID == stim) & tr.rotation.isin([0, 180])).to_numpy()\n    ver = (lum & (tr.stim_ID == stim) & tr.rotation.isin([90, 270])).to_numpy()\n    au = np.array([V.auc(s[\"counts\"][u, ver], s[\"counts\"][u, hor]) for u in np.flatnonzero(keep)])\n    d = shape[key][\"depth0\"][keep]\n    bins = (d // 100).astype(int)\n    b = pd.Series(au).groupby(bins).mean().sort_index()\n    return au, b, int(hor.sum()), int(ver.sum())\n\ndef classify(b):\n    side = np.sign(b.dropna() - 0.5)\n    side = side[side != 0].to_numpy()\n    if len(side) == 0:\n        return \"none\"\n    if np.all(side == side[0]):\n        return \"all one\"\n    changes = int((np.diff(side) != 0).sum())\n    return \"switching\" if changes == 1 else f\"mixed ({changes} changes)\"\n\nkinds = {}\nfor key, r in shape.items():\n    if r[\"keep\"].sum() == 0:\n        continue\n    au, b, nh, nv = pen_auc(key)\n    kinds[key] = {\"class\": classify(b), \"bins\": len(b), \"neurons\": len(au), \"hor_pres\": nh, \"ver_pres\": nv,\n                  \"frac_vertical_bins\": float((b > 0.5).mean())}\nK = pd.DataFrame(kinds).T\nprint(K[\"class\"].value_counts().to_string())\nprint(\"Of these, penetrations with at least 3 occupied bins:\", K[K.bins >= 3][\"class\"].value_counts().to_dict())\nfor name in (\"M2p6\", \"M1p5\"):\n    key = found[name]\n    au, b, nh, nv = pen_auc(key)\n    print(f\"{name} {key}: class {classify(b)}, {len(au)} neurons, {len(b)} bins, horizontal/vertical presentations {nh}/{nv}\")\n    print(\"   bin means (100 um bins from the top):\", b.round(2).to_dict())\nfig, ax = plt.subplots(1, 2, figsize=(8, 3.5))\nfor k, name in enumerate((\"M2p6\", \"M1p5\")):\n    au, b, _, _ = pen_auc(found[name])\n    ax[k].barh(b.index * 100, b.to_numpy() - 0.5, height=90, left=0.5, color=np.where(b > 0.5, \"tab:red\", \"tab:blue\"))\n    ax[k].axvline(0.5, color=\"k\", lw=0.5); ax[k].invert_yaxis()\n    ax[k].set_xlabel(\"mean AUC (vertical > 0.5)\"); ax[k].set_ylabel(\"depth bin (um)\")\n    ax[k].set_title(f\"{name}: AUC {b.min():.2f} to {b.max():.2f}\")\nplt.tight_layout(); plt.show()\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## texture-sparse-clusters\n#\n# > For textures, of 979 neurons in 51 sessions (6 to 83 per penetration), a small subset (207; 18 in\n# > M1, 189 in M2) across 34 of 51 penetrations (7 in M1, 27 in M2) showed clustered selectivity, and\n# > 16 penetrations had five or more neurons with significant Isimilarity.\n\n# %% tags=claim:texture-sparse-clusters\nPT = T.groupby([\"monkey\", \"date\"]).size()\nprint(\"Texture neurons\", len(T), \"in\", len(PT), \"penetrations; per penetration\", PT.min(), \"to\", PT.max())\nrows = []\nfor c in (\"original\", \"reversed\", \"either\"):\n    for rd in \"ab\":\n        for sr in (\"i\", \"ii\"):\n            line, sel = readings(T, rd, c, sr, (\"original\", \"reversed\"))\n            g = T[sel].groupby(\"monkey\").size()\n            per = T[sel].groupby([\"monkey\", \"date\"]).size()\n            pm = per.groupby(level=0).size()\n            rows.append({\"contrast\": c, \"reliability\": rd, \"slope\": sr, \"lines\": int(line.sum()), \"sig\": int(sel.sum()),\n                         \"M1\": int(g.get(\"M1\", 0)), \"M2\": int(g.get(\"M2\", 0)), \"pens\": len(per), \"pens_M1\": int(pm.get(\"M1\", 0)),\n                         \"pens_M2\": int(pm.get(\"M2\", 0)), \"pens_5plus\": int((per >= 5).sum())})\nR = pd.DataFrame(rows)\nexp = {\"sig\": (207, 20.7), \"M1\": (18, 1.8), \"M2\": (189, 18.9), \"pens\": (34, 3.4), \"pens_M1\": (7, 0.7), \"pens_M2\": (27, 2.7), \"pens_5plus\": (16, 1.6)}\nfor k, (v, tol) in exp.items():\n    R[f\"{k}_ok\"] = (R[k] - v).abs() <= tol\nR[\"most_ok\"] = abs(PT.max() - 83) <= 8.3\nR[\"all\"] = R[[f\"{k}_ok\" for k in exp] + [\"most_ok\"]].all(axis=1)\nR[\"total_and_pens\"] = R[[\"sig_ok\", \"pens_ok\", \"pens_5plus_ok\", \"most_ok\"]].all(axis=1)\nprint(R.drop(columns=[f\"{k}_ok\" for k in exp]).to_string(index=False))\nprint(\"Neurons without a line (paper: 48 of 979): original\", int((~T.has_line_original_a).sum()), \"/\", int((~T.has_line_original_b).sum()),\n      \"| reversed\", int((~T.has_line_reversed_a).sum()), \"/\", int((~T.has_line_reversed_b).sum()), \"(reliability a / b)\")\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## texture-original-reversed-consistent\n#\n# > Texture Isimilarity from original and contrast-reversed textures is consistent across neurons\n# > (Spearman's r = 0.464, n = 905).\n\n# %% tags=claim:texture-original-reversed-consistent\nfor rd in \"ab\":\n    x, y = T[f\"intercept_original_{rd}\"], T[f\"intercept_reversed_{rd}\"]\n    ok = x.notna() & y.notna()\n    r_, p_ = stats.spearmanr(x[ok], y[ok])\n    print(f\"reliability {rd}: Spearman r = {r_:.3f}, p = {p_:.2g}, n = {int(ok.sum())}; r within 0.464 +/- 0.0464: {abs(r_ - 0.464) <= 0.0464}; \"\n          f\"n within 905 +/- 90.5: {abs(ok.sum() - 905) <= 90.5}\")\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## texture-asymptote-20-percent\n#\n# > For textures as for shapes, the fraction of neurons with a significant intercept levels off at\n# > about 20% when many neurons are recorded.\n\n# %% tags=claim:texture-asymptote-20-percent\nRT = asymptote(T, PT, (\"original\", \"reversed\"))\nprint(\"Texture penetrations with more than 30 neurons:\", int((PT > 30).sum()))\nprint(RT.round(1).to_string(index=False))\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## position-optimal-consistent\n#\n# > In 33 M2 penetrations (723 neurons), Isimilarity computed from responses at each neuron's optimal\n# > stimulus position correlates positively with Isimilarity at the aggregate RF center (r = 0.325).\n#\n# The files number the five positions 0 to 4 without saying which is the center. The center is taken\n# to be the position with the largest mean response over the penetration's responsive neurons,\n# since the aggregate RF center is where the stimuli were centred on the neurons' RFs (an\n# assumption); how often each position wins is printed. Neurons are those responsive in the main\n# shape test (the same units, by `unit_ID`); responsiveness within the position test is a variant.\n# Optimal position: the largest variance-to-mean ratio of mean rates over the 15 shapes (Materials\n# and Methods, RF localization, paragraph 2).\n\n# %% tags=claim:position-optimal-consistent\nt0 = time.time()\npos = {}\nfor (mk, d), g in by_date.items():\n    if \"SP\" not in g:\n        continue\n    s = g[\"SP\"]\n    A = V.position_arrays(s)\n    keep_shape = shape[(mk, d)][\"keep\"]\n    keep_pos = V.responsive([A[p][0] for p in range(5)], A[\"blank\"])\n    rates_p = np.stack([V.rates(A[p][0]) for p in range(5)])  # (pos, unit, stim)\n    pop = np.nanmean(rates_p[:, keep_shape], axis=(1, 2)) if keep_shape.any() else np.full(5, np.nan)\n    pos[(mk, d)] = {\"A\": A, \"keep_shape\": keep_shape, \"keep_pos\": keep_pos, \"rates\": rates_p,\n                    \"center\": int(np.nanargmax(pop)) if np.isfinite(pop).any() else None, \"pop\": pop,\n                    \"depth0\": s[\"units\"].depth0.to_numpy()}\ncenters = pd.Series({k: v[\"center\"] for k, v in pos.items()})\nprint(\"Position test files:\", len(pos), \"| position with the largest population response:\", centers.value_counts().to_dict())\n\n\ndef optimal_isim(p, keep, tag):\n    A, rates_p = p[\"A\"], p[\"rates\"]\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        disp = np.nanvar(rates_p, axis=2, ddof=1) / np.nanmean(rates_p, axis=2)\n    best = np.nanargmax(np.nan_to_num(disp, nan=-1), axis=0)\n    arr = np.stack([A[best[u]][0][u] for u in range(len(best))])\n    nrep = A[0][1]\n    assert all((A[q][1] == nrep).all() for q in range(5))\n    r, lo, hi = V.similarity(arr[keep], nrep, tag)\n    out = {\"best\": best}\n    for rd in \"ab\":\n        out[rd] = V.isimilarity(r, V.reliable(r, lo, hi, rd), p[\"depth0\"][keep], np.ones(keep.sum(), bool))\n    return out\n\n\ndef position_isim(p, keep, q, tag):\n    arr, nrep = p[\"A\"][q]\n    r, lo, hi = V.similarity(arr[keep], nrep, tag)\n    return {rd: V.isimilarity(r, V.reliable(r, lo, hi, rd), p[\"depth0\"][keep], np.ones(keep.sum(), bool)) for rd in \"ab\"} | {\"r\": r, \"lo\": lo, \"hi\": hi}\n\nrows = []\npos_res = {}\nfor (mk, d), p in pos.items():\n    for which, keep in ((\"shape-responsive\", p[\"keep_shape\"]), (\"position-responsive\", p[\"keep_pos\"])):\n        if keep.sum() < 4:\n            continue\n        o = optimal_isim(p, keep, f\"{d}-SP-opt-{which}\")\n        cen = position_isim(p, keep, p[\"center\"], f\"{d}-SP-center-{which}\")\n        main = N[(N.monkey == mk) & (N.date == d)]\n        main_units = main.unit.to_numpy()\n        units = np.flatnonzero(keep)\n        pos_res[(d, which)] = (o, cen)\n        for rd in \"ab\":\n            for i, u in enumerate(units):\n                mrow = main[main.unit == u]\n                rows.append({\"date\": d, \"which\": which, \"rd\": rd, \"unit\": u, \"opt\": o[rd].intercept.iloc[i],\n                             \"center\": cen[rd].intercept.iloc[i],\n                             \"main_dark\": mrow[f\"intercept_dark_{rd}\"].iloc[0] if len(mrow) else np.nan})\nPR = pd.DataFrame(rows)\nprint(f\"position analyses in {time.time() - t0:.0f} s\")\nfor which in (\"shape-responsive\", \"position-responsive\"):\n    sub = PR[(PR.which == which) & (PR.rd == \"a\")]\n    print(f\"{which}: {sub.unit.size} neurons in {sub.date.nunique()} penetrations (penetrations with 4 or more)\")\nout = []\nfor which in (\"shape-responsive\", \"position-responsive\"):\n    for rd in \"ab\":\n        sub = PR[(PR.which == which) & (PR.rd == rd)]\n        for ref in (\"center\", \"main_dark\"):\n            ok = sub.opt.notna() & sub[ref].notna()\n            r_, p_ = stats.spearmanr(sub.opt[ok], sub[ref][ok])\n            out.append({\"neurons\": which, \"reliability\": rd, \"reference\": ref, \"spearman_r\": r_, \"p\": p_, \"n\": int(ok.sum()),\n                        \"pens\": sub[ok].date.nunique()})\nR = pd.DataFrame(out)\nR[\"positive_p\"] = (R.spearman_r > 0) & (R.p < 1e-4)\nR[\"r_within\"] = (R.spearman_r - 0.325).abs() <= 0.0325\nprint(R.round(4).to_string(index=False))\n# all positions as center, for the assumption\nalt = []\nfor q in range(5):\n    vals = []\n    for (mk, d), p in pos.items():\n        keep = p[\"keep_shape\"]\n        if keep.sum() < 4:\n            continue\n        cen = position_isim(p, keep, q, f\"{d}-SP-pos{q}\")\n        o = pos_res[(d, \"shape-responsive\")][0]\n        vals.append(pd.DataFrame({\"opt\": o[\"a\"].intercept.to_numpy(), \"cen\": cen[\"a\"].intercept.to_numpy()}))\n    v = pd.concat(vals).dropna()\n    alt.append({\"position_as_center\": q, \"spearman_r\": stats.spearmanr(v.opt, v.cen)[0], \"n\": len(v)})\nprint(\"Variant, each position taken as the center (shape-responsive neurons, reliability a):\")\nprint(pd.DataFrame(alt).round(3).to_string(index=False))\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## position-examples-invariant\n#\n# > In two example penetrations, the pattern of tuning similarity is the same at all five stimulus\n# > positions; a small cluster at every position in M2p9 and none at any position in M2p28.\n\n# %% tags=claim:position-examples-invariant\nfor name, exp in ((\"M2p9\", 16), (\"M2p28\", 55)):\n    key = found[name]\n    p = pos[key]\n    for which, keep in ((\"shape-responsive\", p[\"keep_shape\"]), (\"position-responsive\", p[\"keep_pos\"])):\n        print(f\"{name} {key}: {which} neurons {int(keep.sum())} (Figure 11: {exp}, accepted within 10%: {abs(keep.sum() - exp) <= 0.1 * exp})\")\n    keep = p[\"keep_shape\"]\n    per = {q: position_isim(p, keep, q, f\"{key[1]}-SP-pos{q}\") for q in range(5)}\n    c = p[\"center\"]\n    iu = np.triu_indices(keep.sum(), 1)\n    for rd in \"ab\":\n        line = []\n        for q in range(5):\n            if q == c:\n                continue\n            relc = V.reliable(per[c][\"r\"], per[c][\"lo\"], per[c][\"hi\"], rd)[iu]\n            relq = V.reliable(per[q][\"r\"], per[q][\"lo\"], per[q][\"hi\"], rd)[iu]\n            both = relc & relq\n            if both.sum() > 2:\n                r_, p_ = stats.pearsonr(per[c][\"r\"][iu][both], per[q][\"r\"][iu][both])\n            else:\n                r_, p_ = np.nan, np.nan\n            line.append(f\"pos {q}: r = {r_:.3f}, p = {p_:.2g}, pairs {int(both.sum())}\")\n        print(f\"  (a) reliability {rd}, against center {c}:\", \"; \".join(line))\n        print(f\"  (b) reliability {rd}, neurons with significant positive Isimilarity per position:\",\n              {q: int(per[q][rd].sig_pos.sum()) for q in range(5)}, \"| with a line:\", {q: int(per[q][rd].has_line.sum()) for q in range(5)})\n    print(f\"  reliable fraction of pairs per position (a): {[round(float(V.reliable(per[q]['r'], per[q]['lo'], per[q]['hi'], 'a')[iu].mean()), 2) for q in range(5)]}\")\n\n# %% [markdown]\n# **Result: see above.**\n\n# %% [markdown]\n# ## Blocked claims\n#\n# - **ex-csd-sinks**: the dataset holds spike times only; the assets summary lists Units and\n#   ElectrodeGroup, and no file has an LF series (`acquisition` and `processing` are empty).\n# - **orientation-sf-isimilarity**, **apc-peaks-sparse-clustering**, **apc-example-m2p51**: they need the\n#   shape images or their boundary-curvature descriptions (Pasupathy and Connor 2001), which neither\n#   the dataset (its `stimulus/templates` is empty) nor any public, pinned source found holds.\n# - **gyrus-penetrations-consistent**: the 18 gyral penetrations are identified only by grid location\n#   and RF azimuth (Figure 8B), and the files give neither (electrode location is only \"V4\").\n# - **simulation-random-with-domains**: a simulation whose peak amplitudes and progression steps are not\n#   given, judged by eye; it uses no recorded data.\n\n# %% tags=sanity\nempty = {s[\"asset\"][\"kind\"]: (len(by_date[(s[\"asset\"][\"monkey\"], s[\"asset\"][\"date\"])]), ) for s in sess[:1]}\nprint(\"Assets summary variables:\", meta[\"assetsSummary\"][\"variableMeasured\"])\n\n# %% [markdown]\n# ## Summary\n#\n# (Filled in from the outputs.)\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001357-namima-2025 && python - <<'EOF'
p='v4clusters.py'; s=open(p).read()
s=s.replace('''        "depth_unit": u["depth"].attrs.get("description"),
    }''','''        "depth_unit": u["depth"].attrs.get("description"),
        "acquisition": sorted(f["acquisition"].keys()),
        "processing": sorted(f["processing"].keys()),
        "templates": sorted(f["stimulus/templates"].keys()),
        "electrode_columns": sorted(f["general/extracellular_ephys/electrodes"].keys()),
        "electrode_locations": sorted({_s(x) for x in f["general/extracellular_ephys/electrodes/location"][:]}),
    }''')
open(p,'w').write(s)
p='/tmp/claude-1001/cells.py'; s=open(p).read()
s=s.replace('''empty = {s["asset"]["kind"]: (len(by_date[(s["asset"]["monkey"], s["asset"]["date"])]), ) for s in sess[:1]}
print("Assets summary variables:", meta["assetsSummary"]["variableMeasured"])''','''print("Assets summary variables:", meta["assetsSummary"]["variableMeasured"])
for f_ in ("acquisition", "processing", "templates", "electrode_columns", "electrode_locations"):
    print(f_, "across files:", sorted({tuple(s["meta"][f_]) for s in sess}))''')
open(p,'w').write(s)
EOF
cat > $TMPDIR/dev.py <<'EOF'
import sys, os, re, pickle, time, io, contextlib
sys.path.insert(0,'entries/001357-namima-2025')
import matplotlib; matplotlib.use('Agg')
import v4clusters as V
cache='/tmp/claude-1001/cache2.pkl'
if os.path.exists(cache):
    S=pickle.load(open(cache,'rb')); V.load_many=lambda ids, threads=16: S
else:
    orig=V.load_many
    def lm(ids, threads=16):
        S=orig(ids,threads); pickle.dump(S,open(cache,'wb')); return S
    V.load_many=lm
src=open('/tmp/claude-1001/cells.py').read()
blocks=re.split(r"^# %%", src, flags=re.M)[1:]
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
stop=int(sys.argv[2]) if len(sys.argv)>2 else 999
ns={}
if start>0: 
    ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb')) if False else {}
for i,b in enumerate(blocks):
    head,_,body=b.partition("\n")
    if "[markdown]" in head: continue
    if i>=stop: break
    t=time.time()
    print(f"===== cell {i} {head.strip()}")
    exec(compile(body, f"cell{i}", "exec"), ns)
    print(f"----- {time.time()-t:.1f}s")
EOF
cd $TMPDIR && . dev/bin/activate && timeout 3000 python dev.py 2>&1 | tail -300
```

```
reading     date label  responsive  accepted
      a 20191025   p13          13     False
      b 20191025   p13          13     False
      c 20191024   p12          42      True
M2p9 (paper's count: 16 )
reading     date label  responsive  accepted
      a 20210421   p12          16      True
      b 20210420   p11          11     False
      c 20210417   p09          18     False
M2p28 (paper's count: 55 )
reading     date label  responsive  accepted
      a 20210529   p40           1     False
      b 20210527   p37          24     False
      c 20210512   p28          55      True
M2p51 (paper's count: 33 )
reading     date label  responsive  accepted
      a      NaN   NaN         NaN     False
      b      NaN   NaN         NaN     False
      c 20210611   p51        48.0     False
M1p5 (paper's count: None )
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/cells.py'; s=open(p).read()
s=s.replace('''    arr = np.stack([A[best[u]][0][u] for u in range(len(best))])
    nrep = A[0][1]
    assert all((A[q][1] == nrep).all() for q in range(5))''','''    R = max(A[q][0].shape[2] for q in range(5))
    pad = {q: np.pad(A[q][0], ((0, 0), (0, 0), (0, R - A[q][0].shape[2])), constant_values=np.nan) for q in range(5)}
    nreps = np.stack([A[q][1] for q in range(5)])
    # each neuron uses its own position; the repeats per stimulus are taken as the smallest over the
    # positions in use, so that every resampled repeat exists (the files have 8 at every position)
    nrep = nreps[np.unique(best)].min(0)
    arr = np.stack([pad[best[u]][u] for u in range(len(best))])[:, :, : nrep.max()]
    for j in range(arr.shape[1]):
        arr[:, j, nrep[j]:] = np.nan''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle,sys; sys.path.insert(0,'entries/001357-namima-2025'); import v4clusters as V, numpy as np
S=pickle.load(open('cache2.pkl','rb'))
import collections; c=collections.Counter()
for s in S:
  if s['trials'].ses_ID.iloc[0].endswith('SL') and 'position' in s['trials']:
    A=V.position_arrays(s); c[tuple((A[q][1].min(),A[q][1].max()) for q in range(5))]+=1
print(c)"
```

```
Counter({((np.int64(8), np.int64(8)), (np.int64(8), np.int64(8)), (np.int64(8), np.int64(8)), (np.int64(8), np.int64(8)), (np.int64(8), np.int64(8))): 30, ((np.int64(5), np.int64(6)), (np.int64(5), np.int64(6)), (np.int64(5), np.int64(6)), (np.int64(5), np.int64(6)), (np.int64(5), np.int64(6))): 2, ((np.int64(4), np.int64(4)), (np.int64(4), np.int64(4)), (np.int64(4), np.int64(4)), (np.int64(4), np.int64(4)), (np.int64(4), np.int64(5))): 1, ((np.int64(15), np.int64(16)), (np.int64(15), np.int64(16)), (np.int64(15), np.int64(16)), (np.int64(15), np.int64(16)), (np.int64(15), np.int64(16))): 1})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && date -u && timeout 3000 python dev.py 2>&1 | sed -n '/cell 72/,$p'; date -u
```

```
Mon Nov  2 07:21:29 UTC 2026
===== cell 72 tags=claim:position-optimal-consistent
Position test files: 34 | position with the largest population response: {1: 12, 2: 11, 4: 5, 0: 3, 3: 3}
position analyses in 28 s
shape-responsive: 721 neurons in 33 penetrations (penetrations with 4 or more)
position-responsive: 603 neurons in 33 penetrations (penetrations with 4 or more)
            neurons reliability reference  spearman_r   p   n  pens  positive_p  r_within
   shape-responsive           a    center      0.4679 0.0 248    22        True     False
   shape-responsive           a main_dark      0.2968 0.0 378    26        True      True
   shape-responsive           b    center      0.4465 0.0 623    33        True     False
   shape-responsive           b main_dark      0.3252 0.0 676    33        True      True
position-responsive           a    center      0.4743 0.0 220    20        True     False
position-responsive           a main_dark      0.2975 0.0 343    23        True      True
position-responsive           b    center      0.4524 0.0 535    32        True     False
position-responsive           b main_dark      0.3479 0.0 554    32        True      True
Variant, each position taken as the center (shape-responsive neurons, reliability a):
 position_as_center  spearman_r   n
                  0       0.359 217
                  1       0.447 222
                  2       0.567 222
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1480,1500p paper/*.txt; sed -n 1560,1615p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/cells.py'; s=open(p).read()
a=s.index('# %% tags=claim:position-examples-invariant'); b=s.index('# %% [markdown]', a)
new='''# %% tags=claim:position-examples-invariant
ex_rows = []
for name, num, exp in (("M2p9", 9, 16), ("M2p28", 28, 55)):
    f = find_pen("M2", num, exp)
    for _, fr in f.iterrows():
        key = ("M2", fr.date)
        if key not in pos:
            print(f"{name} reading {fr.reading}: {fr.date} has no position test")
            continue
        p = pos[key]
        keep = p["keep_shape"]
        print(f"{name} reading {fr.reading}: {key} ({fr.label}), shape-responsive {int(keep.sum())}, position-responsive "
              f"{int(p['keep_pos'].sum())}; Figure 11 n = {exp}; accepted: {bool(fr.accepted)}")
        per = {q: position_isim(p, keep, q, f"{key[1]}-SP-pos{q}") for q in range(5)}
        iu = np.triu_indices(keep.sum(), 1)
        for rd in "ab":
            rel = {q: V.reliable(per[q]["r"], per[q]["lo"], per[q]["hi"], rd)[iu] for q in range(5)}
            cor = {}
            for q1 in range(5):
                for q2 in range(q1 + 1, 5):
                    both = rel[q1] & rel[q2]
                    cor[(q1, q2)] = stats.pearsonr(per[q1]["r"][iu][both], per[q2]["r"][iu][both]) if both.sum() > 2 else (np.nan, np.nan)
            # reading (a) for each choice of center: all four correlations with it positive, p < 0.05
            a_by_center = {c: all((cor[tuple(sorted((c, q)))][0] > 0) and (cor[tuple(sorted((c, q)))][1] < 0.05) for q in range(5) if q != c)
                           for c in range(5)}
            nsig = {q: int(per[q][rd].sig_pos.sum()) for q in range(5)}
            print(f"   reliability {rd}: pair correlations " + ", ".join(f"{k[0]}-{k[1]} r={v[0]:.2f} p={v[1]:.2g}" for k, v in cor.items()))
            print(f"   reliability {rd}: (a) holds with center = {a_by_center}; (b) significant positive Isimilarity per position {nsig}, "
                  f"lines {[int(per[q][rd].has_line.sum()) for q in range(5)]}; reliable pairs {[int(rel[q].sum()) for q in range(5)]} of {len(iu[0])}")
            ex_rows.append({"name": name, "reading": fr.reading, "date": fr.date, "accepted": bool(fr.accepted), "rel": rd,
                            "a_any_center": any(a_by_center.values()), "a_inferred_center": a_by_center[p["center"]],
                            "nsig_min": min(nsig.values()), "nsig_max": max(nsig.values())})
EX = pd.DataFrame(ex_rows)
EX["b_holds"] = np.where(EX.name == "M2p9", EX.nsig_min >= 2, EX.nsig_max <= 1)
print(EX.to_string(index=False))

'''
s=s[:a]+new+s[b:]
# AUC variant over stim ids
s=s.replace('''fig, ax = plt.subplots(1, 2, figsize=(8, 3.5))
for k, name in enumerate(("M2p6", "M1p5")):''','''var = []
for st in range(15):
    cls = {name: classify(pen_auc(found[name], st)[1]) for name in ("M2p6", "M1p5")}
    allk = pd.Series({k: classify(pen_auc(k, st)[1]) for k, r in shape.items() if r["keep"].sum() > 0})
    var.append({"stim_ID": st, **cls, "all_one": int((allk == "all one").sum()), "switching": int((allk == "switching").sum())})
print("Variant, each stim_ID taken as the spindle:")
print(pd.DataFrame(var).to_string(index=False))
fig, ax = plt.subplots(1, 2, figsize=(8, 3.5))
for k, name in enumerate(("M2p6", "M1p5")):''')
# p-values in center variant
s=s.replace('''    alt.append({"position_as_center": q, "spearman_r": stats.spearmanr(v.opt, v.cen)[0], "n": len(v)})''','''    rr_ = stats.spearmanr(v.opt, v.cen)
    alt.append({"position_as_center": q, "spearman_r": rr_[0], "p": rr_[1], "n": len(v)})''')
s=s.replace('''print(pd.DataFrame(alt).round(3).to_string(index=False))''','''print(pd.DataFrame(alt).to_string(index=False))''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && timeout 3000 python dev.py 2>&1 | sed -n '/cell 60/,/cell 63/p;/cell 72/,$p'; date -u
```

```
===== cell 60 tags=claim:orientation-auc-coarse-clusters
class
mixed (5 changes)     12
mixed (3 changes)     11
mixed (2 changes)     10
mixed (7 changes)      7
mixed (4 changes)      7
mixed (8 changes)      6
mixed (10 changes)     5
mixed (9 changes)      4
mixed (6 changes)      4
mixed (12 changes)     2
all one                2
switching              2
mixed (11 changes)     1
mixed (14 changes)     1
Of these, penetrations with at least 3 occupied bins: {'mixed (5 changes)': 12, 'mixed (3 changes)': 11, 'mixed (2 changes)': 10, 'mixed (7 changes)': 7, 'mixed (4 changes)': 7, 'mixed (8 changes)': 6, 'mixed (10 changes)': 5, 'mixed (9 changes)': 4, 'mixed (6 changes)': 4, 'mixed (12 changes)': 2, 'switching': 2, 'mixed (11 changes)': 1, 'all one': 1, 'mixed (14 changes)': 1}
M2p6 ('M2', '20210414'): class mixed (2 changes), 24 neurons, 17 bins, horizontal/vertical presentations 18/19
   bin means (100 um bins from the top): {0: 0.17, 1: 0.41, 2: 0.2, 3: 0.36, 4: 0.16, 5: 0.32, 9: 1.0, 11: 0.87, 13: 0.75, 14: 0.69, 15: 0.58, 17: 0.61, 18: 0.73, 19: 0.75, 20: 0.68, 22: 0.37, 23: 0.38}
M1p5 ('M1', '20190726'): class mixed (12 changes), 60 neurons, 25 bins, horizontal/vertical presentations 18/17
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > results.py <<'EOF'
import re
R = {
"methods-sessions-and-neurons": "**Result: reproduced.** The files hold 30 and 44 shape sessions, 17 and 34 texture sessions and 34 position-test sessions (expected 33 +/- 3.3; one holds a single unit). 1,869 responsive shape neurons (427 excluded) and 985 responsive texture neurons (360 excluded) are all within tolerance. The good units of the texture files sum to the paper's 979 + 366 = 1,345 exactly; the shape files hold 2,296 against the paper's 2,311.",
"ex-m2p6-cluster": "**Result: partially reproduced.** The penetration the files label p06 of M2 (readings a and b give sessions with 13 and 16 responsive neurons) has 24 responsive neurons spanning 2,340 um, and neurons 1 to 9, spread over 540 um, are similarly tuned at both contrasts (mean similarity 0.70 dark and 0.86 bright, against -0.02 with the deeper neurons). With dark shapes 13 neurons have a significant positive Isimilarity under both reliability readings, all with negative slopes: neurons 1 to 9 and 14, as in the paper, plus 12, 21 and 22, and not 17. The count, 13 against 11 +/- 1.1, and the set are outside the claim's margin.",
"ex-m2p6-pairs": "**Result: partially reproduced.** Neurons 3 and 8 are 260 um apart with similarity 0.780 (dark) and 0.894 (bright), and neurons 18 and 19 are 80 um apart with a dark similarity of 0.000, all within tolerance. The bright similarity of 18 and 19 is -0.144, outside -0.25 +/- 0.025.",
"ex-m2p6-invariance": "**Result: reproduced.** Under reliability reading (a), 20 of the 24 neurons have a reliable invariance above 0.5 (19 +/- 1.9); under reading (b) 22, outside tolerance. The criterion asks for one reading. Invariance is high whether or not the neuron has a significant Isimilarity (medians 0.955 and 0.954).",
"ex-m1p12-no-cluster": "**Result: reproduced.** The penetration labelled p12 of M1 has 42 responsive neurons over 2,580 um. With dark shapes one neuron has a significant positive Isimilarity under both reliability readings, and 35 (reading a) or 36 (reading b) of 42 have reliable invariance above 0.5. With bright shapes 4 neurons have a significant positive Isimilarity, which the criterion does not judge.",
"ex-m1p12-strong-responses": "**Result: reproduced.** With baseline subtracted (reading a), 28 neurons peak above 15 spikes/s for dark shapes and 26 for bright shapes, the paper's numbers; raw rates (reading b) give 29 and 31.",
"pop-significant-isimilarity": "**Result: partially reproduced.** Under every reading a minority of neurons with a line has a significant positive Isimilarity (22% to 34%), nearly all with a negative slope, but no reading puts the four counts within tolerance: the closest, bright shapes under reliability (a) with rule (ii), gives 381 (226 in M1, 155 in M2) against 344 (203, 141), and 1,349 not significant against 1,504. Penetrations hold 1 to 77 responsive neurons; the one with a single neuron is M2 p40, and the next smallest hold 6.",
"pop-intercept-slope-correlation": "**Result: reproduced.** With dark shapes Pearson's r between Isimilarity and Ssimilarity is -0.768 (reliability a, n = 1,729) or -0.735 (b, n = 1,805), p far below 0.0001, within -0.745 +/- 0.0745; with bright shapes it is -0.667 and -0.653, outside. No neuron has both a significantly positive Isimilarity and a significantly positive Ssimilarity, where the paper reports one; the criterion allows up to 2.",
"pop-dark-bright-consistent": "**Result: not reproduced.** Isimilarity from dark and bright shapes is positively correlated, more strongly than the paper reports: Spearman's r = 0.484 (reliability a, n = 1,643) and 0.520 (b, n = 1,757), p < 1e-90, both above 0.435 +/- 0.0435. The consistency the claim states holds; the value does not.",
"pop-contrast-invariance": "**Result: reproduced.** Under reliability reading (b), with unreliable values counted as 0, the median invariance is 0.632 over all neurons and 0.619 over the per-penetration medians, both within 0.64 +/- 0.064; 54.7% of neurons have reliable invariance above 0.5. Leaving unreliable values out gives medians of 0.76 to 0.77, and reading (a) with unreliable values as 0 gives 0.474 and 0.513; these readings do not match.",
"pop-sparse-across-penetrations": "**Result: reproduced.** Under all eight dark and bright readings, 54 to 59 penetrations have at least one neuron with a significant positive Isimilarity (55 +/- 5.5), 27 to 29 have five or more (28 +/- 2.8), and 20 penetrations have more than 30 responsive neurons. The readings counting either contrast give 62 and 39 to 41 penetrations, outside tolerance.",
"pop-asymptote-20-percent": "**Result: reproduced.** Over the 20 penetrations with more than 30 neurons, the pooled percentage with a significant positive Isimilarity is 21.1% to 21.5% with dark or bright shapes under reliability (a), and the median per penetration is 19.4% to 21.0% under reliability (b), within 20 +/- 2. Per-penetration values range from 0% to 60%; counting either contrast gives 29% to 36%.",
"pop-mean-isimilarity-yield": "**Result: reproduced.** The SD of the penetration means of Isimilarity is smaller for penetrations with more than 30 neurons than for those with 30 or fewer under all four contrast and reliability readings (dark 0.089 against 0.204 under a, Levene p = 0.015; bright under b 0.107 against 0.133, Levene p = 0.18). No contrast reading reproduces pop-significant-isimilarity, so all are shown.",
"pop-recording-density": "**Result: reproduced.** With density read as neurons per um (reading a), Pearson's r is 0.254 to 0.257 under the dark and bright readings with reliability (a) (p = 0.028 to 0.030, 73 penetrations), within 0.236 +/- 0.0236; reliability (b) and either contrast give 0.296 to 0.336. Read as um per neuron (the legend's quotient), r is negative (-0.355 to -0.456).",
"pop-within-vs-across-sessions": "**Result: partially reproduced.** Under every reading same-session pairs are more similar than different-session pairs and pairs within 200 um more than pairs further apart (Welch p below 1e-4 throughout). No reading matches all four means: Pearson's r of mean rates gives 0.0021 to 0.0036 across sessions (matching 0.0022 for bright shapes over all sessions) but 0.0295 to 0.0317 within (0.0582 in the paper), 0.073 within 200 um and 0.019 to 0.022 beyond; the noise-corrected values are 0.006 to 0.009, 0.083 to 0.090, 0.195 and 0.056 to 0.066. All means are weak, as the paper says.",
"orientation-auc-coarse-clusters": "**Result: not reproduced.** Taking stim_ID 0 as the spindle, 2 of 74 penetrations are all one preference and 2 switch once, so both kinds exist, but neither M2p6 nor M1p5 is of one kind: M2p6 has bins preferring horizontal at the top (0 to 500 um), vertical below and horizontal again in its two deepest bins (2 changes), and M1p5 changes side 12 times. No stim_ID taken as the spindle makes either penetration of one kind.",
"texture-sparse-clusters": "**Result: not reproduced.** Over 985 texture neurons in 51 penetrations (6 to 83 per penetration), no reading puts the counts within tolerance. The closest, original or reversed textures under reliability (a), give 193 and 198 neurons (207 +/- 20.7) but 30 and 27 penetrations (34 +/- 3.4), 4 and 2 in M1 (7) and 12 and 7 neurons in M1 (18); reliability (b) gives 304 to 395 neurons, in 15 to 37 penetrations, and 41 to 79 in M1. A minority of neurons is clustered under every reading (20% to 41% of those with a line).",
"texture-original-reversed-consistent": "**Result: not reproduced.** Texture Isimilarity from original and reversed textures is positively correlated, more strongly than the paper reports: Spearman's r = 0.706 (reliability a, n = 624) and 0.642 (b, n = 894), against 0.464 +/- 0.0464. The neuron count under (b), 894, is within 905 +/- 90.5.",
"texture-asymptote-20-percent": "**Result: not reproduced.** Seven texture penetrations have more than 30 neurons. In them the percentage with a significant intercept is 25.6% to 52.1% pooled and 28.9% to 51.4% as a median, above 20 +/- 2 under every reading.",
"position-optimal-consistent": "**Result: reproduced.** In 33 M2 penetrations, 721 shape-responsive neurons (723 in the paper) enter the position test. Isimilarity at each neuron's optimal position correlates positively with Isimilarity in the main shape test with dark shapes (reading b), Spearman's r = 0.297 (reliability a) and 0.325 (b), p < 1e-4, within 0.325 +/- 0.0325. Against the position test's center (reading a) r is 0.447 to 0.474 with the inferred center, and positive with p < 0.001 whichever of the five positions is taken as the center (0.279 to 0.567).",
"position-examples-invariant": "**Result: not reproduced.** Under the claims file's rule, M2p9 is the session whose shape-responsive count is within 10% of 16, reading (a), the files' p12 (16 neurons); there the similarity patterns are not shown to agree across positions (reading a fails for every choice of center) and no position has two or more neurons with significant Isimilarity under reliability (a). M2p28 (the files' p28, 55 neurons) fails both readings: neurons with significant Isimilarity number up to 2 (reliability a) or 3 to 16 (b) per position, against at most 1. With the files' label p09 for M2p9 (18 neurons), both readings hold for M2p9.",
}
src=open('cells.py').read()
for cid, text in R.items():
    i = src.index(f"# %% tags=claim:{cid}\n")
    j = src.index("# %% [markdown]", i)
    k = src.index("# %%", j + 5)
    md = "# %% [markdown]\n" + "\n".join("# " + l for l in __import__("textwrap").wrap(text, 98)) + "\n\n"
    src = src[:j] + md + src[k:]
open('cells.py','w').write(src)
EOF
python results.py && grep -c "Result:" cells.py
```

```
21
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
import re
i=s.index('**Result: not reproduced.** Over 985 texture'); j=s.index('# %%', i)
t='''**Result: not reproduced.** Over 985 texture neurons in 51 penetrations (6 to 83 per penetration),
# no reading puts the counts within tolerance. The closest, original or reversed textures under
# reliability (a), give 193 and 198 neurons (207 +/- 20.7) but 30 and 27 penetrations (34 +/- 3.4),
# 4 and 2 penetrations in M1 (7) and 12 and 7 neurons in M1 (18). Reliability (b) gives 276 to 395
# neurons in 37 to 42 penetrations, 41 to 79 of them in M1. Under every reading a minority of the
# neurons with a line is clustered (27% to 41%).

'''
s=s[:i]+t+s[j:]
s=s.replace('''R["total_and_pens"] = R[["sig_ok", "pens_ok", "pens_5plus_ok", "most_ok"]].all(axis=1)''','''R["total_and_pens"] = R[["sig_ok", "pens_ok", "pens_5plus_ok", "most_ok"]].all(axis=1)
R["frac_of_lines"] = (R.sig / R.lines).round(3)''')
s=s.replace('''but 0.0295 to 0.0317 within''','''but 0.0295 to 0.0317 within''').replace('(matching 0.0022 for bright shapes over all sessions)','(within 0.0022 +/- 0.00022 for bright shapes and for both contrasts over all sessions)').replace('0.073 within 200 um and 0.019 to 0.022 beyond','0.073 to 0.074 within 200 um and 0.019 to 0.022 beyond')
open('cells.py','w').write(s)
EOF
grep -n "M2p6 (paper" -A5 /dev/null; cd $TMPDIR && . dev/bin/activate && timeout 3000 python dev.py 0 30 2>&1 | sed -n '/cell 16/,/cell 18/p'
```

```
===== cell 16 
M2p6 (paper's count: 24 )
reading     date label  responsive  accepted
      a 20210417   p09          18     False
      b 20210416   p08          18     False
      c 20210414   p06          24      True
M1p12 (paper's count: 42 )
reading     date label  responsive  accepted
      a 20191025   p13          13     False
      b 20191025   p13          13     False
      c 20191024   p12          42      True
M2p9 (paper's count: 16 )
reading     date label  responsive  accepted
      a 20210421   p12          16      True
      b 20210420   p11          11     False
      c 20210417   p09          18     False
M2p28 (paper's count: 55 )
reading     date label  responsive  accepted
      a 20210529   p40           1     False
      b 20210527   p37          24     False
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
s=s.replace("(readings a and b give sessions with 13 and 16 responsive neurons)","(readings a and b both give sessions with 18 responsive neurons)")
i=s.index('# ## Summary')
s=s[:i]+'''# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | methods-sessions-and-neurons | reproduced |
# | ex-m2p6-cluster | partially reproduced |
# | ex-m2p6-pairs | partially reproduced |
# | ex-m2p6-invariance | reproduced |
# | ex-csd-sinks | blocked (data missing) |
# | ex-m1p12-no-cluster | reproduced |
# | ex-m1p12-strong-responses | reproduced |
# | pop-significant-isimilarity | partially reproduced |
# | pop-intercept-slope-correlation | reproduced |
# | pop-dark-bright-consistent | not reproduced |
# | pop-contrast-invariance | reproduced |
# | pop-sparse-across-penetrations | reproduced |
# | pop-asymptote-20-percent | reproduced |
# | pop-mean-isimilarity-yield | reproduced |
# | pop-recording-density | reproduced |
# | pop-within-vs-across-sessions | partially reproduced |
# | orientation-sf-isimilarity | blocked (data missing: shape images) |
# | orientation-auc-coarse-clusters | not reproduced |
# | apc-peaks-sparse-clustering | blocked (data missing: shape descriptions) |
# | apc-example-m2p51 | blocked (data missing: shape descriptions) |
# | gyrus-penetrations-consistent | blocked (metadata insufficient) |
# | texture-sparse-clusters | not reproduced |
# | texture-original-reversed-consistent | not reproduced |
# | texture-asymptote-20-percent | not reproduced |
# | position-optimal-consistent | reproduced |
# | position-examples-invariant | not reproduced |
# | simulation-random-with-domains | blocked (methods underspecified) |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **How the analysis differs from the paper's.** Depth is the best channel's position in 20 um steps,
# as the files give it, not the template center of mass. The noise-corrected correlation is written
# here from the Methods' description and Pospisil and Bair (2021), for unequal repeats; the paper's
# MATLAB code is not public. The bootstrap interval's level (95%) and the reading of "confidence
# limit > 0.5" (width or half-width) are not stated, and both readings are run. The bootstrap of the
# corrected estimator sits below the point estimate (resampling with replacement inflates the noise
# it corrects for); only its width is used. Example penetrations are found by the files' `pen_ID`
# labels, which give the paper's neuron counts for M2p6, M1p12 and M2p28.
#
# **What was found about the dataset.** The files hold the shape, texture and position tests with
# spike times of good units only; no LF signal, no stimulus images, no RF-mapping data and no grid
# coordinates. The session counts match the Methods, except a 34th position-test file (one unit).
# The shape files hold a third luminance level (8 cd/m2, the background luminance) and the texture
# files a third version (spectral noise) that the paper does not use; the trial tables of the
# position files name their session `...SL`; positions are coded 0 to 4 without saying which is the
# center, and shapes 0 to 14 without saying which shape each is; texture rotations are not stored.
'''
open('cells.py','w').write(s)
EOF
cd entries/001357-namima-2025 && python $TMPDIR/build_nb.py $TMPDIR/cells.py reproduce_namima_2025.ipynb && ls
```

```
__pycache__
reproduce_namima_2025.ipynb
v4clusters.py
```

**Agent calls Bash**

```bash
rm -rf __pycache__ && cat > entry.yaml <<'EOF'
schema_version: 1
name: 001357-namima-2025
type: reproduction
title: Sparse clusters of shape and texture tuning in macaque V4 (Namima et al. 2025)
description: Tests the findings of Namima, Kempkes, Zamarashkina, Owen and Pasupathy (2025) on dandiset
  001357, which holds the spike times of Neuropixels units from two monkeys in the shape, texture and
  position tests. It computes noise-corrected tuning similarity between simultaneously recorded neurons,
  its decline with distance along the probe (Isimilarity), contrast invariance, and the comparisons
  across penetrations, textures and stimulus positions. The LF signal, the stimulus images and the
  penetration coordinates are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_namima_2025.ipynb
  title: Reproducing Namima et al. (2025) from dandiset 001357
  runtime_minutes: 8
helpers:
- v4clusters.py
related:
- id: dandi:001357/0.261006.2007
  relation: uses_data
- id: doi:10.1523/jneurosci.1893-23.2024
  relation: reproduces
EOF
printf "h5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\n" > requirements.in
cd  && . $TMPDIR/dev/bin/activate && python tools/entry.py lock entries/001357-namima-2025 2>&1 | tail -3 && python tools/entry.py check entries/001357-namima-2025 2>&1 | tail -10
```

```
wrote entries/001357-namima-2025/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && date -u && time python tools/entry.py run entries/001357-namima-2025 2>&1 | tail -15; date -u
```

```
Mon Nov  2 07:33:07 UTC 2026
Installed kernelspec registry-001357-namima-2025 in executed/001357-namima-2025/.venv/share/jupyter/kernels/registry-001357-namima-2025
pass  reproduce_namima_2025.ipynb  (382 s)

real	6m25.021s
user	4m2.082s
sys	0m5.255s
Mon Nov  2 07:39:32 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/001357-namima-2025/reproduce_namima_2025.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code' and ('sanity' in c.metadata.get('tags',[]) or 'claim:methods-sessions-and-neurons' in c.metadata.get('tags',[]) or c.source.startswith('t0 = time.time()\nmeta')):
        for o in c.outputs:
            if 'text' in o: print(o['text'][:6000])
"
```

```
High-Density Recording Reveals Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4
version 0.261006.2007 | files 159 | subjects 2 | variables ['Units', 'ElectrodeGroup']
We used high-density Neuropixels probes in two awake monkeys (one female and one male) to characterize the shape and texture tuning of dozens of neurons simultaneously. The shape set included 15 simple geometric shapes each presented at eight different rotations in 45° increments, resulting in a total of 120 shape stimuli. Shapes were filled with a uniform color, either darker or brighter than the background luminance. The texture stimulus set was composed of 40 naturalistic grayscale textures. Each texture image was presented in three versions: original, contrast-reversed, or spectrally-match

subject  monkey  kind
Z08115   M1      SL      30
                 TX      17
Z11111   M2      SL      44
                 SP      34
                 TX      34

loaded 159 files in 154 s

Files by monkey and test, with good units (is_sua = 1) and presentations:
             files  units   sua  presentations sexes                      descriptions
monkey kind                                                                           
M1     SL       30   1167  1167          63337   {F}                 {V4 shape screen}
       TX       17    461   461          15936   {F}               {V4 texture screen}
M2     SL       44   1129  1129          94966   {M}                 {V4 shape screen}
       SP       34    888   888          21292   {M}  {V4 shape screen. position test}
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle,numpy as np
from scipy import stats
S=pickle.load(open('cache2.pkl','rb'))
bad=[]
for s in S:
    b=(s['trials'].cond_ID==0).to_numpy()
    dt=(s['counts'][:,~b].mean(1)-s['counts'][:,b].mean(1))/0.17
    ds=(s['shifted'][:,~b].mean(1)-s['shifted'][:,b].mean(1))/0.17
    p=stats.wilcoxon(dt).pvalue if len(dt)>1 else np.nan
    if not (dt.mean()>0 and p<0.05): bad.append((s['meta']['session_id'],len(dt),round(dt.mean(),2),round(ds.mean(),2),p))
print(len(bad)); print(bad)
for s in S:
  if s['meta']['session_id'][:8] in ('20210415','20210428','20210530','20210602','20210613'): print(s['meta']['session_id'], s['units'].pen_ID.iloc[0], len(s['units']))
"
```

```
58
[('20190723SL', 41, np.float64(3.01), np.float64(0.43), np.float64(0.05795002135891991)), ('20190802SL', 87, np.float64(2.38), np.float64(-0.46), np.float64(0.05683529977790903)), ('20191028SL', 22, np.float64(0.19), np.float64(-0.48), np.float64(0.8485937118530273)), ('20191101SL', 16, np.float64(1.04), np.float64(0.37), np.float64(0.433197021484375)), ('20191114SL', 6, np.float64(7.59), np.float64(2.08), np.float64(0.0625)), ('20191118SL', 9, np.float64(0.31), np.float64(-0.85), np.float64(1.0)), ('20191121SL', 40, np.float64(1.11), np.float64(-0.35), np.float64(0.7648249070225575)), ('20200109SL', 52, np.float64(0.85), np.float64(-0.44), np.float64(0.07727147253145507)), ('20200117SL', 42, np.float64(1.55), np.float64(0.62), np.float64(0.13511890654692407)), ('20200318SL', 27, np.float64(0.68), np.float64(-0.34), np.float64(0.29008127748966217)), ('20200630TX', 19, np.float64(0.97), np.float64(0.53), np.float64(0.4413337707519531)), ('20200703TX', 26, np.float64(2.95), np.float64(-2.51), np.float64(0.12266942858695984)), ('20200709TX', 67, np.float64(1.4), np.float64(0.85), np.float64(0.9203861585574784)), ('20200712TX', 16, np.float64(0.1), np.float64(-0.58), np.float64(0.860260009765625)), ('20200716TX', 28, np.float64(7.87), np.float64(-2.66), np.float64(0.27407141774892807)), ('20200718TX', 8, np.float64(13.01), np.float64(1.64), np.float64(0.0546875)), ('20200719TX', 20, np.float64(3.65), np.float64(-1.39), np.float64(0.20244979858398438)), ('20200720TX', 28, np.float64(1.34), np.float64(-0.18), np.float64(0.5670346617698669)), ('20200723TX', 51, np.float64(-0.55), np.float64(-1.36), np.float64(0.693811571572745)), ('20200730TX', 31, np.float64(4.03), np.float64(-0.46), np.float64(0.12031982094049454)), ('20200804TX', 22, np.float64(-0.93), np.float64(1.84), np.float64(0.27562665939331055)), ('20200805TX', 18, np.float64(3.81), np.float64(-0.5), np.float64(0.12973785400390625)), ('20210417SP', 20, np.float64(0.77), np.float64(-0.15), np.float64(0.15596752
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
i=s.index("# %% [markdown]\n# Clock check."); j=s.index("# %% [markdown]\n# ### Shape analyses")
new='''# %% [markdown]
# Clock check. If spikes and presentations share a clock, many units' counts in the 30 to 200 ms
# window differ between stimuli (a one-way ANOVA over the stimuli of the file, per unit), and with
# the onsets moved by -1.3 s, onto other presentations or the gaps, that contrast should fall to
# the false-positive rate. Per file, the fraction of units with p < 0.01 is compared between true and
# shifted onsets; the clock is taken as established in a file when the true fraction exceeds 1% with
# a binomial p < 0.01 and exceeds the shifted fraction.

# %% tags=sanity
def stim_key(s):
    tr = s["trials"]
    k = s["asset"]["kind"]
    other = {"SL": "luminance", "TX": "mode", "SP": "position"}[k]
    sel = (tr.cond_ID != 0).to_numpy() & tr.stim_ID.notna().to_numpy()
    if k == "SL":
        sel &= tr.luminance.isin([V.DARK, V.BRIGHT]).to_numpy()
    key = tr.stim_ID.astype(str) + "_" + tr[other].astype(str) + ("_" + tr.rotation.astype(str) if k == "SL" else "")
    return sel, key.to_numpy()

clock = []
for s in sess:
    sel, key = stim_key(s)
    groups = [np.flatnonzero(sel & (key == g)) for g in np.unique(key[sel])]
    groups = [g for g in groups if len(g) > 1]
    fr = {}
    for name, cnt in (("true", s["counts"]), ("shifted", s["shifted"])):
        with np.errstate(all="ignore"):
            p = np.array([stats.f_oneway(*[cnt[u, g] for g in groups]).pvalue for u in range(cnt.shape[0])])
        fr[name] = np.nanmean(p < 0.01)
    n = s["counts"].shape[0]
    clock.append({"kind": s["asset"]["kind"], "date": s["asset"]["date"], "units": n, "true": fr["true"], "shifted": fr["shifted"],
                  "p_binom": stats.binomtest(int(round(fr["true"] * n)), n, 0.01, alternative="greater").pvalue})
clock = pd.DataFrame(clock)
clock["established"] = (clock.p_binom < 0.01) & (clock.true > clock.shifted)
print("Fraction of units whose counts differ between stimuli (ANOVA p < 0.01), per file:")
print(clock.groupby("kind").agg(files=("date", "size"), true_median=("true", "median"), true_min=("true", "min"),
      shifted_median=("shifted", "median"), shifted_max=("shifted", "max"), established=("established", "sum")).to_string())
print("Files where it is not established:", clock[~clock.established][["kind", "date", "units", "true", "shifted"]].round(3).to_dict("records"))

'''
s=s[:i]+new+s[j:]
s=s.replace('''    "spikes_in_trials": (s["meta"]["spike_range"][0] >= s["meta"]["trial_range"][0] - 1)
                        and (s["meta"]["spike_range"][1] <= s["meta"]["trial_range"][1] + 1),''','''    "spikes_beyond_trials_s": max(s["meta"]["trial_range"][0] - s["meta"]["spike_range"][0],
                                  s["meta"]["spike_range"][1] - s["meta"]["trial_range"][1], 0),''')
s=s.replace('''print("Spike times sorted in every file:", bool(info.spikes_sorted.all()),
      "| spikes within the trial span (1 s margin):", int(info.spikes_in_trials.sum()), "of", len(info))''','''print("Spike times sorted in every file:", bool(info.spikes_sorted.all()),
      "| spikes extend beyond the file's trials by up to", round(info.spikes_beyond_trials_s.max(), 1), "s; files with more than 1 s:",
      int((info.spikes_beyond_trials_s > 1).sum()))''')
s=s.replace('''print(f"M2 texture days that also have a shape file: {len(tx2 & sl2)} of {len(tx2)}; texture-only days: {sorted(tx2 - sl2)}")''','''print(f"M2 texture days that also have a shape file: {len(tx2 & sl2)} of {len(tx2)}; texture-only days and labels:",
      [(d, by_date[("M2", d)]["TX"]["units"].pen_ID.iloc[0]) for d in sorted(tx2 - sl2)])''')
open('cells.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && timeout 3000 python dev.py 0 14 2>&1 | grep -v Warn | tail -30
```

```
SL       74     0.726965  0.225000             0.0     0.166667           73
SP       34     0.723355  0.259259             0.0     0.142857           33
TX       51     0.730769  0.000000             0.0     0.062500           46
Files where it is not established: [{'kind': 'TX', 'date': '20200715', 'units': 25, 'true': 0.04, 'shifted': 0.0}, {'kind': 'TX', 'date': '20200719', 'units': 20, 'true': 0.0, 'shifted': 0.0}, {'kind': 'TX', 'date': '20200729', 'units': 17, 'true': 0.118, 'shifted': 0.0}, {'kind': 'TX', 'date': '20200730', 'units': 31, 'true': 0.065, 'shifted': 0.0}, {'kind': 'TX', 'date': '20200804', 'units': 22, 'true': 0.045, 'shifted': 0.0}, {'kind': 'SL', 'date': '20210529', 'units': 1, 'true': 1.0, 'shifted': 0.0}, {'kind': 'SP', 'date': '20210529', 'units': 1, 'true': 1.0, 'shifted': 0.0}]
----- 82.7s
===== cell 10 
shape analyses in 89 s; 1869 responsive neurons in 74 penetrations
Mean fraction of reliable off-diagonal dark similarities per penetration: {'a': np.float64(0.748), 'b': np.float64(0.777)}
----- 89.3s
===== cell 12 
texture analyses in 37 s
----- 37.0s
===== cell 13 tags=claim:methods-sessions-and-neurons
                     quantity  measured  expected  tolerance  within
           shape sessions, M1        30        30        3.0    True
           shape sessions, M2        44        44        4.4    True
         texture sessions, M1        17        17        1.7    True
         texture sessions, M2        34        34        3.4    True
position control sessions, M2        34        33        3.3    True
    responsive neurons, shape      1869      1850      185.0    True
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; cat questions/$(ls questions | head -1) | head -40; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:5000])" 2>/dev/null | head -150
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
dandiset: "000005"
paper: doi:10.1038/nn.4412
questions:
- claim: fs-vm-touch-whisking
  asked: 2026-10-20
  question: At what resolution is dVm/dt of the touch-aligned average Vm taken for the latency rule,
    the recording's own sampling rate (10 or 20 kHz) or the average in 1 ms bins as for the spike
    PSTH? The same question applies to the laser-onset latencies of exc-thalamus-photoinhibition and
    to exc-vm-touch-whisking.
  passage: Touch latency was identified as the latency from touch onset to the time when dVm/dt
    crossed baseline (3x s.d. of the dVm/dt between 0 and 25 ms before touch). All touch-spike PSTHs
    were constructed with a bin size of 1 ms. (Online Methods, Data analysis)
  why: At the full sampling rate two of the five whole-cell FS cells cross the threshold at 0.0 and
    0.3 ms and the mean latency is 1.88 ms (not reproduced); in 1 ms bins the mean over three cells
    is 3.67 to 4.17 ms (within 4.0 +- 0.4). For the thalamic and cortical light the full rate gives
    0.1 ms for both, the 1 ms bins 5.0 and 2.0 ms.
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(json.dumps(p['outcomes'],indent=0)[:3500]); print(json.dumps(p['findings'],indent=0)[:1500]); print(json.dumps(p['inputs'],indent=0)[:600]); print(list(p))"
```

```
{
"description": "One per claim attempted.",
"type": "array",
"minItems": 1,
"items": {
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
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/cells.py entries/001357-namima-2025/reproduce_namima_2025.ipynb && python tools/entry.py check entries/001357-namima-2025 | tail -3 && python tools/entry.py run entries/001357-namima-2025 2>&1 | tail -2; date -u
```

```
0 error(s)
Installed kernelspec registry-001357-namima-2025 in executed/001357-namima-2025/.venv/share/jupyter/kernels/registry-001357-namima-2025
pass  reproduce_namima_2025.ipynb  (457 s)
Mon Nov  2 07:51:40 UTC 2026
```

**Agent**

Now verify the executed outputs against each conclusion.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/001357-namima-2025/reproduce_namima_2025.ipynb',4)
for i,c in enumerate(nb.cells):
    tags=c.metadata.get('tags',[])
    if c.cell_type=='code' and any(t.startswith('claim:') for t in tags) and tags[0] not in ('claim:methods-sessions-and-neurons',):
        print('#####',tags)
        for o in c.outputs:
            if 'text' in o: print(o['text'][:4000])
    if c.cell_type=='markdown' and c.source.startswith('**Result'): print('>>>',c.source[:3000]); print()
" > $TMPDIR/exec_out.txt; wc -l $TMPDIR/exec_out.txt; diff <(grep -v "^>>>" $TMPDIR/exec_out.txt | head -0) /dev/null; grep -n "M2p6 = \|reliability a: 20\|reliable invariance above 0.5 for\|stim_ID taken\|^ *0  mixed" $TMPDIR/exec_out.txt | head
```

```
504 /tmp/claude-1001/exec_out.txt
8:M2p6 = ('M2', '20210414') | responsive neurons 24 | span of depths 2340.0 um
69:reliability a: 20 of 24 neurons with reliable invariance above 0.5 (expected 19 +/- 1.9); unreliable 2
90:reliability a: reliable invariance above 0.5 for 35 of 42 (83%); unreliable 1
91:reliability b: reliable invariance above 0.5 for 36 of 42 (86%); unreliable 0
313:Variant, each stim_ID taken as the spindle:
315:       0  mixed (2 changes) mixed (12 changes)        2          2
334:its two deepest bins (2 changes), and M1p5 changes side 12 times. No stim_ID taken as the spindle
```

**Agent calls Bash**

```bash
cd $TMPDIR; for k in "  381 " "r = 0.484" "0.632" "0.2968" "0.3252" "  193 " "r = 0.706" "0.2571" "SD of penetration means, >30 neurons 0.089" "-0.768378" "mixed (2 changes)" "13 neurons\|(13)"; do printf "%s: " "$k"; grep -c -- "$k" exec_out.txt; done; sed -n '/position-examples/,$p' exec_out.txt | grep -v "pair correlations" | head -40
```

```
381 : 1
r = 0.484: 2
0.632: 2
0.2968: 1
0.3252: 1
  193 : 1
r = 0.706: 2
0.2571: 1
SD of penetration means, >30 neurons 0.089: 1
-0.768378: 1
mixed (2 changes): 4
13 neurons\|(13): 5
##### ['claim:position-examples-invariant']
M2p9 reading a: ('M2', '20210421') (p12), shape-responsive 16, position-responsive 14; Figure 11 n = 16; accepted: True

   reliability a: (a) holds with center = {0: False, 1: False, 2: False, 3: False, 4: False}; (b) significant positive Isimilarity per position {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, lines [0, 0, 0, 0, 0]; reliable pairs [0, 1, 1, 0, 0] of 120
   reliability b: (a) holds with center = {0: False, 1: False, 2: False, 3: False, 4: False}; (b) significant positive Isimilarity per position {0: 2, 1: 1, 2: 0, 3: 3, 4: 3}, lines [4, 10, 4, 8, 11]; reliable pairs [14, 27, 13, 21, 39] of 120
M2p9 reading b: 20210420 has no position test
M2p9 reading c: ('M2', '20210417') (p09), shape-responsive 18, position-responsive 12; Figure 11 n = 16; accepted: False

[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cat > entries/001357-namima-2025/README.md <<'EOF'
# Namima, Kempkes, Zamarashkina, Owen & Pasupathy (2025) from dandiset 001357

Tests the findings of [Namima et al. (2025)](https://doi.org/10.1523/jneurosci.1893-23.2024) that can
be tested on [DANDI:001357](https://dandiarchive.org/dandiset/001357/0.261006.2007), which holds the
spike times of Neuropixels units in V4 of two monkeys during the shape test (74 sessions), the texture
test (51) and the position control (34).

| Claim | Outcome |
|---|---|
| Session and neuron counts | Reproduced |
| M2p6: a cluster of similarly tuned superficial neurons | Partially reproduced |
| M2p6: similarity of two example pairs | Partially reproduced |
| M2p6: contrast invariance in 19 of 24 neurons | Reproduced |
| M2p6 and M1p12: CSD sinks | Blocked: no LF signal in the dandiset |
| M1p12: no cluster, high invariance | Reproduced |
| M1p12: strong peak responses | Reproduced |
| 344 of 1,850 neurons with significant Isimilarity | Partially reproduced |
| Isimilarity and Ssimilarity correlated, r = -0.745 | Reproduced |
| Dark and bright Isimilarity consistent, r = 0.435 | Not reproduced |
| Median contrast invariance 0.64 | Reproduced |
| Clusters in 55 of 74 penetrations, 28 with five or more | Reproduced |
| About 20% significant when more than 30 neurons | Reproduced |
| Mean Isimilarity levels off with yield | Reproduced |
| Weak relation to recording density, r = 0.236 | Reproduced |
| Same-session pairs slightly more similar | Partially reproduced |
| Orientation x SF fits | Blocked: shape images not public |
| Coarse orientation preference along the probe | Not reproduced |
| APC peak clustering (two claims) | Blocked: shape descriptions not public |
| 18 gyral penetrations | Blocked: penetration coordinates not in the dandiset |
| Texture: 207 of 979 neurons clustered | Not reproduced |
| Texture: original and reversed Isimilarity consistent, r = 0.464 | Not reproduced |
| Texture: about 20% significant in large penetrations | Not reproduced |
| Isimilarity at the optimal position, r = 0.325 | Reproduced |
| Example penetrations at five positions | Not reproduced |
| Simulation of tuning progressions | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001357-namima-2025-01.yaml`](../../attempts/001357-namima-2025-01.yaml).

- `reproduce_namima_2025.ipynb`: the analysis. It takes about eight minutes, half of it streaming the
  files.
- `v4clusters.py`: loading the files into spike counts per presentation, the noise-corrected
  correlation with its bootstrap, Isimilarity, and the per-session analyses. Other notebooks on this
  dandiset can import it.
EOF
cat > questions/001357.yaml <<'EOF'
dandiset: "001357"
paper: doi:10.1523/jneurosci.1893-23.2024
questions:
- claim: position-examples-invariant
  asked: 2026-11-02
  question: The criterion accepts a session as M2p9 or M2p28 when its neuron count is within 10% of
    16 or 55, the n of Figure 11. Is that n the number of neurons in the similarity matrices? The
    legend defines it as the number of neurons with quantified RF centers, after leaving out neurons
    whose RF could not be estimated.
  passage: Eight neurons that failed to yield an RF estimate are not depicted ... Inset n indicates
    neuron numbers with quantified RF centers. (Figure 11 legend, B)
  why: The dataset labels penetrations, and its p09 of M2 has 18 shape-responsive neurons, so the
    10% rule rejects it and accepts the session labelled p12 (16 neurons). Under the label p09 both
    readings of the claim hold for M2p9; under p12 neither does. The outcome of the claim, not
    reproduced either way because M2p28 fails, does not change, but the M2p9 half does.
EOF
date -u
```

```
Mon Nov  2 07:52:03 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && cat > $TMPDIR/record.py <<'EOF'
import yaml
NB = "reproduce_namima_2025.ipynb"
DEV_DEPTH = ("Depth is the unit's best-channel position from the files (20 um steps, `depth`, distance from the tip), "
             "measured from the most superficial good unit; the template center of mass of the Methods is not in the files.")
DEV_NC = ("The noise-corrected correlation was written from the Methods' description and Pospisil and Bair (2021) "
          "(Materials and Methods, Tuning similarity and contrast invariance); its bias terms are written for unequal "
          "repeats per stimulus (3 to 10 here), which reduce to the published terms with equal repeats. The paper's code is not public.")
DEV_BOOT = ("The bootstrap resamples each stimulus's repeats (500 times), with the same indices for all neurons of a session. "
            "Its distribution sits below the point estimate, since resampling with replacement inflates the noise the estimator "
            "corrects for; only its width decides reliability. Both readings of the reliability rule (width or half-width above 0.5) are run.")
DEV_PEN = "Penetrations are found by the files' `pen_ID` label (reading c of the claims file); readings a and b give other sessions whose counts do not match."
def o(claim, outcome, notes, measured=None, deviations=None, blocked_by=None, assumed=None, output=True):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if output and outcome != "blocked":
        d["notebook"] = NB; d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed is not None: d["assumed"] = assumed
    return d

outcomes = [
o("methods-sessions-and-neurons", "reproduced",
  "The files hold 30 and 44 shape sessions (M1, M2), 17 and 34 texture sessions, and 34 position-test sessions "
  "(expected 33 within 3.3; one holds a single unit). 1,869 shape neurons are responsive and 427 excluded, 985 texture "
  "neurons responsive and 360 excluded, all within tolerance. The texture files' good units sum to the paper's 1,345 exactly; "
  "the shape files hold 2,296 against 2,311.",
  [30, 44, 17, 34, 34, 1869, 985, 427, 360],
  ["Texture responsiveness uses the original and contrast-reversed textures; the spectral-noise version in the files is left out, as the paper does not use it.",
   "Shape responsiveness uses the dark (4 cd/m2) and bright (12 cd/m2) shapes; the files' third luminance level (8 cd/m2) is left out."]),
o("ex-m2p6-cluster", "partially_reproduced",
  "The files' p06 of M2 (2021-04-14) has 24 responsive neurons spanning 2,340 um; neurons 1 to 9 lie over 540 um and are similarly "
  "tuned at both contrasts (mean similarity 0.70 dark, 0.86 bright, against -0.02 with deeper neurons). With dark shapes 13 neurons "
  "have a significant positive Isimilarity under both reliability readings, all with negative slopes; neurons 1 to 9 and 14 as in "
  "the paper, plus 12, 21 and 22, without 17. Count and set are outside the margin of one neuron.",
  [24, 2340, 13], [DEV_PEN, DEV_DEPTH, DEV_NC, DEV_BOOT]),
o("ex-m2p6-pairs", "partially_reproduced",
  "Neurons 3 and 8 are 260 um apart with similarity 0.780 (dark) and 0.894 (bright); neurons 18 and 19 are 80 um apart with dark "
  "similarity 0.000. All within tolerance. The bright similarity of 18 and 19 is -0.144 against -0.25 within 0.025. The template "
  "center-of-mass variant of distance cannot be run, as the files give only the best channel.",
  [0.780, 0.894, 0.0, -0.144, 260, 80], [DEV_PEN, DEV_DEPTH, DEV_NC]),
o("ex-m2p6-invariance", "reproduced",
  "Under reliability reading (a) 20 of 24 neurons have a reliable invariance above 0.5 (19 within 1.9); under reading (b) 22. "
  "The median invariance is 0.955 among neurons with a significant Isimilarity and 0.954 among the others.",
  20, [DEV_PEN, DEV_NC, DEV_BOOT]),
o("ex-csd-sinks", "blocked",
  "Needs the LF signal. The files hold spike times only; `acquisition` and `processing` are empty in all 159 files, and the "
  "archive's assets summary lists only Units and ElectrodeGroup. The paper names no other archive for the LF data.",
  blocked_by="data_missing"),
o("ex-m1p12-no-cluster", "reproduced",
  "The files' p12 of M1 (2019-10-24) has 42 responsive neurons over 2,580 um. With dark shapes one neuron has a significant positive "
  "Isimilarity under both reliability readings; 35 (a) or 36 (b) of 42 have reliable invariance above 0.5. With bright shapes 4 "
  "neurons have a significant positive Isimilarity, so the statement's 'at either contrast' holds less cleanly for bright shapes; the criterion judges dark.",
  [42, 2580, 1], [DEV_PEN, DEV_DEPTH, DEV_NC, DEV_BOOT]),
o("ex-m1p12-strong-responses", "reproduced",
  "Baseline-subtracted peaks (reading a) exceed 15 spikes/s in 28 neurons for dark and 26 for bright shapes; raw peaks (reading b) in 29 and 31.",
  [28, 26], [DEV_PEN]),
o("pop-significant-isimilarity", "partially_reproduced",
  "Under all 12 readings a minority of the neurons with a line has a significantly positive Isimilarity (22% to 34%), nearly all "
  "with a negative slope, but no reading puts the four counts within tolerance. The closest, bright shapes, reliability (a), rule (ii), "
  "gives 381 (226 in M1, 155 in M2) and 1,349 not significant; dark (a)(i) gives 400 (233, 167) and 1,329. Penetrations hold 1 to 77 "
  "responsive neurons; the single-neuron one is M2 p40 (2021-05-29), and the next smallest hold 6. Neurons with a line number 1,729 "
  "to 1,847 against the paper's 1,848. The criterion gives no rule for a partial outcome; the minority the statement describes holds "
  "and the counts do not, which is the protocol's partially reproduced.",
  [400, 233, 167, 1329, 1, 77], [DEV_NC, DEV_BOOT, DEV_DEPTH]),
o("pop-intercept-slope-correlation", "reproduced",
  "Pearson's r between Isimilarity and Ssimilarity with dark shapes is -0.768 (reliability a, n = 1,729) and -0.735 (b, n = 1,805), "
  "p far below 0.0001; with bright shapes -0.667 and -0.653 (outside tolerance). Spearman's r is -0.777 to -0.817. No neuron has both "
  "a significantly positive Isimilarity and Ssimilarity; the paper reports one.",
  [-0.768, 0], [DEV_NC, DEV_BOOT]),
o("pop-dark-bright-consistent", "not_reproduced",
  "Spearman's r between dark and bright Isimilarity is 0.484 (reliability a, n = 1,643) and 0.520 (b, n = 1,757), p below 1e-90, "
  "above 0.435 within 0.0435. The consistency the statement describes holds, more strongly than reported.",
  0.484, [DEV_NC, DEV_BOOT]),
o("pop-contrast-invariance", "reproduced",
  "Under reliability (b), with unreliable values counted as 0, the median invariance is 0.632 over all 1,869 neurons and 0.619 over "
  "per-penetration medians, within 0.64 of 0.064; 54.7% of neurons have reliable invariance above 0.5 (49.1% under reading a). "
  "Leaving unreliable values out gives 0.764 to 0.770; reading (a) with unreliable as 0 gives 0.474 and 0.513.",
  0.632, [DEV_NC, DEV_BOOT]),
o("pop-sparse-across-penetrations", "reproduced",
  "Under the eight dark and bright readings 54 to 59 penetrations have a neuron with significant positive Isimilarity and 27 to 29 have "
  "five or more; 20 penetrations have more than 30 responsive neurons. Counting either contrast gives 62 and 39 to 41.",
  [58, 27, 20], [DEV_NC, DEV_BOOT]),
o("pop-asymptote-20-percent", "reproduced",
  "Over the 20 penetrations with more than 30 neurons, the pooled percentage is 21.1% to 21.5% with dark or bright shapes under "
  "reliability (a) and the median per penetration 19.4% to 21.0% under (b). Per penetration it ranges 0% to 60%. Either contrast gives 29% to 36%.",
  21.5, [DEV_NC, DEV_BOOT]),
o("pop-mean-isimilarity-yield", "reproduced",
  "The SD of penetration means is smaller with more than 30 neurons under all four readings; dark (a) 0.089 against 0.204 (Levene "
  "p = 0.015), dark (b) 0.104 against 0.201 (p = 0.041), bright (a) 0.084 against 0.127 (p = 0.051), bright (b) 0.107 against 0.133 "
  "(p = 0.18). No contrast reading reproduces pop-significant-isimilarity, so all are shown, as the criterion asks.",
  None, [DEV_NC, DEV_BOOT]),
o("pop-recording-density", "reproduced",
  "With density as neurons per um, Pearson's r is 0.257 (dark, reliability a, p = 0.028, 73 penetrations), within 0.236 of 0.0236; "
  "bright (a) 0.256. Reliability (b) and either contrast give 0.296 to 0.336. Density as um per neuron, the legend's quotient, gives "
  "-0.355 to -0.456. The penetration with one neuron has no depth range and is left out.",
  0.257, [DEV_NC, DEV_BOOT, DEV_DEPTH]),
o("pop-within-vs-across-sessions", "partially_reproduced",
  "Under all 12 readings same-session pairs are more similar than different-session pairs and pairs within 200 um more than pairs "
  "further apart (Welch p below 1e-4). No reading matches all four means. Pearson's r of mean rates gives 0.0021 to 0.0036 across "
  "sessions, 0.0295 to 0.0317 within (0.0582), 0.073 to 0.074 within 200 um (0.0918) and 0.019 to 0.022 beyond (0.0435); the "
  "noise-corrected values are 0.006 to 0.009, 0.083 to 0.090, 0.195 and 0.056 to 0.066. All means are weak.",
  [0.0025, 0.0295, 0.0732, 0.0191],
  [DEV_NC, "The noise-corrected reading uses point estimates for all pairs so that same- and different-session pairs are treated alike; reliable same-session pairs are a variant."]),
o("orientation-sf-isimilarity", "blocked",
  "Needs the 120 shape images to compute Gabor filter outputs. The dandiset holds none (`stimulus/templates` is empty) and does not "
  "say which shape each stim_ID is. A search for a public, pinned copy of the Pasupathy and Connor (2001) shapes (the shape lab's "
  "publication pages, Pospisil et al. 2018 eLife, github.com/deanpospisil/er_est, the SparseShape OSF project) found none; other "
  "groups report obtaining them from the lab.",
  blocked_by="data_missing"),
o("orientation-auc-coarse-clusters", "not_reproduced",
  "With stim_ID 0 as the spindle, 2 of 74 penetrations are all one preference and 2 switch once, so both kinds exist, but M2p6 "
  "(horizontal from 0 to 500 um, vertical below, horizontal in its two deepest bins; 2 changes) and M1p5 (12 changes) are of neither "
  "kind. Under every stim_ID taken as the spindle, neither penetration is of one kind (M2p6 2 to 12 changes, M1p5 7 to 15), so the "
  "outcome does not rest on that mapping.",
  None, ["The files number shapes 0 to 14 without saying which is the spindle; stim_ID 0 is taken as Shape 1 of Figure 1B, and all 15 are shown.",
         "Rotations 0 and 180 are taken as horizontal, 90 and 270 as vertical (Materials and Methods, Feature models).", DEV_PEN]),
o("apc-peaks-sparse-clustering", "blocked",
  "Needs the boundary curvature and angular position descriptions of the shapes (Pasupathy and Connor 2001) and which stim_ID is "
  "which shape. Neither is in the dandiset or, as far as a search found, public and pinned (see orientation-sf-isimilarity).",
  blocked_by="data_missing"),
o("apc-example-m2p51", "blocked",
  "Depends on apc-peaks-sparse-clustering, blocked for the same missing shape descriptions. The files' p51 of M2 (2021-06-11) has 48 shape-responsive neurons.",
  blocked_by="data_missing"),
o("gyrus-penetrations-consistent", "blocked",
  "The 18 gyral penetrations are identified only by grid location and RF azimuth (Figure 8B). The files give neither the grid "
  "coordinates nor RF-mapping data; the electrode table's location is 'V4' for every channel.",
  blocked_by="metadata_insufficient"),
o("texture-sparse-clusters", "not_reproduced",
  "985 texture neurons in 51 penetrations (6 to 83 each). No reading puts the counts within tolerance. Original and reversed textures "
  "under reliability (a) give 193 and 198 neurons (207) but 30 and 27 penetrations (34), 4 and 2 in M1 (7), and 12 and 7 M1 neurons (18). "
  "Reliability (b) gives 276 to 395 neurons in 37 to 42 penetrations. A minority of neurons with a line is clustered under every "
  "reading (27% to 41%). Neurons without a line are 304 and 322 under (a) and 62 and 44 under (b), against the paper's 48, which "
  "points to reading (b) for the paper's reliability rule.",
  [193, 12, 181, 30, 4, 26, 15, 83], [DEV_NC, DEV_BOOT, "Rotations are pooled per texture; the files do not store the rotation of each presentation."]),
o("texture-original-reversed-consistent", "not_reproduced",
  "Spearman's r between original and reversed texture Isimilarity is 0.706 (reliability a, n = 624) and 0.642 (b, n = 894), p below "
  "1e-90, against 0.464 within 0.0464. The neuron count under (b) is within 905 of 90.5. The consistency holds, more strongly than reported.",
  [0.642, 894], [DEV_NC, DEV_BOOT]),
o("texture-asymptote-20-percent", "not_reproduced",
  "Seven texture penetrations have more than 30 neurons; the percentage with significant Isimilarity is 25.6% to 52.1% pooled and "
  "28.9% to 51.4% as a median under every reading, above 20 of 2.",
  26.8, [DEV_NC, DEV_BOOT]),
o("position-optimal-consistent", "reproduced",
  "721 shape-responsive neurons in 33 M2 penetrations (723 in the paper) enter the position test (penetrations with 4 or more). "
  "Isimilarity at the optimal position against the main shape test with dark shapes (reading b) gives Spearman's r = 0.297 "
  "(reliability a, n = 378) and 0.325 (b, n = 676), p below 1e-4. Against the position test's center (reading a), r is 0.447 to "
  "0.474 with the inferred center, and 0.279 to 0.567 (p at most 2.1e-4) whichever position is taken as the center, so every "
  "reading gives a positive r and one is within tolerance.",
  [0.325, 721],
  ["The files code positions 0 to 4 without saying which is the center; the position with the largest mean response of the penetration's responsive neurons is taken as the center (position 1 in 12 files, 2 in 11, others in 11), and all five are shown.",
   "Neurons are those responsive in the main shape test; neurons responsive in the position test are a variant (603 neurons, r = 0.298 and 0.348)."]),
o("position-examples-invariant", "not_reproduced",
  "Under the criterion's rule M2p9 is the session whose responsive count is within 10% of 16, the files' p12 (2021-04-21, 16 neurons); "
  "there reading (a) fails for every choice of center and reading (b) finds 0 to 3 neurons with significant Isimilarity per position. "
  "M2p28 (the files' p28, 55 neurons) fails both readings, with up to 2 (reliability a) or 3 to 16 (b) such neurons per position against "
  "at most 1, and position correlations from -0.06 to 1.00 with few reliable pairs (23 to 60 of 1,485 under a). With the files' label "
  "p09 for M2p9 (18 neurons), both readings hold for M2p9. Whether Figure 11's n is the matrix count is asked of a reader.",
  None, ["Positions are not labelled; reading (a) is evaluated for every choice of center.", DEV_NC, DEV_BOOT]),
o("simulation-random-with-domains", "blocked",
  "A simulation judged by eye, with peak amplitudes and progression step sizes not given, which also needs the shapes' APC descriptions "
  "(not public, see apc-peaks-sparse-clustering). It uses no recorded data, so the dataset cannot test it.",
  blocked_by="methods_underspecified"),
]
record = {
 "schema_version": 2, "id": "001357-namima-2025-01",
 "dataset": {"archive": "dandi", "id": "001357", "version": "0.261006.2007", "doi": "10.48324/dandi.001357/0.261006.2007"},
 "paper": "doi:10.1523/jneurosci.1893-23.2024", "date": "2026-11-02", "entry": "001357-namima-2025",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
   "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-13"},
   "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/41402628393"}},
 "outcomes": outcomes,
 "findings": [
  {"kind": "data_missing", "statement": "The dandiset holds spike times of good units only. The LF signal behind the CSD analysis, the RF-mapping experiment, the stimulus images and the penetrations' grid coordinates are not in it, so the CSD, feature-model and gyral-penetration findings cannot be tested."},
  {"kind": "metadata_insufficient", "statement": "Shapes are coded by stim_ID 0 to 14 and the position test's positions 0 to 4 without saying which shape each code is or which position is the aggregate RF center. The penetration with the largest population response is position 1 in 12 files, 2 in 11 and another in 11, so the center cannot be read from the data either."},
  {"kind": "metadata_error", "statement": "The trial tables of all 34 position-test files give the session as '...SL' (the shape test's code), while their units tables and file names give '...SP'."},
  {"kind": "other", "statement": "The shape files hold a third luminance level, 8 cd/m2 (the background luminance), presented as often as the dark and bright shapes in 73 of 74 files; the paper and the dandiset description mention only dark and bright shapes. The texture files hold the spectral-noise version the description mentions and the paper does not use."},
  {"kind": "other", "statement": "Unit depth is the best channel's distance from the tip in 20 um steps, not the template center of mass the Methods use; it gives the paper's distances for the example pairs (260 and 80 um) and spans (2,340 and 2,580 um)."},
  {"kind": "paper_inconsistency", "statement": "The Methods say shape and texture tests were run in 34 M2 sessions; the dandiset has 34 M2 texture files of which 29 share a day and penetration label with a shape file, and 5 (p07, p17, p40, p42, p53) are texture-only days. The 2021-05-30 texture file is labelled p40, as is the 2021-05-29 shape file."},
  {"kind": "other", "statement": "The position test has 34 files, where the paper reports 33 sessions; one (2021-05-29, p40) holds a single unit. The shape test of the same day is the penetration with one responsive neuron, where the paper reports at least 6 per penetration."},
  {"kind": "other", "statement": "The texture files do not store the rotation of each presentation, which the Methods say was chosen at random from 8."},
  {"kind": "methods_unavailable", "statement": "For the paper's authors. Is a noise-corrected similarity unreliable when the width of its 95% bootstrap interval exceeds 0.5, or its half-width, and what interval level is used? Under the width reading, 1,729 neurons have a regression line with dark shapes and 681 texture neurons with original textures; under the half-width reading 1,805 and 923; the paper has 1,848 and 931. The significant-Isimilarity counts change by 10% to 60% between them. How are unequal repeats per stimulus handled in the bias correction?"},
 ],
 "inputs": [],
}
record.pop("inputs")
with open("attempts/001357-namima-2025-01.yaml", "w") as f:
    yaml.safe_dump(record, f, sort_keys=False, width=110, allow_unicode=True)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/record.py && python tools/entry.py check entries/001357-namima-2025 | tail -5; grep -n "': \|: '" attempts/001357-namima-2025-01.yaml | head
```

```
0 error(s)
5:  id: '001357'
9:date: '2026-11-02'
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
s=s.replace('''rot = pd.concat([s["trials"].rotation for s in sess if s["asset"]["kind"] == "SL"])''','''print("Shape files with luminance 8 presentations:", sum(int((s["trials"].luminance == 8).any()) for s in sess if s["asset"]["kind"] == "SL"),
      "of", sum(s["asset"]["kind"] == "SL" for s in sess))
rot = pd.concat([s["trials"].rotation for s in sess if s["asset"]["kind"] == "SL"])''')
open('cells.py','w').write(s)
s=open('record.py').read()
s=s.replace("[0.642, 894], [DEV_NC, DEV_BOOT]","[0.706, 624], [DEV_NC, DEV_BOOT]")
open('record.py','w').write(s)
EOF
cd  && . $TMPDIR/dev/bin/activate && python $TMPDIR/record.py && python $TMPDIR/build_nb.py $TMPDIR/cells.py entries/001357-namima-2025/reproduce_namima_2025.ipynb && python tools/entry.py all entries/001357-namima-2025 2>&1 | tail -3; date -u
```

```
Installed kernelspec registry-001357-namima-2025 in executed/001357-namima-2025/.venv/share/jupyter/kernels/registry-001357-namima-2025
0 error(s)
pass  reproduce_namima_2025.ipynb  (461 s)
Mon Nov  2 08:01:14 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/001357-namima-2025/reproduce_namima_2025.ipynb',4)
for c in nb.cells:
  if c.cell_type=='code':
    for o in c.outputs:
      if o.get('output_type')=='error': print('ERR', o['ename'])
      if 'text' in o and ('luminance 8' in o['text'] or 'stimulus minus' in o['text'] or 'not established' in o['text']):
        print([l for l in o['text'].splitlines() if 'luminance 8' in l or 'not established' in l])
" ; python tools/entry.py handover entries/001357-namima-2025 2>&1 | tail -3; ls executed/001357-namima-2025/handover; git status --short
```

```
['Shape files with luminance 8 presentations: 73 of 74']
["Files where it is not established: [{'kind': 'TX', 'date': '20200715', 'units': 25, 'true': 0.04, 'shifted': 0.0}, {'kind': 'TX', 'date': '20200719', 'units': 20, 'true': 0.0, 'shifted': 0.0}, {'kind': 'TX', 'date': '20200729', 'units': 17, 'true': 0.118, 'shifted': 0.0}, {'kind': 'TX', 'date': '20200730', 'units': 31, 'true': 0.065, 'shifted': 0.0}, {'kind': 'TX', 'date': '20200804', 'units': 22, 'true': 0.045, 'shifted': 0.0}, {'kind': 'SL', 'date': '20210529', 'units': 1, 'true': 1.0, 'shifted': 0.0}, {'kind': 'SP', 'date': '20210529', 'units': 1, 'true': 1.0, 'shifted': 0.0}]"]
wrote executed/001357-namima-2025/handover
10.1523-jneurosci.1893-23.2024.yaml
reproduce_namima_2025.ipynb
v4clusters.py
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
?? attempts/001357-namima-2025-01.yaml
?? entries/001357-namima-2025/
?? questions/001357.yaml
?? scripts
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
s=s.replace("center, and shapes 0 to 14 without saying which shape each is; texture rotations are not stored.","center, and shapes 0 to 14 without saying which shape each is; texture rotations are not stored.\n# The clock check (stimulus tuning at the true onsets, none at shifted onsets) holds in 152 of 159\n# files; it is not established in five M1 texture files, where 0% to 12% of units are tuned, and\n# in the two single-unit files of 2021-05-29.")
open('cells.py','w').write(s)
r=open('record.py').read()
r=r.replace(''' {"kind": "methods_unavailable",''',''' {"kind": "other", "statement": "Spikes and presentations share a clock in 152 of 159 files (units are tuned to the stimuli at the photodiode onsets and not at onsets moved by -1.3 s). It could not be established in five M1 texture files (2020-07-15, 07-19, 07-29, 07-30, 08-04), where 0% to 12% of units are tuned at the true onsets, nor in the two single-unit files of 2021-05-29."},
 {"kind": "methods_unavailable",''')
open('record.py','w').write(r)
EOF
cd  && . $TMPDIR/dev/bin/activate && python $TMPDIR/record.py && python $TMPDIR/build_nb.py $TMPDIR/cells.py entries/001357-namima-2025/reproduce_namima_2025.ipynb && python tools/entry.py all entries/001357-namima-2025 2>&1 | tail -2 && python tools/entry.py handover entries/001357-namima-2025 | tail -1; date -u
```

```
0 error(s)
pass  reproduce_namima_2025.ipynb  (457 s)
wrote executed/001357-namima-2025/handover
Mon Nov  2 08:09:37 UTC 2026
```

**Agent**

All 27 claims have an outcome: 18 were tested on the data and 9 are blocked. The entry is written, `tools/entry.py all` passes (0 errors; the notebook runs in 457 s) and the handover package is built. Nothing is committed.

The dataset is pinned at version 0.261006.2007, its only published version; the paper cites no version. The notebook header records this.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-sessions-and-neurons | reproduced |
| ex-m2p6-cluster | partially reproduced (13 neurons with significant Isimilarity, expected 11; 17 missing, 12, 21 and 22 added) |
| ex-m2p6-pairs | partially reproduced (only the bright similarity of neurons 18 and 19 misses: −0.144, expected −0.25) |
| ex-m2p6-invariance | reproduced |
| ex-csd-sinks | blocked, data_missing (no LF signal in the files) |
| ex-m1p12-no-cluster | reproduced |
| ex-m1p12-strong-responses | reproduced (28 and 26, exactly the paper's numbers) |
| pop-significant-isimilarity | partially reproduced (always a minority, but 381–625 neurons, expected 344) |
| pop-intercept-slope-correlation | reproduced (r = −0.768) |
| pop-dark-bright-consistent | not reproduced (r = 0.48–0.52, expected 0.435; the consistency is stronger than reported) |
| pop-contrast-invariance | reproduced (0.632, reliability reading b) |
| pop-sparse-across-penetrations | reproduced |
| pop-asymptote-20-percent | reproduced |
| pop-mean-isimilarity-yield | reproduced |
| pop-recording-density | reproduced (r = 0.257) |
| pop-within-vs-across-sessions | partially reproduced (direction and p hold under every reading; no reading matches the means) |
| orientation-sf-isimilarity | blocked, data_missing (shape images not public) |
| orientation-auc-coarse-clusters | not reproduced (M2p6 and M1p5 are of neither kind, whichever stim_ID is taken as the spindle) |
| apc-peaks-sparse-clustering, apc-example-m2p51 | blocked, data_missing (the shapes' curvature descriptions are not public) |
| gyrus-penetrations-consistent | blocked, metadata_insufficient (no grid coordinates in the files) |
| texture-sparse-clusters | not reproduced |
| texture-original-reversed-consistent | not reproduced (r = 0.64–0.71, expected 0.464) |
| texture-asymptote-20-percent | not reproduced (26–52%, expected 20%) |
| position-optimal-consistent | reproduced (r = 0.325, 721 neurons; expected 723) |
| position-examples-invariant | not reproduced |
| simulation-random-with-domains | blocked, methods_underspecified |

No outcome rests on an assumption (`assumed` is never set).

## 2. The dataset, assumptions and questions

**What the dataset holds.** Only spike times of good units, with a `pen_ID` label on every file. The labels identify the example penetrations: the labelled sessions give the paper's neuron counts for M2p6 (24), M1p12 (42) and M2p28 (55). Session counts and responsive-neuron counts match the paper. The texture files' good units sum to exactly 1,345, the paper's 979 + 366.

**Findings recorded in the attempt:**
- **Missing:** the LF signal, the stimulus images, the RF-mapping data and the grid coordinates are not in the files.
- **Unlabelled codes:** shape `stim_ID` 0–14 and position codes 0–4 have no names. The data do not reveal which position is the center either: the largest population response falls on different positions in different files.
- **Mislabelled sessions:** the trial tables of all 34 position-test files name their session "…SL".
- **Undescribed conditions:** a third luminance level of 8 cd/m2 (the background) appears in 73 of 74 shape files, and the texture files hold the spectral-noise version.
- **Depth:** unit depth is the best channel in 20 µm steps, not the template center of mass the Methods describe.
- **Session mismatch:** 5 of the 34 M2 texture sessions are texture-only days, where the paper says shape and texture were both run in 34 sessions. There is also a 34th position-test file holding a single unit; the paper reports 33.
- **Clock check:** spikes and presentations share a clock in 152 of 159 files. It could not be established in five M1 texture files and the two single-unit files.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): does "confidence limit > 0.5" mean the width or the half-width of the bootstrap interval, and at what level? The two readings change the significant-Isimilarity counts by 10–60%. The texture counts point to the half-width reading.

**Question to a reader** (`questions/001357.yaml`): position-examples-invariant accepts a session only if its neuron count is within 10% of Figure 11's n. But the legend defines that n as neurons with quantified RF centers, not the neurons in the matrices. Under the rule as written, M2p9 is matched to the session labelled p12, where the claim fails. Under the dataset's p09 label, the M2p9 half of the claim holds. The claim's outcome is not reproduced either way, because M2p28 fails.

## 3. Where the protocol was unclear

1. **No partial rule in a criterion.** pop-significant-isimilarity's criterion defines only "reproduced". I recorded partially reproduced, because the minority the statement describes holds and the counts do not, and gave that reasoning in the notes.
2. **The clock check for this dataset.** A stimulus-against-blank rate contrast did not work: stimuli suppress some units, so it failed in many files. I used per-unit ANOVA over stimuli at true onsets against onsets shifted by −1.3 s, and named the files where the check fails.
3. **A misreading that cannot change the outcome.** The protocol says to ask a reader only when a misreading "could change the outcome". In the Figure 11 case it changes half of the claim but not the outcome; I asked anyway and said so in the question.
4. **Bootstrap bias.** The bootstrap of a noise-corrected estimator sits below the point estimate, which the paper does not mention. I used only the interval's width and recorded this as a deviation.
5. **Outside data.** No pinned public copy of the Pasupathy and Connor (2001) shapes turned up; I searched the shape lab's publication pages, Pospisil et al. 2018, github.com/deanpospisil/er_est and the SparseShape OSF project. Those claims are blocked as data_missing, as the protocol requires for an outside input that is not public.

## 4. Runtime and failures

The run took about 1 h 20 min (06:52 to 08:10 UTC); the notebook runs in about 8 minutes, half of it streaming the files. Nothing failed.

Untracked dotfiles (`.bashrc`, `.profile`, `.idea`, `scripts` and others) appeared in the repository root; I did not create them and left them alone. Exclude them when committing.

Sources (web search for the shape set):
- [Pospisil et al. 2018, eLife](https://elifesciences.org/articles/38242)
- [SparseShape, J Neurosci 2023](https://www.jneurosci.org/content/43/22/4129)
- [Pasupathy & Connor 2001 PDF](https://depts.washington.edu/shapelab/publications/ShapeRepV4JNeurophys.pdf)

## End of run

64 turns, 74 minutes, $6.46 at API prices, result: success.
