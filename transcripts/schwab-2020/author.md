# 000947 · author · run 39099561342

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; echo ======; cat README.md; echo =====; cat docs/design.md; ls; ls entries claims attempts tools
```

```
<persisted-output>
Output too large (46.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f29b5c8b-1452-41e7-ae05-b8a8e260f95f/tool-results/blj76tf53.txt

Preview (first 2KB):
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
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
date +%s > $TMPDIR/start; find entries/001453-fouke-2025 claims/001453 -type f | head -50; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (35KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f29b5c8b-1452-41e7-ae05-b8a8e260f95f/tool-results/b4vghy1ka.txt

Preview (first 2KB):
entries/001453-fouke-2025/requirements.in
entries/001453-fouke-2025/requirements.lock.txt
entries/001453-fouke-2025/reproduce_fouke_2025.ipynb
entries/001453-fouke-2025/README.md
entries/001453-fouke-2025/omr.py
entries/001453-fouke-2025/entry.yaml
claims/001453/10.1016-j.cub.2025.04.027.yaml
schema_version: 1
id: 001453-fouke-2025-01
dandiset: "001453"
dandiset_version: 0.250518.1950
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: 001453-fouke-2025
provenance:
  kind: agent
[... 28 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f29b5c8b-1452-41e7-ae05-b8a8e260f95f/tool-results/blj76tf53.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-7`. Record this version in the attempt's provenance.
4	
5	This is what an agent, or a person, does to attempt a target and deposit the
6	result. It is written from the eight pilot attempts
7	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
8	
9	There are two roles. The **author** makes the attempt. The **verifier** checks
10	it and must not be the author: for agents, a separate run with a separate
11	context that has not seen the author's reasoning.
12	
13	Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
14	workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
15	`verifier-2`, `author-revise-2`, and, when the last of these proposes changes
16	of outcome, `verifier-3` and `author-revise-3`. Each run's transcript and final report are
17	kept in [`transcripts/<dandiset>/`](../transcripts).
18	
19	## Author
20	
[... 903 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f29b5c8b-1452-41e7-ae05-b8a8e260f95f/tool-results/b4vghy1ka.txt"
}
```

```
1	entries/001453-fouke-2025/requirements.in
2	entries/001453-fouke-2025/requirements.lock.txt
3	entries/001453-fouke-2025/reproduce_fouke_2025.ipynb
4	entries/001453-fouke-2025/README.md
5	entries/001453-fouke-2025/omr.py
6	entries/001453-fouke-2025/entry.yaml
7	claims/001453/10.1016-j.cub.2025.04.027.yaml
8	schema_version: 1
9	id: 001453-fouke-2025-01
10	dandiset: "001453"
11	dandiset_version: 0.250518.1950
12	paper: doi:10.1016/j.cub.2025.04.027
13	date: 2026-10-14
14	entry: 001453-fouke-2025
15	provenance:
16	  kind: agent
17	  accountable:
18	    name: CatalystNeuro
19	  agent:
20	    harness: Claude Code (GitHub Actions)
[... 602 more lines not kept]
```

**Agent**

Now the entry files.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -80 omr.py; cat ../../claims/001453/*.yaml | head -120
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
[... 243 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import nbformat
nb=nbformat.read('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb',4)
for i,c in enumerate(nb.cells[:6]+nb.cells[-3:]):
    print('---',c.cell_type,c.metadata.get('tags'));print(c.source[:1500])
print(len(nb.cells))
for c in nb.cells: print(c.cell_type, c.metadata.get('tags'), c.source[:60].replace(chr(10),' '))
"
```

```
--- markdown None
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
[... 188 more lines not kept]
```

**Agent**

Now look at the tool's checks and schemas.

**Agent calls Bash**

```bash
ls schemas; wc -l tools/entry.py; grep -n "def \|fail\|error(" tools/entry.py | head -120
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
396 tools/entry.py
28:that takes longer than --max-minutes fails, even if it ran without error.
68:    def __init__(self):
71:    def error(self, where, message: str) -> None:
75:def schema(name: str) -> Draft202012Validator:
79:def load(report: Report, path: Path):
84:        report.error(path.relative_to(ROOT), f"not valid YAML: {e}")
88:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
94:        report.error(path.relative_to(ROOT), f"{where}: {err.message}")
98:def _plain(value):
109:def code_of(notebook_path: Path) -> str:
116:def check(entry_dir: Path) -> Report:
123:        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")
128:        report.error(rel / name, "notebook is not listed in entry.yaml")
130:        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
134:            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")
138:        report.error(rel, "no requirements.in")
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,70p tools/entry.py; sed -n 180,360p tools/entry.py; cat schemas/claims.schema.json
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
[... 371 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat schemas/attempt.schema.json | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1))" | head -250
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
[... 230 more lines not kept]
```

**Agent**

Now get the paper (PLOS Biology, open access) and dandiset metadata.

**Agent calls Bash**

```bash
mkdir -p paper; curl -sL "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3000829&type=manuscript" -o paper/paper.xml; ls -la paper; head -c 600 paper/paper.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python - <<'EOF'
import re
x=open('paper/paper.xml').read()
x=re.sub(r'<mml:math.*?</mml:math>','[math]',x,flags=re.S)
x=re.sub(r'</(p|title|caption|sec|label)>','\n',x)
t=re.sub(r'<[^>]+>','',x)
t=re.sub(r'\n\s*\n+','\n\n',t)
open('paper/paper.txt','w').write(t)
print(len(t))
EOF
wc -l paper/paper.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/paper.txt",
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/paper.txt",
 "offset": 400,
 "limit": 320
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/paper.txt",
 "offset": 400,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^Materials and methods\|^Supporting information\|^References\|^Data analysis\|^Detection\|^Spike\|^Cross\|^Noise\|^Burst\|^Animals\|^Behav" paper/paper.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/paper.txt",
 "offset": 634,
 "limit": 290
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper is open access (PLOS Biology); full text saved under `paper/`. Now the dandiset metadata.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000947/ | python -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/000947/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000947/versions/0.240510.2211/ | python -m json.tool > $TMPDIR/meta.json; python - <<EOF
import json
m=json.load(open("$TMPDIR/meta.json"))
for k in ['name','description','keywords','relatedResource','assetsSummary','contributor','citation','wasGeneratedBy','protocol','ethicsApproval','about']:
    print('==',k); print(json.dumps(m.get(k),indent=1)[:3000])
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import requests, json
url="https://api.dandiarchive.org/api/dandisets/000947/versions/0.240510.2211/assets/?page_size=1000"
r=requests.get(url).json()
assets=r['results']; print(r['count'], len(assets))
json.dump(assets,open('assets.json','w'))
for a in assets[:30]: print(a['path'], round(a['size']/1e6,1))
import collections
print(collections.Counter(a['path'].split('/')[0] for a in assets))
print(collections.Counter(a['path'].split('_')[-1] for a in assets))
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
cd $TMPDIR && uv venv -q --python 3.13 venv && uv pip install -q --python venv/bin/python dandi pynwb h5py remfile numpy scipy pandas matplotlib requests 2>&1 | tail -3; venv/bin/python -c "import pynwb, dandi; print(pynwb.__version__, dandi.__version__)"
```

```
4.2.0 0.81.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import requests, json, collections
url="https://api.dandiarchive.org/api/dandisets/000947/versions/0.240510.2211/assets/?page_size=1000"
r=requests.get(url).json()
assets=r['results']; print(r['count'], len(assets))
json.dump(assets,open('assets.json','w'))
for a in assets[:15]: print(a['path'], round(a['size']/1e6,1))
print(collections.Counter(a['path'].split('/')[0] for a in assets))
sizes=sorted(a['size']/1e9 for a in assets); print('size GB min/med/max', sizes[0], sizes[len(sizes)//2], sizes[-1])
EOF
```

```
378 378
sub-Isis/sub-Isis_ses-post-MPTP-I-181022-2_ecephys.nwb 1388.3
sub-Isis/sub-Isis_ses-post-MPTP-I-181023-1_ecephys.nwb 2974.6
sub-Isis/sub-Isis_ses-post-MPTP-I-181024-1_ecephys.nwb 1387.1
sub-Isis/sub-Isis_ses-post-MPTP-I-181018-1_ecephys.nwb 3499.5
sub-Isis/sub-Isis_ses-post-MPTP-I-181026-1_ecephys.nwb 737.4
sub-Isis/sub-Isis_ses-post-MPTP-I-190122-3_ecephys.nwb 1355.7
sub-Isis/sub-Isis_ses-post-MPTP-I-190122-6_ecephys.nwb 1397.4
sub-Isis/sub-Isis_ses-post-MPTP-I-190117-11_ecephys.nwb 4229.9
sub-Isis/sub-Isis_ses-post-MPTP-I-181016-1_ecephys.nwb 7445.0
sub-Isis/sub-Isis_ses-post-MPTP-I-190124-3_ecephys.nwb 3077.9
sub-Isis/sub-Isis_ses-post-MPTP-I-190125-6_ecephys.nwb 1986.0
sub-Isis/sub-Isis_ses-post-MPTP-I-190124-6_ecephys.nwb 2426.8
sub-Isis/sub-Isis_ses-post-MPTP-I-190125-3_ecephys.nwb 2162.1
sub-Isis/sub-Isis_ses-post-MPTP-I-190129-3_ecephys.nwb 1287.3
sub-Isis/sub-Isis_ses-post-MPTP-I-181019-2_ecephys.nwb 11038.4
Counter({'sub-Gaia': 220, 'sub-Isis': 158})
size GB min/med/max 0.041450607 1.986006209 14.235593622
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import json, collections, re
assets=json.load(open('assets.json'))
rows=[]
for a in assets:
    p=a['path']; m=re.match(r'sub-(\w+)/sub-\w+_ses-(pre|post)-MPTP-(.*)_ecephys\.nwb',p)
    rows.append((m.group(1),m.group(2),m.group(3),a['size']))
print(collections.Counter((r[0],r[1]) for r in rows))
for s in ['Gaia','Isis']:
  pre=sorted(r[2] for r in rows if r[0]==s and r[1]=='pre'); print(s,len(pre),pre[:10],pre[-5:])
other=[a['path'] for a in assets if not re.match(r'sub-(\w+)/sub-\w+_ses-(pre|post)-MPTP-(.*)_ecephys\.nwb',a['path'])]
print(other)
pre=[r for r in rows if r[1]=='pre']; print('pre total GB', sum(r[3] for r in pre)/1e9)
EOF
```

```
Counter({('Isis', 'pre'): 135, ('Gaia', 'pre'): 119, ('Gaia', 'post'): 101, ('Isis', 'post'): 23})
Gaia 119 ['G-140511-1', 'G-140511-2', 'G-140511-3', 'G-140511-4', 'G-140511-5', 'G-140511-6', 'G-140511-7', 'G-140511-8', 'G-140511-9', 'G-140512-1'] ['G-140902-4', 'G-140903-1', 'G-140909-1', 'G-140909-2', 'G-141111-1']
Isis 135 ['I-160615-1', 'I-160615-2', 'I-160616-1', 'I-160616-2', 'I-160616-4', 'I-160617-1', 'I-160617-2', 'I-160617-3', 'I-160620-1', 'I-160620-2'] ['I-170620-2', 'I-170620-3', 'I-170623-1', 'I-170623-2', 'I-170623-5']
[]
pre total GB 456.007923621
Shell cwd was reset to
```

**Agent**

The pinned version (0.240510.2211, the only published one) holds 378 files from two monkeys: 254 pre-MPTP sessions (the paper's condition) and 124 post-MPTP. Opening one file next.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > open1.py <<'EOF'
import json, sys, h5py, remfile, pynwb
from dandi.dandiapi import DandiAPIClient
path=sys.argv[1]
with DandiAPIClient() as c:
    a=c.get_dandiset('000947','0.240510.2211').get_asset_by_path(path)
    url=a.get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print(nwb)
print('desc',nwb.session_description); print('start',nwb.session_start_time); print(nwb.subject)
print('acq',{k:(type(v).__name__) for k,v in nwb.acquisition.items()})
for k,v in nwb.acquisition.items():
    try: print(k, v.data.shape, v.rate, v.conversion, v.unit, v.starting_time)
    except Exception as e: print(k,e)
print('proc',{k:list(v.data_interfaces) for k,v in nwb.processing.items()})
for k,v in nwb.processing.items():
    for kk,vv in v.data_interfaces.items():
        print('---',k,kk,type(vv).__name__, vv)
print('intervals',list(nwb.intervals) if nwb.intervals else None)
if nwb.trials is not None:
    df=nwb.trials.to_dataframe(); print(df.columns.tolist()); print(df.head(5).T); print(len(df))
    for c in df.columns: print(c, nwb.trials[c].description)
u=nwb.units
if u is not None:
    print('units cols', u.colnames)
    for c in u.colnames: print(c, '|', u[c].description)
    ud=u.to_dataframe(index=True)
    print(ud.drop(columns=[c for c in ud.columns if c in('spike_times','waveform_mean','waveform_sd','waveforms')]).to_string()[:6000])
e=nwb.electrodes
if e is not None:
    ed=e.to_dataframe(); print(ed.columns.tolist()); print(ed.head(20).to_string())
    for c in e.colnames: print(c,'|',e[c].description)
print('egroups',{k:(v.location,v.description) for k,v in nwb.electrode_groups.items()})
print('devices',list(nwb.devices))
print('epochs', nwb.epochs)
print('stim', list(nwb.stimulus))
print('lab',nwb.lab, nwb.institution, nwb.experimenter, nwb.experiment_description, nwb.notes, nwb.keywords[:] if nwb.keywords is not None else None)
EOF
venv/bin/python open1.py sub-Isis/sub-Isis_ses-pre-MPTP-I-160615-1_ecephys.nwb 2>&1 | head -300
```

```
root pynwb.file.NWBFile at 0x139689396777856
Fields:
  acquisition: {
    ElectricalSeries <class 'pynwb.ecephys.ElectricalSeries'>
  }
  devices: {
    DeviceEcephys <class 'pynwb.device.Device'>
  }
  electrode_groups: {
    Group GPi <class 'pynwb.ecephys.ElectrodeGroup'>,
    Group VL <class 'pynwb.ecephys.ElectrodeGroup'>
  }
  electrodes: electrodes <class 'pynwb.ecephys.ElectrodesTable'>
  experiment_description: This dataset contains recordings of single-unit activity from from multiple cortical areas, 
including globus pallidus-internus (GPi), ventrolateral nucleus of the thalamus (VLa and VLp) and 
the arm-related regions of primary motor cortex, including sulcus (M1-S) and gyrus (M1-G) subregions in  monkeys performing a choice
reaction time reaching task. Small numbers of recordings were also obtained from supplementary motor area (SMA),
external globus pallidus (GPe), the thalamic reticular nucleus (RTN), striatum (STR) and the region between RTN
and VL thalamus (R-V).
The neuronal activity was recorded using 16-contact linear probes (0.5–1.0 MΩ, V-probe, Plexon) or glass-insulated
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > h5walk.py <<'EOF'
import sys, h5py, remfile
from dandi.dandiapi import DandiAPIClient
path=sys.argv[1]
with DandiAPIClient() as c:
    url=c.get_dandiset('000947','0.240510.2211').get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        v=''
        if obj.size<12: v=obj[()]
        print(name, obj.shape, obj.dtype, dict(obj.attrs).get('unit',''), v)
    else:
        a={k:v for k,v in obj.attrs.items() if k not in('namespace','object_id')}
        print(name+'/', a)
f.visititems(show)
EOF
venv/bin/python h5walk.py sub-Isis/sub-Isis_ses-pre-MPTP-I-160615-1_ecephys.nwb 2>&1 | grep -v "^acquisition/ElectricalSeries/\|^specifications" | head -150
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object  [b'2024-04-26T20:05:15.086711+02:00']
general/ {}
general/MPTPMetaData/ {'MPTP_status': 'pre_MPTP', 'neurodata_type': 'TurnerLabMetaData'}
general/devices/ {}
general/devices/DeviceEcephys/ {'description': 'TDT recording', 'manufacturer': 'Tucker-Davis Technologies (TDT)', 'neurodata_type': 'Device'}
general/experiment_description () object  b'This dataset contains recordings of single-unit activity from from multiple cortical areas, \nincluding globus pallidus-internus (GPi), ventrolateral nucleus of the thalamus (VLa and VLp) and \nthe arm-related regions of primary motor cortex, including sulcus (M1-S) and gyrus (M1-G) subregions in  monkeys performing a choice\nreaction time reaching task. Small numbers of recordings were also obtained from supplementary motor area (SMA),\nexternal globus pallidus (GPe), the thalamic reticular nucleus (RTN), striatum (STR) and the region between RTN\nand VL thalamus (R-V).\nThe neuronal activity was recorded using 16-contact linear probes (0.5\xe2\x80\x931.0 M\xce\xa9, V-probe, Plexon) or glass-insulated\ntungsten microelectrodes (0.5\xe2\x80\x931.5 M\xce\xa9, Alpha Omega). The neuronal data were amplified (4\xc3\x97, 2 Hz\xe2\x80\x937.5 kHz) and\ndigitized at 24.414 kHz (approx., 16-bit resolution; Tucker Davis Technologies).\nThe neuronal data were high-pass filtered (Fpass: 200 Hz, Matlab FIRPM) and thresholded, and candidate action\npotentials were sorted into clusters in principal components space (Off-line Sorter, Plexon).\n'
general/experimenter (2,) object  [b'Kase, Daisuke' b'Zimnik, Andrew']
general/extracellular_ephys/ {}
general/extracellular_ephys/Group GPi/ {'description': 'Group new V-probe electrodes.', 'location': 'GPi', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/Group VL/ {'description': 'Group AlphaOmega electrodes.', 'location': 'VLa', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'colnames': array([
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL "https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.0cfxpnvxm" | python -m json.tool | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL "https://datadryad.org/api/v2/versions/79104" | python -c "import json,sys; d=json.load(sys.stdin); print({k:d[k] for k in d if k not in ('authors','_links')})" | head -50; curl -sL "https://datadryad.org/api/v2/versions/79104/files" | python -c "
import json,sys; d=json.load(sys.stdin)
for f in d['_embedded']['stash:files']: print(f['path'], f['size'], f['_links'].get('stash:download',{}).get('href'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for p in 1 2 3; do curl -sL "https://datadryad.org/api/v2/versions/79104/files?page=$p" | python -c "
import json,sys; d=json.load(sys.stdin)
for f in d.get('_embedded',{}).get('stash:files',[]): print(f['path'], f['size'], f['_links'].get('stash:download',{}).get('href'))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p paper/dryad; cd paper/dryad; for pair in absmax.m:403501 Fig2_3_S8_S9.m:403513 Fig4_S10to13.m:403514 Fig5_S14.m:403515 FigS2.m:403518 FigS6_S8.m:403521 PeriEventChange_SDF_pctchng.m:403532 find_local_nmax.m:403525 IsoutlierBCS.m:403531 Gaia_MvtSum.mat:403528 Isis_MvtSum.mat:403530 Increases.mat:403529 Decreases.mat:403512 Data_S13.mat:403508 Data_S11.mat:403506; do n=${pair%%:*}; id=${pair##*:}; curl -sL -o $n "https://datadryad.org/api/v2/files/$id/download"; done; ls -la; file *; head -c 300 Fig2_3_S8_S9.m
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper/dryad; for u in "https://datadryad.org/stash/downloads/file_stream/403513" "https://datadryad.org/downloads/file_stream/403513" "https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.0cfxpnvxm/download"; do curl -sL -o t -w "%{http_code} %{content_type}\n" -A "Mozilla/5.0" "$u"; head -c 200 t; echo; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  rm -f paper/dryad/*; curl -s "https://zenodo.org/api/records?q=%22counter%20to%20gating%20and%20rebound%22&size=10" | python -c "
import json,sys; d=json.load(sys.stdin)
for h in d['hits']['hits']: print(h['id'], h['metadata']['title'], h.get('doi'), [f['key'] for f in h.get('files',[])][:40])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://zenodo.org/api/records?q=%22counter%20to%20gating%20and%20rebound%22&size=10" -o paper/zenodo_search.json; python3 -c "
import json; d=json.load(open('paper/zenodo_search.json'))
for h in d['hits']['hits']: print(h['id'], h['metadata']['title'], h.get('doi'), [f['key'] for f in h.get('files',[])][:40])"
```

Result: the fetched text is not kept.

**Agent**

Zenodo mirrors the Dryad deposit (record 4000719, same DOI). Downloading code and small files from there.

**Agent calls Bash**

```bash
cd paper/dryad; for n in absmax.m Fig2_3_S8_S9.m Fig4_S10to13.m Fig5_S14.m FigS2.m FigS6_S8.m FigS7.m FigS5.m FigS4.m PeriEventChange_SDF_pctchng.m find_local_nmax.m IsoutlierBCS.m Gaia_MvtSum.mat Isis_MvtSum.mat Increases.mat Decreases.mat Data_S13.mat Data_S11.mat; do curl -sL -o $n "https://zenodo.org/records/4000719/files/$n?download=1"; done; ls -la; file * | head -30; python3 -c "
import json; d=json.load(open('../zenodo_search.json'))['hits']['hits'][0]
print(d['created'], d['metadata'].get('version'), d['metadata'].get('publication_date'))
for f in d['files']: print(f['key'], f['size'], f['checksum'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper/dryad; tr -d '\r' < PeriEventChange_SDF_pctchng.m; tr -d '\r' < Fig2_3_S8_S9.m | head -250
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper/dryad; tr -d '\r' < Fig2_3_S8_S9.m | sed -n 250,900p | grep -v "^\s*$" | grep -iv "set(gca\|xlabel\|ylabel\|print(\|meta_file\|axis\|xlim\|ylim\|title(\|legend\|subplot\|hold \|figure\|line(" | head -330
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper/dryad; for n in Gaia_Analy.mat Isis_Analy.mat; do curl -sL -o $n "https://zenodo.org/records/4000719/files/$n?download=1"; done; md5sum Gaia_Analy.mat Isis_Analy.mat; file Gaia_Analy.mat
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper/dryad; $TMPDIR/venv/bin/python - <<'EOF'
import scipy.io as sio, numpy as np
m=sio.loadmat('Gaia_Analy.mat',squeeze_me=True,struct_as_record=False)
for k,v in m.items():
    if k.startswith('__'): continue
    print('==',k,type(v))
    if hasattr(v,'_fieldnames'):
        for f in v._fieldnames:
            x=getattr(v,f); print('  ',f, type(x).__name__, getattr(x,'shape',None), (x if np.size(x)<6 else ''))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper/dryad; $TMPDIR/venv/bin/python - <<'EOF'
import scipy.io as sio, numpy as np, collections
for mk in ['Gaia','Isis']:
    m=sio.loadmat(f'{mk}_Analy.mat',squeeze_me=True,struct_as_record=False)
    S=m['RespSDFIncr']; I=m['RespISIIncr']
    print('=====',mk, len(S.fname))
    print(collections.Counter(S.unit_type))
    for i in range(4): print(S.fname[i], S.Uchan[i], S.Usort[i] if i<len(S.Usort) else '', S.unit_type[i], S.RecInds[i], S.on_ind[i], I.on_ind[i], S.cntl_mean[i], S.sig_thr[i], np.shape(S.evt_spkt[i,0]))
    print('rec example', S.evt_spkt[0,0][:2] if np.size(S.evt_spkt[0,0]) else None)
    print('slope', S.CntlSlope[0,0]._fieldnames if hasattr(S.CntlSlope[0,0],'_fieldnames') else S.CntlSlope[0,0])
    print('rt', S.rt[0])
    fn=[str(f) for f in S.fname]; print('distinct files', len(set(fn)), sorted(set(fn))[:5])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > scan.py <<'EOF'
import json, h5py, remfile, numpy as np, pandas as pd, time
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset('000947','0.240510.2211')
    assets=[(a.path, a.get_content_url(follow_redirects=1, strip_query=True)) for a in ds.get_assets()]
def s(x): return x.decode() if isinstance(x,bytes) else x
def scan(pu):
    p,u=pu
    for k in range(3):
        try:
            f=h5py.File(remfile.File(u),'r'); break
        except Exception as e: err=e; time.sleep(2)
    else: return {'path':p,'error':str(err)}
    r={'path':p,'session_id':s(f['general/session_id'][()]),'start':s(f['session_start_time'][()]),
       'mptp':s(f['general/MPTPMetaData'].attrs.get('MPTP_status','')),'subject':s(f['general/subject/subject_id'][()])}
    tr=f['intervals/trials']; r['n_trials']=len(tr['id']); r['trial_cols']=list(tr.attrs['colnames'])
    r['targets']=dict(pd.Series([s(x) for x in tr['target'][:]]).value_counts())
    r['groups']={g:dict(f['general/extracellular_ephys'][g].attrs) .get('location') for g in f['general/extracellular_ephys'] if g!='electrodes'}
    r['elec_loc']=dict(pd.Series([s(x) for x in f['general/extracellular_ephys/electrodes/location'][:]]).value_counts())
    r['acq']={k:f['acquisition'][k]['data'].shape for k in f['acquisition']}
    r['rel_pub']=[s(x) for x in f['general/related_publications'][:]] if 'related_publications' in f['general'] else []
    if 'units' in f:
        U=f['units']; r['u_cols']=list(U.attrs['colnames'])
        idx=U['spike_times_index'][:]; st=U['spike_times']
        r['units']=[]
        lo=0
        for i in range(len(idx)):
            row={c:s(U[c][i]) for c in U.attrs['colnames'] if c!='spike_times'}
            row['n_spikes']=int(idx[i]-lo); lo=idx[i]
            r['units'].append(row)
        r['dur']=float(np.nanmax(st[:])) if len(st) else None
    else: r['units']=[]
    P=f['processing/ecephys/units'] if 'units' in f['processing/ecephys'] else None
    if P is not None:
        r['p_cols']=list(P.attrs['colnames']); r['p_n']=len(P['id'])
        r['p_loc']=dict(pd.Series([s(x) for x in P['location'][:]]).value_counts())
        r['p_names']=[s(x) for x in P['unit_name'][:]]
    return r
pre=[a for a in assets]
t=time.time()
with ThreadPoolExecutor(16) as ex: res=list(ex.map(scan, pre))
print(time.time()-t)
json.dump(res,open('scan.json','w'),default=str)
EOF
venv/bin/python scan.py 2>&1 | tail -5
```

```
oid = h5o.open(self.id, self._e(name), lapl=lapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5o.pyx", line 255, in h5py.h5o.open
KeyError: 'Unable to synchronously open object (component not found)'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -i 's/^def scan(pu):/def scan(pu):\n    try: return scan0(pu)\n    except Exception as e:\n        import traceback; return {"path":pu[0],"error":traceback.format_exc()[-400:]}\ndef scan0(pu):/' scan.py; venv/bin/python scan.py 2>&1 | tail -3; venv/bin/python -c "
import json; r=json.load(open('scan.json')); e=[x for x in r if 'error' in x]; print(len(r), len(e)); [print(x['path'], x['error'][-300:]) for x in e[:5]]"
```

```
288.33004903793335
378 1
sub-Isis/sub-Isis_ses-pre-MPTP-I-160616-4_ecephys.nwb (self.id, self._e(name), lapl=lapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5o.pyx", line 255, in h5py.h5o.open
KeyError: 'Unable to synchronously open object (component not found)'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python h5walk.py sub-Isis/sub-Isis_ses-pre-MPTP-I-160616-4_ecephys.nwb 2>&1 | grep -v "^acquisition/ElectricalSeries/\|^specifications\|electrodes/" | grep -v "^general/[a-z_]* (" | head -40
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object  [b'2024-04-26T17:06:54.887288+02:00']
general/ {}
general/MPTPMetaData/ {'MPTP_status': 'pre_MPTP', 'neurodata_type': 'TurnerLabMetaData'}
general/devices/ {}
general/devices/DeviceEcephys/ {'description': 'TDT recording', 'manufacturer': 'Tucker-Davis Technologies (TDT)', 'neurodata_type': 'Device'}
general/extracellular_ephys/ {}
general/extracellular_ephys/Group GPi/ {'description': 'Group new V-probe electrodes.', 'location': 'GPi', 'neurodata_type': 'ElectrodeGroup'}
       'offset_to_uV', 'channel_ids', 'electrode_type', 'chamber_type',
       'chamber_x', 'chamber_y', 'chamber_z', 'acx_x', 'acx_y', 'acx_z'],
      dtype=object), 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
 b'globus pallidus-internus' b'ventrolateral anterior nucleus'
 b'primary motor cortex' b'reaching task' b'macaque']
general/subject/ {'neurodata_type': 'Subject'}
general/subject/date_of_birth () object  b'2005-06-14T00:00:00-07:00'
general/subject/description () object  b'USDA registration number RQ7513'
general/subject/sex () object  b'F'
general/subject/species () object  b'Macaca mulatta'
general/subject/subject_id () object  b'Isis'
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import json, pandas as pd, collections
r=[x for x in json.load(open('scan.json')) if 'error' not in x]
print(collections.Counter((x['subject'],x['mptp']) for x in r))
pre=[x for x in r if x['mptp']=='pre_MPTP']
print('trial cols', collections.Counter(tuple(x['trial_cols']) for x in pre))
print('u cols', collections.Counter(tuple(x.get('u_cols',[])) for x in pre))
print('groups', collections.Counter(json.dumps(x['groups'],sort_keys=True) for x in pre).most_common(10))
print('rel pub', collections.Counter(tuple(x['rel_pub']) for x in r))
U=pd.DataFrame([dict(u, session=x['session_id'], subject=x['subject'], n_trials=x['n_trials']) for x in pre for u in x['units']])
print(len(U)); print(U.groupby(['subject','location']).size())
print(U.groupby(['location','unit_quality_post_sorting']).size())
print(U.sort_label.value_counts())
print('sessions with curated units', U.session.nunique(), 'of', len(pre))
print('trials range', min(x['n_trials'] for x in pre), max(x['n_trials'] for x in pre))
print('no curated units:', [x['session_id'] for x in pre if not x['units']][:30], sum(1 for x in pre if not x['units']))
print('p_loc', collections.Counter(k for x in pre for k in x.get('p_loc',{})))
print('acq', collections.Counter(len(x['acq']) for x in pre))
# start date vs session id date
import re
mm=[]
for x in pre:
    d=re.search(r'-(\d{6})-',x['session_id']).group(1); st=x['start'][:10].replace('-','')[2:]
    if d!=st: mm.append((x['session_id'],x['start'][:10]))
print('date mismatch', len(mm), mm[:8])
EOF
```

```
Counter({('Isis', 'pre_MPTP'): 134, ('Gaia', 'pre_MPTP'): 119, ('Gaia', 'post_MPTP'): 101, ('Isis', 'post_MPTP'): 23})
trial cols Counter({('start_time', 'stop_time', 'error_onset_time', 'reward_start_time', 'reward_stop_time', 'movement_start_time', 'movement_stop_time', 'return_start_time', 'return_stop_time', 'cue_onset_time', 'target'): 84, ('start_time', 'stop_time', 'reward_start_time', 'reward_stop_time', 'movement_start_time', 'movement_stop_time', 'return_start_time', 'return_stop_time', 'cue_onset_time', 'target'): 82, ('start_time', 'stop_time', 'reward_start_time', 'reward_stop_time', 'movement_start_time', 'cue_onset_time', 'target'): 44, ('start_time', 'stop_time', 'error_onset_time', 'reward_start_time', 'reward_stop_time', 'movement_start_time', 'cue_onset_time', 'target'): 43})
u cols Counter({('spike_times', 'unit_name', 'location', 'channel_ids', 'sort_label', 'unit_quality_post_sorting'): 125, ('spike_times', 'unit_name', 'location', 'channel_ids', 'sort_label'): 73, (): 21, ('spike_times', 'unit_name', 'unit_quality_post_sorting', 'location', 'channel_ids', 'sort_label'): 13, ('spike_times', 'unit_name', 'location', 'sort_label', 'channel_ids', 'unit_quality_post_sorting'): 7, ('spike_times', 'unit_name', 'channel_ids', 'location', 'sort_label'): 6, ('spike_times', 'unit_name', 'channel_ids', 'unit_quality_post_sorting', 'sort_label', 'location'): 5, ('spike_times', 'unit_name', 'channel_ids', 'location', 'unit_quality_post_sorting', 'sort_label'): 3})
groups [('{"Group GPi": "GPi", "Group VL": "VLa"}', 79), ('{"Group GPi": "GPi", "Group VL": "VLp"}', 64), ('{"Group VL": "VLa"}', 18), ('{"Group M1-G": "M1-G", "Group M1-S": "M1-S"}', 18), ('{"Group M1-S": "M1-S", "Group SMA": "SMA"}', 12), ('{"Group GPi": "GPi", "Group VL": "Thalamus"}', 10), ('{"Group VL": "VLp"}', 7), ('{"Group SMA": "SMA"}', 5), ('{"Group M1-G": "M1-G", "Group M1-S": "M1-S", "Group SMA": "SMA"}', 5), ('{"Group GPi": "GP", "Group VL": "VL"}', 5)]
rel pub Counter({('https://doi.
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import json, pandas as pd, collections, re, scipy.io as sio, numpy as np
from datetime import datetime
r=[x for x in json.load(open('scan.json')) if 'error' not in x and x['mptp']=='pre_MPTP']
U=pd.DataFrame([dict(u, session=x['session_id'], subject=x['subject']) for x in r for u in x['units']])
print(U[U.sort_label.isin(['1.0','2.0'])].groupby('subject').session.nunique(), U[U.sort_label.isin(['a','b'])].groupby('subject').session.nunique())
print(U[U.sort_label.isin(['1.0'])].head(5).to_string())
print(U[U.sort_label==''].head(5).to_string())
# date offsets
offs=collections.Counter()
for x in r:
    d=datetime.strptime(re.search(r'-(\d{6})-',x['session_id']).group(1),'%y%m%d'); st=datetime.fromisoformat(x['start'][:10])
    offs[(x['subject'],(st-d).days)]+=1
print(offs)
EOF
```

```
Series([], Name: session, dtype: int64) subject
Gaia    100
Isis     72
Name: session, dtype: int64
Empty DataFrame
Columns: [unit_name, location, channel_ids, sort_label, unit_quality_post_sorting, n_spikes, session, subject]
Index: []
   unit_name location  channel_ids sort_label unit_quality_post_sorting  n_spikes              session subject
26   sig001a                   NaN                                          63798  pre-MPTP-I-160620-3    Isis
43   sig001a                   NaN                                          47813  pre-MPTP-I-160621-1    Isis
44   sig001b                   NaN                                           9039  pre-MPTP-I-160621-1    Isis
51   sig002a                   NaN                                          47972  pre-MPTP-I-160621-3    Isis
93   sig007a                   NaN                                          35383  pre-MPTP-I-160622-1    Isis
Counter({('Isis', 2): 134, ('Gaia', 2): 119})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import json, pandas as pd, collections, re, scipy.io as sio, numpy as np
r=[x for x in json.load(open('scan.json')) if 'error' not in x and x['mptp']=='pre_MPTP']
U=pd.DataFrame([dict(u, session=x['session_id'], subject=x['subject']) for x in r for u in x['units']])
U['sl']=U.sort_label.map(lambda v: {1:'a',2:'b',3:'c',4:'d'}.get(v,v) if not isinstance(v,str) else v)
print(U.sort_label.map(type).value_counts())
U['key_file']=U.session.str.replace('pre-MPTP-','').str.replace('-','_')
U['ch']=pd.to_numeric(U.channel_ids,errors='coerce')
# unit_name channel number vs channel_ids
U['name_ch']=U.unit_name.str.extract(r'sig(\d+)')[0].astype(float)
print('name sort letter == sort_label:', (U.unit_name.str[-1]==U.sl).mean())
recs=[]
for mk in ['Gaia','Isis']:
    m=sio.loadmat(f'paper/dryad/{mk}_Analy.mat',squeeze_me=True,struct_as_record=False)
    S=m['RespSDFIncr']
    for i in range(len(S.fname)):
        nan=bool(np.isnan(S.evt_sdf[i,:,0]).any())
        recs.append(dict(monk=mk,i=i,fname=str(S.fname[i]),ch=float(S.Uchan[i]),sort=S.Usort[i],utype=str(S.unit_type[i]),nan=nan,ntr=[np.shape(S.evt_spkt[i,t])[0] if np.size(S.evt_spkt[i,t]) else 0 for t in range(2)]))
R=pd.DataFrame(recs); print(R.groupby(['monk','utype','nan']).size())
keep=R[(~R.nan)&(R.utype!='VLp')]; print('kept', keep.groupby(['monk','utype']).size())
# link
hits=[]
for _,x in R.iterrows():
    files=x.fname.split('/')
    m=[U[(U.key_file==f)&(U.ch==x.ch)&(U.sl==x.sort)] for f in files]
    hits.append(dict(nfiles=len(files), found=sum(len(k)==1 for k in m), loc=[list(k.location) for k in m]))
R=pd.concat([R,pd.DataFrame(hits)],axis=1)
R['all']=R.found==R.nfiles
print(R.groupby(['monk','utype'])[['all']].mean(), R.groupby(['monk','utype']).found.apply(lambda s:(s>0).mean()))
print(R[~R['all']].head(20).to_string())
print('multi-file records', (R.nfiles>1).sum(), R.nfiles.value_counts())
R.to_pickle('link.pkl'); U.to_pickle('U.pkl')
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import json, pandas as pd
r=[x for x in json.load(open('scan.json')) if 'error' not in x and x['mptp']=='pre_MPTP']
P={x['session_id'].replace('pre-MPTP-','').replace('-','_'):x.get('p_names',[]) for x in r}
R=pd.read_pickle('link.pkl'); U=pd.read_pickle('U.pkl')
K=R[(~R.nan)&(R.utype!='VLp')].copy()
def inproc(x):
    out=[]
    for f in x.fname.split('/'):
        names=P.get(f)
        if names is None: out.append('nofile'); continue
        out.append(any(n.startswith('sig') and int(n[3:6])==int(x.ch) and n[6:]==x.sort for n in names))
    return out
K['proc']=K.apply(inproc,axis=1)
print(K.groupby(['monk','utype'])['all'].agg(['sum','size']))
miss=K[~K['all']]
print(len(miss)); print(miss[['monk','fname','ch','sort','utype','found','nfiles','proc']].to_string())
# location agreement for found
def locs(x): return [l for k in x['loc'] for l in k]
K['dl']=K.apply(locs,axis=1)
import collections
print(collections.Counter((x.utype, tuple(sorted(set(x.dl)))) for _,x in K.iterrows()))
EOF
```

```
sum  size
monk utype           
Gaia GPi     95   105
     VLa     60    66
Isis GPi    104   104
     VLa    105   119
30
     monk                             fname    ch sort utype  found  nfiles                   proc
76   Gaia                        G_140524_3   3.0    a   GPi      0       1                [False]
82   Gaia                        G_140524_8   3.0    a   GPi      0       1                [False]
84   Gaia                        G_140525_1   2.0    a   VLa      0       1                [False]
164  Gaia             G_140731_1/G_140731_2  10.0    a   VLa      0       2         [False, False]
165  Gaia                        G_140731_2   1.0    a   GPi      0       1                [False]
166  Gaia                        G_140731_2  18.0    a   VLa      0       1                [False]
167  Gaia                        G_140813_1   2.0    a   VLa      0       1                [False]
168  Gaia                        G_140813_2   2.0    a   VLa      0       1                [False]
169  Gaia                        G_140813_2   3.0    a   VLa      0       1                [False]
170  Gaia                        G_140813_2   8.0    a   GPi      0       1                [False]
171  Gaia                        G_140813_3   6.0    a   GPi      0       1                [False]
172  Gaia                        G_140813_3   8.0    a   GPi      0       1                [False]
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import json, pandas as pd
r={x['session_id']:x for x in json.load(open('scan.json')) if 'error' not in x and x['mptp']=='pre_MPTP'}
for s in ['pre-MPTP-G-140813-2','pre-MPTP-G-140524-3','pre-MPTP-I-160621-1','pre-MPTP-I-160817-1']:
    x=r[s]; print(s, x['n_trials'], x['groups'], x.get('p_names'), x.get('p_loc'), [(u['unit_name'],u.get('channel_ids'),u.get('location'),u.get('sort_label')) for u in x['units']])
EOF
```

```
pre-MPTP-G-140813-2 197 {'Group GPi': 'GPi', 'Group VL': 'VLa'} ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'] {'GPi': '7', 'GPe': '5', 'VLa': '4'} []
pre-MPTP-G-140524-3 38 {'Group GPi': 'GPi', 'Group VL': 'VLa'} ['0', '1', '2', '3'] {'VLa': '2', 'GPi': '2'} [('sig001a', 1.0, 'VLa', 'a')]
pre-MPTP-I-160621-1 128 {'Group GPi': 'GPi', 'Group VL': 'VLa'} ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'] {'GPi': '15', 'VLa': '3'} [('sig001a', 17.0, 'GPi', 'a'), ('sig001b', 17.0, 'GPi', 'b'), ('sig001a', nan, '', ''), ('sig001b', nan, '', ''), ('sig001c', 17.0, 'GPi', 'c'), ('sig010a', 26.0, 'GPi', 'a'), ('sig012a', 28.0, 'GPi', 'a'), ('sig014a', 30.0, 'GPi', 'a')]
pre-MPTP-I-160817-1 129 {'Group GPi': 'GPi', 'Group VL': 'VLa'} ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'] {'GPi': '16', 'VLa': '8', 'RTN': '3', 'R-V': '2'} [('sig001a', 17.0, 'GPi', 'a'), ('sig002a', 18.0, 'GPi', 'a'), ('sig004a', 4.0, 'VLa', 'a'), ('sig001a', nan, '', ''), ('sig002a', nan, '', ''), ('sig003a', 19.0, 'GPi', 'a'), ('sig009a', 25.0, 'GPi', 'a'), ('sig009b', 25.0, 'GPi', 'b'), ('sig009c', 25.0, 'GPi', 'c'), ('sig011a', 27.0, 'GPi', 'a'), ('sig015a', 31.0, 'GPi', 'a')]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import json, pandas as pd
R=pd.read_pickle('link.pkl'); U=pd.read_pickle('U.pkl')
K=R[(~R.nan)&(R.utype!='VLp')]
pfiles=set(f for x in R.fname for f in x.split('/'))
U['in_paper_file']=U.key_file.isin(pfiles)
U['loc2']=U.location.fillna('').str.upper().map({'GPI':'GPi','VLA':'VLa'}).fillna(U.location.fillna(''))
print(U.groupby(['subject','loc2','in_paper_file']).size().unstack())
print('paper files',len(pfiles),'dandiset pre files', U.key_file.nunique())
sess=json.load(open('scan.json')); pre=[x for x in sess if 'error' not in x and x['mptp']=='pre_MPTP']
ids=set(x['session_id'].replace('pre-MPTP-','').replace('-','_') for x in pre)
print('paper files not in dandiset', sorted(pfiles-ids))
notp=sorted(ids-pfiles); print(len(notp), notp[:60])
EOF
```

```
in_paper_file     False  True 
subject loc2                  
Gaia    GPE         NaN    1.0
        GPi         1.0  150.0
        Thalamus    NaN   54.0
        VLP         8.0    NaN
        VLa         6.0   79.0
        VLp         NaN    6.0
Isis                NaN   33.0
        GPi         5.0  202.0
        M1-G       98.0    NaN
        M1-S      145.0    NaN
        R-V         6.0    6.0
        RTN         3.0   11.0
        S-R         NaN    2.0
        SMA        77.0    NaN
        STR         NaN    2.0
        VLa        24.0  195.0
        VLp        32.0   86.0
paper files 163 dandiset pre files 232
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper/dryad; tr -d '\r' < Fig2_3_S8_S9.m | sed -n 600,1100p | grep -v "^\s*$" | grep -iv "set(gca\|xlabel\|ylabel\|print(\|meta_file\|axis \|xlim\|ylim\|title(\|legend\|subplot\|hold \|figure\|line(\|'FontSize'\|plot(" | sed -n '/ALL RESPONSES/,$p' | head -150; echo ====; tr -d '\r' < FigS2.m
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper/dryad; grep -v "^\s*$" Fig4_S10to13.m | grep -iv "set(gca\|xlabel\|ylabel\|print(\|meta_file\|xlim\|ylim\|title(\|legend\|subplot\|hold \|figure\|'FontSize'" | head -200
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 - <<'EOF'
import re
x=open('paper.xml').read()
i=x.find('normalized CCF'); seg=x[i:i+6000]
seg=re.sub(r'<mml:annotation.*?</mml:annotation>','',seg,flags=re.S)
t=re.sub(r'<[^>]+>',' ',seg); t=re.sub(r'\s+',' ',t)
print(t[:1500])
EOF
```

```
normalized CCF C C F ( τ ) = ∑ s = 1 n y ( t s + τ ) n y ( t ) ¯ was computed for time lags τ ≤200 ms, taking advantage of zero-padding, and averaged over all trials of a recording. t s denotes the s = 1,… n spike times of the GPi neuron, y(t) the binary spike time series of the VLa neuron, and y ( t ) ¯ the average VLa firing rate. Surrogate time series were generated by randomly jittering spike times within intervals of 20 ms as suggested by Amarasingham and colleagues [ 100 ]. This kind of surrogate data left local firing rates unchanged while removing spike synchrony on a time scale of 20 ms or shorter and thereby serving as a negative control for spike synchrony. Average CCFs of surrogate data were subtracted from both trial averaged CCFs for each GPi-VLa unit pair as well as from all control CCFs. All final CCFs were rated by the absolute value of the maximum deviation from zero in the time interval [0,10] ms ([−5,5] ms for CCFs between GPi neurons) after smoothing with a 2-ms moving average filter. Additionally, to control for false negative findings, we simulated Poisson spike trains with known correlations. For each recorded pair, 400 simulated spike trains were matched to the firing rates of GPi and VLa neurons and to peak correlations of value p for very long recording times. By subsampling those simulated spike trains at the length of our recordings, we observed simulated distributions of correlations around the underlying correlation p . This procedure allowed us
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat paper 2>/dev/null; cat paper/dryad/IsoutlierBCS.m; venv/bin/python - <<'EOF'
import h5py, remfile, time
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    url=c.get_dandiset('000947','0.240510.2211').get_asset_by_path('sub-Isis/sub-Isis_ses-pre-MPTP-I-160615-1_ecephys.nwb').get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
for k in ['acquisition/ElectricalSeries/data','processing/ecephys/Processed/ElectricalSeriesProcessedGPi/data']:
    d=f[k]; print(k, d.shape, d.dtype, d.chunks, d.compression)
d=f['processing/ecephys/Processed/ElectricalSeriesProcessedGPi/data']
t=time.time(); x=d[1000000:1000048,:]; print(time.time()-t)
t=time.time(); x=d[5000000:5000048,:]; print(time.time()-t)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

I have enough of the method now. Next: write the helper module and prototype the response-detection algorithm, checking it against the paper's per-unit results for linked units.

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python - <<'EOF'
import h5py, remfile, numpy as np, pandas as pd
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset('000947','0.240510.2211')
    url=ds.get_asset_by_path('sub-Gaia/sub-Gaia_ses-pre-MPTP-G-140511-3_ecephys.nwb').get_content_url(follow_redirects=1, strip_query=True)
f=h5py.File(remfile.File(url),'r')
tr=f['intervals/trials']
df=pd.DataFrame({k:tr[k][:] for k in tr.attrs['colnames']})
print(df.head(10).to_string()); print(df.isna().sum())
print(df.target.value_counts())
if 'error_onset_time' in df: print(df[df.error_onset_time.notna()].head())
U=f['units']; print([ (U['unit_name'][i],U['channel_ids'][i]) for i in range(len(U['id']))])
st=U['spike_times'][:U['spike_times_index'][0]]; print(st[:5], st[-5:], 'trial range', df.start_time.min(), df.stop_time.max())
print('ES dur', f['acquisition/ElectricalSeries/data'].shape[0]/24414.0625)
EOF
```

```
start_time  stop_time  reward_start_time  reward_stop_time  movement_start_time  cue_onset_time    target
0    5.916959   9.146245           8.798290          9.145426             7.925146        7.701135   b'Left'
1   10.604380  15.336653          14.981407         15.335752            13.959701       13.700465   b'Left'
2   16.244982  20.935107          20.638556         20.934287            19.410698       19.200369  b'Right'
3   22.228337  27.583447          27.230863         27.582628            25.872056       25.637356  b'Right'
4   28.572836  33.624146          33.339351         33.620582            31.973130       31.746826   b'Left'
5   34.604728  38.515958          38.151946         38.513091            37.226783       36.996465  b'Right'
6   39.447675  44.525568          44.199363         44.524749            43.124490       42.901627   b'Left'
7   45.604700  50.564833          50.277335         50.560737            49.250550       49.010934  b'Right'
8   51.635937  55.844373          55.526441         55.840891            54.641172       54.433751   b'Left'
9   56.885781  61.931561          61.622641         61.930660            60.331704       60.090859  b'Right'
start_time             0
stop_time              0
reward_start_time      0
reward_stop_time       0
movement_start_time    0
cue_onset_time         0
target                 0
dtype: int64
target
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000947-schwab-2020
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd paper/dryad; $TMPDIR/venv/bin/python -c "
import scipy.io as sio, numpy as np
for mk in ['Gaia','Isis']:
    m=sio.loadmat(mk+'_MvtSum.mat',squeeze_me=True,struct_as_record=False)['MvtSum']
    print(mk, m._fieldnames if hasattr(m,'_fieldnames') else type(m))
    for f in m._fieldnames: x=getattr(m,f); print(' ',f, np.shape(x), x[:3] if np.ndim(x)>0 else x)
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper/dryad; curl -sL -o FigS3.m "https://zenodo.org/records/4000719/files/FigS3.m?download=1"; tr -d '\r' < FigS3.m | grep -v "^\s*$" | head -80
```

Result: the fetched text is not kept.

**Agent**

The EMG onset method is not given anywhere (the S3 code only plots), so that claim will be blocked as methods_underspecified. Writing the helper module now.

**Agent calls Write**

```json
{
 "file_path": "entries/000947-schwab-2020/gpivla.py",
 "content": "\"\"\"Loading and measures for the pre-MPTP GPi and VLa recordings of dandiset 000947.\n\nSchwab, Kase, Zimnik, Rosenbaum, Codianni, Rubin & Turner (2020), PLOS Biology,\ndoi:10.1371/journal.pbio.3000829.\n\nEach NWB file holds one recording block of one monkey (Gaia or Isis): a trials table (cue onset,\nmovement onset and end, target, and in some files error onset), the curated single units in\n`units` (spike times in seconds, a location label, channel id and sort letter), all sorted\nclusters in `processing/ecephys/units`, and raw and 200 Hz high-pass filtered traces. Files are\nstreamed from the archive at the pinned version; nothing is written to disk. Only the curated\n`units` table and the trials are read, except for the action potential width, which reads one\nchunk of the filtered traces per unit.\n\nWhere the parameters come from:\n\n- Paper's Methods: valid trials exclude errors and outliers in reaction time or movement duration\n  (more than 6 median absolute differences from the mean); a unit needs at least 10 valid trials\n  (applied here per direction); its mean rate over the recording must be at least 30 spikes/s in\n  GPi and 1 spike/s in VLa; spike density functions (SDF) use a Gaussian kernel of 25 ms at 1 ms\n  resolution; decreases are detected on the interspike interval (ISI) function, the current ISI\n  at each ms smoothed with the same kernel; the control period is the 700 ms ending at the median\n  cue onset, the test period the 700 ms after it; a linear trend fitted to the control period is\n  removed; a change must last at least 70 ms at an omnibus p < 0.001 (Bonferroni). Correlation\n  windows: rest 1.5 to 1.0 s before movement onset, movement 0.2 s before to 0.3 s after; CCFs in\n  2 ms bins shifted by 1 ms, jitter of 20 ms, peaks in 0 to 10 ms after a 2 ms moving average; noise\n  correlations on 500 ms spike counts, bins with fewer than 10 spikes in total left out, trials\n  with |z| > 3 removed, 400 shuffles; bursts and pauses by the Poisson surprise method (surprise\n  at least 5, bursts of at least 3 spikes at twice the baseline rate, pauses of at least 100 ms),\n  outside the task (0.4 s before movement onset to 0.8 s after the return to the home key); VLa\n  SDF with a 10 ms kernel, from 0.8 s before to 0.8 s after each event.\n- Paper's code (Dryad doi:10.5061/dryad.0cfxpnvxm, mirrored on Zenodo record 4000719):\n  `PeriEventChange_SDF_pctchng.m` fixes the threshold, p = alpha / (control length / 70) and\n  threshold = norminv(1 - p) times the SD of the control, the test period of control length + 1\n  samples, the first run of 70 consecutive supra-threshold samples as onset, and the offset as a\n  return within threshold for 70 samples or a change of sign; `Fig2_3_S8_S9.m` fixes the window\n  (-1500 to +1000 ms from movement onset), the rest rate as the mean SDF from -1500 to -301 ms, and\n  the integrated change as the summed SDF minus that mean from -300 to +399 ms; `Fig4_S10to13.m`\n  fixes the CCF lags (-20 to +20 ms) and that each pair is significant when its peak exceeds the\n  95th percentile of its own jittered controls.\n- Common choices, where neither says: the surprise uses log base 10 (as in Legendy and Salcman);\n  the VLa spikes are the ones jittered; the Poisson probability for a burst uses the unit's mean\n  rest rate.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nimport time\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET_ID = \"000947\"\nDANDISET_VERSION = \"0.240510.2211\"\n\nWIN = (-1500, 1000)            # ms around movement onset (Fig2_3_S8_S9.m, IND_OFFSET = 1500)\nNWIN = WIN[1] - WIN[0] + 1     # 2501 samples\nSIGMA_MS = 25.0                # SDF and ISI kernel (Methods)\nCNTL_MS = 700                  # control and test period length (Methods)\nCONTIG = 70                    # ms a change must last (Methods)\nALPHA = 0.001                  # omnibus p (Methods)\nMIN_TRIALS = 10                # per direction (Methods: 10 valid trials)\nMIN_RATE = {\"GPi\": 30.0, \"VLa\": 1.0}   # spikes/s over the recording (Methods)\nOUTLIER_MADS = 6.0             # Methods: > 6 median absolute differences from the mean\nREST_WIN = (-1.5, -1.0)        # s from movement onset (Methods, correlations)\nMVT_WIN = (-0.2, 0.3)\nTASK_EXCL = (-0.4, 0.8)        # s: from movement onset, to after return end (Methods, bursts)\n\n\n# --- loading -------------------------------------------------------------------------------\n\ndef area(label) -> str:\n    \"\"\"The dandiset's location label with case unified (GPI and GPi, VLA and VLa).\"\"\"\n    text = \"\" if label is None else str(label)\n    return {\"GPI\": \"GPi\", \"VLA\": \"VLa\", \"VLP\": \"VLp\", \"GPE\": \"GPe\"}.get(text.upper(), text)\n\n\ndef file_key(session_id: str) -> str:\n    \"\"\"'pre-MPTP-G-140511-3' -> 'G_140511_3', the file name used in the paper's code.\"\"\"\n    return re.sub(r\"^(pre|post)-MPTP-\", \"\", session_id).replace(\"-\", \"_\")\n\n\ndef asset_urls(pre_only: bool = True) -> list[tuple[str, str]]:\n    \"\"\"(path, streaming URL) of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        out = sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n                     for a in dandiset.get_assets() if a.path.endswith(\".nwb\"))\n    return [p for p in out if not pre_only or \"ses-pre-MPTP\" in p[0]]\n\n\ndef _s(x):\n    return x.decode() if isinstance(x, bytes) else x\n\n\ndef _open(url: str, tries: int = 4):\n    for k in range(tries):\n        try:\n            return h5py.File(remfile.File(url), \"r\")\n        except Exception:\n            if k == tries - 1:\n                raise\n            time.sleep(2 + 3 * k)\n\n\ndef load_session(path: str, url: str) -> dict:\n    \"\"\"Trials, curated units and metadata of one file.\"\"\"\n    f = _open(url)\n    g = f[\"general\"]\n    s = {\"path\": path, \"url\": url, \"session_id\": _s(g[\"session_id\"][()]),\n         \"subject\": _s(g[\"subject/subject_id\"][()]),\n         \"mptp\": _s(g[\"MPTPMetaData\"].attrs.get(\"MPTP_status\", \"\")),\n         \"session_start\": _s(f[\"session_start_time\"][()]),\n         \"groups\": {k: _s(v.attrs.get(\"location\")) for k, v in g[\"extracellular_ephys\"].items()\n                    if k != \"electrodes\"}}\n    s[\"key\"] = file_key(s[\"session_id\"])\n    if \"intervals\" in f and \"trials\" in f[\"intervals\"]:\n        tr = f[\"intervals/trials\"]\n        df = pd.DataFrame({c: tr[c][:] for c in tr.attrs[\"colnames\"]})\n        df[\"target\"] = df[\"target\"].map(_s)\n        s[\"trials\"] = df\n    else:\n        s[\"trials\"] = None\n    units = []\n    if \"units\" in f:\n        u = f[\"units\"]\n        cols = list(u.attrs[\"colnames\"])\n        index = u[\"spike_times_index\"][:]\n        times = u[\"spike_times\"][:]\n        lo = 0\n        for i in range(len(index)):\n            row = {c: _s(u[c][i]) for c in cols if c != \"spike_times\"}\n            row[\"spikes\"] = np.sort(times[lo:index[i]])\n            row[\"sorted_in_file\"] = bool(np.all(np.diff(times[lo:index[i]]) >= 0))\n            lo = index[i]\n            units.append(row)\n    s[\"units\"] = units\n    el = g[\"extracellular_ephys/electrodes\"]\n    s[\"electrodes\"] = pd.DataFrame({\"channel_ids\": [_s(x) for x in el[\"channel_ids\"][:]],\n                                    \"location\": [_s(x) for x in el[\"location\"][:]],\n                                    \"group_name\": [_s(x) for x in el[\"group_name\"][:]]})\n    proc = {}\n    if \"processing\" in f and \"ecephys\" in f[\"processing\"] and \"Processed\" in f[\"processing/ecephys\"]:\n        for name, es in f[\"processing/ecephys/Processed\"].items():\n            proc[name] = {\"electrodes\": es[\"electrodes\"][:], \"shape\": es[\"data\"].shape,\n                          \"chunks\": es[\"data\"].chunks,\n                          \"rate\": float(es[\"data\"].attrs.get(\"rate\", 0) or es.get(\"starting_time\").attrs.get(\"rate\", 0)),\n                          \"start\": float(es[\"starting_time\"][()])}\n    s[\"processed\"] = proc\n    s[\"n_raw\"] = f[\"acquisition/ElectricalSeries/data\"].shape[0] if \"ElectricalSeries\" in f.get(\"acquisition\", {}) else 0\n    f.close()\n    return s\n\n\ndef load_all(paths=None, workers: int = 16) -> list[dict]:\n    \"\"\"Load the pre-MPTP files (or the given (path, url) pairs) in parallel.\"\"\"\n    pairs = asset_urls() if paths is None else paths\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(lambda pu: load_session(*pu), pairs))\n\n\n# --- trials --------------------------------------------------------------------------------\n\ndef _outliers(x: np.ndarray) -> np.ndarray:\n    \"\"\"Methods: values more than 6 median absolute differences away from the mean.\"\"\"\n    x = np.asarray(x, float)\n    ok = np.isfinite(x)\n    if ok.sum() < 3:\n        return np.zeros(len(x), bool)\n    mad = np.median(np.abs(x[ok] - np.median(x[ok])))\n    return ok & (np.abs(x - np.mean(x[ok])) > OUTLIER_MADS * mad)\n\n\ndef valid_trials(trials: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Trials with RT and MT, and the flag `valid`: no error, a target, cue and movement onset,\n    and RT and MT (where the file has movement ends) not outliers within the file.\"\"\"\n    df = trials.copy()\n    df[\"rt\"] = df[\"movement_start_time\"] - df[\"cue_onset_time\"]\n    df[\"mt\"] = (df[\"movement_stop_time\"] - df[\"movement_start_time\"]) if \"movement_stop_time\" in df else np.nan\n    err = df[\"error_onset_time\"].notna() if \"error_onset_time\" in df else pd.Series(False, index=df.index)\n    ok = (~err) & df[\"target\"].isin([\"Left\", \"Right\"]) & df[\"rt\"].notna() & (df[\"rt\"] > 0)\n    df[\"error\"] = err\n    out = pd.Series(False, index=df.index)\n    out[ok] = _outliers(df.loc[ok, \"rt\"].to_numpy()) | _outliers(df.loc[ok, \"mt\"].to_numpy())\n    df[\"outlier\"] = out\n    df[\"valid\"] = ok & ~out\n    return df\n\n\n# --- activity functions --------------------------------------------------------------------\n\ndef _grid(align: np.ndarray, pad: int = 0) -> np.ndarray:\n    ms = np.arange(WIN[0] - pad, WIN[1] + pad + 1) / 1000.0\n    return np.asarray(align)[:, None] + ms[None, :]\n\n\ndef spike_counts_ms(spikes: np.ndarray, align: np.ndarray, pad: int = 100) -> np.ndarray:\n    \"\"\"Spike counts in 1 ms bins (trials x time) from WIN[0]-pad to WIN[1]+pad ms.\"\"\"\n    edges = np.arange(WIN[0] - pad, WIN[1] + pad + 2) / 1000.0\n    out = np.zeros((len(align), len(edges) - 1))\n    for i, a in enumerate(align):\n        lo, hi = np.searchsorted(spikes, [a + edges[0], a + edges[-1]])\n        out[i] = np.histogram(spikes[lo:hi] - a, edges)[0]\n    return out\n\n\ndef sdf(spikes: np.ndarray, align: np.ndarray, sigma: float = SIGMA_MS) -> np.ndarray:\n    \"\"\"Mean spike density (spikes/s) over trials, -1500 to +1000 ms, Gaussian kernel.\"\"\"\n    pad = int(4 * sigma)\n    c = spike_counts_ms(spikes, align, pad).mean(0) * 1000.0\n    return gaussian_filter1d(c, sigma, mode=\"nearest\")[pad:-pad]\n\n\ndef isi_function(spikes: np.ndarray, align: np.ndarray, sigma: float = SIGMA_MS) -> np.ndarray:\n    \"\"\"Mean over trials of the current interspike interval (ms) at each ms, smoothed.\"\"\"\n    pad = int(4 * sigma)\n    t = _grid(align, pad)\n    idx = np.searchsorted(spikes, t, side=\"right\")\n    ok = (idx > 0) & (idx < len(spikes))\n    isi = np.full(t.shape, np.nan)\n    isi[ok] = (spikes[np.minimum(idx[ok], len(spikes) - 1)] - spikes[idx[ok] - 1]) * 1000.0\n    m = np.nanmean(isi, 0)\n    m = pd.Series(m).interpolate(limit_direction=\"both\").to_numpy()\n    return gaussian_filter1d(m, sigma, mode=\"nearest\")[pad:-pad]\n\n\n# --- detection of peri-movement changes ----------------------------------------------------\n\ndef control_fit(func: np.ndarray, cue_idx: int):\n    \"\"\"OLS line over the 700 ms control period; returns (intercept, slope per ms, slope 95% CI).\"\"\"\n    x = np.arange(cue_idx - CNTL_MS, cue_idx)\n    y = func[x]\n    res = stats.linregress(x, y)\n    tcrit = stats.t.ppf(0.975, len(x) - 2)\n    return res.intercept, res.slope, (res.slope - tcrit * res.stderr, res.slope + tcrit * res.stderr)\n\n\ndef detect(func: np.ndarray, median_rt_ms: float, alpha: float = ALPHA, contig: int = CONTIG,\n           detrend: bool = True) -> dict:\n    \"\"\"Increase of `func` above its control period, as PeriEventChange_SDF_pctchng.m with\n    incr_decr = +1, after removing the control period's linear trend (Methods).\n\n    Returns onset and offset (ms from movement onset, NaN when none), the mean change over the\n    response, the control slope per s and whether its 95% CI excludes zero, and the threshold.\"\"\"\n    cue_idx = int(round(-WIN[0] - median_rt_ms))\n    b0, b1, ci = control_fit(func, cue_idx)\n    data = func - (b0 + b1 * np.arange(len(func))) if detrend else func.copy()\n    cntl = data[cue_idx - CNTL_MS:cue_idx]\n    data = data - cntl.mean()\n    p = alpha / (CNTL_MS / contig)\n    thr = stats.norm.ppf(1 - p) * np.std(cntl, ddof=1)\n    test = data[cue_idx:cue_idx + CNTL_MS + 1]\n    out = {\"onset\": np.nan, \"offset\": np.nan, \"mean_change\": np.nan, \"thr\": thr,\n           \"slope_per_s\": b1 * 1000.0, \"slope_sig\": bool(ci[0] > 0 or ci[1] < 0)}\n    above = test > thr\n    run = np.convolve(above.astype(int), np.ones(contig, int), \"valid\")\n    hits = np.flatnonzero(run == contig)\n    if len(hits) == 0:\n        return out\n    on = cue_idx + hits[0]\n    after = data[on + 1:]\n    inside = np.abs(after) < thr\n    run2 = np.convolve(inside.astype(int), np.ones(contig, int), \"valid\")\n    z = np.flatnonzero(run2 == contig)\n    sw = np.flatnonzero((np.sign(after) < 0) & (np.abs(after) > thr))\n    cands = ([z[0] + on + 1] if len(z) else []) + ([sw[0] + on + 1] if len(sw) else [])\n    off = min(cands) if cands else len(data) - 1\n    out.update(onset=on + WIN[0], offset=off + WIN[0], mean_change=float(data[on:off + 1].mean()))\n    return out\n\n\ndef unit_direction(segments: list[tuple[np.ndarray, pd.DataFrame]], target: str) -> dict | None:\n    \"\"\"Detection for one unit and one target over its recording segments (each a spike train and\n    its file's valid trials). Returns None when there are fewer than MIN_TRIALS valid trials.\"\"\"\n    counts, isis, rts = [], [], []\n    for spikes, tr in segments:\n        t = tr[tr.valid & (tr.target == target)]\n        if len(t) == 0:\n            continue\n        align = t[\"movement_start_time\"].to_numpy()\n        counts.append(spike_counts_ms(spikes, align, int(4 * SIGMA_MS)))\n        pad = int(4 * SIGMA_MS)\n        g = _grid(align, pad)\n        idx = np.searchsorted(spikes, g, side=\"right\")\n        ok = (idx > 0) & (idx < len(spikes))\n        isi = np.full(g.shape, np.nan)\n        isi[ok] = (spikes[np.minimum(idx[ok], len(spikes) - 1)] - spikes[idx[ok] - 1]) * 1000.0\n        isis.append(isi)\n        rts.append(t[\"rt\"].to_numpy())\n    n = sum(len(c) for c in counts)\n    if n < MIN_TRIALS:\n        return None\n    pad = int(4 * SIGMA_MS)\n    c = np.vstack(counts)\n    f_sdf = gaussian_filter1d(c.mean(0) * 1000.0, SIGMA_MS, mode=\"nearest\")[pad:-pad]\n    m = pd.Series(np.nanmean(np.vstack(isis), 0)).interpolate(limit_direction=\"both\").to_numpy()\n    f_isi = gaussian_filter1d(m, SIGMA_MS, mode=\"nearest\")[pad:-pad]\n    med_rt = float(np.median(np.concatenate(rts))) * 1000.0\n    inc, dec = detect(f_sdf, med_rt), detect(f_isi, med_rt)\n    base = f_sdf[:1200].mean()                      # Fig2_3_S8_S9.m: -1500 to -301 ms\n    integ = (f_sdf[1200:1900] - base).sum() / 1000  # -300 to +399 ms, spikes\n    return {\"n_trials\": n, \"median_rt_ms\": med_rt, \"sdf\": f_sdf, \"rest_rate\": base,\n            \"integrated\": integ, \"inc_onset\": inc[\"onset\"], \"dec_onset\": dec[\"onset\"],\n            \"inc_change\": inc[\"mean_change\"], \"dec_change\": dec[\"mean_change\"],\n            \"slope_per_s2\": inc[\"slope_per_s\"], \"slope_sig\": inc[\"slope_sig\"],\n            \"trial_counts\": c[:, pad:-pad]}\n\n\ndef response_form(inc: float, dec: float) -> str:\n    \"\"\"'increase', 'decrease', 'inc_first', 'dec_first' or 'none' (Fig2_3_S8_S9.m).\"\"\"\n    i, d = np.isfinite(inc), np.isfinite(dec)\n    if i and d:\n        return \"inc_first\" if inc <= dec else \"dec_first\"\n    return \"increase\" if i else (\"decrease\" if d else \"none\")\n\n\n# --- correlations --------------------------------------------------------------------------\n\nCCF_LAGS = np.arange(-20, 21)            # ms, bin centres; 2 ms bins shifted by 1 ms\n\n\ndef ccf_counts(gpi: np.ndarray, vla: np.ndarray, windows=None):\n    \"\"\"Counts of VLa spikes in 2 ms bins at lags -20..+20 ms from each GPi spike, and the number of\n    GPi spikes and VLa rate used for normalisation. `windows` (n x 2, s) restricts both trains.\"\"\"\n    if windows is not None:\n        keep_g = _in_windows(gpi, windows)\n        gpi = gpi[keep_g]\n        dur = float(np.sum(windows[:, 1] - windows[:, 0]))\n        vla = vla[_in_windows(vla, windows)]\n    else:\n        dur = float(max(gpi.max(), vla.max()) - min(gpi.min(), vla.min()))\n    lo = np.searchsorted(vla, gpi - 0.0225)\n    hi = np.searchsorted(vla, gpi + 0.0225)\n    return gpi, vla, dur, lo, hi\n\n\ndef _in_windows(t: np.ndarray, windows: np.ndarray) -> np.ndarray:\n    idx = np.searchsorted(windows[:, 0], t, side=\"right\") - 1\n    ok = idx >= 0\n    ok[ok] = t[ok] < windows[idx[ok], 1]\n    return ok\n\n\ndef ccf(gpi: np.ndarray, vla: np.ndarray, dur: float) -> np.ndarray:\n    \"\"\"Normalised CCF (Methods): VLa spikes at each lag after GPi spikes, divided by the number of\n    GPi spikes times the expected VLa count per 2 ms bin; 1 means no correlation.\"\"\"\n    d = _pair_diffs(gpi, vla)\n    cnt = np.array([np.sum((d >= (l - 1) / 1000) & (d < (l + 1) / 1000)) for l in CCF_LAGS])\n    expected = len(gpi) * len(vla) / dur * 0.002\n    return cnt / expected\n\n\ndef _pair_diffs(gpi, vla, reach=0.0225):\n    lo = np.searchsorted(vla, gpi - reach)\n    hi = np.searchsorted(vla, gpi + reach)\n    n = hi - lo\n    gi = np.repeat(np.arange(len(gpi)), n)\n    vj = np.concatenate([np.arange(a, b) for a, b in zip(lo, hi)]) if n.sum() else np.array([], int)\n    return vla[vj] - gpi[gi]\n\n\ndef jitter(t: np.ndarray, rng: np.random.Generator, width: float = 0.020) -> np.ndarray:\n    \"\"\"Interval jitter: each spike moved uniformly within its own fixed 20 ms window.\"\"\"\n    return np.sort(np.floor(t / width) * width + rng.random(len(t)) * width)\n\n\ndef ccf_test(gpi: np.ndarray, vla: np.ndarray, dur: float, rng, n_surr: int = 400) -> dict:\n    \"\"\"Peak of the jitter-corrected CCF in 0..10 ms after a 2 ms moving average, its sign, and the\n    95th percentile of the same peak over jittered controls (each corrected by the mean control).\"\"\"\n    real = ccf(gpi, vla, dur)\n    ctrl = np.array([ccf(gpi, jitter(vla, rng), dur) for _ in range(n_surr)])\n    mean_ctrl = ctrl.mean(0)\n\n    def peak(c):\n        c = c - mean_ctrl\n        c = (c + np.roll(c, 1)) / 2           # 2 ms moving average (Fig4_S10to13.m)\n        seg = c[(CCF_LAGS >= 0) & (CCF_LAGS <= 10)]\n        k = np.argmax(np.abs(seg))\n        return np.abs(seg[k]), np.sign(seg[k])\n\n    p_real, s_real = peak(real)\n    p_ctrl = np.array([peak(c)[0] for c in ctrl])\n    return {\"peak\": p_real, \"sign\": s_real, \"ctrl_peaks\": p_ctrl,\n            \"thr95\": np.percentile(p_ctrl, 95), \"significant\": p_real > np.percentile(p_ctrl, 95)}\n\n\ndef ks_permutation(real: np.ndarray, ctrl: np.ndarray) -> float:\n    \"\"\"Fig4_S10to13.m: one-sided KS statistic of the real peaks against the pooled controls,\n    compared with the same statistic for each control set against the others. Returns the\n    fraction of control statistics larger than the real one (the p-value).\"\"\"\n    def ks(a, b):\n        grid = np.sort(np.concatenate([a, b]))\n        fa = np.searchsorted(np.sort(a), grid, side=\"right\") / len(a)\n        fb = np.searchsorted(np.sort(b), grid, side=\"right\") / len(b)\n        return np.max(fb - fa)               # a shifted right of b\n    k = ctrl.shape[1]\n    real_stat = ks(real, ctrl[:, :-1].ravel())\n    ctrl_stat = np.array([ks(ctrl[:, j], np.delete(ctrl, j, axis=1).ravel()) for j in range(k)])\n    return float(np.mean(ctrl_stat > real_stat))\n\n\n# --- bursts and pauses ---------------------------------------------------------------------\n\ndef _poisson_surprise(n_spikes: int, duration: float, rate: float) -> float:\n    \"\"\"-log10 of the Poisson probability of n or more spikes in `duration` at `rate`.\"\"\"\n    return -np.log10(max(stats.poisson.sf(n_spikes - 1, rate * duration), 1e-300))\n\n\ndef bursts(spikes: np.ndarray, rate: float, min_surprise: float = 5.0) -> list[tuple[float, float]]:\n    \"\"\"Legendy and Salcman bursts: start at two consecutive ISIs below half the mean ISI, extend\n    while the surprise grows (up to 10 spikes beyond its maximum), then trim the start while it\n    grows. Kept with surprise >= 5, >= 3 spikes and an intraburst rate >= 2x the baseline.\"\"\"\n    out = []\n    if len(spikes) < 3 or rate <= 0:\n        return out\n    isi = np.diff(spikes)\n    half = 0.5 / rate\n    i, n = 0, len(spikes)\n    while i < n - 2:\n        if not (isi[i] < half and isi[i + 1] < half):\n            i += 1\n            continue\n        j = i + 2\n        best_j, best_s = j, _poisson_surprise(3, spikes[j] - spikes[i], rate)\n        k = j\n        while k + 1 < n and k + 1 - best_j <= 10:\n            k += 1\n            s = _poisson_surprise(k - i + 1, spikes[k] - spikes[i], rate)\n            if s > best_s:\n                best_s, best_j = s, k\n        a = i\n        while best_j - a + 1 > 3:\n            s = _poisson_surprise(best_j - a, spikes[best_j] - spikes[a + 1], rate)\n            if s >= best_s:\n                best_s, a = s, a + 1\n            else:\n                break\n        nsp = best_j - a + 1\n        dur = spikes[best_j] - spikes[a]\n        if best_s >= min_surprise and nsp >= 3 and dur > 0 and (nsp - 1) / dur >= 2 * rate:\n            out.append((spikes[a], spikes[best_j]))\n        i = best_j + 1\n    return out\n\n\ndef pauses(spikes: np.ndarray, rate: float, min_surprise: float = 5.0, min_len: float = 0.1):\n    \"\"\"ISIs of at least 100 ms whose Poisson surprise of zero spikes is at least 5.\"\"\"\n    isi = np.diff(spikes)\n    s = rate * isi / np.log(10)                 # -log10(exp(-rate * isi))\n    k = np.flatnonzero((isi >= min_len) & (s >= min_surprise))\n    return [(spikes[i], spikes[i + 1]) for i in k]\n\n\ndef triggered_average(spikes: np.ndarray, events: np.ndarray, half: float = 0.8,\n                      sigma_ms: float = 10.0) -> np.ndarray:\n    \"\"\"Mean VLa SDF (spikes/s, 1 ms) from -0.8 to +0.8 s around the events.\"\"\"\n    edges = np.arange(-half - 0.05, half + 0.05 + 0.0005, 0.001)\n    acc = np.zeros(len(edges) - 1)\n    for e in events:\n        lo, hi = np.searchsorted(spikes, [e + edges[0], e + edges[-1]])\n        acc += np.histogram(spikes[lo:hi] - e, edges)[0]\n    acc = acc / max(len(events), 1) * 1000.0\n    return gaussian_filter1d(acc, sigma_ms)[50:-50]\n\n\n# --- action potential width ----------------------------------------------------------------\n\ndef ap_width(url: str, series: str, column: int, spikes: np.ndarray, rate: float,\n             start: float, chunk: int, max_spikes: int = 300) -> tuple[float, int]:\n    \"\"\"Trough-to-peak time (ms) of the mean waveform on the unit's channel of the filtered trace,\n    from the spikes inside the one HDF5 chunk that holds the most of them.\"\"\"\n    idx = np.round((spikes - start) * rate).astype(int)\n    which = idx // chunk\n    vals, counts = np.unique(which, return_counts=True)\n    c = vals[np.argmax(counts)]\n    f = _open(url)\n    d = f[f\"processing/ecephys/Processed/{series}/data\"]\n    lo, hi = c * chunk, min((c + 1) * chunk, d.shape[0])\n    trace = d[lo:hi, column]\n    f.close()\n    pre, post = int(0.0006 * rate), int(0.0012 * rate)\n    sel = idx[(which == c)] - lo\n    sel = sel[(sel > pre) & (sel < len(trace) - post)][:max_spikes]\n    if len(sel) < 10:\n        return np.nan, len(sel)\n    w = np.mean([trace[k - pre:k + post] for k in sel], 0)\n    t0 = int(np.argmin(w))\n    t1 = t0 + int(np.argmax(w[t0:]))\n    return (t1 - t0) / rate * 1000.0, len(sel)\n"
}
```

```
File created successfully at: entries/000947-schwab-2020/gpivla.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000947-schwab-2020; python3 - <<'EOF'
import re
p='gpivla.py'; s=open(p).read()
s=s.replace('''                          "rate": float(es["data"].attrs.get("rate", 0) or es.get("starting_time").attrs.get("rate", 0)),''','''                          "rate": float(es["starting_time"].attrs["rate"]),''')
# drop unused ccf_counts
i=s.index('def ccf_counts'); j=s.index('def _in_windows')
s=s[:i]+s[j:]
open(p,'w').write(s)
EOF
cd $TMPDIR; cat > proto.py <<'EOF'
import sys, time, pickle
sys.path.insert(0,'entries/000947-schwab-2020')
import gpivla as g
t=time.time(); S=g.load_all(); print('loaded', len(S), time.time()-t)
pickle.dump(S, open('sessions.pkl','wb'))
EOF
venv/bin/python proto.py
```

```
loaded 254 202.89092135429382
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > proto2.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, scipy.io as sio
sys.path.insert(0,'entries/000947-schwab-2020')
import gpivla as g
S=pickle.load(open('sessions.pkl','rb'))
byk={s['key']:s for s in S}
for s in S:
    if s['trials'] is not None: s['vt']=g.valid_trials(s['trials'])
rows=[]
for mk in ['Gaia','Isis']:
    m=sio.loadmat(f'paper/dryad/{mk}_Analy.mat',squeeze_me=True,struct_as_record=False)
    A=m['RespSDFIncr']; B=m['RespISIIncr']
    for i in range(len(A.fname)):
        ut=str(A.unit_type[i])
        if ut=='VLp' or np.isnan(A.evt_sdf[i,:,0]).any(): continue
        segs=[]
        for fk in str(A.fname[i]).split('/'):
            s=byk.get(fk)
            us=[u for u in s['units'] if g.area(u.get('location'))!='' and float(u.get('channel_ids') if u.get('channel_ids') not in ('',None) else np.nan)==float(A.Uchan[i]) and str(u.get('sort_label')).replace('1.0','a')==A.Usort[i]] if s else []
            if len(us)==1: segs.append((us[0]['spikes'], s['vt']))
        if len(segs)!=len(str(A.fname[i]).split('/')): continue
        for t,tg in enumerate(['Left','Right']):
            r=g.unit_direction(segs,tg)
            if r is None: rows.append(dict(mk=mk,i=i,ut=ut,t=t,none=True)); continue
            ref=A.evt_sdf[i,t,:]
            rows.append(dict(mk=mk,i=i,ut=ut,t=t,n=r['n_trials'],nref=np.shape(A.evt_spkt[i,t])[0],
              r=np.corrcoef(r['sdf'],ref)[0,1], ratio=r['sdf'].mean()/ref.mean(),
              inc=r['inc_onset'],inc_ref=A.on_ind[i,t]-1500, dec=r['dec_onset'],dec_ref=B.on_ind[i,t]-1500,
              rest=r['rest_rate'], rest_ref=ref[:1200].mean()))
D=pd.DataFrame(rows); D.to_pickle('proto2.pkl')
print(len(D), D.none.sum() if 'none' in D else 0)
D=D[D.n.notna()]
print('n trials equal', (D.n==D.nref).mean(), 'r>0.9', (D.r>0.9).mean(), D.r.median(), 'ratio', D.ratio.median())
print('inc detect agree', ((D.inc.notna())==(D.inc_ref.notna())).mean(), 'dec agree', ((D.dec.notna())==(D.dec_ref.notna())).mean())
both=D[D.inc.notna()&D.inc_ref.notna()]; print('inc onset diff median abs', (both.inc-both.inc_ref).abs().median())
both=D[D.dec.notna()&D.dec_ref.notna()]; print('dec onset diff median abs', (both.dec-both.dec_ref).abs().median())
print(pd.crosstab(D.inc.notna(),D.inc_ref.notna()), pd.crosstab(D.dec.notna(),D.dec_ref.notna()))
print(D[D.n!=D.nref][['mk','i','t','n','nref']].head(15))
EOF
venv/bin/python proto2.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > proto3.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, scipy.io as sio
sys.path.insert(0,'entries/000947-schwab-2020')
import gpivla as g
S=pickle.load(open('sessions.pkl','rb')); byk={s['key']:s for s in S}
from scipy.special import erfcinv
def rule(x, kind):
    x=np.asarray(x,float); ok=np.isfinite(x)
    if ok.sum()<3: return np.zeros(len(x),bool)
    med=np.median(x[ok]); mad=np.median(np.abs(x[ok]-med))
    if kind=='none': return np.zeros(len(x),bool)
    if kind=='6mad_mean': return ok&(np.abs(x-np.mean(x[ok]))>6*mad)
    if kind=='6mad_med': return ok&(np.abs(x-med)>6*mad)
    if kind=='bcs10': c=-1/(np.sqrt(2)*erfcinv(1.5)); return ok&(np.abs(x-med)>=10*c*mad)
    if kind=='iso3': c=-1/(np.sqrt(2)*erfcinv(1.5)); return ok&(np.abs(x-med)>3*c*mad)
res={}
for kind in ['none','6mad_mean','6mad_med','bcs10','iso3']:
  for rtonly in [True, False]:
    eq=[]; 
    for mk in ['Gaia','Isis']:
        A=sio.loadmat(f'paper/dryad/{mk}_Analy.mat',squeeze_me=True,struct_as_record=False)['RespSDFIncr']
        for i in range(len(A.fname)):
            fk=str(A.fname[i]).split('/')
            if len(fk)>1 or fk[0] not in byk or byk[fk[0]]['trials'] is None: continue
            tr=byk[fk[0]]['trials'].copy()
            tr['rt']=tr.movement_start_time-tr.cue_onset_time
            tr['mt']=tr.movement_stop_time-tr.movement_start_time if 'movement_stop_time' in tr else np.nan
            err=tr.error_onset_time.notna() if 'error_onset_time' in tr else False
            ok=(~err)&tr.rt.notna()
            out=pd.Series(False,index=tr.index)
            o=rule(tr.loc[ok,'rt'],kind)
            if not rtonly: o=o|rule(tr.loc[ok,'mt'],kind)
            out[ok]=o
            v=tr[ok&~out]
            for t,tg in enumerate(['Left','Right']):
                eq.append((v.target==tg).sum()==np.shape(A.evt_spkt[i,t])[0])
    print(kind, rtonly, np.mean(eq), len(eq))
EOF
venv/bin/python proto3.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -v "Deprecation\|ok=(~err)" /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f29b5c8b-1452-41e7-ae05-b8a8e260f95f/tool-results/bzo9wg8m9.txt
```

```
none True 0.7152103559870551 618
none False 0.7152103559870551 618
6mad_mean True 0.6084142394822006 618
6mad_mean False 0.6148867313915858 618
6mad_med True 0.6197411003236246 618
6mad_med False 0.63915857605178 618
bcs10 True 0.7313915857605178 618
bcs10 False 0.7508090614886731 618
iso3 True 0.42394822006472493 618
iso3 False 0.4110032362459547 618
```

**Agent calls Write**

```json
{
 "file_path": "claims/000947/10.1371-journal.pbio.3000829.yaml",
 "content": "# Claims for Schwab, Kase, Zimnik, Rosenbaum, Codianni, Rubin & Turner (2020) on dandiset 000947.\n# Source: the full text (open access, PLOS Biology), read from its Results, tables, figure legends,\n# Methods and supporting figure legends.\n#\n# When these criteria were written, the author had seen the data check only: the file list and\n# metadata of every file, the location labels, channels, sort letters and spike counts of the\n# curated units, the trial tables, and the link of the paper's unit list (the Dryad deposit\n# doi:10.5061/dryad.0cfxpnvxm, files Gaia_Analy.mat and Isis_Analy.mat) to the dandiset's units,\n# with the agreement of this attempt's spike density functions and detected onsets with the ones\n# stored in those files (median correlation 0.999; increase detection agreeing for 91% and decrease\n# detection for 81% of unit-directions; trial counts equal for 63%). No claim's statistic had been\n# computed.\n#\n# The dandiset holds 378 files; 254 are pre-MPTP recordings, the condition of the paper. Its\n# curated `units` tables carry a location label per unit; some labels differ only in case (GPI,\n# VLA), some Gaia VLa units are labelled \"Thalamus\", and some Isis units have no label.\n#\n# Unit selection, fixed here for every claim on single units (the \"dandiset rule\"): curated units\n# in pre-MPTP files whose location label is GPi or VLa ignoring case; valid trials as the Methods\n# define them (no error, reaction time and movement duration not more than 6 median absolute\n# differences from the file's mean); a unit-direction is analysed when it has at least 10 valid\n# trials; a unit is kept when its mean rate (spikes over the span of its spike train) is at least\n# 30 spikes/s in GPi or 1 spike/s in VLa. The dandiset has no identifier that follows a neuron\n# across files, so each file's unit is counted as one unit. The paper's own unit list, linked\n# through unit-link, is shown as a variant for every claim and does not decide outcomes.\n#\n# Method choices fixed here from the Methods and the paper's code (PeriEventChange_SDF_pctchng.m,\n# Fig2_3_S8_S9.m, Fig4_S10to13.m): activity aligned to movement onset from -1500 to +1000 ms;\n# SDF and ISI functions with a 25 ms Gaussian kernel; control period the 700 ms before the median\n# cue onset, test period the following 701 ms; the control period's linear trend removed; a change\n# needs 70 consecutive ms above norminv(1 - 0.001/10) control SDs; increases from the SDF,\n# decreases from the ISI function; a response's latency is its onset; the rest rate is the mean\n# SDF from -1500 to -301 ms; the integrated change is the summed SDF minus that rate from -300 to\n# +399 ms, in spikes. Statistics are over unit-directions where the paper's code uses them so (rest\n# rate, integrated change, latencies), and over units otherwise.\nschema_version: 1\ndandiset: \"000947\"\npaper: doi:10.1371/journal.pbio.3000829\nclaims:\n- id: unit-link\n  statement: The units the paper analysed can be found in the dandiset, and the dandiset's spike\n    times and trials reproduce the per-unit peri-movement activity the paper's code stored.\n  source: Data Availability; Dryad doi:10.5061/dryad.0cfxpnvxm, Gaia_Analy.mat and Isis_Analy.mat\n  data: with_inputs\n  criterion: Records are matched by file name (session_id), channel id and sort letter of the\n    curated units. For the 394 records the paper's code keeps (not VLp, no missing SDF), the link\n    holds (reproduced) when at least 90% are found in every file they span and, for matched\n    unit-directions with at least 10 valid trials, the SDF computed from the dandiset correlates\n    with the stored SDF at r > 0.9 for at least 90%. Partially reproduced when 50 to 90% of the\n    records are found or match; not reproduced below 50%. Trial counts and the location labels of\n    the matched units are reported.\n- id: table1-unit-counts\n  statement: 209 single units met the criteria to be included as GPi neurons (105 in NHP G, 104 in\n    NHP I) and 185 as VLa neurons (66 and 119).\n  source: Results, first section; Table 1\n  expected:\n  - quantity: GPi units\n    value: 209\n    tolerance: 20.9\n  - quantity: VLa units\n    value: 185\n    tolerance: 18.5\n  criterion: Units under the dandiset rule, counted by area. Reproduced when both counts are within\n    tolerance. The Results text gives 218 VLa units where Table 1 gives 185; both readings are\n    checked for VLa. Counts per animal are reported, and, as variants, the count of distinct\n    channel and sort letter combinations per day (treating them as one neuron, an assumption) and\n    the count of the paper's list found in the dandiset.\n- id: table1-rest-rate\n  statement: The resting firing rate of GPi neurons (mean 70.1 spikes/s) is significantly higher\n    than that of VLa neurons (13.5 spikes/s), and the rates are consistent between the two animals.\n  source: Results, first section; Table 1\n  expected:\n  - quantity: GPi mean rest rate\n    value: 70.1\n    tolerance: 7.01\n    unit: spikes/s\n  - quantity: VLa mean rest rate\n    value: 13.5\n    tolerance: 1.35\n    unit: spikes/s\n  criterion: Rest rate per unit-direction as the mean SDF from -1500 to -301 ms around movement\n    onset (Fig2_3_S8_S9.m), averaged over unit-directions. Reproduced when both means are within\n    tolerance and a rank sum test finds GPi higher (p < 0.05). Per animal values are reported.\n- id: table1-ap-width\n  statement: Action potentials of GPi neurons are shorter than those of VLa neurons (trough to\n    peak 0.24 against 0.50 ms; rank sum p = 1e-33).\n  source: Results, first section; Table 1\n  expected:\n  - quantity: GPi mean action potential width\n    value: 0.24\n    tolerance: 0.024\n    unit: ms\n  - quantity: VLa mean action potential width\n    value: 0.50\n    tolerance: 0.05\n    unit: ms\n  criterion: Width as the time from the trough to the following peak of the mean waveform on the\n    unit's channel in the dandiset's 200 Hz high-pass filtered trace, from the spikes in one\n    stored chunk (about 3.2 s) per unit. Reproduced when both means are within tolerance and GPi\n    widths are smaller (rank sum p < 0.05); partially reproduced when only the difference holds.\n- id: hold-period-ramps\n  statement: The firing rate of most units ramps during the start-position hold period (97% of\n    GPi and 98% of VLa units with a significant linear trend); slopes are distributed symmetrically\n    around zero, without a difference between GPi and VLa (rank sum p = 0.29).\n  source: Results, first section; Fig 2A\n  expected:\n  - quantity: GPi units with a significant hold-period slope\n    value: 97\n    tolerance: 9.7\n    unit: percent\n  - quantity: VLa units with a significant hold-period slope\n    value: 98\n    tolerance: 9.8\n    unit: percent\n  criterion: A unit has a significant slope when the 95% CI of the OLS slope of its mean SDF over\n    the control period excludes zero in at least one direction (Fig2_3_S8_S9.m). Reproduced when\n    both fractions are within tolerance and the slopes of GPi and VLa do not differ by a rank sum\n    test (p >= 0.05). The mean slopes (paper -0.05 and -0.14 spikes/s2) are reported.\n- id: mvt-responsive-fraction\n  statement: Nearly all units change their discharge around movement for at least one direction\n    (GPi 99%, 206 of 209; VLa 88.1%, 163 of 185 in Table 1, 94% in the text).\n  source: Results, second section; Table 1\n  expected:\n  - quantity: GPi movement-responsive units\n    value: 99\n    tolerance: 9.9\n    unit: percent\n  - quantity: VLa movement-responsive units\n    value: 88.1\n    tolerance: 8.81\n    unit: percent\n  criterion: A unit is responsive when an increase or a decrease is detected for at least one\n    direction. Reproduced when both fractions are within tolerance; VLa is read as 88.1% (Table\n    1) or 94% (text, tolerance 9.4), and either reading counts.\n- id: increases-most-common\n  statement: Monophasic increases are the most common form of response in both GPi and VLa (48.7%\n    and 65.3% of responses), and increases make up most detected changes (61.5% and 68.8%,\n    biphasic responses counted twice), more than decreases (chi-squared p = 1.2e-17).\n  source: Results, second section; Table 1; Fig 2B\n  expected:\n  - quantity: GPi monophasic increases, percent of responses\n    value: 48.7\n    tolerance: 4.87\n  - quantity: VLa monophasic increases, percent of responses\n    value: 65.3\n    tolerance: 6.53\n  - quantity: GPi increases, percent of changes\n    value: 61.5\n    tolerance: 6.15\n  - quantity: VLa increases, percent of changes\n    value: 68.8\n    tolerance: 6.88\n  criterion: Over unit-directions with a response. Reproduced when monophasic increase is the most\n    common of the four forms in both areas, increases exceed 50% of changes in both areas, and all\n    four values are within tolerance. Partially reproduced when the order holds (increases most\n    common in both) but a value is outside tolerance.\n- id: monophasic-more-in-vla\n  statement: Monophasic changes are more common in VLa than in GPi (88.9% against 66.7% of\n    responses; chi-squared p = 2.8e-12), and polyphasic responses more common in GPi.\n  source: Results, second section; Table 1\n  expected:\n  - quantity: GPi monophasic responses, percent\n    value: 66.7\n    tolerance: 6.67\n  - quantity: VLa monophasic responses, percent\n    value: 88.9\n    tolerance: 8.89\n  criterion: Over unit-directions with a response, a chi-squared test of monophasic against\n    polyphasic by area. Reproduced when both values are within tolerance and VLa is higher with p\n    < 0.05; partially reproduced when only the significant difference holds.\n- id: integrated-change-positive\n  statement: The mean integrated change in firing over the peri-movement epoch is positive in both\n    GPi and VLa (3.89 and 1.75 spikes), significantly different from zero.\n  source: Results, second section; Table 1\n  expected:\n  - quantity: GPi mean integrated change\n    value: 3.89\n    tolerance: 0.389\n    unit: spikes\n  - quantity: VLa mean integrated change\n    value: 1.75\n    tolerance: 0.175\n    unit: spikes\n  criterion: Over unit-directions (Fig2_3_S8_S9.m). Reproduced when both means are positive with a\n    signed rank test against zero at p < 0.05 and both are within tolerance; partially reproduced\n    when both are significantly positive but a value is outside tolerance. Table 1 gives the unit\n    as \"sp x 10^3\"; the code divides the summed rate deviation in spikes/s at 1 ms by 1000, which\n    gives spikes, and that is the reading used.\n- id: fig3a-vla-leads-gpi\n  statement: Peri-movement changes begin later in GPi than in VLa (median onsets -47 and -90 ms;\n    rank sum p = 2.4e-5).\n  source: Results, third section; Fig 3A\n  expected:\n  - quantity: GPi median onset, all changes\n    value: -47\n    tolerance: 4.7\n    unit: ms\n  - quantity: VLa median onset, all changes\n    value: -90\n    tolerance: 9\n    unit: ms\n  criterion: All detected increases and decreases pooled per area (Fig2_3_S8_S9.m, \"ALL\n    RESPONSES\"). Reproduced when GPi onsets are later than VLa onsets by a rank sum test (p < 0.05)\n    and both medians are within tolerance; partially reproduced when only the significant\n    difference holds.\n- id: fig3b-gpi-decr-lag-vla-incr\n  statement: GPi decreases lag behind VLa increases (median onsets -27 and -88 ms; rank sum p =\n    4.9e-4), against the gating prediction.\n  source: Results, third section; Fig 3B\n  expected:\n  - quantity: GPi decrease median onset\n    value: -27\n    tolerance: 2.7\n    unit: ms\n  - quantity: VLa increase median onset\n    value: -88\n    tolerance: 8.8\n    unit: ms\n  criterion: As fig3a-vla-leads-gpi, on GPi decreases against VLa increases.\n- id: fig3c-vla-decr-lead-gpi-incr\n  statement: VLa decreases precede GPi increases (median onsets -108 and -62 ms; rank sum p =\n    0.01).\n  source: Results, third section; Fig 3C\n  expected:\n  - quantity: VLa decrease median onset\n    value: -108\n    tolerance: 10.8\n    unit: ms\n  - quantity: GPi increase median onset\n    value: -62\n    tolerance: 6.2\n    unit: ms\n  criterion: As fig3a-vla-leads-gpi, on VLa decreases against GPi increases.\n- id: gating-conflict-fraction\n  statement: Comparing every GPi response with every VLa response, 96% of comparisons conflict with\n    gating (178,846 of 187,154); only 4% have a GPi onset 0 to 50 ms before the VLa onset with the\n    opposite sign.\n  source: Results, third section\n  expected:\n    quantity: Comparisons that conflict with gating\n    value: 96\n    tolerance: 9.6\n    unit: percent\n  criterion: Every detected GPi change against every detected VLa change; a comparison fits gating\n    when the GPi onset precedes the VLa onset by 0 to 50 ms and the signs are opposite. Reproduced\n    when the conflicting fraction is within tolerance.\n- id: directional-units\n  statement: A majority of GPi neurons (109 of 206) and some VLa neurons (56 of 179) respond\n    significantly more strongly to one movement direction.\n  source: Results, second section; Methods\n  expected:\n  - quantity: GPi directional units, percent of responsive\n    value: 52.9\n    tolerance: 5.29\n  - quantity: VLa directional units, percent of responsive\n    value: 31.3\n    tolerance: 3.13\n  criterion: For responsive units, trial spike counts in the 300 ms from the unit's earliest\n    detected onset compared between left and right trials (rank sum p < 0.005, Methods).\n    Reproduced when both fractions are within tolerance; partially reproduced when GPi is\n    directional more often than VLa (chi-squared p < 0.05) but a value is outside tolerance.\n- id: fig4-ccf-rare\n  statement: Short-time-scale spike-to-spike correlations between simultaneously recorded GPi and\n    VLa units are rare (3.5% of 427 pairs over whole recordings, 2.2% of 183 at rest, 5.2% of 172\n    during movement) and their peaks are not larger than those of jittered controls (p = 0.975,\n    0.675 and 0.998).\n  source: Results, fourth section; Fig 4A-F; Table 2\n  criterion: A claim of absence judged on the paper's test, the one-sided permutation test of the\n    KS statistic of peak absolute CCFs (0 to 10 ms) against jittered controls (Fig4_S10to13.m).\n    Reproduced when p >= 0.05 in all three periods; not reproduced when p < 0.05 in any. Pairs are\n    GPi and VLa units of the dandiset rule in the same file, with at least 100 spikes each in the\n    period. The fraction of significant pairs, its binomial test against 5%, and the signs of the\n    significant peaks are reported.\n- id: fig4-noise-corr-rare\n  statement: Trial-to-trial noise correlations between GPi and VLa are rare (5.4% of 332 pairs at\n    rest, 7.2% of 372 during movement), not different from shuffled controls (p = 0.07 and 0.388),\n    and equally often positive and negative.\n  source: Results, fourth section; Fig 4G-H; Table 2\n  criterion: A claim of absence judged on the paper's test, the one-sided permutation test of the\n    KS statistic of the absolute noise correlations against trial-shuffled controls. Reproduced\n    when p >= 0.05 in both periods; not reproduced when p < 0.05 in either. Noise correlations are\n    computed per pair and target on 500 ms spike counts in the rest and movement windows, with the\n    Methods' exclusions; the fraction outside the 2.5 to 97.5 percentiles of the pooled shuffles\n    and its sign balance are reported, counted (a) over pair-targets and (b) over pairs.\n- id: fig5-vla-decrease-after-gpi-bursts\n  statement: At rest, GPi burst onsets, burst offsets and pause onsets are each followed by a small,\n    slow decrease of the population VLa firing rate.\n  source: Results, fifth section; Fig 5A-C; Table 2\n  criterion: Bursts and pauses detected outside the task by the Poisson surprise method (Methods);\n    VLa SDF (10 ms kernel) averaged around each event per pair, pairs with noisy baselines left\n    out as the Methods say; population average over pairs. Its control is the same average with\n    the events shifted by random offsets of 2 to 20 s within rest, 400 times, with the 2.5 and 97.5\n    percentile band widened so that 5% of controls cross it anywhere in 0 to 300 ms. Reproduced when\n    the population average falls below the band within 0 to 300 ms after the event for all three\n    event types; partially reproduced for one or two. The onset of the decrease (paper 119, 95 and\n    50 ms) and the per-pair fractions of significant changes are reported.\n- id: behavior-rt-mt\n  statement: Reaction times do not differ between the animals or reach directions; movement\n    durations are longer for reaches to the right target, and NHP G moves more slowly than NHP I.\n  source: Results, Task performance; S2 Fig\n  criterion: Per file and direction, the median reaction time and movement duration of valid\n    trials; a two-way ANOVA (animal, direction, interaction). Reproduced when the reaction time has\n    no significant animal or direction effect (p >= 0.05) and the movement duration has both,\n    right longer and G slower (p < 0.05). Partially reproduced when the movement duration part\n    holds and the reaction time part does not, or the reverse.\n- id: figs3-emg-onset\n  statement: Agonist EMG activity begins well before movement onset, at similar times in both\n    animals (-123 and -135 ms).\n  source: Results, Task performance; S3 Fig\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.0cfxpnvxm (S3_EMGdata_NHP_G.mat, S3_EMGdata_NHP_I.mat), mirrored on\n    Zenodo record 4000719\n- id: fig1-vla-localization\n  statement: Thalamic neurons inhibited by GPi stimulation lie dorsal and anterior to neurons\n    excited by SCP stimulation, with a narrow border between VLa and VLp.\n  source: Results, first section; Fig 1; S1 Fig\n- id: fig6-simulation\n  statement: In a model thalamocortical cell with N converging GPi inputs, post-spike inhibition\n    grows with GPi synchrony c and shrinks with convergence N, approximately as ((N - 1)/N)c + 1/N.\n  source: Results, sixth section; Fig 6\n  data: elsewhere\n  where: Dryad doi:10.5061/dryad.0cfxpnvxm (Data_Fig6.mat, simulation output), mirrored on Zenodo\n    record 4000719\n"
}
```

```
File created successfully at: claims/000947/10.1371-journal.pbio.3000829.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Claims file written (20 claims). Now replacing the CCF code in the helper with a faster jitter implementation, then building the notebook.

**Agent calls Bash**

```bash
cd entries/000947-schwab-2020; grep -n "^def \|^CCF_LAGS\|^# ---" gpivla.py
```

```
76:# --- loading -------------------------------------------------------------------------------
78:def area(label) -> str:
84:def file_key(session_id: str) -> str:
89:def asset_urls(pre_only: bool = True) -> list[tuple[str, str]]:
98:def _s(x):
102:def _open(url: str, tries: int = 4):
112:def load_session(path: str, url: str) -> dict:
161:def load_all(paths=None, workers: int = 16) -> list[dict]:
168:# --- trials --------------------------------------------------------------------------------
170:def _outliers(x: np.ndarray) -> np.ndarray:
180:def valid_trials(trials: pd.DataFrame) -> pd.DataFrame:
196:# --- activity functions --------------------------------------------------------------------
198:def _grid(align: np.ndarray, pad: int = 0) -> np.ndarray:
203:def spike_counts_ms(spikes: np.ndarray, align: np.ndarray, pad: int = 100) -> np.ndarray:
213:def sdf(spikes: np.ndarray, align: np.ndarray, sigma: float = SIGMA_MS) -> np.ndarray:
220:def isi_function(spikes: np.ndarray, align: np.ndarray, sigma: float = SIGMA_MS) -> np.ndarray:
233:# --- detection of peri-movement changes ----------------------------------------------------
235:def control_fit(func: np.ndarray, cue_idx: int):
244:def detect(func: np.ndarray, median_rt_ms: float, alpha: float = ALPHA, contig: int = CONTIG,
278:def unit_direction(segments: list[tuple[np.ndarray, pd.DataFrame]], target: str) -> dict | None:
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/000947-schwab-2020/gpivla.py",
 "offset": 323,
 "limit": 135
}
```

```
323	# --- correlations --------------------------------------------------------------------------
324	
325	CCF_LAGS = np.arange(-20, 21)            # ms, bin centres; 2 ms bins shifted by 1 ms
326	
327	
328	def _in_windows(t: np.ndarray, windows: np.ndarray) -> np.ndarray:
329	    idx = np.searchsorted(windows[:, 0], t, side="right") - 1
330	    ok = idx >= 0
331	    ok[ok] = t[ok] < windows[idx[ok], 1]
332	    return ok
333	
334	
335	def ccf(gpi: np.ndarray, vla: np.ndarray, dur: float) -> np.ndarray:
336	    """Normalised CCF (Methods): VLa spikes at each lag after GPi spikes, divided by the number of
337	    GPi spikes times the expected VLa count per 2 ms bin; 1 means no correlation."""
338	    d = _pair_diffs(gpi, vla)
339	    cnt = np.array([np.sum((d >= (l - 1) / 1000) & (d < (l + 1) / 1000)) for l in CCF_LAGS])
340	    expected = len(gpi) * len(vla) / dur * 0.002
341	    return cnt / expected
342	
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000947-schwab-2020; python3 - <<'EOF'
p='gpivla.py'; s=open(p).read()
i=s.index('def ccf(gpi'); j=s.index('def ks_permutation')
new='''def _bins(gpi: np.ndarray, vla: np.ndarray, reach: float = 0.0215):
    """Index pairs (GPi spike, VLa spike) whose 20 ms jitter window can fall within `reach` s of
    each other, with the start of the VLa spike's window and its offset in it."""
    w = np.floor(vla / 0.020) * 0.020
    lo = np.searchsorted(w, gpi - reach - 0.020)
    hi = np.searchsorted(w, gpi + reach, side="right")
    n = hi - lo
    gi = np.repeat(np.arange(len(gpi)), n)
    vj = (np.repeat(lo - np.cumsum(np.r_[0, n[:-1]]), n) + np.arange(n.sum())).astype(int)
    return gi, vj, w


def _lag_counts(d: np.ndarray) -> np.ndarray:
    """Counts in 2 ms bins centred on -20..+20 ms (each bin [L-1, L+1) ms)."""
    k = np.floor(d * 1000.0).astype(int) + 21            # 1 ms bins from -21 ms
    c1 = np.bincount(k[(k >= 0) & (k < 42)], minlength=42)
    return c1[:-1] + c1[1:]


def ccf_test(gpi: np.ndarray, vla: np.ndarray, dur: float, rng: np.random.Generator,
             n_surr: int = 400) -> dict:
    """Normalised CCF (Methods: VLa spikes at each lag after GPi spikes over the number of GPi
    spikes times the mean VLa count per bin) at lags -20..+20 ms in 2 ms bins, its jittered controls
    (VLa spikes moved uniformly within fixed 20 ms windows), and the peak of the control-corrected
    CCF in 0..10 ms after a 2 ms moving average, with the 95th percentile of the same peak over the
    controls. A pair is significant when its peak exceeds that percentile (Fig4_S10to13.m)."""
    gi, vj, w = _bins(gpi, vla)
    expected = len(gpi) * len(vla) / dur * 0.002
    real = _lag_counts(vla[vj] - gpi[gi]) / expected
    base = w[vj] - gpi[gi]
    ctrl = np.empty((n_surr, len(CCF_LAGS)))
    for k in range(n_surr):
        u = rng.random(len(vla)) * 0.020
        ctrl[k] = _lag_counts(base + u[vj]) / expected
    mean_ctrl = ctrl.mean(0)
    sel = (CCF_LAGS >= 0) & (CCF_LAGS <= 10)

    def peak(c):
        c = c - mean_ctrl
        c = (c + np.r_[c[0], c[:-1]]) / 2       # 2 ms moving average
        seg = c[sel]
        k = int(np.argmax(np.abs(seg)))
        return np.abs(seg[k]), np.sign(seg[k])

    p_real, s_real = peak(real)
    p_ctrl = np.array([peak(c)[0] for c in ctrl])
    thr = np.percentile(p_ctrl, 95)
    return {"peak": p_real, "sign": s_real, "ctrl_peaks": p_ctrl, "thr95": thr,
            "significant": bool(p_real > thr), "ccf": real - mean_ctrl}


'''
s=s[:i]+new+s[j:]
s=s.replace('''def _poisson_surprise(n_spikes: int, duration: float, rate: float) -> float:
    """-log10 of the Poisson probability of n or more spikes in `duration` at `rate`."""
    return -np.log10(max(stats.poisson.sf(n_spikes - 1, rate * duration), 1e-300))''','''def _poisson_surprise(n_spikes: int, duration: float, rate: float) -> float:
    """-log10 of the Poisson probability of n or more spikes in `duration` at `rate`."""
    return -np.log10(max(gammainc(n_spikes, rate * duration), 1e-300))''')
s=s.replace("from scipy.ndimage import gaussian_filter1d","from scipy.ndimage import gaussian_filter1d\nfrom scipy.special import gammainc")
i=s.index('def triggered_average'); j=s.index('# --- action potential width')
new2='''def event_sums(rate_ms: np.ndarray, events_ms: np.ndarray) -> np.ndarray:
    """X(L) = sum over events e of rate_ms[e + L], for every lag L (circular), by FFT. The
    event-triggered average at lag L is X(L) / n; with the events shifted by k it is X(L + k) / n."""
    n = len(rate_ms)
    ev = np.zeros(n)
    np.add.at(ev, events_ms, 1.0)
    x = np.fft.irfft(np.conj(np.fft.rfft(ev)) * np.fft.rfft(rate_ms), n)
    return x


'''
s=s[:i]+new2+s[j:]
open(p,'w').write(s)
EOF
grep -n "^def " gpivla.py
```

```
79:def area(label) -> str:
85:def file_key(session_id: str) -> str:
90:def asset_urls(pre_only: bool = True) -> list[tuple[str, str]]:
99:def _s(x):
103:def _open(url: str, tries: int = 4):
113:def load_session(path: str, url: str) -> dict:
162:def load_all(paths=None, workers: int = 16) -> list[dict]:
171:def _outliers(x: np.ndarray) -> np.ndarray:
181:def valid_trials(trials: pd.DataFrame) -> pd.DataFrame:
199:def _grid(align: np.ndarray, pad: int = 0) -> np.ndarray:
204:def spike_counts_ms(spikes: np.ndarray, align: np.ndarray, pad: int = 100) -> np.ndarray:
214:def sdf(spikes: np.ndarray, align: np.ndarray, sigma: float = SIGMA_MS) -> np.ndarray:
221:def isi_function(spikes: np.ndarray, align: np.ndarray, sigma: float = SIGMA_MS) -> np.ndarray:
236:def control_fit(func: np.ndarray, cue_idx: int):
245:def detect(func: np.ndarray, median_rt_ms: float, alpha: float = ALPHA, contig: int = CONTIG,
279:def unit_direction(segments: list[tuple[np.ndarray, pd.DataFrame]], target: str) -> dict | None:
316:def response_form(inc: float, dec: float) -> str:
329:def _in_windows(t: np.ndarray, windows: np.ndarray) -> np.ndarray:
336:def _bins(gpi: np.ndarray, vla: np.ndarray, reach: float = 0.0215):
348:def _lag_counts(d: np.ndarray) -> np.ndarray:
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > t1.py <<'EOF'
import sys,time,numpy as np
sys.path.insert(0,'entries/000947-schwab-2020')
import gpivla as g
rng=np.random.default_rng(0)
T=1000
gp=np.sort(rng.random(70*T)*T); vl=np.sort(rng.random(15*T)*T)
t=time.time(); r=g.ccf_test(gp,vl,T,rng,400); print('time',time.time()-t, r['peak'], r['thr95'], r['significant'])
sig=0
for k in range(40):
    gp=np.sort(rng.random(70*200)*200); vl=np.sort(rng.random(15*200)*200)
    sig+=g.ccf_test(gp,vl,200,rng,200)['significant']
print('false pos', sig/40)
# inhibition: delete VLa spikes within 1-4 ms after GPi spikes with prob .5
gp=np.sort(rng.random(70*T)*T); vl=np.sort(rng.random(15*T)*T)
idx=np.searchsorted(gp,vl)-1; dt=vl-gp[np.maximum(idx,0)]
vl2=vl[~((dt>0.001)&(dt<0.004)&(rng.random(len(vl))<0.5))]
r=g.ccf_test(gp,vl2,T,rng,200); print('inhib', r['peak'], r['sign'], r['thr95'], r['significant'])
# bursts
sp=np.sort(rng.random(70*100)*100); b=[50+np.arange(8)*0.002]; sp2=np.sort(np.r_[sp,b[0]])
t=time.time(); bb=g.bursts(sp2,70); print('bursts',len(bb), [x for x in bb if 49.9<x[0]<50.1], time.time()-t)
pp=g.pauses(np.r_[sp[sp<30], sp[sp>30.3]],70); print('pauses', pp)
x=g.event_sums(np.arange(10.0), np.array([2,5])); print(x[:3], 'expect', [2+5,3+6,4+7])
EOF
venv/bin/python t1.py
```

```
time 0.2478947639465332 0.030052976190475644 0.04780976190476251 False
false pos 0.05
inhib 0.35669160302157654 -1.0 0.04733381849672429 True
bursts 6 [] 0.0186769962310791
pauses [(np.float64(29.99159067474636), np.float64(30.30411670378651))]
[ 7.  9. 11.] expect [7, 9, 11]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python -c "
import sys,numpy as np
sys.path.insert(0,'entries/000947-schwab-2020')
import gpivla as g
rng=np.random.default_rng(1)
sp=np.sort(rng.random(70*100)*100); b=50+np.arange(12)*0.002; sp2=np.sort(np.r_[sp[(sp<49.99)|(sp>50.05)],b])
bb=g.bursts(sp2,70); print(len(bb), [x for x in bb if 49.9<x[0]<50.1])
print(g._poisson_surprise(12,0.022,70))
"
```

```
7 [(np.float64(50.0), np.float64(50.022))]
7.044682773663839
Shell cwd was reset to
```

**Agent**

Helpers pass synthetic checks (CCF false-positive rate 5%, injected inhibition detected, bursts and pauses found). Now writing the notebook.

**Agent calls Bash**

```bash
cd entries/000947-schwab-2020; python3 - <<'EOF'
p='gpivla.py'; s=open(p).read()
s=s.replace('''         "session_start": _s(f["session_start_time"][()]),''','''         "session_start": _s(f["session_start_time"][()]),
         "related_publications": [_s(x) for x in g["related_publications"][:]]
         if "related_publications" in g else [],''')
open(p,'w').write(s)
EOF
grep -n "related_publications" gpivla.py
```

```
121:         "related_publications": [_s(x) for x in g["related_publications"][:]]
122:         if "related_publications" in g else [],
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.py",
 "content": "# %% md\n# Reproducing Schwab et al. (2020) from dandiset 000947\n\n**Paper.** Schwab BC, Kase D, Zimnik A, Rosenbaum R, Codianni MG, Rubin JE, Turner RS (2020). Neural\nactivity during a simple reaching task in macaques is counter to gating and rebound in basal\nganglia-thalamic communication. *PLOS Biology* 18(10): e3000829.\n[doi:10.1371/journal.pbio.3000829](https://doi.org/10.1371/journal.pbio.3000829). The paper is open\naccess and this attempt used its full text.\n\n**Dandiset.** [DANDI:000947](https://dandiarchive.org/dandiset/000947/0.240510.2211), version\n0.240510.2211. The paper predates the dandiset and cites no DANDI version (its data statement points\nto Dryad). 0.240510.2211 is the only published version, so it is pinned; the draft lists the same\n378 files.\n\n**What the dandiset holds.** Single-unit recordings from two monkeys (Gaia, \"NHP G\", and Isis,\n\"NHP I\") in GPi, VL thalamus, motor cortex and other areas, before and after MPTP, with trial\ntables and raw and filtered traces. The paper uses the pre-MPTP GPi and VLa recordings. EMG,\nthe stimulation mapping of Fig 1 and the simulations of Fig 6 are not in the dandiset.\n\n**Outside inputs.** The paper's Dryad deposit (doi:10.5061/dryad.0cfxpnvxm, read here from its\nZenodo mirror, record 4000719) holds the analysis code read for the method and the per-unit result\nfiles `Gaia_Analy.mat` and `Isis_Analy.mat`. Those files name each analysed unit by file, channel\nand sort letter; they are used only by the claim `unit-link` and by variants that use the paper's\nown unit list. Every outcome on the paper's findings is decided on a unit selection made from the\ndandiset alone.\n\n| Claim | Data | Status |\n|---|---|---|\n| unit-link | with inputs | tested |\n| table1-unit-counts | dandiset | tested |\n| table1-rest-rate | dandiset | tested |\n| table1-ap-width | dandiset | tested |\n| hold-period-ramps | dandiset | tested |\n| mvt-responsive-fraction | dandiset | tested |\n| increases-most-common | dandiset | tested |\n| monophasic-more-in-vla | dandiset | tested |\n| integrated-change-positive | dandiset | tested |\n| fig3a-vla-leads-gpi | dandiset | tested |\n| fig3b-gpi-decr-lag-vla-incr | dandiset | tested |\n| fig3c-vla-decr-lead-gpi-incr | dandiset | tested |\n| gating-conflict-fraction | dandiset | tested |\n| directional-units | dandiset | tested |\n| fig4-ccf-rare | dandiset | tested |\n| fig4-noise-corr-rare | dandiset | tested |\n| fig5-vla-decrease-after-gpi-bursts | dandiset | tested |\n| behavior-rt-mt | dandiset | tested |\n| figs3-emg-onset | elsewhere | blocked: methods underspecified |\n| fig1-vla-localization | dandiset | blocked: data missing |\n| fig6-simulation | elsewhere | blocked: other |\n\n# %% code\nimport io\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport requests\nimport scipy.io as sio\nimport statsmodels.api as sm\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\nfrom statsmodels.formula.api import ols\n\nimport gpivla as g\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nall_files = g.asset_urls(pre_only=False)\nsessions = g.load_all()\nprint(f\"{len(all_files)} files in dandiset {g.DANDISET_ID} version {g.DANDISET_VERSION}; \"\n      f\"loaded the {len(sessions)} pre-MPTP files in {time.time() - started:.0f} s\")\n\n# %% md\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\n# %% code sanity\nwith DandiAPIClient() as client:\n    meta = client.get_dandiset(g.DANDISET_ID, g.DANDISET_VERSION).get_raw_metadata()\nsummary = meta[\"assetsSummary\"]\nprint(\"Archive summary: subjects\", summary[\"numberOfSubjects\"], \"| files\", summary[\"numberOfFiles\"],\n      \"| species\", [s[\"name\"] for s in summary[\"species\"]])\nprint(\"Related resources:\", [r.get(\"identifier\") or r.get(\"url\") for r in meta.get(\"relatedResource\", [])])\npaths = pd.DataFrame({\"path\": [p for p, _ in all_files]})\npaths[\"subject\"] = paths.path.str.extract(r\"sub-(\\w+)/\")[0]\npaths[\"condition\"] = np.where(paths.path.str.contains(\"ses-pre-MPTP\"), \"pre-MPTP\", \"post-MPTP\")\nprint(\"\\nFiles by subject and condition:\")\nprint(pd.crosstab(paths.subject, paths.condition).to_string())\n\ninfo = pd.DataFrame([{\n    \"session\": s[\"session_id\"], \"key\": s[\"key\"], \"subject\": s[\"subject\"], \"mptp_attr\": s[\"mptp\"],\n    \"start\": s[\"session_start\"][:10], \"has_trials\": s[\"trials\"] is not None,\n    \"n_trials\": 0 if s[\"trials\"] is None else len(s[\"trials\"]), \"n_units\": len(s[\"units\"]),\n    \"publications\": \";\".join(s[\"related_publications\"]), \"groups\": str(sorted(s[\"groups\"].values()))}\n    for s in sessions])\nprint(\"\\nMPTP status attribute of the pre-MPTP files:\", info.mptp_attr.value_counts().to_dict())\nprint(\"related_publications in the files:\", info.publications.value_counts().to_dict())\nprint(\"Files without a trials table:\", info.session[~info.has_trials].tolist())\nprint(\"Files without curated units:\", int((info.n_units == 0).sum()), \"of\", len(info))\nprint(\"Trials per file: min\", info.n_trials[info.has_trials].min(), \"median\",\n      info.n_trials[info.has_trials].median(), \"max\", info.n_trials.max())\nday = pd.to_datetime(info.session.str.extract(r\"-(\\d{6})-\")[0], format=\"%y%m%d\")\noffset = (pd.to_datetime(info.start) - day).dt.days\nprint(\"session_start_time minus the date in session_id (days):\", offset.value_counts().to_dict())\nprint(\"Electrode group locations (files):\")\nprint(info.groups.value_counts().head(12).to_string())\n\n# %% md\nThe archive summary counts 2 subjects, as the files do (Gaia and Isis). Every pre-MPTP file\ncarries the MPTP status `pre_MPTP`, consistent with its name. The files name the paper only by its\nbioRxiv preprint (doi:10.1101/546598); the post-MPTP files name a different preprint. One\npre-MPTP file has no trials table and no curated units. In every file the\n`session_start_time` is two days after the date in the `session_id`; the paper does not use dates,\nso this does not affect the analysis, but one of the two is wrong or shifted on purpose and the\nfiles do not say which.\n\n# %% code sanity\nrows = []\nfor s in sessions:\n    span = None\n    for u in s[\"units\"]:\n        sp = u[\"spikes\"]\n        rows.append({\"session\": s[\"session_id\"], \"key\": s[\"key\"], \"subject\": s[\"subject\"],\n                     \"unit_name\": u.get(\"unit_name\"), \"label\": u.get(\"location\"),\n                     \"area\": g.area(u.get(\"location\")), \"channel\": pd.to_numeric(u.get(\"channel_ids\"), errors=\"coerce\"),\n                     \"sort\": str(u.get(\"sort_label\")), \"quality\": u.get(\"unit_quality_post_sorting\"),\n                     \"n_spikes\": len(sp), \"first\": sp[0] if len(sp) else np.nan, \"last\": sp[-1] if len(sp) else np.nan,\n                     \"sorted\": u[\"sorted_in_file\"], \"rec_s\": s[\"n_raw\"] / 24414.0625})\nU = pd.DataFrame(rows)\nprint(\"Curated units by subject and location label as written in the files:\")\nprint(pd.crosstab(U.label.fillna(\"(none)\").replace(\"\", \"(empty)\"), U.subject).to_string())\nprint(\"\\nUnits with no channel id:\", int(U.channel.isna().sum()), \"; with an empty location:\", int((U.label.fillna(\"\") == \"\").sum()))\nprint(\"Sort labels:\", U[\"sort\"].value_counts().to_dict())\nprint(\"Quality labels (GPi and VLa):\", U[U.area.isin([\"GPi\", \"VLa\"])].quality.fillna(\"(column absent)\").value_counts().to_dict())\nprint(\"\\nSpike times stored in increasing order in every unit:\", bool(U.sorted.all()))\nprint(\"Spike times within the raw recording (0 to its length):\",\n      bool(((U[\"first\"] >= 0) & (U[\"last\"] <= U.rec_s + 1)).all()))\n# Recordings deposited twice: identical spike trains within or across files.\ndigest = {}\nfor s in sessions:\n    for u in s[\"units\"]:\n        if len(u[\"spikes\"]):\n            digest.setdefault((len(u[\"spikes\"]), round(float(u[\"spikes\"][0]), 6), round(float(u[\"spikes\"][-1]), 6)), []).append(\n                (s[\"session_id\"], u.get(\"unit_name\")))\ndups = {k: v for k, v in digest.items() if len(v) > 1}\nprint(\"Spike trains with the same count, first and last spike in more than one unit:\", len(dups))\nfor k, v in list(dups.items())[:10]:\n    print(\"  \", v)\nsame_name = U.groupby([\"session\", \"unit_name\"]).size()\nprint(\"Unit names used twice within a file:\", int((same_name > 1).sum()))\n\n# %% md\nThe location labels differ in case between files (GPi and GPI, VLa and VLA), so they are compared\nhere ignoring case. In Gaia, 54 thalamic units are labelled only \"Thalamus\", and in Isis 33 units\nhave an empty label and no channel id; the paper's code calls many of these VLa (see `unit-link`),\nbut the dandiset does not say so, and the dandiset rule leaves them out. Sort labels are written as\nletters in some files and as numbers in others, and the quality column is missing from some files\nand holds free text in others. Unit names repeat within some files (a unit on the GPi probe and a\nunit with an empty label share a name). No spike train is stored twice, so no recording is counted\ntwice by identity; a neuron recorded over consecutive files appears once per file (see\n`table1-unit-counts`).\n\n# %% code sanity\nfor s in sessions:\n    s[\"vt\"] = None if s[\"trials\"] is None else g.valid_trials(s[\"trials\"])\ntr = pd.concat([s[\"vt\"].assign(session=s[\"session_id\"], subject=s[\"subject\"]) for s in sessions if s[\"vt\"] is not None])\nprint(\"Trial table columns (files):\")\nprint(pd.Series([tuple(s[\"trials\"].columns) for s in sessions if s[\"trials\"] is not None]).value_counts().to_string())\nprint(\"\\nTrials by subject: total, errors, outliers, valid\")\nprint(tr.groupby(\"subject\").agg(total=(\"valid\", \"size\"), errors=(\"error\", \"sum\"),\n                                outliers=(\"outlier\", \"sum\"), valid=(\"valid\", \"sum\")).to_string())\nprint(\"Targets:\", tr.target.value_counts().to_dict())\nv = tr[tr.valid]\nprint(\"Reaction time of valid trials (s): min %.3f median %.3f max %.3f\" % (v.rt.min(), v.rt.median(), v.rt.max()))\nprint(\"Movement duration of valid trials (s): min %.3f median %.3f max %.3f; trials without one: %d of %d\"\n      % (v.mt.min(), v.mt.median(), v.mt.max(), v.mt.isna().sum(), len(v)))\norder_ok = (tr.cue_onset_time <= tr.movement_start_time) | ~tr.valid\nprint(\"Valid trials with cue onset before movement onset:\", bool(order_ok.all()))\nprint(\"Files with movement ends, by subject:\",\n      {k: int(x) for k, x in pd.Series({s[\"session_id\"]: (\"movement_stop_time\" in s[\"trials\"]) for s in sessions if s[\"trials\"] is not None}).groupby(lambda k: k.split(\"-\")[2]).sum().items()})\n\n# %% md\nTimes are in seconds, and reaction times and movement durations of valid trials fall in the range\nthe task allows (the animal had 1 s to reach). The paper's reaction times (S2 Fig) are around\n0.2 to 0.3 s, as here. Error trials are flagged only in files that have an `error_onset_time`\ncolumn; in the other files no trial is marked as an error, so error trials there, if any, cannot\nbe excluded. Movement ends are missing from many files, so movement durations are available for\npart of the data only.\n\n# %% md\n**Clock check.** With spikes and a trial table only, the check is whether the trial labels carry\ninformation in the spikes at the time of movement but not before the cue, when the animal does not\nknow the target. For each unit with at least 10 valid trials per direction, left and right spike\ncounts are compared (rank sum) in the movement window (-200 to +300 ms) and in a window before the\ncue (-1500 to -1000 ms from movement onset); a contrast that a constant offset between the clocks\nwould not produce. The same is repeated with the labels shifted by one trial.\n\n# %% code sanity\ndef window_counts(spikes, align, lo, hi):\n    a = np.searchsorted(spikes, align + lo)\n    b = np.searchsorted(spikes, align + hi)\n    return b - a\n\nrows = []\nfor s in sessions:\n    if s[\"vt\"] is None:\n        continue\n    t = s[\"vt\"][s[\"vt\"].valid]\n    left = (t.target == \"Left\").to_numpy()\n    shifted = np.roll(left, 1)\n    al = t.movement_start_time.to_numpy()\n    for u in s[\"units\"]:\n        if g.area(u.get(\"location\")) not in (\"GPi\", \"VLa\") or left.sum() < 10 or (~left).sum() < 10:\n            continue\n        r = {\"session\": s[\"session_id\"], \"subject\": s[\"subject\"], \"area\": g.area(u.get(\"location\"))}\n        for name, (lo, hi) in {\"movement\": (-0.2, 0.3), \"pre_cue\": (-1.5, -1.0)}.items():\n            c = window_counts(u[\"spikes\"], al, lo, hi)\n            for lab, mask in ((\"true\", left), (\"shifted\", shifted)):\n                r[f\"{name}_{lab}\"] = stats.mannwhitneyu(c[mask], c[~mask]).pvalue if c.std() > 0 else 1.0\n        rows.append(r)\nclock = pd.DataFrame(rows)\nfrac = clock.groupby(\"area\")[[c for c in clock.columns if c.endswith((\"true\", \"shifted\"))]].agg(lambda p: (p < 0.05).mean())\nprint(\"Fraction of units whose spike counts differ between left and right trials (p < 0.05):\")\nprint(frac.round(3).to_string())\nper_session = clock.groupby(\"session\").movement_true.apply(lambda p: (p < 0.05).any())\nprint(f\"\\nFiles with at least one direction-tuned unit in the movement window: {per_session.sum()} of {len(per_session)}\")\nprint(\"Files where none is tuned (the clock cannot be checked this way):\", sorted(per_session[~per_session].index))\n\n# %% md\nWith the true labels, many more units differ between left and right trials in the movement window\nthan before the cue, where the fraction is near the 5% expected by chance; with labels shifted by\none trial, the movement window falls to chance too. This supports that the spike times and the\ntrial table share a clock. Files with no tuned unit are listed; for them the shared clock is\nassumed, not shown.\n\n# %% md\n## Unit selection and peri-movement responses\n\nThe dandiset rule (fixed in the claims file): curated units labelled GPi or VLa (ignoring case) in\npre-MPTP files; a unit-direction is analysed with at least 10 valid trials; a unit is kept when its\nmean rate is at least 30 spikes/s (GPi) or 1 spike/s (VLa) and at least one direction is analysed.\nEach file's unit is one unit. For every unit-direction the helper computes the SDF and ISI\nfunctions, detects increases and decreases, and records the rest rate, the integrated change and\nthe control-period slope.\n\n# %% code\nstarted = time.time()\ndef run_units(records):\n    \"\"\"records: list of dicts with unit id, area, subject and segments [(spikes, valid trials)].\"\"\"\n    out = []\n    for r in records:\n        for target in (\"Left\", \"Right\"):\n            d = g.unit_direction(r[\"segments\"], target)\n            if d is None:\n                continue\n            out.append({\"uid\": r[\"uid\"], \"area\": r[\"area\"], \"subject\": r[\"subject\"], \"target\": target,\n                        **{k: d[k] for k in (\"n_trials\", \"median_rt_ms\", \"rest_rate\", \"integrated\", \"inc_onset\",\n                                             \"dec_onset\", \"slope_per_s2\", \"slope_sig\")},\n                        \"sdf\": d[\"sdf\"], \"counts\": d[\"trial_counts\"]})\n    df = pd.DataFrame(out)\n    df[\"form\"] = [g.response_form(i, d) for i, d in zip(df.inc_onset, df.dec_onset)]\n    return df\n\ndand_records, dropped = [], {\"rate\": 0, \"trials\": 0}\nfor s in sessions:\n    if s[\"vt\"] is None:\n        continue\n    for k, u in enumerate(s[\"units\"]):\n        a = g.area(u.get(\"location\"))\n        if a not in (\"GPi\", \"VLa\") or len(u[\"spikes\"]) < 2:\n            continue\n        rate = len(u[\"spikes\"]) / (u[\"spikes\"][-1] - u[\"spikes\"][0])\n        if rate < g.MIN_RATE[a]:\n            dropped[\"rate\"] += 1\n            continue\n        dand_records.append({\"uid\": f\"{s['session_id']}/{k}\", \"area\": a, \"subject\": s[\"subject\"], \"session\": s[\"session_id\"],\n                             \"key\": s[\"key\"], \"channel\": pd.to_numeric(u.get(\"channel_ids\"), errors=\"coerce\"),\n                             \"sort\": str(u.get(\"sort_label\")), \"rate\": rate, \"segments\": [(u[\"spikes\"], s[\"vt\"])],\n                             \"unit\": u, \"sess\": s})\nud = run_units(dand_records)\nkept = set(ud.uid)\ndropped[\"trials\"] = sum(r[\"uid\"] not in kept for r in dand_records)\nunits = pd.DataFrame([{k: r[k] for k in (\"uid\", \"area\", \"subject\", \"session\", \"key\", \"channel\", \"sort\", \"rate\")}\n                      for r in dand_records if r[\"uid\"] in kept])\nprint(f\"Dandiset rule: {len(units)} units, {len(ud)} unit-directions ({time.time() - started:.0f} s)\")\nprint(\"Left out: below the rate criterion\", dropped[\"rate\"], \"; fewer than 10 valid trials in both directions\", dropped[\"trials\"])\nprint(units.groupby([\"area\", \"subject\"]).size().unstack().to_string())\n\n# %% md\nThe paper's unit list, for the variants: the records the paper's code keeps (`Fig2_3_S8_S9.m`\ndrops VLp units and records with missing SDFs) are matched to the curated units by file, channel id\nand sort letter; a record that spans several files pools the trials of all of them, as the paper's\nrecords do. Records not found in every file they span are left out of the variants.\n\n# %% code\nstarted = time.time()\nZENODO = \"https://zenodo.org/records/4000719/files/{}?download=1\"\nanaly = {}\nfor monk in (\"Gaia\", \"Isis\"):\n    r = requests.get(ZENODO.format(f\"{monk}_Analy.mat\"), timeout=600)\n    r.raise_for_status()\n    m = sio.loadmat(io.BytesIO(r.content), squeeze_me=True, struct_as_record=False)\n    analy[monk] = (m[\"RespSDFIncr\"], m[\"RespISIIncr\"])\n\ndef sort_letter(x):\n    return {\"1.0\": \"a\", \"2.0\": \"b\", \"3.0\": \"c\", \"4.0\": \"d\"}.get(str(x), str(x))\n\nby_key = {s[\"key\"]: s for s in sessions}\npaper_rows, paper_records = [], []\nfor monk, (A, B) in analy.items():\n    for i in range(len(A.fname)):\n        utype = str(A.unit_type[i])\n        files = str(A.fname[i]).split(\"/\")\n        keep = utype != \"VLp\" and not np.isnan(A.evt_sdf[i, :, 0]).any()\n        found = []\n        for f in files:\n            s = by_key.get(f)\n            hits = [] if s is None else [u for u in s[\"units\"]\n                    if pd.to_numeric(u.get(\"channel_ids\"), errors=\"coerce\") == float(A.Uchan[i])\n                    and sort_letter(u.get(\"sort_label\")) == A.Usort[i]]\n            found.append((s, hits[0]) if len(hits) == 1 else None)\n        complete = all(x is not None for x in found)\n        paper_rows.append({\"monk\": monk, \"i\": i, \"fname\": str(A.fname[i]), \"area\": utype, \"keep\": keep,\n                           \"n_files\": len(files), \"n_found\": sum(x is not None for x in found), \"complete\": complete,\n                           \"labels\": sorted({g.area(x[1].get(\"location\")) or \"(empty)\" for x in found if x})})\n        if keep and complete:\n            paper_records.append({\"uid\": f\"paper/{monk}/{i}\", \"area\": utype, \"subject\": monk, \"monk\": monk, \"i\": i,\n                                  \"segments\": [(u[\"spikes\"], s[\"vt\"]) for s, u in found]})\npaper = pd.DataFrame(paper_rows)\nud_paper = run_units(paper_records)\nprint(f\"Paper's records: {len(paper)}; kept by its code: {int(paper.keep.sum())}; found in every file: \"\n      f\"{int((paper.keep & paper.complete).sum())}; unit-directions analysed: {len(ud_paper)} ({time.time() - started:.0f} s)\")\n\n# %% md\n## unit-link\n\n> The units the paper analysed can be found in the dandiset, and the dandiset's spike times and\n> trials reproduce the per-unit peri-movement activity the paper's code stored.\n\n# %% code claim:unit-link\nk = paper[paper.keep]\nprint(\"Records kept by the paper's code, by animal and area:\")\nprint(k.groupby([\"monk\", \"area\"]).size().unstack().to_string())\nprint(\"\\nFound in every file they span:\")\nprint(k.groupby([\"monk\", \"area\"]).complete.agg([\"sum\", \"size\", \"mean\"]).round(3).to_string())\nprint(f\"Overall: {int(k.complete.sum())} of {len(k)} ({k.complete.mean():.1%}); records spanning 2 to 5 files: {int((k.n_files > 1).sum())}\")\nmissing = k[~k.complete]\nprint(\"\\nRecords not found, by file:\")\nprint(missing.groupby(\"fname\").size().to_string())\nprint(\"\\nDandiset labels of the matched records, by the paper's area:\")\nprint(pd.crosstab(k[k.complete].area, k[k.complete].labels.map(lambda l: \"/\".join(l))).to_string())\n\nrows = []\nfor _, r in ud_paper.iterrows():\n    monk, i = r.uid.split(\"/\")[1], int(r.uid.split(\"/\")[2])\n    A, B = analy[monk]\n    t = 0 if r.target == \"Left\" else 1\n    ref = A.evt_sdf[i, t, :]\n    rows.append({\"area\": r.area, \"r\": np.corrcoef(r.sdf, ref)[0, 1], \"mean_ratio\": r.sdf.mean() / ref.mean(),\n                 \"n\": r.n_trials, \"n_ref\": np.shape(A.evt_spkt[i, t])[0],\n                 \"inc\": r.inc_onset, \"inc_ref\": A.on_ind[i, t] - 1500, \"dec\": r.dec_onset, \"dec_ref\": B.on_ind[i, t] - 1500})\ncmp_ = pd.DataFrame(rows)\nprint(f\"\\nUnit-directions compared: {len(cmp_)}\")\nprint(f\"SDF correlation with the stored SDF: median {cmp_.r.median():.4f}; r > 0.9 for {(cmp_.r > 0.9).mean():.1%}; \"\n      f\"r > 0.99 for {(cmp_.r > 0.99).mean():.1%}; mean rate ratio median {cmp_.mean_ratio.median():.4f}\")\nprint(f\"Valid trial counts equal to the paper's: {(cmp_.n == cmp_.n_ref).mean():.1%}; \"\n      f\"median absolute difference {np.median(np.abs(cmp_.n - cmp_.n_ref)):.0f}, max {np.max(np.abs(cmp_.n - cmp_.n_ref)):.0f}\")\nfor kind in (\"inc\", \"dec\"):\n    a, b = cmp_[kind].notna(), cmp_[kind + \"_ref\"].notna()\n    both = a & b\n    print(f\"{kind}reases: detected here {a.sum()}, by the paper {b.sum()}, agreement on presence {(a == b).mean():.1%}; \"\n          f\"onset difference where both, median absolute {np.median(np.abs(cmp_[kind][both] - cmp_[kind + '_ref'][both])):.0f} ms\")\n\n# %% md\n## table1-unit-counts\n\n> 209 single units met the criteria to be included as GPi neurons (105 in NHP G, 104 in NHP I)\n> and 185 as VLa neurons (66 and 119).\n\n# %% code claim:table1-unit-counts\ncounts = units.groupby([\"area\", \"subject\"]).size().unstack()\ncounts[\"total\"] = counts.sum(1)\nprint(\"Dandiset rule (one unit per file):\")\nprint(counts.to_string())\nfor a, ref in ((\"GPi\", [209]), (\"VLa\", [185, 218])):\n    n = int(counts.loc[a, \"total\"])\n    print(f\"{a}: {n}; paper {ref}; within 10%: {[abs(n - x) <= 0.1 * x for x in ref]}\")\nday = units.session.str.extract(r\"-(\\d{6})-\")[0]\ndistinct = units.assign(day=day).dropna(subset=[\"channel\"]).drop_duplicates([\"subject\", \"day\", \"area\", \"channel\", \"sort\"])\nprint(\"\\nVariant, units with the same channel and sort letter on the same day taken as one neuron (an assumption):\")\nprint(distinct.groupby([\"area\", \"subject\"]).size().unstack().assign(total=lambda d: d.sum(1)).to_string())\nprint(\"\\nVariant, the paper's records found in the dandiset:\")\nprint(paper[paper.keep & paper.complete].groupby([\"area\", \"monk\"]).size().unstack().assign(total=lambda d: d.sum(1)).to_string())\nin_paper_file = units.key.isin({f for x in paper.fname for f in x.split(\"/\")})\nprint(f\"\\nDandiset-rule units in files the paper used: {int(in_paper_file.sum())} of {len(units)}\")\n\n# %% md\n## table1-rest-rate\n\n> The resting firing rate of GPi neurons (mean 70.1 spikes/s) is significantly higher than that of\n> VLa neurons (13.5 spikes/s), and the rates are consistent between the two animals.\n\n# %% code claim:table1-rest-rate\ndef rest_table(df):\n    t = df.groupby([\"area\", \"subject\"]).rest_rate.agg([\"mean\", \"std\", \"size\"])\n    t2 = df.groupby(\"area\").rest_rate.agg([\"mean\", \"std\", \"size\"]).assign(subject=\"all\").set_index(\"subject\", append=True)\n    return pd.concat([t, t2]).sort_index()\n\nprint(\"Rest rate (spikes/s), mean SDF from -1500 to -301 ms, over unit-directions. Dandiset rule:\")\nprint(rest_table(ud).round(2).to_string())\ngp, vl = ud[ud.area == \"GPi\"].rest_rate, ud[ud.area == \"VLa\"].rest_rate\nres = stats.ranksums(gp, vl)\nprint(f\"GPi {gp.mean():.2f} against VLa {vl.mean():.2f}; rank sum z = {res.statistic:.2f}, p = {res.pvalue:.2g}\")\nfor a in (\"GPi\", \"VLa\"):\n    x = ud[ud.area == a]\n    p = stats.ranksums(x[x.subject == \"Gaia\"].rest_rate, x[x.subject == \"Isis\"].rest_rate).pvalue\n    print(f\"{a}: Gaia against Isis, rank sum p = {p:.3g}\")\nprint(\"\\nRange of rest rates (spikes/s):\", ud.groupby(\"area\").rest_rate.agg([\"min\", \"max\"]).round(1).to_dict(\"index\"))\nprint(\"\\nVariant, the paper's records:\")\nprint(rest_table(ud_paper).round(2).to_string())\nprint(f\"rank sum p = {stats.ranksums(ud_paper[ud_paper.area == 'GPi'].rest_rate, ud_paper[ud_paper.area == 'VLa'].rest_rate).pvalue:.2g}\")\n\n# %% md\n## table1-ap-width\n\n> Action potentials of GPi neurons are shorter than those of VLa neurons (trough to peak 0.24\n> against 0.50 ms; rank sum p = 1e-33).\n\n# %% code claim:table1-ap-width\nfrom concurrent.futures import ThreadPoolExecutor\nstarted = time.time()\njobs = []\nfor r in dand_records:\n    if r[\"uid\"] not in kept or np.isnan(r[\"channel\"]):\n        continue\n    s = r[\"sess\"]\n    el = s[\"electrodes\"]\n    rows_ = np.flatnonzero(pd.to_numeric(el.channel_ids, errors=\"coerce\").to_numpy() == r[\"channel\"])\n    for name, p in s[\"processed\"].items():\n        cols = np.flatnonzero(np.isin(p[\"electrodes\"], rows_))\n        if len(cols) == 1:\n            jobs.append((r[\"uid\"], r[\"area\"], r[\"subject\"], s[\"url\"], name, int(cols[0]), r[\"segments\"][0][0], p))\n            break\n\ndef width_job(j):\n    uid, a, subj, url, name, col, spikes, p = j\n    w, n = g.ap_width(url, name, col, spikes, p[\"rate\"], p[\"start\"], p[\"chunks\"][0])\n    return {\"uid\": uid, \"area\": a, \"subject\": subj, \"width_ms\": w, \"n_spikes\": n}\n\nwith ThreadPoolExecutor(16) as ex:\n    widths = pd.DataFrame(list(ex.map(width_job, jobs)))\nprint(f\"Units with a channel in a filtered series: {len(jobs)} of {len(units)}; widths measured: \"\n      f\"{int(widths.width_ms.notna().sum())} ({time.time() - started:.0f} s)\")\nprint(widths.groupby([\"area\", \"subject\"]).width_ms.agg([\"mean\", \"std\", \"median\", \"size\"]).round(3).to_string())\nprint(widths.groupby(\"area\").width_ms.agg([\"mean\", \"std\", \"median\", \"min\", \"max\", \"size\"]).round(3).to_string())\nw_gp, w_vl = widths[widths.area == \"GPi\"].width_ms.dropna(), widths[widths.area == \"VLa\"].width_ms.dropna()\nres = stats.ranksums(w_gp, w_vl)\nprint(f\"GPi {w_gp.mean():.3f} ms against VLa {w_vl.mean():.3f} ms; rank sum z = {res.statistic:.2f}, p = {res.pvalue:.2g}\")\nprint(\"Sampling interval of the trace: %.4f ms\" % (1000 / list(sessions[0][\"processed\"].values())[0][\"rate\"]))\nfig, ax = plt.subplots(figsize=(5, 3))\nax.hist([w_gp, w_vl], bins=np.arange(0, 1.2, 0.041), label=[\"GPi\", \"VLa\"])\nax.set_xlabel(\"trough to peak (ms)\"); ax.set_ylabel(\"units\"); ax.legend()\nprint(\"Units outside the axes (above 1.2 ms):\", int((widths.width_ms > 1.2).sum()))\n\n# %% md\n## hold-period-ramps\n\n> The firing rate of most units ramps during the start-position hold period (97% of GPi and 98% of\n> VLa units with a significant linear trend); slopes are distributed symmetrically around zero,\n> without a difference between GPi and VLa.\n\n# %% code claim:hold-period-ramps\ndef ramps(df):\n    per_unit = df.groupby([\"uid\", \"area\"]).slope_sig.any().groupby(\"area\").agg([\"mean\", \"sum\", \"size\"])\n    return per_unit\n\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    t = ramps(df)\n    print(name, \"- units with a significant control-period slope in at least one direction:\")\n    print(t.assign(percent=lambda d: (100 * d[\"mean\"]).round(1)).to_string())\n    gs, vs = df[df.area == \"GPi\"].slope_per_s2, df[df.area == \"VLa\"].slope_per_s2\n    print(f\"  mean slope (spikes/s2) GPi {gs.mean():.3f}, VLa {vs.mean():.3f}; medians {gs.median():.3f}, {vs.median():.3f}; \"\n          f\"rank sum p = {stats.ranksums(gs, vs).pvalue:.3g}\")\n    sig = df[df.slope_sig]\n    print(f\"  significant unit-direction slopes positive: {(sig.slope_per_s2 > 0).mean():.1%} of {len(sig)}\")\nprint(\"By animal (dandiset rule):\")\nprint(ud.groupby([\"uid\", \"area\", \"subject\"]).slope_sig.any().groupby([\"area\", \"subject\"]).mean().round(3).to_string())\nprint(\"Variant, significance at alpha 0.01 (99% CI) instead of 0.05:\")\ndef sig01(df):\n    out = []\n    for _, r in df.iterrows():\n        cue = int(round(1500 - r.median_rt_ms))\n        x = np.arange(cue - 700, cue)\n        lr = stats.linregress(x, r.sdf[x])\n        out.append(lr.pvalue < 0.01)\n    return pd.Series(out, index=df.index)\nud[\"slope_sig01\"] = sig01(ud)\nprint(ud.groupby([\"uid\", \"area\"]).slope_sig01.any().groupby(\"area\").mean().round(3).to_string())\n\n# %% md\n## mvt-responsive-fraction\n\n> Nearly all units change their discharge around movement for at least one direction (GPi 99%;\n> VLa 88.1% in Table 1, 94% in the text).\n\n# %% code claim:mvt-responsive-fraction\ndef responsive(df):\n    return df.assign(resp=df.form != \"none\").groupby([\"uid\", \"area\", \"subject\"]).resp.any()\n\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    r = responsive(df)\n    t = r.groupby(\"area\").agg([\"sum\", \"size\", \"mean\"])\n    print(name); print(t.assign(percent=lambda d: (100 * d[\"mean\"]).round(1)).to_string())\n    print(r.groupby([\"area\", \"subject\"]).mean().round(3).to_string())\nprint(\"\\nUnit-directions with a response (dandiset rule):\", (ud.form != \"none\").groupby(ud.area).agg([\"sum\", \"size\"]).to_dict(\"index\"))\nprint(\"Variant, alpha 0.0001 instead of 0.001 (stricter):\")\nstrict = []\nfor _, r in ud.iterrows():\n    f_ = g.detect(r.sdf, r.median_rt_ms, alpha=0.0001)\n    strict.append(np.isfinite(f_[\"onset\"]))\nprint(\"  units with an increase in at least one direction:\", ud.assign(s=strict).groupby([\"uid\", \"area\"]).s.any().groupby(\"area\").mean().round(3).to_dict())\n\n# %% md\n## increases-most-common\n\n> Monophasic increases are the most common form of response in both GPi and VLa (48.7% and 65.3%\n> of responses), and increases make up most detected changes (61.5% and 68.8%, biphasic responses\n> counted twice), more than decreases.\n\n# %% code claim:increases-most-common\nFORMS = [\"increase\", \"decrease\", \"inc_first\", \"dec_first\"]\ndef forms_table(df):\n    r = df[df.form != \"none\"]\n    t = pd.crosstab(r.area, r.form)[FORMS]\n    pct = (100 * t.div(t.sum(1), axis=0)).round(1)\n    inc = t.increase + t.inc_first + t.dec_first\n    changes = t.increase + t.decrease + 2 * (t.inc_first + t.dec_first)\n    return t, pct, inc, changes\n\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    t, pct, inc, changes = forms_table(df)\n    print(name, \"- responses by form (unit-directions):\"); print(t.to_string()); print(\"percent:\"); print(pct.to_string())\n    for a in t.index:\n        print(f\"  {a}: increases {inc[a]} of {changes[a]} changes ({100 * inc[a] / changes[a]:.1f}%)\")\n    chi = stats.chi2_contingency(np.array([[inc[a], changes[a] - inc[a]] for a in t.index]))\n    allinc, allchg = inc.sum(), changes.sum()\n    print(f\"  increases against decreases over both areas: {allinc} of {allchg}, binomial p = {stats.binomtest(int(allinc), int(allchg)).pvalue:.2g}; \"\n          f\"GPi against VLa chi-squared p = {chi.pvalue:.3g}\")\nprint(\"By animal (dandiset rule), percent monophasic increases:\")\nr = ud[ud.form != \"none\"]\nprint((100 * pd.crosstab([r.area, r.subject], r.form, normalize=\"index\")).round(1)[FORMS].to_string())\n\n# %% md\n## monophasic-more-in-vla\n\n> Monophasic changes are more common in VLa than in GPi (88.9% against 66.7% of responses), and\n> polyphasic responses more common in GPi.\n\n# %% code claim:monophasic-more-in-vla\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    r = df[df.form != \"none\"]\n    mono = r.form.isin([\"increase\", \"decrease\"])\n    t = pd.crosstab(r.area, mono)\n    chi = stats.chi2_contingency(t.to_numpy())\n    print(name); print((100 * mono.groupby(r.area).mean()).round(1).to_string())\n    print(f\"  counts (polyphasic, monophasic): {t.to_dict('index')}; chi-squared p = {chi.pvalue:.2g}\")\nr = ud[ud.form != \"none\"]\nprint(\"By animal (dandiset rule):\", (100 * r.form.isin([\"increase\", \"decrease\"]).groupby([r.area, r.subject]).mean()).round(1).to_dict())\n\n# %% md\n## integrated-change-positive\n\n> The mean integrated change in firing over the peri-movement epoch is positive in both GPi and VLa\n> (3.89 and 1.75 spikes), significantly different from zero.\n\n# %% code claim:integrated-change-positive\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    print(name)\n    for a in (\"GPi\", \"VLa\"):\n        x = df[df.area == a].integrated\n        w = stats.wilcoxon(x)\n        print(f\"  {a}: mean {x.mean():.2f} spikes (SD {x.std():.2f}), median {x.median():.2f}, n {len(x)}; signed rank p = {w.pvalue:.2g}; \"\n              f\"range {x.min():.1f} to {x.max():.1f}\")\n    print(\"  by animal:\", df.groupby([\"area\", \"subject\"]).integrated.mean().round(2).to_dict())\n\n# %% md\n## fig3a-vla-leads-gpi\n\n> Peri-movement changes begin later in GPi than in VLa (median onsets -47 and -90 ms).\n\n# %% code claim:fig3a-vla-leads-gpi\ndef onsets(df, area, kind):\n    col = {\"inc\": \"inc_onset\", \"dec\": \"dec_onset\"}\n    if kind == \"all\":\n        return pd.concat([df[df.area == area].inc_onset, df[df.area == area].dec_onset]).dropna()\n    return df[df.area == area][col[kind]].dropna()\n\ndef compare(df, a1, k1, a2, k2, label):\n    x, y = onsets(df, a1, k1), onsets(df, a2, k2)\n    res = stats.ranksums(x, y)\n    print(f\"  {label}: {a1} {k1} median {x.median():.1f} ms (n {len(x)}), {a2} {k2} median {y.median():.1f} ms (n {len(y)}); \"\n          f\"difference {x.median() - y.median():.1f} ms; rank sum z = {res.statistic:.2f}, p = {res.pvalue:.2g}\")\n    return x, y\n\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    print(name)\n    x, y = compare(df, \"GPi\", \"all\", \"VLa\", \"all\", \"all changes\")\nfor subj in (\"Gaia\", \"Isis\"):\n    print(\"Dandiset rule,\", subj)\n    compare(ud[ud.subject == subj], \"GPi\", \"all\", \"VLa\", \"all\", \"all changes\")\nx, y = onsets(ud, \"GPi\", \"all\"), onsets(ud, \"VLa\", \"all\")\nfig, ax = plt.subplots(figsize=(5, 3))\nfor v, lab in ((x, \"GPi\"), (y, \"VLa\")):\n    ax.step(np.sort(v), np.arange(1, len(v) + 1) / len(v), label=lab)\nax.set_xlabel(\"onset from movement onset (ms)\"); ax.set_ylabel(\"cumulative fraction\"); ax.legend()\nprint(\"Onset range (ms):\", int(min(x.min(), y.min())), \"to\", int(max(x.max(), y.max())), \"; all inside the axes\")\n\n# %% md\n## fig3b-gpi-decr-lag-vla-incr\n\n> GPi decreases lag behind VLa increases (median onsets -27 and -88 ms).\n\n# %% code claim:fig3b-gpi-decr-lag-vla-incr\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    print(name)\n    compare(df, \"GPi\", \"dec\", \"VLa\", \"inc\", \"GPi decreases against VLa increases\")\nfor subj in (\"Gaia\", \"Isis\"):\n    print(\"Dandiset rule,\", subj)\n    compare(ud[ud.subject == subj], \"GPi\", \"dec\", \"VLa\", \"inc\", \"GPi decreases against VLa increases\")\n\n# %% md\n## fig3c-vla-decr-lead-gpi-incr\n\n> VLa decreases precede GPi increases (median onsets -108 and -62 ms).\n\n# %% code claim:fig3c-vla-decr-lead-gpi-incr\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    print(name)\n    compare(df, \"GPi\", \"inc\", \"VLa\", \"dec\", \"GPi increases against VLa decreases\")\nfor subj in (\"Gaia\", \"Isis\"):\n    print(\"Dandiset rule,\", subj)\n    compare(ud[ud.subject == subj], \"GPi\", \"inc\", \"VLa\", \"dec\", \"GPi increases against VLa decreases\")\n\n# %% md\n## gating-conflict-fraction\n\n> Comparing every GPi response with every VLa response, 96% of comparisons conflict with gating;\n> only 4% have a GPi onset 0 to 50 ms before the VLa onset with the opposite sign.\n\n# %% code claim:gating-conflict-fraction\ndef gating(df, lo=0, hi=50):\n    def changes(a):\n        d = df[df.area == a]\n        return np.r_[d.inc_onset.dropna(), d.dec_onset.dropna()], np.r_[np.ones(d.inc_onset.notna().sum()), -np.ones(d.dec_onset.notna().sum())]\n    gt, gs = changes(\"GPi\")\n    vt, vs = changes(\"VLa\")\n    lead = vt[None, :] - gt[:, None]\n    fits = (lead >= lo) & (lead <= hi) & (gs[:, None] != vs[None, :])\n    return fits.size, int(fits.sum())\n\nfor name, df in ((\"Dandiset rule\", ud), (\"Variant, the paper's records\", ud_paper)):\n    n, fit = gating(df)\n    print(f\"{name}: {n} comparisons, {fit} fit gating; conflicting {100 * (1 - fit / n):.1f}%\")\nfor lo, hi in ((0, 20), (0, 100), (0, 200)):\n    n, fit = gating(ud, lo, hi)\n    print(f\"  variant, GPi leading by {lo} to {hi} ms: conflicting {100 * (1 - fit / n):.1f}%\")\nn, fit = gating(ud)\nrng = np.random.default_rng(1)\nd = ud.copy()\nnull = []\nfor _ in range(200):\n    d[\"inc_onset\"] = rng.permutation(ud.inc_onset.to_numpy())\n    d[\"dec_onset\"] = rng.permutation(ud.dec_onset.to_numpy())\n    nn, ff = gating(d)\n    null.append(100 * (1 - ff / nn))\nprint(f\"Reference: onsets shuffled across unit-directions, conflicting {np.mean(null):.1f}% (2.5 to 97.5 percentile {np.percentile(null, 2.5):.1f} to {np.percentile(null, 97.5):.1f})\")\n\n# %% md\n## directional-units\n\n> A majority of GPi neurons (109 of 206) and some VLa neurons (56 of 179) respond significantly more\n> strongly to one movement direction.\n\n# %% code claim:directional-units\ndef directional(df, records):\n    seg = {r[\"uid\"]: r[\"segments\"] for r in records}\n    out = []\n    for uid, d in df[df.form != \"none\"].groupby(\"uid\"):\n        first = np.nanmin(np.r_[d.inc_onset, d.dec_onset]) / 1000.0\n        c = {}\n        for target in (\"Left\", \"Right\"):\n            vals = []\n            for spikes, t in seg[uid]:\n                tt = t[t.valid & (t.target == target)]\n                vals.append(window_counts(spikes, tt.movement_start_time.to_numpy(), first, first + 0.3))\n            c[target] = np.concatenate(vals)\n        p = stats.ranksums(c[\"Left\"], c[\"Right\"]).pvalue if min(len(c[\"Left\"]), len(c[\"Right\"])) else np.nan\n        out.append({\"uid\": uid, \"area\": d.area.iloc[0], \"subject\": d.subject.iloc[0], \"p\": p})\n    return pd.DataFrame(out)\n\nfor name, df, recs in ((\"Dandiset rule\", ud, dand_records), (\"Variant, the paper's records\", ud_paper, paper_records)):\n    dd = directional(df, recs)\n    t = dd.assign(dir=dd.p < 0.005).groupby(\"area\").dir.agg([\"sum\", \"size\", \"mean\"])\n    print(name); print(t.assign(percent=lambda x: (100 * x[\"mean\"]).round(1)).to_string())\n    chi = stats.chi2_contingency(pd.crosstab(dd.area, dd.p < 0.005).to_numpy())\n    print(f\"  GPi against VLa chi-squared p = {chi.pvalue:.2g}\")\n    if name == \"Dandiset rule\":\n        print(\"  by animal:\", dd.assign(dir=dd.p < 0.005).groupby([\"area\", \"subject\"]).dir.mean().round(3).to_dict())\n        print(\"  variant p < 0.05:\", dd.assign(dir=dd.p < 0.05).groupby(\"area\").dir.mean().round(3).to_dict())\n\n# %% md\n## Pairs of simultaneously recorded GPi and VLa units\n\nPairs are the GPi and VLa units of the dandiset rule in the same file. Windows: rest is 1.5 to 1.0 s\nbefore movement onset, movement 0.2 s before to 0.3 s after, in valid trials.\n\n# %% code\npairs = []\nfor s in sessions:\n    us = units[units.session == s[\"session_id\"]]\n    gps, vls = us[us.area == \"GPi\"], us[us.area == \"VLa\"]\n    for _, a in gps.iterrows():\n        for _, b in vls.iterrows():\n            pairs.append({\"session\": s[\"session_id\"], \"subject\": s[\"subject\"], \"gpi\": a.uid, \"vla\": b.uid})\npairs = pd.DataFrame(pairs)\nspk = {r[\"uid\"]: r[\"segments\"][0][0] for r in dand_records}\nsess_of = {s[\"session_id\"]: s for s in sessions}\nprint(f\"GPi-VLa pairs in the same file: {len(pairs)} in {pairs.session.nunique()} files\")\nprint(pairs.groupby(\"subject\").size().to_string())\n\n# %% md\n## fig4-ccf-rare\n\n> Short-time-scale spike-to-spike correlations between simultaneously recorded GPi and VLa units are\n> rare (3.5% of 427 pairs over whole recordings, 2.2% of 183 at rest, 5.2% of 172 during movement)\n> and their peaks are not larger than those of jittered controls.\n\n# %% code claim:fig4-ccf-rare\nstarted = time.time()\nrng = np.random.default_rng(4)\nN_SURR = 400\nccf_rows, ctrl_peaks = [], {\"whole\": [], \"rest\": [], \"movement\": []}\nfor _, p in pairs.iterrows():\n    s = sess_of[p.session]\n    a, b = spk[p.gpi], spk[p.vla]\n    t = s[\"vt\"][s[\"vt\"].valid]\n    periods = {\"whole\": None,\n               \"rest\": np.c_[t.movement_start_time + g.REST_WIN[0], t.movement_start_time + g.REST_WIN[1]],\n               \"movement\": np.c_[t.movement_start_time + g.MVT_WIN[0], t.movement_start_time + g.MVT_WIN[1]]}\n    for name, win in periods.items():\n        if win is None:\n            x, y = a, b\n            dur = max(a[-1], b[-1]) - min(a[0], b[0])\n        else:\n            x, y = a[g._in_windows(a, win)], b[g._in_windows(b, win)]\n            dur = float(np.sum(win[:, 1] - win[:, 0]))\n        if min(len(x), len(y)) < 100:\n            continue\n        r = g.ccf_test(x, y, dur, rng, N_SURR)\n        ccf_rows.append({\"period\": name, \"subject\": p.subject, \"peak\": r[\"peak\"], \"sign\": r[\"sign\"],\n                         \"thr95\": r[\"thr95\"], \"significant\": r[\"significant\"]})\n        ctrl_peaks[name].append(r[\"ctrl_peaks\"])\ncc = pd.DataFrame(ccf_rows)\nprint(f\"CCFs computed in {time.time() - started:.0f} s; {N_SURR} jittered controls per pair and period\")\nfor name in (\"whole\", \"rest\", \"movement\"):\n    d = cc[cc.period == name]\n    k, n = int(d.significant.sum()), len(d)\n    pks = ks_p = g.ks_permutation(d.peak.to_numpy(), np.vstack(ctrl_peaks[name]))\n    print(f\"{name}: {n} pairs; significant {k} ({100 * k / n:.1f}%), binomial p against 5% (greater) = \"\n          f\"{stats.binomtest(k, n, 0.05, alternative='greater').pvalue:.3g}; signs of significant peaks \"\n          f\"+{int((d[d.significant].sign > 0).sum())} / -{int((d[d.significant].sign < 0).sum())}; \"\n          f\"KS permutation p = {ks_p:.3f}; median peak {d.peak.median():.3f}, median control 95th percentile {d.thr95.median():.3f}\")\nprint(\"By animal, percent significant:\", (100 * cc.groupby([\"period\", \"subject\"]).significant.mean()).round(1).to_dict())\n\n# %% md\n## fig4-noise-corr-rare\n\n> Trial-to-trial noise correlations between GPi and VLa are rare (5.4% of 332 pairs at rest, 7.2% of\n> 372 during movement), not different from shuffled controls, and equally often positive and\n> negative.\n\n# %% code claim:fig4-noise-corr-rare\nrng = np.random.default_rng(5)\nnc_rows, nc_ctrl = [], {\"rest\": [], \"movement\": []}\nfor _, p in pairs.iterrows():\n    s = sess_of[p.session]\n    for target in (\"Left\", \"Right\"):\n        t = s[\"vt\"][s[\"vt\"].valid & (s[\"vt\"].target == target)]\n        al = t.movement_start_time.to_numpy()\n        for name, (lo, hi) in ((\"rest\", g.REST_WIN), (\"movement\", g.MVT_WIN)):\n            ca = window_counts(spk[p.gpi], al, lo, hi).astype(float)\n            cb = window_counts(spk[p.vla], al, lo, hi).astype(float)\n            if ca.sum() < 10 or cb.sum() < 10 or len(al) < 10 or ca.std() == 0 or cb.std() == 0:\n                continue\n            za, zb = stats.zscore(ca), stats.zscore(cb)\n            ok = (np.abs(za) <= 3) & (np.abs(zb) <= 3)\n            ca, cb = ca[ok], cb[ok]\n            if ca.std() == 0 or cb.std() == 0:\n                continue\n            r = np.corrcoef(ca, cb)[0, 1]\n            sh = np.array([np.corrcoef(ca, rng.permutation(cb))[0, 1] for _ in range(400)])\n            nc_rows.append({\"period\": name, \"pair\": f\"{p.gpi}|{p.vla}\", \"subject\": p.subject, \"target\": target, \"r\": r})\n            nc_ctrl[name].append(sh)\nnc = pd.DataFrame(nc_rows)\nfor name in (\"rest\", \"movement\"):\n    d = nc[nc.period == name].copy()\n    ctrl = np.vstack(nc_ctrl[name])\n    lo, hi = np.percentile(ctrl, [2.5, 97.5])\n    d[\"sig\"] = (d.r < lo) | (d.r > hi)\n    pos, neg = int((d.r > hi).sum()), int((d.r < lo).sum())\n    ks_p = g.ks_permutation(np.abs(d.r.to_numpy()), np.abs(ctrl))\n    by_pair = d.groupby(\"pair\").sig.any()\n    print(f\"{name}: (a) {len(d)} pair-targets, significant {int(d.sig.sum())} ({100 * d.sig.mean():.1f}%), +{pos} / -{neg} \"\n          f\"(binomial p of the sign balance {stats.binomtest(pos, pos + neg).pvalue:.3g}); \"\n          f\"(b) {len(by_pair)} pairs, significant in either target {int(by_pair.sum())} ({100 * by_pair.mean():.1f}%)\")\n    print(f\"   KS permutation p (absolute correlations against shuffles) = {ks_p:.3f}; median r {d.r.median():.3f}; \"\n          f\"shuffle band {lo:.3f} to {hi:.3f}\")\n\n# %% md\n## fig5-vla-decrease-after-gpi-bursts\n\n> At rest, GPi burst onsets, burst offsets and pause onsets are each followed by a small, slow\n> decrease of the population VLa firing rate.\n\n# %% code claim:fig5-vla-decrease-after-gpi-bursts\nstarted = time.time()\nrng = np.random.default_rng(6)\nLAGS = np.arange(-800, 801)\nta = {\"burst onset\": [], \"burst offset\": [], \"pause onset\": []}\nctrl = {k: [] for k in ta}\npair_sig = {k: [] for k in ta}\nn_excluded = {k: 0 for k in ta}\nn_events = {k: [] for k in ta}\nfor _, p in pairs.iterrows():\n    s = sess_of[p.session]\n    t = s[\"trials\"]\n    end = t[\"return_stop_time\"] if \"return_stop_time\" in t else t[\"stop_time\"]\n    task = np.c_[t.movement_start_time + g.TASK_EXCL[0], end.fillna(t.stop_time) + g.TASK_EXCL[1]]\n    task = task[np.isfinite(task).all(1)]\n    a, b = spk[p.gpi], spk[p.vla]\n    T = int(np.ceil(max(a[-1], b[-1]) * 1000)) + 2000\n    in_task = np.zeros(T, bool)\n    for lo_, hi_ in (task * 1000).astype(int):\n        in_task[max(lo_, 0):min(hi_, T)] = True\n    rest_a = a[~in_task[(a * 1000).astype(int)]]\n    rest_dur = (~in_task[:int(a[-1] * 1000)]).sum() / 1000\n    rate = len(rest_a) / rest_dur\n    # detect within rest segments\n    edges = np.flatnonzero(np.diff(np.r_[0, (~in_task).astype(int), 0]))\n    segs = edges.reshape(-1, 2) / 1000\n    bl, pl = [], []\n    for lo_, hi_ in segs:\n        x = a[(a >= lo_) & (a < hi_)]\n        bl += g.bursts(x, rate)\n        pl += g.pauses(x, rate)\n    events = {\"burst onset\": np.array([e[0] for e in bl]), \"burst offset\": np.array([e[1] for e in bl]),\n              \"pause onset\": np.array([e[0] for e in pl])}\n    counts = np.bincount((b * 1000).astype(int), minlength=T)[:T].astype(float)\n    vrate = g.gaussian_filter1d(counts * 1000.0, 10.0)\n    for k, ev in events.items():\n        ev = ev[(ev > 1.0) & (ev < T / 1000 - 1.0)]\n        if len(ev) < 5:\n            continue\n        idx = (ev * 1000).astype(int)\n        X = g.event_sums(vrate, idx)\n        avg = X[LAGS % T] / len(idx)\n        base = avg[(LAGS >= -800) & (LAGS < -50)]\n        lo_b, hi_b = np.percentile(base, [2.5, 97.5])\n        if hi_b - lo_b > 0.6 * abs(base.mean()):\n            n_excluded[k] += 1\n            continue\n        ta[k].append(avg)\n        n_events[k].append(len(idx))\n        post = avg[(LAGS >= 0) & (LAGS <= 100)]\n        pair_sig[k].append(\"decrease\" if (post < lo_b).any() else (\"increase\" if (post > hi_b).any() else \"none\"))\n        shifts = rng.integers(2000, 20001, size=400) * rng.choice([-1, 1], size=400)\n        ctrl[k].append(np.array([X[(LAGS + sh) % T] / len(idx) for sh in shifts]))\nprint(f\"Bursts and pauses in {time.time() - started:.0f} s\")\nfig, axes = plt.subplots(1, 3, figsize=(12, 3), sharey=True)\nwin = (LAGS >= 0) & (LAGS <= 300)\nfor ax, k in zip(axes, ta):\n    pop = np.mean(ta[k], 0)\n    c = np.mean(np.stack(ctrl[k]), 0)               # control population averages, 400 x lags\n    lo_c, hi_c = np.percentile(c, [2.5, 97.5], axis=0)\n    shift = np.percentile((c[:, win] - lo_c[win]).min(1), 5)\n    lo_corr = lo_c + min(shift, 0)\n    below = win & (pop < lo_corr)\n    above = win & (pop > hi_c - min(shift, 0))\n    first = LAGS[below][0] if below.any() else None\n    sig = pd.Series(pair_sig[k]).value_counts()\n    print(f\"{k}: {len(ta[k])} pairs (excluded as noisy {n_excluded[k]}), events per pair median {np.median(n_events[k]):.0f}; \"\n          f\"population rate at baseline {pop[LAGS < -50].mean():.2f} spikes/s, minimum in 0 to 300 ms {pop[win].min():.2f} \"\n          f\"({100 * (pop[win].min() / pop[LAGS < -50].mean() - 1):.1f}%); below the corrected band: {bool(below.any())}, \"\n          f\"from {first} ms; above it: {bool(above.any())}\")\n    print(f\"   pairs with a change in 0 to 100 ms: {int(sig.drop('none', errors='ignore').sum())} of {len(pair_sig[k])} \"\n          f\"({100 * sig.drop('none', errors='ignore').sum() / len(pair_sig[k]):.1f}%); decreases {int(sig.get('decrease', 0))}, increases {int(sig.get('increase', 0))}\")\n    ax.plot(LAGS, pop, \"k\"); ax.fill_between(LAGS, lo_corr, hi_c - min(shift, 0), color=\"0.8\")\n    ax.set_title(k); ax.set_xlabel(\"ms from event\")\naxes[0].set_ylabel(\"VLa rate (spikes/s)\")\nprint(\"All plotted values are inside the axes.\")\n\n# %% md\n## behavior-rt-mt\n\n> Reaction times do not differ between the animals or reach directions; movement durations are\n> longer for reaches to the right target, and NHP G moves more slowly than NHP I.\n\n# %% code claim:behavior-rt-mt\nv = tr[tr.valid]\nper = v.groupby([\"subject\", \"session\", \"target\"]).agg(rt=(\"rt\", \"median\"), mt=(\"mt\", \"median\"), n=(\"rt\", \"size\")).reset_index()\nprint(\"Per file and direction, medians (s):\")\nprint(per.groupby([\"subject\", \"target\"])[[\"rt\", \"mt\"]].agg([\"median\", \"count\"]).round(3).to_string())\nfor col in (\"rt\", \"mt\"):\n    d = per.dropna(subset=[col])\n    model = ols(f\"{col} ~ C(subject) * C(target)\", data=d).fit()\n    print(f\"\\nTwo-way ANOVA of {col} (type II), {len(d)} file-directions:\")\n    print(sm.stats.anova_lm(model, typ=2).round(4).to_string())\nprint(\"\\nVariant, trials pooled: RT animal p = %.3g, direction p = %.3g\" % (\n    stats.ranksums(v[v.subject == \"Gaia\"].rt, v[v.subject == \"Isis\"].rt).pvalue,\n    stats.ranksums(v[v.target == \"Left\"].rt, v[v.target == \"Right\"].rt).pvalue))\n\n# %% md\n## figs3-emg-onset\n\nBlocked. The EMG is not in the dandiset; it is in the paper's Dryad deposit (S3_EMGdata files).\nNeither the Methods nor `FigS3.m`, which only plots the trial-averaged EMG, say how the onset of\nthe EMG change was determined, so the reported onsets cannot be recomputed by the paper's method.\n\n## fig1-vla-localization\n\nBlocked. The stimulation mapping (responses to GPi, SCP and motor cortex stimulation along the\nelectrode tracks) is not in the dandiset, which holds the task recordings only, nor in the Dryad\ndeposit.\n\n## fig6-simulation\n\nBlocked. The simulation uses no recorded data. The Dryad deposit holds its output\n(`Data_Fig6.mat`) and a plotting script, but not the model thalamocortical cell or the code that\ngenerated correlated GPi spike trains; reimplementing the model of the paper's reference 103 was\nnot attempted.\n\n# %% code\nprint(f\"Notebook ran in {(time.time() - started) / 60:.1f} min since the last timer reset\")\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('nb_src.py').read()
s=s.replace("""from scipy import stats
from statsmodels.formula.api import ols""","""from scipy import stats
from scipy.ndimage import gaussian_filter1d
from statsmodels.formula.api import ols""")
s=s.replace("""started = time.time()
all_files""","""NB_START = started = time.time()
all_files""")
s=s.replace("g.gaussian_filter1d(counts","gaussian_filter1d(counts")
s=s.replace("    pks = ks_p = g.ks_permutation","    ks_p = g.ks_permutation")
s=s.replace('print(f"Notebook ran in {(time.time() - started) / 60:.1f} min since the last timer reset")','print(f"Notebook ran in {(time.time() - NB_START) / 60:.1f} min")')
# fig5 memory fix and caching
s=s.replace("""ctrl = {k: [] for k in ta}""","""ctrl_sum = {k: 0.0 for k in ta}
burst_cache, rate_cache = {}, {}""")
s=s.replace("""        ctrl[k].append(np.array([X[(LAGS + sh) % T] / len(idx) for sh in shifts]))""","""        ctrl_sum[k] = ctrl_sum[k] + np.array([X[(LAGS + sh) % T] / len(idx) for sh in shifts])""")
s=s.replace("""    c = np.mean(np.stack(ctrl[k]), 0)               # control population averages, 400 x lags""","""    c = ctrl_sum[k] / len(ta[k])                   # control population averages, 400 x lags""")
s=s.replace("""    rest_a = a[~in_task[(a * 1000).astype(int)]]
    rest_dur = (~in_task[:int(a[-1] * 1000)]).sum() / 1000
    rate = len(rest_a) / rest_dur
    # detect within rest segments
    edges = np.flatnonzero(np.diff(np.r_[0, (~in_task).astype(int), 0]))
    segs = edges.reshape(-1, 2) / 1000
    bl, pl = [], []
    for lo_, hi_ in segs:
        x = a[(a >= lo_) & (a < hi_)]
        bl += g.bursts(x, rate)
        pl += g.pauses(x, rate)""","""    if p.gpi not in burst_cache:
        rest_a = a[~in_task[(a * 1000).astype(int)]]
        rest_dur = (~in_task[int(a[0] * 1000):int(a[-1] * 1000)]).sum() / 1000
        rate = len(rest_a) / rest_dur
        edges = np.flatnonzero(np.diff(np.r_[0, (~in_task).astype(int), 0]))
        bl, pl = [], []
        for lo_, hi_ in edges.reshape(-1, 2) / 1000:      # rest segments
            x = a[(a >= lo_) & (a < hi_)]
            bl += g.bursts(x, rate)
            pl += g.pauses(x, rate)
        burst_cache[p.gpi] = (bl, pl)
    bl, pl = burst_cache[p.gpi]""")
open('nb_src.py','w').write(s)

import re, nbformat
cells=[]
parts=re.split(r'^# %% ', s, flags=re.M)[1:]
for p in parts:
    head, _, body = p.partition('\n')
    body=body.strip('\n')
    h=head.split()
    if h[0]=='md':
        cells.append(nbformat.v4.new_markdown_cell(body))
    else:
        c=nbformat.v4.new_code_cell(body)
        if len(h)>1: c.metadata['tags']=h[1:]
        cells.append(c)
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb,'entries/000947-schwab-2020/reproduce_schwab_2020.ipynb')
# also export as script for quick run
code='\n\n'.join(c.source for c in cells if c.cell_type=='code')
open('nb_run.py','w').write(code)
print(len(cells))
EOF
```

```
56
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; uv pip install -q --python venv/bin/python statsmodels 2>&1 | tail -1; sed 's#^sessions = g.load_all()#import pickle; sessions = pickle.load(open("/tmp/claude-1001/sessions.pkl","rb"))#' nb_run.py > nb_dbg.py; sed -i 's#^import matplotlib.pyplot as plt#import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt#' nb_dbg.py; cd entries/000947-schwab-2020 && timeout 3000 $TMPDIR/venv/bin/python $TMPDIR/nb_dbg.py 2>&1 | tail -150
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/nb_dbg.py", line 16, in <module>
    import gpivla as g
ModuleNotFoundError: No module named 'gpivla'
```

**Agent calls Bash**

```bash
PYTHONPATH=. $TMPDIR/venv/bin/python -c "
import gpivla as g, pickle, time
t=time.time(); S=g.load_all(); print(len(S), time.time()-t)
pickle.dump(S, open('/tmp/claude-1001/sessions.pkl','wb'))
print(list(S[0]['processed'].items())[0])
"
```

```
254 194.73779296875
('ElectricalSeriesProcessed', {'electrodes': array([0, 1, 2, 3]), 'shape': (8345627, 4), 'chunks': (312500, 4), 'rate': 24414.0625, 'start': 9.5367431640625e-07})
```

**Agent calls Bash**

```bash
PYTHONPATH=. timeout 3000 $TMPDIR/venv/bin/python $TMPDIR/nb_dbg.py > $TMPDIR/run1.log 2>&1; tail -5 $TMPDIR/run1.log; wc -l $TMPDIR/run1.log
```

```
C(subject):C(target)  0.0065    1.0   30.8620     0.0
Residual              0.0679  322.0       NaN     NaN

Variant, trials pooled: RT animal p = 2.47e-59, direction p = 2.23e-13
Notebook ran in 13.9 min
403 /tmp/claude-1001/run1.log
```

**Agent**

The full analysis ran without errors (about 14 minutes plus 3 minutes of loading). Reviewing the outputs.

**Agent calls Bash**

```bash
sed -n 1,200p $TMPDIR/run1.log
```

```
/tmp/claude-1001/nb_dbg.py:255: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
  counts["total"] = counts.sum(1)
/tmp/claude-1001/nb_dbg.py:264: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
  print(distinct.groupby(["area", "subject"]).size().unstack().assign(total=lambda d: d.sum(1)).to_string())
/tmp/claude-1001/nb_dbg.py:266: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
  print(paper[paper.keep & paper.complete].groupby(["area", "monk"]).size().unstack().assign(total=lambda d: d.sum(1)).to_string())
378 files in dandiset 000947 version 0.240510.2211; loaded the 254 pre-MPTP files in 13 s
Archive summary: subjects 2 | files 378 | species ['Macaca mulatta - Rhesus monkey']
Related resources: ['https://doi.org/10.1371/journal.pbio.3000829', 'https://github.com/dandi/example-notebooks/blob/master/000947/TurnerLab/public_demo/000947_demo.ipynb', 'https://doi.org/10.1101/2023.09.08.556120']

Files by subject and condition:
condition  post-MPTP  pre-MPTP
subject                       
Gaia             101       119
Isis              23       135

MPTP status attribute of the pre-MPTP files: {'pre_MPTP': 254}
related_publications in the files: {'https://doi.org/10.1101/546598': 254}
Files without a trials table: ['pre-MPTP-I-160616-4']
Files without curated units: 21 of 254
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,403p $TMPDIR/run1.log | grep -v Pandas4Warning | grep -v "pct = (100"
```

```
mean    std  median  size
area subject                            
GPi  Gaia     0.241  0.061   0.246   137
     Isis     0.271  0.135   0.246   131
VLa  Gaia     0.496  0.219   0.573    78
     Isis     0.537  0.225   0.573   201
       mean    std  median    min    max  size
area                                          
GPi   0.256  0.105   0.246  0.082  0.983   268
VLa   0.526  0.224   0.573  0.082  1.065   279
GPi 0.256 ms against VLa 0.526 ms; rank sum z = -12.82, p = 1.3e-37
Sampling interval of the trace: 0.0410 ms
Units outside the axes (above 1.2 ms): 0
Dandiset rule - units with a significant control-period slope in at least one direction:
          mean  sum  size  percent
area                              
GPi   0.985075  264   268     98.5
VLa   0.985663  275   279     98.6
  mean slope (spikes/s2) GPi -0.598, VLa 0.233; medians -0.531, 0.176; rank sum p = 0.0415
  significant unit-direction slopes positive: 49.9% of 969
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000947-schwab-2020; python3 - <<'EOF'
p='gpivla.py'; s=open(p).read()
i=s.index('def ap_width(')
s=s[:i]+'''def ap_widths(url: str, series: str, rate: float, start: float, chunk: int,
              units: list[tuple[str, int, np.ndarray]], max_spikes: int = 300) -> list[dict]:
    """Trough-to-peak time (ms) of the mean waveform of each unit on its channel of the filtered
    trace `series`, from the spikes inside one HDF5 chunk (the one holding the most spikes of
    these units), so that each file and series is read once. `units` holds (id, column, spikes)."""
    idx = {uid: np.round((sp - start) * rate).astype(int) for uid, _, sp in units}
    which = np.concatenate([v // chunk for v in idx.values()])
    vals, counts = np.unique(which, return_counts=True)
    c = int(vals[np.argmax(counts)])
    f = _open(url)
    d = f[f"processing/ecephys/Processed/{series}/data"]
    lo, hi = c * chunk, min((c + 1) * chunk, d.shape[0])
    block = d[lo:hi, :]
    f.close()
    pre, post = int(0.0006 * rate), int(0.0012 * rate)
    out = []
    for uid, col, _ in units:
        sel = idx[uid][(idx[uid] // chunk) == c] - lo
        sel = sel[(sel > pre) & (sel < len(block) - post)][:max_spikes]
        if len(sel) < 10:
            out.append({"uid": uid, "width_ms": np.nan, "n_spikes": len(sel)})
            continue
        w = np.mean([block[k - pre:k + post, col] for k in sel], 0)
        t0 = int(np.argmin(w))
        t1 = t0 + int(np.argmax(w[t0:]))
        out.append({"uid": uid, "width_ms": (t1 - t0) / rate * 1000.0, "n_spikes": len(sel)})
    return out
'''
open(p,'w').write(s)
EOF
tail -5 gpivla.py
```

```
w = np.mean([block[k - pre:k + post, col] for k in sel], 0)
        t0 = int(np.argmin(w))
        t1 = t0 + int(np.argmax(w[t0:]))
        out.append({"uid": uid, "width_ms": (t1 - t0) / rate * 1000.0, "n_spikes": len(sel)})
    return out
```

**Agent**

Now updating the notebook source for these changes.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('nb_src.py').read()
old_start=s.index("# %% md\n**Clock check.**")
old_end=s.index("# %% md\n## Unit selection and peri-movement responses")
s=s[:old_start]+'''# %% md
**Clock check.** With spikes and a trial table only, the check is whether the trial labels carry
information in the spikes at the time of movement but not before the cue, when the animal does not
know the target. For each unit with at least 10 valid trials per direction, left and right spike
counts are compared (rank sum) in the movement window (-200 to +300 ms) and in a window before the
cue (-1500 to -1000 ms from movement onset). Two controls: the labels permuted within the file,
and the true labels with every trial time moved 1 s later (a clock offset).

# %% code sanity
def window_counts(spikes, align, lo, hi):
    a = np.searchsorted(spikes, align + lo)
    b = np.searchsorted(spikes, align + hi)
    return b - a

rng = np.random.default_rng(0)
rows = []
for s in sessions:
    if s["vt"] is None:
        continue
    t = s["vt"][s["vt"].valid]
    left = (t.target == "Left").to_numpy()
    permuted = rng.permutation(left)
    al = t.movement_start_time.to_numpy()
    for u in s["units"]:
        if g.area(u.get("location")) not in ("GPi", "VLa") or left.sum() < 10 or (~left).sum() < 10:
            continue
        r = {"session": s["session_id"], "subject": s["subject"], "area": g.area(u.get("location"))}
        for name, (lo, hi) in {"movement": (-0.2, 0.3), "pre_cue": (-1.5, -1.0)}.items():
            for lab, mask, shift in (("true", left, 0.0), ("permuted", permuted, 0.0), ("offset_1s", left, 1.0)):
                c = window_counts(u["spikes"], al + shift, lo, hi)
                r[f"{name}_{lab}"] = stats.mannwhitneyu(c[mask], c[~mask]).pvalue if c.std() > 0 else 1.0
        rows.append(r)
clock = pd.DataFrame(rows)
cols = [f"{w}_{l}" for w in ("movement", "pre_cue") for l in ("true", "permuted", "offset_1s")]
print("Fraction of units whose spike counts differ between left and right trials (p < 0.05):")
print(clock.groupby("area")[cols].agg(lambda p: (p < 0.05).mean()).round(3).T.to_string())
per_session = clock.groupby("session").movement_true.apply(lambda p: (p < 0.05).any())
print(f"\\nFiles with at least one direction-tuned unit in the movement window: {per_session.sum()} of {len(per_session)}")
print("Files where none is tuned (the clock cannot be checked this way):", sorted(per_session[~per_session].index))

# %% md
CLOCK_TEXT

'''+s[old_end:]

# AP width block
a=s.index("from concurrent.futures import ThreadPoolExecutor\nstarted = time.time()\njobs = []")
b=s.index('print(widths.groupby(["area", "subject"])')
s=s[:a]+'''from concurrent.futures import ThreadPoolExecutor
started = time.time()
jobs = {}
for r in dand_records:
    if r["uid"] not in kept or np.isnan(r["channel"]):
        continue
    s = r["sess"]
    rows_ = np.flatnonzero(pd.to_numeric(s["electrodes"].channel_ids, errors="coerce").to_numpy() == r["channel"])
    for name, p in s["processed"].items():
        cols = np.flatnonzero(np.isin(p["electrodes"], rows_))
        if len(cols) == 1:
            jobs.setdefault((s["url"], name), (p, []))[1].append((r["uid"], int(cols[0]), r["segments"][0][0]))
            break

def width_job(item):
    (url, name), (p, us) = item
    return g.ap_widths(url, name, p["rate"], p["start"], p["chunks"][0], us)

with ThreadPoolExecutor(16) as ex:
    widths = pd.DataFrame([w for ws in ex.map(width_job, jobs.items()) for w in ws])
widths = widths.merge(units[["uid", "area", "subject"]], on="uid")
print(f"Units with a channel in a filtered series: {len(widths)} of {len(units)}, in {len(jobs)} file-series; widths measured: "
      f"{int(widths.width_ms.notna().sum())} ({time.time() - started:.0f} s)")
print("Spikes per unit used: median", int(widths.n_spikes.median()), ", min", int(widths.n_spikes.min()))
'''+s[b:]

# CCF: print control median
s=s.replace('''f"KS permutation p = {ks_p:.3f}; median peak {d.peak.median():.3f}, median control 95th percentile {d.thr95.median():.3f}")''','''f"KS permutation p = {ks_p:.3f}; median peak {d.peak.median():.3f}, median control peak {np.median(np.vstack(ctrl_peaks[name])):.3f}, "
          f"median control 95th percentile {d.thr95.median():.3f}")''')
# bursts stats
s=s.replace('''        burst_cache[p.gpi] = (bl, pl)''','''        burst_cache[p.gpi] = (bl, pl)
        burst_stats.append({"gpi": p.gpi, "rest_s": rest_dur, "rate": rate, "n_bursts": len(bl), "n_pauses": len(pl),
                            "burst_ms": np.mean([1000 * (e - b0) for b0, e in bl]) if bl else np.nan,
                            "pause_ms": np.mean([1000 * (e - b0) for b0, e in pl]) if pl else np.nan})''')
s=s.replace('''burst_cache, rate_cache = {}, {}''','''burst_cache, burst_stats = {}, []''')
s=s.replace('''print(f"Bursts and pauses in {time.time() - started:.0f} s")''','''print(f"Bursts and pauses in {time.time() - started:.0f} s")
bs = pd.DataFrame(burst_stats)
print(f"GPi units: {len(bs)}; rest per unit median {bs.rest_s.median():.0f} s; bursts per minute of rest median "
      f"{(60 * bs.n_bursts / bs.rest_s).median():.2f}; pauses per minute median {(60 * bs.n_pauses / bs.rest_s).median():.2f}")
print(f"Mean burst duration {np.nanmean(bs.burst_ms):.1f} ms (paper 24 ms); mean pause duration {np.nanmean(bs.pause_ms):.1f} ms (paper 195 ms)")''')
s=s.replace('counts["total"] = counts.sum(1)','counts["total"] = counts.sum(axis=1)').replace('d.sum(1)','d.sum(axis=1)').replace('t.div(t.sum(1), axis=0)','t.div(t.sum(axis=1), axis=0)')
open('nb_src.py','w').write(s)
EOF
grep -n "sum(1)" nb_src.py | head
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > build.py <<'EOF'
import re, nbformat, sys
s=open('/tmp/claude-1001/nb_src.py').read()
cells=[]
for p in re.split(r'^# %% ', s, flags=re.M)[1:]:
    head, _, body = p.partition('\n'); body=body.strip('\n'); h=head.split()
    if h[0]=='md': cells.append(nbformat.v4.new_markdown_cell(body))
    else:
        c=nbformat.v4.new_code_cell(body)
        if len(h)>1: c.metadata['tags']=h[1:]
        cells.append(c)
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb,'entries/000947-schwab-2020/reproduce_schwab_2020.ipynb')
code='\n\n'.join(c.source for c in cells if c.cell_type=='code')
code=code.replace('sessions = g.load_all()','import pickle; sessions = pickle.load(open("/tmp/claude-1001/sessions.pkl","rb"))')
code=code.replace('import matplotlib.pyplot as plt','import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt')
open('/tmp/claude-1001/nb_dbg.py','w').write(code)
print(len(cells))
EOF
python3 build.py && cd entries/000947-schwab-2020 && PYTHONPATH=. timeout 3000 $TMPDIR/venv/bin/python $TMPDIR/nb_dbg.py > $TMPDIR/run2.log 2>&1; grep -v Pandas4 $TMPDIR/run2.log | sed -n '/Fraction of units/,/Dandiset rule:/p'; grep -A8 "Units with a channel" $TMPDIR/run2.log; grep -B2 -A12 "Bursts and pauses in" $TMPDIR/run2.log; grep "^whole\|^rest\|^movement\|Notebook ran" $TMPDIR/run2.log; grep -i "error\|Traceback" $TMPDIR/run2.log | head
```

```
56
Fraction of units whose spike counts differ between left and right trials (p < 0.05):
area                  GPi    VLa
movement_true       0.485  0.386
movement_permuted   0.067  0.034
movement_offset_1s  0.372  0.319
pre_cue_true        0.087  0.078
pre_cue_permuted    0.038  0.041
pre_cue_offset_1s   0.253  0.214

Files with at least one direction-tuned unit in the movement window: 129 of 163
Files where none is tuned (the clock cannot be checked this way): ['pre-MPTP-G-140511-3', 'pre-MPTP-G-140511-6', 'pre-MPTP-G-140511-8', 'pre-MPTP-G-140511-9', 'pre-MPTP-G-140512-1', 'pre-MPTP-G-140512-8', 'pre-MPTP-G-140512-9', 'pre-MPTP-G-140514-10', 'pre-MPTP-G-140514-8', 'pre-MPTP-G-140521-3', 'pre-MPTP-G-140524-1', 'pre-MPTP-G-140524-3', 'pre-MPTP-G-140524-5', 'pre-MPTP-G-140524-6', 'pre-MPTP-G-140525-6', 'pre-MPTP-G-140611-1', 'pre-MPTP-G-140611-3', 'pre-MPTP-G-140612-5', 'pre-MPTP-G-140612-9', 'pre-MPTP-G-140617-3', 'pre-MPTP-G-140617-4', 'pre-MPTP-G-140627-2', 'pre-MPTP-G-140701-1', 'pre-MPTP-G-140723-1', 'pre-MPTP-G-140723-2', 'pre-MPTP-G-140902-3', 'pre-MPTP-G-140902-4', 'pre-MPTP-I-160624-1', 'pre-MPTP-I-160714-1', 'pre-MPTP-I-160714-4', 'pre-MPTP-I-160718-1', 'pre-MPTP-I-170615-2', 'pre-MPTP-I-170616-2', 'pre-MPTP-I-170623-2']
Dandiset rule: 547 units, 1083 unit-directions (12 s)
Units with a channel in a filtered series: 547 of 547, in 205 file-series; widths measured: 532 (197 s)
Spikes per unit used: median 273 , min 0
               mean    std  median  size
area subject                            
GPi  Gaia     0.239  0.064   0.246   137
     Isis     0.256  0.133   0.205   131
VLa  Gaia     0.489  0.223   0.532    78
[... 30 more lines not kept]
```

**Agent**

Burst durations come out at 254 ms against the paper's 24 ms, so the burst detection needs a check before the result can count. Inspecting it on real GPi trains.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > bt.py <<'EOF'
import sys, pickle, numpy as np
sys.path.insert(0,'entries/000947-schwab-2020')
import gpivla as g
S=pickle.load(open('sessions.pkl','rb'))
s=[x for x in S if x['session_id']=='pre-MPTP-I-160615-1'][0]
u=[u for u in s['units'] if g.area(u['location'])=='GPi'][0]
a=u['spikes']; rate=len(a)/(a[-1]-a[0]); print('rate',rate, len(a))
b=g.bursts(a,rate); d=np.array([e-s0 for s0,e in b])*1000
n=[np.sum((a>=s0)&(a<=e)) for s0,e in b]
print(len(b), np.mean(d), np.median(d), np.median(n))
for (s0,e),nn in list(zip(b,n))[:8]: print(round(s0,3), round((e-s0)*1000,1), nn, (nn-1)/(e-s0))
EOF
venv/bin/python bt.py
```

```
/tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/venv/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
rate 68.79924172783731 71067
0 nan nan nan
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat >> bt.py <<'EOF'
import gpivla
from scipy.special import gammainc
for base in ['ln','log10']:
    f = (lambda n,d,r: -np.log(max(gammainc(n, r*d),1e-300))) if base=='ln' else (lambda n,d,r: -np.log10(max(gammainc(n, r*d),1e-300)))
    g._poisson_surprise=f
    allb=[]; allp=[]
    for s in S[:60]:
        for u in s['units']:
            if g.area(u['location'])!='GPi' or len(u['spikes'])<1000: continue
            a=u['spikes']; r=len(a)/(a[-1]-a[0])
            if r<30: continue
            b=g.bursts(a,r); allb+= [ (e-s0)*1000 for s0,e in b]
            isi=np.diff(a); ss = r*isi if base=='ln' else r*isi/np.log(10)
            allp += list(isi[(isi>=0.1)&(ss>=5)]*1000)
    print(base, 'bursts', len(allb), np.mean(allb) if allb else None, np.median(allb) if allb else None, 'pauses', len(allp), np.mean(allp))
EOF
venv/bin/python bt.py 2>&1 | grep -v Warn | tail -3
```

```
0 nan nan nan
ln bursts 19380 67.71097599999995 35.75807999999681 pauses 10988 172.67304189297414
log10 bursts 1150 311.9721249391305 272.8345599999926 pauses 2857 288.7542080784042
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000947-schwab-2020; python3 - <<'EOF'
p='gpivla.py'; s=open(p).read()
s=s.replace('''- Common choices, where neither says: the surprise uses log base 10 (as in Legendy and Salcman);
  the VLa spikes are the ones jittered; the Poisson probability for a burst uses the unit's mean
  rest rate.''','''- The Methods define the surprise as S = -log(P); the natural log is used, as `log` is in the
  paper's MATLAB. (A first run used log10, which gave bursts ten times longer than the paper's
  mean of 24 ms.)
- Common choices, where neither says: the VLa spikes are the ones jittered; the Poisson
  probability for a burst uses the unit's mean rest rate.''')
s=s.replace('''    """-log10 of the Poisson probability of n or more spikes in `duration` at `rate`."""
    return -np.log10(max(gammainc(n_spikes, rate * duration), 1e-300))''','''    """-ln of the Poisson probability of n or more spikes in `duration` at `rate`."""
    return -np.log(max(gammainc(n_spikes, rate * duration), 1e-300))''')
s=s.replace('''    s = rate * isi / np.log(10)                 # -log10(exp(-rate * isi))''','''    s = rate * isi                              # -ln(exp(-rate * isi))''')
open(p,'w').write(s)
EOF
grep -n "log" gpivla.py | head
```

```
3:Schwab, Kase, Zimnik, Rosenbaum, Codianni, Rubin & Turner (2020), PLOS Biology,
40:- The Methods define the surprise as S = -log(P); the natural log is used, as `log` is in the
41:  paper's MATLAB. (A first run used log10, which gave bursts ten times longer than the paper's
410:    return -np.log(max(gammainc(n_spikes, rate * duration), 1e-300))
```

**Agent calls Bash**

```bash
grep -n "rate \* isi" gpivla.py; PYTHONPATH=. timeout 3000 $TMPDIR/venv/bin/python $TMPDIR/nb_dbg.py > $TMPDIR/run3.log 2>&1; grep -B2 -A12 "Bursts and pauses in" $TMPDIR/run3.log; grep "Notebook ran\|Traceback" $TMPDIR/run3.log
```

```
453:    s = rate * isi                              # -ln(exp(-rate * isi))
movement: (a) 669 pair-targets, significant 72 (10.8%), +39 / -33 (binomial p of the sign balance 0.556); (b) 338 pairs, significant in either target 63 (18.6%)
   KS permutation p (absolute correlations against shuffles) = 0.000; median r 0.001; shuffle band -0.291 to 0.292
Bursts and pauses in 224 s
GPi units: 144; rest per unit median 312 s; bursts per minute of rest median 17.75; pauses per minute median 11.66
Mean burst duration 67.1 ms (paper 24 ms); mean pause duration 145.3 ms (paper 195 ms)
burst onset: 163 pairs (excluded as noisy 144), events per pair median 208; population rate at baseline 20.92 spikes/s, minimum in 0 to 300 ms 20.36 (-2.6%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 85 of 163 (52.1%); decreases 52, increases 33
burst offset: 160 pairs (excluded as noisy 147), events per pair median 208; population rate at baseline 20.97 spikes/s, minimum in 0 to 300 ms 20.50 (-2.3%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 92 of 160 (57.5%); decreases 52, increases 40
pause onset: 119 pairs (excluded as noisy 134), events per pair median 188; population rate at baseline 21.52 spikes/s, minimum in 0 to 300 ms 21.11 (-1.9%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 61 of 119 (51.3%); decreases 34, increases 27
All plotted values are inside the axes.
Per file and direction, medians (s):
                   rt           mt      
               median count median count
Notebook ran in 10.5 min
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('nb_src.py').read()
old='''    counts = np.bincount((b * 1000).astype(int), minlength=T)[:T].astype(float)
    vrate = gaussian_filter1d(counts * 1000.0, 10.0)
    for k, ev in events.items():
        ev = ev[(ev > 1.0) & (ev < T / 1000 - 1.0)]
        if len(ev) < 5:
            continue
        idx = (ev * 1000).astype(int)
        X = g.event_sums(vrate, idx)
        avg = X[LAGS % T] / len(idx)'''
new='''    counts = np.bincount((b * 1000).astype(int), minlength=T)[:T].astype(float)
    rest = (~in_task).astype(float)
    vrate = gaussian_filter1d(counts * 1000.0, 10.0) * rest       # VLa rate, rest samples only
    for k, ev in events.items():
        ev = ev[(ev > 1.0) & (ev < T / 1000 - 1.0)]
        if len(ev) < 5:
            continue
        idx = (ev * 1000).astype(int)
        X, W = g.event_sums(vrate, idx), g.event_sums(rest, idx)
        avg = X[LAGS % T] / W[LAGS % T]'''
assert old in s; s=s.replace(old,new)
old2='''        shifts = rng.integers(2000, 20001, size=400) * rng.choice([-1, 1], size=400)
        ctrl_sum[k] = ctrl_sum[k] + np.array([X[(LAGS + sh) % T] / len(idx) for sh in shifts])'''
new2='''        shifts = rng.integers(2000, 20001, size=400) * rng.choice([-1, 1], size=400)
        ctrl_sum[k] = ctrl_sum[k] + np.array([X[(LAGS + sh) % T] / W[(LAGS + sh) % T] for sh in shifts])'''
assert old2 in s; s=s.replace(old2,new2)
open('nb_src.py','w').write(s)
EOF
grep -n "def event_sums" -A12 entries/000947-schwab-2020/gpivla.py
```

```
458:def event_sums(rate_ms: np.ndarray, events_ms: np.ndarray) -> np.ndarray:
459-    """X(L) = sum over events e of rate_ms[e + L], for every lag L (circular), by FFT. The
460-    event-triggered average at lag L is X(L) / n; with the events shifted by k it is X(L + k) / n."""
461-    n = len(rate_ms)
462-    ev = np.zeros(n)
463-    np.add.at(ev, events_ms, 1.0)
464-    x = np.fft.irfft(np.conj(np.fft.rfft(ev)) * np.fft.rfft(rate_ms), n)
465-    return x
466-
467-
468-# --- action potential width ----------------------------------------------------------------
469-
470-def ap_widths(url: str, series: str, rate: float, start: float, chunk: int,
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''        avg = X[LAGS % T] / W[LAGS % T]''','''        ratio = np.where(W > 0.5, X / np.maximum(W, 0.5), np.nan)     # lags where no event has a rest sample: NaN
        avg = ratio[LAGS % T]''')
s=s.replace('''        ctrl_sum[k] = ctrl_sum[k] + np.array([X[(LAGS + sh) % T] / W[(LAGS + sh) % T] for sh in shifts])''','''        c_ = np.array([ratio[(LAGS + sh) % T] for sh in shifts])
        ctrl_sum[k] = ctrl_sum[k] + np.where(np.isnan(c_), np.nanmean(avg), c_)''')
s=s.replace('''        base = avg[(LAGS >= -800) & (LAGS < -50)]
        lo_b, hi_b = np.percentile(base, [2.5, 97.5])''','''        if np.isnan(avg).any():
            n_excluded[k] += 1
            continue
        base = avg[(LAGS >= -800) & (LAGS < -50)]
        lo_b, hi_b = np.percentile(base, [2.5, 97.5])''')
open('nb_src.py','w').write(s)
EOF
python3 build.py && cd entries/000947-schwab-2020 && PYTHONPATH=. timeout 3000 $TMPDIR/venv/bin/python $TMPDIR/nb_dbg.py > $TMPDIR/run4.log 2>&1; grep -B2 -A12 "Bursts and pauses in" $TMPDIR/run4.log; grep "Notebook ran\|Traceback\|Error" $TMPDIR/run4.log
```

```
56
movement: (a) 669 pair-targets, significant 72 (10.8%), +39 / -33 (binomial p of the sign balance 0.556); (b) 338 pairs, significant in either target 63 (18.6%)
   KS permutation p (absolute correlations against shuffles) = 0.000; median r 0.001; shuffle band -0.291 to 0.292
Bursts and pauses in 430 s
GPi units: 144; rest per unit median 312 s; bursts per minute of rest median 17.75; pauses per minute median 11.66
Mean burst duration 67.1 ms (paper 24 ms); mean pause duration 145.3 ms (paper 195 ms)
burst onset: 150 pairs (excluded as noisy 157), events per pair median 224; population rate at baseline 21.26 spikes/s, minimum in 0 to 300 ms 20.73 (-2.5%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 76 of 150 (50.7%); decreases 43, increases 33
burst offset: 150 pairs (excluded as noisy 157), events per pair median 241; population rate at baseline 21.20 spikes/s, minimum in 0 to 300 ms 20.80 (-1.9%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 75 of 150 (50.0%); decreases 38, increases 37
pause onset: 110 pairs (excluded as noisy 143), events per pair median 208; population rate at baseline 22.18 spikes/s, minimum in 0 to 300 ms 21.76 (-1.9%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 49 of 110 (44.5%); decreases 28, increases 21
All plotted values are inside the axes.
Per file and direction, medians (s):
                   rt           mt      
               median count median count
Notebook ran in 14.2 min
```

**Agent**

Burst section is now the slowest part (7 min). Speeding up its FFTs with padded fast lengths, then a final debug run to get the numbers for the conclusions.

**Agent calls Bash**

```bash
cd entries/000947-schwab-2020; python3 - <<'EOF'
p='gpivla.py'; s=open(p).read()
old=s[s.index('def event_sums'):s.index('# --- action potential width')]
new='''def event_sums(rate_ms: np.ndarray, events_ms: np.ndarray) -> np.ndarray:
    """X(L) = sum over events e of rate_ms[e + L], for every lag L, by FFT on a zero-padded
    (circular) array of fast length; index it modulo its own length. The event-triggered
    average at lag L is X(L) / n; with the events shifted by k it is X(L + k) / n."""
    n = next_fast_len(len(rate_ms), real=True)
    ev = np.zeros(n)
    np.add.at(ev, events_ms, 1.0)
    r = np.zeros(n)
    r[:len(rate_ms)] = rate_ms
    return irfft(np.conj(rfft(ev)) * rfft(r), n)


'''
s=s.replace(old,new)
s=s.replace("from scipy.special import gammainc","from scipy.fft import irfft, next_fast_len, rfft\nfrom scipy.special import gammainc")
open(p,'w').write(s)
EOF
cd $TMPDIR; python3 - <<'EOF'
s=open('nb_src.py').read()
old='''        ratio = np.where(W > 0.5, X / np.maximum(W, 0.5), np.nan)     # lags where no event has a rest sample: NaN
        avg = ratio[LAGS % T]'''
new='''        ratio = np.where(W > 0.5, X / np.maximum(W, 0.5), np.nan)     # lags where no event has a rest sample: NaN
        M = len(ratio)
        avg = ratio[LAGS % M]'''
assert old in s; s=s.replace(old,new)
s=s.replace("c_ = np.array([ratio[(LAGS + sh) % T] for sh in shifts])","c_ = np.array([ratio[(LAGS + sh) % M] for sh in shifts])")
open('nb_src.py','w').write(s)
EOF
python3 build.py && cd entries/000947-schwab-2020 && PYTHONPATH=. timeout 3000 $TMPDIR/venv/bin/python $TMPDIR/nb_dbg.py > $TMPDIR/run5.log 2>&1; grep -B2 -A12 "Bursts and pauses in" $TMPDIR/run5.log | head -14; grep "Notebook ran\|Traceback\|Error" $TMPDIR/run5.log
```

```
56
movement: (a) 669 pair-targets, significant 72 (10.8%), +39 / -33 (binomial p of the sign balance 0.556); (b) 338 pairs, significant in either target 63 (18.6%)
   KS permutation p (absolute correlations against shuffles) = 0.000; median r 0.001; shuffle band -0.291 to 0.292
Bursts and pauses in 57 s
GPi units: 144; rest per unit median 312 s; bursts per minute of rest median 17.75; pauses per minute median 11.66
Mean burst duration 67.1 ms (paper 24 ms); mean pause duration 145.3 ms (paper 195 ms)
burst onset: 150 pairs (excluded as noisy 157), events per pair median 224; population rate at baseline 21.26 spikes/s, minimum in 0 to 300 ms 20.73 (-2.5%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 76 of 150 (50.7%); decreases 43, increases 33
burst offset: 150 pairs (excluded as noisy 157), events per pair median 241; population rate at baseline 21.20 spikes/s, minimum in 0 to 300 ms 20.80 (-1.9%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 75 of 150 (50.0%); decreases 38, increases 37
pause onset: 110 pairs (excluded as noisy 143), events per pair median 208; population rate at baseline 22.18 spikes/s, minimum in 0 to 300 ms 21.76 (-1.9%); below the corrected band: False, from None ms; above it: False
   pairs with a change in 0 to 100 ms: 49 of 110 (44.5%); decreases 29, increases 20
All plotted values are inside the axes.
Per file and direction, medians (s):
                   rt           mt      
Notebook ran in 7.5 min
```

**Agent**

Run time is now about 11 minutes including loading. Reading the final numbers to write the conclusions.

**Agent calls Bash**

```bash
grep -v "Pandas4\|pct = (100\|counts\[\"total\"\]\|assign(total" $TMPDIR/run5.log | sed -n '/Units with a channel/,/Dandiset rule$/p' | head -30; grep -A3 "GPi 0.2" $TMPDIR/run5.log | head -4
```

```
Units with a channel in a filtered series: 547 of 547, in 205 file-series; widths measured: 532 (195 s)
Spikes per unit used: median 273 , min 0
               mean    std  median  size
area subject                            
GPi  Gaia     0.239  0.064   0.246   137
     Isis     0.256  0.133   0.205   131
VLa  Gaia     0.489  0.223   0.532    78
     Isis     0.518  0.218   0.573   201
       mean    std  median    min    max  size
area                                          
GPi   0.247  0.104   0.246  0.000  0.983   268
VLa   0.509  0.219   0.553  0.082  1.065   279
GPi 0.247 ms against VLa 0.509 ms; rank sum z = -12.76, p = 2.9e-37
Sampling interval of the trace: 0.0410 ms
Units outside the axes (above 1.2 ms): 0
Dandiset rule - units with a significant control-period slope in at least one direction:
          mean  sum  size  percent
area                              
GPi   0.985075  264   268     98.5
VLa   0.985663  275   279     98.6
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; venv/bin/python -c "
import pickle, numpy as np
S=pickle.load(open('sessions.pkl','rb'))
s=[x for x in S if x['session_id']=='pre-MPTP-I-170518-2'][0]
us=[u for u in s['units'] if u.get('unit_name') in ('6','7')]
for u in us: print({k:v for k,v in u.items() if k!='spikes'}, len(u['spikes']))
print(np.array_equal(us[0]['spikes'],us[1]['spikes']))
print(sum(1 for x in S if x['trials'] is not None and 'error_onset_time' in x['trials']), sum(1 for x in S if x['trials'] is not None))
"
```

```
{'unit_name': '6', 'location': 'M1-S', 'channel_ids': np.float64(40.0), 'sort_label': np.float64(1.0), 'unit_quality_post_sorting': 'good', 'sorted_in_file': True} 18841
{'unit_name': '7', 'location': 'M1-S', 'channel_ids': np.float64(43.0), 'sort_label': np.float64(1.0), 'unit_quality_post_sorting': 'good', 'sorted_in_file': True} 18841
True
127 253
Shell cwd was reset to
```

**Agent**

Writing the conclusions and summary into the notebook source.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('nb_src.py').read()
def after(marker_code_start, text):
    """insert a markdown cell after the code cell that starts with marker (the next '# %% ' after it)."""
    global s
    i=s.index(marker_code_start)
    j=s.index('\n# %% ', i+len(marker_code_start))
    s=s[:j]+'\n\n# %% md\n'+text.strip()+'\n'+s[j:]

s=s.replace('''for k, v in list(dups.items())[:10]:
    print("  ", v)''','''for k, v in list(dups.items())[:10]:
    us = [u for s in sessions if s["session_id"] == v[0][0] for u in s["units"] if u.get("unit_name") in [x[1] for x in v]]
    print("  ", v, "labels", [u.get("location") for u in us], "channels", [u.get("channel_ids") for u in us],
          "identical:", all(np.array_equal(us[0]["spikes"], x["spikes"]) for x in us[1:]))''')
s=s.replace('''Unit names repeat within some files (a unit on the GPi probe and a
unit with an empty label share a name). No spike train is stored twice, so no recording is counted
twice by identity; a neuron recorded over consecutive files appears once per file (see
`table1-unit-counts`).''','''Unit names repeat within some files (a unit on the GPi probe and a
unit with an empty label share a name). One spike train is stored twice, as two M1-S units on
different channels of one file; no GPi or VLa train is, so no recording used here is counted twice
by identity. A neuron recorded over consecutive files appears once per file (see
`table1-unit-counts`).''')
s=s.replace('CLOCK_TEXT','''With the true labels, 48.5% of GPi and 38.6% of VLa units differ between left and right trials in
the movement window, against 8.7% and 7.8% before the cue; with permuted labels both windows are
near the 5% expected by chance (3.4% to 6.7%). The 1 s offset does not remove the tuning (37.2% and
31.9%), because activity while holding at the target also depends on the target, so it does not
test the clock. The contrast between the movement and pre-cue windows is consistent with the spike
times and the trial table sharing a clock; the detected response onsets below, which cluster
between about -100 and 0 ms from movement onset, support it. In 34 of the 163 files with GPi or
VLa units no unit is tuned, and for them the shared clock is assumed, not shown.''')

after('# %% code claim:unit-link', '''**Result: reproduced.** Of the 394 records the paper's code keeps, 364 (92.4%) are found among the
dandiset's curated units in every file they span (Isis GPi 104 of 104, Gaia GPi 95 of 105, Gaia VLa
60 of 66, Isis VLa 105 of 119). For the 724 matched unit-directions, the SDF computed from the
dandiset correlates with the stored one at a median r of 0.9992, above 0.9 for 94.6%, with a median
rate ratio of 1.0003. Valid trial counts equal the paper's for 62.6% of unit-directions (median
difference 0). Detection agrees on the presence of an increase for 90.9% and of a decrease for
80.7% of unit-directions, with median onset differences of 7 and 11 ms. Of the matched units the
paper calls VLa, 25 are labelled "Thalamus" in the dandiset; 97 records span 2 to 5 files, which
the dandiset does not link.''')
after('# %% code claim:table1-unit-counts', '''**Result: not reproduced.** The dandiset rule gives 268 GPi units (Gaia 137, Isis 131) and 279 VLa
units (78 and 201), against 209 and 185 (or 218 in the text); neither is within 10%. Counting
units with the same channel and sort letter on the same day once gives 132 GPi and 186 VLa units,
and the paper's own records found in the dandiset are 199 and 165. The dandiset holds more
GPi and VLa-labelled units than the paper analysed (518 of the 547 are in files the paper used) and
does not say which ones the paper kept, nor which units in consecutive files are one neuron.''')
after('# %% code claim:table1-rest-rate', '''**Result: reproduced.** The mean rest rate over unit-directions is 75.65 spikes/s in GPi (SD 25.63,
531) and 12.78 in VLa (SD 11.62, 552), both within 10% of 70.1 and 13.5, and GPi is higher (rank
sum p = 1.2e-171). The animals differ slightly in GPi (73.17 and 78.25 spikes/s, p = 0.041), where
the paper reports no difference, and not in VLa (p = 0.53). With the paper's records the means are
64.26 and 13.53 spikes/s.''')
after('# %% code claim:table1-ap-width', '''**Result: reproduced.** Trough-to-peak widths from the filtered traces average 0.247 ms in GPi and
0.509 ms in VLa (532 of 547 units measured), within 10% of 0.24 and 0.50 ms, and GPi widths are
smaller (rank sum p = 2.9e-37). The trace is sampled every 0.041 ms, and the 200 Hz high-pass filter
of the dandiset differs from the paper's 300 Hz.''')
after('# %% code claim:hold-period-ramps', '''**Result: partially reproduced.** 98.5% of GPi and 98.6% of VLa units have a significant
control-period slope in at least one direction, within 10% of 97% and 98% (97.0% and 97.5% at
alpha 0.01), and 49.9% of significant slopes are positive. The slopes of GPi and VLa differ by the
rank sum test (mean -0.598 against 0.233 spikes/s2, p = 0.042), where the paper finds no difference
(means -0.05 and -0.14, p = 0.29); with the paper's records they do not differ (p = 0.19). The
criterion did not define a partial outcome; the first part holds and the second does not.''')
after('# %% code claim:mvt-responsive-fraction', '''**Result: reproduced.** 98.5% of GPi units (264 of 268) and 97.5% of VLa units (272 of 279) respond
in at least one direction. GPi is within 10% of 99%. VLa is within 10% of the text's 94% but not
of Table 1's 88.1%; the criterion accepts either reading. With alpha 0.0001 the fractions with an
increase alone fall to 81.0% and 77.4%.''')
after('# %% code claim:increases-most-common', '''**Result: partially reproduced.** Monophasic increase is the most common form in both areas (GPi
46.9%, VLa 50.9% of responses), and increases make up 58.8% of GPi and 60.2% of VLa changes (746 of
1254 overall, binomial p = 1.9e-11). The GPi values are within 10% of 48.7% and 61.5%; the VLa values
are below 65.3% and 68.8% by more than 10%, also with the paper's records (54.1% and 61.4%).''')
after('# %% code claim:monophasic-more-in-vla', '''**Result: not reproduced.** Monophasic responses are 71.0% in GPi and 76.7% in VLa; the difference
is not significant (chi-squared p = 0.051), and VLa is more than 10% below 88.9%. With the paper's
records the values are 69.0% and 81.2% (p = 0.00036), both within tolerance; the difference comes
with the selection of units.''')
after('# %% code claim:integrated-change-positive', '''**Result: partially reproduced.** The mean integrated change is positive in GPi (3.07 spikes, signed
rank p = 1.1e-10) and in VLa (1.50 spikes, p = 3.7e-18), but both are more than 10% below 3.89 and
1.75. With the paper's records they are 3.42 and 1.97 spikes.''')
after('# %% code claim:fig3a-vla-leads-gpi', '''**Result: not reproduced.** The median onset of all changes is -48 ms in GPi (641 changes) and -67 ms
in VLa (613); GPi is later by 19 ms, but not significantly (rank sum p = 0.079), and the VLa median
is outside -90 +/- 9 ms. In Gaia the medians are equal (-48.5 and -48 ms). With the paper's records
the medians are -49 and -85 ms (p = 0.004), which would meet the criterion; the difference comes
with the selection of units.''')
after('# %% code claim:fig3b-gpi-decr-lag-vla-incr', '''**Result: reproduced.** GPi decreases begin at a median of -29.5 ms (264) and VLa increases at -84 ms
(369), both within tolerance of -27 and -88 ms, and GPi decreases are later (rank sum p = 0.00021).
The lag holds in Gaia (0 against -95 ms, p = 0.0014) and in Isis without significance (-44 against
-81 ms, p = 0.055), and with the paper's records (-36 against -85 ms, p = 0.00069).''')
after('# %% code claim:fig3c-vla-decr-lead-gpi-incr', '''**Result: not reproduced.** GPi increases begin at a median of -69 ms (377) and VLa decreases at -19
ms (244); VLa decreases do not lead (rank sum p = 0.17), and the VLa median is far from -108 ms. In
Gaia VLa decreases come later than GPi increases (12.5 against -75 ms, p = 0.0028). With the paper's
records VLa decreases lead by 13 ms without significance (-86 against -73 ms, p = 0.2).''')
after('# %% code claim:gating-conflict-fraction', '''**Result: reproduced.** 95.4% of the 392,933 GPi-VLa comparisons conflict with gating (96 +/- 9.6%);
95.6% with the paper's records. The number says little: with onsets shuffled across
unit-directions it is 95.1% (95.0 to 95.2), and it follows the width of the gating window (98.0%
for 0 to 20 ms, 86.6% for 0 to 200 ms).''')
after('# %% code claim:directional-units', '''**Result: partially reproduced.** GPi units are directional more often than VLa units (46.2%, 122 of
264, against 24.3%, 66 of 272; chi-squared p = 1.7e-07), but both fractions are more than 10% below
52.9% and 31.3%. With the paper's records they are 48.2% and 26.8%.''')
after('# %% code claim:fig4-ccf-rare', '''**Result: not reproduced.** By the paper's test the peak CCFs of the 338 whole-recording pairs are
larger than those of the jittered controls (KS permutation p = 0.003), and so are those of the 306
movement pairs (p = 0.045); the 298 rest pairs are not (p = 0.705). Significant pairs are few (5.6%,
3.4% and 6.5%, none above 5% by a binomial test, p 0.14 to 0.93), as the paper reports, and their
peaks are mostly positive (15 of 19 whole-recording, 15 of 20 movement), where gating predicts
negative ones. The effect is small: median peak 0.042 against a control median of 0.038.''')
after('# %% code claim:fig4-noise-corr-rare', '''**Result: not reproduced.** Absolute noise correlations exceed those of trial-shuffled controls at
rest and during movement (KS permutation p < 0.001 in both). 10.1% (rest) and 10.8% (movement) of
pair-targets lie outside the shuffled 2.5 to 97.5 percentiles, against 5.4% and 7.2%, or 17.5% and
18.6% of pairs counting either target. Positive and negative correlations are about equally common
(38 and 29 at rest, p = 0.33; 39 and 33 during movement, p = 0.56), as the paper reports.''')
after('# %% code claim:fig5-vla-decrease-after-gpi-bursts', '''**Result: not reproduced.** The population VLa rate does not fall below the control band in 0 to
300 ms after GPi burst onsets (150 pairs; lowest point 2.5% below baseline), burst offsets (150;
1.9%) or pause onsets (110; 1.9%). Per pair, 50.7% show a change in 0 to 100 ms after burst onsets,
43 decreases and 33 increases, against 11.6% in the paper, so this per-pair test is not the
paper's. Bursts here last 67.1 ms on average and pauses 145.3 ms, against 24 and 195 ms in the
paper, so the burst detection also differs from the paper's.''')
after('# %% code claim:behavior-rt-mt', '''**Result: partially reproduced.** Movement durations are longer to the right target (Gaia 0.273
against 0.218 s, Isis 0.204 against 0.175 s) and longer in Gaia, both with p < 1e-4 in the
two-way ANOVA. Reaction times differ between the animals (F = 15.19, p = 0.0001; medians 0.243 and
0.235 to 0.241 s), where the paper finds no difference, and not between directions (p = 0.073).
Movement durations exist for only 32 of the 119 Gaia files.''')

summary='''# %% md
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Data | Outcome |
|---|---|---|
| unit-link | with inputs | reproduced |
| table1-unit-counts | dandiset | not reproduced |
| table1-rest-rate | dandiset | reproduced |
| table1-ap-width | dandiset | reproduced |
| hold-period-ramps | dandiset | partially reproduced |
| mvt-responsive-fraction | dandiset | reproduced |
| increases-most-common | dandiset | partially reproduced |
| monophasic-more-in-vla | dandiset | not reproduced |
| integrated-change-positive | dandiset | partially reproduced |
| fig3a-vla-leads-gpi | dandiset | not reproduced |
| fig3b-gpi-decr-lag-vla-incr | dandiset | reproduced |
| fig3c-vla-decr-lead-gpi-incr | dandiset | not reproduced |
| gating-conflict-fraction | dandiset | reproduced |
| directional-units | dandiset | partially reproduced |
| fig4-ccf-rare | dandiset | not reproduced |
| fig4-noise-corr-rare | dandiset | not reproduced |
| fig5-vla-decrease-after-gpi-bursts | dandiset | not reproduced |
| behavior-rt-mt | dandiset | partially reproduced |
| figs3-emg-onset | elsewhere | blocked: methods underspecified |
| fig1-vla-localization | dandiset | blocked: data missing |
| fig6-simulation | elsewhere | blocked: other |

**How the analysis differs from the paper's.** The units are selected from the dandiset's own
labels, and each file's unit is counted once, because the dandiset does not say which units the
paper kept nor which units in consecutive files are one neuron; this gives about 40% more units
than the paper. The paper's own unit list, linked through the Dryad files, is shown as a variant;
with it, monophasic-more-in-vla and fig3a-vla-leads-gpi would meet their criteria, so those two
outcomes depend on the selection. The detection of responses follows the Methods and the paper's
detection function, but the detrending and the ISI function are implemented here; on the paper's
units they agree with its stored results for 91% (increases) and 81% (decreases) of
unit-directions. Trial exclusion follows the Methods and matches the paper's trial counts for 63%
of unit-directions. Widths are measured on the dandiset's 200 Hz filtered traces. The CCF jitters
the VLa spikes and does not apply the paper's sensitivity exclusion (c0 > 0.3). Burst and pause
detection is a reimplementation of the surprise method and gives longer bursts than the paper's;
its control shifts events within rest. The first run used log10 in the surprise, which gave bursts
of 254 ms; the natural log of the paper's MATLAB is used.

**What was found about the dandiset.** It holds the paper's pre-MPTP GPi and VLa recordings: 364
of the 394 units the paper analysed are among its curated units, and their spike times reproduce
the paper's per-unit activity. It does not identify which units the paper analysed or link a neuron
across consecutive files. Location labels vary in case, 54 Gaia thalamic units are labelled only
"Thalamus" and 33 Isis units have no label or channel; 30 of the paper's units are missing from the
curated tables (some files have none). Every `session_start_time` is two days after the date in
the `session_id`. Error trials are flagged only in files with an `error_onset_time` column (127 of
253), and movement ends are missing from 87 files. One pre-MPTP file has no trials, raw data or
curated units, and one M1 spike train is stored twice. The EMG and the stimulation mapping are not
in the dandiset.

'''
i=s.index('# %% md\n## figs3-emg-onset')
j=s.index('# %% code\nprint(f"Notebook ran in')
blocked=s[i:j]
s=s[:i]+blocked+summary+s[j:]
open('nb_src.py','w').write(s)
EOF
python3 build.py
```

```
75
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('nb_src.py').read()
s=s.replace("the detected response onsets below, which cluster\nbetween about -100 and 0 ms from movement onset, support it.","the detected response onsets below, with medians\nbetween -84 and -19 ms from movement onset, support it.")
s=s.replace("medians 0.243 and\n0.235 to 0.241 s)","medians Gaia 0.243 and\n0.242 s, Isis 0.235 and 0.241 s)")
s=s.replace("""its control shifts events within rest. The first run used log10 in the surprise, which gave bursts
of 254 ms; the natural log of the paper's MATLAB is used.""","""its control shifts events within rest. A first run, not shown here, used log10 in the surprise and
gave bursts far longer than the paper's; the natural log of the paper's MATLAB is used.""")
t='# %% code\nprint(f"Notebook ran in {(time.time() - NB_START) / 60:.1f} min")\n'
assert t in s
s=s.replace(t,'')
s=s.replace('# %% md\n## Summary', t+'\n# %% md\n## Summary')
open('nb_src.py','w').write(s)
EOF
grep -n "Notebook ran\|## Summary\|between -84" nb_src.py; python3 build.py
cd entries/000947-schwab-2020; sed -i 's/which gave bursts ten times longer than the paper.s\n  mean of 24 ms./X/' gpivla.py; python3 - <<'EOF'
p='gpivla.py'; s=open(p).read()
s=s.replace("""(A first run used log10, which gave bursts ten times longer than the paper's
  mean of 24 ms.)""","""(A first run used log10, which gave bursts far longer than the paper's.)""")
open(p,'w').write(s)
EOF
grep -n "first run" gpivla.py
```

```
248:between -84 and -19 ms from movement onset, support it. In 34 of the 163 files with GPi or
1116:print(f"Notebook ran in {(time.time() - NB_START) / 60:.1f} min")
1119:## Summary
75
34:  samples, the first run of 70 consecutive supra-threshold samples as onset, and the offset as a
41:  paper's MATLAB. (A first run used log10, which gave bursts far longer than the paper's.)
```

**Agent**

Now the entry metadata, requirements and README, then lock and run.

**Agent calls Bash**

```bash
cd entries/000947-schwab-2020; printf 'dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\nstatsmodels\n' > requirements.in
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000947-schwab-2020
type: reproduction
title: GPi and VLa activity during reaching in macaques (Schwab et al. 2020)
description: Tests the findings of Schwab, Kase, Zimnik, Rosenbaum, Codianni, Rubin and Turner (2020)
  on the pre-MPTP recordings of dandiset 000947, single units from the internal globus pallidus and
  the ventrolateral anterior thalamus of two monkeys performing a reaching task. It compares rates,
  spike widths, peri-movement responses and their latencies, spike and rate correlations of
  simultaneously recorded pairs, and the effect of GPi bursts and pauses on VLa activity, and links
  the dandiset's units to the paper's own unit list.
license: Apache-2.0
notebooks:
- path: reproduce_schwab_2020.ipynb
  title: Reproducing Schwab et al. (2020) from dandiset 000947
  runtime_minutes: 12
helpers:
- gpivla.py
related:
- id: dandi:000947/0.240510.2211
  relation: uses_data
- id: doi:10.1371/journal.pbio.3000829
  relation: reproduces
EOF
cat ../001453-fouke-2025/entry.yaml | head -3 >/dev/null; cd  && python tools/entry.py lock entries/000947-schwab-2020 && python tools/entry.py check entries/000947-schwab-2020
```

```
wrote entries/000947-schwab-2020/requirements.lock.txt
0 error(s)
```

**Agent**

Check passes. Running the entry from a clean environment now (about 12 to 15 minutes).

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000947-schwab-2020 2>&1 | tail -30
```

```
Installed kernelspec registry-000947-schwab-2020 in executed/000947-schwab-2020/.venv/share/jupyter/kernels/registry-000947-schwab-2020
0 error(s)
pass  reproduce_schwab_2020.ipynb  (691 s)

real	11m42.157s
user	5m0.210s
sys	0m10.574s
```

**Agent**

Passed in 691 s. Now confirming that the executed outputs match every number in the conclusions.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import nbformat
nb=nbformat.read('executed/000947-schwab-2020/reproduce_schwab_2020.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': out.append(o['text'])
            if o.get('output_type')=='error': print('ERROR', o['ename'])
open('/tmp/claude-1001/exec_out.txt','w').write('\n'.join(out))
EOF
diff <(grep -v "Pandas4\|pct = (100\|in [0-9]* s\|([0-9]* s)\|Notebook ran\|counts\[\|assign(total" $TMPDIR/run5.log) <(grep -v "in [0-9]* s\|([0-9]* s)\|Notebook ran" $TMPDIR/exec_out.txt) | head -40; grep "Notebook ran\|loaded the" $TMPDIR/exec_out.txt
```

```
0a1
> 
29a31
> 
57c59
<    [('pre-MPTP-I-170518-2', '6'), ('pre-MPTP-I-170518-2', '7')]
---
>    [('pre-MPTP-I-170518-2', '6'), ('pre-MPTP-I-170518-2', '7')] labels ['M1-S', 'M1-S'] channels [np.float64(40.0), np.float64(43.0)] identical: True
58a61
> 
74a78
> 
85a90
> 
90a96,97
> 
> 
142a150
> 
163a172
[... 22 more lines not kept]
```

**Agent**

Executed outputs match the debug run exactly. Now writing the attempt record and the entry README.

**Agent calls Write**

```json
{
 "file_path": "attempts/000947-schwab-2020-01.yaml",
 "content": "schema_version: 1\nid: 000947-schwab-2020-01\ndandiset: \"000947\"\ndandiset_version: 0.240510.2211\npaper: doi:10.1371/journal.pbio.3000829\ndate: 2026-10-18\nentry: 000947-schwab-2020\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\ninputs:\n- what: The paper's per-unit result files Gaia_Analy.mat and Isis_Analy.mat, which name each analysed\n    unit by recording file, channel and sort letter and store its peri-movement SDF, trials and\n    detected onsets. Used for the link claim unit-link and for variants with the paper's own unit\n    list; no outcome on the paper's findings rests on them. The analysis code read for the method\n    (PeriEventChange_SDF_pctchng.m, Fig2_3_S8_S9.m, Fig4_S10to13.m, Fig5_S14.m, FigS2.m, FigS3.m) is\n    from the same deposit.\n  source: Dryad doi:10.5061/dryad.0cfxpnvxm (version of 2020-08-24), read from its Zenodo mirror,\n    record 4000719 (https://zenodo.org/records/4000719), as the Dryad download API requires a token\noutcomes:\n- claim: unit-link\n  outcome: reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:unit-link\n  notes: Records are matched by file, channel id and sort letter. 364 of the 394 records the paper's\n    code keeps (92.4%) are found in every file they span (Isis GPi 104 of 104, Gaia GPi 95 of 105,\n    Gaia VLa 60 of 66, Isis VLa 105 of 119). For 724 matched unit-directions the SDF from the\n    dandiset correlates with the stored SDF at a median r of 0.9992, above 0.9 for 94.6%. Valid trial\n    counts equal the paper's for 62.6%. Detection agrees on the presence of an increase for 90.9% and\n    of a decrease for 80.7% of unit-directions. 25 matched units the paper calls VLa are labelled\n    \"Thalamus\" in the dandiset, and 97 records span 2 to 5 files. On the side of the outside data,\n    the paper's list gives 209 GPi and 185 VLa units, as Table 1 does.\n  deviations:\n  - Trial exclusion follows the Methods (6 median absolute differences from the mean); the paper's\n    stored trial counts differ for 37% of unit-directions, by a median of 0.\n- claim: table1-unit-counts\n  outcome: not_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:table1-unit-counts\n  measured:\n  - 268\n  - 279\n  notes: The dandiset rule gives 268 GPi units (Gaia 137, Isis 131) and 279 VLa units (78 and 201),\n    against 209 and 185 (218 in the text). Counting the same channel and sort letter on one day once\n    gives 132 and 186; the paper's records found in the dandiset are 199 and 165. 518 of the 547\n    units are in files the paper used. The dandiset holds more units than the paper analysed and\n    does not say which were kept or which units in consecutive files are one neuron.\n  deviations:\n  - Units are selected by the dandiset's location labels and the Methods' rate and trial criteria;\n    the paper's anatomical criteria (within 0.5 mm of an M1-responsive site, the VLa border) cannot\n    be applied from the files.\n  - Each file's unit is counted once; the paper pools a neuron recorded over consecutive files.\n- claim: table1-rest-rate\n  outcome: reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:table1-rest-rate\n  measured:\n  - 75.65\n  - 12.78\n  notes: Mean rest rate over unit-directions 75.65 spikes/s in GPi (531) and 12.78 in VLa (552), GPi\n    higher with rank sum p = 1.2e-171. The animals differ slightly in GPi (73.17 and 78.25, p =\n    0.041), where the paper reports no difference; not in VLa (p = 0.53). With the paper's records\n    64.26 and 13.53.\n  deviations:\n  - Unit selection by the dandiset rule (see table1-unit-counts).\n- claim: table1-ap-width\n  outcome: reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:table1-ap-width\n  measured:\n  - 0.247\n  - 0.509\n  notes: Mean trough-to-peak width 0.247 ms in GPi and 0.509 ms in VLa, 532 of 547 units measured,\n    rank sum p = 2.9e-37.\n  deviations:\n  - Widths come from the dandiset's 200 Hz high-pass filtered traces (the paper filtered at 300 Hz)\n    and from the spikes in one stored chunk (about 3.2 s, median 273 spikes) per file and series.\n- claim: hold-period-ramps\n  outcome: partially_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:hold-period-ramps\n  measured:\n  - 98.5\n  - 98.6\n  notes: 98.5% of GPi and 98.6% of VLa units have a significant control-period slope (97.0% and 97.5%\n    at alpha 0.01), and 49.9% of significant slopes are positive. GPi and VLa slopes differ (mean\n    -0.598 against 0.233 spikes/s2, rank sum p = 0.042), where the paper finds no difference (p =\n    0.29); with the paper's records they do not (p = 0.19).\n  deviations:\n  - The criterion did not define a partial outcome; the outcome is partial because the first part\n    (ramps are common) holds and the second (no difference between areas) does not.\n- claim: mvt-responsive-fraction\n  outcome: reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:mvt-responsive-fraction\n  measured:\n  - 98.5\n  - 97.5\n  notes: 264 of 268 GPi (98.5%) and 272 of 279 VLa units (97.5%) respond in at least one direction.\n    VLa matches the text's 94% but not Table 1's 88.1%; the criterion accepts either reading. With\n    alpha 0.0001 the fractions with an increase alone are 81.0% and 77.4%.\n  deviations:\n  - The paper gives 88.1% (Table 1) and 94% (text) for VLa; both readings were listed and only the\n    text's matches.\n- claim: increases-most-common\n  outcome: partially_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:increases-most-common\n  measured:\n  - 46.9\n  - 50.9\n  - 58.8\n  - 60.2\n  notes: Monophasic increase is the most common form in GPi (46.9%) and VLa (50.9%), and increases\n    are 58.8% and 60.2% of changes (746 of 1254 overall, binomial p = 1.9e-11). The GPi values are\n    within tolerance; the VLa values are below 65.3% and 68.8% by more than 10%, also with the paper's\n    records (54.1% and 61.4%).\n  deviations:\n  - Detrending of the control period and the ISI function are implemented here from the Methods;\n    the paper's own implementation of these steps is not in its deposit.\n- claim: monophasic-more-in-vla\n  outcome: not_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:monophasic-more-in-vla\n  measured:\n  - 71.0\n  - 76.7\n  notes: Monophasic responses are 71.0% in GPi and 76.7% in VLa, chi-squared p = 0.051, and VLa is\n    outside tolerance. With the paper's records 69.0% and 81.2% (p = 0.00036), both within tolerance,\n    so the outcome depends on the selection of units.\n  deviations:\n  - Unit selection by the dandiset rule (see table1-unit-counts).\n- claim: integrated-change-positive\n  outcome: partially_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:integrated-change-positive\n  measured:\n  - 3.07\n  - 1.50\n  notes: The mean integrated change is positive in GPi (3.07 spikes, signed rank p = 1.1e-10) and VLa\n    (1.50 spikes, p = 3.7e-18), both more than 10% below 3.89 and 1.75. With the paper's records 3.42\n    and 1.97.\n  deviations:\n  - Table 1 gives the unit as spikes x 10^3; the code's computation gives spikes, the reading used.\n- claim: fig3a-vla-leads-gpi\n  outcome: not_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:fig3a-vla-leads-gpi\n  measured:\n  - -48\n  - -67\n  notes: Median onsets of all changes are -48 ms in GPi (641) and -67 ms in VLa (613); GPi is later by\n    19 ms without significance (rank sum p = 0.079), and the VLa median is outside tolerance. In\n    Gaia the medians are equal (-48.5 and -48 ms). With the paper's records -49 and -85 ms (p =\n    0.004), which meets the criterion, so the outcome depends on the selection of units.\n  deviations:\n  - Unit selection by the dandiset rule (see table1-unit-counts).\n- claim: fig3b-gpi-decr-lag-vla-incr\n  outcome: reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:fig3b-gpi-decr-lag-vla-incr\n  measured:\n  - -29.5\n  - -84\n  notes: GPi decreases begin at a median of -29.5 ms (264) and VLa increases at -84 ms (369), rank\n    sum p = 0.00021. Gaia 0 against -95 ms (p = 0.0014), Isis -44 against -81 ms (p = 0.055); with\n    the paper's records -36 against -85 ms (p = 0.00069).\n- claim: fig3c-vla-decr-lead-gpi-incr\n  outcome: not_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:fig3c-vla-decr-lead-gpi-incr\n  measured:\n  - -19\n  - -69\n  notes: VLa decreases begin at a median of -19 ms (244) and GPi increases at -69 ms (377); VLa does\n    not lead (rank sum p = 0.17). In Gaia VLa decreases come later (12.5 against -75 ms, p = 0.0028).\n    With the paper's records VLa leads by 13 ms without significance (-86 against -73 ms, p = 0.2).\n    The paper itself gives -62 ms for GPi increases here and -76 ms in Table 1.\n  deviations:\n  - The ISI-based detection finds more decreases than the paper's on the same units (330 against 286\n    on the linked units), which weighs on this comparison.\n- claim: gating-conflict-fraction\n  outcome: reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:gating-conflict-fraction\n  measured: 95.4\n  notes: 95.4% of 392,933 comparisons conflict with gating (95.6% with the paper's records). With\n    onsets shuffled across unit-directions the fraction is 95.1% (95.0 to 95.2), so the number does\n    not distinguish the data from random onsets; it follows the gating window (98.0% for 0 to 20 ms,\n    86.6% for 0 to 200 ms).\n- claim: directional-units\n  outcome: partially_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:directional-units\n  measured:\n  - 46.2\n  - 24.3\n  notes: 122 of 264 responsive GPi units (46.2%) and 66 of 272 VLa units (24.3%) are directional,\n    chi-squared p = 1.7e-07; both fractions are more than 10% below 52.9% and 31.3%. With the paper's\n    records 48.2% and 26.8%.\n- claim: fig4-ccf-rare\n  outcome: not_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:fig4-ccf-rare\n  notes: By the KS permutation test the peak CCFs exceed those of jittered controls over whole\n    recordings (338 pairs, p = 0.003) and during movement (306 pairs, p = 0.045), not at rest (298\n    pairs, p = 0.705). Significant pairs are 5.6%, 3.4% and 6.5%, none above 5% by a binomial test,\n    and mostly positive (15 of 19 whole, 15 of 20 movement). The shift is small (median peak 0.042\n    against a control median of 0.038). The part of the statement that correlations are rare holds;\n    the part that peaks are not larger than controls does not.\n  deviations:\n  - The paper's exclusion of pairs with a minimum detectable correlation above 0.3 was not applied\n    (its simulation is not in the deposit), so more pairs enter (338 against 427 in the paper, from a\n    different unit selection).\n  - Only VLa spikes are jittered; the Methods do not say which train.\n- claim: fig4-noise-corr-rare\n  outcome: not_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:fig4-noise-corr-rare\n  notes: Absolute noise correlations exceed trial-shuffled controls at rest and during movement (KS\n    permutation p < 0.001 in both). 10.1% and 10.8% of pair-targets (17.5% and 18.6% of pairs) are\n    significant against 5.4% and 7.2% in the paper. Signs are balanced (38 and 29 at rest, p = 0.33;\n    39 and 33 during movement, p = 0.56), as the paper reports.\n  deviations:\n  - The paper's test statistic for noise correlations is not printed in its code; the KS permutation\n    test on absolute correlations was fixed in the criterion before the analysis.\n  - Significance uses the 2.5 to 97.5 percentiles of the shuffles pooled over pairs, as the paper's\n    code does per time point.\n- claim: fig5-vla-decrease-after-gpi-bursts\n  outcome: not_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:fig5-vla-decrease-after-gpi-bursts\n  notes: The population VLa rate does not fall below the control band within 300 ms of GPi burst onsets\n    (150 pairs, lowest point 2.5% below baseline), burst offsets (150, 1.9%) or pause onsets (110,\n    1.9%). Bursts here last 67.1 ms on average and pauses 145.3 ms, against 24 and 195 ms in the\n    paper, and 50.7% of pairs show a change after burst onsets against 11.6% in the paper, so the\n    detection and the per-pair test differ from the paper's.\n  deviations:\n  - Burst and pause detection is a reimplementation of the Legendy and Salcman surprise method; the\n    paper's implementation is not in its deposit (Fig5_S14.m plots stored results).\n  - A first run used log10 in the surprise and gave bursts far longer than the paper's; the natural\n    log, as in the Methods' formula in the paper's MATLAB, was then used. The claim's outcome was not\n    significant in both runs.\n  - The control shifts all events of a pair by one random offset of 2 to 20 s and uses VLa rate in rest\n    samples only; the paper does not describe its control for Fig 5.\n- claim: behavior-rt-mt\n  outcome: partially_reproduced\n  notebook: reproduce_schwab_2020.ipynb\n  output: claim:behavior-rt-mt\n  notes: Movement durations are longer to the right target (Gaia 0.273 against 0.218 s, Isis 0.204\n    against 0.175 s) and longer in Gaia (both p < 0.0001). Reaction times differ between the animals\n    (F = 15.19, p = 0.0001) where the paper finds none, and not between directions (p = 0.073).\n  deviations:\n  - Movement durations exist for 32 of 119 Gaia files only.\n  - The observations are file and direction medians (500 for RT); the paper's ANOVA has 452 error\n    degrees of freedom and does not say what its observations are.\n- claim: figs3-emg-onset\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: The EMG is not in the dandiset; it is in the paper's Dryad deposit (S3_EMGdata files). The\n    Methods do not say how the onset of the EMG change was determined, and FigS3.m only plots the\n    trial-averaged EMG with reaction times, so the onsets cannot be recomputed by the paper's method.\n- claim: fig1-vla-localization\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The stimulation mapping (responses to GPi, SCP and motor cortex stimulation along electrode\n    tracks) is not in the dandiset, which holds task recordings only, nor in the Dryad deposit. The\n    files give electrode coordinates and location labels, which do not test the claim.\n- claim: fig6-simulation\n  outcome: blocked\n  blocked_by: other\n  notes: A simulation that uses no recorded data. The Dryad deposit holds its output (Data_Fig6.mat)\n    and a plotting script, but not the model thalamocortical cell or the generator of correlated GPi\n    spike trains; reimplementing the model of the paper's reference 103 in XPPAUT was not attempted.\nfindings:\n- kind: selection_undocumented\n  statement: The dandiset holds more GPi and VLa units than the paper analysed (268 GPi and 279 VLa\n    units under its own labels and the Methods' rate criteria, against 209 and 185) and does not say\n    which units the paper kept. The paper's unit list is only in its Dryad deposit.\n- kind: identifier_missing\n  statement: No identifier links a neuron recorded over consecutive files. 97 of the paper's 394\n    units span 2 to 5 files, and the dandiset stores them as separate units.\n- kind: metadata_error\n  statement: Location labels are inconsistent. GPi and VLa are written GPI and VLA in some files, 54\n    Gaia thalamic units are labelled only \"Thalamus\" (25 of them are VLa units in the paper), and 33\n    Isis units have an empty location and no channel id.\n- kind: data_missing\n  statement: 30 of the 394 units the paper analysed are not among the curated units. Some files have\n    no curated units at all (21 of 254 pre-MPTP files, for example G-140813-2), though their sorted\n    clusters are in processing/ecephys/units, which has no channel or sort letter to match them.\n- kind: metadata_error\n  statement: In all 254 pre-MPTP files the session_start_time is two days after the date in the\n    session_id.\n- kind: metadata_insufficient\n  statement: Sort labels are letters in some files and numbers in others, and the unit quality column\n    is missing from some files and holds free text (for example \"B -> C\") in others, without a\n    description of its values.\n- kind: other\n  statement: Error trials are flagged only in files with an error_onset_time column (127 of 253 files\n    with trials), and movement ends are missing from 87 files, 87 of them Gaia, so the Methods' trial\n    exclusion can be applied only in part.\n- kind: format_error\n  statement: One pre-MPTP file (I-160616-4) has no trials table, no raw data and no curated units, and\n    one spike train is stored twice in I-170518-2, as two M1-S units on channels 40 and 43.\n- kind: other\n  statement: The NWB files name the paper only by its bioRxiv preprint (doi:10.1101/546598); the\n    dandiset metadata names the published paper.\n- kind: data_missing\n  statement: The EMG of S3 Fig and the stimulation mapping of Fig 1 are not in the dandiset; the EMG is\n    in the paper's Dryad deposit and the mapping is not public.\n- kind: paper_inconsistency\n  statement: The Results give 218 VLa units and 94% responsive VLa units where Table 1 gives 185 and\n    88.1%; the text gives median onsets of -62 ms for GPi increases and -108 ms for VLa decreases\n    (Fig 3C) where Table 1 gives -76 and -95.5 ms.\n"
}
```

```
File created successfully at: attempts/000947-schwab-2020-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml,re
p='attempts/000947-schwab-2020-01.yaml'; s=open(p).read()
s=s.replace("""and movement ends are missing from 87 files, 87 of them Gaia, so the Methods' trial
    exclusion can be applied only in part.""","""and movement ends are missing from 87 files, all of them Gaia (32 of 119 Gaia files have them), so
    the Methods' trial exclusion can be applied only in part.""")
open(p,'w').write(s)
d=yaml.safe_load(s)
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print('COLON', path, x[:80])
walk(d)
for f in ['claims/000947/10.1371-journal.pbio.3000829.yaml']: walk(yaml.safe_load(open(f)))
print('ok')
EOF
cd $TMPDIR; python3 - <<'EOF'
s=open('nb_src.py').read()
old="""Error trials are flagged only in files with an `error_onset_time` column (127 of
253), and movement ends are missing from 87 files."""
assert old in s
s=s.replace(old,"""Error trials are flagged only in files with an `error_onset_time` column (84 and 43
files in the column table), and movement ends are in only 32 of the 119 Gaia files.""")
open('nb_src.py','w').write(s)
EOF
python3 build.py
```

```
ok
75
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/000947-schwab-2020/README.md",
 "content": "# Schwab, Kase, Zimnik, Rosenbaum, Codianni, Rubin & Turner (2020) from dandiset 000947\n\nTests the findings of [Schwab et al. (2020)](https://doi.org/10.1371/journal.pbio.3000829) on the\npre-MPTP recordings of [DANDI:000947](https://dandiarchive.org/dandiset/000947/0.240510.2211):\nsingle units from the internal globus pallidus (GPi) and the ventrolateral anterior thalamus (VLa)\nof two monkeys performing a reaching task.\n\n| Claim | Outcome |\n|---|---|\n| The paper's units can be found in the dandiset and their activity reproduced | Reproduced |\n| 209 GPi and 185 VLa units | Not reproduced |\n| Rest rate GPi 70.1, VLa 13.5 spikes/s | Reproduced |\n| Spike width GPi 0.24, VLa 0.50 ms | Reproduced |\n| Hold-period ramps in 97% and 98% of units, no difference between areas | Partially reproduced |\n| Nearly all units respond around movement | Reproduced |\n| Monophasic increases are the most common response | Partially reproduced |\n| Monophasic responses more common in VLa | Not reproduced |\n| Integrated change positive in both areas | Partially reproduced |\n| GPi changes begin later than VLa changes (Fig 3A) | Not reproduced |\n| GPi decreases lag VLa increases (Fig 3B) | Reproduced |\n| VLa decreases precede GPi increases (Fig 3C) | Not reproduced |\n| 96% of response comparisons conflict with gating | Reproduced |\n| GPi units more often directional than VLa units | Partially reproduced |\n| GPi-VLa spike correlations no larger than controls (Fig 4A-F) | Not reproduced |\n| GPi-VLa noise correlations no larger than controls (Fig 4G-H) | Not reproduced |\n| VLa rate decreases after GPi bursts and pauses (Fig 5) | Not reproduced |\n| Reaction times and movement durations (S2 Fig) | Partially reproduced |\n| EMG onsets (S3 Fig) | Blocked: methods underspecified |\n| Localization of VLa by stimulation (Fig 1) | Blocked: data missing |\n| Simulations (Fig 6) | Blocked: other |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe units are selected from the dandiset's own labels, which gives more units than the paper\nanalysed; the paper's own unit list, from its Dryad deposit, is shown as a variant, and two\noutcomes (monophasic responses, Fig 3A) would differ with it. The attempt record, with the reasons\nand the differences from the paper's method, is\n[`attempts/000947-schwab-2020-01.yaml`](../../attempts/000947-schwab-2020-01.yaml).\n\n- `reproduce_schwab_2020.ipynb`: the analysis. It takes about 12 minutes, about 3 of them streaming\n  the files and another 3 reading the filtered traces for the spike widths.\n- `gpivla.py`: loading the files, valid trials, spike density and ISI functions, the detection of\n  peri-movement changes, CCFs with jittered controls, burst and pause detection, and spike widths.\n  Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/000947-schwab-2020/README.md (file state is current in your context — no need to Read it back)
```

**Agent**

Final lock, check and run, then the handover.

**Agent calls Bash**

```bash
python tools/entry.py lock entries/000947-schwab-2020 && python tools/entry.py all entries/000947-schwab-2020 2>&1 | grep -v "kernelspec\|^Resolved\|^Installed\|^ +" | tail -15
```

```
wrote entries/000947-schwab-2020/requirements.lock.txt
0 error(s)
pass  reproduce_schwab_2020.ipynb  (687 s)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat
nb=nbformat.read('executed/000947-schwab-2020/reproduce_schwab_2020.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': out.append(o['text'])
            if o.get('output_type')=='error': print('ERROR', o['ename'])
open('/tmp/claude-1001/exec_out2.txt','w').write('\n'.join(out))
EOF
diff <(grep -v "in [0-9]* s\|([0-9]* s)\|Notebook ran" $TMPDIR/exec_out.txt) <(grep -v "in [0-9]* s\|([0-9]* s)\|Notebook ran" $TMPDIR/exec_out2.txt) && echo SAME; grep "Notebook ran" $TMPDIR/exec_out2.txt; python tools/entry.py handover entries/000947-schwab-2020; ls executed/000947-schwab-2020/handover/; git status --short
```

```
148a149
> 
174d174
< 
334a335
> 
337d337
< 
344a345
> 
347d347
< 
Notebook ran in 11.3 min
wrote executed/000947-schwab-2020/handover
10.1371-journal.pbio.3000829.yaml
gpivla.py
reproduce_schwab_2020.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
echo $(( ($(date +%s) - $(cat $TMPDIR/start)) / 60 )) min; ls -la scripts .idea .vscode 2>&1 | head; git log -1 --format=%cd
```

```
117 min
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 05:04 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 05:04 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 05:04 scripts
Sun Oct 18 01:09:01 2026 -0400
```

**Agent**

I did steps 1 to 6 for dandiset 000947 and Schwab et al. 2020. The entry passes `check` and runs from a clean environment in 687 s, and the handover is built in `executed/000947-schwab-2020/handover/`. I did not verify my own work, commit, or push. I used the paper's full text: it is open access in PLOS Biology, and I saved the JATS XML and a text copy under `paper/`. I pinned 0.240510.2211 because the paper cites no DANDI version and this is the only published version.

**1. Outcomes**

Of the 18 tested claims, 6 are reproduced, 5 partially reproduced and 7 not reproduced; 3 are blocked.

| Claim | Data | Outcome |
|---|---|---|
| unit-link | with_inputs | reproduced |
| table1-unit-counts | dandiset | not reproduced |
| table1-rest-rate | dandiset | reproduced |
| table1-ap-width | dandiset | reproduced |
| hold-period-ramps | dandiset | partially reproduced |
| mvt-responsive-fraction | dandiset | reproduced |
| increases-most-common | dandiset | partially reproduced |
| monophasic-more-in-vla | dandiset | not reproduced |
| integrated-change-positive | dandiset | partially reproduced |
| fig3a-vla-leads-gpi | dandiset | not reproduced |
| fig3b-gpi-decr-lag-vla-incr | dandiset | reproduced |
| fig3c-vla-decr-lead-gpi-incr | dandiset | not reproduced |
| gating-conflict-fraction | dandiset | reproduced |
| directional-units | dandiset | partially reproduced |
| fig4-ccf-rare | dandiset | not reproduced |
| fig4-noise-corr-rare | dandiset | not reproduced |
| fig5-vla-decrease-after-gpi-bursts | dandiset | not reproduced |
| behavior-rt-mt | dandiset | partially reproduced |
| figs3-emg-onset | elsewhere | blocked: methods_underspecified |
| fig1-vla-localization | dandiset | blocked: data_missing |
| fig6-simulation | elsewhere | blocked: other |

Two outcomes depend on which units are selected. The claims are judged on units chosen from the dandiset's own labels. With the paper's own unit list, monophasic-more-in-vla and fig3a-vla-leads-gpi would meet their criteria.

**2. What the dandiset holds**
- It has the paper's data. 364 of the 394 units the paper analysed are among its curated units. For matched units, activity computed from the dandiset matches the paper's stored per-unit activity (median r = 0.9992).
- It does not say which units the paper used. Its own labels give 268 GPi and 279 VLa units, against 209 and 185 in the paper.
- No identifier follows a neuron across consecutive files. 97 of the paper's units span 2 to 5 files.
- Location labels are inconsistent: GPI/VLA appear alongside GPi/VLa, 54 Gaia units are labelled only "Thalamus", and 33 Isis units have no label and no channel.
- 30 of the paper's units are missing from the curated tables, and 21 pre-MPTP files have no curated units at all.
- In every file, `session_start_time` is two days after the date in `session_id`.
- Error trials are flagged in only 127 of the 253 files with trials, and 87 Gaia files lack movement ends.
- One pre-MPTP file is empty, and one M1 spike train is stored twice.
- The EMG and the stimulation mapping are not in the dandiset.
- The paper contradicts itself: it gives 218 VLa units in the text and 185 in Table 1, and its Fig 3C latencies differ from Table 1.

**3. Where the protocol was unclear, wrong or missing something**
1. **Paper's unit list as an outside input.** The Dryad files list the paper's units, which is a selection, not names for codes. I used it only in a `with_inputs` link claim and in variants. Every claim on the findings is judged on a unit selection rule built from the dandiset alone and fixed in the claims file.
2. **Dryad download blocked.** Dryad's API needs a token. I read the identical deposit from its Zenodo mirror (record 4000719) and recorded that.
3. **No clean null for the clock check.** The protocol does not say what control to use for spikes plus a trial table. Shifting labels by one trial is not a null, because the previous trial's target affects activity. A 1 s offset also fails, because activity while holding at the target depends on the target. I used permuted labels and reported the offset honestly.
4. **Simulation claim category.** The protocol has no data category for a simulation. I set Fig 6 to `data: elsewhere` (its output is on Dryad) and blocked it as `other`.
5. **No partial outcome defined.** For hold-period-ramps the criterion only defined "reproduced". One part holds and one fails, so I recorded it as partially reproduced and noted this as a deviation.
6. **Method error found after a first run.** The first run computed the burst surprise with log10. Bursts came out about ten times longer than the paper's, so I switched to the natural log (MATLAB's `log`). The outcome was not significant in both runs, and the switch is in the deviations.
7. **Control not as stated.** My first burst control did not keep the shifted events in rest periods, though the criterion said it would. I fixed it before writing the conclusions.
8. **Chance level for a reported fraction.** The protocol does not cover a number that matches chance. The paper's 96% gating-conflict figure equals what shuffled onsets give (95.1%). I recorded the claim as reproduced and said in the notes that the number does not tell the data from random onsets.

**4. Runtime and failures**
- The notebook takes about 11.5 min: 3.3 min streaming files, about 3 min reading filtered traces for spike widths.
- The session took about 2 hours.
- Nothing failed in the final run. A Zenodo search command was denied by the permission system; I reran it without the `rm` it included.
- Untracked entries now sit in the repository root (`.bashrc`, `.idea`, `scripts` and others). The three I checked are character devices created at 05:04, before my first command, so they look like sandbox mounts. I left them alone, but they should not be committed.

Files are in `entries/000947-schwab-2020/`:
- `reproduce_schwab_2020.ipynb`
- `gpivla.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

Also new:
- `claims/000947/10.1371-journal.pbio.3000829.yaml`
- `attempts/000947-schwab-2020-01.yaml`

## End of run

97 turns, 117 minutes, result: success.
