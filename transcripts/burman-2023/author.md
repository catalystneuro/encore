# burman-2023 · author · run 42760152737

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper entries claims attempts | head -50
```

```
<persisted-output>
Output too large (39.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/756d8c6b-50b8-48bf-8dca-8b7dac3a2350/tool-results/btf0ta7nn.txt

Preview (first 2KB):
Tue Nov 10 05:13:40 UTC 2026
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/756d8c6b-50b8-48bf-8dca-8b7dac3a2350/tool-results/btf0ta7nn.txt"
}
```

```
1	Tue Nov 10 05:13:40 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 713 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/burman-2023.yaml; ls paper; ls attempts | grep burman; ls entries | grep burman; cat papers/datasets/burman-2023.yaml; ls questions | grep burman
```

```
<persisted-output>
Output too large (49.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/756d8c6b-50b8-48bf-8dca-8b7dac3a2350/tool-results/buzoy1prn.txt

Preview (first 2KB):
# Claims for Burman, Brodersen, Raimondo, Sen & Akerman (2023), Neuron 111, 3531-3540,
# "Active cortical networks promote shunting fast synaptic inhibition in vivo", on dandiset 000458.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The version of record (open access, CC BY), full text from Europe PMC (PMC11913778),
# in paper/10.1016-j.neuron.2023.08.005.txt: Summary, Introduction, Results, the legends of
# Figures 1 to 4, Discussion, STAR Methods with Tables 1 and 2, and Data and code availability.
# The supplement (Document S1, Figures S1 to S7 and their legends) is not in the text, and no PDF
# was supplied. No claim on the dandiset needs it except figs6-rate-regressed, whose method is
# only in the Figure S6 legend; that claim names readings. The claims on Figures S2 to S5 and S7
# rest on the main-text sentences that cite them, and their tests are not known here.
#
# Code read. (1) gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf, revision
# 43a13d89441b7f56e835e84fa5811d9567917daf, burman_et_al_2023_neuropixel_data_analysis.py: reads
# the 17 NWB sessions of DANDI:000458 (version 0.230317.0039, named in its docstring) and writes,
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/756d8c6b-50b8-48bf-8dca-8b7dac3a2350/tool-results/buzoy1prn.txt"
}
```

```
1	# Claims for Burman, Brodersen, Raimondo, Sen & Akerman (2023), Neuron 111, 3531-3540,
2	# "Active cortical networks promote shunting fast synaptic inhibition in vivo", on dandiset 000458.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
4	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
5	#
6	# Text read. The version of record (open access, CC BY), full text from Europe PMC (PMC11913778),
7	# in paper/10.1016-j.neuron.2023.08.005.txt: Summary, Introduction, Results, the legends of
8	# Figures 1 to 4, Discussion, STAR Methods with Tables 1 and 2, and Data and code availability.
9	# The supplement (Document S1, Figures S1 to S7 and their legends) is not in the text, and no PDF
10	# was supplied. No claim on the dandiset needs it except figs6-rate-regressed, whose method is
11	# only in the Figure S6 legend; that claim names readings. The claims on Figures S2 to S5 and S7
12	# rest on the main-text sentences that cite them, and their tests are not known here.
13	#
14	# Code read. (1) gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf, revision
15	# 43a13d89441b7f56e835e84fa5811d9567917daf, burman_et_al_2023_neuropixel_data_analysis.py: reads
16	# the 17 NWB sessions of DANDI:000458 (version 0.230317.0039, named in its docstring) and writes,
17	# per unit, evoked firing rate, peri-stimulus histogram entropy and synchrony for the awake and
18	# isoflurane epochs. It does not hold the exclusion step, the statistics or the plots.
19	# (2) gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f, revision
20	# f6a05661c10051560aa381e334099efd8521617b, burman_et_al_2023_neuronal_network_simulation.py: the
[... 883 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -400; cat docs/archives.md
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/756d8c6b-50b8-48bf-8dca-8b7dac3a2350/tool-results/b891cptsi.txt

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

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/756d8c6b-50b8-48bf-8dca-8b7dac3a2350/tool-results/b891cptsi.txt"
}
```

```
1	# Encore Science: the registry
2	
3	Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
4	
5	Agents, and people, try to reproduce the key findings of papers from the open
6	data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
7	here: the notebooks when it works, and the reason when it does not.
8	
9	- **For the archive:** evidence of whether each dandiset is complete and
10	  accurate enough to support the findings of its paper.
11	- **For analysts:** working notebooks to build new analyses on.
12	
13	Status: pilot. All eight pilot targets have been attempted and checked by an
14	independent agent.
15	
16	**Dashboard:** <https://encorescience.org/>
17	
18	## Reading the outcomes
19	
20	An outcome says what one attempt could recover from the data in a dandiset,
[... 671 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/fouke-2025/; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -250
```

```
total 132
drwxr-xr-x   2 runner runner  4096 Nov 10 05:09 .
drwxr-xr-x 249 runner runner 12288 Nov 10 05:09 ..
-rw-r--r--   1 runner runner  2144 Nov 10 05:09 README.md
-rw-r--r--   1 runner runner   907 Nov 10 05:09 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 10 05:09 omr.py
-rw-r--r--   1 runner runner 79403 Nov 10 05:09 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 10 05:09 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 10 05:09 requirements.lock.txt
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
[... 268 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 250,400p attempts/fouke-2025-01.yaml; cat entries/fouke-2025/README.md; python -c "import json;nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'));[print(c['cell_type'],c.get('metadata',{}).get('tags'),''.join(c['source'])[:300].replace('\n','|')) for c in nb['cells'][:8]]"
```

```
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
- kind: metadata_error
  statement: f0_vtheta is stated in radians/s but holds the heading change per frame in radians,
    and f0_vx and f0_vy are stated in pixels/s but are per frame. In most Danionella files the sum
    of f0_vtheta over a trial does not match the change of f0_theta (median ratios 0.09 to 0.89).
- kind: other
  statement: 18 of 25 zebrafish files and 1 of 12 Danionella files are sampled at 32 to 35 Hz,
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; grep -n -i "neuropixel\|entropy\|synchron\|brian\|simulat\|regress" paper/10.1016-j.neuron.2023.08.005.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/w; fold -s -w 200 paper/10.1016-j.neuron.2023.08.005.txt > $TMPDIR/w/paper.txt; wc -l $TMPDIR/w/paper.txt; grep -n -i "Pre-processing of Neuropixels\|Characterization of stimulus\|Statistical analyses\|Network model\|Shunting inhibition promotes\|Data and code" $TMPDIR/w/paper.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 116,145p $TMPDIR/w/paper.txt; echo ----; sed -n 215,235p $TMPDIR/w/paper.txt; echo ----; sed -n 265,290p $TMPDIR/w/paper.txt; sed -n 350,356p $TMPDIR/w/paper.txt
```

```
conductances. Also, the differences in synaptic E GABAAR could not be explained by the neurons’ intrinsic membrane properties ( Figure S4 ). Shunting inhibition promotes local network 
desynchronization and response flexibility The nature of synaptic inhibition affects how neurons integrate incoming excitatory input. 12 , 13 To explore the implications of the shunting synaptic E 
GABAAR observed in the awake state, we first analyzed a publicly available data set of high-density Neuropixels (NPXs) recordings from regular spiking neurons in mouse cortex. 29 , 30 These data 
allowed us to compare how the same population of neurons respond to a stimulus under awake and isoflurane-anesthetized conditions ( Figure 4 A). In the awake state, electrical stimuli delivered to 
cortex evoked spiking activity, with neurons exhibiting variability in terms of when they spiked relative to one another. In contrast, in the anesthetized state, the same stimuli evoked less overall 
activity, and spiking responses were more closely aligned to the spiking of other neurons ( Figure 4 B). To quantify this, we (1) determined the degree of neuronal synchrony, which relates the firing 
of a single neuron to the activity of the other neurons on a trial-by-trial basis, 31 , 32 and (2) computed the peri-stimulus histogram entropy, as a measure of the flexibility (or variability) of 
each neuron’s responses. 33 This revealed that in the awake state, stimulus-evoked synchrony was lower and entropy was higher ( Figures 4 C and 4D). As the mean firing rate was greater in the awake 
state, we also established that the differences in synchrony and entropy were still evident after regressing out the effect of firing rate ( Figure S6 ). Figure 4 Shunting inhibition promotes local 
network desynchronization and response flexibility (A) High-density Neuropixels (NPXs) recordings were used to compare spiking activity in the same cortical neurons under awake and anesthetized 
conditions. (B) Example raster 
[... 75 more lines not kept]
```

**Agent**

Read the protocol, claims and paper. Next: fetching the paper's two gists and the dataset listing.

**Agent calls Bash**

```bash
cd $TMPDIR/w; curl -sL -o ana.py https://gist.githubusercontent.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf/raw/43a13d89441b7f56e835e84fa5811d9567917daf/burman_et_al_2023_neuropixel_data_analysis.py; curl -sL -o sim.py https://gist.githubusercontent.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f/raw/f6a05661c10051560aa381e334099efd8521617b/burman_et_al_2023_neuronal_network_simulation.py; wc -l ana.py sim.py; cat ana.py
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat $TMPDIR/w/sim.py
```

```
#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Simulate a LIF neuronal network with variable EGABA and structured inputs.

Copyright (C) 2023 by Paul Brodersen.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version. This program is distributed in the
hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details. You
should have received a copy of the GNU General Public License along
with this program. If not, see <https://www.gnu.org/licenses/.

"""

import time
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w; curl -s https://api.dandiarchive.org/api/dandisets/000458/versions/ | python -m json.tool | grep -E '"version"|"status"|"modified"|"size"|"asset_count"'; curl -s "https://api.dandiarchive.org/api/dandisets/000458/versions/0.230317.0039/assets/?page_size=200" > assets.json; python -c "
import json;d=json.load(open('assets.json'));print(d['count'])
for a in d['results']: print(a['path'], round(a['size']/1e9,2), a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/w; python -c "import h5py, remfile, pynwb; print(h5py.__version__, pynwb.__version__)" 2>&1; which uv python; python --version; cat entries/fouke-2025/requirements.lock.txt | head -5
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, remfile, pynwb; print(h5py.__version__, pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Python 3.13.18
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
    # via bidsschematools
aiohappyeyeballs==2.7.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && uv venv -q -p 3.13 venv && . venv/bin/activate && uv pip install -q h5py remfile pynwb numpy scipy pandas brian2 scikit-learn statsmodels matplotlib 2>&1 | tail -3; python -c "import brian2, pynwb; print(brian2.__version__, pynwb.__version__)"
```

```
2.11.0 4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && . venv/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, sys, time
aid = sys.argv[1]
url = requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/", allow_redirects=True).url
t=time.time()
f = h5py.File(remfile.File(url), "r")
def show(name, obj):
    if isinstance(obj, h5py.Dataset):
        print("D", name, obj.shape, obj.dtype)
    else:
        print("G", name, dict(obj.attrs).get("neurodata_type"))
f.visititems(show)
print("time", time.time()-t)
EOF
python survey.py 8e6e4eec-c987-4dea-bf45-c59052bdbee0 > survey_546655.txt; wc -l survey_546655.txt; grep -v "processing/\|acquisition/.*probe" survey_546655.txt | head -150
```

```
128 survey_546655.txt
G acquisition None
G acquisition/ElectricalSeriesEEG ElectricalSeries
D acquisition/ElectricalSeriesEEG/data (17436416, 30) int16
D acquisition/ElectricalSeriesEEG/electrodes (30,) int32
D acquisition/ElectricalSeriesEEG/timestamps (17436416,) float64
G analysis None
D file_create_date (1,) object
G general None
G general/devices None
G general/devices/EEG array Device
G general/devices/probeB Device
G general/devices/probeC Device
D general/experiment_description () object
D general/experimenter (7,) object
G general/extracellular_ephys None
G general/extracellular_ephys/EEG array ElectrodeGroup
G general/extracellular_ephys/electrodes DynamicTable
D general/extracellular_ephys/electrodes/group (798,) object
D general/extracellular_ephys/electrodes/group_name (798,) object
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w; grep "processing/\|acquisition/" survey_546655.txt
```

```
G acquisition/ElectricalSeriesEEG ElectricalSeries
D acquisition/ElectricalSeriesEEG/data (17436416, 30) int16
D acquisition/ElectricalSeriesEEG/electrodes (30,) int32
D acquisition/ElectricalSeriesEEG/timestamps (17436416,) float64
G acquisition/LFPprobeB LFP
G acquisition/LFPprobeB/ElectricalSeriesprobeB ElectricalSeries
D acquisition/LFPprobeB/ElectricalSeriesprobeB/data (17436518, 384) int16
D acquisition/LFPprobeB/ElectricalSeriesprobeB/electrodes (384,) int32
D acquisition/LFPprobeB/ElectricalSeriesprobeB/timestamps (17436518,) float64
G acquisition/LFPprobeC LFP
G acquisition/LFPprobeC/ElectricalSeriesprobeC ElectricalSeries
D acquisition/LFPprobeC/ElectricalSeriesprobeC/data (17436511, 384) int16
D acquisition/LFPprobeC/ElectricalSeriesprobeC/electrodes (384,) int32
D acquisition/LFPprobeC/ElectricalSeriesprobeC/timestamps (17436511,) float64
G processing/behavior ProcessingModule
G processing/behavior/BehavioralTimeSeries BehavioralTimeSeries
G processing/behavior/BehavioralTimeSeries/running_speed TimeSeries
D processing/behavior/BehavioralTimeSeries/running_speed/data (701010,) float64
D processing/behavior/BehavioralTimeSeries/running_speed/starting_time () float64
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && . venv/bin/activate && cat > peek.py <<'EOF'
import h5py, remfile, requests, sys, time, numpy as np, pandas as pd
aid = sys.argv[1]
url = requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/", allow_redirects=True).url
t=time.time()
f = h5py.File(remfile.File(url), "r")
tr = f["intervals/trials"]
df = pd.DataFrame({k: tr[k][:] for k in tr.keys() if k not in ("id",)})
for c in df.columns:
    if df[c].dtype==object: df[c]=df[c].map(lambda x: x.decode() if isinstance(x,bytes) else x)
df["id"]=tr["id"][:]
print(df.head(10).to_string()); print(df.dtypes)
for c in ["behavioral_epoch","estim_current","estim_target_depth","estim_target_region","stimulus_description","stimulus_type","is_valid","is_running"]:
    print(c, df[c].value_counts().to_dict())
el = df[df.stimulus_type=="electrical"]
print("dur", (el.stop_time-el.start_time).describe())
print(pd.crosstab([el.behavioral_epoch, el.is_valid],[el.estim_target_region]))
u = f["units"]
ids = u["id"][:]; print("ids==rows", np.array_equal(ids, np.arange(len(ids))), ids[:10])
loc = np.array([x.decode() if isinstance(x,bytes) else x for x in u["location"][:]])
print(pd.Series(loc).value_counts().to_dict())
wd = u["waveform_duration"][:]; print("wd", np.percentile(wd,[0,25,50,75,100]), (wd==0.4).sum(), np.isclose(wd,0.4).sum())
print(np.unique(np.round(wd,4))[:30])
eg = [x.decode() if isinstance(x,bytes) else x for x in u["electrode_group"][:]]
print(eg[:3])
ep = f["intervals/epochs"]; print(ep["start_time"][:], ep["stop_time"][:], ep["tags"][:])
print({k: f["general"][k][()] for k in ["experiment_description","session_id","stimulus"] }, f["session_description"][()])
print({k: f["general/subject"][k][()] for k in f["general/subject"].keys()})
print("time", time.time()-t)
EOF
python peek.py 8e6e4eec-c987-4dea-bf45-c59052bdbee0
```

```
behavioral_epoch estim_current estim_target_depth estim_target_region  is_running  is_valid  start_time stimulus_description stimulus_type  stop_time  id
0            awake            70               deep                 MOs       False      True    82.58399             biphasic    electrical   82.58439   0
1            awake            50               deep                 MOs        True      True    86.48837             biphasic    electrical   86.48877   1
2            awake            50               deep                 MOs        True      True    90.16804             biphasic    electrical   90.16844   2
3            awake            50               deep                 MOs        True      True    94.63739             biphasic    electrical   94.63779   3
4            awake            50               deep                 MOs        True      True    98.54527             biphasic    electrical   98.54567   4
5            awake            70               deep                 MOs        True      True   102.89018             biphasic    electrical  102.89058   5
6            awake            70               deep                 MOs        True      True   107.00593             biphasic    electrical  107.00633   6
7            awake            90               deep                 MOs       False      True   110.88297             biphasic    electrical  110.88337   7
8            awake            50               deep                 MOs       False      True   115.26058             biphasic    electrical  115.26098   8
9            awake            70               deep                 MOs       False      True   119.54587             biphasic    electrical  119.54627   9
behavioral_epoch            str
estim_current               str
estim_target_depth          str
estim_target_region         str
is_running                 bool
is_valid                   bool
start_time              float64
stimulus_description        str
stimulus_type               st
[... 40 more lines not kept]
```

**Agent**

Dataset structure is clear (units + trials tables; ids equal row numbers in the first file). Now timing the network simulation, which may be the bottleneck.

**Agent calls Bash**

```bash
mkdir -p entries/burman-2023 && cat > entries/burman-2023/network.py <<'EOF'
"""The leaky integrate-and-fire network of Burman et al. (2023), Figures 4E to 4H and S7.

A transcription of the paper's simulation gist,
gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision
f6a05661c10051560aa381e334099efd8521617b (burman_et_al_2023_neuronal_network_simulation.py),
which the claims file names as the method of the model claims. Every parameter below is the
gist's, and matches the Methods ("Neuronal network simulations", Table 1): 800 excitatory and
200 inhibitory neurons, connection probability 10%, weights 0.1 nS and 1 nS, Vogels
inhibitory plasticity during a balancing set, E_GABA -60 mV then -80 mV in the excitatory
neurons, 100 input patterns of 1 ms pulses (M = 500 pA) every 25 ms, each repeated 100 times
per condition, and lognormal noise (M = 25 pA) changed every 10 ms.

Differences from the gist, none of which changes the model:

- The gist builds the stimulus as one array for the whole run (502,500 by 1,000 values,
  4 GB, copied again when given units), which does not fit the runner's memory with a second
  copy. The stimulus is periodic (the same 100 patterns in every 2,500 ms set), so here the
  TimedArray holds one set and is read at t modulo the set's length. The values each neuron
  receives at each time step are the same.
- Random seeds are fixed, one per run (protocol: fix every seed); the gist sets none. The
  paper does not give its seeds, so runs here are other draws of the same model.
- The gist's coo_matrix is converted to CSR before columns are taken, as the classifier needs
  an indexable matrix; the values are the same.
- The analysis returns the values the gist writes to its CSV (spike count, firing rate,
  entropy, synchrony per excitatory neuron, and the decoding accuracy) as arrays.
"""
import time

import brian2 as b2
import numpy as np
from scipy.sparse import coo_matrix
from scipy.stats import entropy as get_entropy
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

EGABA = (-60, -80)  # mV, shunting then hyperpolarizing (Methods; gist)


def peristimulus_histogram(spike_times, interval, bin_width):
    """The gist's histogram without KDE: bins of bin_width from interval[0]."""
    bins = np.arange(interval[0], interval[1] + bin_width, bin_width)
    indices = np.digitize(spike_times, bins) - 1
    interval_length = interval[1] - interval[0]
    counts = np.bincount(indices[indices >= 0], minlength=interval_length)
    return counts[:interval_length].astype(float)


def histogram_entropy(spike_times, interval, bin_width):
    """Entropy in nats of the normalized peri-stimulus histogram (scipy.stats.entropy)."""
    h = peristimulus_histogram(spike_times, interval, bin_width)
    return get_entropy(h / h.sum())


def simulate(seed, stimuli=100, repeats=100, verbose=False):
    """One run of the gist's network. Returns a dict per E_GABA value (-60, -80) with the
    per-neuron arrays of the 800 excitatory neurons and the decoding accuracy."""
    np.random.seed(seed)
    b2.seed(seed)
    b2.start_scope()
    b2.prefs.codegen.target = "cython"

    total_conditions = 2
    total_neurons = 1000
    total_stimuli = stimuli
    total_repeats = total_conditions * repeats
    total_condition_epochs = total_stimuli * repeats
    total_balancing_epochs = total_stimuli
    total_testing_epochs = total_stimuli * total_repeats
    epoch_duration = 25
    balancing_time = total_balancing_epochs * epoch_duration
    testing_time = total_testing_epochs * epoch_duration
    total_time = balancing_time + testing_time
    condition_duration = testing_time / total_conditions
    stimulus_set_duration = total_stimuli * epoch_duration

    stimulus_duration = 1
    stimulus_magnitude = 500
    total_subepochs = int(epoch_duration / stimulus_duration)
    base_stimuli = np.zeros((total_stimuli * total_subepochs, total_neurons))
    base_stimuli[::total_subepochs] = stimulus_magnitude * np.random.lognormal(
        size=(total_stimuli, total_neurons))
    # one stimulus set, read periodically (see the module docstring)
    I_stimulus_set = b2.TimedArray(-base_stimuli * b2.pA, dt=stimulus_duration * b2.ms)
    set_duration = stimulus_set_duration * b2.ms

    base_stimuli_labels = np.arange(total_stimuli)
    stimuli_labels = np.hstack([base_stimuli_labels] * (total_repeats + 1))

    noise_time_scale = 10.
    noise_magnitude = 25
    arr_noise = noise_magnitude * np.random.lognormal(
        size=(int(total_time / noise_time_scale), total_neurons))
    I_random = b2.TimedArray(-arr_noise * b2.pA, dt=noise_time_scale * b2.ms)

    n_exc, n_inh = int(4 * total_neurons / 5), int(total_neurons / 5)
    values = [np.mean(EGABA)] + repeats * [EGABA[0]] + repeats * [EGABA[1]]
    E_GABA_exc = b2.TimedArray(np.array(values) * b2.mV, dt=stimulus_set_duration * b2.ms)

    ns = dict(I_stimulus_set=I_stimulus_set, set_duration=set_duration, I_random=I_random,
              E_GABA_exc=E_GABA_exc,
              E_L_exc=-60. * b2.mV, V_th_exc=-50. * b2.mV, E_GABA_inh=-60. * b2.mV,
              E_L_inh=-60. * b2.mV, V_th_inh=-50. * b2.mV, C_m=200. * b2.pfarad,
              g_L=10. * b2.nsiemens, E_GLUT=0. * b2.mV, tau_GLUT=5. * b2.ms,
              tau_GABA=10. * b2.ms)
    t_ref = 5. * b2.ms

    exc_neuron_eqs = '''
    dv/dt      = -(I_L + I_GLUT + I_GABA + I_ext)/C_m  : volt (unless refractory)
    I_ext      =  I_stimulus_set(t % set_duration, i) + I_random(t, i) : amp
    I_L        =  g_L    * (v - E_L_exc)               : amp
    I_GLUT     =  g_GLUT * (v - E_GLUT)                : amp
    I_GABA     =  g_GABA * (v - E_GABA_exc(t))         : amp
    dg_GLUT/dt = -g_GLUT / tau_GLUT                    : siemens
    dg_GABA/dt = -g_GABA / tau_GABA                    : siemens
    '''
    inh_neuron_eqs = '''
    dv/dt      = -(I_L + I_GLUT + I_GABA + I_ext)/C_m  : volt (unless refractory)
    I_ext      =  I_stimulus_set(t % set_duration, i + 800) + I_random(t, i + 800) : amp
    I_L        =  g_L    * (v - E_L_inh)               : amp
    I_GLUT     =  g_GLUT * (v - E_GLUT)                : amp
    I_GABA     =  g_GABA * (v - E_GABA_inh)            : amp
    dg_GLUT/dt = -g_GLUT / tau_GLUT                    : siemens
    dg_GABA/dt = -g_GABA / tau_GABA                    : siemens
    '''
    exc = b2.NeuronGroup(n_exc, model=exc_neuron_eqs, threshold='v>V_th_exc',
                         reset='v=E_L_exc', refractory=t_ref, method='euler', namespace=ns)
    inh = b2.NeuronGroup(n_inh, model=inh_neuron_eqs, threshold='v>V_th_inh',
                         reset='v=E_L_inh', refractory=t_ref, method='euler', namespace=ns)
    exc.v = ns["E_L_exc"]
    inh.v = ns["E_L_inh"]

    syn_ns = dict(tau_stdp=20. * b2.ms, gmax=100. * b2.nsiemens,
                  beta=3. * b2.Hz * 20. * b2.ms * 2, eta=0.1)
    static_ex = dict(model='w : siemens', on_pre='g_GLUT_post += w')
    static_in = dict(model='w : siemens', on_pre='g_GABA_post += w')
    vogels = dict(model='''
        w : siemens
        dApre/dt  = -Apre  / tau_stdp : siemens (event-driven)
        dApost/dt = -Apost / tau_stdp : siemens (event-driven)
        ''',
        on_pre='''
        Apre += 1.*nsiemens
        w = clip(w + (Apost - beta * nsiemens) * eta, 0 * nsiemens, gmax)
        g_GABA_post += w''',
        on_post='''
        Apost += 1. * nsiemens
        w = clip(w + Apre * eta, 0 * nsiemens, gmax)
        ''')
    pop = {"exc": exc, "inh": inh}
    conns = {("exc", "exc"): (static_ex, 0.1, 0.1), ("exc", "inh"): (static_ex, 0.1, 0.1),
             ("inh", "inh"): (static_in, 0.1, 1.), ("inh", "exc"): (vogels, 0.1, 1.)}
    synapses = []
    for (a, b_), (model, p, w) in conns.items():
        s = b2.Synapses(pop[a], pop[b_], **model, namespace=syn_ns)
        s.connect(p=p)
        s.w = w * b2.nsiemens
        synapses.append(s)
    mon = b2.SpikeMonitor(exc)
    net = b2.Network(exc, inh, *synapses, mon)

    # the gist's loop runs the balancing set with eta = 0.1, then the test with eta = 0
    timing = []
    for sim_time, eta in zip((balancing_time, testing_time), (0.1, 0.)):
        syn_ns["eta"] = eta
        tic = time.time()
        net.run(sim_time * b2.ms, namespace={})
        timing.append(time.time() - tic)
    if verbose:
        print("run times", timing)

    out = {}
    all_t = np.asarray(mon.t / b2.ms)
    all_i = np.asarray(mon.i)
    for ctr, E_GABA in enumerate(EGABA):
        condition_start = balancing_time + ctr * condition_duration
        condition_stop = condition_start + condition_duration
        valid = (all_t >= condition_start) & (all_t < condition_stop)
        spike_indices = all_i[valid]
        spike_times = all_t[valid] - condition_start

        epoch_indices = (spike_times / epoch_duration).astype(int)
        X = coo_matrix((np.ones_like(spike_times), (epoch_indices, spike_indices)),
                       shape=(total_condition_epochs, n_exc)).tocsr()
        y = stimuli_labels[(total_balancing_epochs + ctr * total_condition_epochs):
                           (total_balancing_epochs + (ctr + 1) * total_condition_epochs)]
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
        accuracy = np.mean(cross_val_score(KNeighborsClassifier(), X[:, :50], y, cv=cv))

        is_valid = (spike_times >= 0) & (spike_times < stimulus_set_duration)
        spike_indices = spike_indices[is_valid]
        spike_times = spike_times[is_valid]
        epoch_indices = epoch_indices[is_valid]
        spike_times = spike_times % epoch_duration
        interval = (0, 12)
        is_valid = (spike_times >= interval[0]) & (spike_times < interval[1])
        spike_times = spike_times[is_valid]
        spike_indices = spike_indices[is_valid]
        epoch_indices = epoch_indices[is_valid]

        spike_counts = np.bincount(spike_indices, minlength=n_exc).astype(float)
        firing_rates = spike_counts / (total_stimuli * (interval[1] - interval[0]) / 1000)

        entropy = np.full(n_exc, np.nan)
        for neuron in np.unique(spike_indices):
            entropy[neuron] = histogram_entropy(spike_times[spike_indices == neuron], interval, 1)

        s_sum = np.zeros(n_exc)
        s_n = np.zeros(n_exc)
        for epoch in range(total_stimuli):
            m = epoch_indices == epoch
            if m.any():
                pr = peristimulus_histogram(spike_times[m], interval, 1)
                pr /= pr.sum()
                idx = (spike_times[m] - interval[0]).astype(int)
                np.add.at(s_sum, spike_indices[m], pr[idx])
                np.add.at(s_n, spike_indices[m], 1)
        synchrony = np.where(s_n > 0, s_sum / np.where(s_n > 0, s_n, 1), np.nan)

        out[E_GABA] = dict(spike_count=spike_counts, firing_rate=firing_rates,
                           entropy=entropy, synchrony=synchrony, accuracy=accuracy,
                           total_spikes=int(valid.sum()))
    out["run_seconds"] = sum(timing)
    return out
EOF
cd $TMPDIR/w && . venv/bin/activate && cd entries/burman-2023 && /usr/bin/time -v python -c "
import network, time
t=time.time(); r=network.simulate(1, repeats=5, verbose=True); print('total', time.time()-t)
for k in (-60,-80):
    d=r[k]; import numpy as np; print(k, d['accuracy'], np.nanmean(d['entropy']), np.nanmean(d['synchrony']), d['firing_rate'].mean(), d['total_spikes'])
" 2>&1 | grep -v "^\s*\(Page\|Volun\|Invol\|Swaps\|File\|Socket\|Signals\|Average\|Exit\|Minor\|Major\|Percent\|System time\|Command\)"
```

```
run times [40.84366059303284, 9.965667247772217]
total 86.30293488502502
-60 0.892 0.4677924912358496 0.7760306255119537 19.597916666666666 106536
-80 0.844 0.21147096712372743 0.8744110576067513 8.947916666666668 46768
import network, time
t=time.time(); r=network.simulate(1, repeats=5, verbose=True); print('total', time.time()-t)
for k in (-60,-80):
    d=r[k]; import numpy as np; print(k, d['accuracy'], np.nanmean(d['entropy']), np.nanmean(d['synchrony']), d['firing_rate'].mean(), d['total_spikes'])
"
	User time (seconds): 84.29
	Elapsed (wall clock) time (h:mm:ss or m:ss): 1:31.67
	Maximum resident set size (kbytes): 589992
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
s=open("network.py").read()
s=s.replace("I_stimulus_set(t % set_duration, i + 800) + I_random(t, i + 800) : amp","I_stimulus_set(t % set_duration, i) + I_random(t, i) : amp")
s=s.replace("""- The analysis returns""","""- As in the gist, the inhibitory neurons read columns 0 to 199 of the stimulus and noise
  arrays, the same columns as the first 200 excitatory neurons.
- The analysis returns""")
s=s.replace("""    timing = []
    for sim_time, eta in zip((balancing_time, testing_time), (0.1, 0.)):
        syn_ns["eta"] = eta
        tic = time.time()
        net.run(sim_time * b2.ms, namespace={})
        timing.append(time.time() - tic)""","""    timing, w_sums = [], []
    for sim_time, eta in zip((balancing_time, testing_time), (0.1, 0.)):
        syn_ns["eta"] = eta
        tic = time.time()
        net.run(sim_time * b2.ms, namespace={})
        timing.append(time.time() - tic)
        w_sums.append(float(np.sum(synapses[3].w / b2.nsiemens)))""")
s=s.replace("""    out["run_seconds"] = sum(timing)""","""    out["run_seconds"] = sum(timing)
    # summed inhibitory-to-excitatory weight (nS) at the start, after balancing and after the
    # test: plasticity acts only during balancing (gist: eta 0.1, then 0)
    out["w_sums"] = [float(len(synapses[3]) * 1.0)] + w_sums
    return out


def run(seed):
    \"\"\"One full run at the gist's defaults, for a process pool.\"\"\"
    return simulate(seed)""")
s=s.replace("""    out["w_sums"] = [float(len(synapses[3]) * 1.0)] + w_sums
    return out
    return out""","""    out["w_sums"] = [float(len(synapses[3]) * 1.0)] + w_sums
    return out""")
open("network.py","w").write(s)
EOF
grep -n "return out" network.py; cd $TMPDIR/w && . venv/bin/activate && cd - >/dev/null && cat > $TMPDIR/w/ptest.py <<'EOF'
import sys, time; sys.path.insert(0, ".")
from multiprocessing import Pool
from functools import partial
import network, numpy as np
t=time.time()
with Pool(4) as p:
    rs = p.map(partial(network.simulate, repeats=2), [1,2,3,4])
print("wall", time.time()-t)
for r in rs: print(r["run_seconds"], r["w_sums"], [ (round(r[k]['accuracy'],3), round(np.nanmean(r[k]['entropy']),3), round(np.nanmean(r[k]['synchrony']),3)) for k in (-60,-80)])
EOF
/usr/bin/time -f "%e s %M KB" python $TMPDIR/w/ptest.py
```

```
Exit code 1
229:    return out
235:    return out
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/claude-1001/brian_debug_wc_ijsqy.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/claude-1001/brian_script_ou6td8mr.py Thanks! [brian2]
multiprocessing.pool.RemoteTraceback: 
"""
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/multiprocessing/pool.py", line 125, in worker
    result = (True, func(*args, **kwds))
                    ~~~~^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/multiprocessing/pool.py", line 48, in mapstar
    return list(map(*args))
  File "entries/burman-2023/network.py", line 190, in simulate
    accuracy = np.mean(cross_val_score(KNeighborsClassifier(), X[:, :50], y, cv=cv))
                       ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/w/venv/lib/python3.13/site-packages/sklearn/utils/_param_validation.py", line 218, in wrapper
    return func(*args, **kwargs)
  File "/tmp/claude-1001/w/venv/lib/python3.13/site-packages/sklearn/model_selection/_validation.py", line 654, in cross_val_score
    cv_results = cross_validate(
        estimator=estimator,
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 220,240p network.py; sed -i 's/repeats=2/repeats=5/' $TMPDIR/w/ptest.py; . $TMPDIR/w/venv/bin/activate; /usr/bin/time -f "%e s %M KB" python $TMPDIR/w/ptest.py 2>&1 | tail -6
```

```
synchrony = np.where(s_n > 0, s_sum / np.where(s_n > 0, s_n, 1), np.nan)

        out[E_GABA] = dict(spike_count=spike_counts, firing_rate=firing_rates,
                           entropy=entropy, synchrony=synchrony, accuracy=accuracy,
                           total_spikes=int(valid.sum()))
    out["run_seconds"] = sum(timing)
    # summed inhibitory-to-excitatory weight (nS) at the start, after balancing and after the
    # test: plasticity acts only during balancing (gist: eta 0.1, then 0)
    out["w_sums"] = [float(len(synapses[3]) * 1.0)] + w_sums
    return out


def run(seed):
    """One full run at the gist's defaults, for a process pool."""
    return simulate(seed)
    return out
wall 26.11601448059082
24.1007661819458 [15889.0, 23943.90163337579, 23943.90163337579] [(np.float64(0.918), np.float64(0.469), np.float64(0.775)), (np.float64(0.842), np.float64(0.202), np.float64(0.879))]
25.03178834915161 [16025.0, 23849.32467691329, 23849.32467691329] [(np.float64(0.84), np.float64(0.452), np.float64(0.783)), (np.float64(0.772), np.float64(0.184), np.float64(0.888))]
24.25772261619568 [16055.0, 23857.37636425943, 23857.37636425943] [(np.float64(0.898), np.float64(0.456), np.float64(0.781)), (np.float64(0.792), np.float64(0.205), np.float64(0.877))]
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open("network.py").read()
s=s.replace('    return simulate(seed)\n    return out\n','    return simulate(seed)\n')
open("network.py","w").write(s)
EOF
tail -3 network.py; sed -i 's/repeats=5/repeats=20/' $TMPDIR/w/ptest.py; . $TMPDIR/w/venv/bin/activate; /usr/bin/time -f "%e s %M KB" python $TMPDIR/w/ptest.py 2>&1 | tail -6; date -u
```

```
def run(seed):
    """One full run at the gist's defaults, for a process pool."""
    return simulate(seed)
wall 84.66469073295593
81.79461407661438 [15840.0, 23906.855317057732, 23906.855317057732] [(np.float64(0.961), np.float64(0.478), np.float64(0.772)), (np.float64(0.928), np.float64(0.202), np.float64(0.879))]
83.13557982444763 [15908.0, 23624.144031206568, 23624.144031206568] [(np.float64(0.956), np.float64(0.441), np.float64(0.787)), (np.float64(0.876), np.float64(0.225), np.float64(0.866))]
82.81472301483154 [16111.0, 23972.6411978682, 23972.6411978682] [(np.float64(0.97), np.float64(0.459), np.float64(0.78)), (np.float64(0.882), np.float64(0.209), np.float64(0.875))]
82.25458860397339 [16052.0, 23846.44295031674, 23846.44295031674] [(np.float64(0.974), np.float64(0.44), np.float64(0.788)), (np.float64(0.932), np.float64(0.182), np.float64(0.89))]
87.15 s 622792 KB
Tue Nov 10 05:24:24 UTC 2026
```

**Agent calls Bash**

```bash
cat > npx.py <<'EOF'
"""Loading DANDI:000458 (Claar et al. 2023) and the per-unit measures of Burman et al. (2023),
Figure 4A to 4D and Figure S6.

Every method choice is the claims file's (claims/burman-2023.yaml, opening comment N1 to N8),
which takes it from the paper's Methods ("Pre-processing of Neuropixels dataset",
"Characterization of stimulus-evoked spiking responses") and the paper's analysis gist,
gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf at revision
43a13d89441b7f56e835e84fa5811d9567917daf (burman_et_al_2023_neuropixel_data_analysis.py):

- SESSIONS: the 17 recordings the gist lists (N1).
- Units (N2): waveform_duration >= 0.4 ms (Methods; the gist's > 0.4 is a variant). Area reading
  A1, the Methods: location "SSp-ll" or "SSp-tr" when SSp was stimulated, "MOs" when MOs was;
  reading A2, the gist: location[:3] among the session's estim_target_region values of its
  electrical trials.
- Trials (N3): stimulus_type "electrical", is_valid true, behavioral_epoch "awake" or
  "isoflurane", all currents and depths pooled, times from stop_time (gist).
- Window (N4): spikes 2 to 12 ms after the stimulus, 1 ms bins.
- Entropy (N5), synchrony (N6) and the evoked rate (N7, readings F1 and F2) as the gist computes
  them; see each function.

Data are streamed with remfile and h5py from the pinned version; spikes are reduced, as they
load, to those within 0 to 20 ms of an electrical trial's stop_time.
"""
import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET = "000458"
VERSION = "0.230317.0039"  # the version the analysis gist names
API = "https://api.dandiarchive.org/api"
INTERVAL = (2, 12)  # ms after the stimulus (Methods; gist)
KEEP = (0.0, 20.0)  # ms after stop_time kept on loading, wider than every window used

SESSIONS = [
    "sub-546655_ses-20201023", "sub-551397_ses-20210211", "sub-551399_ses-20210128",
    "sub-569062_ses-20210218", "sub-569064_ses-20210408", "sub-569068_ses-20210304",
    "sub-569069_ses-20210312", "sub-569072_ses-20210422", "sub-569073_ses-20210415",
    "sub-569073_ses-20210416", "sub-571619_ses-20210319", "sub-571620_ses-20210513",
    "sub-575102_ses-20210603", "sub-586466_ses-20210729", "sub-586468_ses-20210819",
    "sub-590479_ses-20210921", "sub-590480_ses-20211111",
]
CONDITIONS = ("awake", "isoflurane")


def assets():
    """All assets of the pinned version: path, size and asset id."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    rows = []
    while url:
        page = requests.get(url, timeout=60).json()
        rows += [dict(path=a["path"], size=a["size"], asset_id=a["asset_id"])
                 for a in page["results"]]
        url = page["next"]
    return pd.DataFrame(rows)


def version_metadata():
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/", timeout=60).json()


def open_asset(asset_id):
    url = requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True,
                        timeout=60).url
    return h5py.File(remfile.File(url), "r")


def _str(a):
    return np.array([x.decode() if isinstance(x, bytes) else x for x in a], dtype=object)


def read_table(group, skip=()):
    """A DynamicTable's 1-D columns as a DataFrame (ragged and 2-D columns left out)."""
    cols = {}
    for k in group.keys():
        d = group[k]
        if k in skip or not isinstance(d, h5py.Dataset) or d.ndim != 1:
            continue
        if k + "_index" in group or k.endswith("_index"):
            continue
        if len(d) != len(group["id"]):
            continue
        v = d[:]
        cols[k] = _str(v) if v.dtype.kind in "OS" else v
    return pd.DataFrame(cols)


def read_session(asset_id):
    """Trials, unit metadata and peri-stimulus spikes of one file.

    Returns a dict with `trials` (all trials), `units` (all units, with the electrode group
    name), `spikes` (per unit row: an array of (index into trials, time in ms after the
    trial's stop_time) for spikes within KEEP of an electrical trial), `n_spikes` (each unit's
    total spike count) and file metadata.
    """
    f = open_asset(asset_id)
    trials = read_table(f["intervals/trials"])
    u = f["units"]
    units = read_table(u, skip=("electrode_group",))
    units["electrode_group"] = [f[r].name.split("/")[-1] for r in u["electrode_group"][:]]
    index = u["spike_times_index"][:].astype(np.int64)
    starts = np.r_[0, index[:-1]]
    units["n_spikes"] = index - starts
    el = trials.index[trials.stimulus_type == "electrical"].to_numpy()
    stops = trials.loc[el, "stop_time"].to_numpy()
    order = np.argsort(stops)
    el, stops = el[order], stops[order]
    st = u["spike_times"]
    spikes = {}
    chunk = 2_000_000
    # read the flat spike_times in chunks, keeping only spikes near electrical trials
    n_total = int(index[-1]) if len(index) else 0
    unit_of = np.repeat(np.arange(len(index)), units["n_spikes"].to_numpy())
    kept_unit, kept_trial, kept_time = [], [], []
    sorted_ok = True
    for a in range(0, n_total, chunk):
        t = st[a:a + chunk] * 1000.0  # s -> ms
        k = np.searchsorted(stops * 1000.0, t - KEEP[1], side="left")
        k = np.clip(k, 0, len(stops) - 1)
        # candidate trial: the latest stop at or before t - KEEP[0]
        j = np.searchsorted(stops * 1000.0, t - KEEP[0], side="right") - 1
        ok = j >= 0
        rel = np.where(ok, t - stops[np.clip(j, 0, None)] * 1000.0, np.inf)
        m = ok & (rel >= KEEP[0]) & (rel < KEEP[1])
        kept_unit.append(unit_of[a:a + chunk][m])
        kept_trial.append(el[j[m]])
        kept_time.append(rel[m])
    ku = np.concatenate(kept_unit) if kept_unit else np.array([], int)
    kt = np.concatenate(kept_trial) if kept_trial else np.array([], int)
    kx = np.concatenate(kept_time) if kept_time else np.array([])
    for r in range(len(units)):
        m = ku == r
        spikes[r] = np.c_[kt[m], kx[m]]
    # spike times sorted within each unit (checked on a sample of units)
    for r in range(0, len(units), max(1, len(units) // 20)):
        s0, s1 = starts[r], index[r]
        if s1 - s0 > 1 and np.any(np.diff(st[s0:min(s1, s0 + 100000)]) < 0):
            sorted_ok = False
    gen = f["general"]
    meta = dict(
        subject_id=gen["subject/subject_id"][()].decode(),
        session_id=gen["session_id"][()].decode(),
        stimulus=gen["stimulus"][()].decode(),
        epochs=pd.DataFrame(dict(start=f["intervals/epochs/start_time"][:],
                                 stop=f["intervals/epochs/stop_time"][:],
                                 tags=_str(f["intervals/epochs/tags"][:]))),
        spike_times_sorted=sorted_ok,
        ids_are_rows=bool(np.array_equal(u["id"][:], np.arange(len(units)))),
    )
    f.close()
    return dict(trials=trials, units=units, spikes=spikes, meta=meta)


# ---------------------------------------------------------------- selection

def target_regions(trials):
    el = trials[trials.stimulus_type == "electrical"]
    return sorted(el.estim_target_region.unique())


def select_units(session, area="A1", wf="ge"):
    """Row indices of the regular spiking units of the stimulated area (N2)."""
    units = session["units"]
    regions = target_regions(session["trials"])
    if area == "A1":  # Methods
        allowed = set()
        for r in regions:
            if r.startswith("SSp"):
                allowed |= {"SSp-ll", "SSp-tr"}
            if r == "MOs":
                allowed |= {"MOs"}
        in_area = units.location.isin(allowed)
    elif area == "A2":  # gist
        in_area = units.location.map(lambda x: x[:3] in regions)
    else:
        raise ValueError(area)
    wd = units.waveform_duration
    rs = wd >= 0.4 if wf == "ge" else wd > 0.4
    return np.flatnonzero((in_area & rs).to_numpy())


def condition_trials(trials, condition):
    """Trial indices of valid electrical trials of one behavioral epoch (N3), in table order."""
    m = ((trials.stimulus_type == "electrical") & (trials.behavioral_epoch == condition)
         & trials.is_valid.astype(bool))
    return trials.index[m].to_numpy()


def peristimulus(session, rows, trial_idx, interval=INTERVAL, offset=0.0):
    """Spikes of the units `rows` within `interval` ms of the trials `trial_idx`, as arrays
    (unit row, trial position in trial_idx, time in ms after the stimulus). `offset` shifts
    the time origin from stop_time (offset = -0.4 would be start_time for a 0.4 ms pulse)."""
    pos = {t: k for k, t in enumerate(trial_idx)}
    us, ts, xs = [], [], []
    for r in rows:
        s = session["spikes"][r]
        if not len(s):
            continue
        t = s[:, 1] - offset
        m = np.isin(s[:, 0], trial_idx) & (t >= interval[0]) & (t < interval[1])
        us.append(np.full(m.sum(), r))
        ts.append(np.array([pos[int(x)] for x in s[m, 0]], dtype=int))
        xs.append(t[m])
    if not us:
        return np.array([], int), np.array([], int), np.array([])
    return np.concatenate(us), np.concatenate(ts), np.concatenate(xs)


# ---------------------------------------------------------------- measures

def histogram(times, interval=INTERVAL, bin_width=1):
    """The gist's peri-stimulus histogram: 1 ms bins from interval[0]."""
    bins = np.arange(interval[0], interval[1] + bin_width, bin_width)
    idx = np.digitize(times, bins) - 1
    n = interval[1] - interval[0]
    return np.bincount(idx[idx >= 0], minlength=n)[:n].astype(float)


def measures(session, rows, trial_idx, population=None, interval=INTERVAL, offset=0.0):
    """Per unit of `rows`: spike count, rate F1 (Methods: count / (trials x 10 ms)), rate F2
    (the gist's get_firing_rate: summed spike times in ms over (highest trial position with a
    population spike + 1) x 10 ms), entropy (N5; NaN with fewer than two spikes) and synchrony
    (N6; NaN with no spike). The synchrony population is `population` (default: `rows`), the
    gist's units of N2 before any exclusion."""
    population = rows if population is None else population
    allrows = np.union1d(rows, population)
    u, tr, x = peristimulus(session, allrows, trial_idx, interval, offset)
    in_pop = np.isin(u, population)
    n_trials = len(trial_idx)
    width_s = (interval[1] - interval[0]) / 1000
    pu, ptr = u[in_pop], tr[in_pop]
    gist_trials = int(ptr.max() + 1) if len(ptr) else 0
    out = []
    # population histogram per trial, normalized by the trial's total count (N6)
    pop_hist = {}
    for t in np.unique(ptr):
        h = histogram(x[in_pop][ptr == t], interval)
        pop_hist[t] = h / h.sum()
    for r in rows:
        m = u == r
        times, trs = x[m], tr[m]
        count = int(m.sum())
        f1 = count / (n_trials * width_s)
        f2 = (np.sum(times) / (gist_trials * width_s)) if gist_trials else np.nan
        if count > 1:
            h = histogram(times, interval)
            p = h / h.sum()
            p = p[p > 0]
            ent = float(-(p * np.log(p)).sum())
        else:
            ent = np.nan
        if count and r in population:
            vals = [pop_hist[t][int(tt - interval[0])] for t, tt in zip(trs, times)]
            syn = float(np.mean(vals))
        elif count:
            # a unit outside the population: its spikes are read against the population's
            # histogram where the population has spikes on that trial
            vals = [pop_hist[t][int(tt - interval[0])] for t, tt in zip(trs, times) if t in pop_hist]
            syn = float(np.mean(vals)) if vals else np.nan
        else:
            syn = np.nan
        out.append(dict(row=int(r), count=count, rate_F1=f1, rate_F2=f2, entropy=ent,
                        synchrony=syn))
    df = pd.DataFrame(out)
    df.attrs["n_trials"] = n_trials
    df.attrs["gist_trials"] = gist_trials
    return df


def unit_table(session, area="A1", wf="ge", population="selected", offset=0.0):
    """One row per selected unit with awake and isoflurane measures (suffixes _aw, _an).
    population: "selected" (the N2 units, the gist) or a callable giving rows to use."""
    rows = select_units(session, area, wf)
    res = {}
    for c, suffix in zip(CONDITIONS, ("_aw", "_an")):
        tr = condition_trials(session["trials"], c)
        pop = rows if population == "selected" else population(session, rows, c)
        m = measures(session, rows, tr, population=pop, offset=offset)
        res[suffix] = m.set_index("row").add_suffix(suffix)
        res[suffix + "_trials"] = len(tr)
        res[suffix + "_gist_trials"] = m.attrs["gist_trials"]
    df = res["_aw"].join(res["_an"]).reset_index()
    df["n_trials_aw"], df["n_trials_an"] = res["_aw_trials"], res["_an_trials"]
    df["gist_trials_aw"], df["gist_trials_an"] = res["_aw_gist_trials"], res["_an_gist_trials"]
    df["location"] = session["units"].location.to_numpy()[df.row] if len(df) else []
    return df


def excluded(df, rate="F1", low=0.1, high=200.0):
    """The Methods' exclusion (N7): evoked rate below 0.1 Hz or above 200 Hz in either
    condition."""
    a, b = df[f"rate_{rate}_aw"], df[f"rate_{rate}_an"]
    return (a < low) | (a > high) | (b < low) | (b > high)
EOF
cat > $TMPDIR/w/t1.py <<'EOF'
import sys, time, resource; sys.path.insert(0, ".")
import npx, numpy as np, pandas as pd
A = npx.assets(); A["session"] = A.path.str.split("/").str[1].str.replace("_behavior+ecephys.nwb", "")
aid = A.set_index("session").loc["sub-546655_ses-20201023", "asset_id"]
t = time.time(); s = npx.read_session(aid); print("load", time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, "GB")
print(s["meta"])
for area in ("A1","A2"):
    df = npx.unit_table(s, area)
    ex = npx.excluded(df,"F1"); ex2 = npx.excluded(df,"F2")
    print(area, len(df), ex.sum(), ex2.sum(), df[~ex][["synchrony_aw","synchrony_an","entropy_aw","entropy_an","rate_F1_aw","rate_F1_an"]].mean().round(3).to_dict())
EOF
. $TMPDIR/w/venv/bin/activate; python $TMPDIR/w/t1.py
```

```
load 3.029449939727783 0.317144 GB
{'subject_id': '546655', 'session_id': '20201023', 'stimulus': 'single pulse electrical stimuli targeted to MOs (deep layers)', 'epochs':          start         stop                   tags
0  2006.054146  2362.014146   isoflurane_induction
1  2362.024146  4523.784146  isoflurane_anesthesia, 'spike_times_sorted': True, 'ids_are_rows': True}
A1 18 5 5 {'synchrony_aw': 0.529, 'synchrony_an': 0.561, 'entropy_aw': 1.287, 'entropy_an': 0.698, 'rate_F1_aw': 12.149, 'rate_F1_an': 6.926}
A2 18 5 5 {'synchrony_aw': 0.529, 'synchrony_an': 0.561, 'entropy_aw': 1.287, 'entropy_an': 0.698, 'rate_F1_aw': 12.149, 'rate_F1_an': 6.926}
```

**Agent calls Bash**

```bash
cat > $TMPDIR/w/t2.py <<'EOF'
import sys, time, resource, pickle; sys.path.insert(0, ".")
import npx, numpy as np, pandas as pd
A = npx.assets(); A["session"] = A.path.str.split("/").str[1].str.replace("_behavior+ecephys.nwb", "")
S = {}
for _, a in A.iterrows():
    t = time.time()
    s = npx.read_session(a.asset_id)
    S[a.session] = s
    tr = s["trials"]; el = tr[tr.stimulus_type=="electrical"]
    print(a.session, a.session in npx.SESSIONS, round(time.time()-t,1), "s", len(s["units"]), "units", npx.target_regions(tr),
          el.groupby("behavioral_epoch").is_valid.sum().to_dict(), s["meta"]["ids_are_rows"], s["meta"]["spike_times_sorted"], flush=True)
print("maxrss GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
pickle.dump(S, open(sys.argv[1], "wb"))
EOF
. $TMPDIR/w/venv/bin/activate; python $TMPDIR/w/t2.py $TMPDIR/w/S.pkl; date -u
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/w/t2.py", line 7, in <module>
    s = npx.read_session(a.asset_id)
  File "entries/burman-2023/npx.py", line 99, in read_session
    u = f["units"]
        ~^^^^^^^^^
  File "/tmp/claude-1001/w/venv/lib/python3.13/site-packages/h5py/_hl/group.py", line 407, in __getitem__
    return self._get(name)
           ~~~~~~~~~^^^^^^
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "/tmp/claude-1001/w/venv/lib/python3.13/site-packages/h5py/_hl/group.py", line 421, in _get
    oid = h5o.open(self.id, self._e(name), lapl=lapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5o.pyx", line 255, in h5py.h5o.open
KeyError: "Unable to synchronously open object (object 'units' doesn't exist)"
Tue Nov 10 05:25:33 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open("npx.py").read()
s=s.replace("""    trials = read_table(f["intervals/trials"])
    u = f["units"]""","""    trials = read_table(f["intervals/trials"]) if "intervals/trials" in f else pd.DataFrame()
    if "units" not in f:
        gen = f["general"]
        meta = dict(subject_id=gen["subject/subject_id"][()].decode(),
                    session_id=gen["session_id"][()].decode(), has_units=False,
                    groups=sorted(f.keys()), acquisition=sorted(f["acquisition"].keys()))
        f.close()
        return dict(trials=trials, units=pd.DataFrame(), spikes={}, meta=meta)
    u = f["units"]""")
s=s.replace("""        k = np.searchsorted(stops * 1000.0, t - KEEP[1], side="left")
        k = np.clip(k, 0, len(stops) - 1)
""","")
s=s.replace("""        session_id=gen["session_id"][()].decode(),
        stimulus=""","""        session_id=gen["session_id"][()].decode(),
        has_units=True,
        stimulus=""")
open("npx.py","w").write(s)
EOF
sed -i 's/    tr = s\["trials"\]; el = /    if not s["meta"]["has_units"]: print(a.session, a.session in npx.SESSIONS, "no units", s["meta"], len(s["trials"]), list(s["trials"].columns)); continue\n    tr = s["trials"]; el = /' $TMPDIR/w/t2.py
. $TMPDIR/w/venv/bin/activate; python $TMPDIR/w/t2.py $TMPDIR/w/S.pkl; date -u
```

```
sub-543393_ses-20200820 False no units {'subject_id': '543393', 'session_id': '20200820', 'has_units': False, 'groups': ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'intervals', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'], 'acquisition': ['ElectricalSeriesEEG']} 900 ['behavioral_epoch', 'estim_current', 'estim_target_depth', 'estim_target_region', 'id', 'is_running', 'is_valid', 'start_time', 'stimulus_description', 'stimulus_type', 'stop_time']
sub-543394_ses-20200827 False no units {'subject_id': '543394', 'session_id': '20200827', 'has_units': False, 'groups': ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'intervals', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'], 'acquisition': ['ElectricalSeriesEEG']} 900 ['behavioral_epoch', 'estim_current', 'estim_target_depth', 'estim_target_region', 'id', 'is_running', 'is_valid', 'start_time', 'stimulus_description', 'stimulus_type', 'stop_time']
sub-521887_ses-20200730 False no units {'subject_id': '521887', 'session_id': '20200730', 'has_units': False, 'groups': ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'intervals', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'], 'acquisition': ['ElectricalSeriesEEG']} 800 ['behavioral_epoch', 'estim_current', 'estim_target_depth', 'estim_target_region', 'id', 'is_running', 'is_valid', 'start_time', 'stimulus_description', 'stimulus_type', 'stop_time']
sub-521885_ses-20200709 False no units {'subject_id': '521885', 'session_id': '20200709', 'has_units': False, 'groups': ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'intervals', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'], 'acquisition': ['El
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/w/t3.py <<'EOF'
import sys, pickle; sys.path.insert(0, ".")
import npx, numpy as np, pandas as pd
from scipy import stats
S = pickle.load(open(sys.argv[1], "rb"))
for s in npx.SESSIONS:
    u = S[s]["units"]; reg = npx.target_regions(S[s]["trials"])
    locs = u.location[u.location.str[:3].isin(reg)].value_counts().to_dict()
    print(s, reg, locs)
res = {}
for area in ("A1","A2"):
    for wf in ("ge","gt"):
        T = pd.concat([npx.unit_table(S[s], area, wf).assign(session=s) for s in npx.SESSIONS], ignore_index=True)
        res[(area,wf)] = T
        for rate in ("F1","F2"):
            ex = npx.excluded(T, rate); K = T[~ex]
            per = K.groupby("session").size().reindex(npx.SESSIONS, fill_value=0)
            r = dict(total=len(T), kept=len(K), excl=int(ex.sum()), sessions=int((per>0).sum()), mice=K.session.str[:10].nunique(), med=per[per>0].median(), mn=per[per>0].min(), mx=per.max())
            for m in ("synchrony","entropy"):
                a, b = K[m+"_aw"], K[m+"_an"]; ok = a.notna() & b.notna()
                t = stats.ttest_rel(a[ok], b[ok])
                r[m] = (round(a[ok].mean(),3), round(b[ok].mean(),3), int(ok.sum()), f"{t.pvalue:.1e}")
            r["rate"] = (round(K["rate_"+rate+"_aw"].mean(),2), round(K["rate_"+rate+"_an"].mean(),2))
            print(area, wf, rate, r)
pickle.dump(res, open(sys.argv[2], "wb"))
EOF
. $TMPDIR/w/venv/bin/activate; python $TMPDIR/w/t3.py $TMPDIR/w/S.pkl $TMPDIR/w/T.pkl
```

```
sub-546655_ses-20201023 ['MOs'] {'MOs': 18}
sub-551397_ses-20210211 ['MOs'] {'MOs': 89}
sub-551399_ses-20210128 ['MOs'] {'MOs': 99}
sub-569062_ses-20210218 ['MOs'] {'MOs': 132}
sub-569064_ses-20210408 ['MOs'] {'MOs': 29}
sub-569068_ses-20210304 ['MOs'] {'MOs': 62}
sub-569069_ses-20210312 ['MOs'] {'MOs': 32}
sub-569072_ses-20210422 ['SSp'] {'SSp-tr': 51, 'SSp-ll': 48}
sub-569073_ses-20210415 ['MOs'] {'MOs': 29}
sub-569073_ses-20210416 ['SSp'] {'SSp-ll': 11, 'SSp-tr': 2}
sub-571619_ses-20210319 ['MOs'] {'MOs': 103}
sub-571620_ses-20210513 ['SSp'] {'SSp-ll': 14}
sub-575102_ses-20210603 ['MOs'] {'MOs': 15}
sub-586466_ses-20210729 ['SSp'] {'SSp-tr': 27}
sub-586468_ses-20210819 ['SSp'] {'SSp-tr': 57}
sub-590479_ses-20210921 ['SSp'] {'SSp-tr': 105}
sub-590480_ses-20211111 ['SSp'] {'SSp-tr': 94}
A1 ge F1 {'total': 865, 'kept': 721, 'excl': 144, 'sessions': 17, 'mice': 16, 'med': np.float64(37.0), 'mn': np.int64(7), 'mx': np.int64(95), 'synchrony': (np.float64(0.319), np.float64(0.386), 721, '1.5e-32'), 'entropy': (np.float64(1.389), np.float64(1.15), 656, '3.3e-30'), 'rate': (np.float64(14.0), np.float64(7.59))}
A1 ge F2 {'total': 865, 'kept': 662, 'excl': 203, 'sessions': 17, 'mice': 16, 'med': np.float64(34.0), 'mn': np.int64(1), 'mx': np.int64(93), 'synchrony': (np.float64(0.325), np.float64(0.393), 662, '3.1e-29'), 'entropy': (np.float64(1.347), np.float64(1.111), 597, '2.8e-26'), 'rate': (np.float64(45.05), np.float64(24.29))}
A1 gt F1 {'total': 865, 'kept': 721, 'excl': 144, 'sessions': 17, 'mice': 16, 'med': np.float64(37.0), 'mn': np.int64(7), 'mx': np.int64(95), 'synchrony': (np.float64(0.319), np.float64(0.386), 721, '1.5e-32'), 'entropy': (np.float64(1.389), np.float64(1.15), 656, '3.3e-30'), 'rate': (np.float64(14.0), np.float64(7.59))}
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.github.com/repos/richardjburman/burman-et-al-2022---Awake-EGABAAR/git/trees/a404c3ec9e8ba6865500ec5e1138835df4398c08?recursive=1 | python -c "import json,sys; d=json.load(sys.stdin); [print(t['path'], t.get('size')) for t in d.get('tree',[])] or print(d)" | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  grep -n "def \|tag\|sanity\|claim:" tools/entry.py | head -80; ls schemas
```

```
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
70:    def __init__(self):
73:    def error(self, where, message: str) -> None:
78:def dataset_id(record: dict) -> str | None:
87:def dataset_ids(record: dict) -> list[str]:
92:def claims_paths() -> list[Path]:
98:def claims_target(data: dict) -> tuple:
103:def lookup(index: dict, attempt: dict):
112:def schema(name: str) -> Draft202012Validator:
123:def _parsed(text: str):
131:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
137:def load(report: Report, path: Path):
145:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
154:def _plain(value):
165:def code_of(notebook_path: Path) -> str:
172:def check(entry_dir: Path) -> Report:
229:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
230:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
342:            tag = outcome.get("output")
343:            if notebook in present and tag:
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,66p tools/entry.py; sed -n 172,372p tools/entry.py; sed -n 463,547p tools/entry.py
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
[... 330 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 548,640p tools/entry.py | grep -n "max\|timeout"; python -c "import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])"
```

```
8:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
9:    parser.add_argument("--max-minutes", type=float, default=60,
45:                              args.timeout, args.max_minutes)
55:    return run(entry_dir, output_dir, args.timeout, args.max_minutes)
{
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "One attempt at reproducing the claims of a target",
"description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
"type": "object",
"additionalProperties": false,
"required": [
"schema_version",
"id",
"datasets",
"paper",
"date",
"provenance",
"outcomes"
],
"properties": {
[... 275 more lines not kept]
```

**Agent**

Now writing the Neuropixels notebook.

**Agent calls Bash**

```bash
cat >> entries/burman-2023/npx.py <<'EOF'


# ---------------------------------------------------------------- readings and statistics

READINGS = {  # name: (area, waveform cut, rate) ; A1F1 is the claims file's main reading (N7)
    "A1F1": ("A1", "ge", "F1"), "A1F2": ("A1", "ge", "F2"), "A2F1": ("A2", "ge", "F1"),
    "A2F2": ("A2", "ge", "F2"), "A1F1 gist cut (> 0.4 ms)": ("A1", "gt", "F1"),
    "A2F2 gist cut (> 0.4 ms)": ("A2", "gt", "F2"),
}


def all_units(sessions, area="A1", wf="ge", population="selected", offset=0.0):
    """unit_table over every session, with a `session` and `subject` column."""
    parts = []
    for name, s in sessions.items():
        t = unit_table(s, area, wf, population, offset)
        t["session"] = name
        t["subject"] = name.split("_")[0]
        parts.append(t)
    return pd.concat(parts, ignore_index=True)


def paired(df, measure):
    """Mean and SEM per condition and the paired t test (scipy.stats.ttest_rel) over units with
    the measure defined in both conditions (N8)."""
    from scipy import stats
    a, b = df[measure + "_aw"], df[measure + "_an"]
    ok = a.notna() & b.notna()
    t = stats.ttest_rel(a[ok], b[ok])
    return dict(n=int(ok.sum()), awake=a[ok].mean(), awake_sem=a[ok].sem(),
                anesthetized=b[ok].mean(), anesthetized_sem=b[ok].sem(),
                t=float(t.statistic), p=float(t.pvalue), dropped=int((~ok).sum()))
EOF
cat > $TMPDIR/w/build_nb1.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
C = []
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip("\n")); 
    if tags: c.metadata["tags"] = tags
    C.append(c)
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)

md(r"""
# Reproducing Burman et al. (2023) on DANDI:000458: Neuropixels claims

**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)

**Dataset.** [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), version
0.230317.0039 (doi:10.48324/dandi.000458/0.230317.0039), the Allen Institute recordings of Claar et
al. (2023) that the paper reuses (Figure 4A to 4D, Figure S6). This is the only published version
of the dandiset, and the one the paper's analysis code names in its docstring
(gist a77bcf5e, revision 43a13d89), so it is pinned. The draft has the same 24 assets (checked below).

**Text the claims were written from.** The version of record (Europe PMC, PMC11913778), with STAR
Methods; the supplement (Figures S1 to S7) was not available (claims file, opening comment).

**What this notebook tests.** The claims on the dandiset. The network model claims are in
`network_model.ipynb`. The patch-clamp claims (Figures 1 to 3, S1 to S5) rest on recordings that
are not in the dandiset nor deposited anywhere ("available on request"), and are blocked.

| Claim | Here |
|---|---|
| dataset-sessions-link | tested |
| fig4c-sample | tested |
| fig4d-synchrony-lower-awake | tested |
| fig4d-entropy-higher-awake | tested |
| fig4-rate-higher-awake | tested |
| figs6-rate-regressed | tested (regression readings R1 to R3) |
| fig4f-model-hyperpolarizing-less-activity, fig4h-model-synchrony, fig4h-model-entropy, figs7-model-decoding | tested in `network_model.ipynb` |
| figs4-intrinsic-properties | blocked: methods_underspecified |
| 24 patch-clamp claims (fig1b to fig3j, rm-*, figs2, figs3, figs5) | blocked: data_missing |

Every method is the claims file's (opening comment N1 to N8); where it lacks a detail, the passage
of the paper used is cited in the cell or in `npx.py`.
""")
code(r"""
import time, resource
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats
import npx

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
T0 = time.time()
""")
md("## Data check\n\nThe archive's listing and metadata first, then every file the paper's code reads.")
code(r"""
assets = npx.assets()
assets["session"] = assets.path.str.split("/").str[1].str.replace("_behavior+ecephys.nwb", "", regex=False)
meta = npx.version_metadata()
print("version", meta["version"], "| name:", meta["name"])
print("related resources:", [r.get("identifier") or r.get("url") for r in meta.get("relatedResource", [])])
print("assets:", len(assets), "| total size %.1f GB" % (assets["size"].sum() / 1e9))
import requests
draft = requests.get(f"{npx.API}/dandisets/{npx.DANDISET}/versions/draft/assets/?page_size=200", timeout=60).json()["results"]
same = sorted((a["path"], a["size"]) for a in draft) == sorted(zip(assets.path, assets["size"]))
print("draft assets identical in path and size to", npx.VERSION, ":", same)
print("the 17 sessions the gist reads are all assets:", set(npx.SESSIONS) <= set(assets.session))
print("assets not read by the paper's code:", sorted(set(assets.session) - set(npx.SESSIONS)))
""", tags=["sanity"])
code(r"""
t = time.time()
S_all = {}
for _, a in assets.sort_values("session").iterrows():
    S_all[a.session] = npx.read_session(a.asset_id)
S = {k: S_all[k] for k in npx.SESSIONS}
print(f"loaded {len(S_all)} files in {time.time() - t:.0f} s; peak memory "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
rows = []
for k, s in S_all.items():
    m = s["meta"]
    if not m["has_units"]:
        rows.append(dict(session=k, in_gist=k in npx.SESSIONS, units=0, note="no units table; acquisition " + ",".join(m["acquisition"])))
        continue
    tr, u = s["trials"], s["units"]
    el = tr[tr.stimulus_type == "electrical"]
    rows.append(dict(
        session=k, in_gist=k in npx.SESSIONS, units=len(u), target=",".join(npx.target_regions(tr)),
        depth=",".join(sorted(el.estim_target_depth.unique())),
        aw_valid=int((el.is_valid & (el.behavioral_epoch == "awake")).sum()),
        iso_valid=int((el.is_valid & (el.behavioral_epoch == "isoflurane")).sum()),
        invalid=int((~el.is_valid.astype(bool)).sum()),
        currents=",".join(sorted(el.estim_current.unique(), key=lambda x: float(x))),
        pulse_ms="%.2f-%.2f" % ((el.stop_time - el.start_time).min() * 1e3, (el.stop_time - el.start_time).max() * 1e3),
        ids_are_rows=m["ids_are_rows"], sorted=m["spike_times_sorted"]))
info = pd.DataFrame(rows)
print(info.to_string())
print("\nsubjects among the 17:", len({k.split('_')[0] for k in npx.SESSIONS}))
""", tags=["sanity"])
md(r"""
The paper's 17 recordings in 16 mice are the 17 files the gist lists (sub-569073 has two sessions,
one stimulating MOs and one SSp). Seven other files are in the version: six hold only EEG and no
units, and one, sub-599017, has units and SSp stimulation but is not in the gist's list; the paper
does not say why it was left out. Each electrical trial lasts 0.4 ms (a biphasic pulse), so
`stop_time` is the pulse's end and `start_time` its onset.
""")
code(r"""
# Units, variables and ranges used. waveform_duration is described in the Allen data as ms.
U = pd.concat([s["units"].assign(session=k) for k, s in S.items()], ignore_index=True)
print("units in the 17 files:", len(U))
print("waveform_duration range %.3f to %.3f (ms); values exactly 0.4: %d; between 0.399 and 0.401: %d"
      % (U.waveform_duration.min(), U.waveform_duration.max(), (U.waveform_duration == 0.4).sum(),
         U.waveform_duration.between(0.399, 0.401).sum()))
print("distinct waveform_duration steps near 0.4:", np.unique(np.round(U.waveform_duration[U.waveform_duration.between(0.35, 0.45)], 4)))
print("unit locations in stimulated areas (first three characters among estim_target_region):")
for k, s in S.items():
    u = s["units"]; reg = npx.target_regions(s["trials"])
    print("  ", k, reg, u.location[u.location.str[:3].isin(reg)].value_counts().to_dict())
# spike and trial clocks: ranges in seconds
for k, s in list(S.items())[:17]:
    tr = s["trials"]; ep = s["meta"]["epochs"]
    iso = tr[(tr.behavioral_epoch == "isoflurane") & (tr.stimulus_type == "electrical")]
    an = ep[ep.tags.str.contains("anesthesia")]
    inside = ((iso.start_time.values[:, None] >= an.start.values) & (iso.start_time.values[:, None] < an.stop.values)).any(1).mean()
    print(f"{k}: trials {tr.start_time.min():.0f} to {tr.stop_time.max():.0f} s; isoflurane trials inside the "
          f"isoflurane_anesthesia epoch: {inside:.0%}; epochs {list(ep.tags)}")
""", tags=["sanity"])
md(r"""
The isoflurane trials fall inside the file's `isoflurane_anesthesia` epoch, which supports the
`behavioral_epoch` labels. Unit ids equal row numbers in all 17 files, so the gist's keying of
units by row index and lookup by id (claims file, checks, last point) select the same units here.
No unit has a waveform duration of exactly 0.4 ms (the values come in steps of about 0.0137 ms,
0.398 and 0.412 on either side), so the Methods' cut (>= 0.4) and the gist's (> 0.4) select the
same units.

**Clock check.** If the spike times share the trials' clock, spiking 2 to 12 ms after each pulse
should exceed spiking in the same window at times shifted away from the pulses, and differ between
awake and isoflurane trials.
""")
code(r"""
# Population spike count per trial in 2-12 ms after stop_time, against the same window placed
# 1.5 s after each pulse (inter-pulse intervals are 3.5 to 4.5 s), from the full spike trains of
# the selected units (reading A1, first file read again for the shifted windows).
clock = []
for k, s in S.items():
    rows_ = npx.select_units(s, "A1", "ge")
    for c in npx.CONDITIONS:
        tr = npx.condition_trials(s["trials"], c)
        u, t_, x = npx.peristimulus(s, rows_, tr)
        clock.append(dict(session=k, condition=c, trials=len(tr), units=len(rows_),
                          spikes_per_trial_true=len(x) / len(tr)))
clock = pd.DataFrame(clock)
# shifted windows need spikes away from the pulses, which read_session does not keep: read them
# for the units selected, from two files
shift = []
for k in npx.SESSIONS[:2]:
    aid = assets.set_index("session").loc[k, "asset_id"]
    f = npx.open_asset(aid)
    s = S[k]; rows_ = npx.select_units(s, "A1", "ge")
    idx = f["units/spike_times_index"][:]
    st0 = np.r_[0, idx[:-1]]
    for c in npx.CONDITIONS:
        tr = npx.condition_trials(s["trials"], c)
        stops = s["trials"].stop_time.to_numpy()[tr]
        for lag in (0.0, 1.5, -1.5):
            n = 0
            for r in rows_:
                sp = f["units/spike_times"][st0[r]:idx[r]]
                a = np.searchsorted(sp, stops + lag + 0.002); b = np.searchsorted(sp, stops + lag + 0.012)
                n += int((b - a).sum())
            shift.append(dict(session=k, condition=c, lag_s=lag, spikes_per_trial=n / len(tr)))
    f.close()
print(clock.pivot(index="session", columns="condition", values="spikes_per_trial_true").round(2).to_string())
print()
print(pd.DataFrame(shift).pivot_table(index=["session", "condition"], columns="lag_s", values="spikes_per_trial").round(2).to_string())
""", tags=["sanity"])
md(r"""
In both files read at full length, the 2 to 12 ms window after the pulse holds several times the
spikes of the same window 1.5 s before or after it, in both conditions, and the counts differ
between conditions. This is consistent with spikes and trials sharing one clock; it is shown on
two of the 17 files, and the evoked counts of the others (table above) are consistent with it.

**Duplicates.** sub-569073 has two files; they are distinct recordings if their trials and spike
counts differ.
""")
code(r"""
sig = []
for k, s in S.items():
    sig.append(dict(session=k, units=len(s["units"]), spikes=int(s["units"].n_spikes.sum()),
                    first_trial=round(float(s["trials"].start_time.iloc[0]), 5), trials=len(s["trials"])))
sig = pd.DataFrame(sig)
print(sig.to_string())
print("duplicate (units, spikes) pairs:", int(sig.duplicated(["units", "spikes"]).sum()),
      "| duplicate first-trial times:", int(sig.duplicated(["first_trial"]).sum()))
""", tags=["sanity"])
md("No two files share unit and spike counts or trial times, so each recording is counted once. "
   "The same unit in the awake and isoflurane epochs is the same row of one file's units table, "
   "sorted over the whole session, so no matching across sessions is needed.")

md(r"""
## dataset-sessions-link

> The 17 sessions the paper's analysis code reads are in DANDI:000458 and carry the fields the
> code uses.
""")
code(r"""
need_units = {"spike_times", "location", "waveform_duration"}
need_trials = {"stimulus_type", "behavioral_epoch", "is_valid", "estim_target_region", "stop_time"}
link = []
for k in npx.SESSIONS:
    s = S[k]
    el = s["trials"][s["trials"].stimulus_type == "electrical"]
    link.append(dict(session=k, file=k in set(assets.session),
                     units_fields=need_units <= set(s["units"].columns) | {"spike_times"},
                     trials_fields=need_trials <= set(s["trials"].columns),
                     awake=(el.behavioral_epoch == "awake").any(),
                     isoflurane=(el.behavioral_epoch == "isoflurane").any()))
link = pd.DataFrame(link)
print(link.to_string())
print("all 17 present with every field and both epochs:", bool(link.drop(columns="session").all().all()))
""", tags=["claim:dataset-sessions-link"])
md("**Result: reproduced.** All 17 files are in version 0.230317.0039, each with the units fields "
   "(spike_times read through its index, location, waveform_duration) and the trial fields the "
   "code uses, and with awake and isoflurane electrical trials.")

md(r"""
## fig4c-sample

> After excluding 203 neurons with evoked rates below 0.1 Hz or above 200 Hz, 662 regular spiking
> neurons remain, from 17 recordings in 16 mice, a median of 34 per recording (1 to 93).

Judged under the Methods reading A1F1 (the spike count rate); A1F2, A2F1, A2F2 and the gist's
waveform cut are variants (claims file, N7).
""")
code(r"""
tables, kept = {}, {}
for name, (area, wf, rate) in npx.READINGS.items():
    T = npx.all_units(S, area, wf)
    ex = npx.excluded(T, rate)
    tables[name], kept[name] = T, T[~ex].copy()
rows = []
for name, (area, wf, rate) in npx.READINGS.items():
    T, K = tables[name], kept[name]
    per = K.groupby("session").size().reindex(npx.SESSIONS, fill_value=0)
    low = ((T[f"rate_{rate}_aw"] < 0.1) | (T[f"rate_{rate}_an"] < 0.1)).sum()
    high = ((T[f"rate_{rate}_aw"] > 200) | (T[f"rate_{rate}_an"] > 200)).sum()
    rows.append(dict(reading=name, selected=len(T), kept=len(K), excluded=len(T) - len(K),
                     below_0_1Hz=int(low), above_200Hz=int(high), recordings=int((per > 0).sum()),
                     mice=K.subject.nunique(), median=float(per[per > 0].median()),
                     min=int(per[per > 0].min()), max=int(per.max())))
sample = pd.DataFrame(rows).set_index("reading")
print(sample.to_string())
print("\nexpected: kept 662 +- 66.2, excluded 203 +- 20.3, recordings 17, mice 16, median 34 +- 3.4, min 1 +- 0.1, max 93 +- 9.3")
per = pd.DataFrame({n: kept[n].groupby("session").size().reindex(npx.SESSIONS, fill_value=0) for n in ("A1F1", "A1F2")})
per["selected"] = tables["A1F1"].groupby("session").size().reindex(npx.SESSIONS, fill_value=0)
print("\nper recording:\n" + per.to_string())
""", tags=["claim:fig4c-sample"])
code(r"""
# What the F2 rate is: the gist sums spike times (in ms after the stimulus) where a count is
# expected, so F2 is about the mean spike latency (ms) times F1. Its 200 Hz bound is then a bound
# near 200 / 7 Hz on the spike-count rate.
T = tables["A1F1"]
ratio = (T.rate_F2_aw / T.rate_F1_aw).replace([np.inf], np.nan)
print("F2 / F1 (awake), median %.2f, 5th to 95th percentile %.2f to %.2f" % (ratio.median(), *ratio.quantile([.05, .95])))
K2 = kept["A1F2"]
print("F1 rate of the units F2 keeps: awake max %.1f Hz, isoflurane max %.1f Hz" % (K2.rate_F1_aw.max(), K2.rate_F1_an.max()))
ex_only_F2 = npx.excluded(T, "F2") & ~npx.excluded(T, "F1")
print("excluded under F2 but not F1:", int(ex_only_F2.sum()), "| under F1 but not F2:", int((npx.excluded(T, "F1") & ~npx.excluded(T, "F2")).sum()))
""", tags=["claim:fig4c-sample"])
md(r"""
**Result: partially reproduced.** Under the Methods reading A1F1, 865 units are selected, the
paper's total (662 + 203), and 721 are kept and 144 excluded: the kept count is within tolerance of
662 but the excluded count is outside 203 +- 20.3. Recordings (17) and mice (16) match; the median
per recording is 37 (range 7 to 95). Under the gist's rate (A1F2, and A2F2, which selects the same
units here), every number matches exactly: 662 kept, 203 excluded, median 34, range 1 to 93. The
gist's rate sums spike latencies, so its 200 Hz bound acts on the spike-count rate near 30 Hz; the
paper's exclusion was made with this rate.
""")

md(r"""
## fig4d-synchrony-lower-awake

> Neurons show lower stimulus-evoked synchrony with the population awake than under isoflurane
> (0.325 against 0.393).
""")
code(r"""
def stat_table(measure, readings=npx.READINGS):
    out = []
    for name in readings:
        r = npx.paired(kept[name], measure)
        out.append(dict(reading=name, **{k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()}))
    return pd.DataFrame(out).set_index("reading")
syn = stat_table("synchrony")
print(syn.to_string())
print("\nexpected awake 0.325 +- 0.005 (0.320 to 0.330), isoflurane 0.393 +- 0.007 (0.386 to 0.400)")
r = npx.paired(kept["A1F1"], "synchrony")
print("A1F1 unrounded: awake %.5f, isoflurane %.5f, p = %.2e" % (r["awake"], r["anesthetized"], r["p"]))
""", tags=["claim:fig4d-synchrony-lower-awake"])
code(r"""
# Variants: (a) the synchrony population restricted to the kept units (claims file, N6);
# (b) times from start_time, the pulse onset (the Methods say only "following an electrical
# stimulus"; the gist uses stop_time), for A1F1.
def kept_population(reading):
    area, wf, rate = npx.READINGS[reading]
    keep = {(r.session, r.row) for r in kept[reading].itertuples()}
    def pop(session, rows, c, _name=[None]):
        name = [k for k, v in S.items() if v is session][0]
        return np.array([r for r in rows if (name, r) in keep], dtype=int)
    return pop
var = []
for name in ("A1F1", "A1F2"):
    area, wf, rate = npx.READINGS[name]
    T = npx.all_units(S, area, wf, population=kept_population(name))
    K = T.merge(kept[name][["session", "row"]], on=["session", "row"])
    var.append(dict(variant=f"{name}, population = kept units", **npx.paired(K, "synchrony")))
Tst = npx.all_units(S, "A1", "ge", offset=-0.4)
Kst = Tst[~npx.excluded(Tst, "F1")]
var.append(dict(variant="A1F1, times from start_time", **npx.paired(Kst, "synchrony")))
var.append(dict(variant="A1F1, times from start_time, kept n", n=len(Kst)))
print(pd.DataFrame(var).round(4).to_string())
""", tags=["claim:fig4d-synchrony-lower-awake"])
code(r"""
# By recording (A1F1), and the range of the plotted values
K = kept["A1F1"]
by = K.groupby("session").apply(lambda d: pd.Series(dict(n=len(d), awake=d.synchrony_aw.mean(),
        isoflurane=d.synchrony_an.mean(), lower_awake=(d.synchrony_aw < d.synchrony_an).mean())), include_groups=False)
print(by.round(3).to_string())
print("recordings with awake mean lower: %d of %d" % ((by.awake < by.isoflurane).sum(), len(by)))
print("units with awake lower: %d of %d" % ((K.synchrony_aw < K.synchrony_an).sum(), len(K)))
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
for ax, m, lab in zip(axes, ("synchrony", "entropy"), ("Synchrony", "Entropy (nats)")):
    ax.scatter(K[m + "_an"], K[m + "_aw"], s=4)
    lim = [np.nanmin(K[[m + "_an", m + "_aw"]].values), np.nanmax(K[[m + "_an", m + "_aw"]].values)]
    ax.plot(lim, lim, "k--", lw=1); ax.set_xlabel(lab + ", isoflurane"); ax.set_ylabel(lab + ", awake")
    print(f"{m} plotted range: {lim[0]:.3f} to {lim[1]:.3f}; all points inside the axes")
fig.suptitle("A1F1 kept units"); fig.tight_layout(); plt.show()
""", tags=["claim:fig4d-synchrony-lower-awake"])
md(r"""
**Result: partially reproduced.** Under A1F1 (721 units) synchrony is lower awake, 0.319 against
0.386 (paired t test p = 1.5e-32), in the paper's direction and at its significance, but the awake
mean is just outside 0.325 +- 0.005 (the isoflurane mean is at the lower edge of its tolerance,
see the unrounded values). Under the gist's rate (A1F2, A2F2) the means are 0.325 and 0.393, the
paper's values. Restricting the population to kept units, or timing from pulse onset, keeps the
direction (variant table).
""")

md(r"""
## fig4d-entropy-higher-awake

> Peri-stimulus histogram entropy is higher awake than under isoflurane (1.347 against 1.111
> nats), so responses are more variable in time.
""")
code(r"""
ent = stat_table("entropy")
print(ent.to_string())
print("\nexpected awake 1.347 +- 0.018 (1.329 to 1.365), isoflurane 1.111 +- 0.020 (1.091 to 1.131)")
# units left out: entropy is undefined with fewer than two spikes in a condition (N5, N8)
K = kept["A1F1"]
print("A1F1 kept units with fewer than two spikes awake / isoflurane:", int((K.count_aw < 2).sum()), "/", int((K.count_an < 2).sum()))
# means over all units with a value in each condition separately (pandas skipna), a variant
for name in ("A1F1", "A1F2"):
    K = kept[name]
    print(f"{name}, each condition over its own defined values: awake {K.entropy_aw.mean():.3f} (n = {K.entropy_aw.notna().sum()}), "
          f"isoflurane {K.entropy_an.mean():.3f} (n = {K.entropy_an.notna().sum()})")
Kst = Tst[~npx.excluded(Tst, "F1")]
print("A1F1 from start_time:", {k: round(v, 4) for k, v in npx.paired(Kst, "entropy").items()})
by = kept["A1F1"].groupby("session").apply(lambda d: pd.Series(dict(n=d.entropy_aw.notna().sum(),
        awake=d.entropy_aw.mean(), isoflurane=d.entropy_an.mean())), include_groups=False)
print(by.round(3).to_string())
print("recordings with awake mean higher: %d of %d" % ((by.awake > by.isoflurane).sum(), by.awake.notna().sum()))
""", tags=["claim:fig4d-entropy-higher-awake"])
md(r"""
**Result: partially reproduced.** Under A1F1 entropy is higher awake, 1.389 against 1.150 nats
over 656 units with a value in both conditions (paired t test p = 3.3e-30), in the paper's direction
and at its significance, but both means are outside tolerance. Under the gist's rate (A1F2, A2F2)
they are 1.347 and 1.111 nats over 597 units, the paper's values.
""")

md(r"""
## fig4-rate-higher-awake

> The same electrical stimuli evoke more spiking awake than under isoflurane; the mean evoked
> firing rate is higher in the awake state.
""")
code(r"""
rows = []
for name, (area, wf, rate) in npx.READINGS.items():
    K = kept[name]
    r = npx.paired(K, f"rate_{rate}")
    rows.append(dict(reading=name, rate=rate, **{k: round(v, 4) if isinstance(v, float) else v for k, v in r.items()}))
    r1 = npx.paired(K, "rate_F1")
    rows.append(dict(reading=name, rate="F1 (spike count)", **{k: round(v, 4) if isinstance(v, float) else v for k, v in r1.items()}))
print(pd.DataFrame(rows).drop_duplicates().to_string())
K = kept["A1F1"]
print("units with a higher awake rate: %d of %d" % ((K.rate_F1_aw > K.rate_F1_an).sum(), len(K)))
by = K.groupby("session")[["rate_F1_aw", "rate_F1_an"]].mean()
print("recordings with higher awake mean rate: %d of %d" % ((by.rate_F1_aw > by.rate_F1_an).sum(), len(by)))
print(by.round(2).to_string())
""", tags=["claim:fig4-rate-higher-awake"])
md(r"""
**Result: reproduced.** Under A1F1 the mean evoked rate is 14.0 Hz awake against 7.6 Hz under
isoflurane (paired t test p well below 0.05, table above); every reading gives the same direction.
""")

md(r"""
## figs6-rate-regressed

> The awake decrease in synchrony and increase in entropy remain after the effect of firing rate
> is regressed out.

Readings from the criterion: (R1) one linear regression of the measure on the evoked rate across
all unit and condition values, residuals compared by the paired t test; (R2) OLS of the measure on
condition and rate, condition coefficient tested; (R3) per unit, the awake minus isoflurane
difference of the measure regressed on the difference of rate, intercept tested. The rate is the
reading's own (F1 under A1F1).
""")
code(r"""
def regressed(K, measure, rate):
    a, b = K[measure + "_aw"], K[measure + "_an"]
    ok = a.notna() & b.notna()
    K = K[ok]
    long = pd.DataFrame({"y": np.r_[K[measure + "_aw"], K[measure + "_an"]],
                         "rate": np.r_[K[f"rate_{rate}_aw"], K[f"rate_{rate}_an"]],
                         "awake": np.r_[np.ones(len(K)), np.zeros(len(K))]})
    # R1
    slope, icpt = np.polyfit(long.rate, long.y, 1)
    res = long.y - (icpt + slope * long.rate)
    n = len(K)
    t1 = stats.ttest_rel(res[:n], res[n:])
    # R2
    m2 = smf.ols("y ~ awake + rate", data=long).fit()
    # R3
    d = pd.DataFrame({"dy": K[measure + "_aw"].values - K[measure + "_an"].values,
                      "dr": K[f"rate_{rate}_aw"].values - K[f"rate_{rate}_an"].values})
    m3 = smf.ols("dy ~ dr", data=d).fit()
    return dict(n=n, R1_diff=res[:n].mean() - res[n:].mean(), R1_p=t1.pvalue,
                R2_awake_coef=m2.params["awake"], R2_p=m2.pvalues["awake"],
                R3_intercept=m3.params["Intercept"], R3_p=m3.pvalues["Intercept"])
rows = []
for name, (area, wf, rate) in npx.READINGS.items():
    for m in ("synchrony", "entropy"):
        rows.append(dict(reading=name, measure=m, **regressed(kept[name], m, rate)))
reg = pd.DataFrame(rows)
with pd.option_context("display.float_format", "{:.3g}".format):
    print(reg.to_string())
print("\nexpected signs: synchrony awake difference negative, entropy positive, p < 0.05 under every regression reading")
for m, sign in (("synchrony", -1), ("entropy", 1)):
    r = reg[(reg.reading == "A1F1") & (reg.measure == m)].iloc[0]
    ok = all(np.sign(r[k]) == sign and r[p] < 0.05 for k, p in (("R1_diff", "R1_p"), ("R2_awake_coef", "R2_p"), ("R3_intercept", "R3_p")))
    print(f"A1F1 {m}: holds under R1, R2 and R3: {ok}")
""", tags=["claim:figs6-rate-regressed"])
code(r"""
# By recording, R2 under A1F1 (a breakdown; recordings with fewer than 5 units are skipped)
rows = []
for k, d in kept["A1F1"].groupby("session"):
    if len(d) < 5:
        continue
    for m in ("synchrony", "entropy"):
        r = regressed(d, m, "F1")
        rows.append(dict(session=k, measure=m, n=r["n"], R2_awake_coef=r["R2_awake_coef"], R2_p=r["R2_p"]))
br = pd.DataFrame(rows)
with pd.option_context("display.float_format", "{:.3g}".format):
    print(br.pivot(index="session", columns="measure", values=["R2_awake_coef", "R2_p"]).to_string())
for m, sign in (("synchrony", -1), ("entropy", 1)):
    d = br[br.measure == m]
    print(f"{m}: awake coefficient in the expected direction in {int((np.sign(d.R2_awake_coef) == sign).sum())} of {len(d)} recordings")
print(f"\nnotebook run time so far {(time.time() - T0) / 60:.1f} min")
""", tags=["claim:figs6-rate-regressed"])
md(r"""
**Result: reproduced.** Under A1F1, with the evoked rate regressed out, synchrony stays lower and
entropy higher awake under each of R1, R2 and R3 (p < 0.05 for all six tests, table above), and
the same holds under every other reading.
""")

md(r"""
## Summary

| Claim | Outcome |
|---|---|
| dataset-sessions-link | reproduced |
| fig4c-sample | partially reproduced (exact under the gist's rate) |
| fig4d-synchrony-lower-awake | partially reproduced (exact under the gist's rate) |
| fig4d-entropy-higher-awake | partially reproduced (exact under the gist's rate) |
| fig4-rate-higher-awake | reproduced |
| figs6-rate-regressed | reproduced, resting on the assumption that the regression is one of R1 to R3 |
| model claims (four) | see `network_model.ipynb` |
| figs4-intrinsic-properties | blocked: methods_underspecified |
| 24 patch-clamp claims | blocked: data_missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The claims file judges each claim under the
Methods' evoked rate (spike count over trials times 10 ms). The paper's numbers come out exactly
under the rate its own code computes, which sums the spikes' latencies where a count is expected;
under that rate the exclusion keeps units below about 30 Hz of spike-count rate. The three partial
outcomes are this difference: the effects are there, at the paper's significance, with means a
little off under the Methods' rate.

**What was found about the dataset.** The 17 recordings the paper used are in the pinned version
with every field needed, and their labels and clocks pass the checks above. The version also holds
sub-599017 (units, SSp stimulation), which the paper does not use and does not mention, and six
EEG-only files. The patch-clamp recordings of Figures 1 to 3 are not in the dandiset.
""")
nb.cells = C
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "entries/burman-2023/reproduce_burman_2023.ipynb")
PYEOF
python $TMPDIR/w/build_nb1.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && . venv/bin/activate && uv pip install -q nbconvert ipykernel && cd entries/burman-2023 && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir $TMPDIR/w/out reproduce_burman_2023.ipynb 2>&1 | tail -20
```

```
Tue Nov 10 05:30:26 UTC 2026
[NbConvertApp] Making directory /tmp/claude-1001/w/out
[NbConvertApp] Converting notebook reproduce_burman_2023.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 152757 bytes to /tmp/claude-1001/w/out/reproduce_burman_2023.ipynb

real	2m0.387s
user	0m32.085s
sys	0m7.212s
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python -c "
import json;nb=json.load(open('out/reproduce_burman_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print('=== cell',i, c['metadata'].get('tags'))
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:6000])
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
        elif 'data' in o and 'text/plain' in o['data']: print(''.join(o['data']['text/plain'])[:500])
"
```

```
=== cell 1 None
=== cell 3 ['sanity']
version 0.230317.0039 | name: Simultaneous electroencephalography, extracellular electrophysiology, and cortical electrical stimulation in head-fixed mice
related resources: ['Reviewed preprint (eLife)', 'Manuscript preprint (bioRxiv)']
assets: 24 | total size 361.5 GB
draft assets identical in path and size to 0.230317.0039 : True
the 17 sessions the gist reads are all assets: True
assets not read by the paper's code: ['sub-521885_ses-20200709', 'sub-521886_ses-20200716', 'sub-521887_ses-20200730', 'sub-543393_ses-20200820', 'sub-543394_ses-20200827', 'sub-569070_ses-20210401', 'sub-599017_ses-20220210']

=== cell 4 ['sanity']
loaded 24 files in 105 s; peak memory 1.00 GB
                    session  in_gist  units                                             note target             depth  aw_valid  iso_valid  invalid   currents   pulse_ms ids_are_rows sorted
0   sub-521885_ses-20200709    False      0  no units table; acquisition ElectricalSeriesEEG    NaN               NaN       NaN        NaN      NaN        NaN        NaN          NaN    NaN
1   sub-521886_ses-20200716    False      0  no units table; acquisition ElectricalSeriesEEG    NaN               NaN       NaN        NaN      NaN        NaN        NaN          NaN    NaN
2   sub-521887_ses-20200730    False      0  no units table; acquisition ElectricalSeriesEEG    NaN               NaN       NaN        NaN      NaN        NaN        NaN          NaN    NaN
3   sub-543393_ses-20200820    False      0  no units table; acquisition ElectricalSeriesEEG    NaN               NaN       NaN        NaN      NaN        NaN        NaN          NaN    NaN
4   sub-543394_ses-20200827    False      0  no units table; acquisition ElectricalSeriesEEG    NaN               NaN       NaN        NaN      NaN        NaN        NaN          NaN    NaN
5   sub-546655_ses-20201023     True    265                                              NaN    MOs              deep     359.0      301.0  
[... 332 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python - <<'EOF'
s=open("build_nb1.py").read()
rep = [
("""        out.append(dict(reading=name, **{k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()}))
    return pd.DataFrame(out).set_index("reading")""","""        out.append(dict(reading=name, **{k: (f"{v:.2e}" if k == "p" else round(v, 4) if isinstance(v, float) else v) for k, v in r.items()}))
    return pd.DataFrame(out).set_index("reading")"""),
("""var.append(dict(variant="A1F1, times from start_time, kept n", n=len(Kst)))
print(pd.DataFrame(var).round(4).to_string())""","""var = pd.DataFrame(var).round(4)
var["p"] = var.p.map(lambda p: f"{p:.2e}")
print(var.to_string())"""),
("""    rows.append(dict(reading=name, rate=rate, **{k: round(v, 4) if isinstance(v, float) else v for k, v in r.items()}))
    r1 = npx.paired(K, "rate_F1")
    rows.append(dict(reading=name, rate="F1 (spike count)", **{k: round(v, 4) if isinstance(v, float) else v for k, v in r1.items()}))
print(pd.DataFrame(rows).drop_duplicates().to_string())""","""    rows.append(dict(reading=name, rate=rate, **r))
    if rate != "F1":
        rows.append(dict(reading=name, rate="F1 (spike count)", **npx.paired(K, "rate_F1")))
rt = pd.DataFrame(rows).round(3)
rt["p"] = rt.p.map(lambda p: f"{p:.2e}")
print(rt.to_string())"""),
("""print("A1F1 from start_time:", {k: round(v, 4) for k, v in npx.paired(Kst, "entropy").items()})""","""print("A1F1 from start_time:", {k: (f"{v:.2e}" if k == "p" else round(float(v), 4)) for k, v in npx.paired(Kst, "entropy").items()})"""),
("""# expected, so F2 is about the mean spike latency (ms) times F1. Its 200 Hz bound is then a bound
# near 200 / 7 Hz on the spike-count rate.""","""# expected, so F2 is the mean spike latency (in ms) times F1. Its 200 Hz bound is then a bound
# of 200 Hz divided by the mean latency on the spike-count rate."""),
("""In both files read at full length, the 2 to 12 ms window after the pulse holds several times the
spikes of the same window 1.5 s before or after it, in both conditions, and the counts differ
between conditions.""","""In both files read at full length, the 2 to 12 ms window after the pulse holds 3 to 18 times the
spikes of the same window 1.5 s before or after it, in both conditions, and the counts differ
between conditions (awake about twice isoflurane)."""),
("""per recording is 37 (range 7 to 95). Under the gist's rate (A1F2, and A2F2, which selects the same
units here), every number matches exactly: 662 kept, 203 excluded, median 34, range 1 to 93. The
gist's rate sums spike latencies, so its 200 Hz bound acts on the spike-count rate near 30 Hz; the
paper's exclusion was made with this rate.""","""per recording is 37 (range 7 to 95). Under the gist's rate (A1F2, and A2F2, which selects the same
units here), every number matches exactly: 662 kept, 203 excluded (143 below 0.1 Hz, 61 above
200 Hz, one unit both), median 34, range 1 to 93. The gist's rate sums spike latencies (F2 / F1
median 4.50), so its 200 Hz bound acts on spike-count rates near 45 Hz (the kept units reach
54.2 Hz); the paper's exclusion matches this rate, not the Methods' count rate."""),
("""**Result: partially reproduced.** Under A1F1 (721 units) synchrony is lower awake, 0.319 against
0.386 (paired t test p = 1.5e-32), in the paper's direction and at its significance, but the awake
mean is just outside 0.325 +- 0.005 (the isoflurane mean is at the lower edge of its tolerance,
see the unrounded values). Under the gist's rate (A1F2, A2F2) the means are 0.325 and 0.393, the
paper's values. Restricting the population to kept units, or timing from pulse onset, keeps the
direction (variant table).""","""**Result: partially reproduced.** Under A1F1 (721 units) synchrony is lower awake, 0.3188 against
0.3862 (paired t test p = 1.45e-32), in the paper's direction and at its significance, but the
awake mean is just outside 0.325 +- 0.005; the isoflurane mean is inside its tolerance, at its
lower edge. Awake is lower in 15 of 17 recordings. Under the gist's rate (A1F2, A2F2) the means
are 0.3253 and 0.3928, the paper's values. Restricting the population to kept units (0.3225
against 0.3876) or timing from pulse onset (0.3073 against 0.3720) keeps the direction."""),
("""**Result: partially reproduced.** Under A1F1 entropy is higher awake, 1.389 against 1.150 nats
over 656 units with a value in both conditions (paired t test p = 3.3e-30), in the paper's direction
and at its significance, but both means are outside tolerance. Under the gist's rate (A1F2, A2F2)
they are 1.347 and 1.111 nats over 597 units, the paper's values.""","""**Result: partially reproduced.** Under A1F1 entropy is higher awake, 1.389 against 1.150 nats
over 656 units with a value in both conditions (65 dropped with fewer than two spikes in a
condition; paired t test p below 0.001, table above), in the paper's direction and at its
significance, but both means are outside tolerance. Awake is higher in 15 of 17 recordings. Under
the gist's rate (A1F2, A2F2) they are 1.347 and 1.111 nats over 597 units, the paper's values."""),
("""**Result: reproduced.** Under A1F1 the mean evoked rate is 14.0 Hz awake against 7.6 Hz under
isoflurane (paired t test p well below 0.05, table above); every reading gives the same direction.""","""**Result: reproduced.** Under A1F1 the mean evoked rate is 14.0 Hz awake against 7.59 Hz under
isoflurane (paired t test, t = 12.36, p below 0.05, table above), higher awake in 539 of 721 units
and 15 of 17 recordings; every reading gives the same direction."""),
("""**Result: reproduced.** Under A1F1, with the evoked rate regressed out, synchrony stays lower and
entropy higher awake under each of R1, R2 and R3 (p < 0.05 for all six tests, table above), and
the same holds under every other reading.""","""**Result: reproduced.** Under A1F1, with the evoked rate regressed out, synchrony stays lower and
entropy higher awake under each of R1, R2 and R3 (all six p below 1e-10, table above), and the
same holds under every other reading, so the outcome does not depend on which regression the
unread Figure S6 legend describes."""),
("""| figs6-rate-regressed | reproduced, resting on the assumption that the regression is one of R1 to R3 |""","""| figs6-rate-regressed | reproduced (under all three regression readings) |"""),
("""under that rate the exclusion keeps units below about 30 Hz of spike-count rate.""","""under that rate the exclusion drops units above about 45 Hz of spike-count rate."""),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open("build_nb1.py","w").write(s)
EOF
cd  && python $TMPDIR/w/build_nb1.py && echo built; date -u
```

```
built
Tue Nov 10 05:33:03 UTC 2026
```

**Agent**

Neuropixels notebook done (2 min runtime). Now the model notebook, including an exact-equivalence check of my memory-saving stimulus change against the gist's original formulation.

**Agent calls Bash**

```bash
cd entries/burman-2023 && python - <<'EOF'
s=open("network.py").read()
s=s.replace("def simulate(seed, stimuli=100, repeats=100, verbose=False):\n    \"\"\"One run of the gist's network. Returns a dict per E_GABA value (-60, -80) with the\n    per-neuron arrays of the 800 excitatory neurons and the decoding accuracy.\"\"\"",
"def simulate(seed, stimuli=100, repeats=100, verbose=False, periodic=True, spikes=False):\n    \"\"\"One run of the gist's network. Returns a dict per E_GABA value (-60, -80) with the\n    per-neuron arrays of the 800 excitatory neurons and the decoding accuracy.\n\n    periodic=False builds the stimulus as the gist does, one array for the whole run (for the\n    check that both give the same spikes, on a small network run); spikes=True also returns the\n    excitatory spike times and indices.\"\"\"")
s=s.replace("""    # one stimulus set, read periodically (see the module docstring)
    I_stimulus_set = b2.TimedArray(-base_stimuli * b2.pA, dt=stimulus_duration * b2.ms)
    set_duration = stimulus_set_duration * b2.ms
""","""    if periodic:
        # one stimulus set, read periodically (see the module docstring)
        I_stimulus_set = b2.TimedArray(-base_stimuli * b2.pA, dt=stimulus_duration * b2.ms)
        set_duration = stimulus_set_duration * b2.ms
    else:
        # the gist's array for the whole run; t % set_duration then leaves t unchanged
        stimuli_full = np.vstack([base_stimuli] * (total_repeats + 1))
        I_stimulus_set = b2.TimedArray(-stimuli_full * b2.pA, dt=stimulus_duration * b2.ms)
        set_duration = 10 * total_time * b2.ms
""")
s=s.replace("""    out["run_seconds"] = sum(timing)""","""    if spikes:
        out["spikes"] = (all_t, all_i)
    out["run_seconds"] = sum(timing)""")
open("network.py","w").write(s)
EOF
. $TMPDIR/w/venv/bin/activate; python -c "
import network, numpy as np
a = network.simulate(7, stimuli=10, repeats=5, periodic=True, spikes=True)
b = network.simulate(7, stimuli=10, repeats=5, periodic=False, spikes=True)
ta, ia = a['spikes']; tb, ib = b['spikes']
print(len(ta), len(tb), np.array_equal(ia, ib) and np.allclose(ta, tb))
"
```

```
19093 19093 True
```

**Agent calls Bash**

```bash
cat > $TMPDIR/w/build_nb2.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
C = []
def md(s):
    C.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)

md(r"""
# Reproducing Burman et al. (2023): the network model (Figures 4E to 4H, S7)

**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)

**Data.** These claims are `data: elsewhere`: their data are generated by the paper's simulation
code, gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision
f6a05661c10051560aa381e334099efd8521617b, transcribed in `network.py` (its docstring lists the
differences, none of which changes the model). They use nothing from DANDI:000458 (version
0.230317.0039, read in `reproduce_burman_2023.ipynb`; the version constant is `npx.VERSION`).

**Text the claims were written from.** The version of record (PMC11913778) with STAR Methods; the
supplement (Figure S7) was not available.

| Claim | Here |
|---|---|
| fig4f-model-hyperpolarizing-less-activity | tested |
| fig4h-model-synchrony | tested |
| fig4h-model-entropy | tested |
| figs7-model-decoding | tested |

Method (every claim's criterion): the gist at its defaults (100 patterns, 100 repeats per
condition, 800 excitatory and 200 inhibitory neurons, E_GABA -60 mV then -80 mV in the excitatory
neurons), run 20 times (Methods, "Each simulation was repeated 20 times"); per run and condition,
the gist's entropy, synchrony and peri-stimulus rate of each excitatory neuron from spikes 0 to 12 ms
after each input of the first stimulus set, and its decoding accuracy; the 20 runs pooled (16,000
neurons). Seeds are fixed here, 1 to 20, one per run (the gist sets none).
""")
code(r"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time, resource
from multiprocessing import Pool
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import network, npx

pd.set_option("display.width", 200)
T0 = time.time()
SEEDS = list(range(1, 21))
print("dataset named for the record:", npx.DANDISET, npx.VERSION, "(not used by this notebook)")
""")
md("## Data check\n\nThe model's data are its simulated spikes. First a check that the stimulus held "
   "as one periodic set (`network.py`) gives the same spikes as the gist's whole-run array, on a "
   "small network run (10 patterns, 5 repeats) with one seed.")
code(r"""
a = network.simulate(7, stimuli=10, repeats=5, periodic=True, spikes=True)
b = network.simulate(7, stimuli=10, repeats=5, periodic=False, spikes=True)
(ta, ia), (tb, ib) = a["spikes"], b["spikes"]
print("spikes, periodic stimulus:", len(ta), "| gist's whole-run array:", len(tb))
print("identical spike trains:", len(ta) == len(tb) and np.array_equal(ia, ib) and np.allclose(ta, tb))
print("inhibitory-to-excitatory summed weight (nS): start %.0f, after balancing %.1f, after test %.1f"
      % tuple(a["w_sums"]))
""", tags=["sanity"])
code(r"""
t = time.time()
with Pool(4) as pool:
    runs = pool.map(network.run, SEEDS)
print(f"20 runs in {(time.time() - t) / 60:.1f} min (4 processes); peak memory of this process "
      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB, of a child "
      f"{resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6:.2f} GB")
rows = []
for seed, r in zip(SEEDS, runs):
    for eg, cond in zip(network.EGABA, ("shunting", "hyperpolarizing")):
        d = r[eg]
        rows.append(dict(seed=seed, condition=cond, E_GABA=eg, spikes_in_condition=d["total_spikes"],
                         neurons_with_spikes=int((d["spike_count"] > 0).sum()),
                         rate_mean=d["firing_rate"].mean(), entropy_mean=np.nanmean(d["entropy"]),
                         synchrony_mean=np.nanmean(d["synchrony"]), accuracy=d["accuracy"]))
per_run = pd.DataFrame(rows)
print(per_run.round(4).to_string())
print("\nweights after balancing equal weights after the test in every run:",
      all(abs(r["w_sums"][1] - r["w_sums"][2]) < 1e-6 for r in runs))
""", tags=["sanity"])
code(r"""
def pooled(key):
    sh = np.concatenate([r[-60][key] for r in runs])
    hy = np.concatenate([r[-80][key] for r in runs])
    return sh, hy
def paired_report(key, label):
    sh, hy = pooled(key)
    ok = ~np.isnan(sh) & ~np.isnan(hy)
    t = stats.ttest_rel(sh[ok], hy[ok])
    print(f"{label}: neurons {len(sh)}, defined in both conditions {ok.sum()} (dropped {(~ok).sum()})")
    print(f"  shunting {sh[ok].mean():.4f} +- {stats.sem(sh[ok]):.4f} (SEM), hyperpolarizing {hy[ok].mean():.4f} +- {stats.sem(hy[ok]):.4f}")
    print(f"  paired t test t = {t.statistic:.2f}, p = {t.pvalue:.2e}")
    print(f"  range shunting {np.nanmin(sh):.3f} to {np.nanmax(sh):.3f}, hyperpolarizing {np.nanmin(hy):.3f} to {np.nanmax(hy):.3f}")
    return sh[ok].mean(), hy[ok].mean(), t
""")

md(r"""
## fig4h-model-synchrony

> Model pyramidal neurons are less synchronous with shunting than with hyperpolarizing E_GABAAR
> (0.784 against 0.881).
""")
code(r"""
syn_sh, syn_hy, syn_t = paired_report("synchrony", "synchrony")
print("expected shunting 0.784 +- 0.001, hyperpolarizing 0.881 +- 0.001")
pr = per_run.pivot(index="seed", columns="condition", values="synchrony_mean")
print("runs with lower mean synchrony under shunting: %d of %d; per-run means shunting %.4f to %.4f, hyperpolarizing %.4f to %.4f"
      % ((pr.shunting < pr.hyperpolarizing).sum(), len(pr), pr.shunting.min(), pr.shunting.max(), pr.hyperpolarizing.min(), pr.hyperpolarizing.max()))
""", tags=["claim:fig4h-model-synchrony"])
md("**Result: SYNC_RESULT**")

md(r"""
## fig4h-model-entropy

> Model pyramidal neurons have higher peri-stimulus entropy with shunting than with
> hyperpolarizing E_GABAAR (0.451 against 0.197 nats).
""")
code(r"""
ent_sh, ent_hy, ent_t = paired_report("entropy", "entropy (nats)")
print("expected shunting 0.451 +- 0.002, hyperpolarizing 0.197 +- 0.002")
pr = per_run.pivot(index="seed", columns="condition", values="entropy_mean")
print("runs with higher mean entropy under shunting: %d of %d; per-run means shunting %.4f to %.4f, hyperpolarizing %.4f to %.4f"
      % ((pr.shunting > pr.hyperpolarizing).sum(), len(pr), pr.shunting.min(), pr.shunting.max(), pr.hyperpolarizing.min(), pr.hyperpolarizing.max()))
rng = np.random.default_rng(4)  # this section's generator: the 1,000 neurons plotted, as in Figure 4G
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
for ax, key, lab in zip(axes, ("synchrony", "entropy"), ("Synchrony", "Entropy (nats)")):
    sh, hy = pooled(key)
    ok = np.flatnonzero(~np.isnan(sh) & ~np.isnan(hy))
    pick = rng.choice(ok, 1000, replace=False)
    ax.scatter(hy[pick], sh[pick], s=3)
    lim = [min(sh[pick].min(), hy[pick].min()), max(sh[pick].max(), hy[pick].max())]
    ax.plot(lim, lim, "k--", lw=1); ax.set_xlabel(lab + ", hyperpolarizing"); ax.set_ylabel(lab + ", shunting")
    print(f"{key}: plotted 1,000 of {len(ok)} neurons, range {lim[0]:.3f} to {lim[1]:.3f}, none outside the axes")
fig.tight_layout(); plt.show()
""", tags=["claim:fig4h-model-entropy"])
md("**Result: ENT_RESULT**")

md(r"""
## fig4f-model-hyperpolarizing-less-activity

> In the network model, shunting E_GABAAR gives more variable input-evoked spike times, while
> hyperpolarizing E_GABAAR gives less activity and spiking more closely aligned across neurons.

The activity part: the gist's peri-stimulus firing rate of the excitatory neurons, pooled over
the 20 runs, neurons with no spike included at zero, paired t test. The spike-time parts are judged
in the two claims above.
""")
code(r"""
sh, hy = pooled("firing_rate")
t = stats.ttest_rel(sh, hy)
print(f"neurons {len(sh)}; peri-stimulus rate shunting {sh.mean():.3f} +- {stats.sem(sh):.3f} Hz, "
      f"hyperpolarizing {hy.mean():.3f} +- {stats.sem(hy):.3f} Hz; paired t = {t.statistic:.2f}, p = {t.pvalue:.2e}")
print("neurons with no peri-stimulus spike: shunting %d, hyperpolarizing %d" % ((sh == 0).sum(), (hy == 0).sum()))
pr = per_run.pivot(index="seed", columns="condition", values="rate_mean")
print("runs with lower mean rate under hyperpolarizing: %d of %d" % ((pr.hyperpolarizing < pr.shunting).sum(), len(pr)))
sp = per_run.pivot(index="seed", columns="condition", values="spikes_in_condition")
print("spikes over the whole condition (all 100 repeats), hyperpolarizing / shunting: %.3f to %.3f"
      % ((sp.hyperpolarizing / sp.shunting).min(), (sp.hyperpolarizing / sp.shunting).max()))
""", tags=["claim:fig4f-model-hyperpolarizing-less-activity"])
md("**Result: RATE_RESULT**")

md(r"""
## figs7-model-decoding

> Responses of networks with shunting E_GABAAR to 100 different input patterns are decoded more
> accurately by a downstream classifier.

The gist's decoder: spike counts of the first 50 excitatory neurons in each 25 ms epoch, a
k-nearest neighbour classifier (scikit-learn defaults), 5-fold shuffled stratified
cross-validation over the 10,000 trials of a condition, mean accuracy. Chance is 1%. Readings: (D1)
paired t test of the 20 per-run accuracies, (D2) shunting higher in every run.
""")
code(r"""
acc = per_run.pivot(index="seed", columns="condition", values="accuracy")
t = stats.ttest_rel(acc.shunting, acc.hyperpolarizing)
print(acc.round(4).to_string())
print(f"\nmean accuracy shunting {acc.shunting.mean():.4f}, hyperpolarizing {acc.hyperpolarizing.mean():.4f} (chance 0.01)")
print(f"D1 paired t = {t.statistic:.2f}, p = {t.pvalue:.2e}")
print("D2 shunting higher in %d of %d runs" % ((acc.shunting > acc.hyperpolarizing).sum(), len(acc)))
print(f"\nnotebook run time {(time.time() - T0) / 60:.1f} min")
""", tags=["claim:figs7-model-decoding"])
md("**Result: DEC_RESULT**")

md(r"""
## Summary

SUMMARY_TABLE

**How the analysis differs from the paper's.** The model is the paper's code, with the stimulus held
as one periodic set to fit in memory (identical spikes, checked above) and seeds fixed, so the 20
runs are other draws of the same model than the paper's.
""")
nb.cells = C
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "entries/burman-2023/network_model.ipynb")
PYEOF
cd  && python $TMPDIR/w/build_nb2.py && cd entries/burman-2023 && . $TMPDIR/w/venv/bin/activate && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=4000 --output-dir $TMPDIR/w/out network_model.ipynb 2>&1 | tail -3; date -u
```

```
Tue Nov 10 05:34:58 UTC 2026
[NbConvertApp] Converting notebook network_model.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 110414 bytes to /tmp/claude-1001/w/out/network_model.ipynb

real	31m53.015s
user	112m44.684s
sys	0m9.583s
Tue Nov 10 06:06:51 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python -c "
import json;nb=json.load(open('out/network_model.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print('=== cell',i, c['metadata'].get('tags'))
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:8000])
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
"
```

```
=== cell 1 None
dataset named for the record: 000458 0.230317.0039 (not used by this notebook)

=== cell 3 ['sanity']
spikes, periodic stimulus: 19093 | gist's whole-run array: 19093
identical spike trains: True
inhibitory-to-excitatory summed weight (nS): start 15905, after balancing 16646.9, after test 16646.9

=== cell 4 ['sanity']
20 runs in 31.7 min (4 processes); peak memory of this process 0.36 GB, of a child 2.17 GB
    seed        condition  E_GABA  spikes_in_condition  neurons_with_spikes  rate_mean  entropy_mean  synchrony_mean  accuracy
0      1         shunting     -60              2119560                  800    19.5021        0.4647          0.7782    0.9820
1      1  hyperpolarizing     -80               927971                  800     8.6719        0.1798          0.8909    0.9437
2      2         shunting     -60              2107732                  800    19.3281        0.4527          0.7828    0.9785
3      2  hyperpolarizing     -80               927676                  800     8.7865        0.2042          0.8767    0.9328
4      3         shunting     -60              2118960                  800    19.3958        0.4598          0.7791    0.9866
5      3  hyperpolarizing     -80               942619                  800     8.9146        0.1986          0.8813    0.9225
6      4         shunting     -60              2110248                  800    19.3885        0.4475          0.7842    0.9906
7      4  hyperpolarizing     -80               913382                  800     8.6448        0.1955          0.8825    0.9527
8      5         shunting     -60              2126850                  800    19.4938        0.4446          0.7869    0.9919
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/w/venv/bin/activate; uv pip list 2>/dev/null | grep -i -E "cython|setuptools|brian|scikit|requests|statsmodels|remfile|h5py|pynwb|numpy|scipy|pandas|matplotlib"
```

```
brian2                    2.11.0
cython                    3.3.1
h5py                      3.16.0
matplotlib                3.11.2
matplotlib-inline         0.2.2
numpy                     2.5.4
pandas                    3.1.1
pynwb                     4.2.0
remfile                   0.1.15
requests                  2.34.2
scikit-learn              1.9.1
scipy                     1.18.1
setuptools                84.2.1
statsmodels               0.15.0
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python - <<'EOF'
s=open("build_nb2.py").read()
rep = {
'md("**Result: SYNC_RESULT**")': '''md("**Result: partially reproduced.** Over the 16,000 pooled neurons synchrony is lower with "
   "shunting E_GABA, 0.7833 against 0.8789 (paired t = -134.60; p underflows to 0, below 0.001), and "
   "lower in all 20 runs. The shunting mean is within 0.784 +- 0.001; the hyperpolarizing mean is "
   "0.0011 below the lower bound of 0.881 +- 0.001. The per-run hyperpolarizing means span 0.8661 to "
   "0.8909, so the tolerance, the paper's SEM over pooled neurons, is narrower than the spread "
   "between runs with other seeds.")''',
'md("**Result: ENT_RESULT**")': '''md("**Result: partially reproduced.** Entropy is higher with shunting E_GABA, 0.4516 against "
   "0.2014 nats (paired t = 93.09; p underflows to 0, below 0.001), and higher in all 20 runs. The "
   "shunting mean is within 0.451 +- 0.002; the hyperpolarizing mean is 0.0024 above the upper bound "
   "of 0.197 +- 0.002. Per-run hyperpolarizing means span 0.1798 to 0.2217, wider than the "
   "tolerance.")''',
'md("**Result: RATE_RESULT**")': '''md("**Result: reproduced.** The peri-stimulus rate is lower with hyperpolarizing E_GABA, 8.785 "
   "against 19.468 Hz over 16,000 neurons (paired t = 446.42, p below 0.05), and lower in all 20 runs; "
   "over whole conditions the hyperpolarizing network fires 0.431 to 0.445 times the spikes of the "
   "shunting one. The spike-time parts of the statement hold in the two claims above (higher entropy "
   "and lower synchrony with shunting E_GABA).")''',
'md("**Result: DEC_RESULT**")': '''md("**Result: reproduced.** Decoding accuracy is higher with shunting E_GABA, 0.9848 against "
   "0.9315 on average (chance 0.01); D1 paired t = 16.92, p = 6.52e-13, and D2 holds, shunting higher "
   "in 20 of 20 runs.")''',
"SUMMARY_TABLE": """| Claim | Outcome |
|---|---|
| fig4h-model-synchrony | partially reproduced (hyperpolarizing mean 0.8789, 0.0011 outside tolerance) |
| fig4h-model-entropy | partially reproduced (hyperpolarizing mean 0.2014, 0.0024 outside tolerance) |
| fig4f-model-hyperpolarizing-less-activity | reproduced |
| figs7-model-decoding | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The two partial outcomes are means a little outside tolerances that are the SEM over pooled
neurons; the spread of the per-run means is wider, and the paper's seeds are not known.""",
}
for a,b in rep.items():
    assert a in s, a; s=s.replace(a,b)
open("build_nb2.py","w").write(s)
EOF
cd  && python $TMPDIR/w/build_nb2.py && cat > entries/burman-2023/requirements.in <<'EOF'
brian2
cython
h5py
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
setuptools
statsmodels
EOF
cat > entries/burman-2023/entry.yaml <<'EOF'
schema_version: 1
name: burman-2023
type: reproduction
title: Shunting inhibition, synchrony and entropy in Neuropixels recordings and a network model (Burman et al. 2023)
description: Tests the findings of Burman, Brodersen, Raimondo, Sen and Akerman (2023) that can be
  tested on dandiset 000458, the Allen Institute Neuropixels recordings with cortical electrical
  stimulation awake and under isoflurane that the paper reuses (Figure 4A to 4D, Figure S6), and
  runs the paper's network model (Figure 4E to 4H, Figure S7). The paper's gramicidin patch-clamp
  recordings (Figures 1 to 3) are not in the dandiset nor deposited elsewhere.
license: Apache-2.0
notebooks:
- path: reproduce_burman_2023.ipynb
  title: Neuropixels claims of Burman et al. (2023) on dandiset 000458
  runtime_minutes: 3
- path: network_model.ipynb
  title: The network model of Burman et al. (2023), 20 runs
  runtime_minutes: 33
helpers:
- npx.py
- network.py
related:
- id: dandi:000458/0.230317.0039
  relation: uses_data
- id: doi:10.1016/j.neuron.2023.08.005
  relation: reproduces
EOF
python -c "import json;s=json.load(open('schemas/entry.schema.json'));print(json.dumps(s['properties'],indent=0)[:2500])"
```

```
{
"schema_version": {
"const": 1
},
"name": {
"description": "Unique across the registry, and the name of the entry's directory.",
"type": "string",
"pattern": "^[a-z0-9]+(-[a-z0-9]+)*$",
"maxLength": 100
},
"type": {
"enum": [
"orientation",
"reproduction",
"analysis"
]
},
"title": {
"type": "string",
"minLength": 1,
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/entry.py lock entries/burman-2023 2>&1 | tail -3 && python tools/entry.py check entries/burman-2023 2>&1 | tail -10; date -u
```

```
wrote burman-2023/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
Tue Nov 10 06:07:42 UTC 2026
```

**Agent**

Entry locks and passes checks. Running the full entry from a clean environment now (~35 min).

**Agent calls Bash**

```bash
time python tools/entry.py all entries/burman-2023 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-burman-2023 in executed/burman-2023/.venv/share/jupyter/kernels/registry-burman-2023
0 error(s)
pass  reproduce_burman_2023.ipynb  (137 s)
pass  network_model.ipynb  (2041 s)

real	36m26.256s
user	115m45.897s
sys	0m28.664s
Tue Nov 10 06:44:11 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/burman-2023 && python -c "
import json
for f in ['reproduce_burman_2023.ipynb','network_model.ipynb']:
    nb=json.load(open(f))
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        tags=c['metadata'].get('tags',[])
        if not any(t.startswith('claim:') for t in tags): continue
        for o in c.get('outputs',[]):
            if 'text' in o:
                t=''.join(o['text'])
                for line in t.splitlines():
                    if any(k in line for k in ['A1F1  ','A1F2  ','shunting 0.','mean accuracy','D1','D2','peri-stimulus rate','unrounded','holds under','F2 / F1','kept units reach','F1 rate of','units with a higher','recordings with']): print(f[:5], line[:160])
            elif o.get('output_type')=='error': print('ERROR')
"
```

```
repro A1F1                           865   721       144          143            1          17    16    37.0    7   95
repro A1F2                           865   662       203          143           61          17    16    34.0    1   93
repro                          A1F1  A1F2  selected
repro F2 / F1 (awake), median 4.50, 5th to 95th percentile 2.93 to 7.22
repro F1 rate of the units F2 keeps: awake max 51.0 Hz, isoflurane max 54.2 Hz
repro A1F1                      721  0.3188     0.0046        0.3862            0.0067 -12.4948  1.45e-32        0
repro A1F2                      662  0.3253     0.0049        0.3928            0.0071 -11.7850  3.12e-29        0
repro A1F1 unrounded: awake 0.31885, isoflurane 0.38624, p = 1.45e-32
repro recordings with awake mean lower: 15 of 17
repro A1F1                      656  1.3887     0.0182        1.1502            0.0205  12.0189  3.28e-30       65
repro A1F2                      597  1.3474     0.0188        1.1106            0.0211  11.1306  2.82e-26       65
repro recordings with awake mean higher: 15 of 17
repro 0                      A1F1                F1  721  14.000      0.658         7.591             0.471  12.361  0.00e+00        0
repro 1                      A1F2                F2  662  45.051      1.750        24.294             1.225  13.446  0.00e+00        0
repro 2                      A1F2  F1 (spike count)  662  10.156      0.404         5.401             0.280  13.610  0.00e+00        0
repro units with a higher awake rate: 539 of 721
repro recordings with higher awake mean rate: 15 of 17
repro 0                       A1F1  synchrony  721  -0.0593 3.32e-26        -0.0619 1.52e-13       -0.0625 2.79e-24
repro 1                       A1F1    entropy  656    0.171 7.08e-17          0.179 4.17e-11          0.21 1.07e-20
repro 2                       A1F2  synchrony  662  -0.0569 4.73e-22         -0.061  9.2e-12       -0.0583 1.28e-18
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
for q in gramicidin Akerman "Burman" "EGABA"; do echo "== $q"; curl -s "https://api.dandiarchive.org/api/dandisets/?search=$(python -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&page_size=20" | python -c "import json,sys;d=json.load(sys.stdin);print(d['count']);[print(r['identifier'], r.get('most_recent_published_version',{}) and r['most_recent_published_version'].get('name') or r['draft_version']['name']) for r in d['results']]"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  && cat > $TMPDIR/w/write_attempt.py <<'PYEOF'
import yaml
NB1, NB2 = "reproduce_burman_2023.ipynb", "network_model.ipynb"
patch = ["fig1b-perforation-rs", "fig1h-vu-egaba", "fig1i-vu-rmp", "fig1j-vu-df", "figs2-ramp-equals-step",
         "figs3-egaba-unrelated-amplitude-rs", "rm-awake-lower", "fig2c-vm-depolarized",
         "fig2d-subthreshold-fluctuation", "fig2f-response-polarity", "fig2h-egaba-depolarized",
         "fig2i-rmp-depolarized", "fig2j-df-depolarized", "fig2j-awake-df-zero", "fig2k-conductance-same",
         "figs5-within-anesthetized", "rm-nbqx-higher", "fig3c-nbqx-vm", "fig3d-nbqx-fluctuation",
         "fig3e-nbqx-polarity", "fig3g-nbqx-egaba", "fig3h-nbqx-rmp", "fig3i-nbqx-df",
         "fig3j-nbqx-conductance-same"]
GIST_A = ("the analysis gist (gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf at "
          "revision 43a13d89)")
common_dev = [
    "Trials of all stimulus currents and depths of a session are pooled and times are taken from "
    "stop_time, as the claims file (N3) gives from the gist; the Methods say only \"following an "
    "electrical stimulus\". Timing from start_time, the pulse onset 0.4 ms earlier, is shown as a "
    "variant and keeps the direction.",
    "The Methods' waveform cut (>= 0.4 ms) and the gist's (> 0.4 ms) select the same units, as no "
    "unit has a duration of exactly 0.4 ms; readings A1 and A2 also select the same 865 units, as "
    "the SSp sessions hold only SSp-ll and SSp-tr units.",
]
gist_rate_dev = ("Judged under the Methods reading A1F1, as the claims file requires. The paper's "
                 "numbers come out exactly under the gist's rate (A1F2, A2F2), which sums spike "
                 "latencies where a count is expected; this claim holds fully only under that variant.")
outcomes = []
outcomes.append(dict(
    claim="dataset-sessions-link", outcome="reproduced", notebook=NB1, output="claim:dataset-sessions-link",
    notes="All 17 files the gist lists are in version 0.230317.0039, each with spike_times, location and "
          "waveform_duration in its units table, stimulus_type, behavioral_epoch, is_valid, "
          "estim_target_region and stop_time in its trials table, and awake and isoflurane electrical "
          "trials. They hold 16 subjects (sub-569073 twice, one MOs and one SSp session). Unit ids equal "
          "row numbers in every file, so the gist's keying of units by row and lookup by id select the "
          "same units. The version holds seven more files, six with EEG only and sub-599017 with units "
          "and SSp stimulation, which the gist does not read."))
outcomes.append(dict(
    claim="fig4c-sample", outcome="partially_reproduced", notebook=NB1, output="claim:fig4c-sample",
    measured=[721, 144, 17, 16, 37, 7, 95],
    notes="Under A1F1, 865 regular spiking units of the stimulated areas are selected (the paper's "
          "662 + 203), 721 kept and 144 excluded (143 below 0.1 Hz, 1 above 200 Hz), from 17 recordings "
          "in 16 mice, a median of 37 per recording (7 to 95). Kept is within 662 +- 66.2 and excluded is "
          "outside 203 +- 20.3, so by the criterion the claim is partially reproduced (the total is the "
          "paper's). Under the gist's rate (A1F2 and A2F2) every number is the paper's exactly, 662 kept, "
          "203 excluded (143 below 0.1 Hz, 61 above 200 Hz), median 34, range 1 to 93. The gist's rate is "
          "the summed spike latency over trials times 10 ms, a median 4.50 times the count rate, so its "
          "200 Hz bound drops units whose spike-count rate exceeds about 45 Hz (kept units reach 54.2 Hz).",
    deviations=[gist_rate_dev] + common_dev))
outcomes.append(dict(
    claim="fig4d-synchrony-lower-awake", outcome="partially_reproduced", notebook=NB1,
    output="claim:fig4d-synchrony-lower-awake", measured=[0.3188, 0.3862],
    notes="Under A1F1 (721 units) synchrony is 0.3188 +- 0.0046 awake against 0.3862 +- 0.0067 under "
          "isoflurane, paired t = -12.49, p = 1.45e-32. Direction and test hold; the awake mean is just "
          "below 0.325 +- 0.005 and the isoflurane mean is inside its tolerance. Awake is lower in 489 "
          "of 721 units and in 15 of 17 recordings. Under the gist's rate (A1F2, A2F2, 662 units) the "
          "means are 0.3253 and 0.3928, the paper's (p = 3.12e-29). With the population restricted to "
          "kept units, A1F1 gives 0.3225 against 0.3876 and A1F2 gives 0.3686 against 0.4333, further from "
          "the paper, which supports the gist's population of all selected units (N6). Timed from "
          "start_time, 0.3073 against 0.3720.",
    deviations=[gist_rate_dev] + common_dev))
outcomes.append(dict(
    claim="fig4d-entropy-higher-awake", outcome="partially_reproduced", notebook=NB1,
    output="claim:fig4d-entropy-higher-awake", measured=[1.3887, 1.1502],
    notes="Under A1F1 entropy is 1.3887 +- 0.0182 awake against 1.1502 +- 0.0205 nats under isoflurane "
          "over 656 units with a value in both conditions (65 left out with fewer than two spikes in a "
          "condition), paired t = 12.02, p = 3.28e-30. Direction and test hold; both means are outside "
          "tolerance. Awake is higher in 15 of 17 recordings. Under the gist's rate (A1F2, A2F2) the "
          "means are 1.3474 and 1.1106 over 597 units, the paper's values; taking each condition's mean "
          "over its own defined units gives 1.324 and 1.104 there, so the paper's means are over units "
          "defined in both conditions, though it gives n = 662.",
    deviations=[gist_rate_dev] + common_dev))
outcomes.append(dict(
    claim="fig4-rate-higher-awake", outcome="reproduced", notebook=NB1, output="claim:fig4-rate-higher-awake",
    notes="Under A1F1 the evoked spike-count rate is 14.00 +- 0.66 Hz awake against 7.59 +- 0.47 Hz under "
          "isoflurane over 721 units, paired t = 12.36 (p printed as 0, far below 0.05); higher awake in "
          "539 of 721 units and 15 of 17 recordings. Every reading gives the same direction (gist rate "
          "45.05 against 24.29). The paper reports no value or test for this in the text read; the test "
          "is the claims file's.",
    deviations=common_dev))
outcomes.append(dict(
    claim="figs6-rate-regressed", outcome="reproduced", notebook=NB1, output="claim:figs6-rate-regressed",
    notes="Under A1F1, with the evoked rate regressed out, the awake difference keeps its sign with p "
          "below 1e-10 in all six tests. Synchrony R1 -0.0593 (p = 3.3e-26), R2 -0.0619 (p = 1.5e-13), "
          "R3 -0.0625 (p = 2.8e-24); entropy R1 0.171 (p = 7.1e-17), R2 0.179 (p = 4.2e-11), R3 0.210 "
          "(p = 1.1e-20). Every other reading gives the same. By recording (R2), the coefficient has the "
          "expected sign in 15 of 17 for each measure. The regression of Figure S6 is in a legend not "
          "read; as all three readings the criterion names agree, the outcome does not depend on which "
          "it is.",
    deviations=common_dev + ["The regression method is open (Figure S6 legend not in the text read); the "
                             "three readings of the criterion were all run and agree."]))
outcomes.append(dict(
    claim="fig4f-model-hyperpolarizing-less-activity", outcome="reproduced", notebook=NB2,
    output="claim:fig4f-model-hyperpolarizing-less-activity",
    notes="Over the 16,000 excitatory neurons of 20 runs, the peri-stimulus rate is 8.785 +- 0.020 Hz "
          "with hyperpolarizing E_GABA against 19.468 +- 0.026 Hz with shunting E_GABA, paired t = "
          "446.42 (p underflows to 0); lower in all 20 runs. No neuron is without a spike. The spike-time "
          "parts of the statement are judged in fig4h-model-synchrony and fig4h-model-entropy, where the "
          "direction holds.",
    deviations=["Seeds are fixed (1 to 20, one per run) where the gist sets none, so the runs are other "
                "draws of the paper's model; this cannot change the model, only the sample.",
                "The stimulus is held as one periodic 2,500 ms set instead of the gist's 4 GB whole-run "
                "array, to fit in memory; a small run with both gives identical spike trains (data check)."]))
model_dev = outcomes[-1]["deviations"]
outcomes.append(dict(
    claim="fig4h-model-synchrony", outcome="partially_reproduced", notebook=NB2,
    output="claim:fig4h-model-synchrony", measured=[0.7833, 0.8789],
    notes="Synchrony 0.7833 +- 0.0005 shunting against 0.8789 +- 0.0006 hyperpolarizing over 16,000 "
          "neurons, paired t = -134.60 (p underflows to 0, below 0.001), lower with shunting in all 20 "
          "runs. The shunting mean is within 0.784 +- 0.001; the hyperpolarizing mean is 0.0011 below "
          "0.880, so the criterion gives partially reproduced. Per-run hyperpolarizing means span 0.8661 "
          "to 0.8909, so the tolerance (the paper's SEM over pooled neurons) is narrower than the spread "
          "between seeds, and the paper's seeds are not known.", deviations=model_dev))
outcomes.append(dict(
    claim="fig4h-model-entropy", outcome="partially_reproduced", notebook=NB2,
    output="claim:fig4h-model-entropy", measured=[0.4516, 0.2014],
    notes="Entropy 0.4516 +- 0.0020 shunting against 0.2014 +- 0.0019 nats hyperpolarizing over 16,000 "
          "neurons, paired t = 93.09 (p underflows to 0, below 0.001), higher with shunting in all 20 "
          "runs. The shunting mean is within 0.451 +- 0.002; the hyperpolarizing mean is 0.0024 above "
          "0.199, so the criterion gives partially reproduced. Per-run hyperpolarizing means span 0.1798 "
          "to 0.2217, wider than the tolerance.", deviations=model_dev))
outcomes.append(dict(
    claim="figs7-model-decoding", outcome="reproduced", notebook=NB2, output="claim:figs7-model-decoding",
    notes="Mean decoding accuracy 0.9848 shunting against 0.9315 hyperpolarizing (chance 0.01). D1, paired "
          "t test of the 20 per-run accuracies, t = 16.92, p = 6.52e-13; D2, shunting higher in 20 of 20 "
          "runs.",
    deviations=model_dev + ["The cross-validation shuffle is seeded with the run's seed (the gist sets none), "
                            "a standard choice that cannot change the outcome."]))
outcomes.append(dict(
    claim="figs4-intrinsic-properties", outcome="blocked", blocked_by="other",
    notes="The claim rests on the paper's NEURON model of an L2/3 pyramidal neuron and a Matlab analysis "
          "of its simulated ramps (github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR at commit "
          "a404c3e: hoc files and NEURON_Egaba_Analysis.m). The measure and test of Figure S4 are in the "
          "supplement, which was not supplied with the text, and the claims file gives no criterion for "
          "them, so there is nothing fixed to judge; the analysis code is Matlab, which cannot be run in "
          "a locked Python environment here (a transcription was not attempted). Neither part uses the "
          "dandiset."))
for c in patch:
    outcomes.append(dict(
        claim=c, outcome="blocked", blocked_by="data_missing",
        notes="Needs the paper's in vivo gramicidin perforated patch recordings of L2/3 pyramidal neurons in "
              "V1. DANDI:000458 holds only the Allen Institute Neuropixels and EEG recordings, and the "
              "paper deposits the patch data nowhere (\"available on request to the lead contact\"). A "
              "search of the DANDI archive for gramicidin, Akerman, Burman and EGABA found no dandiset."))

attempt = dict(
    schema_version=3, id="burman-2023-01",
    datasets=[dict(archive="dandi", id="000458", version="0.230317.0039",
                   doi="10.48324/dandi.000458/0.230317.0039", relation="reuses")],
    paper="doi:10.1016/j.neuron.2023.08.005", date="2026-11-10", entry="burman-2023",
    provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
                    agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-14"),
                    runner=dict(platform="GitHub Actions",
                                url="https://github.com/catalystneuro/encore/actions/runs/42760152737")),
    inputs=[
        dict(what="The paper's Neuropixels analysis code, burman_et_al_2023_neuropixel_data_analysis.py: the "
                  "list of 17 sessions and the method details the claims file takes from it (stop_time, the "
                  "area and waveform selection, the evoked rate of reading F2, entropy and synchrony). No data.",
             source="https://gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf at revision "
                    "43a13d89441b7f56e835e84fa5811d9567917daf"),
        dict(what="The paper's network simulation, burman_et_al_2023_neuronal_network_simulation.py, transcribed "
                  "in network.py and run 20 times to generate the data of the four model claims "
                  "(data elsewhere).",
             source="https://gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision "
                    "f6a05661c10051560aa381e334099efd8521617b"),
    ],
    outcomes=outcomes,
    findings=[
        dict(kind="code_mismatch",
             statement="The paper's analysis code computes the evoked firing rate used for the exclusion "
                       "(below 0.1 Hz or above 200 Hz) as the sum of the spikes' latencies in ms (np.sum of "
                       "spike_times) over trials times 10 ms, where the Methods describe an average evoked "
                       "firing rate. With this rate the dataset gives the paper's sample exactly (662 kept, "
                       "203 excluded, median 34 per recording, 1 to 93) and its Figure 4D means (synchrony "
                       "0.325 and 0.393, entropy 1.347 and 1.111); with the spike-count rate it gives 721 kept "
                       "and 144 excluded. The 200 Hz bound thus acted on spike-count rates near 45 Hz."),
        dict(kind="selection_undocumented",
             statement="Version 0.230317.0039 holds 18 files with units and electrical stimulation awake and "
                       "under isoflurane; the paper uses 17. sub-599017_ses-20220210 (943 units, SSp "
                       "stimulation, 718 awake and 720 isoflurane valid trials) is not in the paper's code "
                       "list, and the paper does not say why. Six further files hold EEG only, with no units."),
        dict(kind="data_missing",
             statement="The paper's gramicidin perforated patch recordings (Figures 1 to 3, S1 to S5), which "
                       "carry most of its findings, are not in DANDI:000458 nor in any other dandiset found; "
                       "the paper offers them on request. 24 of its claims cannot be tested."),
        dict(kind="code_mismatch",
             statement="The Methods select regular spiking units with a waveform duration of 0.4 ms or more, "
                       "the code more than 0.4 ms, and the Methods name the areas SSp-ll, SSp-tr and MOs where "
                       "the code takes every unit whose location begins with the stimulated region. Neither "
                       "difference changes the units selected in this dataset."),
    ],
)
class D(yaml.SafeDumper): pass
def str_rep(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)
D.add_representer(str, str_rep)
txt = yaml.dump(attempt, Dumper=D, sort_keys=False, width=100, allow_unicode=True)
open("attempts/burman-2023-01.yaml", "w").write(txt)
print(len(outcomes))
PYEOF
python $TMPDIR/w/write_attempt.py && grep -c ": " attempts/burman-2023-01.yaml >/dev/null; python - <<'EOF'
import yaml,re
t=open("attempts/burman-2023-01.yaml").read()
# plain scalars containing ': ' would have been quoted by yaml; check unquoted lines
bad=[l for l in t.splitlines() if re.search(r":\s.*: ", l) and not re.search(r":\s+['\"]", l)]
print("suspect lines", bad[:5])
print(len(yaml.safe_load(t)["outcomes"]))
EOF
grep -c "—" attempts/burman-2023-01.yaml; grep -ci "rather" attempts/burman-2023-01.yaml
```

```
Exit code 1
35
suspect lines []
35
0
0
```

**Agent calls Bash**

```bash
sed -n 1,60p attempts/burman-2023-01.yaml
```

```
Exit code 2
sed: can't read attempts/burman-2023-01.yaml: No such file or directory
```

**Agent calls Bash**

```bash
cd  ls executed/burman-2023/attempts 2>/dev/null; sed -n 1,50p attempts/burman-2023-01.yaml
```

```
schema_version: 3
id: burman-2023-01
datasets:
- archive: dandi
  id: 000458
  version: 0.230317.0039
  doi: 10.48324/dandi.000458/0.230317.0039
  relation: reuses
paper: doi:10.1016/j.neuron.2023.08.005
date: '2026-11-10'
entry: burman-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/^  id: 000458$/  id: "000458"/' attempts/burman-2023-01.yaml && python -c "import yaml;print(repr(yaml.safe_load(open('attempts/burman-2023-01.yaml'))['datasets'][0]['id']))" && python tools/entry.py check entries/burman-2023 2>&1 | tail -5
```

```
'000458'
0 error(s)
```

**Agent calls Write**

```json
{
 "file_path": "entries/burman-2023/README.md",
 "content": "# Burman, Brodersen, Raimondo, Sen & Akerman (2023) on dandiset 000458\n\nTests the findings of [Burman et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.005) that can\nbe tested on [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), the Allen\nInstitute Neuropixels recordings with cortical electrical stimulation, awake and under isoflurane,\nthat the paper reuses (Figure 4A to 4D, Figure S6), and runs the paper's network model (Figure 4E\nto 4H, Figure S7). The paper's gramicidin patch-clamp recordings (Figures 1 to 3) are not in the\ndandiset nor deposited anywhere.\n\n| Claim | Outcome |\n|---|---|\n| The 17 sessions the paper's code reads are in the dandiset with the fields it uses | Reproduced |\n| 662 neurons kept and 203 excluded, from 17 recordings in 16 mice | Partially reproduced |\n| Synchrony lower awake (0.325 against 0.393) | Partially reproduced |\n| Entropy higher awake (1.347 against 1.111 nats) | Partially reproduced |\n| Evoked firing rate higher awake | Reproduced |\n| Synchrony and entropy differences remain with firing rate regressed out | Reproduced |\n| Model: hyperpolarizing E_GABA gives less activity | Reproduced |\n| Model: synchrony lower with shunting E_GABA (0.784 against 0.881) | Partially reproduced |\n| Model: entropy higher with shunting E_GABA (0.451 against 0.197 nats) | Partially reproduced |\n| Model: shunting networks decoded more accurately | Reproduced |\n| Multi-compartment model of Figure S4 | Blocked: other |\n| Patch-clamp findings of Figures 1 to 3 and S1 to S5 (24 claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe three partial outcomes on the dandiset come from the evoked rate used to exclude neurons. The\nclaims are judged under the Methods' rate, a spike count; under the rate the paper's own code\ncomputes, which sums spike latencies, the dandiset gives the paper's numbers exactly. The two\npartial model outcomes are hyperpolarizing means 0.001 to 0.002 outside tolerances narrower than\nthe spread between runs. The attempt record, with the reasons and the differences from the paper's\nmethod, is [`attempts/burman-2023-01.yaml`](../../attempts/burman-2023-01.yaml).\n\n- `reproduce_burman_2023.ipynb`: the Neuropixels claims. About two minutes, most of it streaming the\n  units and trials of 24 files.\n- `network_model.ipynb`: 20 runs of the paper's network model on four processes, about 35 minutes.\n- `npx.py`: loading the dandiset and the per-unit measures (rate, entropy, synchrony) of the paper's\n  code. Other notebooks on this dandiset can import it.\n- `network.py`: the paper's Brian 2 network, transcribed from its simulation code.\n"
}
```

```
File created successfully at: entries/burman-2023/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n "methods_underspecified" $TMPDIR/w/build_nb1.py && sed -i 's/| figs4-intrinsic-properties | blocked: methods_underspecified |/| figs4-intrinsic-properties | blocked: other (the Figure S4 measure is in the unsupplied supplement; Matlab analysis) |/' $TMPDIR/w/build_nb1.py && sed -i 's/(reading A1, first file read again for the shifted windows)/(reading A1). The shifted windows need spikes away from the pulses, read below for two files./' $TMPDIR/w/build_nb1.py && python $TMPDIR/w/build_nb1.py && grep -c "blocked: other" entries/burman-2023/reproduce_burman_2023.ipynb && date -u && time python tools/entry.py all entries/burman-2023 2>&1 | tail -4; date -u
```

```
42:| figs4-intrinsic-properties | blocked: methods_underspecified |
499:| figs4-intrinsic-properties | blocked: methods_underspecified |
2
Tue Nov 10 06:46:33 UTC 2026
Installed kernelspec registry-burman-2023 in executed/burman-2023/.venv/share/jupyter/kernels/registry-burman-2023
0 error(s)
pass  reproduce_burman_2023.ipynb  (123 s)
pass  network_model.ipynb  (1903 s)

real	33m55.111s
user	112m33.042s
sys	0m20.302s
Tue Nov 10 07:20:28 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/burman-2023 && python -c "
import json
for f in ['reproduce_burman_2023.ipynb','network_model.ipynb']:
    nb=json.load(open(f))
    for c in nb['cells']:
        for o in c.get('outputs',[]):
            if o.get('output_type')=='error': print('ERROR', f)
            t=''.join(o.get('text',''))
            for line in t.splitlines():
                if any(k in line for k in ['unrounded','  shunting 0.','D1','A1F1                           865','mean accuracy']): print(f[:5], line[:150])
"; cd  && python tools/entry.py handover entries/burman-2023 && ls executed/burman-2023/handover && git status --short
```

```
repro A1F1                           865   721       144          143            1          17    16    37.0    7   95
repro A1F1 unrounded: awake 0.31885, isoflurane 0.38624, p = 1.45e-32
netwo   shunting 0.7833 +- 0.0005 (SEM), hyperpolarizing 0.8789 +- 0.0006
netwo   shunting 0.4516 +- 0.0020 (SEM), hyperpolarizing 0.2014 +- 0.0019
netwo mean accuracy shunting 0.9848, hyperpolarizing 0.9315 (chance 0.01)
netwo D1 paired t = 16.92, p = 6.52e-13
wrote executed/burman-2023/handover
burman-2023.yaml
network.py
network_model.ipynb
npx.py
reproduce_burman_2023.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/burman-2023/; date -u
```

```
total 224
drwxr-xr-x   4 runner runner   4096 Nov 10 06:46 .
drwxr-xr-x 250 runner runner  12288 Nov 10 05:19 ..
drwxr-xr-x   3 runner runner   4096 Nov 10 05:21 .claude
-rw-r--r--   1 runner runner   2755 Nov 10 06:46 README.md
drwxr-xr-x   2 runner runner   4096 Nov 10 05:33 __pycache__
-rw-r--r--   1 runner runner   1083 Nov 10 06:07 entry.yaml
-rw-r--r--   1 runner runner  12171 Nov 10 05:33 network.py
-rw-r--r--   1 runner runner  15878 Nov 10 06:07 network_model.ipynb
-rw-r--r--   1 runner runner  14858 Nov 10 05:30 npx.py
-rw-r--r--   1 runner runner  36073 Nov 10 06:46 reproduce_burman_2023.ipynb
-rw-r--r--   1 runner runner    102 Nov 10 06:07 requirements.in
-rw-r--r--   1 runner runner 110073 Nov 10 06:07 requirements.lock.txt
Tue Nov 10 07:20:55 UTC 2026
```

**Agent calls Bash**

```bash
find entries/burman-2023/.claude | head; rm -rf entries/burman-2023/__pycache__
```

```
entries/burman-2023/.claude
entries/burman-2023/.claude/.cc-writes
```

**Agent**

I've done steps 1 to 6 of the Author section and built the handover. The entry ran from a clean environment with 0 check errors: the Neuropixels notebook in 123 s and the model notebook in 1903 s. Nothing was committed.

The main result is that the dandiset gives the paper's Figure 4 numbers exactly, but only under the firing rate the paper's own code computes, not the one its Methods describe. The claims file judges each claim under the Methods' rate, so three claims that would otherwise reproduce are partial.

## 1. Outcomes (35 claims)

| Claim | Outcome |
|---|---|
| dataset-sessions-link | reproduced |
| fig4c-sample | partially reproduced: 721 kept and 144 excluded against 662 and 203; exact under the code's rate |
| fig4d-synchrony-lower-awake | partially reproduced: 0.3188 awake (just outside 0.325 ± 0.005) and 0.3862 isoflurane, p = 1.45e-32; exact under the code's rate |
| fig4d-entropy-higher-awake | partially reproduced: 1.389 and 1.150 nats, both outside tolerance, p = 3.3e-30; exact under the code's rate |
| fig4-rate-higher-awake | reproduced (14.0 against 7.6 Hz) |
| figs6-rate-regressed | reproduced: all three regression readings agree, every p below 1e-10 |
| fig4f-model-hyperpolarizing-less-activity | reproduced |
| fig4h-model-synchrony | partially reproduced: 0.7833 and 0.8789; the hyperpolarizing mean is 0.0011 outside tolerance |
| fig4h-model-entropy | partially reproduced: 0.4516 and 0.2014; the hyperpolarizing mean is 0.0024 outside tolerance |
| figs7-model-decoding | reproduced: 0.985 against 0.932, shunting higher in 20 of 20 runs |
| figs4-intrinsic-properties | blocked, `other` |
| 24 patch-clamp claims | blocked, `data_missing` |

## 2. Dataset, assumptions and questions

**What the dataset holds.**
- **Version pinned.** 0.230317.0039 is the only published version and the one the paper's code names. The draft has the same assets.
- **The paper's recordings are all there.** All 17 recordings (16 mice) are present with every field the analysis needs.
  - Unit ids equal row numbers, so the code's keying of units by row selects the right units.
  - Labels and clocks are consistent with the data: evoked spiking is 3 to 18 times the spiking in time-shifted windows, and the isoflurane trials fall inside the isoflurane epoch.
  - There are no duplicate files.
- **Code mismatch on the firing rate.** The paper's code sums spike latencies where the Methods describe an average firing rate. That rate gives exactly 662 kept, 203 excluded, a median of 34 per recording (1 to 93), and the Figure 4D means. Its 200 Hz exclusion bound therefore acts on spike-count rates near 45 Hz.
- **Undocumented selection.** One file with units and stimulation, sub-599017, is in the version but not used by the paper, and the paper does not say why. Six other files hold EEG only.
- **Missing data.** The patch-clamp recordings (Figures 1 to 3, S1 to S5) are not deposited anywhere. A DANDI search for gramicidin, Akerman, Burman and EGABA found nothing.
- **Minor code mismatch.** The waveform cut (≥ against > 0.4 ms) and the area rule differ between the Methods and the code, but select the same 865 units here.

**Assumptions:** none (no outcome is marked `assumed`). The Figure S6 regression method is open, but all three readings in the criterion agree.

**Questions for the paper's authors:** none filed. **Questions to a reader:** none. The claims file follows the Methods, as the protocol requires; it does not misread the paper.

## 3. Protocol gaps

1. There is no block reason for a claim whose method lives only in a supplement that was not supplied (Figure S4, which also needs Matlab). I used `other` and explained it in the notes.
2. The protocol makes the Methods reading decide the outcome even when the code's reading reproduces the paper exactly. I followed it, recorded the code mismatch as a finding, and showed the code's reading as a variant.
3. "Fix every random seed" conflicts with the model criterion's "seeds as given by the gist (none set)". I fixed seeds 1 to 20 and recorded it as a deviation.
4. The paper's simulation builds a 4 GB stimulus array that does not fit in memory, and the protocol says nothing about changing an outside input's code. I held one periodic stimulus set instead, showed it gives identical spikes on a small run, and recorded the change.
5. For stochastic simulations, the paper's SEM over pooled neurons is narrower than the spread between seeds, and the protocol has no rule for this. I applied the criterion as written, so the two model claims are partial, and noted the spread.
6. The clock-check guidance (decoding a task variable around trial starts) is heavier than needed here. I used a shifted-window contrast on two files at full length.
7. `entry.py check` requires every notebook to name the dataset, including the simulation-only one, so that notebook imports the version constant from the helper.

## 4. Runtime and failures

- **Runtime.** The agent run took about 2 h 10 min (05:13 to 07:21 UTC). The entry was run in full twice, about 35 min each; the second run came after correcting the Figure S4 block reason in the notebook text.
- **Failures.**
  - A first parallel test with 2 repeats failed because 5-fold cross-validation needs at least 5 repeats; I re-ran with 5.
  - The loader first crashed on the six files with no units table; it now handles them.
  - Nothing failed in the final run.
- **Files I did not create.** `git status` shows untracked dotfiles at the repo root (.bashrc, .gitconfig, .vscode and others), a `scripts/` folder, and an `entries/burman-2023/.claude/` folder. I left them alone; `.claude/` looks like a harness file, so you may want to exclude it from the commit.

Files are in `entries/burman-2023/`:
- `reproduce_burman_2023.ipynb`
- `network_model.ipynb`
- `npx.py`
- `network.py`
- `README.md`

The attempt record is `attempts/burman-2023-01.yaml`.

## End of run

54 turns, 128 minutes, $4.83 at API prices, result: success.
