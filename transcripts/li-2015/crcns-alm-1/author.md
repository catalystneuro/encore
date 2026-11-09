# crcns-alm-1 · author · run 42414841408

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bmtyxg39j.txt

Preview (first 2KB):
Sat Nov  7 21:20:48 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bmtyxg39j.txt"
}
```

```
1	Sat Nov  7 21:20:48 UTC 2026
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
[... 633 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; echo ----; wc -l docs/design.md; sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md
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
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/crcns-alm-1/ paper/ entries/001453-fouke-2025/ claims/001453/; cat claims/crcns-alm-1/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml"
}
```

```
1	# Claims for Li, Chen, Guo, Gerfen & Svoboda (2015), Nature 519, 51-56, "A motor cortex circuit for
2	# motor planning and movement", doi:10.1038/nature14178, on CRCNS data set alm-1
3	# (doi:10.6080/K0RF5RZT).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the version of record, as text extracted from the PDF supplied under paper/ (main
8	# text, Methods, legends of Figures 1 to 5 and Extended Data Figures 1 to 7). The paper has no
9	# separate Supplementary Information. The extraction prints "=" as "5", "<" as ",", ">" as ".",
10	# "±" as "6" and a minus sign as "2"; quotes keep these glyphs as printed. PDF pages 2, 3 and 5
11	# were opened to read Fig. 1d, 2c, 2d, 3e, 3f, 3i and 5b, which the text garbles.
12	#
13	# Code. The paper links no analysis code. The data set's description says it holds MATLAB scripts;
14	# they are files of the data set and were not read. Every method below is from the paper's text.
15	#
16	# Data the paper used. 52 mice (age > P60). Behaviour, whisker-based object location
17	# discrimination, head-fixed (n = 42 mice in the Results): pole at an anterior (lick left) or
18	# posterior (lick right) position; sample epoch 1.3 s from pole movement onset to 0.1 s after pole
19	# retraction onset; delay epoch 1.3 s; auditory go cue (3.4 kHz, 0.1 s); response by licking one of
20	# two lickports; licks before the cue are "lick early" trials. Photoinhibition of ALM (Fig. 1), 5
[... 733 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/alm-1.data-description.txt; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=alm-1/" | python -c "import sys,re; d=sys.stdin.read(); [print(k,s) for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',d)]"
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bdn38s2rs.txt"
}
```

```
1	Data descriptor: of the data set CRCNS:alm-1, not a paper. It describes the data set's files and how they were recorded.
2	Version: as published by CRCNS.org, https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/docs/crcns_alm-1_data_description.pdf
3	Source: the CRCNS data set's documentation (alm-1/live/docs/crcns_alm-1_data_description.pdf; alm-1/live/docs/Svoboda_lab_data_format_general.pdf; alm-1/live/README.txt)
4	Stored: 2026-11-05
5	Extracted: PyMuPDF, dehyphenated, NFKC
6	------------------------------------------------------------------------
7	##### alm-1/live/docs/crcns_alm-1_data_description.pdf
8	1 
9	 
10	CRCNS.org alm-1 data description 
11	Version 0.91 (May 8, 2017) 
12	 
13	Summary 
14	These experiments probe neural dynamics in the anterior motor cortex (ALM) and its 
15	relationship to voluntary movement.  The data represent extracellular recordings from ALM 
16	neurons of adult mice performing a tactile decision behavior.  The data is from 19 animals and 
17	includes 99 recording sessions.  Results from the experiments are described in: 
18	 
19	A motor cortex circuit for motor planning and movement 
20	Nuo Li, Tsai-Wen Chen, Zengcai V. Guo, Charles R. Gerfen & Karel Svoboda 
[... 781 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:8]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('=====')
print(len(nb['cells']))"
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
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml; ls questions | head; ls tools; sed -n 1,80p docs/design.md | head -5
```

```
cat: attempts/001453-fouke-2025-01.yaml: No such file or directory
ls: cannot access 'questions': No such file or directory
ls: cannot access 'tools': No such file or directory
sed: can't read docs/design.md: No such file or directory
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -250; ls questions | head; ls tools schemas
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
[... 275 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 250,400p attempts/001453-fouke-2025-01.yaml; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s)[:6000])"
```

```
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
    where the Methods state tracking at more than 150 Hz. Their timestamp intervals are regular
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/10.1038-nature14178.txt; grep -n -i "Methods\|Electrophysiology data analyses\|Behavioural data analyses" paper/10.1038-nature14178.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 866,1110p paper/10.1038-nature14178.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/matlab_scripts/analyses_scripts; curl -s $B/analysis_compile_all_data.m
```

```
clear all
close all


file_list = dir('..\datafiles\data_structure_*.mat');



%% establish variables to compute and save
N_trials_all = [];

spike_times_all = {};       %[yes no yes_error no_error]

PSTH_yes_cue_aligned  = [];
PSTH_no_cue_aligned  = [];
PSTH_yes_error_cue_aligned  = [];
PSTH_no_error_cue_aligned  = [];

