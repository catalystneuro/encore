# 000637 · author · run 41182673080

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d50444de-c98b-45ce-9125-575dcc8dd471/tool-results/bznx17v79.txt

Preview (first 2KB):
Sat Oct 31 08:02:45 UTC 2026
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d50444de-c98b-45ce-9125-575dcc8dd471/tool-results/bznx17v79.txt"
}
```

```
1	Sat Oct 31 08:02:45 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-12`. Record this version in the attempt's provenance.
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
ls claims/000637 paper entries/001453-fouke-2025; cat claims/000637/*;
```

```
<persisted-output>
Output too large (54.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d50444de-c98b-45ce-9125-575dcc8dd471/tool-results/bunqgvr1k.txt

Preview (first 2KB):
claims/000637:
10.1523-jneurosci.2218-24.2025.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.1523-jneurosci.2218-24.2025.txt
# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, on dandiset 000637.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d50444de-c98b-45ce-9125-575dcc8dd471/tool-results/bunqgvr1k.txt"
}
```

```
1	claims/000637:
2	10.1523-jneurosci.2218-24.2025.yaml
3	
4	entries/001453-fouke-2025:
5	README.md
6	entry.yaml
7	omr.py
8	reproduce_fouke_2025.ipynb
9	requirements.in
10	requirements.lock.txt
11	
12	paper:
13	10.1523-jneurosci.2218-24.2025.txt
14	# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, on dandiset 000637.
15	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
16	# protocol pilot-10 as stated in docs/protocol.md.
17	#
18	# Text read: the version of record as served by PubMed Central (PMC12139594), full text with
19	# Materials and Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt).
20	# The paper has no supplement. No PDF was supplied. The equation defining the directional spike time
[... 835 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d50444de-c98b-45ce-9125-575dcc8dd471/tool-results/bunqgvr1k.txt",
 "offset": 856
}
```

```
856	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 1; Figure 10B legend
857	  quote: When delivering 30 Hz ultrasound, S1 RSUs to POm FSUs higher correlated (p = 0.0058), while POm RSUs showed
858	    decreased correlation to S1 FSUs during sonication (p = 0.0058)
859	  statistics:
860	  - about: S1 RSU to POm FSU, increase
861	    test: Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon
862	    p: 0.0058
863	  - about: POm RSU to S1 FSU, decrease
864	    test: Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon
865	    p: 0.0058
866	  depends_on:
867	  - unit-counts
868	  criterion: Method D, pairs within the 30 Hz 0.6% DC sessions, window 0 to 67 ms against prestimulation. Reproduced
869	    when, under every reading, S1 RSU to POm FSU is significantly higher and POm RSU to S1 FSU significantly lower
870	    (one-tailed, p < 0.05); partially reproduced when one of the two holds.
871	- id: fig10c-sttc-constant-pd
872	  statement: At constant 200 us pulse duration, the S1 RSU to POm RSU correlation change during sonication does
873	    not depend on PRF, though 1500 Hz gives a higher change than 30 Hz.
874	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 2; Figure 10C
875	  quote: When applying tFUS with constant 200 μs PD, varying the DC and PRF, the correlation did not show PRF-dependent
[... 154 more lines not kept]
```

**Agent**

Read the protocol and claims file. Key open question: the paper says its data are in DANDI:000946, so 000637 may hold only part of it. Next I check the dataset and read the docs and example entry.

**Agent calls Bash**

```bash
cat README.md | head -80; echo ----; cat docs/archives.md | sed -n '1,200p'
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
[... 261 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000637/ | python -m json.tool | head -50; curl -s "https://api.dandiarchive.org/api/dandisets/000637/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
V=0.250829.1249; curl -s "https://api.dandiarchive.org/api/dandisets/000637/versions/" | python -c "import json,sys; [print(r['version'],r['created'],r['size'],r['asset_count']) for r in json.load(sys.stdin)['results']]"; curl -s https://api.dandiarchive.org/api/dandisets/000637/versions/$V/ | python -c "
import json,sys; m=json.load(sys.stdin)
for k in ['description','relatedResource','citation','keywords','wasGeneratedBy','assetsSummary','contributor']:
  print(k, json.dumps(m.get(k),indent=0)[:3000])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
V=0.250829.1249; curl -s "https://api.dandiarchive.org/api/dandisets/000637/versions/$V/assets/?page_size=400" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size'])" > $TMPDIR/assets.txt; head -3 $TMPDIR/assets.txt; awk '{print $1}' $TMPDIR/assets.txt | cut -d/ -f1 | sort | uniq -c; sed -n '2,40p' $TMPDIR/assets.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -80 omr.py; python -c "import pynwb,remfile,h5py;print(pynwb.__version__)"; which python uv
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
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv $TMPDIR/venv -q && . $TMPDIR/venv/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas matplotlib scikit-learn jupyter nbformat nbconvert 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/venv/bin/activate; cat > $TMPDIR/peek.py <<'EOF'
import h5py, remfile, pynwb, sys
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); d=c.get_dandiset("000637","0.250829.1249")
a=d.get_asset_by_path(sys.argv[1]); url=a.get_content_url(follow_redirects=1,strip_query=True)
f=h5py.File(remfile.File(url),'r')
def show(n,o):
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, dict(o.attrs).get('description',''))
    else: print(n, {k:(v if not hasattr(v,'shape') or v.size<5 else v.shape) for k,v in o.attrs.items() if k not in ('namespace','object_id')})
f.visititems(show)
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); n=io.read()
print(n)
print(n.subject)
print(n.units.to_dataframe().head())
print(n.trials.to_dataframe().head() if n.trials is not None else None)
print(n.electrodes.to_dataframe().head())
EOF
python $TMPDIR/peek.py sub-BH401/sub-BH401_obj-1yd986l_ecephys.nwb 2>&1 | grep -v Warn | head -150
```

```
acquisition {}
analysis {}
file_create_date (1,) object 
general {}
general/devices {}
general/devices/array {'description': 'A1x32-Poly3-10mm-50-177-A32', 'manufacturer': 'Neuronexus', 'neurodata_type': 'Device'}
general/extracellular_ephys {}
general/extracellular_ephys/electrodes {'colnames': (8,), 'description': 'all electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (32,) object my description
general/extracellular_ephys/electrodes/group (32,) object my description
general/extracellular_ephys/electrodes/group_name (32,) object my description
general/extracellular_ephys/electrodes/id (32,) int64 
general/extracellular_ephys/electrodes/imp (32,) float64 my description
general/extracellular_ephys/electrodes/location (32,) object my description
general/extracellular_ephys/electrodes/x (32,) float64 my description
general/extracellular_ephys/electrodes/y (32,) float64 my description
general/extracellular_ephys/electrodes/z (32,) float64 my description
general/extracellular_ephys/shank1 {'description': 'electrode group for shank1', 'location': 'brain area', 'neurodata_type': 'ElectrodeGroup'}
general/institution () object 
general/intracellular_ephys {}
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/venv/bin/activate; cat > $TMPDIR/survey.py <<'EOF'
import h5py, remfile, json
from concurrent.futures import ThreadPoolExecutor
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); d=c.get_dandiset("000637","0.250829.1249")
assets=[(a.path,a.get_content_url(follow_redirects=1,strip_query=True)) for a in d.get_assets()]
def one(pu):
    p,u=pu
    f=h5py.File(remfile.File(u),'r')
    r=dict(path=p, ident=f['identifier'][()].decode(), desc=f['session_description'][()].decode(),
      start=f['session_start_time'][()].decode(), nunits=len(f['units/id']), unitcols=list(f['units'].attrs['colnames']),
      ntr=len(f['intervals/trials/id']), trcols=list(f['intervals/trials'].attrs['colnames']),
      nspk=f['units/spike_times'].shape[0],
      loc=sorted(set(x.decode() if isinstance(x,bytes) else str(x) for x in f['general/extracellular_ephys/electrodes/location'][:])),
      dev=[f['general/devices'][k].attrs.get('description','') for k in f['general/devices']],
      groups=[k for k in f['general/extracellular_ephys'] if k!='electrodes'],
      subj={k:f['general/subject'][k][()].decode() for k in f['general/subject']},
      acq=list(f['acquisition']), proc=list(f['processing']), stim=list(f['stimulus/presentation']),
      tr0=float(f['intervals/trials/start_time'][0]), trdur=float(f['intervals/trials/stop_time'][0]-f['intervals/trials/start_time'][0]),
      )
    return r
with ThreadPoolExecutor(16) as ex: res=list(ex.map(one,assets))
json.dump(res,open('/tmp/claude-1001/survey.json' if False else __import__('os').environ['TMPDIR']+'/survey.json','w'),indent=0)
print(len(res))
EOF
time python $TMPDIR/survey.py 2>&1 | grep -v Warn | tail -3
```

```
292

real	3m53.389s
user	0m10.479s
sys	0m1.353s
```

**Agent calls Bash**

```bash
cd $TMPDIR; . venv/bin/activate; python -c "
import json,collections as C
r=json.load(open('survey.json'))
for k in ['desc','unitcols','trcols','loc','dev','groups','acq','proc','stim']:
  print(k, C.Counter(str(x[k]) for x in r).most_common(8))
print(C.Counter(x['ntr'] for x in r).most_common(20))
print(C.Counter(round(x['trdur'],3) for x in r).most_common(5))
print(C.Counter(str(x['subj']) for x in r).most_common(30))
ids=sorted(x['ident'] for x in r); print(ids)
"
```

