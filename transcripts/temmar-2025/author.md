# temmar-2025 · author · run 43201995281

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (51.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/056ccacd-695e-4936-8075-9c6010019477/tool-results/b27qi31xb.txt

Preview (first 2KB):
Thu Nov 12 10:40:16 UTC 2026
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
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 635 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -100; wc -l docs/design.md docs/archives.md; ls entries/fouke-2025 claims attempts paper questions papers/datasets | head -80; cat papers/datasets/temmar-2025.yaml
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
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p claims/temmar-2025.yaml
```

```
# Claims for Temmar et al. (2025), "Long-term Intracortical Neural activity and Kinematics
# (LINK)", NeurIPS 2025 Datasets and Benchmarks track, on dandiset 001201.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-12, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the version of record (open-access PDF from the Curran Associates NeurIPS 2025
# proceedings, extracted to paper/10.52202-085713-4642.txt), main text, figure legends and
# checklist, and the supplement (Supplementary Materials and Appendices, from OpenReview):
# Appendix A (task, implants, feature extraction), B (curation, file format), C (analysis
# methods) and Figures S1 to S6. The paper reports no statistical test for any finding; its
# findings are slopes of linear fits, counts, R2 values and visual descriptions of figures.
#
# Code read: github.com/chesteklab/LINK_dataset at commit 5e1c36a1282f90abb8d96963920a8b1fdd27a6e7
# (2026-10-20). It holds the NWB-to-pickle converter (utils/), the signal-change analysis
# (data_processing/signal_changes: mean SBP per channel and day, active channels, participation
# ratio), single-channel tuning (data_processing/single_channel_tuning/tuning_utils.py), the
# population PCA analysis (data_processing/pop_level_analyses/population_level_analyses.py),
# single-day RR and LSTM decoders and their cross-day evaluation (data_processing/bci_decoding),
# the multi-day training (data_processing/stability/stability, which calls an outside library,
# "neuraldecoding", not in the repository) and the continual fine-tuning
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,900p claims/temmar-2025.yaml
```

```
are listed, and the LSTM is retrained with two further seeds on those sessions to show whether
    the result rests on the seed (42 in the code).
- id: fig4bc-dof-accuracy
  statement: Decoding of finger positions is more accurate than of velocities, and MRS predictions
    are more accurate than IDX predictions.
  source: Section 4.3, paragraph 1; Figure 4B and 4C
  quote: In general, the position accuracies of the two finger groups outperformed velocities, and
    MRS predictions outperformed IDX predictions, suggesting there may be more information
    regarding the MRS finger group in the neural data than IDX.
  depends_on:
  - fig4a-sameday-stable
  criterion: Same-day R2 per output from fig4a-sameday-stable. For each decoder, the median over
    sessions of each of IDX position, MRS position, IDX velocity and MRS velocity. Reproduced when,
    for both decoders, both position medians exceed both velocity medians, and MRS exceeds IDX for
    position and for velocity; partially reproduced when the orderings hold for one decoder or
    only one of the two orderings holds for both. The fraction of sessions in which each ordering
    holds is reported ("in general").
- id: fig4d-cross-day-decay
  statement: Decoders tested on hold-out sets of other days within 100 days of training lose
    accuracy sharply in the short term, with the decay stabilising at longer offsets; neither RR
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -150; grep -n "DANDI" -A60 docs/archives.md | head -120
```

```
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
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
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
[... 285 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/fouke-2025-01.yaml | grep -v "^    " | head -60; tail -80 attempts/fouke-2025-01.yaml; cat entries/fouke-2025/README.md | head -30
```

```
outcome: not_reproduced
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
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^findings" -A25 attempts/fouke-2025-01.yaml | head -40; curl -s https://api.dandiarchive.org/api/dandisets/001201/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001201/versions/" | python -m json.tool | grep -E '"version"|"status"|"modified"|asset_count|size'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls -la paper/; grep -n -i "dandi\|doi.org/10.48324" paper/*.txt | head; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.52202-085713-4642.txt",
 "offset": 100,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Appendix\|^A\.[0-9]\|^B\.[0-9]\|^C\.[0-9]\|Supplementary" paper/10.52202-085713-4642.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.52202-085713-4642.txt",
 "offset": 1100,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; which python; python -c "import pynwb, remfile, h5py, dandi, torch, sklearn; print(torch.__version__, torch.get_num_threads())" 2>&1; nproc; free -g; nvidia-smi 2>&1 | head -3
```

```
Thu Nov 12 10:40:44 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, dandi, torch, sklearn; print(torch.__version__, torch.get_num_threads())
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Swap:              2           0           2
/bin/bash: line 1: nvidia-smi: command not found
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.12 venv && . venv/bin/activate && uv pip install -q dandi pynwb remfile h5py numpy scipy pandas scikit-learn matplotlib jupyter nbconvert ipykernel && uv pip install -q torch --index-url https://download.pytorch.org/whl/cpu && python -c "import torch;print(torch.__version__)"; cat tools/entry.py | grep -n "python\|torch\|index-url" | head -30
```

```
2.15.0+cpu
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
206:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
208:                         f"says {entry['python']}; run `tools/entry.py lock`")
403:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
406:def python_of(entry_dir: Path) -> str:
407:    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
410:    if entry.get("python"):
411:        return str(entry["python"])
420:def set_python(entry_dir: Path, version: str) -> None:
421:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
424:    line = f'python: "{version}"'
425:    if re.search(r"^python:.*$", text, re.M):
426:        text = re.sub(r"^python:.*$", line, text, count=1, flags=re.M)
436:    version = version or python_of(entry_dir)
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 425,600p tools/entry.py; grep -rn "torch" entries/*/requirements.in | head
```

```
if re.search(r"^python:.*$", text, re.M):
        text = re.sub(r"^python:.*$", line, text, count=1, flags=re.M)
    elif re.search(r"^license:.*$", text, re.M):
        text = re.sub(r"^(license:.*)$", rf"\1\n{line}", text, count=1, flags=re.M)
    else:
        text = text.rstrip("\n") + f"\n{line}\n"
    path.write_text(text)


def lock(entry_dir: Path, version: str | None = None) -> int:
    """Pin every package, with its hashes, for the entry's Python version, which entry.yaml then records."""
    version = version or python_of(entry_dir)
    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--generate-hashes", "--python-version", version,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        set_python(entry_dir, version)
        print(f"wrote {entry_dir.name}/requirements.lock.txt (Python {version}, with hashes)")
    return r.returncode


[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import requests, json
V="0.261026.1912"
url=f"https://api.dandiarchive.org/api/dandisets/001201/versions/{V}/assets/?page_size=1000"
r=requests.get(url).json()
print(r['count'])
a=r['results']
for x in a[:5]+a[-3:]: print(x['path'], x['size'], x['asset_id'])
json.dump(a, open('assets.json','w'))
m=requests.get(f"https://api.dandiarchive.org/api/dandisets/001201/versions/{V}/").json()
print(json.dumps({k:m[k] for k in ['name','description','citation','doi','version','assetsSummary','relatedResource'] if k in m}, indent=1)[:4000])
EOF
```

```
312
sub-Monkey-N/sub-Monkey-N_ses-20200204_ecephys.nwb 43052898 ea07a2e3-d5f4-4036-9b62-93d1f89cba64
sub-Monkey-N/sub-Monkey-N_ses-20200127_ecephys.nwb 45005026 c002a9a1-664d-4a69-af02-ba810046c4fb
sub-Monkey-N/sub-Monkey-N_ses-20200130_ecephys.nwb 43863496 9d1820f1-7583-4faf-bbd0-7e9fb7001ca4
sub-Monkey-N/sub-Monkey-N_ses-20200206_ecephys.nwb 43884592 008fc384-2a95-47ec-8dbe-7acb4a18bcc7
sub-Monkey-N/sub-Monkey-N_ses-20200205_ecephys.nwb 43262978 24b91bc3-92ba-457c-8718-490b508f6b8f
sub-Monkey-N/sub-Monkey-N_ses-20230620_ecephys.nwb 39833192 0b2c3248-9087-4e92-95b5-374c3a998d4d
sub-Monkey-N/sub-Monkey-N_ses-20230621_ecephys.nwb 38365864 9f72e8a2-1132-4255-80bb-adc7d8bbdf90
sub-Monkey-N/sub-Monkey-N_ses-20230622_ecephys.nwb 46628472 6c90efe9-f100-4196-9b92-0e27e78aa13f
{
 "name": "LINK: Long-Term Intracortical Neural Activity and Kinematics",
 "description": "This dataset contains 312 sessions of multiunit threshold crossings, spiking band power, and behavioral data from a macaque performing a self-paced finger movement task. These sessions were recorded on 303 days spanning 1,242 days (~3.5 years). The dataset will be useful in evaluating the stability of neural population recordings and BMI decoding algorithms across long time frames. On each day, we include 96 channels of neural activity from Utah microelectrode arrays implanted in the motor cortex (M1). The positions & velocities of the index finger and middle-ring-small fingers were recorded using a manipulandum, where positions were normalized between full flexion and full extension. The experimental task was to move the two finger groups to acquire targets cued on a screen. Each session has 375 trials of one of two target presentation styles, center-out (trials alternating between the targets at a non-center location and then both targets at center), or random targets (target position for each finger chosen randomly at each trial, with a maximum flexion difference between fingers of 50%). Further details on t
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import json, collections, time, h5py, remfile, requests
a=json.load(open('assets.json'))
paths=sorted(x['path'] for x in a)
print([p for p in paths if 'ses-2020020' in p])
dates=collections.Counter(p.split('ses-')[1][:8] for p in paths)
print(len(dates), [d for d,c in dates.items() if c>1])
print([p for p in paths if not p.endswith('_ecephys.nwb')][:20])
x=a[0]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
s3=requests.head(url, allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(s3),'r')
def show(n,o):
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, dict(o.attrs) if len(o.attrs)<8 else list(o.attrs))
    else: print(n, dict(o.attrs) if o.attrs else '')
f.visititems(show)
print(time.time()-t)
EOF
```

```
['sub-Monkey-N/sub-Monkey-N_ses-20200204_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20200205_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20200206_ecephys.nwb']
303 ['20211015', '20220225', '20220408', '20220415', '20220429', '20220513', '20220810', '20220921', '20221102']
[]
acquisition 
analysis 
analysis/SpikingBandPower {'comments': 'no comments', 'description': 'Spiking Band Power across time, in 20ms bins', 'namespace': 'core', 'neurodata_type': 'ElectricalSeries', 'object_id': 'd66c9977-39ae-48de-af6a-881f397fc931'}
analysis/SpikingBandPower/data (26441, 96) float64 {'conversion': np.float64(1e-06), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
analysis/SpikingBandPower/electrodes (96,) int64 {'description': 'All recorded contacts', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTableRegion', 'object_id': 'e7b4a369-77a8-45fe-ae4c-827cd54b0290', 'table': <HDF5 object reference>}
analysis/SpikingBandPower/timestamps (26441,) float64 {'interval': np.int64(1), 'unit': 'seconds'}
analysis/ThresholdCrossings {'comments': 'no comments', 'description': 'Threshold crossings (threshold = -4.5RMS) across time, in 20ms bins', 'namespace': 'core', 'neurodata_type': 'ElectricalSeries', 'object_id': '855b41d5-2e18-461f-85dc-4a23147060ff'}
analysis/ThresholdCrossings/data (26441, 96) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'volts'}
analysis/ThresholdCrossings/timestamps (26441,) float64 {'interval': np.int64(1), 'unit': 'seconds'}
analysis/index_position {'comments': 'Processed position data (averaged over 20 ms bins)', 'description': 'Index flexion position, from fully extended (0) to fully flexed (1)', 'namespace': 'core', 'neurodata_type': 'TimeSeries', 'object_id': '67f3c22b-c736-49b3-be78-509a018beec1'}
analysis/index_position/data (26441, 1) float64 {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'flexion units'}
a
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import json, time, h5py, remfile, requests, numpy as np, resource
a=json.load(open('assets.json'))
for V in ["0.251023.2336","0.261015.2153"]:
    r=requests.get(f"https://api.dandiarchive.org/api/dandisets/001201/versions/{V}/assets/?page_size=1000").json()['results']
    old={x['path']:x['asset_id'] for x in r}
    print(V, len(old), sum(old.get(x['path'])==x['asset_id'] for x in a))
    # compare blob via asset detail?
x=a[0]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
s3=requests.head(url, allow_redirects=True).url
print(s3[:120])
t=time.time()
f=h5py.File(remfile.File(s3),'r')
sbp=f['analysis/SpikingBandPower/data'][:]
tc=f['analysis/ThresholdCrossings/data'][:]
ts=f['analysis/SpikingBandPower/timestamps'][:]
print('read', time.time()-t, sbp.nbytes/1e6, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
print(f['analysis/SpikingBandPower/data'].chunks, f['analysis/SpikingBandPower/data'].compression)
print(sbp.mean(), sbp.min(), sbp.max(), np.percentile(sbp.mean(0),[0,50,100]))
print(np.unique(tc)[:20], tc.mean()*50)
print(np.diff(ts)[:5], np.unique(np.round(np.diff(ts),4)), ts[0], ts[-1])
tr=f['intervals/trials']
for k in ['start_time','stop_time','trial_number','trial_count','run_id','index_target_position','mrs_target_position','target_style','trial_timeout']:
    print(k, tr[k][:6])
for k in ['session_description','identifier','session_start_time','timestamps_reference_time','general/experiment_description','general/subject/date_of_birth','general/subject/description','general/subject/subject_id','general/keywords']:
    print(k, f[k][()])
e=f['general/extracellular_ephys/electrodes']
for k in ['id','array_name','bank','pin','row','col','imp','location','filtering']:
    print(k, e[k][:8], e[k][-3:])
EOF
```

```
0.251023.2336 312 312
0.261015.2153 312 312
https://dandiarchive.s3.amazonaws.com/blobs/68f/2af/68f2afdf-0748-4644-a5e7-f13d9b976411?response-content-disposition=at
read 1.0669658184051514 20.306688 167.76
None None
3.9168437441531094 0.86875 38.175 [ 1.77618342  3.26790501 16.20395374]
[0. 1. 2. 3. 4. 5. 6. 7.] 6.232587017636751
[0.02 0.02 0.02 0.02 0.02] [0.019 0.02  0.021] 4.772 533.572
start_time [ 4.772  7.372  8.492 10.312 11.712 14.552]
stop_time [ 7.352  8.472 10.292 11.692 14.532 15.692]
trial_number [ 6  7  8  9 10 11]
trial_count [130  56  91  70 142  58]
run_id [5 5 5 5 5 5]
index_target_position [0.7 0.5 0.9 0.5 0.9 0.5]
mrs_target_position [0.3 0.5 0.5 0.5 0.9 0.5]
target_style [b'CO' b'CO' b'CO' b'CO' b'CO' b'CO']
trial_timeout [10000 10000 10000 10000 10000 10000]
session_description b'Neural and behavioral data for target style CO'
identifier b'2020-02-04_CO_nwb'
session_start_time b'2020-02-04T00:00:00+00:00'
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import torch, time
torch.manual_seed(0)
for nt in [1,2,4]:
    torch.set_num_threads(nt)
    lstm=torch.nn.LSTM(96,300,1,batch_first=True); fc=torch.nn.Linear(300,4)
    opt=torch.optim.Adam(list(lstm.parameters())+list(fc.parameters()),lr=2e-4, weight_decay=1e-3)
    x=torch.randn(64,20,96); y=torch.randn(64,4)
    t=time.time()
    for i in range(200):
        o,_=lstm(x); l=((fc(o[:,-1])-y)**2).mean(); opt.zero_grad(); l.backward(); opt.step()
    print(nt,(time.time()-t)/200*2000,'s per model')
EOF
```

```
1 105.05433797836304 s per model
2 57.017385959625244 s per model
4 70.1624870300293 s per model
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/chesteklab/LINK_dataset && cd LINK_dataset && git checkout -q 5e1c36a1282f90abb8d96963920a8b1fdd27a6e7 && git log -1 --format=%H && find . -name "*.py" | head -50
```

```
5e1c36a1282f90abb8d96963920a8b1fdd27a6e7
./generate_figures.py
./data_plotting/dataset_overview.py
./data_plotting/signal_changes_plotter.py
./data_plotting/dimensionality_across_days_analysis.py
./data_plotting/bci_decoding_plots.py
./data_plotting/single_channel_tuning.py
./data_plotting/__init__.py
./data_processing/dataset_overview/dataset_overview.py
./data_processing/dataset_overview/__init__.py
./data_processing/single_channel_tuning/tuning_plotter.py
./data_processing/single_channel_tuning/tuning_utils.py
./data_processing/single_channel_tuning/__init__.py
./data_processing/stability/stability/multiday_eval.py
./data_processing/stability/stability/trainer_multiday.py
./data_processing/stability/stability/plot_continual_learning_final.py
./data_processing/signal_changes/signal_utils.py
./data_processing/signal_changes/signal_changes.py
./data_processing/signal_changes/__init__.py
./data_processing/pop_level_analyses/population_level_analyses.py
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset/data_processing/bci_decoding && cat train_models_singleday.py lstm.py nn_utils.py | head -400
```

```
import os
import pickle
import sys
import pandas as pd
import random
import numpy as np
import torch
import time
from sklearn.linear_model import Ridge
from torch.utils.data import DataLoader
from sklearn.preprocessing import StandardScaler
import torch.nn as nn

from lstm import LSTMModel
from data_utils import prep_data_and_split
from nn_utils import FingerDataset, create_optimizer_and_scheduler, train_model, SequenceScaler

"""
Script for training an LSTM and a Ridge Regression model on every day of the dataset.
Models are saved as .pkl files.
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset/data_processing && sed -n '/def train_model/,$p' bci_decoding/nn_utils.py | sed -n 25,90p; cat bci_decoding/data_utils.py | head -80; cat bci_decoding/metrics.py | head -30
```

```
model.train()
    
    # Initialize history dictionary
    history = {
        'train_losses': [],
        'iterations': []
    }
    
    # Add validation losses list only if validation is enabled
    if val_dataloader is not None:
        history['val_losses'] = []
    
    iteration = 0
    pbar = tqdm(total=num_iterations, desc="Training")
    
    while iteration < num_iterations:
        for inputs, targets in dataloader:
            if iteration >= num_iterations:
                break
                
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset && sed -n '/def add_training_noise/,/return/p' data_processing/bci_decoding/nn_utils.py; grep -n "sbp\|0.25\|finger_kinematics\|tcfr\|conversion" utils/nwb_tools.py utils/data_tools.py | head -40; grep -n "0.25\|\*50\|\* 50\|linregress\|def " data_processing/signal_changes/signal_utils.py | head -40
```

```
def add_training_noise(x,
                       bias_neural_std=None,
                       noise_neural_std=None,
                       noise_neural_walk_std=None,
                       bias_allchans_neural_std=None,
                       device='cpu'):
    """Function to add different types of noise to training input data to make models more robust.
       Identical to the methods in Willet 2021.
    Args:
        x (tensor):                     neural data of shape [batch_size x seq_len x num_chans]
        bias_neural_std (float):        std of bias noise
        noise_neural_std (float):       std of white noise
        noise_neural_walk_std (float):  std of random walk noise
        bias_allchans_neural_std (float): std of bias noise, bias is same across all channels
        device (device):                torch device (cpu or cuda)
    """
    # Transpose x to [batch_size x num_chans x seq_len] to match original function's expectation
    x = x.transpose(1, 2)
    
    if bias_neural_std:
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset && sed -n 15,70p utils/nwb_tools.py; sed -n 20,90p data_processing/signal_changes/signal_utils.py
```

```
# helper → fetch from /analysis or raise clear error
        def ts(name: str):
            try:
                return ana[name]
            except KeyError as e:
                raise KeyError(
                    f"TimeSeries '{name}' not in /analysis of '{fp}'"
                ) from e

        # --- time and kinematics ---
        t_sec = ts("index_position").timestamps[:]
        time_ms = (np.round(t_sec * 1000)).astype(np.int32)

        finger_kinematics = np.column_stack(
            [
                ts(n).data[:].ravel()
                for n in (
                    "index_position",
                    "mrs_position",
                    "index_velocity",
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset/data_processing && grep -n "def compute_channel_tuning" -A45 single_channel_tuning/tuning_utils.py | head -70; grep -n "STARTING_DAYS\|UPDATE_NEURAL\|SECONDS\|ITER" continual_learning/continual_learning_lstm.py | head
```

```
19:def compute_channel_tuning(neural, full_behavior, velocity_tuning = False):
20-    if velocity_tuning:
21-        behavior = full_behavior[:,[2,3]]
22-    else:
23-        behavior = full_behavior[:,[0,1]]
24-
25-    channel_tunings = np.zeros((neural.shape[1], behavior.shape[1]))
26-    for channel in range(neural.shape[1]):
27-        single_channel = neural[:, channel]
28-
29-        eps = 1e-8
30-        std = np.std(single_channel)
31-
32-        if std < eps:
33-            single_channel = single_channel - np.mean(single_channel)
34-        else:
35-            single_channel = (single_channel - np.mean(single_channel)) / std
36-
37-        # calculate tuning to each dof at a variety of lags, pick the one which gives the largest l2 norm across the 2 dof
38-        lag_range = 11 # look up to 10 bins of lag
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LINK_dataset/data_processing && sed -n 41,84p continual_learning/continual_learning_lstm.py
```

```
STARTING_DAYS = [
    '2020-07-08', # 1
    '2020-10-02', # 2
    '2020-12-12', # 3
    '2021-02-27', # 4
    '2021-04-05', # 5
    '2021-05-05', # 6
    '2021-06-16', # 7
    '2021-07-09', # 8
    '2021-07-29', # 9
    '2021-08-19', # 10
    '2021-09-14', # 11
    '2021-10-27', # 12
    '2022-01-17', # 13
    '2022-02-21', # 14
    '2022-04-01', # 15
    '2022-04-21', # 16
    '2022-06-01', # 17
    '2022-08-05', # 18
    '2022-09-01', # 19
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import json;a=json.load(open('assets.json'))
p=sorted(x['path'] for x in a); print([x for x in p if '20211015' in x or '20220225' in x]); print(p[0],p[-1])"; grep -n "std\|150\|600\|align\|jerk" LINK_dataset/data_processing/pop_level_analyses/population_level_analyses.py | head -40
```

```
['sub-Monkey-N/sub-Monkey-N_ses-20211015_obj-1wbkdus_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20211015_obj-a6r2sq_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220225_obj-1n9hlgs_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220225_obj-1o8kg92_ecephys.nwb']
sub-Monkey-N/sub-Monkey-N_ses-20200127_ecephys.nwb sub-Monkey-N/sub-Monkey-N_ses-20230622_ecephys.nwb
562:def max_jerk(trial_data, kinematics, std_multiplier):
564:    mvmt_idx, _ = movement_onset(trial_data, kinematics, std_multiplier)
569:        jerk = np.hstack(([0], np.diff(acceleration)))
570:        ind = np.argmax(abs(jerk[:mvmt_idx]))
573:def movement_onset(trial_data, kinematics, std_multiplier):
577:    baseline_std = np.std(baseline_period)
580:    threshold = baseline_mean + (baseline_std * std_multiplier)
581:    min_threshold = baseline_mean - (baseline_std * std_multiplier)
588:    buffer = 150
591:def trim_neural_data_at_movement_onset_std_and_smooth(data_dict, std_multiplier=2, sigma=5, display_alignment=False, trim_pt = movement_onset, direction_key = None, position_data = None):
597:    - std_multiplier: Number of standard deviations above baseline mean (default: 2)
599:    - display_alignment: flag that specifies whether to visualize kinematic alignment
615:            if display_alignment:
619:                # print(f"Movement Onset: {movement_onset(trial_data, kinematics, std_multiplier)}, Max Jerk: {max_jerk(trial_data, kinematics, None)} ")
620:                ind, buffer = trim_pt(trial_data, kinematics, std_multiplier) 
622:                start = ind - (buffer//20) # want 150 ms pre movement and 20 ms bins 
623:                end = ind + ((750-buffer) // 20) # want 600 ms post movement and 20 ms bins 
624:                # pre_movement_start = movement_onset_idx # want 150 ms pre movement and 20 ms bins 
[... 16 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/temmar-2025/link.py",
 "content": "\"\"\"Loading and measures for the LINK dataset (DANDI:001201), used by the notebooks of the\ntemmar-2025 entry, which test Temmar et al. (2025), NeurIPS Datasets and Benchmarks.\n\nWhere each parameter comes from is given next to it, as one of:\n- \"claim <id>\": the claims file's criterion for that claim (claims/temmar-2025.yaml), which cites\n  the paper or its code (github.com/chesteklab/LINK_dataset at 5e1c36a);\n- \"paper, <passage>\": a detail the claims file lacks, taken from the paper (protocol, author 1.6);\n- \"assumption\": a choice the paper leaves open, stated as such;\n- \"standard choice\": a detail that cannot change a result.\n\nThe data are streamed from the archive (remfile + h5py); nothing is written to disk.\n\"\"\"\nfrom __future__ import annotations\n\nimport os\nfrom functools import lru_cache\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET = \"001201\"\nVERSION = \"0.261026.1912\"   # most recent published version; the paper cites none\nAPI = \"https://api.dandiarchive.org/api\"\n\nBIN_S = 0.02                # 20 ms bins (paper, Section 3; checked on the timestamps)\nTCR_TO_HZ = 50.0            # counts per 20 ms bin times 50 = Hz (claim fig2b-active-channels-decrease)\nSBP_CODE_SCALE = 0.25       # claim fig2a-sbp-decline, reading (a): NWB values times 0.25\nDAYS_PER_MONTH = 30.44      # claim fig2a-sbp-decline\nKIN_NAMES = [\"idx_pos\", \"mrs_pos\", \"idx_vel\", \"mrs_vel\"]   # order of the code (utils/nwb_tools.py)\nN_TRAIN_TRIALS = 300        # paper, Appendix C.1: first 300 trials train, last 75 test\n\n\n# --------------------------------------------------------------------------------------------\n# Archive\n# --------------------------------------------------------------------------------------------\n\n@lru_cache(maxsize=1)\ndef version_metadata() -> dict:\n    return requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/\", timeout=60).json()\n\n\n@lru_cache(maxsize=1)\ndef assets() -> pd.DataFrame:\n    \"\"\"Every asset of the pinned version, with its session date from the file name.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000\"\n    rows = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        rows += r[\"results\"]\n        url = r.get(\"next\")\n    df = pd.DataFrame([{\"path\": a[\"path\"], \"asset_id\": a[\"asset_id\"], \"size\": a[\"size\"]} for a in rows])\n    df[\"date\"] = pd.to_datetime(df[\"path\"].str.extract(r\"ses-(\\d{8})\")[0], format=\"%Y%m%d\")\n    return df.sort_values([\"date\", \"path\"]).reset_index(drop=True)\n\n\ndef s3_url(asset_id: str) -> str:\n    r = requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60)\n    return r.url\n\n\ndef open_asset(asset_id: str) -> h5py.File:\n    return h5py.File(remfile.File(s3_url(asset_id)), \"r\")\n\n\ndef _str(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef read_session(asset_id: str, neural=True, tcr=True, kin=True) -> dict:\n    \"\"\"One session file, reduced to what the analyses use. Arrays are float32 except time.\n\n    trial_index is the bin at which each trial starts, found as the code does\n    (np.searchsorted of the start times in the timestamps, utils/nwb_tools.py).\"\"\"\n    out = {}\n    with open_asset(asset_id) as f:\n        an = f[\"analysis\"]\n        ts = an[\"SpikingBandPower/timestamps\"][:]\n        out[\"t\"] = ts\n        if neural:\n            out[\"sbp\"] = an[\"SpikingBandPower/data\"][:].astype(np.float32)\n        if tcr:\n            out[\"tcr\"] = an[\"ThresholdCrossings/data\"][:].astype(np.float32)\n        if kin:\n            out[\"kin\"] = np.column_stack([an[n + \"/data\"][:].ravel() for n in\n                                          (\"index_position\", \"mrs_position\", \"index_velocity\",\n                                           \"mrs_velocity\")]).astype(np.float32)\n        tr = f[\"intervals/trials\"]\n        trials = pd.DataFrame({k: tr[k][:] for k in\n                               (\"start_time\", \"stop_time\", \"trial_number\", \"trial_count\", \"run_id\",\n                                \"index_target_position\", \"mrs_target_position\", \"trial_timeout\")})\n        trials[\"target_style\"] = [_str(s) for s in tr[\"target_style\"][:]]\n        out[\"trials\"] = trials\n        out[\"trial_index\"] = np.searchsorted(ts, trials[\"start_time\"].to_numpy())\n        out[\"style\"] = trials[\"target_style\"].iloc[0]\n        out[\"identifier\"] = _str(f[\"identifier\"][()])\n        out[\"start\"] = _str(f[\"session_start_time\"][()])\n    return out\n\n\ndef read_layout(asset_id: str) -> dict:\n    \"\"\"Metadata, shapes and attributes of a file, without reading its large arrays.\"\"\"\n    with open_asset(asset_id) as f:\n        an = f[\"analysis\"]\n        series = {}\n        for name in an:\n            d = an[name][\"data\"]\n            t = an[name][\"timestamps\"]\n            series[name] = {\"shape\": d.shape, \"unit\": _str(d.attrs.get(\"unit\")),\n                            \"conversion\": float(d.attrs.get(\"conversion\")),\n                            \"n_timestamps\": t.shape[0],\n                            \"description\": _str(an[name].attrs.get(\"description\"))}\n        e = f[\"general/extracellular_ephys/electrodes\"]\n        el = pd.DataFrame({k: [(_str(v) if isinstance(v, bytes) else v) for v in e[k][:]]\n                           for k in (\"id\", \"array_name\", \"group_name\", \"bank\", \"pin\", \"row\", \"col\",\n                                     \"imp\", \"location\")})\n        tr = f[\"intervals/trials\"]\n        cols = list(tr.attrs[\"colnames\"])\n        trials = pd.DataFrame({k: tr[k][:] for k in (\"start_time\", \"stop_time\", \"trial_count\")})\n        trials[\"target_style\"] = [_str(s) for s in tr[\"target_style\"][:]]\n        return {\"series\": series, \"electrodes\": el, \"trial_columns\": [_str(c) for c in cols],\n                \"n_trials\": tr[\"id\"].shape[0], \"trials\": trials,\n                \"identifier\": _str(f[\"identifier\"][()]),\n                \"session_start_time\": _str(f[\"session_start_time\"][()]),\n                \"subject\": {k: _str(f[\"general/subject/\" + k][()]) for k in\n                            (\"subject_id\", \"date_of_birth\", \"sex\", \"species\")},\n                \"first_t\": float(f[\"analysis/SpikingBandPower/timestamps\"][0]),\n                \"dt\": np.unique(np.round(np.diff(f[\"analysis/SpikingBandPower/timestamps\"][:]), 4))}\n\n\n# --------------------------------------------------------------------------------------------\n# Signal measures\n# --------------------------------------------------------------------------------------------\n\ndef participation_ratio(x: np.ndarray) -> tuple[float, np.ndarray]:\n    \"\"\"PR of samples x (n_samples, n_channels), mean-subtracted and not z-scored, with the\n    eigenvalues of the covariance (claim fig2c-pr-decline; code signal_utils.participation_ratio).\"\"\"\n    x = x.astype(np.float64)\n    x = x - x.mean(0)\n    ev = np.linalg.eigvalsh(x.T @ x)[::-1]\n    ev = np.clip(ev, 0, None)\n    return float(ev.sum() ** 2 / (ev ** 2).sum()), ev\n\n\ndef linfit(x, y):\n    from scipy.stats import linregress\n    r = linregress(np.asarray(x, float), np.asarray(y, float))\n    return r\n\n\ndef channel_tuning(sbp: np.ndarray, pos: np.ndarray, max_lag=10) -> np.ndarray:\n    \"\"\"Preferred tuning per channel (claim fig3b-two-channels; code tuning_utils.compute_channel_tuning):\n    each channel's SBP z-scored; for each lag 0..max_lag (behaviour at t + lag), the slopes of a\n    linear regression with intercept of IDX and MRS position on the channel; the lag with the\n    largest norm is kept. Returns (n_channels, 2) coefficients (idx, mrs).\"\"\"\n    x = sbp.astype(np.float64)\n    sd = x.std(0)\n    sd[sd < 1e-8] = 1.0\n    z = (x - x.mean(0)) / sd\n    y = pos.astype(np.float64)\n    best = np.zeros((x.shape[1], 2))\n    bestn = np.full(x.shape[1], -1.0)\n    n = len(z)\n    for lag in range(max_lag + 1):\n        zx = z[: n - lag]\n        yy = y[lag:]\n        zc = zx - zx.mean(0)\n        yc = yy - yy.mean(0)\n        coef = (zc.T @ yc) / (zc ** 2).sum(0)[:, None]\n        nrm = np.linalg.norm(coef, axis=1)\n        upd = nrm > bestn\n        best[upd] = coef[upd]\n        bestn[upd] = nrm[upd]\n    return best\n\n\ndef circ_median(theta: np.ndarray) -> float:\n    \"\"\"Circular median, by brute-force minimisation of Fisher's d(theta) (paper, Appendix C.2,\n    equation 1), over the observed angles (radians).\"\"\"\n    th = np.asarray(theta, float)\n    th = th[np.isfinite(th)]\n    d = np.pi - np.abs(np.pi - np.abs(th[:, None] - th[None, :]) % (2 * np.pi))\n    return float(th[np.argmin(d.sum(0))])\n\n\ndef wrap(a):\n    return (a + np.pi) % (2 * np.pi) - np.pi\n\n\ndef circ_iqr(theta: np.ndarray) -> float:\n    \"\"\"Circular IQR (paper, Appendix C.2): shift the circular median to 0, take the quartiles\n    of the angles, and return their difference (radians).\"\"\"\n    m = circ_median(theta)\n    s = wrap(np.asarray(theta, float) - m)\n    q1, q3 = np.percentile(s, [25, 75])\n    return float(q3 - q1)\n\n\n# --------------------------------------------------------------------------------------------\n# Trials: direction, onset, alignment, throughput\n# --------------------------------------------------------------------------------------------\n\nDIRECTIONS = np.arange(8) * 45.0     # paper, Appendix C.3 and Figure S6: eight 45-degree sectors\n\n\ndef trial_directions(trials: pd.DataFrame) -> np.ndarray:\n    \"\"\"Direction class 0..7 (centre angle k*45 degrees, IDX on x, MRS on y) of the vector from the\n    previous trial's targets to this trial's targets; -1 for the first trial of a session, whose\n    starting targets are not in the file (paper, Appendix C.3).\"\"\"\n    tg = trials[[\"index_target_position\", \"mrs_target_position\"]].to_numpy(float)\n    d = np.diff(tg, axis=0)\n    ang = np.degrees(np.arctan2(d[:, 1], d[:, 0])) % 360\n    cls = (np.floor((ang + 22.5) / 45) % 8).astype(int)\n    cls[np.linalg.norm(d, axis=1) == 0] = -1\n    return np.concatenate([[-1], cls])\n\n\ndef mrs_dominant(cls: int) -> bool:\n    \"\"\"Directions centred on +-90 degrees are MRS-only movements (paper, Appendix C.3).\"\"\"\n    return cls in (2, 6)\n\n\ndef onset_and_jerk(vel: np.ndarray, k_sd: float):\n    \"\"\"Movement onset: first bin where velocity leaves mean +- k_sd * SD of the first 10% of the\n    trial's velocities; alignment: bin of maximum absolute jerk (second difference of velocity)\n    before onset (paper, Appendix C.3; k_sd 1 in the paper, 2 in the code). Returns (onset, align)\n    or (None, None).\"\"\"\n    n = len(vel)\n    nb = max(int(np.ceil(0.1 * n)), 2)\n    base = vel[:nb]\n    mu, sd = base.mean(), base.std()\n    out = np.where((vel > mu + k_sd * sd) | (vel < mu - k_sd * sd))[0]\n    out = out[out >= nb]\n    if len(out) == 0:\n        return None, None\n    on = int(out[0])\n    jerk = np.concatenate([[0, 0], np.diff(vel, 2)])\n    if on < 1:\n        return on, None\n    return on, int(np.argmax(np.abs(jerk[:on])))\n\n\ndef throughput(trials: pd.DataFrame, reading: str, width=0.15, hold_s=0.75) -> np.ndarray:\n    \"\"\"Fitts' law throughput per trial, bits/s (claim figs2-throughput-improves, readings a, b, c;\n    target width 0.15 from paper, Appendix A.1). The first trial of a session, whose starting\n    targets are unknown, is NaN. Trial length is stop_time - start_time.\"\"\"\n    tg = trials[[\"index_target_position\", \"mrs_target_position\"]].to_numpy(float)\n    d = np.diff(tg, axis=0)\n    length = (trials[\"stop_time\"] - trials[\"start_time\"]).to_numpy(float)[1:]\n    if reading == \"a\":\n        idd, t = np.log2(1 + np.linalg.norm(d, axis=1) / width), length - hold_s\n    elif reading == \"b\":\n        idd, t = np.log2(1 + np.linalg.norm(d, axis=1) / width), length\n    elif reading == \"c\":\n        idd, t = np.log2(1 + np.abs(d) / width).sum(1), length - hold_s\n    else:\n        raise ValueError(reading)\n    tp = np.where(t > 0, idd / np.where(t > 0, t, 1), np.nan)\n    return np.concatenate([[np.nan], tp])\n\n\n# --------------------------------------------------------------------------------------------\n# Decoders (paper, Section 4.3 and Appendix C.1; claim fig4a-sameday-stable; code\n# bci_decoding/train_models_singleday.py, data_utils.py, nn_utils.py)\n# --------------------------------------------------------------------------------------------\n\nRR_HIST = 8           # bins of history for ridge regression\nRR_ALPHA = 0.1\nLSTM_SEQ = 20\nLSTM_HIDDEN = 300\nLSTM_ITERS = 2000\nLSTM_BATCH = 64\nLSTM_LR = (2e-4, 1e-5)\nLSTM_WD = 1e-3\nNOISE_WHITE = 0.1     # claim fig4a-sameday-stable: 0.1 per sample (the code passes it as bias, see notebook)\nNOISE_BIAS = 0.2      # claim fig4a-sameday-stable: 0.2 per sequence and channel\n\n\ndef split(sess: dict):\n    \"\"\"Training bins (first 300 trials) and test bins (the 75 trials after them, to the end of the\n    file), as Appendix C.1 states.\"\"\"\n    i = sess[\"trial_index\"][N_TRAIN_TRIALS]\n    return (sess[\"sbp\"][:i], sess[\"kin\"][:i]), (sess[\"sbp\"][i:], sess[\"kin\"][i:])\n\n\ndef zparams(x):\n    mu = x.mean(0).astype(np.float64)\n    sd = x.std(0).astype(np.float64)\n    sd[sd < 1e-8] = 1.0\n    return mu, sd\n\n\ndef history(x: np.ndarray, k: int) -> np.ndarray:\n    \"\"\"(n, k, ch) windows ending at each bin, zero-padded before the start of the segment, as\n    data_utils.add_history does (padding is applied to the normalised data here).\"\"\"\n    pad = np.concatenate([np.zeros((k - 1, x.shape[1]), x.dtype), x])\n    idx = np.arange(len(x))[:, None] + np.arange(k)[None, :]\n    return pad[idx]\n\n\ndef rr_fit(xz: np.ndarray, y: np.ndarray):\n    from sklearn.linear_model import Ridge\n    m = Ridge(alpha=RR_ALPHA, fit_intercept=True)\n    m.fit(history(xz, RR_HIST).reshape(len(xz), -1), y)\n    return m.coef_.astype(np.float64), m.intercept_.astype(np.float64)\n\n\ndef rr_predict(model, xz):\n    W, b = model\n    return history(xz, RR_HIST).reshape(len(xz), -1) @ W.T + b\n\n\ndef r2_per_output(y, p):\n    from sklearn.metrics import r2_score\n    return np.array([r2_score(y[:, j], p[:, j]) for j in range(y.shape[1])])\n\n\ndef _lstm_modules(torch):\n    class LSTMModel(torch.nn.Module):\n        def __init__(self):\n            super().__init__()\n            self.lstm = torch.nn.LSTM(96, LSTM_HIDDEN, 1, batch_first=True)\n            self.fc = torch.nn.Linear(LSTM_HIDDEN, 4)\n\n        def forward(self, x):\n            o, _ = self.lstm(x)\n            return self.fc(o[:, -1])\n    return LSTMModel\n\n\ndef lstm_train(segments, seed=42, iters=LSTM_ITERS, init_state=None, out_norm=None, lr=LSTM_LR):\n    \"\"\"Train (or fine-tune, from init_state) the LSTM on a list of (xz, y) segments, xz already\n    normalised. Windows of 20 bins never cross a segment boundary. Batches of 64 are drawn without\n    replacement within an epoch, as the code's shuffled DataLoader does. Outputs are z-scored on\n    the training data unless out_norm is given (kept for fine-tuning). Noise: white noise of SD\n    NOISE_WHITE per bin and channel, and a bias of SD NOISE_BIAS per sequence and channel.\n    Returns (state_dict, out_norm).\"\"\"\n    import torch\n    torch.set_num_threads(1)\n    torch.manual_seed(seed)\n    rng = np.random.default_rng(seed)\n    X = np.concatenate([np.concatenate([np.zeros((LSTM_SEQ - 1, 96), np.float32), xz.astype(np.float32)])\n                        for xz, _ in segments])\n    Y = np.concatenate([y for _, y in segments]).astype(np.float64)\n    starts, off = [], 0\n    for xz, _ in segments:\n        starts.append(off + np.arange(len(xz)))\n        off += len(xz) + LSTM_SEQ - 1\n    starts = np.concatenate(starts)\n    if out_norm is None:\n        out_norm = zparams(Y)\n    Yz = ((Y - out_norm[0]) / out_norm[1]).astype(np.float32)\n    Xt = torch.from_numpy(X)\n    Yt = torch.from_numpy(Yz)\n    model = _lstm_modules(torch)()\n    if init_state is not None:\n        model.load_state_dict(init_state)\n    opt = torch.optim.Adam(model.parameters(), lr=lr[0], weight_decay=LSTM_WD)\n    sch = torch.optim.lr_scheduler.LinearLR(opt, start_factor=1.0, end_factor=lr[1] / lr[0], total_iters=iters)\n    ar = torch.arange(LSTM_SEQ)\n    it = 0\n    model.train()\n    while it < iters:\n        perm = rng.permutation(len(starts))\n        for b in range(0, len(perm), LSTM_BATCH):\n            if it >= iters:\n                break\n            sel = perm[b:b + LSTM_BATCH]\n            st = torch.from_numpy(starts[sel])\n            xb = Xt[st[:, None] + ar[None, :]]\n            xb = xb + NOISE_WHITE * torch.randn_like(xb) + NOISE_BIAS * torch.randn(xb.shape[0], 1, 96)\n            loss = torch.nn.functional.mse_loss(model(xb), Yt[sel])\n            opt.zero_grad()\n            loss.backward()\n            opt.step()\n            sch.step()\n            it += 1\n    return {k: v.detach().clone() for k, v in model.state_dict().items()}, out_norm\n\n\ndef lstm_predict(state, out_norm, xz: np.ndarray, every=1, batch=2048) -> np.ndarray:\n    \"\"\"Predictions at every `every`-th bin of a normalised segment, inverse-transformed to the\n    kinematics' units.\"\"\"\n    import torch\n    torch.set_num_threads(1)\n    model = _lstm_modules(torch)()\n    model.load_state_dict(state)\n    model.eval()\n    X = np.concatenate([np.zeros((LSTM_SEQ - 1, 96), np.float32), xz.astype(np.float32)])\n    idx = np.arange(0, len(xz), every)\n    Xt = torch.from_numpy(X)\n    ar = torch.arange(LSTM_SEQ)\n    out = []\n    with torch.no_grad():\n        for b in range(0, len(idx), batch):\n            st = torch.from_numpy(idx[b:b + batch])\n            out.append(model(Xt[st[:, None] + ar[None, :]]).numpy())\n    p = np.concatenate(out).astype(np.float64)\n    return p * out_norm[1] + out_norm[0]\n\n\ndef pool(n=None):\n    \"\"\"A process pool for LSTM fits, one linear-algebra thread per process.\"\"\"\n    from concurrent.futures import ProcessPoolExecutor\n    import multiprocessing as mp\n    os.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\n    return ProcessPoolExecutor(max_workers=n or min(4, os.cpu_count() or 1),\n                               mp_context=mp.get_context(\"spawn\"))\n"
}
```

```
File created successfully at: entries/temmar-2025/link.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/temmar-2025 && python3 - <<'EOF'
import re
s=open('link.py').read()
s=s.replace('''def read_session(asset_id: str, neural=True, tcr=True, kin=True) -> dict:''','''def read_session(asset_id: str, neural=True, tcr=True, kin=True, meta=False) -> dict:''')
s=s.replace('''        out["start"] = _str(f["session_start_time"][()])
    return out''','''        out["start"] = _str(f["session_start_time"][()])
        if meta:
            out["series"] = {n: {"shape": an[n]["data"].shape, "unit": _str(an[n]["data"].attrs.get("unit")),
                                 "conversion": float(an[n]["data"].attrs.get("conversion")),
                                 "n_timestamps": an[n]["timestamps"].shape[0],
                                 "same_t": bool(np.array_equal(an[n]["timestamps"][:], ts))}
                             for n in an}
            out["trial_columns"] = [_str(c) for c in tr.attrs["colnames"]]
            e = f["general/extracellular_ephys/electrodes"]
            out["electrodes"] = pd.DataFrame({k: [(_str(v) if isinstance(v, bytes) else v) for v in e[k][:]]
                                              for k in ("id", "array_name", "bank", "row", "col", "imp")})
    return out''')
open('link.py','w').write(s)
EOF
mkdir -p $TMPDIR/dev
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/nbbuild.py",
 "content": "\"\"\"Build a .ipynb from a percent-format script: '# %% [markdown]' cells hold markdown in\ncomment lines; '# %% tags=[\"a\",\"b\"]' gives tags.\"\"\"\nimport json, re, sys\nimport nbformat\n\nsrc, dst = sys.argv[1], sys.argv[2]\ntext = open(src).read()\ncells = []\nfor block in re.split(r\"^# %%\", text, flags=re.M)[1:]:\n    head, _, body = block.partition(\"\\n\")\n    tags = re.findall(r'\"([^\"]+)\"', head.split(\"tags=\")[1]) if \"tags=\" in head else []\n    if \"[markdown]\" in head:\n        lines = [l[2:] if l.startswith(\"# \") else l.lstrip(\"#\") for l in body.strip(\"\\n\").split(\"\\n\")]\n        c = nbformat.v4.new_markdown_cell(\"\\n\".join(lines).strip())\n    else:\n        c = nbformat.v4.new_code_cell(body.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\nnb = nbformat.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbformat.write(nb, dst)\nprint(\"wrote\", dst, len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude/nbbuild.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/nb1.py",
 "content": "# %% [markdown]\n# # Temmar et al. (2025), LINK: the dataset, neural signals and tuning over time\n#\n# Paper: Temmar, Gill, Wang et al., \"Long-term Intracortical Neural activity and Kinematics (LINK): An\n# intracortical neural dataset for chronic brain-machine interfaces, neuroscience, and machine learning\",\n# NeurIPS 2025 Datasets and Benchmarks, doi:10.52202/085713-4642.\n#\n# Dataset: DANDI:001201, version 0.261026.1912 (doi:10.48324/dandi.001201/0.261026.1912), streamed.\n# The paper cites no version, so the most recent published one is pinned. The dandiset has three\n# published versions (0.251023.2336, 0.261015.2153, 0.261026.1912); the cell below shows that the\n# three list the same 312 assets with the same asset identifiers, so the data the analysis uses do not\n# differ between them.\n#\n# Claims file: `claims/temmar-2025.yaml`, written from the version of record (NeurIPS proceedings) and\n# the supplement (Appendices A to C, Figures S1 to S6). Code read for method details:\n# github.com/chesteklab/LINK_dataset at commit 5e1c36a1282f90abb8d96963920a8b1fdd27a6e7.\n#\n# This notebook tests the claims on the dataset's contents, the neural signals over time (Figure 2,\n# S2, S4, S5) and single-channel tuning (Figure 3). The decoding claims (Figures 4 and 5) are in\n# `decoding.ipynb` and `multiday.ipynb`.\n#\n# | Claim | Notebook | Tested |\n# |---|---|---|\n# | dataset-sessions | this one | tested |\n# | dataset-contents | this one | tested |\n# | figs2-throughput-improves | this one | tested |\n# | fig2a-sbp-decline | this one | tested |\n# | fig2a-irregular-shifts | decoding.ipynb | tested |\n# | fig2b-active-channels-decrease | this one | tested |\n# | fig2c-pr-decline | this one | tested |\n# | fig2c-ten-dimensions | this one | tested |\n# | figs4-bank-slopes | this one | tested |\n# | figs5-active-inactive-slopes | this one | tested |\n# | fig2d-population-drift | this one | tested |\n# | fig2e-trajectories-separable | this one | tested |\n# | fig3b-two-channels | this one | tested |\n# | fig3cd-tuning-stable | this one | tested |\n# | fig3d-weak-channels-low-tcr | this one | tested |\n# | fig3e-array-tuning | this one | tested |\n# | fig4a-sameday-stable, fig4a-lstm-beats-rr, fig4bc-dof-accuracy, fig4d-cross-day-decay, suppc1-shuffle-baseline | decoding.ipynb | tested, the LSTM on a subset of sessions |\n# | fig5a-multiday-short-term, fig5a-long-term-decay | multiday.ipynb | tested on a subset of day-0 sessions |\n# | fig5b-finetune | multiday.ipynb | blocked, too large |\n\n# %%\nimport os, time, resource\nimport numpy as np\nimport pandas as pd\nimport requests\nimport matplotlib.pyplot as plt\nfrom concurrent.futures import ThreadPoolExecutor\nfrom scipy import stats\nfrom sklearn.decomposition import PCA\nimport link\n\nT0 = time.time()\nSUBSET = int(os.environ.get(\"LINK_SUBSET\", \"0\"))   # 0 = every session; set only while developing\nA = link.assets()\nprint(len(A), \"assets in version\", link.VERSION)\nmeta = link.version_metadata()\nprint(meta[\"name\"], \"|\", meta[\"doi\"])\nfor v in [\"0.251023.2336\", \"0.261015.2153\"]:\n    r = requests.get(f\"{link.API}/dandisets/{link.DANDISET}/versions/{v}/assets/?page_size=1000\", timeout=60).json()\n    old = {x[\"path\"]: x[\"asset_id\"] for x in r[\"results\"]}\n    same = sum(old.get(p) == a for p, a in zip(A[\"path\"], A[\"asset_id\"]))\n    print(f\"version {v}: {len(old)} assets, {same} with the same path and asset id as {link.VERSION}\")\n\n# %% [markdown]\n# ## What one file holds\n#\n# Everything in the first session file: its time series with shapes, units and conversion factors,\n# every column of the trials and electrodes tables, and the subject.\n\n# %%\nlay = link.read_layout(A[\"asset_id\"][0])\nprint(A[\"path\"][0])\nfor k, v in lay[\"series\"].items():\n    print(f\"  analysis/{k}: {v}\")\nprint(\"trials columns:\", lay[\"trial_columns\"], \"| rows:\", lay[\"n_trials\"])\nprint(lay[\"trials\"].head(3).to_string())\nprint(\"electrodes columns:\", list(lay[\"electrodes\"].columns))\nprint(lay[\"electrodes\"].head(4).to_string())\nprint(lay[\"electrodes\"].groupby([\"array_name\", \"bank\"]).size())\nprint(\"identifier:\", lay[\"identifier\"], \"| session_start_time:\", lay[\"session_start_time\"])\nprint(\"subject:\", lay[\"subject\"], \"| first timestamp:\", lay[\"first_t\"], \"s | bin steps:\", lay[\"dt\"])\n\n# %% [markdown]\n# ## One pass over the dataset\n#\n# Each file is streamed once and reduced to what the claims below use. Per session: the mean SBP and\n# TCR per channel, the sums for a whole-dataset PCA, the participation ratio of the active channels,\n# per-trial throughput, and checks of the contents. Per day (both sessions concatenated on two-session\n# days, as `signal_utils.calc_avg_sbps` and the tuning code do): the mean SBP per channel, the tuning\n# of each channel, and the per-day PCA trajectories of Figure 2E.\n\n# %%\ndef trial_bounds(sess):\n    ti = sess[\"trial_index\"]\n    return ti, np.append(ti[1:], len(sess[\"t\"]))\n\n\ndef trajectories(sessions, pcs_day):\n    \"\"\"Per-trial 3-PC trajectories for the two alignment readings of fig2e (claim criterion).\"\"\"\n    out = []\n    off = 0\n    for s in sessions:\n        st, en = trial_bounds(s)\n        cls = link.trial_directions(s[\"trials\"])\n        for i in range(len(st)):\n            if cls[i] < 0:\n                continue\n            v = s[\"kin\"][st[i]:en[i], 3 if link.mrs_dominant(cls[i]) else 2].astype(float)\n            rec = {\"date\": s[\"date\"], \"cls\": int(cls[i]), \"style\": s[\"style\"]}\n            for name, k, pre, n in ((\"main\", 1.0, 0, 37), (\"code\", 2.0, 7, 37)):\n                on, al = link.onset_and_jerk(v, k)\n                a0 = None if al is None else al - pre\n                if a0 is None or a0 < 0 or a0 + n > en[i] - st[i]:\n                    rec[name] = None\n                else:\n                    rec[name] = pcs_day[off + st[i] + a0: off + st[i] + a0 + n].astype(np.float32)\n            out.append(rec)\n        off += len(s[\"t\"])\n    return out\n\n\ndef reduce_day(rows):\n    sessions = []\n    for _, r in rows.iterrows():\n        s = link.read_session(r[\"asset_id\"], meta=True)\n        s[\"date\"] = r[\"date\"]\n        s[\"path\"] = r[\"path\"]\n        sessions.append(s)\n    recs = []\n    for s in sessions:\n        x = s[\"sbp\"].astype(np.float64)\n        tc = s[\"tcr\"] * link.TCR_TO_HZ\n        act = tc.mean(0) > 1\n        pr, ev = link.participation_ratio(s[\"sbp\"][:, act]) if act.any() else (np.nan, np.array([]))\n        dpos = np.diff(s[\"kin\"][:, :2].astype(float), axis=0)\n        st, en = trial_bounds(s)\n        recs.append({\n            \"date\": s[\"date\"], \"path\": s[\"path\"], \"style\": s[\"style\"], \"identifier\": s[\"identifier\"],\n            \"start\": s[\"start\"], \"n_trials\": len(s[\"trials\"]), \"n_bins\": len(s[\"t\"]),\n            \"styles_in_trials\": sorted(set(s[\"trials\"][\"target_style\"])),\n            \"dt\": np.unique(np.round(np.diff(s[\"t\"]), 3)),\n            \"t_first\": s[\"t\"][0], \"t_last\": s[\"t\"][-1],\n            \"series\": s[\"series\"], \"trial_columns\": s[\"trial_columns\"], \"electrodes\": s[\"electrodes\"],\n            \"sbp_mean\": x.mean(0), \"sbp_sum\": x.sum(0), \"sbp_xx\": x.T @ x,\n            \"sbp_min\": float(x.min()), \"sbp_max\": float(x.max()),\n            \"tcr_hz\": tc.mean(0), \"tcr_max_count\": float(s[\"tcr\"].max()),\n            \"tcr_integer\": bool(np.all(s[\"tcr\"] == np.round(s[\"tcr\"]))),\n            \"kin_min\": s[\"kin\"].min(0), \"kin_max\": s[\"kin\"].max(0),\n            \"vel_vs_diff\": [float(np.max(np.abs(s[\"kin\"][1:, 2 + j] - dpos[:, j]))) for j in range(2)],\n            \"vel_vs_diff_lag\": [float(np.max(np.abs(s[\"kin\"][:-1, 2 + j] - dpos[:, j]))) for j in range(2)],\n            \"trial_len_vs_count\": float(np.max(np.abs((en - st) - s[\"trials\"][\"trial_count\"].to_numpy()))),\n            \"trial_dur_s\": (s[\"trials\"][\"stop_time\"] - s[\"trials\"][\"start_time\"]).to_numpy(),\n            \"trial_count_s\": s[\"trials\"][\"trial_count\"].to_numpy() * link.BIN_S,\n            \"active\": act, \"pr\": pr, \"ev\": ev,\n            \"tp\": {k: link.throughput(s[\"trials\"], k) for k in \"abc\"},\n            \"timeout\": s[\"trials\"][\"trial_timeout\"].to_numpy(),\n            \"target_min\": s[\"trials\"][[\"index_target_position\", \"mrs_target_position\"]].min().to_numpy(),\n            \"target_max\": s[\"trials\"][[\"index_target_position\", \"mrs_target_position\"]].max().to_numpy(),\n        })\n    sbp = np.concatenate([s[\"sbp\"] for s in sessions]).astype(np.float64)\n    pos = np.concatenate([s[\"kin\"][:, :2] for s in sessions])\n    tun = link.channel_tuning(sbp, pos)\n    z = (sbp - sbp.mean(0)) / np.where(sbp.std(0) > 1e-8, sbp.std(0), 1)\n    pcs = PCA(3).fit_transform(z)\n    day = {\"date\": sessions[0][\"date\"], \"sbp_mean\": sbp.mean(0), \"tuning\": tun,\n           \"tcr_hz\": np.concatenate([s[\"tcr\"] for s in sessions]).mean(0) * link.TCR_TO_HZ,\n           \"traj\": trajectories(sessions, pcs)}\n    return recs, day\n\n\ngroups = [g for _, g in A.groupby(\"date\")]\nif SUBSET:\n    groups = groups[:: max(1, len(groups) // SUBSET)][:SUBSET]\nt = time.time()\nwith ThreadPoolExecutor(4) as ex:\n    results = list(ex.map(reduce_day, groups))\nS = pd.DataFrame([r for rs, _ in results for r in rs]).sort_values([\"date\", \"style\"]).reset_index(drop=True)\nD = pd.DataFrame([d for _, d in results]).sort_values(\"date\").reset_index(drop=True)\nprint(f\"{len(S)} sessions on {len(D)} days read in {time.time() - t:.0f} s; \"\n      f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nfirst = S[\"date\"].min()\nS[\"day\"] = (S[\"date\"] - first).dt.days\nD[\"day\"] = (D[\"date\"] - first).dt.days\nprint(\"subjects: 1 (Monkey N) in every file:\", lay[\"subject\"])\nprint(\"sessions by style:\", S[\"style\"].value_counts().to_dict())\nprint(\"sessions by year:\", S[\"date\"].dt.year.value_counts().sort_index().to_dict())\nprint(\"styles inside each file's trials table equal to its file style:\",\n      all(r[\"styles_in_trials\"] == [r[\"style\"]] for _, r in S.iterrows()))\nprint(\"trials per session:\", S[\"n_trials\"].value_counts().to_dict())\nprint(\"bins per session: min\", S[\"n_bins\"].min(), \"max\", S[\"n_bins\"].max())\nprint(\"timestamp steps (s) seen:\", sorted(set(np.concatenate(S[\"dt\"].to_list()).round(3))))\nprint(\"first timestamp per session (s): min %.3f max %.3f\" % (S[\"t_first\"].min(), S[\"t_first\"].max()))\nprint(\"session_start_time is midnight of the file date:\",\n      all(pd.Timestamp(r[\"start\"]).tz_localize(None) == r[\"date\"] for _, r in S.iterrows()))\nunits = {(k, v[\"unit\"], v[\"conversion\"]) for sr in S[\"series\"] for k, v in sr.items()}\nprint(\"series, unit, conversion (all files):\", sorted(units))\nprint(\"every series shares the SBP timestamps:\", all(v[\"same_t\"] for sr in S[\"series\"] for v in sr.values()))\nprint(\"SBP range over all bins: %.3f to %.3f (file values)\" % (S[\"sbp_min\"].min(), S[\"sbp_max\"].max()))\nprint(\"TCR counts per bin are integers:\", S[\"tcr_integer\"].all(), \"| max count per bin\", S[\"tcr_max_count\"].max())\nkm = np.vstack(S[\"kin_min\"]).min(0); kx = np.vstack(S[\"kin_max\"]).max(0)\nfor n, a, b in zip(link.KIN_NAMES, km, kx):\n    print(f\"  {n}: {a:.3f} to {b:.3f}\")\ntmin = np.vstack(S[\"target_min\"]).min(0); tmax = np.vstack(S[\"target_max\"]).max(0)\nprint(\"target positions IDX %.2f to %.2f, MRS %.2f to %.2f\" % (tmin[0], tmax[0], tmin[1], tmax[1]))\nprint(\"trial timeouts (ms):\", sorted(set(np.concatenate(S[\"timeout\"].to_list()))))\nprint(\"largest |trial bins from trial_index - trial_count| over sessions:\", S[\"trial_len_vs_count\"].max())\ndd = np.concatenate([a - b for a, b in zip(S[\"trial_dur_s\"], S[\"trial_count_s\"])])\nprint(\"stop - start minus trial_count x 20 ms (s): median %.3f, range %.3f to %.3f\" % (np.median(dd), dd.min(), dd.max()))\nel0 = S[\"electrodes\"].iloc[0]\nsame_layout = all((e[[\"id\", \"array_name\", \"bank\", \"row\", \"col\"]].values == el0[[\"id\", \"array_name\", \"bank\", \"row\", \"col\"]].values).all() for e in S[\"electrodes\"])\nprint(\"electrode layout identical in every file:\", same_layout)\nimp = np.vstack([e[\"imp\"].to_numpy(float) for e in S[\"electrodes\"]])\nprint(\"impedance (ohm): %d of %d values NaN, range %.0f to %.0f\" % (np.isnan(imp).sum(), imp.size, np.nanmin(imp), np.nanmax(imp)))\nprint(\"sessions whose impedances are all NaN:\", int(np.isnan(imp).all(1).sum()))\nprint(\"velocity minus difference of positions, max over sessions (velocity[t] vs pos[t]-pos[t-1]):\",\n      np.round(np.vstack(S[\"vel_vs_diff\"]).max(0), 4),\n      \"| (velocity[t] vs pos[t+1]-pos[t]):\", np.round(np.vstack(S[\"vel_vs_diff_lag\"]).max(0), 4))\n\n# %% [markdown]\n# Clock check. The behaviour and neural series share one timestamp vector in every file (above). To\n# check that the neural data and the trial table share a clock, the next cell decodes the movement\n# direction class of each trial from the mean SBP of the 0 to 500 ms after its start, with the trial\n# table as stored and with the start times shifted by whole trials (labels from trial i paired with the\n# neural data of trial i + k). Nearest-centroid, 5-fold cross-validation, per session, on a few sessions.\n\n# %%\ndef clock_check(asset_id, shifts=(0, 1, 2, 5)):\n    s = link.read_session(asset_id, tcr=False, kin=False)\n    st = s[\"trial_index\"]\n    cls = link.trial_directions(s[\"trials\"])\n    X = np.array([s[\"sbp\"][a:a + 25].mean(0) for a in st])\n    X = (X - X.mean(0)) / X.std(0)\n    out = {}\n    for k in shifts:\n        y = cls[: len(cls) - k] if k else cls\n        Xk = X[k:]\n        ok = y >= 0\n        out[k] = nc_cv_accuracy(Xk[ok], y[ok], np.random.default_rng(0))\n    return out\n\n\ndef nc_cv_accuracy(X, y, rng, folds=5):\n    idx = rng.permutation(len(y))\n    correct = 0\n    for f in range(folds):\n        te = idx[f::folds]\n        tr = np.setdiff1d(idx, te)\n        labs = np.unique(y[tr])\n        cent = np.array([X[tr][y[tr] == c].mean(0) for c in labs])\n        pred = labs[np.argmin(((X[te][:, None, :] - cent[None]) ** 2).sum(-1), axis=1)]\n        correct += (pred == y[te]).sum()\n    return correct / len(y)\n\n\nchk = S.groupby(\"date\").head(1).iloc[np.linspace(0, len(S.groupby(\"date\").head(1)) - 1, 6).astype(int)]\nfor _, r in chk.iterrows():\n    aid = A.set_index(\"path\").loc[r[\"path\"], \"asset_id\"]\n    print(r[\"date\"].date(), r[\"style\"], {k: round(v, 3) for k, v in clock_check(aid).items()})\n\n# %% [markdown]\n# ## dataset-sessions\n#\n# > The dataset holds 312 sessions recorded on 303 days spanning 1,242 days, two sessions (one CO, one\n# > RD) on 9 days, each session 375 successful trials, from days 349 to 1591 after implant.\n\n# %% tags=[\"claim:dataset-sessions\"]\nper_day = S.groupby(\"date\")[\"style\"].apply(lambda s: \"+\".join(sorted(s)))\ntwo = per_day[per_day.str.contains(r\"\\+\")]\nspan = (S[\"date\"].max() - S[\"date\"].min()).days\nprint(\"sessions (files):\", len(S))\nprint(\"recording days:\", S[\"date\"].nunique())\nprint(\"span, last minus first date:\", span, \"days;\", S[\"date\"].min().date(), \"to\", S[\"date\"].max().date())\nprint(\"days with two sessions:\", len(two), \"| their styles:\", two.value_counts().to_dict())\nprint(\"sessions with a trial count other than 375:\", S.loc[S[\"n_trials\"] != 375, [\"date\", \"style\", \"n_trials\"]].to_dict(\"records\"))\nprint(\"implant date in the files or the dandiset metadata: none (the subject has only a date of birth,\",\n      lay[\"subject\"][\"date_of_birth\"], \")\")\n\n# %% [markdown]\n# ## dataset-contents\n#\n# > Each session holds SBP and TCR for 96 motor-cortex channels and the position and velocity of the two\n# > finger groups in 20 ms bins, with per-trial target positions, start times, lengths and target style,\n# > and per-channel array locations and impedances.\n\n# %% tags=[\"claim:dataset-contents\"]\nneed_series = {\"SpikingBandPower\": 96, \"ThresholdCrossings\": 96, \"index_position\": 1, \"index_velocity\": 1,\n               \"mrs_position\": 1, \"mrs_velocity\": 1}\nneed_trials = [\"start_time\", \"stop_time\", \"trial_number\", \"trial_count\", \"run_id\", \"index_target_position\",\n               \"mrs_target_position\", \"target_style\", \"trial_timeout\", \"timeseries\"]\ngaps = []\nfor _, r in S.iterrows():\n    for n, ch in need_series.items():\n        v = r[\"series\"].get(n)\n        if v is None or v[\"shape\"][1] != ch or v[\"shape\"][0] != r[\"n_bins\"]:\n            gaps.append((r[\"path\"], n))\n    miss = [c for c in need_trials if c not in r[\"trial_columns\"]]\n    if miss:\n        gaps.append((r[\"path\"], \"trials \" + \",\".join(miss)))\n    if not {\"array_name\", \"bank\", \"row\", \"col\", \"imp\"} <= set(r[\"electrodes\"].columns):\n        gaps.append((r[\"path\"], \"electrodes\"))\nsteps = np.concatenate(S[\"dt\"].to_list())\nprint(\"files checked:\", len(S), \"| files with a missing part:\", len({g[0] for g in gaps}), gaps[:5])\nprint(\"timestamp steps (s):\", sorted(set(steps.round(3))), \"(all within 1 ms of 0.02)\")\nprint(\"velocity equals pos[t] - pos[t-1] to within\", np.round(np.vstack(S[\"vel_vs_diff\"]).max(0), 5))\n\n# %% [markdown]\n# ## figs2-throughput-improves\n#\n# > The monkey's real-time task performance, measured as average Fitts' law throughput per day, appears to\n# > improve gradually over the dataset.\n#\n# Readings (a), (b), (c) of the criterion; per day the mean over all trials of both sessions; the first\n# trial of each session has no previous target in the file and is left out.\n\n# %% tags=[\"claim:figs2-throughput-improves\"]\ntp_rows = []\nfor k in \"abc\":\n    daily = S.groupby(\"day\")[\"tp\"].apply(lambda col: np.nanmean(np.concatenate([d[k] for d in col])))\n    r = link.linfit(daily.index, daily.values)\n    tp_rows.append({\"reading\": k, \"days\": len(daily), \"first 30 days mean\": daily.iloc[:30].mean(),\n                    \"last 30 days mean\": daily.iloc[-30:].mean(), \"slope bits/s per year\": r.slope * 365.25,\n                    \"r\": r.rvalue, \"p\": r.pvalue})\n    by_year = daily.groupby((first + pd.to_timedelta(daily.index, \"D\")).year).mean().round(3).to_dict()\n    print(k, \"mean per year:\", by_year)\nprint(pd.DataFrame(tp_rows).to_string(index=False))\nnonpos = sum(int(np.sum((t[\"a\"][1:] <= 0) | ~np.isfinite(t[\"a\"][1:]))) for t in S[\"tp\"])\nprint(\"trials with acquisition time <= 0 under reading (a):\", nonpos)\n\n# %% [markdown]\n# ## fig2a-sbp-decline\n#\n# > Average SBP across channels decreased gradually by about 0.033 microvolts per month, as estimated by a\n# > linear model fit to every channel's mean SBP on every day.\n\n# %% tags=[\"claim:fig2a-sbp-decline\"]\nM = np.vstack(D[\"sbp_mean\"])        # days x channels, file units\ndayx = np.repeat(D[\"day\"].to_numpy(), 96)\nres = {}\nfor name, scale in ((\"(a) x0.25\", link.SBP_CODE_SCALE), (\"(b) as stored\", 1.0)):\n    r = link.linfit(dayx, (M * scale).ravel())\n    res[name] = r\n    print(f\"{name}: slope {r.slope:.3e} per day = {r.slope * link.DAYS_PER_MONTH:.4f} per month, \"\n          f\"intercept {r.intercept:.3f}, p = {r.pvalue:.2g}, points {len(dayx)}\")\nprint(\"mean SBP over channels, first and last 30 days (file units): %.3f, %.3f\" % (M[:30].mean(), M[-30:].mean()))\nprint(\"channel-day values (file units): %.3f to %.3f; values above 10: %d\" % (M.min(), M.max(), (M > 10).sum()))\nfig, ax = plt.subplots(figsize=(8, 3))\nax.scatter(D[\"date\"].repeat(96), M.ravel(), s=1, alpha=.3)\nax.plot(D[\"date\"], res[\"(b) as stored\"].intercept + res[\"(b) as stored\"].slope * D[\"day\"], \"r\")\nax.set_ylim(0, 10); ax.set_ylabel(\"mean SBP (file units)\")\nplt.show()\n\n# %% [markdown]\n# ## fig2b-active-channels-decrease\n#\n# > The number of active channels, those with mean TCR above 1 Hz on a day, appears to decrease over time.\n#\n# CO session on two-session days, the day's only session otherwise.\n\n# %% tags=[\"claim:fig2b-active-channels-decrease\"]\nP = S.sort_values([\"date\", \"style\"]).groupby(\"date\").head(1).reset_index(drop=True)   # \"CO\" sorts before \"RD\"\nP[\"n_active\"] = [a.sum() for a in P[\"active\"]]\nr = link.linfit(P[\"day\"], P[\"n_active\"])\nprint(f\"days {len(P)}; slope {r.slope:.4f} channels per day ({r.slope * 365.25:.1f} per year), r = {r.rvalue:.3f}, p = {r.pvalue:.2g}\")\nprint(\"active channels, first 30 sessions: mean %.1f (range %d to %d); last 30: mean %.1f (range %d to %d)\" % (\n    P[\"n_active\"][:30].mean(), P[\"n_active\"][:30].min(), P[\"n_active\"][:30].max(),\n    P[\"n_active\"][-30:].mean(), P[\"n_active\"][-30:].min(), P[\"n_active\"][-30:].max()))\nprint(\"days with no active channel:\", int((P[\"n_active\"] == 0).sum()))\n\n# %% [markdown]\n# ## fig2c-pr-decline\n#\n# > The participation ratio of the active channels' SBP decreased by about 0.07 per month, as estimated by\n# > a linear model.\n\n# %% tags=[\"claim:fig2c-pr-decline\"]\nok = np.isfinite(P[\"pr\"])\nr = link.linfit(P[\"day\"][ok], P[\"pr\"][ok])\nprint(f\"CO session on two-session days: days {ok.sum()}, slope {r.slope * link.DAYS_PER_MONTH:.4f} PR per month, p = {r.pvalue:.2g}\")\nprint(\"PR first 30 days mean %.2f, last 30 mean %.2f, range %.2f to %.2f\" % (P[\"pr\"][ok][:30].mean(), P[\"pr\"][ok][-30:].mean(), P[\"pr\"][ok].min(), P[\"pr\"][ok].max()))\n# variant: both sessions on two-session days (PR of the concatenated active-channel SBP is not kept;\n# the variant uses each session as a point)\nok2 = np.isfinite(S[\"pr\"])\nr2 = link.linfit(S[\"day\"][ok2], S[\"pr\"][ok2])\nprint(f\"variant, every session a point: sessions {ok2.sum()}, slope {r2.slope * link.DAYS_PER_MONTH:.4f} PR per month, p = {r2.pvalue:.2g}\")\n\n# %% [markdown]\n# ## fig2c-ten-dimensions\n#\n# > Generally, 10 dimensions were sufficient to capture the majority of the variance of the active channels.\n\n# %% tags=[\"claim:fig2c-ten-dimensions\"]\nfrac10 = np.array([ev[:10].sum() / ev.sum() if len(ev) else np.nan for ev in P[\"ev\"]])\nokd = np.isfinite(frac10)\nprint(\"days:\", okd.sum())\nprint(\"(a) PR <= 10 on %.3f of days (median PR %.2f)\" % ((P[\"pr\"][okd] <= 10).mean(), P[\"pr\"][okd].median()))\nprint(\"(b) top 10 PCs explain > 50%% on %.3f of days\" % (frac10[okd] > 0.5).mean())\nprint(\"(c) top 10 PCs explain > 80%% on %.3f of days\" % (frac10[okd] > 0.8).mean())\nprint(\"variance explained by 10 PCs: median %.3f, range %.3f to %.3f\" % (np.median(frac10[okd]), frac10[okd].min(), frac10[okd].max()))\nprint(\"days with 10 or fewer active channels (10 PCs explain all):\", int((P[\"n_active\"][okd] <= 10).sum()))\n\n# %% [markdown]\n# ## figs4-bank-slopes\n#\n# > Mean SBP decreases over time in each 32-channel bank, with lower overall activity and a shallower slope on\n# > the lateral bank (-0.58e-3) than on the two medial banks (-1.34e-3 and -1.40e-3), against -1.11e-3 for all\n# > channels.\n#\n# Banks from the electrodes table: bank A is on the lateral array, B and C on the medial array; Medial 1 is\n# taken as bank B and Medial 2 as bank C (the paper does not say which is which; both medial values are\n# shown).\n\n# %% tags=[\"claim:figs4-bank-slopes\"]\nel = S[\"electrodes\"].iloc[0]\nprint(el.groupby([\"bank\", \"array_name\"]).size().to_dict())\ngroups_b = {\"Lateral (A)\": el[\"bank\"].eq(\"A\").to_numpy(), \"Medial 1 (B)\": el[\"bank\"].eq(\"B\").to_numpy(),\n            \"Medial 2 (C)\": el[\"bank\"].eq(\"C\").to_numpy(), \"all\": np.ones(96, bool)}\nrows = []\nfor scale_name, scale in ((\"(a) x0.25\", 0.25), (\"(b) as stored\", 1.0)):\n    for fit in (\"(a) channel-day points\", \"(b) daily bank mean\"):\n        for g, m in groups_b.items():\n            Y = M[:, m] * scale\n            if fit.startswith(\"(a)\"):\n                r = link.linfit(np.repeat(D[\"day\"].to_numpy(), m.sum()), Y.ravel())\n            else:\n                r = link.linfit(D[\"day\"], Y.mean(1))\n            rows.append({\"unit\": scale_name, \"fit\": fit, \"group\": g, \"slope per day\": r.slope, \"mean SBP\": Y.mean()})\nT4 = pd.DataFrame(rows)\nprint(T4.pivot_table(index=[\"unit\", \"fit\"], columns=\"group\", values=\"slope per day\").map(lambda v: f\"{v:.2e}\").to_string())\nprint(T4[T4[\"fit\"].str.startswith(\"(a)\")].pivot_table(index=\"unit\", columns=\"group\", values=\"mean SBP\").round(3).to_string())\n\n# %% [markdown]\n# ## figs5-active-inactive-slopes\n#\n# > Grouped per session into active and inactive channels by TCR, mean SBP of active channels declines faster\n# > (-1.29e-3) than all channels, while the slope for inactive channels is near zero (0.54e-3), and inactive\n# > channels have lower SBP.\n#\n# Each session classifies its own channels (mean TCR above 1 Hz in the session), and each session is a point.\n\n# %% tags=[\"claim:figs5-active-inactive-slopes\"]\nrows = []\nSM = np.vstack(S[\"sbp_mean\"])\nAM = np.vstack(S[\"active\"])\nfor scale_name, scale in ((\"(a) x0.25\", 0.25), (\"(b) as stored\", 1.0)):\n    for g, mask in ((\"active\", AM), (\"inactive\", ~AM)):\n        xs = np.repeat(S[\"day\"].to_numpy()[:, None], 96, 1)[mask]\n        ys = (SM * scale)[mask]\n        ra = link.linfit(xs, ys)\n        okg = mask.any(1)\n        gm = np.array([(SM[i, mask[i]] * scale).mean() for i in np.where(okg)[0]])\n        rb = link.linfit(S[\"day\"][okg], gm)\n        rows.append({\"unit\": scale_name, \"group\": g, \"(a) channel-session slope\": ra.slope,\n                     \"(b) session-mean slope\": rb.slope, \"mean SBP\": ys.mean(), \"sessions with group\": okg.sum()})\nprint(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f\"{v:.3e}\"))\n\n# %% [markdown]\n# ## fig2d-population-drift\n#\n# > In a PCA fit to SBP z-scored per channel across the whole dataset, the per-day and per-quarter centroids of\n# > the top 3 PCs move through PC space over time, while the standard deviation of the top 3 PCs per quarter\n# > changes little except in two quarters.\n#\n# The PCA of the whole-dataset z-scored SBP is computed from per-session sums (the mean and covariance of all\n# bins), which gives the same components as fitting scikit-learn's PCA to the concatenated matrix. Centroids\n# and per-quarter standard deviations of the scores follow from the same sums.\n\n# %% tags=[\"claim:fig2d-population-drift\"]\nN = S[\"n_bins\"].sum()\nmu = np.vstack(S[\"sbp_sum\"]).sum(0) / N\nC = sum(S[\"sbp_xx\"]) / N - np.outer(mu, mu)\nsd = np.sqrt(np.diag(C))\nR = C / np.outer(sd, sd)\nw, V = np.linalg.eigh(R)\norder = np.argsort(w)[::-1]\nW = V[:, order[:3]]\nprint(\"variance explained by PC1-3 (z-scored):\", np.round(w[order[:3]] / w.sum(), 3))\nS[\"quarter\"] = S[\"date\"].dt.to_period(\"Q\")\ncent_day = np.array([W.T @ ((r[\"sbp_sum\"] / r[\"n_bins\"] - mu) / sd) for _, r in S.iterrows()])\nqrows = []\nfor q, g in S.groupby(\"quarter\"):\n    n = g[\"n_bins\"].sum()\n    m = np.vstack(g[\"sbp_sum\"]).sum(0) / n\n    Cq = sum(g[\"sbp_xx\"]) / n - np.outer(m, m)\n    Cz = Cq / np.outer(sd, sd)\n    sds = np.sqrt(np.diag(W.T @ Cz @ W))\n    qrows.append({\"quarter\": str(q), \"sessions\": len(g), \"centroid\": W.T @ ((m - mu) / sd), \"sd_pc\": sds,\n                  \"sd_rms\": float(np.sqrt(np.mean(sds ** 2)))})\nQ = pd.DataFrame(qrows)\nfor _, q in Q.iterrows():\n    print(q[\"quarter\"], q[\"sessions\"], \"centroid\", np.round(q[\"centroid\"], 3), \"sd\", np.round(q[\"sd_pc\"], 3), \"rms %.3f\" % q[\"sd_rms\"])\nmove = np.linalg.norm(Q[\"centroid\"].iloc[-1] - Q[\"centroid\"].iloc[0])\nprint(\"distance first to last quarter centroid: %.3f; mean within-quarter SD (rms over 3 PCs): %.3f\" % (move, Q[\"sd_rms\"].mean()))\nmed = Q[\"sd_rms\"].median()\nfar = Q[np.abs(Q[\"sd_rms\"] - med) > 0.25 * med]\nprint(\"quarters with SD more than 25%% from the median (%.3f): %d %s\" % (med, len(far), far[\"quarter\"].tolist()))\nfor thr in (0.15, 0.25, 0.5):\n    print(f\"  at {int(thr*100)}%: {int((np.abs(Q['sd_rms'] - med) > thr * med).sum())} quarters\")\nprint(\"per-day centroid range per PC:\", np.round(cent_day.min(0), 2), np.round(cent_day.max(0), 2))\nprint(\"path length of quarter centroids: %.3f\" % np.sum(np.linalg.norm(np.diff(np.vstack(Q[\"centroid\"]), axis=0), axis=1)))\n\n# %% [markdown]\n# ## fig2e-trajectories-separable\n#\n# > Average neural trajectories in the top 3 PCs for the eight movement directions remain visually separable in\n# > both the first year (2020) and the last (2023) of the dataset.\n\n# %% tags=[\"claim:fig2e-trajectories-separable\"]\nTR = pd.DataFrame([t for d in D[\"traj\"] for t in d])\nTR[\"year\"] = pd.to_datetime(TR[\"date\"]).dt.year\nprint(\"trials with a direction:\", len(TR), \"| by class:\", TR[\"cls\"].value_counts().sort_index().to_dict())\nfor name in (\"main\", \"code\"):\n    print(f\"alignment {name}: trials dropped (no onset or window outside the trial): {TR[name].isna().sum()} of {len(TR)}\")\n    for yr in (2020, 2023):\n        g = TR[(TR[\"year\"] == yr) & TR[name].notna()]\n        X = np.stack([a.ravel() for a in g[name]])\n        y = g[\"cls\"].to_numpy()\n        acc = nc_cv_accuracy(X, y, np.random.default_rng(yr))\n        k = int(round(acc * len(y)))\n        p = stats.binomtest(k, len(y), 1 / 8, alternative=\"greater\").pvalue\n        maj = g[\"cls\"].value_counts(normalize=True).max()\n        # null: labels permuted\n        accn = nc_cv_accuracy(X, np.random.default_rng(1).permutation(y), np.random.default_rng(yr))\n        print(f\"  {yr}: trials {len(y)}, days {g['date'].nunique()}, accuracy {acc:.3f} (chance 1/8, \"\n              f\"majority class {maj:.3f}, permuted labels {accn:.3f}), binomial p = {p:.2g}\")\n\n# %% [markdown]\n# ## Tuning (fig3b, fig3cd, fig3d, fig3e)\n\n# %%\nTUN = np.stack(D[\"tuning\"])                     # days x channels x (idx, mrs)\nANG = np.arctan2(TUN[..., 1], TUN[..., 0])      # 0 = IDX flexion, 90 deg = MRS flexion\nSTR = np.linalg.norm(TUN, axis=2)\ncmed = np.array([link.circ_median(ANG[:, c]) for c in range(96)])\nciqr = np.array([link.circ_iqr(ANG[:, c]) for c in range(96)])\nsmed = np.median(STR, 0)\nTCRD = np.vstack(D[\"tcr_hz\"])                   # days x channels, Hz\ntcr_mean = TCRD.mean(0)\nact_ds = tcr_mean > 1\nprint(\"tuning strength over all channel-days: 1%%, 99%% quantiles %.4f, %.4f (paper's axis 0 to 0.06)\" % tuple(np.percentile(STR, [1, 99])))\nprint(\"channels active over the dataset (mean TCR > 1 Hz):\", act_ds.sum())\n\n# %% [markdown]\n# ### fig3b-two-channels\n#\n# > Channel 7 is strongly tuned to MRS flexion throughout the dataset, whereas channel 32 shows large shifts in\n# > tuning angle; both are active, with average TCR above 1 Hz across the dataset.\n\n# %% tags=[\"claim:fig3b-two-channels\"]\nfor c in (7, 32):\n    print(f\"channel {c}: array {el['array_name'][c]}, bank {el['bank'][c]}; circular median angle {np.degrees(cmed[c]):.1f} deg, \"\n          f\"circular IQR {np.degrees(ciqr[c]):.1f} deg, median strength {smed[c]:.4f}, mean TCR {tcr_mean[c]:.2f} Hz\")\nprint(\"over channels: median strength %.4f, median circular IQR %.1f deg\" % (np.median(smed), np.degrees(np.median(ciqr))))\nprint(\"rank of channel 7's median strength: %d of 96\" % (1 + (smed > smed[7]).sum()))\nprint(\"rank of channel 32's circular IQR: %d of 96\" % (1 + (ciqr > ciqr[32]).sum()))\n\n# %% [markdown]\n# ### fig3cd-tuning-stable\n#\n# > Per-channel tuning angles generally appear consistent through the dataset; in most channels the circular IQR\n# > of tuning angle is small, so their tunings did not change much.\n\n# %% tags=[\"claim:fig3cd-tuning-stable\"]\nfor lim in (45, 90):\n    for lab, m in ((\"(i) all 96\", np.ones(96, bool)), (\"(ii) active\", act_ds)):\n        f = (np.degrees(ciqr[m]) < lim).mean()\n        print(f\"circular IQR < {lim} deg, {lab} ({m.sum()} channels): fraction {f:.3f}\")\nprint(\"circular IQR quantiles (deg) 10/25/50/75/90:\", np.round(np.degrees(np.percentile(ciqr, [10, 25, 50, 75, 90])), 1))\n\n# %% [markdown]\n# ### fig3d-weak-channels-low-tcr\n#\n# > Many channels have very low tuning strength throughout the arrays' lifespan, and such channels typically have\n# > low average TCR per day.\n\n# %% tags=[\"claim:fig3d-weak-channels-low-tcr\"]\ntcr_med = np.median(TCRD, 0)\nrho, p = stats.spearmanr(smed, tcr_med)\nlow = smed <= np.percentile(smed, 25)\nu = stats.mannwhitneyu(tcr_med[low], tcr_med[~low], alternative=\"two-sided\")\nprint(f\"Spearman rho (median strength vs median daily TCR, 96 channels) = {rho:.3f}, p = {p:.2g}\")\nprint(f\"lowest-quartile strength channels ({low.sum()}): median TCR {np.median(tcr_med[low]):.2f} Hz; \"\n      f\"others ({(~low).sum()}): {np.median(tcr_med[~low]):.2f} Hz; Mann-Whitney U = {u.statistic:.0f}, p = {u.pvalue:.2g}\")\nprint(\"median strength quantiles 0/25/50/75/100:\", np.round(np.percentile(smed, [0, 25, 50, 75, 100]), 4))\n\n# %% [markdown]\n# ### fig3e-array-tuning\n#\n# > Channels on the medial array are mainly tuned to MRS flexion, with some to IDX flexion, while channels on the\n# > lateral array are more tuned to extension of both fingers, so channels on the same array tend to have similar\n# > tuning angles.\n\n# %% tags=[\"claim:fig3e-array-tuning\"]\ndeg = np.degrees(cmed)\nmed_arr = el[\"array_name\"].eq(\"Medial\").to_numpy()\ndef within(a, c, h):\n    return np.abs(((a - c + 180) % 360) - 180) <= h\nfor lab, m in ((\"all channels\", np.ones(96, bool)), (\"active channels\", act_ds)):\n    mm, ll = med_arr & m, ~med_arr & m\n    in_flex = within(deg[mm], 45, 67.5)          # -22.5 to 112.5\n    near90, near0 = within(deg[mm], 90, 45).sum(), within(deg[mm], 0, 45).sum()\n    in_ext = within(deg[ll], -135, 67.5)         # -202.5 to -67.5\n    print(f\"{lab}: medial {mm.sum()} channels, {in_flex.mean():.3f} in -22.5..112.5 deg, {near90} within 45 deg of 90, \"\n          f\"{near0} within 45 deg of 0; lateral {ll.sum()} channels, {in_ext.mean():.3f} in -202.5..-67.5 deg\")\nprint(\"lateral circular medians (deg):\", np.round(np.sort(deg[~med_arr])).astype(int).tolist())\nprint(\"medial circular medians (deg):\", np.round(np.sort(deg[med_arr])).astype(int).tolist())\n\n# %% [markdown]\n# ## Summary\n#\n# PLACEHOLDER\n\n# %%\nprint(f\"notebook time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude/nb1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
echo $TMPDIR; cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && date -u && time LINK_SUBSET=6 MPLBACKEND=Agg python $TMPDIR/nb1.py 2>&1 | tail -150
```

```
/tmp/claude-1001
Thu Nov 12 10:48:02 UTC 2026
python: can't open file '/tmp/claude-1001/nb1.py': [Errno 2] No such file or directory

real	0m0.014s
user	0m0.009s
sys	0m0.008s
```

**Agent calls Bash**

```bash
mv /tmp/claude/nb1.py /tmp/claude/nbbuild.py $TMPDIR/ && cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && time LINK_SUBSET=6 MPLBACKEND=Agg python $TMPDIR/nb1.py 2>&1 | tail -150
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/nb1.py", line 53, in <module>
    import link
ModuleNotFoundError: No module named 'link'

real	0m4.506s
user	0m4.714s
sys	0m0.349s
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && time PYTHONPATH=. LINK_SUBSET=6 MPLBACKEND=Agg python $TMPDIR/nb1.py 2>&1 | tail -150
```

```
312 assets in version 0.261026.1912
LINK: Long-Term Intracortical Neural Activity and Kinematics | 10.48324/dandi.001201/0.261026.1912
version 0.251023.2336: 312 assets, 312 with the same path and asset id as 0.261026.1912
version 0.261015.2153: 312 assets, 312 with the same path and asset id as 0.261026.1912
sub-Monkey-N/sub-Monkey-N_ses-20200127_ecephys.nwb
  analysis/SpikingBandPower: {'shape': (27649, 96), 'unit': 'volts', 'conversion': 1e-06, 'n_timestamps': 27649, 'description': 'Spiking Band Power across time, in 20ms bins'}
  analysis/ThresholdCrossings: {'shape': (27649, 96), 'unit': 'volts', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Threshold crossings (threshold = -4.5RMS) across time, in 20ms bins'}
  analysis/index_position: {'shape': (27649, 1), 'unit': 'flexion units', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Index flexion position, from fully extended (0) to fully flexed (1)'}
  analysis/index_velocity: {'shape': (27649, 1), 'unit': 'flexion units per time bin', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Velocity of index flexion'}
  analysis/mrs_position: {'shape': (27649, 1), 'unit': 'flexion units', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Middle-ring-pinky flexion position, from fully extended (0) to fully flexed (1)'}
  analysis/mrs_velocity: {'shape': (27649, 1), 'unit': 'flexion units per time bin', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Velocity of middle-ring-pinky flexion'}
trials columns: ['start_time', 'stop_time', 'trial_number', 'trial_count', 'run_id', 'index_target_position', 'mrs_target_position', 'target_style', 'trial_timeout', 'timeseries'] | rows: 375
   start_time  stop_time  trial_count target_style
0        8.41       9.67           64           CO
1        9.69      11.05           69           CO
2       11.07      12.95           95           CO
electrodes columns: ['id', 'array_name', 'group_name', 'bank', 'pin', 'row', 'col', 'imp', 'locat
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('link.py').read()
old='''            out["electrodes"] = pd.DataFrame({k: [(_str(v) if isinstance(v, bytes) else v) for v in e[k][:]]
                                              for k in ("id", "array_name", "bank", "row", "col", "imp")})'''
new='''            out["electrode_columns"] = [_str(c) for c in e.attrs["colnames"]]
            out["electrodes"] = pd.DataFrame({k: ([(_str(v) if isinstance(v, bytes) else v) for v in e[k][:]]
                                                  if k in e else [np.nan] * e["id"].shape[0])
                                              for k in ("id", "array_name", "bank", "row", "col", "imp")})'''
assert old in s
s=s.replace(old,new)
open('link.py','w').write(s)
s=open('/tmp/claude-1001/nb1.py').read()
s=s.replace('''            "series": s["series"], "trial_columns": s["trial_columns"], "electrodes": s["electrodes"],''','''            "series": s["series"], "trial_columns": s["trial_columns"], "electrodes": s["electrodes"],
            "electrode_columns": s["electrode_columns"],''')
s=s.replace('''    if not {"array_name", "bank", "row", "col", "imp"} <= set(r["electrodes"].columns):
        gaps.append((r["path"], "electrodes"))''','''    miss = [c for c in ("array_name", "bank", "row", "col", "imp") if c not in r["electrode_columns"]]
    if miss:
        gaps.append((r["path"], "electrodes " + ",".join(miss)))''')
s=s.replace('''print("files checked:", len(S), "| files with a missing part:", len({g[0] for g in gaps}), gaps[:5])''','''print("files checked:", len(S), "| files with a missing part:", len({g[0] for g in gaps}))
print("missing parts and how many files lack each:", pd.Series([g[1] for g in gaps]).value_counts().to_dict())
print("files without the imp column, by year:", S.loc[["imp" not in c for c in S["electrode_columns"]], "date"].dt.year.value_counts().sort_index().to_dict())''')
open('/tmp/claude-1001/nb1.py','w').write(s)
EOF
. $TMPDIR/venv/bin/activate && time PYTHONPATH=. LINK_SUBSET=6 MPLBACKEND=Agg python $TMPDIR/nb1.py 2>&1 | tail -120
```

```
electrodes columns: ['id', 'array_name', 'group_name', 'bank', 'pin', 'row', 'col', 'imp', 'location']
   id array_name group_name bank  pin  row  col       imp         location
0   0    Lateral    Lateral    A    1    1    0  267000.0  Hand area of M1
1   1    Lateral    Lateral    A    2    0    0   72000.0  Hand area of M1
2   2    Lateral    Lateral    A    3    2    0  139000.0  Hand area of M1
3   3    Lateral    Lateral    A    4    3    0  232000.0  Hand area of M1
array_name  bank
Lateral     A       32
Medial      B       32
            C       32
dtype: int64
identifier: 2020-01-27_CO_nwb | session_start_time: 2020-01-27T00:00:00+00:00
subject: {'subject_id': 'Monkey N', 'date_of_birth': '2012-05-26T00:00:00+00:00', 'sex': 'M', 'species': 'Macaca mulatta'} | first timestamp: 8.41 s | bin steps: [0.019 0.02  0.021]
6 sessions on 6 days read in 8 s; peak memory 0.84 GB
subjects: 1 (Monkey N) in every file: {'subject_id': 'Monkey N', 'date_of_birth': '2012-05-26T00:00:00+00:00', 'sex': 'M', 'species': 'Macaca mulatta'}
sessions by style: {'CO': 4, 'RD': 2}
sessions by year: {2020: 1, 2021: 3, 2022: 2}
styles inside each file's trials table equal to its file style: True
trials per session: {375: 6}
bins per session: min 21451 max 27649
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude-1001/nb1.py'
s=open(p).read()
s=s.replace('''        g = TR[(TR["year"] == yr) & TR[name].notna()]
        X =''','''        g = TR[(TR["year"] == yr) & TR[name].notna()]
        if len(g) == 0:
            print(f"  {yr}: no trials")
            continue
        X =''')
open(p,'w').write(s)
EOF
. $TMPDIR/venv/bin/activate && PYTHONPATH=. LINK_SUBSET=12 MPLBACKEND=Agg python $TMPDIR/nb1.py 2>&1 | sed -n '/trials with a direction/,$p'
```

```
trials with a direction: 4488 | by class: {0: 548, 1: 811, 2: 531, 3: 356, 4: 542, 5: 802, 6: 528, 7: 370}
alignment main: trials dropped (no onset or window outside the trial): 44 of 4488
  2020: trials 739, days 2, accuracy 0.231 (chance 1/8, majority class 0.215, permuted labels 0.143), binomial p = 1.2e-15
  2023: trials 370, days 1, accuracy 0.224 (chance 1/8, majority class 0.197, permuted labels 0.141), binomial p = 8.3e-08
alignment code: trials dropped (no onset or window outside the trial): 3449 of 4488
  2020: trials 264, days 2, accuracy 0.277 (chance 1/8, majority class 0.205, permuted labels 0.106), binomial p = 3.4e-11
  2023: trials 101, days 1, accuracy 0.149 (chance 1/8, majority class 0.228, permuted labels 0.109), binomial p = 0.28
tuning strength over all channel-days: 1%, 99% quantiles 0.0011, 0.0528 (paper's axis 0 to 0.06)
channels active over the dataset (mean TCR > 1 Hz): 46
channel 7: array Lateral, bank A; circular median angle 85.3 deg, circular IQR 17.2 deg, median strength 0.0245, mean TCR 1.36 Hz
channel 32: array Medial, bank B; circular median angle -145.6 deg, circular IQR 97.2 deg, median strength 0.0295, mean TCR 37.89 Hz
over channels: median strength 0.0083, median circular IQR 34.7 deg
rank of channel 7's median strength: 11 of 96
rank of channel 32's circular IQR: 18 of 96
circular IQR < 45 deg, (i) all 96 (96 channels): fraction 0.583
circular IQR < 45 deg, (ii) active (46 channels): fraction 0.630
circular IQR < 90 deg, (i) all 96 (96 channels): fraction 0.792
circular IQR < 90 deg, (ii) active (46 channels): fraction 0.848
circular IQR quantiles (deg) 10/25/50/75/90: [ 19.   23.7  34.7  77.6 129.1]
Spearman rho (median strength vs median daily TCR, 96 channels) = 0.820, p = 1.7e-24
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python -c "
import sys; sys.path.insert(0,'entries/temmar-2025'); import link
l=link.read_layout(link.assets()['asset_id'][0]); e=l['electrodes']; print(e.iloc[[7,32,47]].to_string()); print(e.to_string())" | head -110
```

```
id array_name group_name bank  pin  row  col         imp         location
7    7    Lateral    Lateral    A    8    2    1  12537000.0  Hand area of M1
32  32     Medial     Medial    B    1    0    4    554000.0  Hand area of M1
47  47     Medial     Medial    B   16    5    5    768000.0  Hand area of M1
    id array_name group_name bank  pin  row  col         imp         location
0    0    Lateral    Lateral    A    1    1    0    267000.0  Hand area of M1
1    1    Lateral    Lateral    A    2    0    0     72000.0  Hand area of M1
2    2    Lateral    Lateral    A    3    2    0    139000.0  Hand area of M1
3    3    Lateral    Lateral    A    4    3    0    232000.0  Hand area of M1
4    4    Lateral    Lateral    A    5    5    0    229000.0  Hand area of M1
5    5    Lateral    Lateral    A    6    6    0    236000.0  Hand area of M1
6    6    Lateral    Lateral    A    7    4    0    337000.0  Hand area of M1
7    7    Lateral    Lateral    A    8    2    1  12537000.0  Hand area of M1
8    8    Lateral    Lateral    A    9    7    0    104000.0  Hand area of M1
9    9    Lateral    Lateral    A   10    6    1    322000.0  Hand area of M1
10  10    Lateral    Lateral    A   11    3    1    288000.0  Hand area of M1
11  11    Lateral    Lateral    A   12    7    1   1014000.0  Hand area of M1
12  12    Lateral    Lateral    A   13    4    1    248000.0  Hand area of M1
13  13    Lateral    Lateral    A   14    3    2    309000.0  Hand area of M1
14  14    Lateral    Lateral    A   15    1    1    416000.0  Hand area of M1
[... 82 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb2.py",
 "content": "# %% [markdown]\n# # Temmar et al. (2025), LINK: same-day and cross-day decoding (Figure 4, Appendix C.1)\n#\n# Paper: doi:10.52202/085713-4642. Dataset: DANDI:001201, version 0.261026.1912, streamed (the most recent\n# published version; the paper cites none, and the three published versions hold the same assets, see\n# `signals.ipynb`). Claims file: `claims/temmar-2025.yaml`. Code read: github.com/chesteklab/LINK_dataset at\n# 5e1c36a.\n#\n# | Claim | Tested here |\n# |---|---|\n# | fig4a-sameday-stable | RR on all 312 sessions, the LSTM on every 8th session |\n# | fig4a-lstm-beats-rr | on the LSTM sessions |\n# | fig4bc-dof-accuracy | RR on all sessions, LSTM on its sessions |\n# | fig4d-cross-day-decay | RR and LSTM decoders of the LSTM sessions, tested on every session within 100 days |\n# | suppc1-shuffle-baseline | RR on all sessions, LSTM on its sessions |\n# | fig2a-irregular-shifts | all days, with the R2 above |\n#\n# Why a subset for the LSTM. One LSTM of the paper's size (2000 iterations, batch 64, 20 bins, 300 hidden\n# units) takes about 105 s to train on one CPU thread of this runner (timed while preparing; the cell\n# below prints the time of each fit). 312 of them, four at a time, take about 2.3 hours, over the 60-minute\n# limit of a notebook. The LSTM is therefore trained on every 8th session in date order (39 sessions),\n# chosen before any result was seen, and the claims that need it are tested on those sessions.\n# Ridge regression is cheap and runs on every session.\n\n# %%\nimport os, time, resource\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom concurrent.futures import ThreadPoolExecutor\nfrom scipy import stats\nimport link\n\nT0 = time.time()\nSUBSET = int(os.environ.get(\"LINK_SUBSET\", \"0\"))            # 0 = every session; set only while developing\nITERS = int(os.environ.get(\"LINK_DEV_ITERS\", link.LSTM_ITERS))   # 2000 (paper); lowered only while developing\nLSTM_EVERY = 8              # every 8th session gets an LSTM (see above)\nEVAL_EVERY = 5              # cross-day evaluations score every 5th test bin (cost; same-day uses every bin)\nMAX_OFFSET = 100            # paper, Section 4.3: hold-outs within 100 days of training\nA = link.assets()\nif SUBSET:\n    A = A.iloc[np.linspace(0, len(A) - 1, SUBSET).astype(int)].reset_index(drop=True)\nprint(len(A), \"sessions; LSTM iterations\", ITERS)\n\n# %% [markdown]\n# ## Load and fit ridge regression\n#\n# Per session: the first 300 trials train and the remaining 75 test (Appendix C.1). SBP is z-scored per\n# channel on the training bins. Ridge regression (alpha 0.1, intercept, 8 bins of history, 768 inputs)\n# is fit with that normalisation (Appendix C.1) and, as a variant, on the raw SBP as the code does.\n\n# %%\ndef load(i):\n    r = A.iloc[i]\n    s = link.read_session(r[\"asset_id\"], tcr=False)\n    (xtr, ytr), (xte, yte) = link.split(s)\n    mu, sd = link.zparams(xtr)\n    rr = link.rr_fit(((xtr - mu) / sd).astype(np.float32), ytr)\n    rr_raw = link.rr_fit(xtr, ytr)\n    rec = {\"i\": i, \"date\": r[\"date\"], \"style\": s[\"style\"], \"path\": r[\"path\"],\n           \"n_train_bins\": len(xtr), \"n_test_bins\": len(xte),\n           \"n_test_trials\": len(s[\"trials\"]) - link.N_TRAIN_TRIALS,\n           \"mu\": mu, \"sd\": sd, \"rr\": rr, \"rr_raw\": rr_raw, \"xte\": xte, \"yte\": yte,\n           \"sbp_mean\": s[\"sbp\"].astype(np.float64).mean(0), \"n_bins\": len(s[\"sbp\"]),\n           \"test_trial_index\": s[\"trial_index\"][link.N_TRAIN_TRIALS:] - s[\"trial_index\"][link.N_TRAIN_TRIALS]}\n    if i % LSTM_EVERY == 0:\n        rec[\"xtr_z\"] = ((xtr - mu) / sd).astype(np.float32)\n        rec[\"ytr\"] = ytr\n    return rec\n\n\nt = time.time()\nwith ThreadPoolExecutor(4) as ex:\n    SES = list(ex.map(load, range(len(A))))\nfirst = A[\"date\"].min()\nfor s in SES:\n    s[\"day\"] = (s[\"date\"] - first).days\nprint(f\"loaded and fit RR on {len(SES)} sessions in {time.time() - t:.0f} s; \"\n      f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\nprint(\"test trials per session:\", pd.Series([s[\"n_test_trials\"] for s in SES]).value_counts().to_dict(),\n      \"| test bins: %d to %d\" % (min(s[\"n_test_bins\"] for s in SES), max(s[\"n_test_bins\"] for s in SES)))\nprint(\"training bins: %d to %d\" % (min(s[\"n_train_bins\"] for s in SES), max(s[\"n_train_bins\"] for s in SES)))\n\n# %%\ndef z(x, mu, sd):\n    return ((x - mu) / sd).astype(np.float32)\n\n\nfor s in SES:\n    s[\"r2_rr\"] = link.r2_per_output(s[\"yte\"], link.rr_predict(s[\"rr\"], z(s[\"xte\"], s[\"mu\"], s[\"sd\"])))\n    s[\"r2_rr_raw\"] = link.r2_per_output(s[\"yte\"], link.rr_predict(s[\"rr_raw\"], s[\"xte\"]))\nprint(\"same-day RR R2 (mean of 4 outputs): median %.3f, range %.3f to %.3f\" %\n      (np.median([s[\"r2_rr\"].mean() for s in SES]), min(s[\"r2_rr\"].mean() for s in SES), max(s[\"r2_rr\"].mean() for s in SES)))\n\n# %% [markdown]\n# ## Train the LSTMs\n#\n# Each LSTM is trained as Appendix C.1 and the claim's criterion give (96 inputs, 300 hidden units, one\n# layer, linear readout of the four outputs at the last of 20 bins; Adam, batch 64, 2000 iterations,\n# learning rate linear from 2e-4 to 1e-5, weight decay 0.001; outputs z-scored on the training data; white\n# noise of SD 0.1 per bin and a bias of SD 0.2 per sequence and channel), seed 42 as in the code. Each\n# worker then evaluates its decoder on its own hold-out, on the shuffled hold-out (suppc1), and on the\n# hold-out of every session within 100 days under both normalisations of fig4d (every 5th bin).\n\n# %%\nLSTM_IDX = [s[\"i\"] for s in SES if s[\"i\"] % LSTM_EVERY == 0]\nTEST = {s[\"i\"]: (s[\"day\"], s[\"xte\"], s[\"yte\"], s[\"mu\"], s[\"sd\"]) for s in SES}\n\n\ndef shuffles(x_raw, y, mu, sd, tti, rng):\n    \"\"\"The hold-out shuffles of suppc1-shuffle-baseline: (a) permute the raw bins of SBP, then build the\n    history; (b) permute whole input windows; and (trials) permute whole trials; kinematics are permuted\n    separately in each case.\"\"\"\n    n = len(y)\n    pa, pk = rng.permutation(n), rng.permutation(n)\n    out = {\"a\": (x_raw[pa], y[pk], None)}\n    out[\"b\"] = (x_raw, y[pk], rng.permutation(n))       # window permutation applied to the predictions\n    bounds = np.append(tti, n)\n    tr = [np.arange(bounds[j], bounds[j + 1]) for j in range(len(tti))]\n    o1 = np.concatenate([tr[j] for j in rng.permutation(len(tr))])\n    o2 = np.concatenate([tr[j] for j in rng.permutation(len(tr))])\n    out[\"trials\"] = (x_raw[o1], y[o2], None)\n    return out\n\n\ndef lstm_task(i, seed=42, cross=True):\n    t0 = time.time()\n    s = SES_BY_I[i]\n    state, onorm = link.lstm_train([(s[\"xtr_z\"], s[\"ytr\"])], seed=seed, iters=ITERS)\n    fit_s = time.time() - t0\n    res = {\"i\": i, \"seed\": seed, \"fit_s\": fit_s}\n    p = link.lstm_predict(state, onorm, z(s[\"xte\"], s[\"mu\"], s[\"sd\"]))\n    res[\"r2\"] = link.r2_per_output(s[\"yte\"], p)\n    if not cross:\n        return res\n    rng = np.random.default_rng(0)\n    sh = {}\n    for k, (xs, ys, perm) in shuffles(s[\"xte\"], s[\"yte\"], s[\"mu\"], s[\"sd\"], s[\"test_trial_index\"], rng).items():\n        pr = link.lstm_predict(state, onorm, z(xs, s[\"mu\"], s[\"sd\"]))\n        if perm is not None:\n            pr = pr[perm]\n        sh[k] = link.r2_per_output(ys, pr).mean()\n    res[\"shuffle\"] = sh\n    cr = []\n    for j, (day, xte, yte, mu, sd) in TEST.items():\n        off = day - s[\"day\"]\n        if abs(off) > MAX_OFFSET:\n            continue\n        sel = slice(None, None, EVAL_EVERY)\n        for norm, (m_, s_) in ((\"train\", (s[\"mu\"], s[\"sd\"])), (\"test\", (mu, sd))):\n            pr = link.lstm_predict(state, onorm, z(xte, m_, s_), every=EVAL_EVERY)\n            cr.append({\"dec\": i, \"test\": j, \"offset\": off, \"norm\": norm, \"decoder\": \"LSTM\",\n                       \"r2\": link.r2_per_output(yte[sel], pr).mean()})\n    res[\"cross\"] = cr\n    res[\"total_s\"] = time.time() - t0\n    return res\n\n\nSES_BY_I = {s[\"i\"]: s for s in SES}\nimport multiprocessing as mp\nfrom concurrent.futures import ProcessPoolExecutor\nt = time.time()\nwith ProcessPoolExecutor(4, mp_context=mp.get_context(\"fork\")) as ex:\n    LRES = list(ex.map(lstm_task, LSTM_IDX))\nfits = np.array([r[\"fit_s\"] for r in LRES])\nprint(f\"{len(LRES)} LSTMs in {(time.time() - t) / 60:.1f} min; seconds per fit {fits.min():.0f} to {fits.max():.0f} \"\n      f\"(median {np.median(fits):.0f}); estimate for all {len(SES)} sessions at 4 in parallel: \"\n      f\"{len(SES) * np.median(fits) / 4 / 3600:.1f} h of fitting alone\")\nfor r in LRES:\n    SES_BY_I[r[\"i\"]][\"r2_lstm\"] = r[\"r2\"]\n\n# %% [markdown]\n# ## fig4a-sameday-stable\n#\n# > Same-day decoding accuracy (R2 averaged across the four outputs on the 75 hold-out trials) remains\n# > relatively stable over the dataset, with most shifts shared by RR and LSTM.\n\n# %% tags=[\"claim:fig4a-sameday-stable\"]\nSD = pd.DataFrame([{\"i\": s[\"i\"], \"date\": s[\"date\"], \"day\": s[\"day\"], \"style\": s[\"style\"],\n                    \"rr\": s[\"r2_rr\"].mean(), \"rr_raw\": s[\"r2_rr_raw\"].mean(),\n                    \"lstm\": s[\"r2_lstm\"].mean() if \"r2_lstm\" in s else np.nan,\n                    **{f\"rr_{n}\": v for n, v in zip(link.KIN_NAMES, s[\"r2_rr\"])},\n                    **{f\"lstm_{n}\": v for n, v in zip(link.KIN_NAMES, s.get(\"r2_lstm\", [np.nan] * 4))}} for s in SES])\nL = SD.dropna(subset=[\"lstm\"])\nfor name, d, col in ((\"RR, all sessions\", SD, \"rr\"), (\"RR without scaler (code), all sessions\", SD, \"rr_raw\"),\n                     (\"RR, LSTM sessions\", L, \"rr\"), (\"LSTM\", L, \"lstm\")):\n    r = link.linfit(d[\"day\"], d[col])\n    print(f\"{name}: n = {len(d)}, median R2 {d[col].median():.3f} (range {d[col].min():.3f} to {d[col].max():.3f}), \"\n          f\"slope {r.slope * 365.25:+.4f} per year, p = {r.pvalue:.2g}\")\npc = stats.pearsonr(L[\"rr\"], L[\"lstm\"])\nprint(f\"Pearson r between RR and LSTM same-day R2 over {len(L)} sessions: {pc.statistic:.3f}, p = {pc.pvalue:.2g}\")\nprint(\"by year (median R2):\")\nprint(SD.groupby(SD[\"date\"].dt.year)[[\"rr\", \"rr_raw\", \"lstm\"]].median().round(3).to_string())\nfig, ax = plt.subplots(figsize=(8, 3))\nax.plot(SD[\"date\"], SD[\"rr\"], \".\", ms=3, label=\"RR\")\nax.plot(L[\"date\"], L[\"lstm\"], \"o\", ms=4, label=\"LSTM\")\nax.set_ylabel(\"same-day R2\"); ax.legend(); plt.show()\nprint(\"plotted R2 range: %.3f to %.3f\" % (min(SD[\"rr\"].min(), L[\"lstm\"].min()), max(SD[\"rr\"].max(), L[\"lstm\"].max())))\n\n# %% [markdown]\n# ## fig4a-lstm-beats-rr\n#\n# > The LSTM outperformed ridge regression in same-day decoding on every day.\n\n# %% tags=[\"claim:fig4a-lstm-beats-rr\"]\nL = L.assign(diff=L[\"lstm\"] - L[\"rr\"])\nworse = L[L[\"diff\"] <= 0]\nprint(f\"LSTM above RR on {(L['diff'] > 0).sum()} of {len(L)} sessions ({(L['diff'] > 0).mean():.3f}); \"\n      f\"difference median {L['diff'].median():.3f}, range {L['diff'].min():.3f} to {L['diff'].max():.3f}\")\nprint(\"sessions where RR is not below the LSTM:\", worse[[\"date\", \"style\", \"rr\", \"lstm\"]].to_dict(\"records\"))\nif len(worse):\n    with ProcessPoolExecutor(4, mp_context=mp.get_context(\"fork\")) as ex:\n        extra = list(ex.map(lstm_task, [i for i in worse[\"i\"] for _ in (1, 2)],\n                            [sd_ for _ in worse[\"i\"] for sd_ in (1, 2)], [False] * (2 * len(worse))))\n    for r in extra:\n        print(f\"  session {SES_BY_I[r['i']]['date'].date()} seed {r['seed']}: LSTM R2 {r['r2'].mean():.3f} \"\n              f\"(RR {SES_BY_I[r['i']]['r2_rr'].mean():.3f})\")\n\n# %% [markdown]\n# ## fig4bc-dof-accuracy\n#\n# > Decoding of finger positions is more accurate than of velocities, and MRS predictions are more accurate\n# > than IDX predictions.\n\n# %% tags=[\"claim:fig4bc-dof-accuracy\"]\nfor dec, d in ((\"rr\", SD), (\"rr (LSTM sessions)\", L), (\"lstm\", L)):\n    p = dec.split()[0]\n    med = {n: d[f\"{p}_{n}\"].median() for n in link.KIN_NAMES}\n    pos_gt_vel = min(med[\"idx_pos\"], med[\"mrs_pos\"]) > max(med[\"idx_vel\"], med[\"mrs_vel\"])\n    mrs_gt = med[\"mrs_pos\"] > med[\"idx_pos\"] and med[\"mrs_vel\"] > med[\"idx_vel\"]\n    f_pos = ((d[f\"{p}_idx_pos\"] > d[f\"{p}_idx_vel\"]) & (d[f\"{p}_mrs_pos\"] > d[f\"{p}_mrs_vel\"])).mean()\n    f_mrs = ((d[f\"{p}_mrs_pos\"] > d[f\"{p}_idx_pos\"]) & (d[f\"{p}_mrs_vel\"] > d[f\"{p}_idx_vel\"])).mean()\n    print(f\"{dec} (n = {len(d)}): medians \" + \", \".join(f\"{n} {v:.3f}\" for n, v in med.items()))\n    print(f\"   positions above velocities: {pos_gt_vel}; MRS above IDX for position and velocity: {mrs_gt}; \"\n          f\"fraction of sessions with position > velocity for both fingers {f_pos:.3f}, MRS > IDX for both {f_mrs:.3f}\")\n\n# %% [markdown]\n# ## fig4d-cross-day-decay\n#\n# > Decoders tested on hold-out sets of other days within 100 days of training lose accuracy sharply in the\n# > short term, with the decay stabilising at longer offsets; neither RR nor LSTM generalises well, the LSTM is\n# > better at every offset, and both follow a similar decay.\n#\n# The decoders are those of the LSTM sessions, for both RR and LSTM, so the two curves come from the same\n# training days; both are scored on every 5th test bin. Readings: offset (a) signed or (b) absolute;\n# normalisation (i) the training day's or (ii) the test day's own training-trial parameters. RR from every\n# session's decoder is shown as a variant.\n\n# %%\nrr_rows = []\nfor s in SES:\n    for j, (day, xte, yte, mu, sd) in TEST.items():\n        off = day - s[\"day\"]\n        if abs(off) > MAX_OFFSET:\n            continue\n        for norm, (m_, s_) in ((\"train\", (s[\"mu\"], s[\"sd\"])), (\"test\", (mu, sd))):\n            for every in ((EVAL_EVERY,) if s[\"i\"] not in LSTM_IDX else (EVAL_EVERY,)):\n                pr = link.rr_predict(s[\"rr\"], z(xte, m_, s_))\n                rr_rows.append({\"dec\": s[\"i\"], \"test\": j, \"offset\": off, \"norm\": norm, \"decoder\": \"RR\",\n                                \"r2\": link.r2_per_output(yte[::every], pr[::every]).mean()})\nCR = pd.concat([pd.DataFrame(rr_rows), pd.DataFrame([c for r in LRES for c in r[\"cross\"]])], ignore_index=True)\nCR[\"subset\"] = CR[\"dec\"].isin(LSTM_IDX)\nprint(\"evaluations:\", CR.groupby([\"decoder\", \"subset\", \"norm\"]).size().to_dict())\n\n# %% tags=[\"claim:fig4d-cross-day-decay\"]\ndef curve(d, absolute):\n    off = d[\"offset\"].abs() if absolute else d[\"offset\"]\n    return d.groupby(off)[\"r2\"].agg([\"mean\", \"sem\", \"size\"])\n\n\nsummary = []\nfor absolute in (False, True):\n    for norm in (\"train\", \"test\"):\n        c_l = curve(CR[(CR[\"decoder\"] == \"LSTM\") & (CR[\"norm\"] == norm)], absolute)\n        c_r = curve(CR[(CR[\"decoder\"] == \"RR\") & CR[\"subset\"] & (CR[\"norm\"] == norm)], absolute)\n        both = c_l.join(c_r, lsuffix=\"_l\", rsuffix=\"_r\", how=\"inner\")\n        better = (both[\"mean_l\"] > both[\"mean_r\"]).mean()\n        res = {}\n        for lab, c in ((\"LSTM\", c_l), (\"RR\", c_r)):\n            m = c[\"mean\"]\n            o = m.index.to_series()\n            d0 = m.get(0, np.nan)\n            near = m[(o.abs() >= 1) & (o.abs() <= 5)].mean()\n            far = m[(o.abs() >= 90) & (o.abs() <= 100)].mean()\n            res[lab] = (d0, near, far)\n        sharp = all(res[k][0] - res[k][1] > res[k][1] - res[k][2] for k in res)\n        bb = both[both.index != 0] if True else both\n        rcorr = stats.pearsonr(both[\"mean_l\"] / res[\"LSTM\"][0], both[\"mean_r\"] / res[\"RR\"][0]).statistic\n        summary.append({\"offset\": \"absolute\" if absolute else \"signed\", \"norm\": norm, \"offsets\": len(both),\n                        \"LSTM better at fraction\": round(better, 3),\n                        \"LSTM day0 / 1-5 / 90-100\": \"%.3f / %.3f / %.3f\" % res[\"LSTM\"],\n                        \"RR day0 / 1-5 / 90-100\": \"%.3f / %.3f / %.3f\" % res[\"RR\"],\n                        \"sharp then stable\": sharp, \"r(normalised curves)\": round(rcorr, 3)})\nprint(pd.DataFrame(summary).to_string(index=False))\nfor norm in (\"train\", \"test\"):\n    c_all = curve(CR[(CR[\"decoder\"] == \"RR\") & (CR[\"norm\"] == norm)], True)\n    print(f\"variant, RR of all {len(SES)} decoders, absolute offset, norm {norm}: day0 {c_all['mean'].get(0, np.nan):.3f}, \"\n          f\"1-5 {c_all['mean'].loc[1:5].mean():.3f}, 90-100 {c_all['mean'].loc[90:100].mean():.3f}\")\nfig, ax = plt.subplots(figsize=(7, 3))\nfor lab in (\"LSTM\", \"RR\"):\n    c = curve(CR[(CR[\"decoder\"] == lab) & CR[\"subset\"] & (CR[\"norm\"] == \"train\")], False)\n    ax.plot(c.index, c[\"mean\"], \".-\", ms=3, label=lab)\nax.set_xlabel(\"test day minus training day\"); ax.set_ylabel(\"R2\"); ax.legend(); plt.show()\nc = CR[CR[\"subset\"] & (CR[\"norm\"] == \"train\")]\nprint(\"plotted per-offset means: %.3f to %.3f (no point outside the axes; axes auto-scaled)\" % (\n    c.groupby([\"decoder\", \"offset\"])[\"r2\"].mean().min(), c.groupby([\"decoder\", \"offset\"])[\"r2\"].mean().max()))\n\n# %% [markdown]\n# ## suppc1-shuffle-baseline\n#\n# > With neural and behavioural hold-out data shuffled independently on one session, RR gives an average R2 of\n# > -0.166 and the LSTM of -0.156.\n\n# %% tags=[\"claim:suppc1-shuffle-baseline\"]\nrows = []\nfor s in SES:\n    rng = np.random.default_rng(0)\n    for k, (xs, ys, perm) in shuffles(s[\"xte\"], s[\"yte\"], s[\"mu\"], s[\"sd\"], s[\"test_trial_index\"], rng).items():\n        pr = link.rr_predict(s[\"rr\"], z(xs, s[\"mu\"], s[\"sd\"]))\n        if perm is not None:\n            pr = pr[perm]\n        rows.append({\"i\": s[\"i\"], \"reading\": k, \"decoder\": \"RR\", \"r2\": link.r2_per_output(ys, pr).mean()})\nfor r in LRES:\n    for k, v in r[\"shuffle\"].items():\n        rows.append({\"i\": r[\"i\"], \"reading\": k, \"decoder\": \"LSTM\", \"r2\": v})\nSH = pd.DataFrame(rows)\nSH[\"lstm_session\"] = SH[\"i\"].isin(LSTM_IDX)\nprint(SH.groupby([\"decoder\", \"reading\"])[\"r2\"].describe()[[\"count\", \"50%\", \"min\", \"max\"]].round(4).to_string())\nprint(\"RR on the LSTM sessions only:\")\nprint(SH[SH[\"lstm_session\"] & (SH[\"decoder\"] == \"RR\")].groupby(\"reading\")[\"r2\"].median().round(4).to_string())\n\n# %% [markdown]\n# ## fig2a-irregular-shifts\n#\n# > Groups of channels show irregular SBP shifts in some periods, for example from about July to November 2022,\n# > and these shifts did not affect overall decoding performance.\n\n# %% tags=[\"claim:fig2a-irregular-shifts\"]\nday_mean = {}\nfor s in SES:\n    a = day_mean.setdefault(s[\"date\"], [np.zeros(96), 0])\n    a[0] += s[\"sbp_mean\"] * s[\"n_bins\"]; a[1] += s[\"n_bins\"]\nDM = pd.DataFrame({d: v[0] / v[1] for d, v in day_mean.items()}).T.sort_index()\nshifts = []\nfor d in DM.index:\n    win = DM[(DM.index < d) & (DM.index >= d - pd.Timedelta(days=30))]\n    if len(win) < 3:\n        shifts.append(np.nan); continue\n    med = win.median(); mad = (win - med).abs().median()\n    shifts.append(int(((DM.loc[d] - med).abs() > 3 * mad.where(mad > 0, np.nan)).sum()))\nSHF = pd.Series(shifts, index=DM.index)\ninwin = (SHF.index >= \"2022-07-01\") & (SHF.index <= \"2022-11-30\")\nprint(\"days in July to November 2022:\", inwin.sum(), \"| max channels shifting on one day there:\", SHF[inwin].max(),\n      \"| days with >= 5:\", int((SHF[inwin] >= 5).sum()))\nprint(\"outside that window: days with >= 5 shifting channels: %d of %d (max %d)\" % (\n    (SHF[~inwin] >= 5).sum(), SHF[~inwin].notna().sum(), SHF[~inwin].max()))\nprint(\"days with >= 5 shifting channels by year:\", SHF[SHF >= 5].groupby(SHF[SHF >= 5].index.year).size().to_dict())\nw = (SD[\"date\"] >= \"2022-07-01\") & (SD[\"date\"] <= \"2022-11-30\")\nfor col, d in ((\"rr\", SD), (\"lstm\", SD.dropna(subset=[\"lstm\"]))):\n    ww = (d[\"date\"] >= \"2022-07-01\") & (d[\"date\"] <= \"2022-11-30\")\n    lo, hi = np.percentile(d[col], [10, 90])\n    print(f\"{col}: sessions in window {ww.sum()}, median R2 there {d.loc[ww, col].median():.3f}; \"\n          f\"10th to 90th percentile over all {len(d)} sessions {lo:.3f} to {hi:.3f}\")\n\n# %% [markdown]\n# ## Summary\n#\n# PLACEHOLDER\n\n# %%\nprint(f\"notebook time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && date -u && time PYTHONPATH=. LINK_SUBSET=24 LINK_DEV_ITERS=100 MPLBACKEND=Agg python $TMPDIR/nb2.py 2>&1 | tail -80
```

```
Thu Nov 12 10:51:32 UTC 2026
24 sessions; LSTM iterations 100
loaded and fit RR on 24 sessions in 35 s; peak memory 1.25 GB
test trials per session: {75: 24} | test bins: 4162 to 6225
training bins: 17009 to 23061
same-day RR R2 (mean of 4 outputs): median 0.318, range 0.188 to 0.375
3 LSTMs in 0.4 min; seconds per fit 8 to 13 (median 12); estimate for all 24 sessions at 4 in parallel: 0.0 h of fitting alone
RR, all sessions: n = 24, median R2 0.318 (range 0.188 to 0.375), slope -0.0059 per year, p = 0.63
RR without scaler (code), all sessions: n = 24, median R2 0.319 (range 0.188 to 0.372), slope -0.0059 per year, p = 0.63
RR, LSTM sessions: n = 3, median R2 0.349 (range 0.269 to 0.351), slope -0.0048 per year, p = 0.92
LSTM: n = 3, median R2 0.125 (range 0.084 to 0.147), slope -0.0130 per year, p = 0.68
Pearson r between RR and LSTM same-day R2 over 3 sessions: 0.928, p = 0.24
by year (median R2):
         rr  rr_raw   lstm
date                      
2020  0.343   0.341  0.147
2021  0.299   0.299  0.084
2022  0.323   0.323  0.125
2023  0.306   0.305    NaN
plotted R2 range: 0.084 to 0.375
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude-1001/nb1.py'
s=open(p).read()
s=s.replace('''print("lateral circular medians (deg):"''','''mm, ll = ~med_arr, med_arr
print("variant, with the array names swapped (file Lateral read as medial): medial-sector fraction %.3f, "
      "near 90: %d, near 0: %d; lateral-sector fraction %.3f" % (within(deg[mm], 45, 67.5).mean(),
      within(deg[mm], 90, 45).sum(), within(deg[mm], 0, 45).sum(), within(deg[ll], -135, 67.5).mean()))
print("lateral circular medians (deg):"''')
open(p,'w').write(s)
p='/tmp/claude-1001/nb2.py'
s=open(p).read()
s=s.replace('both = c_l.join(c_r, lsuffix="_l", rsuffix="_r", how="inner")','both = c_l.add_suffix("_l").join(c_r.add_suffix("_r"), how="inner")')
s=s.replace('''    print("outside that window: days with >= 5 shifting channels: %d of %d (max %d)" % (
    (SHF[~inwin] >= 5).sum(), SHF[~inwin].notna().sum(), SHF[~inwin].max()))''','''    print("outside that window: days with >= 5 shifting channels: %d of %d (max %s)" % (
    (SHF[~inwin] >= 5).sum(), SHF[~inwin].notna().sum(), SHF[~inwin].max()))''')
s=s.replace('''print("outside that window: days with >= 5 shifting channels: %d of %d (max %d)" % (''','''print("outside that window: days with >= 5 shifting channels: %d of %d (max %s)" % (''')
s=s.replace("LSTM_EVERY = 8 ","LSTM_EVERY = 12")
s=s.replace("every 8th session in date order (39 sessions)","every 12th session in date order (26 sessions)")
s=s.replace("the LSTM on every 8th session","the LSTM on every 12th session")
s=s.replace("about 105 s to train on one CPU thread of this runner (timed while preparing; the cell\n# below prints the time of each fit). 312 of them, four at a time, take about 2.3 hours","about 105 s to train alone on one CPU thread of this runner, and about 200 s when four train at once\n# (timed while preparing; the cell below prints the time of each fit). 312 of them, four at a time, take\n# about 4.3 hours")
open(p,'w').write(s)
EOF
grep -n "LSTM_EVERY =\|4.3 hours\|every 12th" $TMPDIR/nb2.py | head; . $TMPDIR/venv/bin/activate && python $TMPDIR/nbbuild.py $TMPDIR/nb1.py signals.ipynb && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3600 --output-dir $TMPDIR/exec --output signals.ipynb signals.ipynb 2>&1 | tail -3
```

```
11:# | fig4a-sameday-stable | RR on all 312 sessions, the LSTM on every 12th session |
21:# about 4.3 hours, over the 60-minute
22:# limit of a notebook. The LSTM is therefore trained on every 12th session in date order (26 sessions),
38:LSTM_EVERY = 12             # every 8th session gets an LSTM (see above)
67:    if i % LSTM_EVERY == 0:
107:LSTM_IDX = [s["i"] for s in SES if s["i"] % LSTM_EVERY == 0]
wrote signals.ipynb 44 cells
Thu Nov 12 10:53:35 UTC 2026
[NbConvertApp] Converting notebook signals.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 200113 bytes to /tmp/claude-1001/exec/signals.ipynb

real	7m39.022s
user	5m28.454s
sys	0m25.467s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('exec/signals.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or (o.get('data') or {}).get('text/plain','')
        if t and 'image' not in str(o.get('data',{}).keys()): print(t[:6000])
EOF
```

```
312 assets in version 0.261026.1912
LINK: Long-Term Intracortical Neural Activity and Kinematics | 10.48324/dandi.001201/0.261026.1912
version 0.251023.2336: 312 assets, 312 with the same path and asset id as 0.261026.1912
version 0.261015.2153: 312 assets, 312 with the same path and asset id as 0.261026.1912

sub-Monkey-N/sub-Monkey-N_ses-20200127_ecephys.nwb
  analysis/SpikingBandPower: {'shape': (27649, 96), 'unit': 'volts', 'conversion': 1e-06, 'n_timestamps': 27649, 'description': 'Spiking Band Power across time, in 20ms bins'}
  analysis/ThresholdCrossings: {'shape': (27649, 96), 'unit': 'volts', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Threshold crossings (threshold = -4.5RMS) across time, in 20ms bins'}
  analysis/index_position: {'shape': (27649, 1), 'unit': 'flexion units', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Index flexion position, from fully extended (0) to fully flexed (1)'}
  analysis/index_velocity: {'shape': (27649, 1), 'unit': 'flexion units per time bin', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Velocity of index flexion'}
  analysis/mrs_position: {'shape': (27649, 1), 'unit': 'flexion units', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Middle-ring-pinky flexion position, from fully extended (0) to fully flexed (1)'}
  analysis/mrs_velocity: {'shape': (27649, 1), 'unit': 'flexion units per time bin', 'conversion': 1.0, 'n_timestamps': 27649, 'description': 'Velocity of middle-ring-pinky flexion'}
trials columns: ['start_time', 'stop_time', 'trial_number', 'trial_count', 'run_id', 'index_target_position', 'mrs_target_position', 'target_style', 'trial_timeout', 'timeseries'] | rows: 375
   start_time  stop_time  trial_count target_style
0        8.41       9.67           64           CO
1        9.69      11.05           69           CO
2       11.07      12.95           95           CO
electrodes columns: ['id', 'array_name', 'group_name', 'bank', 'pin', 'row', 'col', 'imp', 'loca
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && python - <<'EOF'
import sys; sys.path.insert(0,'entries/temmar-2025'); import link, numpy as np
from concurrent.futures import ThreadPoolExecutor
A=link.assets()
def f(i):
    s=link.read_session(A.asset_id[i], neural=False, tcr=False)
    k=s['kin']; t=s['t']
    fd=np.diff(k[:,:2].astype(float),axis=0); v=k[:-1,2:].astype(float)
    bad=np.abs(v-fd).max(1)>1e-5
    gaps=np.where(np.diff(t)>0.03)[0]
    # mismatch positions near gaps or trial starts
    ti=set(s['trial_index'])
    badi=np.where(bad)[0]
    neargap=np.isin(badi, gaps).sum()
    neartrial=sum((b+1) in ti for b in badi)
    return i, len(t), bad.sum(), len(gaps), neargap, neartrial
with ThreadPoolExecutor(8) as ex:
    for r in ex.map(f, range(0,312,8)): 
        if r[2] or r[3]: print(r)
EOF
```

```
(24, 30315, np.int64(1), 1, np.int64(1), 1)
(152, 25105, np.int64(1), 1, np.int64(1), 1)
(272, 26497, np.int64(9), 9, np.int64(9), 9)
(304, 25325, np.int64(1), 1, np.int64(1), 1)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude-1001/nb1.py'
s=open(p).read()
old='''            "vel_vs_diff": [float(np.max(np.abs(s["kin"][1:, 2 + j] - dpos[:, j]))) for j in range(2)],
            "vel_vs_diff_lag": [float(np.max(np.abs(s["kin"][:-1, 2 + j] - dpos[:, j]))) for j in range(2)],'''
new='''            "vel_vs_back": [float(np.max(np.abs(s["kin"][1:, 2 + j] - dpos[:, j]))) for j in range(2)],
            "vel_vs_fwd": [float(np.max(np.abs(s["kin"][:-1, 2 + j] - dpos[:, j]))) for j in range(2)],
            "gaps": np.where(np.diff(s["t"]) > 0.03)[0],
            "gap_s": np.diff(s["t"])[np.diff(s["t"]) > 0.03],
            "vel_fwd_mismatch": np.where(np.abs(s["kin"][:-1, 2:] - dpos).max(1) > 1e-5)[0],'''
assert old in s; s=s.replace(old,new)
old='''print("velocity minus difference of positions, max over sessions (velocity[t] vs pos[t]-pos[t-1]):",
      np.round(np.vstack(S["vel_vs_diff"]).max(0), 4),
      "| (velocity[t] vs pos[t+1]-pos[t]):", np.round(np.vstack(S["vel_vs_diff_lag"]).max(0), 4))'''
new='''print("time gaps (steps over 30 ms): %d sessions have any, %d gaps in all, %.2f to %.1f s long" % (
    sum(len(g) > 0 for g in S["gaps"]), sum(len(g) for g in S["gaps"]),
    min(np.min(g) for g in S["gap_s"] if len(g)), max(np.max(g) for g in S["gap_s"] if len(g))))
mis = sum(len(m) for m in S["vel_fwd_mismatch"])
mis_gap = sum(np.isin(m, g).sum() for m, g in zip(S["vel_fwd_mismatch"], S["gaps"]))
print("velocity[t] equals pos[t+1] - pos[t] (a forward difference) except at %d bins, %d of which are the bin "
      "before a time gap" % (mis, mis_gap))
print("velocity[t] minus pos[t] - pos[t-1] (backward difference), largest |difference| per finger:",
      np.round(np.vstack(S["vel_vs_back"]).max(0), 4))'''
assert old in s; s=s.replace(old,new)
old='''print("timestamp steps (s):", sorted(set(steps.round(3))), "(all within 1 ms of 0.02)")
print("velocity equals pos[t] - pos[t-1] to within", np.round(np.vstack(S["vel_vs_diff"]).max(0), 5))'''
new='''print("timestamp steps within a run of bins: %s s; %d sessions also have gaps over 30 ms (see the data check)" % (
    sorted(set(steps[steps < 0.03].round(3))), sum(len(g) > 0 for g in S["gaps"])))
print("velocity is the forward difference of binned position, except at %d bins (%d before a gap)" % (mis, mis_gap))'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
date -u
```

```
Thu Nov 12 11:02:31 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude-1001/nb2.py'
s=open(p).read()
s=s.replace("LSTM_EVERY = 12             # every 8th session gets an LSTM (see above)","LSTM_EVERY = 16             # every 16th session gets an LSTM (see above)")
s=s.replace("every 12th session in date order (26 sessions)","every 16th session in date order (20 sessions)")
s=s.replace("the LSTM on every 12th session","the LSTM on every 16th session")
old='''rr_rows = []
for s in SES:
    for j'''
new='''rr_rows = []
for s in [SES_BY_I[i] for i in LSTM_IDX]:
    for j'''
assert old in s; s=s.replace(old,new)
old='''            for every in ((EVAL_EVERY,) if s["i"] not in LSTM_IDX else (EVAL_EVERY,)):
                pr = link.rr_predict(s["rr"], z(xte, m_, s_))
                rr_rows.append({"dec": s["i"], "test": j, "offset": off, "norm": norm, "decoder": "RR",
                                "r2": link.r2_per_output(yte[::every], pr[::every]).mean()})'''
new='''            pr = link.rr_predict(s["rr"], z(xte, m_, s_))
            rr_rows.append({"dec": s["i"], "test": j, "offset": off, "norm": norm, "decoder": "RR",
                            "r2": link.r2_per_output(yte[::EVAL_EVERY], pr[::EVAL_EVERY]).mean()})'''
assert old in s; s=s.replace(old,new)
old='''for norm in ("train", "test"):
    c_all = curve(CR[(CR["decoder"] == "RR") & (CR["norm"] == norm)], True)
    print(f"variant, RR of all {len(SES)} decoders, absolute offset, norm {norm}: day0 {c_all['mean'].get(0, np.nan):.3f}, "
          f"1-5 {c_all['mean'].loc[1:5].mean():.3f}, 90-100 {c_all['mean'].loc[90:100].mean():.3f}")
'''
assert old in s; s=s.replace(old,'''print("evaluations per offset (LSTM, signed): median %d, offsets with data %d of 201" % (
    curve(CR[(CR["decoder"] == "LSTM") & (CR["norm"] == "train")], False)["size"].median(),
    len(curve(CR[(CR["decoder"] == "LSTM") & (CR["norm"] == "train")], False))))
''')
s=s.replace("The decoders are those of the LSTM sessions, for both RR and LSTM, so the two curves come from the same\n# training days; both are scored on every 5th test bin. Readings: offset (a) signed or (b) absolute;\n# normalisation (i) the training day's or (ii) the test day's own training-trial parameters. RR from every\n# session's decoder is shown as a variant.",
 "The decoders are those of the LSTM sessions, for both RR and LSTM, so the two curves come from the same\n# training days; each is tested on every session within 100 days, scored on every 5th test bin. Readings:\n# offset (a) signed or (b) absolute; normalisation (i) the training day's or (ii) the test day's own\n# training-trial parameters.")
s=s.replace('''print("evaluations:", CR.groupby(["decoder", "subset", "norm"]).size().to_dict())''','''print("evaluations:", CR.groupby(["decoder", "norm"]).size().to_dict())''')
open(p,'w').write(s)
EOF
grep -n "variant, RR of all\|bb = both" $TMPDIR/nb2.py
```

```
287:        bb = both[both.index != 0] if True else both
```

**Agent calls Bash**

```bash
sed -i '/bb = both\[both.index != 0\] if True else both/d' $TMPDIR/nb2.py && cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && time PYTHONPATH=. LINK_SUBSET=40 LINK_DEV_ITERS=30 MPLBACKEND=Agg python $TMPDIR/nb2.py 2>&1 | sed -n '/evaluations:/,$p'
```

```
evaluations: {('LSTM', 'test'): 18, ('LSTM', 'train'): 18, ('RR', 'test'): 18, ('RR', 'train'): 18}
  offset  norm  offsets  LSTM better at fraction LSTM day0 / 1-5 / 90-100 RR day0 / 1-5 / 90-100  sharp then stable  r(normalised curves)
  signed train       15                    0.933        0.012 / nan / nan      0.292 / nan / nan              False                 0.260
  signed  test       15                    0.200        0.012 / nan / nan      0.292 / nan / nan              False                 0.756
absolute train       14                    0.929        0.012 / nan / nan      0.292 / nan / nan              False                 0.250
absolute  test       14                    0.214        0.012 / nan / nan      0.292 / nan / nan              False                 0.745
evaluations per offset (LSTM, signed): median 1, offsets with data 15 of 201
plotted per-offset means: -20.784 to 0.292 (no point outside the axes; axes auto-scaled)
                 count     50%     min     max
decoder reading                               
LSTM    a          3.0 -0.0085 -0.0442 -0.0073
        b          3.0 -0.0125 -0.0442 -0.0078
        trials     3.0 -0.0139 -0.0465 -0.0055
RR      a         40.0 -0.2256 -0.2969 -0.1603
        b         40.0 -0.4194 -0.5623 -0.2654
        trials    40.0 -0.4223 -0.5265 -0.2807
RR on the LSTM sessions only:
reading
a        -0.2258
b        -0.4138
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/venv/bin/activate && python $TMPDIR/nbbuild.py $TMPDIR/nb2.py decoding.ipynb && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=4000 --output-dir $TMPDIR/exec --output decoding.ipynb decoding.ipynb 2>&1 | tail -3; date -u
```

```
wrote decoding.ipynb 22 cells
Thu Nov 12 11:04:40 UTC 2026
[NbConvertApp] Converting notebook decoding.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 106409 bytes to /tmp/claude-1001/exec/decoding.ipynb

real	30m22.518s
user	93m53.598s
sys	1m23.915s
Thu Nov 12 11:35:03 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && cat > show.py <<'EOF'
import nbformat, sys
nb=nbformat.read(sys.argv[1],4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or (o.get('data') or {}).get('text/plain','')
        if o.get('output_type')=='error': print('ERROR', o.get('ename'), o.get('evalue'))
        if t and 'image/png' not in (o.get('data') or {}): print(t[:5000])
EOF
python show.py exec/decoding.ipynb
```

```
312 sessions; LSTM iterations 2000

loaded and fit RR on 312 sessions in 439 s; peak memory 4.29 GB
test trials per session: {75: 312} | test bins: 4093 to 7497
training bins: 16632 to 27756

same-day RR R2 (mean of 4 outputs): median 0.296, range 0.127 to 0.467

20 LSTMs in 22.4 min; seconds per fit 192 to 199 (median 194); estimate for all 312 sessions at 4 in parallel: 4.2 h of fitting alone

RR, all sessions: n = 312, median R2 0.296 (range 0.127 to 0.467), slope +0.0020 per year, p = 0.58
RR without scaler (code), all sessions: n = 312, median R2 0.294 (range 0.127 to 0.466), slope +0.0019 per year, p = 0.58
RR, LSTM sessions: n = 20, median R2 0.290 (range 0.211 to 0.400), slope -0.0165 per year, p = 0.11
LSTM: n = 20, median R2 0.591 (range 0.514 to 0.666), slope +0.0064 per year, p = 0.56
Pearson r between RR and LSTM same-day R2 over 20 sessions: 0.582, p = 0.007
by year (median R2):
         rr  rr_raw   lstm
date                      
2020  0.302   0.300  0.593
2021  0.290   0.288  0.606
[... 48 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb3.py",
 "content": "# %% [markdown]\n# # Temmar et al. (2025), LINK: multi-day training and fine-tuning (Figure 5)\n#\n# Paper: doi:10.52202/085713-4642. Dataset: DANDI:001201, version 0.261026.1912, streamed (the most recent\n# published version; the paper cites none, and the three published versions hold the same assets, see\n# `signals.ipynb`). Claims file: `claims/temmar-2025.yaml`. Code read: github.com/chesteklab/LINK_dataset at\n# 5e1c36a.\n#\n# | Claim | Here |\n# |---|---|\n# | fig5a-multiday-short-term | tested on 12 day-0 sessions, 1 and 5 training sessions |\n# | fig5a-long-term-decay | tested on the same models |\n# | fig5b-finetune | blocked, too large (the estimate is computed below) |\n#\n# Why a subset. Each LSTM takes about 195 s to train when four train at once on this runner\n# (`decoding.ipynb` prints the times). The paper trains 5 LSTMs on each of 283 day-0 sessions, 1415 fits,\n# about 19 hours here. The criteria of both Figure 5A claims compare only 1 and 5 training sessions, so\n# only those two are trained, on 12 day-0 sessions spread evenly over the eligible ones, chosen before\n# any result was seen: 24 fits.\n\n# %%\nimport os, time, resource\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport multiprocessing as mp\nfrom concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor\nfrom scipy.optimize import curve_fit\nimport link\n\nT0 = time.time()\nITERS = int(os.environ.get(\"LINK_DEV_ITERS\", link.LSTM_ITERS))   # 2000 (paper); lowered only while developing\nN_DAY0 = int(os.environ.get(\"LINK_DEV_NDAY0\", \"12\"))              # 12 day-0 sessions (see above)\nEVAL_EVERY = 5      # score every 5th test bin (cost)\nHORIZON = 180       # paper, Section 4.3: evaluated on all sessions within 180 days of day 0\nA = link.assets()\ncounts = A.groupby(\"date\").size()\nsingle = A[A[\"date\"].map(counts) == 1].reset_index(drop=True)      # paper, Section 4.3: days with two sessions excluded\neligible = single.index[10:]                                       # and the first 10 sessions\nprint(f\"{len(A)} sessions; on single-session days {len(single)}; eligible day-0 sessions {len(eligible)} \"\n      f\"(the Figure 5A legend reports 283 days)\")\nday0_idx = eligible[np.linspace(0, len(eligible) - 1, N_DAY0).round().astype(int)]\nprint(\"day-0 sessions:\", [single[\"date\"][i].date().isoformat() for i in day0_idx])\n\n# %% [markdown]\n# ## Load the sessions needed\n#\n# For each day 0, its training sessions (the latest 1 or 5 single-session days up to and including day 0)\n# and every single-session day within 180 days after it.\n\n# %%\nneed = set()\nfor i in day0_idx:\n    need.update(range(i - 4, i + 1))\n    d0 = single[\"date\"][i]\n    need.update(single.index[(single[\"date\"] >= d0) & (single[\"date\"] <= d0 + pd.Timedelta(days=HORIZON))])\nneed = sorted(need)\n\n\ndef load(i):\n    s = link.read_session(single[\"asset_id\"][i], tcr=False)\n    (xtr, ytr), (xte, yte) = link.split(s)\n    return i, {\"date\": single[\"date\"][i], \"xtr\": xtr, \"ytr\": ytr, \"xte\": xte, \"yte\": yte}\n\n\nt = time.time()\nwith ThreadPoolExecutor(4) as ex:\n    SES = dict(ex.map(load, need))\nprint(f\"loaded {len(SES)} sessions in {time.time() - t:.0f} s; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% [markdown]\n# ## Train and evaluate\n#\n# The LSTM and its training are those of `decoding.ipynb` (Appendix C.1). For k training sessions the\n# training bins of the k sessions are z-scored together (one mean and SD per channel), the windows never\n# cross a session boundary, and the model sees 2000 batches in all. Every model is then evaluated on the\n# hold-out trials of each session within 180 days after day 0, with input normalisation held at the\n# training parameters (Appendix C.1, \"For the analyses in Figure 5\").\n\n# %%\ndef task(arg):\n    i, k = arg\n    t0 = time.time()\n    tr = [SES[j] for j in range(i - k + 1, i + 1)]\n    mu, sd = link.zparams(np.concatenate([s[\"xtr\"] for s in tr]))\n    segs = [(((s[\"xtr\"] - mu) / sd).astype(np.float32), s[\"ytr\"]) for s in tr]\n    state, onorm = link.lstm_train(segs, seed=42, iters=ITERS)\n    fit_s = time.time() - t0\n    d0 = SES[i][\"date\"]\n    rows = []\n    for j, s in SES.items():\n        rel = (s[\"date\"] - d0).days\n        if j < i or rel > HORIZON:\n            continue\n        p = link.lstm_predict(state, onorm, ((s[\"xte\"] - mu) / sd).astype(np.float32), every=EVAL_EVERY)\n        rows.append({\"day0\": d0, \"k\": k, \"test\": s[\"date\"], \"rel\": rel,\n                     \"r2\": link.r2_per_output(s[\"yte\"][::EVAL_EVERY], p).mean()})\n    return {\"rows\": rows, \"fit_s\": fit_s, \"span_days\": (d0 - tr[0][\"date\"]).days, \"k\": k, \"day0\": d0}\n\n\nt = time.time()\nwith ProcessPoolExecutor(4, mp_context=mp.get_context(\"fork\")) as ex:\n    RES = list(ex.map(task, [(i, k) for i in day0_idx for k in (1, 5)]))\nfits = np.array([r[\"fit_s\"] for r in RES])\nprint(f\"{len(RES)} fits in {(time.time() - t) / 60:.1f} min; seconds per fit {fits.min():.0f} to {fits.max():.0f}\")\nMD = pd.DataFrame([row for r in RES for row in r[\"rows\"]])\nspans = [r[\"span_days\"] for r in RES if r[\"k\"] == 5]\nprint(\"days spanned by the 5 training sessions: %d to %d\" % (min(spans), max(spans)))\nprint(\"evaluations per model: %d to %d\" % (MD.groupby([\"day0\", \"k\"]).size().min(), MD.groupby([\"day0\", \"k\"]).size().max()))\n\n# %% [markdown]\n# ## fig5a-multiday-short-term\n#\n# > Training the LSTM on up to five consecutive past sessions reduces the initial drop in performance within\n# > about 5 days of training and improves performance over time, but slightly lowers day-0 performance.\n\n# %% tags=[\"claim:fig5a-multiday-short-term\"]\ncurve = MD.groupby([\"k\", \"rel\"])[\"r2\"].mean().unstack(0)\nrows = []\nfor k in (1, 5):\n    c = curve[k].dropna()\n    d0 = c.get(0, np.nan)\n    near = c.loc[1:5].mean()\n    rows.append({\"k\": k, \"day0 R2\": d0, \"mean R2 days 1-5\": near, \"drop\": d0 - near,\n                 \"mean days 6-30\": c.loc[6:30].mean(), \"mean days 31-180\": c.loc[31:180].mean(),\n                 \"relative days with data 1-5\": int(c.loc[1:5].notna().sum())})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nper = MD.pivot_table(index=[\"day0\", \"test\"], columns=\"k\", values=\"r2\")\nper[\"rel\"] = [(t - d).days for d, t in per.index]\nfor lab, sel in ((\"day 0\", per[\"rel\"] == 0), (\"days 1-5\", per[\"rel\"].between(1, 5)),\n                 (\"days 6-180\", per[\"rel\"].between(6, 180))):\n    d = per[sel]\n    print(f\"paired, {lab}: {len(d)} evaluations, 5 sessions higher in {(d[5] > d[1]).mean():.3f}, \"\n          f\"mean difference {(d[5] - d[1]).mean():+.4f}\")\nprint(\"per day 0 (day-0 R2, k=1 / k=5):\")\nprint(per[per[\"rel\"] == 0][[1, 5]].round(3).to_string())\n\n# %% [markdown]\n# ## fig5a-long-term-decay\n#\n# > Double-exponential fits to the single-session and five-session conditions over 0 to 180 days show steeper\n# > decay for single-session training; the initial decay decreases with more training sessions, but the\n# > long-term decay is not significantly affected.\n\n# %% tags=[\"claim:fig5a-long-term-decay\"]\ndef dexp(x, a, b, c, d):\n    return a * np.exp(b * x) + c * np.exp(d * x)\n\n\nfitres = {}\nfor k in (1, 5):\n    c = curve[k].dropna()\n    try:\n        p, cov = curve_fit(dexp, c.index.to_numpy(float), c.to_numpy(), p0=(0.374, 0.00365, 0.134, 0.140), maxfev=10000)\n        se = np.sqrt(np.diag(cov))\n        fast, slow = (1, 3) if abs(p[1]) > abs(p[3]) else (3, 1)\n        res = c.to_numpy() - dexp(c.index.to_numpy(float), *p)\n        fitres[k] = {\"params\": p, \"se\": se, \"fast\": fast, \"slow\": slow, \"drop5\": dexp(0, *p) - dexp(5, *p),\n                     \"rmse\": float(np.sqrt(np.mean(res ** 2)))}\n        print(f\"k={k}: a={p[0]:.4f} b={p[1]:.4f} c={p[2]:.4f} d={p[3]:.5f}; initial rate {p[fast]:.4f} \"\n              f\"(95% {p[fast] - 1.96 * se[fast]:.4f} to {p[fast] + 1.96 * se[fast]:.4f}); long-term rate {p[slow]:.5f} \"\n              f\"(95% {p[slow] - 1.96 * se[slow]:.5f} to {p[slow] + 1.96 * se[slow]:.5f}); predicted drop day 0 to 5 \"\n              f\"{fitres[k]['drop5']:.4f}; residual RMS {fitres[k]['rmse']:.4f}; points {len(c)}\")\n    except Exception as e:\n        print(f\"k={k}: fit failed: {e}\")\nif len(fitres) == 2:\n    f1, f5 = fitres[1], fitres[5]\n    lo = lambda f, j: f[\"params\"][j] - 1.96 * f[\"se\"][j]\n    hi = lambda f, j: f[\"params\"][j] + 1.96 * f[\"se\"][j]\n    overlap = not (hi(f1, f1[\"slow\"]) < lo(f5, f5[\"slow\"]) or hi(f5, f5[\"slow\"]) < lo(f1, f1[\"slow\"]))\n    print(\"initial rate more negative for k=1:\", f1[\"params\"][f1[\"fast\"]] < f5[\"params\"][f5[\"fast\"]],\n          \"| larger predicted drop to day 5 for k=1:\", f1[\"drop5\"] > f5[\"drop5\"],\n          \"| long-term rate intervals overlap:\", overlap,\n          \"| long-term rate difference (k=1 minus k=5): %.5f\" % (f1[\"params\"][f1[\"slow\"]] - f5[\"params\"][f5[\"slow\"]]))\nfig, ax = plt.subplots(figsize=(7, 3))\nfor k in (1, 5):\n    c = curve[k].dropna()\n    ax.plot(c.index, c, \".\", ms=3, label=f\"{k} session(s)\")\n    if k in fitres:\n        xx = np.arange(0, HORIZON + 1)\n        ax.plot(xx, dexp(xx, *fitres[k][\"params\"]))\nax.set_xlabel(\"days after day 0\"); ax.set_ylabel(\"R2\"); ax.legend(); plt.show()\nprint(\"plotted mean R2: %.3f to %.3f\" % (np.nanmin(curve.to_numpy()), np.nanmax(curve.to_numpy())))\n\n# %% [markdown]\n# ## fig5b-finetune: the size of the computation\n#\n# > Continual daily fine-tuning of an LSTM on 30 s to 5 min of each new session's data, over up to 200 days\n# > from 20 seed days, reduces both short- and long-term decay, and with 120 s or 300 s later decoders\n# > outperform the day-0 decode.\n#\n# Not run. The cell estimates its cost from the seed days of `continual_learning_lstm.py` (STARTING_DAYS,\n# named in the claim's criterion), the sessions within 200 days after each (CO on two-session days), the\n# fine-tuning iterations per duration of the criterion (50, 250, 250, 500), the two normalisation readings,\n# and the seconds per iteration measured above.\n\n# %% tags=[\"claim:fig5b-finetune\"]\nSTARTING_DAYS = [\"2020-07-08\", \"2020-10-02\", \"2020-12-12\", \"2021-02-27\", \"2021-04-05\", \"2021-05-05\", \"2021-06-16\",\n                 \"2021-07-09\", \"2021-07-29\", \"2021-08-19\", \"2021-09-14\", \"2021-10-27\", \"2022-01-17\", \"2022-02-21\",\n                 \"2022-04-01\", \"2022-04-21\", \"2022-06-01\", \"2022-08-05\", \"2022-09-01\", \"2022-09-30\"]\ndays = pd.Series(sorted(A[\"date\"].unique()))\npresent = [d for d in STARTING_DAYS if pd.Timestamp(d) in set(days)]\nn_later = [int(((days > pd.Timestamp(d)) & (days <= pd.Timestamp(d) + pd.Timedelta(days=200))).sum()) for d in STARTING_DAYS]\nsec_per_iter = np.median(fits) / ITERS\niters = len(STARTING_DAYS) * 2000 + sum(n_later) * (50 + 250 + 250 + 500) * 2\nprint(f\"seed days in the dataset: {len(present)} of {len(STARTING_DAYS)}; later sessions within 200 days: \"\n      f\"{min(n_later)} to {max(n_later)} per seed, {sum(n_later)} in all\")\nprint(f\"training iterations: {iters}; at {sec_per_iter:.3f} s per iteration with 4 fits at once: \"\n      f\"{iters * sec_per_iter / 4 / 3600:.1f} h, without the evaluations\")\n\n# %% [markdown]\n# ## Summary\n#\n# PLACEHOLDER\n\n# %%\nprint(f\"notebook time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && time PYTHONPATH=. LINK_DEV_NDAY0=2 LINK_DEV_ITERS=20 MPLBACKEND=Agg python $TMPDIR/nb3.py 2>&1 | tail -40
```

```
312 sessions; on single-session days 294; eligible day-0 sessions 284 (the Figure 5A legend reports 283 days)
day-0 sessions: ['2020-03-02', '2023-06-22']
loaded 25 sessions in 27 s; peak memory 0.71 GB
4 fits in 0.2 min; seconds per fit 5 to 5
days spanned by the 5 training sessions: 6 to 9
evaluations per model: 1 to 16
 k  day0 R2  mean R2 days 1-5  drop  mean days 6-30  mean days 31-180  relative days with data 1-5
 1   0.0028               NaN   NaN         -0.0230           -0.0132                            0
 5  -0.0121               NaN   NaN         -0.0369           -0.0139                            0
paired, day 0: 2 evaluations, 5 sessions higher in 0.000, mean difference -0.0149
paired, days 1-5: 0 evaluations, 5 sessions higher in nan, mean difference +nan
paired, days 6-180: 15 evaluations, 5 sessions higher in 0.200, mean difference -0.0060
per day 0 (day-0 R2, k=1 / k=5):
k                          1      5
day0       test                    
2020-03-02 2020-03-02 -0.024 -0.038
2023-06-22 2023-06-22  0.029  0.014
k=1: a=-0.4304 b=0.0118 c=0.4114 d=0.01204; initial rate 0.0120 (95% -10.0067 to 10.0308); long-term rate 0.01178 (95% -9.83715 to 9.86071); predicted drop day 0 to 5 0.0006; residual RMS 0.0203; points 16
k=5: a=-0.2010 b=0.0040 c=0.1668 d=0.00493; initial rate 0.0049 (95% -3.6922 to 3.7021); long-term rate 0.00395 (95% -3.39340 to 3.40131); predicted drop day 0 to 5 -0.0002; residual RMS 0.0204; points 16
initial rate more negative for k=1: False | larger predicted drop to day 5 for k=1: True | long-term rate intervals overlap: True | long-term rate difference (k=1 minus k=5): 0.00783
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude-1001/nb3.py'
s=open(p).read()
old='''eligible = single.index[10:]                                       # and the first 10 sessions'''
new='''eligible = single.index[10:-1]   # and the first 10 sessions; the last, with no later session to test on, is left out'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && python $TMPDIR/nbbuild.py $TMPDIR/nb3.py multiday.ipynb && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=4000 --output-dir $TMPDIR/exec --output multiday.ipynb multiday.ipynb 2>&1 | tail -1; date -u; python $TMPDIR/show.py $TMPDIR/exec/multiday.ipynb
```

```
wrote multiday.ipynb 14 cells
Thu Nov 12 11:37:03 UTC 2026
[NbConvertApp] Writing 53898 bytes to /tmp/claude-1001/exec/multiday.ipynb

real	26m52.506s
user	81m22.176s
sys	0m37.647s
Thu Nov 12 12:03:56 UTC 2026
312 sessions; on single-session days 294; eligible day-0 sessions 283 (the Figure 5A legend reports 283 days)
day-0 sessions: ['2020-03-02', '2020-11-05', '2021-03-22', '2021-06-08', '2021-07-28', '2021-09-14', '2022-01-24', '2022-04-11', '2022-08-01', '2022-10-12', '2023-03-10', '2023-06-21']

loaded 282 sessions in 296 s; peak memory 3.28 GB

24 fits in 21.9 min; seconds per fit 192 to 200
days spanned by the 5 training sessions: 7 to 24
evaluations per model: 2 to 80

 k  day0 R2  mean R2 days 1-5   drop  mean days 6-30  mean days 31-180  relative days with data 1-5
 1   0.5868           -0.5020 1.0888         -0.6077           -0.4705                            5
 5   0.5404           -0.2508 0.7913         -0.4539           -0.5919                            5
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/addres.py <<'EOF'
import re, sys
def add(path, results, summary):
    s = open(path).read()
    for tag, text in results.items():
        i = s.index(f'tags=["claim:{tag}"]')
        j = s.index("\n# %%", i + 10)
        md = "\n# %% [markdown]\n" + "\n".join("# " + l if l else "#" for l in text.strip().split("\n")) + "\n"
        s = s[:j] + "\n" + md.rstrip("\n") + s[j:]
    s = s.replace("# ## Summary\n#\n# PLACEHOLDER", "# ## Summary\n#\n" + "\n".join("# " + l if l else "#" for l in summary.strip().split("\n")))
    open(path, "w").write(s)
EOF
date -u
```

```
Thu Nov 12 12:05:01 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/res1.py <<'EOF'
import sys; sys.path.insert(0, sys.argv[1]); from addres import add
R = {
"dataset-sessions": """**Result: reproduced.** The pinned version holds 312 session files on 303 dates spanning 1,242 days (2020-01-27 to 2023-06-22); on 9 dates there are two files, each a CO and an RD session, and every session has 375 trials. All five counts match. The days after implant (349 to 1591) cannot be compared: the files and the dandiset metadata give the subject's date of birth but no implant date.""",
"dataset-contents": """**Result: partially reproduced.** Every one of the 312 files holds 96-channel SpikingBandPower and ThresholdCrossings series and the four position and velocity series on one shared timestamp vector, a trials table with every column Appendix B.3 lists, and an electrodes table with array, bank, row and column. The one gap is the impedance: 81 files have no `imp` column at all. Appendix A.2 says that no impedances are reported for a session without a measurement within three weeks, so the gap may be what the paper describes, but the criterion asks for the column in every file. Within a run of bins the timestamps step by 0.019 to 0.021 s; some sessions also have pauses between runs of bins (the data check gives their count and length). Velocity is the forward difference of the binned position (velocity at bin t is position at t + 1 minus position at t) except at the bins listed above, and so is not the backward difference.""",
"figs2-throughput-improves": """**Result: reproduced.** Under all three readings the daily mean throughput rises over the dataset: reading (a) by 0.238 bits/s per year (r = 0.31, p = 5.8e-08), (b) by 0.068 (p = 7.7e-37) and (c) by 0.455 (p = 2.8e-20), over 303 days. Under reading (a) the yearly means rise from 3.66 in 2020 to 4.33 in 2022 and fall to 3.85 in the six months of 2023, so the rise is not monotonic. Under readings (a) and (c), 998 trials whose length (stop minus start) is at most the 750 ms hold get no throughput.""",
"fig2a-sbp-decline": """**Result: reproduced, under unit reading (b).** With the values as stored (microvolts by the files' conversion factor of 1e-6 V), the linear fit to 29,088 channel-day means has a slope of -1.110e-03 per day, -0.0338 microvolts per month, within the tolerance of -0.033 +- 0.0033, and the per-day value equals the supplement's -1.11e-3. Reading (a), the stored values times 0.25, gives -0.0084 per month, outside it. The code's converter divides the stored SBP by 0.25 before its analysis multiplies by 0.25, so the code's own path is reading (b).""",
"fig2b-active-channels-decrease": """**Result: reproduced.** The count of channels with mean TCR above 1 Hz falls by 6.5 channels per year (slope -0.0177 per day, r = -0.39, p = 2.6e-12, 303 days), from a mean of 44.6 in the first 30 sessions to 25.9 in the last 30.""",
"fig2c-pr-decline": """**Result: reproduced.** The participation ratio of the active channels falls by 0.0708 per month (p = 1.5e-08, 303 days), within the tolerance of -0.07 +- 0.007; using every session as a point gives -0.0720.""",
"fig2c-ten-dimensions": """**Result: reproduced, under reading (a).** The daily PR is at most 10 on 84.8% of days (median 7.86). The top 10 PCs explain more than half the variance on every day (reading b) and more than 80% on 44.6% of days (reading c, not reproduced under it).""",
"figs4-bank-slopes": """**Result: reproduced, under unit reading (b).** With the stored values, the slopes are -5.84e-04 (lateral, bank A), -1.34e-03 (bank B), -1.40e-03 (bank C) and -1.11e-03 (all channels) per day, all four equal to the supplement's values to the printed digits, and the lateral bank has the lowest mean SBP (2.19, against 2.55 and 3.57). The two fit readings give the same slopes, since every day has a value for every channel. Under unit reading (a) every slope is a quarter of these, outside the tolerances.""",
"figs5-active-inactive-slopes": """**Result: partially reproduced.** With the stored values and channel-session points (fit reading a), the active channels' slope is -1.261e-03 per day, within the tolerance of -1.29e-3, and inactive channels have the lower mean SBP (2.15 against 3.74). The inactive slope is -5.36e-04: the size of the supplement's 0.54e-3, with the opposite sign, so it is outside the tolerance. The negative sign agrees with Section 4.1 ("All categories saw steady decreases in average SBP"). Fit reading (b) gives -1.162e-03 and -4.50e-04.""",
"fig2d-population-drift": """**Result: partially reproduced.** The centroids move: the first and last quarters' centroids are 17.04 apart in the space of the top 3 PCs, against a mean within-quarter standard deviation of 2.02, and the first PC's quarterly centroid falls from 12.28 to -4.60. The spread is less stable than the rule asks: 3 quarters (2021Q1, 2022Q3, 2023Q2) have a 3-PC standard deviation more than 25% from the median, where the rule allows two. At 50% two quarters (2021Q1 at 4.27 and 2022Q3 at 2.80 against a median of 1.83) stand out, as the paper's "except for two quarters" says.""",
"fig2e-trajectories-separable": """**Result: reproduced.** Classified by direction from their 37-bin trajectories in the day's top 3 PCs, trials are classified with accuracy 0.212 in 2020 (15,951 trials) and 0.220 in 2023 (16,511 trials), against chance of 1/8 (binomial p below 1e-200 in both years), the majority-class rate (0.158 and 0.184) and permuted labels (0.125 and 0.114). The code's alignment (2 SD, from 150 ms before) gives 0.232 and 0.221, but keeps only 24,139 of 116,683 trials. Separable here means better than chance; the accuracies are low in absolute terms.""",
"fig3b-two-channels": """**Result: reproduced.** Channel 7 has a circular median tuning angle of 81.1 degrees (MRS flexion is 90), a circular IQR of 18.6 degrees and a median strength of 0.0245, sixth of 96 channels (median over channels 0.0070). Channel 32 has a circular IQR of 146.9 degrees, sixth largest (median over channels 46.9). Their mean TCR over the dataset is 3.12 and 36.45 Hz.""",
"fig3cd-tuning-stable": """**Result: reproduced, under reading (b).** 77.1% of all channels (and 77.4% of the 53 active ones) have a circular IQR of tuning angle below 90 degrees. Under reading (a), below 45 degrees, it is 47.9% and 45.3%, under half, so the outcome rests on the wider threshold. The median circular IQR is 46.9 degrees.""",
"fig3d-weak-channels-low-tcr": """**Result: reproduced.** Over the 96 channels, median tuning strength and median daily TCR correlate with Spearman rho = 0.925 (p = 3e-41), and the 24 channels in the lowest quartile of strength have a median TCR of 0.40 Hz against 0.87 Hz for the others (Mann-Whitney p = 5.3e-11).""",
"fig3e-array-tuning": """**Result: not reproduced.** With the arrays as the files label them, the medial channels' circular median angles are near -130 degrees (extension of both fingers): 2 of 64 (0.031) fall in the flexion sector of -22.5 to 112.5 degrees. Most lateral channels are tuned to flexion (12 to 88 degrees), and 2 of 32 (0.062) fall in the extension sector. The pattern is the paper's with the array names swapped: read that way, 81.2% of the file's lateral channels are in the flexion sector and 92.2% of its medial channels in the extension sector, though more of the flexion channels are within 45 degrees of IDX flexion (17) than of MRS flexion (11). The files' labels agree with Figure S1 (channel 47 is medial, row 5, column 5) and with the lower SBP of the lateral bank (figs4), so the files and this sentence of the paper disagree on which array is which, or the paper's angles have another sign convention.""",
}
S = """| Claim | Outcome |
|---|---|
| dataset-sessions | reproduced |
| dataset-contents | partially reproduced (81 files without impedances) |
| figs2-throughput-improves | reproduced |
| fig2a-sbp-decline | reproduced (stored values in microvolts) |
| fig2b-active-channels-decrease | reproduced |
| fig2c-pr-decline | reproduced |
| fig2c-ten-dimensions | reproduced (PR at most 10) |
| figs4-bank-slopes | reproduced |
| figs5-active-inactive-slopes | partially reproduced (inactive slope of opposite sign) |
| fig2d-population-drift | partially reproduced |
| fig2e-trajectories-separable | reproduced |
| fig3b-two-channels | reproduced |
| fig3cd-tuning-stable | reproduced (90-degree reading) |
| fig3d-weak-channels-low-tcr | reproduced |
| fig3e-array-tuning | not reproduced |

The decoding claims are in `decoding.ipynb` and `multiday.ipynb`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the readings each criterion names are all run and shown; the PCA of Figure 2D is computed from per-session sums, which gives the same components as a fit to the concatenated matrix; the first trial of each session, which has no previous target in the file, has no direction or throughput; tuning uses position, as the main text and code do.

What was found about the dataset: the counts match the paper exactly; the stored SBP is in microvolts, as its conversion factor says, and the code's division by 0.25 and multiplication by 0.25 cancel; ThresholdCrossings is labelled in volts though it holds integer counts per bin; 81 files have no impedance column; the files give no implant date; velocity is a forward difference; some sessions have pauses inside them; and the tuning angles by array are the paper's with the array names swapped."""
add(sys.argv[2], R, S)
EOF
cd $TMPDIR && python res1.py $TMPDIR $TMPDIR/nb1.py && grep -c "Result:" nb1.py; grep -n "92544\|24,139" nb1.py | head -3
```

```
15
583:# **Result: reproduced.** Classified by direction from their 37-bin trajectories in the day's top 3 PCs, trials are classified with accuracy 0.212 in 2020 (15,951 trials) and 0.220 in 2023 (16,511 trials), against chance of 1/8 (binomial p below 1e-200 in both years), the majority-class rate (0.158 and 0.184) and permuted labels (0.125 and 0.114). The code's alignment (2 SD, from 150 ms before) gives 0.232 and 0.221, but keeps only 24,139 of 116,683 trials. Separable here means better than chance; the accuracies are low in absolute terms.
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -i 's/but keeps only 24,139 of 116,683 trials/but drops 92,544 of 116,683 trials, whose window starts before the trial or that have no onset/' $TMPDIR/nb1.py && date -u
```

```
Thu Nov 12 12:05:40 UTC 2026
```

**Agent**

Now the results for the decoding and multi-day notebooks.

**Agent calls Bash**

```bash
cat > $TMPDIR/res23.py <<'EOF'
import sys; sys.path.insert(0, sys.argv[1]); from addres import add
R2 = {
"fig4a-sameday-stable": """**Result: reproduced, with the LSTM on 20 of 312 sessions.** Same-day R2 shows no decline: the RR slope over all 312 sessions is +0.0020 per year (p = 0.58) and the LSTM slope over its 20 sessions +0.0064 per year (p = 0.56). The two decoders' R2 correlate across the 20 sessions (Pearson r = 0.582, p = 0.007). RR without input normalisation, as the code fits it, gives the same (+0.0019 per year, p = 0.58). Median R2 is 0.296 for RR and 0.591 for the LSTM.""",
"fig4a-lstm-beats-rr": """**Result: reproduced on the 20 sessions tested.** The LSTM's same-day R2 is above RR's on 20 of 20 sessions, by 0.223 to 0.385 (median 0.301), so no session needed the extra seeds. The other 292 sessions were not tested with the LSTM; RR's highest same-day R2 over all 312 sessions (0.467) is below the lowest LSTM R2 seen (0.514).""",
"fig4bc-dof-accuracy": """**Result: reproduced.** For RR (312 sessions) the median R2 is 0.316 and 0.362 for IDX and MRS position against 0.220 and 0.286 for velocity; for the LSTM (20 sessions) 0.645 and 0.663 against 0.480 and 0.576. Both orderings hold for both decoders. Per session the orderings hold less often: position above velocity for both fingers in 62.8% (RR) and 75.0% (LSTM) of sessions, MRS above IDX for both in 50.6% and 60.0%.""",
"fig4d-cross-day-decay": """**Result: reproduced, under the readings of absolute offset and test-day normalisation.** For the 20 decoders of each type, each tested on every session within 100 days, the LSTM's mean R2 is above RR's at all 101 absolute offsets. The LSTM falls from 0.583 on day 0 to 0.376 at 1 to 5 days and 0.186 at 90 to 100 days, and RR from 0.294 to 0.088 and -0.005, so both drop more in the first five days than over the next 85 to 95. The two curves, each divided by its day-0 value, correlate with r = 0.903. Under the other readings the LSTM is also better at every offset, but the shapes correlate less (r = 0.887 signed with test-day normalisation, 0.526 and 0.391 with the training day's normalisation). With the training day's normalisation RR R2 falls to about -13 to -17 within days and the signed test-day curve does not meet the sharp-then-stable part. So the outcome rests on the readings named.""",
"suppc1-shuffle-baseline": """**Result: partially reproduced.** Shuffled hold-out data give negative R2 for both decoders under every reading. Under reading (a), raw bins permuted, the LSTM's median over its 20 sessions is -0.154, within the tolerance of -0.156, but RR's median over 312 sessions is -0.223, outside the tolerance of -0.166 +- 0.0166 (its per-session values range from -0.363 to -0.149, so a single session can give -0.166). Under reading (b), whole windows permuted, the medians are -0.410 (RR) and -0.596 (LSTM), and whole trials give -0.409 and -0.533.""",
"fig2a-irregular-shifts": """**Result: partially reproduced.** By the criterion's rule, 38 of 42 days from July to November 2022 have five or more channels shifting on the same day (up to 66). The rule does not single out that period: it flags 237 of the 243 other days with a 30-day baseline as well. Decoding in the window: RR's median same-day R2 there (0.321, 45 sessions) is inside the 10th to 90th percentile range of all sessions (0.220 to 0.360). The LSTM's median there (0.652, 3 sessions) is just above its 90th percentile (0.651), so that part fails, in the direction of better, not worse, decoding.""",
}
S2 = """| Claim | Outcome |
|---|---|
| fig4a-sameday-stable | reproduced (LSTM on 20 sessions) |
| fig4a-lstm-beats-rr | reproduced on the 20 sessions tested |
| fig4bc-dof-accuracy | reproduced |
| fig4d-cross-day-decay | reproduced under one pair of readings |
| suppc1-shuffle-baseline | partially reproduced |
| fig2a-irregular-shifts | partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the LSTM is trained on 20 of the 312 sessions (every 16th), for time; cross-day R2 is scored on every 5th test bin; the cross-day curves use the decoders of those 20 sessions for both RR and the LSTM; the LSTM's noise is 0.1 white and 0.2 bias as the Methods state, while the code passes them the other way round; the test set is the 75 trials after the first 300, to the end of the file.

What was found about the dataset: every session has 375 trials, so the 300/75 split is exact; same-day decoding is stable across the 3.5 years."""
add(sys.argv[2], R2, S2)
R3 = {
"fig5a-multiday-short-term": """**Result: reproduced, on 12 day-0 sessions.** Against one training session, five raise the mean R2 over relative days 1 to 5 from -0.502 to -0.251, shrink the drop from day 0 to those days from 1.089 to 0.791, and lower day-0 R2 from 0.587 to 0.540 (lower on 11 of 12 day-0 sessions). Paired over the 16 evaluations at 1 to 5 days, five sessions are better in 81% of them. The R2 values after day 0 are negative because the input normalisation is held at the training day's, as Appendix C.1 says for Figure 5.""",
"fig5a-long-term-decay": """**Result: not reproduced.** Fit to the mean R2 per relative day from 12 day-0 sessions, the double exponentials are degenerate. For one session the fit has a growing component of near-zero amplitude and a single decay at -0.0029 per day. For five sessions the fit has two growing components of opposing amplitude. Neither condition holds: the initial rate is not more negative for one session and the predicted drop from day 0 to day 5 is not larger (-0.009 against 0.014). The long-term rates' intervals overlap, but they are very wide (five sessions: -1.48 to 1.50 per day). The residual RMS is 0.40 and 0.65 R2 on a curve that ranges down to -3.98, so 12 day-0 sessions are likely too few for this fit; the raw short-term comparison above does show the smaller drop with five sessions.""",
"fig5b-finetune": """**Result: blocked, too large.** The fine-tuning runs 20 seed days, each followed by 32 to 85 sessions within 200 days, four durations and two normalisation readings: 2,446,600 training iterations, about 16.5 hours at the measured 0.097 s per iteration with four fits at once, beyond the notebook limit and the run's time. It was not run.""",
}
S3 = """| Claim | Outcome |
|---|---|
| fig5a-multiday-short-term | reproduced (12 day-0 sessions) |
| fig5a-long-term-decay | not reproduced |
| fig5b-finetune | blocked, too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: 12 of the 283 day-0 sessions, and only 1 and 5 training sessions, for time; scored on every 5th test bin; the code's variant of the multi-day trainer (90/10 split, refit normalisation, no noise) was not run.

What was found about the dataset: dropping the 9 two-session days, the first 10 sessions and the last session (which has no later session) leaves 283 day-0 sessions, the count in the Figure 5A legend."""
add(sys.argv[3], R3, S3)
EOF
cd $TMPDIR && python res23.py $TMPDIR $TMPDIR/nb2.py $TMPDIR/nb3.py && grep -c "Result:" nb2.py nb3.py; date -u
```

```
nb2.py:6
nb3.py:3
Thu Nov 12 12:06:06 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='nb2.py'; s=open(p).read()
old="With the training day's normalisation RR R2 falls to about -13 to -17 within days and the signed test-day curve does not meet the sharp-then-stable part."
assert old in s
s=s.replace(old,"With the training day's normalisation RR's mean R2 is -13.4 to -17.9 at the offsets past day 0, and the signed test-day curves do not meet the sharp-then-stable part.")
open(p,'w').write(s)
p='nb3.py'; s=open(p).read()
old="and a single decay at -0.0029 per day."
assert old in s
s=s.replace(old,"and a single negative-amplitude component with rate -0.0029 per day.")
open(p,'w').write(s)
EOF
date -u
```

```
Thu Nov 12 12:06:16 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "REGISTRY_PYTHON\|DEFAULT_PYTHON\|def python_of" -A6 tools/entry.py | head -30; cat entries/ashworth-2025/requirements.in; grep -n "python:" entries/ashworth-2025/entry.yaml
```

```
406:def python_of(entry_dir: Path) -> str:
407-    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
408-    (entries from before the field), else the registry's default for new entries, PYTHON_VERSION."""
409-    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text()) or {}
410-    if entry.get("python"):
411-        return str(entry["python"])
412-    lock_file = entry_dir / "requirements.lock.txt"
numpy<2.4
scipy
pandas
matplotlib
h5py
remfile
pymc<6
arviz<0.23
torch @ https://download.pytorch.org/whl/cpu/torch-2.15.0%2Bcpu-cp313-cp313-manylinux_2_28_x86_64.whl
```

**Agent calls Bash**

```bash
grep -n "^PYTHON_VERSION" tools/entry.py; cd entries/temmar-2025 && for n in 1 2 3; do :; done; . $TMPDIR/venv/bin/activate; python $TMPDIR/nbbuild.py $TMPDIR/nb1.py signals.ipynb; python $TMPDIR/nbbuild.py $TMPDIR/nb2.py decoding.ipynb; python $TMPDIR/nbbuild.py $TMPDIR/nb3.py multiday.ipynb; ls
```

```
63:PYTHON_VERSION = "3.13"
wrote signals.ipynb 59 cells
wrote decoding.ipynb 28 cells
wrote multiday.ipynb 17 cells
__pycache__
decoding.ipynb
link.py
multiday.ipynb
signals.ipynb
```

**Agent calls Bash**

```bash
rm -rf __pycache__ && cat > requirements.in <<'EOF'
numpy<2.4
scipy
pandas
matplotlib
h5py
remfile
requests
scikit-learn
torch @ https://download.pytorch.org/whl/cpu/torch-2.15.0%2Bcpu-cp313-cp313-manylinux_2_28_x86_64.whl
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: temmar-2025
type: reproduction
title: Long-term intracortical neural activity and kinematics, LINK (Temmar et al. 2025)
description: Tests the findings of Temmar et al. (2025) on dandiset 001201, which holds 312 sessions of
  spiking-band power, threshold crossings and finger kinematics from one macaque over 3.5 years. It checks
  the dataset's counts and contents, the decline of neural signals over time, single-channel tuning,
  same-day and cross-day decoding with ridge regression and an LSTM, and multi-day training. The LSTM
  analyses run on subsets of sessions for time, and the continual fine-tuning is too large to run.
license: Apache-2.0
notebooks:
- path: signals.ipynb
  title: The dataset, neural signals and tuning over time (Figures 2, 3, S2, S4, S5)
  runtime_minutes: 8
- path: decoding.ipynb
  title: Same-day and cross-day decoding (Figure 4, Appendix C.1)
  runtime_minutes: 31
- path: multiday.ipynb
  title: Multi-day training and fine-tuning (Figure 5)
  runtime_minutes: 27
helpers:
- link.py
related:
- id: dandi:001201/0.261026.1912
  relation: uses_data
- id: doi:10.52202/085713-4642
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/temmar-2025 2>&1 | tail -3 && python tools/entry.py check entries/temmar-2025 2>&1 | tail -20
```

```
wrote temmar-2025/requirements.lock.txt (Python 3.13, with hashes)
error: entries/temmar-2025/decoding.ipynb: no code cell tagged `sanity` (the data check; see docs/protocol.md)
error: entries/temmar-2025/multiday.ipynb: no code cell tagged `sanity` (the data check; see docs/protocol.md)
2 error(s)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='nb2.py'; s=open(p).read()
anchor='''# %%
def z(x, mu, sd):'''
assert anchor in s
s=s.replace(anchor,'''# %% tags=["sanity"]
SS = pd.DataFrame([{"date": s["date"], "style": s["style"], "n_test_trials": s["n_test_trials"]} for s in SES])
print("sessions by style:", SS["style"].value_counts().to_dict(), "| by year:", SS["date"].dt.year.value_counts().sort_index().to_dict())
print("days:", SS["date"].nunique(), "| sessions with an LSTM:", sum(1 for s in SES if s["i"] % LSTM_EVERY == 0))
print("test trials per session:", SS["n_test_trials"].value_counts().to_dict())
print("hold-out SBP (stored units, microvolts): %.3f to %.3f" % (min(s["xte"].min() for s in SES), max(s["xte"].max() for s in SES)))
yk = np.vstack([s["yte"] for s in SES])
for n, a, b in zip(link.KIN_NAMES, yk.min(0), yk.max(0)):
    print(f"  hold-out {n}: {a:.3f} to {b:.3f}")
print("training-bin SD per channel: %.3f to %.3f (no channel constant)" % (min(s["sd"].min() for s in SES), max(s["sd"].max() for s in SES)))

''' + anchor)
open(p,'w').write(s)
p='nb3.py'; s=open(p).read()
anchor='''# %% [markdown]
# ## Train and evaluate'''
assert anchor in s
s=s.replace(anchor,'''# %% tags=["sanity"]
L3 = pd.DataFrame([{"date": v["date"], "train_bins": len(v["xtr"]), "test_bins": len(v["xte"])} for v in SES.values()])
print("sessions loaded:", len(L3), "| by year:", L3["date"].dt.year.value_counts().sort_index().to_dict())
print("training bins %d to %d, test bins %d to %d" % (L3["train_bins"].min(), L3["train_bins"].max(), L3["test_bins"].min(), L3["test_bins"].max()))
print("SBP (stored units): %.3f to %.3f" % (min(v["xte"].min() for v in SES.values()), max(v["xte"].max() for v in SES.values())))
yk = np.vstack([v["yte"] for v in SES.values()])
for n, a, b in zip(link.KIN_NAMES, yk.min(0), yk.max(0)):
    print(f"  hold-out {n}: {a:.3f} to {b:.3f}")

''' + anchor)
open(p,'w').write(s)
EOF
cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && python $TMPDIR/nbbuild.py $TMPDIR/nb2.py decoding.ipynb && python $TMPDIR/nbbuild.py $TMPDIR/nb3.py multiday.ipynb && cd ../.. && python tools/entry.py check entries/temmar-2025 2>&1 | tail -5
```

```
wrote decoding.ipynb 29 cells
wrote multiday.ipynb 18 cells
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && (PYTHONPATH=. LINK_SUBSET=6 MPLBACKEND=Agg python $TMPDIR/nb1.py 2>&1 | grep -n "Error\|gaps\|forward\|backward" ; PYTHONPATH=. LINK_SUBSET=17 LINK_DEV_ITERS=10 MPLBACKEND=Agg python $TMPDIR/nb2.py 2>&1 | grep -A8 "sessions by style" | head -12; PYTHONPATH=. LINK_DEV_NDAY0=1 LINK_DEV_ITERS=10 MPLBACKEND=Agg python $TMPDIR/nb3.py 2>&1 | grep -B2 -A6 "sessions loaded\|Error" | head -20); rm -rf __pycache__; date -u
```

```
59:ValueError: min() iterable argument is empty
sessions by style: {'CO': 9, 'RD': 8} | by year: {2020: 3, 2021: 6, 2022: 5, 2023: 3}
days: 17 | sessions with an LSTM: 2
test trials per session: {75: 17}
hold-out SBP (stored units, microvolts): 0.544 to 36.206
  hold-out idx_pos: 0.000 to 1.000
  hold-out mrs_pos: 0.000 to 1.000
  hold-out idx_vel: -0.224 to 0.286
  hold-out mrs_vel: -0.312 to 0.270
training-bin SD per channel: 0.138 to 5.409 (no channel constant)
day-0 sessions: ['2020-03-02']
loaded 20 sessions in 23 s; peak memory 0.60 GB
sessions loaded: 20 | by year: {2020: 20}
training bins 18857 to 26945, test bins 4635 to 7134
SBP (stored units): 0.675 to 71.872
  hold-out idx_pos: 0.000 to 1.000
  hold-out mrs_pos: 0.000 to 1.000
  hold-out idx_vel: -0.201 to 0.448
  hold-out mrs_vel: -0.263 to 0.338
Thu Nov 12 12:08:40 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
p='nb1.py'; s=open(p).read()
old='''print("time gaps (steps over 30 ms): %d sessions have any, %d gaps in all, %.2f to %.1f s long" % (
    sum(len(g) > 0 for g in S["gaps"]), sum(len(g) for g in S["gaps"]),
    min(np.min(g) for g in S["gap_s"] if len(g)), max(np.max(g) for g in S["gap_s"] if len(g))))'''
new='''gl = np.concatenate([np.zeros(0)] + list(S["gap_s"]))
print("time gaps (steps over 30 ms): %d sessions have any, %d gaps in all, %s s long" % (
    sum(len(g) > 0 for g in S["gaps"]), len(gl), f"{gl.min():.2f} to {gl.max():.1f}" if len(gl) else "none"))'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
cd entries/temmar-2025 && . $TMPDIR/venv/bin/activate && PYTHONPATH=. LINK_SUBSET=6 MPLBACKEND=Agg python $TMPDIR/nb1.py 2>&1 | grep -n "Error\|gaps\|forward\|backward"; rm -rf __pycache__; python $TMPDIR/nbbuild.py $TMPDIR/nb1.py signals.ipynb; cd ../.. && python tools/entry.py check entries/temmar-2025 | tail -1; date -u
```

```
55:time gaps (steps over 30 ms): 0 sessions have any, 0 gaps in all, none s long
56:velocity[t] equals pos[t+1] - pos[t] (a forward difference) except at 0 bins, 0 of which are the bin before a time gap
57:velocity[t] minus pos[t] - pos[t-1] (backward difference), largest |difference| per finger: [0.22   0.1728]
73:timestamp steps within a run of bins: [np.float64(0.019), np.float64(0.02), np.float64(0.021)] s; 0 sessions also have gaps over 30 ms (see the data check)
74:velocity is the forward difference of binned position, except at 0 bins (0 before a gap)
wrote signals.ipynb 59 cells
0 error(s)
Thu Nov 12 12:09:09 UTC 2026
```

**Agent calls Bash**

```bash
cat > entries/temmar-2025/README.md <<'EOF'
# Temmar et al. (2025), LINK, from dandiset 001201

Tests the findings of [Temmar et al. (2025)](https://doi.org/10.52202/085713-4642) on
[DANDI:001201](https://dandiarchive.org/dandiset/001201/0.261026.1912), which holds 312 sessions of
spiking-band power (SBP), threshold crossings and the kinematics of two finger groups from Monkey N,
recorded on 303 days over 3.5 years.

| Notebook | Claims |
|---|---|
| `signals.ipynb` | dataset counts and contents, throughput, SBP decline, active channels, participation ratio, bank and activity slopes, population drift, trajectories, tuning (Figures 2, 3, S2, S4, S5) |
| `decoding.ipynb` | same-day and cross-day decoding with ridge regression and an LSTM, the shuffle baseline, irregular SBP shifts (Figure 4, Appendix C.1) |
| `multiday.ipynb` | multi-day training (Figure 5A) and the size of the fine-tuning (Figure 5B) |

The LSTM is trained on 20 of the 312 sessions and the multi-day comparison on 12 of 283 day-0 sessions,
for time; the continual fine-tuning of Figure 5B is too large to run here. The outcomes, the reasons and
the differences from the paper's method are in the attempt record,
[`attempts/temmar-2025-01.yaml`](../../attempts/temmar-2025-01.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.
EOF
date -u; time python tools/entry.py all entries/temmar-2025 2>&1 | tail -15; date -u
```

```
Thu Nov 12 12:09:19 UTC 2026
Installed kernelspec registry-temmar-2025 in executed/temmar-2025/.venv/share/jupyter/kernels/registry-temmar-2025
0 error(s)
pass  signals.ipynb  (626 s)
pass  decoding.ipynb  (2004 s)
pass  multiday.ipynb  (1607 s)

real	70m48.975s
user	202m20.141s
sys	2m36.567s
Thu Nov 12 13:20:08 UTC 2026
```

**Agent**

All three notebooks pass. Now I compare the executed outputs with the conclusions.

**Agent calls Bash**

```bash
cd $TMPDIR && . venv/bin/activate && for n in signals decoding multiday; do python show.py executed/temmar-2025/$n.ipynb > out_$n.txt; done; diff <(python show.py exec/signals.ipynb) out_signals.txt | head -60; diff <(python show.py exec/decoding.ipynb) out_decoding.txt | head -60; diff <(python show.py exec/multiday.ipynb) out_multiday.txt | head -40
```

```
32c32
< 312 sessions on 303 days read in 446 s; peak memory 1.36 GB
---
> 312 sessions on 303 days read in 606 s; peak memory 1.36 GB
59c59,61
< velocity minus difference of positions, max over sessions (velocity[t] vs pos[t]-pos[t-1]): [0.6923 0.8331] | (velocity[t] vs pos[t+1]-pos[t]): [0.6926 0.8331]
---
> time gaps (steps over 30 ms): 29 sessions have any, 72 gaps in all, 1.05 to 472.9 s long
> velocity[t] equals pos[t+1] - pos[t] (a forward difference) except at 72 bins, 72 of which are the bin before a time gap
> velocity[t] minus pos[t] - pos[t-1] (backward difference), largest |difference| per finger: [0.6923 0.8331]
83,84c85,86
< timestamp steps (s): [np.float64(0.019), np.float64(0.02), np.float64(0.021), np.float64(1.046), np.float64(1.094), np.float64(1.139), np.float64(1.163), np.float64(1.309), np.float64(1.462), np.float64(1.5), np.float64(2.025), np.float64(2.028), np.float64(2.029), np.float64(2.03), np.float64(2.032), np.float64(2.033), np.float64(2.038), np.float64(2.043), np.float64(2.044), np.float64(4.035), np.float64(5.025), np.float64(5.026), np.float64(5.027), np.float64(5.029), np.float64(5.033), np.float64(5.034), np.float64(5.036), np.float64(5.037), np.float64(5.038), np.float64(5.041), np.float64(5.043), np.float64(7.536), np.float64(7.541), np.float64(7.543), np.float64(10.028), np.float64(10.029), np.float64(10.031), np.float64(10.032), np.float64(10.033), np.float64(10.034), np.float64(10.035), np.float64(10.038), np.float64(10.039), np.float64(10.04), np.float64(10.041), np.float64(10.043), np.float64(10.044), np.float64(32.429), np.float64(240.058), np.float64(363.802), np.float64(443.403), np.float64(470.97), np.float64(472.915)] (all within 1 ms of 0.02)
< velocity equals pos[t] - pos[t-1] to within [0.6923  0.83312]
---
> timestamp steps within a run of bins: [np.float64(0.019), np.float64(0.02), np.float64(0.021)] s; 29 sessions also have gaps over 30 ms (see the data check)
> velocity is the forward difference of binned positi
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/temmar-2025 2>&1 | tail -3; ls schemas/; grep -n "assumed\|measured\|blocked_by\|found\|enum" schemas/attempt* | head -40
```

```
wrote executed/temmar-2025/handover
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
66:            "enum": [
157:          "enum": [
243:            "enum": [
249:            "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."
251:          "blocked_by": {
253:            "enum": [
276:          "measured": {
299:          "assumed": {
300:            "description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).",
304:            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
313:                "enum": [
320:              "blocked_by": {
322:                "enum": [
351:                "blocked_by",
359:                "assumed": {
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,120p schemas/attempt.schema.json | grep -n '"required"\|"properties"\|"[a-z_]*": {' | head -60; sed -n 270,300p schemas/attempt.schema.json
```

```
7:  "required": [
16:  "properties": {
17:    "schema_version": {
20:    "id": {
24:    "datasets": {
28:      "items": {
32:        "required": [
38:        "properties": {
39:          "archive": {
44:          "id": {
49:          "version": {
54:          "modified": {
59:          "doi": {
64:          "relation": {
72:        "if": {
73:          "properties": {
74:            "archive": {
79:        "then": {
80:          "properties": {
81:            "id": {
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec && cat > $TMPDIR/rec/make.py <<'EOF'
import yaml
NB1, NB2, NB3 = "signals.ipynb", "decoding.ipynb", "multiday.ipynb"
LSTM_SUB = ("The LSTM is trained on 20 of the 312 sessions (every 16th in date order, chosen before any result), "
            "for time; one fit takes about 194 s with four at once, so all 312 would take about 4.2 hours of fitting.")
def o(claim, outcome, nb, notes, deviations=None, measured=None, blocked_by=None, assumed=None):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    d["notebook"] = nb
    d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed is not None: d["assumed"] = assumed
    return d

outcomes = [
o("dataset-sessions", "reproduced", NB1,
  "312 session files on 303 dates, 2020-01-27 to 2023-06-22, a span of 1242 days. On 9 dates there are two files, each a CO "
  "and an RD session. Every session has 375 trials. The days after implant (349 to 1591) were not compared, as the "
  "criterion asks only when the dataset gives the implant date; it gives the date of birth (2012-05-26) and no implant date.",
  measured=[312, 303, 1242, 9, 375]),
o("dataset-contents", "partially_reproduced", NB1,
  "All 312 files hold 96-channel SpikingBandPower and ThresholdCrossings and the four kinematic series on one timestamp "
  "vector, the trials columns of Appendix B.3, and electrodes with array, bank, row and column. 81 files have no imp "
  "column (14 in 2020, 2 in 2021, 49 in 2022, 16 in 2023). Appendix A.2 says no impedances are reported for a session "
  "without a measurement within three weeks, so this may be the documented behaviour, but the criterion asks for the "
  "column in every file. Within runs the timestamps step 0.019 to 0.021 s; 29 sessions have 72 pauses of 1.05 to "
  "472.9 s. Velocity at bin t equals position at t+1 minus position at t in every bin except the 72 bins before a pause, "
  "a forward difference.",
  deviations=["The criterion's velocity check, against the difference of consecutive binned positions, is shown both "
              "ways; the data match the forward difference, not the backward one."]),
o("figs2-throughput-improves", "reproduced", NB1,
  "Daily mean throughput rises under all three readings, (a) 0.238 bits/s per year (r = 0.31, p = 5.8e-08), (b) 0.068 "
  "(p = 7.7e-37), (c) 0.455 (p = 2.8e-20), over 303 days. Under (a) the yearly means are 3.66, 3.96, 4.33 and 3.85 for "
  "2020 to 2023. 998 trials whose length is at most the 750 ms hold get no throughput under (a) and (c).",
  deviations=["Throughput's formula is cited to Nason et al. 2021 and not given in the paper or its code; the three "
              "readings of the criterion are run and agree.",
              "The first trial of each session, whose starting targets are not in the file, has no throughput.",
              "The p < 0.05 threshold is the criterion's standard choice; the paper gives no test."]),
o("fig2a-sbp-decline", "reproduced", NB1,
  "With the stored values (microvolts by their conversion factor), the fit to 29,088 channel-day means gives "
  "-1.110e-03 per day, -0.0338 per month, inside -0.033 +- 0.0033. Reading (a), the stored values times 0.25, gives "
  "-0.0084 per month. The code's converter divides the stored SBP by 0.25 and its analysis multiplies by 0.25, so the "
  "code's path is reading (b).",
  measured=-0.0338,
  deviations=["The unit of SBP was open between two readings named in the criterion; reading (b) matches and (a) does not."]),
o("fig2a-irregular-shifts", "partially_reproduced", NB2,
  "Under the criterion's rule 38 of 42 days in July to November 2022 have at least five channels shifting on the same day "
  "(up to 66), so the shift part holds; but the rule flags 237 of the 243 other days that have a 30-day baseline, so it "
  "does not single out that period. RR's median same-day R2 in the window is 0.321 (45 sessions), inside its 10th to 90th "
  "percentile range of 0.220 to 0.360. The LSTM's is 0.652 (3 sessions), just above its 90th percentile of 0.651 over 20 "
  "sessions, so that part fails, in the direction of better decoding.",
  deviations=[LSTM_SUB,
              "A day's 30-day baseline needs at least 3 earlier days; days with fewer have no shift count. This is a "
              "standard choice the criterion does not fix."]),
o("fig2b-active-channels-decrease", "reproduced", NB1,
  "The daily count of channels above 1 Hz falls by 6.5 per year (slope -0.0177 per day, r = -0.39, p = 2.6e-12, 303 "
  "days), from a mean of 44.6 in the first 30 sessions to 25.9 in the last 30."),
o("fig2c-pr-decline", "reproduced", NB1,
  "PR of the active channels falls by 0.0708 per month (p = 1.5e-08, 303 days), inside -0.07 +- 0.007. With every "
  "session as a point, -0.0720.", measured=-0.0708),
o("fig2c-ten-dimensions", "reproduced", NB1,
  "Under reading (a) the daily PR is at most 10 on 84.8% of days (median 7.86). Under (b) the top 10 PCs explain more "
  "than 50% on every day; under (c) more than 80% on 44.6% of days, which alone would not reproduce it."),
o("figs4-bank-slopes", "reproduced", NB1,
  "With the stored values, slopes per day are -5.84e-04 (lateral, bank A), -1.34e-03 (bank B), -1.40e-03 (bank C) and "
  "-1.11e-03 (all), equal to the supplement's values to the printed digits; the lateral bank has the lowest mean SBP "
  "(2.19 against 2.55 and 3.57). Both fit readings give the same slopes, since every day has every channel. Under unit "
  "reading (a) each slope is a quarter of these.",
  measured=[-0.000584, -0.00134, -0.0014, -0.00111],
  deviations=["Medial 1 and Medial 2 are taken as banks B and C, which the paper does not name; the two medial values "
              "match in that order."]),
o("figs5-active-inactive-slopes", "partially_reproduced", NB1,
  "With the stored values and channel-session points, active channels decline at -1.261e-03 per day, inside the "
  "tolerance of -1.29e-3, and inactive channels have the lower mean SBP (2.15 against 3.74). The inactive slope is "
  "-5.36e-04, the size of the supplement's 0.54e-3 with the opposite sign, so outside the tolerance. The negative sign "
  "agrees with Section 4.1, which says all categories decreased. With session means (reading b) the slopes are "
  "-1.162e-03 and -4.50e-04.",
  measured=[-0.001261, -0.000536],
  deviations=["Each session classifies its own channels and is one point in time; on the 9 two-session days both "
              "sessions are points."]),
o("fig2d-population-drift", "partially_reproduced", NB1,
  "The centroids move: the first and last quarters' centroids are 17.04 apart against a mean within-quarter SD of "
  "2.02. Three quarters (2021Q1, 2022Q3, 2023Q2) have a 3-PC SD more than 25% from the median of 1.83, where the rule "
  "allows two; at 50%, two quarters (2021Q1 at 4.27, 2022Q3 at 2.80) stand out, as the paper's two exceptions would. "
  "2020Q2 has one session.",
  deviations=["The PCA is computed from per-session sums of the SBP and its products, which gives the same components "
              "as fitting scikit-learn's PCA to the concatenated, z-scored matrix of all bins.",
              "The 3-PC standard deviation of a quarter is the root mean square of the three PCs' SDs, as the criterion's "
              "movement rule defines it."]),
o("fig2e-trajectories-separable", "reproduced", NB1,
  "Nearest-centroid classification of the 37-bin, 3-PC trajectories by direction gives 0.212 in 2020 (15,951 trials) "
  "and 0.220 in 2023 (16,511 trials), against 1/8 (binomial p below 1e-200), the majority-class rate (0.158 and 0.184) "
  "and permuted labels (0.125 and 0.114). The code's alignment gives 0.232 and 0.221 but drops 92,544 of 116,683 "
  "trials. Accuracy is well above chance but low in absolute terms.",
  deviations=["The first trial of each session, with no previous target in the file, has no direction.",
              "A trial whose 37-bin window runs past its end, or with no movement onset, is dropped (1,067 of 116,683 "
              "under the paper's alignment). The paper says trials were trimmed to 37 bins but not what was done with "
              "shorter ones; this is a standard choice.",
              "The day's PCA is fit to both sessions concatenated on two-session days."]),
o("fig3b-two-channels", "reproduced", NB1,
  "Channel 7, circular median angle 81.1 degrees, circular IQR 18.6 degrees, median strength 0.0245 (sixth of 96; "
  "median over channels 0.0070). Channel 32, circular IQR 146.9 degrees (sixth largest; median 46.9). Mean TCR 3.12 and "
  "36.45 Hz."),
o("fig3cd-tuning-stable", "reproduced", NB1,
  "Below 90 degrees (reading b), 77.1% of all channels and 77.4% of the 53 active ones; below 45 degrees (reading a), "
  "47.9% and 45.3%. The outcome holds under the 90-degree reading only.",
  deviations=["The criterion names two thresholds; the result holds under one of them, so it is reproduced as the "
              "criterion states, and depends on that reading."]),
o("fig3d-weak-channels-low-tcr", "reproduced", NB1,
  "Spearman rho = 0.925 (p = 3e-41) between median tuning strength and median daily TCR over 96 channels; the 24 "
  "weakest channels have a median TCR of 0.40 Hz against 0.87 Hz (Mann-Whitney p = 5.3e-11)."),
o("fig3e-array-tuning", "not_reproduced", NB1,
  "With the files' array labels, medial channels' circular medians cluster near -130 degrees (extension of both); 2 of "
  "64 are in the flexion sector. Most lateral channels are tuned to flexion (about 12 to 88 degrees); 2 of 32 are in the "
  "extension sector. With the array names swapped the pattern is close to the paper's (81.2% of file-lateral channels "
  "in the flexion sector, 92.2% of file-medial channels in the extension sector), though more of the flexion channels "
  "lie near IDX flexion (17) than near MRS flexion (11). The files' labels agree with Figure S1 (channel 47 medial, row 5, "
  "column 5) and with Figure S4 (lowest SBP on the lateral bank), so the disagreement is between the files and this "
  "sentence of the paper, or a sign convention of the paper's tuning angles.",
  deviations=["The swapped-label reading is shown as a variant and does not decide the outcome."]),
o("fig4a-sameday-stable", "reproduced", NB2,
  "RR same-day R2 slope +0.0020 per year (p = 0.58, 312 sessions), LSTM +0.0064 per year (p = 0.56, 20 sessions); "
  "Pearson r between the two over the 20 sessions 0.582 (p = 0.007). RR without input normalisation, as the code fits "
  "it, gives +0.0019 per year (p = 0.58). Median R2, RR 0.296, LSTM 0.591.",
  deviations=[LSTM_SUB,
              "The LSTM's training noise is 0.1 white per bin and 0.2 bias per sequence and channel, as the Methods and "
              "the criterion state; the code's train_model passes the two to add_training_noise in the other order, so "
              "the code adds a bias of 0.1 and white noise of 0.2.",
              "Training windows are drawn without replacement per epoch, as the code's shuffled DataLoader does; history "
              "before the start of a segment is zero in the normalised data."]),
o("fig4a-lstm-beats-rr", "reproduced", NB2,
  "LSTM above RR on 20 of 20 sessions, by 0.223 to 0.385 (median 0.301), so no extra seeds were needed. RR's highest "
  "same-day R2 over all 312 sessions, 0.467, is below the lowest LSTM R2 seen, 0.514; the other 292 sessions were not "
  "tested with the LSTM.",
  deviations=[LSTM_SUB]),
o("fig4bc-dof-accuracy", "reproduced", NB2,
  "Median R2 for RR (312 sessions) IDX and MRS position 0.316 and 0.362, velocity 0.220 and 0.286; LSTM (20 sessions) "
  "0.645 and 0.663, velocity 0.480 and 0.576. Per session, position above velocity for both fingers in 62.8% (RR) and "
  "75.0% (LSTM), MRS above IDX for both in 50.6% and 60.0%.",
  deviations=[LSTM_SUB]),
o("fig4d-cross-day-decay", "reproduced", NB2,
  "Under absolute offset and test-day normalisation, the LSTM is above RR at all 101 offsets; LSTM 0.583, 0.376, 0.186 "
  "and RR 0.294, 0.088, -0.005 at day 0, 1 to 5 days and 90 to 100 days; normalised curves correlate at r = 0.903. "
  "Under the other three pairs the LSTM is also better at every offset, but r is 0.887, 0.526 and 0.391, and with the "
  "signed offset and test-day normalisation the sharp-then-stable part fails. With the training day's normalisation "
  "RR's mean R2 is -13.4 to -17.9 past day 0.",
  deviations=[LSTM_SUB,
              "Both decoders' cross-day curves use the 20 LSTM sessions' decoders, each tested on every session within "
              "100 days (1,088 evaluations per decoder and normalisation), scored on every 5th test bin for time.",
              "The criterion names two readings each of offset and normalisation; the outcome holds under one pair of the four."]),
o("suppc1-shuffle-baseline", "partially_reproduced", NB2,
  "All shuffles give negative R2. Under reading (a), raw bins permuted, the LSTM median is -0.154 (20 sessions), inside "
  "-0.156 +- 0.0156, and RR's -0.223 (312 sessions), outside -0.166 +- 0.0166 (per-session range -0.363 to -0.149). "
  "Reading (b) gives -0.410 (RR) and -0.596 (LSTM); whole trials give -0.409 and -0.533.",
  measured=[-0.223, -0.154],
  deviations=[LSTM_SUB, "Judged on the median over sessions, as the criterion says, since the paper's one session is not named."]),
o("fig5a-multiday-short-term", "reproduced", NB3,
  "Over 12 day-0 sessions, five training sessions against one raise mean R2 over relative days 1 to 5 from -0.502 to "
  "-0.251, shrink the drop from day 0 from 1.089 to 0.791, and lower day-0 R2 from 0.587 to 0.540 (lower on 11 of 12). "
  "R2 after day 0 is negative because input normalisation is held at the training parameters. 283 day-0 sessions are "
  "eligible, as the legend reports, when the last session, with nothing after it, is left out.",
  deviations=["12 of the 283 day-0 sessions, evenly spaced and chosen before any result, and only 1 and 5 training "
              "sessions (the two the criterion compares), for time; the paper trains 1415 LSTMs, about 19 hours here.",
              "Scored on every 5th test bin; the code's variant of the multi-day trainer was not run.",
              "The last eligible session is left out as it has no later session to test on; this gives the legend's 283."]),
o("fig5a-long-term-decay", "not_reproduced", NB3,
  "The double-exponential fits to the mean R2 per relative day are degenerate (one session, a component of near-zero "
  "amplitude with rate 0.18 and one with rate -0.0029; five sessions, two growing components of opposing amplitude). "
  "The initial rate is not more negative for one session and the predicted drop to day 5 is not larger (-0.009 against "
  "0.014). The long-term rates' 95% intervals overlap but are very wide (five sessions, -1.48 to 1.50 per day). Residual "
  "RMS 0.40 and 0.65 on a curve that reaches -3.98. With 12 day-0 sessions the curve is likely too noisy for this fit; "
  "the raw comparison of fig5a-multiday-short-term does show the smaller early drop with five sessions.",
  deviations=["Fit to the 12 day-0 sessions of fig5a-multiday-short-term in place of 283, for time; this may be why the "
              "fit fails."]),
o("fig5b-finetune", "blocked", NB3,
  "Estimated from the 20 seed days, 32 to 85 later sessions each within 200 days (1146 in all), the four durations' "
  "iterations and the two normalisation readings, 2,446,600 training iterations, about 16.5 hours at the measured "
  "0.097 s per iteration with four fits at once, beyond the 60-minute notebook limit and the run. Not run.",
  blocked_by="too_large"),
]
rec = {
 "schema_version": 3, "id": "temmar-2025-01",
 "datasets": [{"archive": "dandi", "id": "001201", "version": "0.261026.1912",
               "doi": "10.48324/dandi.001201/0.261026.1912", "relation": "primary"}],
 "paper": "doi:10.52202/085713-4642", "date": "2026-11-12", "entry": "temmar-2025",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-14"},
                "runner": {"platform": "GitHub Actions",
                           "url": "https://github.com/catalystneuro/encore/actions/runs/43201995281"}},
 "outcomes": outcomes,
 "findings": [
  {"kind": "metadata_error", "statement": "ThresholdCrossings is stored with unit volts and conversion 1.0, but it holds "
   "integer counts of threshold crossings per 20 ms bin."},
  {"kind": "data_missing", "statement": "The files and the dandiset metadata give the subject's date of birth but not the "
   "implant date, so the paper's days after implant (349 to 1591) cannot be recovered from the dataset."},
  {"kind": "format_error", "statement": "In 81 of 312 files the electrodes table has no imp column at all, in place of "
   "empty values; Appendix A.2 says such sessions have no impedance within three weeks, but a column that comes and goes "
   "breaks code that reads every file the same way."},
  {"kind": "metadata_insufficient", "statement": "The velocity series are described only as velocity of flexion. In the "
   "data, velocity at bin t is position at t+1 minus position at t (a forward difference), except at the bin before a "
   "pause, so velocity leads position by one bin; the direction of the difference is not stated in the files or the paper."},
  {"kind": "other", "statement": "29 sessions have 72 pauses of 1.05 to 472.9 s between runs of 20 ms bins, which the "
   "paper's '(mostly) contiguous' allows but the files do not mark; 998 trials have a length (stop minus start) of at most "
   "the 750 ms hold."},
  {"kind": "paper_inconsistency", "statement": "The supplement gives the inactive channels' SBP slope as +0.54e-3 while "
   "Section 4.1 says all categories decreased; the data give -0.536e-3, the same size with the main text's sign."},
  {"kind": "other", "statement": "With the files' array labels, medial-array channels are tuned to extension of both "
   "fingers and lateral-array channels to flexion, the reverse of Section 4.2. The labels agree with Figure S1 and with "
   "the lateral bank's lower SBP, so the files and the paper's tuning description disagree on which array is which, or on "
   "the sign of the tuning angles."},
  {"kind": "code_mismatch", "statement": "In bci_decoding/nn_utils.py, train_model calls add_training_noise(inputs, "
   "noise_neural_std, noise_bias_std), whose parameters are (x, bias_neural_std, noise_neural_std), so the code adds a "
   "bias of SD 0.1 and white noise of SD 0.2, the reverse of Appendix C.1 (noise 0.1, bias 0.2)."},
 ],
}
open("attempts/temmar-2025-01.yaml", "w").write(
    yaml.safe_dump(rec, sort_keys=False, width=110, allow_unicode=True))
EOF
cd  && python $TMPDIR/rec/make.py && python tools/entry.py check entries/temmar-2025 | tail -3; grep -n '—\|rather\|\*\*' attempts/temmar-2025-01.yaml entries/temmar-2025/README.md entries/temmar-2025/link.py | head; date -u
```

```
error: attempts/temmar-2025-01.yaml: finding 5 (other): say what it is about, `about: data` or `about: paper`
error: attempts/temmar-2025-01.yaml: finding 7 (other): say what it is about, `about: data` or `about: paper`
2 error(s)
entries/temmar-2025/link.py:156:    return float(ev.sum() ** 2 / (ev ** 2).sum()), ev
entries/temmar-2025/link.py:183:        coef = (zc.T @ yc) / (zc ** 2).sum(0)[:, None]
Thu Nov 12 13:21:55 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude-1001/rec/make.py'; s=open(p).read()
s=s.replace('''  {"kind": "other", "statement": "29 sessions''','''  {"kind": "other", "about": "data", "statement": "29 sessions''')
s=s.replace('''  {"kind": "other", "statement": "With the files' array labels''','''  {"kind": "other", "about": "paper", "statement": "With the files' array labels''')
open(p,'w').write(s)
EOF
python $TMPDIR/rec/make.py && python tools/entry.py check entries/temmar-2025 | tail -3; head -30 attempts/temmar-2025-01.yaml
```

```
error: attempts/temmar-2025-01.yaml: findings/4: Additional properties are not allowed ('about' was unexpected)
error: attempts/temmar-2025-01.yaml: findings/6: Additional properties are not allowed ('about' was unexpected)
2 error(s)
schema_version: 3
id: temmar-2025-01
datasets:
- archive: dandi
  id: '001201'
  version: 0.261026.1912
  doi: 10.48324/dandi.001201/0.261026.1912
  relation: primary
paper: doi:10.52202/085713-4642
date: '2026-11-12'
entry: temmar-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "about" tools/entry.py | head; grep -n '"about"' -B3 -A12 schemas/attempt.schema.json | head -50
```

```
86:    """The identifier of the one dataset a claims file or attempt record is about, in its archive: None for a
325:        # A finding is about the data (its dataset's page) or the paper (the paper's page). Its kind says which,
326:        # except for these two kinds, which must say; and in an attempt on several datasets a finding about the data
327:        # names the datasets it is about (docs/protocol.md, the attempt record).
332:            if f.get("kind") in ("other", "selection_undocumented") and not f.get("about"):
333:                report.error(where, f"finding {n} ({f.get('kind')}): say what it is about, `about: data` or `about: paper`")
334:            about = f.get("about") or ("paper" if f.get("kind") in ("methods_unavailable", "code_mismatch",
336:            if about == "data" and len(used) > 1 and not f.get("datasets"):
337:                report.error(where, f"finding {n}: the attempt used {len(used)} datasets; name the ones it is about "
```

**Agent calls Bash**

```bash
sed -n 17,20p schemas/attempt.schema.json; sed -n 455,500p schemas/attempt.schema.json; grep -rln "about: data" attempts | head -3
```

```
"schema_version": {
      "const": 3
    },
    "id": {
    "findings": {
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
[... 31 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.52202-085713-4642.supp-Supplementary_Material.pdf",
 "pages": "2"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='/tmp/claude-1001/rec/make.py'; s=open(p).read()
s=s.replace('''  {"kind": "other", "about": "data", "statement": "29 sessions''','''  {"kind": "metadata_insufficient", "statement": "29 sessions''')
old_start = s.index('''  {"kind": "other", "about": "paper", "statement": "With the files' array labels''')
old_end = s.index('''  {"kind": "code_mismatch"''')
s = s[:old_start] + '''  {"kind": "paper_inconsistency", "statement": "On these data the paper's statements about the two arrays cannot "
   "both hold. With the files' array labels, which agree with Figure S1's example (channel 47 medial, row 5, column 5), "
   "the lateral bank has the lowest SBP and the shallowest slope, as Appendix C.2 and Figure S4 say, but medial channels "
   "are tuned to extension of both fingers and lateral channels to flexion, the reverse of Section 4.2. With the labels "
   "swapped the tuning would match and the SBP result would not. Either the tuning description names the arrays the "
   "other way round, or its angles use another sign."},
''' + s[old_end:]
open(p,'w').write(s)
EOF
python $TMPDIR/rec/make.py && python tools/entry.py check entries/temmar-2025 | tail -3; date -u
```

```
0 error(s)
Thu Nov 12 13:22:37 UTC 2026
```

**Agent calls Bash**

```bash
grep -n -i '—\|\brather\b' entries/temmar-2025/*.ipynb entries/temmar-2025/*.md entries/temmar-2025/link.py attempts/temmar-2025-01.yaml | head; grep -o '\*\*[^*]*\*\*' entries/temmar-2025/*.ipynb | grep -v "Result:" | head; python3 -c "
import yaml
c=[x['id'] for x in yaml.safe_load(open('claims/temmar-2025.yaml'))['claims']]
a=[x['claim'] for x in yaml.safe_load(open('attempts/temmar-2025-01.yaml'))['outcomes']]
print(len(c),len(a),set(c)^set(a))
import collections; print(collections.Counter(x['outcome'] for x in yaml.safe_load(open('attempts/temmar-2025-01.yaml'))['outcomes']))"; ls executed/temmar-2025/handover
```

```
24 24 set()
Counter({'reproduced': 16, 'partially_reproduced': 5, 'not_reproduced': 2, 'blocked': 1})
decoding.ipynb
link.py
multiday.ipynb
signals.ipynb
temmar-2025.yaml
```

**Agent calls Bash**

```bash
sed -i 's/  runtime_minutes: 8$/  runtime_minutes: 10/; s/  runtime_minutes: 31$/  runtime_minutes: 33/' entries/temmar-2025/entry.yaml && grep runtime entries/temmar-2025/entry.yaml && python tools/entry.py check entries/temmar-2025 | tail -1 && python tools/entry.py handover entries/temmar-2025 | tail -1; git status --short | head; cat .gitignore | head
```

```
runtime_minutes: 10
  runtime_minutes: 33
  runtime_minutes: 27
0 error(s)
wrote executed/temmar-2025/handover
 M tools/build_reuse_targets.py
 M tools/build_site.py
 M tools/entry.py
 M tools/journals.py
 M tools/notify.py
 M tools/papers_manifest.py
 M tools/runner/chain.sh
 M tools/runner/describe.py
 M tools/site_assets/app.css
 M tools/site_assets/list.js
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
.DS_Store
[... 4 more lines not kept]
```

**Agent**

I've done steps 1 to 6 of the Author section. `entry.py all` passed on all three notebooks (10, 33 and 27 min), `check` reports 0 errors, and the handover is built in `executed/temmar-2025/handover/`. The entry is in `entries/temmar-2025/` and the record in `attempts/temmar-2025-01.yaml`. Of the 24 claims, 16 are reproduced, 5 partially reproduced, 2 not reproduced and 1 blocked.

### 1. Outcome per claim

| Claim | Outcome | Measured |
|---|---|---|
| dataset-sessions | reproduced | 312 sessions, 303 days, 1242-day span, 9 two-session days, 375 trials each |
| dataset-contents | partially reproduced | 81 of 312 files have no `imp` column |
| figs2-throughput-improves | reproduced | positive slope under all 3 readings |
| fig2a-sbp-decline | reproduced | −0.0338 µV/month |
| fig2a-irregular-shifts | partially reproduced | the shift rule flags almost every day; LSTM R2 in the window is just above its 90th percentile |
| fig2b-active-channels-decrease | reproduced | −6.5 channels/year |
| fig2c-pr-decline | reproduced | −0.0708 PR/month |
| fig2c-ten-dimensions | reproduced | PR at most 10 on 84.8% of days |
| figs4-bank-slopes | reproduced | all four slopes equal the paper's to the printed digits |
| figs5-active-inactive-slopes | partially reproduced | inactive slope −0.54e-3, where the paper prints +0.54e-3 |
| fig2d-population-drift | partially reproduced | 3 quarters with an outlying spread, where the rule allows 2 |
| fig2e-trajectories-separable | reproduced | 0.21 and 0.22 accuracy against 1/8 chance |
| fig3b-two-channels | reproduced | |
| fig3cd-tuning-stable | reproduced | holds at the 90° reading only |
| fig3d-weak-channels-low-tcr | reproduced | |
| fig3e-array-tuning | not reproduced | the pattern matches the paper only with the array names swapped |
| fig4a-sameday-stable | reproduced | LSTM tested on 20 sessions |
| fig4a-lstm-beats-rr | reproduced | 20 of 20 sessions tested |
| fig4bc-dof-accuracy | reproduced | |
| fig4d-cross-day-decay | reproduced | under one of the four reading pairs only (absolute offset, test-day normalisation) |
| suppc1-shuffle-baseline | partially reproduced | LSTM −0.154 inside the tolerance; RR −0.223 outside it |
| fig5a-multiday-short-term | reproduced | 12 day-0 sessions |
| fig5a-long-term-decay | not reproduced | the double-exponential fits are degenerate, likely because 12 day-0 sessions are too few |
| fig5b-finetune | blocked, `too_large` | estimate 2.45M training iterations, about 16.5 h |

### 2. Dataset

**Version pinned.** 0.261026.1912, the latest published. The paper cites none, and all three published versions list identical asset ids.

**What was found about the data:**
- The stored SBP is already in µV. The code divides it by 0.25 and its analysis multiplies by 0.25, which cancel.
- ThresholdCrossings is labelled "volts" but holds integer counts.
- The files give no implant date, so the paper's days after implant cannot be checked.
- 81 files have no impedance column at all.
- Velocity is a forward difference: velocity at a bin is the next bin's position minus this one's.
- 29 sessions have 72 unmarked pauses of 1 to 473 s.
- 998 trials are no longer than the 750 ms hold.
- **Paper inconsistency:** with the files' array labels, the paper's lower-SBP-on-lateral result (Figure S4) holds but its tuning-by-array sentence (Section 4.2) is reversed.
- **Code mismatch:** the code swaps the LSTM's noise arguments (0.1 bias and 0.2 white, where the paper says the reverse). I followed the paper.

**Subsets, recorded as deviations.** For time, the LSTM runs on every 16th session (20 of 312) and multi-day training on 12 of 283 day-0 sessions, with only 1 and 5 training sessions. Cross-day scores use every 5th test bin.

**Assumptions, questions for the paper's authors, questions to a reader.** None. Every open choice was one of the readings the criteria name, so `questions/temmar-2025.yaml` was not created.

### 3. Protocol problems

1. **`about` field on findings:** `tools/entry.py check` requires `about: data|paper` on `other` findings, but `schemas/attempt.schema.json` rejects that field. I re-filed those two findings as `metadata_insufficient` and `paper_inconsistency`. (`tools/entry.py` is modified in the working tree, which may be why.)
2. **Writing conclusions after the run:** the protocol says to develop on a subset and run the whole once. But the conclusion cells must quote the full run's numbers, and editing them changes the entry hash, so every notebook has to run twice. I ran each notebook in full once, wrote the conclusions, then ran `all`. The claim outputs were identical between the two runs.
3. **Subsets versus blocking:** "Develop on a subset" says to block a claim as `too_large` when the estimate is over the limit, yet the protocol also lists "one session of four" as an acceptable deviation. I tested the LSTM claims on pre-chosen subsets and recorded deviations. I blocked only fig5b, whose estimate is far over even the run's time.
4. **Editing `entry.yaml` after the run:** I changed `runtime_minutes` after `all`, which invalidates the run's reuse stamp. The executed copies are unaffected.
5. **Supplement figures:** the PDF renderer (pdftoppm) is missing, so I could not open Figure S1 to check where channel 7 sits. The array-label finding rests on the files and the text only.

### 4. Runtime and failures

The run took about 2 h 50 min, ending at about 13:25 UTC, well before the 14:52 cutoff. Two development runs failed and were fixed (the missing `imp` column, and a statistic over an empty list). Nothing failed in the final run. Nothing was committed.

## End of run

74 turns, 163 minutes, $8.83 at API prices, result: success.
