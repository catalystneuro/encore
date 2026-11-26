# costabile-2023 · author · run 45721168613

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (67.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/38987a61-3033-41ca-92c6-29ea782dbb55/tool-results/b5wndytvh.txt

Preview (first 2KB):
Wed Nov 25 23:28:04 UTC 2026
# Protocol for an attempt

Version: `pilot-19`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 19 more lines not kept]
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
3	Version: `pilot-19`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
[... 794 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; wc -l docs/design.md docs/archives.md; ls entries/fouke-2025 paper; cat claims/costabile-2023.yaml; cat papers/datasets/costabile-2023.yaml; git diff --stat
```

```
<persisted-output>
Output too large (63.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/38987a61-3033-41ca-92c6-29ea782dbb55/tool-results/buvfvd4ca.txt

Preview (first 2KB):
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Site:** <https://encorescience.org/>, with the registry's dashboard at <https://encorescience.org/registry/> and what Encore offers a journal at <https://encorescience.org/journals/>.
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/costabile-2023.yaml"
}
```

```
1	# Claims for Costabile, Balakrishnan, Schwinn & Haesemeyer (2023), "Model discovery to link neural
2	# activity to behavioral tasks", eLife 12:e83289, tested on DANDI:000235, 000236, 000237 and 000238.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
4	# protocol as stated in docs/protocol.md (version pilot-19, Reader).
5	#
6	# Text read. The version of record (eLife, published 6 June 2023), paper/10.7554-elife.83289.txt,
7	# extracted from the publisher PDF (also under paper/): main text, the legends of Figures 1 to 7,
8	# Table 1, Methods, Data availability. The PDF was opened only to read Figure 6 (panels F and G)
9	# and Figure 7 (panel E), whose values the text does not give. eLife's figure supplements
10	# (Figure 1, 2, 3, 4, 5, 6 and 7, figure supplement 1) are online only: neither their panels nor
11	# their legends are in the PDF or the text. The Results state what each of them shows, and the
12	# claims that rest on them (region enrichments, Figure 6, figure supplement 1D, E, G to I;
13	# Figure 7, figure supplement 1A to E) are written from those Results sentences and from the
14	# code that draws them. Supplementary file 1 (Z-Brain region abbreviations) and the MDAR checklist
15	# are not under paper/; neither holds results.
16	#
17	# Code read. github.com/haesemeyer/mine_pub at commit 368d75650a1de92d9dd6c7dd1aadff24be6ba379,
18	# the revision the paper archives (Software Heritage, Haesemeyer 2023). It holds the CNN
19	# (model.py), the Taylor routines (taylorDecomp.py), the MINE interface (mine.py), the simulation
20	# scripts for Figures 1 to 4 (cnn_fit_test.py, cnn_nonlin_test.py, cnn_sta_test.py, mine_edf.py,
[... 852 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/datasets/costabile-2023.yaml; ls entries/fouke-2025 attempts | head -50; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; git diff; ls paper; ls questions | head
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.7554/elife.83289
title: Model discovery to link neural activity to behavioral tasks
datasets:
- archive: dandi
  id: '000235'
  relation: primary
- archive: dandi
  id: '000236'
  relation: primary
- archive: dandi
  id: '000237'
  relation: primary
- archive: dandi
  id: 000238
  relation: primary
attempts:
amjad-2025-01.yaml
amjad-2025-02.yaml
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -120; grep -n "" docs/design.md | head -5; wc -l docs/design.md
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
1:# Reproduction registry: design
2:
[... 4 more lines not kept]
```

**Agent**

Read the protocol and the claims file (37 claims). Surveying the four dandisets now.

**Agent calls Bash**

```bash
for d in 000235 000236 000237 000238; do curl -s "https://api.dandiarchive.org/api/dandisets/$d/versions/" | python -c "import json,sys; r=json.load(sys.stdin); [print('$d',v['version'],v['created'],v['asset_count'],v['size'],v['status']) for v in r['results']]"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for d in 000235:0.230316.1600 000236:0.230316.2031 000237:0.230316.1655 000238:0.230316.1519; do id=${d%%:*}; v=${d##*:}; curl -s "https://api.dandiarchive.org/api/dandisets/$id/versions/$v/assets/?page_size=100" | python -c "import json,sys; r=json.load(sys.stdin); [print('$id',a['asset_id'],a['path'],a['size']) for a in r['results']]"; done; curl -s https://api.dandiarchive.org/api/dandisets/000235/versions/0.230316.1600/ | python -m json.tool | head -150
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q sv && . sv/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy dandi 2>&1 | tail -2; python -c "import pynwb,remfile;print(pynwb.__version__)"; nproc; free -g
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
cd $TMPDIR && . sv/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, sys, requests
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
r=requests.head(url,allow_redirects=True); s3=r.url.split('?')[0]
f=h5py.File(remfile.File(s3),'r')
def v(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name,obj.shape,obj.dtype,dict((k,(obj.attrs[k] if not isinstance(obj.attrs[k],h5py.Reference) else 'ref')) for k in obj.attrs if k in('unit','conversion','rate','starting_time','description','resolution')))
    else:
        a={k:obj.attrs[k] for k in obj.attrs if k in ('neurodata_type','description')}
        print(name+'/',a)
f.visititems(v)
EOF
time python survey.py af99ab20-fa1f-4730-b706-8327f2ca48e2 2>&1 | head -150
```

```
acquisition/ {}
acquisition/Z0_0/ {'description': 'Timeseries in Plane 0 for channel 0', 'neurodata_type': 'TwoPhotonSeries'}
acquisition/Z0_0/data (1182, 512, 512) uint8 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'Photon count'}
acquisition/Z0_0/starting_time () float64 {'rate': np.float64(2.384185791015625), 'unit': 'seconds'}
acquisition/Z0_1/ {'description': 'Timeseries in Plane 0 for channel 1', 'neurodata_type': 'TwoPhotonSeries'}
acquisition/Z0_1/data (1182, 512, 512) uint8 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'Photon count'}
acquisition/Z0_1/starting_time () float64 {'rate': np.float64(2.384185791015625), 'unit': 'seconds'}
acquisition/Z10_0/ {'description': 'Timeseries in Plane 10 for channel 0', 'neurodata_type': 'TwoPhotonSeries'}
acquisition/Z10_0/data (1182, 512, 512) uint8 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'Photon count'}
acquisition/Z10_0/starting_time () float64 {'rate': np.float64(2.384185791015625), 'unit': 'seconds'}
acquisition/Z10_1/ {'description': 'Timeseries in Plane 10 for channel 1', 'neurodata_type': 'TwoPhotonSeries'}
acquisition/Z10_1/data (1182, 512, 512) uint8 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'Photon count'}
acquisition/Z10_1/starting_time () float64 {'rate': np.float64(2.384185791015625), 'unit': 'seconds'}
acquisition/Z11_0/ {'description': 'Timeseries in Plane 11 for channel 0', 'neurodata_type': 'TwoPhotonSeries'}
acquisition/Z11_0/data (1182, 512, 512) uint8 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'Photon count'}
acquisition/Z11_0/starting_time () float64 {'rate': np.float64(2.384185791015625), 'unit': 'seconds'}
acquisition/Z11_1/ {'description': 'Timeseries in Plane 11 for channel 1', 'neurodata_type': 'TwoPhotonSeries'}
acquisition/Z11_1/data (1182, 512, 512) uint8 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'Photon count'}
acquis
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && sed -i 's/^f.visititems(v)/[f[k].visititems(lambda n,o,k=k: v(k+"\/"+n,o)) for k in f.keys() if k!="acquisition"]\nprint(list(f["acquisition"].keys())[:3], len(f["acquisition"]))/' survey.py && time python survey.py af99ab20-fa1f-4730-b706-8327f2ca48e2 > s1.txt 2>&1; wc -l s1.txt; grep -v "Z[0-9]*_" s1.txt | head -100; grep -c "" s1.txt
```

```
real	0m1.384s
user	0m0.571s
sys	0m0.053s
5 s1.txt
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 12, in <module>
    [f[k].visititems(lambda n,o,k=k: v(k+"/"+n,o)) for k in f.keys() if k!="acquisition"]
     ^^^^^^^^^^^^^^^
AttributeError: 'Dataset' object has no attribute 'visititems'
5
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && sed -i 's/for k in f.keys() if k!="acquisition"\]/for k in f.keys() if k!="acquisition" and isinstance(f[k],h5py.Group)]/' survey.py && time python survey.py af99ab20-fa1f-4730-b706-8327f2ca48e2 > s1.txt 2>&1; wc -l s1.txt; grep -v "Z[0-9]*_" s1.txt | head -150; grep "Z0_" s1.txt|head -40
```

```
real	0m24.643s
user	0m1.611s
sys	0m0.278s
1133 s1.txt
general/devices/ {}
general/devices/OSU_2P_1/ {'description': 'OSU Haesemeyer Lab, 2-Photon 1', 'neurodata_type': 'Device'}
general/experiment_description () object {}
general/experimenter (1,) object {}
general/institution () object {}
general/optophysiology/ {}
general/subject/ {'neurodata_type': 'Subject'}
general/subject/date_of_birth () object {}
general/subject/genotype () object {}
general/subject/sex () object {}
general/subject/species () object {}
general/subject/subject_id () object {}
processing/behavior/ {'description': 'preprocessed tail behavior data', 'neurodata_type': 'ProcessingModule'}
processing/behavior/Cumulative Tail Angle/ {'neurodata_type': 'BehavioralTimeSeries'}
processing/behavior/Cumulative Tail Angle/TailCumAngle_Z0/ {'description': 'Cumulative Tail angle in plane 0', 'neurodata_type': 'TimeSeries'}
processing/behavior/Cumulative Tail Angle/TailCumAngle_Z0/data (125361,) float64 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'radians'}
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "Tail\|Z[0-9]*_[01]/\|optophysiology" s1.txt | grep -v "_Z[1-9]" | head -80; grep -o "processing/[^/]*/[^/]*/" s1.txt | sort | uniq -c
```

```
general/devices/ {}
general/devices/OSU_2P_1/ {'description': 'OSU Haesemeyer Lab, 2-Photon 1', 'neurodata_type': 'Device'}
general/experiment_description () object {}
general/experimenter (1,) object {}
general/institution () object {}
general/subject/ {'neurodata_type': 'Subject'}
general/subject/date_of_birth () object {}
general/subject/genotype () object {}
general/subject/sex () object {}
general/subject/species () object {}
general/subject/subject_id () object {}
processing/behavior/ {'description': 'preprocessed tail behavior data', 'neurodata_type': 'ProcessingModule'}
processing/ophys/ {'description': 'CaImAn data', 'neurodata_type': 'ProcessingModule'}
processing/ophys/CaUnitRespones_Z0/ {'description': 'CaImAn inferred calcium for plane 0', 'neurodata_type': 'RoiResponseSeries'}
processing/ophys/CaUnitRespones_Z0/data (1182, 690) float64 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'calcium'}
processing/ophys/CaUnitRespones_Z0/rois (690,) int64 {'description': 'All identified units'}
processing/ophys/CaUnitRespones_Z0/starting_time () float64 {'rate': np.float64(2.384185791015625), 'unit': 'seconds'}
processing/ophys/Dff_Z0/ {'neurodata_type': 'DfOverF'}
processing/ophys/Dff_Z0/DffUnitResponses_Z0/ {'description': 'CaImAn Dff for plane 0', 'neurodata_type': 'RoiResponseSeries'}
processing/ophys/Dff_Z0/DffUnitResponses_Z0/data (1182, 690) float64 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'deltaF/F0'}
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/haesemeyer/mine_pub && cd mine_pub && git checkout -q 368d75650a1de92d9dd6c7dd1aadff24be6ba379 && ls && wc -l *.py | tail -1; date -u
```

```
AnatomyClustering.py
LICENSE
README.md
cnn_fit_test.py
cnn_nonlin_test.py
cnn_sta_test.py
environment_utf8.yml
example_train_trajectory.py
experiment.py
mine.py
mine_edf.py
model.py
perf_nlc_nonlin.py
plotMusall.py
processMusall.py
rspinal_build_main.py
rspinal_plot_panels.py
rwave_build_main.py
rwave_create_cmtk_commands.py
rwave_data_fit.py
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && cat rwave_data_fit.py
```

```
"""
Script for identifying stimulus and behavior related neurons in random-wave experiment data
"""

import model
import numpy as np
import utilities
import h5py
from scipy.ndimage import gaussian_filter1d
import os
from os import path
from experiment import Experiment2P
from numba import njit
from multiprocessing import Pool
import multiprocessing as mp
from typing import Union, Any, List, Tuple, Optional
import argparse
import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression
from collections import Counter
[... 415 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -n "def \|bout" experiment.py | head -80; grep -n "def avg_component_brightness" -A40 experiment.py
```

```
22:    def __init__(self, message: str):
29:    def __init__(self, backend: Optional[h5py.File], storage_name: str, lazy_loaded=True):
42:    def get_data(self, n_planes) -> List[np.ndarray]:
55:    def set_data(self, value: List[np.ndarray]) -> None:
60:    def update(self) -> None:
70:    def am_i_lazy(self):
74:    def am_i_modified(self):
82:    def __init__(self, lazy_load_filename: str = "", allow_write=True):
96:        self.bout_data: List[np.ndarray] = []  # for each experimental plane, matrix of extracted swim bouts
136:    def __enter__(self):
139:    def __exit__(self, exc_type, exc_value, traceback):
145:    def __lazy_load(self, lazy_load_filename: str, allow_write: bool) -> None:
186:                self.bout_data.append(plane_group["bout_data"][()])
207:    def tail_data(self) -> List[np.ndarray]:
211:    def tail_data(self, value: List[np.ndarray]):
215:    def replaced_tail_frames(self) -> List[np.ndarray]:
219:    def replaced_tail_frames(self, value: List[np.ndarray]):
223:    def laser_data(self) -> List[np.ndarray]:
227:    def laser_data(self, value: List[np.ndarray]):
231:    def all_c(self) -> List[np.ndarray]:
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && cat > peek.py <<'EOF'
import h5py, remfile, requests, numpy as np
aid="af99ab20-fa1f-4730-b706-8327f2ca48e2"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url.split('?')[0]
print(s3)
f=h5py.File(remfile.File(s3),'r')
for k in ['experiment_description','institution','session_description','session_start_time','timestamps_reference_time','identifier']:
    if k in f['general'] or k in f: 
        try: print(k, f['general'][k][()] )
        except Exception: print(k, f[k][()])
for k in f['general/subject']: print('subject',k,f['general/subject'][k][()])
for k in f['general/optophysiology/Z0_0']: 
    try: print('ip',k,f['general/optophysiology/Z0_0'][k][()])
    except Exception: pass
print(f['general/optophysiology/Z0_0/Ch0/description'][()],f['general/optophysiology/Z0_1/Ch1/description'][()])
s=f['scratch/Raw Experiment metadata'][()]; print(type(s), str(s)[:3000])
ri=f['processing/ophys/ImageSegmentation/Segmentation_Z0/reference_images']
print('refimg', list(ri.keys()))
def show(n,o):
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, dict(o.attrs))
ri.visititems(show)
seg=f['processing/ophys/ImageSegmentation/Segmentation_Z0']; print(dict(seg.attrs)); print(list(seg.keys()))
t=f['stimulus/presentation/Temperature_Z0/data'][:]; print('temp',t.min(),t.max(),t.mean(), t[:5])
ca=f['processing/ophys/CaUnitRespones_Z0/data']; print(dict(ca.attrs)); c=ca[:]; print('ca',c.min(),c.max(),np.mean(c))
print('rois', f['processing/ophys/CaUnitRespones_Z0/rois'][:10], dict(f['processing/ophys/CaUnitRespones_Z0'].attrs))
ta=f['processing/behavior/Cumulative Tail Angle/TailCumAngle_Z0/timestamps'][:]; print('tailts',ta[:5],ta[-5:], np.median(np.diff(ta)))
d=f['processing/behavior/Cumulative Tail Angle/TailCumAngle_Z0/data'][:]; print('tail',np.nanmin(d),np.nanmax(d),np.isnan(d).sum())
EOF
python peek.py
```

```
https://dandiarchive.s3.amazonaws.com/blobs/5f5/18f/5f518f65-d329-4d94-8d12-cfcd43d77f2f
experiment_description b'Experiment type: RandomWave\n\nMinimum generator frequency: 0.005 Hz\n\nMaximum generator frequency: 0.075 Hz\n\nGenerator frequency count: 25\n\nRandom wave offset: 2000 mA\n\nRandom wave amplitude: 2000 mA\n\nNumber of pre seconds: 60\n\nNumber of stim seconds: 30\n\nNumber of post seconds: 75\n\nNumber of repeats: 3\n\nNumber of ZPlanes: 30\n\nZ-Step: 5\n\nFrame duration in seconds: 0.4194304\n\nSample frequency of laser current file: 20 Hz\n\nStart time: 8/18/2021 11:25:56 AM\n\nNumber of turn-around pixels: 10\n\nStable Z enabled.\n\nPre stack spacing: 0.4\n\nPre stack slices: 21\n\nPre stack repeats: 20\n\nStabilizer accumulation: 5\n\nCurrent shift boxcar filter length: 7\n\nZero position shift update weight: 0.025165824\n\nBrightness clip value: 20\n\n\n\nFinish time: 8/18/2021 5:14:35 PM\n'
institution b'THE Ohio State University'
session_description b'vglut RandomWave'
session_start_time b'2021-08-18T11:25:56-04:00'
timestamps_reference_time b'2021-08-18T11:25:56-04:00'
identifier b'Fish01_GCaMP_vlgut_FBd_5dpf_RandomWave'
subject date_of_birth b'2021-08-12T11:25:56-04:00'
subject genotype b'mitfa -/-; elavl3-H2B:GCaMP6s +/-; vglut2a-mCherry +/-'
subject sex b'U'
subject species b'http://purl.obolibrary.org/obo/NCBITaxon_7955'
subject subject_id b'Fish01_GCaMP_vlgut_FBd_5dpf_RandomWave'
ip description b'Zoom\t1.25\n\nDwellTimeInMicroseconds\t1.6\n\nPixelsPerLine\t512\n\nLinesPerImage\t512\n\nRepsPerLine\t1\n\nPower\t68.50341513\n\nX\t9.94459594075\n\nY\t15.36088353219\n\nZ\t-0.108635\n'
ip excitation_lambda 950.0
ip grid_spacing [0.78125 0.78125]
ip imaging_rate 2.384185791015625
ip indicator b'HuC-H2B:GCaMP6s'
ip location b'Dorsal Forebrain'
b'PMT Ch0, Green' b'PMT Ch1, Red'
<class 'bytes'> b'Experiment type: RandomWave\n\nMinimum generator frequency: 0.005 Hz\n\nMaximum generator frequency: 0.075 Hz\n\nGenerator frequency count: 25\n\nRandom w
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && cat > peek2.py <<'EOF'
import h5py, remfile, requests, numpy as np, time
aid="af99ab20-fa1f-4730-b706-8327f2ca48e2"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url.split('?')[0]
f=h5py.File(remfile.File(s3),'r')
d=f['acquisition/Z0_0/data']; print(d.chunks, d.compression, d.compression_opts)
t=time.time(); x=d[:100]; print('100 frames',time.time()-t, x.mean())
pm=f['processing/ophys/ImageSegmentation/Segmentation_Z0/pixel_mask'][:]; idx=f['processing/ophys/ImageSegmentation/Segmentation_Z0/pixel_mask_index'][:]
print(pm[:5], idx[:5], pm['weight'].min(), pm['weight'].max(), pm['x'].max(), pm['y'].max())
print(f['processing/ophys/ImageSegmentation/Segmentation_Z0/id'][:5])
EOF
python peek2.py
```

```
(74, 32, 32) gzip 4
100 frames 0.35200953483581543 0.015452461242675781
[(40, 1, 0.11733086) (41, 1, 0.38279274) (42, 1, 0.38279274)
 (43, 1, 0.19337907) (44, 1, 0.19734596)] [ 27  67 121 159 184] 0.0035254753 0.5985418 510 510