```
desc [('Neural Spikes for S1 tFUS', 292)]
unitcols [("['spike_times']", 292)]
trcols [("['start_time', 'stop_time']", 292)]
loc [("['unknown']", 292)]
dev [("['A1x32-Poly3-10mm-50-177-A32']", 292)]
groups [("['shank1']", 292)]
acq [('[]', 292)]
proc [('[]', 292)]
stim [('[]', 292)]
[(500, 219), (230, 45), (425, 13), (375, 11), (328, 1), (400, 1), (344, 1), (252, 1)]
[(2.2, 292)]
[("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH458'}", 18), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH464'}", 17), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH446'}", 14), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH469'}", 14), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH453'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH454'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH459'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH462'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH463'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH465'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH466'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH467'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat', 'sex': 'M', 'species': 'Rattus norvegicus', 'subject_id': 'BH470'}", 13), ("{'age': 'P24W', 'description': 'HSD:WI rat
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000946/ | python -m json.tool | head -30; grep -n -i "dandi\|000946\|000637\|available\|github" paper/*.txt | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls claims | grep -c .; ls claims/000946 2>&1; ls entries | grep 946; grep -n "000946\|000637" -r targets/*.yaml targets/*.json | head;
```

```
231
10.1523-jneurosci.2218-24.2025.yaml
targets/description_papers.yaml:49:  "000637":
targets/description_papers.yaml:69:  "000946":
targets/dandisets.json:3193:   "dandiset": "000637",
targets/dandisets.json:3909:   "dandiset": "000946",
```

**Agent calls Bash**

```bash
sed -n 45,80p targets/description_papers.yaml; curl -s "https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=20" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size'])"; curl -s https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/ | python -c "import json,sys; print(json.load(sys.stdin)['description'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls schemas; sed -n 1,80p attempts/001453-fouke-2025-01.yaml; grep -n "elsewhere\|with_inputs\|where" schemas/*.json | head -30
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000946/versions/0.250829.1249/assets/?page_size=2000" | python -c "
import json,sys,collections as C; d=json.load(sys.stdin); print(d['count'], d['next'])
c=C.Counter(a['path'].split('/')[0] for a in d['results']); print(c)
print([a['path'] for a in d['results'] if 'STTC' in a['path'] or not a['path'].endswith('.nwb')][:10])
"; curl -s https://api.dandiarchive.org/api/dandisets/001199/versions/draft/ | python -c "import json,sys; m=json.load(sys.stdin); print(m['name']); print(m['description'][:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; grep -n -o -i ".\{200\}\(sham\|kPa\|voltage\|2,000 spikes\|normaliz\|Group 1\|N = 16\|pressure\).\{200\}" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 195,245p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l tools/entry.py; grep -n "def \|blocked\|claim:\|sanity\|tag" tools/entry.py | head -80
```

```
473 tools/entry.py
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
70:    def __init__(self):
73:    def error(self, where, message: str) -> None:
78:def dataset_id(record: dict) -> str | None:
83:def schema(name: str) -> Draft202012Validator:
94:def _parsed(text: str):
102:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
108:def load(report: Report, path: Path):
116:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
125:def _plain(value):
136:def code_of(notebook_path: Path) -> str:
143:def check(entry_dir: Path) -> Report:
196:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
197:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
273:            report.error(where, f"claim {claim!r} has no outcome; give every claim one, blocked included")
284:            # A claim on data in another archive names where they are, so it is never blocked for missing data,
288:                if outcome.get("blocked_by") == "data_missing":
292:                if outcome.get("outcome") != "blocked" and not attempt.get("inputs"):
305:            tag = outcome.get("output")
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 143,335p tools/entry.py; sed -n 386,425p tools/entry.py
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

[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; . venv/bin/activate; python -c "
import json,collections as C
r=json.load(open('survey.json'))
for x in r:
  if 'BASE' in x['ident'] or x['ntr']!=500: print(x['ident'],x['ntr'],x['nunits'],x['nspk'],x['tr0'])
# duplicates by (nunits,nspk)
c=C.defaultdict(list)
for x in r: c[(x['nunits'],x['nspk'])].append(x['ident'])
print([v for v in c.values() if len(v)>1])
print(C.Counter(x['ident'].split('_')[-1] if not x['ident'].split('_')[-1].isdigit() or len(x['ident'].split('_'))==5 else x['ident'].split('_')[4] for x in r))
"
```

```
Sat Oct 31 08:09:03 UTC 2026
BH401_1500_400_67_5V 230 34 265314 0.37486592
BH401_300_100_67_5V 230 45 289203 0.23793664
BH401_3000_100_67_5V 230 41 262252 0.2992128
BH401_1500_200_67_5V 230 33 245462 0.32567296
BH401_3000_200_67_5V 230 35 343077 0.30797824
BH401_300_200_67_5V 230 46 280547 0.23199744
BH401_300_400_67_5V 230 43 295181 0.25010176
BH401_1500_100_67_5V 230 33 258616 0.23588864
BH444_300_100_67_55V 230 34 237495 0.30347264
BH444_4500_100_67_55V 230 27 168384 0.25264128
BH444_4500_200_67_55V 230 32 211592 0.28987392
BH444_30_400_67_55V 230 31 204398 0.23867392
BH444_300_200_67_55V 230 34 249900 0.25018368
BH444_3000_100_67_55V 230 20 120571 0.2902016
BH444_1500_100_67_55V 230 32 220578 0.3641344
BH444_1500_200_67_55V 230 47 261691 0.25366528
BH444_3000_200_67_55V 230 15 86115 0.31522816
BH444_30_200_67_55V 230 31 201936 0.25378816
BH444_30_100_67_55V 230 32 229026 0.31096832
[... 60 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000637-gao-2025/tfus.py",
 "content": "\"\"\"Loading and spiking measures for dandiset 000637 (S1 spike times under tFUS).\n\nGao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, doi:10.1523/jneurosci.2218-24.2025.\n\nEach NWB file holds one recording from one rat: a Units table with spike times only (no waveforms, no\nelectrode per unit, electrode locations \"unknown\"), and a trials table with start and stop times only.\nThe stimulation condition is coded in the file's identifier, `<subject>_<PRF Hz>_<PD us>_<UD ms>_<V>`\n(for example BH401_1500_400_67_5V: PRF 1500 Hz, pulse duration 400 us, ultrasound duration 67 ms, 5 V),\nwith a trailing `_2`, `_3` on repeated recordings, and `<subject>_BASELINE` for recordings without a\ncondition. The dandiset's description says so for its sister dandiset 000946 (\"in BH494_1500_200_67_5,\nthe PRF is 1500Hz and PD is 200us\"); for 000637 it is read from the values, and the last field is read\nas the input voltage (the paper's Methods use \"5 V input voltage\"). Files are streamed from the archive\nat the pinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- Units with more than 2,000 spikes in the session (`MIN_SPIKES`): Methods, \"Neuronal type\n  classification and neuronal response quantification\" (\"Only neurons that fire >2,000 spikes for\n  each session were considered\").\n- Windows of 67 ms aligned to the trial start, taken as the tFUS onset (`WINDOWS`): the claims file,\n  Method S, from the Methods (\"normalized to 67 ms before each stimulation\") and the Results' windows.\n  That the trial start is the onset is checked in the notebook (a response contrast), not given by\n  the files.\n- Normalized rate, readings N1 (sum over trials of window counts over sum of pre-stimulus counts) and\n  N2 (mean over trials of the per-trial ratio, trials without a pre-stimulus spike left out): the\n  claims file, Method S.\n- The time shift of the clock check (`SHIFT_S`, 1.2 s, about half the 2.5 s intersonication\n  interval) is a standard choice that cannot change a claim's outcome.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\n\nDANDISET_ID = \"000637\"\nDANDISET_VERSION = \"0.250829.1249\"\n\nMIN_SPIKES = 2000\nWIN_MS = 67.0\nWINDOWS = {\"pre\": (-67.0, 0.0), \"0-67\": (0.0, 67.0), \"67-134\": (67.0, 134.0),\n           \"134-201\": (134.0, 201.0), \"201-268\": (201.0, 268.0)}\nSHIFT_S = 1.2\n\n_IDENT = re.compile(r\"^(BH\\d+)_(\\d+)_(\\d+)_(\\d+)_(\\d+)V?(?:_(\\d+))?$\")\n\n\ndef parse_identifier(ident: str) -> dict:\n    \"\"\"Condition fields coded in a file's identifier.\"\"\"\n    if ident.endswith(\"_BASELINE\"):\n        return dict(subject=ident.split(\"_\")[0], prf=np.nan, pd_us=np.nan, ud_ms=np.nan,\n                    volt=np.nan, repeat=1, baseline=True)\n    m = _IDENT.match(ident)\n    if m is None:\n        raise ValueError(f\"unparsed identifier {ident!r}\")\n    subj, prf, pd_us, ud, volt, rep = m.groups()\n    # \"55\" and \"35\" are 5.5 V and 3.5 V; \"5\" and \"7\" are whole volts.\n    v = float(volt) / 10 if len(volt) == 2 else float(volt)\n    return dict(subject=subj, prf=int(prf), pd_us=int(pd_us), ud_ms=int(ud), volt=v,\n                repeat=int(rep) if rep else 1, baseline=False)\n\n\ndef asset_urls() -> list[tuple[str, str]]:\n    \"\"\"(path, streaming URL) of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n                      for a in ds.get_assets() if a.path.endswith(\".nwb\"))\n\n\ndef _str(x) -> str:\n    x = x[()] if hasattr(x, \"shape\") else x\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef load_session(path: str, url: str) -> dict:\n    \"\"\"One recording: metadata, trial starts and stops, and spike times per unit (seconds).\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        ident = _str(f[\"identifier\"])\n        st = f[\"units/spike_times\"][:]\n        idx = f[\"units/spike_times_index\"][:]\n        starts = f[\"intervals/trials/start_time\"][:]\n        stops = f[\"intervals/trials/stop_time\"][:]\n        loc = sorted({_str(x) for x in f[\"general/extracellular_ephys/electrodes/location\"][:]})\n        meta = dict(path=path, identifier=ident,\n                    subject_id=_str(f[\"general/subject/subject_id\"]),\n                    description=_str(f[\"session_description\"]),\n                    start_time=_str(f[\"session_start_time\"]),\n                    unit_columns=list(f[\"units\"].attrs[\"colnames\"]),\n                    trial_columns=list(f[\"intervals/trials\"].attrs[\"colnames\"]),\n                    electrode_locations=loc,\n                    n_electrodes=len(f[\"general/extracellular_ephys/electrodes/id\"]),\n                    device=[_str(f[\"general/devices\"][k].attrs.get(\"description\", \"\"))\n                            for k in f[\"general/devices\"]],\n                    acquisition=list(f[\"acquisition\"]), processing=list(f[\"processing\"]))\n    units = np.split(st, idx[:-1].astype(int))\n    meta.update(parse_identifier(ident))\n    meta.update(trial_start=starts, trial_stop=stops, units=units)\n    return meta\n\n\ndef load_all(workers: int = 16) -> list[dict]:\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(lambda pu: load_session(*pu), asset_urls()))\n\n\ndef window_counts(spikes: np.ndarray, onsets: np.ndarray) -> np.ndarray:\n    \"\"\"Spike counts per trial (rows) in each window of `WINDOWS` (columns), windows in ms from onset.\"\"\"\n    out = np.empty((len(onsets), len(WINDOWS)), dtype=np.int64)\n    for j, (a, b) in enumerate(WINDOWS.values()):\n        lo = np.searchsorted(spikes, onsets + a / 1000.0, side=\"left\")\n        hi = np.searchsorted(spikes, onsets + b / 1000.0, side=\"left\")\n        out[:, j] = hi - lo\n    return out\n\n\ndef unit_table(sessions: list[dict], shift_s: float = 0.0) -> pd.DataFrame:\n    \"\"\"One row per unit with more than `MIN_SPIKES` spikes: session fields, and for each window the\n    summed count, the normalized rate N1 and N2 (percent of the pre-stimulus window), and the rate in\n    Hz. With `shift_s`, the onsets are moved by that many seconds (the clock check).\"\"\"\n    rows = []\n    names = list(WINDOWS)\n    for s in sessions:\n        onsets = s[\"trial_start\"] + shift_s\n        for u, sp in enumerate(s[\"units\"]):\n            if len(sp) <= MIN_SPIKES:\n                continue\n            c = window_counts(sp, onsets)\n            row = dict(identifier=s[\"identifier\"], subject=s[\"subject\"], prf=s[\"prf\"], pd_us=s[\"pd_us\"],\n                       volt=s[\"volt\"], baseline=s[\"baseline\"], unit=u, n_spikes=len(sp), n_trials=len(onsets))\n            pre = c[:, 0]\n            for j, w in enumerate(names):\n                row[f\"count_{w}\"] = int(c[:, j].sum())\n                row[f\"rate_{w}\"] = c[:, j].sum() / (len(onsets) * WIN_MS / 1000.0)\n                if j == 0:\n                    continue\n                row[f\"n1_{w}\"] = 100.0 * c[:, j].sum() / pre.sum() if pre.sum() > 0 else np.nan\n                ok = pre > 0\n                row[f\"n2_{w}\"] = 100.0 * np.mean(c[ok, j] / pre[ok]) if ok.any() else np.nan\n            rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef duty_cycle(prf, pd_us):\n    \"\"\"Duty cycle in percent: PRF times pulse duration (Figure 1B legend, \"PDs were calculated by\n    PRFs*DCs\").\"\"\"\n    return np.asarray(prf, dtype=float) * np.asarray(pd_us, dtype=float) * 1e-4\n"
}
```

