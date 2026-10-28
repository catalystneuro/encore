# 001177 · author · run 40671825405

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs paper claims/001177 entries | head -50; wc -l docs/*.md README.md
```

```
Wed Oct 28 10:29:51 UTC 2026
LICENSE
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
scripts
[... 66 more lines not kept]
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
cd  cat README.md; sed -n 1,271p docs/design.md
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
[... 388 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/001177/*.yaml; ls -la paper
```

```
<persisted-output>
Output too large (65.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/388d1196-06f3-42a2-8a8d-f47faef993c7/tool-results/bk2cftvxa.txt

Preview (first 2KB):
# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
# was added by the check of 2026-10-28.
#
# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
# statistics"). Figure panels of the main paper were not available as images; values in the main
# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
#
# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
# block of the delay discounting task (delay_discounting_task.py, phase2.py, phase3.py) and
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001177/10.1093-brain-awaf312.yaml"
}
```

```
1	# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
4	# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
5	# was added by the check of 2026-10-28.
6	#
7	# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
8	# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
9	# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
10	# statistics"). Figure panels of the main paper were not available as images; values in the main
11	# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
12	# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
13	#
14	# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
15	# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
16	# block of the delay discounting task (delay_discounting_task.py, phase2.py, phase3.py) and
17	# Summary_Cognitive.m, which averages each mouse's sessions within a condition, fits
18	# V = A/(1 + K*D) to the four delays with lsqcurvefit (start A = 1, K = 0.5, no bounds) and takes
19	# the AUC as the trapezoidal integral of the fitted values at D = 0, 3, 6, 9 s; (2)
20	# UCSF-Nelson-Lab/ICD-Cognitive-Arduino, tag ICD, commit f7cff8b (Zenodo doi:10.5281/zenodo.10703131),
[... 938 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001177/10.1093-brain-awaf312.yaml",
 "offset": 958
}
```

```
958	  statistics:
959	  - about: CNO main effect
960	    test: two-way repeated measures ANOVA, Bonferroni
961	    statistic: F(1, 56) = 0.97
962	    p: 0.3297
963	    n: 15 mice
964	  criterion: A claim of absence, judged on the paper's test. Pre-CNO baseline against post-CNO
965	    sessions averaged per mouse over four CNO sessions (Supplementary methods, Chemogenetic
966	    manipulation), two-way repeated measures ANOVA with Bonferroni per delay. Reproduced when the
967	    CNO effect and every per-delay test have p >= 0.05.
968	  data: elsewhere
969	  where: Zenodo doi:10.5281/zenodo.15258978 (Data_ICD_Fig1&2&5&6_CognitiveAssay.zip)
970	- id: fig5hi-dreadd-fewer-large
971	  statement: Chemogenetic inhibition of iMSNs (hM4Di) or excitation of dMSNs (hM3Dq) in the DMS shifted
972	    choices of parkinsonian mice toward immediate/small rewards.
973	  source: Figure 5H and I
974	  quote: Chemogenetic inhibition of iMSNs or excitation of dMSNs robustly shifted choices towards
975	    immediate/small rewards over delayed/large rewards
976	  statistics:
977	  - about: hM4Di, CNO main effect
[... 327 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,140p docs/archives.md; ls entries/001453-fouke-2025; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; ls paper
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
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -150; cat entries/001453-fouke-2025/README.md; ls questions | head; ls schemas
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
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json,urllib.request
u="https://api.dandiarchive.org/api/dandisets/001177/"
d=json.load(urllib.request.urlopen(u))
print(json.dumps(d,indent=1)[:1500])
v=json.load(urllib.request.urlopen(u+"versions/"))
for r in v['results']: print(r['version'],r['status'],r['asset_count'],r['size'],r['modified'])
EOF
```

```
{
 "identifier": "001177",
 "created": "2024-08-21T06:52:49.369009Z",
 "modified": "2025-09-02T21:29:48.807860Z",
 "contact_person": "Zhuang, Xiaowen",
 "embargo_status": "OPEN",
 "star_count": 0,
 "is_starred": false,
 "most_recent_published_version": {
  "version": "0.250902.2127",
  "name": "Abnormal Striatal Activity in a Mouse Model of Impulse Control Disorder in Parkinson\u2019s Disease",
  "asset_count": 56,
  "active_uploads": 0,
  "size": 1993998839930,
  "status": "Valid",
  "created": "2025-09-02T21:27:54.605701Z",
  "modified": "2025-09-02T21:27:57.196493Z",
  "release_notes": ""
 },
 "draft_version": {
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "dandi" paper/*.txt | head; python - <<'EOF'
import json,urllib.request
u="https://api.dandiarchive.org/api/dandisets/001177/versions/0.250902.2127/"
m=json.load(urllib.request.urlopen(u))
print(m.get('description'))
print(m.get('doi'))
a=json.load(urllib.request.urlopen(u+"assets/?page_size=200"))
for r in a['results']: print(r['path'], round(r['size']/1e9,1))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "import pynwb,remfile,h5py,dandi;print(pynwb.__version__)" 2>&1; which python uv; sed -n 1,80p tools/entry.py | head -80
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb,remfile,h5py,dandi;print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/bin/uv
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
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/venv && uv venv -q $TMPDIR/venv/w --python 3.13 && uv pip install -q --python $TMPDIR/venv/w/bin/python pynwb remfile h5py dandi numpy pandas scipy statsmodels matplotlib fsspec aiohttp requests openpyxl 2>&1 | tail -3; $TMPDIR/venv/w/bin/python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
```

**Agent**

Environment ready. The dataset's latest published version is 0.250902.2127 (56 NWB files, about 2 TB, 18 subjects). Now opening one file to list its contents.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > survey.py <<'EOF'
import json,urllib.request,h5py,remfile,sys,time
V="0.250902.2127"
u=f"https://api.dandiarchive.org/api/dandisets/001177/versions/{V}/assets/?page_size=200"
a=json.load(urllib.request.urlopen(u))['results']
a=sorted(a,key=lambda r:r['path'])
path=sys.argv[1]
r=[x for x in a if x['path']==path][0]
url=f"https://api.dandiarchive.org/api/assets/{r['asset_id']}/download/"
t=time.time()
f=h5py.File(remfile.File(url),'r')
def show(n,o):
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in o.attrs.items() if k not in('namespace','object_id')))
    else:
        at={k:v for k,v in o.attrs.items() if k not in('namespace','object_id')}
        print(n+'/',at)
f.visititems(show)
print(time.time()-t)
EOF
$TMPDIR/venv/w/bin/python survey.py sub-K4/sub-K4_ses-PPXopenField-K4-day2-optoSession_ecephys.nwb 2>&1 | grep -v "^acquisition/ElectricalSeries/.*electrodes" | head -150
```

```
acquisition/ {}
acquisition/ElectricalSeries/ {'comments': 'no comments', 'description': 'Acquisition traces for the ElectricalSeries.', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries/data (128282534, 32) int16 {'conversion': np.float64(2.5e-07), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/ElectricalSeries/starting_time () float64 {'rate': np.float64(30000.0), 'unit': 'seconds'}
acquisition/SpikeEvents_Electrode_0/ {'comments': 'no comments', 'description': 'Events detected with threshold crossing, manually set for each electrode.', 'neurodata_type': 'SpikeEventSeries'}
acquisition/SpikeEvents_Electrode_0/data (184116, 1, 48) int16 {'conversion': np.float64(2.5e-07), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/SpikeEvents_Electrode_0/electrodes (1,) int32 {'description': 'electrode_0', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
acquisition/SpikeEvents_Electrode_0/timestamps (184116,) float64 {'interval': np.int32(1), 'unit': 'seconds'}
acquisition/SpikeEvents_Electrode_1/ {'comments': 'no comments', 'description': 'Events detected with threshold crossing, manually set for each electrode.', 'neurodata_type': 'SpikeEventSeries'}
acquisition/SpikeEvents_Electrode_1/data (187678, 1, 48) int16 {'conversion': np.float64(2.5e-07), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/SpikeEvents_Electrode_1/electrodes (1,) int32 {'description': 'electrode_1', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
acquisition/SpikeEvents_Electrode_1/timestamps (187678,) float64 {'interval': np.int32(1), 'unit': 'seconds'}
acquisition/SpikeEvents_Electrode_10/ {'comments': 'no comments', 'description': 'Events detected with threshold crossing, manually set for each electrode.', 'neurodata_type': 'SpikeEventSeries'}
acquisition/SpikeEvents_Electrode_10/data (94829, 1, 48) int16 {'convers
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python survey.py sub-K4/sub-K4_ses-PPXopenField-K4-day2-optoSession_ecephys.nwb 2>&1 | grep -v "SpikeEvents_Electrode" | sed -n '/^general\/extracellular_ephys\/electrodes\/offset/,$p'
```

```
general/extracellular_ephys/electrodes/offset_to_physical_unit (32,) float64 {'description': 'no description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/physical_unit (32,) object {'description': 'no description', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/rel_x (32,) float64 {'description': 'rel_x', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/rel_y (32,) float64 {'description': 'rel_y', 'neurodata_type': 'VectorData'}
general/institution () object {}
general/lab () object {}
general/session_id () object {}
general/source_script () object {'file_name': 'C:\\Users\\zhuan\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\neuroconv\\basedatainterface.py'}
general/subject/ {'neurodata_type': 'Subject'}
general/subject/date_of_birth () object {}
general/subject/description () object {}
general/subject/genotype () object {}
general/subject/sex () object {}
general/subject/species () object {}
general/subject/subject_id () object {}
identifier () object {}
processing/ {}
processing/ecephys/ {'description': 'Intermediate data from extracellular electrophysiology recordings, e.g., LFP.', 'neurodata_type': 'ProcessingModule'}
processing/ecephys/LFP/ {'neurodata_type': 'LFP'}
processing/ecephys/LFP/ElectricalSeries/ {'comments': 'no comments', 'description': 'Acquisition traces for the ElectricalSeries.', 'neurodata_type': 'ElectricalSeries'}
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > survey2.py <<'EOF'
import json,urllib.request,h5py,remfile,sys,time
V="0.250902.2127"
u=f"https://api.dandiarchive.org/api/dandisets/001177/versions/{V}/assets/?page_size=200"
a=json.load(urllib.request.urlopen(u))['results']
for path in sys.argv[1:]:
    r=[x for x in a if x['path']==path][0]
    url=f"https://api.dandiarchive.org/api/assets/{r['asset_id']}/download/"
    f=h5py.File(remfile.File(url),'r')
    print("=====",path)
    def show(n,o):
        if 'SpikeEvents_Electrode' in n or n.startswith('specifications'): return
        if isinstance(o,h5py.Dataset):
            s=o.shape
            val=o[()] if o.size<=3 and o.dtype.kind in 'OSU' or s==() else ''
            print(n,s,o.dtype,val, {k:v for k,v in o.attrs.items() if k in('description','unit','rate','conversion')})
        else:
            print(n+'/',{k:v for k,v in o.attrs.items() if k not in('namespace','object_id')})
    f.visititems(show)
    print('n SpikeEvents', sum(1 for k in f['acquisition'] if k.startswith('SpikeEvents')))
EOF
$TMPDIR/venv/w/bin/python survey2.py sub-D0/sub-D0_ses-PPXopenField-D0-day1_ecephys.nwb 2>&1 | grep -v "^general/extracellular_ephys/electrodes"
```

```
===== sub-D0/sub-D0_ses-PPXopenField-D0-day1_ecephys.nwb
acquisition/ {}
acquisition/ElectricalSeries0/ {'comments': 'no comments', 'description': 'Acquisition traces for the ElectricalSeries.', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries0/data (54100222, 32) int16  {'conversion': np.float64(2.5e-07), 'unit': 'volts'}
acquisition/ElectricalSeries0/electrodes (32,) int32  {'description': 'electrode_table_region'}
acquisition/ElectricalSeries0/starting_time () float64 0.0074 {'rate': np.float64(30000.0), 'unit': 'seconds'}
acquisition/ElectricalSeries1/ {'comments': 'no comments', 'description': 'Acquisition traces for the ElectricalSeries.', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries1/data (563854614, 32) int16  {'conversion': np.float64(2.5e-07), 'unit': 'volts'}
acquisition/ElectricalSeries1/electrodes (32,) int32  {'description': 'electrode_table_region'}
acquisition/ElectricalSeries1/starting_time () float64 1900.8705666666665 {'rate': np.float64(30000.0), 'unit': 'seconds'}
acquisition/ElectricalSeries2/ {'comments': 'no comments', 'description': 'Acquisition traces for the ElectricalSeries.', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries2/data (124309684, 32) int16  {'conversion': np.float64(2.5e-07), 'unit': 'volts'}
acquisition/ElectricalSeries2/electrodes (32,) int32  {'description': 'electrode_table_region'}
acquisition/ElectricalSeries2/starting_time () float64 20747.845666666668 {'rate': np.float64(30000.0), 'unit': 'seconds'}
analysis/ {}
file_create_date (1,) object [b'2025-07-22T09:46:19.143802-07:00'] {}
general/ {}
general/devices/ {}
general/devices/DeviceEcephys/ {'description': 'no description', 'neurodata_type': 'Device'}
general/experimenter (1,) object [b'Xiaowen, Zhuang'] {}
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > survey3.py <<'EOF'
import json,urllib.request,h5py,remfile,sys,time
from concurrent.futures import ThreadPoolExecutor
V="0.250902.2127"
u=f"https://api.dandiarchive.org/api/dandisets/001177/versions/{V}/assets/?page_size=200"
a=sorted(json.load(urllib.request.urlopen(u))['results'],key=lambda r:r['path'])
def one(r):
    try:
        url=f"https://api.dandiarchive.org/api/assets/{r['asset_id']}/download/"
        f=h5py.File(remfile.File(url),'r')
        top=sorted(f.keys())
        acq=[k for k in f['acquisition'] if not k.startswith('SpikeEvents')]
        nse=sum(1 for k in f['acquisition'] if k.startswith('SpikeEvents'))
        es=[(k,f['acquisition'][k]['data'].shape[0]/30000/60, float(f['acquisition'][k]['starting_time'][()])/60) for k in acq if 'data' in f['acquisition'][k]]
        g=lambda p: f[p][()].decode() if p in f else None
        other=[k for k in top if k not in ('acquisition','analysis','file_create_date','general','identifier','processing','session_description','session_start_time','specifications','stimulus','timestamps_reference_time')]
        stim=list(f['stimulus/presentation'].keys())
        proc={k:list(f['processing'][k].keys()) for k in f['processing']}
        ann=list(f['analysis'].keys())
        evt=[k for k in f['acquisition'] if not k.startswith('SpikeEvents') and not k.startswith('ElectricalSeries')]
        return (r['path'], g('general/subject/genotype'), g('general/subject/sex'), (g('general/subject/description') or '')[:60], g('general/session_id'), g('session_start_time'), nse, [(k,round(d,1),round(s,1)) for k,d,s in es], other, stim, proc, ann, evt)
    except Exception as e:
        return (r['path'],'ERR',repr(e))
with ThreadPoolExecutor(8) as ex:
    for res in ex.map(one,a): print(res)
EOF
time $TMPDIR/venv/w/bin/python survey3.py 2>&1 | tee survey3.out
```

```
('sub-C3-2/sub-C3-2_ses-PPXopenField-C3-2-day1_ecephys.nwb', 'Drd1aCre', 'F', 'A total of 1.5â€¯microliters of saline was injected bilatera', 'PPXopenField-C3.2-day1', '2021-11-30T21:35:42.746000-08:00', 32, [('ElectricalSeries0', 30.6, 0.0), ('ElectricalSeries1', 300.9, 31.9), ('ElectricalSeries2', 69.9, 333.6)], [], [], {'ecephys': ['LFP']}, [], [])
('sub-C3-2/sub-C3-2_ses-PPXopenField-C3-2-day2_ecephys.nwb', 'Drd1aCre', 'F', 'A total of 1.5â€¯microliters of saline was injected bilatera', 'PPXopenField-C3.2-day2', '2021-12-09T20:19:19.383000-08:00', 25, [('ElectricalSeries0', 33.6, 0.0), ('ElectricalSeries1', 296.6, 35.0), ('ElectricalSeries2', 72.3, 332.3)], [], [], {'ecephys': ['LFP']}, [], [])
('sub-C9/sub-C9_ses-PPXopenField-C9-day1_ecephys.nwb', 'A2aCre', 'M', 'A total of 1.5â€¯microliters of 6-OHDA was injected bilatera', 'PPXopenField-C9-day1', '2021-11-21T22:23:09.467000-08:00', 22, [('ElectricalSeries0', 30.4, 0.0), ('ElectricalSeries1', 10.4, 31.5), ('ElectricalSeries2', 42.6, 42.7), ('ElectricalSeries3', 0.6, 85.4), ('ElectricalSeries4', 257.5, 86.0), ('ElectricalSeries5', 68.5, 345.5)], [], [], {'ecephys': ['LFP']}, [], [])
('sub-C9/sub-C9_ses-PPXopenField-C9-day2_ecephys.nwb', 'A2aCre', 'M', 'A total of 1.5â€¯microliters of 6-OHDA was injected bilatera', 'PPXopenField-C9-day2', '2021-11-26T22:10:31.094000-08:00', 22, [('ElectricalSeries0', 30.6, 0.0), ('ElectricalSeries1', 302.2, 31.9), ('ElectricalSeries2', 69.0, 335.1)], [], [], {'ecephys': ['LFP']}, [], [])
('sub-D0/sub-D0_ses-PPXopenField-D0-day1_ecephys.nwb', 'A2aCre', 'M', 'A total of 1.5â€¯microliters of 6-OHDA was injected bilatera', 'PPXopenField-D0-day1', '2022-03-07T19:58:35.940000-08:00', 27, [('ElectricalSeries0', 30.1, 0.0), ('ElectricalSeries1', 313.3, 31.7), ('ElectricalSeries2', 69.1, 345.8)], [], [], {'ecephys': ['LFP']}, [], [])
('sub-D0/sub-D0_ses-PPXopenField-D0-day2_ecephys.nwb', 'A2aCre', 'M', 'A total of 1.5â€¯microliters of 6-OHDA was injected bilatera', 'PPXopenField-D0-day2'
[... 55 more lines not kept]
```

**Agent**

Two files (E0 day4, P4 day1) have a `units` table; the other 54 have only per-electrode threshold-crossing snippets. Looking at those two tables.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > units.py <<'EOF'
import json,urllib.request,h5py,remfile,sys,numpy as np
V="0.250902.2127"
a=json.load(urllib.request.urlopen(f"https://api.dandiarchive.org/api/dandisets/001177/versions/{V}/assets/?page_size=200"))['results']
for path in sys.argv[1:]:
    r=[x for x in a if x['path']==path][0]
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{r['asset_id']}/download/"),'r')
    u=f['units']; print(path, dict(u.attrs))
    for k in u: 
        d=u[k]; print(' ',k,d.shape,d.dtype,dict((kk,vv) for kk,vv in d.attrs.items() if kk=='description'))
        if d.shape[0]<200 and d.dtype.kind!='V': print('   ',d[:40])
    st=u['spike_times'][:]; idx=u['spike_times_index'][:]
    print('n units',len(idx),'spikes',len(st),'range',st.min(),st.max(), 'sorted per unit', all(np.all(np.diff(s)>=0) for s in np.split(st,idx[:-1])))
    print('counts',np.diff(np.r_[0,idx]))
EOF
$TMPDIR/venv/w/bin/python units.py sub-E0/sub-E0_ses-PPXopenField-E0-day4_ecephys.nwb sub-P4/sub-P4_ses-PPXopenField-P4-day1_ecephys.nwb 2>&1
```

```
sub-E0/sub-E0_ses-PPXopenField-E0-day4_ecephys.nwb {'colnames': array(['spike_times', 'unit_name'], dtype=object), 'description': 'Autogenerated by neuroconv.', 'namespace': 'core', 'neurodata_type': 'Units', 'object_id': '7b419731-9fd9-4867-ab3d-b95c818cd78e'}
  id (60,) int32 {}
    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
  spike_times (26380440,) float64 {'description': 'the spike times for each unit'}
  spike_times_index (60,) uint32 {'description': "Index for VectorData 'spike_times'"}
    [ 1394151  1399405  2638650  2641135  3699136  3700821  3700822  4061400
  4066485  5109423  5119507  5871598  5884599  6405618  6411331  7252941
  7257484  8062051  8076662  9511905  9518612 10263722 10266531 10966504
 10972143 11451401 11456852 11957038 11982313 12623342 12633011 13497062
 13499533 13765290 13774616 14449546 14460880 15648349 15650832 16431896]
  unit_name (60,) object {'description': 'Unique reference for each unit.'}
    [b'0' b'1' b'2' b'3' b'4' b'5' b'6' b'7' b'8' b'9' b'10' b'11' b'12' b'13'
 b'14' b'15' b'16' b'17' b'18' b'19' b'20' b'21' b'22' b'23' b'24' b'25'
 b'26' b'27' b'28' b'29' b'30' b'31' b'32' b'33' b'34' b'35' b'36' b'37'
 b'38' b'39']
n units 60 spikes 26380440 range 0.010166666666666666 24762.326366666668 sorted per unit True
counts [1394151    5254 1239245    2485 1058001    1685       1  360578    5085
 1042938   10084  752091   13001  521019    5713  841610    4543  804567
   14611 1435243    6707  745110    2809  699973    5639  479258    5451
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://zenodo.org/api/records/15258978 | python -c "
import json,sys; d=json.load(sys.stdin)
print(d['metadata']['title'], d['metadata'].get('version'), d['metadata']['publication_date'], d['id'], d.get('conceptrecid'))
print(d['metadata'].get('description','')[:3000])
for f in d['files']: print(f['key'], f['size'], f['checksum'])
print(d['links'].get('versions'))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://zenodo.org/api/records/15258978/versions | python -c "
import json,sys; d=json.load(sys.stdin); [print(h['id'],h['metadata'].get('version'),h['metadata']['publication_date'],h['doi']) for h in d['hits']['hits']]"; for f in README_ICD_CognitiveAssessment.txt README_ICD_LocomotionRaw.txt README_ICD_TH_Striatum_RawImages.txt README_ICD_SNcTH_CellCounting_RawImages.txt; do echo "== $f"; curl -sL "https://zenodo.org/records/15258978/files/$f?download=1"; echo; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > zl.py <<'EOF'
import fsspec,zipfile,sys,collections
url=sys.argv[1]
z=zipfile.ZipFile(fsspec.open(url,block_size=2**20).open())
n=z.namelist(); print(len(n))
c=collections.Counter('/'.join(x.split('/')[:-1]) for x in n)
for k,v in sorted(c.items()): print(v,k)
for x in n[:15]: print(x)
EOF
$TMPDIR/venv/w/bin/python zl.py "https://zenodo.org/records/15258978/files/Data_ICD_Fig1%262%265%266_CognitiveAssay.zip?download=1"
```

```
7
5 Data_ICD_Fig1&2&5&6_CognitiveAssay
2 __MACOSX/Data_ICD_Fig1&2&5&6_CognitiveAssay
Data_ICD_Fig1&2&5&6_CognitiveAssay/
Data_ICD_Fig1&2&5&6_CognitiveAssay/.DS_Store
__MACOSX/Data_ICD_Fig1&2&5&6_CognitiveAssay/._.DS_Store
Data_ICD_Fig1&2&5&6_CognitiveAssay/Data_ICD_PPX.zip
Data_ICD_Fig1&2&5&6_CognitiveAssay/Data_ICD_DREADD.zip
Data_ICD_Fig1&2&5&6_CognitiveAssay/Data_ICD_A77636.zip
__MACOSX/Data_ICD_Fig1&2&5&6_CognitiveAssay/._Data_ICD_A77636.zip
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > zl2.py <<'EOF'
import fsspec,zipfile,io,collections
url="https://zenodo.org/records/15258978/files/Data_ICD_Fig1%262%265%266_CognitiveAssay.zip?download=1"
z=zipfile.ZipFile(fsspec.open(url,block_size=2**22).open())
for inner in ['Data_ICD_PPX.zip','Data_ICD_A77636.zip','Data_ICD_DREADD.zip']:
    b=z.read('Data_ICD_Fig1&2&5&6_CognitiveAssay/'+inner)
    zi=zipfile.ZipFile(io.BytesIO(b))
    n=[x for x in zi.namelist() if not x.startswith('__MACOSX') and not x.endswith('/') and 'DS_Store' not in x]
    print('=====',inner,len(b),len(n))
    c=collections.Counter('/'.join(x.split('/')[:-1]) for x in n)
    for k,v in sorted(c.items()): print(v,k)
    for x in n[:8]: print('  ',x)
    open(inner,'wb').write(b)  # scratch copy for exploration only
EOF
$TMPDIR/venv/w/bin/python zl2.py
```

```
===== Data_ICD_PPX.zip 16956540 1168
1168 Data_ICD_PPX
   Data_ICD_PPX/H4.1_delay_082423.CSV
   Data_ICD_PPX/H5.2_delay_PPXwashout_071623.CSV
   Data_ICD_PPX/D4.2_nosepoke_012022_right.CSV
   Data_ICD_PPX/E3.3_delay_PPXwashout_082322.CSV
   Data_ICD_PPX/P5_nosepoke_leftright_0821_day2_right.CSV
   Data_ICD_PPX/D6_nosepoke_011922_left.CSV
   Data_ICD_PPX/N5_nosepoke_111820_left.CSV
   Data_ICD_PPX/E4_center nosepoke_060622.CSV
===== Data_ICD_A77636.zip 8916469 553
553 Data_ICD_A77636
   Data_ICD_A77636/R5_nosepoke_090524.CSV
   Data_ICD_A77636/R2.2_nosepoke_090524.CSV
   Data_ICD_A77636/R3.3_delay_010725.CSV
   Data_ICD_A77636/R1.5_center nosepoke_111524.CSV
   Data_ICD_A77636/R4.1_delay_010725.CSV
   Data_ICD_A77636/O0.6_delay_090524.CSV
   Data_ICD_A77636/R3.1_center nosepoke_091024.CSV
   Data_ICD_A77636/R0.2_delay_A77636_012225.CSV
[... 11 more lines not kept]
```

**Agent**

Raw operant event logs (CSV per session). Fetching the paper's analysis code to parse them as the authors did.

**Agent calls Bash**

```bash
cd $TMPDIR; git clone -q https://github.com/UCSF-Nelson-Lab/ICD-Cognitive-Analysis.git code 2>&1|tail -2; cd code && git log --oneline | head; git tag; ls -la; wc -l *
```

```
5528e222 Relocate Arduino code
26469a3f .DS_Store banished!
6ea9af21 Add analysis code
ICD
total 180
drwxr-xr-x 3 runner runner   180 Oct 28 10:38 .
drwx------ 7 runner runner   340 Oct 28 10:38 ..
drwxr-xr-x 7 runner runner   240 Oct 28 10:38 .git
-rw-r--r-- 1 runner runner    10 Oct 28 10:38 .gitignore
-rw-r--r-- 1 runner runner   386 Oct 28 10:38 README.md
-rw-r--r-- 1 runner runner 13968 Oct 28 10:38 Summary_Cognitive.m
-rw-r--r-- 1 runner runner 59113 Oct 28 10:38 delay_discounting_task.py
-rw-r--r-- 1 runner runner 46299 Oct 28 10:38 phase2.py
-rw-r--r-- 1 runner runner 48285 Oct 28 10:38 phase3.py
    18 README.md
   356 Summary_Cognitive.m
  1379 delay_discounting_task.py
  1154 phase2.py
  1207 phase3.py
  4114 total
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; git rev-parse HEAD; cat README.md; sed -n 1,200p delay_discounting_task.py
```

````
5528e2229f186e0785a676ae6f15219c47146930
"# ICD-Cognitive-Analysis"

## How to use the Python Analysis

1. Open the python file using command line tool (Terminal for MacOS), for example
```python
python python2.py
```

2. Open the data file (select `open` in the option) using via the opened window.

3. Select OK in the pop-up window

4. Results are shown in the terminal.

## PIP requirement

pandas, pyqt5
#!/usr/bin/python3
[... 200 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -n "def processCsv_1" -A 400 delay_discounting_task.py | head -420
```

```
424:    def processCsv_1(self):
425-        block_lock = False
426-        result = {}
427-        current_block = ""
428-        latency_time = 0
429-        trial_npc_lock = False
430-        centri_npc_lock = False
431-        time_error_flag = False
432-        latency_lock = False
433-        latency_lock2 = False
434-
435-
436-        latency_Bin = 0
437-        latency_Din = 0
438-        latency_calc_lock = False
439-        reward_status = False
440-        first_cin = False
441-        trial_count = 0
442-        for x in self.raw[0]:
443-            slots = x.split(",")
[... 382 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import zipfile
z=zipfile.ZipFile('Data_ICD_PPX.zip')
n=[x for x in z.namelist() if x.endswith('.CSV') and not x.startswith('__')]
t=z.read('Data_ICD_PPX/H4.1_delay_082423.CSV').decode('latin1').splitlines()
print(len(t)); print('\n'.join(t[:60]))
import collections
c=collections.Counter(l.split(',')[1] if ',' in l else l for l in t)
print(c.most_common(60))
EOF
```

```
2042
Date, Event Name, Event Time
"2023/8/24 18:5:14", B1_, 00:00:03:206
"2023/8/24 18:5:14", trial start, 00:00:03:216
"2023/8/24 18:5:18", np_C in, 00:00:07:238
"2023/8/24 18:5:18", cen tri, 00:00:07:250
"2023/8/24 18:5:18", np_C out, 00:00:07:264
"2023/8/24 18:5:18", np_C in, 00:00:07:336
"2023/8/24 18:5:18", np_C out, 00:00:07:351
"2023/8/24 18:5:18", np_C in, 00:00:07:364
"2023/8/24 18:5:20", np_C out, 00:00:09:484
"2023/8/24 18:5:21", np_C in, 00:00:09:908
"2023/8/24 18:5:22", np_C out, 00:00:11:531
"2023/8/24 18:5:28", side omi, 00:00:17:264
"2023/8/24 18:5:28", timeout, 00:00:17:277
"2023/8/24 18:6:9", trial start, 00:00:58:219
"2023/8/24 18:6:10", np_C in, 00:00:58:797
"2023/8/24 18:6:10", cen tri, 00:00:58:809
"2023/8/24 18:6:10", np_C out, 00:00:58:823
"2023/8/24 18:6:10", np_B in, 00:00:59:319
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat Summary_Cognitive.m
```

```
%%
clear all;
close all;
% Specify the Excel file path
filePath = '{Your file path}';
% Get the sheet names in the Excel file
[~, sheetNames] = xlsfinfo(excelFilePath);
% Initialize cell arrays to store averages and standard errors for each sheet
averages = cell(numel(sheetNames), 1);
stdErrors = cell(numel(sheetNames), 1);
% Define the column index for "Animal ID" (assuming it's in the first column)
animalIDColumn = 1;

%% calculate the averages across different days of PPX injection
% Initialize cell arrays to store averages and standard errors for each sheet
SeparateAvg = cell(numel(sheetNames), 1);
SeparateSTE = cell(numel(sheetNames), 1);

% Define the column index for "Animal ID" (assuming it's in the first column)
animalIDColumn = 1;
[... 338 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import zipfile,re,collections
for zn in ['Data_ICD_PPX.zip','Data_ICD_A77636.zip','Data_ICD_DREADD.zip']:
    z=zipfile.ZipFile(zn)
    n=[x.split('/')[-1] for x in z.namelist() if x.upper().endswith('.CSV') and not x.startswith('__')]
    kinds=collections.Counter()
    for x in n:
        parts=x[:-4].split('_')
        kinds['_'.join(parts[1:-1]) if len(parts)>2 else parts[1]]+=1
    print(zn,len(n)); print(sorted(kinds.items()))
    other=[x for x in z.namelist() if not x.upper().endswith('.CSV')]
    print('non-csv',other[:10])
EOF
```

```
Data_ICD_PPX.zip 1168
[('center nosepoke', 230), ('center nosepoke trig _0825', 3), ('center nosepoke trig _0826', 3), ('center nosepoke trig _0827', 3), ('center nosepoke trig _0828', 3), ('center nosepoke trig _0829', 3), ('center nosepoke trig _0831', 3), ('center nosepoke_081120', 1), ('centernosepoke', 3), ('delay', 144), ('delay discounting', 3), ('delay discounting_PPX', 4), ('delay_PPX', 173), ('delay_PPX washout', 10), ('delay_PPXwashont', 1), ('delay_PPXwashout', 79), ('delay_washout', 15), ('nosepoke training', 1), ('nosepoke training_111820', 2), ('nosepoke training_111920', 2), ('nosepoke training_112320', 2), ('nosepoke training_113020', 2), ('nosepoke_011322', 15), ('nosepoke_011322.', 1), ('nosepoke_011421', 2), ('nosepoke_011422', 14), ('nosepoke_011622', 16), ('nosepoke_011822', 16), ('nosepoke_011921', 2), ('nosepoke_011922', 14), ('nosepoke_012022', 16), ('nosepoke_050423', 22), ('nosepoke_050523', 22), ('nosepoke_050823', 22), ('nosepoke_051023', 22), ('nosepoke_051123', 22), ('nosepoke_051223', 22), ('nosepoke_051822', 2), ('nosepoke_052322', 6), ('nosepoke_052422', 6), ('nosepoke_052522', 8), ('nosepoke_052622', 8), ('nosepoke_052722', 8), ('nosepoke_053122', 8), ('nosepoke_060122', 2), ('nosepoke_060922', 2), ('nosepoke_061022', 2), ('nosepoke_061422', 2), ('nosepoke_061522', 2), ('nosepoke_061622', 2), ('nosepoke_061722', 2), ('nosepoke_062222', 4), ('nosepoke_062322', 4), ('nosepoke_062422', 4), ('nosepoke_062922', 4), ('nosepoke_063022', 4), ('nosepoke_070122', 4), ('nosepoke_080320', 4), ('nosepoke_080420', 6), ('nosepoke_080620', 6), ('nosepoke_080720', 6), ('nosepoke_080820', 2), ('nosepoke_091823', 4), ('nosepoke_092023', 4), ('nosepoke_092123', 4), ('nosepoke_092223', 4), ('nosepoke_092523', 4), ('nosepoke_092623', 4), ('nosepoke_101122', 8), ('nosepoke_101322', 8), ('nosepoke_101422', 8), ('nosepoke_101722', 8), ('nosepoke_101822', 8), ('nosepoke_101922', 6), ('nosepoke_102222', 2), ('nosepoke_111620', 10), ('nosepoke_111820', 8), ('
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > xl.py <<'EOF'
import pandas as pd,sys,io,urllib.parse,fsspec
for name in sys.argv[1:]:
    url="https://zenodo.org/records/15258978/files/"+urllib.parse.quote(name)+"?download=1"
    b=fsspec.open(url).open().read()
    x=pd.read_excel(io.BytesIO(b),sheet_name=None,header=None)
    for s,d in x.items():
        print('=====',name,'|',s,d.shape)
        with pd.option_context('display.width',250,'display.max_columns',40,'display.max_rows',80):
            print(d.head(45).to_string(max_colwidth=14))
EOF
$TMPDIR/venv/w/bin/python xl.py Data_ICD_Fig1_Rotarod_PPX.xlsx Data_ICD_FigS6_SliceValidation.xlsx 2>&1 | head -200
```

```
===== Data_ICD_Fig1_Rotarod_PPX.xlsx | Sheet1 (47, 7)
                0   1              2              3   4              5              6
0   Ctrl_baseline NaN  Park_cohor...  Park_cohor... NaN  Park_cohor...  Park_cohor...
1   latency to... NaN  latency to...  latency to... NaN  latency to...  latency to...
2       94.333333 NaN      48.333333      70.666667 NaN             46             74
3              93 NaN             96             97 NaN      64.666667             39
4       70.666667 NaN      60.333333             47 NaN             79      66.333333
5      105.666667 NaN      24.333333      62.666667 NaN             46      62.333333
6       93.666667 NaN      23.333333      61.333333 NaN             55      36.666667
7              91 NaN      61.666667     114.666667 NaN             84      61.666667
8              89 NaN      35.333333      63.666667 NaN             28      30.333333
9       99.333333 NaN      36.666667      95.333333 NaN      29.666667      55.333333
10            113 NaN      47.333333      75.666667 NaN      49.333333      50.666667
11           77.5 NaN      20.333333             26 NaN             49             52
12      70.666667 NaN      60.333333      73.333333 NaN             48      53.333333
13     109.666667 NaN      53.666667      63.333333 NaN      44.333333      63.333333
14      75.666667 NaN           48.5      82.666667 NaN      49.333333      76.666667
15      74.666667 NaN             15             26 NaN      59.666667      81.666667
16     106.666667 NaN             44     127.666667 NaN             17             54
17     123.333333 NaN             56             62 NaN      49.666667             58
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
import pandas as pd,io,urllib.parse,fsspec
for name in ["Data_ICD_Fig1_Rotarod_PPX.xlsx"]:
    b=fsspec.open("https://zenodo.org/records/15258978/files/"+urllib.parse.quote(name)+"?download=1").open().read()
    d=pd.read_excel(io.BytesIO(b),header=None)
    print(d.iloc[:2].to_dict()); print(d.count())
EOF
$TMPDIR/venv/w/bin/python xl.py Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx 2>&1 | head -120
```

```
{0: {0: 'Ctrl_baseline', 1: 'latency to fall (s)'}, 1: {0: nan, 1: nan}, 2: {0: 'Park_cohort1_baseline', 1: 'latency to fall (s)'}, 3: {0: 'Park_cohort1_PPX', 1: 'latency to fall (s)'}, 4: {0: nan, 1: nan}, 5: {0: 'Park_cohort2_baseline', 1: 'latency to fall (s)'}, 6: {0: 'Park_cohort2_Saline', 1: 'latency to fall (s)'}}
0    42
1     0
2    47
3    47
4     0
5    29
6    29
dtype: int64
===== Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx | Fig. S1D (154, 8)
                0              1              2              3              4              5              6              7
0   AP coordin...  OriginalIm...          Notes  Behavior Name  Left Side ...  Left Side ...  Right Side...  Right Side...
1           -3.07  Xiaowen_C2...            NaN             C2             36     147116.409             30     155719.299
2             NaN  Xiaowen_C3...  *swap left...           C3.2             95     130964.066             13     174614.586
3             NaN  RIGHT_Xiao...            NaN           C1.1              X              X             60     169186.264
4             NaN  LEFT_Xiaow...            NaN           C1.1             74     124289.967              X              X
5             NaN  Xiaowen_C9...            NaN             C9             46     197524.285             52      133777.76
6           -3.07  RIGHT_D2_S...            NaN             D2              X              X             62     142930.503
7             NaN  LEFT_D2_SN...            NaN             D2             65       115333.6              X              X
8             NaN  D2.2_SNC_S...            NaN           D2.2            116     222397.343             26     258593.504
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
import pandas as pd,io,urllib.parse,fsspec
pd.set_option('display.width',250); pd.set_option('display.max_columns',40)
for name in ["Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx","Data_ICD_Fig3_HistologyQuantification_striatum_raw.xlsx"]:
    b=fsspec.open("https://zenodo.org/records/15258978/files/"+urllib.parse.quote(name)+"?download=1").open().read()
    open(name,'wb').write(b)
    x=pd.read_excel(io.BytesIO(b),sheet_name=None,header=None)
    for s,d in x.items():
        print('=====',name,'|',s,d.shape)
        print(d.iloc[0].tolist())
        # rows where column0 is a string label
        lab=d[d[0].apply(lambda v:isinstance(v,str))][0]
        print(lab.to_dict())
EOF
```

```
===== Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx | Fig. S1D (154, 8)
['AP coordinates', 'OriginalImageName', 'Notes', 'Behavior Name', 'Left Side Count', 'Left Side Area', 'Right Side Count', 'Right Side Area']
{0: 'AP coordinates'}
===== Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx | Fig. S1H&I (713, 17)
['Session1_Ctrl', '# of rewarded trials', 'Latency to Trigger (s)', '# omission', '# of total trials', '% of successful trials', np.float64(nan), '# of rewarded trials', 'Latency to Trigger (s)', '# omission', '# of total trials', '% of successful trials', nan, '% of TOTAL successful trials', 'TOTAL Latency to Trigger (s)', np.float64(nan), nan]
{0: 'Session1_Ctrl', 38: 'Session1_Park', 125: 'Session2_Ctrl', 161: 'Session2_Park', 246: 'Session3_Ctrl', 283: 'Session3_Park', 368: 'Session4_Ctrl', 405: 'Session4_Park', 490: 'Session5_Ctrl', 520: 'Session5_Park', 605: 'Session6_Ctrl', 636: 'Session6_Park'}
===== Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx | Fig. S1K&L (701, 9)
['Session1_Ctrl', '# Total Trials', '# left rewarded trials', '# of right rewarded trials', '# of center triggered trials', '% of succesful trials', '# of center omission trials', '# of side omission trials', 'CenterTriggerLatency (s)']
{0: 'Session1_Ctrl', 33: 'average_session1', 34: 'SE_session1', 35: 'Session1_Park', 116: 'average_session1', 117: 'SE_session1', 118: 'Session1_Park', 149: 'average_session2', 150: 'SE_session2', 152: 'Session2_Park', 233: 'average_session2', 234: 'SE_session2', 236: 'Session3_Ctrl', 269: 'average_session3', 270: 'SE_session3', 272: 'Session3_Park', 353: 'average_session3', 354: 'SE_session3', 356: 'Session4_Ctrl', 388: 'average_session4', 389: 'SE_session4', 391: 'Session4_Park', 472: 'average_session4', 473: 'SE_session4', 475: 'Session 5_Ctrl', 508: 'average_session5', 509: 'SE_session5', 511: 'Session5_Park', 591: 'average_session5', 592: 'SE_session5', 594: 'Session 6_Ctrl', 621: 'average_session6', 622: 'SE_session6', 624: 'Session 6_Park', 6
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  which pdftotext; pdftotext -layout paper/10.1093-brain-awaf312.supp.pdf $TMPDIR/supp.txt 2>&1 | head -2; wc -l $TMPDIR/supp.txt; wc -c paper/10.1093-brain-awaf312.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  uv pip install -q --python $TMPDIR/venv/w/bin/python pypdf && $TMPDIR/venv/w/bin/python -c "
import pypdf;r=pypdf.PdfReader('paper/10.1093-brain-awaf312.supp.pdf');open('$TMPDIR/supp.txt','w').write('\n'.join(f'=== page {i+1}\n'+p.extract_text() for i,p in enumerate(r.pages)))"; wc -l $TMPDIR/supp.txt; grep -n -i "histolog\|corrected total\|CTCF\|rotarod\|stable\|coefficient of var\|CV\b" $TMPDIR/supp.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 400,800p $TMPDIR/supp.txt
```

```
their free-feeding body weight.  
Surgical Procedures 
 For subsequent optically identified single -unit recordings, AAV5 -DIO-ChR2-eYFP 
(UPenn Vector Core, 1.0 μL, undiluted) was injected into the left DMS ( + 0.8 mm AP, + 1.5 mm 
ML, − 2.5 mm DV) in a subset of mice. For chemogenetic experiments, AAV5 -DIO-hM4D(Gi)-
mCherry (UNC Vector Core, 1.0 μL, diluted 1:2 in sterile saline), AAV5-DIO-hM3q(Gq)-mCherry 
(UNC Vector Core, 1.0 μL, undiluted), or AAV5 -DIO-mCherry (UNC Vector Core, 1.0 μL, 
undiluted) was injected in bilateral DMS ( + 0.8 mm AP,  1.5 mm ML, − 2.5 mm DV). Both 6-
OHDA and virus were injected at a rate of 0.2 μL/min, after which the injection cannula was left 
in place for 10 min prior to being withdrawn, and the scalp being sutured. In preparation for in 
vivo single-unit recordings, D1-Cre and A2a -Cre mice were injected bilaterally with DLS 6 -
OHDA (or saline) and DMS DIO -ChR2-eYFP, followed by implantation of DMS optrode arrays 
in a second surgical procedure.  
Motor Assessment 
 Each rotarod session included three trials with a 10 -min intertrial interval. The rotation 
speed gradually increased from 5 to 80 RPM over 5 min. Mice were scored for their latency to fall 
=== page 12
 - 12 - 
and the average across three trials was reported. Open field locomotion was also performed in a 
subset of mice to examine the therapeutic effect of PPX or A77636. Mice were habituated to the 
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
import pandas as pd,io,urllib.parse,fsspec,zipfile,collections
pd.set_option('display.width',250); pd.set_option('display.max_columns',40)
b=fsspec.open("https://zenodo.org/records/15258978/files/KeyResourceTable_ICD.xlsx?download=1").open().read()
x=pd.read_excel(io.BytesIO(b),sheet_name=None,header=None)
for s,d in x.items(): print(s,d.shape); print(d.to_string(max_colwidth=50)[:3000])
for zn in ["Data_ICD_A77636OpenField_Raw.zip","Data_ICD_Fig5_DREADDLocomotion_Raw.zip"]:
    z=zipfile.ZipFile(fsspec.open("https://zenodo.org/records/15258978/files/"+zn+"?download=1",block_size=2**20).open())
    n=[q for q in z.namelist() if not q.startswith('__') and 'DS_Store' not in q]
    print(zn,len(n)); print(n[:40])
EOF
```

```
ICD_KRT (49, 6)
                                            0                                                  1                                        2                                                  3          4                                                  5
0                               RESOURCE TYPE                                      RESOURCE NAME                                   SOURCE                                         IDENTIFIER  NEW/REUSE                             ADDITIONAL INFORMATION
1                                     Dataset  cognitive behavioral and image quantification ...                                   Zenodo                    doi.org/10.5281/zenodo.15258978        New  Raw tubular data used to produce Figures1-3, 5, 6
2                                     Dataset                    In vivo Electrophysioloogy data                            DANDI Archive           https://dandiarchive.org/dandiset/001177        New          Raw tubular data used to produce Figure 4
3                               Software/code      Arduino code for running cognitive assessment                                   Zenodo                       DOI: 10.5281/zenodo.10703132        New                                                NaN
4                               Software/code      Python code for cognitive assessment analysis                                   Zenodo                       DOI: 10.5281/zenodo.10703140        New                                                NaN
5                               Software/code                                           Igor Pro                              Wavemetrics  http://www.wavemetrics.com/products/igorpro/ i...      Reuse                                                NaN
6                               Software/code                                      MATLAB R2020b                                MathWorks  https://www.mathworks.com/products/matlab.html...      Reuse                            
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/001177-zhuang-2025; cd $TMPDIR; python3 - <<'EOF'
import zipfile,re,collections
for zn in ['Data_ICD_PPX.zip','Data_ICD_A77636.zip','Data_ICD_DREADD.zip']:
    z=zipfile.ZipFile(zn)
    n=[x.split('/')[-1] for x in z.namelist() if x.upper().endswith('.CSV') and not x.startswith('__') and '_delay' in x]
    bad=[x for x in n if not re.match(r'^(.+?)_delay(?: discounting)?(?:_(.*))?_(\d{6})\.CSV$',x,re.I)]
    print(zn,len(n),'unparsed',bad[:20])
    ids=collections.Counter(re.match(r'^(.+?)_',x).group(1) for x in n); print(sorted(ids))
EOF
```

```
Data_ICD_PPX.zip 429 unparsed ['D4.1_delay_03092.CSV', 'E6.2_delay_PPXwashout_0830122.CSV']
['C1.1', 'C2', 'C3.1', 'C9', 'D2', 'D2.1', 'D2.2', 'D3', 'D4', 'D4.1', 'D4.2', 'D6', 'E1', 'E3.3', 'E4', 'E6', 'E6.2', 'E7', 'E9', 'F1.1', 'F4', 'F5', 'F7', 'H0', 'H0.4', 'H1.4', 'H2', 'H2.1', 'H2.2', 'H3', 'H4', 'H4.1', 'H5.1', 'H5.2', 'J1', 'J3.1', 'N0', 'N1', 'N4', 'N5', 'N5.1', 'P1', 'P2', 'P4', 'P5', 'P6', 'P7']
Data_ICD_A77636.zip 251 unparsed []
['O0', 'O0.1', 'O0.6', 'O2', 'O3', 'O3.6', 'O4.1', 'R0.1', 'R0.2', 'R1.1', 'R1.2', 'R1.3', 'R1.5', 'R17', 'R2.2', 'R3', 'R3.1', 'R3.3', 'R4', 'R4.1', 'R4.3', 'R4.4', 'R5', 'R5.1', 'R6.1', 'R7.3']
Data_ICD_DREADD.zip 270 unparsed ['H2.1_delay_061423CSV.CSV']
['F1', 'F5', 'F5.1', 'F7', 'H0', 'H0.4', 'H1', 'H1.2', 'H1.4', 'H2', 'H2.1', 'H2.2', 'H3', 'H4.1', 'H4.2', 'H5.1', 'H5.2', 'H7', 'J3', 'J5.1', 'J6', 'O1', 'O4.1', 'O7.1', 'O8.1', 'R0.4', 'R1', 'R1.4', 'R17', 'R2', 'R2.2', 'R2.4', 'R4', 'R5', 'R5.2', 'R5.3', 'R6', 'R7.2']
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/001177-zhuang-2025/icd.py",
 "content": "\"\"\"Loading and measures for Zhuang, Lemak, Sridhar & Nelson (2025), Brain, doi:10.1093/brain/awaf312.\n\nTwo sources are read, both streamed and held in memory, never written to disk:\n\n- DANDI:001177 at version 0.250902.2127, the in vivo electrophysiology (Figure 4, 6F-K, S5, S8).\n  Only metadata, array shapes and the two `units` tables are read; the claims on these data are\n  blocked (see the notebook), so no voltage is streamed.\n- Zenodo record 15258978 (doi:10.5281/zenodo.15258978), the paper's deposit of its behaviour,\n  histology and slice data. The claims file names it as the data of every `data: elsewhere` claim.\n\nWhere each parameter comes from:\n\n- Delay discounting events. The block and event names follow the paper's analysis code,\n  UCSF-Nelson-Lab/ICD-Cognitive-Analysis at commit 5528e222 (delay_discounting_task.py,\n  processCsv_1): the free choice blocks are B3, B6, B9 and B12, events are counted only inside\n  them, \"l reward delivery\" and \"s reward delivery\" mark delayed/large and immediate/small\n  choices, \"center omi\" and \"side omi\" omissions. The delays of these blocks, 0, 3, 6 and 9 s,\n  are from the Supplementary methods (\"Operant Training and Assessment\": the delay \"increased\n  across a session (between blocks) from 0 s (block 1) to 3 s (block 2), to 6 s (block 3) to 9 s\n  (block 4)\").\n- Choice measure. \"the percentage of free choice trials (excluding omissions) on which mice chose\n  the delayed/large reward\" (Supplementary methods, Experimental design, Behavior).\n- Choice latency. \"the interval between the illumination of the nosepoke (side) cue light and a\n  nosepoke (side) response, excluding side omissions\" (same passage). The code marks the side cue\n  light by \"cen tri\" and the response by the first \"np_B in\" or \"np_D in\" after it.\n- Hyperbolic fit. V = A/(1 + K D) fitted by least squares from A = 1, K = 0.5 without bounds, on\n  the fraction of delayed/large choices, and AUC the trapezoidal integral of the fitted values at\n  D = 0, 3, 6, 9 s, as Summary_Cognitive.m does (claims file, fig1ijk-ppx-a-k-auc).\n- Stability rule for baseline reading (b). \"CV < 20% in at least 3 blocks for three consecutive\n  sessions, or CV < 20% in each block for two consecutive sessions\" (Supplementary methods,\n  Behavior). Which stable run is used, when there are several, is not stated; the last one before\n  the first drug session is taken (an assumption, stated in the notebook).\n- Groups. The control and parkinsonian, mCherry, hM4Di and hM3Dq mouse lists are those of the\n  deposit's README_ICD_CognitiveAssessment.txt, parsed at run time.\n- Two-way \"repeated measures\" ANOVA. The degrees of freedom the paper prints (F(1, 60) for 16\n  control mice, F(1, 120) for 31 parkinsonian mice, F(1, 44) for 12 DREADD mice) are those of a\n  split-plot design in which each mouse and delay pair is the unit measured under both\n  treatments, with delay between units: error df = (mice x 4 - 4) x (treatments - 1). This is the\n  layout `split_plot_anova` computes. The per-delay Bonferroni comparisons use the pooled\n  within-unit error of that ANOVA, as GraphPad Prism does, and multiply p by the number of delays.\n  A paired t test per delay, Bonferroni corrected, is the variant.\n- Between-group two-way ANOVA (Figure 1F-G baseline, F(1, 180) for 47 mice): ordinary two-way\n  ANOVA on group and delay with every mouse and delay value an observation, type III sums of\n  squares; per-delay Bonferroni comparisons use the pooled error.\n- Friedman with Dunn's comparisons, \"between baseline and PPX ON or OFF conditions\"\n  (Supplementary methods, Behavior): Dunn's z on mean ranks, Bonferroni over the two comparisons\n  with baseline.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport json\nimport re\nimport urllib.parse\nimport urllib.request\nimport zipfile\nfrom functools import lru_cache\n\nimport fsspec\nimport numpy as np\nimport pandas as pd\nfrom scipy import optimize, stats\n\nDANDISET = \"001177\"\nDANDI_VERSION = \"0.250902.2127\"\nZENODO_RECORD = \"15258978\"\nZENODO_DOI = \"10.5281/zenodo.15258978\"\nCODE_REPO = \"https://github.com/UCSF-Nelson-Lab/ICD-Cognitive-Analysis\"\nCODE_COMMIT = \"5528e2229f186e0785a676ae6f15219c47146930\"\n\nDELAYS = [0, 3, 6, 9]\nFREE_BLOCKS = {\"B3\": 0, \"B6\": 3, \"B9\": 6, \"B12\": 9}\nCOGNITIVE_ZIP = \"Data_ICD_Fig1&2&5&6_CognitiveAssay.zip\"\n\n\n# ---------------------------------------------------------------- DANDI\n\ndef dandi_assets() -> pd.DataFrame:\n    url = (f\"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{DANDI_VERSION}\"\n           \"/assets/?page_size=200\")\n    rows = json.load(urllib.request.urlopen(url))[\"results\"]\n    return pd.DataFrame([{\"path\": r[\"path\"], \"asset_id\": r[\"asset_id\"], \"size_gb\": r[\"size\"] / 1e9}\n                         for r in rows]).sort_values(\"path\").reset_index(drop=True)\n\n\ndef dandi_metadata() -> dict:\n    url = f\"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{DANDI_VERSION}/\"\n    return json.load(urllib.request.urlopen(url))\n\n\ndef open_nwb(asset_id: str):\n    import h5py\n    import remfile\n    return h5py.File(remfile.File(f\"https://api.dandiarchive.org/api/assets/{asset_id}/download/\"), \"r\")\n\n\ndef survey_file(asset_id: str) -> dict:\n    \"\"\"What one NWB file holds, from its metadata and array shapes only.\"\"\"\n    f = open_nwb(asset_id)\n    text = lambda p: f[p][()].decode(\"utf-8\", \"replace\") if p in f else None\n    acq = f[\"acquisition\"]\n    series = [k for k in acq if k.startswith(\"ElectricalSeries\")]\n    spike_events = [k for k in acq if k.startswith(\"SpikeEvents\")]\n    segments = [(float(acq[k][\"starting_time\"][()]) / 60, acq[k][\"data\"].shape[0] / 30000 / 60)\n                for k in series]\n    out = {\n        \"subject\": text(\"general/subject/subject_id\"),\n        \"genotype\": text(\"general/subject/genotype\"),\n        \"sex\": text(\"general/subject/sex\"),\n        \"lesion\": (\"6-OHDA\" if \"6-OHDA\" in (text(\"general/subject/description\") or \"\")\n                   else \"saline\" if \"saline\" in (text(\"general/subject/description\") or \"\") else \"?\"),\n        \"description_start\": (text(\"general/subject/description\") or \"\")[:40],\n        \"session_id\": text(\"general/session_id\"),\n        \"start\": text(\"session_start_time\"),\n        \"n_segments\": len(series),\n        \"segments_min\": \"; \".join(f\"{s:.1f}+{d:.1f}\" for s, d in segments),\n        \"n_channels\": acq[series[0]][\"data\"].shape[1] if series else 0,\n        \"n_spike_event_series\": len(spike_events),\n        \"n_threshold_crossings\": int(sum(acq[k][\"timestamps\"].shape[0] for k in spike_events)),\n        \"has_units\": \"units\" in f,\n        \"units_columns\": \",\".join(f[\"units\"].attrs[\"colnames\"]) if \"units\" in f else \"\",\n        \"n_units\": f[\"units\"][\"id\"].shape[0] if \"units\" in f else 0,\n        \"intervals\": \",\".join(f[\"intervals\"].keys()) if \"intervals\" in f else \"\",\n        \"stimulus\": \",\".join(f[\"stimulus/presentation\"].keys()),\n        \"ogen\": \"ogen_sites\" in f[\"general\"] or \"optogenetics\" in f[\"general\"],\n        \"processing\": \",\".join(f\"{m}/{k}\" for m in f[\"processing\"] for k in f[\"processing\"][m]),\n        \"behavior_in_file\": any(\"behavior\" in m.lower() for m in f[\"processing\"]),\n    }\n    if out[\"has_units\"]:\n        idx = f[\"units\"][\"spike_times_index\"][:]\n        out[\"unit_spike_counts\"] = np.diff(np.r_[0, idx]).tolist()\n    return out\n\n\n# ---------------------------------------------------------------- Zenodo\n\ndef zenodo_files() -> pd.DataFrame:\n    d = json.load(urllib.request.urlopen(f\"https://zenodo.org/api/records/{ZENODO_RECORD}\"))\n    return pd.DataFrame([{\"key\": f[\"key\"], \"size_mb\": f[\"size\"] / 1e6, \"checksum\": f[\"checksum\"]}\n                         for f in d[\"files\"]])\n\n\ndef zenodo_url(name: str) -> str:\n    return f\"https://zenodo.org/records/{ZENODO_RECORD}/files/{urllib.parse.quote(name)}?download=1\"\n\n\n@lru_cache(maxsize=None)\ndef zenodo_bytes(name: str) -> bytes:\n    with fsspec.open(zenodo_url(name), block_size=2**22) as fh:\n        return fh.read()\n\n\ndef read_excel(name: str, **kw) -> dict:\n    return pd.read_excel(io.BytesIO(zenodo_bytes(name)), sheet_name=None, header=None, **kw)\n\n\n@lru_cache(maxsize=None)\ndef readme_groups() -> dict:\n    \"\"\"Mouse lists per experiment and group, from README_ICD_CognitiveAssessment.txt.\"\"\"\n    text = zenodo_bytes(\"README_ICD_CognitiveAssessment.txt\").decode(\"utf-8\", \"replace\")\n    groups, experiment = {}, None\n    for line in text.splitlines():\n        line = line.strip()\n        if line.endswith(\"related experiments\"):\n            experiment = line.split(\"-\")[0].strip()\n        m = re.match(r\"^(Control|Parkinsonian|mCherry|Inhibitory DREADD \\(hM4Di\\)|\"\n                     r\"Excitatory DREADD \\(hM3Dq\\)):\\s*(.*)$\", line)\n        if m and experiment:\n            name = {\"Control\": \"control\", \"Parkinsonian\": \"parkinsonian\", \"mCherry\": \"mCherry\",\n                    \"Inhibitory DREADD (hM4Di)\": \"hM4Di\",\n                    \"Excitatory DREADD (hM3Dq)\": \"hM3Dq\"}[m.group(1)]\n            groups[(experiment, name)] = m.group(2)\n    # lists may continue on the next line\n    out = {}\n    lines = text.splitlines()\n    for (experiment, name), first in groups.items():\n        out[(experiment, name)] = [x.strip() for x in first.split(\",\") if x.strip()]\n    for i, line in enumerate(lines):\n        if line.strip() and \",\" in line and \":\" not in line and i > 0:\n            prev = next(l for l in reversed(lines[:i]) if \":\" in l)\n            for key, ids in out.items():\n                if prev.strip().startswith({\"control\": \"Control\", \"parkinsonian\": \"Parkinsonian\"}.get(key[1], \"@\")) \\\n                        and ids and ids[-1] and ids[-1] in prev:\n                    out[key] = ids + [x.strip() for x in line.split(\",\") if x.strip()]\n    return out\n\n\n@lru_cache(maxsize=None)\ndef cognitive_archives() -> dict:\n    \"\"\"The three inner zips of the cognitive assay deposit, opened in memory.\"\"\"\n    outer = zipfile.ZipFile(io.BytesIO(zenodo_bytes(COGNITIVE_ZIP)))\n    out = {}\n    for name in outer.namelist():\n        if name.endswith(\".zip\") and not name.startswith(\"__MACOSX\"):\n            key = name.split(\"/\")[-1].replace(\"Data_ICD_\", \"\").replace(\".zip\", \"\")\n            out[key] = zipfile.ZipFile(io.BytesIO(outer.read(name)))\n    return out\n\n\nDELAY_FILE = re.compile(r\"^(?P<mouse>[^_]+)_delay(?: discounting)?(?:_(?P<cond>[^_]*?))?_(?P<date>[^_]+)\\.CSV$\",\n                        re.IGNORECASE)\n\n\ndef condition_of(tag: str | None) -> str | None:\n    tag = (tag or \"\").replace(\" \", \"\").lower()\n    if tag == \"\":\n        return \"baseline\"\n    if \"washout\" in tag or \"washont\" in tag:\n        return \"off\"\n    if tag in (\"ppx\", \"a77636\", \"cno\"):\n        return \"on\"\n    return None\n\n\ndef _ms(t: str) -> float:\n    h, m, s, ms = (int(x) for x in t.strip().split(\":\"))\n    return ((h * 60 + m) * 60 + s) * 1000 + ms\n\n\ndef parse_session(text: str) -> dict:\n    \"\"\"Per free choice block: choices, omissions and choice latencies (ms), and the session date.\"\"\"\n    blocks = {d: {\"large\": 0, \"small\": 0, \"center_om\": 0, \"side_om\": 0, \"trials\": 0,\n                  \"lat_large\": [], \"lat_small\": []} for d in DELAYS}\n    current = None\n    cue_time = None\n    first_side = None\n    date = None\n    for line in text.splitlines()[1:]:\n        parts = [p.strip().strip('\"') for p in line.split(\",\")]\n        if len(parts) < 3:\n            continue\n        stamp, event, t = parts[0], parts[1], parts[2]\n        if date is None and stamp:\n            date = stamp.split(\" \")[0]\n        b = re.fullmatch(r\"B(\\d+)_?\", event)\n        if b:\n            current = FREE_BLOCKS.get(\"B\" + b.group(1))\n            continue\n        if current is None:\n            continue\n        blk = blocks[current]\n        if event == \"trial start\":\n            blk[\"trials\"] += 1\n            cue_time, first_side = None, None\n        elif event == \"cen tri\":\n            cue_time, first_side = _ms(t), None\n        elif event in (\"np_B in\", \"np_D in\") and cue_time is not None and first_side is None:\n            first_side = _ms(t) - cue_time\n        elif event == \"l reward delivery\":\n            blk[\"large\"] += 1\n            if first_side is not None:\n                blk[\"lat_large\"].append(first_side)\n        elif event == \"s reward delivery\":\n            blk[\"small\"] += 1\n            if first_side is not None:\n                blk[\"lat_small\"].append(first_side)\n        elif event == \"center omi\":\n            blk[\"center_om\"] += 1\n        elif event == \"side omi\":\n            blk[\"side_om\"] += 1\n    return {\"date\": pd.to_datetime(date, format=\"%Y/%m/%d\") if date else pd.NaT, \"blocks\": blocks}\n\n\n@lru_cache(maxsize=None)\ndef sessions() -> pd.DataFrame:\n    \"\"\"One row per delay discounting session and free choice block, for the three experiments.\"\"\"\n    groups = readme_groups()\n    rows, skipped = [], []\n    for experiment, zf in cognitive_archives().items():\n        exp = {\"PPX\": \"PPX\", \"A77636\": \"A77636\", \"DREADD\": \"DREADD\"}[experiment]\n        for name in zf.namelist():\n            base = name.split(\"/\")[-1]\n            if name.startswith(\"__MACOSX\") or \"_delay\" not in base:\n                continue\n            m = DELAY_FILE.match(base.replace(\"CSV.CSV\", \".CSV\"))\n            if not m:\n                skipped.append((experiment, base, \"name\"))\n                continue\n            cond = condition_of(m.group(\"cond\"))\n            if cond is None:\n                skipped.append((experiment, base, \"condition\"))\n                continue\n            mouse = m.group(\"mouse\")\n            group = [g for (e, g), ids in groups.items() if e == exp and mouse in ids]\n            s = parse_session(zf.read(name).decode(\"latin-1\"))\n            for d, blk in s[\"blocks\"].items():\n                rows.append({\"experiment\": exp, \"mouse\": mouse, \"group\": group[0] if group else None,\n                             \"file\": base, \"condition\": cond, \"date\": s[\"date\"], \"delay\": d,\n                             \"large\": blk[\"large\"], \"small\": blk[\"small\"],\n                             \"center_om\": blk[\"center_om\"], \"side_om\": blk[\"side_om\"],\n                             \"trials\": blk[\"trials\"],\n                             \"lat_large\": np.mean(blk[\"lat_large\"]) / 1000 if blk[\"lat_large\"] else np.nan,\n                             \"lat_small\": np.mean(blk[\"lat_small\"]) / 1000 if blk[\"lat_small\"] else np.nan,\n                             \"lat_all\": (np.mean(blk[\"lat_large\"] + blk[\"lat_small\"]) / 1000\n                                         if blk[\"lat_large\"] + blk[\"lat_small\"] else np.nan)})\n    df = pd.DataFrame(rows)\n    chosen = df[\"large\"] + df[\"small\"]\n    df[\"pct_large\"] = np.where(chosen > 0, 100 * df[\"large\"] / chosen.where(chosen > 0, 1), np.nan)\n    df[\"pct_center_om\"] = 100 * df[\"center_om\"] / df[\"trials\"].where(df[\"trials\"] > 0)\n    df[\"pct_side_om\"] = 100 * df[\"side_om\"] / df[\"trials\"].where(df[\"trials\"] > 0)\n    df.attrs[\"skipped\"] = skipped\n    return df\n\n\ndef wide(df: pd.DataFrame, value: str = \"pct_large\") -> pd.DataFrame:\n    \"\"\"Sessions by delay: one row per session file.\"\"\"\n    return df.pivot_table(index=[\"experiment\", \"group\", \"mouse\", \"condition\", \"date\", \"file\"],\n                          columns=\"delay\", values=value, aggfunc=\"first\").reset_index()\n\n\ndef stable_window(base: pd.DataFrame) -> list:\n    \"\"\"The files of the last stable run of baseline sessions (reader's rule, see module docstring).\n\n    `base` is one mouse's baseline sessions in `wide` form, ordered by date. Returns [] when no run\n    meets the rule.\"\"\"\n    base = base.sort_values(\"date\")\n    vals = base[DELAYS].to_numpy(float)\n    files = base[\"file\"].tolist()\n    found = []\n    for i in range(len(files)):\n        for n, need in ((3, 3), (2, 4)):\n            if i + n <= len(files):\n                w = vals[i:i + n]\n                mean = np.nanmean(w, axis=0)\n                cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)\n                if np.sum(cv < 20) >= need:\n                    found.append(files[i:i + n])\n    return found[-1] if found else []\n\n\n# ---------------------------------------------------------------- fits\n\ndef hyperbolic(d, a, k):\n    return a / (1 + k * d)\n\n\ndef fit_curve(values) -> tuple:\n    \"\"\"A, K and AUC of V = A/(1 + K D) on fractions at D = 0, 3, 6, 9 s; NaN when the fit fails.\"\"\"\n    y = np.asarray(values, float)\n    if np.isnan(y).any():\n        return np.nan, np.nan, np.nan\n    try:\n        (a, k), _ = optimize.curve_fit(hyperbolic, np.array(DELAYS, float), y, p0=[1, 0.5],\n                                       maxfev=1000)\n    except (RuntimeError, optimize.OptimizeWarning):\n        return np.nan, np.nan, np.nan\n    pred = hyperbolic(np.array(DELAYS, float), a, k)\n    return a, k, np.trapezoid(pred, DELAYS)\n\n\n# ---------------------------------------------------------------- statistics\n\ndef split_plot_anova(data: pd.DataFrame, value: str, treat: str, levels: list) -> dict:\n    \"\"\"Two-way ANOVA with delay between units and treatment within units (unit = mouse x delay).\n\n    `data` has columns mouse, delay, `treat` and `value`; units missing a level are dropped.\n    Returns the treatment, delay and interaction F tests and Bonferroni per-delay comparisons of\n    each level against the first.\"\"\"\n    piv = data.pivot_table(index=[\"mouse\", \"delay\"], columns=treat, values=value)[levels].dropna()\n    y = piv.to_numpy(float)\n    delays = piv.index.get_level_values(\"delay\").to_numpy()\n    k = len(levels)\n    n_units = len(piv)\n    grand = y.mean()\n    unit_mean = y.mean(axis=1)\n    lev_mean = y.mean(axis=0)\n    d_levels = sorted(set(delays))\n    ss_t = n_units * np.sum((lev_mean - grand) ** 2)\n    ss_d = ss_dt = ss_err_b = ss_err_w = 0.0\n    for d in d_levels:\n        sel = delays == d\n        yd = y[sel]\n        nd = sel.sum()\n        md = yd.mean()\n        mdt = yd.mean(axis=0)\n        ss_d += nd * k * (md - grand) ** 2\n        ss_dt += nd * np.sum((mdt - md - lev_mean + grand) ** 2)\n        ss_err_b += k * np.sum((yd.mean(axis=1) - md) ** 2)\n        ss_err_w += np.sum((yd - yd.mean(axis=1, keepdims=True) - mdt + md) ** 2)\n    df_t, df_d = k - 1, len(d_levels) - 1\n    df_dt = df_t * df_d\n    df_eb = n_units - len(d_levels)\n    df_ew = df_eb * (k - 1)\n    ms_ew = ss_err_w / df_ew\n    out = {\"n_mice\": piv.index.get_level_values(\"mouse\").nunique(), \"n_units\": n_units,\n           \"treat_F\": (ss_t / df_t) / ms_ew, \"treat_df\": (df_t, df_ew),\n           \"delay_F\": (ss_d / df_d) / (ss_err_b / df_eb), \"delay_df\": (df_d, df_eb),\n           \"inter_F\": (ss_dt / df_dt) / ms_ew, \"inter_df\": (df_dt, df_ew)}\n    out[\"treat_p\"] = stats.f.sf(out[\"treat_F\"], df_t, df_ew)\n    out[\"delay_p\"] = stats.f.sf(out[\"delay_F\"], df_d, df_eb)\n    out[\"inter_p\"] = stats.f.sf(out[\"inter_F\"], df_dt, df_ew)\n    comps = []\n    n_comp = len(d_levels) * (k - 1)\n    for d in d_levels:\n        yd = y[delays == d]\n        for j in range(1, k):\n            diff = yd[:, j] - yd[:, 0]\n            t_pool = diff.mean() / np.sqrt(2 * ms_ew / len(diff))\n            p_pool = min(1.0, 2 * stats.t.sf(abs(t_pool), df_ew) * n_comp)\n            t_pair, p_pair = stats.ttest_rel(yd[:, j], yd[:, 0])\n            comps.append({\"delay\": d, \"level\": levels[j], \"n\": len(diff),\n                          \"mean_\" + str(levels[0]): yd[:, 0].mean(), \"mean_level\": yd[:, j].mean(),\n                          \"diff\": diff.mean(), \"p_bonf_pooled\": p_pool,\n                          \"p_bonf_paired\": min(1.0, p_pair * n_comp)})\n    out[\"per_delay\"] = pd.DataFrame(comps)\n    return out\n\n\ndef between_anova(data: pd.DataFrame, value: str, factor: str) -> dict:\n    \"\"\"Ordinary two-way ANOVA of `value` on `factor` and delay (type III), with per-delay\n    Bonferroni comparisons of the two factor levels on the pooled error.\"\"\"\n    import statsmodels.formula.api as smf\n    from statsmodels.stats.anova import anova_lm\n    d = data.dropna(subset=[value]).copy()\n    model = smf.ols(f\"{value} ~ C({factor}, Sum) * C(delay, Sum)\", data=d).fit()\n    table = anova_lm(model, typ=3)\n    mse, df_e = model.mse_resid, model.df_resid\n    levels = sorted(d[factor].unique())\n    comps = []\n    for dl in DELAYS:\n        a = d[(d.delay == dl) & (d[factor] == levels[0])][value]\n        b = d[(d.delay == dl) & (d[factor] == levels[1])][value]\n        t = (b.mean() - a.mean()) / np.sqrt(mse * (1 / len(a) + 1 / len(b)))\n        comps.append({\"delay\": dl, levels[0]: a.mean(), levels[1]: b.mean(), \"n0\": len(a), \"n1\": len(b),\n                      \"p_bonf\": min(1.0, 2 * stats.t.sf(abs(t), df_e) * len(DELAYS))})\n    row = lambda name: table.loc[[i for i in table.index if name in i and \":\" not in i][0]]\n    inter = table.loc[[i for i in table.index if \":\" in i][0]]\n    return {\"factor_F\": row(f\"C({factor}\")[\"F\"], \"factor_p\": row(f\"C({factor}\")[\"PR(>F)\"],\n            \"delay_F\": row(\"C(delay\")[\"F\"], \"delay_p\": row(\"C(delay\")[\"PR(>F)\"],\n            \"inter_F\": inter[\"F\"], \"inter_p\": inter[\"PR(>F)\"],\n            \"df\": (1, int(df_e)), \"delay_df\": (3, int(df_e)), \"per_delay\": pd.DataFrame(comps),\n            \"n_mice\": d.groupby(factor)[\"mouse\"].nunique().to_dict()}\n\n\ndef friedman_dunn(table: pd.DataFrame, reference: str) -> dict:\n    \"\"\"Friedman test over the columns of `table` (one row per mouse, complete rows only) and\n    Dunn's z for each column against `reference`, Bonferroni over those comparisons.\"\"\"\n    t = table.dropna()\n    chi2, p = stats.friedmanchisquare(*[t[c] for c in t.columns])\n    ranks = t.rank(axis=1)\n    k, n = t.shape[1], len(t)\n    se = np.sqrt(k * (k + 1) / (6 * n))\n    others = [c for c in t.columns if c != reference]\n    dunn = {}\n    for c in others:\n        z = (ranks[c].mean() - ranks[reference].mean()) / se\n        dunn[c] = {\"z\": z, \"p_bonf\": min(1.0, 2 * stats.norm.sf(abs(z)) * len(others)),\n                   \"median_ref\": t[reference].median(), \"median\": t[c].median()}\n    return {\"n\": n, \"chi2\": chi2, \"p\": p, \"dunn\": dunn}\n"
}
```

```
File created successfully at: entries/001177-zhuang-2025/icd.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; $TMPDIR/venv/w/bin/python - <<'EOF'
import re
s=open('icd.py').read()
start=s.index('@lru_cache(maxsize=None)\ndef readme_groups')
end=s.index('@lru_cache(maxsize=None)\ndef cognitive_archives')
new='''@lru_cache(maxsize=None)
def readme_groups() -> dict:
    """Mouse lists per experiment and group, from README_ICD_CognitiveAssessment.txt."""
    text = zenodo_bytes("README_ICD_CognitiveAssessment.txt").decode("utf-8", "replace")
    names = {"Control": "control", "Parkinsonian": "parkinsonian", "mCherry": "mCherry",
             "Inhibitory DREADD (hM4Di)": "hM4Di", "Excitatory DREADD (hM3Dq)": "hM3Dq"}
    groups, experiment, key = {}, None, None
    for line in text.splitlines():
        line = line.strip()
        if line.endswith("related experiments"):
            experiment, key = line.split("-")[0].strip(), None
            continue
        m = re.match(r"^(" + "|".join(re.escape(n) for n in names) + r"):\\s*(.*)$", line)
        if m and experiment:
            key = (experiment, names[m.group(1)])
            groups[key] = [x.strip() for x in m.group(2).split(",") if x.strip()]
        elif key and line and ":" not in line and "," in line:
            groups[key] += [x.strip() for x in line.split(",") if x.strip()]
        elif not line:
            key = None if key and groups.get(key) and not line else key
    return groups


'''
open('icd.py','w').write(s[:start]+new+s[end:])
EOF
cd entries/001177-zhuang-2025; time $TMPDIR/venv/w/bin/python -c "
import icd
g=icd.readme_groups()
for k,v in g.items(): print(k,len(v),v)
df=icd.sessions()
print(df.shape, df.attrs['skipped'])
print(df.groupby(['experiment','group','condition'])['file'].nunique())
print(df[df.group.isna()].groupby(['experiment','mouse']).file.nunique())
print(df.describe().T)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    df=icd.sessions()
  File "entries/001177-zhuang-2025/icd.py", line 278, in sessions
    s = parse_session(zf.read(name).decode("latin-1"))
  File "entries/001177-zhuang-2025/icd.py", line 254, in parse_session
    return {"date": pd.to_datetime(date, format="%Y/%m/%d") if date else pd.NaT, "blocks": blocks}
                    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/venv/w/lib/python3.13/site-packages/pandas/core/tools/datetimes.py", line 1273, in to_datetime
    result = convert_listlike(np.array([arg]), format)[0]
             ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/venv/w/lib/python3.13/site-packages/pandas/core/tools/datetimes.py", line 484, in _convert_listlike_datetimes
    return _array_strptime_with_fallback(arg, name, utc, format, exact, errors)
  File "/tmp/claude-1001/venv/w/lib/python3.13/site-packages/pandas/core/tools/datetimes.py", line 518, in _array_strptime_with_fallback
    result, tz_out = array_strptime(arg, fmt, exact=exact, errors=errors, utc=utc)
                     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pandas/_libs/tslibs/strptime.pyx", line 644, in pandas._libs.tslibs.strptime.array_strptime
  File "pandas/_libs/tslibs/strptime.pyx", line 561, in pandas._libs.tslibs.strptime.array_strptime
  File "pandas/_libs/tslibs/strptime.pyx", line 701, in pandas._libs.tslibs.strptime._parse_with_format
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; $TMPDIR/venv/w/bin/python - <<'EOF'
s=open('icd.py').read()
s=s.replace('''    return {"date": pd.to_datetime(date, format="%Y/%m/%d") if date else pd.NaT, "blocks": blocks}''','''    return {"date": pd.to_datetime(date, format="%Y/%m/%d", errors="coerce") if date else pd.NaT,
            "blocks": blocks}


def name_date(token: str):
    """The session date written in a file name as mmddyy; NaT when it is not six digits."""
    return pd.to_datetime(token, format="%m%d%y", errors="coerce") if re.fullmatch(r"\\d{6}", token) else pd.NaT''')
s=s.replace('''            s = parse_session(zf.read(name).decode("latin-1"))
''','''            s = parse_session(zf.read(name).decode("latin-1"))
            date = name_date(m.group("date"))
            date_from = "name"
            if pd.isna(date):
                date, date_from = s["date"], "log"
''')
s=s.replace('''"file": base, "condition": cond, "date": s["date"], "delay": d,''','''"file": base, "condition": cond, "date": date, "date_from": date_from,
                             "log_date": s["date"], "delay": d,''')
open('icd.py','w').write(s)
EOF
time $TMPDIR/venv/w/bin/python -c "
import icd,pandas as pd
pd.set_option('display.width',200)
df=icd.sessions()
print(df.shape, df.attrs['skipped'])
print(df.groupby(['experiment','group','condition'])['file'].nunique())
print(df[df.group.isna()].groupby(['experiment','mouse']).file.nunique())
print(df[df.date_from=='log'][['file','date','log_date']].drop_duplicates())
x=df.drop_duplicates('file'); print('name vs log date mismatch', (x.date!=x.log_date).sum(), len(x))
print(df[['large','small','center_om','side_om','trials','pct_large','lat_large','lat_small']].describe().T)
df.to_pickle('$TMPDIR/sess.pkl')
"
```

```
(3800, 20) []
experiment  group         condition
A77636      control       baseline      33
                          on            40
            parkinsonian  baseline      50
                          off           64
                          on            64
DREADD      hM3Dq         baseline      40
                          on            48
            hM4Di         baseline      41
                          on            43
            mCherry       baseline      43
                          on            55
PPX         control       baseline      49
                          on            60
            parkinsonian  baseline      98
                          off          105
                          on           117
Name: file, dtype: int64
Series([], Name: file, dtype: int64)
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python -c "
import pandas as pd
df=pd.read_pickle('sess.pkl')
print(df.trials.value_counts().sort_index())
x=df[df.trials!=20].groupby('file').trials.apply(list)
print(len(x)); print(x.head(30))
"
```

```
trials
0      164
7        2
15       1
20    3474
30     159
Name: count, dtype: int64
82
file
C1.1_delay discounting_080221.CSV        [30, 30, 30, 30]
C1.1_delay discounting_080321.CSV        [30, 30, 30, 30]
C1.1_delay discounting_080421.CSV        [30, 30, 30, 30]
C1.1_delay discounting_PPX_080621.CSV    [30, 30, 30, 30]
C1.1_delay discounting_PPX_081021.CSV    [30, 30, 30, 30]
C1.1_delay discounting_PPX_081321.CSV    [30, 30, 30, 30]
C1.1_delay discounting_PPX_081721.CSV    [30, 30, 30, 30]
C2_delay_080221.CSV                      [30, 30, 30, 30]
C2_delay_080321.CSV                      [30, 30, 30, 30]
C2_delay_080421.CSV                      [30, 30, 30, 30]
C2_delay_PPX_080621.CSV                  [30, 30, 30, 30]
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import zipfile,collections
z=zipfile.ZipFile('Data_ICD_PPX.zip')
for f in ['Data_ICD_PPX/C2_delay_080221.CSV']:
    t=z.read(f).decode('latin1').splitlines()
    c=collections.Counter(l.split(',')[1].strip() for l in t[1:] if ',' in l); print(c)
    ev=[l.split(',')[1].strip() for l in t[1:]]
    print([e for e in ev if e.startswith('B') or 'end' in e][:40])
    # print lines around first B3
    i=[k for k,l in enumerate(t) if ' B2' in l]; print(t[1:6]); print(t[i[0]-3:i[0]+25] if i else '')
EOF
$TMPDIR/venv/w/bin/python -c "
import pandas as pd
df=pd.read_pickle('$TMPDIR/sess.pkl')
x=df[df.trials==0].groupby('file').trials.apply(list); print(len(x)); print(x.head(10))
"
```

```
Counter({'Leak_on': 3967, 'Leak_off': 3967, 'np_C in': 826, 'np_C out': 826, 'trial start': 160, 'timeout': 160, 'cen tri': 150, 'np_D in': 142, 'np_D out': 142, 'np_B in': 137, 'np_B out': 137, 's reward delivery': 82, 'l reward delivery': 68, 'center omi': 10, 'B1_': 1, 'B2_': 1, 'B3_': 1, 'B4_': 1, 'B5_': 1, 'B6_': 1, 'B7_': 1, 'B8_': 1, 'B9_': 1, 'B10_': 1, 'B11_': 1, 'B12_': 1, 'session ends': 1})
['B1_', 'B2_', 'B3_', 'B4_', 'B5_', 'B6_', 'B7_', 'B8_', 'B9_', 'B10_', 'B11_', 'B12_', 'session ends']
['"2021/8/2 17:8:31", B1_, 00:00:00:822', '"2021/8/2 17:8:31", trial start, 00:00:00:833', '"2021/8/2 17:8:31", np_C in, 00:00:00:873', '"2021/8/2 17:8:31", cen tri, 00:00:00:885', '"2021/8/2 17:8:31", Leak_on, 00:00:00:900']
['"2021/8/2 17:13:3", np_C out, 00:04:31:938', '"2021/8/2 17:13:3", np_D in, 00:04:32:813', '"2021/8/2 17:13:3", np_D out, 00:04:32:858', '"2021/8/2 17:13:46", B2_, 00:05:15:844', '"2021/8/2 17:13:46", trial start, 00:05:15:857', '"2021/8/2 17:13:48", np_C in, 00:05:17:502', '"2021/8/2 17:13:48", cen tri, 00:05:17:514', '"2021/8/2 17:13:48", np_C out, 00:05:17:648', '"2021/8/2 17:13:49", np_B in, 00:05:18:28', '"2021/8/2 17:13:49", s reward delivery, 00:05:18:42', '"2021/8/2 17:13:49", np_B out, 00:05:18:106', '"2021/8/2 17:13:49", np_C in, 00:05:18:496', '"2021/8/2 17:13:49", Leak_on, 00:05:18:577', '"2021/8/2 17:13:49", Leak_off, 00:05:18:623', '"2021/8/2 17:13:49", Leak_on, 00:05:18:666', '"2021/8/2 17:13:49", Leak_off, 00:05:18:721', '"2021/8/2 17:13:49", np_C out, 00:05:18:734', '"2021/8/2 17:13:49", Leak_on, 00:05:18:812', '"2021/8/2 17:13:50", Leak_off, 00:05:18:861', '"2021/8/2 17:13:50", np_C in, 00:05:18:907', '"2021/8/2 17:13:50", Leak_on, 00:05:18:921', '"2021/8/2 17:13:50", Leak_off, 00:05:18:962', '"2021/8/2 17:13:50", Leak_on, 00:05:18:977', '"2021/8/2 17:13:50", np_C out, 00:05:18:989', '"2021/8/2 17:13:50", Leak_off, 00:05:19:03', '"2021/8/2 17:13:50", np_C in, 00:05:19:271', '"2021/8/2 17:13:50", np_C out, 00:05:19:331', '"202
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import zipfile,collections
z=zipfile.ZipFile('Data_ICD_PPX.zip')
def per_block(f):
    t=z.read(f).decode('latin1').splitlines()
    cur='pre'; c=collections.OrderedDict()
    for l in t[1:]:
        p=[x.strip().strip('"') for x in l.split(',')]
        if len(p)<3: continue
        e=p[1]
        if e.startswith('B') and e.endswith('_'): cur=e
        c.setdefault(cur,collections.Counter())
        if e in('trial start','l reward delivery','s reward delivery','center omi','side omi','cen tri'): c[cur][e]+=1
    return c
for f in ['Data_ICD_PPX/C2_delay_080221.CSV','Data_ICD_PPX/P1_delay_091320.CSV','Data_ICD_PPX/H4.1_delay_082423.CSV']:
    print(f)
    for k,v in per_block(f).items(): print('  ',k,dict(v))
t=z.read('Data_ICD_PPX/P1_delay_091320.CSV').decode('latin1').splitlines()
print(t[:30])
print(collections.Counter(l.split(',')[1].strip() for l in t[1:] if ',' in l))
EOF
```

```
Data_ICD_PPX/C2_delay_080221.CSV
   B1_ {'trial start': 5, 'cen tri': 4, 'l reward delivery': 4, 'center omi': 1}
   B2_ {'trial start': 5, 'cen tri': 3, 's reward delivery': 3, 'center omi': 2}
   B3_ {'trial start': 30, 'cen tri': 30, 's reward delivery': 5, 'l reward delivery': 25}
   B4_ {'trial start': 5, 'cen tri': 5, 'l reward delivery': 5}
   B5_ {'trial start': 5, 'cen tri': 5, 's reward delivery': 5}
   B6_ {'trial start': 30, 'cen tri': 28, 's reward delivery': 17, 'l reward delivery': 11, 'center omi': 2}
   B7_ {'trial start': 5, 'cen tri': 5, 'l reward delivery': 5}
   B8_ {'trial start': 5, 'cen tri': 5, 's reward delivery': 5}
   B9_ {'trial start': 30, 'cen tri': 27, 's reward delivery': 21, 'center omi': 3, 'l reward delivery': 6}
   B10_ {'trial start': 5, 'cen tri': 5, 'l reward delivery': 5}
   B11_ {'trial start': 5, 'cen tri': 5, 's reward delivery': 5}
   B12_ {'trial start': 30, 'cen tri': 28, 's reward delivery': 21, 'l reward delivery': 7, 'center omi': 2}
Data_ICD_PPX/P1_delay_091320.CSV
   pre {'trial start': 120, 'cen tri': 104, 'l reward delivery': 47, 'center omi': 16, 's reward delivery': 49, 'side omi': 8}
Data_ICD_PPX/H4.1_delay_082423.CSV
   B1_ {'trial start': 5, 'cen tri': 5, 'side omi': 1, 'l reward delivery': 4}
   B2_ {'trial start': 5, 'cen tri': 5, 's reward delivery': 5}
   B3_ {'trial start': 20, 'cen tri': 20, 'l reward delivery': 20}
   B4_ {'trial start': 5, 'cen tri': 5, 'l reward delivery': 5}
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; $TMPDIR/venv/w/bin/python - <<'EOF'
s=open('icd.py').read()
s=s.replace('''        b = re.fullmatch(r"B(\\d+)_?", event)
        if b:
            current = FREE_BLOCKS.get("B" + b.group(1))
            continue''','''        b = re.match(r"B(\\d+)_", event)
        if b:
            current = FREE_BLOCKS.get("B" + b.group(1))
            if current is not None:
                labels[current] = event
            continue''')
s=s.replace('''    current = None
    cue_time = None''','''    current = None
    labels = {}
    cue_time = None''')
s=s.replace('''"blocks": blocks}


def name_date''','''"blocks": blocks, "labels": labels}


def name_date''')
s=s.replace('''"trials": blk["trials"],
''','''"trials": blk["trials"], "block_label": s["labels"].get(d, ""),
''')
open('icd.py','w').write(s)
EOF
grep -n "labels" icd.py | head; cd entries/001177-zhuang-2025 && $TMPDIR/venv/w/bin/python -c "
import icd,pandas as pd
df=icd.sessions(); df.to_pickle('$TMPDIR/sess.pkl')
print(df.trials.value_counts().sort_index())
x=df.drop_duplicates('file')
print(df.groupby(['experiment','block_label']).file.nunique())
print(df[df.trials!=20].groupby(['experiment','mouse']).file.nunique())
"
```

```
218:    labels = {}
233:                labels[current] = event
258:            "blocks": blocks, "labels": labels}
298:                             "trials": blk["trials"], "block_label": s["labels"].get(d, ""),
trials
0       30
7        2
15       1
20    3608
30     159
Name: count, dtype: int64
experiment  block_label 
A77636      B12_            251
            B3_             251
            B6_             251
            B9_             251
DREADD      B12_            270
            B3_             270
            B6_             270
            B9_             270
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python -c "
import pandas as pd,zipfile,collections
df=pd.read_pickle('sess.pkl')
f=df[(df.delay==9)&(df.block_label=='')].file.unique(); print(len(f), f[:5])
z=zipfile.ZipFile('Data_ICD_PPX.zip')
t=z.read('Data_ICD_PPX/'+f[0]).decode('latin1').splitlines()
print([l.split(',')[1] for l in t[1:] if ',' in l and l.split(',')[1].strip().startswith('B')])
print(df[df.trials==0][['file','delay','block_label']].head(10))
"
```

```
30 <StringArray>
['P2_delay_PPX_102620.CSV', 'P2_delay_PPX_102020.CSV',
 'P7_delay_PPX_102020.CSV',     'P7_delay_101320.CSV',
 'P7_delay_PPX_102220.CSV']
Length: 5, dtype: str
[' B1_forced imme', ' B2_forced del_0s', ' B3_free_0s', ' B4_forced imme', ' B5_forced del_6s', ' B6_free_6s', ' B7_forced imme', ' B8_forced del_12s', ' B9_free_12s']
                        file  delay block_label
23   P2_delay_PPX_102620.CSV      9            
227  P2_delay_PPX_102020.CSV      9            
287  P7_delay_PPX_102020.CSV      9            
311      P7_delay_101320.CSV      9            
375  P7_delay_PPX_102220.CSV      9            
463  P2_delay_PPX_102220.CSV      9            
651      P7_delay_101420.CSV      9            
755  P2_delay_PPX_102320.CSV      9            
767      P7_delay_100920.CSV      9            
843  P4_delay_PPX_100920.CSV      9
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u
```

```
Wed Oct 28 10:45:18 UTC 2026
```

**Agent**

More time than I estimated: it is 10:45 UTC. Now prototyping the delay discounting analyses on the parsed table.

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; cat > $TMPDIR/dd.py <<'EOF'
import sys; sys.path.insert(0,'.')
import icd, pandas as pd, numpy as np
pd.set_option('display.width',220); pd.set_option('display.max_columns',30)
df=pd.read_pickle(sys.argv[1] if len(sys.argv)>1 else '/tmp/claude-1001/sess.pkl')
W=icd.wide(df)
D=icd.DELAYS
def per_mouse(exp, group, cond, reading):
    w=W[(W.experiment==exp)&(W.group==group)&(W.condition==cond)].sort_values('date')
    out={}
    for m,g in w.groupby('mouse'):
        if reading=='all': sel=g
        elif reading=='first': sel=g.head(1)
        elif reading=='four': sel=g.head(4)
        elif reading=='fourth': sel=g.iloc[3:4]
        elif reading=='stable':
            first_drug=W[(W.experiment==exp)&(W.mouse==m)&(W.condition!='baseline')].date.min()
            b=g[g.date<first_drug] if pd.notna(first_drug) else g
            f=icd.stable_window(b); sel=g[g.file.isin(f)]
        if len(sel): out[m]=sel[D].mean()
    return pd.DataFrame(out).T
def long(tab, **kw):
    t=tab.copy(); t.index.name='mouse'; l=t.reset_index().melt(id_vars='mouse',var_name='delay',value_name='v')
    for k,v in kw.items(): l[k]=v
    return l
for exp,groups in [('PPX',['control','parkinsonian'])]:
    for r in ['all','stable']:
        b={g:per_mouse(exp,g,'baseline',r) for g in groups}
        print(r,{g:len(v) for g,v in b.items()})
        L=pd.concat([long(b[g],grp=g) for g in groups])
        res=icd.between_anova(L,'v','grp')
        print({k:v for k,v in res.items() if k!='per_delay'}); print(res['per_delay'])
    for g in groups:
        for rb in ['all','stable']:
            for rp in ['first','four']:
                base=per_mouse(exp,g,'baseline',rb); on=per_mouse(exp,g,'on',rp)
                L=pd.concat([long(base,t='base'),long(on,t='on')])
                res=icd.split_plot_anova(L,'v','t',['base','on'])
                print(g,rb,rp,res['n_mice'],'F%.3f df%s p%.4g'%(res['treat_F'],res['treat_df'],res['treat_p']))
                print(res['per_delay'][['delay','n','mean_base','mean_level','p_bonf_pooled','p_bonf_paired']].round(4).to_string())
EOF
$TMPDIR/venv/w/bin/python $TMPDIR/dd.py 2>&1 | tail -80
```

```
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
entries/001177-zhuang-2025/icd.py:332: RuntimeWarning: invalid value encountered in divide
  cv = np.where(mean > 0, np.nanstd(w, axis=0, ddof=1) / mean * 100, np.inf)
all {'control': 16, 'parkinsonian': 31}
{'factor_F': np.float64(0.007103051737053012), 'factor_p': np.float64(0.9329288400203708), 'delay_F': np.float64(38.15286443758067), 'delay_p': np.float64(4.3313170031400966e-19), 'inter_F': np.float64(0.23712946683673794), 'inter_p': np.float64(0.870387389526989), 'df': (1, 178), 'delay_df': (3, 178), 'n_mice': {'control': 16, 'parkinsonian': 31}}
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; $TMPDIR/venv/w/bin/python -W ignore -c "
import pandas as pd, icd
df=pd.read_pickle('$TMPDIR/sess.pkl'); W=icd.wide(df)
c=W.groupby(['experiment','group','mouse','condition']).file.count().unstack()
pd.set_option('display.max_rows',200); print(c.to_string())
print(W[W.mouse.isin(['D4.1'])].sort_values('date')[['file','condition','date',0,3,6,9]])
"
```

```
condition                      baseline  off   on
experiment group        mouse                    
A77636     control      O0          3.0  NaN  4.0
                        O0.6        3.0  NaN  4.0
                        O2          4.0  NaN  4.0
                        O3          4.0  NaN  4.0
                        O3.6        2.0  NaN  4.0
                        R0.1        3.0  NaN  4.0
                        R4.3        4.0  NaN  4.0
                        R4.4        4.0  NaN  4.0
                        R5.1        3.0  NaN  4.0
                        R7.3        3.0  NaN  4.0
           parkinsonian O0.1        4.0  4.0  4.0
                        O4.1        3.0  4.0  4.0
                        R0.2        3.0  4.0  4.0
                        R1.1        3.0  4.0  4.0
                        R1.2        3.0  4.0  4.0
                        R1.3        3.0  4.0  4.0
                        R1.5        3.0  4.0  4.0
                        R17         3.0  4.0  4.0
[... 106 more lines not kept]
```

**Agent**

E6 (parkinsonian) has baseline sessions but no PPX sessions in the deposit, so 30 of 31 parkinsonian mice enter the PPX tests; that will be a finding. Next: the hyperbolic fits and Friedman tests.

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; cat > $TMPDIR/fit.py <<'EOF'
import sys,warnings; warnings.filterwarnings('ignore'); sys.path.insert(0,'.')
import icd, pandas as pd, numpy as np
exec(open('/tmp/claude-1001/dd.py').read().split("for exp,groups")[0])
def params(tab):
    r={m:icd.fit_curve(row.values/100) for m,row in tab.iterrows()}
    return pd.DataFrame(r,index=['A','K','AUC']).T
for exp,g in [('PPX','parkinsonian'),('A77636','parkinsonian'),('PPX','control'),('A77636','control')]:
  for ron,roff in [('four','all'),('first','first'),('all','all')]:
    P={'baseline':params(per_mouse(exp,g,'baseline','all')),'on':params(per_mouse(exp,g,'on',ron))}
    offt=per_mouse(exp,g,'off',roff)
    if len(offt): P['off']=params(offt)
    print('==',exp,g,ron,roff,{k:(len(v),int(v.A.isna().sum())) for k,v in P.items()})
    for p in ['A','K','AUC']:
        t=pd.DataFrame({k:v[p] for k,v in P.items()})
        if 'off' in t:
            r=icd.friedman_dunn(t,'baseline')
            print(p,'n',r['n'],'friedman p %.4g'%r['p'],{k:('med %.3f->%.3f p %.4g'%(v['median_ref'],v['median'],v['p_bonf'])) for k,v in r['dunn'].items()})
        else:
            from scipy import stats
            tt=t.dropna(); print(p,len(tt),'wilcoxon',stats.wilcoxon(tt.baseline,tt.on).pvalue, tt.median().round(3).to_dict())
EOF
$TMPDIR/venv/w/bin/python $TMPDIR/fit.py
```

```
== PPX parkinsonian four all {'baseline': (31, 0), 'on': (30, 0), 'off': (30, 0)}
A n 30 friedman p 1.2e-06 {'on': 'med 0.891->0.785 p 1.861e-06', 'off': 'med 0.891->0.879 p 0.7323'}
K n 30 friedman p 0.03228 {'on': 'med 0.258->0.321 p 0.1866', 'off': 'med 0.258->0.419 p 0.01965'}
AUC n 30 friedman p 6.602e-08 {'on': 'med 3.948->2.905 p 2.688e-08', 'off': 'med 3.948->3.379 p 0.07773'}
== PPX parkinsonian first first {'baseline': (31, 0), 'on': (30, 0), 'off': (30, 1)}
A n 29 friedman p 0.006289 {'on': 'med 0.899->0.810 p 0.01165', 'off': 'med 0.899->0.960 p 1'}
K n 29 friedman p 0.576 {'on': 'med 0.252->0.290 p 1', 'off': 'med 0.252->0.318 p 0.587'}
AUC n 29 friedman p 9.694e-05 {'on': 'med 4.065->3.442 p 5.296e-05', 'off': 'med 4.065->3.953 p 0.3783'}
== PPX parkinsonian all all {'baseline': (31, 0), 'on': (30, 0), 'off': (30, 0)}
A n 30 friedman p 1.2e-06 {'on': 'med 0.891->0.785 p 1.861e-06', 'off': 'med 0.891->0.879 p 0.7323'}
K n 30 friedman p 0.03228 {'on': 'med 0.258->0.321 p 0.1866', 'off': 'med 0.258->0.419 p 0.01965'}
AUC n 30 friedman p 6.602e-08 {'on': 'med 3.948->2.905 p 2.688e-08', 'off': 'med 3.948->3.379 p 0.07773'}
== A77636 parkinsonian four all {'baseline': (16, 0), 'on': (16, 0), 'off': (16, 0)}
A n 16 friedman p 0.305 {'on': 'med 0.915->0.913 p 0.3146', 'off': 'med 0.915->0.966 p 1'}
K n 16 friedman p 0.007173 {'on': 'med 0.115->0.291 p 0.005308', 'off': 'med 0.115->0.209 p 0.04311'}
AUC n 16 friedman p 0.0016 {'on': 'med 5.817->3.971 p 0.0008139', 'off': 'med 5.817->4.932 p 0.04311'}
== A77636 parkinsonian first first {'baseline': (16, 0), 'on': (16, 0), 'off': (16, 0)}
A n 16 friedman p 0.829 {'on': 'med 0.915->0.947 p 1', 'off': 'med 0.915->0.945 p 1'}
K n 16 friedman p 0.04677 {'on': 'med 0.115->0.226 p 0.4318', 'off': 'med 0.115->0.244 p 0.02666'}
AUC n 16 friedman p 0.04677 {'on': 'med 5.817->4.688 p 0.1037', 'off': 'med 5.817->4.860 p 0.04311'}
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python -c "
import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
x=pd.read_excel('Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx',sheet_name='Fig. S1D',header=None)
print(x.drop(columns=[1]).to_string(max_colwidth=40))
"
```

```
0                                        2              3                4               5                 6                7
0    AP coordinates                                    Notes  Behavior Name  Left Side Count  Left Side Area  Right Side Count  Right Side Area
1             -3.07                                      NaN             C2               36      147116.409                30       155719.299
2               NaN  *swap left and right blade, correcte...           C3.2               95      130964.066                13       174614.586
3               NaN                                      NaN           C1.1                X               X                60       169186.264
4               NaN                                      NaN           C1.1               74      124289.967                 X                X
5               NaN                                      NaN             C9               46      197524.285                52        133777.76
6             -3.07                                      NaN             D2                X               X                62       142930.503
7               NaN                                      NaN             D2               65        115333.6                 X                X
8               NaN                                      NaN           D2.2              116      222397.343                26       258593.504
9               NaN                                      NaN           D0.1              142      172103.392               148        219896.91
10              NaN                                      NaN           D4.2              145      167909.281               129        182813.29
11              NaN                                      NaN           D4                 59      154389.859                16       194848.459
12              NaN                                      NaN             D3               37      201514.488                39       199317.496
13
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python -c "
import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_rows',200); pd.set_option('display.max_columns',30)
x=pd.read_excel('Data_ICD_Fig3_HistologyQuantification_striatum_raw.xlsx',sheet_name='Striatum_TH_cohort1',header=None)
print(x.iloc[:46,:14].to_string(max_colwidth=22))
"
```

```
0            1                  2               3            4                  5               6            7                  8               9            10                 11              12           13
0   Park_striatum sect...    E6_slice4                NaN             NaN    E6_slice5                NaN             NaN    E6_slice6                NaN             NaN    E6_slice7                NaN             NaN    E6_slice8
1                     NaN         Area  Mean Fluorescence       RawIntDen         Area  Mean Fluorescence       RawIntDen         Area  Mean Fluorescence       RawIntDen         Area  Mean Fluorescence       RawIntDen         Area
2              left str-1   2470385.16            599.564      1481154059  2755820.326            598.941      1650573673  3374343.888            579.195      1954403023  3925080.553            564.898  2217270599.171  3846886.257
3                   DLS-2   632898.297            579.845     366982704.7   669902.021            569.485     381499196.1   749452.119            534.282     400418549.1   909001.022             507.52   461335878.791   809762.735
4                   DMS-3   707312.486            560.959     396773627.9   883166.528            534.157     471749226.5   918417.393            509.912     468311704.9  1064492.202            484.966   516242855.256   708351.935
5                   VLS-4   582078.299            666.519     387965993.7   656243.925            673.251       441816737   879757.653             661.75     582180059.9    890116.63            606.993   540294583.605   1125154.68
6                   VMS-5   480522.235            602.284     289410678.1    506831.26            648.977       328922050   762819.687            609.518     464952682.1  1010850.844             663.57   670770243.722  1114175.908
7             right str-6  3178656.393            555.002      1764159891   3465789.54            565.212      1958905176  3849430.001            610.265      2349174149  4351
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > histo.py <<'EOF'
import pandas as pd, numpy as np, re
from scipy import stats
x=pd.read_excel('Data_ICD_Fig3_HistologyQuantification_striatum_raw.xlsx',sheet_name=None,header=None)
rows=[]
for sheet,d in x.items():
    starts=[i for i in range(len(d)) if isinstance(d.iat[i,0],str) and 'sections' in d.iat[i,0].lower()]
    for s in starts:
        grp='parkinsonian' if d.iat[s,0].lower().startswith('park') else 'control'
        labels=d.iloc[s+2:s+20,0].tolist()
        for c in range(1,d.shape[1]):
            name=d.iat[s,c]
            if not isinstance(name,str) or d.iat[s+1,c]!='Area': continue
            mouse=re.split(r'[_-]sl', name.strip())[0].strip()
            blk=d.iloc[s+2:s+20,c:c+3].apply(pd.to_numeric,errors='coerce').to_numpy(float)
            roi=dict(zip(labels,blk))
            bg=np.nanmean([roi[k][1] for k in roi if k.startswith('background')])
            ctf={k.split('-')[0]+k.split('-')[1]:(v[2]-v[0]*bg)/v[0] for k,v in roi.items() if not k.startswith(('blank','background'))}
            rows.append(dict(cohort=sheet,group=grp,mouse=mouse,slice=name,
                DLS=np.nanmean([ctf['DLS2'],ctf['DLS7']]),DMS=np.nanmean([ctf['DMS3'],ctf['DMS8']]),
                VS=np.nanmean([ctf['VLS4'],ctf['VMS5'],ctf['VLS9'],ctf['VMS10']])))
S=pd.DataFrame(rows)
M=S.groupby(['cohort','group','mouse'])[['DLS','DMS','VS']].mean().reset_index()
print(M.groupby(['cohort','group']).mouse.apply(list))
ctrl=M[M.group=='control'].groupby('cohort')[['DLS','DMS','VS']].mean()
for r in ['DLS','DMS','VS']: M[r+'_norm']=M[r]/M.cohort.map(ctrl[r])
P=M[M.group=='parkinsonian']
print(len(P), 'n ctrl',(M.group=='control').sum())
print('loss %',(100*(1-P[['DLS_norm','DMS_norm','VS_norm']].mean())).round(1).to_dict(), 'median', (100*(1-P[['DLS_norm','DMS_norm','VS_norm']].median())).round(1).to_dict())
print(stats.kruskal(P.DLS_norm,P.DMS_norm,P.VS_norm))
EOF
$TMPDIR/venv/w/bin/python -W ignore histo.py
```

```
cohort               group       
Striatum_TH_cohort1  control                                        [D6.1, E1.1, E5.2]
                     parkinsonian                                   [E6, E6.2, E7, E9]
Striatum_TH_cohort2  control                                          [D0.1, D2, D4.2]
                     parkinsonian                             [D2.2, D3, D4, D4.1, D6]
Striatum_TH_cohort3  control                                                    [C1.1]
                     parkinsonian                                             [C2, C9]
Striatum_TH_cohort4  control                                                      [P4]
                     parkinsonian                                         [N0, N4, N5]
Striatum_TH_cohort5  control                                                  [E1, F6]
                     parkinsonian                                             [F5, F7]
Striatum_TH_cohort6  control                                                [F1.1, F4]
                     parkinsonian    [F1, H0, H0.4, H1.4, H2, H2.1, H2.2, H3, H5.1,...
Striatum_TH_cohort7  control                      [O0, O2, O3, R4.3, R4.4, R5.1, R7.3]
                     parkinsonian    [O0.1, O4.1, R0.2, R1.1, R1.2, R1.3, R1.5, R17...
Striatum_TH_cohort8  control                                        [D6.1, E1.1, E5.2]
                     parkinsonian                                           [E3, E3.2]
Name: mouse, dtype: object
45 n ctrl 22
loss % {'DLS_norm': 64.3, 'DMS_norm': 56.8, 'VS_norm': 35.3} median {'DLS_norm': 66.3, 'DMS_norm': 58.4, 'VS_norm': 39.7}
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; $TMPDIR/venv/w/bin/python -c "
import pandas as pd
x=pd.read_excel('Data_ICD_Fig3_HistologyQuantification_striatum_raw.xlsx',sheet_name=None,header=None)
a=x['Striatum_TH_cohort1'].iloc[22:42]; b=x['Striatum_TH_cohort8'].iloc[22:42]
print(a.iloc[0,:12].tolist()); print(b.iloc[0,:12].tolist())
print(a.iloc[2:5,1:7].values); print(b.iloc[2:5,1:7].values)
"; ls tools/; grep -n "tags\|sanity\|claim:" tools/entry.py | head -30
```

```
Wed Oct 28 10:46:51 UTC 2026
['Ctrl_Striatum sections', 'E5.2_slice4', nan, nan, 'E5.2_slice5', nan, nan, 'E5.2_slice6', nan, nan, 'E5.2_slice7', nan]
['Ctrl_Striatum sections', 'E5.2_slice4', nan, nan, 'E5.2_slice5', nan, nan, 'E5.2_slice6', nan, nan, 'E5.2_slice7', nan]
[[3281161.519 1048.904 3441623068.549 3863501.294 1041.308 4023093046.252]
 [684754.515 780.878 534709936.215 754207.113 1000.069 754259225.973]
 [906147.381 1153.962 1045659575.983 1002435.184 992.688 995105427.694]]
[[3324582.708 416.079 1383287531.459 4045724.38 430.365 1741139477.048]
 [841753.218 412.429 347163476.486 966396.662 428.05 413665872.155]
 [852761.043 413.395 352527564.398 1189529.474 434.981 517423122.769]]
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
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,330p tools/entry.py
```

```
name = re.split(r"[=<>!~\[ ;]", line.strip(), maxsplit=1)[0].lower().replace("_", "-")
            if name and not name.startswith("#") and name not in pinned:
                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")

    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
    used = [r["id"].split(":", 1)[1].partition("/")
            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
    archives = {r["id"].split(":", 1)[1].partition("/")[0]: r["id"].split(":", 1)[0]
                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
    dandisets = [d for d, _, _ in used]
    versions = {d: v for d, _, v in used}
    if entry.get("type") in ("orientation", "reproduction"):
        if not dandisets:
            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
        for d, v in versions.items():
            if not v:
                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
    helper_code = "\n".join((entry_dir / h).read_text() for h in helpers if (entry_dir / h).is_file())

    for name in [n for n in listed if n in present]:
[... 161 more lines not kept]
```

**Agent**

Notebook structure is planned. One more data format to inspect before writing: the open field velocity files, to find where the injection falls.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
import fsspec,zipfile,io,pandas as pd
for zn,f in [("Data_ICD_A77636OpenField_Raw.zip","Data_ICD_A77636OpenField_Raw/O2_openField_A77636_101624.xlsx"),("Data_ICD_Fig5_DREADDLocomotion_Raw.zip","Data_ICD_Fig5_DREADDLocomotion_Raw/H2_openField_CNO_061323.xlsx")]:
    b=fsspec.open("https://zenodo.org/records/15258978/files/"+zn+"?download=1",block_size=2**22).open().read()
    open(zn,'wb').write(b)
    z=zipfile.ZipFile(io.BytesIO(b))
    x=pd.read_excel(io.BytesIO(z.read(f)),sheet_name=None,header=None)
    for s,d in x.items():
        print(zn,s,d.shape); print(d.head(8).to_string()); 
        v=pd.to_numeric(d[0],errors='coerce'); print('time range',v.min(),v.max(), 'dt',v.diff().median())
        print(d[d[1].isna() | d[0].apply(lambda q:isinstance(q,str))].head(10))
EOF
```

```
Data_ICD_A77636OpenField_Raw.zip Sheet1 (125191, 4)
       0   1   2         3
0  0.000 NaN NaN         -
1  0.067 NaN NaN   0.98423
2  0.134 NaN NaN  0.753773
3  0.201 NaN NaN  0.164422
4  0.268 NaN NaN  0.093378
5  0.335 NaN NaN  0.181665
6  0.402 NaN NaN  0.798617
7  0.470 NaN NaN  0.338591
time range 0.0 8406.508 dt 0.06700000000000728
       0   1   2         3
0  0.000 NaN NaN         -
1  0.067 NaN NaN   0.98423
2  0.134 NaN NaN  0.753773
3  0.201 NaN NaN  0.164422
4  0.268 NaN NaN  0.093378
5  0.335 NaN NaN  0.181665
6  0.402 NaN NaN  0.798617
7  0.470 NaN NaN  0.338591
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
import zipfile,io,pandas as pd,numpy as np
from concurrent.futures import ThreadPoolExecutor
for zn in ["Data_ICD_A77636OpenField_Raw.zip","Data_ICD_Fig5_DREADDLocomotion_Raw.zip"]:
    z=zipfile.ZipFile(zn)
    names=[n for n in z.namelist() if n.endswith('.xlsx') and not n.startswith('__')]
    def one(n):
        d=pd.read_excel(io.BytesIO(z.read(n)),header=None)
        t=pd.to_numeric(d[0],errors='coerce').to_numpy(); v=pd.to_numeric(d[3],errors='coerce').to_numpy()
        dt=np.diff(t); gaps=[(round(t[i]/60,1),round(dt[i]/60,2)) for i in np.where(dt>1)[0]]
        nan_rows=np.where(np.isnan(v))[0]
        return n.split('/')[-1], round(t[0]/60,2), round(t[-1]/60,1), gaps, len(nan_rows), [round(t[i]/60,1) for i in nan_rows[:5] if not np.isnan(t[i])], d.shape[1]
    with ThreadPoolExecutor(8) as ex:
        for r in ex.map(one,names): print(r)
EOF
```

```
Exit code 1
('R1.3_openField_A77636_013125.xlsx', np.float64(0.0), np.float64(180.0), [], 75, [np.float64(0.0), np.float64(9.7), np.float64(9.7), np.float64(9.7), np.float64(9.7)], 4)
('O3.6_openField_A77636_111224.xlsx', np.float64(0.0), np.float64(122.7), [], 26, [np.float64(0.0), np.float64(4.0), np.float64(4.0), np.float64(20.1), np.float64(20.1)], 4)
Traceback (most recent call last):
  File "<stdin>", line 13, in <module>
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 453, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
  File "<stdin>", line 7, in one
  File "/tmp/claude-1001/venv/w/lib/python3.13/site-packages/pandas/io/excel/_base.py", line 513, in read_excel
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
import openpyxl,zipfile,io,pandas as pd,numpy as np
for zn in ["Data_ICD_A77636OpenField_Raw.zip","Data_ICD_Fig5_DREADDLocomotion_Raw.zip"]:
    z=zipfile.ZipFile(zn)
    names=[n for n in z.namelist() if n.endswith('.xlsx') and not n.startswith('__')]
    for n in names:
        d=pd.read_excel(io.BytesIO(z.read(n)),header=None)
        t=pd.to_numeric(d[0],errors='coerce').to_numpy(); v=pd.to_numeric(d[3],errors='coerce').to_numpy()
        nan_t=t[np.isnan(v)]/60
        # clusters of NaN
        cl=[];
        for q in nan_t:
            if not cl or q-cl[-1][1]>0.5: cl.append([q,q,1])
            else: cl[-1][1]=q; cl[-1][2]+=1
        big=[(round(a,1),round(b,1),c) for a,b,c in cl if c>=5]
        # also high speed peaks
        print(n.split('/')[-1], 'start %.1f end %.1f'%(t[0]/60,t[-1]/60), 'nan clusters>=5:',big[:6])
EOF
```

```
R1.3_openField_A77636_013125.xlsx start 0.0 end 180.0 nan clusters>=5: [(np.float64(9.7), np.float64(9.7), 11), (np.float64(20.2), np.float64(20.7), 19), (np.float64(56.9), np.float64(56.9), 5)]
O3.6_openField_A77636_111224.xlsx start 0.0 end 122.7 nan clusters>=5: [(np.float64(20.1), np.float64(20.1), 11)]
R0.2_openField_A77636_013025.xlsx start 0.0 end 143.8 nan clusters>=5: [(np.float64(20.3), np.float64(20.3), 12)]
R6_openField_A77636_121624.xlsx start 0.0 end 132.5 nan clusters>=5: [(np.float64(20.1), np.float64(20.2), 13)]
O0.1_openField_A77636_101624.xlsx start 0.0 end 140.1 nan clusters>=5: [(np.float64(20.0), np.float64(20.0), 11)]
R0_openField_A77636_122024.xlsx start 0.0 end 158.6 nan clusters>=5: [(np.float64(20.2), np.float64(20.2), 13)]
O2_openField_A77636_101624.xlsx start 0.0 end 140.1 nan clusters>=5: [(np.float64(20.0), np.float64(20.0), 11)]
R3.2_openField_A77636_120224.xlsx start 0.0 end 141.1 nan clusters>=5: [(np.float64(20.0), np.float64(20.0), 12)]
R1.5_openField_A77636_020425.xlsx start 0.0 end 147.8 nan clusters>=5: [(np.float64(20.1), np.float64(20.1), 16)]
R3.1_openField_A77636_120224.xlsx start 0.0 end 141.1 nan clusters>=5: [(np.float64(20.0), np.float64(20.0), 12)]
R5.1_openField_A77636_120224.xlsx start 0.0 end 141.1 nan clusters>=5: [(np.float64(20.0), np.float64(20.0), 12)]
R6.1_openField_A77636_013125.xlsx start 0.0 end 180.0 nan clusters>=5: [(np.float64(20.2), np.float64(20.2), 12)]
R7.3_openField_A77636_013025.xlsx start 0.0 end 143.8 nan clusters>=5: [(np.float64(20.3), np.float64(20.3), 12)]
O0_openField_A77636_101624.xlsx start 0.0 end 140.1 nan clusters>=5: [(np.float64(20.0), np.float64(20.0), 11)]
R3.3_openField_A77636_013125.xlsx start 0.0 end 180.0 nan clusters>=5: [(np.float64(20.2), np.float64(20.2), 12)]
R4.1_openField_A77636_013025.xlsx start 0.0 end 143.8 nan clusters>=5: [(np.float64(20.3), np.float64(20.3), 12)]
R5.3_openField_A77636_020425.xlsx start 0.0 end 147.8 nan clusters>=5: [(np.float64(20.1), np.float64(2
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
import pandas as pd
pd.set_option('display.width',250)
x=pd.read_excel('Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx',sheet_name=None,header=None)
d=x['Fig. S1H&I']; print(d.iloc[:3].to_string(max_colwidth=30)); print(d.iloc[30:40].to_string(max_colwidth=20))
print(d.iloc[0].tolist())
k=x['Fig. S1K&L']; print(k.iloc[28:40].to_string(max_colwidth=20))
EOF
```

```
Wed Oct 28 10:52:03 UTC 2026
              0                     1                       2           3                  4                       5   6                     7                       8           9                  10                      11   12                            13                            14  15                             16
0  Session1_Ctrl  # of rewarded trials  Latency to Trigger (s)  # omission  # of total trials  % of successful trials NaN  # of rewarded trials  Latency to Trigger (s)  # omission  # of total trials  % of successful trials  NaN  % of TOTAL successful trials  TOTAL Latency to Trigger (s) NaN                            NaN
1            NaN                BLOCK1                     NaN         NaN                NaN                     NaN NaN                BLOCK2                     NaN         NaN                NaN                     NaN  NaN                         TOTAL                           NaN NaN  Note: the grey cell in the...
2            NaN                    46                5.963848           7                 53               86.792453 NaN                    48                5.584604           5                 53               90.566038  NaN                     88.679245                      5.774226 NaN                            NaN
               0                    1                    2           3                  4                    5   6                    7                    8           9                  10                   11                12                   13                   14  15   16
30            NaN                    5               8.4542          45                 50                   10 NaN                    1                5.003          49                 50                    2               NaN                    6               6.7286 NaN  NaN
31            NaN                    2               10.823          48                 50                    4 NaN      
[... 23 more lines not kept]
```

**Agent**

All the data formats are understood. Writing the notebook (as a cell-marked script converted with nbformat).

**Agent calls Write**

```json
{
 "file_path": "entries/001177-zhuang-2025/build_notebook.py",
 "content": "\"\"\"Builds reproduce_zhuang_2025.ipynb from reproduce_zhuang_2025.py (cells separated by '# %%' lines).\n\nA line '# %% [markdown]' starts a markdown cell; '# %% tags=a,b' starts a code cell with tags.\n\"\"\"\nimport sys\nfrom pathlib import Path\n\nimport nbformat\n\nsrc = Path(__file__).with_name(\"reproduce_zhuang_2025.py\").read_text()\ncells = []\nfor block in src.split(\"\\n# %%\")[1:]:\n    head, _, body = block.partition(\"\\n\")\n    head = head.strip()\n    body = body.strip(\"\\n\")\n    if head.startswith(\"[markdown]\"):\n        text = \"\\n\".join(l[2:] if l.startswith(\"# \") else l.lstrip(\"#\") for l in body.splitlines())\n        cells.append(nbformat.v4.new_markdown_cell(text))\n    else:\n        tags = head.split(\"tags=\", 1)[1].split(\",\") if \"tags=\" in head else []\n        cell = nbformat.v4.new_code_cell(body)\n        if tags:\n            cell.metadata[\"tags\"] = tags\n        cells.append(cell)\nnb = nbformat.v4.new_notebook(cells=cells)\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbformat.write(nb, Path(__file__).with_name(\"reproduce_zhuang_2025.ipynb\"))\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: entries/001177-zhuang-2025/build_notebook.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
mv entries/001177-zhuang-2025/build_notebook.py $TMPDIR/build_notebook.py; sed -i 's|Path(__file__).with_name("reproduce_zhuang_2025.py")|Path(sys.argv[1])|; s|Path(__file__).with_name("reproduce_zhuang_2025.ipynb")|Path(sys.argv[2])|' $TMPDIR/build_notebook.py; grep -n argv $TMPDIR/build_notebook.py
```

```
10:src = Path(sys.argv[1]).read_text()
27:nbformat.write(nb, Path(sys.argv[2]))
```

**Agent**

Adding the helper functions still needed (session-level comparisons, repeated measures one-way ANOVA, histology, open field, instrumental learning tables).

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; cat >> icd.py <<'EOF'


def main_effect_pairs(data: pd.DataFrame, value: str, treat: str, levels: list) -> pd.DataFrame:
    """Bonferroni comparisons of treatment levels pooled over delays, on the pooled within-unit
    error of `split_plot_anova` (the 'first against fourth session' tests of Figure 6B-E)."""
    piv = data.pivot_table(index=["mouse", "delay"], columns=treat, values=value)[levels].dropna()
    res = split_plot_anova(data, value, treat, levels)
    df_ew = res["treat_df"][1]
    # recompute the pooled within-unit mean square
    y = piv.to_numpy(float)
    delays = piv.index.get_level_values("delay").to_numpy()
    ss = 0.0
    for d in sorted(set(delays)):
        yd = y[delays == d]
        ss += np.sum((yd - yd.mean(axis=1, keepdims=True) - yd.mean(axis=0) + yd.mean()) ** 2)
    mse = ss / df_ew
    pairs = [(a, b) for i, a in enumerate(levels) for b in levels[i + 1:]]
    rows = []
    for a, b in pairs:
        diff = piv[b].mean() - piv[a].mean()
        t = diff / np.sqrt(2 * mse / len(piv))
        rows.append({"pair": f"{a} vs {b}", "mean_a": piv[a].mean(), "mean_b": piv[b].mean(),
                     "diff": diff, "n_units": len(piv),
                     "p_bonf": min(1.0, 2 * stats.t.sf(abs(t), df_ew) * len(pairs))})
    return pd.DataFrame(rows)


def rm_oneway(table: pd.DataFrame, reference: str) -> dict:
    """Repeated measures one-way ANOVA over the columns of `table` (complete rows), with
    Bonferroni-corrected paired t tests between every pair of columns (Table 1's reading)."""
    t = table.dropna()
    y = t.to_numpy(float)
    n, k = y.shape
    grand = y.mean()
    ss_c = n * np.sum((y.mean(axis=0) - grand) ** 2)
    ss_s = k * np.sum((y.mean(axis=1) - grand) ** 2)
    ss_e = np.sum((y - grand) ** 2) - ss_c - ss_s
    df_c, df_e = k - 1, (k - 1) * (n - 1)
    F = (ss_c / df_c) / (ss_e / df_e)
    cols = list(t.columns)
    pairs = [(a, b) for i, a in enumerate(cols) for b in cols[i + 1:]]
    comps = {f"{a} vs {b}": min(1.0, stats.ttest_rel(t[a], t[b]).pvalue * len(pairs)) for a, b in pairs}
    return {"n": n, "F": F, "df": (df_c, df_e), "p": stats.f.sf(F, df_c, df_e), "pairs": comps}


# ---------------------------------------------------------------- histology

HISTOLOGY = "Data_ICD_Fig3_HistologyQuantification_striatum_raw.xlsx"


def striatal_th() -> pd.DataFrame:
    """Corrected total fluorescence (CTF) per mouse and subregion, from the histology workbook.

    CTF = (RawIntDen - Area x mean background) / Area, the background the mean of the four
    'background' ROIs of the section (Supplementary methods, Histology, quantification and
    microscopy). DLS and DMS average the left and right ROIs; VS averages VLS and VMS of both
    sides ("VLS and VMS were then combined into ventral striatum (VS)"). Sections are averaged per
    mouse within each staining cohort."""
    rows = []
    for sheet, d in read_excel(HISTOLOGY).items():
        starts = [i for i in range(len(d)) if isinstance(d.iat[i, 0], str) and "sections" in d.iat[i, 0].lower()]
        for s in starts:
            group = "parkinsonian" if d.iat[s, 0].lower().startswith("park") else "control"
            labels = d.iloc[s + 2:s + 20, 0].tolist()
            for c in range(1, d.shape[1] - 2):
                name = d.iat[s, c]
                if not isinstance(name, str) or d.iat[s + 1, c] != "Area":
                    continue
                mouse = re.split(r"[_-]sl", name.strip())[0].strip()
                blk = d.iloc[s + 2:s + 20, c:c + 3].apply(pd.to_numeric, errors="coerce").to_numpy(float)
                roi = dict(zip(labels, blk))
                bg = np.nanmean([v[1] for k, v in roi.items() if str(k).startswith("background")])
                ctf = {str(k).replace("-", ""): (v[2] - v[0] * bg) / v[0] for k, v in roi.items()
                       if not str(k).startswith(("blank", "background"))}
                rows.append({"cohort": sheet.replace("Striatum_TH_", ""), "group": group, "mouse": mouse,
                             "section": name.strip(),
                             "DLS": np.nanmean([ctf.get("DLS2", np.nan), ctf.get("DLS7", np.nan)]),
                             "DMS": np.nanmean([ctf.get("DMS3", np.nan), ctf.get("DMS8", np.nan)]),
                             "VS": np.nanmean([ctf.get(k, np.nan) for k in ("VLS4", "VMS5", "VLS9", "VMS10")])})
    sec = pd.DataFrame(rows)
    return sec


# ---------------------------------------------------------------- open field

def open_field(zip_name: str) -> pd.DataFrame:
    """Velocity (cm/s) per frame of every open field session in one deposit zip, with its mouse."""
    import openpyxl  # noqa: F401  (imported before reading, so the engine loads once)
    zf = zipfile.ZipFile(io.BytesIO(zenodo_bytes(zip_name)))
    out = []
    for name in zf.namelist():
        if not name.endswith(".xlsx") or name.startswith("__MACOSX"):
            continue
        d = pd.read_excel(io.BytesIO(zf.read(name)), header=None)
        t = pd.to_numeric(d[0], errors="coerce").to_numpy(float)
        v = pd.to_numeric(d[3], errors="coerce").to_numpy(float)
        out.append({"file": name.split("/")[-1], "mouse": name.split("/")[-1].split("_")[0],
                    "t_min": t / 60, "velocity": v})
    return pd.DataFrame(out)


def tracking_gaps(t_min, v, near=(15, 25), min_frames=5) -> list:
    """Runs of at least `min_frames` untracked frames starting between `near` minutes."""
    miss = np.isnan(v)
    runs, start = [], None
    for i, m in enumerate(miss):
        if m and start is None:
            start = i
        if (not m or i == len(miss) - 1) and start is not None:
            end = i if not m else i + 1
            if end - start >= min_frames and near[0] <= t_min[start] <= near[1]:
                runs.append((t_min[start], end - start))
            start = None
    return runs


# ---------------------------------------------------------------- instrumental learning

INSTRUMENTAL = "Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx"


def instrumental_tables() -> pd.DataFrame:
    """Per mouse and session, success and latency of the blocked (Figure S1H-I) and random
    (Figure S1K-L) learning phases, read from the two sheets of the workbook as labelled."""
    sheets = read_excel(INSTRUMENTAL)
    rows = []
    for sheet, cols in (("Fig. S1H&I", {"success": 13, "latency": 14}),
                        ("Fig. S1K&L", {"success": 5, "latency": 8})):
        d = sheets[sheet]
        label = None
        for i in range(len(d)):
            first = d.iat[i, 0]
            if isinstance(first, str):
                m = re.match(r"Session\s*(\d+)_(Ctrl|Park)", first.strip())
                label = (int(m.group(1)), "control" if m.group(2) == "Ctrl" else "parkinsonian", i) if m else None
                continue
            if label is None:
                continue
            vals = pd.to_numeric(d.iloc[i, list(cols.values())], errors="coerce").to_numpy(float)
            if np.isnan(vals).all():
                continue
            rows.append({"phase": "blocked" if "H&I" in sheet else "random", "session": label[0],
                         "group": label[1], "header_row": label[2], "row": i,
                         "success": vals[0], "latency": vals[1]})
    return pd.DataFrame(rows)
EOF
$TMPDIR/venv/w/bin/python -W ignore -c "
import icd
t=icd.instrumental_tables(); print(t.groupby(['phase','session','group','header_row']).size())
"
```

```
phase    session  group         header_row
blocked  1        control       0             34
                  parkinsonian  38            83
         2        control       125           34
                  parkinsonian  161           83
         3        control       246           34
                  parkinsonian  283           83
         4        control       368           34
                  parkinsonian  405           83
         5        control       490           28
                  parkinsonian  520           83
         6        control       605           28
                  parkinsonian  636           76
random   1        control       0             32
                  parkinsonian  35            80
                                118           30
         2        parkinsonian  152           80
         3        control       236           32
                  parkinsonian  272           80
         4        control       356           31
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; $TMPDIR/venv/w/bin/python - <<'EOF'
s=open('icd.py').read()
s=s.replace('''            if label is None:
                continue
            vals''','''            if label is None or any(isinstance(v, str) for v in d.iloc[i].tolist()):
                continue
            vals''')
open('icd.py','w').write(s)
EOF
$TMPDIR/venv/w/bin/python -W ignore -c "
import icd
t=icd.instrumental_tables(); print(t.groupby(['phase','session','group','header_row']).size())
"
```

```
phase    session  group         header_row
blocked  1        control       0             32
                  parkinsonian  38            81
         2        control       125           32
                  parkinsonian  161           81
         3        control       246           32
                  parkinsonian  283           81
         4        control       368           32
                  parkinsonian  405           81
         5        control       490           26
                  parkinsonian  520           81
         6        control       605           26
                  parkinsonian  636           74
random   1        control       0             32
                  parkinsonian  35            80
                                118           30
         2        parkinsonian  152           80
         3        control       236           32
                  parkinsonian  272           80
         4        control       356           31
[... 6 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb.py",
 "content": "\n# %% [markdown]\n# # Zhuang, Lemak, Sridhar & Nelson (2025): what DANDI:001177 and the paper's Zenodo deposit support\n#\n# Paper: Zhuang X, Lemak J, Sridhar S, Nelson AB. \"Aberrant striatal firing mediates impulsive\n# decision-making in a mouse model of Parkinson's disease.\" Brain (2025), doi:10.1093/brain/awaf312.\n# The claims file (`claims/001177/10.1093-brain-awaf312.yaml`) was written from the version of record\n# (Europe PMC full text, PMC12597312) with its supplement, and checked by a second reader.\n#\n# Data.\n#\n# - DANDI:001177, version 0.250902.2127, streamed. The paper cites the dandiset without a version\n#   (\"Raw in vivo electrophysiology datasets have been deposited in DANDI\n#   (https://dandiarchive.org/dandiset/001177)\"). This is the only published version; the draft was\n#   modified later (2026-09-03) with the same 56 assets and total size, so the published version is\n#   pinned, as the protocol asks when the paper names none. The dandiset holds the in vivo\n#   electrophysiology of Figures 4, 6F-K, S5 and S8.\n# - Zenodo record 15258978 (doi:10.5281/zenodo.15258978), the paper's deposit of its behaviour,\n#   histology, rotarod and slice data, which the claims file names for every `data: elsewhere`\n#   claim. It has one version. Its files are streamed into memory.\n# - The paper's analysis code, UCSF-Nelson-Lab/ICD-Cognitive-Analysis at commit 5528e222, was read for\n#   the event names and the curve fit; it is not run (it needs a GUI), and `icd.py` re-implements\n#   the parts used, citing them.\n#\n# | Claims | Data | Status here |\n# |---|---|---|\n# | 14 electrophysiology claims (Figure 4, S5, 6F-I, S8) | DANDI:001177 | blocked: the dandiset has no sorted, classified or optically identified units, no laser pulse times and no injection time |\n# | 23 behaviour, histology, rotarod and slice claims | Zenodo 15258978 | tested, except two blocked (sex not recorded; no PPX open field file) |\n# | figs2abc-sex-similar | Zenodo | blocked: the deposit does not give each mouse's sex |\n# | figs1ef-ppx-locomotion | Zenodo | blocked: no PPX open field file in the deposit |\n#\n# Each claim's outcome is in the attempt record and the summary at the end.\n\n# %%\nimport sys\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\n\nimport icd\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\npd.set_option(\"display.max_rows\", 200)\nprint(\"DANDI\", icd.DANDISET, icd.DANDI_VERSION, \"| Zenodo\", icd.ZENODO_DOI, \"| code\", icd.CODE_COMMIT[:8])\n\n# %% [markdown]\n# ## Data check\n#\n# DANDI:001177. Every file is opened and its metadata, groups and array shapes are listed (no\n# voltage is read). The claims need, per session, sorted single units, their putative MSN class,\n# their optical identification (laser pulse times) and the PPX injection time.\n\n# %% tags=sanity\nfrom concurrent.futures import ThreadPoolExecutor\n\nmeta = icd.dandi_metadata()\nassets = icd.dandi_assets()\nprint(meta[\"name\"], \"|\", meta[\"version\"], \"|\", len(assets), \"assets |\", round(assets.size_gb.sum()), \"GB\")\nwith ThreadPoolExecutor(8) as ex:\n    survey = pd.DataFrame(list(ex.map(icd.survey_file, assets.asset_id)))\nsurvey.insert(0, \"path\", assets.path.str.split(\"/\").str[-1].str.replace(\"_ecephys.nwb\", \"\"))\nprint(survey[[\"path\", \"subject\", \"genotype\", \"sex\", \"lesion\", \"start\", \"segments_min\", \"n_channels\",\n              \"n_spike_event_series\", \"n_threshold_crossings\", \"has_units\", \"n_units\"]].to_string())\n\n# %% tags=sanity\nsubj = survey.drop_duplicates(\"subject\")\nprint(\"subjects:\", len(subj), \"| by lesion:\", subj.lesion.value_counts().to_dict(),\n      \"| by genotype:\", subj.genotype.str.replace(\"-\", \"\").value_counts().to_dict())\nprint(\"sessions by kind:\", survey.path.str.contains(\"Saline\").map({True: \"saline\", False: \"PPX\"}).value_counts().to_dict())\nprint(\"saline-session mice:\", sorted(survey[survey.path.str.contains(\"Saline\")].subject))\nprint(\"files with a units table:\", survey[survey.has_units].path.tolist())\nprint(\"units table columns:\", survey[survey.has_units].units_columns.unique().tolist())\nfor _, r in survey[survey.has_units].iterrows():\n    c = np.array(r.unit_spike_counts)\n    print(f\"  {r.path}: {len(c)} units, spike counts {c.min()} to {c.max()}; even-numbered units median \"\n          f\"{np.median(c[::2]):.0f}, odd-numbered median {np.median(c[1::2]):.0f}\")\nprint(\"files with intervals, stimulus or optogenetics metadata:\",\n      int((survey.intervals != \"\").sum()), int((survey.stimulus != \"\").sum()), int(survey.ogen.sum()))\nprint(\"processing modules:\", survey.processing.unique().tolist())\nprint(\"session start years:\", survey.start.str[:4].value_counts().sort_index().to_dict())\nprint(\"description encoding (first 40 characters):\", survey.description_start.iloc[0])\n\n# %% [markdown]\n# What the dandiset holds: 18 mice, 7 with striatal saline and 11 with 6-OHDA (as the paper's Ctrl\n# N = 7 and Park N = 11), 52 PPX open field sessions and 4 saline sessions (4 mice, as Figure S5E),\n# each a 30 kHz 32-channel recording split into segments (most often about 30 min, then about 300 min,\n# then about 70 min, the last presumably the laser session), the 1 kHz LFP, and per electrode the\n# threshold crossings with their 48-sample waveforms (\"Events detected with threshold crossing,\n# manually set for each electrode\"). These are the input to the paper's manual sorting in Plexon\n# Offline Sorter, not its output. Two files carry a `units` table, with spike times only; in both,\n# even-numbered units have far more spikes than odd-numbered ones, consistent with an unsorted and a\n# sorted cluster per channel, but no column says which, nor the channel, the MSN class or the\n# optical label. No file has laser pulse times, an injection time or behaviour. The segment gaps are\n# consistent with an injection after the first 30 min, but this is not stated in the files.\n#\n# Zenodo deposit: the files, then the delay discounting sessions parsed from the raw operant logs.\n\n# %% tags=sanity\nfiles = icd.zenodo_files()\nprint(files.to_string())\ngroups = icd.readme_groups()\nprint({f\"{e}/{g}\": len(v) for (e, g), v in groups.items()})\nsess = icd.sessions()\nprint(\"skipped files:\", sess.attrs[\"skipped\"])\nprint(sess.drop_duplicates(\"file\").groupby([\"experiment\", \"group\", \"condition\"]).agg(\n    mice=(\"mouse\", \"nunique\"), sessions=(\"file\", \"nunique\")).to_string())\nprint(\"mice per experiment and group with no drug session:\",\n      sess.groupby([\"experiment\", \"group\", \"mouse\"]).condition.apply(lambda c: \"on\" not in set(c))\n      .loc[lambda s: s].index.tolist())\nprint(\"free choice trials per block:\", sess.trials.value_counts().sort_index().to_dict())\nprint(\"block labels (delay -> label: sessions):\",\n      sess.groupby([\"delay\", \"block_label\"]).file.nunique().to_dict())\nprint(\"sessions dated from the log (file name malformed):\",\n      sess[sess.date_from == \"log\"].drop_duplicates(\"file\")[[\"file\", \"date\"]].values.tolist())\nprint(\"range of % delayed/large:\", sess.pct_large.min(), sess.pct_large.max(),\n      \"| latency (s):\", round(np.nanmin(sess.lat_all), 3), round(np.nanmax(sess.lat_all), 3))\n\n# %% [markdown]\n# Clock and block check. In every free choice block, the delay between the side nosepoke and the\n# large reward delivery, measured on the logs' own clock, should equal the block's delay. This tests\n# the block-to-delay mapping and that the event times share one clock.\n\n# %% tags=sanity\ndef reward_delays(text):\n    out, block, poke = {}, None, None\n    for line in text.splitlines()[1:]:\n        p = [x.strip().strip('\"') for x in line.split(\",\")]\n        if len(p) < 3:\n            continue\n        m = icd.re.match(r\"B(\\d+)_\", p[1])\n        if m:\n            block = icd.FREE_BLOCKS.get(\"B\" + m.group(1))\n        elif block is not None and p[1] in (\"np_B in\", \"np_D in\") and poke is None:\n            poke = icd._ms(p[2])\n        elif p[1] == \"trial start\" or p[1] == \"cen tri\":\n            poke = None\n        elif block is not None and p[1] == \"l reward delivery\" and poke is not None:\n            out.setdefault(block, []).append((icd._ms(p[2]) - poke) / 1000)\n    return out\n\nrows = []\nfor exp, zf in icd.cognitive_archives().items():\n    for name in zf.namelist():\n        base = name.split(\"/\")[-1]\n        if \"_delay\" in base and not name.startswith(\"__\"):\n            for d, v in reward_delays(zf.read(name).decode(\"latin-1\")).items():\n                rows.append({\"experiment\": exp, \"file\": base, \"delay\": d, \"median_s\": np.median(v),\n                             \"old_labels\": base.startswith(\"P\")})\nrd = pd.DataFrame(rows)\nprint(rd.groupby([\"experiment\", \"old_labels\", \"delay\"]).median_s.describe()[[\"count\", \"25%\", \"50%\", \"75%\"]].round(2))\n\n# %% [markdown]\n# The measured nosepoke-to-reward delays are about 0, 3, 6 and 9 s in the four free choice blocks of\n# every experiment, so the blocks are the paper's delays and the logs keep one clock. The exception\n# is the 2020 cohort of six control PPX mice (files of mice P1 to P7), whose block labels name delays\n# of 0, 6, 12 and 18 s and whose measured delays agree with those labels; 30 of their sessions have\n# no fourth block. The paper's code counts these blocks as the other mice's; so does this analysis,\n# which is a deviation noted under each affected claim. Sessions of the 2021 cohort (C mice) have 30\n# free choice trials per block, the Methods 20.\n\n# %% [markdown]\n# Shared definitions for the delay discounting claims. Per mouse and condition, the per-delay value\n# is the mean over the condition's sessions. Readings, from the claims file:\n#\n# - baseline (a) every baseline session in the deposit, (b) the last stable run by the Methods' CV\n#   rule;\n# - drug ON (a) the first ON session by date, (b) the mean over the first four ON sessions;\n# - drug OFF: every washout session (the claims file gives no reading; all are used, as\n#   Summary_Cognitive.m averages a mouse's sessions within a condition), with the first OFF session\n#   as a variant.\n\n# %%\nW = icd.wide(sess)\nD = icd.DELAYS\n\ndef per_mouse(exp, group, cond, reading, value=\"pct_large\"):\n    w = (icd.wide(sess, value) if value != \"pct_large\" else W)\n    w = w[(w.experiment == exp) & (w.group == group) & (w.condition == cond)].sort_values(\"date\")\n    out = {}\n    for m, g in w.groupby(\"mouse\"):\n        if reading == \"all\":\n            sel = g\n        elif reading == \"first\":\n            sel = g.head(1)\n        elif reading == \"four\":\n            sel = g.head(4)\n        elif reading == \"fourth\":\n            sel = g.iloc[3:4]\n        elif reading == \"stable\":\n            later = W[(W.experiment == exp) & (W.mouse == m) & (W.condition != \"baseline\")].date.min()\n            files_b = W[(W.experiment == exp) & (W.mouse == m) & (W.condition == \"baseline\")]\n            files_b = files_b[files_b.date < later] if pd.notna(later) else files_b\n            sel = g[g.file.isin(icd.stable_window(files_b))]\n        if len(sel):\n            out[m] = sel[D].mean()\n    t = pd.DataFrame(out).T\n    t.index.name = \"mouse\"\n    return t\n\ndef long(tab, **kw):\n    l = tab.reset_index().melt(id_vars=\"mouse\", var_name=\"delay\", value_name=\"v\")\n    for k, v in kw.items():\n        l[k] = v\n    return l\n\ndef drug_test(exp, group, rb, rd, value=\"pct_large\"):\n    base, on = per_mouse(exp, group, \"baseline\", rb, value), per_mouse(exp, group, \"on\", rd, value)\n    L = pd.concat([long(base, t=\"baseline\"), long(on, t=\"on\")])\n    return icd.split_plot_anova(L, \"v\", \"t\", [\"baseline\", \"on\"])\n\ndef show(res, label):\n    print(f\"{label}: mice {res['n_mice']}, units {res['n_units']}, treatment F{res['treat_df']} = \"\n          f\"{res['treat_F']:.3f}, p = {res['treat_p']:.3g}; delay F{res['delay_df']} = {res['delay_F']:.2f}, \"\n          f\"p = {res['delay_p']:.3g}; interaction p = {res['inter_p']:.3g}\")\n    print(res[\"per_delay\"].round(4).to_string(index=False))\n\ndef params(tab):\n    r = {m: icd.fit_curve(row.values / 100) for m, row in tab.iterrows()}\n    return pd.DataFrame(r, index=[\"A\", \"K\", \"AUC\"]).T\n\n# %% [markdown]\n# ## fig1fg-baseline-similar\n#\n# > PPX-naive control and parkinsonian mice showed similar delay discounting.\n#\n# Criterion: two-way ANOVA on group and delay (Table 1), Bonferroni per delay; reproduced when the\n# group effect and every per-delay comparison have p >= 0.05.\n\n# %% tags=claim:fig1fg-baseline-similar\nbaseline_res = {}\nfor r in [\"all\", \"stable\"]:\n    b = {g: per_mouse(\"PPX\", g, \"baseline\", r) for g in [\"control\", \"parkinsonian\"]}\n    L = pd.concat([long(b[g], grp=g) for g in b])\n    res = icd.between_anova(L, \"v\", \"grp\")\n    baseline_res[r] = res\n    print(f\"reading {r}: mice {res['n_mice']}; group F{res['df']} = {res['factor_F']:.4f}, p = {res['factor_p']:.4f}; \"\n          f\"delay F{res['delay_df']} = {res['delay_F']:.2f}, p = {res['delay_p']:.3g}; interaction p = {res['inter_p']:.3f}\")\n    print(res[\"per_delay\"].round(3).to_string(index=False))\nnostable = [m for g in [\"control\", \"parkinsonian\"] for m in per_mouse(\"PPX\", g, \"baseline\", \"all\").index\n            if m not in per_mouse(\"PPX\", g, \"baseline\", \"stable\").index]\nprint(\"mice with no stable run under the CV rule:\", len(nostable))\n\n# %% [markdown]\n# **Result: reproduced.** Under reading (a), every baseline session (16 control and 31 parkinsonian\n# mice), the group effect is F = 0.007, p = 0.93 (paper F = 0.003, p = 0.96) and no per-delay\n# comparison differs (all Bonferroni p = 1). Reading (b) keeps only the 12 mice whose deposited\n# baseline sessions pass the CV rule; it also finds no group effect (p = 0.11) and no per-delay\n# difference. The two control mice of the 2020 cohort without a fourth block are missing at 9 s.\n\n# %% [markdown]\n# ## fig1fg-delay-discounting\n#\n# > At baseline both control and parkinsonian mice chose the delayed/large reward less often as its\n# > delay increased.\n#\n# Criterion: the ANOVA above; reproduced when the delay effect has p < 0.05 and in each group the\n# mean is lower at 9 s than at 0 s.\n\n# %% tags=claim:fig1fg-delay-discounting\nfor r, res in baseline_res.items():\n    pdl = res[\"per_delay\"].set_index(\"delay\")\n    print(f\"reading {r}: delay F{res['delay_df']} = {res['delay_F']:.2f}, p = {res['delay_p']:.3g}; \"\n          f\"control {pdl.loc[0, 'control']:.1f} -> {pdl.loc[9, 'control']:.1f} %, \"\n          f\"parkinsonian {pdl.loc[0, 'parkinsonian']:.1f} -> {pdl.loc[9, 'parkinsonian']:.1f} % (0 s -> 9 s)\")\nfig, ax = plt.subplots(figsize=(4, 3))\nfor g in [\"control\", \"parkinsonian\"]:\n    t = per_mouse(\"PPX\", g, \"baseline\", \"all\")\n    ax.errorbar(D, t.mean(), t.sem(), marker=\"o\", label=g)\nax.set(xlabel=\"delay (s)\", ylabel=\"% delayed/large\", ylim=(0, 100), title=\"Baseline, reading (a)\")\nax.legend()\nplt.show()\n\n# %% [markdown]\n# **Result: reproduced.** Under reading (a) the delay effect is F(3, 178) = 38.15, p = 4e-19 (paper\n# F(3, 180) = 38.53), and the choice of the delayed/large reward falls from 91.7 to 32.1% in control\n# and from 85.7 to 32.9% in parkinsonian mice between 0 and 9 s. Under reading (b) the means also\n# fall (95.4 to 82.4%, 95.7 to 58.8%) but the delay effect is not significant (p = 0.11) in 12 mice.\n\n# %% [markdown]\n# ## fig1f-ctrl-ppx-no-change and fig1g-park-ppx-fewer-large\n#\n# > PPX did not change delay discounting in healthy control mice.\n# > In parkinsonian mice PPX reduced the likelihood of choosing the delayed/large reward at every delay.\n#\n# Split-plot ANOVA (unit = mouse x delay, see `icd.py`) of baseline against PPX ON, Bonferroni per\n# delay on the pooled error (paired t tests as a variant). Readings: baseline (a)/(b) x PPX first/four.\n\n# %% tags=claim:fig1f-ctrl-ppx-no-change\nfor rb in [\"all\", \"stable\"]:\n    for rd in [\"first\", \"four\"]:\n        show(drug_test(\"PPX\", \"control\", rb, rd), f\"control, baseline {rb}, PPX {rd}\")\n\n# %% [markdown]\n# **Result: reproduced.** In the 16 control mice the PPX effect is not significant under any reading\n# (p = 0.10 to 0.38; paper F(1, 60) = 0.96, p = 0.33), and no per-delay comparison reaches\n# p < 0.05 on the pooled error. With the first four PPX sessions and every baseline, F(1, 54) = 1.98,\n# p = 0.16. Six control mice of the 2020 cohort had delays of 0, 6, 12 and 18 s; their fourth block is\n# missing in some sessions, so 10 mice enter at 9 s.\n\n# %% tags=claim:fig1g-park-ppx-fewer-large\nfor rb in [\"all\", \"stable\"]:\n    for rd in [\"first\", \"four\"]:\n        show(drug_test(\"PPX\", \"parkinsonian\", rb, rd), f\"parkinsonian, baseline {rb}, PPX {rd}\")\n\n# %% [markdown]\n# **Result: reproduced.** With every baseline session and the mean of the four PPX sessions, the PPX\n# effect is F(1, 116) = 91.46, p = 2.5e-16 (paper F(1, 120) = 95.48) and the delayed/large choices are\n# lower under PPX at all four delays (Bonferroni p < 0.0001, < 0.0001, 0.0002 and 0.022 at 0, 3, 6\n# and 9 s; paired variant p <= 0.0034). With the first PPX session only, three of four delays are\n# significant. 30 of the 31 parkinsonian mice have PPX sessions in the deposit (mouse E6 has only\n# baseline sessions).\n\n# %% [markdown]\n# ## fig1ijk-ppx-a-k-auc\n#\n# > In parkinsonian mice PPX decreased A, increased K and reduced the area under the discounting curve.\n#\n# Fit of V = A/(1 + K D) per mouse and condition, Friedman over baseline, PPX ON and PPX OFF, Dunn's\n# comparisons against baseline (Bonferroni over two).\n\n# %%\ndef friedman_block(exp, group, ron, roff, label):\n    P = {\"baseline\": params(per_mouse(exp, group, \"baseline\", \"all\")),\n         \"on\": params(per_mouse(exp, group, \"on\", ron)),\n         \"off\": params(per_mouse(exp, group, \"off\", roff))}\n    fails = {k: int(v.A.isna().sum()) for k, v in P.items()}\n    out = {}\n    for p in [\"A\", \"K\", \"AUC\"]:\n        t = pd.DataFrame({k: v[p] for k, v in P.items()})\n        r = icd.friedman_dunn(t, \"baseline\")\n        rm = icd.rm_oneway(t, \"baseline\")\n        out[p] = (r, rm, t)\n        print(f\"{label} {p}: n = {r['n']}, Friedman chi2 = {r['chi2']:.2f}, p = {r['p']:.3g}; \"\n              + \"; \".join(f\"Dunn baseline vs {c}: median {v['median_ref']:.3f} -> {v['median']:.3f}, p = {v['p_bonf']:.3g}\"\n                          for c, v in r[\"dunn\"].items())\n              + f\" | RM ANOVA p = {rm['p']:.3g}, Bonferroni \" + \", \".join(f\"{k} p = {v:.3g}\" for k, v in rm[\"pairs\"].items()))\n    print(f\"{label}: failed fits per condition {fails}\")\n    return out\n\n# %% tags=claim:fig1ijk-ppx-a-k-auc\nppx_params = {}\nfor ron, roff in [(\"four\", \"all\"), (\"first\", \"first\")]:\n    ppx_params[ron] = friedman_block(\"PPX\", \"parkinsonian\", ron, roff, f\"PPX ON {ron}, OFF {roff}\")\n\n# %% [markdown]\n# **Result: partially reproduced.** With the four PPX sessions, A falls (median 0.891 to 0.785, Dunn\n# p = 1.9e-06) and AUC falls (3.95 to 2.91, p = 2.7e-08), but the rise in K (0.258 to 0.321) is not\n# significant by Dunn's test (p = 0.19), although the Friedman test over the three conditions gives\n# p = 0.032 (the paper reports p = 0.03 for K). With the first PPX session, A and AUC fall (p = 0.012\n# and 5.3e-05) and K does not change (p = 1). 30 mice enter; no fit failed.\n\n# %% [markdown]\n# ## figs2ijk-ppx-washout\n#\n# > After a 48 h PPX washout the A value of parkinsonian mice returned to baseline while the changes in\n# > K and AUC persisted.\n#\n# The same fits; readings (a) Friedman with Dunn's, (b) repeated measures one-way ANOVA with Bonferroni\n# (Table 1). Reproduced when baseline against OFF has p >= 0.05 for A and p < 0.05 for K and AUC, in\n# the direction seen under PPX.\n\n# %% tags=claim:figs2ijk-ppx-washout\nfor ron, out in ppx_params.items():\n    for p in [\"A\", \"K\", \"AUC\"]:\n        r, rm, t = out[p]\n        print(f\"ON {ron} {p}: baseline vs OFF Dunn p = {r['dunn']['off']['p_bonf']:.3g} \"\n              f\"(median {r['dunn']['off']['median_ref']:.3f} -> {r['dunn']['off']['median']:.3f}); \"\n              f\"RM ANOVA Bonferroni p = {rm['pairs']['baseline vs off']:.3g}; ON vs OFF p = {rm['pairs']['on vs off']:.3g}\")\n\n# %% [markdown]\n# **Result: partially reproduced.** With every washout session, A after washout does not differ from\n# baseline (Dunn p = 0.73, RM ANOVA p > 0.05) and K stays raised (0.258 to 0.419, Dunn p = 0.020), but\n# AUC after washout (3.95 to 3.38) does not differ from baseline at p < 0.05 by Dunn's test\n# (p = 0.078); the printed RM ANOVA reading is above.\n\n# %% [markdown]\n# ## figs2de-omissions-low\n#\n# > Omission rates were low at baseline and under PPX; per-delay comparisons found no PPX effect on\n# > center or side omissions in either group, except center omissions at the 6 s delay in\n# > parkinsonian mice.\n\n# %% tags=claim:figs2de-omissions-low\nom = {}\nfor value in [\"pct_center_om\", \"pct_side_om\"]:\n    for g in [\"control\", \"parkinsonian\"]:\n        res = drug_test(\"PPX\", g, \"all\", \"four\", value)\n        om[(value, g)] = res\n        show(res, f\"{value}, {g}\")\n        base = per_mouse(\"PPX\", g, \"baseline\", \"all\", value)\n        on = per_mouse(\"PPX\", g, \"on\", \"four\", value)\n        print(f\"   mean rate baseline {np.nanmean(base.values):.2f} %, PPX {np.nanmean(on.values):.2f} %\")\n\n# %% [markdown]\n# **Result: not reproduced.** The criterion asks that center omissions differ only at 6 s in\n# parkinsonian mice and that no other per-delay comparison is significant; the printed Bonferroni\n# p-values above decide it. Mean omission rates are a few percent of free choice trials.\n\n# %% [markdown]\n# ## figs2gh-ppx-latency\n#\n# > In parkinsonian mice on PPX, the latency to choose the immediate/small reward was shorter than at\n# > baseline, and the modulation of choice latency by outcome was lost.\n\n# %% tags=claim:figs2gh-ppx-latency\nshow(drug_test(\"PPX\", \"parkinsonian\", \"all\", \"four\", \"lat_small\"), \"latency to small reward, parkinsonian, baseline vs PPX\")\nfor cond, rd in [(\"baseline\", \"all\"), (\"on\", \"four\")]:\n    lg = per_mouse(\"PPX\", \"parkinsonian\", cond, rd, \"lat_large\")\n    sm = per_mouse(\"PPX\", \"parkinsonian\", cond, rd, \"lat_small\")\n    L = pd.concat([long(lg, size=\"large\"), long(sm, size=\"small\")])\n    show(icd.split_plot_anova(L, \"v\", \"size\", [\"large\", \"small\"]), f\"reward size effect on latency, {cond}\")\n\n# %% [markdown]\n# **Result: see the summary.** The three tests printed above are those of the criterion.\n\n# %% [markdown]\n# ## A77636 claims: fig2d-ctrl-a77636-no-change, fig2e-park-a77636-fewer-large, fig2fgh-a77636-k-auc, figs3-a77636-washout-latency\n\n# %% tags=claim:fig2d-ctrl-a77636-no-change\nfor rb in [\"all\", \"stable\"]:\n    for rd in [\"first\", \"four\"]:\n        show(drug_test(\"A77636\", \"control\", rb, rd), f\"A77636 control, baseline {rb}, ON {rd}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:fig2e-park-a77636-fewer-large\nfor rb in [\"all\", \"stable\"]:\n    for rd in [\"first\", \"four\"]:\n        show(drug_test(\"A77636\", \"parkinsonian\", rb, rd), f\"A77636 parkinsonian, baseline {rb}, ON {rd}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:fig2fgh-a77636-k-auc\na77_params = {}\nfor ron, roff in [(\"four\", \"all\"), (\"first\", \"first\")]:\n    a77_params[ron] = friedman_block(\"A77636\", \"parkinsonian\", ron, roff, f\"A77636 ON {ron}, OFF {roff}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:figs3-a77636-washout-latency\nfor ron, out in a77_params.items():\n    for p in [\"K\", \"AUC\"]:\n        r, rm, t = out[p]\n        on_off = stats.wilcoxon(t.dropna()[\"on\"], t.dropna()[\"off\"]).pvalue\n        k = t.dropna()\n        ranks = k.rank(axis=1)\n        z = (ranks[\"off\"].mean() - ranks[\"on\"].mean()) / np.sqrt(3 * 4 / (6 * len(k)))\n        print(f\"ON {ron} {p}: medians baseline {k.baseline.median():.3f}, ON {k.on.median():.3f}, OFF {k.off.median():.3f}; \"\n              f\"Dunn ON vs OFF p = {min(1, 2 * stats.norm.sf(abs(z)) * 3):.3g} (three comparisons); \"\n              f\"Dunn baseline vs OFF p = {r['dunn']['off']['p_bonf']:.3g}\")\nfor value in [\"pct_center_om\", \"pct_side_om\"]:\n    show(drug_test(\"A77636\", \"parkinsonian\", \"all\", \"four\", value), f\"A77636 parkinsonian, {value}\")\nfor cond, rd in [(\"baseline\", \"all\"), (\"on\", \"four\")]:\n    lg = per_mouse(\"A77636\", \"parkinsonian\", cond, rd, \"lat_large\")\n    sm = per_mouse(\"A77636\", \"parkinsonian\", cond, rd, \"lat_small\")\n    L = pd.concat([long(lg, size=\"large\"), long(sm, size=\"small\")])\n    show(icd.split_plot_anova(L, \"v\", \"size\", [\"large\", \"small\"]), f\"A77636 reward size effect on latency, {cond}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## DREADD claims: fig5g-mcherry-no-change, fig5hi-dreadd-fewer-large, fig5jl-dreadd-params\n#\n# Pre-CNO baseline sessions against the mean of the post-CNO sessions (first four), per group.\n\n# %% tags=claim:fig5g-mcherry-no-change\nfor rb in [\"all\", \"stable\"]:\n    show(drug_test(\"DREADD\", \"mCherry\", rb, \"four\"), f\"mCherry, baseline {rb}, CNO four\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:fig5hi-dreadd-fewer-large\nfor g in [\"hM4Di\", \"hM3Dq\"]:\n    for rb in [\"all\", \"stable\"]:\n        show(drug_test(\"DREADD\", g, rb, \"four\"), f\"{g}, baseline {rb}, CNO four\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:fig5jl-dreadd-params\nfor g in [\"mCherry\", \"hM4Di\", \"hM3Dq\"]:\n    base = params(per_mouse(\"DREADD\", g, \"baseline\", \"all\"))\n    on = params(per_mouse(\"DREADD\", g, \"on\", \"four\"))\n    for p in [\"A\", \"K\", \"AUC\"]:\n        t = pd.DataFrame({\"baseline\": base[p], \"on\": on[p]}).dropna()\n        w = stats.wilcoxon(t.baseline, t.on).pvalue\n        print(f\"{g} {p}: n = {len(t)}, median {t.baseline.median():.3f} -> {t.on.median():.3f}, Wilcoxon p = {w:.3g}\")\n    print(f\"   failed fits: baseline {int(base.A.isna().sum())}, CNO {int(on.A.isna().sum())}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## Repeated dosing: fig6b-ctrl-ppx-stable, fig6c-park-ppx-progressive, fig6de-a77636-persistent\n#\n# Split-plot ANOVA over baseline, first and fourth ON session, with Bonferroni comparisons of the\n# condition means pooled over delays (and per delay as a variant).\n\n# %%\ndef sessions_test(exp, group):\n    base = per_mouse(exp, group, \"baseline\", \"all\")\n    first = per_mouse(exp, group, \"on\", \"first\")\n    fourth = per_mouse(exp, group, \"on\", \"fourth\")\n    L = pd.concat([long(base, t=\"baseline\"), long(first, t=\"first\"), long(fourth, t=\"fourth\")])\n    res = icd.split_plot_anova(L, \"v\", \"t\", [\"baseline\", \"first\", \"fourth\"])\n    pairs = icd.main_effect_pairs(L, \"v\", \"t\", [\"baseline\", \"first\", \"fourth\"])\n    print(f\"{exp} {group}: mice with a fourth session {len(fourth)} of {len(base)}; \"\n          f\"session F{res['treat_df']} = {res['treat_F']:.2f}, p = {res['treat_p']:.3g}\")\n    print(pairs.round(4).to_string(index=False))\n    L2 = pd.concat([long(first, t=\"first\"), long(fourth, t=\"fourth\")])\n    print(icd.split_plot_anova(L2, \"v\", \"t\", [\"first\", \"fourth\"])[\"per_delay\"].round(4).to_string(index=False))\n    return pairs\n\n# %% tags=claim:fig6b-ctrl-ppx-stable\nsessions_test(\"PPX\", \"control\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:fig6c-park-ppx-progressive\nsessions_test(\"PPX\", \"parkinsonian\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:fig6de-a77636-persistent\nsessions_test(\"A77636\", \"parkinsonian\")\nsessions_test(\"A77636\", \"control\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig1b-th-loss\n#\n# > 6-OHDA caused about 50% loss of TH immunofluorescence in the rostral dorsolateral and\n# > dorsomedial striatum, with less depletion in the ventral striatum.\n#\n# CTF per ROI (Supplementary methods), normalized to the mean of the control mice of the same staining\n# cohort (each cohort \"includes both healthy and parkinsonian samples to control for inter-batch\n# staining variability\", deposit README); reading (b) normalizes to the mean of all control mice.\n# Kruskal-Wallis over DLS, DMS and VS of the parkinsonian mice with Dunn's comparisons.\n\n# %% tags=claim:fig1b-th-loss\nsec = icd.striatal_th()\nprint(\"sections:\", len(sec), \"| mice per cohort and group:\")\nprint(sec.groupby([\"cohort\", \"group\"]).mouse.nunique().unstack().to_string())\nM = sec.groupby([\"cohort\", \"group\", \"mouse\"])[[\"DLS\", \"DMS\", \"VS\"]].mean().reset_index()\nctrl_cohort = M[M.group == \"control\"].groupby(\"cohort\")[[\"DLS\", \"DMS\", \"VS\"]].mean()\nctrl_all = M[M.group == \"control\"][[\"DLS\", \"DMS\", \"VS\"]].mean()\n\ndef dunn_kw(df, cols):\n    allv = pd.concat([df[c] for c in cols]).rank()\n    n = len(df)\n    ranks = {c: allv.iloc[i * n:(i + 1) * n].mean() for i, c in enumerate(cols)}\n    N = n * len(cols)\n    se = np.sqrt(N * (N + 1) / 12 * (2 / n))\n    pairs = [(a, b) for i, a in enumerate(cols) for b in cols[i + 1:]]\n    return {f\"{a} vs {b}\": min(1, 2 * stats.norm.sf(abs(ranks[a] - ranks[b]) / se) * len(pairs)) for a, b in pairs}\n\nth = {}\nfor reading, ref in [(\"per cohort\", None), (\"all controls\", ctrl_all)]:\n    N = M.copy()\n    for r in [\"DLS\", \"DMS\", \"VS\"]:\n        N[r] = N[r] / (N.cohort.map(ctrl_cohort[r]) if ref is None else ref[r])\n    P = N[N.group == \"parkinsonian\"].groupby(\"mouse\")[[\"DLS\", \"DMS\", \"VS\"]].mean()\n    th[reading] = P\n    loss = 100 * (1 - P.mean())\n    print(f\"{reading}: {len(P)} parkinsonian mice; loss % mean {loss.round(1).to_dict()}, \"\n          f\"median {(100 * (1 - P.median())).round(1).to_dict()}; Kruskal-Wallis p = {stats.kruskal(P.DLS, P.DMS, P.VS).pvalue:.3g}; \"\n          f\"Dunn {dict((k, round(v, 4)) for k, v in dunn_kw(P, ['DLS', 'DMS', 'VS']).items())}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## figs1d-snc-cells\n#\n# > Parkinsonian mice had fewer TH-positive dopamine neurons in the substantia nigra pars compacta\n# > than controls.\n#\n# Density = TH+ cells counted over the four sections and both sides, divided by the area counted.\n# The workbook has no group column; groups come from the deposit README's PPX lists and, for the\n# electrophysiology mice, from the DANDI subjects' lesion (saline or 6-OHDA).\n\n# %% tags=claim:figs1d-snc-cells\nsnc = icd.read_excel(icd.INSTRUMENTAL)[\"Fig. S1D\"].iloc[1:].copy()\nsnc.columns = [\"ap\", \"image\", \"notes\", \"mouse\", \"lc\", \"la\", \"rc\", \"ra\"]\nfor c in [\"lc\", \"la\", \"rc\", \"ra\"]:\n    snc[c] = pd.to_numeric(snc[c], errors=\"coerce\")\nbad = snc[(snc.la < 1000) | (snc.ra < 1000)]\nprint(\"rows whose area is under 1000 (columns shifted):\", bad[[\"mouse\", \"lc\", \"la\", \"rc\", \"ra\"]].values.tolist())\nsnc.loc[bad.index, [\"lc\", \"la\", \"rc\", \"ra\"]] = np.nan\nmouse_n = snc.mouse.str.replace(\"JF-\", \"JF\").str.strip()\nper = snc.assign(mouse=mouse_n).groupby(\"mouse\").apply(\n    lambda g: pd.Series({\"cells\": g.lc.sum() + g.rc.sum(), \"area\": g.la.sum() + g.ra.sum()}))\nper[\"density\"] = per.cells / per.area * 1e6\nppx_c, ppx_p = groups[(\"PPX\", \"control\")], groups[(\"PPX\", \"parkinsonian\")]\ndandi_lesion = {s.replace(\"-\", \".\"): l for s, l in zip(subj.subject, subj.lesion)}\ndandi_lesion.update({s.replace(\"-\", \"\"): l for s, l in zip(subj.subject, subj.lesion)})\ndef snc_group(m):\n    if m in ppx_c:\n        return \"control\"\n    if m in ppx_p:\n        return \"parkinsonian\"\n    return {\"saline\": \"control\", \"6-OHDA\": \"parkinsonian\"}.get(dandi_lesion.get(m), None)\nper[\"group\"] = [snc_group(m) for m in per.index]\nprint(per.round(2).to_string())\nlab = per.dropna(subset=[\"group\"])\nc, p = lab[lab.group == \"control\"].density, lab[lab.group == \"parkinsonian\"].density\nprint(f\"linked mice: {len(lab)} of {len(per)} (control {len(c)}, parkinsonian {len(p)}); median density \"\n      f\"control {c.median():.1f}, parkinsonian {p.median():.1f} cells/mm2 (area units assumed um2); \"\n      f\"Mann-Whitney p = {stats.mannwhitneyu(c, p).pvalue:.3g}\")\nunl = per[per.group.isna()].density\nfor g in [\"control\", \"parkinsonian\"]:\n    cc = pd.concat([c, unl]) if g == \"control\" else c\n    pp = pd.concat([p, unl]) if g == \"parkinsonian\" else p\n    print(f\"   unlinked mice all counted as {g}: Mann-Whitney p = {stats.mannwhitneyu(cc, pp).pvalue:.3g}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## fig1c-rotarod\n#\n# > Parkinsonian mice fell sooner from the accelerating rotarod than controls, and PPX improved their\n# > performance.\n\n# %% tags=claim:fig1c-rotarod\nrr = icd.read_excel(\"Data_ICD_Fig1_Rotarod_PPX.xlsx\")[\"Sheet1\"]\ncols = {rr.iat[0, j]: pd.to_numeric(rr.iloc[2:, j], errors=\"coerce\").dropna().reset_index(drop=True)\n        for j in range(rr.shape[1]) if isinstance(rr.iat[0, j], str)}\nfor k, v in cols.items():\n    print(f\"{k}: n = {len(v)}, median {v.median():.1f} s, range {v.min():.1f} to {v.max():.1f}\")\nctrl = cols[\"Ctrl_baseline\"]\np1, ppx = cols[\"Park_cohort1_baseline\"], cols[\"Park_cohort1_PPX\"]\np2, sal = cols[\"Park_cohort2_baseline\"], cols[\"Park_cohort2_Saline\"]\nkw = stats.kruskal(ctrl, p1, ppx, p2, sal)\nallv = pd.concat([ctrl, p1, ppx, p2, sal], keys=[\"ctrl\", \"p1\", \"ppx\", \"p2\", \"sal\"]).rank()\nN = len(allv)\ndef dunn(a, b, m=3):\n    ra, rb = allv[a].mean(), allv[b].mean()\n    se = np.sqrt(N * (N + 1) / 12 * (1 / len(allv[a]) + 1 / len(allv[b])))\n    return min(1, 2 * stats.norm.sf(abs(ra - rb) / se) * m)\nprint(f\"Kruskal-Wallis over the five columns p = {kw.pvalue:.3g}; Dunn (3 comparisons): control vs park \"\n      f\"baseline p = {dunn('ctrl', 'p1'):.3g}, park baseline vs PPX p = {dunn('p1', 'ppx'):.3g}, \"\n      f\"park baseline vs saline p = {dunn('p2', 'sal'):.3g}\")\nprint(f\"variant: Mann-Whitney control vs park baseline (cohort 1) p = {stats.mannwhitneyu(ctrl, p1).pvalue:.3g}; \"\n      f\"Wilcoxon baseline vs PPX p = {stats.wilcoxon(p1, ppx).pvalue:.3g}; baseline vs saline p = {stats.wilcoxon(p2, sal).pvalue:.3g}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## figs1-instrumental-learning\n#\n# > Parkinsonian mice had slightly slower response latencies and learning in the first instrumental\n# > learning phase but reached performance similar to controls in the second.\n#\n# Mann-Whitney per session, Bonferroni over six sessions, from the workbook's Figure S1H-I and S1K-L\n# sheets. The second \"Session1_Park\" header of the S1K-L sheet (row 118), between session 1\n# parkinsonian and session 2 parkinsonian, is read as session 2 control.\n\n# %% tags=claim:figs1-instrumental-learning\ninst = icd.instrumental_tables()\nfix = (inst.phase == \"random\") & (inst.header_row == 118)\ninst.loc[fix, [\"session\", \"group\"]] = [2, \"control\"]\nrows = []\nfor (phase, s), g in inst.groupby([\"phase\", \"session\"]):\n    c, p = g[g.group == \"control\"], g[g.group == \"parkinsonian\"]\n    for m in [\"success\", \"latency\"]:\n        rows.append({\"phase\": phase, \"session\": s, \"measure\": m, \"n_ctrl\": c[m].notna().sum(),\n                     \"n_park\": p[m].notna().sum(), \"median_ctrl\": c[m].median(), \"median_park\": p[m].median(),\n                     \"p_bonf\": min(1, stats.mannwhitneyu(c[m].dropna(), p[m].dropna()).pvalue * 6)})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## Correlations with striatal TH: fig3a-a-correlates-dms, fig3b-k-no-correlation, figs4-a77636-no-correlation\n#\n# A and K on the drug (four ON sessions) of each parkinsonian mouse against its normalized TH\n# (per-cohort reading of fig1b-th-loss), Pearson correlation.\n\n# %% tags=claim:fig3a-a-correlates-dms\ndef corr_block(exp, label):\n    on = params(per_mouse(exp, \"parkinsonian\", \"on\", \"four\"))\n    out = {}\n    for reading, P in th.items():\n        j = on.join(P, how=\"inner\")\n        for p in [\"A\", \"K\"]:\n            for r in [\"DMS\", \"DLS\", \"VS\"]:\n                rr_, pp = stats.pearsonr(j[p], j[r])\n                out[(reading, p, r)] = (len(j), rr_, pp)\n                print(f\"{label} {reading}: {p} vs {r} TH, n = {len(j)}, r = {rr_:.2f}, p = {pp:.3g}\")\n    return out\ncorr_ppx = corr_block(\"PPX\", \"PPX\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:fig3b-k-no-correlation\nfor (reading, p, r), (n, rr_, pp) in corr_ppx.items():\n    if p == \"K\":\n        print(f\"PPX {reading}: K vs {r}, n = {n}, r = {rr_:.2f}, p = {pp:.3g}\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:figs4-a77636-no-correlation\ncorr_a77 = corr_block(\"A77636\", \"A77636\")\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## figs6-dreadd-validation\n#\n# > In slices CNO reduced optically evoked IPSCs from hM4Di-expressing iMSNs and increased the firing\n# > of hM3Dq-expressing dMSNs.\n\n# %% tags=claim:figs6-dreadd-validation\nsl = icd.read_excel(\"Data_ICD_FigS6_SliceValidation.xlsx\")[\"Sheet1\"]\noipsc = sl.iloc[1:7, 1:3].apply(pd.to_numeric, errors=\"coerce\")\noipsc.columns = [\"baseline\", \"cno\"]\nprint(oipsc.to_string())\nprint(f\"oIPSC: n = {len(oipsc)}, median {oipsc.baseline.median():.1f} -> {oipsc.cno.median():.1f}, \"\n      f\"Wilcoxon p = {stats.wilcoxon(oipsc.baseline, oipsc.cno).pvalue:.3g}\")\ndef io_block(r0):\n    blk = sl.iloc[r0:r0 + 6, 1:11].apply(pd.to_numeric, errors=\"coerce\")\n    blk.index = blk.iloc[:, 0].astype(int)\n    return blk.iloc[:, 1:]\nbase_io, cno_io = io_block(10), io_block(21)\nprint(\"cells:\", base_io.shape[1])\nprint(f\"firing at 300 pA: median {base_io.loc[300].median():.1f} -> {cno_io.loc[300].median():.1f} Hz, \"\n      f\"Wilcoxon p = {stats.wilcoxon(base_io.loc[300], cno_io.loc[300]).pvalue:.3g}\")\nLio = pd.concat([base_io.loc[[100, 200, 300, 400]].T.reset_index(drop=True).rename_axis(\"mouse\").reset_index()\n                 .melt(id_vars=\"mouse\", var_name=\"delay\", value_name=\"v\").assign(t=\"baseline\"),\n                 cno_io.loc[[100, 200, 300, 400]].T.reset_index(drop=True).rename_axis(\"mouse\").reset_index()\n                 .melt(id_vars=\"mouse\", var_name=\"delay\", value_name=\"v\").assign(t=\"cno\")])\nres = icd.split_plot_anova(Lio, \"v\", \"t\", [\"baseline\", \"cno\"])\nprint(f\"input-output, CNO effect (cell x current units): F{res['treat_df']} = {res['treat_F']:.2f}, p = {res['treat_p']:.3g}\")\nimport statsmodels.formula.api as smf\nfrom statsmodels.stats.anova import anova_lm\nfit = smf.ols(\"v ~ C(t) * C(delay)\", data=Lio).fit()\nprint(\"ordinary two-way ANOVA (variant):\", anova_lm(fit, typ=2).round(4).to_dict()[\"PR(>F)\"], \"error df\", int(fit.df_resid))\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## Open field: fig2bc-a77636-locomotion and fig5cf-cno-locomotion\n#\n# The files hold time (s) and velocity (cm/s) at 15 frames/s and no injection mark. Nearly all have\n# a short run of untracked frames at 20.0 to 20.7 min, consistent with the mouse being lifted for the\n# injection after a 20 min baseline. Injection is taken at 20 min (an assumption); a -30 to 0 min\n# baseline does not exist in these files, so only the -20 to 0 min reading can be run.\n\n# %% tags=claim:fig2bc-a77636-locomotion\ndef of_table(zip_name, pre, post):\n    of = icd.open_field(zip_name)\n    rows = []\n    for _, r in of.iterrows():\n        t, v = r.t_min - 20, r.velocity\n        gaps = icd.tracking_gaps(r.t_min, v)\n        rows.append({\"mouse\": r.mouse, \"file\": r.file, \"end_min\": r.t_min[-1],\n                     \"gap_near_20\": f\"{gaps[0][0]:.1f}\" if gaps else \"\",\n                     \"pre\": np.nanmean(v[(t >= pre[0]) & (t < pre[1])]),\n                     \"post\": np.nanmean(v[(t >= post[0]) & (t < post[1])]),\n                     \"post_covered\": r.t_min[-1] - 20 >= post[1]})\n    return pd.DataFrame(rows)\na77_of = of_table(\"Data_ICD_A77636OpenField_Raw.zip\", (-20, 0), (30, 100))\nctrl_ids = groups[(\"A77636\", \"control\")]\na77_of[\"group\"] = np.where(a77_of.mouse.isin(ctrl_ids), \"control\", \"not in the control list\")\nprint(a77_of.round(2).to_string(index=False))\nfor g, t in a77_of.groupby(\"group\"):\n    print(f\"{g}: n = {len(t)}, median {t.pre.median():.2f} -> {t.post.median():.2f} cm/s, \"\n          f\"Wilcoxon p = {stats.wilcoxon(t.pre, t.post).pvalue:.3g}, faster in {int((t.post > t.pre).sum())}\")\nprint(\"mice not in either A77636 list:\", sorted(set(a77_of.mouse) - set(ctrl_ids) - set(groups[(\"A77636\", \"parkinsonian\")])))\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% tags=claim:fig5cf-cno-locomotion\ncno_of = of_table(\"Data_ICD_Fig5_DREADDLocomotion_Raw.zip\", (-20, 0), (20, 30))\ndef dgroup(m):\n    for g in [\"mCherry\", \"hM4Di\", \"hM3Dq\"]:\n        if m in groups[(\"DREADD\", g)]:\n            return g\n    return None\ncno_of[\"group\"] = cno_of.mouse.map(dgroup)\nprint(cno_of.round(2).to_string(index=False))\nfor g, t in cno_of.dropna(subset=[\"group\"]).groupby(\"group\"):\n    print(f\"{g}: n = {len(t)}, median {t.pre.median():.2f} -> {t.post.median():.2f} cm/s, \"\n          f\"Wilcoxon p = {stats.wilcoxon(t.pre, t.post).pvalue:.3g}, faster in {int((t.post > t.pre).sum())}\")\nprint(\"files whose mouse is in no DREADD list:\", cno_of[cno_of.group.isna()].file.tolist())\n\n# %% [markdown]\n# **Result: see the summary.**\n\n# %% [markdown]\n# ## Summary\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

First full draft of the notebook is written; conclusions marked "see the summary" will be filled in from its outputs. Running it once end to end.

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; uv pip install -q --python $TMPDIR/venv/w/bin/python ipykernel nbconvert nbformat 2>&1|tail -1; $TMPDIR/venv/w/bin/python $TMPDIR/build_notebook.py $TMPDIR/nb.py reproduce_zhuang_2025.ipynb && date -u && time $TMPDIR/venv/w/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1800 --output $TMPDIR/run1.ipynb reproduce_zhuang_2025.ipynb 2>&1 | tail -30
```

```
88 cells
Wed Oct 28 10:55:43 UTC 2026
[NbConvertApp] Converting notebook reproduce_zhuang_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 180864 bytes to /tmp/claude-1001/run1.ipynb

real	16m7.043s
user	3m36.417s
sys	0m2.762s
```

**Agent**

It ran without errors in 16 minutes (under the 30 min limit; I'll look for what is slow). Reading the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
import nbformat
nb=nbformat.read('run1.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    out=''.join(o.get('text','') if o.output_type=='stream' else (o.get('data',{}).get('text/plain','') if o.output_type=='execute_result' else (o.get('ename','')+str(o.get('evalue','')) if o.output_type=='error' else '')) for o in c.outputs)
    print(f'##### cell {i} {tags}'); print(out[:6000])
EOF
```

```
<persisted-output>
Output too large (56.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/388d1196-06f3-42a2-8a8d-f47faef993c7/tool-results/b8wej8o83.txt

Preview (first 2KB):
##### cell 1 []
DANDI 001177 0.250902.2127 | Zenodo 10.5281/zenodo.15258978 | code 5528e222

##### cell 3 ['sanity']
Abnormal Striatal Activity in a Mouse Model of Impulse Control Disorder in Parkinson’s Disease | 0.250902.2127 | 56 assets | 1994 GB
                                           path subject   genotype sex  lesion                             start                                                      segments_min  n_channels  n_spike_event_series  n_threshold_crossings  has_units  n_units
0           sub-C3-2_ses-PPXopenField-C3-2-day1    C3.2   Drd1aCre   F  saline  2021-11-30T21:35:42.746000-08:00                                  0.0+30.6; 31.9+300.9; 333.6+69.9          32                    32               38396440      False        0
1           sub-C3-2_ses-PPXopenField-C3-2-day2    C3.2   Drd1aCre   F  saline  2021-12-09T20:19:19.383000-08:00                                  0.0+33.6; 35.0+296.6; 332.3+72.3          32                    25               12315643      False        0
2               sub-C9_ses-PPXopenField-C9-day1      C9     A2aCre   M  6-OHDA  2021-11-21T22:23:09.467000-08:00  0.0+30.4; 31.5+10.4; 42.7+42.6; 85.4+0.6; 86.0+257.5; 345.5+68.5          32                    22                 931492      False        0
3               sub-C9_ses-PPXopenField-C9-day2      C9     A2aCre   M  6-OHDA  2021-11-26T22:10:31.094000-08:00                                  0.0+30.6; 31.9+302.2; 335.1+69.0          32                    22                5951798      False        0
4               sub-D0_ses-PPXopenField-D0-day1      D0     A2aCre   M  6-OHDA  2022-03-07T19:58:35.940000-08:00                                  0.0+30.1; 31.7+313.3; 345.8+69.1          32                    27                8835331      False        
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/388d1196-06f3-42a2-8a8d-f47faef993c7/tool-results/b8wej8o83.txt",
 "offset": 60
}
```

```
60	16  Data_ICD_Striatum_TH_Quantification_RawImages_cohort3.zip   3751.987414  md5:82785a096dee570a6687d0b1e81c91cb
61	17  Data_ICD_Striatum_TH_Quantification_RawImages_cohort4.zip   3914.302469  md5:9fdefa9e1117a00b9bd6fa734935fca8
62	18  Data_ICD_Striatum_TH_Quantification_RawImages_cohort5.zip    266.207508  md5:e0ac9e4a1998e6636fb40703f362acd5
63	19  Data_ICD_Striatum_TH_Quantification_RawImages_cohort6.zip   1330.661444  md5:f3c1bd1e97c764235e2845352b1e5617
64	20  Data_ICD_Striatum_TH_Quantification_RawImages_cohort8.zip   2053.840511  md5:34c9155c1560bead27137ef3e09a07c7
65	{'PPX/control': 16, 'PPX/parkinsonian': 31, 'A77636/control': 10, 'A77636/parkinsonian': 16, 'DREADD/mCherry': 15, 'DREADD/hM4Di': 12, 'DREADD/hM3Dq': 12}
66	skipped files: []
67	                                   mice  sessions
68	experiment group        condition                
69	A77636     control      baseline     10        33
70	                        on           10        40
71	           parkinsonian baseline     11        36
72	                        off          16        64
73	                        on           16        64
74	DREADD     hM3Dq        baseline     12        40
75	                        on           12        48
76	           hM4Di        baseline     10        29
77	                        on           12        43
78	           mCherry      baseline     13        37
79	                        on           14        55
[... 595 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; $TMPDIR/venv/w/bin/python -W ignore - <<'EOF'
import pandas as pd, icd, hashlib
df=pd.read_pickle('/tmp/claude-1001/sess.pkl')
W=icd.wide(df)
m=W[(W.experiment=='DREADD')&(W.group=='mCherry')]
print(m.groupby(['mouse','condition']).file.count().unstack())
print(m[m[[0,3,6,9]].isna().any(axis=1)][['mouse','file',0,3,6,9]])
# files in two folders
arch=icd.cognitive_archives()
names={k:{n.split('/')[-1]:hashlib.md5(z.read(n)).hexdigest() for n in z.namelist() if n.upper().endswith('.CSV') and not n.startswith('__')} for k,z in arch.items()}
for a in names:
    for b in names:
        if a<b:
            common=set(names[a])&set(names[b]); same=sum(names[a][f]==names[b][f] for f in common)
            print(a,b,len(common),'identical',same)
EOF
```

```
condition  baseline  on
mouse                  
F7                4   3
H1                3   4
H1.4              3   4
H2                2   4
H5.1              5   4
H7                3   4
J3                3   4
J5.1              3   4
J6                3   4
O7.1              3   4
R1                3   4
R2.2              2   4
R2.4              3   4
R7.2              3   4
Empty DataFrame
Columns: [mouse, file, 0, 3, 6, 9]
Index: []
DREADD PPX 233 identical 233
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
s=open('nb.py').read()
old='''print(sess.drop_duplicates("file").groupby(["experiment", "group", "condition"]).agg('''
new='''print(sess.drop_duplicates(["experiment", "file"]).groupby(["experiment", "group", "condition"]).agg('''
assert old in s; s=s.replace(old,new)
old='''print("free choice trials per block:"'''
new='''import hashlib
digests = {e: {n.split("/")[-1]: hashlib.md5(z.read(n)).hexdigest() for n in z.namelist()
               if n.upper().endswith(".CSV") and not n.startswith("__")} for e, z in icd.cognitive_archives().items()}
for a in digests:
    for b in digests:
        if a < b:
            common = set(digests[a]) & set(digests[b])
            print(f"files in both {a} and {b}: {len(common)}, byte-identical {sum(digests[a][f] == digests[b][f] for f in common)}")
listed = {(e, m) for (e, g), ids in groups.items() for m in ids}
present = set(zip(sess.experiment, sess.mouse))
print("README mice with no delay discounting file:", sorted(listed - present))
print("free choice trials per block:"'''
assert old in s; s=s.replace(old,new)
# SNc labels from histology
old='''def snc_group(m):
    if m in ppx_c:'''
new='''histo_group = icd.striatal_th().drop_duplicates("mouse").set_index("mouse").group.to_dict()
def snc_group(m):
    if m in histo_group:
        return histo_group[m]
    if m in ppx_c:'''
assert old in s; s=s.replace(old,new)
s=s.replace('''# The workbook has no group column; groups come from the deposit README's PPX lists and, for the
# electrophysiology mice, from the DANDI subjects' lesion (saline or 6-OHDA).''','''# The workbook has no group column. Groups come, in this order, from the histology workbook of the same
# deposit (its "Ctrl" and "Park" blocks), the deposit README's PPX lists, and, for the
# electrophysiology mice, the DANDI subjects' lesion (saline or 6-OHDA).''')
# latency first reading
old='''show(drug_test("PPX", "parkinsonian", "all", "four", "lat_small"), "latency to small reward, parkinsonian, baseline vs PPX")
for cond, rd in [("baseline", "all"), ("on", "four")]:'''
new='''for rd in ["four", "first"]:
    show(drug_test("PPX", "parkinsonian", "all", rd, "lat_small"), f"latency to small reward, parkinsonian, baseline vs PPX {rd}")
for cond, rd in [("baseline", "all"), ("on", "four"), ("on", "first")]:'''
assert old in s; s=s.replace(old,new)
s=s.replace('''show(icd.split_plot_anova(L, "v", "size", ["large", "small"]), f"reward size effect on latency, {cond}")''','''show(icd.split_plot_anova(L, "v", "size", ["large", "small"]), f"reward size effect on latency, {cond} {rd}")''')
# fig5jl friedman reading
old='''        w = stats.wilcoxon(t.baseline, t.on).pvalue
        print(f"{g} {p}: n = {len(t)}, median {t.baseline.median():.3f} -> {t.on.median():.3f}, Wilcoxon p = {w:.3g}")'''
new='''        w = stats.wilcoxon(t.baseline, t.on).pvalue
        # reading (b): Friedman over the two conditions, which reduces to a two-sided sign test
        fr = stats.binomtest(int((t.on > t.baseline).sum()), int((t.on != t.baseline).sum())).pvalue
        print(f"{g} {p}: n = {len(t)}, median {t.baseline.median():.3f} -> {t.on.median():.3f}, "
              f"higher in {int((t.on > t.baseline).sum())}; Wilcoxon p = {w:.3g}; Friedman (sign test) p = {fr:.3g}")'''
assert old in s; s=s.replace(old,new)
open('nb.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Writing the conclusion cells now from the printed numbers, leaving the three changed sections for after the final run.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
s=open('nb.py').read()
def rep(after_tag, text):
    global s
    i=s.index(after_tag)
    j=s.index("**Result: see the summary.**", i)
    s=s[:j]+text+s[j+len("**Result: see the summary.**"):]
rep("claim:fig2d-ctrl-a77636-no-change", """**Result: reproduced.** In the 10 control mice the A77636 effect is not significant under
# any reading (p = 0.31 to 0.80; paper F(1, 36) = 1.05, p = 0.31) and no per-delay comparison
# reaches p < 0.05.""")
rep("claim:fig2e-park-a77636-fewer-large", """**Result: reproduced.** With every baseline session and the four A77636 sessions, the
# effect is F(1, 60) = 45.06, p = 7.7e-09 (paper F(1, 60) = 45.68) and the choices are lower at 3, 6
# and 9 s (Bonferroni p = 0.0049, 0.0003, 0.0003; paper 0.0047, 0.0003, 0.0002), not at 0 s
# (p = 0.56; paper 0.57).""")
rep("claim:fig2fgh-a77636-k-auc", """**Result: reproduced.** With the four A77636 sessions, A does not change (Friedman
# p = 0.31, Dunn p = 0.31; paper 0.31), K rises (median 0.115 to 0.291, Dunn p = 0.0053; paper
# 0.0053) and AUC falls (5.82 to 3.97, Dunn p = 0.0008; paper 0.0008). With the first session only,
# the K and AUC changes are not significant (Dunn p = 0.43 and 0.10).""")
rep("claim:figs3-a77636-washout-latency", """**Result: partially reproduced.** After washout K (0.209) and AUC (4.93) do not differ from
# the A77636 values (Dunn p = 1 and 0.65) and stay on the same side of baseline (0.115, 5.82; Dunn
# baseline against OFF p = 0.043 for both). No per-delay omission comparison is significant
# (smallest Bonferroni p = 0.65). The reward size effect on choice latency is significant at
# baseline (F(1, 52) = 14.70, p = 0.0003; paper F(1, 52) = 11.70) but, against the criterion, also
# on A77636 (F(1, 56) = 4.84, p = 0.032; paper p = 0.07).""")
rep("claim:fig5g-mcherry-no-change", """**Result: reproduced.** In the 14 mCherry mice with delay discounting files, CNO has no
# effect (F(1, 52) = 0.94, p = 0.34; paper F(1, 56) = 0.97, p = 0.33) and no per-delay comparison
# differs (all Bonferroni p = 1). The README lists 15 mCherry mice; R5.5 has no delay discounting
# file in the deposit.""")
rep("claim:fig5hi-dreadd-fewer-large", """**Result: partially reproduced.** In hM3Dq mice CNO lowers the delayed/large choices
# (F(1, 44) = 40.94, p = 8.8e-08; paper 42.30) at 3, 6 and 9 s (p = 0.0006, 0.0013, 0.026). In hM4Di
# mice the main effect holds (F(1, 44) = 12.77, p = 0.0009; paper 22.22) but only the 3 s comparison
# is significant (p = 0.022; 6 s p = 0.38, 9 s p = 0.62).""")
rep("claim:fig6b-ctrl-ppx-stable", """**Result: reproduced.** In control mice no pair of baseline, first and fourth PPX session
# differs (Bonferroni p = 0.46, 0.75 and 1; paper first against fourth p > 0.99); 12 of 16 control
# mice have a fourth PPX session.""")
rep("claim:fig6c-park-ppx-progressive", """**Result: reproduced.** In the 27 parkinsonian mice with four PPX sessions, the
# delayed/large choices fall from 50.7% at baseline to 41.6% in the first and 36.2% in the fourth
# session; baseline differs from both (p = 2.7e-05, 2.7e-11) and the fourth from the first
# (p = 0.024; paper p < 0.0081).""")
rep("claim:fig6de-a77636-persistent", """**Result: reproduced.** In parkinsonian mice baseline differs from the first and fourth
# A77636 session (p = 0.0004 and < 0.0001) and the two sessions do not differ (p = 1; paper 0.59). In
# controls no comparison is significant (smallest p = 0.31; paper first against fourth 0.49).""")
rep("claim:fig1b-th-loss", """**Result: partially reproduced.** VS is less depleted than DLS and DMS and DLS does not
# differ from DMS under the per-cohort reading (Dunn p < 0.0001, 0.0001 and 0.38), but the mean losses
# in DLS (64.3%) and DMS (56.8%) are outside 50 +/- 5%. Normalized to all controls, the DMS loss
# (52.4%) is inside the tolerance and DLS (60.5%) is not, and VS against DMS gives p = 0.052. 45
# parkinsonian mice enter (Table 1 gives N = 44).""")
rep("claim:fig1c-rotarod", """**Result: reproduced.** Parkinsonian mice fall sooner than controls (median 47.3 against
# 91.3 s, Dunn p = 1.1e-15), PPX raises their latency (to 66.7 s, Dunn p = 1.8e-05) and saline does
# not (Dunn p = 0.83). The variant tests agree (Mann-Whitney p = 5e-13, Wilcoxon p = 3e-08 and
# 0.074). The workbook has 40 control, 45 PPX and 27 saline mice; Table 1 gives 31, 45 and 27.""")
rep("claim:figs1-instrumental-learning", """**Result: partially reproduced.** In blocked learning parkinsonian mice have lower success
# in sessions 1, 3 and 4 (Bonferroni p = 0.007, 0.0055, 0.0035) and longer latencies in sessions 3
# to 6 (p = 0.0005 to 0.012). In random learning they are similar in sessions 2 to 6, but session 1
# success differs (65.9 against 86.9%, p = 0.003), against the criterion's "no session of random
# learning differs". Initiation latency differs in no random session.""")
rep("claim:fig3a-a-correlates-dms", """**Result: not reproduced.** A on PPX correlates with DMS TH at r = 0.32, p = 0.13 in the
# 24 mice with both measures (paper r = 0.51, p = 0.006, n = 28), outside the tolerance (0.46 to
# 0.56); DLS and VS are not significant (p = 0.29 and 0.18). Normalized to all controls, r = 0.14.""")
rep("claim:fig3b-k-no-correlation", """**Result: reproduced.** K on PPX does not correlate with TH in any subregion (DMS r = 0.03,
# DLS r = 0.40, VS r = 0.32; p = 0.89, 0.056, 0.13; n = 24).""")
rep("claim:figs4-a77636-no-correlation", """**Result: reproduced.** None of the six correlations of A and K on A77636 with TH is
# significant (smallest p = 0.24, K against VS, r = -0.31; paper r = -0.31, p = 0.23; n = 16).""")
rep("claim:figs6-dreadd-validation", """**Result: reproduced.** CNO reduces oIPSC amplitude (median 647.5 to 55.0 pA, Wilcoxon
# p = 0.031, 6 cells) and raises firing at 300 pA (8 to 16 Hz, p = 0.016, 9 cells), and the CNO
# effect on the input-output curve is F(1, 32) = 17.64, p = 0.0002, the paper's values, when each
# cell and current is the repeated unit; an ordinary two-way ANOVA gives p = 0.082.""")
rep("claim:fig2bc-a77636-locomotion", """**Result: reproduced, resting on an assumption.** With injection at 20 min, the 16 mice
# not in the control list are faster 30 to 100 min after A77636 (median 3.14 to 3.69 cm/s, 13 of
# 16, Wilcoxon p = 0.016; paper p = 0.02) and the 10 controls are not (3.19 to 2.90 cm/s, p = 0.065;
# paper 0.16). Six of the 16 (O6, R0, R1, R3.2, R5.3, R6) are in neither A77636 list; they are taken
# as parkinsonian because the control list is complete (10 of 10) and 16 mice remain, the paper's
# N. R1.1's file has no tracking gap near 20 min.""")
rep("claim:fig5cf-cno-locomotion", """**Result: partially reproduced, resting on an assumption.** With injection at 20 min,
# hM3Dq mice (11 of 11 faster, p = 0.001) and hM4Di mice (9 of 10, p = 0.004) move faster 20 to 30 min
# after CNO, but mCherry mice move slower (2.96 to 2.23 cm/s, 1 of 12 faster, p = 0.016), where the
# criterion needs p >= 0.05. Four files (R0, F0, F3, R1.2) are of mice in no DREADD list, and the
# 2023 files have no tracking gap, so their injection time rests on the assumption alone.""")
# earlier ones
s=s.replace("""# **Result: not reproduced.** The criterion asks that center omissions differ only at 6 s in
# parkinsonian mice and that no other per-delay comparison is significant; the printed Bonferroni
# p-values above decide it. Mean omission rates are a few percent of free choice trials.""","""# **Result: reproduced.** With the four PPX sessions, center omissions of parkinsonian mice
# differ only at 6 s (4.5 against 11.7%, Bonferroni p < 0.0001; other delays p = 0.15 to 1), with a
# PPX main effect (F(1, 116) = 24.82, p = 2.2e-06; paper F(1, 120) = 16.54); no side omission
# comparison and no control comparison is significant (smallest p = 0.60). Mean omission rates are
# 5.0 and 7.8% (center) and 1.6 and 1.9% (side) of free choice trials in parkinsonian mice at
# baseline and on PPX.""")
open('nb.py','w').write(s)
print(s.count("see the summary"))
EOF
```

```
3
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; date -u; $TMPDIR/venv/w/bin/python $TMPDIR/build_notebook.py $TMPDIR/nb.py reproduce_zhuang_2025.ipynb && $TMPDIR/venv/w/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=1800 --output $TMPDIR/run2.ipynb reproduce_zhuang_2025.ipynb 2>&1 | grep -v WARNING | tail -5; date -u; $TMPDIR/venv/w/bin/python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/run2.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    if not any(t in str(tags) for t in ['sanity','figs2gh','figs1d','fig5jl']): continue
    out=''.join(o.get('text','') if o.output_type=='stream' else (o.get('ename','')+str(o.get('evalue','')) if o.output_type=='error' else '') for o in c.outputs)
    print(f'##### cell {i} {tags}'); print(out[-3500:])
EOF
```

```
Wed Oct 28 11:14:52 UTC 2026
88 cells
[NbConvertApp] Converting notebook reproduce_zhuang_2025.ipynb to notebook
[NbConvertApp] Writing 191155 bytes to /tmp/claude-1001/run2.ipynb
Wed Oct 28 11:29:36 UTC 2026
##### cell 3 ['sanity']
-12-01T19:20:06.993000-08:00                                  0.0+30.6; 31.9+293.5; 335.7+78.7          32                    31               20216471      False        0
43              sub-K1_ses-PPXopenField-K1-day2      K1   Drd1aCre   F  6-OHDA  2023-12-05T18:33:13.520000-08:00                                              0.0+30.2; 31.3+371.1          32                    29               20503077      False        0
44              sub-K1_ses-PPXopenField-K1-day3      K1   Drd1aCre   F  6-OHDA  2023-12-14T19:40:44.984000-08:00                                              0.0+30.1; 31.3+371.9          32                    31               20355367      False        0
45              sub-K1_ses-PPXopenField-K1-day4      K1   Drd1aCre   F  6-OHDA  2023-12-20T18:58:15.509000-08:00                                              0.0+30.2; 31.7+370.4          32                    32               22009934      False        0
46              sub-K4_ses-PPXopenField-K4-day1      K4   Drd1aCre   M  6-OHDA  2023-11-30T19:35:24.867000-08:00                                              0.0+30.1; 32.0+376.5          32                    32               22790960      False        0
47  sub-K4_ses-PPXopenField-K4-day2-optoSession      K4   Drd1aCre   M  6-OHDA  2023-12-05T00:18:32.606000-08:00                                                          0.0+71.3          32                    32                7038153      False        0
48              sub-K4_ses-PPXopenField-K4-day2      K4   Drd1aCre   M  6-OHDA  2023-12-04T18:16:50.393000-08:00                                              0.0+30.1; 31.3+300.9          32                    32               16244697      False        0
49              sub-K4_ses-PPXopenField-K4-day3      K4   D
[... 170 more lines not kept]
```

**Agent**

Final numbers for the last three sections are in. It is 11:30 UTC. Filling in the remaining conclusions and the summary, then writing the entry files.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
s=open('nb.py').read()
def rep(after_tag, text):
    global s
    i=s.index(after_tag)
    j=s.index("**Result: see the summary.**", i)
    s=s[:j]+text+s[j+len("**Result: see the summary.**"):]
rep("claim:figs1d-snc-cells", """**Result: reproduced.** In the 29 mice whose group is known (9 control, 20 parkinsonian; the
# paper has 9 and 21), TH+ cell density in the SNc is lower in parkinsonian mice (median 186.6
# against 316.0 cells per mm2, Mann-Whitney p = 0.0003). The three mice in no list (C0.1, C2.1,
# D5.2) do not change this whichever group they are put in (p = 0.0001 and 0.0019). Two rows of the
# workbook (D3 and N4 at -3.51 mm) have their count and area columns shifted and are left out.""")
s=s.replace("""# **Result: see the summary.** The three tests printed above are those of the criterion.""","""# **Result: partially reproduced.** The latency to choose the small reward is shorter on PPX at
# 0 and 3 s (1.28 to 1.09 s and 1.38 to 1.02 s) but the PPX effect is not significant (F(1, 110) =
# 2.87, p = 0.093 with four sessions; p = 0.15 with the first; paper F(1, 114) = 4.505, p = 0.02).
# The reward size effect on latency is present at baseline (F(1, 114) = 5.33, p = 0.023; paper
# F(1, 114) = 7.016, p = 0.0092) and absent on PPX (p = 0.71 with four sessions, 0.19 with the first;
# paper p = 0.70), as the criterion requires.""")
rep("claim:fig5jl-dreadd-params", """**Result: partially reproduced.** Under reading (a), Wilcoxon (Table 1), hM3Dq mice show
# the three changes (A 0.923 to 0.880, p = 0.012; K 0.133 to 0.198, p = 0.0015; AUC 5.10 to 4.31,
# p = 0.0005), hM4Di mice a lower AUC (6.08 to 5.78, p = 0.043) and unchanged A (p = 0.20), and
# mCherry mice no change (p >= 0.36). The rise in K of hM4Di mice (0.123 to 0.136, 7 of 12 higher) is
# not significant (p = 0.20), so "K higher in both DREADD groups" fails; the criterion names a
# partial outcome only for the case where K and AUC hold and A does not. Reading (b), Friedman,
# which with two conditions reduces to a sign test, gives the same pattern with fewer significant
# results (hM4Di AUC p = 0.15).""")
assert "see the summary" not in s
s=s.rstrip()+"""
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
# and the differences from the paper's method.
#
# | Claim | Data | Outcome |
# |---|---|---|
# | fig1b-th-loss | Zenodo | partially reproduced (pattern holds; losses 64 and 57% against 50 +/- 5%) |
# | figs1d-snc-cells | Zenodo | reproduced |
# | fig1c-rotarod | Zenodo | reproduced |
# | figs1ef-ppx-locomotion | Zenodo | blocked: no PPX open field file in the deposit |
# | figs1-instrumental-learning | Zenodo | partially reproduced (random learning session 1 differs) |
# | fig1fg-baseline-similar | Zenodo | reproduced |
# | fig1fg-delay-discounting | Zenodo | reproduced |
# | fig1f-ctrl-ppx-no-change | Zenodo | reproduced |
# | fig1g-park-ppx-fewer-large | Zenodo | reproduced |
# | fig1ijk-ppx-a-k-auc | Zenodo | partially reproduced (K rise not significant by Dunn's test) |
# | figs2abc-sex-similar | Zenodo | blocked: no sex per mouse in the deposit |
# | figs2de-omissions-low | Zenodo | reproduced |
# | figs2gh-ppx-latency | Zenodo | partially reproduced (PPX shortening of small-reward latency not significant) |
# | figs2ijk-ppx-washout | Zenodo | partially reproduced (A recovers, K or AUC persists depending on the test) |
# | fig2bc-a77636-locomotion | Zenodo | reproduced, resting on an assumption (injection at 20 min) |
# | fig2d-ctrl-a77636-no-change | Zenodo | reproduced |
# | fig2e-park-a77636-fewer-large | Zenodo | reproduced |
# | fig2fgh-a77636-k-auc | Zenodo | reproduced |
# | figs3-a77636-washout-latency | Zenodo | partially reproduced (reward size effect on latency remains on A77636) |
# | fig3a-a-correlates-dms | Zenodo | not reproduced (r = 0.32, p = 0.13) |
# | fig3b-k-no-correlation | Zenodo | reproduced |
# | figs4-a77636-no-correlation | Zenodo | reproduced |
# | figs6-dreadd-validation | Zenodo | reproduced |
# | fig5cf-cno-locomotion | Zenodo | partially reproduced, resting on an assumption (mCherry mice slower) |
# | fig5g-mcherry-no-change | Zenodo | reproduced |
# | fig5hi-dreadd-fewer-large | Zenodo | partially reproduced (hM4Di significant at 3 s only) |
# | fig5jl-dreadd-params | Zenodo | partially reproduced (hM4Di K rise not significant) |
# | fig6b-ctrl-ppx-stable | Zenodo | reproduced |
# | fig6c-park-ppx-progressive | Zenodo | reproduced |
# | fig6de-a77636-persistent | Zenodo | reproduced |
# | fig4bc, fig4de (2), fig4f, fig4g, fig4 insets, fig4hk, figs5abcd, figs5ef, fig6f, fig6g, figs8, fig6h, fig6i (14 claims) | DANDI:001177 | blocked: data missing |
#
# How the analysis differs from the paper's. The paper's per-mouse spreadsheets of choices were not
# deposited, so every session is recounted from the raw operant logs with the paper's event names.
# The baseline sessions are every baseline session deposited (2 to 5 per mouse), since the CV rule
# finds a stable run in only 12 of 47 PPX mice. The "two-way repeated measures ANOVA" is run with
# each mouse and delay as the unit, the layout the paper's degrees of freedom imply. The open field
# windows assume injection at 20 min. Striatal TH is normalized to the control mice of each staining
# cohort.
#
# What was found about the data.
#
# - DANDI:001177 holds raw voltage, LFP and per-electrode threshold crossings for 18 mice and 56
#   sessions, matching the paper's mice (7 control, 11 parkinsonian, 4 with saline sessions), but no
#   sorted units in 54 files, no unit labels in the other two, no laser pulse times and no injection
#   time, so none of the electrophysiology findings can be tested. Three sessions have start times
#   in 2025, out of order with the same mouse's other days, and the subject descriptions are
#   mis-encoded ("1.5â€¯microliters").
# - In the Zenodo deposit, 233 operant logs are byte-identical between the PPX and DREADD folders
#   and 75 between the A77636 and DREADD folders (mice used in two experiments); one PPX
#   parkinsonian mouse (E6) has no PPX sessions and one mCherry mouse (R5.5) no delay discounting
#   files; the 2020 control cohort ran delays of 0, 6, 12 and 18 s and the 2021 cohort 30 free
#   choice trials per block, unlike the Methods; the open field files carry no injection time; no
#   file gives each mouse's sex; and no PPX open field file is deposited.
"""
open('nb.py','w').write(s)
EOF
grep -c "Result:" $TMPDIR/nb.py
```

```
28
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/w/bin/python - <<'EOF'
s=open('nb.py').read()
for a,b in [
("# | 23 behaviour, histology, rotarod and slice claims | Zenodo 15258978 | tested, except two blocked (sex not recorded; no PPX open field file) |",
 "# | 30 behaviour, histology, rotarod and slice claims | Zenodo 15258978 | 28 tested; two blocked (sex not recorded; no PPX open field file) |"),
("# and 9 s; paired variant p <= 0.0034). With the first PPX session only, three of four delays are\n# significant.",
 "# and 9 s; paired variant p <= 0.0034). With the first PPX session only, two of four delays are\n# significant on the pooled error (three with paired tests)."),
("# (p = 0.078); the printed RM ANOVA reading is above.",
 "# (p = 0.078). Under reading (b), repeated measures ANOVA with Bonferroni, AUC persists (p = 0.039)\n# and K does not (p = 0.063). Neither reading gives all three parts."),
]:
    assert a in s, a[:50]; s=s.replace(a,b)
open('nb.py','w').write(s)
EOF
cd entries/001177-zhuang-2025; $TMPDIR/venv/w/bin/python $TMPDIR/build_notebook.py $TMPDIR/nb.py reproduce_zhuang_2025.ipynb; ls; cat > requirements.in <<'EOF'
fsspec
aiohttp
requests
h5py
remfile
numpy
pandas
scipy
statsmodels
matplotlib
openpyxl
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001177-zhuang-2025
type: reproduction
title: Pramipexole, striatal firing and delay discounting in parkinsonian mice (Zhuang et al. 2025)
description: Tests the findings of Zhuang, Lemak, Sridhar and Nelson (2025) on dandiset 001177 and on
  the paper's Zenodo deposit (doi:10.5281/zenodo.15258978). The dandiset holds raw voltage, LFP and
  threshold crossings of the striatal recordings, without sorted or labelled units, so the
  electrophysiology claims are blocked. The delay discounting, rotarod, open field, histology and
  slice claims are tested on the Zenodo files, recounting every operant session from its raw log.
license: Apache-2.0
notebooks:
- path: reproduce_zhuang_2025.ipynb
  title: Reproducing Zhuang et al. (2025) from DANDI:001177 and its Zenodo deposit
  runtime_minutes: 16
helpers:
- icd.py
related:
- id: dandi:001177/0.250902.2127
  relation: uses_data
- id: doi:10.1093/brain/awaf312
  relation: reproduces
EOF
cat ../001453-fouke-2025/entry.yaml | head -3; grep -n "relation" schemas/entry.schema.json | head
```

```
88 cells
__pycache__
icd.py
reproduce_zhuang_2025.ipynb
schema_version: 1
name: 001453-fouke-2025
type: reproduction
45:        "required": ["id", "relation"],
52:          "relation": {"enum": ["uses_data", "reproduces", "derived_from", "references"]}
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; rm -rf __pycache__; cat >> entry.yaml <<'EOF'
- id: doi:10.5281/zenodo.15258978
  relation: uses_data
EOF
cd  date -u; python -c "import yaml,jsonschema,nbformat" 2>&1; python tools/entry.py lock entries/001177-zhuang-2025 && python tools/entry.py check entries/001177-zhuang-2025
```

```
Wed Oct 28 11:30:50 UTC 2026
wrote entries/001177-zhuang-2025/requirements.lock.txt
0 error(s)
```

**Agent**

Lock and check pass. Running the entry from a clean environment (about 16 minutes).

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/001177-zhuang-2025 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-001177-zhuang-2025 in executed/001177-zhuang-2025/.venv/share/jupyter/kernels/registry-001177-zhuang-2025
0 error(s)
pass  reproduce_zhuang_2025.ipynb  (1059 s)

real	18m9.941s
user	4m13.603s
sys	0m5.948s
Wed Oct 28 11:49:32 UTC 2026
```

**Agent**

Passed from a clean environment in 17.7 minutes. Checking that the executed outputs match the numbers the conclusions quote.

**Agent calls Bash**

```bash
cd  ls executed/001177-zhuang-2025/; $TMPDIR/venv/w/bin/python - <<'EOF'
import nbformat
def outs(p):
    nb=nbformat.read(p,4); r={}
    for c in nb.cells:
        if c.cell_type=='code':
            t=tuple(c.metadata.get('tags',[])); r[(t,c.source[:60])]=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
    return r
a=outs('/tmp/claude-1001/run2.ipynb'); b=outs('executed/001177-zhuang-2025/reproduce_zhuang_2025.ipynb')
for k in b:
    if k in a and a[k]!=b[k] and 'sanity' not in k[0]: print('DIFF',k)
nb=nbformat.read('executed/001177-zhuang-2025/reproduce_zhuang_2025.ipynb',4)
print(sum(1 for c in nb.cells if c.cell_type=='code' for o in c.outputs if o.output_type=='error'),'errors')
EOF
```

```
reproduce_zhuang_2025.ipynb
result.json
0 errors
```

**Agent**

Outputs are identical to my development run, so the conclusions hold. Two wording fixes about the open field tracking gaps, applied to both the source and the executed copy (markdown only).

**Agent calls Bash**

```bash
cd  $TMPDIR/venv/w/bin/python - <<'EOF'
import nbformat
reps=[("# N. R1.1's file has no tracking gap near 20 min.","# N. R1.1's file has long tracking losses before 20 min and its first gap near the injection at 15 min."),
("# criterion needs p >= 0.05. Four files (R0, F0, F3, R1.2) are of mice in no DREADD list, and the\n# 2023 files have no tracking gap, so their injection time rests on the assumption alone.",
 "# criterion needs p >= 0.05. Four files (R0, F0, F3, R1.2) are of mice in no DREADD list, and most\n# 2023 files (H mice) have no tracking gap near 20 min, so their injection time rests on the assumption alone.")]
s=open('/tmp/claude-1001/nb.py').read()
for a,b in reps:
    assert a in s; s=s.replace(a,b)
open('/tmp/claude-1001/nb.py','w').write(s)
p='executed/001177-zhuang-2025/reproduce_zhuang_2025.ipynb'
nb=nbformat.read(p,4)
n=0
for c in nb.cells:
    if c.cell_type=='markdown':
        for a,b in reps:
            a2="\n".join(l[2:] for l in a.splitlines()); b2="\n".join(l[2:] for l in b.splitlines())
            if a2 in c.source: c.source=c.source.replace(a2,b2); n+=1
nbformat.write(nb,p); print(n)
EOF
cd entries/001177-zhuang-2025 && $TMPDIR/venv/w/bin/python $TMPDIR/build_notebook.py $TMPDIR/nb.py reproduce_zhuang_2025.ipynb
```

```
2
88 cells
```

**Agent**

Now the entry README and the attempt record. Checking the attempt schema first.

**Agent calls Bash**

```bash
cd  $TMPDIR/venv/w/bin/python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=0)[:6000])"
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
[... 258 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/venv/w/bin/python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in ['inputs','findings']: print(k, json.dumps(p[k],indent=0)[:2500])
print([k for k in p])
"; sed -n '/^inputs/,/^outcomes/p' attempts/001453-fouke-2025-01.yaml | head -5; grep -n "^findings" -A 30 attempts/001453-fouke-2025-01.yaml | head -40
```

```
inputs {
"description": "Everything the attempt used that is not in the dataset.",
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"what",
"source"
],
"properties": {
"what": {
"type": "string",
"minLength": 1
},
"source": {
"description": "A DOI, or a repository URL with the commit read.",
"type": "string",
"minLength": 1
}
[... 78 more lines not kept]
```

**Agent**

Writing the attempt record (generated from Python so the YAML quoting is safe).

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec; cat > $TMPDIR/rec/make.py <<'PYEOF'
import yaml, re
NB = "reproduce_zhuang_2025.ipynb"
DD_DEV = [
    "Choices, omissions and latencies are recounted from the raw operant logs, as the paper's per-mouse spreadsheets are not deposited, with the event and block names of the paper's code (UCSF-Nelson-Lab/ICD-Cognitive-Analysis at 5528e222, delay_discounting_task.py, processCsv_1; free choice blocks B3, B6, B9, B12).",
    "The two-way 'repeated measures' ANOVA treats each mouse and delay pair as the repeated unit with delay between units, the layout implied by the degrees of freedom the paper prints (F(1, 60) for 16 control mice, F(1, 120) for 31 parkinsonian mice; Figure 1 legend and Table 1); per-delay Bonferroni comparisons use the pooled within-unit error, with paired t tests as a variant.",
    "The six control mice of the 2020 cohort ran delays of 0, 6, 12 and 18 s (their block labels and the measured reward delays agree), and 30 of their sessions have no fourth block; their blocks are counted as the other mice's, as the paper's code does.",
]
BLOCK_EPHYS = ("The dandiset holds raw voltage, LFP and per-electrode threshold crossings only. None of its 56 files "
               "has sorted units with a putative MSN class or an optical label, none has laser pulse times or the "
               "PPX injection time, and the two files with a units table (E0 day 4, P4 day 1) give spike times "
               "only, without the channel, the sorted or unsorted status, or any label. The Zenodo deposit holds "
               "no electrophysiology. The paper's units come from manual sorting in Plexon Offline Sorter and "
               "classification by thresholds it does not give, which cannot be repeated from the files.")
ephys = ["fig4bc-baseline-rates-similar", "fig4de-ctrl-immediate-suppression", "fig4de-ctrl-no-change-4-5h",
         "fig4f-park-dmsn-increase", "fig4g-park-imsn-decrease", "fig4-insets-response-types",
         "fig4hk-modulation-more-marked", "figs5abcd-putative-msns", "figs5ef-saline-no-change",
         "fig6f-ctrl-types-stable", "fig6g-park-types-shift", "figs8-session-trend",
         "fig6h-increase-type-larger", "fig6i-decrease-type-similar"]
ephys_extra = {
    "fig4bc-baseline-rates-similar": "Needs optically identified dMSNs and iMSNs.",
    "fig4de-ctrl-immediate-suppression": "Needs optically identified units and the injection time.",
    "fig4de-ctrl-no-change-4-5h": "Needs optically identified units and the injection time.",
    "fig4f-park-dmsn-increase": "Needs optically identified dMSNs and the injection time.",
    "fig4g-park-imsn-decrease": "Needs optically identified iMSNs and the injection time.",
    "fig4-insets-response-types": "Depends on fig4f and fig4g, and needs optically identified units.",
    "fig4hk-modulation-more-marked": "Needs optically identified units.",
    "figs5abcd-putative-msns": "Needs sorted single units classified as putative MSNs. The files are consistent with the paper's mice (7 control and 11 parkinsonian subjects).",
    "figs5ef-saline-no-change": "Needs sorted putative MSNs; the four saline sessions (mice D0, E0, H1.3, H4.3, as Figure S5E's 4 mice) hold threshold crossings only.",
    "fig6f-ctrl-types-stable": "Needs sorted putative MSNs per session.",
    "fig6g-park-types-shift": "Needs sorted putative MSNs per session.",
    "figs8-session-trend": "Depends on fig6g-park-types-shift.",
    "fig6h-increase-type-larger": "Depends on fig6g-park-types-shift.",
    "fig6i-decrease-type-similar": "Depends on fig6g-park-types-shift.",
}
def o(claim, outcome, notes, deviations=None, measured=None, assumed=None, blocked_by=None, tested=True):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if tested:
        d["notebook"] = NB; d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    if assumed: d["assumed"] = True
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    return d

outcomes = [
 o("fig1b-th-loss", "partially_reproduced",
   "Corrected total fluorescence per ROI, normalized to the control mice of the same staining cohort, in 45 parkinsonian mice (Table 1 gives N = 44). Mean losses are DLS 64.3%, DMS 56.8% and VS 35.3% (medians 66.3, 58.4, 39.7%), so DLS and DMS are outside 50 +/- 5%. Kruskal-Wallis p = 3.4e-08; Dunn DLS against DMS p = 0.38, DLS against VS p < 0.0001, DMS against VS p = 0.0001, so the pattern holds. Normalized to all controls, DLS 60.5% and DMS 52.4% (DMS inside the tolerance), and DMS against VS p = 0.052. The measured value is the mean of the DLS and DMS losses.",
   ["Normalization reference not given beyond 'normalized TH fluorescence levels' (Supplementary methods, Histology); the control mice of the same staining cohort are used, as the deposit README says each cohort includes healthy and parkinsonian samples 'to control for inter-batch staining variability', and all controls pooled is run as a variant. Both readings give a partial outcome.",
    "VS is the mean of the VLS and VMS ROIs of both sides ('VLS and VMS were then combined into ventral striatum (VS)', Supplementary methods); background is the mean of the four background ROIs of each section (same passage)."],
   measured=60.6),
 o("figs1d-snc-cells", "reproduced",
   "TH+ cells over the four sections and both sides divided by the area counted. 29 of 32 mice could be given a group (9 control, 20 parkinsonian; paper 9 and 21); median density 316.0 against 186.6 cells per mm2, Mann-Whitney p = 0.0003. The three unlinked mice (C0.1, C2.1, D5.2) do not change the result in either group (p = 0.0001 and 0.0019).",
   ["The workbook has no group column. Groups are taken from the histology workbook of the same deposit, the README's PPX lists and the DANDI subjects' lesion, in that order.",
    "Two rows (D3 and N4 at -3.51 mm) have shifted count and area columns and are left out."]),
 o("fig1c-rotarod", "reproduced",
   "Medians control 91.3 s (n = 40), parkinsonian before PPX 47.3 s (n = 45), on PPX 66.7 s, second cohort before saline 51.0 s and on saline 62.3 s (n = 27). Kruskal-Wallis over the five columns p = 6.7e-15; Dunn control against parkinsonian p = 1.1e-15, before against PPX p = 1.8e-05, before against saline p = 0.83. Variant (Supplementary methods) Mann-Whitney p = 5e-13, Wilcoxon p = 3e-08 (PPX) and 0.074 (saline).",
   ["The deposited columns are labelled Park_cohort1_baseline and Park_cohort1_PPX, Park_cohort2_baseline and Park_cohort2_Saline; the pre-drug sessions are the baseline columns, as the claim's criterion asks the author to read from the file.",
    "Dunn's comparisons are corrected for the three comparisons the criterion names; the workbook has 40 controls where Table 1 gives 31."]),
 o("figs1ef-ppx-locomotion", "blocked",
   "The Zenodo deposit holds open field velocity for the A77636 and CNO experiments only; no file holds the PPX open field sessions of Figure S1E-F, and the DANDI files hold no behaviour. Recorded as a finding.",
   blocked_by="other", tested=False),
 o("figs1-instrumental-learning", "partially_reproduced",
   "From the workbook's Figure S1H-I and S1K-L sheets (32 control and 81 parkinsonian mice; paper 34 and 81). Blocked learning: parkinsonian success lower in sessions 1, 3 and 4 (Bonferroni p = 0.007, 0.0055, 0.0035), latency longer in sessions 3 to 6 (p = 0.0005 to 0.012). Random learning: success similar in sessions 2 to 6 but different in session 1 (65.9 against 86.9%, p = 0.003), and initiation latency similar in all sessions (p >= 0.13). The criterion's last part, no random session differing, fails on session 1.",
   ["The S1K-L sheet has a second 'Session1_Park' header at row 118, between session 1 and session 2 parkinsonian blocks, with 30 rows; it is read as session 2 control. Without it, random session 2 has no control data."]),
 o("fig1fg-baseline-similar", "reproduced",
   "Reading (a), every deposited baseline session (16 control, 31 parkinsonian mice); group F(1, 178) = 0.007, p = 0.93 (paper F(1, 180) = 0.003, p = 0.96); every per-delay Bonferroni p = 1. Reading (b), the stable-run rule, keeps 12 mice; group p = 0.11, per-delay p >= 0.45. Both readings find no difference.",
   DD_DEV + ["Two control mice of the 2020 cohort have no 9 s block, so error df is 178."]),
 o("fig1fg-delay-discounting", "reproduced",
   "Reading (a); delay F(3, 178) = 38.15, p = 4.3e-19 (paper F(3, 180) = 38.53); delayed/large choices fall from 91.7 to 32.1% (control) and 85.7 to 32.9% (parkinsonian) between 0 and 9 s. Reading (b), 12 mice; the means fall (95.4 to 82.4%, 95.7 to 58.8%) but delay p = 0.11. The criterion is met under reading (a).",
   DD_DEV),
 o("fig1f-ctrl-ppx-no-change", "reproduced",
   "16 control mice. PPX effect p = 0.10 (first session), 0.16 (four sessions) with every baseline, 0.38 and 0.27 with stable baselines (3 mice); paper F(1, 60) = 0.96, p = 0.33. No per-delay Bonferroni comparison reaches p < 0.05 on the pooled error or by paired tests (smallest 0.21). Largest effect 5.5 points at 0 s.",
   DD_DEV),
 o("fig1g-park-ppx-fewer-large", "reproduced",
   "Every baseline and the mean of four PPX sessions, 30 mice; PPX F(1, 116) = 91.46, p = 2.5e-16 (paper F(1, 120) = 95.48); lower at 0, 3, 6 and 9 s by 12.5, 14.7, 9.7 and 6.4 points, Bonferroni p < 0.0001, < 0.0001, 0.0002, 0.022 (paired p <= 0.0034). With the first PPX session, F = 28.56, p = 4.6e-07, two of four delays significant on the pooled error. Mouse E6 has no PPX session in the deposit, so 30 of 31 mice enter.",
   DD_DEV + ["PPX ON is read two ways, as the criterion lists; the outcome rests on the mean of the first four sessions, as Summary_Cognitive.m averages a mouse's sessions within a condition."]),
 o("fig1ijk-ppx-a-k-auc", "partially_reproduced",
   "Four PPX sessions, 30 mice, no failed fit. A falls (median 0.891 to 0.785, Dunn p = 1.9e-06), AUC falls (3.95 to 2.91, p = 2.7e-08), K rises (0.258 to 0.321) without significance (Dunn p = 0.19; Friedman over the three conditions p = 0.032, which is the paper's printed p = 0.03). With the first PPX session, A and AUC fall (p = 0.012, 5.3e-05) and K does not change (p = 1). The same procedure reproduces the paper's A77636 values exactly (Dunn K p = 0.0053, AUC p = 0.0008), so the method matches the paper's; the paper's K result for PPX may come from the Friedman test (asked of the authors).",
   DD_DEV + ["Dunn's comparisons are those against baseline, corrected for two comparisons ('between baseline and PPX ON or OFF conditions', Supplementary methods, Behavior).",
             "PPX OFF is every washout session of the mouse (the claims file gives no reading; Summary_Cognitive.m averages a mouse's sessions within a condition), with the first OFF session as a variant."]),
 o("figs2abc-sex-similar", "blocked",
   "No file of the deposit gives each mouse's sex: the README lists mice by experiment and group only, and the Key Resource Table names strains. The DANDI subjects have a sex, but they are the electrophysiology mice, not the 31 delay discounting mice.",
   blocked_by="metadata_insufficient", tested=False),
 o("figs2de-omissions-low", "reproduced",
   "Four PPX sessions. Parkinsonian center omissions differ only at 6 s (4.5 against 11.7%, Bonferroni p < 0.0001; 0 s p = 1, 3 s p = 0.15, 9 s p = 0.49); PPX main effect F(1, 116) = 24.82, p = 2.2e-06 (paper F(1, 120) = 16.54). Side omissions F(1, 116) = 0.96, p = 0.33 (paper 2.06, p = 0.15) and no per-delay difference (smallest p = 0.94); control comparisons all p >= 0.60. Mean rates in parkinsonian mice 5.0 and 7.8% (center), 1.6 and 1.9% (side) at baseline and on PPX.",
   DD_DEV + ["Omissions are counted in the free choice blocks as a percentage of the block's trials, the code's 'center omi' and 'side omi' events; the PPX sessions are the mean of four, as in fig1g-park-ppx-fewer-large."]),
 o("figs2gh-ppx-latency", "partially_reproduced",
   "Parkinsonian mice. Small-reward latency is shorter on PPX at 0 and 3 s (1.28 to 1.09 s, 1.38 to 1.02 s) but the PPX effect is F(1, 110) = 2.87, p = 0.093 with four sessions and p = 0.15 with the first (paper F(1, 114) = 4.505, p = 0.02). The reward size effect is significant at baseline (F(1, 114) = 5.33, p = 0.023; paper p = 0.0092) and not on PPX (p = 0.71 with four sessions, 0.19 with the first; paper p = 0.70). Two of the criterion's three parts hold.",
   DD_DEV + ["Latency is from the 'cen tri' event (side cue light) to the first side nosepoke of the trial, classed by the reward delivered, per the Supplementary methods' definition; per mouse and condition, the mean over the block's trials and the condition's sessions."]),
 o("figs2ijk-ppx-washout", "partially_reproduced",
   "Four PPX sessions and every washout session, 30 mice. Reading (a), Friedman with Dunn's; A after washout 0.879 against 0.891 at baseline (p = 0.73), K 0.419 against 0.258 (p = 0.020), AUC 3.38 against 3.95 (p = 0.078). Reading (b), repeated measures ANOVA with Bonferroni; A p = 1, K p = 0.063, AUC p = 0.039; ON against OFF A p = 3e-05, K p = 1, AUC p = 0.0011 (Table 1 gives < 0.0001, > 0.99, 0.0019). A recovers and both K and AUC stay on the PPX side of baseline, but neither reading makes both significant.",
   DD_DEV + ["PPX OFF is every washout session of the mouse; with the first ON and first OFF session none of the three differs from baseline (A p = 1, K p = 0.59, AUC p = 0.38)."]),
 o("fig2bc-a77636-locomotion", "reproduced",
   "26 files. The 10 control mice are not faster 30 to 100 min after A77636 (median 3.19 to 2.90 cm/s, Wilcoxon p = 0.065; paper p = 0.16); the other 16 are (3.14 to 3.69 cm/s, 13 of 16 faster, p = 0.016; paper p = 0.02). Six of these 16 (O6, R0, R1, R3.2, R5.3, R6) are in neither A77636 list of the README.",
   ["The files hold time and velocity without an injection mark. Injection is assumed at 20 min after the start, where 24 of 26 files have a short run of untracked frames (20.0 to 20.4 min), consistent with the mouse being lifted for the injection and with a 20 min baseline (-20 to 0 min, the window stated for CNO); a -30 to 0 min baseline does not exist in these files, so the criterion's reading (b) cannot be run.",
    "Mice not in the README's A77636 control list are taken as parkinsonian: the control list is complete in the files (10 of 10) and 16 mice remain, the paper's N."],
   assumed=True),
 o("fig2d-ctrl-a77636-no-change", "reproduced",
   "10 control mice; A77636 effect p = 0.80 and 0.61 (first, four sessions) with every baseline, 0.79 and 0.31 with stable baselines (8 mice); paper F(1, 36) = 1.05, p = 0.31. No per-delay comparison reaches p < 0.05 (smallest pooled p = 0.71).",
   DD_DEV),
 o("fig2e-park-a77636-fewer-large", "reproduced",
   "16 parkinsonian mice, every baseline, four A77636 sessions; F(1, 60) = 45.06, p = 7.7e-09 (paper 45.68); lower at 3, 6 and 9 s by 15.3, 19.0 and 19.3 points (Bonferroni p = 0.0049, 0.0003, 0.0003; paper 0.0047, 0.0003, 0.0002), not at 0 s (p = 0.56; paper 0.57). With the first session, F = 16.85, p = 0.0001, with 6 and 9 s significant.",
   DD_DEV),
 o("fig2fgh-a77636-k-auc", "reproduced",
   "16 mice, four A77636 sessions, every washout session, no failed fit. A unchanged (Friedman p = 0.31, Dunn p = 0.31; paper 0.31), K higher (median 0.115 to 0.291, Dunn p = 0.0053; paper 0.0053), AUC lower (5.82 to 3.97, Dunn p = 0.0008; paper 0.0008). With the first session only, K and AUC are not significant (Dunn p = 0.43, 0.10).",
   DD_DEV + ["Dunn's comparisons against baseline, corrected for two (Supplementary methods, Behavior)."]),
 o("figs3-a77636-washout-latency", "partially_reproduced",
   "K and AUC after washout (0.209, 4.93) do not differ from A77636 (Dunn p = 1 and 0.65, three comparisons; paper 0.96, 0.43) and stay on the A77636 side of baseline (0.115, 5.82; Dunn baseline against OFF p = 0.043 each). No per-delay center or side omission comparison is significant (smallest p = 0.65). The reward size effect on latency is present at baseline (F(1, 52) = 14.70, p = 0.0003; paper F(1, 52) = 11.70, p = 0.0012) and also on A77636 (F(1, 56) = 4.84, p = 0.032; paper p = 0.07), where the criterion requires p >= 0.05.",
   DD_DEV),
 o("fig3a-a-correlates-dms", "not_reproduced",
   "A on PPX (four sessions) against normalized DMS TH in the 24 parkinsonian mice with both measures (paper 28); r = 0.32, p = 0.13, outside 0.51 +/- 0.051. DLS r = 0.23 (p = 0.29) and VS r = 0.28 (p = 0.18). Normalized to all controls, DMS r = 0.14 (p = 0.52).",
   DD_DEV + ["TH as in fig1b-th-loss (per staining cohort), A as in fig1ijk-ppx-a-k-auc. Mice are matched by their identifiers in the two workbooks; 24 of the 30 PPX mice have histology."],
   measured=0.32),
 o("fig3b-k-no-correlation", "reproduced",
   "K on PPX against TH, n = 24; DMS r = 0.03 (p = 0.89), DLS r = 0.40 (p = 0.056), VS r = 0.32 (p = 0.13). With all controls as reference, p = 0.70, 0.060, 0.068. None is significant.",
   DD_DEV),
 o("figs4-a77636-no-correlation", "reproduced",
   "A and K on A77636 against TH in 16 mice; all six p >= 0.24, the smallest K against VS (r = -0.31, p = 0.24; paper r = -0.31, p = 0.23).",
   DD_DEV),
 o("figs6-dreadd-validation", "reproduced",
   "oIPSC amplitude 647.5 to 55.0 pA (median, 6 cells, Wilcoxon p = 0.031); firing at 300 pA 8 to 16 Hz (9 cells, p = 0.016); CNO effect on the input-output curve (100 to 400 pA) F(1, 32) = 17.64, p = 0.0002, the paper's values, with each cell and current as the repeated unit. An ordinary two-way ANOVA gives p = 0.082.",
   ["The input-output ANOVA uses the layout of the delay discounting ANOVA, which the paper's F(1, 32) for 9 cells and 4 currents implies."]),
 o("fig5cf-cno-locomotion", "partially_reproduced",
   "hM3Dq mice move faster 20 to 30 min after CNO (median 2.20 to 4.35 cm/s, 11 of 11, Wilcoxon p = 0.001) and hM4Di mice too (3.83 to 6.13 cm/s, 9 of 10, p = 0.004); mCherry mice move slower (2.96 to 2.23 cm/s, 1 of 12 faster, p = 0.016), where the criterion needs p >= 0.05. Four files (R0, F0, F3, R1.2) are of mice in no DREADD list and are left out.",
   ["Injection is assumed at 20 min after the start of each file, as in fig2bc-a77636-locomotion; most 2023 files (H mice) have no tracking gap near 20 min, so for them the time rests on the assumption alone."],
   assumed=True),
 o("fig5g-mcherry-no-change", "reproduced",
   "14 mCherry mice with delay discounting files (README lists 15; R5.5 has none). CNO effect F(1, 52) = 0.94, p = 0.34 (paper F(1, 56) = 0.97, p = 0.33); stable baselines (7 mice) p = 0.34; every per-delay p = 1.",
   DD_DEV + ["Post-CNO sessions are averaged per mouse over the first four CNO sessions ('Post CNO administration sessions were averaged per animal across four CNO treatment sessions', Supplementary methods, Chemogenetic manipulation)."]),
 o("fig5hi-dreadd-fewer-large", "partially_reproduced",
   "hM3Dq (12 mice); CNO F(1, 44) = 40.94, p = 8.8e-08 (paper 42.30), lower at 3, 6 and 9 s (p = 0.0006, 0.0013, 0.026). hM4Di (12 mice); F(1, 44) = 12.77, p = 0.0009 (paper 22.22), lower at 3 s only (p = 0.022; 6 s p = 0.38, 9 s p = 0.62). The criterion's partial case holds (one group).",
   DD_DEV),
 o("fig5jl-dreadd-params", "partially_reproduced",
   "Reading (a), Wilcoxon (Table 1). hM3Dq; A 0.923 to 0.880 (p = 0.012), K 0.133 to 0.198 (p = 0.0015), AUC 5.10 to 4.31 (p = 0.0005). hM4Di; A unchanged (p = 0.20), AUC 6.08 to 5.78 (p = 0.043), K 0.123 to 0.136 (7 of 12 higher, p = 0.20). mCherry; no change (p >= 0.36). Reading (b), Friedman, reduces to a sign test with two conditions and finds fewer effects (hM4Di AUC p = 0.15). Eight of the nine parts hold under reading (a); the K rise in hM4Di does not. The criterion names a partial outcome for K and AUC holding with the A pattern failing; it does not name this case, and the outcome is recorded as partial because the effects hold in part.",
   DD_DEV),
 o("fig6b-ctrl-ppx-stable", "reproduced",
   "Control mice, 12 of 16 with a fourth PPX session; baseline against first p = 0.46, against fourth p = 0.75, first against fourth p = 1 (paper p > 0.99), Bonferroni on condition means; per-delay first against fourth all p = 1.",
   DD_DEV + ["The first-against-fourth test compares condition means pooled over delays, with Bonferroni over the three pairs ('the 1st and 4th PPX injections were compared across different delays using two-way repeated measures ANOVA, followed by Bonferroni multiple comparisons', Supplementary methods, Behavior); per-delay comparisons are shown as a variant."]),
 o("fig6c-park-ppx-progressive", "reproduced",
   "27 of 31 parkinsonian mice with four PPX sessions; delayed/large choices 50.7% at baseline, 41.6% first and 36.2% fourth session; baseline against first p = 2.7e-05, against fourth p = 2.7e-11, first against fourth p = 0.024 (paper p < 0.0081). No single delay differs between first and fourth (smallest p = 0.19).",
   DD_DEV),
 o("fig6de-a77636-persistent", "reproduced",
   "Parkinsonian (16 mice); baseline against first p = 0.0004, against fourth p < 0.0001, first against fourth p = 1 (paper 0.59). Control (10 mice); p = 1, 0.31, 0.48 (paper first against fourth 0.49).",
   DD_DEV),
]
for c in ephys:
    outcomes.append(o(c, "blocked", BLOCK_EPHYS + " " + ephys_extra[c], blocked_by="data_missing", tested=False))

findings = [
 {"kind": "data_missing", "statement": "DANDI:001177 holds, for 18 mice and 56 sessions, the 30 kHz voltage, the 1 kHz LFP and per-electrode threshold crossings with their waveforms, which are the input to the paper's manual spike sorting. It holds none of what the paper's electrophysiology analysis used; sorted single units (54 files have none), their putative MSN class, their optical identification, the laser pulse times and the PPX injection time. None of the 14 electrophysiology findings (Figures 4, 6F-I, S5, S8) can be tested."},
 {"kind": "metadata_insufficient", "statement": "Two files (sub-E0 PPX day 4, sub-P4 PPX day 1) have a units table with spike times and unit names only. Even-numbered and odd-numbered units differ by about two orders of magnitude in spike count in E0, consistent with an unsorted and a sorted cluster per channel, but no column gives the channel, the sorted status, the MSN class or an optical label."},
 {"kind": "metadata_error", "statement": "Three sessions have start times in 2025 (sub-H0-2 days 3 and 4, 2025-07-31 and 2025-07-30, out of day order; sub-H4-3 day 3, 2025-05-23) while the same mice's other days are from 2023, likely the conversion date."},
 {"kind": "metadata_error", "statement": "The subject descriptions are mis-encoded ('1.5â€¯microliters', a UTF-8 narrow space decoded twice), and the genotype is written 'Drd1a-Cre' in sub-E0's PPX sessions and 'Drd1aCre' elsewhere."},
 {"kind": "data_missing", "statement": "In the paper's Zenodo deposit (doi:10.5281/zenodo.15258978), the PPX open field data of Figure S1E-F are absent; parkinsonian mouse E6 has baseline but no PPX or washout delay discounting sessions; and mCherry mouse R5.5, listed in the README, has no delay discounting file."},
 {"kind": "metadata_insufficient", "statement": "In the Zenodo deposit, no file gives each mouse's sex (Figure S2A-C cannot be tested); the open field files carry no injection time (24 of 26 A77636 files show a tracking gap at 20 min, taken as the injection); six A77636 and four CNO open field mice are in no group list of the README; and the SNc cell count workbook has no group column, so three of its 32 mice cannot be placed."},
 {"kind": "selection_undocumented", "statement": "The deposit holds 2 to 5 baseline sessions per mouse, and the Methods' stability rule (CV < 20% in 3 blocks over three sessions or in all blocks over two) finds a stable run in only 12 of 47 PPX mice among them. Which baseline sessions entered the figures is not stated; using all deposited baselines gives the paper's statistics closely (delay F = 38.15 against 38.53)."},
 {"kind": "other", "statement": "Not all sessions follow the Methods' task. The 2020 cohort of six control PPX mice (P1 to P7) ran delays of 0, 6, 12 and 18 s, as both its block labels and the measured reward delays show, and 30 of its sessions have no fourth block; the 2021 cohort (C mice) ran 30 free choice trials per block, the Methods 20. The paper's code counts them with the others."},
 {"kind": "other", "statement": "233 operant logs are byte-identical between the PPX and DREADD folders of the cognitive assay zip, and 75 between the A77636 and DREADD folders; they are the baseline sessions of mice used in two experiments, deposited twice."},
 {"kind": "metadata_error", "statement": "In the Zenodo workbook Data_ICD_FigS1_SNcTH_CellCounting_RawImages.xlsx, the Figure S1K&L sheet labels two blocks 'Session1_Park' (rows 35 and 118), the second presumably session 2 control, and two rows of the Figure S1D sheet (D3 and N4 at -3.51 mm) have their count and area columns shifted. The rotarod workbook has 40 control mice where Table 1 gives 31."},
 {"kind": "methods_unavailable", "statement": "Questions for the authors. (1) When was the drug injected in each open field file (A77636 and CNO)? This attempt assumed 20 min after the start, where most files lose tracking briefly. (2) Was striatal TH normalized to the control mice of each staining cohort or to all controls? The DMS loss is 56.8% one way and 52.4% the other. (3) Which test gives p = 0.03 for the PPX effect on K in Figure 1J? Dunn's comparison of baseline against PPX ON gives p = 0.19 here, the Friedman test over three conditions p = 0.032, while the same procedure reproduces the A77636 Dunn's p-values exactly."},
]

rec = {
 "schema_version": 2,
 "id": "001177-zhuang-2025-01",
 "dataset": {"archive": "dandi", "id": "001177", "version": "0.250902.2127", "doi": "10.48324/dandi.001177/0.250902.2127"},
 "paper": "doi:10.1093/brain/awaf312",
 "date": "2026-10-28",
 "entry": "001177-zhuang-2025",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-12"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/40671825405"}},
 "inputs": [
  {"what": "The paper's deposit of its behaviour, histology, rotarod, open field and slice data (operant logs, Excel workbooks, velocity files and READMEs with the mouse lists), on which every data-elsewhere claim is tested. One version exists.",
   "source": "doi:10.5281/zenodo.15258978"},
  {"what": "The paper's analysis code, read for the event and block names of the operant logs and the hyperbolic fit (re-implemented in icd.py, not run).",
   "source": "https://github.com/UCSF-Nelson-Lab/ICD-Cognitive-Analysis at commit 5528e2229f186e0785a676ae6f15219c47146930"},
 ],
 "outcomes": outcomes,
 "findings": findings,
}
txt = yaml.safe_dump(rec, sort_keys=False, width=100, allow_unicode=True)
open("attempts/001177-zhuang-2025-01.yaml", "w").write(txt)
print(len(outcomes), "outcomes")
PYEOF
cd  && $TMPDIR/venv/w/bin/python $TMPDIR/rec/make.py && grep -c "claim:" claims/001177/*.yaml; grep -c "^- id:" claims/001177/*.yaml; python tools/entry.py check entries/001177-zhuang-2025
```

```
44 outcomes
0
44
0 error(s)
```

**Agent**

Record written and the entry check passes. One count to correct (25 of 26 open field files show the 20 min gap, not 24), then a scan for ": " in the YAML text.

**Agent calls Bash**

```bash
cd  sed -i 's/where 24 of 26 files have a short run of untracked frames (20.0 to 20.4 min)/where 25 of 26 files have a short run of untracked frames (20.0 to 20.3 min)/; s/(24 of 26 A77636 files show a tracking gap at 20 min/(25 of 26 A77636 files show a tracking gap at 20 min/' $TMPDIR/rec/make.py && $TMPDIR/venv/w/bin/python $TMPDIR/rec/make.py && grep -n "24 of 26\|25 of 26" attempts/001177-zhuang-2025-01.yaml | head; grep -n ': .*: ' attempts/001177-zhuang-2025-01.yaml | grep -v "^\s*[0-9]*:\s*- \(what\|kind\)" | head; $TMPDIR/venv/w/bin/python -c "
import yaml; d=yaml.safe_load(open('attempts/001177-zhuang-2025-01.yaml'))
from collections import Counter; print(Counter(o['outcome'] for o in d['outcomes'])); print(Counter(o.get('blocked_by') for o in d['outcomes'] if o['outcome']=='blocked'))"
```

```
44 outcomes
276:    start, where 25 of 26 files have a short run of untracked frames (20.0 to 20.3 min), consistent with
632:    open field files carry no injection time (25 of 26 A77636 files show a tracking gap at 20 min, taken
195:  notes: 'No file of the deposit gives each mouse''s sex: the README lists mice by experiment and group
Counter({'reproduced': 18, 'blocked': 16, 'partially_reproduced': 9, 'not_reproduced': 1})
Counter({'data_missing': 14, 'other': 1, 'metadata_insufficient': 1})
```

**Agent calls Bash**

```bash
cd  $TMPDIR/venv/w/bin/python -c "
import yaml; d=yaml.safe_load(open('attempts/001177-zhuang-2025-01.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+'/'+str(i))
    elif isinstance(x,str) and (': ' in x or x.startswith((\"'\",'\"'))): 
        import re; print(p, [x[max(0,m.start()-30):m.start()+10] for m in re.finditer(': ',x)])
walk(d)"
```

```
/outcomes/4/notes ['r 34 and 81). Blocked learning: parkinso', '005 to 0.012). Random learning: success ']
/outcomes/10/notes ["deposit gives each mouse's sex: the READ"]
/outcomes/14/deviations/1 ['list are taken as parkinsonian: the cont']
```

**Agent calls Bash**

```bash
cd  sed -i 's/Blocked learning: parkinsonian success/In blocked learning, parkinsonian success/; s/Random learning: success similar/In random learning, success is similar/; s/No file of the deposit gives each mouse'"'"'s sex: the README lists/No file of the deposit gives each mouse'"'"'s sex. The README lists/; s/list are taken as parkinsonian: the control list/list are taken as parkinsonian, because the control list/' $TMPDIR/rec/make.py && $TMPDIR/venv/w/bin/python $TMPDIR/rec/make.py && grep -c "^  notes: '" attempts/001177-zhuang-2025-01.yaml; grep -n "notes: '\|- '" attempts/001177-zhuang-2025-01.yaml | head
```

```
44 outcomes
0
```

**Agent**

Now the entry README.

**Agent calls Write**

```json
{
 "file_path": "entries/001177-zhuang-2025/README.md",
 "content": "# Zhuang, Lemak, Sridhar & Nelson (2025) from DANDI:001177 and its Zenodo deposit\n\nTests the findings of [Zhuang et al. (2025)](https://doi.org/10.1093/brain/awaf312) on\n[DANDI:001177](https://dandiarchive.org/dandiset/001177/0.250902.2127), which holds the striatal\nrecordings of Figures 4, 6 and S5 and S8, and on the paper's\n[Zenodo deposit](https://doi.org/10.5281/zenodo.15258978), which holds its behaviour, histology,\nrotarod and slice data.\n\nThe dandiset holds raw voltage, LFP and per-electrode threshold crossings for the paper's 18 mice,\nbut no sorted units, unit classes, optical labels, laser times or injection times, so the 14\nelectrophysiology claims are blocked. Of the 30 claims on the Zenodo data, 28 are tested, each\noperant session recounted from its raw log.\n\n| Claims | Outcome |\n|---|---|\n| Delay discounting at baseline, under PPX and A77636, after washout, with repeated dosing (12 claims) | 10 reproduced, 2 partially reproduced |\n| Hyperbolic fit parameters A, K and AUC (PPX, A77636, DREADD) | 1 reproduced, 2 partially reproduced |\n| Omissions and choice latencies (3 claims) | 1 reproduced, 2 partially reproduced |\n| DREADD delay discounting (mCherry, hM4Di, hM3Dq) | 1 reproduced, 1 partially reproduced |\n| Rotarod, SNc cell counts, slice validation | 3 reproduced |\n| Striatal TH loss | Partially reproduced |\n| Correlations of A and K with TH (3 claims) | 2 reproduced, 1 not reproduced |\n| Instrumental learning | Partially reproduced |\n| Open field after A77636 and after CNO | 1 reproduced, 1 partially reproduced (both assume the injection time) |\n| Sex differences; PPX open field | Blocked: sex not recorded; no PPX open field file |\n| Electrophysiology (14 claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/001177-zhuang-2025-01.yaml`](../../attempts/001177-zhuang-2025-01.yaml).\n\n- `reproduce_zhuang_2025.ipynb`: the analysis. It takes about 18 minutes, most of it opening the 56\n  NWB files to list their contents and reading the open field workbooks.\n- `icd.py`: listing the dandiset, reading the Zenodo files, parsing the operant logs with the event\n  names of the paper's code, the hyperbolic fit, and the statistics. Other notebooks on these data\n  can import it.\n"
}
```

```
File created successfully at: entries/001177-zhuang-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001177-zhuang-2025; $TMPDIR/venv/w/bin/python - <<'EOF'
s=open('README.md').read()
old=s[s.index("| Delay discounting at baseline"):s.index("| DREADD delay discounting")]
new="""| Delayed/large choices at baseline, under PPX and A77636, and over repeated dosing (9 claims) | 9 reproduced |
| Washout, omissions and choice latencies (4 claims) | 1 reproduced, 3 partially reproduced |
| Hyperbolic fit parameters A, K and AUC (PPX, A77636, DREADD) | 1 reproduced, 2 partially reproduced |
"""
s=s.replace(old,new); open('README.md','w').write(s)
EOF
grep -n "^|" README.md; cd  python tools/entry.py check entries/001177-zhuang-2025; date -u
```

```
14:| Claims | Outcome |
15:|---|---|
16:| Delayed/large choices at baseline, under PPX and A77636, and over repeated dosing (9 claims) | 9 reproduced |
17:| Washout, omissions and choice latencies (4 claims) | 1 reproduced, 3 partially reproduced |
18:| Hyperbolic fit parameters A, K and AUC (PPX, A77636, DREADD) | 1 reproduced, 2 partially reproduced |
19:| DREADD delay discounting (mCherry, hM4Di, hM3Dq) | 1 reproduced, 1 partially reproduced |
20:| Rotarod, SNc cell counts, slice validation | 3 reproduced |
21:| Striatal TH loss | Partially reproduced |
22:| Correlations of A and K with TH (3 claims) | 2 reproduced, 1 not reproduced |
23:| Instrumental learning | Partially reproduced |
24:| Open field after A77636 and after CNO | 1 reproduced, 1 partially reproduced (both assume the injection time) |
25:| Sex differences; PPX open field | Blocked: sex not recorded; no PPX open field file |
26:| Electrophysiology (14 claims) | Blocked: data missing |
0 error(s)
Wed Oct 28 11:53:26 UTC 2026
```

**Agent**

Check passes. Building the verifier's handover package.

**Agent calls Bash**

```bash
cd  rm -rf entries/001177-zhuang-2025/__pycache__; python tools/entry.py handover entries/001177-zhuang-2025 2>&1 | tail -5; ls -R executed/001177-zhuang-2025/handover | head; git status --short
```

```
wrote executed/001177-zhuang-2025/handover
executed/001177-zhuang-2025/handover:
10.1093-brain-awaf312.yaml
icd.py
reproduce_zhuang_2025.ipynb
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
?? attempts/001177-zhuang-2025-01.yaml
?? entries/001177-zhuang-2025/
?? scripts
```

**Agent**

The handover is built. Some untracked dotfiles and a `scripts` folder appeared in the repository root that I did not create; checking what they are before deciding anything.

**Agent calls Bash**

```bash
cd  ls -la .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc scripts .idea .vscode 2>&1 | head -30
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 28 10:23 scripts
```

**Agent calls Bash**

```bash
cd  $TMPDIR/venv/w/bin/python - <<'EOF'
import nbformat
a="# consistent with an injection after the first 30 min, but this is not stated in the files."
b=a+"\n# No session has a trial or event table, so whether the streams share a trial clock cannot be\n# established for any electrophysiology session; this is moot here, as no claim on them is tested."
s=open('/tmp/claude-1001/nb.py').read(); assert a in s; open('/tmp/claude-1001/nb.py','w').write(s.replace(a,b))
p='executed/001177-zhuang-2025/reproduce_zhuang_2025.ipynb'
nb=nbformat.read(p,4); a2=a[2:]; b2="\n".join(l[2:] for l in b.splitlines()); n=0
for c in nb.cells:
    if c.cell_type=='markdown' and a2 in c.source: c.source=c.source.replace(a2,b2); n+=1
nbformat.write(nb,p); print(n)
EOF
cd entries/001177-zhuang-2025 && $TMPDIR/venv/w/bin/python $TMPDIR/build_notebook.py $TMPDIR/nb.py reproduce_zhuang_2025.ipynb && cd ../.. && python tools/entry.py check entries/001177-zhuang-2025 && python tools/entry.py handover entries/001177-zhuang-2025 | tail -1; $TMPDIR/venv/w/bin/python -c "
import nbformat
a=nbformat.read('entries/001177-zhuang-2025/reproduce_zhuang_2025.ipynb',4); b=nbformat.read('executed/001177-zhuang-2025/reproduce_zhuang_2025.ipynb',4)
print(len(a.cells),len(b.cells), sum(x.source!=y.source for x,y in zip(a.cells,b.cells)),'cells differ in source')"; date -u
```

```
1
88 cells
0 error(s)
wrote executed/001177-zhuang-2025/handover
88 88 0 cells differ in source
Wed Oct 28 11:54:38 UTC 2026
```

**Agent**

All six author steps are done. The entry checks and runs from a clean environment, the attempt record is written, and the handover is built in `executed/001177-zhuang-2025/handover/`. Nothing is committed.

## 1. Outcomes (44 claims)

| Claim | Outcome |
|---|---|
| fig1fg-baseline-similar, fig1fg-delay-discounting, fig1f-ctrl-ppx-no-change, fig1g-park-ppx-fewer-large | reproduced |
| fig2d-ctrl-a77636-no-change, fig2e-park-a77636-fewer-large, fig2fgh-a77636-k-auc | reproduced |
| fig6b-ctrl-ppx-stable, fig6c-park-ppx-progressive, fig6de-a77636-persistent | reproduced |
| figs2de-omissions-low, fig5g-mcherry-no-change | reproduced |
| fig1c-rotarod, figs1d-snc-cells, figs6-dreadd-validation | reproduced |
| fig3b-k-no-correlation, figs4-a77636-no-correlation | reproduced |
| fig2bc-a77636-locomotion | reproduced (rests on an assumption) |
| fig1ijk-ppx-a-k-auc | partially reproduced: the rise in K is not significant by Dunn's test (p = 0.19) |
| figs2ijk-ppx-washout | partially reproduced |
| figs2gh-ppx-latency | partially reproduced |
| figs3-a77636-washout-latency | partially reproduced |
| fig1b-th-loss | partially reproduced: losses of 64% (DLS) and 57% (DMS) against 50 ± 5% |
| figs1-instrumental-learning | partially reproduced |
| fig5hi-dreadd-fewer-large | partially reproduced |
| fig5jl-dreadd-params | partially reproduced |
| fig5cf-cno-locomotion | partially reproduced (rests on an assumption) |
| fig3a-a-correlates-dms | not reproduced: r = 0.32, p = 0.13 against the paper's 0.51 |
| figs2abc-sex-similar | blocked (metadata_insufficient): no file gives each mouse's sex |
| figs1ef-ppx-locomotion | blocked (other): no PPX open field file was deposited |
| 14 electrophysiology claims (Figures 4, S5, 6F–I, S8) | blocked (data_missing) |

Totals: 18 reproduced, 9 partially reproduced, 1 not reproduced, 16 blocked.

Where the method could be checked, it matches the paper exactly. The A77636 Dunn's p-values (0.0053 and 0.0008) and the slice input-output result F(1, 32) = 17.64 come out identical to the paper's.

## 2. What was found about the data

**The dandiset (DANDI:001177, pinned at 0.250902.2127, the only published version):**
- It holds the paper's 18 mice (7 control, 11 parkinsonian) in 56 sessions: raw 30 kHz voltage, LFP and per-electrode threshold crossings.
- It has no sorted units, unit classes, optical labels, laser pulse times or injection times, so no electrophysiology claim can be tested.
- Two files have a `units` table with spike times only and no labels.
- Three sessions have start times in 2025, out of order with the same mice's other days.
- The subject descriptions are mis-encoded ("1.5â€¯microliters").

**The Zenodo deposit (doi:10.5281/zenodo.15258978), which holds all the tested data:**
- Mouse E6 has no PPX sessions, mouse R5.5 has no delay discounting files, and the PPX open field data are absent.
- Some logs are deposited twice: 233 are byte-identical between the PPX and DREADD folders, and 75 between the A77636 and DREADD folders.
- Two cohorts ran a different task from the Methods: the 2020 control cohort used delays of 0, 6, 12 and 18 s, and the 2021 cohort ran 30 free-choice trials per block instead of 20.
- The open field files have no injection mark.
- The SNc and instrumental-learning workbooks have labelling and column-shift errors.
- The Methods' stability rule passes only 12 of 47 mice on the deposited baseline sessions, so which baselines the paper used is undocumented.

**Assumptions** (marked `assumed: true` on fig2bc and fig5cf):
- Injection is taken at 20 min into each open field file, where 25 of 26 A77636 files lose tracking briefly.
- Mice missing from the A77636 control list are counted as parkinsonian; that leaves 16, the paper's N.

Other choices did not change any outcome: TH normalized per staining cohort (normalizing to all controls is also shown), and the drug-OFF condition averaging every washout session, following the paper's code.

**Questions for the paper's authors** (recorded as a `methods_unavailable` finding):
1. When was the drug injected in each open field file?
2. Was striatal TH normalized to the controls of each staining cohort or to all controls?
3. Which test gives p = 0.03 for the PPX effect on K? Dunn's test gives 0.19 here; the Friedman test gives 0.032.

**Questions to a reader:** none.

## 3. Protocol gaps

1. A claim marked `data: elsewhere` whose data are not public anywhere (figs1ef) cannot be blocked as `data_missing`, because the entry check rejects it. I used `other` and recorded a `data_missing` finding.
2. Findings are defined as being about the dataset, but most findings here concern the outside deposit. I recorded them and labelled each as Zenodo.
3. Group labels for data elsewhere had to come from other files in the same deposit (the README lists, the histology workbook) or from the DANDI subjects. Link claims seem meant only for matching outside data to the dataset, so I added none and recorded the sources as deviations.
4. For fig5jl the criterion defines a partial outcome only for a case that did not occur. I recorded it as partial (the effects hold in part) and explained this in the notes.
5. When a claim's criterion says "as" another claim's, it is unclear whether that claim's readings carry over. For figs2de I used the four-session reading.
6. One expected value covered two quantities (fig1b, "DLS and DMS"). I recorded their mean as `measured` and gave both values in the notes.
7. archives.md has no Zenodo section. I streamed the files into memory with fsspec, as the CRCNS section describes.
8. The clock check could not be done for the electrophysiology because no session has trial or event tables. The notebook says so. For the behaviour data, the check confirmed that the block delays and the event times are consistent.

## 4. Runtime and failures

- The run went from 10:25 to 11:55 UTC.
- The notebook takes 17.7 minutes from a clean environment, over the 10-minute aim but under the 30-minute limit. Most of the time goes to opening all 56 NWB files and reading the open field workbooks.
- Nothing failed.
- After the final run I edited three markdown sentences (two wording fixes and the clock-check sentence) in both the source and the executed copy. I confirmed the two have identical cell sources and re-ran the check and the handover after the edits.
- The untracked dotfiles in the repository root are `/dev/null` mounts the sandbox created before this run. I left them alone.

## End of run

86 turns, 85 minutes, result: success.
