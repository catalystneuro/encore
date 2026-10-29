# 000140 · author · run 40791667840

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8d8084f7-032e-4565-b0ce-d90724fccdfd/tool-results/bmuaz4ny6.txt

Preview (first 2KB):
Thu Oct 29 00:07:20 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8d8084f7-032e-4565-b0ce-d90724fccdfd/tool-results/bmuaz4ny6.txt"
}
```

```
1	Thu Oct 29 00:07:20 UTC 2026
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
ls claims/000140 paper entries/001453-fouke-2025 questions | head -50; cat claims/000140/*.yaml; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md docs/archives.md
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
[... 122 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000140/10.1016-j.neuron.2010.09.015.yaml"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000140.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol as stated in docs/protocol.md.
4	#
5	# Text read: the NIH author manuscript in PubMed Central (PMC2991102), not the version of record,
6	# as extracted to paper/10.1016-j.neuron.2010.09.015.txt: Summary, Results, Discussion, Methods,
7	# figure legends, and its one supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1
8	# to 5 with legends, Supplemental Text, Supplemental Experimental Procedures). The figures are not
9	# in the text; values shown only in Figures 4, 6 and 7 are not stated and no expected value is
10	# taken from them. The paper links no code, so every method below comes from the Methods, the
11	# legends or the supplement. The archive also lists doi:10.1038/nature11129 for this dandiset;
12	# these claims are for the 2010 paper only.
13	#
14	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
15	# Procedures). Three adult male rhesus monkeys (A, B, J, about 10 kg) made delayed reaches on a
16	# fronto-parallel screen from a central touch spot to a target. Events per trial: target onset
17	# (the target jitters), go cue (jitter stops, touch spot disappears), movement onset. Delays about
18	# 0 to 1000 ms; only trials with delays above 400 ms analysed. Hand tracked at 60 Hz, eye at
19	# 240 Hz. Four datasets:
20	#   monkeys A and B, speed task, 28 conditions (7 directions, 2 distances, 2 instructed speeds),
[... 473 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,140p docs/archives.md
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
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 6000 omr.py; cat ../../attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (43.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8d8084f7-032e-4565-b0ce-d90724fccdfd/tool-results/b6i20l53k.txt

Preview (first 2KB):
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
[... 31 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8d8084f7-032e-4565-b0ce-d90724fccdfd/tool-results/b6i20l53k.txt"
}
```

```
1	schema_version: 1
2	name: 001453-fouke-2025
3	type: reproduction
4	title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
5	description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
6	  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
7	  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
8	  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
9	  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
10	license: Apache-2.0
11	notebooks:
12	- path: reproduce_fouke_2025.ipynb
13	  title: Reproducing Fouke et al. (2025) from dandiset 001453
14	  runtime_minutes: 6
15	helpers:
16	- omr.py
17	related:
18	- id: dandi:001453/0.250518.1950
19	  relation: uses_data
20	- id: doi:10.1016/j.cub.2025.04.027
[... 774 more lines not kept]
```

**Agent calls Bash**

```bash
cd  curl -s https://api.dandiarchive.org/api/dandisets/000140/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000140/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000140/versions/0.220113.0408/ | python -m json.tool | head -150; curl -s https://api.dandiarchive.org/api/dandisets/000140/versions/0.220113.0408/assets/ | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000140/versions/0.220113.0408/ | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d[k] for k in d if k in ('relatedResource','assetsSummary','ethicsApproval','wasGeneratedBy')},indent=1))" | sed -n 1,200p | grep -v schemaKey; python -c "import h5py, remfile, pynwb, numpy, scipy, sklearn; print('ok')"; which uv
```

Result: the fetched text is not kept.

**Agent**

Let me set up a scratch env and open the files.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q scratch && . scratch/bin/activate && uv pip install -q h5py remfile pynwb numpy scipy matplotlib dandi pandas scikit-learn nbformat pyyaml 2>&1 | tail -3; python -c "import h5py,remfile,pynwb;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/survey.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset("000140","0.220113.0408")
    assets=[(a.path,a.get_content_url(follow_redirects=1,strip_query=True)) for a in ds.get_assets()]
for p,u in assets:
    print("=====",p,u)
    f=h5py.File(remfile.File(u),"r")
    def v(name,obj):
        if isinstance(obj,h5py.Dataset):
            s=f"{name} {obj.shape} {obj.dtype}"
            if obj.size<=3 or obj.dtype.kind in 'SO' and obj.size<5: s+=f" {obj[()]}"
            a={k:obj.attrs[k] for k in obj.attrs if k in ('unit','description','conversion','resolution','rate','starting_time')}
            print(s,a)
        else:
            a={k:obj.attrs[k] for k in obj.attrs if k in ('description','neurodata_type','colnames')}
            print(name+"/",a)
    f.visititems(v)
EOF
python $TMPDIR/survey.py 2>&1 | head -200
```

```
<persisted-output>
Output too large (281.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8d8084f7-032e-4565-b0ce-d90724fccdfd/tool-results/bejzytvs2.txt

Preview (first 2KB):
===== sub-Jenkins/sub-Jenkins_ses-small_desc-test_ecephys.nwb https://dandiarchive.s3.amazonaws.com/blobs/118/a0f/118a0fea-39e2-4e85-b01d-a72df466f266
acquisition/ {}
analysis/ {}
file_create_date (1,) object [b'2021-09-01T22:14:15.160313-04:00'] {}
general/ {}
general/devices/ {}
general/devices/electrode_array_M1/ {'description': '96-electrode Utah array in M1', 'neurodata_type': 'Device'}
general/devices/electrode_array_PMd/ {'description': '96-electrode Utah array in PMd', 'neurodata_type': 'Device'}
general/experiment_description () object b'Center-out delayed reaching task with maze barriers' {}
general/experimenter (2,) object [b'Mark M. Churchland' b'Matthew T. Kaufman'] {}
general/extracellular_ephys/ {}
general/extracellular_ephys/electrode_group_M1/ {'description': 'Electrodes in an implanted Utah array in M1', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrode_group_PMd/ {'description': 'Electrodes in implanted Utah Array in PMd', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name'], dtype=object), 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (192,) object {'description': 'description of hardware filtering'}
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "spike_times\b" /home/runner/.claude/projects/-home-runner-work-encore-encore/8d8084f7-032e-4565-b0ce-d90724fccdfd/tool-results/bejzytvs2.txt | cut -c1-300 | awk 'length<400' | head -150
```

```
===== sub-Jenkins/sub-Jenkins_ses-small_desc-test_ecephys.nwb https://dandiarchive.s3.amazonaws.com/blobs/118/a0f/118a0fea-39e2-4e85-b01d-a72df466f266
acquisition/ {}
analysis/ {}
file_create_date (1,) object [b'2021-09-01T22:14:15.160313-04:00'] {}
general/ {}
general/devices/ {}
general/devices/electrode_array_M1/ {'description': '96-electrode Utah array in M1', 'neurodata_type': 'Device'}
general/devices/electrode_array_PMd/ {'description': '96-electrode Utah array in PMd', 'neurodata_type': 'Device'}
general/experiment_description () object b'Center-out delayed reaching task with maze barriers' {}
general/experimenter (2,) object [b'Mark M. Churchland' b'Matthew T. Kaufman'] {}
general/extracellular_ephys/ {}
general/extracellular_ephys/electrode_group_M1/ {'description': 'Electrodes in an implanted Utah array in M1', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrode_group_PMd/ {'description': 'Electrodes in implanted Utah Array in PMd', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name'], dtype=object), 'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (192,) object {'description': 'description of hardware filtering'}
general/extracellular_ephys/electrodes/group (192,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of'}
general/extracellular_ephys/electrodes/group_name (192,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of'}
general/extracellular_ephys/electrodes/id (192,) int64 {}
general/extracellular_ephys/electrodes/imp (192,) float64 {'description': 'the impedance of the channel'}
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "spike_times\b" /home/runner/.claude/projects/-home-runner-work-encore-encore/8d8084f7-032e-4565-b0ce-d90724fccdfd/tool-results/bejzytvs2.txt | cut -c1-300 | awk 'length<400' | sed -n 150,400p | grep -v specifications
```

```
processing/behavior/eye_pos/data (287710, 2) float64 {'conversion': np.float64(0.001), 'resolution': np.float64(-1.0), 'unit': 'meters'}
processing/behavior/eye_pos/reference_frame () object b'(0, 0) is screen center' {}
processing/behavior/eye_pos/timestamps (287710,) float64 {'unit': 'seconds'}
processing/behavior/hand_pos/ {'description': 'Monkey hand position in mm. First column x, second column y', 'neurodata_type': 'SpatialSeries'}
processing/behavior/hand_pos/data (287710, 2) float64 {'conversion': np.float64(0.001), 'resolution': np.float64(-1.0), 'unit': 'meters'}
processing/behavior/hand_pos/reference_frame () object b'(0, 0) is screen center' {}
processing/behavior/hand_pos/timestamps (287710,) float64 {'unit': 'seconds'}
processing/behavior/hand_vel/ {'description': 'Monkey hand velocity in mm/s, calculated from monkey hand position. First column x, second column y', 'neurodata_type': 'TimeSeries'}
processing/behavior/hand_vel/data (287710, 2) float64 {'conversion': np.float64(0.001), 'resolution': np.float64(-1.0), 'unit': 'm/s'}
processing/behavior/hand_vel/timestamps (287710,) float64 {'unit': 'seconds'}
session_description () object b'Data from monkey Jenkins performing center-out delayed reaching task. This file contains trials from the full session on 2009-09-28 that can be used for training models for the Neural Latents Benchmark.' {}
session_start_time () object b'2009-09-28T00:00:00-07:00' {}
stimulus/ {}
stimulus/presentation/ {}
stimulus/templates/ {}
timestamps_reference_time () object b'2009-09-28T00:00:00-07:00' {}
      dtype=object), 'description': 'data on spiking units', 'neurodata_type': 'Units'}
units/electrodes (142,) int64 {'description': 'the electrodes that each spike unit came from'}
units/electrodes_index (142,) uint8 {'description': "Index for VectorData 'electrodes'"}
```

**Agent calls Bash**

```bash
grep -n "units/" /home/runner/.claude/projects/-home-runner-work-encore-encore/8d8084f7-032e-4565-b0ce-d90724fccdfd/tool-results/bejzytvs2.txt | cut -c1-250
```

```
77:units/ {'colnames': array(['heldout', 'spike_times', 'obs_intervals', 'electrodes'],
79:units/electrodes (107,) int64 {'description': 'the electrodes that each spike unit came from'}
80:units/electrodes_index (107,) uint8 {'description': "Index for VectorData 'electrodes'"}
81:units/heldout (107,) bool {'description': 'Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark'}
82:units/id (107,) int64 {}
83:units/obs_intervals (10700, 2) float64 {'description': 'the observation intervals for each unit'}
84:units/obs_intervals_index (107,) uint16 {'description': "Index for VectorData 'obs_intervals'"}
85:units/spike_times (32897,) float64 {'description': 'the spike times for each unit'}
86:units/spike_times_index (107,) uint16 {'description': "Index for VectorData 'spike_times'"}
197:units/ {'colnames': array(['heldout', 'spike_times', 'obs_intervals', 'electrodes'],
199:units/electrodes (142,) int64 {'description': 'the electrodes that each spike unit came from'}
200:units/electrodes_index (142,) uint8 {'description': "Index for VectorData 'electrodes'"}
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/look.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd
U="https://dandiarchive.s3.amazonaws.com/blobs/7f4/e60/7f4e60f3-2184-4e68-ace1-504a2e564939"
f=h5py.File(remfile.File(U),"r")
T=f["intervals/trials"]
d={k:T[k][()] for k in ['start_time','stop_time','trial_type','trial_version','maze_id','success','target_on_time','go_cue_time','move_onset_time','rt','delay','num_targets','num_barriers','active_target','split']}
d['split']=[s.decode() if isinstance(s,bytes) else s for s in d['split']]
df=pd.DataFrame(d); pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
print(df.head(20)); print(df.describe().T)
print(df.groupby(['maze_id','trial_version']).size().to_string())
print("n conditions", df.groupby(['trial_type','trial_version']).ngroups, df.maze_id.nunique(), df.trial_type.nunique())
print(df.split.value_counts())
tp=T['target_pos'][()]; ti=T['target_pos_index'][()]
print(tp[:10], ti[:10])
E=f["general/extracellular_ephys/electrodes"]
for k in ['x','y','z','imp']: v=E[k][()]; print(k, v[:5], np.unique(v)[:10], len(np.unique(v)))
print(np.unique(E['location'][()]), np.unique(E['group_name'][()]), np.unique(E['filtering'][()]))
U_=f['units']; el=U_['electrodes'][()]; print('unit electrodes', el[:20], len(np.unique(el))); print(U_['electrodes_index'][()][:10])
print('heldout', U_['heldout'][()].sum())
oi=U_['obs_intervals'][()]; oii=U_['obs_intervals_index'][()]; print(oi[:3], oii[:5], oi.shape)
st=U_['spike_times'][()]; sti=U_['spike_times_index'][()]; print(st.shape, st[:5], st.max())
hp=f['processing/behavior/hand_pos/timestamps'][()]; print(hp[:5], np.diff(hp)[:5], hp[-1], np.unique(np.round(np.diff(hp),5))[:10])
EOF
python $TMPDIR/look.py
```

```
start_time  stop_time  trial_type  ...  num_barriers  active_target  split
0          0.0      3.421          11  ...             9              0    val
1          3.5      5.631          12  ...             0              0  train
2          5.7      8.536           4  ...             9              0  train
3          8.6     11.746           8  ...             9              1    val
4         11.8     14.706           7  ...             9              0  train
5         14.8     17.551           4  ...             9              0    val
6         17.6     20.626           8  ...             9              1  train
7         20.7     23.651           7  ...             0              0  train
8         23.7     26.971           6  ...             9              0    val
9         27.0     29.641           3  ...             9              0  train
10        29.7     33.036          10  ...             9              0  train
11        33.1     36.226           8  ...             0              0  train
12        36.3     39.276           7  ...             0              0    val
13        39.3     41.656           3  ...             9              0  train
14        41.7     44.661           2  ...             0              0  train
15        44.7     47.691          10  ...             9              0  train
16        47.8     50.581           4  ...             0              0  train
17        50.6     53.631           7  ...             9              0  train
18        53.7     56.956           3  ...             9              1  train
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
wc -w paper/*.txt; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2010.09.015.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1016-j.neuron.2010.09.015.txt').read()
i=58000
print(s[i:i+6000])
print('#####')
j=s.find('Supplemental Experimental Procedures',i); print(j, len(s))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1016-j.neuron.2010.09.015.txt').read()
i=s.find('Wise SP',60000)
k=s.find('Supplement',i-2000)
print(s[k-500:])
" | head -c 40000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/look2.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd
U="https://dandiarchive.s3.amazonaws.com/blobs/7f4/e60/7f4e60f3-2184-4e68-ace1-504a2e564939"
UT="https://dandiarchive.s3.amazonaws.com/blobs/118/a0f/118a0fea-39e2-4e85-b01d-a72df466f266"
f=h5py.File(remfile.File(U),"r"); T=f["intervals/trials"]
g={k:T[k][()] for k in ['start_time','stop_time','target_on_time','go_cue_time','move_onset_time','rt','delay','num_targets','num_barriers','trial_version']}
df=pd.DataFrame(g)
print((df.target_on_time-df.start_time).describe()); print((df.stop_time-df.move_onset_time).describe())
print(((df.go_cue_time-df.target_on_time)*1000-df.delay).describe()); print(((df.move_onset_time-df.go_cue_time)*1000-df.rt).describe())
print(df.delay.describe(), (df.delay<=400).sum()); print(df.rt.describe())
print(pd.crosstab(df.trial_version,[df.num_targets,df.num_barriers]))
el=f['units/electrodes'][()]; gn=f['general/extracellular_ephys/electrodes/group_name'][()]
print(pd.Series(gn[el]).value_counts()); print('heldout by array', pd.crosstab(gn[el], f['units/heldout'][()]))
oi=f['units/obs_intervals'][()]; print('obs equal trials', np.allclose(oi.reshape(142,100,2)[0], np.c_[df.start_time,df.stop_time]), np.allclose(oi.reshape(142,100,2), oi.reshape(142,100,2)[0:1]))
st=f['units/spike_times'][()]; sti=f['units/spike_times_index'][()]
print('sorted', all(np.all(np.diff(s)>=0) for s in np.split(st,sti[:-1])))
# test file
ft=h5py.File(remfile.File(UT),"r"); Tt=ft['intervals/trials']
print('test start', Tt['start_time'][:5], Tt['stop_time'][:5], Tt['move_onset_time'][:5])
print(np.unique([s.decode() for s in Tt['split'][()]],return_counts=True))
print('test units heldout', ft['units/heldout'][()].sum(), ft['units/electrodes'][()][:10], el[:10])
stt=ft['units/spike_times'][()]; print('test spikes',stt.shape, stt.min(), stt.max())
# time ranges overlap?
print('train range', df.start_time.min(), df.stop_time.max(), 'test range', Tt['start_time'][()].min(), Tt['stop_time'][()].max())
hp=f['processing/behavior/hand_pos/data'][()]; hv=f['processing/behavior/hand_vel/data'][()]; ts=f['processing/behavior/hand_pos/timestamps'][()]
print('hand pos range', np.nanmin(hp,0), np.nanmax(hp,0), 'nan', np.isnan(hp).sum()); print('vel range', np.nanpercentile(hv,[0.1,99.9],axis=0))
print('ts diffs', pd.Series(np.round(np.diff(ts),3)).value_counts().head())
print([ (k, ft['processing'].keys()) for k in [0]])
EOF
python $TMPDIR/look2.py
```

```
count    100.000000
mean       0.800660
std        0.083843
min        0.659000
25%        0.740500
50%        0.794000
75%        0.864250
max        0.952000
dtype: float64
count    100.000000
mean       1.141730
std        0.105858
min        0.979000
25%        1.065000
50%        1.138000
75%        1.187250
max        1.626000
dtype: float64
count    1.000000e+02
mean    -1.364526e-12
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/look3.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd
U="https://dandiarchive.s3.amazonaws.com/blobs/7f4/e60/7f4e60f3-2184-4e68-ace1-504a2e564939"
f=h5py.File(remfile.File(U),"r"); T=f["intervals/trials"]
E=f['general/extracellular_ephys/electrodes']
gn=np.array([x.decode() for x in E['group_name'][()]]); loc=np.array([x.decode() for x in E['location'][()]]); ids=E['id'][()]
print(ids[:5], ids[90:100], ids[-3:]); print(gn[:3], gn[95:98], gn[-3:]); print(loc[:3], loc[95:98], loc[-3:])
print(pd.crosstab(gn,loc))
el=f['units/electrodes'][()]; print('unit electrode idx range', el.min(), el.max(), np.bincount(el)[:10])
print(f['units/id'][()][:10])
df=pd.DataFrame({k:T[k][()] for k in ['maze_id','trial_version','delay']})
df=df[df.delay>400]; c=df.groupby(['maze_id','trial_version']).size(); print(c.to_string()); print(len(c), c.min())
EOF
python $TMPDIR/look3.py
```

```
[1 2 3 4 5] [ 91  92  93  94  95  96  97  98  99 100] [190 191 192]
['electrode_group_PMd' 'electrode_group_PMd' 'electrode_group_PMd'] ['electrode_group_PMd' 'electrode_group_M1' 'electrode_group_M1'] ['electrode_group_M1' 'electrode_group_M1' 'electrode_group_M1']
['PMd' 'PMd' 'PMd'] ['PMd' 'M1' 'M1'] ['M1' 'M1' 'M1']
col_0                M1  PMd
row_0                       
electrode_group_M1   96    0
electrode_group_PMd   0   96
unit electrode idx range 0 94 [2 3 2 1 0 2 2 0 2 1]
[1011 1012 1021 1022 1031 1032 1041 1061 1062 1071]
maze_id  trial_version
2        0                2
         1                3
         2                4
3        0                3
         1                3
         2                3
4        0                3
         1                2
         2                2
7        0                4
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; python -c "
import h5py, remfile, numpy as np
f=h5py.File(remfile.File('https://dandiarchive.s3.amazonaws.com/blobs/7f4/e60/7f4e60f3-2184-4e68-ace1-504a2e564939'),'r')
ids=f['units/id'][()]; el=f['units/electrodes'][()]
for i,e in zip(ids,el): print(i,e,end='; ')
"
```

```
1011 0; 1012 0; 1021 1; 1022 1; 1031 2; 1032 2; 1041 3; 1061 5; 1062 5; 1071 6; 1072 6; 1091 8; 1092 8; 1101 9; 1131 12; 1141 13; 1151 14; 1152 14; 1161 15; 1163 15; 1171 16; 1172 16; 1181 17; 1191 18; 1201 19; 1203 19; 1211 20; 1221 21; 1222 21; 1241 23; 1242 23; 1251 24; 1252 24; 1253 24; 1261 25; 1271 26; 1291 28; 1292 28; 1331 32; 1341 33; 1342 33; 1361 35; 1362 35; 1371 36; 1391 38; 1401 39; 1431 42; 1441 43; 1471 46; 1472 46; 1501 49; 1502 49; 1511 50; 1541 53; 1581 57; 1601 59; 1651 64; 1671 66; 1702 69; 1711 70; 1721 71; 1731 72; 1741 73; 1751 74; 1801 79; 1821 81; 1831 82; 1851 84; 1871 86; 1881 87; 1891 88; 1901 89; 2021 1; 2131 12; 2132 12; 2151 14; 2181 17; 2201 19; 2202 19; 2231 22; 2232 22; 2251 24; 2271 26; 2272 26; 2281 27; 2301 29; 2302 29; 2311 30; 2312 30; 2331 32; 2341 33; 2351 34; 2352 34; 2361 35; 2371 36; 2381 37; 2391 38; 2392 38; 2401 39; 2412 40; 2421 41; 2461 45; 2471 46; 2481 47; 2491 48; 2501 49; 2521 51; 2522 51; 2541 53; 2542 53; 2571 56; 2601 59; 2621 61; 2622 61; 2631 62; 2641 63; 2671 66; 2681 67; 2691 68; 2701 69; 2711 70; 2721 71; 2722 71; 2731 72; 2732 72; 2733 72; 2741 73; 2751 74; 2761 75; 2762 75; 2771 76; 2772 76; 2791 78; 2792 78; 2801 79; 2802 79; 2812 80; 2821 81; 2841 83; 2842 83; 2861 85; 2951 94;
```

**Agent calls Bash**

```bash
date -u; ls tools; sed -n 1,60p schemas/attempt*.json 2>/dev/null | head -5; ls schemas
```

```
Thu Oct 29 00:10:48 UTC 2026
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
flagged.py
get_papers.sh
notify.py
paper_match.py
papers_manifest.py
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; python -c "
import h5py, remfile, numpy as np
f=h5py.File(remfile.File('https://dandiarchive.s3.amazonaws.com/blobs/7f4/e60/7f4e60f3-2184-4e68-ace1-504a2e564939'),'r')
p=f['processing/behavior/hand_pos/data'][5000:5100]; v=f['processing/behavior/hand_vel/data'][5000:5100]
print(np.round(p[:40,0],2)); print(np.round(v[:40,0],1))
d=np.diff(f['processing/behavior/hand_pos/data'][:50000,0]); print('frac zero diffs', np.mean(d==0))
"
```

```
[-71.78 -71.78 -71.79 -71.8  -71.81 -71.82 -71.83 -71.84 -71.84 -71.85
 -71.86 -71.87 -71.87 -71.88 -71.88 -71.89 -71.89 -71.9  -71.9  -71.9
 -71.9  -71.9  -71.91 -71.91 -71.91 -71.91 -71.91 -71.91 -71.91 -71.91
 -71.91 -71.91 -71.91 -71.91 -71.91 -71.91 -71.91 -71.91 -71.91 -71.91]
[-8.4 -8.6 -8.8 -8.9 -8.8 -8.8 -8.7 -8.3 -7.9 -7.5 -7.1 -6.5 -6.  -5.5
 -4.8 -4.3 -3.8 -3.2 -2.7 -2.2 -1.8 -1.4 -1.1 -0.8 -0.6 -0.4 -0.3 -0.3
 -0.3 -0.2 -0.2 -0.3 -0.4 -0.4 -0.5 -0.6 -0.6 -0.7 -0.6 -0.6]
frac zero diffs 2.000040000800016e-05
```

**Agent calls Bash**

```bash
mkdir -p entries/000140-churchland-2010; date -u
```

```
Thu Oct 29 00:11:47 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/000140-churchland-2010/maze_prep.py",
 "content": "\"\"\"Loading and measures for the maze-task array data of dandiset 000140 (MC_Maze_Small).\n\nChurchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68:387-400,\ndoi:10.1016/j.neuron.2010.09.015. Claims: claims/000140/10.1016-j.neuron.2010.09.015.yaml.\n\nThe train file holds 100 trials of monkey J (Jenkins) on 2009-09-28, 27 maze conditions\n(`maze_id` x `trial_version`), 142 units from two 96-electrode arrays, and hand position and\nvelocity at 1 kHz. The test file holds 100 segments of 0.7 s with no condition, go cue or\nbehaviour, so only the train file is used. Files are streamed; nothing is written to disk.\n\nWhere the parameters come from (C = the claim's criterion or the claims file header, which\ncite the paper; P = a passage of the paper taken by the author, step 1.6; A = an assumption;\nS = a standard choice for a detail that cannot change a result):\n\n- Delay > 400 ms (C; Methods, Task design and behavior).\n- Spike trains smoothed with a 20 ms Gaussian before averaging (C; Supplemental Experimental\n  Procedures, Computing the mean firing rate versus time). The width is taken as the SD (S).\n- Preparatory epoch -200 to +100 ms around the go cue; peri-movement epoch -100 to +350 ms\n  around movement onset (C; Methods, Correlations).\n- Inclusion > 5 spikes/s of preparatory tuning; peri-movement tuning >= 1.5 times it (C;\n  Methods). Tuning is the range (reading O1a) or SD (O1b) across conditions (C, header O1).\n- Movement onset: the dataset's `move_onset_time` (O3a) or the first time after the go cue\n  that hand speed reaches `ONSET_FRACTION` of the trial's peak (O3b) (C, header O3). The\n  fraction 0.15 is a common choice (A, shown with O3a).\n- Trial filter: velocity profiles correlated with a proto-trial at r > 0.9 (C; Supplemental\n  Experimental Procedures). Proto-trial readings O4a, O4b, O4c (C). The window of the profiles,\n  150 ms before to 800 ms after movement onset, is the peri-movement window (P; Methods,\n  PCA-based spaces) (S).\n- Peri-movement T matrix: condition means 150 ms before to 800 ms after movement onset\n  (maze task), all units but the fitted one, not normalised, columns mean-centred (C; Methods,\n  PCA-based spaces; Supplemental Text). Samples every 10 ms (C, header O5).\n- PD performance: leave-one-condition-out linear regression with offset; one minus the mean\n  squared prediction error over the variance across conditions (C; Methods, PD performance).\n  The variance is taken with ddof 0 (S).\n- Kinematic T matrix: horizontal and vertical position, velocity and acceleration from 150 ms\n  before movement onset to the end of the reach (600 or 800 ms, C), each variable scaled to\n  unity range across times and conditions (C; Methods). Acceleration is the time derivative of\n  the dataset's hand velocity after a 20 ms Gaussian (S).\n- Task spaces as the Methods list them (Task spaces). The reach ends at the last time within\n  800 ms of onset at which speed is at least `REACH_END_FRACTION` of its peak (A); the\n  maximum velocity component is the signed value of largest magnitude (A); segments are of\n  equal path length, with equal duration as a variant (A).\n- Upper limit of PD performance: PCA space of the c x n preparatory matrix (C; Supplemental\n  Experimental Procedures, Estimating the upper limit), here without the fitted unit, as for the\n  peri-movement space (A).\n- Array of a unit: the first digit of its id (1 or 2). The file's `units/electrodes` points every\n  unit to the PMd electrode group, and the electrodes table has no positions; unit ids\n  1xxx map to electrode index xx-1 of that table, which is the PMd group, so prefix 1 is read\n  as PMd and prefix 2 as M1 (A).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET_ID = \"000140\"\nDANDISET_VERSION = \"0.220113.0408\"\nTRAIN_PATH = \"sub-Jenkins/sub-Jenkins_ses-small_desc-train_behavior+ecephys.nwb\"\nTEST_PATH = \"sub-Jenkins/sub-Jenkins_ses-small_desc-test_ecephys.nwb\"\n\nMIN_DELAY_MS = 400\nSMOOTH_SD_MS = 20\nPREP_WIN = (-200, 100)        # ms re go cue\nPERI_WIN = (-100, 350)        # ms re movement onset\nT_WIN = (-150, 800)           # ms re movement onset, maze task\nSTEP_MS = 10\nGO_SPAN = (-300, 200)         # stored go-locked span, ms\nMV_SPAN = (-400, 900)         # stored movement-locked span, ms\nPREP_TUNING_MIN = 5.0         # spikes/s, array data\nPERI_RATIO_MIN = 1.5\nONSET_FRACTION = 0.15\nREACH_END_FRACTION = 0.10\nPROTO_R_MIN = 0.9\n\n\ndef asset_urls() -> dict:\n    \"\"\"Streaming URL of each NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)\n                for a in ds.get_assets()}\n\n\ndef _txt(v):\n    return v.decode() if isinstance(v, bytes) else str(v)\n\n\ndef load_train(url: str) -> dict:\n    \"\"\"Trials, units, spikes and hand kinematics of the train file.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        T = f[\"intervals/trials\"]\n        cols = [\"start_time\", \"stop_time\", \"trial_type\", \"trial_version\", \"maze_id\", \"success\",\n                \"target_on_time\", \"go_cue_time\", \"move_onset_time\", \"rt\", \"delay\",\n                \"num_targets\", \"num_barriers\", \"active_target\"]\n        trials = pd.DataFrame({c: T[c][()] for c in cols})\n        trials[\"split\"] = [_txt(s) for s in T[\"split\"][()]]\n        tp, tpi = T[\"target_pos\"][()], T[\"target_pos_index\"][()]\n        starts = np.r_[0, tpi[:-1]]\n        trials[\"target_x\"] = [tp[s + a, 0] for s, a in zip(starts, trials.active_target)]\n        trials[\"target_y\"] = [tp[s + a, 1] for s, a in zip(starts, trials.active_target)]\n        U = f[\"units\"]\n        ids = U[\"id\"][()]\n        st, sti = U[\"spike_times\"][()], U[\"spike_times_index\"][()]\n        spikes = np.split(st, sti[:-1])\n        E = f[\"general/extracellular_ephys/electrodes\"]\n        units = pd.DataFrame({\n            \"id\": ids,\n            \"electrode\": U[\"electrodes\"][()],\n            \"heldout\": U[\"heldout\"][()],\n        })\n        units[\"electrode_group\"] = [_txt(E[\"group_name\"][()][e]) for e in units.electrode]\n        units[\"array_prefix\"] = ids // 1000\n        units[\"channel\"] = (ids // 10) % 100\n        units[\"array\"] = np.where(units.array_prefix == 1, \"PMd\", \"M1\")\n        B = f[\"processing/behavior\"]\n        beh = {\"t\": B[\"hand_pos/timestamps\"][()], \"pos\": B[\"hand_pos/data\"][()],\n               \"vel\": B[\"hand_vel/data\"][()]}\n        meta = {\n            \"electrode_xyz_all_nan\": bool(np.all(np.isnan(np.c_[E[\"x\"][()], E[\"y\"][()], E[\"z\"][()]]))),\n            \"electrode_groups\": pd.Series([_txt(g) for g in E[\"group_name\"][()]]).value_counts().to_dict(),\n            \"pos_unit\": B[\"hand_pos/data\"].attrs[\"unit\"], \"pos_conversion\": float(B[\"hand_pos/data\"].attrs[\"conversion\"]),\n            \"vel_unit\": B[\"hand_vel/data\"].attrs[\"unit\"], \"vel_conversion\": float(B[\"hand_vel/data\"].attrs[\"conversion\"]),\n            \"pos_description\": _txt(B[\"hand_pos\"].attrs[\"description\"]),\n            \"vel_description\": _txt(B[\"hand_vel\"].attrs[\"description\"]),\n            \"session_start\": _txt(f[\"session_start_time\"][()]),\n            \"subject\": _txt(f[\"general/subject/subject_id\"][()]),\n            \"obs_intervals\": U[\"obs_intervals\"][()],\n        }\n    conds = trials[[\"maze_id\", \"trial_version\"]].drop_duplicates().sort_values([\"maze_id\", \"trial_version\"])\n    cmap = {tuple(r): i for i, r in enumerate(conds.values)}\n    trials[\"cond\"] = [cmap[(m, v)] for m, v in zip(trials.maze_id, trials.trial_version)]\n    return {\"trials\": trials, \"units\": units, \"spikes\": spikes, \"beh\": beh, \"meta\": meta,\n            \"conditions\": conds.reset_index(drop=True)}\n\n\ndef load_test(url: str) -> dict:\n    \"\"\"The test file: segment table, units and spikes (no conditions or behaviour).\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        T = f[\"intervals/trials\"]\n        trials = pd.DataFrame({c: T[c][()] for c in [\"start_time\", \"stop_time\", \"move_onset_time\"]})\n        U = f[\"units\"]\n        st, sti = U[\"spike_times\"][()], U[\"spike_times_index\"][()]\n        return {\"trials\": trials, \"ids\": U[\"id\"][()], \"spikes\": np.split(st, sti[:-1]),\n                \"heldout\": U[\"heldout\"][()], \"colnames\": [_txt(c) for c in T.attrs[\"colnames\"]],\n                \"has_behavior\": \"processing/behavior\" in f}\n\n\n# ---------------------------------------------------------------- kinematics per trial\n\ndef _trial_slice(beh, t0, t1):\n    i0, i1 = np.searchsorted(beh[\"t\"], [t0 - 1e-6, t1 + 1e-6])\n    return beh[\"t\"][i0:i1], beh[\"pos\"][i0:i1], beh[\"vel\"][i0:i1]\n\n\ndef speed_onset(beh, trial, fraction=ONSET_FRACTION) -> float:\n    \"\"\"O3b: first time after the go cue that hand speed reaches `fraction` of its trial peak.\"\"\"\n    t, _, v = _trial_slice(beh, trial.go_cue_time, trial.stop_time)\n    sp = np.hypot(v[:, 0], v[:, 1])\n    return float(t[np.argmax(sp >= fraction * sp.max())])\n\n\ndef trial_kinematics(beh, onset: float, span=MV_SPAN) -> dict:\n    \"\"\"Movement-locked position, velocity and acceleration at 1 ms (mm, mm/s, mm/s^2).\"\"\"\n    lags = np.arange(span[0], span[1] + 1) / 1000.0\n    t, p, v = _trial_slice(beh, onset + span[0] / 1000 - 0.05, onset + span[1] / 1000 + 0.05)\n    pos = np.c_[np.interp(onset + lags, t, p[:, 0]), np.interp(onset + lags, t, p[:, 1])]\n    vel = np.c_[np.interp(onset + lags, t, v[:, 0]), np.interp(onset + lags, t, v[:, 1])]\n    acc = np.gradient(gaussian_filter1d(vel, SMOOTH_SD_MS, axis=0), axis=0) * 1000.0\n    return {\"lags_ms\": np.arange(span[0], span[1] + 1), \"pos\": pos, \"vel\": vel, \"acc\": acc}\n\n\n# ---------------------------------------------------------------- rates per trial\n\ndef trial_rates(data: dict, onsets: np.ndarray, trial_idx) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Smoothed rates (spikes/s, float32) of every unit, go-locked over GO_SPAN and\n    movement-locked over MV_SPAN, for the given trials. Spikes are binned at 1 ms over the\n    whole trial and smoothed with a Gaussian of SD 20 ms before the windows are cut.\"\"\"\n    tr = data[\"trials\"]\n    n_units = len(data[\"spikes\"])\n    go_lags = np.arange(GO_SPAN[0], GO_SPAN[1] + 1)\n    mv_lags = np.arange(MV_SPAN[0], MV_SPAN[1] + 1)\n    R_go = np.zeros((len(trial_idx), n_units, len(go_lags)), np.float32)\n    R_mv = np.zeros((len(trial_idx), n_units, len(mv_lags)), np.float32)\n    for j, i in enumerate(trial_idx):\n        t0, t1 = tr.start_time.iat[i], tr.stop_time.iat[i]\n        nb = int(round((t1 - t0) * 1000))\n        counts = np.zeros((n_units, nb), np.float32)\n        for u, s in enumerate(data[\"spikes\"]):\n            s = s[(s >= t0) & (s < t1)]\n            b = np.minimum(((s - t0) * 1000).astype(int), nb - 1)\n            np.add.at(counts[u], b, 1.0)\n        rate = gaussian_filter1d(counts, SMOOTH_SD_MS, axis=1, mode=\"reflect\") * 1000.0\n        g = int(round((tr.go_cue_time.iat[i] - t0) * 1000))\n        m = int(round((onsets[i] - t0) * 1000))\n        R_go[j] = rate[:, g + go_lags]\n        R_mv[j] = rate[:, m + mv_lags]\n    return R_go, R_mv\n\n\n# ---------------------------------------------------------------- trial filter (O4)\n\ndef proto_filter(vel_profiles: np.ndarray, conds: np.ndarray, reading: str) -> np.ndarray:\n    \"\"\"Keep trials whose horizontal and vertical velocity profiles both correlate with the\n    condition's proto-trial at r > 0.9. reading 'a': the proto-trial is the trial best\n    correlated with the condition mean; 'b': the condition mean itself; 'c': no filter.\n    vel_profiles: trials x time x 2.\"\"\"\n    keep = np.ones(len(conds), bool)\n    if reading == \"c\":\n        return keep\n    for c in np.unique(conds):\n        idx = np.flatnonzero(conds == c)\n        if len(idx) < 2:\n            continue\n        V = vel_profiles[idx]\n        mean = V.mean(0)\n        r_mean = np.array([[np.corrcoef(v[:, d], mean[:, d])[0, 1] for d in (0, 1)] for v in V])\n        if reading == \"b\":\n            ok = np.all(r_mean > PROTO_R_MIN, axis=1)\n        else:\n            proto = V[np.argmax(r_mean.mean(1))]\n            r = np.array([[np.corrcoef(v[:, d], proto[:, d])[0, 1] for d in (0, 1)] for v in V])\n            ok = np.all(r > PROTO_R_MIN, axis=1)\n        keep[idx] = ok\n    return keep\n\n\ndef condition_means(X: np.ndarray, conds: np.ndarray, n_cond: int) -> np.ndarray:\n    \"\"\"Mean over trials of each condition, first axis trials.\"\"\"\n    return np.stack([X[conds == c].mean(0) for c in range(n_cond)])\n\n\n# ---------------------------------------------------------------- tuning and correlations\n\ndef epoch_mean(CM, lags, win):\n    sel = (lags >= win[0]) & (lags <= win[1])\n    return CM[..., sel].mean(-1)\n\n\ndef tuning(V: np.ndarray, measure: str) -> np.ndarray:\n    \"\"\"Across-condition tuning strength of each column of V (conditions first):\n    'range' (O1a) or 'sd' (O1b, ddof 0).\"\"\"\n    return np.ptp(V, axis=0) if measure == \"range\" else V.std(axis=0)\n\n\ndef peri_tuning(CM_mv, mv_lags, peri_rates, measure: str, reading: str) -> np.ndarray:\n    \"\"\"O2: (i) tuning of the peri-movement epoch means, (ii) the largest across-condition\n    tuning at any time from 100 ms before to 350 ms after movement onset.\"\"\"\n    if reading == \"i\":\n        return tuning(peri_rates, measure)\n    sel = (mv_lags >= PERI_WIN[0]) & (mv_lags <= PERI_WIN[1])\n    X = CM_mv[:, :, sel]\n    t = np.ptp(X, axis=0) if measure == \"range\" else X.std(axis=0)\n    return t.max(-1)\n\n\ndef rowwise_corr(A: np.ndarray, B: np.ndarray) -> np.ndarray:\n    \"\"\"Pearson r between matching columns of A and B (conditions x units).\"\"\"\n    a = A - A.mean(0)\n    b = B - B.mean(0)\n    return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))\n\n\n# ---------------------------------------------------------------- PD performance\n\ndef loo_performance(x: np.ndarray, S: np.ndarray) -> float:\n    \"\"\"Leave-one-condition-out performance of x ~ b0 + S b: one minus the mean squared\n    prediction error over the variance of x across conditions (Methods, PD performance).\n    Uses the closed form of the leave-one-out residual, e_i / (1 - h_ii).\"\"\"\n    X = np.c_[np.ones(len(x)), S]\n    H = X @ np.linalg.pinv(X)\n    h = np.diag(H)\n    if np.any(h > 1 - 1e-8):\n        return np.nan\n    press = (x - H @ x) / (1 - h)\n    return 1.0 - np.mean(press ** 2) / np.var(x)\n\n\ndef loo_performance_curve(x, scores, kmax):\n    return np.array([loo_performance(x, scores[:, :k]) for k in range(1, kmax + 1)])\n\n\ndef gram_scores(G: np.ndarray, kmax: int) -> np.ndarray:\n    \"\"\"PC scores (c x kmax) of a column-centred matrix from its c x c Gram matrix.\"\"\"\n    w, V = np.linalg.eigh(G)\n    order = np.argsort(w)[::-1][:kmax]\n    return V[:, order] * np.sqrt(np.clip(w[order], 0, None))\n\n\ndef leave_one_out_scores(blocks: np.ndarray, kmax: int, members=None) -> list[np.ndarray]:\n    \"\"\"For each unit j, the PC scores of the matrix of all other units' blocks.\n    blocks: conditions x units x features (each unit's columns of the T matrix).\n    members: optional boolean mask of units allowed in the space (others are left out).\"\"\"\n    c, n, _ = blocks.shape\n    Bc = blocks - blocks.mean(0, keepdims=True)\n    per_unit = np.einsum(\"aif,bif->iab\", Bc, Bc)         # n x c x c\n    if members is None:\n        members = np.ones(n, bool)\n    G = per_unit[members].sum(0)\n    out = []\n    for j in range(n):\n        Gj = G - per_unit[j] if members[j] else G\n        out.append(gram_scores(Gj, kmax))\n    return out\n\n\ndef pca_scores(M: np.ndarray, kmax: int) -> np.ndarray:\n    Mc = M - M.mean(0)\n    return gram_scores(Mc @ Mc.T, kmax)\n\n\ndef n_components_for(M: np.ndarray, frac=0.9) -> tuple[int, np.ndarray]:\n    Mc = M - M.mean(0)\n    s = np.linalg.svd(Mc, compute_uv=False)\n    ev = s ** 2 / np.sum(s ** 2)\n    return int(np.searchsorted(np.cumsum(ev), frac) + 1), ev\n\n\n# ---------------------------------------------------------------- kinematic and task spaces\n\ndef kinematic_matrix(KIN: dict, end_ms: int) -> np.ndarray:\n    \"\"\"c x (6 t) matrix of condition-mean x and y position, velocity and acceleration from\n    150 ms before onset to `end_ms`, every 10 ms, each variable scaled to unity range.\"\"\"\n    lags = KIN[\"lags_ms\"]\n    sel = (lags >= T_WIN[0]) & (lags <= end_ms) & ((lags - T_WIN[0]) % STEP_MS == 0)\n    cols = []\n    for key in (\"pos\", \"vel\", \"acc\"):\n        for d in (0, 1):\n            v = KIN[key][:, sel, d]\n            cols.append(v / np.ptp(v))\n    return np.concatenate(cols, axis=1)\n\n\ndef _resample_path(p, n_pts):\n    seg = np.r_[0, np.cumsum(np.hypot(*np.diff(p, axis=0).T))]\n    targets = np.linspace(0, seg[-1], n_pts)\n    return np.c_[np.interp(targets, seg, p[:, 0]), np.interp(targets, seg, p[:, 1])], seg\n\n\ndef task_features(kin: dict, segments: str = \"length\") -> dict:\n    \"\"\"Task-space features of one trial (Methods, Task spaces).\"\"\"\n    lags, pos, vel = kin[\"lags_ms\"], kin[\"pos\"], kin[\"vel\"]\n    sp = np.hypot(vel[:, 0], vel[:, 1])\n    after = (lags >= 0) & (lags <= 800)\n    i0 = np.flatnonzero(lags == 0)[0]\n    peak = sp[after].max()\n    above = np.flatnonzero(after & (sp >= REACH_END_FRACTION * peak))\n    i_end = above[-1]\n    path = pos[i0:i_end + 1]\n    start, end = path[0], path[-1]\n    d = end - start\n    L = np.hypot(*d)\n    cross = (d[0] * (path[:, 1] - start[1]) - d[1] * (path[:, 0] - start[0])) / max(L, 1e-9)\n    i_exc = np.argmax(np.abs(cross))\n    i_ccw = np.argmax(cross)\n    first150 = (lags >= 0) & (lags < 150)\n    v_r = vel[i0:i_end + 1]\n    vmax = np.array([v_r[np.argmax(np.abs(v_r[:, k])), k] for k in (0, 1)])\n    half, _ = _resample_path(path, 3)\n    if segments == \"length\":\n        pts, _ = _resample_path(path, 4)\n    else:\n        idx = np.linspace(0, len(path) - 1, 4).round().astype(int)\n        pts = path[idx]\n    segs = np.diff(pts, axis=0).ravel()\n    return {\n        \"initial_velocity\": vel[first150].mean(0),\n        \"endpoint\": end,\n        \"max_speed\": np.array([peak]),\n        \"orth_excursion\": np.array([cross[i_exc]]),\n        \"viapoint\": path[i_exc],\n        \"max_velocity\": vmax,\n        \"halfpoint\": half[1],\n        \"segments\": segs,\n        \"max_ccw_excursion\": np.array([cross[i_ccw]]),\n        \"ccw_location\": path[i_ccw],\n        \"reach_end_ms\": np.array([lags[i_end]]),\n    }\n\n\nTASK_SPACES = {\n    \"initial vel.\": [\"initial_velocity\"],\n    \"endpoints + max. spd.\": [\"endpoint\", \"max_speed\"],\n    \"endpoints + orth. exc.\": [\"endpoint\", \"orth_excursion\"],\n    \"endpoints + viapoint\": [\"endpoint\", \"viapoint\"],\n    \"endpoints + max. vel.\": [\"endpoint\", \"max_velocity\"],\n    \"endpoints + halfpoint\": [\"endpoint\", \"halfpoint\"],\n    \"segment dirs.\": [\"segments\"],\n    \"kitchen sink\": [\"segments\", \"max_ccw_excursion\", \"ccw_location\", \"barriers\", \"distractors\"],\n}\n\n\ndef task_space_matrices(feats: list[dict], trials: pd.DataFrame, conds: np.ndarray, n_cond: int) -> dict:\n    \"\"\"Condition means of each task space (c x dim).\"\"\"\n    F = {}\n    keys = feats[0].keys()\n    for k in keys:\n        F[k] = condition_means(np.stack([f[k] for f in feats]), conds, n_cond)\n    F[\"barriers\"] = condition_means((trials.num_barriers.values > 0).astype(float)[:, None], conds, n_cond)\n    F[\"distractors\"] = condition_means((trials.num_targets.values > 1).astype(float)[:, None], conds, n_cond)\n    return {name: np.concatenate([F[p] for p in parts], axis=1) for name, parts in TASK_SPACES.items()}\n\n\n# ---------------------------------------------------------------- PD consistency\n\ndef pd_consistency(x, S, rng, n_draw=25, n_rep=100, standardize=False) -> float:\n    \"\"\"Mean dot product of two unit-length PDs, each fitted on n_draw conditions drawn with\n    replacement (Results, Stability of the PD).\"\"\"\n    if standardize:\n        S = (S - S.mean(0)) / S.std(0)\n    c = len(x)\n    dots = []\n    for _ in range(n_rep):\n        bs = []\n        for _ in range(2):\n            idx = rng.integers(0, c, n_draw)\n            X = np.c_[np.ones(n_draw), S[idx]]\n            b = np.linalg.lstsq(X, x[idx], rcond=None)[0][1:]\n            bs.append(b / np.linalg.norm(b))\n        dots.append(bs[0] @ bs[1])\n    return float(np.mean(dots))\n\n\n# ---------------------------------------------------------------- Figure 8 simulation\n\ndef simulate_rotation(rng, n_cond=25, hold=100, n_steps=360, init=\"disk\"):\n    \"\"\"x(t+1) = W x(t), W = [[1, -2pi/360], [2pi/360, 1]] (Figure 8 legend), after holding the\n    initial state for `hold` steps. Returns initial states (c x 2) and released trajectories\n    (c x n_steps x 2).\"\"\"\n    if init == \"disk\":\n        r = np.sqrt(rng.uniform(0, 1, n_cond))\n        th = rng.uniform(0, 2 * np.pi, n_cond)\n        x0 = np.c_[r * np.cos(th), r * np.sin(th)]\n    else:\n        x0 = rng.uniform(-1, 1, (n_cond, 2))\n    a = 2 * np.pi / 360\n    W = np.array([[1, -a], [a, 1]])\n    traj = np.zeros((n_cond, n_steps, 2))\n    x = x0.copy()\n    for t in range(n_steps):\n        x = x @ W.T\n        traj[:, t] = x\n    return x0, traj\n"
}
```

```
File created successfully at: entries/000140-churchland-2010/maze_prep.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cd entries/000140-churchland-2010; cat > $TMPDIR/dev1.py <<'EOF'
import time, numpy as np, pickle, sys
sys.path.insert(0,'.')
import maze_prep as mp
t0=time.time()
urls=mp.asset_urls(); d=mp.load_train(urls[mp.TRAIN_PATH]); print('load',time.time()-t0)
tr=d['trials']; keep=np.flatnonzero(tr.delay>mp.MIN_DELAY_MS)
on_a=tr.move_onset_time.values
on_b=np.array([mp.speed_onset(d['beh'],tr.iloc[i]) for i in range(len(tr))])
print('onset diff ms', np.percentile((on_b-on_a)*1000,[0,5,50,95,100]))
t1=time.time(); Rg,Rm=mp.trial_rates(d,on_a,keep); print('rates',time.time()-t1, Rg.shape,Rm.shape)
Rg2,Rm2=mp.trial_rates(d,on_b,keep)
kin_a=[mp.trial_kinematics(d['beh'],on_a[i]) for i in keep]; kin_b=[mp.trial_kinematics(d['beh'],on_b[i]) for i in keep]
pickle.dump(dict(d=d,keep=keep,on_a=on_a,on_b=on_b,Rg=Rg,Rm=Rm,Rg2=Rg2,Rm2=Rm2,kin_a=kin_a,kin_b=kin_b),open('/tmp/claude/dev.pkl' if False else __import__('os').environ['TMPDIR']+'/dev.pkl','wb'))
print('total',time.time()-t0)
EOF
python $TMPDIR/dev1.py
```

```
load 1.94571852684021
onset diff ms [ 8.    9.   24.5  41.05 49.  ]
rates 2.0566952228546143 (78, 142, 501) (78, 142, 1301)
total 6.298478841781616
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/dev2.py <<'EOF'
import numpy as np, pickle, sys, os
sys.path.insert(0,'.')
import maze_prep as mp
from scipy import stats
D=pickle.load(open(os.environ['TMPDIR']+'/dev.pkl','rb'))
d=D['d']; tr=d['trials']; keep=D['keep']; conds=tr.cond.values[keep]; C=27
go_l=np.arange(mp.GO_SPAN[0],mp.GO_SPAN[1]+1); mv_l=np.arange(mp.MV_SPAN[0],mp.MV_SPAN[1]+1)
for O4 in 'abc':
  for onset in 'ab':
    Rg,Rm,kin=(D['Rg'],D['Rm'],D['kin_a']) if onset=='a' else (D['Rg2'],D['Rm2'],D['kin_b'])
    vp=np.stack([k['vel'][(k['lags_ms']>=-150)&(k['lags_ms']<=800)] for k in kin])
    kp=mp.proto_filter(vp,conds,O4)
    CMg=mp.condition_means(Rg[kp],conds[kp],C); CMm=mp.condition_means(Rm[kp],conds[kp],C)
    P=mp.epoch_mean(CMg,go_l,mp.PREP_WIN); M=mp.epoch_mean(CMm,mv_l,mp.PERI_WIN)
    for O1 in ['range','sd']:
      pt=mp.tuning(P,O1)
      for O2 in 'i','ii':
        qt=mp.peri_tuning(CMm,mv_l,M,O1,O2)
        sel=(pt>5)&(qt>=1.5*pt)
        r=mp.rowwise_corr(P[:,sel],M[:,sel]); rs=np.array([stats.spearmanr(P[:,j],M[:,j])[0] for j in np.flatnonzero(sel)])
        print(O4,onset,O1,O2,'kept',kp.sum(),'prep-sel',(pt>5).sum(),'n',sel.sum(),'r %.3f sp %.3f'%(r.mean(),rs.mean()),'t p %.3g'%stats.ttest_1samp(r,0).pvalue,'z p %.3g'%stats.ttest_1samp(np.arctanh(r),0).pvalue,'w p %.3g'%stats.wilcoxon(r).pvalue, 'med %.2f'%np.median(r))
EOF
python $TMPDIR/dev2.py
```

```
/tmp/claude-1001/dev2.py:21: RuntimeWarning: Mean of empty slice
  print(O4,onset,O1,O2,'kept',kp.sum(),'prep-sel',(pt>5).sum(),'n',sel.sum(),'r %.3f sp %.3f'%(r.mean(),rs.mean()),'t p %.3g'%stats.ttest_1samp(r,0).pvalue,'z p %.3g'%stats.ttest_1samp(np.arctanh(r),0).pvalue,'w p %.3g'%stats.wilcoxon(r).pvalue, 'med %.2f'%np.median(r))
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in divide
  ret = ret.dtype.type(ret / rcount)
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
/tmp/claude-1001/dev2.py:21: SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
  print(O4,onset,O1,O2,'kept',kp.sum(),'prep-sel',(pt>5).sum(),'n',sel.sum(),'r %.3f sp %.3f'%(r.mean(),rs.mean()),'t p %.3g'%stats.ttest_1samp(r,0).pvalue,'z p %.3g'%stats.ttest_1samp(np.arctanh(r),0).pvalue,'w p %.3g'%stats.wilcoxon(r).pvalue, 'med %.2f'%np.median(r))
/tmp/claude-1001/scratch/lib/python3.13/site-packages/scipy/_lib/_util.py:882: SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
  return fun(*args, **kwargs)
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
a a range i kept 66 prep-sel 93 n 19 r -0.079 sp -0.020 t p 0.0863 z p 0.0855 w p 0.169 med -0.07
a a range ii kept 66 prep-sel 93 n 88 r 0.011 sp 0.043 t p 0.662 z p 0.587 w p 0.973 med -0.02
a a sd i kept 66 prep-sel 8 n 0 r nan sp nan t p nan z p nan w p nan med nan
a a sd ii kept 66 prep-sel 8 n 5 r 0.095 sp -0.053 t p 0.607 z p 0.582 w p 0.625 med 0.09
a b range i kept 66 prep-sel 93 n 18 r -0.041 sp -0.000 t p 0.379 z p 0.366 w p 0.
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate; cat > $TMPDIR/dev3.py <<'EOF'
import numpy as np, pickle, sys, os, time
sys.path.insert(0,'.')
import maze_prep as mp
D=pickle.load(open(os.environ['TMPDIR']+'/dev.pkl','rb'))
d=D['d']; tr=d['trials']; keep=D['keep']; conds=tr.cond.values[keep]; C=27
go_l=np.arange(mp.GO_SPAN[0],mp.GO_SPAN[1]+1); mv_l=np.arange(mp.MV_SPAN[0],mp.MV_SPAN[1]+1)
Rg,Rm,kin=D['Rg'],D['Rm'],D['kin_a']
vp=np.stack([k['vel'][(k['lags_ms']>=-150)&(k['lags_ms']<=800)] for k in kin])
kp=mp.proto_filter(vp,conds,'a')
CMg=mp.condition_means(Rg[kp],conds[kp],C); CMm=mp.condition_means(Rm[kp],conds[kp],C)
P=mp.epoch_mean(CMg,go_l,mp.PREP_WIN)
sel=mp.tuning(P,'range')>5
t0=time.time()
tsel=(mv_l>=-150)&(mv_l<=800)&((mv_l+150)%10==0)
blocks=CMm[:,:,tsel]
peri=mp.leave_one_out_scores(blocks,20)
perf_peri=np.array([mp.loo_performance_curve(P[:,j],peri[j],20) for j in np.flatnonzero(sel)])
print('peri',time.time()-t0, np.round(np.nanmean(perf_peri,0),3))
up=mp.leave_one_out_scores(P[:,:,None],20)
perf_up=np.array([mp.loo_performance_curve(P[:,j],up[j],20) for j in np.flatnonzero(sel)])
print('upper', np.round(np.nanmean(perf_up,0),3))
KIN={k:mp.condition_means(np.stack([x[k] for x in [kin[i] for i in np.flatnonzero(kp)]]),conds[kp],C) for k in ('pos','vel','acc')}; KIN['lags_ms']=kin[0]['lags_ms']
for end in (600,800):
  K=mp.kinematic_matrix(KIN,end); ks=mp.pca_scores(K,20)
  pk=np.array([mp.loo_performance_curve(P[:,j],ks,20) for j in np.flatnonzero(sel)])
  print('kin',end,np.round(np.nanmean(pk,0),3))
for seg in ('length','time'):
  feats=[mp.task_features(kin[i],seg) for i in np.flatnonzero(kp)]
  TS=mp.task_space_matrices(feats,tr.iloc[keep[kp]],conds[kp],C)
  for name,S in TS.items():
    pt=np.array([mp.loo_performance(P[:,j],S) for j in np.flatnonzero(sel)])
    print(seg,name,S.shape[1],round(np.nanmean(pt),3))
print('reach end ms', np.percentile([mp.task_features(k)['reach_end_ms'][0] for k in kin],[0,50,100]))
EOF
python $TMPDIR/dev3.py
```

```
peri 0.33226871490478516 [-5.5000e-02 -4.4000e-02 -1.0400e-01 -2.7500e-01 -9.8100e-01 -1.3690e+00
 -2.2850e+00 -3.1240e+00 -3.4870e+00 -4.0690e+00 -4.3990e+00 -5.0420e+00
 -5.7160e+00 -8.2660e+00 -1.0835e+01 -1.6163e+01 -2.0155e+01 -2.8106e+01
 -3.4954e+01 -4.4316e+01]
upper [-0.045 -0.067 -0.086 -0.114 -0.159 -0.192 -0.343 -0.476 -0.528 -0.589
 -0.67  -0.825 -1.111 -1.61  -2.015 -2.646 -3.323 -4.075 -5.626 -6.514]
kin 600 [-0.052 -0.052 -0.079 -0.09  -0.125 -0.191 -0.256 -0.323 -0.367 -0.424
 -0.549 -0.778 -0.884 -1.142 -1.349 -1.954 -2.094 -2.472 -2.713 -3.479]
kin 800 [-0.053 -0.058 -0.081 -0.091 -0.126 -0.191 -0.257 -0.324 -0.372 -0.428
 -0.553 -0.778 -0.882 -1.222 -1.462 -2.05  -2.12  -2.503 -2.849 -3.805]
length initial vel. 2 -0.048
length endpoints + max. spd. 3 -0.143
length endpoints + orth. exc. 3 -0.126
length endpoints + viapoint 4 -0.138
length endpoints + max. vel. 4 -0.185
length endpoints + halfpoint 4 -0.126
length segment dirs. 6 -0.176
length kitchen sink 11 -0.573
time initial vel. 2 -0.048
time endpoints + max. spd. 3 -0.143
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  python tools/entry.py --help 2>&1 | head; grep -n "tags\|sanity\|claim:" tools/entry.py | head -40
```

```
Thu Oct 29 00:14:08 UTC 2026
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
20:- each notebook has a cell tagged `sanity` that prints what was loaded;
174:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
175:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
286:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/entry.py; sed -n 150,330p tools/entry.py
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
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 221 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/build_nb.py <<'EOF'
"""Convert a percent-format script to an ipynb (cells split at '# %%')."""
import sys, re, nbformat
src = open(sys.argv[1]).read()
cells = []
for chunk in re.split(r"^# %%", src, flags=re.M)[1:]:
    head, _, body = chunk.partition("\n")
    tags = re.findall(r"tags=\[([^\]]*)\]", head)
    tags = [t.strip().strip('"\'') for t in tags[0].split(",")] if tags else []
    body = body.strip("\n")
    if "[markdown]" in head:
        body = "\n".join(l[2:] if l.startswith("# ") else l.lstrip("#") for l in body.splitlines())
        c = nbformat.v4.new_markdown_cell(body)
    else:
        c = nbformat.v4.new_code_cell(body)
    if tags:
        c.metadata["tags"] = tags
    cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, sys.argv[2])
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "entries/000140-churchland-2010/nb_src.py",
 "content": "# %% [markdown]\n# # Churchland et al. (2010) on dandiset 000140 (MC_Maze_Small)\n#\n# **Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory\n# activity: representation of movement or first cog in a dynamical machine? Neuron 68:387-400,\n# doi:10.1016/j.neuron.2010.09.015.\n#\n# **Claims.** `claims/000140/10.1016-j.neuron.2010.09.015.yaml`, written from the NIH author manuscript\n# in PubMed Central (PMC2991102) and its supplement (NIHMS240235-supplement-01.pdf), and checked by a\n# second reader. The claims file decides what is tested; method details it lacks are taken from the\n# paper and cited where they are used, here and in `maze_prep.py`.\n#\n# **Dataset.** DANDI:000140, version 0.220113.0408 (doi:10.48324/dandi.000140/0.220113.0408), streamed.\n# The paper cites no version of the dandiset. 0.220113.0408 is the only published version; the draft\n# (modified 2023-06-20) has the same two assets and size. A published version is fixed, so it is pinned.\n#\n# The dandiset is the Neural Latents Benchmark's MC_Maze_Small: one session of monkey J (Jenkins,\n# 2009-09-28) with two 96-electrode arrays, 100 train/val trials over 27 maze conditions, and 100 test\n# segments without conditions. The paper's J-array dataset has 108 conditions and 2166 trials per\n# neuron; the dandiset holds 27 of its conditions (or of a session like it) with 1 to 4 analysable\n# trials each. The single-electrode datasets of monkeys A, B and J and all EMG are not in it.\n#\n# | Claim | Tested here |\n# |---|---|\n# | fig4d-mean-correlation-j-array | tested |\n# | fig4abc-mean-correlation-other-datasets | blocked: data_missing (single-electrode A, B, J) |\n# | fig4-broad-near-zero | tested |\n# | fig4e-correlation-time-course | tested |\n# | suppfig1-population-averages-lose-tuning | tested |\n# | fig6d-perimovement-best-j-array | tested |\n# | fig6abc-perimovement-best-other-datasets | blocked: data_missing (single-electrode data, EMG) |\n# | fig6-perimovement-best-each-dimensionality | tested |\n# | fig6-maze-endpoint-speed-space-poor | tested |\n# | fig6-dimensionality-trend | tested |\n# | fig6e-summary-rank | blocked: data_missing (A, B, J and EMG); J-array variant shown |\n# | prep-dimensionality-7-to-10 | tested |\n# | fig7a-shuffled-space-poor | tested |\n# | fig7b-window-start-slide | tested (monkey J reading (a), J-array); A and B not in the dandiset |\n# | ap-location-no-effect-j-array | tested on array identity (assumption) |\n# | ap-location-no-effect-other-datasets | blocked: data_missing |\n# | fig7c-anterior-posterior-performance | tested on array identity (assumption) |\n# | prep-activity-more-anterior | tested on array identity (assumption) |\n# | fig7d-pd-consistency | tested |\n# | fig8-linear-dynamics-simulation | tested (simulation, no data) |\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport time\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport maze_prep as mp\n\nT_START = time.time()\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nurls = mp.asset_urls()\nprint(\"dandiset\", mp.DANDISET_ID, \"version\", mp.DANDISET_VERSION)\nfor p, u in urls.items():\n    print(\" \", p, u)\ndata = mp.load_train(urls[mp.TRAIN_PATH])\ntest = mp.load_test(urls[mp.TEST_PATH])\ntrials, units = data[\"trials\"], data[\"units\"]\nprint(f\"loaded in {time.time() - T_START:.1f} s\")\n\n# %% [markdown]\n# ## Data check\n#\n# What was loaded, and each check of the description against the values.\n\n# %% tags=[\"sanity\"]\nmeta = data[\"meta\"]\nprint(\"subject\", meta[\"subject\"], \"session start\", meta[\"session_start\"])\nprint(\"train file trials:\", len(trials), \"splits:\", trials.split.value_counts().to_dict())\nprint(\"test file segments:\", len(test[\"trials\"]), \"columns:\", test[\"colnames\"], \"behaviour:\", test[\"has_behavior\"])\nprint(\"test segment length (s):\", np.unique(np.round(test[\"trials\"].stop_time - test[\"trials\"].start_time, 3)),\n      \"move onset re start (s):\", np.unique(np.round(test[\"trials\"].move_onset_time - test[\"trials\"].start_time, 3)))\nprint(\"all train trials successful:\", bool(trials.success.all()))\nprint(\"conditions (maze_id x trial_version):\", trials.groupby([\"maze_id\", \"trial_version\"]).ngroups,\n      \"| mazes:\", trials.maze_id.nunique(), \"| trial_type values:\", trials.trial_type.nunique())\nprint(\"trial_version vs targets/barriers:\")\nprint(pd.crosstab(trials.trial_version, [trials.num_targets, trials.num_barriers]))\nprint(\"delay (ms): min %d median %d max %d; trials with delay > 400 ms: %d\"\n      % (trials.delay.min(), trials.delay.median(), trials.delay.max(), (trials.delay > mp.MIN_DELAY_MS).sum()))\nkept_delay = trials[trials.delay > mp.MIN_DELAY_MS]\nper_cond = kept_delay.groupby(\"cond\").size()\nprint(\"trials per condition after the delay rule: min %d, median %.0f, max %d; conditions with 1 trial: %d\"\n      % (per_cond.min(), per_cond.median(), per_cond.max(), (per_cond == 1).sum()))\nprint(\"delay column = go cue - target onset (max abs diff, ms):\",\n      float(np.abs((trials.go_cue_time - trials.target_on_time) * 1000 - trials.delay).max()))\nprint(\"rt column = move onset - go cue (max abs diff, ms):\",\n      float(np.abs((trials.move_onset_time - trials.go_cue_time) * 1000 - trials.rt).max()))\nprint(\"rt (ms): min %d median %d max %d\" % (trials.rt.min(), trials.rt.median(), trials.rt.max()))\nprint(\"target onset - trial start (s): %.3f to %.3f; trial stop - move onset (s): %.3f to %.3f\"\n      % ((trials.target_on_time - trials.start_time).min(), (trials.target_on_time - trials.start_time).max(),\n         (trials.stop_time - trials.move_onset_time).min(), (trials.stop_time - trials.move_onset_time).max()))\nprint(\"so go cue - 300 ms and move onset + 900 ms lie inside every trial:\",\n      bool(((trials.go_cue_time - 0.3) > trials.start_time).all() and ((trials.move_onset_time + 0.9) < trials.stop_time).all()))\nprint()\nprint(\"units:\", len(units), \"| heldout:\", int(units.heldout.sum()))\nprint(\"unit id prefix (array) counts:\", units.array_prefix.value_counts().to_dict())\nprint(\"electrode group that units/electrodes points to:\", units.electrode_group.value_counts().to_dict())\nprint(\"electrode index == channel - 1 for every unit:\", bool((units.electrode == units.channel - 1).all()))\nprint(\"electrodes table groups:\", meta[\"electrode_groups\"], \"| x, y, z all NaN:\", meta[\"electrode_xyz_all_nan\"])\noi = meta[\"obs_intervals\"].reshape(len(units), len(trials), 2)\nprint(\"obs_intervals of every unit equal the trial intervals:\",\n      bool(np.allclose(oi, np.c_[trials.start_time, trials.stop_time][None])))\nn_spk = np.array([len(s) for s in data[\"spikes\"]])\ndur = (trials.stop_time - trials.start_time).sum()\nprint(\"spikes per unit: min %d median %d max %d; mean rate over trials %.2f to %.2f spikes/s\"\n      % (n_spk.min(), np.median(n_spk), n_spk.max(), n_spk.min() / dur, n_spk.max() / dur))\nprint(\"spike times sorted in every unit:\", all(np.all(np.diff(s) >= 0) for s in data[\"spikes\"]))\ninside = np.zeros(len(n_spk), int)\nfor u, s in enumerate(data[\"spikes\"]):\n    inside[u] = sum(((s >= a) & (s <= b)).sum() for a, b in zip(trials.start_time, trials.stop_time))\nprint(\"spikes outside the trial intervals:\", int((n_spk - inside).sum()))\nbeh = data[\"beh\"]\nprint()\nprint(\"hand_pos:\", meta[\"pos_description\"], \"| stored unit\", meta[\"pos_unit\"], \"conversion\", meta[\"pos_conversion\"])\nprint(\"hand_vel:\", meta[\"vel_description\"], \"| stored unit\", meta[\"vel_unit\"], \"conversion\", meta[\"vel_conversion\"])\nprint(\"hand position range x %.1f to %.1f, y %.1f to %.1f (values, mm)\" % (beh[\"pos\"][:, 0].min(), beh[\"pos\"][:, 0].max(),\n                                                                         beh[\"pos\"][:, 1].min(), beh[\"pos\"][:, 1].max()))\ndt = np.diff(beh[\"t\"])\nprint(\"behaviour sampling: %.0f%% of intervals are 1 ms; gaps (between trials) up to %.3f s\" % (100 * np.mean(np.isclose(dt, 0.001)), dt.max()))\n# velocity is the derivative of position (description); check the scale on the 1 ms samples\ndpos = np.diff(beh[\"pos\"], axis=0) / dt[:, None]\nok = np.isclose(dt, 0.001)\nslope = np.polyfit(beh[\"vel\"][1:][ok, 0], dpos[ok, 0], 1)[0]\nprint(\"d(position)/dt against hand_vel, slope %.3f (1 if both are mm and mm/s)\" % slope)\nsp = np.hypot(beh[\"vel\"][:, 0], beh[\"vel\"][:, 1])\nprint(\"hand speed 99.9th percentile %.0f mm/s\" % np.percentile(sp, 99.9))\nprint(\"target positions (mm) x %d to %d, y %d to %d\" % (trials.target_x.min(), trials.target_x.max(), trials.target_y.min(), trials.target_y.max()))\n\n# %% [markdown]\n# The positions are stored as numbers in mm with `unit` meters and `conversion` 0.001, which is\n# consistent; the derivative of position matches `hand_vel` with slope about 1, so velocity is in mm/s.\n# Every unit's `electrodes` entry points to the PMd group, but the unit ids carry two array prefixes\n# (1 and 2) and the electrode index equals the channel number minus one for both, so units of the\n# second array point to PMd electrodes as well. The electrodes table has no positions. Both are findings.\n#\n# ### Clock check\n#\n# Spikes and the trial table: decode the side of the reach target (target x > 0) from population spike\n# counts in 100 ms windows around target onset, leave-one-trial-out, nearest class mean on z-scored\n# counts. Before target onset the target is unknown and decoding should be at chance; after it, above\n# chance. The same is shown with the labels of the next trial (a shifted label sequence). Hand and trial\n# table: hand speed around the stored movement onset.\n\n# %%\nrng_clock = np.random.default_rng(0)\n\ndef window_counts(t_ref, w0, w1):\n    X = np.zeros((len(trials), len(units)))\n    for u, s in enumerate(data[\"spikes\"]):\n        lo = np.searchsorted(s, t_ref + w0)\n        hi = np.searchsorted(s, t_ref + w1)\n        X[:, u] = hi - lo\n    return X\n\ndef loo_centroid_accuracy(X, y):\n    X = (X - X.mean(0)) / (X.std(0) + 1e-9)\n    hits = 0\n    for i in range(len(y)):\n        tr_ = np.arange(len(y)) != i\n        m1 = X[tr_ & (y == 1)].mean(0); m0 = X[tr_ & (y == 0)].mean(0)\n        pred = int(np.sum((X[i] - m1) ** 2) < np.sum((X[i] - m0) ** 2))\n        hits += pred == y[i]\n    return hits / len(y)\n\ny_side = (trials.target_x.values > 0).astype(int)\ny_next = np.r_[y_side[1:], y_side[:1]]\nrows = []\nfor w0 in np.arange(-0.4, 0.6, 0.1):\n    X = window_counts(trials.target_on_time.values, w0, w0 + 0.1)\n    rows.append({\"window re target onset (ms)\": f\"{int(round(w0*1000))} to {int(round((w0+0.1)*1000))}\",\n                 \"accuracy, true labels\": loo_centroid_accuracy(X, y_side),\n                 \"accuracy, next trial's labels\": loo_centroid_accuracy(X, y_next)})\nclock = pd.DataFrame(rows)\nnull = [loo_centroid_accuracy(window_counts(trials.target_on_time.values, 0.2, 0.3), rng_clock.permutation(y_side)) for _ in range(50)]\nprint(clock.round(2).to_string(index=False))\nprint(\"chance: majority class %.2f; permuted labels at 200 to 300 ms, 95th percentile %.2f\" % (max(y_side.mean(), 1 - y_side.mean()), np.percentile(null, 95)))\nspeed_at = lambda lag: np.array([np.hypot(*beh[\"vel\"][np.searchsorted(beh[\"t\"], t + lag)]) for t in trials.move_onset_time])\ns_before, s_on, s_after = speed_at(-0.1), speed_at(0.0), speed_at(0.1)\nprint(\"hand speed (mm/s) median at move onset -100 ms %.1f, at onset %.1f, +100 ms %.1f; trials faster at +100 than -100: %d of %d\"\n      % (np.median(s_before), np.median(s_on), np.median(s_after), (s_after > s_before).sum(), len(trials)))\n\n# %% [markdown]\n# ### Duplicated recordings\n#\n# The test file holds 0.7 s segments with movement onset at 250 ms. Are any of them copies of train\n# trials? Each test segment's spike counts of the held-in units are compared with the counts of every\n# train trial in the window 250 ms before to 450 ms after its movement onset. Train trials are also\n# compared with each other.\n\n# %%\nheld = units.index[~units.heldout].values\nassert np.array_equal(units.id.values[held], test[\"ids\"])\ntt = test[\"trials\"]\nXtest = np.zeros((len(tt), len(held)))\nfor k, u in enumerate(held):\n    s = test[\"spikes\"][k]\n    Xtest[:, k] = np.searchsorted(s, tt.stop_time.values) - np.searchsorted(s, tt.start_time.values)\nXtrain = window_counts(trials.move_onset_time.values, -0.25, 0.45)[:, held]\nsame_test_train = sum(np.any(np.all(Xtrain == x, axis=1)) for x in Xtest)\ndist = np.abs(Xtest[:, None, :] - Xtrain[None]).sum(-1)\nXfull = window_counts(trials.start_time.values, 0, 2.0)\nsame_train = sum(np.all(Xfull[i] == Xfull[j]) for i in range(len(trials)) for j in range(i + 1, len(trials)))\nprint(\"test segments identical to a train trial window:\", same_test_train, \"of\", len(tt))\nprint(\"smallest summed count difference between a test segment and any train window: %d (median over segments %d)\"\n      % (dist.min(), np.median(dist.min(1))))\nprint(\"pairs of train trials with identical spike counts in their first 2 s:\", same_train)\nprint(\"total spikes, test file %d, train file %d\" % (sum(len(s) for s in test[\"spikes\"]), n_spk.sum()))\n\n# %% [markdown]\n# ### Shared computations\n#\n# Condition means under each reading of the open details the claims file names: movement onset (O3a,\n# the dataset's `move_onset_time`; O3b, hand speed reaching 15% of its trial peak) and the proto-trial\n# filter (O4a, b, c). Only trials with delay > 400 ms are used. A condition is a `maze_id` and\n# `trial_version` pair (27). Spike trains are smoothed with a 20 ms Gaussian before averaging\n# (Supplemental Experimental Procedures). The 10 ms time step of the T matrices is O5.\n\n# %%\nt0 = time.time()\nkeep = np.flatnonzero(trials.delay.values > mp.MIN_DELAY_MS)\nconds = trials.cond.values[keep]\nC = len(data[\"conditions\"])\nGO_L = np.arange(mp.GO_SPAN[0], mp.GO_SPAN[1] + 1)\nMV_L = np.arange(mp.MV_SPAN[0], mp.MV_SPAN[1] + 1)\nonsets = {\"a\": trials.move_onset_time.values,\n          \"b\": np.array([mp.speed_onset(beh, trials.iloc[i]) for i in range(len(trials))])}\nd_on = (onsets[\"b\"] - onsets[\"a\"])[keep] * 1000\nprint(\"O3b minus O3a onset (ms): min %.0f median %.0f max %.0f\" % (d_on.min(), np.median(d_on), d_on.max()))\nRATES, KINS = {}, {}\nfor o in \"ab\":\n    RATES[o] = mp.trial_rates(data, onsets[o], keep)\n    KINS[o] = [mp.trial_kinematics(beh, onsets[o][i]) for i in keep]\nTSEL = (MV_L >= mp.T_WIN[0]) & (MV_L <= mp.T_WIN[1]) & ((MV_L - mp.T_WIN[0]) % mp.STEP_MS == 0)\n\nCONFIGS = {}\nfor o in \"ab\":\n    vp = np.stack([k[\"vel\"][(k[\"lags_ms\"] >= mp.T_WIN[0]) & (k[\"lags_ms\"] <= mp.T_WIN[1])] for k in KINS[o]])\n    for f in \"abc\":\n        kp = mp.proto_filter(vp, conds, f)\n        Rg, Rm = RATES[o]\n        cfg = {\"kept\": kp,\n               \"CMg\": mp.condition_means(Rg[kp], conds[kp], C),\n               \"CMm\": mp.condition_means(Rm[kp], conds[kp], C)}\n        cfg[\"P\"] = mp.epoch_mean(cfg[\"CMg\"], GO_L, mp.PREP_WIN)\n        cfg[\"M\"] = mp.epoch_mean(cfg[\"CMm\"], MV_L, mp.PERI_WIN)\n        kins = [KINS[o][i] for i in np.flatnonzero(kp)]\n        cfg[\"KIN\"] = {k: mp.condition_means(np.stack([x[k] for x in kins]), conds[kp], C) for k in (\"pos\", \"vel\", \"acc\")}\n        cfg[\"KIN\"][\"lags_ms\"] = kins[0][\"lags_ms\"]\n        for seg in (\"length\", \"time\"):\n            feats = [mp.task_features(x, seg) for x in kins]\n            cfg[\"TS_\" + seg] = mp.task_space_matrices(feats, trials.iloc[keep[kp]], conds[kp], C)\n        cfg[\"reach_end\"] = np.array([mp.task_features(x)[\"reach_end_ms\"][0] for x in kins])\n        CONFIGS[(o, f)] = cfg\nrows = []\nfor (o, f), cfg in CONFIGS.items():\n    n = np.bincount(conds[cfg[\"kept\"]], minlength=C)\n    rows.append({\"onset\": o, \"filter\": f, \"trials kept\": int(cfg[\"kept\"].sum()), \"of\": len(keep),\n                 \"trials per condition min\": n.min(), \"median\": np.median(n), \"max\": n.max()})\nprint(pd.DataFrame(rows).to_string(index=False))\nre_ = CONFIGS[(\"a\", \"a\")][\"reach_end\"]\nprint(\"reach end (ms after onset, 10%% of peak speed): min %d median %d max %d; at the 800 ms limit: %d trials\"\n      % (re_.min(), np.median(re_), re_.max(), (re_ >= 800).sum()))\nprint(f\"shared computations {time.time() - t0:.1f} s\")\nMAIN = (\"a\", \"a\")\n\n# %% [markdown]\n# ### Reliability of condition means\n#\n# The paper's J-array dataset averaged about 20 trials per condition (2166 trials per neuron over 108\n# conditions); here there are 1 to 4. As a reference for every claim below, the split-half reliability of\n# each unit's preparatory and peri-movement tuning: over the conditions with at least two trials, the\n# correlation between the condition means of one trial (the first) and of the others.\n\n# %%\nRg, Rm = RATES[\"a\"]\nPt = mp.epoch_mean(Rg, GO_L, mp.PREP_WIN)       # trials x units\nMt = mp.epoch_mean(Rm, MV_L, mp.PERI_WIN)\nmulti = [c for c in range(C) if (conds == c).sum() >= 2]\nfirst = np.array([np.flatnonzero(conds == c)[0] for c in multi])\nrest_P = np.stack([Pt[np.flatnonzero(conds == c)[1:]].mean(0) for c in multi])\nrest_M = np.stack([Mt[np.flatnonzero(conds == c)[1:]].mean(0) for c in multi])\nrel_P = mp.rowwise_corr(Pt[first], rest_P)\nrel_M = mp.rowwise_corr(Mt[first], rest_M)\npt_main = mp.tuning(CONFIGS[MAIN][\"P\"], \"range\")\nprint(\"conditions with >= 2 trials:\", len(multi))\nfor name, r in ((\"preparatory\", rel_P), (\"peri-movement\", rel_M)):\n    r = r[np.isfinite(r)]\n    print(f\"{name} split-half r over units: median {np.median(r):.2f}, IQR {np.percentile(r,25):.2f} to {np.percentile(r,75):.2f}\")\nsel5 = pt_main > mp.PREP_TUNING_MIN\nprint(\"same, units with > 5 spikes/s preparatory range: preparatory median %.2f, peri-movement median %.2f\"\n      % (np.nanmedian(rel_P[sel5]), np.nanmedian(rel_M[sel5])))\n\n# %% [markdown]\n# ## fig4d-mean-correlation-j-array\n#\n# > For the J-array dataset, the correlation across conditions between a unit's preparatory and\n# > peri-movement firing rates is positive on average but small (mean Pearson r = 0.13, p = 0.03; mean\n# > Spearman r = 0.11).\n#\n# Criterion: units with > 5 spikes/s of preparatory tuning and peri-movement tuning at least 1.5 times as\n# strong, under O1 (range, SD) and O2 (i epoch means, ii largest tuning at any time); O3 and O4 as\n# above; the mean against zero by (a) one-sample t-test, (b) t-test on Fisher z, (c) Wilcoxon. Expected\n# mean Pearson 0.13 ± 0.013 and Spearman 0.11 ± 0.011.\n\n# %% tags=[\"claim:fig4d-mean-correlation-j-array\"]\ndef fig4_units(cfg, O1, O2):\n    pt = mp.tuning(cfg[\"P\"], O1)\n    qt = mp.peri_tuning(cfg[\"CMm\"], MV_L, cfg[\"M\"], O1, O2)\n    return (pt > mp.PREP_TUNING_MIN) & (qt >= mp.PERI_RATIO_MIN * pt)\n\ndef fig4_corrs(cfg, sel):\n    r = mp.rowwise_corr(cfg[\"P\"][:, sel], cfg[\"M\"][:, sel])\n    rs = np.array([stats.spearmanr(cfg[\"P\"][:, j], cfg[\"M\"][:, j])[0] for j in np.flatnonzero(sel)])\n    return r, rs\n\nrows = []\nfor (o, f), cfg in CONFIGS.items():\n    for O1 in (\"range\", \"sd\"):\n        for O2 in (\"i\", \"ii\"):\n            sel = fig4_units(cfg, O1, O2)\n            row = {\"O3\": o, \"O4\": f, \"O1\": O1, \"O2\": O2, \"n units\": int(sel.sum())}\n            if sel.sum() >= 3:\n                r, rs = fig4_corrs(cfg, sel)\n                row.update({\"mean r\": r.mean(), \"mean Spearman\": rs.mean(),\n                            \"p t\": stats.ttest_1samp(r, 0).pvalue,\n                            \"p t(z)\": stats.ttest_1samp(np.arctanh(np.clip(r, -0.999, 0.999)), 0).pvalue,\n                            \"p Wilcoxon\": stats.wilcoxon(r).pvalue})\n                row[\"within tol\"] = abs(r.mean() - 0.13) <= 0.013 and abs(rs.mean() - 0.11) <= 0.011\n                row[\"positive, p<0.05 (any test)\"] = r.mean() > 0 and min(row[\"p t\"], row[\"p t(z)\"], row[\"p Wilcoxon\"]) < 0.05\n            rows.append(row)\nfig4_table = pd.DataFrame(rows)\nprint(fig4_table.round(3).to_string(index=False))\nprint(\"units selected under O1 range / O1 SD (preparatory > 5 spikes/s, main O3/O4):\",\n      int((mp.tuning(CONFIGS[MAIN][\"P\"], \"range\") > 5).sum()), \"/\", int((mp.tuning(CONFIGS[MAIN][\"P\"], \"sd\") > 5).sum()), \"of\", len(units))\nok = fig4_table.dropna(subset=[\"mean r\"])\nprint(\"readings with >= 3 units:\", len(ok), \"| within tolerance and p < 0.05:\",\n      int((ok[\"within tol\"] & ok[\"positive, p<0.05 (any test)\"]).sum()),\n      \"| positive at p < 0.05:\", int(ok[\"positive, p<0.05 (any test)\"].sum()))\nprint(\"mean r over readings: min %.3f max %.3f; mean Spearman min %.3f max %.3f\"\n      % (ok[\"mean r\"].min(), ok[\"mean r\"].max(), ok[\"mean Spearman\"].min(), ok[\"mean Spearman\"].max()))\nsel_main = fig4_units(CONFIGS[MAIN], \"range\", \"i\")\nr_main, rs_main = fig4_corrs(CONFIGS[MAIN], sel_main)\nprint(\"main reading (O1 range, O2 i, O3a, O4a): n = %d, mean r = %.3f, mean Spearman = %.3f, conditions = %d\"\n      % (sel_main.sum(), r_main.mean(), rs_main.mean(), C))\nfor arr in (\"PMd\", \"M1\"):\n    m = (units.array.values == arr)[sel_main]\n    print(f\"  {arr} (by unit id prefix): n = {m.sum()}, mean r = {r_main[m].mean():.3f}\")\n# the units of the widest selection (O2 ii) for reference\nsel_ii = fig4_units(CONFIGS[MAIN], \"range\", \"ii\")\nr_ii, rs_ii = fig4_corrs(CONFIGS[MAIN], sel_ii)\nprint(\"O2 ii (main otherwise): n = %d, mean r = %.3f (t-test p = %.3f), mean Spearman %.3f\" % (sel_ii.sum(), r_ii.mean(), stats.ttest_1samp(r_ii, 0).pvalue, rs_ii.mean()))\n\n# %% [markdown]\n# **Result: not reproduced.** Under none of the readings is the mean correlation within 0.13 ± 0.013 and\n# positive at p < 0.05: the means range from slightly negative to just above zero, and no reading gives a\n# positive mean at p < 0.05. The condition means here rest on 1 to 4 trials, and their split-half\n# reliability (above) is low, so a weak true correlation such as 0.13 could not be resolved; the outcome\n# is a property of these 100 trials, not a test of the paper's J-array data.\n\n# %% [markdown]\n# ## fig4abc-mean-correlation-other-datasets\n#\n# Blocked, `data_missing`: the dandiset holds no single-electrode recordings of monkeys A, B or J (one\n# subject, Jenkins, two Utah arrays).\n\n# %% [markdown]\n# ## fig4-broad-near-zero\n#\n# > Correlations between preparatory and peri-movement tuning span a broad range centred near zero, with\n# > no separate populations of concordant (r near 1) and opposing (r near -1) tuning; most neurons have\n# > weakly correlated tuning.\n#\n# Criterion: on the units and correlations of fig4d, median r in [-0.3, 0.3], IQR at least 0.3, more\n# than half of units with |r| < 0.5, fewer than 15% above 0.8 and fewer than 15% below -0.8.\n\n# %% tags=[\"claim:fig4-broad-near-zero\"]\ndef broad(r):\n    q1, q3 = np.percentile(r, [25, 75])\n    out = {\"n\": len(r), \"median\": np.median(r), \"IQR\": q3 - q1, \"frac |r|<0.5\": np.mean(np.abs(r) < 0.5),\n           \"frac r>0.8\": np.mean(r > 0.8), \"frac r<-0.8\": np.mean(r < -0.8)}\n    out[\"pass\"] = (-0.3 <= out[\"median\"] <= 0.3 and out[\"IQR\"] >= 0.3 and out[\"frac |r|<0.5\"] > 0.5\n                   and out[\"frac r>0.8\"] < 0.15 and out[\"frac r<-0.8\"] < 0.15)\n    return out\n\nrows = []\nfor (o, f), cfg in CONFIGS.items():\n    for O1 in (\"range\", \"sd\"):\n        for O2 in (\"i\", \"ii\"):\n            sel = fig4_units(cfg, O1, O2)\n            if sel.sum() >= 3:\n                rows.append({\"O3\": o, \"O4\": f, \"O1\": O1, \"O2\": O2, **broad(fig4_corrs(cfg, sel)[0])})\nbroad_table = pd.DataFrame(rows)\nprint(broad_table.round(3).to_string(index=False))\nprint(\"readings passing:\", int(broad_table[\"pass\"].sum()), \"of\", len(broad_table))\nprint(\"main reading r range: %.2f to %.2f\" % (r_main.min(), r_main.max()))\nfig, ax = plt.subplots(1, 2, figsize=(8, 3))\nfor a, r, t in ((ax[0], r_main, \"O2 i (main)\"), (ax[1], r_ii, \"O2 ii\")):\n    a.hist(r, bins=np.arange(-1, 1.01, 0.1), color=\"0.4\")\n    a.axvline(r.mean(), color=\"r\")\n    a.set_xlabel(\"r, preparatory vs peri-movement\"); a.set_title(f\"{t}, n = {len(r)}\")\nax[0].set_ylabel(\"units\")\nplt.tight_layout(); plt.show()\n\n# %% [markdown]\n# **Result: reproduced.** Under every reading with at least three units the median correlation is near\n# zero, the spread is broad, most units have |r| < 0.5 and neither end holds 15% of units (the table\n# gives each value). With the low reliability of these condition means, a broad distribution centred near\n# zero is also what noise alone would give, so this agreement is weak evidence.\n\n# %% [markdown]\n# ## fig4e-correlation-time-course\n#\n# > When peri-movement activity is taken at single time points, its correlation with preparatory tuning\n# > starts to fall about 200 ms before movement onset and is near zero by movement onset.\n#\n# Criterion: the rate at single time points of the 20 ms smoothed condition means, swept along the\n# go-locked and movement-locked means, correlated per unit with the preparatory vector, averaged over\n# units ((a) the fig4 units, (b) all units with > 5 spikes/s preparatory tuning). Reproduced when the\n# mean at movement onset is below 0.1 and below half its value at -200 ms, and the largest drop over a\n# 50 ms step begins between -300 ms and onset.\n\n# %% tags=[\"claim:fig4e-correlation-time-course\"]\nLAGS_MV = np.arange(-400, 401, 10)\nLAGS_GO = np.arange(-200, 201, 10)\n\ndef time_course(cfg, sel):\n    P = cfg[\"P\"][:, sel]\n    mv = np.array([np.nanmean(mp.rowwise_corr(P, cfg[\"CMm\"][:, sel, np.flatnonzero(MV_L == t)[0]])) for t in LAGS_MV])\n    go = np.array([np.nanmean(mp.rowwise_corr(P, cfg[\"CMg\"][:, sel, np.flatnonzero(GO_L == t)[0]])) for t in LAGS_GO])\n    return go, mv\n\ndef judge_tc(mv):\n    at0 = mv[LAGS_MV == 0][0]; at200 = mv[LAGS_MV == -200][0]\n    drops = mv[:-5] - mv[5:]            # drop over 50 ms starting at each lag\n    start = LAGS_MV[:-5][np.argmax(drops)]\n    return {\"r at -200\": at200, \"r at 0\": at0, \"largest 50 ms drop starts\": start,\n            \"pass\": at0 < 0.1 and at0 < 0.5 * at200 and -300 <= start <= 0,\n            \"partial\": at0 >= 0.1 and at0 < at200}\n\nrows, curves = [], {}\nfor (o, f), cfg in CONFIGS.items():\n    for O1 in (\"range\", \"sd\"):\n        for O2 in (\"i\", \"ii\"):\n            for units_reading in (\"a\", \"b\"):\n                sel = fig4_units(cfg, O1, O2) if units_reading == \"a\" else mp.tuning(cfg[\"P\"], O1) > mp.PREP_TUNING_MIN\n                if sel.sum() < 3 or (units_reading == \"b\" and O2 == \"ii\"):\n                    continue\n                go, mv = time_course(cfg, sel)\n                curves[(o, f, O1, O2, units_reading)] = (go, mv)\n                rows.append({\"O3\": o, \"O4\": f, \"O1\": O1, \"O2\": O2 if units_reading == \"a\" else \"-\",\n                             \"units\": units_reading, \"n\": int(sel.sum()), \"r at go-200\": go[0], \"r at go\": go[LAGS_GO == 0][0],\n                             **judge_tc(mv)})\ntc_table = pd.DataFrame(rows)\nprint(tc_table.round(3).to_string(index=False))\nprint(\"readings passing:\", int(tc_table[\"pass\"].sum()), \"of\", len(tc_table))\ngo_m, mv_m = curves[(\"a\", \"a\", \"range\", \"i\", \"a\")]\ngo_b, mv_b = curves[(\"a\", \"a\", \"range\", \"i\", \"b\")]\nprint(\"main, fig4 units: r from %.2f to %.2f over -400..400 ms re onset\" % (mv_m.min(), mv_m.max()))\nprint(\"main, all prep-tuned units: r at -400 %.2f, -200 %.2f, -100 %.2f, 0 %.2f, +200 %.2f\"\n      % tuple(mv_b[np.isin(LAGS_MV, [-400, -200, -100, 0, 200])]))\nfig, ax = plt.subplots(1, 2, figsize=(8, 3), sharey=True, gridspec_kw={\"width_ratios\": [1, 2]})\nfor go, mv, lab in ((go_m, mv_m, \"fig4 units\"), (go_b, mv_b, \"all > 5 spikes/s\")):\n    ax[0].plot(LAGS_GO, go, label=lab); ax[1].plot(LAGS_MV, mv, label=lab)\nax[0].set_xlabel(\"ms re go cue\"); ax[1].set_xlabel(\"ms re movement onset\"); ax[0].set_ylabel(\"mean r with preparatory rates\")\nfor a in ax: a.axhline(0, color=\"k\", lw=0.5)\nax[1].legend(); plt.tight_layout(); plt.show()\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## suppfig1-population-averages-lose-tuning\n#\n# > Population-average PSTHs grouped by each neuron's preparatory preference show weak peri-movement\n# > differences that shrink with time, with little relationship to preparatory tuning by movement onset.\n#\n# Criterion: per fig4 unit, the conditions with the strongest and weakest preparatory rate and those at\n# the 1/3 and 2/3 ranks; each unit normalised by its maximum rate; averaged. Reproduced when the spread\n# between the strongest and weakest traces at movement onset is less than half the spread in the\n# preparatory epoch, with the strongest still on top at -150 ms. Unnormalised average as a variant.\n\n# %% tags=[\"claim:suppfig1-population-averages-lose-tuning\"]\ndef pop_avg(cfg, sel, normalise=True):\n    P = cfg[\"P\"][:, sel]\n    order = np.argsort(P, axis=0)\n    ranks = [order[-1], order[int(round((C - 1) * 2 / 3))], order[int(round((C - 1) / 3))], order[0]]\n    idx = np.flatnonzero(sel)\n    go_tr, mv_tr = [], []\n    for rk in ranks:\n        g = np.stack([cfg[\"CMg\"][c, u] for c, u in zip(rk, idx)])\n        m = np.stack([cfg[\"CMm\"][c, u] for c, u in zip(rk, idx)])\n        if normalise:\n            mx = np.maximum(cfg[\"CMg\"][:, idx].max((0, 2)), cfg[\"CMm\"][:, idx].max((0, 2)))\n            g, m = g / mx[:, None], m / mx[:, None]\n        go_tr.append(g.mean(0)); mv_tr.append(m.mean(0))\n    return np.array(go_tr), np.array(mv_tr)\n\ndef judge_pop(go_tr, mv_tr):\n    prep = (GO_L >= mp.PREP_WIN[0]) & (GO_L <= mp.PREP_WIN[1])\n    spread_prep = (go_tr[0] - go_tr[3])[prep].mean()\n    spread_0 = (mv_tr[0] - mv_tr[3])[MV_L == 0][0]\n    top150 = mv_tr[:, MV_L == -150][:, 0]\n    return {\"spread prep\": spread_prep, \"spread at onset\": spread_0, \"ratio\": spread_0 / spread_prep,\n            \"strongest on top at -150\": bool(np.argmax(top150) == 0),\n            \"pass\": spread_0 < 0.5 * spread_prep and np.argmax(top150) == 0}\n\nrows = []\nfor (o, f), cfg in CONFIGS.items():\n    for O1 in (\"range\", \"sd\"):\n        for O2 in (\"i\", \"ii\"):\n            sel = fig4_units(cfg, O1, O2)\n            if sel.sum() < 3:\n                continue\n            for norm in (True, False):\n                rows.append({\"O3\": o, \"O4\": f, \"O1\": O1, \"O2\": O2, \"n\": int(sel.sum()), \"normalised\": norm,\n                             **judge_pop(*pop_avg(cfg, sel, norm))})\npop_table = pd.DataFrame(rows)\nprint(pop_table.round(3).to_string(index=False))\nprint(\"normalised readings passing:\", int(pop_table[pop_table.normalised][\"pass\"].sum()), \"of\", int(pop_table.normalised.sum()),\n      \"| unnormalised:\", int(pop_table[~pop_table.normalised][\"pass\"].sum()), \"of\", int((~pop_table.normalised).sum()))\ng_tr, m_tr = pop_avg(CONFIGS[MAIN], sel_main, True)\nfig, ax = plt.subplots(1, 2, figsize=(8, 3), sharey=True, gridspec_kw={\"width_ratios\": [1, 2]})\ncols = [\"#b2182b\", \"#ef8a62\", \"#67a9cf\", \"#1a9850\"]\nfor k in range(4):\n    ax[0].plot(GO_L, g_tr[k], color=cols[k]); ax[1].plot(MV_L, m_tr[k], color=cols[k])\nax[0].set_xlabel(\"ms re go cue\"); ax[1].set_xlabel(\"ms re movement onset\"); ax[0].set_ylabel(\"normalised rate\")\nplt.tight_layout(); plt.show()\nprint(\"plotted normalised rates range %.3f to %.3f\" % (min(g_tr.min(), m_tr.min()), max(g_tr.max(), m_tr.max())))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig6d-perimovement-best-j-array\n#\n# > For the J-array dataset, the cross-validated performance of a preferred direction in capturing\n# > preparatory tuning is highest when the PD is expressed in the PCA-based peri-movement space, compared\n# > with the kinematic space and the task spaces.\n#\n# Criterion: units with > 5 spikes/s preparatory tuning (O1); leave-one-condition-out regression on a\n# space plus offset; performance 1 - MSE / variance, averaged over units. Peri-movement space: PC scores\n# of the condition means from -150 to +800 ms of all other units, not normalised. Kinematic space: PC\n# scores of x, y position, velocity and acceleration from -150 ms to the end of the reach (600 or 800 ms),\n# each scaled to unit range; reading (a) repeats the six variables to about n columns and (b) uses them\n# once. The eight maze task spaces of the Methods. k = 1 to 14 and 1 to 20. Reproduced when under each\n# reading the best peri-movement performance over k exceeds the best kinematic one and every task space;\n# partially when it exceeds all but one.\n#\n# Readings (a) and (b) of the kinematic matrix give the same scores up to a common scale (each variable\n# repeated the same number of times multiplies the Gram matrix by that number), and regression with an\n# offset is unchanged by scaling, so one is computed and the identity is checked below. Segment\n# directions are computed with segments of equal path length and, as a variant, of equal duration.\n\n# %% tags=[\"claim:fig6d-perimovement-best-j-array\"]\nKMAX = 20\nt0 = time.time()\n\ndef perf_matrix(P, spaces_per_unit, idx, kmax=KMAX):\n    return np.array([mp.loo_performance_curve(P[:, j], spaces_per_unit[j], kmax) for j in idx])\n\nPERF = {}\nfor key, cfg in CONFIGS.items():\n    P = cfg[\"P\"]\n    peri = mp.leave_one_out_scores(cfg[\"CMm\"][:, :, TSEL], KMAX)\n    upper = mp.leave_one_out_scores(P[:, :, None], KMAX)\n    allidx = np.arange(len(units))\n    res = {\"peri\": perf_matrix(P, peri, allidx), \"upper\": perf_matrix(P, upper, allidx)}\n    for end in (600, 800):\n        ks = mp.pca_scores(mp.kinematic_matrix(cfg[\"KIN\"], end), KMAX)\n        res[f\"kin{end}\"] = perf_matrix(P, [ks] * len(units), allidx)\n    for seg in (\"length\", \"time\"):\n        for name, S in cfg[\"TS_\" + seg].items():\n            res[f\"{seg}:{name}\"] = np.array([mp.loo_performance(P[:, j], S) for j in allidx])\n    res[\"peri_scores\"] = peri\n    PERF[key] = res\nprint(f\"performance for all units and readings in {time.time() - t0:.1f} s\")\n# check: repeating the six kinematic variables equally leaves performance unchanged\nK = mp.kinematic_matrix(CONFIGS[MAIN][\"KIN\"], 800)\nKrep = np.tile(K, (1, 23))\np1 = mp.loo_performance_curve(CONFIGS[MAIN][\"P\"][:, 0], mp.pca_scores(K, 10), 10)\np2 = mp.loo_performance_curve(CONFIGS[MAIN][\"P\"][:, 0], mp.pca_scores(Krep, 10), 10)\nprint(\"kinematic reading (a) vs (b), max abs difference in performance (unit 0, k 1-10): %.2e\" % np.nanmax(np.abs(p1 - p2)))\n\ndef fig6_summary(key, O1, kmax, end, seg):\n    cfg, res = CONFIGS[key], PERF[key]\n    sel = mp.tuning(cfg[\"P\"], O1) > mp.PREP_TUNING_MIN\n    peri = np.nanmean(res[\"peri\"][sel, :kmax], 0)\n    kin = np.nanmean(res[f\"kin{end}\"][sel, :kmax], 0)\n    tasks = {name: np.nanmean(res[f\"{seg}:{name}\"][sel]) for name in mp.TASK_SPACES}\n    return sel, peri, kin, tasks\n\nrows = []\nfor key in CONFIGS:\n    for O1 in (\"range\", \"sd\"):\n        for kmax in (14, 20):\n            for end in (600, 800):\n                for seg in (\"length\", \"time\"):\n                    sel, peri, kin, tasks = fig6_summary(key, O1, kmax, end, seg)\n                    best_p = peri.max()\n                    others = {\"kinematic\": kin.max(), **tasks}\n                    beaten = [k for k, v in others.items() if v >= best_p]\n                    rows.append({\"O3\": key[0], \"O4\": key[1], \"O1\": O1, \"kmax\": kmax, \"kin end\": end, \"segments\": seg,\n                                 \"n\": int(sel.sum()), \"best peri\": best_p, \"best peri k\": int(np.argmax(peri) + 1),\n                                 \"best kin\": kin.max(), \"best task\": max(tasks.values()),\n                                 \"best task space\": max(tasks, key=tasks.get), \"spaces >= peri\": len(beaten),\n                                 \"outcome\": \"reproduced\" if not beaten else (\"partial\" if len(beaten) == 1 else \"no\")})\nfig6_table = pd.DataFrame(rows)\nprint(fig6_table.round(3).to_string(index=False))\nprint(fig6_table.outcome.value_counts().to_dict())\nsel6, peri6, kin6, tasks6 = fig6_summary(MAIN, \"range\", 20, 800, \"length\")\nupper6 = np.nanmean(PERF[MAIN][\"upper\"][sel6], 0)\nprint(\"main reading: n = %d units; mean performance by k:\" % sel6.sum())\nprint(pd.DataFrame({\"k\": np.arange(1, KMAX + 1), \"peri\": peri6, \"kinematic\": kin6, \"upper limit\": upper6}).round(3).to_string(index=False))\nprint(\"task spaces:\", {k: round(v, 3) for k, v in tasks6.items()})\nmed = {k: np.nanmedian(PERF[MAIN][k][sel6, :6], 0) for k in (\"peri\", \"kin800\", \"upper\")}\nprint(\"median over units, k = 1..6:\", {k: np.round(v, 3) for k, v in med.items()})\nprint(\"units with peri performance > 0 at their best k <= 14: %d of %d\" % ((np.nanmax(PERF[MAIN][\"peri\"][sel6, :14], 1) > 0).sum(), sel6.sum()))\nsd_sel = mp.tuning(CONFIGS[MAIN][\"P\"], \"sd\") > 5\nprint(\"O1 SD units (n = %d): peri best %.3f, kin best %.3f, upper best %.3f\"\n      % (sd_sel.sum(), np.nanmean(PERF[MAIN][\"peri\"][sd_sel, :14], 0).max(), np.nanmean(PERF[MAIN][\"kin800\"][sd_sel, :14], 0).max(),\n         np.nanmean(PERF[MAIN][\"upper\"][sd_sel, :14], 0).max()))\nfig, ax = plt.subplots(figsize=(5, 3.5))\nks = np.arange(1, KMAX + 1)\nax.plot(ks, peri6, \"k-o\", ms=3, label=\"peri-movement\"); ax.plot(ks, kin6, \"-o\", color=\"tab:purple\", ms=3, label=\"kinematic\")\nax.plot(ks, upper6, color=\"0.6\", label=\"upper limit\")\ndims = {name: S.shape[1] for name, S in CONFIGS[MAIN][\"TS_length\"].items()}\nax.scatter([dims[n] for n in tasks6], list(tasks6.values()), color=\"tab:green\", label=\"task spaces\", zorder=3)\nax.set_ylim(-1.5, 0.2); ax.set_xlabel(\"dimensionality\"); ax.set_ylabel(\"mean performance\"); ax.legend(fontsize=7)\nplt.tight_layout(); plt.show()\nallv = np.r_[peri6, kin6, upper6, list(tasks6.values())]\nprint(\"points below the axis (< -1.5): %d of %d; plotted values range %.2f to %.2f\" % ((allv < -1.5).sum(), len(allv), allv.min(), allv.max()))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig6abc-perimovement-best-other-datasets\n#\n# Blocked, `data_missing`: single-electrode datasets and EMG are not in the dandiset.\n\n# %% [markdown]\n# ## fig6-perimovement-best-each-dimensionality\n#\n# > Taken one dimensionality at a time, performance is almost always higher in the peri-movement space\n# > than in other spaces of the same dimensionality.\n#\n# Criterion: for each k under the fig6d readings, the peri-movement space against the kinematic space at\n# the same k and every task space of that dimensionality; at least 80% of comparisons won.\n\n# %% tags=[\"claim:fig6-perimovement-best-each-dimensionality\"]\nrows = []\nfor key in CONFIGS:\n    for O1 in (\"range\", \"sd\"):\n        for kmax in (14, 20):\n            for end in (600, 800):\n                for seg in (\"length\", \"time\"):\n                    sel, peri, kin, tasks = fig6_summary(key, O1, kmax, end, seg)\n                    wins = total = 0\n                    for k in range(1, kmax + 1):\n                        total += 1; wins += peri[k - 1] > kin[k - 1]\n                        for name, v in tasks.items():\n                            if dims[name] == k:\n                                total += 1; wins += peri[k - 1] > v\n                    rows.append({\"O3\": key[0], \"O4\": key[1], \"O1\": O1, \"kmax\": kmax, \"kin end\": end, \"segments\": seg,\n                                 \"wins\": wins, \"comparisons\": total, \"fraction\": wins / total})\neach_table = pd.DataFrame(rows)\nprint(each_table.round(3).to_string(index=False))\nprint(\"readings with fraction >= 0.8:\", int((each_table.fraction >= 0.8).sum()), \"of\", len(each_table),\n      \"| fraction range %.2f to %.2f\" % (each_table.fraction.min(), each_table.fraction.max()))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig6-maze-endpoint-speed-space-poor\n#\n# > In the maze task the endpoints + maximum speed space, which did well for the speed task, does not\n# > perform well.\n#\n# Criterion: the 3-D endpoints + max. speed performance below the 3-D peri-movement performance by at\n# least 0.1 and below half the best peri-movement performance over k.\n\n# %% tags=[\"claim:fig6-maze-endpoint-speed-space-poor\"]\nrows = []\nfor key in CONFIGS:\n    for O1 in (\"range\", \"sd\"):\n        for kmax in (14, 20):\n            sel, peri, kin, tasks = fig6_summary(key, O1, kmax, 800, \"length\")\n            e = tasks[\"endpoints + max. spd.\"]\n            rows.append({\"O3\": key[0], \"O4\": key[1], \"O1\": O1, \"kmax\": kmax, \"endpoints+max spd\": e, \"peri k=3\": peri[2],\n                         \"best peri\": peri.max(), \"below peri3 by >= 0.1\": e <= peri[2] - 0.1, \"below half best\": e < 0.5 * peri.max(),\n                         \"pass\": (e <= peri[2] - 0.1) and (e < 0.5 * peri.max())})\nems_table = pd.DataFrame(rows)\nprint(ems_table.round(3).to_string(index=False))\nprint(\"readings passing:\", int(ems_table[\"pass\"].sum()), \"of\", len(ems_table))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig6-dimensionality-trend\n#\n# > Performance of the PCA-based spaces typically improves with dimensionality and then declines above\n# > about 10 dimensions.\n#\n# Criterion: for the peri-movement space over k = 1 to 20, performance at the best k above that at k = 2,\n# best k between 3 and 14, and performance at k = 20 below that at k = 10; partially when only the rise\n# holds.\n\n# %% tags=[\"claim:fig6-dimensionality-trend\"]\nrows = []\nfor key in CONFIGS:\n    for O1 in (\"range\", \"sd\"):\n        sel, peri, kin, tasks = fig6_summary(key, O1, 20, 800, \"length\")\n        kb = int(np.argmax(peri) + 1)\n        rise = peri.max() > peri[1] and 3 <= kb <= 14\n        fall = peri[19] < peri[9]\n        rows.append({\"O3\": key[0], \"O4\": key[1], \"O1\": O1, \"best k\": kb, \"perf best\": peri.max(), \"perf k=2\": peri[1],\n                     \"perf k=10\": peri[9], \"perf k=20\": peri[19], \"rise\": rise, \"decline\": fall,\n                     \"kin best k\": int(np.argmax(kin) + 1)})\ntrend_table = pd.DataFrame(rows)\nprint(trend_table.round(3).to_string(index=False))\nprint(\"readings with rise and decline:\", int((trend_table.rise & trend_table.decline).sum()), \"| rise only:\",\n      int((trend_table.rise & ~trend_table.decline).sum()), \"| no rise:\", int((~trend_table.rise).sum()), \"of\", len(trend_table))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig6e-summary-rank\n#\n# Blocked, `data_missing`: Figure 6E combines monkeys A, B and J with EMG spaces, none of which are in\n# the dandiset. As the criterion asks, the same ranking without EMG is shown on the J-array data: for\n# limits 3, 6 and 12, the best PCA-based performance with k up to the limit and each task space at or\n# under it, with SEs across units and paired tests against the best space.\n\n# %% tags=[\"claim:fig6e-summary-rank\"]\nres, sel = PERF[MAIN], mp.tuning(CONFIGS[MAIN][\"P\"], \"range\") > 5\nfor lim in (3, 6, 12):\n    vals = {\"peri-movement\": res[\"peri\"][sel, :lim], \"kinematic\": res[\"kin800\"][sel, :lim]}\n    per_unit = {}\n    for name, v in vals.items():\n        kb = np.argmax(np.nanmean(v, 0))\n        per_unit[name] = v[:, kb]\n    for name in mp.TASK_SPACES:\n        if dims[name] <= lim:\n            per_unit[name] = res[f\"length:{name}\"][sel]\n    means = {k: np.nanmean(v) for k, v in per_unit.items()}\n    best = max(means, key=means.get)\n    out = []\n    for k, v in per_unit.items():\n        p_t = stats.ttest_rel(per_unit[best], v, nan_policy=\"omit\").pvalue if k != best else np.nan\n        p_w = stats.wilcoxon(per_unit[best], v).pvalue if k != best else np.nan\n        out.append({\"space\": k, \"mean\": means[k], \"SE\": np.nanstd(v) / np.sqrt(np.isfinite(v).sum()), \"p paired t\": p_t, \"p Wilcoxon\": p_w})\n    print(f\"limit {lim}: best space {best}\")\n    print(pd.DataFrame(out).round(4).to_string(index=False))\n\n# %% [markdown]\n# ## prep-dimensionality-7-to-10\n#\n# > Preparatory activity is moderately high dimensional; depending on the dataset 7 to 10 dimensions\n# > capture 90% of its variance.\n#\n# Criterion: PCA of the c x n matrix of condition-mean preparatory rates of the fig6d units; the number\n# of components reaching 90% of the variance; expected 8.65 ± 2.35 (6.3 to 11). Unnormalised main,\n# z-scored variant; bounded by c - 1 = 26.\n\n# %% tags=[\"claim:prep-dimensionality-7-to-10\"]\nrows = []\nfor key, cfg in CONFIGS.items():\n    for O1 in (\"range\", \"sd\"):\n        sel = mp.tuning(cfg[\"P\"], O1) > mp.PREP_TUNING_MIN\n        Psel = cfg[\"P\"][:, sel]\n        n90, ev = mp.n_components_for(Psel)\n        z = (Psel - Psel.mean(0)) / Psel.std(0)\n        n90z, _ = mp.n_components_for(z)\n        rows.append({\"O3\": key[0], \"O4\": key[1], \"O1\": O1, \"n units\": int(sel.sum()), \"PCs for 90%\": n90,\n                     \"z-scored\": n90z, \"PC1 share\": ev[0], \"within 6.3-11\": 6.3 <= n90 <= 11})\ndim_table = pd.DataFrame(rows)\nprint(dim_table.round(3).to_string(index=False))\n# reference: the same count for a matrix of pure trial noise (conditions shuffled across trials)\nrng_dim = np.random.default_rng(1)\ncfg = CONFIGS[MAIN]; kp = cfg[\"kept\"]\nPt_k = Pt[kp]; sel = mp.tuning(cfg[\"P\"], \"range\") > 5\nnull_n = []\nfor _ in range(50):\n    perm = rng_dim.permutation(conds[kp])\n    null_n.append(mp.n_components_for(mp.condition_means(Pt_k, perm, C)[:, sel])[0])\nprint(\"same count with condition labels shuffled across trials (50 shuffles): median %d, range %d to %d\"\n      % (np.median(null_n), min(null_n), max(null_n)))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig7a-shuffled-space-poor\n#\n# > A control peri-movement space in which each condition's peri-movement response is inverted at random\n# > on half the conditions performs poorly.\n#\n# Criterion: for each unit and condition with probability 0.5 the activity after -150 ms is reflected\n# around the rate at -150 ms; the shuffled T matrix is the space; per condition for all units as a\n# variant; 20 shuffles. Reproduced when the best shuffled performance over k is below half the best\n# intact performance and below the best kinematic performance.\n\n# %% tags=[\"claim:fig7a-shuffled-space-poor\"]\nrng_shuf = np.random.default_rng(2)\nt0 = time.time()\n\ndef shuffled_perf(cfg, sel, mode, rng, kmax=14):\n    B = cfg[\"CMm\"][:, :, TSEL].copy()           # c x n x t, first sample is -150 ms\n    flip = rng.random((C, len(units))) < 0.5 if mode == \"unit\" else np.repeat(rng.random((C, 1)) < 0.5, len(units), 1)\n    B[flip] = 2 * B[flip][:, :1] - B[flip]\n    sc = mp.leave_one_out_scores(B, kmax)\n    return np.nanmean(perf_matrix(cfg[\"P\"], sc, np.flatnonzero(sel), kmax), 0)\n\nrows = []\nfor key in [MAIN, (\"a\", \"c\"), (\"b\", \"a\")]:\n    cfg = CONFIGS[key]\n    for O1 in (\"range\", \"sd\"):\n        sel = mp.tuning(cfg[\"P\"], O1) > mp.PREP_TUNING_MIN\n        intact = np.nanmean(PERF[key][\"peri\"][sel, :14], 0).max()\n        kin = np.nanmean(PERF[key][\"kin800\"][sel, :14], 0).max()\n        for mode in (\"unit\", \"condition\"):\n            best = [shuffled_perf(cfg, sel, mode, rng_shuf).max() for _ in range(20)]\n            rows.append({\"O3\": key[0], \"O4\": key[1], \"O1\": O1, \"coin per\": mode, \"intact best\": intact, \"kin best\": kin,\n                         \"shuffled best (mean of 20)\": np.mean(best), \"min\": np.min(best), \"max\": np.max(best),\n                         \"pass\": np.mean(best) < 0.5 * intact and np.mean(best) < kin})\nshuf_table = pd.DataFrame(rows)\nprint(shuf_table.round(3).to_string(index=False))\nprint(f\"{time.time() - t0:.1f} s\")\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig7b-window-start-slide\n#\n# > Sliding the start of the peri-movement window later costs little; with the window starting at\n# > movement onset, performance is still 97% (monkey J) and 94% (monkeys A, B) of its original value.\n#\n# Criterion: performance averaged across units at the best k for each start time, window end fixed;\n# the J value under reading (a), J-array; expected ratio 0.97 ± 0.097. Monkeys A and B are not in the\n# dandiset.\n\n# %% tags=[\"claim:fig7b-window-start-slide\"]\nSTARTS = [-150, -100, -50, 0, 50, 100]\nrows = []\nfor key in [MAIN, (\"a\", \"c\"), (\"b\", \"a\")]:\n    cfg = CONFIGS[key]\n    for O1 in (\"range\", \"sd\"):\n        sel = mp.tuning(cfg[\"P\"], O1) > mp.PREP_TUNING_MIN\n        row = {\"O3\": key[0], \"O4\": key[1], \"O1\": O1}\n        for s in STARTS:\n            tsel = (MV_L >= s) & (MV_L <= mp.T_WIN[1]) & ((MV_L - s) % mp.STEP_MS == 0)\n            sc = mp.leave_one_out_scores(cfg[\"CMm\"][:, :, tsel], 14)\n            row[s] = np.nanmean(perf_matrix(cfg[\"P\"], sc, np.flatnonzero(sel), 14), 0).max()\n        row[\"ratio 0/-150\"] = row[0] / row[-150]\n        rows.append(row)\nslide_table = pd.DataFrame(rows)\nprint(slide_table.round(3).to_string(index=False))\nprint(\"ratio within 0.97 +/- 0.097:\", int(((slide_table[\"ratio 0/-150\"] - 0.97).abs() <= 0.097).sum()), \"of\", len(slide_table))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## Anterior and posterior sites\n#\n# The electrodes table has no positions, and every unit's `electrodes` entry points to the PMd group.\n# The three claims below use array identity as the only anterior-posterior information: PMd anterior,\n# M1 posterior (Supplemental Figure 3 legend: \"the first in caudal PMd ... the second in surface M1\").\n# Which array is which comes from the unit ids (prefix 1 maps onto the PMd electrodes, prefix 2 is read\n# as M1); this is an assumption, and every result is also shown with the two arrays swapped.\n\n# %% [markdown]\n# ### ap-location-no-effect-j-array\n#\n# > For J-array, the preparatory to peri-movement tuning correlation does not depend on\n# > anterior-posterior recording location (r = 0.20, p = 0.27).\n#\n# Criterion: a claim of absence; the fig4d correlations regressed on AP location, reproduced when\n# p >= 0.05. With array identity only, the two-group comparison (two-sided t-test) is the variant the\n# criterion names; regression on a 0/1 location is the same test.\n\n# %% tags=[\"claim:ap-location-no-effect-j-array\"]\nrows = []\nfor (o, f), cfg in CONFIGS.items():\n    for O1 in (\"range\", \"sd\"):\n        for O2 in (\"i\", \"ii\"):\n            sel = fig4_units(cfg, O1, O2)\n            if sel.sum() < 4:\n                continue\n            r, _ = fig4_corrs(cfg, sel)\n            ant = (units.array.values == \"PMd\")[sel].astype(float)\n            if ant.min() == ant.max():\n                continue\n            lr = stats.linregress(ant, r)\n            tt_ = stats.ttest_ind(r[ant == 1], r[ant == 0])\n            rows.append({\"O3\": o, \"O4\": f, \"O1\": O1, \"O2\": O2, \"n PMd\": int(ant.sum()), \"n M1\": int((1 - ant).sum()),\n                         \"mean r PMd\": r[ant == 1].mean(), \"mean r M1\": r[ant == 0].mean(),\n                         \"regression r\": lr.rvalue, \"p\": lr.pvalue, \"t-test p\": tt_.pvalue})\nap_table = pd.DataFrame(rows)\nprint(ap_table.round(3).to_string(index=False))\nprint(\"readings with p >= 0.05:\", int((ap_table.p >= 0.05).sum()), \"of\", len(ap_table),\n      \"| swapping the arrays changes the sign of r only\")\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## ap-location-no-effect-other-datasets\n#\n# Blocked, `data_missing`: single-electrode penetrations of monkeys A, B and J are not in the dandiset.\n\n# %% [markdown]\n# ### fig7c-anterior-posterior-performance\n#\n# > The peri-movement space captures preparatory tuning at both anterior and posterior sites, with\n# > normalised performance slightly better at anterior sites.\n#\n# Criterion: a 6-D peri-movement space; units split by AP (here by array); performance normalised by its\n# upper limit (the PCA space of the preparatory matrix) and compared with random halves; the space built\n# from the half's units or from all units. Reproduced when both halves reach 70% of the random-half\n# normalised performance and the anterior half is higher.\n\n# %% tags=[\"claim:fig7c-anterior-posterior-performance\"]\nrng_ap = np.random.default_rng(3)\ncfg = CONFIGS[MAIN]; P = cfg[\"P\"]\nprep_sel = mp.tuning(P, \"range\") > mp.PREP_TUNING_MIN\n\ndef half_perf(members, space_from):\n    \"\"\"Mean 6-D peri performance and upper limit (best k) over prep-tuned units in `members`.\"\"\"\n    mem_space = members if space_from == \"half\" else np.ones(len(units), bool)\n    sc = mp.leave_one_out_scores(cfg[\"CMm\"][:, :, TSEL], 6, members=mem_space)\n    up = mp.leave_one_out_scores(P[:, :, None], 14, members=mem_space)\n    idx = np.flatnonzero(members & prep_sel)\n    perf6 = np.nanmean([mp.loo_performance(P[:, j], sc[j][:, :6]) for j in idx])\n    upper = np.nanmean(perf_matrix(P, up, idx, 14), 0).max()\n    return perf6, upper, len(idx)\n\nrows = []\npmd = units.array.values == \"PMd\"\nfor space_from in (\"half\", \"all\"):\n    for lab, mem in ((\"all units\", np.ones(len(units), bool)), (\"PMd (anterior)\", pmd), (\"M1 (posterior)\", ~pmd)):\n        p6, up, n = half_perf(mem, space_from)\n        rows.append({\"space from\": space_from, \"subset\": lab, \"n tuned\": n, \"perf k=6\": p6, \"upper limit\": up,\n                     \"normalised\": p6 / up if up > 0 else np.nan})\n    rand = []\n    for _ in range(20):\n        mem = np.zeros(len(units), bool); mem[rng_ap.choice(len(units), pmd.sum(), replace=False)] = True\n        p6, up, n = half_perf(mem, space_from)\n        rand.append((p6, up))\n    rand = np.array(rand)\n    rows.append({\"space from\": space_from, \"subset\": \"random halves (20)\", \"n tuned\": np.nan, \"perf k=6\": rand[:, 0].mean(),\n                 \"upper limit\": rand[:, 1].mean(), \"normalised\": np.nan})\nap7_table = pd.DataFrame(rows)\nprint(ap7_table.round(3).to_string(index=False))\nprint(\"upper limits <= 0 make the normalisation undefined:\", int((ap7_table[\"upper limit\"] <= 0).sum()), \"of\", len(ap7_table))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ### prep-activity-more-anterior\n#\n# > Preparatory activity is more prevalent at anterior sites.\n#\n# Criterion: the fraction of units passing > 5 spikes/s preparatory tuning (O1) higher anterior than\n# posterior, two-sided Fisher exact test at p < 0.05; partially when higher without significance.\n\n# %% tags=[\"claim:prep-activity-more-anterior\"]\nrows = []\nfor (o, f), cfg in CONFIGS.items():\n    for O1 in (\"range\", \"sd\"):\n        passed = mp.tuning(cfg[\"P\"], O1) > mp.PREP_TUNING_MIN\n        a_ = passed[pmd].sum(); b_ = passed[~pmd].sum()\n        p = stats.fisher_exact([[a_, pmd.sum() - a_], [b_, (~pmd).sum() - b_]]).pvalue\n        rows.append({\"O3\": o, \"O4\": f, \"O1\": O1, \"PMd passing\": f\"{a_}/{pmd.sum()}\", \"M1 passing\": f\"{b_}/{(~pmd).sum()}\",\n                     \"frac PMd\": a_ / pmd.sum(), \"frac M1\": b_ / (~pmd).sum(), \"Fisher p\": p})\nprev_table = pd.DataFrame(rows)\nprint(prev_table.round(4).to_string(index=False))\n# the same with a measure less sensitive to noise: preparatory range relative to the condition-shuffled range\ncfg = CONFIGS[MAIN]; kp = cfg[\"kept\"]\nrng_prev = np.random.default_rng(4)\nnull_rng = np.stack([np.ptp(mp.condition_means(Pt[kp], rng_prev.permutation(conds[kp]), C), axis=0) for _ in range(200)])\nz_tune = (np.ptp(cfg[\"P\"], 0) - null_rng.mean(0)) / null_rng.std(0)\nprint(\"preparatory range above the 95th percentile of its condition-shuffled null: PMd %d/%d, M1 %d/%d (Fisher p = %.3g)\"\n      % ((z_tune[pmd] > 1.645).sum(), pmd.sum(), (z_tune[~pmd] > 1.645).sum(), (~pmd).sum(),\n         stats.fisher_exact([[(z_tune[pmd] > 1.645).sum(), (z_tune[pmd] <= 1.645).sum()], [(z_tune[~pmd] > 1.645).sum(), (z_tune[~pmd] <= 1.645).sum()]]).pvalue))\nprint(\"median preparatory range (spikes/s): PMd %.2f, M1 %.2f; mean rate in the preparatory epoch: PMd %.2f, M1 %.2f\"\n      % (np.median(np.ptp(cfg[\"P\"], 0)[pmd]), np.median(np.ptp(cfg[\"P\"], 0)[~pmd]), cfg[\"P\"].mean(0)[pmd].mean(), cfg[\"P\"].mean(0)[~pmd].mean()))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig7d-pd-consistency\n#\n# > The PD measured on two random sets of 25 conditions is more stable (higher dot product) in the\n# > peri-movement space than in the task, kinematic and EMG spaces, for every comparison and every dataset.\n#\n# Criterion: per unit, 25 conditions drawn with replacement, PD fitted, another 25 drawn, PD refitted;\n# dot product averaged over units; 100 repeats. Maze comparison spaces: endpoints + max. spd. (3-D),\n# segment dirs. (6-D), and the kinematic space at its best k; the peri-movement space at the same\n# dimensionality. The task-space axes have mixed units (mm, mm/s), and the PD's direction depends on\n# their scale, which the paper does not give: raw units and z-scored axes are both run.\n\n# %% tags=[\"claim:fig7d-pd-consistency\"]\nrng_pd = np.random.default_rng(5)\nrows = []\nfor key in [MAIN, (\"a\", \"c\")]:\n    cfg = CONFIGS[key]; P = cfg[\"P\"]\n    sel = np.flatnonzero(mp.tuning(P, \"range\") > mp.PREP_TUNING_MIN)\n    kin_k = int(np.argmax(np.nanmean(PERF[key][\"kin800\"][sel, :14], 0)) + 1)\n    ks_kin = mp.pca_scores(mp.kinematic_matrix(cfg[\"KIN\"], 800), KMAX)\n    comps = {\"endpoints + max. spd.\": cfg[\"TS_length\"][\"endpoints + max. spd.\"],\n             \"segment dirs.\": cfg[\"TS_length\"][\"segment dirs.\"], f\"kinematic (k={kin_k})\": ks_kin[:, :kin_k]}\n    for name, S in comps.items():\n        k = S.shape[1]\n        for zs in (False, True):\n            c_other = np.mean([mp.pd_consistency(P[:, j], S, rng_pd, standardize=zs) for j in sel])\n            c_peri = np.mean([mp.pd_consistency(P[:, j], PERF[key][\"peri_scores\"][j][:, :k], rng_pd, standardize=zs) for j in sel])\n            rows.append({\"O3\": key[0], \"O4\": key[1], \"space\": name, \"k\": k, \"z-scored axes\": zs, \"n units\": len(sel),\n                         \"consistency other\": c_other, \"consistency peri\": c_peri, \"peri higher\": c_peri > c_other})\npd_table = pd.DataFrame(rows)\nprint(pd_table.round(3).to_string(index=False))\nprint(\"comparisons with peri higher:\", int(pd_table[\"peri higher\"].sum()), \"of\", len(pd_table))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## fig8-linear-dynamics-simulation\n#\n# > In a simulated two-unit rotational linear system with 25 random initial states, the single-unit\n# > correlation between initial (preparatory) and later (peri-movement) activity is near zero (0.08), yet\n# > a PD in the PCA-based peri-movement space captures the initial state perfectly.\n#\n# Criterion: x(t+1) = W x(t), W = [1, -2pi/360; 2pi/360, 1], 25 random initial states, 1000 simulations\n# with initial states uniform in the unit disk and in a square, a released interval of 360 steps;\n# reproduced when the median |r| (unit 1 initial rate against its mean over the interval) is below 0.3\n# and the PD in the 2-D PCA space of the released trajectories gives cross-validated performance above\n# 0.99. The expected value 0.08 ± 0.3 is compared with the median r.\n\n# %% tags=[\"claim:fig8-linear-dynamics-simulation\"]\nrng_sim = np.random.default_rng(6)\nrows = []\nfor init in (\"disk\", \"square\"):\n    rs, perfs = [], []\n    for _ in range(1000):\n        x0, traj = mp.simulate_rotation(rng_sim, init=init)\n        later = traj[:, :, 0].mean(1)\n        rs.append(np.corrcoef(x0[:, 0], later)[0, 1])\n        T = traj.reshape(25, -1)\n        perfs.append(mp.loo_performance(x0[:, 0], mp.pca_scores(T, 2)))\n    rs, perfs = np.array(rs), np.array(perfs)\n    rows.append({\"initial states\": init, \"median r\": np.median(rs), \"median |r|\": np.median(np.abs(rs)),\n                 \"5th pct r\": np.percentile(rs, 5), \"95th pct r\": np.percentile(rs, 95),\n                 \"min PD performance\": perfs.min(), \"median PD performance\": np.median(perfs)})\nsim_table = pd.DataFrame(rows)\nprint(sim_table.round(4).to_string(index=False))\n\n# %% [markdown]\n# **Result: see the table.** (Filled in from the outputs.)\n\n# %% [markdown]\n# ## Summary\n#\n# (Filled in from the outputs.)\n\n# %%\nprint(f\"notebook ran in {(time.time() - T_START) / 60:.1f} min\")\n"
}
```

```
File created successfully at: entries/000140-churchland-2010/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000140-churchland-2010 && . $TMPDIR/scratch/bin/activate && date -u && time MPLBACKEND=Agg python nb_src.py > $TMPDIR/run1.txt 2>&1; tail -5 $TMPDIR/run1.txt
```

```
Thu Oct 29 00:17:49 UTC 2026

real	1m44.766s
user	1m40.159s
sys	0m0.396s
comparisons with peri higher: 2 of 12
initial states  median r  median |r|  5th pct r  95th pct r  min PD performance  median PD performance
          disk    0.0044      0.1114    -0.2533      0.2718                 1.0                    1.0
        square    0.0115      0.1473    -0.3312      0.3304                 1.0                    1.0
notebook ran in 1.7 min
```

**Agent**

Runs end to end in under 2 minutes. Reading the outputs.

**Agent calls Bash**

```bash
sed -n 1,140p $TMPDIR/run1.txt
```

```
entries/000140-churchland-2010/maze_prep.py:265: RuntimeWarning: invalid value encountered in divide
  return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
dandiset 000140 version 0.220113.0408
  sub-Jenkins/sub-Jenkins_ses-small_desc-test_ecephys.nwb https://dandiarchive.s3.amazonaws.com/blobs/118/a0f/118a0fea-39e2-4e85-b01d-a72df466f266
  sub-Jenkins/sub-Jenkins_ses-small_desc-train_behavior+ecephys.nwb https://dandiarchive.s3.amazonaws.com/blobs/7f4/e60/7f4e60f3-2184-4e68-ace1-504a2e564939
loaded in 2.2 s
subject Jenkins session start 2009-09-28T00:00:00-07:00
train file trials: 100 splits: {'train': 75, 'val': 25}
test file segments: 100 columns: ['start_time', 'stop_time', 'move_onset_time', 'split'] behaviour: False
test segment length (s): [0.7] move onset re start (s): [0.25]
all train trials successful: True
conditions (maze_id x trial_version): 27 | mazes: 9 | trial_type values: 9
trial_version vs targets/barriers:
num_targets     1       3
num_barriers    0   9   9
trial_version            
0              32   0   0
1               0  34   0
2               0   0  34
delay (ms): min 14 median 615 max 999; trials with delay > 400 ms: 78
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,330p $TMPDIR/run1.txt
```

```
a  b    sd  -     b  8        0.637    0.803      0.593   0.126                       -130 False     True
 a  b    sd ii     a  4        0.565    0.782      0.543   0.147                       -220 False     True
 a  c range  i     a 15        0.334    0.604      0.330  -0.065                       -230  True    False
 a  c range  -     b 91        0.452    0.614      0.414   0.022                       -220  True    False
 a  c range ii     a 85        0.442    0.599      0.395   0.012                       -210  True    False
 a  c    sd  -     b  7        0.691    0.834      0.661   0.172                       -130 False     True
 a  c    sd ii     a  4        0.625    0.766      0.561   0.142                         90 False     True
 b  a range  i     a 18        0.306    0.578      0.216  -0.018                       -270  True    False
 b  a range  -     b 93        0.416    0.606      0.299   0.021                       -250  True    False
 b  a range ii     a 89        0.404    0.597      0.288   0.015                       -230  True    False
 b  a    sd  -     b  8        0.619    0.784      0.482   0.180                       -160 False     True
 b  a    sd ii     a  5        0.629    0.797      0.492   0.210                       -230 False     True
 b  b range  i     a 15        0.328    0.606      0.207  -0.026                       -260  True    False
 b  b range  -     b 91        0.438    0.608      0.295   0.036                       -250  True    False
 b  b range ii     a 86        0.426    0.594      0.276   0.026                       -250  True    False
 b  b    sd  -     b  8        0.646    0.794      0.468   0.180                       -150 False     True
 b  b    sd ii     a  4        0.585    0.765      0.349   0.177                       -240 False     True
 b  c range  i     a 15        0.307    0.602      0.200  -0.043                       -250  True    False
 b  c range  -     b 91        0.452    0.614      0.302   0.021           
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 330,600p $TMPDIR/run1.txt | grep -v "^ *[ab]  *[abc]  *\(range\|sd\)  *\(14\|20\)  *\(600\|800\)" | head -150; grep -c . $TMPDIR/run1.txt
```

```
units with peri performance > 0 at their best k <= 14: 47 of 93
O1 SD units (n = 8): peri best 0.209, kin best 0.136, upper best 0.123
points below the axis (< -1.5): 26 of 68; plotted values range -44.32 to -0.04
O3 O4    O1  kmax  kin end segments  wins  comparisons  fraction
readings with fraction >= 0.8: 0 of 96 | fraction range 0.07 to 0.36
O3 O4    O1  kmax  endpoints+max spd  peri k=3  best peri  below peri3 by >= 0.1  below half best  pass
 a  a range    14             -0.143    -0.104     -0.044                  False             True False
 a  a range    20             -0.143    -0.104     -0.044                  False             True False
 a  a    sd    14             -0.029     0.110      0.209                   True             True  True
 a  a    sd    20             -0.029     0.110      0.209                   True             True  True
 a  b range    14             -0.138    -0.127     -0.045                  False             True False
 a  b range    20             -0.138    -0.127     -0.045                  False             True False
 a  b    sd    14             -0.029     0.101      0.202                   True             True  True
 a  b    sd    20             -0.029     0.101      0.202                   True             True  True
 a  c range    14             -0.126    -0.087     -0.023                  False             True False
 a  c range    20             -0.126    -0.087     -0.023                  False             True False
 a  c    sd    14              0.018     0.202      0.247                   True             True  True
 a  c    sd    20              0.018     0.202      0.247                   True             True  True
 b  a range    14             -0.147    -0.093     -0.046                  False             True False
 b  a range    20             -0.147    -0.093     -0.046                  False             True False
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 575,597p $TMPDIR/run1.txt
```

```
b  b range       43/72      48/70    0.5972   0.6857    0.2977
 b  b    sd        4/72       4/70    0.0556   0.0571    1.0000
 b  c range       43/72      48/70    0.5972   0.6857    0.2977
 b  c    sd        3/72       4/70    0.0417   0.0571    0.7167entries/000140-churchland-2010/nb_src.py:995: RuntimeWarning: invalid value encountered in divide
  z_tune = (np.ptp(cfg["P"], 0) - null_rng.mean(0)) / null_rng.std(0)
entries/000140-churchland-2010/maze_prep.py:423: RuntimeWarning: invalid value encountered in divide
  bs.append(b / np.linalg.norm(b))

preparatory range above the 95th percentile of its condition-shuffled null: PMd 7/72, M1 6/70 (Fisher p = 1)
median preparatory range (spikes/s): PMd 6.58, M1 10.19; mean rate in the preparatory epoch: PMd 2.40, M1 3.73
O3 O4                 space  k  z-scored axes  n units  consistency other  consistency peri  peri higher
 a  a endpoints + max. spd.  3          False       93                NaN             0.617        False
 a  a endpoints + max. spd.  3           True       93              0.531               NaN        False
 a  a         segment dirs.  6          False       93                NaN               NaN        False
 a  a         segment dirs.  6           True       93              0.527               NaN        False
 a  a       kinematic (k=1)  1          False       93              0.563               NaN        False
 a  a       kinematic (k=1)  1           True       93                NaN             0.591        False
 a  c endpoints + max. spd.  3          False       91              0.535             0.641         True
 a  c endpoints + max. spd.  3           True       91                NaN             0.644        False
 a  c         segment dirs.  6          False       91              0.538             0.484        False
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='maze_prep.py'; s=open(p).read()
s=s.replace("""            b = np.linalg.lstsq(X, x[idx], rcond=None)[0][1:]
            bs.append(b / np.linalg.norm(b))
        dots.append(bs[0] @ bs[1])
    return float(np.mean(dots))""","""            b = np.linalg.lstsq(X, x[idx], rcond=None)[0][1:]
            nb = np.linalg.norm(b)
            bs.append(b / nb if nb > 0 else None)
        if bs[0] is not None and bs[1] is not None:
            dots.append(bs[0] @ bs[1])
    return float(np.mean(dots)) if dots else np.nan""")
s=s.replace('''    """Mean dot product of two unit-length PDs, each fitted on n_draw conditions drawn with
    replacement (Results, Stability of the PD)."""''','''    """Mean dot product of two unit-length PDs, each fitted on n_draw conditions drawn with
    replacement (Results, Stability of the PD). Draws where a PD is zero (the unit's rate is
    the same in every drawn condition) are dropped. Axes are z-scored across conditions
    when `standardize` (an open reading: the paper does not give the axes' scale)."""''')
open(p,'w').write(s)
p='nb_src.py'; s=open(p).read()
s=s.replace("""            c_other = np.mean([mp.pd_consistency(P[:, j], S, rng_pd, standardize=zs) for j in sel])
            c_peri = np.mean([mp.pd_consistency(P[:, j], PERF[key]["peri_scores"][j][:, :k], rng_pd, standardize=zs) for j in sel])""","""            c_other = np.nanmean([mp.pd_consistency(P[:, j], S, rng_pd, standardize=zs) for j in sel])
            c_peri = np.nanmean([mp.pd_consistency(P[:, j], PERF[key]["peri_scores"][j][:, :k], rng_pd, standardize=zs) for j in sel])""")
# fig7c SD variant
s=s.replace("""def half_perf(members, space_from):""","""def half_perf(members, space_from, prep_sel=prep_sel):""")
s=s.replace("""ap7_table = pd.DataFrame(rows)""","""sd_sel = mp.tuning(P, "sd") > mp.PREP_TUNING_MIN
for lab, mem in (("PMd (anterior), O1 SD units", pmd), ("M1 (posterior), O1 SD units", ~pmd)):
    p6, up, n = half_perf(mem, "all", sd_sel)
    rows.append({"space from": "all", "subset": lab, "n tuned": n, "perf k=6": p6, "upper limit": up,
                 "normalised": p6 / up if up > 0 else np.nan})
ap7_table = pd.DataFrame(rows)""")
s=s.replace("""print("preparatory range above the 95th percentile of its condition-shuffled null: PMd %d/%d, M1 %d/%d (Fisher p = %.3g)\"""","""print("preparatory range above the 95th percentile of its condition-shuffled null: PMd %d/%d, M1 %d/%d (Fisher p = %.3g); units with no spikes in the epoch give no z\"""")
open(p,'w').write(s)
EOF
grep -n "no z" nb_src.py | head
```

```
1001:print("preparatory range above the 95th percentile of its condition-shuffled null: PMd %d/%d, M1 %d/%d (Fisher p = %.3g); units with no spikes in the epoch give no z"
```

**Agent calls Bash**

```bash
. $TMPDIR/scratch/bin/activate && MPLBACKEND=Agg python nb_src.py > $TMPDIR/run2.txt 2>&1; grep -A12 "^space from" $TMPDIR/run2.txt; grep -B2 -A16 "consistency other" $TMPDIR/run2.txt; tail -3 $TMPDIR/run2.txt; date -u
```

```
space from                      subset  n tuned  perf k=6  upper limit  normalised
      half                   all units     93.0    -1.369       -0.045         NaN
      half              PMd (anterior)     44.0    -1.535       -0.034         NaN
      half              M1 (posterior)     49.0    -1.087       -0.097         NaN
      half          random halves (20)      NaN    -1.008       -0.059         NaN
       all                   all units     93.0    -1.369       -0.045         NaN
       all              PMd (anterior)     44.0    -1.454       -0.019         NaN
       all              M1 (posterior)     49.0    -1.293       -0.069         NaN
       all          random halves (20)      NaN    -1.400       -0.046         NaN
       all PMd (anterior), O1 SD units      4.0    -1.751        0.145     -12.048
       all M1 (posterior), O1 SD units      4.0    -0.537        0.184      -2.915entries/000140-churchland-2010/nb_src.py:1000: RuntimeWarning: invalid value encountered in divide
  z_tune = (np.ptp(cfg["P"], 0) - null_rng.mean(0)) / null_rng.std(0)

preparatory range above the 95th percentile of its condition-shuffled null: PMd 7/72, M1 6/70 (Fisher p = 1); units with no spikes in the epoch give no z
median preparatory range (spikes/s): PMd 6.58, M1 10.19; mean rate in the preparatory epoch: PMd 2.40, M1 3.73
O3 O4                 space  k  z-scored axes  n units  consistency other  consistency peri  peri higher
 a  a endpoints + max. spd.  3          False       93              0.523             0.617         True
 a  a endpoints + max. spd.  3           True       93              0.531             0.630         True
 a  a         segment dirs.  6          False       93              0.525             0.416        False
 a  a         segment dirs.  6           True       93              0.527             0.449        False
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='nb_src.py'; s=open(p).read()
ph="# **Result: see the table.** (Filled in from the outputs.)"
texts=[
# fig4e
"""# **Result: reproduced, resting on the assumption that tuning is the range across conditions (O1a).**
# Under every reading with O1a (18 of 18) the mean correlation at movement onset is below 0.1 and below
# half its value at 200 ms before onset, and the largest 50 ms drop starts between 270 and 210 ms before
# onset; in the main reading it falls from 0.295 at -200 ms to -0.078 at onset, and for all units with
# preparatory tuning from 0.39 to -0.00. Under O1b (SD, 3 to 8 units) the correlation at onset stays
# between 0.09 and 0.24, partially reproduced in 10 of 12 readings.""",
# suppfig1
"""# **Result: reproduced.** In all 36 readings (normalised and not) the spread between the strongest and
# weakest preparatory conditions at movement onset is less than half the preparatory spread (ratio 0.186
# in the main normalised reading, -0.175 to 0.295 over readings), with the strongest-preparatory trace on
# top at 150 ms before onset. Conditions are ranked by the same noisy preparatory means that give the
# preparatory spread, so part of that spread is selection of noise; the spread at onset does not share
# that noise.""",
# fig6d
"""# **Result: reproduced, resting on assumptions (O1a range, O3a the dataset's onset, O4a a proto-trial).**
# In the main reading the best peri-movement performance (-0.044 at k = 2) is above the best kinematic
# (-0.053) and every task space (best, initial velocity, -0.048), so the criterion holds; it also holds
# with no trial filter (O4c) and under O1b. With the condition mean as proto-trial (O4b) or the speed-based
# onset (O3b) the initial-velocity space matches or beats it (partially reproduced in 32 of 96 readings).
# Under O1a every space performs below zero, that is worse than predicting the mean rate, so the ranking
# is among fits that do not generalise. Under O1b (8 units with an SD above 5 spikes/s) performances are
# positive and the peri-movement space leads clearly (0.209 against 0.136 kinematic and 0.133 task).""",
# each dim
"""# **Result: not reproduced.** Under no reading does the peri-movement space win 80% of the same-dimension
# comparisons; the fraction is 0.07 to 0.36 over 96 readings. Its performance falls steeply with k (from
# -0.104 at k = 3 to -1.369 at k = 6 in the main reading) while the kinematic space falls slowly.""",
# endpoint
"""# **Result: not reproduced, resting on the assumption O1a.** Under O1a (12 readings) the endpoints +
# max. speed space (-0.126 to -0.147) is below the 3-D peri-movement space by less than 0.1 (main: -0.143
# against -0.104). Under O1b (12 readings) it passes: -0.040 to 0.018 against 0.101 to 0.209.""",
# trend
"""# **Result: not reproduced, resting on the assumption O1a.** Under O1a the best k is 2 in all 6 readings,
# so performance does not rise with dimensionality; the decline above 10 holds (main: -4.069 at k = 10,
# -44.316 at k = 20). Under O1b the rise and the decline both hold in 3 of 6 readings (best k = 4).""",
# prep dim
"""# **Result: not reproduced.** 90% of the variance needs 16 or 17 components under O1a (91 to 93 units)
# and 5 or 6 under O1b (7 or 8 units), outside 6.3 to 11 in all 12 readings. With the condition labels
# shuffled across trials the count is 16 to 17, the same as with the true labels, so under O1a the count
# measures trial noise in 1 to 4 trials per condition, not the dimensionality of preparatory tuning.""",
# fig7a
"""# **Result: reproduced.** In all 12 readings the shuffled space's best performance (mean of 20 shuffles)
# is below half the intact best and below the best kinematic performance: main reading -0.097 against
# -0.044 intact and -0.053 kinematic; under O1b -0.056 against 0.209 and 0.136. Under O1a the intact space
# is itself below zero, so the comparison is between two spaces that do not capture tuning.""",
# fig7b
"""# **Result: not reproduced.** The ratio of performance with the window starting at movement onset to
# that at -150 ms is outside 0.97 ± 0.097 in all 6 readings: under O1a performance goes from -0.044 to
# -0.054 (a ratio of 1.242 between two negative values, which has no meaning as a fraction of the
# original), and under O1b from 0.209 to 0.105 (0.501), 0.247 to 0.188 (0.761) and 0.140 to 0.091 (0.646).
# The monkeys A and B value cannot be computed from this dandiset.""",
# ap
"""# **Result: reproduced, resting on the assumption that array identity gives AP location.** In all 17
# readings with units in both arrays the tuning correlation does not differ between the PMd and M1
# arrays (p 0.538 to 1.000; main reading r = 0.105, p = 0.668, 10 PMd and 9 M1 units). Swapping which
# array is PMd changes only the sign of r. With 19 units and two locations the test has little power.""",
# fig7c
"""# **Result: not reproduced, resting on the assumption that array identity gives AP location.** The
# upper-limit performance is at or below zero for every subset (-0.019 to -0.097), so the normalisation
# the criterion needs is undefined. Without it, the 6-D peri-movement space does not capture preparatory
# tuning at either site: performance is -1.535 (PMd) and -1.087 (M1) with the space from the half's own
# units, -1.454 and -1.293 with the space from all units, against -1.008 and -1.400 for random halves.
# For the 4 and 4 units of O1b, the 6-D performance is also negative (-1.751 and -0.537).""",
# prep anterior
"""# **Result: not reproduced, resting on the assumptions O1a and the array mapping.** Under O1a 44 of 72
# PMd units (0.611) and 49 of 70 M1 units (0.700) pass the > 5 spikes/s rule (Fisher p = 0.293), so
# preparatory tuning is not more prevalent at the anterior array; over the O1a readings the PMd fraction
# is lower in all 6 (p 0.293 to 0.488). Under O1b 4 of 72 and 4 of 70 (p = 1.000). With the arrays swapped,
# the anterior fraction would be higher without significance (partially reproduced). Units whose range is
# above the 95th percentile of its condition-shuffled null: 7 of 72 PMd and 6 of 70 M1.""",
# fig7d
"""# **Result: not reproduced.** The peri-movement space is more consistent than endpoints + max. speed
# (main reading 0.617 against 0.523) and than the kinematic space at its best k (k = 1; 0.587 against
# 0.563), but less consistent than segment directions at k = 6 (0.416 against 0.525) in all 4 readings of
# that comparison; 7 of 12 comparisons favour it.""",
# fig8
"""# **Result: reproduced.** Over 1000 simulations the median correlation between unit 1's initial rate and
# its mean over the 360-step released interval is 0.004 (initial states in the unit disk) and 0.012 (in a
# square), within 0.08 ± 0.3; the median |r| is 0.111 and 0.147, below 0.3; the 2-D PCA-space PD gives
# leave-one-out performance of 1.0 in every simulation (minimum 1.0).""",
]
n=s.count(ph); print(n, len(texts))
for t in texts:
    s=s.replace(ph,t,1)
open(p,'w').write(s)
EOF
```

```
14 14
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='nb_src.py'; s=open(p).read()
old_b=s[s.index("# **Result: reproduced.** Under every reading with at least three units"):s.index("# %% [markdown]\n# ## fig4e-correlation-time-course")]
new_b="""# **Result: partially reproduced, resting on the assumption that tuning is the range across conditions
# (O1a).** Under O1a (12 readings) the median correlation is near zero (-0.098 to 0.016), 92% to 100% of
# units have |r| < 0.5, and at most 1.2% lie above 0.8 and none below -0.8, but the interquartile range
# (0.173 to 0.286) is below the 0.3 the criterion asks for broad, so no O1a reading passes in full. Under
# O1b (SD; 3 to 5 units) all 6 readings pass. With the low reliability of these condition means, a
# distribution centred near zero is also what noise alone would give.

"""
s=s.replace(old_b,new_b)
s=s.replace("""# (-0.053) and every task space (best, initial velocity, -0.048), so the criterion holds; it also holds
# with no trial filter (O4c) and under O1b. With the condition mean as proto-trial (O4b) or the speed-based
# onset (O3b) the initial-velocity space matches or beats it (partially reproduced in 32 of 96 readings).""","""# (-0.053) and every task space (best, initial velocity, -0.048), so the criterion holds; it also holds
# with no trial filter (O4c) and under O1b except with O3b and O4b together. With the condition mean as
# proto-trial (O4b) or the speed-based onset (O3b) under O1a, the initial-velocity space matches or beats
# it (partially reproduced in 32 of 96 readings, never worse).""")
s=s.replace("""# **Result: not reproduced.** Under none of the readings is the mean correlation within 0.13 ± 0.013 and
# positive at p < 0.05: the means range from slightly negative to just above zero, and no reading gives a
# positive mean at p < 0.05.""","""# **Result: not reproduced.** Under none of the 18 readings with units is the mean correlation within
# 0.13 ± 0.013 or positive at p < 0.05: mean r ranges from -0.148 to 0.095 and mean Spearman r from -0.061
# to 0.061 (main reading -0.079 and -0.020, 19 units, 27 conditions); the one reading at p < 0.05 has a
# negative mean.""")
open(p,'w').write(s)
EOF
grep -n "Result:" nb_src.py | head -30
```

```
362:# **Result: not reproduced.** Under none of the 18 readings with units is the mean correlation within
414:# **Result: partially reproduced, resting on the assumption that tuning is the range across conditions
480:# **Result: reproduced, resting on the assumption that tuning is the range across conditions (O1a).**
547:# **Result: reproduced.** In all 36 readings (normalised and not) the spread between the strongest and
655:# **Result: reproduced, resting on assumptions (O1a range, O3a the dataset's onset, O4a a proto-trial).**
701:# **Result: not reproduced.** Under no reading does the peri-movement space win 80% of the same-dimension
729:# **Result: not reproduced, resting on the assumption O1a.** Under O1a (12 readings) the endpoints +
760:# **Result: not reproduced, resting on the assumption O1a.** Under O1a the best k is 2 in all 6 readings,
828:# **Result: not reproduced.** 90% of the variance needs 16 or 17 components under O1a (91 to 93 units)
872:# **Result: reproduced.** In all 12 readings the shuffled space's best performance (mean of 20 shuffles)
906:# **Result: not reproduced.** The ratio of performance with the window starting at movement onset to
954:# **Result: reproduced, resting on the assumption that array identity gives AP location.** In all 17
1015:# **Result: not reproduced, resting on the assumption that array identity gives AP location.** The
1053:# **Result: not reproduced, resting on the assumptions O1a and the array mapping.** Under O1a 44 of 72
1094:# **Result: not reproduced.** The peri-movement space is more consistent than endpoints + max. speed
1131:# **Result: reproduced.** Over 1000 simulations the median correlation between unit 1's initial rate and
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='nb_src.py'; s=open(p).read()
assump='''# %% [markdown]
# ### Readings adopted where readings differ (author, step 1.6)
#
# Every claim below is run under every reading the claims file names. Where they give different
# outcomes, these are adopted as assumptions, and the outcome is marked as resting on them:
#
# - O1, "spikes/s of preparatory tuning" (Methods, Neural recordings and datasets): the range of the
#   preparatory rate across conditions (O1a). The Methods speak of a rate difference ("Firing rate
#   modulation was typically lower for the array recordings ... We thus used a lower inclusion criterion:
#   >5 spikes/s of preparatory tuning"), which the range measures directly. The SD reading (O1b) is
#   shown everywhere.
# - O3, movement onset: the dataset's `move_onset_time` (O3a), computed by the data's authors ("calculated
#   offline using a robust algorithm", its description). The paper defers to Churchland et al. (2006c).
# - O4, the proto-trial: a trial of the condition, the one best correlated with the condition mean (O4a),
#   since the Supplemental Experimental Procedures call it a "reference 'proto-trial'".

# %% [markdown]
# ## fig4d-mean-correlation-j-array'''
s=s.replace("# %% [markdown]\n# ## fig4d-mean-correlation-j-array",assump,1)
summ_old=s[s.index("# ## Summary"):s.index("# %%\nprint(f\"notebook ran in")]
summ='''# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | fig4d-mean-correlation-j-array | not reproduced |
# | fig4abc-mean-correlation-other-datasets | blocked: data missing |
# | fig4-broad-near-zero | partially reproduced (assumption O1a) |
# | fig4e-correlation-time-course | reproduced (assumption O1a) |
# | suppfig1-population-averages-lose-tuning | reproduced |
# | fig6d-perimovement-best-j-array | reproduced (assumptions O1a, O3a, O4a) |
# | fig6abc-perimovement-best-other-datasets | blocked: data missing |
# | fig6-perimovement-best-each-dimensionality | not reproduced |
# | fig6-maze-endpoint-speed-space-poor | not reproduced (assumption O1a) |
# | fig6-dimensionality-trend | not reproduced (assumption O1a) |
# | fig6e-summary-rank | blocked: data missing |
# | prep-dimensionality-7-to-10 | not reproduced |
# | fig7a-shuffled-space-poor | reproduced |
# | fig7b-window-start-slide | not reproduced |
# | ap-location-no-effect-j-array | reproduced (assumption: array identity as AP location) |
# | ap-location-no-effect-other-datasets | blocked: data missing |
# | fig7c-anterior-posterior-performance | not reproduced (assumption: array identity as AP location) |
# | prep-activity-more-anterior | not reproduced (assumptions O1a and the array mapping) |
# | fig7d-pd-consistency | not reproduced |
# | fig8-linear-dynamics-simulation | reproduced |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
# the differences from the paper's method.
#
# **How the analysis differs from the paper's.** The dandiset holds 27 maze conditions with 1 to 4
# trials each after the delay rule (78 trials), where the paper's J-array dataset has 108 conditions and
# about 2166 trials per neuron. Condition means are therefore noisy (median split-half reliability of
# preparatory tuning 0.20), and under the range reading of tuning every PD space performs below zero.
# Several outcomes differ between the range and SD readings of "spikes/s of tuning"; the SD reading keeps
# 7 or 8 units with clearer tuning, and on them the peri-movement space performs best with positive
# performance, as in the paper. The anterior-posterior claims use array identity, as the electrodes have
# no positions. Task-space details the Methods leave open (end of reach, segments, signed peak velocity)
# are stated in `maze_prep.py`.
#
# **What was found about the dataset.**
#
# - Every unit's `electrodes` entry points to the PMd electrode group, though unit ids carry two array
#   prefixes (72 units with 1, 70 with 2) and the dataset describes recordings from M1 and PMd; no unit
#   points to an M1 electrode.
# - The electrodes table has no positions (x, y, z and impedance are NaN), so no unit has an
#   anterior-posterior location.
# - The dandiset holds one session of the J-array kind, 100 trials of 27 conditions; the single-electrode
#   datasets of monkeys A, B and J, the EMG and 81 of the 108 conditions are not in it, and which trials
#   and conditions were chosen is not said beyond "limited to 100 train trials and 100 test trials".
# - The 100 test segments carry no condition, go cue or behaviour and only the 107 held-in units, so the
#   paper's condition-wise analyses cannot use them; none duplicates a train trial.
# - 22 of the 100 train trials have delays of 400 ms or less, which the paper excludes.

'''
s=s.replace(summ_old,summ)
open(p,'w').write(s)
EOF
grep -n "Summary" nb_src.py
```

```
1153:# ## Summary
```

**Agent calls Bash**

```bash
printf "dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nscipy\n" > requirements.in && cat > entry.yaml <<'EOF'
schema_version: 1
name: 000140-churchland-2010
type: reproduction
title: Preparatory and peri-movement tuning in the maze-task array data (Churchland et al. 2010)
description: Tests the findings of Churchland, Cunningham, Kaufman, Ryu and Shenoy (2010) on dandiset
  000140 (MC_Maze_Small), which holds 100 trials of 27 maze conditions from the two Utah arrays of
  monkey J. It correlates preparatory and peri-movement tuning, compares how well a preferred direction
  in the peri-movement, kinematic and task spaces captures preparatory tuning, runs the paper's controls,
  compares the two arrays, and repeats the paper's simulation of a rotational linear system. The
  single-electrode datasets and EMG of the paper are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_churchland_2010.ipynb
  title: Reproducing Churchland et al. (2010) from dandiset 000140
  runtime_minutes: 3
helpers:
- maze_prep.py
related:
- id: dandi:000140/0.220113.0408
  relation: uses_data
- id: doi:10.1016/j.neuron.2010.09.015
  relation: reproduces
EOF
. $TMPDIR/scratch/bin/activate; python $TMPDIR/build_nb.py nb_src.py reproduce_churchland_2010.ipynb && mv nb_src.py $TMPDIR/nb_src.py && ls; cd ../..; python tools/entry.py lock entries/000140-churchland-2010 && python tools/entry.py check entries/000140-churchland-2010
```

```
__pycache__
entry.yaml
maze_prep.py
reproduce_churchland_2010.ipynb
requirements.in
wrote entries/000140-churchland-2010/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
rm -rf entries/000140-churchland-2010/__pycache__; date -u; time python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -15
```

```
Thu Oct 29 00:24:43 UTC 2026
Installed kernelspec registry-000140-churchland-2010 in executed/000140-churchland-2010/.venv/share/jupyter/kernels/registry-000140-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (111 s)

real	2m27.109s
user	2m19.871s
sys	0m4.471s
```

**Agent**

The entry runs cleanly from a locked environment (111 s). Now I'll confirm the executed numbers match the conclusions.

**Agent calls Bash**

```bash
cd executed/000140-churchland-2010 && . $TMPDIR/scratch/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('reproduce_churchland_2010.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': out.append(o['text'])
            elif 'text/plain' in o.get('data',{}) and 'image/png' not in o.get('data',{}): out.append(o['data']['text/plain'])
open('/tmp/claude-1001/exec.txt','w').write('\n'.join(out))
EOF
diff <(grep -v "s$\|in [0-9.]* s\|ran in\|RuntimeWarning\|return\|z_tune\|bs.append" $TMPDIR/run2.txt | grep -v "^ *$") <(grep -v "s$\|in [0-9.]* s\|ran in\|RuntimeWarning\|return\|z_tune\|bs.append" $TMPDIR/exec.txt | grep -v "^ *$") | head -40
```

```
95a96
> O2 ii (main otherwise): n = 88, mean r = 0.011 (t-test p = 0.662), mean Spearman 0.043
184a186
>  b  c    sd ii  3       False    23.391001            6.358  0.272                      True  True
542a545
>        all M1 (posterior), O1 SD units      4.0    -0.537        0.184      -2.915
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'));
p=s['properties']; print(list(p))
print(json.dumps(p['outcomes'],indent=0)[:3000]); print(json.dumps(p['findings'],indent=0)[:1500]); print(json.dumps(p['provenance'],indent=0)[:1500])"
```

```
['schema_version', 'id', 'dataset', 'paper', 'date', 'provenance', 'outcomes']
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
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
[... 256 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000140-churchland-2010-01.yaml",
 "content": "schema_version: 2\nid: 000140-churchland-2010-01\ndataset:\n  archive: dandi\n  id: \"000140\"\n  version: 0.220113.0408\n  doi: 10.48324/dandi.000140/0.220113.0408\npaper: doi:10.1016/j.neuron.2010.09.015\ndate: 2026-10-29\nentry: 000140-churchland-2010\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40791667840\noutcomes:\n- claim: fig4d-mean-correlation-j-array\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4d-mean-correlation-j-array\n  measured:\n  - -0.079\n  - -0.020\n  notes: Under none of the 18 readings with units (O1 x O2 x O3 x O4) is the mean correlation within\n    0.13 +/- 0.013 or positive at p < 0.05. Mean Pearson r ranges from -0.148 to 0.095 and mean\n    Spearman r from -0.061 to 0.061; the one reading with p < 0.05 (O3a, O4b, O1 range, O2 i, 13\n    units, r = -0.148) is negative. The main reading (O1 range, O2 i, O3a, O4a) gives 19 units over\n    27 conditions, mean r -0.079 (t-test p = 0.086) and Spearman -0.020; with O2 ii 88 units and mean\n    r 0.011 (p = 0.662). Under O1 SD no unit passes with O2 i and 3 to 5 with O2 ii. The condition\n    means rest on 1 to 4 trials (66 to 78 trials kept), and the split-half reliability of preparatory\n    tuning has a median of 0.20 over units, so a mean correlation of 0.13 could not be resolved here;\n    the outcome describes these 100 trials, not the paper's 2166 trials per neuron.\n  deviations:\n  - 27 conditions with 1 to 4 trials each after the delay rule, against 108 conditions and about 20\n    trials each in the paper's J-array dataset.\n  - Spike trains smoothed with a Gaussian of SD 20 ms before averaging (Supplemental Experimental\n    Procedures, Computing the mean firing rate versus time; the width is read as the SD, a standard\n    choice).\n- claim: fig4abc-mean-correlation-other-datasets\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds one subject (Jenkins) recorded with two Utah arrays. The single-electrode\n    datasets of monkeys A, B and J are not in it, and no other dandiset of these recordings was named\n    by the paper or the dandiset.\n- claim: fig4-broad-near-zero\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4-broad-near-zero\n  notes: Under O1 range (12 readings) the median r is near zero (-0.098 to 0.016), 92% to 100% of\n    units have |r| < 0.5, at most 1.2% are above 0.8 and none below -0.8, but the interquartile range\n    is 0.173 to 0.286, below the 0.3 the criterion requires; no O1 range reading passes in full. Under\n    O1 SD (3 to 5 units) all 6 readings pass. The criterion has no partial rule; the outcome is partial\n    because four of its five conditions hold. A distribution centred near zero is also what the noise\n    of 1 to 4 trials per condition would give.\n  deviations:\n  - Assumed O1 is the range of the preparatory rate across conditions, as the Methods describe the\n    inclusion rule as a rate difference (\"Firing rate modulation was typically lower ... >5 spikes/s\n    of preparatory tuning\"); under the SD reading the claim is reproduced, on 3 to 5 units.\n- claim: fig4e-correlation-time-course\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4e-correlation-time-course\n  notes: Under all 18 O1 range readings the mean correlation at movement onset is below 0.1 and below\n    half its value at -200 ms, and the largest 50 ms drop starts 270 to 210 ms before onset. Main\n    reading (fig4 units, 19) 0.295 at -200 ms and -0.078 at onset; all units with preparatory tuning\n    (93) 0.62 at -400 ms, 0.39 at -200 ms, 0.12 at -100 ms and -0.00 at onset. Under O1 SD (3 to 8\n    units) the value at onset is 0.091 to 0.244, partially reproduced in 10 of 12 readings.\n  deviations:\n  - Assumed O1 is the range across conditions (see fig4-broad-near-zero).\n  - The time axis uses go-locked means from -200 to +200 ms and movement-locked means from -400 to\n    +400 ms, in 10 ms steps (Supplemental Experimental Procedures, the spliced trace); the judgement\n    uses the movement-locked part.\n- claim: suppfig1-population-averages-lose-tuning\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:suppfig1-population-averages-lose-tuning\n  notes: In all 36 readings, normalised and not, the spread between the strongest and weakest\n    preparatory conditions at movement onset is below half the preparatory spread (ratio 0.186 in the\n    main normalised reading; -0.175 to 0.295 over readings), with the strongest trace on top at -150\n    ms. The conditions are ranked by the same noisy preparatory means that make the preparatory spread,\n    so part of that spread is selected noise, which the spread at onset does not share; with 1 to 4\n    trials per condition this criterion would be met by noise alone.\n  deviations:\n  - Each unit is normalised by its maximum condition-mean rate over the go-locked and movement-locked\n    spans stored (-300 to +200 ms and -400 to +900 ms); the legend says \"normalizing each neuron's\n    activity by its maximum rate\".\n- claim: fig6d-perimovement-best-j-array\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6d-perimovement-best-j-array\n  notes: Main reading (O1 range, O3a, O4a; 93 units) best peri-movement performance -0.044 at k = 2,\n    best kinematic -0.053, best task space (initial velocity) -0.048. Of 96 readings 64 meet the\n    criterion and 32 are partial (initial velocity at or above the peri-movement space), the partial\n    ones under O1 range with O4b or O3b, and under O1 SD with O3b and O4b together. Under O1 range all\n    spaces perform below zero, worse than predicting the mean rate, and 47 of 93 units have a positive\n    peri-movement performance at their best k up to 14. Under O1 SD (8 units) the peri-movement space\n    is best with positive performance, 0.209 against 0.136 kinematic and 0.133 task. Repeating the\n    kinematic variables (reading a) leaves performance unchanged (largest difference 8e-15).\n  deviations:\n  - Assumed O1 range, O3a (the dataset's movement onset, computed by the data's authors) and O4a (the\n    proto-trial is the trial of the condition best correlated with its mean, as the supplement calls\n    it a \"proto-trial\"); under O3b or O4b with O1 range the outcome is partially reproduced.\n  - The upper limit uses the preparatory matrix of all units except the fitted one, as the\n    peri-movement space does (Methods, PCA-based spaces); the supplement says \"all neurons\".\n  - Task spaces follow the Methods' list (Task spaces). Details they leave open, set here and stated\n    in maze_prep.py, are the end of the reach (last time within 800 ms of onset with speed at least\n    10% of peak), the peak velocity components (the signed value of largest magnitude), and the\n    segments (equal path length, with equal duration as a variant, which gives the same outcome).\n  - Acceleration for the kinematic space is the derivative of the dataset's hand velocity after a\n    20 ms Gaussian, a standard choice.\n- claim: fig6abc-perimovement-best-other-datasets\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the single-electrode datasets of monkeys A, B and J and their EMG, which are not in the\n    dandiset.\n- claim: fig6-perimovement-best-each-dimensionality\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-perimovement-best-each-dimensionality\n  notes: The peri-movement space wins 7% to 36% of the same-dimension comparisons over the 96 readings\n    of fig6d, never the 80% the criterion requires. Its performance falls steeply with k (main reading\n    -0.104 at k = 3, -1.369 at k = 6) while the kinematic space falls slowly (-0.081 and -0.191).\n- claim: fig6-maze-endpoint-speed-space-poor\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-maze-endpoint-speed-space-poor\n  notes: Under O1 range (12 readings) the endpoints + max. speed space (-0.126 to -0.147) is below the\n    3-D peri-movement space by less than 0.1 (main reading -0.143 against -0.104). Under O1 SD all 12\n    readings pass (-0.040 to 0.018 against 0.101 to 0.209).\n  deviations:\n  - Assumed O1 is the range across conditions (see fig4-broad-near-zero); under the SD reading the\n    claim is reproduced.\n- claim: fig6-dimensionality-trend\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-dimensionality-trend\n  notes: Under O1 range the best k is 2 in all 6 readings, so performance does not rise with\n    dimensionality; the decline above 10 holds (main reading -4.069 at k = 10, -44.316 at k = 20).\n    Under O1 SD the rise and the decline both hold in 3 of 6 readings (best k = 4), and in the other 3\n    the best k is 2.\n  deviations:\n  - Assumed O1 is the range across conditions (see fig4-broad-near-zero).\n- claim: fig6e-summary-rank\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Figure 6E combines monkeys A, B and J with EMG spaces, none of which are in the dandiset. The\n    variant on J-array without EMG is shown in the notebook (main reading); the peri-movement space has\n    the highest mean at limits 3, 6 and 12 (-0.044), and the kinematic and initial-velocity spaces are\n    not significantly worse (paired t p = 0.62 and 0.81).\n- claim: prep-dimensionality-7-to-10\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:prep-dimensionality-7-to-10\n  measured: 16\n  notes: 90% of the variance of the condition-mean preparatory matrix needs 16 or 17 components under\n    O1 range (91 to 93 units) and 5 or 6 under O1 SD (7 or 8 units); none of the 12 readings is within\n    6.3 to 11, z-scored or not. With the condition labels shuffled across trials the count is 16 to 17,\n    the same as with the true labels, so under O1 range the count measures trial noise. The count is\n    bounded here by 26.\n- claim: fig7a-shuffled-space-poor\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7a-shuffled-space-poor\n  notes: In all 12 readings (three O3/O4 settings, O1 range and SD, the coin per unit and condition or\n    per condition) the mean best performance over 20 shuffles is below half the intact best and below\n    the best kinematic performance. Main reading -0.097 against -0.044 intact and -0.053 kinematic;\n    O1 SD -0.056 against 0.209 and 0.136. Under O1 range the intact space is itself below zero.\n  deviations:\n  - Readings run for O3a with O4a and O4c and for O3b with O4a, not all six settings, to keep the\n    notebook short; all give the same outcome.\n- claim: fig7b-window-start-slide\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7b-window-start-slide\n  measured: 1.242\n  notes: The ratio of performance with the window starting at movement onset to that at -150 ms is\n    outside 0.97 +/- 0.097 in all 6 readings. Under O1 range performance goes from -0.044 to -0.054\n    (ratio 1.242, a ratio of two negative values with no meaning as a fraction of the original),\n    -0.023 to -0.050 and -0.046 to -0.057; under O1 SD from 0.209 to 0.105 (0.501), 0.247 to 0.188\n    (0.761) and 0.140 to 0.091 (0.646). Only the monkey J value under reading (a) can be computed; the\n    monkeys A and B value (0.94) is not in the dandiset.\n  deviations:\n  - Start times -150 to +100 ms in 50 ms steps, end fixed at +800 ms, best k up to 14 for each start\n    (Figure 7B legend, \"the best dimensionality for that dataset/start-time\").\n- claim: ap-location-no-effect-j-array\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:ap-location-no-effect-j-array\n  notes: In all 17 readings with units on both arrays the tuning correlation does not differ by array\n    (p 0.538 to 1.000). Main reading r = 0.105, p = 0.668, 10 PMd and 9 M1 units (mean r -0.060 and\n    -0.099). With 19 units and two locations the test has little power; the paper's r = 0.20 would\n    not be detected here either.\n  deviations:\n  - The electrodes have no positions, so AP location is the array, PMd anterior and M1 posterior\n    (Supplemental Figure 3 legend). Regression on a 0/1 location, the two-group comparison the\n    criterion names as the variant for array identity.\n  - Assumed the array of a unit is the first digit of its id, 1 for PMd and 2 for M1, as units with\n    prefix 1 map onto the PMd electrodes of the table; every unit's electrodes entry points to the PMd\n    group. Swapping the arrays changes only the sign of r.\n- claim: ap-location-no-effect-other-datasets\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The single-electrode penetrations of monkeys A, B and J, and their AP coordinates, are not in\n    the dandiset.\n- claim: fig7c-anterior-posterior-performance\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7c-anterior-posterior-performance\n  notes: The upper-limit performance is at or below zero for every subset (-0.019 to -0.097), so the\n    normalisation the criterion needs is undefined. Without it, the 6-D peri-movement space does not\n    capture preparatory tuning at either array, with performance -1.535 (PMd, 44 units) and -1.087\n    (M1, 49 units) when the space is built from the half's units, and -1.454 and -1.293 from all units,\n    against -1.008 and -1.400 for random halves. For the 4 and 4 units of O1 SD the 6-D performance is\n    -1.751 and -0.537. The criterion cannot be applied as written; the outcome is not reproduced\n    because the first part of the statement, that the space captures tuning at both sites, does not\n    hold.\n  deviations:\n  - AP halves are the two arrays (see ap-location-no-effect-j-array), not a median split of positions.\n  - Assumed O1 range, O3a and O4a (see fig6d-perimovement-best-j-array); 20 random halves of the\n    size of the PMd array.\n- claim: prep-activity-more-anterior\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:prep-activity-more-anterior\n  notes: Under O1 range 44 of 72 PMd units (0.611) and 49 of 70 M1 units (0.700) pass the > 5 spikes/s\n    rule (Fisher p = 0.293); the PMd fraction is lower in all 6 O1 range readings (p 0.293 to 0.488).\n    Under O1 SD 4 of 72 and 4 of 70 (p = 1.000). Units whose range exceeds the 95th percentile of a\n    condition-shuffled null are 7 of 72 PMd and 6 of 70 M1. Median preparatory range is 6.58 spikes/s\n    on the PMd array and 10.19 on M1, and the mean preparatory rate 2.40 and 3.73 spikes/s. With the\n    arrays swapped the anterior fraction would be higher without significance, partially reproduced.\n  deviations:\n  - Assumed O1 range and the array mapping of ap-location-no-effect-j-array (prefix 1 PMd); the outcome\n    depends on the mapping.\n- claim: fig7d-pd-consistency\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7d-pd-consistency\n  notes: The peri-movement space is more consistent than endpoints + max. speed (main reading 0.617\n    against 0.523) and than the kinematic space at its best k (k = 1, 0.587 against 0.563), but less\n    consistent than segment directions at k = 6 (0.416 against 0.525) in all 4 readings of that\n    comparison (O4a and O4c, raw and z-scored axes); 7 of 12 comparisons favour it.\n  deviations:\n  - The paper does not give the scale of task-space axes, which sets a PD's direction when units are\n    mixed (mm and mm/s); raw and z-scored axes are both run and agree on the segment-directions\n    comparison.\n  - Draws in which the unit's rate is the same in all drawn conditions (a zero PD) are dropped; 100\n    repeats per unit, the claim's standard choice.\n- claim: fig8-linear-dynamics-simulation\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig8-linear-dynamics-simulation\n  measured: 0.0044\n  notes: Over 1000 simulations the median correlation between unit 1's initial rate and its mean over\n    the 360-step released interval is 0.0044 (initial states uniform in the unit disk) and 0.0115 (in\n    a square), within 0.08 +/- 0.3; the median |r| is 0.111 and 0.147, below 0.3; the PD in the 2-D\n    PCA space of the released trajectories gives leave-one-out performance of 1.0 in every simulation.\n  deviations:\n  - The initial state is held for 100 steps before release; the hold does not enter either measure.\nfindings:\n- kind: metadata_error\n  statement: Every unit's `electrodes` entry in the train and test files points to an electrode of the\n    PMd group (indices 0 to 94), though the unit ids carry two array prefixes (72 units with 1, 70 with\n    2) and the dandiset describes recordings from M1 and PMd. The electrode index equals the channel\n    number in the id minus one for both prefixes, so the units of one array point to the wrong group\n    and no unit points to an M1 electrode. Which prefix is PMd is not stated.\n- kind: metadata_insufficient\n  statement: The electrodes table has no positions or impedances (x, y, z and imp are NaN for all 192\n    electrodes), so no unit has an anterior-posterior location, which the paper's comparison of\n    anterior and posterior sites uses.\n- kind: data_missing\n  statement: The dandiset holds 100 trials of 27 of the 108 maze conditions from the arrays of monkey\n    J (1 to 4 trials per condition after the paper's delay rule), where the paper's J-array dataset has\n    about 2166 trials per neuron. The single-electrode datasets of monkeys A, B and J and all EMG are\n    not in it. Four claims cannot be tested, and the claims that were tested rest on condition means\n    whose split-half reliability has a median of 0.20.\n- kind: selection_undocumented\n  statement: The dandiset says the data are \"limited to 100 train trials and 100 test trials\" but not\n    how the 27 conditions and 100 trials were chosen, whether this session is the paper's J-array\n    dataset, or whether the trials were filtered by the paper's velocity-profile rule. 22 of the 100\n    train trials have delays of 400 ms or less, which the paper excludes.\n- kind: other\n  statement: The test file's 100 segments (0.7 s, movement onset at 0.25 s) have no condition, go cue,\n    target or behaviour, and hold only the 107 held-in units, so they cannot enter condition-wise\n    analyses. None duplicates a train trial (smallest summed difference in spike counts 117).\n- kind: methods_unavailable\n  statement: Question for the paper's authors. The inclusion rule \">5 spikes/s of preparatory tuning\"\n    (10 spikes/s for single electrodes) does not define tuning. Read as the range across conditions\n    it keeps 93 of 142 units here, as the SD 8; outcomes of fig4-broad-near-zero, fig4e,\n    fig6-maze-endpoint-speed-space-poor and fig6-dimensionality-trend differ between the two. Was it the\n    range, the SD, or another measure, and was the same measure used for the 1.5 times peri-movement\n    rule?\n- kind: methods_unavailable\n  statement: Question for the paper's authors. How was the maze-task \"proto-trial\" chosen (a trial best\n    matching the condition mean, or the mean itself), over what window were velocity profiles\n    correlated, and how was movement onset detected (Churchland et al. 2006c is cited)? With the\n    condition mean as proto-trial or a speed-threshold onset the fig6d result is partially reproduced\n    here, with a proto-trial and the dataset's onset reproduced.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. For the task spaces, how was the end of the reach set\n    for the endpoints, were the three segments of equal length or duration, was \"peak horizontal and\n    vertical velocity\" signed, and were task-space axes scaled before the PD consistency analysis of\n    Figure 7D? Did the upper-limit space of the supplement include the fitted neuron?\n"
}
```

```
File created successfully at: attempts/000140-churchland-2010-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/nb_src.py'; s=open(p).read()
old="""# with no trial filter (O4c) and under O1b except with O3b and O4b together. With the condition mean as
# proto-trial (O4b) or the speed-based onset (O3b) under O1a, the initial-velocity space matches or beats
# it (partially reproduced in 32 of 96 readings, never worse)."""
assert old in s
s=s.replace(old,"""# with no trial filter (O4c) and under O1b except with O3b and O4b together. Under O1a with the condition
# mean as proto-trial (O4b), or with the speed-based onset (O3b) and a filter, the initial-velocity space
# matches or beats it (partially reproduced in 32 of 96 readings, never worse).""")
open(p,'w').write(s)
p='attempts/000140-churchland-2010-01.yaml'; s=open(p).read()
old="""    criterion and 32 are partial (initial velocity at or above the peri-movement space), the partial
    ones under O1 range with O4b or O3b, and under O1 SD with O3b and O4b together."""
assert old in s
s=s.replace(old,"""    criterion and 32 are partial (initial velocity at or above the peri-movement space), the partial
    ones under O1 range with O3a and O4b, O3b and O4a, or O3b and O4b, and under O1 SD with O3b and
    O4b.""")
old2="""    it a "proto-trial"); under O3b or O4b with O1 range the outcome is partially reproduced."""
assert old2 in s
s=s.replace(old2,"""    it a "proto-trial"); with O4b, or O3b with a filter, the outcome is partially reproduced.""")
open(p,'w').write(s)
EOF
. $TMPDIR/scratch/bin/activate; python $TMPDIR/build_nb.py $TMPDIR/nb_src.py entries/000140-churchland-2010/reproduce_churchland_2010.ipynb
python3 -c "
import yaml,re
t=open('attempts/000140-churchland-2010-01.yaml').read(); yaml.safe_load(t)
for i,l in enumerate(t.splitlines()):
    if re.search(r'\S: ', l.split(':',1)[1] if ':' in l else '') : print(i+1,l)
" | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  grep -n ": .*: " attempts/000140-churchland-2010-01.yaml | head; grep -nE "^\s+[^-][^:]*: " attempts/000140-churchland-2010-01.yaml | grep -vE "^\s*[0-9]+:\s+[a-z_]+: " | head; grep -n "—\|rather\|\*\*" attempts/000140-churchland-2010-01.yaml entries/000140-churchland-2010/maze_prep.py $TMPDIR/nb_src.py | grep -v "Result:" | head
```

```
entries/000140-churchland-2010/maze_prep.py:265:    return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
entries/000140-churchland-2010/maze_prep.py:280:    return 1.0 - np.mean(press ** 2) / np.var(x)
entries/000140-churchland-2010/maze_prep.py:319:    ev = s ** 2 / np.sum(s ** 2)
/tmp/claude-1001/nb_src.py:4:# **Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
/tmp/claude-1001/nb_src.py:8:# **Claims.** `claims/000140/10.1016-j.neuron.2010.09.015.yaml`, written from the NIH author manuscript
/tmp/claude-1001/nb_src.py:13:# **Dataset.** DANDI:000140, version 0.220113.0408 (doi:10.48324/dandi.000140/0.220113.0408), streamed.
/tmp/claude-1001/nb_src.py:169:        pred = int(np.sum((X[i] - m1) ** 2) < np.sum((X[i] - m0) ** 2))
/tmp/claude-1001/nb_src.py:416:                rows.append({"O3": o, "O4": f, "O1": O1, "O2": O2, **broad(fig4_corrs(cfg, sel)[0])})
/tmp/claude-1001/nb_src.py:431:# (O1a).** Under O1a (12 readings) the median correlation is near zero (-0.098 to 0.016), 92% to 100% of
/tmp/claude-1001/nb_src.py:479:                             **judge_tc(mv)})
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import os,re
p=os.environ['TMPDIR']+'/nb_src.py'; s=open(p).read()
for a in ["**Paper.**","**Claims.**","**Dataset.**","**How the analysis differs from the paper's.**","**What was found about the dataset.**"]:
    assert a in s, a
    s=s.replace(a,a.strip('*'))
open(p,'w').write(s)
print([m for m in re.findall(r"\*\*[^*]+\*\*", s) if not m.startswith("**Result")])
EOF
. $TMPDIR/scratch/bin/activate; python $TMPDIR/build_nb.py $TMPDIR/nb_src.py entries/000140-churchland-2010/reproduce_churchland_2010.ipynb; date -u
```

```
['** 2) < np.sum((X[i] - m0) **', '**broad(fig4_corrs(cfg, sel)[0])})\nbroad_table = pd.DataFrame(rows)\nprint(broad_table.round(3).to_string(index=False))\nprint("readings passing:", int(broad_table["pass"].sum()), "of", len(broad_table))\nprint("main reading r range: %.2f to %.2f" % (r_main.min(), r_main.max()))\nfig, ax = plt.subplots(1, 2, figsize=(8, 3))\nfor a, r, t in ((ax[0], r_main, "O2 i (main)"), (ax[1], r_ii, "O2 ii")):\n    a.hist(r, bins=np.arange(-1, 1.01, 0.1), color="0.4")\n    a.axvline(r.mean(), color="r")\n    a.set_xlabel("r, preparatory vs peri-movement"); a.set_title(f"{t}, n = {len(r)}")\nax[0].set_ylabel("units")\nplt.tight_layout(); plt.show()\n\n# %% [markdown]\n# **', '**judge_tc(mv)})\ntc_table = pd.DataFrame(rows)\nprint(tc_table.round(3).to_string(index=False))\nprint("readings passing:", int(tc_table["pass"].sum()), "of", len(tc_table))\ngo_m, mv_m = curves[("a", "a", "range", "i", "a")]\ngo_b, mv_b = curves[("a", "a", "range", "i", "b")]\nprint("main, fig4 units: r from %.2f to %.2f over -400..400 ms re onset" % (mv_m.min(), mv_m.max()))\nprint("main, all prep-tuned units: r at -400 %.2f, -200 %.2f, -100 %.2f, 0 %.2f, +200 %.2f"\n      % tuple(mv_b[np.isin(LAGS_MV, [-400, -200, -100, 0, 200])]))\nfig, ax = plt.subplots(1, 2, figsize=(8, 3), sharey=True, gridspec_kw={"width_ratios": [1, 2]})\nfor go, mv, lab in ((go_m, mv_m, "fig4 units"), (go_b, mv_b, "all > 5 spikes/s")):\n    ax[0].plot(LAGS_GO, go, label=lab); ax[1].plot(LAGS_MV, mv, label=lab)\nax[0].set_xlabel("ms re go cue"); ax[1].set_xlabel("ms re movement onset"); ax[0].set_ylabel("mean r with preparatory rates")\nfor a in ax: a.axhline(0, color="k", lw=0.5)\nax[1].legend(); plt.tight_layout(); plt.show()\n\n# %% [markdown]\n# **', '**tasks}\n                    beaten = [k for k, v in others.items() if v >= best_p]\n                    rows.append({"O3": key[0], "O4": key[1], "O1": O1, "kmax": kmax, "kin end": end, "segments": seg,\n                                 "n": int
[... 1 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000140-churchland-2010/README.md",
 "content": "# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000140\n\nTests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can\nbe tested on [DANDI:000140](https://dandiarchive.org/dandiset/000140/0.220113.0408) (MC_Maze_Small of\nthe Neural Latents Benchmark), which holds 100 trials of 27 maze conditions recorded with the two Utah\narrays of monkey J. The paper's J-array dataset has 108 conditions and about 2166 trials per neuron; its\nsingle-electrode datasets of monkeys A, B and J and its EMG are not in the dandiset.\n\n| Claim | Outcome |\n|---|---|\n| Mean preparatory to peri-movement tuning correlation, J-array (r = 0.13) | Not reproduced |\n| The same for monkeys A, B and J | Blocked: data missing |\n| Correlations broad and centred near zero | Partially reproduced (assumption) |\n| Correlation falls to near zero by movement onset | Reproduced (assumption) |\n| Population averages lose preparatory tuning by movement onset | Reproduced |\n| PD performance best in the peri-movement space, J-array | Reproduced (assumptions) |\n| The same for monkeys A, B and J | Blocked: data missing |\n| Peri-movement space best at each dimensionality | Not reproduced |\n| Endpoints + max. speed space performs poorly in the maze task | Not reproduced (assumption) |\n| Performance rises with dimensionality, then declines above 10 | Not reproduced (assumption) |\n| Summary ranking across monkeys A, B and J (Figure 6E) | Blocked: data missing |\n| 7 to 10 dimensions capture 90% of preparatory variance | Not reproduced |\n| Shuffled peri-movement space performs poorly | Reproduced |\n| Window start can slide to movement onset (97% of performance) | Not reproduced |\n| Tuning correlation does not depend on AP location, J-array | Reproduced (assumption) |\n| The same for monkeys A, B and J | Blocked: data missing |\n| Peri-movement space works at anterior and posterior sites | Not reproduced (assumption) |\n| Preparatory activity more prevalent at anterior sites | Not reproduced (assumption) |\n| PD more stable in the peri-movement space | Not reproduced |\n| Rotational linear system: low correlation, perfect PD | Reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nWith 1 to 4 trials per condition the condition means are noisy (median split-half reliability of\npreparatory tuning 0.20), and when tuning is read as the range across conditions every preferred\ndirection space performs below zero. Several outcomes change when tuning is read as the SD across\nconditions, which keeps 7 or 8 units. Every unit's electrode entry points to the PMd group and the\nelectrodes have no positions, so the anterior-posterior claims use the array read from the unit ids.\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000140-churchland-2010-01.yaml`](../../attempts/000140-churchland-2010-01.yaml).\n\n- `reproduce_churchland_2010.ipynb`: the analysis, about two minutes.\n- `maze_prep.py`: loading, condition means, tuning measures, the leave-one-condition-out PD\n  performance, the peri-movement, kinematic and task spaces, and the Figure 8 simulation. Other\n  notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/000140-churchland-2010/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/000140-churchland-2010 2>&1 | tail -4 && python tools/entry.py handover entries/000140-churchland-2010 2>&1 | tail -5; git status --short; date -u
```

```
Installed kernelspec registry-000140-churchland-2010 in executed/000140-churchland-2010/.venv/share/jupyter/kernels/registry-000140-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (110 s)
wrote executed/000140-churchland-2010/handover
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
?? attempts/000140-churchland-2010-01.yaml
?? entries/000140-churchland-2010/
?? scripts
Thu Oct 29 00:31:41 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/000140-churchland-2010 && . $TMPDIR/scratch/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('reproduce_churchland_2010.ipynb',4)
out=[]
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': out.append(o['text'])
open('/tmp/claude-1001/exec2.txt','w').write('\n'.join(out))
EOF
diff <(grep -v " s$\|in [0-9.]* s\|ran in" $TMPDIR/exec.txt) <(grep -v " s$\|in [0-9.]* s\|ran in" $TMPDIR/exec2.txt) && echo same; ls handover
```

```
606c606
< /tmp/claude-1001/ipykernel_57/3729054532.py:15: RuntimeWarning: invalid value encountered in divide
---
> /tmp/claude-1001/ipykernel_27/3729054532.py:15: RuntimeWarning: invalid value encountered in divide
10.1016-j.neuron.2010.09.015.yaml
maze_prep.py
reproduce_churchland_2010.ipynb
```

**Agent**

I finished steps 1 to 5 and ran the handover (step 6). The entry passes `lock` and `all` with 0 errors, and the notebook runs in 110 s. I did not verify my own work, asked no reader any question, and committed nothing.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig4d-mean-correlation-j-array | not reproduced (mean r −0.079, Spearman −0.020; no reading within tolerance or positive at p < 0.05) |
| fig4abc-mean-correlation-other-datasets | blocked: data_missing |
| fig4-broad-near-zero | partially reproduced (assumed): the interquartile range is 0.17–0.29, below the required 0.3; the other four conditions hold |
| fig4e-correlation-time-course | reproduced (assumed): 0.295 at −200 ms falls to −0.078 at onset |
| suppfig1-population-averages-lose-tuning | reproduced |
| fig6d-perimovement-best-j-array | reproduced (assumed); every space scores below zero under the main reading |
| fig6abc-perimovement-best-other-datasets | blocked: data_missing |
| fig6-perimovement-best-each-dimensionality | not reproduced |
| fig6-maze-endpoint-speed-space-poor | not reproduced (assumed) |
| fig6-dimensionality-trend | not reproduced (assumed) |
| fig6e-summary-rank | blocked: data_missing (a J-array version without EMG is shown) |
| prep-dimensionality-7-to-10 | not reproduced (16 components; shuffled labels also give 16–17) |
| fig7a-shuffled-space-poor | reproduced |
| fig7b-window-start-slide | not reproduced |
| ap-location-no-effect-j-array | reproduced (assumed; r = 0.105, p = 0.668) |
| ap-location-no-effect-other-datasets | blocked: data_missing |
| fig7c-anterior-posterior-performance | not reproduced (assumed) |
| prep-activity-more-anterior | not reproduced (assumed) |
| fig7d-pd-consistency | not reproduced (segment directions beat the peri-movement space) |
| fig8-linear-dynamics-simulation | reproduced |

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.220113.0408, the only published version. The paper cites none. The draft holds the same two assets.

**What the dandiset holds.** One J-array session (Jenkins, 2009-09-28): 100 trials over 27 maze conditions. After the paper's delay > 400 ms rule, 78 trials remain, 1 to 4 per condition. It has 142 units. The paper's J-array data had 108 conditions and about 2166 trials per neuron. The condition means here are therefore noisy: the median split-half reliability of preparatory tuning is 0.20. The 100 test segments have no conditions or behaviour, and none duplicates a train trial. The single-electrode data of monkeys A, B and J and all EMG are absent.

**Metadata problems.**
- Every unit's `electrodes` entry points to the PMd group, although the unit ids carry two array prefixes (72 units with 1, 70 with 2).
- All electrode x, y, z and impedance values are NaN, so no unit has an anterior-posterior position.
- 22 of the 100 trials have delays of 400 ms or less, which the paper excludes.
- How the 27 conditions and 100 trials were chosen is not documented.

**Assumptions** (each run under every reading, all shown in the notebook):
- **O1, the measure of "spikes/s of tuning":** the range across conditions. Under the SD reading, which keeps 7 or 8 units, four outcomes change (fig4-broad, fig4e, the endpoint-speed claim and the dimensionality trend).
- **O3, movement onset:** the dataset's `move_onset_time`.
- **O4, the trial filter:** the proto-trial is the trial best correlated with its condition mean. Under the other filter or onset readings, fig6d drops to partially reproduced.
- **Array mapping:** id prefix 1 is PMd and prefix 2 is M1, with array identity standing in for anterior-posterior location.

**Questions for the paper's authors** (recorded as three `methods_unavailable` findings):
- How was preparatory tuning measured for the inclusion rule?
- How was the proto-trial chosen, and how was movement onset detected?
- For the task spaces: where does the reach end, are segments equal in length or duration, is peak velocity signed, how were axes scaled for Figure 7D, and does the upper-limit space include the fitted neuron?

## 3. Where the protocol was unclear or missing something

1. **A criterion can stop making sense.** In fig7c the upper limit is ≤ 0, so normalised performance is undefined. In fig7b both performances are negative, so their ratio means nothing. The protocol has no rule for this. I recorded `not_reproduced` and explained why in the notes.
2. **No partial rule in a criterion.** fig4-broad's criterion only defines "reproduced", but four of its five conditions held. I used `partially_reproduced`.
3. **Many interacting open details.** O1, O2, O3, O4 and the task-space details give up to 96 readings per claim. The protocol does not say whether an adopted assumption must be the same across claims. I kept it the same for all claims.
4. **A dataset too small to resolve the effect.** The protocol has no notion of statistical power, so a claim can be "not reproduced" only because the subset is tiny. I said so in the notes and recorded a `data_missing` finding.
5. **`measured` when one expected value cannot be computed.** For fig7b the monkeys A and B value is not in the dandiset. I gave the single J value.
6. **Metadata assumptions versus method assumptions.** Step 1.6 covers method details. The array-to-region mapping is a metadata question; I treated it the same way, as an assumption with both readings shown.

## 4. Runtime and failures

The work took about 30 minutes (00:05 to 00:32 UTC). The notebook runs in 110 s in the clean environment, and two executed runs gave identical numbers. Nothing failed.

The repository root has untracked dotfiles (`.bashrc`, `.idea`, `scripts`, and similar) that I did not create and left untouched.

Files are in `entries/000140-churchland-2010/`:
- `reproduce_churchland_2010.ipynb`
- `maze_prep.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/000140-churchland-2010-01.yaml`, and the verifier's package is in `executed/000140-churchland-2010/handover/`.

## End of run

57 turns, 25 minutes, result: success.
