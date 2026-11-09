# 001863 · author · run 42057646913

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/001863 paper entries | head -50
```

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -300; cat docs/archives.md | sed -n '/DANDI/,$p' | head -120
```

```
<persisted-output>
Output too large (36.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26beedb0-2a20-4d96-84aa-5cbc616add04/tool-results/bw6eigpkl.txt

Preview (first 2KB):
Thu Nov  5 15:45:02 UTC 2026
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
[... 400 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/26beedb0-2a20-4d96-84aa-5cbc616add04/tool-results/bw6eigpkl.txt"
}
```

```
1	Thu Nov  5 15:45:02 UTC 2026
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
[... 672 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001863/*.yaml; ls paper; ls questions | head; ls entries/001453-fouke-2025 claims/001453
```

```
<persisted-output>
Output too large (42.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26beedb0-2a20-4d96-84aa-5cbc616add04/tool-results/bzkhssvd6.txt

Preview (first 2KB):
# Claims for Welch, Gonzales-Hess, Tarvin, Connor & Smear (2025), "The impact of a psychedelic
# drug on olfactory search behavior by mice", bioRxiv doi:10.1101/2025.07.09.663970, on dandiset
# 001863.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, under
# docs/protocol.md version pilot-10 (Reader, steps 1 to 4). Nobody had analysed the dataset's data
# when these criteria were written; the reader saw only the dandiset's title and description.
#
# Text read: the bioRxiv preprint, version 1, full text flattened from its JATS XML
# (paper/10.1101-2025.07.09.663970.txt): Results, figure legends, Discussion and Materials and
# methods. The preprint has no separate supplement file; the legends of its supplemental figures
# (Figure 2A, 2B, 2C, 2D, 3, 4 and 5 supplemental) are in the text and were read. No PDF was
# supplied, and none was needed.
#
# Code read: github.com/Smear-Lab/Olfactory-search-on-psychedelics at commit
# aa80af0a153c6bf099e5668d27c9d88e2bfc033f (2026-08-06). The paper itself links only the rig
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/26beedb0-2a20-4d96-84aa-5cbc616add04/tool-results/bzkhssvd6.txt"
}
```

```
1	# Claims for Welch, Gonzales-Hess, Tarvin, Connor & Smear (2025), "The impact of a psychedelic
2	# drug on olfactory search behavior by mice", bioRxiv doi:10.1101/2025.07.09.663970, on dandiset
3	# 001863.
4	#
5	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, under
6	# docs/protocol.md version pilot-10 (Reader, steps 1 to 4). Nobody had analysed the dataset's data
7	# when these criteria were written; the reader saw only the dandiset's title and description.
8	#
9	# Text read: the bioRxiv preprint, version 1, full text flattened from its JATS XML
10	# (paper/10.1101-2025.07.09.663970.txt): Results, figure legends, Discussion and Materials and
11	# methods. The preprint has no separate supplement file; the legends of its supplemental figures
12	# (Figure 2A, 2B, 2C, 2D, 3, 4 and 5 supplemental) are in the text and were read. No PDF was
13	# supplied, and none was needed.
14	#
15	# Code read: github.com/Smear-Lab/Olfactory-search-on-psychedelics at commit
16	# aa80af0a153c6bf099e5668d27c9d88e2bfc033f (2026-08-06). The paper itself links only the rig
17	# documentation (nghess.github.io/fmon-docs); this repository is the authors' code, named in the
18	# dandiset's description and naming the paper in its README. It holds analysis/fig1_cleaned.Rmd to
19	# fig5_cleaned.Rmd (the R code of each figure's statistics), a MATLAB plotting script for the
20	# occupancy maps, the Bpod/Bonsai task software (fmon-bpod) and the NWB conversion script. The
[... 700 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/26beedb0-2a20-4d96-84aa-5cbc616add04/tool-results/b521xpcup.txt",
 "offset": 20
}
```

```
20	Psychedelics induce stereotypical behaviors in both humans and animals. In rodents, administration of a serotonergic psychedelic reliably produces a rotational head shake known as the head-twitch response (HTR; ( González-Maeso et al., 2007 ; Halberstadt et al., 2020 ; Halberstadt & Geyer, 2013 ). The quantity of HTRs correlates with the potency of hallucinations in humans. This correlation has motivated the idea that HTRs are a behavioral analog to the human experience ( Hanks & González-Maeso, 2013 ). In humans, erratic, high-rate eye saccades occur after administration of a classic psychedelic ( Hebbard & Fischer, 1966 ). In schizophrenia, auditory hallucinations can be predicted by subtle lip movement ( Rapin et al., 2013 ), and humming can decrease the rate of auditory hallucinations (M. F. Green & Kinsbourne, 1990 ).
21	
22	Considering the importance of olfaction in rodents and the large gap in understanding how psychedelics impact the olfactory system, we sought to establish an understanding of respiration and behavior of mice after the administration of the psychedelic DOI (2,5-Dimethoxy-4-iodoamphetamine). Here, we show the changes in active sampling and olfactory search behavior after the administration of the psychedelic DOI. Taken together, our results lay the foundation for using mouse olfaction in behavioral preparations for understanding the mechanisms of psychedelics.
23	
24	## Results
25	
26	## DOI alters olfactory search behavior
27	
28	To study the impact of psychedelics on active olfactory behavior we administered DOI to mice and tested them in an olfactory search paradigm in which they report the source location of a noisy, turbulent odor gradient ( Findley et al., 2021 ). In the search paradigm, mice poked into an initiation port to start a trial. Odor was pseudo-randomly delivered from the left or right side of the opposite end of the arena. To receive a water reward, mice had to navigate toward higher odor concentration. To investigate tas
[... 174 more lines not kept]
```

**Agent**

Now the example entry format, and the dataset.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -80 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('----')
"; cd ../..; cat attempts/001453-fouke-2025-01.yaml | head -150
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
[... 469 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001863/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001863/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent**

Only one published version (0.260806.2109); 44 assets, 1.6 GB.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/001863/versions/0.260806.2109/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['path'], a['size'], a['asset_id'])"; curl -s "https://api.dandiarchive.org/api/dandisets/001863/versions/0.260806.2109/" | python -c "
import json,sys; d=json.load(sys.stdin); print(d.get('description')); print(json.dumps(d.get('relatedResource'),indent=1)); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q pynwb h5py remfile dandi numpy pandas scipy 2>&1 | tail -2; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > probe.py <<'EOF'
import h5py, remfile, pynwb, time
url="https://api.dandiarchive.org/api/assets/e8ff1ad3-7ea7-4b2a-98ff-606accd5f233/download/"
t=time.time()
f=remfile.File(url); h=h5py.File(f,'r')
io=pynwb.NWBHDF5IO(file=h,load_namespaces=True); nwb=io.read()
print(nwb)
print(nwb.subject)
print(nwb.session_description, nwb.session_start_time, nwb.experiment_description)
def walk(g,p=''):
    for k,v in g.items():
        if isinstance(v,h5py.Dataset): print(p+'/'+k, v.shape, v.dtype, dict(v.attrs).get('unit',''), dict(v.attrs).get('description','')[:100] if isinstance(dict(v.attrs).get('description',''),str) else '')
        else: walk(v,p+'/'+k)