```
File created successfully at: entries/000637-gao-2025/tfus.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000637-gao-2025; . $TMPDIR/venv/bin/activate; cat > $TMPDIR/t1.py <<'EOF'
import time, numpy as np, tfus
t=time.time(); urls=tfus.asset_urls(); print(len(urls), time.time()-t)
sub=[u for u in urls if 'BH462' in u[0]]
t=time.time(); S=[tfus.load_session(*u) for u in sub]; print('load',time.time()-t)
for s in S: print(s['identifier'], len(s['units']), all(np.all(np.diff(x)>=0) for x in s['units']), s['trial_start'][:3], np.diff(s['trial_start']).min(), np.diff(s['trial_start']).max(), max(x[-1] for x in s['units']), s['trial_stop'][-1])
T=tfus.unit_table(S); Ts=tfus.unit_table(S, shift_s=tfus.SHIFT_S)
print(T.groupby('identifier')[['n1_0-67','n1_67-134','n1_201-268']].mean().round(1))
print(Ts.groupby('identifier')[['n1_0-67','n1_67-134','n1_201-268']].mean().round(1))
EOF
python $TMPDIR/t1.py 2>&1 | grep -v Warn
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/t1.py", line 1, in <module>
    import time, numpy as np, tfus
ModuleNotFoundError: No module named 'tfus'
```

**Agent calls Bash**

```bash
cd entries/000637-gao-2025; . $TMPDIR/venv/bin/activate; PYTHONPATH=. python $TMPDIR/t1.py 2>&1 | grep -v Warn
```

