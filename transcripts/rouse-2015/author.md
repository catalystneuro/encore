# 000941 · author · run 41231374559

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/000941 paper entries | head -50
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2f4b94e9-d3d7-43e2-90e2-2709082655ac/tool-results/bpxjefwr2.txt

Preview (first 2KB):
Sat Oct 31 18:52:54 UTC 2026
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

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2f4b94e9-d3d7-43e2-90e2-2709082655ac/tool-results/bpxjefwr2.txt"
}
```

```
1	Sat Oct 31 18:52:54 UTC 2026
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
[... 669 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000941/*.yaml; ls paper; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat README.md | head -150; echo ----; cat docs/design.md | head -300
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
[... 391 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2f4b94e9-d3d7-43e2-90e2-2709082655ac/tool-results/bl4vppb4y.txt"
}
```

```
1	# Claims for Rouse & Schieber (2015), J Neurophysiol 114:3268-3282, on dandiset 000941.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).
4	#
5	# Text read. The version of record (PDF supplied by a person, text extracted with PyMuPDF),
6	# complete with Methods, Results, figure legends, Table 1 and Table 2. The paper has no
7	# supplement. Some symbols are garbled in the extracted text (the "<", ">", "~", "x" glyphs
8	# and the eta in "eta squared"); quotes are cut around them with "...". The sense of each
9	# garbled comparison was taken from the sentence around it (e.g. "Qm ratios ... 0.5, indicating
10	# larger location than object effects" is Qm > 0.5).
11	#
12	# Code read. The paper links no code and gives no code or data availability statement. Nothing
13	# below rests on code; every method detail is from the Methods, the Results or the legends.
14	#
15	# Dataset. Dandiset 000941 is titled "FALCON Benchmark M1-A: primary motor cortex recordings in
16	# primate during reach-to-grasp task" and lists this paper with three others from the same
17	# laboratory (J Neurosci 2016, J Neurophysiol 2016 on EMG, Cell Reports 2018). Whether it holds
18	# the kinematic data of this paper (marker positions or joint angles, for which monkeys and
19	# sessions) is for the author to find.
20	#
[... 676 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -120
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
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000941/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000941/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000941/versions/0.241029.1405/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['path'], a['size'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000941/versions/0.241029.1405/" | python -c "
import json,sys; d=json.load(sys.stdin); print(d.get('description')); print(json.dumps(d.get('relatedResource'),indent=1)); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls entries/001453-fouke-2025/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml | head -150; ls questions | head
```

```
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
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
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -v "^    " | head -80; grep -n "blocked" attempts/001453-fouke-2025-01.yaml | head; ls schemas;
```

```
notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:figs1e-dc-respond-less-monocular
  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
  deviations:
  - Codes 9 and 11 are assigned as the figure code has them; the stimulus software's conversion
- claim: fig1c-continuous-vs-bouts
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1c-continuous-vs-bouts
  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)
  deviations:
  - The paper shows this with representative traces and a bout analysis whose bout files are not
[... 74 more lines not kept]
```

**Agent**

Now let me open an NWB file and list everything it holds.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "import pynwb, remfile, h5py, dandi; print(pynwb.__version__)" 2>&1; which uv python; python --version
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
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py numpy pandas scipy matplotlib statsmodels 2>&1 | tail -2; python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import remfile, h5py, pynwb, requests, sys
aid=sys.argv[1]
r=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False)
url=r.headers['Location']
f=h5py.File(remfile.File(url),'r')
def walk(name,obj):
    if isinstance(obj,h5py.Dataset): print(name, obj.shape, obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
    else: print(name+'/', dict((k,v) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
f.visititems(walk)
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); n=io.read()
print(n)
print(n.subject)
t=n.trials.to_dataframe(); print(t.head(10).to_string()); print(t.describe(include='all').to_string())
EOF
python survey.py 61dbe78b-58da-4089-b308-96378c5a95b9 2>&1 | grep -v "^units/spike_times\b" | head -200
```

```
acquisition/ {}
acquisition/eval_mask/ {'comments': 'no comments', 'description': 'Timesteps to KEEP covariates (for training, eval).', 'neurodata_type': 'TimeSeries'}
acquisition/eval_mask/data (160436,) bool {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'bool'}
acquisition/eval_mask/timestamps (160436,) float64 {'interval': np.int64(1), 'unit': 'seconds'}
acquisition/preprocessed_emg/ {'neurodata_type': 'BehavioralTimeSeries'}
acquisition/preprocessed_emg/APL/ {'comments': 'columns=[APL]', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/preprocessed_emg/APL/data (160436,) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mV'}
acquisition/preprocessed_emg/APL/timestamps (160436,) float64 {'interval': np.int64(1), 'unit': 'seconds'}
acquisition/preprocessed_emg/BCPs/ {'comments': 'columns=[BCPs]', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/preprocessed_emg/BCPs/data (160436,) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mV'}
acquisition/preprocessed_emg/BCPs/timestamps (160436,) float64 {'interval': np.int64(1), 'unit': 'seconds'}
acquisition/preprocessed_emg/DLTa/ {'comments': 'columns=[DLTa]', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/preprocessed_emg/DLTa/data (160436,) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mV'}
acquisition/preprocessed_emg/DLTa/timestamps (160436,) float64 {'interval': np.int64(1), 'unit': 'seconds'}
acquisition/preprocessed_emg/DLTp/ {'comments': 'columns=[DLTp]', 'description': 'no description', 'neurodata_type': 'TimeSeries'}
acquisition/preprocessed_emg/DLTp/data (160436,) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'mV'}
acquisition/preprocess
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > trials.py <<'EOF'
import remfile, h5py, pynwb, requests, sys, pandas as pd, numpy as np
pd.set_option('display.width',250)
assets=requests.get("https://api.dandiarchive.org/api/dandisets/000941/versions/0.241029.1405/assets/?page_size=100").json()['results']
out={}
for a in sorted(assets,key=lambda a:a['path']):
    url=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=False).headers['Location']
    f=h5py.File(remfile.File(url),'r')
    n=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
    t=n.trials.to_dataframe()
    ts=n.acquisition['eval_mask'].timestamps
    print(a['path'], len(t), 'result',t.result.value_counts().to_dict(), 'numbers',t.number.min(),t.number.max(), 'units',len(n.units), 'emg_ts',ts.shape, ts[0], ts[-1], ts[1]-ts[0])
    t.to_pickle(a['path'].split('/')[-1]+'.trials.pkl')
EOF
python trials.py
```

```
sub-MonkeyL-held-in-calib/sub-MonkeyL-held-in-calib_ses-20120924_behavior+ecephys.nwb 414 result {'R': 414} numbers 127 700 units 64 emg_ts (182498,) 0.0 3649.94 0.02
sub-MonkeyL-held-in-calib/sub-MonkeyL-held-in-calib_ses-20120926_behavior+ecephys.nwb 409 result {'R': 409} numbers 127 668 units 64 emg_ts (172325,) 0.0 3446.48 0.02
sub-MonkeyL-held-in-calib/sub-MonkeyL-held-in-calib_ses-20120927_behavior+ecephys.nwb 376 result {'R': 376} numbers 127 672 units 64 emg_ts (177606,) 0.0 3552.1 0.02
sub-MonkeyL-held-in-calib/sub-MonkeyL-held-in-calib_ses-20120928_behavior+ecephys.nwb 412 result {'R': 412} numbers 127 673 units 64 emg_ts (160436,) 0.0 3208.7 0.02
sub-MonkeyL-held-in-minival/sub-MonkeyL-held-in-minival_ses-20120924_behavior+ecephys.nwb 2 result {'R': 2} numbers 232 233 units 64 emg_ts (806,) 0.0 16.1 0.02
sub-MonkeyL-held-in-minival/sub-MonkeyL-held-in-minival_ses-20120926_behavior+ecephys.nwb 2 result {'R': 2} numbers 191 192 units 64 emg_ts (652,) 0.0 13.02 0.02
sub-MonkeyL-held-in-minival/sub-MonkeyL-held-in-minival_ses-20120927_behavior+ecephys.nwb 2 result {'R': 2} numbers 127 128 units 64 emg_ts (1039,) 0.0 20.76 0.02
sub-MonkeyL-held-in-minival/sub-MonkeyL-held-in-minival_ses-20120928_behavior+ecephys.nwb 2 result {'R': 2} numbers 201 202 units 64 emg_ts (727,) 0.0 14.52 0.02
sub-MonkeyL-held-out-calib/sub-MonkeyL-held-out-calib_ses-20121004_behavior+ecephys.nwb 10 result {'R': 10} numbers 186 197 units 64 emg_ts (3442,) 0.0 68.82 0.02
sub-MonkeyL-held-out-calib/sub-MonkeyL-held-out-calib_ses-20121017_behavior+ecephys.nwb 10 result {'R': 10} numbers 115 124 units 64 emg_ts (3342,) 0.0 66.82 0.02
sub-MonkeyL-held-out-calib/sub-MonkeyL-held-out-calib_ses-20121024_behavior+ecephys.nwb 10 result {'R': 10} numbers 45 65 units 64 emg_ts (6671,) 0.0 133.4 0.02
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001209/" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['most_recent_published_version'], d['draft_version']['name'])"; curl -s "https://api.dandiarchive.org/api/dandisets/001209/versions/draft/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['path'], a['size'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -n -i -E "onset|Table 2|successful|preceded|contact|200 frames|sample|movement time|Kruskal" paper/10.1152-jn.00686.2015.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 175,215p paper/10.1152-jn.00686.2015.txt; sed -n 318,345p paper/10.1152-jn.00686.2015.txt; sed -n 515,570p paper/10.1152-jn.00686.2015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "onset of movement|movement onset was|L20120928|X20121219|sessions?\b.*monkey L|trials were" paper/10.1523-jneurosci.1716-16.2016.txt paper/10.1016-j.celrep.2018.11.057.txt paper/10.1152-jn.00008.2016.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,135p paper/10.1523-jneurosci.1716-16.2016.txt; sed -n 380,395p paper/10.1523-jneurosci.1716-16.2016.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd, numpy as np
c=pd.read_pickle('sub-MonkeyL-held-in-calib_ses-20120928_behavior+ecephys.nwb.trials.pkl')
m=pd.read_pickle('sub-MonkeyL-held-in-minival_ses-20120928_behavior+ecephys.nwb.trials.pkl')
print(m.to_string()); print(c.head(3).to_string())
print(c.groupby(['tgt_obj','tgt_loc']).size().unstack())
print(c.groupby(['tgt_obj','obj_id']).size().unstack())
mt=(c.contact_time-c.move_onset_time)*1000; print(mt.describe(), mt.quantile([.25,.5,.75]))
print(np.unique(np.round((c.move_onset_time*1000)%20,3)))
print(np.diff(c.number.values).min(), (np.diff(c.number.values)>1).sum())
print((c.gocue_time-c.start_time).describe(), (c.stop_time-c.reward_time).describe(), (c.move_onset_time-c.gocue_time).describe())
"
```

```
Sat Oct 31 18:54:46 UTC 2026
    start_time  stop_time  gocue_time  move_onset_time  contact_time  reward_time result  number  tgt_loc tgt_obj  obj_id  condition_id
id                                                                                                                                     
0         5.22       7.90        6.22             6.50          6.74         6.90      R     201     67.5  Sphere       4             6
1        11.96      14.52       12.96            13.24         13.44        13.52      R     202    112.5  Sphere       1            12
    start_time  stop_time  gocue_time  move_onset_time  contact_time  reward_time result  number  tgt_loc tgt_obj  obj_id  condition_id
id                                                                                                                                     
0         5.22       7.90        6.22             6.50          6.74         6.90      R     201     67.5  Sphere       4             6
1        11.96      14.52       12.96            13.24         13.44        13.52      R     202    112.5  Sphere       1            12
2        17.86      20.38       18.86            19.12         19.30        19.38      R     203     22.5  Sphere       3             2
tgt_loc  0.0    22.5   45.0   67.5   90.0   112.5  135.0  157.5
tgt_obj                                                        
Button      29     17     27     28     19     20     10      9
Coaxial      8     15     19     26     18     20     11     18
Sphere      10     21     20     19      9     20      9     10
obj_id    1   2   3   4
tgt_obj                
Button   59  47  20  33
Coaxial  44  26  30  35
Sphere   39  29  21  29
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd, numpy as np
c=pd.read_pickle('sub-MonkeyL-held-in-calib_ses-20120928_behavior+ecephys.nwb.trials.pkl')
n=c.number.values; s=c.start_time.values
d=np.diff(n); idx=np.where(d!=1)[0]
for i in idx: print(i, n[i], n[i+1], s[i], s[i+1])
print(n[:3], n[-3:], (np.diff(s)<0).sum())
"; sed -n 215,240p paper/10.1152-jn.00686.2015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 215,245p paper/10.1152-jn.00686.2015.txt; grep -n -i "perpendicular" paper/10.1523-jneurosci.1716-16.2016.txt | head; grep -n -i -E "perpendicular|three objects|falcon" paper/10.1016-j.celrep.2018.11.057.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd, numpy as np
c=pd.read_pickle('sub-MonkeyL-held-in-calib_ses-20120928_behavior+ecephys.nwb.trials.pkl')
print(pd.crosstab(c.obj_id,c.tgt_loc))
print(pd.crosstab([c.tgt_obj,c.obj_id],c.tgt_loc))
print(pd.crosstab(c.condition_id,[c.tgt_loc]).to_string())
print(c[['number','tgt_loc','tgt_obj','obj_id']].iloc[40:110].T.to_string())
"
```

```
tgt_loc  0.0    22.5   45.0   67.5   90.0   112.5  135.0  157.5
obj_id                                                         
1           19     16     19     20     10     20     20     18
2            0      0     18     16     19     20     10     19
3           11     21     20     19      0      0      0      0
4           17     16      9     18     17     20      0      0
tgt_loc         0.0    22.5   45.0   67.5   90.0   112.5  135.0  157.5
tgt_obj obj_id                                                        
Button  1          10     11      9     10     10      0      0      9
        2           0      0      9      9      9     10     10      0
        3          11      0      0      9      0      0      0      0
        4           8      6      9      0      0     10      0      0
Coaxial 1           0      5      9      0      0     10     11      9
        2           0      0      0      7     10      0      0      9
        3           0     10     10     10      0      0      0      0
        4           8      0      0      9      8     10      0      0
Sphere  1           9      0      1     10      0     10      9      0
        2           0      0      9      0      0     10      0     10
        3           0     11     10      0      0      0      0      0
        4           1     10      0      9      9      0      0      0
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; grep -n -i -E "Fig\. 1\.|leftmost|rightmost|bottom right|orientation" paper/10.1152-jn.00686.2015.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 258,272p paper/10.1152-jn.00686.2015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd, numpy as np, itertools
c=pd.read_pickle('sub-MonkeyL-held-in-calib_ses-20120928_behavior+ecephys.nwb.trials.pkl')
runs=[(k,len(list(g))) for k,g in itertools.groupby(c.tgt_obj)]; print(runs)
# orientation per trial = tgt_loc - offset(obj)
off={3:0,4:45,1:90,2:135}
c['orient']=c.tgt_loc-c.obj_id.map(off)
print([(k,len(list(g))) for k,g in itertools.groupby(c.orient)])
print(pd.crosstab(c.condition_id,[c.obj_id,c.tgt_loc]).max(axis=1).eq(pd.crosstab(c.condition_id,[c.obj_id,c.tgt_loc]).sum(axis=1)).all())
print(c.groupby('condition_id').apply(lambda d:(d.obj_id.unique().tolist(),d.tgt_loc.unique().tolist(),d.tgt_obj.unique().tolist())).to_string())
"
```

```
[('Sphere', 118), ('Button', 159), ('Coaxial', 135)]
[(22.5, 40), (45.0, 28), (-22.5, 30), (-90.0, 18), (-45.0, 28), (0.0, 40), (-67.5, 20), (67.5, 28), (-22.5, 26), (-90.0, 19), (22.5, 38), (-45.0, 27), (67.5, 29), (45.0, 29), (-67.5, 12)]
True
condition_id
0             ([3], [67.5], [Button, Coaxial])
1             ([3], [45.0], [Sphere, Coaxial])
2             ([3], [22.5], [Sphere, Coaxial])
3                       ([3], [0.0], [Button])
4            ([4], [112.5], [Button, Coaxial])
5             ([4], [90.0], [Sphere, Coaxial])
6             ([4], [67.5], [Sphere, Coaxial])
7                      ([4], [45.0], [Button])
8              ([4], [22.5], [Sphere, Button])
9      ([4], [0.0], [Sphere, Button, Coaxial])
10           ([1], [157.5], [Button, Coaxial])
11           ([1], [135.0], [Sphere, Coaxial])
12           ([1], [112.5], [Sphere, Coaxial])
13                     ([1], [90.0], [Button])
14             ([1], [67.5], [Sphere, Button])
15    ([1], [45.0], [Sphere, Button, Coaxial])
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat entries/001453-fouke-2025/README.md | head -30; python - <<'EOF'
import json
nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]:
    print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:600]); print('---')
for c in nb['cells'][-3:]:
    print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('---')
EOF
head -60 entries/001453-fouke-2025/omr.py
```

```
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
| DC turn less than ZF to monocular stimuli | Reproduced |
| ZF swim in bouts, DC continuously | Reproduced |
| Values from representative trials (Figure 1C, E, F) | Blocked: metadata insufficient |
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -E "def check|fail\(|error\(|problems.append|errors.append" tools/entry.py | head -60; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:5000])"
```

```
73:    def error(self, where, message: str) -> None:
74:        self.errors.append(f"{where}: {message}")
112:        report.error(path.relative_to(ROOT), problem)
121:        report.error(path.relative_to(ROOT), message)
143:def check(entry_dir: Path) -> Report:
150:        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")
155:        report.error(rel / name, "notebook is not listed in entry.yaml")
157:        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
161:            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")
165:        report.error(rel, "no requirements.in")
167:        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
174:                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")
185:            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
188:                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
195:            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
197:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
201:                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
204:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
224:                    report.error(path.relative_to(ROOT), f"claim {c['id']!r} depends on {other!r}, which is not in the file")
237:            report.error(where, f"dataset version {version!r} differs from {pinned!r} in entry.yaml")
[... 261 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['outcomes']['items']['properties'],indent=0)[1500:4000]); print(json.dumps(s['properties']['findings'],indent=0)[:2500]); print(list(s['properties']))"; sed -n 300,340p tools/entry.py
```

```
ocs/protocol.md, Author, step 1.6).",
"type": "boolean"
},
"proposed": {
"description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
"type": "object",
"additionalProperties": false,
"required": [
"outcome",
"reason"
],
"properties": {
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
]
},
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/000941-rouse-2015 && cat > entries/000941-rouse-2015/rouse.py <<'EOF'
"""Loading for dandiset 000941 (FALCON Benchmark M1-A), read against Rouse & Schieber (2015).

Rouse AG, Schieber MH (2015). Spatiotemporal distribution of location and object effects in
reach-to-grasp kinematics. J Neurophysiol 114:3268-3282, doi:10.1152/jn.00686.2015.

The dandiset holds monkey L only. Each NWB file holds a trial table (`gocue_time`,
`move_onset_time`, `contact_time`, `reward_time`, `result`, `number`, `tgt_loc`, `tgt_obj`,
`obj_id`, `condition_id`), 16 channels of preprocessed EMG at 50 Hz (`preprocessed_emg`), an
`eval_mask`, and multiunit spike times from 64 channels (`units`). It holds no marker positions
and no joint angles. Files are streamed from the archive at the pinned version; nothing is
written to disk.

Where the parameters come from:

- `PAPER_SESSION` is the session of monkey L in the paper's Table 2 (L20120928).
- `APPARATUS_ORDER` is the fixed order of the objects on the apparatus, from the Fig. 1 legend
  of the paper: "positioned in a fixed clockwise order: a perpendicular cylinder ..., a coaxial
  cylinder ..., a button ..., and a sphere", with 157.5 degrees the leftmost location and 0
  degrees the right horizontal one, so that going clockwise the location angle decreases.
  `infer_object_names` uses it to name the codes of `obj_id`, which the files do not name.
- `SAMPLE_HZ` (200 frames/s) is the paper's video frame rate (Methods, Temporal Normalization),
  used to turn a median movement time into the number of normalized samples from M to C.
- The windows and the classifier of `decode_object` (100 ms windows of mean activity, linear
  discriminant analysis, 5-fold stratified cross-validation, seed 0) belong to the clock check
  of the data, not to any claim; they are standard choices that cannot change a claim's result.
"""

from __future__ import annotations

from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
import remfile
from dandi.dandiapi import DandiAPIClient

DANDISET_ID = "000941"
DANDISET_VERSION = "0.241029.1405"
PAPER_SESSION = "20120928"
SAMPLE_HZ = 200.0

APPARATUS_ORDER = ["perpendicular cylinder", "coaxial cylinder", "button", "sphere"]  # clockwise

TRIAL_COLUMNS = ["start_time", "stop_time", "gocue_time", "move_onset_time", "contact_time",
                 "reward_time", "result", "number", "tgt_loc", "tgt_obj", "obj_id", "condition_id"]


@lru_cache(maxsize=1)
def assets() -> pd.DataFrame:
    """Every asset of the pinned version: path, size, split, session and S3 URL."""
    with DandiAPIClient() as client:
        ds = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)
        rows = []
        for a in ds.get_assets():
            name = a.path.split("/")[-1]
            rows.append({"path": a.path, "size": a.size,
                         "split": a.path.split("/")[0].replace("sub-MonkeyL-", ""),
                         "session": name.split("_ses-")[1].split("_")[0],
                         "url": a.get_content_url(follow_redirects=1, strip_query=True)})
    return pd.DataFrame(rows).sort_values(["split", "session"]).reset_index(drop=True)


def open_file(url: str) -> h5py.File:
    return h5py.File(remfile.File(url), "r")


def _text(x):
    return x.decode() if isinstance(x, bytes) else x


def read_trials(f: h5py.File) -> pd.DataFrame:
    g = f["intervals/trials"]
    t = pd.DataFrame({c: g[c][:] for c in TRIAL_COLUMNS})
    for c in ("result", "tgt_obj"):
        t[c] = t[c].map(_text)
    return t


def read_emg(f: h5py.File) -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Timestamps (s), data (samples x muscles, in the file's unit) and muscle names."""
    g = f["acquisition/preprocessed_emg"]
    names = sorted(g.keys())
    ts = g[names[0]]["timestamps"][:]
    for n in names[1:]:
        assert np.array_equal(g[n]["timestamps"][:], ts)
    data = np.column_stack([g[n]["data"][:] for n in names])
    return ts, data, names


def read_spike_times(f: h5py.File) -> list[np.ndarray]:
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    return np.split(st, idx[:-1])


def file_summary(f: h5py.File) -> dict:
    s = f["general/subject"]
    return {"identifier": _text(f["identifier"][()]),
            "session_start": _text(f["session_start_time"][()]),
            "subject_id": _text(s["subject_id"][()]),
            "acquisition": sorted(f["acquisition"].keys()),
            "processing": sorted(f["processing"].keys()),
            "analysis": sorted(f["analysis"].keys()),
            "stimulus": sorted(f["stimulus/presentation"].keys()),
            "n_units": len(f["units/id"]),
            "n_emg_samples": f["acquisition/eval_mask/timestamps"].shape[0]}


def infer_object_names(trials: pd.DataFrame) -> tuple[dict, pd.DataFrame]:
    """Name the `obj_id` codes from the apparatus order of the paper's Fig. 1 legend.

    Within a block of trials at one apparatus orientation each object sits at a fixed location,
    and the objects are 45 degrees apart. The location minus the object's offset on the apparatus
    must then be constant within a block. The offsets are found from the trials (for each pair of
    codes, the most frequent difference of location between successive trials), ordered from the
    largest angle (leftmost) to the smallest, and named in the clockwise order of the legend.
    """
    t = trials.reset_index(drop=True)
    codes = sorted(t.obj_id.unique())
    diffs = {}
    for a, b in zip(t.index[:-1], t.index[1:]):
        oa, ob = t.obj_id[a], t.obj_id[b]
        if oa != ob:
            diffs.setdefault((oa, ob), []).append(t.tgt_loc[b] - t.tgt_loc[a])
    ref = codes[0]
    offset = {ref: 0.0}
    for c in codes[1:]:
        vals = pd.Series(diffs.get((ref, c), [np.nan]))
        offset[c] = vals.mode().iloc[0]
    order = sorted(codes, key=lambda c: -offset[c])           # leftmost first = clockwise order
    names = {c: APPARATUS_ORDER[i] for i, c in enumerate(order)}
    table = pd.DataFrame({"obj_id": order, "offset_deg": [offset[c] for c in order],
                          "name": [names[c] for c in order]})
    return names, table


def window_means(ts: np.ndarray, data: np.ndarray, times: np.ndarray, start: float, stop: float) -> np.ndarray:
    """Mean of each channel over [time + start, time + stop) for each event time."""
    out = np.empty((len(times), data.shape[1]))
    for i, t0 in enumerate(times):
        sel = (ts >= t0 + start) & (ts < t0 + stop)
        out[i] = data[sel].mean(axis=0) if sel.any() else np.nan
    return out


def decode_object(X: np.ndarray, y: np.ndarray, seed: int = 0) -> float:
    """5-fold stratified cross-validated accuracy of LDA (standard choices for a data check)."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.model_selection import StratifiedKFold, cross_val_score
    ok = np.isfinite(X).all(axis=1)
    cv = StratifiedKFold(5, shuffle=True, random_state=seed)
    return float(cross_val_score(LinearDiscriminantAnalysis(), X[ok], y[ok], cv=cv).mean())


def spike_counts(spikes: list[np.ndarray], times: np.ndarray, start: float, stop: float) -> np.ndarray:
    out = np.empty((len(times), len(spikes)))
    for j, s in enumerate(spikes):
        out[:, j] = np.searchsorted(s, times + stop) - np.searchsorted(s, times + start)
    return out
EOF
cd $TMPDIR && . dev/bin/activate && uv pip install -q dandi scikit-learn 2>&1|tail -1; cd entries/000941-rouse-2015 && time python -c "
import rouse, numpy as np, pandas as pd
a=rouse.assets(); print(a[['path','size','split','session']])
row=a[(a.split=='held-in-calib')&(a.session=='20120928')].iloc[0]
f=rouse.open_file(row.url); t=rouse.read_trials(f)
print(rouse.infer_object_names(t))
ts,emg,names=rouse.read_emg(f); print(names, emg.shape, np.nanmin(emg), np.nanmax(emg))
y=t.obj_id.values
for lag in [-1.5,-1.0,-0.5,-0.3,-0.2,-0.1,0,0.1,0.3]:
    X=rouse.window_means(ts,emg,t.contact_time.values,lag,lag+0.1)
    print(lag, round(rouse.decode_object(X,y),3), round(rouse.decode_object(X,t.tgt_obj.values),3))
"
```

```
path  ...   session
0   sub-MonkeyL-held-in-calib/sub-MonkeyL-held-in-...  ...  20120924
1   sub-MonkeyL-held-in-calib/sub-MonkeyL-held-in-...  ...  20120926
2   sub-MonkeyL-held-in-calib/sub-MonkeyL-held-in-...  ...  20120927
3   sub-MonkeyL-held-in-calib/sub-MonkeyL-held-in-...  ...  20120928
4   sub-MonkeyL-held-in-minival/sub-MonkeyL-held-i...  ...  20120924
5   sub-MonkeyL-held-in-minival/sub-MonkeyL-held-i...  ...  20120926
6   sub-MonkeyL-held-in-minival/sub-MonkeyL-held-i...  ...  20120927
7   sub-MonkeyL-held-in-minival/sub-MonkeyL-held-i...  ...  20120928
8   sub-MonkeyL-held-out-calib/sub-MonkeyL-held-ou...  ...  20121004
9   sub-MonkeyL-held-out-calib/sub-MonkeyL-held-ou...  ...  20121017
10  sub-MonkeyL-held-out-calib/sub-MonkeyL-held-ou...  ...  20121024

[11 rows x 4 columns]
({np.int64(2): 'perpendicular cylinder', np.int64(1): 'coaxial cylinder', np.int64(4): 'button', np.int64(3): 'sphere'},    obj_id  offset_deg                    name
0       2        45.0  perpendicular cylinder
1       1         0.0        coaxial cylinder
2       4       -45.0                  button
3       3       -90.0                  sphere)
['APL', 'BCPs', 'DLTa', 'DLTp', 'ECRB', 'ECU', 'EDC', 'FCR', 'FCU', 'FDI', 'FDPr', 'FDPu', 'Hypoth', 'PECmaj', 'TCPlat', 'Thenar'] (160436, 16) -0.13330804528483414 3.464956369951695
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import rouse, numpy as np, pandas as pd
a=rouse.assets()
for _,r in a.iterrows():
    f=rouse.open_file(r.url); t=rouse.read_trials(f)
    n=t.number.values; i=np.where(n==127)[0]
    print(r.split, r.session, len(t), i, n[max(0,i[0]-2):i[0]+3] if len(i) else '', t.start_time.min(), t.stop_time.max())
    def walk(name,obj):
        if isinstance(obj,h5py.Dataset) and any(k in name.lower() for k in ['pos','joint','marker','kin','angle','vel']): print('  ',name)
    import h5py; f.visititems(walk)
"
```

```
held-in-calib 20120924 414 [22] [253 254 127 256 257] 8.34 3644.82
held-in-calib 20120926 409 [60] [253 254 127 256 257] 5.4 3441.1200000000003
held-in-calib 20120927 376 [ 0 93] [127 128 129] 13.3 3549.7200000000003
held-in-calib 20120928 412 [49] [253 254 127 257 258] 5.220000000000001 3203.76
held-in-minival 20120924 2 []  8.34 16.1
held-in-minival 20120926 2 []  5.4 13.040000000000001
held-in-minival 20120927 2 [0] [127 128] 13.3 20.78
held-in-minival 20120928 2 []  5.220000000000001 14.520000000000001
held-out-calib 20121004 10 []  2.7 68.84
held-out-calib 20121017 10 []  12.700000000000001 66.84
held-out-calib 20121024 10 []  3.8200000000000003 133.42000000000002
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen && cat > $TMPDIR/gen/make_nb.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
cells = []
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    cells.append(c)
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    cells.append(c)

md(r"""
# Reproducing Rouse & Schieber (2015) from dandiset 000941

**Paper.** Rouse AG, Schieber MH (2015). Spatiotemporal distribution of location and object effects
in reach-to-grasp kinematics. *J Neurophysiol* 114:3268-3282.
[doi:10.1152/jn.00686.2015](https://doi.org/10.1152/jn.00686.2015). The claims file
(`claims/000941/10.1152-jn.00686.2015.yaml`) was written from the version of record (Methods,
Results, legends, Tables 1 and 2; the paper has no supplement).

**Dandiset.** [DANDI:000941](https://dandiarchive.org/dandiset/000941/0.241029.1405), "FALCON
Benchmark M1-A", version **0.241029.1405**. The paper cites no version of the dataset (it predates
it), and this is the only published version, so it is the one pinned. The draft has the same 11
assets and was last modified a second after this version was published.

**What the dandiset holds.** Monkey L only: trial tables, 16 channels of preprocessed EMG at 50 Hz
and multiunit spike times, for four sessions (one of them the paper's session L20120928) split for
the FALCON benchmark, and three later sessions with ten trials each. It holds no marker positions
and no joint angles, the data every kinematic claim of the paper is about, and no data of monkeys X
and Y. Only the trial table can be used here.

| Claim | Tested here |
|---|---|
| table2-trial-counts | counts shown; blocked, data missing (the dataset holds a part of the session's successful trials and no failed trials) |
| table2-movement-time | tested on monkey L (X and Y are not in the dataset) |
| fig2-trial-count-coax-45 | count shown; blocked, data missing (a part of the session's trials) |
| fig2-joint-patterns, fig2-hand-opening-two-phases | blocked, data missing (no marker positions or joint angles) |
| fig4-armps-time-course, the eleven Fig. 5 to Fig. 7 claims | blocked, data missing (no joint angles) |
| fig8a-lda-location, fig8b-lda-object, fig8-hand-shape-invariant-to-location | blocked, data missing (no joint angles) |
| fig9-hand-configuration-location, fig10-forearm-trajectory-object, elbow-point-trajectory-object | blocked, data missing (no marker positions) |
""")

code(r"""
import time
import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import rouse

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 200)

started = time.time()
assets = rouse.assets()
print(f"dandiset {rouse.DANDISET_ID} version {rouse.DANDISET_VERSION}: {len(assets)} assets, "
      f"{assets['size'].sum() / 1e6:.1f} MB")
print(assets[["path", "size", "split", "session"]].to_string())

files = {(r.split, r.session): rouse.open_file(r.url) for r in assets.itertuples()}
trials = {k: rouse.read_trials(f) for k, f in files.items()}
key = ("held-in-calib", rouse.PAPER_SESSION)
t = trials[key]
print(f"\nloaded the trial tables of every file in {time.time() - started:.0f} s")
""")

md(r"""
## Data check

Each check of the metadata against the values is stated under its output.
""")

code(r"""
f = files[key]
print("Everything the file of the paper's session holds (held-in-calib, 20120928):")
def show(name, obj):
    import h5py
    if name.startswith("specifications"):
        return
    if isinstance(obj, h5py.Dataset):
        desc = obj.attrs.get("description", "")
        unit = obj.attrs.get("unit", "")
        print(f"  {name} {obj.shape} {obj.dtype}" + (f" unit={unit}" if unit else "") + (f" -- {desc}" if desc else ""))
f.visititems(show)
summary = pd.DataFrame([{"split": k[0], "session": k[1], **rouse.file_summary(fh)} for k, fh in files.items()])
print("\nPer file:")
print(summary.drop(columns=["acquisition"]).to_string())
print("\nAcquisition groups in every file:", sorted(set(map(tuple, summary.acquisition))))
""", tags=["sanity"])

md(r"""
The only data streams are `preprocessed_emg` (16 muscles, unit mV, 20 ms steps), `eval_mask` and the
spike times of 64 multiunit channels; `processing`, `analysis` and `stimulus` are empty in every
file. There are no marker positions, joint angles or any other kinematic series, so every claim of
the paper about joint angles, marker trajectories or the forearm and elbow points is blocked. Every
file's subject is monkey L (identifier and subject id per file above); the dandiset holds no data of
monkeys X and Y. Its description says data of another monkey are in dandiset 001209 (FALCON M1-B,
monkey X, a draft with no published version); the claims file does not name it, so it is not used.
""")

code(r"""
print("Trial table columns, with their descriptions in the file:")
g = f["intervals/trials"]
for c in rouse.TRIAL_COLUMNS:
    print(f"  {c}: {g[c].attrs.get('description', '')}")

rows = []
for k, tt in trials.items():
    n = tt.number.to_numpy()
    rows.append({"split": k[0], "session": k[1], "trials": len(tt),
                 "results": dict(tt.result.value_counts()),
                 "number_min": n.min(), "number_max": n.max(),
                 "first_start_s": tt.start_time.min(), "last_stop_s": tt.stop_time.max()})
counts = pd.DataFrame(rows)
print("\nTrials per file:")
print(counts.to_string())

print("\nWhere trial number 127 sits in each file (neighbours in file order):")
for k, tt in trials.items():
    n = tt.number.to_numpy()
    for i in np.where(n == 127)[0]:
        print(f"  {k}: row {i}, numbers {n[max(0, i - 2):i + 3].tolist()}")
""", tags=["sanity"])

md(r"""
Every trial in every file has result `R` (rewarded): the files hold no failed trials, although the
column's description says it holds success, failure or abort. In the paper's session (held-in-calib,
20120928) the 412 trials carry numbers from 201 to 673, apart from one numbered 127, and span about
3,200 s. The paper's Table 2 gives this session 768 trials, 717 of them successful, over 1:26:11
(5,171 s). The trial with number 127 sits between 254 and 257 in the same session (and between 254
and 256 in two others), in time order, so its number is very likely 255 or 256, stored wrong; the
number 127 is the largest value of a signed 8-bit integer. Session 20120927 also has a true trial
127 at its start, so in that file the number does not identify a trial.
""")

code(r"""
print("Session 20120928, held-in-calib: numbers in file order, gaps between successive numbers")
n = t.number.to_numpy()
n_fixed = n.copy()
n_fixed[(n == 127) & (np.arange(len(n)) > 0)] = -1
order_ok = np.all(np.diff(t.start_time.to_numpy()) > 0)
print("start times increase through the file:", order_ok)
valid = n_fixed[n_fixed > 0]
span = valid.max() - valid.min() + 1
print(f"numbers {valid.min()} to {valid.max()}: {span} numbers, {len(valid)} present besides the one numbered 127, "
      f"{span - len(valid) - 1} absent (counting 127 as one of 255 or 256)")
gaps = np.diff(valid)
print("absent numbers per gap:", pd.Series(gaps[gaps > 1] - 1).value_counts().sort_index().to_dict())

print("\nEvent times (s), session 20120928:")
ev = ["start_time", "gocue_time", "move_onset_time", "contact_time", "reward_time", "stop_time"]
print(t[ev].describe().round(3).to_string())
print("\nAll event times on a 20 ms grid:",
      bool(np.all(np.abs(np.round(t[ev].to_numpy() / 0.02) - t[ev].to_numpy() / 0.02) < 1e-6)))
d = pd.DataFrame({
    "cue minus start": t.gocue_time - t.start_time,
    "onset minus cue": t.move_onset_time - t.gocue_time,
    "contact minus onset": t.contact_time - t.move_onset_time,
    "reward minus contact": t.reward_time - t.contact_time,
    "stop minus reward": t.stop_time - t.reward_time})
print("\nIntervals between events (s):")
print(d.describe().round(3).to_string())
""", tags=["sanity"])

md(r"""
All event times lie on a 20 ms grid, the step of the EMG, so each is known only to 20 ms; the paper
times movement from 200 Hz video (5 ms) and contact from strain gauges sampled at 1 kHz. Each trial
starts exactly 1 s before the go cue and stops exactly 1 s after the reward, so `start_time` and
`stop_time` are a window cut around the events, not the trial's own start and stop. The reward comes
0.04 to 0.3 s after contact here, where the paper requires a 1,000 ms hold of the object before
reward; `reward_time` therefore cannot be the paper's reward, and its definition is not given.
The events are in the expected order in every trial (all intervals positive).
""")

code(r"""
print("Objects: tgt_obj against obj_id, session 20120928")
print(pd.crosstab(t.tgt_obj, t.obj_id).to_string())
print("\nRuns of tgt_obj in file order:", [(k, len(list(g))) for k, g in itertools.groupby(t.tgt_obj)])

names, offsets = rouse.infer_object_names(t)
print("\nOffsets of each obj_id on the apparatus (most frequent difference of location from obj_id",
      offsets.obj_id.iloc[1], "between successive trials), and the names they imply:")
print(offsets.to_string(index=False))
t["object"] = t.obj_id.map(names)
t["orientation"] = t.tgt_loc - t.obj_id.map(dict(zip(offsets.obj_id, offsets.offset_deg)))
runs = [(k, len(list(g))) for k, g in itertools.groupby(t.orientation)]
print(f"\nApparatus orientation implied per trial (location minus offset): {len(runs)} runs in file order:")
print(runs)

print("\nTrials per object and location (columns: degrees; 157.5 is the leftmost location, 0 the rightmost):")
print(pd.crosstab(t.object, t.tgt_loc).to_string())
print("\ncondition_id is one to one with (obj_id, tgt_loc):",
      bool((t.groupby("condition_id")[["obj_id", "tgt_loc"]].nunique() == 1).all().all()
           and t.groupby(["obj_id", "tgt_loc"]).condition_id.nunique().eq(1).all()))
""", tags=["sanity"])

md(r"""
`tgt_obj` ("object to grasp at target") takes three values (Sphere, Button, Coaxial) in three long
runs of 118, 159 and 135 trials, and each value occurs with all four `obj_id` codes and with every
location. It cannot be the object grasped: the paper's monkeys grasped four objects, presented in
blocks at each apparatus orientation. `obj_id` ("integer id for each object") has four codes, and
within each run of trials the location minus a fixed offset per code is constant, with offsets 45
degrees apart, as the paper's apparatus has them; the orientations implied fall in 15 runs of 12 to
40 trials, consistent with the paper's blocks at one apparatus orientation. Named in the clockwise
order of the Fig. 1 legend (perpendicular cylinder, coaxial cylinder, button, sphere, with 157.5
degrees leftmost), the codes are 2, 1, 4 and 3. The names agree with every constraint the legend
states: the coaxial cylinder is at all eight locations (the legend's frames show it at eight), the
sphere and button are never at the leftmost locations, and the perpendicular cylinder is not at the
rightmost ones; 4 + 6 + 6 + 8 = 24 combinations, as in the paper. The names are inferred from the
paper's legend and the structure of the trials; the files do not name the codes. `condition_id`
is one to one with object and location. The EMG check below supports `obj_id` as the grasped object.
""")

code(r"""
print("Recordings deposited more than once: held-in-minival against held-in-calib, per session")
for s in sorted({k[1] for k in trials if k[0] == "held-in-minival"}):
    mv, ca = trials[("held-in-minival", s)], trials[("held-in-calib", s)]
    same = ca.merge(mv, on=["number", "start_time"], suffixes=("_c", "_m"))
    cols_equal = all(np.allclose(same[c + "_c"], same[c + "_m"]) for c in ["gocue_time", "move_onset_time", "contact_time", "obj_id", "tgt_loc"])
    ts_m, emg_m, _ = rouse.read_emg(files[("held-in-minival", s)])
    gc = files[("held-in-calib", s)]["acquisition/preprocessed_emg"]
    names_m = sorted(gc.keys())
    emg_c = np.column_stack([gc[nm]["data"][:len(ts_m)] for nm in names_m])
    ts_c = gc[names_m[0]]["timestamps"][:len(ts_m)]
    st_m = rouse.read_spike_times(files[("held-in-minival", s)])
    st_c = rouse.read_spike_times(files[("held-in-calib", s)])
    lim = ts_m[-1]
    spikes_same = all(np.array_equal(a, b[b <= lim]) for a, b in zip(st_m, st_c))
    print(f"  {s}: minival trials {mv.number.tolist()} found in calib: {len(same)}; event times equal: {cols_equal}; "
          f"EMG over the first {len(ts_m)} samples equal: {np.array_equal(ts_m, ts_c) and np.allclose(emg_m, emg_c, equal_nan=True)}; "
          f"spike times up to {lim:.1f} s equal: {spikes_same}")
print("\nSessions in held-out-calib:", sorted(k[1] for k in trials if k[0] == "held-out-calib"),
      "(none is the paper's session)")
""", tags=["sanity"])

md(r"""
Each `held-in-minival` file repeats the first two trials of the `held-in-calib` file of the same
session, with the same event times, EMG and spike times: the same recording deposited twice. As
the dataset's description says, minival is a subset of calib. Only the `held-in-calib` file of
20120928 is used below, and each trial is counted once.
""")

code(r"""
ts, emg, muscles = rouse.read_emg(f)
spikes = rouse.read_spike_times(f)
print(f"EMG: {emg.shape[1]} muscles {muscles}, {emg.shape[0]} samples, step {np.median(np.diff(ts)) * 1000:.0f} ms, "
      f"{ts[0]:.2f} to {ts[-1]:.2f} s, values {np.nanmin(emg):.3f} to {np.nanmax(emg):.3f} (unit mV in the file), "
      f"NaN fraction {np.isnan(emg).mean():.4f}")
n_sp = np.array([len(s) for s in spikes])
print(f"Spikes: {len(spikes)} channels, {n_sp.sum()} spikes, per channel {n_sp.min()} to {n_sp.max()}, "
      f"times {min(s.min() for s in spikes if len(s)):.2f} to {max(s.max() for s in spikes if len(s)):.2f} s")

# Clock check: decode the grasped object (obj_id) from activity in 100 ms windows at lags from contact.
# With a shared clock, accuracy should be near chance well before the cue and high around contact.
# Labels from the next trial (shifted by one trial) are the control.
y = t.obj_id.to_numpy()
y_shift = np.roll(y, -1)
rows = []
for lag in np.round(np.arange(-1.6, 0.61, 0.1), 2):
    Xe = rouse.window_means(ts, emg, t.contact_time.to_numpy(), lag, lag + 0.1)
    Xs = rouse.spike_counts(spikes, t.contact_time.to_numpy(), lag, lag + 0.1)
    rows.append({"lag_from_contact_s": lag,
                 "emg_obj_id": rouse.decode_object(Xe, y), "emg_obj_id_next_trial": rouse.decode_object(Xe, y_shift),
                 "emg_tgt_obj": rouse.decode_object(Xe, t.tgt_obj.to_numpy()),
                 "spikes_obj_id": rouse.decode_object(Xs, y)})
clock = pd.DataFrame(rows)
chance = t.obj_id.value_counts(normalize=True).max()
print(f"\nCross-validated accuracy of decoding (chance as the largest class: obj_id {chance:.3f}, "
      f"tgt_obj {t.tgt_obj.value_counts(normalize=True).max():.3f}); median cue to contact "
      f"{(t.contact_time - t.gocue_time).median():.2f} s:")
print(clock.round(3).to_string(index=False))
""", tags=["sanity"])

code(r"""
fig, ax = plt.subplots(figsize=(7, 3.5))
for c, lab in [("emg_obj_id", "EMG, obj_id"), ("spikes_obj_id", "spikes, obj_id"),
               ("emg_obj_id_next_trial", "EMG, next trial's obj_id"), ("emg_tgt_obj", "EMG, tgt_obj")]:
    ax.plot(clock.lag_from_contact_s + 0.05, clock[c], marker="o", ms=3, label=lab)
ax.axhline(chance, color="grey", ls=":", lw=1)
ax.axvline(0, color="k", lw=0.5)
ax.axvline(-(t.contact_time - t.gocue_time).median(), color="k", lw=0.5, ls="--")
ax.set_xlabel("window centre from contact (s); dashed: median cue")
ax.set_ylabel("decoding accuracy")
ax.set_ylim(0, 1.02)
ax.legend(fontsize=7)
print("All plotted values lie within the axes:", float(clock.iloc[:, 1:].min().min()), "to", float(clock.iloc[:, 1:].max().max()))
""", tags=["sanity"])

md(r"""
The EMG and the spikes share the clock of the trial table: the object (`obj_id`) is decoded near
chance from EMG at lags of a second or more before contact, before the median go cue, rises from
about 0.5 s before contact (the median onset is about 0.2 s before contact) and is decoded almost
perfectly around contact, while the next trial's object is not. `tgt_obj` is decoded no better
around contact than a second before it, so it does not label what the hand did; this agrees with
reading `obj_id` as the grasped object. Only the trial table enters the claims below; the event
times themselves (onset and contact) could not be checked against kinematics, as the dataset has
none. The movement onset and contact times are consistent with the EMG (the object is decoded from
EMG in the window just before contact), which is consistent with, but does not show, the paper's
definitions.
""")

md(r"""
## table2-trial-counts

> In the three sessions the monkeys performed 768, 824 and 745 trials (L, X, Y), of which 717, 788
> and 688 were successful and 685, 752 and 637 were analyzed.

Criterion: counts per session from the trial records; analyzed trials are successful trials not
preceded by an error trial. Monkeys X and Y are not in the dataset. For monkey L the counts are
taken from the `held-in-calib` file of session 20120928 (the minival file repeats two of its trials).
""")

code(r"""
n_success = int((t.result == "R").sum())
n_fail = int((t.result != "R").sum())
print(f"Session 20120928: {len(t)} trials in the file, {n_success} rewarded, {n_fail} failed or aborted")
print(f"Paper (Table 2): 768 total (tolerance 691 to 845), 717 successful (645 to 789), 685 analyzed (617 to 754)")
print(f"File spans {t.start_time.min():.0f} to {t.stop_time.max():.0f} s ({(t.stop_time.max() - t.start_time.min()) / 60:.1f} min); "
      f"paper: session of 1:26:11 ({5171 / 60:.1f} min)")
print(f"Trial numbers {valid.min()} to {valid.max()}; numbers below {valid.min()} and above {valid.max()} are absent; "
      f"{span - len(valid) - 1} numbers inside the span are absent")
prev_present = np.isin(n_fixed - 1, n_fixed[n_fixed > 0]) & (n_fixed > 0)
print(f"Variant, if every absent number inside the span were an error trial: "
      f"total in the span {span}, successful {n_success}, successful with the preceding number present {int(prev_present.sum())}")
""", tags=["claim:table2-trial-counts"])

md(r"""
**Result: blocked, data missing.** The file of session L20120928 holds 412 rewarded trials and no
failed ones, numbered 201 to 673 and spanning about 53 of the session's 86 minutes, against 768
trials and 717 successes in the paper. The dataset holds only the part of the session released for
the FALCON benchmark's calibration split, so none of the nine counts can be taken from it, and X and
Y are not in it. The difference comes from the selection, not from the paper.
""")

md(r"""
## table2-movement-time

> The median duration from movement onset to contact differs among the monkeys (255, 235 and 335 ms
> for L, X and Y; Kruskal-Wallis P < 0.001), giving 52, 48 and 68 normalized samples from M to C.

Criterion: movement time from onset to contact over the analyzed trials (a) or all successful
trials (b); the claims file says that onset times given by the dataset are used. The dataset gives
`move_onset_time` and `contact_time`, so the marker-speed onset is not recomputed (and could not be:
there are no markers). The number of samples from M to C, inclusive of both, at 200 Hz is
median / 5 ms + 1 (Results, paragraph 1: "inclusive of the first sample at movement onset and the
last sample at peripheral object contact"; 255 ms gives 52). Only monkey L is in the dataset.
Reading (b) uses the 412 successful trials in the file; reading (a) cannot be formed exactly, as the
error trials are absent, and is approximated by the trials whose preceding trial number is present.
""")

code(r"""
mt = (t.contact_time - t.move_onset_time) * 1000
readings = {"(b) successful trials in the file": mt,
            "(a) approx.: preceding number present": mt[prev_present]}
rows = []
for name, v in readings.items():
    q = v.quantile([0.25, 0.5, 0.75])
    rows.append({"reading": name, "n": len(v), "median_ms": q[0.5], "q25_ms": q[0.25], "q75_ms": q[0.75],
                 "samples_M_to_C": q[0.5] / (1000 / rouse.SAMPLE_HZ) + 1,
                 "median_within_229.5_280.5": 229.5 <= q[0.5] <= 280.5})
res = pd.DataFrame(rows)
print("Monkey L, session 20120928. Paper: median 255 ms (225, 295), 52 samples; tolerance 229.5 to 280.5 ms, 46.8 to 57.2 samples")
print(res.round(1).to_string(index=False))
print(f"\nMovement times range {mt.min():.0f} to {mt.max():.0f} ms; 20 ms steps, so each value is known to +-20 ms")
print("Fraction of trials with movement time >= 255 ms:", round(float((mt >= 255).mean()), 3))

print("\nMedian movement time by object (names inferred above) and by location, ms:")
print(t.assign(mt=mt).groupby("object").mt.agg(["median", "size"]).to_string())
print(t.assign(mt=mt).groupby("tgt_loc").mt.median().to_string())
half = t.start_time < t.start_time.median()
print(f"\nFirst half of the file: median {mt[half].median():.0f} ms; second half: {mt[~half].median():.0f} ms")

other = {s: ((trials[('held-in-calib', s)].contact_time - trials[('held-in-calib', s)].move_onset_time) * 1000).median()
         for s in sorted(k[1] for k in trials if k[0] == "held-in-calib")}
print("For reference, median movement time in the other monkey L sessions of the dataset (ms):", other)
print("\nKruskal-Wallis across monkeys: not run; monkeys X and Y are not in the dataset.")
""", tags=["claim:table2-movement-time"])

code(r"""
fig, ax = plt.subplots(figsize=(6, 3))
bins = np.arange(90, 760, 20)
ax.hist(mt, bins=bins, color="0.5")
ax.axvline(mt.median(), color="C0", label=f"median here {mt.median():.0f} ms")
ax.axvspan(229.5, 280.5, color="C1", alpha=0.25, label="paper 255 ms, tolerance")
ax.set_xlabel("contact minus move onset (ms)")
ax.set_ylabel("trials")
ax.legend(fontsize=7)
print(f"Plotted range {mt.min():.0f} to {mt.max():.0f} ms, all within the axes")
""", tags=["claim:table2-movement-time"])

md(r"""
**Result: not reproduced.** The median time from the dataset's movement onset to contact in session
L20120928 is 200 ms (quartiles 160 and 240 ms) over the 412 successful trials in the file, and
200 ms over the 347 trials whose preceding trial is present. The paper's 255 ms (225, 295) lies
outside the tolerance of 229.5 to 280.5 ms, and the implied 41 samples from M to C are outside 47
to 57. The 20 ms steps of the event times cannot account for a 55 ms difference of the median. The
dataset does not describe how `move_onset_time` was found; a different definition of onset than the
paper's marker-speed threshold would explain the difference, and the trials in the file are a part
of the session's. The comparison among monkeys and its Kruskal-Wallis test cannot be made, as X and
Y are not in the dataset.
""")

md(r"""
## fig2-trial-count-coax-45

> Monkey L successfully reached to, grasped and manipulated the coaxial cylinder at the 45 degree
> location in 28 trials of its session.

Criterion: analyzed (a) or all successful (b) trials of session L20120928 with that object and
location. The object is named from `obj_id` as in the data check (the files' `tgt_obj` is not the
object).
""")

code(r"""
sel = (t.object == "coaxial cylinder") & (t.tgt_loc == 45.0)
print(f"Coaxial cylinder (obj_id {[k for k, v in names.items() if v == 'coaxial cylinder'][0]}) at 45 degrees: "
      f"(b) {int(sel.sum())} successful trials in the file, (a) approx. {int((sel & prev_present).sum())} with the preceding number present")
print("Paper: 28 (tolerance 25.2 to 30.8)")
print("With the file's tgt_obj == 'Coaxial' at 45 degrees:", int(((t.tgt_obj == "Coaxial") & (t.tgt_loc == 45.0)).sum()))
print(f"Successful trials of the session in the file: {len(t)} of the paper's 717 ({len(t) / 717:.2f}); "
      f"28 x {len(t) / 717:.2f} = {28 * len(t) / 717:.1f}")
""", tags=["claim:fig2-trial-count-coax-45"])

md(r"""
**Result: blocked, data missing.** The file holds 19 successful trials of the coaxial cylinder at 45
degrees (17 with the preceding trial present), against 28 in the paper; it holds 412 of the 717
successful trials of the session (57%), and 57% of 28 is 16. The count cannot be taken from a part
of the session.
""")

md(r"""
## Claims blocked for missing kinematic data

The other 23 claims (fig2-joint-patterns, fig2-hand-opening-two-phases, fig4-armps-time-course,
fig5-location-proximal-object-distal, fig5-early-significance-concurrent, fig5-shoulderier-location,
fig5-shoulder-object-effects, fig5-elbowflex-object, fig5-wrist-comparable,
fig5-hand-object-predominates, fig5-location-early-object-late, fig5-interaction-small,
fig6a-qm-30-90, fig6b-qx-small, fig7-mean-eta-30, fig7-mean-eta-90, fig7-time-course,
fig8a-lda-location, fig8b-lda-object, fig8-hand-shape-invariant-to-location,
fig9-hand-configuration-location, fig10-forearm-trajectory-object,
elbow-point-trajectory-object) are all tests on the 22 joint angles or on marker positions, in
three monkeys. The data check shows that no file holds a marker position, a joint angle or any
other kinematic series, and that only monkey L is in the dataset. They are blocked, data missing.
""")

code(r"""
import h5py
kin = []
for k, fh in files.items():
    def look(name, obj):
        if isinstance(obj, h5py.Dataset) and not name.startswith("specifications"):
            if name.split("/")[0] in ("acquisition", "processing", "analysis", "stimulus"):
                kin.append((k, name))
    fh.visititems(look)
streams = sorted({n.split("/")[0] + "/" + n.split("/")[1] for _, n in kin})
print("Data series outside the trial table and units, over all 11 files:", streams)
print(f"Done in {time.time() - started:.0f} s")
""", tags=["sanity"])

md(r"""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| table2-trial-counts | blocked: data missing |
| table2-movement-time | not reproduced (monkey L only) |
| fig2-trial-count-coax-45 | blocked: data missing |
| the other 23 claims (joint angles and marker positions) | blocked: data missing |

**How the analysis differs from the paper's.** Movement onset and contact are the dataset's own
event times, at 20 ms resolution, not the paper's onset from marker speed (5 ms steps) and contact
from strain gauges (1 kHz). Only monkey L is in the dataset, and only 412 of the 717 successful
trials of its session. The objects are named from `obj_id` by the apparatus order of the paper's
Fig. 1 legend.

**What was found about the dataset.** It holds trial tables, EMG and multiunit spikes of monkey L,
and no kinematics, so it cannot support the paper it names first. The session L20120928 is there
only in part (trials 201 to 673, about 53 of 86 minutes, no failed trials). `tgt_obj` does not name
the grasped object; `obj_id` does, without names. Trial number 255 or 256 is stored as 127 in each
of the four calibration files. The minival files repeat the first two trials of the calibration
files. `move_onset_time`, `contact_time` and `reward_time` are not defined, and the reward comes
0.04 to 0.3 s after contact, where the paper's task requires a 1 s hold.
""")

nb["cells"] = cells
nb["metadata"] = {"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
                  "language_info": {"name": "python"}}
nbf.write(nb, "entries/000941-rouse-2015/reproduce_rouse_2015.ipynb")
PYEOF
. $TMPDIR/dev/bin/activate && uv pip install -q nbformat nbclient ipykernel 2>&1|tail -1; python $TMPDIR/gen/make_nb.py && cd entries/000941-rouse-2015 && time jupyter nbconvert --to notebook --execute reproduce_rouse_2015.ipynb --output $TMPDIR/out.ipynb 2>&1 | tail -3
```

```
trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.090s
user	0m0.076s
sys	0m0.017s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cd entries/000941-rouse-2015 && cat > $TMPDIR/run.py <<'EOF'
import nbformat, sys
from nbclient import NotebookClient
nb=nbformat.read(sys.argv[1],4)
NotebookClient(nb,timeout=1200,kernel_name='python3',resources={'metadata':{'path':'.'}}).execute()
nbformat.write(nb,sys.argv[2])
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.outputs:
            if o.output_type=='stream': print(o.text)
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
time python $TMPDIR/run.py reproduce_rouse_2015.ipynb $TMPDIR/out.ipynb 2>&1 | tail -250
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
Traceback (most recent call last):
  File "/tmp/claude-1001/run.py", line 4, in <module>
    NotebookClient(nb,timeout=1200,kernel_name='python3',resources={'metadata':{'path':'.'}}).execute()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/asyncio/base_events.py", line 726, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
        cell, index, execution_count=self.code_cells_executed + 1
    )
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cd entries/000941-rouse-2015 && sed -i 's/n = t.number.to_numpy()\\nn_fixed/X/' $TMPDIR/gen/make_nb.py && python - <<'EOF'
p='/tmp/claude-1001/gen/make_nb.py'
s=open(p).read()
s=s.replace('n = t.number.to_numpy()\nn_fixed = n.copy()','n = t.number.to_numpy().astype(int)\nn_fixed = n.copy()')
open(p,'w').write(s)
EOF
python $TMPDIR/gen/make_nb.py && time python $TMPDIR/run.py reproduce_rouse_2015.ipynb $TMPDIR/out.ipynb 2>&1 | grep -v WARNING | tail -250
```

```
acquisition/preprocessed_emg/TCPlat/data (160436,) float64 unit=mV
  acquisition/preprocessed_emg/TCPlat/timestamps (160436,) float64 unit=seconds
  acquisition/preprocessed_emg/Thenar/data (160436,) float64 unit=mV
  acquisition/preprocessed_emg/Thenar/timestamps (160436,) float64 unit=seconds
  file_create_date (1,) object
  general/experiment_description () object
  general/experimenter (1,) object
  general/extracellular_ephys/electrodes/filtering (64,) object -- description of hardware filtering, including the filter name and frequency cutoffs
  general/extracellular_ephys/electrodes/group (64,) object -- a reference to the ElectrodeGroup this electrode is a part of
  general/extracellular_ephys/electrodes/group_name (64,) object -- the name of the ElectrodeGroup this electrode is a part of
  general/extracellular_ephys/electrodes/id (64,) int64
  general/extracellular_ephys/electrodes/imp (64,) float64 -- the impedance of the electrode, in ohms
  general/extracellular_ephys/electrodes/location (64,) object -- the location of channel within the subject e.g. brain region
  general/extracellular_ephys/electrodes/x (64,) float64 -- the x coordinate of the position (+x is posterior)
  general/extracellular_ephys/electrodes/y (64,) float64 -- the y coordinate of the position (+y is inferior)
  general/extracellular_ephys/electrodes/z (64,) float64 -- the z coordinate of the position (+z is right)
  general/institution () object
  general/lab () object
  general/subject/age () object
  general/subject/sex () object
[... 234 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cd entries/000941-rouse-2015 && python -c "
import rouse, numpy as np
a=rouse.assets()
u=lambda sp,s: a[(a.split==sp)&(a.session==s)].url.iloc[0]
fm=rouse.open_file(u('held-in-minival','20120928')); fc=rouse.open_file(u('held-in-calib','20120928'))
tm,em,_=rouse.read_emg(fm); tc,ec,_=rouse.read_emg(fc)
n=len(tm); print(np.array_equal(tm,tc[:n]))
d=em-ec[:n]; print(np.abs(d).max(), np.corrcoef(em.ravel(),ec[:n].ravel())[0,1], em.mean(0)[:4], ec[:n].mean(0)[:4], ec.mean(0)[:4])
r=em/ec[:n]; print(np.nanmedian(r,0))
sm=rouse.read_spike_times(fm); sc=rouse.read_spike_times(fc)
for i in range(3):
    a_=sm[i]; b=sc[i][sc[i]<=tm[-1]]; print(len(a_),len(b), a_[:3], b[:3], sm[i].max())
"
```

```
True
0.44956744236501367 0.9998788707329117 [0.19899776 0.16380518 0.32088692 0.07933582] [0.19795284 0.16308124 0.31950971 0.07903435] [0.1939784  0.17282017 0.32731263 0.07859308]
[1.00466158 1.00466158 1.00466158 1.00466158 1.00466158 1.00466158
 1.00466158 1.00466158 1.00466158 1.00466158 1.00466158 1.0067582
 1.00466158 1.00466158 1.00466158 1.00466265]
14 14 [1.1535 1.3045 1.6804] [1.1535 1.3045 1.6804] 13.3725
404 404 [0.1235 0.1947 0.554 ] [0.1235 0.1947 0.554 ] 14.5009
17 17 [1.2197 1.3504 1.4335] [1.2197 1.3504 1.4335] 13.9896
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
p='/tmp/claude-1001/gen/make_nb.py'
s=open(p).read()
old=s[s.index('    st_m = rouse.read_spike_times'):s.index('print("\\nSessions in held-out-calib:"')]
new='''    st_m = rouse.read_spike_times(files[("held-in-minival", s)])
    st_c = rouse.read_spike_times(files[("held-in-calib", s)])
    n_same = sum(np.array_equal(a, b[b <= (a.max() if len(a) else -1)]) for a, b in zip(st_m, st_c))
    ratio = emg_m / emg_c
    r = np.corrcoef(emg_m.ravel(), emg_c.ravel())[0, 1]
    print(f"  {s}: minival trials {mv.number.tolist()} found in calib: {len(same)}; event times equal: {cols_equal}; "
          f"EMG timestamps equal: {np.array_equal(ts_m, ts_c)}, values identical: {np.array_equal(emg_m, emg_c)}, "
          f"correlation {r:.5f}, median ratio minival/calib per muscle {np.nanmin(np.nanmedian(ratio, 0)):.4f} to "
          f"{np.nanmax(np.nanmedian(ratio, 0)):.4f}; channels with identical spike times: {n_same} of {len(st_m)}")
'''
s=s.replace(old,new)
s=s.replace('''Each `held-in-minival` file repeats the first two trials of the `held-in-calib` file of the same
session, with the same event times, EMG and spike times: the same recording deposited twice. As
the dataset's description says, minival is a subset of calib.''','''Each `held-in-minival` file repeats the first two trials of the `held-in-calib` file of the same
session, with the same event times and the same EMG timestamps; the spike times and EMG agree as
printed above (the EMG of the two files differs by a near-constant scale factor, so each file's EMG
was normalized on its own). They are the same recording deposited twice, as the dataset's
description says (minival is a subset of calib).''')
s=s.replace('''The reward comes
0.04 to 0.3 s after contact here, where the paper requires a 1,000 ms hold of the object before
reward; `reward_time` therefore cannot be the paper's reward, and its definition is not given.''','''The reward time
comes 0 to 0.92 s after contact (median 0.10 s), where the paper's task requires a 1,000 ms hold of
the manipulated object before the water reward; `reward_time` therefore cannot be the time of the
paper's reward, and the file does not define it.''')
s=s.replace('''and the reward comes
0.04 to 0.3 s after contact, where the paper's task requires a 1 s hold.''','''and `reward_time` comes a median 0.10 s after contact, where the paper's task requires a 1 s hold
before the reward.''')
s=s.replace('200 ms over the 347 trials whose preceding trial is present','200 ms over the 387 trials whose preceding trial number is present')
s=s.replace('degrees (17 with the preceding trial present)','degrees (16 with the preceding trial number present)')
open(p,'w').write(s)
EOF
cd entries/000941-rouse-2015 && python $TMPDIR/gen/make_nb.py && python $TMPDIR/run.py reproduce_rouse_2015.ipynb $TMPDIR/out.ipynb 2>&1 | grep -A8 "deposited more"; date -u
```

```
Recordings deposited more than once: held-in-minival against held-in-calib, per session

  20120924: minival trials [232, 233] found in calib: 2; event times equal: True; EMG timestamps equal: True, values identical: False, correlation 0.99982, median ratio minival/calib per muscle 1.0063 to 1.0156; channels with identical spike times: 64 of 64

  20120926: minival trials [191, 192] found in calib: 2; event times equal: True; EMG timestamps equal: True, values identical: False, correlation 0.99998, median ratio minival/calib per muscle 0.9600 to 0.9605; channels with identical spike times: 64 of 64

  20120927: minival trials [127, 128] found in calib: 2; event times equal: True; EMG timestamps equal: True, values identical: False, correlation 0.99999, median ratio minival/calib per muscle 0.9550 to 0.9562; channels with identical spike times: 64 of 64

  20120928: minival trials [201, 202] found in calib: 2; event times equal: True; EMG timestamps equal: True, values identical: False, correlation 0.99988, median ratio minival/calib per muscle 1.0047 to 1.0068; channels with identical spike times: 64 of 64
Sat Oct 31 19:01:01 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
p='/tmp/claude-1001/gen/make_nb.py'
s=open(p).read()
s=s.replace('''chance from EMG at lags of a second or more before contact, before the median go cue, rises from
about 0.5 s before contact (the median onset is about 0.2 s before contact) and is decoded almost
perfectly around contact''','''chance (0.26 to 0.35, against 0.345 for the largest class) from EMG at lags of a second or more
before contact, before the median go cue (0.5 s before contact), rises from about 0.7 s before
contact, and is decoded at 0.95 to 0.99 from 0.2 s before contact to 0.1 s after it (spikes 0.84 to
0.90)''')
s=s.replace("while the next trial's object is not.","while the next trial's object is decoded at 0.40 to 0.45 at those lags.")
open(p,'w').write(s)
EOF
cd entries/000941-rouse-2015 && python $TMPDIR/gen/make_nb.py
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000941-rouse-2015
type: reproduction
title: Location and object effects in reach-to-grasp kinematics (Rouse and Schieber 2015)
description: Tests the claims of Rouse and Schieber (2015) on dandiset 000941, the FALCON M1-A
  benchmark, which holds trial tables, EMG and multiunit spikes of monkey L, including part of the
  paper's session L20120928, and no marker positions or joint angles. It checks the trial counts
  and the movement time of the session, names the object codes from the paper's apparatus order,
  and records the kinematic claims as blocked.
license: Apache-2.0
notebooks:
- path: reproduce_rouse_2015.ipynb
  title: Reproducing Rouse and Schieber (2015) from dandiset 000941
  runtime_minutes: 1
helpers:
- rouse.py
related:
- id: dandi:000941/0.241029.1405
  relation: uses_data
- id: doi:10.1152/jn.00686.2015
  relation: reproduces
EOF
printf "dandi\nh5py\nmatplotlib\nnumpy\npandas\nremfile\nscikit-learn\nscipy\n" > requirements.in
cd  && python tools/entry.py lock entries/000941-rouse-2015 2>&1 | tail -3
```

```
wrote entries/000941-rouse-2015/requirements.lock.txt
```

**Agent**

Now the README, then the attempt record before running checks.

**Agent calls Bash**

```bash
cat > entries/000941-rouse-2015/README.md <<'EOF'
# Rouse & Schieber (2015) from dandiset 000941

Tests the findings of [Rouse and Schieber (2015)](https://doi.org/10.1152/jn.00686.2015) on
[DANDI:000941](https://dandiarchive.org/dandiset/000941/0.241029.1405), the FALCON M1-A benchmark.
The dandiset holds trial tables, EMG and multiunit spikes of monkey L, including the first 53
minutes of the paper's session L20120928 (412 successful trials, no failed ones). It holds no marker
positions or joint angles, which every kinematic finding of the paper uses, and no data of monkeys
X and Y.

| Claim | Outcome |
|---|---|
| Trial counts of Table 2 | Blocked: data missing |
| Median movement time 255 ms in monkey L, differing among monkeys | Not reproduced (200 ms; monkey L only) |
| 28 trials to the coaxial cylinder at 45 degrees (Fig. 2) | Blocked: data missing |
| The 23 claims on joint angles and marker positions (Figs. 2 to 10) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files' `tgt_obj` does not name the grasped object; `obj_id` does, and its codes are named here
from the apparatus order in the paper's Fig. 1 legend. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000941-rouse-2015-01.yaml`](../../attempts/000941-rouse-2015-01.yaml).
EOF
grep -n "verifications\|response" schemas/attempt.schema.json | head -5; ls questions | grep 000941
```

```
334:    "verifications": {
380:                "response": {
```

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/make_attempt.py <<'PYEOF'
import yaml
claims = yaml.safe_load(open('claims/000941/10.1152-jn.00686.2015.yaml'))['claims']
ids = [c['id'] for c in claims]
NB = 'reproduce_rouse_2015.ipynb'
no_kin_angles = ("No file of the dandiset holds joint angles or the marker positions they are computed from; "
                 "the only data series are the trial table, 16 channels of EMG, an evaluation mask and multiunit "
                 "spike times (notebook, data check). Monkeys X and Y are not in the dandiset. No other public "
                 "source of the paper's kinematics is named by the paper or the claims file.")
no_kin_markers = ("No file of the dandiset holds marker positions, from which the distal forearm point, the "
                  "elbow point and the hand configurations are computed; the only data series are the trial "
                  "table, EMG, an evaluation mask and multiunit spike times (notebook, data check). Monkeys X "
                  "and Y are not in the dandiset.")
out = []
for cid in ids:
    if cid == 'table2-trial-counts':
        out.append({'claim': cid, 'outcome': 'blocked', 'blocked_by': 'data_missing', 'notebook': NB,
                    'output': f'claim:{cid}',
                    'notes': ("The file of session L20120928 (held-in-calib) holds 412 trials, all rewarded, "
                              "numbered 201 to 673 (one stored as 127) and spanning 53.3 of the session's 86.2 "
                              "minutes; the paper gives 768 trials, 717 successful and 685 analyzed. The file "
                              "holds no failed trials, so neither the total nor the analyzed count can be formed, "
                              "and it holds a part of the successful ones, the part released as the FALCON "
                              "calibration split. If every number absent inside 201 to 673 were an error trial, "
                              "the span would hold 473 trials, 412 successful and 387 with the preceding number "
                              "present; this is not a count of the session. Monkeys X and Y are not in the "
                              "dandiset."),
                    'deviations': ["Only the held-in-calib file of the session is counted; the minival file "
                                   "repeats its first two trials."]})
    elif cid == 'table2-movement-time':
        out.append({'claim': cid, 'outcome': 'not_reproduced', 'notebook': NB, 'output': f'claim:{cid}',
                    'measured': [200.0],
                    'notes': ("Monkey L only. Median contact_time minus move_onset_time over the 412 successful "
                              "trials of session L20120928 in the file is 200 ms (quartiles 160 and 240 ms), "
                              "against 255 ms (225, 295) with tolerance 229.5 to 280.5 ms; 41 samples from M to C "
                              "against 52. The approximation of the analyzed trials (preceding trial number "
                              "present, 387 trials) gives the same 200 ms. Event times lie on a 20 ms grid. "
                              "Medians by object run from 160 ms (perpendicular cylinder) to 280 ms (button), and by "
                              "location from 160 ms (157.5 degrees) to 300 ms (0 degrees); the other three monkey "
                              "L sessions of the dandiset give 180 to 200 ms. Monkeys X and Y are not in the "
                              "dandiset, so their medians, the difference among monkeys and the Kruskal-Wallis "
                              "test cannot be tested, and the claim is judged on the one median that can. The "
                              "dandiset does not say how move_onset_time was found; an onset defined differently "
                              "from the paper's marker-speed threshold would explain the difference, and the "
                              "data cannot show which, as they hold no kinematics."),
                    'deviations': [
                        "The dataset's move_onset_time and contact_time are used, as the claims file directs when "
                        "the dataset gives onset times; the paper's onset (average speed of 36 markers above 5 SD "
                        "of a baseline, Methods, Temporal Normalization) cannot be recomputed without markers.",
                        "Event times are at 20 ms resolution, where the paper's onset is at 5 ms and contact at 1 ms.",
                        "Only 412 of the session's 717 successful trials are in the dandiset; reading (a), the "
                        "analyzed trials, is approximated by the trials whose preceding trial number is present, "
                        "as the error trials are absent.",
                        "Monkey L only; X and Y are not in the dandiset."]})
    elif cid == 'fig2-trial-count-coax-45':
        out.append({'claim': cid, 'outcome': 'blocked', 'blocked_by': 'data_missing', 'notebook': NB,
                    'output': f'claim:{cid}',
                    'notes': ("The file holds 19 successful trials of the coaxial cylinder (obj_id 1) at 45 "
                              "degrees, 16 with the preceding trial number present, against 28 in the paper. It "
                              "holds 412 of the session's 717 successful trials (57%), and 57% of 28 is 16, so the "
                              "count of the whole session cannot be taken from it. The object is named from obj_id "
                              "by the apparatus order of the Fig. 1 legend; tgt_obj does not name the grasped "
                              "object (notebook, data check)."),
                    'deviations': ["The name of obj_id 1 (coaxial cylinder) is inferred from the order of the "
                                   "objects in the paper's Fig. 1 legend and the locations at which each code "
                                   "occurs; the files do not name the codes."]})
    else:
        markers = cid in ('fig9-hand-configuration-location', 'fig10-forearm-trajectory-object',
                          'elbow-point-trajectory-object')
        o = {'claim': cid, 'outcome': 'blocked', 'blocked_by': 'data_missing',
             'notes': no_kin_markers if markers else no_kin_angles}
        if cid in ('fig2-joint-patterns', 'fig2-hand-opening-two-phases'):
            o['notes'] += " It also depends on fig2-trial-count-coax-45, which is blocked."
        if cid in ('fig7-time-course',):
            o['notes'] += " It also depends on fig7-mean-eta-30 and fig7-mean-eta-90, which are blocked."
        if cid == 'fig8-hand-shape-invariant-to-location':
            o['notes'] += " It also depends on fig8a-lda-location and fig8b-lda-object, which are blocked."
        out.append(o)

rec = {
 'schema_version': 2,
 'id': '000941-rouse-2015-01',
 'dataset': {'archive': 'dandi', 'id': '000941', 'version': '0.241029.1405',
             'doi': '10.48324/dandi.000941/0.241029.1405'},
 'paper': 'doi:10.1152/jn.00686.2015',
 'date': '2026-10-31',
 'entry': '000941-rouse-2015',
 'provenance': {'kind': 'agent', 'accountable': {'name': 'CatalystNeuro'},
                'agent': {'harness': 'Claude Code', 'model': 'claude-opus-5-5', 'protocol': 'pilot-13'},
                'runner': {'platform': 'GitHub Actions',
                           'url': 'https://github.com/catalystneuro/encore/actions/runs/41231374559'}},
 'outcomes': out,
 'findings': [
  {'kind': 'data_missing', 'statement': (
     "The dandiset holds no kinematic data. The paper's findings are about 22 joint angles computed from 36 "
     "markers tracked at 200 frames/s, and no file holds a marker position, a joint angle or any other "
     "kinematic series; the files hold trial tables, 16 channels of EMG at 50 Hz, an evaluation mask and "
     "multiunit spike times. 23 of the 26 claims are blocked for this reason.")},
  {'kind': 'data_missing', 'statement': (
     "Only monkey L is in the dandiset. The paper's monkeys X (session X20121219) and Y (Y20130516) are not; "
     "the description points to dandiset 001209 for another monkey, which holds monkey X (with session "
     "20121219 in its held-out-calib split) and had no published version when read.")},
  {'kind': 'selection_undocumented', 'statement': (
     "The paper's session L20120928 is in the dandiset only in part. Its held-in-calib file holds 412 trials, "
     "all rewarded, numbered 201 to 673 and spanning 53 of the session's 86 minutes, where the paper reports 768 "
     "trials and 717 successes. Within 201 to 673, 61 numbers are absent in gaps of 1 to 15; the files do not say "
     "which trials were left out, or why (errors, or trials held back for the benchmark's evaluation). The "
     "result column, described as success, failure or abort, holds R in every trial of every file.")},
  {'kind': 'metadata_error', 'statement': (
     "tgt_obj, described as the object to grasp at the target, does not name the grasped object. In session "
     "20120928 it takes three values (Sphere, Button, Coaxial) in three runs of 118, 159 and 135 consecutive "
     "trials, each value occurring with all four obj_id codes and every location. obj_id has four codes whose "
     "locations within each block are offset by multiples of 45 degrees, as the paper's apparatus has them, and "
     "the grasped object is decoded from EMG around contact at 0.99 with obj_id against 0.42 with tgt_obj "
     "(largest class 0.39).")},
  {'kind': 'metadata_insufficient', 'statement': (
     "obj_id, the actual object code, has no names. From the paper's Fig. 1 legend (clockwise order "
     "perpendicular cylinder, coaxial cylinder, button, sphere, with 157.5 degrees leftmost) and the locations "
     "at which each code occurs, codes 2, 1, 4 and 3 are the perpendicular cylinder, coaxial cylinder, button "
     "and sphere; the names fit every constraint the legend states, but the files do not confirm them.")},
  {'kind': 'metadata_error', 'statement': (
     "In each of the four held-in-calib files one trial carries the number 127 between trials 254 and 256 or "
     "257, in time order, where 255 (or 256) is expected; 127 is the largest signed 8-bit integer. In session "
     "20120927 a second trial, the first of the file, is also numbered 127, so the number does not identify a "
     "trial there.")},
  {'kind': 'metadata_insufficient', 'statement': (
     "The event times move_onset_time, contact_time and reward_time are not defined, and all event times lie on "
     "a 20 ms grid. The median time from move_onset_time to contact_time in session 20120928 is 200 ms, where "
     "the paper reports 255 ms for the same session, so the onset is likely defined differently from the paper's "
     "marker-speed threshold. reward_time follows contact by a median of 0.10 s (0 to 0.92 s), where the paper's "
     "task requires a 1,000 ms hold before the reward. start_time and stop_time are exactly 1 s before the cue "
     "and 1 s after reward_time in every trial, a window, not the trial's start and stop.")},
  {'kind': 'other', 'statement': (
     "Each held-in-minival file repeats the first two trials of the held-in-calib file of the same session "
     "(same trial numbers, event times, EMG timestamps and spike times on all 64 channels), as the description "
     "says. The EMG values of the two copies differ by a near-constant factor per file (0.955 to 1.016), so each "
     "file's EMG was scaled on its own, and the same recording has two different EMG amplitudes in the dandiset.")},
 ],
}
class D(yaml.SafeDumper): pass
def str_rep(d, s):
    return d.represent_scalar('tag:yaml.org,2002:str', s)
D.add_representer(str, str_rep)
yaml.dump(rec, open('attempts/000941-rouse-2015-01.yaml', 'w'), Dumper=D, sort_keys=False, width=100, allow_unicode=True)
PYEOF
python $TMPDIR/gen/make_attempt.py && grep -n ": .*: " attempts/000941-rouse-2015-01.yaml | head; grep -c "claim:" attempts/000941-rouse-2015-01.yaml; head -40 attempts/000941-rouse-2015-01.yaml
```

```
29
schema_version: 2
id: 000941-rouse-2015-01
dataset:
  archive: dandi
  id: 000941
  version: 0.241029.1405
  doi: 10.48324/dandi.000941/0.241029.1405
paper: doi:10.1152/jn.00686.2015
date: '2026-10-31'
entry: 000941-rouse-2015
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/gen/make_attempt.py'
s=open(p).read()
s=s.replace("""class D(yaml.SafeDumper): pass
def str_rep(d, s):
    return d.represent_scalar('tag:yaml.org,2002:str', s)
D.add_representer(str, str_rep)
""","""import datetime
rec['date'] = datetime.date(2026, 10, 31)
D = yaml.SafeDumper
""")
open(p,'w').write(s)
EOF
python $TMPDIR/gen/make_attempt.py && head -12 attempts/000941-rouse-2015-01.yaml && python tools/entry.py check entries/000941-rouse-2015
```

```
schema_version: 2
id: 000941-rouse-2015-01
dataset:
  archive: dandi
  id: 000941
  version: 0.241029.1405
  doi: 10.48324/dandi.000941/0.241029.1405
paper: doi:10.1152/jn.00686.2015
date: 2026-10-31
entry: 000941-rouse-2015
provenance:
  kind: agent
0 error(s)
```

**Agent calls Bash**

```bash
python -c "import yaml;print(repr(yaml.safe_load(open('attempts/000941-rouse-2015-01.yaml'))['dataset']['id']))"; grep -rn "id: \"000941\"\|id: '000941'\|id: 000941" attempts/001453-fouke-2025-01.yaml claims/000941/*.yaml | head -3
```

```
'000941'
claims/000941/10.1152-jn.00686.2015.yaml:81:  id: "000941"
```

**Agent calls Bash**

```bash
date -u; time python tools/entry.py all entries/000941-rouse-2015 2>&1 | tail -15
```

```
Sat Oct 31 19:02:08 UTC 2026
Installed kernelspec registry-000941-rouse-2015 in executed/000941-rouse-2015/.venv/share/jupyter/kernels/registry-000941-rouse-2015
0 error(s)
pass  reproduce_rouse_2015.ipynb  (33 s)

real	0m39.789s
user	0m29.913s
sys	0m4.348s
```

**Agent**

Now read the executed copy and confirm the conclusions match the numbers.

**Agent calls Bash**

```bash
ls executed/000941-rouse-2015/; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000941-rouse-2015/reproduce_rouse_2015.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.outputs:
            if o.output_type=='stream' and ('Cross' in o.text or 'Monkey L' in o.text or 'Coaxial cylinder' in o.text or 'deposited' in o.text): print(o.text[:3000])
            if o.output_type=='error': print("ERR",o.ename)
EOF
```

```
reproduce_rouse_2015.ipynb
result.json
Recordings deposited more than once: held-in-minival against held-in-calib, per session


Cross-validated accuracy of decoding (chance as the largest class: obj_id 0.345, tgt_obj 0.386); median cue to contact 0.50 s:
 lag_from_contact_s  emg_obj_id  emg_obj_id_next_trial  emg_tgt_obj  spikes_obj_id
               -1.6       0.308                  0.345        0.485          0.250
               -1.5       0.330                  0.291        0.427          0.313
               -1.4       0.352                  0.274        0.444          0.272
               -1.3       0.286                  0.299        0.461          0.294
               -1.2       0.330                  0.313        0.478          0.255
               -1.1       0.299                  0.286        0.461          0.315
               -1.0       0.264                  0.308        0.410          0.298
               -0.9       0.354                  0.306        0.442          0.301
               -0.8       0.393                  0.301        0.452          0.245
               -0.7       0.476                  0.345        0.425          0.318
               -0.6       0.473                  0.291        0.430          0.303
               -0.5       0.529                  0.318        0.439          0.418
               -0.4       0.726                  0.427        0.403          0.517
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/was last modified a second after this version was published/was last modified within a second of the publication of this version/' $TMPDIR/gen/make_nb.py && . $TMPDIR/dev/bin/activate && python $TMPDIR/gen/make_nb.py && deactivate && python tools/entry.py all entries/000941-rouse-2015 2>&1 | tail -2 && python tools/entry.py handover entries/000941-rouse-2015 2>&1 | tail -5; ls executed/000941-rouse-2015/handover; git status --short; date -u
```

```
0 error(s)
pass  reproduce_rouse_2015.ipynb  (32 s)
wrote executed/000941-rouse-2015/handover
10.1152-jn.00686.2015.yaml
reproduce_rouse_2015.ipynb
rouse.py
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
?? attempts/000941-rouse-2015-01.yaml
?? entries/000941-rouse-2015/
?? scripts
Sat Oct 31 19:03:51 UTC 2026
```

**Agent calls Bash**

```bash
ls -la entries/000941-rouse-2015/; ls -la .bashrc scripts | head; python -c "
import nbformat;nb=nbformat.read('entries/000941-rouse-2015/reproduce_rouse_2015.ipynb',4);print(any(c.get('outputs') for c in nb.cells if c.cell_type=='code'))"
```

```
total 80
drwxr-xr-x   4 runner runner  4096 Oct 31 19:01 .
drwxr-xr-x 122 runner runner  4096 Oct 31 18:56 ..
drwxr-xr-x   3 runner runner  4096 Oct 31 18:57 .claude
-rw-r--r--   1 runner runner  1381 Oct 31 19:01 README.md
drwxr-xr-x   2 runner runner  4096 Oct 31 18:56 __pycache__
-rw-r--r--   1 runner runner   880 Oct 31 19:01 entry.yaml
-rw-r--r--   1 runner runner 34796 Oct 31 19:02 reproduce_rouse_2015.ipynb
-rw-r--r--   1 runner runner    62 Oct 31 19:01 requirements.in
-rw-r--r--   1 runner runner  5795 Oct 31 19:01 requirements.lock.txt
-rw-r--r--   1 runner runner  7323 Oct 31 18:56 rouse.py
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 18:49 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 18:49 scripts
False
```

**Agent calls Bash**

```bash
find entries/000941-rouse-2015/.claude | head; rm -rf entries/000941-rouse-2015/__pycache__; find entries/000941-rouse-2015/.claude -type f | wc -l
```

```
entries/000941-rouse-2015/.claude
entries/000941-rouse-2015/.claude/.cc-writes
0
```

**Agent calls Bash**

```bash
rm -rf entries/000941-rouse-2015/.claude 2>&1; ls -a entries/000941-rouse-2015; python tools/entry.py check entries/000941-rouse-2015
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: This Bash command contains multiple operations. The following parts require approval: rm -rf entries/000941-rouse-2015/.claude, python tools/entry.py check entries/000941-rouse-2015
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/000941-rouse-2015; date -u
```

```
0 error(s)
Sat Oct 31 19:04:02 UTC 2026
```

**Agent**

I tested 1 of the 26 claims, and it was not reproduced. The other 25 are blocked because their data are not in the dandiset, which holds no kinematics at all. The entry passes `python tools/entry.py all` (0 errors, notebook runs in 32 s), and the handover package is built in `executed/000941-rouse-2015/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| table2-trial-counts | blocked: data missing |
| table2-movement-time | not reproduced (monkey L only) |
| fig2-trial-count-coax-45 | blocked: data missing |
| The other 23 claims (fig2 shapes, fig4, all fig5–fig7, fig8a/b, fig8-hand-shape, fig9, fig10, elbow point) | blocked: data missing |

- **Trial counts:** the file of session L20120928 holds 412 successful trials (numbers 201 to 673, about 53 of 86 minutes) and no failed trials. The paper reports 768 trials and 717 successes, so the counts cannot be taken from a part of the session.
- **Movement time:** the median from the dataset's `move_onset_time` to `contact_time` is 200 ms (quartiles 160 and 240). The paper gives 255 ms (225, 295), so it is outside the tolerance of 229.5 to 280.5 ms, and it gives 41 samples where the paper has 52. The Kruskal-Wallis comparison across monkeys could not be run.
- **Coaxial cylinder at 45 degrees:** the file has 19 such trials against the paper's 28. That fits a file holding 57% of the session's successful trials.

## 2. What was found about the dataset

- **Version:** I pinned 0.241029.1405, the only published version; the paper cites none.
- **No kinematics:** no file holds marker positions or joint angles. The files hold trial tables, 16 EMG channels at 50 Hz and multiunit spikes from 64 channels.
- **Monkey L only:** the description points to dandiset 001209 for another monkey (X). It has no published version and the claims file does not name it, so I did not use it.
- **`tgt_obj` is not the object:** it runs in three long blocks (118, 159 and 135 trials) regardless of object or location.
  - `obj_id` is the object, but its codes have no names. I named them from the object order in the paper's Fig. 1 legend: 2 = perpendicular cylinder, 1 = coaxial, 4 = button, 3 = sphere. The names fit every constraint the legend states.
  - EMG decodes `obj_id` at 0.99 around contact, against 0.42 for `tgt_obj`.
  - I recorded the naming as a deviation and a finding, not as outside data.
- **Clock check:** EMG and spikes share the trial table's clock. The object decodes near chance a second or more before contact and near perfectly at contact; the next trial's object does not.
- **Trial numbers:** trial 255 or 256 is stored as 127 in all four calibration files. In session 20120927 a second trial is also numbered 127.
- **Event times:** they lie on a 20 ms grid and are not defined. `reward_time` falls a median of 0.10 s after contact, but the paper's task requires a 1 s hold before reward. `start_time` and `stop_time` are fixed 1 s windows around the cue and the reward.
- **Duplicates:** each minival file repeats the first two trials of the matching calibration file. Spikes and timestamps are identical, but the EMG is rescaled by a factor of 0.955 to 1.016.
- **Assumptions, questions for the paper's authors, questions to a reader:** none. No outcome rests on an open method choice, and I found no misreading in the claims file.

## 3. Where the protocol was unclear

1. **Claims that need three monkeys when only one is present.** The protocol does not say whether to block such a claim or judge the part that can be tested. I judged the movement time on L, since a failing L median makes the claim fail whatever X and Y show. I blocked the counts.
2. **Counts on a dataset holding only part of a session.** The protocol does not say whether that is `blocked` or `not_reproduced`. I chose `blocked: data_missing`, because the subset neither confirms nor contradicts the paper's counts.
3. **Naming dataset codes from the paper's own figure.** `with_labels` is defined for outside sources, and this source is the paper itself. I treated it as a method detail taken from the paper (step 1.6).
4. **Near-identical duplicates.** Step 1.2 speaks of identical recordings; here the copies match except for a rescaled EMG. I reported them as duplicates and noted the difference.
5. **Streams used by no claim.** Step 2's clock check is written for every data stream. I checked EMG and spikes anyway, even though only the trial table enters any claim.
6. **Blocked claims and notebook cells.** The protocol does not say whether blocked claims get notebook cells. I gave cells to the two count claims, since they show what the data hold.

## 4. Runtime and failures

- The run took about 13 minutes (18:51 to 19:04 UTC); the notebook itself runs in 32 s.
- One development error, an overflow on an unsigned trial-number column, was fixed before the final run.
- The sandbox refused to delete an empty `.claude/` directory the harness created inside the entry. Git ignores empty directories, so it will not be committed.
- The untracked dotfiles and `scripts` in the repository root are sandbox device files, not mine.

## End of run

49 turns, 12 minutes, result: success.
