# memar-2026 · author · run 44898633044

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (63.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/bee3ce62-1c90-4b85-bc6b-9e3b53905afe/tool-results/bev87dfij.txt

Preview (first 2KB):
Sat Nov 21 11:26:00 UTC 2026
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
cat README.md | head -100; wc -l docs/design.md docs/archives.md; ls paper; cat claims/memar-2026.yaml; cat papers/datasets/memar-2026.yaml; ls papers/author-notes | grep memar
```

```
<persisted-output>
Output too large (40.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/bee3ce62-1c90-4b85-bc6b-9e3b53905afe/tool-results/bl58a6y3y.txt

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
ls paper; wc -c paper/*; cat papers/datasets/memar-2026.yaml; ls papers/author-notes | grep memar; ls questions | grep memar
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/memar-2026.yaml"
}
```

```
1	# Claims for Ostadsharif Memar & Dehghani (2026), "Spatially Masked Regression Reveals Local and
2	# Distributed Predictability in Electrophysiological Recordings", doi:10.48550/arxiv.2606.11415.
3	#
4	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-21, protocol as stated in docs/protocol.md (pilot-18), Reader role.
6	#
7	# Text read. The arXiv preprint, version 1 (arXiv:2606.11415v1, dated 11 June 2026), full text as
8	# stored under paper/ (paper/10.48550-arxiv.2606.11415.txt, "Version: preprint"): main text,
9	# Material and Methods (sections II A to II H, Algorithms 1 to 4), Results, Discussion, and the
10	# appendix Tables II (iEEG) and III (EEG) and Figure 6. The paper has no separate supplement and
11	# cites none. No version of record was available. The PDF was not needed; the table values were
12	# read from the text, row by row in the column order the headers give.
13	#
14	# Code read. GitHub neurovium/SpatiallyMaskedRegression (linked in the paper's footnote and Code
15	# Availability), commit 244dcdbd67f217873c2a52b77485d97c6fa9bf0e (2026-06-24, after the preprint's
16	# date). It holds the model (ReconModel.py, model.py), intra-subject training and the EEG
17	# cross-subject path (train.py, main.py), the iEEG cross-subject path (similarity.py,
18	# generate_adj_matrix_ieeg_unseen.py, Test_new_subject_iEEG.py), the coverage experiment
19	# (run_coverage_experiment.py), surrogates (Load_preprocess_data.py), the neighborhood and mask
20	# (neighborhood.py), settings (configs/settings.yaml), a METHODS.md map from the paper to the code,
[... 517 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p paper/10.48550-arxiv.2606.11415.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 400,1100p paper/10.48550-arxiv.2606.11415.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1100,1500p paper/10.48550-arxiv.2606.11415.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "DANDI" -A60 docs/archives.md | head -120; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
```

```
4:the DANDI Archive. The protocol is written for any archive. What is particular
5-to an archive (how its datasets are named, versioned and read) is here, and an
6-agent is pointed to its archive's section.
7-
8-A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
9:`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
10-`transcripts/`, the `attempt/` branch, the paper store) are under its folder
11:name: the identifier alone for DANDI, which the registry began with, and
12-`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
13-below), and `tools/datasets.py` turns one form of a dataset's name into another.
14-The workflows take a dataset in any of these forms.
15-
16:## DANDI
17-
18-- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
19-  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
20:  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
21-- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
22-  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
23-  paper cites, or the latest published one. For a draft, record its
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -150; cat entries/fouke-2025/README.md | head -30
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
[... 159 more lines not kept]
```

**Agent**

Now the dataset. Let me survey DANDI:000055.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000055/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/?page_size=100" | python -c "
import json,sys
d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['path'], round(a['size']/1e9,1))
"; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/" | python -c "
import json,sys; d=json.load(sys.stdin); print(d.get('doi')); print(d['description'][:3000]); print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q wenv --python 3.12 2>&1 | tail -2; source wenv/bin/activate; uv pip install -q pynwb remfile h5py numpy scipy pandas torch --index-url https://pypi.org/simple --extra-index-url https://download.pytorch.org/whl/cpu 2>&1 | tail -3; python -c "import torch, pynwb; print(torch.__version__, pynwb.__version__)"; cat tools/entry.py | grep -n "python" | head -20
```

```
2.15.0+cpu 4.2.0
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
206:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
208:                         f"says {entry['python']}; run `tools/entry.py lock`")
467:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
470:def python_of(entry_dir: Path) -> str:
471:    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
474:    if entry.get("python"):
475:        return str(entry["python"])
484:def set_python(entry_dir: Path, version: str) -> None:
485:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
488:    line = f'python: "{version}"'
489:    if re.search(r"^python:.*$", text, re.M):
490:        text = re.sub(r"^python:.*$", line, text, count=1, flags=re.M)
500:    version = version or python_of(entry_dir)
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source wenv/bin/activate && cat > survey.py <<'EOF'
import remfile, h5py, pynwb, time, requests
t=time.time()
aid="7b9e2ca1-9097-488a-b4e9-ac407fb31457"
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
f=h5py.File(remfile.File(url),"r")
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True)
nwb=io.read()
print(nwb)
for k,v in nwb.acquisition.items(): print(k, v, getattr(v,'data',None) is not None and v.data.shape, getattr(v,'data',None) is not None and v.data.chunks)
for k,m in nwb.processing.items():
    for n,d in m.data_interfaces.items(): print(k,n,type(d).__name__)
print(nwb.electrodes.to_dataframe().head()); print(nwb.electrodes.colnames)
for k,v in nwb.intervals.items(): print(k, v.colnames); print(v.to_dataframe().head(10))
print(time.time()-t)
EOF
python survey.py 2>&1 | tail -80
```

```
Fields:
  comments: no comments
  conversion: nan
  data: <HDF5 dataset "data": shape (43200000,), type "<f4">
  description: Electrooculography for tracking saccades - left
  offset: 0.0
  rate: 500.0
  resolution: -1.0
  starting_time: 0.0
  starting_time_unit: seconds
  unit: V
 (43200000,) None
EOGR EOGR pynwb.base.TimeSeries at 0x124515221044448
Fields:
  comments: no comments
  conversion: nan
  data: <HDF5 dataset "data": shape (43200000,), type "<f4">
  description: Electrooculography for tracking saccades - right
  offset: 0.0
  rate: 500.0
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source wenv/bin/activate && cat > survey2.py <<'EOF'
import remfile, h5py, pynwb, time, requests, numpy as np
aid="7b9e2ca1-9097-488a-b4e9-ac407fb31457"
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
f=h5py.File(remfile.File(url),"r")
d=f["acquisition/ElectricalSeries/data"]
print(d.compression, d.compression_opts, d.chunks, d.dtype)
r=f["intervals/reaches"]; print(len(r["start_time"]))
st=r["start_time"][:]; print(st[:5], np.diff(st).min())
print(list(f["processing/behavior"].keys()))
ev=f["processing/behavior/ReachEvents"]; print(list(ev.keys()), ev["timestamps"].shape, ev.attrs.get("description"))
print(ev["timestamps"][:10])
print(ev["data"][:10] if "data" in ev else None)
ep=f["intervals/epochs"]; import collections
lab=[x.decode() if isinstance(x,bytes) else x for x in ep["labels"][:]]; print(collections.Counter(lab))
t=time.time(); x=d[int(st[3]*500)-500:int(st[3]*500)+500,:]; print("read",time.time()-t, x.shape)
el=f["general/extracellular_ephys/electrodes"]; print({k:el[k][:5] for k in el.keys() if k not in ('group',)})
EOF
python survey2.py 2>&1 | tail -40
```

```
gzip 4 (84375, 1) float32
156
[ 1791.954  3520.224  3584.342 26884.645 27984.897] 2.4660000000003492
['Position', 'ReachEvents']
['timestamps'] (156,) r_wrist
[ 1791.954  3520.224  3584.342 26884.644 27984.896 28768.352 28853.918
 29639.048 31409.66  31434.982]
None
Counter({'Blocklist (Data break)': 714, 'Sleep/rest': 293, 'Talk': 105, 'TV': 92, 'Blocklist (Experiment)': 88, 'Blocklist (Private time)': 35, 'Talk, TV': 24, 'Computer/phone': 16, 'Inactive': 15, 'Blocklist (Tether/bandage)': 13, 'Eat, TV': 12, 'Eat, Talk': 11, 'Other activity': 6, 'Blocklist (Camera move/zoom)': 2, '': 1})
read 1.2005383968353271 (1000, 94)
{'filtering': array([b'250 Hz lowpass', b'250 Hz lowpass', b'250 Hz lowpass',
       b'250 Hz lowpass', b'250 Hz lowpass'], dtype=object), 'good': array([False,  True,  True,  True,  True]), 'group_name': array([b'GRID', b'GRID', b'GRID', b'GRID', b'GRID'], dtype=object), 'high_freq_R2': array([-0.00110715, -0.01904136, -0.00323491, -0.0133427 , -0.01421174]), 'id': array([0, 1, 2, 3, 4]), 'imp': array([nan, nan, nan, nan, nan]), 'kurtosis': array([6.15478128, 1.30933177, 1.58515443, 2.65256404, 2.62686694]), 'location': array([b'unknown', b'unknown', b'unknown', b'unknown', b'unknown'],
      dtype=object), 'low_freq_R2': array([ 0.01310574, -0.00472891, -0.00322645,  0.03600192,  0.09638015]), 'median_deviation': array([28.97865005, 48.2471422 , 31.0778001 , 28.65150912, 51.30115885]), 'standard_deviation': array([35.39853467, 55.51872672, 33.99200802, 33.70126142, 59.64846978]), 'x': array([-45.64849509, -47.34715172, -50.29140891, -51.35896118,
       -51.21981805]), 'y': array([38.56037242, 31.1828614 , 22.15720826, 11.78726768,  1.71388884]), 'z': array([36.18796239, 41.17679881, 45.19188514, 48.72650925, 53.00098123])}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source wenv/bin/activate && cat > survey3.py <<'EOF'
import remfile, h5py, requests, numpy as np, json
from concurrent.futures import ThreadPoolExecutor
assets=requests.get("https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/?page_size=100").json()["results"]
def one(a):
    url=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=False).headers["Location"]
    f=h5py.File(remfile.File(url),"r")
    d=f["acquisition/ElectricalSeries/data"]
    st=f["intervals/reaches/start_time"][:]
    ev=f["processing/behavior/ReachEvents/timestamps"][:]
    el=f["general/extracellular_ephys/electrodes"]
    loc=[x.decode() for x in el["location"][:]]
    good=el["good"][:]
    gn=[x.decode() for x in el["group_name"][:]]
    es=f["acquisition/ElectricalSeries"]
    return a["path"], d.shape, len(st), len(ev), int(good.sum()), len(set(loc)), sorted(set(gn)), es["data"].attrs.get("conversion"), f["session_start_time"][()]
with ThreadPoolExecutor(16) as ex:
    for r in sorted(ex.map(one, assets)): print(r)
EOF
python survey3.py 2>&1 | tail -60
```

```
('sub-01/sub-01_ses-3_behavior+ecephys.nwb', (43200000, 94), 156, 156, 85, 1, ['GRID', 'LAT', 'LID', 'LMT', 'LPT', 'LTO'], np.float64(1e-06), b'2000-01-02T19:00:00-05:00')
('sub-01/sub-01_ses-4_behavior+ecephys.nwb', (43200000, 94), 196, 196, 91, 1, ['GRID', 'LAT', 'LID', 'LMT', 'LPT', 'LTO'], np.float64(1e-06), b'2000-01-03T19:00:00-05:00')
('sub-01/sub-01_ses-5_behavior+ecephys.nwb', (43200000, 94), 199, 199, 91, 1, ['GRID', 'LAT', 'LID', 'LMT', 'LPT', 'LTO'], np.float64(1e-06), b'2000-01-04T19:00:00-05:00')
('sub-01/sub-01_ses-7_behavior+ecephys.nwb', (27858793, 94), 190, 190, 91, 1, ['GRID', 'LAT', 'LID', 'LMT', 'LPT', 'LTO'], np.float64(1e-06), b'2000-01-07T03:31:22.414000-05:00')
('sub-02/sub-02_ses-3_behavior+ecephys.nwb', (43200000, 86), 51, 51, 85, 1, ['GRID', 'RDA', 'RDP', 'RST'], np.float64(1e-06), b'2000-01-02T19:00:00-05:00')
('sub-02/sub-02_ses-4_behavior+ecephys.nwb', (43200000, 86), 94, 94, 85, 1, ['GRID', 'RDA', 'RDP', 'RST'], np.float64(1e-06), b'2000-01-03T19:00:00-05:00')
('sub-02/sub-02_ses-5_behavior+ecephys.nwb', (43200000, 86), 82, 82, 81, 1, ['GRID', 'RDA', 'RDP', 'RST'], np.float64(1e-06), b'2000-01-04T19:00:00-05:00')
('sub-02/sub-02_ses-6_behavior+ecephys.nwb', (43200000, 86), 78, 78, 80, 1, ['GRID', 'RDA', 'RDP', 'RST'], np.float64(1e-06), b'2000-01-05T19:00:00-05:00')
('sub-03/sub-03_ses-3_behavior+ecephys.nwb', (43200000, 96), 198, 198, 79, 1, ['GRID', 'LAD', 'LAT', 'LMT', 'LPD'], np.float64(1e-06), b'2000-01-02T19:00:00-05:00')
('sub-03/sub-03_ses-4_behavior+ecephys.nwb', (43200000, 96), 193, 193, 71, 1, ['GRID', 'LAD', 'LAT', 'LMT', 'LPD'], np.float64(1e-06), b'2000-01-03T19:00:00-05:00')
('sub-03/sub-03_ses-5_behavior+ecephys.nwb', (43200000, 96), 137, 137, 76, 1, ['GRID', 'LAD', 'LAT', 'LMT', 'LPD'], np.float64(1e-06), b'2000-01-04T19:00:00-05:00')
('sub-03/sub-03_ses-6_behavior+ecephys.nwb', (43200000, 96), 114, 114, 79, 1, ['GRID', 'LAD', 'LAT', 'LMT', 'LPD'], np.float64(1e-06), b'2000-01-05T19:00:00-05:00')
('sub-04/sub-04_ses-3
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && git clone -q https://github.com/neurovium/SpatiallyMaskedRegression smr 2>&1 | tail -2; cd smr && git checkout -q 244dcdbd67f217873c2a52b77485d97c6fa9bf0e && ls -R | head -50
```

```
Sat Nov 21 11:28:39 UTC 2026
.:
CITATION.cff
LICENSE
Load_preprocess_data.py
METHODS.md
README.md
ReconModel.py
Test_new_subject_iEEG.py
__pycache__
configs
generate_adj_matrix_ieeg_unseen.py
main.py
model.py
neighborhood.py
notebooks
path.py
run_coverage_experiment.py
setting.py
similarity.py
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && cat configs/settings.yaml ReconModel.py; sed -n 1,400p train.py
```

```
# ============================================================================
# SMR experiment configuration
# ============================================================================
#
# This file is loaded by ``fixed/setting.py::Settings.load_settings``. All
# keys must match a property on the ``Settings`` class; unknown keys are
# rejected.

# ---- Dataset / mode --------------------------------------------------------
# dataset_type:
#   'EEG' / 'iEEG'                           -- real recordings
#   'Surrogate_EEG' / 'Surrogate_iEEG'       -- phase-shuffled surrogates
#   'IAAFT_EEG'     / 'IAAFT_iEEG'           -- IAAFT surrogates
#   'Block_EEG'     / 'Block_iEEG'           -- block-shuffled surrogates
dataset_type: 'EEG'

# mode: 'train', 'test_new', 'compare', 'Evaluate_dandiset'.
mode: 'train'

# Number of subjects in the experiment.
[... 533 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && cat Load_preprocess_data.py | head -250; grep -n "def " utils.py visualize.py neighborhood.py similarity.py model.py
```

```
"""
Subject loaders and surrogate generators.

For real data, this module loads the pickled per-subject arrays produced
by the user's preprocessing pipeline. For surrogate experiments it loads
the original signal and then applies one of three surrogate procedures
(phase-shuffle, IAAFT, block-shuffle) channel by channel.

Paths to the preprocessed data come from ``Paths`` (see ``fixed/path.py``)
and so are configurable via ``configs/device_path.yaml``.
"""

from __future__ import annotations

import pickle as pkl

import numpy as np


# ---------------------------------------------------------------------------
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && sed -n 60,330p utils.py; sed -n 55,200p visualize.py; sed -n 100,260p neighborhood.py; sed -n 55,150p model.py
```

```
cleaned[k.replace('_Settings__', '')] = v
        else:
            cleaned[k] = v
    os.makedirs(file_path, exist_ok=True)
    with open(os.path.join(file_path, 'settings.json'), 'w') as f:
        json.dump(cleaned, f, indent=4, default=str)


# ---------------------------------------------------------------------------
# iEEG preprocessing
# ---------------------------------------------------------------------------
def preprocess_iEEG(data: np.ndarray,
                    fs: float = 1000,
                    band: tuple = (0.5, 150),
                    notch_freq: float = 60,
                    notch_q: float = 30,
                    new_fs: Optional[float] = None,
                    zscore: bool = True,
                    artifact_thresh: float = 5,
                    rereference: bool = True,
[... 632 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source wenv/bin/activate && cat > rt.py <<'EOF'
import remfile, h5py, requests, numpy as np, time
from concurrent.futures import ProcessPoolExecutor
aid="7b9e2ca1-9097-488a-b4e9-ac407fb31457"
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
def init():
    global d
    d=h5py.File(remfile.File(url),"r")["acquisition/ElectricalSeries/data"]
def read(t):
    i=int(round(t*500)); return d[i-1500:i+1500,:]
if __name__=="__main__":
    st=h5py.File(remfile.File(url),"r")["intervals/reaches/start_time"][:]
    for nw in (8,16):
        t=time.time()
        with ProcessPoolExecutor(nw, initializer=init) as ex:
            out=list(ex.map(read, st[(nw//8)*40:(nw//8)*40+40]))
        print(nw, time.time()-t, out[0].shape)
EOF
python rt.py
```

```
8 6.839201927185059 (3000, 94)
16 5.069077968597412 (3000, 94)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/smr && sed -n 1,200p similarity.py | sed -n 40,185p; grep -n "zscore\|mean(\|nanmean\|split" Test_new_subject_iEEG.py generate_adj_matrix_ieeg_unseen.py | head -40
```

```
Sat Nov 21 11:30:14 UTC 2026

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------
def _concat_trials(data: np.ndarray) -> np.ndarray:
    """Concatenate trials within a subject.

    Parameters
    ----------
    data : ndarray of shape (n_trials, n_channels, n_time)

    Returns
    -------
    ndarray of shape (n_channels, n_trials * n_time)
        A single 1-D time series per channel.
    """
    if data.ndim != 3:
        raise ValueError(
            f"Expected (n_trials, n_channels, n_time); got shape {data.shape}."
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && sed -n 60,200p Test_new_subject_iEEG.py; sed -n 1,80p generate_adj_matrix_ieeg_unseen.py | grep -v "^#" | head -80
```

```
adj_norm = np.zeros_like(adj)
    for i in range(adj.shape[0]):
        row_min = np.min(adj[i, :])
        row_max = np.max(adj[i, :])
        if row_max != row_min:
            adj_norm[i, :] = (adj[i, :] - row_min) / (row_max - row_min)
        else:
            adj_norm[i, :] = adj[i, :]
    return adj_norm


# ---------------------------------------------------------------------------
# Main evaluation function
# ---------------------------------------------------------------------------
def run_cross_subject_eval(settings, paths, fs: Optional[int] = None) -> None:
    """Evaluate every (src, dst) cross-subject reconstruction and write
    per-electrode DistCorr scores plus comparison plots.

    Parameters
    ----------
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source wenv/bin/activate && uv pip install -q dcor numba 2>&1|tail -1; python -c "
import dcor, numpy as np, time
x=np.random.randn(1000); y=x+np.random.randn(1000)
t=time.time()
for _ in range(200): a=dcor.distance_correlation(x,y,method='mergesort')
print((time.time()-t)/200, a, dcor.distance_correlation(x,y,method='naive'))
X=np.random.randn(2000,1000); Y=X+np.random.randn(2000,1000)
t=time.time(); r=dcor.rowwise(dcor.distance_correlation, X, Y, method='mergesort'); print(time.time()-t, r[:3])
"
```

```
0.00039070844650268555 0.6566861971266383 0.65668619712664
1.0113685131072998 [0.64884983 0.68752774 0.67402897]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/memar-2026/smr.py",
 "content": "\"\"\"Loading and measures for testing Ostadsharif Memar & Dehghani (2026), \"Spatially Masked\nRegression\", on AJILE12 (DANDI:000055).\n\nWhere each parameter comes from:\n\n- Trials. 2 s windows centred on the start of each wrist movement event of the `reaches` table\n  (the same times as processing/behavior/ReachEvents), every session of a subject pooled. Claims\n  file, opening comment, \"Which movement events\", reading (a), and \"Which recording days\".\n- Preprocessing. The steps and their order are the paper's (Methods II A a): DC removal and linear\n  detrending, 0.5 to 150 Hz Butterworth band-pass, 60 Hz notch, 120 Hz low-pass, |z| > 5 replaced\n  by the channel median, common average reference, per-channel z-scoring across time. Filter\n  orders (4th-order Butterworth, zero phase with filtfilt; notch Q = 30) are the paper's code\n  (utils.preprocess_iEEG), which the claims file read. The code's median filter and Hilbert\n  envelope are left out, as the claims file says.\n  Where preprocessing is applied is open (claims file, readings a and b):\n  (a) `continuous`: the paper's order (preprocess, then segment). The whole recording is 16 GB a\n      file, so each event is read with 5 s of padding on each side, filtered, and cut to its\n      centre; the statistics of the |z| > 5 step and of the z-scoring are taken over all the\n      event windows of the session, standing in for the whole recording. An approximation of\n      reading (a), stated as such.\n  (b) `epoch`: every step applied to each 2 s epoch on its own.\n- Electrodes. All electrodes; none excluded (claims file, \"Trial and electrode exclusion\").\n- Neighbourhood. The 9 electrodes nearest in the (x, z) projection of the MNI coordinates, the\n  electrode itself excluded (Methods II B).\n- Mask. ceil(m |N(i)|) neighbours drawn at random and masked with i (Results III D); `round` is\n  the code's variant (neighborhood.find_index_mask).\n- Model and training. Eq. 1 with a bias; loss mean absolute error + 1e-5 L1 + 1e-4 squared L2 on\n  all parameters with the bias (Eq. 2, Methods II F); Adam (betas 0.9, 0.999, eps 1e-8, PyTorch's\n  defaults, which the code uses), learning rate 0.01, batches of 32 trials, patience 200 epochs on\n  the epoch-averaged validation loss, at most 10000 epochs, best validation checkpoint kept\n  (claims file, from configs/settings.yaml and train.py). Weights start uniform in\n  +-1/sqrt(fan_in), as PyTorch's nn.Linear (standard choice). All electrodes are trained at once\n  as independent rows of one weight matrix; Adam's updates are per parameter and each row's loss\n  is its own, so this is the same as one model per electrode, except that the batches are shared.\n  `decim` keeps every k-th time sample of each trial for the gradient steps and the validation\n  loss (a speed deviation, stated in the notebook); the test score uses every sample.\n- Split. z-score across trials (each channel and time sample), then 64/16/20 by two nested 80/20\n  random splits (Methods II D 1; sklearn train_test_split with random_state 42 in the code).\n- Score. Distance correlation (Eqs. 8 to 14) per test trial, averaged over trials; computed with\n  the exact O(n log n) algorithm of the `dcor` package (the same V-statistic as the paper's\n  double-centred matrices).\n- Lagged model. Lags 0, 20, 30, 50, 60 ms, offsets ceil(tau fs / 1000) samples, zero before the\n  trial start (Methods II E, Eq. 6; model.LaggedReconModelConfigurable). One bias in place of the\n  code's one per lag (a standard choice; a sum of biases is one bias).\n- Surrogates. Per trial and channel (Algorithm 4; Load_preprocess_data): phase permutation with\n  Hermitian symmetry and DC kept (shuffle_phase), IAAFT with 5 iterations (iaaft_1d), blocks of\n  0.5 s (block_shuffle_1d default).\n- Cross-subject (Methods II D 2, Algorithm 2; Test_new_subject_iEEG.py): see `cross_subject`.\n\"\"\"\nfrom __future__ import annotations\n\nimport math\nimport os\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\nfrom scipy import signal\nfrom scipy.optimize import linear_sum_assignment\n\nDANDISET = \"000055\"\nVERSION = \"0.220127.0436\"\nAPI = \"https://api.dandiarchive.org/api\"\nFS = 500.0\nHALF = 500          # samples on each side of the event: 2 s trials\nPAD = 2500          # 5 s of padding for reading (a)\nL1, L2 = 1e-5, 1e-4\nLAGS_MS = (0, 20, 30, 50, 60)\n\n\n# ----------------------------------------------------------------------------- archive\ndef assets():\n    \"\"\"Every asset of the pinned version: list of dicts with path, asset_id, size.\"\"\"\n    out, url = [], f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    while url:\n        r = requests.get(url, timeout=60).json()\n        out += r[\"results\"]\n        url = r[\"next\"]\n    return sorted(out, key=lambda a: a[\"path\"])\n\n\ndef s3_url(asset_id):\n    r = requests.get(f\"{API}/assets/{asset_id}/download/\", allow_redirects=False, timeout=60)\n    return r.headers[\"Location\"]\n\n\ndef open_nwb(asset_id):\n    return h5py.File(remfile.File(s3_url(asset_id)), \"r\")\n\n\n# ----------------------------------------------------------------------------- preprocessing\n_B_BP = signal.butter(4, [0.5 / (FS / 2), 150 / (FS / 2)], btype=\"band\")\n_B_NOTCH = signal.iirnotch(60 / (FS / 2), 30)\n_B_LP = signal.butter(4, 120 / (FS / 2), btype=\"low\")\n\n\ndef filter_steps(x):\n    \"\"\"DC removal, linear detrend, band-pass, notch and low-pass on (time, channels).\"\"\"\n    x = x - x.mean(axis=0)\n    x = signal.detrend(x, axis=0, type=\"linear\")\n    x = signal.filtfilt(*_B_BP, x, axis=0)\n    x = signal.filtfilt(*_B_NOTCH, x, axis=0)\n    x = signal.filtfilt(*_B_LP, x, axis=0)\n    return x\n\n\ndef stat_steps(x, mean, std, med):\n    \"\"\"|z| > 5 replaced by the channel median, common average reference, z-score across time.\n\n    x: (..., time, channels); mean, std, med: per channel statistics of the filtered signal.\n    \"\"\"\n    x = x.copy()\n    z = np.abs((x - mean) / std)\n    x = np.where(z > 5, med, x)\n    x = x - x.mean(axis=-1, keepdims=True)\n    return x\n\n\n_WORKER = {}\n\n\ndef _init_worker(url):\n    _WORKER[\"d\"] = h5py.File(remfile.File(url), \"r\")[\"acquisition/ElectricalSeries/data\"]\n\n\ndef _read_event(i0):\n    \"\"\"One event: the filtered padded centre (reading a) and the filtered bare epoch (reading b).\"\"\"\n    d = _WORKER[\"d\"]\n    raw = d[i0 - HALF - PAD:i0 + HALF + PAD, :].astype(np.float64)\n    bad = ~np.isfinite(raw).all(axis=0)\n    raw = np.nan_to_num(raw)\n    a = filter_steps(raw)[PAD:PAD + 2 * HALF]\n    b = filter_steps(raw[PAD:PAD + 2 * HALF])\n    return a.astype(np.float32), b.astype(np.float32), bad\n\n\ndef load_session(asset_id, workers=16):\n    \"\"\"Events of one session, preprocessed under both readings.\n\n    Returns dict with 'a' and 'b' (trials, channels, time) float32, the event times kept, the\n    number of events dropped at the file's edges and the channels holding non-finite values.\n    \"\"\"\n    url = s3_url(asset_id)\n    f = h5py.File(remfile.File(url), \"r\")\n    n_samp = f[\"acquisition/ElectricalSeries/data\"].shape[0]\n    t = f[\"intervals/reaches/start_time\"][:]\n    i0 = np.round(t * FS).astype(int)\n    keep = (i0 - HALF - PAD >= 0) & (i0 + HALF + PAD <= n_samp)\n    with ProcessPoolExecutor(workers, initializer=_init_worker, initargs=(url,)) as ex:\n        res = list(ex.map(_read_event, i0[keep]))\n    a = np.stack([r[0] for r in res])            # (trials, time, ch)\n    b = np.stack([r[1] for r in res])\n    bad = np.any([r[2] for r in res], axis=0)\n    # reading (a): statistics over all event windows of the session\n    flat = a.reshape(-1, a.shape[-1])\n    mean, std, med = flat.mean(0), flat.std(0), np.median(flat, 0)\n    a = stat_steps(a, mean, std, med)\n    flat = a.reshape(-1, a.shape[-1])\n    a = (a - flat.mean(0)) / flat.std(0)\n    # reading (b): every statistic within the epoch\n    mean, std, med = b.mean(1, keepdims=True), b.std(1, keepdims=True), np.median(b, 1, keepdims=True)\n    b = stat_steps(b, mean, std, med)\n    b = (b - b.mean(1, keepdims=True)) / b.std(1, keepdims=True)\n    return dict(a=np.ascontiguousarray(a.transpose(0, 2, 1), dtype=np.float32),\n                b=np.ascontiguousarray(b.transpose(0, 2, 1), dtype=np.float32),\n                times=t[keep], dropped=int((~keep).sum()), bad=bad)\n\n\ndef electrodes(asset_id):\n    \"\"\"Electrode table of one file as a dict of arrays.\"\"\"\n    f = open_nwb(asset_id)\n    el = f[\"general/extracellular_ephys/electrodes\"]\n    out = {}\n    for k in (\"x\", \"y\", \"z\", \"good\", \"location\", \"group_name\"):\n        v = el[k][:]\n        out[k] = np.array([s.decode() for s in v]) if v.dtype.kind == \"O\" else v\n    return out\n\n\n# ----------------------------------------------------------------------------- neighbourhood\ndef neighbours(xyz, k=9):\n    \"\"\"N(i): the k electrodes nearest to i in the (x, z) projection, i excluded (Methods II B).\"\"\"\n    p = xyz[:, [0, 2]]\n    d = np.sqrt(((p[:, None, :] - p[None, :, :]) ** 2).sum(-1))\n    np.fill_diagonal(d, np.inf)\n    return np.argsort(d, axis=1, kind=\"stable\")[:, :k]\n\n\ndef mask_matrix(nbr, m, rng, rule=\"ceil\", mode=\"mask\"):\n    \"\"\"Boolean (N, N) matrix of allowed predictors: True where j may predict i.\n\n    mode 'mask': i and ceil(m |N|) random neighbours excluded (Results III D).\n    mode 'local': only N(i) allowed (Results III E, \"Local\").\n    \"\"\"\n    n = nbr.shape[0]\n    allow = np.ones((n, n), bool)\n    if mode == \"local\":\n        allow[:] = False\n        for i in range(n):\n            allow[i, nbr[i]] = True\n        return allow\n    k = nbr.shape[1]\n    n_mask = math.ceil(m * k - 1e-9) if rule == \"ceil\" else int(round(m * k))\n    for i in range(n):\n        allow[i, i] = False\n        if n_mask:\n            allow[i, rng.choice(nbr[i], n_mask, replace=False)] = False\n    return allow\n\n\n# ----------------------------------------------------------------------------- data split\ndef zscore_trials(x):\n    \"\"\"z-score each channel and time sample across trials (scipy.stats.zscore, axis 0).\"\"\"\n    sd = x.std(0)\n    sd[sd == 0] = 1\n    return ((x - x.mean(0)) / sd).astype(np.float32)\n\n\ndef split_64_16_20(n, seed=42):\n    \"\"\"Two nested 80/20 splits as sklearn train_test_split(..., random_state=seed).\"\"\"\n    from sklearn.model_selection import train_test_split\n    idx = np.arange(n)\n    trval, te = train_test_split(idx, test_size=0.2, random_state=seed)\n    tr, va = train_test_split(trval, test_size=0.2, random_state=seed)\n    return tr, va, te\n\n\n# ----------------------------------------------------------------------------- model\ndef lag_samples():\n    return [math.ceil(t / 1000 * FS - 1e-9) for t in LAGS_MS]\n\n\ndef features(x, lagged=False):\n    \"\"\"(trials, ch, time) -> (trials, time, ch * n_lags) predictors, zero before trial start.\"\"\"\n    xt = x.transpose(0, 2, 1)\n    if not lagged:\n        return xt\n    out = np.zeros(xt.shape[:2] + (xt.shape[2] * len(LAGS_MS),), np.float32)\n    n = xt.shape[2]\n    for k, s in enumerate(lag_samples()):\n        if s == 0:\n            out[:, :, :n] = xt\n        else:\n            out[:, s:, k * n:(k + 1) * n] = xt[:, :-s]\n    return out\n\n\ndef fit_smr(x, tr, va, allow, rng, lagged=False, decim=1, lr=0.01, batch=32, patience=200,\n            max_epoch=10000):\n    \"\"\"Train every electrode's masked linear model with Adam and early stopping.\n\n    x: (trials, ch, time) z-scored across trials. allow: (ch, ch) predictors allowed.\n    Returns weights W (ch, ch * n_lags), biases b (ch,), and the epoch at which each row's best\n    validation loss was reached.\n    \"\"\"\n    n = x.shape[1]\n    nl = len(LAGS_MS) if lagged else 1\n    A = np.tile(allow, (1, nl)).astype(np.float32)\n    fan = A.sum(1, keepdims=True)\n    bound = 1 / np.sqrt(fan)\n    W = (rng.uniform(-1, 1, (n, n * nl)) * bound * A).astype(np.float32)\n    b = (rng.uniform(-1, 1, (n, 1)) * bound).astype(np.float32).ravel()\n    Xf = features(x, lagged)[:, ::decim]             # (trials, time', ch * nl)\n    Y = x.transpose(0, 2, 1)[:, ::decim]              # (trials, time', ch)\n    Xva, Yva = Xf[va].reshape(-1, n * nl), Y[va].reshape(-1, n)\n    mW, vW = np.zeros_like(W), np.zeros_like(W)\n    mb, vb = np.zeros_like(b), np.zeros_like(b)\n    b1, b2, eps = 0.9, 0.999, 1e-8\n    best = np.full(n, np.inf)\n    bestW, bestb = W.copy(), b.copy()\n    best_ep = np.zeros(n, int)\n    wait = np.zeros(n, int)\n    step = 0\n    for ep in range(max_epoch):\n        order = rng.permutation(tr)\n        for s in range(0, len(order), batch):\n            idx = order[s:s + batch]\n            Xb = Xf[idx].reshape(-1, n * nl)\n            Yb = Y[idx].reshape(-1, n)\n            R = Xb @ W.T + b - Yb\n            G = np.sign(R) / R.shape[0]\n            gW = (G.T @ Xb + L1 * np.sign(W) + 2 * L2 * W) * A\n            gb = G.sum(0) + L1 * np.sign(b) + 2 * L2 * b\n            step += 1\n            c1, c2 = 1 - b1 ** step, 1 - b2 ** step\n            mW = b1 * mW + (1 - b1) * gW\n            vW = b2 * vW + (1 - b2) * gW * gW\n            W -= (lr * (mW / c1) / (np.sqrt(vW / c2) + eps)).astype(np.float32)\n            mb = b1 * mb + (1 - b1) * gb\n            vb = b2 * vb + (1 - b2) * gb * gb\n            b -= (lr * (mb / c1) / (np.sqrt(vb / c2) + eps)).astype(np.float32)\n        val = np.abs(Xva @ W.T + b - Yva).mean(0)\n        better = val < best\n        best[better] = val[better]\n        bestW[better], bestb[better] = W[better], b[better]\n        best_ep[better] = ep\n        wait[better] = 0\n        wait[~better] += 1\n        if (wait >= patience).all():\n            break\n    return bestW, bestb, best_ep, ep + 1\n\n\ndef predict(x, W, b, lagged=False):\n    \"\"\"Reconstruction (trials, ch, time) from the full-rate predictors.\"\"\"\n    Xf = features(x, lagged)\n    return (Xf @ W.T + b).transpose(0, 2, 1)\n\n\ndef dcor_rows(u, v):\n    \"\"\"Distance correlation of each row pair (Eqs. 8 to 14); 0 where a row is constant.\"\"\"\n    import dcor\n    u = np.ascontiguousarray(u, dtype=np.float64)\n    v = np.ascontiguousarray(v, dtype=np.float64)\n    out = np.asarray(dcor.rowwise(dcor.distance_correlation, u, v, method=\"mergesort\"))\n    const = (u.std(1) == 0) | (v.std(1) == 0)\n    out[const] = 0.0\n    return np.nan_to_num(out)\n\n\ndef score(x, xhat, te):\n    \"\"\"Per-electrode mean over test trials of the per-trial DistCorr.\"\"\"\n    n = x.shape[1]\n    u = x[te].reshape(-1, x.shape[2])\n    v = xhat[te].reshape(-1, x.shape[2])\n    return dcor_rows(u, v).reshape(len(te), n).mean(0)\n\n\ndef run_smr(x, nbr, m, seed, *, lagged=False, decim=1, rule=\"ceil\", mode=\"mask\", split_seed=42,\n            max_epoch=10000):\n    \"\"\"One intra-subject SMR run. x: preprocessed trials (trials, ch, time), not yet z-scored\n    across trials. Returns per-electrode test DistCorr, W, b, and fit diagnostics.\"\"\"\n    rng = np.random.default_rng(seed)\n    xz = zscore_trials(x)\n    tr, va, te = split_64_16_20(len(x), split_seed)\n    allow = mask_matrix(nbr, m, rng, rule=rule, mode=mode)\n    W, b, best_ep, n_ep = fit_smr(xz, tr, va, allow, rng, lagged=lagged, decim=decim,\n                                   max_epoch=max_epoch)\n    xhat = predict(xz[te], W, b, lagged)\n    dc = score(xz[te], xhat, np.arange(len(te)))\n    return dict(dc=dc, W=W, b=b, best_ep=best_ep, n_ep=n_ep, allow=allow)\n\n\n# ----------------------------------------------------------------------------- surrogates\ndef shuffle_phase(sig, rng):\n    \"\"\"Load_preprocess_data.shuffle_phase, with a seeded generator.\"\"\"\n    n = len(sig)\n    F = np.fft.fft(sig)\n    amp, ph = np.abs(F), np.angle(F)\n    half = n // 2\n    pos = np.arange(1, half)\n    rp = rng.permutation(ph[pos])\n    ph2 = ph.copy()\n    ph2[pos] = rp\n    ph2[-pos] = -rp\n    return np.fft.ifft(amp * np.exp(1j * ph2)).real\n\n\ndef iaaft(sig, rng, n_iter=5):\n    \"\"\"Load_preprocess_data.iaaft_1d, with a seeded generator.\"\"\"\n    s = np.sort(sig)\n    mag = np.abs(np.fft.fft(sig))\n    z = rng.permutation(sig)\n    for _ in range(n_iter):\n        Z = np.fft.fft(z)\n        zn = np.fft.ifft(mag * np.exp(1j * np.angle(Z))).real\n        z = s[np.argsort(np.argsort(zn))]\n    return z\n\n\ndef block_shuffle(sig, rng, block=250):\n    \"\"\"Load_preprocess_data.block_shuffle_1d with 0.5 s blocks at 500 Hz.\"\"\"\n    nb = len(sig) // block\n    rem = len(sig) % block\n    blocks = [sig[i * block:(i + 1) * block] for i in range(nb)]\n    out = np.concatenate([blocks[i] for i in rng.permutation(nb)])\n    return np.concatenate([out, sig[-rem:]]) if rem else out\n\n\ndef surrogate(x, kind, rng):\n    \"\"\"Surrogate of every trial and channel independently (Algorithm 4).\"\"\"\n    fn = dict(phase=shuffle_phase, iaaft=iaaft, block=block_shuffle)[kind]\n    out = np.empty_like(x)\n    for t in range(x.shape[0]):\n        for c in range(x.shape[1]):\n            out[t, c] = fn(x[t, c].astype(np.float64), rng)\n    return out\n\n\n# ----------------------------------------------------------------------------- cross-subject\ndef corr_matrix_paired(xs, xd):\n    \"\"\"Eq. 3: Pearson correlation of target electrode i and donor electrode j on paired trials\n    1..min(R_s, R_s'), averaged over trials, NaN trials left out. xs, xd: (trials, ch, time).\"\"\"\n    r = min(len(xs), len(xd))\n    acc = np.zeros((xs.shape[1], xd.shape[1]))\n    cnt = np.zeros_like(acc)\n    for t in range(r):\n        a = xs[t] - xs[t].mean(1, keepdims=True)\n        c = xd[t] - xd[t].mean(1, keepdims=True)\n        na, nc = np.linalg.norm(a, axis=1), np.linalg.norm(c, axis=1)\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            C = (a @ c.T) / np.outer(na, nc)\n        ok = np.isfinite(C)\n        acc[ok] += C[ok]\n        cnt += ok\n    with np.errstate(invalid=\"ignore\"):\n        return acc / cnt\n\n\ndef corr_matrix_concat(xs, xd):\n    \"\"\"The code's variant (similarity.cross_subject_pearson): trial-concatenated series, truncated\n    to the common length.\"\"\"\n    a = xs.transpose(1, 0, 2).reshape(xs.shape[1], -1)\n    c = xd.transpose(1, 0, 2).reshape(xd.shape[1], -1)\n    L = min(a.shape[1], c.shape[1])\n    a, c = a[:, :L], c[:, :L]\n    a = a - a.mean(1, keepdims=True)\n    c = c - c.mean(1, keepdims=True)\n    return (a @ c.T) / np.outer(np.linalg.norm(a, axis=1), np.linalg.norm(c, axis=1))\n\n\ndef transfer(C, M):\n    \"\"\"Hungarian assignment maximising summed correlation, M_est = P M P^T (Eqs. 4, 5).\n\n    Returns M_est (Ns, Ns) and the rows of the target that were matched.\"\"\"\n    safe = np.where(np.isfinite(C), C, np.nanmin(C))\n    r, c = linear_sum_assignment(-safe)\n    P = np.zeros(C.shape)\n    P[r, c] = 1\n    matched = np.zeros(C.shape[0], bool)\n    matched[r] = True\n    return P @ M @ P.T, matched\n\n\ndef _z(v):\n    sd = v.std(-1, keepdims=True)\n    sd[sd == 0] = 1\n    return (v - v.mean(-1, keepdims=True)) / sd\n\n\ndef cross_subject(target, donors, which_c=\"all\", corr=\"paired\", split_seed=42):\n    \"\"\"Per-electrode donor selection (Algorithm 2) on trial-averaged signals.\n\n    target: preprocessed trials (trials, ch, time) of the target, not z-scored across trials (as\n    Test_new_subject_iEEG.py, which averages the stored trials). donors: list of (trials_d, W_d),\n    each donor's preprocessed trials and its m = 1.0 intra-subject weight matrix.\n    which_c: 'all' trials of the target enter C (code), or 'val' only.\n    Returns per-electrode test DistCorr (NaN where no donor matched) and the donor chosen.\n    \"\"\"\n    from sklearn.model_selection import train_test_split\n    idx = np.arange(len(target))\n    va, te = train_test_split(idx, test_size=0.5, random_state=split_seed)\n    vmean, tmean = target[va].mean(0), target[te].mean(0)\n    n = target.shape[1]\n    val_dc = np.full((len(donors), n), np.nan)\n    test_dc = np.full((len(donors), n), np.nan)\n    src = target if which_c == \"all\" else target[va]\n    for k, (xd, Wd) in enumerate(donors):\n        C = corr_matrix_paired(src, xd) if corr == \"paired\" else corr_matrix_concat(src, xd)\n        Mest, matched = transfer(C, Wd)\n        rv = _z(Mest @ vmean)\n        rt = _z(Mest @ tmean)\n        val_dc[k, matched] = dcor_rows(_z(vmean)[matched], rv[matched])\n        test_dc[k, matched] = dcor_rows(_z(tmean)[matched], rt[matched])\n    has = np.isfinite(val_dc).any(0)\n    choice = np.full(n, -1)\n    choice[has] = np.nanargmax(val_dc[:, has], axis=0)\n    out = np.full(n, np.nan)\n    out[has] = test_dc[choice[has], np.where(has)[0]]\n    return out, choice\n"
}
```

```
File created successfully at: entries/memar-2026/smr.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/memar-2026 && source $TMPDIR/wenv/bin/activate && uv pip install -q scikit-learn 2>&1|tail -1; cat > $TMPDIR/t1.py <<'EOF'
import time, numpy as np, resource, pickle, sys
sys.path.insert(0,'.')
import smr
A=smr.assets()
sub="sub-07"
ss=[a for a in A if a["path"].startswith(sub+"/")]
t=time.time()
sess=[smr.load_session(a["asset_id"]) for a in ss]
print("load", time.time()-t, [s["a"].shape for s in sess], [s["dropped"] for s in sess], [s["bad"].sum() for s in sess])
print("maxrss MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
el=smr.electrodes(ss[0]["asset_id"])
pickle.dump(dict(a=np.concatenate([s["a"] for s in sess]), b=np.concatenate([s["b"] for s in sess]), el=el), open(sys.argv[1],"wb"))
EOF
python $TMPDIR/t1.py $TMPDIR/sub07.pkl
```

```
entries/memar-2026/smr.py:115: RuntimeWarning: invalid value encountered in divide
  z = np.abs((x - mean) / std)
entries/memar-2026/smr.py:165: RuntimeWarning: invalid value encountered in divide
  b = (b - b.mean(1, keepdims=True)) / b.std(1, keepdims=True)
load 96.49256706237793 [(93, 64, 1000), (112, 64, 1000), (199, 64, 1000), (197, 64, 1000), (199, 64, 1000)] [0, 0, 0, 0, 0] [np.int64(0), np.int64(0), np.int64(0), np.int64(0), np.int64(64)]
maxrss MB 875.96
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
s=open("smr.py").read()
s=s.replace('''    raw = d[i0 - HALF - PAD:i0 + HALF + PAD, :].astype(np.float64)
    bad = ~np.isfinite(raw).all(axis=0)
    raw = np.nan_to_num(raw)
    a = filter_steps(raw)[PAD:PAD + 2 * HALF]
    b = filter_steps(raw[PAD:PAD + 2 * HALF])
    return a.astype(np.float32), b.astype(np.float32), bad''','''    raw = d[i0 - HALF - PAD:i0 + HALF + PAD, :].astype(np.float64)
    fin = np.isfinite(raw)
    if not fin.all():
        return None, None, (~fin[PAD:PAD + 2 * HALF]).any(), (~fin).any(0)
    a = filter_steps(raw)[PAD:PAD + 2 * HALF]
    b = filter_steps(raw[PAD:PAD + 2 * HALF])
    return a.astype(np.float32), b.astype(np.float32), False, None''')
s=s.replace('''    Returns dict with 'a' and 'b' (trials, channels, time) float32, the event times kept, the
    number of events dropped at the file's edges and the channels holding non-finite values.''','''    Returns dict with 'a' and 'b' (trials, channels, time) float32, the event times kept, the
    number of events dropped at the file's edges, the number dropped for non-finite samples in
    the padded window (`nan_pad`) and, of these, in the 2 s epoch itself (`nan_epoch`).''')
s=s.replace('''    a = np.stack([r[0] for r in res])            # (trials, time, ch)
    b = np.stack([r[1] for r in res])
    bad = np.any([r[2] for r in res], axis=0)''','''    ok = [r[0] is not None for r in res]
    a = np.stack([r[0] for r in res if r[0] is not None])            # (trials, time, ch)
    b = np.stack([r[1] for r in res if r[1] is not None])
    nan_pad = int(len(ok) - sum(ok))
    nan_epoch = int(sum(r[2] for r in res))''')
s=s.replace('''                times=t[keep], dropped=int((~keep).sum()), bad=bad)''','''                times=t[keep][ok], dropped=int((~keep).sum()), nan_pad=nan_pad,
                nan_epoch=nan_epoch)''')
open("smr.py","w").write(s)
EOF
grep -n "ok\]" smr.py
```

```
172:                times=t[keep][ok], dropped=int((~keep).sum()), nan_pad=nan_pad,
411:        acc[ok] += C[ok]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t2.py <<'EOF'
import time, numpy as np, pickle, sys, os
sys.path.insert(0,'.')
import smr
D=pickle.load(open(os.environ["TMPDIR"]+"/sub07.pkl","rb"))
x=D["a"]; ok=np.isfinite(x).all((1,2)); x=x[ok]; print(x.shape)
xyz=np.c_[D["el"]["x"],D["el"]["y"],D["el"]["z"]]
nbr=smr.neighbours(xyz)
for decim in (int(sys.argv[1]),):
    t=time.time()
    r=smr.run_smr(x, nbr, 1.0, 1, decim=decim)
    print(decim, "time", time.time()-t, "epochs", r["n_ep"], "best ep median", np.median(r["best_ep"]), "dc mean", r["dc"].mean())
EOF
OMP_NUM_THREADS=4 timeout 900 python $TMPDIR/t2.py 10
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t2.py", line 1, in <module>
    import time, numpy as np, pickle, sys, os
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate; OMP_NUM_THREADS=4 timeout 900 python $TMPDIR/t2.py 10
```

```
(800, 64, 1000)
10 time 152.0290150642395 epochs 4843 best ep median 2527.0 dc mean 0.6431242690685307
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t3.py <<'EOF'
import time, numpy as np, pickle, sys, os
sys.path.insert(0,'.')
import smr
D=pickle.load(open(os.environ["TMPDIR"]+"/sub07.pkl","rb"))
x=D["a"]
xyz=np.c_[D["el"]["x"],D["el"]["y"],D["el"]["z"]]
nbr=smr.neighbours(xyz)
for decim,me in [(10,100),(10,300),(10,1000),(2,300)]:
    t=time.time()
    r=smr.run_smr(x, nbr, 1.0, 1, decim=decim, max_epoch=me)
    print(decim, me, "time", round(time.time()-t,1), "dc mean", r["dc"].mean(), flush=True)
EOF
OMP_NUM_THREADS=4 timeout 1200 python $TMPDIR/t3.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t3.py", line 1, in <module>
    import time, numpy as np, pickle, sys, os
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate; OMP_NUM_THREADS=4 timeout 1200 python $TMPDIR/t3.py
```

```
10 100 time 12.8 dc mean 0.6430857702891155
10 300 time 14.1 dc mean 0.6430887307918565
10 1000 time 34.7 dc mean 0.6432468352991512
2 300 time 36.7 dc mean 0.6434123723103116
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate; python -c "
import dcor, numpy as np, time
X=np.random.randn(10000,1000); Y=X+np.random.randn(10000,1000)
r=dcor.rowwise(dcor.distance_correlation, X[:10], Y[:10], method='mergesort')
t=time.time(); r=dcor.rowwise(dcor.distance_correlation, X, Y, method='mergesort'); print('default',time.time()-t)
t=time.time(); r2=dcor.rowwise(dcor.distance_correlation, X, Y, method='avl'); print('avl',time.time()-t, np.abs(r-r2).max())
t=time.time(); r2=dcor.rowwise(dcor.distance_correlation, X, Y, method='mergesort', compile_mode=dcor.CompileMode.COMPILE_PARALLEL); print('par',time.time()-t, np.abs(r-r2).max())
"; nproc; free -g
```

```
Traceback (most recent call last):
  File "<string>", line 7, in <module>
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_rowwise.py", line 192, in rowwise
    [function(x_elem, y_elem, **kwargs) for x_elem, y_elem in zip(x, y)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_dcor.py", line 1033, in distance_correlation
    distance_correlation_sqr(
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_dcor.py", line 911, in distance_correlation_sqr
    return method.value.stats_sqr(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_dcor.py", line 260, in stats_sqr
    ) = self.terms(
        ^^^^^^^^^^^
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_fast_dcov_mergesort.py", line 398, in _distance_covariance_sqr_terms_mergesort
    raise NotImplementedError(
NotImplementedError: Compile mode CompileMode.COMPILE_PARALLEL not implemented.
default 5.148895740509033
avl 7.337457656860352 1.8540724511240114e-14
4
               total        used        free      shared  buff/cache   available
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate; python -c "
import dcor, numpy as np, time
X=np.random.randn(10000,1000); Y=X+np.random.randn(10000,1000)
r=dcor.rowwise(dcor.distance_correlation, X[:10], Y[:10], method='avl', compile_mode=dcor.CompileMode.COMPILE_PARALLEL)
t=time.time(); r2=dcor.rowwise(dcor.distance_correlation, X, Y, method='avl', compile_mode=dcor.CompileMode.COMPILE_PARALLEL); print('avlpar',time.time()-t)
r3=np.array([dcor.distance_correlation(X[i],Y[i],method='naive') for i in range(5)]); print(np.abs(r2[:5]-r3).max())
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_rowwise.py", line 192, in rowwise
    [function(x_elem, y_elem, **kwargs) for x_elem, y_elem in zip(x, y)],
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_dcor.py", line 1033, in distance_correlation
    distance_correlation_sqr(
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_dcor.py", line 911, in distance_correlation_sqr
    return method.value.stats_sqr(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_dcor.py", line 260, in stats_sqr
    ) = self.terms(
        ^^^^^^^^^^^
  File "/tmp/claude-1001/wenv/lib/python3.12/site-packages/dcor/_fast_dcov_avl.py", line 539, in _distance_covariance_sqr_terms_avl
    raise NotImplementedError(
NotImplementedError: Compile mode CompileMode.COMPILE_PARALLEL not implemented.
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open("smr.py").read()
s=s.replace('''def dcor_rows(u, v):
    """Distance correlation of each row pair (Eqs. 8 to 14); 0 where a row is constant."""
    import dcor
    u = np.ascontiguousarray(u, dtype=np.float64)
    v = np.ascontiguousarray(v, dtype=np.float64)
    out = np.asarray(dcor.rowwise(dcor.distance_correlation, u, v, method="mergesort"))
    const = (u.std(1) == 0) | (v.std(1) == 0)
    out[const] = 0.0
    return np.nan_to_num(out)''','''def _dcor_chunk(args):
    import dcor
    u, v = args
    return np.asarray(dcor.rowwise(dcor.distance_correlation, u, v, method="mergesort"))


_POOL = {}


def dcor_rows(u, v, workers=4):
    """Distance correlation of each row pair (Eqs. 8 to 14); 0 where a row is constant."""
    u = np.ascontiguousarray(u, dtype=np.float64)
    v = np.ascontiguousarray(v, dtype=np.float64)
    if len(u) < 400:
        out = _dcor_chunk((u, v))
    else:
        if "p" not in _POOL:
            _POOL["p"] = ProcessPoolExecutor(workers)
        parts = np.array_split(np.arange(len(u)), workers * 4)
        out = np.concatenate(list(_POOL["p"].map(_dcor_chunk, [(u[p], v[p]) for p in parts])))
    const = (u.std(1) == 0) | (v.std(1) == 0)
    out[const] = 0.0
    return np.nan_to_num(out)''')
s=s.replace('''def electrodes(asset_id):''','''def load_subject(sub, readings=("a", "b"), workers=16):
    """All sessions of one subject ('sub-01'), pooled. Returns the trials of each reading
    (reading b kept as float16 to save memory), the electrode table of the first session, and
    per-session counts."""
    ss = [a for a in assets() if a["path"].startswith(sub + "/")]
    out = {r: [] for r in readings}
    info = []
    for a in ss:
        s = load_session(a["asset_id"], workers)
        for r in readings:
            out[r].append(s[r].astype(np.float16 if r == "b" else np.float32))
        info.append(dict(path=a["path"], trials=len(s["times"]), dropped_edge=s["dropped"],
                         dropped_nan=s["nan_pad"], nan_in_epoch=s["nan_epoch"]))
    res = {r: np.concatenate(v) for r, v in out.items()}
    res["el"] = electrodes(ss[0]["asset_id"])
    res["sessions"] = info
    return res


def electrodes(asset_id):''')
open("smr.py","w").write(s)
EOF
cat > $TMPDIR/t4.py <<'EOF'
import time, numpy as np, pickle, sys, os, resource
sys.path.insert(0,'.')
import smr
t=time.time()
S=smr.load_subject(sys.argv[1])
print("load", time.time()-t, S["a"].shape, S["sessions"]); print("rss",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
pickle.dump(S, open(os.environ["TMPDIR"]+f"/{sys.argv[1]}.pkl","wb"))
x=S["a"]
xyz=np.c_[S["el"]["x"],S["el"]["y"],S["el"]["z"]]
nbr=smr.neighbours(xyz)
for decim,me,lag in [(10,200,False),(10,200,True)]:
    t=time.time()
    r=smr.run_smr(x, nbr, 1.0, 1, decim=decim, max_epoch=me, lagged=lag)
    print(decim, me, lag, "time", round(time.time()-t,1), "dc mean", r["dc"].mean(), flush=True)
EOF
source $TMPDIR/wenv/bin/activate; OMP_NUM_THREADS=4 timeout 1200 python $TMPDIR/t4.py sub-12
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t4.py", line 5, in <module>
    S=smr.load_subject(sys.argv[1])
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/memar-2026/smr.py", line 184, in load_subject
    s = load_session(a["asset_id"], workers)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/memar-2026/smr.py", line 154, in load_session
    res = list(ex.map(_read_event, i0[keep]))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/process.py", line 636, in _chain_from_iterable_of_lists
    for element in iterable:
                   ^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 619, in result_iterator
    yield _result_or_cancel(fs.pop())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/.local/share/uv/python/cpython-3.12.16-linux-x86_64-gnu/lib/python3.12/concurrent/futures/_base.py", line 317, in _result_or_cancel
    return fut.result(timeout)
           ^^^^^^^^^^^^^^^^^^^
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate; python -c "import remfile,inspect; print(inspect.signature(remfile.File.__init__))"; grep -n "cache\|chunk_size\|max" $TMPDIR/wenv/lib/python3.12/site-packages/remfile/RemFile.py | head -30; dmesg 2>/dev/null | tail -5
```

```
(self, url: Union[str, Any], *, verbose: bool = False, disk_cache: Optional[remfile.DiskCache.DiskCache] = None, timeout: Union[float, Tuple[float, float], NoneType] = (30, 60), _min_chunk_size: int = 102400, _max_cache_size: int = 1000000000.0, _chunk_increment_factor: int = 1.7, _bytes_per_thread: int = 4194304, _max_threads: int = 1, _max_chunk_size: int = 104857600, _impose_request_failures_for_testing: bool = False, _size: Optional[int] = None, _use_session: bool = True)
8:default_min_chunk_size = 100 * 1024
9:default_max_cache_size = 1e9
12:default_max_threads = 1
24:        disk_cache: Union[DiskCache, None] = None,
26:        _min_chunk_size: int = default_min_chunk_size,
27:        _max_cache_size: int = default_max_cache_size,
30:        _max_threads: int = default_max_threads,
31:        _max_chunk_size: int = 100 * 1024 * 1024,
41:            disk_cache (DiskCache, optional): A disk cache for storing the chunks of the file. Defaults to None.
43:            _min_chunk_size (int, optional): The minimum chunk size. When reading, the chunks will be loaded in multiples of this size.
44:            _max_cache_size (int, optional): The maximum number of bytes to keep in the cache.
47:            _max_threads (int, optional): The maximum number of threads to use when loading the file.
48:            _max_chunk_size (int, optional): The maximum chunk size. When reading, the chunks will be loaded in multiples of the minimum chunk size up to this size.
55:        self._disk_cache = disk_cache
57:        self._min_chunk_size = _min_chunk_size
58:        self._max_chunks_in_cache = int(_max_cache_size / _min_chunk_size)
61:        self._max_threads = _max_threads
62:        self._max_chunk_size = _max_chunk_size
69:        )  # list of chunk indices in order of loading for purposes of cleaning up the cache
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's|    _WORKER\["d"\] = h5py.File(remfile.File(url), "r")\["acquisition/ElectricalSeries/data"\]|    # remfile keeps up to 1 GB of cache by default; 16 workers would exhaust the memory\n    _WORKER["d"] = h5py.File(remfile.File(url, _max_cache_size=64e6), "r")[\n        "acquisition/ElectricalSeries/data"]|' smr.py; grep -n "_max_cache" smr.py; source $TMPDIR/wenv/bin/activate; OMP_NUM_THREADS=4 timeout 1200 python $TMPDIR/t4.py sub-12
```

```
126:    _WORKER["d"] = h5py.File(remfile.File(url, _max_cache_size=64e6), "r")[
load 197.0254771709442 (986, 124, 1000) [{'path': 'sub-12/sub-12_ses-3_behavior+ecephys.nwb', 'trials': 198, 'dropped_edge': 0, 'dropped_nan': 2, 'nan_in_epoch': 1}, {'path': 'sub-12/sub-12_ses-4_behavior+ecephys.nwb', 'trials': 197, 'dropped_edge': 0, 'dropped_nan': 3, 'nan_in_epoch': 3}, {'path': 'sub-12/sub-12_ses-5_behavior+ecephys.nwb', 'trials': 197, 'dropped_edge': 0, 'dropped_nan': 3, 'nan_in_epoch': 1}, {'path': 'sub-12/sub-12_ses-6_behavior+ecephys.nwb', 'trials': 197, 'dropped_edge': 0, 'dropped_nan': 0, 'nan_in_epoch': 0}, {'path': 'sub-12/sub-12_ses-7_behavior+ecephys.nwb', 'trials': 197, 'dropped_edge': 0, 'dropped_nan': 2, 'nan_in_epoch': 2}]
rss 1977.736
10 200 False time 27.1 dc mean 0.6578040180621343
10 200 True time 44.1 dc mean 0.6719876758795068
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/wenv/bin/activate; python - <<'EOF'
import pickle, os, numpy as np
S=pickle.load(open(os.environ["TMPDIR"]+"/sub-12.pkl","rb"))
el=S["el"]; print({k:(v[:3], v.dtype) for k,v in el.items()}); print(np.unique(el["location"]), (el["x"]>0).sum(), (el["x"]<0).sum(), el["good"].sum())
xyz=np.c_[el["x"],el["y"],el["z"]]
p=xyz[:,[0,2]]; d=np.sqrt(((p[:,None]-p[None])**2).sum(-1)); np.fill_diagonal(d,np.inf); print("min xz dist", d.min(), (d==0).sum())
print(np.isnan(xyz).sum())
EOF
```

```
Sat Nov 21 11:45:53 UTC 2026
{'x': (array([-53.92384236, -55.10274194, -56.92833614]), dtype('float64')), 'y': (array([42.93428065, 36.27487657, 29.72381889]), dtype('float64')), 'z': (array([ 6.52890157, 14.62263385, 24.41566731]), dtype('float64')), 'good': (array([False,  True,  True]), dtype('bool')), 'location': (array(['unknown', 'unknown', 'unknown'], dtype='<U7'), dtype('<U7')), 'group_name': (array(['GRID', 'GRID', 'GRID'], dtype='<U4'), dtype('<U4'))}
['unknown'] 4 112 112
min xz dist nan 0
24
```

**Agent calls Bash**

```bash
cd  ls tools; sed -n 1,60p tools/entry.py | head -80; grep -n "sanity\|claim:\|tags" tools/entry.py | head -30
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def run\|max-minutes\|--only\|notebook" tools/entry.py | sed -n 1,60p | grep -n "add_argument\|def "
```

```
11:172:def code_of(notebook_path: Path) -> str:
30:509:def tagged_outputs(notebook: Path) -> dict[str, str]:
39:596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
53:701:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
54:703:    parser.add_argument("--max-minutes", type=float, default=60,
56:709:    parser.add_argument("--before", type=Path, help="upgrade-python: the executed notebooks to compare with "
```

**Agent calls Bash**

```bash
cd  sed -n 596,700p tools/entry.py
```

```
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/build; cat > $TMPDIR/build/common.py <<'EOF'
import nbformat as nbf
def build(cells, path):
    nb = nbf.v4.new_notebook()
    out = []
    for kind, src, *tags in cells:
        c = nbf.v4.new_markdown_cell(src.strip()) if kind == "md" else nbf.v4.new_code_cell(src.strip())
        if tags:
            c.metadata["tags"] = list(tags)
        out.append(c)
    nb.cells = out
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    nbf.write(nb, path)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/memar-2026 && cat >> smr.py <<'EOF'


# ----------------------------------------------------------------------------- survey and checks
def survey_file(a):
    """Metadata and array shapes of one file (no signal is read)."""
    f = open_nwb(a["asset_id"])
    es = f["acquisition/ElectricalSeries"]
    el = f["general/extracellular_ephys/electrodes"]
    xyz = np.c_[el["x"][:], el["y"][:], el["z"][:]]
    loc = sorted({s.decode() for s in el["location"][:]})
    return dict(path=a["path"], subject=a["path"].split("/")[0], samples=es["data"].shape[0],
                channels=es["data"].shape[1], rate=float(es["starting_time"].attrs["rate"]),
                conversion=float(es["data"].attrs["conversion"]), unit=es["data"].attrs["unit"],
                hours=es["data"].shape[0] / float(es["starting_time"].attrs["rate"]) / 3600,
                reaches=len(f["intervals/reaches/start_time"]),
                reach_events=len(f["processing/behavior/ReachEvents/timestamps"]),
                same_times=bool(np.allclose(f["intervals/reaches/start_time"][:],
                                            f["processing/behavior/ReachEvents/timestamps"][:],
                                            atol=0.002)),
                good=int(el["good"][:].sum()), no_coords=int(np.isnan(xyz).any(1).sum()),
                x_pos=int((xyz[:, 0] > 0).sum()), x_neg=int((xyz[:, 0] < 0).sum()),
                locations=",".join(loc))


def survey(workers=16):
    from concurrent.futures import ThreadPoolExecutor
    import pandas as pd
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(survey_file, assets()))
    return pd.DataFrame(rows)


def hg_power(x, lo=70, hi=110):
    """High-gamma power (band-pass 70 to 110 Hz, squared) of trials (trials, ch, time)."""
    b, a = signal.butter(4, [lo / (FS / 2), hi / (FS / 2)], btype="band")
    return signal.filtfilt(b, a, x.astype(np.float64), axis=-1) ** 2


def clock_check(x, rng, n_perm=200):
    """Event-locked change: per electrode, high-gamma power 0 to 0.75 s after the event minus
    0.75 to 0 s before, paired over trials (t statistic). The largest |t| over electrodes is
    compared with a null in which the pre and post labels are swapped at random per trial.
    Returns the observed max |t|, the null 95th percentile, and the electrode count with |t| > 4."""
    p = hg_power(x)
    pre = np.log(p[:, :, 125:500].mean(-1))
    post = np.log(p[:, :, 500:875].mean(-1))
    d = post - pre

    def tmax(d):
        t = d.mean(0) / (d.std(0, ddof=1) / np.sqrt(len(d)))
        return np.abs(t).max(), t
    obs, t = tmax(d)
    null = np.array([tmax(d * rng.choice([-1, 1], (len(d), 1)))[0] for _ in range(n_perm)])
    return obs, np.percentile(null, 95), int((np.abs(t) > 4).sum()), t
EOF
python -c "import ast;ast.parse(open('smr.py').read())"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> smr.py <<'EOF'


def drop_uncoordinated(S):
    """Drop electrodes with no MNI coordinates: they have no (x, z) neighbourhood (Methods II B).
    The paper names no such exclusion; it is this attempt's choice for a rare input."""
    el = S["el"]
    xyz = np.c_[el["x"], el["y"], el["z"]]
    keep = np.isfinite(xyz).all(1)
    S = dict(S)
    for r in ("a", "b"):
        if r in S:
            S[r] = S[r][:, keep]
    S["el"] = {k: v[keep] for k, v in el.items()}
    S["xyz"] = xyz[keep]
    S["n_dropped_el"] = int((~keep).sum())
    return S
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/build/nb1.py <<'PYEOF'
import sys; sys.path.insert(0, sys.argv[1]); from common import build
cells = []
md = lambda s, *t: cells.append(("md", s, *t))
code = lambda s, *t: cells.append(("code", s, *t))

md("""
# Spatially Masked Regression on AJILE12: intra-subject, cross-subject, masking and coverage

Ostadsharif Memar & Dehghani (2026), "Spatially Masked Regression Reveals Local and Distributed
Predictability in Electrophysiological Recordings", arXiv:2606.11415 (doi:10.48550/arxiv.2606.11415).
The claims file `claims/memar-2026.yaml` was written from the arXiv preprint, version 1, and its
code at commit 244dcdbd of github.com/neurovium/SpatiallyMaskedRegression.

Dataset: DANDI:000055 (AJILE12), version 0.220127.0436 (doi:10.48324/dandi.000055/0.220127.0436).
Why this version: the paper cites the dataset (Peterson et al. 2022) but no version of it. 0.220127.0436
is the only published version and the most recent; the draft (modified 2026-02-12) has the same
55 assets and size, and a draft can change. The files are streamed; nothing is written to disk.

This notebook tests the claims below. A second notebook, `surrogates_lagged.ipynb`, tests the
surrogate, lagged and full-mask claims. The EEG claims rest on a dataset the paper names without
an accession (BNCI Horizon 2020, Ofner et al. 2017) that is not in DANDI:000055 and is not tested.

| Claim | Here |
|---|---|
| intra-ieeg-mean | tested |
| table2-ieeg-intra-subjects | tested |
| cross-ieeg-mean | tested |
| table2-ieeg-cross-subjects | tested |
| cross-below-intra-ieeg | tested |
| fig4a-mask-sweep-ieeg | tested |
| fig5a-coverage-ieeg | tested |
| lagged-ieeg-no-gain, surrogate-ieeg, surrogate-order-ieeg, full-mask-above-zero-ieeg | tested in `surrogates_lagged.ipynb` |
| intra-eeg-mean, intra-eeg-above-ieeg, cross-eeg-mean, transfer-penalty-larger-ieeg, lagged-eeg-no-gain, fig4b-mask-sweep-eeg, fig5b-coverage-eeg, surrogate-eeg, surrogate-order-eeg | blocked: the EEG data are not in this dataset (data elsewhere, no accession) |

Method details and where each comes from are in the docstring of `smr.py`. Two deviations, for
time, apply to every fit: the gradient steps and the validation loss use every 10th sample of
each trial (the test score uses all samples), and training stops after 200 epochs (the paper's
code allows 10000 with a patience of 200). `surrogates_lagged.ipynb` shows on one subject how
little either changes the score.
""")

code("""
import os, time, zlib, json, resource
import numpy as np
import pandas as pd
from scipy import stats
import smr

T0 = time.time()
PAPER = "memar-2026"
def seed(claim):
    return zlib.crc32(f"{PAPER}/{claim}".encode())

DECIM, MAX_EPOCH = 10, 200
SUBJECTS = [f"sub-{i:02d}" for i in range(1, 13)]
print("dataset", smr.DANDISET, smr.VERSION)
""")

md("## Data check\n\nMetadata of every file (no signal read), then the trials of every subject.")

code("""
sv = smr.survey()
pd.set_option("display.width", 250, "display.max_columns", 30, "display.max_rows", 100)
print(sv.drop(columns=["subject"]).to_string(index=False))
print()
print("files", len(sv), "subjects", sv.subject.nunique(), "sessions per subject",
      sv.groupby("subject").size().to_dict())
print("sampling rates", sorted(sv.rate.unique()), "units", sorted(sv.unit.unique()),
      "conversion", sorted(sv.conversion.unique()))
print("channels per subject", sv.groupby("subject").channels.agg(["min", "max"]).to_dict("index"))
print("location labels in the electrode tables", sorted(set(",".join(sv.locations).split(","))))
print("reaches table and ReachEvents timestamps agree in every file:", bool(sv.same_times.all()))
print("total reach events", int(sv.reaches.sum()))
""", "sanity")

code("""
t = time.time()
DATA = {}
for s in SUBJECTS:
    S = smr.load_subject(s)
    DATA[s] = smr.drop_uncoordinated(S)
    print(s, "trials", DATA[s]["a"].shape[0], "electrodes", DATA[s]["a"].shape[1],
          "dropped without coordinates", DATA[s]["n_dropped_el"],
          "events dropped at file edges", sum(x["dropped_edge"] for x in S["sessions"]),
          "dropped for NaN in the padded window", sum(x["dropped_nan"] for x in S["sessions"]),
          "of which NaN in the 2 s epoch", sum(x["nan_in_epoch"] for x in S["sessions"]),
          f"({time.time() - t:.0f} s)", flush=True)
print("peak memory MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3)
""", "sanity")

code("""
rows = []
for s, S in DATA.items():
    xa = S["a"]
    rows.append(dict(subject=s, trials=xa.shape[0], electrodes=xa.shape[1], samples=xa.shape[2],
                     a_min=float(xa.min()), a_max=float(xa.max()), a_sd=float(xa.std()),
                     b_min=float(S["b"].min()), b_max=float(S["b"].max()),
                     hemisphere_x_neg=int((S["xyz"][:, 0] < 0).sum()), x_pos=int((S["xyz"][:, 0] > 0).sum()),
                     good_false=int((~S["el"]["good"]).sum()),
                     sessions=len(S["sessions"])))
summary = pd.DataFrame(rows)
print(summary.to_string(index=False))
print("trials in all:", summary.trials.sum())
""", "sanity")

md("""
Duplicate recordings: each pair of sessions (within and across subjects with the same channel
count) is compared by its reach event times and by the per-channel SD of its trials. The clock:
high-gamma power after the event against before it, against a null with the labels swapped per
trial (protocol, author step 2).
""")

code("""
fp = []
for s, S in DATA.items():
    start = 0
    for x in S["sessions"]:
        n = x["trials"]
        fp.append((x["path"], S["a"][start:start + n].std(axis=(0, 2))))
        start += n
dups = 0
for i in range(len(fp)):
    for j in range(i + 1, len(fp)):
        if len(fp[i][1]) == len(fp[j][1]) and np.allclose(fp[i][1], fp[j][1], rtol=1e-4):
            dups += 1
            print("same channel SDs:", fp[i][0], fp[j][0])
times = {}
for a in smr.assets():
    f = smr.open_nwb(a["asset_id"])
    times[a["path"]] = f["intervals/reaches/start_time"][:]
same_t = [(p, q) for i, p in enumerate(times) for q in list(times)[i + 1:]
          if len(times[p]) == len(times[q]) and np.allclose(times[p], times[q])]
print("session pairs with identical trial SD profiles:", dups, "; with identical event times:", len(same_t), same_t)
""", "sanity")

code("""
rng = np.random.default_rng(seed("intra-ieeg-mean") + 7)   # a generator for the data check only
clock = []
for s, S in DATA.items():
    obs, null95, n4, _ = smr.clock_check(S["a"], rng)
    clock.append(dict(subject=s, max_abs_t=round(obs, 2), null_95=round(null95, 2), electrodes_abs_t_over_4=n4))
print(pd.DataFrame(clock).to_string(index=False))
""", "sanity")

md("""
## intra-ieeg-mean

> In the intra-subject setting, SMR reconstructs held-out iEEG with a mean distance correlation of
> 0.553 ± 0.068 across the 12 AJILE12 subjects.

The common pipeline at m = 1.0 (the whole 9-electrode neighbourhood masked with the target), under
both readings of where the preprocessing is applied. The atlas neighbourhood variant cannot be
run: every electrode's `location` is "unknown" (data check above), and the dataset holds no AAL
labels.
""")

code("""
def run_all(m, claim, reading="a", **kw):
    rng_seed = seed(claim)
    out = {}
    for k, s in enumerate(SUBJECTS):
        S = DATA[s]
        x = S[reading].astype(np.float32)
        nbr = smr.neighbours(S["xyz"])
        r = smr.run_smr(x, nbr, m, rng_seed + 0 if False else rng_seed + 100 * k, decim=DECIM,
                        max_epoch=MAX_EPOCH, **kw)
        out[s] = r
    return out

def table(res, label):
    v = np.array([res[s]["dc"].mean() for s in SUBJECTS])
    return v

t = time.time()
R1a = run_all(1.0, "intra-ieeg-mean", "a")
print(f"reading a done ({time.time() - t:.0f} s)", flush=True)
R1b = run_all(1.0, "intra-ieeg-mean", "b")
print(f"reading b done ({time.time() - t:.0f} s)", flush=True)
""")
PYEOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open("smr.py").read()
s=s.replace('''def run_smr(x, nbr, m, seed, *, lagged=False, decim=1, rule="ceil", mode="mask", split_seed=42,
            max_epoch=10000):
    """One intra-subject SMR run. x: preprocessed trials (trials, ch, time), not yet z-scored
    across trials. Returns per-electrode test DistCorr, W, b, and fit diagnostics."""
    rng = np.random.default_rng(seed)''','''def run_smr(x, nbr, m, rng, *, lagged=False, decim=1, rule="ceil", mode="mask", split_seed=42,
            max_epoch=10000):
    """One intra-subject SMR run. x: preprocessed trials (trials, ch, time), not yet z-scored
    across trials; rng: the claim's generator (mask draws, initial weights, batch order).
    Returns per-electrode test DistCorr, W, b, and fit diagnostics."""''')
open("smr.py","w").write(s)
EOF
python - <<'EOF'
import os
p=os.environ["TMPDIR"]+"/build/nb1.py"
s=open(p).read()
s=s.replace('''def run_all(m, claim, reading="a", **kw):
    rng_seed = seed(claim)
    out = {}
    for k, s in enumerate(SUBJECTS):
        S = DATA[s]
        x = S[reading].astype(np.float32)
        nbr = smr.neighbours(S["xyz"])
        r = smr.run_smr(x, nbr, m, rng_seed + 0 if False else rng_seed + 100 * k, decim=DECIM,
                        max_epoch=MAX_EPOCH, **kw)
        out[s] = r
    return out

def table(res, label):
    v = np.array([res[s]["dc"].mean() for s in SUBJECTS])
    return v

t = time.time()
R1a = run_all(1.0, "intra-ieeg-mean", "a")
print(f"reading a done ({time.time() - t:.0f} s)", flush=True)
R1b = run_all(1.0, "intra-ieeg-mean", "b")
print(f"reading b done ({time.time() - t:.0f} s)", flush=True)''','''def run_all(m, rng, reading="a", **kw):
    \"\"\"One SMR condition on every subject, in order, from one generator.\"\"\"
    out = {}
    for s in SUBJECTS:
        S = DATA[s]
        out[s] = smr.run_smr(S[reading].astype(np.float32), smr.neighbours(S["xyz"]), m, rng,
                             decim=DECIM, max_epoch=MAX_EPOCH, **kw)
    return out

def subj(res):
    return np.array([res[s]["dc"].mean() for s in SUBJECTS])

def msd(v):
    return f"{np.mean(v):.3f} ± {np.std(v):.3f}"

t = time.time()
R1a = run_all(1.0, np.random.default_rng(seed("intra-ieeg-mean")), "a")
print(f"reading a done ({time.time() - t:.0f} s)", flush=True)
R1b = run_all(1.0, np.random.default_rng(seed("intra-ieeg-mean") + 1), "b")
print(f"reading b done ({time.time() - t:.0f} s)", flush=True)''')
open(p,"w").write(s)
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/build/nb1.py <<'PYEOF'

code("""
TAB_INTRA = [0.585, 0.647, 0.535, 0.452, 0.524, 0.428, 0.531, 0.487, 0.635, 0.605, 0.612, 0.593]
TAB_INTRA_SD = [0.041, 0.038, 0.035, 0.036, 0.034, 0.021, 0.028, 0.025, 0.041, 0.040, 0.032, 0.032]
ia, ib = subj(R1a), subj(R1b)
df = pd.DataFrame({"subject": SUBJECTS, "electrodes": [len(R1a[s]["dc"]) for s in SUBJECTS],
                   "reading_a": ia.round(3), "sd_el_a": [R1a[s]["dc"].std().round(3) for s in SUBJECTS],
                   "reading_b": ib.round(3), "paper": TAB_INTRA,
                   "min_el_a": [R1a[s]["dc"].min().round(3) for s in SUBJECTS],
                   "max_el_a": [R1a[s]["dc"].max().round(3) for s in SUBJECTS]})
print(df.to_string(index=False))
for name, v in (("reading a (preprocess, then segment)", ia), ("reading b (preprocess each epoch)", ib)):
    print(f"{name}: mean over subjects {msd(v)}; within 0.553 ± 0.068: {abs(v.mean() - 0.553) <= 0.068}")
print("epochs run per subject (reading a):", [R1a[s]["n_ep"] for s in SUBJECTS])
print("median epoch of the best validation loss per subject:", [int(np.median(R1a[s]["best_ep"])) for s in SUBJECTS])
""", "claim:intra-ieeg-mean")

md("""
## table2-ieeg-intra-subjects

> Intra-subject iEEG DistCorr differs across subjects, from 0.428 to 0.647, with the subject values
> Table II and Figure 2A give.

Row n of Table II is taken as sub-n (claims file). Each subject's value is compared with the
table's value, with the table's SD across electrodes as tolerance.
""")

code("""
for name, v in (("reading a", ia), ("reading b", ib)):
    within = np.abs(v - np.array(TAB_INTRA)) <= np.array(TAB_INTRA_SD)
    rho, p = stats.spearmanr(v, TAB_INTRA)
    print(f"{name}: {within.sum()} of 12 within tolerance; subjects within: "
          f"{[s for s, w in zip(SUBJECTS, within) if w]}; Spearman rho with Table II {rho:.2f} (p = {p:.3f}); "
          f"range {v.min():.3f} to {v.max():.3f}")
    print("   difference from the table:", np.round(v - np.array(TAB_INTRA), 3).tolist())
""", "claim:table2-ieeg-intra-subjects")

md("""
## cross-ieeg-mean

> Transferring learned inter-electrode matrices from other subjects, through correlation-based
> electrode mapping and per-electrode donor selection, reconstructs a target subject's
> trial-averaged iEEG with a mean DistCorr of 0.389 ± 0.064, without fitting weights on the target.

Donor matrices are the m = 1.0 intra-subject weights of reading (a). The target's trials enter as
stored after preprocessing (not z-scored across trials), as the paper's evaluation script averages
the stored trials (Test_new_subject_iEEG.py, lines 101 to 106: split 50/50 with random_state 42,
mean over trials, z-score of each mean trace). Readings: which of the target's trials enter C (all,
as the code; or the validation half), and how C is computed (Eq. 3, paired trials; or the code's
concatenated series). Electrodes with no matched donor are left out of the mean.
""")

code("""
TAB_CROSS = [0.331, 0.483, 0.440, 0.325, 0.509, 0.285, 0.415, 0.377, 0.409, 0.363, 0.395, 0.340]
TAB_CROSS_SD = [0.007, 0.013, 0.012, 0.006, 0.016, 0.004, 0.010, 0.013, 0.010, 0.007, 0.014, 0.006]
t = time.time()
CROSS = {}
for which_c in ("all", "val"):
    for corr in ("paired", "concat"):
        vals, unmatched = [], []
        for s in SUBJECTS:
            donors = [(DATA[d]["a"], R1a[d]["W"]) for d in SUBJECTS if d != s]
            dc, choice = smr.cross_subject(DATA[s]["a"], donors, which_c=which_c, corr=corr)
            vals.append(np.nanmean(dc))
            unmatched.append(int(np.isnan(dc).sum()))
        CROSS[(which_c, corr)] = np.array(vals)
        v = CROSS[(which_c, corr)]
        print(f"C from {which_c} trials, {corr}: mean {msd(v)}; within 0.389 ± 0.064: {abs(v.mean() - 0.389) <= 0.064}; "
              f"electrodes without a donor per subject {unmatched} ({time.time() - t:.0f} s)", flush=True)
print(pd.DataFrame({"subject": SUBJECTS, **{f"{a}/{b}": v.round(3) for (a, b), v in CROSS.items()},
                    "paper": TAB_CROSS}).to_string(index=False))
""", "claim:cross-ieeg-mean")

md("""
## table2-ieeg-cross-subjects

> Cross-subject iEEG DistCorr ranges over subjects from 0.285 to 0.509, with the subject values
> Table II and Figure 2A give.
""")

code("""
for key, v in CROSS.items():
    within = np.abs(v - np.array(TAB_CROSS)) <= np.array(TAB_CROSS_SD)
    rho, p = stats.spearmanr(v, TAB_CROSS)
    print(f"{key}: {within.sum()} of 12 within tolerance {[s for s, w in zip(SUBJECTS, within) if w]}; "
          f"Spearman rho {rho:.2f} (p = {p:.3f}); range {v.min():.3f} to {v.max():.3f}")
""", "claim:table2-ieeg-cross-subjects")

md("""
## cross-below-intra-ieeg

> Cross-subject iEEG performance is lower than intra-subject performance but keeps appreciable
> predictive power.
""")

code("""
for key, v in CROSS.items():
    print(f"{key}: cross {v.mean():.3f} against intra (reading a) {ia.mean():.3f}: below {v.mean() < ia.mean()}; "
          f"subjects with cross below intra {int((v < ia).sum())} of 12; "
          f"cross-ieeg-mean within tolerance {abs(v.mean() - 0.389) <= 0.064}")
""", "claim:cross-below-intra-ieeg")

md("""
## fig4a-mask-sweep-ieeg

> In iEEG, DistCorr decreases as more of the target's local neighborhood is masked (mask
> intensity 0, 25, 50, 75 and 100%).

ceil(m × 9) neighbours drawn at random per electrode (Results III D); m = 1.0 is the run above.
""")

code("""
t = time.time()
rng_sweep = np.random.default_rng(seed("fig4a-mask-sweep-ieeg"))
SWEEP = {}
for m in (0.0, 0.25, 0.5, 0.75):
    SWEEP[m] = run_all(m, rng_sweep, "a")
    print(f"m = {m} done ({time.time() - t:.0f} s)", flush=True)
SWEEP[1.0] = R1a
ms = sorted(SWEEP)
sw = np.array([subj(SWEEP[m]) for m in ms])          # (m, subject)
print(pd.DataFrame(sw.T.round(3), index=SUBJECTS, columns=[f"m={m}" for m in ms]).to_string())
avg = sw.mean(1)
print("average over subjects:", dict(zip(ms, avg.round(3))))
print("masked neighbours per electrode:", {m: int(np.ceil(m * 9 - 1e-9)) for m in ms})
steps = np.diff(avg)
print("average decreases at every step:", bool((steps < 0).all()), "steps", steps.round(4).tolist())
mono = (np.diff(sw, axis=0) < 0).all(0)
print("subjects decreasing at every step:", int(mono.sum()), "of 12", [s for s, k in zip(SUBJECTS, mono) if not k])
print("m = 1.0 below m = 0:", avg[-1] < avg[0], f"({avg[-1]:.3f} against {avg[0]:.3f})")
""", "claim:fig4a-mask-sweep-ieeg")

md("""
## fig5a-coverage-ieeg

> In iEEG, reconstruction is best with all electrodes as predictors, and local electrodes alone
> consistently outperform non-local electrodes alone.

All = only the target masked (m = 0 of the sweep); Non-local = target and neighbourhood masked
(m = 1.0); Local = only the 9 neighbours as predictors (Results III E; run_coverage_experiment.py).
""")

code("""
t = time.time()
LOCAL = run_all(0.0, np.random.default_rng(seed("fig5a-coverage-ieeg")), "a", mode="local")
print(f"local done ({time.time() - t:.0f} s)")
cov = pd.DataFrame({"subject": SUBJECTS, "all": subj(SWEEP[0.0]), "local": subj(LOCAL), "non_local": subj(R1a)})
print(cov.round(3).to_string(index=False))
a_, l_, n_ = cov["all"].mean(), cov["local"].mean(), cov["non_local"].mean()
print(f"averages: all {a_:.3f}, local {l_:.3f}, non-local {n_:.3f}; ordered all > local > non-local: {a_ > l_ > n_}")
print("subjects with local above non-local:", int((cov.local > cov.non_local).sum()), "of 12;",
      "with all above local:", int((cov["all"] > cov.local).sum()), "of 12")
""", "claim:fig5a-coverage-ieeg")

code("""
print(f"notebook ran {(time.time() - T0) / 60:.1f} min; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB")
""")
PYEOF
python $TMPDIR/build/nb1.py $TMPDIR/build && echo built || true
```

```
File "/tmp/claude-1001/build/nb1.py", line 157
    code("""
         ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && sed -i 's|    """One SMR condition on every subject, in order, from one generator."""|    # one SMR condition on every subject, in order, from one generator|' nb1.py && python nb1.py $TMPDIR/build && echo built
```

```
built
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open("nb1.py").read()
s=s.replace('''SUBJECTS = [f"sub-{i:02d}" for i in range(1, 13)]''','''SUBJECTS = [f"sub-{i:02d}" for i in range(1, 13)]
if os.environ.get("SMR_TEST"):                 # development only: two subjects
    SUBJECTS = ["sub-07", "sub-04"]
IDX = [int(s[-2:]) - 1 for s in SUBJECTS]''')
for name in ["TAB_INTRA","TAB_INTRA_SD","TAB_CROSS","TAB_CROSS_SD"]:
    import re
    s=re.sub(rf'^{name} = (\[[^\]]*\])', rf'{name} = np.array(\1)[IDX]', s, flags=re.M)
s=s.replace("np.array(TAB_INTRA)","TAB_INTRA").replace("np.array(TAB_INTRA_SD)","TAB_INTRA_SD").replace("np.array(TAB_CROSS)","TAB_CROSS").replace("np.array(TAB_CROSS_SD)","TAB_CROSS_SD")
s+='\nbuild(cells, sys.argv[2])\n'
open("nb1.py","w").write(s)
EOF
grep -n "TAB_INTRA = \|TAB_CROSS = " nb1.py; python nb1.py $TMPDIR/build entries/memar-2026/reproduce_memar_2026.ipynb && echo built
```

```
184:TAB_INTRA = np.array([0.585, 0.647, 0.535, 0.452, 0.524, 0.428, 0.531, 0.487, 0.635, 0.605, 0.612, 0.593])[IDX]
235:TAB_CROSS = np.array([0.331, 0.483, 0.440, 0.325, 0.509, 0.285, 0.415, 0.377, 0.409, 0.363, 0.395, 0.340])[IDX]
built
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/memar-2026 && python - <<'EOF'
s=open("smr.py").read()
s=s.replace('''                locations=",".join(loc))''','''                locations=",".join(loc), times=f["intervals/reaches/start_time"][:])''')
open("smr.py","w").write(s)
import os
p=os.environ["TMPDIR"]+"/build/nb1.py"
s=open(p).read()
s=s.replace('''times = {}
for a in smr.assets():
    f = smr.open_nwb(a["asset_id"])
    times[a["path"]] = f["intervals/reaches/start_time"][:]
''','''times = dict(zip(sv.path, sv.times))
''')
s=s.replace('''print(sv.drop(columns=["subject"]).to_string(index=False))''','''print(sv.drop(columns=["subject", "times"]).to_string(index=False))''')
open(p,"w").write(s)
EOF
cd $TMPDIR/build && python nb1.py $TMPDIR/build entries/memar-2026/reproduce_memar_2026.ipynb; source $TMPDIR/wenv/bin/activate; uv pip install -q nbconvert ipykernel matplotlib 2>&1 | tail -1; date -u
```

```
Sat Nov 21 11:48:13 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/memar-2026 && source $TMPDIR/wenv/bin/activate && SMR_TEST=1 OMP_NUM_THREADS=4 timeout 2400 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/out reproduce_memar_2026.ipynb 2>&1 | tail -5; date -u
```

```
[NbConvertApp] Making directory /tmp/claude-1001/out
[NbConvertApp] Converting notebook reproduce_memar_2026.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 46213 bytes to /tmp/claude-1001/out/reproduce_memar_2026.ipynb
Sat Nov 21 11:54:01 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate; python - <<'EOF'
import nbformat, os
nb=nbformat.read(os.environ["TMPDIR"]+"/out/reproduce_memar_2026.ipynb",4)
for c in nb.cells:
    if c.cell_type=="code":
        for o in c.outputs:
            t=o.get("text") or str(o.get("data",{}).get("text/plain",""))
            print(t[-3500:])
        print("-----")
EOF
```

```
dataset 000055 0.220127.0436

-----
.000000       31            31        True   106          0     16    110   unknown
sub-10/sub-10_ses-3_behavior+ecephys.nwb 43200000       126 500.0    0.000001 volts 24.000000      184           184        True   121          0      0    126   unknown
sub-10/sub-10_ses-4_behavior+ecephys.nwb 43200000       126 500.0    0.000001 volts 24.000000      154           154        True   121          0      0    126   unknown
sub-10/sub-10_ses-5_behavior+ecephys.nwb 43200000       126 500.0    0.000001 volts 24.000000      112           112        True   117          0      0    126   unknown
sub-10/sub-10_ses-6_behavior+ecephys.nwb 43200000       126 500.0    0.000001 volts 24.000000      157           157        True   121          0      0    126   unknown
sub-10/sub-10_ses-7_behavior+ecephys.nwb 43200000       126 500.0    0.000001 volts 24.000000      199           199        True   106          0      0    126   unknown
sub-11/sub-11_ses-3_behavior+ecephys.nwb 43200000       106 500.0    0.000001 volts 24.000000      199           199        True   103          0      0    106   unknown
sub-11/sub-11_ses-4_behavior+ecephys.nwb 43200000       106 500.0    0.000001 volts 24.000000      194           194        True   103          0      0    106   unknown
sub-11/sub-11_ses-5_behavior+ecephys.nwb 43200000       106 500.0    0.000001 volts 24.000000      195           195        True   105          0      0    106   unknown
sub-11/sub-11_ses-6_behavior+ecephys.nwb 43200000       106 500.0    0.000001 volts 24.000000      198           198        True   105          0      0    106   unknown
sub-11/sub-11_ses-7_behavior+ecephys.nwb 43200000       106 500.0    0.000001 volts 24.000000      196           196        True   105          0      0    106   unknown
sub-12/sub-12_ses-3_behavior+ecephys.nwb 43200000       124 500.0    0.000001 volts 24.000000      200           200        True   112          8      4    112   unknown
sub-12/sub
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate && python -c "
import smr, time
t=time.time(); S=smr.load_subject('sub-04', readings=('a',), workers=48); print(time.time()-t, S['a'].shape, S['sessions'])
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
"; free -g | head -2
```

```
63.57634615898132 (390, 84, 1000) [{'path': 'sub-04/sub-04_ses-3_behavior+ecephys.nwb', 'trials': 13, 'dropped_edge': 22, 'dropped_nan': 0, 'nan_in_epoch': 0}, {'path': 'sub-04/sub-04_ses-4_behavior+ecephys.nwb', 'trials': 97, 'dropped_edge': 0, 'dropped_nan': 1, 'nan_in_epoch': 0}, {'path': 'sub-04/sub-04_ses-5_behavior+ecephys.nwb', 'trials': 43, 'dropped_edge': 0, 'dropped_nan': 0, 'nan_in_epoch': 0}, {'path': 'sub-04/sub-04_ses-6_behavior+ecephys.nwb', 'trials': 81, 'dropped_edge': 0, 'dropped_nan': 1, 'nan_in_epoch': 1}, {'path': 'sub-04/sub-04_ses-7_behavior+ecephys.nwb', 'trials': 156, 'dropped_edge': 0, 'dropped_nan': 3, 'nan_in_epoch': 2}]
715.788
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          13
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate && python -c "
import smr, numpy as np
sv=smr.survey()
tot=0; uniq=0
for t in sv.times:
    i=np.round(t*500).astype(int); c=set()
    for x in i:
        c.update(range((x-3000)//84375, (x+3000)//84375+1))
    tot+=len(i); uniq+=len(c)
print(tot, uniq)
"
```

```
8088 5161
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open("smr.py").read()
s=s.replace('''        res = list(ex.map(_read_event, i0[keep]))''','''        # consecutive events to the same worker, so events in the same HDF5 chunk share its cache
        res = list(ex.map(_read_event, i0[keep], chunksize=4))''')
s=s.replace('''def load_session(asset_id, workers=16):''','''def load_session(asset_id, workers=32):''')
s=s.replace('''def load_subject(sub, readings=("a", "b"), workers=16):''','''def load_subject(sub, readings=("a", "b"), workers=32):''')
s=s.replace('''                locations=",".join(loc), times=f["intervals/reaches/start_time"][:])''','''                locations=",".join(loc), times=f["intervals/reaches/start_time"][:],
                reaches_after_end=int((f["intervals/reaches/start_time"][:] * FS
                                       >= es["data"].shape[0]).sum()),
                reach_vs_events_max_diff_s=float(np.abs(
                    f["intervals/reaches/start_time"][:]
                    - f["processing/behavior/ReachEvents/timestamps"][:]).max()))''')
open("smr.py","w").write(s)
EOF
grep -n "same_times" smr.py
```

```
530:                same_times=bool(np.allclose(f["intervals/reaches/start_time"][:],
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open("smr.py").read()
import re
i=s.index("                same_times=bool(")
j=s.index("                good=int(", i)
s=s[:i]+s[j:]
open("smr.py","w").write(s)
EOF
sed -n 515,545p smr.py
```

```
# ----------------------------------------------------------------------------- survey and checks
def survey_file(a):
    """Metadata and array shapes of one file (no signal is read)."""
    f = open_nwb(a["asset_id"])
    es = f["acquisition/ElectricalSeries"]
    el = f["general/extracellular_ephys/electrodes"]
    xyz = np.c_[el["x"][:], el["y"][:], el["z"][:]]
    loc = sorted({s.decode() for s in el["location"][:]})
    return dict(path=a["path"], subject=a["path"].split("/")[0], samples=es["data"].shape[0],
                channels=es["data"].shape[1], rate=float(es["starting_time"].attrs["rate"]),
                conversion=float(es["data"].attrs["conversion"]), unit=es["data"].attrs["unit"],
                hours=es["data"].shape[0] / float(es["starting_time"].attrs["rate"]) / 3600,
                reaches=len(f["intervals/reaches/start_time"]),
                reach_events=len(f["processing/behavior/ReachEvents/timestamps"]),
                good=int(el["good"][:].sum()), no_coords=int(np.isnan(xyz).any(1).sum()),
                x_pos=int((xyz[:, 0] > 0).sum()), x_neg=int((xyz[:, 0] < 0).sum()),
                locations=",".join(loc), times=f["intervals/reaches/start_time"][:],
                reaches_after_end=int((f["intervals/reaches/start_time"][:] * FS
                                       >= es["data"].shape[0]).sum()),
                reach_vs_events_max_diff_s=float(np.abs(
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> smr.py <<'EOF'


def list_file(asset_id):
    """Every group and dataset of one file, with shapes; the columns of each table are its
    datasets."""
    f = open_nwb(asset_id)
    lines = []
    f.visititems(lambda name, obj: lines.append(
        f"{name}  {obj.shape} {obj.dtype}" if isinstance(obj, h5py.Dataset) else f"{name}/"))
    return lines
EOF
python - <<'EOF'
import os
p=os.environ["TMPDIR"]+"/build/nb1.py"
s=open(p).read()
# fix dup check
old_start=s.index('fp = []')
old_end=s.index('""", "sanity")', old_start)
s=s[:old_start]+'''# per session: the channel correlation matrix of the pooled trials (reading a)
fp = []
for s, S in DATA.items():
    start = 0
    for x in S["sessions"]:
        n = x["trials"]
        v = S["a"][start:start + n].transpose(1, 0, 2).reshape(S["a"].shape[1], -1)
        fp.append((x["path"], np.corrcoef(v)))
        start += n
dups = [(fp[i][0], fp[j][0]) for i in range(len(fp)) for j in range(i + 1, len(fp))
        if fp[i][1].shape == fp[j][1].shape and np.allclose(fp[i][1], fp[j][1], atol=1e-3)]
times = dict(zip(sv.path, sv.times))
same_t = [(p, q) for i, p in enumerate(times) for q in list(times)[i + 1:]
          if len(times[p]) == len(times[q]) and np.allclose(times[p], times[q])]
print("session pairs with the same channel correlation matrix:", len(dups), dups)
print("session pairs with identical event times:", len(same_t), same_t)
'''+s[old_end:]
s=s.replace('''print("reaches table and ReachEvents timestamps agree in every file:", bool(sv.same_times.all()))''','''print("largest difference between the reaches table and ReachEvents timestamps (s):",
      sv.reach_vs_events_max_diff_s.max())
print("reach events after the end of the recording:", sv.set_index("path").reaches_after_end[sv.reaches_after_end.values > 0].to_dict())
print()
print("Everything the first file holds:")
print("\\n".join(smr.list_file(smr.assets()[0]["asset_id"])))''')
open(p,"w").write(s)
EOF
grep -n "list_file\|after_end" $TMPDIR/build/nb1.py
```

```
77:print("reach events after the end of the recording:", sv.set_index("path").reaches_after_end[sv.reaches_after_end.values > 0].to_dict())
80:print("\n".join(smr.list_file(smr.assets()[0]["asset_id"])))
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open("nb1.py").read()
i=s.index('md("""\n## fig4a-mask-sweep-ieeg')
j=s.index('code("""\nprint(f"notebook ran')
sweep=s[i:j]
open("sweep_cells.txt","w").write(sweep)
# seed sensitivity cell for intra after the intra cell
seedcell='''
md("""
Seed sensitivity of intra-ieeg-mean (protocol, author step 3): the m = 1.0 run of reading (a) under
the claim's seed plus 1000, 2000, 3000 and 4000. Each draws the initial weights and the batch
order, and its seed also sets the 64/16/20 split (in place of 42).
""")

code("""
t = time.time()
SEEDS = {0: ia}
for add in (1000, 2000, 3000, 4000):
    rng = np.random.default_rng(seed("intra-ieeg-mean") + add)
    SEEDS[add] = subj(run_all(1.0, rng, "a", split_seed=int(seed("intra-ieeg-mean") + add) % 2**32))
    print(f"seed + {add}: mean over subjects {msd(SEEDS[add])} ({time.time() - t:.0f} s)", flush=True)
means = [v.mean() for v in SEEDS.values()]
print(f"range of the mean over the five seeds: {min(means):.3f} to {max(means):.3f}; all within 0.553 ± 0.068: "
      f"{all(abs(m - 0.553) <= 0.068 for m in means)}")
print("per subject range over seeds:", np.ptp(np.array(list(SEEDS.values())), axis=0).round(3).tolist())
""", "claim:intra-ieeg-mean")
'''
k=s.index('md("""\n## table2-ieeg-intra-subjects')
s=s[:k]+seedcell.lstrip()+"\n"+s[k:]
s=s.replace(sweep,"")
open("nb1.py","w").write(s)
EOF
grep -n "^md\|^code" nb1.py | head -40; grep -n "split_seed" entries/memar-2026/smr.py | head
```

```
3:md = lambda s, *t: cells.append(("md", s, *t))
4:code = lambda s, *t: cells.append(("code", s, *t))
6:md("""
12:code at commit 244dcdbd of github.com/neurovium/SpatiallyMaskedRegression.
38:code allows 10000 with a patience of 200). `surrogates_lagged.ipynb` shows on one subject how
42:code("""
62:md("## Data check\n\nMetadata of every file (no signal read), then the trials of every subject.")
64:code("""
84:code("""
99:code("""
114:md("""
121:code("""
140:code("""
149:md("""
161:code("""
184:code("""
200:md("""
206:code("""
219:md("""
229:code("""
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open("nb1.py").read()
s=s.replace('''This notebook tests the claims below. A second notebook, `surrogates_lagged.ipynb`, tests the
surrogate, lagged and full-mask claims.''','''This notebook tests the intra-subject and cross-subject claims. `masking_coverage.ipynb` tests the
mask sweep and the electrode coverage, and `surrogates_lagged.ipynb` the surrogate, lagged and
full-mask claims; each loads the data again.''')
s=s.replace('''| fig4a-mask-sweep-ieeg | tested |
| fig5a-coverage-ieeg | tested |
| lagged-ieeg-no-gain''','''| fig4a-mask-sweep-ieeg, fig5a-coverage-ieeg | tested in `masking_coverage.ipynb` |
| lagged-ieeg-no-gain''')
open("nb1.py","w").write(s)

pre = s[:s.index('md("## Data check')]
# preamble for nb2/3
def preamble(title, intro):
    p = pre
    a = p.index('md("""')
    b = p.index('code("""', a)
    hdr = 'md("""\n# ' + title + '\n\n' + intro + '\n""")\n\n'
    return p[:a] + hdr + p[b:]
light = '''
md("## Data check\\n\\nThe trials of every subject, preprocessed as in `reproduce_memar_2026.ipynb` (reading a only; its data check covers the metadata, duplicates and the clock).")

code("""
t = time.time()
DATA = {}
for s in SUBJECTS:
    S = smr.load_subject(s, readings=("a",))
    DATA[s] = smr.drop_uncoordinated(S)
    x = DATA[s]["a"]
    print(s, "sessions", len(S["sessions"]), "trials", x.shape[0], "electrodes", x.shape[1], "samples", x.shape[2],
          "dropped without coordinates", DATA[s]["n_dropped_el"], f"range {x.min():.2f} to {x.max():.2f}, SD {x.std():.3f}",
          f"({time.time() - t:.0f} s)", flush=True)
print("trials in all", sum(S["a"].shape[0] for S in DATA.values()))
print("peak memory MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3)
""", "sanity")

code("""
def run_all(m, rng, reading="a", **kw):
    # one SMR condition on every subject, in order, from one generator
    out = {}
    for s in SUBJECTS:
        S = DATA[s]
        out[s] = smr.run_smr(S[reading].astype(np.float32), smr.neighbours(S["xyz"]), m, rng,
                             decim=DECIM, max_epoch=MAX_EPOCH, **kw)
    return out

def subj(res):
    return np.array([res[s]["dc"].mean() for s in SUBJECTS])

def msd(v):
    return f"{np.mean(v):.3f} ± {np.std(v):.3f}"
""")
'''
open("pre2.txt","w").write(preamble("Spatially Masked Regression on AJILE12: mask sweep and electrode coverage", '''Ostadsharif Memar & Dehghani (2026), arXiv:2606.11415, on DANDI:000055 version 0.220127.0436
(the only published version; see `reproduce_memar_2026.ipynb` for the header, the version choice
and the full data check). Claims tested here: fig4a-mask-sweep-ieeg and fig5a-coverage-ieeg.
Settings and deviations as in `reproduce_memar_2026.ipynb` (every 10th sample for the gradient
steps, 200 epochs).''') + light)
open("pre3.txt","w").write(preamble("Spatially Masked Regression on AJILE12: surrogates, lagged model and full masking", '''Ostadsharif Memar & Dehghani (2026), arXiv:2606.11415, on DANDI:000055 version 0.220127.0436
(the only published version; see `reproduce_memar_2026.ipynb` for the header, the version choice
and the full data check). Claims tested here: surrogate-ieeg, surrogate-order-ieeg,
lagged-ieeg-no-gain and full-mask-above-zero-ieeg (which uses the mask sweep's m = 1.0 values; the
m = 1.0 run is repeated here with this notebook's generator). Settings and deviations as in
`reproduce_memar_2026.ipynb`; the last section shows how much they change the score on one
subject.''') + light)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
sw=open("sweep_cells.txt").read()
sw=sw.replace("ceil(m × 9) neighbours drawn at random per electrode (Results III D); m = 1.0 is the run above.",
 "ceil(m × 9) neighbours drawn at random per electrode (Results III D), m in 0, 0.25, 0.5, 0.75 and 1.0, one generator for the whole sweep. The code's rule, round(m × 9), differs at m = 0.25 (2 in place of 3) and m = 0.5 (4 in place of 5), and is shown as a variant.")
sw=sw.replace('''for m in (0.0, 0.25, 0.5, 0.75):
    SWEEP[m] = run_all(m, rng_sweep, "a")
    print(f"m = {m} done ({time.time() - t:.0f} s)", flush=True)
SWEEP[1.0] = R1a
''','''for m in (0.0, 0.25, 0.5, 0.75, 1.0):
    SWEEP[m] = run_all(m, rng_sweep, "a")
    print(f"m = {m} done ({time.time() - t:.0f} s)", flush=True)
''')
sw=sw.replace('''print("m = 1.0 below m = 0:", avg[-1] < avg[0], f"({avg[-1]:.3f} against {avg[0]:.3f})")
"""''','''print("m = 1.0 below m = 0:", avg[-1] < avg[0], f"({avg[-1]:.3f} against {avg[0]:.3f})")
print("m = 1.0 values for full-mask-above-zero-ieeg:", dict(zip(SUBJECTS, sw[-1].round(3))), "average", round(avg[-1], 3))
"""''')
sw=sw.replace('''md("""
## fig5a-coverage-ieeg''','''md("Variant: the code's round(m × 9) at m = 0.25 and 0.5 (a second generator for the claim).")

code("""
rng_round = np.random.default_rng(seed("fig4a-mask-sweep-ieeg") + 1)
ROUND = {m: subj(run_all(m, rng_round, "a", rule="round")) for m in (0.25, 0.5)}
alt = [sw[0].mean(), ROUND[0.25].mean(), ROUND[0.5].mean(), sw[3].mean(), sw[4].mean()]
print("averages with round at 0.25 and 0.5:", np.round(alt, 3).tolist(), "; decreasing at every step:",
      bool((np.diff(alt) < 0).all()))
print("subjects decreasing at every step with round:",
      int((np.diff(np.array([sw[0], ROUND[0.25], ROUND[0.5], sw[3], sw[4]]), axis=0) < 0).all(0).sum()), "of 12")
""", "claim:fig4a-mask-sweep-ieeg")

md("""
## fig5a-coverage-ieeg''')
sw=sw.replace('''"non_local": subj(R1a)})''','''"non_local": subj(SWEEP[1.0])})''')
sw=sw.replace("(m = 0 of the sweep); Non-local = target and neighbourhood masked\n(m = 1.0)","(m = 0 of the sweep); Non-local = target and neighbourhood masked\n(m = 1.0 of the sweep)")
s=open("pre2.txt").read()+sw+'''
code("""
print(f"notebook ran {(time.time() - T0) / 60:.1f} min; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB")
""")

build(cells, sys.argv[2])
'''
open("nb2.py","w").write(s)
EOF
python nb2.py $TMPDIR/build entries/memar-2026/masking_coverage.ipynb && echo ok; python nb1.py $TMPDIR/build entries/memar-2026/reproduce_memar_2026.ipynb && echo ok1
```

```
ok
ok1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/memar-2026 && python - <<'EOF'
s=open("smr.py").read()
i=s.index("def surrogate(x, kind, rng):")
j=s.index("# ----------------------------------------------------------------------------- cross-subject")
s=s[:i]+'''def surrogate(x, kind, rng, batch=20000):
    """Surrogate of every trial and channel independently (Algorithm 4), vectorised over rows:
    the same operations as `shuffle_phase`, `iaaft` and `block_shuffle`, with each row's
    permutation drawn by `rng.permuted` (the draws differ from a per-row loop; a standard choice).
    x: (trials, ch, time)."""
    shp = x.shape
    rows = x.reshape(-1, shp[-1]).astype(np.float64)
    out = np.empty_like(rows)
    n = shp[-1]
    for s in range(0, len(rows), batch):
        r = rows[s:s + batch]
        if kind == "phase":
            F = np.fft.fft(r, axis=1)
            amp, ph = np.abs(F), np.angle(F)
            pos = np.arange(1, n // 2)
            rp = rng.permuted(ph[:, pos], axis=1)
            ph[:, pos] = rp
            ph[:, n - pos] = -rp
            out[s:s + batch] = np.fft.ifft(amp * np.exp(1j * ph), axis=1).real
        elif kind == "iaaft":
            srt = np.sort(r, axis=1)
            mag = np.abs(np.fft.fft(r, axis=1))
            z = rng.permuted(r, axis=1)
            for _ in range(5):
                zn = np.fft.ifft(mag * np.exp(1j * np.angle(np.fft.fft(z, axis=1))), axis=1).real
                z = np.take_along_axis(srt, np.argsort(np.argsort(zn, axis=1), axis=1), axis=1)
            out[s:s + batch] = z
        elif kind == "block":
            B = 250
            nb, rem = n // B, n % B
            perm = np.argsort(rng.random((len(r), nb)), axis=1)
            idx = (perm[:, :, None] * B + np.arange(B)).reshape(len(r), nb * B)
            if rem:
                idx = np.concatenate([idx, np.broadcast_to(np.arange(nb * B, n), (len(r), rem))], 1)
            out[s:s + batch] = np.take_along_axis(r, idx, axis=1)
    return out.reshape(shp).astype(np.float32)


'''+s[j:]
open("smr.py","w").write(s)
EOF
source $TMPDIR/wenv/bin/activate; python -c "
import smr, numpy as np, time
rng=np.random.default_rng(0)
x=np.random.randn(100,64,1000).astype(np.float32)
for k in ('phase','iaaft','block'):
    t=time.time(); y=smr.surrogate(x,k,rng); print(k, time.time()-t)
    # checks
    r=x[3,5].astype(float); q=y[3,5]
    print(' amp spectrum equal', np.allclose(np.abs(np.fft.fft(r)), np.abs(np.fft.fft(q)), rtol=1e-3, atol=1e-2), 'sorted equal', np.allclose(np.sort(r), np.sort(q), atol=1e-5), 'corr', np.corrcoef(r,q)[0,1].round(3))
q=smr.shuffle_phase(r, rng); print('loop phase amp eq', np.allclose(np.abs(np.fft.fft(r)), np.abs(np.fft.fft(q))))
"
```

```
phase 0.35810232162475586
 amp spectrum equal True sorted equal False corr 0.037
iaaft 3.115621566772461
 amp spectrum equal False sorted equal True corr -0.022
block 0.04201769828796387
 amp spectrum equal False sorted equal True corr -0.104
loop phase amp eq True
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open("smr.py").read()
s=s.replace('''                z = np.take_along_axis(srt, np.argsort(np.argsort(zn, axis=1), axis=1), axis=1)''','''                z = np.empty_like(zn)
                np.put_along_axis(z, np.argsort(zn, axis=1), srt, axis=1)''')
open("smr.py","w").write(s)
EOF
source $TMPDIR/wenv/bin/activate; python -c "
import smr, numpy as np, time
rng=np.random.default_rng(0)
x=np.random.randn(100,64,1000).astype(np.float32)
t=time.time(); y=smr.surrogate(x,'iaaft',rng); print(time.time()-t)
r=x[3,5].astype(float); q=y[3,5]; print(np.allclose(np.sort(r), np.sort(q), atol=1e-5))
r2=smr.iaaft(r, np.random.default_rng(1)); print('loop version spectrum err', np.abs(np.abs(np.fft.fft(r2))-np.abs(np.fft.fft(r))).mean(), 'vec', np.abs(np.abs(np.fft.fft(q))-np.abs(np.fft.fft(r))).mean())
"
```

```
2.4144017696380615
True
loop version spectrum err 0.16531962074397114 vec 0.19282360111096886
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && cat > nb3_tail.txt <<'PYEOF'
md("""
## Instantaneous model at m = 1.0

The baseline for the surrogate and lagged comparisons, and the m = 1.0 values for
full-mask-above-zero-ieeg: the common pipeline at m = 1.0, reading (a), with the generator of
lagged-ieeg-no-gain (the lagged run below continues from it).
""")

code("""
t = time.time()
rng_lag = np.random.default_rng(seed("lagged-ieeg-no-gain"))
INST = run_all(1.0, rng_lag, "a")
inst = subj(INST)
print(f"instantaneous m = 1.0: {msd(inst)} ({time.time() - t:.0f} s)")
print(dict(zip(SUBJECTS, inst.round(3))))
""")

md("""
## surrogate-ieeg

> On iEEG surrogates, intra-subject DistCorr falls from 0.553 to 0.181 (phase shuffle), 0.232
> (IAAFT) and 0.201 (block shuffle).

Surrogates of every preprocessed trial and channel, then the common pipeline at m = 1.0 (one
generator for the claim, used for the surrogate draws and the fits). Reading (b) of the criterion
(end-matched segments before the phase shuffle) is not run: trimming each trial and channel to its
own best-matching segment gives series of different lengths, and neither the paper nor the code
says how they are put back into trials of one length.
""")

code("""
TAB_SUR = {"phase": (0.181, 0.029), "iaaft": (0.232, 0.060), "block": (0.201, 0.168)}
TAB_SUR_SUBJ = {"phase": None, "iaaft": None, "block": None}
t = time.time()
rng_sur = np.random.default_rng(seed("surrogate-ieeg"))
SUR = {}
for kind in ("phase", "iaaft", "block"):
    res = {}
    for s in SUBJECTS:
        S = DATA[s]
        xs = smr.surrogate(S["a"], kind, rng_sur)
        res[s] = smr.run_smr(xs, smr.neighbours(S["xyz"]), 1.0, rng_sur, decim=DECIM, max_epoch=MAX_EPOCH)
        del xs
    SUR[kind] = subj(res)
    v = SUR[kind]
    exp, tol = TAB_SUR[kind]
    print(f"{kind}: {msd(v)}; within {exp} ± {tol}: {abs(v.mean() - exp) <= tol}; below the original "
          f"({inst.mean():.3f}): {v.mean() < inst.mean()}; subjects below their original: {int((v < inst).sum())} of 12 "
          f"({time.time() - t:.0f} s)", flush=True)
print(pd.DataFrame({"subject": SUBJECTS, "original": inst, **SUR}).round(3).to_string(index=False))
ok = all(abs(SUR[k].mean() - TAB_SUR[k][0]) <= TAB_SUR[k][1] and SUR[k].mean() < inst.mean() for k in SUR)
print("all three within tolerance and below the original:", ok)
""", "claim:surrogate-ieeg")

md("""
## surrogate-order-ieeg

> In iEEG, phase shuffling degrades reconstruction most on average, and IAAFT surrogates retain
> somewhat more reconstructability.
""")

code("""
avgs = {k: round(float(v.mean()), 3) for k, v in SUR.items()}
print("averages:", avgs)
print("phase shuffle lowest of the three:", min(avgs, key=avgs.get) == "phase")
print("IAAFT above phase (reading a):", avgs["iaaft"] > avgs["phase"], "; order of Table II, phase < block < IAAFT (reading b):",
      avgs["phase"] < avgs["block"] < avgs["iaaft"])
print("subjects with phase lowest:", int(sum(SUR["phase"][i] < min(SUR["iaaft"][i], SUR["block"][i]) for i in range(len(SUBJECTS)))), "of 12")
""", "claim:surrogate-order-ieeg")

md("""
## full-mask-above-zero-ieeg

> With the whole local neighborhood masked, iEEG reconstruction remains above zero, so the target
> signal is not determined by its immediate neighborhood alone.

The criterion takes the m = 1.0 values of the mask sweep; they are recomputed here (the run above)
to compare them with the phase-shuffled surrogate in one notebook. `masking_coverage.ipynb` prints
the sweep's own m = 1.0 values.
""")

code("""
print(f"(a) m = 1.0 average {inst.mean():.3f} > 0: {inst.mean() > 0}; smallest electrode value "
      f"{min(INST[s]['dc'].min() for s in SUBJECTS):.3f}")
print(f"(b) m = 1.0 average {inst.mean():.3f} against the phase-shuffled average {SUR['phase'].mean():.3f}: "
      f"above {inst.mean() > SUR['phase'].mean()}; subjects above their own phase-shuffled value: "
      f"{int((inst > SUR['phase']).sum())} of 12")
""", "claim:full-mask-above-zero-ieeg")

md("""
## lagged-ieeg-no-gain

> Adding lagged predictors (0, 20, 30, 50 and 60 ms) barely changes iEEG reconstruction (0.554 ±
> 0.067 against 0.553 ± 0.068).
""")

code("""
t = time.time()
print("lag offsets in samples:", smr.lag_samples())
LAG = run_all(1.0, rng_lag, "a", lagged=True)
lag = subj(LAG)
d = lag - inst
print(f"lagged {msd(lag)} against instantaneous {msd(inst)} ({time.time() - t:.0f} s)")
print(f"lagged average within 0.554 ± 0.067: {abs(lag.mean() - 0.554) <= 0.067}; "
      f"difference {lag.mean() - inst.mean():+.4f}, {100 * (lag.mean() - inst.mean()) / inst.mean():+.1f}% of the "
      f"instantaneous average; under 10%: {abs(lag.mean() - inst.mean()) < 0.1 * inst.mean()}")
print("per subject lagged minus instantaneous:", dict(zip(SUBJECTS, d.round(4))))
w = stats.wilcoxon(lag, inst)
print(f"context only: Wilcoxon signed-rank over subjects, statistic {w.statistic}, p = {w.pvalue:.4f}; "
      f"subjects with a gain {int((d > 0).sum())} of 12")
""", "claim:lagged-ieeg-no-gain")

md("""
## How much the speed deviations change the score

On sub-07, the m = 1.0 model is trained as the paper's code does it (every sample, early stopping
with a patience of 200 epochs, up to 10000 epochs) only in part, for time: (1) every 10th sample
with early stopping up to 10000 epochs, (2) every sample for 200 epochs, against this attempt's
setting (every 10th sample, 200 epochs). A generator for this check only.
""")

code("""
S = DATA["sub-07"]
nbr = smr.neighbours(S["xyz"])
t = time.time()
chk = {}
for label, decim, me in (("this attempt: every 10th sample, 200 epochs", 10, 200),
                         ("every 10th sample, up to 10000 epochs, patience 200", 10, 10000),
                         ("every sample, 200 epochs", 1, 200)):
    r = smr.run_smr(S["a"], nbr, 1.0, np.random.default_rng(seed("intra-ieeg-mean") + 9), decim=decim, max_epoch=me)
    chk[label] = r["dc"].mean()
    print(f"{label}: mean DistCorr {r['dc'].mean():.4f}, epochs run {r['n_ep']}, "
          f"median best epoch {int(np.median(r['best_ep']))} ({time.time() - t:.0f} s)", flush=True)
print("largest difference from this attempt's setting:", round(max(abs(v - chk[list(chk)[0]]) for v in chk.values()), 4))
""")

code("""
print(f"notebook ran {(time.time() - T0) / 60:.1f} min; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB")
""")

build(cells, sys.argv[2])
PYEOF
cat pre3.txt nb3_tail.txt > nb3.py && python nb3.py $TMPDIR/build entries/memar-2026/surrogates_lagged.ipynb && echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/memar-2026 && sed -i '/TAB_SUR_SUBJ/d' $TMPDIR/build/nb3.py && python $TMPDIR/build/nb3.py $TMPDIR/build surrogates_lagged.ipynb && source $TMPDIR/wenv/bin/activate && date -u && for nb in reproduce_memar_2026 masking_coverage surrogates_lagged; do SMR_TEST=1 OMP_NUM_THREADS=4 timeout 2400 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/out $nb.ipynb 2>&1 | grep -v WARNING | tail -3; date -u; done
```

```
Sat Nov 21 11:58:26 UTC 2026
[31mSyntaxError[39m[31m:[39m unterminated string literal (detected at line 16)


Sat Nov 21 11:58:28 UTC 2026
[NbConvertApp] Converting notebook masking_coverage.ipynb to notebook
[NbConvertApp] Writing 13488 bytes to /tmp/claude-1001/out/masking_coverage.ipynb
Sat Nov 21 12:03:21 UTC 2026
[NbConvertApp] Converting notebook surrogates_lagged.ipynb to notebook
[NbConvertApp] Writing 19485 bytes to /tmp/claude-1001/out/surrogates_lagged.ipynb
Sat Nov 21 12:13:11 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/wenv/bin/activate; cat > $TMPDIR/show.py <<'EOF'
import nbformat, sys
nb=nbformat.read(sys.argv[1],4)
for c in nb.cells:
    if c.cell_type=="code":
        for o in c.outputs:
            t=o.get("text") or str(o.get("data",{}).get("text/plain","")) or "".join(o.get("traceback",[]))[-2000:]
            print(t[-int(sys.argv[2]) if len(sys.argv)>2 else -3000:])
        print("-----")
EOF
python $TMPDIR/show.py $TMPDIR/out/masking_coverage.ipynb; python $TMPDIR/show.py $TMPDIR/out/surrogates_lagged.ipynb
```

```
dataset 000055 0.220127.0436

-----
sub-07 sessions 5 trials 794 electrodes 64 samples 1000 dropped without coordinates 0 range -5.73 to 5.83, SD 1.000 (85 s)

sub-04 sessions 5 trials 390 electrodes 84 samples 1000 dropped without coordinates 0 range -9.42 to 9.69, SD 1.000 (150 s)

trials in all 1184
peak memory MB 1196.94

-----
-----
m = 0.0 done (23 s)

m = 0.25 done (40 s)

m = 0.5 done (56 s)

m = 0.75 done (73 s)

[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && grep -n 'join(smr.list_file' nb1.py && sed -i 's|print("\\n".join(smr.list_file|print("\\\\n".join(smr.list_file|' nb1.py && grep -n 'join(smr.list_file' nb1.py; python - <<'EOF'
s=open("nb3.py").read()
s=s.replace('''for label, decim, me in (("this attempt: every 10th sample, 200 epochs", 10, 200),
                         ("every 10th sample, up to 10000 epochs, patience 200", 10, 10000),
                         ("every sample, 200 epochs", 1, 200)):''','''for label, decim, me in (("this attempt: every 10th sample, 200 epochs", 10, 200),
                         ("every 10th sample, up to 3000 epochs, patience 200", 10, 3000),
                         ("every sample, 100 epochs", 1, 100)):''')
s=s.replace('''On sub-07, the m = 1.0 model is trained as the paper's code does it (every sample, early stopping
with a patience of 200 epochs, up to 10000 epochs) only in part, for time: (1) every 10th sample
with early stopping up to 10000 epochs, (2) every sample for 200 epochs, against this attempt's
setting (every 10th sample, 200 epochs). A generator for this check only.''','''On sub-07, the m = 1.0 model is trained closer to the paper's code (every sample, early stopping
with a patience of 200 epochs, up to 10000 epochs) in two parts, for time: (1) every 10th sample
with early stopping up to 3000 epochs, (2) every sample for 100 epochs, against this attempt's
setting (every 10th sample, 200 epochs). A generator for this check only.''')
open("nb3.py","w").write(s)
EOF
cd entries/memar-2026 && python $TMPDIR/build/nb3.py $TMPDIR/build surrogates_lagged.ipynb && python $TMPDIR/build/nb1.py $TMPDIR/build reproduce_memar_2026.ipynb && source $TMPDIR/wenv/bin/activate && SMR_TEST=1 OMP_NUM_THREADS=4 timeout 2400 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/out reproduce_memar_2026.ipynb 2>&1 | grep -v WARNING | tail -3; date -u; python $TMPDIR/show.py $TMPDIR/out/reproduce_memar_2026.ipynb 2500 | grep -v "^sub-.*nwb  " | head -150
```

```
80:print("\n".join(smr.list_file(smr.assets()[0]["asset_id"])))
80:print("\\n".join(smr.list_file(smr.assets()[0]["asset_id"])))
[NbConvertApp] Converting notebook reproduce_memar_2026.ipynb to notebook
[NbConvertApp] Writing 52428 bytes to /tmp/claude-1001/out/reproduce_memar_2026.ipynb
Sat Nov 21 12:20:50 UTC 2026
dataset 000055 0.220127.0436

-----
   0.000001 volts 24.000000      198           198   105          0      0    106   unknown                  0                       0.001
sub-11/sub-11_ses-7_behavior+ecephys.nwb 43200000       106 500.0    0.000001 volts 24.000000      196           196   105          0      0    106   unknown                  0                       0.001
sub-12/sub-12_ses-3_behavior+ecephys.nwb 43200000       124 500.0    0.000001 volts 24.000000      200           200   112          8      4    112   unknown                  0                       0.001
sub-12/sub-12_ses-4_behavior+ecephys.nwb 43200000       124 500.0    0.000001 volts 24.000000      200           200   115          8      4    112   unknown                  0                       0.001
sub-12/sub-12_ses-5_behavior+ecephys.nwb 43200000       124 500.0    0.000001 volts 24.000000      200           200   113          8      4    112   unknown                  0                       0.001
sub-12/sub-12_ses-6_behavior+ecephys.nwb 43200000       124 500.0    0.000001 volts 24.000000      197           197   113          8      4    112   unknown                  0                       0.001
sub-12/sub-12_ses-7_behavior+ecephys.nwb 43200000       124 500.0    0.000001 volts 24.000000      199           199   111          8      4    112   unknown                  0                       0.001

files 55 subjects 12 sessions per subject {'sub-01': 4, 'sub-02': 4, 'sub-03': 4, 'sub-04': 5, 'sub-05': 3, 'sub-06': 5, 'sub-07': 5, 'sub-08': 5, 'sub-09': 5, 'sub-10': 5, 'sub-11': 5, 'sub-12': 5}
sampling rates [np.float64(500.0)] units ['volts'] conversion [np.float64(1e-
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open("nb1.py").read()
s=s.replace('''print("largest difference between the reaches table and ReachEvents timestamps (s):",
      sv.reach_vs_events_max_diff_s.max())''','''print("files whose reaches table and ReachEvents timestamps differ by more than 10 ms:",
      sv.set_index("path").reach_vs_events_max_diff_s[sv.reach_vs_events_max_diff_s.values > 0.01].to_dict(),
      "; largest difference elsewhere (s):", sv.reach_vs_events_max_diff_s[sv.reach_vs_events_max_diff_s <= 0.01].max())''')
open("nb1.py","w").write(s)
EOF
cd entries/memar-2026 && python $TMPDIR/build/nb1.py $TMPDIR/build reproduce_memar_2026.ipynb && cat > requirements.in <<'EOF'
dcor
h5py
matplotlib
numba
numpy
pandas
remfile
requests
scikit-learn
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: memar-2026
type: reproduction
title: Spatially masked regression on AJILE12 iEEG (Ostadsharif Memar and Dehghani 2026)
description: Tests the iEEG findings of Ostadsharif Memar and Dehghani (2026) on AJILE12, dandiset
  000055, which holds the intracranial recordings and wrist movement events of the paper's 12
  subjects. It fits the spatially masked linear reconstruction model to 2 s trials around movement
  events and tests intra-subject and cross-subject reconstruction, the effect of masking the local
  neighbourhood, electrode coverage, surrogate data and lagged predictors. The paper's scalp EEG
  data are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_memar_2026.ipynb
  title: Intra-subject and cross-subject reconstruction of AJILE12 iEEG
  runtime_minutes: 35
- path: masking_coverage.ipynb
  title: Local masking and electrode coverage
  runtime_minutes: 35
- path: surrogates_lagged.ipynb
  title: Surrogate data, lagged predictors and full local masking
  runtime_minutes: 40
helpers:
- smr.py
related:
- id: dandi:000055/0.220127.0436
  relation: uses_data
- id: doi:10.48550/arxiv.2606.11415
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/memar-2026 2>&1 | tail -3; python tools/entry.py check entries/memar-2026 2>&1 | tail -10; date -u
```

```
wrote memar-2026/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
Sat Nov 21 12:21:30 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && sed -i 's|rng = np.random.default_rng(seed("intra-ieeg-mean") + 7)   # a generator for the data check only|rng = np.random.default_rng(seed("intra-ieeg-mean") + 2)   # third generator of the claim, for the clock check|' nb1.py && sed -i 's|np.random.default_rng(seed("intra-ieeg-mean") + 9)|np.random.default_rng(seed("intra-ieeg-mean") + 3)|; s|A generator for this check only.|The generator is the fourth of intra-ieeg-mean (its seed plus 3).|' nb3.py && grep -c 'intra-ieeg-mean") + 2' nb1.py && grep -c 'intra-ieeg-mean") + 3' nb3.py && cd entries/memar-2026 && python $TMPDIR/build/nb1.py $TMPDIR/build reproduce_memar_2026.ipynb && python $TMPDIR/build/nb3.py $TMPDIR/build surrogates_lagged.ipynb && python $TMPDIR/build/nb2.py $TMPDIR/build masking_coverage.ipynb && cd  && date -u && timeout 7000 python tools/entry.py all entries/memar-2026 2>&1 | tail -30; date -u
```

```
Exit code 143
Command timed out after 1h 0m 0s
1
1
Sat Nov 21 12:21:45 UTC 2026
```

**Agent calls Bash**

```bash
date -u; ls -la executed/memar-2026/ 2>&1; cat executed/memar-2026/result.json 2>&1 | head; ps aux | grep -c nbconvert
```

```
Sat Nov 21 13:21:49 UTC 2026
total 72
drwxr-xr-x 3 runner runner  4096 Nov 21 13:07 .
drwxr-xr-x 3 runner runner  4096 Nov 21 12:21 ..
drwxr-xr-x 5 runner runner  4096 Nov 21 12:21 .venv
-rw-r--r-- 1 runner runner 60232 Nov 21 13:07 reproduce_memar_2026.ipynb
cat: executed/memar-2026/result.json: No such file or directory
3
```

**Agent calls Bash**

```bash
pkill -f nbconvert; pkill -f ipykernel; sleep 1; ps aux | grep -E "nbconvert|ipykernel" | grep -v grep | wc -l; source $TMPDIR/wenv/bin/activate; python $TMPDIR/show.py executed/memar-2026/reproduce_memar_2026.ipynb 4000 | grep -v "^sub-.*nwb  \|^specifications\|^processing\|^general\|^acquisition\|^intervals\|^analysis\|^stimulus\|^file_create\|^identifier\|^session_\|^timestamps_ref\|^units"
```

```
Exit code 143
```

**Agent calls Bash**

```bash
ps aux | grep -E "jupyter|ipykernel" | grep -v grep | awk '{print $2}' | xargs -r kill; sleep 1; ps aux | grep -E "jupyter|ipykernel" | grep -v grep | wc -l
```

```
0
```

**Agent**

Now start the remaining two notebooks in the entry's locked environment (the `all` run was cut at the tool's 60-minute limit after the first notebook finished).

**Agent calls Bash**

```bash
cd entries/memar-2026 && V=executed/memar-2026/.venv && date -u && for nb in masking_coverage surrogates_lagged; do s=$(date +%s); JUPYTER_PATH=$V/share/jupyter $V/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=6000 --ExecutePreprocessor.kernel_name=registry-memar-2026 --output-dir executed/memar-2026 --output $nb.ipynb $nb.ipynb 2>&1 | grep -v WARNING | tail -2; echo "$nb $(( $(date +%s) - s )) s"; done; date -u
```

```
Sat Nov 21 13:22:07 UTC 2026
[NbConvertApp] Converting notebook masking_coverage.ipynb to notebook
[NbConvertApp] Writing 17256 bytes to executed/memar-2026/masking_coverage.ipynb
masking_coverage 2512 s
[NbConvertApp] Converting notebook surrogates_lagged.ipynb to notebook
[NbConvertApp] Writing 23106 bytes to executed/memar-2026/surrogates_lagged.ipynb
surrogates_lagged 2506 s
Sat Nov 21 14:45:45 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/memar-2026; source $TMPDIR/wenv/bin/activate; python $TMPDIR/show.py reproduce_memar_2026.ipynb 3500 | grep -v "^sub-.*nwb  \|^specifications\|^processing\|^general\|^acquisition\|^intervals\|^analysis\|^stimulus\|^file_create\|^identifier\|^session_\|^timestamps_ref\|^units" | tail -120
```

```
sub-12 trials 986 electrodes 116 dropped without coordinates 8 events dropped at file edges 0 dropped for NaN in the padded window 10 of which NaN in the 2 s epoch 7 (1353 s)

peak memory MB 6442.536

-----
subject  trials  electrodes  samples      a_min     a_max     a_sd      b_min     b_max  hemisphere_x_neg  x_pos  good_false  sessions
 sub-01     603          94     1000 -20.664747 19.954464 1.000025  -6.750000  7.128906                94      0           9         4
 sub-02     301          86     1000  -9.720924  9.524643 1.000007  -6.210938  6.925781                 0     86           1         4
 sub-03     642          80     1000 -22.063131 22.506958 1.000023  -5.878906  8.851562                80      0           1         4
 sub-04     390          84     1000  -9.421446  9.686454 1.000011  -5.835938  6.851562                 0     84          17         5
 sub-05     267         106     1000 -23.567358 23.722071 1.000016  -5.957031  6.785156                 0    106           2         3
 sub-06     844          80     1000 -19.915827 20.793173 1.000022 -10.351562  8.296875                79      1          10         5
 sub-07     794          64     1000  -5.727464  5.833453 1.000019  -6.292969  6.878906                 0     64           1         5
 sub-08     952          92     1000  -7.161022  7.058645 1.000024  -9.515625 10.125000                 0     92           9         5
 sub-09     211         126     1000  -6.652214  6.321128 1.000009  -6.765625  7.140625               110     16           2         5
 sub-10     757         126     1000  -8.241361  8.334767 1.000023 -11.070312 10.101562               126      0           5         5
 sub-11     971         106     1000  -7.285220  7.445350 1.000032  -7.585938  8.968750               106      0           3         5
 sub-12     986         116     1000  -9.765090  8.310636 1.000031  -7.164062  7.921875               112      4           4         5
trials in all: 7718

[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/memar-2026; source $TMPDIR/wenv/bin/activate; python $TMPDIR/show.py reproduce_memar_2026.ipynb 3500 | grep -A3 "^files 55\|reaches table\|after the end"; python $TMPDIR/show.py masking_coverage.ipynb | tail -45; python $TMPDIR/show.py surrogates_lagged.ipynb | tail -60
```

```
files 55 subjects 12 sessions per subject {'sub-01': 4, 'sub-02': 4, 'sub-03': 4, 'sub-04': 5, 'sub-05': 3, 'sub-06': 5, 'sub-07': 5, 'sub-08': 5, 'sub-09': 5, 'sub-10': 5, 'sub-11': 5, 'sub-12': 5}
sampling rates [np.float64(500.0)] units ['volts'] conversion [np.float64(1e-06)]
channels per subject {'sub-01': {'min': 94, 'max': 94}, 'sub-02': {'min': 86, 'max': 86}, 'sub-03': {'min': 96, 'max': 96}, 'sub-04': {'min': 84, 'max': 84}, 'sub-05': {'min': 106, 'max': 106}, 'sub-06': {'min': 80, 'max': 80}, 'sub-07': {'min': 64, 'max': 64}, 'sub-08': {'min': 92, 'max': 92}, 'sub-09': {'min': 126, 'max': 126}, 'sub-10': {'min': 126, 'max': 126}, 'sub-11': {'min': 106, 'max': 106}, 'sub-12': {'min': 124, 'max': 124}}
location labels in the electrode tables ['unknown']
files whose reaches table and ReachEvents timestamps differ by more than 10 ms: {'sub-01/sub-01_ses-7_behavior+ecephys.nwb': 30682.415000000015, 'sub-04/sub-04_ses-3_behavior+ecephys.nwb': 30048.323000000008, 'sub-06/sub-06_ses-3_behavior+ecephys.nwb': 29240.56700000001, 'sub-08/sub-08_ses-4_behavior+ecephys.nwb': 86400.0} ; largest difference elsewhere (s): 0.0010000000183936208
reach events after the end of the recording: {'sub-01/sub-01_ses-7_behavior+ecephys.nwb': 132, 'sub-04/sub-04_ses-3_behavior+ecephys.nwb': 22, 'sub-06/sub-06_ses-3_behavior+ecephys.nwb': 83, 'sub-08/sub-08_ses-4_behavior+ecephys.nwb': 1}

Everything the first file holds:

sub-01  0.672   0.650  0.624   0.600  0.580
sub-02  0.806   0.780  0.763   0.745  0.718
sub-03  0.736   0.697  0.673   0.656  0.627
sub-04  0.708   0.627  0.587   0.561  0.529
sub-05  0.673   0.653  0.638   0.621  0.605
sub-06  0.604   0.561  0.541   0.520  0.502
sub-07  0.788   0.717  0.689   0.668  0.645
sub-08  0.684   0.613  0.585   0.555  0.533
sub-09  0.767   0.744  0.722   0.687  0.648
sub-10  0.714   0.686  0.662   0.640  0.598
sub-11  0.670   0.652  0.638   0.618  0.594
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/results.py <<'PYEOF'
import nbformat, sys
R = {
"reproduce_memar_2026.ipynb": {
"claim:intra-ieeg-mean": "**Result: reproduced.** The mean over the 12 subjects is 0.602 ± 0.058 under reading (a) and 0.570 ± 0.066 under reading (b), both within 0.553 ± 0.068; over five seeds the reading (a) mean ranges from 0.598 to 0.602.",
"claim:table2-ieeg-intra-subjects": "**Result: partially reproduced.** Under reading (b) 8 of 12 subject values are within the table's SD (Spearman rho 0.78 with Table II), under reading (a) 4 of 12 (rho 0.71); the values range from 0.431 to 0.669 (b) and 0.501 to 0.718 (a), against 0.428 to 0.647 in the paper.",
"claim:cross-ieeg-mean": "**Result: reproduced.** The cross-subject mean is 0.351 ± 0.105 with C from all trials and Eq. 3, and 0.339 to 0.350 under the other three readings, all within 0.389 ± 0.064; every electrode got a donor.",
"claim:table2-ieeg-cross-subjects": "**Result: not reproduced.** No subject value is within the table's SD under any reading (0 of 12), and the Spearman rho with Table II is 0.16 to 0.28; sub-12 is 0.647 against 0.340 in the table and sub-05 0.269 against 0.509.",
"claim:cross-below-intra-ieeg": "**Result: reproduced.** The cross-subject average (0.351) is below the intra-subject average (0.602), cross-ieeg-mean is reproduced, and 11 of 12 subjects (12 of 12 under the concatenated readings) have cross below intra.",
},
"masking_coverage.ipynb": {
"claim:fig4a-mask-sweep-ieeg": "**Result: reproduced.** The subject average falls at every step, 0.712, 0.674, 0.650, 0.628 and 0.602 from m = 0 to m = 1.0, and in each of the 12 subjects; with the code's round rule it also falls at every step (0.712, 0.685, 0.660, 0.628, 0.602).",
"claim:fig5a-coverage-ieeg": "**Result: not reproduced.** All (0.712) is highest, but Local alone (0.567) is below Non-local (0.602) on average and in 10 of 12 subjects, so the order All > Local > Non-local does not hold.",
},
"surrogates_lagged.ipynb": {
"claim:surrogate-ieeg": "**Result: reproduced.** The averages are 0.201 (phase), 0.184 (IAAFT) and 0.229 (block), each within its tolerance and below the original 0.602, in every subject.",
"claim:surrogate-order-ieeg": "**Result: not reproduced.** IAAFT (0.184), not phase shuffling (0.201), gives the lowest average, in all 12 subjects; IAAFT is not above phase (reading a) and the order of Table II (reading b) does not hold.",
"claim:full-mask-above-zero-ieeg": "**Result: reproduced (on the criterion's assumed reading b).** With the whole neighbourhood masked the average is 0.602, above zero (reading a) and above the phase-shuffled average 0.201 (reading b), in 12 of 12 subjects.",
"claim:lagged-ieeg-no-gain": "**Result: reproduced.** The lagged average is 0.603 ± 0.060 against 0.602 ± 0.058 for the instantaneous model, within 0.554 ± 0.067 and a difference of +0.3% of the instantaneous average; 7 of 12 subjects gain, Wilcoxon p = 0.42.",
},
}
SUMMARY = {
"reproduce_memar_2026.ipynb": """## Summary

| Claim | Outcome |
|---|---|
| intra-ieeg-mean | reproduced (0.602 ± 0.058, reading a; 0.570 ± 0.066, reading b) |
| table2-ieeg-intra-subjects | partially reproduced (8 of 12 within tolerance, reading b) |
| cross-ieeg-mean | reproduced (0.351 ± 0.105) |
| table2-ieeg-cross-subjects | not reproduced (0 of 12) |
| cross-below-intra-ieeg | reproduced |
| fig4a-mask-sweep-ieeg, fig5a-coverage-ieeg | see `masking_coverage.ipynb` (reproduced; not reproduced) |
| surrogate-ieeg, surrogate-order-ieeg, full-mask-above-zero-ieeg, lagged-ieeg-no-gain | see `surrogates_lagged.ipynb` (reproduced; not reproduced; reproduced; reproduced) |
| the nine EEG claims | blocked: their data are not in DANDI:000055 and were not tested in this run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the trials are 2 s windows around every wrist movement
event in the `reaches` table, all sessions pooled (the paper does not say which events or days);
preprocessing over the whole recording is approximated by filtering each event with 5 s of padding
and taking the |z| and z-score statistics over the session's event windows; the gradient steps use
every 10th sample and training stops at 200 epochs (on sub-07 this changes the mean score by at
most 0.0003, `surrogates_lagged.ipynb`); electrodes without coordinates are left out (8 in sub-12);
events whose padded window holds NaN samples or runs past the recording are left out (7718 of 8088
trials kept).

What was found about the dataset: no electrode has an anatomical label (`location` is "unknown"
everywhere), so the code's atlas neighbourhood cannot be built; sub-12 has 8 electrodes without
coordinates; in four files the `reaches` table and the ReachEvents timestamps disagree by 29240 to
86400 s, and in three of them (the recordings shorter than 24 h) the table puts 22 to 132 events
after the end of the recording; sub-09, sub-06 and sub-12 have 16, 1 and 4 electrodes at x > 0 in
a left-hemisphere implant; sub-02 and sub-09 show no event-locked high-gamma change, so the event
clock is not established for them. No session was deposited twice.
""",
"masking_coverage.ipynb": """## Summary

| Claim | Outcome |
|---|---|
| fig4a-mask-sweep-ieeg | reproduced (0.712 to 0.602, falling at every step in 12 of 12 subjects) |
| fig5a-coverage-ieeg | not reproduced (Local 0.567 below Non-local 0.602) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method. The differences and the dataset findings
are listed in the summary of `reproduce_memar_2026.ipynb`.
""",
"surrogates_lagged.ipynb": """## Summary

| Claim | Outcome |
|---|---|
| surrogate-ieeg | reproduced (0.201, 0.184, 0.229) |
| surrogate-order-ieeg | not reproduced (IAAFT lowest, not phase) |
| full-mask-above-zero-ieeg | reproduced, on the criterion's assumed reading (0.602 against 0.201) |
| lagged-ieeg-no-gain | reproduced (0.603 against 0.602) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method. The speed deviations change the sub-07
score by at most 0.0003. The end-matched reading of the phase surrogate was not run. The other
differences and the dataset findings are listed in the summary of `reproduce_memar_2026.ipynb`.
""",
}
def patch(path, name):
    nb = nbformat.read(path, 4)
    nb.cells = [c for c in nb.cells if not (c.cell_type == "markdown" and (c.source.startswith("**Result:") or c.source.startswith("## Summary")))]
    for tag, text in R[name].items():
        last = max(i for i, c in enumerate(nb.cells) if tag in c.metadata.get("tags", []))
        nb.cells.insert(last + 1, nbformat.v4.new_markdown_cell(text))
    nb.cells.insert(len(nb.cells) - 1, nbformat.v4.new_markdown_cell(SUMMARY[name]))
    nbformat.write(nb, path)
for d in sys.argv[1:]:
    for name in R:
        patch(f"{d}/{name}", name)
PYEOF
source $TMPDIR/wenv/bin/activate; cd  && python $TMPDIR/results.py entries/memar-2026 executed/memar-2026 && python -c "
import nbformat
for n in ['reproduce_memar_2026','masking_coverage','surrogates_lagged']:
    a=nbformat.read(f'entries/memar-2026/{n}.ipynb',4); b=nbformat.read(f'executed/memar-2026/{n}.ipynb',4)
    print(n, len(a.cells), len(b.cells), all(x.source==y.source for x,y in zip(a.cells,b.cells)), sum(len(c.get('outputs',[])) for c in a.cells))
"; date -u
```

```
reproduce_memar_2026 29 29 True 0
masking_coverage 15 15 True 0
surrogates_lagged 23 23 True 0
Sat Nov 21 14:46:46 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -n "^findings" -A14 attempts/fouke-2025-01.yaml | head -30; grep -n "blocked_by" -B3 -A4 attempts/fouke-2025-01.yaml | head -20; grep -n "^verifications\|^questions\|^schema\|^date\|^entry" attempts/fouke-2025-01.yaml; ls schemas 2>/dev/null | head
```

```
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
--
626:findings_review:
627-  date: 2026-11-19
628-  basis: Each finding about the data was rated from its statement alone, against the definitions of docs/protocol.md
629-    (the attempt record), and every critical rating was then read a second time. The attempt did not rate
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(list(s['properties'].keys())); print(s.get('required'))
o=s['properties']['outcomes']['items']; print(o.get('required'), list(o['properties'].keys()))
f=s['properties']['findings']['items']; print(f.get('required'), list(f['properties'].keys()))
print(s['properties']['provenance'])
" 2>&1 | head -40
```

```
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
['kind', 'statement'] ['kind', 'statement', 'found', 'about', 'severity', 'datasets']
{'type': 'object', 'additionalProperties': False, 'required': ['kind', 'accountable'], 'properties': {'kind': {'enum': ['agent', 'person']}, 'accountable': {'description': 'The person or organisation responsible for this attempt.', 'type': 'object', 'additionalProperties': False, 'required': ['name'], 'properties': {'name': {'type': 'string'}, 'orcid': {'type': 'string', 'pattern': '^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$'}, 'ror': {'type': 'string'}}}, 'agent': {'description': 'Required when kind is agent.', 'type': 'object', 'additionalProperties': False, 'required': ['harness', 'model', 'protocol'], 'properties': {'harness': {'type': 'string'}, 'model': {'type': 'string'}, 'protocol': {'description': 'Version of the reproduction protocol the agent followed.', 'type': 'string'}}}, 'runner': {'description': 'Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.', 'type': 'object', 'additionalProperties': False, 'required': ['platform'], 'properties': {'platform': {'description': "The platform that ran it, e.g. GitHub Actions, or local for a person's machine.", 'type': 'string', 'minLength': 1}, 'url': {'description': 'The run that wrote the record, e.g. https://github.com/<owner>/<repo>/actions/runs/<id>.', 'type': 'string', 'pattern': '^https://'}}}, 'author_notes': {'description': "The notes from the paper's authors that this attempt used (papers
[... 1 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/memar-2026-01.yaml",
 "content": "schema_version: 3\nid: memar-2026-01\ndatasets:\n- archive: dandi\n  id: \"000055\"\n  version: 0.220127.0436\n  doi: 10.48324/dandi.000055/0.220127.0436\n  relation: reuses\npaper: doi:10.48550/arxiv.2606.11415\ndate: 2026-11-21\nentry: memar-2026\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/44898633044\ninputs:\n- what: Method details the claims file does not give, read from the paper's code. The filter orders\n    of the preprocessing (4th-order Butterworth, zero phase, notch Q of 30; utils.preprocess_iEEG),\n    PyTorch's default Adam and nn.Linear settings that train.py uses, and the cross-subject\n    evaluation on stored trials that are not z-scored across trials (Test_new_subject_iEEG.py,\n    lines 101 to 161). No data come from the code.\n  source: https://github.com/neurovium/SpatiallyMaskedRegression at commit\n    244dcdbd67f217873c2a52b77485d97c6fa9bf0e\noutcomes:\n- claim: intra-ieeg-mean\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_memar_2026.ipynb\n  output: claim:intra-ieeg-mean\n  measured:\n  - 0.602\n  notes: Mean over the 12 subjects of the per-electrode mean of per-trial test DistCorr at m = 1.0,\n    0.602 ± 0.058 under reading (a) (preprocessing before segmentation, approximated with padded\n    windows) and 0.570 ± 0.066 under reading (b) (preprocessing per epoch); both are within\n    0.553 ± 0.068. Under the claim's seed plus 0, 1000, 2000, 3000 and 4000 (each also setting the\n    split) the reading (a) mean ranges from 0.598 to 0.602, and per subject by at most 0.033.\n    7718 trials over 55 sessions. The atlas neighbourhood variant could not be run, as no\n    electrode has an anatomical label; m = 0 gives 0.712 (masking_coverage.ipynb); the round rule\n    does not change m = 1.0.\n  deviations:\n  - The trials are 2 s windows centred on each start time of the reaches table, every session of a\n    subject pooled (claims file, readings (a) for the events and the days). Reading (b) for the\n    events, movement together with rest trials, was not run; the paper and its code do not define\n    rest trials (the code's unused DANDI path places all of them at 0.5 s).\n  - Preprocessing the whole recording (reading a) would mean reading 845 GB; each event is read with\n    5 s of padding on each side and filtered, and the statistics of the |z| > 5 step and the\n    z-scoring are taken over the session's event windows. An approximation of reading (a).\n  - Filter orders (4th-order Butterworth, filtfilt, notch Q 30) from the code\n    (utils.preprocess_iEEG), which the Methods do not give.\n  - For time, the gradient steps and the validation loss use every 10th sample of each trial, and\n    training stops at 200 epochs (the code allows 10000 with a patience of 200). On sub-07 the mean\n    score is 0.6453 under this setting, 0.6454 with early stopping up to 3000 epochs and 0.6456\n    with every sample for 100 epochs (surrogates_lagged.ipynb). The median epoch of the best\n    validation loss is 72 to 139 per subject.\n  - All electrodes are trained at once as independent rows of one matrix, so the batch order is\n    shared across electrodes; each row has its own loss, Adam state and early-stopping checkpoint.\n  - Electrodes without MNI coordinates (8 in sub-12) are left out, as they have no (x, z)\n    neighbourhood; events whose padded window holds NaN samples (52) or runs past the end of the\n    recording (318) are left out. The paper names no exclusion.\n- claim: table2-ieeg-intra-subjects\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_memar_2026.ipynb\n  output: claim:table2-ieeg-intra-subjects\n  measured: [0.561, 0.669, 0.600, 0.485, 0.559, 0.431, 0.616, 0.493, 0.612, 0.589, 0.593, 0.634]\n  notes: Under reading (b) 8 of 12 subject values are within the table's SD across electrodes\n    (sub-01, 02, 04, 06, 08, 09, 10, 11), Spearman rho 0.78 (p = 0.003), range 0.431 to 0.669\n    against 0.428 to 0.647; these are the values given as measured. Under reading (a) 4 of 12 are\n    within (sub-01, 09, 10, 11), rho 0.71 (p = 0.009), range 0.501 to 0.718. The misses are mostly\n    above the table (sub-03 +0.065, sub-05 +0.035 and sub-07 +0.085 under reading b). The outcome\n    rests on reading (b) of where preprocessing is applied, and on row n of Table II being sub-n.\n  deviations:\n  - As intra-ieeg-mean. The subject order is the claims file's reading; the paper gives no\n    identifiers in Table II.\n- claim: cross-ieeg-mean\n  outcome: reproduced\n  notebook: reproduce_memar_2026.ipynb\n  output: claim:cross-ieeg-mean\n  measured:\n  - 0.351\n  notes: With C from all of the target's trials and Eq. 3 (paired trials), the mean over subjects is\n    0.351 ± 0.105; with the validation trials only 0.339, and with the code's concatenated\n    correlation 0.350 (all) and 0.347 (validation). All four are within 0.389 ± 0.064. Every\n    electrode of every target was matched to a donor electrode in at least one donor. Donor\n    matrices are the reading (a) m = 1.0 weights.\n  deviations:\n  - The target's trials enter as stored after preprocessing, not z-scored across trials, as the\n    paper's evaluation script averages the stored trials (Test_new_subject_iEEG.py, lines 101 to\n    106; the Methods say only that the trial averages are z-scored).\n  - Inherits the trial definition and speed deviations of intra-ieeg-mean through the donor\n    matrices.\n- claim: table2-ieeg-cross-subjects\n  outcome: not_reproduced\n  notebook: reproduce_memar_2026.ipynb\n  output: claim:table2-ieeg-cross-subjects\n  measured: [0.290, 0.386, 0.344, 0.272, 0.269, 0.280, 0.467, 0.279, 0.289, 0.332, 0.354, 0.647]\n  notes: No subject value is within the table's SD under any of the four readings (0 of 12); the\n    tolerances are 0.004 to 0.016. The Spearman rho with Table II is 0.17 (p = 0.60) for the first\n    reading and 0.16 to 0.28 for the others. The largest differences are sub-12 (0.647 against\n    0.340) and sub-05 (0.269 against 0.509). The values given are the first reading's.\n- claim: cross-below-intra-ieeg\n  outcome: reproduced\n  notebook: reproduce_memar_2026.ipynb\n  output: claim:cross-below-intra-ieeg\n  notes: The cross-subject average (0.351) is below the intra-subject average (0.602, reading a),\n    and cross-ieeg-mean is reproduced. 11 of 12 subjects have cross below intra with the paired\n    correlation, 12 of 12 with the concatenated one; sub-12 is the exception (0.647 against\n    0.639).\n- claim: fig4a-mask-sweep-ieeg\n  outcome: reproduced\n  notebook: masking_coverage.ipynb\n  output: claim:fig4a-mask-sweep-ieeg\n  notes: Subject averages 0.712, 0.674, 0.650, 0.628 and 0.602 at m = 0, 0.25, 0.5, 0.75 and 1.0\n    (0, 3, 5, 7 and 9 neighbours masked); the average and each of the 12 subjects fall at every\n    step. With the code's round rule (2 and 4 neighbours at 0.25 and 0.5) the averages are 0.685\n    and 0.660 and still fall at every step in all 12 subjects. The seed sensitivity of the mask\n    draws was not computed (see deviations).\n  deviations:\n  - As intra-ieeg-mean (trials, preprocessing reading a, speed).\n  - For time, the five-seed check of the protocol was run for intra-ieeg-mean only. The steps of\n    the average (0.023 to 0.039) are larger than the spread over seeds seen there (0.004 for the\n    mean).\n- claim: full-mask-above-zero-ieeg\n  outcome: reproduced\n  assumed: true\n  notebook: surrogates_lagged.ipynb\n  output: claim:full-mask-above-zero-ieeg\n  notes: The m = 1.0 average is 0.602, above zero (reading a; smallest electrode value 0.225) and\n    above the phase-shuffled surrogate average 0.201 (reading b, the criterion's assumption), with\n    12 of 12 subjects above their own phase-shuffled value. The m = 1.0 values are recomputed in\n    surrogates_lagged.ipynb with that notebook's generator; they equal the sweep's m = 1.0 values\n    to three decimals in every subject.\n- claim: fig5a-coverage-ieeg\n  outcome: not_reproduced\n  notebook: masking_coverage.ipynb\n  output: claim:fig5a-coverage-ieeg\n  notes: All 0.712, Local 0.567, Non-local 0.602. All is highest in 12 of 12 subjects, but Local\n    is below Non-local on average and in 10 of 12 subjects (Local is above only in sub-09 and\n    sub-10), so the order All > Local > Non-local does not hold under either reading of\n    \"consistently\".\n  deviations:\n  - As intra-ieeg-mean. Local is the 9 nearest electrodes in the (x, z) projection; the atlas\n    neighbourhood of the code could not be built (no anatomical labels), and with it Local could\n    hold a different number of electrodes.\n- claim: surrogate-ieeg\n  outcome: reproduced\n  notebook: surrogates_lagged.ipynb\n  output: claim:surrogate-ieeg\n  measured:\n  - 0.201\n  - 0.184\n  - 0.229\n  notes: Averages 0.201 ± 0.033 (phase), 0.184 ± 0.024 (IAAFT) and 0.229 ± 0.027 (block), within\n    0.181 ± 0.029, 0.232 ± 0.060 and 0.201 ± 0.168, and below the original 0.602 in each of the 12\n    subjects. The paper's subject 3 block value above its original is not seen (sub-03 0.226\n    against 0.627).\n  deviations:\n  - Reading (b), end-matched segments before the phase shuffle, was not run; trimming each trial\n    and channel to its own segment gives series of different lengths, and neither the paper nor\n    the code says how they are recombined. The outcome rests on reading (a), the code's.\n  - The surrogates are drawn with per-row permutations of one generator (rng.permuted), vectorised\n    over channels and trials; the code draws them one series at a time.\n  - Seed sensitivity not computed, for time.\n- claim: surrogate-order-ieeg\n  outcome: not_reproduced\n  notebook: surrogates_lagged.ipynb\n  output: claim:surrogate-order-ieeg\n  notes: IAAFT gives the lowest average (0.184), then phase (0.201) and block (0.229). Phase is not\n    the lowest in any of the 12 subjects, and IAAFT is below phase in all 12, the reverse of\n    \"IAAFT surrogates retain somewhat more\". The differences between surrogates (0.017 between\n    IAAFT and phase) are smaller than between any surrogate and the original.\n  deviations:\n  - As surrogate-ieeg.\n- claim: lagged-ieeg-no-gain\n  outcome: reproduced\n  notebook: surrogates_lagged.ipynb\n  output: claim:lagged-ieeg-no-gain\n  measured:\n  - 0.603\n  notes: Lagged 0.603 ± 0.060 against instantaneous 0.602 ± 0.058 (lags of 0, 10, 15, 25 and 30\n    samples); the difference is +0.0018, 0.3% of the instantaneous average, under the 10% bound\n    the criterion assumes. Per subject differences range from -0.0097 to +0.0145; 7 of 12 gain;\n    Wilcoxon signed-rank p = 0.42 (context only).\n  deviations:\n  - One bias in place of the code's one per lag.\n  - As intra-ieeg-mean (trials, preprocessing reading a, speed); seed sensitivity not computed.\n- claim: intra-eeg-mean\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: The EEG data (BNCI Horizon 2020, Upper Limb Movements, Ofner et al. 2017) are not in\n    DANDI:000055, and the paper gives no accession or version. The iEEG analyses filled the run's\n    five hours (the three notebooks took 46, 42 and 42 minutes), and the EEG data were not\n    fetched or tested.\n- claim: intra-eeg-above-ieeg\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Depends on intra-eeg-mean, not tested in this run. The iEEG average is 0.602.\n- claim: cross-eeg-mean\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: EEG data not tested in this run (see intra-eeg-mean).\n- claim: transfer-penalty-larger-ieeg\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: Depends on the EEG claims, not tested in this run. On iEEG the cross over intra ratio is\n    0.58 (0.351 / 0.602) and the difference 0.251.\n- claim: lagged-eeg-no-gain\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: EEG data not tested in this run (see intra-eeg-mean).\n- claim: fig4b-mask-sweep-eeg\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: EEG data not tested in this run (see intra-eeg-mean).\n- claim: fig5b-coverage-eeg\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: EEG data not tested in this run (see intra-eeg-mean).\n- claim: surrogate-eeg\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: EEG data not tested in this run (see intra-eeg-mean).\n- claim: surrogate-order-eeg\n  outcome: blocked\n  blocked_by: not_runnable\n  notes: EEG data not tested in this run (see intra-eeg-mean).\nfindings:\n- kind: metadata_error\n  about: data\n  severity: major\n  statement: In four files the reaches table and the ReachEvents timestamps disagree, by 30682 s\n    (sub-01 ses-7), 30048 s (sub-04 ses-3), 29240 s (sub-06 ses-3) and 86400 s (sub-08 ses-4);\n    elsewhere they agree within 1 ms. In the first three, the files whose recordings are shorter\n    than 24 h, the reaches table puts 132, 22 and 83 events after the end of the recording, and\n    sub-08 ses-4 has 1. One of the two tables is not on the recording's clock in these files; this\n    attempt did not establish which. It used the reaches table and dropped the events past the end,\n    so the remaining trials of those sessions may not be centred on movements.\n- kind: metadata_insufficient\n  about: data\n  severity: minor\n  statement: The location column of every electrode table holds \"unknown\"; the dataset has no\n    anatomical (AAL) labels, which the paper's Figure 6 shows and its code's default atlas\n    neighbourhood needs.\n- kind: metadata_insufficient\n  about: data\n  severity: minor\n  statement: Eight electrodes of sub-12 have no MNI coordinates (NaN x, y and z) in every session;\n    they cannot be placed in a coordinate neighbourhood.\n- kind: other\n  about: data\n  severity: minor\n  statement: The paper says each subject's electrodes are in one hemisphere; in the electrode\n    tables sub-09 has 16 of 126 electrodes at x > 0 with the rest at x < 0, and sub-06 and sub-12\n    have 1 and 4 at x > 0. They may be midline or contralateral contacts; the files do not say.\n- kind: other\n  about: data\n  severity: minor\n  statement: High-gamma power after the movement events against before them shows an event-locked\n    change in 10 of 12 subjects (largest |t| 5.2 to 30.2 against a null 95th percentile near 3.4),\n    but not in sub-02 (2.65) and sub-09 (3.09), so the alignment of events and signal is not\n    established for those two. 52 events fall in stretches with NaN samples. No session is\n    deposited twice (no two sessions share event times or a channel correlation matrix).\n- kind: methods_unavailable\n  about: paper\n  statement: Questions for the paper's authors. (1) Which movement events and recording days form\n    the iEEG trials, whether rest trials were included, and how rest trials were chosen. (2)\n    Whether the preprocessing was applied to the continuous recordings or to each 2 s epoch; the\n    per-subject values in Table II match better under per-epoch preprocessing (8 of 12) than under\n    continuous (4 of 12). (3) How Table II's rows map to AJILE12 participants. (4) Which mask\n    intensity the Intra-Subject, Lagged and surrogate columns use (m = 1.0 is assumed here, as the\n    code's notebook says).\n"
}
```

```
File created successfully at: attempts/memar-2026-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  source $TMPDIR/wenv/bin/activate; python $TMPDIR/show.py executed/memar-2026/reproduce_memar_2026.ipynb 100000 | grep "dropped without coord" | python -c "
import sys,re
e=n=ne=0
for l in sys.stdin:
    m=re.search(r'file edges (\d+) dropped for NaN in the padded window (\d+) of which NaN in the 2 s epoch (\d+)',l); e+=int(m[1]); n+=int(m[2]); ne+=int(m[3])
print(e,n,ne)"; date -u
```

```
238 132 75
Sat Nov 21 14:47:54 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
p="attempts/memar-2026-01.yaml"; s=open(p).read()
s=s.replace("events whose padded window holds NaN samples (52) or runs past the end of the\n    recording (318) are left out.","events whose padded window holds NaN samples (132) or runs past the start or end of\n    the recording (238) are left out.")
s=s.replace("52 events fall in stretches with NaN samples.","132 events have NaN samples within 5 s of the 2 s window, 75 of them inside it.")
open(p,"w").write(s)
EOF
grep -n "(132)\|132 events" attempts/memar-2026-01.yaml; cat > entries/memar-2026/README.md <<'EOF'
# Ostadsharif Memar & Dehghani (2026) on AJILE12, dandiset 000055

Tests the iEEG findings of [Ostadsharif Memar & Dehghani (2026)](https://doi.org/10.48550/arxiv.2606.11415),
"Spatially Masked Regression Reveals Local and Distributed Predictability in Electrophysiological
Recordings", on [DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which
holds the intracranial recordings and wrist movement events of the paper's 12 subjects. The paper's
scalp EEG dataset is not in the dandiset.

| Claim | Outcome |
|---|---|
| Intra-subject iEEG DistCorr 0.553 ± 0.068 | Reproduced |
| Intra-subject values per subject (Table II) | Partially reproduced |
| Cross-subject iEEG DistCorr 0.389 ± 0.064 | Reproduced |
| Cross-subject values per subject (Table II) | Not reproduced |
| Cross-subject below intra-subject | Reproduced |
| DistCorr falls as more of the neighbourhood is masked | Reproduced |
| Reconstruction stays above zero with the neighbourhood masked | Reproduced (on an assumed reading) |
| All > Local > Non-local electrodes as predictors | Not reproduced |
| Surrogates reduce DistCorr to 0.181, 0.232 and 0.201 | Reproduced |
| Phase shuffling degrades most, IAAFT retains more | Not reproduced |
| Lagged predictors barely change DistCorr | Reproduced |
| Nine EEG claims | Blocked: not runnable in this run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Three notebooks, each loading the data again: `reproduce_memar_2026.ipynb` (data check,
intra-subject and cross-subject), `masking_coverage.ipynb` and `surrogates_lagged.ipynb`. The
helper `smr.py` holds the loading, preprocessing, model and measures, with the source of every
parameter. The attempt record is [`attempts/memar-2026-01.yaml`](../../attempts/memar-2026-01.yaml).
EOF
python tools/entry.py check entries/memar-2026 2>&1 | tail -8; date -u
```

```
65:    neighbourhood; events whose padded window holds NaN samples (132) or runs past the start or end of
268:    established for those two. 132 events have NaN samples within 5 s of the 2 s window, 75 of them inside it. No session is
error: attempts/memar-2026-01.yaml: outcomes/6: 'deviations' is a required property
1 error(s)
Sat Nov 21 14:48:10 UTC 2026
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/memar-2026-01.yaml",
 "old_string": "    to three decimals in every subject.\n- claim: fig5a-coverage-ieeg",
 "new_string": "    to three decimals in every subject.\n  deviations:\n  - Judged by reading (b) of the criterion, the m = 1.0 average against the phase-shuffled\n    surrogate average, an assumption the claims file names because the paper compares with zero\n    only and the sample DistCorr cannot fall below zero.\n  - As intra-ieeg-mean (trials, preprocessing reading a, speed).\n- claim: fig5a-coverage-ieeg"
}
```

```
The file attempts/memar-2026-01.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/memar-2026 2>&1 | tail -5; python tools/entry.py handover entries/memar-2026 2>&1 | tail -2; ls executed/memar-2026/handover; git status --short; date -u
```

```
0 error(s)
wrote executed/memar-2026/handover
masking_coverage.ipynb
memar-2026.yaml
reproduce_memar_2026.ipynb
smr.py
surrogates_lagged.ipynb
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
?? attempts/memar-2026-01.yaml
?? entries/memar-2026/
?? scripts
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la entries/memar-2026; git check-ignore -v entries/memar-2026/__pycache__ 2>&1 | head -2
```

```
total 200
drwxr-xr-x   4 runner runner  4096 Nov 21 14:48 .
drwxr-xr-x 337 runner runner 12288 Nov 21 11:31 ..
drwxr-xr-x   3 runner runner  4096 Nov 21 11:33 .claude
-rw-r--r--   1 runner runner  1880 Nov 21 14:48 README.md
drwxr-xr-x   2 runner runner  4096 Nov 21 12:22 __pycache__
-rw-r--r--   1 runner runner  1198 Nov 21 12:21 entry.yaml
-rw-r--r--   1 runner runner  9726 Nov 21 14:46 masking_coverage.ipynb
-rw-r--r--   1 runner runner 24379 Nov 21 14:46 reproduce_memar_2026.ipynb
-rw-r--r--   1 runner runner    76 Nov 21 12:21 requirements.in
-rw-r--r--   1 runner runner 83236 Nov 21 12:21 requirements.lock.txt
-rw-r--r--   1 runner runner 27137 Nov 21 11:57 smr.py
-rw-r--r--   1 runner runner 14642 Nov 21 14:46 surrogates_lagged.ipynb
.gitignore:1:__pycache__/	entries/memar-2026/__pycache__
```

**Agent calls Bash**

```bash
cd  find entries/memar-2026/.claude -type f | head; git check-ignore -v entries/memar-2026/.claude 2>&1 | head -1
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  find entries/memar-2026/.claude; rmdir -p entries/memar-2026/.claude/* 2>/dev/null; find entries/memar-2026/.claude -depth -type d -empty -delete; ls -a entries/memar-2026; date -u
```

```
entries/memar-2026/.claude
entries/memar-2026/.claude/.cc-writes
.
..
README.md
__pycache__
entry.yaml
masking_coverage.ipynb
reproduce_memar_2026.ipynb
requirements.in
requirements.lock.txt
smr.py
surrogates_lagged.ipynb
Sat Nov 21 14:48:43 UTC 2026
```

**Agent**

The iEEG part of the attempt is done: 11 claims tested, 7 reproduced, 1 partially reproduced and 3 not reproduced. The 9 EEG claims are blocked. The record is `attempts/memar-2026-01.yaml`, the handover is built, and `entry.py check` reports 0 errors. The entry was not run end to end by `entry.py all`: the tool cut that run at 60 minutes, and I ran the last two notebooks myself (point 1 below).

**1. Outcomes**

| Claim | Outcome | Measured |
|---|---|---|
| intra-ieeg-mean | reproduced (assumed) | 0.602 ± 0.058 for preprocessing before cutting trials, 0.570 for preprocessing each trial; 0.598 to 0.602 over five seeds |
| table2-ieeg-intra-subjects | partially reproduced (assumed) | 8 of 12 subjects within tolerance with per-trial preprocessing, 4 of 12 with preprocessing first |
| cross-ieeg-mean | reproduced | 0.351 (0.339 to 0.351 across the four readings) |
| table2-ieeg-cross-subjects | not reproduced | 0 of 12 within tolerance; rank correlation with the table 0.16 to 0.28 |
| cross-below-intra-ieeg | reproduced | 0.351 against 0.602; 11 or 12 of 12 subjects |
| fig4a-mask-sweep-ieeg | reproduced | 0.712 → 0.674 → 0.650 → 0.628 → 0.602, falling in all 12 subjects |
| full-mask-above-zero-ieeg | reproduced (assumed) | 0.602 against 0.201 for the phase-shuffled surrogate |
| fig5a-coverage-ieeg | not reproduced | All 0.712, Local 0.567, Non-local 0.602 (Local is lower) |
| surrogate-ieeg | reproduced | 0.201 phase, 0.184 IAAFT, 0.229 block |
| surrogate-order-ieeg | not reproduced | IAAFT is lowest in all 12 subjects, not phase |
| lagged-ieeg-no-gain | reproduced | 0.603 against 0.602 |
| 9 EEG claims | blocked (`not_runnable`) | the EEG data are not in DANDI:000055; the iEEG work used the whole run |

**2. The dataset, assumptions and questions**
- **Version:** I pinned 0.220127.0436, the only published version. The paper cites no version.
- **Event times (major):** in four files the `reaches` table and the ReachEvents timestamps disagree by 29,240 to 86,400 s. In three of them, the recordings shorter than 24 h, the table puts 22 to 132 events after the end of the recording. I did not establish which table is right.
- **Electrode metadata:** no electrode has an anatomical label (every `location` is "unknown"), so the code's atlas neighbourhood could not be built. Eight sub-12 electrodes have no coordinates. sub-09 has 16 electrodes on the other hemisphere's side, although the paper says one hemisphere per subject.
- **Event alignment:** sub-02 and sub-09 show no high-gamma change locked to the movement events, so alignment is not established for them. No session was deposited twice.
- **Data dropped:** 7,718 of 8,088 events were kept. 238 were past the recording's edges and 132 had missing samples nearby.
- **Assumptions:**
  - Trials are the `reaches` events with all sessions pooled.
  - Whole-recording preprocessing is approximated by filtering each event with 5 s of padding. The real version would mean reading 845 GB.
  - The mask covers the whole neighbourhood (m = 1.0).
  - Row n of Table II is sub-n.
- **Questions for the paper's authors:** recorded as a `methods_unavailable` finding. They ask which events and days form the trials, where preprocessing is applied, how the table rows map to subjects, and which mask intensity the tables use.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or did not fit**
1. The protocol asks for one `entry.py all` run, but my tool stops a command at 60 minutes by default. The first `all` was cut after notebook 1 finished, so there is no run stamp. I ran notebooks 2 and 3 in the entry's locked environment with the same nbconvert command. There was no time left for a full re-run.
2. The protocol does not say how to write the conclusion cells when the notebooks take most of the run to execute. I added the conclusion and summary markdown after execution, identically to the notebooks and the executed copies, leaving code and outputs untouched. A fresh `run` will re-execute everything.
3. The five-seed rule could not fit the time on this many model fits. I ran it for intra-ieeg-mean only and said so in the other claims' deviations.
4. Speed deviations: training used every 10th sample and stopped at 200 epochs. On sub-07 this changes the score by at most 0.0003.
5. For `data: elsewhere` claims stopped by the time limit, the protocol names no block reason. I used `not_runnable`.
6. The surrogate claim's end-matched reading is not well defined, because trimming gives series of different lengths. I recorded it as not run.
7. The criterion's second event reading, movement plus rest trials, has no definition of rest trials in the paper or its code. It was not run.

**4. Runtime and failures**
- The notebooks took 45.7, 41.8 and 41.7 minutes, with peak memory up to 8.6 GB. Most of each is loading about 7,700 events over the network, about 14 to 22 minutes per notebook.
- The first `all` run was lost to the 60-minute tool limit.
- Untracked dotfiles and folders I did not create (`.bashrc`, `.idea`, `scripts` and others) appeared at the repository root. I left them alone; they should not be committed.

## End of run

85 turns, 203 minutes, $10.19 at API prices, result: success.