```
292 40.92398262023926
load 14.878473281860352
BH462_3000_100_67_5 65 True [0.32526336 3.053568   5.42621696] 2.2500147199999674 2.7486617600000045 1258.11974144 1256.1226112
BH462_300_200_67_5 31 True [0.2545664  2.90193408 5.4329344 ] 2.25214464000004 2.748211199999787 1247.71446784 1246.3846169600001
BH462_30_400_67_5 60 True [0.35917824 2.9200384  5.49023744] 2.250342399999999 2.749276160000022 1330.09235968 1252.18967296
BH462_1500_200_67_5 35 True [0.33099776 3.03542272 5.61750016] 2.2506700799999635 2.7488665600000033 1255.85293312 1250.3982464
BH462_4500_100_67_5 65 True [0.39624704 2.75402752 5.0733056 ] 2.2516940799998792 2.7499315200000183 1317.08284928 1249.16928256
BH462_4500_200_67_5 35 True [0.34701312 2.97562112 5.57039616] 2.2505471999999997 2.7497267199998987 1254.4290816 1251.8994304
BH462_1500_400_67_5 64 True [0.321536   2.89665024 5.26614528] 2.2507929600000125 2.7494809599999996 1249.64089856 1248.8610176
BH462_3000_200_67_5 62 True [0.24776704 2.57949696 5.13359872] 2.2515712000000008 2.746900480000022 1254.68020736 1250.4961408000001
BH462_30_100_67_5 65 True [0.34680832 2.99008    5.63920896] 2.252267520000032 2.749439999999993 1262.56541696 1261.09220608
BH462_300_100_67_5 64 True [0.33091584 2.6159104  5.1781632 ] 2.2501785600001085 2.7480064000000084 1279.92344576 1250.83148032
BH462_1500_100_67_5 65 True [0.37769216 3.05577984 5.4032384 ] 2.2503424 2.749358079999979 1255.85096704 1254.48425216
BH462_30_200_67_5 44 True [0.3350528  2.65596928 5.32180992] 2.251161599999932 2.7496038400000202 1255.6032 1251.51956736
BH462_300_400_67_5 59 True [0.331776   2.755584   5.03222272] 2.2500556800000027 2.749153279999973 1253.7536512 1252.2486144
                     n1_0-67  n1_67-134  n1_201-268
identifier                                         
BH462_1500_100_67_5    107.2      105.7       212.9
BH462_1500_200_67_5    174.8      101.6       161.3
BH462_1500_400_67_5    152.2      145.6       529.8
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  grep -n -i "Figure 4\.\|Figure 6\.\|^Figure" paper/*.txt | head; sed -n 246,250p paper/*.txt | cut -c1-1500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/b; cat > $TMPDIR/b/build.py <<'PYEOF'
import nbformat as nbf, sys
cells = []
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip()); 
    if tags: c.metadata["tags"] = tags
    cells.append(c)
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip())
    if tags: c.metadata["tags"] = tags
    cells.append(c)

md(r"""
# Gao, Ramachandran, Yu & He (2025) on dandiset 000637

**Paper.** Gao H, Ramachandran S, Yu K, He B (2025). Transcranial focused ultrasound modulates feedforward
and feedback cortico-thalamo-cortical pathways by selectively activating excitatory neurons.
*J Neurosci* 45(23):e2218242025, doi:10.1523/jneurosci.2218-24.2025.

**Dataset.** DANDI:000637, version 0.250829.1249 (doi:10.48324/dandi.000637/0.250829.1249), streamed.
The paper cites no version of 000637 (its data statement names a different dandiset, 000946), so the
most recent published version is pinned. The five published versions (0.250711.1756 to 0.250829.1249)
are compared below: they hold the same files with the same digests, so the choice does not change the
data.

**Claims file.** `claims/000637/10.1523-jneurosci.2218-24.2025.yaml`, written from the version of record
(PMC12139594), which has no supplement and links no code.

**What the dataset holds.** 292 recordings from 25 rats, each with spike times of sorted units from one
32-channel probe in S1 and the trial start and stop times. The condition is coded only in the file's
identifier. There are no spike waveforms, no POm, auditory cortex or CG1-targeted recordings, and of the
duty-cycle series only the conditions that share pulse durations with the PRF series.

Every claim of the paper is about units classified as RSUs or FSUs, and the paper classifies them from
waveform shape (Methods, "Neuronal type classification"). Without waveforms none of the claims can be
tested as the claims file states them, and most also need POm or AC units or conditions that are not
here. All 27 claims are blocked. The notebook shows what the dataset does hold: the conditions, the
checks of the metadata against the data, the trial clock, the counts of units under the paper's 2,000
spike rule, and, as variants that decide no claim, the responses of all S1 units pooled across cell types.

| Claim | Outcome | Main reason |
|---|---|---|
| unit-counts | blocked | data_missing: no waveforms for RSU/FSU classification; no POm units |
| fig4-s1-rsu-timelocked-3000, fig4-post-3000, fig4-30hz-s1-rsu-inhibition | blocked | data_missing: no cell types (and no POm for fig4-post-3000) |
| fig4-pom-rsu-timelocked-3000, fig4-30hz-pom-rsu-delayed, fig4-fsu-no-change | blocked | data_missing: no POm units, no cell types |
| fig5-sham-no-response | blocked | data_missing: no cell types, no POm; three unlabelled BASELINE recordings |
| fig5-cg1-control-no-response | blocked | data_missing: no CG1-targeted recordings |
| fig6a-s1-rsu-timelocked-high-prf, fig6a-s1-rsu-delayed, fig6b-s1-fsu | blocked | data_missing: no cell types |
| fig6c-pom-rsu-timelocked, fig6c-pom-rsu-delayed, fig6d-pom-fsu | blocked | data_missing: no POm units |
| fig7a to fig7d, fig8a, fig8b, fig9a, fig9b | blocked | data_missing: no cell types; most duty cycles absent; no POm for 7c and 7d |
| fig10a to fig10ef (dSTTC and STTC) | blocked | data_missing: no POm units |
| fig11b, fig11c, fig11d | blocked | data_missing: no auditory cortex units |
""")

code(r"""
import numpy as np, pandas as pd, requests, time
from scipy import stats
import matplotlib.pyplot as plt
import tfus
pd.set_option("display.width", 200); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 200)
print(tfus.DANDISET_ID, tfus.DANDISET_VERSION)
""")

md("## Versions\nThe asset lists of the published versions, with each file's SHA-256 digest.")
code(r"""
API = "https://api.dandiarchive.org/api/dandisets/000637/versions/"
versions = [v["version"] for v in requests.get(API, timeout=60).json()["results"] if v["version"] != "draft"]
def asset_list(v):
    out, url = {}, f"{API}{v}/assets/?page_size=1000&metadata=1"
    while url:
        r = requests.get(url, timeout=120).json()
        for a in r["results"]:
            out[a["path"]] = (a["metadata"].get("digest") or {}).get("dandi:sha2-256")
        url = r["next"]
    return out
lists = {v: asset_list(v) for v in versions}
ref = lists[tfus.DANDISET_VERSION]
for v, l in lists.items():
    print(v, len(l), "files;", "identical paths and digests to the pinned version" if l == ref else
          f"differs: {len(set(l.items()) ^ set(ref.items()))} path/digest pairs")
""")

md("## Loading\nAll 292 files are streamed; spike times and trial times are read into memory.")
code(r"""
t0 = time.time()
sessions = tfus.load_all()
print(f"{len(sessions)} recordings loaded in {time.time() - t0:.0f} s")
meta = pd.DataFrame([{k: v for k, v in s.items() if k not in ("trial_start", "trial_stop", "units")} |
                     dict(n_units=len(s["units"]), n_trials=len(s["trial_start"]),
                          n_units_2000=sum(len(u) > tfus.MIN_SPIKES for u in s["units"]))
                     for s in sessions])
meta["dc_pct"] = tfus.duty_cycle(meta.prf, meta.pd_us)
""")

md("## Data check")
code(r"""
print("Files per subject:"); print(meta.groupby("subject").size().to_string())
print("\nsubject_id field equals the identifier's subject:", bool((meta.subject_id == meta.subject).all()))
print("\nDistinct values across files:")
for col in ["description", "unit_columns", "trial_columns", "electrode_locations", "n_electrodes", "device", "acquisition", "processing"]:
    print(f"  {col}: {meta[col].astype(str).value_counts().to_dict()}")
print("\nRecordings by PRF (Hz) and pulse duration (us), stimulated recordings:")
print(pd.crosstab(meta.prf, meta.pd_us).to_string())
print("\nRecordings by input voltage:", meta.volt.value_counts(dropna=False).to_dict())
print("Ultrasound duration (ms):", meta.ud_ms.value_counts(dropna=False).to_dict())
print("Baseline recordings (no condition in the identifier):", meta.loc[meta.baseline, "identifier"].tolist())
print("Repeated recordings (_2, _3, _4):", meta.loc[meta.repeat > 1, "identifier"].tolist())
print("\nDuty cycles (PRF x PD) present:", sorted(meta.dc_pct.dropna().round(2).unique().tolist()))
print("\nTrials per recording:", meta.n_trials.value_counts().to_dict())
print("Units per recording: min", meta.n_units.min(), "median", meta.n_units.median(), "max", meta.n_units.max(),
      "; total", meta.n_units.sum(), "; with more than 2,000 spikes", meta.n_units_2000.sum())

iti = np.concatenate([np.diff(s["trial_start"]) for s in sessions])
dur = np.concatenate([s["trial_stop"] - s["trial_start"] for s in sessions])
print(f"\nIntertrial interval (s): min {iti.min():.3f}, 1st pct {np.percentile(iti, 1):.3f}, median {np.median(iti):.3f}, "
      f"99th pct {np.percentile(iti, 99):.3f}, max {iti.max():.3f}  (paper: 2.5 s with 10% jitter, 2.25 to 2.75 s)")
print(f"Trial duration stop - start (s): {np.unique(dur.round(4))}")
srt = all(np.all(np.diff(u) >= 0) for s in sessions for u in s["units"])
print("Spike times sorted in every unit:", srt)
allsp = np.concatenate([u for s in sessions for u in s["units"]])
print(f"Spike times (s): min {allsp.min():.4f}, max {allsp.max():.1f}")
last_trial = np.array([s["trial_stop"][-1] for s in sessions]); last_spike = np.array([max(u[-1] for u in s["units"] if len(u)) for s in sessions])
print(f"Last spike minus last trial stop (s): median {np.median(last_spike - last_trial):.1f}, max {np.max(last_spike - last_trial):.1f}")
print("Session start times:", meta.start_time.str[:10].value_counts().to_dict())
""", tags=["sanity"])

md(r"""
Checks of the description against the data, from the output above:

- The description says "Each recording has 500 trials"; the counts per file are printed above, and
  those with fewer than 500 are a metadata error.
- The description calls 100, 200 and 400 us "ultrasound durations (UDs)" and says "The pulse duration
  was kept at 67ms". The paper uses the opposite terms (UD 67 ms; PD 200 us in the PRF series). The
  identifiers carry 67 in the ultrasound-duration place for every stimulated recording, consistent
  with the paper's terms; the description has them swapped. One recording uses 600 us, which the
  description does not list.
- The last field of the identifier is read as the input voltage (5 V in the paper's Methods); recordings
  at 3.5, 5.5 and 7 V are present and are not described.
- The units carry no electrode, waveform or quality column, and all electrode locations are "unknown":
  the units cannot be assigned to S1 layers, to channels, or to cell types.
- The intertrial intervals are within the paper's 2.25 to 2.75 s, consistent with trial start being the
  tFUS onset, which the next check tests.
""")

md(r"""
## Trial clock

The files do not say that a trial's start is the tFUS onset. For each unit with more than 2,000 spikes in
a stimulated recording at 1500, 3000 or 4500 Hz (where the paper reports responses), the spike counts in
the 67 ms windows after the trial start are compared with the 67 ms before it, at the true trial starts
and at starts shifted by 1.2 s (half an intersonication interval). A response that appears at the true
starts and not at the shifted ones shows the trials and spikes share a clock and that the start is
the onset to within the window.
""")
code(r"""
units = tfus.unit_table(sessions)
shifted = tfus.unit_table(sessions, shift_s=tfus.SHIFT_S)
hi = units.prf.isin([1500, 3000, 4500]) & ~units.baseline
hs = shifted.prf.isin([1500, 3000, 4500]) & ~shifted.baseline
rows = []
for name, tab, m in [("true onsets", units, hi), ("shifted 1.2 s", shifted, hs)]:
    for w in ["0-67", "67-134", "134-201", "201-268"]:
        r = stats.wilcoxon(tab.loc[m, f"count_{w}"], tab.loc[m, "count_pre"])
        rows.append(dict(onsets=name, window=w, n_units=int(m.sum()),
                         median_N1=tab.loc[m, f"n1_{w}"].median(),
                         frac_units_up=np.mean(tab.loc[m, f"count_{w}"] > tab.loc[m, "count_pre"]),
                         signed_rank_p=r.pvalue))
clock = pd.DataFrame(rows); print(clock.round(4).to_string(index=False))
# Per subject: median N1 at 201-268 ms with true and shifted onsets
per = pd.DataFrame({"true": units[hi].groupby("subject")["n1_201-268"].median(),
                    "shifted": shifted[hs].groupby("subject")["n1_201-268"].median()})
print("\nPer subject, median N1 at 201-268 ms (%), PRF 1500-4500 Hz:"); print(per.round(1).T.to_string())
print("Subjects with true > shifted:", int((per["true"] > per["shifted"]).sum()), "of", len(per))
""")

md(r"""
## Recordings deposited more than once

Each unit is fingerprinted by its spike count and its first 20 spike times (to 0.1 ms). A fingerprint
shared by units in two files, or two units of one file, would be a recording deposited twice.
""")
code(r"""
fp = {}
for s in sessions:
    for i, u in enumerate(s["units"]):
        fp.setdefault((len(u), tuple(np.round(u[:20], 4))), []).append((s["identifier"], i))
shared = [v for v in fp.values() if len(v) > 1]
print("Units:", sum(len(v) for v in fp.values()), "; fingerprints shared by more than one unit:", len(shared))
for v in shared[:10]: print("  ", v)
# Recordings with the same condition in the same rat (_2, _3): correlation of their per-unit spike counts
for subj, g in meta[meta.repeat > 1].groupby("subject"):
    print(subj, "repeats:", g.identifier.tolist(), "units", g.n_units.tolist())
""")

md(r"""
## What the claims need, and what is here

The claims test cell-typed units (RSU, FSU) in S1 and POm, and for Figure 11 in auditory cortex, under
the paper's conditions. The table lists each condition set the claims use, with the pulse durations
that give it (PD = DC / PRF, Figure 1B legend), and how many recordings of each the dataset has.
""")
code(r"""
needed = {
    "PRF series, 200 us (Fig 4, 6, 10C)": [(p, 200) for p in (30, 300, 1500, 3000, 4500)],
    "3000 Hz DC series 0.6-90% (Fig 7, 10F)": [(3000, d) for d in (2, 20, 100, 200, 300)],
    "30 Hz DC series 0.6-90% (Fig 8, 10E)": [(30, d) for d in (200, 2000, 10000, 20000, 30000)],
    "60% DC PRF series (Fig 9, 10D)": [(30, 20000), (300, 2000), (1500, 400), (3000, 200), (4500, 133)],
}
stim = meta[~meta.baseline]
rows = []
for name, conds in needed.items():
    for prf, pd_us in conds:
        n = int(((stim.prf == prf) & (stim.pd_us == pd_us)).sum())
        rows.append(dict(series=name, prf=prf, pd_us=pd_us, dc_pct=round(prf * pd_us * 1e-4, 2), recordings=n))
print(pd.DataFrame(rows).to_string(index=False))
print("\nSham (no tFUS): no recording is labelled sham; recordings named BASELINE:", int(meta.baseline.sum()))
print("CG1-targeted control: no identifier or field names a target; S1 is the only target described.")
print("Brain areas: one probe per file, electrode locations", meta.electrode_locations.astype(str).unique().tolist(),
      "; the description names only S1. No POm or auditory cortex units.")
print("Waveforms or waveform features in the Units table:", any(c != ["spike_times"] for c in meta.unit_columns))
""")

md(r"""
## unit-counts (blocked): counts under the 2,000 spike rule

> The analyses of PRF at constant 200 us pulse duration rest on 1,050 S1 RSUs, 247 S1 FSUs, 913 POm RSUs and
> 106 POm FSUs, and the 3000 Hz and 30 Hz sessions of Figure 4 on 312 and 148 S1 RSUs, 54 and 61 S1 FSUs,
> 233 and 189 POm RSUs, and 17 and 43 POm FSUs.

The RSU/FSU split needs waveforms, which the dataset lacks, and the POm counts need POm units. As a
variant that does not decide the claim, the S1 units with more than 2,000 spikes are counted per
condition, all cell types together, and compared with the paper's S1 RSU + FSU sums. The counts are
given for all input voltages and for 5 V alone (the paper's stated input voltage).
""")
code(r"""
s1 = units[~units.baseline]
def count(df, prf=None, pd_us=200):
    m = (df.pd_us == pd_us) & (df.prf.isin(prf) if prf is not None else True)
    return int(m.sum())
paper = {"PRF series, all PRFs": 1050 + 247, "3000 Hz 200 us": 312 + 54, "30 Hz 200 us": 148 + 61}
rows = []
for label, prfs in [("PRF series, all PRFs", None), ("3000 Hz 200 us", [3000]), ("30 Hz 200 us", [30])]:
    rows.append(dict(set=label, paper_S1_RSU_plus_FSU=paper[label],
                     dataset_all_volts=count(s1, prfs), dataset_5V=count(s1[s1.volt == 5], prfs)))
print(pd.DataFrame(rows).to_string(index=False))
print("\nS1 units with >2,000 spikes per PRF at 200 us (all voltages):", s1[s1.pd_us == 200].groupby("prf").size().to_dict())
print("Paper's S1 RSUs per PRF at 200 us (Results, Fig 6A): 1500 Hz 284, 3000 Hz 312, 4500 Hz 152; S1 FSUs at 60% DC 1500 Hz 48 (Fig 9B)")
print("Units dropped by the 2,000 spike rule:", int(meta.n_units.sum() - meta.n_units_2000.sum()), "of", int(meta.n_units.sum()))
""", tags=["claim:unit-counts"])

md(r"""
## Variant: all S1 units pooled, PRF series at 200 us

This decides no claim: the claims are about RSUs and FSUs separately, and the paper's RSUs and FSUs
respond differently. It shows whether the S1 recordings in this dataset carry the time-locked and
delayed responses that the paper reports for S1 units. Normalized rates N1 and N2 are those of the claims
file's Method S; the tests are Wilcoxon signed-rank (W2) and rank-sum (W1) of the raw rates in each
window against the pre-stimulus window, one-tailed for an increase and for a decrease, Bonferroni over
the four windows (M1). Units are counted once per recording.
""")
code(r"""
def window_tests(df, label):
    rows = []
    for w in ["0-67", "67-134", "134-201", "201-268"]:
        x, b = df[f"rate_{w}"], df["rate_pre"]
        r = dict(set=label, window=w, n=len(df), mean_N1=df[f"n1_{w}"].mean(), sem_N1=df[f"n1_{w}"].sem(),
                 mean_N2=df[f"n2_{w}"].mean())
        for tail, alt in [("up", "greater"), ("down", "less")]:
            r[f"W2_{tail}_p"] = min(1.0, 4 * stats.wilcoxon(x, b, alternative=alt).pvalue)
            r[f"W1_{tail}_p"] = min(1.0, 4 * stats.mannwhitneyu(x, b, alternative=alt).pvalue)
        rows.append(r)
    return rows
prf_rows = []
for prf in (30, 300, 1500, 3000, 4500):
    prf_rows += window_tests(s1[(s1.pd_us == 200) & (s1.prf == prf)], f"{prf} Hz")
prf_tab = pd.DataFrame(prf_rows)
with pd.option_context("display.float_format", "{:.3g}".format):
    print(prf_tab.to_string(index=False))
for w in ["0-67", "201-268"]:
    groups = [s1.loc[(s1.pd_us == 200) & (s1.prf == p), f"n1_{w}"].dropna() for p in (30, 300, 1500, 3000, 4500)]
    print(f"Kruskal-Wallis across PRFs, N1 {w}: H = {stats.kruskal(*groups).statistic:.1f}, p = {stats.kruskal(*groups).pvalue:.3g}")
print("Units with no pre-stimulus spike (N1 undefined):", int(s1['n1_0-67'].isna().sum()))
print("Range of N1 at 201-268 ms (%):", round(s1['n1_201-268'].min(), 1), "to", round(s1['n1_201-268'].max(), 1))
""", tags=["variant:pooled-s1-prf"])
code(r"""
# By animal: median N1 per PRF at 0-67 and 201-268 ms (S1 units, 200 us)
d = s1[s1.pd_us == 200]
for w in ["0-67", "201-268"]:
    t = d.pivot_table(index="subject", columns="prf", values=f"n1_{w}", aggfunc="median")
    print(f"Median N1 {w} ms (%), by subject and PRF:"); print(t.round(0).to_string())
    print("Subjects with median above 100% at each PRF:", (t > 100).sum().to_dict(), "of", t.notna().sum().to_dict(), "\n")
fig, ax = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
for a, w in zip(ax, ["0-67", "201-268"]):
    sub = prf_tab[prf_tab.window == w]
    a.errorbar(range(5), sub.mean_N1, yerr=sub.sem_N1, fmt="o-", color="k")
    a.axhline(100, color="grey", lw=0.8); a.set_xticks(range(5)); a.set_xticklabels(sub.set)
    a.set_title(f"All S1 units, {w} ms, PD 200 us"); a.set_ylabel("mean N1 (%) +/- SEM")
plt.tight_layout(); plt.show()
print("Plotted means (%):", prf_tab[prf_tab.window.isin(['0-67', '201-268'])].mean_N1.round(1).tolist())
""", tags=["variant:pooled-s1-prf"])

md(r"""
## Variant: BASELINE recordings

Three recordings are named BASELINE, with 500 trials each. Nothing in the files says whether they are the
paper's sham sessions (no tFUS) or how their trial times were made. The same measures are shown for them,
all units pooled; this decides no claim.
""")
code(r"""
b = units[units.baseline]
print("Units with >2,000 spikes in BASELINE recordings, by recording:", b.groupby("identifier").size().to_dict())
with pd.option_context("display.float_format", "{:.3g}".format):
    print(pd.DataFrame(window_tests(b, "BASELINE")).to_string(index=False))
""", tags=["variant:baseline"])

md(r"""
## Summary

| Claim | Outcome |
|---|---|
| all 27 claims | blocked, data_missing |

Every claim is about RSUs and FSUs, which the paper separates by waveform shape; the dataset holds spike
times only. Most claims also need POm or auditory cortex units, CG1-targeted or sham recordings, or duty
cycles that are not in the dataset (the condition table above). The paper's own data statement names a
different dandiset, 000946, whose subjects (BH494 to BH535) are not those of 000637 (BH401 to BH477).
No recording of this dataset could be linked to a recording the paper analysed.

What was found about the dataset:

- The units have no waveforms, electrodes or quality metrics, and all electrode locations are "unknown".
- Trials per recording differ from the 500 the description states (counts in the data check).
- The description swaps pulse duration and ultrasound duration, and does not list the 600 us recording or
  the 3.5, 5.5 and 7 V recordings; conditions are coded only in the identifier.
- Three recordings named BASELINE are not described.
- Trial starts share a clock with the spikes and behave as tFUS onsets (trial clock section).
- No unit was found deposited twice.

How the analysis differs from the paper's: no claim was tested. The pooled-unit variants mix RSUs and
FSUs, which the paper does not do, and are shown only to describe the data.
""")

nb = nbf.v4.new_notebook(); nb.cells = cells
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, sys.argv[1])
PYEOF
. $TMPDIR/venv/bin/activate; python $TMPDIR/b/build.py entries/000637-gao-2025/reproduce_gao_2025.ipynb && echo ok
```

