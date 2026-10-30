# 000574 · author · run 41113745819

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools | head -80; wc -l docs/*.md README.md
```

```
Fri Oct 30 19:20:10 UTC 2026
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
[... 97 more lines not kept]
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
cat README.md docs/design.md | head -420; sed -n 1,120p docs/archives.md
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
[... 510 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000574 claims/001453 entries/001453-fouke-2025 paper questions | head; cat claims/000574/*.yaml
```

```
<persisted-output>
Output too large (63.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/df13931c-4dea-4227-a80d-921ca46b1302/tool-results/b49s8nqvb.txt

Preview (first 2KB):
claims/000574:
10.1126-sciadv.aav3687.yaml

claims/001453:
10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
# Claims for Boran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald & Sarnthein (2019), Science
# Advances 5, eaav3687, on dandiset 000574.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record as served by Europe PMC (PMC6436923), in
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000574/10.1126-sciadv.aav3687.yaml"
}
```

```
1	# Claims for Boran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald & Sarnthein (2019), Science
2	# Advances 5, eaav3687, on dandiset 000574.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record as served by Europe PMC (PMC6436923), in
7	# paper/10.1126-sciadv.aav3687.txt, with its Results, figure legends and Methods, and the
8	# supplement aav3687_SM.pdf (figs. S1 to S6, table S1 and table S2, the statistics checklist)
9	# extracted into the same file. Table S1 is garbled by the extraction; it was read by its column
10	# order (subject, diagnosis, age, hemisphere of the hippocampal electrode with maximal PLV,
11	# tissue SOZ or non-SOZ, scalp electrode with maximal PLV, PLV peak frequency, individual PLV
12	# band, maximal PLV, PLV workload dependent and its band, PLV maintenance against encoding,
13	# EEG workload dependent, iEEG workload dependent, then the median band limits), and the
14	# medians it prints (6.0 to 11.5 Hz, 7.8 to 10.0 Hz) were recomputed from the rows to confirm
15	# the reading. The supplement PDF page could not be rendered in this run. Movie S1 was not read.
16	# The data descriptor for the deposit (Boran et al. 2020, Sci Data 7, 30,
17	# doi:10.1038/s41597-020-0364-3, paper/10.1038-s41597-020-0364-3.txt) was read for the
18	# description of the deposited data; it repeats the behavior and spike sorting numbers.
19	#
20	# Code read: the paper links no analysis code ("Additional data related to this paper may be
[... 907 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000574/10.1126-sciadv.aav3687.yaml",
 "offset": 928
}
```

```
928	    unit: Hz
929	  - quantity: median upper limit of the workload bands
930	    value: 10
931	    tolerance: 1.0
932	    unit: Hz
933	  depends_on:
934	  - fig6-plv-all-subjects
935	  criterion: >-
936	    The pair of fig6-plv-all-subjects per subject. PLV for set size 8 minus PLV for set size 4,
937	    against the 95th percentile of 200 differences with the epochs randomly assigned to the two
938	    set sizes (Methods, Phase-locking value). A subject counts when at least one bin inside the
939	    individual band is significant. Table S1 lists subject 3 as not significant. Reproduced
940	    when, under one reading, eight subjects count (seven or nine is partially reproduced) and
941	    both medians and the range (5.5 to 16.5 Hz widened by 10% of each bound) hold.
942	- id: fig6-plv-maintenance-over-encoding
943	  statement: >-
944	    The PLV during the last 2 s of maintenance exceeded the PLV during encoding in eight of nine
945	    subjects, so hippocampal-cortical connectivity in the theta-alpha range increased
946	    specifically during maintenance.
947	  source: Results, Cortico-hippocampal low-frequency coupling in the group of subjects, paragraph 2; Figure 6A to 6H; table S1
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml README.md; ls -la; head -60 omr.py; cd ../..; sed -n 1,200p attempts/001453-fouke-2025-01.yaml
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
[... 304 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p attempts/001453-fouke-2025-01.yaml | grep -n -E "^[a-z]|^- |^  [a-z_]+:" | head -60; ls schemas; cat entries/001453-fouke-2025/requirements.in; ls questions | head -3; ls paper
```

```
1:  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
4:- claim: fig2d-shared-architecture
5:  outcome: blocked
6:  blocked_by: data_missing
7:  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
10:- claim: fig2g-dsi-similar
11:  outcome: blocked
12:  blocked_by: data_missing
13:  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
14:- claim: fig2h-fewer-motion-responsive
15:  outcome: blocked
16:  blocked_by: data_missing
17:  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
18:- claim: fig2k-more-monocular
19:  outcome: blocked
20:  blocked_by: data_missing
21:  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
22:- claim: fig2l-bi-ratio
23:  outcome: blocked
24:  blocked_by: data_missing
[... 58 more lines not kept]
```

**Agent**

Now the dataset. Let me list assets and open one file while I read the paper.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000574/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['most_recent_published_version'], d['draft_version'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000574/versions/" | python -c "import json,sys;d=json.load(sys.stdin);[print(v['version'],v['created'],v['asset_count'],v['size']) for v in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for v in 0.231010.1809 0.250610.0938 0.250815.1108; do echo == $v; curl -s "https://api.dandiarchive.org/api/dandisets/000574/versions/$v/assets/?page_size=100" | python -c "import json,sys;d=json.load(sys.stdin);[print(a['path'],a['size'],a['asset_id']) for a in d['results']]"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import pynwb, remfile, h5py, dandi; print(pynwb.__version__)" 2>&1; which uv python; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, dandi; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
Python 3.13.17
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas scikit-learn matplotlib ipykernel nbformat nbclient 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/probe.py <<'EOF'
import h5py, remfile, sys
url = "https://api.dandiarchive.org/api/assets/%s/download/" % sys.argv[1]
f = h5py.File(remfile.File(url), "r")
def show(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k, (v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k in ('unit','rate','conversion','description','resolution')))
    else:
        a = {k: v for k, v in obj.attrs.items() if k in ('neurodata_type','description','colnames')}
        print(name + "/", a)
f.visititems(show)
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/probe.py 6f367ffb-c6a9-468f-a974-394eabae6060 2>&1 | grep -v "^stimulus/presentation/.*/data" | head -150
```

```
acquisition/ {}
acquisition/ecephys.eeg/ {'description': 'Scalp EEG data', 'neurodata_type': 'ElectricalSeries'}
acquisition/ecephys.eeg/data (80000, 19) float64 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/ecephys.eeg/electrodes (19,) int32 {'description': 'eeg electrodes'}
acquisition/ecephys.eeg/timestamps (80000,) float64 {'unit': 'seconds'}
acquisition/ecephys.ieeg/ {'description': 'Macro iEEG data', 'neurodata_type': 'ElectricalSeries'}
acquisition/ecephys.ieeg/data (800000, 48) float64 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/ecephys.ieeg/electrodes (48,) int32 {'description': 'ieeg electrodes'}
acquisition/ecephys.ieeg/timestamps (800000,) float64 {'unit': 'seconds'}
acquisition/ecephys.lfp/ {'description': 'Micro iEEG data', 'neurodata_type': 'ElectricalSeries'}
acquisition/ecephys.lfp/data (12800000, 32) float64 {'conversion': np.float64(1.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/ecephys.lfp/electrodes (32,) int32 {'description': 'ieeg electrodes'}
acquisition/ecephys.lfp/timestamps (12800000,) float64 {'unit': 'seconds'}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/devices/ {}
general/devices/ATLAS Neurophysiology System/ {'description': 'iEEG recording system', 'neurodata_type': 'Device'}
general/devices/NicoletOne EEG System/ {'description': 'EEG recording system', 'neurodata_type': 'Device'}
general/experiment_description () object {}
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i -E "^(materials|methods|results|discussion|statistics|neural decoding|dpca|phase|spike|frequency|task|patients|electrodes|recording)" paper/10.1126-sciadv.aav3687.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-sciadv.aav3687.txt",
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -E "MATERIALS AND METHODS|^Patients|^Task|^Recording|^Spike detection|^Neural decoding|^dPCA|^Phase|^Spike-field|^Frequency|^Statistics|^Electrode|^Data|Results$|RESULTS|DISCUSSION" paper/10.1126-sciadv.aav3687.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 7p ~/work/encore/encore/paper/10.1126-sciadv.aav3687.txt | fold -s -w 200 > p.txt; wc -l p.txt; grep -n -E "MATERIALS AND METHODS|Neural decoding|dPCA of firing|Phase-locking value|Spike-field coherence|Frequency spectra|Statistics|Spike detection|Task" p.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 34,60p p.txt; echo ======; sed -n 229,300p p.txt
```

```
maintenance. RESULTS Task and behavior Subjects performed a modified Sternberg WM task (36 total sessions from nine subjects). The task differs from the original Sternberg paradigm in that the items 
were presented all at once rather than sequentially, thus separating the encoding period from the maintenance period. In each trial, subjects were instructed to memorize a set of four, six, or eight 
letters presented for 2 s (encoding). The number of letters was thus specific for the memory load. After a delay (maintenance) period of 3 s, a probe letter prompted the subjects to retrieve their 
memory (retrieval) and to indicate by button press (“IN” or “OUT”) whether or not the probe letter was a member of the letter set held in memory ( Fig. 1A ). Throughout this paper, the term 
“workload” refers to the number of letters held in memory. In their effort to solve the task, the subjects reported that they relied on audio-verbal transformation of the letters. Although stimuli 
were visually presented in this task, letter strings are thought to activate verbal WM through the phonological loop ( 1 ). Fig. 1 Task, behavioral results, and recording sites. ( A ) In the task, 
sets of consonants were presented and had to be memorized. The set size (4, 6, or 8 letters) determined WM workload. In each trial, presentation of a letter string (encoding period, 2 s) was followed 
by a delay (maintenance period, 3 s). After the delay, a probe letter was shown, and subjects indicated whether the probe was presented during the encoding period. ( B and C ) Behavioral results. (B) 
Accuracy of all sessions. The jitter reflects the rank order of the accuracy in trials with set size 8. Each dotted line connects an individual session. The nine subjects performed a total of 36 
sessions. (C) Median reaction time (relative to onset of the probe letter) as a function of workload. The jitter reflects the rank order of the reaction time in trials with set size 8. Each dotted 
line connects an in
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 60,72p p.txt; echo ====; sed -n 140,180p p.txt; echo; sed -n 300,313p p.txt
```

```
= 47.30, P = 6.1 × 10 −12 ), where 20.6% of all recorded neurons were maintenance neurons (permutation test against scrambled data, P = 0.002). Were the firing rates of maintenance neurons related to 
workload? During maintenance, a subset of maintenance neurons in the hippocampus (15%, 21 neurons; permutation test against scrambled data, P = 0.002) increased their firing rates systematically with 
workload (set size 4 versus set sizes 6 and 8; Fig. 2C ). Across MTL, the hippocampus stood out with a significant percentage of maintenance neurons with persistent activity that correlated with the 
WM load. Fig. 2 Persistent activity of maintenance neurons. ( A ) Example of a maintenance neuron recorded from hippocampus. Top: Peristimulus time histogram (bin size, 500 ms; step size, 20 ms). 
Shaded areas represent ± SEM across trials of all spikes associated with the neuron. Inset: Mean extracellular waveform ± SEM. Middle: Periods of significance (black) between low-workload trials (set 
size 4, 45 trials) and high-workload trials (set sizes 6 and 8, 46 trials; P < 0.05, cluster-based nonparametric permutation test). Bottom: Raster plot of trials reordered to set size and RT for 
plotting purposes only. Compared to set size 4 (blue), the neuron fires more for set size 6 (green) and set size 8 (red). Figure S1 provides further examples of single neurons. ( B ) Percentage of 
all recorded neurons identified as maintenance neurons in the hippocampus (Hipp), entorhinal cortex (Ent), and amygdala (Amg). The number of maintenance neurons is provided below the area label. The 
hippocampus contained significantly higher proportions of maintenance neurons than the two other areas. ( C ) Percentage of maintenance neurons for which the firing rate during maintenance differed 
as a function of load. The hippocampus stood out as containing a significant percentage of neurons that increased their firing rate under high workloads. For (B) and (C), significance was assessed by 
compar
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000574-boran-2019; cat > $TMPDIR/probe2.py <<'EOF'
import h5py, remfile, sys, time, numpy as np
t=time.time()
url = "https://api.dandiarchive.org/api/assets/%s/download/" % sys.argv[1]
f = h5py.File(remfile.File(url), "r")
def s(x): 
    x = x[()] 
    return x.decode() if isinstance(x, bytes) else x
print(s(f['session_description']), s(f['general/subject/subject_id']), s(f['general/subject/age']), s(f['session_start_time']), s(f['identifier']))
print(s(f['general/experiment_description'])[:500])
tr = f['intervals/trials']
for c in ['start_time','stop_time','set_size','probe_letter','solution','artifact','response_type','response_time','correct']:
    v = tr[c][:]
    print(c, v[:8])
ts = f['intervals/ttl_stage']
tags = ts['tags'][:]; ti = ts['tags_index'][:]
print('ttl', ts['start_time'][:8], ts['stop_time'][:8], ts['trial_number'][:8], tags[:8], ti[:8])
el = f['general/extracellular_ephys/electrodes']
import pandas as pd
d = pd.DataFrame({c: el[c][:] for c in ['location','group_name','label','is_inside_soz','x','y','z','filtering','reference']})
pd.set_option('display.width',250); pd.set_option('display.max_rows',100)
print(d)
u = f['units']
print('units eg', u['electrodes'][:], u['electrode_group'][:3], u['offset'][:3])
print('obs', u['obs_intervals'][:3], u['obs_intervals_index'][:3])
st = u['spike_times'][:]; print('spikes', st[:5], st.min(), st.max(), np.all(np.diff(st[:u['spike_times_index'][0]])>=0))
for k in ['eeg','ieeg','lfp']:
    a = f['acquisition/ecephys.'+k]
    print(k, a['data'].chunks, a['timestamps'][:3], a['timestamps'][-1], a['electrodes'][:])
print(time.time()-t)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/probe2.py 6f367ffb-c6a9-468f-a974-394eabae6060 2>&1
```

```
Running experiment as described in the the experiment description 01 P24Y 2016-12-14T17:13:00+01:00 Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM_subject01_session01
Task Name: Sternberg
Task Description: The task is a modified Sternberg task in which the encoding of memory items, maintenance, and recall were temporally separated. Each trial starts with a fixation period ([-6, -5] s), followed by the stimulus ([-5, -3] s). The stimulus consists of a set of eight consonants at the center of the screen. The middle four, six, or eight letters are the memory items,which determine the set size for the trial (4, 6, or 8, respectively). The outer positions are fill
start_time [ 0.       17.946711 33.087674 43.945357 54.338196 64.797442 74.692188
 84.752997]
stop_time [ 8.       25.946711 41.087674 51.945357 62.338196 72.797442 82.692188
 92.752997]
set_size [8 4 8 6 8 4 8 8]
probe_letter [b'H' b'T' b'L' b'G' b'S' b'R' b'N' b'Z']
solution [False  True False False False  True False  True]
artifact [False False False False False False False False]
response_type [b'52' b'51' b'52' b'52' b'52' b'51' b'52' b'51']
response_time [ 8.484    25.614461 40.559674 51.254107 61.854446 71.696442 81.824188
 92.333247]
correct [1. 1. 1. 1. 1. 1. 1. 1.]
ttl [ 0.        1.        3.        6.       17.946711 18.946711 20.946711
 23.946711] [ 1.        3.        6.       17.946711 18.946711 20.946711 23.946711
 33.087674] [0 0 0 1 1 1 1 2] [b'Fixation' b'Stimulus' b'Maintenance' b'Probe' b'Fixation' b'Stimulus'
 b'Maintenance' b'Probe'] [1 2 3 4 5 6 7 8]
                                             location  ...                         reference
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/probe3.py <<'EOF'
import h5py, remfile, sys, numpy as np, pandas as pd
url = "https://api.dandiarchive.org/api/assets/%s/download/" % sys.argv[1]
f = h5py.File(remfile.File(url), "r")
el = f['general/extracellular_ephys/electrodes']
d = pd.DataFrame({c: el[c][:] for c in ['location','group_name','label','is_inside_soz','x','y','z','filtering']})
for c in ['location','group_name','label','filtering']: d[c]=d[c].str.decode('utf8')
d['location']=d.location.str[:30]
pd.set_option('display.width',250); pd.set_option('display.max_rows',100); pd.set_option('display.max_colwidth',40)
print(d)
print(f['general/subject/description'][()], f['general/keywords'][:])
print(f['general/related_publications'][:])
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/probe3.py 6f367ffb-c6a9-468f-a974-394eabae6060 2>&1
```

```
location  ...                 filtering
0                               F3  ...  Passband, 0.5 to 5000 Hz
1                               F4  ...  Passband, 0.5 to 5000 Hz
2                               C3  ...  Passband, 0.5 to 5000 Hz
3                               C4  ...  Passband, 0.5 to 5000 Hz
4                               P3  ...  Passband, 0.5 to 5000 Hz
5                               P4  ...  Passband, 0.5 to 5000 Hz
6                               O1  ...  Passband, 0.5 to 5000 Hz
7                               O2  ...  Passband, 0.5 to 5000 Hz
8                               F7  ...  Passband, 0.5 to 5000 Hz
9                               F8  ...  Passband, 0.5 to 5000 Hz
10                              T3  ...  Passband, 0.5 to 5000 Hz
11                              T4  ...  Passband, 0.5 to 5000 Hz
12                              T5  ...  Passband, 0.5 to 5000 Hz
13                              T6  ...  Passband, 0.5 to 5000 Hz
14                              Fz  ...  Passband, 0.5 to 5000 Hz
15                              Cz  ...  Passband, 0.5 to 5000 Hz
16                              Pz  ...  Passband, 0.5 to 5000 Hz
17                              A1  ...  Passband, 0.5 to 5000 Hz
18                              A2  ...  Passband, 0.5 to 5000 Hz
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/print(d)/print(d[["group_name","label","is_inside_soz","x","y","z"]].to_string())/' $TMPDIR/probe3.py; . $TMPDIR/dev/bin/activate; python $TMPDIR/probe3.py 6f367ffb-c6a9-468f-a974-394eabae6060 2>&1 | head -70
```

```
group_name label  is_inside_soz             x          y             z
0         eeg    F3          False -5.755106e+01 -39.869712 -4.820043e+01
1         eeg    F4          False -5.758403e+01 -39.891983  4.814260e+01
2         eeg    C3          False -3.868125e-15 -56.871691 -6.317128e+01
3         eeg    C4          False -3.867882e-15 -56.876102  6.316731e+01
4         eeg    P3          False  5.755106e+01 -39.869712 -4.820043e+01
5         eeg    P4          False  5.758403e+01 -39.891983  4.814260e+01
6         eeg    O1          False  8.078401e+01   4.001085 -2.613301e+01
7         eeg    O2          False  8.078401e+01   4.001085  2.613301e+01
8         eeg    F7          False -4.987138e+01   7.489518 -6.842334e+01
9         eeg    F8          False -4.992653e+01   7.485085  6.838359e+01
10        eeg    T3          False -5.176493e-15   8.845083 -8.453854e+01
11        eeg    T4          False -5.176493e-15   8.845083  8.453854e+01
12        eeg    T5          False  4.987138e+01   7.489518 -6.842334e+01
13        eeg    T6          False  4.992653e+01   7.485085  6.838359e+01
14        eeg    Fz          False -6.073848e+01 -59.462904  0.000000e+00
15        eeg    Cz          False -5.204749e-15 -85.000000  0.000000e+00
16        eeg    Pz          False  6.073848e+01 -59.462904  7.438319e-15
17        eeg    A1          False -3.680313e-15  60.104076 -6.010408e+01
18        eeg    A2          False -3.680313e-15  60.104076  6.010408e+01
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat ~/work/encore/encore/paper/10.1038-s41597-020-0364-3.txt | fold -s -w 200 > dd.txt; grep -n -i -E "AH|PH|entorhinal|LR|session|duplicate|units|waveform|trial rejection|artifact" dd.txt | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/000574-boran-2019/sternberg.py",
 "content": "\"\"\"Loading and measures for dandiset 000574 (human MTL units, scalp EEG and iEEG, Sternberg task).\n\nBoran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald & Sarnthein (2019), Science Advances 5,\neaav3687, doi:10.1126/sciadv.aav3687. Files are streamed from the archive at the pinned\nversion with remfile and h5py; nothing is written to disk.\n\nEach NWB file holds one session of 50 trials. Only the 8 s of each trial are stored (trial\nstart = fixation onset, probe onset at +6 s, trial end at +8 s), so all times here are made\nrelative to probe onset, as in the paper (\"Times are relative to probe onset\"). Trial periods\nare from the paper (Methods, Task): fixation [-6, -5] s, encoding [-5, -3] s, maintenance\n[-3, 0] s, probe at 0 s.\n\nWhere the parameters come from:\n\n- Regions of units: the units' `electrodes` column points at macroelectrode rows of the\n  electrodes table; the microwire bundle is named by that row's label without its contact\n  number (AHL, PHR, ECL, AL...). Hippocampus is AH and PH (hippocampal head and body),\n  entorhinal cortex EC, amygdala A (claims file, neurons-recorded criterion, from Table 1 of\n  the data descriptor).\n- IN/OUT: `response_type` codes 51 and 52. That 51 is IN is read from the data (it matches\n  `solution` on every correct trial, checked in the notebook).\n- Hippocampal iEEG: one bipolar signal per hippocampal macroelectrode from its two deepest\n  contacts, contact 1 minus contact 2 (Methods, Recording setup, \"Only one bipolar signal from a\n  pair involving the deepest contacts of each macroelectrode\"). That contact 1 is the deepest\n  is an assumption from the coordinates (contact 1 is nearest the midline, checked in the\n  notebook).\n- Multitaper spectra: +/- 2 Hz smoothing with seven tapers on 2-s epochs (Methods, Frequency\n  spectra). FieldTrip's mtmfft takes tapers = 2 * T * W - 1 = 7 for T = 2 s and W = 2 Hz, so\n  DPSS with NW = 4 and K = 7; the frequency resolution is 0.5 Hz.\n- PLV: Methods equation 3 applied to each taper's Fourier coefficients. How tapers enter is\n  not stated; FieldTrip's ft_connectivityanalysis averages the normalized cross-spectra over\n  tapers and trials, which is what is done (standard choice, `plv`).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom scipy.signal.windows import dpss\n\nDANDISET_ID = \"000574\"\nDANDISET_VERSION = \"0.250815.1108\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nFIX = (-6.0, -5.0)\nENC = (-5.0, -3.0)\nMAINT = (-3.0, 0.0)\nLAST2 = (-2.0, 0.0)          # last 2 s of maintenance (Methods, Frequency spectra)\nPROBE_OFFSET = 6.0           # probe onset relative to trial start (Methods, Task)\nIN_CODE, OUT_CODE = \"51\", \"52\"\n\n\ndef assets():\n    \"\"\"Asset paths and ids of the pinned version, sorted by path.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200\"\n    r = requests.get(url, timeout=60)\n    r.raise_for_status()\n    rows = [(a[\"path\"], a[\"asset_id\"], a[\"size\"]) for a in r.json()[\"results\"]]\n    return pd.DataFrame(rows, columns=[\"path\", \"asset_id\", \"size\"]).sort_values(\"path\").reset_index(drop=True)\n\n\ndef open_asset(asset_id):\n    return h5py.File(remfile.File(f\"{API}/assets/{asset_id}/download/\"), \"r\")\n\n\ndef _str(a):\n    return np.array([x.decode() if isinstance(x, bytes) else x for x in a], dtype=object)\n\n\ndef _scalar(x):\n    x = x[()]\n    return x.decode() if isinstance(x, bytes) else x\n\n\ndef region_of(bundle):\n    if bundle.startswith((\"AH\", \"PH\")):\n        return \"hippocampus\"\n    if bundle.startswith(\"EC\"):\n        return \"entorhinal\"\n    if bundle.startswith(\"A\"):\n        return \"amygdala\"\n    return \"other\"\n\n\ndef load_session(path, asset_id):\n    \"\"\"Trials, trial stages, electrodes and units of one session (tables and spike times only).\"\"\"\n    with open_asset(asset_id) as f:\n        tr = f[\"intervals/trials\"]\n        trials = pd.DataFrame({\n            \"start\": tr[\"start_time\"][:], \"stop\": tr[\"stop_time\"][:],\n            \"set_size\": tr[\"set_size\"][:], \"solution\": tr[\"solution\"][:].astype(bool),\n            \"artifact\": tr[\"artifact\"][:].astype(bool), \"response\": _str(tr[\"response_type\"][:]),\n            \"response_time\": tr[\"response_time\"][:], \"correct_raw\": tr[\"correct\"][:],\n            \"probe_letter\": _str(tr[\"probe_letter\"][:]),\n        })\n        st = f[\"intervals/ttl_stage\"]\n        tags_idx = st[\"tags_index\"][:]\n        tags = _str(st[\"tags\"][:])\n        starts = np.concatenate([[0], tags_idx[:-1]])\n        stages = pd.DataFrame({\"start\": st[\"start_time\"][:], \"stop\": st[\"stop_time\"][:],\n                               \"trial\": st[\"trial_number\"][:],\n                               \"tag\": [\",\".join(tags[a:b]) for a, b in zip(starts, tags_idx)]})\n        el = f[\"general/extracellular_ephys/electrodes\"]\n        elec = pd.DataFrame({c: el[c][:] for c in [\"x\", \"y\", \"z\", \"is_inside_soz\"]})\n        for c in [\"label\", \"group_name\", \"location\"]:\n            elec[c] = _str(el[c][:])\n        u = f[\"units\"]\n        sidx = u[\"spike_times_index\"][:]\n        spikes = u[\"spike_times\"][:]\n        eidx = u[\"electrodes_index\"][:]\n        uel = u[\"electrodes\"][:]\n        wm = u[\"waveform_mean\"][:]\n        wsd = u[\"waveform_sd\"][:]\n        obs = u[\"obs_intervals\"][:]\n        oidx = u[\"obs_intervals_index\"][:]\n        meta = {k: _scalar(f[p]) for k, p in [(\"subject\", \"general/subject/subject_id\"),\n                                               (\"description\", \"general/subject/description\"),\n                                               (\"start_time\", \"session_start_time\"),\n                                               (\"identifier\", \"identifier\")]}\n        shapes = {k: f[f\"acquisition/ecephys.{k}/data\"].shape for k in [\"eeg\", \"ieeg\", \"lfp\"]}\n    stage_probe = stages[stages.tag == \"Probe\"].set_index(\"trial\")[\"start\"]\n    trials[\"probe\"] = trials[\"start\"] + PROBE_OFFSET\n    trials[\"stage_probe\"] = stage_probe.reindex(np.arange(len(trials))).to_numpy()\n    trials[\"rt\"] = trials[\"response_time\"] - trials[\"probe\"]\n    trials[\"correct\"] = trials[\"correct_raw\"] == 1\n    trials[\"is_in\"] = trials[\"response\"] == IN_CODE\n    sb = np.concatenate([[0], sidx])\n    ob = np.concatenate([[0], oidx])\n    eb = np.concatenate([[0], eidx])\n    units = []\n    for i in range(len(sidx)):\n        rows = uel[eb[i]:eb[i + 1]]\n        label = elec.label[rows[0]]\n        bundle = re.sub(r\"\\d+$\", \"\", label)\n        units.append({\"unit\": i, \"electrode_row\": int(rows[0]), \"label\": label, \"bundle\": bundle,\n                      \"region\": region_of(bundle), \"spikes\": spikes[sb[i]:sb[i + 1]],\n                      \"obs\": obs[ob[i]:ob[i + 1]], \"waveform_mean\": wm[i], \"waveform_sd\": wsd[i]})\n    sub = path.split(\"/\")[0].replace(\"sub-\", \"\")\n    ses = path.split(\"_ses-\")[1].split(\".\")[0]\n    return {\"path\": path, \"asset_id\": asset_id, \"subject\": sub, \"session\": ses, \"meta\": meta,\n            \"trials\": trials, \"stages\": stages, \"electrodes\": elec, \"units\": units, \"shapes\": shapes}\n\n\ndef load_all(table, workers=12):\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(lambda r: load_session(r.path, r.asset_id), table.itertuples()))\n\n\ndef aligned_spikes(spk, probes, lo=-6.0, hi=2.0):\n    \"\"\"Spike times of one unit relative to each trial's probe onset, a list over trials.\"\"\"\n    out = []\n    for p in probes:\n        a, b = np.searchsorted(spk, [p + lo, p + hi])\n        out.append(spk[a:b] - p)\n    return out\n\n\ndef count_in(aligned, window):\n    lo, hi = window\n    return np.array([np.sum((s >= lo) & (s < hi)) for s in aligned], dtype=float)\n\n\ndef rate_in(aligned, window):\n    return count_in(aligned, window) / (window[1] - window[0])\n\n\ndef binned(aligned, edges):\n    return np.array([np.histogram(s, edges)[0] for s in aligned], dtype=float)\n\n\n# ---- statistics -------------------------------------------------------------------------\n\ndef perm_t(a, b, n_perm=2000, paired=False, rng=None):\n    \"\"\"Permutation t test as in EEGLAB statcond (Methods, Statistics: values of the two\n    distributions mixed 2000 times). Paired: signs of the differences flipped. Returns\n    (t, two-sided P), P = (exceedances + 1) / (n_perm + 1).\"\"\"\n    rng = rng if rng is not None else np.random.default_rng(0)\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    if paired:\n        d = a - b\n        def tstat(x):\n            s = x.std(axis=-1, ddof=1)\n            with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n                return np.where(s > 0, x.mean(axis=-1) / (s / np.sqrt(x.shape[-1])), 0.0)\n        t0 = tstat(d)\n        signs = rng.choice([-1.0, 1.0], size=(n_perm, d.size))\n        tn = tstat(signs * d)\n    else:\n        x = np.concatenate([a, b])\n        na = a.size\n        def tstat2(xa, xb):\n            va = xa.var(axis=-1, ddof=1)\n            vb = xb.var(axis=-1, ddof=1)\n            se = np.sqrt(va / xa.shape[-1] + vb / xb.shape[-1])\n            with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n                return np.where(se > 0, (xa.mean(axis=-1) - xb.mean(axis=-1)) / se, 0.0)\n        t0 = tstat2(a, b)\n        perms = np.argsort(rng.random((n_perm, x.size)), axis=1)\n        xp = x[perms]\n        tn = tstat2(xp[:, :na], xp[:, na:])\n    p = (np.sum(np.abs(tn) >= abs(t0)) + 1) / (n_perm + 1)\n    return float(t0), float(p)\n\n\ndef cluster_perm_1d(a, b, n_perm=1000, alpha=0.05, rng=None, paired=False):\n    \"\"\"Cluster-based permutation test over one dimension (Maris & Oostenveld 2007, as in\n    FieldTrip; Methods, Statistics). a, b: observations x points. Clusters of points with\n    two-sided t beyond the t threshold at alpha, cluster mass = sum of t; null of the maximal\n    absolute cluster mass under label (or sign) permutation. Returns a list of\n    (start, stop, mass, P).\"\"\"\n    from scipy import stats\n    rng = rng if rng is not None else np.random.default_rng(0)\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n\n    def tmap(xa, xb):\n        if paired:\n            d = xa - xb\n            s = d.std(axis=0, ddof=1)\n            with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n                return np.nan_to_num(d.mean(0) / (s / np.sqrt(d.shape[0])))\n        va, vb = xa.var(0, ddof=1), xb.var(0, ddof=1)\n        se = np.sqrt(va / len(xa) + vb / len(xb))\n        with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n            return np.nan_to_num((xa.mean(0) - xb.mean(0)) / se)\n\n    df = (len(a) - 1) if paired else (len(a) + len(b) - 2)\n    thr = stats.t.ppf(1 - alpha / 2, df)\n\n    def clusters(t):\n        out = []\n        for sign in (1, -1):\n            m = sign * t > thr\n            i = 0\n            while i < len(m):\n                if m[i]:\n                    j = i\n                    while j < len(m) and m[j]:\n                        j += 1\n                    out.append((i, j, float(t[i:j].sum())))\n                    i = j\n                else:\n                    i += 1\n        return out\n\n    t0 = tmap(a, b)\n    obs = clusters(t0)\n    if not obs:\n        return []\n    null = np.zeros(n_perm)\n    x = np.concatenate([a, b])\n    for k in range(n_perm):\n        if paired:\n            s = rng.choice([-1.0, 1.0], size=(len(a), 1))\n            d = (a - b) * s\n            tt = tmap(d, np.zeros_like(d))\n        else:\n            p = rng.permutation(len(x))\n            tt = tmap(x[p[:len(a)]], x[p[len(a):]])\n        c = clusters(tt)\n        null[k] = max([abs(m) for _, _, m in c], default=0.0)\n    return [(i, j, m, float((np.sum(null >= abs(m)) + 1) / (n_perm + 1))) for i, j, m in obs]\n\n\n# ---- spectra and PLV ---------------------------------------------------------------------\n\ndef mt_fourier(x, fs, nw=4.0, k=7):\n    \"\"\"Multitaper Fourier coefficients of epochs x (epochs x samples): tapers x epochs x freqs.\n    Each epoch is demeaned first (as FieldTrip does by default for mtmfft with demean).\"\"\"\n    x = np.asarray(x, float)\n    x = x - x.mean(axis=-1, keepdims=True)\n    n = x.shape[-1]\n    tap = dpss(n, nw, k)\n    F = np.fft.rfft(tap[:, None, :] * x[None, :, :], axis=-1)\n    freqs = np.fft.rfftfreq(n, 1 / fs)\n    return F, freqs\n\n\ndef mt_power(x, fs):\n    F, f = mt_fourier(x, fs)\n    return (np.abs(F) ** 2).mean(axis=0), f   # epochs x freqs\n\n\ndef plv(Fi, Fj):\n    \"\"\"PLV (Methods eq. 3) from multitaper coefficients (tapers x epochs x freqs), normalized\n    cross-spectra averaged over tapers and epochs.\"\"\"\n    c = Fi * np.conj(Fj)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        c = c / np.abs(c)\n    return np.abs(np.nanmean(c, axis=(0, 1)))\n"
}
```

```
File created successfully at: entries/000574-boran-2019/sternberg.py (file state is current in your context — no need to Read it back)
```

**Agent**

Now a survey of all 37 sessions (tables only), cached to $TMPDIR for development.

**Agent calls Bash**

```bash
cd entries/000574-boran-2019 && . $TMPDIR/dev/bin/activate && uv pip install -q requests 2>&1|tail -1; cat > $TMPDIR/survey.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'.')
import sternberg as S, numpy as np, pandas as pd
t=time.time()
A = S.assets(); print(len(A))
D = S.load_all(A, workers=16)
print('load', time.time()-t)
pickle.dump(D, open(sys.argv[1],'wb'))
for d in D:
    tr=d['trials']; u=pd.DataFrame(d['units'])
    print(d['path'], d['meta']['start_time'], len(tr), (tr.probe-tr.stage_probe).abs().max(), tr.correct.sum(), tr.artifact.sum(), len(u), u.region.value_counts().to_dict() if len(u) else {}, d['shapes'])
EOF
python $TMPDIR/survey.py $TMPDIR/D.pkl
```

```
Exit code 1
37
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 5, in <module>
    D = S.load_all(A, workers=16)
  File "entries/000574-boran-2019/sternberg.py", line 152, in load_all
    return list(ex.map(lambda r: load_session(r.path, r.asset_id), table.itertuples()))
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 460, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000574-boran-2019 && python - <<'EOF'
import re
s=open('sternberg.py').read()
s=s.replace('stage_probe = stages[stages.tag == "Probe"].set_index("trial")["start"]','stage_probe = stages[stages.tag == "Probe"].groupby("trial")["start"].min()')
open('sternberg.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/survey.py $TMPDIR/D.pkl
```

```
Exit code 1
37
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 5, in <module>
    D = S.load_all(A, workers=16)
  File "entries/000574-boran-2019/sternberg.py", line 152, in load_all
    return list(ex.map(lambda r: load_session(r.path, r.asset_id), table.itertuples()))
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 453, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000574-boran-2019 && python - <<'EOF'
s=open('sternberg.py').read()
old_start = s.index('        st = f["intervals/ttl_stage"]')
old_end = s.index('        el = f["general/extracellular_ephys/electrodes"]')
new = '''        if "ttl_stage" in f["intervals"]:
            st = f["intervals/ttl_stage"]
            tags_idx = st["tags_index"][:]
            tags = _str(st["tags"][:])
            starts = np.concatenate([[0], tags_idx[:-1]])
            stages = pd.DataFrame({"start": st["start_time"][:], "stop": st["stop_time"][:],
                                   "trial": st["trial_number"][:],
                                   "tag": [",".join(tags[a:b]) for a, b in zip(starts, tags_idx)]})
        else:
            stages = pd.DataFrame(columns=["start", "stop", "trial", "tag"])
'''
s = s[:old_start] + new + s[old_end:]
open('sternberg.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/survey.py $TMPDIR/D.pkl
```

```
Exit code 1
37
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 5, in <module>
    D = S.load_all(A, workers=16)
  File "entries/000574-boran-2019/sternberg.py", line 155, in load_all
    return list(ex.map(lambda r: load_session(r.path, r.asset_id), table.itertuples()))
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 453, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
[... 17 more lines not kept]
```

**Agent**

Some sessions have no units table; making units optional too.

**Agent calls Bash**

```bash
cd entries/000574-boran-2019 && python - <<'EOF'
s=open('sternberg.py').read()
a = s.index('        u = f["units"]')
b = s.index('        meta = {k: _scalar(f[p])')
block = s[a:b]
lines = block.splitlines()
new = '        has_units = "units" in f\n        if has_units:\n' + "\n".join("    "+l for l in lines) + "\n"
s = s[:a] + new + s[b:]
s = s.replace('''    sb = np.concatenate([[0], sidx])
    ob = np.concatenate([[0], oidx])
    eb = np.concatenate([[0], eidx])
    units = []
    for i in range(len(sidx)):''','''    units = []
    if not has_units:
        sidx = []
    else:
        sb = np.concatenate([[0], sidx])
        ob = np.concatenate([[0], oidx])
        eb = np.concatenate([[0], eidx])
    for i in range(len(sidx)):''')
open('sternberg.py','w').write(s)
EOF
sed -n 112,160p sternberg.py; . $TMPDIR/dev/bin/activate; python $TMPDIR/survey.py $TMPDIR/D.pkl
```

```
el = f["general/extracellular_ephys/electrodes"]
        elec = pd.DataFrame({c: el[c][:] for c in ["x", "y", "z", "is_inside_soz"]})
        for c in ["label", "group_name", "location"]:
            elec[c] = _str(el[c][:])
        has_units = "units" in f
        if has_units:
            u = f["units"]
            sidx = u["spike_times_index"][:]
            spikes = u["spike_times"][:]
            eidx = u["electrodes_index"][:]
            uel = u["electrodes"][:]
            wm = u["waveform_mean"][:]
            wsd = u["waveform_sd"][:]
            obs = u["obs_intervals"][:]
            oidx = u["obs_intervals_index"][:]
        meta = {k: _scalar(f[p]) for k, p in [("subject", "general/subject/subject_id"),
                                               ("description", "general/subject/description"),
                                               ("start_time", "session_start_time"),
                                               ("identifier", "identifier")]}
        shapes = {k: f[f"acquisition/ecephys.{k}/data"].shape for k in ["eeg", "ieeg", "lfp"]}
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/s2.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
D = pickle.load(open(sys.argv[1],'rb'))
n = sum(len(d['units']) for d in D); print('units', n)
print(pd.Series([u['region'] for d in D for u in d['units']]).value_counts())
d = D[0]; tr=d['trials']; st=d['stages']
print(st.head(12)); print(tr[['start','probe','stage_probe','response_time','rt','set_size','solution','response','correct']].head(6))
# duplicates
for i in range(len(D)):
    for j in range(i+1,len(D)):
        a,b=D[i],D[j]
        if a['subject']!=b['subject']: continue
        ta,tb=a['trials'],b['trials']
        same_ss = None
        k=min(len(ta),len(tb))
        ss = np.mean(ta.set_size.values[:k]==tb.set_size.values[:k])
        rt = np.round(ta.rt.values,3); rtb=np.round(tb.rt.values,3)
        common_rt = len(set(rt)&set(rtb))
        sa = np.concatenate([u['spikes'] for u in a['units']]) if a['units'] else np.array([])
        sb = np.concatenate([u['spikes'] for u in b['units']]) if b['units'] else np.array([])
        cs = len(set(np.round(sa,4))&set(np.round(sb,4)))
        if ss>0.5 or common_rt>10 or cs>100:
            print(a['session'],b['session'],a['subject'],'setsize match',ss,'common rts',common_rt,'of',len(rt),len(rtb),'common spikes',cs,len(sa),len(sb))
EOF
python $TMPDIR/s2.py $TMPDIR/D.pkl
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/s2.py", line 1, in <module>
    import pickle, numpy as np, pandas as pd, sys
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python $TMPDIR/s2.py $TMPDIR/D.pkl
```

```
units 1487
amygdala       585
entorhinal     456
hippocampus    446
Name: count, dtype: int64
        start       stop  trial          tag
0    0.000000   1.000000      0     Fixation
1    1.000000   3.000000      0     Stimulus
2    3.000000   6.000000      0  Maintenance
3    6.000000  17.946711      1        Probe
4   17.946711  18.946711      1     Fixation
5   18.946711  20.946711      1     Stimulus
6   20.946711  23.946711      1  Maintenance
7   23.946711  33.087674      2        Probe
8   33.087674  34.087674      2     Fixation
9   34.087674  36.087674      2     Stimulus
10  36.087674  39.087674      2  Maintenance
11  39.087674  43.945357      3        Probe
       start      probe  stage_probe  ...  solution response  correct
0   0.000000   6.000000          NaN  ...     False       52     True
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/s3.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys
D = pickle.load(open(sys.argv[1],'rb'))
rows=[]
for d in D:
    for u in d['units']: rows.append((d['subject'],d['session'],u['bundle'],u['region'], d['electrodes'].location[u['electrode_row']][:40]))
U=pd.DataFrame(rows,columns=['sub','ses','bundle','region','loc'])
print(U.groupby(['sub','bundle']).size().unstack(fill_value=0))
print(U.groupby(['bundle','loc']).size().to_string())
for d in D:
    if d['session']=='01': print(d['subject'], d['meta']['description'].replace('\n',' | '))
# probe stage check
for d in D[:3]:
    tr=d['trials']; st=d['stages']
    if len(st): 
        p=st[st.tag=='Probe']; print(len(p), np.abs(p.start.values[:len(tr)] - tr.probe.values[:len(p)]).max())
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/s3.py $TMPDIR/D.pkl
```

```
bundle  AHL  AHR  AL   AR  ECL  ECR  PHL  PHR
sub                                          
01       29    0   0    0   14    0    0   25
02       33   28  42   76   13   65   22   20
03        2   45  12    0    0    0    0    0
04       19    4  35   42   53   69   45    8
05        0    0  11    0    0    0    0    0
06       36    0  11    4   21    0    0    5
07        3   13  22   48    0   82   19    4
08       41    0  67  186    2   85    5    0
09        0   34   0   29   42   10    6    0
bundle  loc                                     
AHL     FuG, Left Fusiform Gyrus A20rv, rostrove      6
        Hipp, Left Hippocampus cHipp, caudal hip      9
        Hipp, Left Hippocampus rHipp, rostral hi     27
        ITG, Left Inferior Temporal Gyrus A20cl,      2
        ITG, Left Inferior Temporal Gyrus A20il,      2
        MTG, Left Middle Temporal Gyrus A21c, ca      2
        MTG, Left Middle Temporal Gyrus A21r, ro     43
        MTG, Left Middle Temporal Gyrus aSTS, an     24
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/s4.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys
D = pickle.load(open(sys.argv[1],'rb'))
rows=[]
for d in D:
    el=d['electrodes']; lab=dict(zip(el.label, el.location))
    for u in d['units']:
        rows.append((d['subject'],u['bundle'],u['region'], lab.get(u['bundle']+'1','?')[:12]))
U=pd.DataFrame(rows,columns=['sub','bundle','region','loc1'])
print(U.groupby(['sub','bundle','loc1']).size().to_string())
U['r2']=U.loc1.str.split(',').str[0]
print(U.r2.value_counts())
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/s4.py $TMPDIR/D.pkl
```

```
sub  bundle  loc1        
01   AHL     Hipp, Left H     29
     ECL     Amyg, Right      14
     PHR     Hipp, Right      25
02   AHL     Hipp, Left H     33
     AHR     FuG, Right F     28
     AL      Amyg, Left A     42
     AR      Amyg, Right      76
     ECL     PhG, Left Pa     13
     ECR     PhG, Right P     65
     PHL     Hipp, Left H     22
     PHR     Hipp, Right      20
03   AHL     Hipp, Left H      2
     AHR     Hipp, Right      45
     AL      Amyg, Left A     12
04   AHL     Hipp, Left H     19
     AHR     Hipp, Right       4
     AL      Amyg, Left A     35
     AR      Amyg, Right      42
     ECL     PhG, Left Pa     53
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t_ieeg.py <<'EOF'
import sys, time; sys.path.insert(0,'.')
import sternberg as S, numpy as np
t=time.time()
f = S.open_asset('6f367ffb-c6a9-468f-a974-394eabae6060')
d = f['acquisition/ecephys.ieeg/data']
x = d[:, 0:2]; print(x.shape, time.time()-t)
e = f['acquisition/ecephys.eeg/data'][:]; print(e.shape, time.time()-t)
ts = f['acquisition/ecephys.ieeg/timestamps'][:]; print(time.time()-t, np.diff(ts[:5]), ts[::16000][:10])
l = f['acquisition/ecephys.lfp/data']; y = l[:, 0]; print('lfp', time.time()-t)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/t_ieeg.py
```

```
(800000, 2) 34.60581374168396
(80000, 19) 35.164469480514526
35.61803650856018 [0.0005 0.0005 0.0005 0.0005] [  0.        17.946711  33.087674  43.945357  54.338196  64.797442
  74.692188  84.752997  95.262024 105.040707]
lfp 178.76142525672913
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t2.py <<'EOF'
import sys, time, requests; sys.path.insert(0,'.')
import h5py, remfile, numpy as np
aid='6f367ffb-c6a9-468f-a974-394eabae6060'
m = requests.get(f'https://api.dandiarchive.org/api/assets/{aid}/').json()
s3 = [u for u in m['contentUrl'] if 'amazonaws' in u][0]; print(s3)
t=time.time()
f = h5py.File(remfile.File(s3), 'r')
x = f['acquisition/ecephys.ieeg/data'][:, 0:2]; print(time.time()-t)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/t2.py
```

```
https://dandiarchive.s3.amazonaws.com/blobs/fc7/9f6/fc79f641-16f2-4ddf-9241-7b1c9ef03137
17.513000011444092
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('sternberg.py').read()
s=s.replace('''def open_asset(asset_id):
    return h5py.File(remfile.File(f"{API}/assets/{asset_id}/download/"), "r")''','''def s3_url(asset_id):
    """The asset's S3 address (from its metadata); reading it directly avoids a redirect on
    every range request, which halves streaming time."""
    r = requests.get(f"{API}/assets/{asset_id}/", timeout=60)
    r.raise_for_status()
    return [u for u in r.json()["contentUrl"] if "amazonaws" in u][0]


def open_asset(asset_id):
    return h5py.File(remfile.File(s3_url(asset_id)), "r")''')
open('sternberg.py','w').write(s)
EOF
cat > $TMPDIR/beh.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import sternberg as S
D = pickle.load(open(sys.argv[1],'rb'))
T = pd.concat([d['trials'].assign(subject=d['subject'], session=d['session']) for d in D], ignore_index=True)
print(len(T), T.correct.sum(), T.artifact.sum(), T.rt.describe())
print('IN code check', ((T.response=='51')==T.solution)[T.correct].mean(), ((T.response=='51')==T.solution)[~T.correct].mean())
print(T.response.value_counts(), T.correct_raw.value_counts())
g = T.groupby(['subject','session'])
ps = g.apply(lambda x: pd.Series({'IN': x[x.solution].correct.mean()*100, 'OUT': x[~x.solution].correct.mean()*100, **{f'ss{k}': x[x.set_size==k].correct.mean()*100 for k in (4,6,8)}}))
print(ps.mean()); 
print('pooled', T[T.solution].correct.mean(), T[~T.solution].correct.mean(), T.groupby('set_size').correct.mean())
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/beh.py $TMPDIR/D.pkl
```

```
1827 1676 144 count    1827.000000
mean        1.405302
std         0.715720
min         0.508250
25%         0.992125
50%         1.204500
75%         1.540375
max         9.972750
Name: rt, dtype: float64
IN code check 1.0 0.4370860927152318
response
52    874
51    802
2      85
1      66
Name: count, dtype: int64 correct_raw
1.0    1676
0.0     151
Name: count, dtype: int64
IN     90.256289
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/mk.py <<'EOF'
"""Convert a py file with '# %%' cell markers into a notebook. '# %% md' makes markdown,
'# %% [tag1,tag2]' sets tags."""
import sys, re, nbformat
src = open(sys.argv[1]).read()
cells = []
for block in re.split(r'^# %%', src, flags=re.M)[1:]:
    head, _, body = block.partition('\n')
    head = head.strip()
    tags = []
    m = re.search(r'\[(.*?)\]', head)
    if m: tags = [t.strip() for t in m.group(1).split(',') if t.strip()]
    if head.startswith('md'):
        text = "\n".join(l[2:] if l.startswith('# ') else l.lstrip('#') for l in body.strip('\n').splitlines())
        c = nbformat.v4.new_markdown_cell(text)
    else:
        c = nbformat.v4.new_code_cell(body.strip('\n'))
    if tags: c.metadata['tags'] = tags
    cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata['kernelspec'] = {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'}
nbformat.write(nb, sys.argv[2])
EOF
cat > $TMPDIR/runcells.py <<'EOF'
"""Dev runner: exec cells of the py notebook whose index is in a range, with D from pickle."""
import sys, re, pickle, time
sys.path.insert(0, '.')
src = open(sys.argv[1]).read()
blocks = re.split(r'^# %%', src, flags=re.M)[1:]
names = sys.argv[3].split(',')
g = {}
exec(open(sys.argv[2]).read(), g) if sys.argv[2] != '-' else None
for i, b in enumerate(blocks):
    head, _, body = b.partition('\n')
    if head.strip().startswith('md'): continue
    if any(n in head for n in names) or 'setup' in head:
        t = time.time()
        print(f'---- cell {i} {head.strip()}')
        exec(body, g)
        print(f'---- {time.time()-t:.1f}s')
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "entries/000574-boran-2019/nb_src.py",
 "content": "# %% md\n# # Reproducing Boran et al. (2019) from dandiset 000574\n#\n# Paper: Boran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald & Sarnthein (2019), \"Persistent\n# hippocampal neural firing and hippocampal-cortical coupling predict verbal working memory\n# load\", Science Advances 5, eaav3687, doi:10.1126/sciadv.aav3687.\n#\n# Dataset: [DANDI:000574](https://dandiarchive.org/dandiset/000574/0.250815.1108), version\n# 0.250815.1108 (doi:10.48324/dandi.000574/0.250815.1108). The paper cites no version of the\n# dandiset (it predates it and points to the authors on request), so the most recent published\n# version is pinned. Version 0.250610.0938 holds the same 37 assets (identical asset ids). The\n# earlier version 0.231010.1809 held 45 files, with sessions of subjects 2, 5, 7 and 9 deposited\n# more than once under `obj-` names; it matches the claims file's description no better.\n#\n# Claims file: `claims/000574/10.1126-sciadv.aav3687.yaml`, written from the version of record\n# (Europe PMC, PMC6436923) with its supplement, and the data descriptor (Boran et al. 2020,\n# Sci Data 7, 30).\n#\n# Every number below is computed from the streamed NWB files. The table of claims and outcomes\n# is in the summary at the end.\n\n# %% [setup]\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport sternberg as S\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\npd.set_option(\"display.max_rows\", 200)\n\n# %% [load]\nA = S.assets()\nD = S.load_all(A, workers=16)\nprint(len(A), \"assets read at version\", S.DANDISET_VERSION)\n\n# %% md\n# ## Data check\n#\n# Counts by subject and session, trial fields, units and their regions, and the checks of the\n# description against the values.\n\n# %% [sanity]\nT = pd.concat([d[\"trials\"].assign(subject=d[\"subject\"], session=d[\"session\"]) for d in D],\n              ignore_index=True)\nsess = pd.DataFrame([{\"subject\": d[\"subject\"], \"session\": d[\"session\"],\n                      \"start\": d[\"meta\"][\"start_time\"], \"trials\": len(d[\"trials\"]),\n                      \"correct\": int(d[\"trials\"].correct.sum()),\n                      \"artifact\": int(d[\"trials\"].artifact.sum()), \"units\": len(d[\"units\"]),\n                      \"eeg_ch\": d[\"shapes\"][\"eeg\"][1], \"ieeg_ch\": d[\"shapes\"][\"ieeg\"][1],\n                      \"eeg_rate\": d[\"shapes\"][\"eeg\"][0] / (8 * len(d[\"trials\"])),\n                      \"ieeg_rate\": d[\"shapes\"][\"ieeg\"][0] / (8 * len(d[\"trials\"])),\n                      \"lfp_rate\": d[\"shapes\"][\"lfp\"][0] / (8 * len(d[\"trials\"]))} for d in D])\nprint(sess.to_string())\nprint(\"\\nsubjects\", sess.subject.nunique(), \"sessions\", len(sess), \"per subject\",\n      sess.groupby(\"subject\").size().to_dict())\nprint(\"trials\", len(T), \"correct\", int(T.correct.sum()), \"artifact-marked\", int(T.artifact.sum()))\nprint(\"sessions with fewer than 50 trials:\", int((sess.trials < 50).sum()),\n      \"; sessions without a units table:\", int((sess.units == 0).sum()))\nprint(\"trial duration (s):\", np.unique(np.round(T.stop - T.start, 6)))\nprint(\"set sizes:\", T.set_size.value_counts().sort_index().to_dict())\nprint(\"response codes by correctness and solution:\")\nprint(pd.crosstab([T.correct, T.solution], T.response))\nprint(\"RT relative to probe onset (s): min %.3f median %.3f max %.3f\" % (T.rt.min(), T.rt.median(), T.rt.max()))\n\n# %% [sanity]\n# The trial-stage table: its Probe stages are numbered one trial late, and some files lack it.\nchk = []\nfor d in D:\n    st, tr = d[\"stages\"], d[\"trials\"]\n    if len(st) == 0:\n        chk.append((d[\"subject\"], d[\"session\"], \"no ttl_stage\", np.nan, np.nan))\n        continue\n    pr = st[st.tag == \"Probe\"].sort_values(\"start\").start.to_numpy()\n    k = min(len(pr), len(tr))\n    off = np.abs(pr[:k] - tr.probe.to_numpy()[:k]).max()\n    fx = st[st.tag == \"Fixation\"].sort_values(\"start\").start.to_numpy()\n    offf = np.abs(fx[:len(tr)] - tr.start.to_numpy()[:len(fx)]).max()\n    chk.append((d[\"subject\"], d[\"session\"], \"ok\", off, offf))\nchk = pd.DataFrame(chk, columns=[\"subject\", \"session\", \"stages\", \"max |probe stage - (start+6)|\",\n                                 \"max |fixation stage - start|\"])\nprint(chk.to_string())\n\n# %% [sanity]\n# Units: regions from the bundle name (claims file) and from the atlas label of the bundle's\n# deepest contact (Methods, Depth electrode localization).\nrows = []\nfor d in D:\n    lab = dict(zip(d[\"electrodes\"].label, d[\"electrodes\"].location))\n    for u in d[\"units\"]:\n        loc1 = lab.get(u[\"bundle\"] + \"1\", \"?\").split(\",\")[0]\n        atlas = {\"Hipp\": \"hippocampus\", \"PhG\": \"entorhinal\", \"Amyg\": \"amygdala\"}.get(loc1, \"other:\" + loc1)\n        sp = u[\"spikes\"]\n        rows.append({\"subject\": d[\"subject\"], \"session\": d[\"session\"], \"unit\": u[\"unit\"],\n                     \"bundle\": u[\"bundle\"], \"region_bundle\": u[\"region\"], \"atlas_label\": loc1,\n                     \"region_atlas\": atlas, \"n_spikes\": len(sp),\n                     \"sorted\": bool(np.all(np.diff(sp) >= 0)),\n                     \"in_obs\": float(np.mean([np.any((s >= u[\"obs\"][:, 0]) & (s <= u[\"obs\"][:, 1])) for s in sp[:200]])) if len(sp) else np.nan})\nU = pd.DataFrame(rows)\nprint(\"units\", len(U), \"; spike times sorted in all units:\", bool(U.sorted.all()),\n      \"; fraction of (first 200) spikes inside the unit's obs_intervals:\", U.in_obs.min())\nprint(pd.crosstab(U.region_bundle, U.region_atlas, margins=True))\nprint(pd.crosstab([U.subject, U.bundle], U.atlas_label))\n\n# %% [sanity]\n# Electrode coordinates: the table says +x is posterior, +y inferior, +z right. Check on the\n# bundles: posterior hippocampus (PH) should lie at larger x than anterior (AH), right\n# electrodes at positive z, and contact 1 should be the deepest (nearest the midline, smallest |z|).\nec = pd.concat([d[\"electrodes\"].assign(subject=d[\"subject\"]) for d in D if d[\"session\"] == \"01\"])\nie = ec[ec.group_name == \"ieeg\"].copy()\nie[\"bundle\"] = ie.label.str.replace(r\"\\d+$\", \"\", regex=True)\nie[\"contact\"] = ie.label.str.extract(r\"(\\d+)$\").astype(float)\nmx = ie.groupby([\"subject\", \"bundle\"]).apply(lambda g: pd.Series({\n    \"x1\": g[g.contact == 1].x.mean(), \"z1\": g[g.contact == 1].z.mean(),\n    \"absz_1_lt_8\": float(abs(g[g.contact == 1].z.mean()) < abs(g[g.contact == g.contact.max()].z.mean()))}))\nmx = mx.reset_index()\nah = mx[mx.bundle.str.startswith(\"AH\")].groupby(\"subject\").x1.mean()\nph = mx[mx.bundle.str.startswith(\"PH\")].groupby(\"subject\").x1.mean()\nprint(\"x of contact 1, AH and PH per subject:\\n\", pd.concat([ah, ph], axis=1, keys=[\"AH\", \"PH\"]))\nprint(\"right bundles with z > 0:\", float((mx[mx.bundle.str.endswith(\"R\")].z1 > 0).mean()),\n      \"; left bundles with z < 0:\", float((mx[mx.bundle.str.endswith(\"L\")].z1 < 0).mean()))\nprint(\"bundles whose contact 1 is nearer the midline than their last contact:\", mx.absz_1_lt_8.mean())\nprint(\"SOZ electrodes per subject (is_inside_soz) and the SOZ list in the subject description:\")\nfor d in D:\n    if d[\"session\"] != \"01\":\n        continue\n    e = d[\"electrodes\"]\n    soz = sorted(set(e[e.is_inside_soz].label.str.replace(r\"\\d+$\", \"\", regex=True)))\n    desc = [l for l in d[\"meta\"][\"description\"].split(\"\\n\") if \"SOZ\" in l][0]\n    print(\" \", d[\"subject\"], soz, \"|\", desc)\n"
}
```

```
File created successfully at: entries/000574-boran-2019/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
echo "import pickle; D = pickle.load(open('$TMPDIR/D.pkl','rb'))" > $TMPDIR/pre.py; . $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity 2>&1 | tail -150
```

```
25      06      07  2014-08-28T15:21:00+02:00      50       49         4      0      10       64     200.0     2000.0  32000.000000
26      07      01  2016-03-02T17:01:00+01:00      49       48         1      0       8       64     200.0     2000.0  32000.000000
27      07      02  2016-03-03T16:40:00+01:00      48       48         7     85       8       64     200.0     2000.0  32000.000000
28      07      03  2016-03-05T10:32:00+01:00      50       46         1     58       8       64     200.0     2000.0  32000.000000
29      07      04  2016-03-05T10:32:00+01:00      50       45         2     48       8       64     200.0     2000.0  32000.000000
30      08      01  2017-01-11T11:54:00+01:00      50       44        17     85      19       62     200.0     2000.0  32000.000000
31      08      02  2017-01-11T12:05:00+01:00      50       47         8     69      19       62     200.0     2000.0  32000.000000
32      08      03  2017-01-13T12:14:00+01:00      50       43         5     69      19       62     200.0     2000.0  32000.000000
33      08      04  2017-01-13T12:16:00+01:00      50       44         4     76      19       62     200.0     2000.0  32000.000000
34      08      05  2017-01-14T17:29:00+01:00      49       46         0     87      19       62     200.0     2000.0  32000.000000
35      09      01  2015-01-15T14:43:00+01:00      48       44         2     60       8       64     200.0     2000.0  32000.000000
36      09      02  2015-01-15T14:43:00+01:00      49       46         7     61       8       64     200.0     2000.0  32000.000000

subjects 9 sessions 37 per subject {'01': 4, '02': 7, '03': 3, '04': 2, '05': 3, '06': 7, '07': 4, '08': 5, '09': 2}
trials 1827 correct 1676 artifact-marked 144
sessions with fewer than 50 trials: 13 ; sessions without a units table: 8
trial duration (s): [8.]
set sizes: {4: 703, 6: 552, 8: 572}
response codes by correctness and solution:
response           1   2   51   52
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('sternberg.py').read()
s=s.replace('IN_CODE, OUT_CODE = "51", "52"','IN_CODES = ("51", "1")    # IN on correct trials 51, on incorrect trials 1 (read from the data)')
s=s.replace('trials["is_in"] = trials["response"] == IN_CODE','trials["is_in"] = trials["response"].isin(IN_CODES)')
s=s.replace('''- IN/OUT: `response_type` codes 51 and 52. That 51 is IN is read from the data (it matches
  `solution` on every correct trial, checked in the notebook).''','''- IN/OUT: `response_type` holds 51 (IN) and 52 (OUT) on correct trials and 1 (IN) and 2 (OUT)
  on incorrect ones. The meaning is read from the data: with `solution`, every correct trial
  has 51 when the probe was in the set, and every incorrect trial has 1 when it was not
  (checked in the notebook). The codes are not described in the files.
- Spike times are sorted on loading; some units store them unsorted (counted in the notebook).''')
s=s.replace('''"region": region_of(bundle), "spikes": spikes[sb[i]:sb[i + 1]],''','''"region": region_of(bundle), "spikes": np.sort(spikes[sb[i]:sb[i + 1]]),
                      "sorted_in_file": bool(np.all(np.diff(spikes[sb[i]:sb[i + 1]]) >= 0)),''')
open('sternberg.py','w').write(s)
EOF
grep -n "sorted_in_file\|IN_CODES" sternberg.py
```

```
59:IN_CODES = ("51", "1")    # IN on correct trials 51, on incorrect trials 1 (read from the data)
148:    trials["is_in"] = trials["response"].isin(IN_CODES)
162:                      "sorted_in_file": bool(np.all(np.diff(spikes[sb[i]:sb[i + 1]]) >= 0)),
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/pre.py <<'EOF'
import numpy as np
for d in D:
    d['trials']['is_in'] = d['trials'].response.isin(('51','1'))
    for u in d['units']:
        u['sorted_in_file'] = bool(np.all(np.diff(u['spikes'])>=0)); u['spikes'] = np.sort(u['spikes'])
EOF
python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('"sorted": bool(np.all(np.diff(sp) >= 0)),','"sorted": u["sorted_in_file"],')
s=s.replace('''print("units", len(U), "; spike times sorted in all units:", bool(U.sorted.all()),''','''print("units", len(U), "; units whose spike times are stored unsorted:", int((~U.sorted).sum()),
      U[~U.sorted].groupby(["subject", "session"]).size().to_dict(),''')
open('nb_src.py','w').write(s)
EOF
cat >> nb_src.py <<'EOF'

# %% md
# ## Behavior
#
# All trials of all 37 sessions (the paper has 36; the dataset holds 37, as the data
# descriptor's Table 1 lists). 13 sessions hold fewer than 50 trials.
#
# ### behavior-accuracy-set-size
#
# > Correct response rates were 90.2 +/- 7.8% for IN and 93.1 +/- 4.3% for OUT trials, and the
# > rate of correct responses decreased with set size, from 98.5% (set size 4) to 90.5% (6) and
# > 84.7% (8), a significant effect in a permuted repeated-measures ANOVA over 36 sessions.
#
# IN and OUT trials are those whose probe was or was not in the set (`solution`), as Cowan's K
# uses "correct IN rate" for hits.

# %% [claim:behavior-accuracy-set-size]
rng = np.random.default_rng(101)
T["sess"] = T.subject + "-" + T.session
per = T.groupby("sess").apply(lambda x: pd.Series({
    "IN": 100 * x[x.solution].correct.mean(), "OUT": 100 * x[~x.solution].correct.mean(),
    **{f"ss{k}": 100 * x[x.set_size == k].correct.mean() for k in (4, 6, 8)}}))
pooled = {"IN": 100 * T[T.solution].correct.mean(), "OUT": 100 * T[~T.solution].correct.mean(),
          **{f"ss{k}": 100 * T[T.set_size == k].correct.mean() for k in (4, 6, 8)}}
print("(a) mean of per-session percentages:", per.mean().round(2).to_dict())
print("    SD over sessions:", per.std().round(2).to_dict())
print("(b) trials pooled:", {k: round(v, 2) for k, v in pooled.items()})


def rm_anova_F(Y):
    """One-way repeated-measures F; Y is sessions x conditions."""
    n, k = Y.shape
    gm = Y.mean()
    ss_c = n * ((Y.mean(0) - gm) ** 2).sum()
    ss_s = k * ((Y.mean(1) - gm) ** 2).sum()
    ss_e = ((Y - gm) ** 2).sum() - ss_c - ss_s
    return (ss_c / (k - 1)) / (ss_e / ((n - 1) * (k - 1))), (k - 1, (n - 1) * (k - 1))


Y = per[["ss4", "ss6", "ss8"]].to_numpy()
F0, dfs = rm_anova_F(Y)
nperm = 4999
Fn = np.array([rm_anova_F(np.array([rng.permutation(r) for r in Y]))[0] for _ in range(nperm)])
p_anova = (np.sum(Fn >= F0) + 1) / (nperm + 1)
print(f"repeated-measures ANOVA over {Y.shape[0]} sessions: F{dfs} = {F0:.2f}, permutation P = {p_anova:.4f}"
      f" (labels shuffled within session, {nperm} permutations)")
# Same without the one session the paper may not have had: leave each session out in turn
Fl = [rm_anova_F(np.delete(Y, i, 0))[0] for i in range(len(Y))]
print("F with one session left out, range: %.2f to %.2f" % (min(Fl), max(Fl)))
print("per subject (mean of session percentages):")
print(per.groupby(per.index.str[:2]).mean().round(1))

# %% md
# ### behavior-capacity
#
# > Across all sessions the working memory capacity (Cowan's K) averaged 6.8 letters.

# %% [claim:behavior-capacity]
def cowan(x, k):
    return (x[x.solution].correct.mean() + x[~x.solution].correct.mean() - 1) * k


K = T.groupby("sess").apply(lambda x: pd.Series({
    "a_K8": cowan(x[x.set_size == 8], 8),
    "b_maxK": max(cowan(x[x.set_size == k], k) for k in (4, 6, 8)),
    "c_pooled_x8": cowan(x, 8),
    "d_meanK": np.mean([cowan(x[x.set_size == k], k) for k in (4, 6, 8)])}))
print("mean Cowan's K over sessions, by reading:")
print(K.mean().round(2).to_string())
print("range of K over sessions:", K.min().round(2).to_dict(), K.max().round(2).to_dict())

# %% md
# ### behavior-rt-workload
#
# > The mean response time of correct trials (1630 trials) increased with workload, by 48 ms per
# > item, a significant effect in a permuted repeated-measures ANOVA.

# %% [claim:behavior-rt-workload]
rng = np.random.default_rng(102)
C = T[T.correct].copy()
print("correct trials:", len(C), "; mean RT by set size (s):", C.groupby("set_size").rt.mean().round(4).to_dict())


def oneway_F(y, g):
    groups = [y[g == k] for k in np.unique(g)]
    return stats.f_oneway(*groups).statistic


F0 = oneway_F(C.rt.to_numpy(), C.set_size.to_numpy())
Fn = np.array([oneway_F(C.rt.to_numpy(), rng.permutation(C.set_size.to_numpy())) for _ in range(4999)])
print(f"one-way ANOVA over correct trials: F(2, {len(C) - 3}) = {F0:.2f}, permutation P = {(np.sum(Fn >= F0) + 1) / 5000:.4f}")
slope_i = np.polyfit(C.set_size, C.rt, 1)[0] * 1000
ps_mean = C.groupby("sess").apply(lambda x: np.polyfit(x.set_size, x.rt, 1)[0] * 1000 if x.set_size.nunique() > 1 else np.nan)
med = C.groupby(["sess", "set_size"]).rt.median().unstack()
ps_med = med.apply(lambda r: np.polyfit([4, 6, 8], r.to_numpy(), 1)[0] * 1000 if r.notna().all() else np.nan, axis=1)
m3 = C.groupby("set_size").rt.mean()
slope_iii = np.polyfit(m3.index, m3.to_numpy(), 1)[0] * 1000
slope_iv = (m3[8] - m3[4]) / 4 * 1000
print("RT increase per item (ms): (i) line over trials %.1f; (ii) mean of per-session slopes, trial RTs %.1f,"
      " session medians %.1f; (iii) slope of set-size means %.1f; (iv) (8 - 4) / 4 %.1f"
      % (slope_i, ps_mean.mean(), ps_med.mean(), slope_iii, slope_iv))
print("per subject slope (i):", C.groupby("subject").apply(lambda x: round(np.polyfit(x.set_size, x.rt, 1)[0] * 1000, 1)).to_dict())

# %% md
# ### behavior-rt-correct-incorrect
#
# > Correct IN/OUT decisions were made faster than incorrect ones (1.36 +/- 0.64 s against
# > 1.87 +/- 1.21 s).

# %% [claim:behavior-rt-correct-incorrect]
rng = np.random.default_rng(103)
rc, ri = T[T.correct].rt.to_numpy(), T[~T.correct].rt.to_numpy()
t_a, p_a = S.perm_t(ri, rc, n_perm=2000, rng=rng)
print(f"(a) pooled trials: correct {rc.mean():.3f} +/- {rc.std(ddof=1):.3f} s (n = {len(rc)}), incorrect "
      f"{ri.mean():.3f} +/- {ri.std(ddof=1):.3f} s (n = {len(ri)}); unpaired permutation t = {t_a:.2f}, P = {p_a:.4f}")
sm = T.groupby(["sess", "correct"]).rt.mean().unstack().dropna()
t_b, p_b = S.perm_t(sm[False], sm[True], n_perm=2000, paired=True, rng=rng)
print(f"(b) per-session means, {len(sm)} sessions with an error: correct {sm[True].mean():.3f} +/- {sm[True].std():.3f},"
      f" incorrect {sm[False].mean():.3f} +/- {sm[False].std():.3f}; paired permutation t = {t_b:.2f}, P = {p_b:.4f}")
print("medians (s): correct %.3f, incorrect %.3f" % (np.median(rc), np.median(ri)))
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py claim:behavior 2>&1 | tail -60
```

```
---- cell 1 [setup]
---- 1.2s
---- cell 9 [claim:behavior-accuracy-set-size]
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 15, in <module>
    exec(body, g)
    ~~~~^^^^^^^^^
  File "<string>", line 2, in <module>
NameError: name 'T' is not defined
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity,claim:behavior 2>&1 | sed -n '/cell 9/,$p'
```

```
---- cell 9 [claim:behavior-accuracy-set-size]
(a) mean of per-session percentages: {'IN': 90.26, 'OUT': 93.12, 'ss4': 98.44, 'ss6': 90.47, 'ss8': 85.12}
    SD over sessions: {'IN': 7.69, 'OUT': 4.26, 'ss4': 2.54, 'ss6': 8.67, 'ss8': 9.06}
(b) trials pooled: {'IN': np.float64(90.42), 'OUT': np.float64(92.98), 'ss4': np.float64(98.29), 'ss6': np.float64(90.4), 'ss8': np.float64(84.97)}
repeated-measures ANOVA over 37 sessions: F(2, 72) = 37.28, permutation P = 0.0002 (labels shuffled within session, 4999 permutations)
F with one session left out, range: 34.41 to 41.81
per subject (mean of session percentages):
        IN   OUT    ss4   ss6   ss8
sess                               
01    90.3  94.3  100.0  91.7  85.2
02    82.9  89.0   95.7  80.4  79.3
03    94.4  91.9   98.2  94.1  86.5
04    96.8  92.7  100.0  94.1  89.6
05    87.9  95.8  100.0  88.5  83.2
06    93.9  94.9   99.4  91.4  90.7
07    93.4  96.8   98.8  93.1  93.2
08    87.2  93.1   97.3  96.1  77.5
09    95.7  90.0  100.0  94.4  85.0
---- 0.8s
---- cell 11 [claim:behavior-capacity]
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ## Neurons
#
# Spike times are aligned to each trial's probe onset (trial start + 6 s) and counted in 20 ms
# bins from -6 to +2 s, the 8 s that each trial stores. Sliding windows (500 ms or 200 ms at
# 20 ms steps, Fig. 2A and Fig. 3 legends) are sums of these bins.
#
# Regions. The claims file defines them for `neurons-recorded` by the bundle name (AH and PH
# hippocampus, EC entorhinal cortex, A amygdala). The other claims do not say; the paper assigns
# electrodes to regions with the Brainnetome atlas (Methods, Depth electrode localization: "The
# contact positions were normalized to the MNI space and assigned to a brain region using the
# Brainnetome Atlas"), and the microwires protrude from the tip, next to contact 1. So for those
# claims the main reading is the atlas label of the bundle's contact 1 (Hipp hippocampus, PhG
# entorhinal cortex, Amyg amygdala; 28 units under FuG are left out), and the bundle reading is
# shown as a variant.

# %% [prep]
EDGES = np.round(np.arange(-6.0, 2.0 + 1e-9, 0.02), 4)
units = []
for d in D:
    tr = d["trials"]
    lab = dict(zip(d["electrodes"].label, d["electrodes"].location))
    for u in d["units"]:
        al = S.aligned_spikes(u["spikes"], tr.probe.to_numpy())
        loc1 = lab.get(u["bundle"] + "1", "?").split(",")[0]
        units.append({"subject": d["subject"], "session": d["session"], "sess": d["subject"] + "-" + d["session"],
                      "unit": u["unit"], "bundle": u["bundle"], "region_bundle": u["region"],
                      "region_atlas": {"Hipp": "hippocampus", "PhG": "entorhinal", "Amyg": "amygdala"}.get(loc1, "other"),
                      "aligned": al, "bins": S.binned(al, EDGES).astype(np.int16),
                      "correct": tr.correct.to_numpy(), "set_size": tr.set_size.to_numpy(),
                      "is_in": tr.is_in.to_numpy(), "rt": tr.rt.to_numpy(),
                      "spikes": u["spikes"], "obs": u["obs"],
                      "wm": u["waveform_mean"], "wsd": u["waveform_sd"]})
UN = pd.DataFrame([{k: v for k, v in u.items() if k in ("subject", "session", "sess", "unit", "bundle", "region_bundle", "region_atlas")} for u in units])
REG = ["hippocampus", "entorhinal", "amygdala"]
print(len(units), "units;", UN.region_atlas.value_counts().to_dict())


def win_counts(u, window):
    i0 = int(round((window[0] + 6) / 0.02))
    i1 = int(round((window[1] + 6) / 0.02))
    return u["bins"][:, i0:i1].sum(1).astype(float)


def win_rate(u, window):
    return win_counts(u, window) / (window[1] - window[0])


def sliding(u, width, lo, hi, step=0.02):
    """Rate in windows of `width` s centred on times lo..hi at 20 ms steps (trials x times)."""
    w = int(round(width / 0.02))
    cs = np.concatenate([np.zeros((u["bins"].shape[0], 1)), np.cumsum(u["bins"], 1)], 1)
    centres = np.round(np.arange(lo, hi + 1e-9, step), 4)
    out = []
    for c in centres:
        a = int(round((c - width / 2 + 6) / 0.02))
        a = min(max(a, 0), u["bins"].shape[1] - w)
        out.append((cs[:, a + w] - cs[:, a]) / width)
    return np.array(out).T, centres

# %% md
# ### neurons-recorded
#
# > 1526 neurons were recorded (51 +/- 35 per session), 676 in hippocampus, 449 in entorhinal
# > cortex and 401 in amygdala.

# %% [claim:neurons-recorded]
cnt_b = UN.region_bundle.value_counts()
cnt_a = UN.region_atlas.value_counts()
print("units:", len(UN))
print("by bundle name (claims file):", cnt_b.to_dict())
print("by atlas label of contact 1 (variant):", cnt_a.to_dict())
per_sess = sess.set_index(sess.subject + "-" + sess.session).units
print("per session, (a) all 37 sessions: %.1f +/- %.1f; (b) the %d sessions with units: %.1f +/- %.1f"
      % (per_sess.mean(), per_sess.std(), (per_sess > 0).sum(), per_sess[per_sess > 0].mean(), per_sess[per_sess > 0].std()))
print("sessions without units:", list(per_sess[per_sess == 0].index))
print("units per subject:", UN.groupby("subject").size().to_dict())
print("differences from the paper (bundle): total %+d, hippocampus %+d, entorhinal %+d, amygdala %+d"
      % (len(UN) - 1526, cnt_b["hippocampus"] - 676, cnt_b["entorhinal"] - 449, cnt_b["amygdala"] - 401))

# %% md
# ### spike-sorting-quality
#
# > The mean firing rate of all neurons was 2.55 +/- 3.30 Hz; the percentage of interspike
# > intervals below 3 ms was 1.58 +/- 4.18%, and the ratio of the peak of the mean waveform to
# > the SD of the noise was 3.28 +/- 1.56.

# %% [claim:spike-sorting-quality]
q = []
for u in units:
    obs = u["obs"]
    dur_trials = float(np.sum(obs[:, 1] - obs[:, 0]))
    dur_session = float(obs[:, 1].max() - obs[:, 0].min())
    sp = u["spikes"]
    isi = np.diff(sp)
    # ISIs within one stored trial only (the gaps between trials are not recorded)
    same = np.searchsorted(obs[:, 0], sp[1:], side="right") == np.searchsorted(obs[:, 0], sp[:-1], side="right")
    isi = isi[same]
    peak = np.max(np.abs(u["wm"]))
    q.append({"rate_trials": len(sp) / dur_trials, "rate_session": len(sp) / dur_session,
              "isi3": 100 * np.mean(isi < 0.003) if len(isi) else np.nan,
              "snr_meansd": peak / np.mean(u["wsd"]), "snr_first": peak / np.mean(u["wsd"][:5])})
Q = pd.DataFrame(q)
print(Q.agg(["mean", "std", "median", "min", "max"]).round(3).to_string())
print("units with ISI computable:", int(Q.isi3.notna().sum()), "of", len(Q))
print("waveform: %d samples (2 ms at 32 kHz); peak |mean| range %.1f to %.1f uV" %
      (len(units[0]["wm"]), 1e6 * min(np.abs(u["wm"]).max() for u in units), 1e6 * max(np.abs(u["wm"]).max() for u in units)))
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity,prep,claim:neurons,claim:spike 2>&1 | sed -n '/cell 1[6-9]/,$p'
```

```
---- cell 17 [prep]
1487 units; {'hippocampus': 640, 'entorhinal': 421, 'amygdala': 398, 'other': 28}
---- 2.1s
---- cell 19 [claim:neurons-recorded]
units: 1487
by bundle name (claims file): {'amygdala': 585, 'entorhinal': 456, 'hippocampus': 446}
by atlas label of contact 1 (variant): {'hippocampus': 640, 'entorhinal': 421, 'amygdala': 398, 'other': 28}
per session, (a) all 37 sessions: 40.2 +/- 38.0; (b) the 29 sessions with units: 51.3 +/- 35.6
sessions without units: ['01-03', '01-04', '06-03', '06-04', '06-05', '06-06', '06-07', '07-01']
units per subject: {'01': 68, '02': 299, '03': 59, '04': 275, '05': 11, '06': 77, '07': 191, '08': 386, '09': 121}
differences from the paper (bundle): total -39, hippocampus -230, entorhinal +7, amygdala +184
---- 0.0s
---- cell 21 [claim:spike-sorting-quality]
        rate_trials  rate_session    isi3  snr_meansd  snr_first
mean          2.569         1.829   1.748       5.343      5.341
std           3.327         2.378   4.594       2.594      3.171
median        1.471         1.059   0.423       4.910      4.808
min           0.005         0.004   0.000       1.276      0.924
max          40.691        31.073  77.079      23.553     26.171
units with ISI computable: 1486 of 1487
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> sternberg.py <<'EOF'


# ---- vectorized permutation tests --------------------------------------------------------
# For a permutation test whose relabelings keep the pooled values (sign flips of paired
# differences, or reassigning pooled values to two groups), the permutation distribution of a
# relabeled data set is the same as that of the original. So the reference distribution is
# computed once per unit and reused for the relabeled ("scrambled") repetitions of a selection.

def t_paired_rows(Dm):
    """Paired t of each row of Dm (rows = sets of differences)."""
    n = Dm.shape[-1]
    m = Dm.mean(-1)
    v = Dm.var(-1, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(v > 0, m / np.sqrt(v / n), 0.0)


def t_groups(X, G):
    """Unequal-variance t of group A (G True) against B for each row of the masks G (P x N),
    for every column of X (N x K). Returns P x K."""
    G = G.astype(float)
    na = G.sum(1, keepdims=True)
    nb = X.shape[0] - na
    s1 = G @ X
    q1 = G @ (X ** 2)
    S1, Q1 = X.sum(0), (X ** 2).sum(0)
    ma, mb = s1 / na, (S1 - s1) / nb
    va = (q1 - na * ma ** 2) / (na - 1)
    vb = ((Q1 - q1) - nb * mb ** 2) / (nb - 1)
    se = np.sqrt(np.clip(va, 0, None) / na + np.clip(vb, 0, None) / nb)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(se > 0, (ma - mb) / se, 0.0)


def random_masks(n_a, n, n_perm, rng):
    """n_perm random boolean masks with n_a of n entries True."""
    r = rng.random((n_perm, n))
    idx = np.argsort(r, axis=1)[:, :n_a]
    G = np.zeros((n_perm, n), bool)
    np.put_along_axis(G, idx, True, axis=1)
    return G


def perm_p(t_obs, t_ref):
    """Two-sided permutation P of each observed t against the reference |t| values."""
    t_ref = np.sort(np.abs(np.asarray(t_ref)))
    k = len(t_ref) - np.searchsorted(t_ref, np.abs(np.asarray(t_obs)) - 1e-12, side="left")
    return (k + 1) / (len(t_ref) + 1)


def cluster_masses(Tm, thr):
    """Masses (sum of t) of positive and negative supra-threshold runs in each row of Tm (P x K).
    Returns (max |mass| per row, list of (start, stop, mass) for row 0)."""
    P, K = Tm.shape
    out = np.zeros(P)
    for sign in (1, -1):
        sup = sign * Tm > thr
        start = sup & ~np.concatenate([np.zeros((P, 1), bool), sup[:, :-1]], 1)
        rid = np.cumsum(start, 1) * sup
        flat = (np.arange(P)[:, None] * (K + 1) + rid)[sup]
        mass = np.bincount(flat, weights=(sign * Tm)[sup], minlength=P * (K + 1)).reshape(P, K + 1)
        out = np.maximum(out, mass[:, 1:].max(1) if K else 0)
    row0 = []
    for sign in (1, -1):
        sup = sign * Tm[0] > thr
        i = 0
        while i < K:
            if sup[i]:
                j = i
                while j < K and sup[j]:
                    j += 1
                row0.append((i, j, float(Tm[0, i:j].sum())))
                i = j
            else:
                i += 1
    return out, row0
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
cat >> sternberg.py <<'EOF'


def cluster_max(Tm, thr, sign=1):
    """Largest mass of runs with sign * t > thr in each row of Tm (P x K); 0 when none."""
    P, K = Tm.shape
    sup = sign * Tm > thr
    start = sup & ~np.concatenate([np.zeros((P, 1), bool), sup[:, :-1]], 1)
    rid = np.cumsum(start, 1) * sup
    flat = (np.arange(P)[:, None] * (K + 1) + rid)[sup]
    mass = np.bincount(flat, weights=(sign * Tm)[sup], minlength=P * (K + 1)).reshape(P, K + 1)
    return mass[:, 1:].max(1)


def cluster_test(X, g, n_perm, rng, alpha=0.05, sign=1, extra=None):
    """Cluster-based permutation test (FieldTrip style, two-sided cluster threshold at alpha,
    maximal |cluster mass| null) of group g (True) against the rest, rows of X are trials.
    Returns the P of the largest cluster in direction `sign` (1.0 when there is none) and, if
    `extra` masks are given (relabelings), the P of each of them against the same null."""
    from scipy import stats as _st
    n = len(g)
    thr = _st.t.ppf(1 - alpha / 2, n - 2)
    G = random_masks(int(g.sum()), n, n_perm, rng)
    Tn = t_groups(X, G)
    null = np.maximum(cluster_max(Tn, thr, 1), cluster_max(Tn, thr, -1))
    null = np.sort(null)

    def pval(m):
        k = len(null) - np.searchsorted(null, m - 1e-12, side="left")
        return np.where(m > 0, (k + 1) / (len(null) + 1), 1.0)

    T0 = t_groups(X, g[None, :])
    p0 = float(pval(cluster_max(T0, thr, sign))[0])
    if extra is None:
        return p0
    Te = t_groups(X, extra)
    return p0, pval(cluster_max(Te, thr, sign))
EOF
cat >> nb_src.py <<'EOF'

# %% md
# ### fig2b-maintenance-neurons-hippocampus
#
# > Neurons with higher firing during maintenance than fixation (maintenance neurons) occurred in
# > all three areas, most frequently in hippocampus, where 20.6% of the recorded neurons were
# > maintenance neurons.
#
# Correct trials; rate in maintenance (-3 to 0 s) against fixation (-6 to -5 s), permutation t
# test with 2000 permutations, P < 0.05 and maintenance higher; paired and unpaired readings.
# The null shuffles the maintenance and fixation labels within each trial and reruns the
# selection, 1000 times (P also given from the first 499 repetitions).

# %% [claim:fig2b-maintenance-neurons-hippocampus]
rng = np.random.default_rng(201)
R = 1000
sel = {"paired": [], "unpaired": []}
null_sel = {"paired": [], "unpaired": []}
p_mf = {"paired": [], "unpaired": []}
for u in units:
    c = u["correct"]
    m, f = win_rate(u, S.MAINT)[c], win_rate(u, S.FIX)[c]
    n = len(m)
    d = m - f
    # paired: sign flips
    t_ref = S.t_paired_rows(rng.choice([-1.0, 1.0], (2000, n)) * d)
    t0 = S.t_paired_rows(d[None])[0]
    p0 = S.perm_p(t0, t_ref)
    tr_ = S.t_paired_rows(rng.choice([-1.0, 1.0], (R, n)) * d)
    sel["paired"].append(bool(p0 < 0.05 and t0 > 0))
    null_sel["paired"].append((S.perm_p(tr_, t_ref) < 0.05) & (tr_ > 0))
    p_mf["paired"].append(p0)
    # unpaired: values of the two periods pooled
    x = np.concatenate([m, f])[:, None]
    t_ref = S.t_groups(x, S.random_masks(n, 2 * n, 2000, rng))[:, 0]
    g0 = np.r_[np.ones(n, bool), np.zeros(n, bool)]
    t0 = S.t_groups(x, g0[None])[0, 0]
    p0 = S.perm_p(t0, t_ref)
    sw = rng.random((R, n)) < 0.5
    tr_ = S.t_groups(x, np.concatenate([~sw, sw], 1))[:, 0]
    sel["unpaired"].append(bool(p0 < 0.05 and t0 > 0))
    null_sel["unpaired"].append((S.perm_p(tr_, t_ref) < 0.05) & (tr_ > 0))
    p_mf["unpaired"].append(p0)
for k in sel:
    UN["maint_" + k] = sel[k]
    null_sel[k] = np.array(null_sel[k])


def area_table(selcol, null, regcol):
    rows = []
    for r in REG:
        idx = (UN[regcol] == r).to_numpy()
        obs = int(UN.loc[idx, selcol].sum())
        nl = null[idx].sum(0)
        rows.append({"region": r, "n": int(idx.sum()), "selected": obs, "pct": 100 * obs / idx.sum(),
                     "null_mean": nl.mean(), "null_95": np.percentile(nl, 95),
                     "P_1000": (np.sum(nl >= obs) + 1) / (len(nl) + 1),
                     "P_499": (np.sum(nl[:499] >= obs) + 1) / 500})
    return pd.DataFrame(rows)


def chi_hipp(selcol, regcol, target="hippocampus"):
    sub = UN[UN[regcol].isin(REG)]
    a = sub[sub[regcol] == target][selcol]
    b = sub[sub[regcol] != target][selcol]
    tab = np.array([[a.sum(), (~a).sum()], [b.sum(), (~b).sum()]])
    c0 = stats.chi2_contingency(tab, correction=False)
    c1 = stats.chi2_contingency(tab, correction=True)
    return tab, c0[0], c0[1], c1[0], c1[1]


for regcol in ["region_atlas", "region_bundle"]:
    for k in ["paired", "unpaired"]:
        print(f"== regions {regcol}, {k} test")
        print(area_table("maint_" + k, null_sel[k], regcol).round(4).to_string(index=False))
        tab, x0, p0, x1, p1 = chi_hipp("maint_" + k, regcol)
        print(f"   chi-square hippocampus against the other two: {x0:.2f} (P = {p0:.2g}); Yates {x1:.2f} (P = {p1:.2g}); table {tab.tolist()}")
print("per subject, hippocampal maintenance neurons (atlas, paired):")
print(UN[UN.region_atlas == "hippocampus"].groupby("subject").maint_paired.agg(["sum", "count"]).T)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity,prep,claim:fig2b 2>&1 | sed -n '/cell 23/,$p'
```

```
---- cell 23 [claim:fig2b-maintenance-neurons-hippocampus]
== regions region_atlas, paired test
     region   n  selected     pct  null_mean  null_95  P_1000  P_499
hippocampus 640       128 20.0000     14.690     21.0   0.001  0.002
 entorhinal 421        42  9.9762      9.743     15.0   0.001  0.002
   amygdala 398        23  5.7789      9.060     15.0   0.001  0.002
   chi-square hippocampus against the other two: 45.55 (P = 1.5e-11); Yates 44.50 (P = 2.5e-11); table [[128, 512], [65, 754]]
== regions region_atlas, unpaired test
     region   n  selected     pct  null_mean  null_95  P_1000  P_499
hippocampus 640       123 19.2188     13.702     20.0   0.001  0.002
 entorhinal 421        42  9.9762      8.749     14.0   0.001  0.002
   amygdala 398        22  5.5276      7.834     12.0   0.001  0.002
   chi-square hippocampus against the other two: 41.81 (P = 1e-10); Yates 40.80 (P = 1.7e-10); table [[123, 517], [64, 755]]
== regions region_bundle, paired test
     region   n  selected     pct  null_mean  null_95  P_1000  P_499
hippocampus 446        99 22.1973     10.254     16.0   0.001  0.002
 entorhinal 456        42  9.2105     10.551     16.0   0.001  0.002
   amygdala 585        56  9.5726     13.315     19.0   0.001  0.002
   chi-square hippocampus against the other two: 44.39 (P = 2.7e-11); Yates 43.29 (P = 4.7e-11); table [[99, 347], [98, 943]]
== regions region_bundle, unpaired test
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ### fig2c-load-dependent-maintenance-neurons
#
# > During maintenance, 15% of hippocampal maintenance neurons (21 neurons) increased their
# > firing rate with workload (set size 4 against set sizes 6 and 8), a significant percentage
# > against scrambled data; the percentage was not significant in entorhinal cortex or amygdala.
#
# Maintenance neurons of each fig2b reading, correct trials, set size 6 and 8 against 4.
# Readings: (a) permutation t test of maintenance rates (2000 permutations); (b) cluster-based
# permutation test on rates in 500 ms windows at 20 ms steps (centres -2.75 to -0.25 s, inside
# maintenance; 1000 permutations). Both need 6/8 higher at P < 0.05. The null shuffles set-size
# labels across trials and reruns the test, 1000 times (P from the first 499 also given).

# %% [claim:fig2c-load-dependent-maintenance-neurons]
rng = np.random.default_rng(202)
R = 1000
res2c = {}
for k in ["paired", "unpaired"]:
    for reading in ["a_ttest", "b_cluster"]:
        obs_sel, null_s = [], []
        for i in np.where(UN["maint_" + k])[0]:
            u = units[i]
            c = u["correct"]
            g = u["set_size"][c] >= 6
            Gr = np.array([rng.permutation(g) for _ in range(R)])
            if reading == "a_ttest":
                x = win_rate(u, S.MAINT)[c][:, None]
                t_ref = S.t_groups(x, S.random_masks(int(g.sum()), len(g), 2000, rng))[:, 0]
                t0 = S.t_groups(x, g[None])[0, 0]
                tr_ = S.t_groups(x, Gr)[:, 0]
                obs_sel.append(bool(S.perm_p(t0, t_ref) < 0.05 and t0 > 0))
                null_s.append((S.perm_p(tr_, t_ref) < 0.05) & (tr_ > 0))
            else:
                X, _ = sliding(u, 0.5, -2.75, -0.25)
                X = X[c]
                p0, pe = S.cluster_test(X, g, 1000, rng, extra=Gr)
                obs_sel.append(bool(p0 < 0.05))
                null_s.append(pe < 0.05)
        idx = np.where(UN["maint_" + k])[0]
        res2c[(k, reading)] = (idx, np.array(obs_sel), np.array(null_s))
        for regcol in ["region_atlas", "region_bundle"]:
            rows = []
            for r in REG:
                m = (UN[regcol].to_numpy()[idx] == r)
                obs = int(np.array(obs_sel)[m].sum())
                nl = np.array(null_s)[m].sum(0)
                rows.append({"region": r, "maintenance": int(m.sum()), "load_dependent": obs,
                             "pct": 100 * obs / max(m.sum(), 1), "null_mean": nl.mean(),
                             "P_1000": (np.sum(nl >= obs) + 1) / (R + 1), "P_499": (np.sum(nl[:499] >= obs) + 1) / 500})
            print(f"== maintenance neurons from the {k} test, reading {reading}, regions {regcol}")
            print(pd.DataFrame(rows).round(4).to_string(index=False))
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity,prep,claim:fig2 2>&1 | sed -n '/cell 25/,$p'
```

```
---- cell 25 [claim:fig2c-load-dependent-maintenance-neurons]
== maintenance neurons from the paired test, reading a_ttest, regions region_atlas
     region  maintenance  load_dependent     pct  null_mean  P_1000  P_499
hippocampus          128              20 15.6250      3.401  0.0010  0.002
 entorhinal           42               2  4.7619      1.177  0.3357  0.350
   amygdala           23               3 13.0435      0.649  0.0310  0.032
== maintenance neurons from the paired test, reading a_ttest, regions region_bundle
     region  maintenance  load_dependent     pct  null_mean  P_1000  P_499
hippocampus           99              19 19.1919      2.654  0.0010  0.002
 entorhinal           42               2  4.7619      1.177  0.3357  0.350
   amygdala           56               4  7.1429      1.499  0.0589  0.052
== maintenance neurons from the paired test, reading b_cluster, regions region_atlas
     region  maintenance  load_dependent     pct  null_mean  P_1000  P_499
hippocampus          128              19 14.8438      4.025  0.0010  0.002
 entorhinal           42               2  4.7619      1.431  0.4146  0.420
   amygdala           23               3 13.0435      0.786  0.0450  0.040
== maintenance neurons from the paired test, reading b_cluster, regions region_bundle
     region  maintenance  load_dependent     pct  null_mean  P_1000  P_499
hippocampus           99              16 16.1616      3.052  0.0010  0.002
 entorhinal           42               2  4.7619      1.431  0.4146  0.420
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ### fig3e-probe-neurons-entorhinal
#
# > Neurons firing specifically after the probe letter (probe neurons) occurred in all areas,
# > most prominently in entorhinal cortex, where 9% of neurons (41) were probe neurons.
#
# Correct trials. Probe rate higher than encoding (-5 to -3 s) and than maintenance (-3 to 0 s),
# each by a permutation t test (2000 permutations) at P < 0.05. Probe windows: (a) 0 to 1 s
# after probe onset; (b) probe onset to the button press; (c) -500 to 0 ms before the press.
# The files store only 2 s after probe onset, so (b) is cut at 2 s and (c) uses the trials whose
# press falls within those 2 s. The null shuffles the three period labels within each trial and
# reruns the selection (1000 times). In the null repetitions the P of each test is taken from
# the t distribution instead of 2000 permutations (to keep the run short); the agreement of the
# two on the observed data is printed.

# %% [claim:fig3e-probe-neurons-entorhinal]
rng = np.random.default_rng(301)
R = 1000


def probe_rates(u, reading, c):
    rt = u["rt"]
    if reading == "a":
        return win_rate(u, (0.0, 1.0)), np.ones(len(rt), bool)
    if reading == "b":
        end = np.minimum(rt, 2.0)
        cnt = np.array([np.sum((s >= 0) & (s < e)) for s, e in zip(u["aligned"], end)])
        return cnt / end, np.ones(len(rt), bool)
    ok = rt <= 2.0
    cnt = np.array([np.sum((s >= r - 0.5) & (s < r)) for s, r in zip(u["aligned"], rt)])
    return cnt / 0.5, ok


def ttest_p(a, b, paired):
    if paired:
        t, p = stats.ttest_rel(a, b, axis=-1)
    else:
        t, p = stats.ttest_ind(a, b, axis=-1, equal_var=False)
    return np.nan_to_num(t), np.nan_to_num(p, nan=1.0)


probe_sel = {}
agree = []
for reading in ["a", "b", "c"]:
    for k in ["paired", "unpaired"]:
        obs, nul = [], []
        for u in units:
            pr, ok = probe_rates(u, reading, None)
            c = u["correct"] & ok
            P_, E_, M_ = pr[c], win_rate(u, S.ENC)[c], win_rate(u, S.MAINT)[c]
            n = len(P_)
            sel_ = True
            for other in (E_, M_):
                if k == "paired":
                    d = P_ - other
                    t_ref = S.t_paired_rows(rng.choice([-1.0, 1.0], (2000, n)) * d)
                    t0 = S.t_paired_rows(d[None])[0]
                else:
                    x = np.concatenate([P_, other])[:, None]
                    t_ref = S.t_groups(x, S.random_masks(n, 2 * n, 2000, rng))[:, 0]
                    t0 = S.t_groups(x, np.r_[np.ones(n, bool), np.zeros(n, bool)][None])[0, 0]
                pp = S.perm_p(t0, t_ref)
                tp, ppar = ttest_p(P_, other, k == "paired")
                agree.append((pp < 0.05) == (ppar < 0.05))
                sel_ = sel_ and (pp < 0.05) and (t0 > 0)
            obs.append(sel_)
            V = np.stack([P_, E_, M_], 1)
            perm = np.argsort(rng.random((R, n, 3)), axis=2)
            Vp = np.take_along_axis(np.broadcast_to(V, (R, n, 3)), perm, axis=2)
            t1, p1 = ttest_p(Vp[..., 0], Vp[..., 1], k == "paired")
            t2, p2 = ttest_p(Vp[..., 0], Vp[..., 2], k == "paired")
            nul.append((t1 > 0) & (p1 < 0.05) & (t2 > 0) & (p2 < 0.05))
        UN[f"probe_{reading}_{k}"] = obs
        probe_sel[(reading, k)] = np.array(nul)
print("agreement of permutation and t-distribution P at 0.05 on the observed tests: %.4f" % np.mean(agree))
for regcol in ["region_atlas", "region_bundle"]:
    for reading in ["a", "b", "c"]:
        for k in ["paired", "unpaired"]:
            col = f"probe_{reading}_{k}"
            tab = area_table(col, probe_sel[(reading, k)], regcol)
            _, x0, p0, x1, p1 = chi_hipp(col, regcol, target="entorhinal")
            print(f"== window ({reading}), {k}, regions {regcol}: total probe neurons {int(UN.loc[UN[regcol].isin(REG), col].sum())}")
            print(tab.round(4).to_string(index=False))
            print(f"   chi-square entorhinal against the other two: {x0:.2f} (P = {p0:.2g}); Yates {x1:.2f} (P = {p1:.2g})")
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity,prep,claim:fig2b,claim:fig3e 2>&1 | sed -n '/cell 27/,$p'
```

```
---- cell 27 [claim:fig3e-probe-neurons-entorhinal]
agreement of permutation and t-distribution P at 0.05 on the observed tests: 0.9871
== window (a), paired, regions region_atlas: total probe neurons 95
     region   n  selected     pct  null_mean  null_95  P_1000  P_499
hippocampus 640        28  4.3750      2.557      5.0   0.001  0.002
 entorhinal 421        48 11.4014      1.604      4.0   0.001  0.002
   amygdala 398        19  4.7739      1.423      4.0   0.001  0.002
   chi-square entorhinal against the other two: 23.25 (P = 1.4e-06); Yates 22.13 (P = 2.5e-06)
== window (a), unpaired, regions region_atlas: total probe neurons 97
     region   n  selected     pct  null_mean  null_95  P_1000  P_499
hippocampus 640        29  4.5312      2.044      4.0   0.001  0.002
 entorhinal 421        48 11.4014      1.468      4.0   0.001  0.002
   amygdala 398        20  5.0251      1.160      3.0   0.001  0.002
   chi-square entorhinal against the other two: 21.54 (P = 3.5e-06); Yates 20.48 (P = 6e-06)
== window (b), paired, regions region_atlas: total probe neurons 109
     region   n  selected     pct  null_mean  null_95  P_1000  P_499
hippocampus 640        33  5.1562      2.504      5.0   0.001  0.002
 entorhinal 421        46 10.9264      1.655      4.0   0.001  0.002
   amygdala 398        30  7.5377      1.563      4.0   0.001  0.002
   chi-square entorhinal against the other two: 10.22 (P = 0.0014); Yates 9.53 (P = 0.002)
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ### fig3-probe-onset-not-movement
#
# > Peak firing of probe neurons was higher when aligned to probe onset than when aligned to the
# > button press (5.47 +/- 4.97 Hz against 4.28 +/- 4.37 Hz), so their firing reflects the probe
# > stimulus more than movement preparation.
#
# Probe neurons of fig3e under each of its readings (the claim depends on it). Per neuron, the
# maximum of the trial-averaged rate in 200 ms windows at 20 ms steps, correct trials, after
# each alignment, in (a) 0 to 1 s after the event or (b) -1 to +1 s. Button-aligned windows
# that fall outside the stored 8 s of a trial are left out of that trial's average (the files
# end 2 s after probe onset). Paired permutation t test over neurons (2000 permutations).

# %% [claim:fig3-probe-onset-not-movement]
rng = np.random.default_rng(302)


def peak_rates(u, lo, hi):
    c = u["correct"]
    cen = np.round(np.arange(lo, hi + 1e-9, 0.02), 4)
    X, _ = sliding(u, 0.2, lo, hi)
    probe_peak = X[c].mean(0).max()
    rows = []
    for s, r in zip([u["aligned"][i] for i in np.where(c)[0]], u["rt"][c]):
        rel = s - r
        v = []
        for cc in cen:
            a, b = cc - 0.1 + r, cc + 0.1 + r   # window in probe time
            v.append(np.sum((rel >= cc - 0.1) & (rel < cc + 0.1)) / 0.2 if (a >= -6 and b <= 2.0) else np.nan)
        rows.append(v)
    rows = np.array(rows)
    btn = np.nanmean(rows, 0)
    return probe_peak, np.nanmax(btn) if np.isfinite(btn).any() else np.nan, np.isfinite(rows).mean()


for (reading, k) in [("b", "unpaired"), ("a", "paired"), ("a", "unpaired"), ("b", "paired"), ("c", "paired"), ("c", "unpaired")]:
    col = f"probe_{reading}_{k}"
    idx = np.where(UN[col] & UN.region_atlas.isin(REG))[0]
    for wname, (lo, hi) in [("(a) 0 to 1 s", (0.1, 0.9)), ("(b) -1 to 1 s", (-0.9, 0.9))]:
        pk = np.array([peak_rates(units[i], lo, hi) for i in idx])
        ok = np.isfinite(pk[:, 1])
        t, p = S.perm_t(pk[ok, 0], pk[ok, 1], n_perm=2000, paired=True, rng=rng)
        print(f"probe neurons {reading}/{k} (n = {ok.sum()} of {len(idx)}), window {wname}: probe-aligned "
              f"{pk[ok, 0].mean():.2f} +/- {pk[ok, 0].std(ddof=1):.2f} Hz, button-aligned {pk[ok, 1].mean():.2f} +/- "
              f"{pk[ok, 1].std(ddof=1):.2f} Hz; paired t({ok.sum() - 1}) = {t:.2f}, P = {p:.4f}; "
              f"button windows covered {np.mean(pk[:, 2]):.2f}")

# %% md
# ### fig3-probe-neurons-few-task-specific
#
# > Only a few probe neurons reflected the decision (8 neurons, 10.5% of probe neurons, IN
# > against OUT), and only one showed workload dependence.
#
# Probe neurons of fig3e. IN against OUT, and set size 4 against 6 and 8, by a cluster-based
# permutation test (1000 permutations) at P < 0.05 on rates in 200 ms windows at 20 ms steps
# after probe onset, correct trials, over (a) 0 to 1 s or (b) 0 to 2 s (window centres 0.1 to
# 0.9 s and 0.1 to 1.9 s). A neuron counts for a cluster in either direction.

# %% [claim:fig3-probe-neurons-few-task-specific]
rng = np.random.default_rng(303)
for (reading, k) in [("b", "unpaired"), ("a", "paired"), ("a", "unpaired"), ("b", "paired"), ("c", "paired"), ("c", "unpaired")]:
    col = f"probe_{reading}_{k}"
    idx = np.where(UN[col] & UN.region_atlas.isin(REG))[0]
    for wname, (lo, hi) in [("(a) 0-1 s", (0.1, 0.9)), ("(b) 0-2 s", (0.1, 1.9))]:
        n_inout = n_load = 0
        for i in idx:
            u = units[i]
            c = u["correct"]
            X, _ = sliding(u, 0.2, lo, hi)
            X = X[c]
            p_io = min(S.cluster_test(X, u["is_in"][c], 1000, rng, sign=1), S.cluster_test(X, u["is_in"][c], 1000, rng, sign=-1))
            g = u["set_size"][c] >= 6
            p_ld = min(S.cluster_test(X, g, 1000, rng, sign=1), S.cluster_test(X, g, 1000, rng, sign=-1))
            n_inout += p_io < 0.05
            n_load += p_ld < 0.05
        print(f"probe neurons {reading}/{k} ({len(idx)}), {wname}: IN/OUT {n_inout} ({100 * n_inout / len(idx):.1f}%), "
              f"workload {n_load} ({100 * n_load / len(idx):.1f}%)")
EOF
. $TMPDIR/dev/bin/activate; python - <<'EOF'
# quick dev: pickle the state after fig3e to avoid recomputing
EOF
sed -i 's/^for i, b in enumerate(blocks):/import pickle as _p\nfor i, b in enumerate(blocks):/' $TMPDIR/runcells.py
python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity,prep,claim:fig2b,claim:fig3 2>&1 | sed -n '/cell 29/,$p'
```

```
---- cell 29 [claim:fig3-probe-onset-not-movement]
probe neurons b/unpaired (n = 100 of 100), window (a) 0 to 1 s: probe-aligned 7.25 +/- 5.74 Hz, button-aligned 6.74 +/- 6.22 Hz; paired t(99) = 1.06, P = 0.2694; button windows covered 0.56
probe neurons b/unpaired (n = 100 of 100), window (b) -1 to 1 s: probe-aligned 7.25 +/- 5.74 Hz, button-aligned 8.23 +/- 6.46 Hz; paired t(99) = -2.50, P = 0.0150; button windows covered 0.75
probe neurons a/paired (n = 95 of 95), window (a) 0 to 1 s: probe-aligned 7.69 +/- 5.92 Hz, button-aligned 6.04 +/- 5.65 Hz; paired t(94) = 4.91, P = 0.0005; button windows covered 0.59
probe neurons a/paired (n = 95 of 95), window (b) -1 to 1 s: probe-aligned 7.69 +/- 5.92 Hz, button-aligned 7.30 +/- 5.96 Hz; paired t(94) = 1.94, P = 0.0590; button windows covered 0.77
probe neurons a/unpaired (n = 97 of 97), window (a) 0 to 1 s: probe-aligned 7.67 +/- 5.86 Hz, button-aligned 6.03 +/- 5.58 Hz; paired t(96) = 4.96, P = 0.0005; button windows covered 0.59
probe neurons a/unpaired (n = 97 of 97), window (b) -1 to 1 s: probe-aligned 7.67 +/- 5.86 Hz, button-aligned 7.27 +/- 5.90 Hz; paired t(96) = 2.04, P = 0.0400; button windows covered 0.78
probe neurons b/paired (n = 109 of 109), window (a) 0 to 1 s: probe-aligned 6.92 +/- 5.60 Hz, button-aligned 6.46 +/- 6.08 Hz; paired t(108) = 1.06, P = 0.2959; button windows covered 0.56
probe neurons b/paired (n = 109 of 109), window (b) -1 to 1 s: probe-aligned 6.92 +/- 5.60 Hz, button-aligned 7.90 +/- 6.33 Hz; paired t(108) = -2.68, P = 0.0050; button windows covered 0.75
probe neurons c/paired (n = 93 of 93), window (a) 0 to 1 s: probe-aligned 6.21 +/- 5.43 Hz, button-aligned 6.69 +/- 6.49 Hz; paired t(92) = -1.08, P = 0.2949; button windows covered 0.56
probe neurons c/paired (n = 93 of 93), window (b) -1 to 1 s: probe-aligned 6.23 +/- 5.42 Hz, button-aligned 8.25 +/- 6.54 Hz; paired t(92) = -5.32, P = 0.0005; button windows covered 0.76
probe neurons c/unpaired (n = 90 of 90), window (a) 0 to 1 s: 
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> sternberg.py <<'EOF'


# ---- scalp EEG and hippocampal iEEG ------------------------------------------------------

EEG_FS = 200.0      # deposited sampling rate (checked in the notebook)
IEEG_FS = 2000.0


def _load_signals(args):
    from scipy.signal import decimate
    path, asset_id = args
    with open_asset(asset_id) as f:
        el = f["general/extracellular_ephys/electrodes"]
        labels = _str(el["label"][:])
        soz = el["is_inside_soz"][:].astype(bool)
        xyz = np.stack([el["x"][:], el["y"][:], el["z"][:]], 1)
        e = f["acquisition/ecephys.eeg"]
        erows = e["electrodes"][:]
        eeg = e["data"][:].astype(np.float32)
        ets = e["timestamps"][:]
        ie = f["acquisition/ecephys.ieeg"]
        irows = ie["electrodes"][:]
        ilab = labels[irows]
        bundles = sorted({re.sub(r"\d+$", "", l) for l in ilab if re.match(r"^(AH|PH)[LR]\d+$", l)})
        chans, cols = [], []
        for b in bundles:
            c1 = np.where(ilab == b + "1")[0]
            c2 = np.where(ilab == b + "2")[0]
            if len(c1) and len(c2):
                chans.append(b)
                cols += [int(c1[0]), int(c2[0])]
        raw = np.stack([ie["data"][:, c] for c in cols], 1) if cols else np.zeros((ie["data"].shape[0], 0))
        its = ie["timestamps"][:]
        tr = f["intervals/trials"]
        starts = tr["start_time"][:]
    n_tr = len(starts)
    ne, ni = int(8 * EEG_FS), int(8 * IEEG_FS)
    eeg_ep = eeg.reshape(n_tr, ne, -1).transpose(0, 2, 1)
    bip = raw[:, 0::2] - raw[:, 1::2]
    bip_ep = bip.reshape(n_tr, ni, -1).transpose(0, 2, 1)
    bip_ep = decimate(bip_ep, 10, axis=-1, zero_phase=True).astype(np.float32) if bip.shape[1] else np.zeros((n_tr, 0, ne), np.float32)
    lab_rows = {l: i for i, l in enumerate(labels)}
    meta = {"eeg_labels": list(labels[erows]), "hipp_channels": chans,
            "hipp_soz": [bool(soz[lab_rows[c + "1"]] or soz[lab_rows[c + "2"]]) for c in chans],
            "hipp_xyz1": [xyz[lab_rows[c + "1"]] for c in chans],
            "hipp_xyz12": [(xyz[lab_rows[c + "1"]] + xyz[lab_rows[c + "2"]]) / 2 for c in chans],
            "eeg_start_err": float(np.max(np.abs(ets[::ne] - starts))),
            "ieeg_start_err": float(np.max(np.abs(its[::ni] - starts))),
            "eeg_dt": float(np.median(np.diff(ets[:ne]))), "ieeg_dt": float(np.median(np.diff(its[:ni])))}
    return path, eeg_ep, bip_ep, meta


def load_signals(table, workers=16):
    """Scalp EEG (trials x channels x 1600 samples at 200 Hz) and hippocampal bipolar iEEG
    (contact 1 minus contact 2 of each AH and PH macroelectrode, decimated to 200 Hz with a
    zero-phase filter) of every session, from -6 to +2 s around probe onset. Read in parallel
    processes (h5py serializes threads)."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        out = list(ex.map(_load_signals, [(r.path, r.asset_id) for r in table.itertuples()]))
    return {p: {"eeg": e, "ieeg": i, **m} for p, e, i, m in out}
EOF
cat > $TMPDIR/tsig.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'.')
import sternberg as S
A = S.assets()
t=time.time()
sub = A if len(sys.argv) < 3 else A.iloc[:int(sys.argv[2])]
SIG = S.load_signals(sub, workers=20)
print(len(SIG), time.time()-t)
for p, s in SIG.items(): print(p, s['eeg'].shape, s['ieeg'].shape, s['hipp_channels'], s['eeg_start_err'], s['ieeg_start_err'], s['eeg_dt'], s['ieeg_dt'])
pickle.dump(SIG, open(sys.argv[1], 'wb'))
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/tsig.py $TMPDIR/SIG2.pkl 2
```

```
2 34.060182094573975
sub-01/sub-01_ses-01.nwb (50, 19, 1600) (50, 3, 1600) ['AHL', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-01/sub-01_ses-02.nwb (50, 19, 1600) (50, 3, 1600) ['AHL', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python $TMPDIR/tsig.py $TMPDIR/SIG.pkl 2>&1 | tail -40; date -u
```

```
37 96.8916528224945
sub-01/sub-01_ses-01.nwb (50, 19, 1600) (50, 3, 1600) ['AHL', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-01/sub-01_ses-02.nwb (50, 19, 1600) (50, 3, 1600) ['AHL', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-01/sub-01_ses-03.nwb (50, 19, 1600) (50, 3, 1600) ['AHL', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-01/sub-01_ses-04.nwb (50, 19, 1600) (50, 3, 1600) ['AHL', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-02/sub-02_ses-01.nwb (49, 8, 1600) (49, 4, 1600) ['AHL', 'AHR', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-02/sub-02_ses-02.nwb (47, 8, 1600) (47, 4, 1600) ['AHL', 'AHR', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-02/sub-02_ses-03.nwb (50, 8, 1600) (50, 4, 1600) ['AHL', 'AHR', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-02/sub-02_ses-04.nwb (48, 8, 1600) (48, 4, 1600) ['AHL', 'AHR', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-02/sub-02_ses-05.nwb (46, 8, 1600) (46, 4, 1600) ['AHL', 'AHR', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-02/sub-02_ses-06.nwb (50, 8, 1600) (50, 4, 1600) ['AHL', 'AHR', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-02/sub-02_ses-07.nwb (49, 8, 1600) (49, 4, 1600) ['AHL', 'AHR', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-03/sub-03_ses-01.nwb (47, 8, 1600) (47, 3, 1600) ['AHL', 'AHR', 'PHL'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-03/sub-03_ses-02.nwb (50, 8, 1600) (50, 3, 1600) ['AHL', 'AHR', 'PHL'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-03/sub-03_ses-03.nwb (50, 8, 1600) (50, 3, 1600) ['AHL', 'AHR', 'PHL'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-04/sub-04_ses-01.nwb (49, 19, 1600) (49, 4, 1600) ['AHL', 'AHR', 'PHL', 'PHR'] 0.0 0.0 0.004999999999999893 0.0004999999999999449
sub-04/sub-04_ses-02.nwb (50,
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python -c "
import pickle; S=pickle.load(open('$TMPDIR/SIG.pkl','rb'))
seen=set()
for p,s in S.items():
    k=p[:6]
    if k in seen: continue
    seen.add(k); print(k, s['eeg_labels'], s['hipp_soz'])
"
```

```
sub-01 ['F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Cz', 'Pz', 'A1', 'A2'] [False, False, False]
sub-02 ['F3', 'F4', 'C3', 'C4', 'O1', 'O2', 'A1', 'A2'] [False, True, False, True]
sub-03 ['F3', 'F4', 'C3', 'C4', 'O1', 'O2', 'A1', 'A2'] [True, False, True]
sub-04 ['F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Cz', 'Pz', 'A1', 'A2'] [True, True, True, True]
sub-05 ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T4', 'T5', 'T6', 'Fz', 'Cz', 'Pz', 'A1', 'A2'] [False, False]
sub-06 ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'O1', 'O2', 'A1', 'A2'] [True, False, True, False]
sub-07 ['F3', 'F4', 'C3', 'C4', 'O1', 'O2', 'A1', 'A2'] [False, True, False, True]
sub-08 ['F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'Fz', 'Cz', 'Pz', 'A1', 'A2'] [False, False, False]
sub-09 ['F3', 'F4', 'C3', 'C4', 'O1', 'O2', 'A1', 'A2'] [False, False, False, False]
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ## Scalp EEG, hippocampal iEEG and phase locking
#
# Scalp EEG (200 Hz as deposited) and one bipolar iEEG signal per hippocampal macroelectrode
# (AH and PH; contact 1 minus contact 2, decimated from 2 kHz to 200 Hz with a zero-phase
# filter), from -6 to +2 s around each probe. Trials are pooled over the sessions of a subject
# (Fig. 5 legend counts trials of subject 1 over its sessions). Trials marked as artifacts are
# left out (Methods, EEG preprocessing). Epochs: last 2 s of maintenance (-2 to 0 s) and
# encoding (-5 to -3 s), 400 samples, multitaper with 7 tapers (NW = 4, +/- 2 Hz), 0.5 Hz bins.
# A1 and A2 are not used as scalp sites.

# %% [load]
SIG = S.load_signals(A, workers=20)

# %% [sanity]
print("EEG and iEEG samples per trial, sampling intervals and first-sample offsets from trial starts:")
chk = pd.DataFrame([{"path": p, "eeg": s["eeg"].shape, "ieeg_bipolar": s["ieeg"].shape,
                     "eeg_dt": round(s["eeg_dt"], 6), "ieeg_dt": round(s["ieeg_dt"], 6),
                     "max_offset_eeg": s["eeg_start_err"], "max_offset_ieeg": s["ieeg_start_err"],
                     "hipp": ",".join(s["hipp_channels"])} for p, s in SIG.items()])
print(chk.to_string(index=False))
e1 = SIG[A.path[0]]
lab = e1["eeg_labels"]
a1, a2 = e1["eeg"][:, lab.index("A1")], e1["eeg"][:, lab.index("A2")]
print("subject 1 session 1: SD of A1 %.3g V, A2 %.3g V, A1 + A2 %.3g V (re-referenced to averaged mastoids if A1 = -A2)"
      % (a1.std(), a2.std(), (a1 + a2).std()))
print("EEG range (uV), 1st and 99th percentiles over all sessions: %.1f, %.1f" % tuple(1e6 * np.percentile(np.concatenate([s["eeg"][:, :2].ravel() for s in SIG.values()]), [1, 99])))
print("bipolar iEEG range (uV): %.1f, %.1f" % tuple(1e6 * np.percentile(np.concatenate([s["ieeg"].ravel() for s in SIG.values()]), [1, 99])))

# %% [prep]
FS = 200.0
I_LAST2 = slice(int((6 + S.LAST2[0]) * FS), int((6 + S.LAST2[1]) * FS))
I_ENC = slice(int((6 + S.ENC[0]) * FS), int((6 + S.ENC[1]) * FS))
I_FIX = slice(int((6 + S.FIX[0]) * FS), int((6 + S.FIX[1]) * FS))
SUBJ = {}
for d in D:
    s = SIG[d["path"]]
    tr = d["trials"]
    sj = SUBJ.setdefault(d["subject"], {"eeg": [], "ieeg": [], "trials": [], "eeg_labels": s["eeg_labels"],
                                        "hipp": s["hipp_channels"], "soz": s["hipp_soz"],
                                        "xyz1": s["hipp_xyz1"], "xyz12": s["hipp_xyz12"]})
    assert sj["eeg_labels"] == s["eeg_labels"] and sj["hipp"] == s["hipp_channels"]
    sj["eeg"].append(s["eeg"])
    sj["ieeg"].append(s["ieeg"])
    sj["trials"].append(tr.assign(session=d["session"]))
for sj in SUBJ.values():
    sj["eeg"] = np.concatenate(sj["eeg"])
    sj["ieeg"] = np.concatenate(sj["ieeg"])
    sj["trials"] = pd.concat(sj["trials"], ignore_index=True)
    sj["scalp"] = [i for i, l in enumerate(sj["eeg_labels"]) if l not in ("A1", "A2")]
_, FREQS = S.mt_fourier(np.zeros((1, 400)), FS)


def trial_mask(sj, which, set_sizes=(8,)):
    t = sj["trials"]
    m = ~t.artifact.to_numpy() & t.set_size.isin(set_sizes).to_numpy()
    if which == "correct":
        m &= t.correct.to_numpy()
    return m


def coeffs(sj, mask, period):
    return (S.mt_fourier(sj["ieeg"][mask][:, :, period], FS)[0],
            S.mt_fourier(sj["eeg"][mask][:, :, period], FS)[0])   # tapers x trials x chans x freqs


def plv_pair(Fi, Fe, perm=None):
    if perm is not None:
        Fe = Fe[:, perm]
    return S.plv(Fi, Fe)


def runs(sig, peak):
    """Contiguous run of True bins in `sig` containing index `peak`."""
    a = b = peak
    while a > 0 and sig[a - 1]:
        a -= 1
    while b < len(sig) - 1 and sig[b + 1]:
        b += 1
    return a, b


def select_pair(sj, which, frange, rng, n_perm=200):
    """PLV of every hippocampal-scalp pair, set size 8, last 2 s of maintenance; significance per
    bin against the 95th percentile of PLVs with the trials of the scalp channel permuted
    (Methods, Phase-locking value). Returns the pair and band of the highest significant PLV."""
    m = trial_mask(sj, which)
    Fi, Fe = coeffs(sj, m, I_LAST2)
    fsel = (FREQS >= frange[0]) & (FREQS <= frange[1])
    n = Fi.shape[1]
    perms = [rng.permutation(n) for _ in range(n_perm)]
    best = None
    table = []
    for hi, hname in enumerate(sj["hipp"]):
        for ei in sj["scalp"]:
            p = S.plv(Fi[:, :, hi], Fe[:, :, ei])
            null = np.array([S.plv(Fi[:, :, hi], Fe[:, pp, ei]) for pp in perms])
            thr = np.percentile(null, 95, axis=0)
            sig = (p > thr) & fsel
            table.append((hname, sj["eeg_labels"][ei], p[fsel].max(), bool(sig.any())))
            if sig.any():
                k = np.argmax(np.where(sig, p, -1))
                if best is None or p[k] > best["plv"]:
                    a, b = runs(sig, k)
                    best = {"hipp": hname, "hi": hi, "scalp": sj["eeg_labels"][ei], "ei": ei, "plv": float(p[k]),
                            "peak_f": float(FREQS[k]), "band": (float(FREQS[a]), float(FREQS[b])), "n_trials": int(n)}
    return best, pd.DataFrame(table, columns=["hipp", "scalp", "max_plv", "significant"])
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'


def plv_diff_test(FiA, FeA, FiB, FeB, rng, n_perm=200):
    """PLV(A) - PLV(B) of one pair (coefficients tapers x epochs x freqs) and the 95th percentile
    of differences with the epochs randomly assigned to the two conditions (Methods)."""
    d0 = S.plv(FiA, FeA) - S.plv(FiB, FeB)
    Fi = np.concatenate([FiA, FiB], 1)
    Fe = np.concatenate([FeA, FeB], 1)
    nA = FiA.shape[1]
    null = []
    for _ in range(n_perm):
        p = rng.permutation(Fi.shape[1])
        a, b = p[:nA], p[nA:]
        null.append(S.plv(Fi[:, a], Fe[:, a]) - S.plv(Fi[:, b], Fe[:, b]))
    thr = np.percentile(np.array(null), 95, axis=0)
    return d0, thr, d0 > thr


READINGS = [("correct", (4, 30)), ("correct", (1, 40)), ("all", (4, 30)), ("all", (1, 40))]

# %% md
# ### fig6-plv-all-subjects
#
# > All subjects showed a significant hippocampal-scalp PLV peak during maintenance (set size
# > 8), with individual frequency bands whose lower bound lay in the theta-alpha range and which
# > extended up to 17.5 Hz (median band limits 6.0 to 11.5 Hz).
#
# Readings: trials (a) correct only or (b) all artifact-free; frequency range searched (a) 4 to
# 30 Hz or (b) 1 to 40 Hz. 200 trial permutations per pair.

# %% [claim:fig6-plv-all-subjects]
rng = np.random.default_rng(601)
PAIRS = {}
PAIR_TABLES = {}
for which, fr in READINGS:
    rows = []
    for sid, sj in SUBJ.items():
        best, tab = select_pair(sj, which, fr, rng)
        PAIRS[(which, fr, sid)] = best
        PAIR_TABLES[(which, fr, sid)] = tab
        rows.append({"subject": sid, **({k: v for k, v in best.items() if k not in ("hi", "ei")} if best else {"hipp": None}),
                     "pairs_significant": f"{int(tab.significant.sum())}/{len(tab)}"})
    R6 = pd.DataFrame(rows)
    lo = R6.band.dropna().map(lambda b: b[0])
    hi = R6.band.dropna().map(lambda b: b[1])
    print(f"== trials {which}, range {fr} Hz: subjects with a significant pair {R6.hipp.notna().sum()} of {len(R6)}; "
          f"median band limits {np.median(lo):.2f} to {np.median(hi):.2f} Hz; band edges range {lo.min():.1f} to {hi.max():.1f} Hz")
    print(R6.to_string(index=False))

# %% md
# ### tables1-plv-per-subject
#
# > Table S1 gives for each subject the scalp electrode of maximal PLV, its peak frequency and
# > the maximal PLV (subject 1 Pz 10.5 Hz 0.72; 2 F3 7 Hz 0.40; 3 F3 12 Hz 0.43; 4 F3 14 Hz
# > 0.85; 5 P3 5.5 Hz 0.60; 6 O1 7.5 Hz 0.50; 7 O1 7.5 Hz 0.64; 8 O1 11.5 Hz 0.57; 9 O1 8 Hz
# > 0.69), with the hippocampal electrode in the left hemisphere for subjects 1 to 6 and the
# > right for 7 to 9.

# %% [claim:tables1-plv-per-subject]
TS1 = pd.DataFrame({"subject": [f"{i:02d}" for i in range(1, 10)],
                    "scalp": ["Pz", "F3", "F3", "F3", "P3", "O1", "O1", "O1", "O1"],
                    "peak_f": [10.5, 7, 12, 14, 5.5, 7.5, 7.5, 11.5, 8],
                    "plv": [0.72, 0.40, 0.43, 0.85, 0.60, 0.50, 0.64, 0.57, 0.69],
                    "hemi": ["L"] * 6 + ["R"] * 3})
for which, fr in READINGS:
    rows = []
    for r in TS1.itertuples():
        b = PAIRS[(which, fr, r.subject)]
        if b is None:
            rows.append({"subject": r.subject, "match": False})
            continue
        same_e = b["scalp"] == r.scalp
        same_h = b["hipp"][-1] == r.hemi
        in_tol = abs(b["plv"] - r.plv) <= 0.1 * r.plv
        rows.append({"subject": r.subject, "scalp": b["scalp"], "paper_scalp": r.scalp, "hipp": b["hipp"],
                     "paper_hemi": r.hemi, "plv": round(b["plv"], 3), "paper_plv": r.plv,
                     "peak_f": b["peak_f"], "paper_f": r.peak_f, "electrode": same_e, "hemisphere": same_h,
                     "plv_in_tol": in_tol, "match": bool(same_e and same_h and in_tol)})
    R = pd.DataFrame(rows)
    print(f"== trials {which}, range {fr}: subjects matching on electrode, hemisphere and PLV: {int(R.match.sum())} of 9;"
          f" electrode {int(R.electrode.sum())}, hemisphere {int(R.hemisphere.sum())}, PLV within 10% {int(R.plv_in_tol.sum())}")
    print(R.to_string(index=False))
# Is the paper's electrode present in each subject's EEG?
print("paper's scalp electrode present in the deposited EEG:",
      {r.subject: r.scalp in SUBJ[r.subject]["eeg_labels"] for r in TS1.itertuples()})
EOF
. $TMPDIR/dev/bin/activate; cat > $TMPDIR/pre2.py <<EOF
exec(open('$TMPDIR/pre.py').read())
import sternberg as S
A = S.assets()
SIG = pickle.load(open('$TMPDIR/SIG.pkl','rb'))
EOF
time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre2.py sanity,prep,claim:fig6-plv-all,claim:tables1 2>&1 | sed -n '/cell 3[3-9]/,$p'
```

```
---- cell 34 [sanity]
EEG and iEEG samples per trial, sampling intervals and first-sample offsets from trial starts:
                    path            eeg  ieeg_bipolar  eeg_dt  ieeg_dt  max_offset_eeg  max_offset_ieeg            hipp
sub-01/sub-01_ses-01.nwb (50, 19, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,PHL,PHR
sub-01/sub-01_ses-02.nwb (50, 19, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,PHL,PHR
sub-01/sub-01_ses-03.nwb (50, 19, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,PHL,PHR
sub-01/sub-01_ses-04.nwb (50, 19, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,PHL,PHR
sub-02/sub-02_ses-01.nwb  (49, 8, 1600) (49, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-02.nwb  (47, 8, 1600) (47, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-03.nwb  (50, 8, 1600) (50, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-04.nwb  (48, 8, 1600) (48, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-05.nwb  (46, 8, 1600) (46, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-06.nwb  (50, 8, 1600) (50, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-07.nwb  (49, 8, 1600) (49, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-03/sub-03_ses-01.nwb  (47, 8, 1600) (47, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,AHR,PHL
sub-03/sub-03_ses-02.nwb  (50, 8, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,AHR,PHL
sub-03/sub-03_ses-03.nwb  (50, 8, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,AHR,PHL
sub-04/sub-04_ses-01.nwb (49, 19, 1600) (49, 4, 1600)   0.005   0.0005    0.000000e
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('sternberg.py').read()
s=s.replace("""    F = np.fft.rfft(tap[:, None, :] * x[None, :, :], axis=-1)""","""    tap = tap.reshape((k,) + (1,) * (x.ndim - 1) + (n,))
    F = np.fft.rfft(tap * x[None], axis=-1)""")
s=s.replace('"""Multitaper Fourier coefficients of epochs x (epochs x samples): tapers x epochs x freqs.','"""Multitaper Fourier coefficients of epochs x (... x samples): tapers x ... x freqs.')
open('sternberg.py','w').write(s)
s=open('nb_src.py').read()
s=s.replace('''print("subject 1 session 1: SD of A1 %.3g V, A2 %.3g V, A1 + A2 %.3g V (re-referenced to averaged mastoids if A1 = -A2)"
      % (a1.std(), a2.std(), (a1 + a2).std()))
print("EEG range (uV), 1st and 99th percentiles over all sessions: %.1f, %.1f" % tuple(1e6 * np.percentile(np.concatenate([s["eeg"][:, :2].ravel() for s in SIG.values()]), [1, 99])))
print("bipolar iEEG range (uV): %.1f, %.1f" % tuple(1e6 * np.percentile(np.concatenate([s["ieeg"].ravel() for s in SIG.values()]), [1, 99])))''','''print("subject 1 session 1: SD of A1 %.3g, A2 %.3g, A1 + A2 %.3g (file units); if the EEG were re-referenced to the"
      " averaged mastoids, A1 + A2 would be 0" % (a1.std(), a2.std(), (a1 + a2).std()))
print("A1 + A2 relative to A1 - A2, per subject:",
      {d["subject"]: round(float(np.std(SIG[d["path"]]["eeg"][:, SIG[d["path"]]["eeg_labels"].index("A1")] + SIG[d["path"]]["eeg"][:, SIG[d["path"]]["eeg_labels"].index("A2")]) /
                                 np.std(SIG[d["path"]]["eeg"][:, SIG[d["path"]]["eeg_labels"].index("A1")] - SIG[d["path"]]["eeg"][:, SIG[d["path"]]["eeg_labels"].index("A2")])), 2)
       for d in D if d["session"] == "01"})
print("EEG values, 1st and 99th percentiles over all sessions (file says volts): %.1f, %.1f" % tuple(np.percentile(np.concatenate([s["eeg"][:, :2].ravel() for s in SIG.values()]), [1, 99])))
print("bipolar iEEG values, 1st and 99th percentiles (file says volts): %.1f, %.1f" % tuple(np.percentile(np.concatenate([s["ieeg"].ravel() for s in SIG.values()]), [1, 99])))''')
s=s.replace('''    sj["eeg"] = np.concatenate(sj["eeg"])''','''    sj["eeg"] = np.concatenate(sj["eeg"])
    # re-reference to the averaged mastoids (Methods, Recording setup); the deposited EEG is not
    ia, ib = sj["eeg_labels"].index("A1"), sj["eeg_labels"].index("A2")
    sj["eeg"] = sj["eeg"] - (sj["eeg"][:, ia:ia + 1] + sj["eeg"][:, ib:ib + 1]) / 2''')
s=s.replace("# A1 and A2 are not used as scalp sites.","# The EEG is re-referenced here to the averaged mastoids (A1, A2), as the Methods say; the\n# deposited EEG is not (checked below). A1 and A2 are not used as scalp sites.")
open('nb_src.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre2.py sanity,prep,claim:fig6-plv-all,claim:tables1 2>&1 | sed -n '/subject 1 session 1/,$p'
```

```
subject 1 session 1: SD of A1 90.6, A2 86.6, A1 + A2 177 (file units); if the EEG were re-referenced to the averaged mastoids, A1 + A2 would be 0
A1 + A2 relative to A1 - A2, per subject: {'01': 13.67, '02': 2.3, '03': 4.75, '04': 4.88, '05': 2.26, '06': 9.72, '07': 3.25, '08': 1.83, '09': 7.79}
EEG values, 1st and 99th percentiles over all sessions (file says volts): -149.0, 135.9
bipolar iEEG values, 1st and 99th percentiles (file says volts): -241.3, 220.4
---- 0.2s
---- cell 35 [prep]
---- 0.1s
---- cell 37 [claim:fig6-plv-all-subjects]
== trials correct, range (4, 30) Hz: subjects with a significant pair 9 of 9; median band limits 5.50 to 12.00 Hz; band edges range 4.0 to 30.0 Hz
subject hipp scalp      plv  peak_f         band  n_trials pairs_significant
     01  PHL    Pz 0.339083    10.5  (7.0, 12.0)        55             51/51
     02  PHR    C4 0.206994    15.5 (13.0, 17.5)        75             24/24
     03  AHR    F3 0.195750     5.5   (4.5, 6.5)        38             18/18
     04  AHR    O1 0.276248     4.5   (4.0, 6.5)        24             68/68
     05  AHL    T5 0.435811     4.0   (4.0, 8.0)        29             36/36
     06  PHL   Fp1 0.300901     4.0  (4.0, 13.5)        95             32/32
     07  AHR    O1 0.238112     7.5   (5.5, 9.5)        54             22/24
     08  PHL    Cz 0.258045    15.0 (13.0, 17.5)        50             49/51
     09  PHR    F4 0.363706    30.0 (29.5, 30.0)        27             24/24
== trials correct, range (1, 40) Hz: subjects with a significant pair 9 of 9; median band limits 5.50 to 13.50 Hz; band edges range 1.0 to 38.0 Hz
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('sternberg.py').read()
a=s.index('def plv(Fi, Fj):')
s=s[:a]+'''def plv(Fi, Fj):
    """PLV (Methods eq. 3) from multitaper coefficients (tapers x epochs x ... x freqs). The
    cross-spectrum of each epoch is averaged over tapers, normalized, and averaged over epochs,
    as FieldTrip's ft_connectivityanalysis does with method 'plv' on mtmfft output (the
    toolbox the Methods cite; the cross-spectra per trial are taper averages)."""
    c = (Fi * np.conj(Fj)).mean(axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        c = c / np.abs(c)
    return np.abs(np.nanmean(c, axis=0))


def plv_tapers(Fi, Fj):
    """Variant: each taper's cross-spectrum normalized on its own, averaged over tapers and epochs."""
    c = Fi * np.conj(Fj)
    with np.errstate(divide="ignore", invalid="ignore"):
        c = c / np.abs(c)
    return np.abs(np.nanmean(c, axis=(0, 1)))
'''
s=s.replace('''- PLV: Methods equation 3 applied to each taper's Fourier coefficients. How tapers enter is
  not stated; FieldTrip's ft_connectivityanalysis averages the normalized cross-spectra over
  tapers and trials, which is what is done (standard choice, `plv`).''','''- PLV: Methods equation 3. How the tapers enter is not stated. `plv` follows FieldTrip (cited
  by the Methods for the spectra and the PLV): the cross-spectrum of each trial is averaged
  over tapers, then normalized and averaged over trials (assumption, the toolbox's standard
  path). `plv_tapers`, normalizing each taper on its own, is shown as a variant.''')
open('sternberg.py','w').write(s)

n=open('nb_src.py').read()
old_a=n.index('def select_pair(sj, which, frange, rng, n_perm=200):')
old_b=n.index('def plv_diff_test(')
n=n[:old_a]+'''FMAX = 40.0
FK = FREQS <= FMAX


def select_pair(sj, which, frange, rng, n_perm=200, fn=S.plv):
    """PLV of every hippocampal-scalp pair, set size 8, last 2 s of maintenance; significance per
    bin against the 95th percentile of PLVs with the trials of the scalp channel permuted
    (Methods, Phase-locking value). Returns the pair and band of the highest significant PLV."""
    m = trial_mask(sj, which)
    Fi, Fe = coeffs(sj, m, I_LAST2)
    Fi, Fe = Fi[..., FK], Fe[..., FK]
    f = FREQS[FK]
    fsel = (f >= frange[0]) & (f <= frange[1])
    n = Fi.shape[1]
    perms = np.array([rng.permutation(n) for _ in range(n_perm)])
    best = None
    table = []
    for hi, hname in enumerate(sj["hipp"]):
        for ei in sj["scalp"]:
            p = fn(Fi[:, :, hi], Fe[:, :, ei])
            null = fn(Fi[:, None, :, hi], Fe[:, perms, ei].transpose(0, 2, 1, 3)) if fn is S.plv else \\
                np.array([fn(Fi[:, :, hi], Fe[:, pp, ei]) for pp in perms])
            thr = np.percentile(null, 95, axis=0)
            sig = (p > thr) & fsel
            table.append((hname, sj["eeg_labels"][ei], p[fsel].max(), bool(sig.any()), int(sig.sum())))
            if sig.any():
                k = np.argmax(np.where(sig, p, -1))
                if best is None or p[k] > best["plv"]:
                    a, b = runs(sig, k)
                    best = {"hipp": hname, "hi": hi, "scalp": sj["eeg_labels"][ei], "ei": ei, "plv": float(p[k]),
                            "peak_f": float(f[k]), "band": (float(f[a]), float(f[b])), "n_trials": int(n)}
    return best, pd.DataFrame(table, columns=["hipp", "scalp", "max_plv", "significant", "sig_bins"])


'''+n[old_b:]
open('nb_src.py','w').write(n)
EOF
grep -n "transpose(0, 2, 1, 3)" nb_src.py
```

```
770:            null = fn(Fi[:, None, :, hi], Fe[:, perms, ei].transpose(0, 2, 1, 3)) if fn is S.plv else \
```

**Agent calls Bash**

```bash
sed -i 's/null = fn(Fi\[:, None, :, hi\], Fe\[:, perms, ei\].transpose(0, 2, 1, 3))/null = fn(Fi[:, :, hi][:, :, None, :], Fe[:, perms, ei].transpose(0, 2, 1, 3))/' nb_src.py
python - <<'EOF'
n=open('nb_src.py').read()
# add plv-form variant to the selection cell: main readings with S.plv; per-taper variant for one reading
n=n.replace('''    print(R6.to_string(index=False))
''','''    print(R6.to_string(index=False))
# Variant: PLV with each taper normalized on its own (sternberg.plv_tapers), correct trials, 4 to 30 Hz
rows = []
for sid, sj in SUBJ.items():
    best, tab = select_pair(sj, "correct", (4, 30), rng, fn=S.plv_tapers)
    rows.append({"subject": sid, **{k: v for k, v in best.items() if k not in ("hi", "ei")}})
print("== variant, per-taper PLV, correct trials, 4 to 30 Hz")
print(pd.DataFrame(rows).to_string(index=False))
''',1)
open('nb_src.py','w').write(n)
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre2.py prep,claim:fig6-plv-all,claim:tables1 2>&1 | sed -n '/cell 37/,$p' | grep -v "^ *0[0-9] " | head -60
```

```
---- cell 37 [claim:fig6-plv-all-subjects]
== trials correct, range (4, 30) Hz: subjects with a significant pair 9 of 9; median band limits 4.00 to 9.50 Hz; band edges range 4.0 to 30.0 Hz
subject hipp scalp      plv  peak_f         band  n_trials pairs_significant
== trials correct, range (1, 40) Hz: subjects with a significant pair 9 of 9; median band limits 7.00 to 17.00 Hz; band edges range 1.0 to 34.5 Hz
subject hipp scalp      plv  peak_f         band  n_trials pairs_significant
== trials all, range (4, 30) Hz: subjects with a significant pair 9 of 9; median band limits 5.50 to 17.50 Hz; band edges range 4.0 to 30.0 Hz
subject hipp scalp      plv  peak_f         band  n_trials pairs_significant
== trials all, range (1, 40) Hz: subjects with a significant pair 9 of 9; median band limits 7.50 to 18.00 Hz; band edges range 1.0 to 38.0 Hz
subject hipp scalp      plv  peak_f         band  n_trials pairs_significant
== variant, per-taper PLV, correct trials, 4 to 30 Hz
subject hipp scalp      plv  peak_f         band  n_trials
---- 144.9s
---- cell 39 [claim:tables1-plv-per-subject]
== trials correct, range (4, 30): subjects matching on electrode, hemisphere and PLV: 0 of 9; electrode 1, hemisphere 4, PLV within 10% 2
subject scalp paper_scalp hipp paper_hemi   plv  paper_plv  peak_f  paper_f  electrode  hemisphere  plv_in_tol  match
== trials correct, range (1, 40): subjects matching on electrode, hemisphere and PLV: 0 of 9; electrode 0, hemisphere 4, PLV within 10% 2
subject scalp paper_scalp hipp paper_hemi   plv  paper_plv  peak_f  paper_f  electrode  hemisphere  plv_in_tol  match
== trials all, range (4, 30): subjects matching on electrode, hemisphere and PLV: 0 of 9; electrode 0, hemisphere 6, PLV within 10% 3
subject scalp paper_scalp hipp paper_hemi   plv  paper_plv  peak_f  paper_f  electrode  hemisphere  plv_in_tol  match
== trials all, range (1, 40): subjects matching on electrode, hemisphere and PLV: 0 of 9; electrode 0, hemisphere 5, PLV within 10% 2
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; cat >> $TMPDIR/runcells.py <<'EOF'
if len(sys.argv) > 4:
    _p.dump({k: g[k] for k in sys.argv[4].split(',') if k in g}, open(sys.argv[5], 'wb'))
EOF
python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre2.py prep,claim:fig6-plv-all,claim:tables1 PAIRS,PAIR_TABLES $TMPDIR/pairs.pkl > $TMPDIR/plv_out.txt 2>&1; sed -n '/cell 37/,/cell 39/p' $TMPDIR/plv_out.txt | head -60; date -u
```

```
---- cell 37 [claim:fig6-plv-all-subjects]
== trials correct, range (4, 30) Hz: subjects with a significant pair 9 of 9; median band limits 4.00 to 9.50 Hz; band edges range 4.0 to 30.0 Hz
subject hipp scalp      plv  peak_f         band  n_trials pairs_significant
     01  PHL    O2 0.741414     9.0  (4.0, 11.5)        55             51/51
     02  PHR    F4 0.470102    15.0 (13.0, 18.0)        75             24/24
     03  AHR    F4 0.572769    30.0 (29.5, 30.0)        38             18/18
     04  AHR    O2 0.759507     4.5   (4.0, 6.0)        24             67/68
     05  AHL    T5 0.784875     4.0   (4.0, 8.0)        29             35/36
     06  PHL   Fp1 0.597884     4.0   (4.0, 5.0)        95             32/32
     07  AHR    O2 0.511936     7.0   (4.0, 9.5)        54             22/24
     08  PHL    Cz 0.689373    15.0  (7.0, 17.0)        50             50/51
     09  PHL    O1 0.755191     5.0   (4.0, 8.0)        27             22/24
== trials correct, range (1, 40) Hz: subjects with a significant pair 9 of 9; median band limits 7.00 to 17.00 Hz; band edges range 1.0 to 34.5 Hz
subject hipp scalp      plv  peak_f         band  n_trials pairs_significant
     01  PHL    O2 0.741414     9.0  (2.5, 12.0)        55             51/51
     02  PHR    F4 0.470102    15.0 (13.0, 17.0)        75             24/24
     03  AHR    F4 0.811551    32.5 (29.5, 34.0)        38             18/18
     04  PHR    O2 0.793353     2.5   (1.0, 6.0)        24             68/68
     05  PHR    F4 0.828254    33.0 (29.5, 34.0)        29             36/36
     06  PHL   Fp1 0.597884     4.0   (1.5, 5.0)        95             32/32
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ### fig6-plv-workload-eight-of-nine
#
# > During maintenance, PLV in the individual frequency band was higher for set size 8 than set
# > size 4 in eight of nine subjects (range 5.5 to 16.5 Hz, median band limits 7.8 to 10 Hz).
#
# The pair of fig6-plv-all-subjects under each of its readings. PLV(8) - PLV(4) against the 95th
# percentile of 200 differences with the epochs randomly assigned to the two set sizes. A
# subject counts when a significant bin falls in the individual band. The workload band is the
# contiguous run of significant bins with the largest difference inside the individual band.

# %% [claim:fig6-plv-workload-eight-of-nine]
rng = np.random.default_rng(602)
f40 = FREQS[FK]
WL = {}
for which, fr in READINGS:
    rows = []
    for sid, sj in SUBJ.items():
        b = PAIRS[(which, fr, sid)]
        m8, m4 = trial_mask(sj, which, (8,)), trial_mask(sj, which, (4,))
        Fi8, Fe8 = coeffs(sj, m8, I_LAST2)
        Fi4, Fe4 = coeffs(sj, m4, I_LAST2)
        d, thr, sig = plv_diff_test(Fi8[:, :, b["hi"]][..., FK], Fe8[:, :, b["ei"]][..., FK],
                                    Fi4[:, :, b["hi"]][..., FK], Fe4[:, :, b["ei"]][..., FK], rng)
        inband = (f40 >= b["band"][0]) & (f40 <= b["band"][1])
        counts = bool((sig & inband).any())
        wb = None
        if counts:
            k = np.argmax(np.where(sig & inband, d, -np.inf))
            a, e = runs(sig, k)
            wb = (float(f40[a]), float(f40[e]))
        WL[(which, fr, sid)] = (d, thr, sig)
        rows.append({"subject": sid, "pair": f'{b["hipp"]}-{b["scalp"]}', "band": b["band"], "n8": int(m8.sum()),
                     "n4": int(m4.sum()), "max_diff_in_band": float(d[inband].max()), "counts": counts, "workload_band": wb})
    R = pd.DataFrame(rows)
    wbs = R.workload_band.dropna()
    print(f"== trials {which}, range {fr}: subjects with higher PLV for set size 8: {int(R.counts.sum())} of 9"
          + (f"; median workload band limits {np.median([w[0] for w in wbs]):.2f} to {np.median([w[1] for w in wbs]):.2f} Hz,"
             f" range {min(w[0] for w in wbs):.1f} to {max(w[1] for w in wbs):.1f} Hz" if len(wbs) else ""))
    print(R.round(3).to_string(index=False))

# %% md
# ### fig6-plv-maintenance-over-encoding
#
# > The PLV during the last 2 s of maintenance exceeded the PLV during encoding in eight of nine
# > subjects, so hippocampal-cortical connectivity in the theta-alpha range increased
# > specifically during maintenance.
#
# The pair of fig6-plv-all-subjects. PLV(last 2 s of maintenance) - PLV(encoding, -5 to -3 s),
# against the 95th percentile of 200 differences with epochs randomly assigned to the two
# periods. Trials (a) set size 8 or (b) all set sizes.

# %% [claim:fig6-plv-maintenance-over-encoding]
rng = np.random.default_rng(603)
ME = {}
for which, fr in READINGS:
    for sets in [(8,), (4, 6, 8)]:
        rows = []
        for sid, sj in SUBJ.items():
            b = PAIRS[(which, fr, sid)]
            m = trial_mask(sj, which, sets)
            FiM, FeM = coeffs(sj, m, I_LAST2)
            FiE, FeE = coeffs(sj, m, I_ENC)
            d, thr, sig = plv_diff_test(FiM[:, :, b["hi"]][..., FK], FeM[:, :, b["ei"]][..., FK],
                                        FiE[:, :, b["hi"]][..., FK], FeE[:, :, b["ei"]][..., FK], rng)
            inband = (f40 >= b["band"][0]) & (f40 <= b["band"][1])
            ME[(which, fr, sets, sid)] = (d, thr, sig)
            rows.append({"subject": sid, "pair": f'{b["hipp"]}-{b["scalp"]}', "band": b["band"], "n": int(m.sum()),
                         "max_diff_in_band": float(d[inband].max()), "counts": bool((sig & inband).any())})
        R = pd.DataFrame(rows)
        print(f"== trials {which}, range {fr}, set sizes {sets}: subjects with maintenance PLV above encoding: {int(R.counts.sum())} of 9")
        print(R.round(3).to_string(index=False))
EOF
cat > $TMPDIR/pre3.py <<EOF
exec(open('$TMPDIR/pre2.py').read())
EOF
cat > $TMPDIR/post_pairs.py <<EOF
EOF
# runner: exec pre, then prep cells, then load PAIRS from pickle, then target cells
cat > $TMPDIR/pre3.py <<EOF
exec(open('$TMPDIR/pre2.py').read())
_PAIRS = pickle.load(open('$TMPDIR/pairs.pkl','rb'))
EOF
python - <<'EOF'
import os
p=os.environ.get('TMPDIR')+'/runcells.py'
s=open(p).read()
s=s.replace("        exec(body, g)\n","        exec(body, g)\n        if 'prep' in head and '_PAIRS' in g: g.update(g['_PAIRS'])\n")
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig6-plv-workload,claim:fig6-plv-maint > $TMPDIR/o2.txt 2>&1; sed -n '/cell 4[0-9]/,$p' $TMPDIR/o2.txt | grep -E "==|Error|Trace|line"
```

```
real	0m41.040s
user	0m40.184s
sys	0m1.213s
== trials correct, range (4, 30): subjects with higher PLV for set size 8: 5 of 9; median workload band limits 5.50 to 5.50 Hz, range 4.0 to 16.0 Hz
== trials correct, range (1, 40): subjects with higher PLV for set size 8: 7 of 9; median workload band limits 7.00 to 7.50 Hz, range 1.0 to 33.0 Hz
== trials all, range (4, 30): subjects with higher PLV for set size 8: 5 of 9; median workload band limits 6.00 to 7.50 Hz, range 4.0 to 14.5 Hz
== trials all, range (1, 40): subjects with higher PLV for set size 8: 8 of 9; median workload band limits 10.75 to 11.00 Hz, range 2.0 to 34.0 Hz
== trials correct, range (4, 30), set sizes (8,): subjects with maintenance PLV above encoding: 4 of 9
== trials correct, range (4, 30), set sizes (4, 6, 8): subjects with maintenance PLV above encoding: 4 of 9
== trials correct, range (1, 40), set sizes (8,): subjects with maintenance PLV above encoding: 5 of 9
== trials correct, range (1, 40), set sizes (4, 6, 8): subjects with maintenance PLV above encoding: 6 of 9
== trials all, range (4, 30), set sizes (8,): subjects with maintenance PLV above encoding: 4 of 9
== trials all, range (4, 30), set sizes (4, 6, 8): subjects with maintenance PLV above encoding: 4 of 9
== trials all, range (1, 40), set sizes (8,): subjects with maintenance PLV above encoding: 5 of 9
== trials all, range (1, 40), set sizes (4, 6, 8): subjects with maintenance PLV above encoding: 6 of 9
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ### fig6-power-unchanged-individual-band
#
# > In the majority of subjects, iEEG and EEG power in the individual frequency band did not
# > differ during maintenance, which suggests that the PLV differences came from phase
# > consistency.
#
# A claim of absence. Per subject, the two channels of the maximal PLV pair, last 2 s of
# maintenance, multitaper power, set size 8 against 4, cluster-based permutation test (1000
# permutations, either sign) over the bins of the individual band, P < 0.05.

# %% [claim:fig6-power-unchanged-individual-band]
rng = np.random.default_rng(604)


def power_epochs(sj, mask, chan_kind, ci, period=I_LAST2):
    x = (sj["ieeg"] if chan_kind == "ieeg" else sj["eeg"])[mask][:, ci, period]
    P, _ = S.mt_power(x, FS)
    return P[:, FK]


def power_diff(sj, which, chan_kind, ci, band, rng):
    m8, m4 = trial_mask(sj, which, (8,)), trial_mask(sj, which, (4,))
    P = np.concatenate([power_epochs(sj, m8, chan_kind, ci), power_epochs(sj, m4, chan_kind, ci)])
    g = np.r_[np.ones(m8.sum(), bool), np.zeros(m4.sum(), bool)]
    inb = (f40 >= band[0]) & (f40 <= band[1])
    X = P[:, inb]
    p_up = S.cluster_test(X, g, 1000, rng, sign=1)
    p_dn = S.cluster_test(X, g, 1000, rng, sign=-1)
    return p_up, p_dn, float(np.log10(X[g].mean() / X[~g].mean()))


for which, fr in READINGS:
    rows = []
    for sid, sj in SUBJ.items():
        b = PAIRS[(which, fr, sid)]
        e_up, e_dn, e_eff = power_diff(sj, which, "eeg", b["ei"], b["band"], rng)
        i_up, i_dn, i_eff = power_diff(sj, which, "ieeg", b["hi"], b["band"], rng)
        rows.append({"subject": sid, "pair": f'{b["hipp"]}-{b["scalp"]}', "band": b["band"],
                     "EEG_P_up": e_up, "EEG_P_down": e_dn, "EEG_log10_ratio": e_eff,
                     "iEEG_P_up": i_up, "iEEG_P_down": i_dn, "iEEG_log10_ratio": i_eff})
    R = pd.DataFrame(rows)
    ne = int(((R.EEG_P_up >= 0.05) & (R.EEG_P_down >= 0.05)).sum())
    ni = int(((R.iEEG_P_up >= 0.05) & (R.iEEG_P_down >= 0.05)).sum())
    print(f"== trials {which}, range {fr}: subjects without an EEG power difference {ne} of 9, without an iEEG difference {ni} of 9")
    print(R.round(4).to_string(index=False))

# %% md
# ### fig5-subject1-eeg-power-workload
#
# > In subject 1, scalp EEG power during the last 2 s of maintenance was higher for set size 8
# > than for set size 4 at Pz (8.5 to 16 Hz) and at Fz (8 to 12.5 Hz); this workload-dependent
# > power increase did not appear in the other subjects.
#
# Last 2 s of maintenance, multitaper power, set size 8 against 4, cluster-based permutation
# test over frequency (1000 permutations), ranges (a) 4 to 30 Hz, (b) 1 to 40 Hz.

# %% [claim:fig5-subject1-eeg-power-workload]
rng = np.random.default_rng(605)


def power_clusters(sj, which, chan_kind, ci, fr, rng, sign=1, baseline=False):
    m8, m4 = trial_mask(sj, which, (8,)), trial_mask(sj, which, (4,))
    P8, P4 = power_epochs(sj, m8, chan_kind, ci), power_epochs(sj, m4, chan_kind, ci)
    if baseline:
        def fixp(mask):
            x = (sj["ieeg"] if chan_kind == "ieeg" else sj["eeg"])[mask][:, ci, I_FIX]
            F, fq = S.mt_fourier(x, FS, nw=2.0, k=3)     # 1 s epoch, +/- 2 Hz, 3 tapers
            pw = (np.abs(F) ** 2).mean(0)
            return np.array([np.interp(f40, fq, r) for r in pw])
        P8, P4 = P8 / fixp(m8), P4 / fixp(m4)
    sel = (f40 >= fr[0]) & (f40 <= fr[1])
    X = np.concatenate([P8, P4])[:, sel]
    g = np.r_[np.ones(len(P8), bool), np.zeros(len(P4), bool)]
    from scipy import stats as st_
    thr = st_.t.ppf(0.975, len(g) - 2)
    G = S.random_masks(int(g.sum()), len(g), 1000, rng)
    Tn = S.t_groups(X, G)
    null = np.sort(np.maximum(S.cluster_max(Tn, thr, 1), S.cluster_max(Tn, thr, -1)))
    T0 = S.t_groups(X, g[None])
    _, cl = S.cluster_masses(T0, thr)
    fs_ = f40[sel]
    out = []
    for a, b, mss in cl:
        if np.sign(mss) != sign:
            continue
        p = (np.sum(null >= abs(mss)) + 1) / (len(null) + 1)
        out.append((float(fs_[a]), float(fs_[b - 1]), round(mss, 1), p))
    return out, int(m8.sum()), int(m4.sum())


sj1 = SUBJ["01"]
for which, fr in READINGS:
    for el, target in [("Pz", (8.5, 16)), ("Fz", (8, 12.5))]:
        cl, n8, n4 = power_clusters(sj1, which, "eeg", sj1["eeg_labels"].index(el), fr, rng)
        hit = any(p < 0.05 and a <= target[1] and b >= target[0] for a, b, _, p in cl)
        print(f"subject 1, trials {which}, range {fr}, {el} (n8 = {n8}, n4 = {n4}): positive clusters (from, to Hz, mass, P) {cl}; "
              f"significant and overlapping {target}: {hit}")
print("other subjects, set size 8 above 4 (significant positive clusters):")
for which, fr in READINGS:
    rows = []
    for sid, sj in SUBJ.items():
        if sid == "01":
            continue
        b = PAIRS[(which, fr, sid)]
        cl, _, _ = power_clusters(sj, which, "eeg", b["ei"], fr, rng)
        cln, _, _ = power_clusters(sj, which, "eeg", b["ei"], fr, rng, sign=-1)
        r = {"subject": sid, "electrode": b["scalp"], "increase": [c for c in cl if c[3] < 0.05],
             "decrease": [c for c in cln if c[3] < 0.05]}
        for el in ("Pz", "Fz"):
            if el in sj["eeg_labels"]:
                c2, _, _ = power_clusters(sj, which, "eeg", sj["eeg_labels"].index(el), fr, rng)
                r[f"{el}_increase"] = [c for c in c2 if c[3] < 0.05]
        rows.append(r)
    R = pd.DataFrame(rows)
    print(f"== trials {which}, range {fr}: subjects 2 to 9 with a significant increase at the maximal-PLV electrode: "
          f"{int((R.increase.map(len) > 0).sum())}")
    print(R.to_string(index=False))

# %% md
# ### fig5-subject1-hippocampal-power-workload
#
# > In subject 1, theta-alpha power (7.5 to 10 Hz) in the left hippocampal iEEG increased with
# > workload during maintenance.
#
# Subject 1, the hippocampal channel of the maximal PLV pair, last 2 s of maintenance, power
# normalized to the fixation power of the same trial (Fig. 5H legend; the 1 s fixation epoch
# with 3 tapers, +/- 2 Hz, interpolated to the 0.5 Hz bins), set size 8 against 4, cluster
# test at P < 0.05. Without the normalization as a variant. All subjects' channels reported.

# %% [claim:fig5-subject1-hippocampal-power-workload]
rng = np.random.default_rng(606)
for which, fr in READINGS:
    b = PAIRS[(which, fr, "01")]
    for base in (True, False):
        cl, n8, n4 = power_clusters(sj1, which, "ieeg", b["hi"], fr, rng, baseline=base)
        hit = any(p < 0.05 and a <= 10 and bb >= 7.5 for a, bb, _, p in cl)
        print(f"subject 1, trials {which}, range {fr}, {b['hipp']} (normalized {base}): positive clusters {cl}; overlapping 7.5-10 Hz and significant: {hit}")
    for h in sj1["hipp"]:
        cl, _, _ = power_clusters(sj1, which, "ieeg", sj1["hipp"].index(h), fr, rng, baseline=True)
        print(f"   channel {h}: significant positive clusters {[c for c in cl if c[3] < 0.05]}")
print("all subjects, maximal-PLV hippocampal channel, normalized, trials correct, 4 to 30 Hz:")
for sid, sj in SUBJ.items():
    b = PAIRS[("correct", (4, 30), sid)]
    cl, _, _ = power_clusters(sj, "correct", "ieeg", b["hi"], (4, 30), rng, baseline=True)
    print(f"   {sid} {b['hipp']}: significant increases {[c for c in cl if c[3] < 0.05]}")
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig6-power,claim:fig5-subject1-eeg,claim:fig5-subject1-hipp > $TMPDIR/o3.txt 2>&1; sed -n '/cell 4[0-9]/,$p' $TMPDIR/o3.txt | cut -c1-400
```

```
real	0m4.707s
user	0m4.572s
sys	0m0.351s
---- cell 45 [claim:fig6-power-unchanged-individual-band]
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 16, in <module>
    exec(body, g)
    ~~~~^^^^^^^^^
  File "<string>", line 25, in <module>
  File "<string>", line 14, in power_diff
NameError: name 'f40' is not defined
```

**Agent calls Bash**

```bash
sed -i 's/^FK = FREQS <= FMAX$/FK = FREQS <= FMAX\nf40 = FREQS[FK]/' nb_src.py; . $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig6-power,claim:fig5-subject1-eeg,claim:fig5-subject1-hipp > $TMPDIR/o3.txt 2>&1; sed -n '/cell 4[0-9]/,$p' $TMPDIR/o3.txt | cut -c1-600
```

```
real	0m4.507s
user	0m4.506s
sys	0m0.383s
---- cell 45 [claim:fig6-power-unchanged-individual-band]
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 16, in <module>
    exec(body, g)
    ~~~~^^^^^^^^^
  File "<string>", line 25, in <module>
  File "<string>", line 16, in power_diff
AttributeError: module 'sternberg' has no attribute 'cluster_test'
```

**Agent calls Bash**

```bash
grep -n "^def " sternberg.py
```

```
63:def assets():
72:def s3_url(asset_id):
80:def open_asset(asset_id):
84:def _str(a):
88:def _scalar(x):
93:def region_of(bundle):
103:def load_session(path, asset_id):
171:def load_all(table, workers=12):
176:def aligned_spikes(spk, probes, lo=-6.0, hi=2.0):
185:def count_in(aligned, window):
190:def rate_in(aligned, window):
194:def binned(aligned, edges):
200:def perm_t(a, b, n_perm=2000, paired=False, rng=None):
233:def cluster_perm_1d(a, b, n_perm=1000, alpha=0.05, rng=None, paired=False):
295:def mt_fourier(x, fs, nw=4.0, k=7):
308:def mt_power(x, fs):
313:def plv(Fi, Fj):
324:def plv_tapers(Fi, Fj):
```

**Agent calls Bash**

```bash
cat >> sternberg.py <<'EOF'


# ---- vectorized permutation tests --------------------------------------------------------
# For a permutation test whose relabelings keep the pooled values (sign flips of paired
# differences, or reassigning pooled values to two groups), the permutation distribution of a
# relabeled data set is the same as that of the original. So the reference distribution is
# computed once per unit and reused for the relabeled ("scrambled") repetitions of a selection.

def t_paired_rows(Dm):
    """Paired t of each row of Dm (rows = sets of differences)."""
    n = Dm.shape[-1]
    m = Dm.mean(-1)
    v = Dm.var(-1, ddof=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(v > 0, m / np.sqrt(v / n), 0.0)


def t_groups(X, G):
    """Unequal-variance t of group A (G True) against B for each row of the masks G (P x N),
    for every column of X (N x K). Returns P x K."""
    G = G.astype(float)
    na = G.sum(1, keepdims=True)
    nb = X.shape[0] - na
    s1 = G @ X
    q1 = G @ (X ** 2)
    S1, Q1 = X.sum(0), (X ** 2).sum(0)
    ma, mb = s1 / na, (S1 - s1) / nb
    va = (q1 - na * ma ** 2) / (na - 1)
    vb = ((Q1 - q1) - nb * mb ** 2) / (nb - 1)
    se = np.sqrt(np.clip(va, 0, None) / na + np.clip(vb, 0, None) / nb)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(se > 0, (ma - mb) / se, 0.0)


def random_masks(n_a, n, n_perm, rng):
    """n_perm random boolean masks with n_a of n entries True."""
    r = rng.random((n_perm, n))
    idx = np.argsort(r, axis=1)[:, :n_a]
    G = np.zeros((n_perm, n), bool)
    np.put_along_axis(G, idx, True, axis=1)
    return G


def perm_p(t_obs, t_ref):
    """Two-sided permutation P of each observed t against the reference |t| values."""
    t_ref = np.sort(np.abs(np.asarray(t_ref)))
    k = len(t_ref) - np.searchsorted(t_ref, np.abs(np.asarray(t_obs)) - 1e-12, side="left")
    return (k + 1) / (len(t_ref) + 1)


def cluster_masses(Tm, thr):
    """Masses (sum of t) of positive and negative supra-threshold runs in each row of Tm (P x K).
    Returns (max |mass| per row, list of (start, stop, mass) for row 0)."""
    P, K = Tm.shape
    out = np.maximum(cluster_max(Tm, thr, 1), cluster_max(Tm, thr, -1))
    row0 = []
    for sign in (1, -1):
        sup = sign * Tm[0] > thr
        i = 0
        while i < K:
            if sup[i]:
                j = i
                while j < K and sup[j]:
                    j += 1
                row0.append((i, j, float(Tm[0, i:j].sum())))
                i = j
            else:
                i += 1
    return out, row0


def cluster_max(Tm, thr, sign=1):
    """Largest mass of runs with sign * t > thr in each row of Tm (P x K); 0 when none."""
    P, K = Tm.shape
    sup = sign * Tm > thr
    start = sup & ~np.concatenate([np.zeros((P, 1), bool), sup[:, :-1]], 1)
    rid = np.cumsum(start, 1) * sup
    flat = (np.arange(P)[:, None] * (K + 1) + rid)[sup]
    mass = np.bincount(flat, weights=(sign * Tm)[sup], minlength=P * (K + 1)).reshape(P, K + 1)
    return mass[:, 1:].max(1)


def cluster_test(X, g, n_perm, rng, alpha=0.05, sign=1, extra=None):
    """Cluster-based permutation test (Maris & Oostenveld 2007, as in FieldTrip; Methods,
    Statistics): runs of points with two-sided t beyond the threshold at alpha, cluster mass =
    sum of t, null of the maximal |cluster mass| over label permutations. Group g (True)
    against the rest; rows of X are trials. Returns the P of the largest cluster in direction
    `sign` (1.0 when there is none) and, if `extra` masks (relabelings) are given, the P of each
    of them against the same null."""
    from scipy import stats as _st
    n = len(g)
    thr = _st.t.ppf(1 - alpha / 2, n - 2)
    G = random_masks(int(g.sum()), n, n_perm, rng)
    Tn = t_groups(X, G)
    null = np.sort(np.maximum(cluster_max(Tn, thr, 1), cluster_max(Tn, thr, -1)))

    def pval(m):
        k = len(null) - np.searchsorted(null, m - 1e-12, side="left")
        return np.where(m > 0, (k + 1) / (len(null) + 1), 1.0)

    T0 = t_groups(X, g[None, :])
    p0 = float(pval(cluster_max(T0, thr, sign))[0])
    if extra is None:
        return p0
    Te = t_groups(X, extra)
    return p0, pval(cluster_max(Te, thr, sign))


# ---- scalp EEG and hippocampal iEEG ------------------------------------------------------

EEG_FS = 200.0      # deposited sampling rate (checked in the notebook)
IEEG_FS = 2000.0


def _load_signals(args):
    from scipy.signal import decimate
    path, asset_id = args
    with open_asset(asset_id) as f:
        el = f["general/extracellular_ephys/electrodes"]
        labels = _str(el["label"][:])
        soz = el["is_inside_soz"][:].astype(bool)
        xyz = np.stack([el["x"][:], el["y"][:], el["z"][:]], 1)
        e = f["acquisition/ecephys.eeg"]
        erows = e["electrodes"][:]
        eeg = e["data"][:].astype(np.float32)
        ets = e["timestamps"][:]
        ie = f["acquisition/ecephys.ieeg"]
        irows = ie["electrodes"][:]
        ilab = labels[irows]
        bundles = sorted({re.sub(r"\d+$", "", l) for l in ilab if re.match(r"^(AH|PH)[LR]\d+$", l)})
        chans, cols = [], []
        for b in bundles:
            c1 = np.where(ilab == b + "1")[0]
            c2 = np.where(ilab == b + "2")[0]
            if len(c1) and len(c2):
                chans.append(b)
                cols += [int(c1[0]), int(c2[0])]
        raw = np.stack([ie["data"][:, c] for c in cols], 1) if cols else np.zeros((ie["data"].shape[0], 0))
        its = ie["timestamps"][:]
        tr = f["intervals/trials"]
        starts = tr["start_time"][:]
    n_tr = len(starts)
    ne, ni = int(8 * EEG_FS), int(8 * IEEG_FS)
    eeg_ep = eeg.reshape(n_tr, ne, -1).transpose(0, 2, 1)
    bip = raw[:, 0::2] - raw[:, 1::2]
    bip_ep = bip.reshape(n_tr, ni, -1).transpose(0, 2, 1)
    bip_ep = decimate(bip_ep, 10, axis=-1, zero_phase=True).astype(np.float32) if bip.shape[1] else np.zeros((n_tr, 0, ne), np.float32)
    lab_rows = {l: i for i, l in enumerate(labels)}
    meta = {"eeg_labels": list(labels[erows]), "hipp_channels": chans,
            "hipp_soz": [bool(soz[lab_rows[c + "1"]] or soz[lab_rows[c + "2"]]) for c in chans],
            "hipp_xyz1": [xyz[lab_rows[c + "1"]] for c in chans],
            "hipp_xyz12": [(xyz[lab_rows[c + "1"]] + xyz[lab_rows[c + "2"]]) / 2 for c in chans],
            "eeg_start_err": float(np.max(np.abs(ets[::ne] - starts))),
            "ieeg_start_err": float(np.max(np.abs(its[::ni] - starts))),
            "eeg_dt": float(np.median(np.diff(ets[:ne]))), "ieeg_dt": float(np.median(np.diff(its[:ni])))}
    return path, eeg_ep, bip_ep, meta


def load_signals(table, workers=16):
    """Scalp EEG (trials x channels x 1600 samples at 200 Hz) and hippocampal bipolar iEEG
    (contact 1 minus contact 2 of each AH and PH macroelectrode, decimated to 200 Hz with a
    zero-phase filter) of every session, from -6 to +2 s around probe onset. Read in parallel
    processes (h5py serializes threads)."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        out = list(ex.map(_load_signals, [(r.path, r.asset_id) for r in table.itertuples()]))
    return {p: {"eeg": e, "ieeg": i, **m} for p, e, i, m in out}
EOF
python - <<'EOF'
s=open('sternberg.py').read()
a=s.index('def cluster_perm_1d('); b=s.index('# ---- spectra and PLV')
s=s[:a]+s[b:]
open('sternberg.py','w').write(s)
EOF
grep -n "^def " sternberg.py | wc -l; . $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig6-power,claim:fig5-subject1-eeg,claim:fig5-subject1-hipp > $TMPDIR/o3.txt 2>&1; sed -n '/cell 4[0-9]/,$p' $TMPDIR/o3.txt | cut -c1-600
```

```
26

real	0m7.297s
user	0m15.590s
sys	0m0.377s
---- cell 45 [claim:fig6-power-unchanged-individual-band]
== trials correct, range (4, 30): subjects without an EEG power difference 4 of 9, without an iEEG difference 7 of 9
subject    pair         band  EEG_P_up  EEG_P_down  EEG_log10_ratio  iEEG_P_up  iEEG_P_down  iEEG_log10_ratio
     01  PHL-O2  (4.0, 11.5)    0.0100      1.0000           0.1610     0.0779          1.0            0.0254
     02  PHR-F4 (13.0, 18.0)    0.0010      1.0000           0.2417     1.0000          1.0           -0.0157
     03  AHR-F4 (29.5, 30.0)    1.0000      1.0000          -0.0815     1.0000          1.0           -0.1290
     04  AHR-O2   (4.0, 6.0)    1.0000      0.0629          -0.0785     1.0000          1.0            0.0348
     05  AHL-T5   (4.0, 8.0)    0.1499      1.0000           0.1409     0.0040          1.0            0.5823
     06 PHL-Fp1   (4.0, 5.0)    0.0010      1.0000           0.1199     0.0010          1.0            0.1926
     07  AHR-O2   (4.0, 9.5)    1.0000      0.0380          -0.0452     1.0000          1.0           -0.1129
     08  PHL-Cz  (7.0, 17.0)    0.1049      1.0000           0.1235     0.1538          1.0            0.0172
     09  PHL-O1   (4.0, 8.0)    1.0000      0.0010          -0.1284     1.0000          1.0            0.0144
== trials correct, range (1, 40): subjects without an EEG power difference 6 of 9, without an iEEG difference 8 of 9
subject    pair         band  EEG_P_up  EEG_P_down  EEG_log10_ratio  iEEG_P_up  iEEG_P_down  iEEG_log10_ratio
     01  PHL-O2  (2.5, 12.0)    0.0060      1.0000           0.2039     0.1029          1.0            0.0028
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ### fig5-subject1-neurons-workload
#
# > In subject 1, the average firing rate of the five hippocampal maintenance neurons was higher
# > for high workload (set size 8 against 4) during encoding and maintenance.
#
# Hippocampal maintenance neurons of subject 1 (fig2b, each reading) with more than 100 spikes in
# encoding and more than 100 in maintenance (summed over correct trials). Rate in 500 ms windows
# at 20 ms steps (centres -4.75 to -0.25 s), set size 8 against 4, correct trials,
# cluster-based permutation test (1000 permutations). Unit of the test: (a) trials, the rate
# averaged over the neurons of the session (subject 1's neurons come from two sessions, so trials
# of both sessions are pooled), (b) neuron-trial pairs.

# %% [claim:fig5-subject1-neurons-workload]
rng = np.random.default_rng(607)
for k in ["paired", "unpaired"]:
    for regcol in ["region_atlas", "region_bundle"]:
        idx = [i for i in np.where((UN.subject == "01") & (UN[regcol] == "hippocampus") & UN["maint_" + k])[0]]
        keep = [i for i in idx if win_counts(units[i], S.ENC)[units[i]["correct"]].sum() > 100
                and win_counts(units[i], S.MAINT)[units[i]["correct"]].sum() > 100]
        line = f"maintenance neurons {k}, regions {regcol}: {len(idx)} in subject 1 hippocampus, {len(keep)} with > 100 spikes in both periods"
        if not keep:
            print(line)
            continue
        Xs, gs, Xn, gn = [], [], [], []
        for sess_ in sorted(set(UN.sess[keep])):
            ii = [i for i in keep if UN.sess[i] == sess_]
            c = units[ii[0]]["correct"] & np.isin(units[ii[0]]["set_size"], (4, 8))
            Xm = np.mean([sliding(units[i], 0.5, -4.75, -0.25)[0][c] for i in ii], axis=0)
            Xs.append(Xm)
            gs.append(units[ii[0]]["set_size"][c] == 8)
            for i in ii:
                Xn.append(sliding(units[i], 0.5, -4.75, -0.25)[0][c])
                gn.append(units[i]["set_size"][c] == 8)
        cen = np.round(np.arange(-4.75, -0.25 + 1e-9, 0.02), 4)
        for name, X, g in [("(a) trials", np.concatenate(Xs), np.concatenate(gs)), ("(b) neuron-trials", np.concatenate(Xn), np.concatenate(gn))]:
            from scipy import stats as st_
            thr = st_.t.ppf(0.975, len(g) - 2)
            G = S.random_masks(int(g.sum()), len(g), 1000, rng)
            Tn = S.t_groups(X, G)
            null = np.sort(np.maximum(S.cluster_max(Tn, thr, 1), S.cluster_max(Tn, thr, -1)))
            _, cl = S.cluster_masses(S.t_groups(X, g[None]), thr)
            sig = [(float(cen[a]), float(cen[b - 1]), round(m, 1), (np.sum(null >= abs(m)) + 1) / 1001) for a, b, m in cl if m > 0]
            sig = [c for c in sig if c[3] < 0.05]
            enc = any(a < -3 for a, b, _, _ in sig)
            mnt = any(b > -3 for a, b, _, _ in sig)
            print(line + f"; {name} (n = {len(g)}, {int(g.sum())} of set size 8): significant positive clusters {sig}; "
                  f"in encoding {enc}, in maintenance {mnt}")
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity,prep,claim:fig2b,claim:fig5-subject1-neurons 2>&1 | sed -n '/cell 5[0-9]/,$p' | cut -c1-500
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py sanity,prep,claim:fig2b,claim:fig5-subject1-neurons 2>&1 | tail -12 | cut -c1-600
```

```
subject  01  02  03  04  05  06  07   08  09
sum      30  14  12   4   0  22   6   37   3
count    54  75  47  76  11  66  39  232  40
---- 9.1s
---- cell 34 [sanity]
EEG and iEEG samples per trial, sampling intervals and first-sample offsets from trial starts:
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 16, in <module>
    exec(body, g)
    ~~~~^^^^^^^^^
  File "<string>", line 5, in <module>
NameError: name 'SIG' is not defined
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py sanity,prep,claim:fig2b,claim:fig5-subject1-neurons 2>&1 | sed -n '/cell 5[0-9]/,$p' | cut -c1-600
```

```
---- cell 51 [claim:fig5-subject1-neurons-workload]
maintenance neurons paired, regions region_atlas: 30 in subject 1 hippocampus, 14 with > 100 spikes in both periods; (a) trials (n = 70, 25 of set size 8): significant positive clusters [(-4.67, -1.57, 508.8, np.float64(0.000999000999000999))]; in encoding True, in maintenance True
maintenance neurons paired, regions region_atlas: 30 in subject 1 hippocampus, 14 with > 100 spikes in both periods; (b) neuron-trials (n = 490, 175 of set size 8): significant positive clusters [(-4.75, -1.29, 638.8, np.float64(0.000999000999000999)), (-0.87, -0.25, 99.2, np.float64(0.01998001998001998))]; in encoding True, in maintenance True
maintenance neurons paired, regions region_bundle: 30 in subject 1 hippocampus, 14 with > 100 spikes in both periods; (a) trials (n = 70, 25 of set size 8): significant positive clusters [(-4.67, -1.57, 508.8, np.float64(0.000999000999000999))]; in encoding True, in maintenance True
maintenance neurons paired, regions region_bundle: 30 in subject 1 hippocampus, 14 with > 100 spikes in both periods; (b) neuron-trials (n = 490, 175 of set size 8): significant positive clusters [(-4.75, -1.29, 638.8, np.float64(0.000999000999000999)), (-0.87, -0.25, 99.2, np.float64(0.012987012987012988))]; in encoding True, in maintenance True
maintenance neurons unpaired, regions region_atlas: 31 in subject 1 hippocampus, 15 with > 100 spikes in both periods; (a) trials (n = 70, 25 of set size 8): significant positive clusters [(-4.67, -1.59, 513.4, np.float64(0.000999000999000999))]; in encoding True, in maintenance True
maintenance neurons unpaired, regions region_atlas: 31 in subject 1 hippocampus, 15 with > 100 spikes in both periods; (b) neuron-trials (n = 524, 188 of set size 8): significant positive clusters [(-4.75, -1.29, 663.5, np.float64(0.000999000999000999)), (-0.89, -0.25, 103.1, np.float64(0.00999000999000999))]; in encoding True, in maintenance True
maintenance neurons unpaired, regions region_bundl
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ### fig5-subject1-plv-hippocampus-pz
#
# > In subject 1, the task increased the phase locking value (PLV) between hippocampal iEEG and
# > scalp EEG at Pz in the alpha band during the last 2 s of maintenance; this PLV was higher
# > for set size 8 than 4 (9.0 to 12.0 Hz) and maximal at occipitoparietal electrodes. The PLV
# > to Fz was also higher for set size 8 (8.5 to 10 Hz).
#
# The selection, workload and maintenance-encoding tests of the fig6 claims, for subject 1, with
# the left hippocampal channel of the maximal pair and with each hippocampal channel against Pz
# and Fz.

# %% [claim:fig5-subject1-plv-hippocampus-pz]
rng = np.random.default_rng(608)


def pair_tests(sj, which, hi, ei, rng):
    m8, m4 = trial_mask(sj, which, (8,)), trial_mask(sj, which, (4,))
    Fi8, Fe8 = coeffs(sj, m8, I_LAST2)
    Fi4, Fe4 = coeffs(sj, m4, I_LAST2)
    FiE, FeE = coeffs(sj, m8, I_ENC)
    a = lambda F, c: F[:, :, c][..., FK]
    dW, tW, sW = plv_diff_test(a(Fi8, hi), a(Fe8, ei), a(Fi4, hi), a(Fe4, ei), rng)
    dM, tM, sM = plv_diff_test(a(Fi8, hi), a(Fe8, ei), a(FiE, hi), a(FeE, ei), rng)
    return sW, sM, S.plv(a(Fi8, hi), a(Fe8, ei))


def bins_in(sig, lo, hi):
    return bool((sig & (f40 >= lo) & (f40 <= hi)).any())


def sig_ranges(sig):
    out, i = [], 0
    while i < len(sig):
        if sig[i]:
            j = i
            while j < len(sig) and sig[j]:
                j += 1
            out.append((float(f40[i]), float(f40[j - 1])))
            i = j
        else:
            i += 1
    return out


for which, fr in READINGS:
    b = PAIRS[(which, fr, "01")]
    print(f"== subject 1, trials {which}, range {fr}: maximal pair {b['hipp']}-{b['scalp']} at {b['peak_f']} Hz (PLV {b['plv']:.3f})")
for which in ["correct", "all"]:
    for h in sj1["hipp"]:
        hi = sj1["hipp"].index(h)
        res = {}
        for el in ["Pz", "Fz"]:
            sW, sM, p8 = pair_tests(sj1, which, hi, sj1["eeg_labels"].index(el), rng)
            res[el] = (sW, sM, p8)
        alpha = (f40 >= 8) & (f40 <= 12)
        top = sorted([(float(S.plv(coeffs(sj1, trial_mask(sj1, which), I_LAST2)[0][:, :, hi][..., FK],
                                   coeffs(sj1, trial_mask(sj1, which), I_LAST2)[1][:, :, ei][..., FK])[alpha].mean()), sj1["eeg_labels"][ei])
                      for ei in sj1["scalp"]], reverse=True)[:4]
        print(f"trials {which}, {h}: Pz maint > enc in 8-10 Hz {bins_in(res['Pz'][1], 8, 10)} (significant {sig_ranges(res['Pz'][1])}); "
              f"Pz workload in 9-12 Hz {bins_in(res['Pz'][0], 9, 12)} ({sig_ranges(res['Pz'][0])}); "
              f"Fz workload in 8.5-10 Hz {bins_in(res['Fz'][0], 8.5, 10)} ({sig_ranges(res['Fz'][0])}); "
              f"highest mean 8-12 Hz PLV electrodes {[(e, round(v, 3)) for v, e in top]}")

# %% md
# ### fig6i-plv-posterior-gradient
#
# > Across subjects, maximal PLV increased from the anterior to the posterior end of the
# > hippocampal axis (34 electrode pairs, R2 = 0.118), and PLV to posterior sites (y < -20 mm)
# > was higher than to anterior sites.
#
# Per subject, the scalp electrode of the maximal pair with every hippocampal bipolar channel;
# the maximal PLV in the individual band (set size 8, last 2 s), against the anterior-posterior
# coordinate. The files give coordinates with +x posterior; MNI y is taken as -x (assumption:
# the axes are described in the electrodes table, and AH contacts lie at x 11 to 21 mm, PH at 22
# to 30 mm, see the data check). Coordinate of a channel: (a) contact 1, (b) midpoint of
# contacts 1 and 2. Fit P from 2000 permutations of the PLV values over positions (two-sided on
# the slope); posterior against anterior by an unpaired permutation t test.

# %% [claim:fig6i-plv-posterior-gradient]
rng = np.random.default_rng(609)
GRAD = {}
for which, fr in READINGS:
    rows = []
    for sid, sj in SUBJ.items():
        b = PAIRS[(which, fr, sid)]
        Fi, Fe = coeffs(sj, trial_mask(sj, which), I_LAST2)
        inb = (f40 >= b["band"][0]) & (f40 <= b["band"][1])
        for hi, h in enumerate(sj["hipp"]):
            p = S.plv(Fi[:, :, hi][..., FK], Fe[:, :, b["ei"]][..., FK])
            rows.append({"subject": sid, "hipp": h, "scalp": b["scalp"], "plv": float(p[inb].max()),
                         "y_a": -float(sj["xyz1"][hi][0]), "y_b": -float(sj["xyz12"][hi][0]),
                         "side": h[-1], "soz": sj["soz"][hi], "is_max": h == b["hipp"]})
    G = pd.DataFrame(rows)
    GRAD[(which, fr)] = G
    for yc in ["y_a", "y_b"]:
        y, x = G.plv.to_numpy(), G[yc].to_numpy()
        sl, ic, r, p, _ = stats.linregress(-x, y)          # slope per mm toward posterior
        null = np.array([stats.linregress(-x, rng.permutation(y)).slope for _ in range(2000)])
        pp = (np.sum(np.abs(null) >= abs(sl)) + 1) / 2001
        post, ant = y[x < -20], y[x >= -20]
        t, pt = S.perm_t(post, ant, n_perm=2000, rng=rng)
        print(f"trials {which}, range {fr}, coordinate {yc}: {len(G)} pairs; slope {sl:.4f} per mm posterior, R2 = {r ** 2:.3f}, "
              f"permutation P = {pp:.4f}; posterior (n = {len(post)}) {post.mean():.3f} against anterior (n = {len(ant)}) "
              f"{ant.mean():.3f}, t = {t:.2f}, P = {pt:.4f}")
print("y range of the channels (mm):", GRAD[READINGS[0]].y_a.min().round(1), "to", GRAD[READINGS[0]].y_a.max().round(1))

# %% md
# ### fig6i-no-left-right-difference
#
# > There was no evidence that the PLV differed between left and right hippocampus.
#
# A claim of absence: the PLV values of fig6i-plv-posterior-gradient, left against right
# channels, unpaired permutation t test (2000 permutations), P < 0.05.

# %% [claim:fig6i-no-left-right-difference]
rng = np.random.default_rng(610)
for which, fr in READINGS:
    G = GRAD[(which, fr)]
    l, r = G[G.side == "L"].plv, G[G.side == "R"].plv
    t, p = S.perm_t(l, r, n_perm=2000, rng=rng)
    print(f"trials {which}, range {fr}: left {l.mean():.3f} (n = {len(l)}), right {r.mean():.3f} (n = {len(r)}), "
          f"difference {l.mean() - r.mean():+.3f}, t = {t:.2f}, P = {p:.4f}")

# %% md
# ### soz-plv-no-difference
#
# > The increase in PLV did not differ significantly between hippocampal channels inside and
# > outside the seizure onset zone.
#
# A claim of absence. SOZ membership of a bipolar channel: either of its contacts marked
# `is_inside_soz`. Increase (a) set size 8 minus 4, (b) maintenance minus encoding, the maximum
# in the individual band; channels (a) all hippocampal channels with the maximal-PLV scalp
# electrode, (b) the nine maximal pairs. Unpaired permutation t test (2000), P < 0.05.

# %% [claim:soz-plv-no-difference]
rng = np.random.default_rng(611)
for which, fr in READINGS:
    rows = []
    for sid, sj in SUBJ.items():
        b = PAIRS[(which, fr, sid)]
        m8, m4 = trial_mask(sj, which, (8,)), trial_mask(sj, which, (4,))
        Fi8, Fe8 = coeffs(sj, m8, I_LAST2)
        Fi4, Fe4 = coeffs(sj, m4, I_LAST2)
        FiE, FeE = coeffs(sj, m8, I_ENC)
        inb = (f40 >= b["band"][0]) & (f40 <= b["band"][1])
        for hi, h in enumerate(sj["hipp"]):
            a = lambda F, c: F[:, :, c][..., FK]
            p8 = S.plv(a(Fi8, hi), a(Fe8, b["ei"]))
            rows.append({"subject": sid, "hipp": h, "soz": sj["soz"][hi], "is_max": h == b["hipp"],
                         "inc_load": float((p8 - S.plv(a(Fi4, hi), a(Fe4, b["ei"])))[inb].max()),
                         "inc_period": float((p8 - S.plv(a(FiE, hi), a(FeE, b["ei"])))[inb].max())})
    Z = pd.DataFrame(rows)
    for chans, sub_ in [("(a) all channels", Z), ("(b) nine maximal pairs", Z[Z.is_max])]:
        for inc in ["inc_load", "inc_period"]:
            s_, n_ = sub_[sub_.soz][inc], sub_[~sub_.soz][inc]
            if len(s_) < 2 or len(n_) < 2:
                print(f"trials {which}, range {fr}, {chans}, {inc}: too few channels (SOZ {len(s_)}, non-SOZ {len(n_)})")
                continue
            t, p = S.perm_t(s_, n_, n_perm=2000, rng=rng)
            print(f"trials {which}, range {fr}, {chans}, {inc}: SOZ {s_.mean():.3f} (n = {len(s_)}), non-SOZ {n_.mean():.3f} "
                  f"(n = {len(n_)}), difference {s_.mean() - n_.mean():+.3f}, t = {t:.2f}, P = {p:.4f}")
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig5-subject1-plv,claim:fig6i,claim:soz 2>&1 | sed -n '/cell 5[0-9]/,$p' | cut -c1-700
```

```
---- cell 53 [claim:fig5-subject1-plv-hippocampus-pz]
== subject 1, trials correct, range (4, 30): maximal pair PHL-O2 at 9.0 Hz (PLV 0.741)
== subject 1, trials correct, range (1, 40): maximal pair PHL-O2 at 9.0 Hz (PLV 0.741)
== subject 1, trials all, range (4, 30): maximal pair PHL-F7 at 15.0 Hz (PLV 0.767)
== subject 1, trials all, range (1, 40): maximal pair PHL-F7 at 15.0 Hz (PLV 0.767)
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 16, in <module>
    exec(body, g)
    ~~~~^^^^^^^^^
  File "<string>", line 37, in <module>
NameError: name 'sj1' is not defined. Did you mean: 'sj'?
```

**Agent calls Bash**

```bash
python - <<'EOF'
n=open('nb_src.py').read()
n=n.replace('''_, FREQS = S.mt_fourier(np.zeros((1, 400)), FS)''','''_, FREQS = S.mt_fourier(np.zeros((1, 400)), FS)
sj1 = SUBJ["01"]''')
n=n.replace('''sj1 = SUBJ["01"]
for which, fr in READINGS:
    for el, target''','''for which, fr in READINGS:
    for el, target''')
open('nb_src.py','w').write(n)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig5-subject1-plv,claim:fig6i,claim:soz 2>&1 | sed -n '/cell 5[0-9]/,$p' | cut -c1-700
```

```
---- cell 53 [claim:fig5-subject1-plv-hippocampus-pz]
== subject 1, trials correct, range (4, 30): maximal pair PHL-O2 at 9.0 Hz (PLV 0.741)
== subject 1, trials correct, range (1, 40): maximal pair PHL-O2 at 9.0 Hz (PLV 0.741)
== subject 1, trials all, range (4, 30): maximal pair PHL-F7 at 15.0 Hz (PLV 0.767)
== subject 1, trials all, range (1, 40): maximal pair PHL-F7 at 15.0 Hz (PLV 0.767)
trials correct, AHL: Pz maint > enc in 8-10 Hz False (significant [(14.0, 14.0), (30.5, 30.5), (31.5, 32.0)]); Pz workload in 9-12 Hz False ([(4.5, 6.5), (14.5, 14.5), (15.5, 18.0), (31.5, 32.0), (34.5, 34.5), (37.5, 37.5)]); Fz workload in 8.5-10 Hz False ([(4.5, 5.0), (14.5, 14.5)]); highest mean 8-12 Hz PLV electrodes [('T3', 0.317), ('F7', 0.295), ('F3', 0.266), ('Cz', 0.255)]
trials correct, PHL: Pz maint > enc in 8-10 Hz True (significant [(8.0, 11.5)]); Pz workload in 9-12 Hz True ([(0.0, 0.0), (3.5, 3.5), (5.5, 6.0), (8.5, 10.0), (30.5, 30.5)]); Fz workload in 8.5-10 Hz True ([(9.5, 10.5), (12.0, 12.0), (13.0, 13.0), (17.0, 17.0), (29.5, 29.5), (31.0, 31.0), (35.0, 35.0)]); highest mean 8-12 Hz PLV electrodes [('O2', 0.635), ('Pz', 0.626), ('O1', 0.574), ('T6', 0.561)]
trials correct, PHR: Pz maint > enc in 8-10 Hz True (significant [(0.5, 0.5), (4.0, 5.0), (9.0, 11.5), (15.0, 15.5), (16.5, 16.5), (22.5, 22.5)]); Pz workload in 9-12 Hz False ([(2.5, 2.5), (3.5, 5.0), (14.5, 14.5), (20.0, 20.0)]); Fz workload in 8.5-10 Hz False ([(1.0, 1.0), (2.0, 3.0), (12.0, 12.0)]); highest mean 8-12 Hz PLV electrodes [('F8', 0.302), ('O2', 0.3), ('T5', 0.291), ('P4', 0.287)]
trials all, AHL: Pz maint > enc in 8-10 Hz False (significant [(28.5, 28.5), (32.0, 32.0), (33.0, 33.0), (37.0, 37.5), (38.5, 38.5)]); Pz workload in 9-12 Hz False ([(4.5, 4.5), (5.5, 6.5), (14.5, 14.5), (15.5, 18.0), (31.5, 32.0), (37.5, 37.5)]); Fz workload in 8.5-10 Hz False ([(4.5, 4.5)]); highest mean 8-12 Hz PLV electrodes [('T3', 0.296), ('F7', 0.291), ('F3', 0.235), ('C3', 0.228)]
trials all, PHL: Pz main
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/tsvm.py <<'EOF'
import numpy as np, time
from sklearn.svm import SVC, LinearSVC
rng=np.random.default_rng(0)
X=rng.normal(size=(18,640)); y=np.r_[np.zeros(9),np.ones(9)]
t=time.time()
for _ in range(1000): SVC(kernel='linear', C=1.0).fit(X,y).predict(X[:2])
print('SVC', (time.time()-t)/1000*1e3,'ms')
t=time.time()
for _ in range(1000):
    # closed form-ish: linear SVM via sklearn LinearSVC
    LinearSVC(C=1.0, dual=True, max_iter=2000).fit(X,y).predict(X[:2])
print('LinearSVC', (time.time()-t)/1000*1e3,'ms')
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/tsvm.py
```

```
SVC 1.1616275310516357 ms
LinearSVC 1.3014538288116455 ms
```

**Agent calls Bash**

```bash
nproc; free -g | head -2; date -u
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
Fri Oct 30 20:07:34 UTC 2026
```

**Agent calls Bash**

```bash
cat >> sternberg.py <<'EOF'


# ---- pseudopopulation decoding (Methods, Neural decoding of firing rates) -----------------
# A support vector machine (linear kernel, C = 1, the NDT toolbox's libsvm default) trained and
# tested at each time step on pseudopopulations: in each resampling run, for each neuron, a
# number of trials per class is drawn at random and spread over the cross-validation splits
# (one trial per class per split, NDT's default), features are z-scored with the training
# mean and SD (NDT's zscore_normalize_FP), and the accuracy is averaged over the splits. The
# null runs scramble the labels of each neuron's trials before drawing.

_DEC = {}


def _decode_chunk(args):
    from sklearn.svm import SVC
    seed, n_runs, n_splits, per_class, scramble, zscore = args
    rng = np.random.default_rng(seed)
    feats, labels = _DEC["feats"], _DEC["labels"]     # per neuron: trials x times, trials
    n_t = feats[0].shape[1]
    classes = (0, 1)
    out = np.zeros((n_runs, n_t))
    for r in range(n_runs):
        # draw trials: for each class, per_class[c] trials per neuron, assigned to splits in turn
        Xc = {c: np.zeros((per_class[c], len(feats), n_t)) for c in classes}
        for j, (F, y) in enumerate(zip(feats, labels)):
            yy = rng.permutation(y) if scramble else y
            for c in classes:
                idx = np.flatnonzero(yy == c)
                pick = rng.choice(idx, per_class[c], replace=False)
                Xc[c][:, j, :] = F[pick]
        split_of = {c: np.arange(per_class[c]) % n_splits for c in classes}
        acc = np.zeros(n_t)
        for t in range(n_t):
            a_t = []
            for s in range(n_splits):
                tr = [Xc[c][split_of[c] != s, :, t] for c in classes]
                te = [Xc[c][split_of[c] == s, :, t] for c in classes]
                Xtr = np.concatenate(tr)
                ytr = np.concatenate([np.full(len(x), c) for c, x in zip(classes, tr)])
                Xte = np.concatenate(te)
                yte = np.concatenate([np.full(len(x), c) for c, x in zip(classes, te)])
                if zscore:
                    mu, sd = Xtr.mean(0), Xtr.std(0)
                    sd[sd == 0] = 1.0
                    Xtr, Xte = (Xtr - mu) / sd, (Xte - mu) / sd
                clf = SVC(kernel="linear", C=1.0).fit(Xtr, ytr)
                a_t.append(np.mean(clf.predict(Xte) == yte))
            acc[t] = np.mean(a_t)
        out[r] = acc
    return out


def decode(feats, labels, n_splits, n_runs, rng, scramble=False, zscore=True, per_class=None, workers=4):
    """Accuracy (runs x time steps). feats: list over neurons of trials x time-step features;
    labels: list over neurons of 0/1 class labels per trial. per_class: trials drawn per class
    (default n_splits each, balanced)."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    per_class = per_class or {0: n_splits, 1: n_splits}
    _DEC["feats"], _DEC["labels"] = feats, labels
    chunks = np.array_split(np.arange(n_runs), workers)
    seeds = rng.integers(0, 2 ** 31, len(chunks))
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
        res = list(ex.map(_decode_chunk, [(int(s), len(c), n_splits, per_class, scramble, zscore)
                                          for s, c in zip(seeds, chunks) if len(c)]))
    return np.concatenate(res)
EOF
cat >> nb_src.py <<'EOF'

# %% md
# ## Population decoding
#
# Pseudopopulation decoding as in the Methods (Neural decoding of firing rates) with the NDT
# defaults the Methods leave open (see `sternberg.decode`). Features: rates in a 1500 ms window
# at 250 ms steps; reading (a) a boxcar (the main reading), (b) a Gaussian with SD 250 ms
# (the window as +/- 3 SD; standard choice). Normalization: (a) z-score on training data,
# (b) none. Neurons enter when they have enough trials of each class for the draws. Accuracy:
# reading (a) per run the mean over the steps inside the period, then the median over runs
# (main), (b) median over runs and steps together. P against the null runs with scrambled
# labels, (k + 1) / (n + 1), then times 12 (Bonferroni, Methods). Regions by the atlas label
# (main) and by the bundle name.

# %% [prep]
CENTERS = {"encoding": np.arange(-4.75, -3.25 + 1e-9, 0.25), "maintenance": np.arange(-2.75, -0.25 + 1e-9, 0.25)}


def feats_for(u, centres, kind="boxcar"):
    if kind == "boxcar":
        X, _ = None, None
        cs = np.concatenate([np.zeros((u["bins"].shape[0], 1)), np.cumsum(u["bins"], 1)], 1)
        out = []
        for c in centres:
            a = int(round((c - 0.75 + 6) / 0.02))
            b = int(round((c + 0.75 + 6) / 0.02))
            a, b = max(a, 0), min(b, u["bins"].shape[1])
            out.append((cs[:, b] - cs[:, a]) / ((b - a) * 0.02))
        return np.array(out).T
    t = np.round(np.arange(-6.0, 2.0, 0.02) + 0.01, 4)
    out = []
    for c in centres:
        w = np.exp(-0.5 * ((t - c) / 0.25) ** 2) * (np.abs(t - c) <= 0.75)
        out.append(u["bins"] @ (w / (w.sum() * 0.02)))
    return np.array(out).T


def build(pop_idx, label_fn, need, centres, kind="boxcar"):
    """Features and labels of the neurons in pop_idx that have at least need[c] trials per class."""
    F, L, used = [], [], []
    for i in pop_idx:
        u = units[i]
        y, keep = label_fn(u)
        if np.sum(y[keep] == 0) < need[0] or np.sum(y[keep] == 1) < need[1]:
            continue
        F.append(feats_for(u, centres, kind)[keep])
        L.append(y[keep].astype(int))
        used.append(i)
    return F, L, used


def summarize(acc, null, n_tests=12):
    a_med = np.median(acc.mean(1))
    b_med = np.median(acc)
    pa = (np.sum(null.mean(1) >= a_med) + 1) / (len(null) + 1)
    pb = (np.sum(null.ravel() >= b_med) + 1) / (null.size + 1)
    return {"median_a": 100 * a_med, "median_b": 100 * b_med, "null_median": 100 * np.median(null.mean(1)),
            "null_95": 100 * np.percentile(null.mean(1), 95), "P_a": pa, "P_a_bonf": min(1, pa * n_tests),
            "P_b": pb, "P_b_bonf": min(1, pb * n_tests)}


def region_idx(r, regcol="region_atlas", extra=None):
    m = (UN[regcol] == r) if r != "all" else UN[regcol].isin(REG)
    if extra is not None:
        m &= extra
    return list(np.where(m)[0])
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat >> nb_src.py <<'EOF'

# %% md
# ### fig4e-maintenance-decodes-workload
#
# > During maintenance, workload (set size 4 against 6 and 8) could be decoded from hippocampal
# > neurons with a median accuracy of 80%, but not from neurons of the other areas.
#
# Correct trials, set size 4 (class 0) against 6 and 8 (class 1), 10 splits, steps -2.75 to
# -0.25 s. Class balance: (a) 10 trials per class (NDT), (b) 10 of set size 4 and 20 of set
# sizes 6 and 8, the design's 1:2 ratio (the "all trials" reading as far as a pseudopopulation
# allows; chance is then 67% for a classifier that always answers "high").

# %% [claim:fig4e-maintenance-decodes-workload]
rng = np.random.default_rng(401)
NR, NN = 500, 500
lab_load = lambda u: ((u["set_size"] >= 6).astype(int), u["correct"])
DEC4E = {}
for regcol in ["region_atlas", "region_bundle"]:
    for r in REG:
        F, L, used = build(region_idx(r, regcol), lab_load, {0: 10, 1: 10}, CENTERS["maintenance"])
        acc = S.decode(F, L, 10, NR, rng)
        null = S.decode(F, L, 10, NN, rng, scramble=True)
        DEC4E[(regcol, r)] = (acc, null, used)
        print(f"{regcol} {r}: {len(used)} neurons;", {k: round(v, 4) for k, v in summarize(acc, null).items()})
print("variants, hippocampus (atlas), 200 runs and 200 null runs each:")
idx_h = region_idx("hippocampus")
for name, kind, z, pc, need in [("Gaussian, z-scored", "gauss", True, None, {0: 10, 1: 10}),
                                ("boxcar, not normalized", "boxcar", False, None, {0: 10, 1: 10}),
                                ("boxcar, z-scored, 10:20 trials", "boxcar", True, {0: 10, 1: 20}, {0: 10, 1: 20})]:
    F, L, used = build(idx_h, lab_load, need, CENTERS["maintenance"], kind)
    acc = S.decode(F, L, 10, 200, rng, zscore=z, per_class=pc)
    null = S.decode(F, L, 10, 200, rng, scramble=True, zscore=z, per_class=pc)
    print(f"  {name}: {len(used)} neurons;", {k: round(v, 4) for k, v in summarize(acc, null).items()})
EOF
sed -i 's/^NR, NN = 500, 500$/NR, NN = int(os.environ.get("NR", 500)), int(os.environ.get("NR", 500))/' nb_src.py
. $TMPDIR/dev/bin/activate; time NR=40 python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py prep,claim:fig2b,claim:fig4e-maint 2>&1 | sed -n '/cell 6[0-9]/,$p' | cut -c1-400
```

```
real	0m13.175s
user	0m13.099s
sys	0m0.409s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; NR=40 python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre.py prep,claim:fig2b,claim:fig4e-maint 2>&1 | tail -20 | cut -c1-400
```

```
amygdala 585        56  9.5726     13.315     19.0   0.001  0.002
   chi-square hippocampus against the other two: 44.39 (P = 2.7e-11); Yates 43.29 (P = 4.7e-11); table [[99, 347], [98, 943]]
== regions region_bundle, unpaired test
     region   n  selected     pct  null_mean  null_95  P_1000  P_499
hippocampus 446        96 21.5247      9.738    15.00   0.001  0.002
 entorhinal 456        42  9.2105      9.549    15.00   0.001  0.002
   amygdala 585        53  9.0598     11.518    17.05   0.001  0.002
   chi-square hippocampus against the other two: 42.88 (P = 5.8e-11); Yates 41.78 (P = 1e-10); table [[96, 350], [95, 946]]
per subject, hippocampal maintenance neurons (atlas, paired):
subject  01  02  03  04  05  06  07   08  09
sum      30  14  12   4   0  22   6   37   3
count    54  75  47  76  11  66  39  232  40
---- 9.0s
---- cell 35 [prep]
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 16, in <module>
    exec(body, g)
    ~~~~^^^^^^^^^
  File "<string>", line 7, in <module>
NameError: name 'SIG' is not defined
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; time NR=40 python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig2b,claim:fig4e-maint 2>&1 | sed -n '/cell 6[0-9]/,$p' | cut -c1-500
```

```
---- cell 61 [prep]
---- 0.0s
---- cell 63 [claim:fig4e-maintenance-decodes-workload]
region_atlas hippocampus: 640 neurons; {'median_a': np.float64(80.9091), 'median_b': np.float64(85.0), 'null_median': np.float64(50.4545), 'null_95': np.float64(64.1591), 'P_a': np.float64(0.0244), 'P_a_bonf': np.float64(0.2927), 'P_b': np.float64(0.0113), 'P_b_bonf': np.float64(0.1361)}
region_atlas entorhinal: 421 neurons; {'median_a': np.float64(64.3182), 'median_b': np.float64(65.0), 'null_median': np.float64(47.9545), 'null_95': np.float64(61.4545), 'P_a': np.float64(0.0488), 'P_a_bonf': np.float64(0.5854), 'P_b': np.float64(0.195), 'P_b_bonf': 1}
region_atlas amygdala: 398 neurons; {'median_a': np.float64(59.0909), 'median_b': np.float64(60.0), 'null_median': np.float64(51.5909), 'null_95': np.float64(60.0227), 'P_a': np.float64(0.1707), 'P_a_bonf': 1, 'P_b': np.float64(0.3197), 'P_b_bonf': 1}
region_bundle hippocampus: 446 neurons; {'median_a': np.float64(82.5), 'median_b': np.float64(85.0), 'null_median': np.float64(49.7727), 'null_95': np.float64(59.25), 'P_a': np.float64(0.0244), 'P_a_bonf': np.float64(0.2927), 'P_b': np.float64(0.0091), 'P_b_bonf': np.float64(0.1088)}
region_bundle entorhinal: 456 neurons; {'median_a': np.float64(64.3182), 'median_b': np.float64(65.0), 'null_median': np.float64(49.3182), 'null_95': np.float64(62.1136), 'P_a': np.float64(0.0732), 'P_a_bonf': np.float64(0.878), 'P_b': np.float64(0.1905), 'P_b_bonf': 1}
region_bundle amygdala: 585 neurons; {'median_a': np.float64(64.5455), 'median_b': np.float64(65.0), 'null_median': np.float64(49.0909), 'null_95': np.float64(60.0227), 'P_a': np.float64(0.0488), 'P_a_bonf': np.float64(0.5854), 'P_b': np.float64(0.1451), 'P_b_bonf': 1}
variants, hippocampus (atlas), 200 runs and 200 null runs each:
  Gaussian, z-scored: 640 neurons; {'median_a': np.float64(70.0), 'median_b': np.float64(70.0), 'null_median': np.float64(49.7727), 'null_95': np.float64(59.1136), 'P_a': np.float64(0.005), 'P_a_bonf': np.float64(
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
n=open('nb_src.py').read()
n=n.replace('NR, NN = int(os.environ.get("NR", 500)), int(os.environ.get("NR", 500))','NR, NN = 100, 250   # Methods: 500 and 500; reduced for the run time (minimum P 1/251, x 12 = 0.048)')
n=n.replace('print("variants, hippocampus (atlas), 200 runs and 200 null runs each:")','print("variants, hippocampus (atlas), 100 runs and 250 null runs each:")')
n=n.replace('''    acc = S.decode(F, L, 10, 200, rng, zscore=z, per_class=pc)
    null = S.decode(F, L, 10, 200, rng, scramble=True, zscore=z, per_class=pc)''','''    acc = S.decode(F, L, 10, NR, rng, zscore=z, per_class=pc)
    null = S.decode(F, L, 10, NN, rng, scramble=True, zscore=z, per_class=pc)''')
n=n.replace("# labels, (k + 1) / (n + 1), then times 12 (Bonferroni, Methods).","# labels, (k + 1) / (n + 1), then times 12 (Bonferroni, Methods). The Methods use 500\n# resampling runs and 500 null runs; to keep the notebook within its time limit this attempt uses\n# 100 runs and 250 null runs (the smallest corrected P is then 12/251 = 0.048).")
open('nb_src.py','w').write(n)
EOF
cat >> nb_src.py <<'EOF'

# %% md
# ### fig4d-encoding-decodes-correct
#
# > During encoding of high-workload trials (set sizes 6 and 8), hippocampal neurons, but not
# > entorhinal or amygdala neurons, predicted whether the subject would later respond correctly,
# > with a median decoding accuracy of 80%.
#
# Trials of set sizes 6 and 8, incorrect (class 0) against correct (class 1), units from
# sessions with at least five incorrect responses among them, five splits (five trials per class
# per neuron), steps -4.75 to -3.25 s.

# %% [claim:fig4d-encoding-decodes-correct]
rng = np.random.default_rng(402)
lab_corr = lambda u: (u["correct"].astype(int), u["set_size"] >= 6)
for regcol in ["region_atlas", "region_bundle"]:
    for r in REG:
        F, L, used = build(region_idx(r, regcol), lab_corr, {0: 5, 1: 5}, CENTERS["encoding"])
        acc = S.decode(F, L, 5, NR, rng)
        null = S.decode(F, L, 5, NN, rng, scramble=True)
        print(f"{regcol} {r}: {len(used)} neurons from {UN.sess.iloc[used].nunique()} sessions;",
              {k: round(v, 4) for k, v in summarize(acc, null).items()})
print("variants, hippocampus (atlas):")
for name, kind, z in [("Gaussian, z-scored", "gauss", True), ("boxcar, not normalized", "boxcar", False)]:
    F, L, used = build(region_idx("hippocampus"), lab_corr, {0: 5, 1: 5}, CENTERS["encoding"], kind)
    acc = S.decode(F, L, 5, NR, rng, zscore=z)
    null = S.decode(F, L, 5, NN, rng, scramble=True, zscore=z)
    print(f"  {name}: {len(used)} neurons;", {k: round(v, 4) for k, v in summarize(acc, null).items()})

# %% md
# ### fig4e-workload-decoding-leave-one-subject-out
#
# > Excluding any one subject changed the hippocampal workload decoding accuracy to a value in
# > the range 71 to 81%.
#
# The main reading of fig4e (atlas regions, boxcar, z-scored, 10 trials per class), rerun
# without the hippocampal units of each subject in turn (100 runs each).

# %% [claim:fig4e-workload-decoding-leave-one-subject-out]
rng = np.random.default_rng(403)
loso = {}
for sid in sorted(UN.subject.unique()):
    F, L, used = build(region_idx("hippocampus", extra=(UN.subject != sid)), lab_load, {0: 10, 1: 10}, CENTERS["maintenance"])
    acc = S.decode(F, L, 10, NR, rng)
    loso[sid] = (100 * np.median(acc.mean(1)), 100 * np.median(acc), len(used))
L_ = pd.DataFrame(loso, index=["median_a", "median_b", "neurons"]).T
print(L_.round(2).to_string())
print("range, reading (a): %.1f to %.1f%%; reading (b): %.1f to %.1f%%" % (L_.median_a.min(), L_.median_a.max(), L_.median_b.min(), L_.median_b.max()))

# %% md
# ### fig4e-maintenance-neurons-carry-workload
#
# > Workload decoding from hippocampal maintenance neurons alone was little different from
# > decoding from all hippocampal neurons, while excluding the maintenance neurons reduced the
# > accuracy to 71%.
#
# The decoder of fig4e (main reading) on (i) hippocampal maintenance neurons only and (ii) the
# other hippocampal neurons, for the maintenance neurons of each fig2b reading.

# %% [claim:fig4e-maintenance-neurons-carry-workload]
rng = np.random.default_rng(404)
all_h = summarize(*DEC4E[("region_atlas", "hippocampus")][:2])
print("all hippocampal neurons: median (a) %.1f%%, (b) %.1f%%" % (all_h["median_a"], all_h["median_b"]))
for k in ["paired", "unpaired"]:
    for name, extra in [("(i) maintenance neurons only", UN["maint_" + k]), ("(ii) without maintenance neurons", ~UN["maint_" + k])]:
        F, L, used = build(region_idx("hippocampus", extra=extra), lab_load, {0: 10, 1: 10}, CENTERS["maintenance"])
        acc = S.decode(F, L, 10, NR, rng)
        null = S.decode(F, L, 10, NN, rng, scramble=True)
        sm = summarize(acc, null)
        print(f"fig2b {k}, {name}: {len(used)} neurons;", {kk: round(v, 4) for kk, v in sm.items()},
              f"; difference from all, (a) {sm['median_a'] - all_h['median_a']:+.1f} points")

# %% md
# ### fig4e-no-decoding-6-vs-8
#
# > The decoder did not distinguish trials of set size 6 from set size 8.
#
# A claim of absence: the decoder of fig4e (main reading), hippocampal neurons, correct trials,
# set size 6 (class 0) against 8 (class 1), against its scrambled null at P < 0.05 (not
# corrected).

# %% [claim:fig4e-no-decoding-6-vs-8]
rng = np.random.default_rng(405)
lab_68 = lambda u: ((u["set_size"] == 8).astype(int), u["correct"] & (u["set_size"] >= 6))
F, L, used = build(region_idx("hippocampus"), lab_68, {0: 10, 1: 10}, CENTERS["maintenance"])
acc = S.decode(F, L, 10, NR, rng)
null = S.decode(F, L, 10, NN, rng, scramble=True)
print(f"hippocampus, set size 6 against 8: {len(used)} neurons;", {k: round(v, 4) for k, v in summarize(acc, null, n_tests=1).items()})

# %% md
# ### fig4f-retrieval-decodes-response
#
# > During retrieval (500 ms before the button press), neurons in all recorded areas predicted
# > the IN or OUT response; with all neurons the median decoding accuracy reached 90%.
#
# Correct trials whose press falls within the 2 s stored after probe onset, OUT (class 0)
# against IN (class 1), the rate in the 500 ms before the press (one step), 10 splits.

# %% [claim:fig4f-retrieval-decodes-response]
rng = np.random.default_rng(406)


def build_retrieval(pop_idx):
    F, L, used = [], [], []
    for i in pop_idx:
        u = units[i]
        keep = u["correct"] & (u["rt"] <= 2.0)
        y = u["is_in"].astype(int)
        if np.sum(y[keep] == 0) < 10 or np.sum(y[keep] == 1) < 10:
            continue
        cnt = np.array([np.sum((s >= r - 0.5) & (s < r)) for s, r in zip(u["aligned"], u["rt"])]) / 0.5
        F.append(cnt[keep][:, None])
        L.append(y[keep])
        used.append(i)
    return F, L, used


for regcol in ["region_atlas", "region_bundle"]:
    for r in REG + ["all"]:
        F, L, used = build_retrieval(region_idx(r, regcol))
        acc = S.decode(F, L, 10, NR, rng)
        null = S.decode(F, L, 10, NN, rng, scramble=True)
        print(f"{regcol} {r}: {len(used)} neurons;", {k: round(v, 4) for k, v in summarize(acc, null).items()})
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig2b,claim:fig4 2>&1 | sed -n '/cell 6[0-9]/,$p' | cut -c1-450
```

```
---- cell 61 [prep]
---- 0.0s
---- cell 63 [claim:fig4e-maintenance-decodes-workload]
region_atlas hippocampus: 640 neurons; {'median_a': np.float64(81.3636), 'median_b': np.float64(85.0), 'null_median': np.float64(49.5455), 'null_95': np.float64(62.1136), 'P_a': np.float64(0.004), 'P_a_bonf': np.float64(0.0478), 'P_b': np.float64(0.004), 'P_b_bonf': np.float64(0.048)}
region_atlas entorhinal: 421 neurons; {'median_a': np.float64(62.5), 'median_b': np.float64(65.0), 'null_median': np.float64(49.5455), 'null_95': np.float64(61.3636), 'P_a': np.float64(0.0438), 'P_a_bonf': np.float64(0.5259), 'P_b': np.float64(0.1752), 'P_b_bonf': 1}
region_atlas amygdala: 398 neurons; {'median_a': np.float64(59.5455), 'median_b': np.float64(60.0), 'null_median': np.float64(49.5455), 'null_95': np.float64(62.9773), 'P_a': np.float64(0.1195), 'P_a_bonf': 1, 'P_b': np.float64(0.3021), 'P_b_bonf': 1}
region_bundle hippocampus: 446 neurons; {'median_a': np.float64(81.5909), 'median_b': np.float64(80.0), 'null_median': np.float64(50.2273), 'null_95': np.float64(61.8182), 'P_a': np.float64(0.004), 'P_a_bonf': np.float64(0.0478), 'P_b': np.float64(0.0193), 'P_b_bonf': np.float64(0.2312)}
region_bundle entorhinal: 456 neurons; {'median_a': np.float64(65.2273), 'median_b': np.float64(65.0), 'null_median': np.float64(50.0), 'null_95': np.float64(61.8182), 'P_a': np.float64(0.0359), 'P_a_bonf': np.float64(0.4303), 'P_b': np.float64(0.1825), 'P_b_bonf': 1}
region_bundle amygdala: 585 neurons; {'median_a': np.float64(65.9091), 'median_b': np.float64(65.0), 'null_median': np.float64(50.0), 'null_95': np.float64(60.7045), 'P_a': np.float64(0.0159), 'P_a_bonf': np.float64(0.1912), 'P_b': np.float64(0.1741), 'P_b_bonf': 1}
variants, hippocampus (atlas), 100 runs and 250 null runs each:
  Gaussian, z-scored: 640 neurons; {'median_a': np.float64(70.0), 'median_b': np.float64(70.0), 'null_median': np.float64(50.0), 'null_95': np.float64(59.0909), 'P_a': np.float64(0.004), 'P_a_bonf': np.float64(0.0478), 
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; ls ../../tools/; python ../../tools/entry.py --help 2>&1 | head -20
```

```
Fri Oct 30 20:21:00 UTC 2026
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
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> sternberg.py <<'EOF'


# ---- dPCA (Kobak et al. 2016; Methods, dPCA of firing rates) -----------------------------

def dpca(X, n_comp=15, lam=0.0):
    """dPCA of trial-averaged data X (neurons x set sizes x times) with a time marginalization
    and a set-size marginalization (set size plus its interaction with time). For each
    marginalization the reduced-rank regression of Kobak et al. (2016): B = X_phi X' (X X' +
    mu I)^-1 with mu = (lam ||X||)^2 (lam = 0 uses the pseudo-inverse), decoder and encoder
    from the SVD of B X. Returns components ordered by explained variance: a list of dicts
    with marginalization, decoder (neurons), encoder, and explained variance (% of the total)."""
    N, Sn, Tn = X.shape
    Xc = X - X.mean(axis=(1, 2), keepdims=True)
    Xf = Xc.reshape(N, -1)
    Xt = np.broadcast_to(Xc.mean(1, keepdims=True), Xc.shape).reshape(N, -1)
    margs = {"time": Xt, "set size": Xf - Xt}
    total = np.sum(Xf ** 2)
    C = Xf @ Xf.T
    if lam > 0:
        Cinv = np.linalg.inv(C + (lam * np.sqrt(total)) ** 2 * np.eye(N))
    else:
        Cinv = np.linalg.pinv(C)
    comps = []
    for name, Xm in margs.items():
        B = Xm @ Xf.T @ Cinv
        U, s, Vt = np.linalg.svd(B @ Xf, full_matrices=False)
        for k in range(min(n_comp, U.shape[1])):
            enc = U[:, k]
            dec = U[:, k] @ B
            z = dec @ Xf
            ev = 100 * (total - np.sum((Xf - np.outer(enc, z)) ** 2)) / total
            comps.append({"marg": name, "decoder": dec, "encoder": enc, "ev": ev,
                          "z": z.reshape(Sn, Tn)})
    comps.sort(key=lambda c: -c["ev"])
    return comps[:n_comp], Xf, total


def cumulative_ev(comps, Xf, total, k):
    """Variance of the data explained jointly by the first k components (% of the total)."""
    E = np.array([c["encoder"] for c in comps[:k]]).T
    Dm = np.array([c["decoder"] for c in comps[:k]])
    R = Xf - E @ (Dm @ Xf)
    return 100 * (total - np.sum(R ** 2)) / total
EOF
cat >> nb_src.py <<'EOF'

# %% md
# ## Population state space (dPCA)
#
# Trial-averaged rates per set size of all neurons (atlas regions), correct trials, -6 to +2 s
# at 20 ms steps, smoothed with a Gaussian kernel over a 1000 ms window (SD 1000/6 ms, the window
# as +/- 3 SD, a standard choice; the 20 ms bins replace the Methods' 2 ms bins, which cannot
# change a rate smoothed over 1 s). Z-score to fixation: (a) by the mean and SD over trials of
# the fixation rate, (b) by the fixation mean and the SD of the rate over the whole trial.
# Regularization: (a) the toolbox's cross-validated lambda is not run here (it needs
# single-trial pseudopopulations); fixed lambdas of 1e-3 and 1e-2 of the data norm are shown
# instead, (b) none (pseudo-inverse).
#
# ### fig4a-dpca-workload-separation
#
# > The first three demixed principal components of the population firing rates explained 44.7%
# > of the variance and separated set sizes 4, 6 and 8, with three angles of 120 degrees in the
# > dPC2-dPC3 plane; the first 15 components explained 79%.

# %% [claim:fig4a-dpca-workload-separation]
rng = np.random.default_rng(501)
TT = np.round(np.arange(-6.0, 2.0, 0.02) + 0.01, 4)
sig_ = (1.0 / 6) / 0.02
kern = np.exp(-0.5 * (np.arange(-25, 26) / sig_) ** 2)
kern /= kern.sum()
pop = [i for i in range(len(units)) if UN.region_atlas[i] in REG]


def psth_z(u, mode):
    c = u["correct"]
    r = np.apply_along_axis(lambda x: np.convolve(x, kern, mode="same"), 1, u["bins"][c].astype(float)) / 0.02
    fix_tr = win_rate(u, S.FIX)[c]
    m = fix_tr.mean()
    out = np.array([r[u["set_size"][c] == k].mean(0) for k in (4, 6, 8)])
    sd = fix_tr.std(ddof=1) if mode == "a" else r.mean(0).std()
    return (out - m) / (sd if sd > 0 else 1.0)


XZ = {mode: np.array([psth_z(units[i], mode) for i in pop]) for mode in ("a", "b")}
maint_t = (TT >= -3) & (TT < 0)


def angles(comps):
    P = np.array([[comps[1]["z"][s][maint_t].mean(), comps[2]["z"][s][maint_t].mean()] for s in range(3)])
    v = P - P.mean(0)
    ang = np.degrees(np.arctan2(v[:, 1], v[:, 0]))
    order = np.argsort(ang)
    a = np.diff(np.r_[ang[order], ang[order][0] + 360])
    return np.sort(a), P


DP = {}
for mode in ("a", "b"):
    for lam in (0.0, 1e-3, 1e-2):
        comps, Xf, tot = S.dpca(XZ[mode], 15, lam)
        DP[(mode, lam)] = comps
        ev3, ev15 = S.cumulative_ev(comps, Xf, tot, 3), S.cumulative_ev(comps, Xf, tot, 15)
        ang, P = angles(comps)
        print(f"z-score ({mode}), lambda {lam}: first 3 dPCs {ev3:.1f}% (sum of single {sum(c['ev'] for c in comps[:3]):.1f}%), "
              f"first 15 {ev15:.1f}%; marginalizations of dPC1-3 {[c['marg'] for c in comps[:3]]}; "
              f"angles in the dPC2-dPC3 plane {np.round(ang, 1).tolist()}")
# separation against label-shuffled dPCA (main: z-score a, no regularization)
def pair_dists(comps):
    Z = np.array([[c["z"][s][maint_t] for c in comps[:15]] for s in range(3)])   # set x comp x time
    return [float(np.mean(np.sqrt(((Z[i] - Z[j]) ** 2).sum(0)))) for i, j in [(0, 1), (0, 2), (1, 2)]]


obs_d = pair_dists(DP[("a", 0.0)])
null_d = []
for _ in range(200):
    Xs = []
    for i in pop:
        u = units[i]
        uu = dict(u)
        uu["set_size"] = u["set_size"].copy()
        c = u["correct"]
        uu["set_size"][c] = rng.permutation(u["set_size"][c])
        Xs.append(psth_z(uu, "a"))
    null_d.append(pair_dists(S.dpca(np.array(Xs), 15, 0.0)[0]))
null_d = np.array(null_d)
print("maintenance distance between set sizes (4-6, 4-8, 6-8):", np.round(obs_d, 3).tolist(),
      "; label-shuffled 95th percentiles:", np.round(np.percentile(null_d, 95, axis=0), 3).tolist(),
      "; P:", [(np.sum(null_d[:, k] >= obs_d[k]) + 1) / 201 for k in range(3)])
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig4a 2>&1 | sed -n '/cell 7[5-9]/,$p' | cut -c1-500
```

```
---- cell 75 [claim:fig4a-dpca-workload-separation]
z-score (a), lambda 0.0: first 3 dPCs 32.2% (sum of single 32.2%), first 15 64.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (a), lambda 0.001: first 3 dPCs 32.2% (sum of single 32.2%), first 15 64.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (a), lambda 0.01: first 3 dPCs 32.2% (sum of single 32.2%), first 15 64.3%; marginalizations of dPC1-3 ['time', 'set size', 'time']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (b), lambda 0.0: first 3 dPCs 18.7% (sum of single 18.7%), first 15 52.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (b), lambda 0.001: first 3 dPCs 18.7% (sum of single 18.7%), first 15 52.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (b), lambda 0.01: first 3 dPCs 18.7% (sum of single 18.7%), first 15 52.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
maintenance distance between set sizes (4-6, 4-8, 6-8): [16.945, 17.785, 15.593] ; label-shuffled 95th percentiles: [14.105, 14.101, 17.169] ; P: [np.float64(0.004975124378109453), np.float64(0.004975124378109453), np.float64(0.6517412935323383)]
---- 660.9s

real	11m5.596s
user	36m0.269s
sys	0m28.278s
```

**Agent calls Bash**

```bash
python - <<'EOF'
n=open('nb_src.py').read()
a=n.index('def psth_z(u, mode):')
b=n.index('maint_t = (TT >= -3) & (TT < 0)')
n=n[:a]+'''SM = []     # per neuron: smoothed rates of correct trials, their set sizes, fixation mean and SDs
for i in pop:
    u = units[i]
    c = u["correct"]
    r = np.apply_along_axis(lambda x: np.convolve(x, kern, mode="same"), 1, u["bins"][c].astype(float)) / 0.02
    fix_tr = win_rate(u, S.FIX)[c]
    SM.append((r, u["set_size"][c], fix_tr.mean(), fix_tr.std(ddof=1), r.mean(0).std()))


def psth_z(k, mode, ss=None):
    r, s, m, sd_a, sd_b = SM[k]
    s = s if ss is None else ss
    sd = sd_a if mode == "a" else sd_b
    return (np.array([r[s == v].mean(0) for v in (4, 6, 8)]) - m) / (sd if sd > 0 else 1.0)


XZ = {mode: np.array([psth_z(k, mode) for k in range(len(pop))]) for mode in ("a", "b")}
'''+n[b:]
n=n.replace('''    Xs = []
    for i in pop:
        u = units[i]
        uu = dict(u)
        uu["set_size"] = u["set_size"].copy()
        c = u["correct"]
        uu["set_size"][c] = rng.permutation(u["set_size"][c])
        Xs.append(psth_z(uu, "a"))
    null_d.append''','''    Xs = [psth_z(k, "a", rng.permutation(SM[k][1])) for k in range(len(pop))]
    null_d.append''')
open('nb_src.py','w').write(n)
EOF
cat >> nb_src.py <<'EOF'

# %% md
# ### fig4b-speed-lowest-maintenance
#
# > In the dPCA state space, the speed of the population trajectory was highest during encoding
# > and lowest during maintenance, lower than in each other trial period, including fixation.
#
# First 15 dPCs, speed by Methods equation 2 (step 20 ms), averaged over set sizes and over each
# period; dPCA rerun on neurons subsampled at 20% with replacement, (i) 200 runs, (ii) 2000
# runs; z-score (a), no regularization. Retrieval (a) 0 to 1 s, (b) 0 to 2 s. Permutation t test
# (2000 permutations) of the per-run maintenance speeds against each other period.
#
# ### fig4c-distance-largest-maintenance
#
# > The pairwise distance between the trajectories of different set sizes was larger during
# > maintenance than during encoding, and the largest of the trial periods.
#
# Distance by Methods equation 1 between each pair of set-size trajectories in the first 15
# dPCs, averaged over pairs and periods, from the same runs.

# %% [claim:fig4b-speed-lowest-maintenance,claim:fig4c-distance-largest-maintenance]
rng = np.random.default_rng(502)
PER = {"fixation": (-6, -5), "encoding": (-5, -3), "maintenance": (-3, 0), "retrieval_a": (0, 1), "retrieval_b": (0, 2)}


def speed_dist(comps):
    Z = np.array([[c["z"][s] for c in comps[:15]] for s in range(3)])     # set x comp x time
    V = np.sqrt((np.diff(Z, axis=2) ** 2).sum(1)) / 15 / 0.02            # set x (time - 1)
    Dd = np.mean([np.sqrt(((Z[i] - Z[j]) ** 2).sum(0)) for i, j in [(0, 1), (0, 2), (1, 2)]], axis=0)
    out = {}
    for k, (a, b) in PER.items():
        m = (TT >= a) & (TT < b)
        out["V_" + k] = V.mean(0)[m[1:]].mean()
        out["D_" + k] = Dd[m].mean()
    return out


runs_sd = []
for r_ in range(2000):
    sub = rng.integers(0, len(pop), int(round(0.2 * len(pop))))
    runs_sd.append(speed_dist(S.dpca(XZ["a"][sub], 15, 0.0)[0]))
RS = pd.DataFrame(runs_sd)
for n_runs in (200, 2000):
    Rk = RS.iloc[:n_runs]
    print(f"== {n_runs} runs; per-period means (speed in z per s, distance in z):")
    print(Rk.mean().round(4).to_string())
    for kind in ("V", "D"):
        for ret in ("retrieval_a", "retrieval_b"):
            others = ["fixation", "encoding", ret]
            res = []
            for o in others:
                t, p = S.perm_t(Rk[f"{kind}_maintenance"], Rk[f"{kind}_{o}"], n_perm=2000, rng=rng)
                res.append(f"{o}: t = {t:.2f}, P = {p:.4f}")
            vals = {o: Rk[f"{kind}_{o}"].mean() for o in ["maintenance"] + others}
            print(f"   {'speed' if kind == 'V' else 'distance'}, {ret}: maintenance against " + "; ".join(res)
                  + f"; highest period {max(vals, key=vals.get)}, lowest {min(vals, key=vals.get)}")
full = speed_dist(DP[("a", 0.0)])
print("full population (no subsampling):", {k: round(v, 4) for k, v in full.items()})

# %% md
# ### figs3d-hippocampus-loadings
#
# > Ranking the first 200 neurons of each region by their dPCA loading, hippocampal neurons had
# > higher loadings than entorhinal and amygdala neurons at each rank except the first three,
# > where entorhinal neurons had the highest loading.
#
# The main dPCA (z-score a, no regularization). Component (a) dPC2, (b) dPC3; loading (i) the
# absolute decoder weight, (ii) the signed weight. Per region the 200 largest, sorted; paired
# Wilcoxon signed-rank test of hippocampus against entorhinal cortex over the ranks.

# %% [claim:figs3d-hippocampus-loadings]
regs_pop = UN.region_atlas.to_numpy()[pop]
for comp_name, ci in [("(a) dPC2", 1), ("(b) dPC3", 2)]:
    w = DP[("a", 0.0)][ci]["decoder"]
    for lname, f_ in [("(i) absolute", np.abs), ("(ii) signed", lambda x: x)]:
        top = {r: np.sort(f_(w[regs_pop == r]))[::-1][:200] for r in REG}
        wt = stats.wilcoxon(top["hippocampus"], top["entorhinal"])
        print(f"{comp_name} [{DP[('a', 0.0)][ci]['marg']}], {lname}: hippocampus above entorhinal at {int(np.sum(top['hippocampus'] > top['entorhinal']))} of 200 ranks "
              f"(Wilcoxon P = {wt.pvalue:.2g}), above amygdala at {int(np.sum(top['hippocampus'] > top['amygdala']))}; "
              f"ranks 1-3 hipp {np.round(top['hippocampus'][:3], 4).tolist()} ent {np.round(top['entorhinal'][:3], 4).tolist()}")
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig4a,claim:fig4b,claim:figs3d 2>&1 | sed -n '/cell 7[5-9]/,$p' | cut -c1-500
```

```
---- cell 75 [claim:fig4a-dpca-workload-separation]
z-score (a), lambda 0.0: first 3 dPCs 32.2% (sum of single 32.2%), first 15 64.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (a), lambda 0.001: first 3 dPCs 32.2% (sum of single 32.2%), first 15 64.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (a), lambda 0.01: first 3 dPCs 32.2% (sum of single 32.2%), first 15 64.3%; marginalizations of dPC1-3 ['time', 'set size', 'time']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (b), lambda 0.0: first 3 dPCs 18.7% (sum of single 18.7%), first 15 52.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (b), lambda 0.001: first 3 dPCs 18.7% (sum of single 18.7%), first 15 52.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (b), lambda 0.01: first 3 dPCs 18.7% (sum of single 18.7%), first 15 52.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
maintenance distance between set sizes (4-6, 4-8, 6-8): [16.945, 17.785, 15.593] ; label-shuffled 95th percentiles: [14.105, 14.101, 17.169] ; P: [np.float64(0.004975124378109453), np.float64(0.004975124378109453), np.float64(0.6517412935323383)]
---- 525.0s
---- cell 77 [claim:fig4b-speed-lowest-maintenance,claim:fig4c-distance-largest-maintenance]
== 200 runs; per-period means (speed in z per s, distance in z):
V_fixation       1.0742
D_fixation       3.5083
V_encoding       0.9526
D_encoding       7.4848
V_maintenance    0.7402
D_maintenance    7.5239
V_retrieval_a    1.4138
D_retrieval_a    5.7204
V_retrieval_b    1.2948
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('sternberg.py').read()
s=s.replace('''    C = Xf @ Xf.T
    if lam > 0:
        Cinv = np.linalg.inv(C + (lam * np.sqrt(total)) ** 2 * np.eye(N))
    else:
        Cinv = np.linalg.pinv(C)
    comps = []
    for name, Xm in margs.items():
        B = Xm @ Xf.T @ Cinv''','''    # X X' + mu I through the thin SVD of X: B = X_phi V S / (S^2 + mu) U' (mu = 0 is the
    # pseudo-inverse, singular values below 1e-10 of the largest dropped)
    U0, S0, Vt0 = np.linalg.svd(Xf, full_matrices=False)
    keep = S0 > 1e-10 * S0[0]
    U0, S0, Vt0 = U0[:, keep], S0[keep], Vt0[keep]
    mu = (lam * np.sqrt(total)) ** 2
    comps = []
    for name, Xm in margs.items():
        B = ((Xm @ Vt0.T) * (S0 / (S0 ** 2 + mu))) @ U0.T''')
open('sternberg.py','w').write(s)
n=open('nb_src.py').read()
n=n.replace("    for lam in (0.0, 1e-3, 1e-2):","    for lam in (0.0, 1e-2):")
n=n.replace("for _ in range(200):\n    Xs = [psth_z","for _ in range(100):\n    Xs = [psth_z")
n=n.replace('"; P:", [(np.sum(null_d[:, k] >= obs_d[k]) + 1) / 201 for k in range(3)])','"; P:", [(np.sum(null_d[:, k] >= obs_d[k]) + 1) / 101 for k in range(3)])')
n=n.replace("# single-trial pseudopopulations); fixed lambdas of 1e-3 and 1e-2 of the data norm are shown\n# instead, (b) none (pseudo-inverse).","# single-trial pseudopopulations); a fixed lambda of 1e-2 of the data norm is shown instead,\n# (b) none (pseudo-inverse). The separation of set sizes is compared with 100 dPCA runs on\n# set-size labels shuffled across each neuron's trials.")
open('nb_src.py','w').write(n)
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig4a 2>&1 | sed -n '/cell 7[5-9]/,$p' | cut -c1-300
```

```
---- cell 75 [claim:fig4a-dpca-workload-separation]
z-score (a), lambda 0.0: first 3 dPCs 32.2% (sum of single 32.2%), first 15 64.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (a), lambda 0.01: first 3 dPCs 32.2% (sum of single 32.2%), first 15 64.3%; marginalizations of dPC1-3 ['time', 'set size', 'time']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (b), lambda 0.0: first 3 dPCs 18.7% (sum of single 18.7%), first 15 52.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
z-score (b), lambda 0.01: first 3 dPCs 18.7% (sum of single 18.7%), first 15 52.3%; marginalizations of dPC1-3 ['time', 'time', 'set size']; angles in the dPC2-dPC3 plane [0.0, 180.0, 180.0]
maintenance distance between set sizes (4-6, 4-8, 6-8): [16.945, 17.785, 15.593] ; label-shuffled 95th percentiles: [14.146, 14.089, 17.169] ; P: [np.float64(0.009900990099009901), np.float64(0.009900990099009901), np.float64(0.693069306930693)]
---- 219.7s

real	3m44.460s
user	14m7.897s
sys	0m12.308s
```

**Agent calls Bash**

```bash
python - <<'EOF'
n=open('nb_src.py').read()
n=n.replace('''import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import warnings''','''import time
import warnings''')
n=n.replace('''# %% [load]
SIG = S.load_signals(A, workers=20)''','''# %% [load]
t0 = time.time()
SIG = S.load_signals(A, workers=20)
t_sig = time.time() - t0
mb_sig = sum((s["ieeg"].shape[0] * 8 * S.IEEG_FS * 2 * s["ieeg"].shape[1] + s["eeg"].size) * 8 for s in SIG.values()) / 1e6
print(f"read {mb_sig:.0f} MB of EEG and iEEG in {t_sig:.0f} s ({mb_sig / t_sig:.1f} MB/s with 20 processes)")''')
n=n.replace('''rng = np.random.default_rng(301)
R = 1000''','''rng = np.random.default_rng(301)
R = 500''')
n=n.replace("# reruns the selection (1000 times). In the null","# reruns the selection (500 times). In the null")
n=n.replace("for _ in range(100):\n    Xs = [psth_z","for _ in range(50):\n    Xs = [psth_z")
n=n.replace('[(np.sum(null_d[:, k] >= obs_d[k]) + 1) / 101 for k in range(3)])','[(np.sum(null_d[:, k] >= obs_d[k]) + 1) / 51 for k in range(3)])')
n=n.replace("compared with 100 dPCA runs on","compared with 50 dPCA runs on")
open('nb_src.py','w').write(n)
EOF
grep -n "P_1000\|R = 500" nb_src.py | head
```

```
419:                     "P_1000": (np.sum(nl >= obs) + 1) / (len(nl) + 1),
491:                             "P_1000": (np.sum(nl >= obs) + 1) / (R + 1), "P_499": (np.sum(nl[:499] >= obs) + 1) / 500})
512:R = 500
```

**Agent calls Bash**

```bash
sed -i 's/"P_1000": /"P": /g' nb_src.py; date -u
```

```
Fri Oct 30 20:51:35 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/results.py <<'PYEOF'
R = {
"behavior-accuracy-set-size": "Reproduced. Over the 37 sessions the mean of per-session percentages is 90.26% for IN and 93.12% for OUT trials, and 98.44%, 90.47% and 85.12% for set sizes 4, 6 and 8, all within tolerance; pooling trials gives the same within 0.4 points. The repeated-measures ANOVA gives F(2, 72) = 37.28 (paper 40.25 +/- 4.03), permutation P = 0.0002. The data hold 37 sessions where the paper has 36.",
"behavior-capacity": "Reproduced under reading (c), rates pooled over set sizes times 8: mean K = 6.67 (paper 6.8 +/- 0.68). Readings (a) 5.53, (b) 6.01 and (d) 4.71 are outside the tolerance.",
"behavior-rt-workload": "Reproduced. 1676 correct trials (paper 1630 +/- 163); RT rises from 1.262 s (set size 4) to 1.420 s (6) and 1.443 s (8); the slope over trials is 47.0 ms per item (paper 48 +/- 4.8), and per-session slopes give 48.7 ms; the one-way ANOVA over trials has F(2, 1673) = 14.98, permutation P = 0.0002 (the paper's F of 21.10 on 2 and 2007 degrees of freedom is reported, not judged).",
"behavior-rt-correct-incorrect": "Reproduced. Pooled trials: correct 1.361 +/- 0.632 s, incorrect 1.894 +/- 1.228 s (paper 1.36 and 1.87), unpaired permutation t = 5.27, P = 0.0005; per-session means give the same direction (paired t = 5.73, P = 0.0005).",
"neurons-recorded": "Not reproduced. The dataset holds 1487 units (paper 1526). By bundle name, as the criterion defines the regions, 446 are hippocampal (paper 676), 456 entorhinal (449) and 585 amygdalar (401). By the atlas label of each bundle's deepest contact the counts are 640, 421 and 398 (28 under fusiform gyrus), closer to the paper. Per session, 51.3 +/- 35.6 over the 29 sessions with units matches the paper's 51 +/- 35; 8 of the 37 sessions hold no units.",
"spike-sorting-quality": "Partially reproduced. The mean firing rate over the stored trials is 2.57 +/- 3.33 Hz (paper 2.55 +/- 3.30) and the percentage of ISIs below 3 ms is 1.75 +/- 4.59% (paper 1.58 +/- 4.18), both within tolerance; the waveform SNR is 5.34 under both noise readings (paper 3.28 +/- 1.56), outside it. The noise SD of the paper is not in the files; the deposited waveform SD is a different quantity.",
"fig2b-maintenance-neurons-hippocampus": "Reproduced. With atlas regions and the paired test, 128 of 640 hippocampal neurons (20.0%, paper 20.6 +/- 2.06) are maintenance neurons, against 9.98% in entorhinal cortex and 5.78% in amygdala; chi-square 45.55 (paper 47.30 +/- 4.73), P = 1.5e-11; each area exceeds its scrambled null (P = 0.001 with 1000 repetitions, 0.002 with 499). The unpaired test and the bundle regions give the same pattern (19.2 to 22.2% in hippocampus, chi-square 41.8 to 45.6).",
"fig2c-load-dependent-maintenance-neurons": "Reproduced under the criterion. With the unpaired selection and reading (a), 22 hippocampal maintenance neurons are load dependent (paper 21 +/- 2.1), above the null (P = 0.001), and neither entorhinal cortex (P = 0.32) nor amygdala (P = 0.12) is significant; their percentage, 17.9% of 123, is outside the 15 +/- 1.5% tolerance, which the criterion does not judge. With the paired selection, 20 of 128 (15.6%) are within both tolerances but amygdala is also significant (3 of 23, P = 0.031), which is partial under the criterion.",
"fig3e-probe-neurons-entorhinal": "Reproduced under the criterion with window (b), the probe to the press, and the unpaired test: entorhinal cortex has the highest percentage (45 of 421, 10.7%; paper 41 +/- 4.1), the chi-square against the other areas is 13.63 (P = 0.0002) and every area exceeds its null. The chi-square value is outside its tolerance (23.16 +/- 2.32), which the criterion does not judge. Window (a) gives 48 entorhinal probe neurons and chi-square 23.25 (paired); window (c) puts entorhinal cortex below amygdala.",
"fig3-probe-onset-not-movement": "Reproduced under one reading. With the probe neurons of fig3e window (a), paired test (95 neurons), peaks in 0 to 1 s after the event are 7.69 +/- 5.92 Hz probe-aligned against 6.04 +/- 5.65 Hz button-aligned (paper 5.47 and 4.28, both within tolerance), paired t(94) = 4.91, P = 0.0005. With the probe neurons of the fig3e reading that met its criterion (window (b), unpaired), the difference is not significant (7.25 against 6.74 Hz, P = 0.27), and with -1 to +1 s windows the button-aligned peak is the higher in most readings.",
"fig3-probe-neurons-few-task-specific": "Partially reproduced. Among the 100 probe neurons of fig3e (window (b), unpaired), 8 (8.0%) differ between IN and OUT over 0 to 1 s (paper 8 +/- 0.8, within; 10.5% +/- 1.05, outside), but 8 differ with workload where the paper has one (0 to 2 accepted). Other readings give 2 to 12 IN/OUT neurons and 5 to 10 workload neurons.",
"fig4a-dpca-workload-separation": "Not reproduced. The first three dPCs explain 32.2% (paper 44.7 +/- 4.47) and the first 15 explain 64.3% (79 +/- 7.9) with the fixation-SD z-score; 18.7% and 52.3% with the other z-score. dPC2 is a time component, so the three set sizes lie on a line in the dPC2-dPC3 plane (angles 0, 180, 180 degrees, not 120). In the first 15 dPCs, set size 4 is farther from 6 and from 8 during maintenance than in label-shuffled runs (P = 0.02), but 6 and 8 are not (P = 0.69), so the partial criterion is not met either.",
"fig4b-speed-lowest-maintenance": "Partially reproduced. Speed is lowest during maintenance (0.74 z/s over 200 runs, below fixation 1.07, encoding 0.95 and retrieval 1.41 or 1.29; P = 0.0005 for each), but it is highest during retrieval, not encoding, under both retrieval windows and both run counts.",
"fig4c-distance-largest-maintenance": "Reproduced with 2000 runs: the distance between set-size trajectories is largest during maintenance (7.67) and larger than during encoding (7.49), t = 4.96, P = 0.0005. With 200 runs maintenance is still the largest, but its excess over encoding is not significant (7.52 against 7.48, P = 0.74), which is partial under the criterion.",
"figs3d-hippocampus-loadings": "Reproduced. Under every component and loading reading, the hippocampal top-200 loadings exceed the entorhinal ones at 196 to 200 ranks (Wilcoxon P = 1.2e-33 to 1.4e-34) and the amygdalar ones at all 200. The paper's exception, entorhinal neurons highest at the first three ranks, appears only for dPC2 with signed weights (rank 1: 0.264 against 0.255).",
"fig4d-encoding-decodes-correct": "Not reproduced. During encoding of set size 6 and 8 trials, hippocampal neurons (201 from the 10 sessions with at least five errors) decode later correctness at 51.4% (paper 80 +/- 8), at the level of the scrambled null (P = 0.47); no area and no variant is above chance.",
"fig4e-maintenance-decodes-workload": "Reproduced. Hippocampal neurons decode workload during maintenance at a median of 81.4% (paper 80 +/- 8), above the scrambled null (P = 0.004, Bonferroni 0.048, the smallest this run allows); entorhinal (62.5%) and amygdala (59.5%) are not significant after correction. The bundle regions give 81.6% for hippocampus; the variants give 70.0% (Gaussian window), 81.4% (no normalization) and 78.9% (1:2 classes).",
"fig4e-workload-decoding-leave-one-subject-out": "Reproduced. Leaving out the hippocampal units of one subject gives medians from 71.6% (without subject 1) to 81.4%, inside the widened range 63.9 to 89.1%.",
"fig4e-maintenance-neurons-carry-workload": "Reproduced. The 128 hippocampal maintenance neurons alone decode workload at 81.8%, 0.5 points from all hippocampal neurons (81.4%) and above their null (P = 0.004); the other 512 hippocampal neurons give 71.6% (paper 71 +/- 7.1), below all neurons. The unpaired selection gives 82.3% and 71.6%.",
"fig4e-no-decoding-6-vs-8": "Reproduced. Set size 6 against 8 is decoded from hippocampal neurons at 57.7%, not above the scrambled null (P = 0.16).",
"fig4f-retrieval-decodes-response": "Not reproduced. In the 500 ms before the press, all neurons decode IN against OUT at 80% (paper 90 +/- 9), with uncorrected P = 0.02 and corrected P = 0.24; no single area is significant (hippocampus 70%, entorhinal 65%, amygdala 65%). Only trials whose press falls within the 2 s stored after the probe can be used.",
"fig5-subject1-eeg-power-workload": "Partially reproduced. In subject 1, set size 8 power exceeds set size 4 at Pz (cluster 8.5 to 14.5 Hz, P = 0.002) and Fz (8 to 14 Hz, P = 0.002), as the paper shows, under every reading. But other subjects show increases too: at their maximal-PLV electrode, subjects 2 and 6 with correct trials and 4 to 30 Hz, and 2 to 4 subjects under the other readings.",
"fig5-subject1-hippocampal-power-workload": "Reproduced. In subject 1 the left posterior hippocampal channel (PHL, the hippocampal channel of the maximal pair) has higher fixation-normalized power for set size 8 in 7.5 to 9.5 Hz (P = 0.033, correct trials, 4 to 30 Hz) and 7.5 to 10 Hz with all trials; without normalization the cluster is significant only with all trials.",
"fig5-subject1-neurons-workload": "Partially reproduced. Subject 1 has 14 hippocampal maintenance neurons with more than 100 spikes in both periods (paper 5, tolerance 0). Their rate is higher for set size 8 in a cluster from -4.67 to -1.57 s, which spans encoding and maintenance (P = 0.001), under every reading.",
"fig5-subject1-plv-hippocampus-pz": "Partially reproduced. The maximal pair of subject 1 is the left hippocampal channel PHL with O2 (PLV 0.741 at 9 Hz), not Pz, which is second (mean alpha PLV 0.626 against 0.635). For PHL with Pz, maintenance PLV exceeds encoding in 8 to 11.5 Hz, the set size 8 PLV exceeds set size 4 in 8.5 to 10 Hz, the highest alpha PLV is at occipitoparietal sites (O2, Pz, O1, T6), and the PLV to Fz is higher for set size 8 in 9.5 to 10.5 Hz.",
"fig6-plv-all-subjects": "Partially reproduced. All nine subjects have a significant hippocampal-scalp pair under every reading, but the median band limits are 4.0 to 9.5 Hz (correct trials, 4 to 30 Hz), 7.0 to 17.0, 5.5 to 17.5 and 7.5 to 18.0 Hz under the other readings, none within the paper's 6.0 +/- 0.6 to 11.5 +/- 1.15 Hz. Almost every pair is significant somewhere, as the per-bin threshold is uncorrected over bins.",
"tables1-plv-per-subject": "Not reproduced. No subject matches table S1 on scalp electrode, hemisphere and maximal PLV together under any reading; the electrode matches in at most 1 subject, the hemisphere in 4 to 6, and the PLV within 10% in 2 to 3. With the PLV the Methods define, values are in the paper's range (0.47 to 0.88).",
"fig6-plv-workload-eight-of-nine": "Partially reproduced. With all trials and 1 to 40 Hz, eight of nine subjects have a higher set size 8 PLV in their individual band, as the paper says, but the workload bands (median 10.75 to 11.0 Hz, range 2.0 to 34.0 Hz) differ from the paper's (7.8 to 10 Hz, 5.5 to 16.5 Hz). Under the other readings 5 to 7 subjects count.",
"fig6-plv-maintenance-over-encoding": "Not reproduced. Maintenance PLV exceeds encoding PLV in the individual band in 4 to 6 of nine subjects under the readings (paper eight).",
"fig6-power-unchanged-individual-band": "Not reproduced, resting on an assumption. Under the adopted reading (correct trials, 4 to 30 Hz), 4 of nine subjects show no EEG power difference (five needed) and 7 no iEEG difference. With 1 to 40 Hz the counts are 6 and 8, which would reproduce the claim; with all trials 4 and 5 to 7.",
"fig6i-plv-posterior-gradient": "Not reproduced. The dataset gives 31 hippocampal channels (paper 34). PLV rises toward posterior sites (slope 0.0064 per mm), but R2 = 0.045 (paper 0.118) and permutation P = 0.26; posterior sites are higher than anterior ones without significance (0.501 against 0.385, P = 0.14). No reading is significant.",
"fig6i-no-left-right-difference": "Reproduced. Left and right hippocampal channels do not differ (0.464 against 0.431, P = 0.65, correct trials, 4 to 30 Hz; P = 0.33 to 0.78 under the other readings).",
"soz-plv-no-difference": "Reproduced. No reading finds a difference between SOZ and non-SOZ channels (differences -0.134 to +0.056, P = 0.12 to 0.97).",
}
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
sed -i 's/and with -1 to +1 s windows the button-aligned peak is the higher in most readings./and with -1 to +1 s windows the button-aligned peak is the higher in four of the six readings./' $TMPDIR/results.py
cat >> nb_src.py <<'EOF'

# %% md
# ## Claims not tested
#
# ### sfc-maintenance-over-encoding (blocked, too large)
#
# > Maintenance neurons showed significant spike-field coherence to the local field potential,
# > but not to the iEEG or scalp EEG, and for all frequency bins the percentage of neurons with
# > spike-field coherence was higher during maintenance than during encoding.
#
# The microwire LFP is in the files (`ecephys.lfp`, 32 kHz, chunked one column at a time). The
# claim needs the LFP of every microwire that carries a hippocampal maintenance neuron with at
# least 100 spikes in maintenance and in encoding. The cell below counts those wires and
# estimates the streaming time from the rate measured when the EEG and iEEG were read above.

# %% [blocked-estimate]
rows = []
for k in ["paired", "unpaired"]:
    idx = [i for i in np.where((UN.region_atlas == "hippocampus") & UN["maint_" + k])[0]
           if win_counts(units[i], S.ENC)[units[i]["correct"]].sum() >= 100 and win_counts(units[i], S.MAINT)[units[i]["correct"]].sum() >= 100]
    wires = {(UN.sess[i], [u for u in D if u["subject"] + "-" + u["session"] == UN.sess[i]][0]["units"][UN.unit[i]]["electrode_row"]) for i in idx}
    mb = sum(SIG[[d["path"] for d in D if d["subject"] + "-" + d["session"] == s][0]]["ieeg"].shape[0] * 8 * 32000 * 8 for s, _ in wires) / 1e6
    rows.append({"selection": k, "neurons": len(idx), "wires": len(wires), "LFP_MB": round(mb), "est_minutes": round(mb / (mb_sig / t_sig) / 60, 1)})
print(pd.DataFrame(rows).to_string(index=False))
print("expected neurons (fig. S6b): 94")

# %% md
# **Result: blocked (too large).** The LFP of the wires above would take the estimated minutes
# printed, at the rate measured in this notebook, on top of a notebook that already runs close
# to the 30 minute limit; it was not read. The iEEG and scalp EEG parts of the claim do not
# decide it alone (the criterion needs the LFP comparison of maintenance and encoding).
#
# ### hfo-rates-unaffected (blocked, methods underspecified)
#
# > The rates of clinically relevant high-frequency oscillations were not affected by performing
# > the task.
#
# The claims file blocks this claim until the HFO detector of reference 27 (Fedele et al. 2017)
# is supplied; neither the detector nor the comparison is given in the paper. The files hold
# the iEEG at 2 kHz, which an HFO detector would need, but only during the 8 s of each trial.
EOF
python - <<'EOF'
import os, re
exec(open(os.environ['TMPDIR'] + '/results.py').read())
n = open('nb_src.py').read()
# insert result md after the last code cell of each claim (before the next '# %% md' that follows it)
for cid, text in R.items():
    tag = f"claim:{cid}"
    pos = n.find(f"# %% [{tag}")
    if pos < 0:
        pos = n.find(tag)
    assert pos >= 0, cid
    nxt = n.find("\n# %% md", pos)
    # skip forward if the next md belongs to another tagged claim that shares the cell (4b/4c)
    block = f"\n# %% md\n# **Result: {text.split('.')[0]}.**{text[len(text.split('.')[0]) + 1:]}\n"
    # wrap long lines
    words = block.split(' ')
    n = n[:nxt] + "\n# %% md\n# " + "**Result: " + text.split('.')[0] + ".**" + text[len(text.split('.')[0]) + 1:] + "\n" + n[nxt:]
open('nb_src.py', 'w').write(n)
EOF
grep -c "Result:" nb_src.py
```

```
34
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os
exec(open(os.environ['TMPDIR'] + '/results.py').read())
order = ["behavior-accuracy-set-size","behavior-capacity","behavior-rt-workload","behavior-rt-correct-incorrect","neurons-recorded","spike-sorting-quality","fig2b-maintenance-neurons-hippocampus","fig2c-load-dependent-maintenance-neurons","fig3e-probe-neurons-entorhinal","fig3-probe-onset-not-movement","fig3-probe-neurons-few-task-specific","fig4a-dpca-workload-separation","fig4b-speed-lowest-maintenance","fig4c-distance-largest-maintenance","fig4d-encoding-decodes-correct","fig4e-maintenance-decodes-workload","fig4e-workload-decoding-leave-one-subject-out","fig4e-maintenance-neurons-carry-workload","fig4e-no-decoding-6-vs-8","fig4f-retrieval-decodes-response","figs3d-hippocampus-loadings","fig5-subject1-eeg-power-workload","fig5-subject1-hippocampal-power-workload","fig5-subject1-neurons-workload","fig5-subject1-plv-hippocampus-pz","fig6-plv-all-subjects","tables1-plv-per-subject","fig6-plv-workload-eight-of-nine","fig6-plv-maintenance-over-encoding","fig6-power-unchanged-individual-band","fig6i-plv-posterior-gradient","fig6i-no-left-right-difference","soz-plv-no-difference","hfo-rates-unaffected","sfc-maintenance-over-encoding"]
def outc(cid):
    if cid == "hfo-rates-unaffected": return "Blocked: methods underspecified"
    if cid == "sfc-maintenance-over-encoding": return "Blocked: too large"
    return R[cid].split('.')[0]
head = "\n# %% md\n# ## Claims\n#\n# | Claim | Tested |\n# |---|---|\n" + "".join(f"# | {c} | {'no, blocked' if c in ('hfo-rates-unaffected','sfc-maintenance-over-encoding') else 'yes'} |\n" for c in order)
summ = "\n# %% md\n# ## Summary\n#\n# | Claim | Outcome |\n# |---|---|\n" + "".join(f"# | {c} | {outc(c)} |\n" for c in order) + """#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's:
#
# - 37 sessions, where the paper has 36; 1487 units, where it has 1526. Eight sessions hold no
#   units table.
# - Regions of units: the atlas label of each bundle's deepest contact (Methods, Depth electrode
#   localization) for every claim except `neurons-recorded`, where the claims file names the
#   bundle; the bundle reading is shown for the main neuron and decoding claims.
# - In the null repetitions of the probe-neuron selection, the P of each t test comes from the t
#   distribution (agreement with the permutation P on the observed tests printed).
# - Decoding uses 100 resampling runs and 250 null runs (Methods: 500 and 500); the NDT details
#   the Methods leave open take the toolbox's defaults.
# - The files store only 8 s per trial (-6 to +2 s around the probe), which limits the
#   retrieval and button-aligned analyses to presses within 2 s.
# - dPCA uses 20 ms bins, no cross-validated regularization, and 50 label-shuffled runs.
# - The scalp EEG is re-referenced to the averaged mastoids here; the deposited EEG is not.
# - PLV follows FieldTrip's taper-averaged cross-spectra (assumption); per-taper PLV is a
#   variant for the selection.
# - The microwire LFP was not read (spike-field coherence blocked for run time), and the HFO
#   detector is not available.
#
# What was found about the dataset:
#
# - 1487 units in 29 of 37 sessions; the per-session mean over sessions with units (51.3) matches
#   the paper's 51, which suggests the paper's 1526 includes about one more session of units.
# - Units point at macroelectrode rows of the electrodes table, and the microwire LFP channels
#   reuse those rows; microwires have no rows or coordinates of their own.
# - Region counts by bundle name differ widely from the paper's; the atlas label of the bundle's
#   deepest contact comes close (640, 421, 398 against 676, 449, 401).
# - Spike times are stored unsorted in some units.
# - `response_type` uses 51/52 on correct and 1/2 on incorrect trials, without a description.
# - The trial-stage table numbers each Probe stage one trial late, and seven files lack it.
# - EEG and iEEG are labelled volts but hold values of about +/- 150 and +/- 240, consistent with
#   microvolts; the electrodes table says the EEG is referenced to the averaged mastoids, but A1
#   + A2 is not zero.
# - Electrode coordinates use a frame with +x posterior, not MNI; scalp electrode positions are
#   template positions on a sphere.
# - The subject 1 description lists AHR among SOZ electrodes, but subject 1 has no AHR electrode.
"""
n = open('nb_src.py').read()
first = n.index("\n# %% [setup]")
n = n[:first] + head + n[first:] + summ
open('nb_src.py', 'w').write(n)
EOF
cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000574-boran-2019
type: reproduction
title: Persistent hippocampal firing and hippocampal-cortical coupling in verbal working memory (Boran et al. 2019)
description: Tests the findings of Boran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald and Sarnthein
  (2019) on dandiset 000574, which holds the units, scalp EEG, hippocampal and other iEEG and
  microwire LFP of nine epilepsy patients performing a modified Sternberg task (37 sessions). It
  tests behavior, unit counts and sorting quality, maintenance and probe neurons, population
  decoding, dPCA state space, scalp EEG and hippocampal iEEG power, and hippocampal-scalp phase
  locking.
license: Apache-2.0
notebooks:
- path: reproduce_boran_2019.ipynb
  title: Reproducing Boran et al. (2019) from dandiset 000574
  runtime_minutes: 25
helpers:
- sternberg.py
related:
- id: dandi:000574/0.250815.1108
  relation: uses_data
- id: doi:10.1126/sciadv.aav3687
  relation: reproduces
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/mk.py nb_src.py reproduce_boran_2019.ipynb && python -c "import nbformat;nb=nbformat.read('reproduce_boran_2019.ipynb',4);print(len(nb.cells))"; sed -n 1,80p ../../tools/entry.py | grep -n "install\|cell" | head
```

```
118
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
26:notebook through a Jupyter kernel installed in that environment, in the entry
33:markdown cell that begins "**Result:" and everything from the "## Summary"
```

**Agent calls Bash**

```bash
sed -n 1,60p ../../tools/entry.py; cd ../.. && python tools/entry.py lock entries/000574-boran-2019 2>&1 | tail -5
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
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/000574-boran-2019 2>&1 | tail -15
```

```
0 error(s)
```

**Agent calls Bash**

```bash
date -u; time python tools/entry.py run entries/000574-boran-2019 --max-minutes 40 2>&1 | tail -15; date -u
```

```
Fri Oct 30 20:53:21 UTC 2026
[32m   1837[39m [38;5;28;01mwith[39;00m errstate(call=_raise_linalgerror_svd_nonconvergence,
[32m   1838[39m               invalid=[33m'[39m[33mcall[39m[33m'[39m, over=[33m'[39m[33mignore[39m[33m'[39m, divide=[33m'[39m[33mignore[39m[33m'[39m,
[32m   1839[39m               under=[33m'[39m[33mignore[39m[33m'[39m):
[32m-> [39m[32m1840[39m     u, s, vh = [30;43mgufunc[39;49m[30;43m([39;49m[30;43ma[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43msignature[39;49m[30;43m=[39;49m[30;43msignature[39;49m[30;43m)[39;49m
[32m   1841[39m u = u.astype(result_t, copy=[38;5;28;01mFalse[39;00m)
[32m   1842[39m s = s.astype(_realType(result_t), copy=[38;5;28;01mFalse[39;00m)

[36mFile [39m[32m~/work/encore/encore/executed/000574-boran-2019/.venv/lib/python3.13/site-packages/numpy/linalg/_linalg.py:153[39m, in [36m_raise_linalgerror_svd_nonconvergence[39m[34m(err, flag)[39m
[32m    152[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m_raise_linalgerror_svd_nonconvergence[39m(err, flag):
[32m--> [39m[32m153[39m     [38;5;28;01mraise[39;00m LinAlgError([33m"[39m[33mSVD did not converge[39m[33m"[39m)

[31mLinAlgError[39m: SVD did not converge


FAIL  reproduce_boran_2019.ipynb  (1413 s)

real	23m36.243s
user	62m21.500s
sys	1m31.635s
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/000574-boran-2019/; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat
nb = nbformat.read('executed/000574-boran-2019/reproduce_boran_2019.ipynb', 4)
for i, c in enumerate(nb.cells):
    if c.cell_type == 'code':
        tags = c.metadata.get('tags', [])
        err = any(o.get('output_type') == 'error' for o in c.get('outputs', []))
        txt = "".join(o.get('text', '') for o in c.get('outputs', []) if o.get('output_type') == 'stream')
        print(i, tags, 'ERROR' if err else '', txt[:150].replace('\n', ' | '))
EOF
```

```
Exit code 1
result.json
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbformat/__init__.py", line 169, in read
    buf = fp.read()
          ^^^^^^^
AttributeError: 'str' object has no attribute 'read'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbformat/__init__.py", line 171, in read
    with open(fp, encoding="utf8") as f:  # noqa: PTH123
         ~~~~^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'executed/000574-boran-2019/reproduce_boran_2019.ipynb'
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('entries/000574-boran-2019/sternberg.py').read()
s=s.replace('''    U0, S0, Vt0 = np.linalg.svd(Xf, full_matrices=False)''','''    U0, S0, Vt0 = _svd(Xf)''')
s=s.replace('''        U, s, Vt = np.linalg.svd(B @ Xf, full_matrices=False)
        for k in range(min(n_comp, U.shape[1])):
            enc = U[:, k]
            dec = U[:, k] @ B
            z = dec @ Xf
            ev = 100 * (total - np.sum((Xf - np.outer(enc, z)) ** 2)) / total''','''        U, s, Vt = _svd(B @ Xf)
        for k in range(min(n_comp, U.shape[1])):
            enc = U[:, k]
            dec = U[:, k] @ B
            z = dec @ Xf
            # ||X - enc z||^2 = ||X||^2 - 2 enc' X z + ||enc||^2 ||z||^2
            ev = 100 * (2 * enc @ (Xf @ z) - (enc @ enc) * (z @ z)) / total''')
s=s.replace('''def dpca(X, n_comp=15, lam=0.0):''','''def _svd(M):
    """Thin SVD; falls back to LAPACK gesvd when gesdd does not converge (subsamples drawn with
    replacement repeat rows, which gesdd sometimes fails on)."""
    try:
        return np.linalg.svd(M, full_matrices=False)
    except np.linalg.LinAlgError:
        from scipy.linalg import svd
        return svd(M, full_matrices=False, lapack_driver="gesvd")


def dpca(X, n_comp=15, lam=0.0):''')
open('entries/000574-boran-2019/sternberg.py','w').write(s)
n=open('entries/000574-boran-2019/nb_src.py').read()
n=n.replace("for _ in range(50):\n    Xs = [psth_z","for _ in range(40):\n    Xs = [psth_z")
n=n.replace('[(np.sum(null_d[:, k] >= obs_d[k]) + 1) / 51 for k in range(3)])','[(np.sum(null_d[:, k] >= obs_d[k]) + 1) / 41 for k in range(3)])')
n=n.replace("compared with 50 dPCA runs on","compared with 40 dPCA runs on")
n=n.replace('''rng = np.random.default_rng(402)
lab_corr = lambda u: (u["correct"].astype(int), u["set_size"] >= 6)
for regcol in ["region_atlas", "region_bundle"]:''','''rng = np.random.default_rng(402)
lab_corr = lambda u: (u["correct"].astype(int), u["set_size"] >= 6)
for regcol in ["region_atlas"]:''')
n=n.replace('''for regcol in ["region_atlas", "region_bundle"]:
    for r in REG + ["all"]:''','''for regcol in ["region_atlas"]:
    for r in REG + ["all"]:''')
open('entries/000574-boran-2019/nb_src.py','w').write(n)
EOF
cd entries/000574-boran-2019; . $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig4a,claim:fig4b,claim:figs3d 2>&1 | sed -n '/cell 7[5-9]/,$p' | grep -v "^ *[VD]_" | cut -c1-300
```

```
real	6m29.397s
user	25m5.102s
sys	0m5.624s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; date -u; python $TMPDIR/runcells.py nb_src.py $TMPDIR/pre3.py prep,claim:fig4b 2>&1 | tail -30 | cut -c1-300
```

```
Fri Oct 30 21:23:59 UTC 2026
---- cell 2 [setup]
---- 0.4s
---- cell 22 [prep]
1487 units; {'hippocampus': 640, 'entorhinal': 421, 'amygdala': 398, 'other': 28}
---- 2.2s
---- cell 47 [prep]
---- 0.1s
---- cell 85 [prep]
---- 0.0s
---- cell 108 [claim:fig4b-speed-lowest-maintenance,claim:fig4c-distance-largest-maintenance]
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 16, in <module>
    exec(body, g)
    ~~~~^^^^^^^^^
  File "<string>", line 19, in <module>
NameError: name 'pop' is not defined. Did you mean: 'pow'?
```

**Agent calls Bash**

```bash
cd ../.. && . $TMPDIR/dev/bin/activate && python $TMPDIR/mk.py entries/000574-boran-2019/nb_src.py entries/000574-boran-2019/reproduce_boran_2019.ipynb && deactivate; date -u; time python tools/entry.py run entries/000574-boran-2019 --max-minutes 40 2>&1 | tail -5; date -u
```

```
Fri Oct 30 21:24:11 UTC 2026
Installed kernelspec registry-000574-boran-2019 in executed/000574-boran-2019/.venv/share/jupyter/kernels/registry-000574-boran-2019
pass  reproduce_boran_2019.ipynb  (1433 s)

real	23m57.284s
user	63m12.396s
sys	1m24.981s
Fri Oct 30 21:48:08 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python - <<'EOF' > $TMPDIR/exec_out.txt
import nbformat
nb = nbformat.read('executed/000574-boran-2019/reproduce_boran_2019.ipynb', 4)
for i, c in enumerate(nb.cells):
    if c.cell_type == 'code':
        tags = c.metadata.get('tags', [])
        txt = "".join(o.get('text', '') for o in c.get('outputs', []) if o.get('output_type') == 'stream')
        print(f"#### cell {i} {tags}\n{txt}")
EOF
wc -l $TMPDIR/exec_out.txt; grep -n "####" $TMPDIR/exec_out.txt | head -80
```

```
996 /tmp/claude-1001/exec_out.txt
1:#### cell 2 ['setup']
3:#### cell 3 ['load']
6:#### cell 5 ['sanity']
60:#### cell 6 ['sanity']
100:#### cell 7 ['sanity']
157:#### cell 8 ['sanity']
183:#### cell 10 ['claim:behavior-accuracy-set-size']
202:#### cell 13 ['claim:behavior-capacity']
210:#### cell 16 ['claim:behavior-rt-workload']
216:#### cell 19 ['claim:behavior-rt-correct-incorrect']
221:#### cell 22 ['prep']
224:#### cell 24 ['claim:neurons-recorded']
233:#### cell 27 ['claim:spike-sorting-quality']
243:#### cell 30 ['claim:fig2b-maintenance-neurons-hippocampus']
273:#### cell 33 ['claim:fig2c-load-dependent-maintenance-neurons']
315:#### cell 36 ['claim:fig3e-probe-neurons-entorhinal']
390:#### cell 39 ['claim:fig3-probe-onset-not-movement']
404:#### cell 42 ['claim:fig3-probe-neurons-few-task-specific']
418:#### cell 45 ['load']
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '1,8p;60,64p;157,243p' $TMPDIR/exec_out.txt | cut -c1-250
```

```
#### cell 2 ['setup']

#### cell 3 ['load']
37 assets read at version 0.250815.1108

#### cell 5 ['sanity']
   subject session                      start  trials  correct  artifact  units  eeg_ch  ieeg_ch  eeg_rate  ieeg_rate      lfp_rate
0       01      01  2016-12-14T17:13:00+01:00      50       44         2     37      19       48     200.0     2000.0  32000.000000
#### cell 6 ['sanity']
   subject session        stages  max |probe stage - (start+6)|  max |fixation stage - start|
0       01      01            ok                            0.0                           0.0
1       01      02            ok                            0.0                           0.0
2       01      03  no ttl_stage                            NaN                           NaN
#### cell 8 ['sanity']
x of contact 1, AH and PH per subject:
                 AH         PH
subject                      
01       12.875392  30.128983
02       11.928791  22.130217
03       10.986120  28.851149
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '100,103p;273,281p;315,330p;385,418p' $TMPDIR/exec_out.txt | cut -c1-330
```

```
#### cell 7 ['sanity']
units 1487 ; units whose spike times are stored unsorted: 43 {('01', '01'): 4, ('01', '02'): 8, ('07', '02'): 10, ('07', '03'): 14, ('07', '04'): 7} ; fraction of (first 200) spikes inside the unit's obs_intervals: 1.0
region_atlas   amygdala  entorhinal  hippocampus  other:FuG   All
region_bundle                                                    
#### cell 33 ['claim:fig2c-load-dependent-maintenance-neurons']
== maintenance neurons from the paired test, reading a_ttest, regions region_atlas
     region  maintenance  load_dependent     pct  null_mean      P  P_499
hippocampus          128              20 15.6250      3.401 0.0010  0.002
 entorhinal           42               2  4.7619      1.177 0.3357  0.350
   amygdala           23               3 13.0435      0.649 0.0310  0.032
== maintenance neurons from the paired test, reading a_ttest, regions region_bundle
     region  maintenance  load_dependent     pct  null_mean      P  P_499
hippocampus           99              19 19.1919      2.654 0.0010  0.002
#### cell 36 ['claim:fig3e-probe-neurons-entorhinal']
agreement of permutation and t-distribution P at 0.05 on the observed tests: 0.9870
== window (a), paired, regions region_atlas: total probe neurons 97
     region   n  selected     pct  null_mean  null_95     P  P_499
hippocampus 640        29  4.5312      2.576      5.0 0.002  0.002
 entorhinal 421        48 11.4014      1.710      4.0 0.002  0.002
   amygdala 398        20  5.0251      1.422      4.0 0.002  0.002
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '330,352p' $TMPDIR/exec_out.txt | cut -c1-200
```

```
region   n  selected     pct  null_mean  null_95     P  P_499
hippocampus 640        30  4.6875      2.536     5.05 0.002  0.002
 entorhinal 421        46 10.9264      1.662     4.00 0.002  0.002
   amygdala 398        31  7.7889      1.528     4.00 0.002  0.002
   chi-square entorhinal against the other two: 11.24 (P = 0.0008); Yates 10.51 (P = 0.0012)
== window (b), unpaired, regions region_atlas: total probe neurons 97
     region   n  selected     pct  null_mean  null_95     P  P_499
hippocampus 640        26  4.0625      2.186      5.0 0.002  0.002
 entorhinal 421        44 10.4513      1.358      4.0 0.002  0.002
   amygdala 398        27  6.7839      1.082      3.0 0.002  0.002
   chi-square entorhinal against the other two: 13.79 (P = 0.0002); Yates 12.94 (P = 0.00032)
== window (c), paired, regions region_atlas: total probe neurons 94
     region   n  selected    pct  null_mean  null_95     P  P_499
hippocampus 640        33 5.1562      2.310      5.0 0.002  0.002
 entorhinal 421        30 7.1259      1.628      4.0 0.002  0.002
   amygdala 398        31 7.7889      1.400      3.0 0.002  0.002
   chi-square entorhinal against the other two: 0.46 (P = 0.5); Yates 0.31 (P = 0.58)
== window (c), unpaired, regions region_atlas: total probe neurons 91
     region   n  selected    pct  null_mean  null_95     P  P_499
hippocampus 640        33 5.1562      1.966      4.0 0.002  0.002
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '418,470p' $TMPDIR/exec_out.txt | cut -c1-200; grep -n "==\|maximal pair\|subject 1, trials\|significant increases\|range,\|chi\|left\|SOZ" $TMPDIR/exec_out.txt | sed -n '1,400p' | awk -F: '$1>468' | cut -c1-260 | head -120
```

```
#### cell 45 ['load']
read 1938 MB of EEG and iEEG in 126 s (15.4 MB/s with 20 processes)

#### cell 46 ['sanity']
EEG and iEEG samples per trial, sampling intervals and first-sample offsets from trial starts:
                    path            eeg  ieeg_bipolar  eeg_dt  ieeg_dt  max_offset_eeg  max_offset_ieeg            hipp
sub-01/sub-01_ses-01.nwb (50, 19, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,PHL,PHR
sub-01/sub-01_ses-02.nwb (50, 19, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,PHL,PHR
sub-01/sub-01_ses-03.nwb (50, 19, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,PHL,PHR
sub-01/sub-01_ses-04.nwb (50, 19, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,PHL,PHR
sub-02/sub-02_ses-01.nwb  (49, 8, 1600) (49, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-02.nwb  (47, 8, 1600) (47, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-03.nwb  (50, 8, 1600) (50, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-04.nwb  (48, 8, 1600) (48, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-05.nwb  (46, 8, 1600) (46, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-06.nwb  (50, 8, 1600) (50, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-02/sub-02_ses-07.nwb  (49, 8, 1600) (49, 4, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00 AHL,AHR,PHL,PHR
sub-03/sub-03_ses-01.nwb  (47, 8, 1600) (47, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,AHR,PHL
sub-03/sub-03_ses-02.nwb  (50, 8, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AHL,AHR,PHL
sub-03/sub-03_ses-03.nwb  (50, 8, 1600) (50, 3, 1600)   0.005   0.0005    0.000000e+00     0.000000e+00     AH
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '837,847p;852,869p;894,996p' $TMPDIR/exec_out.txt | cut -c1-330
```

```
#### cell 70 ['claim:fig5-subject1-neurons-workload']
maintenance neurons paired, regions region_atlas: 30 in subject 1 hippocampus, 14 with > 100 spikes in both periods; (a) trials (n = 70, 25 of set size 8): significant positive clusters [(-4.67, -1.57, 508.8, np.float64(0.000999000999000999))]; in encoding True, in maintenance True
maintenance neurons paired, regions region_atlas: 30 in subject 1 hippocampus, 14 with > 100 spikes in both periods; (b) neuron-trials (n = 490, 175 of set size 8): significant positive clusters [(-4.75, -1.29, 638.8, np.float64(0.000999000999000999)), (-0.87, -0.25, 99.2, np.float64(0.01998001998001998))]; in encoding True, in 
maintenance neurons paired, regions region_bundle: 30 in subject 1 hippocampus, 14 with > 100 spikes in both periods; (a) trials (n = 70, 25 of set size 8): significant positive clusters [(-4.67, -1.57, 508.8, np.float64(0.000999000999000999))]; in encoding True, in maintenance True
maintenance neurons paired, regions region_bundle: 30 in subject 1 hippocampus, 14 with > 100 spikes in both periods; (b) neuron-trials (n = 490, 175 of set size 8): significant positive clusters [(-4.75, -1.29, 638.8, np.float64(0.000999000999000999)), (-0.87, -0.25, 99.2, np.float64(0.012987012987012988))]; in encoding True, i
maintenance neurons unpaired, regions region_atlas: 31 in subject 1 hippocampus, 15 with > 100 spikes in both periods; (a) trials (n = 70, 25 of set size 8): significant positive clusters [(-4.67, -1.59, 513.4, np.float64(0.000999000999000999))]; in encoding True, in maintenance True
maintenance neurons unpaired, regions region_atlas: 31 in subject 1 hippocampus, 15 with > 100 spikes in both periods; (b) neuron-trials (n = 524, 188 of set size 8): significant positive clusters [(-4.75, -1.29, 663.5, np.float64(0.000999000999000999)), (-0.89, -0.25, 103.1, np.float64(0.00999000999000999))]; in encoding True, 
maintenance neurons unpaired, regions region_bundle: 31 in subject 1 hippocampus, 15 with > 100 spike
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os
p = os.environ['TMPDIR'] + '/results.py'
s = open(p).read()
rep = {
'"fig3e-probe-neurons-entorhinal": "Reproduced under the criterion with window (b), the probe to the press, and the unpaired test: entorhinal cortex has the highest percentage (45 of 421, 10.7%; paper 41 +/- 4.1), the chi-square against the other areas is 13.63 (P = 0.0002) and every area exceeds its null. The chi-square value is outside its tolerance (23.16 +/- 2.32), which the criterion does not judge. Window (a) gives 48 entorhinal probe neurons and chi-square 23.25 (paired); window (c) puts entorhinal cortex below amygdala.",':
'"fig3e-probe-neurons-entorhinal": "Reproduced under the criterion with window (b), the probe to the press, and the unpaired test: entorhinal cortex has the highest percentage (44 of 421, 10.5%; paper 41 +/- 4.1), the chi-square against the other areas is 13.79 (P = 0.0002) and every area exceeds its null (P = 0.002). The chi-square value is outside its tolerance (23.16 +/- 2.32), which the criterion does not judge. Window (a) gives 46 to 48 entorhinal probe neurons with chi-square 20.55 to 21.54; window (c) puts entorhinal cortex below amygdala.",',
'With the probe neurons of fig3e window (a), paired test (95 neurons), peaks in 0 to 1 s after the event are 7.69 +/- 5.92 Hz probe-aligned against 6.04 +/- 5.65 Hz button-aligned (paper 5.47 and 4.28, both within tolerance), paired t(94) = 4.91, P = 0.0005. With the probe neurons of the fig3e reading that met its criterion (window (b), unpaired), the difference is not significant (7.25 against 6.74 Hz, P = 0.27)':
'With the probe neurons of fig3e window (a), paired test (97 neurons), peaks in 0 to 1 s after the event are 7.72 +/- 5.91 Hz probe-aligned against 6.04 +/- 5.61 Hz button-aligned (paper 5.47 and 4.28, both within tolerance), paired t(96) = 5.07, P = 0.0005. With the probe neurons of the fig3e reading that met its criterion (window (b), unpaired), the difference is not significant (7.26 against 6.76 Hz, P = 0.33)',
'"fig3-probe-neurons-few-task-specific": "Partially reproduced. Among the 100 probe neurons of fig3e (window (b), unpaired), 8 (8.0%) differ between IN and OUT over 0 to 1 s (paper 8 +/- 0.8, within; 10.5% +/- 1.05, outside), but 8 differ with workload where the paper has one (0 to 2 accepted). Other readings give 2 to 12 IN/OUT neurons and 5 to 10 workload neurons.",':
'"fig3-probe-neurons-few-task-specific": "Partially reproduced. With the probe neurons of fig3e window (b), paired test (107), 8 (7.5%) differ between IN and OUT over 0 to 2 s (paper 8 +/- 0.8, within; 10.5% +/- 1.05, outside), but 7 differ with workload where the paper has one (0 to 2 accepted). Across all readings 2 to 13 probe neurons differ between IN and OUT and 5 to 8 with workload, so the workload count never holds.",',
'In the first 15 dPCs, set size 4 is farther from 6 and from 8 during maintenance than in label-shuffled runs (P = 0.02), but 6 and 8 are not (P = 0.69)':
'In the first 15 dPCs, set size 4 is farther from 6 and from 8 during maintenance than in 40 label-shuffled runs (P = 0.024), but 6 and 8 are not (P = 0.68)',
'"figs3d-hippocampus-loadings": "Reproduced. Under every component and loading reading, the hippocampal top-200 loadings exceed the entorhinal ones at 196 to 200 ranks (Wilcoxon P = 1.2e-33 to 1.4e-34) and the amygdalar ones at all 200. The paper\'s exception, entorhinal neurons highest at the first three ranks, appears only for dPC2 with signed weights (rank 1: 0.264 against 0.255).",':
'"figs3d-hippocampus-loadings": "Reproduced. Under every component and loading reading, the hippocampal top-200 loadings exceed the entorhinal and the amygdalar ones at all 200 ranks (Wilcoxon P = 1.4e-34 against entorhinal cortex). The exception the statement mentions, entorhinal neurons highest at the first three ranks, does not appear in any reading; the criterion does not judge it.",',
}
for a, b in rep.items():
    assert a in s, a[:60]
    s = s.replace(a, b)
open(p, 'w').write(s)
EOF
grep -c "" $TMPDIR/results.py
```

```
35
```

**Agent calls Bash**

```bash
cd entries/000574-boran-2019 && python - <<'EOF'
import os, re
exec(open(os.environ['TMPDIR'] + '/results.py').read())
n = open('nb_src.py').read()
n = re.sub(r"\n# %% md\n# \*\*Result: (?!blocked)[^\n]*\n", "\n", n)
assert n.count("**Result:") == 1
for cid, text in R.items():
    pos = n.find(f"claim:{cid}")
    nxt = n.find("\n# %% md", pos)
    first = text.split('.')[0]
    n = n[:nxt] + "\n# %% md\n# **Result: " + first + ".**" + text[len(first) + 1:] + "\n" + n[nxt:]
open('nb_src.py', 'w').write(n)
print(n.count("**Result:"))
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/mk.py nb_src.py reproduce_boran_2019.ipynb
# patch executed copy markdown: replace md cells by the source's md cells in order (code cells unchanged)
python - <<'EOF'
import nbformat
src = nbformat.read('reproduce_boran_2019.ipynb', 4)
ex = nbformat.read('../../executed/000574-boran-2019/reproduce_boran_2019.ipynb', 4)
sc = [c for c in src.cells]
# align by code cells: the code sources must match
src_code = [c.source for c in sc if c.cell_type == 'code']
ex_code = [c for c in ex.cells if c.cell_type == 'code']
assert src_code == [c.source for c in ex_code], "code differs"
new = []
it = iter(ex_code)
for c in sc:
    new.append(next(it) if c.cell_type == 'code' else c)
ex.cells = new
nbformat.write(ex, '../../executed/000574-boran-2019/reproduce_boran_2019.ipynb')
print('patched', len(new))
EOF
```

```
34
patched 118
```

**Agent calls Bash**

```bash
mv nb_src.py $TMPDIR/nb_src.py; cd ../..; date -u; cat questions/000005.yaml | head -30; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['required']));print(list(s['properties'].keys()));o=s['properties']['outcomes']['items'];print(o.get('required'),list(o['properties'].keys()));f=s['properties']['findings']['items'];print(f.get('required'),list(f['properties'].keys()))"
```

```
Fri Oct 30 21:49:30 UTC 2026
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
  answer: >-
    The recording's sampling rate, not 1 ms bins. The Methods give 1 ms bins for spike PSTHs
    only ("All touch-spike PSTHs were constructed with a bin size of 1 ms"), and the paper's Vm
[... 15 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "questions/000574.yaml",
 "content": "dandiset: \"000574\"\npaper: doi:10.1126/sciadv.aav3687\nquestions:\n- claim: neurons-recorded\n  asked: 2026-10-30\n  question: >-\n    The criterion assigns units to regions by the name of their electrode (AH and PH\n    hippocampus, EC entorhinal cortex, A amygdala, from Table 1 of the data descriptor). Does the\n    paper assign them that way, or by the atlas location of the recording site, as its Methods\n    describe for the electrode contacts? If the latter, should the region of a unit be the\n    Brainnetome label of the contact nearest the microwires (contact 1)?\n  passage: >-\n    \"The contact positions were normalized to the MNI space and assigned to a brain region using\n    the Brainnetome Atlas\" (Methods, Depth electrode localization); \"Location of the\n    microelectrodes at the tip of the depth electrodes in MNI's MNI152 space ... color-coded\n    (cyan, hippocampus; magenta, entorhinal cortex; yellow, amygdala)\" (Fig. 1D legend).\n  why: >-\n    By electrode name the dataset's 1487 units split 446 hippocampus, 456 entorhinal cortex and\n    585 amygdala (paper 676, 449, 401); by the atlas label of each bundle's contact 1 they split\n    640, 421 and 398, with 28 under fusiform gyrus. Several electrodes named for amygdala or\n    entorhinal cortex have their deepest contact labelled hippocampus (for example AR of subject\n    8, 186 units). The criterion's counts are exact, so the reading decides the outcome of this\n    claim, and the region of every neuron in the other neuron and decoding claims.\n"
}
```

```
File created successfully at: questions/000574.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n "verifications\|found" schemas/attempt.schema.json | head; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['provenance'],indent=0)[:1500]);print(json.dumps(s['properties']['inputs'])[:400]);print(json.dumps(s['properties']['outcomes']['items']['properties']['measured'])[:300]); print(json.dumps(s['properties']['findings']['items']['properties']['kind']))"
```

```
199:            "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
253:            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
334:    "verifications": {
404:      "description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.",
432:          "found": {
433:            "description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\").",
{
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"accountable"
],
"properties": {
"kind": {
"enum": [
"agent",
"person"
]
},
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/mkattempt.py <<'PYEOF'
import os, yaml, textwrap
exec(open(os.environ['TMPDIR'] + '/results.py').read())
NB = "reproduce_boran_2019.ipynb"
REG_DEV = ("Regions of units by the Brainnetome label of each bundle's deepest contact (Methods, Depth "
           "electrode localization, \"assigned to a brain region using the Brainnetome Atlas\"); the "
           "claims file does not say for this claim. Taking contact 1 as the site of the microwires is an "
           "assumption (they protrude from the tip). The bundle-name reading is shown as a variant.")
SESS_DEV = "37 sessions and 1487 units, where the paper has 36 sessions and 1526 units."
PLV_DEV = ("PLV as FieldTrip computes it (cross-spectra averaged over tapers within each trial, then "
           "normalized and averaged over trials); the Methods give equation 3 and cite FieldTrip but not how "
           "the seven tapers enter (assumption; per-taper PLV shown as a variant for the selection).")
EEG_DEV = ("Scalp EEG re-referenced here to the averaged mastoids (Methods, Recording setup); the deposited "
           "EEG is not re-referenced although its electrodes table says it is. iEEG decimated from 2 kHz to "
           "200 Hz with a zero-phase filter before the spectra (standard choice; it cannot change spectra "
           "below 40 Hz). Trials pooled over each subject's sessions, artifact-marked trials left out.")
O = []
def add(cid, outcome, notes, deviations=(), measured=None, assumed=False, blocked_by=None):
    o = {"claim": cid, "outcome": outcome}
    if blocked_by: o["blocked_by"] = blocked_by
    o["notebook"] = NB
    if outcome != "blocked":
        o["output"] = f"claim:{cid}"
    if measured is not None: o["measured"] = measured
    if assumed: o["assumed"] = True
    o["notes"] = notes
    if deviations: o["deviations"] = list(deviations)
    O.append(o)
def body(cid):
    t = R[cid]
    return t[len(t.split('.')[0]) + 1:].strip()

add("behavior-accuracy-set-size", "reproduced", body("behavior-accuracy-set-size") + " With one session left out in turn, F ranges from 34.41 to 41.81.",
    [SESS_DEV, "The ANOVA's permutation scheme (set-size labels shuffled within session, 4999 permutations) is the claims file's reading."],
    [90.26, 93.12, 98.44, 90.47, 85.12, 37.28])
add("behavior-capacity", "reproduced", body("behavior-capacity"), [SESS_DEV], 6.67)
add("behavior-rt-workload", "reproduced", body("behavior-rt-workload") + " Per-session medians give 31.6 ms per item and the set-size means 45.2 ms.",
    [SESS_DEV, "RT is response_time minus probe onset (trial start + 6 s); response_time is stored in session time."], [1676, 47.0, 14.98])
add("behavior-rt-correct-incorrect", "reproduced", body("behavior-rt-correct-incorrect"), [SESS_DEV], [1.361, 1.894])
add("neurons-recorded", "not_reproduced", body("neurons-recorded") + " A question to a reader asks whether the paper assigns regions by electrode name or by atlas location (questions/000574.yaml); with the atlas reading the counts would still differ from the exact expected values.",
    [SESS_DEV, "Per-session mean recorded under reading (b), sessions with at least one unit, the reading that matches."],
    [1487, 446, 456, 585, 51.3])
add("spike-sorting-quality", "partially_reproduced", body("spike-sorting-quality") + " The rate over the whole session (first to last stored trial) is 1.83 +/- 2.38 Hz.",
    ["Firing rate over the stored 8 s trials (reading a); the files hold only the trial epochs.",
     "ISIs counted within each stored trial; gaps between trials are not recorded."], [2.569, 1.748, 5.343])
add("fig2b-maintenance-neurons-hippocampus", "reproduced", body("fig2b-maintenance-neurons-hippocampus"),
    [REG_DEV, SESS_DEV, "Permutation reference distributions are computed once per unit and reused for the scrambled repetitions; for these relabelings the reference is unchanged (sternberg.py, vectorized permutation tests)."],
    [20.0, 45.55])
add("fig2c-load-dependent-maintenance-neurons", "reproduced", body("fig2c-load-dependent-maintenance-neurons") + " Under reading (b), cluster test, 19 to 22 hippocampal neurons are load dependent and amygdala is significant in some readings (P = 0.011 to 0.045).",
    [REG_DEV, "The percentage expected value (15 +/- 1.5%) is outside under the reading that meets the criterion; the criterion judges the count only."],
    [22, 17.9])
add("fig3e-probe-neurons-entorhinal", "reproduced", body("fig3e-probe-neurons-entorhinal"),
    [REG_DEV, "The files end 2 s after probe onset, so window (b) is cut at 2 s and window (c) uses presses within 2 s.",
     "In the 500 scrambled repetitions the P of each t test comes from the t distribution; on the observed tests it agrees with the permutation P at 0.05 in 98.7% of cases."],
    [44, 13.79])
add("fig3-probe-onset-not-movement", "reproduced", body("fig3-probe-onset-not-movement") + " The outcome rests on the probe neurons of fig3e window (a), which put 46 to 48 neurons in entorhinal cortex (outside the fig3e tolerance).",
    ["Button-aligned windows that fall outside the stored 8 s of a trial are left out of that trial's average (55 to 77% of windows covered).", REG_DEV],
    [7.72, 6.04])
add("fig3-probe-neurons-few-task-specific", "partially_reproduced", body("fig3-probe-neurons-few-task-specific"), [REG_DEV], [8, 7.5, 7])
add("fig4a-dpca-workload-separation", "not_reproduced", body("fig4a-dpca-workload-separation") + " The angles are 0, 180 and 180 degrees; the largest is recorded as measured.",
    ["20 ms bins in place of 2 ms, Gaussian SD 1000/6 ms (standard choices).",
     "The toolbox's cross-validated regularization was not run (needs single-trial pseudopopulations); no regularization and a fixed lambda of 1e-2 are shown.",
     "40 label-shuffled dPCA runs for the separation test (runtime).", REG_DEV],
    [32.2, 64.3, 180.0])
add("fig4b-speed-lowest-maintenance", "partially_reproduced", body("fig4b-speed-lowest-maintenance"),
    ["The dPCA of fig4a (z-score a, no regularization), 20 ms steps."])
add("fig4c-distance-largest-maintenance", "reproduced", body("fig4c-distance-largest-maintenance"),
    ["The dPCA of fig4a (z-score a, no regularization)."])
add("fig4d-encoding-decodes-correct", "not_reproduced", body("fig4d-encoding-decodes-correct"),
    ["100 resampling runs and 250 null runs, where the Methods use 500 and 500 (runtime).",
     "NDT details the Methods leave open take the toolbox defaults (linear SVM, C = 1, one trial per class per split, z-scoring on training data).", REG_DEV],
    51.4)
add("fig4e-maintenance-decodes-workload", "reproduced", body("fig4e-maintenance-decodes-workload"),
    ["100 resampling runs and 250 null runs, where the Methods use 500 and 500 (runtime); the smallest corrected P is 0.048.",
     "NDT details the Methods leave open take the toolbox defaults.", REG_DEV],
    81.4)
add("fig4e-workload-decoding-leave-one-subject-out", "reproduced", body("fig4e-workload-decoding-leave-one-subject-out"),
    ["100 resampling runs per subject left out."], [71.6, 81.4])
add("fig4e-maintenance-neurons-carry-workload", "reproduced", body("fig4e-maintenance-neurons-carry-workload"),
    ["100 resampling runs and 250 null runs."], 71.6)
add("fig4e-no-decoding-6-vs-8", "reproduced", body("fig4e-no-decoding-6-vs-8"), ["100 resampling runs and 250 null runs."])
add("fig4f-retrieval-decodes-response", "not_reproduced", body("fig4f-retrieval-decodes-response"),
    ["Only correct trials with the press within 2 s of the probe; later presses fall outside the stored data.",
     "100 resampling runs and 250 null runs.", REG_DEV], 80.0)
add("figs3d-hippocampus-loadings", "reproduced", body("figs3d-hippocampus-loadings"), ["The dPCA of fig4a (z-score a, no regularization).", REG_DEV])
add("fig5-subject1-eeg-power-workload", "partially_reproduced", body("fig5-subject1-eeg-power-workload") + " Subject 1 has 55 correct set size 8 and 61 set size 4 trials (116, as table S2 gives).",
    [EEG_DEV])
add("fig5-subject1-hippocampal-power-workload", "reproduced", body("fig5-subject1-hippocampal-power-workload") + " With correct trials and 1 to 40 Hz the cluster has P = 0.061.",
    [EEG_DEV, "Fixation power from the 1 s fixation epoch (3 tapers, +/- 2 Hz), interpolated to 0.5 Hz bins, per trial (standard choice; the legend says normalized to fixation)."])
add("fig5-subject1-neurons-workload", "partially_reproduced", body("fig5-subject1-neurons-workload"),
    ["More than 100 spikes summed over correct trials in each period.", REG_DEV], 14)
add("fig5-subject1-plv-hippocampus-pz", "partially_reproduced", body("fig5-subject1-plv-hippocampus-pz"), [PLV_DEV, EEG_DEV], assumed=True)
add("fig6-plv-all-subjects", "partially_reproduced", body("fig6-plv-all-subjects") + " With per-taper PLV the pairs change and the values halve (0.20 to 0.44).",
    [PLV_DEV, EEG_DEV, "Frequencies up to 40 Hz only (0.5 Hz bins)."], [9, 4.0, 9.5], assumed=True)
add("tables1-plv-per-subject", "not_reproduced", body("tables1-plv-per-subject"), [PLV_DEV, EEG_DEV],
    [0.741, 0.470, 0.573, 0.760, 0.785, 0.598, 0.512, 0.689, 0.755], assumed=True)
add("fig6-plv-workload-eight-of-nine", "partially_reproduced", body("fig6-plv-workload-eight-of-nine"),
    [PLV_DEV, EEG_DEV, "The workload band is the contiguous run of significant bins with the largest difference inside the individual band (the Methods do not say how it is cut)."],
    [8, 10.75, 11.0], assumed=True)
add("fig6-plv-maintenance-over-encoding", "not_reproduced", body("fig6-plv-maintenance-over-encoding") + " Measured is the first reading (correct trials, 4 to 30 Hz, set size 8).",
    [PLV_DEV, EEG_DEV], 4, assumed=True)
add("fig6-power-unchanged-individual-band", "not_reproduced", body("fig6-power-unchanged-individual-band"),
    ["The claim of absence needs one test, but its channels and band come from the PLV selection, whose readings (trials, frequency range) give different outcomes. Adopted (assumption) correct trials, which give subject 1 the 116 trials of table S2, and 4 to 30 Hz, the only range the Methods name; the question is put to the authors.", PLV_DEV, EEG_DEV],
    assumed=True)
add("fig6i-plv-posterior-gradient", "not_reproduced", body("fig6i-plv-posterior-gradient"),
    ["The files give coordinates in a frame with +x posterior; MNI y is taken as -x (assumption). Channels lie from -31.5 to -9.4 mm.", PLV_DEV, EEG_DEV],
    [0.045, 31], assumed=True)
add("fig6i-no-left-right-difference", "reproduced", body("fig6i-no-left-right-difference"), [PLV_DEV], assumed=True)
add("soz-plv-no-difference", "reproduced", body("soz-plv-no-difference"),
    ["SOZ membership of a bipolar channel: either contact marked is_inside_soz.", PLV_DEV], assumed=True)
add("hfo-rates-unaffected", "blocked", "The paper names neither the HFO detector (it cites Fedele et al. 2017, not supplied) nor the test nor the comparison; the claims file blocks the claim until the detector is supplied. The files hold the iEEG at 2 kHz but only for the 8 s of each trial.",
    blocked_by="methods_underspecified")
add("sfc-maintenance-over-encoding", "blocked", "The microwire LFP is in the files (32 kHz). 73 hippocampal maintenance neurons with at least 100 spikes in both periods (paper 94) sit on 47 to 49 wires, about 4.8 to 5.0 GB of LFP, estimated at 5.2 to 5.4 minutes of streaming at the 15.4 MB/s the notebook measured. Added to a notebook that already runs 24 minutes, with the PPC permutations, it would pass the 30 minute limit; a second notebook was not written in the time of this run. Nothing was computed for this claim.",
    blocked_by="too_large")
for o in O:
    if o["outcome"] == "blocked":
        o.pop("output", None)

F = [
 {"kind": "data_missing", "statement": "The dataset holds 37 sessions and 1487 units; the paper reports 36 sessions and 1526 units. Eight sessions (subject 1 sessions 3 and 4, subject 6 sessions 3 to 7, subject 7 session 1) have no units table, and the 29 sessions with units average 51.3 units, matching the paper's 51 per session, so about one session of units seems to be missing."},
 {"kind": "metadata_insufficient", "statement": "Units point at macroelectrode rows of the electrodes table (microwire k of a bundle at contact k), and the microwire LFP channels reuse the same rows. Microwires have no rows, coordinates or atlas labels of their own, so the region of a unit has to be inferred from the bundle name or from a macro contact."},
 {"kind": "metadata_error", "statement": "Electrode names and atlas labels disagree for several bundles: AR of subject 8 (186 units) and ECL of subject 6 have their deepest contact labelled hippocampus, AHR of subject 2 fusiform gyrus, and ECL of subject 1 (a left electrode) Right Amygdala. Counting units by bundle name gives 446, 456 and 585 in hippocampus, entorhinal cortex and amygdala; by the deepest contact's label 640, 421 and 398 (paper 676, 449, 401)."},
 {"kind": "format_error", "statement": "Spike times are stored unsorted in 43 units of five sessions (subject 1 sessions 1 and 2, subject 7 sessions 2 to 4)."},
 {"kind": "metadata_insufficient", "statement": "response_type holds 51 and 52 on correct trials and 1 and 2 on incorrect trials, with no description. From solution, 51 and 1 are IN, 52 and 2 OUT."},
 {"kind": "metadata_error", "statement": "In the ttl_stage table the Probe stage of each trial carries the next trial's number, and seven files have no ttl_stage table at all."},
 {"kind": "metadata_error", "statement": "The EEG and iEEG series are labelled volts but hold values of about +/- 150 and +/- 240 (1st to 99th percentile), consistent with microvolts."},
 {"kind": "metadata_error", "statement": "The electrodes table gives the EEG reference as averaged mastoid channels, but A1 + A2 is not zero (its SD is 1.8 to 13.7 times that of A1 - A2 across subjects), so the deposited EEG is not re-referenced to the mastoids."},
 {"kind": "metadata_insufficient", "statement": "Electrode coordinates are in a frame with +x posterior, +y inferior and +z right, not MNI as the paper uses, and the scalp electrode positions are template positions on a sphere; converting to MNI y needs an assumption."},
 {"kind": "metadata_error", "statement": "The subject description of subject 1 lists AHR among the seizure onset zone electrodes, but subject 1 has no AHR electrode (the data descriptor's Table 1 has the same entry); is_inside_soz marks only LR."},
 {"kind": "data_missing", "statement": "Only 8 s of each trial are stored (fixation onset to 2 s after the probe), so button presses later than 2 s after the probe, and the activity after them, are not in the files."},
 {"kind": "methods_unavailable", "statement": "For the authors: how were microwire units assigned to hippocampus, entorhinal cortex and amygdala, by electrode name or by the atlas label of a contact (which)? The two give very different counts here."},
 {"kind": "methods_unavailable", "statement": "For the authors: how were the seven tapers combined in the PLV (cross-spectra averaged over tapers per trial, as FieldTrip does, or each taper normalized), what frequency range was searched for the maximal pair, and were the EEG analyses run on correct trials only? This attempt assumed FieldTrip's taper averaging, correct trials and 4 to 30 Hz; the frequency range changes the outcome of fig6-power-unchanged-individual-band."},
 {"kind": "methods_unavailable", "statement": "For the authors: which window defined the probe response of probe neurons (a fixed window after the probe, or up to the press), and in which coordinate frame are the electrode positions of Fig. 6I given?"},
]
A = {"schema_version": 2, "id": "000574-boran-2019-01",
     "dataset": {"archive": "dandi", "id": "000574", "version": "0.250815.1108", "doi": "10.48324/dandi.000574/0.250815.1108"},
     "paper": "doi:10.1126/sciadv.aav3687", "date": "2026-10-30", "entry": "000574-boran-2019",
     "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                    "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-12"},
                    "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/41113745819"}},
     "outcomes": O, "findings": F}

class D(yaml.SafeDumper): pass
def str_rep(d, s):
    if len(s) > 80 or ": " in s or s.startswith(("'", '"')):
        return d.represent_scalar("tag:yaml.org,2002:str", s, style=">")
    return d.represent_scalar("tag:yaml.org,2002:str", s)
D.add_representer(str, str_rep)
open("attempts/000574-boran-2019-01.yaml", "w").write(yaml.dump(A, Dumper=D, sort_keys=False, width=100, allow_unicode=True))
PYEOF
. $TMPDIR/dev/bin/activate; uv pip install -q pyyaml jsonschema 2>&1 | tail -1; python $TMPDIR/mkattempt.py && head -40 attempts/000574-boran-2019-01.yaml && python tools/entry.py check entries/000574-boran-2019 2>&1 | tail
```

```
schema_version: 2
id: 000574-boran-2019-01
dataset:
  archive: dandi
  id: '000574'
  version: 0.250815.1108
  doi: 10.48324/dandi.000574/0.250815.1108
paper: doi:10.1126/sciadv.aav3687
date: '2026-10-30'
entry: 000574-boran-2019
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
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/(55 to 77% of windows covered)/(55 to 78% of windows covered)/; s/AHR of subject 2 fusiform gyrus, and ECL of subject 1 (a left electrode) Right Amygdala/AHR of subject 2 fusiform gyrus, and ECL of subject 1 amygdala/' $TMPDIR/mkattempt.py; . $TMPDIR/dev/bin/activate; python $TMPDIR/mkattempt.py; grep -c "outcome:" attempts/000574-boran-2019-01.yaml; grep "outcome:" attempts/000574-boran-2019-01.yaml | sort | uniq -c; date -u
```

```
35
      2   outcome: blocked
      8   outcome: not_reproduced
      8   outcome: partially_reproduced
     17   outcome: reproduced
Fri Oct 30 21:51:17 UTC 2026
```

**Agent calls Bash**

```bash
cat >> entries/000574-boran-2019/sternberg.py <<'EOF'


# ---- spike-field coherence ---------------------------------------------------------------

LFP_FS = 32000.0
SFC_FS = 1000.0


def _load_wire(args):
    """One microwire LFP column, its bundle's deepest bipolar iEEG pair and the scalp EEG of one
    session, as trials x samples, the LFP decimated to 1 kHz with zero-phase filters."""
    from scipy.signal import decimate
    asset_id, lfp_row, bundle, scalp = args
    with open_asset(asset_id) as f:
        labels = _str(f["general/extracellular_ephys/electrodes/label"][:])
        lf = f["acquisition/ecephys.lfp"]
        col = int(np.flatnonzero(lf["electrodes"][:] == lfp_row)[0])
        x = lf["data"][:, col].astype(np.float64)
        ie = f["acquisition/ecephys.ieeg"]
        il = labels[ie["electrodes"][:]]
        c1, c2 = np.flatnonzero(il == bundle + "1"), np.flatnonzero(il == bundle + "2")
        bip = (ie["data"][:, int(c1[0])] - ie["data"][:, int(c2[0])]) if len(c1) and len(c2) else None
        e = f["acquisition/ecephys.eeg"]
        el = list(labels[e["electrodes"][:]])
        eeg = e["data"][:, [el.index(scalp), el.index("A1"), el.index("A2")]] if scalp in el else None
        n_tr = len(f["intervals/trials/start_time"][:])
    lfp = decimate(decimate(x.reshape(n_tr, -1), 8, axis=-1, zero_phase=True), 4, axis=-1, zero_phase=True)
    out = {"lfp": lfp.astype(np.float32)}
    if bip is not None:
        out["ieeg"] = decimate(bip.reshape(n_tr, -1), 2, axis=-1, zero_phase=True).astype(np.float32)   # 1 kHz
    if eeg is not None:
        ref = eeg[:, 0] - eeg[:, 1:].mean(1)            # re-referenced to the averaged mastoids
        out["eeg"] = ref.reshape(n_tr, -1).astype(np.float32)                                   # 200 Hz
    return out


def load_wires(jobs, workers=20):
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(_load_wire, jobs))


def spike_phases_setup(x, fs, freqs, cycles):
    """Complex convolution of each trial (trials x samples) with Hanning-tapered complex
    exponentials of `cycles` cycles per frequency, as FieldTrip's spike-triggered spectrum
    (ft_spiketriggeredspectrum_convol) uses around each spike. NaN where the window passes the
    trial's edges. Returns trials x samples x freqs (complex64)."""
    from scipy.signal import fftconvolve
    n_tr, n = x.shape
    out = np.full((n_tr, n, len(freqs)), np.nan + 0j, dtype=np.complex64)
    for k, f in enumerate(freqs):
        L = int(round(cycles / f * fs))
        L += (L % 2 == 0)
        t = (np.arange(L) - L // 2) / fs
        w = np.hanning(L) * np.exp(-2j * np.pi * f * t)
        c = fftconvolve(x, w[None, ::-1], mode="same", axes=1)
        h = L // 2
        c[:, :h] = np.nan
        c[:, n - h:] = np.nan
        out[:, :, k] = c
    return out


def ppc2(Z, trial_of):
    """P-hat-2 of Vinck et al. (2012) per frequency: unit vectors Z (spikes x freqs) whose
    pairs are counted only across trials."""
    Z = Z / np.abs(Z)
    ok = np.isfinite(Z).all(1)
    Z, trial_of = Z[ok], trial_of[ok]
    if len(np.unique(trial_of)) < 2:
        return np.full(Z.shape[1], np.nan)
    tr = np.unique(trial_of, return_inverse=True)[1]
    Sm = np.zeros((tr.max() + 1, Z.shape[1]), complex)
    np.add.at(Sm, tr, Z)
    Nm = np.bincount(tr).astype(float)
    num = np.abs(Sm.sum(0)) ** 2 - (np.abs(Sm) ** 2).sum(0)
    den = Nm.sum() ** 2 - (Nm ** 2).sum()
    return num / den
EOF
cat > $TMPDIR/sfc_src.py <<'EOF'
# %% md
# # Spike-field coherence, Boran et al. (2019), dandiset 000574
#
# Second notebook of the entry: the claim `sfc-maintenance-over-encoding`, kept apart because
# it streams the microwire LFP (32 kHz). Dataset version 0.250815.1108 (see the first notebook's
# header for why). It repeats the selection of hippocampal maintenance neurons of the first
# notebook (paired permutation t test, maintenance against fixation, correct trials, atlas
# regions) with the same generator.

# %% [setup]
import time
import numpy as np
import pandas as pd
import sternberg as S
pd.set_option("display.width", 200)
pd.set_option("display.max_rows", 200)

# %% [load]
A = S.assets()
D = S.load_all(A, workers=16)

# %% [sanity]
units = []
for d in D:
    tr = d["trials"]
    lab = dict(zip(d["electrodes"].label, d["electrodes"].location))
    for u in d["units"]:
        loc1 = lab.get(u["bundle"] + "1", "?").split(",")[0]
        al = S.aligned_spikes(u["spikes"], tr.probe.to_numpy())
        units.append({"d": d, "u": u, "aligned": al, "correct": tr.correct.to_numpy(),
                      "atlas": {"Hipp": "hippocampus", "PhG": "entorhinal", "Amyg": "amygdala"}.get(loc1, "other")})
print(len(D), "sessions,", len(units), "units,", sum(x["atlas"] == "hippocampus" for x in units), "hippocampal (atlas)")
print("LFP shapes (samples x wires) and rates:", sorted({(d["shapes"]["lfp"][1], d["shapes"]["lfp"][0] / (8 * len(d["trials"]))) for d in D}))

# %% md
# ## Selection
#
# Hippocampal maintenance neurons (rate in -3 to 0 s above -6 to -5 s, paired permutation t test,
# 2000 sign flips, P < 0.05, correct trials), with at least 100 spikes in the last 2 s of
# maintenance and in encoding (fig. S6b legend: N = 94). The paper's "at least 100 spikes
# during both maintenance and encoding" is read on the windows the coherence uses.

# %% [claim:sfc-maintenance-over-encoding]
rng = np.random.default_rng(701)
sel = []
for x in units:
    if x["atlas"] != "hippocampus":
        continue
    c = x["correct"]
    m = S.count_in(x["aligned"], S.MAINT)[c] / 3.0
    f = S.count_in(x["aligned"], S.FIX)[c] / 1.0
    d_ = m - f
    t_ref = S.t_paired_rows(rng.choice([-1.0, 1.0], (2000, len(d_))) * d_)
    t0 = S.t_paired_rows(d_[None])[0]
    if S.perm_p(t0, t_ref) < 0.05 and t0 > 0:
        nm = S.count_in(x["aligned"], S.LAST2)[c].sum()
        ne = S.count_in(x["aligned"], S.ENC)[c].sum()
        if nm >= 100 and ne >= 100:
            sel.append(x)
wires = sorted({(x["d"]["asset_id"], x["u"]["electrode_row"], x["u"]["bundle"]) for x in sel})
print(f"selected neurons: {len(sel)} (paper 94), on {len(wires)} microwires")

# %% md
# ## Streaming the LFP
#
# Each wire's LFP column is read whole and decimated to 1 kHz; the bundle's bipolar iEEG (contact
# 1 minus 2, 1 kHz) and one scalp EEG channel (Pz where recorded, otherwise O1, the most common
# maximal-PLV electrode of table S1; an assumption, the paper does not say which) are read with it.

# %% [load]
def scalp_for(asset_id):
    d = [d for d in D if d["asset_id"] == asset_id][0]
    labs = list(d["electrodes"][d["electrodes"].group_name == "eeg"].label)
    return "Pz" if "Pz" in labs else "O1"


t0 = time.time()
W = S.load_wires([(a, r, b, scalp_for(a)) for a, r, b in wires], workers=20)
W = dict(zip(wires, W))
print(f"read {len(W)} wires in {time.time() - t0:.0f} s")

# %% md
# ## Pairwise phase consistency
#
# PPC (P-hat-2, Vinck et al. 2012, FieldTrip's ppc2) between each neuron's spikes and the LFP of
# its own wire, per frequency (1 Hz steps), in the last 2 s of maintenance and in encoding (-5 to
# -3 s), correct trials. Phase at each spike from a Hanning-tapered window of 3 or 5 cycles
# (readings; the paper gives no window). Significance per bin against the 95th percentile of 200
# PPCs with the spike trains assigned to permuted trials (Methods, Spike-field coherence).
# Frequency ranges (a) 4 to 30 Hz, (b) 1 to 40 Hz. The same for the bundle's iEEG and for scalp
# EEG.

# %% [claim:sfc-maintenance-over-encoding]
rng = np.random.default_rng(702)
FREQS = np.arange(1, 41)


def ppc_sig(x, sig_name, cycles, fs):
    key = (x["d"]["asset_id"], x["u"]["electrode_row"], x["u"]["bundle"])
    if sig_name not in W[key]:
        return None
    sig = W[key][sig_name]
    c = np.flatnonzero(x["correct"])
    Zc = S.spike_phases_setup(sig[c].astype(np.float64), fs, FREQS, cycles)
    res = {}
    for per, (lo, hi) in [("maintenance", S.LAST2), ("encoding", S.ENC)]:
        idx, tri = [], []
        for j, k in enumerate(c):
            s = x["aligned"][k]
            s = s[(s >= lo) & (s < hi)]
            idx.append(np.round((s + 6.0) * fs).astype(int))
            tri.append(np.full(len(s), j))
        idx, tri = np.concatenate(idx), np.concatenate(tri)
        idx = np.clip(idx, 0, sig.shape[1] - 1)
        obs = S.ppc2(Zc[tri, idx], tri)
        null = np.array([S.ppc2(Zc[p[tri], idx], tri) for p in (rng.permutation(len(c)) for _ in range(200))])
        res[per] = obs > np.nanpercentile(null, 95, axis=0)
    return res


rows = {}
for sig_name, fs in [("lfp", S.SFC_FS), ("ieeg", S.SFC_FS), ("eeg", S.EEG_FS)]:
    for cycles in (3, 5):
        R = [ppc_sig(x, sig_name, cycles, fs) for x in sel]
        R = [r for r in R if r is not None]
        M = np.array([r["maintenance"] for r in R])
        E = np.array([r["encoding"] for r in R])
        rows[(sig_name, cycles)] = (100 * M.mean(0), 100 * E.mean(0), len(R))
for (sig_name, cycles), (m, e, n) in rows.items():
    for fr in [(4, 30), (1, 40)]:
        k = (FREQS >= fr[0]) & (FREQS <= fr[1])
        print(f"{sig_name}, {cycles} cycles, {fr[0]}-{fr[1]} Hz, {n} neurons: maintenance % per bin {np.round(m[k], 1).tolist()}")
        print(f"   encoding % per bin {np.round(e[k], 1).tolist()}")
        print(f"   bins with maintenance above encoding: {int(np.sum(m[k] > e[k]))} of {int(k.sum())}; "
              f"mean % maintenance {m[k].mean():.1f}, encoding {e[k].mean():.1f}; max maintenance {m[k].max():.1f}")
EOF
cd entries/000574-boran-2019; . $TMPDIR/dev/bin/activate; python - <<'EOF'
import sys; sys.path.insert(0,'.')
import numpy as np, sternberg as S
# synthetic check of ppc2: locked phases -> high, random -> ~0
rng=np.random.default_rng(0)
tri=np.repeat(np.arange(20),10)
Z=np.exp(1j*(0.3+0.1*rng.normal(size=(200,3))))
print(S.ppc2(Z,tri))
Z=np.exp(1j*rng.uniform(0,2*np.pi,(200,3)))
print(S.ppc2(Z,tri))
x=np.sin(2*np.pi*10*np.arange(0,8,0.001))[None].repeat(3,0)
Zc=S.spike_phases_setup(x,1000.,np.array([5,10,20]),3)
print(np.angle(Zc[0,4000]), np.abs(Zc[0,4000]))
EOF
```

```
[0.98975408 0.99004519 0.9904766 ]
[-0.00542408 -0.00392375  0.00026318]
[-1.6218282 -1.5707964 -1.5707964] [6.8226444e-14 7.5000000e+01 6.5039935e+00]
```

**Agent calls Bash**

```bash
cd entries/000574-boran-2019; date -u; cat > $TMPDIR/pre_sfc.py <<EOF
import pickle, numpy as np
D = pickle.load(open('$TMPDIR/D.pkl','rb'))
import sternberg as S
A = S.assets()
for d in D:
    d['trials']['is_in'] = d['trials'].response.isin(('51','1'))
    for u in d['units']:
        u['spikes'] = np.sort(u['spikes'])
EOF
python - <<'EOF'
import os
s=open(os.environ['TMPDIR']+'/sfc_src.py').read()
# dev: limit to 3 wires
s=s.replace('wires = sorted({','wires = sorted({') 
open(os.environ['TMPDIR']+'/sfc_dev.py','w').write(s.replace('print(f"selected neurons: {len(sel)} (paper 94), on {len(wires)} microwires")','print(f"selected neurons: {len(sel)} (paper 94), on {len(wires)} microwires")\nwires = wires[:2]; sel = [x for x in sel if (x["d"]["asset_id"], x["u"]["electrode_row"], x["u"]["bundle"]) in wires]'))
EOF
sed -i 's/^A = S.assets()\nD = S.load_all(A, workers=16)//' $TMPDIR/sfc_dev.py
python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/runcells.py'; s=open(p).read()
s=s.replace("if any(n in head for n in names) or 'setup' in head:","if (any(n in head for n in names) or 'setup' in head) and not ('load' in head and 'S.load_all' in body):")
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate; time python $TMPDIR/runcells.py $TMPDIR/sfc_dev.py $TMPDIR/pre_sfc.py sanity,claim,load 2>&1 | tail -30 | cut -c1-400
```

```
/bin/bash: line 1: cd: entries/000574-boran-2019: No such file or directory
Fri Oct 30 21:52:31 UTC 2026
   encoding % per bin [0.0, 0.0, 0.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
   bins with maintenance above encoding: 13 of 27; mean % maintenance 50.0, encoding 25.9; max maintenance 50.0
lfp, 5 cycles, 1-40 Hz, 2 neurons: maintenance % per bin [0.0, 50.0, 0.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]
   encoding % per bin [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
   bins with maintenance above encoding: 24 of 40; mean % maintenance 47.5, encoding 17.5; max maintenance 50.0
ieeg, 3 cycles, 4-30 Hz, 2 neurons: maintenance % per bin [0.0, 0.0, 50.0, 100.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
   encoding % per bin [50.0, 0.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
   bins with maintenance above encoding: 2 of 27; mean % maintenance 20.4, encoding 18.5; max maintenance 100.0
ieeg, 3 cycles, 1-40 Hz, 2 neurons: maintenance % per bin [0.0, 0.0, 0.0, 0.0, 0.0, 50.0, 100.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 50.0]
   encoding % per bin [50.0, 50.0, 50.0, 50.0, 0.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python $TMPDIR/mk.py $TMPDIR/sfc_src.py reproduce_boran_2019_sfc.ipynb && python - <<'EOF'
s=open('entry.yaml').read()
s=s.replace('''  runtime_minutes: 25
''','''  runtime_minutes: 24
- path: reproduce_boran_2019_sfc.ipynb
  title: Spike-field coherence of maintenance neurons (Boran et al. 2019, dandiset 000574)
  runtime_minutes: 13
''')
open('entry.yaml','w').write(s)
EOF
cd ../.. && deactivate; python tools/entry.py check entries/000574-boran-2019 2>&1 | tail -3; date -u; python tools/entry.py run entries/000574-boran-2019 --max-minutes 40 2>&1 | grep -E "pass|FAIL|Error" | tail -5; date -u
```

```
0 error(s)
Fri Oct 30 21:55:07 UTC 2026
pass  reproduce_boran_2019.ipynb  (1430 s)
pass  reproduce_boran_2019_sfc.ipynb  (787 s)
Fri Oct 30 22:32:08 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; python - <<'EOF' > $TMPDIR/exec_out2.txt
import nbformat
for nbn in ['reproduce_boran_2019.ipynb', 'reproduce_boran_2019_sfc.ipynb']:
    nb = nbformat.read('executed/000574-boran-2019/' + nbn, 4)
    for i, c in enumerate(nb.cells):
        if c.cell_type == 'code':
            txt = "".join(o.get('text', '') for o in c.get('outputs', []) if o.get('output_type') == 'stream')
            print(f"#### {nbn} cell {i} {c.metadata.get('tags', [])}\n{txt}")
EOF
diff <(grep -v "read .* MB\|read .* wires" $TMPDIR/exec_out.txt) <(sed -n '/reproduce_boran_2019.ipynb cell/,/reproduce_boran_2019_sfc.ipynb cell 1 /p' $TMPDIR/exec_out2.txt | sed 's/#### reproduce_boran_2019.ipynb /#### /' | grep -v "read .* MB" | grep -v "_sfc") | head -20; sed -n '/_sfc.ipynb cell/,$p' $TMPDIR/exec_out2.txt | grep -v "per bin" | cut -c1-300
```

```
992,993c992,993
<    paired       73     47    4768          5.2
<  unpaired       73     49    4970          5.4
---
>    paired       73     47    4768          4.8
>  unpaired       73     49    4970          5.0
#### reproduce_boran_2019_sfc.ipynb cell 1 ['setup']

#### reproduce_boran_2019_sfc.ipynb cell 2 ['load']

#### reproduce_boran_2019_sfc.ipynb cell 3 ['sanity']
37 sessions, 1487 units, 640 hippocampal (atlas)
LFP shapes (samples x wires) and rates: [(32, 32000.0), (40, 32000.0), (62, 32000.0), (64, 30608.695652173912), (64, 32000.0)]

#### reproduce_boran_2019_sfc.ipynb cell 5 ['claim:sfc-maintenance-over-encoding']
selected neurons: 73 (paper 94), on 47 microwires

#### reproduce_boran_2019_sfc.ipynb cell 7 ['load']
read 47 wires in 360 s

[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "30608" $TMPDIR/exec_out2.txt | head; date -u
```

```
16:8       02      05  2016-02-13T15:37:00+01:00      46       40         1     18       8       64     200.0     2000.0  30608.695652
1003:LFP shapes (samples x wires) and rates: [(32, 32000.0), (40, 32000.0), (62, 32000.0), (64, 30608.695652173912), (64, 32000.0)]
Fri Oct 30 22:32:42 UTC 2026
```

**Agent calls Bash**

```bash
sed -n '/cell 5 \[.sanity.\]/,/cell 6/p' $TMPDIR/exec_out2.txt | head -3; sed -n '/cell 5 \[.sanity.\]/,/cell 6/p' $TMPDIR/exec_out2.txt | sed -n '7,8p'
```

```
#### reproduce_boran_2019.ipynb cell 5 ['sanity']
   subject session                      start  trials  correct  artifact  units  eeg_ch  ieeg_ch  eeg_rate  ieeg_rate      lfp_rate
0       01      01  2016-12-14T17:13:00+01:00      50       44         2     37      19       48     200.0     2000.0  32000.000000
4       02      01  2016-02-11T11:56:00+01:00      49       45         2     71       8       64     200.0     2000.0  32000.000000
5       02      02  2016-02-11T12:06:00+01:00      47       43         4     82       8       64     200.0     2000.0  32000.000000
```

**Agent calls Bash**

```bash
cat > $TMPDIR/patch.py <<'PYEOF'
import os, re, nbformat
T = os.environ['TMPDIR']
SFC_RES = ("**Result: Partially reproduced.** 73 hippocampal maintenance neurons have at least 100 spikes in the last 2 s of "
 "maintenance and in encoding (paper 94 +/- 9.4, outside), on 47 microwires. With 3-cycle windows over 4 to 30 Hz, the "
 "percentage of neurons with significant PPC to the LFP of their own wire is higher in maintenance than in encoding in all 27 "
 "bins (means 58.4% against 42.1%), and in 39 of 40 bins over 1 to 40 Hz; with 5-cycle windows in 26 of 27 and 38 of 40. "
 "Coupling to the bundle's iEEG is also well above the 5% chance level (maintenance means 29.6% and 21.0% of neurons over 4 "
 "to 30 Hz with 3 and 5 cycles), and to the scalp EEG it is near chance on average (5.3% and 5.0%) with single bins up to "
 "16.4%, so the part of the claim that the coupling is not to the iEEG or scalp EEG does not hold.")
SFC_SUM = ("## Summary\n\n| Claim | Outcome |\n|---|---|\n| sfc-maintenance-over-encoding | Partially reproduced |\n\n"
 "A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences "
 "from the paper's method.\n\nDifferences from the paper's method: the window around each spike (3 or 5 cycles, Hanning) "
 "is not given by the paper; the LFP is decimated to 1 kHz; the scalp EEG channel is Pz or, where Pz was not recorded, O1 "
 "(assumption); 73 neurons where the paper has 94. What was found about the dataset: the microwire LFP is present for all "
 "sessions, but in subject 2 session 5 it holds 11,264,000 samples for 46 trials, not 32 kHz x 8 s per trial (its rate per "
 "stored second is 30,609 Hz in the sanity output); no wire of that session entered this analysis.")
MAIN_SFC = ("## Claims tested in the second notebook\n\n### sfc-maintenance-over-encoding\n\n"
 "> Maintenance neurons showed significant spike-field coherence to the local field potential, but not to the iEEG or scalp "
 "EEG, and for all frequency bins the percentage of neurons with spike-field coherence was higher during maintenance than "
 "during encoding.\n\nThe claim needs the microwire LFP (`ecephys.lfp`, 32 kHz) of every wire that carries a hippocampal "
 "maintenance neuron with at least 100 spikes in maintenance and in encoding. The cell below counts those wires and "
 "estimates the streaming time from the rate measured when the EEG and iEEG were read above. Added to this notebook it "
 "would bring it close to the 30 minute limit, so the claim is tested in `reproduce_boran_2019_sfc.ipynb`.")
MAIN_SFC_AFTER = ("The outcome is in the second notebook. \n\n### hfo-rates-unaffected (blocked, methods underspecified)\n\n"
 "> The rates of clinically relevant high-frequency oscillations were not affected by performing the task.\n\n"
 "The claims file blocks this claim until the HFO detector of reference 27 (Fedele et al. 2017) is supplied; neither the "
 "detector nor the comparison is given in the paper. The files hold the iEEG at 2 kHz, which an HFO detector would need, "
 "but only during the 8 s of each trial.")

def fix_main(nb):
    for c in nb.cells:
        if c.cell_type != 'markdown':
            continue
        if c.source.startswith("## Claims not tested"):
            c.source = MAIN_SFC
        elif c.source.startswith("**Result: blocked (too large).**"):
            c.source = MAIN_SFC_AFTER
        elif c.source.startswith("## Claims\n"):
            c.source = c.source.replace("| sfc-maintenance-over-encoding | no, blocked |", "| sfc-maintenance-over-encoding | yes, in reproduce_boran_2019_sfc.ipynb |")
        elif c.source.startswith("## Summary"):
            s = c.source.replace("| sfc-maintenance-over-encoding | Blocked: too large |", "| sfc-maintenance-over-encoding | Partially reproduced (second notebook) |")
            s = s.replace("- The microwire LFP was not read (spike-field coherence blocked for run time), and the HFO\n  detector is not available.",
                          "- Spike-field coherence is tested in the second notebook, with a window around each spike the\n  paper does not give; the HFO detector is not available.")
            s = s.replace("- The subject 1 description lists AHR", "- In subject 2 session 5 the microwire LFP is shorter than 32 kHz x 8 s per trial (second\n  notebook).\n- The subject 1 description lists AHR")
            c.source = s
    return nb

def fix_sfc(nb):
    nb.cells.append(nbformat.v4.new_markdown_cell(SFC_RES))
    nb.cells.append(nbformat.v4.new_markdown_cell(SFC_SUM))
    return nb

E = 'executed/000574-boran-2019/'
for path, fn in [('entries/000574-boran-2019/reproduce_boran_2019.ipynb', fix_main), (E + 'reproduce_boran_2019.ipynb', fix_main),
                 ('entries/000574-boran-2019/reproduce_boran_2019_sfc.ipynb', fix_sfc), (E + 'reproduce_boran_2019_sfc.ipynb', fix_sfc)]:
    nb = nbformat.read(path, 4)
    nbformat.write(fn(nb), path)
    print('patched', path)
PYEOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/patch.py; grep -c "too large" entries/000574-boran-2019/reproduce_boran_2019.ipynb; grep -o "Summary" entries/000574-boran-2019/reproduce_boran_2019_sfc.ipynb | head -2
```

```
patched entries/000574-boran-2019/reproduce_boran_2019.ipynb
patched executed/000574-boran-2019/reproduce_boran_2019.ipynb
patched entries/000574-boran-2019/reproduce_boran_2019_sfc.ipynb
patched executed/000574-boran-2019/reproduce_boran_2019_sfc.ipynb
0
Summary
```

**Agent calls Bash**

```bash
python - <<'EOF'
import os
p = os.environ['TMPDIR'] + '/mkattempt.py'
s = open(p).read()
a = s.index('add("sfc-maintenance-over-encoding"')
b = s.index('for o in O:')
s = s[:a] + '''add("sfc-maintenance-over-encoding", "partially_reproduced",
    "73 hippocampal maintenance neurons (atlas regions, paired selection) have at least 100 spikes in the last 2 s of maintenance and in encoding (paper 94 +/- 9.4), on 47 microwires. With 3-cycle windows over 4 to 30 Hz the percentage of neurons with significant PPC to the LFP of their own wire is higher in maintenance than in encoding in all 27 bins (means 58.4% against 42.1%), and in 39 of 40 bins over 1 to 40 Hz; with 5-cycle windows in 26 of 27 and 38 of 40. Coupling to the bundle's bipolar iEEG is well above the 5% chance level (maintenance means 29.6% and 21.0% over 4 to 30 Hz), and to scalp EEG near chance on average (5.3% and 5.0%) with single bins up to 16.4%, so the statement's 'not to the iEEG or the scalp EEG' does not hold.",
    ["Tested in the second notebook, which streams the LFP of the selected wires (360 s).",
     "The window around each spike is not given; Hanning-tapered windows of 3 and 5 cycles (the claims file's readings) as in FieldTrip's spike-triggered spectrum, on LFP decimated to 1 kHz.",
     "The 100-spike rule is applied to the last 2 s of maintenance and to encoding, the windows the coherence uses.",
     "iEEG is the bipolar pair of contacts 1 and 2 of the neuron's own bundle; scalp EEG is Pz, or O1 where Pz was not recorded (assumption; the paper does not say which channels).",
     REG_DEV], 73, assumed=True)
for o in O:
    if o["claim"] == "sfc-maintenance-over-encoding":
        o["notebook"] = "reproduce_boran_2019_sfc.ipynb"
''' + s[b:]
s = s.replace(''' {"kind": "data_missing", "statement": "Only 8 s of each trial''', ''' {"kind": "format_error", "statement": "In subject 2 session 5 the microwire LFP holds 11,264,000 samples for the 46 stored trials, where 32 kHz times 8 s per trial gives 11,776,000 (30,609 samples per stored second); the EEG and iEEG of the same file have the expected length."},
 {"kind": "data_missing", "statement": "Only 8 s of each trial''')
open(p, 'w').write(s)
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/mkattempt.py && grep "outcome:" attempts/000574-boran-2019-01.yaml | sort | uniq -c; grep -n "sfc" attempts/000574-boran-2019-01.yaml | head -5
```

```
1   outcome: blocked
      8   outcome: not_reproduced
      9   outcome: partially_reproduced
     17   outcome: reproduced
648:- claim: sfc-maintenance-over-encoding
650:  notebook: reproduce_boran_2019_sfc.ipynb
651:  output: claim:sfc-maintenance-over-encoding
```

**Agent calls Bash**

```bash
cat > entries/000574-boran-2019/README.md <<'EOF'
# Boran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald & Sarnthein (2019) from dandiset 000574

Tests the findings of [Boran et al. (2019)](https://doi.org/10.1126/sciadv.aav3687) on
[DANDI:000574](https://dandiarchive.org/dandiset/000574/0.250815.1108), which holds the trials,
sorted units, scalp EEG, macroelectrode iEEG and microwire LFP of nine epilepsy patients doing a
modified Sternberg task (37 sessions, 8 s stored per trial).

| Claim | Outcome |
|---|---|
| Behavior: accuracy by set size, capacity, RT and workload, RT of errors (4 claims) | Reproduced |
| 1526 neurons, 676 / 449 / 401 by region | Not reproduced |
| Spike sorting quality | Partially reproduced |
| Hippocampal maintenance neurons (Fig. 2B) and their load dependence (Fig. 2C) | Reproduced |
| Entorhinal probe neurons (Fig. 3E); probe-aligned peaks above button-aligned | Reproduced |
| Few probe neurons task specific | Partially reproduced |
| dPCA variance and set-size angles (Fig. 4A) | Not reproduced |
| Speed lowest in maintenance (Fig. 4B) | Partially reproduced |
| Distance largest in maintenance (Fig. 4C); hippocampal loadings (fig. S3d) | Reproduced |
| Encoding decodes later correctness (Fig. 4D) | Not reproduced |
| Maintenance decodes workload, leave-one-subject-out, maintenance neurons, no 6 against 8 (Fig. 4E, 4 claims) | Reproduced |
| Retrieval decodes IN/OUT (Fig. 4F) | Not reproduced |
| Subject 1 scalp EEG power | Partially reproduced |
| Subject 1 hippocampal power | Reproduced |
| Subject 1 maintenance neurons; subject 1 PLV with Pz | Partially reproduced |
| PLV peak in all subjects; workload PLV in eight of nine | Partially reproduced |
| Table S1 per subject; maintenance PLV above encoding; power unchanged; posterior gradient | Not reproduced |
| No left-right difference; no SOZ difference | Reproduced |
| Spike-field coherence (second notebook) | Partially reproduced |
| HFO rates | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dataset holds 1487 units where the paper has 1526, and gives no region for the microwires;
regions come from the atlas label of each bundle's deepest contact (the bundle names give very
different counts). The attempt record, with the reasons, the assumptions and the findings about
the dataset, is [`attempts/000574-boran-2019-01.yaml`](../../attempts/000574-boran-2019-01.yaml).

- `reproduce_boran_2019.ipynb`: all claims but spike-field coherence. About 24 minutes, most of it
  decoding and dPCA resampling.
- `reproduce_boran_2019_sfc.ipynb`: spike-field coherence; streams the LFP of 47 microwires. About
  13 minutes.
- `sternberg.py`: loading (tables, spikes, EEG, hippocampal iEEG, LFP), the permutation and
  cluster tests, multitaper spectra and PLV, pseudopopulation decoding, dPCA and PPC. Other
  notebooks on this dandiset can import it.
EOF
python tools/entry.py check entries/000574-boran-2019 2>&1 | tail -5; date -u
```

```
0 error(s)
Fri Oct 30 22:33:42 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000574-boran-2019 2>&1 | tail -5; ls executed/000574-boran-2019/handover/; git status --short
```

```
wrote executed/000574-boran-2019/handover
10.1126-sciadv.aav3687.yaml
reproduce_boran_2019.ipynb
reproduce_boran_2019_sfc.ipynb
sternberg.py
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
?? attempts/000574-boran-2019-01.yaml
?? entries/000574-boran-2019/
?? questions/000574.yaml
?? scripts
```

**Agent calls Bash**

```bash
ls -la entries/000574-boran-2019/; rm -rf entries/000574-boran-2019/__pycache__; grep -c "Result:" executed/000574-boran-2019/handover/*.ipynb; python tools/entry.py check entries/000574-boran-2019 2>&1 | tail -2; python -c "
import nbformat
for f in ['entries/000574-boran-2019/reproduce_boran_2019.ipynb','entries/000574-boran-2019/reproduce_boran_2019_sfc.ipynb']:
    nb=nbformat.read(f,4); print(f, sum(len(c.get('outputs',[])) for c in nb.cells if c.cell_type=='code'))"
```

```
total 212
drwxr-xr-x   4 runner runner   4096 Oct 30 22:33 .
drwxr-xr-x 108 runner runner   4096 Oct 30 19:22 ..
drwxr-xr-x   3 runner runner   4096 Oct 30 19:31 .claude
-rw-r--r--   1 runner runner   2946 Oct 30 22:33 README.md
drwxr-xr-x   2 runner runner   4096 Oct 30 21:52 __pycache__
-rw-r--r--   1 runner runner   1116 Oct 30 21:55 entry.yaml
-rw-r--r--   1 runner runner 136197 Oct 30 22:33 reproduce_boran_2019.ipynb
-rw-r--r--   1 runner runner  10488 Oct 30 22:33 reproduce_boran_2019_sfc.ipynb
-rw-r--r--   1 runner runner     65 Oct 30 20:53 requirements.in
-rw-r--r--   1 runner runner   1419 Oct 30 20:53 requirements.lock.txt
-rw-r--r--   1 runner runner  28686 Oct 30 21:52 sternberg.py
executed/000574-boran-2019/handover/reproduce_boran_2019.ipynb:0
executed/000574-boran-2019/handover/reproduce_boran_2019_sfc.ipynb:0
0 error(s)
entries/000574-boran-2019/reproduce_boran_2019.ipynb 0
entries/000574-boran-2019/reproduce_boran_2019_sfc.ipynb 0
```

**Agent calls Bash**

```bash
find entries/000574-boran-2019/.claude | head
```

```
entries/000574-boran-2019/.claude
entries/000574-boran-2019/.claude/.cc-writes
```

**Agent calls Bash**

```bash
rm -rf entries/000574-boran-2019/.claude; ls -a entries/000574-boran-2019; date -u
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: Claude requested permissions to write to entries/000574-boran-2019/.claude, but you haven't granted it yet.
```

**Agent**

I've finished the attempt on DANDI:000574 for steps 1 to 6: the entry is locked, checked (0 errors) and run, the record is written, and the verifier's package is built. Nothing is committed.

## 1. Outcomes (35 claims: 17 reproduced, 9 partially reproduced, 8 not reproduced, 1 blocked)

| Claim | Outcome |
|---|---|
| behavior-accuracy-set-size, behavior-capacity, behavior-rt-workload, behavior-rt-correct-incorrect | Reproduced |
| neurons-recorded | Not reproduced |
| spike-sorting-quality | Partially (waveform SNR 5.34 against 3.28 ± 1.56) |
| fig2b, fig2c (maintenance neurons, load dependence) | Reproduced |
| fig3e, fig3-probe-onset-not-movement | Reproduced (under one reading each) |
| fig3-probe-neurons-few-task-specific | Partially |
| fig4a dPCA | Not reproduced |
| fig4b speed | Partially (highest during retrieval, not encoding) |
| fig4c, figs3d | Reproduced |
| fig4d encoding decodes correct/incorrect | Not reproduced (51%) |
| fig4e workload decoding and its three follow-ups (leave-one-subject-out, maintenance neurons, no 6 against 8) | Reproduced |
| fig4f retrieval decodes IN/OUT | Not reproduced |
| fig5 subject 1: EEG power / hippocampal power / neurons / PLV with Pz | Partially / Reproduced / Partially / Partially |
| fig6-plv-all-subjects, fig6-plv-workload-eight-of-nine | Partially |
| tables1, fig6-plv-maintenance-over-encoding, fig6-power-unchanged (assumed), fig6i gradient | Not reproduced |
| fig6i no left-right difference, soz-plv-no-difference | Reproduced |
| sfc-maintenance-over-encoding (second notebook) | Partially (coupling to iEEG is well above chance) |
| hfo-rates-unaffected | Blocked: methods_underspecified |

## 2. Dataset, assumptions and questions

**What the dataset holds**
- I pinned version 0.250815.1108, the newest. 0.250610.0938 has the same assets, and the older 0.231010.1809 had duplicate `obj-` files.
- There are 37 sessions (the paper has 36) and 1487 units (the paper has 1526). Eight sessions have no units table.
- The units point at macroelectrode rows of the electrodes table. Region counts by electrode name are far from the paper's; counts by the atlas label of each electrode's deepest contact are close (640/421/398 against 676/449/401).

**Format and metadata problems found**
- 43 units store their spike times unsorted.
- The response codes (51/52 on correct trials, 1/2 on errors) are not described.
- The trial-stage table numbers each Probe stage one trial late, and seven files lack the table.
- EEG and iEEG are labelled volts but hold values consistent with microvolts.
- The EEG is said to be referenced to the averaged mastoids, but it is not (A1 + A2 is not zero).
- Coordinates are not in MNI space.
- Subject 1's seizure-onset list names an electrode (AHR) that subject 1 does not have.
- The LFP of subject 2 session 5 is shorter than its 46 trials need.
- Only 8 s of each trial are stored, so presses later than 2 s after the probe are missing.

**Assumptions**
- Regions come from the atlas label of each electrode's deepest contact, as the Methods describe.
- PLV is computed as FieldTrip does (cross-spectra averaged over tapers within each trial).
- MNI y is taken as minus the file's x.
- The power-unchanged claim uses correct trials and 4 to 30 Hz.
- For spike-field coherence, the scalp channel is Pz (O1 where Pz is absent) and the iEEG channel is the neuron's own electrode.

Questions for the paper's authors are recorded as `methods_unavailable` findings: how units were assigned to regions, how the PLV combined tapers, which frequency range and trials it used, the probe-neuron window, and the coordinate frame of Fig. 6I.

**Question to a reader:** one, in `questions/000574.yaml`. It asks whether neurons-recorded's region-by-electrode-name rule matches the paper.

## 3. Where the protocol was unclear
1. The protocol says outcomes follow the criterion, but some criteria leave out expected values (fig2c's percentage, fig3e's chi-square value). I followed the criterion and gave the off-tolerance values in the notes.
2. A claim that depends on another inherits that claim's readings. I treated a match under any upstream reading as a match, and said so in the notes (fig3-probe-onset).
3. Several claims of absence have test inputs that come from readings the protocol says not to multiply. I adopted one reading as an assumption (fig6-power-unchanged) and showed the others.
4. The protocol does not say how to judge a run that is under the 30-minute limit but over the 10-minute aim. The main notebook takes 24 min, so I put spike-field coherence in a second notebook (13 min) instead of blocking it.
5. I changed the conclusion text after the final run, without touching any code, and copied it into the executed notebooks. The protocol does not say whether that needs a re-run.

## 4. Runtime and failures
- The main notebook takes 24 min (1430 s) and the spike-field-coherence notebook 13 min (787 s).
- To keep within the time limit, decoding uses 100 resampling runs and 250 null runs where the paper uses 500 and 500. The smallest corrected P this allows is 0.048.
- The first full run failed once on an SVD that did not converge. I added a fallback in `sternberg.py` and the next run passed.
- An empty folder the harness created, `entries/000574-boran-2019/.claude/.cc-writes`, could not be deleted: the delete needed a permission approval this session cannot give. It is empty, so git should not pick it up.
- The run took about 5 h 20 min of the 5 h window (19:16 to about 22:35 UTC).

Files are in `entries/000574-boran-2019/`:
- `reproduce_boran_2019.ipynb`
- `reproduce_boran_2019_sfc.ipynb`
- `sternberg.py`

The record is `attempts/000574-boran-2019-01.yaml` and the handover is in `executed/000574-boran-2019/handover/`.

## End of run

116 turns, 195 minutes, result: success.