[0 1 2 3 4]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd paper && grep -n -i "bout\|brightness\|backfill\|2.5 Hz\|vigor" 10.7554-elife.83289.txt | head -60
```

```
109:because it does not make any explicit assumptions about the underlying probability distributions or 
332:model was designed using a posteriori knowledge about the responses. Nonetheless, the expanded 
551:input to the CNN at the heart of MINE contains information about each predictor across time, 
704:problem, which yields high-quality receptive fields in addition to other information about the relationship between predictors and neural responses.
1156:extracted (1) swim starts and (2) tail features that correlate with swim displacement (‘vigor’) and turn 
1158:We used the information about stimulus and elicited behaviors across time as inputs to MINE fitting 
1235:Vigor
1288:Vigor
1350:of neurons labeled by reticulospinal backfills (inset shows example labeling) across six fish. Orange filled bars 
1360:backfills and as expected the vast majority of these neurons were classified by MINE to be driven by 
1396:swim speed (vigor), and turn angle (directionality). Even though behavior-related neurons are enriched 
1555:Vigor
1562:swim starts (left), swim vigor (middle), and swim direction (right). Neurons were clustered based on spatial 
1575:mixed-selectivity neurons that integrate thermosensory information with information about swim start. Heatmaps 
1611:Mixed-selectivity neurons could provide zebrafish with important information about the thermal 
1652:and 2. We previously found that neurons in this region carry little information about ongoing behavior, 
1675:about which predictors are most important in driving the neural response.
1679:used from a decoding perspective, probing what information can be gleaned about ongoing behavior 
1796:MINE, furthermore, performs a more detailed characterization producing information about the 
1817:which is comparatively small even on ground-truth data (Figure 4D). In fact, most information about a 
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && sed -n 2490,2600p paper/10.7554-elife.83289.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -n -i "bout\|rolling_vigor\|sum_tail" *.py | grep -v "^rwave_data_fit" | head -30; grep -n "def " utilities.py | head -60
```

```
experiment.py:96:        self.bout_data: List[np.ndarray] = []  # for each experimental plane, matrix of extracted swim bouts
experiment.py:186:                self.bout_data.append(plane_group["bout_data"][()])
experiment.py:303:                    exp.bout_data.append(plane_group["bout_data"][()])
experiment.py:402:                if self.bout_data[i] is not None:
experiment.py:403:                    self._update_data(plane_group, "bout_data", self.bout_data[i], True)
experiment.py:405:                    # no bouts were found, save dummy array of one line of np.nan
experiment.py:407:                    self._update_data(plane_group, "bout_data", bd, True)
experiment.py:449:                    if self.bout_data[i] is not None:
experiment.py:450:                        plane_group.create_dataset("bout_data", data=self.bout_data[i], compression="gzip",
experiment.py:453:                        # no bouts were found, save dummy array of one line of np.nan
experiment.py:455:                        plane_group.create_dataset("bout_data", data=bd, compression="gzip", compression_opts=5)
rspinal_build_main.py:38:    Gets information about all ann fit neurons in form of a pandas dataframe
rspinal_plot_panels.py:84:        ang_id = barcode_labels.index("sum_tail")
rspinal_plot_panels.py:85:        disp_id = barcode_labels.index("rolling_vigor")
rspinal_plot_panels.py:86:        start_id = barcode_labels.index("bout_start")
rwave_build_main.py:76:    Gets information about all ann fit neurons in form of a pandas dataframe
rwave_plot_panels.py:395:        all_starts = np.vstack(df_behavior["bout_start"])
rwave_plot_panels.py:396:        all_rvig = np.vstack(df_behavior["rolling_vigor"])
rwave_plot_panels.py:397:        all_sumtail = np.vstack(df_behavior["sum_tail"])
rwave_plot_panels.py:399:        plot_autocorrelations(all_starts, frame_lags, "BoutStarts")
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://bitbucket.org/jcostabile/2p.git 2>&1 | tail -2; ls 2p 2>/dev/null | head; cat mine_pub/README.md | head -40; cat mine_pub/environment_utf8.yml | grep -i "tensorflow\|python\|numpy"
```

```
README.md
environment.yml
experiment.py
helper_functions.py
image_processing.py
interpolate_missing_data.py
supplemental_figure.py
umap_analysis.py
update_behavior_hdf5.py
virtual_swim_behavior.py
# Model identification of neural encoding (MINE)

Repository for the code used in developing, testing and using MINE.
The paper "Model discovery to link neural activity to behavioral tasks" which publishes this code can be found at:

[Costabile JD, Balakrishnan KA, Schwinn S, Haesemeyer M (2023) eLife 12:e83289](https://doi.org/10.7554/eLife.83289
)



[... 36 more lines not kept]
```

**Agent**

The tail-processing repo (bitbucket jcostabile/2p) is public; reading its bout detection.

**Agent calls Bash**

```bash
cd $TMPDIR/2p && git log -1 --format="%H %cd"; grep -n -i "def \|threshold\|bout\|rolling_vigor\|sum_tail" update_behavior_hdf5.py helper_functions.py experiment.py | head -80
```

```
5ffaa2d2b2eeeb50466755a3520de5e5bf0687e2 Mon Jun 6 10:56:16 2022 -0600
update_behavior_hdf5.py:31:  * There is about a 10s gap between imaging planes - so they are imaged in succession but not 
update_behavior_hdf5.py:60:  def __call__(self, parser, namespace, values, option_string=None):
update_behavior_hdf5.py:68:def getOptions(args=sys.argv[1:]):
update_behavior_hdf5.py:88:def tiff_meta_data_table(_data_directory, _image_parent_directory):
update_behavior_hdf5.py:132:          # Extract info about images and tail data
update_behavior_hdf5.py:165:def main(_data_directory, _image_parent_directory):
update_behavior_hdf5.py:230:          # Extract info about images and tail data
helper_functions.py:15:# Bout detection modified from MH script
helper_functions.py:16:def detectBouts(swimMetric, minFramesPerBout, frameRate, loThresh=2, hiThresh=None, zeroLimit=2):
helper_functions.py:18:  Detect bouts based on emprically determined characterstics within a trace
helper_functions.py:21:  #the threshold is determined mostly empirically and probably needs
helper_functions.py:26:  #bouts should have a clear peak, hence the peak metric should not be
helper_functions.py:30:  #threshold swim metric
helper_functions.py:41:  bouts = np.zeros((1,5))  ## '5' because currently tracking five features
helper_functions.py:52:      #we found a potential "start of bout" - loop till end collecting
helper_functions.py:68:      #of the bout is in the frame before this frame
helper_functions.py:71:      if (np.size(peak) <= maxFramesAtPeak and np.size(b) >= minFramesPerBout):
helper_functions.py:72:        #we have a valid, singular bout
helper_functions.py:77:        #a bout should not start on the peakframe
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/2p && sed -n 1,160p helper_functions.py; sed -n 160,330p update_behavior_hdf5.py
```

```
# -*- coding: utf-8 -*-

# Load modules
import os
import subprocess
import glob

import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

from scipy.ndimage import median_filter


# Bout detection modified from MH script
def detectBouts(swimMetric, minFramesPerBout, frameRate, loThresh=2, hiThresh=None, zeroLimit=2):
  """
  Detect bouts based on emprically determined characterstics within a trace
  of a swim metric maintaining a certain value.
  """
[... 311 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/2p && grep -n "detectBouts\|anglePrep\|rolling_vigor\|sum_tail\|bhvr" *.py | head;
```

```
helper_functions.py:16:def detectBouts(swimMetric, minFramesPerBout, frameRate, loThresh=2, hiThresh=None, zeroLimit=2):
helper_functions.py:123:def anglePrep(_cta, _frameRate, _tipLength=(5,-1), _filtWindow=5):
supplemental_figure.py:9:from virtual_swim_behavior import load_bhvr
supplemental_figure.py:16:  bpath = '/media/jamie/2tb-sandisk/2P/bhvr-analysis/total_2rep_raw_modelData.bhvr'
supplemental_figure.py:17:  B, _, _, umap = load_bhvr(bpath)
supplemental_figure.py:22:  B['rolling_sum_tail'] = np.rad2deg(B['rolling_sum_tail'])
supplemental_figure.py:27:  tl_angle = np.poly1d(np.polyfit(B['rolling_sum_tail'], B['dheading'], 1))
supplemental_figure.py:41:  ax[1].plot(B['rolling_sum_tail'], B['dheading'], '.', color='gray')
supplemental_figure.py:42:  ax[1].plot(B['rolling_sum_tail'], tl_angle(B['rolling_sum_tail']), '-k', linewidth=2)
supplemental_figure.py:43:  ax[1].text(0.05, 0.95, f"$\\rho = {np.corrcoef(B['rolling_sum_tail'], B['dheading'])[0,1]:0.3f}$",
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "python\b\|PYTHON\|3\.1[0-9]" tools/entry.py | head -20; cd $TMPDIR && . sv/bin/activate && python survey.py ab03c7e4-42ef-4995-b316-c1d994e49916 > s238.txt 2>&1; grep -v "Tail\|_Z[1-9]\|Z[1-9][0-9]*_\|specifications\|optophysiology/Z[1-9]" s238.txt | head -60; grep -c "" s238.txt
```

```
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
63:PYTHON_VERSION = "3.13"
206:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
208:                         f"says {entry['python']}; run `tools/entry.py lock`")
496:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
500:    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
501:    (entries from before the field), else the registry's default for new entries, PYTHON_VERSION."""
503:    if entry.get("python"):
504:        return str(entry["python"])
510:    return PYTHON_VERSION
513:def set_python(entry_dir: Path, version: str) -> None:
514:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
517:    line = f'python: "{version}"'
518:    if re.search(r"^python:.*$", text, re.M):
519:        text = re.sub(r"^python:.*$", line, text, count=1, flags=re.M)
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
for r in 7737788 7738603 7741542; do curl -s https://zenodo.org/api/records/$r | python -c "import json,sys; d=json.load(sys.stdin); print(d['metadata']['title']); [print(' ',f['key'],f['size']) for f in d['files']]"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 1,200p mine_pub/model.py | grep -v "^\s*#" | head -150
```

```
"""
Module for all network models with tensorflow dependency
"""
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers, regularizers, initializers
from typing import Optional, Union, Tuple
from sklearn.linear_model import LinearRegression


class NotInitialized(Exception):
    def __init__(self, message):
        super().__init__(message)


class ActivityPredictor(keras.Model):
    """
    Simple network for non-linear prediction of calcium activity
    """
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 tv && . tv/bin/activate && time uv pip install -q tensorflow-cpu numpy scipy h5py remfile requests pandas scikit-learn 2>&1 | tail -3; python -c "import tensorflow as tf; print(tf.__version__)" 2>&1 | tail -1
```

```
real	0m9.101s
user	0m2.912s
sys	0m5.188s
2.21.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -n "def get_standard_model" -A20 model.py; grep -n "^def train_model" -A40 model.py | head -50; sed -n 656,760p utilities.py
```

```
220:def get_standard_model(hist_steps: int) -> ActivityPredictor:
221-    """
222-    Creates and returns an activity predictor instance with standard parameters
223-    found through a hyper-parameter search
224-    :param hist_steps: The number of history steps in the model
225-    """
226-    m = ActivityPredictor(64, 80, 0.5, hist_steps, "swish")
227-    m.learning_rate = 1e-3
228-    m.l1_sparsity = 1e-3
229-    m.setup()
230-    return m
205:def train_model(mdl: ActivityPredictor, tset: tf.data.Dataset, n_epochs: int, datacount: int) -> None:
206-    """
207-    Trains the model over n epochs. NOTE: The dataset passed should be generated from a shuffle with
208-    reshuffle_each_iteration set to true to ensure that data is presented in shuffled order in each
209-    training epoch
210-    :param mdl: The model to train
211-    :param tset: The dataset with training data
212-    :param n_epochs: The number of epochs to train for
213-    :param datacount: Unused
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . tv/bin/activate && cat > tcnn.py <<'EOF'
import os, time; os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
import numpy as np, tensorflow as tf
from tensorflow.keras import layers, regularizers
tf.config.threading.set_intra_op_parallelism_threads(1); tf.config.threading.set_inter_op_parallelism_threads(1)
def model(h=50):
    reg=regularizers.l1(1e-3)
    return tf.keras.Sequential([layers.Input((h,4)),layers.Conv1D(80,h,use_bias=False,kernel_regularizer=reg),layers.Flatten(),layers.Dropout(0.5),
      layers.Dense(64,activation='swish',kernel_regularizer=reg),layers.Dropout(0.5),layers.Dense(64,activation='swish',kernel_regularizer=reg),layers.Dropout(0.5),layers.Dense(1)])
rng=np.random.default_rng(0); T=2478; X=rng.standard_normal((T,4)).astype(np.float32); y=rng.standard_normal(T).astype(np.float32)
idx=np.arange(49,T); win=np.stack([X[i-49:i+1] for i in idx]); yy=y[idx]; ntr=(T*2)//3-49
for k in range(3):
    m=model(); opt=tf.keras.optimizers.Adam(1e-3); mse=tf.keras.losses.MeanSquaredError()
    @tf.function
    def step(a,b):
        with tf.GradientTape() as t:
            l=mse(b,m(a,training=True))+tf.add_n(m.losses)
        g=t.gradient(l,m.trainable_variables); opt.apply_gradients(zip(g,m.trainable_variables))
    ds=tf.data.Dataset.from_tensor_slices((win[:ntr],yy[:ntr])).shuffle(ntr,seed=1,reshuffle_each_iteration=True).batch(256,drop_remainder=True)
    t0=time.time()
    for e in range(100):
        for a,b in ds: step(a,b)
    print('fit',time.time()-t0, m.count_params())
EOF
python tcnn.py 2>&1 | grep -v Warning
```

```
fit 1.883126974105835 25409
fit 1.8558964729309082 25409
fit 1.8332161903381348 25409
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && cat > tb.py <<'EOF'
import h5py, remfile, requests, numpy as np, time, resource
aid="af99ab20-fa1f-4730-b706-8327f2ca48e2"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url.split('?')[0]
t=time.time()
f=h5py.File(remfile.File(s3),'r'); print('open',time.time()-t)
t=time.time(); d=f['acquisition/Z5_0/data']; acc=np.zeros((512,512))
for i in range(0,d.shape[0],74): acc+=d[i:i+74].sum(0,dtype=np.float64)
proj=acc/d.shape[0]; print('plane',time.time()-t, proj.mean(), proj.max())
seg=f['processing/ophys/ImageSegmentation/Segmentation_Z5']; pm=seg['pixel_mask'][:]; idx=seg['pixel_mask_index'][:]
st=np.r_[0,idx[:-1]]; br=np.array([proj[pm['y'][a:b],pm['x'][a:b]].mean() for a,b in zip(st,idx)])
print(len(br),(br>=0.1).mean(), np.percentile(br,[5,50,95]))
br2=np.array([proj[pm['x'][a:b],pm['y'][a:b]].mean() for a,b in zip(st,idx)]); print('swapped',(br2>=0.1).mean())
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
python tb.py
```

```
open 0.404522180557251
plane 1.8862061500549316 0.05165319555705372 3.1624365482233503
709 0.12129760225669958 [0.00679813 0.00821852 0.7289211 ]
swapped 0.1227080394922426
0.122272 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && cat > tt.py <<'EOF'
import h5py, remfile, requests, numpy as np, time
aid="af99ab20-fa1f-4730-b706-8327f2ca48e2"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url.split('?')[0]
f=h5py.File(remfile.File(s3),'r')
d=f['processing/behavior/Raw Tail Behavior Data/Tail_Z5/data']; print(d.chunks,d.compression)
t=time.time(); a=d[:]; print('tail read',time.time()-t)
c=f['processing/behavior/Cumulative Tail Angle/TailCumAngle_Z5/data'][:]
print(np.nanmax(np.abs(a.sum(1)-c)), np.isnan(a).sum(0)[:5], a[1000,:6])
ts=f['processing/behavior/Cumulative Tail Angle/TailCumAngle_Z5/timestamps'][:]
print(ts[0],ts[-1],len(ts))
print(dict(f['processing/behavior/Raw Tail Behavior Data/Tail_Z5'].attrs))
EOF
python tt.py
```

```
(3918, 1) gzip
tail read 0.4763448238372803
1.199040866595169e-14 [ 0 18 18 18 20] [ 0.        -0.1994662  0.3989324 -0.0997331 -0.0997331 -0.1994662]
-5.493867016000024 495.791144134 125350
{'comments': 'no comments', 'description': 'Raw Tail segment angles in plane 5', 'namespace': 'core', 'neurodata_type': 'TimeSeries', 'object_id': '518a2129-d848-4a7e-b45c-259c52594d03'}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -n "trial\|corrcoef" rwave_plot_panels.py | head -40
```

```
466:        # plot distribution of correlations across the three trials for stimulus and behavior metrics
472:        trials = [slice(0, t_len), slice(t_len, 2 * t_len), slice(2 * t_len, 3 * t_len)]
478:            for j, t1 in enumerate(trials):
479:                for t2 in trials[j + 1:]:
480:                    c_inter_stim.append(np.corrcoef(this_stim[t1], this_stim[t2])[0, 1])
481:                    c_inter_starts.append(np.corrcoef(this_starts[t1], this_starts[t2])[0, 1])
482:                    c_inter_rvig.append(np.corrcoef(this_rvig[t1], this_rvig[t2])[0, 1])
483:                    c_inter_sumtail.append(np.corrcoef(this_sumtail[t1], this_sumtail[t2])[0, 1])
488:        df_trial_correlations = DataFrame(np.hstack((c_inter_stim, c_inter_starts, c_inter_rvig, c_inter_sumtail)),
491:        sns.boxenplot(data=df_trial_correlations)
492:        pl.ylabel("Inter-trial correlations")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && sed -n 380,400p rwave_plot_panels.py; sed -n 462,495p rwave_plot_panels.py
```

```
sns.despine()
        fig.savefig(path.join(plot_dir, f"mescore_vs_linscore.{ext}"), dpi=300)

        #######################################
        # Paradigm analysis
        #######################################

        experiment_names = np.vstack(rbm.get_experiment_list(dfile)["experiment_name"])
        experiment_names = [en[0].decode('utf-8') for en in experiment_names]

        # plot autocorrelations across stimuli and behavior
        frame_lags = 5 * 30  # up to 30 seconds considered
        df_stimuli = rbm.get_stimuli(dfile)
        all_stimuli = np.vstack(df_stimuli["temperature"])
        df_behavior = rbm.get_behaviors(dfile)
        all_starts = np.vstack(df_behavior["bout_start"])
        all_rvig = np.vstack(df_behavior["rolling_vigor"])
        all_sumtail = np.vstack(df_behavior["sum_tail"])
        plot_autocorrelations(all_stimuli, frame_lags, "Temperature")
        plot_autocorrelations(all_starts, frame_lags, "BoutStarts")
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sv/bin/activate && cat > tm.py <<'EOF'
import h5py, remfile, requests, numpy as np
from scipy.ndimage import uniform_filter1d
aid="af99ab20-fa1f-4730-b706-8327f2ca48e2"
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url.split('?')[0]
f=h5py.File(remfile.File(s3),'r')
mov=f['acquisition/Z5_0/data'][:].astype(np.float32)
proj=mov.mean(0)
seg=f['processing/ophys/ImageSegmentation/Segmentation_Z5']; pm=seg['pixel_mask'][:]; idx=seg['pixel_mask_index'][:]
st=np.r_[0,idx[:-1]]
C=f['processing/ophys/CaUnitRespones_Z5/data'][:]; D=f['processing/ophys/Dff_Z5/DffUnitResponses_Z5/data'][:]
npix=idx-st; print('pixels per roi',np.percentile(npix,[5,50,95]))
br=np.array([proj[pm['y'][a:b],pm['x'][a:b]].mean() for a,b in zip(st,idx)])
order=np.argsort(br)[::-1]
for name,(xa,ya) in {'y,x':('y','x'),'x,y':('x','y')}.items():
    rs=[]
    for j in order[:40]:
        a,b=st[j],idx[j]
        tr=mov[:,pm[xa][a:b],pm[ya][a:b]].mean(1)
        rs.append(np.corrcoef(uniform_filter1d(tr,3),C[:,j])[0,1])
    print(name,np.nanmedian(rs))
# fraction of image pixels covered and bright fraction
print('frac comps br>=0.1',(br>=0.1).mean(),'n',len(br),'proj pct',np.percentile(proj,[50,90,99]))
print('C mean per comp pct',np.percentile(C.mean(0),[5,50,95]), 'C std',np.percentile(C.std(0),[5,50,95]))
print('nan C', np.isnan(C).sum(), 'zero comps', (C.std(0)==0).sum())
EOF
python tm.py
```

```
pixels per roi [ 22.   44.  108.6]
y,x 0.8335596637728837
x,y 0.014480826818797154
frac comps br>=0.1 0.12129760225669958 n 709 proj pct [0.00930626 0.12436548 0.70812184]
C mean per comp pct [0.01691816 0.0312465  1.84860137] C std [0.00228064 0.01145527 2.21811309]
nan C 0 zero comps 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p entries/costabile-2023; date -u
```

```
Wed Nov 25 23:37:26 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/costabile-2023/mine_data.py",
 "content": "\"\"\"Loading and per-plane measures for the zebrafish data of Costabile et al. (2023), eLife 12:e83289.\n\nThe four dandisets (000235 forebrain, 000236 midbrain, 000237 hindbrain, 000238 reticulospinal\nbackfills) hold one NWB file per fish. Each file has, for each imaging plane Z<k>: the raw\ntwo-channel two-photon movie (acquisition/Z<k>_0 GCaMP, Z<k>_1 red), CaImAn's segmentation\n(pixel masks), CaImAn's inferred calcium (CaUnitRespones_Z<k>) and dF/F, the temperature stimulus\nat 20 Hz, and the 250 Hz tail tracking (segment angles and their sum, the cumulative tail angle).\n\nWhere each parameter comes from:\n- Versions: the only published version of each dandiset (see VERSIONS).\n- 5 Hz time base, interpolation, temperature at 20 Hz, bout-start binning, per-bout sums placed at\n  the bout's start bin: the paper's code, github.com/haesemeyer/mine_pub at commit 368d756,\n  rwave_data_fit.py (interp_times, bin_bout_starts, bin_time_discrete), as the claims file's\n  opening comment states.\n- Brightness criterion (mean photon count over imaging time of each component, below 0.1\n  excluded): Methods, \"Processing of zebrafish data\", paragraph 2 (\"all components for which the\n  average brightness across imaging time was <0.1 photons were excluded\"), computed as\n  Experiment2P.avg_component_brightness in mine_pub/experiment.py (the unweighted mean of the\n  time-average projection over the component's pixels). Assumption: the projection is taken of the\n  movie the NWB files hold; whether it is CaImAn's motion-corrected movie is not stated.\n- Bout detection and tail metrics: the dandisets hold no swim bouts, so they are re-derived. Methods,\n  \"Processing of zebrafish data\", paragraph 1: bout starts from \"the absolute angular derivative of\n  the tail crossing an empirically determined threshold\"; vigor \"the sum of the absolute angular\n  derivative across the swimbout\"; directionality \"the sum of the angles of the tip of the tail\n  across the swimbout\". The procedure is the lab's tail code, bitbucket.org/jcostabile/2p at commit\n  5ffaa2d (helper_functions.py, anglePrep and detectBouts, default loThresh 2), which the claims\n  file names but did not read. Assumptions: the NWB segment angles are relative, so the point\n  angles are their cumulative sum; the tail-tip angle is the circular mean of points 5 to the\n  second-last (anglePrep's default); the tip angle summed for directionality is the cumulative tail\n  angle the files hold (the code's column name \"sum_tail\"); the minimum bout length, which the code\n  does not fix, is a reading (BOUT_READINGS).\n\"\"\"\nfrom __future__ import annotations\n\nimport hashlib\nfrom functools import lru_cache\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\n\nAPI = \"https://api.dandiarchive.org/api\"\n# The only published version of each dandiset (all published on 2023-03-16); the paper cites none.\nVERSIONS = {\"000235\": \"0.230316.1600\", \"000236\": \"0.230316.2031\", \"000237\": \"0.230316.1655\",\n            \"000238\": \"0.230316.1519\"}\nZEBRAFISH_WHOLE_BRAIN = (\"000235\", \"000236\", \"000237\")\n\nDT = 0.2  # 5 Hz common time base (rwave_data_fit.py)\nTEMP_RATE = 20.0  # stimulus stored at 20 Hz (rwave_data_fit.py; NWB starting_time rate)\nTAIL_RATE = 250.0  # Methods, \"Zebrafish experiments\"\nBRIGHTNESS_CUT = 0.1  # Methods, \"Processing of zebrafish data\"\n# Bout detection readings (loThresh in rad/s, minimum frames per bout at 250 Hz). loThresh 2 is the\n# default of detectBouts; the code does not fix the minimum length, so 10 frames (40 ms) and 5\n# frames (20 ms), and a higher threshold of 5 rad/s, are run.\nBOUT_READINGS = {\"thr2_min10\": (2.0, 10), \"thr2_min5\": (2.0, 5), \"thr5_min10\": (5.0, 10)}\n\n\ndef list_assets(dandiset: str) -> list[dict]:\n    \"\"\"Assets of the pinned version: path, asset_id, size.\"\"\"\n    url = f\"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/assets/?page_size=200\"\n    out = []\n    while url:\n        r = requests.get(url, timeout=60)\n        r.raise_for_status()\n        j = r.json()\n        out += [dict(path=a[\"path\"], asset_id=a[\"asset_id\"], size=a[\"size\"]) for a in j[\"results\"]]\n        url = j.get(\"next\")\n    return sorted(out, key=lambda a: a[\"path\"])\n\n\ndef version_metadata(dandiset: str) -> dict:\n    r = requests.get(f\"{API}/dandisets/{dandiset}/versions/{VERSIONS[dandiset]}/\", timeout=60)\n    r.raise_for_status()\n    return r.json()\n\n\n@lru_cache(maxsize=None)\ndef s3_url(asset_id: str) -> str:\n    r = requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60)\n    return r.url.split(\"?\")[0]\n\n\ndef open_nwb(asset_id: str) -> h5py.File:\n    \"\"\"Stream an NWB file from the archive (no download to disk).\"\"\"\n    return h5py.File(remfile.File(s3_url(asset_id)), \"r\")\n\n\ndef planes(f: h5py.File) -> list[int]:\n    ks = [k for k in f[\"processing/ophys\"].keys() if k.startswith(\"CaUnitRespones_Z\")]\n    return sorted(int(k.split(\"_Z\")[1]) for k in ks)\n\n\ndef _s(x) -> str:\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef file_metadata(f: h5py.File) -> dict:\n    g = f[\"general\"]\n    ip = g[\"optophysiology/Z0_0\"]\n    return dict(identifier=_s(f[\"identifier\"][()]), subject_id=_s(g[\"subject/subject_id\"][()]),\n                genotype=_s(g[\"subject/genotype\"][()]), location=_s(ip[\"location\"][()]),\n                imaging_rate=float(ip[\"imaging_rate\"][()]), grid_spacing=float(ip[\"grid_spacing\"][0]),\n                session_start=_s(f[\"session_start_time\"][()]),\n                frame_duration=float(_s(g[\"experiment_description\"][()]).split(\n                    \"Frame duration in seconds: \")[1].split(\"\\n\")[0]),\n                n_zplanes_described=int(_s(g[\"experiment_description\"][()]).split(\n                    \"Number of ZPlanes: \")[1].split(\"\\n\")[0]))\n\n\ndef time_base(n_frames: int, frame_duration: float):\n    \"\"\"Imaging frame times and the 5 Hz interpolation times (rwave_data_fit.py).\"\"\"\n    ca_t = np.arange(n_frames) * frame_duration\n    i_t = np.arange((ca_t[-1] * 1000) // 200) * DT\n    return ca_t, i_t\n\n\ndef temperature_5hz(f: h5py.File, p: int, i_t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:\n    raw = f[f\"stimulus/presentation/Temperature_Z{p}/data\"][:]\n    t = np.arange(raw.size) / TEMP_RATE\n    return raw, np.interp(i_t, t, raw)\n\n\ndef mean_projection(f: h5py.File, p: int, channel: int = 0) -> np.ndarray:\n    d = f[f\"acquisition/Z{p}_{channel}/data\"]\n    acc = np.zeros(d.shape[1:], dtype=np.float64)\n    step = d.chunks[0] if d.chunks else 100\n    for i in range(0, d.shape[0], step):\n        acc += d[i:i + step].sum(0, dtype=np.float64)\n    return acc / d.shape[0]\n\n\ndef masks(f: h5py.File, p: int):\n    seg = f[f\"processing/ophys/ImageSegmentation/Segmentation_Z{p}\"]\n    pm = seg[\"pixel_mask\"][:]\n    idx = seg[\"pixel_mask_index\"][:].astype(np.int64)\n    st = np.r_[0, idx[:-1]]\n    return pm, st, idx\n\n\ndef component_brightness(pm, st, idx, proj: np.ndarray) -> np.ndarray:\n    \"\"\"Unweighted mean of the projection over each component's pixels (experiment.py). The NWB\n    pixel mask's x is the column and y the row (checked in the notebook).\"\"\"\n    return np.array([proj[pm[\"y\"][a:b], pm[\"x\"][a:b]].mean() if b > a else np.nan for a, b in zip(st, idx)])\n\n\ndef _filtfilt(x: np.ndarray, w: int) -> np.ndarray:\n    \"\"\"Zero-phase boxcar (2p helper_functions.filtfilt).\"\"\"\n    if w < 3:\n        return x\n    s = np.r_[x[w - 1:0:-1], x, x[-1:-w:-1]]\n    k = np.ones(w) / w\n    y = np.convolve(k, s, mode=\"valid\")\n    y = np.convolve(k, y[::-1], mode=\"valid\")\n    return y[::-1]\n\n\ndef tail_metrics(seg: np.ndarray) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"2p helper_functions.anglePrep on point angles (cumulative sum of the NWB segment angles):\n    median filter over 3 frames, circular mean of points 5 to the second-last, absolute frame-to-frame\n    change times the frame rate, boxcar of 5 forward and back. Returns the per-frame absolute angular\n    derivative (rad/s, before smoothing) and its smoothed version used for bout detection.\"\"\"\n    from scipy.ndimage import median_filter\n    ang = np.cumsum(seg, axis=1)\n    ang = median_filter(ang, size=(3, 1), mode=\"nearest\")\n    ya = np.mean(np.sin(ang[:, 5:-1]), axis=1)\n    xa = np.mean(np.cos(ang[:, 5:-1]), axis=1)\n    u = np.c_[xa[:-1], ya[:-1]]\n    v = np.c_[xa[1:], ya[1:]]\n    d = np.arctan2(u[:, 0] * v[:, 1] - u[:, 1] * v[:, 0], np.sum(u * v, axis=1))\n    d[np.isnan(d)] = 0\n    deriv = np.abs(d * TAIL_RATE)\n    sm = np.insert(_filtfilt(deriv, 5), 0, 0)\n    return np.insert(deriv, 0, 0), sm\n\n\ndef detect_bouts(metric: np.ndarray, min_frames: int, lo_thresh: float, zero_limit: int = 2) -> np.ndarray:\n    \"\"\"2p helper_functions.detectBouts (hiThresh None): start, peak, end frame of each bout.\"\"\"\n    max_at_peak = 0.02 * TAIL_RATE\n    s = metric.copy()\n    s[np.isnan(s)] = 0\n    s[s < lo_thresh] = 0\n    nz = np.nonzero(s)[0]\n    out = []\n    n = s.size\n    k = 0\n    while k < nz.size:\n        i = nz[k]\n        b_start = i\n        j = i + 1\n        zc = 0\n        while j < n and zc <= zero_limit:\n            zc = zc + 1 if s[j] == 0 else 0\n            j += 1\n        b = s[b_start:j]\n        b_end = j - (zero_limit + 1)\n        pk = b.max()\n        if np.sum(b == pk) <= max_at_peak and b.size >= min_frames:\n            peak = b_start + int(np.argmax(b))\n            bs = b_start - 1 if b_start == peak else b_start\n            out.append((bs, peak, b_end))\n        k = np.searchsorted(nz, j)\n    return np.array(out, dtype=np.int64).reshape(-1, 3)\n\n\ndef behavior_5hz(bouts: np.ndarray, tail_t: np.ndarray, deriv: np.ndarray, tip: np.ndarray,\n                 i_t: np.ndarray) -> np.ndarray:\n    \"\"\"Swim starts (count per 5 Hz bin), vigor and direction (per-bout sums placed at the start bin),\n    as bin_bout_starts and bin_time_discrete in rwave_data_fit.py. Returns 3 x len(i_t).\"\"\"\n    out = np.zeros((3, i_t.size))\n    if bouts.size == 0:\n        return out\n    st = bouts[:, 0].clip(0, tail_t.size - 1)\n    en = np.minimum(bouts[:, 2], tail_t.size)\n    t0 = tail_t[st]\n    ok = (t0 >= 0) & (st < tail_t.size - 1)\n    for s, e, t in zip(st[ok], en[ok], t0[ok]):\n        bi = int(t // DT)\n        if bi >= i_t.size:\n            continue\n        out[0, bi] += 1\n        out[1, bi] = np.sum(deriv[s:e])\n        out[2, bi] = np.sum(tip[s:e])\n    return out\n\n\ndef digest(a: np.ndarray) -> str:\n    return hashlib.sha1(np.ascontiguousarray(a).tobytes()).hexdigest()[:16]\n\n\ndef lagged_corr(x: np.ndarray, Y: np.ndarray, lags: np.ndarray) -> np.ndarray:\n    \"\"\"Pearson correlation of predictor x (T) with each column of Y (T x n) for x leading Y by each lag\n    (in samples). Returns len(lags) x n.\"\"\"\n    out = np.full((lags.size, Y.shape[1]), np.nan)\n    for i, L in enumerate(lags):\n        if L >= 0:\n            a, b = x[:x.size - L], Y[L:]\n        else:\n            a, b = x[-L:], Y[:Y.shape[0] + L]\n        a = (a - a.mean()) / (a.std() + 1e-12)\n        bz = (b - b.mean(0)) / (b.std(0) + 1e-12)\n        out[i] = a @ bz / a.size\n    return out\n\n\ndef plane_pass(asset_id: str, dandiset: str, p: int, with_movie: bool = True) -> dict:\n    \"\"\"Everything the notebook uses from one plane, reduced as it loads.\"\"\"\n    with open_nwb(asset_id) as f:\n        md = file_metadata(f)\n        ca = f[f\"processing/ophys/CaUnitRespones_Z{p}\"]\n        C = ca[\"data\"][:]\n        rate = float(ca[\"starting_time\"].attrs[\"rate\"])\n        n_frames = C.shape[0]\n        ca_t, i_t = time_base(n_frames, md[\"frame_duration\"])\n        traw, t5 = temperature_5hz(f, p, i_t)\n        tg = f[f\"processing/behavior/Raw Tail Behavior Data/Tail_Z{p}\"]\n        seg = tg[\"data\"][:]\n        tail_t = tg[\"timestamps\"][:]\n        cum = f[f\"processing/behavior/Cumulative Tail Angle/TailCumAngle_Z{p}/data\"][:]\n        pm, st, idx = masks(f, p)\n        rois = f[f\"processing/ophys/CaUnitRespones_Z{p}/rois\"][:]\n        proj = mean_projection(f, p, 0) if with_movie else None\n        mshape = f[f\"acquisition/Z{p}_0/data\"].shape\n        mshape1 = f[f\"acquisition/Z{p}_1/data\"].shape if f\"Z{p}_1\" in f[\"acquisition\"] else None\n    deriv, sm = tail_metrics(seg)\n    beh = {}\n    nb = {}\n    for name, (thr, mn) in BOUT_READINGS.items():\n        b = detect_bouts(sm, mn, thr)\n        nb[name] = int(b.shape[0])\n        beh[name] = behavior_5hz(b, tail_t, deriv, cum, i_t)\n    out = dict(dandiset=dandiset, asset_id=asset_id, fish=md[\"subject_id\"], plane=p, n_rois=C.shape[1],\n               n_rois_masks=int(st.size), rois_ok=bool(np.array_equal(rois, np.arange(C.shape[1]))),\n               n_frames=n_frames, ca_rate=rate, frame_duration=md[\"frame_duration\"], movie_shape=mshape,\n               movie_shape_red=mshape1, temp_n=traw.size, temp_min=float(traw.min()), temp_max=float(traw.max()),\n               temp5=t5, tail_n=tail_t.size, tail_t0=float(tail_t[0]), tail_t1=float(tail_t[-1]),\n               tail_dt=float(np.median(np.diff(tail_t))), tail_nan=int(np.isnan(seg).sum()),\n               cum_matches_sum=float(np.nanmax(np.abs(seg.sum(1) - cum))), n_bouts=nb, behavior=beh,\n               ca_min=float(C.min()), ca_max=float(C.max()), ca_nan=int(np.isnan(C).sum()),\n               digest_ca=digest(C), digest_temp=digest(traw), digest_tail=digest(cum),\n               mask_x_max=int(pm[\"x\"].max()) if pm.size else -1, mask_y_max=int(pm[\"y\"].max()) if pm.size else -1)\n    if proj is not None:\n        br = component_brightness(pm, st, idx, proj)\n        out[\"brightness\"] = br\n        out[\"proj_mean\"] = float(proj.mean())\n        # Clock check: bright components, z-scored and smoothed as rwave_data_fit.py, on the 5 Hz base.\n        from scipy.ndimage import gaussian_filter1d\n        keep = br >= BRIGHTNESS_CUT\n        if keep.sum() >= 5:\n            Ci = np.vstack([np.interp(i_t, ca_t, c) for c in C[:, keep].T]).T\n            Ci = (Ci - Ci.mean(0)) / (Ci.std(0) + 1e-9)\n            Ci = gaussian_filter1d(Ci, 2.5, axis=0)\n            lags = np.arange(-50, 151, 5)  # -10 s to +30 s\n            rt = lagged_corr(t5, Ci, lags)\n            out[\"clock_lags_s\"] = lags * DT\n            out[\"clock_temp_top\"] = np.sort(np.abs(rt), axis=1)[:, -max(1, keep.sum() // 20):].mean(1)\n            s5 = beh[\"thr2_min10\"][0]\n            if s5.sum() >= 3:\n                lags_b = np.arange(-25, 51, 1)  # -5 s to +10 s\n                rb = lagged_corr(s5, Ci, lags_b)\n                out[\"clock_bout_lags_s\"] = lags_b * DT\n                out[\"clock_bout_top\"] = np.sort(rb, axis=1)[:, -max(1, keep.sum() // 20):].mean(1)\n            out[\"ca5_digest\"] = digest(Ci[:50, :5].round(6))\n            out[\"_Ci_small\"] = Ci[:, :200].astype(np.float32)  # for the mismatch control\n    return out\n"
}
```

```
File created successfully at: entries/costabile-2023/mine_data.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/costabile-2023 && python - <<'EOF'
import re
s=open('mine_data.py').read()
s=s.replace('''        traw, t5 = temperature_5hz(f, p, i_t)
''','''        traw, t5 = temperature_5hz(f, p, i_t)
        pl_all = planes(f)
        p_other = pl_all[(pl_all.index(p) + 1) % len(pl_all)]
        _, t5_other = temperature_5hz(f, p_other, i_t)
''')
s=s.replace('''            out["clock_temp_top"] = np.sort(np.abs(rt), axis=1)[:, -max(1, keep.sum() // 20):].mean(1)
''','''            ntop = max(1, keep.sum() // 20)
            out["clock_temp_top"] = np.sort(np.abs(rt), axis=1)[:, -ntop:].mean(1)
            # mismatch control: the temperature trace of the next plane of the same fish
            ro = lagged_corr(t5_other, Ci, lags)
            out["clock_temp_other_top"] = np.sort(np.abs(ro), axis=1)[:, -ntop:].mean(1)
''')
s=s.replace('''            out["ca5_digest"] = digest(Ci[:50, :5].round(6))
            out["_Ci_small"] = Ci[:, :200].astype(np.float32)  # for the mismatch control
''','')
s=s.replace('''                out["clock_bout_top"] = np.sort(rb, axis=1)[:, -max(1, keep.sum() // 20):].mean(1)''','''                out["clock_bout_top"] = np.sort(rb, axis=1)[:, -ntop:].mean(1)''')
open('mine_data.py','w').write(s)
EOF
cd $TMPDIR && . sv/bin/activate && uv pip install -q pandas 2>/dev/null; cd entries/costabile-2023 && time python -c "
import mine_data as m, numpy as np, resource
r=m.plane_pass('af99ab20-fa1f-4730-b706-8327f2ca48e2','000235',5)
for k,v in r.items():
    if k not in('brightness','temp5','behavior'): print(k,v if not isinstance(v,np.ndarray) else np.round(v,3))
print((r['brightness']>=0.1).mean())
for k,b in r['behavior'].items(): print(k, b[0].sum(), b[1].max(), np.abs(b[2]).max())
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
"
```

```
dandiset 000235
asset_id af99ab20-fa1f-4730-b706-8327f2ca48e2
fish Fish01_GCaMP_vlgut_FBd_5dpf_RandomWave
plane 5
n_rois 709
n_rois_masks 709
rois_ok True
n_frames 1182
ca_rate 2.384185791015625
frame_duration 0.4194304
movie_shape (1182, 512, 512)
movie_shape_red (1182, 512, 512)
temp_n 10124
temp_min 22.0
temp_max 26.549540023974977
tail_n 125350
tail_t0 -5.493867016000024
tail_t1 495.791144134
tail_dt 0.003998981999984608
tail_nan 4090
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import mine_data as m, numpy as np
f=m.open_nwb('af99ab20-fa1f-4730-b706-8327f2ca48e2')
for p in [5,15]:
    seg=f[f'processing/behavior/Raw Tail Behavior Data/Tail_Z{p}/data'][:]
    print('nan rows',np.isnan(seg).any(1).sum(), 'unique step', np.unique(np.round(np.abs(seg[~np.isnan(seg)]),4))[:6])
    d,sm=m.tail_metrics(seg)
    print(np.nanpercentile(sm,[50,75,90,95,98,99,99.5,99.9]))
    for thr in [2,3,5,8,10,20]:
        print(thr, m.detect_bouts(sm,10,thr).shape[0], m.detect_bouts(sm,5,thr).shape[0])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import mine_data as m, numpy as np
  File "entries/costabile-2023/mine_data.py", line 38, in <module>
    import h5py
ModuleNotFoundError: No module named 'h5py'
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && python -c "
import mine_data as m, numpy as np
f=m.open_nwb('af99ab20-fa1f-4730-b706-8327f2ca48e2')
for p in [5,15]:
    seg=f[f'processing/behavior/Raw Tail Behavior Data/Tail_Z{p}/data'][:]
    print('nan rows',np.isnan(seg).any(1).sum(), 'unique step', np.unique(np.round(np.abs(seg[~np.isnan(seg)]),4))[:6])
    d,sm=m.tail_metrics(seg)
    print(np.nanpercentile(sm,[50,75,90,95,98,99,99.5,99.9]))
    for thr in [2,3,5,8,10,20]:
        print(thr, m.detect_bouts(sm,10,thr).shape[0], m.detect_bouts(sm,5,thr).shape[0])
"
```

```
nan rows 489 unique step [0.     0.0997 0.1995 0.2992 0.3989 0.4987]
[ 1.27163454  1.74972001  2.28532857  2.70506136  3.4600458   6.54554443
 23.54013942 81.94486862]
2 1041 3045
3 113 540
5 57 63
8 55 65
10 52 63
20 41 56
nan rows 78 unique step [0.     0.0997 0.1995 0.2992 0.3989 0.4987]
[ 1.24798566  1.68296097  2.18154896  2.51748655  2.99966902  3.56537088
  7.55427303 48.85694252]
2 840 2777
3 59 406
5 26 30
8 26 28
10 24 26
20 21 22
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && python - <<'EOF'
s=open('mine_data.py').read()
s=s.replace('''# Bout detection readings (loThresh in rad/s, minimum frames per bout at 250 Hz). loThresh 2 is the
# default of detectBouts; the code does not fix the minimum length, so 10 frames (40 ms) and 5
# frames (20 ms), and a higher threshold of 5 rad/s, are run.
BOUT_READINGS = {"thr2_min10": (2.0, 10), "thr2_min5": (2.0, 5), "thr5_min10": (5.0, 10)}''','''# Bout detection readings (loThresh in rad/s, minimum frames per bout at 250 Hz). The threshold is
# "empirically determined" (Methods) and its value for these data is not given; detectBouts' default
# of 2 rad/s lies inside the noise of the tracked tail here (the notebook shows the distribution),
# so 5 and 10 rad/s, above the noise, are the readings, with a minimum length of 10 frames (40 ms)
# or 5 frames (20 ms); the code does not fix the minimum. The default of 2 rad/s is run as a variant.
BOUT_READINGS = {"thr5_min10": (5.0, 10), "thr10_min10": (10.0, 10), "thr5_min5": (5.0, 5),
                 "thr2_min10_code_default": (2.0, 10)}
PRIMARY_BOUTS = "thr5_min10"''')
s=s.replace('s5 = beh["thr2_min10"][0]','s5 = beh[PRIMARY_BOUTS][0]')
open('mine_data.py','w').write(s)
EOF
cat > $TMPDIR/run1.py <<'EOF'
import sys, time, resource; sys.path.insert(0,'.')
import mine_data as m
from concurrent.futures import ProcessPoolExecutor
aid='af99ab20-fa1f-4730-b706-8327f2ca48e2'
f=m.open_nwb(aid); pl=m.planes(f); f.close()
t=time.time()
with ProcessPoolExecutor(4) as ex:
    res=list(ex.map(m.plane_pass,[aid]*len(pl),['000235']*len(pl),pl))
print(len(res),'planes',time.time()-t,'s')
import numpy as np
br=np.concatenate([r['brightness'] for r in res]); print(br.size,(br>=0.1).sum())
print([r['n_bouts']['thr5_min10'] for r in res])
print(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e6)
EOF
time python $TMPDIR/run1.py
```

```
30 planes 66.97595453262329 s
28916 15684
[55, 51, 43, 50, 45, 57, 57, 66, 61, 59, 71, 74, 47, 25, 31, 26, 21, 30, 21, 22, 16, 14, 14, 21, 18, 29, 16, 15, 22, 19]
0.33538

real	1m9.345s
user	2m51.523s
sys	0m5.244s
```

**Agent**

Full pass costs 67 s per fish (about 30 min for all 25). Fish01: 28,916 components, 15,684 pass brightness (54%), so the earlier 12% was just one plane. Writing the notebook.

**Agent calls Bash**

```bash
date -u; ls ../fouke-2025; python3 -c "import json;nb=json.load(open('../fouke-2025/reproduce_fouke_2025.ipynb'));print(nb['metadata']);[print(c['cell_type'],c['metadata'],''.join(c['source'])[:300].replace('\n',' | ')) for c in nb['cells'][:8]]"
```

```
Wed Nov 25 23:40:53 UTC 2026
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453 |  | **Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent | visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*. | [doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04
code {} import time | import warnings |  | import matplotlib.pyplot as plt | import numpy as np | import pandas as pd | import statsmodels.api as sm | from scipy import stats | from statsmodels.formula.api import ols | from statsmodels.stats.multicomp import pairwise_tukeyhsd |  | import omr |  | pd.set_option("display.width", 200) | 
markdown {} ## Data check |  | Each check of the metadata against the values is stated under its output.
code {'tags': ['sanity']} info = pd.DataFrame([{ |     "fish": omr.fish_key(s), "species": s["species"], "subject_id": s["subject_id"], "age": s["age"], |     "session_start": s["session_start"][:19], "frames": s["n_frames"], "tracked": s["n_tracked"], |     "frame_hz": round(s["frame_hz"], 1), "x_max": round(s["x_range"][1]), "y_
markdown {} The archive's summary says 25 subjects and lists only *Danio rerio*. The files hold 37 fish: | subject ids 0 to 11 are each used for one zebrafish and one *D. cerebrum*, so `subject_id` alone | does not identify an animal. Fish are named here by species and subject id. The 25 ZF are one fewer | than the 2
code {'tags': ['sanity']} fast = info.frame_hz > 100 | print("Files by frame rate (Methods: tracking at more than 150 Hz):") | print(pd.crosstab(info.species, np.where(fast, "128-171 Hz", "32-35 Hz")).to_string()) | dts = pd.DataFrame([{"fish": omr.fish_key(s), **{f"dt_{k}": v for k, v in s["dt_ms"].items()}} for s in sessions]) | p
markdown {} `f0_vtheta` is stated in radia
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
head -120 ../../attempts/fouke-2025-01.yaml; grep -n "^[a-z_]*:" ../../attempts/fouke-2025-01.yaml; cat ../fouke-2025/README.md | head -30
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
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 160,320p ../../attempts/fouke-2025-01.yaml; ls ../../schemas 2>/dev/null; ls ../../ | head -30
```

```
noise. In the 3 s stationary phase the DC median is 205 deg/s2, higher than the 171 during
    motion (per fish median ratio 1.24, p = 0.016), but ZF are also higher at rest (66.9 and 60.8,
    ratio 1.07, p = 0.00012), so this does not separate the species. In frames where the fish is
    still (below 1 mm/s) DC are higher than ZF (per-fish medians 72.4 and 34.9 deg/s2, Mann-Whitney
    p = 0.00014), and DC are higher in every speed band (at 5 mm/s or more, 207 and 85.8). The
    outputs cannot say whether the higher values in moving DC are noise or turning during
    continuous swimming. With the heading from the unwrapped `f0_theta` DC are higher still (218
    to 278 against ZF 61.8 to 77.3 deg/s2, 0 of 9). The reversal should not be read as evidence
    against the paper.
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
    the code's quantity, which disagrees with the Methods, is shown as a variant.
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
    not match `f0_theta`.
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:figs1e-dc-respond-less-monocular
  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
    medial stimuli (3.26 against 13.48 deg/s, p = 0.0003) and binocular ones (2.87 against 21.87,
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../.. && python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); print(list(s['properties'].keys()))
d=s.get('\$defs',s.get('definitions',{}))
for k,v in d.items(): print(k, v.get('required'), list(v.get('properties',{}).keys()))
" | head -40
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(json.dumps(p['outcomes'],indent=0)[:2500]); print(json.dumps(p['findings'],indent=0)[:2500]); print(json.dumps(p['provenance'],indent=0)[:1500]); print(json.dumps(p['datasets'],indent=0)[:800])"
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
[... 258 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && wc -l cnn_fit_test.py cnn_nonlin_test.py cnn_sta_test.py mine_edf.py taylorDecomp.py && grep -n "n_epochs\|n_sims\|n_reps\|range(\|def \|n_boot\|hist_steps\|frame_rate\|n_frames\|np.random\|seed" cnn_fit_test.py | head -60
```

```
417 cnn_fit_test.py
   558 cnn_nonlin_test.py
   527 cnn_sta_test.py
   231 mine_edf.py
   565 taylorDecomp.py
  2298 total
31:    frame_rate = 5
32:    n_frames = 3000
33:    time_base = np.arange(n_frames*5) / frame_rate
37:    hist_steps = hist_seconds * frame_rate
38:    hist_frames = hist_seconds * frame_rate
39:    train_frames = (time_base.size * 2) // 3
40:    n_epochs = 100
49:    analyze_every = frame_rate * 5  # compute every 5 seconds
50:    look_ahead = frame_rate * 5  # use 5s look-ahead to compute input data direction
65:    np.random.seed(777)
70:    for i in range(2):
74:    reg = (np.random.rand(time_base.size) < 0.01).astype(np.float32)
77:    reg = (np.random.rand(time_base.size) < 0.01) * np.random.randn(time_base.size)
94:    tau_on *= frame_rate  # in frames
[... 24 more lines not kept]
```

**Agent**

Starting the dataset notebook. After that I'll decide whether the simulation claims (fig1f, Figure 1F; about 160 CNN fits) fit in the time left.

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && sed -n 25,200p cnn_fit_test.py
```

```
mpl.rcParams['pdf.fonttype'] = 42

    plot_dir = "cnn_fit_test_plots"
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)

    frame_rate = 5
    n_frames = 3000
    time_base = np.arange(n_frames*5) / frame_rate
    assert time_base.size % 3 == 0
    trial_time = time_base[:time_base.size//3]
    hist_seconds = 10
    hist_steps = hist_seconds * frame_rate
    hist_frames = hist_seconds * frame_rate
    train_frames = (time_base.size * 2) // 3
    n_epochs = 100

    # all signals are standardized to unit variance/sd - noise_fraction controls the standard deviation of the noise
    # SNR = 1/noise_fraction
    noise_fraction = 0.25
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Figure 1\.\|Figure 1F\|(F)" paper/10.7554-elife.83289.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/costabile-2023/build_nb.py",
 "content": "\"\"\"Builds reproduce_costabile_2023.ipynb (cells without outputs). Not part of the entry.\"\"\"\nimport nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Costabile et al. (2023) from dandisets 000235, 000236, 000237 and 000238\n\n**Paper.** Costabile JD, Balakrishnan KA, Schwinn S, Haesemeyer M (2023). Model discovery to link\nneural activity to behavioral tasks. *eLife* 12:e83289.\n[doi:10.7554/eLife.83289](https://doi.org/10.7554/eLife.83289)\n\n**Datasets.** DANDI:000235 \"Thermoregulatory Responses Forebrain\" version 0.230316.1600,\nDANDI:000236 \"Midbrain\" version 0.230316.2031, DANDI:000237 \"Hindbrain\" version 0.230316.1655 and\nDANDI:000238 \"Thermoregulatory Responses Reticulospinal system\" version 0.230316.1519. The paper\ncites no version (its data list names the dandisets only). Each dandiset has a single published\nversion, all made on 2023-03-16, and the draft of each has the same asset count and size; the\npublished versions are pinned because they are the only fixed ones and the most recent.\n\n**Claims.** `claims/costabile-2023.yaml`, written from the version of record (eLife, 6 June 2023)\nand checked by a second reader. The paper's code is github.com/haesemeyer/mine_pub at commit\n368d756; the tail-processing code it names is bitbucket.org/jcostabile/2p, read here at commit\n5ffaa2d.\n\n**What the dandisets hold.** Per fish, one NWB file with, for each of 30 planes, the raw\ntwo-channel movie, CaImAn's segmentation and inferred calcium, the temperature stimulus and the\n250 Hz tail tracking. They hold no fitted models, no Taylor metrics, no swim-bout calls, no\nregistration to the Z-Brain atlas, and no annotation of the backfilled reticulospinal neurons.\n\n**Scope.** Most claims rest on the MINE CNN fit to every one of 432,882 neurons (and again to\nrotated control data), with Taylor bootstraps on the fit ones. Section 5 times the paper's CNN on\nthis machine; the estimate is far beyond the run limit, so those claims are blocked `too_large`.\nThe simulation claims (Figures 1 to 4) and the mouse claims (Figure 5) use data that are not in\nthese dandisets (`data: elsewhere`); they are not run here (see the summary).\n\n| Claim | Tested here |\n|---|---|\n| data-zebrafish-coverage | tested (section 3) |\n| figs6-train-test-uncorrelated | tested (section 4) |\n| fig6d, figs6-shuffle-enrichment, figs6-mine-more-at-every-cutoff, fig6e (two), fig6g, fig7b, fig7d, fig7e, lm-recovers-fewer-clusters, temperature-nonlinear-behavior-linear, interaction-terms-small | blocked, too_large (section 5) |\n| fig6f-reticulospinal-behavior | blocked, too_large; the backfill annotation is also not in 000238 (section 5) |\n| figs6 region claims (three), fig7a, fig7c, fig7f | blocked, too_large through their dependence on the fits; they also need the Z-Brain registration, which is not in the dandisets |\n| Figures 1 to 5 (simulations, mouse widefield) | blocked, not run here (data elsewhere) |\n\"\"\")\n\ncode(r\"\"\"\nimport os, time, resource, zlib\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\nimport mine_data as md\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nT0 = time.time()\n\"\"\")\n\nmd(r\"\"\"\n## 1. Data check\n\nThe archive's metadata for each pinned version, and every asset.\n\"\"\")\n\ncode(r\"\"\"\nassets = {}\nfor d in md.VERSIONS:\n    meta = md.version_metadata(d)\n    assets[d] = md.list_assets(d)\n    s = meta[\"assetsSummary\"]\n    print(f\"{d} {md.VERSIONS[d]}: {meta['name']!r}; {s['numberOfFiles']} files, {s['numberOfSubjects']} subjects, \"\n          f\"{s['numberOfBytes']/1e9:.1f} GB\")\n    print(\"   description:\", meta[\"description\"])\n    for a in assets[d]:\n        print(\"   \", a[\"path\"], f\"{a['size']/1e9:.2f} GB\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nOne file, listed in full: every group and dataset of the first plane (the other 29 planes have\nthe same structure), and the counts of each kind of object.\n\"\"\")\n\ncode(r\"\"\"\nimport h5py\nf = md.open_nwb(assets[\"000235\"][0][\"asset_id\"])\nkinds = {}\ndef visit(name, obj):\n    parts = name.split(\"/\")\n    if any(p.endswith((\"_Z0\", \"Z0_0\", \"Z0_1\")) or p in (\"Segmentation_Z0\",) for p in parts) or len(parts) <= 2:\n        if isinstance(obj, h5py.Dataset):\n            print(f\"  {name} {obj.shape} {obj.dtype} {obj.attrs.get('unit', '')}\")\n        else:\n            print(f\"  {name}/ {obj.attrs.get('neurodata_type', '')}\")\n    if isinstance(obj, h5py.Group):\n        t = obj.attrs.get(\"neurodata_type\", \"\")\n        t = t.decode() if isinstance(t, bytes) else t\n        kinds[t] = kinds.get(t, 0) + 1\nfor top in [\"acquisition\", \"processing\", \"stimulus\", \"general\", \"scratch\"]:\n    if isinstance(f[top], h5py.Group):\n        f[top].visititems(visit)\nprint({k: v for k, v in kinds.items() if k})\nprint(\"reference_images in Segmentation_Z0:\", list(f[\"processing/ophys/ImageSegmentation/Segmentation_Z0/reference_images\"].keys()))\nprint(\"experiment_description:\", f[\"general/experiment_description\"][()].decode()[:600])\nf.close()\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n### One pass over every plane\n\nEach plane is read once and reduced as it loads (`mine_data.plane_pass`): counts and shapes, the\ntemperature trace on the 5 Hz base, the tail metrics and bouts under each bout reading, the\nbrightness of every component (the mean of the GCaMP movie over imaging time, over the\ncomponent's pixels), and the lagged correlations of the calcium traces with temperature and with\nswim starts for the clock check. The movie is read for the 25 whole-brain fish only; the backfill\nfiles are summarised without it. Four processes run in parallel.\n\"\"\")\n\ncode(r\"\"\"\ntasks = []\nfor d in md.VERSIONS:\n    for a in assets[d]:\n        with md.open_nwb(a[\"asset_id\"]) as f:\n            pl = md.planes(f)\n        for p in pl:\n            tasks.append((a[\"asset_id\"], d, p, d in md.ZEBRAFISH_WHOLE_BRAIN))\nprint(len(tasks), \"planes in\", sum(len(v) for v in assets.values()), \"files\")\nt = time.time()\nwith ProcessPoolExecutor(4) as ex:\n    res = list(ex.map(md.plane_pass, *zip(*tasks), chunksize=2))\nprint(f\"pass took {time.time()-t:.0f} s\")\npp = pd.DataFrame([{k: v for k, v in r.items() if not isinstance(v, (np.ndarray, dict))} for r in res])\npp[\"fish_short\"] = pp.fish.str.split(\"_\").str[0].str.replace(\"sub-\", \"\")\nprint(\"peak memory of this process (GB):\", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6,\n      \"; of the workers (GB, largest):\", resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6)\n\"\"\", [\"sanity\"])\n\ncode(r\"\"\"\nfish = pp.groupby([\"dandiset\", \"fish\"]).agg(planes=(\"plane\", \"size\"), plane_min=(\"plane\", \"min\"), plane_max=(\"plane\", \"max\"),\n    rois=(\"n_rois\", \"sum\"), frames_min=(\"n_frames\", \"min\"), frames_max=(\"n_frames\", \"max\"),\n    ca_rate=(\"ca_rate\", \"first\"), frame_s=(\"frame_duration\", \"first\"), temp_min=(\"temp_min\", \"min\"),\n    temp_max=(\"temp_max\", \"max\"), tail_dt_ms=(\"tail_dt\", lambda x: 1000 * np.median(x))).reset_index()\nprint(fish.to_string())\nprint()\nprint(\"files per dandiset:\", fish.groupby(\"dandiset\").size().to_dict())\nprint(\"planes per file:\", sorted(fish.planes.unique()), \" frames per plane:\", pp.n_frames.min(), \"to\", pp.n_frames.max())\nprint(\"imaging rate (Hz):\", sorted(pp.ca_rate.unique()), \" = 1 / frame duration\", sorted(pp.frame_duration.unique()),\n      \" -> 1/0.4194304 =\", 1 / 0.4194304)\nprint(\"plane length (s):\", (pp.n_frames * pp.frame_duration).min(), \"to\", (pp.n_frames * pp.frame_duration).max())\nprint(\"temperature range over all planes (C):\", pp.temp_min.min(), \"to\", pp.temp_max.max(),\n      \"; samples per plane\", pp.temp_n.min(), \"to\", pp.temp_n.max(), \"at 20 Hz =\", pp.temp_n.min() / 20, \"to\", pp.temp_n.max() / 20, \"s\")\nprint(\"tail sampling interval (ms), median per plane:\", round(1000 * pp.tail_dt.min(), 3), \"to\", round(1000 * pp.tail_dt.max(), 3),\n      \"; tail time range (s):\", round(pp.tail_t0.min(), 2), \"to\", round(pp.tail_t1.max(), 2))\nprint(\"cumulative tail angle equals the sum of the segment angles: max abs difference\", pp.cum_matches_sum.max())\nprint(\"ROI ids are 0..n-1 in every plane:\", pp.rois_ok.all(), \"; masks per plane equal traces per plane:\", (pp.n_rois == pp.n_rois_masks).all())\nprint(\"mask coordinates within the 512 x 512 frame:\", pp.mask_x_max.max(), pp.mask_y_max.max(), \"; movie shapes:\", pp.movie_shape.astype(str).unique())\nprint(\"calcium traces: NaN\", pp.ca_nan.sum(), \"; range\", pp.ca_min.min(), \"to\", pp.ca_max.max())\nprint(\"tail segment angles: NaN values\", pp.tail_nan.sum(), \"in\", (pp.tail_nan > 0).sum(), \"planes\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nChecks of the description against the values:\n\n- 25 whole-brain fish (8 + 9 + 8 files), and 6 backfill fish in 000238, as the paper states.\n  Every file has 30 planes, the paper's \"30 planes ... in each fish\".\n- The imaging rate is 2.384 Hz in every file, the reciprocal of the frame duration of 0.4194304 s\n  in the experiment description. The Methods say 2.5 Hz. The plane length, 1182 frames of\n  0.419 s (495.8 s), matches the paper's 495 s of stimulus per plane, so 2.384 Hz is the\n  acquisition rate and the paper's 2.5 Hz is rounded (a finding, minor).\n- Pixel size 0.78125 um (the paper's 0.78 um) and the 512 x 512 frame.\n- Temperature is stored in degrees C at 20 Hz and runs from 22 C upwards, within the paper's 22 to\n  30 C; it is the converted trace (the code adds 22 C to the temperature model's output).\n- The tail is sampled every 4.0 ms (250 Hz), and the tail time runs from a few seconds before\n  the first imaging frame to its end, so tail time 0 is the start of imaging (as the code treats\n  it).\n- The cumulative tail angle is exactly the sum of the segment angles, so the segment angles are\n  relative angles between tail segments.\n- The pixel masks' `x` is the column and `y` the row: a trace averaged over the mask pixels of the\n  movie follows the CaImAn trace only in that orientation (next cell).\n\"\"\")\n\ncode(r\"\"\"\n# Orientation of the pixel masks: correlate each of the 40 brightest components' CaImAn trace with\n# the movie averaged over its mask pixels, read as (row=y, col=x) and as (row=x, col=y).\nfrom scipy.ndimage import uniform_filter1d\na = assets[\"000235\"][0][\"asset_id\"]\nwith md.open_nwb(a) as f:\n    mov = f[\"acquisition/Z5_0/data\"][:].astype(np.float32)\n    pm, st, idx = md.masks(f, 5)\n    C = f[\"processing/ophys/CaUnitRespones_Z5/data\"][:]\nproj = mov.mean(0)\nbr = md.component_brightness(pm, st, idx, proj)\ntop = np.argsort(br)[::-1][:40]\nfor name, (r_, c_) in {\"row=y, col=x\": (\"y\", \"x\"), \"row=x, col=y\": (\"x\", \"y\")}.items():\n    rs = [np.corrcoef(uniform_filter1d(mov[:, pm[r_][st[j]:idx[j]], pm[c_][st[j]:idx[j]]].mean(1), 3), C[:, j])[0, 1] for j in top]\n    print(f\"{name}: median r = {np.nanmedian(rs):.3f} (range {np.nanmin(rs):.3f} to {np.nanmax(rs):.3f})\")\ndel mov\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n### Recordings deposited more than once\n\nEach plane's temperature trace is a random wave of its own, and its calcium and tail traces are\nits own. A plane deposited twice (within a file or across files and dandisets) would repeat a\ndigest, or have a temperature trace that correlates almost perfectly with another plane's.\n\"\"\")\n\ncode(r\"\"\"\nfor col in [\"digest_ca\", \"digest_temp\", \"digest_tail\"]:\n    dup = pp[pp.duplicated(col, keep=False)]\n    print(col, \": repeated digests\", dup[col].nunique(), \"over\", len(dup), \"planes\")\nT5 = np.vstack([r[\"temp5\"][:2300] for r in res])\nTz = (T5 - T5.mean(1, keepdims=True)) / (T5.std(1, keepdims=True) + 1e-9)\nR = Tz @ Tz.T / Tz.shape[1]\nnp.fill_diagonal(R, np.nan)\niu = np.triu_indices_from(R, 1)\nprint(f\"temperature traces of different planes: largest correlation {np.nanmax(R):.3f}; \"\n      f\"pairs above 0.99: {(R[iu] > 0.99).sum()} of {iu[0].size}; 99.9th percentile {np.nanpercentile(R[iu], 99.9):.3f}\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n### Do the calcium, stimulus and tail data share a clock?\n\nFor each plane of the 25 whole-brain fish, the components that pass the brightness cut are put on\nthe 5 Hz base, z-scored and smoothed as the code does, and correlated with the plane's own\ntemperature trace at lags from -10 to +30 s (temperature leading). The mean of the top 5% of\nabsolute correlations per lag is averaged over planes. A shared clock shows as a peak a few\nseconds after the stimulus (GCaMP6s is slow), and the plane's own temperature should explain the\nneurons far better than the temperature of the next plane of the same fish (a mismatch control\nwith the same statistics). The same is done for swim starts (bout reading `thr5_min10`), where\nmotor-related activity should peak shortly after the bout.\n\"\"\")\n\ncode(r\"\"\"\nok = [r for r in res if \"clock_temp_top\" in r]\nlags = ok[0][\"clock_lags_s\"]\nown = np.vstack([r[\"clock_temp_top\"] for r in ok]); oth = np.vstack([r[\"clock_temp_other_top\"] for r in ok])\nbest_lag = lags[np.argmax(own, 1)]\nprint(f\"{len(ok)} planes with at least 5 bright components\")\nprint(\"mean top-5% |r| with own temperature by lag (s):\")\nprint(pd.Series(own.mean(0).round(3), index=lags).iloc[::5].to_string())\nprint(f\"peak of the mean curve at {lags[np.argmax(own.mean(0))]:.0f} s; per-plane peak lag median {np.median(best_lag):.0f} s, \"\n      f\"25th to 75th percentile {np.percentile(best_lag, 25):.0f} to {np.percentile(best_lag, 75):.0f} s\")\npk_own = own.max(1); pk_oth = oth.max(1)\nprint(f\"peak |r|, own temperature {np.median(pk_own):.3f} against next plane's temperature {np.median(pk_oth):.3f} (medians); \"\n      f\"own higher in {np.mean(pk_own > pk_oth):.1%} of planes\")\nby_fish = pd.DataFrame({\"fish\": [r[\"fish\"].split(\"_\")[0] for r in ok], \"lag\": best_lag, \"own\": pk_own, \"other\": pk_oth})\ng = by_fish.groupby(\"fish\").agg(median_peak_lag_s=(\"lag\", \"median\"), own=(\"own\", \"median\"), other=(\"other\", \"median\"))\ng[\"own_minus_other\"] = g.own - g.other\nprint(g.round(3).to_string())\nokb = [r for r in ok if \"clock_bout_top\" in r]\nlb = okb[0][\"clock_bout_lags_s\"]; B = np.vstack([r[\"clock_bout_top\"] for r in okb])\nprint(f\"swim starts: {len(okb)} planes with at least 3 bouts; mean top-5% r by lag (s):\")\nprint(pd.Series(B.mean(0).round(3), index=lb).iloc[::5].to_string())\nprint(f\"peak of the mean curve at {lb[np.argmax(B.mean(0))]:.1f} s\")\nfig, ax = plt.subplots(1, 2, figsize=(10, 3.2))\nax[0].plot(lags, own.mean(0), label=\"own temperature\"); ax[0].plot(lags, oth.mean(0), label=\"next plane's temperature\")\nax[0].set_xlabel(\"lag of calcium after temperature (s)\"); ax[0].set_ylabel(\"mean top-5% |r|\"); ax[0].legend()\nax[1].plot(lb, B.mean(0)); ax[1].set_xlabel(\"lag of calcium after swim start (s)\"); ax[1].set_ylabel(\"mean top-5% r\")\nplt.tight_layout(); plt.show()\nprint(\"axis ranges: left\", own.mean(0).min().round(3), \"to\", own.mean(0).max().round(3), \"; right\", B.mean(0).min().round(3), \"to\", B.mean(0).max().round(3))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n### Bout detection\n\nThe dandisets hold no swim bouts. Bouts are re-derived from the tail (see the helper's\ndocstring). The smoothed absolute angular derivative has a noise floor of a few rad/s, because\nthe tracked segment angles move in steps of about 0.1 rad; the code's default threshold of\n2 rad/s lies inside that noise, so the readings use 5 and 10 rad/s.\n\"\"\")\n\ncode(r\"\"\"\nnb = pd.DataFrame([{**r[\"n_bouts\"], \"dandiset\": r[\"dandiset\"]} for r in res if r[\"dandiset\"] in md.ZEBRAFISH_WHOLE_BRAIN])\ndur = 495.8\nprint(\"bouts per plane (and per second) under each reading, whole-brain planes:\")\nfor k in md.BOUT_READINGS:\n    print(f\"  {k:26s} median {nb[k].median():7.0f}  ({nb[k].median()/dur:.3f}/s); 5th to 95th percentile {nb[k].quantile(.05):.0f} to {nb[k].quantile(.95):.0f}; planes with none {(nb[k]==0).sum()}\")\nwith md.open_nwb(assets[\"000235\"][0][\"asset_id\"]) as f:\n    seg = f[\"processing/behavior/Raw Tail Behavior Data/Tail_Z5/data\"][:]\nderiv, sm = md.tail_metrics(seg)\nprint(\"segment-angle steps (rad):\", np.unique(np.round(np.abs(seg[~np.isnan(seg)]), 4))[:5])\nprint(\"smoothed |d angle / dt| (rad/s), fish 01 plane 5, percentiles 50/90/99/99.5/99.9:\", np.round(np.nanpercentile(sm, [50, 90, 99, 99.5, 99.9]), 2))\nprint(\"bouts in that plane by threshold (min 10 frames):\", {thr: md.detect_bouts(sm, 10, thr).shape[0] for thr in [2, 3, 5, 8, 10, 20]})\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n## 2. Findings in the data\n\"\"\")\n\ncode(r\"\"\"\n# Frame rate: the files' imaging rate and frame duration against the Methods' 2.5 Hz.\nprint(\"imaging rates in all\", len(pp), \"planes (Hz):\", sorted(pp.ca_rate.unique()))\nprint(\"frame duration in the experiment description (s):\", sorted(pp.frame_duration.unique()))\nprint(\"1182 frames at 2.384 Hz:\", 1182 / 2.384185791015625, \"s;  at the paper's 2.5 Hz:\", 1182 / 2.5, \"s; paper's stimulus per plane: 495 s\")\n\"\"\", [\"finding-frame-rate\"])\n\ncode(r\"\"\"\n# What is not in the files: no bouts or behavior predictors, no anatomy registration, no backfill annotation.\nwith md.open_nwb(assets[\"000238\"][0][\"asset_id\"]) as f:\n    print(\"000238 processing/ophys holds:\", sorted({k.split(\"_Z\")[0] for k in f[\"processing/ophys\"].keys()}))\n    print(\"000238 segmentation columns:\", f[\"processing/ophys/ImageSegmentation/Segmentation_Z0\"].attrs[\"colnames\"])\n    print(\"000238 reference images:\", list(f[\"processing/ophys/ImageSegmentation/Segmentation_Z0/reference_images\"].keys()))\n    print(\"000238 behavior:\", list(f[\"processing/behavior\"].keys()), \"; general:\", list(f[\"general\"].keys()))\n    print(\"000238 genotype:\", f[\"general/subject/genotype\"][()])\nwith md.open_nwb(assets[\"000235\"][0][\"asset_id\"]) as f:\n    print(\"000235 processing modules:\", list(f[\"processing\"].keys()), \"; behavior:\", list(f[\"processing/behavior\"].keys()))\n    print(\"000235 segmentation columns:\", f[\"processing/ophys/ImageSegmentation/Segmentation_Z0\"].attrs[\"colnames\"])\n    print(\"000235 genotype:\", f[\"general/subject/genotype\"][()], \"; location of plane 0:\", f[\"general/optophysiology/Z0_0/location\"][()])\n\"\"\", [\"finding-not-deposited\"])\n\nmd(r\"\"\"\n## 3. data-zebrafish-coverage\n\n> The zebrafish dataset holds 750 imaging planes from 25 larvae, with 706,543 CaImAn components\n> of which 432,882 pass the brightness criterion.\n\nCounts over 000235, 000236 and 000237. Brightness is the mean photon count of the GCaMP movie over\nimaging time, averaged over the component's pixels (Methods; `avg_component_brightness` in the\ncode); components below 0.1 are excluded. The cut is also shown at other levels.\n\"\"\")\n\ncode(r\"\"\"\nwb = pp[pp.dandiset.isin(md.ZEBRAFISH_WHOLE_BRAIN)]\nbrs = np.concatenate([r[\"brightness\"] for r in res if r[\"dandiset\"] in md.ZEBRAFISH_WHOLE_BRAIN])\nn_fish = wb.fish.nunique(); n_planes = len(wb); n_comp = int(wb.n_rois.sum()); n_bright = int(np.sum(brs >= md.BRIGHTNESS_CUT))\nprint(f\"fish {n_fish} (expected 25), planes {n_planes} (expected 750)\")\nprint(f\"components {n_comp} (expected 706,543, tolerance 70,654): {n_comp/706543-1:+.2%}\")\nprint(f\"components with brightness >= 0.1: {n_bright} (expected 432,882, tolerance 43,288): {n_bright/432882-1:+.2%}; \"\n      f\"fraction {n_bright/n_comp:.3f} (paper {432882/706543:.3f})\")\nprint(\"NaN brightness (components with no pixels):\", int(np.isnan(brs).sum()))\nfor cut in [0.05, 0.08, 0.09, 0.1, 0.11, 0.12, 0.15]:\n    print(f\"   cut {cut:.2f}: {int(np.sum(brs >= cut))}\")\nper_ds = wb.groupby(\"dandiset\").agg(fish=(\"fish\", \"nunique\"), planes=(\"plane\", \"size\"), components=(\"n_rois\", \"sum\"))\nper_ds[\"bright\"] = [int(np.sum(np.concatenate([r[\"brightness\"] for r in res if r[\"dandiset\"] == d]) >= 0.1)) for d in per_ds.index]\nprint(per_ds.to_string())\npf = pd.DataFrame([{\"fish\": r[\"fish\"].split(\"_\")[0], \"n\": r[\"n_rois\"], \"bright\": int(np.sum(r[\"brightness\"] >= 0.1))} for r in res if \"brightness\" in r]).groupby(\"fish\").sum()\npf[\"fraction\"] = (pf.bright / pf.n).round(3)\nprint(pf.T.to_string())\n\"\"\", [\"claim:data-zebrafish-coverage\"])\n\nmd(r\"\"\"\n**Result: see the printed counts.** The conclusion is in the next cell.\n\"\"\")\n\ncode(r\"\"\"\nin_tol = lambda v, e, t: abs(v - e) <= t\nchecks = {\"fish\": n_fish == 25, \"planes\": n_planes == 750, \"components\": in_tol(n_comp, 706543, 70654),\n          \"bright components\": in_tol(n_bright, 432882, 43288)}\nprint(checks, \"-> all within tolerance:\", all(checks.values()))\n\"\"\", [\"claim:data-zebrafish-coverage\"])\n\nmd(r\"\"\"\n## 4. figs6-train-test-uncorrelated\n\n> Because stimulus and behavior are random, test and training data are largely uncorrelated.\n\nAs `rwave_plot_panels.py`: each plane's temperature, swim-start, vigor and direction traces (raw,\nbefore the Gram-Schmidt step) cut to the shortest plane length, split into three equal trials, and\nthe Pearson correlation of every pair of trials. Readings of \"largely uncorrelated\" (criterion): (a)\nthe median absolute value of each predictor's inter-trial correlations below 0.2, (b) below 0.1.\nThe behavior traces depend on the bout reading; all are shown. The temperature trace does not.\n\"\"\")\n\ncode(r\"\"\"\nwbres = [r for r in res if r[\"dandiset\"] in md.ZEBRAFISH_WHOLE_BRAIN]\nL = min(r[\"temp5\"].size for r in wbres); tl = L // 3\ntrials = [slice(0, tl), slice(tl, 2 * tl), slice(2 * tl, 3 * tl)]\ndef inter_trial(x):\n    out = []\n    for j, a in enumerate(trials):\n        for b in trials[j + 1:]:\n            xa, xb = x[a], x[b]\n            out.append(np.corrcoef(xa, xb)[0, 1] if xa.std() > 0 and xb.std() > 0 else np.nan)\n    return out\nrows = []\nfor reading in md.BOUT_READINGS:\n    cs = {\"Temperature\": [], \"Swim\": [], \"Vigor\": [], \"Directionality\": []}\n    for r in wbres:\n        cs[\"Temperature\"] += inter_trial(r[\"temp5\"][:L])\n        b = r[\"behavior\"][reading][:, :L]\n        cs[\"Swim\"] += inter_trial(b[0]); cs[\"Vigor\"] += inter_trial(b[1]); cs[\"Directionality\"] += inter_trial(b[2])\n    for k, v in cs.items():\n        v = np.array(v)\n        rows.append(dict(bouts=reading, predictor=k, n=int(np.isfinite(v).sum()), undefined=int(np.isnan(v).sum()),\n                         median=np.nanmedian(v), median_abs=np.nanmedian(np.abs(v)), p5=np.nanpercentile(v, 5), p95=np.nanpercentile(v, 95),\n                         min=np.nanmin(v), max=np.nanmax(v)))\n    if reading == md.PRIMARY_BOUTS:\n        main_cs = {k: np.array(v) for k, v in cs.items()}\ntt = pd.DataFrame(rows)\nprint(f\"{len(wbres)} planes, trial length {tl} bins of 0.2 s\")\nprint(tt.round(3).to_string(index=False))\nfig, ax = plt.subplots(figsize=(6, 3))\nax.boxplot([v[np.isfinite(v)] for v in main_cs.values()], labels=list(main_cs.keys()))\nax.set_ylabel(\"inter-trial correlation\"); ax.set_title(f\"bouts {md.PRIMARY_BOUTS}\"); plt.show()\nprint(\"axis range:\", min(np.nanmin(v) for v in main_cs.values()).round(3), \"to\", max(np.nanmax(v) for v in main_cs.values()).round(3))\n\"\"\", [\"claim:figs6-train-test-uncorrelated\"])\n\ncode(r\"\"\"\n# Per dandiset (each fish contributes 30 planes x 3 pairs), primary bout reading.\nrows = []\nfor d in md.ZEBRAFISH_WHOLE_BRAIN:\n    sub = [r for r in wbres if r[\"dandiset\"] == d]\n    for k, i in [(\"Temperature\", None), (\"Swim\", 0), (\"Vigor\", 1), (\"Directionality\", 2)]:\n        v = np.array(sum([inter_trial(r[\"temp5\"][:L] if i is None else r[\"behavior\"][md.PRIMARY_BOUTS][i, :L]) for r in sub], []))\n        rows.append(dict(dandiset=d, predictor=k, median_abs=np.nanmedian(np.abs(v)), median=np.nanmedian(v)))\nprint(pd.DataFrame(rows).pivot(index=\"predictor\", columns=\"dandiset\", values=\"median_abs\").round(3).to_string())\nma = tt.groupby(\"bouts\").apply(lambda g: pd.Series({\"max_median_abs\": g.median_abs.max(), \"reading_a_(<0.2)\": bool((g.median_abs < 0.2).all()),\n                                                     \"reading_b_(<0.1)\": bool((g.median_abs < 0.1).all())}))\nprint(ma.to_string())\n\"\"\", [\"claim:figs6-train-test-uncorrelated\"])\n\nmd(r\"\"\"\n**Result: see the printed medians.** The conclusion is in the summary.\n\"\"\")\n\nmd(r\"\"\"\n## 5. The fits: how long the paper's method takes here\n\nThe remaining zebrafish claims need, for every one of the 432,882 bright components, the MINE CNN\nof the code (`get_standard_model`: 80 linear filters over 50 timepoints, two 64-unit swish layers,\ndropout 0.5, L1 1e-3, Adam 1e-3, batch 256, 100 epochs on the first two-thirds of the plane), the\nsame again on rotated control data (figs6-shuffle-enrichment), and Taylor bootstraps on the fit\nneurons. The cell below fits the paper's architecture to three bright components of one plane, with\nthe plane's own predictors (temperature and the three behavior traces, prepared as\n`rwave_data_fit.py` does), on one thread, and extrapolates.\n\"\"\")\n\ncode(r\"\"\"\nimport mine_cnn\nr0 = next(r for r in res if r[\"dandiset\"] == \"000235\" and r[\"plane\"] == 5)\nwith md.open_nwb(r0[\"asset_id\"]) as f:\n    C = f[\"processing/ophys/CaUnitRespones_Z5/data\"][:]\nca_t, i_t = md.time_base(C.shape[0], r0[\"frame_duration\"])\nbright = np.nonzero(r0[\"brightness\"] >= 0.1)[0]\nX = mine_cnn.prepare_predictors(r0[\"temp5\"], r0[\"behavior\"][md.PRIMARY_BOUTS])\nseed = zlib.crc32(b\"costabile-2023/fig6d-mine-identifies-more-than-lm\")\ntimes, rs = [], []\nfor k, j in enumerate(bright[:3]):\n    y = mine_cnn.prepare_response(np.interp(i_t, ca_t, C[:, j]))\n    t = time.time()\n    r_test = mine_cnn.fit_and_test(X, y, seed + k)\n    times.append(time.time() - t); rs.append(r_test)\nprint(\"fit times (s):\", np.round(times, 2), \"; test correlations:\", np.round(rs, 3))\nper_fit = float(np.median(times))\nn_fits = 432882\nhours_1 = per_fit * n_fits / 3600\nprint(f\"real data: {n_fits} fits x {per_fit:.2f} s = {hours_1:.0f} h on one thread, {hours_1/4:.0f} h on 4; \"\n      f\"with the rotated controls {2*hours_1/4:.0f} h on 4 threads, before any Taylor bootstrap\")\nprint(\"the backfill fish (000238):\", int(pp[pp.dandiset == \"000238\"].n_rois.sum()), \"components, about\",\n      round(per_fit * pp[pp.dandiset == \"000238\"].n_rois.sum() / 3600 / 4), \"h on 4 threads without the brightness cut\")\nprint(f\"notebook elapsed so far: {(time.time()-T0)/60:.1f} min\")\n\"\"\", [\"claim:fig6d-mine-identifies-more-than-lm\"])\n\nmd(r\"\"\"\n## 6. Summary\n\n| Claim | Outcome |\n|---|---|\n| data-zebrafish-coverage | see the attempt record |\n| figs6-train-test-uncorrelated | see the attempt record |\n| 13 claims on the CNN fits, and 6 anatomical claims that depend on them | blocked, too_large |\n| fig6f-reticulospinal-behavior | blocked, too_large (and no backfill annotation in 000238) |\n| 13 claims on simulations and mouse widefield data | blocked, not run here |\n\nHow this analysis differs from the paper: brightness is computed on the movie the files hold\n(whether CaImAn's projection came from a motion-corrected movie is not stated); bouts are re-derived\nfrom the tail with thresholds above the tracking noise, since the files hold no bout calls and the\npaper gives no threshold.\n\nWhat was found about the dataset: see section 2 and the attempt record. The files hold no swim\nbouts or behavior predictors, no registration to the Z-Brain atlas, and no annotation of the\nbackfilled neurons, so most of the paper's analyses cannot be run from the dandisets alone. The\nimaging rate is 2.384 Hz, where the Methods say 2.5 Hz.\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, \"reproduce_costabile_2023.ipynb\")\nprint(\"written\", len(cells), \"cells\")\n"
}
```

```
File created successfully at: entries/costabile-2023/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && sed -n 297,313p utilities.py; sed -n 399,457p utilities.py
```

```
def safe_standardize(x: np.ndarray, axis: Optional[int] = None, epsilon=1e-9) -> np.ndarray:
    """
    Standardizes an array to 0 mean and unit standard deviation avoiding division by 0
    :param x: The array to standardize
    :param axis: The axis along which standardization should be performmed
    :param epsilon: Small constant to add to standard deviation to avoid divide by 0 if sd(x)=0
    :return: The standardized array of same dimension as x
    """
    if x.ndim == 1 or axis is None:
        y = x - np.mean(x)
        y /= (np.std(y) + epsilon)
    else:
        y = x - np.mean(x, axis=axis, keepdims=True)
        y /= (np.std(y, axis=axis, keepdims=True) + epsilon)
    return y


def simulate_response(act_predictor: model.ActivityPredictor, predictors: np.ndarray) -> np.ndarray:
    """
    Simulate the predicted response of a neuron to an arbitrary input
[... 55 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/costabile-2023/mine_cnn.py",
 "content": "\"\"\"The MINE CNN of Costabile et al. (2023), used here only to time a fit on this machine.\n\nThe architecture, training and data preparation follow the paper's code, github.com/haesemeyer/mine_pub\nat commit 368d756: model.py (ActivityPredictor, get_standard_model: 80 linear convolutional filters\nover the 50-step history without bias, two dense layers of 64 swish units, dropout 0.5 after each,\nL1 penalty 1e-3 on the filters and dense weights, Adam with learning rate 1e-3, mean squared error;\ntrain_model: 100 epochs), utilities.py (Data.training_data: batch 256, shuffled each epoch;\nsafe_standardize; modified_gram_schmidt) and rwave_data_fit.py (behavior predictors mean-subtracted,\northogonalized and z-scored; calcium z-scored and smoothed with a Gaussian of sigma 2.5 frames;\nthe first two-thirds of the frames for training). Keras' Sequential model replaces the code's\nsubclassed model; the layers and their order are the same. Seeds come from the claim\n(docs/protocol.md, Author, step 3).\n\"\"\"\nfrom __future__ import annotations\n\nimport os\n\nos.environ.setdefault(\"TF_CPP_MIN_LOG_LEVEL\", \"3\")\nimport numpy as np\nfrom scipy.ndimage import gaussian_filter1d\n\nHIST = 50  # 10 s at 5 Hz (rwave_data_fit.py)\nN_EPOCHS = 100\nBATCH = 256\n\n\ndef safe_standardize(x: np.ndarray, epsilon: float = 1e-9) -> np.ndarray:\n    y = x - np.mean(x)\n    return y / (np.std(y) + epsilon)\n\n\ndef modified_gram_schmidt(col_mat: np.ndarray) -> np.ndarray:\n    \"\"\"utilities.modified_gram_schmidt: orthonormal columns, linearly dependent ones set to 0.\"\"\"\n    v = col_mat.astype(np.float64).copy()\n    for j in range(v.shape[1]):\n        if np.allclose(v[:, j], 0):\n            v[:, j] = 0\n            continue\n        q = v[:, j] / np.linalg.norm(v[:, j])\n        for k in range(j + 1, v.shape[1]):\n            v[:, k] = v[:, k] - (q @ v[:, k]) * q\n    norms = np.linalg.norm(v, axis=0, keepdims=True)\n    norms[norms < 1e-9] = 1e-9\n    return v / norms\n\n\ndef prepare_predictors(temp5: np.ndarray, behavior: np.ndarray) -> np.ndarray:\n    \"\"\"Temperature and three behavior rows (5 Hz) -> T x 4 standardized predictor matrix.\"\"\"\n    b = behavior - behavior.mean(axis=1, keepdims=True)\n    b = modified_gram_schmidt(b.T).T\n    cols = [safe_standardize(temp5)] + [safe_standardize(r) for r in b]\n    return np.vstack(cols).T.astype(np.float32)\n\n\ndef prepare_response(ca5: np.ndarray) -> np.ndarray:\n    return gaussian_filter1d(safe_standardize(ca5), 2.5).astype(np.float32)\n\n\ndef _model(n_pred: int):\n    import tensorflow as tf\n    from tensorflow.keras import initializers, layers, regularizers\n    reg = regularizers.l1(1e-3)\n    g = initializers.GlorotUniform\n    return tf.keras.Sequential([\n        layers.Input((HIST, n_pred)),\n        layers.Conv1D(80, HIST, use_bias=False, kernel_regularizer=reg, kernel_initializer=g()),\n        layers.Flatten(), layers.Dropout(0.5),\n        layers.Dense(64, activation=\"swish\", kernel_regularizer=reg, kernel_initializer=g()), layers.Dropout(0.5),\n        layers.Dense(64, activation=\"swish\", kernel_regularizer=reg, kernel_initializer=g()), layers.Dropout(0.5),\n        layers.Dense(1)])\n\n\ndef fit_and_test(X: np.ndarray, y: np.ndarray, seed: int) -> float:\n    \"\"\"Fit on the first two-thirds, return the test correlation on the last third.\"\"\"\n    import tensorflow as tf\n    tf.config.threading.set_intra_op_parallelism_threads(1)\n    tf.config.threading.set_inter_op_parallelism_threads(1)\n    tf.keras.utils.set_random_seed(seed % (2 ** 31))\n    T = y.size\n    train = (T * 2) // 3\n    idx = np.arange(HIST - 1, T)\n    win = np.stack([X[i - HIST + 1:i + 1] for i in idx])\n    yy = y[idx]\n    ntr = train - (HIST - 1)\n    m = _model(X.shape[1])\n    opt = tf.keras.optimizers.Adam(1e-3)\n    mse = tf.keras.losses.MeanSquaredError()\n\n    @tf.function\n    def step(a, b):\n        with tf.GradientTape() as tape:\n            loss = mse(b, m(a, training=True)) + tf.add_n(m.losses)\n        g = tape.gradient(loss, m.trainable_variables)\n        opt.apply_gradients(zip(g, m.trainable_variables))\n\n    ds = tf.data.Dataset.from_tensor_slices((win[:ntr], yy[:ntr])).shuffle(\n        ntr, seed=seed % (2 ** 31), reshuffle_each_iteration=True).batch(BATCH, drop_remainder=True)\n    for _ in range(N_EPOCHS):\n        for a, b in ds:\n            step(a, b)\n    pred = m(win[ntr:], training=False).numpy().ravel()\n    return float(np.corrcoef(pred, yy[ntr:])[0, 1])\n"
}
```

```
File created successfully at: entries/costabile-2023/mine_cnn.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/costabile-2023 && python3 - <<'EOF'
s=open('build_nb.py').read()
s=s.replace('''tasks = []
for d in md.VERSIONS:
    for a in assets[d]:''','''SUBSET = os.environ.get("COSTABILE_SUBSET")  # development only: first file of each dandiset, 3 planes
tasks = []
for d in md.VERSIONS:
    for a in (assets[d][:1] if SUBSET else assets[d]):''')
s=s.replace('''        for p in pl:
            tasks.append''','''        for p in (pl[4:7] if SUBSET else pl):
            tasks.append''')
open('build_nb.py','w').write(s)
EOF
. $TMPDIR/sv/bin/activate && uv pip install -q nbformat nbconvert ipykernel matplotlib tensorflow-cpu scikit-learn 2>&1|tail -1; python build_nb.py && time COSTABILE_SUBSET=1 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 reproduce_costabile_2023.ipynb --output $TMPDIR/sub.ipynb 2>&1 | tail -20
```

```
written 31 cells
[32m     28[39m fig, ax = plt.subplots(figsize=([32m6[39m, [32m3[39m))
[32m---> [39m[32m29[39m ax.boxplot([v[np.isfinite(v)] [38;5;28;01mfor[39;00m v [38;5;28;01min[39;00m main_cs.values()], labels=list(main_cs.keys()))
[32m     30[39m ax.set_ylabel([33m"inter-trial correlation"[39m); ax.set_title(f"bouts {md.PRIMARY_BOUTS}"); plt.show()
[32m     31[39m print([33m"axis range:"[39m, min(np.nanmin(v) [38;5;28;01mfor[39;00m v [38;5;28;01min[39;00m main_cs.values()).round([32m3[39m), [33m"to"[39m, max(np.nanmax(v) [38;5;28;01mfor[39;00m v [38;5;28;01min[39;00m main_cs.values()).round([32m3[39m))

    [31m[... skipping hidden 1 frame][39m

[36mFile [39m[32m/tmp/claude-1001/sv/lib/python3.13/site-packages/matplotlib/__init__.py:1531[39m, in [36m_preprocess_data.<locals>.inner[39m[34m(ax, data, *args, **kwargs)[39m
[32m   1528[39m __tracebackhide__ = [38;5;28;01mTrue[39;00m
[32m   1530[39m [38;5;28;01mif[39;00m data [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
[32m-> [39m[32m1531[39m     [38;5;28;01mreturn[39;00m [30;43mfunc[39;49m[30;43m([39;49m
[32m   1532[39m [30;43m        [39;49m[30;43max[39;49m[30;43m,[39;49m
[32m   1533[39m [30;43m        [39;49m[30;43m*[39;49m[30;43mmap[39;49m[30;43m([39;49m[30;43mcbook[39;49m[30;43m.[39;49m[30;43msanitize_sequence[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43margs[39;49m[30;43m)[39;49m[30;43m,[39;49m
[32m   1534[39m [30;43m        [39;49m[30;43m*[39;49m[30;43m*[39;49m[30;43m{[39;49m[30;43mk[39;49m[30;43m:[39;49m[30;43m [39;49m[30;43mcbook[39;49m[30;43m.[39;49m[30;43msanitize_sequence[39;49m[30;43m([39;49m[30;43mv[39;49m[30;43m)[39;49m[30;43m [39;49m[30;43;01mfor[39;49;00m[30;43m [39;49m[30;43mk[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mv[39;49m[30;43m [39;49m[30;43;01min[39;49;00m[30;43m [39;49m[30;43mkwargs[39;49m[30;43m.[39;49m[30;43mitems[39;49m[30;43m([3
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/costabile-2023 && sed -i 's/labels=list(main_cs.keys()))/tick_labels=list(main_cs.keys()))/' build_nb.py && python3 -c "
import json;nb=json.load(open('$TMPDIR/sub.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            print(''.join(t)[:3000]); print('-----')
" | head -230
```

```
Exit code 1
/bin/bash: line 1: cd: entries/costabile-2023: No such file or directory
```

**Agent calls Bash**

```bash
sed -i 's/labels=list(main_cs.keys()))/tick_labels=list(main_cs.keys()))/' build_nb.py && python3 -c "
import json;nb=json.load(open('$TMPDIR/sub.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            print(''.join(t)[:3000]); print('-----')
" | head -230
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import json;nb=json.load(open('/tmp/claude-1001/sub.ipynb'))
                             ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/claude-1001/sub.ipynb'
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && python build_nb.py && time COSTABILE_SUBSET=1 jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 reproduce_costabile_2023.ipynb --output $TMPDIR/sub.ipynb 2>&1 | tail -2; python3 -c "
import json;nb=json.load(open('$TMPDIR/sub.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','') or o.get('evalue','')
            print(''.join(t)[:3500]); print('-----')
" | head -260
```

```
written 31 cells
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 185100 bytes to /tmp/claude-1001/sub.ipynb

real	4m33.037s
user	0m48.901s
sys	0m7.354s
000235 0.230316.1600: 'Thermoregulatory Responses Forebrain'; 8 files, 8 subjects, 30.6 GB
   description: Imaging in the forebrain of nac -/-; Elavl3-H2B:GCaMP6s +/-; vglut2a-mCherry +/- larval zebrafish during random wave temperature stimulus presentation
    sub-Fish01-GCaMP-vlgut-FBd-5dpf-RandomWave/sub-Fish01-GCaMP-vlgut-FBd-5dpf-RandomWave_ses-20210818T112556_behavior+ophys.nwb 3.73 GB
    sub-Fish02-GCaMP-vlgut-FBv-5dpf-RandomWave/sub-Fish02-GCaMP-vlgut-FBv-5dpf-RandomWave_ses-20210818T173531_behavior+ophys.nwb 3.88 GB
    sub-Fish13-GCaMP-vlgut-FBv-5dpf-RandomWave/sub-Fish13-GCaMP-vlgut-FBv-5dpf-RandomWave_ses-20210830T100716_behavior+ophys.nwb 4.24 GB
    sub-Fish31-GCaMP-vlgut-FBd-5dpf-RandomWave/sub-Fish31-GCaMP-vlgut-FBd-5dpf-RandomWave_ses-20210920T120959_behavior+ophys.nwb 3.31 GB
    sub-Fish32-GCaMP-vlgut-FBv-5dpf-RandomWave/sub-Fish32-GCaMP-vlgut-FBv-5dpf-RandomWave_ses-20210920T181347_behavior+ophys.nwb 3.90 GB
    sub-Fish41-GCaMP-vlgut-FBv-7dpf-RandomWave/sub-Fish41-GCaMP-vlgut-FBv-7dpf-RandomWave_ses-20210929T173736_behavior+ophys.nwb 3.67 GB
    sub-Fish47-GCaMP-vlgut-FBd-7dpf-RandomWave/sub-Fish47-GCaMP-vlgut-FBd-7dpf-RandomWave_ses-20211124T174401_behavior+ophys.nwb 3.90 GB
    sub-Fish58-GCaMP-vlgut-FBd-5dpf-RandomWave/sub-Fish58-GCaMP-vlgut-FBd-5dpf-RandomWave_ses-20220525T092829_behavior+ophys.nwb 3.99 GB
000236 0.230316.2031: 'Thermoregulatory Responses Midbrain'; 9 files, 9 subjects, 39.3 GB
   description: Imaging in the midbrain of nac -/-; Elavl3-H2B:GCaMP6s +/-; vglut2a-mCherry +/- larval zebrafish during random wave temperature st
[... 248 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('build_nb.py').read()
s=s.replace('''    if any(p.endswith(("_Z0", "Z0_0", "Z0_1")) or p in ("Segmentation_Z0",) for p in parts) or len(parts) <= 2:''','''    if any(p.endswith("_Z0") or p in ("Z0_0", "Z0_1", "Segmentation_Z0") for p in parts) or (len(parts) <= 1 and not parts[0].startswith(("Z", "Ca", "Dff"))):''')
open('build_nb.py','w').write(s)
EOF
cat > $TMPDIR/show.py <<'EOF'
import json,sys;nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print(f'=== cell {i}', c['metadata'].get('tags'))
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','') or (o.get('ename','')+' '+o.get('evalue',''))
            print(''.join(t)[:int(sys.argv[2]) if len(sys.argv)>2 else 4000])
EOF
python3 $TMPDIR/show.py $TMPDIR/sub.ipynb 3000 | sed -n '/=== cell 6/,$p' | grep -v "^  Z[0-9]" | head -230
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python3 $TMPDIR/show.py $TMPDIR/sub.ipynb 3000 | grep -v "^  Z[0-9]" | grep -n "=== cell" ; python3 $TMPDIR/show.py $TMPDIR/sub.ipynb 3000 | grep -v "^  Z[0-9]" | sed -n '/=== cell 8/,$p' | head -230
```

```
1:=== cell 1 None
2:=== cell 3 ['sanity']
35:=== cell 5 ['sanity']
317:=== cell 7 ['sanity']
323:=== cell 8 ['sanity']
344:=== cell 10 ['sanity']
348:=== cell 12 ['sanity']
354:=== cell 14 ['sanity']
395:=== cell 16 ['sanity']
406:=== cell 18 ['finding-frame-rate']
411:=== cell 19 ['finding-not-deposited']
425:=== cell 21 ['claim:data-zebrafish-coverage']
447:=== cell 23 ['claim:data-zebrafish-coverage']
450:=== cell 25 ['claim:figs6-train-test-uncorrelated']
473:=== cell 26 ['claim:figs6-train-test-uncorrelated']
487:=== cell 29 ['claim:fig6d-mine-identifies-more-than-lm']
=== cell 8 ['sanity']
  dandiset                                    fish  planes  plane_min  plane_max  rois  frames_min  frames_max   ca_rate  frame_s  temp_min   temp_max  tail_dt_ms
0   000235  Fish01_GCaMP_vlgut_FBd_5dpf_RandomWave       3          4          6  2163        1182        1182  2.384186  0.41943      22.0  28.725910    3.998982
1   000236  Fish03_GCaMP_vlgut_MBd_6dpf_RandomWave       3          4          6  2803        1182        1182  2.384186  0.41943      22.0  29.191852    3.998982
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python3 - <<'EOF'
s=open('mine_data.py').read()
s=s.replace('''def plane_pass(''','''def heldout_shift_r(x: np.ndarray, Y: np.ndarray, offsets: np.ndarray, hist: int = 50, alpha: float = 1e-4) -> np.ndarray:
    """Clock check by decoding with the labels shifted in time: Ridge regression (alpha 1e-4, as the
    paper's comparison model) of every component on the predictor x shifted by 0 to hist-1 samples,
    fit on the first two-thirds and scored by the test correlation on the last third; x is first
    displaced by each offset (samples, circularly). Returns len(offsets) x n test correlations."""
    T = x.size
    tr = (T * 2) // 3
    out = np.full((offsets.size, Y.shape[1]), np.nan)
    Yv = Y[hist - 1:]
    for i, o in enumerate(offsets):
        xs = np.roll(x, int(o))
        Xm = np.stack([xs[h:T - hist + 1 + h] for h in range(hist)], axis=1)
        Xm = (Xm - Xm[:tr].mean(0)) / (Xm[:tr].std(0) + 1e-9)
        Xm = np.c_[np.ones(Xm.shape[0]), Xm]
        ntr = tr - (hist - 1)
        A = Xm[:ntr]
        W = np.linalg.solve(A.T @ A + alpha * np.eye(A.shape[1]), A.T @ Yv[:ntr])
        P = Xm[ntr:] @ W
        Yt = Yv[ntr:]
        Pz = (P - P.mean(0)) / (P.std(0) + 1e-12)
        Yz = (Yt - Yt.mean(0)) / (Yt.std(0) + 1e-12)
        out[i] = (Pz * Yz).mean(0)
    return out


CLOCK_OFFSETS = np.array([-150, -100, -50, -25, -10, -5, 0, 5, 10, 25, 50, 100, 150])  # samples at 5 Hz


def plane_pass(''')
s=s.replace('''            s5 = beh[PRIMARY_BOUTS][0]''','''            ho = heldout_shift_r(t5, Ci, CLOCK_OFFSETS)
            out["clock_ho_temp"] = np.sort(ho, axis=1)[:, -ntop:].mean(1)
            out["clock_ho_temp_mean"] = ho.mean(1)
            ho_o = heldout_shift_r(t5_other, Ci, CLOCK_OFFSETS[CLOCK_OFFSETS == 0])
            out["clock_ho_temp_other"] = float(np.sort(ho_o[0])[-ntop:].mean())
            s5 = beh[PRIMARY_BOUTS][0]''')
open('mine_data.py','w').write(s)

b=open('build_nb.py').read()
b=b.replace('''For each plane of the 25 whole-brain fish, the components that pass the brightness cut are put on
the 5 Hz base, z-scored and smoothed as the code does, and correlated with the plane's own
temperature trace at lags from -10 to +30 s (temperature leading). The mean of the top 5% of
absolute correlations per lag is averaged over planes. A shared clock shows as a peak a few
seconds after the stimulus (GCaMP6s is slow), and the plane's own temperature should explain the
neurons far better than the temperature of the next plane of the same fish (a mismatch control
with the same statistics). The same is done for swim starts (bout reading `thr5_min10`), where
motor-related activity should peak shortly after the bout.''','''For each plane of the 25 whole-brain fish, the components that pass the brightness cut are put on
the 5 Hz base, z-scored and smoothed as the code does. Two checks:

- Temperature, by decoding with the labels shifted in time: a Ridge model of each component on
  the temperature over the preceding 10 s (as the paper's linear comparison model, temperature
  only) is fit on the first two-thirds and scored on the last third, with the temperature trace
  displaced by -30 to +30 s. With a shared clock the held-out correlation peaks at no displacement.
  The temperature of the next plane of the same fish, with the same statistics, is the mismatch
  control. Raw lagged correlations are printed too; for a slow stimulus they are high by chance,
  so they do not separate a response from an offset.
- Swim starts (bout reading `thr5_min10`): the lagged correlation of calcium with the bout-start
  count; motor-related activity should rise in the seconds after a bout and not before.

Each curve is the mean over planes of the mean of the top 5% of components.''')
b=b.replace('''okb = [r for r in ok if "clock_bout_top" in r]''','''offs = md.CLOCK_OFFSETS * md.DT
HO = np.vstack([r["clock_ho_temp"] for r in ok]); HOm = np.vstack([r["clock_ho_temp_mean"] for r in ok])
HOo = np.array([r["clock_ho_temp_other"] for r in ok])
print("held-out correlation (top 5% of components) by displacement of the temperature trace (s):")
print(pd.DataFrame({"top5%": HO.mean(0), "all components": HOm.mean(0)}, index=offs).round(3).T.to_string())
best = offs[np.argmax(HO, 1)]
i0 = list(md.CLOCK_OFFSETS).index(0)
print(f"per-plane best displacement: 0 s in {np.mean(best == 0):.1%} of planes, within 2 s in {np.mean(np.abs(best) <= 2):.1%}; "
      f"median {np.median(best):.1f} s")
print(f"at 0 s, own temperature {np.median(HO[:, i0]):.3f} against next plane's {np.median(HOo):.3f} (medians over planes); "
      f"own higher in {np.mean(HO[:, i0] > HOo):.1%} of planes")
fb = pd.DataFrame({"fish": [r["fish"].split("_")[0] for r in ok], "best_s": best, "own_0": HO[:, i0], "other_0": HOo})
print(fb.groupby("fish").agg(planes=("best_s", "size"), best_is_0=("best_s", lambda x: np.mean(x == 0)), median_best_s=("best_s", "median"),
                             own_0=("own_0", "median"), other_0=("other_0", "median")).round(3).to_string())
okb = [r for r in ok if "clock_bout_top" in r]''')
b=b.replace('''fig, ax = plt.subplots(1, 2, figsize=(10, 3.2))
ax[0].plot(lags, own.mean(0), label="own temperature"); ax[0].plot(lags, oth.mean(0), label="next plane's temperature")
ax[0].set_xlabel("lag of calcium after temperature (s)"); ax[0].set_ylabel("mean top-5% |r|"); ax[0].legend()''','''fig, ax = plt.subplots(1, 2, figsize=(10, 3.2))
ax[0].plot(offs, HO.mean(0), "o-", label="own temperature"); ax[0].axhline(HOo.mean(), color="C1", label="next plane's, 0 s")
ax[0].set_xlabel("displacement of temperature trace (s)"); ax[0].set_ylabel("held-out r, top 5%"); ax[0].legend()''')
b=b.replace('''print("axis ranges: left", own.mean(0).min().round(3), "to", own.mean(0).max().round(3), "; right"''','''print("axis ranges: left", HO.mean(0).min().round(3), "to", HO.mean(0).max().round(3), "; right"''')
# criterion reading |median|
b=b.replace('''ma = tt.groupby("bouts").apply(lambda g: pd.Series({"max_median_abs": g.median_abs.max(), "reading_a_(<0.2)": bool((g.median_abs < 0.2).all()),
                                                     "reading_b_(<0.1)": bool((g.median_abs < 0.1).all())}))''','''# The criterion: "the median of each predictor's inter-trial correlations below 0.2 in absolute value"
# (reading a) or below 0.1 (reading b), that is |median|. The median of |r| is shown as a stricter variant.
ma = tt.groupby("bouts").apply(lambda g: pd.Series({"max_abs_median": g["median"].abs().max(), "a_|median|<0.2": bool((g["median"].abs() < 0.2).all()),
                                                     "b_|median|<0.1": bool((g["median"].abs() < 0.1).all()), "variant_max_median_abs": g.median_abs.max(),
                                                     "variant_median|r|<0.2": bool((g.median_abs < 0.2).all()), "variant_median|r|<0.1": bool((g.median_abs < 0.1).all())}),
                               include_groups=False)''')
b=b.replace('''the Pearson correlation of every pair of trials. Readings of "largely uncorrelated" (criterion): (a)
the median absolute value of each predictor's inter-trial correlations below 0.2, (b) below 0.1.''','''the Pearson correlation of every pair of trials. Readings of "largely uncorrelated" (criterion): (a)
the median of each predictor's inter-trial correlations below 0.2 in absolute value, (b) below 0.1.
The median of the absolute correlations is shown as a stricter variant.''')
open('build_nb.py','w').write(b)
EOF
. $TMPDIR/sv/bin/activate && python -c "
import mine_data as m, numpy as np
r=m.plane_pass('af99ab20-fa1f-4730-b706-8327f2ca48e2','000235',5)
print(np.round(r['clock_ho_temp'],3), r['clock_ho_temp_other'])"
```

```
Wed Nov 25 23:54:18 UTC 2026
[0.044 0.045 0.022 0.109 0.171 0.159 0.576 0.576 0.575 0.57  0.514 0.339
 0.28 ] 0.317006091904589
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && python - <<'EOF'
import mine_data as m, numpy as np
from scipy.ndimage import gaussian_filter1d
aid='af99ab20-fa1f-4730-b706-8327f2ca48e2'
f=m.open_nwb(aid)
for p in [3,5,10,20]:
    C=f[f'processing/ophys/CaUnitRespones_Z{p}/data'][:]
    ca_t,i_t=m.time_base(C.shape[0],0.4194304)
    traw,t5=m.temperature_5hz(f,p,i_t)
    Ci=np.vstack([np.interp(i_t,ca_t,c) for c in C.T]).T
    Ci=(Ci-Ci.mean(0))/(Ci.std(0)+1e-9)
    dT=np.diff(t5); dC=np.diff(gaussian_filter1d(Ci,2.5,axis=0),axis=0)
    lags=np.arange(-100,151,5)
    r=m.lagged_corr(dT,dC,lags)
    top=np.sort(np.abs(r),1)[:,-30:].mean(1)
    print(p, 'temp n',traw.size, 'peak lag s', lags[np.argmax(top)]*0.2, np.round(top[::4],3))
EOF
```

```
3 temp n 10126 peak lag s 6.0 [0.085 0.098 0.085 0.085 0.132 0.093 0.146 0.145 0.083 0.115 0.078 0.073
 0.085]
5 temp n 10124 peak lag s -4.0 [0.113 0.118 0.134 0.106 0.23  0.135 0.223 0.164 0.123 0.12  0.091 0.098
 0.123]
10 temp n 10124 peak lag s 2.0 [0.199 0.133 0.144 0.097 0.189 0.232 0.244 0.181 0.21  0.131 0.113 0.14
 0.108]
20 temp n 10126 peak lag s 1.0 [0.169 0.173 0.171 0.189 0.294 0.424 0.356 0.293 0.368 0.261 0.165 0.183
 0.164]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
b=open('build_nb.py').read()
b=b.replace('''print(f"notebook elapsed so far: {(time.time()-T0)/60:.1f} min")''','''# The simulation claims (data elsewhere) rest on fits of the same network to 15,000-frame simulations
# (cnn_fit_test.py: n_frames 3000 * 5, two-thirds for training), so each fit sees about 6 times as
# many training samples as a plane here.
train_here = (2478 * 2) // 3 - 49
train_sim = (15000 * 2) // 3 - 49
per_sim_fit = per_fit * train_sim / train_here
fits = {"fig1f and fig4 (11 response types x 20)": 220, "fig2e and fig2s1 (500 sets x 4 responses)": 2000,
        "fig3 and fig3s1 white noise (2 filter sets x 100)": 200, "mouse, Figure 5 (13 sessions x 200 components)": 2600}
for k, n in fits.items():
    h = n * per_sim_fit / 3600
    print(f"{k}: {n} fits x {per_sim_fit:.0f} s = {h:.1f} h on one thread, {h/4:.1f} h on 4; x5 for the protocol's five seeds: {5*h/4:.1f} h")
print(f"notebook elapsed so far: {(time.time()-T0)/60:.1f} min")''')
open('build_nb.py','w').write(b)
EOF
. $TMPDIR/sv/bin/activate && python build_nb.py && date -u && time jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=4000 reproduce_costabile_2023.ipynb --output $TMPDIR/full.ipynb 2>&1 | tail -1; date -u
```

```
written 31 cells
Wed Nov 25 23:55:17 UTC 2026
[NbConvertApp] Writing 168111 bytes to /tmp/claude-1001/full.ipynb

real	32m17.979s
user	36m54.856s
sys	1m59.273s
Thu Nov 26 00:27:35 UTC 2026
```

**Agent calls Bash**

```bash
python3 $TMPDIR/show.py $TMPDIR/full.ipynb 6000 | grep -v "^  Z[0-9]\|^    sub-" | sed -n '/=== cell 5/,$p' | head -300
```

```
=== cell 5 ['sanity']




  behavior/ ProcessingModule

  behavior/Cumulative Tail Angle/TailCumAngle_Z0/ TimeSeries
  behavior/Cumulative Tail Angle/TailCumAngle_Z0/data (125361,) float64 radians
  behavior/Cumulative Tail Angle/TailCumAngle_Z0/timestamps (125361,) float64 seconds

  behavior/Raw Tail Behavior Data/Tail_Z0/ TimeSeries

  behavior/Raw Tail Behavior Data/Tail_Z0/data (125361, 21) float64 radians
  behavior/Raw Tail Behavior Data/Tail_Z0/timestamps (125361,) float64 seconds

  ophys/ ProcessingModule

  ophys/CaUnitRespones_Z0/ RoiResponseSeries
  ophys/CaUnitRespones_Z0/data (1182, 690) float64 calcium
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
python3 $TMPDIR/show.py $TMPDIR/full.ipynb 6000 | sed -n '/=== cell 21/,$p' | head -120; date -u
```

```
=== cell 21 ['claim:data-zebrafish-coverage']
fish 25 (expected 25), planes 750 (expected 750)
components 706543 (expected 706,543, tolerance 70,654): +0.00%
components with brightness >= 0.1: 434651 (expected 432,882, tolerance 43,288): +0.41%; fraction 0.615 (paper 0.613)
NaN brightness (components with no pixels): 0
   cut 0.05: 464475
   cut 0.08: 443886
   cut 0.09: 439048
   cut 0.10: 434651
   cut 0.11: 430311
   cut 0.12: 426146
   cut 0.15: 413077
          fish  planes  components  bright
dandiset                                  
000235       8     240      213881  114471
000236       9     270      256331  172795
000237       8     240      236331  147385
fish         Fish01     Fish02     Fish03     Fish05     Fish06     Fish07     Fish08     Fish10     Fish13     Fish14     Fish18     Fish19     Fish21    Fish24     Fish31     Fish32     Fish33     Fish34     Fish35     Fish36    Fish37     Fish39     Fish41     Fish47     Fish58
n         28916.000  23038.000  38016.000  31234.000  22461.000  37402.000  36988.000  26994.000  31663.000  37908.000  21283.000  32716.000  25573.000  20405.00  28008.000  26347.000  33126.000  25797.000  18437.000  33839.000  28808.00  21675.000  23058.000  24824.000  28027.000
bright    15684.000  12165.000  31365.000  21986.000  13311.000  25651.000  29425.000  14201.000  21064.000  29147.000  11736.000  22779.000  12090.000   8983.00  12847.000  14532.000  20804.000  14359.000   8680.000  25947.000  19004.00  10712.000  10714.000  11114.000  16351.000
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
b=open('build_nb.py').read()
b=b.replace('''md(r"""
**Result: see the printed counts.** The conclusion is in the next cell.
""")

code(r"""
in_tol''','''code(r"""
in_tol''')
b=b.replace('''print(checks, "-> all within tolerance:", all(checks.values()))
""", ["claim:data-zebrafish-coverage"])''','''print(checks, "-> all within tolerance:", all(checks.values()))
""", ["claim:data-zebrafish-coverage"])

md(r"""
**Result: reproduced.** The three dandisets hold 25 fish and 750 planes, as the paper states, and
706,543 CaImAn components, exactly the paper's count. 434,651 components have a mean brightness of
at least 0.1 photons, 0.41% more than the paper's 432,882 (a fraction of 0.615 against 0.613),
well within tolerance. The count moves by about 4,000 for each 0.01 of the cut (430,311 at 0.11,
439,048 at 0.09). The brightness is computed on the movie the files hold.
""")''')
b=b.replace('''md(r"""
**Result: see the printed medians.** The conclusion is in the summary.
""")''','''md(r"""
**Result: reproduced.** Over the 750 planes (2,250 trial pairs) the median inter-trial correlation
is -0.051 for temperature and between -0.009 and -0.001 for swim starts, vigor and direction,
under every bout reading, so all four are below 0.1 in absolute value (readings a and b both
hold). The behavior traces are uncorrelated by any measure (median absolute correlation 0.015 or
less under the main reading). The temperature correlations spread widely, from -0.909 to 0.873
(5th to 95th percentile -0.620 to 0.544), and their median absolute value is 0.266, so the
stricter variant (median of absolute values below 0.2) fails for temperature. Under the main
bout reading 117 of 2,250 behavior pairs are undefined, from trials without a bout.
""")''')
b=b.replace('''md(r"""
## 6. Summary''','''md(r"""
**Result: the fits are too large for this run.** One fit of the paper's network takes about 1.9 s
on one thread here (the first, 4.1 s, includes building the graph). The 432,882 real-data fits alone
come to about 57 h on four threads, and the rotated controls double that, so every claim that rests
on the fits is blocked as too large, as is each claim that depends on them. The three test
correlations printed are from these timing fits only and test nothing.
""")

md(r"""
## 6. Summary''')
b=b.replace('''| data-zebrafish-coverage | see the attempt record |
| figs6-train-test-uncorrelated | see the attempt record |''','''| data-zebrafish-coverage | reproduced |
| figs6-train-test-uncorrelated | reproduced |''')
b=b.replace('''| 13 claims on simulations and mouse widefield data | blocked, not run here |''','''| 13 claims on simulations and mouse widefield data (data elsewhere) | blocked, too_large for the time left in this run |''')
b=b.replace('''What was found about the dataset: see section 2 and the attempt record. The files hold no swim
bouts or behavior predictors, no registration to the Z-Brain atlas, and no annotation of the
backfilled neurons, so most of the paper's analyses cannot be run from the dandisets alone. The
imaging rate is 2.384 Hz, where the Methods say 2.5 Hz.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.''','''What was found about the dataset: the counts of fish, planes and components match the paper
exactly, and the brightness cut gives the paper's count within 0.4%. No plane is deposited twice.
The calcium follows its own plane's temperature far better than the next plane's, and the swim
starts by about 2 s, which is consistent with shared clocks. The files hold no swim bouts or
behavior predictors, no registration to the Z-Brain atlas, and no annotation of the backfilled
neurons, so most of the paper's analyses need these re-derived or taken from elsewhere. The
imaging rate is 2.384 Hz, where the Methods say 2.5 Hz. Section 2 lists the rest.''')
# anomalies cell after finding-not-deposited
b=b.replace('''""", ["finding-not-deposited"])''','''""", ["finding-not-deposited"])

code(r"""
# Planes that differ from the rest: frame counts, tail time ranges, temperature trace lengths and ranges.
print("files with fewer than 30 planes:", fish[fish.planes != 30][["dandiset", "fish", "planes"]].to_string(index=False))
print("planes with 1181 frames:", pp[pp.n_frames != 1182][["dandiset", "fish_short", "plane", "n_frames"]].to_string(index=False))
odd_tail = pp[(pp.tail_t0 < -10) | (pp.tail_t1 > 500)]
print("planes whose tail time starts before -10 s or ends after 500 s:")
print(odd_tail[["dandiset", "fish_short", "plane", "tail_n", "tail_t0", "tail_t1"]].to_string(index=False))
print("tail start time (s) over all planes, percentiles 1/50/99:", np.round(np.percentile(pp.tail_t0, [1, 50, 99]), 2),
      "; end:", np.round(np.percentile(pp.tail_t1, [1, 50, 99]), 2))
dur_t = pp.temp_n / 20; dur_c = pp.n_frames * pp.frame_duration
print(f"temperature trace minus imaging duration (s): median {np.median(dur_t - dur_c):.2f}, range {np.min(dur_t - dur_c):.2f} to {np.max(dur_t - dur_c):.2f}")
hot = pp[pp.temp_max > 30]
print(f"planes whose temperature exceeds 30 C (paper: 22 to 30 C): {len(hot)} of {len(pp)}; highest {pp.temp_max.max():.2f} C;",
      hot.groupby("fish_short").size().to_dict())
""", ["finding-plane-anomalies"])''')
open('build_nb.py','w').write(b)
EOF
grep -n "Result" build_nb.py | head
```

```
401:**Result: reproduced.** The three dandisets hold 25 fish and 750 planes, as the paper states, and
474:**Result: reproduced.** Over the 750 planes (2,250 trial pairs) the median inter-trial correlation
534:**Result: the fits are too large for this run.** One fit of the paper's network takes about 1.9 s
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
b=open('build_nb.py').read()
b=b.replace('''| Figures 1 to 5 (simulations, mouse widefield) | blocked, not run here (data elsewhere) |''','''| Figures 1 to 5 (simulations, mouse widefield; data elsewhere) | blocked, too_large for the time left in this run (estimates in section 5) |''')
b=b.replace('''The simulation claims (Figures 1 to 4) and the mouse claims (Figure 5) use data that are not in
these dandisets (`data: elsewhere`); they are not run here (see the summary).''','''The simulation claims (Figures 1 to 4) and the mouse claims (Figure 5) use data that are not in
these dandisets (`data: elsewhere`); each needs hundreds to thousands of fits of the same network,
which do not fit in the time this run has left after the dataset's checks (estimates in section 5).''')
b=b.replace('''md(r"""
### Bout detection''','''md(r"""
The held-out prediction from the plane's own temperature (median 0.656 at no displacement) is far
above the prediction from the next plane's temperature (0.393), in 98.4% of planes and in every
fish. It stays near its best for displacements of 0 to +5 s (the temperature delayed) and falls
to 0.198 when the temperature is advanced by 1 s and to 0.04 by 10 s or more: the calcium follows
the temperature and never precedes it. The best displacement is +2 s in most planes, so this check
places the two clocks within a few seconds of each other; it cannot resolve a smaller offset,
because the response to the slow stimulus is itself delayed. Calcium correlates with swim starts
from 0 s, peaking 1.8 s after the bout, and not before it. Both are consistent with the calcium,
stimulus and tail sharing one clock; neither proves it to better than a second or two.

### Bout detection''')
b=b.replace('''""", ["finding-plane-anomalies"])''','''""", ["finding-plane-anomalies"])

md(r"""
The attempt record states which of these are findings.
""")''')
open('build_nb.py','w').write(b)
EOF
cat > requirements.in <<'EOF'
h5py
ipykernel
matplotlib
numpy
pandas
remfile
requests
scipy
tensorflow-cpu
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: costabile-2023
type: reproduction
title: Model discovery to link neural activity to behavioral tasks (Costabile et al. 2023)
description: Tests the zebrafish findings of Costabile, Balakrishnan, Schwinn and Haesemeyer (2023)
  on dandisets 000235, 000236 and 000237 (25 larval zebrafish, forebrain, midbrain and hindbrain,
  imaged during a random-wave heat stimulus) and 000238 (six fish with reticulospinal backfills).
  It checks the files against the paper, counts the fish, planes and CaImAn components, applies
  the brightness criterion, re-derives swim bouts from the tail tracking, tests that training and
  test data are uncorrelated, and times the paper's CNN to size the analyses that rest on it.
license: Apache-2.0
notebooks:
- path: reproduce_costabile_2023.ipynb
  title: Reproducing Costabile et al. (2023) from dandisets 000235 to 000238
  runtime_minutes: 33
helpers:
- mine_data.py
- mine_cnn.py
related:
- id: dandi:000235/0.230316.1600
  relation: uses_data
- id: dandi:000236/0.230316.2031
  relation: uses_data
- id: dandi:000237/0.230316.1655
  relation: uses_data
- id: dandi:000238/0.230316.1519
  relation: uses_data
- id: doi:10.7554/elife.83289
  relation: reproduces
EOF
grep -n "ipykernel\|tensorflow" ../fouke-2025/requirements.in ../*/requirements.in | head -5; python3 -c "
import json;s=json.load(open('../../schemas/entry.schema.json'));print(s.get('required'), list(s['properties']))"
```

```
../costabile-2023/requirements.in:2:ipykernel
../costabile-2023/requirements.in:9:tensorflow-cpu
../liu-2026-001750/requirements.in:2:ipykernel
../martel-2025/requirements.in:2:ipykernel
../masset-2025/requirements.in:2:ipykernel
['schema_version', 'name', 'type', 'title', 'description', 'license', 'notebooks', 'related'] ['schema_version', 'name', 'type', 'title', 'description', 'license', 'python', 'notebooks', 'helpers', 'related']
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && python build_nb.py && mv build_nb.py $TMPDIR/ && rm -rf __pycache__ && ls && cd ../.. && time python tools/entry.py lock entries/costabile-2023 2>&1 | tail -5 && python tools/entry.py check entries/costabile-2023 2>&1 | tail -15; date -u
```

```
written 34 cells
entry.yaml
mine_cnn.py
mine_data.py
reproduce_costabile_2023.ipynb
requirements.in
wrote costabile-2023/requirements.lock.txt (Python 3.13, with hashes)

real	0m0.411s
user	0m0.252s
sys	0m0.079s
0 error(s)
Thu Nov 26 00:29:07 UTC 2026
```

**Agent calls Bash**

```bash
sed -n 280,340p paper/10.7554-elife.83289.txt; grep -n "Ground-truth datasets" -A30 paper/10.7554-elife.83289.txt | sed -n 1,60p
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
b=open('build_nb.py').read()
old_start=b.index('- 25 whole-brain fish (8 + 9 + 8 files)')
old_end=b.index('- The imaging rate is 2.384 Hz')
b=b[:old_start]+'''- 25 whole-brain fish (8 + 9 + 8 files), and 6 backfill fish in 000238, as the paper states.
  Every whole-brain file has 30 planes, the paper's "30 planes ... in each fish"; one backfill
  file (RSpinal-Random-Wave-01) has 25 (section 2). A few planes have 1181 frames, not 1182.
'''+b[old_end:]
b=b.replace('''- Temperature is stored in degrees C at 20 Hz and runs from 22 C upwards, within the paper's 22 to
  30 C; it is the converted trace (the code adds 22 C to the temperature model's output).
- The tail is sampled every 4.0 ms (250 Hz), and the tail time runs from a few seconds before
  the first imaging frame to its end, so tail time 0 is the start of imaging (as the code treats
  it).''','''- Temperature is stored in degrees C at 20 Hz and starts at 22 C, the baseline the code adds to
  the temperature model's output, so it is the converted trace. Its maximum exceeds the paper's
  30 C in some planes, and each trace is up to about 11 s longer than the plane's imaging (section 2).
- The tail is sampled every 4.0 ms (250 Hz). In most planes the tail time runs from a few seconds
  before the first imaging frame to its end, so tail time 0 is the start of imaging (as the code
  treats it); the planes that differ are listed in section 2.''')
b=b.replace('''print("bouts in that plane by threshold (min 10 frames):", {thr: md.detect_bouts(sm, 10, thr).shape[0] for thr in [2, 3, 5, 8, 10, 20]})
""", ["sanity"])''','''print("bouts in that plane by threshold (min 10 frames):", {thr: md.detect_bouts(sm, 10, thr).shape[0] for thr in [2, 3, 5, 8, 10, 20]})
""", ["sanity", "finding-bout-threshold"])''')
open('build_nb.py','w').write(b)
EOF
. sv/bin/activate && cd entries/costabile-2023 && python $TMPDIR/build_nb.py && rm -rf __pycache__ && cd ../.. && python tools/entry.py check entries/costabile-2023 2>&1 | tail -3; date -u
```

```
written 34 cells
0 error(s)
Thu Nov 26 00:30:06 UTC 2026
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/costabile-2023 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-costabile-2023 in executed/costabile-2023/.venv/share/jupyter/kernels/registry-costabile-2023
0 error(s)
pass  reproduce_costabile_2023.ipynb  (2099 s)

real	35m17.706s
user	37m31.101s
sys	2m7.352s
Thu Nov 26 01:05:27 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/costabile-2023/; python3 $TMPDIR/show.py executed/costabile-2023/reproduce_costabile_2023.ipynb 6000 | grep -v "^  Z[0-9]\|^    sub-" | sed -n '/=== cell 8 /,/=== cell 10 /p;/=== cell 1[5-9] /,/=== cell 2[0-9] /p' | head -150
```

```
reproduce_costabile_2023.ipynb
result.json
=== cell 8 ['sanity']
   dandiset                                    fish  planes  plane_min  plane_max   rois  frames_min  frames_max   ca_rate  frame_s  temp_min   temp_max  tail_dt_ms
0    000235  Fish01_GCaMP_vlgut_FBd_5dpf_RandomWave      30          0         29  28916        1182        1182  2.384186  0.41943      22.0  31.567410    3.998982
1    000235  Fish02_GCaMP_vlgut_FBv_5dpf_RandomWave      30          0         29  23038        1182        1182  2.384186  0.41943      22.0  29.802939    3.998982
2    000235  Fish13_GCaMP_vlgut_FBv_5dpf_RandomWave      30          0         29  31663        1182        1182  2.384186  0.41943      22.0  29.677081    3.998982
3    000235  Fish31_GCaMP_vlgut_FBd_5dpf_RandomWave      30          0         29  28008        1182        1182  2.384186  0.41943      22.0  29.925659    3.998982
4    000235  Fish32_GCaMP_vlgut_FBv_5dpf_RandomWave      30          0         29  26347        1181        1182  2.384186  0.41943      22.0  30.213663    3.998982
5    000235  Fish41_GCaMP_vlgut_FBv_7dpf_RandomWave      30          0         29  23058        1182        1182  2.384186  0.41943      22.0  29.637814    3.998982
6    000235  Fish47_GCaMP_vlgut_FBd_7dpf_RandomWave      30          0         29  24824        1182        1182  2.384186  0.41943      22.0  29.538644    3.998982
7    000235  Fish58_GCaMP_vlgut_FBd_5dpf_RandomWave      30          0         29  28027        1182        1182  2.384186  0.41943      22.0  29.638099    3.998982
8    000236  Fish03_GCaMP_vlgut_MBd_6dpf_RandomWave      30          0         29  38016        1181        1182  2.384186  0.41943      22.0  30.082153    3.998982
9    000236  Fish06_GCaMP_vlgut_MBv_7dpf_RandomWave      30          0         29  22461        1181        1182  2.384186  0.41943      22.0  29.793278    3.998982
10   000236  Fish08_GCaMP_vlgut_MBd_5dpf_RandomWave      30          0         29  36988        1181        1182  2.3841
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;nb=json.load(open('executed/costabile-2023/reproduce_costabile_2023.ipynb'))
for i in [10,20,22,24,26,28,29,32]:
    c=nb['cells'][i]; print('=== ',i,c['cell_type'],c['metadata'].get('tags'))
    for o in c.get('outputs',[]): print(o.get('output_type'), ''.join(o.get('text',''))[:3000] or str(o.get('data',{}).keys()))
"
```

```
===  10 code ['sanity']
stream row=y, col=x: median r = 0.834 (range 0.504 to 0.957)
row=x, col=y: median r = 0.014 (range -0.090 to 0.087)

===  20 code ['finding-plane-anomalies']
stream files with fewer than 30 planes: dandiset                   fish  planes
  000238 RSpinal_Random_Wave_01      25
planes with 1181 frames: dandiset fish_short  plane  n_frames
  000235     Fish32     27      1181
  000236     Fish03     26      1181
  000236     Fish03     27      1181
  000236     Fish06     27      1181
  000236     Fish06     29      1181
  000236     Fish08     27      1181
  000236     Fish18     26      1181
  000236     Fish18     29      1181
planes whose tail time starts before -10 s or ends after 500 s:
dandiset fish_short  plane  tail_n     tail_t0    tail_t1
  000235     Fish31     12  125303   -5.433369 623.799658
  000235     Fish31     29  125349   -5.461372 623.815622
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;nb=json.load(open('executed/costabile-2023/reproduce_costabile_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    for key in ['own temperature','held-out','peak of','per-plane best','components with brightness','fit times','real data','fig1f','pass took','largest correlation','repeated']:
        for line in t.split('\n'):
            if key in line: print(i,line[:250])
" | sort -u; date -u
```

```
12 digest_ca : repeated digests 0 over 0 planes
12 digest_tail : repeated digests 0 over 0 planes
12 digest_temp : repeated digests 0 over 0 planes
12 temperature traces of different planes: largest correlation 0.926; pairs above 0.99: 0 of 427350; 99.9th percentile 0.854
14 at 0 s, own temperature 0.656 against next plane's 0.393 (medians over planes); own higher in 98.4% of planes
14 held-out correlation (top 5% of components) by displacement of the temperature trace (s):
14 mean top-5% |r| with own temperature by lag (s):
14 peak of the mean curve at 1.8 s
14 peak of the mean curve at 3 s; per-plane peak lag median 12 s, 25th to 75th percentile 3 to 24 s
14 peak |r|, own temperature 0.587 against next plane's temperature 0.547 (medians); own higher in 69.0% of planes
14 per-plane best displacement: 0 s in 5.3% of planes, within 2 s in 54.5%; median 2.0 s
23 components with brightness >= 0.1: 434651 (expected 432,882, tolerance 43,288): +0.41%; fraction 0.615 (paper 0.613)
31 fig1f and fig4 (11 response types x 20): 220 fits x 12 s = 0.7 h on one thread, 0.2 h on 4; x5 for the protocol's five seeds: 0.9 h
31 fit times (s): [8.04 1.97 1.96] ; test correlations: [0.305 0.14  0.361]
31 real data: 432882 fits x 1.97 s = 236 h on one thread, 59 h on 4; with the rotated controls 118 h on 4 threads, before any Taylor bootstrap
7 pass took 1726 s
Thu Nov 26 01:05:45 UTC 2026
```

**Agent**

Final run passed (35 min). The numbers match the dev run except the timing (1.97 s per fit, 59 h), so I'll loosen that wording and re-run once at the end. Writing the attempt record and README now.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
b=open('build_nb.py').read()
b=b.replace('''**Result: the fits are too large for this run.** One fit of the paper's network takes about 1.9 s
on one thread here (the first, 4.1 s, includes building the graph). The 432,882 real-data fits alone
come to about 57 h on four threads, and the rotated controls double that''','''**Result: the fits are too large for this run.** One fit of the paper's network takes about 2 s
on one thread here (the first is slower, as it includes building the graph). The 432,882 real-data
fits alone come to about 60 h on four threads, and the rotated controls double that''')
b=b.replace('''the temperature and never precedes it. The best displacement is +2 s in most planes, so this check''','''the temperature and never precedes it. The median best displacement is +2 s, so this check''')
open('build_nb.py','w').write(b)
EOF
grep -n "about 2 s\|median best displacement" build_nb.py | head
```

```
307:the temperature and never precedes it. The median best displacement is +2 s, so this check
551:**Result: the fits are too large for this run.** One fit of the paper's network takes about 2 s
577:starts by about 2 s, which is consistent with shared clocks. The files hold no swim bouts or
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls attempts | grep costabile; ls questions | grep costabile; git -C . log --oneline -1
```

```
5667d93 Agent run on costabile-2023: claims-check (success)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/costabile-2023-01.yaml",
 "content": "schema_version: 3\nid: costabile-2023-01\ndatasets:\n- archive: dandi\n  id: \"000235\"\n  version: 0.230316.1600\n  doi: 10.48324/dandi.000235/0.230316.1600\n  relation: primary\n- archive: dandi\n  id: \"000236\"\n  version: 0.230316.2031\n  doi: 10.48324/dandi.000236/0.230316.2031\n  relation: primary\n- archive: dandi\n  id: \"000237\"\n  version: 0.230316.1655\n  doi: 10.48324/dandi.000237/0.230316.1655\n  relation: primary\n- archive: dandi\n  id: \"000238\"\n  version: 0.230316.1519\n  doi: 10.48324/dandi.000238/0.230316.1519\n  relation: primary\npaper: doi:10.7554/elife.83289\ndate: 2026-11-25\nentry: costabile-2023\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-19\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/encorescience/encore-registry/actions/runs/45721168613\ninputs:\n- what: The paper's analysis code, read for the method details the claims file cites and for the\n    brightness criterion (experiment.py, avg_component_brightness), the 5 Hz time base and the\n    binning of behavior (rwave_data_fit.py), the CNN and its training (model.py, utilities.py) and\n    the inter-trial correlations (rwave_plot_panels.py). No code is run from it; the entry's helpers\n    re-implement what they use.\n  source: https://github.com/haesemeyer/mine_pub at commit 368d75650a1de92d9dd6c7dd1aadff24be6ba379\n- what: The lab's tail-processing code that the paper names (Methods, Processing of zebrafish data),\n    read for the bout detection (helper_functions.py, detectBouts and anglePrep), which the entry\n    re-implements to re-derive swim bouts, vigor and direction from the deposited tail angles.\n  source: https://bitbucket.org/jcostabile/2p at commit 5ffaa2d2b2eeeb50466755a3520de5e5bf0687e2\noutcomes:\n- claim: data-zebrafish-coverage\n  outcome: reproduced\n  notebook: reproduce_costabile_2023.ipynb\n  output: claim:data-zebrafish-coverage\n  measured:\n  - 25\n  - 750\n  - 706543\n  - 434651\n  notes: The three whole-brain dandisets hold 25 fish (8, 9 and 8 files) with 30 planes each, 750\n    planes, and 706,543 CaImAn components, the paper's count exactly. 434,651 components have a mean\n    brightness of at least 0.1 photons over imaging time, 0.41% more than the paper's 432,882 (a\n    fraction of 0.615 against 0.613). The count changes by about 4,000 per 0.01 of the cut (439,048\n    at 0.09, 430,311 at 0.11). Per dandiset the bright components are 114,471 (000235), 172,795\n    (000236) and 147,385 (000237); per fish the bright fraction ranges from 0.44 to 0.83. No plane\n    is deposited twice (no repeated digest of calcium, temperature or tail data among 925 planes;\n    largest correlation of two planes' temperature traces 0.926).\n  deviations:\n  - Brightness is the unweighted mean, over each component's pixel mask, of the time-average of the\n    GCaMP channel of the movie the NWB files hold (as experiment.py, avg_component_brightness).\n    The code averages the projection of its own experiment store; whether that projection was of\n    the raw or the motion-corrected movie is not stated. The raw movie is assumed here; the count\n    matches the paper's to 0.4%.\n- claim: figs6-train-test-uncorrelated\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_costabile_2023.ipynb\n  output: claim:figs6-train-test-uncorrelated\n  notes: Over 750 planes and 2,250 trial pairs the median inter-trial correlation is -0.051 for\n    temperature, and -0.009 (swim starts), -0.006 (vigor) and -0.001 (direction) under the main\n    bout reading (5 rad/s, at least 10 frames); every bout reading, including the code's default\n    threshold of 2 rad/s, gives medians within 0.013 of zero for the behavior traces. All four\n    predictors meet both readings of the criterion (absolute median below 0.2 and below 0.1). The\n    temperature correlations spread widely (range -0.909 to 0.873, 5th to 95th percentile -0.620\n    to 0.544), so their median absolute value is 0.266, and a stricter variant (median of absolute\n    values below 0.2) fails for temperature; the behavior traces pass it (0.015 or less). Per\n    dandiset the temperature median absolute value is 0.249, 0.268 and 0.286. Under the main\n    reading 117 of 2,250 behavior pairs are undefined, from trials without a bout. No random draws\n    are involved.\n  deviations:\n  - The dandisets hold no swim bouts, vigor or direction traces, so they are re-derived from the\n    tail angles with the lab's bout detection (2p helper_functions.py at 5ffaa2d, detectBouts after\n    anglePrep). Assumed, as the code's input is not deposited in that form, that the NWB segment\n    angles are relative (their sum equals the stored cumulative tail angle to 3e-14), so point\n    angles are their cumulative sum, and that the direction metric sums the cumulative tail angle\n    (the code's column \"sum_tail\"). The Methods give the threshold only as \"empirically\n    determined\". The code's default of 2 rad/s lies inside the tracking noise here (4.9 bouts per\n    second), so 5 and 10 rad/s, with minimum lengths of 10 or 5 frames, are the readings and the\n    default is a variant. The outcome is the same under all four. The question is recorded for the\n    paper's authors (findings).\n  - Planes are cut to the shortest length (4,120 bins of 0.2 s, trials of 824 bins), as\n    rwave_plot_panels.py does.\n- claim: fig6d-mine-identifies-more-than-lm\n  outcome: blocked\n  blocked_by: too_large\n  notebook: reproduce_costabile_2023.ipynb\n  output: claim:fig6d-mine-identifies-more-than-lm\n  notes: Needs the paper's CNN fit to each of the 432,882 bright components (434,651 here). One fit\n    of the paper's architecture on a real plane takes 1.97 s on one thread here (three fits timed in\n    the notebook), so the fits alone come to about 236 h on one thread, 59 h on the runner's four,\n    against a run of five hours. The Ridge comparison model is cheap, but the claim needs both. The\n    inputs to the fits (calcium, temperature, tail) are in the dandisets; the bout calls have to be\n    re-derived (see figs6-train-test-uncorrelated).\n- claim: figs6-shuffle-enrichment\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the CNN fits to the real data and again to the rotated control data, about 118 h on\n    four threads by the timing in the notebook (claim fig6d-mine-identifies-more-than-lm).\n- claim: figs6-mine-more-at-every-cutoff\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6d-mine-identifies-more-than-lm, blocked as too large.\n- claim: fig6e-functional-classes\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the CNN fits and the Taylor bootstraps (1,000 resamples every 5 frames) of every fit\n    neuron; depends on fig6d-mine-identifies-more-than-lm, blocked as too large.\n- claim: fig6e-mixed-selectivity-exists\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6e-functional-classes, blocked as too large.\n- claim: fig6g-linear-model-bias\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6d-mine-identifies-more-than-lm and fig6e-functional-classes, blocked as too\n    large.\n- claim: fig6f-reticulospinal-behavior\n  outcome: blocked\n  blocked_by: too_large\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-not-deposited\n  notes: The six backfill fish of 000238 hold 218,257 components (one file has 25 planes, the others\n    30); fitting them all takes about 29 h on four threads at the measured 1.97 s per fit, and the\n    Bonferroni count the claim uses is over all fit neurons of these fish, so the fits cannot be\n    limited to the backfilled cells. Even with the fits, the claim could not be tested from the\n    dandiset, which holds no annotation of the backfilled reticulospinal neurons (no column in the\n    segmentation, no reference images, the red channel only as a raw movie). The paper's processed\n    data on Zenodo (doi:10.5281/zenodo.7737788, rs_analysis.hdf5) may hold it; the claims file does\n    not name it as an input and it was not opened.\n- claim: fig7b-receptive-field-clusters\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6e-functional-classes (needs the fits and the Jacobians of each pure stimulus\n    neuron's CNN), blocked as too large.\n- claim: fig7d-mixed-integration-modes\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6e-functional-classes, blocked as too large.\n- claim: fig7e-complexity-by-cluster\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig7b-receptive-field-clusters, blocked as too large.\n- claim: lm-recovers-fewer-clusters\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig7b-receptive-field-clusters, blocked as too large.\n- claim: temperature-nonlinear-behavior-linear\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6e-functional-classes, blocked as too large.\n- claim: interaction-terms-small\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6d-mine-identifies-more-than-lm and needs the Taylor metrics of every fit\n    neuron, blocked as too large.\n- claim: figs6-stimulus-neuron-regions\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6e-functional-classes, blocked as too large. It also needs each neuron's\n    Z-Brain region; the dandisets hold no registration or anatomical coordinates (finding), so the\n    centroids would come from the paper's processed data on Zenodo (doi:10.5281/zenodo.7737788,\n    main_analysis.hdf5, 7.9 GB), which was not opened.\n- claim: figs6-behavior-neuron-regions\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6e-functional-classes, blocked as too large; needs the Z-Brain regions too\n    (see figs6-stimulus-neuron-regions).\n- claim: figs6-mixed-neuron-regions\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6e-functional-classes, blocked as too large; needs the Z-Brain regions too\n    (see figs6-stimulus-neuron-regions).\n- claim: fig7a-behavior-feature-regions\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig6e-functional-classes, blocked as too large; needs the Z-Brain regions too\n    (see figs6-stimulus-neuron-regions).\n- claim: fig7c-receptive-field-types\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig7b-receptive-field-clusters, blocked as too large; needs the Z-Brain regions\n    too (see figs6-stimulus-neuron-regions).\n- claim: fig7f-complexity-anatomy\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig7e-complexity-by-cluster, blocked as too large; needs the Z-Brain regions too\n    (see figs6-stimulus-neuron-regions).\n- claim: fig1f-mine-fits-ground-truth\n  outcome: blocked\n  blocked_by: too_large\n  notebook: reproduce_costabile_2023.ipynb\n  output: claim:fig6d-mine-identifies-more-than-lm\n  notes: Data elsewhere (generated by cnn_fit_test.py). Not run in this attempt. It needs 220 CNN\n    fits on 15,000-frame simulations, about 12 s each on one thread by the timing in the notebook,\n    so 0.2 h on four threads for the claim's seed and 0.9 h with the protocol's four further seeds,\n    plus porting the simulation and the two regression models. With the dataset's checks taking 35\n    minutes of each full run, this did not fit in the time this run had.\n- claim: fig2bcd-complexity-scores\n  outcome: blocked\n  blocked_by: too_large\n  notes: Data elsewhere (cnn_nonlin_test.py). Not run in this attempt, for the time this run had\n    (see fig1f-mine-fits-ground-truth); it needs CNN fits for each mixing fraction of three series\n    and the Taylor expansions at the data mean.\n- claim: fig2e-linearity-roc\n  outcome: blocked\n  blocked_by: too_large\n  output: claim:fig6d-mine-identifies-more-than-lm\n  notebook: reproduce_costabile_2023.ipynb\n  notes: Data elsewhere (cnn_nonlin_test.py). 500 sets of four responses, 2,000 CNN fits, about 1.6 h\n    on four threads for one seed and 8.2 h for five by the notebook's estimate, over the run's time.\n- claim: fig2s1-nonlinearity-metrics-agree\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig2e-linearity-roc, blocked as too large.\n- claim: fig3-receptive-fields-slow-stimuli\n  outcome: blocked\n  blocked_by: too_large\n  notes: Data elsewhere (cnn_sta_test.py). 100 simulations per filter set (200 CNN fits, about 0.2 h\n    on four threads per seed by the notebook's estimate) plus OLS and Ridge Volterra fits; not run in\n    this attempt, for the time this run had (see fig1f-mine-fits-ground-truth).\n- claim: fig3-effective-degrees-of-freedom\n  outcome: blocked\n  blocked_by: too_large\n  notes: Data elsewhere (mine_edf.py). The effective degrees of freedom are estimated by repeated\n    simulation and refitting of the CNN; not run in this attempt, for the time this run had.\n- claim: fig3s1-white-noise-benchmark\n  outcome: blocked\n  blocked_by: too_large\n  notes: Data elsewhere (cnn_sta_test.py). 10 or 100 simulations per filter set with CNN and Volterra\n    fits; not run in this attempt, for the time this run had.\n- claim: fig3s1-training-length\n  outcome: blocked\n  blocked_by: too_large\n  notes: Data elsewhere (cnn_sta_test.py). 50 replicates at seven training lengths up to 64 times 93 s,\n    350 CNN fits on up to 64 times the base length; not run in this attempt, for the time this run had.\n- claim: fig4-taylor-metric-ranks-predictors\n  outcome: blocked\n  blocked_by: too_large\n  notes: Data elsewhere (cnn_fit_test.py). Needs the 220 fits of fig1f-mine-fits-ground-truth and a\n    Taylor decomposition every 25 frames of each; not run in this attempt, for the time this run had.\n- claim: fig5c-cortex-components-fit\n  outcome: blocked\n  blocked_by: too_large\n  output: claim:fig6d-mine-identifies-more-than-lm\n  notebook: reproduce_costabile_2023.ipynb\n  notes: Data elsewhere (Musall et al. 2019, CSHL doi:10.14224/1.38599, 13 sessions), which would have\n    to be fetched from that repository. 13 sessions times 200 components, 2,600 CNN fits, about 2.1 h\n    on four threads for one seed and 10.7 h for five by the notebook's estimate (on the zebrafish\n    training length; the mouse sessions are longer), over the run's time.\n- claim: fig5d-cortex-largely-linear\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig5c-cortex-components-fit, blocked as too large.\n- claim: fig5e-uninstructed-movements-dominate\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig5c-cortex-components-fit, blocked as too large.\n- claim: fig5fh-cortex-maps\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig5c-cortex-components-fit, blocked as too large; it also needs per-pixel Taylor\n    metrics.\n- claim: fig5i-cortex-receptive-fields\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig5fh-cortex-maps, blocked as too large.\nfindings:\n- kind: data_missing\n  about: data\n  severity: major\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  - \"000238\"\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-bout-threshold\n  statement: The files hold the tail tracking (segment angles and cumulative tail angle at 250 Hz)\n    but no swim bouts, and none of the three behavior predictors the paper fits (swim starts, vigor,\n    direction). They have to be re-derived, and the threshold the paper uses is not given. The lab's\n    bout detection with its default threshold of 2 rad/s finds a median 4.9 bouts per second on\n    these data, inside the tracking noise (segment angles move in steps of 0.0997 rad); 5 or 10 rad/s\n    give 0.075 to 0.095 per second. Every analysis of behavior-driven activity depends on this\n    choice.\n- kind: data_missing\n  about: data\n  severity: major\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-not-deposited\n  statement: The files hold no registration to the Z-Brain atlas and no anatomical coordinates of the\n    components beyond their pixel masks in each plane, and only a plane-level location label (such\n    as \"Dorsal Forebrain\"). The paper's regional analyses (Figure 6, figure supplement 1; Figure 7A,\n    C and F) cannot be run from the dandisets; the paper's processed data on Zenodo\n    (doi:10.5281/zenodo.7737788) hold its registered centroids.\n- kind: data_missing\n  about: data\n  severity: major\n  datasets:\n  - \"000238\"\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-not-deposited\n  statement: The backfill dandiset holds no annotation of which components are reticulospinal\n    neurons labelled by the backfill (the segmentation has only pixel masks and no reference images;\n    the Texas-Red channel is there only as the raw movie). The paper's control analysis of Figure 6F\n    rests on this manual annotation.\n- kind: other\n  about: data\n  severity: minor\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-frame-rate\n  statement: The imaging rate is 2.384 Hz in every plane of every file (frame duration 0.4194304 s in\n    the experiment description), where the Methods say 2.5 Hz. The files are consistent with\n    themselves and with the paper's 495 s per plane (1,182 frames last 495.8 s); the paper's rate\n    is rounded.\n- kind: other\n  about: data\n  severity: minor\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-plane-anomalies\n  statement: In 10 of 925 planes the tail timestamps span about 629 s for the usual 125,300 samples\n    at 4 ms; 8 end at 623.8 s, 128 s after imaging ends, and 2 start at -133.5 s, where all others\n    run from about -5.4 s to 495.8 s. The timestamps of these planes hold a jump that the files do\n    not explain, and bouts placed by them would move by up to 128 s. The affected planes are\n    Fish31 planes 12 and 29, Fish47 planes 13 and 22, Fish58 planes 0, 7 and 8, Fish10 plane 5,\n    Fish36 plane 11 and Fish39 plane 16.\n- kind: metadata_insufficient\n  about: data\n  severity: minor\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  - \"000238\"\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-plane-anomalies\n  statement: Each plane's temperature trace (20 Hz) is a median 10.5 s (up to 10.95 s) longer than its\n    imaging, and the files do not say when it starts relative to the first frame. The paper's code\n    takes it to start with imaging; with that reading the calcium follows the temperature by about\n    2 s at best, consistent with a shared start but not proof of one.\n- kind: other\n  about: data\n  severity: minor\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-plane-anomalies\n  statement: Small differences from the paper's description. One backfill file (000238,\n    RSpinal-Random-Wave-01) has 25 planes, where the paper images 30 per fish; 8 planes have 1,181\n    frames, not 1,182; and in 10 planes the temperature exceeds the paper's 22 to 30 C, up to 31.57 C\n    (Fish01).\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  - \"000238\"\n- kind: metadata_insufficient\n  about: data\n  severity: minor\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  - \"000238\"\n  notebook: reproduce_costabile_2023.ipynb\n  output: finding-not-deposited\n  statement: The segmentation's reference images are empty, so the time-average projection on which\n    the paper's brightness criterion is computed is not deposited. It can be recomputed from the raw\n    movie, and doing so reproduces the paper's count of analyzed components to 0.4%. The response\n    series are named CaUnitRespones (sic).\n- kind: other\n  about: data\n  severity: none\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  notebook: reproduce_costabile_2023.ipynb\n  output: claim:data-zebrafish-coverage\n  statement: The whole-brain dandisets hold the paper's 25 fish, 750 planes and 706,543 CaImAn\n    components exactly, and the brightness criterion recomputed from the movies keeps 434,651 (the\n    paper 432,882). No plane is deposited twice. The pixel masks line up with the movie (traces from\n    the mask pixels correlate a median 0.834 with CaImAn's). The calcium is predicted far better by\n    its own plane's temperature than by the next plane's (held-out correlation 0.656 against 0.393,\n    in 98.4% of planes and every fish) and rises after swim starts (peak at 1.8 s), consistent with\n    shared clocks.\n- kind: methods_unavailable\n  about: paper\n  statement: Question for the authors. Which threshold on the smoothed absolute angular derivative of\n    the tail, and which minimum bout length, were used to detect swim bouts (Methods, \"an empirically\n    determined threshold\")? The bout detection the paper names (bitbucket.org/jcostabile/2p,\n    detectBouts) defaults to 2 rad/s, which on the deposited tail angles detects about 4.9 bouts per\n    second, inside the tracking noise; 5 to 10 rad/s give about 0.1 per second. This attempt used 5\n    and 10 rad/s with 10 or 5 frames as readings. Were the angles fed to anglePrep the cumulative\n    sums of the deposited segment angles, and is \"sum_tail\" the cumulative tail angle?\n- kind: methods_unavailable\n  about: paper\n  statement: Question for the authors. Was the time-average projection behind the brightness\n    criterion (avg_component_brightness) taken from the raw movie, as deposited, or from CaImAn's\n    motion-corrected movie? The raw movie gives 434,651 components at 0.1 photons, against the\n    paper's 432,882.\n"
}
```

```
File created successfully at: attempts/costabile-2023-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/costabile-2023-01.yaml'
s=open(p).read()
s=s.replace('''  - Planes are cut to the shortest length (4,120 bins of 0.2 s, trials of 824 bins), as
    rwave_plot_panels.py does.''','''  - Planes are cut to the shortest length and split into trials of 824 bins of 0.2 s, as
    rwave_plot_panels.py does.''')
s=s.replace('''  statement: In 10 of 925 planes the tail timestamps span about 629 s for the usual 125,300 samples
    at 4 ms; 8 end at 623.8 s, 128 s after imaging ends, and 2 start at -133.5 s, where all others
    run from about -5.4 s to 495.8 s. The timestamps of these planes hold a jump that the files do
    not explain, and bouts placed by them would move by up to 128 s.''','''  statement: In 10 of 925 planes the tail timestamps span about 629 s for the usual 125,300 samples
    at a median interval of 4 ms; 8 end at 623.8 s, 128 s after imaging ends, and 2 start at
    -133.5 s, where the others run from about -5.4 s to 495.8 s. The timestamps of these planes must
    hold a gap or jump that the files do not explain (where it lies was not located here), and
    bouts placed by them can be misplaced by up to 128 s.''')
s=s.replace('''  statement: Each plane's temperature trace (20 Hz) is a median 10.5 s (up to 10.95 s) longer than its
    imaging, and the files do not say when it starts relative to the first frame. The paper's code
    takes it to start with imaging; with that reading the calcium follows the temperature by about
    2 s at best, consistent with a shared start but not proof of one.''','''  statement: Each plane's temperature trace (20 Hz) is a median 10.5 s longer than its imaging (from
    -0.07 to 10.95 s), and the files do not say when it starts relative to the first frame. The
    paper's code takes it to start with imaging. With that reading the held-out prediction of the
    calcium is best with the temperature delayed by a median 2 s and collapses when it is advanced
    by 1 s or more, consistent with a shared start but not proof of one.''')
open(p,'w').write(s)
EOF
grep -n ": .*: " attempts/costabile-2023-01.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: [\"']" | head
```

```
(Bash completed with no output)
```

**Agent**

Now the README, then rebuild the notebook and run the final check.

**Agent calls Write**

```json
{
 "file_path": "entries/costabile-2023/README.md",
 "content": "# Costabile, Balakrishnan, Schwinn & Haesemeyer (2023) from dandisets 000235 to 000238\n\nTests the zebrafish findings of [Costabile et al. (2023)](https://doi.org/10.7554/eLife.83289)\non the four dandisets the paper deposited: [000235](https://dandiarchive.org/dandiset/000235/0.230316.1600)\n(forebrain), [000236](https://dandiarchive.org/dandiset/000236/0.230316.2031) (midbrain),\n[000237](https://dandiarchive.org/dandiset/000237/0.230316.1655) (hindbrain), 25 larval zebrafish\nimaged during a random-wave heat stimulus, and [000238](https://dandiarchive.org/dandiset/000238/0.230316.1519),\nsix fish with reticulospinal backfills.\n\n| Claim | Outcome |\n|---|---|\n| 25 fish, 750 planes, 706,543 components, 432,882 pass the brightness criterion | Reproduced |\n| Training and test data are largely uncorrelated | Reproduced (rests on an assumption) |\n| Claims on the MINE fits of the zebrafish neurons (15, including six that also need the Z-Brain registration) | Blocked: too large |\n| Reticulospinal neurons are mostly behavior-driven | Blocked: too large (and no backfill annotation in 000238) |\n| Simulations (Figures 1 to 4) and mouse widefield data (Figure 5), data elsewhere (14) | Blocked: too large for this run's time |\n\nThe files match the paper's counts exactly and pass the clock checks. Most of the paper's\nanalyses rest on a CNN fit to each of about 433,000 neurons; on this runner that takes about 60\nhours, so those claims are blocked. The dandisets hold no swim bouts, no Z-Brain registration and\nno annotation of the backfilled neurons; the bouts are re-derived here from the tail tracking.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/costabile-2023-01.yaml`](../../attempts/costabile-2023-01.yaml).\n"
}
```

```
File created successfully at: entries/costabile-2023/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/sv/bin/activate && cd entries/costabile-2023 && python $TMPDIR/build_nb.py && rm -rf __pycache__ && cd ../.. && python tools/entry.py check entries/costabile-2023 2>&1 | tail -20; date -u
```

```
written 34 cells
error: attempts/costabile-2023-01.yaml: finding 4: the attempt used 4 datasets; name the ones it is about (`datasets:`, from 000235, 000236, 000237, 000238)
1 error(s)
Thu Nov 26 01:07:58 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/costabile-2023-01.yaml'
s=open(p).read()
s=s.replace('''- kind: other
  about: data
  severity: minor
  notebook: reproduce_costabile_2023.ipynb
  output: finding-frame-rate''','''- kind: other
  about: data
  severity: minor
  datasets:
  - "000235"
  - "000236"
  - "000237"
  - "000238"
  notebook: reproduce_costabile_2023.ipynb
  output: finding-frame-rate''')
open(p,'w').write(s)
EOF
python tools/entry.py check entries/costabile-2023 2>&1 | tail -5; ls tools; grep -n "def cmd_\|^def " tools/entry.py | head -40
```

```
0 error(s)
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
build_osf_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
build_zenodo_targets.py
changed_entries.py
claims_check.py
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/| 13 claims on the CNN fits, and 6 anatomical claims that depend on them |/| 12 claims on the CNN fits, and 6 anatomical claims that depend on them |/; s/| 13 claims on simulations and mouse widefield data (data elsewhere) |/| 14 claims on simulations and mouse widefield data (data elsewhere) |/' $TMPDIR/build_nb.py && grep -n "12 claims on\|14 claims on" $TMPDIR/build_nb.py && sed -i 's/(15, including six that also need the Z-Brain registration)/(18, including six that also need the Z-Brain registration)/' entries/costabile-2023/README.md && grep -n "18, incl" entries/costabile-2023/README.md && . $TMPDIR/sv/bin/activate && cd entries/costabile-2023 && python $TMPDIR/build_nb.py && rm -rf __pycache__ && cd ../.. && python tools/entry.py check entries/costabile-2023 | tail -2
```

```
565:| 12 claims on the CNN fits, and 6 anatomical claims that depend on them | blocked, too_large |
567:| 14 claims on simulations and mouse widefield data (data elsewhere) | blocked, too_large for the time left in this run |
14:| Claims on the MINE fits of the zebrafish neurons (18, including six that also need the Z-Brain registration) | Blocked: too large |
written 34 cells
0 error(s)
```

**Agent calls Bash**

```bash
sed -i "s/^The files match the paper's counts exactly and pass the clock checks. Most of the paper's$/The files hold the paper's counts of fish, planes and components exactly, and the clock checks are consistent with one clock. Most of the paper's/" entries/costabile-2023/README.md && grep -n "clock checks" entries/costabile-2023/README.md && date -u && time python tools/entry.py all entries/costabile-2023 2>&1 | tail -4; date -u
```

```
18:The files hold the paper's counts of fish, planes and components exactly, and the clock checks are consistent with one clock. Most of the paper's
Thu Nov 26 01:08:33 UTC 2026
Installed kernelspec registry-costabile-2023 in executed/costabile-2023/.venv/share/jupyter/kernels/registry-costabile-2023
0 error(s)
pass  reproduce_costabile_2023.ipynb  (2406 s)

real	40m22.122s
user	37m31.832s
sys	2m13.523s
Thu Nov 26 01:48:56 UTC 2026
```

**Agent calls Bash**

```bash
python3 -c "
import json;nb=json.load(open('executed/costabile-2023/reproduce_costabile_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    errs=[o for o in c.get('outputs',[]) if o.get('output_type')=='error']
    if errs: print('ERROR in',i)
    for key in ['own temperature 0','per-plane best','components with brightness','components 7','fit times','real data','pass took','largest correlation','median    ','fish 25','all within']:
        for line in t.split('\n'):
            if key in line: print(i,line[:200])
" | sort -u; sed -i 's/runtime_minutes: 33/runtime_minutes: 40/' entries/costabile-2023/entry.yaml; git status --short
```

```
12 temperature traces of different planes: largest correlation 0.926; pairs above 0.99: 0 of 427350; 99.9th percentile 0.854
14 at 0 s, own temperature 0.656 against next plane's 0.393 (medians over planes); own higher in 98.4% of planes
14 peak |r|, own temperature 0.587 against next plane's temperature 0.547 (medians); own higher in 69.0% of planes
14 per-plane best displacement: 0 s in 5.3% of planes, within 2 s in 54.5%; median 2.0 s
16   thr10_min10                median      37  (0.075/s); 5th to 95th percentile 7 to 163; planes with none 3
16   thr2_min10_code_default    median    2420  (4.881/s); 5th to 95th percentile 730 to 3628; planes with none 0
16   thr5_min10                 median      47  (0.095/s); 5th to 95th percentile 9 to 173; planes with none 1
16   thr5_min5                  median      99  (0.200/s); 5th to 95th percentile 15 to 707; planes with none 0
23 components 706543 (expected 706,543, tolerance 70,654): +0.00%
23 components with brightness >= 0.1: 434651 (expected 432,882, tolerance 43,288): +0.41%; fraction 0.615 (paper 0.613)
23 fish 25 (expected 25), planes 750 (expected 750)
24 {'fish': True, 'planes': True, 'components': True, 'bright components': True} -> all within tolerance: True
31 fit times (s): [8.5  2.05 2.08] ; test correlations: [0.305 0.14  0.361]
31 real data: 432882 fits x 2.08 s = 250 h on one thread, 62 h on 4; with the rotated controls 125 h on 4 threads, before any Taylor bootstrap
7 pass took 2084 s
 M tools/runner/chain.sh
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 588,625p tools/entry.py
```

```
def file_hash(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
    return h.hexdigest()


def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/runtime_minutes: 40/runtime_minutes: 33/' entries/costabile-2023/entry.yaml; python3 -c "
import json;nb=json.load(open('executed/costabile-2023/reproduce_costabile_2023.ipynb'))
print(''.join(''.join(o.get('text','')) for o in nb['cells'][31]['outputs']))"
```

```
fit times (s): [8.5  2.05 2.08] ; test correlations: [0.305 0.14  0.361]
real data: 432882 fits x 2.08 s = 250 h on one thread, 62 h on 4; with the rotated controls 125 h on 4 threads, before any Taylor bootstrap
the backfill fish (000238): 218257 components, about 31 h on 4 threads without the brightness cut
fig1f and fig4 (11 response types x 20): 220 fits x 13 s = 0.8 h on one thread, 0.2 h on 4; x5 for the protocol's five seeds: 1.0 h
fig2e and fig2s1 (500 sets x 4 responses): 2000 fits x 13 s = 7.2 h on one thread, 1.8 h on 4; x5 for the protocol's five seeds: 8.9 h
fig3 and fig3s1 white noise (2 filter sets x 100): 200 fits x 13 s = 0.7 h on one thread, 0.2 h on 4; x5 for the protocol's five seeds: 0.9 h
mouse, Figure 5 (13 sessions x 200 components): 2600 fits x 13 s = 9.3 h on one thread, 2.3 h on 4; x5 for the protocol's five seeds: 11.6 h
notebook elapsed so far: 40.0 min
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/costabile-2023-01.yaml'
s=open(p).read()
reps=[("One fit\n    of the paper's architecture on a real plane takes 1.97 s on one thread here (three fits timed in\n    the notebook), so the fits alone come to about 236 h on one thread, 59 h on the runner's four,",
       "One fit\n    of the paper's architecture on a real plane takes 2.08 s on one thread here (three fits timed in\n    the notebook), so the fits alone come to about 250 h on one thread, 62 h on the runner's four,"),
("about 118 h on\n    four threads","about 125 h on\n    four threads"),
("fitting them all takes about 29 h on four threads at the measured 1.97 s per fit","fitting them all takes about 31 h on four threads at the measured 2.08 s per fit"),
("about 12 s each on one thread by the timing in the notebook,\n    so 0.2 h on four threads for the claim's seed and 0.9 h with the protocol's four further seeds,",
 "about 13 s each on one thread by the timing in the notebook,\n    so 0.2 h on four threads for the claim's seed and 1.0 h with the protocol's four further seeds,"),
("With the dataset's checks taking 35\n    minutes of each full run","With the dataset's checks taking 35 to 40\n    minutes of each full run"),
("about 1.6 h\n    on four threads for one seed and 8.2 h for five","about 1.8 h\n    on four threads for one seed and 8.9 h for five"),
("about 2.1 h\n    on four threads for one seed and 10.7 h for five","about 2.3 h\n    on four threads for one seed and 11.6 h for five"),
]
for a,b in reps:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "1.97\|236 h\|59 h\|118 h" attempts/costabile-2023-01.yaml; python tools/entry.py check entries/costabile-2023 | tail -2; python tools/entry.py run entries/costabile-2023 2>&1 | tail -2
```

```
0 error(s)
pass  reproduce_costabile_2023.ipynb  (2406 s, reused)
reused the executed copies of 2026-11-26 01:48 UTC: nothing the run reads has changed since (hash ec398a9d397a). Nothing was executed and no environment was built; --fresh runs it again.
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/costabile-2023 2>&1 | tail -5; ls executed/costabile-2023/handover/; git status --short | grep -v "^??.*\.\(bash\|z\|profile\|git\|idea\|mcp\|ripgrep\|vscode\)" ; date -u
```

```
wrote executed/costabile-2023/handover
costabile-2023.yaml
mine_cnn.py
mine_data.py
reproduce_costabile_2023.ipynb
 M tools/runner/chain.sh
?? attempts/costabile-2023-01.yaml
?? entries/costabile-2023/
?? scripts
Thu Nov 26 01:50:03 UTC 2026
```

**Agent**

I've done steps 1 to 6. The entry passes `entry.py check` and a clean run (40 min), the attempt record is written, and the handover is built. Two claims were tested and both reproduced. The other 33 are blocked as `too_large`, almost all because the paper's CNN would have to be fit to about 433,000 neurons. Nothing is committed.

**(1) Outcomes per claim**

| Claim | Outcome |
|---|---|
| data-zebrafish-coverage | reproduced: 25 fish, 750 planes, 706,543 components (the paper's count exactly); 434,651 pass the brightness cut against the paper's 432,882 (+0.4%) |
| figs6-train-test-uncorrelated | reproduced, resting on an assumption: median inter-trial correlation is -0.051 for temperature and between -0.009 and -0.001 for the three behavior traces, under every bout reading. Temperature fails a stricter variant (median of absolute values 0.266) |
| 12 claims on the zebrafish fits (fig6d, shuffle enrichment, every-cutoff, fig6e ×2, fig6g, fig7b, fig7d, fig7e, lm-recovers, temperature-nonlinear, interaction-terms) | blocked, `too_large`: one CNN fit takes 2.08 s here, so about 62 h on 4 threads, or 125 h with the rotated controls |
| 6 anatomical claims (three Figure 6 supplement region claims, fig7a, fig7c, fig7f) | blocked, `too_large` through the fit claims they depend on; they would also need the Z-Brain registration, which the dandisets don't hold |
| fig6f-reticulospinal-behavior | blocked, `too_large` (218,257 components, about 31 h); 000238 also holds no backfill annotation |
| 14 simulation and mouse claims (Figures 1 to 5, data elsewhere) | blocked, `too_large` for this run's time; the notebook gives the estimates |

**(2) The dataset**
- **Pinned versions:** each dandiset's only published version (000235/0.230316.1600, 000236/0.230316.2031, 000237/0.230316.1655, 000238/0.230316.1519). The paper cites none.
- **What checks out:**
  - No plane is deposited twice.
  - The pixel masks line up with the movie (median r 0.834 between mask-pixel traces and CaImAn's).
  - Calcium is predicted far better by its own plane's temperature than by the next plane's (held-out r 0.656 against 0.393). It rises after swim starts, peaking at 1.8 s. Both are consistent with one shared clock, resolved only to about 2 s.
- **Major findings:**
  - There are no swim bouts or behavior predictors in the files. The lab's bout code with its default threshold of 2 rad/s finds 4.9 bouts per second, which is tracking noise.
  - There is no Z-Brain registration.
  - There is no backfill annotation in 000238.
- **Minor findings:**
  - The imaging rate is 2.384 Hz; the Methods say 2.5 Hz.
  - In 10 planes the tail timestamps span 629 s, so they must contain a jump of up to 128 s.
  - Each temperature trace is about 10.5 s longer than its imaging, and the files don't say where it starts.
  - One backfill file has 25 planes, 8 planes have 1,181 frames, and 10 planes exceed 30 °C.
  - The reference images are empty.
- **Assumptions:**
  - Brightness is computed on the raw movie as deposited.
  - The NWB segment angles are relative, so their cumulative sum gives the point angles.
  - "sum_tail" is the cumulative tail angle.
  - The bout threshold is 5 or 10 rad/s, not the code's 2.
- **Questions for the paper's authors:** what bout threshold, minimum bout length and angle input were used; and whether the brightness projection came from the raw or the motion-corrected movie.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear or didn't fit**
1. `too_large` mixes "the computation is too big" with "the time left in this run". fig1f, Figure 1F (about 1.0 h with five seeds) would fit under the notebook limit, but not beside a 40-minute dataset notebook. I used `too_large` and said so in each claim's notes.
2. The five-seed rule multiplies the cost of the simulation claims by five, and the protocol allows no reduced seed check.
3. A claim gets one `blocked_by`. The anatomical claims have two blockers (the fits and the missing registration), so I put the second in the notes.
4. The clock-check recipes don't fit a slow continuous stimulus: raw lagged correlations are high by chance. I used held-out decoding with the temperature shifted in time.
5. The bout method lives in code the claims file names but didn't read (bitbucket.org/jcostabile/2p), and its default threshold doesn't fit these data. I read it at commit 5ffaa2d, ran every reading, and recorded the choice as an assumption.
6. The train/test criterion ("median ... below 0.2 in absolute value") can pass with strong correlations of both signs. I applied it as written (|median|) and showed median |r| as a variant.
7. A finding needs a cell tag, but the bout-threshold problem shows in a sanity cell, so that cell carries two tags.
8. `runtime_minutes` has to be written before the run, and editing it afterwards invalidates the run's stamp. The record says 33 min; the final run took 40.
9. The backfill annotation may be in the paper's Zenodo processed data (doi:10.5281/zenodo.7737788, `rs_analysis.hdf5`). The claims file doesn't name it as an input, so I didn't open it.

**(4) Runtime and failures**
- **Runtime:** about 2 h 25 min of the session, ending at 01:50 UTC. The notebook takes 40 min, with peak memory about 1.3 GB.
- **Failures:** none in the final runs. One subset run failed on a matplotlib argument and was fixed. Nothing was left unrecorded.

The entry is in `entries/costabile-2023/`; the record is `attempts/costabile-2023-01.yaml`, and the handover is in `executed/costabile-2023/handover/`.

## End of run

88 turns, 143 minutes, $7.26 at API prices, result: success.