```
ok
```

**Agent**

Notebook drafted. Running it once in my dev environment to see the numbers (load is about 2 min).

**Agent calls Bash**

```bash
cd entries/000637-gao-2025; . $TMPDIR/venv/bin/activate; time jupyter nbconvert --to notebook --execute reproduce_gao_2025.ipynb --output-dir $TMPDIR/run --ExecutePreprocessor.timeout=1800 2>&1 | tail -3; python - <<'EOF'
import nbformat, os
nb=nbformat.read(os.environ['TMPDIR']+'/run/reproduce_gao_2025.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.outputs:
            if 'text' in o: print(o['text'][:6000])
            elif o.get('output_type')=='error': print(o['ename'],o['evalue'])
        print('-----')
EOF
```

```
[NbConvertApp] Converting notebook reproduce_gao_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 97321 bytes to /tmp/claude-1001/run/reproduce_gao_2025.ipynb

real	5m27.174s
user	0m29.011s
sys	0m3.660s
000637 0.250829.1249

-----
0.250711.1756 292 files; identical paths and digests to the pinned version
0.250711.1944 292 files; identical paths and digests to the pinned version
0.250828.1935 292 files; identical paths and digests to the pinned version
0.250829.1249 292 files; identical paths and digests to the pinned version

-----
292 recordings loaded in 308 s

-----
Files per subject:
[... 229 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/b; python - <<'EOF'
p='build.py'; s=open(p).read()
s=s.replace('clock = pd.DataFrame(rows); print(clock.round(4).to_string(index=False))',
 'clock = pd.DataFrame(rows)\nwith pd.option_context("display.float_format", "{:.3g}".format):\n    print(clock.to_string(index=False))')
s=s.replace("""print("Units dropped by the 2,000 spike rule:\"""","""print(f"Ratio of dataset to paper, PRF series all voltages: {rows[0]['dataset_all_volts'] / rows[0]['paper_S1_RSU_plus_FSU']:.2f}")
print("Units dropped by the 2,000 spike rule:\"""")
s=s.replace("""No recording of this dataset could be linked to a recording the paper analysed.""","""No recording of this dataset could be linked to a recording the paper analysed, and the dataset has
about 3.6 times as many S1 units over 2,000 spikes in the PRF series at 200 us as the paper's S1 RSUs and
FSUs together (4,642 against 1,297; unit-counts section), so these are not, or not only, the units the
paper analysed.""")
s=s.replace("""- Trial starts share a clock with the spikes and behave as tFUS onsets (trial clock section).""","""- Trial starts share a clock with the spikes and behave as tFUS onsets: at 1500 to 4500 Hz, 74% of units
  fire more in 0 to 67 ms than in the 67 ms before, against 43% with onsets shifted by 1.2 s, and the
  delayed response is larger at the true onsets in 23 of 25 rats (trial clock section).
- Pooling all S1 units (a variant, not a claim), every PRF at 200 us raises the 0 to 67 ms rate over
  baseline under W2, and 300 to 4500 Hz raise the 201 to 268 ms rate; 30 Hz does not raise it.
- The three BASELINE recordings show an increase over the pre-trial window at 134 to 268 ms under W2
  (corrected p 6e-09 and 1.2e-05) and not under W1; they behave unlike a clean sham, which is another
  reason not to use them as one without a description.""")
open(p,'w').write(s)
EOF
cd  . $TMPDIR/venv/bin/activate; python $TMPDIR/b/build.py entries/000637-gao-2025/reproduce_gao_2025.ipynb; grep -c "Ratio of dataset" entries/000637-gao-2025/reproduce_gao_2025.ipynb; date -u
```