spk_count_yes_all  = [];    %[sample delay resposne whole_trial baseline]
spk_count_no_all  = [];
[... 475 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "import h5py,fsspec,scipy,numpy;print(h5py.__version__,fsspec.__version__)"; which uv
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py,fsspec,scipy,numpy;print(h5py.__version__,fsspec.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q h5py fsspec aiohttp requests scipy numpy pandas matplotlib statsmodels ipykernel 2>&1 | tail -2; python -c "import h5py; print(h5py.__version__)"; sed -n 1,80p tools/entry.py | head -60
```

```
3.16.0
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
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > ls_nwb.py <<'EOF'
import fsspec, h5py, time
t=time.time()
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/datafiles/nwb_files/data_structure_ANM210861_20130701.nwb"
f=h5py.File(fsspec.open(url,block_size=2**20).open(),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        v=''
        if obj.size<6 or obj.dtype.kind in 'SO' and obj.size<20:
            try: v=obj[()]
            except Exception as e: v=e
        print(name,obj.shape,obj.dtype,obj.compression,dict(obj.attrs) if len(obj.attrs)<5 else list(obj.attrs),v)
    else:
        print(name+'/',dict(obj.attrs) if len(obj.attrs)<6 else list(obj.attrs))
f.visititems(show)
print(time.time()-t)
EOF
python ls_nwb.py 2>&1 | grep -v "unit_[0-9]*/" | head -150; python ls_nwb.py 2>&1 | grep "unit_0*1[/ ]" | head
```

```
acquisition/ {}
acquisition/images/ {}
acquisition/timeseries/ {}
acquisition/timeseries/extracellular_traces/ {'description': np.bytes_(b'File containing the raw voltage data for this session'), 'neurodata_type': np.bytes_(b'Custom'), 'source': np.bytes_(b' ')}
acquisition/timeseries/extracellular_traces/ephys_raw_data () |S40 None {'neurodata_type': np.bytes_(b'Custom')} b'voltage_filenamee_ANM210861_20130701.mat'
acquisition/timeseries/lick_trace/ ['ancestry', 'comments', 'description', 'help', 'neurodata_type', 'source']
acquisition/timeseries/lick_trace/data (21100000,) float32 gzip {'conversion': np.float64(1.0), 'keyName': np.bytes_(b'EphusVars'), 'resolution': np.float64(nan), 'unit': np.bytes_(b'unknown')} 
acquisition/timeseries/lick_trace/num_samples () int32 None {} 21100000
acquisition/timeseries/lick_trace/timestamps (21100000,) float64 gzip {'interval': np.int64(1), 'unit': np.bytes_(b'Seconds')} 
analysis/ {}
analysis/description () |S396 None {'neurodata_type': np.bytes_(b'Custom')} b'Trial_type_string has six values, with three response possibilities and two correct responses.  The format is {response type}{correct response}, with response type taking the value Hit, Err, or NoLick, indicating that the animal got the trial right, wrong, or did nothing, respectively.  Corret response is either L or R, indicating that the animal should have licked left or right, respectively.'
analysis/trial_start_times (423,) float32 gzip {'neurodata_type': np.bytes_(b'Custom')} 
analysis/trial_type_mat (8, 423) uint8 gzip {'neurodata_type': np.bytes_(b'Custom')} 
analysis/trial_type_string (8,) |S10 gzip {'neurodata_type': np.bytes_(b'Custom')} [b'HitR' b'HitL' b'ErrR' b'ErrL' b'NoLickR' b'NoLickL' b'LickEarly'
 b'StimTrials']
epochs/ {'tags': array([b'ErrL', b'ErrR', b'Good trial', b'HitL', b'HitR', b'LickEarly',
       b'NoLickL', b'NoLickR', b'Non-performing', b'StimTrials',
       b'discard', b'non-stimulation trial'], dtype='|S21')}
epochs/trial_001/ {'links': 
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && time python ls_nwb.py > nwb_list.txt 2>&1; grep -v "^epochs/trial\|unit_[0-9]*/" nwb_list.txt | cut -c1-400; grep -c "^processing/extracellular_units/UnitTimes/unit_[0-9]*/$" nwb_list.txt; grep "UnitTimes/unit_01/" nwb_list.txt
```

```
<persisted-output>
Output too large (56.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/b3zogz761.txt

Preview (first 2KB):
real	0m45.047s
user	0m3.668s
sys	0m1.009s
acquisition/ {}
acquisition/images/ {}
acquisition/timeseries/ {}
acquisition/timeseries/extracellular_traces/ {'description': np.bytes_(b'File containing the raw voltage data for this session'), 'neurodata_type': np.bytes_(b'Custom'), 'source': np.bytes_(b' ')}
acquisition/timeseries/extracellular_traces/ephys_raw_data () |S40 None {'neurodata_type': np.bytes_(b'Custom')} b'voltage_filenamee_ANM210861_20130701.mat'
acquisition/timeseries/lick_trace/ ['ancestry', 'comments', 'description', 'help', 'neurodata_type', 'source']
acquisition/timeseries/lick_trace/data (21100000,) float32 gzip {'conversion': np.float64(1.0), 'keyName': np.bytes_(b'EphusVars'), 'resolution': np.float64(nan), 'unit': np.bytes_(b'unknown')} 
acquisition/timeseries/lick_trace/num_samples () int32 None {} 21100000
acquisition/timeseries/lick_trace/timestamps (21100000,) float64 gzip {'interval': np.int64(1), 'unit': np.bytes_(b'Seconds')} 
analysis/ {}
analysis/description () |S396 None {'neurodata_type': np.bytes_(b'Custom')} b'Trial_type_string has six values, with three response possibilities and two correct responses.  The format is {response type}{correct response}, with response type taking the value Hit, Err, or NoLick, indicating that the animal got the trial right, wrong, or did nothing, respectively.  Corret response is either L or R, 
analysis/trial_start_times (423,) float32 gzip {'neurodata_type': np.bytes_(b'Custom')} 
analysis/trial_type_mat (8, 423) uint8 gzip {'neurodata_type': np.bytes_(b'Custom')} 
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v "^epochs/\|unit_[0-9]*/\|^ b'" nwb_list.txt | cut -c1-600; grep -c "UnitTimes/unit_[0-9]*/$" nwb_list.txt; grep "UnitTimes/unit_01/" nwb_list.txt
```

```
acquisition/ {}
acquisition/images/ {}
acquisition/timeseries/ {}
acquisition/timeseries/extracellular_traces/ {'description': np.bytes_(b'File containing the raw voltage data for this session'), 'neurodata_type': np.bytes_(b'Custom'), 'source': np.bytes_(b' ')}
acquisition/timeseries/extracellular_traces/ephys_raw_data () |S40 None {'neurodata_type': np.bytes_(b'Custom')} b'voltage_filenamee_ANM210861_20130701.mat'
acquisition/timeseries/lick_trace/ ['ancestry', 'comments', 'description', 'help', 'neurodata_type', 'source']
acquisition/timeseries/lick_trace/data (21100000,) float32 gzip {'conversion': np.float64(1.0), 'keyName': np.bytes_(b'EphusVars'), 'resolution': np.float64(nan), 'unit': np.bytes_(b'unknown')} 
acquisition/timeseries/lick_trace/num_samples () int32 None {} 21100000
acquisition/timeseries/lick_trace/timestamps (21100000,) float64 gzip {'interval': np.int64(1), 'unit': np.bytes_(b'Seconds')} 
analysis/ {}
analysis/description () |S396 None {'neurodata_type': np.bytes_(b'Custom')} b'Trial_type_string has six values, with three response possibilities and two correct responses.  The format is {response type}{correct response}, with response type taking the value Hit, Err, or NoLick, indicating that the animal got the trial right, wrong, or did nothing, respectively.  Corret response is either L or R, indicating that the animal should have licked left or right, respectively.'
analysis/trial_start_times (423,) float32 gzip {'neurodata_type': np.bytes_(b'Custom')} 
analysis/trial_type_mat (8, 423) uint8 gzip {'neurodata_type': np.bytes_(b'Custom')} 
analysis/trial_type_string (8,) |S10 gzip {'neurodata_type': np.bytes_(b'Custom')} [b'HitR' b'HitL' b'ErrR' b'ErrL' b'NoLickR' b'NoLickL' b'LickEarly'
       b'NoLickL', b'NoLickR', b'Non-performing', b'StimTrials',
       b'discard', b'non-stimulation trial'], dtype='|S21')}
file_create_date (1,) object gzip {} [b'2017-04-24T11:32:54.281831']
general/ {}
general/data_collection () |S2035 None {} b"The extr
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > tartest.py <<'EOF'
import fsspec, tarfile, time
t=time.time()
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/datafiles/data_structure_files/data_structure_ANM221977.tar.gz"
with fsspec.open(url,block_size=2**23).open() as fh:
    tf=tarfile.open(fileobj=fh,mode='r|gz')
    for m in tf:
        print(m.name,m.size, time.time()-t, flush=True)
        if m.isfile():
            b=tf.extractfile(m).read(); print(b[:130])
print(time.time()-t)
EOF
python tartest.py
```

```
data_structure_ANM221977_20140115.mat 157127989 0.5448818206787109
b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Mon Jan 19 17:03:16 2015                                                \x00\x01IM\x0f\x00'
data_structure_ANM221977_20140116.mat 190500393 5.652629137039185
b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Mon Jan 19 17:03:46 2015                                                \x00\x01IM\x0f\x00'
data_structure_ANM221977_20140118.mat 90502868 11.336373090744019
b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Mon Jan 19 17:04:15 2015                                                \x00\x01IM\x0f\x00'
13.842114448547363
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > mattest.py <<'EOF'
import fsspec, tarfile, time, io, resource
import scipy.io as sio, numpy as np
t=time.time()
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/datafiles/data_structure_files/data_structure_ANM221977.tar.gz"
with fsspec.open(url,block_size=2**23).open() as fh:
    tf=tarfile.open(fileobj=fh,mode='r|gz')
    for m in tf:
        b=tf.extractfile(m).read()
        print('read',time.time()-t)
        d=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
        print('loaded',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
        o=d['obj']
        for k in o._fieldnames:
            v=getattr(o,k); print(k,type(v), getattr(v,'shape',None), v if np.size(v)<12 else '')
        print('tph',o.trialPropertiesHash.keyNames, o.trialPropertiesHash.descr)
        for k,v in zip(o.trialPropertiesHash.keyNames,o.trialPropertiesHash.value): print(k,v.shape,np.unique(v[~np.isnan(v)])[:10] if k=='PhotostimulationType' or k=='GoodTrials' else v[:5])
        print(o.trialTypeStr)
        ts=o.timeSeriesArrayHash
        print(ts._fieldnames, ts.keyNames, ts.descr)
        v=ts.value
        print(v._fieldnames, v.idStr, v.idStrDetailed, v.timeUnit, v.time.shape, v.valueMatrix.shape, v.time[:5], v.trial[:5])
        es=o.eventSeriesHash
        print(es._fieldnames, es.keyNames[:5], es.descr[:3])
        u=es.value[0]; print(u._fieldnames)
        for k in u._fieldnames: x=getattr(u,k); print(k, getattr(x,'shape',None), x if np.size(x)<5 else x[:3])
        print('meta' , [k for k in d.keys()])
        print('descrHash', o.descrHash.keyNames, str(o.descrHash.value)[:500])
        print(o.timeUnitIds,o.timeUnitNames,o.trialTimeUnit)
        print([ (i,list(np.atleast_1d(e.cellType))) for i,e in enumerate(es.value)])
        break
EOF
python mattest.py
```

```
read 4.766940355300903
loaded 6.1994898319244385 0.93864
timeUnitIds <class 'numpy.ndarray'> (5,) [1 2 3 4 5]
timeUnitNames <class 'numpy.ndarray'> (5,) ['millisecond' 'second' 'minute' 'hour' 'day']
descrHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None <scipy.io.matlab._mio5_params.mat_struct object at 0x7464d262e2c0>
trialTimeUnit <class 'int'> None 2
trialTypeStr <class 'numpy.ndarray'> (8,) ['HitR' 'HitL' 'ErrR' 'ErrL' 'NoLickR' 'NoLickL' 'LickEarly' 'StimTrials']
trialIds <class 'numpy.ndarray'> (337,) 
trialStartTimes <class 'numpy.ndarray'> (337,) 
trialTypeMat <class 'numpy.ndarray'> (8, 337) 
trialPropertiesHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None <scipy.io.matlab._mio5_params.mat_struct object at 0x7464d2115fd0>
timeSeriesHash <class 'numpy.ndarray'> (0,) []
timeSeriesArrayHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None <scipy.io.matlab._mio5_params.mat_struct object at 0x7464d2207460>
eventSeriesHash <class 'scipy.io.matlab._mio5_params.mat_struct'> None <scipy.io.matlab._mio5_params.mat_struct object at 0x7464d21263f0>
tph ['PoleInTime' 'PoleOutTime' 'CueTime' 'GoodTrials' 'PhotostimulationType'] ['Start of Sample period (in seconds, relative to trial start time)'
 'Start of Delay period (in seconds, relative to trial start time)'
 'Start of Response period (in seconds, relative to trial start time)'
 '0 for trials in which mice are not performing, discard for analyses'
 '"0"--non-stimulation trials; "1"--PT axonal stimulation; "2"--IT axonal stimulation; "NaN"--discard (stimulation configuration for other purposes, should not analyze)']
PoleInTime (337,) [nan nan nan nan nan]
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > meta.py <<'EOF'
import fsspec, tarfile, io, scipy.io as sio, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/datafiles/meta_data_files.tar.gz"
with fsspec.open(url).open() as fh:
    tf=tarfile.open(fileobj=fh,mode='r|gz'); n=0
    for m in tf:
        if not m.isfile(): continue
        d=sio.loadmat(io.BytesIO(tf.extractfile(m).read()),squeeze_me=True,struct_as_record=False)
        md=d['meta_data']
        if n<1:
            def dump(s,p=''):
                for k in s._fieldnames:
                    v=getattr(s,k)
                    if hasattr(v,'_fieldnames'): dump(v,p+k+'.')
                    else: print(p+k,repr(v)[:150])
            dump(md)
        n+=1
        e=md.extracellular
        print(m.name, md.animalID if hasattr(md,'animalID') else '', getattr(md,'animalStrain',''), getattr(md,'animalGeneModification',''), getattr(e,'penetrationN',''), getattr(e,'recordingLocation',''), getattr(md,'photostim','') and getattr(md.photostim,'photostimLocation',''))
print(n)
EOF
python meta.py 2>&1 | head -150
```

```
species 'Mus musculus'
animalStrain 'kj18'
animalGeneModification 'sim1-cre'
animalSource 'GENSAT'
animalGeneCopy 1
animalGeneticBackground 'unidentified'
animalID 'anm00210861'
sex 'm'
dateOfBirth '20130311'
dateOfExperiment '20130701'
timeOfExperiment '105723'
experimenters 'Nuo Li'
citation '**PMID currently not avaliable'
whiskerConfig 'full'
weightBefore array([], dtype=object)
weightAfter array([], dtype=object)
experimentType array(['behavior', 'extracellular', 'photostim'], dtype=object)
referenceAtlas 'Paxinos'
surgicalManipulation 'virus injection'
virus.virusSource 'Janelia core'
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > tr.py <<'EOF'
import fsspec, tarfile, time, io, pickle
import scipy.io as sio, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/datafiles/data_structure_files/data_structure_ANM221977.tar.gz"
with fsspec.open(url,block_size=2**23).open() as fh:
    tf=tarfile.open(fileobj=fh,mode='r|gz')
    m=next(iter(tf))
    d=sio.loadmat(io.BytesIO(tf.extractfile(m).read()),squeeze_me=True,struct_as_record=False)
o=d['obj']; v=o.timeSeriesArrayHash.value
np.savez('/tmp/claude/x.npz' if False else 'sess.npz', time=v.time, trial=v.trial, vm=v.valueMatrix.astype(np.float32))
tp=dict(zip(o.trialPropertiesHash.keyNames,o.trialPropertiesHash.value))
pickle.dump(dict(tp=tp,tm=o.trialTypeMat,ts=o.trialStartTimes,ids=o.trialIds, units=[(u.eventTimes,u.eventTrials,u.cellType,u.channel) for u in o.eventSeriesHash.value]),open('sess.pkl','wb'))
EOF
python tr.py; ls -la
```

```
total 360796
drwx------  3 runner runner       4096 Nov  7 21:20 -home-runner-work--temp
drwx------  3 runner runner       4096 Nov  7 21:20 -home-runner-work-encore-encore
drwx------  6 runner runner       4096 Nov  7 21:25 .
drwxrwxrwt 15 nobody nogroup      4096 Nov  7 21:25 ..
drwxr-xr-x  2 runner runner         40 Nov  7 21:25 bash-edit-diff
drwxr-xr-x  5 runner runner       4096 Nov  7 21:21 dev
-rw-r--r--  1 runner runner        668 Nov  7 21:21 ls_nwb.py
-rw-r--r--  1 runner runner       1791 Nov  7 21:24 mattest.py
-rw-r--r--  1 runner runner       1008 Nov  7 21:24 meta.py
-rw-r--r--  1 runner runner     432366 Nov  7 21:23 nwb_list.txt
-rw-r--r--  1 runner runner  368500740 Nov  7 21:25 sess.npz
-rw-r--r--  1 runner runner     473787 Nov  7 21:25 sess.pkl
-rw-r--r--  1 runner runner        440 Nov  7 21:23 tartest.py
-rw-r--r--  1 runner runner        846 Nov  7 21:25 tr.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > an.py <<'EOF'
import numpy as np, pickle
z=np.load('sess.npz'); t=z['time']; tr=z['trial']; vm=z['vm']
p=pickle.load(open('sess.pkl','rb')); tp=p['tp']
print('dt', np.unique(np.round(np.diff(t[:1000]),7)), t[0], t[-1], len(t))
for c in range(3): print(c, np.percentile(vm[:,c],[0,1,50,99,99.9,100]))
pt=tp['PhotostimulationType']; good=tp['GoodTrials']
print('ptype counts', {k:int(np.sum(pt==k)) for k in [0,1,2]}, 'nan',int(np.isnan(pt).sum()), 'good',good.sum(), len(pt))
print('trial ids', p['ids'][:5], p['ts'][:5], 'unique trials in ts', np.unique(tr)[:5], len(np.unique(tr)))
# tagging trial
for kind in [2,0]:
    idx=np.where((pt==kind))[0][:2]
    for i in idx:
        tid=p['ids'][i]; s=tr==tid
        a=vm[s,1]; lk=vm[s,0]; tt=t[s]-p['ts'][i]
        on=np.where((a[1:]>0.5*a.max())&(a[:-1]<=0.5*a.max()))[0] if a.max()>0.1 else []
        print('kind',kind,'trial',tid,'good',good[i],'dur',tt[0],tt[-1],'aom max',a.max(),'laser max',vm[s,2].max(),'n onsets',len(on), 'first onsets', tt[on[:6]] if len(on) else '', 'pole',tp['PoleInTime'][i],tp['CueTime'][i])
        print('  lick pct', np.percentile(lk,[1,50,99]), 'tm', p['tm'][:,i])
EOF
python an.py
```

```
Exit code 1
dt [0.0001] 57.895312 3545.754614 16750000
0 [-0.69866252  0.16089514  0.19637407  1.6874584   1.82421386  2.12868857]
1 [-9.72627010e-03  2.20755185e-03  8.65826663e-03  1.47864455e-02
  4.00392342e+00  4.01295471e+00]
2 [7.02030957e-05 1.01050874e-03 2.45712721e-03 4.39977925e-03
 4.70998955e+01 4.70999985e+01]
ptype counts {0: 198, 1: 0, 2: 103} nan 36 good 300 337
trial ids [1 2 3 4 5] [ 2.370534 57.895312 65.349282 72.737753 80.268556] unique trials in ts [2 3 4 5 6] 335
kind 2 trial 13 good 1 dur 0.0 4.999899999999997 aom max 4.0123096 laser max 47.1 n onsets 20 first onsets [0.3001 0.3111 0.8001 0.8111 1.3002 1.3112] pole 0.5721729999999923 3.172820999999999
  lick pct [0.16541064 0.17637686 0.20798537] tm [0 0 0 1 0 0 0 1]
kind 2 trial 14 good 1 dur 0.0 4.999899999999997 aom max 4.011342 laser max 47.1 n onsets 20 first onsets [0.3001 0.3111 0.8001 0.8111 1.3002 1.3112] pole 0.5723310000000197 3.173154000000011
  lick pct [0.16831346 0.17895715 0.20476002] tm [0 0 0 1 0 0 0 1]
Traceback (most recent call last):
  File "/tmp/claude-1001/an.py", line 15, in <module>
    on=np.where((a[1:]>0.5*a.max())&(a[:-1]<=0.5*a.max()))[0] if a.max()>0.1 else []
                                                                 ~~~~~^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/_methods.py", line 41, in _amax
    return umr_maximum(a, axis, None, out, keepdims, initial, where)
ValueError: zero-size array to reduction operation maximum which has no identity
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > an2.py <<'EOF'
import numpy as np, pickle
z=np.load('sess.npz'); t=z['time']; tr=z['trial']; vm=z['vm']
p=pickle.load(open('sess.pkl','rb')); tp=p['tp']; tm=p['tm']
ids=p['ids']; ts=p['ts']
hist=[]
for i in range(len(ids)):
    s=tr==ids[i]
    if not s.any() or np.isnan(tp['CueTime'][i]): continue
    lk=vm[s,0]; tt=t[s]-ts[i]; cue=tp['CueTime'][i]
    hi=lk>1.0
    up=np.where(hi[1:]&~hi[:-1])[0]+1
    after=tt[up][tt[up]>cue]
    early=tt[up][(tt[up]<cue)&(tt[up]>tp['PoleInTime'][i])]
    lab=[n for n,k in zip(['HitR','HitL','ErrR','ErrL','NoLickR','NoLickL','LickEarly','Stim'],tm[:,i]) if k]
    if i<60 or 'NoLickR' in lab or 'NoLickL' in lab: print(ids[i],lab, 'first lick after cue %.4f'%((after[0]-cue) if len(after) else np.nan), 'n',len(after),'early',len(early), 'range',lk.min().round(2),lk.max().round(2))
EOF
python an2.py | head -80
```

```
13 ['ErrL', 'Stim'] first lick after cue nan n 0 early 0 range -0.69 0.25
14 ['ErrL', 'Stim'] first lick after cue nan n 0 early 0 range -0.69 0.22
15 ['ErrL', 'Stim'] first lick after cue nan n 0 early 0 range -0.69 0.2
16 ['ErrL', 'Stim'] first lick after cue 0.4191 n 6 early 0 range -0.64 2.13
17 ['HitL', 'Stim'] first lick after cue 0.1392 n 9 early 0 range -0.65 1.91
18 ['HitL', 'Stim'] first lick after cue nan n 0 early 0 range -0.68 1.0
19 ['HitL', 'Stim'] first lick after cue 0.1071 n 1 early 0 range -0.69 1.43
20 ['HitR', 'LickEarly', 'Stim'] first lick after cue 0.1150 n 3 early 4 range -0.68 1.97
21 ['HitR', 'LickEarly', 'Stim'] first lick after cue 0.0930 n 11 early 3 range -0.66 1.97
22 ['HitR', 'LickEarly', 'Stim'] first lick after cue 0.1054 n 11 early 1 range -0.67 1.93
23 ['ErrL', 'Stim'] first lick after cue 0.1145 n 2 early 0 range -0.67 1.93
24 ['HitL', 'Stim'] first lick after cue 0.4286 n 3 early 0 range -0.68 1.15
25 ['HitL', 'Stim'] first lick after cue 0.0973 n 4 early 0 range -0.68 1.45
26 ['HitL', 'Stim'] first lick after cue 0.0987 n 2 early 0 range -0.66 1.25
27 ['NoLickR'] first lick after cue 0.2489 n 1 early 0 range -0.68 1.86
28 ['HitL'] first lick after cue 1.0767 n 3 early 0 range -0.68 1.75
29 ['HitL', 'LickEarly', 'Stim'] first lick after cue 0.5864 n 2 early 3 range -0.69 1.65
30 ['HitL'] first lick after cue nan n 0 early 0 range -0.68 0.97
31 ['ErrR'] first lick after cue 0.0951 n 3 early 0 range -0.68 1.79
32 ['HitL'] first lick after cue 1.2597 n 3 early 0 range -0.7 1.43
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > an3.py <<'EOF'
import numpy as np, pickle
z=np.load('sess.npz'); t=z['time']; tr=z['trial']; vm=z['vm']
p=pickle.load(open('sess.pkl','rb')); tp=p['tp']; ids=list(p['ids']); ts=p['ts']
for tid in [42,51,31]:
    i=ids.index(tid); s=tr==tid; lk=vm[s,0]; tt=t[s]-ts[i]; cue=tp['CueTime'][i]
    neg=np.where(lk<-0.3)[0]
    print(tid,'cue',cue,'neg times',np.round(tt[neg][[0,-1]],3) if len(neg) else None, len(neg))
    w=(tt>cue-0.05)&(tt<cue+0.15)
    print(np.round(tt[w][::20]-cue,3)); print(np.round(lk[w][::20],2))
EOF
python an3.py
```

```
42 cue 3.1733199999999897 neg times [5. 5.] 1
[-0.05  -0.048 -0.046 -0.044 -0.042 -0.04  -0.038 -0.036 -0.034 -0.032
 -0.03  -0.028 -0.026 -0.024 -0.022 -0.02  -0.018 -0.016 -0.014 -0.012
 -0.01  -0.008 -0.006 -0.004 -0.002  0.     0.002  0.004  0.006  0.008
  0.01   0.012  0.014  0.016  0.018  0.02   0.022  0.024  0.026  0.028
  0.03   0.032  0.034  0.036  0.038  0.04   0.042  0.044  0.046  0.048
  0.05   0.052  0.054  0.056  0.058  0.06   0.062  0.064  0.066  0.068
  0.07   0.072  0.074  0.076  0.078  0.08   0.082  0.084  0.086  0.088
  0.09   0.092  0.094  0.096  0.098  0.1    0.102  0.104  0.106  0.108
  0.11   0.112  0.114  0.116  0.118  0.12   0.122  0.124  0.126  0.128
  0.13   0.132  0.134  0.136  0.138  0.14   0.142  0.144  0.146  0.148]
[0.25 0.25 0.24 0.24 0.24 0.24 0.24 0.24 0.23 0.23 0.23 0.23 0.23 0.23
 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23
 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23 0.23
 0.24 0.24 0.24 0.24 0.25 0.25 0.26 0.28 0.27 0.26 0.27 0.28 0.27 0.26
 0.26 0.27 0.27 0.31 0.3  0.33 0.31 0.29 0.27 0.26 0.26 0.27 0.28 0.32
 0.42 0.63 0.88 1.06 1.17 1.25 1.31 1.39 1.41 1.44 1.42 1.43 1.44 1.43
 1.4  1.36 1.33 1.27 1.13 0.95 0.6  0.23 0.2  0.19 0.19 0.19 0.2  0.2
 0.2  0.2 ]
51 cue 3.173153999999954 neg times [5. 5.] 1
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/matlab_scripts/analyses_scripts; for f in analysis_ALM_population_selectivity.m analysis_ALM_IT_PT_selectivity.m; do echo "=== $f"; curl -s $B/$f | grep -v "^\s*$" | grep -v "^\s*%\s*$"; done
```

```
=== analysis_ALM_population_selectivity.m
%% figure 2,  supplemental figure 1, supplemental figure 2
clear all
close all
% check to see if the data has been compiled
if ~exist('ALM_compiled_all_data.mat')
    % if not, compile all data first
    analysis_compile_all_data
end
load ALM_compiled_all_data
sig_selective(isnan(sig_selective))=0;
%% example neurons, PSTH and raster
example_cells = {
    'ANM218457', 4, 9;...
    'ANM219248', 2, 11;...
    'ANM219037', 2, 5;...
    'ANM219031', 2, 17;...
    'ANM210862', 2, 21;...
    'ANM210863', 2, 10;...
    'ANM210863', 1, 9;...
[... 473 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/matlab_scripts/analyses_scripts; for f in func_getPSTH.m analysis_ALM_error_trial_selectivity.m; do echo "=== $f"; curl -s $B/$f | grep -v "^\s*$" | grep -v "line(\|xlim\|ylim\|xlabel\|ylabel"; done; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/checksums.md5 | grep -v voltage_traces | grep -v nwb_files
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p entries/crcns-alm-1-li-2015; ls entries | head -3; grep -n "related\|crcns" schemas/entry.schema.json | head
```

```
000003-senzai-2017
000004-chandravadia-2020
000005-yu-2016
7:  "required": ["schema_version", "name", "type", "title", "description", "license", "notebooks", "related"],
39:    "related": {
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-alm-1-li-2015/alm.py",
 "content": "\"\"\"Loading and measures for CRCNS data set alm-1 (Li, Chen, Guo, Gerfen & Svoboda 2015, Nature\n519, 51-56, doi:10.1038/nature14178).\n\nThe data set (doi:10.6080/K0RF5RZT) is unversioned; the files are read from the public S3 bucket\n`crcnsarchive` under `alm-1/live/`. Each animal's sessions are MATLAB files inside one\n`data_structure_<animal>.tar.gz`; the tar is streamed and decompressed in memory, one session at\na time, and reduced to what the analyses need. Nothing is written to disk.\n\nEach session is reduced to:\n\n- a trial table: trial id, start time, pole in, pole out and cue times (seconds from trial\n  start), `GoodTrials`, `PhotostimulationType`, the eight trial type flags, the reaction time\n  read from the lick trace, and a summary of the photostimulation waveform;\n- per unit: its cell type labels, its median channel, its mean waveform, and its spike times\n  (seconds from the start of their trial) with the index of their trial;\n- per tagging trial: the onset times of the light pulses, read from the AOM input trace.\n\nWhere the parameters come from:\n\n- Epochs. Sample from `PoleInTime` to `PoleOutTime`, delay from `PoleOutTime` to `CueTime`\n  (the data set's trial properties; Methods, Behaviour). The response epoch is `RESPONSE_S` =\n  1.3 s after the cue, the claims file's reading (a), which is also what the data set's own\n  script `matlab_scripts/analyses_scripts/analysis_compile_all_data.m` uses; 1.5 s is reading (b).\n- Trials for the neural analyses. Correct trials (Methods, Electrophysiology data analyses),\n  `GoodTrials` = 1 (the data description: trials with 0 \"should be discarded\"), no axonal\n  photostimulation (`PhotostimulationType` = 0; the claims file's shared methods), and lick\n  early trials dropped or kept (claims file readings a and b). Only trials within each unit's\n  recorded span (from its first to its last trial with a spike) count for it: an assumption\n  taken from `analysis_compile_all_data.m` (\"index stable trials\"); the paper does not say.\n- Spike width is the trough-to-peak interval of the mean waveform (Methods), at the sampling\n  rate of 19531.25 Hz (Methods; the data description). The thresholds 0.35 and 0.45 ms are the\n  Methods'.\n- Selectivity test: two-tailed t-test with pooled variance on spike rates of lick right against\n  lick left trials, P < 0.05 (Methods; claims file). Welch is the claims file's variant.\n- Time courses: 200 ms windows (Fig. 2c and ED Fig. 2a legends), stepped by `STEP_S` = 10 ms,\n  a standard choice for a detail that cannot change a result beyond the window.\n- Reaction time: first rise of the lick (mouth movement) trace after the cue (Methods,\n  Behaviour). The paper gives no threshold; `LICK_RISE` holds the rises above the pre-cue\n  baseline that are run as readings (an assumption, see the notebook).\n- Light pulses: onsets where the AOM input trace (`aom_input_trace`, 10 kHz) crosses half its\n  trial maximum, in trials whose maximum exceeds `AOM_MIN` volts (a standard choice).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport tarfile\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport fsspec\nimport numpy as np\nimport pandas as pd\nimport scipy.io as sio\nfrom scipy import stats\n\nDATASET = \"crcns:alm-1\"\nDATASET_DOI = \"10.6080/K0RF5RZT\"\nVERSION = \"unversioned\"\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/\"\nANIMALS = [\"ANM210861\", \"ANM210862\", \"ANM210863\", \"ANM214427\", \"ANM214429\", \"ANM214430\",\n           \"ANM218453\", \"ANM218457\", \"ANM218693\", \"ANM219030\", \"ANM219031\", \"ANM219033\",\n           \"ANM219036\", \"ANM219037\", \"ANM219038\", \"ANM219247\", \"ANM219248\", \"ANM219253\",\n           \"ANM221977\"]\n\nFS_WAVEFORM = 19531.25        # Hz, Methods and data description\nFS_MAX_MS, PYR_MIN_MS = 0.35, 0.45   # Methods\nRESPONSE_S = 1.3              # response epoch, reading (a); 1.5 s is reading (b)\nSTEP_S = 0.01                 # time-course step, standard choice\nWIN_S = 0.2                   # averaging window, Fig. 2c legend\nLICK_RISE = (0.05, 0.1, 0.2, 0.5)   # volts above the pre-cue baseline, readings\nAOM_MIN = 1.0                 # volts, a trial with a light pulse\nTRIAL_TYPES = [\"HitR\", \"HitL\", \"ErrR\", \"ErrL\", \"NoLickR\", \"NoLickL\", \"LickEarly\", \"StimTrials\"]\n\n\ndef _as_list(x):\n    if isinstance(x, str):\n        return [x]\n    return [str(v) for v in np.atleast_1d(x)]\n\n\ndef _reduce(o, animal, session):\n    \"\"\"Reduce one session object (`obj` of a data structure file) to what the analyses use.\"\"\"\n    ids = np.atleast_1d(o.trialIds).astype(int)\n    start = np.atleast_1d(o.trialStartTimes).astype(float)\n    props = dict(zip(_as_list(o.trialPropertiesHash.keyNames), o.trialPropertiesHash.value))\n    tts = _as_list(o.trialTypeStr)\n    mat = np.atleast_2d(o.trialTypeMat)\n    trials = pd.DataFrame({\"trial_id\": ids, \"start\": start,\n                           \"pole_in\": props[\"PoleInTime\"].astype(float),\n                           \"pole_out\": props[\"PoleOutTime\"].astype(float),\n                           \"cue\": props[\"CueTime\"].astype(float),\n                           \"good\": props[\"GoodTrials\"].astype(float),\n                           \"ptype\": props[\"PhotostimulationType\"].astype(float)})\n    for name in TRIAL_TYPES:\n        trials[name] = mat[tts.index(name)].astype(bool) if name in tts else False\n    trials.insert(0, \"session\", session)\n    trials.insert(0, \"animal\", animal)\n\n    # time series: lick trace, AOM input, laser power, 10 kHz, only within trials\n    ts = o.timeSeriesArrayHash.value\n    names = _as_list(ts.idStr)\n    t = np.asarray(ts.time, float)\n    tr = np.asarray(ts.trial).astype(int)\n    vm = np.asarray(ts.valueMatrix)\n    lick, aom, power = (vm[:, names.index(n)] for n in (\"lick_trace\", \"aom_input_trace\", \"laser_power\"))\n    bounds = np.flatnonzero(np.diff(tr)) + 1\n    seg_start = np.r_[0, bounds]\n    seg_end = np.r_[bounds, len(tr)]\n    pos = {tid: k for k, tid in enumerate(ids)}\n    extra = {k: np.full(len(ids), np.nan) for k in\n             [\"ts_offset\", \"ts_len\", \"aom_max\", \"power_max\", \"stim_on\", \"stim_off\", \"n_pulses\",\n              \"pulse_ms\", \"lick_base\", \"n_lick_pre\"] + [f\"rt_{r}\" for r in LICK_RISE]}\n    pulses = {}\n    for a, b in zip(seg_start, seg_end):\n        tid = tr[a]\n        if tid not in pos:\n            continue\n        k = pos[tid]\n        tt = t[a:b] - start[k]\n        extra[\"ts_offset\"][k] = tt[0]\n        extra[\"ts_len\"][k] = tt[-1] - tt[0]\n        am = aom[a:b]\n        extra[\"aom_max\"][k] = am.max()\n        extra[\"power_max\"][k] = power[a:b].max()\n        if am.max() > AOM_MIN:\n            hi = am > am.max() / 2\n            on = np.flatnonzero(hi[1:] & ~hi[:-1]) + 1\n            off = np.flatnonzero(~hi[1:] & hi[:-1]) + 1\n            if len(on):\n                extra[\"stim_on\"][k] = tt[on[0]]\n                extra[\"stim_off\"][k] = tt[off[-1]] if len(off) else tt[-1]\n                extra[\"n_pulses\"][k] = len(on)\n                if len(off) >= len(on):\n                    extra[\"pulse_ms\"][k] = np.median(tt[off[:len(on)]] - tt[on]) * 1e3\n                pulses[k] = tt[on]\n        cue = trials.cue.iat[k]\n        if np.isfinite(cue):\n            lk = lick[a:b]\n            pre = (tt > cue - 0.2) & (tt <= cue)\n            post = tt > cue\n            if pre.sum() > 100 and post.sum() > 100:\n                base = np.median(lk[pre])\n                extra[\"lick_base\"][k] = base\n                for r in LICK_RISE:\n                    above = np.flatnonzero(post & (lk > base + r))\n                    extra[f\"rt_{r}\"][k] = tt[above[0]] - cue if len(above) else np.nan\n            samp = (tt > trials.pole_in.iat[k]) & (tt < cue)\n            hi = lk > 1.0\n            extra[\"n_lick_pre\"][k] = int(np.sum(samp[1:] & hi[1:] & ~hi[:-1]))\n    for key, v in extra.items():\n        trials[key] = v\n\n    units = []\n    for i, u in enumerate(np.atleast_1d(o.eventSeriesHash.value)):\n        et = np.atleast_1d(u.eventTimes).astype(float)\n        etr = np.atleast_1d(u.eventTrials).astype(int)\n        k = np.searchsorted(ids, etr)\n        ok = (k < len(ids)) & (ids[np.minimum(k, len(ids) - 1)] == etr)\n        wf = np.atleast_2d(u.waveforms)\n        units.append({\"animal\": animal, \"session\": session, \"unit\": i + 1,\n                      \"cell_types\": tuple(_as_list(u.cellType)) if np.size(u.cellType) else (),\n                      \"channel\": float(np.median(u.channel)),\n                      \"waveform\": wf.mean(axis=0),\n                      \"n_spikes\": len(et),\n                      \"spike_t\": et[ok] - start[k[ok]],\n                      \"spike_k\": k[ok].astype(np.int32),\n                      \"spike_t_session\": et[ok]})\n    return {\"animal\": animal, \"session\": session, \"trials\": trials, \"units\": units,\n            \"pulses\": pulses}\n\n\ndef load_animal(animal):\n    \"\"\"Stream one animal's tar.gz and reduce each session in it.\"\"\"\n    url = f\"{BASE}datafiles/data_structure_files/data_structure_{animal}.tar.gz\"\n    out = []\n    with fsspec.open(url, block_size=2**23).open() as fh:\n        with tarfile.open(fileobj=fh, mode=\"r|gz\") as tf:\n            for m in tf:\n                if not m.isfile() or not m.name.endswith(\".mat\"):\n                    continue\n                raw = tf.extractfile(m).read()\n                o = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)[\"obj\"]\n                del raw\n                session = m.name.split(\"/\")[-1].replace(\"data_structure_\", \"\").replace(\".mat\", \"\")\n                out.append(_reduce(o, animal, session))\n                del o\n    return out\n\n\ndef load_meta():\n    \"\"\"Per-session metadata from meta_data_files.tar.gz.\"\"\"\n    rows = []\n    with fsspec.open(BASE + \"datafiles/meta_data_files.tar.gz\").open() as fh:\n        with tarfile.open(fileobj=fh, mode=\"r|gz\") as tf:\n            for m in tf:\n                if not m.isfile():\n                    continue\n                md = sio.loadmat(io.BytesIO(tf.extractfile(m).read()), squeeze_me=True,\n                                 struct_as_record=False)[\"meta_data\"]\n                ph = getattr(md, \"photostim\", None)\n                rows.append({\"session\": m.name.split(\"/\")[-1].replace(\"meta_data_\", \"\").replace(\".mat\", \"\"),\n                             \"animal_id\": \"/\".join(_as_list(md.animalID)),\n                             \"strain\": \"/\".join(_as_list(md.animalStrain)),\n                             \"gene\": \"/\".join(_as_list(md.animalGeneModification)),\n                             \"date_of_birth\": str(md.dateOfBirth),\n                             \"penetration\": int(md.extracellular.penetrationN),\n                             \"probe\": str(md.extracellular.probeType),\n                             \"photostim_location\": \"/\".join(_as_list(ph.photostimLocation)) if ph is not None and hasattr(ph, \"photostimLocation\") else \"\"})\n    return pd.DataFrame(rows)\n\n\ndef load_all(workers=3):\n    \"\"\"Stream every animal (largest files first, `workers` at a time) and return the sessions.\"\"\"\n    with ProcessPoolExecutor(workers) as ex:\n        parts = list(ex.map(load_animal, ANIMALS))\n    return [s for p in parts for s in p]\n\n\ndef spike_width_ms(waveform):\n    \"\"\"Trough-to-peak interval of a mean waveform (Methods): from the trough to the following\n    maximum.\"\"\"\n    w = np.asarray(waveform, float)\n    i = int(np.argmin(w))\n    j = i + int(np.argmax(w[i:]))\n    return (j - i) / FS_WAVEFORM * 1e3\n\n\ndef trial_mask(trials, unit, lick_early=\"drop\", outcome=\"hit\"):\n    \"\"\"Trials a unit's analysis uses. `outcome` is 'hit' or 'err'.\"\"\"\n    span = np.zeros(len(trials), bool)\n    if len(unit[\"spike_k\"]):\n        span[unit[\"spike_k\"].min():unit[\"spike_k\"].max() + 1] = True\n    m = span & (trials.good.values == 1) & (trials.ptype.values == 0) & np.isfinite(trials.cue.values)\n    if lick_early == \"drop\":\n        m &= ~trials.LickEarly.values\n    right = trials[\"HitR\" if outcome == \"hit\" else \"ErrR\"].values\n    left = trials[\"HitL\" if outcome == \"hit\" else \"ErrL\"].values\n    return m & right, m & left\n\n\ndef counts_in(unit, trials, sel, t0, t1):\n    \"\"\"Spike counts of a unit in trials `sel` between t0 and t1 (arrays, seconds from trial start).\"\"\"\n    idx = np.flatnonzero(sel)\n    out = np.zeros(len(idx))\n    if not len(idx):\n        return out\n    k, t = unit[\"spike_k\"], unit[\"spike_t\"]\n    m = np.isin(k, idx)\n    k, t = k[m], t[m]\n    loc = np.searchsorted(idx, k)\n    a, b = t0[k], t1[k]\n    inside = (t > a) & (t < b)\n    np.add.at(out, loc[inside], 1)\n    return out\n\n\ndef epoch_bounds(trials, response_s=RESPONSE_S):\n    \"\"\"Start and end (s from trial start) of sample, delay and response epochs, and the whole\n    trial (sample start to response end), per trial.\"\"\"\n    pi, po, cu = trials.pole_in.values, trials.pole_out.values, trials.cue.values\n    return {\"sample\": (pi, po), \"delay\": (po, cu), \"response\": (cu, cu + response_s),\n            \"trial\": (pi, cu + response_s), \"pre\": (pi - 0.5, pi), \"pre_all\": (np.zeros_like(pi), pi)}\n\n\ndef unit_epoch_rates(unit, trials, lick_early=\"drop\", response_s=RESPONSE_S, outcome=\"hit\"):\n    \"\"\"Per epoch, the spike rates (spikes/s) on lick right and lick left trials.\"\"\"\n    r, l = trial_mask(trials, unit, lick_early, outcome)\n    out = {\"n_right\": int(r.sum()), \"n_left\": int(l.sum())}\n    for name, (a, b) in epoch_bounds(trials, response_s).items():\n        dur = b - a\n        out[name] = (counts_in(unit, trials, r, a, b) / dur[r], counts_in(unit, trials, l, a, b) / dur[l])\n    return out\n\n\ndef ttest_p(x, y, welch=False):\n    if len(x) < 2 or len(y) < 2:\n        return np.nan\n    if np.var(x) == 0 and np.var(y) == 0:\n        return 1.0 if np.mean(x) == np.mean(y) else 0.0\n    return stats.ttest_ind(x, y, equal_var=not welch).pvalue\n\n\ndef cue_aligned_counts(unit, trials, sel, centers, win=WIN_S):\n    \"\"\"Spike counts per trial in windows of `win` s centred on `centers` (s from the cue).\"\"\"\n    idx = np.flatnonzero(sel)\n    out = np.zeros((len(idx), len(centers)))\n    if not len(idx):\n        return out\n    k, t = unit[\"spike_k\"], unit[\"spike_t\"]\n    m = np.isin(k, idx)\n    rel = t[m] - trials.cue.values[k[m]]\n    loc = np.searchsorted(idx, k[m])\n    edges_lo = centers - win / 2\n    for j, lo in enumerate(edges_lo):\n        inside = (rel > lo) & (rel < lo + win)\n        out[:, j] = np.bincount(loc[inside], minlength=len(idx))\n    return out\n"
}
```

```
File created successfully at: entries/crcns-alm-1-li-2015/alm.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/crcns-alm-1-li-2015 && . $TMPDIR/dev/bin/activate && python -c "
import time,resource,alm,pickle
t=time.time(); s=alm.load_animal('ANM221977'); print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
for x in s:
    tr=x['trials']; print(x['session'], len(tr), len(x['units']), len(x['pulses']), tr.ts_offset.describe()[['min','max']].values, tr.ptype.value_counts(dropna=False).to_dict())
    print(tr[['rt_0.05','rt_0.1','rt_0.2','rt_0.5']].median().values, tr.pulse_ms.median(), tr.n_pulses.value_counts().to_dict())
    print([u['cell_types'] for u in x['units']])
pickle.dump(s,open('$TMPDIR/a221977.pkl','wb'))
"
```

```
18.7718026638031 1.229596
ANM221977_20140115 337 8 138 [0. 0.] {0.0: 198, 2.0: 103, nan: 36}
[0.070196 0.079912 0.08948  0.095813] 0.9999999999763531 {20.0: 103, 18.0: 35}
[('pyramidal',), ('pyramidal',), ('pyramidal',), (), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',)]
ANM221977_20140116 415 13 116 [0. 0.] {0.0: 299, 2.0: 105, nan: 11}
[0.113613 0.145979 0.461846 1.00688 ] 0.9999999999763531 {20.0: 105, 18.0: 11}
[('pyramidal', 'IT'), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',)]
ANM221977_20140118 178 15 57 [0. 0.] {0.0: 119, 2.0: 50, nan: 9}
[0.137846 0.51528  0.714046 1.265546] 0.9999999999763531 {20.0: 49, 24.0: 2, 29.0: 1, 33.0: 1, 34.0: 1, 27.0: 1, 37.0: 1, 25.0: 1}
[('pyramidal',), ('FS',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), (), ('FS',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',), ('pyramidal',)]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && date -u && python -c "
import time,resource,alm,pickle
t=time.time(); S=alm.load_all(4); print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e6)
pickle.dump(S,open('$TMPDIR/all.pkl','wb')); print(len(S), sum(len(s['units']) for s in S))
"
```

```
Sat Nov  7 21:27:34 UTC 2026
179.92389822006226 0.32714 1.803012
99 1408
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,alm,numpy as np,pandas as pd, collections
S=pickle.load(open('$TMPDIR/all.pkl','rb'))
U=[u for s in S for u in s['units']]
ct=collections.Counter(u['cell_types'] for u in U); print(ct)
w=np.array([alm.spike_width_ms(u['waveform']) for u in U])
print('width uniq', np.unique(np.round(w,3))[:20])
print('<0.35',(w<0.35).sum(),'>0.45',(w>0.45).sum(),'mid',((w>=0.35)&(w<=0.45)).sum())
lab=np.array(['FS' if 'FS' in u['cell_types'] else 'pyr' if 'pyramidal' in u['cell_types'] else 'none' for u in U])
print(pd.crosstab(lab, pd.cut(w,[0,0.35,0.45,5])))
print('animals', len(set(u['animal'] for u in U)), 'sessions', len(S))
T=pd.concat([s['trials'] for s in S]); print(len(T)); print(T.ptype.value_counts(dropna=False)); print(T.good.value_counts())
print(T.groupby('ptype',dropna=False)[['n_pulses','pulse_ms','power_max','stim_on']].median())
"
```

```
Counter({('pyramidal',): 1173, ('FS',): 124, ('pyramidal', 'PT'): 45, (): 39, ('pyramidal', 'IT'): 27})
width uniq [0.154 0.205 0.256 0.307 0.41  0.461 0.512 0.563 0.614 0.666]
<0.35 158 >0.45 1245 mid 5
col_0  (0.0, 0.35]  (0.35, 0.45]  (0.45, 5.0]
row_0                                        
FS             124             0            0
none            34             5            0
pyr              0             0         1245
animals 19 sessions 99
31439
ptype
0.0    19492
NaN     4261
1.0     4029
2.0     3162
4.0      171
5.0      164
3.0      160
Name: count, dtype: int64
good
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,alm,numpy as np,pandas as pd
S=pickle.load(open('$TMPDIR/all.pkl','rb'))
T=pd.concat([s['trials'] for s in S]); T['has']=T.aom_max>1
T['pt']=T.ptype.fillna(-1)
g=T.groupby(['animal','pt']).agg(n=('has','size'),stim=('has','sum'),good=('good','sum'),npul=('n_pulses','median'),pms=('pulse_ms','median'),pw=('power_max','median'),on=('stim_on','median'),off=('stim_off','median'))
pd.set_option('display.width',200); pd.set_option('display.max_rows',200)
print(g.round(2))
"
```

```
n  stim    good  npul   pms     pw    on   off
animal    pt                                                     
ANM210861 -1.0   283   267   279.0  14.0  50.0  47.10  3.20  4.45
           0.0  1007     0   960.0   NaN   NaN   0.01   NaN   NaN
ANM210862 -1.0   215   162   204.0  16.0  50.0  47.10  2.72  3.97
           0.0   756    43   666.0  16.0  50.0   0.01  3.20  4.45
ANM210863 -1.0   216   216   210.0  16.0  50.0  47.10  2.03  3.28
           0.0   815     0   736.0   NaN   NaN   0.01   NaN   NaN
ANM214427 -1.0   265   248     0.0  26.0  49.9  22.65  0.70  2.65
           0.0   890     0   888.0   NaN   NaN   0.00   NaN   NaN
           1.0    72    71    66.0  20.0   1.0  82.00  0.30  4.81
           2.0   258   255   252.0  20.0   1.0  47.10  0.30  4.81
ANM214429 -1.0   374   367     9.0  22.0  49.8  22.65  0.70  2.65
           0.0  1177     0  1168.0   NaN   NaN   0.00   NaN   NaN
           1.0   246   246   245.0  20.0   1.0  82.00  0.30  4.81
           2.0   254   254   242.0  20.0   1.0  47.10  0.30  4.81
ANM214430 -1.0   191   180     0.0  25.0  50.0  22.66  0.70  2.65
           0.0   507     0   499.0   NaN   NaN   0.00   NaN   NaN
           1.0   237   237   237.0  20.0   1.0  82.00  0.30  4.81
           2.0   310   310   298.0  20.0   1.0  47.10  0.30  4.81
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/alm-1/live/matlab_scripts/demos/Demo_get_performance.m | grep -v "^\s*$" | head -70; date -u
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat >> entries/crcns-alm-1-li-2015/alm.py <<'EOF'


def unit_table(sessions, lick_early="drop", response_s=RESPONSE_S):
    """One row per unit: labels, spike width, trial counts, per-epoch rates on lick right (R)
    and lick left (L) correct trials and on error trials (labelled by the instructed side), the
    selectivity t-test P values (pooled and Welch), and baseline rates."""
    rows = []
    for s in sessions:
        tr = s["trials"]
        for u in s["units"]:
            ct = u["cell_types"]
            row = {"animal": s["animal"], "session": s["session"], "unit": u["unit"],
                   "label": "FS" if "FS" in ct else "pyramidal" if "pyramidal" in ct else "unclassified",
                   "tag": "PT" if "PT" in ct else "IT" if "IT" in ct else "",
                   "width_ms": spike_width_ms(u["waveform"]), "n_spikes": u["n_spikes"]}
            rates = unit_epoch_rates(u, tr, lick_early, response_s)
            err = unit_epoch_rates(u, tr, lick_early, response_s, outcome="err")
            row["n_R"], row["n_L"] = rates["n_right"], rates["n_left"]
            row["n_errR"], row["n_errL"] = err["n_right"], err["n_left"]
            for ep in ("sample", "delay", "response", "trial", "pre", "pre_all"):
                r, l = rates[ep]
                row[f"{ep}_R"] = r.mean() if len(r) else np.nan
                row[f"{ep}_L"] = l.mean() if len(l) else np.nan
                er, el = err[ep]
                row[f"{ep}_errR"] = er.mean() if len(er) else np.nan
                row[f"{ep}_errL"] = el.mean() if len(el) else np.nan
                if ep in ("sample", "delay", "response", "trial"):
                    row[f"p_{ep}"] = ttest_p(r, l)
                    row[f"pw_{ep}"] = ttest_p(r, l, welch=True)
            rows.append(row)
    df = pd.DataFrame(rows)
    for kind, col in (("p", "selective"), ("pw", "selective_welch")):
        sig = df[[f"{kind}_sample", f"{kind}_delay", f"{kind}_response"]].fillna(1) < 0.05
        df[col] = sig.any(axis=1)
        df[col + "_prep"] = sig.iloc[:, 0] | sig.iloc[:, 1]
        df[col + "_peri"] = sig.iloc[:, 2]
    df["contra"] = df.trial_R > df.trial_L
    return df


def categories(df, sel_col="selective"):
    """Preparatory only, both, peri-movement only, among the rows where `sel_col` holds."""
    d = df[df[sel_col]]
    prep, peri = d[sel_col + "_prep"], d[sel_col + "_peri"]
    return {"prep_only": int((prep & ~peri).sum()), "both": int((prep & peri).sum()),
            "peri_only": int((~prep & peri).sum()), "n": len(d)}


def bootstrap_more_ipsi(contra, n_boot=10_000, rng=None):
    """Methods (Fig. 3f, j): neurons resampled with replacement; P is the fraction of resamples
    with more ipsi-preferring than contra-preferring neurons (one-tailed)."""
    contra = np.asarray(contra, bool)
    n = len(contra)
    if n == 0:
        return np.nan
    k = rng.binomial(n, contra.mean(), size=n_boot)   # resampling n neurons with replacement
    return float(np.mean(n - k > k))


def antidromic_latencies(session, unit, ptypes, order=0, max_ms=20.0):
    """Latency (ms) of the first spike after each light pulse in tagging trials of the given
    photostimulation types. `order` 0 is the first pulse of each pair, 1 the second. Pulses are
    paired when the next onset follows within 15 ms. Returns one latency per pulse (NaN when no
    spike within `max_ms`), so the response probability is the fraction that is finite."""
    tr = session["trials"]
    out = []
    k, t = unit["spike_k"], unit["spike_t"]
    span = (k.min(), k.max()) if len(k) else (0, -1)
    for ti, on in session["pulses"].items():
        if not np.isfinite(tr.ptype.iat[ti]) or tr.ptype.iat[ti] not in ptypes:
            continue
        if not (span[0] <= ti <= span[1]):
            continue
        first = np.r_[True, np.diff(on) > 0.015]
        idx = np.flatnonzero(first)
        if order == 1:
            idx = idx[(idx + 1 < len(on))]
            idx = idx[np.diff(on)[idx] <= 0.015] + 1
        st = np.sort(t[k == ti])
        for p in on[idx]:
            j = np.searchsorted(st, p, side="right")
            lat = (st[j] - p) * 1e3 if j < len(st) else np.inf
            out.append(lat if lat <= max_ms else np.nan)
    return np.array(out)


def latency_mode_stats(lat, half_width_ms=1.0, bin_ms=0.2):
    """Mean latency and jitter (s.d.) of the spikes within `half_width_ms` of the modal latency
    (bins of `bin_ms`), with the response probability and the number of responses."""
    lat = lat[np.isfinite(lat)]
    if len(lat) < 3:
        return np.nan, np.nan, 0.0, len(lat)
    h, e = np.histogram(lat, bins=np.arange(0, lat.max() + bin_ms, bin_ms))
    mode = e[np.argmax(h)] + bin_ms / 2
    near = lat[np.abs(lat - mode) <= half_width_ms]
    return near.mean(), near.std(ddof=1) if len(near) > 1 else np.nan, len(near), len(lat)
EOF
cd entries/crcns-alm-1-li-2015 && . $TMPDIR/dev/bin/activate && python -c "
import pickle,alm,time,numpy as np
S=pickle.load(open('$TMPDIR/all.pkl','rb'))
t=time.time(); df=alm.unit_table(S); print(time.time()-t)
df.to_pickle('$TMPDIR/ut.pkl')
p=df[df.label=='pyramidal']; print(len(p), p.selective.sum(), p.selective.mean(), p.selective_welch.sum(), alm.categories(p), p[p.selective].contra.sum(), (~p[p.selective].contra).sum())
"
```

```
/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/stats/_axis_nan_policy.py:601: RuntimeWarning: Precision loss occurred in moment calculation due to catastrophic cancellation. This occurs when the data are nearly identical. Results may be unreliable.
  res = hypotest_fun_out(*samples, **kwds)
8.906797409057617
1245 912 0.7325301204819277 906 {'prep_only': 219, 'both': 389, 'peri_only': 304, 'n': 912} 427 485
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,alm,numpy as np,pandas as pd
S=pickle.load(open('$TMPDIR/all.pkl','rb'))
rows=[]
for s in S:
    for u in s['units']:
        tag='PT' if 'PT' in u['cell_types'] else 'IT' if 'IT' in u['cell_types'] else ''
        if not tag: continue
        for o in (0,1):
            lat=alm.antidromic_latencies(s,u,{1.0} if tag=='PT' else {2.0,3.0,4.0,5.0},order=o)
            for hw in (0.5,1.0,2.0):
                m,sd,nn,nr=alm.latency_mode_stats(lat,hw)
                rows.append(dict(tag=tag,order=o,hw=hw,mean=m,sd=sd,n=nn,npulse=len(lat),nresp=nr))
d=pd.DataFrame(rows)
print(d.groupby(['tag','order','hw'])[['mean','sd','n','npulse']].agg(['mean','median','count']).round(3))
"
```

```
mean                  sd  ...         npulse             
                mean median count   mean  ... count     mean median count
tag order hw                              ...                            
IT  0     0.5  6.114  4.551    27  0.167  ...    27  457.222  360.0    27
          1.0  6.093  4.538    27  0.235  ...    27  457.222  360.0    27
          2.0  6.034  4.457    27  0.385  ...    27  457.222  360.0    27
    1     0.5  4.763  3.500    25  0.151  ...    27  426.815  360.0    27
          1.0  4.786  3.509    25  0.232  ...    27  426.815  360.0    27
          2.0  4.771  3.472    25  0.397  ...    27  426.815  360.0    27
PT  0     0.5  2.921  2.724    45  0.112  ...    45  523.311  540.0    45
          1.0  2.918  2.714    45  0.124  ...    45  523.311  540.0    45
          2.0  2.913  2.708    45  0.201  ...    45  523.311  540.0    45
    1     0.5  2.816  2.824    44  0.125  ...    45  523.311  540.0    45
          1.0  2.815  2.823    44  0.144  ...    45  523.311  540.0    45
          2.0  2.812  2.796    44  0.233  ...    45  523.311  540.0    45

[12 rows x 12 columns]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python -c "
import pickle,alm,numpy as np,pandas as pd
S=pickle.load(open('$TMPDIR/all.pkl','rb'))
for s in S:
    for u in s['units']:
        if 'IT' not in u['cell_types']: continue
        out=[]
        for o in (0,1):
            lat=alm.antidromic_latencies(s,u,{2.0,3.0,4.0,5.0},order=o)
            m,sd,nn,nr=alm.latency_mode_stats(lat,1.0)
            h,_=np.histogram(lat[np.isfinite(lat)],bins=np.arange(0,20.5,1))
            out.append(f'o{o} m={m:.2f} sd={sd:.2f} n={nn}/{len(lat)} hist={h.tolist()}')
        print(s['session'],u['unit'],s['trials'].ptype.value_counts().to_dict()); print('   ',out[0]); print('   ',out[1])
" 2>&1 | head -90
```

```
ANM214427_20130806 2 {0.0: 156, 2.0: 34, 1.0: 27}
    o0 m=3.28 sd=0.20 n=79/200 hist=[0, 0, 5, 74, 0, 2, 2, 0, 1, 0, 0, 1, 0, 3, 17, 2, 1, 2, 1, 0]
    o1 m=3.11 sd=0.17 n=35/200 hist=[1, 0, 6, 29, 2, 1, 3, 1, 0, 2, 2, 1, 2, 0, 3, 0, 1, 0, 2, 0]
ANM214427_20130808 1 {0.0: 180, 2.0: 73}
    o0 m=14.91 sd=0.21 n=62/610 hist=[0, 0, 0, 10, 57, 8, 1, 0, 0, 0, 0, 0, 0, 0, 41, 21, 0, 0, 0, 0]
    o1 m=3.88 sd=0.21 n=75/610 hist=[0, 0, 0, 52, 23, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
ANM214427_20130808 2 {0.0: 180, 2.0: 73}
    o0 m=14.02 sd=0.17 n=65/600 hist=[3, 9, 14, 70, 40, 11, 21, 16, 9, 9, 3, 14, 9, 29, 36, 5, 15, 11, 7, 6]
    o1 m=2.98 sd=0.24 n=95/600 hist=[17, 12, 46, 47, 7, 21, 16, 9, 10, 18, 6, 7, 9, 8, 5, 6, 1, 3, 8, 3]
ANM218453_20131014 9 {0.0: 180, 3.0: 23, 4.0: 20, 5.0: 13, 2.0: 4}
    o0 m=4.54 sd=0.19 n=52/234 hist=[2, 2, 3, 3, 51, 0, 5, 7, 4, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    o1 m=nan sd=nan n=0.0/234 hist=[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ANM218453_20131014 16 {0.0: 180, 3.0: 23, 4.0: 20, 5.0: 13, 2.0: 4}
    o0 m=2.57 sd=0.07 n=32/80 hist=[2, 0, 32, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 2]
    o1 m=2.41 sd=0.06 n=22/80 hist=[0, 0, 22, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]
ANM218453_20131015 10 {0.0: 142, 5.0: 28, 3.0: 21, 4.0: 17, 2.0: 6}
    o0 m=4.00 sd=0.17 n=130/172 hist=[1, 0, 0, 71, 59, 3, 1, 0, 0, 1, 1, 0, 0, 0, 14, 3, 0, 0, 0, 0]
    o1 m=3.84 sd=0.19 n=108/172 hist=[2, 0, 0, 87, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ANM218453_20131017 8 {0.0: 146, 4.0: 28, 5.0: 17, 3.0: 16, 2.0: 3}
    o0 m=2.67 sd=0.07 n=30/108 hist=[0, 0, 30, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0]
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/def antidromic_latencies(session, unit, ptypes, order=0, max_ms=20.0):/def antidromic_latencies(session, unit, ptypes, order=0, max_ms=10.0):/; s/    spike within `max_ms`), so the response probability is the fraction that is finite."""/    spike within `max_ms`), so the response probability is the fraction that is finite. The\n    default window, 10 ms, ends before the second pulse of a pair (onsets 11 ms apart in the\n    AOM trace), so a response to the second pulse is not taken for one to the first."""/' alm.py && . $TMPDIR/dev/bin/activate && python -c "
import pickle,alm,numpy as np,pandas as pd
S=pickle.load(open('$TMPDIR/all.pkl','rb'))
T=pd.concat([s['trials'] for s in S])
ok=(T.good==1)&(T.ptype==0)&T.cue.notna()
hit=ok&(T.HitR|T.HitL)
for r in alm.LICK_RISE:
    c=f'rt_{r}'
    pm=T[hit&~T.LickEarly].groupby('animal')[c].mean()*1e3
    pmed=T[hit&~T.LickEarly].groupby('animal')[c].median()*1e3
    print(r,'mean of mouse means %.1f sd %.1f'%(pm.mean(),pm.std()),' mean of mouse medians %.1f'%pmed.mean(), 'nan frac',T[hit][c].isna().mean().round(3))
print(T[hit].groupby('animal').lick_base.median().round(2).to_dict())
print(T[hit].groupby('session')['rt_0.1'].median().mul(1e3).round(0).describe())
"
```

```
0.05 mean of mouse means 172.9 sd 70.8  mean of mouse medians 143.9 nan frac 0.22
0.1 mean of mouse means 222.1 sd 110.0  mean of mouse medians 177.9 nan frac 0.434
0.2 mean of mouse means 223.2 sd 115.4  mean of mouse medians 164.8 nan frac 0.735
0.5 mean of mouse means 273.5 sd 157.7  mean of mouse medians 181.3 nan frac 0.778
{'ANM210861': 0.13, 'ANM210862': 0.13, 'ANM210863': 0.15, 'ANM214427': 0.11, 'ANM214429': 3.62, 'ANM214430': 4.72, 'ANM218453': 0.11, 'ANM218457': 0.13, 'ANM218693': 0.13, 'ANM219030': 0.91, 'ANM219031': 0.09, 'ANM219033': 0.08, 'ANM219036': 0.08, 'ANM219037': 0.09, 'ANM219038': 0.08, 'ANM219247': 0.12, 'ANM219248': 0.18, 'ANM219253': 0.14, 'ANM221977': 0.2}
count     72.000000
mean     207.777778
std      139.010104
min        9.000000
25%      114.750000
50%      194.500000
75%      224.250000
max      633.000000
Name: rt_0.1, dtype: float64
```

**Agent calls Bash**

```bash
grep -n "lk > base + r" alm.py && sed -i 's/                    above = np.flatnonzero(post \& (lk > base + r))/                    above = np.flatnonzero(post \& (np.abs(lk - base) > r))/' alm.py && sed -i 's/  Behaviour). The paper gives no threshold; `LICK_RISE` holds the rises above the pre-cue\n//' alm.py && grep -n "np.abs(lk - base)" alm.py && . $TMPDIR/dev/bin/activate && python -c "
import time,alm,pickle
t=time.time(); S=alm.load_animal('ANM214429')+alm.load_animal('ANM219037'); print(time.time()-t)
import pandas as pd
T=pd.concat([s['trials'] for s in S]); hit=(T.good==1)&(T.ptype==0)&(T.HitR|T.HitL)&~T.LickEarly
for r in alm.LICK_RISE: print(r, T[hit].groupby('session')[f'rt_{r}'].agg(['median','mean',lambda x: x.isna().mean()]).mul([1e3,1e3,1]).round(3).to_string())
"
```

```
145:                    above = np.flatnonzero(post & (lk > base + r))
145:                    above = np.flatnonzero(post & (np.abs(lk - base) > r))
126.98649787902832
0.05                     median    mean  <lambda_0>
session                                       
ANM214429_20130805   0.046   0.046         0.0
ANM214429_20130806  44.312  63.029         0.0
ANM214429_20130807   0.079  23.952         0.0
ANM214429_20130808   0.079   4.311         0.0
ANM219037_20131116  87.879  90.334         0.0
ANM219037_20131117  82.330  94.817         0.0
ANM219037_20131118  81.896  89.591         0.0
ANM219037_20131119  79.780  91.703         0.0
ANM219037_20131120  78.713  92.057         0.0
ANM219037_20131121  82.746  84.804         0.0
ANM219037_20131122  77.596  83.254         0.0
0.1                     median     mean  <lambda_0>
session                                        
ANM214429_20130805   0.046    0.046         0.0
ANM214429_20130806  71.012  335.227         0.0
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='alm.py'; s=open(p).read()
old=s[s.index("            if pre.sum() > 100 and post.sum() > 100:"):s.index("            samp = (tt > trials.pole_in.iat[k])")]
new='''            post = (tt > cue) & (tt <= cue + 1.0)
            if pre.sum() > 100 and post.sum() > 100:
                base = np.median(lk[pre])
                noise = 1.4826 * np.median(np.abs(lk[pre] - base))
                exc = lk[post] - base
                peak = exc[np.argmax(np.abs(exc))]
                extra["lick_base"][k] = base
                extra["lick_peak"][k] = peak
                extra["lick_noise"][k] = noise
                for r in LICK_RISE:
                    if abs(peak) <= max(5 * noise, 0.02):
                        continue
                    above = np.flatnonzero(exc * np.sign(peak) > r * abs(peak))
                    extra[f"rt_{r}"][k] = tt[post][above[0]] - cue
'''
s=s.replace(old,new)
s=s.replace('"pulse_ms", "lick_base", "n_lick_pre"]','"pulse_ms", "lick_base", "lick_peak", "lick_noise", "n_lick_pre"]')
s=s.replace('LICK_RISE = (0.05, 0.1, 0.2, 0.5)   # volts above the pre-cue baseline, readings','LICK_RISE = (0.1, 0.25, 0.5)   # fractions of the trial\'s peak excursion, readings')
s=s.replace('''- Reaction time: first rise of the lick (mouth movement) trace after the cue (Methods,
  Behaviour). The paper gives no threshold; `LICK_RISE` holds the rises above the pre-cue
  baseline that are run as readings (an assumption, see the notebook).''','''- Reaction time: first movement of the lick (mouth movement) trace after the cue (Methods,
  Behaviour). The paper gives no detection rule, and the trace's level, scale and sign differ
  between sessions. The onset is the first sample after the cue at which the trace has moved
  from its pre-cue baseline (median of the 0.2 s before the cue) by a fraction `LICK_RISE` of
  its largest excursion in the 1 s after the cue; trials whose excursion is under five times
  the baseline noise (or 0.02 V) have none. The fractions are readings, an assumption.''')
open(p,'w').write(s)
EOF
grep -n "rt_\|LICK_RISE" alm.py | head; . $TMPDIR/dev/bin/activate && python -c "
import time,alm
t=time.time(); S=alm.load_animal('ANM221977'); print(time.time()-t)
import pandas as pd
T=pd.concat([s['trials'] for s in S]); hit=(T.good==1)&(T.ptype==0)&(T.HitR|T.HitL)&~T.LickEarly
for r in alm.LICK_RISE: print(r, T[hit].groupby('session')[f'rt_{r}'].agg(['median','mean',lambda x: x.isna().mean()]).mul([1e3,1e3,1]).round(3).to_string())
print(T[hit].groupby('session')[['lick_base','lick_peak','lick_noise']].median())
"
```

```
40:  from its pre-cue baseline (median of the 0.2 s before the cue) by a fraction `LICK_RISE` of
73:LICK_RISE = (0.1, 0.25, 0.5)   # fractions of the trial's peak excursion, readings
115:              "pulse_ms", "lick_base", "lick_peak", "lick_noise", "n_lick_pre"] + [f"rt_{r}" for r in LICK_RISE]}
153:                for r in LICK_RISE:
157:                    extra[f"rt_{r}"][k] = tt[post][above[0]] - cue
17.50078058242798
0.1                     median     mean  <lambda_0>
session                                        
ANM221977_20140115  83.596   97.025       0.000
ANM221977_20140116  85.263  135.218       0.000
ANM221977_20140118  63.979  112.047       0.014
0.25                      median     mean  <lambda_0>
session                                         
ANM221977_20140115   94.913  130.868       0.000
ANM221977_20140116  102.408  218.450       0.000
ANM221977_20140118   98.213  226.368       0.014
0.5                      median     mean  <lambda_0>
session                                         
ANM221977_20140115  101.729  156.206       0.000
ANM221977_20140116  119.463  289.175       0.000
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate && python -c "
import time,resource,alm,pickle
t=time.time(); S=alm.load_all(4); print(time.time()-t, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e6)
pickle.dump(S,open('$TMPDIR/all.pkl','wb'))
"
```

```
Sat Nov  7 21:35:31 UTC 2026
183.18796253204346 1.802876
```

**Agent calls Bash**

```bash
cat >> entries/crcns-alm-1-li-2015/alm.py <<'EOF'


BIN_S = 0.01
CUE_EDGES = np.round(np.arange(-3.6, 2.1 + 1e-9, BIN_S), 3)   # 10 ms bins around the cue


def cue_binned(unit, trials, sel):
    """Spike counts in 10 ms bins from 3.6 s before to 2.1 s after the cue, one row per trial
    in `sel`."""
    idx = np.flatnonzero(sel)
    out = np.zeros((len(idx), len(CUE_EDGES) - 1))
    if not len(idx):
        return out
    k, t = unit["spike_k"], unit["spike_t"]
    m = np.isin(k, idx)
    rel = t[m] - trials.cue.values[k[m]]
    loc = np.searchsorted(idx, k[m])
    b = np.floor((rel - CUE_EDGES[0]) / BIN_S).astype(int)
    ok = (b >= 0) & (b < out.shape[1])
    np.add.at(out, (loc[ok], b[ok]), 1)
    return out


def window_sums(binned, win=WIN_S):
    """Sliding sums over `win` s of 10 ms bins; returns the sums and the window centres (s from
    the cue)."""
    n = int(round(win / BIN_S))
    c = np.cumsum(np.pad(binned, ((0, 0), (1, 0))), axis=1)
    sums = c[:, n:] - c[:, :-n]
    centers = CUE_EDGES[:len(CUE_EDGES) - n] + win / 2
    return sums, np.round(centers, 3)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells.py",
 "content": "#%% md\n# Reproducing Li, Chen, Guo, Gerfen & Svoboda (2015) from CRCNS alm-1\n\n**Paper.** Li N, Chen T-W, Guo ZV, Gerfen CR, Svoboda K (2015). A motor cortex circuit for motor\nplanning and movement. *Nature* 519, 51-56.\n[doi:10.1038/nature14178](https://doi.org/10.1038/nature14178). The claims file\n(`claims/crcns-alm-1/10.1038-nature14178.yaml`) was written from the version of record (main\ntext, Methods and the legends of Figures 1 to 5 and Extended Data Figures 1 to 7).\n\n**Data set.** CRCNS alm-1, \"Extracellular recordings from anterior lateral motor cortex (ALM)\nneurons of adult mice performing a tactile decision behavior\",\n[doi:10.6080/K0RF5RZT](https://doi.org/10.6080/K0RF5RZT), read from the public bucket\n`crcnsarchive` under `alm-1/live/`. Version: `unversioned`. CRCNS data sets have no versions;\nthe bucket holds `alm-1/live/` (the data) and `alm-1/version_1/` and `alm-1/version_2/`, which\nhold only earlier copies of the documentation, and `alm-1/live/old/`, three example sessions\nthat the data description says are superseded. The paper cites no version, so the only\npublished copy of the data, `live`, is used. A later change can be detected with the MD5 sums\nof the files read, from the data set's `checksums.md5` (checked against the bucket below):\n\n| file | MD5 |\n|---|---|\n| datafiles/meta_data_files.tar.gz | cfacee06a26e5252ff22c922cab6e728 |\n| datafiles/data_structure_files/data_structure_ANM210861.tar.gz | ffc4cd8784c52d59509dec395f4dca6c |\n| datafiles/data_structure_files/data_structure_ANM210862.tar.gz | 455903de0b4efbbe3b6702d096001fd0 |\n| datafiles/data_structure_files/data_structure_ANM210863.tar.gz | a7ff42aed79240ce6522decd5a378bcc |\n| datafiles/data_structure_files/data_structure_ANM214427.tar.gz | 6506e8e3e5426af5e6aae2a7d4be020f |\n| datafiles/data_structure_files/data_structure_ANM214429.tar.gz | 72e04c6020096fc38de13b4e34d9a2f2 |\n| datafiles/data_structure_files/data_structure_ANM214430.tar.gz | 52747848292c53270f69093dd0aa72be |\n| datafiles/data_structure_files/data_structure_ANM218453.tar.gz | dbec672edde54c4fdf15a57ec1153deb |\n| datafiles/data_structure_files/data_structure_ANM218457.tar.gz | 4ab95446cc36e12debe2c85b86ec6ecc |\n| datafiles/data_structure_files/data_structure_ANM218693.tar.gz | 62ff3d44e9fd34c094d7e16cc27d14ad |\n| datafiles/data_structure_files/data_structure_ANM219030.tar.gz | 8d71cd3922820875730d56946e39f2be |\n| datafiles/data_structure_files/data_structure_ANM219031.tar.gz | ef87eff90c4ed2aff67f5260acd0cc8c |\n| datafiles/data_structure_files/data_structure_ANM219033.tar.gz | 29493ad8cce197c3f01c1ee117bedd26 |\n| datafiles/data_structure_files/data_structure_ANM219036.tar.gz | 146b101d61fa9628cd3da54f279664c4 |\n| datafiles/data_structure_files/data_structure_ANM219037.tar.gz | 73f788942ec903eebd048001b2f4db6f |\n| datafiles/data_structure_files/data_structure_ANM219038.tar.gz | 5aca92550f1707fa5c0a82fe80b2ab4f |\n| datafiles/data_structure_files/data_structure_ANM219247.tar.gz | 234db2241f25af06233ad58fcf101c73 |\n| datafiles/data_structure_files/data_structure_ANM219248.tar.gz | e2cae036a2b333cb3a06eeb691093468 |\n| datafiles/data_structure_files/data_structure_ANM219253.tar.gz | 4f118c0085d3011a7ff6d0f35f298bf9 |\n| datafiles/data_structure_files/data_structure_ANM221977.tar.gz | 44ceb341033227f98693e39c7103527a |\n\nThe session files (MATLAB \"data structure\" files, one tar.gz per animal) are used. The same\nsessions are also in NWB 1.0 files, which lack the photostimulation type, the AOM and laser\npower traces and the `GoodTrials` flag, so they are not used. The raw voltage traces\n(about 800 GB) are not read. The data set also holds the authors' MATLAB scripts that\n\"reproduce the figures\" and their compiled output (`ALM_compiled_all_data.mat`); the output is\nnot read. The scripts are cited below where the paper leaves a detail open.\n\n**What the data set holds.** The electrophysiology of Figures 2 and 3 and Extended Data\nFigures 1, 2 and 5: 99 sessions from 19 mice, 1,408 units with cell type labels, trial types,\nepoch times, photostimulation type per trial, and the lick, AOM and laser power traces. The\nphotoinhibition and photoactivation behaviour (Figs 1 and 5, ED Figs 3 and 6), the imaging\n(Fig. 4), the anatomy (ED Fig. 3) and the recordings with somatic PT photoactivation (ED Fig. 7)\nare not in it.\n\n| claim | tested |\n|---|---|\n| fig1d-photoinhibition-ipsilateral-bias | blocked, data missing |\n| fig1d-sample-epoch-smaller-bias | blocked, data missing |\n| task-performance | tested, on the 19 electrophysiology mice |\n| unit-counts | tested |\n| fig2-selective-fraction | tested |\n| fig2d-response-categories | tested |\n| fig2c-selectivity-time-course | tested |\n| fig2c-dynamic-single-neurons | tested |\n| ed2-error-trials-predict-choice | tested |\n| fig2e-equal-contra-ipsi | tested |\n| ed1-no-population-contra-bias | tested |\n| ed1-fast-spiking-properties | tested |\n| tagging-counts | tested |\n| antidromic-latency-jitter | tested |\n| ed5g-it-second-pulse-jitter | tested |\n| fig3ei-both-types-preparatory-and-movement | tested |\n| fig3fj-contra-preferring-pt-not-it | tested |\n| fig3f-late-contra-selectivity-pt | tested |\n| reaction-time | tested |\n| fig4-imaging-intermingled | blocked, data missing |\n| fig4h-imaging-pt-contra-bias | blocked, data missing |\n| imaging-overall-counts | blocked, data missing |\n| contra-ipsi-selectivity-forms | tested |\n| fig5-pt-activation-contralateral-bias | blocked, data missing |\n| ed6b-pt-dose-response | blocked, data missing |\n| ed6d-it-activation-inconsistent | blocked, data missing |\n| ed3-high-power-contralateral-licking | blocked, data missing |\n| ed3d-non-overlapping-it-pt | blocked, data missing |\n| ed7-pt-stimulation-persistent-activity | blocked, data missing |\n\nLick right trials are contralateral to the recorded left ALM. \"R\" and \"L\" below are lick right\nand lick left trials. Loading streams about 14 GB and takes about four minutes.\n#%% code\nimport time\nimport warnings\nfrom collections import Counter\n\nimport fsspec\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport alm\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nS = alm.load_all(workers=4)\nmeta = alm.load_meta()\nprint(f\"{alm.DATASET} ({alm.VERSION}, doi:{alm.DATASET_DOI}): {len(S)} sessions streamed in {time.time() - started:.0f} s\")\n#%% md\n## Data check\n#%% code tags=sanity\nwith fsspec.open(alm.BASE + \"checksums.md5\", \"rt\") as fh:\n    md5 = dict(line.split()[::-1] for line in fh if line.strip())\nread = [\"datafiles/meta_data_files.tar.gz\"] + [f\"datafiles/data_structure_files/data_structure_{a}.tar.gz\" for a in alm.ANIMALS]\nprint(\"MD5 sums on the bucket now (compare with the header):\")\nfor f in read:\n    print(f\"  {md5.get(f)}  {f}\")\n\nT = pd.concat([s[\"trials\"] for s in S], ignore_index=True)\nunits = [(s, u) for s in S for u in s[\"units\"]]\nmeta[\"animal\"] = meta.session.str[:9]\ngeno = meta.groupby(\"animal\").agg(strain=(\"strain\", \"first\"), gene=(\"gene\", \"first\"), sessions=(\"session\", \"size\"),\n                                  photostim_location=(\"photostim_location\", \"first\"))\nper_animal = pd.DataFrame({\n    \"sessions\": pd.Series(Counter(s[\"animal\"] for s in S)),\n    \"units\": pd.Series(Counter(s[\"animal\"] for s, u in units)),\n    \"trials\": T.groupby(\"animal\").size()})\nprint(per_animal.join(geno[[\"strain\", \"gene\", \"photostim_location\"]]).to_string())\nprint(f\"\\nAnimals {len(per_animal)}, sessions {len(S)}, units {len(units)} (data description: 19 animals, 99 sessions, 1,408 units)\")\nprint(\"Meta data files:\", len(meta), \"; sessions with a meta data file:\", len(set(meta.session) & {s['session'] for s in S}))\nprint(\"Strains (paper, Methods: 9 Sim1_KJ18-Cre, 3 Rbp4-Cre, 4 Tlx_PL56-Cre injected; 1 Sim1 x Ai32, 2 Tlx x Ai32):\")\nprint(geno.groupby([\"strain\", \"gene\"]).size().to_string())\n#%% code tags=sanity\nprint(\"Trials:\", len(T))\nprint(\"\\nPhotostimulationType (description: 0 none, 1 PT axonal, 2 IT axonal, NaN do not analyse):\")\nprint(T.ptype.value_counts(dropna=False).sort_index().to_string())\nprint(\"\\nGoodTrials:\", T.good.value_counts().to_dict())\nT[\"has_light\"] = T.aom_max > alm.AOM_MIN\nprint(\"\\nLight pulses by photostimulation type (per trial medians):\")\nprint(T.groupby(T.ptype.fillna(-1)).agg(trials=(\"has_light\", \"size\"), with_light=(\"has_light\", \"sum\"),\n      pulses=(\"n_pulses\", \"median\"), pulse_ms=(\"pulse_ms\", \"median\"), power_mW=(\"power_max\", \"median\"),\n      first_onset_s=(\"stim_on\", \"median\")).rename_axis(\"ptype (-1 = NaN)\").round(2).to_string())\nbad0 = T[(T.ptype == 0) & T.has_light]\nprint(\"\\nTrials of type 0 (no stimulation) with light pulses:\", len(bad0), \"in sessions\", bad0.session.value_counts().to_dict())\nprint(\"StimTrials flag against PhotostimulationType:\")\nprint(pd.crosstab(T.StimTrials, T.ptype.fillna(-1)).to_string())\n#%% code tags=sanity\ng = T[(T.good == 1) & T.cue.notna()]\nep = pd.DataFrame({\"sample_s\": g.pole_out - g.pole_in, \"delay_s\": g.cue - g.pole_out, \"pole_in_s\": g.pole_in, \"cue_s\": g.cue,\n                   \"timeseries_start_s\": g.ts_offset, \"timeseries_len_s\": g.ts_len})\nprint(\"Epoch times in performing trials (seconds; Methods: sample 1.3 s to 0.1 s after pole retraction onset, delay 1.3 s):\")\nprint(ep.describe(percentiles=[0.01, 0.5, 0.99]).round(3).to_string())\noutcome = g[[\"HitR\", \"HitL\", \"ErrR\", \"ErrL\", \"NoLickR\", \"NoLickL\"]].sum(axis=1)\nprint(\"\\nPerforming trials with exactly one outcome flag:\", int((outcome == 1).sum()), \"of\", len(g), \"; lick early:\", int(g.LickEarly.sum()))\nprint(\"Trial type counts in performing trials:\", g[alm.TRIAL_TYPES].sum().to_dict())\n#%% md\nTwo things in the trial tables are not in the description. Photostimulation types 3, 4 and 5\noccur in the two Tlx_PL56-Cre x Ai32 mice: eight 1 ms pulses at about 23 mW starting 1.8, 2.3\nor 2.8 s into the trial; the description lists only 0, 1, 2 and NaN. The authors' compile\nscript counts types 1 to 5 as tagging trials. And in one session of ANM210862 some trials of\ntype 0 (\"non-stimulation\") carry light pulses (counts above). Trials of type 0 with light\nare kept as the data label them, as the paper's analysis would have; how many enter is printed.\nThe epoch lengths fit the Methods' 1.3 s sample and delay epochs.\n#%% code tags=sanity\n# Units: labels, widths, spikes, and recordings deposited twice.\nlab = Counter(u[\"cell_types\"] for s, u in units)\nprint(\"cellType labels:\", dict(lab))\nwidth = np.array([alm.spike_width_ms(u[\"waveform\"]) for s, u in units])\nprint(\"Trough-to-peak widths take the values (ms):\", np.unique(np.round(width, 3)).tolist(),\n      \"; sampling interval\", round(1e3 / alm.FS_WAVEFORM, 4), \"ms\")\nnsp = np.array([u[\"n_spikes\"] for s, u in units])\nprint(\"Spikes per unit: min\", nsp.min(), \"median\", int(np.median(nsp)), \"max\", nsp.max())\nunsorted = sum(int(np.any(np.diff(u[\"spike_t_session\"]) < 0)) for s, u in units)\nprint(\"Units whose spike times are not sorted:\", unsorted)\nsig = {}\nfor s, u in units:\n    key = (len(u[\"spike_t_session\"]), round(float(u[\"spike_t_session\"][:20].sum()), 6) if len(u[\"spike_t_session\"]) else 0)\n    sig.setdefault(key, []).append(f\"{s['session']}/{u['unit']}\")\ndups = [v for v in sig.values() if len(v) > 1]\nprint(\"Units with identical spike trains (count and first 20 times):\", dups)\nsess_sig = Counter((len(s[\"trials\"]), round(float(s[\"trials\"].start.sum()), 3)) for s in S)\nprint(\"Sessions with identical trial start times:\", [k for k, v in sess_sig.items() if v > 1])\nprint(\"Mean waveform amplitude range (V):\", np.round(np.percentile([np.ptp(u['waveform']) for s, u in units], [0, 50, 100]), 6).tolist())\n#%% md\nThe labels give 1,173 pyramidal, 45 pyramidal and PT, 27 pyramidal and IT, 124 FS and 39 units\nwithout a label: 1,245 pyramidal in all, as the paper says. Waveforms are sampled every\n0.0512 ms, so trough-to-peak widths come in steps of that size; the claim on unit counts\ncompares both the labels and widths recomputed from the waveforms.\n\nClocks. Three checks show the streams share the trial clock. Spikes and trial times: the\nnumber of pyramidal neurons that distinguish lick right from lick left trials, in 200 ms\nwindows, is near the 5% expected by chance before the sample epoch and rises after it (claim\nfig2c-selectivity-time-course, printed there with the same count when the trial labels are\nshuffled). Spikes and the AOM trace: antidromic spikes follow the light pulses at a fixed\nlatency, with a jitter near 0.1 ms (claim antidromic-latency-jitter). Lick trace and cue: the\nfirst movement of the lick trace follows the cue by a narrow interval (claim reaction-time),\nand the lick trace's movement is concentrated after the cue (printed next).\n#%% code tags=sanity\ngc = T[(T.good == 1) & (T.ptype == 0) & (T.HitR | T.HitL) & ~T.LickEarly]\nprint(\"Correct non-stimulation trials without early licks:\", len(gc))\nprint(\"Fraction with a lick trace onset in the 1 s after the cue (reading 0.25):\", round(gc[\"rt_0.25\"].notna().mean(), 3))\nprint(\"Onset after the cue, percentiles 5, 25, 50, 75, 95 (ms):\", np.round(np.nanpercentile(gc[\"rt_0.25\"] * 1e3, [5, 25, 50, 75, 95]), 1).tolist())\nprint(\"Licks (crossings of 1 V) between sample onset and cue in correct non-lick-early trials, mean per trial:\",\n      round(gc.n_lick_pre.mean(), 3), \"; in lick early trials:\", round(T[(T.good == 1) & T.LickEarly].n_lick_pre.mean(), 3))\nprint(\"Per session median lick trace baseline (V), range:\", np.round(gc.groupby('session').lick_base.median().agg(['min', 'max']).values, 2).tolist(),\n      \"; median peak excursion after the cue (V), range:\", np.round(gc.groupby('session').lick_peak.median().agg(['min', 'max']).values, 2).tolist())\n#%% code\n# Unit tables under the readings of the shared methods: lick early trials dropped (a) or\n# kept (b); response epoch 1.3 s (a) or 1.5 s (b).\nUT = {}\nfor le in (\"drop\", \"keep\"):\n    for resp in (1.3, 1.5):\n        UT[(le, resp)] = alm.unit_table(S, lick_early=le, response_s=resp)\nD = UT[(\"drop\", 1.3)]\npyr = D[D.label == \"pyramidal\"]\nprint(\"Units:\", len(D), \"; pyramidal:\", len(pyr))\nprint(\"Correct trials per pyramidal neuron (drop lick early), R:\", pyr.n_R.describe()[[\"min\", \"50%\", \"max\"]].to_dict(),\n      \"L:\", pyr.n_L.describe()[[\"min\", \"50%\", \"max\"]].to_dict())\nprint(\"Pyramidal neurons with fewer than 2 trials of a type (no test):\", int(((pyr.n_R < 2) | (pyr.n_L < 2)).sum()))\nprint(\"Trials of type 0 with light used by any unit:\", int(((T.ptype == 0) & T.has_light & (T.good == 1) & (T.HitR | T.HitL)).sum()))\n#%% md\n## task-performance\n\n> Mice performed the task at 78.4% correct on average, with responses before the go cue on\n> fewer than 13% of trials (n = 42 mice).\n\nOnly the 19 electrophysiology mice are in the data set, against 42 in the paper. Per cent\ncorrect is hits over hits and errors, lick early trials excluded (Methods); no-lick trials are\nleft out, as the data set's `Demo_get_performance.m` does. Lick early fraction is over all\nperforming trials of the same set. Readings from the criterion: mean over sessions (a), over\nmice (b), pooled trials (c); control trials (type 0, no StimTrials flag) or all performing trials.\n#%% code tags=claim:task-performance\nrows = []\nfor trials_name, sel in ((\"control\", (T.ptype == 0) & ~T.StimTrials), (\"all\", T.ptype.notna() | T.ptype.isna())):\n    d = T[(T.good == 1) & sel & T.cue.notna()]\n    d = d.assign(hit=d.HitR | d.HitL, resp=d.HitR | d.HitL | d.ErrR | d.ErrL)\n    ne = d[~d.LickEarly & d.resp]\n    ps = ne.groupby(\"session\").hit.mean() * 100\n    le_s = d.groupby(\"session\").LickEarly.mean() * 100\n    pm = ne.groupby(\"animal\").hit.mean() * 100\n    le_m = d.groupby(\"animal\").LickEarly.mean() * 100\n    for how, pc, le in ((\"a sessions\", ps.mean(), le_s.mean()), (\"b mice\", ne.assign(s=ne.session).groupby(\"animal\").apply(lambda x: x.groupby(\"session\").hit.mean().mean()).mean() * 100, d.groupby(\"animal\").apply(lambda x: x.groupby(\"session\").LickEarly.mean().mean()).mean() * 100),\n                        (\"c pooled\", ne.hit.mean() * 100, d.LickEarly.mean() * 100)):\n        rows.append({\"trials\": trials_name, \"mean\": how, \"per_cent_correct\": pc, \"lick_early_pct\": le,\n                     \"within_tolerance\": abs(pc - 78.4) <= 7.84, \"lick_early_below_14.3\": le < 14.3, \"n_trials\": len(d)})\nperf = pd.DataFrame(rows)\nprint(perf.round(2).to_string(index=False))\nprint(\"\\nPer mouse (control trials):\")\nd = T[(T.good == 1) & (T.ptype == 0) & ~T.StimTrials & T.cue.notna()]\nprint(pd.DataFrame({\"pct_correct\": d[~d.LickEarly & (d.HitR | d.HitL | d.ErrR | d.ErrL)].groupby(\"animal\").apply(lambda x: (x.HitR | x.HitL).mean() * 100),\n                    \"lick_early_pct\": d.groupby(\"animal\").LickEarly.mean() * 100}).round(1).T.to_string())\n#%% md\n## unit-counts\n\n> 1,408 single units were recorded in left ALM from 19 mice in 99 sessions; by spike width,\n> 1,245 are putative pyramidal neurons (> 0.45 ms), 124 fast-spiking neurons (< 0.35 ms) and 39\n> intermediate units excluded.\n#%% code tags=claim:unit-counts\nprint(\"From the cellType labels: units\", len(D), \"; pyramidal\", int((D.label == \"pyramidal\").sum()),\n      \"; FS\", int((D.label == \"FS\").sum()), \"; unlabelled\", int((D.label == \"unclassified\").sum()))\nw = D.width_ms\nprint(\"From the trough-to-peak width of the mean waveform (sampled at 19531.25 Hz): >0.45 ms\", int((w > 0.45).sum()),\n      \"; <0.35 ms\", int((w < 0.35).sum()), \"; 0.35 to 0.45 ms\", int(((w >= 0.35) & (w <= 0.45)).sum()))\nprint(pd.crosstab(D.label, pd.cut(w, [0, 0.35, 0.45, 2], labels=[\"<0.35\", \"0.35-0.45\", \">0.45\"])).to_string())\n# variant: the width on a waveform interpolated to 1 us (cubic spline)\nfrom scipy.interpolate import CubicSpline\ndef width_interp(wf):\n    x = np.arange(len(wf)) / alm.FS_WAVEFORM * 1e3\n    xs = np.arange(0, x[-1], 0.001)\n    ys = CubicSpline(x, wf)(xs)\n    i = int(np.argmin(ys)); j = i + int(np.argmax(ys[i:]))\n    return xs[j] - xs[i]\nwi = np.array([width_interp(u[\"waveform\"]) for s, u in units])\nprint(\"Variant, spline-interpolated widths: >0.45 ms\", int((wi > 0.45).sum()), \"; <0.35 ms\", int((wi < 0.35).sum()),\n      \"; 0.35 to 0.45 ms\", int(((wi >= 0.35) & (wi <= 0.45)).sum()))\nprint(pd.crosstab(D.label.values, pd.cut(wi, [0, 0.35, 0.45, 2], labels=[\"<0.35\", \"0.35-0.45\", \">0.45\"])).to_string())\nprint(\"Mice:\", D.animal.nunique(), \"; sessions:\", D.session.nunique())\nprint(\"Units per mouse:\", D.groupby(\"animal\").size().to_dict())\n#%% md\n## fig2-selective-fraction\n\n> 73% (912 of 1,245) of putative pyramidal neurons distinguish the trial types in at least one\n> epoch.\n\nTwo-tailed t-test (pooled variance) of spike rates on lick right against lick left correct\ntrials, in the sample, delay or response epoch, P < 0.05 uncorrected (Methods). Under each\nreading of the response epoch and of lick early trials; Welch's test as a variant.\n#%% code tags=claim:fig2-selective-fraction\nrows = []\nfor (le, resp), d in UT.items():\n    p = d[d.label == \"pyramidal\"]\n    for test, col in ((\"pooled\", \"selective\"), (\"Welch\", \"selective_welch\")):\n        rows.append({\"lick_early\": le, \"response_s\": resp, \"test\": test, \"selective\": int(p[col].sum()),\n                     \"of\": len(p), \"fraction\": p[col].mean()})\nsel_tab = pd.DataFrame(rows)\nsel_tab[\"within_tolerance\"] = (abs(sel_tab.selective - 912) <= 91.2) & (abs(sel_tab.fraction - 0.73) <= 0.073)\nprint(sel_tab.round(4).to_string(index=False))\nprint(\"\\nPer mouse (reading a, a, pooled): fraction selective\")\nprint(pyr.groupby(\"animal\").selective.agg([\"sum\", \"size\", \"mean\"]).round(3).T.to_string())\nprint(\"Per epoch, pyramidal neurons significant: sample\", int((pyr.p_sample < .05).sum()), \"delay\", int((pyr.p_delay < .05).sum()),\n      \"response\", int((pyr.p_response < .05).sum()), \"; chance at P < 0.05 for one epoch is about\", round(0.05 * len(pyr)))\n#%% md\n## fig2d-response-categories\n\n> Of the selective neurons, 219 have selectivity only in the sample or delay epochs (preparatory\n> only), and the rest have peri-movement selectivity in the response epoch, alone or together\n> with preparatory selectivity (389 and 304 of 912).\n#%% code tags=claim:fig2d-response-categories\nrows = []\nfor (le, resp), d in UT.items():\n    c = alm.categories(d[d.label == \"pyramidal\"])\n    rows.append({\"lick_early\": le, \"response_s\": resp, **c})\ncat = pd.DataFrame(rows)\ncat[\"text_reading_ok\"] = (abs(cat.prep_only - 219) <= 21.9) & (abs(cat.peri_only - 389) <= 38.9) & (abs(cat.both - 304) <= 30.4)\ncat[\"figure_reading_ok\"] = (abs(cat.prep_only - 219) <= 21.9) & (abs(cat.both - 389) <= 38.9) & (abs(cat.peri_only - 304) <= 30.4)\nfor k in (\"prep_only\", \"both\", \"peri_only\"):\n    cat[f\"frac_{k}\"] = (cat[k] / cat.n).round(3)\nprint(cat.to_string(index=False))\nprint(\"\\nPaper, as fractions of 912: preparatory only\", round(219 / 912, 3), \"; 389/912 =\", round(389 / 912, 3), \"; 304/912 =\", round(304 / 912, 3))\nprint(\"Per mouse (reading a, a):\")\nprint(pyr[pyr.selective].groupby(\"animal\").apply(lambda x: pd.Series(alm.categories(x.assign(selective=True)))).T.to_string())\n#%% md\n## fig2c-selectivity-time-course\n\n> Selectivity emerges in the sample epoch, increases through the delay epoch and is largest at\n> the beginning of the response epoch.\n\nMeasure 1 (ED Fig. 1f): the number of pyramidal neurons significant (two-tailed t-test on spike\ncounts, P < 0.05) in 200 ms windows, stepped by 10 ms. Measure 2 (Fig. 2c): the population\nselectivity of the selective neurons, preferred minus non-preferred rate, with the preference\nset from 10 random trials of each type (by spike count from sample onset to the end of the\nresponse epoch, as the data set's compile script does) and the rate difference taken on the\nremaining trials. Neurons need at least 11 trials of each type for the split; the data set's\nscript requires more than 15, a variant. The epoch boundaries relative to the cue are the\nmedians over trials. Seeds are fixed.\n#%% code tags=claim:fig2c-selectivity-time-course\nrng = np.random.default_rng(20150305)\nt_sample = -float(np.median(g.cue - g.pole_in))\nt_delay = -float(np.median(g.cue - g.pole_out))\nprint(f\"Median sample onset {t_sample:.3f} s and delay onset {t_delay:.3f} s relative to the cue\")\ncnt_sig, cnt_sig_shuf, popsel, popsel15, n_pop = None, None, [], [], 0\nsel_keys = set(map(tuple, pyr[pyr.selective][[\"session\", \"unit\"]].values))\nfor s, u in units:\n    if (D.label.values[0] is None):\n        pass\nfor s, u in units:\n    key = (s[\"session\"], u[\"unit\"])\n    if key not in set(map(tuple, pyr[[\"session\", \"unit\"]].values)):\n        continue\n    tr = s[\"trials\"]\n    r, l = alm.trial_mask(tr, u)\n    if r.sum() < 2 or l.sum() < 2:\n        continue\n    br, bl = alm.cue_binned(u, tr, r), alm.cue_binned(u, tr, l)\n    wr, centers = alm.window_sums(br)\n    wl, _ = alm.window_sums(bl)\n    p = stats.ttest_ind(wr, wl, axis=0).pvalue\n    p = np.where(np.isnan(p), 1, p)\n    allw = np.vstack([wr, wl])\n    perm = rng.permutation(len(allw))\n    ps = stats.ttest_ind(allw[perm[:len(wr)]], allw[perm[len(wr):]], axis=0).pvalue\n    ps = np.where(np.isnan(ps), 1, ps)\n    cnt_sig = (p < 0.05).astype(int) if cnt_sig is None else cnt_sig + (p < 0.05)\n    cnt_sig_shuf = (ps < 0.05).astype(int) if cnt_sig_shuf is None else cnt_sig_shuf + (ps < 0.05)\n    if key in sel_keys and r.sum() >= 11 and l.sum() >= 11:\n        ir, il = rng.permutation(r.sum()), rng.permutation(l.sum())\n        whole = lambda b: b[:, (alm.CUE_EDGES[:-1] >= t_sample) & (alm.CUE_EDGES[:-1] < alm.RESPONSE_S)].sum(axis=1)\n        pref_r = whole(br)[ir[:10]].mean() >= whole(bl)[il[:10]].mean()\n        diff = (wr[ir[10:]].mean(axis=0) - wl[il[10:]].mean(axis=0)) / alm.WIN_S\n        popsel.append(diff if pref_r else -diff)\n        if r.sum() > 15 and l.sum() > 15:\n            popsel15.append(popsel[-1])\npopsel, popsel15 = np.array(popsel), np.array(popsel15)\nprint(\"Neurons in measure 1:\", None if cnt_sig is None else \"pyramidal with >= 2 trials of each type\",\n      \"; in measure 2:\", len(popsel), \"(>15 trials each:\", len(popsel15), \")\")\n\ndef at(x, t):\n    return float(x[np.argmin(np.abs(centers - t))])\n\ndef check(x, name):\n    rng_t = (centers >= -3.4) & (centers <= 1.9)\n    tmax = float(centers[rng_t][np.argmax(x[rng_t])])\n    v = {\"measure\": name, \"pre_sample\": at(x, t_sample - 0.1), \"sample_end\": at(x, t_delay - 0.1),\n         \"delay_start\": at(x, t_delay + 0.1), \"delay_end\": at(x, -0.1), \"max_value\": float(x[rng_t].max()), \"t_max_s\": tmax}\n    v[\"emerges\"] = v[\"sample_end\"] > v[\"pre_sample\"]\n    v[\"increases_in_delay\"] = v[\"delay_end\"] > v[\"delay_start\"]\n    v[\"max_within_0.5s\"] = 0 < tmax <= 0.5\n    v[\"max_within_0.2s\"] = 0 < tmax <= 0.2\n    return v\n\nres = pd.DataFrame([check(cnt_sig.astype(float), \"1 significant neurons\"), check(popsel.mean(axis=0), \"2 population selectivity\"),\n                    check(popsel15.mean(axis=0), \"2 variant, >15 trials\")])\nprint(res.round(3).to_string(index=False))\nprint(\"\\nShuffled labels, significant neurons: median\", int(np.median(cnt_sig_shuf)), \"max\", int(cnt_sig_shuf.max()),\n      \"; true labels before sample onset (window centred 0.1 s before):\", int(at(cnt_sig, t_sample - 0.1)),\n      \"; 5% of the neurons tested:\", round(0.05 * len(pyr)))\nfig, ax = plt.subplots(1, 2, figsize=(11, 3.2))\nax[0].plot(centers, cnt_sig, \"k\"); ax[0].plot(centers, cnt_sig_shuf, color=\"0.6\")\nax[1].plot(centers, popsel.mean(axis=0), \"k\")\nfor a in ax:\n    for x in (t_sample, t_delay, 0):\n        a.axvline(x, color=\"0.7\", ls=\":\")\n    a.set_xlabel(\"time from cue (s)\")\nax[0].set_ylabel(\"significant neurons\"); ax[1].set_ylabel(\"pref - nonpref (spikes/s)\")\nplt.tight_layout(); plt.show()\nprint(\"Plotted ranges: significant neurons\", int(cnt_sig.min()), \"to\", int(cnt_sig.max()), \"; population selectivity\",\n      round(float(popsel.mean(axis=0).min()), 2), \"to\", round(float(popsel.mean(axis=0).max()), 2), \"spikes/s\")\n#%% md\n## fig2c-dynamic-single-neurons\n\n> Individual neuron responses are dynamic while selectivity at the population level is stable.\n\nPopulation response correlation (Methods): for the selective neurons, each neuron's\ncue-aligned rate (200 ms window, 10 ms step, correct trials) is mean-subtracted and divided by\nthe variance of its response across the trial (as the Methods say; the data set's script does\nthe same; division by the s.d. is a variant). Pearson's r between the population vector at each\ntime and at the cue. Readings (a) the vector of selectivities (R minus L) and (b) the R and L\nrates concatenated. The population selectivity is measure 2 of the previous claim.\n#%% code tags=claim:fig2c-dynamic-single-neurons\nPR, PL = [], []\nfor s, u in units:\n    if (s[\"session\"], u[\"unit\"]) not in sel_keys:\n        continue\n    tr = s[\"trials\"]\n    r, l = alm.trial_mask(tr, u)\n    if r.sum() < 2 or l.sum() < 2:\n        continue\n    PR.append(alm.window_sums(alm.cue_binned(u, tr, r))[0].mean(axis=0) / alm.WIN_S)\n    PL.append(alm.window_sums(alm.cue_binned(u, tr, l))[0].mean(axis=0) / alm.WIN_S)\nPR, PL = np.array(PR), np.array(PL)\nspan = (centers >= -3.4) & (centers <= 1.9)\ndef norm(x, how):\n    x = x[:, span]\n    x = x - x.mean(axis=1, keepdims=True)\n    d = x.var(axis=1, keepdims=True) if how == \"var\" else x.std(axis=1, keepdims=True)\n    return x / np.where(d == 0, np.nan, d)\ncs = centers[span]\ni0 = np.argmin(np.abs(cs))\nwin_early = (cs >= t_sample) & (cs <= t_delay + 0.5)\nrows, curves = [], {}\nfor how in (\"var\", \"sd\"):\n    nr, nl = norm(PR, how), norm(PL, how)\n    for reading, M in ((\"a selectivity\", nr - nl), (\"b concatenated\", np.vstack([nr, nl]))):\n        ok = ~np.isnan(M).any(axis=1)\n        M = M[ok]\n        rc = np.array([np.corrcoef(M[:, j], M[:, i0])[0, 1] for j in range(M.shape[1])])\n        curves[(how, reading)] = rc\n        rows.append({\"normalised_by\": how, \"reading\": reading, \"neurons_rows\": int(ok.sum()),\n                     \"mean_r_sample_to_delay+0.5\": rc[win_early].mean(), \"max_r_in_that_window\": rc[win_early].max(),\n                     \"r_at_delay_end_-0.1s\": rc[np.argmin(np.abs(cs + 0.1))]})\ndyn = pd.DataFrame(rows)\ndyn[\"below_0.5\"] = dyn[\"mean_r_sample_to_delay+0.5\"] < 0.5\nprint(dyn.round(3).to_string(index=False))\nps_curve = popsel.mean(axis=0)\nstable = (centers >= t_delay - 0.1) & (centers <= -0.1)\nprint(\"\\nPopulation selectivity from the end of the sample epoch through the delay: min\", round(float(ps_curve[stable].min()), 3),\n      \"spikes/s; all above 0:\", bool((ps_curve[stable] > 0).all()))\n#%% md\n## ed2-error-trials-predict-choice\n\n> On error trials, when mice lick opposite to the instructed direction, ALM activity predicts\n> the licking direction; most selective neurons switch their trial type preference.\n\nError trials are labelled by the instructed side (ErrR: pole for lick right, mouse licked\nleft). Per selective pyramidal neuron and epoch, correct selectivity R minus L and error\nselectivity ErrR minus ErrL. Readings: at least 1 or at least 5 error trials of each type; the\ndata set's script uses more than 10 correct and more than 5 error trials of each type (variant).\n#%% code tags=claim:ed2-error-trials-predict-choice\nrows = []\nsp = pyr[pyr.selective]\nfor name, m in ((\"min 1 error each\", (sp.n_errR >= 1) & (sp.n_errL >= 1)), (\"min 5 error each\", (sp.n_errR >= 5) & (sp.n_errL >= 5)),\n                (\"script: >10 correct, >5 error\", (sp.n_R > 10) & (sp.n_L > 10) & (sp.n_errR > 5) & (sp.n_errL > 5))):\n    d = sp[m]\n    for e in (\"sample\", \"delay\", \"response\"):\n        c = d[f\"{e}_R\"] - d[f\"{e}_L\"]\n        er = d[f\"{e}_errR\"] - d[f\"{e}_errL\"]\n        r, p = stats.pearsonr(c, er)\n        nz = (c != 0) & (er != 0)\n        rows.append({\"reading\": name, \"epoch\": e, \"neurons\": len(d), \"r\": r, \"p\": p,\n                     \"fraction_switched\": float((np.sign(c[nz]) != np.sign(er[nz])).mean()), \"n_nonzero\": int(nz.sum())})\nerr = pd.DataFrame(rows)\nerr[\"holds\"] = (err.r < 0) & (err.p < 0.05) & (err.fraction_switched > 0.5)\nprint(err.round(4).to_string(index=False))\nprint(\"\\nSelective pyramidal neurons without error trials of both types:\", int(((sp.n_errR < 1) | (sp.n_errL < 1)).sum()), \"of\", len(sp))\n#%% md\n## fig2e-equal-contra-ipsi\n\n> Among selective putative pyramidal neurons, contra-preferring and ipsi-preferring neurons are\n> present in equal proportions (427 contra-preferring and 485 ipsi-preferring in Fig. 2c).\n\nPreference from the spike rates from sample onset to the end of the response epoch, R against\nL (reading a, all correct trials; Methods), or from the 10-trial split of the previous claims\n(reading b). The test is the Methods' bootstrap over neurons, one-tailed, 10^4 resamples.\n#%% code tags=claim:fig2e-equal-contra-ipsi\nrng = np.random.default_rng(2)\nsp = pyr[pyr.selective]\nca = sp.contra.values\npb = popsel  # sign convention: the 10-trial split's preference is in the sign of R-L on held-out trials below\nrows = [{\"reading\": \"a total counts\", \"contra\": int(ca.sum()), \"ipsi\": int((~ca).sum()), \"fraction_contra\": ca.mean(),\n         \"P_more_contra\": alm.bootstrap_more_ipsi(ca, rng=rng)}]\n# reading b: preference from 10 random trials of each type\nrng_b = np.random.default_rng(3)\ncb = []\nfor s, u in units:\n    if (s[\"session\"], u[\"unit\"]) not in sel_keys:\n        continue\n    tr = s[\"trials\"]\n    r, l = alm.trial_mask(tr, u)\n    if r.sum() < 11 or l.sum() < 11:\n        continue\n    a, b = alm.epoch_bounds(tr)[\"trial\"]\n    cr, cl = alm.counts_in(u, tr, r, a, b), alm.counts_in(u, tr, l, a, b)\n    cb.append(cr[rng_b.permutation(len(cr))[:10]].mean() > cl[rng_b.permutation(len(cl))[:10]].mean())\ncb = np.array(cb)\nrows.append({\"reading\": \"b 10-trial split\", \"contra\": int(cb.sum()), \"ipsi\": int((~cb).sum()), \"fraction_contra\": cb.mean(),\n             \"P_more_contra\": alm.bootstrap_more_ipsi(cb, rng=rng)})\npref = pd.DataFrame(rows)\npref[\"counts_ok\"] = (abs(pref.contra - 427) <= 42.7) & (abs(pref.ipsi - 485) <= 48.5)\npref[\"no_more_contra\"] = pref.P_more_contra >= 0.05\nprint(pref.round(4).to_string(index=False))\nprint(\"\\nPer mouse, reading a, fraction contra-preferring:\", sp.groupby(\"animal\").contra.mean().round(2).to_dict())\nprint(\"Binomial test against 0.5 (variant), reading a: p =\", round(stats.binomtest(int(ca.sum()), len(ca)).pvalue, 4))\n#%% md\n## ed1-no-population-contra-bias\n\n> The overall spike count of the recorded population shows no significant contralateral bias\n> (P = 0.13, two-tailed t-test against 0).\n\nPer neuron, the difference between its mean spike rate on R and L trials from sample onset to\nthe end of the response epoch; two-tailed one-sample t-test against 0. Readings (a) selective\npyramidal neurons, (b) all pyramidal neurons, (c) all units.\n#%% code tags=claim:ed1-no-population-contra-bias\nrows = []\nfor name, d in ((\"a selective pyramidal\", pyr[pyr.selective]), (\"b all pyramidal\", pyr), (\"c all units\", D)):\n    x = (d.trial_R - d.trial_L).dropna()\n    t_, p_ = stats.ttest_1samp(x, 0)\n    rows.append({\"reading\": name, \"neurons\": len(x), \"mean_R_minus_L_spk_s\": x.mean(), \"median\": x.median(), \"t\": t_, \"p\": p_})\nbias = pd.DataFrame(rows)\nbias[\"significant\"] = bias.p < 0.05\nprint(bias.round(4).to_string(index=False))\nfor le_resp in [(\"keep\", 1.3), (\"drop\", 1.5)]:\n    d = UT[le_resp]; x = (d[d.label == \"pyramidal\"].trial_R - d[d.label == \"pyramidal\"].trial_L).dropna()\n    print(\"Variant\", le_resp, \"all pyramidal: mean\", round(x.mean(), 3), \"p\", round(stats.ttest_1samp(x, 0).pvalue, 4))\n#%% md\n## ed1-fast-spiking-properties\n\n> Fast-spiking neurons have higher baseline firing rates and are less selective than putative\n> pyramidal neurons.\n\nBaseline readings: (a) the rate before sample onset (from the start of the trial), (b) the\n0.5 s before sample onset; the average of the R and L trial means. Selectivity readings: (a)\nthe fraction selective by the shared test, (b) the absolute rate difference over the three\nepochs.\n#%% code tags=claim:ed1-fast-spiking-properties\nfs = D[D.label == \"FS\"]\nrows = []\nfor name, col in ((\"a whole pre-sample\", \"pre_all\"), (\"b 0.5 s pre-sample\", \"pre\")):\n    bf, bp = (fs[f\"{col}_R\"] + fs[f\"{col}_L\"]) / 2, (pyr[f\"{col}_R\"] + pyr[f\"{col}_L\"]) / 2\n    rows.append({\"measure\": \"baseline \" + name, \"FS_mean\": bf.mean(), \"pyr_mean\": bp.mean(), \"FS_median\": bf.median(),\n                 \"pyr_median\": bp.median(), \"FS_higher\": bf.mean() > bp.mean() and bf.median() > bp.median(),\n                 \"ranksum_p\": stats.mannwhitneyu(bf.dropna(), bp.dropna()).pvalue})\nrows.append({\"measure\": \"selectivity a fraction selective\", \"FS_mean\": fs.selective.mean(), \"pyr_mean\": pyr.selective.mean(),\n             \"FS_less_selective\": fs.selective.mean() < pyr.selective.mean()})\naf, ap = (fs.trial_R - fs.trial_L).abs(), (pyr.trial_R - pyr.trial_L).abs()\nrows.append({\"measure\": \"selectivity b |R-L| (spk/s)\", \"FS_mean\": af.mean(), \"pyr_mean\": ap.mean(), \"FS_median\": af.median(),\n             \"pyr_median\": ap.median(), \"FS_less_selective\": af.mean() < ap.mean(), \"ranksum_p\": stats.mannwhitneyu(af.dropna(), ap.dropna()).pvalue})\nafn, apn = af / ((fs.trial_R + fs.trial_L) / 2), ap / ((pyr.trial_R + pyr.trial_L) / 2)\nrows.append({\"measure\": \"variant |R-L| / mean rate\", \"FS_mean\": afn.mean(), \"pyr_mean\": apn.mean(), \"FS_median\": afn.median(),\n             \"pyr_median\": apn.median(), \"FS_less_selective\": afn.median() < apn.median(), \"ranksum_p\": stats.mannwhitneyu(afn.dropna(), apn.dropna()).pvalue})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"\\nFS neurons:\", len(fs), \"; pyramidal:\", len(pyr), \"; FS per mouse:\", fs.groupby(\"animal\").size().to_dict())\n#%% md\n## tagging-counts\n\n> 73 neurons were antidromically activated from PT axons and 134 from IT axons; 45 and 27 passed\n> the collision test (PT and IT neurons), 22 and 106 failed it, and 6 and 1 could not be tested\n> and were excluded.\n#%% code tags=claim:tagging-counts\nprint(\"Units labelled PT:\", int((D.tag == \"PT\").sum()), \"; IT:\", int((D.tag == \"IT\").sum()))\nprint(\"PT per mouse:\", D[D.tag == \"PT\"].groupby(\"animal\").size().to_dict())\nprint(\"IT per mouse:\", D[D.tag == \"IT\"].groupby(\"animal\").size().to_dict())\nprint(\"Labels other than pyramidal, FS, PT, IT:\", sorted({c for s, u in units for c in u['cell_types']} - {\"pyramidal\", \"FS\", \"PT\", \"IT\"}))\nprint(\"Sessions with PT (type 1) tagging trials:\", T[T.ptype == 1].session.nunique(), \"; with IT (types 2 to 5):\", T[T.ptype.isin([2, 3, 4, 5])].session.nunique())\n#%% md\nThe data set labels only the neurons that passed the collision test. The pyramidal-tract- and\nintratelencephalic-activated neurons (22 and 106) and the 7 that could not be tested carry no\nlabel, so their counts cannot be read from the data set.\n\n## antidromic-latency-jitter\n\n> PT neurons have shorter antidromic latencies than IT neurons (mean 2.7 against 4.6 ms) and both\n> have small jitter (mean s.d. 0.1 and 0.2 ms) ...; the mean jitter of tagged neurons is 0.15 ms.\n\nPulse onsets are read from the AOM input trace (10 kHz, so 0.1 ms steps); spike times are at\nthe 19531.25 Hz sampling of the recording. For each PT neuron, the PT axonal stimulation trials\n(type 1); for each IT neuron, the IT trials (type 2, and in a variant also the undocumented\ntypes 3 to 5). Latency is the first spike within 10 ms of a pulse onset (before the second\npulse). The paper does not say how antidromic spikes are told from spontaneous ones; here they\nare the spikes within ±1 ms of the neuron's modal latency (0.2 ms bins), with ±0.5 ms as a\nvariant (an assumption). Readings: (a) first pulse of each pair, (b) both pulses pooled.\n#%% code tags=claim:antidromic-latency-jitter\ndef lat_table(it_types, hw):\n    rows = []\n    for s, u in units:\n        tag = \"PT\" if \"PT\" in u[\"cell_types\"] else \"IT\" if \"IT\" in u[\"cell_types\"] else \"\"\n        if not tag:\n            continue\n        types = {1.0} if tag == \"PT\" else it_types\n        l0 = alm.antidromic_latencies(s, u, types, order=0)\n        l1 = alm.antidromic_latencies(s, u, types, order=1)\n        for reading, lat in ((\"a first pulse\", l0), (\"b both pulses\", np.r_[l0, l1])):\n            m, sd, n, nr = alm.latency_mode_stats(lat, hw)\n            rows.append({\"session\": s[\"session\"], \"unit\": u[\"unit\"], \"animal\": s[\"animal\"], \"tag\": tag, \"reading\": reading,\n                         \"latency_ms\": m, \"jitter_ms\": sd, \"n_resp\": n, \"n_pulses\": len(lat), \"p_resp\": n / max(len(lat), 1)})\n    return pd.DataFrame(rows)\n\nLT = {}\nsumm = []\nfor it_types, it_name in (({2.0}, \"IT type 2\"), ({2.0, 3.0, 4.0, 5.0}, \"IT types 2-5\")):\n    for hw in (1.0, 0.5):\n        lt = lat_table(it_types, hw)\n        LT[(it_name, hw)] = lt\n        for reading, d in lt.groupby(\"reading\"):\n            ok = d[d.n_resp >= 3]\n            pt, it = ok[ok.tag == \"PT\"], ok[ok.tag == \"IT\"]\n            summ.append({\"IT trials\": it_name, \"window_ms\": hw, \"reading\": reading, \"PT_n\": len(pt), \"IT_n\": len(it),\n                         \"PT_latency\": pt.latency_ms.mean(), \"IT_latency\": it.latency_ms.mean(),\n                         \"PT_jitter\": pt.jitter_ms.mean(), \"IT_jitter\": it.jitter_ms.mean(), \"tagged_jitter\": ok.jitter_ms.mean(),\n                         \"PT_latency_median\": pt.latency_ms.median(), \"IT_latency_median\": it.latency_ms.median()})\nlat = pd.DataFrame(summ)\nlat[\"PT_ok\"] = (abs(lat.PT_latency - 2.7) <= 0.27) & (abs(lat.PT_jitter - 0.1) <= 0.05)\nlat[\"IT_ok\"] = (abs(lat.IT_latency - 4.6) <= 0.46) & (abs(lat.IT_jitter - 0.2) <= 0.05)\nlat[\"tagged_jitter_ok\"] = abs(lat.tagged_jitter - 0.15) <= 0.015\nlat[\"PT_shorter\"] = lat.PT_latency < lat.IT_latency\nprint(lat.round(3).to_string(index=False))\nmain_lt = LT[(\"IT type 2\", 1.0)]\nprint(\"\\nPer neuron (IT type 2, ±1 ms, first pulse):\")\nprint(main_lt[main_lt.reading == \"a first pulse\"].round(3).to_string(index=False))\n#%% md\n## ed5g-it-second-pulse-jitter\n\n> After a conditioning pulse, IT neurons respond to a second light pulse 10 ms later with less\n> temporal jitter.\n#%% code tags=claim:ed5g-it-second-pulse-jitter\nrows = []\nfor it_types, it_name in (({2.0}, \"IT type 2\"), ({2.0, 3.0, 4.0, 5.0}, \"IT types 2-5\")):\n    for hw in (1.0, 0.5):\n        for s, u in units:\n            if \"IT\" not in u[\"cell_types\"]:\n                continue\n            j = []\n            for order in (0, 1):\n                m, sd, n, nr = alm.latency_mode_stats(alm.antidromic_latencies(s, u, it_types, order=order), hw)\n                j += [sd, n]\n            rows.append({\"IT trials\": it_name, \"window_ms\": hw, \"session\": s[\"session\"], \"unit\": u[\"unit\"], \"jitter_1\": j[0], \"n_1\": j[1], \"jitter_2\": j[2], \"n_2\": j[3]})\nj2 = pd.DataFrame(rows)\nout = []\nfor (it_name, hw), d in j2.groupby([\"IT trials\", \"window_ms\"]):\n    ok = d[(d.n_1 >= 3) & (d.n_2 >= 3)].dropna()\n    out.append({\"IT trials\": it_name, \"window_ms\": hw, \"neurons\": len(ok), \"mean_jitter_first\": ok.jitter_1.mean(), \"mean_jitter_second\": ok.jitter_2.mean(),\n                \"fraction_decrease\": (ok.jitter_2 < ok.jitter_1).mean(), \"wilcoxon_p\": stats.wilcoxon(ok.jitter_1, ok.jitter_2).pvalue if len(ok) > 1 else np.nan,\n                \"dropped_few_responses\": len(d) - len(ok)})\nj2s = pd.DataFrame(out)\nj2s[\"holds\"] = (j2s.mean_jitter_second < j2s.mean_jitter_first) & (j2s.fraction_decrease > 0.5)\nprint(j2s.round(4).to_string(index=False))\n#%% md\n## fig3ei-both-types-preparatory-and-movement\n\n> Both IT and PT neurons display preparatory and movement-related activity.\n#%% code tags=claim:fig3ei-both-types-preparatory-and-movement\nrows = []\nfor (le, resp), d in UT.items():\n    for tag in (\"PT\", \"IT\"):\n        c = alm.categories(d[d.tag == tag])\n        rows.append({\"lick_early\": le, \"response_s\": resp, \"type\": tag, \"neurons\": int((d.tag == tag).sum()), **c,\n                     \"frac_prep_only\": c[\"prep_only\"] / max(c[\"n\"], 1), \"frac_both\": c[\"both\"] / max(c[\"n\"], 1), \"frac_peri_only\": c[\"peri_only\"] / max(c[\"n\"], 1)})\nc3 = pd.DataFrame(rows)\nc3[\"has_prep_and_peri\"] = (c3.prep_only + c3.both > 0) & (c3.peri_only + c3.both > 0)\nprint(c3.round(3).to_string(index=False))\nprint(\"Paper, read from Fig. 3e, i: PT about 0.18, 0.43, 0.40; IT about 0.22, 0.56, 0.22 (preparatory only, both, movement only)\")\n#%% md\n## fig3fj-contra-preferring-pt-not-it\n\n> Contra-preferring neurons outnumber ipsi-preferring neurons among PT neurons but not among IT\n> neurons.\n#%% code tags=claim:fig3fj-contra-preferring-pt-not-it\nrng = np.random.default_rng(4)\nrows = []\nfor (le, resp), d in UT.items():\n    for reading, base in ((\"a all\", d), (\"b selective\", d[d.selective])):\n        for tag in (\"PT\", \"IT\"):\n            x = base[base.tag == tag].contra.values\n            rows.append({\"lick_early\": le, \"response_s\": resp, \"reading\": reading, \"type\": tag, \"neurons\": len(x),\n                         \"contra\": int(x.sum()), \"fraction_contra\": x.mean(), \"P\": alm.bootstrap_more_ipsi(x, rng=rng)})\nf3 = pd.DataFrame(rows)\nprint(f3.round(4).to_string(index=False))\npiv = f3.pivot_table(index=[\"lick_early\", \"response_s\", \"reading\"], columns=\"type\", values=\"P\")\npiv[\"PT_sig_IT_not\"] = (piv.PT < 0.05) & (piv.IT >= 0.05)\nprint(\"\\n\", piv.round(4).to_string())\n#%% md\n## fig3f-late-contra-selectivity-pt\n\n> Robust contralateral selectivity emerges in PT neurons starting 570 ms before the response\n> epoch (34% spike rate modulation, P < 0.05), but not in IT neurons (-19%, P = 0.40) nor in all\n> task-selective neurons (8%, P = 0.13).\n\nContra-selectivity is R minus L rate per neuron (correct trials, 200 ms windows, 10 ms step).\nOnset readings (a) the earliest window centre from which the PT mean stays significantly above\n0 (t-test across neurons, P < 0.05) through the window centred 0.1 s before the cue, (b) the\nfirst significant window after sample onset. Modulation windows (a) 570 ms before the cue to\nthe cue, (b) to the end of the response epoch; percentage of (a) the mean rate over both trial\ntypes in the window, (b) the mean rate in the 0.5 s before sample onset. Neurons (a) all PT\n(IT), (b) the selective ones; \"all task-selective\" is the selective pyramidal neurons.\n#%% code tags=claim:fig3f-late-contra-selectivity-pt\ndef cs_curve(keys):\n    out = []\n    for s, u in units:\n        if (s[\"session\"], u[\"unit\"]) not in keys:\n            continue\n        tr = s[\"trials\"]\n        r, l = alm.trial_mask(tr, u)\n        if r.sum() < 2 or l.sum() < 2:\n            continue\n        out.append((alm.window_sums(alm.cue_binned(u, tr, r))[0].mean(axis=0) - alm.window_sums(alm.cue_binned(u, tr, l))[0].mean(axis=0)) / alm.WIN_S)\n    return np.array(out)\n\ndef win_rates(keys, a_rel, b_rel):\n    rows = []\n    for s, u in units:\n        if (s[\"session\"], u[\"unit\"]) not in keys:\n            continue\n        tr = s[\"trials\"]\n        r, l = alm.trial_mask(tr, u)\n        if r.sum() < 2 or l.sum() < 2:\n            continue\n        a, b = tr.cue.values + a_rel, tr.cue.values + b_rel\n        pa, pb_ = tr.pole_in.values - 0.5, tr.pole_in.values\n        R = alm.counts_in(u, tr, r, a, b).mean() / (b_rel - a_rel)\n        L = alm.counts_in(u, tr, l, a, b).mean() / (b_rel - a_rel)\n        base = (alm.counts_in(u, tr, r, pa, pb_).mean() + alm.counts_in(u, tr, l, pa, pb_).mean()) / 2 / 0.5\n        rows.append((R, L, base))\n    return np.array(rows)\n\nkeyset = lambda d: set(map(tuple, d[[\"session\", \"unit\"]].values))\ngroups = {\"PT a all\": keyset(D[D.tag == \"PT\"]), \"PT b selective\": keyset(D[(D.tag == \"PT\") & D.selective]),\n          \"IT a all\": keyset(D[D.tag == \"IT\"]), \"IT b selective\": keyset(D[(D.tag == \"IT\") & D.selective]),\n          \"all task-selective\": keyset(pyr[pyr.selective])}\nonsets = []\nfor name in (\"PT a all\", \"PT b selective\"):\n    C = cs_curve(groups[name])\n    p = stats.ttest_1samp(C, 0, axis=0).pvalue\n    sigpos = (p < 0.05) & (C.mean(axis=0) > 0)\n    valid = (centers >= t_sample) & (centers <= -0.1)\n    idx = np.flatnonzero(valid)\n    stay = None\n    for i in idx[::-1]:\n        if sigpos[i]:\n            stay = centers[i]\n        else:\n            break\n    first = centers[idx][sigpos[idx]][0] if sigpos[idx].any() else np.nan\n    onsets.append({\"neurons\": name, \"n\": len(C), \"onset_a_stays_ms_before_cue\": -1e3 * stay if stay is not None else np.nan,\n                   \"onset_b_first_ms_before_cue\": -1e3 * first})\nons = pd.DataFrame(onsets)\nons[\"a_ok\"] = abs(ons.onset_a_stays_ms_before_cue - 570) <= 100\nons[\"b_ok\"] = abs(ons.onset_b_first_ms_before_cue - 570) <= 100\nprint(ons.round(1).to_string(index=False))\nrows = []\nfor wname, (a_rel, b_rel) in ((\"a -0.57 to cue\", (-0.57, 0.0)), (\"b -0.57 to response end\", (-0.57, alm.RESPONSE_S))):\n    for name, keys in groups.items():\n        X = win_rates(keys, a_rel, b_rel)\n        dlt = X[:, 0] - X[:, 1]\n        tt = stats.ttest_1samp(dlt, 0)\n        rows.append({\"window\": wname, \"neurons\": name, \"n\": len(X), \"mean_R_minus_L\": dlt.mean(), \"p\": tt.pvalue,\n                     \"mod_pct_a_window_rate\": 100 * dlt.mean() / ((X[:, 0] + X[:, 1]) / 2).mean(),\n                     \"mod_pct_b_baseline\": 100 * dlt.mean() / X[:, 2].mean()})\nmod = pd.DataFrame(rows)\nprint(mod.round(4).to_string(index=False))\nexp = {\"PT\": 34, \"IT\": -19, \"all task-selective\": 8}\ncombos = []\nfor w in mod.window.unique():\n    for nr in (\"a all\", \"b selective\"):\n        for pct in (\"mod_pct_a_window_rate\", \"mod_pct_b_baseline\"):\n            m = mod[mod.window == w].set_index(\"neurons\")\n            pt_, it_, al_ = m.loc[f\"PT {nr}\"], m.loc[f\"IT {nr}\"], m.loc[\"all task-selective\"]\n            combos.append({\"window\": w, \"neurons\": nr, \"percent_of\": pct, \"PT_sig\": pt_.p < 0.05, \"IT_not\": it_.p >= 0.05, \"all_not\": al_.p >= 0.05,\n                           \"PT_pct\": pt_[pct], \"IT_pct\": it_[pct], \"all_pct\": al_[pct],\n                           \"values_ok\": abs(pt_[pct] - 34) <= 3.4 and abs(it_[pct] + 19) <= 1.9 and abs(al_[pct] - 8) <= 0.8})\ncmb = pd.DataFrame(combos)\ncmb[\"pattern_ok\"] = cmb.PT_sig & cmb.IT_not & cmb.all_not\nprint(\"\\n\", cmb.round(2).to_string(index=False))\n#%% md\n## reaction-time\n\n> The reaction time after go cue onset is 61.1 +/- 10.5 ms across mice (mean +/- s.d.).\n\nFirst movement of the lick trace after the cue (rule in the helper's docstring; the threshold\nfraction of the trial's peak excursion is a reading). Trials (a) correct trials without early\nlicks or stimulation, (b) all performing trials with a response (hit or error). Per mouse the\nmean, then mean and s.d. across mice; per-mouse medians are a variant.\n#%% code tags=claim:reaction-time\nrows = []\nbase_sel = (T.good == 1) & T.cue.notna()\nfor tname, sel in ((\"a correct\", base_sel & (T.ptype == 0) & (T.HitR | T.HitL) & ~T.LickEarly),\n                   (\"b all responses\", base_sel & (T.HitR | T.HitL | T.ErrR | T.ErrL))):\n    for r in alm.LICK_RISE:\n        col = f\"rt_{r}\"\n        d = T[sel]\n        pm = d.groupby(\"animal\")[col].mean() * 1e3\n        pmed = d.groupby(\"animal\")[col].median() * 1e3\n        rows.append({\"trials\": tname, \"fraction_of_peak\": r, \"mice\": int(pm.notna().sum()), \"mean_ms\": pm.mean(), \"sd_ms\": pm.std(),\n                     \"mean_of_medians_ms\": pmed.mean(), \"trials_without_onset\": float(d[col].isna().mean())})\nrt = pd.DataFrame(rows)\nrt[\"within_tolerance\"] = abs(rt.mean_ms - 61.1) <= 10.5\nprint(rt.round(2).to_string(index=False))\nd = T[base_sel & (T.ptype == 0) & (T.HitR | T.HitL) & ~T.LickEarly]\nprint(\"\\nPer mouse, reading a, fraction 0.1 (ms):\", (d.groupby(\"animal\")[\"rt_0.1\"].mean() * 1e3).round(1).to_dict())\n#%% md\n## contra-ipsi-selectivity-forms\n\n> Contra-preferring neurons include most of the neurons with large spike count differences\n> between trial types, while ipsi-preferring neurons more often express their selectivity\n> through suppression of activity on contra trials.\n\nPer selective pyramidal neuron, the absolute difference of R and L rates from sample onset to\nthe end of the response epoch. Contra-suppression: the rate on R trials (same span) below the\nrate in the 0.5 s before sample onset, with the rate on L trials not below it; ipsi-suppression\nis the same with the trial types swapped. The whole pre-sample period is a variant baseline.\n#%% code tags=claim:contra-ipsi-selectivity-forms\nsp = pyr[pyr.selective].copy()\nsp[\"absdiff\"] = (sp.trial_R - sp.trial_L).abs()\nrows = []\nfor q, name in ((0.75, \"a top quarter\"), (0.90, \"b top tenth\")):\n    big = sp[sp.absdiff >= sp.absdiff.quantile(q)]\n    rows.append({\"reading\": name, \"neurons\": len(big), \"fraction_contra\": big.contra.mean(), \"binomial_p\": stats.binomtest(int(big.contra.sum()), len(big)).pvalue})\nlarge = pd.DataFrame(rows)\nlarge[\"contra_majority\"] = large.fraction_contra > 0.5\nprint(large.round(4).to_string(index=False))\nrows = []\nfor bname, bcol in ((\"0.5 s pre-sample\", \"pre\"), (\"whole pre-sample (variant)\", \"pre_all\")):\n    base = (sp[f\"{bcol}_R\"] + sp[f\"{bcol}_L\"]) / 2\n    csup = (sp.trial_R < base) & ~(sp.trial_L < base)\n    isup = (sp.trial_L < base) & ~(sp.trial_R < base)\n    ip, cp = sp[~sp.contra], sp[sp.contra]\n    rows.append({\"baseline\": bname, \"ipsi_pref_n\": len(ip), \"ipsi_pref_with_contra_suppression\": float(csup[~sp.contra].mean()),\n                 \"contra_pref_n\": len(cp), \"contra_pref_with_ipsi_suppression\": float(isup[sp.contra].mean()),\n                 \"fisher_p\": stats.fisher_exact([[int(csup[~sp.contra].sum()), len(ip) - int(csup[~sp.contra].sum())],\n                                                 [int(isup[sp.contra].sum()), len(cp) - int(isup[sp.contra].sum())]])[1]})\nsup = pd.DataFrame(rows)\nsup[\"ipsi_more\"] = sup.ipsi_pref_with_contra_suppression > sup.contra_pref_with_ipsi_suppression\nprint(sup.round(4).to_string(index=False))\n#%% md\n## Summary\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
s=s.replace('''for s, u in units:
    if (D.label.values[0] is None):
        pass
for s, u in units:
    key = (s["session"], u["unit"])
    if key not in set(map(tuple, pyr[["session", "unit"]].values)):''','''pyr_keys = set(map(tuple, pyr[["session", "unit"]].values))
for s, u in units:
    key = (s["session"], u["unit"])
    if key not in pyr_keys:''')
open('cells.py','w').write(s)
EOF
cat > build.py <<'EOF'
import re, sys, nbformat
src = open('/tmp/claude-1001/cells.py').read()
parts = re.split(r'^#%% (md|code)(?: tags=(\S+))?\n', src, flags=re.M)
cells = []
for i in range(1, len(parts), 3):
    kind, tags, body = parts[i], parts[i+1], parts[i+2].rstrip('\n')
    if kind == 'md':
        c = nbformat.v4.new_markdown_cell(body)
    else:
        c = nbformat.v4.new_code_cell(body)
    if tags:
        c.metadata['tags'] = [tags]
    cells.append(c)
if sys.argv[1] == 'nb':
    extra = open('/tmp/claude-1001/summary.md').read() if len(sys.argv) > 3 else None
    nb = nbformat.v4.new_notebook(); nb.cells = cells
    nb.metadata['kernelspec'] = {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'}
    nbformat.write(nb, sys.argv[2])
else:
    code = []
    for c in cells:
        if c.cell_type != 'code': continue
        b = c.source
        if 'S = alm.load_all' in b:
            b = b.replace('S = alm.load_all(workers=4)', 'import pickle; S = pickle.load(open("/tmp/claude-1001/all.pkl","rb"))')
        b = b.replace('plt.show()', 'plt.close()')
        code.append('print("\\n##### CELL", %r)\n' % (c.metadata.get('tags', [''])[0]) + b)
    open('/tmp/claude-1001/dev_run.py', 'w').write('\n'.join(code))
EOF
. dev/bin/activate && python build.py dev && cd entries/crcns-alm-1-li-2015 && time python $TMPDIR/dev_run.py 2>&1 | tail -n +1 > $TMPDIR/out.txt; tail -5 $TMPDIR/out.txt; wc -l $TMPDIR/out.txt
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/build.py", line 1, in <module>
    import re, sys, nbformat
ModuleNotFoundError: No module named 'nbformat'
tail: cannot open '/tmp/claude-1001/out.txt' for reading: No such file or directory
wc: /tmp/claude-1001/out.txt: No such file or directory
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q nbformat pyyaml jsonschema && python build.py dev && cd entries/crcns-alm-1-li-2015 && time python $TMPDIR/dev_run.py > $TMPDIR/out.txt 2>&1; tail -5 $TMPDIR/out.txt; wc -l $TMPDIR/out.txt
```

```
real	0m2.424s
user	0m2.585s
sys	0m0.156s
##### CELL 
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_run.py", line 12, in <module>
    import alm
ModuleNotFoundError: No module named 'alm'
6 /tmp/claude-1001/out.txt
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time PYTHONPATH=. python $TMPDIR/dev_run.py > $TMPDIR/out.txt 2>&1; date -u; cat $TMPDIR/out.txt | cut -c1-250
```

```
<persisted-output>
Output too large (37.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bfu2h9g5m.txt

Preview (first 2KB):
real	0m49.273s
user	0m49.236s
sys	0m0.303s
Sat Nov  7 21:43:36 UTC 2026

##### CELL 
crcns:alm-1 (unversioned, doi:10.6080/K0RF5RZT): 99 sessions streamed in 1 s

##### CELL sanity
MD5 sums on the bucket now (compare with the header):
  cfacee06a26e5252ff22c922cab6e728  datafiles/meta_data_files.tar.gz
  ffc4cd8784c52d59509dec395f4dca6c  datafiles/data_structure_files/data_structure_ANM210861.tar.gz
  455903de0b4efbbe3b6702d096001fd0  datafiles/data_structure_files/data_structure_ANM210862.tar.gz
  a7ff42aed79240ce6522decd5a378bcc  datafiles/data_structure_files/data_structure_ANM210863.tar.gz
  6506e8e3e5426af5e6aae2a7d4be020f  datafiles/data_structure_files/data_structure_ANM214427.tar.gz
  72e04c6020096fc38de13b4e34d9a2f2  datafiles/data_structure_files/data_structure_ANM214429.tar.gz
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 30,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bfu2h9g5m.txt | cut -c1-260 | grep -v "^ANM2.*first pulse"
```

```
<persisted-output>
Output too large (30.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bx3whxuqa.txt

Preview (first 2KB):
  4f118c0085d3011a7ff6d0f35f298bf9  datafiles/data_structure_files/data_structure_ANM219253.tar.gz
  44ceb341033227f98693e39c7103527a  datafiles/data_structure_files/data_structure_ANM221977.tar.gz
           sessions  units  trials     strain                gene photostim_location
ANM210861         3     58    1290       kj18            sim1-cre           PONS/ALM
ANM210862         3     53     971       kj18            sim1-cre           PONS/ALM
ANM210863         3     90    1031       kj18            sim1-cre           PONS/ALM
ANM214427         4     26    1485      kl100            rbp4-cre       ALM/PONS/ALM
ANM214429         4     48    2051      kl100            rbp4-cre       ALM/PONS/ALM
ANM214430         4     42    1245      kl100            rbp4-cre       ALM/PONS/ALM
ANM218453         5     54    1566  pl56/ai32   tlx-cre/chr2-eyfp                   
ANM218457         6    118    1906  pl56/ai32   tlx-cre/chr2-eyfp                   
ANM218693         3     59    1022  kj18/ai32  sim1-cre/chr2-eyfp                   
ANM219030         5     57    1676       kj18            sim1-cre           PONS/ALM
ANM219031         5     93    1487       kj18            sim1-cre           PONS/ALM
ANM219033         7     57    2069       kj18            sim1-cre           PONS/ALM
ANM219036         7     97    1840       kj18            sim1-cre           PONS/ALM
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bx3whxuqa.txt",
 "offset": 22
}
```

```
22	ANM221977         3     36     930       pl56             tlx-cre            ALM/ALM
23	
24	Animals 19, sessions 99, units 1408 (data description: 19 animals, 99 sessions, 1,408 units)
25	Meta data files: 99 ; sessions with a meta data file: 99
26	Strains (paper, Methods: 9 Sim1_KJ18-Cre, 3 Rbp4-Cre, 4 Tlx_PL56-Cre injected; 1 Sim1 x Ai32, 2 Tlx x Ai32):
27	strain     gene              
28	kj18       sim1-cre              9
29	kj18/ai32  sim1-cre/chr2-eyfp    1
30	kl100      rbp4-cre              3
31	pl56       tlx-cre               4
32	pl56/ai32  tlx-cre/chr2-eyfp     2
33	
34	##### CELL sanity
35	Trials: 31439
36	
37	PhotostimulationType (description: 0 none, 1 PT axonal, 2 IT axonal, NaN do not analyse):
38	ptype
39	0.0    19492
40	1.0     4029
41	2.0     3162
[... 330 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 370,420p /home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bx3whxuqa.txt | cut -c1-260
```

```
neurons  n  onset_a_stays_ms_before_cue  onset_b_first_ms_before_cue  a_ok  b_ok
```

**Agent calls Bash**

```bash
grep -n "fig3f-late" -A 60 /home/runner/.claude/projects/-home-runner-work-encore-encore/8b6c56f4-f4cb-4bb7-a693-6d507439725f/tool-results/bfu2h9g5m.txt | cut -c1-240
```

```
399:##### CELL claim:fig3f-late-contra-selectivity-pt
400-       neurons  n  onset_a_stays_ms_before_cue  onset_b_first_ms_before_cue  a_ok  b_ok
401-      PT a all 45                        310.0                       2480.0 False False
402-PT b selective 38                        310.0                       2480.0 False False
403-                 window            neurons   n  mean_R_minus_L      p  mod_pct_a_window_rate  mod_pct_b_baseline
404-         a -0.57 to cue           PT a all  45          2.0023 0.0266                34.4016             31.1241
405-         a -0.57 to cue     PT b selective  38          2.3588 0.0270                37.4029             33.4684
406-         a -0.57 to cue           IT a all  27         -0.6826 0.1134               -16.4354            -15.4458
407-         a -0.57 to cue     IT b selective  23         -0.9200 0.0548               -22.1559            -21.9750
408-         a -0.57 to cue all task-selective 912          0.4638 0.0240                 9.1961             10.2620
409-b -0.57 to response end           PT a all  45          1.3084 0.0683                20.5637             20.3375
410-b -0.57 to response end     PT b selective  38          1.5514 0.0677                22.1920             22.0118
411-b -0.57 to response end           IT a all  27         -0.7869 0.5096               -15.9920            -17.8052
412-b -0.57 to response end     IT b selective  23         -0.8680 0.5365               -16.8604            -20.7320
413-b -0.57 to response end all task-selective 912          0.0090 0.9578                 0.1818              0.1989
414-
415-                  window     neurons            percent_of  PT_sig  IT_not  all_not  PT_pct  IT_pct  all_pct  values_ok  pattern_ok
416-         a -0.57 to cue       a all mod_pct_a_window_rate    True    True    False   34.40  -16.44     9.20      False       False
417-         a -0.57 to cue       a all    mod_pct_b_baseline    True    True    False   31.12  -15.45    1
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
s=s.replace('''print("Units whose spike times are not sorted:", unsorted)''','''print("Units whose spike times are not sorted:", unsorted, [f"{s['session']}/{u['unit']}" for s, u in units if np.any(np.diff(u["spike_t_session"]) < 0)])''')
s=s.replace('''print("Trial type counts in performing trials:", g[alm.TRIAL_TYPES].sum().to_dict())''','''print("Trial type counts in performing trials:", g[alm.TRIAL_TYPES].sum().to_dict())
odd = g[(abs(g.pole_out - g.pole_in - 1.3) > 0.05) | (abs(g.cue - g.pole_out - 1.3) > 0.05)]
print("Performing trials whose sample or delay epoch differs from 1.3 s by more than 50 ms:", len(odd), "of", len(g),
      "; of these correct non-stimulation trials:", int((odd.ptype.eq(0) & (odd.HitR | odd.HitL)).sum()))''')
open('cells.py','w').write(s)
EOF
cd entries/crcns-alm-1-li-2015 && sed -i 's/LICK_RISE = (0.1, 0.25, 0.5)/LICK_RISE = (0.05, 0.1, 0.25, 0.5)/' alm.py && grep -n "^LICK_RISE" alm.py; date -u
```

```
73:LICK_RISE = (0.05, 0.1, 0.25, 0.5)   # fractions of the trial's peak excursion, readings
Sat Nov  7 21:44:34 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
R = {
'task-performance': '''**Result: reproduced, on 19 of the 42 mice.** On control trials the mean per cent correct is 76.84% over sessions (reading a), 76.37% over mice and 77.28% over pooled trials, all within 78.4 ± 7.84%; lick early trials are 10.88% of control trials over sessions and 12.59% pooled, below 13%. Over mice the lick early fraction is 14.06%, above 13% but below 14.3%. With all trials the per cent correct is 75.81% to 76.58%. Only the 19 electrophysiology mice are in the data set; per mouse the per cent correct ranges from 60.4% to 87.0%.''',
'unit-counts': '''**Result: partially reproduced.** The data set holds 1,408 units from 19 mice in 99 sessions, and its cell type labels give exactly 1,245 pyramidal, 124 FS and 39 unclassified units. Recomputed as the criterion says, from the trough-to-peak interval of the deposited mean waveforms, 1,245 units are above 0.45 ms, as the paper has, but 158 are below 0.35 ms and 5 in between, against 124 and 39: 34 of the 39 unlabelled units have widths below 0.35 ms. The spline-interpolated variant gives 1,241, 158 and 9. The labels hold the paper's classification; the widths of the deposited waveforms do not give it for the unlabelled units.''',
'fig2-selective-fraction': '''**Result: reproduced.** With lick early trials dropped and a 1.3 s response epoch, 912 of 1,245 pyramidal neurons (73.25%) are selective, the paper's numbers exactly. The other readings give 910 to 950 (73.1% to 76.3%) and Welch's test 903 to 947; all are within tolerance. Per mouse the fraction ranges from 0.417 to 0.852.''',
'fig2d-response-categories': '''**Result: reproduced, under the figure's reading of the labels.** With lick early trials dropped and a 1.3 s response epoch the 912 selective neurons split into 219 preparatory only, 389 with both and 304 peri-movement only. This matches Fig. 2d (reading b) exactly and the text (reading a, 389 peri-movement only and 304 both) not at all, under every reading of the response epoch and of lick early trials. The text has the two larger counts the wrong way round.''',
'fig2c-selectivity-time-course': '''**Result: reproduced.** The number of significant pyramidal neurons is 60 in the window before sample onset (shuffled labels: median 54, 5% of neurons 62), 246 at the end of the sample epoch, 298 at the start and 379 at the end of the delay, and peaks at 554 in the window centred 0.19 s after the cue. The population selectivity of 880 selective neurons is 0.005 spikes/s before the sample, 1.19 at the end of the sample, 1.46 and 2.28 at the start and end of the delay, and peaks at 3.38 spikes/s 0.20 s after the cue. Both measures meet all three conditions under both readings (maximum within 0.2 s of the cue).''',
'fig2c-dynamic-single-neurons': '''**Result: reproduced, resting on the claims file's 0.5 bound.** The mean population response correlation with the cue-time vector over the sample epoch and the first 0.5 s of the delay is -0.168 (reading a) and -0.159 (reading b), with maxima of -0.024 and -0.042 in that span; with division by the s.d. it is -0.041 and -0.084. All are below 0.5, while the population selectivity stays above 0 from the end of the sample epoch through the delay (minimum 1.19 spikes/s).''',
'ed2-error-trials-predict-choice': '''**Result: reproduced.** Under both readings and the script's selection, correct and error selectivity are negatively correlated in all three epochs (sample r = -0.085 to -0.123, P 0.006 to 0.017; delay r = -0.43 to -0.48; response r = -0.44 to -0.50, P < 1e-20), and the fraction of neurons whose error selectivity has the opposite sign exceeds one half in every epoch (0.507 to 0.652). In the sample epoch the correlation is weak and the fraction just above one half (0.507 with at least one error trial of each type).''',
'fig2e-equal-contra-ipsi': '''**Result: reproduced.** By total counts 427 selective pyramidal neurons prefer contra and 485 ipsi, the counts of Fig. 2c exactly (fraction contra 0.468); the Methods' bootstrap finds no excess of contra-preferring neurons (P = 0.97). With the 10-trial split, 436 and 444 (P = 0.60). A binomial test of reading a against 0.5 gives p = 0.059, so ipsi-preferring neurons are slightly more common, short of significance.''',
'ed1-no-population-contra-bias': '''**Result: reproduced.** The mean lick right minus lick left rate is 0.090 spikes/s for the selective pyramidal neurons (P = 0.44), 0.061 for all pyramidal neurons (P = 0.48) and 0.071 for all units (P = 0.39); none is significant, as the paper's P = 0.13 is not. The variants give P = 0.36 and 0.62.''',
'ed1-fast-spiking-properties': '''**Result: partially reproduced.** FS neurons have higher baseline rates than pyramidal neurons under both readings (mean 9.03 against 3.97 spikes/s, median 6.40 against 2.37, rank-sum p < 1e-10). They are not less selective under either of the criterion's readings: 79.8% of FS neurons are selective against 73.3% of pyramidal neurons, and their mean absolute rate difference is larger (2.29 against 1.53 spikes/s). Only relative to their rate (a variant the criterion does not name) are FS neurons less selective (median 0.21 against 0.33).''',
'tagging-counts': '''**Result: reproduced for the PT and IT counts.** The labels give 45 PT neurons in 8 mice and 27 IT neurons in 7 mice, the paper's numbers. The pyramidal-tract-activated and intratelencephalic-activated neurons and the untestable ones have no label, so those counts cannot be reported.''',
'antidromic-latency-jitter': '''**Result: reproduced, resting on the assumed ±0.5 ms window.** With antidromic spikes taken within ±0.5 ms of each neuron's modal latency, first pulses, PT neurons have a mean latency of 2.675 ms and jitter 0.113 ms (45 neurons), and IT neurons 5.00 ms and 0.198 ms (21 neurons with type 2 trials) or 4.58 ms and 0.177 ms (27 neurons with types 2 to 5); the mean jitter of tagged neurons is 0.140 or 0.137 ms; all within tolerance and PT shorter than IT. With a ±1 ms window the PT values still match (2.672 ms, 0.126 ms) but the IT jitter is 0.27 to 0.31 ms, outside 0.2 ± 0.05, and the tagged mean 0.18 ms, so the IT jitter depends on the window. The activated neurons are not labelled, so their values cannot be computed.''',
'ed5g-it-second-pulse-jitter': '''**Result: reproduced.** In every variant the mean jitter of IT neurons is lower for the second pulse than for the first (0.156 against 0.204 ms with type 2 trials and ±0.5 ms; 0.232 against 0.280 ms with types 2 to 5 and ±1 ms), and 65% to 87% of IT neurons show the decrease (Wilcoxon p 0.004 to 0.098). 4 to 8 IT neurons with fewer than three responses to either pulse are left out.''',
'fig3ei-both-types-preparatory-and-movement': '''**Result: reproduced.** Under every reading both populations hold neurons with preparatory and with peri-movement selectivity. With lick early trials dropped and a 1.3 s response epoch, of 38 selective PT neurons 7 are preparatory only, 16 both and 15 peri-movement only (0.184, 0.421, 0.395; Fig. 3e reads about 0.18, 0.43, 0.40), and of 23 selective IT neurons 5, 13 and 5 (0.217, 0.565, 0.217; Fig. 3i about 0.22, 0.56, 0.22).''',
'fig3fj-contra-preferring-pt-not-it': '''**Result: reproduced, under the reading of selective neurons.** Among selective neurons (reading b, lick early dropped, 1.3 s response) 24 of 38 PT neurons prefer contra (0.632, P = 0.033) and 10 of 23 IT neurons (0.435, P = 0.74, the paper's value). With lick early trials kept the PT P is 0.014; with a 1.5 s response epoch and lick early dropped it is 0.071. Among all tagged neurons (reading a) PT is not significant (0.600, P = 0.089) while IT stays far from it (P = 0.58). The outcome depends on which neurons enter, which the paper does not say; the Methods' compile script in the data set uses the selective ones.''',
'fig3f-late-contra-selectivity-pt': '''**Result: not reproduced.** Over the 570 ms before the cue, the PT spike rate modulation is 34.4% of the window rate (P = 0.027), the paper's value, and the IT modulation -16.4% (P = 0.11, not significant; the paper has -19%). But all task-selective neurons show 9.2% (P = 0.024), significant where the paper has 8% with P = 0.13, so the pattern of significance does not hold in this window under any reading. Over the window to the end of the response epoch, all task-selective neurons are not significant (0.18%, P = 0.96) but neither is PT (20.6%, P = 0.068). The PT contra-selectivity stays significant only from 310 ms before the cue (reading a) and is first significant 2,480 ms before it (reading b), against the paper's 570 ms.''',
'contra-ipsi-selectivity-forms': '''**Result: partially reproduced.** Contra-preferring neurons are a slight majority of the neurons with the largest rate differences (0.535 of the top quarter, 228 neurons, binomial p = 0.32; 0.522 of the top tenth, p = 0.75). Contra-suppression in ipsi-preferring neurons (0.365) is not more common than ipsi-suppression in contra-preferring neurons (0.389, Fisher p = 0.49); the whole pre-sample baseline gives the same (0.367 against 0.391). The first part holds weakly and the second does not.''',
}
order = list(R.keys())
for cid, txt in R.items():
    tag = f'#%% code tags=claim:{cid}\n'
    i = s.index(tag)
    j = s.index('\n#%% ', i + len(tag))
    s = s[:j] + '\n#%% md\n' + txt + s[j:]
open('cells.py','w').write(s)
EOF
grep -c "Result:" cells.py
```

```
17
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/response r = -0.44 to -0.50, P < 1e-20)/response r = -0.44 to -0.50, printed P < 0.0001)/' cells.py && cd entries/crcns-alm-1-li-2015 && cat > requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: crcns-alm-1-li-2015
type: reproduction
title: A motor cortex circuit for motor planning and movement (Li et al. 2015)
description: Tests the electrophysiology findings of Li, Chen, Guo, Gerfen and Svoboda (2015) on
  CRCNS data set alm-1, which holds 1,408 units recorded in left ALM of 19 mice over 99 sessions
  of a delayed tactile discrimination task, with PT and IT neurons identified by antidromic
  tagging. It tests trial-type selectivity and its time course, response categories, error
  trials, contra and ipsi preference, fast-spiking neurons, antidromic latencies, and the
  contralateral selectivity of PT neurons. The photoinhibition and photoactivation behaviour,
  the imaging and the anatomy are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_li_2015.ipynb
  title: Reproducing Li et al. (2015) from CRCNS alm-1
  runtime_minutes: 8
helpers:
- alm.py
related:
- id: crcns:alm-1/unversioned
  relation: uses_data
- id: doi:10.1038/nature14178
  relation: reproduces
EOF
sed -n 30,70p schemas/entry.schema.json
```

```
"runtime_minutes": {"description": "Roughly how long it takes to run.", "type": "integer", "minimum": 1}
        }
      }
    },
    "helpers": {
      "description": "Python modules in the entry that the notebooks import.",
      "type": "array",
      "items": {"type": "string", "pattern": "\\.py$"}
    },
    "related": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["id", "relation"],
        "properties": {
          "id": {
            "description": "A dataset as <archive>:<id>[/<version>] (dandi:000003/0.220126.1855), doi:<doi>, or entry:<name>.",
            "type": "string",
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat >> cells.py <<'EOF'

| claim | outcome |
|---|---|
| fig1d-photoinhibition-ipsilateral-bias | blocked, data missing |
| fig1d-sample-epoch-smaller-bias | blocked, data missing |
| task-performance | reproduced (19 of 42 mice) |
| unit-counts | partially reproduced |
| fig2-selective-fraction | reproduced |
| fig2d-response-categories | reproduced (figure reading) |
| fig2c-selectivity-time-course | reproduced |
| fig2c-dynamic-single-neurons | reproduced (assumed 0.5 bound) |
| ed2-error-trials-predict-choice | reproduced |
| fig2e-equal-contra-ipsi | reproduced |
| ed1-no-population-contra-bias | reproduced |
| ed1-fast-spiking-properties | partially reproduced |
| tagging-counts | reproduced |
| antidromic-latency-jitter | reproduced (assumed window) |
| ed5g-it-second-pulse-jitter | reproduced |
| fig3ei-both-types-preparatory-and-movement | reproduced |
| fig3fj-contra-preferring-pt-not-it | reproduced (selective neurons) |
| fig3f-late-contra-selectivity-pt | not reproduced |
| reaction-time | not reproduced (assumed detection rule) |
| fig4-imaging-intermingled | blocked, data missing |
| fig4h-imaging-pt-contra-bias | blocked, data missing |
| imaging-overall-counts | blocked, data missing |
| contra-ipsi-selectivity-forms | partially reproduced |
| fig5-pt-activation-contralateral-bias | blocked, data missing |
| ed6b-pt-dose-response | blocked, data missing |
| ed6d-it-activation-inconsistent | blocked, data missing |
| ed3-high-power-contralateral-licking | blocked, data missing |
| ed3d-non-overlapping-it-pt | blocked, data missing |
| ed7-pt-stimulation-persistent-activity | blocked, data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's. Only the 19 electrophysiology mice are in the data
set, so task performance and reaction time are measured on them alone. Where the paper leaves a
detail open, the data set's own MATLAB scripts were followed and the choice is stated: the
response epoch of 1.3 s, the exclusion of lick early and axonal stimulation trials, each
unit's trials limited to its recorded span, preference from the counts from sample onset to the
end of the response epoch. The paper gives no rule for telling antidromic from spontaneous
spikes, nor for detecting the first mouth movement in the lick trace; both are assumptions here,
shown under several readings. Spike widths are recomputed from the deposited 29-sample
waveforms.

What was found about the data set. The electrophysiology matches the paper closely: 1,408 units,
19 mice, 99 sessions, the labels' 1,245 pyramidal, 124 FS, 45 PT and 27 IT neurons, and the
paper's 912 selective neurons, response categories and contra and ipsi counts are recovered
exactly. The data set's description lists photostimulation types 0, 1, 2 and NaN; types 3, 4
and 5 also occur (IT tagging in the Tlx x Ai32 mice). 43 trials of type 0 in session
ANM210862_20130627 carry light pulses. The trough-to-peak widths of the deposited waveforms put
34 of the 39 unlabelled units below 0.35 ms, so the "intermediate" class cannot be recomputed.
The activated (non-collision) neurons are not labelled. The lick trace differs in baseline,
scale and sign between sessions and is not described beyond "licking movement from
photodiode". 10 units have spike times out of order. The NWB copies omit the photostimulation
type, the AOM and laser traces and `GoodTrials`. The behaviour, imaging and anatomy of
Figs 1, 4 and 5 and ED Figs 3, 6 and 7 are not in the data set.
EOF
python build.py nb entries/crcns-alm-1-li-2015/reproduce_li_2015.ipynb && cd  && python -c "import yaml,jsonschema,nbformat" 2>&1; . $TMPDIR/dev/bin/activate; python tools/entry.py lock entries/crcns-alm-1-li-2015 2>&1 | tail -5
```

```
wrote entries/crcns-alm-1-li-2015/requirements.lock.txt
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && date -u && time python tools/entry.py all entries/crcns-alm-1-li-2015 2>&1 | tail -30
```

```
Sat Nov  7 21:45:37 UTC 2026
Installed kernelspec registry-crcns-alm-1-li-2015 in executed/crcns-alm-1-li-2015/.venv/share/jupyter/kernels/registry-crcns-alm-1-li-2015
0 error(s)
pass  reproduce_li_2015.ipynb  (251 s)

real	4m19.611s
user	5m30.063s
sys	1m15.250s
```

**Agent calls Bash**

```bash
ls executed/crcns-alm-1-li-2015/ && python -c "
import nbformat
nb=nbformat.read('executed/crcns-alm-1-li-2015/reproduce_li_2015.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    tag=c.metadata.get('tags',[''])[0]
    txt=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
    err=[o for o in c.outputs if o.output_type=='error']
    if err: print('ERROR in',tag)
    if tag in ('claim:reaction-time','claim:task-performance','claim:fig3f-late-contra-selectivity-pt','claim:fig2c-selectivity-time-course','claim:antidromic-latency-jitter') or tag=='sanity':
        print('=====',tag); print(txt[:3000])
" | grep -v "^  [0-9a-f]\{32\}"
```

```
reproduce_li_2015.ipynb
result.json
===== sanity
MD5 sums on the bucket now (compare with the header):
           sessions  units  trials     strain                gene photostim_location
ANM210861         3     58    1290       kj18            sim1-cre           PONS/ALM
ANM210862         3     53     971       kj18            sim1-cre           PONS/ALM
ANM210863         3     90    1031       kj18            sim1-cre           PONS/ALM
ANM214427         4     26    1485      kl100            rbp4-cre       ALM/PONS/ALM
ANM214429         4     48    2051      kl100            rbp4-cre       ALM/PONS/ALM
ANM214430         4     42    1245      kl100            rbp4-cre       ALM/PONS/ALM
ANM218453         5     54    1566  pl56/ai32   tlx-cre/chr2-eyfp                   
ANM218457         6    118    1906  pl56/ai32   tlx-cre/chr2-eyfp                   
ANM218693         3     59    1022  kj18/ai32  sim1-cre/chr2-eyfp                   
ANM219030         5     57    1676       kj18            sim1-cre           PONS/ALM
ANM219031         5     93    1487       kj18            sim1
===== sanity
Trials: 31439

PhotostimulationType (description: 0 none, 1 PT axonal, 2 IT axonal, NaN do not analyse):
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('cells.py').read()
txt='''**Result: not reproduced, resting on an assumed detection rule.** The paper does not say how the first mouth movement is detected. With onset at 5% of the trial's peak excursion, the mean over the 19 mice of per-mouse mean reaction times is 81.7 ms (s.d. 56.9 ms) on correct trials and 100.7 ms on all responses; higher fractions give 99.9 to 188.5 ms. None is within 61.1 ± 10.5 ms. The variant of per-mouse medians gives 68.2 ms at 5%, within the tolerance, and 84.5 to 142.8 ms at higher fractions. Per-mouse means at 10% range from 22.1 to 287.6 ms, and the spread across mice (s.d. 51 to 65 ms) is five to six times the paper's 10.5 ms, which points at differences in the lick trace between sessions (baselines 0.07 to 4.83 V, peak excursions of either sign) more than in the mice.'''
tag='#%% code tags=claim:reaction-time\n'
i=s.index(tag); j=s.index('\n#%% ', i+len(tag))
s=s[:j]+'\n#%% md\n'+txt+s[j:]
s=s.replace('''The labels give 1,173 pyramidal, 45 pyramidal and PT''','''In 3,707 of 28,465 performing trials the sample or delay epoch differs from 1.3 s by more than
50 ms (1,859 of them correct trials without stimulation); epoch rates divide by each trial's
own epoch length, so these trials are kept. 10 units, 7 of them from one session, have spike
times out of order; every measure here bins or sorts spikes, so this does not change them.

The labels give 1,173 pyramidal, 45 pyramidal and PT''')
open('cells.py','w').write(s)
EOF
grep -c "Result:" cells.py; . dev/bin/activate; python build.py nb entries/crcns-alm-1-li-2015/reproduce_li_2015.ipynb
```

```
18
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-alm-1-li-2015/README.md",
 "content": "# Li, Chen, Guo, Gerfen & Svoboda (2015) from CRCNS alm-1\n\nTests the findings of [Li et al. (2015)](https://doi.org/10.1038/nature14178) that can be tested\non CRCNS data set [alm-1](https://doi.org/10.6080/K0RF5RZT), which holds the extracellular\nrecordings of Figures 2 and 3: 1,408 units from left ALM of 19 mice over 99 sessions, with\npyramidal, FS, PT and IT labels, trial types, epoch times, and the lick and photostimulation\ntraces. The photoinhibition and photoactivation behaviour, the calcium imaging and the anatomy\nare not in it.\n\n| Claim | Outcome |\n|---|---|\n| Mean performance 78.4% correct, fewer than 13% early responses | Reproduced (19 of 42 mice) |\n| 1,408 units; 1,245 pyramidal, 124 FS, 39 intermediate by spike width | Partially reproduced |\n| 73% (912/1,245) of pyramidal neurons are selective | Reproduced |\n| 219 preparatory, 389 and 304 peri-movement categories | Reproduced (figure's reading) |\n| Selectivity emerges in the sample epoch, grows, peaks after the cue | Reproduced |\n| Dynamic single neurons, stable population selectivity | Reproduced |\n| Activity on error trials follows the lick | Reproduced |\n| Equal numbers of contra- and ipsi-preferring neurons | Reproduced |\n| No contralateral bias in the population spike count | Reproduced |\n| FS neurons fire more at baseline and are less selective | Partially reproduced |\n| 45 PT and 27 IT neurons passed the collision test | Reproduced |\n| Antidromic latency and jitter of PT and IT neurons | Reproduced (assumed window) |\n| IT neurons have less jitter on the second pulse | Reproduced |\n| PT and IT neurons both preparatory and movement-related | Reproduced |\n| Contra-preferring neurons outnumber ipsi among PT, not IT | Reproduced (selective neurons) |\n| Late contralateral selectivity in PT neurons, from 570 ms before the cue | Not reproduced |\n| Reaction time 61.1 ± 10.5 ms | Not reproduced (assumed detection rule) |\n| Large differences in contra-preferring neurons, contra-suppression in ipsi-preferring | Partially reproduced |\n| Photoinhibition, photoactivation, imaging and anatomy (eleven claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe data set's own labels and trial tables reproduce the paper's counts of selective neurons,\nresponse categories and contra and ipsi preference exactly. The attempt record, with the\nreasons and the differences from the paper's method, is\n[`attempts/crcns-alm-1-li-2015-01.yaml`](../../attempts/crcns-alm-1-li-2015-01.yaml).\n\n- `reproduce_li_2015.ipynb`: the analysis. It takes about five minutes, most of it streaming\n  about 14 GB of session files from the CRCNS bucket.\n- `alm.py`: streaming and reducing the session files, the unit table of epoch rates and\n  selectivity tests, and the antidromic latency measures. Other notebooks on this data set can\n  import it.\n"
}
```

```
File created successfully at: entries/crcns-alm-1-li-2015/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && date -u && python tools/entry.py all entries/crcns-alm-1-li-2015 2>&1 | tail -4
```

```
Sat Nov  7 21:50:25 UTC 2026
Installed kernelspec registry-crcns-alm-1-li-2015 in executed/crcns-alm-1-li-2015/.venv/share/jupyter/kernels/registry-crcns-alm-1-li-2015
0 error(s)
pass  reproduce_li_2015.ipynb  (239 s)
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('executed/crcns-alm-1-li-2015/reproduce_li_2015.ipynb',4)
for c in nb.cells:
    tag=c.metadata.get('tags',[''])[0] if c.cell_type=='code' else ''
    if tag in ('claim:fig2e-equal-contra-ipsi','claim:fig3fj-contra-preferring-pt-not-it','claim:ed5g-it-second-pulse-jitter','claim:contra-ipsi-selectivity-forms','claim:ed2-error-trials-predict-choice'):
        print(tag, ''.join(o.get('text','') for o in c.outputs)[:900])
"
```

```
claim:ed2-error-trials-predict-choice                       reading    epoch  neurons       r      p  fraction_switched  n_nonzero  holds
             min 1 error each   sample      843 -0.0848 0.0138             0.5072        830   True
             min 1 error each    delay      843 -0.4345 0.0000             0.5713        828   True
             min 1 error each response      843 -0.5020 0.0000             0.6267        833   True
             min 5 error each   sample      592 -0.0981 0.0170             0.5239        586   True
             min 5 error each    delay      592 -0.4796 0.0000             0.5873        584   True
             min 5 error each response      592 -0.4428 0.0000             0.6444        585   True
script: >10 correct, >5 error   sample      496 -0.1227 0.0062             0.5244        492   True
script: >10 correct, >5 error    delay      496 -0.4595 0.0000             0.6041        490   True

claim:fig2e-equal-contra-ipsi          reading  contra  ipsi  fraction_contra  P_more_contra  counts_ok  no_more_contra
  a total counts     427   485           0.4682         0.9695       True            True
b 10-trial split     436   444           0.4955         0.6036       True            True

Per mouse, reading a, fraction contra-preferring: {'ANM210861': 0.1, 'ANM210862': 0.52, 'ANM210863': 0.42, 'ANM214427': 0.28, 'ANM214429': 0.5, 'ANM214430': 0.52, 'ANM218453': 0.48, 'ANM218457': 0.42, 'ANM218693': 0.38, 'ANM219030': 0.36, 'ANM219031': 0.51, 'ANM219033': 0.49, 'ANM219036': 0.45, 'ANM219037': 0.53, 'ANM219038': 0.39, 'ANM219247': 0.67, 'ANM219248': 0.55, 'ANM219253': 0.49, 'ANM221977': 0.55}
Binomial test against 0.5 (variant), reading a: p = 0.059

claim:ed5g-it-second-pulse-jitter    IT trials  window_ms  neurons  mean_jitter_first  mean_jitter_second  fraction_decrease  wilcoxon_p  dropped_few_responses  holds
   IT type 2        0.5       19             0.2038              0.1562             0.8421      0.0124                      
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));p=s['properties']
print(json.dumps(p['findings'])[:1500]); print(json.dumps(p.get('inputs'))[:600]); print([k for k in p])"
```

```
{"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\").", "enum": ["on_prompt"]}}}}
{"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
```

**Agent calls Write**

```json
{
 "file_path": "attempts/crcns-alm-1-li-2015-01.yaml",
 "content": "schema_version: 2\nid: crcns-alm-1-li-2015-01\ndataset:\n  archive: crcns\n  id: alm-1\n  version: unversioned\n  doi: 10.6080/K0RF5RZT\npaper: doi:10.1038/nature14178\ndate: 2026-11-07\nentry: crcns-alm-1-li-2015\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42414841408\noutcomes:\n- claim: fig1d-photoinhibition-ipsilateral-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The photoinhibition behaviour (VGAT-ChR2-EYFP and PV-ires-Cre x ReaChR mice) is not in\n    the data set, which holds only the 19 electrophysiology mice; its trials carry axonal\n    tagging stimulation, not ALM photoinhibition. The data description names no other deposit,\n    and none was found on CRCNS.\n- claim: fig1d-sample-epoch-smaller-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Same data as fig1d-photoinhibition-ipsilateral-bias, not in the data set.\n- claim: task-performance\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:task-performance\n  measured: 76.84\n  notes: Control trials, mean over sessions (reading a), 76.84% correct and 10.88% lick early\n    trials; over mice 76.37% and 14.06%; pooled 77.28% and 12.59%. With all trials 75.81% to\n    76.58% correct. Every reading puts the per cent correct within 78.4 +/- 7.84; the lick early\n    fraction is below 14.3% under every reading but the mean over mice with all trials (14.71%).\n    Per mouse 60.4% to 87.0% correct.\n  deviations:\n  - Measured on the 19 electrophysiology mice in the data set; the paper's figure is over 42\n    mice, and the behaviour-only mice are not deposited.\n  - No-lick trials are left out of the denominator, as the data set's Demo_get_performance.m\n    does; the Methods say only that lick early trials are excluded.\n- claim: unit-counts\n  outcome: partially_reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:unit-counts\n  measured:\n  - 1408\n  - 1245\n  - 158\n  - 5\n  notes: 1,408 units, 19 mice, 99 sessions. The trough-to-peak widths of the deposited mean\n    waveforms (the criterion's measure) give 1,245 units above 0.45 ms, 158 below 0.35 ms and 5\n    in between, so the FS and intermediate counts are outside tolerance; 34 of the 39 units\n    without a label have widths below 0.35 ms. A spline-interpolated variant gives 1,241, 158\n    and 9. The data set's cellType labels give exactly 1,245 pyramidal, 124 FS and 39 unlabelled\n    units, so the paper's classification is in the labels but cannot be recomputed from the\n    deposited waveforms.\n  deviations:\n  - Waveforms are the deposited 29-sample snippets at 19531.25 Hz, so widths come in steps of\n    0.0512 ms; the paper does not say whether its widths were interpolated.\n- claim: fig2-selective-fraction\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:fig2-selective-fraction\n  measured:\n  - 0.7325\n  - 912\n  notes: With lick early trials dropped and a 1.3 s response epoch, 912 of 1,245 pyramidal\n    neurons (73.25%) are selective, exactly the paper's count. The other readings give 910 to\n    950; Welch's test 903 to 947. All within tolerance. Per mouse 0.417 to 0.852.\n  deviations:\n  - Trials with axonal photostimulation (types 1 to 5 and NaN) and trials with GoodTrials 0 are\n    left out, and each unit's trials are limited to the span from its first to its last trial\n    with a spike, as the data set's analysis_compile_all_data.m does; the paper does not state\n    either.\n- claim: fig2d-response-categories\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:fig2d-response-categories\n  measured:\n  - 219\n  - 304\n  - 389\n  notes: 219 preparatory only, 389 with both and 304 peri-movement only, exactly the figure's\n    reading (b), under the main readings; the text's reading (a), 389 peri-movement only and 304\n    both, does not match under any reading of the response epoch or lick early trials. Measured\n    values are given in the order of the expected values (preparatory only, peri-movement only,\n    both).\n  deviations:\n  - The text and Fig. 2d disagree on which of 389 and 304 is the peri-movement-only count; the\n    data match the figure (recorded as a paper inconsistency).\n- claim: fig2c-selectivity-time-course\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:fig2c-selectivity-time-course\n  notes: Significant neurons in 200 ms windows, 60 before sample onset (shuffled labels median\n    54), 246 at the end of the sample, 298 and 379 at the start and end of the delay, peak 554 at\n    0.19 s after the cue. Population selectivity of 880 selective neurons with at least 11\n    trials of each type, 0.005, 1.19, 1.46 and 2.28 spikes/s at those times, peak 3.38 at 0.20 s.\n    All three conditions hold for both measures under both readings.\n  deviations:\n  - The 10 trials that set each neuron's preference are drawn at random with a fixed seed; the\n    preference uses spike counts from sample onset to the end of the response epoch, as the data\n    set's compile script does. Neurons need 11 trials of each type for the split (848 with more\n    than 15, as the script requires, give the same).\n- claim: fig2c-dynamic-single-neurons\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_li_2015.ipynb\n  output: claim:fig2c-dynamic-single-neurons\n  notes: Mean population response correlation with the cue-time vector over the sample epoch\n    and the first 0.5 s of the delay is -0.168 (reading a) and -0.159 (reading b); -0.041 and\n    -0.084 with division by the s.d. Population selectivity stays above 0 from the end of the\n    sample epoch through the delay (minimum 1.19 spikes/s).\n  deviations:\n  - The 0.5 bound is the claims file's assumption read from Fig. 2c; the paper gives no\n    threshold.\n- claim: ed2-error-trials-predict-choice\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:ed2-error-trials-predict-choice\n  notes: Pearson's r between correct and error selectivity is negative in every epoch under both\n    readings and the script's selection; sample -0.085 to -0.123 (P 0.006 to 0.017), delay -0.43\n    to -0.48, response -0.44 to -0.50 (printed P < 0.0001). The fraction of neurons switching\n    sign is 0.507 to 0.652, above one half in all epochs; in the sample epoch the effect is\n    weak. 69 of 912 selective neurons have no error trials of one type.\n- claim: fig2e-equal-contra-ipsi\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:fig2e-equal-contra-ipsi\n  measured:\n  - 427\n  - 485\n  notes: 427 contra-preferring and 485 ipsi-preferring selective pyramidal neurons by total\n    counts (reading a), the Fig. 2c counts exactly; bootstrap P for more contra-preferring\n    neurons 0.97. With the 10-trial split 436 and 444 (P = 0.60). A binomial test against 0.5\n    gives p = 0.059.\n- claim: ed1-no-population-contra-bias\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:ed1-no-population-contra-bias\n  notes: Mean lick right minus lick left rate, 0.090 spikes/s for selective pyramidal neurons\n    (P = 0.44), 0.061 for all pyramidal (P = 0.48), 0.071 for all units (P = 0.39); not\n    significant under any reading. The paper reports P = 0.13.\n- claim: ed1-fast-spiking-properties\n  outcome: partially_reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:ed1-fast-spiking-properties\n  notes: FS baseline rates are higher under both readings (mean 9.03 against 3.97 spikes/s,\n    median 6.40 against 2.37). FS are not less selective under either criterion reading - 79.8%\n    selective against 73.3%, mean absolute rate difference 2.29 against 1.53 spikes/s. Only the\n    rate difference relative to the mean rate, a variant the criterion does not name, makes FS\n    less selective (median 0.21 against 0.33). The baseline half holds, the selectivity half\n    does not.\n- claim: tagging-counts\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:tagging-counts\n  measured:\n  - 45\n  - 27\n  notes: The labels give 45 PT neurons (8 mice) and 27 IT neurons (7 mice), the paper's counts.\n    The activated neurons that failed the collision test (22 and 106) and the 7 untestable ones\n    carry no label, so those counts cannot be reported; only two values are measured.\n- claim: antidromic-latency-jitter\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_li_2015.ipynb\n  output: claim:antidromic-latency-jitter\n  measured:\n  - 2.675\n  - 5.002\n  - 0.113\n  - 0.198\n  - 0.14\n  notes: First pulses, spikes within +/-0.5 ms of each neuron's modal latency. PT 2.675 ms and\n    0.113 ms jitter (45 neurons); IT 5.00 ms and 0.198 ms (21 neurons with type 2 trials), or\n    4.58 ms and 0.177 ms with types 2 to 5 (27 neurons); tagged mean jitter 0.140 (0.137). All\n    within tolerance; PT shorter than IT. With +/-1 ms the PT values hold (2.672, 0.126) but the\n    IT jitter is 0.27 to 0.31 ms and the tagged mean 0.18 ms, outside tolerance. The measured\n    values are PT latency, IT latency, PT jitter, IT jitter and tagged jitter; the four\n    activated-neuron values cannot be computed, as those neurons are not labelled.\n  deviations:\n  - The paper does not say how antidromic spikes are told from spontaneous ones. Assumed - the\n    first spike within 10 ms of a pulse, kept when within +/-0.5 ms of the neuron's modal\n    latency (0.2 ms bins); +/-1 ms is shown and changes the IT jitter. The narrower window is\n    adopted because the paper's jitter values (0.1 to 0.2 ms) describe spikes locked to the\n    pulse, and a wider window admits spontaneous spikes.\n  - Pulse onsets are read from the AOM input trace at 10 kHz, so they are quantised to 0.1 ms,\n    and any delay between the AOM input and the light is not known.\n  - IT tagging trials are type 2; types 3 to 5, undocumented, are included as a variant.\n- claim: ed5g-it-second-pulse-jitter\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:ed5g-it-second-pulse-jitter\n  notes: Mean IT jitter is lower for the second pulse in all four variants (type 2 trials,\n    +/-0.5 ms, 0.156 against 0.204 ms; types 2 to 5, +/-1 ms, 0.232 against 0.280 ms), and 65% to\n    87% of IT neurons decrease (Wilcoxon p 0.004 to 0.098). 4 to 8 IT neurons with fewer than\n    three responses to a pulse are left out.\n  deviations:\n  - Antidromic spikes are selected as in antidromic-latency-jitter.\n- claim: fig3ei-both-types-preparatory-and-movement\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:fig3ei-both-types-preparatory-and-movement\n  notes: Selective PT neurons 7 preparatory only, 16 both, 15 peri-movement only of 38 (0.184,\n    0.421, 0.395; Fig. 3e about 0.18, 0.43, 0.40); selective IT neurons 5, 13, 5 of 23 (0.217,\n    0.565, 0.217; Fig. 3i about 0.22, 0.56, 0.22). Both populations hold both kinds under every\n    reading.\n- claim: fig3fj-contra-preferring-pt-not-it\n  outcome: reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:fig3fj-contra-preferring-pt-not-it\n  notes: Selective neurons (reading b), lick early dropped, 1.3 s response epoch; PT 24 of 38\n    contra-preferring (0.632, P = 0.033), IT 10 of 23 (0.435, P = 0.74, the paper's value). With\n    lick early kept PT P = 0.014; with a 1.5 s response epoch and lick early dropped P = 0.071.\n    All tagged neurons (reading a) give PT 27 of 45 (0.600, P = 0.089) and IT P = 0.58, so the\n    PT part does not hold under reading a. The data set's IT_PT script uses the selective\n    neurons.\n- claim: fig3f-late-contra-selectivity-pt\n  outcome: not_reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:fig3f-late-contra-selectivity-pt\n  measured:\n  - 310\n  - 34.4\n  - -16.4\n  - 9.2\n  notes: Over the 570 ms before the cue, PT modulation is 34.4% of the window rate (P = 0.027),\n    the paper's value, and IT -16.4% (P = 0.11), but all task-selective neurons give 9.2% with P\n    = 0.024, significant where the paper has P = 0.13. Over the window to the end of the\n    response epoch all task-selective neurons are not significant (P = 0.96) but neither is PT\n    (20.6%, P = 0.068). No combination of readings gives the paper's pattern of significance.\n    The PT contra-selectivity stays significant from 310 ms before the cue (reading a; first\n    significant 2,480 ms before, reading b), against 570 ms. The PT and IT part of the claim\n    holds in the pre-cue window; the comparison with all selective neurons and the onset do\n    not.\n- claim: reaction-time\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_li_2015.ipynb\n  output: claim:reaction-time\n  measured: 81.66\n  notes: Mean over 19 mice of per-mouse mean reaction times, correct trials, onset at 5% of the\n    trial's peak excursion of the lick trace, 81.7 ms (s.d. 56.9); 99.9 to 176.8 ms at 10% to\n    50%; 100.7 to 188.5 ms on all responses. None within 61.1 +/- 10.5. The variant of per-mouse\n    medians gives 68.2 ms at 5%, within tolerance, and 84.5 to 142.8 ms at higher fractions. The\n    spread across mice (s.d. 51 to 65 ms) is five to six times the paper's, and per-mouse means\n    at 10% range from 22.1 to 287.6 ms, which points to session-to-session differences in the\n    lick trace.\n  deviations:\n  - The paper does not say how the first movement is found in the photodiode trace, and the\n    trace's baseline (0.07 to 4.83 V), scale and sign differ between sessions. Assumed - onset\n    when the trace has moved from its pre-cue median by a fraction (5%, 10%, 25% or 50%) of its\n    largest excursion in the 1 s after the cue. Every fraction gives the same outcome on the\n    per-mouse means the criterion names.\n  - Measured on the 19 electrophysiology mice; the paper's mice for this number are not stated.\n- claim: fig4-imaging-intermingled\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The two-photon calcium imaging (4 C57Bl/6Crl mice, 59 fields of view) is not in the\n    data set, which holds only extracellular recordings; the paper names no deposit of it.\n- claim: fig4h-imaging-pt-contra-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Imaging data not in the data set (see fig4-imaging-intermingled).\n- claim: imaging-overall-counts\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Imaging data not in the data set (see fig4-imaging-intermingled).\n- claim: contra-ipsi-selectivity-forms\n  outcome: partially_reproduced\n  notebook: reproduce_li_2015.ipynb\n  output: claim:contra-ipsi-selectivity-forms\n  notes: Contra-preferring neurons are 0.535 of the top quarter of absolute rate differences (228\n    neurons, binomial p = 0.32) and 0.522 of the top tenth (p = 0.75), a slight majority.\n    Contra-suppression in ipsi-preferring neurons (0.365) is not more frequent than\n    ipsi-suppression in contra-preferring neurons (0.389, Fisher p = 0.49); the whole\n    pre-sample baseline gives 0.367 against 0.391. The first part holds weakly, the second does\n    not.\n  deviations:\n  - The paper does not define a large difference or contra-suppression; the claims file's\n    readings are used, with the 0.5 s before sample onset as baseline (the data set's compile\n    script's baseline) and the whole pre-sample period as a variant.\n- claim: fig5-pt-activation-contralateral-bias\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The photoactivation behaviour of 7 Sim1_KJ18-Cre x Ai32 and 7 Tlx_PL56-Cre x Ai32 mice\n    is not in the data set. Its one Sim1 x Ai32 mouse (ANM218693) has only trials of type NaN\n    (\"do not analyse\") with eight 1 ms pulses at about 23 mW, not the 20 Hz trains of 2 ms\n    pulses of Fig. 5.\n- claim: ed6b-pt-dose-response\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photoactivation behaviour not in the data set (see fig5-pt-activation-contralateral-bias).\n- claim: ed6d-it-activation-inconsistent\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photoactivation behaviour not in the data set (see fig5-pt-activation-contralateral-bias).\n- claim: ed3-high-power-contralateral-licking\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The high-power photostimulation of trained and untrained mice and of vibrissal motor\n    cortex is not in the data set.\n- claim: ed3d-non-overlapping-it-pt\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The retrograde tracer anatomy is not in the data set.\n- claim: ed7-pt-stimulation-persistent-activity\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The recordings with somatic PT photoactivation during the sample epoch (2 mice, 8\n    sessions, 91 neurons) are not identified in the data set. Its photostimulation types are\n    axonal tagging (1 and 2), undocumented types 3 to 5 (pulses at 1.8 to 2.8 s) and NaN (\"do not\n    analyse\"); the only Sim1 x Ai32 mouse has 3 sessions with NaN-type trials of eight 1 ms\n    pulses, not sample-epoch trains, and no behaviour trials with stimulation that would give\n    the ED Fig. 7 conditions.\nfindings:\n- kind: data_missing\n  statement: The data set holds only the electrophysiology of Figures 2 and 3 and Extended Data\n    Figures 1, 2 and 5. The photoinhibition and photoactivation behaviour (Fig. 1, Fig. 5, ED\n    Figs 3 and 6), the calcium imaging (Fig. 4), the anatomy (ED Fig. 3) and the recordings with\n    somatic PT photoactivation (ED Fig. 7) are not in it, and the paper names no other deposit.\n    Eleven of the paper's findings cannot be tested.\n- kind: metadata_insufficient\n  statement: PhotostimulationType takes the values 3, 4 and 5 in 495 trials of the two\n    Tlx_PL56-Cre x Ai32 mice (eight 1 ms pulses at about 23 mW starting 1.8, 2.3 or 2.8 s into the\n    trial), but the data description lists only 0, 1, 2 and NaN. The data set's own compile\n    script treats 1 to 5 as tagging trials.\n- kind: metadata_error\n  statement: In session ANM210862_20130627, 43 trials have PhotostimulationType 0 (\"non-stimulation\n    trials\") but their AOM and laser power traces carry 50 ms light pulses at about 47 mW from 3.2\n    s into the trial.\n- kind: metadata_insufficient\n  statement: Only neurons that passed the collision test are labelled (45 PT, 27 IT). The 22\n    pyramidal-tract-activated and 106 intratelencephalic-activated neurons and the 7 untestable\n    ones are not identified, so their counts, latencies and jitter cannot be checked.\n- kind: other\n  statement: The trough-to-peak widths of the deposited mean waveforms put 34 of the 39\n    unlabelled units below 0.35 ms (158 in all), where the paper and the data description call\n    all 39 intermediate (0.35 to 0.45 ms). The cellType labels match the paper; the widths do not\n    reproduce its intermediate class.\n- kind: format_error\n  statement: 10 units have spike times out of order (7 in session ANM214429_20130806, and\n    ANM219030_20130829 unit 12, ANM219030_20130831 unit 5, ANM219247_20130920 unit 5).\n- kind: metadata_insufficient\n  statement: The lick trace is described only as \"licking movement from photodiode\"; its baseline\n    (0.07 to 4.83 V per session), scale and sign of excursion differ between sessions, and no\n    detection rule or calibration is given, so the paper's reaction time cannot be recomputed\n    reliably.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. How was the reaction time (61.1 +/- 10.5 ms) found\n    from the photodiode trace, with what threshold, which trials and which mice? Detecting the\n    first movement at 5% to 50% of each trial's peak excursion gives per-mouse means of 82 to\n    177 ms on correct trials of the 19 electrophysiology mice (medians 68 to 143 ms).\n- kind: methods_unavailable\n  statement: Question for the paper's authors. How were antidromic spikes told from spontaneous\n    spikes when measuring latency and jitter? Taking spikes within 0.5 ms of each neuron's modal\n    latency gives the paper's values (PT 2.7 ms and 0.11 ms, IT 4.6 to 5.0 ms and 0.18 to 0.20 ms);\n    a 1 ms window gives IT jitter of 0.27 to 0.31 ms.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Do the PT and IT bootstraps of Fig. 3f, j use all\n    tagged neurons or only the selective ones, and which neurons and window give the P = 0.13 for\n    all task-selective neurons in the late contralateral selectivity? With selective neurons PT\n    is significant (P = 0.033) and IT gives P = 0.74 as printed; with all tagged neurons PT gives\n    P = 0.089. Over the 570 ms before the cue all 912 selective neurons give 9.2% modulation with\n    P = 0.024.\n- kind: paper_inconsistency\n  statement: The Results give 389 neurons with peri-movement selectivity only and 304 with both,\n    while Fig. 2d shows about 0.43 with both and 0.33 with peri-movement only. The data give 389\n    with both and 304 peri-movement only, as the figure has.\n- kind: other\n  statement: In 3,707 of 28,465 performing trials the sample or delay epoch differs from 1.3 s by\n    more than 50 ms (up to 14 s), which the data description does not mention. The NWB copies of\n    the sessions omit the photostimulation type, the AOM and laser power traces and GoodTrials,\n    which the analysis needs, so only the MATLAB files support it.\n"
}
```

```
File created successfully at: attempts/crcns-alm-1-li-2015-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/crcns-alm-1-li-2015-01.yaml'; s=open(p).read()
s=s.replace('''  measured:
  - 45
  - 27
''','')
s=s.replace('''  measured:
  - 2.675
  - 5.002
  - 0.113
  - 0.198
  - 0.14
''','')
s=s.replace("carry no label, so those counts cannot be reported; only two values are measured.","carry no label, so those counts cannot be reported, and no measured list is given.")
s=s.replace("""within tolerance; PT shorter than IT. With +/-1 ms the PT values hold (2.672, 0.126) but the
    IT jitter is 0.27 to 0.31 ms and the tagged mean 0.18 ms, outside tolerance. The measured
    values are PT latency, IT latency, PT jitter, IT jitter and tagged jitter; the four
    activated-neuron values cannot be computed, as those neurons are not labelled.""","""within tolerance; PT shorter than IT. With +/-1 ms the PT values hold (2.672, 0.126) but the
    IT jitter is 0.27 to 0.31 ms and the tagged mean 0.18 ms, outside tolerance. The four
    activated-neuron values cannot be computed, as those neurons are not labelled, so no measured
    list is given.""")
s=s.replace("is not in the data set. Its one Sim1 x Ai32 mouse (ANM218693) has only trials of type NaN\n    (\"do not analyse\") with eight 1 ms pulses","is not in the data set. In its one Sim1 x Ai32 mouse (ANM218693) every stimulation trial is of\n    type NaN (\"do not analyse\"), with eight 1 ms pulses")
open(p,'w').write(s)
import yaml,re
d=yaml.safe_load(open(p))
for line in s.splitlines():
    v=line.split(': ',1)[1] if re.match(r'^\s*-?\s*[a-z_]+: ',line) else line
    if ': ' in v: print('COLON',line)
print(len(d['outcomes']))
EOF
grep -n "ANM218693" attempts/crcns-alm-1-li-2015-01.yaml | head -3; . $TMPDIR/dev/bin/activate; python tools/entry.py check entries/crcns-alm-1-li-2015 2>&1 | tail
```

```
29
287:    is not in the data set. In its one Sim1 x Ai32 mouse (ANM218693) every stimulation trial is of
0 error(s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/crcns-alm-1-li-2015-01.yaml'; s=open(p).read()
old=s[s.index("    analyse\"); the only Sim1 x Ai32 mouse has 3 sessions"):s.index("findings:")]
new='''    analyse"); in the only Sim1 x Ai32 mouse (ANM218693, 3 sessions) every stimulation trial is
    of type NaN, with eight 1 ms pulses starting about 2.3 s into the trial, not sample-epoch
    trains. Nothing marks a session or trial as an ED Fig. 7 recording.
'''
s=s.replace(old,new); open(p,'w').write(s)
import yaml; yaml.safe_load(open(p))
EOF
sed -n '/claim: ed7/,/findings:/p' attempts/crcns-alm-1-li-2015-01.yaml; . $TMPDIR/dev/bin/activate; python tools/entry.py check entries/crcns-alm-1-li-2015 2>&1 | tail -2; python tools/entry.py handover entries/crcns-alm-1-li-2015 2>&1 | tail -5; ls executed/crcns-alm-1-li-2015/handover; date -u
```

```
- claim: ed7-pt-stimulation-persistent-activity
  outcome: blocked
  blocked_by: data_missing
  notes: The recordings with somatic PT photoactivation during the sample epoch (2 mice, 8
    sessions, 91 neurons) are not identified in the data set. Its photostimulation types are
    axonal tagging (1 and 2), undocumented types 3 to 5 (pulses at 1.8 to 2.8 s) and NaN ("do not
    analyse"); in the only Sim1 x Ai32 mouse (ANM218693, 3 sessions) every stimulation trial is
    of type NaN, with eight 1 ms pulses starting about 2.3 s into the trial, not sample-epoch
    trains. Nothing marks a session or trial as an ED Fig. 7 recording.
findings:
0 error(s)
wrote executed/crcns-alm-1-li-2015/handover
10.1038-nature14178.yaml
alm.py
reproduce_li_2015.ipynb
Sat Nov  7 21:56:30 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/median 6.40 against 2.37, rank-sum p < 1e-10)/median 6.40 against 2.37, rank-sum p printed as 0.0)/' cells.py && grep -c "printed as 0.0" cells.py && . dev/bin/activate && python build.py nb entries/crcns-alm-1-li-2015/reproduce_li_2015.ipynb && cd  && python tools/entry.py all entries/crcns-alm-1-li-2015 2>&1 | tail -2 && python tools/entry.py handover entries/crcns-alm-1-li-2015 | tail -1; git status --short; date -u
```

```
1
0 error(s)
pass  reproduce_li_2015.ipynb  (245 s)
wrote executed/crcns-alm-1-li-2015/handover
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
?? attempts/crcns-alm-1-li-2015-01.yaml
?? entries/crcns-alm-1-li-2015/
?? scripts
Sat Nov  7 22:01:01 UTC 2026
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('executed/crcns-alm-1-li-2015/handover/reproduce_li_2015.ipynb',4)
print(len(nb.cells), sum('**Result' in c.source for c in nb.cells), any('## Summary' in c.source for c in nb.cells))"; ls entries/crcns-alm-1-li-2015
```

```
47 0 False
README.md
__pycache__
alm.py
entry.yaml
reproduce_li_2015.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/crcns-alm-1-li-2015/__pycache__; git check-ignore -q entries/crcns-alm-1-li-2015/__pycache__ && echo ignored; ls entries/crcns-alm-1-li-2015
```

```
README.md
alm.py
entry.yaml
reproduce_li_2015.ipynb
requirements.in
requirements.lock.txt
```

**Agent**

I've done steps 1 to 6 of the Author protocol for CRCNS alm-1 against Li et al. (2015). Of the 29 claims, 13 are reproduced, 3 partially reproduced and 2 not reproduced; 11 are blocked because their data are not in the data set. The entry passes its checks and runs from a clean environment in about 4 minutes, and the verifier's handover package is built. Nothing is committed.

The files are `entries/crcns-alm-1-li-2015/` (notebook, `alm.py`, `entry.yaml`, `README.md`, requirements and lock file) and `attempts/crcns-alm-1-li-2015-01.yaml`.

**1. Outcomes**

| claim | outcome |
|---|---|
| task-performance | reproduced (only 19 of the paper's 42 mice are in the data set) |
| unit-counts | partially reproduced |
| fig2-selective-fraction | reproduced (912/1,245, exact) |
| fig2d-response-categories | reproduced under the figure's reading (219/389/304, exact) |
| fig2c-selectivity-time-course | reproduced |
| fig2c-dynamic-single-neurons | reproduced, resting on the claims file's assumed 0.5 bound |
| ed2-error-trials-predict-choice | reproduced |
| fig2e-equal-contra-ipsi | reproduced (427/485, exact) |
| ed1-no-population-contra-bias | reproduced |
| ed1-fast-spiking-properties | partially reproduced (baseline holds, "less selective" does not) |
| tagging-counts | reproduced (45 PT, 27 IT) |
| antidromic-latency-jitter | reproduced, resting on an assumed ±0.5 ms window |
| ed5g-it-second-pulse-jitter | reproduced |
| fig3ei-both-types-preparatory-and-movement | reproduced |
| fig3fj-contra-preferring-pt-not-it | reproduced with selective neurons (IT P = 0.74, as printed in the paper); PT P = 0.089 with all tagged neurons |
| fig3f-late-contra-selectivity-pt | not reproduced (PT 34.4% matches, but all task-selective neurons give P = 0.024 and the onset is 310 ms, not 570) |
| reaction-time | not reproduced, resting on an assumed detection rule (82 to 189 ms against 61.1 ± 10.5) |
| contra-ipsi-selectivity-forms | partially reproduced |
| photoinhibition (2), imaging (3), photoactivation (3), ED3 licking, ED3d anatomy, ED7 | blocked, data missing |

**2. Dataset, assumptions, questions**
- **What matches:** 19 mice, 99 sessions, 1,408 units. The cell-type labels and trial tables reproduce the paper's counts exactly.
- **What doesn't:**
  - Photostimulation types 3 to 5 appear in the data but are not in the description.
  - 43 trials marked "no stimulation" in session ANM210862_20130627 carry light pulses.
  - The deposited waveforms put 34 of the 39 "intermediate" units below 0.35 ms.
  - The neurons that failed the collision test are not labelled.
  - 10 units have spike times out of order.
  - The lick trace's level, scale and sign vary between sessions and it is undocumented.
  - The NWB copies lack the photostimulation type, the AOM trace and `GoodTrials`.
  - In 3,707 trials an epoch differs from 1.3 s.
- **Assumptions:**
  - Where the paper is silent I followed the authors' MATLAB scripts in the data set: 1.3 s response epoch, lick-early and axonal-stimulation trials dropped, each unit's trials limited to its recorded span.
  - Antidromic spikes are those within ±0.5 ms of each neuron's modal latency.
  - Reaction time is the first lick-trace movement at a fraction of the trial's peak excursion; four fractions were run.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): how reaction time was detected; how antidromic spikes were told from spontaneous ones; which neurons enter the Fig. 3f/j bootstrap and the P = 0.13 test.
- **Questions to a reader:** none. The claims file already lists both readings of the Fig. 2d text-versus-figure disagreement.

**3. Where the protocol was unclear**
1. `archives.md` describes CRCNS data as zip files. This data set uses one tar.gz per animal, which can only be streamed in sequence (about 14 GB). I streamed each tar and decompressed it in memory, four animals at a time.
2. "Pinned version": CRCNS has none, but the bucket holds `version_1/` and `version_2/` folders that contain only documentation. I used `live`, recorded the version as `unversioned`, and put the MD5 sums in the notebook header.
3. The authors' analysis code ships inside the data set but the paper does not link it, so its rank among the method sources is unclear. I used it as the basis for assumptions and cited it.
4. The data set includes the authors' precomputed results (`ALM_compiled_all_data.mat`). I did not read it, to keep every number computed from the data.
5. `measured` must give one number per expected value, but the activated-neuron values can't be measured. I left `measured` out for tagging-counts and antidromic-latency-jitter and said why in the notes.
6. When a criterion defines no partial outcome but part of the claim holds (ed1-fast-spiking, contra-ipsi-forms), I used the protocol's general definition of partially reproduced.
7. For unit-counts, the criterion's width measure and the data set's labels disagree. I followed the criterion's measure, which gives partial.
8. For fig3fj, the criterion says "under one reading", while step 1.6 says the outcome is what all readings give. I followed the claims file and did not mark it as resting on an assumption; a verifier may disagree.

**4. Runtime and failures**
The work ran from 21:14 to about 22:02 UTC. Nothing failed: the notebook ran in 239 to 251 s per full run, peak memory per worker was about 1.8 GB, and the checks reported 0 errors. The raw voltage traces (about 800 GB) were not read. Untracked dotfiles (`.bashrc`, `.idea` and others) and a `scripts` folder are in the working tree; I did not create them and left them alone.

## End of run

69 turns, 41 minutes, $6.90 at API prices, result: success.