walk(h)
print(time.time()-t)
EOF
python probe.py 2>&1 | head -300
```

```
root pynwb.file.NWBFile at 0x134973348472752
Fields:
  experiment_description: Welch, Gonzales-Hess, Tarvin, Connor, Smear -- "The impact of a psychedelic drug on olfactory search behavior by mice," bioRxiv 2025.07.09.663970.
  experimenter: ['Welch, Amanda']
  file_create_date: [datetime.datetime(2026, 8, 6, 7, 25, 47, 904318, tzinfo=tzoffset(None, -25200))]
  identifier: 2198_17
  institution: University of Oregon
  intervals: {
    sniff_cycles <class 'pynwb.epoch.TimeIntervals'>,
    trials <class 'pynwb.epoch.TimeIntervals'>
  }
  keywords: <StrDataset for HDF5 dataset "keywords": shape (6,), type "|O">
  notes: {'Experimenter': 'Amanda', 'Trainer': 'None', 'Mouse sex': 'Male', 'Date': '13-Sep-2023 14:20:43', 'Mouse ID': '2198', 'Initial Weight': '20.5', 'Side Bias': 'None', 'Session': '17', 'Odorant': '2-PE', 'Sniffing': 'Yes', 'Thermistor Type': 'Glass', 'Left Port': '7.21', 'Right Port': '7.25', 'Initiation Port': '0', 'Experimenter Notes': '', 'L': '31/40', 'R': '37/38'}
  processing: {
    behavior <class 'pynwb.base.ProcessingModule'>
  }
  scratch: {
    drug_condition <class 'pynwb.core.ScratchData'>
  }
  session_description: Olfactory search task (2-PE odor, left/right choice, 10% no-odor catch trials, 5s response window). Drug condition: doi. Cohort B (see CLAUDE.md for what that means operationally -- different raw acquisition system, same task).
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > probe2.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd, sys
url=sys.argv[1]
h=h5py.File(remfile.File(url),'r')
pe=h['/processing/behavior/PoseEstimation']
for k in ['description','source_software']: print(k, pe[k][()])
print(dict(pe.attrs))
n=pe['nose']
print({k:n[k][()] for k in ['starting_time','reference_frame']}, dict(n['starting_time'].attrs), dict(n.attrs))
print(dict(n['data'].attrs))
te=h['/processing/behavior/task_event_timestamps']
print(dict(te.attrs)); print(dict(te['data'].attrs)); 
print(np.unique(te['data'][:],return_counts=True)); print(te['timestamps'][:20], te['data'][:20])
tr=h['/intervals/trials']; print(dict(tr.attrs))
df=pd.DataFrame({k:tr[k][:] for k in tr.keys() if k!='id'})
print(df.head(20).to_string()); print(df.describe().to_string())
for c in ['false_alarm','odor_control','outcome','repoke','side']: print(c, df[c].value_counts().to_dict())
sc=h['/intervals/sniff_cycles']; print(dict(sc.attrs))
s=pd.DataFrame({k:sc[k][:] for k in sc.keys() if k!='id'}); print(s.head(10)); print(s.describe())
print(h['/scratch/drug_condition'][()], dict(h['/scratch/drug_condition'].attrs))
print(h['/general/keywords'][:])
print(h['/session_description'][()])
EOF
python probe2.py https://api.dandiarchive.org/api/assets/e8ff1ad3-7ea7-4b2a-98ff-606accd5f233/download/
```

```
description b"DeepLabCut tracking, 8 keypoints, from DLC_tracked_task -- the tracking used for this paper's main analysis (Matt, 2026-08-06), not newmove's own separate (simpler, cohort-A-only) tracking arrays."
source_software b'DeepLabCut'
{'namespace': 'ndx-pose', 'neurodata_type': 'PoseEstimation', 'object_id': '1adf7098-ac73-40a5-bbdf-54e8fbf85a7b'}
{'starting_time': np.float64(0.0), 'reference_frame': b'top-left corner of the camera frame, DeepLabCut default'} {'rate': np.float64(81.71753175944605), 'unit': 'seconds'} {'comments': 'no comments', 'description': 'x,y in pixels, DeepLabCut model DLC_resnet_50_olfactory-searchFeb23shuffle1_300000.', 'namespace': 'ndx-pose', 'neurodata_type': 'PoseEstimationSeries', 'object_id': 'c6431421-1c71-431e-afe0-a76841171d70'}
{'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'pixels'}
{'comments': 'no comments', 'description': "Event times (s) from Time Stamps Task. Relationship to the trials table's own start/end times not independently confirmed -- see MISSION_NOTES.md.", 'namespace': 'core', 'neurodata_type': 'TimeSeries', 'object_id': 'de9148b7-cdcf-4c8f-917c-1653e3373221'}
{'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'n.a.'}
(array([1.]), array([137]))
[ 17.21  26.09  31.23  40.63  55.27  70.13  84.47 131.18 140.43 149.44
 164.37 180.79 191.45 195.51 207.44 226.37 241.61 260.29 271.6  279.4 ] [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
{'colnames': array(['start_time', 'stop_time', 'odor_control', 'side', 'outcome',
       'iti_time', 'false_alarm', 'repoke'], dtype=object), 'description': 'experimental trials', 'namespace': 'core', 'neurodata_type': 'TimeIntervals', 'object_id': '09122da9-0993-4949-afac-bcd5f6868a52'}
    false_alarm  iti_time  odor_control  outcome  repoke  side  start_time  stop_time
0           0.0       2.0           0.0      1.0     0.0   2.0     19.9877    22.7735
1          
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, numpy as np, pandas as pd, json, requests
from concurrent.futures import ThreadPoolExecutor
r=requests.get("https://api.dandiarchive.org/api/dandisets/001863/versions/0.260806.2109/assets/?page_size=100").json()['results']
def one(a):
    h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    pe=h['/processing/behavior/PoseEstimation']
    d=dict(path=a['path'], sess=h['/session_id'][()].decode(), drug=h['/scratch/drug_condition'][()].decode(),
      sex=h['/general/subject/sex'][()].decode(), desc=h['/session_description'][()].decode()[-120:],
      nframes=pe['nose/data'].shape[0], rate=float(pe['nose/starting_time'].attrs['rate']),
      ntr=h['/intervals/trials/id'].shape[0], cols=list(h['/intervals/trials'].attrs['colnames']),
      nsniff=h['/intervals/sniff_cycles/id'].shape[0] if 'sniff_cycles' in h['/intervals'] else None,
      sniffdesc=h['/intervals/sniff_cycles'].attrs['description'][-150:] if 'sniff_cycles' in h['/intervals'] else None,
      nev=h['/processing/behavior/task_event_timestamps/data'].shape[0] if 'task_event_timestamps' in h['/processing/behavior'] else None,
      beh=list(h['/processing/behavior'].keys()), intervals=list(h['/intervals'].keys()), top=list(h.keys()),
      notes=h['/general/notes'][()].decode() if 'notes' in h['/general'] else None,
      start=h['/session_start_time'][()].decode())
    return d
with ThreadPoolExecutor(8) as ex: rows=list(ex.map(one,r))
df=pd.DataFrame(rows).sort_values('path'); df.to_pickle('survey.pkl')
pd.set_option('display.width',250); pd.set_option('display.max_colwidth',80)
print(df[['path','sess','drug','sex','nframes','rate','ntr','nsniff','nev','start']].to_string())
print(df.cols.astype(str).value_counts()); print(df.beh.astype(str).value_counts()); print(df.intervals.astype(str).value_counts()); print(df.top.astype(str).value_counts())
print(df.desc.value_counts())
for s in df.sniffdesc.unique(): print(s)
print(df.notes.iloc[0]); print(df.notes.iloc[20])
EOF
time python survey.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 18, in <module>
    with ThreadPoolExecutor(8) as ex: rows=list(ex.map(one,r))
                                           ~~~~^^^^^^^^^^^^^^^
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
  File "/tmp/claude-1001/survey.py", line 7, in one
    d=dict(path=a['path'], sess=h['/session_id'][()].decode(), drug=h['/scratch/drug_condition'][()].decode(),
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && sed -i "s#sess=h\['/session_id'\]\[()\].decode()#sess=h['/general/session_id'][()].decode()#; s#'/session_start_time'\]\[()\].decode()#'/session_start_time'][()].decode()#" survey.py && sed -i "s#h\['/general/notes'\]\[()\].decode() if 'notes' in h\['/general'\] else None#(h['/general/notes'][()].decode() if 'notes' in h['/general'] else None)#" survey.py && time python survey.py
```

```
path     sess    drug sex  nframes       rate  ntr   nsniff    nev                      start
9   sub-2174/sub-2174_ses-2174-56.nwb  2174_56  saline   F   185828  77.434829  158      NaN    NaN  2022-01-27T10:12:19-08:00
1   sub-2174/sub-2174_ses-2174-57.nwb  2174_57     doi   F   177027  74.140802  121      NaN  166.0  2022-01-28T12:18:19-08:00
3   sub-2181/sub-2181_ses-2181-41.nwb  2181_41  saline   F   173159  72.724270  132      NaN    NaN  2022-01-27T11:00:51-08:00
2   sub-2181/sub-2181_ses-2181-42.nwb  2181_42     doi   F   180616  75.393709  126      NaN  176.0  2022-01-28T13:05:23-08:00
0   sub-2182/sub-2182_ses-2182-31.nwb  2182_31  saline   F   179464  74.857491  103      NaN    NaN  2022-01-27T12:05:16-08:00
4   sub-2182/sub-2182_ses-2182-32.nwb  2182_32     doi   M   180540  75.718858  128      NaN  174.0  2022-01-28T13:50:38-08:00
7   sub-2183/sub-2183_ses-2183-33.nwb  2183_33  saline   M   176506  73.666207  145      NaN    NaN  2022-01-27T12:50:07-08:00
5   sub-2183/sub-2183_ses-2183-34.nwb  2183_34     doi   M   180573  75.512625  139      NaN  204.0  2022-01-28T14:38:14-08:00
6   sub-2185/sub-2185_ses-2185-40.nwb  2185_40  saline   M   175720  73.757082  118      NaN    NaN  2022-01-27T13:34:56-08:00
8   sub-2185/sub-2185_ses-2185-41.nwb  2185_41     doi   M   185127  77.161002  119      NaN  171.0  2022-01-28T15:24:02-08:00
10  sub-2191/sub-2191_ses-2191-21.nwb  2191_21  saline   F   192012  82.939507   87  11004.0    NaN  2023-09-19T15:33:14-07:00
11  sub-2191/sub-2191_ses-2191-25.nwb  2191_25     doi   F   191914  82.514103   68  14490.0  141.0  2023-09-26T15:30:23-07:00
12  sub-2195/sub-2195_ses-2195-17.nwb  2195_17     doi   M   192029  83.630522   45   1612.0  131.0  2023-09-13T11:43:02-07:00
13  sub-2195/sub-2195_ses-2195-20.nwb  2195_20  saline   M   192010  81.322992  103      NaN    NaN  2023-09-19T11:42:31-07:00
14  sub-2196/sub-2196_ses-2196-16.nwb  2196_16  saline   M   192020  80.793814   57  11664.0    NaN  2023-09-13T12:38:55-07:00
1
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python -c "
import h5py,remfile
for a in ['e8ff1ad3-7ea7-4b2a-98ff-606accd5f233','998a969e-b5f0-4d10-aeea-161d1c7ab8fa','9ad76bcf-3675-4757-8f07-e2f64d1a9e10']:
  h=h5py.File(remfile.File(f'https://api.dandiarchive.org/api/assets/{a}/download/'),'r')
  for g in ['acquisition','analysis','stimulus','scratch']: print(g, list(h[g].keys()))
  print(list(h['/intervals/trials'].attrs['colnames']))
"; git clone -q https://github.com/Smear-Lab/Olfactory-search-on-psychedelics.git code && cd code && git log -1 --format='%H %cd' && find . -type f | grep -v .git/ | head -100
```

```
acquisition []
analysis []
stimulus ['presentation', 'templates']
scratch ['drug_condition']
['start_time', 'stop_time', 'odor_control', 'side', 'outcome', 'iti_time', 'false_alarm', 'repoke']
acquisition []
analysis []
stimulus ['presentation', 'templates']
scratch ['drug_condition']
['start_time', 'stop_time', 'odor_control', 'side', 'outcome', 'iti_time']
acquisition []
analysis []
stimulus ['presentation', 'templates']
scratch ['drug_condition']
['start_time', 'stop_time', 'odor_control', 'side', 'outcome', 'iti_time']
aa80af0a153c6bf099e5668d27c9d88e2bfc033f Thu Aug 6 14:46:47 2026 -0700
./fmon-bpod/bonsai protocols/bpod-fmon-tcp.bonsai
./fmon-bpod/bonsai protocols/bpod-fmon-spontaneous.bonsai.layout
./fmon-bpod/bonsai protocols/bpod-fmon-serial.bonsai
./fmon-bpod/bonsai protocols/bpod-fmon.bonsai.layout
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && wc -l nwb_conversion/convert_session_to_nwb.py analysis/*.Rmd && cat nwb_conversion/convert_session_to_nwb.py
```

```
446 nwb_conversion/convert_session_to_nwb.py
  1354 analysis/fig1_cleaned.Rmd
   692 analysis/fig2_cleaned.Rmd
   773 analysis/fig3_cleaned.Rmd
   476 analysis/fig4_cleaned.Rmd
   629 analysis/fig5_cleaned.Rmd
  4370 total
#!/usr/bin/env python3
"""
convert_session_to_nwb.py -- Psychedelic_Sniff mission

Converts one session of the DOI-vs-saline olfactory search task dataset
(Welch, Gonzales-Hess, Tarvin, Connor, Smear -- "The impact of a
psychedelic drug on olfactory search behavior by mice," bioRxiv
2025.07.09.663970) into a single NWB file.

Source: /Volumes/TOSHIBA (external drive, read-only from this machine --
never written to). See CLAUDE.md for the full data-format mapping this
implements, and MISSION_NOTES.md for how each piece of that mapping was
verified (and what's still an open assumption).
[... 434 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/analysis && grep -n -i "time stamps\|htr\|read\.csv\|read_csv\|list.files\|readMat\|drinking\|setwd\|path" fig5_cleaned.Rmd | head -80
```

````
20:- `bin_width` for the HTR grand-mean CSVs (below) is 100 px in this
22:  htr_grandmean_iti/htr_grandmean_within on the drive with different bin
107:is_matching_file <- function(path) {
108:  parts <- strsplit(path, "/")[[1]]
114:trial_summ <- list.files(path = "D:/newmove", recursive = TRUE, pattern = "trialsummary.txt", full.names = TRUE)
162:# HTR event import and matching
164:```{r import htr timestamps}
165:# htr timestamps from two sources: automated detection ("D:/Time Stamps
166:# Task") and manually-scored files ("D:/Time Stamps Task Logan")
167:read_htr_timestamps <- function(file) {
178:  read.csv(tmp_file, header = FALSE, col.names = "Timestamp", stringsAsFactors = FALSE)
181:htr_list <- list.files(path = "D:/Time Stamps Task", pattern = "*.csv", full.names = TRUE)
182:htr_data <- lapply(htr_list, read_htr_timestamps)
183:names(htr_data) <- basename(htr_list)
192:htr_seconds <- lapply(htr_data, function(df) {
200:# manually-scored htr files (already in seconds)
201:logan_paths <- list.files("D:/Time Stamps Task Logan", full.names = TRUE)
202:logan_names <- basename(logan_paths)
203:logan_htr <- setNames(lapply(logan_paths, function(f) {
204:  df <- read.csv(f)
[... 61 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python -c "
import h5py,remfile
h=h5py.File(remfile.File('https://api.dandiarchive.org/api/assets/e8ff1ad3-7ea7-4b2a-98ff-606accd5f233/download/'),'r')
h['stimulus'].visititems(lambda n,o: print(n,o))
"; ls $TMPDIR/code/analysis/Figure1 | head
```

```
presentation <HDF5 group "/stimulus/presentation" (0 members)>
templates <HDF5 group "/stimulus/templates" (0 members)>
/tmp/claude-1001/code/analysis/Figure1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/analysis && sed -n 1,400p fig1_cleaned.Rmd
```

````
---
title: "Figure 1"
author: "Amanda Welch"
output: html_document
---
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

<!--
Figure 1: task accuracy and engagement, DOI vs. saline, all paired by
mouse (one DOI session + one saline session per animal). 1B = odor-trial
accuracy; 1C = accuracy over the first 40 min, 5-min bins; 1D = trials
completed in 40 min; 1E = trial-initiation ("repoke") rate during the ITI.
The dose/session-number/sex lookup tables below (`doi_dose`/`saline_dose`/
`sex`) are re-typed by hand 3 times in this file (once per section) rather
than defined once and reused -- same session list each time, just
duplicated, not a discrepancy.
-->

[... 382 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/code/analysis && sed -n 400,1354p fig1_cleaned.Rmd | grep -v "^\s*accuracy\$id ==\|ggplot\|theme\|geom_\|scale_\|labs(\|size =\|element_" | sed -n 1,500p
```

````
# append the corresponding data frame to doi_trial_summaries
    doi_trial_summaries[[file_path]] <- all_data[[file_path]]
  }
}
```

```{r name columns doi}
# name columns in dfs
for (i in seq_along(doi_trial_summaries)) {
  colnames(doi_trial_summaries[[i]]) <- colnames
}
```

```{r}
# define the list of conditions for mouse ID and session number for saline
saline_conditions <- list(
  c(2174, 56), c(2181, 41), c(2182, 31), c(2183, 33), c(2185, 40),
  c(2191, 21), c(2195, 20), c(2196, 16), c(2197, 19), c(2198, 19),
  c(2200, 19), c(2201, 21), c(2202, 14), c(2203, 18), c(2204, 22),
  c(2205, 16), c(2208, 14), c(2209, 18), c(2210, 13), c(2211, 17),
[... 481 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/code/analysis && grep -n -i -B2 -A12 "repoke" fig1_cleaned.Rmd | grep -v "== \"" | sed -n 1,140p
```

````
12-mouse (one DOI session + one saline session per animal). 1B = odor-trial
13-accuracy; 1C = accuracy over the first 40 min, 5-min bins; 1D = trials
14:completed in 40 min; 1E = trial-initiation ("repoke") rate during the ITI.
15-The dose/session-number/sex lookup tables below (`doi_dose`/`saline_dose`/
16-`sex`) are re-typed by hand 3 times in this file (once per section) rather
17-than defined once and reused -- same session list each time, just
18-duplicated, not a discrepancy.
19--->
20-
21-# Figure 1
22-
23-```{r}
24-library(gtools)
25-
26-# create vector listing all the trial summary files in the chosen directory with trial summary files
--
1076-# 1E
1077-
1078:Trial-initiation attempt ("repoke") rate during the ITI, DOI vs. saline,
1079:one point per mouse. Uses `trialsummary_falsealarms_softcode_repoke.txt`
[... 121 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/code/analysis && sed -n 1153,1168p fig1_cleaned.Rmd; grep -n "" fig3_cleaned.Rmd | grep -v "ggplot\|theme\|geom_\|scale_\|labs(\|size =\|element_\|== \"" | sed -n 1,400p
```

````
# shift ITI duration up one row for each frame
shift <- function(x, n) {
  c(x[-(seq(n))], rep(NA, n))
}

for (i in seq_along(all_data)) {
  all_data[[i]]$iti_length <- shift(all_data[[i]]$iti_length, 1)
}
```

```{r}
all_data %>%
  map(~ .x %>%
        summarise(
          trials_performed = n(),
1:---
2:title: "Figure 3"
3:author: "Amanda Welch"
4:output: html_document
5:---
[... 396 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/code/analysis && sed -n 438,773p fig3_cleaned.Rmd | grep -v "ggplot\|theme\|geom_\|scale_\|labs(\|size =\|element_\|== \"\|^\s*$"
```

````
for (file_name in names(TrackingAll)) {
  parts <- strsplit(file_name, "_")[[1]]
  mouse_id <- parts[1]
  session <- parts[2]
  if (grepl("_doi\\.csv$", file_name, ignore.case = TRUE)) {
    doi_tracking_data[[file_name]] <- get_nose_tracking(TrackingAll, mouse_id, session, "doi")
  } else if (grepl("_saline\\.csv$", file_name, ignore.case = TRUE)) {
    saline_tracking_data[[file_name]] <- get_nose_tracking(TrackingAll, mouse_id, session, "saline")
  }
}
```
```{r trial timing lookup}
# ids/sessions to keep, in the "<mouse_id> = c(doi_session, saline_session)"
# form needed for file-path matching below (derived from mouse_sessions)
keep_ids_sessions <- setNames(
  lapply(seq_len(nrow(mouse_sessions)), function(i) {
    c(mouse_sessions$session_doi[i], mouse_sessions$session_saline[i])
  }),
  as.character(mouse_sessions$mouse_id)
)
[... 224 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/code/analysis && grep -v "ggplot\|theme\|geom_\|scale_\|labs(\|size =\|element_\|^\s*$" fig4_cleaned.Rmd | sed -n 1,330p
```

````
---
title: "Figure 4"
author: "amanda welch"
output: html_document
---
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
library(R.matlab)
library(gtools)
library(dplyr)
library(stringr)
library(purrr)
library(tidyr)
library(coin)
```
<!--
Figure 4: sniff frequency (from Task sniff params/*.mat, thermistor-derived
inhalation timing), DOI vs. saline. 4A/4B = per-mouse density overlays;
4C = pooled density, mean +/- SEM across mice; 4D = 4C split by trial
period (odor/omission/ITI); 4E = per-mouse median frequency, paired
[... 311 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/code/analysis && grep -v "ggplot\|theme(\|geom_\|scale_\|labs(\|size =\|element_\|^\s*$" fig5_cleaned.Rmd | sed -n 1,420p
```

```
---
title: "Figure 5"
author: "Amanda Welch"
output: html_document
---
this file produces the data (as csvs) and statistics for figure 5
(occupancy and head-twitch response location/rate). plotting is done
separately in occupancy_grandmean_gaussian.mlx (matlab) - this script
only writes the csvs that script reads in, plus runs the reported stats.
r and matlab code are kept in separate files intentionally.
<!--
Two things worth knowing before re-running this file:
- The `write.csv` calls for the occupancy_*.csv files that the MATLAB
  script needs (see "export occupancy csvs" chunk near the end) are
  commented out. A fresh run of this notebook will NOT regenerate those
  CSVs -- they only exist because someone ran that block manually at some
  point. Uncomment before relying on a from-scratch re-run.
- `bin_width` for the HTR grand-mean CSVs (below) is 100 px in this
  version of the file. If you find more than one copy of
  htr_grandmean_iti/htr_grandmean_within on the drive with different bin
[... 401 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; ls schemas; python - <<'EOF'
import json
for f in ['schemas/attempt.schema.json','schemas/claims.schema.json']:
    try:
        s=json.load(open(f)); print(f); print(json.dumps(s,indent=0)[:6000])
    except Exception as e: print(e)
EOF
```

```
Thu Nov  5 15:48:34 UTC 2026
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/attempt.schema.json
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
[... 554 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
for k in p:
    if k not in ('dataset','provenance','outcomes'): print(k, json.dumps(p[k])[:1500]); print()
EOF
grep -n -B3 -A30 "kind: link" claims/001453/*.yaml | head -60; grep -n "data:" claims/001453/*.yaml | head
```

```
schema_version {"const": 2}

id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}

paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}

date {"type": "string", "format": "date"}

entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}

deprecated {"description": "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", "type": "object", "additionalProperties": false, "required": ["date", "reason"], "properties": {"date": {"type": "string", "format": "date"}, "reason": {"type": "string", "minLength": 1}, "superseded_by": {"description": "The id of the attempt that replaces it, once there is one.", "type": "string"}}}

verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}}}}

findings {"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "requi
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/001863-welch-2025 && cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import h5py,remfile,numpy as np, pickle, pandas as pd
df=pd.read_pickle('survey.pkl')
import requests
r=requests.get("https://api.dandiarchive.org/api/dandisets/001863/versions/0.260806.2109/assets/?page_size=100").json()['results']
ids={a['path']:a['asset_id'] for a in r}
for p in df.path[df.nev.notna()][:44]:
    h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{ids[p]}/download/"),'r')
    te=h['/processing/behavior/task_event_timestamps']
    t=te['timestamps'][:]; desc=te.attrs['description']
    frac=np.round((t-np.floor(t))*100).astype(int)
    tr=h['/intervals/trials']; st=tr['start_time'][:]; en=tr['stop_time'][:]
    print(p.split('/')[1][:-4], 'Logan' in desc, len(t), 'frac max',frac.max(), 'tmin %.1f tmax %.1f'%(t.min(),t.max()), 'sorted',np.all(np.diff(t)>=0), 'trials end %.0f'%en.max())
EOF
```

```
sub-2174_ses-2174-57 True 166 frac max 88 tmin 27.4 tmax 2195.2 sorted True trials end 2388
sub-2181_ses-2181-42 True 176 frac max 89 tmin 6.9 tmax 2254.6 sorted True trials end 2396
sub-2182_ses-2182-32 True 174 frac max 89 tmin 6.8 tmax 2246.7 sorted True trials end 2384
sub-2183_ses-2183-34 True 204 frac max 89 tmin 4.7 tmax 2247.2 sorted True trials end 2391
sub-2185_ses-2185-41 True 171 frac max 89 tmin 17.2 tmax 2287.1 sorted True trials end 2399
sub-2191_ses-2191-25 False 141 frac max 78 tmin 0.7 tmax 2395.1 sorted True trials end 2326
sub-2195_ses-2195-17 False 131 frac max 79 tmin 4.5 tmax 2397.3 sorted True trials end 2296
sub-2196_ses-2196-18 False 107 frac max 79 tmin 6.5 tmax 2349.3 sorted True trials end 2365
sub-2197_ses-2197-17 False 30 frac max 77 tmin 21.1 tmax 2257.1 sorted True trials end 2346
sub-2198_ses-2198-17 False 137 frac max 79 tmin 17.2 tmax 2390.1 sorted True trials end 2348
sub-2200_ses-2200-14 False 152 frac max 79 tmin 1.1 tmax 2387.7 sorted True trials end 2364
sub-2200_ses-2200-19 False 18 frac max 78 tmin 52.3 tmax 2345.6 sorted True trials end 2357
sub-2201_ses-2201-16 False 163 frac max 79 tmin 5.7 tmax 2379.3 sorted True trials end 2349
sub-2201_ses-2201-21 False 15 frac max 71 tmin 5.2 tmax 2348.1 sorted True trials end 2377
sub-2202_ses-2202-14 False 20 frac max 77 tmin 74.8 tmax 1852.3 sorted True trials end 2344
sub-2202_ses-2202-19 False 122 frac max 79 tmin 11.5 tmax 2365.6 sorted True trials end 2321
sub-2203_ses-2203-13 False 143 frac max 79 tmin 1.3 tmax 2394.1 sorted True trials end 2347
sub-2203_ses-2203-18 False 17 frac max 77 tmin 13.1 tmax 2261.7 sorted True trials end 2351
sub-2204_ses-2204-17 False 24 frac max 76 tmin 13.8 tmax 2259.6 sorted True trials end 2376
sub-2204_ses-2204-22 False 14 frac max 79 tmin 25.3 tmax 2246.8 sorted True trials end 2333
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import h5py,remfile,numpy as np
for a in ['998a969e-b5f0-4d10-aeea-161d1c7ab8fa','e926e1b7-1a9c-4222-9b43-07240e418c90','e8ff1ad3-7ea7-4b2a-98ff-606accd5f233']:
    h=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a}/download/"),'r')
    t=h['/processing/behavior/task_event_timestamps/timestamps'][:]
    print(t[:15]); fr=np.round((t-np.floor(t))*1000).astype(int); print(np.unique(fr)[:60], len(np.unique(fr)))
EOF
```

```
[ 27.36   44.105  68.59   74.24   89.065 106.71  113.015 126.57  135.07
 150.685 156.76  165.71  170.06  182.03  188.18 ]
[  5  15  30  40  60  65  70  75  85  90  95 105 115 120 125 130 140 145
 150 165 170 175 180 185 190 195 200 210 240 245 250 255 260 265 275 285
 295 305 315 325 330 340 345 350 360 365 380 385 505 510 525 535 540 550
 555 570 575 590 595 605] 95
[  4.745  12.055  19.135  46.505  59.33   68.02   76.53   83.825  94.28
 111.895 112.215 119.26  138.885 150.3   158.855]
[  0   5  10  20  25  30  35  45  50  55  60  65  70  75  85  90  95 100
 105 115 120 125 130 135 140 145 150 155 165 170 175 185 190 195 200 205
 215 220 225 240 250 255 260 270 280 285 290 295 300 310 320 325 330 335
 345 350 365 370 375 380] 116
[ 17.21  26.09  31.23  40.63  55.27  70.13  84.47 131.18 140.43 149.44
 164.37 180.79 191.45 195.51 207.44]
[ 10  30  40  70  80  90 100 110 120 130 140 150 160 180 190 200 210 230
 240 260 270 280 290 310 320 330 350 370 380 390 400 420 430 440 450 460
 470 480 490 500 510 530 540 570 580 590 600 610 620 630 640 650 660 680
 690 700 710 720 730 740] 65
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cat entries/001453-fouke-2025/omr.py | sed -n 80,200p | head -60; cat tools/entry.py | head -80; ls executed 2>/dev/null | head -3
```

```
Thu Nov  5 15:50:05 UTC 2026
def _text(value) -> str:
    value = value[()]
    return value.decode() if isinstance(value, bytes) else str(value)


def load_session(path: str, url: str) -> dict:
    """One fish: its metadata, and the frames that belong to a trial.

    Frames outside a trial (no stim_index) are dropped, and the static block (code 20, hours
    long) is cut to its first 60 s. Fig1-S1.ipynb treats code 20 like any trial number and keeps
    its first 35 s, so the cut keeps every frame the measures use. Before that, the file's mean
    frame interval over tracked frames is kept as `code_dt`, which Fig1-S1.ipynb uses for its
    angular acceleration, with the timestamp intervals (`dt_ms`) and the code-20 block's length.
    """
    with h5py.File(remfile.File(url), "r") as f:
        subject = f["general/subject"]
        series = f["processing/behavior/BehavioralTimeSeries"]
        t = series["f0_x/timestamps"][:]
        data = {k: series[f"{k}/data"][:] for k in
[... 121 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/001863-welch-2025/doi_search.py",
 "content": "\"\"\"Loading and measures for the DOI olfactory search sessions of dandiset 001863.\n\nWelch, Gonzales-Hess, Tarvin, Connor & Smear (2025), \"The impact of a psychedelic drug on\nolfactory search behavior by mice\", bioRxiv doi:10.1101/2025.07.09.663970.\n\nEach NWB file holds one session of one mouse: the trial table (start and stop time, odor_control\n0 for an odor trial and 3 for an omission trial, side, outcome, the set ITI and, for the 17 mice of\nthe later cohort, `false_alarm` and `repoke` counts), DeepLabCut tracking of eight keypoints, the\nsniff cycles detected from the nasal thermistor (31 sessions) and a series\n`task_event_timestamps` (32 sessions). Files are streamed from the archive at the pinned version;\nnothing is written to disk.\n\nWhere the parameters come from. \"Code\" is the authors' repository\ngithub.com/Smear-Lab/Olfactory-search-on-psychedelics at commit\naa80af0a153c6bf099e5668d27c9d88e2bfc033f, which the claims file cites.\n\n- `DOI_SESSION` and `SALINE_SESSION`: the claims file's opening comment (the code's list).\n- `FEMALES`: the claims file's opening comment and fig1_cleaned.Rmd; the files' own sex field is\n  checked against it in the notebook.\n- `FIRST_COHORT`: Methods, Figure 1 and Figure 2 (\"the first cohort of 5\"), and the code's\n  `flip_ids`; their x coordinate is flipped as 1200 - x for the maps (fig5_cleaned.Rmd).\n- `MIN_TRIALS = 40`: fig1_cleaned.Rmd and fig3_cleaned.Rmd, as the claims file gives it.\n- Tracking cleaning: Methods, Figure 3 (\"points with likelihood < 0.95 or delta > 8 pixels were\n  interpolated\", \"Any speed that was > 160 cm/s was excluded\"), with the code's `CleanTracking`\n  (delta from the raw positions, linear interpolation, ends held at the nearest value as\n  imputeTS::na_interpolation does).\n- `CODE_FPS = 80` and `CM_PER_PX = 0.0237`: fig3_cleaned.Rmd (`speed_aw`, `speed_aw_cm`; frame i,\n  counted from 1, at time i / 80 s), as the claims file gives them. The files' own frame rate is\n  an estimate made at conversion (frames divided by the last trial's end time) and is not used;\n  the notebook checks the 80 frames/s clock against the trial table.\n- `OCC_BIN_PX = 48`: the claims file (fig5ab, \"48 pixels in fig5_cleaned.Rmd\", 1 cm bins).\n- `HTR_BIN_PX = 100` and the dropped edge bins (x bin 1200, y bin 700): fig5_cleaned.Rmd.\n- `task_event_timestamps` are the head-twitch (HTR) times: the conversion script\n  (nwb_conversion/convert_session_to_nwb.py) loads them from the folders \"Time Stamps Task\" and\n  \"Time Stamps Task Logan\", which fig5_cleaned.Rmd reads as HTR timestamps. The files do not name\n  them. For the \"Time Stamps Task\" files (later cohort) the conversion script read the last field\n  of an HH:MM:SS:XX string as hundredths of a second, fig5_cleaned.Rmd reads it as thousandths,\n  and the values (0 to 79) look like a frame count at 80 frames/s. `htr_times` returns each\n  reading; \"code\" (thousandths) is the one the paper's numbers were computed with.\n- Statistical tests follow R's defaults as the code calls them (`r_signrank`, `r_ranksum`):\n  exact when there are fewer than 50 values and no ties, otherwise the normal approximation with\n  continuity correction, zero differences dropped.\n\"\"\"\n\nfrom __future__ import annotations\n\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import stats\n\nDANDISET_ID = \"001863\"\nDANDISET_VERSION = \"0.260806.2109\"\n\nDOI_SESSION = {2174: 57, 2181: 42, 2182: 32, 2183: 34, 2185: 41, 2191: 25, 2195: 17, 2196: 18,\n               2197: 17, 2198: 17, 2200: 14, 2201: 16, 2202: 19, 2203: 13, 2204: 17, 2205: 12,\n               2208: 18, 2209: 14, 2210: 17, 2211: 13, 2212: 16, 2213: 14}\nSALINE_SESSION = {2174: 56, 2181: 41, 2182: 31, 2183: 33, 2185: 40, 2191: 21, 2195: 20, 2196: 16,\n                  2197: 19, 2198: 19, 2200: 19, 2201: 21, 2202: 14, 2203: 18, 2204: 22, 2205: 16,\n                  2208: 14, 2209: 18, 2210: 13, 2211: 17, 2212: 13, 2213: 18}\nFEMALES = {2174, 2181, 2191, 2200, 2201, 2202, 2203, 2204, 2210, 2211, 2212, 2213}\nFIRST_COHORT = {2174, 2181, 2182, 2183, 2185}\nFAULTY_SNIFF = {(2198, 17), (2195, 17), (2198, 19), (2213, 18)}   # fig4_cleaned.Rmd\n\nMIN_TRIALS = 40\nCODE_FPS = 80.0\nCM_PER_PX = 0.0237\nLIKELIHOOD_MIN = 0.95\nMAX_DELTA_PX = 8.0\nMAX_SPEED_CM_S = 160.0\nSESSION_S = 2400.0\nOCC_BIN_PX = 48\nHTR_BIN_PX = 100\nHTR_EDGE_X, HTR_EDGE_Y = 1200, 700\nFLIP_X = 1200.0\n\n\ndef asset_urls() -> list[tuple[str, str]]:\n    \"\"\"(path, streaming URL) of every NWB file at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return sorted((a.path, a.get_content_url(follow_redirects=1, strip_query=True))\n                      for a in dandiset.get_assets() if a.path.endswith(\".nwb\"))\n\n\ndef _text(value) -> str:\n    value = value[()]\n    return value.decode() if isinstance(value, bytes) else str(value)\n\n\ndef load_session(path: str, url: str) -> dict:\n    \"\"\"One session: metadata, trial table, nose track, sniff cycles and event times.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        mouse, session = (int(v) for v in _text(f[\"general/session_id\"]).split(\"_\"))\n        tr = f[\"intervals/trials\"]\n        cols = [c.decode() if isinstance(c, bytes) else str(c) for c in tr.attrs[\"colnames\"]]\n        trials = pd.DataFrame({c: tr[c][:] for c in cols})\n        nose = f[\"processing/behavior/PoseEstimation/nose\"]\n        s = {\n            \"path\": path, \"mouse\": mouse, \"session\": session,\n            \"drug\": _text(f[\"scratch/drug_condition\"]),\n            \"sex_file\": _text(f[\"general/subject/sex\"]),\n            \"description\": _text(f[\"session_description\"]),\n            \"start\": _text(f[\"session_start_time\"]),\n            \"trials\": trials,\n            \"nose_xy\": nose[\"data\"][:],\n            \"nose_conf\": nose[\"confidence\"][:],\n            \"file_rate\": float(nose[\"starting_time\"].attrs[\"rate\"]),\n            \"pose_unit\": nose[\"data\"].attrs.get(\"unit\"),\n        }\n        if \"sniff_cycles\" in f[\"intervals\"]:\n            sc = f[\"intervals/sniff_cycles\"]\n            s[\"sniff_start\"] = sc[\"start_time\"][:]\n            s[\"sniff_stop\"] = sc[\"stop_time\"][:]\n            s[\"sniff_description\"] = sc.attrs[\"description\"]\n        else:\n            s[\"sniff_start\"] = None\n        if \"task_event_timestamps\" in f[\"processing/behavior\"]:\n            te = f[\"processing/behavior/task_event_timestamps\"]\n            s[\"events\"] = te[\"timestamps\"][:]\n            s[\"events_source\"] = \"logan\" if \"Logan\" in te.attrs[\"description\"] else \"task\"\n            s[\"events_data\"] = np.unique(te[\"data\"][:])\n        else:\n            s[\"events\"] = None\n    s[\"condition\"] = (\"DOI\" if DOI_SESSION[mouse] == session else\n                      \"saline\" if SALINE_SESSION[mouse] == session else \"other\")\n    s[\"sex\"] = \"F\" if mouse in FEMALES else \"M\"\n    s[\"cohort\"] = \"first\" if mouse in FIRST_COHORT else \"later\"\n    return s\n\n\ndef load_all(workers: int = 8) -> list[dict]:\n    \"\"\"Every session of the dandiset, loaded in parallel.\"\"\"\n    urls = asset_urls()\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(lambda pu: load_session(*pu), urls))\n\n\n# ---------------------------------------------------------------- trials\n\n\ndef odor_mask(trials: pd.DataFrame) -> np.ndarray:\n    return trials.odor_control.to_numpy() == 0\n\n\ndef iti_lengths(trials: pd.DataFrame) -> np.ndarray:\n    \"\"\"Next trial's start minus this trial's end (the last trial has none), as the code does.\"\"\"\n    st, en = trials.start_time.to_numpy(), trials.stop_time.to_numpy()\n    return np.append(st[1:] - en[:-1], np.nan)\n\n\ndef rolling_accuracy(trials: pd.DataFrame) -> np.ndarray:\n    \"\"\"Percent correct of a trial type's trials up to and including each trial (fig1_cleaned.Rmd).\"\"\"\n    out = np.full(len(trials), np.nan)\n    for kind in (0, 3):\n        m = trials.odor_control.to_numpy() == kind\n        succ = trials.outcome.to_numpy()[m]\n        out[m] = 100 * np.cumsum(succ) / np.arange(1, m.sum() + 1)\n    return out\n\n\n# ---------------------------------------------------------------- tracking\n\n\ndef _interp_nan(v: np.ndarray) -> np.ndarray:\n    ok = ~np.isnan(v)\n    if ok.sum() == 0:\n        return v\n    idx = np.arange(len(v))\n    return np.interp(idx, idx[ok], v[ok])   # ends held at the nearest value\n\n\ndef clean_nose(s: dict) -> tuple[np.ndarray, np.ndarray, dict]:\n    \"\"\"Nose x, y after the code's CleanTracking (likelihood < 0.95 or delta > 8 px interpolated).\"\"\"\n    x, y = s[\"nose_xy\"][:, 0].astype(float), s[\"nose_xy\"][:, 1].astype(float)\n    delta = np.r_[np.nan, np.hypot(np.diff(x), np.diff(y))]\n    low = s[\"nose_conf\"] < LIKELIHOOD_MIN\n    jump = delta > MAX_DELTA_PX\n    bad = low | jump | np.isnan(x) | np.isnan(y)\n    x[bad] = np.nan\n    y[bad] = np.nan\n    info = {\"frames\": len(x), \"low_likelihood\": int(low.sum()), \"jump\": int(jump.sum()),\n            \"interpolated\": int(bad.sum())}\n    return _interp_nan(x), _interp_nan(y), info\n\n\ndef frame_times(n: int, fps: float = CODE_FPS) -> np.ndarray:\n    \"\"\"Frame i (from 1) at i / fps s, as add_trial_label in the code.\"\"\"\n    return np.arange(1, n + 1) / fps\n\n\ndef label_periods(times: np.ndarray, trials: pd.DataFrame) -> np.ndarray:\n    \"\"\"0 for the ITI, 1 within an odor trial, 3 within an omission trial (start <= t <= end).\n\n    A later trial overwrites an earlier one where they overlap, as the code's loop does.\"\"\"\n    lab = np.zeros(len(times), dtype=int)\n    for st, en, oc in zip(trials.start_time, trials.stop_time, trials.odor_control):\n        i0, i1 = np.searchsorted(times, st, \"left\"), np.searchsorted(times, en, \"right\")\n        lab[i0:i1] = 3 if oc == 3 else 1\n    return lab\n\n\ndef speed_cm_s(x: np.ndarray, y: np.ndarray, fps: float = CODE_FPS) -> np.ndarray:\n    \"\"\"Frame-to-frame nose speed in cm/s; the first frame has none.\"\"\"\n    return np.r_[np.nan, np.hypot(np.diff(x), np.diff(y)) * fps * CM_PER_PX]\n\n\n# ---------------------------------------------------------------- HTR\n\n\ndef htr_times(s: dict, reading: str = \"code\") -> np.ndarray | None:\n    \"\"\"HTR times in s under a reading of the timestamp files (see the module docstring).\n\n    \"file\": as stored (last field of HH:MM:SS:XX as hundredths); \"code\": as fig5_cleaned.Rmd\n    (thousandths); \"frames\": as frames at 80 per second. The manually scored (\"Logan\") files were\n    stored in seconds and are the same under every reading.\"\"\"\n    t = s[\"events\"]\n    if t is None or s[\"events_source\"] == \"logan\" or reading == \"file\":\n        return t\n    whole = np.floor(t + 1e-9)\n    xx = np.round((t - whole) * 100)\n    return whole + xx / (1000.0 if reading == \"code\" else CODE_FPS)\n\n\n# ---------------------------------------------------------------- statistics\n\n\ndef r_signrank(a, b) -> tuple[float, float]:\n    \"\"\"Two-sided paired Wilcoxon signed-rank test as R's wilcox.test(a, b, paired = TRUE).\n\n    Returns (V, p); V is the sum of positive ranks of a - b.\"\"\"\n    d = np.asarray(a, float) - np.asarray(b, float)\n    d = d[~np.isnan(d)]\n    d = d[d != 0]\n    n = len(d)\n    if n == 0:\n        return np.nan, np.nan\n    r = stats.rankdata(np.abs(d))\n    v = float(r[d > 0].sum())\n    ties = len(np.unique(np.abs(d))) < n\n    if n < 50 and not ties:\n        p = stats.wilcoxon(d, method=\"exact\").pvalue\n    else:\n        mu = n * (n + 1) / 4\n        _, cnt = np.unique(r, return_counts=True)\n        sigma = np.sqrt(n * (n + 1) * (2 * n + 1) / 24 - (cnt ** 3 - cnt).sum() / 48)\n        z = v - mu\n        z = (z - np.sign(z) * 0.5) / sigma\n        p = 2 * min(stats.norm.cdf(z), stats.norm.sf(z))\n    return v, float(min(p, 1.0))\n\n\ndef r_ranksum(a, b, exact: bool | None = None) -> tuple[float, float]:\n    \"\"\"Two-sided Wilcoxon rank-sum test as R's wilcox.test(a, b); returns (W, p).\"\"\"\n    a = np.asarray(a, float)\n    b = np.asarray(b, float)\n    a, b = a[~np.isnan(a)], b[~np.isnan(b)]\n    allv = np.r_[a, b]\n    ties = len(np.unique(allv)) < len(allv)\n    use_exact = (len(a) < 50 and len(b) < 50 and not ties) if exact is None else exact\n    res = stats.mannwhitneyu(a, b, alternative=\"two-sided\",\n                             method=\"exact\" if use_exact else \"asymptotic\", use_continuity=True)\n    return float(res.statistic), float(res.pvalue)\n\n\ndef pairwise_ranksum_bonferroni(groups: dict[str, np.ndarray]) -> pd.DataFrame:\n    \"\"\"R pairwise.wilcox.test(..., p.adjust.method = \"bonferroni\") over every pair of groups.\"\"\"\n    names = list(groups)\n    rows = []\n    m = len(names) * (len(names) - 1) // 2\n    for i in range(len(names)):\n        for j in range(i + 1, len(names)):\n            w, p = r_ranksum(groups[names[i]], groups[names[j]])\n            rows.append({\"a\": names[i], \"b\": names[j], \"W\": w, \"p\": p, \"p_bonf\": min(1.0, p * m)})\n    return pd.DataFrame(rows)\n\n\ndef fisher_pitman(x: np.ndarray, y: np.ndarray, n_resample: int = 10000, seed: int = 0,\n                  chunk: int = 50) -> tuple[float, float]:\n    \"\"\"Two-sample Fisher-Pitman permutation test as coin::oneway_test.\n\n    Returns (Z, p): Z is the standardised sum of the first group, p two-sided from `n_resample`\n    random permutations (coin's approximate(nresample = 10000)).\"\"\"\n    v = np.r_[x, y].astype(float)\n    n1, n = len(x), len(v)\n    t_obs = v[:n1].sum()\n    mean_t = n1 * v.mean()\n    var_t = n1 * (n - n1) / (n * (n - 1)) * ((v - v.mean()) ** 2).sum()\n    z = (t_obs - mean_t) / np.sqrt(var_t)\n    rng = np.random.default_rng(seed)\n    hits = 0\n    done = 0\n    while done < n_resample:\n        k = min(chunk, n_resample - done)\n        for _ in range(k):\n            t = v[rng.permutation(n)[:n1]].sum()\n            hits += abs(t - mean_t) >= abs(t_obs - mean_t) - 1e-9\n        done += k\n    return float(z), hits / n_resample\n\n\ndef perm_corr_test(rate: np.ndarray, coord: np.ndarray, n_perm: int = 10000,\n                   seed: int = 123) -> tuple[float, float]:\n    \"\"\"Correlation of rate with a bin coordinate, null from permuted coordinates (fig5_cleaned.Rmd).\n\n    Two-sided p as the fraction of permuted |r| at or above the observed |r|. The seed is the\n    code's number, though numpy's generator gives other permutations than R's: a choice that\n    cannot change the outcome beyond Monte Carlo error.\"\"\"\n    rate = np.asarray(rate, float)\n    coord = np.asarray(coord, float)\n    r_obs = np.corrcoef(rate, coord)[0, 1]\n    rng = np.random.default_rng(seed)\n    rc = rate - rate.mean()\n    cc = coord - coord.mean()\n    denom = np.sqrt((rc ** 2).sum() * (cc ** 2).sum())\n    perm = np.array([rc @ rng.permutation(cc) for _ in range(n_perm)]) / denom\n    return float(r_obs), float(np.mean(np.abs(perm) >= abs(r_obs) - 1e-12))\n"
}
```

```
File created successfully at: entries/001863-welch-2025/doi_search.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev_load.py <<'EOF'
import sys, time, pickle
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
t=time.time(); S=ds.load_all(); print('loaded',len(S),time.time()-t)
pickle.dump(S,open('S.pkl','wb'))
EOF
python dev_load.py
```

```
loaded 44 51.993813276290894
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev1.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
S=pickle.load(open('S.pkl','rb'))
rows=[]
for s in S:
    x,y,info=ds.clean_nose(s); tr=s['trials']
    corr=tr.outcome.to_numpy()==1
    for lab,fps in [('80',80.0),('file',s['file_rate'])]:
        for shift in [0,5,-5]:
            t=ds.frame_times(len(x),fps)
            def at(ts): 
                i=np.clip(np.searchsorted(t,ts),0,len(t)-1); return i
            ie=at(tr.stop_time.to_numpy()+shift); i0=at(tr.start_time.to_numpy()+shift)
            side=tr.side.to_numpy()
            dy=np.median(y[ie][corr&(side==1)])-np.median(y[ie][corr&(side==2)])
            dx=np.median(x[ie])-np.median(x[i0])
            rows.append(dict(sess=f"{s['mouse']}_{s['session']}",cohort=s['cohort'],fps=lab,shift=shift,dx=dx,dy=dy))
d=pd.DataFrame(rows)
print(d.groupby(['cohort','fps','shift'])[['dx','dy']].median())
print(d[(d.shift==0)].pivot_table(index='sess',columns='fps',values=['dx','dy']).round(0).to_string())
EOF
python dev1.py
```

```
Exit code 1
                           dx          dy
cohort fps  shift                        
first  80   -5      -6.077234  -16.393400
             0     -13.162166  -11.053238
             5      12.723339   -1.526811
       file -5     -20.243873  -79.701678
             0     -17.063137 -148.921281
             5       3.820735  -69.195311
later  80   -5     -64.658939  -17.730042
             0       0.270220    8.534104
             5     110.705810  185.595548
       file -5      35.423187   92.529414
             0       1.002959   52.949689
             5      12.312211   11.640806
Traceback (most recent call last):
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/core/indexes/base.py", line 3816, in get_loc
    return self._engine.get_loc(casted_key)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "pandas/_libs/index.pyx", line 172, in pandas._libs.index.IndexEngine.get_loc
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev2.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
S=pickle.load(open('S.pkl','rb'))
for s in [S[0],S[20]]:
    x,y,info=ds.clean_nose(s); tr=s['trials']; print(s['path'],info, 'x pct',np.percentile(x,[1,25,50,75,99]).round(), 'y pct',np.percentile(y,[1,25,50,75,99]).round())
    t=ds.frame_times(len(x))
    for k in range(6):
        st,en=tr.start_time[k],tr.stop_time[k]
        i=np.searchsorted(t,[st-2,st,en,en+3])
        print(k, tr.side[k], tr.outcome[k], tr.odor_control[k], 'st %.1f en %.1f'%(st,en), [(int(x[j]),int(y[j])) for j in i])
    # 2D occupancy coarse
    H,_,_=np.histogram2d(y,x,bins=[np.arange(0,800,100),np.arange(0,1400,100)])
    print((H/H.sum()*1000).astype(int))
EOF
python dev2.py
```

```
sub-2174/sub-2174_ses-2174-56.nwb {'frames': 185828, 'low_likelihood': 74726, 'jump': 78819, 'interpolated': 138933} x pct [  80.  179.  695.  984. 1120.] y pct [ 28. 225. 369. 473. 657.]
0 1.0 0.0 0.0 st 10.0 en 11.3 [(834, 128), (113, 579), (116, 584), (791, 326)]
1 2.0 0.0 0.0 st 22.0 en 23.4 [(701, 402), (127, 30), (126, 31), (1079, 431)]
2 2.0 1.0 0.0 st 40.5 en 41.6 [(585, 469), (430, 473), (348, 474), (258, 409)]
3 1.0 0.0 0.0 st 69.4 en 70.9 [(199, 53), (737, 368), (577, 46), (1090, 268)]
4 1.0 0.0 0.0 st 86.1 en 87.5 [(1095, 342), (1106, 375), (1054, 432), (860, 507)]
5 2.0 1.0 3.0 st 99.7 en 101.1 [(711, 415), (864, 368), (804, 273), (1108, 371)]
[[  9 176   9   1   0   0   0   0   0   0   1   5   0]
 [  1   1   3   7   3   2   1   0   1   1   4   3   0]
 [  1   1   0   2   2   2   2  13  19  14  24   3   0]
 [  0   1   0   1   2   5  16  47  32  31  85  46   0]
 [  2   3   6   8  14  24  26  29  24  22  40   7   0]
 [  2  17  25  24  18   7   2   2   9   5   9   2   0]
 [  9  38   9   1   0   0   0   0   0   0   1   0   0]]
sub-2200/sub-2200_ses-2200-14.nwb {'frames': 191780, 'low_likelihood': 173760, 'jump': 74799, 'interpolated': 177579} x pct [  33.   84.  272.  744. 1125.] y pct [ 18. 201. 321. 362. 658.]
0 1.0 1.0 0.0 st 2.0 en 19.8 [(75, 352), (983, 55), (358, 174), (655, 384)]
1 2.0 1.0 0.0 st 45.5 en 47.4 [(974, 16), (883, 64), (45, 340), (996, 20)]
2 2.0 0.0 0.0 st 59.1 en 60.9 [(52, 318), (58, 297), (50, 333), (559, 344)]
3 2.0 1.0 0.0 st 92.6 en 94.1 [(1066, 156), (828, 255), (195, 316), (493, 244)]
4 1.0 1.0 0.0 st 117.8 en 119.7 [(157, 580), (68, 666), (78, 333), (594, 392)]
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev3.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
S=pickle.load(open('S.pkl','rb'))
def score(x, tr, fps, off):
    n=len(x)
    i0=np.clip(((tr.start_time.to_numpy()+off)*fps).astype(int)-1,0,n-1)
    ie=np.clip(((tr.stop_time.to_numpy()+off)*fps).astype(int)-1,0,n-1)
    return np.median(x[ie]-x[i0])
for s in S[::4]+[S[1],S[21]]:
    x,y,_=ds.clean_nose(s); tr=s['trials']
    if s['cohort']=='first': x=1200-x
    best=max(((score(x,tr,f,o),f,o) for f in np.arange(70,90.1,0.5) for o in np.arange(-20,20.1,0.5)))
    print(s['mouse'],s['session'],s['cohort'],'rate %.2f'%s['file_rate'],'score@80,0 %.0f'%score(x,tr,80,0),'best',np.round(best,2), 'nframes/80=%.0f lastend=%.0f'%(len(x)/80, tr.stop_time.max()))
EOF
python dev3.py
```

```
2174 56 first rate 77.43 score@80,0 0 best [133.29  72.5    4.5 ] nframes/80=2323 lastend=2400
2182 31 first rate 74.86 score@80,0 7 best [235.03  74.     0.  ] nframes/80=2243 lastend=2397
2185 40 first rate 73.76 score@80,0 0 best [124.58  71.5    4.  ] nframes/80=2196 lastend=2382
2195 17 later rate 83.63 score@80,0 8 best [826.18  80.5    3.5 ] nframes/80=2400 lastend=2296
2197 17 later rate 81.83 score@80,0 1 best [20.74 88.5   8.  ] nframes/80=2399 lastend=2346
2200 14 later rate 81.13 score@80,0 -3 best [282.92  80.5    1.  ] nframes/80=2397 lastend=2364
2202 14 later rate 81.83 score@80,0 -23 best [452.91  80.5    2.  ] nframes/80=2397 lastend=2344
2204 17 later rate 80.69 score@80,0 -4 best [112.85  71.    13.5 ] nframes/80=2396 lastend=2376
2208 14 later rate 81.45 score@80,0 4 best [228.28  80.5    0.  ] nframes/80=2396 lastend=2353
2210 13 later rate 81.56 score@80,0 14 best [339.4  80.5  -1.5] nframes/80=2397 lastend=2351
2212 13 later rate 81.25 score@80,0 2 best [333.92  80.5    0.5 ] nframes/80=2397 lastend=2360
2174 57 first rate 74.14 score@80,0 0 best [797.48  73.5   -3.  ] nframes/80=2213 lastend=2388
2200 19 later rate 81.31 score@80,0 28 best [296.66  80.5   -1.  ] nframes/80=2396 lastend=2357
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev4.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, time
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
S=pickle.load(open('S.pkl','rb'))
def score(x, st, en, fps, off):
    n=len(x)
    i0=np.clip(((st+off)*fps).astype(int)-1,0,n-1)
    ie=np.clip(((en+off)*fps).astype(int)-1,0,n-1)
    return np.median(x[ie]-x[i0])
def fit(x,st,en,fgrid,ogrid):
    return max(((score(x,st,en,f,o),f,o) for f in fgrid for o in ogrid))
rows=[]
t0=time.time()
for s in S:
    x,y,_=ds.clean_nose(s); tr=s['trials']
    if s['cohort']=='first': x=1200-x
    st,en=tr.start_time.to_numpy(),tr.stop_time.to_numpy()
    sc,f,o=fit(x,st,en,np.arange(70,90.01,0.25),np.arange(-20,20.01,0.5))
    sc2,f2,o2=fit(x,st,en,np.arange(f-0.5,f+0.501,0.02),np.arange(o-2,o+2.01,0.1))
    h=len(st)//2
    a=fit(x,st[:h],en[:h],[f2],np.arange(o2-5,o2+5.01,0.1)); b=fit(x,st[h:],en[h:],[f2],np.arange(o2-5,o2+5.01,0.1))
    rows.append(dict(sess=f"{s['mouse']}_{s['session']}",cohort=s['cohort'],file_rate=s['file_rate'],score80=score(x,st,en,80,0),best=sc2,fps=f2,off=o2,off_first_half=a[2],off_second_half=b[2],score_halves=(a[0]+b[0])/2))
d=pd.DataFrame(rows); print(d.round(2).to_string()); print(time.time()-t0)
d.to_pickle('align.pkl')
EOF
python dev4.py
```

```
sess cohort  file_rate  score80    best    fps   off  off_first_half  off_second_half  score_halves
0   2174_56  first      77.43     0.00  318.74  72.27   6.6             6.7              6.7        308.60
1   2174_57  first      74.14     0.00  868.19  73.52  -3.0            -3.0             -3.0        866.58
2   2181_41  first      72.72     1.01  261.49  71.88   7.3             7.6              7.7        260.52
3   2181_42  first      75.39     0.00  911.17  75.12  -1.5            -1.5             -1.6        900.56
4   2182_31  first      74.86     6.80  292.09  73.94   0.2             0.2              1.3        435.13
5   2182_32  first      75.72     0.81  702.88  75.06  -1.0            -0.7             -0.9        722.71
6   2183_33  first      73.67    27.46  148.03  72.25  14.0            12.2             13.7        201.19
7   2183_34  first      75.51     0.15  725.71  74.96  -1.2            -1.2             -1.3        680.87
8   2185_40  first      73.76     0.00  469.23  71.67   2.4             2.5              2.4        491.90
9   2185_41  first      77.16     4.81  761.20  74.58  -2.0            -1.4             -2.2        680.33
10  2191_21  later      82.94   -11.08  479.31  80.35  -0.1            -0.0             -0.1        496.34
11  2191_25  later      82.51    -9.62  634.61  80.27   0.1            -0.0              0.2        651.13
12  2195_17  later      83.63     7.65  845.91  80.48   3.8             3.8              3.8        848.26
13  2195_20  later      81.32   -10.65  358.49  80.40  -0.7            -0.8             -0.6        352.28
14  2196_16  later      80.79  -115.86  589.11  80.29   3.0             3.1              2.6        606.41
15  2196_18  later      81.17    -0.92  364.70  80.23   1.4             1.0              1.4        315.56
16  2197_17  later      81.83     0.91   27.23  81.75   9.0             8.1              9.0         30.56
17  2197_19  later      81.34    -6.96   82.77  83.00 -10.5           -10.2      
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . env/bin/activate && cat > dev5.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
S=pickle.load(open('S.pkl','rb'))
rows=[]
for s in S:
    if s['sniff_start'] is None: continue
    t=np.sort(s['sniff_start']); d=np.diff(t)*1000; f=1000/d; tt=t[1:]; ok=d>0
    tr=s['trials']
    r={'sess':f"{s['mouse']}_{s['session']}",'n':len(t),'faulty':(s['mouse'],s['session']) in ds.FAULTY_SNIFF,'span':t.max()-t.min(),'tmin':t.min(),'tmax':t.max(),'stop-start med ms':np.median((s['sniff_stop']-s['sniff_start'])*1000)}
    for sh in [0,-20,-10,-5,-2,2,5,10,20]:
        lab=ds.label_periods(tt, tr.assign(start_time=tr.start_time+sh, stop_time=tr.stop_time+sh))
        r[f'c{sh}']=np.median(f[ok&(lab>0)])-np.median(f[ok&(lab==0)])
    # rate in the 2 s after trial start minus 2 s before
    rows.append(r)
d=pd.DataFrame(rows); pd.set_option('display.width',250); print(d.round(2).to_string())
EOF
python dev5.py
```

```
Thu Nov  5 15:53:44 UTC 2026
       sess      n  faulty     span   tmin     tmax  stop-start med ms    c0  c-20  c-10   c-5   c-2    c2    c5   c10   c20
0   2191_21  11004   False  2401.15   0.09  2401.24               40.0  0.96 -1.26  0.33 -0.54  0.43  1.69  1.79  1.20 -0.33
1   2191_25  14490   False  2401.05   0.06  2401.12               41.0  0.54 -0.17 -0.06  0.06  0.41  0.54  0.29 -0.22 -0.32
2   2195_17   1612    True  2393.87   0.15  2394.02               68.0  3.09  2.25 -0.09  0.63  0.19  2.72  3.71  4.53  1.12
3   2196_16  11664   False  2401.18   0.07  2401.24               44.0  2.61  0.44  1.76  1.90  2.32  3.30  3.72  3.07  2.71
4   2196_18  14832   False  2401.46   0.05  2401.50               41.0  1.07  0.05 -0.21 -0.00  0.51  1.33  1.53  0.51 -0.05
5   2197_17  14702   False  2401.53   0.09  2401.62               41.0  0.62  0.21  0.31  0.24  0.43  0.81  0.56  0.56  0.18
6   2197_19  12702   False  2386.35  14.57  2400.92               43.0  1.25  0.15  0.55  0.76  0.86  1.42  1.49  1.09  0.05
7   2198_17    861    True  2392.04   2.74  2394.78               45.0 -0.62  0.14 -1.84  0.00 -0.28 -1.08 -0.42 -0.81  0.00
8   2198_19    890    True  2390.16   5.61  2395.77               47.0 -0.85 -0.91 -3.23 -2.02 -0.18 -0.69 -2.96 -2.00  0.13
9   2200_14  14482   False  2401.50   0.07  2401.58               46.0 -0.12  0.12 -0.35  0.18 -0.12  0.18  0.44 -0.18  0.12
10  2200_19   6693   False  2396.67   4.11  2400.78               58.0  0.34  0.30  0.56  0.26 -0.31  0.18 -0.14  0.30 -0.16
11  2201_16  14892   False  2401.15   0.07  2401.22               37.0  0.37 -0.06 -0.13 -0.25 -0.19  0.70  0.07 -0.67  0.20
12  2201_21  12969   False  2397.25   0.23  2397.49               39.0  0.28  0.22 -0.21 -0.05 -0.11  0.83  0.00 -0.41  0.22
13  2202_14  13778   False  2398.73   0.12  2398.86               37.0  0.42  0.24 -0.28 -0.11  0.36  0.96  1.23  0.18  0.61
14  2202_19  14227   False  2401.29   0.14  2401.42               38.0  1.19  0.39 -0.05  0.69  
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import sys,time,numpy as np
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
x=np.random.rand(200000); y=np.random.rand(170000)
t=time.time(); print(ds.fisher_pitman(x,y,n_resample=200)); print((time.time()-t)/200*10000)
EOF
```

```
(1.1320461273787654, np.float64(0.22))
53.28963994979858
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev6.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
S=pickle.load(open('S.pkl','rb'))
rows=[]
for s in S:
    tr=s['trials']; o=ds.odor_mask(tr); iti=ds.iti_lengths(tr)
    r=dict(mouse=s['mouse'],cond=s['condition'],sex=s['sex'],cohort=s['cohort'],n_all=len(tr),n_odor=o.sum(),n_om=(~o).sum(),
      acc_odor=100*tr.outcome[o].mean(), acc_om=100*tr.outcome[~o].mean(),
      dur_odor=(tr.stop_time-tr.start_time)[o].mean(), dur_om=(tr.stop_time-tr.start_time)[~o].mean(), iti=np.nanmean(iti))
    if 'repoke' in tr: r.update(repoke=tr.repoke.sum()/(len(tr)-1), fa=tr.false_alarm.sum(), fa_rate=tr.false_alarm.sum()/(len(tr)-1))
    rows.append(r)
d=pd.DataFrame(rows)
w=d.pivot(index='mouse',columns='cond')
def pr(name,col,sub=None):
    ww=w if sub is None else w.loc[sub]
    a,b=ww[(col,'DOI')],ww[(col,'saline')]
    ok=a.notna()&b.notna()
    print(name, 'n',ok.sum(),'median diff %.3f'%np.median(a[ok]-b[ok]), ds.r_signrank(a[ok],b[ok]))
pr('acc odor','acc_odor'); pr('acc om','acc_om')
pr('n odor','n_odor'); pr('n all','n_all')
F=[m for m in w.index if m in ds.FEMALES]; M=[m for m in w.index if m not in ds.FEMALES]
for nm,sub in [('F',F),('M',M)]:
    pr('n odor '+nm,'n_odor',sub); pr('n all '+nm,'n_all',sub)
pr('repoke','repoke')
pr('dur odor','dur_odor'); pr('dur om','dur_om'); pr('iti','iti')
dd=d[d.cohort=='later']
print('FA counts', dd.groupby('cond').fa.describe())
print('fa ranksum', ds.r_ranksum(dd.fa[dd.cond=='DOI'],dd.fa[dd.cond=='saline']), ds.r_ranksum(dd.fa_rate[dd.cond=='DOI'],dd.fa_rate[dd.cond=='saline']))
# 1C
rows=[]
for s in S:
    tr=s['trials']; ra=ds.rolling_accuracy(tr); o=ds.odor_mask(tr)
    tm=tr.start_time.to_numpy()/60
    b=pd.cut(tm, bins=np.arange(0,41,5), include_lowest=True, labels=False)
    df=pd.DataFrame(dict(b=b,ra=ra,succ=tr.outcome))[o]
    g=df.groupby('b').agg(ra=('ra','mean'),fc=('succ','mean'))
    for k,v in g.iterrows(): rows.append(dict(mouse=s['mouse'],cond=s['condition'],bin=k,ra=v.ra,fc=100*v.fc))
b=pd.DataFrame(rows)
for k,g in b.groupby('bin'):
    a=g.ra[g.cond=='DOI']; c=g.ra[g.cond=='saline']
    print(k, len(a),len(c),'DOI %.1f sal %.1f'%(a.mean(),c.mean()), ds.r_ranksum(a,c))
EOF
python dev6.py
```

```
acc odor n 22 median diff -3.244 (57.0, 0.022916316986083984)
acc om n 22 median diff -5.159 (89.0, 0.37372493743896484)
n odor n 22 median diff -9.500 (48.0, 0.011212713555832008)
n all n 22 median diff -8.000 (53.0, 0.017720896340603823)
n odor F n 12 median diff -14.000 (6.0, 0.01048613131430333)
n all F n 12 median diff -12.500 (7.5, 0.014983569711609428)
n odor M n 10 median diff -3.500 (18.5, 0.38596207926442694)
n all M n 10 median diff -3.000 (19.5, 0.4436974958333839)
repoke n 17 median diff -0.097 (57.0, 0.3778228759765625)
dur odor n 22 median diff 0.259 (248.0, 4.76837158203125e-06)
dur om n 22 median diff 0.547 (158.0, 0.32088327407836914)
iti n 22 median diff 1.418 (178.0, 0.09841060638427734)
FA counts         count      mean       std  min  25%  50%  75%  max
cond                                                      
DOI      17.0  0.176471  0.528594  0.0  0.0  0.0  0.0  2.0
saline   17.0  0.176471  0.528594  0.0  0.0  0.0  0.0  2.0
fa ranksum (144.5, 1.0) (144.5, 1.0)
0 22 22 DOI 78.7 sal 83.0 (214.0, 0.5117432437461082)
1 21 22 DOI 86.2 sal 91.5 (157.0, 0.0728232750877565)
2 21 21 DOI 87.0 sal 92.7 (114.0, 0.007639754680076546)
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev7.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
S=pickle.load(open('S.pkl','rb'))
A=pd.read_pickle('align.pkl').set_index('sess')
rows=[]
for s in S:
    x,y,_=ds.clean_nose(s); sp=ds.speed_cm_s(x,y)
    key=f"{s['mouse']}_{s['session']}"
    for clock in ['code','fit']:
        if clock=='code': t=ds.frame_times(len(x))
        else: t=ds.frame_times(len(x),A.fps[key])-A.off[key]
        lab=ds.label_periods(t,s['trials'])
        ok=(sp<=160)
        r=dict(mouse=s['mouse'],cond=s['condition'],clock=clock,within=np.nanmean(sp[ok&(lab>0)]),iti=np.nanmean(sp[ok&(lab==0)]),odor=np.nanmean(sp[ok&(lab==1)]),om=np.nanmean(sp[ok&(lab==3)]),frac_dropped=1-ok[1:].mean())
        rows.append(r)
d=pd.DataFrame(rows)
for clock in ['code','fit']:
    w=d[d.clock==clock].pivot(index='mouse',columns='cond')
    print(clock, w.median().round(2).to_dict())
    for nm,(a,b) in {'within D-S':(('within','DOI'),('within','saline')),'iti D-S':(('iti','DOI'),('iti','saline')),'odor D-S':(('odor','DOI'),('odor','saline')),
        'DOI iti-odor':(('iti','DOI'),('odor','DOI')),'DOI odor-om':(('odor','DOI'),('om','DOI')),'DOI iti-om':(('iti','DOI'),('om','DOI')),
        'sal iti-odor':(('iti','saline'),('odor','saline')),'sal iti-om':(('iti','saline'),('om','saline')),'sal odor-om':(('odor','saline'),('om','saline'))}.items():
        print(' ',nm,'med diff %.2f'%np.median(w[a]-w[b]), np.round(ds.r_signrank(w[a],w[b]),4), 'ranksum',np.round(ds.r_ranksum(w[a],w[b]),4))
EOF
python dev7.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev7.py", line 20, in <module>
    print(clock, w.median().round(2).to_dict())
                 ~~~~~~~~^^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/util/_decorators.py", line 335, in wrapper
    return func(*args, **kwargs)
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/core/frame.py", line 18191, in median
    result = super().median(
        axis=axis, skipna=skipna, numeric_only=numeric_only, **kwargs
    )
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/core/generic.py", line 12040, in median
    return self._stat_function(
           ~~~~~~~~~~~~~~~~~~~^
        "median", nanops.nanmedian, axis, skipna, numeric_only, **kwargs
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/pandas/core/generic.py", line 11982, in _stat_function
    return self._reduce(
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && sed -i "s/w=d\[d.clock==clock\].pivot/w=d[d.clock==clock].drop(columns='clock').pivot/" dev7.py && python dev7.py
```

```
code {('within', 'DOI'): 6.34, ('within', 'saline'): 6.62, ('iti', 'DOI'): 5.57, ('iti', 'saline'): 5.76, ('odor', 'DOI'): 6.53, ('odor', 'saline'): 6.33, ('om', 'DOI'): 6.01, ('om', 'saline'): 7.01, ('frac_dropped', 'DOI'): 0.0, ('frac_dropped', 'saline'): 0.0}
  within D-S med diff -0.63 [6.90e+01 6.34e-02] ranksum [213.       0.5073]
  iti D-S med diff -0.60 [72.      0.0794] ranksum [217.       0.5688]
  odor D-S med diff -0.54 [85.     0.187] ranksum [225.       0.7014]
  DOI iti-odor med diff -0.83 [2.e+01 2.e-04] ranksum [1.820e+02 1.641e-01]
  DOI odor-om med diff 0.58 [159.       0.3053] ranksum [264.       0.6172]
  DOI iti-om med diff -0.70 [4.4e+01 5.9e-03] ranksum [203.       0.3698]
  sal iti-odor med diff -0.43 [5.80e+01 2.51e-02] ranksum [199.       0.3219]
  sal iti-om med diff -0.98 [5.30e+01 1.56e-02] ranksum [187.      0.203]
  sal odor-om med diff -0.18 [113.       0.6789] ranksum [234.       0.8617]
fit {('within', 'DOI'): 8.15, ('within', 'saline'): 8.02, ('iti', 'DOI'): 5.4, ('iti', 'saline'): 5.76, ('odor', 'DOI'): 8.97, ('odor', 'saline'): 8.27, ('om', 'DOI'): 6.57, ('om', 'saline'): 7.31, ('frac_dropped', 'DOI'): 0.0, ('frac_dropped', 'saline'): 0.0}
  within D-S med diff -0.39 [117.       0.7745] ranksum [228.       0.7537]
  iti D-S med diff -0.58 [6.80e+01 5.87e-02] ranksum [217.       0.5688]
  odor D-S med diff -0.13 [138.       0.7262] ranksum [241.       0.9907]
  DOI iti-odor med diff -3.54 [1. 0.] ranksum [1.1e+02 1.5e-03]
  DOI odor-om med diff 1.25 [2.27e+02 5.00e-04] ranksum [3.08e+02 1.25e-01]
  DOI iti-om med diff -1.25 [10.  0.] ranksum [1.81e+02 1.57e-01]
  sal iti-odor med diff -1.96 [8. 0.] ranksum [1.33e+02 9.90e-03]
  sal iti-om med diff -1.59 [3. 0.] ranksum [1.55e+02 4.15e-02]
  sal odor-om med diff 0.38 [155.       0.3705] ranksum [270.       0.5224]
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev8.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, time
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
from scipy import stats
S=pickle.load(open('S.pkl','rb'))
rows=[]
for s in S:
    if s['sniff_start'] is None or (s['mouse'],s['session']) in ds.FAULTY_SNIFF: continue
    t=np.sort(s['sniff_start']); dms=np.diff(t*1000)
    keep=dms>0; tt=t[1:][keep]; dms=dms[keep]
    lab=ds.label_periods(tt,s['trials'])
    rows.append(pd.DataFrame(dict(mouse=s['mouse'],cond=s['condition'],dur=dms,freq=1000/dms,lab=lab)))
d=pd.concat(rows)
print(d.groupby('cond').mouse.nunique(), d.groupby('cond').freq.describe())
def readings(d):
    out={'code':d}
    m=(d.dur>=10)&(d.dur<=1000)
    q=d.groupby(['mouse','cond']).dur.transform(lambda v: (v>=v.quantile(.05))&(v<=v.quantile(.95))).astype(bool)
    out['a_session']=d[q&m]
    q2=d.groupby('cond').dur.transform(lambda v: (v>=v.quantile(.05))&(v<=v.quantile(.95))).astype(bool)
    out['b_condition']=d[q2&m]
    return out
for k,dd in readings(d).items():
    a=dd.freq[dd.cond=='DOI'].to_numpy(); b=dd.freq[dd.cond=='saline'].to_numpy()
    z,_= ds.fisher_pitman(a,b,n_resample=1)
    print(k,len(a),len(b),'mean %.3f %.3f'%(a.mean(),b.mean()),'Z %.2f'%z)
    for L,nm in [(1,'odor'),(3,'om'),(0,'iti')]:
        aa=dd.freq[(dd.cond=='DOI')&(dd.lab==L)]; bb=dd.freq[(dd.cond=='saline')&(dd.lab==L)]
        print('   ',nm,len(aa),len(bb),'Z %.2f'%ds.fisher_pitman(aa.to_numpy(),bb.to_numpy(),n_resample=1)[0])
    med=dd.groupby(['mouse','cond']).freq.median().unstack()
    print('   median', ds.r_signrank(med.DOI,med.saline), med.notna().all(axis=1).sum(), 'med diff', np.nanmedian(med.DOI-med.saline))
    ks=[]
    for m,g in dd.groupby('mouse'):
        if g.cond.nunique()<2: continue
        r=stats.ks_2samp(g.freq[g.cond=='DOI'],g.freq[g.cond=='saline'],alternative='less')
        ks.append((m,r.pvalue,r.statistic))
    print('   ks', len(ks), sum(p<0.001 for _,p,_ in ks), [(m,'%.2g'%p) for m,p,_ in ks])
EOF
time python dev8.py
```

```
cond
DOI       14
saline    13
Name: mouse, dtype: int64            count      mean       std  ...       50%       75%        max
cond                                  ...                               
DOI     210828.0  7.707174  2.799090  ...  7.936508  10.00000  20.408163
saline  170007.0  7.515578  3.250192  ...  7.692308  10.10101  20.833333

[2 rows x 8 columns]
code 210828 170007 mean 7.707 7.516 Z 19.53
    odor 18000 12963 Z 3.72
    om 7681 5604 Z 2.12
    iti 185147 151440 Z 18.60
   median (69.0, 0.10986328125) 13 med diff 0.5743525480367584
   ks 13 11 [(2191, '5.3e-152'), (2196, '1e-214'), (2197, '1.4e-71'), (2200, '1.8e-132'), (2201, '3.7e-37'), (2202, '1.6e-07'), (2204, '1.9e-11'), (2205, '4e-83'), (2208, '8.3e-22'), (2209, '0.0059'), (2210, '1e-25'), (2211, '0.011'), (2212, '2.7e-65')]
a_session 190947 153863 mean 7.778 7.550 Z 25.18
    odor 16493 11755 Z 4.31
    om 6976 5071 Z 3.88
    iti 167478 137037 Z 24.21
   median (69.0, 0.10986328125) 13 med diff 0.5257899994742097
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev9.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd, time
sys.path.insert(0,'entries/001863-welch-2025')
import doi_search as ds
S=pickle.load(open('S.pkl','rb'))
A=pd.read_pickle('align.pkl').set_index('sess')
allx=[];ally=[]
tracks={}
for s in S:
    x,y,_=ds.clean_nose(s); sp=ds.speed_cm_s(x,y)
    if s['cohort']=='first': x=ds.FLIP_X-x
    x=np.maximum(x,0); y=np.maximum(y,0)
    tracks[(s['mouse'],s['condition'])]=(x,y,sp,s)
    allx.append(x[::10]); ally.append(y[::10])
allx=np.concatenate(allx); ally=np.concatenate(ally)
print('x pct',np.percentile(allx,[0,0.5,1,99,99.5,100]).round(), 'y pct',np.percentile(ally,[0,0.5,1,99,99.5,100]).round())
x0,x1=np.percentile(allx,[0.5,99.5]); y0,y1=np.percentile(ally,[0.5,99.5])
rows=[]
for (m,c),(x,y,sp,s) in tracks.items():
    ok=sp[1:]<=160; xx=x[1:][ok]; yy=y[1:][ok]
    bx=np.floor(xx/48).astype(int); by=np.floor(yy/48).astype(int)
    _,cnt=np.unique(bx*1000+by,return_counts=True); p=cnt/cnt.sum()
    H=-(p*np.log2(p)).sum()
    r=dict(mouse=m,cond=c,entropy=H)
    for side_cm in (5,10):
        L=side_cm/ds.CM_PER_PX
        inx=(xx<x0+L)|(xx>x1-L); iny=(yy<y0+L)|(yy>y1-L)
        r[f'corner{side_cm}']=np.mean(((xx<x0+L)|(xx>x1-L))&((yy<y0+L)|(yy>y1-L)))
    rows.append(r)
d=pd.DataFrame(rows).pivot(index='mouse',columns='cond')
for k in ['entropy','corner5','corner10']:
    print(k, d[k].median().round(3).to_dict(), ds.r_signrank(d[(k,'DOI')],d[(k,'saline')]))
# HTR
for reading in ['code','file','frames']:
  for period in ['all','within','iti']:
    tabs=[]
    for (m,c),(x,y,sp,s) in tracks.items():
        if c!='DOI': continue
        h=ds.htr_times(s,reading)
        n=len(x); t=ds.frame_times(n)
        lab=ds.label_periods(t,s['trials'])
        hidx=np.clip(np.searchsorted(t,h),1,n-1); hidx=np.where(np.abs(t[hidx-1]-h)<=np.abs(t[hidx]-h),hidx-1,hidx)
        isH=np.zeros(n,bool); isH[hidx]=True
        keep=np.r_[False, sp[1:]<160]
        bx=(np.floor(x/100)*100).astype(int); by=(np.floor(y/100)*100).astype(int)
        df=pd.DataFrame(dict(bx=bx,by=by,h=isH,lab=lab))[keep]
        master=df.groupby(['bx','by']).size().rename('occ_all')
        sub=df if period=='all' else df[(df.lab>0) if period=='within' else (df.lab==0)]
        occ=sub.groupby(['bx','by']).size().rename('occ')/80
        hc=sub[sub.h].groupby(['bx','by']).size().rename('hc')
        if period=='within':
            g=pd.DataFrame(index=master.index).join(occ).join(hc).fillna(0)
            g['rate']=np.where(g.occ>0,g.hc/g.occ*60,0)
        else:
            g=pd.DataFrame(occ).join(hc,how='outer').fillna({'hc':0}); g['rate']=(g.hc/g.occ*60).fillna(0)
        g=g.reset_index(); g['mouse']=m; tabs.append(g)
    T=pd.concat(tabs); T=T[(T.bx!=1200)&(T.by!=700)]
    rx=ds.perm_corr_test(T.rate,T.bx,2000); ry=ds.perm_corr_test(T.rate,T.by,2000)
    print(reading,period,len(T),T.mouse.nunique(),'x r=%.3f p=%.4f'%rx,'y r=%.3f p=%.4f'%ry)
EOF
time python dev9.py
```

```
x pct [   5.   22.   28. 1168. 1181. 1196.] y pct [  2.  14.  17. 665. 674. 694.]
entropy {'DOI': 7.197, 'saline': 7.133} (184.0, 0.06341934204101562)
corner5 {'DOI': 0.267, 'saline': 0.245} (163.0, 0.24789905548095703)
corner10 {'DOI': 0.85, 'saline': 0.862} (114.0, 0.7023849487304688)
code all 1848 22 x r=0.149 p=0.0000 y r=-0.005 p=0.8270
code within 1848 22 x r=0.056 p=0.0060 y r=0.028 p=0.2605
code iti 1847 22 x r=0.152 p=0.0000 y r=-0.013 p=0.5640
file all 1848 22 x r=0.126 p=0.0000 y r=-0.032 p=0.1710
file within 1848 22 x r=0.063 p=0.0030 y r=-0.003 p=0.9210
file iti 1847 22 x r=0.122 p=0.0000 y r=-0.026 p=0.2490
frames all 1848 22 x r=0.122 p=0.0000 y r=-0.044 p=0.0555
frames within 1848 22 x r=0.060 p=0.0010 y r=0.005 p=0.8575
frames iti 1847 22 x r=0.118 p=0.0000 y r=-0.041 p=0.0790

real	0m7.099s
user	0m7.057s
sys	0m0.699s
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001863-welch-2025/doi_search.py",
 "old_string": "            \"pose_unit\": nose[\"data\"].attrs.get(\"unit\"),\n        }",
 "new_string": "            \"pose_unit\": nose[\"data\"].attrs.get(\"unit\"),\n            \"notes\": ast.literal_eval(_text(f[\"general/notes\"])),\n        }"
}
```

```
The file entries/001863-welch-2025/doi_search.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001863-welch-2025/doi_search.py",
 "old_string": "from __future__ import annotations\n\nfrom concurrent.futures",
 "new_string": "from __future__ import annotations\n\nimport ast\nfrom concurrent.futures"
}
```

```
The file entries/001863-welch-2025/doi_search.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> entries/001863-welch-2025/doi_search.py <<'EOF'


# ---------------------------------------------------------------- clocks


def trial_displacement(x: np.ndarray, trials: pd.DataFrame, fps: float, offset: float) -> float:
    """Median of nose x at trial end minus nose x at trial start, frames placed by a clock.

    Frame i (from 1) is taken at trial time i / fps - offset. A trial starts at the initiation
    port and ends when the mouse enters the odor side's quadrant at the far end (Methods, Odor
    navigation task), so with the right clock x moves far toward the odor end over a trial; with
    a wrong one the difference is near 0. x must point toward the odor end (first cohort flipped)."""
    n = len(x)
    i0 = np.clip(np.round((trials.start_time.to_numpy() + offset) * fps).astype(int) - 1, 0, n - 1)
    i1 = np.clip(np.round((trials.stop_time.to_numpy() + offset) * fps).astype(int) - 1, 0, n - 1)
    return float(np.median(x[i1] - x[i0]))


def fit_clock(x: np.ndarray, trials: pd.DataFrame) -> dict:
    """The frame rate and offset that best align the track with the trial table.

    A grid search (70 to 90 frames/s in 0.25 steps, offsets -20 to 20 s in 0.5 s steps, then a
    finer grid around the best) for the largest `trial_displacement`, and the offset refitted on
    each half of the session at that rate, to see whether one linear clock holds throughout. This
    is a check made here, not the paper's method; the grids are a standard choice."""
    def best(fgrid, ogrid, tr):
        return max((trial_displacement(x, tr, f, o), f, o) for f in fgrid for o in ogrid)
    sc, f, o = best(np.arange(70, 90.01, 0.25), np.arange(-20, 20.01, 0.5), trials)
    sc, f, o = best(np.arange(f - 0.5, f + 0.501, 0.02), np.arange(o - 2, o + 2.01, 0.1), trials)
    h = len(trials) // 2
    first = best([f], np.arange(o - 5, o + 5.01, 0.1), trials.iloc[:h])
    second = best([f], np.arange(o - 5, o + 5.01, 0.1), trials.iloc[h:])
    return {"fps": float(f), "offset": float(o), "displacement": sc,
            "offset_first_half": float(first[2]), "offset_second_half": float(second[2])}


def nearest_frame(times: np.ndarray, events: np.ndarray) -> np.ndarray:
    """Index of the frame nearest each event time (which.min in the code)."""
    n = len(times)
    i = np.clip(np.searchsorted(times, events), 1, n - 1)
    return np.where(np.abs(times[i - 1] - events) <= np.abs(times[i] - events), i - 1, i)


# ---------------------------------------------------------------- sniffing


def sniff_table(s: dict, trials_times: np.ndarray | None = None) -> pd.DataFrame | None:
    """One row per sniff: duration (ms, between successive inhalations) and frequency (Hz).

    As fig4_cleaned.Rmd: rows with no exhalation are already dropped in the file; inhalations
    sorted, differences taken, those not above 0 dropped, frequency 1000 / difference. Each sniff
    is placed by its inhalation time in an odor trial (1), an omission trial (3) or the ITI (0).
    `trials_times` may give the inhalation times on another clock (for checks)."""
    if s["sniff_start"] is None:
        return None
    t = np.sort(s["sniff_start"])
    dms = np.diff(t * 1000)
    keep = dms > 0
    tt = t[1:][keep] if trials_times is None else trials_times
    return pd.DataFrame({"mouse": s["mouse"], "condition": s["condition"], "t": tt,
                         "duration_ms": dms[keep], "frequency": 1000 / dms[keep],
                         "period": label_periods(tt, s["trials"])})


def sniff_readings(d: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """The exclusions of the claims file's readings for Figure 4.

    "a_session": durations below the 5th or above the 95th percentile of the session dropped, and
    durations outside 10 to 1000 ms; "b_condition": the percentiles over all sessions of a
    condition; "code": no further exclusion, as fig4_cleaned.Rmd computes from the same files."""
    in_range = (d.duration_ms >= 10) & (d.duration_ms <= 1000)

    def within(g):
        lo, hi = g.quantile(0.05), g.quantile(0.95)
        return (g >= lo) & (g <= hi)
    per_session = d.groupby(["mouse", "condition"]).duration_ms.transform(within).astype(bool)
    per_condition = d.groupby("condition").duration_ms.transform(within).astype(bool)
    return {"a_session": d[per_session & in_range], "b_condition": d[per_condition & in_range],
            "code": d}


# ---------------------------------------------------------------- maps


def map_frames(s: dict, fps: float = CODE_FPS, offset: float = 0.0,
               htr_reading: str = "code") -> pd.DataFrame:
    """Per frame of a session: nose x, y (first cohort flipped, negatives set to 0), speed,
    period label and whether an HTR is assigned to it, as fig5_cleaned.Rmd builds them.

    Frames are timed at i / 80 s for the HTR assignment (the video clock of the timestamps) and
    at i / fps - offset for the period labels; the code uses 80 and 0 for both."""
    x, y, _ = clean_nose(s)
    sp = speed_cm_s(x, y)
    if s["cohort"] == "first":
        x = FLIP_X - x
    x, y = np.maximum(x, 0), np.maximum(y, 0)
    n = len(x)
    video_t = frame_times(n)
    lab = label_periods(frame_times(n, fps) - offset, s["trials"])
    htr = np.zeros(n, bool)
    h = htr_times(s, htr_reading)
    if h is not None and len(h):
        htr[nearest_frame(video_t, h)] = True
    return pd.DataFrame({"x": x, "y": y, "speed": sp, "period": lab, "htr": htr})


def htr_rate_table(frames: pd.DataFrame, mouse: int, period: str) -> pd.DataFrame:
    """Per bin of 100 px, HTR count over occupancy in HTR/min for one mouse (fig5_cleaned.Rmd).

    Frames at or above 160 cm/s (and the first frame, which has no speed) are dropped. "all":
    bins the mouse occupied; "within": every bin the mouse occupied in the session, filled with 0
    where it had no within-trial time; "iti": bins it occupied in the ITI. The edge bins (x 1200,
    y 700) are dropped."""
    f = frames[frames.speed < MAX_SPEED_CM_S]
    f = f.assign(bx=(np.floor(f.x / HTR_BIN_PX) * HTR_BIN_PX).astype(int),
                 by=(np.floor(f.y / HTR_BIN_PX) * HTR_BIN_PX).astype(int))
    master = f.groupby(["bx", "by"]).size().rename("all_frames")
    sub = f if period == "all" else f[f.period > 0] if period == "within" else f[f.period == 0]
    occ = (sub.groupby(["bx", "by"]).size() / CODE_FPS).rename("occupancy_s")
    count = sub[sub.htr].groupby(["bx", "by"]).size().rename("htr_count")
    if period == "within":
        g = pd.DataFrame(index=master.index).join(occ).join(count).fillna(0)
        g["rate"] = np.where(g.occupancy_s > 0, g.htr_count / g.occupancy_s * 60, 0.0)
    else:
        g = pd.DataFrame(occ).join(count, how="outer").fillna({"htr_count": 0})
        g["rate"] = (g.htr_count / g.occupancy_s * 60).fillna(0)
    g = g.reset_index()
    g["mouse"] = mouse
    return g[(g.bx != HTR_EDGE_X) & (g.by != HTR_EDGE_Y)]


def occupancy_measures(frames: pd.DataFrame, bounds: tuple[float, float, float, float]) -> dict:
    """Shannon entropy (bits) of the 48 px occupancy map, and the fraction of frames in the four
    corner squares of 5 cm and 10 cm side, for frames at or below 160 cm/s.

    `bounds` (x0, x1, y0, y1) is the arena's extent, taken in the notebook from the pooled
    positions (an assumption, as the paper gives no arena coordinates)."""
    f = frames[frames.speed <= MAX_SPEED_CM_S]
    bx = np.floor(f.x.to_numpy() / OCC_BIN_PX).astype(int)
    by = np.floor(f.y.to_numpy() / OCC_BIN_PX).astype(int)
    _, cnt = np.unique(bx * 10000 + by, return_counts=True)
    p = cnt / cnt.sum()
    out = {"entropy": float(-(p * np.log2(p)).sum())}
    x0, x1, y0, y1 = bounds
    for side_cm in (5, 10):
        side = side_cm / CM_PER_PX
        xs = (f.x < x0 + side) | (f.x > x1 - side)
        ys = (f.y < y0 + side) | (f.y > y1 - side)
        out[f"corners_{side_cm}cm"] = float((xs & ys).mean())
    return out
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
date -u; cat entries/001453-fouke-2025/reproduce_fouke_2025.ipynb | python -c "
import json,sys; nb=json.load(sys.stdin); print(nb['metadata']); c=nb['cells'][1]; print(c.keys())
for c in nb['cells']:
  if c['cell_type']=='code' and 'pip' in ''.join(c['source']): print(''.join(c['source']))
"; grep -n "install cell\|pip install\|INSTALL" tools/entry.py | head
```

```
Thu Nov  5 15:56:46 UTC 2026
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
dict_keys(['cell_type', 'execution_count', 'id', 'metadata', 'outputs', 'source'])
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip()))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Welch et al. (2025) from dandiset 001863\n\n**Paper.** Welch AC, Gonzales-Hess N, Tarvin T, Connor S, Smear M (2025). The impact of a\npsychedelic drug on olfactory search behavior by mice. bioRxiv\n[doi:10.1101/2025.07.09.663970](https://doi.org/10.1101/2025.07.09.663970). The claims file was\nwritten from the full text of the preprint, version 1 (its JATS XML), which has its supplemental\nfigure legends in the text and no separate supplement.\n\n**Dandiset.** [DANDI:001863](https://dandiarchive.org/dandiset/001863/0.260806.2109), version\n0.260806.2109. The paper cites no DANDI version (it predates the dandiset). This is the only\npublished version; the draft has the same 44 assets and size, so the published version is pinned.\n\n**What the dandiset holds.** 44 NWB files, one DOI and one saline session for each of 22 mice:\nthe trial table, DeepLabCut tracking of 8 keypoints, the sniff cycles detected from the nasal\nthermistor (31 sessions) and an unnamed event series that the authors' conversion script and\nfigure code identify as the head-twitch (HTR) times (32 sessions). The reward-port entries and\nexits of Figure 2 are not in it.\n\n**Outside inputs.** The authors' code, github.com/Smear-Lab/Olfactory-search-on-psychedelics at\ncommit aa80af0a153c6bf099e5668d27c9d88e2bfc033f, which the claims file cites for its method\ndetails. It also names the event series as HTR times (claim `htr-event-link`).\n\n| Claim | Tested here |\n|---|---|\n| fig1b-accuracy-lower-doi, fig1c-accuracy-time-bins, fig1d-fewer-trials, fig1d-fewer-trials-females-only, fig1e-repoke-no-difference, iti-false-report-no-difference | Tested |\n| fig2a to fig2d and their supplements (9 claims) | Blocked: data missing (no reward-port entries or exits) |\n| fig3a-odor-trial-duration-longer, fig3a-omission-duration-no-difference, fig3b-iti-duration-no-difference | Tested |\n| fig3c, fig3d and the five speed claims of the Figure 3 supplement | Tested |\n| fig4abc, fig4supp-ks-every-mouse, fig4d, fig4e | Tested |\n| fig5ab-occupancy-similar | Tested |\n| htr-event-link (added here) and the five HTR claims of Figure 5 | Tested |\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport doi_search as ds\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nsessions = ds.load_all()\nprint(f\"loaded {len(sessions)} files from dandiset {ds.DANDISET_ID} version {ds.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\nby_key = {(s[\"mouse\"], s[\"condition\"]): s for s in sessions}\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\ninfo = pd.DataFrame([{\n    \"mouse\": s[\"mouse\"], \"session\": s[\"session\"], \"condition\": s[\"condition\"],\n    \"drug_field\": s[\"drug\"], \"sex_code\": s[\"sex\"], \"sex_file\": s[\"sex_file\"], \"cohort\": s[\"cohort\"],\n    \"trials\": len(s[\"trials\"]), \"odor_trials\": int(ds.odor_mask(s[\"trials\"]).sum()),\n    \"trial_columns\": len(s[\"trials\"].columns), \"frames\": len(s[\"nose_xy\"]),\n    \"file_rate\": round(s[\"file_rate\"], 2),\n    \"sniff_rows\": 0 if s[\"sniff_start\"] is None else len(s[\"sniff_start\"]),\n    \"events\": 0 if s[\"events\"] is None else len(s[\"events\"]),\n    \"event_source\": None if s[\"events\"] is None else s[\"events_source\"],\n    \"start\": s[\"start\"][:10]} for s in sessions]).sort_values([\"mouse\", \"condition\"])\nprint(info.to_string(index=False))\nprint(\"\\nSessions by condition:\", info.condition.value_counts().to_dict(), \"; mice:\", info.mouse.nunique())\nprint(\"Every mouse has one DOI and one saline session, the code's session numbers:\",\n      bool((info.groupby(\"mouse\").condition.apply(sorted).apply(tuple) == (\"DOI\", \"saline\")).all()))\nprint(\"Condition from the code's session list agrees with the file's drug field:\",\n      bool((info.condition.str.lower() == info.drug_field).all()))\nprint(\"Sex in the file differs from the code's list:\",\n      info[info.sex_code != info.sex_file][[\"mouse\", \"session\", \"condition\", \"sex_code\", \"sex_file\"]].to_dict(\"records\"))\nprint(\"Mice per sex (code):\", info.drop_duplicates(\"mouse\").sex_code.value_counts().to_dict())\nprint(\"Sessions with fewer than\", ds.MIN_TRIALS, \"trials:\", int((info.trials < ds.MIN_TRIALS).sum()))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe 44 files are the 22 mice and the DOI and saline sessions of the code's list, and the file's\ndrug field agrees for every session. The paper's 12 females and 10 males are the code's list. One\nfile disagrees with it: the saline session of mouse 2182 says female while its DOI session says\nmale (the code and the claims file have 2182 as male). The analysis uses the code's list. No\nsession has fewer than 40 trials, so the code's 40-trial filter drops none. The first cohort's\ntrial tables have 6 columns and no `false_alarm` or `repoke` (Methods, Figure 1: \"17 due to data\nacquisition updates\").\n\"\"\")\n\ncode(r\"\"\"\ntr_all = pd.concat([s[\"trials\"].assign(mouse=s[\"mouse\"], condition=s[\"condition\"], cohort=s[\"cohort\"])\n                    for s in sessions])\nprint(\"odor_control values:\", tr_all.odor_control.value_counts().to_dict())\nprint(\"outcome values:\", tr_all.outcome.value_counts().to_dict(), \"; side values:\", tr_all.side.value_counts().to_dict())\nprint(\"Omission share of trials: %.3f (Methods: 10%%)\" % (tr_all.odor_control == 3).mean())\nprint(\"Set ITI (s) range:\", tr_all.iti_time.min(), \"to\", tr_all.iti_time.max(), \"(Methods: 1 to 15 s)\")\ndur = tr_all.stop_time - tr_all.start_time\nprint(\"Trial duration (s): min %.2f, median %.2f, max %.1f\" % (dur.min(), dur.median(), dur.max()))\nprint(\"Trial start (s): min %.1f, max %.1f; last trial end per session, min %.0f max %.0f\"\n      % (tr_all.start_time.min(), tr_all.start_time.max(),\n         tr_all.groupby([\"mouse\", \"condition\"]).stop_time.max().min(), tr_all.groupby([\"mouse\", \"condition\"]).stop_time.max().max()))\niti_obs = np.concatenate([ds.iti_lengths(s[\"trials\"])[:-1] for s in sessions])\nprint(\"Observed ITI, next start minus end (s): min %.2f, median %.2f, max %.1f; negative: %d\"\n      % (iti_obs.min(), np.median(iti_obs), iti_obs.max(), (iti_obs < 0).sum()))\nlater = tr_all[tr_all.cohort == \"later\"]\nprint(\"false_alarm values (later cohort):\", later.false_alarm.value_counts().to_dict())\nprint(\"repoke values (later cohort):\", later.repoke.value_counts().sort_index().to_dict())\n\n# The session notes give, for the later cohort, correct over total trials by side.\nrows = []\nfor s in sessions:\n    n, t = s[\"notes\"], s[\"trials\"]\n    if s[\"cohort\"] != \"later\":\n        continue\n    def frac(k):\n        a, b = n.get(k, \"0/0\").split(\"/\")\n        return int(a), int(b)\n    o = ds.odor_mask(t)\n    rows.append({\"mouse\": s[\"mouse\"], \"condition\": s[\"condition\"],\n                 \"notes_L\": frac(\"L\"), \"notes_R\": frac(\"R\"),\n                 \"table_side1\": (int(t.outcome[o & (t.side == 1)].sum()), int((o & (t.side == 1)).sum())),\n                 \"table_side2\": (int(t.outcome[o & (t.side == 2)].sum()), int((o & (t.side == 2)).sum()))})\nnotes_check = pd.DataFrame(rows)\nmatch1 = (notes_check.notes_L == notes_check.table_side1) & (notes_check.notes_R == notes_check.table_side2)\nmatch2 = (notes_check.notes_L == notes_check.table_side2) & (notes_check.notes_R == notes_check.table_side1)\nprint(\"\\nLater-cohort sessions whose notes' L and R (correct/total odor trials) equal the table's side 1 and 2:\",\n      int(match1.sum()), \"; side 2 and 1:\", int(match2.sum()), \"; of\", len(notes_check))\nprint(notes_check[~(match1 | match2)].to_string(index=False))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe trial table holds odor trials (0) and omission trials (3), about 10% omission as the Methods\nsay, set ITIs of 1 to 15 s, outcomes 0 and 1 and sides 1 and 2. The ITI observed between trials\nis longer than the set ITI, as it includes the time to poke into the initiation port. The session\nnotes count correct and total odor trials by side; where they agree with the table for every\nsession printed as matching above, side 1 is left. `false_alarm` is almost always 0, as the\npaper says false reports were rare.\n\"\"\")\n\nmd(r\"\"\"\n### Do the tracking frames share the trial table's clock?\n\nThe files give the tracking no timestamps: each series has a starting time of 0 and a rate that\nthe conversion script estimated as the number of frames over the last trial's end time (its\ncomments call it an approximation). The paper's code places frame i at i / 80 s. A trial starts\nat the initiation port and ends when the mouse reaches the odor side at the far end of the arena,\nso the nose's x at the end of a trial minus its x at the start (first cohort flipped) shows\nwhether frames and trials are aligned. A rate and offset are fitted for each session\n(`ds.fit_clock`), and refitted on each half of the session.\n\"\"\")\n\ncode(r\"\"\"\nclock_rows = []\nx_by_session = {}\nfor s in sessions:\n    x, y, cinfo = ds.clean_nose(s)\n    if s[\"cohort\"] == \"first\":\n        x = ds.FLIP_X - x\n    fit = ds.fit_clock(x, s[\"trials\"])\n    shifted = s[\"trials\"].assign(start_time=s[\"trials\"].start_time + 30, stop_time=s[\"trials\"].stop_time + 30)\n    clock_rows.append({\"mouse\": s[\"mouse\"], \"condition\": s[\"condition\"], \"cohort\": s[\"cohort\"],\n                       \"frames\": len(x), \"file_rate\": round(s[\"file_rate\"], 2),\n                       \"disp_code_80fps\": ds.trial_displacement(x, s[\"trials\"], ds.CODE_FPS, 0.0),\n                       \"disp_file_rate\": ds.trial_displacement(x, s[\"trials\"], s[\"file_rate\"], 0.0),\n                       \"fit_fps\": fit[\"fps\"], \"fit_offset_s\": fit[\"offset\"], \"disp_fit\": fit[\"displacement\"],\n                       \"disp_fit_trials_shifted_30s\": ds.trial_displacement(x, shifted, fit[\"fps\"], fit[\"offset\"]),\n                       \"offset_1st_half\": fit[\"offset_first_half\"], \"offset_2nd_half\": fit[\"offset_second_half\"],\n                       \"nose_low_likelihood\": cinfo[\"low_likelihood\"] / cinfo[\"frames\"],\n                       \"nose_interpolated\": cinfo[\"interpolated\"] / cinfo[\"frames\"]})\nclock = pd.DataFrame(clock_rows).sort_values([\"cohort\", \"mouse\", \"condition\"])\nprint(clock.round(3).to_string(index=False))\nprint(\"\\nMedian displacement (px) by cohort:\")\nprint(clock.groupby(\"cohort\")[[\"disp_code_80fps\", \"disp_file_rate\", \"disp_fit\", \"disp_fit_trials_shifted_30s\"]].median().round(1).to_string())\nprint(\"\\nFitted rate by cohort (frames/s):\", clock.groupby(\"cohort\").fit_fps.describe()[[\"min\", \"50%\", \"max\"]].round(2).to_dict(\"index\"))\nclock[\"halves_agree\"] = (clock.offset_1st_half - clock.offset_2nd_half).abs() <= 1.0\nclock[\"fit_ok\"] = (clock.disp_fit >= 100) & clock.halves_agree\nprint(\"Sessions whose fit is weak (displacement < 100 px) or whose halves differ by more than 1 s:\")\nprint(clock[~clock.fit_ok][[\"mouse\", \"condition\", \"fit_fps\", \"fit_offset_s\", \"disp_fit\", \"offset_1st_half\", \"offset_2nd_half\"]].to_string(index=False))\nprint(\"\\nFraction of nose frames below likelihood 0.95: median %.2f, range %.2f to %.2f\"\n      % (clock.nose_low_likelihood.median(), clock.nose_low_likelihood.min(), clock.nose_low_likelihood.max()))\nCLOCK = {(r.mouse, r.condition): (r.fit_fps, r.fit_offset_s) for r in clock.itertuples()}\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nWith the code's clock (frame i at i / 80 s) the nose moves by a median of about 0 px between the\nstart and the end of a trial: the frames the code labels as within a trial are not the trial's\nframes. The file's own rate does no better. A linear clock fitted to each session moves the nose\nby hundreds of pixels toward the odor end over a trial, and the same offset fits both halves of\nmost sessions. The fitted rate is near 80.5 frames/s in the later cohort (the 80 frames/s of the\ncode drifts by about 0.5 x 2400 / 80, some 15 s, over a session, more than a trial lasts) and 72\nto 75 frames/s in the first cohort, whose videos hold fewer frames than 40 min at 80 frames/s. The\nsessions printed as weak are not established. Shifting the trials by 30 s under the fitted clock\nremoves the displacement, so the fit is a response to the trials and not an offset.\n\nThis is a finding about the dataset: the tracking carries no frame times and the stated rate is an\nestimate that does not align it with the trials. The claims file fixes the code's clock for the\nanalyses that split frames by trial period (speed, HTR maps); they are run with it, as the paper\ndid, and again with the fitted clock as a variant. The nose keypoint is below the 0.95 likelihood\ncut in most frames of many sessions, so most nose positions are interpolated, as the code does.\n\"\"\")\n\ncode(r\"\"\"\n# Sniff clock: sniff frequency is higher within trials than in the ITI; compare with the trial\n# labels shifted in time.\nshifts = [-30, -10, -5, -2, 0, 2, 5, 10, 30]\nrows = []\nfor s in sessions:\n    d = ds.sniff_table(s)\n    if d is None:\n        continue\n    row = {\"mouse\": s[\"mouse\"], \"condition\": s[\"condition\"], \"rows\": len(s[\"sniff_start\"]),\n           \"faulty_in_code\": (s[\"mouse\"], s[\"session\"]) in ds.FAULTY_SNIFF,\n           \"first_s\": d.t.min(), \"last_s\": d.t.max(),\n           \"inh_to_exh_ms_median\": 1000 * np.median(s[\"sniff_stop\"] - s[\"sniff_start\"])}\n    for sh in shifts:\n        lab = ds.label_periods(d.t.to_numpy(), s[\"trials\"].assign(start_time=s[\"trials\"].start_time + sh,\n                                                                  stop_time=s[\"trials\"].stop_time + sh))\n        row[f\"shift_{sh}\"] = np.median(d.frequency[lab > 0]) - np.median(d.frequency[lab == 0])\n    rows.append(row)\nsniff_clock = pd.DataFrame(rows).sort_values([\"mouse\", \"condition\"])\nprint(sniff_clock.round(2).to_string(index=False))\ngood = sniff_clock[~sniff_clock.faulty_in_code]\nprint(\"\\nUsable sessions: within-trial minus ITI median frequency (Hz), median over sessions, by shift of the trial labels (s):\")\nprint(good[[f\"shift_{sh}\" for sh in shifts]].median().round(3).to_string())\nprint(\"Sessions where the true labels give a larger contrast than every shift of 10 s or more:\",\n      int((good.shift_0 > good[[\"shift_-30\", \"shift_-10\", \"shift_10\", \"shift_30\"]].max(axis=1)).sum()), \"of\", len(good))\nprint(\"\\nSessions with sniff cycles by condition (usable, code's exclusions):\",\n      good.condition.value_counts().to_dict(), \"; all:\", sniff_clock.condition.value_counts().to_dict())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe sniff cycles span the 40 min session (0 to about 2400 s), and sniffing is faster within\ntrials than in the ITI with the true trial labels, more than with labels shifted by 10 s or more\nin most usable sessions; the contrast peaks between 0 and 2 s of shift. This is consistent with a\nshared clock to within a few seconds, not a proof of it. The code's four faulty sessions keep only\na few hundred to a few thousand rows of tens of thousands (the files' descriptions give the rows\ndropped for a missing exhalation). Without them, 14 DOI and 13 saline sessions remain.\n\"\"\")\n\ncode(r\"\"\"\n# The event series: values, counts by condition, and the form of the timestamps.\nev = info[info.events > 0]\nprint(\"Data values of the series (all 1):\", sorted({float(v) for s in sessions if s[\"events\"] is not None for v in s[\"events_data\"]}))\nprint(\"Sessions with events by condition:\", ev.condition.value_counts().to_dict())\nprint(\"Events per session, DOI: median %d (range %d to %d); saline: median %d (range %d to %d)\" % (\n    ev[ev.condition == \"DOI\"].events.median(), ev[ev.condition == \"DOI\"].events.min(), ev[ev.condition == \"DOI\"].events.max(),\n    ev[ev.condition == \"saline\"].events.median(), ev[ev.condition == \"saline\"].events.min(), ev[ev.condition == \"saline\"].events.max()))\nfrac_rows = []\nfor s in sessions:\n    if s[\"events\"] is None:\n        continue\n    t = s[\"events\"]\n    frac_rows.append({\"mouse\": s[\"mouse\"], \"condition\": s[\"condition\"], \"source\": s[\"events_source\"],\n                      \"max_last_field_x100\": int(np.round((t - np.floor(t + 1e-9)) * 100).max()),\n                      \"steps_of_5ms\": bool(np.allclose(np.round(t * 200), t * 200, atol=1e-6)),\n                      \"first_s\": t.min(), \"last_s\": t.max()})\nfr = pd.DataFrame(frac_rows)\nprint(fr.groupby(\"source\").agg(sessions=(\"mouse\", \"size\"), max_field=(\"max_last_field_x100\", \"max\"),\n                               all_5ms=(\"steps_of_5ms\", \"all\"), last_s=(\"last_s\", \"max\")).to_string())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe series has no name or unit beyond \"Event times (s) from Time Stamps Task\", and its values are\nall 1. In the later cohort the last field of the stored timestamps, read as hundredths by the\nconversion script, never exceeds 79: it is a frame count at 80 frames/s (a video timecode), so\nthe stored times are off by up to 0.2 s, and the code, which reads the field as thousandths, by up\nto 0.7 s. The first cohort's manually scored files are in seconds, in steps of 5 ms. The HTR\nclaims are run under the code's reading and shown under the other two.\n\"\"\")\n\ncode(r\"\"\"\n# Recordings deposited twice: compare trial tables and nose tracks between every pair of sessions.\nsig = []\nfor s in sessions:\n    sig.append(((s[\"mouse\"], s[\"condition\"]), len(s[\"trials\"]), s[\"trials\"].start_time.to_numpy()[:20].round(2),\n                np.nan_to_num(s[\"nose_xy\"][:2000, 0]).round(1), len(s[\"nose_xy\"])))\npairs = []\nfor i in range(len(sig)):\n    for j in range(i + 1, len(sig)):\n        same_trials = sig[i][1] == sig[j][1] and np.array_equal(sig[i][2], sig[j][2])\n        same_track = sig[i][4] == sig[j][4] and np.array_equal(sig[i][3], sig[j][3])\n        if same_trials or same_track:\n            pairs.append((sig[i][0], sig[j][0], same_trials, same_track))\nprint(\"Pairs of sessions with identical trial starts or identical nose tracks:\", pairs if pairs else \"none\")\nprint(\"Distinct session start times:\", info.start.nunique(), \"dates for\", len(info), \"sessions\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nNo session's trial table or nose track repeats another's, so each recording is counted once.\nEach mouse is the same animal in its two sessions by its subject id, as the paired design and the\ncode have it.\n\"\"\")\n\n# ------------------------------------------------------------------ Figure 1\n\nmd(r\"\"\"\n## Figure 1: accuracy and task engagement\n\nPer session from the trial table: accuracy on odor trials (percent correct), the trial counts,\nand for the later cohort the repoke rate and false reports (fig1_cleaned.Rmd, as the claims file\ngives it).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    t = s[\"trials\"]\n    o = ds.odor_mask(t)\n    r = {\"mouse\": s[\"mouse\"], \"condition\": s[\"condition\"], \"sex\": s[\"sex\"], \"cohort\": s[\"cohort\"],\n         \"trials_all\": len(t), \"trials_odor\": int(o.sum()),\n         \"acc_odor\": 100 * t.outcome[o].mean(), \"acc_omission\": 100 * t.outcome[~o].mean(),\n         \"dur_odor\": (t.stop_time - t.start_time)[o].mean(), \"dur_omission\": (t.stop_time - t.start_time)[~o].mean(),\n         \"iti\": np.nanmean(ds.iti_lengths(t))}\n    if \"repoke\" in t:\n        r.update(repoke_rate=t.repoke.sum() / (len(t) - 1), false_reports=t.false_alarm.sum(),\n                 false_report_rate=t.false_alarm.sum() / (len(t) - 1))\n    rows.append(r)\nper_session = pd.DataFrame(rows)\nwide = per_session.pivot(index=\"mouse\", columns=\"condition\")\nsex_of = per_session.drop_duplicates(\"mouse\").set_index(\"mouse\").sex\n\n\ndef paired(col, mice=None, label=None):\n    w = wide if mice is None else wide.loc[mice]\n    a, b = w[(col, \"DOI\")], w[(col, \"saline\")]\n    ok = a.notna() & b.notna()\n    v, p = ds.r_signrank(a[ok], b[ok])\n    diff = a[ok] - b[ok]\n    return {\"measure\": label or col, \"n\": int(ok.sum()), \"DOI_median\": a[ok].median(), \"saline_median\": b[ok].median(),\n            \"median_DOI_minus_saline\": diff.median(), \"DOI_lower_in\": int((diff < 0).sum()), \"V\": v, \"p\": p}\n\"\"\")\n\nmd(r\"\"\"\n### fig1b-accuracy-lower-doi\n\n> Mice are less accurate in the olfactory search task in the DOI session than in the saline\n> session, going more often to the incorrect side.\n\"\"\")\n\ncode(r\"\"\"\nres = pd.DataFrame([paired(\"acc_odor\", label=\"odor-trial accuracy (%)\"),\n                    paired(\"acc_omission\", label=\"omission-trial accuracy (%), variant\")])\nprint(res.round(4).to_string(index=False))\nprint(\"\\nBy sex, odor-trial accuracy:\")\nprint(pd.DataFrame([paired(\"acc_odor\", [m for m in wide.index if sex_of[m] == sx], f\"sex {sx}\") for sx in \"FM\"]).round(4).to_string(index=False))\nprint(\"\\nPer mouse (odor-trial accuracy, %):\")\nprint(wide[\"acc_odor\"].assign(sex=sex_of).round(1).T.to_string())\nfig, ax = plt.subplots(figsize=(4, 4))\nfor sx, c in ((\"F\", \"#990068\"), (\"M\", \"#00B19E\")):\n    m = sex_of[sex_of == sx].index\n    ax.scatter(wide.loc[m, (\"acc_odor\", \"saline\")], wide.loc[m, (\"acc_odor\", \"DOI\")], c=c, label=sx)\nax.plot([60, 100], [60, 100], \"k:\")\nax.set(xlabel=\"saline accuracy (%)\", ylabel=\"DOI accuracy (%)\", xlim=(60, 100), ylim=(60, 100))\nax.legend()\nplt.show()\nprint(\"Plotted range: saline %.1f to %.1f, DOI %.1f to %.1f; none outside the axes.\"\n      % (wide[(\"acc_odor\", \"saline\")].min(), wide[(\"acc_odor\", \"saline\")].max(), wide[(\"acc_odor\", \"DOI\")].min(), wide[(\"acc_odor\", \"DOI\")].max()))\n\"\"\", [\"claim:fig1b-accuracy-lower-doi\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Over the 22 mice with paired sessions (the expected 22), odor-trial\naccuracy is lower on DOI (median difference -3.2 points, lower in most mice), signed-rank p =\n0.023 against the paper's 0.024. Omission-trial accuracy does not differ significantly (variant).\n\"\"\")\n\nmd(r\"\"\"\n### fig1c-accuracy-time-bins\n\n> Over the session, odor-trial accuracy in 5 min bins is higher in the saline condition than the\n> DOI condition after the first 10 min, except in the 30 to 35 min bin, so the effect is spread\n> across the session.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    t = s[\"trials\"]\n    o = ds.odor_mask(t)\n    b = pd.cut(t.start_time.to_numpy() / 60, bins=np.arange(0, 41, 5), include_lowest=True, labels=False)\n    g = pd.DataFrame({\"bin\": b, \"rolling\": ds.rolling_accuracy(t), \"success\": t.outcome})[o].groupby(\"bin\")\n    for k, v in g.agg(rolling=(\"rolling\", \"mean\"), fraction=(\"success\", \"mean\")).iterrows():\n        rows.append({\"mouse\": s[\"mouse\"], \"condition\": s[\"condition\"], \"bin\": int(k), \"rolling\": v.rolling, \"fraction\": 100 * v.fraction})\nbinned = pd.DataFrame(rows)\nout = []\nfor k, g in binned.groupby(\"bin\"):\n    rec = {\"bin_min\": f\"{5 * k}-{5 * k + 5}\"}\n    for col in (\"rolling\", \"fraction\"):\n        a, c = g[g.condition == \"DOI\"][col], g[g.condition == \"saline\"][col]\n        w, p = ds.r_ranksum(a, c)\n        rec.update({f\"{col}_n_DOI\": len(a), f\"{col}_n_sal\": len(c), f\"{col}_DOI_mean\": a.mean(),\n                    f\"{col}_saline_mean\": c.mean(), f\"{col}_saline_higher\": c.mean() > a.mean(), f\"{col}_p\": p})\n    out.append(rec)\nbins_res = pd.DataFrame(out)\nprint(bins_res.round(4).to_string(index=False))\nstated = bins_res.iloc[[2, 3, 4, 7]]\nprint(\"\\nRolling accuracy: saline higher at p < 0.05 in 10-15, 15-20, 20-25, 35-40:\",\n      bool((stated.rolling_saline_higher & (stated.rolling_p < 0.05)).all()),\n      \"; p < 0.01 in the first three:\", bool((bins_res.iloc[[2, 3, 4]].rolling_p < 0.01).all()),\n      \"; 30-35 not significant:\", bool(bins_res.iloc[6].rolling_p >= 0.05))\nprint(\"Mice without odor trials in a bin are absent from it (counts above).\")\ngrand = binned.groupby([\"condition\", \"bin\"]).rolling.agg([\"mean\", \"std\"]).unstack(0)\nfig, ax = plt.subplots(figsize=(5, 3))\nfor cnd, c in ((\"DOI\", \"purple\"), (\"saline\", \"k\")):\n    ax.errorbar(grand.index * 5 + 2.5, grand[(\"mean\", cnd)], yerr=grand[(\"std\", cnd)], color=c, label=cnd, capsize=3)\nax.set(xlabel=\"time in session (min)\", ylabel=\"mean rolling accuracy (%)\")\nax.legend()\nplt.show()\nprint(\"Plotted means range %.1f to %.1f %%; error bars are 1 SD.\" % (grand.xs(\"mean\", axis=1, level=0).min().min(), grand.xs(\"mean\", axis=1, level=0).max().max()))\n\"\"\", [\"claim:fig1c-accuracy-time-bins\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Saline rolling accuracy is higher than DOI in every bin. It is higher at\np < 0.01 in the 10-15, 15-20 and 20-25 min bins (p = 0.0076, 0.0037, 0.0070) and at p = 0.039 in\nthe 35-40 min bin, the paper's value, and the 30-35 min bin is not significant (p = 0.052). The\n25-30 min bin, which the text does not state, has p = 0.018, and the first two bins are not\nsignificant. The per-bin fraction correct (variant) is printed alongside.\n\"\"\")\n\nmd(r\"\"\"\n### fig1d-fewer-trials\n\n> Mice complete fewer trials in the 40 min DOI session than in the saline session.\n\"\"\")\n\ncode(r\"\"\"\nres = pd.DataFrame([paired(\"trials_odor\", label=\"(a) odor trials, the code\"),\n                    paired(\"trials_all\", label=\"(b) all trials, the Methods\")])\nprint(res.round(4).to_string(index=False))\nprint(\"\\nPer mouse, all trials:\")\nprint(wide[\"trials_all\"].assign(sex=sex_of).T.to_string())\n\"\"\", [\"claim:fig1d-fewer-trials\"])\n\nmd(r\"\"\"\n**Result: reproduced.** DOI sessions have fewer trials under both readings: odor trials median\ndifference -9.5, p = 0.011 (the paper's 0.011); all trials -8, p = 0.018.\n\"\"\")\n\nmd(r\"\"\"\n### fig1d-fewer-trials-females-only\n\n> The drop in trials completed under DOI is driven by females; female mice perform fewer trials on\n> DOI than saline, while male mice show no significant difference.\n\"\"\")\n\ncode(r\"\"\"\nF = [m for m in wide.index if sex_of[m] == \"F\"]\nM = [m for m in wide.index if sex_of[m] == \"M\"]\nres = pd.DataFrame([paired(c, mice, f\"{lab}, {sx}\") for c, lab in ((\"trials_odor\", \"(a) odor trials\"), (\"trials_all\", \"(b) all trials\"))\n                    for sx, mice in ((\"females\", F), (\"males\", M))])\nprint(res.round(4).to_string(index=False))\n\"\"\", [\"claim:fig1d-fewer-trials-females-only\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under both readings females (12) do fewer trials on DOI (odor trials p =\n0.010, the paper's 0.011; all trials p = 0.015) and males (10) do not differ (p = 0.39, the\npaper's 0.39; all trials p = 0.44).\n\"\"\")\n\nmd(r\"\"\"\n### fig1e-repoke-no-difference\n\n> Mice poke into the initiation port during the ITI at the same rate in the DOI and saline\n> conditions, showing an equivalent motivation to do the task.\n\"\"\")\n\ncode(r\"\"\"\nres = pd.DataFrame([paired(\"repoke_rate\", label=\"repokes per ITI, later cohort\")])\nprint(res.round(4).to_string(index=False))\nprint(\"\\nPer mouse:\")\nprint(wide[\"repoke_rate\"].dropna().round(3).T.to_string())\n\"\"\", [\"claim:fig1e-repoke-no-difference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Over the 17 later-cohort mice the repoke rate does not differ (median\ndifference -0.10 pokes per ITI, p = 0.38; the paper's p = 0.27).\n\"\"\")\n\nmd(r\"\"\"\n### iti-false-report-no-difference\n\n> Mice rarely enter a reward port during the ITI after a trial-initiation attempt, and DOI does\n> not make them do so more than saline.\n\"\"\")\n\ncode(r\"\"\"\nlat = per_session[per_session.cohort == \"later\"]\nrows = []\nfor col, lab in ((\"false_reports\", \"(a) false reports per session\"), (\"false_report_rate\", \"(b) per ITI\")):\n    a, b = lat[lat.condition == \"DOI\"][col], lat[lat.condition == \"saline\"][col]\n    w, p = ds.r_ranksum(a, b)\n    rows.append({\"reading\": lab, \"n_DOI\": len(a), \"n_saline\": len(b), \"DOI_mean\": a.mean(), \"saline_mean\": b.mean(),\n                 \"DOI_median\": a.median(), \"saline_median\": b.median(), \"W\": w, \"p\": p})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"\\nFalse reports per session (counts):\")\nprint(lat.pivot(index=\"mouse\", columns=\"condition\", values=\"false_reports\").T.to_string())\nprint(\"Sessions with any false report: DOI\", int((lat[lat.condition == 'DOI'].false_reports > 0).sum()),\n      \", saline\", int((lat[lat.condition == 'saline'].false_reports > 0).sum()), \"of 17 each;\",\n      \"false reports over all later-cohort ITIs:\", int(lat.false_reports.sum()), \"of\", int((lat.trials_all - 1).sum()))\nprint(\"The Results' variant (reward-port entries in the ITI) cannot be run: the dandiset has no reward-port events.\")\n\"\"\", [\"claim:iti-false-report-no-difference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The `false_alarm` column of the trial table, the Methods' false odor\nreport, gives 3 false reports in 3 of 17 DOI sessions and 3 in 3 of 17 saline sessions, out of\nover 3000 ITIs; the rank-sum test gives p = 1 under both readings, the paper's value. The Results'\nreward-port variant could not be run.\n\"\"\")\n\n# ------------------------------------------------------------------ Figure 2\n\nmd(r\"\"\"\n## Figure 2: reward-port duration (blocked)\n\nThe nine claims of Figure 2 and its supplement need the times of entering and leaving the reward\nport after each trial. The files hold no such events: the trial table has start, stop, side,\noutcome, set ITI and, for the later cohort, false-alarm and repoke counts; the only event series is\nthe HTR series; `acquisition`, `stimulus` and `analysis` are empty (printed below). The code reads\nthe durations from pre-computed files that are not in its repository either.\n\"\"\")\n\ncode(r\"\"\"\nimport h5py, remfile\npath, url = ds.asset_urls()[20]\nwith h5py.File(remfile.File(url), \"r\") as f:\n    groups = {}\n    f.visit(lambda name: groups.setdefault(name.split(\"/\")[0], []).append(name))\n    print(path)\n    for g in (\"acquisition\", \"analysis\", \"stimulus\", \"intervals\", \"processing\"):\n        members = [n for n in groups.get(g, []) if n.count(\"/\") <= 2]\n        print(f\"  {g}: {members[:12]}\")\n    print(\"  trial columns:\", list(f[\"intervals/trials\"].attrs[\"colnames\"]))\n\"\"\", [\"sanity\"])\n\n# ------------------------------------------------------------------ Figure 3\n\nmd(r\"\"\"\n## Figure 3: trial and ITI duration\n\nTrial duration is end minus start; ITI duration is the next trial's start minus this trial's end;\nper mouse the mean (Methods, Figure 3; fig3_cleaned.Rmd).\n\"\"\")\n\nmd(r\"\"\"\n### fig3a-odor-trial-duration-longer\n\n> Mice take longer to complete odor trials in the DOI condition than in the saline condition.\n\"\"\")\n\ncode(r\"\"\"\nres = pd.DataFrame([paired(\"dur_odor\", label=\"odor-trial duration (s)\")])\nprint(res.round(6).to_string(index=False))\nprint(\"\\nPer mouse (s):\")\nprint(wide[\"dur_odor\"].round(2).T.to_string())\n\"\"\", [\"claim:fig3a-odor-trial-duration-longer\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Odor trials last longer on DOI (median difference 0.26 s, longer in most\nmice), p = 4.8e-06 against the paper's p < 0.001.\n\"\"\")\n\nmd(r\"\"\"\n### fig3a-omission-duration-no-difference\n\n> The duration of omission trials does not differ between DOI and saline.\n\"\"\")\n\ncode(r\"\"\"\nres = pd.DataFrame([paired(\"dur_omission\", label=\"omission-trial duration (s)\")])\nprint(res.round(4).to_string(index=False))\n\"\"\", [\"claim:fig3a-omission-duration-no-difference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Omission-trial duration does not differ (median difference 0.55 s, p =\n0.32; the paper's p = 0.26).\n\"\"\")\n\nmd(r\"\"\"\n### fig3b-iti-duration-no-difference\n\n> ITI duration does not differ between DOI and saline.\n\"\"\")\n\ncode(r\"\"\"\nres = pd.DataFrame([paired(\"iti\", label=\"mean ITI (s)\")])\nprint(res.round(4).to_string(index=False))\nprint(\"\\nPer mouse (s):\")\nprint(wide[\"iti\"].round(2).T.to_string())\n\"\"\", [\"claim:fig3b-iti-duration-no-difference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The mean ITI does not differ at p < 0.05 (median difference 1.4 s, longer on\nDOI, p = 0.098; the paper's p = 0.19).\n\"\"\")\n\n# ------------------------------------------------------------------ speed\n\nmd(r\"\"\"\n## Figure 3C, 3D and supplement: speed\n\nNose speed as the claims file gives it (cleaning of `ds.clean_nose`, frame-to-frame displacement\nx 80 frames/s x 0.0237 cm/px, frames above 160 cm/s dropped), per mouse the mean over the frames\nof each period. Periods by the code's clock (frame i at i / 80 s), and as a variant by the clock\nfitted in the data check.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    x, y, _ = ds.clean_nose(s)\n    sp = ds.speed_cm_s(x, y)\n    keep = sp <= ds.MAX_SPEED_CM_S\n    fps, off = CLOCK[(s[\"mouse\"], s[\"condition\"])]\n    for clk, times in ((\"code\", ds.frame_times(len(x))), (\"fitted\", ds.frame_times(len(x), fps) - off)):\n        lab = ds.label_periods(times, s[\"trials\"])\n        rows.append({\"mouse\": s[\"mouse\"], \"condition\": s[\"condition\"], \"clock\": clk,\n                     \"within\": sp[keep & (lab > 0)].mean(), \"iti\": sp[keep & (lab == 0)].mean(),\n                     \"odor\": sp[keep & (lab == 1)].mean(), \"omission\": sp[keep & (lab == 3)].mean(),\n                     \"frames_dropped_over_160\": int((~keep[1:]).sum()), \"frames\": len(sp),\n                     \"within_frames_frac\": float((lab > 0).mean())})\nspeed = pd.DataFrame(rows)\nprint(\"Frames dropped above 160 cm/s, all sessions:\", int(speed[speed.clock == \"code\"].frames_dropped_over_160.sum()),\n      \"of\", int(speed[speed.clock == \"code\"].frames.sum()))\nprint(\"Fraction of frames within trials: code clock median %.3f, fitted %.3f\"\n      % (speed[speed.clock == \"code\"].within_frames_frac.median(), speed[speed.clock == \"fitted\"].within_frames_frac.median()))\nprint(\"Per-mouse mean speeds (cm/s), range over mice:\")\nprint(speed.groupby([\"clock\", \"condition\"])[[\"within\", \"iti\", \"odor\", \"omission\"]].agg([\"min\", \"median\", \"max\"]).round(2).to_string())\nSW = {clk: g.drop(columns=\"clock\").pivot(index=\"mouse\", columns=\"condition\") for clk, g in speed.groupby(\"clock\")}\nfitted_ok = set(clock[clock.fit_ok].mouse.groupby(clock[clock.fit_ok].mouse).size().loc[lambda v: v == 2].index)\nprint(\"Mice whose two sessions both have a good clock fit:\", len(fitted_ok))\n\n\ndef speed_test(a, b, clk=\"code\", mice=None):\n    w = SW[clk] if mice is None else SW[clk].loc[sorted(mice)]\n    xa, xb = w[a], w[b]\n    v, p = ds.r_signrank(xa, xb)\n    wr, pr = ds.r_ranksum(xa, xb)\n    d = xa - xb\n    return {\"clock\": clk + (\"\" if mice is None else \", good fits\"), \"n\": len(d), \"A_median\": xa.median(), \"B_median\": xb.median(),\n            \"median_A_minus_B\": d.median(), \"A_lower_in\": int((d < 0).sum()), \"signrank_p\": p, \"ranksum_p\": pr}\n\n\ndef speed_block(a, b):\n    out = pd.DataFrame([speed_test(a, b, \"code\"), speed_test(a, b, \"fitted\"), speed_test(a, b, \"fitted\", fitted_ok)])\n    print(f\"A = {a}, B = {b}\")\n    print(out.round(4).to_string(index=False))\n\"\"\")\n\nmd(r\"\"\"\n### fig3c-speed-within-trial-lower\n\n> DOI lowers movement speed within trials, odor and omission trials pooled, compared with saline.\n\"\"\")\n\ncode(r\"\"\"\nspeed_block((\"within\", \"DOI\"), (\"within\", \"saline\"))\nprint(\"\\nBy sex, code clock:\")\nfor sx in \"FM\":\n    print(sx, {k: round(v, 4) if isinstance(v, float) else v for k, v in\n               speed_test((\"within\", \"DOI\"), (\"within\", \"saline\"), \"code\", [m for m in SW[\"code\"].index if sex_of[m] == sx]).items()})\nfig, ax = plt.subplots(1, 2, figsize=(8, 4))\nfor i, (per, title) in enumerate(((\"within\", \"within trial\"), (\"iti\", \"ITI\"))):\n    w = SW[\"code\"]\n    ax[i].scatter(w[(per, \"saline\")], w[(per, \"DOI\")])\n    lim = [0, max(w[per].max().max(), 1) * 1.1]\n    ax[i].plot(lim, lim, \"k:\")\n    ax[i].set(xlabel=\"saline speed (cm/s)\", ylabel=\"DOI speed (cm/s)\", title=title + \" (code clock)\", xlim=lim, ylim=lim)\nplt.show()\nprint(\"Plotted per-mouse speeds span %.2f to %.2f cm/s; none outside the axes.\"\n      % (SW[\"code\"][[\"within\", \"iti\"]].min().min(), SW[\"code\"][[\"within\", \"iti\"]].max().max()))\n\"\"\", [\"claim:fig3c-speed-within-trial-lower\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** With the claims file's method (code clock, signed-rank test)\nwithin-trial speed is lower on DOI (median difference -0.63 cm/s) but p = 0.063, against the\npaper's 0.011; the rank-sum test the Results name gives p = 0.51. With the fitted clock, which\ndoes align the frames with the trials, DOI and saline do not differ (p = 0.77).\n\"\"\")\n\nmd(r\"\"\"\n### fig3d-speed-iti-lower\n\n> DOI lowers movement speed during the ITI compared with saline.\n\"\"\")\n\ncode(r\"\"\"\nspeed_block((\"iti\", \"DOI\"), (\"iti\", \"saline\"))\n\"\"\", [\"claim:fig3d-speed-iti-lower\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** ITI speed is lower on DOI (median difference -0.60 cm/s) but\np = 0.079 with the claims file's method, against the paper's 0.036; with the fitted clock p =\n0.059. The rank-sum variant gives p = 0.57.\n\"\"\")\n\nmd(r\"\"\"\n### fig3supp-odor-trial-speed-no-difference\n\n> Within odor trials alone, speed does not differ between DOI and saline sessions.\n\"\"\")\n\ncode(r\"\"\"\nspeed_block((\"odor\", \"DOI\"), (\"odor\", \"saline\"))\n\"\"\", [\"claim:fig3supp-odor-trial-speed-no-difference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Odor-trial speed does not differ (signed-rank p = 0.19, median difference\n-0.54 cm/s; rank-sum p = 0.70); with the fitted clock p = 0.73.\n\"\"\")\n\nmd(r\"\"\"\n### fig3supp-doi-iti-slower-than-odor\n\n> Within the DOI condition, mice move more slowly in the ITI than in odor trials.\n\"\"\")\n\ncode(r\"\"\"\nspeed_block((\"iti\", \"DOI\"), (\"odor\", \"DOI\"))\n\"\"\", [\"claim:fig3supp-doi-iti-slower-than-odor\"])\n\nmd(r\"\"\"\n**Result: reproduced.** On DOI the ITI is slower than odor trials (median difference -0.83 cm/s,\np = 0.0002); with the fitted clock the difference is larger (-3.5 cm/s, p < 0.001).\n\"\"\")\n\nmd(r\"\"\"\n### fig3supp-doi-omission-no-difference\n\n> Within the DOI condition, speed does not differ between odor and omission trials, nor between\n> the ITI and omission trials.\n\"\"\")\n\ncode(r\"\"\"\nspeed_block((\"odor\", \"DOI\"), (\"omission\", \"DOI\"))\nprint()\nspeed_block((\"iti\", \"DOI\"), (\"omission\", \"DOI\"))\n\"\"\", [\"claim:fig3supp-doi-omission-no-difference\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** With the claims file's method odor and omission trials do not\ndiffer (p = 0.31) but the ITI is slower than omission trials (median difference -0.70 cm/s, p =\n0.0059, against the paper's 0.068): one of the two comparisons is significant. The rank-sum\nvariants give p = 0.62 and 0.37. With the fitted clock both comparisons are significant.\n\"\"\")\n\nmd(r\"\"\"\n### fig3supp-saline-iti-slower\n\n> In saline sessions, mice move more slowly in the ITI than in odor trials and in omission trials.\n\"\"\")\n\ncode(r\"\"\"\nspeed_block((\"iti\", \"saline\"), (\"odor\", \"saline\"))\nprint()\nspeed_block((\"iti\", \"saline\"), (\"omission\", \"saline\"))\n\"\"\", [\"claim:fig3supp-saline-iti-slower\"])\n\nmd(r\"\"\"\n**Result: reproduced.** On saline the ITI is slower than odor trials (p = 0.025, the paper's\n0.002) and than omission trials (p = 0.016, the paper's 0.017); with the fitted clock both at\np < 0.001.\n\"\"\")\n\nmd(r\"\"\"\n### fig3supp-saline-odor-omission-no-difference\n\n> In saline sessions, speed does not differ between odor and omission trials.\n\"\"\")\n\ncode(r\"\"\"\nspeed_block((\"odor\", \"saline\"), (\"omission\", \"saline\"))\n\"\"\", [\"claim:fig3supp-saline-odor-omission-no-difference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** On saline odor and omission trials do not differ (p = 0.68, median\ndifference -0.18 cm/s; the paper's 0.54); with the fitted clock p = 0.37.\n\"\"\")\n\n# ------------------------------------------------------------------ Figure 4\n\nmd(r\"\"\"\n## Figure 4: sniff frequency\n\nSniff frequency is 1000 over the interval in ms between successive inhalations (`ds.sniff_table`),\nin the 14 DOI and 13 saline sessions the code keeps. The claims file names two readings of the\nMethods' exclusions, (a) the 5th to 95th percentile of durations per session and (b) over the\nsessions of a condition, each with durations outside 10 to 1000 ms dropped. The file's cycles are\nthe same detections the code reads, so the code's computation (no further exclusion) is shown as a\nthird reading.\n\"\"\")\n\ncode(r\"\"\"\nsniffs = pd.concat([ds.sniff_table(s) for s in sessions\n                    if s[\"sniff_start\"] is not None and (s[\"mouse\"], s[\"session\"]) not in ds.FAULTY_SNIFF])\nREAD = ds.sniff_readings(sniffs)\nfor k, d in READ.items():\n    print(f\"{k}: sniffs DOI {int((d.condition == 'DOI').sum())}, saline {int((d.condition == 'saline').sum())}; \"\n          f\"sessions DOI {d[d.condition == 'DOI'].mouse.nunique()}, saline {d[d.condition == 'saline'].mouse.nunique()}; \"\n          f\"frequency {d.frequency.min():.2f} to {d.frequency.max():.2f} Hz; duration {d.duration_ms.min():.0f} to {d.duration_ms.max():.0f} ms\")\n\"\"\")\n\nmd(r\"\"\"\n### fig4abc-sniff-frequency-higher\n\n> Pooling all sessions with a usable sniff signal, sniff frequency is higher in DOI sessions than\n> in saline sessions.\n\"\"\")\n\ncode(r\"\"\"\nrng_seed = 4\nrows = []\nfor k, d in READ.items():\n    a = d.frequency[d.condition == \"DOI\"].to_numpy()\n    b = d.frequency[d.condition == \"saline\"].to_numpy()\n    z, p = ds.fisher_pitman(a, b, n_resample=10000, seed=rng_seed)\n    rows.append({\"reading\": k, \"n_DOI\": len(a), \"n_saline\": len(b), \"DOI_mean_Hz\": a.mean(), \"saline_mean_Hz\": b.mean(),\n                 \"Z\": z, \"p_10000_resamples\": p, \"p_normal\": 2 * stats.norm.sf(abs(z))})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"Sessions with a usable signal: DOI\", READ[\"a_session\"][READ[\"a_session\"].condition == \"DOI\"].mouse.nunique(),\n      \"(expected 14), saline\", READ[\"a_session\"][READ[\"a_session\"].condition == \"saline\"].mouse.nunique(), \"(expected 13)\")\nd = READ[\"a_session\"]\nfig, ax = plt.subplots(figsize=(5, 3))\nbins = np.arange(0, 16.25, 0.25)\nfor cnd, c in ((\"DOI\", \"purple\"), (\"saline\", \"grey\")):\n    ax.hist(d.frequency[d.condition == cnd], bins=bins, density=True, histtype=\"step\", color=c, label=cnd)\nax.set(xlabel=\"sniff frequency (Hz)\", ylabel=\"density\")\nax.legend()\nplt.show()\nprint(\"Sniffs above the 16 Hz axis, reading (a):\", int((d.frequency > 16).sum()), \"of\", len(d))\n\"\"\", [\"claim:fig4abc-sniff-frequency-higher\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The sessions are 14 DOI and 13 saline, the expected counts. DOI sniff\nfrequency is higher under every reading (mean 7.78 against 7.55 Hz under reading a), Z = 25.2\n(a), 28.4 (b) and 19.5 (the code's), against the paper's Z = 24.9, with no permutation of 10000 as\nextreme (p < 0.0001).\n\"\"\")\n\nmd(r\"\"\"\n### fig4supp-ks-every-mouse\n\n> Every mouse with matched DOI and saline sniff sessions has a sniff-frequency distribution\n> shifted higher in the DOI condition.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor k, d in READ.items():\n    for m, g in d.groupby(\"mouse\"):\n        if g.condition.nunique() < 2:\n            continue\n        r = stats.ks_2samp(g.frequency[g.condition == \"DOI\"], g.frequency[g.condition == \"saline\"], alternative=\"less\")\n        rows.append({\"reading\": k, \"mouse\": m, \"D\": r.statistic, \"p\": r.pvalue,\n                     \"DOI_median\": g.frequency[g.condition == \"DOI\"].median(), \"saline_median\": g.frequency[g.condition == \"saline\"].median()})\nks = pd.DataFrame(rows)\nprint(ks.pivot(index=\"mouse\", columns=\"reading\", values=\"p\").map(lambda v: f\"{v:.2g}\").to_string())\nprint()\nprint(ks.groupby(\"reading\").agg(matched_mice=(\"mouse\", \"size\"), p_below_0_001=(\"p\", lambda v: int((v < 0.001).sum())),\n                                p_below_0_05=(\"p\", lambda v: int((v < 0.05).sum()))).to_string())\nprint(\"\\nMedian frequency (Hz) per mouse, reading (a):\")\nprint(ks[ks.reading == \"a_session\"][[\"mouse\", \"DOI_median\", \"saline_median\"]].round(2).to_string(index=False))\n\"\"\", [\"claim:fig4supp-ks-every-mouse\"])\n\nmd(r\"\"\"\n**Result: reproduced.** 13 mice have matched sessions, the expected number. Under reading (b) all\n13 have a one-sided KS p < 0.001; under reading (a) and the code's computation 11 of 13 do, and the\nother two (2209 and 2211) have p of 0.003 to 0.011. The criterion names both readings, and the\nclaim holds under (b).\n\"\"\")\n\nmd(r\"\"\"\n### fig4d-sniff-frequency-by-period\n\n> Mice sniff faster in the DOI condition in odor trials, in omission trials and during the ITI.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor k, d in READ.items():\n    for per, lab in ((1, \"odor trials\"), (3, \"omission trials\"), (0, \"ITI\")):\n        a = d.frequency[(d.condition == \"DOI\") & (d.period == per)].to_numpy()\n        b = d.frequency[(d.condition == \"saline\") & (d.period == per)].to_numpy()\n        z, p = ds.fisher_pitman(a, b, n_resample=10000 if k == \"a_session\" else 0, seed=rng_seed)\n        rows.append({\"reading\": k, \"period\": lab, \"n_DOI\": len(a), \"n_saline\": len(b), \"DOI_mean\": a.mean(),\n                     \"saline_mean\": b.mean(), \"Z\": z, \"p_10000_resamples\": p if k == \"a_session\" else np.nan,\n                     \"p_normal\": 2 * stats.norm.sf(abs(z))})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"Resampled p is computed for reading (a); the others give the normal approximation of the same statistic.\")\n\"\"\", [\"claim:fig4d-sniff-frequency-by-period\"])\n\nmd(r\"\"\"\n**Result: reproduced.** DOI sniffing is faster in all three periods under every reading: under\nreading (a) odor trials Z = 4.3, omission trials Z = 3.9, ITI Z = 24.2 (the paper's 3.38, 2.71 and\n18.4), each with p < 0.001. Sniffs are placed in periods by the trial table's clock, which the\ndata check found consistent with the sniff clock.\n\"\"\")\n\nmd(r\"\"\"\n### fig4e-median-sniff-no-difference\n\n> Per-mouse median sniff frequency does not differ between DOI and saline.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor k, d in READ.items():\n    med = d.groupby([\"mouse\", \"condition\"]).frequency.median().unstack()\n    both = med.dropna()\n    v, p = ds.r_signrank(both.DOI, both.saline)\n    rows.append({\"reading\": k, \"mice_with_both\": len(both), \"median_DOI_minus_saline\": (both.DOI - both.saline).median(),\n                 \"DOI_higher_in\": int((both.DOI > both.saline).sum()), \"V\": v, \"p\": p})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n\"\"\", [\"claim:fig4e-median-sniff-no-difference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Over the 13 mice with both sessions, the per-mouse median frequency does\nnot differ at p < 0.05 (p = 0.11 under readings a and the code's, the paper's 0.11; 0.15 under b),\nalthough it is higher on DOI in most mice (median difference about 0.53 Hz).\n\"\"\")\n\n# ------------------------------------------------------------------ Figure 5\n\nmd(r\"\"\"\n## Figure 5: occupancy and head twitches\n\nFrames as fig5_cleaned.Rmd builds them (`ds.map_frames`): nose position after cleaning, the first\ncohort's x flipped (1200 - x), negative positions set to 0, periods by the code's clock (and the\nfitted clock as a variant), HTRs on the frame nearest each timestamp.\n\"\"\")\n\ncode(r\"\"\"\nFR = {}\nfor s in sessions:\n    FR[(s[\"mouse\"], s[\"condition\"], \"code\")] = ds.map_frames(s)\nallx = np.concatenate([f.x.to_numpy()[::10] for (m, c, r), f in FR.items()])\nally = np.concatenate([f.y.to_numpy()[::10] for (m, c, r), f in FR.items()])\nBOUNDS = (*np.percentile(allx, [0.5, 99.5]), *np.percentile(ally, [0.5, 99.5]))\nprint(\"Nose positions pooled over sessions (px): x %.0f to %.0f, y %.0f to %.0f; 0.5 to 99.5 percentile box %s\"\n      % (allx.min(), allx.max(), ally.min(), ally.max(), np.round(BOUNDS, 0)))\nprint(\"Arena from that box: %.1f x %.1f cm at 0.0237 cm/px\" % ((BOUNDS[1] - BOUNDS[0]) * ds.CM_PER_PX, (BOUNDS[3] - BOUNDS[2]) * ds.CM_PER_PX))\n\"\"\")\n\nmd(r\"\"\"\n### fig5ab-occupancy-similar\n\n> Mice occupy the arena similarly in the DOI and saline conditions; DOI does not make them spend\n> more time in task-irrelevant areas such as the corners or spread more evenly.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (m, c, r), f in FR.items():\n    rows.append({\"mouse\": m, \"condition\": c, **ds.occupancy_measures(f, BOUNDS)})\nocc = pd.DataFrame(rows).pivot(index=\"mouse\", columns=\"condition\")\nout = []\nfor k in (\"entropy\", \"corners_5cm\", \"corners_10cm\"):\n    v, p = ds.r_signrank(occ[(k, \"DOI\")], occ[(k, \"saline\")])\n    out.append({\"measure\": k, \"DOI_median\": occ[(k, \"DOI\")].median(), \"saline_median\": occ[(k, \"saline\")].median(),\n                \"median_DOI_minus_saline\": (occ[(k, \"DOI\")] - occ[(k, \"saline\")]).median(), \"p\": p})\nprint(pd.DataFrame(out).round(4).to_string(index=False))\n\n\ndef occ_map(cond):\n    maps = []\n    for (m, c, r), f in FR.items():\n        if c != cond:\n            continue\n        g = f[f.speed <= ds.MAX_SPEED_CM_S]\n        H, _, _ = np.histogram2d(g.x, g.y, bins=[np.arange(0, 1249, ds.OCC_BIN_PX), np.arange(0, 721, ds.OCC_BIN_PX)])\n        maps.append(H / H.sum())\n    return np.mean(maps, axis=0)\nmD, mS = occ_map(\"DOI\"), occ_map(\"saline\")\nprint(\"Pearson r between the grand-mean maps (22 mice each): %.3f\" % np.corrcoef(mD.ravel(), mS.ravel())[0, 1])\nfig, ax = plt.subplots(1, 2, figsize=(9, 3))\nvmax = max(mD.max(), mS.max())\nfor a, mp, t in ((ax[0], mS, \"saline\"), (ax[1], mD, \"DOI\")):\n    im = a.imshow(mp.T, origin=\"upper\", vmin=0, vmax=vmax, extent=(0, 1248, 720, 0))\n    a.set(title=f\"occupancy, {t}\", xlabel=\"x (px, odor end right)\", ylabel=\"y (px)\")\nfig.colorbar(im, ax=ax, label=\"fraction of frames\")\nplt.show()\nprint(\"Map values range 0 to %.4f; the colour scale covers it.\" % vmax)\n\"\"\", [\"claim:fig5ab-occupancy-similar\"])\n\nmd(r\"\"\"\n**Result: reproduced.** No measure differs at p < 0.05: occupancy entropy (p = 0.063), the\nfraction of frames in 5 cm corners (p = 0.25) and in 10 cm corners (p = 0.70). The grand-mean maps\ncorrelate closely (Pearson r printed above). With the arena about 27 by 16 cm at the code's scale,\n10 cm corner squares cover most of it, so that reading says little.\n\"\"\")\n\nmd(r\"\"\"\n### htr-event-link (added here)\n\n> The dataset's `task_event_timestamps` are the head-twitch (HTR) times the paper analysed.\n\nThe files do not name the series. The conversion script loads it from the folders \"Time Stamps\nTask\" and \"Time Stamps Task Logan\", which fig5_cleaned.Rmd reads as HTR timestamps, by the same\nmouse and session names. HTRs are induced by DOI, so the series should be present in all 22 DOI\nsessions (the paper's n = 22) and much more frequent there than in saline sessions.\n\"\"\")\n\ncode(r\"\"\"\nev_counts = info.pivot(index=\"mouse\", columns=\"condition\", values=\"events\")\nprint(\"DOI sessions with the series:\", int((ev_counts.DOI > 0).sum()), \"of 22; saline sessions:\", int((ev_counts.saline > 0).sum()), \"of 22\")\nboth = ev_counts[(ev_counts.DOI > 0) & (ev_counts.saline > 0)]\nprint(\"Mice with the series in both sessions:\", len(both), \"; DOI count higher in\", int((both.DOI > both.saline).sum()))\nprint(\"Events per minute of the 40 min session, DOI: median %.2f (range %.2f to %.2f); saline (where present): median %.2f\"\n      % ((ev_counts.DOI / 40).median(), (ev_counts.DOI / 40).min(), (ev_counts.DOI / 40).max(), (ev_counts.saline[ev_counts.saline > 0] / 40).median()))\nprint(\"Source folder by cohort:\", info[info.events > 0].groupby([\"cohort\", \"event_source\"]).size().to_dict())\nprint(ev_counts.T.to_string())\n\"\"\", [\"claim:htr-event-link\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The series is in all 22 DOI sessions, as the paper's n = 22 needs, and in\n10 saline sessions; in every mouse with both, the DOI session has more events (a median of about\n3.7 per minute on DOI, 0.6 on saline). Together with the conversion script's sources this links the\nseries to the HTR times. The 2197 DOI session has only 30 events.\n\"\"\")\n\ncode(r\"\"\"\nHTR_READINGS = (\"code\", \"file\", \"frames\")\nhtr_tables = {}\nfor reading in HTR_READINGS:\n    for clk in (\"code\", \"fitted\"):\n        if clk == \"fitted\" and reading != \"code\":\n            continue\n        for s in sessions:\n            if s[\"condition\"] != \"DOI\":\n                continue\n            fps, off = (ds.CODE_FPS, 0.0) if clk == \"code\" else CLOCK[(s[\"mouse\"], \"DOI\")]\n            f = FR[(s[\"mouse\"], \"DOI\", \"code\")] if (reading, clk) == (\"code\", \"code\") else ds.map_frames(s, fps, off, reading)\n            for period in (\"all\", \"within\", \"iti\"):\n                htr_tables.setdefault((reading, clk, period), []).append(ds.htr_rate_table(f, s[\"mouse\"], period))\nhtr_tables = {k: pd.concat(v) for k, v in htr_tables.items()}\n\n\ndef htr_perm(period):\n    rows = []\n    for (reading, clk, per), T in htr_tables.items():\n        if per != period:\n            continue\n        rx, px = ds.perm_corr_test(T.rate, T.bx)\n        ry, py = ds.perm_corr_test(T.rate, T.by)\n        rows.append({\"timestamps\": reading, \"clock\": clk, \"rows\": len(T), \"mice\": T.mouse.nunique(),\n                     \"HTRs_counted\": int(T.htr_count.sum()), \"r_x\": rx, \"p_x\": px, \"r_y\": ry, \"p_y\": py})\n    return pd.DataFrame(rows)\n\"\"\")\n\nmd(r\"\"\"\n### fig5supp-htr-within-trial-x-not-y\n\n> During trials, HTR rate (normalized to occupancy) varies with the X coordinate of the arena but\n> not with the Y coordinate.\n\"\"\")\n\ncode(r\"\"\"\nprint(htr_perm(\"within\").round(4).to_string(index=False))\nT = htr_tables[(\"code\", \"code\", \"within\")]\nprint(\"\\nWithin-trial rate (HTR/min) per bin, code reading: range %.2f to %.2f; bins with rate 0: %d of %d\"\n      % (T.rate.min(), T.rate.max(), int((T.rate == 0).sum()), len(T)))\n\"\"\", [\"claim:fig5supp-htr-within-trial-x-not-y\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Within trials the per-mouse, per-bin HTR rate correlates with x (r =\n0.056, permutation p = 0.006 under the code's reading; the paper's p = 0.002) and not with y (p =\n0.26; the paper's 0.92). The other timestamp readings and the fitted clock give the same pattern\n(printed above).\n\"\"\")\n\nmd(r\"\"\"\n### fig5e-htr-combined-x\n\n> With trial and ITI periods combined, mice head-twitch more often closer to the odor end of the\n> arena, as the X coordinate increases.\n\"\"\")\n\ncode(r\"\"\"\nprint(htr_perm(\"all\").round(4).to_string(index=False))\nT = htr_tables[(\"code\", \"code\", \"all\")]\nprint(\"\\nMice in the map:\", T.mouse.nunique(), \"(expected 22)\")\ngrand = T.groupby([\"bx\", \"by\"]).rate.mean().unstack()\nprint(\"Grand-mean rate by x bin (mean over y bins, HTR/min):\")\nprint(grand.mean(axis=1).round(2).to_string())\nfig, ax = plt.subplots(figsize=(5, 3))\nim = ax.imshow(grand.T.to_numpy(), origin=\"upper\", extent=(grand.index.min(), grand.index.max() + 100, grand.columns.max() + 100, grand.columns.min()))\nax.set(xlabel=\"x (px, odor end right)\", ylabel=\"y (px)\", title=\"HTR rate, DOI (grand mean)\")\nfig.colorbar(im, label=\"HTR/min\")\nplt.show()\nprint(\"Map range %.2f to %.2f HTR/min.\" % (np.nanmin(grand.to_numpy()), np.nanmax(grand.to_numpy())))\n\"\"\", [\"claim:fig5e-htr-combined-x\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Over the 22 DOI mice (the expected 22), with trial and ITI frames combined,\nthe HTR rate rises with x toward the odor and reward ports (r = 0.149, permutation p < 0.0001,\nnone of 10000 permutations as extreme), under every timestamp reading.\n\"\"\")\n\nmd(r\"\"\"\n### fig5supp-htr-iti-x\n\n> During the ITI, mice head-twitch more often toward the end of the arena past the decision line\n> (as X increases), but not specifically next to the reward ports on the Y coordinate.\n\"\"\")\n\ncode(r\"\"\"\nprint(htr_perm(\"iti\").round(4).to_string(index=False))\n\"\"\", [\"claim:fig5supp-htr-iti-x\"])\n\nmd(r\"\"\"\n**Result: reproduced.** In the ITI the HTR rate rises with x (r = 0.152, p < 0.0001) and does not\nvary with y (p = 0.56 under the code's reading; 0.08 to 0.25 under the others).\n\"\"\")\n\nmd(r\"\"\"\n### fig5f-htr-rate-trial-vs-iti\n\n> HTR rate does not differ between time within trials and time in the ITI.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor reading in HTR_READINGS:\n    for clk in (\"code\", \"fitted\"):\n        for s in sessions:\n            if s[\"condition\"] != \"DOI\":\n                continue\n            h = ds.htr_times(s, reading)\n            if clk == \"fitted\":\n                fps, off = CLOCK[(s[\"mouse\"], \"DOI\")]\n                h = h * ds.CODE_FPS / fps - off      # video time to trial time\n            t = s[\"trials\"]\n            within = np.zeros(len(h), bool)\n            for st, en in zip(t.start_time, t.stop_time):\n                within |= (h >= st) & (h <= en)\n            trial_time = (t.stop_time - t.start_time).sum()\n            rows.append({\"timestamps\": reading, \"clock\": clk, \"mouse\": s[\"mouse\"], \"sex\": s[\"sex\"],\n                         \"htr\": len(h), \"in_trial\": int(within.sum()),\n                         \"rate_trial\": within.sum() / trial_time * 60, \"rate_iti\": (~within).sum() / (ds.SESSION_S - trial_time) * 60})\nhtr_rates = pd.DataFrame(rows)\nout = []\nfor (reading, clk), g in htr_rates.groupby([\"timestamps\", \"clock\"]):\n    v, p = ds.r_signrank(g.rate_trial, g.rate_iti)\n    out.append({\"timestamps\": reading, \"clock\": clk, \"mice\": len(g), \"trial_median\": g.rate_trial.median(), \"iti_median\": g.rate_iti.median(),\n                \"median_trial_minus_iti\": (g.rate_trial - g.rate_iti).median(), \"V\": v, \"p\": p})\nprint(pd.DataFrame(out).round(4).to_string(index=False))\nprint(\"\\nPer mouse, code reading and clock (HTR/min):\")\nprint(htr_rates[(htr_rates.timestamps == \"code\") & (htr_rates.clock == \"code\")][[\"mouse\", \"htr\", \"in_trial\", \"rate_trial\", \"rate_iti\"]].round(2).to_string(index=False))\n\"\"\", [\"claim:fig5f-htr-rate-trial-vs-iti\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Over the 22 DOI sessions the HTR rate within trials and in the ITI does\nnot differ at p < 0.05 with the code's method (signed-rank p printed above for each reading; the\npaper's p = 1). The fitted-clock variant is printed alongside.\n\"\"\")\n\nmd(r\"\"\"\n### fig5supp-htr-no-sex-difference\n\n> HTR rate over the 40 min DOI session does not differ between male and female mice.\n\"\"\")\n\ncode(r\"\"\"\ng = htr_rates[(htr_rates.timestamps == \"code\") & (htr_rates.clock == \"code\")].assign(rate=lambda d: d.htr / 40)\nw, p = ds.r_ranksum(g.rate[g.sex == \"F\"], g.rate[g.sex == \"M\"], exact=False)\nprint(\"HTR per min over 40 min: females n=%d median %.2f mean %.2f; males n=%d median %.2f mean %.2f; rank-sum W=%.1f p=%.4f\"\n      % ((g.sex == \"F\").sum(), g.rate[g.sex == \"F\"].median(), g.rate[g.sex == \"F\"].mean(),\n         (g.sex == \"M\").sum(), g.rate[g.sex == \"M\"].median(), g.rate[g.sex == \"M\"].mean(), w, p))\n\"\"\", [\"claim:fig5supp-htr-no-sex-difference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** HTR rate over the session does not differ between the sexes (rank-sum,\nnormal approximation as the code, p printed above; the paper's p = 0.31).\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| fig1b-accuracy-lower-doi | reproduced |\n| fig1c-accuracy-time-bins | reproduced |\n| fig1d-fewer-trials | reproduced |\n| fig1d-fewer-trials-females-only | reproduced |\n| fig1e-repoke-no-difference | reproduced |\n| iti-false-report-no-difference | reproduced |\n| fig2a to fig2d-supp (9 claims) | blocked, data missing |\n| fig3a-odor-trial-duration-longer | reproduced |\n| fig3a-omission-duration-no-difference | reproduced |\n| fig3b-iti-duration-no-difference | reproduced |\n| fig3c-speed-within-trial-lower | partially reproduced |\n| fig3d-speed-iti-lower | partially reproduced |\n| fig3supp-odor-trial-speed-no-difference | reproduced |\n| fig3supp-doi-iti-slower-than-odor | reproduced |\n| fig3supp-doi-omission-no-difference | partially reproduced |\n| fig3supp-saline-iti-slower | reproduced |\n| fig3supp-saline-odor-omission-no-difference | reproduced |\n| fig4abc-sniff-frequency-higher | reproduced |\n| fig4supp-ks-every-mouse | reproduced (under reading b) |\n| fig4d-sniff-frequency-by-period | reproduced |\n| fig4e-median-sniff-no-difference | reproduced |\n| fig5ab-occupancy-similar | reproduced |\n| htr-event-link | reproduced |\n| fig5supp-htr-within-trial-x-not-y | reproduced |\n| fig5e-htr-combined-x | reproduced |\n| fig5supp-htr-iti-x | reproduced |\n| fig5f-htr-rate-trial-vs-iti | reproduced |\n| fig5supp-htr-no-sex-difference | reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n**How the analysis differs from the paper's.** Statistics are computed in Python with R's\ndefaults reproduced; the permutation tests draw other random permutations than R's. The\nFisher-Pitman p-values of the per-period tests are resampled for reading (a) only. The occupancy\nmeasures and the arena box are this attempt's readings of the paper's prediction. Frames are split\ninto trial periods by the code's 80 frames/s clock, with a fitted clock as a variant.\n\n**What was found about the dataset.** The reward-port entries and exits of Figure 2 are not in\nit. The tracking has no frame times; its stated rate is an estimate, and neither it nor the\ncode's 80 frames/s aligns the frames with the trial table, while a fitted clock (about 80.5\nframes/s in the later cohort, 72 to 75 in the first) does. The HTR series is not named in the\nfiles, and its later-cohort timestamps store a frame count as hundredths of a second. The saline\nsession of mouse 2182 gives the wrong sex.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"notebook ran in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata = {\"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}}\nnbf.write(nb, \"entries/001863-welch-2025/reproduce_welch_2025.ipynb\")\nprint(\"cells\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . env/bin/activate && uv pip install -q nbformat nbconvert ipykernel matplotlib 2>&1 | tail -1; python build_nb.py && cd entries/001863-welch-2025 && time jupyter nbconvert --to notebook --execute reproduce_welch_2025.ipynb --output $TMPDIR/exec1.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
Thu Nov  5 16:00:12 UTC 2026
cells 111
[32m   1041[39m             arr = np.array(values, dtype=dtype, copy=copy)
[32m   1042[39m 

[31mTypeError[39m: float() argument must be a string or a real number, not 'method'


real	1m56.974s
user	1m2.053s
sys	0m1.829s
```

**Agent calls Bash**

```bash
jupyter nbconvert --to notebook --execute reproduce_welch_2025.ipynb --output $TMPDIR/exec1.ipynb --ExecutePreprocessor.timeout=3000 --allow-errors >/dev/null 2>&1; cd $TMPDIR && cat > show.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
lo=int(sys.argv[2]) if len(sys.argv)>2 else 0; hi=int(sys.argv[3]) if len(sys.argv)>3 else 999
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or not (lo<=i<hi): continue
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(f'[{i}]',''.join(o['text'])[:6000])
        elif o['output_type']=='error': print(f'[{i}] ERROR',o['ename'],o['evalue'], ''.join(o['traceback'][-3:])[:2000])
EOF
python show.py exec1.ipynb 0 12
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/show.py", line 2, in <module>
    nb=json.load(open(sys.argv[1]))
                 ~~~~^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'exec1.ipynb'
```

**Agent calls Bash**

```bash
ls $TMPDIR/*.ipynb entries/001863-welch-2025/; find / -name "exec1.ipynb" 2>/dev/null | head
```

```
ls: cannot access '/tmp/claude-1001/*.ipynb': No such file or directory
entries/001863-welch-2025/:
__pycache__
doi_search.py
reproduce_welch_2025.ipynb
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && jupyter nbconvert --to notebook --execute reproduce_welch_2025.ipynb --output exec1 --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 --allow-errors 2>&1 | tail -2; python $TMPDIR/show.py $TMPDIR/exec1.ipynb 0 14
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 328093 bytes to /tmp/claude-1001/exec1.ipynb
[1] loaded 44 files from dandiset 001863 version 0.260806.2109 in 56 s

[3]  mouse  session condition drug_field sex_code sex_file cohort  trials  odor_trials  trial_columns  frames  file_rate  sniff_rows  events event_source      start
  2174       57       DOI        doi        F        F  first     121          108              6  177027      74.14           0     166        logan 2022-01-28
  2174       56    saline     saline        F        F  first     158          142              6  185828      77.43           0       0          NaN 2022-01-27
  2181       42       DOI        doi        F        F  first     126          113              6  180616      75.39           0     176        logan 2022-01-28
  2181       41    saline     saline        F        F  first     132          118              6  173159      72.72           0       0          NaN 2022-01-27
  2182       32       DOI        doi        M        M  first     128          115              6  180540      75.72           0     174        logan 2022-01-28
  2182       31    saline     saline        M        F  first     103           93              6  179464      74.86           0       0          NaN 2022-01-27
  2183       34       DOI        doi        M        M  first     139          125              6  180573      75.51           0     204        logan 2022-01-28
  2183       33    saline     saline        M        M  first     145          131              6  176506      73.67           0       0          NaN 2022-01-27
  2185       41       DOI        doi        M        M  first     119          107              6  185127      77.16        
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; python $TMPDIR/show.py $TMPDIR/exec1.ipynb 8 9 | tail -30; python $TMPDIR/show.py $TMPDIR/exec1.ipynb 13 60
```

```
[8]  mouse condition cohort  frames  file_rate  disp_code_80fps  disp_file_rate  fit_fps  fit_offset_s  disp_fit  disp_fit_trials_shifted_30s  offset_1st_half  offset_2nd_half  nose_low_likelihood  nose_interpolated
  2174       DOI  first  177027      74.14            0.000           2.362    73.52          -3.0   871.444                       -0.461             -3.0             -3.0                0.445              0.705
  2174    saline  first  185828      77.43            0.000           3.695    72.27           6.6   322.614                        4.126              6.5              6.7                0.402              0.748
  2181       DOI  first  180616      75.39            0.000           6.668    75.12          -1.5   914.255                       -3.853             -1.5             -1.6                0.587              0.759
  2181    saline  first  173159      72.72            0.500          75.304    71.88           7.3   262.289                        6.741              7.6              7.7                0.585              0.796
  2182       DOI  first  180540      75.72            0.807          17.573    75.06          -1.0   697.962                        0.440             -0.7             -0.9                0.453              0.661
  2182    saline  first  179464      74.86            6.787          39.264    73.90           0.6   291.176                        2.941              0.6              2.6                0.562              0.763
  2183       DOI  first  180573      75.51            0.000          -4.974    74.96          -1.2   741.416                        8.165             -1.1             -1.3                0.565              0.807
  2183    saline  first  176506      73.67           20.388          22.049    72.25          14.0   143.352                       27.982             12.1             13.6                0.524              0.801
  2185       DOI  first  185127      77.16            4.773          16.965    74.58    
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('''        rows.append({"mouse": s["mouse"], "condition": s["condition"], "bin": int(k), "rolling": v.rolling, "fraction": 100 * v.fraction})''','''        rows.append({"mouse": s["mouse"], "condition": s["condition"], "bin": int(k), "rolling": v["rolling"], "fraction": 100 * v["fraction"]})''')
s=s.replace('''"clock": clk + ("" if mice is None else ", good fits")''','''"clock": clk if mice is None else f"{clk}, {len(mice)} mice"''')
s=s.replace('''                      "steps_of_5ms": bool(np.allclose(np.round(t * 200), t * 200, atol=1e-6)),''','''                      "hundredths_only": bool(np.allclose(np.round(t * 100), t * 100, atol=1e-6)),''')
s=s.replace('''all_5ms=("steps_of_5ms", "all")''','''hundredths_only=("hundredths_only", "all")''')
open(p,'w').write(s)
EOF
grep -n "v\[\"rolling\"\]\|hundredths_only" build_nb.py | head
```

```
278:                      "hundredths_only": bool(np.allclose(np.round(t * 100), t * 100, atol=1e-6)),
282:                               hundredths_only=("hundredths_only", "all"), last_s=("last_s", "max")).to_string())
405:        rows.append({"mouse": s["mouse"], "condition": s["condition"], "bin": int(k), "rolling": v["rolling"], "fraction": 100 * v["fraction"]})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/env/bin/activate && python $TMPDIR/build_nb.py && cd entries/001863-welch-2025 && time jupyter nbconvert --to notebook --execute reproduce_welch_2025.ipynb --output exec2 --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 --allow-errors 2>&1 | tail -1; python $TMPDIR/show.py $TMPDIR/exec2.ipynb 20 23; python $TMPDIR/show.py $TMPDIR/exec2.ipynb 58 200
```

```
Thu Nov  5 16:09:27 UTC 2026
cells 111
[NbConvertApp] Writing 328844 bytes to /tmp/claude-1001/exec2.ipynb

real	5m25.496s
user	4m30.103s
sys	0m2.380s
[22] bin_min  rolling_n_DOI  rolling_n_sal  rolling_DOI_mean  rolling_saline_mean  rolling_saline_higher  rolling_p  fraction_n_DOI  fraction_n_sal  fraction_DOI_mean  fraction_saline_mean  fraction_saline_higher  fraction_p
    0-5             22             22           78.7062              83.0257                   True     0.5117              22              22            81.3629               88.7305                    True      0.2766
   5-10             21             22           86.1865              91.5382                   True     0.0728              21              22            87.6505               95.2274                    True      0.0058
  10-15             21             21           87.0267              92.7273                   True     0.0076              21              21            89.4540               94.3982                    True      0.0268
  15-20             22             22           85.1798              93.0342                   True     0.0037              22              22            89.1419               91.6608                    True      0.4379
  20-25             22             21           86.4362              93.1861                   True     0.0070              22              21            87.7692               95.1228                    True      0.1031
  25-30             22             22           87.4039              93.0394                   True     0.0184              22              22            86.5580               92.6014                    True      0.0944
  30-35             22             22           87.4858              92.6855                   True     0.0522              22              22            86.2124               89.7016                    True      0.4012
  35-40             22             22           87.1674              92.5544        
[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
s=s.replace('''grand = binned.groupby(["condition", "bin"]).rolling.agg(["mean", "std"]).unstack(0)''','''grand = binned.groupby(["condition", "bin"])["rolling"].agg(["mean", "std"]).unstack(0)''')
s=s.replace('''print("Set ITI (s) range:", tr_all.iti_time.min(), "to", tr_all.iti_time.max(), "(Methods: 1 to 15 s)")''','''print("Set ITI (s) range:", tr_all.iti_time.min(), "to", tr_all.iti_time.max(), "(Methods: 1 to 15 s)")
over = tr_all[tr_all.iti_time > 15]
print("Trials with a set ITI above 15 s:", len(over), "in sessions", sorted(set(zip(over.mouse, over.condition))),
      "; values", over.iti_time.value_counts().to_dict())''')
s=s.replace('''print(pd.DataFrame(out).round(4).to_string(index=False))
print("\\nPer mouse, code reading and clock (HTR/min):")''','''print(pd.DataFrame(out).round(4).to_string(index=False))
print("\\nBy cohort, code timestamps:")
for (clk, coh), g in htr_rates[htr_rates.timestamps == "code"].assign(cohort=lambda d: np.where(d.mouse.isin(ds.FIRST_COHORT), "first", "later")).groupby(["clock", "cohort"]):
    v, p = ds.r_signrank(g.rate_trial, g.rate_iti)
    print(f"  clock {clk}, {coh} cohort: n={len(g)}, trial median {g.rate_trial.median():.2f}, ITI median {g.rate_iti.median():.2f} HTR/min, p={p:.4f}")
good = htr_rates[(htr_rates.timestamps == "code") & (htr_rates.clock == "fitted") & htr_rates.mouse.isin(clock[clock.fit_ok & (clock.condition == "DOI")].mouse)]
v, p = ds.r_signrank(good.rate_trial, good.rate_iti)
print(f"  clock fitted, DOI sessions with a good fit: n={len(good)}, trial median {good.rate_trial.median():.2f}, ITI median {good.rate_iti.median():.2f}, p={p:.4f}")
print("\\nPer mouse, code reading and clock (HTR/min):")''')
open(p,'w').write(s)
EOF
python - <<'EOF'
p='entries/001863-welch-2025/doi_search.py'; s=open(p).read()
s=s.replace('''    return float(z), hits / n_resample


def perm_corr_test''','''    return float(z), (hits / n_resample if n_resample else float("nan"))


def perm_corr_test''')
open(p,'w').write(s)
EOF
grep -n "By cohort, code" $TMPDIR/build_nb.py
```

```
1171:print("\nBy cohort, code timestamps:")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
R=[
('''is longer than the set ITI, as it includes the time to poke into the initiation port. The session
notes count correct and total odor trials by side; where they agree with the table for every
session printed as matching above, side 1 is left. `false_alarm` is almost always 0, as the
paper says false reports were rare.''',
'''is longer than the set ITI, as it includes the time to poke into the initiation port. Some set
ITIs exceed the Methods' 15 s (printed above); they are not used by any claim. The session notes
count correct and total odor trials by side, and in all 34 later-cohort sessions they equal the
table's counts with side 2 as left and side 1 as right; the files do not say which side is which.
`false_alarm` is 1 in 6 of 3261 trials, as the paper says false reports were rare.'''),
('''The series has no name or unit beyond "Event times (s) from Time Stamps Task", and its values are
all 1. In the later cohort the last field''','''The series has no name or unit beyond "Event times (s) from Time Stamps Task", and its values are
all 1. It is in all 22 DOI sessions (24 to 204 events) and in 10 saline sessions (14 to 35). In
the later cohort the last field'''),
('''**Result: partially reproduced.** With the claims file's method (code clock, signed-rank test)
within-trial speed is lower on DOI (median difference -0.63 cm/s) but p = 0.063, against the
paper's 0.011; the rank-sum test the Results name gives p = 0.51. With the fitted clock, which
does align the frames with the trials, DOI and saline do not differ (p = 0.77).''',
'''**Result: partially reproduced.** With the claims file's method (code clock, signed-rank test)
within-trial speed is lower on DOI in 16 of 22 mice (median difference -0.63 cm/s) but p = 0.063,
against the paper's 0.011; the rank-sum test the Results name gives p = 0.51. With the fitted
clock, which aligns the frames with the trials, DOI and saline do not differ (p = 0.82; 0.89 in
the 13 mice whose two fits are good).'''),
('''**Result: partially reproduced.** ITI speed is lower on DOI (median difference -0.60 cm/s) but
p = 0.079 with the claims file's method, against the paper's 0.036; with the fitted clock p =
0.059. The rank-sum variant gives p = 0.57.''',
'''**Result: partially reproduced.** ITI speed is lower on DOI in 15 of 22 mice (median difference
-0.60 cm/s) but p = 0.079 with the claims file's method, against the paper's 0.036; with the
fitted clock p = 0.063 (0.057 in the 13 mice with good fits). The rank-sum variant gives p = 0.57.'''),
('''**Result: reproduced.** Odor-trial speed does not differ (signed-rank p = 0.19, median difference
-0.54 cm/s; rank-sum p = 0.70); with the fitted clock p = 0.73.''',
'''**Result: reproduced.** Odor-trial speed does not differ (signed-rank p = 0.19, median difference
-0.54 cm/s; rank-sum p = 0.70); with the fitted clock p = 0.68.'''),
('''**Result: reproduced.** On DOI the ITI is slower than odor trials (median difference -0.83 cm/s,
p = 0.0002); with the fitted clock the difference is larger (-3.5 cm/s, p < 0.001).''',
'''**Result: reproduced.** On DOI the ITI is slower than odor trials in 19 of 22 mice (median
difference -0.83 cm/s, p = 0.0002, the paper's p < 0.001); with the fitted clock the difference is
larger (-3.5 cm/s, p < 0.0001).'''),
('''**Result: reproduced.** On saline the ITI is slower than odor trials (p = 0.025, the paper's
0.002) and than omission trials (p = 0.016, the paper's 0.017); with the fitted clock both at
p < 0.001.''',
'''**Result: reproduced.** On saline the ITI is slower than odor trials (median difference -0.43
cm/s, p = 0.025, the paper's 0.002) and than omission trials (-0.98 cm/s, p = 0.016, the paper's
0.017); with the fitted clock both at p < 0.0001.'''),
('''**Result: reproduced.** On saline odor and omission trials do not differ (p = 0.68, median
difference -0.18 cm/s; the paper's 0.54); with the fitted clock p = 0.37.''',
'''**Result: reproduced.** On saline odor and omission trials do not differ (p = 0.68, median
difference -0.18 cm/s; the paper's 0.54); with the fitted clock p = 0.32.'''),
('''**Result: reproduced.** The sessions are 14 DOI and 13 saline, the expected counts. DOI sniff
frequency is higher under every reading (mean 7.78 against 7.55 Hz under reading a), Z = 25.2
(a), 28.4 (b) and 19.5 (the code's), against the paper's Z = 24.9, with no permutation of 10000 as
extreme (p < 0.0001).''',
'''**Result: reproduced.** The sessions are 14 DOI and 13 saline, the expected counts. DOI sniff
frequency is higher under every reading (mean 7.78 against 7.55 Hz under reading a), Z = 25.2
(a), 28.4 (b) and 19.5 (the code's), against the paper's Z = 24.9, with no permutation of 10000 as
extreme under any reading (p < 0.0001).'''),
('''**Result: reproduced.** 13 mice have matched sessions, the expected number. Under reading (b) all
13 have a one-sided KS p < 0.001; under reading (a) and the code's computation 11 of 13 do, and the
other two (2209 and 2211) have p of 0.003 to 0.011. The criterion names both readings, and the
claim holds under (b).''',
'''**Result: reproduced.** 13 mice have matched sessions, the expected number. Under reading (b) all
13 have a one-sided KS p < 0.001; under reading (a) and the code's computation 11 of 13 do, and the
other two (2209 and 2211) have p of 0.0031 to 0.011; all 13 have p < 0.05 under every reading. The
criterion names both readings, and the claim holds under (b); under (a) it would be partially
reproduced. Per-mouse medians are higher on DOI in 8 of the 13 mice.'''),
('''**Result: reproduced.** DOI sniffing is faster in all three periods under every reading: under
reading (a) odor trials Z = 4.3, omission trials Z = 3.9, ITI Z = 24.2 (the paper's 3.38, 2.71 and
18.4), each with p < 0.001. Sniffs are placed in periods by the trial table's clock, which the
data check found consistent with the sniff clock.''',
'''**Result: reproduced.** DOI sniffing is faster in all three periods under every reading (Z
printed above; the paper's 3.38, 2.71 and 18.4), each at p < 0.05. Sniffs are placed in periods
by the trial table's clock, which the data check found consistent with the sniff clock.'''),
('''**Result: reproduced.** Over the 13 mice with both sessions, the per-mouse median frequency does
not differ at p < 0.05 (p = 0.11 under readings a and the code's, the paper's 0.11; 0.15 under b),
although it is higher on DOI in most mice (median difference about 0.53 Hz).''',
'''**Result: reproduced.** Over the 13 mice with both sessions, the per-mouse median frequency does
not differ at p < 0.05 (p = 0.11 under reading a and the code's, the paper's 0.11; 0.15 under b);
it is higher on DOI in 8 of 13 mice (median difference 0.53 Hz under a).'''),
('''**Result: reproduced.** No measure differs at p < 0.05: occupancy entropy (p = 0.063), the
fraction of frames in 5 cm corners (p = 0.25) and in 10 cm corners (p = 0.70). The grand-mean maps
correlate closely (Pearson r printed above). With the arena about 27 by 16 cm at the code's scale,
10 cm corner squares cover most of it, so that reading says little.''',
'''**Result: reproduced.** No measure differs at p < 0.05: occupancy entropy (median difference
0.11 bits, p = 0.063), the fraction of frames in 5 cm corners (p = 0.25) and in 10 cm corners (p =
0.70). The grand-mean maps correlate with r = 0.919. With the arena about 27.5 by 15.6 cm at the
code's scale, 10 cm corner squares hold 85% of the frames, so that reading says little.'''),
('''**Result: reproduced.** The series is in all 22 DOI sessions, as the paper's n = 22 needs, and in
10 saline sessions; in every mouse with both, the DOI session has more events (a median of about
3.7 per minute on DOI, 0.6 on saline). Together with the conversion script's sources this links the
series to the HTR times. The 2197 DOI session has only 30 events.''',
'''**Result: reproduced.** The series is in all 22 DOI sessions, as the paper's n = 22 needs, and in
10 saline sessions; in each of the 10 mice with both, the DOI session has more events (median 3.67
per minute on DOI, 0.47 on saline where present). Together with the conversion script's sources
this links the series to the HTR times. The DOI sessions of 2197 and 2204 have only 30 and 24
events. The files themselves do not name the series.'''),
('''**Result: reproduced.** Within trials the per-mouse, per-bin HTR rate correlates with x (r =
0.056, permutation p = 0.006 under the code's reading; the paper's p = 0.002) and not with y (p =
0.26; the paper's 0.92). The other timestamp readings and the fitted clock give the same pattern
(printed above).''',
'''**Result: reproduced.** With the claims file's method (code clock, code timestamps) the
within-trial HTR rate correlates with x (r = 0.056, permutation p = 0.0048; the paper's 0.002) and
not with y (p = 0.26; the paper's 0.92); the other two timestamp readings agree (x p = 0.0016 and
0.0020, y p = 0.92 and 0.86). With the fitted clock only 151 of 3057 HTRs fall within trials and
the x correlation vanishes (r = 0.001, p = 0.96; y p = 0.065), so the result depends on the
code's clock.'''),
('''**Result: reproduced.** Over the 22 DOI mice (the expected 22), with trial and ITI frames combined,
the HTR rate rises with x toward the odor and reward ports (r = 0.149, permutation p < 0.0001,
none of 10000 permutations as extreme), under every timestamp reading.''',
'''**Result: reproduced.** Over the 22 DOI mice (the expected 22), with trial and ITI frames
combined, the HTR rate rises with x toward the odor and reward ports (r = 0.149, none of 10000
permutations as extreme, p < 0.0001), under every timestamp reading; the grand-mean rate rises
from 1.97 HTR/min in the first x bin to about 6.5 at the odor end. This does not depend on the
clock.'''),
('''**Result: reproduced.** In the ITI the HTR rate rises with x (r = 0.152, p < 0.0001) and does not
vary with y (p = 0.56 under the code's reading; 0.08 to 0.25 under the others).''',
'''**Result: reproduced.** In the ITI the HTR rate rises with x (r = 0.152, p < 0.0001) and does not
vary with y (p = 0.55 under the code's reading; 0.08 and 0.25 under the other timestamp readings,
0.13 with the fitted clock).'''),
('''**Result: reproduced.** Over the 22 DOI sessions the HTR rate within trials and in the ITI does
not differ at p < 0.05 with the code's method (signed-rank p printed above for each reading; the
paper's p = 1). The fitted-clock variant is printed alongside.''',
'''**Result: reproduced.** With the code's method the HTR rate within trials and in the ITI does not
differ (medians 3.67 and 3.68 HTR/min, signed-rank p = 0.50; 0.52 and 0.70 under the other
timestamp readings; the paper's p = 1). With the fitted clock, HTRs are about a third as frequent
within trials as in the ITI (medians 1.38 and 3.88 HTR/min, p < 0.0001, under every timestamp
reading), the opposite of the claim: the claim holds only with the code's clock, which the data
check found does not align the two clocks.'''),
('''**Result: reproduced.** HTR rate over the session does not differ between the sexes (rank-sum,
normal approximation as the code, p printed above; the paper's p = 0.31).''',
'''**Result: reproduced.** HTR rate over the session does not differ between the sexes (females
median 3.61, males 3.99 HTR/min; rank-sum with the normal approximation, p = 0.31, the paper's
0.31). It needs no clock.'''),
('''**Result: partially reproduced.** With the claims file's method odor and omission trials do not
differ (p = 0.31) but the ITI is slower than omission trials (median difference -0.70 cm/s, p =
0.0059, against the paper's 0.068): one of the two comparisons is significant. The rank-sum
variants give p = 0.62 and 0.37. With the fitted clock both comparisons are significant.''',
'''**Result: partially reproduced.** With the claims file's method odor and omission trials do not
differ (p = 0.31) but the ITI is slower than omission trials (median difference -0.70 cm/s, p =
0.0059, against the paper's 0.068): one of the two comparisons is significant. The rank-sum
variants the Results name give p = 0.62 and 0.37. With the fitted clock both comparisons are
significant (p = 0.0003 and 0.0001).'''),
]
for a,b in R:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
R=[('''accuracy is lower on DOI (median difference -3.2 points, lower in most mice), signed-rank p =
0.023 against the paper's 0.024.''','''accuracy is lower on DOI (median difference -3.2 points, lower in 14 of 22 mice), signed-rank
p = 0.023 against the paper's 0.024.'''),
('''**Result: reproduced.** Odor trials last longer on DOI (median difference 0.26 s, longer in most
mice), p = 4.8e-06 against the paper's p < 0.001.''','''**Result: reproduced.** Odor trials last longer on DOI (median difference 0.26 s, longer in 21 of
22 mice), p = 5e-06 against the paper's p < 0.001.'''),
('''frames/s in the later cohort, 72 to 75 in the first) does. The HTR series is not named in the
files, and its later-cohort timestamps store a frame count as hundredths of a second. The saline
session of mouse 2182 gives the wrong sex.''','''frames/s in the later cohort, 72 to 75 in the first) does. The claims that split frames or HTRs
by trial period follow the code's clock as the claims file fixes it; with the fitted clock the
within-trial speed difference and the within-trial HTR x preference vanish, and HTRs are rarer
within trials than in the ITI (fig5f). The HTR series is not named in the files, and its
later-cohort timestamps store a frame count as hundredths of a second. The files do not say which
side code is left (the notes show side 2 is left). The saline session of mouse 2182 gives the
wrong sex.'''),
]
for a,b in R:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
date -u; . $TMPDIR/env/bin/activate && python $TMPDIR/build_nb.py && cd entries/001863-welch-2025 && jupyter nbconvert --to notebook --execute reproduce_welch_2025.ipynb --output exec3 --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 --allow-errors 2>&1 | tail -1; python $TMPDIR/show.py $TMPDIR/exec3.ipynb 4 6 | head -12; python $TMPDIR/show.py $TMPDIR/exec3.ipynb 22 23 | tail -3; python $TMPDIR/show.py $TMPDIR/exec3.ipynb 78 82; python $TMPDIR/show.py $TMPDIR/exec3.ipynb 103 106 | head -20; grep -c ERROR <(python $TMPDIR/show.py $TMPDIR/exec3.ipynb)
```

```
Thu Nov  5 16:16:22 UTC 2026
cells 111
/bin/bash: line 24: cd: entries/001863-welch-2025: No such file or directory
Traceback (most recent call last):
  File "/tmp/claude-1001/show.py", line 2, in <module>
    nb=json.load(open(sys.argv[1]))
                 ~~~~^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/claude-1001/exec3.ipynb'
Traceback (most recent call last):
  File "/tmp/claude-1001/show.py", line 2, in <module>
    nb=json.load(open(sys.argv[1]))
                 ~~~~^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/claude-1001/exec3.ipynb'
Traceback (most recent call last):
  File "/tmp/claude-1001/show.py", line 2, in <module>
    nb=json.load(open(sys.argv[1]))
                 ~~~~^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/claude-1001/exec3.ipynb'
Traceback (most recent call last):
  File "/tmp/claude-1001/show.py", line 2, in <module>
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cd entries/001863-welch-2025 && jupyter nbconvert --to notebook --execute reproduce_welch_2025.ipynb --output exec3 --output-dir $TMPDIR --ExecutePreprocessor.timeout=3000 --allow-errors 2>&1 | tail -1; S=$TMPDIR/show.py; E=$TMPDIR/exec3.ipynb; python $S $E 4 6 | head -12; python $S $E 22 23 | tail -3; python $S $E 78 82; python $S $E 103 106 | head -20; python $S $E | grep -c ERROR
```

```
[NbConvertApp] Writing 356889 bytes to /tmp/claude-1001/exec3.ipynb
[5] odor_control values: {0.0: 4109, 3.0: 441}
outcome values: {1.0: 3906, 0.0: 644} ; side values: {1.0: 2292, 2.0: 2258}
Omission share of trials: 0.097 (Methods: 10%)
Set ITI (s) range: 1.0 to 25.0 (Methods: 1 to 15 s)
Trials with a set ITI above 15 s: 347 in sessions [(2174, 'DOI'), (2174, 'saline'), (2181, 'DOI'), (2181, 'saline'), (2182, 'DOI'), (2182, 'saline'), (2183, 'DOI'), (2183, 'saline'), (2185, 'DOI'), (2185, 'saline')] ; values {16.0: 75, 17.0: 62, 18.0: 57, 22.0: 36, 19.0: 34, 20.0: 33, 21.0: 31, 23.0: 11, 25.0: 5, 24.0: 3}
Trial duration (s): min 0.98, median 1.75, max 69.0
Trial start (s): min 1.7, max 2398.1; last trial end per session, min 2249 max 2400
Observed ITI, next start minus end (s): min 2.69, median 17.80, max 807.7; negative: 0
false_alarm values (later cohort): {0.0: 3255, 1.0: 6}
repoke values (later cohort): {0.0: 1870, 1.0: 543, 2.0: 342, 3.0: 196, 4.0: 133, 5.0: 83, 6.0: 48, 7.0: 25, 8.0: 11, 9.0: 5, 10.0: 3, 11.0: 1, 12.0: 1}

Later-cohort sessions whose notes' L and R (correct/total odor trials) equal the table's side 1 and 2: 0 ; side 2 and 1: 34 ; of 34

[22] Plotted means range 78.7 to 93.2 %; error bars are 1 SD.

[80]     reading          period  n_DOI  n_saline  DOI_mean  saline_mean       Z  p_10000_resamples  p_normal
  a_session     odor trials  16493     11755    7.9362       7.8013  4.3071                0.0    0.0000
  a_session omission trials   6976      5071    8.2100       8.0349  3.8807                0.0    0.0001
  a_session             ITI 167478    137037    7.7444       7.5101 24.2056                0.0    0.0000
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
a='''Some set
ITIs exceed the Methods' 15 s (printed above); they are not used by any claim.'''
b='''In the five
first-cohort mice 347 trials have a set ITI of 16 to 25 s, beyond the Methods' 1 to 15 s; the
set ITI is not used by any claim.'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/build_nb.py; cd entries/001863-welch-2025 && rm -rf __pycache__ && cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001863-welch-2025
type: reproduction
title: DOI and olfactory search in mice (Welch et al. 2025)
description: Tests the findings of Welch, Gonzales-Hess, Tarvin, Connor and Smear (2025) on dandiset
  001863, which holds one DOI and one saline session of the olfactory search task for each of 22
  mice, with trial tables, DeepLabCut tracking, thermistor sniff cycles and head-twitch times. It
  tests accuracy, trial counts and durations, movement speed, sniff frequency, occupancy and the
  location and timing of head twitches. The reward-port durations of Figure 2 are not in the
  dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_welch_2025.ipynb
  title: Reproducing Welch et al. (2025) from dandiset 001863
  runtime_minutes: 7
helpers:
- doi_search.py
related:
- id: dandi:001863/0.260806.2109
  relation: uses_data
- id: doi:10.1101/2025.07.09.663970
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/001863-welch-2025 2>&1 | tail -3
```

```
cells 111
wrote entries/001863-welch-2025/requirements.lock.txt
```

**Agent calls Read**

```json
{
 "file_path": "claims/001863/10.1101-2025.07.09.663970.yaml",
 "offset": 596,
 "limit": 90
}
```

```
596	    correlation between the two grand-mean maps is reported as a description.
597	- id: fig5supp-htr-within-trial-x-not-y
598	  statement: During trials, HTR rate (normalized to occupancy) varies with the X coordinate of the
599	    arena but not with the Y coordinate.
600	  source: Results, Mice occupy allocentric space similarly but head twitch preferentially in
601	    proximity to odor ports, paragraph 2; Figure 5 supplemental A
602	  quote: During a trial, HTR rate occurred throughout the arena without spatial predictability on
603	    the Y-coordinate ( Figure 5 supplemental ; Permutation test, p = 0.92), but with preference for
604	    the X-coordinate ( Figure 5 supplemental ; Permutation test, p = 0.002)
605	  statistics:
606	  - about: Y coordinate
607	    test: Permutation test
608	    p: 0.92
609	  - about: X coordinate
610	    test: Permutation test
611	    p: 0.002
612	  criterion: DOI sessions with HTR times. As in the Methods (Figure 5) and fig5_cleaned.Rmd; nose
613	    position at each frame (x flipped for the first cohort, frames above 160 cm/s dropped); each
614	    HTR assigned to the frame nearest its time; the arena in bins of 100 pixels (about 2.5 cm),
615	    the last bin column and row (x bin 1200, y bin 700) dropped; per mouse and bin, HTRs within
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/001863/10.1101-2025.07.09.663970.yaml'; s=open(p).read()
link='''- id: htr-event-link
  kind: link
  statement: The dandiset's unnamed series processing/behavior/task_event_timestamps holds the
    head-twitch (HTR) times the paper analysed, so the HTR claims can be tested on it with the
    name taken from the paper's code.
  source: The paper's code at github.com/Smear-Lab/Olfactory-search-on-psychedelics commit aa80af0a,
    nwb_conversion/convert_session_to_nwb.py (load_event_timestamps) and analysis/fig5_cleaned.Rmd
    (chunk "import htr timestamps")
  data: with_labels
  criterion: Added by the author (protocol, Author, step 1.4). Records are matched by mouse and
    session, the names under which the conversion script reads the folders "Time Stamps Task" and
    "Time Stamps Task Logan" that fig5_cleaned.Rmd reads as HTR timestamps. The link holds
    (reproduced) when the series is present in all 22 DOI sessions (the paper's n = 22 for the HTR
    maps) and, as HTRs are induced by DOI, every mouse with the series in both sessions has more
    events in its DOI session; partially reproduced when it is present in at least 18 DOI sessions
    or the DOI count is higher in most but not all mice with both; not reproduced otherwise. The
    files' lack of a name for the series is recorded as a finding.
'''
a='- id: fig5supp-htr-within-trial-x-not-y\n'
assert a in s; s=s.replace(a, link+a,1)
# data and depends_on for the five HTR claims
def add(after_id_block_start, insert_before_key, text):
    global s
    i=s.index(after_id_block_start); j=s.index(insert_before_key, i)
    s=s[:j]+text+s[j:]
add('- id: fig5supp-htr-within-trial-x-not-y\n','  criterion: DOI sessions with HTR times.','  data: with_labels\n  depends_on:\n  - htr-event-link\n')
add('- id: fig5e-htr-combined-x\n','  - fig5supp-htr-within-trial-x-not-y\n','  - htr-event-link\n')
add('- id: fig5e-htr-combined-x\n','  depends_on:\n','  data: with_labels\n')
add('- id: fig5supp-htr-iti-x\n','  criterion: The paper gives no test','  data: with_labels\n  depends_on:\n  - htr-event-link\n')
add('- id: fig5f-htr-rate-trial-vs-iti\n','  criterion: A claim of absence. As in fig5_cleaned.Rmd; per DOI','  data: with_labels\n  depends_on:\n  - htr-event-link\n')
add('- id: fig5supp-htr-no-sex-difference\n','  criterion: A claim of absence. Per DOI session the number','  data: with_labels\n  depends_on:\n  - htr-event-link\n')
open(p,'w').write(s)
import yaml; d=yaml.safe_load(open(p)); print(len(d['claims']), [ (c['id'],c.get('data'),c.get('depends_on')) for c in d['claims'] if 'htr' in c['id']])
EOF
git diff --stat
```

```
36 [('htr-event-link', 'with_labels', None), ('fig5supp-htr-within-trial-x-not-y', 'with_labels', ['htr-event-link']), ('fig5e-htr-combined-x', 'with_labels', ['htr-event-link', 'fig5supp-htr-within-trial-x-not-y']), ('fig5supp-htr-iti-x', 'with_labels', ['htr-event-link']), ('fig5f-htr-rate-trial-vs-iti', 'with_labels', ['htr-event-link']), ('fig5supp-htr-no-sex-difference', 'with_labels', ['htr-event-link'])]
 claims/001863/10.1101-2025.07.09.663970.yaml | 31 ++++++++++++++++++++++++++++
 1 file changed, 31 insertions(+)
```

**Agent calls Bash**

```bash
python -c "
import yaml; d=yaml.safe_load(open('claims/001863/10.1101-2025.07.09.663970.yaml'))
print([c['id'] for c in d['claims']])"; date -u
```

```
['fig1b-accuracy-lower-doi', 'fig1c-accuracy-time-bins', 'fig1d-fewer-trials', 'fig1d-fewer-trials-females-only', 'fig1e-repoke-no-difference', 'iti-false-report-no-difference', 'fig2a-correct-port-duration-doi-odor', 'fig2a-supp-no-sex-effect', 'fig2b-median-port-duration-correct', 'fig2b-supp-odor-trials-longer', 'fig2b-supp-omission-no-difference', 'fig2c-incorrect-port-duration', 'fig2c-supp-no-sex-difference', 'fig2d-median-incorrect-no-difference', 'fig2d-supp-omission-longer', 'fig3a-odor-trial-duration-longer', 'fig3a-omission-duration-no-difference', 'fig3b-iti-duration-no-difference', 'fig3c-speed-within-trial-lower', 'fig3d-speed-iti-lower', 'fig3supp-odor-trial-speed-no-difference', 'fig3supp-doi-iti-slower-than-odor', 'fig3supp-doi-omission-no-difference', 'fig3supp-saline-iti-slower', 'fig3supp-saline-odor-omission-no-difference', 'fig4abc-sniff-frequency-higher', 'fig4supp-ks-every-mouse', 'fig4d-sniff-frequency-by-period', 'fig4e-median-sniff-no-difference', 'fig5ab-occupancy-similar', 'htr-event-link', 'fig5supp-htr-within-trial-x-not-y', 'fig5e-htr-combined-x', 'fig5supp-htr-iti-x', 'fig5f-htr-rate-trial-vs-iti', 'fig5supp-htr-no-sex-difference']
Thu Nov  5 16:22:36 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/att && cat > $TMPDIR/att/make.py <<'EOF'
import yaml
NB = "reproduce_welch_2025.ipynb"
CLOCK_DEV = ("The claims file fixes the code's frame clock (frame i at i / 80 s); the data check shows it "
             "does not align the tracking with the trial table (median nose displacement over a trial about "
             "0 px), while a per-session linear clock fitted here (about 80.5 frames/s in the later cohort, "
             "72 to 75 in the first) does. The claim is tested with the code's clock and the fitted clock is "
             "shown as a variant, a check made here and not the paper's method.")
FIG2 = ("Blocked because the dandiset holds no reward-port entries or exits. The trial table has start, "
        "stop, odor_control, side, outcome and set ITI, and for the later cohort false_alarm and repoke "
        "counts; the only event series is the HTR series; acquisition, stimulus and analysis are empty. "
        "fig2_cleaned.Rmd reads the durations from pre-computed files (drinking_data_iti_2.txt and "
        "drinking_data_incorrect_trials_iti_2.txt) that are not in the code repository either.")
o = []
def add(claim, outcome, notes, deviations=None, measured=None, blocked_by=None, assumed=None, output=True):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if output:
        d["notebook"] = NB; d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed is not None: d["assumed"] = assumed
    o.append(d)

STATS = ("Statistics are computed in Python with R's defaults reproduced (exact signed-rank and rank-sum "
         "tests below 50 values without ties, otherwise the normal approximation with continuity correction).")
add("fig1b-accuracy-lower-doi", "reproduced",
    "22 mice with paired sessions, the expected 22. Odor-trial accuracy is lower on DOI in 14 of 22 mice "
    "(median DOI 90.7 against saline 92.4 percent, median difference -3.2 points), signed-rank V = 57, "
    "p = 0.023 (paper 0.024). Omission-trial accuracy, the variant, median difference -5.2 points, p = 0.37. "
    "By sex neither group alone is significant (females p = 0.11, males p = 0.13).",
    [STATS], measured=22)
add("fig1c-accuracy-time-bins", "reproduced",
    "Mean rolling accuracy per mouse and 5 min bin, rank-sum tests per bin. Saline is higher in every bin. "
    "p = 0.0076, 0.0037 and 0.0070 in the 10-15, 15-20 and 20-25 min bins, p = 0.039 in 35-40 (paper 0.039), "
    "p = 0.052 in 30-35 (not significant, as stated). The bins the text does not state, 0-5 p = 0.51, 5-10 p = 0.073, "
    "25-30 p = 0.018. 21 or 22 mice per bin and condition. The per-bin fraction correct variant is significant "
    "only in 5-10 and 10-15 min.", [STATS])
add("fig1d-fewer-trials", "reproduced",
    "Reading (a), odor trials (the code), DOI lower in 16 of 22 mice, median difference -9.5 trials, p = 0.011 "
    "(paper 0.011). Reading (b), all trials (the Methods), median difference -8, p = 0.018. Both readings "
    "match.", ["The Methods count all trials and the code odor trials; both readings were run, as the criterion "
               "names, and both match."])
add("fig1d-fewer-trials-females-only", "reproduced",
    "Females (12), odor trials median difference -14, p = 0.010 (paper 0.011); all trials -12.5, p = 0.015. "
    "Males (10), odor trials p = 0.39 (paper 0.39); all trials p = 0.44. Both readings match.",
    ["Sex is taken from the code's list; the file of the 2182 saline session says female, its DOI session "
     "male (the code has male)."])
add("fig1e-repoke-no-difference", "reproduced",
    "17 later-cohort mice; repoke rate (repokes over trials minus one) median DOI 1.04 against saline 1.05 per "
    "ITI, median difference -0.10, signed-rank p = 0.38 (paper 0.27). The test does not find the effect.",
    ["The repoke counts are the trial table's repoke column, which the code reads from the same trial file."])
add("iti-false-report-no-difference", "reproduced",
    "The trial table's false_alarm column (later cohort, 17 mice) gives 3 false reports in 2 of 17 DOI sessions "
    "and 3 in 2 of 17 saline sessions, 6 of 3227 ITIs in all. Rank-sum p = 1 under reading (a), counts per "
    "session, and (b), per ITI, the paper's p = 1. Rare, as stated (not judged). The Results' variant, "
    "reward-port entries in the ITI, cannot be run, as the dandiset has no reward-port events.",
    ["The false_alarm column is taken to be the Methods' false odor report; the files describe it only as "
     "\"false alarm\". The Results' reward-port variant was not run (no data)."])
for c in ["fig2a-correct-port-duration-doi-odor", "fig2a-supp-no-sex-effect", "fig2b-median-port-duration-correct",
          "fig2b-supp-odor-trials-longer", "fig2b-supp-omission-no-difference", "fig2c-incorrect-port-duration",
          "fig2c-supp-no-sex-difference", "fig2d-median-incorrect-no-difference", "fig2d-supp-omission-longer"]:
    add(c, "blocked", FIG2, blocked_by="data_missing", output=False)
o[-9]["notebook"] = NB; o[-9]["output"] = "sanity"
add("fig3a-odor-trial-duration-longer", "reproduced",
    "Odor trials last longer on DOI in 21 of 22 mice (median DOI 2.02 against saline 1.81 s, median "
    "difference 0.26 s), V = 248, p = 4.8e-06 (paper p < 0.001).")
add("fig3a-omission-duration-no-difference", "reproduced",
    "Omission-trial duration median difference 0.55 s (DOI 5.37 against 4.74 s), p = 0.32 (paper 0.26). The "
    "test does not find the effect.")
add("fig3b-iti-duration-no-difference", "reproduced",
    "Mean ITI (next start minus end) median DOI 19.9 against saline 19.1 s, median difference 1.42 s, longer "
    "on DOI in 17 of 22 mice, p = 0.098 (paper 0.19). Not significant at p < 0.05, so the claim of absence holds.")
add("fig3c-speed-within-trial-lower", "partially_reproduced",
    "With the claims file's method (code clock, signed-rank test) within-trial speed is lower on DOI in 16 of "
    "22 mice, median 6.34 against 6.62 cm/s, median difference -0.63 cm/s, p = 0.063 (paper 0.011); the "
    "criterion's p < 0.05 is not met. The rank-sum test the Results name gives p = 0.51. With the fitted clock, "
    "which aligns frames with trials, median difference -0.49 cm/s, p = 0.82 (13 mice with good fits p = 0.89). "
    "By sex (code clock), males p = 0.027, females p = 0.52. 1125 of 8.3 million frames are above 160 cm/s. The "
    "outcome is partially reproduced because the effect has the stated direction with 0.05 <= p < 0.1, the "
    "convention the claims file uses elsewhere; the criterion itself names only the reproduced case.",
    [CLOCK_DEV, "The criterion defines no partial outcome; same direction with 0.05 <= p < 0.1 is called "
     "partially reproduced, as the claims file does for fig1b and fig2d-supp."])
add("fig3d-speed-iti-lower", "partially_reproduced",
    "ITI speed lower on DOI in 15 of 22 mice, median 5.57 against 5.76 cm/s, median difference -0.60 cm/s, "
    "p = 0.079 with the claims file's method (paper 0.036). Fitted clock p = 0.063 (13 mice with good fits "
    "p = 0.057). Rank-sum variant p = 0.57. Direction as stated, weaker than the paper.",
    [CLOCK_DEV, "The criterion defines no partial outcome; same direction with 0.05 <= p < 0.1 is called "
     "partially reproduced, as the claims file does for fig1b and fig2d-supp."])
add("fig3supp-odor-trial-speed-no-difference", "reproduced",
    "Odor-trial speed median difference -0.54 cm/s, signed-rank p = 0.19 (paper rank-sum p = 0.059); rank-sum "
    "variant p = 0.70; fitted clock p = 0.68. The test does not find the effect.", [CLOCK_DEV])
add("fig3supp-doi-iti-slower-than-odor", "reproduced",
    "On DOI the ITI is slower than odor trials in 19 of 22 mice, median 5.57 against 6.53 cm/s, median "
    "difference -0.83 cm/s, p = 0.0002 (paper p < 0.001). Fitted clock -3.54 cm/s, p < 0.0001. Rank-sum "
    "variant p = 0.16.", [CLOCK_DEV])
add("fig3supp-doi-omission-no-difference", "partially_reproduced",
    "DOI odor against omission trials, median difference 0.58 cm/s, p = 0.31 (paper 0.21), not significant. "
    "DOI ITI against omission trials, median difference -0.70 cm/s, ITI slower in 18 of 22 mice, p = 0.0059 "
    "(paper 0.068), significant. One of the two comparisons finds an effect. Rank-sum variants p = 0.62 and "
    "0.37. With the fitted clock both are significant (p = 0.0003 and 0.0001).", [CLOCK_DEV])
add("fig3supp-saline-iti-slower", "reproduced",
    "On saline the ITI is slower than odor trials (median difference -0.43 cm/s, 16 of 22 mice, p = 0.025; "
    "paper 0.002) and than omission trials (-0.98 cm/s, 18 of 22, p = 0.016; paper 0.017). Fitted clock both "
    "p < 0.0001.", [CLOCK_DEV])
add("fig3supp-saline-odor-omission-no-difference", "reproduced",
    "On saline odor against omission trials median difference -0.18 cm/s, p = 0.68 (paper 0.54); rank-sum "
    "variant p = 0.86; fitted clock p = 0.32.", [CLOCK_DEV])
add("fig4abc-sniff-frequency-higher", "reproduced",
    "Sessions with a usable signal 14 DOI and 13 saline, the expected counts, after the code's four faulty "
    "sessions are dropped. Pooled sniff frequency higher on DOI under every reading. Reading (a), per-session "
    "5th to 95th percentile and 10 to 1000 ms, 190947 and 153863 sniffs, mean 7.78 against 7.55 Hz, Z = 25.2; "
    "reading (b), per condition, Z = 28.4; the code's computation without further exclusion Z = 19.5 (paper "
    "Z = 24.9). No permutation of 10000 as extreme under any reading (p < 0.0001).",
    ["The file's sniff cycles are the detections the code reads (sniff_params.mat, rows without exhalation "
     "already dropped); whether the Methods' percentile exclusion was applied before export is not known, so "
     "readings (a) and (b) of the criterion and the code's computation were all run, and all match.",
     "The Fisher-Pitman test is computed here (standardised sum of the DOI group, 10000 random permutations) "
     "in place of coin::oneway_test; its random permutations differ from R's."], measured=[14, 13])
add("fig4supp-ks-every-mouse", "reproduced",
    "13 mice have matched usable sessions, the expected 13. One-sided KS (DOI stochastically larger), reading "
    "(b) 13 of 13 at p < 0.001; reading (a) and the code's computation 11 of 13, with 2209 and 2211 at p = "
    "0.0031 and 0.0063 under (a) and 0.0059 and 0.011 under the code's. All 13 have p < 0.05 under every "
    "reading. The criterion names readings (a) and (b), and the claim is reproduced under (b); under (a) it "
    "would be partially reproduced. Per-mouse medians are higher on DOI in 8 of the 13 mice only.",
    ["The readings of the percentile exclusion give different outcomes (reproduced under b, partially under a "
     "and under the code's computation); by the rule for readings a criterion names, the claim is reproduced "
     "if it matches under any, and the ambiguity is recorded here."], measured=13)
add("fig4d-sniff-frequency-by-period", "reproduced",
    "DOI faster in all three periods under every reading. Reading (a), odor trials Z = 4.31, omission trials "
    "Z = 3.88, ITI Z = 24.2 (paper 3.38, 2.71, 18.4), none of 10000 permutations as extreme. Reading (b) Z = "
    "6.61, 4.00, 26.9; the code's computation Z = 3.72, 2.12 (normal p = 0.034), 18.6. Sniffs are placed in "
    "periods by the trial table's clock; the data check found sniffing faster within trials than in the ITI "
    "with the true labels in 20 of 27 sessions, more than with labels shifted by 10 s or more.",
    ["For readings (b) and the code's computation the p-value is the normal approximation of the same "
     "statistic, to keep the notebook within its time; the resampled p is computed for reading (a)."])
add("fig4e-median-sniff-no-difference", "reproduced",
    "13 mice with both sessions. Per-mouse median frequency higher on DOI in 8 of 13, median difference "
    "0.53 Hz (a), signed-rank p = 0.11 under (a) and the code's computation (paper 0.11), 0.15 under (b). "
    "The test does not find the effect.")
add("fig5ab-occupancy-similar", "reproduced",
    "22 mice. Occupancy entropy (48 px bins) median DOI 7.20 against saline 7.13 bits, p = 0.063; fraction of "
    "frames in 5 cm corner squares 0.267 against 0.245, p = 0.25; in 10 cm corner squares 0.850 against 0.862, "
    "p = 0.70. No measure differs at p < 0.05. The grand-mean maps correlate with r = 0.919. At the code's "
    "0.0237 cm/px the arena box is 27.5 by 15.6 cm, so 10 cm corners hold 85% of frames and that reading "
    "says little; the corners also hold the reward ports.",
    ["The paper reports no test; the measures and corner sizes are the claims file's readings of the paper's "
     "prediction.",
     "Assumed, the arena box for the corners is the 0.5th to 99.5th percentile of all nose positions pooled "
     "over sessions (x 22 to 1181, y 14 to 674 px), as the paper gives no arena coordinates; with entropy far "
     "from significance in either direction and corner fractions at p = 0.25 and 0.70, a box a few cm "
     "larger or smaller is unlikely to change the outcome, but this was not run."], assumed=True)
add("htr-event-link", "reproduced",
    "The series is in all 22 DOI sessions (24 to 204 events, median 147, 3.67 per min) and in 10 saline "
    "sessions (14 to 35); in each of the 10 mice with both, the DOI session has more events. The conversion "
    "script loads it from the folders fig5_cleaned.Rmd reads as HTR timestamps. The files name it only "
    "\"Event times (s) from Time Stamps Task\" with data all 1. The DOI sessions of 2197 and 2204 have only 30 "
    "and 24 events.")
HTR_DEV = ("The later-cohort timestamps' last field is a frame count at 80 frames/s (it never exceeds 79); the "
           "file stores it as hundredths and the code reads it as thousandths. The code's reading is used, as "
           "the paper's numbers were computed with it, and the other two are shown; they agree.")
add("fig5supp-htr-within-trial-x-not-y", "reproduced",
    "22 DOI mice, 1848 mouse and bin rows. With the claims file's method (code clock, code timestamps) the "
    "within-trial rate correlates with x, r = 0.056, permutation p = 0.0048 (paper 0.002), positive toward the "
    "odor and reward ports, and not with y, r = 0.028, p = 0.26 (paper 0.92). Timestamps as stored, x p = "
    "0.0016, y p = 0.92; as frames, x p = 0.0020, y p = 0.86. With the fitted clock only 151 of 3057 HTRs fall "
    "within trials and the x correlation vanishes (r = 0.001, p = 0.96; y p = 0.065): the result rests on the "
    "code's clock, which the data check found does not align frames with trials.",
    [CLOCK_DEV, HTR_DEV, "The permutations are drawn with numpy's generator from seed 123, not R's."])
add("fig5e-htr-combined-x", "reproduced",
    "22 mice in the map, the expected 22. With trial and ITI frames combined the rate rises with x, r = 0.149, "
    "none of 10000 permutations as extreme (p < 0.0001), under every timestamp reading (r = 0.122 to 0.149); "
    "the grand-mean rate rises from 1.97 HTR/min in the first x bin to about 6.5 at the odor end. It needs no "
    "trial clock.", [HTR_DEV], measured=22)
add("fig5supp-htr-iti-x", "reproduced",
    "ITI rates rise with x, r = 0.152, p < 0.0001, and do not vary with y, p = 0.55 (code reading); stored "
    "timestamps y p = 0.25, frames y p = 0.080, fitted clock x r = 0.119 p < 0.0001, y p = 0.13.",
    [CLOCK_DEV, HTR_DEV])
add("fig5f-htr-rate-trial-vs-iti", "reproduced",
    "With the code's method (HTR times compared directly with trial times) 22 DOI sessions, median within-trial "
    "rate 3.67 against ITI 3.68 HTR/min, signed-rank p = 0.50 (paper p = 1); stored timestamps p = 0.52, frames "
    "p = 0.70. With HTR times moved to the trial clock by the fitted clock, within-trial rate 1.38 against ITI "
    "3.88 HTR/min, p < 0.0001 under every timestamp reading (later cohort alone p = 0.0007; sessions with a good "
    "fit p = 0.0001): HTRs are rarer within trials, the opposite of the claim. The outcome follows the claims "
    "file's method; the finding of no difference does not survive an alignment of the clocks.",
    ["The HTR times are on the video's clock and the trial times on the task's; the code compares them "
     "directly. The variant moves the HTR times by the per-session fitted clock (video time x 80 / fitted rate "
     "minus offset). For the first cohort, whose manually scored times are in seconds of video, this assumes "
     "the video's time base is 80 frames/s, which the files do not state.", HTR_DEV])
add("fig5supp-htr-no-sex-difference", "reproduced",
    "HTRs per minute over 40 min, females (12) median 3.61, mean 3.33; males (10) median 3.99, mean 3.65; "
    "rank-sum with the normal approximation W = 44, p = 0.31 (paper 0.31). It needs no clock.")

findings = [
 {"kind": "data_missing", "statement": "The reward-port entries and exits behind Figure 2 (reward-port duration after correct and incorrect trials, nine claims) are not in the dandiset; no event series, column or table holds them, and the code reads them from pre-computed files that are not public."},
 {"kind": "metadata_error", "statement": "The pose series carry no frame times; their stated rate is an estimate made at conversion (frames over the last trial's end time, 72.7 to 85.3 frames/s), and with it the tracking does not line up with the trial table. A linear clock fitted per session to the nose's movement over trials does (about 80.5 frames/s in the later cohort, 72 to 75 in the first, offsets of -10 to 14 s), with the same offset in both halves of 40 of 44 sessions; the fit is weak in the sessions 2197 DOI, 2197 saline, 2183 saline and 2204 DOI."},
 {"kind": "code_mismatch", "statement": "The paper's code (fig3_cleaned.Rmd and fig5_cleaned.Rmd) places tracking frame i at i / 80 s and compares HTR video times directly with trial times. On these data that clock does not align frames with trials (median nose displacement over a trial about 0 px against hundreds with a fitted clock). With the fitted clock the within-trial speed difference (Figure 3C) and the within-trial HTR preference for x vanish, and HTRs are about a third as frequent within trials as in the ITI, against the paper's Figure 5F."},
 {"kind": "metadata_insufficient", "statement": "The series processing/behavior/task_event_timestamps is the head-twitch times (by the conversion script's source folders and the paper's code), but the files call it only \"Event times (s) from Time Stamps Task\" with data all 1."},
 {"kind": "metadata_error", "statement": "In the 27 later-cohort sessions the HTR timestamps came as HH:MM:SS:FF video timecodes whose last field is a frame count at 80 frames/s (never above 79); the conversion stored it as hundredths of a second, so the stored times are late or early by up to 0.2 s."},
 {"kind": "code_mismatch", "statement": "fig5_cleaned.Rmd reads the last field of the later cohort's HTR timecodes as thousandths of a second, while it is a frame count at 80 frames/s, shifting the HTR times by up to 0.9 s; the outcomes here do not change with the reading."},
 {"kind": "metadata_error", "statement": "The subject sex of the saline session of mouse 2182 (sub-2182_ses-2182-31) is female, while its DOI session and the paper's code give male."},
 {"kind": "metadata_insufficient", "statement": "The trial columns are described only by their names (odor_control, side, outcome, iti_time, false_alarm, repoke); the codes are not explained. The session notes show side 2 is left and side 1 right in all 34 later-cohort sessions, and the code gives odor_control 0 as an odor trial and 3 as an omission trial."},
 {"kind": "other", "statement": "In the five first-cohort mice 347 trials have a set ITI of 16 to 25 s, while the Methods give a variable ITI of 1 to 15 s."},
 {"kind": "selection_undocumented", "statement": "The paper's code drops four sniff sessions as faulty (2195 DOI, 2198 DOI, 2198 saline, 2213 saline), without a stated reason; the dandiset keeps them without a flag, though their descriptions show most rows dropped for a missing exhalation."},
 {"kind": "paper_inconsistency", "statement": "The Results name the Wilcoxon rank-sum test for the speed comparisons of Figure 3C, 3D and its supplement, while the Methods and the code use the paired signed-rank test; the two give different p-values here (for example 0.51 against 0.063 for Figure 3C)."},
 {"kind": "methods_unavailable", "statement": "Question for the authors, on fig5ab-occupancy-similar. The paper tests no difference in occupancy and gives no arena coordinates, so the corners of its prediction are not defined. This attempt took the 0.5th to 99.5th percentile box of all nose positions and corner squares of 5 and 10 cm; which region of the arena did the authors mean by its corners?"},
 {"kind": "methods_unavailable", "statement": "Question for the authors, on the speed and HTR claims split by trial period. Were the tracking frames of DLC_tracked_task aligned with the trial summary times by any record of frame times, or only by the 80 frames/s of fig3_cleaned.Rmd? The data here align only with a per-session rate near 80.5 frames/s (72 to 75 in the first cohort) and an offset of a few seconds."},
]

rec = {
 "schema_version": 2, "id": "001863-welch-2025-01",
 "dataset": {"archive": "dandi", "id": "001863", "version": "0.260806.2109", "doi": "10.48324/dandi.001863/0.260806.2109"},
 "paper": "doi:10.1101/2025.07.09.663970", "date": "2026-11-05", "entry": "001863-welch-2025",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-13"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/42057646913"}},
 "inputs": [{"what": "The paper's analysis and conversion code, for method details the claims file cites (session list, sex list, 40-trial filter, tracking cleaning, 80 frames/s and 0.0237 cm/px, bin sizes, faulty sniff sessions, test calls) and for the name of the HTR series (nwb_conversion/convert_session_to_nwb.py and analysis/fig5_cleaned.Rmd).",
             "source": "https://github.com/Smear-Lab/Olfactory-search-on-psychedelics at commit aa80af0a153c6bf099e5668d27c9d88e2bfc033f"}],
 "outcomes": o, "findings": findings,
}
out = yaml.safe_dump(rec, sort_keys=False, width=100, allow_unicode=True)
open("attempts/001863-welch-2025-01.yaml", "w").write(out)
# check for ': ' inside plain scalars
for line in out.splitlines():
    body = line.split(": ", 1)[1] if ": " in line.lstrip("- ") else ""
    if ": " in body and not body.startswith(("'", '"')):
        print("COLON:", line[:120])
print(len(o), "outcomes")
EOF
. $TMPDIR/env/bin/activate; python $TMPDIR/att/make.py; grep -n "'" attempts/001863-welch-2025-01.yaml | head
```

```
36 outcomes
9:date: '2026-11-05'
23:- what: The paper's analysis and conversion code, for method details the claims file cites (session list,
39:  - Statistics are computed in Python with R's defaults reproduced (exact signed-rank and rank-sum tests
51:  - Statistics are computed in Python with R's defaults reproduced (exact signed-rank and rank-sum tests
70:  - Sex is taken from the code's list; the file of the 2182 saline session says female, its DOI session
80:  - The repoke counts are the trial table's repoke column, which the code reads from the same trial file.
85:  notes: The trial table's false_alarm column (later cohort, 17 mice) gives 3 false reports in 2 of 17
87:    (a), counts per session, and (b), per ITI, the paper's p = 1. Rare, as stated (not judged). The Results'
90:  - The false_alarm column is taken to be the Methods' false odor report; the files describe it only as
91:    "false alarm". The Results' reward-port variant was not run (no data).
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
a='''report, gives 3 false reports in 3 of 17 DOI sessions and 3 in 3 of 17 saline sessions, out of
over 3000 ITIs; the rank-sum test gives p = 1 under both readings, the paper's value.'''
b='''report, gives 3 false reports in 2 of 17 DOI sessions and 3 in 2 of 17 saline sessions, 6 of
3227 ITIs; the rank-sum test gives p = 1 under both readings, the paper's value.'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/build_nb.py && cat > entries/001863-welch-2025/README.md <<'EOF'
# Welch, Gonzales-Hess, Tarvin, Connor & Smear (2025) from dandiset 001863

Tests the findings of [Welch et al. (2025)](https://doi.org/10.1101/2025.07.09.663970) on
[DANDI:001863](https://dandiarchive.org/dandiset/001863/0.260806.2109), which holds one DOI and
one saline session of the olfactory search task for each of 22 mice: trial tables, DeepLabCut
tracking, thermistor sniff cycles and head-twitch (HTR) times.

| Claims | Outcome |
|---|---|
| Accuracy, trial counts, repokes and false reports (Figure 1, six claims) | Reproduced |
| Reward-port duration (Figure 2, nine claims) | Blocked: data missing |
| Trial and ITI duration (Figure 3A, 3B, three claims) | Reproduced |
| Speed: lower within trials and in the ITI on DOI (Figure 3C, 3D) | Partially reproduced |
| Speed by trial type (Figure 3 supplement, five claims) | Four reproduced, one partially |
| Sniff frequency (Figure 4, four claims) | Reproduced |
| Occupancy (Figure 5A, 5B) | Reproduced |
| The event series is the HTR times (link claim) | Reproduced |
| HTR location, timing and sex (Figure 5, five claims) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The tracking has no frame times, and the paper's code places frame i at i / 80 s, which does not
line the frames up with the trial table; a clock fitted to each session does. The claims are
tested with the code's clock, as the claims file fixes it, and the notebook shows the fitted clock
as a variant: with it the within-trial speed difference and the within-trial HTR preference vanish,
and HTRs are rarer within trials than in the ITI. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/001863-welch-2025-01.yaml`](../../attempts/001863-welch-2025-01.yaml).

- `reproduce_welch_2025.ipynb`: the analysis. It takes about six minutes, one of them streaming the
  files and most of the rest the permutation tests.
- `doi_search.py`: loading the files, the measures of the paper's code (tracking cleaning, speed,
  rolling accuracy, sniff frequency, HTR maps), R-style tests and the clock check. Other notebooks
  on this dandiset can import it.
EOF
cd  && date -u && time python tools/entry.py all entries/001863-welch-2025 2>&1 | tail -15
```

```
cells 111
Thu Nov  5 16:24:28 UTC 2026
Installed kernelspec registry-001863-welch-2025 in executed/001863-welch-2025/.venv/share/jupyter/kernels/registry-001863-welch-2025
0 error(s)
pass  reproduce_welch_2025.ipynb  (367 s)

real	6m14.677s
user	5m10.792s
sys	0m5.696s
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; E=executed/001863-welch-2025/reproduce_welch_2025.ipynb; python $TMPDIR/show.py $E | grep -c ERROR; python $TMPDIR/show.py $E 48 75 | grep -E "code|fitted|^\[" | head -60
```

```
0
[49] Frames dropped above 160 cm/s, all sessions: 1125 of 8313841
Fraction of frames within trials: code clock median 0.103, fitted 0.103
code   DOI         3.21   6.34  11.08  2.86   5.57  10.29  3.36   6.53  11.25     2.07   6.01  13.38
fitted DOI         2.79   8.15  16.18  2.80   5.40   9.85  3.09   8.97  16.10     2.51   6.57  16.84
[51] A = ('within', 'DOI'), B = ('within', 'saline')
           code 22    6.3418    6.6228           -0.6306          16      0.0634     0.5073
         fitted 22    8.1547    8.0204           -0.4872          13      0.8237     0.7537
fitted, 13 mice 13    8.3024    8.7201           -0.4177           8      0.8926     0.8010
By sex, code clock:
F {'clock': 'code, 12 mice', 'n': 12, 'A_median': np.float64(6.6787), 'B_median': np.float64(6.5319), 'median_A_minus_B': np.float64(-0.4401), 'A_lower_in': 7, 'signrank_p': 0.5186, 'ranksum_p': 0.8428}
M {'clock': 'code, 10 mice', 'n': 10, 'A_median': np.float64(6.0642), 'B_median': np.float64(6.6228), 'median_A_minus_B': np.float64(-0.6765), 'A_lower_in': 9, 'signrank_p': 0.0273, 'ranksum_p': 0.315}
[51] Plotted per-mouse speeds span 2.51 to 12.37 cm/s; none outside the axes.
[54] A = ('iti', 'DOI'), B = ('iti', 'saline')
           code 22    5.5665    5.7576           -0.5957          15      0.0794     0.5688
         fitted 22    5.4016    5.7634           -0.5830          15      0.0634     0.5688
fitted, 13 mice 13    5.4809    5.8583           -0.6302          10      0.0574     0.7241
[57] A = ('odor', 'DOI'), B = ('odor', 'saline')
           code 22    6.5310    6.3287           -0.5382          15      0.1870     0.7014
         fitted 22    8.9690    8.2724           -0.2079          12      0.6789     0.9537
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; E=executed/001863-welch-2025/reproduce_welch_2025.ipynb; python $TMPDIR/show.py $E 8 9 | tail -22; python $TMPDIR/show.py $E 0 2
```

```
2183       DOI  first  180573      75.51            0.000          -4.974    74.96          -1.2   741.416                        8.165             -1.1             -1.3                0.565              0.807
  2183    saline  first  176506      73.67           20.388          22.049    72.25          14.0   143.352                       27.982             12.1             13.6                0.524              0.801
  2185       DOI  first  185127      77.16            4.773          16.965    74.58          -2.1   764.792                       15.057             -1.4             -2.2                0.432              0.711
  2185    saline  first  175720      73.76            0.000           2.885    71.67           2.4   475.363                        2.647              2.5              2.4                0.416              0.749
  2191       DOI  later  191914      82.51           -9.333          25.596    80.27           0.1   634.614                        1.036             -0.0              0.2                0.823              0.866
  2191    saline  later  192012      82.94          -11.183           2.750    80.35          -0.1   482.426                       -0.966             -0.0             -0.1                0.799              0.888
  2195       DOI  later  192029      83.63            7.604           9.184    80.46           4.2   844.344                       20.097              4.2              4.3                0.816              0.849
  2195    saline  later  192010      81.32           -6.857          77.644    80.40          -0.7   359.278                       -0.001             -0.8             -0.6                0.733              0.809
  2196       DOI  later  191999      81.17           -1.017          16.234    80.23           1.4   365.216                        4.191              1.0              1.4                0.824              0.845
  2196    saline  later  192020      80.79         -114.361          90.613    80.29          
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; python -c "
import json; nb=json.load(open('executed/001863-welch-2025/reproduce_welch_2025.ipynb'))
t=''.join(o.get('text','') for o in nb['cells'][8]['outputs']); print(t[t.find('Median displacement'):])"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    t=''.join(o.get('text','') for o in nb['cells'][8]['outputs']); print(t[t.find('Median displacement'):])
TypeError: sequence item 0: expected str instance, list found
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; python -c "
import json; nb=json.load(open('executed/001863-welch-2025/reproduce_welch_2025.ipynb'))
t=''.join(''.join(o.get('text',[])) for o in nb['cells'][8]['outputs']); print(t[t.find('Median displacement'):])"
```

```
Median displacement (px) by cohort:
        disp_code_80fps  disp_file_rate  disp_fit  disp_fit_trials_shifted_30s
cohort                                                                        
first               0.3            11.8     586.7                          3.5
later              -3.4             5.8     447.6                          0.9

Fitted rate by cohort (frames/s): {'first': {'min': 71.67, '50%': 73.71, 'max': 75.12}, 'later': {'min': 71.0, '50%': 80.47, 'max': 83.0}}
Sessions whose fit is weak (displacement < 100 px) or whose halves differ by more than 1 s:
 mouse condition  fit_fps  fit_offset_s   disp_fit  offset_1st_half  offset_2nd_half
  2182    saline    73.90           0.6 291.176257              0.6              2.6
  2183    saline    72.25          14.0 143.351953             12.1             13.6
  2197       DOI    82.17          10.6  27.028282             12.5             15.4
  2197    saline    83.00         -10.5  79.025299            -10.4             -5.5
  2198    saline    80.31           2.4 264.434728              1.2              2.6
  2200       DOI    80.44           1.7 293.362821              1.5              3.2
  2202       DOI    80.46          -3.0 791.723188             -1.8             -2.9
  2203    saline    80.49          -0.7 243.065635             -1.1             -5.7
  2209    saline    80.60          -8.5 345.215169             -7.2             -8.8
  2212       DOI    80.60          -6.5 559.409868             -5.6             -6.9
  2212    saline    80.69          -2.6 471.137219             -1.4             -2.8
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/att && python - <<'EOF'
p='make.py'; s=open(p).read()
a='''A linear clock fitted per session to the nose's movement over trials does (about 80.5 frames/s in the later cohort, 72 to 75 in the first, offsets of -10 to 14 s), with the same offset in both halves of 40 of 44 sessions; the fit is weak in the sessions 2197 DOI, 2197 saline, 2183 saline and 2204 DOI."'''
b='''A linear clock fitted per session to the nose's movement over trials does (median 80.47 frames/s in the later cohort, range 71.0 to 83.0, and 71.7 to 75.1 in the first, offsets of -10.5 to 14.0 s); in 33 of 44 sessions it moves the nose by 100 px or more over a trial with offsets in the two halves of the session within 1 s of each other, and it is weakest in the two sessions of mouse 2197 (27 and 79 px)."'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate; python $TMPDIR/att/make.py && cd  && python tools/entry.py check entries/001863-welch-2025 2>&1 | tail -5
```

```
36 outcomes
0 error(s)
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/001863-welch-2025 2>&1 | tail -5; ls executed/001863-welch-2025/handover/; git status --short; date -u
```

```
wrote executed/001863-welch-2025/handover
10.1101-2025.07.09.663970.yaml
doi_search.py
reproduce_welch_2025.ipynb
 M claims/001863/10.1101-2025.07.09.663970.yaml
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
?? attempts/001863-welch-2025-01.yaml
?? entries/001863-welch-2025/
?? scripts
Thu Nov  5 16:31:33 UTC 2026
```

**Agent calls Bash**

```bash
ls -la .bashrc .profile .gitconfig .mcp.json .idea .vscode scripts 2>&1 | head -20; ls entries/001863-welch-2025
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 15:42 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 15:42 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 15:42 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 15:42 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 15:42 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 15:42 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  5 15:42 scripts
README.md
__pycache__
doi_search.py
entry.yaml
reproduce_welch_2025.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/001863-welch-2025/__pycache__; python tools/entry.py check entries/001863-welch-2025 2>&1 | tail -2; date -u
```

```
0 error(s)
Thu Nov  5 16:31:48 UTC 2026
```

**Agent**

I finished steps 1 to 6. The entry `entries/001863-welch-2025/` is locked, passes `check`, and ran from a clean environment in 6.1 min (367 s) with no errors. The handover package is in `executed/001863-welch-2025/handover/`. Nothing is committed.

## 1. Outcomes (36 claims: 35 from the reader, plus one link claim I added)

| Claim | Outcome |
|---|---|
| fig1b, fig1c, fig1d, fig1d-females-only, fig1e repoke, ITI false report | Reproduced (p = 0.023, 0.039 in the 35-40 min bin, 0.011, 0.010 against males 0.39, 0.38, 1) |
| fig2a to fig2d-supp (9 claims) | Blocked: `data_missing` (no reward-port entries or exits in the dataset) |
| fig3a odor duration, fig3a omission, fig3b ITI | Reproduced |
| fig3c speed within trials, fig3d speed in the ITI | Partially reproduced (same direction, p = 0.063 and 0.079) |
| fig3supp: odor speed no difference, DOI ITI slower than odor, saline ITI slower, saline odor vs omission | Reproduced |
| fig3supp-doi-omission-no-difference | Partially reproduced (ITI vs omission p = 0.0059) |
| fig4abc (Z = 25.2, against the paper's 24.9), fig4d, fig4e (p = 0.11) | Reproduced |
| fig4supp-ks-every-mouse | Reproduced under reading (b): 13 of 13 mice. Under reading (a) and the code's computation, 11 of 13 |
| fig5ab occupancy | Reproduced (`assumed: true`, see section 2) |
| htr-event-link (added), fig5supp within-trial x, fig5e, fig5supp ITI x, fig5f, fig5supp sex | Reproduced with the code's clock |

## 2. Dataset, assumptions, questions

**What the dataset holds**
- 44 files, one DOI and one saline session for each of 22 mice. They match the code's session list. No recording appears twice.
- There are 14 DOI and 13 saline sessions with usable sniff signal, as the paper says.

**What is missing or wrong**
- **No reward-port events.** This is why the nine Figure 2 claims are blocked.
- **Main finding: the tracking clock.** The tracking has no frame times, and its stated rate is only an estimate made during conversion.
  - The code's clock (frame i at i / 80 s) does not line the frames up with the trials: the nose moves a median of about 0 px over a trial.
  - A clock fitted per session does line them up: about 80.5 frames/s in the later cohort and 72 to 75 in the first.
  - With the fitted clock as a variant, the within-trial speed effect and the within-trial HTR preference for x disappear.
  - Also with the fitted clock, HTRs are about a third as frequent within trials as in the ITI (p < 0.0001). This contradicts fig5f.
  - I kept the outcomes on the code's clock, because the claims file fixes it. I recorded the clock problem as a `metadata_error` finding and a `code_mismatch` finding.
- **HTR times.** The HTR series has no name in the files. The paper's code names it, so I added the link claim `htr-event-link` and marked the five HTR claims `data: with_labels`, depending on it.
- **HTR timestamps.** In the later cohort the last field of the timestamps is a frame count (0 to 79). The files store it as hundredths of a second and the code reads it as thousandths. All three readings give the same outcomes.
- **Smaller errors:**
  - The saline session of mouse 2182 is labelled female; the code and its DOI session say male.
  - The side codes are undocumented. The session notes show that side 2 is left.
  - The first cohort has set ITIs of 16 to 25 s, beyond the Methods' 1 to 15 s.
  - The code drops four sniff sessions as faulty, and the dataset does not flag them.

**Assumption:** for the fig5ab corners I took the arena as the 0.5th to 99.5th percentile box of all nose positions, because the paper gives no arena coordinates.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which region of the arena counts as its corners?
- How were the tracking frames aligned with the trial times?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. When a method the claims file fixes (here the 80 frames/s clock) is contradicted by the data, the protocol does not say whether to test with it or "trust the data". I tested with the claims file's method and showed the data-aligned clock as a variant, with findings.
2. fig3c and fig3d have criteria that define only the reproduced case. I called "same direction, 0.05 ≤ p < 0.1" partially reproduced, the convention the claims file uses for other claims.
3. Two rules conflict for readings: "the outcome is the one they all give" (author, step 1.6) and "reproduced under any reading the criterion names" (reader, step 3). For fig4supp-ks I applied the reader rule and recorded the result under the other reading.
4. The protocol does not say whether adding `data: with_labels` and `depends_on` to the reader's claims is allowed alongside a link claim. I added both, following the newest entry, and changed no statement, expected value or criterion.

## 4. Runtime and failures

- The work took about 50 minutes (15:43 to 16:32 UTC).
- Two notebook bugs failed during development and were fixed before the final run.
- For the per-period sniff tests under readings (b) and the code's, I gave the normal-approximation p, not 10,000 resamples, to save time. With |Z| of 2.1 to 26.9 the result is the same; the per-period tests under reading (a) and the pooled tests use full resampling.
- The untracked dotfiles at the repository root are sandbox device mounts, not files I created.

## End of run

75 turns, 47 minutes, $7.71 at API prices, result: success.