```
1
Sat Oct 31 08:18:14 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=0)[:6000])"; sed -n 80,200p attempts/001453-fouke-2025-01.yaml | grep -n "findings\|kind:\|verifications\|blocked_by" | head
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
[... 259 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['findings'],indent=0)[:3000]); print(list(s['properties']))"; grep -n "^findings" -A 12 attempts/001453-fouke-2025-01.yaml | head -20
```

```
{
"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.",
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"statement"
],
"properties": {
"kind": {
"enum": [
"metadata_error",
"data_missing",
"identifier_missing",
"metadata_insufficient",
"selection_undocumented",
"methods_unavailable",
"format_error",
[... 32 more lines not kept]
```

**Agent**

Now the entry files.

**Agent calls Bash**

```bash
cd entries/000637-gao-2025; cat > entry.yaml <<'EOF'
schema_version: 1
name: 000637-gao-2025
type: reproduction
title: Transcranial focused ultrasound and S1 spiking (Gao et al. 2025) on dandiset 000637
description: Tests the findings of Gao, Ramachandran, Yu and He (2025) on dandiset 000637, which holds
  spike times of sorted S1 units from 25 rats under tFUS at five PRFs and several pulse durations. Every
  claim is about units typed as RSU or FSU from their waveforms, which the dandiset lacks, and most also
  need POm or auditory cortex units, so all claims are blocked. The notebook checks the metadata against
  the data, the trial clock and the unit counts, and shows the responses of all S1 units pooled.
license: Apache-2.0
notebooks:
- path: reproduce_gao_2025.ipynb
  title: Gao et al. (2025) on dandiset 000637
  runtime_minutes: 6
helpers:
- tfus.py
related:
- id: dandi:000637/0.250829.1249
  relation: uses_data
- id: doi:10.1523/jneurosci.2218-24.2025
  relation: reproduces
EOF
printf 'dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\n' > requirements.in
cat > README.md <<'EOF'
# Gao, Ramachandran, Yu & He (2025) on dandiset 000637

Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) on
[DANDI:000637](https://dandiarchive.org/dandiset/000637/0.250829.1249), which holds spike times of
sorted units from one 32-channel probe in S1 of 25 rats, under tFUS at PRFs of 30 to 4500 Hz and pulse
durations of 100 to 600 us, with trial start and stop times.

| Claims | Outcome |
|---|---|
| All 27 claims (unit counts, Figures 4 to 11) | Blocked: data missing |

Every claim is about units classified as RSUs or FSUs from their waveforms, and the dandiset has spike
times only. Most claims also need POm or auditory cortex units, sham or CG1-targeted recordings, or duty
cycles that are not in it. The paper's data statement names another dandiset, 000946, whose rats are not
those of 000637, and 000637 has about 3.6 times as many S1 units over the paper's 2,000 spike threshold
as the paper reports for S1, so its recordings could not be linked to those the paper analysed.

The notebook checks the description against the data (trial counts, the condition codes in the file
identifiers, the trial clock, units deposited twice), counts units under the paper's spike threshold,
and shows the responses of all S1 units pooled across cell types, as a description of the data that
decides no claim. The attempt record is
[`attempts/000637-gao-2025-01.yaml`](../../attempts/000637-gao-2025-01.yaml).

- `reproduce_gao_2025.ipynb`: the analysis, about six minutes, most of it streaming the 292 files.
- `tfus.py`: loading, the condition codes in the identifiers, and the window counts and normalized
  rates of the claims file's Method S. Other notebooks on this dandiset can import it.
EOF
cd  . $TMPDIR/venv/bin/activate 2>/dev/null; deactivate 2>/dev/null; python tools/entry.py lock entries/000637-gao-2025 2>&1 | tail -3; ls entries/000637-gao-2025
```

```
wrote entries/000637-gao-2025/requirements.lock.txt
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
cd  rm -rf entries/000637-gao-2025/__pycache__; python -c "
import yaml; d=yaml.safe_load(open('claims/000637/10.1523-jneurosci.2218-24.2025.yaml'))
for c in d['claims']: print(c['id'], c.get('data','dataset'), c.get('depends_on'))"
```

```
unit-counts dataset None
fig4-s1-rsu-timelocked-3000 dataset ['unit-counts']
fig4-pom-rsu-timelocked-3000 dataset ['unit-counts']
fig4-post-3000 dataset ['unit-counts']
fig4-30hz-s1-rsu-inhibition dataset ['unit-counts']
fig4-30hz-pom-rsu-delayed dataset ['unit-counts']
fig4-fsu-no-change dataset ['unit-counts']
fig5-sham-no-response dataset None
fig5-cg1-control-no-response dataset None
fig6a-s1-rsu-timelocked-high-prf dataset ['unit-counts']
fig6a-s1-rsu-delayed dataset ['unit-counts']
fig6b-s1-fsu dataset ['unit-counts']
fig6c-pom-rsu-timelocked dataset ['unit-counts']
fig6c-pom-rsu-delayed dataset ['unit-counts']
fig6d-pom-fsu dataset ['unit-counts']
fig7a-s1-rsu-dc-3000 dataset ['unit-counts']
fig7b-s1-fsu-dc-3000 dataset ['unit-counts']
fig7c-pom-rsu-dc-3000 dataset ['unit-counts']
fig7d-pom-fsu-dc-3000 dataset ['unit-counts']
fig8a-s1-rsu-dc-30 dataset ['unit-counts']
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rl "27" entries/000637-gao-2025/README.md $TMPDIR/b/build.py; sed -i 's/All 27 claims/All 30 claims/; s/all 27 claims/all 30 claims/' entries/000637-gao-2025/README.md $TMPDIR/b/build.py; grep -n "27 claims\|30 claims" entries/000637-gao-2025/README.md $TMPDIR/b/build.py
```

