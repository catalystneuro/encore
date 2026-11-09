# 000463 · author · run 41034930656

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs claims/000463 paper entries | head -50; wc -l docs/*.md README.md
```

```
Fri Oct 30 09:42:26 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
[... 67 more lines not kept]
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

**Agent calls Bash**

```bash
cat README.md; sed -n 1,271p docs/design.md | head -150; cat claims/000463/*.yaml; ls paper
```

```
<persisted-output>
Output too large (75.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9b593e3c-7b21-408f-bc3d-bd2954749c3c/tool-results/baeliiuww.txt

Preview (first 2KB):
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
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000463/*.yaml; ls -la paper
```

```
<persisted-output>
Output too large (61KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9b593e3c-7b21-408f-bc3d-bd2954749c3c/tool-results/b14u1ytio.txt

Preview (first 2KB):
# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025, on dandiset 000463.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record as served by PubMed Central (PMC12139594), full text with
# Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt). The
# paper has no supplement. No PDF was provided, so the dSTTC equation of the Methods, which the
# text drops, could not be read (see open details). The paper links no analysis code; none was read.
#
# Which data. The paper says its data are at DANDI 000946 ("All experimental data has been made
# public in a repository at the DANDI Archive (https://dandiarchive.org/dandiset/000946)").
# Dandiset 000463 is titled "Electrophysiological Recordings in Anesthetized Rats in the Primary
# Somatosensory Cortex with Phased Ultrasound Array Stimulation"; its description cites this paper,
# speaks of S1 recordings with 32-channel NeuroNexus electrodes under 2% isoflurane, testing
# "different intensities and PRFs", stimulation every 2.5 s, 200 or 500 trials per recording, and
# its summary lists 4 subjects. Which of the paper's experiments it holds (S1 only, or S1 with POm,
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025, on dandiset 000463.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record as served by PubMed Central (PMC12139594), full text with
6	# Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt). The
7	# paper has no supplement. No PDF was provided, so the dSTTC equation of the Methods, which the
8	# text drops, could not be read (see open details). The paper links no analysis code; none was read.
9	#
10	# Which data. The paper says its data are at DANDI 000946 ("All experimental data has been made
11	# public in a repository at the DANDI Archive (https://dandiarchive.org/dandiset/000946)").
12	# Dandiset 000463 is titled "Electrophysiological Recordings in Anesthetized Rats in the Primary
13	# Somatosensory Cortex with Phased Ultrasound Array Stimulation"; its description cites this paper,
14	# speaks of S1 recordings with 32-channel NeuroNexus electrodes under 2% isoflurane, testing
15	# "different intensities and PRFs", stimulation every 2.5 s, 200 or 500 trials per recording, and
16	# its summary lists 4 subjects. Which of the paper's experiments it holds (S1 only, or S1 with POm,
17	# or the AC group) is the author's to find; DANDI 000946 is named here as the paper's own deposit.
18	#
19	# Data the paper used, as it reports them. Male Wistar rats (Hsd WI, Envigo), 250 to 350 g, 3 to 6
20	# months, under isoflurane (2%, 0.4 to 0.6 L/min). Main group N = 16 rats with two 32-channel
[... 768 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "offset": 789
}
```

```
789	    p: 0.02
790	  criterion: As fig10a-feedback-s1rsu-pomrsu for dSTTC from POm RSUs to S1 FSUs, one-tailed
791	    greater at p < 0.05. The absence part is judged on the same test for S1 RSU to POm FSU and POm
792	    RSU to S1 RSU during 0 to 67 ms, direction by O5, reproduced when neither is significant.
793	    Reproduced when both parts hold; partially reproduced when one holds.
794	- id: fig10a-post-decrease
795	  statement: After 3000 Hz PRF sonication, the correlation from S1 RSUs to POm FSUs and from POm
796	    RSUs to S1 RSUs decreases significantly.
797	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 1; Figure 10A
798	  quote: Postsonication, we found the correlation from S1 RSUs to POm FSUs and POm RSUs to S1 RSUs
799	    significantly decreased, representing the desynchronization of spikes
800	  criterion: The 3000 Hz, 60% DC sessions, dSTTC (M5, O6, O7) from S1 RSUs to POm FSUs and from POm
801	    RSUs to S1 RSUs. The paper does not name the postsonication window or give the p-values; the
802	    readings are each 67 ms window from 67 to 268 ms, and 201 to 268 ms, the postsonication
803	    window of the rate analyses. One-tailed less against prestimulation at p < 0.05 (M6).
804	    Reproduced when both directions are significant in at least one common window; partially
805	    reproduced when one is.
806	- id: fig10b-30hz-dsttc
807	  statement: With 30 Hz PRF, S1 RSUs show a time-locked increase in correlation to POm FSUs, while
808	    POm RSUs show decreased correlation to S1 FSUs during sonication.
[... 245 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,120p docs/archives.md; ls entries/001453-fouke-2025 claims/001453; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in
```

```
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

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 139 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000463/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000463/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000463/versions/" | python -c "import json,sys; [print(r['version'],r['asset_count'],r['size'],r['created']) for r in json.load(sys.stdin)['results']]"; curl -s "https://api.dandiarchive.org/api/dandisets/000463/versions/0.250829.1248/" > meta.json; python -c "
import json; m=json.load(open('meta.json'))
print(m['description']); print(m.get('relatedResource')); print(json.dumps(m.get('assetsSummary'),indent=0)[:2000]); print(m.get('citation')); print(m.get('doi'))"; curl -s "https://api.dandiarchive.org/api/dandisets/000463/versions/0.250829.1248/assets/?page_size=100" | python -c "import json,sys; [print(r['path'],r['size'],r['asset_id']) for r in json.load(sys.stdin)['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && source env/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas 2>&1 | tail -2; python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > probe.py <<'EOF'
import h5py, remfile, sys, requests
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
r=requests.head(url,allow_redirects=True); u=r.url
f=h5py.File(remfile.File(u),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name,obj.shape,obj.dtype,dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
    else:
        a={k:v for k,v in obj.attrs.items() if k not in('namespace','object_id')}
        print(name+'/',a)
f.visititems(show)
for k in ['session_description','session_start_time','general/experiment_description','general/notes','general/protocol','general/stimulus']:
    try:
        print(k, f[k][()] if k in f else f.attrs.get(k))
    except Exception as e: print(k,e)
EOF
python probe.py 2e6b590a-a2a4-4455-bb9b-45cc3d7d7cc0 2>&1 | head -150
```

```
acquisition/ {}
acquisition/ElectricalSeries/ {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries/data (12773376, 32) float32 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/ElectricalSeries/electrodes (32,) int64 {'description': 'all electrodes', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
acquisition/ElectricalSeries/starting_time () float64 {'rate': np.float64(24414.0625), 'unit': 'seconds'}
analysis/ {}
file_create_date (2,) object {}
general/ {}
general/devices/ {}
general/devices/array/ {'description': 'A1x32-Poly3-10mm-50-177-A32', 'manufacturer': 'Neuronexus', 'neurodata_type': 'Device'}
general/extracellular_ephys/ {}
general/extracellular_ephys/electrodes/ {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name'], dtype=object), 'description': 'all electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group_name (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/id (32,) int64 {'neurodata_type': 'ElementIdentifiers'}
general/extracellular_ephys/electrodes/imp (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/location (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/x (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, json
V="0.250829.1248"
assets=requests.get(f"https://api.dandiarchive.org/api/dandisets/000463/versions/{V}/assets/?page_size=100").json()['results']
def s(x):
    return x.decode() if isinstance(x,bytes) else x
for a in sorted(assets,key=lambda a:a['path']):
    u=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
    f=h5py.File(remfile.File(requests.head(u,allow_redirects=True).url),'r')
    es=f['acquisition'].keys()
    d=f['acquisition/ElectricalSeries/data']; rate=f['acquisition/ElectricalSeries/starting_time'].attrs['rate']
    el=f['general/extracellular_ephys/electrodes']
    loc=set(s(x) for x in el['location'][:])
    subj={k:s(f['general/subject'][k][()]) for k in f['general/subject'].keys()}
    other=[k for k in f.keys()]
    print(a['path'], list(es), d.shape, rate, round(d.shape[0]/rate,1),'s', 'trials~',round(d.shape[0]/rate/2.5,1),
          'intervals:',list(f['intervals'].keys()),'units' in f,'stim:',list(f['stimulus/presentation'].keys()),
          'loc',loc,'groups',list(f['general/extracellular_ephys'].keys()), 'desc',s(f['session_description'][()]), 'id',s(f['identifier'][()]), subj, 'analysis',list(f['analysis'].keys()), 'proc',list(f['processing'].keys()), list(f['processing/ecephys'].keys()) if 'ecephys' in f['processing'] else None, flush=True)
EOF
python survey.py 2>&1
```

```
sub-BH395/sub-BH395_ses-20221213T174039_ecephys.nwb ['ElectricalSeries'] (31021056, 32) 24414.0625 1270.6 s trials~ 508.2 intervals: [] False stim: [] loc {'unknown'} groups ['electrodes', 'shank1'] desc Rat Ultrasound Array Stimulation id BH395_3000Hz_5V {'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH395'} analysis [] proc ['ecephys'] ['LFP']
sub-BH395/sub-BH395_ses-20221213T180853_ecephys.nwb ['ElectricalSeries'] (31137792, 32) 24414.0625 1275.4 s trials~ 510.2 intervals: [] False stim: [] loc {'unknown'} groups ['electrodes', 'shank1'] desc Rat Ultrasound Array Stimulation id BH395_3000Hz_55V {'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH395'} analysis [] proc ['ecephys'] ['LFP']
sub-BH395/sub-BH395_ses-20221213T183140_ecephys.nwb ['ElectricalSeries'] (31440896, 32) 24414.0625 1287.8 s trials~ 515.1 intervals: [] False stim: [] loc {'unknown'} groups ['electrodes', 'shank1'] desc Rat Ultrasound Array Stimulation id BH395_300Hz_55V {'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH395'} analysis [] proc ['ecephys'] ['LFP']
sub-BH395/sub-BH395_ses-20221213T185547_ecephys.nwb ['ElectricalSeries'] (30742528, 32) 24414.0625 1259.2 s trials~ 503.7 intervals: [] False stim: [] loc {'unknown'} groups ['electrodes', 'shank1'] desc Rat Ultrasound Array Stimulation id BH395_30Hz_55V {'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH395'} analysis [] proc ['ecephys'] ['LFP']
sub-BH395/sub-BH395_ses-20221213T195834_ecephys.nwb ['ElectricalSeries'] (12773376, 32) 24414.0625 523.2 s trials~ 209.3 intervals: [] False stim: [] loc {'unknown'} groups ['electrodes', 'shank1'] desc Rat Ultrasound Array Stimulation id BH395_3000Hz_6V {'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH395'} analysis [] p
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper; wc -w paper/*.txt; grep -n -i -E "dandi|trial|volt| V |jitter|trigger|TTL|onset|Offline Sorter|channel" paper/*.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000946/ | python -m json.tool | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml | head -120; ls schemas; grep -n -E "elsewhere|where|data:" schemas/*attempt* | head -30
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
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json; s=json.load(open('schemas/attempt.schema.json')); print(json.dumps(s,indent=1)[:9000])"
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

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=50" | python -c "import json,sys; d=json.load(sys.stdin); print(d['count']); [print(r['path'],r['size'],r['asset_id']) for r in d['results'][:50]]"; curl -s "https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/" | python -c "import json,sys; m=json.load(sys.stdin); print(m['description']); print(m['assetsSummary'].get('numberOfSubjects'), m['assetsSummary'].get('variableMeasured'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import requests, collections, json
V="0.250829.1249"; url=f"https://api.dandiarchive.org/api/dandisets/000946/versions/{V}/assets/?page_size=1000"
out=[]
while url:
    d=requests.get(url).json(); out+=d['results']; url=d['next']
json.dump(out,open('a946.json','w'))
c=collections.Counter(a['path'].split('/')[0] for a in out); print(len(out)); print(c)
sz=sorted(a['size'] for a in out); print(sz[:3], sz[-10:], sum(sz)/1e9)
for a in out:
    if any(s in a['path'] for s in ['BH395','BH396','BH401','BH444']): print(a['path'])
print([a['path'] for a in out if 'STTC' in a['path'] or 'sttc' in a['path'].lower()][:10])
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
cd $TMPDIR; source env/bin/activate; python - <<'EOF'
import requests, collections, json
V="0.250829.1249"; url=f"https://api.dandiarchive.org/api/dandisets/000946/versions/{V}/assets/?page_size=1000"
out=[]
while url:
    d=requests.get(url).json(); out+=d['results']; url=d['next']
json.dump(out,open('a946.json','w'))
c=collections.Counter(a['path'].split('/')[0] for a in out); print(len(out)); print(c)
sz=sorted(a['size'] for a in out); print(sz[:3], sz[-10:], sum(sz)/1e9)
for a in out:
    if any(s in a['path'] for s in ['BH395','BH396','BH401','BH444']): print(a['path'])
print([a['path'] for a in out if 'sttc' in a['path'].lower()][:10])
EOF
```

```
1920
Counter({'sub-BH528': 117, 'sub-BH511': 115, 'sub-BH513': 109, 'sub-BH538': 94, 'sub-BH535': 92, 'sub-BH539': 92, 'sub-BH553': 92, 'sub-BH547': 88, 'sub-BH551': 88, 'sub-BH532': 85, 'sub-BH501': 78, 'sub-BH558': 78, 'sub-BH499': 77, 'sub-BH495': 75, 'sub-BH537': 73, 'sub-BH530': 64, 'sub-BH494': 53, 'sub-BH510': 48, 'sub-BH500': 31, 'sub-STTC-BH528': 30, 'sub-STTC-BH513': 28, 'sub-STTC-BH510': 25, 'sub-STTC-BH535': 24, 'sub-STTC-BH495': 23, 'sub-STTC-BH511': 23, 'sub-STTC-BH538': 23, 'sub-STTC-BH553': 23, 'sub-STTC-BH499': 22, 'sub-STTC-BH547': 21, 'sub-STTC-BH551': 21, 'sub-STTC-BH501': 20, 'sub-STTC-BH532': 20, 'sub-STTC-BH530': 16, 'sub-STTC-BH537': 13, 'sub-STTC-BH494': 11, 'sub-STTC-BH539': 10, 'sub-STTC-BH558': 10, 'sub-STTC-BH500': 7, 'sub-BH594': 1})
[228704, 228704, 235144] [637354912, 654280992, 657177232, 670648488, 671606568, 693562568, 706336968, 718113368, 718592408, 754879688] 65.158691744
['sub-STTC-BH494/sub-STTC-BH494_ses-20240118T231600_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ses-20240119T031300_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ses-20240119T024000_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ses-20240119T010000_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ses-20240119T041900_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ses-20240119T055300_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ses-20240119T061900_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ses-20240119T050800_ecephys.nwb', 'sub-STTC-BH494/sub-STTC-BH494_ses-20240119T044300_ecephys.nwb']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python -c "
import json; s=json.load(open('schemas/claims.schema.json')); c=s['properties']['claims']['items']['properties']; print(json.dumps({k:c[k] for k in ['data','where'] if k in c},indent=1)); print(list(c))"; grep -rn "elsewhere" tools/*.py | head -20; grep -rln "data: elsewhere" claims | head
```

```
{
 "data": {
  "description": "What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in another public archive, which the dataset does not hold (`elsewhere`), counted apart from both. Outside sources that a test uses are listed under `inputs` in the attempt.",
  "enum": [
   "dataset",
   "with_labels",
   "with_inputs",
   "elsewhere"
  ]
 },
 "where": {
  "description": "For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
  "type": "string",
  "minLength": 1
 }
}
['id', 'statement', 'source', 'kind', 'quote', 'inferred', 'expected', 'statistics', 'criterion', 'depends_on', 'data', 'where']
tools/build_site.py:343:    data["outcome_counts_elsewhere"] = outcome_counts(data["attempts"], "elsewhere")
tools/build_site.py:454:    data from elsewhere ("with_inputs"), those on data the paper deposited in another archive
tools/build_site.py:455:    ("elsewhere"), and the registry's checks that the dataset is the paper's data ("link"), which are
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 240,310p tools/entry.py; cat tools/paper_match.py | sed -n 1,40p; ls papers | head; grep -l "000463\|000946" -r papers targets 2>/dev/null | head
```

```
if isinstance(rec, dict):
            earlier = load(Report(), ROOT / "attempts" / f"{rec.get('earlier')}.yaml")
            if not isinstance(earlier, dict):
                report.error(where, f"reconciliation: no attempt record {rec.get('earlier')!r}")
            else:
                n_then, n_now = len(earlier.get("findings") or []), len(attempt.get("findings") or [])
                numbers = [f.get("finding") for f in rec.get("findings") or []]
                if sorted(numbers) != list(range(1, n_then + 1)):
                    report.error(where, f"reconciliation: give each of the {n_then} findings of "
                                        f"{rec['earlier']} one item, numbered from 1")
                for f in rec.get("findings") or []:
                    now = f.get("now")
                    if (f.get("status") in ("still_present", "partly_fixed")) != (now is not None):
                        report.error(where, f"reconciliation: earlier finding {f.get('finding')} needs `now` "
                                            "exactly when it is still present or partly fixed")
                    if now is not None and not 1 <= now <= n_now:
                        report.error(where, f"reconciliation: finding {now} is not in this record")
        # A deprecated attempt no longer stands: its claims are being read again, and the claims file it was
        # tested on may already have been replaced (docs/pipeline.md), so it is not held to the current one.
        if attempt.get("deprecated"):
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python probe.py 3764f5c5-0d06-4f24-9bf2-d2849b1e9d0c 2>&1 | grep -v specifications | head -80
```

```
acquisition/ {}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/data_collection () object {}
general/devices/ {}
general/devices/array/ {'description': 'A1x32-Poly3-10mm-50-177-A32', 'manufacturer': 'Neuronexus', 'neurodata_type': 'Device'}
general/extracellular_ephys/ {}
general/extracellular_ephys/electrodes/ {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
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
general/extracellular_ephys/shank1/ {'description': 'electrode group for shank1', 'location': 'brain area', 'neurodata_type': 'ElectrodeGroup'}
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > survey946.py <<'EOF'
import h5py, remfile, requests, json, time
from concurrent.futures import ThreadPoolExecutor
assets=json.load(open('a946.json'))
def s(x):
    x = x[0] if hasattr(x,'shape') and x.shape else x
    return x.decode() if isinstance(x,bytes) else str(x)
def one(a):
    u=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
    for k in range(3):
        try:
            url=requests.head(u,allow_redirects=True).url
            f=h5py.File(remfile.File(url),'r')
            r=dict(path=a['path'],size=a['size'],asset_id=a['asset_id'],url=url)
            r['identifier']=s(f['identifier'][()]); r['start']=s(f['session_start_time'][()])
            r['notes']=s(f['general/notes'][()]) if 'general/notes' in f else None
            r['desc']=s(f['session_description'][()])
            r['acq']=list(f['acquisition'].keys()); r['proc']=list(f['processing'].keys()); r['analysis']=list(f['analysis'].keys())
            r['ntrials']=f['intervals/trials/id'].shape[0] if 'intervals/trials' in f else None
            r['trialcols']=list(f['intervals/trials'].attrs['colnames']) if 'intervals/trials' in f else None
            if 'units' in f:
                r['nunits']=f['units/id'].shape[0]; r['unitcols']=list(f['units'].attrs['colnames']); r['nspk']=f['units/spike_times'].shape[0]
            r['subject']=s(f['general/subject/subject_id'][()]) if 'general/subject/subject_id' in f else None
            r['top']=[k for k in f.keys()]
            r['scratch']=list(f['scratch'].keys()) if 'scratch' in f else None
            return r
        except Exception as e:
            err=repr(e); time.sleep(2)
    return dict(path=a['path'],error=err)
t=time.time()
with ThreadPoolExecutor(32) as ex: res=list(ex.map(one,assets))
json.dump(res,open('s946.json','w'))
print(time.time()-t, sum('error' in r for r in res))
EOF
python survey946.py 2>&1 | tail -3
```

```
1069.940993309021 370
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import json, collections
res=json.load(open('s946.json'))
errs=[r for r in res if 'error' in r]; print(collections.Counter(r['error'][:80] for r in errs).most_common(5))
ok=[r for r in res if 'error' not in r]
print(collections.Counter(r['notes'] for r in ok).most_common(20))
print(collections.Counter(r['desc'] for r in ok).most_common(5))
print(collections.Counter((tuple(r['acq']),tuple(r['proc']),tuple(r['analysis']),r.get('ntrials'),tuple(r.get('unitcols') or [])) for r in ok).most_common(10))
import re
for r in ok[:15]: print(r['path'],r['identifier'],r['notes'],r.get('nunits'),r['size'])
for r in [r for r in ok if 'STTC' in r['path']][:8]: print(r)
EOF
```

```
Fri Oct 30 10:03:06 UTC 2026
[('KeyError("Unable to synchronously open object (object \'spike_times\' doesn\'t exis', 370)]
[('Recording:S1; stim at:S1', 548), ('Recording:AC; stim at:S1', 299), ('Recording:POM; stim at:S1', 193), ('Recording:S1; stim at:M1', 134), ('Recording:M1; stim at:M1', 77), ('Recording:M1; stim at:S1', 77), ('Recording:S1; stim at:POM', 58), ('Recording:POM; stim at:M1', 55), ('Recording:POM; stim at:POM', 33), ('Recording:M1; stim at:POM', 28), ('recording:S1;stimulation:S1', 6), ('recording:M1;stimulation:S1', 6), ('recording:S1;stimulation:M1', 6), ('recording:M1;stimulation:M1', 6), ('Recording:; stim at:S1', 4), ('recording:S1BF;stimulation:S1', 3), ('Recording:; stim at:M1', 2), ('Recording:S1_1; stim at:S1', 2), ('Recording:AC_1; stim at:S1', 2), ('Recording:AC_2; stim at:S1', 2)]
[('Neural Spikes for neural pathways to tFUS', 1550)]
[(((), (), (), 500, ('spike_times', 'celltype_label')), 1277), (((), (), (), 500, ('spike_times',)), 34), (((), (), (), 451, ('spike_times', 'celltype_label')), 32), (((), (), (), 421, ('spike_times', 'celltype_label')), 20), (((), (), (), 491, ('spike_times', 'celltype_label')), 19), (((), (), (), 400, ('spike_times', 'celltype_label')), 15), (((), (), (), 461, ('spike_times', 'celltype_label')), 12), (((), (), (), 401, ('spike_times', 'celltype_label')), 12), (((), (), (), 450, ('spike_times', 'celltype_label')), 8), (((), (), (), 416, ('spike_times', 'celltype_label')), 8)]
sub-BH494/sub-BH494_ecephys.nwb BH494_1500_200_67_5_MOTOR Recording:M1; stim at:M1 19 3067424
sub-BH494/sub-BH494_ses-20230817T132836_ecephys.nwb BH494_1500_200_67_5 Recording:S1; stim at:S1 35 6291256
sub-BH494/sub-BH494_ses-20230820T123756_ecephys.nwb BH494_1500_200_67_5 Recording:M1; stim at:S1 3 1256120
sub-BH494/sub-BH494_ses-20230820T125042_ecephys.nwb BH494_1500_200_67_5_NEAR Recording:S1; stim at:S1 38 4036944
sub-BH494/sub-BH494_ses-20230820T131032_ecephys.nwb BH494_1500_200_67_5_NEAR Recording:M1; stim at:S1 48 5108112
sub
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import json, collections, re
res=json.load(open('s946.json'))
ok=[r for r in res if 'error' not in r]; err=[r for r in res if 'error' in r]
a={x['path']:x for x in json.load(open('a946.json'))}
print('err sizes', sorted(a[r['path']]['size'] for r in err)[:5], sorted(a[r['path']]['size'] for r in err)[-5:], sum(a[r['path']]['size'] for r in err)/1e9)
print('err STTC', sum('STTC' in r['path'] for r in err), 'ok STTC', sum('STTC' in r['path'] for r in ok))
print('ok size total', sum(r['size'] for r in ok)/1e9, max(r['size'] for r in ok))
# identifier suffixes
suf=collections.Counter(re.sub(r'^BH\d+_','',r['identifier']) for r in ok)
print(len(suf)); print(suf.most_common(80))
EOF
```

```
err sizes [389832, 389832, 389832, 389832, 389832] [693562568, 706336968, 718113368, 718592408, 754879688] 60.358902096
err STTC 370 ok STTC 0
ok size total 4.799789648 12566224
73
[('30_200_67_5', 59), ('4500_200_67_5', 57), ('1500_200_67_5', 56), ('3000_200_67_5', 48), ('300_200_67_5', 46), ('1500_40_67_5', 41), ('30_30000_67_5', 40), ('300_1000_67_5', 40), ('4500_67_67_5', 40), ('3000_100_67_5', 40), ('3000_300_67_5', 38), ('4500_14_67_5', 38), ('1500_600_67_5', 37), ('30_10000_67_5', 36), ('3000_20_67_5', 36), ('30_20000_67_5', 36), ('1500_4_67_5', 36), ('30_2000_67_5', 35), ('300_3000_67_5', 35), ('4500_200_67_5_MOTOR', 34), ('1500_400_67_5', 34), ('4500_134_67_5', 34), ('30_200_67_5_MOTOR', 33), ('300_200_67_5_MOTOR', 33), ('1500_200_67_5_MOTOR', 32), ('3000_200_67_5_MOTOR', 32), ('300_20_67_5', 32), ('300_2000_67_5', 31), ('3000_2_67_5', 30), ('4500_1point4_67_5', 30), ('4500_200_67_5_POM_S1', 26), ('3000_200_67_5_POM_S1', 26), ('300_200_67_5_POM_S1', 26), ('3000_200_67_5_POM_MOTOR', 25), ('300_200_67_5_POM_MOTOR', 25), ('1500_200_67_5_POM_S1', 24), ('1500_200_67_5_POM_MOTOR', 22), ('4500_200_67_5_POM_MOTOR', 22), ('30_200_67_5_POM_S1', 22), ('30_200_67_5_POM_MOTOR', 18), ('1500_200_67_5_POM_POM', 14), ('4500_200_67_5_POM_POM', 14), ('3000_200_67_5_POM_POM', 12), ('300_200_67_5_POM_POM', 11), ('1500_200_67_5_POM', 10), ('30_200_67_5_POM_POM', 10), ('30_200_67_5_POM', 8), ('300_200_67_5_POM', 8), ('3000_200_67_5_POM', 8), ('4500_200_67_5_POM', 7), ('1500_200_67_5_NEAR', 4), ('1500_200_67_5_NEAR_MOTOR', 4), ('1500_200_67_5_NEW', 4), ('3000_200_67_5_NEW', 4), ('30_200_67_5_POM_150-95', 4), ('1500_200_67_5_POM_155-95', 4), ('4500_200_67_5_POM__150-95', 4), ('30_2000_67_5_2', 4), ('30_10000_67_5_2', 4), ('3000_200_67_5_POM_150-95', 3), ('3000_200_67_5_2', 3), ('3000_200_67_5_POM_POM_2', 2), ('30_200_67_5_POM _S1', 2), ('3000_100_67_5_back', 2), ('3000_100_67_5_contra', 2), ('3000_100_67_5_dep05', 2), ('3000_100_67_5_front', 2), ('3000_200_67_5_POM_S1BF', 2), ('300
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import json, collections, re
res=json.load(open('s946.json'))
ok=[r for r in res if 'error' not in r]
def parse(r):
    n=r['notes'].lower().replace(' ','')
    m=re.match(r'recording:([^;]*);(?:stimat|stimulation):(.*)',n)
    return m.group(1),m.group(2)
c=collections.Counter()
for r in ok:
    rec,st=parse(r); suf=re.sub(r'^BH\d+_[\dpoint]+_[\d]+_\d+_\d+','',r['identifier'])
    c[(suf,rec,st)]+=1
for k,v in sorted(c.items()): print(k,v)
subj=collections.defaultdict(collections.Counter)
for r in ok:
    rec,st=parse(r); subj[r['path'].split('/')[0]][(rec,st)]+=1
for k,v in sorted(subj.items()): print(k,dict(v))
EOF
```

```
('', '', 's1') 5
('', 'ac', 's1') 281
('', 'ac_1', 's1') 2
('', 'ac_2', 's1') 2
('', 'm1', 's1') 75
('', 'm1_r', 's1') 2
('', 'pom', 's1') 125
('', 's1', 's1') 460
('', 's1_1', 's1') 2
('', 's1_r', 's1') 2
('BH532_4500_1point4_67_5', 'ac', 's1') 2
('BH532_4500_1point4_67_5', 's1', 's1') 2
('BH535_4500_1point4_67_5', 'ac', 's1') 2
('BH535_4500_1point4_67_5', 's1', 's1') 2
('BH537_4500_1point4_67_5', 'ac', 's1') 2
('BH538_4500_1point4_67_5', 'ac', 's1') 2
('BH538_4500_1point4_67_5', 's1', 's1') 2
('BH539_4500_1point4_67_5', 'ac', 's1') 2
('BH539_4500_1point4_67_5', 's1', 's1') 2
('BH547_4500_1point4_67_5', 'ac', 's1') 2
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import json, collections, re, h5py, remfile, numpy as np
res=json.load(open('s946.json'))
ok=[r for r in res if 'error' not in r]
for sub in ['BH551','BH511','BH530']:
    rs=[r for r in ok if sub in r['path']]
    print(sub, collections.Counter(re.sub(r'^BH\d+_','',r['identifier'])+'|'+r['notes'] for r in rs).most_common(12))
r=[r for r in ok if 'BH551' in r['path']][0]
f=h5py.File(remfile.File(r['url']),'r')
st=f['intervals/trials/start_time'][:]; sp=f['intervals/trials/stop_time'][:]
print(r['identifier'],r['notes'],st[:5],(sp-st)[:5],np.diff(st)[:10],np.diff(st).min(),np.diff(st).max())
sts=f['units/spike_times']; idx=f['units/spike_times_index'][:]; print(idx[:5], sts[:5], sts[-5:], f['units/celltype_label'][:])
print({k:f['units'][k].attrs.get('description') for k in f['units']})
print(f['general/subject/age'][()], f['general/subject/description'][()], f['general/data_collection'][()], f['general/institution'][()])
EOF
```

```
BH551 [('30_200_67_5|Recording:S1; stim at:S1', 2), ('30_200_67_5|Recording:POM; stim at:S1', 2), ('30_2000_67_5|Recording:POM; stim at:S1', 2), ('30_2000_67_5|Recording:S1; stim at:S1', 2), ('30_10000_67_5_2|Recording:POM; stim at:S1', 2), ('30_10000_67_5_2|Recording:S1; stim at:S1', 2), ('30_20000_67_5|Recording:POM; stim at:S1', 2), ('30_20000_67_5|Recording:S1; stim at:S1', 2), ('300_20_67_5|Recording:POM; stim at:S1', 2), ('300_20_67_5|Recording:S1; stim at:S1', 2), ('4500_1point4_67_5|Recording:POM; stim at:S1', 2), ('30_30000_67_5|Recording:POM; stim at:S1', 2)]
BH511 [('1500_200_67_5|Recording:S1; stim at:S1', 2), ('1500_200_67_5|Recording:M1; stim at:S1', 2), ('1500_200_67_5_MOTOR|Recording:M1; stim at:M1', 2), ('1500_200_67_5_MOTOR|Recording:S1; stim at:M1', 2), ('1500_200_67_5_POM_S1|Recording:POM; stim at:S1', 2), ('1500_200_67_5_POM_S1|Recording:S1; stim at:S1', 2), ('1500_200_67_5_POM_MOTOR|Recording:POM; stim at:M1', 2), ('1500_200_67_5_POM_MOTOR|Recording:S1; stim at:M1', 2), ('1500_200_67_5_POM_POM|Recording:POM; stim at:POM', 2), ('30_200_67_5|Recording:S1; stim at:S1', 2), ('1500_200_67_5_POM_POM|Recording:S1; stim at:POM', 2), ('30_200_67_5|Recording:M1; stim at:S1', 2)]
BH530 [('30_2000_67_5|Recording:S1; stim at:S1', 2), ('30_2000_67_5|Recording:AC; stim at:S1', 2), ('300_3000_67_5|Recording:AC; stim at:S1', 2), ('300_3000_67_5|Recording:S1; stim at:S1', 2), ('1500_40_67_5|Recording:S1; stim at:S1', 2), ('1500_40_67_5|Recording:AC; stim at:S1', 2), ('30_2000_67_5_2|Recording:S1; stim at:S1', 2), ('30_2000_67_5_2|Recording:AC; stim at:S1', 2), ('30_10000_67_5|Recording:AC; stim at:S1', 2), ('30_10000_67_5|Recording:S1; stim at:S1', 2), ('30_30000_67_5|Recording:S1; stim at:S1', 2), ('30_30000_67_5|Recording:AC; stim at:S1', 2)]
BH551_30_200_67_5 Recording:S1; stim at:S1 [ 0.43900928  2.9270016   5.23493376  7.77424896 10.38348288] [2.2 2.2 2.2 2.2 2.2] [2.48799232 2.30793216 2.5393152  2.60923392 2.30182912 2.408448
 2.633728   2.5964544  2.5036
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000463-gao-2025 && cd $TMPDIR && source env/bin/activate && cat > cache.py <<'EOF'
import json, re, h5py, remfile, numpy as np, time, pickle
from concurrent.futures import ThreadPoolExecutor
res=json.load(open('s946.json'))
ok=[r for r in res if 'error' not in r]
def parse(r):
    n=r['notes'].lower().replace(' ','')
    m=re.match(r'recording:([^;]*);(?:stimat|stimulation):(.*)',n); return m.group(1),m.group(2)
sel=[r for r in ok if parse(r)[1]=='s1']
print(len(sel), sum(r['size'] for r in sel)/1e9)
def load(r):
    for k in range(4):
        try:
            f=h5py.File(remfile.File(r['url']),'r')
            st=f['intervals/trials/start_time'][:]
            idx=f['units/spike_times_index'][:]; sp=f['units/spike_times'][:]
            lab=f['units/celltype_label'][:] if 'celltype_label' in f['units'] else None
            dc=f['general/data_collection'][()] if 'general/data_collection' in f else None
            return dict(path=r['path'],asset_id=r['asset_id'],identifier=r['identifier'],notes=r['notes'],start=r['start'],trials=st,stop=f['intervals/trials/stop_time'][:],idx=idx,spikes=sp,label=lab,dc=dc)
        except Exception as e: err=e; time.sleep(3)
    return dict(path=r['path'],error=repr(err))
t=time.time()
with ThreadPoolExecutor(48) as ex: out=list(ex.map(load,sel))
print(time.time()-t, sum('error' in o for o in out))
pickle.dump(out,open('cache.pkl','wb'))
EOF
python cache.py
```

```
1150 3.443690304
558.2077457904816 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pickle, numpy as np, collections, re, hashlib
out=pickle.load(open('cache.pkl','rb'))
def parse(n):
    n=n.lower().replace(' ','')
    m=re.match(r'recording:([^;]*);(?:stimat|stimulation):(.*)',n); return m.group(1),m.group(2)
# duplicates by hash of spikes
h=collections.defaultdict(list)
for o in out:
    h[hashlib.md5(o['spikes'].tobytes()+o['trials'].tobytes()).hexdigest()].append(o)
print('files',len(out),'unique',len(h), collections.Counter(len(v) for v in h.values()))
ex=[v for v in h.values() if len(v)>1][:3]
for v in ex: print([(o['path'],o['identifier'],o['start']) for o in v])
# same identifier+area but different content?
g=collections.defaultdict(list)
for k,v in h.items(): g[(v[0]['identifier'],parse(v[0]['notes'])[0])].append(k)
print('id+area with >1 distinct contents', sum(len(x)>1 for x in g.values()))
labs=collections.Counter()
for v in h.values():
    o=v[0]; lab=o['label']; labs[(parse(o['notes'])[0], tuple(sorted(set(lab.tolist()))) if lab is not None else None)]+=1
print(labs)
EOF
```

```
Fri Oct 30 10:13:32 UTC 2026
files 1150 unique 598 Counter({2: 549, 1: 48, 4: 1})
[('sub-BH494/sub-BH494_ses-20230817T132836_ecephys.nwb', 'BH494_1500_200_67_5', '2023-08-17T13:28:36.000000-04:00'), ('sub-BH494/sub-BH494_ses-20230817T132800_ecephys.nwb', 'BH494_1500_200_67_5', '2023-08-17T13:28:00.000000-04:00')]
[('sub-BH494/sub-BH494_ses-20230820T123756_ecephys.nwb', 'BH494_1500_200_67_5', '2023-08-20T12:37:56.000000-04:00'), ('sub-BH494/sub-BH494_ses-20230820T123700_ecephys.nwb', 'BH494_1500_200_67_5', '2023-08-20T12:37:00.000000-04:00')]
[('sub-BH494/sub-BH494_ses-20230820T125042_ecephys.nwb', 'BH494_1500_200_67_5_NEAR', '2023-08-20T12:50:42.000000-04:00'), ('sub-BH494/sub-BH494_ses-20230820T125000_ecephys.nwb', 'BH494_1500_200_67_5_NEAR', '2023-08-20T12:50:00.000000-04:00')]
id+area with >1 distinct contents 0
Counter({('s1', (0.0,)): 288, ('ac', (0.0,)): 152, ('pom', (0.0,)): 100, ('m1', (0.0,)): 44, ('s1bf', None): 3, ('', (0.0,)): 2, ('pom', None): 2, ('s1_r', (0.0,)): 1, ('m1_r', (0.0,)): 1, ('s1_1', (0.0,)): 1, ('ac_1', (0.0,)): 1, ('ac_2', (0.0,)): 1, ('vpm', None): 1, ('', None): 1})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import json
a=json.load(open('a946.json'))
st=[x for x in a if 'STTC' in x['path']]
st=sorted(st,key=lambda x:x['size'])
print(st[0]['path'],st[0]['size'],st[0]['asset_id']); print(st[len(st)//2]['path'],st[len(st)//2]['asset_id'])
EOF
python probe.py $(python -c "
import json;a=json.load(open('$TMPDIR/a946.json'));st=sorted([x for x in a if 'STTC' in x['path']],key=lambda x:x['size']);print(st[len(st)//2]['asset_id'])") 2>&1 | grep -v specifications | head -60
```

```
sub-STTC-BH495/sub-STTC-BH495_ses-20240119T122000_obj-nlfdcd_ecephys.nwb 389832 db351e16-c291-4a7b-a2bf-3a565f5dad60
sub-STTC-BH547/sub-STTC-BH547_ses-20240404T075700_ecephys.nwb d4d91f89-264e-4c1f-8943-1499fc55f1d9
acquisition/ {}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/data_collection () object {}
general/devices/ {}
general/devices/array/ {'description': 'A1x32-Poly3-10mm-50-177-A32', 'manufacturer': 'Neuronexus', 'neurodata_type': 'Device'}
general/extracellular_ephys/ {}
general/extracellular_ephys/electrodes/ {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name'], dtype=object), 'description': 'all electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group_name (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/id (32,) int64 {'neurodata_type': 'ElementIdentifiers'}
general/extracellular_ephys/electrodes/imp (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/location (32,) object {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/x (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/y (32,) float64 {'description': 'my description', 'neurodata_type': 'VectorData'}
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pickle, numpy as np, collections, re, hashlib
out=pickle.load(open('cache.pkl','rb'))
def parse(n):
    n=n.lower().replace(' ','')
    m=re.match(r'recording:([^;]*);(?:stimat|stimulation):(.*)',n); return m.group(1),m.group(2)
seen={}; uniq=[]
for o in sorted(out,key=lambda o:o['path']):
    k=hashlib.md5(o['spikes'].tobytes()+o['trials'].tobytes()).hexdigest()
    if k in seen: continue
    seen[k]=o; uniq.append(o)
rows=[]
for o in uniq:
    area,_=parse(o['notes']); m=re.match(r'BH(\d+)_([\dpoint]+)_(\d+)_(\d+)_(\d+)(.*)',o['identifier'])
    if not m: print('skip',o['identifier']); continue
    sub,prf,pd,ud,v,suf=m.groups()
    n=np.diff(np.r_[0,o['idx']])
    rows.append((o['identifier'],sub,prf,pd,suf,area,len(n),int((n>2000).sum()),len(o['trials'])))
import pandas as pd
df=pd.DataFrame(rows,columns=['id','sub','prf','pd','suf','area','nunits','n2000','ntr'])
df.to_csv('sessions.csv',index=False)
for area in ['s1','pom','ac']:
    d=df[(df.area==area)]
    print(area); print(d.groupby(['prf','pd','suf']).agg(nsess=('id','size'),nsub=('sub','nunique'),units=('nunits','sum'),u2000=('n2000','sum')).to_string())
EOF
```

```
skip BH532_4500_1point4_67_5
skip BH532_4500_1point4_67_5
skip BH535_4500_1point4_67_5
skip BH535_4500_1point4_67_5
skip BH537_4500_1point4_67_5
skip BH538_4500_1point4_67_5
skip BH538_4500_1point4_67_5
skip BH539_4500_1point4_67_5
skip BH539_4500_1point4_67_5
skip BH547_4500_1point4_67_5
skip BH547_4500_1point4_67_5
skip BH551_4500_1point4_67_5
skip BH551_4500_1point4_67_5
skip BH553_4500_1point4_67_5
skip BH553_4500_1point4_67_5
skip BH594_coating_3000_200_10
s1
                     nsess  nsub  units  u2000
prf  pd    suf                                
1500 200                13    13    314    279
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import requests
for ds,vs in [('000463',['0.250711.1756','0.250711.1947','0.250828.1934','0.250829.1248','draft']),('000946',None)]:
    if vs is None:
        vs=[r['version'] for r in requests.get(f'https://api.dandiarchive.org/api/dandisets/{ds}/versions/').json()['results']]
    sets={}
    for v in vs:
        url=f'https://api.dandiarchive.org/api/dandisets/{ds}/versions/{v}/assets/?page_size=1000'; ids=set()
        while url:
            d=requests.get(url).json(); ids|={(a['path'],a['blob'] if 'blob' in a else a['size']) for a in d['results']}; url=d['next']
        sets[v]=ids
    ref=sets[vs[-1]] if ds=='000463' else sets[sorted(vs)[-1]]
    for v in vs: print(ds,v,len(sets[v]), len(sets[v]^ref))
m=requests.get('https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/').json(); print(m.get('doi'), m.get('relatedResource'))
EOF
```

```
000463 0.250711.1756 29 0
000463 0.250711.1947 29 0
000463 0.250828.1934 29 0
000463 0.250829.1248 29 0
000463 draft 29 0
000946 draft 1920 0
000946 0.250711.1640 1920 0
000946 0.250711.1945 1920 0
000946 0.250712.1549 1920 0
000946 0.250828.1938 1920 0
000946 0.250829.1249 1920 0
10.48324/dandi.000946/0.250829.1249 []
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]:
    print(c['cell_type'], c['metadata'].get('tags'), ''.join(c['source'])[:300].replace('\n',' | '))
EOF
grep -n "def check\|report.error" tools/entry.py | sed -n 1,80p | cut -c1-200
```

```
markdown None # Reproducing Fouke et al. (2025) from dandiset 001453 |  | **Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent | visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*. | [doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04
code None import time | import warnings |  | import matplotlib.pyplot as plt | import numpy as np | import pandas as pd | import statsmodels.api as sm | from scipy import stats | from statsmodels.formula.api import ols | from statsmodels.stats.multicomp import pairwise_tukeyhsd |  | import omr |  | pd.set_option("display.width", 200) | 
markdown None ## Data check |  | Each check of the metadata against the values is stated under its output.
code ['sanity'] info = pd.DataFrame([{ |     "fish": omr.fish_key(s), "species": s["species"], "subject_id": s["subject_id"], "age": s["age"], |     "session_start": s["session_start"][:19], "frames": s["n_frames"], "tracked": s["n_tracked"], |     "frame_hz": round(s["frame_hz"], 1), "x_max": round(s["x_range"][1]), "y_
markdown None The archive's summary says 25 subjects and lists only *Danio rerio*. The files hold 37 fish: | subject ids 0 to 11 are each used for one zebrafish and one *D. cerebrum*, so `subject_id` alone | does not identify an animal. Fish are named here by species and subject id. The 25 ZF are one fewer | than the 2
code ['sanity'] fast = info.frame_hz > 100 | print("Files by frame rate (Methods: tracking at more than 150 Hz):") | print(pd.crosstab(info.species, np.where(fast, "128-171 Hz", "32-35 Hz")).to_string()) | dts = pd.DataFrame([{"fish": omr.fish_key(s), **{f"dt_{k}": v for k, v in s["dt_ms"].items()}} for s in sessions]) | p
markdown None `f0_vtheta` is stated in radians/s. Summed over a trial's frames it gives the trial's change of | `f0_theta` (median ratio near 1 in most files), while its time integral gives about 1/frame rate | of it. It is the heading change per frame, in radia
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pickle, numpy as np, re
out=pickle.load(open('cache.pkl','rb'))
ac=[o for o in out if 'BH530_3000_200' in o['identifier']]
for o in ac: print(o['path'],o['notes'],o['start'],o['trials'][:3],len(o['trials']), o['dc'])
EOF
```

```
Fri Oct 30 10:15:31 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pickle, numpy as np, re
out=pickle.load(open('cache.pkl','rb'))
ac=[o for o in out if re.match(r'BH53[02]_3000_200_67_5$',o['identifier']) or re.match(r'BH511_3000_200_67_5_POM_S1$',o['identifier'])]
for o in ac: print(o['path'],o['identifier'],o['notes'],o['start'],o['trials'][:3],len(o['trials']), o['dc'], o['spikes'].max())
EOF
```

```
sub-BH511/sub-BH511_ses-20231020T155200_ecephys.nwb BH511_3000_200_67_5_POM_S1 Recording:POM; stim at:S1 2023-10-20T15:52:49.000000-04:00 [0.40337408 2.69131776 5.13908736] 450 b'tFUS parameters {PRF:3000Hz PD:200us UD:67ms}' 1127.42510592
sub-BH511/sub-BH511_ses-20231020T155249_ecephys.nwb BH511_3000_200_67_5_POM_S1 Recording:POM; stim at:S1 2023-10-20T15:52:49.000000-04:00 [0.40337408 2.69131776 5.13908736] 450 b'tFUS parameters {PRF:3000Hz PD:200us UD:67ms}' 1127.42510592
sub-BH511/sub-BH511_ses-20231020T160600_ecephys.nwb BH511_3000_200_67_5_POM_S1 Recording:S1; stim at:S1 2023-10-20T16:06:04.000000-04:00 [0.40337408 2.69131776 5.13908736] 450 b'tFUS parameters {PRF:3000Hz PD:200us UD:67ms}' 1127.42408192
sub-BH511/sub-BH511_ses-20231020T160604_ecephys.nwb BH511_3000_200_67_5_POM_S1 Recording:S1; stim at:S1 2023-10-20T16:06:04.000000-04:00 [0.40337408 2.69131776 5.13908736] 450 b'tFUS parameters {PRF:3000Hz PD:200us UD:67ms}' 1127.42408192
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/000463-gao-2025/tfus.py",
 "content": "\"\"\"Loading and measures for Gao, Ramachandran, Yu and He (2025), J Neurosci 45(23) e2218242025.\n\nThe target is dandiset 000463. It holds broadband recordings of an S1 probe with no units, no trial\ntimes and no brain locations, from four rats that are not in the paper's own deposit. The paper says\nits data are in dandiset 000946 (Methods, \"Data acquisition and preprocessing\": \"All experimental\ndata has been made public in a repository at the DANDI Archive\n(https://dandiarchive.org/dandiset/000946)\"), so the claims are tested there (`data: elsewhere`).\nBoth are streamed from the DANDI Archive at pinned versions; nothing is downloaded to disk.\n\nWhere each parameter comes from:\n\n- Windows of 67 ms: the claims file (M3) and the Methods (\"The normalized spiking rate which was\n  normalized to 67 ms before each stimulation\"). During sonication 0 to 67 ms, postsonication 201\n  to 268 ms (claims file, M3, from the Figures 5 to 9 and 11 legends).\n- Unit selection, more than 2000 spikes in the session: claims file M1, Methods (\"Only neurons that\n  fire >2,000 spikes for each session were considered\").\n- Normalization readings O2a and O2b, baseline readings O3a to O3c, Bonferroni readings O4a and\n  O4b, alpha 0.01, Kruskal-Wallis then one-tailed two-sample Wilcoxon (rank-sum) tests: the claims\n  file (M4, O2 to O4), from the Methods, \"Statistical analysis\".\n- Sonication onset is the trial `start_time`: the files say \"intervals contains each tFUS trial\n  start and end timestamps\" (general/stimulus); the notebook checks it against the spikes.\n- PRF and PD of a recording are read from its identifier, as the dandiset's description says (\"in\n  BH494_1500_200_67_5, the PRF is 1500Hz and PD is 200us\"). Recording area and stimulation target\n  are read from `general/notes` (\"Recording:S1; stim at:S1\").\n- Parallel reads (threads) and retries change no result; they are standard choices.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport re\nimport time\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\nfrom scipy import stats\n\nAPI = \"https://api.dandiarchive.org/api\"\nDANDISET = \"000463\"\nVERSION = \"0.250829.1248\"\nPAPER_DANDISET = \"000946\"\nPAPER_VERSION = \"0.250829.1249\"\n\nWIN_PRE = (-0.067, 0.0)\nWIN_PRE2 = (-0.134, -0.067)  # O3b baseline sample\nWIN_DURING = (0.0, 0.067)\nWIN_POST = (0.201, 0.268)\nMIN_SPIKES = 2000  # M1\nALPHA = 0.01  # M4\n\n\ndef versions(dandiset):\n    r = requests.get(f\"{API}/dandisets/{dandiset}/versions/\", timeout=60).json()\n    return [v[\"version\"] for v in r[\"results\"]]\n\n\ndef assets(dandiset, version):\n    url = f\"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=1000\"\n    out = []\n    while url:\n        d = requests.get(url, timeout=60).json()\n        out += [dict(path=a[\"path\"], size=a[\"size\"], asset_id=a[\"asset_id\"]) for a in d[\"results\"]]\n        url = d[\"next\"]\n    return sorted(out, key=lambda a: a[\"path\"])\n\n\ndef metadata(dandiset, version):\n    return requests.get(f\"{API}/dandisets/{dandiset}/versions/{version}/\", timeout=60).json()\n\n\ndef s3_url(asset_id):\n    return requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60).url\n\n\ndef _str(x):\n    x = x[0] if hasattr(x, \"shape\") and x.shape else x\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef _retry(fn, a, tries=4):\n    for k in range(tries):\n        try:\n            return fn(a)\n        except Exception as e:  # network errors; retried, then reported\n            err = e\n            time.sleep(2 + 2 * k)\n    return dict(path=a[\"path\"], error=repr(err))\n\n\ndef pmap(fn, items, threads=32):\n    with ThreadPoolExecutor(threads) as ex:\n        return list(ex.map(lambda a: _retry(fn, a), items))\n\n\n# ---------------------------------------------------------------- dandiset 000463 (the target)\n\ndef describe_000463_file(a):\n    \"\"\"Everything an analysis of the claims would need, read from one file's metadata.\"\"\"\n    f = h5py.File(remfile.File(s3_url(a[\"asset_id\"])), \"r\")\n    es = f[\"acquisition/ElectricalSeries\"]\n    el = f[\"general/extracellular_ephys/electrodes\"]\n    return dict(\n        path=a[\"path\"], identifier=_str(f[\"identifier\"][()]),\n        subject=_str(f[\"general/subject/subject_id\"][()]),\n        session_start=_str(f[\"session_start_time\"][()])[:19],\n        acquisition=\",\".join(f[\"acquisition\"].keys()),\n        samples=es[\"data\"].shape[0], channels=es[\"data\"].shape[1],\n        rate_hz=float(es[\"starting_time\"].attrs[\"rate\"]), unit=es[\"data\"].attrs[\"unit\"],\n        duration_s=es[\"data\"].shape[0] / float(es[\"starting_time\"].attrs[\"rate\"]),\n        lfp_rate_hz=float(f[\"processing/ecephys/LFP/ElectricalSeries/starting_time\"].attrs[\"rate\"]),\n        intervals=\",\".join(f[\"intervals\"].keys()) or \"none\",\n        units=\"units\" in f, stimulus=\",\".join(f[\"stimulus/presentation\"].keys()) or \"none\",\n        electrode_location=\",\".join(sorted({_str(x) for x in el[\"location\"][:]})),\n        group_location=_str(f[\"general/extracellular_ephys/shank1\"].attrs[\"location\"]),\n        device=_str(f[\"general/devices/array\"].attrs[\"description\"]),\n    )\n\n\n# ---------------------------------------------------------------- dandiset 000946 (the paper's)\n\nID_RE = re.compile(r\"BH(\\d+)_(\\d+)_([\\dpoint]+)_(\\d+)_(\\d+)(.*)$\")\n\n\ndef parse_identifier(identifier):\n    \"\"\"PRF (Hz), PD (us), UD (ms), voltage and suffix from an identifier such as BH494_1500_200_67_5.\"\"\"\n    m = ID_RE.match(identifier)\n    if not m:\n        return None\n    sub, prf, pd, ud, volt, suffix = m.groups()\n    return dict(subject=\"BH\" + sub, prf=int(prf), pd_us=float(pd.replace(\"point\", \".\")), ud_ms=int(ud),\n                volt=volt, suffix=suffix.strip())\n\n\ndef parse_notes(notes):\n    n = notes.lower().replace(\" \", \"\")\n    m = re.match(r\"recording:([^;]*);(?:stimat|stimulation):(.*)\", n)\n    return (m.group(1), m.group(2)) if m else (\"?\", \"?\")\n\n\ndef describe_000946_file(a):\n    \"\"\"Metadata of one file of 000946, with a signature of its content to find duplicate deposits.\"\"\"\n    f = h5py.File(remfile.File(s3_url(a[\"asset_id\"])), \"r\")\n    r = dict(path=a[\"path\"], asset_id=a[\"asset_id\"], size=a[\"size\"],\n             identifier=_str(f[\"identifier\"][()]), notes=_str(f[\"general/notes\"][()]),\n             description=_str(f[\"session_description\"][()]),\n             session_start=_str(f[\"session_start_time\"][()])[:19])\n    r[\"data_collection\"] = _str(f[\"general/data_collection\"][()]) if \"general/data_collection\" in f else \"\"\n    r[\"unit_columns\"] = \",\".join(f[\"units\"].attrs[\"colnames\"]) if \"units\" in f else \"\"\n    tr = f[\"intervals/trials\"]\n    st, sp = tr[\"start_time\"][:], tr[\"stop_time\"][:]\n    r.update(n_trials=len(st), trial_len_s=float(np.median(sp - st)),\n             isi_min=float(np.diff(st).min()), isi_max=float(np.diff(st).max()))\n    h = hashlib.md5(st.tobytes())\n    if \"spike_times_index\" in f[\"units\"]:\n        idx = f[\"units/spike_times_index\"][:]\n        r[\"spike_counts\"] = np.diff(np.r_[0, idx]).astype(int)\n        lab = f[\"units/celltype_label\"][:] if \"celltype_label\" in f[\"units\"] else None\n        r[\"labels\"] = lab\n        r[\"label_description\"] = (_str(f[\"units/celltype_label\"].attrs[\"description\"])\n                                  if lab is not None else \"\")\n        h.update(idx.tobytes())\n        n = len(f[\"units/spike_times\"])\n        h.update(f[\"units/spike_times\"][: min(n, 1000)].tobytes())\n        h.update(f[\"units/spike_times\"][max(0, n - 1000):].tobytes())\n    else:\n        r[\"spike_counts\"] = None\n        r[\"labels\"] = None\n        r[\"label_description\"] = \"\"\n        r[\"sttc_shape\"] = f[\"units/STTC\"].shape if \"STTC\" in f[\"units\"] else None\n        h.update(str(r[\"sttc_shape\"]).encode())\n    r[\"signature\"] = h.hexdigest()\n    rec, target = parse_notes(r[\"notes\"])\n    r[\"area\"], r[\"target\"] = rec, target\n    p = parse_identifier(r[\"identifier\"]) or {}\n    r.update(p)\n    return r\n\n\ndef load_spikes(a):\n    \"\"\"Spike times of every unit and the trial onsets of one file of 000946.\"\"\"\n    f = h5py.File(remfile.File(s3_url(a[\"asset_id\"])), \"r\")\n    idx = f[\"units/spike_times_index\"][:]\n    sp = f[\"units/spike_times\"][:]\n    units = np.split(sp, idx[:-1])\n    return dict(path=a[\"path\"], onsets=f[\"intervals/trials/start_time\"][:], units=units,\n                digest=hashlib.md5(sp.tobytes()).hexdigest())\n\n\n# ---------------------------------------------------------------- measures\n\ndef window_counts(spikes, onsets, win):\n    \"\"\"Spike counts of one unit in [onset + win[0], onset + win[1]) for each trial.\"\"\"\n    lo = np.searchsorted(spikes, onsets + win[0])\n    hi = np.searchsorted(spikes, onsets + win[1])\n    return hi - lo\n\n\ndef normalized_rate(spikes, onsets, win, reading):\n    \"\"\"Normalized spiking rate in percent (claims file M3), under reading O2a or O2b.\n\n    O2a: mean count in the window over trials / mean count in the 67 ms before onset over trials.\n    O2b: mean over trials of the per-trial ratio, trials with no prestimulation spike left out.\n    Returns nan when the unit has no prestimulation spike (O2a) or no usable trial (O2b).\n    \"\"\"\n    c = window_counts(spikes, onsets, win).astype(float)\n    b = window_counts(spikes, onsets, WIN_PRE).astype(float)\n    if reading == \"a\":\n        return 100 * c.mean() / b.mean() if b.sum() > 0 else np.nan\n    keep = b > 0\n    return 100 * np.mean(c[keep] / b[keep]) if keep.any() else np.nan\n\n\ndef baseline_test(x, x_pre2, reading, alternative=\"greater\"):\n    \"\"\"Raw p of a window's normalized rates against baseline (claims file O3).\n\n    O3a: two-sample rank-sum against the prestimulation window itself (100% for every unit).\n    O3b: two-sample rank-sum against the units' normalized rate 134 to 67 ms before onset.\n    O3c: one-sample signed-rank test against 100%.\n    \"\"\"\n    x = np.asarray(x, float)\n    if reading == \"a\":\n        return stats.mannwhitneyu(x, np.full(len(x), 100.0), alternative=alternative).pvalue\n    if reading == \"b\":\n        return stats.mannwhitneyu(x, np.asarray(x_pre2, float), alternative=alternative).pvalue\n    return stats.wilcoxon(x - 100.0, alternative=alternative).pvalue\n\n\ndef bonferroni(p, k):\n    return min(1.0, p * k)\n"
}
```

```
File created successfully at: entries/000463-gao-2025/tfus.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > dev1.py <<'EOF'
import sys, time, pickle
sys.path.insert(0,'entries/000463-gao-2025')
import tfus, pandas as pd
t=time.time()
a463=tfus.assets(tfus.DANDISET,tfus.VERSION)
d463=pd.DataFrame(tfus.pmap(tfus.describe_000463_file,a463))
print(time.time()-t); print(d463.drop(columns=['path']).to_string())
t=time.time()
a946=tfus.assets(tfus.PAPER_DANDISET,tfus.PAPER_VERSION)
r=tfus.pmap(tfus.describe_000946_file,a946,threads=48)
print(time.time()-t, sum('error' in x for x in r))
pickle.dump((d463,r),open('dev1.pkl','wb'))
EOF
python dev1.py 2>&1 | tail -40
```

```
24.125632762908936
               identifier subject        session_start       acquisition   samples  channels     rate_hz unit   duration_s  lfp_rate_hz intervals  units stimulus electrode_location group_location                       device
0         BH395_3000Hz_5V   BH395  2022-12-13T17:40:39  ElectricalSeries  31021056        32  24414.0625    V  1270.622454       3051.8      none  False     none            unknown     brain area  A1x32-Poly3-10mm-50-177-A32
1        BH395_3000Hz_55V   BH395  2022-12-13T18:08:53  ElectricalSeries  31137792        32  24414.0625    V  1275.403960       3051.8      none  False     none            unknown     brain area  A1x32-Poly3-10mm-50-177-A32
2         BH395_300Hz_55V   BH395  2022-12-13T18:31:40  ElectricalSeries  31440896        32  24414.0625    V  1287.819100       3051.8      none  False     none            unknown     brain area  A1x32-Poly3-10mm-50-177-A32
3          BH395_30Hz_55V   BH395  2022-12-13T18:55:47  ElectricalSeries  30742528        32  24414.0625    V  1259.213947       3051.8      none  False     none            unknown     brain area  A1x32-Poly3-10mm-50-177-A32
4         BH395_3000Hz_6V   BH395  2022-12-13T19:58:34  ElectricalSeries  12773376        32  24414.0625    V   523.197481       3051.8      none  False     none            unknown     brain area  A1x32-Poly3-10mm-50-177-A32
5         BH396_test5_24V   BH396  2022-11-17T21:54:47  ElectricalSeries   7505920        32  24414.0625    V   307.442483       3051.8      none  False     none            unknown     brain area  A1x32-Poly3-10mm-50-177-A32
6          BH396_test5_5V   BH396  2022-11-17T22:04:34  ElectricalSeries   7383040        32  24414.0625    V   302.409318       3051.8      none  False     none            unknown     brain area  A1x32-Poly3-10mm-50-177-A32
7          BH396_test5_4V   BH396  2022-11-17T22:10:38  ElectricalSeries   7411712        32  24414.0625    V   303.583724       3051.8      none  False     none            unknown 
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import sys,time,requests,h5py,remfile,pickle
sys.path.insert(0,'entries/000463-gao-2025')
import tfus
d=requests.get('https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=3').json()['results'][0]; print(d)
a946=tfus.assets(tfus.PAPER_DANDISET,tfus.PAPER_VERSION)
sm=[a for a in a946 if 'STTC' not in a['path']][:10]; st=[a for a in a946 if 'STTC' in a['path']][:10]
for grp in [sm,st]:
    t0=time.time(); urls=[tfus.s3_url(a['asset_id']) for a in grp]; t1=time.time()
    for a in grp: tfus.describe_000946_file(a)
    t2=time.time(); print('head',(t1-t0)/10,'describe',(t2-t1)/10)
EOF
```

```
{'asset_id': '6e7e9b91-0d66-45af-b646-dfb11e4d9967', 'blob': 'c4f53e05-0de9-4450-b1b9-c873afc314bf', 'zarr': None, 'path': 'sub-BH494/sub-BH494_ecephys.nwb', 'size': 3067424, 'created': '2024-04-05T04:21:53.900176Z', 'modified': '2025-07-11T16:40:32.134761Z'}
head 0.26962497234344485 describe 0.8642432451248169
head 0.2374947786331177 describe 0.8430458307266235
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000463-gao-2025 && python - <<'EOF'
p='tfus.py'; s=open(p).read()
s=s.replace("from concurrent.futures import ThreadPoolExecutor\n","from concurrent.futures import ProcessPoolExecutor\nfrom functools import partial\n")
s=s.replace('''def pmap(fn, items, threads=32):
    with ThreadPoolExecutor(threads) as ex:
        return list(ex.map(lambda a: _retry(fn, a), items))''','''def pmap(fn, items, workers=24):
    """Map over files in separate processes (h5py serializes reads within one process)."""
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(partial(_retry, fn), items, chunksize=4))''')
s=s.replace("- Parallel reads (threads) and retries","- Parallel reads (processes) and retries")
open(p,'w').write(s)
EOF
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import sys,time
sys.path.insert(0,'entries/000463-gao-2025')
import tfus
a946=tfus.assets(tfus.PAPER_DANDISET,tfus.PAPER_VERSION)
t=time.time(); r=tfus.pmap(tfus.describe_000946_file,a946[:200]); print(time.time()-t, sum('error' in x for x in r))
EOF
nproc
```

```
288.1156554222107 0
4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import sys,time,requests
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'entries/000463-gao-2025')
import tfus
url="https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=1000"
out=[]
while url:
    d=requests.get(url).json(); out+=d['results']; url=d['next']
b=out[0]['blob']; u=f"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}"
print(requests.head(u).status_code, tfus.s3_url(out[0]['asset_id']))
t=time.time()
with ThreadPoolExecutor(16) as ex: r=list(ex.map(lambda a: tfus.s3_url(a['asset_id']), out[:64]))
print('heads 64 parallel', time.time()-t)
import h5py, remfile
t=time.time()
def op(a):
    b=a['blob']; u=f"https://dandiarchive.s3.amazonaws.com/blobs/{b[:3]}/{b[3:6]}/{b}"
    f=h5py.File(remfile.File(u),'r'); return f['identifier'][()]
for a in out[:10]: op(a)
print('open direct seq 10', time.time()-t)
EOF
```

```
200 https://dandiarchive.s3.amazonaws.com/blobs/c4f/53e/c4f53e05-0de9-4450-b1b9-c873afc314bf?response-content-disposition=attachment%3B%20filename%3D%22sub-BH494_ecephys.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261030%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261030T103955Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=b354d33b52a4c77104a10ddc96927c003a9ef608c1211c96875142e3746e0a18
heads 64 parallel 1.1276822090148926
open direct seq 10 5.343581199645996
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > t.py <<'EOF'
import sys,time
sys.path.insert(0,'entries/000463-gao-2025')
import tfus
if __name__=='__main__':
    a946=tfus.assets(tfus.PAPER_DANDISET,tfus.PAPER_VERSION)
    sm=[a for a in a946 if 'STTC' not in a['path']][300:364]
    for w in [8]:
        t=time.time(); r=tfus.pmap(tfus.describe_000946_file,sm,workers=w); print(w,time.time()-t)
    t=time.time(); [tfus.describe_000946_file(a) for a in sm[:16]]; print('seq16',time.time()-t)
EOF
python t.py
```

```
8 6.76439094543457
seq16 12.162838220596313
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > t2.py <<'EOF'
import sys,time,pickle
sys.path.insert(0,'entries/000463-gao-2025')
import tfus
if __name__=='__main__':
    a946=tfus.assets(tfus.PAPER_DANDISET,tfus.PAPER_VERSION)
    t=time.time(); r=tfus.pmap(tfus.describe_000946_file,a946,workers=8); print(time.time()-t, sum('error' in x for x in r))
    pickle.dump(r,open('s946b.pkl','wb'))
EOF
sed -i 's/def pmap(fn, items, workers=24)/def pmap(fn, items, workers=8)/' entries/000463-gao-2025/tfus.py
python t2.py
```

```
193.16762804985046 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import pickle, pandas as pd, numpy as np, collections
r=pickle.load(open('s946b.pkl','rb'))
df=pd.DataFrame(r)
print(df.columns.tolist())
units=df[df.spike_counts.notna()]; sttc=df[df.spike_counts.isna()]
print(len(units),len(sttc))
print('label values', collections.Counter(np.concatenate([l for l in units.labels if l is not None]).tolist()), 'files without label col', units.labels.isna().sum())
print(units.label_description.value_counts())
g=units.groupby('signature').path.count(); print('dup groups',g.value_counts().to_dict())
print(units.trial_len_s.describe(), units.isi_min.min(), units.isi_max.max(), units.n_trials.value_counts().head())
print(units.data_collection.value_counts().head(3))
print(sttc.notes.value_counts().head(10))
EOF
```

```
Fri Oct 30 10:43:53 UTC 2026
['path', 'asset_id', 'size', 'identifier', 'notes', 'description', 'session_start', 'data_collection', 'unit_columns', 'n_trials', 'trial_len_s', 'isi_min', 'isi_max', 'spike_counts', 'labels', 'label_description', 'signature', 'area', 'target', 'subject', 'prf', 'pd_us', 'ud_ms', 'volt', 'suffix', 'sttc_shape']
1550 370
label values Counter({0.0: 44249}) files without label col 34
label_description
label 1 = RSU, label 2 = FSU    1516
                                  34
Name: count, dtype: int64
dup groups {2: 728, 1: 84, 3: 2, 4: 1}
count    1.550000e+03
mean     2.200000e+00
std      7.330067e-15
min      2.200000e+00
25%      2.200000e+00
50%      2.200000e+00
75%      2.200000e+00
max      2.200000e+00
Name: trial_len_s, dtype: float64 2.249973759999989 2.7500544000000104 n_trials
500    1311
451      32
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > dev2.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, itertools
sys.path.insert(0,'entries/000463-gao-2025')
import tfus
from scipy import stats
surv=pd.DataFrame(pickle.load(open('s946b.pkl','rb')))
cache={o['path']:o for o in pickle.load(open('cache.pkl','rb'))}
u=surv[surv.spike_counts.notna()].sort_values('path')
first=u.drop_duplicates('signature')
acsub=sorted(first[first.area=='ac'].subject.unique()); print(acsub)
ac=first[(first.area=='ac')&(first.target=='s1')&(first.pd_us==200)&(first.suffix=='')]
print(ac[['path','identifier','n_trials']].to_string())
rows=[]
for _,s in ac.iterrows():
    o=cache[s.path]; idx=o['idx']; units=np.split(o['spikes'],idx[:-1]); on=o['trials']
    for k,sp in enumerate(units):
        if len(sp)<=tfus.MIN_SPIKES: continue
        d=dict(subject=s.subject,prf=s.prf,path=s.path,unit=k)
        for rd in 'ab':
            d[f'pre2_{rd}']=tfus.normalized_rate(sp,on,tfus.WIN_PRE2,rd)
            d[f'dur_{rd}']=tfus.normalized_rate(sp,on,tfus.WIN_DURING,rd)
            d[f'post_{rd}']=tfus.normalized_rate(sp,on,tfus.WIN_POST,rd)
        rows.append(d)
R=pd.DataFrame(rows); print(R.groupby('prf').size(), len(R))
for rd in 'ab':
    print('reading O2',rd, 'nan units', R[f'dur_{rd}'].isna().sum())
    for w in ['dur','post']:
        g=[R[R.prf==p][f'{w}_{rd}'].dropna() for p in [30,300,1500,3000,4500]]
        print(w, 'KW', stats.kruskal(*g), 'means', [round(x.mean(),1) for x in g], 'medians',[round(x.median(),1) for x in g])
        for p in [30,300,1500,3000,4500]:
            x=R[R.prf==p][[f'{w}_{rd}',f'pre2_{rd}']].dropna()
            ps=[tfus.baseline_test(x[f'{w}_{rd}'],x[f'pre2_{rd}'],o3) for o3 in 'abc']
            print('  ',p,len(x),['%.2g'%v for v in ps])
EOF
python dev2.py
```

```
['BH530', 'BH532', 'BH535', 'BH537', 'BH538', 'BH539', 'BH547']
                                                     path           identifier  n_trials
729   sub-BH530/sub-BH530_ses-20231202T152500_ecephys.nwb   BH530_300_200_67_5       500
741   sub-BH530/sub-BH530_ses-20231202T171200_ecephys.nwb  BH530_4500_200_67_5       500
745   sub-BH530/sub-BH530_ses-20231202T175400_ecephys.nwb  BH530_1500_200_67_5       500
862   sub-BH535/sub-BH535_ses-20231225T180600_ecephys.nwb    BH535_30_200_67_5       500
910   sub-BH535/sub-BH535_ses-20240103T143800_ecephys.nwb  BH535_1500_200_67_5       500
930   sub-BH535/sub-BH535_ses-20240108T175600_ecephys.nwb  BH535_3000_200_67_5       500
966   sub-BH537/sub-BH537_ses-20240108T223000_ecephys.nwb   BH537_300_200_67_5       500
987   sub-BH537/sub-BH537_ses-20240109T122200_ecephys.nwb  BH537_1500_200_67_5       500
1015  sub-BH537/sub-BH537_ses-20240109T165900_ecephys.nwb  BH537_4500_200_67_5       500
1039  sub-BH538/sub-BH538_ses-20240109T193100_ecephys.nwb   BH538_300_200_67_5       500
1083  sub-BH538/sub-BH538_ses-20240110T163300_ecephys.nwb  BH538_3000_200_67_5       500
1107  sub-BH538/sub-BH538_ses-20240110T193900_ecephys.nwb  BH538_4500_200_67_5       500
1113  sub-BH539/sub-BH539_ses-20240123T201500_ecephys.nwb  BH539_1500_200_67_5       500
1117  sub-BH539/sub-BH539_ses-20240124T173900_ecephys.nwb    BH539_30_200_67_5       500
1181  sub-BH539/sub-BH539_ses-20240126T181400_ecephys.nwb  BH539_3000_200_67_5       500
1237  sub-BH547/sub-BH547_ses-20240223T121100_ecephys.nwb  BH547_4500_200_67_5       500
1241  sub-BH547/sub-BH547_ses-20240223T133300_ecephys.nwb    BH547_30_200_67_5       500
prf
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='claims/000463/10.1523-jneurosci.2218-24.2025.yaml'
s=open(p).read()
lines=s.split('\n')
keep_dataset={'fig5a-sham-no-response','fig5b-control-cg1-no-response','methods-insitu-pressure'}
out=[];cur=None
for i,l in enumerate(lines):
    m=re.match(r'^- id: (\S+)$',l)
    if m:
        cur=m.group(1)
        if cur not in keep_dataset:
            out.append(l); out.append('  data: elsewhere'); out.append('  where: DANDI 000946 version 0.250829.1249 (doi:10.48324/dandi.000946/0.250829.1249)'); continue
    out.append(l)
open(p,'w').write('\n'.join(out))
EOF
git diff --stat; python -c "
import yaml;d=yaml.safe_load(open('claims/000463/10.1523-jneurosci.2218-24.2025.yaml'));print(sum(c.get('data')=='elsewhere' for c in d['claims']),len(d['claims']))"
```

```
claims/000463/10.1523-jneurosci.2218-24.2025.yaml | 68 +++++++++++++++++++++++
 1 file changed, 68 insertions(+)
34 37
```

**Agent calls Bash**

```bash
date -u; python -c "
import yaml;d=yaml.safe_load(open('claims/000463/10.1523-jneurosci.2218-24.2025.yaml'));print([c['id'] for c in d['claims']])"
```

```
Fri Oct 30 10:44:44 UTC 2026
['fig4-unit-counts', 'fig4a-s1-rsu-timelocked-3000', 'fig4b-pom-rsu-timelocked-3000', 'fig4-post-3000', 'fig4-30hz-responses', 'fig4-fsu-no-change', 'fig5a-sham-no-response', 'fig5b-control-cg1-no-response', 'fig6a-s1-rsu-timelocked-prf', 'fig6a-s1-rsu-delayed-prf', 'fig6b-s1-fsu-prf', 'fig6c-pom-rsu-prf', 'fig6d-pom-fsu-prf', 'fig7a-s1-rsu-dc-3000', 'fig7b-s1-fsu-dc-3000', 'fig7c-pom-rsu-dc-3000', 'fig7d-pom-fsu-dc-3000', 'fig8a-s1-rsu-dc-30', 'fig8b-s1-fsu-dc-30', 'fig8b-s1-fsu-no-dc-difference-post', 'fig9a-s1-rsu-prf-60dc', 'fig9b-s1-fsu-prf-60dc', 'fig10a-feedback-s1rsu-pomrsu', 'fig10a-pomrsu-s1fsu', 'fig10a-post-decrease', 'fig10b-30hz-dsttc', 'fig10c-sttc-constant-pd', 'fig10d-sttc-60dc', 'fig10e-sttc-30hz-dc', 'fig10f-sttc-3000hz-dc-independent', 'synthesis-prf-pathway', 'fig11-ac-unit-counts', 'fig11b-ac-prf-responses', 'fig11c-ac-s1-30hz-dsttc', 'fig11c-ac-s1fsu-30hz', 'fig11d-ac-s1-3000hz-dsttc', 'methods-insitu-pressure']
```

**Agent calls Write**

```json
{
 "file_path": "entries/000463-gao-2025/make_notebook.py",
 "content": "\"\"\"Writes reproduce_gao_2025.ipynb (without outputs). Kept out of the entry; run once by the author.\"\"\"\n\nimport nbformat as nbf\n\ncells = []\n\n\ndef md(text, tags=None):\n    cells.append(nbf.v4.new_markdown_cell(text.strip(), metadata={\"tags\": tags} if tags else {}))\n\n\ndef code(text, tags=None):\n    cells.append(nbf.v4.new_code_cell(text.strip(), metadata={\"tags\": tags} if tags else {}))\n\n\nmd(\"\"\"\n# Reproducing Gao et al. (2025) from dandiset 000463\n\n**Paper.** Gao H, Ramachandran S, Yu K, He B (2025). Transcranial Focused Ultrasound Modulates\nFeedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively Activating Excitatory\nNeurons. *J Neurosci* 45(23) e2218242025.\n[doi:10.1523/jneurosci.2218-24.2025](https://doi.org/10.1523/jneurosci.2218-24.2025)\n\n**Claims file.** `claims/000463/10.1523-jneurosci.2218-24.2025.yaml`, written from the version of\nrecord as served by PubMed Central (PMC12139594), full text with Methods and legends; the paper has\nno supplement and links no analysis code.\n\n**Target dataset.** DANDI:000463, version `0.250829.1248`\n([doi:10.48324/dandi.000463/0.250829.1248](https://doi.org/10.48324/dandi.000463/0.250829.1248)).\nThe paper cites no version of 000463 (it does not name 000463 at all), so the most recent published\nversion is pinned. All five versions, the draft included, list the same 29 files with the same\nsizes (checked below), so the choice changes nothing.\n\n**Where the paper's data are.** Dandiset 000463 cites the paper in its description, but holds\nbroadband recordings of one S1 probe from four rats (BH395, BH396, BH401, BH444, recorded November\n2022 to February 2023), with no sorted units, no trial or stimulus times, and electrode locations\n\"unknown\". None of its subjects is in the paper's own deposit. The paper says (Methods, \"Data\nacquisition and preprocessing\"): \"All experimental data has been made public in a repository at\nthe DANDI Archive (https://dandiarchive.org/dandiset/000946).\" The claims are therefore marked\n`data: elsewhere` and tested on DANDI:000946, version `0.250829.1249`\n([doi:10.48324/dandi.000946/0.250829.1249](https://doi.org/10.48324/dandi.000946/0.250829.1249)),\nthe most recent published version; the paper cites no version of it, and its six versions list the\nsame files (checked below). Both dandisets are streamed; nothing is downloaded to disk.\n\n**Claims.** 37 in the claims file. 2 are tested, 35 blocked.\n\n| claim | status | reason |\n|---|---|---|\n| fig4-unit-counts | blocked | `metadata_insufficient`: no unit of 000946 is typed (all `celltype_label` 0) and no waveform is deposited |\n| fig4a, fig4b, fig4-post-3000, fig4-30hz-responses, fig4-fsu-no-change | blocked | `metadata_insufficient`: RSU and FSU types needed |\n| fig5a-sham-no-response | blocked | `data_missing`: no sham session in either dandiset |\n| fig5b-control-cg1-no-response | blocked | `data_missing`: no CG1-targeted session (000946 has M1-targeted ones) |\n| fig6a (2), fig6b, fig6c, fig6d, fig7a to fig7d, fig8a, fig8b (2), fig9a, fig9b | blocked | `metadata_insufficient`: RSU and FSU types needed |\n| fig10a (3), fig10b, fig10c to fig10f | blocked | `metadata_insufficient`: pairs are by type |\n| synthesis-prf-pathway | blocked | `metadata_insufficient`: depends on blocked claims |\n| fig11-ac-unit-counts | tested | AC units are untyped in the paper |\n| fig11b-ac-prf-responses | tested | AC units are untyped in the paper |\n| fig11c-ac-s1-30hz-dsttc, fig11c-ac-s1fsu-30hz, fig11d-ac-s1-3000hz-dsttc | blocked | `metadata_insufficient`: S1 RSU or FSU types needed |\n| methods-insitu-pressure | blocked | `data_missing`: no hydrophone scans in either dandiset |\n\"\"\")\n\ncode(\"\"\"\nimport time\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport tfus\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_rows\", 200)\nT0 = time.time()\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\n### Dandiset 000463\n\nEvery file's metadata, read without the voltage data.\n\"\"\")\n\ncode(\"\"\"\nmeta463 = tfus.metadata(tfus.DANDISET, tfus.VERSION)\nprint(meta463[\"name\"])\nprint(\"subjects (archive summary):\", meta463[\"assetsSummary\"][\"numberOfSubjects\"],\n      \"| variables:\", meta463[\"assetsSummary\"][\"variableMeasured\"])\na463 = tfus.assets(tfus.DANDISET, tfus.VERSION)\nd463 = pd.DataFrame(tfus.pmap(tfus.describe_000463_file, a463))\nassert \"error\" not in d463 or d463[\"error\"].isna().all()\nprint(d463.drop(columns=[\"path\", \"device\", \"acquisition\"]).to_string())\nprint()\nprint(\"files:\", len(d463), \"| subjects:\", d463.subject.nunique(), sorted(d463.subject.unique()))\nprint(\"devices:\", d463.device.unique(), \"| acquisition series:\", d463.acquisition.unique())\nprint(\"files with units:\", int(d463.units.sum()), \"| with any intervals table:\", int((d463.intervals != \"none\").sum()),\n      \"| with stimulus series:\", int((d463.stimulus != \"none\").sum()))\nprint(\"recording length, s: %.1f to %.1f; trials at 2.5 s per trial: %.0f to %.0f\"\n      % (d463.duration_s.min(), d463.duration_s.max(), d463.duration_s.min() / 2.5, d463.duration_s.max() / 2.5))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe 29 files hold 32-channel broadband voltage at 24414 Hz and a 3052 Hz LFP of one NeuroNexus\nA1x32 probe each, from the four subjects the archive lists. There is no units table, no trials or\nepochs table and no stimulus series, and every electrode's location is \"unknown\" (the electrode\ngroup's is the placeholder \"brain area\"). Conditions appear only in the identifier (for example\n`BH401_3000_200_67_5V`, PRF 3000 Hz, PD 200 us, UD 67 ms, 5 V, or `BH396_test5_24V`). The\ndescription says recordings have 200 or 500 trials; the recording lengths give about 121 to 515\nstimulation intervals of 2.5 s. The paper's analyses need units of S1 and POm (or AC), their types\nand the sonication onsets, and the paper says 500 trials per condition and two probes per rat; none\nof this can be read from 000463.\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor ds in (tfus.DANDISET, tfus.PAPER_DANDISET):\n    vs = tfus.versions(ds)\n    pinned = tfus.VERSION if ds == tfus.DANDISET else tfus.PAPER_VERSION\n    ref = {(a[\"path\"], a[\"size\"]) for a in tfus.assets(ds, pinned)}\n    for v in vs:\n        cur = {(a[\"path\"], a[\"size\"]) for a in tfus.assets(ds, v)}\n        rows.append(dict(dandiset=ds, version=v, files=len(cur), differ_from_pinned=len(cur ^ ref)))\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nEvery version of each dandiset lists the same paths with the same sizes as the pinned one.\n\n### Dandiset 000946, the paper's deposit\n\nEvery file's metadata, the units' spike counts and type labels, and the trial table, read without\nthe spike times (only 2000 spike times per file enter a signature used to find duplicates).\n\"\"\")\n\ncode(\"\"\"\nmeta946 = tfus.metadata(tfus.PAPER_DANDISET, tfus.PAPER_VERSION)\nprint(meta946[\"name\"])\nprint(meta946[\"description\"][:900])\na946 = tfus.assets(tfus.PAPER_DANDISET, tfus.PAPER_VERSION)\nt = time.time()\ns946 = pd.DataFrame(tfus.pmap(tfus.describe_000946_file, a946))\nprint(\"\\\\nfiles read:\", len(s946), \"| failed:\", int(s946[\"error\"].notna().sum()) if \"error\" in s946 else 0,\n      \"| %.0f s\" % (time.time() - t))\ns946[\"kind\"] = np.where(s946.spike_counts.notna(), \"spikes\", \"STTC\")\nprint(s946.groupby(\"kind\").agg(files=(\"path\", \"size\"), GB=(\"size\", lambda x: x.sum() / 1e9)).to_string())\nprint(\"\\\\nsubjects of 000463 found in 000946:\", sorted(set(d463.subject) & set(s946.subject.dropna())))\nprint(\"000946 subjects:\", s946.subject.nunique(), \"| recording dates:\", s946.session_start.min()[:10], \"to\",\n      s946.session_start.max()[:10], \"| 000463 dates:\", d463.session_start.min()[:10], \"to\", d463.session_start.max()[:10])\n\"\"\", tags=[\"sanity\"])\n\ncode(\"\"\"\nsp = s946[s946.kind == \"spikes\"].sort_values(\"path\").copy()\n# Recordings deposited more than once: same trial table, spike-count index and first and last spike times.\ngroups = sp.groupby(\"signature\").path.apply(list)\nprint(\"spike files:\", len(sp), \"| distinct recordings:\", len(groups),\n      \"| recordings by number of copies:\", groups.apply(len).value_counts().sort_index().to_dict())\ndup = sp[sp.duplicated(\"signature\", keep=False)]\nsame_meta = dup.groupby(\"signature\").agg(ids=(\"identifier\", \"nunique\"), notes=(\"notes\", \"nunique\"),\n                                           starts=(\"session_start\", \"nunique\"))\nprint(\"duplicate groups with one identifier:\", int((same_meta.ids == 1).sum()), \"of\", len(same_meta),\n      \"| with one recording note:\", int((same_meta.notes == 1).sum()),\n      \"| with differing session_start_time:\", int((same_meta.starts > 1).sum()))\nfor paths in groups[groups.apply(len) > 1].head(3):\n    print(\"   \", paths)\nuniq = sp.drop_duplicates(\"signature\").copy()\nprint(\"\\\\nEach recording is counted once from here on:\", len(uniq), \"files.\")\n\"\"\", tags=[\"sanity\"])\n\ncode(\"\"\"\nlabels = np.concatenate([l for l in uniq.labels if l is not None])\nprint(\"units:\", int(uniq.spike_counts.apply(len).sum()), \"| with a celltype_label column:\", len(labels))\nprint(\"celltype_label values:\", pd.Series(labels).value_counts().to_dict())\nprint(\"label descriptions:\", uniq.label_description.value_counts().to_dict())\nprint(\"unit columns:\", uniq.unit_columns.value_counts().to_dict())\nprint(\"\\\\ntrials per recording:\", uniq.n_trials.value_counts().head(8).to_dict())\nprint(\"trial stop minus start, s: %.3f to %.3f\" % (uniq.trial_len_s.min(), uniq.trial_len_s.max()))\nprint(\"onset to onset, s: %.3f to %.3f (Methods: 2.5 s with 10%% jitter, 2.25 to 2.75)\"\n      % (uniq.isi_min.min(), uniq.isi_max.max()))\n# The identifier's PRF and PD against the data_collection text of the same file.\ndc = uniq.data_collection.str.extract(r\"PRF:(\\\\d+)Hz PD:([\\\\d.]+)us UD:(\\\\d+)ms\")\nok = (dc[0].astype(float) == uniq.prf) & (dc[1].astype(float) == uniq.pd_us)\nprint(\"files whose data_collection gives PRF and PD:\", int(dc[0].notna().sum()), \"| agree with identifier:\", int(ok.sum()))\nprint(\"files whose identifier does not parse:\", uniq.identifier[uniq.prf.isna()].tolist())\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe units table of every spike file has a `celltype_label` column described as \"label 1 = RSU,\nlabel 2 = FSU\", but every one of its values is 0, and 34 files have no such column. No waveform, and\nno IP or AHP measure, is deposited, so the RSU and FSU types of the paper (Methods, \"Neuronal type\nclassification\": k-means on each spike's initial phase and afterhyperpolarization period) cannot\nbe assigned. Trials last 2.2 s in the table and onsets are 2.25 to 2.75 s apart, as the Methods\nsay. Most recordings have 500 trials, as the description says; some have 400 to 499.\n\"\"\")\n\ncode(\"\"\"\nrecs = uniq.copy()\nrecs[\"group\"] = np.where(recs.subject.isin(recs[recs.area == \"ac\"].subject), \"AC group\",\n                         np.where(recs.subject.isin(recs[recs.area == \"pom\"].subject), \"POm group\", \"other\"))\nprint(\"recordings by area recorded and target stimulated (from general/notes):\")\nprint(pd.crosstab(recs.area, recs.target).to_string())\nprint(\"\\\\nsubjects by group:\", recs.groupby(\"group\").subject.unique().apply(sorted).to_dict())\nprint(\"\\\\nidentifier suffixes:\", recs.suffix.value_counts().to_dict())\nprint(\"\\\\nrecordings targeted at S1 with plain identifiers, by PRF and PD (us), per area:\")\nplain = recs[(recs.target == \"s1\") & recs.suffix.isin([\"\", \"_POM_S1\"])]\nprint(pd.crosstab([plain.prf, plain.pd_us], plain.area).to_string())\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe files record one area each; the two probes of one recording are two files with the same\nidentifier and trial table. Areas recorded are S1, POm, AC, M1 and a few others, and targets are\nS1, M1 and POm (identifier suffixes `_MOTOR`, `_POM_MOTOR` and `_POM_POM`). There is no session\nwithout ultrasound (sham, Figure 5A) and none targeted at the cingulate cortex CG1 (control, Figure\n5B); M1-targeted sessions exist, which the paper does not describe. The PRF and PD pairs cover the\npaper's constant-PD series (PD 200 us), its DC series at 3000 Hz (PD 2, 20, 100, 200, 300 us) and at\n30 Hz (PD 200, 2000, 10000, 20000, 30000 us), and its 60% DC series, and add series at 1500, 300 and\n4500 Hz that the paper does not report. The AC group has 7 subjects (paper: 12) and the subjects\nwith POm recordings number 10 (paper: 16).\n\n### Clock of the spikes and the trial table\n\nThe AC recordings of the constant-PD series (the data of the two tested claims) and the S1\nrecordings of the same sessions are loaded. The two files of one session must have the same\ntrial table, and the population rate must respond at the trial onsets and not at times shifted\ninto the middle of the intersonication interval.\n\"\"\")\n\ncode(\"\"\"\nac_files = recs[(recs.area == \"ac\") & (recs.target == \"s1\") & (recs.pd_us == 200) & (recs.suffix == \"\")]\ns1_mates = recs[(recs.area == \"s1\") & recs.identifier.isin(ac_files.identifier)]\nt = time.time()\nloaded = {d[\"path\"]: d for d in tfus.pmap(tfus.load_spikes, [dict(path=p, asset_id=a) for p, a in\n          zip(pd.concat([ac_files, s1_mates]).path, pd.concat([ac_files, s1_mates]).asset_id)])}\nprint(\"files loaded:\", len(loaded), \"| failed:\", sum(\"error\" in d for d in loaded.values()), \"| %.0f s\" % (time.time() - t))\nrows = []\nfor _, a in ac_files.iterrows():\n    mate = s1_mates[s1_mates.identifier == a.identifier]\n    same = [np.array_equal(loaded[a.path][\"onsets\"], loaded[m][\"onsets\"]) for m in mate.path]\n    rows.append(dict(identifier=a.identifier, trials=a.n_trials, s1_files=len(mate), same_trial_table=all(same) and len(same) > 0))\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\", tags=[\"sanity\"])\n\ncode(\"\"\"\ndef population_psth(files, shift=0.0, edges=np.arange(-0.2, 0.5001, 0.01)):\n    total = np.zeros(len(edges) - 1)\n    n_trials = 0\n    for p in files:\n        d = loaded[p]\n        on = d[\"onsets\"] + shift\n        for u in d[\"units\"]:\n            if len(u) > tfus.MIN_SPIKES:\n                rel = np.concatenate([u[(u >= o + edges[0]) & (u < o + edges[-1])] - o for o in on])\n                total += np.histogram(rel, edges)[0]\n        n_trials += len(on)\n    return edges, total / total[edges[:-1] < 0].mean()\n\nfor area, files in ((\"AC\", ac_files.path), (\"S1\", s1_mates.path)):\n    for shift in (0.0, 1.0):\n        e, r = population_psth(files, shift)\n        during = r[(e[:-1] >= 0) & (e[:-1] < 0.067)].mean()\n        post = r[(e[:-1] >= 0.201) & (e[:-1] < 0.268)].mean()\n        print(f\"{area}, onsets shifted by {shift:.1f} s: rate relative to -200 to 0 ms, 0 to 67 ms {during:.3f}, \"\n              f\"201 to 268 ms {post:.3f}, peak {r.max():.2f} at {e[np.argmax(r)] * 1000:.0f} ms\")\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nEvery AC recording of the series has an S1 file with the identical trial table. At the true onsets\nthe pooled AC and S1 rates rise after onset (numbers above), and with the onsets moved 1 s later,\ninto the intersonication interval, they stay near 1. So the trial `start_time` is consistent with the\nsonication onset on the spike clock; that it is the onset to the millisecond is not shown.\n\n## Blocked claims\n\nEvery claim on S1 or POm units uses the RSU and FSU types, which 000946 does not give (all\n`celltype_label` values are 0) and which cannot be computed without waveforms. The counts below show\nwhat the dataset holds for the unit counts of Figures 4 and 6, untyped; they decide no outcome.\n\"\"\")\n\ncode(\"\"\"\ndef count_units(df, threshold=tfus.MIN_SPIKES):\n    return df.spike_counts.apply(lambda c: int((c > threshold).sum()))\n\npom_subjects = recs[(recs.area == \"pom\") & (recs.target == \"s1\")].subject.unique()\nmain = recs[(recs.target == \"s1\") & recs.subject.isin(pom_subjects) & recs.area.isin([\"s1\", \"pom\"])\n            & recs.suffix.isin([\"\", \"_POM_S1\", \"_POM _S1\"])].copy()\nmain[\"units\"] = count_units(main)\ncp = main[main.pd_us == 200]\ntab = cp.pivot_table(index=\"prf\", columns=\"area\", values=\"units\", aggfunc=\"sum\")\ntab[\"sessions\"] = cp[cp.area == \"s1\"].groupby(\"prf\").size()\nprint(\"Units with more than 2000 spikes, untyped, in the constant-PD series of the subjects with POm recordings:\")\nprint(tab.to_string())\nprint(\"Paper (RSU + FSU): 3000 Hz S1 312 + 54 = 366, POm 233 + 17 = 250; 30 Hz S1 148 + 61 = 209, POm 189 + 43 = 232;\"\n      \" all five PRFs S1 1050 + 247 = 1297, POm 913 + 106 = 1019.\")\nprint(\"Totals over five PRFs here: S1\", int(tab[\"s1\"].sum()), \"POm\", int(tab[\"pom\"].sum()))\n\"\"\")\n\nmd(\"\"\"\n## fig11-ac-unit-counts\n\n> The auditory-confound analysis rests on 453 AC neurons over the PRFs, with 83, 107, 104 and 100\n> neurons in the 30, 1500, 3000 and 4500 Hz sessions.\n\nAC units with more than 2000 spikes in the session (M1), counted once per session, per PRF. The\ncriterion names two readings of the sessions: the constant-PD series (PD 200 us, which the Methods\nuse for \"the PRF effect exploration\") and every AC session the dataset labels with these PRFs.\n\"\"\")\n\ncode(\"\"\"\nacr = recs[(recs.area == \"ac\") & (recs.target == \"s1\") & (recs.suffix == \"\")].copy()\nacr[\"units\"] = count_units(acr)\nacr[\"all_units\"] = acr.spike_counts.apply(len)\nexpected = {\"all\": 453, 30: 83, 1500: 107, 3000: 104, 4500: 100}\n\ndef count_table(df):\n    by = df.groupby(\"prf\").agg(sessions=(\"path\", \"size\"), subjects=(\"subject\", \"nunique\"),\n                               units=(\"units\", \"sum\"), units_no_threshold=(\"all_units\", \"sum\"))\n    by.loc[\"all\"] = by.sum()\n    return by\n\nfor name, df in ((\"(a) constant-PD series, PD 200 us\", acr[acr.pd_us == 200]),\n                 (\"(b) every AC session with these PRFs, all PDs\", acr)):\n    tab = count_table(df)\n    tab[\"paper\"] = [expected.get(k, np.nan) for k in tab.index]\n    tab[\"within_10pct\"] = [abs(u - e) <= 0.1 * e if e == e else np.nan for u, e in zip(tab.units, tab.paper)]\n    print(name); print(tab.to_string())\n    print(\"counts within tolerance:\", int(np.nansum(tab.within_10pct.astype(float))), \"of 5\\\\n\")\nprint(\"Constant-PD series by session:\")\nprint(acr[acr.pd_us == 200][[\"identifier\", \"n_trials\", \"all_units\", \"units\"]].to_string(index=False))\n\"\"\", tags=[\"claim:fig11-ac-unit-counts\"])\n\nmd(\"\"\"\n**Result: not reproduced.** In the constant-PD series the dandiset has 112, 138, 167 and 127 AC units\nwith more than 2000 spikes at 30, 1500, 3000 and 4500 Hz (633 with 89 at 300 Hz), against 83, 107,\n104, 100 and 453; none of the five counts is within 10%. Taking every AC session with these PRFs\ngives larger counts still, also none within tolerance. The series comes from 6 of the 7 AC-group\nsubjects, 3 or 4 sessions per PRF.\n\"\"\")\n\nmd(\"\"\"\n## fig11b-ac-prf-responses\n\n> AC neurons show time-locked responses to 1500 and 3000 Hz PRF tFUS targeting S1 and\n> postsonication responses to 30, 1500, 3000 and 4500 Hz, with the least response to 300 Hz.\n\nAC units of the constant-PD series (selected as above), normalized rate (M3) in 0 to 67 ms and 201\nto 268 ms. Kruskal-Wallis across the five PRFs at p < 0.01, then each PRF against baseline,\none-tailed greater, Bonferroni-corrected p < 0.01 (M4). Every reading of O2 (normalization), O3\n(baseline sample) and O4 (Bonferroni factor: 2 windows, or 5 PRFs) is run. The constant-PD series is\ntaken from the Methods (\"For the PRF effect exploration, the pulse duration (PD) was set at 200 μs\nfor all the PRFs\"); every AC session at these PRFs is shown as a variant.\n\"\"\")\n\ncode(\"\"\"\nPRFS = [30, 300, 1500, 3000, 4500]\n\ndef unit_rates(files):\n    rows = []\n    for _, f in files.iterrows():\n        d = loaded[f.path]\n        for k, u in enumerate(d[\"units\"]):\n            if len(u) <= tfus.MIN_SPIKES:\n                continue\n            r = dict(subject=f.subject, identifier=f.identifier, prf=int(f.prf), unit=k)\n            for o2 in \"ab\":\n                r[f\"pre2_{o2}\"] = tfus.normalized_rate(u, d[\"onsets\"], tfus.WIN_PRE2, o2)\n                r[f\"during_{o2}\"] = tfus.normalized_rate(u, d[\"onsets\"], tfus.WIN_DURING, o2)\n                r[f\"post_{o2}\"] = tfus.normalized_rate(u, d[\"onsets\"], tfus.WIN_POST, o2)\n            rows.append(r)\n    return pd.DataFrame(rows)\n\ndef judge(R):\n    out, detail = [], []\n    for o2 in \"ab\":\n        kw = {w: stats.kruskal(*[R[R.prf == p][f\"{w}_{o2}\"].dropna() for p in PRFS]).pvalue for w in (\"during\", \"post\")}\n        means = {w: {p: R[R.prf == p][f\"{w}_{o2}\"].mean() for p in PRFS} for w in (\"during\", \"post\")}\n        for o3 in \"abc\":\n            raw = {}\n            for w in (\"during\", \"post\"):\n                for p in PRFS:\n                    x = R[R.prf == p][[f\"{w}_{o2}\", f\"pre2_{o2}\"]].dropna()\n                    raw[(w, p)] = tfus.baseline_test(x[f\"{w}_{o2}\"], x[f\"pre2_{o2}\"], o3)\n            for o4, k in ((\"a\", 2), (\"b\", 5)):\n                sig = {key: tfus.bonferroni(v, k) < tfus.ALPHA for key, v in raw.items()}\n                named = [sig[(\"during\", 1500)], sig[(\"during\", 3000)], sig[(\"post\", 30)], sig[(\"post\", 1500)],\n                         sig[(\"post\", 3000)], sig[(\"post\", 4500)]]\n                excluded_ok = not any(sig[(\"during\", p)] for p in (30, 300, 4500)) and not sig[(\"post\", 300)]\n                lowest = all(min(means[w], key=means[w].get) == 300 for w in (\"during\", \"post\"))\n                kw_ok = kw[\"during\"] < tfus.ALPHA and kw[\"post\"] < tfus.ALPHA\n                if kw_ok and all(named) and excluded_ok and lowest:\n                    outcome = \"reproduced\"\n                elif kw_ok and sum(named) >= 4:\n                    outcome = \"partially_reproduced\"\n                else:\n                    outcome = \"not_reproduced\"\n                out.append(dict(O2=o2, O3=o3, O4=f\"{o4} (x{k})\", KW_during=kw[\"during\"], KW_post=kw[\"post\"],\n                                named_held=sum(named), exclusions_hold=excluded_ok, lowest_300=lowest, outcome=outcome,\n                                significant_during=\",\".join(str(p) for p in PRFS if sig[(\"during\", p)]),\n                                significant_post=\",\".join(str(p) for p in PRFS if sig[(\"post\", p)])))\n                for key, v in raw.items():\n                    detail.append(dict(O2=o2, O3=o3, O4=o4, window=key[0], prf=key[1], p_raw=v,\n                                       p_corrected=tfus.bonferroni(v, k)))\n    return pd.DataFrame(out), pd.DataFrame(detail)\n\nR = unit_rates(ac_files)\nprint(\"units:\", len(R), \"| by PRF:\", R.groupby(\"prf\").size().to_dict(),\n      \"| without a prestimulation spike (dropped, O2a):\", int(R.during_a.isna().sum()))\nsummary = R.groupby(\"prf\")[[\"during_a\", \"post_a\", \"during_b\", \"post_b\", \"pre2_a\", \"pre2_b\"]].agg([\"mean\", \"sem\", \"median\"])\nprint(summary.round(1).to_string())\nprint(\"ranges, O2a: during %.1f to %.1f, post %.1f to %.1f\" % (R.during_a.min(), R.during_a.max(), R.post_a.min(), R.post_a.max()))\nres, det = judge(R)\nprint(res.to_string(index=False, float_format=lambda v: \"%.3g\" % v))\n\"\"\", tags=[\"claim:fig11b-ac-prf-responses\"])\n\ncode(\"\"\"\nprint(\"Raw and corrected p of each PRF against baseline, reading O2a (one-tailed greater):\")\npiv = det[det.O2 == \"a\"].pivot_table(index=[\"window\", \"prf\"], columns=[\"O3\", \"O4\"], values=\"p_corrected\")\nprint(piv.to_string(float_format=lambda v: \"%.2g\" % v))\nprint(\"\\\\nBy subject (one session per subject and PRF): mean normalized rate, O2a, and units\")\nby = R.groupby([\"prf\", \"subject\"]).agg(units=(\"unit\", \"size\"), during=(\"during_a\", \"mean\"), post=(\"post_a\", \"mean\"))\nprint(by.round(1).to_string())\nprint(\"\\\\nSessions whose mean is above 100%:\",\n      {w: f\"{int((by[w] > 100).sum())} of {len(by)}\" for w in (\"during\", \"post\")})\n\"\"\", tags=[\"claim:fig11b-ac-prf-responses\"])\n\ncode(\"\"\"\n# Variant: every AC session at these PRFs, all PDs (the second reading of the session set in\n# fig11-ac-unit-counts). Loads the remaining AC files.\nrest = acr[~acr.path.isin(loaded)]\nt = time.time()\nloaded.update({d[\"path\"]: d for d in tfus.pmap(tfus.load_spikes, [dict(path=p, asset_id=a) for p, a in zip(rest.path, rest.asset_id)])})\nprint(\"files loaded:\", len(rest), \"| %.0f s\" % (time.time() - t))\nR_all = unit_rates(acr[acr.prf.isin(PRFS)])\nprint(\"units:\", len(R_all), \"| by PRF:\", R_all.groupby(\"prf\").size().to_dict())\nprint(R_all.groupby(\"prf\")[[\"during_a\", \"post_a\"]].mean().round(1).to_string())\nres_all, _ = judge(R_all)\nprint(res_all.to_string(index=False, float_format=lambda v: \"%.3g\" % v))\n\"\"\", tags=[\"claim:fig11b-ac-prf-responses\"])\n\nmd(\"\"\"\n**Result: partially reproduced, resting on the assumption of the O2a normalization.** Under O2a (mean\nwindow rate over mean prestimulation rate) both Kruskal-Wallis tests are significant, the six named\nresults hold (1500 and 3000 Hz during sonication; 30, 1500, 3000 and 4500 Hz after it), 300 Hz has the\nlowest mean in both windows, and 300 Hz is not significant after sonication; but 4500 Hz is also\nsignificant during sonication under every O3 and O4 reading, and 30 Hz under some, where the claim\nsays only 1500 and 3000 Hz respond. Under O2b (mean of per-trial ratios) the means of every PRF and\nwindow, and of the 134 to 67 ms baseline window, are 55 to 75%, the during-sonication\nKruskal-Wallis test is not significant, and no named result holds under most O3 readings; the claim\nis not reproduced under it. With every AC session at these PRFs (all PDs) the outcome under O2a is\nalso partial.\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\n| claim | outcome |\n|---|---|\n| fig11-ac-unit-counts | not reproduced: 0 of 5 counts within 10% (dataset has more AC units) |\n| fig11b-ac-prf-responses | partially reproduced (assumed O2a): named responses hold, but 4500 Hz also responds during sonication |\n| 30 claims on S1 and POm units by type, and synthesis-prf-pathway | blocked, `metadata_insufficient` |\n| fig5a-sham-no-response, fig5b-control-cg1-no-response, methods-insitu-pressure | blocked, `data_missing` |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nHow the analysis differs from the paper's. The data are from 000946, the paper's deposit, not the\ntarget 000463. The AC sessions are those of the dataset's constant-PD series (6 subjects; the paper\nreports 12 rats in the AC group). The normalization of the rate, the baseline sample and the\nBonferroni factor are not fixed by the paper; every reading is shown.\n\nWhat was found about the dataset. Dandiset 000463 cites the paper but holds none of its recordings:\nbroadband voltage of one S1 probe from four other rats, with no units, no trial or stimulus times\nand no electrode locations. The paper's deposit 000946 holds sorted units and trial tables, but every\nunit's `celltype_label` is 0 although the column says 1 is RSU and 2 is FSU, and no waveforms are\ndeposited, so the paper's RSU and FSU types cannot be recovered; most spike files are deposited\ntwice under different file names and session start times; there are no sham or CG1-targeted\nsessions; and it holds more AC units than the paper reports.\n\"\"\")\n\ncode(\"\"\"\nprint(\"notebook runtime: %.1f min\" % ((time.time() - T0) / 60))\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb[\"cells\"] = cells\nnb[\"metadata\"] = {\"kernelspec\": {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}}\nnbf.write(nb, \"reproduce_gao_2025.ipynb\")\n"
}
```

```
File created successfully at: entries/000463-gao-2025/make_notebook.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000463-gao-2025 && mv make_notebook.py $TMPDIR/ && sed -i 's/rest = acr\[~acr.path.isin(loaded)\]/rest = acr[acr.prf.isin(PRFS) \& ~acr.path.isin(list(loaded))]/' $TMPDIR/make_notebook.py && source $TMPDIR/env/bin/activate && uv pip install -q nbformat nbconvert ipykernel 2>&1|tail -1; python $TMPDIR/make_notebook.py && ls; printf "h5py\nnumpy\npandas\nremfile\nrequests\nscipy\n" > requirements.in; cat ../001453-fouke-2025/README.md | head -30
```

```
__pycache__
reproduce_gao_2025.ipynb
tfus.py
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
[... 12 more lines not kept]
```

**Agent**

Now run the notebook in the dev env to check it works and time it.

**Agent calls Bash**

```bash
rm -rf __pycache__ && source $TMPDIR/env/bin/activate && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_gao_2025.ipynb --output $TMPDIR/run1.ipynb 2>&1 | tail -5
```

```
Fri Oct 30 10:46:37 UTC 2026
[36mFile [39m[32mpandas/_libs/lib.pyx:3390[39m, in [36mpandas._libs.lib.map_infer[39m[34m()[39m
[32m-> [39m[32m3390[39m [33m'Could not get source, probably due dynamically evaluated source code.'[39m

[31mTypeError[39m: '<' not supported between instances of 'float' and 'str'


real	3m30.693s
user	1m24.780s
sys	0m5.872s
```

**Agent calls Bash**

```bash
cat > $TMPDIR/harness.py <<'EOF'
import sys, os, pickle, json, hashlib
sys.path.insert(0,'.')
import tfus
orig=tfus.pmap
def cached(fn, items, workers=8):
    key=hashlib.md5((fn.__name__+json.dumps([i['path'] for i in items])).encode()).hexdigest()
    p=os.path.join(os.environ['TMPDIR'],'pm_'+key+'.pkl')
    if os.path.exists(p): return pickle.load(open(p,'rb'))
    r=orig(fn,items,workers); pickle.dump(r,open(p,'wb')); return r
tfus.pmap=cached
nb=json.load(open('reproduce_gao_2025.ipynb'))
g={}
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print(f'----- cell {i}', c['metadata'].get('tags'))
    exec(''.join(c['source']), g)
EOF
cd entries/000463-gao-2025 && sed -i 's/print("\\\\nsubjects by group:", recs.groupby("group").subject.unique().apply(sorted).to_dict())/print("\\\\nsubjects by group:", recs.groupby("group").subject.unique().apply(lambda s: sorted(x for x in s if isinstance(x, str))).to_dict())/' $TMPDIR/make_notebook.py && grep -n "subjects by group" $TMPDIR/make_notebook.py && source $TMPDIR/env/bin/activate && python $TMPDIR/make_notebook.py && python $TMPDIR/harness.py 2>&1 | tail -150
```

```
201:print("\\nsubjects by group:", recs.groupby("group").subject.unique().apply(lambda s: sorted(x for x in s if isinstance(x, str))).to_dict())
BH539_1500_200_67_5     500         1              True
  BH539_30_200_67_5     500         1              True
BH539_3000_200_67_5     500         1              True
BH547_4500_200_67_5     500         1              True
  BH547_30_200_67_5     500         1              True
----- cell 14 ['sanity']
AC, onsets shifted by 0.0 s: rate relative to -200 to 0 ms, 0 to 67 ms 1.099, 201 to 268 ms 1.540, peak 1.56 at 250 ms
AC, onsets shifted by 1.0 s: rate relative to -200 to 0 ms, 0 to 67 ms 0.954, 201 to 268 ms 0.924, peak 1.06 at -180 ms
S1, onsets shifted by 0.0 s: rate relative to -200 to 0 ms, 0 to 67 ms 1.268, 201 to 268 ms 1.189, peak 1.29 at 30 ms
S1, onsets shifted by 1.0 s: rate relative to -200 to 0 ms, 0 to 67 ms 0.966, 201 to 268 ms 0.984, peak 1.02 at -180 ms
----- cell 16 None
Units with more than 2000 spikes, untyped, in the constant-PD series of the subjects with POm recordings:
area    pom   s1  sessions
prf                       
30.0    315  390        17
300.0   249  293        14
1500.0  236  312        16
3000.0  339  320        15
4500.0  290  333        16
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cat > $TMPDIR/h2.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR']+'/harness.py').read().split("nb=json.load")[0])
import json
nb=json.load(open('reproduce_gao_2025.ipynb')); g={}
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code' and i<=14: 
        import contextlib,io
        with contextlib.redirect_stdout(io.StringIO()): exec(''.join(c['source']),g)
import numpy as np
for area, files in (("AC", g['ac_files'].path), ("S1", g['s1_mates'].path)):
    e,r=g['population_psth'](files,0.0,edges=np.arange(-0.4,0.4001,0.02))
    print(area,' '.join(f'{x*1000:.0f}:{y:.2f}' for x,y in zip(e[:-1],r)))
EOF
python $TMPDIR/h2.py
```

```
AC -400:1.00 -380:0.99 -360:1.00 -340:1.00 -320:1.02 -300:1.01 -280:1.02 -260:0.99 -240:0.98 -220:1.00 -200:1.00 -180:0.98 -160:0.98 -140:0.98 -120:0.99 -100:1.00 -80:1.01 -60:1.01 -40:1.03 -20:1.02 0:1.09 20:1.08 40:1.11 60:1.15 80:1.13 100:1.18 120:1.32 140:1.40 160:1.44 180:1.48 200:1.51 220:1.54 240:1.56 260:1.50 280:1.45 300:1.39 320:1.36 340:1.37 360:1.37 380:1.36
S1 -400:1.01 -380:1.00 -360:0.99 -340:1.00 -320:1.01 -300:1.02 -280:1.01 -260:1.02 -240:1.00 -220:0.99 -200:1.00 -180:1.00 -160:1.00 -140:0.99 -120:0.99 -100:0.98 -80:0.98 -60:0.98 -40:1.01 -20:1.00 0:1.27 20:1.27 40:1.27 60:1.10 80:1.01 100:1.04 120:1.06 140:1.08 160:1.10 180:1.10 200:1.15 220:1.17 240:1.18 260:1.21 280:1.17 300:1.14 320:1.14 340:1.15 360:1.17 380:1.15
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && python $TMPDIR/harness.py 2>&1 | sed -n '/cell 4/,/cell 13/p' | grep -v "^ *BH\|^[0-9]* *BH" | head -120
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && python $TMPDIR/harness.py > $TMPDIR/h.out 2>&1; grep -n "cell" $TMPDIR/h.out | head; sed -n '/cell 3 /,/cell 13 /p' $TMPDIR/h.out | cut -c1-250 | grep -v "^ \{0,3\}[0-9]\{1,2\} \+BH" | head -150
```

```
1:----- cell 1 None
2:----- cell 3 ['sanity']
44:----- cell 5 ['sanity']
57:----- cell 7 ['sanity']
69:----- cell 8 ['sanity']
77:----- cell 9 ['sanity']
78:units: 23473 | with a celltype_label column: 22617
79:celltype_label values: {0.0: 22617}
81:unit columns: {'spike_times,celltype_label': 782, 'spike_times': 33}
88:----- cell 11 ['sanity']
----- cell 3 ['sanity']
Electrophysiological Recordings in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation
subjects (archive summary): 4 | variables: ['LFP', 'ElectricalSeries', 'ProcessingModule', 'ElectrodeGroup']
               identifier subject        session_start   samples  channels     rate_hz unit   duration_s  lfp_rate_hz intervals  units stimulus electrode_location group_location

files: 29 | subjects: 4 ['BH395', 'BH396', 'BH401', 'BH444']
devices: <StringArray>
['A1x32-Poly3-10mm-50-177-A32']
Length: 1, dtype: str | acquisition series: <StringArray>
['ElectricalSeries']
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/env/bin/activate && cat > $TMPDIR/h3.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR']+'/harness.py').read().split("nb=json.load")[0])
import json, contextlib, io
nb=json.load(open('reproduce_gao_2025.ipynb')); g={}
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code' and i<=11:
        with contextlib.redirect_stdout(io.StringIO()): exec(''.join(c['source']),g)
sp=g['sp']; uniq=g['uniq']
d=sp[sp.duplicated('signature',keep=False)]
bad=d.groupby('signature').filter(lambda x: x.notes.nunique()>1)
print(bad[['path','identifier','notes','session_start']].sort_values(['identifier','path']).to_string())
dc=uniq.data_collection.str.extract(r"PRF:(\d+)Hz PD:([\d.]+)us UD:(\d+)ms")
ok=(dc[0].astype(float)==uniq.prf)&(dc[1].astype(float)==uniq.pd_us)
print(uniq[dc[0].notna() & ~ok][['path','identifier','data_collection']])
EOF
python $TMPDIR/h3.py
```

```
path                      identifier                          notes        session_start
1    sub-BH494/sub-BH494_ses-20230817T132800_ecephys.nwb             BH494_1500_200_67_5    recording:S1;stimulation:S1  2023-08-17T13:28:00
2    sub-BH494/sub-BH494_ses-20230817T132836_ecephys.nwb             BH494_1500_200_67_5       Recording:S1; stim at:S1  2023-08-17T13:28:36
3    sub-BH494/sub-BH494_ses-20230820T123700_ecephys.nwb             BH494_1500_200_67_5    recording:M1;stimulation:S1  2023-08-20T12:37:00
4    sub-BH494/sub-BH494_ses-20230820T123756_ecephys.nwb             BH494_1500_200_67_5       Recording:M1; stim at:S1  2023-08-20T12:37:56
0                        sub-BH494/sub-BH494_ecephys.nwb       BH494_1500_200_67_5_MOTOR       Recording:M1; stim at:M1  2023-08-21T13:40:17
21   sub-BH494/sub-BH494_ses-20230820T210000_ecephys.nwb       BH494_1500_200_67_5_MOTOR    recording:S1;stimulation:M1  2023-08-20T21:00:00
22   sub-BH494/sub-BH494_ses-20230820T210030_ecephys.nwb       BH494_1500_200_67_5_MOTOR       Recording:S1; stim at:M1  2023-08-20T21:00:30
23   sub-BH494/sub-BH494_ses-20230821T134000_ecephys.nwb       BH494_1500_200_67_5_MOTOR    recording:M1;stimulation:M1  2023-08-21T13:40:00
24   sub-BH494/sub-BH494_ses-20230821T134017_ecephys.nwb       BH494_1500_200_67_5_MOTOR       Recording:M1; stim at:M1  2023-08-21T13:40:17
5    sub-BH494/sub-BH494_ses-20230820T125000_ecephys.nwb        BH494_1500_200_67_5_NEAR    recording:S1;stimulation:S1  2023-08-20T12:50:00
6    sub-BH494/sub-BH494_ses-20230820T125042_ecephys.nwb        BH494_1500_200_67_5_NEAR       Recording:S1; stim at:S1  2023-08-20T12:50:42
7    sub-BH494/sub-BH494_ses-20230820T131000_ecephys.nwb        BH494_1500_200_67_5_NEAR    recording:M1;stimulation:S1  2023-08-20T13:10:00
8    sub-BH494/sub-BH494_ses-20230820T131032_ecephys.nwb        BH494_1500_200_67_5_NEAR       Recording:M1; stim at:S1  2023-08-20T13:10:32
9    sub-BH494/sub-BH494_ses-20230820T144500_ecephys.nwb  BH494_1500_200_67_5_
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='make_notebook.py'; s=open(p).read()
old='''same_meta = dup.groupby("signature").agg(ids=("identifier", "nunique"), notes=("notes", "nunique"),
                                           starts=("session_start", "nunique"))
print("duplicate groups with one identifier:", int((same_meta.ids == 1).sum()), "of", len(same_meta),
      "| with one recording note:", int((same_meta.notes == 1).sum()),
      "| with differing session_start_time:", int((same_meta.starts > 1).sum()))'''
new='''same_meta = dup.groupby("signature").agg(ids=("identifier", "nunique"), notes=("notes", "nunique"),
                                           areas=("area", "nunique"), starts=("session_start", "nunique"))
print("duplicate groups with one identifier:", int((same_meta.ids == 1).sum()), "of", len(same_meta),
      "| with one notes text:", int((same_meta.notes == 1).sum()),
      "| with one recorded area once the notes are parsed:", int((same_meta.areas == 1).sum()),
      "| with differing session_start_time:", int((same_meta.starts > 1).sum()))
for sig in same_meta.index[same_meta.areas > 1]:
    print("  same content, different areas:")
    print(dup[dup.signature == sig][["path", "identifier", "notes"]].to_string(index=False))'''
assert old in s; s=s.replace(old,new)
old2='''The units table of every spike file has a `celltype_label` column described as "label 1 = RSU,
label 2 = FSU", but every one of its values is 0, and 34 files have no such column.'''
new2='''Most duplicate copies differ only in their file name, their session start time (by seconds) and
the wording of `general/notes`; the group printed above holds one recording's spikes under both an
S1 and a POm file, so at least one of them is labelled with the wrong area. The units table of
nearly every spike file has a `celltype_label` column described as "label 1 = RSU, label 2 = FSU",
but every one of its values is 0, and 33 recordings have no such column.'''
assert old2 in s; s=s.replace(old2,new2)
old3='''Trials last 2.2 s in the table'''
new3='''The PRF and PD of the identifier agree with the `data_collection` text in every file that has
both (the one other file, `BH594_coating_3000_200_10`, has an identifier that does not parse). Trials last 2.2 s in the table'''
assert old3 in s; s=s.replace(old3,new3)
old4='''              f"201 to 268 ms {post:.3f}, peak {r.max():.2f} at {e[np.argmax(r)] * 1000:.0f} ms")'''
new4='''              f"201 to 268 ms {post:.3f}, peak {r.max():.2f} at {e[np.argmax(r)] * 1000:.0f} ms")
    e, r = population_psth(files, 0.0, edges=np.arange(-0.1, 0.1401, 0.02))
    print(f"   {area}, 20 ms bins from -100 ms:", " ".join(f"{x * 1000:.0f}:{y:.2f}" for x, y in zip(e[:-1], r)))'''
assert old4 in s; s=s.replace(old4,new4)
old5='''into the intersonication interval, they stay near 1. So the trial `start_time`'''
new5='''into the intersonication interval, they stay near 1. In 20 ms bins the S1 rate steps up in the
bin that starts at 0 ms and falls back after 60 ms, the length of the 67 ms sonication. So the trial `start_time`'''
assert old5 in s; s=s.replace(old5,new5)
old6='''Under O2b (mean of per-trial ratios) the means of every PRF and
window, and of the 134 to 67 ms baseline window, are 55 to 75%, the during-sonication
Kruskal-Wallis test is not significant, and no named result holds under most O3 readings; the claim
is not reproduced under it. With every AC session at these PRFs (all PDs) the outcome under O2a is
also partial.'''
new6='''Under O2b (mean of per-trial ratios, trials without a prestimulation spike left out) the
means of every PRF and window, the 134 to 67 ms baseline window included, are 54 to 74%, the
during-sonication Kruskal-Wallis test is not significant (p = 0.021), and at most 2 of the 6 named
results hold; the claim is not reproduced under it. O2a is adopted: under O2b a window with an
unchanged rate does not come out near 100%, while the paper reports its normalized rates on a scale
where 100% is no change (sham and control p = 1.0, responses of 106 to 159%). The mean responses
differ much between sessions (by subject, above). With every AC session at these PRFs (all PDs) the
outcome under O2a is also partial, and there 300 Hz is not the lowest.'''
assert old6 in s; s=s.replace(old6,new6)
open(p,'w').write(s)
EOF
cd entries/000463-gao-2025 && source $TMPDIR/env/bin/activate && python $TMPDIR/make_notebook.py && python $TMPDIR/harness.py > $TMPDIR/h.out 2>&1; sed -n '/cell 8 /,/cell 9 /p;/cell 14/,/cell 16/p' $TMPDIR/h.out
```

```
----- cell 8 ['sanity']
spike files: 1550 | distinct recordings: 815 | recordings by number of copies: {1: 84, 2: 728, 3: 2, 4: 1}
duplicate groups with one identifier: 731 of 731 | with one notes text: 704 | with one recorded area once the notes are parsed: 730 | with differing session_start_time: 27
  same content, different areas:
                                               path                identifier                     notes
sub-BH499/sub-BH499_ses-20231024T210100_ecephys.nwb BH499_300_200_67_5_POM_S1  Recording:S1; stim at:S1
sub-BH499/sub-BH499_ses-20231024T210103_ecephys.nwb BH499_300_200_67_5_POM_S1  Recording:S1; stim at:S1
sub-BH499/sub-BH499_ses-20231024T210200_ecephys.nwb BH499_300_200_67_5_POM_S1 Recording:POM; stim at:S1
sub-BH499/sub-BH499_ses-20231024T210247_ecephys.nwb BH499_300_200_67_5_POM_S1 Recording:POM; stim at:S1
    ['sub-BH528/sub-BH528_ses-20231001T181700_ecephys.nwb', 'sub-BH528/sub-BH528_ses-20231001T181725_ecephys.nwb']
    ['sub-BH553/sub-BH553_ses-20240308T150100_ecephys.nwb', 'sub-BH553/sub-BH553_ses-20240308T150131_ecephys.nwb']
    ['sub-BH513/sub-BH513_ses-20231007T165000_ecephys.nwb', 'sub-BH513/sub-BH513_ses-20231007T165030_ecephys.nwb']

Each recording is counted once from here on: 815 files.
----- cell 9 ['sanity']
----- cell 14 ['sanity']
AC, onsets shifted by 0.0 s: rate relative to -200 to 0 ms, 0 to 67 ms 1.099, 201 to 268 ms 1.540, peak 1.56 at 250 ms
AC, onsets shifted by 1.0 s: rate relative to -200 to 0 ms, 0 to 67 ms 0.954, 201 to 268 ms 0.924, peak 1.06 at -180 ms
   AC, 20 ms bins from -100 ms: -100:0.99 -80:0.99 -60:1.00 -40:1.02 -20:1.01 0:1.07 20:1.06 40:1.09 60:1.14 80:1.11 100:1.16 120:1.30
S1, onsets shifted by 0.0 s: rate relative to -200 to 0 ms, 0 to 67 ms 1.268, 201 to 268 ms 1.189, peak 1.29 at 30 ms
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/000463-gao-2025 && rm -rf __pycache__ && cat > entry.yaml <<'EOF'
schema_version: 1
name: 000463-gao-2025
type: reproduction
title: Ultrasound modulation of cortico-thalamo-cortical pathways (Gao et al. 2025)
description: Tests the findings of Gao, Ramachandran, Yu and He (2025) on transcranial focused
  ultrasound of rat S1. Dandiset 000463 cites the paper but holds only broadband S1 recordings of four
  other rats, without units or trial times, so the claims are tested on the paper's own deposit,
  dandiset 000946. Its units are not typed as RSU or FSU, so only the auditory cortex claims can be
  tested, the unit counts and the responses to five PRFs.
license: Apache-2.0
notebooks:
- path: reproduce_gao_2025.ipynb
  title: Reproducing Gao et al. (2025) from dandisets 000463 and 000946
  runtime_minutes: 5
helpers:
- tfus.py
related:
- id: dandi:000463/0.250829.1248
  relation: uses_data
- id: dandi:000946/0.250829.1249
  relation: uses_data
- id: doi:10.1523/jneurosci.2218-24.2025
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/000463-gao-2025 2>&1 | tail -3 && python tools/entry.py check entries/000463-gao-2025 2>&1 | tail -10
```

```
Fri Oct 30 10:56:57 UTC 2026
wrote entries/000463-gao-2025/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000463-gao-2025 2>&1 | tail -15
```

```
Installed kernelspec registry-000463-gao-2025 in executed/000463-gao-2025/.venv/share/jupyter/kernels/registry-000463-gao-2025
0 error(s)
pass  reproduce_gao_2025.ipynb  (251 s)

real	4m16.953s
user	2m2.167s
sys	0m10.276s
```

**Agent calls Bash**

```bash
ls executed/000463-gao-2025/; python - <<'EOF'
import json
nb=json.load(open('executed/000463-gao-2025/reproduce_gao_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i<15: continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        print(f'--- {i}', ''.join(t)[:3500])
EOF
```

```
reproduce_gao_2025.ipynb
result.json
--- 16 Units with more than 2000 spikes, untyped, in the constant-PD series of the subjects with POm recordings:
area    pom   s1  sessions
prf                       
30.0    315  390        17
300.0   249  293        14
1500.0  236  312        16
3000.0  339  320        15
4500.0  290  333        16
Paper (RSU + FSU): 3000 Hz S1 312 + 54 = 366, POm 233 + 17 = 250; 30 Hz S1 148 + 61 = 209, POm 189 + 43 = 232; all five PRFs S1 1050 + 247 = 1297, POm 913 + 106 = 1019.
Totals over five PRFs here: S1 1648 POm 1429

--- 18 (a) constant-PD series, PD 200 us
        sessions  subjects  units  units_no_threshold  paper within_10pct
prf                                                                      
30.0           3         3    112                 129   83.0        False
300.0          3         3     89                  92    NaN          NaN
1500.0         4         4    138                 140  107.0        False
3000.0         3         3    167                 172  104.0        False
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^findings:/,$p' attempts/001453-fouke-2025-01.yaml | head -40; python -c "
import json; s=json.load(open('schemas/attempt.schema.json')); print(json.dumps(s['properties']['findings'],indent=0)[:1500]); print(json.dumps(s['properties']['inputs'],indent=0)[:600])"
```

```
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
- kind: metadata_error
  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
    only Danio rerio; the files hold 37 fish of two species.
[... 81 more lines not kept]
```

**Agent**

Fixing two sentences in the notebook text, then writing the record.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='make_notebook.py'; s=open(p).read()
old='''Most duplicate copies differ only in their file name, their session start time (by seconds) and
the wording of `general/notes`; the group printed above'''
new='''The copies of a recording differ in their file names; in 27 groups the session start time also
differs by seconds, and in 27 the wording of `general/notes`. The group printed above'''
assert old in s; s=s.replace(old,new)
old='''but 4500 Hz is also
significant during sonication under every O3 and O4 reading, and 30 Hz under some, where the claim
says only 1500 and 3000 Hz respond.'''
new='''but 4500 Hz is also
significant during sonication under every O3 and O4 reading, 30 Hz under four of the six and
300 Hz under the two O3b readings, where the claim says only 1500 and 3000 Hz respond.'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cd entries/000463-gao-2025 && source $TMPDIR/env/bin/activate && python $TMPDIR/make_notebook.py && cd ../.. && python tools/entry.py check entries/000463-gao-2025 | tail -2; date -u
```

```
0 error(s)
Fri Oct 30 11:01:45 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/record.py <<'EOF'
import yaml
TYPED = ("The paper's deposit DANDI:000946 holds sorted units and trial tables for these sessions, but every "
         "unit's celltype_label is 0 (the column says 1 is RSU and 2 is FSU), 33 recordings have no such column, "
         "and no waveforms are deposited, so the RSU and FSU types the claim needs (Methods, Neuronal type "
         "classification, k-means on each spike's IP and AHP) cannot be assigned.")
SER = {"const": "the constant-PD series (PD 200 us)", "dc3000": "the 3000 Hz DC series (PD 2, 20, 100, 200, 300 us)",
       "dc30": "the 30 Hz DC series (PD 200, 2000, 10000, 20000, 30000 us)", "dc60": "the 60% DC series"}
def typed(claim, extra=""):
    return dict(claim=claim, outcome="blocked", blocked_by="metadata_insufficient",
                notebook="reproduce_gao_2025.ipynb", notes=(TYPED + " " + extra).strip())
out = []
out.append(dict(claim="fig4-unit-counts", outcome="blocked", blocked_by="metadata_insufficient",
    notebook="reproduce_gao_2025.ipynb",
    notes=TYPED + " The criterion compares counts by type, so none of the 12 can be compared. Untyped, the "
          "constant-PD series of the 10 subjects with POm recordings holds 320 S1 and 339 POm units with more "
          "than 2000 spikes at 3000 Hz (paper, RSU plus FSU, 366 and 250), 390 and 315 at 30 Hz (209 and 232), "
          "and 1648 and 1429 over the five PRFs (1297 and 1019); these totals decide nothing. The sorting itself "
          "is the paper's (units are deposited); it is not redone."))
for c, s in [("fig4a-s1-rsu-timelocked-3000", ""), ("fig4b-pom-rsu-timelocked-3000", ""), ("fig4-post-3000", ""),
             ("fig4-30hz-responses", ""), ("fig4-fsu-no-change", "")]:
    out.append(typed(c, "The 3000 Hz 60% DC and 30 Hz 0.6% DC sessions with S1 and POm recordings are in 000946."))
out.append(dict(claim="fig5a-sham-no-response", outcome="blocked", blocked_by="data_missing",
    notebook="reproduce_gao_2025.ipynb",
    notes="No sham session (no tFUS) is in 000463 or in the paper's deposit 000946: every recording of 000946 names "
          "a PRF and PD in its identifier and a stimulation target in its notes, and 000463 has no trial times at "
          "all. The S1 and POm units would also need types, which 000946 does not give."))
out.append(dict(claim="fig5b-control-cg1-no-response", outcome="blocked", blocked_by="data_missing",
    notebook="reproduce_gao_2025.ipynb",
    notes="No session targeted at the cingulate cortex CG1 is in 000463 or 000946. 000946 has sessions targeted at "
          "M1 (identifier suffixes _MOTOR and _POM_MOTOR, notes 'stim at:M1') and at POm, which the paper does not "
          "describe; they are not the paper's control and were not used. The units would also need types."))
for c in ["fig6a-s1-rsu-timelocked-prf", "fig6a-s1-rsu-delayed-prf", "fig6b-s1-fsu-prf", "fig6c-pom-rsu-prf",
          "fig6d-pom-fsu-prf"]:
    out.append(typed(c, f"Recordings of {SER['const']} are in 000946."))
for c in ["fig7a-s1-rsu-dc-3000", "fig7b-s1-fsu-dc-3000", "fig7c-pom-rsu-dc-3000", "fig7d-pom-fsu-dc-3000"]:
    out.append(typed(c, f"Recordings of {SER['dc3000']} are in 000946."))
for c in ["fig8a-s1-rsu-dc-30", "fig8b-s1-fsu-dc-30", "fig8b-s1-fsu-no-dc-difference-post"]:
    out.append(typed(c, f"Recordings of {SER['dc30']} are in 000946."))
for c in ["fig9a-s1-rsu-prf-60dc", "fig9b-s1-fsu-prf-60dc"]:
    out.append(typed(c, f"Recordings of {SER['dc60']} are in 000946."))
STTC = ("000946 also holds 370 files of precomputed STTC (undirected, A to B, B to A, within each area) per pair, "
        "trial and 67 ms window from -67 to 603 ms, for POm, M1 and AC against S1; their pairs are untyped too.")
for c in ["fig10a-feedback-s1rsu-pomrsu", "fig10a-pomrsu-s1fsu", "fig10a-post-decrease", "fig10b-30hz-dsttc",
          "fig10c-sttc-constant-pd", "fig10d-sttc-60dc", "fig10e-sttc-30hz-dc", "fig10f-sttc-3000hz-dc-independent"]:
    out.append(typed(c, "The claim's pairs are of S1 and POm units by type. " + STTC))
out.append(dict(claim="synthesis-prf-pathway", outcome="blocked", blocked_by="metadata_insufficient",
    notebook="reproduce_gao_2025.ipynb",
    notes="Depends on fig6a-s1-rsu-timelocked-prf, fig6c-pom-rsu-prf and fig10d-sttc-60dc, which are blocked "
          "because the units of 000946 are not typed."))
out.append(dict(claim="fig11-ac-unit-counts", outcome="not_reproduced", notebook="reproduce_gao_2025.ipynb",
    output="claim:fig11-ac-unit-counts", measured=[633, 112, 138, 167, 127],
    notes="AC units with more than 2000 spikes, each recording counted once. In the constant-PD series (6 of the 7 "
          "AC-group subjects, 3 or 4 sessions per PRF, 500 trials each) the dandiset has 633 units, 112 at 30 Hz, "
          "89 at 300 Hz, 138 at 1500 Hz, 167 at 3000 Hz and 127 at 4500 Hz, against 453, 83, 107, 104 and 100; "
          "none of the five counts is within 10%, and every one is higher. Under the second reading (every AC "
          "session at these PRFs, all PDs, 147 sessions) the counts are 1111 to 1196 per PRF, none within "
          "tolerance. Without the 2000-spike selection the constant-PD counts are 667 in all. Counting the "
          "duplicate copies of 000946 would double them.",
    deviations=["Tested on the paper's deposit DANDI:000946 (`data: elsewhere`); the target 000463 holds no units.",
                "Recordings deposited more than once in 000946 are counted once."]))
out.append(dict(claim="fig11b-ac-prf-responses", outcome="partially_reproduced", assumed=True,
    notebook="reproduce_gao_2025.ipynb", output="claim:fig11b-ac-prf-responses",
    notes="633 AC units of the constant-PD series, none dropped. Under O2a, Kruskal-Wallis across PRFs p = 7.8e-6 "
          "during sonication and 5.2e-49 after it; mean normalized rates during 105.9, 99.7, 140.3, 107.1 and "
          "108.0% at 30, 300, 1500, 3000 and 4500 Hz, after 176.4, 94.3, 147.9, 310.5 and 210.8%, so 300 Hz is "
          "lowest in both windows. 1500 and 3000 Hz are significant during sonication and 30, 1500, 3000 and 4500 "
          "Hz after it under every O3 and O4 reading (6 of 6 named results), and 300 Hz is not significant after "
          "it. But 4500 Hz is also significant during sonication under all six O3 and O4 readings (corrected p "
          "4.2e-5 to 0.009), 30 Hz under four and 300 Hz under the two O3b readings, where the claim has only 1500 "
          "and 3000 Hz responding. Under O2b every mean, the -134 to -67 ms baseline included, is 54 to 74%, the "
          "during-sonication Kruskal-Wallis test gives p = 0.021, and at most 2 of the 6 named results hold (not "
          "reproduced). Session means vary widely (1500 Hz 99 to 302% during sonication; 3000 Hz 112 to 654% "
          "after it). With every AC session at these PRFs (all PDs) the outcome under O2a is also partial and 300 "
          "Hz is not the lowest. Question for the paper's authors (finding): how was the normalized rate formed, "
          "the ratio of mean counts or the mean of per-trial ratios.",
    deviations=["Tested on the paper's deposit DANDI:000946 (`data: elsewhere`), constant-PD series of the AC group, "
                "6 subjects (the paper reports 12 rats in the AC group) and 633 units where the paper has 453.",
                "Assumed the normalized rate is the mean count in the window over the mean count in the 67 ms before "
                "onset (O2a). The Methods say only that the rate 'was normalized to 67 ms before each stimulation'. "
                "The other reading (O2b, mean of per-trial ratios) puts an unchanged window near 60% where the "
                "paper's scale has 100% for no change (sham and control p = 1.0, responses of 106 to 159%), so O2a "
                "is the reading the paper supports. Under O2b the claim is not reproduced; both are shown.",
                "Sessions are the constant-PD series, from the Methods, Transcranial focused ultrasound stimulation, "
                "paragraph 3 ('For the PRF effect exploration, the pulse duration (PD) was set at 200 μs for all the "
                "PRFs'); every AC session at these PRFs is shown as a variant.",
                "Sonication onset is the trial start_time, as the files' general/stimulus says; the notebook shows "
                "the population rate rising at it and not at times shifted by 1 s."]))
for c in ["fig11c-ac-s1-30hz-dsttc", "fig11c-ac-s1fsu-30hz", "fig11d-ac-s1-3000hz-dsttc"]:
    out.append(typed(c, "The AC neurons are untyped in the paper, but the claim pairs them with S1 RSUs or FSUs. " + STTC))
out.append(dict(claim="methods-insitu-pressure", outcome="blocked", blocked_by="data_missing",
    notebook="reproduce_gao_2025.ipynb",
    notes="The hydrophone scans of Figure 1C are in neither 000463 (voltage recordings only) nor 000946 (units, "
          "trial tables and STTC only); the paper does not say they were deposited."))

findings = [
 dict(kind="other", statement="Dandiset 000463 cites this paper as its detailed description, but holds none of the "
      "recordings the paper analyses. Its 29 files are 32-channel broadband and LFP recordings of one S1 probe from "
      "rats BH395, BH396, BH401 and BH444 (November 2022 to February 2023), with intensities given in volts in the "
      "identifiers; the paper's deposit, dandiset 000946, has 19 other subjects recorded from August 2023, two areas "
      "per recording and 500 trials per condition. None of the paper's claims can be tested on 000463."),
 dict(kind="data_missing", statement="The files of 000463 have no units, no trials or epochs table and no "
      "stimulus series, so the sonication onsets and the conditions' trials cannot be read; the conditions appear "
      "only in the identifiers (for example BH401_3000_200_67_5V, BH396_test5_24V). The description says 200 or 500 "
      "trials per recording; the recording lengths give 121 to 515 intervals of 2.5 s."),
 dict(kind="metadata_insufficient", statement="In 000463 every electrode's location is 'unknown' and the electrode "
      "group's location is the placeholder 'brain area', so the recorded area is not stated."),
 dict(kind="metadata_error", statement="In 000946 the units table's celltype_label column is described as "
      "'label 1 = RSU, label 2 = FSU', but all 22617 values in it are 0, and 33 recordings have no such column. No "
      "waveforms or waveform measures are deposited, so the RSU and FSU types on which 33 of the paper's findings "
      "rest cannot be recovered."),
 dict(kind="other", statement="Most recordings of 000946 are deposited more than once under different file names: of "
      "1550 spike files, 728 recordings have two copies, 2 have three and 1 has four (same trial table, spike "
      "counts and first and last spike times); 84 have one."),
 dict(kind="metadata_error", statement="In 000946 one recording, BH499_300_200_67_5_POM_S1, has identical spikes in "
      "two files noted 'Recording:S1' and two noted 'Recording:POM', so at least one area label is wrong and that "
      "session's other area may be missing."),
 dict(kind="data_missing", statement="000946 holds no sham sessions and no sessions targeted at CG1, the paper's "
      "control (Figure 5), and not the hydrophone scans of Figure 1C. It holds M1- and POm-targeted sessions and "
      "PRF series at 300, 1500 and 4500 Hz that the paper does not describe."),
 dict(kind="selection_undocumented", statement="The AC group of 000946 has 7 subjects and the subjects with POm "
      "recordings number 10, where the paper reports 12 and 16 rats. The constant-PD AC sessions hold 633 units "
      "with more than 2000 spikes where the paper reports 453, and each PRF count is higher; which sessions and units "
      "the paper used is not documented."),
 dict(kind="methods_unavailable", statement="Question for the paper's authors: is the normalized spiking rate the "
      "mean count in the window divided by the mean count in the 67 ms before onset, or the mean over trials of "
      "per-trial ratios? fig11b-ac-prf-responses is partially reproduced under the first and not reproduced under "
      "the second; the attempt assumed the first. Also, is 'against baseline' a rank-sum test against the "
      "prestimulation window (all 100%), against another window, or a signed-rank test against 100%, and is the "
      "Bonferroni factor the number of windows or of parameter levels? These did not change the outcome here."),
]
rec = dict(schema_version=2, id="000463-gao-2025-01",
    dataset=dict(archive="dandi", id="000463", version="0.250829.1248", doi="10.48324/dandi.000463/0.250829.1248"),
    paper="doi:10.1523/jneurosci.2218-24.2025", date="2026-10-30", entry="000463-gao-2025",
    provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
        agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-12"),
        runner=dict(platform="GitHub Actions", url="https://github.com/catalystneuro/encore/actions/runs/41034930656")),
    inputs=[dict(what="The paper's own deposit, dandiset 000946 (units, trial tables and identifiers of the AC group "
                 "and the S1 and POm recordings), on which the claims marked `data: elsewhere` are tested.",
                 source="doi:10.48324/dandi.000946/0.250829.1249")],
    outcomes=out, findings=findings)
class D(yaml.SafeDumper): pass
D.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s))
open("attempts/000463-gao-2025-01.yaml", "w").write(yaml.dump(rec, Dumper=D, sort_keys=False, width=100, allow_unicode=True))
EOF
python $TMPDIR/record.py && python tools/entry.py check entries/000463-gao-2025 | tail -5; grep -c "claim:" attempts/000463-gao-2025-01.yaml; head -30 attempts/000463-gao-2025-01.yaml
```

```
0 error(s)
39
schema_version: 2
id: 000463-gao-2025-01
dataset:
  archive: dandi
  id: '000463'
  version: 0.250829.1248
  doi: 10.48324/dandi.000463/0.250829.1248
paper: doi:10.1523/jneurosci.2218-24.2025
date: '2026-10-30'
entry: 000463-gao-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-12
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/so the RSU and FSU types on which 33 of the paper.s findings "\n      "rest/X/' $TMPDIR/record.py && python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/record.py'; s=open(p).read()
s=s.replace('''"waveforms or waveform measures are deposited, so the RSU and FSU types on which 33 of the paper's findings "
      "rest cannot be recovered."''','''"waveforms or waveform measures are deposited, so the RSU and FSU types, on which 31 of the 37 claims "
      "rest directly, cannot be recovered."''')
open(p,'w').write(s)
p=os.environ['TMPDIR']+'/make_notebook.py'; s=open(p).read()
old="| 30 claims on S1 and POm units by type, and synthesis-prf-pathway | blocked, `metadata_insufficient` |"
assert old in s
s=s.replace(old,"| 31 claims on S1 and POm units by type (fig4 to fig10, fig11c, fig11d) and synthesis-prf-pathway | blocked, `metadata_insufficient` |")
open(p,'w').write(s)
EOF
grep -n "31 of the 37" $TMPDIR/record.py; python $TMPDIR/record.py; cd entries/000463-gao-2025 && source $TMPDIR/env/bin/activate && python $TMPDIR/make_notebook.py; deactivate; cd ../..; grep -c "" attempts/000463-gao-2025-01.yaml
```

```
109:      "waveforms or waveform measures are deposited, so the RSU and FSU types, on which 31 of the 37 claims "
453
```

**Agent**

Now the entry README, then the full run.

**Agent calls Write**

```json
{
 "file_path": "entries/000463-gao-2025/README.md",
 "content": "# Gao, Ramachandran, Yu & He (2025) from dandiset 000463\n\nTests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) on\ntranscranial focused ultrasound of rat S1. [DANDI:000463](https://dandiarchive.org/dandiset/000463/0.250829.1248)\ncites the paper but holds only broadband recordings of one S1 probe from four other rats, with no\nunits, trial times or electrode locations. The paper names its own deposit,\n[DANDI:000946](https://dandiarchive.org/dandiset/000946/0.250829.1249), and the claims are tested\nthere. Its units carry no RSU or FSU type (every `celltype_label` is 0) and no waveforms, so only the\nclaims on auditory cortex units, which the paper does not type, can be tested.\n\n| Claim | Outcome |\n|---|---|\n| AC unit counts, 453 over the PRFs (Figure 11) | Not reproduced |\n| AC responses to five PRFs (Figure 11) | Partially reproduced (resting on an assumption) |\n| S1 and POm responses and correlations by cell type (Figures 4, 6 to 10, 11C and 11D; 31 claims) and the Discussion's synthesis | Blocked: metadata insufficient |\n| Sham and CG1 control sessions (Figure 5), hydrophone scans (Figure 1C) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000463-gao-2025-01.yaml`](../../attempts/000463-gao-2025-01.yaml).\n"
}
```

```
File created successfully at: entries/000463-gao-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/000463-gao-2025 2>&1 | tail -3
```

```
Fri Oct 30 11:03:02 UTC 2026
Installed kernelspec registry-000463-gao-2025 in executed/000463-gao-2025/.venv/share/jupyter/kernels/registry-000463-gao-2025
0 error(s)
pass  reproduce_gao_2025.ipynb  (255 s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/000463-gao-2025/reproduce_gao_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i>14: continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','') or o.get('ename','')
        print(f'--- {i}', ''.join(t)[:1500])
EOF
```

```
--- 3 Electrophysiological Recordings in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation
subjects (archive summary): 4 | variables: ['LFP', 'ElectricalSeries', 'ProcessingModule', 'ElectrodeGroup']

--- 3                identifier subject        session_start   samples  channels     rate_hz unit   duration_s  lfp_rate_hz intervals  units stimulus electrode_location group_location
0         BH395_3000Hz_5V   BH395  2022-12-13T17:40:39  31021056        32  24414.0625    V  1270.622454       3051.8      none  False     none            unknown     brain area
1        BH395_3000Hz_55V   BH395  2022-12-13T18:08:53  31137792        32  24414.0625    V  1275.403960       3051.8      none  False     none            unknown     brain area
2         BH395_300Hz_55V   BH395  2022-12-13T18:31:40  31440896        32  24414.0625    V  1287.819100       3051.8      none  False     none            unknown     brain area
3          BH395_30Hz_55V   BH395  2022-12-13T18:55:47  30742528        32  24414.0625    V  1259.213947       3051.8      none  False     none            unknown     brain area
4         BH395_3000Hz_6V   BH395  2022-12-13T19:58:34  12773376        32  24414.0625    V   523.197481       3051.8      none  False     none            unknown     brain area
5         BH396_test5_24V   BH396  2022-11-17T21:54:47   7505920        32  24414.0625    V   307.442483       3051.8      none  False     none            unknown     brain area
6          BH396_test5_5V   BH396  2022-11-17T22:04:34   7383040        32  24414.0625    V   302.409318       3051.8      none  False     none            unknown     brain area
7          BH396_test5_4V   BH396  2022-11-17T22:10:38   7411712        32  
--- 5 dandiset       version  files  differ_from_pinned
  000463         draft     29                   0
  000463 0.250711.1756     29                   0
  000463 0.250711.1947     29                   0
  000463 0.250828.1934     29            
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/make_notebook.py'; s=open(p).read()
old="Every AC recording of the series has an S1 file with the identical trial table. At the true onsets"
assert old in s
s=s.replace(old,"Of the 17 AC recordings of the series, 16 have an S1 file with the same identifier, and in each the trial table is identical; BH537_1500_200_67_5 has no S1 file. At the true onsets")
open(p,'w').write(s)
EOF
cd entries/000463-gao-2025 && source $TMPDIR/env/bin/activate && python $TMPDIR/make_notebook.py && deactivate && cd ../.. && python tools/entry.py all entries/000463-gao-2025 2>&1 | tail -2 && python tools/entry.py handover entries/000463-gao-2025 2>&1 | tail -5; ls executed/000463-gao-2025/handover; date -u
```

```
0 error(s)
pass  reproduce_gao_2025.ipynb  (251 s)
wrote executed/000463-gao-2025/handover
10.1523-jneurosci.2218-24.2025.yaml
reproduce_gao_2025.ipynb
tfus.py
Fri Oct 30 11:12:01 UTC 2026
```

**Agent calls Bash**

```bash
git status --short; python -c "
import json;nb=json.load(open('executed/000463-gao-2025/reproduce_gao_2025.ipynb'));print(''.join(nb['cells'][-1]['outputs'][0]['text']))"
```

```
M claims/000463/10.1523-jneurosci.2218-24.2025.yaml
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
?? attempts/000463-gao-2025-01.yaml
?? entries/000463-gao-2025/
?? scripts
notebook runtime: 4.1 min
```

**Agent calls Bash**

```bash
ls -la entries/000463-gao-2025; ls scripts | head; git log -1 --format=%cd
```

```
total 80
drwxr-xr-x   4 runner runner  4096 Oct 30 11:03 .
drwxr-xr-x 103 runner runner  4096 Oct 30 10:03 ..
drwxr-xr-x   3 runner runner  4096 Oct 30 10:46 .claude
-rw-r--r--   1 runner runner  1479 Oct 30 11:03 README.md
drwxr-xr-x   2 runner runner  4096 Oct 30 10:57 __pycache__
-rw-r--r--   1 runner runner   955 Oct 30 10:56 entry.yaml
-rw-r--r--   1 runner runner 35313 Oct 30 11:07 reproduce_gao_2025.ipynb
-rw-r--r--   1 runner runner    41 Oct 30 10:46 requirements.in
-rw-r--r--   1 runner runner   788 Oct 30 10:56 requirements.lock.txt
-rw-r--r--   1 runner runner 10252 Oct 30 10:40 tfus.py
scripts
Fri Oct 30 05:38:24 2026 -0400
```

**Agent calls Bash**

```bash
find entries/000463-gao-2025/.claude scripts -maxdepth 3 | head; cat .gitignore | head -20
```

```
entries/000463-gao-2025/.claude
entries/000463-gao-2025/.claude/.cc-writes
scripts
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
.DS_Store
executed/
site/
paper/
targets/local.json
```

**Agent calls Bash**

```bash
date -u
```

```
Fri Oct 30 11:12:13 UTC 2026
```

**Agent**

I did steps 1 to 5 and ran the handover (step 6). Of 37 claims, 2 could be tested, on the paper's own dandiset 000946 because 000463 holds none of the paper's data. The other 35 are blocked. The checks and the clean run both pass.

**1. Outcomes**

| claim | outcome |
|---|---|
| fig11-ac-unit-counts | not_reproduced: in the dataset's 200 µs series there are 633 AC units against the paper's 453. Per PRF it is 112, 138, 167 and 127 against 83, 107, 104 and 100, so none of the 5 counts is within 10%. |
| fig11b-ac-prf-responses | partially_reproduced, resting on an assumption: all 6 named responses hold and 300 Hz is the lowest in both windows. But 4500 Hz also responds during sonication under every test reading. |
| 31 claims on S1 or POm units by cell type (fig4 to fig10, fig11c, fig11d) | blocked, `metadata_insufficient` |
| synthesis-prf-pathway | blocked, `metadata_insufficient` (it depends on blocked claims) |
| fig5a (sham), fig5b (CG1 control), methods-insitu-pressure | blocked, `data_missing` |

**2. The data**

- **000463 (pinned 0.250829.1248, the latest; all versions hold the same files):** it cites the paper but holds none of its recordings. It has broadband recordings from one S1 probe in four rats (BH395, BH396, BH401, BH444) made in 2022–23. There are no units, no trial or stimulus times, and every electrode location is "unknown". None of these rats is in 000946.
- **Where the claims were tested:** the paper names 000946 as its deposit. I marked 34 claims `data: elsewhere` with `where:` pointing at 000946 version 0.250829.1249. I changed no statement, expected value or criterion.
- **What 000946 has:**
  - **No cell types:** every `celltype_label` is 0, although the column says 1 is RSU and 2 is FSU. 33 recordings have no such column, and no waveforms are deposited, so RSU/FSU typing cannot be redone.
  - **Duplicates:** 728 recordings are deposited twice, 2 three times and 1 four times.
  - **One mislabelled recording:** BH499_300_200_67_5_POM_S1 has the same spikes in files labelled S1 and POm.
  - **Missing sessions:** there are no sham or CG1 sessions; there are M1-targeted ones instead.
  - **Fewer animals:** 7 AC-group rats against the paper's 12, and 10 rats with POm recordings against 16.
- **Clock check:** S1 firing steps up at the trial start and falls back after about 60 ms. With onsets shifted by 1 s there is no response.
- **Assumption (fig11b):** the normalized rate is the mean count in a window over the mean count in the 67 ms before onset. The other reading, a mean of per-trial ratios, puts an unchanged window near 60% where the paper treats 100% as no change. Under that reading the claim is not reproduced; both are shown.
- **Questions for the paper's authors** are recorded as a `methods_unavailable` finding: how the rate was normalized, what "against baseline" was compared with, and the Bonferroni factor. Only the normalization changed an outcome.
- **No questions to a reader.**

**3. Where the protocol was unclear**

1. It does not say who sets `data: elsewhere` and `where:`. Both live in the claims file, which the author otherwise must not touch. I set them in the claims file, because the author steps say to give `where` and the check tool reads it from there.
2. It does not say whether `elsewhere` applies when the paper's data are in another dataset of the same archive. I applied it to 000946.
3. Fig5a, fig5b and the pressure claim have data in neither dandiset. I kept them `data: dataset` with `data_missing`, as the protocol says for data that are not public anywhere.
4. The entry's `related` field had no slot for a second dataset with a different role. I listed both dandisets as `uses_data`.

**4. Runtime and failures**

The run took about 1 h 35 min, from 09:39 to 11:12 UTC. The notebook runs in 4.1 min (251 s) from a clean environment. Survey reads in threads were very slow (18 min), so I switched to 8 processes, which brought the 000946 survey down to about 3.3 min. Nothing failed in the final run.

Files are in `entries/000463-gao-2025/`:
- reproduce_gao_2025.ipynb
- tfus.py
- README.md
- entry.yaml

The attempt record is `attempts/000463-gao-2025-01.yaml`, and the claims file change is in `claims/000463/10.1523-jneurosci.2218-24.2025.yaml`.

## End of run

71 turns, 90 minutes, result: success.