```
entries/000637-gao-2025/README.md
/tmp/claude-1001/b/build.py
entries/000637-gao-2025/README.md:10:| All 30 claims (unit counts, Figures 4 to 11) | Blocked: data missing |
/tmp/claude-1001/b/build.py:36:here. All 30 claims are blocked. The notebook shows what the dataset does hold: the conditions, the
/tmp/claude-1001/b/build.py:323:| all 30 claims | blocked, data_missing |
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/venv/bin/activate; python $TMPDIR/b/build.py entries/000637-gao-2025/reproduce_gao_2025.ipynb; cat > $TMPDIR/b/attempt.py <<'PYEOF'
import yaml
NB = "reproduce_gao_2025.ipynb"
WAVE = ("The dandiset's Units tables hold spike times only, with no waveforms, waveform features, "
        "electrodes or cell-type labels (data check), so units cannot be classified as RSUs or FSUs by the "
        "initial phase and afterhyperpolarization of their waveforms (Methods, Neuronal type classification). "
        "The waveforms of these units are not public anywhere else that the attempt could find; the paper's "
        "data statement names dandiset 000946, whose rats (BH494 to BH535) are not those of 000637 (BH401 to "
        "BH477).")
POM = ("No recording holds POm units, one 32-channel probe per file, electrode locations unknown, and the "
       "description names only S1.")
AC = ("No recording holds auditory cortex units; the dataset has one S1 probe per file and no recording of "
      "the paper's auditory-confound group.")
DEP = "It depends on unit-counts, which is blocked for the same reason."
POOL = ("As a variant that decides nothing, all S1 units pooled across cell types are shown in the notebook "
        "(variant:pooled-s1-prf).")
def b(claim, notes, output=None):
    o = dict(claim=claim, outcome="blocked", blocked_by="data_missing", notebook=NB, notes=notes)
    if output: o["output"] = output
    return o
S1_3000_30 = ("The 3000 Hz 60% DC (PD 200 us) and 30 Hz 0.6% DC (PD 200 us) recordings are present (30 and 26 "
              "recordings), so only the cell types are missing. ")
outcomes = [
 b("unit-counts", WAVE + " " + POM + " As a variant, S1 units with more than 2,000 spikes, all cell types "
   "together, number 4,642 in the PRF series at 200 us (4,023 at 5 V), 1,088 at 3000 Hz and 862 at 30 Hz, "
   "against the paper's S1 RSU plus FSU sums of 1,297, 366 and 209, about 3.6 times as many; so the "
   "dataset's units are not, or not only, the units the paper counted.", "claim:unit-counts"),
 b("fig4-s1-rsu-timelocked-3000", S1_3000_30 + WAVE + " " + DEP + " " + POOL + " Pooled, the 0 to 67 ms "
   "rate at 3000 Hz is above baseline (signed-rank, corrected p 2.7e-87; mean N1 364%)."),
 b("fig4-pom-rsu-timelocked-3000", POM + " " + WAVE + " " + DEP),
 b("fig4-post-3000", "Needs S1 RSUs, S1 FSUs and POm RSUs. " + WAVE + " " + POM + " " + DEP + " " + POOL),
 b("fig4-30hz-s1-rsu-inhibition", S1_3000_30 + WAVE + " " + DEP + " " + POOL + " Pooled, the 67 to 134 ms "
   "rate at 30 Hz shows no decrease (signed-rank and rank-sum corrected p 1.0; mean N1 101%), which says "
   "nothing about RSUs alone."),
 b("fig4-30hz-pom-rsu-delayed", POM + " " + WAVE + " " + DEP),
 b("fig4-fsu-no-change", "Needs S1 FSUs and POm FSUs. " + WAVE + " " + POM + " " + DEP),
 b("fig5-sham-no-response", WAVE + " " + POM + " No recording is labelled sham. Three recordings are "
   "named BASELINE (BH458, BH460, BH461; 500 trials each) with no description of whether tFUS was off or how "
   "their trial times were made. Pooled over all their units (119 units), the rate rises over the pre-trial "
   "window at 134 to 201 and 201 to 268 ms under the signed-rank test (corrected p 6.0e-09 and 1.2e-05) "
   "and not under the rank-sum test; this decides nothing (variant:baseline)."),
 b("fig5-cg1-control-no-response", "No recording is identified as targeting CG1; identifiers code PRF, "
   "pulse duration, ultrasound duration and voltage only, and the description names S1 as the target. "
   + WAVE + " " + POM),
 b("fig6a-s1-rsu-timelocked-high-prf", "All five PRFs at 200 us are present (26 to 30 recordings each). "
   + WAVE + " " + DEP + " " + POOL + " Pooled, every PRF raises the 0 to 67 ms rate over baseline under "
   "the signed-rank test, 30 Hz included (corrected p 2.6e-26), and mean N1 is highest at 3000 Hz (364%), "
   "against the paper's RSU-only pattern; mixing FSUs in may explain any difference."),
 b("fig6a-s1-rsu-delayed", "All five PRFs at 200 us are present. " + WAVE + " " + DEP + " " + POOL +
   " Pooled, 300 to 4500 Hz raise the 201 to 268 ms rate and 30 Hz does not; mean N1 is highest at 4500 Hz "
   "(241%)."),
 b("fig6b-s1-fsu", "All five PRFs at 200 us are present. " + WAVE + " " + DEP),
 b("fig6c-pom-rsu-timelocked", POM + " " + WAVE + " " + DEP),
 b("fig6c-pom-rsu-delayed", POM + " " + WAVE + " " + DEP),
 b("fig6d-pom-fsu", POM + " " + WAVE + " " + DEP),
 b("fig7a-s1-rsu-dc-3000", WAVE + " Of the 3000 Hz DC series (PD 2, 20, 100, 200, 300 us) only 100 and "
   "200 us (30% and 60%) are present (20 and 30 recordings); 0.6, 6 and 90% are missing. " + DEP),
 b("fig7b-s1-fsu-dc-3000", WAVE + " Of the 3000 Hz DC series only 30% and 60% are present. " + DEP),
 b("fig7c-pom-rsu-dc-3000", POM + " " + WAVE + " Of the 3000 Hz DC series only 30% and 60% are present. "
   + DEP),
 b("fig7d-pom-fsu-dc-3000", POM + " " + WAVE + " Of the 3000 Hz DC series only 30% and 60% are present. "
   + DEP),
 b("fig8a-s1-rsu-dc-30", WAVE + " Of the 30 Hz DC series (PD 0.2, 2, 10, 20, 30 ms) only 0.2 ms (0.6%) is "
   "present; 6 to 90% are missing. " + DEP),
 b("fig8b-s1-fsu-dc-30", WAVE + " Of the 30 Hz DC series only 0.6% is present. " + DEP),
 b("fig9a-s1-rsu-60dc", WAVE + " Of the 60% DC series (PD 20 ms, 2 ms, 400, 200, 133 us at 30 to 4500 Hz) "
   "only 1500 Hz at 400 us and 3000 Hz at 200 us are present (18 and 30 recordings). " + DEP),
 b("fig9b-s1-fsu-60dc", WAVE + " Of the 60% DC series only 1500 and 3000 Hz are present. " + DEP),
 b("fig10a-dsttc-3000", POM + " The directional correlation is between S1 and POm units. " + WAVE + " " + DEP),
 b("fig10b-dsttc-30", POM + " The directional correlation is between S1 and POm units. " + WAVE + " " + DEP),
 b("fig10c-sttc-constant-pd", POM + " The STTC is between S1 RSUs and POm RSUs. " + WAVE + " " + DEP),
 b("fig10d-sttc-60dc", POM + " " + WAVE + " Of the 60% DC series only 1500 and 3000 Hz are present. " + DEP),
 b("fig10ef-sttc-dc", POM + " " + WAVE + " Of the 30 Hz and 3000 Hz DC series only 0.6% at 30 Hz and 30% "
   "and 60% at 3000 Hz are present. " + DEP),
 b("fig11b-ac-responses", AC),
 b("fig11c-ac-s1-dsttc-30", AC + " " + WAVE),
 b("fig11d-ac-s1-dsttc-3000", AC + " " + WAVE),
]
findings = [
 dict(kind="data_missing", statement="The Units tables hold spike times only, with no waveforms, waveform "
      "features, electrode assignments or quality metrics, so the units cannot be classified as regular- or "
      "fast-spiking as the paper does, and every finding of the paper is about one or the other."),
 dict(kind="data_missing", statement="The dandiset holds one S1 probe per recording. It has no POm or auditory "
      "cortex units, no recording identified as sham or as targeting CG1, and of the paper's duty-cycle series "
      "only the conditions that share a pulse duration with the PRF series (3000 Hz at 30 and 60%, 30 Hz at "
      "0.6%, 1500 Hz at 60%)."),
 dict(kind="other", statement="The recordings cannot be linked to those the paper analysed. The paper's data "
      "statement names dandiset 000946, whose rats (BH494 to BH535) are not those of 000637 (BH401 to BH477), "
      "and 000637 has about 3.6 times as many S1 units over the paper's 2,000 spike threshold in the PRF "
      "series at 200 us as the paper reports S1 RSUs and FSUs (4,642 against 1,297). Which of these recordings, "
      "if any, the paper used is not stated."),
 dict(kind="metadata_error", statement="The description says each recording has 500 trials; 73 of the 292 "
      "files have fewer (230 in 45 files, 425 in 13, 375 in 11, and 252 to 400 in four)."),
 dict(kind="metadata_error", statement="The description calls 100, 200 and 400 us the ultrasound durations "
      "(UDs) and says the pulse duration was kept at 67 ms; in the paper's terms and in the file identifiers "
      "these are the pulse durations and 67 ms is the ultrasound duration. A 600 us recording (BH446) and "
      "recordings at 3.5, 5.5 and 7 V are present and not described."),
 dict(kind="metadata_insufficient", statement="The stimulation condition is coded only in each file's "
      "identifier (PRF, pulse duration, ultrasound duration, voltage, repeat); the trials tables have start "
      "and stop times only, the electrode locations are all 'unknown', and three recordings named BASELINE "
      "are not described (whether tFUS was off, how their trial times were made)."),
]
att = dict(schema_version=2, id="000637-gao-2025-01",
  dataset=dict(archive="dandi", id="000637", version="0.250829.1249", doi="10.48324/dandi.000637/0.250829.1249"),
  paper="doi:10.1523/jneurosci.2218-24.2025", date="2026-10-31", entry="000637-gao-2025",
  provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
    agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-12"),
    runner=dict(platform="GitHub Actions", url="https://github.com/catalystneuro/encore/actions/runs/41182673080")),
  outcomes=outcomes, findings=findings)
for o in outcomes:
    assert ": " not in o["notes"], o["claim"]
for f in findings: assert ": " not in f["statement"]
open("attempts/000637-gao-2025-01.yaml", "w").write(yaml.safe_dump(att, sort_keys=False, width=100, allow_unicode=True))
PYEOF
python $TMPDIR/b/attempt.py && head -40 attempts/000637-gao-2025-01.yaml
```

```
schema_version: 2
id: 000637-gao-2025-01
dataset:
  archive: dandi
  id: '000637'
  version: 0.250829.1249
  doi: 10.48324/dandi.000637/0.250829.1249
paper: doi:10.1523/jneurosci.2218-24.2025
date: '2026-10-31'
entry: 000637-gao-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-12
  runner:
    platform: GitHub Actions
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/venv/bin/activate; python - <<'EOF'
import os; p=os.environ['TMPDIR']+'/b/attempt.py'; s=open(p).read()
s=s.replace('POM = ("No recording holds POm units, one 32-channel probe per file, electrode locations unknown, and the "\n       "description names only S1.")',
 'POM = ("No recording holds POm units (each file has one 32-channel probe with electrode locations \'unknown\', "\n       "and the description names only S1).")')
open(p,'w').write(s)
EOF
python $TMPDIR/b/attempt.py; grep -c "POm units (each" attempts/000637-gao-2025-01.yaml; deactivate; date -u; time python tools/entry.py all entries/000637-gao-2025 2>&1 | tail -15
```

```
17
Sat Oct 31 08:19:20 UTC 2026
Installed kernelspec registry-000637-gao-2025 in executed/000637-gao-2025/.venv/share/jupyter/kernels/registry-000637-gao-2025
0 error(s)
pass  reproduce_gao_2025.ipynb  (332 s)

real	5m38.567s
user	0m35.373s
sys	0m6.797s
```

**Agent**

Checks pass and the clean run took 332 s. Confirming the executed copy's numbers match what the text states.

**Agent calls Bash**

```bash
cd  ls executed/000637-gao-2025/; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000637-gao-2025/reproduce_gao_2025.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code' and set(c.metadata.get('tags',[]))&{'claim:unit-counts','variant:baseline'} or 'clock = pd' in c.source:
        for o in c.outputs:
            if 'text' in o: print(o['text'][:2500])
    if c.cell_type=='code':
        for o in c.outputs:
            if o.get('output_type')=='error': print('ERR',o['ename'])
EOF
```

```
reproduce_gao_2025.ipynb
result.json
       onsets  window  n_units  median_N1  frac_units_up  signed_rank_p
  true onsets    0-67     6093        111          0.744              0
  true onsets  67-134     6093        102          0.578       1.21e-67
  true onsets 134-201     6093        106          0.689              0
  true onsets 201-268     6093        113          0.781              0
shifted 1.2 s    0-67     6093       98.6          0.431       6.21e-31
shifted 1.2 s  67-134     6093       97.9          0.398       9.08e-65
shifted 1.2 s 134-201     6093       97.7          0.392        6.2e-68
shifted 1.2 s 201-268     6093       97.6           0.39       1.95e-76

Per subject, median N1 at 201-268 ms (%), PRF 1500-4500 Hz:
subject  BH401  BH444  BH445  BH446  BH448  BH452  BH453  BH454  BH455  BH456  BH457  BH458  BH459  BH460  BH461  BH462  BH463  BH464  BH465  BH466  BH467  BH468  BH469  BH470  BH477
true     100.0   98.3  104.6  125.5  104.1  158.8  106.3   99.6  106.1  131.6  134.3  114.8  134.7   99.0  116.8  187.7  311.4  102.9  113.5  104.1  105.5  107.6  107.5  111.2  110.5
shifted   98.9  101.3  103.5   96.5  102.4   92.8   98.6  100.0  102.0   98.7   92.5   97.7   96.5   99.0  100.5   87.9   88.5   99.5   97.6   99.8   98.4   97.8   98.6   96.0   98.8
Subjects with true > shifted: 23 of 25

                 set  paper_S1_RSU_plus_FSU  dataset_all_volts  dataset_5V
PRF series, all PRFs                   1297               4642        4023
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/000637-gao-2025 2>&1 | tail -2; ls executed/000637-gao-2025/handover; git status --short; date -u
```

```
wrote executed/000637-gao-2025/handover
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
?? attempts/000637-gao-2025-01.yaml
?? entries/000637-gao-2025/
?? scripts
Sat Oct 31 08:25:19 UTC 2026
```

**Agent**

# Report: author run on DANDI:000637 (Gao et al. 2025)

All 30 claims are blocked as `data_missing`: none of them can be tested on this dataset. The entry runs cleanly: `entry.py all` gives 0 errors and the notebook takes 332 s. The handover is built in `executed/000637-gao-2025/handover/`.

## 1. Outcomes

| Claims | Outcome | Main reason |
|---|---|---|
| unit-counts | blocked, data_missing | No waveforms, so no RSU/FSU split; no POm units |
| fig4 S1 claims (3000 Hz time-locked, post-sonication, 30 Hz inhibition) | blocked, data_missing | No cell types (and no POm for fig4-post-3000) |
| fig4 POm claims, fig4-fsu-no-change | blocked, data_missing | No POm units, no cell types |
| fig5 sham, fig5 CG1 control | blocked, data_missing | No sham-labelled or CG1-targeted recordings; no cell types |
| fig6a, fig6b (S1) | blocked, data_missing | No cell types (all five PRFs at 200 us are present) |
| fig6c, fig6d (POm) | blocked, data_missing | No POm units |
| fig7a–d, fig8a–b, fig9a–b | blocked, data_missing | No cell types; most duty cycles are absent; no POm for 7c and 7d |
| fig10a–ef (dSTTC and STTC) | blocked, data_missing | Need S1 and POm pairs |
| fig11b–d | blocked, data_missing | No auditory cortex units |

## 2. What the dataset holds

- **Contents:** 292 files from 25 rats (BH401 to BH477), one 32-channel probe per file, all in S1. The units have spike times only: no waveforms, no electrode for each unit, and every electrode location is "unknown". The trials tables have start and stop times only, and the stimulation condition is coded only in each file's identifier.
- **Pinned version:** 0.250829.1249, the latest published one. The paper cites no version of 000637; its data statement names a different dandiset, 000946. The notebook shows that all five published versions have the same files with the same digests.
- **Not the paper's units:**
  - 000946 holds other rats (BH494 to BH535).
  - 000637 has 4,642 S1 units over the paper's 2,000-spike threshold in the PRF series at 200 us. The paper reports 1,297 S1 RSUs and FSUs combined, so 000637 has about 3.6 times as many.
  - No recording could be linked to the paper's.
- **Metadata errors:**
  - 73 of the 292 files have fewer than the 500 trials the description states.
  - The description swaps pulse duration and ultrasound duration.
  - Recordings at 600 us and at 3.5, 5.5 and 7 V exist but are not described.
  - Three recordings named BASELINE have no description saying what they are.
- **Checks that held:**
  - The trial starts behave as tFUS onsets. 74% of units fire more in the 0 to 67 ms after onset than in the 67 ms before, against 43% with onsets shifted by 1.2 s; 23 of 25 rats show the effect. Intertrial intervals are 2.25 to 2.75 s, as the paper states.
  - No unit was deposited twice.
- **Pooled variant (decides no claim):** pooling all S1 units across cell types, every PRF raises the 0 to 67 ms rate, and 300 to 4500 Hz raise the 201 to 268 ms rate.
- **Assumptions, questions:** no outcome rests on an assumption. There are no questions for the paper's authors and none for a reader.

## 3. Where the protocol was unclear

1. **`elsewhere` against `data_missing`.** The protocol says to use `data_missing` only when the data are "not public anywhere else". The paper's own deposit, 000946, is public, but it is a separate target in this registry with the same paper and holds different animals. I used `data_missing`, because the waveforms of 000637's own units are not public anywhere. I said so in the notes and left the claims' `data` fields unchanged.
2. **A target dataset that may not be the paper's data.** The protocol has no outcome or finding kind for this. I recorded it as a finding of kind `other` and gave the unit-count comparison as evidence.
3. **Analyses shown for blocked claims.** There is no guidance on tagging analyses that decide no claim. I tagged them `variant:...`, and gave the unit-counts cell the `claim:unit-counts` tag even though that claim is blocked.
4. **Untested claims in the notebook.** The protocol requires one section per tested claim and is silent when none is tested. The notebook has a header table, the data checks, a table of the conditions each claim needs against those present, the variants, and a summary.

## 4. Runtime and failures

- The run took about 26 minutes (07:59 to 08:25 UTC).
- The notebook takes about 5.5 minutes, most of it streaming the 292 files.
- Nothing failed.
- `git status` also lists untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them untouched.

Files are in `entries/000637-gao-2025/`:
- `reproduce_gao_2025.ipynb`
- `tfus.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/000637-gao-2025-01.yaml`.

## End of run

41 turns, 23 minutes, result: success.
