# 000252 · author · run 41825254986

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/000252 paper entries | head -50
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5b0cb1dd-20d1-4c47-97b4-d6b907f306a5/tool-results/byzypzemo.txt

Preview (first 2KB):
Wed Nov  4 12:02:22 UTC 2026
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

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -400; cat docs/archives.md
```

```
<persisted-output>
Output too large (36.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5b0cb1dd-20d1-4c47-97b4-d6b907f306a5/tool-results/be5bpci2v.txt

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/5b0cb1dd-20d1-4c47-97b4-d6b907f306a5/tool-results/byzypzemo.txt"
}
```

```
1	Wed Nov  4 12:02:22 UTC 2026
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
cat docs/archives.md | head -150; cat claims/000252/*.yaml; ls paper
```

```
<persisted-output>
Output too large (44.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5b0cb1dd-20d1-4c47-97b4-d6b907f306a5/tool-results/bsldiw929.txt

Preview (first 2KB):
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
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000252/*.yaml; ls -la paper
```

```
<persisted-output>
Output too large (35.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5b0cb1dd-20d1-4c47-97b4-d6b907f306a5/tool-results/brdvg882g.txt

Preview (first 2KB):
# Claims for Guan et al., "Compositional coding of individual finger movements in human posterior
# parietal cortex and motor cortex enables ten-finger decoding", on dandiset 000252.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read. The bioRxiv preprint, version 1 (doi:10.1101/2022.12.07.22283227), full text from
# bioRxiv JATS XML (paper/10.1101-2022.12.07.22283227.txt): main text, Methods, figure legends and
# the supplementary figure legends (Supplementary Figures 1 to 11). The contents of Supplementary
# Table 1 (phase durations) and Supplementary Table 2 (session dates) are not in the text, only
# their legends; no claim here rests on their numbers, since every analysis window is defined from
# a phase onset. The equation of the cross-validated Mahalanobis distance (Methods, Neural distance
# between fingers) is lost in the text; its description in words is used. No PDF was supplied.
#
# Code. The paper links no analysis code. It names two Python libraries: the representational
# similarity analysis toolbox (rsatoolbox, ref 57) for cross-validated Mahalanobis distances, and
# DABEST (ref 53) for Hedges' g with bootstrap confidence intervals.
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/5b0cb1dd-20d1-4c47-97b4-d6b907f306a5/tool-results/brdvg882g.txt"
}
```

```
1	# Claims for Guan et al., "Compositional coding of individual finger movements in human posterior
2	# parietal cortex and motor cortex enables ten-finger decoding", on dandiset 000252.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md (Reader).
5	#
6	# Text read. The bioRxiv preprint, version 1 (doi:10.1101/2022.12.07.22283227), full text from
7	# bioRxiv JATS XML (paper/10.1101-2022.12.07.22283227.txt): main text, Methods, figure legends and
8	# the supplementary figure legends (Supplementary Figures 1 to 11). The contents of Supplementary
9	# Table 1 (phase durations) and Supplementary Table 2 (session dates) are not in the text, only
10	# their legends; no claim here rests on their numbers, since every analysis window is defined from
11	# a phase onset. The equation of the cross-validated Mahalanobis distance (Methods, Neural distance
12	# between fingers) is lost in the text; its description in words is used. No PDF was supplied.
13	#
14	# Code. The paper links no analysis code. It names two Python libraries: the representational
15	# similarity analysis toolbox (rsatoolbox, ref 57) for cross-validated Mahalanobis distances, and
16	# DABEST (ref 53) for Hedges' g with bootstrap confidence intervals.
17	#
18	# Dataset. Its archive title is "Finger_RL: human intracortical recordings during attempted finger
19	# movements of right and left hands", and the paper's Data Availability names dandiset 000252. It is
20	# meant to hold the ten-finger (right and left hand) task; whether it also holds the
[... 626 more lines not kept]
```

**Agent**

Claims file read: 19 claims across ten-finger, alternating-cues, and BMI tasks. Next I'll survey the dataset and the example entry.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000252/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000252/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls entries/001453-fouke-2025/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; head -c 3000 attempts/001453-fouke-2025-01.yaml; ls tools
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
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000252/versions/0.230408.2207/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin)
for a in d['results']: print(a['path'], a['size'], a['asset_id'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000252/versions/0.230408.2207/" | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('description')); print(d.get('relatedResource')); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent**

The dataset has 12 small files: sub-P1 with 10 sessions (likely N) and sub-N1 with 2 sessions (likely J). That matches the ten-finger task only. Next I open one file.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "import pynwb, remfile, h5py, sklearn; print(pynwb.__version__)" 2>&1; which uv python; sed -n 1,80p tools/entry.py
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, sklearn; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
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
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy scikit-learn pandas statsmodels rsatoolbox matplotlib dandi 2>&1 | tail -3; python -c "import pynwb, rsatoolbox; print(pynwb.__version__, rsatoolbox.__version__)"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, rsatoolbox; print(pynwb.__version__, rsatoolbox.__version__)
                                                       ^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'rsatoolbox' has no attribute '__version__'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > explore.py <<'EOF'
import remfile, h5py, pynwb, requests
aid="d5bd9c5e-9410-4d58-8684-2c01b1a11b2a"
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers['Location']
f=h5py.File(remfile.File(url),'r')
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print(nwb)
print(nwb.session_description, nwb.experiment_description, nwb.subject)
print(nwb.electrodes.to_dataframe().head()); print(nwb.electrodes.to_dataframe().group_name.value_counts())
print(nwb.trials.to_dataframe().head(20)); print(nwb.trials.colnames)
u=nwb.units; print(u.colnames); ud=u.to_dataframe(); print(ud.head()); print(len(ud))
for c in u.colnames: print(c, u[c].description if hasattr(u[c],'description') else '')
for c in nwb.trials.colnames: print(c, nwb.trials[c].description)
print(nwb.intervals, nwb.acquisition, nwb.processing, nwb.stimulus)
EOF
python explore.py 2>&1 | head -150
```

```
root pynwb.file.NWBFile at 0x137333217879312
Fields:
  devices: {
    NSP1 <class 'pynwb.device.Device'>,
    NSP2 <class 'pynwb.device.Device'>
  }
  electrode_groups: {
    MC <class 'pynwb.ecephys.ElectrodeGroup'>,
    PPC <class 'pynwb.ecephys.ElectrodeGroup'>
  }
  electrodes: electrodes <class 'pynwb.ecephys.ElectrodesTable'>
  epochs: epochs <class 'pynwb.epoch.TimeIntervals'>
  experiment_description: Intracortical recordings during contralateral/ipsilateral finger movement
  experimenter: ['Kelly Kadlec' 'Jorge Gamez']
  file_create_date: [datetime.datetime(2023, 4, 8, 14, 38, 36, 277874, tzinfo=tzoffset(None, -25200))]
  identifier: sub-N1_ses-20191220T133955
  institution: California Institute of Technology
  intervals: {
    epochs <class 'pynwb.epoch.TimeIntervals'>,
    trials <class 'pynwb.epoch.TimeIntervals'>
[... 120 more lines not kept]
```

**Agent**

The data has trials (finger, hand, cue on/off, go times) and sorted units with spike times, which look unsorted. Now I read the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2022.12.07.22283227.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2022.12.07.22283227.txt",
 "offset": 363
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import remfile, h5py, pynwb, requests, numpy as np, pandas as pd
assets=requests.get("https://api.dandiarchive.org/api/dandisets/000252/versions/0.230408.2207/assets/?page_size=100").json()['results']
for a in sorted(assets,key=lambda a:a['path']):
    url=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=False).headers['Location']
    f=h5py.File(remfile.File(url),'r'); nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
    tr=nwb.trials.to_dataframe(); ep=nwb.epochs.to_dataframe()
    u=nwb.units
    groups=[g.name for g in u['electrode_group'][:]]
    st=u['spike_times'].data[:]; idx=u['spike_times_index'].data[:]
    sorted_units=sum(np.all(np.diff(st[(idx[i-1] if i else 0):idx[i]])>=0) for i in range(len(idx)))
    print(a['path'], nwb.session_description,'|', nwb.subject.subject_id, nwb.subject.description, nwb.subject.sex)
    print('  trials',len(tr),'runs',tr.Run.nunique(), 'per finger', tr.finger.value_counts().to_dict())
    print('  units by group', pd.Series(groups).value_counts().to_dict(), 'sorted units', sorted_units, 'of', len(idx))
    print('  epochs', len(ep), ep.head(3).values.tolist())
    d=tr.assign(cue=tr.cue_off_time-tr.cue_on_time, delay=tr.go_on_time-tr.cue_off_time, go=tr.stop_time-tr.go_on_time, iti=tr.cue_on_time-tr.start_time)
    print('  durations', d[['iti','cue','delay','go']].describe().loc[['min','mean','max']].round(2).to_dict())
    print('  spikes range', st.min(), st.max(), 'trials range', tr.start_time.min(), tr.stop_time.max())
    oi=u['obs_intervals'][0]; print('  obs_intervals unit0', oi)
    print('  hand', tr.hand.unique(), 'ftype', tr.finger_type.unique())
EOF
python survey.py 2>&1 | grep -v Warn
```

```
sub-N1/sub-N1_ses-2019-02-12_ecephys.nwb ten-finger press task, with delay | N1 tetraplegic man M
  trials 100 runs 2 per finger {'Lp': 10, 'Rm': 10, 'Rr': 10, 'Lt': 10, 'Li': 10, 'Lm': 10, 'Lr': 10, 'Ri': 10, 'Rp': 10, 'Rt': 10}
  units by group {'PPC': 159, 'MC': 139} sorted units 298 of 298
  epochs 2 [[174.22486966666665, 426.44383633333337, 0.0], [470.72493966666667, 721.8736063333333, 1.0]]
  durations {'iti': {'min': 0.08, 'mean': 1.54, 'max': 1.58}, 'cue': {'min': 1.06, 'mean': 1.07, 'max': 1.08}, 'delay': {'min': 1.06, 'mean': 1.35, 'max': 1.58}, 'go': {'min': 1.07, 'mean': 1.07, 'max': 1.08}}
  spikes range 663 1506328 trials range 174.22486966666665 721.8736063333333
  obs_intervals unit0 [[171.43410333 457.97760333]
 [468.04817333 736.18837333]]
  hand <StringArray>
['L', 'R']
Length: 2, dtype: str ftype <StringArray>
['p', 'm', 'r', 't', 'i']
Length: 5, dtype: str
sub-N1/sub-N1_ses-2019-12-20_ecephys.nwb ten-finger press task, with delay | N1 tetraplegic man M
  trials 100 runs 2 per finger {'Lm': 10, 'Rr': 10, 'Rp': 10, 'Rm': 10, 'Lr': 10, 'Li': 10, 'Lt': 10, 'Ri': 10, 'Rt': 10, 'Lp': 10}
  units by group {'PPC': 160, 'MC': 120} sorted units 280 of 280
  epochs 2 [[163.54532999999998, 502.77273, 0.0], [679.5157443333333, 1017.2529443333333, 1.0]]
  durations {'iti': {'min': 0.04, 'mean': 2.05, 'max': 2.14}, 'cue': {'min': 1.58, 'mean': 1.62, 'max': 1.67}, 'delay': {'min': 0.86, 'mean': 0.99, 'max': 1.14}, 'go': {'min': 2.05, 'mean': 2.08, 'max': 2.12}}
  spikes range 920 1135804 trials range 163.54532999999998 1017.2529443333333
  obs_intervals unit0 [[ 155.54563027  544.9387636 ]
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey2.py <<'EOF'
import remfile, h5py, requests, numpy as np
assets=requests.get("https://api.dandiarchive.org/api/dandisets/000252/versions/0.230408.2207/assets/?page_size=100").json()['results']
sig={}
for a in sorted(assets,key=lambda a:a['path']):
    url=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=False).headers['Location']
    f=h5py.File(remfile.File(url),'r')
    st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]
    oi=f['units/obs_intervals'][:]; oidx=f['units/obs_intervals_index'][:]
    starts=np.r_[0,idx[:-1]]
    uns=sum(np.any(np.diff(st[s:e])<0) for s,e in zip(starts,idx))
    out=0
    for i,(s,e) in enumerate(zip(starts,idx)):
        iv=oi[(oidx[i-1] if i else 0):oidx[i]]
        x=st[s:e]; inside=np.zeros(len(x),bool)
        for a0,b0 in iv: inside|=(x>=a0)&(x<=b0)
        out+=(~inside).sum()
    print(a['path'], 'units',len(idx),'unsorted units',uns,'spikes',len(st),'outside obs',out,'range',st.min().round(2),st.max().round(2), 'dup units', len(idx)-len({tuple(np.round(st[s:e][:20],5)) for s,e in zip(starts,idx)}))
    print('  units cols', list(f['units'].keys()), 'electrodes cols', list(f['electrodes'].keys()))
    sig[a['path']]=(np.sort(st)[:50].round(4), f['intervals/trials/go_on_time'][:].round(4))
ks=list(sig)
for i in range(len(ks)):
    for j in range(i+1,len(ks)):
        if np.array_equal(sig[ks[i]][1],sig[ks[j]][1]) or np.array_equal(sig[ks[i]][0],sig[ks[j]][0]): print('DUP',ks[i],ks[j])
print('dup check done')
EOF
python survey2.py 2>&1 | grep -v Warn; python -c "
import rsatoolbox.rdm.calc as c, inspect; src=inspect.getsource(c); i=src.find('def calc_rdm_crossnobis'); print(src[i:i+4500])"
```

```
sub-N1/sub-N1_ses-2019-02-12_ecephys.nwb units 298 unsorted units 283 spikes 1506328 outside obs 0 range 171.44 736.19 dup units 0
Traceback (most recent call last):
  File "/tmp/claude-1001/survey2.py", line 18, in <module>
    print('  units cols', list(f['units'].keys()), 'electrodes cols', list(f['electrodes'].keys()))
                                                                           ~^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/group.py", line 407, in __getitem__
    return self._get(name)
           ~~~~~~~~~^^^^^^
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/group.py", line 421, in _get
    oid = h5o.open(self.id, self._e(name), lapl=lapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5o.pyx", line 255, in h5py.h5o.open
KeyError: "Unable to synchronously open object (object 'electrodes' doesn't exist)"
def calc_rdm_crossnobis(dataset, descriptor, noise=None,
                        cv_descriptor=None, remove_mean: bool = False):
    """
    calculates an RDM from an input dataset using Cross-nobis distance
[... 95 more lines not kept]
```

**Agent**

Real finding: spike times within units are unsorted (283 of 298 units in the first file). That is a format_error. Counting spikes in windows is unaffected. Rerunning across all files:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i "s/print('  units cols'.*/print('  units cols', list(f['units'].keys()), 'electrodes cols', list(f['general\/extracellular_ephys\/electrodes'].keys()))/" survey2.py && python survey2.py 2>&1 | grep -v Warn; python -c "
import rsatoolbox.rdm.calc as c, inspect; print(inspect.getsource(c._calc_rdm_crossnobis_single))
import rsatoolbox.data.noise as n; print(inspect.signature(n.prec_from_residuals)); print(inspect.signature(n.cov_from_residuals))"
```

```
sub-N1/sub-N1_ses-2019-02-12_ecephys.nwb units 298 unsorted units 283 spikes 1506328 outside obs 0 range 171.44 736.19 dup units 0
  units cols ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index'] electrodes cols ['filtering', 'group', 'group_name', 'id', 'imp', 'location', 'x', 'y', 'z']
sub-N1/sub-N1_ses-2019-12-20_ecephys.nwb units 280 unsorted units 224 spikes 1135804 outside obs 0 range 155.55 1030.7 dup units 0
  units cols ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index'] electrodes cols ['filtering', 'group', 'group_name', 'id', 'imp', 'location', 'x', 'y', 'z']
sub-P1/sub-P1_ses-2015-08-12_ecephys.nwb units 112 unsorted units 101 spikes 199276 outside obs 0 range 276.29 1020.56 dup units 0
  units cols ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index'] electrodes cols ['filtering', 'group', 'group_name', 'id', 'imp', 'location', 'x', 'y', 'z']
sub-P1/sub-P1_ses-2015-08-14_ecephys.nwb units 102 unsorted units 92 spikes 179229 outside obs 0 range 309.6 1054.25 dup units 0
  units cols ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index'] electrodes cols ['filtering', 'group', 'group_name', 'id', 'imp', 'location', 'x', 'y', 'z']
sub-P1/sub-P1_ses-2015-08-17_ecephys.nwb units 119 unsorted units 93 spikes 204194 outside obs 0 range 132.11 814.13 dup units 0
  units cols ['electrode_group', 'electrodes', 'electrodes_index', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index'] electrodes cols ['filtering', 'group', 'group_name', 'id', 'imp', 'location', 'x', 'y', 'z']
sub-P1/sub-P1_ses-2015-08-21_ecephys.nwb units 110 unsorted units 94 spikes 157408 outside obs 0 range 168.17 818.62 dup units 0
  units co
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; mkdir -p entries/000252-guan-2022
```

```
Wed Nov  4 12:05:06 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/000252-guan-2022/fingers.py",
 "content": "\"\"\"Loading and measures for dandiset 000252 (Guan et al., ten-finger press task).\n\nThe dandiset holds the ten-finger press task only: 10 sessions of participant N\n(subject ``P1`` in the files, one PPC array) and 2 sessions of participant J\n(subject ``N1`` in the files, a PPC and an MC array). Files are streamed from the\nDANDI archive at the pinned version ``VERSION``; nothing is written to disk.\n\nWhere each parameter comes from:\n\n- Firing rate is the spike count in a 500 ms window divided by its duration;\n  the Go window starts 200 ms after the Go cue, the Delay window 200 ms after the\n  Delay screen, the Cue window 200 ms after the Cue screen, and the ITI window is\n  the last 500 ms of the ITI (paper, Methods, Feature Extraction). The Delay\n  screen onset is the file's ``cue_off_time`` (the cue disappears at the start of\n  the delay; Methods, Tasks, and Figure 3 legend: \"A delay period separates the\n  Cue phase from a condition-independent Go display\").\n- Neurons with mean rate below 0.5 Hz are excluded (Methods, Feature Extraction).\n  Readings of \"average firing rate\" are claims-file O1: (a) spikes over the whole\n  recorded session (the sum of the unit's ``obs_intervals``); (b) the mean of the\n  Go-window rates over all trials. For (b) the Go window is taken as \"the analysis\n  window\", since every ten-finger analysis uses it (claims file O11); this is a\n  reading of O1 (b), stated as such.\n- The classifier is diagonal-covariance LDA, one per session, stratified 8-fold\n  cross-validation, predictions pooled over sessions (Methods, Offline\n  classification with cross-validation). Fold assignment is claims-file O2: (a) no\n  shuffling, (b) shuffled, seeds 0 to 9. The variance floor of 1e-9 times the\n  largest variance (as scikit-learn's GaussianNB) is a standard choice that only\n  guards against division by zero.\n- Single-neuron selectivity is a one-way ANOVA, Benjamini-Hochberg FDR over the\n  neurons of an array pooled across sessions, eta2 = between-group over total sum\n  of squares (Methods, Single-neuron selectivity).\n- Cross-validated Mahalanobis distances use rsatoolbox (Methods, Neural distance\n  between fingers), which divides by the number of neurons. Readings are\n  claims-file O3 (noise covariance estimator) and O4 (partition).\n- CCGP pseudo-populations and decoders are claims-file O6 and O7; the permutation\n  test uses 1001 label shuffles (Methods, Compositionality of finger\n  representations).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport os\n\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"MKL_NUM_THREADS\", \"1\")\n\nfrom dataclasses import dataclass, field\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET_ID = \"000252\"\nVERSION = \"0.230408.2207\"\nAPI = \"https://api.dandiarchive.org/api\"\n\n# Paper names of the participants and arrays, and the file's subject and group.\nARRAYS = {\"N-PPC\": (\"P1\", \"PPC\"), \"J-PPC\": (\"N1\", \"PPC\"), \"J-MC\": (\"N1\", \"MC\")}\nFINGER_TYPES = [\"t\", \"i\", \"m\", \"r\", \"p\"]\nCONDITIONS = [h + f for h in \"RL\" for f in FINGER_TYPES]  # Rt..Rp, Lt..Lp\n\nWINDOW = 0.5      # s, Methods, Feature Extraction\nOFFSET = 0.2      # s, after the phase onset, Methods, Feature Extraction\nMIN_RATE = 0.5    # Hz, Methods, Feature Extraction\n\n\ndef list_assets() -> list[dict]:\n    \"\"\"Assets of the pinned version, sorted by path.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{VERSION}/assets/?page_size=200\"\n    out = []\n    while url:\n        page = requests.get(url, timeout=60).json()\n        out += page[\"results\"]\n        url = page.get(\"next\")\n    return sorted(out, key=lambda a: a[\"path\"])\n\n\ndef version_metadata() -> dict:\n    return requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{VERSION}/\", timeout=60).json()\n\n\ndef s3_url(asset_id: str) -> str:\n    r = requests.get(f\"{API}/assets/{asset_id}/download/\", allow_redirects=False, timeout=60)\n    return r.headers[\"Location\"]\n\n\n@dataclass\nclass Session:\n    path: str\n    subject: str\n    sex: str\n    date: str\n    description: str\n    trials: pd.DataFrame\n    spikes: list            # one sorted array of spike times per unit (s)\n    group: np.ndarray       # electrode group name per unit\n    obs_duration: np.ndarray  # total observed time per unit (s)\n    n_unsorted: int = 0     # units whose stored spike times are not in time order\n    n_outside_obs: int = 0  # spikes outside the unit's obs_intervals\n    extra: dict = field(default_factory=dict)\n\n\ndef _s(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef load_session(asset: dict) -> Session:\n    \"\"\"Stream one NWB file and keep trials, spike times, groups and observed time.\"\"\"\n    f = h5py.File(remfile.File(s3_url(asset[\"asset_id\"])), \"r\")\n    t = f[\"intervals/trials\"]\n    cols = [\"Run\", \"TrialNumber\", \"finger\", \"hand\", \"finger_type\", \"start_time\",\n            \"stop_time\", \"cue_on_time\", \"cue_off_time\", \"go_on_time\"]\n    trials = pd.DataFrame({c: t[c][:] for c in cols})\n    for c in [\"finger\", \"hand\", \"finger_type\"]:\n        trials[c] = [_s(v) for v in trials[c]]\n    st = f[\"units/spike_times\"][:]\n    idx = f[\"units/spike_times_index\"][:]\n    oi = f[\"units/obs_intervals\"][:]\n    oidx = f[\"units/obs_intervals_index\"][:]\n    groups_ref = f[\"units/electrode_group\"][:]\n    group = np.array([f[r].name.split(\"/\")[-1] for r in groups_ref])\n    starts = np.r_[0, idx[:-1]]\n    ostarts = np.r_[0, oidx[:-1]]\n    spikes, obs, n_unsorted, n_out = [], [], 0, 0\n    for i, (s, e) in enumerate(zip(starts, idx)):\n        x = st[s:e]\n        if np.any(np.diff(x) < 0):\n            n_unsorted += 1\n        x = np.sort(x)\n        iv = oi[ostarts[i]:oidx[i]]\n        inside = np.zeros(len(x), bool)\n        for a, b in iv:\n            inside |= (x >= a) & (x <= b)\n        n_out += int((~inside).sum())\n        spikes.append(x)\n        obs.append(float(np.sum(iv[:, 1] - iv[:, 0])))\n    subj = f[\"general/subject\"]\n    sess = Session(\n        path=asset[\"path\"],\n        subject=_s(subj[\"subject_id\"][()]),\n        sex=_s(subj[\"sex\"][()]),\n        date=_s(f[\"general/session_id\"][()]),\n        description=_s(f[\"session_description\"][()]),\n        trials=trials,\n        spikes=spikes,\n        group=group,\n        obs_duration=np.array(obs),\n        n_unsorted=n_unsorted,\n        n_outside_obs=n_out,\n    )\n    sess.extra[\"electrode_groups\"] = pd.Series(\n        [_s(v) for v in f[\"general/extracellular_ephys/electrodes/group_name\"][:]]\n    ).value_counts().to_dict()\n    sess.extra[\"electrode_locations\"] = sorted(\n        {_s(v) for v in f[\"general/extracellular_ephys/electrodes/location\"][:]})\n    sess.extra[\"epochs\"] = len(f[\"intervals/epochs/start_time\"])\n    f.close()\n    return sess\n\n\ndef load_all() -> list[Session]:\n    return [load_session(a) for a in list_assets()]\n\n\ndef counts(spikes: list, align: np.ndarray, start: float = OFFSET, dur: float = WINDOW) -> np.ndarray:\n    \"\"\"Spike counts (trials x units) in [align + start, align + start + dur).\"\"\"\n    lo, hi = align + start, align + start + dur\n    out = np.empty((len(align), len(spikes)))\n    for j, x in enumerate(spikes):\n        out[:, j] = np.searchsorted(x, hi) - np.searchsorted(x, lo)\n    return out\n\n\ndef rates(sess: Session, window: str = \"go\", dur: float = WINDOW, start: float = OFFSET) -> np.ndarray:\n    \"\"\"Firing rates (trials x units, Hz) in an analysis window (Methods, Feature Extraction).\"\"\"\n    tr = sess.trials\n    if window == \"go\":\n        align = tr.go_on_time.values\n    elif window == \"delay\":\n        align = tr.cue_off_time.values\n    elif window == \"cue\":\n        align = tr.cue_on_time.values\n    elif window == \"iti\":\n        align, start = tr.cue_on_time.values, -dur\n    else:\n        raise ValueError(window)\n    return counts(sess.spikes, align, start, dur) / dur\n\n\ndef keep_mask(sess: Session, reading: str) -> np.ndarray:\n    \"\"\"Units kept by the 0.5 Hz exclusion under a reading of claims-file O1 ('none', 'a', 'b').\"\"\"\n    n = len(sess.spikes)\n    if reading == \"none\":\n        return np.ones(n, bool)\n    if reading == \"a\":\n        total = np.array([len(x) for x in sess.spikes])\n        return total / sess.obs_duration >= MIN_RATE\n    if reading == \"b\":\n        return rates(sess, \"go\").mean(axis=0) >= MIN_RATE\n    raise ValueError(reading)\n\n\ndef array_data(sess: Session, array: str, o1: str, window: str = \"go\", **kw):\n    \"\"\"Rates (trials x kept units) of one array, and condition labels.\"\"\"\n    _, grp = ARRAYS[array]\n    m = (sess.group == grp) & keep_mask(sess, o1)\n    X = rates(sess, window, **kw)[:, m]\n    y = sess.trials.finger.values\n    return X, y\n\n\n# ---------------------------------------------------------------- classifier\n\nclass DiagLDA:\n    \"\"\"Diagonal-covariance LDA: class means, one variance per feature pooled over\n    classes (Methods, Offline classification: Gaussian naive Bayes with a single\n    shared covariance).\"\"\"\n\n    def fit(self, X, y):\n        self.classes_ = np.unique(y)\n        self.mu_ = np.array([X[y == c].mean(axis=0) for c in self.classes_])\n        resid = X - self.mu_[np.searchsorted(self.classes_, y)]\n        dof = max(len(y) - len(self.classes_), 1)\n        var = (resid ** 2).sum(axis=0) / dof\n        var = var + 1e-9 * max(var.max(), 1e-12)  # standard floor (as GaussianNB)\n        self.var_ = var\n        self.logprior_ = np.log(np.array([(y == c).mean() for c in self.classes_]))\n        return self\n\n    def decision_function(self, X):\n        d = ((X[:, None, :] - self.mu_[None]) ** 2 / self.var_).sum(axis=2)\n        return -0.5 * d + self.logprior_\n\n    def predict(self, X):\n        return self.classes_[np.argmax(self.decision_function(X), axis=1)]\n\n\ndef make_decoder(kind: str):\n    \"\"\"Linear decoder of claims-file O7: 'lda' (diagonal LDA) or 'svm' (linear SVM on\n    z-scored rates; C = 1 is scikit-learn's default, a standard choice).\"\"\"\n    if kind == \"lda\":\n        return DiagLDA()\n    from sklearn.pipeline import make_pipeline\n    from sklearn.preprocessing import StandardScaler\n    from sklearn.svm import LinearSVC\n    return make_pipeline(StandardScaler(), LinearSVC(C=1.0, dual=\"auto\", max_iter=20000))\n\n\ndef cv_predict(X, y, o2: str = \"a\", seed: int = 0, decoder: str = \"lda\", k: int = 8):\n    \"\"\"Stratified k-fold predictions on held-out trials (Methods, K = 8).\n    o2 'a': folds in trial order; 'b': shuffled with the given seed.\"\"\"\n    from sklearn.model_selection import StratifiedKFold\n    skf = StratifiedKFold(k, shuffle=(o2 == \"b\"), random_state=seed if o2 == \"b\" else None)\n    pred = np.empty(len(y), dtype=object)\n    for tr, te in skf.split(X, y):\n        pred[te] = make_decoder(decoder).fit(X[tr], y[tr]).predict(X[te])\n    return pred\n\n\ndef error_kinds(true, pred):\n    \"\"\"Counts of errors that are adjacent (same hand, neighbouring finger in t,i,m,r,p)\n    or matching (same finger type, other hand).\"\"\"\n    err = true != pred\n    adj = match = 0\n    for t, p in zip(true[err], pred[err]):\n        ft, fp = FINGER_TYPES.index(t[1]), FINGER_TYPES.index(p[1])\n        if t[0] == p[0] and abs(ft - fp) == 1:\n            adj += 1\n        elif t[0] != p[0] and ft == fp:\n            match += 1\n    return int(err.sum()), adj, match\n\n\n# ---------------------------------------------------------------- selectivity\n\ndef anova_eta2(X, y):\n    \"\"\"One-way ANOVA per unit across conditions; returns p (NaN for a constant unit) and eta2.\"\"\"\n    from scipy.stats import f_oneway\n    groups = [X[y == c] for c in np.unique(y)]\n    p = np.full(X.shape[1], np.nan)\n    eta = np.full(X.shape[1], np.nan)\n    grand = X.mean(axis=0)\n    sst = ((X - grand) ** 2).sum(axis=0)\n    ssb = sum(len(g) * (g.mean(axis=0) - grand) ** 2 for g in groups)\n    ok = sst > 0\n    if ok.any():\n        p[ok] = f_oneway(*[g[:, ok] for g in groups]).pvalue\n        eta[ok] = ssb[ok] / sst[ok]\n    return p, eta\n\n\ndef fdr_bh(p):\n    \"\"\"Benjamini-Hochberg adjusted p (q); NaN p (constant units) are kept as not significant\n    but counted in m, the number of neurons (Methods: m = N).\"\"\"\n    p = np.asarray(p, float)\n    m = len(p)\n    pp = np.where(np.isnan(p), 1.0, p)\n    order = np.argsort(pp)\n    q = pp[order] * m / np.arange(1, m + 1)\n    q = np.minimum.accumulate(q[::-1])[::-1]\n    out = np.empty(m)\n    out[order] = np.minimum(q, 1)\n    return out\n\n\n# ---------------------------------------------------------------- distances\n\ndef crossnobis_rdm(X, y, o3: str = \"shrinkage_diag\", o4: str = \"a\") -> np.ndarray:\n    \"\"\"10 x 10 cross-validated squared Mahalanobis distances (rsatoolbox), rows/cols CONDITIONS.\n\n    o3: noise covariance estimator of rsatoolbox ('shrinkage_diag', 'shrinkage_eye', 'diag').\n    o4 'a': two partitions A and B (odd and even repetitions of each condition), each with\n    the precision of its own residuals, combined as rsatoolbox does for a list of noises\n    (Methods: \"incorporating the noise covariances of both folds\"). o4 'b': leave one\n    repetition out, a single precision from all residuals.\"\"\"\n    import rsatoolbox\n    from rsatoolbox.data.noise import prec_from_residuals\n    rep = np.zeros(len(y), int)\n    for c in np.unique(y):\n        rep[y == c] = np.arange((y == c).sum())\n    cond_idx = np.array([CONDITIONS.index(c) for c in y])\n\n    def resid(Xs, ys):\n        mu = {c: Xs[ys == c].mean(axis=0) for c in np.unique(ys)}\n        return Xs - np.array([mu[c] for c in ys]), len(ys) - len(mu)\n\n    if o4 == \"a\":\n        half = rep % 2\n        noises = []\n        for h in (0, 1):\n            r, dof = resid(X[half == h], y[half == h])\n            noises.append(prec_from_residuals(r, dof=dof, method=o3))\n        cv, noise = half, noises\n    else:\n        r, dof = resid(X, y)\n        cv, noise = rep, prec_from_residuals(r, dof=dof, method=o3)\n    ds = rsatoolbox.data.Dataset(X, obs_descriptors={\"cond\": cond_idx, \"cv\": cv})\n    rdm = rsatoolbox.rdm.calc_rdm(ds, method=\"crossnobis\", descriptor=\"cond\",\n                                  cv_descriptor=\"cv\", noise=noise)\n    return rdm.get_matrices()[0]\n\n\ndef cross_hand_elements(rdm: np.ndarray):\n    \"\"\"Matching (5) and non-matching (20) different-hand elements (Methods, Shared\n    representations across hands).\"\"\"\n    match, non = [], []\n    for i, f1 in enumerate(FINGER_TYPES):\n        for j, f2 in enumerate(FINGER_TYPES):\n            d = rdm[i, 5 + j]\n            (match if i == j else non).append(d)\n    return np.array(match), np.array(non)\n\n\n# ---------------------------------------------------------------- CCGP\n\ndef pseudo_population(sessions_X: list, sessions_y: list, o6: str, rng=None):\n    \"\"\"Stack neurons of several sessions into pseudo-trials of each condition.\n    o6 'a': trials matched by repetition index within condition; 'b': matched at random\n    within condition (one draw; callers repeat it).\"\"\"\n    n_rep = min(min((y == c).sum() for c in CONDITIONS) for y in sessions_y)\n    blocks = []\n    for X, y in zip(sessions_X, sessions_y):\n        rows = []\n        for c in CONDITIONS:\n            ix = np.flatnonzero(y == c)[:n_rep] if o6 == \"a\" else rng.permutation(np.flatnonzero(y == c))[:n_rep]\n            rows.append(X[ix])\n        blocks.append(np.concatenate(rows))\n    labels = np.repeat(CONDITIONS, n_rep)\n    return np.concatenate(blocks, axis=1), labels\n\n\ndef ccgp_hand(X, cond, decoder=\"lda\"):\n    \"\"\"Left-vs-right decoder trained on 4 finger types, tested on the held-out one; mean of 5 folds.\"\"\"\n    hand = np.array([c[0] for c in cond])\n    ft = np.array([c[1] for c in cond])\n    acc = []\n    for f in FINGER_TYPES:\n        te = ft == f\n        m = make_decoder(decoder).fit(X[~te], hand[~te])\n        acc.append(np.mean(m.predict(X[te]) == hand[te]))\n    return float(np.mean(acc))\n\n\ndef ccgp_finger(X, cond, decoder=\"lda\"):\n    \"\"\"5-class finger-type decoder trained on one hand, tested on the other; mean of both directions.\"\"\"\n    hand = np.array([c[0] for c in cond])\n    ft = np.array([c[1] for c in cond])\n    acc = []\n    for h in \"RL\":\n        tr = hand == h\n        m = make_decoder(decoder).fit(X[tr], ft[tr])\n        acc.append(np.mean(m.predict(X[~tr]) == ft[~tr]))\n    return float(np.mean(acc))\n\n\ndef standard_accuracy(X, cond, target, decoder=\"lda\", o2=\"a\", seed=0):\n    \"\"\"Cross-validated (stratified 8-fold) accuracy without leaving conditions out.\n    target 'hand'; 'finger_within' (claims-file O8 a, per hand, mean of hands);\n    'finger_both' (O8 b, finger type over both hands).\"\"\"\n    hand = np.array([c[0] for c in cond])\n    ft = np.array([c[1] for c in cond])\n    if target == \"hand\":\n        return float(np.mean(cv_predict(X, hand, o2, seed, decoder) == hand))\n    if target == \"finger_both\":\n        return float(np.mean(cv_predict(X, ft, o2, seed, decoder) == ft))\n    accs = []\n    for h in \"RL\":\n        m = hand == h\n        accs.append(np.mean(cv_predict(X[m], ft[m], o2, seed, decoder) == ft[m]))\n    return float(np.mean(accs))\n\n\ndef shuffle_conditions(cond, rng):\n    \"\"\"A label shuffle for the permutation test: condition labels permuted across pseudo-trials.\"\"\"\n    return rng.permutation(cond)\n"
}
```

```
File created successfully at: entries/000252-guan-2022/fingers.py (file state is current in your context — no need to Read it back)
```

**Agent**

Helper written. Next I prototype: load all sessions (timed), then counts, selectivity and decoding.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > proto1.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000252-guan-2022')
import fingers as F, numpy as np
t=time.time(); S=F.load_all(); print('load s', time.time()-t)
pickle.dump(S, open('S.pkl','wb'))
for s in S: print(s.path, s.subject, s.sex, s.date, s.n_unsorted, s.n_outside_obs, s.extra)
EOF
python proto1.py 2>&1 | grep -v Warn
```

```
load s 9.887396097183228
sub-N1/sub-N1_ses-2019-02-12_ecephys.nwb N1 M 2019-02-12 283 0 {'electrode_groups': {'PPC': 96, 'MC': 95}, 'electrode_locations': ['left motor cortex (MC), near hand knob', 'left posterior parietal cortex (PPC), superior parietal lobule (SPL)'], 'epochs': 2}
sub-N1/sub-N1_ses-2019-12-20_ecephys.nwb N1 M 2019-12-20 224 0 {'electrode_groups': {'MC': 96, 'PPC': 96}, 'electrode_locations': ['left motor cortex (MC), near hand knob', 'left posterior parietal cortex (PPC), superior parietal lobule (SPL)'], 'epochs': 2}
sub-P1/sub-P1_ses-2015-08-12_ecephys.nwb P1 F 2015-08-12 101 0 {'electrode_groups': {'PPC': 96}, 'electrode_locations': ['left posterior parietal cortex (PPC), junction of postcentral and intraparietal sulci (PC-IP)'], 'epochs': 2}
sub-P1/sub-P1_ses-2015-08-14_ecephys.nwb P1 F 2015-08-14 92 0 {'electrode_groups': {'PPC': 96}, 'electrode_locations': ['left posterior parietal cortex (PPC), junction of postcentral and intraparietal sulci (PC-IP)'], 'epochs': 2}
sub-P1/sub-P1_ses-2015-08-17_ecephys.nwb P1 F 2015-08-17 93 0 {'electrode_groups': {'PPC': 96}, 'electrode_locations': ['left posterior parietal cortex (PPC), junction of postcentral and intraparietal sulci (PC-IP)'], 'epochs': 2}
sub-P1/sub-P1_ses-2015-08-21_ecephys.nwb P1 F 2015-08-21 94 0 {'electrode_groups': {'PPC': 96}, 'electrode_locations': ['left posterior parietal cortex (PPC), junction of postcentral and intraparietal sulci (PC-IP)'], 'epochs': 2}
sub-P1/sub-P1_ses-2016-04-27_ecephys.nwb P1 F 2016-04-27 108 0 {'electrode_groups': {'PPC': 96}, 'electrode_locations': ['left posterior parietal cortex (PPC), junction of postcentral and intraparietal sulci (PC-IP)'], 'epochs': 2}
sub-P1/sub-P1_ses-2016-05-04_ecephys.nwb P1 F 2016-05-04 108 0 {'electrode_groups': {'PPC': 96}, 'electrode_locations': ['left posterior parietal cortex (PPC), junction of postcentral and intraparietal sulci (PC-IP)'], 'epochs': 2}
sub-P1/sub-P1_ses-2016-05-11_ecephys.nwb P1 F 2016-05-11 113 0 {'ele
[... 4 more lines not kept]
```

**Agent**

Loading everything takes 10 s. Next: counts, selectivity and decoding.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > proto2.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000252-guan-2022')
import fingers as F, numpy as np
S=pickle.load(open('S.pkl','rb'))
def sess_of(arr): return [s for s in S if s.subject==F.ARRAYS[arr][0]]
for o1 in ['none','a','b']:
    for arr in F.ARRAYS:
        n=[F.array_data(s,arr,o1)[0].shape[1] for s in sess_of(arr)]
        print(o1,arr,n,np.mean(n).round(1),sum(n))
for o1 in ['none','a','b']:
  for arr in F.ARRAYS:
    ps=[];
    for s in sess_of(arr):
        X,y=F.array_data(s,arr,o1); p,e=F.anova_eta2(X,y); ps.append(p)
    p=np.concatenate(ps); q=F.fdr_bh(p); print('sel',o1,arr,len(p),'nan',np.isnan(p).sum(), (q<0.05).mean().round(3))
t=time.time()
for o1 in ['none','a','b']:
  for o2 in ['a','b']:
    for arr in F.ARRAYS:
        accs=[];errs=[]
        for seed in (range(10) if o2=='b' else [0]):
            T=[];P=[]
            for s in sess_of(arr):
                X,y=F.array_data(s,arr,o1); P.append(F.cv_predict(X,y,o2,seed)); T.append(y)
            T=np.concatenate(T);P=np.concatenate(P); accs.append((T==P).mean()); e,a,m=F.error_kinds(T,P); errs.append((a+m)/e)
        print('dec',o1,o2,arr,np.mean(accs).round(3),np.mean(errs).round(3))
print(time.time()-t)
EOF
python proto2.py 2>&1 | grep -v Warn
```

```
none N-PPC [112, 102, 119, 110, 116, 110, 118, 109, 105, 113] 111.4 1114
none J-PPC [159, 160] 159.5 319
none J-MC [139, 120] 129.5 259
a N-PPC [95, 86, 94, 89, 100, 104, 100, 92, 92, 91] 94.3 943
a J-PPC [157, 158] 157.5 315
a J-MC [137, 115] 126.0 252
b N-PPC [96, 91, 93, 82, 99, 100, 96, 91, 93, 89] 93.0 930
b J-PPC [157, 155] 156.0 312
b J-MC [137, 113] 125.0 250
sel none N-PPC 1114 nan 5 0.404
sel none J-PPC 319 nan 0 0.376
sel none J-MC 259 nan 2 0.637
sel a N-PPC 943 nan 0 0.478
sel a J-PPC 315 nan 0 0.381
sel a J-MC 252 nan 0 0.651
sel b N-PPC 930 nan 0 0.489
sel b J-PPC 312 nan 0 0.381
sel b J-MC 250 nan 0 0.656
dec none a N-PPC 0.717 0.749
dec none a J-PPC 0.7 0.7
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > proto3.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000252-guan-2022')
import fingers as F, numpy as np
S=pickle.load(open('S.pkl','rb'))
def sess_of(arr): return [s for s in S if s.subject==F.ARRAYS[arr][0]]
o1='a'
for arr in F.ARRAYS:
    res={}
    for w in ['go','delay','cue','iti']:
        ps=[]
        for s in sess_of(arr):
            X,y=F.array_data(s,arr,o1,window=w); ps.append(F.anova_eta2(X,y)[0])
        p=np.concatenate(ps); res[w]=F.fdr_bh(p)<0.05
        print(arr,w,'q<.05',res[w].mean().round(3),'p<.05 uncorrected',(p<0.05).mean().round(3))
    print(arr,'any of cue/delay/go', (res['go']|res['delay']|res['cue']).mean().round(3))
    # per-session FDR
    fr=[]
    for s in sess_of(arr):
        X,y=F.array_data(s,arr,o1); fr.append((F.fdr_bh(F.anova_eta2(X,y)[0])<0.05).mean())
    print(arr,'per-session FDR mean',np.round(np.mean(fr),3))
# time course decoding around go and cue
for arr in F.ARRAYS:
    row=[]
    for t0 in np.arange(-3.0,1.6,0.5):
        T=[];P=[]
        for s in sess_of(arr):
            m=(s.group==F.ARRAYS[arr][1])&F.keep_mask(s,o1)
            X=F.counts(s.spikes,s.trials.go_on_time.values,t0,0.5)[:,m]; y=s.trials.finger.values
            P.append(F.cv_predict(X,y)); T.append(y)
        row.append(round((np.concatenate(T)==np.concatenate(P)).mean(),2))
    print(arr,'acc by window start rel go -3..1.5', row)
EOF
python proto3.py 2>&1 | grep -v Warn
```

```
N-PPC go q<.05 0.478 p<.05 uncorrected 0.55
N-PPC delay q<.05 0.162 p<.05 uncorrected 0.315
N-PPC cue q<.05 0.0 p<.05 uncorrected 0.078
N-PPC iti q<.05 0.0 p<.05 uncorrected 0.051
N-PPC any of cue/delay/go 0.523
N-PPC per-session FDR mean 0.474
J-PPC go q<.05 0.381 p<.05 uncorrected 0.463
J-PPC delay q<.05 0.368 p<.05 uncorrected 0.441
J-PPC cue q<.05 0.0 p<.05 uncorrected 0.095
J-PPC iti q<.05 0.0 p<.05 uncorrected 0.029
J-PPC any of cue/delay/go 0.517
J-PPC per-session FDR mean 0.384
J-MC go q<.05 0.651 p<.05 uncorrected 0.683
J-MC delay q<.05 0.492 p<.05 uncorrected 0.54
J-MC cue q<.05 0.008 p<.05 uncorrected 0.075
J-MC iti q<.05 0.0 p<.05 uncorrected 0.024
J-MC any of cue/delay/go 0.718
J-MC per-session FDR mean 0.636
N-PPC acc by window start rel go -3..1.5 [np.float64(0.1), np.float64(0.12), np.float64(0.27), np.float64(0.37), np.float64(0.41), np.float64(0.51), np.float64(0.66), np.float64(0.68), np.float64(0.47), np.float64(0.33)]
J-PPC acc by window start rel go -3..1.5 [np.float64(0.04), np.float64(0.15), np.float64(0.23), np.float64(0.4), np.float64(0.56), np.float64(0.68), np.float64(0.74), np.float64(0.61), np.float64(0.52), np.float64(0.42)]
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > proto4.py <<'EOF'
import sys, time, pickle, warnings; warnings.filterwarnings('ignore'); sys.path.insert(0,'entries/000252-guan-2022')
import fingers as F, numpy as np
from scipy.stats import bootstrap
S=pickle.load(open('S.pkl','rb'))
def sess_of(arr): return [s for s in S if s.subject==F.ARRAYS[arr][0]]
t=time.time()
for o1 in ['a','b']:
 for o3 in ['shrinkage_diag','shrinkage_eye','diag']:
  for o4 in ['a','b']:
    out=[]
    for arr in F.ARRAYS:
        M=[];N=[];R=[]
        for s in sess_of(arr):
            X,y=F.array_data(s,arr,o1); rdm=F.crossnobis_rdm(X,y,o3,o4); R.append(rdm); m,n=F.cross_hand_elements(rdm); M+=list(m); N+=list(n)
        M=np.array(M);N=np.array(N)
        d=N.mean()-M.mean()
        ci=bootstrap((N,M),lambda a,b,axis=-1: a.mean(axis)-b.mean(axis),n_resamples=5000,method='BCa',random_state=0,vectorized=True).confidence_interval
        out.append(f"{arr} {d:.2f} [{ci.low:.2f},{ci.high:.2f}]")
        if arr=='N-PPC':
            A=np.mean(R,0); ix={c:i for i,c in enumerate(F.CONDITIONS)}
            pat=[(A[ix[h+'i'],ix[h+'m']],A[ix[h+'i'],ix[h+'r']],A[ix[h+'m'],ix[h+'r']]) for h in 'RL']
            out.append('IM,IR,MR '+str(np.round(pat,2).tolist()))
    print(o1,o3,o4,' | '.join(out))
print(time.time()-t)
EOF
python proto4.py 2>&1 | grep -v Warn
```

```
a shrinkage_diag a N-PPC nan [nan,nan] | IM,IR,MR [[nan, nan, nan], [nan, nan, nan]] | J-PPC 0.04 [-0.02,0.13] | J-MC 0.61 [0.33,0.81]
a shrinkage_diag b N-PPC 0.29 [0.25,0.33] | IM,IR,MR [[0.43, 0.58, 0.13], [0.26, 0.45, 0.12]] | J-PPC 0.04 [-0.01,0.11] | J-MC 0.51 [0.25,0.69]
a shrinkage_eye a N-PPC 0.34 [0.28,0.40] | IM,IR,MR [[0.5, 0.7, 0.15], [0.31, 0.53, 0.16]] | J-PPC 0.04 [-0.06,0.14] | J-MC 0.60 [0.25,0.85]
a shrinkage_eye b N-PPC 0.35 [0.30,0.41] | IM,IR,MR [[0.58, 0.78, 0.24], [0.4, 0.65, 0.23]] | J-PPC 0.05 [-0.04,0.15] | J-MC 0.63 [0.26,0.90]
Traceback (most recent call last):
  File "/tmp/claude-1001/proto4.py", line 14, in <module>
    X,y=F.array_data(s,arr,o1); rdm=F.crossnobis_rdm(X,y,o3,o4); R.append(rdm); m,n=F.cross_hand_elements(rdm); M+=list(m); N+=list(n)
                                    ~~~~~~~~~~~~~~~~^^^^^^^^^^^
  File "entries/000252-guan-2022/fingers.py", line 335, in crossnobis_rdm
    noises.append(prec_from_residuals(r, dof=dof, method=o3))
                  ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/rsatoolbox/data/noise.py", line 271, in prec_from_residuals
    prec = np.linalg.inv(cov)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/linalg/_linalg.py", line 659, in inv
    ainv = _umath_linalg.inv(a, signature=signature)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/linalg/_linalg.py", line 144, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000252-guan-2022/fingers.py",
 "old_string": "def crossnobis_rdm(X, y, o3: str = \"shrinkage_diag\", o4: str = \"a\") -> np.ndarray:\n    \"\"\"10 x 10 cross-validated squared Mahalanobis distances (rsatoolbox), rows/cols CONDITIONS.\n\n    o3: noise covariance estimator of rsatoolbox ('shrinkage_diag', 'shrinkage_eye', 'diag').\n    o4 'a': two partitions A and B (odd and even repetitions of each condition), each with\n    the precision of its own residuals, combined as rsatoolbox does for a list of noises\n    (Methods: \"incorporating the noise covariances of both folds\"). o4 'b': leave one\n    repetition out, a single precision from all residuals.\"\"\"\n    import rsatoolbox\n    from rsatoolbox.data.noise import prec_from_residuals\n    rep = np.zeros(len(y), int)\n    for c in np.unique(y):\n        rep[y == c] = np.arange((y == c).sum())\n    cond_idx = np.array([CONDITIONS.index(c) for c in y])\n\n    def resid(Xs, ys):\n        mu = {c: Xs[ys == c].mean(axis=0) for c in np.unique(ys)}\n        return Xs - np.array([mu[c] for c in ys]), len(ys) - len(mu)\n\n    if o4 == \"a\":\n        half = rep % 2\n        noises = []\n        for h in (0, 1):\n            r, dof = resid(X[half == h], y[half == h])\n            noises.append(prec_from_residuals(r, dof=dof, method=o3))\n        cv, noise = half, noises\n    else:\n        r, dof = resid(X, y)\n        cv, noise = rep, prec_from_residuals(r, dof=dof, method=o3)\n    ds = rsatoolbox.data.Dataset(X, obs_descriptors={\"cond\": cond_idx, \"cv\": cv})\n    rdm = rsatoolbox.rdm.calc_rdm(ds, method=\"crossnobis\", descriptor=\"cond\",\n                                  cv_descriptor=\"cv\", noise=noise)\n    return rdm.get_matrices()[0]",
 "new_string": "def _resid(Xs, ys):\n    mu = {c: Xs[ys == c].mean(axis=0) for c in np.unique(ys)}\n    return Xs - np.array([mu[c] for c in ys]), len(ys) - len(mu)\n\n\ndef crossnobis_rdm(X, y, o3: str = \"shrinkage_diag\", o4: str = \"a\"):\n    \"\"\"10 x 10 cross-validated squared Mahalanobis distances (rsatoolbox), rows/cols CONDITIONS.\n    Returns the matrix and the number of units dropped for zero residual variance.\n\n    o3: noise covariance estimator of rsatoolbox ('shrinkage_diag', 'shrinkage_eye', 'diag').\n    o4 'a': two partitions A and B (odd and even repetitions of each condition), each with\n    the noise precision of its own trials, combined as rsatoolbox does for a list of noises\n    (Methods: \"incorporating the noise covariances of both folds\"). For a list of noises,\n    rsatoolbox's calc_rdm_crossnobis documents that each \"is the precision of the mean from\n    the corresponding crossvalidation fold, i.e. if multiple measurements enter a fold, please\n    compute the resulting noise precision in advance\", so the single-trial precision is\n    multiplied by the number of trials per condition in the fold (5). This follows the\n    toolbox the paper names (Methods, ref 57); it is an assumption about how the paper called\n    it. o4 'a1': the same, with the single-trial precision passed unscaled (a variant).\n    o4 'b': leave one repetition out, one single-trial precision from all residuals.\n\n    Units with zero residual variance in a partition (no spikes, or the same count, in every\n    trial of it) make the covariance singular and are dropped from that session's distance;\n    the count is returned.\"\"\"\n    import rsatoolbox\n    from rsatoolbox.data.noise import prec_from_residuals\n    rep = np.zeros(len(y), int)\n    for c in np.unique(y):\n        rep[y == c] = np.arange((y == c).sum())\n    half = rep % 2\n    ok = np.ones(X.shape[1], bool)\n    for h in (0, 1):\n        r, _ = _resid(X[half == h], y[half == h])\n        ok &= r.var(axis=0) > 0\n    X = X[:, ok]\n    cond_idx = np.array([CONDITIONS.index(c) for c in y])\n\n    if o4 in (\"a\", \"a1\"):\n        noises = []\n        for h in (0, 1):\n            r, dof = _resid(X[half == h], y[half == h])\n            n_per = (half == h).sum() / len(np.unique(y[half == h]))\n            prec = prec_from_residuals(r, dof=dof, method=o3)\n            noises.append(prec * n_per if o4 == \"a\" else prec)\n        cv, noise = half, noises\n    else:\n        r, dof = _resid(X, y)\n        cv, noise = rep, prec_from_residuals(r, dof=dof, method=o3)\n    ds = rsatoolbox.data.Dataset(X, obs_descriptors={\"cond\": cond_idx, \"cv\": cv})\n    rdm = rsatoolbox.rdm.calc_rdm(ds, method=\"crossnobis\", descriptor=\"cond\",\n                                  cv_descriptor=\"cv\", noise=noise)\n    return rdm.get_matrices()[0], int((~ok).sum())"
}
```

```
The file entries/000252-guan-2022/fingers.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i "s/for o4 in \['a','b'\]:/for o4 in ['a','a1','b']:/; s/rdm=F.crossnobis_rdm(X,y,o3,o4);/rdm,nd=F.crossnobis_rdm(X,y,o3,o4);/" proto4.py && python proto4.py 2>&1 | grep -v Warn
```

```
a shrinkage_diag a N-PPC 1.42 [1.20,1.64] | IM,IR,MR [[2.16, 2.96, 0.62], [1.3, 2.23, 0.57]] | J-PPC 0.22 [-0.09,0.65] | J-MC 3.06 [1.66,4.07]
a shrinkage_diag a1 N-PPC 0.28 [0.24,0.33] | IM,IR,MR [[0.43, 0.59, 0.12], [0.26, 0.45, 0.11]] | J-PPC 0.04 [-0.02,0.13] | J-MC 0.61 [0.33,0.81]
a shrinkage_diag b N-PPC 0.29 [0.25,0.33] | IM,IR,MR [[0.43, 0.58, 0.13], [0.26, 0.45, 0.12]] | J-PPC 0.04 [-0.01,0.11] | J-MC 0.51 [0.25,0.69]
a shrinkage_eye a N-PPC 1.70 [1.41,1.98] | IM,IR,MR [[2.52, 3.5, 0.75], [1.54, 2.67, 0.79]] | J-PPC 0.19 [-0.29,0.69] | J-MC 2.99 [1.25,4.23]
a shrinkage_eye a1 N-PPC 0.34 [0.28,0.40] | IM,IR,MR [[0.5, 0.7, 0.15], [0.31, 0.53, 0.16]] | J-PPC 0.04 [-0.06,0.14] | J-MC 0.60 [0.25,0.85]
a shrinkage_eye b N-PPC 0.36 [0.30,0.41] | IM,IR,MR [[0.58, 0.78, 0.24], [0.4, 0.65, 0.23]] | J-PPC 0.05 [-0.04,0.15] | J-MC 0.63 [0.26,0.90]
a diag a N-PPC 1.42 [1.20,1.64] | IM,IR,MR [[2.16, 2.96, 0.62], [1.3, 2.23, 0.57]] | J-PPC 0.22 [-0.09,0.65] | J-MC 3.32 [1.88,4.38]
a diag a1 N-PPC 0.28 [0.24,0.33] | IM,IR,MR [[0.43, 0.59, 0.12], [0.26, 0.45, 0.11]] | J-PPC 0.04 [-0.02,0.13] | J-MC 0.66 [0.38,0.88]
a diag b N-PPC 0.29 [0.25,0.33] | IM,IR,MR [[0.43, 0.58, 0.13], [0.26, 0.45, 0.12]] | J-PPC 0.05 [-0.01,0.12] | J-MC 0.65 [0.36,0.87]
b shrinkage_diag a N-PPC 1.44 [1.23,1.66] | IM,IR,MR [[2.18, 2.98, 0.63], [1.34, 2.27, 0.59]] | J-PPC 0.22 [-0.10,0.65] | J-MC 3.13 [1.65,4.17]
b shrinkage_diag a1 N-PPC 0.29 [0.25,0.33] | IM,IR,MR [[0.44, 0.6, 0.13], [0.27, 0.45, 0.12]] | J-PPC 0.04 [-0.02,0.13] | J-MC 0.63 [0.33,0.83]
b shrinkage_diag b N-PPC 0.30 [0.25,0.34] | IM,IR,MR [[0.44, 0.59, 0.13], [0.27, 0.47, 0.12]] | J-PPC 0.04 [-0.01,0.11] | J-MC 0.52 [0.26,0.70]
b shrinkage_eye a N-PPC 1.71 [1.42,1.99] | IM,IR,MR [[2.52, 3.51, 0.76], [1.54, 2.68, 0.8]] | J-PPC 0.19 [-0.30,0.69] | J-MC 3.01 [1.26,4.26]
b shrinkage_eye a1 N-PPC 0.34 [0.28,0.40] | IM,IR,MR [[0.5, 0.7, 0.15], [0.31, 0.54, 0.16]] | J-PPC 0.04 [-0.06,0.14] | J-MC 0.60 [0.25,0.85]
b shrinkage_eye b N-PPC 
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > proto5.py <<'EOF'
import sys, time, pickle, warnings; warnings.filterwarnings('ignore'); sys.path.insert(0,'entries/000252-guan-2022')
import fingers as F, numpy as np
S=pickle.load(open('S.pkl','rb'))
def sess_of(arr): return [s for s in S if s.subject==F.ARRAYS[arr][0]]
o1='a'
for dec in ['lda','svm']:
  for arr in F.ARRAYS:
    Xs,ys=zip(*[F.array_data(s,arr,o1) for s in sess_of(arr)])
    X,c=F.pseudo_population(list(Xs),list(ys),'a')
    t=time.time()
    h=F.ccgp_hand(X,c,dec); f=F.ccgp_finger(X,c,dec)
    sh=F.standard_accuracy(X,c,'hand',dec); sw=F.standard_accuracy(X,c,'finger_within',dec); sb=F.standard_accuracy(X,c,'finger_both',dec)
    t1=time.time()-t
    rng=np.random.default_rng(0); t=time.time()
    nh=[F.ccgp_hand(X,F.shuffle_conditions(c,rng),dec) for _ in range(20)]
    nf=[F.ccgp_finger(X,F.shuffle_conditions(c,rng),dec) for _ in range(20)]
    print(dec,arr,X.shape,'hand ccgp',round(h,3),'std',round(sh,3),'finger ccgp',round(f,3),'within',round(sw,3),'both',round(sb,3),'null max',max(nh),max(nf),'t obs',round(t1,2),'t per 20 shuffles',round(time.time()-t,2))
EOF
python proto5.py 2>&1 | grep -v Warn
```

```
lda N-PPC (100, 943) hand ccgp 0.98 std 1.0 finger ccgp 0.94 within 0.98 both 0.98 null max 0.6699999999999999 0.26 t obs 0.58 t per 20 shuffles 0.08
lda J-PPC (100, 315) hand ccgp 0.98 std 0.98 finger ccgp 0.29 within 0.87 both 0.79 null max 0.65 0.29000000000000004 t obs 0.01 t per 20 shuffles 0.02
lda J-MC (100, 252) hand ccgp 0.87 std 0.89 finger ccgp 0.78 within 0.98 both 0.91 null max 0.61 0.29000000000000004 t obs 0.01 t per 20 shuffles 0.02
svm N-PPC (100, 943) hand ccgp 0.98 std 1.0 finger ccgp 0.93 within 0.96 both 0.97 null max 0.65 0.29000000000000004 t obs 0.21 t per 20 shuffles 0.7
svm J-PPC (100, 315) hand ccgp 0.98 std 0.98 finger ccgp 0.36 within 0.84 both 0.76 null max 0.6 0.26 t obs 0.1 t per 20 shuffles 0.29
svm J-MC (100, 252) hand ccgp 0.86 std 0.93 finger ccgp 0.79 within 0.96 both 0.93 null max 0.61 0.28 t obs 0.1 t per 20 shuffles 0.31
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && date -u && cat > proto6.py <<'EOF'
import sys, time, pickle, warnings; warnings.filterwarnings('ignore'); sys.path.insert(0,'entries/000252-guan-2022')
import fingers as F, numpy as np
S=pickle.load(open('S.pkl','rb'))
def sess_of(arr): return [s for s in S if s.subject==F.ARRAYS[arr][0]]
for arr in F.ARRAYS:
  for dec in ['lda','svm']:
    r={}
    for tgt in ['hand','finger_within','finger_both']:
        a=[];n=[]
        for s in sess_of(arr):
            X,y=F.array_data(s,arr,'a'); a.append(F.standard_accuracy(X,y,tgt,dec)); n.append(len(y))
        r[tgt]=round(np.average(a,weights=n),3)
    print(arr,dec,'per-session std acc',r)
EOF
python proto6.py 2>&1 | grep -v Warn
```

```
Wed Nov  4 12:08:09 UTC 2026
N-PPC lda per-session std acc {'hand': np.float64(0.847), 'finger_within': np.float64(0.82), 'finger_both': np.float64(0.827)}
N-PPC svm per-session std acc {'hand': np.float64(0.778), 'finger_within': np.float64(0.716), 'finger_both': np.float64(0.731)}
J-PPC lda per-session std acc {'hand': np.float64(0.965), 'finger_within': np.float64(0.69), 'finger_both': np.float64(0.695)}
J-PPC svm per-session std acc {'hand': np.float64(0.94), 'finger_within': np.float64(0.685), 'finger_both': np.float64(0.53)}
J-MC lda per-session std acc {'hand': np.float64(0.86), 'finger_within': np.float64(0.87), 'finger_both': np.float64(0.865)}
J-MC svm per-session std acc {'hand': np.float64(0.915), 'finger_within': np.float64(0.87), 'finger_both': np.float64(0.865)}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000147/versions/0.221122.2256/" | python -c "import json,sys; d=json.load(sys.stdin); print(d['name']); print(d.get('description')); print([ (r.get('name'),r.get('identifier')) for r in d.get('relatedResource',[])]); print(d['assetsSummary'].get('numberOfFiles'))"; curl -s "https://api.dandiarchive.org/api/dandisets/000147/versions/0.221122.2256/assets/?page_size=5" | python -c "import json,sys; d=json.load(sys.stdin); print(d['count'], [a['path'] for a in d['results']])"; curl -s "https://api.dandiarchive.org/api/dandisets/000252/versions/draft/assets/?page_size=100" | python -c "import json,sys; d=json.load(sys.stdin); print(sorted((a['path'],a['asset_id']) for a in d['results'])[:3])"
```

Result: the fetched text is not kept.

**Agent calls Skill**

```json
{
 "skill": "dataviz"
}
```

```
Launching skill: dataviz
```

## Prompt

Base directory for this skill: /tmp/claude-1001/bundled-skills/2.1.284/c1867c2bfcec4c367c26e1f2de121f66/dataviz

# Data Visualization

A chart is **read by people and executed by you**. This skill turns "make it look
good" into a procedure with checks, so the result is right by construction rather
than by taste.

**The method here is design-system-agnostic.** Nothing in the procedure, the form
heuristic, the six checks, or the mark specs is specific to one product. A design
system supplies a small set of *parameters* (its ramps, a categorical order, a
diverging pair, a status palette, a texture, its surfaces, its filter components);
the method consumes them unchanged. A **validated default palette** is the
reference instance, fully specified in `references/palette.md`. To target your
brand, read that file's structure and substitute its values - touch nothing else.

> The single most important habit: **the color part is computable, so compute it.**
> Never eyeball whether a palette is colorblind-safe - run `scripts/validate_palette.js`.

## The procedure - do these in order

Color comes LAST. Most bad charts pick colors first.

1. **Pick the form.** What is the data's job - magnitude, identity, polarity, a
   single headline, change-over-time? The job picks the chart type, and sometimes
   the answer is *not a chart* (a stat tile or hero number). -> `references/choosing-a-form.md`
2. **Assign color by the job it does.** Categorical (identity), sequential
   (magnitude), diverging (polarity), or status (state) - each has one rule.
   Assign categorical hues in fixed order, never cycled. -> `references/color-formula.md`
3. **VALIDATE the palette - run the script, don't reason about Delta E.**
   `node scripts/validate_palette.js "<hex,hex,...>" --mode light` (relative to
   this skill's base directory - or load it as `<script type="module">` in the
   chart's own page, where it reads
   `data-palette` off `<body>` and logs a `console.table` report). It returns
   pass/fail on the lightness band, chroma floor, adjacent-pair CVD separation,
   the normal-vision floor, and contrast. Fix anything that FAILs before continuing. Re-run for
   `--mode dark` with that mode's surface.
4. **Apply mark specs & spacers.** Thin marks, 4px rounded data-ends anchored to
   the baseline, 2px lines, >=8px markers, a 2px surface gap between fills (stacked
   segments and adjacent bars alike) and a 2px surface ring on overlapping marks,
   selective direct labels. -> `references/marks-and-anatomy.md`
5. **Add the hover layer - by default.** An HTML/SVG chart *is* interactive; ship
   a crosshair+tooltip on line/area and a per-mark hover tooltip on bar/dot/cell.
   The only form that skips it is a bare stat tile with no plot. Hit targets bigger
   than the mark; filters in one row above the charts. -> `references/interaction.md`
6. **Final accessibility pass.** For >= 2 series a legend is always present and <= 4
   are also direct-labeled (a single series needs no legend box - the title names
   it), so identity is never color-alone; a table view exists; dark mode is **selected** - its own
   steps from the same ramps, validated against the dark surface, not an automatic
   flip; texture is available for the CVD/print/forced-colors case.
7. **Render it and look at it.** The validator checks color, not layout - open or
   screenshot the output and eyeball it for label collisions, geometry, and overflow
   before calling it done.

Then check the result against **`references/anti-patterns.md`** - it is the catalog
of what goes wrong. If your chart matches an entry, it's wrong.

## Non-negotiables (true in every design system)

- **Assign categorical hues in fixed order, never cycled.** A 9th series is never a
  generated hue - it folds into "Other," small multiples, or composite encoding.
- **One axis.** Never a dual-axis chart (two y-scales). Two measures of different
  scale -> two charts, small multiples, or indexed to a common base. *(This is the
  #1 chart mistake - see anti-patterns.)*
- **Color follows the entity, never its rank.** A filter that changes the series
  count must not repaint the survivors.
- **Sequential = one hue, light->dark. Diverging = two hues + a neutral gray
  midpoint.** Never a rainbow; never a hue at the diverging midpoint.
- **Run the validator before shipping any categorical palette.** CVD Delta E >= 8 is the
  target (OKLab ×100); 6-8 is a floor that is legal ONLY with secondary encoding. A
  normal-vision floor below 15 is a hard FAIL - full-color readers can't tell the
  pair apart; re-step it on the adjacent pairlist (secondary encoding does not excuse
  this one); under `--pairs all` cut series or facet instead - see check 4. A contrast WARN
  obligates visible labels or a table view - it is not dismissable.
- **Thin marks; a legend always present for >= 2 series (none for one), with
  selective direct labels (never a number on every point); recessive grid/axes.**
- **Text wears text tokens, never the series color** - values, labels, and legends
  stay in primary/secondary/muted ink; a colored mark beside them carries identity.
- **Status colors are reserved** (good/warning/serious/critical) and never reused
  for "series 4"; they ship with an icon + label, never color alone.

## Plugging in a design system

The method is invariant; only these parameters change per system. The reference
instance - every value filled in - is `references/palette.md`.

| Parameter | What the system provides |
|---|---|
| **Ramps** | the hue scales (named steps) the palette draws from |
| **Categorical theme** | the fixed hue order (a named theme); default + alternates |
| **Sequential hue** | the default single hue for magnitude |
| **Diverging pair** | two warm/cool poles + a neutral midpoint |
| **Status palette** | good / warning / serious / critical - steps distinct from categorical |
| **Texture fill** | one directional hand-drawn fill, used at 45° / 135° |
| **Surfaces** | light & dark chart-surface colors (the validator needs these) |
| **Filter controls** | date-range & dimension controls (behavioral spec in `interaction.md`) |

To onboard a new system: fill those rows, feed its ramps to the validator, and let
it snap each slot to the nearest passing step. Structure and rules stay as written.

## Reference files

| File | What it answers |
|------|-----------------|
| `references/choosing-a-form.md` | Which chart type / is it even a chart? |
| `references/color-formula.md` | The four jobs, the six checks, snap-to-passing |
| `references/marks-and-anatomy.md` | Mark specs, spacers, labels, figures, hero number |
| `references/interaction.md` | Tooltips & hover, filters & time ranges |
| `references/components.md` | The pieces a chart is made of - build each in plain HTML |
| `references/anti-patterns.md` | **What goes wrong - check every chart against this** |
| `references/palette.md` | **The reference palette instance** - every parameter, filled in; swap for your brand's |
| `scripts/validate_palette.js` | Runnable six-checks validator (run it; don't eyeball) |

**Agent calls Bash**

```bash
cd /tmp/claude-1001/bundled-skills/2.1.284/c1867c2bfcec4c367c26e1f2de121f66/dataviz && grep -n -i -A12 "categorical" references/palette.md | head -40
```

```
21:  --series-1:       #2a78d6;   /* categorical slot 1 */
22-  /* ...only the roles this chart uses */
23-}
24-@media (prefers-color-scheme: dark) {
25-  :root:where(:not([data-theme="light"])) .viz-root {
26-    color-scheme: dark;
27-    --surface-1:      #1a1a19;
28-    --text-primary:   #ffffff;
29-    --text-secondary: #c3c2b7;
30-    --series-1:       #3987e5;
31-  }
32-}
33-:root[data-theme="dark"] .viz-root {
--
47:## Categorical palette
48-
49-Both modes are selected. The dark column is the same eight hues stepped for the
50-dark surface, not a separate palette:
51-
52-| Slot | Hue | Light | Dark |
[... 21 more lines not kept]
```

**Agent**

I'll use the validated default pair (blue #2a78d6, orange #eb6834) and a single-hue blue ramp for RDMs. Now I add the CCGP runner, neuron-dropping and GPA to the helper.

**Agent calls Bash**

```bash
cat >> entries/000252-guan-2022/fingers.py <<'EOF'


N_SHUFFLES = 1001     # Methods, Compositionality of finger representations
N_PAIRINGS = 100      # claims-file O6 (b): random pseudo-trial matchings averaged


def run_ccgp(Xs: list, ys: list, o6: str, decoder: str, rng, n_shuffles: int = N_SHUFFLES):
    """Hand and finger-type CCGP, standard accuracies and permutation p-values on a
    pseudo-population. For o6 'b' the observed values are averaged over N_PAIRINGS random
    matchings, and each shuffle of the null uses a fresh matching (an assumption: the
    paper does not say how its null treats the pseudo-trials). p = (1 + #null >= observed)
    / (1 + n_shuffles)."""
    pairings = 1 if o6 == "a" else N_PAIRINGS
    obs = {k: [] for k in ["hand", "finger", "std_hand", "std_within", "std_both"]}
    for _ in range(pairings):
        X, c = pseudo_population(Xs, ys, o6, rng)
        obs["hand"].append(ccgp_hand(X, c, decoder))
        obs["finger"].append(ccgp_finger(X, c, decoder))
        obs["std_hand"].append(standard_accuracy(X, c, "hand", decoder))
        obs["std_within"].append(standard_accuracy(X, c, "finger_within", decoder))
        obs["std_both"].append(standard_accuracy(X, c, "finger_both", decoder))
    out = {k: float(np.mean(v)) for k, v in obs.items()}
    null_h, null_f = [], []
    X, c = pseudo_population(Xs, ys, o6, rng)
    for _ in range(n_shuffles):
        if o6 == "b":
            X, c = pseudo_population(Xs, ys, o6, rng)
        cs = shuffle_conditions(c, rng)
        null_h.append(ccgp_hand(X, cs, decoder))
        null_f.append(ccgp_finger(X, cs, decoder))
    null_h, null_f = np.array(null_h), np.array(null_f)
    out["p_hand"] = float((1 + (null_h >= out["hand"]).sum()) / (1 + n_shuffles))
    out["p_finger"] = float((1 + (null_f >= out["finger"]).sum()) / (1 + n_shuffles))
    out["null_hand_mean"], out["null_hand_max"] = float(null_h.mean()), float(null_h.max())
    out["null_finger_mean"], out["null_finger_max"] = float(null_f.mean()), float(null_f.max())
    out["n_neurons"] = int(sum(x.shape[1] for x in Xs))
    return out


def ndc_finger(Xs: list, ys: list, sizes, n_sub: int, o6: str, decoder: str, rng):
    """Finger-type CCGP for random subsets of the pooled neurons (Methods, Offline
    classification: neuron-dropping curves from random subsets of neurons stacked across
    sessions). For o6 'b' each subset gets a fresh random matching."""
    X, c = pseudo_population(Xs, ys, o6, rng)
    res = {}
    for n in sizes:
        v = []
        for _ in range(n_sub):
            if o6 == "b":
                X, c = pseudo_population(Xs, ys, o6, rng)
            cols = rng.choice(X.shape[1], n, replace=False)
            v.append(ccgp_finger(X[:, cols], c, decoder))
        res[n] = (float(np.mean(v)), float(np.std(v)))
    return res


def classical_mds(D2: np.ndarray, k: int = 2) -> np.ndarray:
    """Classical MDS of squared distances (negative cross-validated values clipped at 0)."""
    D2 = np.clip(D2, 0, None)
    n = len(D2)
    J = np.eye(n) - 1 / n
    B = -0.5 * J @ D2 @ J
    w, v = np.linalg.eigh(B)
    i = np.argsort(w)[::-1][:k]
    return v[:, i] * np.sqrt(np.clip(w[i], 0, None))


def gpa(configs: list, n_iter: int = 20) -> list:
    """Generalized Procrustes analysis with scaling: each configuration centred and
    rotated/scaled to the running mean (used only to draw Figure 8d)."""
    from scipy.linalg import orthogonal_procrustes
    Y = [c - c.mean(axis=0) for c in configs]
    Y = [y / np.linalg.norm(y) for y in Y]
    ref = Y[0]
    for _ in range(n_iter):
        out = []
        for y in Y:
            R, s = orthogonal_procrustes(y, ref)
            out.append(y @ R * s / (np.linalg.norm(y) ** 2))
        ref = np.mean(out, axis=0)
        ref = ref / np.linalg.norm(ref)
    return out
EOF
cd $TMPDIR && . dev/bin/activate && uv pip install -q nbconvert ipykernel nbformat && date -u
```

```
Wed Nov  4 12:09:18 UTC 2026
Shell cwd was reset to
```

**Agent**

Time one heavy CCGP run (SVM, O6 b, N-PPC) before deciding the reading grid:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > proto7.py <<'EOF'
import sys, time, pickle, warnings; warnings.filterwarnings('ignore'); sys.path.insert(0,'entries/000252-guan-2022')
import fingers as F, numpy as np
S=pickle.load(open('S.pkl','rb'))
def sess_of(arr): return [s for s in S if s.subject==F.ARRAYS[arr][0]]
for arr in ['N-PPC','J-MC']:
  for dec in ['lda','svm']:
    Xs,ys=zip(*[F.array_data(s,arr,'a') for s in sess_of(arr)])
    t=time.time(); r=F.run_ccgp(list(Xs),list(ys),'b',dec,np.random.default_rng(0),n_shuffles=100)
    print(arr,dec,{k:round(v,3) for k,v in r.items()}, 'time(100 shuffles)',round(time.time()-t,1))
EOF
python proto7.py 2>&1 | grep -v Warn
```

```
N-PPC lda {'hand': 0.985, 'finger': 0.946, 'std_hand': 0.996, 'std_within': 0.994, 'std_both': 0.991, 'p_hand': 0.01, 'p_finger': 0.01, 'null_hand_mean': 0.481, 'null_hand_max': 0.6, 'null_finger_mean': 0.189, 'null_finger_max': 0.3, 'n_neurons': 943} time(100 shuffles) 2.9
N-PPC svm {'hand': 0.976, 'finger': 0.918, 'std_hand': 0.997, 'std_within': 0.99, 'std_both': 0.992, 'p_hand': 0.01, 'p_finger': 0.01, 'null_hand_mean': 0.487, 'null_hand_max': 0.65, 'null_finger_mean': 0.191, 'null_finger_max': 0.31, 'n_neurons': 943} time(100 shuffles) 22.0
J-MC lda {'hand': 0.865, 'finger': 0.782, 'std_hand': 0.887, 'std_within': 0.956, 'std_both': 0.919, 'p_hand': 0.01, 'p_finger': 0.01, 'null_hand_mean': 0.505, 'null_hand_max': 0.62, 'null_finger_mean': 0.204, 'null_finger_max': 0.33, 'n_neurons': 252} time(100 shuffles) 0.7
J-MC svm {'hand': 0.863, 'finger': 0.736, 'std_hand': 0.939, 'std_within': 0.955, 'std_both': 0.948, 'p_hand': 0.01, 'p_finger': 0.01, 'null_hand_mean': 0.505, 'null_hand_max': 0.68, 'null_finger_mean': 0.207, 'null_finger_max': 0.33, 'n_neurons': 252} time(100 shuffles) 11.1
Shell cwd was reset to
```

**Agent**

A full SVM run with 1001 shuffles costs about a minute per array, so the whole CCGP grid fits in about 8 minutes. Now I write the notebook builder.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Guan et al. (preprint 2022) from dandiset 000252\n\n**Paper.** Guan, Aflalo, Kadlec, Gámez de Leon, Rosario, Bari, Pouratian and Andersen, \"Compositional coding of individual finger movements in human posterior parietal cortex and motor cortex enables ten-finger decoding\", medRxiv/bioRxiv preprint, doi:10.1101/2022.12.07.22283227.\n\n**Dataset.** DANDI:000252, \"Finger_RL: human intracortical recordings during attempted finger movements of right and left hands\", version **0.230408.2207** (doi:10.48324/dandi.000252/0.230408.2207). The paper cites no version (its Data Availability gives only the dandiset URL), and 0.230408.2207 is the only published version, so it is pinned. The draft was modified later (2023-06-20) but lists the same 12 assets with the same asset identifiers; the check below prints this.\n\n**Text the claims file was written from.** The bioRxiv preprint, version 1, full text with Methods and the supplementary figure legends (claims file `claims/000252/10.1101-2022.12.07.22283227.yaml`). The paper links no analysis code.\n\n**What the dataset holds.** Only the ten-finger press task: 10 sessions of participant N (subject `P1` in the files) and 2 of participant J (subject `N1`). The alternating-cues task (Figures 4 and 5) and the BMI tasks (Figure 6, Supplementary Figures 6 and 7) are not in it.\n\n| Claim | Tested here |\n|---|---|\n| tenfinger-recording-counts | tested |\n| tenfinger-pooled-npcc-neurons | tested |\n| tenfinger-discriminative-fraction | tested |\n| tenfinger-decoding-accuracy | tested |\n| tenfinger-error-structure | tested |\n| fig8b-matching-closer | tested |\n| fig8a-npcc-index-distinct | tested |\n| fig8e-hand-ccgp | tested |\n| fig8e-finger-ccgp | tested |\n| jppc-finger-ccgp-low | tested |\n| figs11-jppc-lower-matched-size | tested |\n| fig4c-contra-discriminative | blocked, data_missing (alternating-cues task not in the dataset) |\n| fig4e-plan-vs-move | blocked, data_missing |\n| fig5a-contra-decoding | blocked, data_missing |\n| fig5bcd-npcc-data-requirements | blocked, data_missing |\n| fig5e-planning-decoding | blocked, data_missing |\n| fig6-online-bmi | blocked, data_missing (BMI sessions not in the dataset) |\n| figs6-single-array-retrospective | blocked, data_missing |\n| figs7-left-hand-bmi | blocked, data_missing |\n\nThe readings O1 to O11 named below are those of the claims file's header.\n\"\"\")\n\ncode(r\"\"\"\nimport os, time, warnings\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nwarnings.filterwarnings(\"ignore\")\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy.stats import bootstrap\nimport requests\nimport fingers as F\n\npd.set_option(\"display.width\", 200)\nBLUE, ORANGE = \"#2a78d6\", \"#eb6834\"\nT0 = time.time()\nprint(\"dandiset\", F.DANDISET_ID, \"version\", F.VERSION)\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nmeta = F.version_metadata()\nprint(\"title:\", meta[\"name\"])\nprint(\"related:\", [(r.get(\"relation\"), r.get(\"identifier\")) for r in meta.get(\"relatedResource\", [])])\nassets = F.list_assets()\ndraft = requests.get(f\"{F.API}/dandisets/{F.DANDISET_ID}/versions/draft/assets/?page_size=200\").json()[\"results\"]\nprint(\"assets in version:\", len(assets), \"| in draft:\", len(draft),\n      \"| same asset ids:\", {a[\"asset_id\"] for a in assets} == {a[\"asset_id\"] for a in draft})\nt = time.time()\nS = [F.load_session(a) for a in assets]\nprint(f\"loaded {len(S)} files in {time.time() - t:.0f} s\")\n\nrows = []\nfor s in S:\n    tr = s.trials\n    rows.append(dict(\n        file=s.path.split(\"/\")[-1], subject=s.subject, sex=s.sex, date=s.date, task=s.description,\n        trials=len(tr), runs=tr.Run.nunique(), per_condition=f\"{tr.finger.value_counts().min()}-{tr.finger.value_counts().max()}\",\n        units_PPC=int((s.group == \"PPC\").sum()), units_MC=int((s.group == \"MC\").sum()),\n        electrodes=s.extra[\"electrode_groups\"], unsorted_units=s.n_unsorted, spikes_outside_obs=s.n_outside_obs))\nsummary = pd.DataFrame(rows)\nprint(summary.to_string())\nfor s in S[:1] + S[2:3]:\n    print(s.subject, s.sex, s.extra[\"electrode_locations\"])\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Conditions, phase durations and units of the variables used\ns0 = S[0]\nprint(\"conditions:\", sorted(s0.trials.finger.unique()), \"| hand:\", sorted(s0.trials.hand.unique()),\n      \"| finger_type:\", sorted(s0.trials.finger_type.unique()))\nprint(\"finger == hand + finger_type in every trial:\",\n      all((s.trials.finger == s.trials.hand + s.trials.finger_type).all() for s in S))\ndur = []\nfor s in S:\n    tr = s.trials\n    dur.append(dict(file=s.path.split(\"/\")[-1],\n                    iti=(tr.cue_on_time - tr.start_time).median(), cue=(tr.cue_off_time - tr.cue_on_time).median(),\n                    delay_min=(tr.go_on_time - tr.cue_off_time).min(), delay_max=(tr.go_on_time - tr.cue_off_time).max(),\n                    go=(tr.stop_time - tr.go_on_time).median(), go_min=(tr.stop_time - tr.go_on_time).min(),\n                    ordered=bool(((tr.start_time <= tr.cue_on_time) & (tr.cue_on_time < tr.cue_off_time) &\n                                  (tr.cue_off_time < tr.go_on_time) & (tr.go_on_time < tr.stop_time)).all())))\nprint(\"phase durations, s (median unless stated):\")\nprint(pd.DataFrame(dur).round(2).to_string())\nallrates = np.concatenate([F.rates(s, \"go\").ravel() for s in S])\nprint(f\"Go-window rates (Hz): min {allrates.min():.1f}, median {np.median(allrates):.1f}, max {allrates.max():.1f}\")\nprint(\"spike-time range per file (s):\", [(round(min(x.min() for x in s.spikes if len(x))), round(max(x.max() for x in s.spikes if len(x)))) for s in S])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe files name participant N `P1` (female, one PPC array at PC-IP) and participant J `N1` (male, PPC array in SPL and MC array near the hand knob), as the sex and electrode locations above show. The subject identifier `N1` is participant J, not N. Every Go phase lasts at least the 0.7 s the Go window needs.\n\"\"\")\n\ncode(r\"\"\"\n# Recordings deposited twice: compare trial times and spike trains between all pairs of files\ndups = []\nfor i in range(len(S)):\n    for j in range(i + 1, len(S)):\n        a, b = S[i], S[j]\n        same_trials = len(a.trials) == len(b.trials) and np.allclose(a.trials.go_on_time.values, b.trials.go_on_time.values)\n        sa = {tuple(np.round(x[:30], 4)) for x in a.spikes}\n        sb = {tuple(np.round(x[:30], 4)) for x in b.spikes}\n        if same_trials or (sa & sb):\n            dups.append((a.path, b.path, same_trials, len(sa & sb)))\nprint(\"pairs of files with identical trial times or identical spike trains:\", dups if dups else \"none\")\nwithin = sum(len(s.spikes) - len({tuple(np.round(x[:30], 4)) for x in s.spikes}) for s in S)\nprint(\"units with an identical spike train to another unit of the same file:\", within)\n\"\"\", tags=[\"sanity\"])\n\ncode(r\"\"\"\n# Clock check: decode the cued finger in 500 ms windows starting from -3 s to +1.5 s around the Go cue,\n# and with the labels shuffled. The ITI should be at chance; decoding should rise after the cue and Go.\nrng = np.random.default_rng(1)\nstarts = np.round(np.arange(-3.0, 1.51, 0.5), 2)\ntc = {}\nfor arr in F.ARRAYS:\n    accs, sh = [], []\n    for t0 in starts:\n        T, P, Psh = [], [], []\n        for s in [s for s in S if s.subject == F.ARRAYS[arr][0]]:\n            m = (s.group == F.ARRAYS[arr][1]) & F.keep_mask(s, \"a\")\n            X = F.counts(s.spikes, s.trials.go_on_time.values, t0, 0.5)[:, m] / 0.5\n            y = s.trials.finger.values\n            T.append(y); P.append(F.cv_predict(X, y)); Psh.append(F.cv_predict(X, rng.permutation(y)))\n        T = np.concatenate(T)\n        accs.append(np.mean(T == np.concatenate(P)))\n    tc[arr] = accs\nprint(\"window start rel. Go (s):\", list(starts))\nfor arr, a in tc.items():\n    print(f\"{arr:6s} accuracy:\", np.round(a, 2).tolist())\n# per-session ITI and Go accuracy, and with labels shuffled\nfor s in S:\n    for arr in [a for a in F.ARRAYS if F.ARRAYS[a][0] == s.subject]:\n        X_go, y = F.array_data(s, arr, \"a\", \"go\"); X_iti, _ = F.array_data(s, arr, \"a\", \"iti\")\n        print(f\"{s.subject} {s.date} {arr:6s} Go {np.mean(F.cv_predict(X_go, y) == y):.2f}  ITI {np.mean(F.cv_predict(X_iti, y) == y):.2f}\"\n              f\"  Go with shuffled labels {np.mean(F.cv_predict(X_go, rng.permutation(y)) == y):.2f}  (chance 0.10)\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nChecks of the description against the data are stated after the outputs above: the condition labels, the per-session trial counts and the arrays are as the paper describes; the trial phases are in the order ITI, Cue, Delay, Go in every trial; Go-window decoding is high in every session while the ITI and shuffled labels are near the 10% chance, so spikes and trial table share a clock in each of the 12 sessions; the units' spike times are stored out of time order (sorted here before counting).\n\"\"\")\n\n# ------------------------------------------------------------------ claims\nmd(r\"\"\"\n## tenfinger-recording-counts and tenfinger-pooled-npcc-neurons\n\n> In the ten-finger task, N-PPC yielded 111 neurons per session (102 to 119) over 10 sessions of 100 trials, J-PPC 160 (159 to 160) and J-MC 130 (120 to 130) over 2 sessions of 100 trials.\n\n> 1111 N-PPC neurons were recorded across the 10 sessions of the ten-finger task.\n\nCounted before the 0.5 Hz exclusion and under both readings of O1: (a) mean rate over the unit's observed time (`obs_intervals`), (b) mean Go-window rate over all trials.\n\"\"\")\n\ncode(r\"\"\"\ndef sess_of(arr):\n    return [s for s in S if s.subject == F.ARRAYS[arr][0]]\n\ncount_rows = []\nfor o1 in [\"none\", \"a\", \"b\"]:\n    for arr in F.ARRAYS:\n        n = [int(F.keep_mask(s, o1)[s.group == F.ARRAYS[arr][1]].sum()) for s in sess_of(arr)]\n        count_rows.append(dict(O1=o1, array=arr, sessions=len(n), per_session=n, mean=np.mean(n), min=min(n), max=max(n), pooled=sum(n)))\ncounts_df = pd.DataFrame(count_rows)\nprint(counts_df.to_string())\nprint(\"trials per session:\", sorted({len(s.trials) for s in S}))\n\"\"\", tags=[\"claim:tenfinger-recording-counts\", \"claim:tenfinger-pooled-npcc-neurons\"])\n\nmd(r\"\"\"\n**Result: reproduced, before the exclusion.** The dataset has 10 N sessions and 2 J sessions of 100 trials each. Before the 0.5 Hz exclusion, N-PPC has a mean of 111.4 units per session (102 to 119), J-PPC 159.5 (159 to 160) and J-MC 129.5 (120 to 139). The J-MC maximum is 139 against the paper's 130, inside the 10% widening of that bound (143). After the exclusion the N-PPC mean falls to 94.3 (O1 a) or 93.0 (O1 b), outside tolerance, so the paper's counts are those before exclusion. Pooled over sessions, N-PPC has 1114 units before the exclusion (paper 1111), and 943 or 930 after it.\n\"\"\")\n\nmd(r\"\"\"\n## tenfinger-discriminative-fraction\n\n> Most neurons discriminate firing rates across the ten fingers (N-PPC 66%, J-PPC 57%, J-MC 78%, q < 0.05).\n\nOne-way ANOVA of Go-window rates across the ten conditions, Benjamini-Hochberg over all neurons of the array pooled across sessions (Methods, Single-neuron selectivity). Readings of O1. Variants, not readings of the criterion: no FDR correction, FDR per session, other analysis windows.\n\"\"\")\n\ncode(r\"\"\"\nsel_rows = []\nfor o1 in [\"none\", \"a\", \"b\"]:\n    for arr in F.ARRAYS:\n        ps, per_sess = [], []\n        for s in sess_of(arr):\n            X, y = F.array_data(s, arr, o1)\n            p, _ = F.anova_eta2(X, y)\n            ps.append(p)\n            per_sess.append(np.mean(F.fdr_bh(p) < 0.05))\n        p = np.concatenate(ps)\n        q = F.fdr_bh(p)\n        sel_rows.append(dict(O1=o1, array=arr, neurons=len(p), constant_units=int(np.isnan(p).sum()),\n                             pct_q05=100 * np.mean(q < 0.05), pct_uncorrected_p05=100 * np.mean(np.nan_to_num(p, nan=1) < 0.05),\n                             pct_FDR_per_session_mean=100 * np.mean(per_sess),\n                             per_session_pct=np.round(100 * np.array(per_sess)).astype(int).tolist()))\nsel_df = pd.DataFrame(sel_rows)\nprint(sel_df.round(1).to_string())\nprint(\"paper: N-PPC 66, J-PPC 57, J-MC 78 (tolerance 10%)\")\n# variant: other windows (O1 a)\nfor arr in F.ARRAYS:\n    out = {}\n    for w in [\"iti\", \"cue\", \"delay\", \"go\"]:\n        p = np.concatenate([F.anova_eta2(*F.array_data(s, arr, \"a\", w))[0] for s in sess_of(arr)])\n        out[w] = round(100 * np.mean(F.fdr_bh(p) < 0.05), 1)\n    print(arr, \"percent q < 0.05 by window (O1 a):\", out)\n\"\"\", tags=[\"claim:tenfinger-discriminative-fraction\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** Under every reading of O1 the Go-window percentages of discriminative neurons are 40 to 49% for N-PPC, 38% for J-PPC and 64 to 66% for J-MC, against 66%, 57% and 78%; all three are below the lower tolerance bounds (59.4%, 51.3% and 70.2%). Without FDR correction the percentages are still lower than the paper's (at most 55%, 46% and 69%), and no other analysis window gives more. The ordering of the arrays (J-MC highest) is as in the paper.\n\"\"\")\n\nmd(r\"\"\"\n## tenfinger-decoding-accuracy and tenfinger-error-structure\n\n> A linear classifier discriminates all ten fingers well above the 10% chance level (cross-validated accuracy N-PPC 70%, J-PPC 66%, J-MC 75%).\n\n> Most ten-finger classification errors confuse an adjacent finger of the same hand or the matching finger of the other hand (N-PPC 76%, J-PPC 66%, J-MC 68% of errors).\n\nDiagonal LDA per session, stratified 8-fold cross-validation, held-out predictions pooled over sessions (Methods, Offline classification). Readings O1 x O2; O2 (b) is averaged over seeds 0 to 9.\n\"\"\")\n\ncode(r\"\"\"\ndec_rows, confusions = [], {}\nfor o1 in [\"a\", \"b\", \"none\"]:\n    for o2 in [\"a\", \"b\"]:\n        for arr in F.ARRAYS:\n            acc, share, per_sess = [], [], []\n            for seed in (range(10) if o2 == \"b\" else [0]):\n                T, P = [], []\n                for s in sess_of(arr):\n                    X, y = F.array_data(s, arr, o1)\n                    p = F.cv_predict(X, y, o2, seed)\n                    T.append(y); P.append(p)\n                    if seed == 0:\n                        per_sess.append(round(np.mean(p == y), 2))\n                T, P = np.concatenate(T), np.concatenate(P)\n                e, adj, mat = F.error_kinds(T, P)\n                acc.append(np.mean(T == P)); share.append((adj + mat) / e)\n                if (o1, o2, seed) == (\"a\", \"a\", 0):\n                    confusions[arr] = pd.crosstab(pd.Series(T, name=\"true\"), pd.Series(P, name=\"pred\")).reindex(index=F.CONDITIONS, columns=F.CONDITIONS, fill_value=0)\n            dec_rows.append(dict(O1=o1, O2=o2, array=arr, trials=len(T), accuracy=100 * np.mean(acc), acc_min_seed=100 * min(acc),\n                                 acc_max_seed=100 * max(acc), errors=e, adjacent=adj, matching=mat,\n                                 share_adj_or_match=100 * np.mean(share), per_session_acc=per_sess))\ndec_df = pd.DataFrame(dec_rows)\nprint(dec_df.round(1).to_string())\nprint(\"paper accuracy: N-PPC 70, J-PPC 66, J-MC 75 (chance 10); error share: 76, 66, 68\")\n\"\"\", tags=[\"claim:tenfinger-decoding-accuracy\", \"claim:tenfinger-error-structure\"])\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 3, figsize=(13, 4))\nfor ax, (arr, cm) in zip(axes, confusions.items()):\n    frac = cm.values / cm.values.sum(axis=1, keepdims=True)\n    im = ax.imshow(frac, cmap=\"Blues\", vmin=0, vmax=1)\n    ax.set_xticks(range(10), F.CONDITIONS, fontsize=8); ax.set_yticks(range(10), F.CONDITIONS, fontsize=8)\n    ax.set_title(f\"{arr}, O1 a, O2 a\"); ax.set_xlabel(\"predicted\"); ax.set_ylabel(\"cued\")\nfig.colorbar(im, ax=axes, shrink=0.8, label=\"fraction of cued trials\")\nplt.show()\nprint(\"confusion fractions are in [0, 1]; colour scale 0 to 1, no value outside it\")\n\"\"\", tags=[\"claim:tenfinger-decoding-accuracy\"])\n\nmd(r\"\"\"\n**Result: tenfinger-decoding-accuracy reproduced.** Under every reading of O1 and O2 the pooled accuracies are 71 to 73% for N-PPC (1000 trials), 68 to 70% for J-PPC and 78 to 79% for J-MC (200 trials each), within the tolerances of 70%, 66% and 75%, against a chance of 10%. The single seeds of O2 (b) stay within tolerance as well.\n\n**Result: tenfinger-error-structure reproduced.** Of the errors, 74 to 77% (N-PPC), 66 to 72% (J-PPC) and 63 to 65% (J-MC) confuse an adjacent finger of the same hand or the matching finger of the other hand; every value is within tolerance of 76%, 66% and 68% under every reading.\n\"\"\")\n\nmd(r\"\"\"\n## fig8b-matching-closer\n\n> Matching right and left finger pairs are closer in neural distance than non-matching pairs, by 1.56 units in N-PPC (95% CI 1.33 to 1.78) and 4.30 in J-MC (2.74 to 5.46), but not conclusively in J-PPC (0.27, -0.17 to 0.64).\n\nCross-validated squared Mahalanobis distances (rsatoolbox), per session and array, on Go-window rates; readings O1 x O3 x O4. For O4 (a) the per-partition precision is multiplied by the number of trials per condition in the partition (5), because rsatoolbox's `calc_rdm_crossnobis` documents that a list of noises must be \"the precision of the mean from the corresponding crossvalidation fold\". This is an assumption about how the paper called the toolbox; O4 (a1), the unscaled single-trial precision, is shown as a variant. The 95% CI is DABEST's (O5 a, BCa bootstrap of the difference of means, 5000 resamples, each group resampled on its own) and the percentile bootstrap (O5 b).\n\"\"\")\n\ncode(r\"\"\"\nrdms, rdm_rows = {}, []\nfor o1 in [\"a\", \"b\"]:\n    for o3 in [\"shrinkage_diag\", \"shrinkage_eye\", \"diag\"]:\n        for o4 in [\"a\", \"b\", \"a1\"]:\n            for arr in F.ARRAYS:\n                M, N, R, dropped = [], [], [], []\n                for s in sess_of(arr):\n                    X, y = F.array_data(s, arr, o1)\n                    rdm, nd = F.crossnobis_rdm(X, y, o3, o4)\n                    m, n = F.cross_hand_elements(rdm)\n                    M += list(m); N += list(n); R.append(rdm); dropped.append(nd)\n                M, N = np.array(M), np.array(N)\n                rdms[(o1, o3, o4, arr)] = R\n                stat = lambda a, b, axis=-1: a.mean(axis) - b.mean(axis)\n                row = dict(O1=o1, O3=o3, O4=o4, array=arr, n_match=len(M), n_non=len(N), dropped_units=sum(dropped),\n                           match_mean=M.mean(), non_mean=N.mean(), diff=N.mean() - M.mean())\n                for meth, lab in [(\"BCa\", \"bca\"), (\"percentile\", \"pct\")]:\n                    ci = bootstrap((N, M), stat, n_resamples=5000, method=meth, vectorized=True,\n                                   random_state=np.random.default_rng(8)).confidence_interval\n                    row[f\"{lab}_low\"], row[f\"{lab}_high\"] = ci.low, ci.high\n                rdm_rows.append(row)\nrdm_df = pd.DataFrame(rdm_rows)\nexp = {\"N-PPC\": (1.56, 0.23), \"J-MC\": (4.30, 1.56), \"J-PPC\": (0.27, 0.44)}\nrdm_df[\"in_tol\"] = [abs(r[\"diff\"] - exp[r[\"array\"]][0]) <= exp[r[\"array\"]][1] for _, r in rdm_df.iterrows()]\nprint(rdm_df.round(2).to_string())\n\"\"\", tags=[\"claim:fig8b-matching-closer\"])\n\ncode(r\"\"\"\ndef verdict(g):\n    d = g.set_index(\"array\")\n    pos = all(d.loc[a, \"diff\"] > 0 and d.loc[a, \"bca_low\"] > 0 for a in [\"N-PPC\", \"J-MC\"])\n    jppc = d.loc[\"J-PPC\", \"bca_low\"] <= 0 <= d.loc[\"J-PPC\", \"bca_high\"]\n    tol = bool(d[\"in_tol\"].all())\n    return pd.Series(dict(NPPC_JMC_positive_CI_excl_0=pos, JPPC_CI_includes_0=jppc, all_in_tol=tol,\n                          N_PPC=round(d.loc[\"N-PPC\", \"diff\"], 2), J_MC=round(d.loc[\"J-MC\", \"diff\"], 2), J_PPC=round(d.loc[\"J-PPC\", \"diff\"], 2)))\nprint(\"per reading (CI by O5 a, BCa):\")\nprint(rdm_df.groupby([\"O1\", \"O3\", \"O4\"]).apply(verdict).to_string())\njp = rdm_df[rdm_df.array == \"J-PPC\"]\nprint(\"J-PPC percentile CI includes 0 in\", int(((jp.pct_low <= 0) & (jp.pct_high >= 0)).sum()), \"of\", len(jp), \"readings\")\n\nkey = (\"a\", \"shrinkage_diag\", \"a\")\nfig, axes = plt.subplots(1, 2, figsize=(11, 4))\nA = np.mean(rdms[key + (\"N-PPC\",)], axis=0)\nim = axes[0].imshow(A, cmap=\"Blues\")\naxes[0].set_xticks(range(10), F.CONDITIONS, fontsize=8); axes[0].set_yticks(range(10), F.CONDITIONS, fontsize=8)\naxes[0].set_title(\"N-PPC distances, mean of 10 sessions (O1 a, O3 a, O4 a)\")\nfig.colorbar(im, ax=axes[0], shrink=0.8)\nprint(f\"N-PPC mean RDM range {A.min():.2f} to {A.max():.2f}\")\nfor i, arr in enumerate(F.ARRAYS):\n    M, N = [], []\n    for r in rdms[key + (arr,)]:\n        m, n = F.cross_hand_elements(r); M += list(m); N += list(n)\n    jit = np.random.default_rng(9)\n    axes[1].scatter(i - 0.15 + 0.05 * jit.standard_normal(len(M)), M, s=12, color=BLUE, label=\"matching\" if i == 0 else None)\n    axes[1].scatter(i + 0.15 + 0.05 * jit.standard_normal(len(N)), N, s=12, color=ORANGE, label=\"non-matching\" if i == 0 else None)\n    print(f\"{arr}: matching {min(M):.2f} to {max(M):.2f}, non-matching {min(N):.2f} to {max(N):.2f}\")\naxes[1].set_xticks(range(3), list(F.ARRAYS)); axes[1].set_ylabel(\"cross-validated distance (per neuron)\")\naxes[1].legend(frameon=False); axes[1].set_title(\"different-hand RDM elements, all sessions\")\nplt.show()\n\"\"\", tags=[\"claim:fig8b-matching-closer\"])\n\nmd(r\"\"\"\n**Result: reproduced, resting on an assumption.** Under O4 (a), with the toolbox's per-partition precision of the mean, the non-matching minus matching difference is 1.42 to 1.71 in N-PPC, 2.99 to 3.38 in J-MC and 0.19 to 0.22 in J-PPC over the readings of O1 and O3; N-PPC and J-MC have positive differences with BCa CIs above 0, the J-PPC CI includes 0, and all values are within tolerance except N-PPC under shrinkage toward identity (1.70 and 1.71 against an upper bound of 1.79, still in; see the table). Under O4 (b) and the variant O4 (a1) the same pattern holds (positive CIs excluding 0 for N-PPC and J-MC, J-PPC CI including 0) but the differences are about a fifth as large (N-PPC 0.28 to 0.36, J-MC 0.51 to 0.68), outside tolerance, which would be partially reproduced. The outcome therefore rests on how rsatoolbox's noise argument was scaled, which the paper does not state.\n\"\"\")\n\nmd(r\"\"\"\n## fig8a-npcc-index-distinct\n\n> In N-PPC the inter-finger geometry is similar across hands, with the index finger relatively distinct from the middle and ring fingers in both hands.\n\nFrom the N-PPC distances of fig8b-matching-closer averaged over the 10 sessions; reproduced when in each hand the index-middle and index-ring distances both exceed the middle-ring distance, under one reading. MDS with Generalized Procrustes alignment, as the Methods describe, is drawn for index, middle and ring.\n\"\"\")\n\ncode(r\"\"\"\nix = {c: i for i, c in enumerate(F.CONDITIONS)}\nrows = []\nfor (o1, o3, o4, arr), R in rdms.items():\n    if arr != \"N-PPC\":\n        continue\n    A = np.mean(R, axis=0)\n    r = dict(O1=o1, O3=o3, O4=o4)\n    ok = True\n    for h in \"RL\":\n        im_, ir_, mr_ = A[ix[h + \"i\"], ix[h + \"m\"]], A[ix[h + \"i\"], ix[h + \"r\"]], A[ix[h + \"m\"], ix[h + \"r\"]]\n        r.update({f\"{h}_IM\": im_, f\"{h}_IR\": ir_, f\"{h}_MR\": mr_})\n        ok &= (im_ > mr_) and (ir_ > mr_)\n    # per-session count of sessions where the pattern holds in both hands\n    n_ok = 0\n    for Rs in R:\n        n_ok += all(Rs[ix[h + \"i\"], ix[h + \"m\"]] > Rs[ix[h + \"m\"], ix[h + \"r\"]] and Rs[ix[h + \"i\"], ix[h + \"r\"]] > Rs[ix[h + \"m\"], ix[h + \"r\"]] for h in \"RL\")\n    r.update(pattern_both_hands=ok, sessions_with_pattern=n_ok)\n    rows.append(r)\nprint(pd.DataFrame(rows).round(2).to_string())\n\nsub = [c for c in F.CONDITIONS if c[1] in \"imr\"]\nsi = [ix[c] for c in sub]\nconfs = [F.classical_mds(Rs[np.ix_(si, si)]) for Rs in rdms[(\"a\", \"shrinkage_diag\", \"a\", \"N-PPC\")]]\naligned = np.array(F.gpa(confs))\nmean, se = aligned.mean(axis=0), aligned.std(axis=0, ddof=1) / np.sqrt(len(aligned))\nfig, ax = plt.subplots(figsize=(4.5, 4.5))\nfor k, c in enumerate(sub):\n    col = BLUE if c[0] == \"R\" else ORANGE\n    ax.errorbar(mean[k, 0], mean[k, 1], xerr=se[k, 0], yerr=se[k, 1], fmt=\"o\", color=col, ms=8)\n    ax.annotate(c, mean[k], textcoords=\"offset points\", xytext=(6, 6))\nfor h, col in [(\"R\", BLUE), (\"L\", ORANGE)]:\n    pts = np.array([mean[sub.index(h + f)] for f in \"imr\"])\n    ax.plot(pts[:, 0], pts[:, 1], color=col, lw=2)\nax.set_title(\"N-PPC MDS, GPA over 10 sessions (mean, SE)\")\nax.set_xticks([]); ax.set_yticks([])\nplt.show()\nprint(\"MDS coordinates (mean over sessions, arbitrary scale):\")\nprint(pd.DataFrame(mean, index=sub, columns=[\"x\", \"y\"]).round(3).to_string())\n\"\"\", tags=[\"claim:fig8a-npcc-index-distinct\"])\n\nmd(r\"\"\"\n**Result: reproduced.** In the N-PPC distances averaged over the 10 sessions, under every reading of O1, O3 and O4, the index-middle and index-ring distances exceed the middle-ring distance in both hands (for example, O4 (a) with diagonal shrinkage: right hand 2.16 and 2.96 against 0.62, left hand 1.30 and 2.23 against 0.57). The session counts in the table say how often the pattern holds in single sessions.\n\"\"\")\n\nmd(r\"\"\"\n## fig8e-hand-ccgp, fig8e-finger-ccgp and jppc-finger-ccgp-low\n\n> Hand (left against right) decoders trained on four finger types generalize to the held-out finger type significantly above chance (p < 0.001, permutation test), with hand CCGP close to standard decoding accuracy, in N-PPC, J-MC and J-PPC.\n\n> Finger-type decoders trained on one hand generalize to the other hand significantly above chance (p < 0.001), with finger-type CCGP close to standard decoding accuracy, in N-PPC and J-MC.\n\n> J-PPC finger representations are less compositional; finger-type CCGP (36%) is above chance (p < 0.001) but much lower than within-hand accuracy (65%).\n\nPseudo-population of the array's neurons over sessions (O6), Go-window rates, decoders O7 (a, diagonal LDA; b, linear SVM), 1001 label shuffles, p = (1 + shuffles reaching the observed CCGP) / 1002, so p < 0.001 means no shuffle reached it. Standard accuracy (8-fold, O2 a) is computed on the same pseudo-population, since the Methods call it \"an upper bound on CCGP\"; this is an assumption (the paper does not say which population), and the per-session standard accuracy (Methods, Offline classification: \"a separate linear classifier for each session\") is shown as a variant. Closeness by O9: (a) CCGP at least 0.9 of standard accuracy; (b) ratio above 0.55. Finger standard accuracy by O8: (a) within hand, (b) over both hands.\n\"\"\")\n\ncode(r\"\"\"\nt = time.time()\nccgp_rows = []\nfor o1 in [\"a\", \"b\"]:\n    for o6 in [\"a\", \"b\"]:\n        for o7 in [\"lda\", \"svm\"]:\n            for k, arr in enumerate(F.ARRAYS):\n                Xs, ys = zip(*[F.array_data(s, arr, o1) for s in sess_of(arr)])\n                rng = np.random.default_rng(1000 + k)   # this section's own generator, per array\n                r = F.run_ccgp(list(Xs), list(ys), o6, o7, rng)\n                ccgp_rows.append(dict(O1=o1, O6=o6, O7=o7, array=arr, **r))\nccgp_df = pd.DataFrame(ccgp_rows)\nccgp_df[\"hand_ratio\"] = ccgp_df.hand / ccgp_df.std_hand\nccgp_df[\"finger_ratio_O8a\"] = ccgp_df.finger / ccgp_df.std_within\nccgp_df[\"finger_ratio_O8b\"] = ccgp_df.finger / ccgp_df.std_both\nprint(f\"{time.time() - t:.0f} s\")\nprint(ccgp_df.round(3).to_string())\n\"\"\", tags=[\"claim:fig8e-hand-ccgp\", \"claim:fig8e-finger-ccgp\", \"claim:jppc-finger-ccgp-low\"])\n\ncode(r\"\"\"\n# Variant: standard accuracy per session (classifier per session, trials pooled), O1 a, O2 a\nvar_rows = []\nfor o7 in [\"lda\", \"svm\"]:\n    for arr in F.ARRAYS:\n        r = {}\n        for tgt in [\"hand\", \"finger_within\", \"finger_both\"]:\n            a, n = [], []\n            for s in sess_of(arr):\n                X, y = F.array_data(s, arr, \"a\")\n                a.append(F.standard_accuracy(X, y, tgt, o7)); n.append(len(y))\n            r[tgt] = np.average(a, weights=n)\n        var_rows.append(dict(O7=o7, array=arr, **r))\nprint(\"per-session standard accuracy (variant):\")\nprint(pd.DataFrame(var_rows).round(3).to_string())\n\ng = ccgp_df.groupby([\"O1\", \"O6\", \"O7\"])\nprint(\"\\nfig8e-hand-ccgp: every array p < 0.001 and hand ratio >= 0.9 (O9 a) / > 0.55 (O9 b):\")\nprint(g.apply(lambda d: pd.Series(dict(all_p=bool((d.p_hand < 0.001).all()), O9a=bool((d.hand_ratio >= 0.9).all()), O9b=bool((d.hand_ratio > 0.55).all()),\n                                       min_ratio=round(d.hand_ratio.min(), 3)))).to_string())\nprint(\"\\nfig8e-finger-ccgp (N-PPC and J-MC): p < 0.001 and finger ratio by O8 a/b and O9 a/b:\")\nnj = ccgp_df[ccgp_df.array.isin([\"N-PPC\", \"J-MC\"])].groupby([\"O1\", \"O6\", \"O7\"])\nprint(nj.apply(lambda d: pd.Series(dict(all_p=bool((d.p_finger < 0.001).all()),\n                                        O8a_O9a=bool((d.finger_ratio_O8a >= 0.9).all()), O8b_O9a=bool((d.finger_ratio_O8b >= 0.9).all()),\n                                        O8a_O9b=bool((d.finger_ratio_O8a > 0.55).all()), O8b_O9b=bool((d.finger_ratio_O8b > 0.55).all()),\n                                        JMC_ratio_O8a=round(d.set_index(\"array\").loc[\"J-MC\", \"finger_ratio_O8a\"], 3)))).to_string())\njp = ccgp_df[ccgp_df.array == \"J-PPC\"][[\"O1\", \"O6\", \"O7\", \"finger\", \"std_within\", \"std_both\", \"p_finger\", \"finger_ratio_O8a\"]].copy()\njp[\"ccgp_in_tol\"] = (jp.finger * 100 - 36).abs() <= 3.6\njp[\"within_in_tol\"] = (jp.std_within * 100 - 65).abs() <= 6.5\nprint(\"\\njppc-finger-ccgp-low (expected CCGP 36 +/- 3.6%, within-hand 65 +/- 6.5%):\")\nprint(jp.round(3).to_string())\n\"\"\", tags=[\"claim:fig8e-hand-ccgp\", \"claim:fig8e-finger-ccgp\", \"claim:jppc-finger-ccgp-low\"])\n\ncode(r\"\"\"\nd = ccgp_df[(ccgp_df.O1 == \"a\") & (ccgp_df.O6 == \"a\") & (ccgp_df.O7 == \"lda\")].set_index(\"array\")\nfig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)\nfor ax, (cc, sd, nul, title) in zip(axes, [(\"hand\", \"std_hand\", \"null_hand_mean\", \"hand\"), (\"finger\", \"std_within\", \"null_finger_mean\", \"finger type\")]):\n    x = np.arange(3)\n    ax.scatter(x - 0.1, d[cc], color=BLUE, s=60, label=\"CCGP\")\n    ax.scatter(x + 0.1, d[sd], color=ORANGE, marker=\"^\", s=60, label=\"standard accuracy\")\n    ax.scatter(x, d[nul], color=\"gray\", marker=\"_\", s=200, label=\"shuffle mean\")\n    ax.set_xticks(x, d.index); ax.set_ylim(0, 1.05); ax.set_title(f\"{title} (O1 a, O6 a, O7 a)\")\naxes[0].set_ylabel(\"accuracy\"); axes[0].legend(frameon=False, fontsize=8)\nplt.show()\nprint(\"all plotted values lie in [0, 1]\")\n\"\"\", tags=[\"claim:fig8e-hand-ccgp\", \"claim:fig8e-finger-ccgp\"])\n\nmd(r\"\"\"\n**Result: fig8e-hand-ccgp reproduced.** In all three arrays, under every reading of O1, O6 and O7, no shuffle reached the observed hand CCGP (p = 1/1002 < 0.001), and hand CCGP is at least 0.9 of the hand accuracy on the same pseudo-population (O9 a; the smallest ratio is printed above), so it is also above 0.55 (O9 b). Hand CCGP is 0.97 to 0.99 in N-PPC and J-PPC and 0.86 to 0.87 in J-MC.\n\n**Result: fig8e-finger-ccgp reproduced under O9 (b), not under O9 (a).** In N-PPC and J-MC no shuffle reached the finger-type CCGP (p < 0.001) under every reading. N-PPC finger CCGP (0.92 to 0.95) is at least 0.9 of its standard accuracy, but J-MC finger CCGP (0.74 to 0.79) is 0.77 to 0.83 of the within-hand accuracy (O8 a) and below 0.9 also against O8 (b); against the ratio of O9 (b), 0.55, both arrays pass. The criterion requires closeness under one reading, so the claim is reproduced; under the 0.9 margin of O9 (a) J-MC would not be close.\n\n**Result: jppc-finger-ccgp-low partially reproduced, resting on an assumption.** J-PPC finger-type CCGP is above chance (p < 0.001 under every reading) and far below the within-hand accuracy (ratio 0.33 to 0.44). With the linear SVM (O7 b) the CCGP is 0.35 to 0.37, within tolerance of 36%; with diagonal LDA it is 0.28 to 0.29, outside. The within-hand accuracy on the pseudo-population is 0.84 to 0.87, outside the tolerance of 65%, so under the adopted assumption no reading has both values within tolerance, and the claim is partial by its rule (p < 0.001 and CCGP below 0.9 of within-hand accuracy). In the per-session variant the within-hand accuracy is 0.69 (LDA) and 0.69 (SVM), within tolerance; with SVM CCGP it would be reproduced.\n\"\"\")\n\nmd(r\"\"\"\n## figs11-jppc-lower-matched-size\n\n> Even at matched neural population size, J-PPC finger-type CCGP is lower than that of N-PPC and J-MC.\n\nFinger-type CCGP for 100 random subsets of the pooled neurons at sizes 50 to 250 in steps of 50 (up to the smallest pooled population, J-MC, 252 neurons under O1 a), under the readings O6 x O7 of fig8e-finger-ccgp, with O1 (a).\n\"\"\")\n\ncode(r\"\"\"\nt = time.time()\nsizes = [50, 100, 150, 200, 250]\nndc_rows = []\nfor o6 in [\"a\", \"b\"]:\n    for o7 in [\"lda\", \"svm\"]:\n        for k, arr in enumerate(F.ARRAYS):\n            Xs, ys = zip(*[F.array_data(s, arr, \"a\") for s in sess_of(arr)])\n            rng = np.random.default_rng(2000 + k)\n            res = F.ndc_finger(list(Xs), list(ys), sizes, 100, o6, o7, rng)\n            for n, (m, sd) in res.items():\n                ndc_rows.append(dict(O6=o6, O7=o7, array=arr, size=n, mean=m, sd=sd))\nndc = pd.DataFrame(ndc_rows)\nprint(f\"{time.time() - t:.0f} s\")\nwide = ndc.pivot_table(index=[\"O6\", \"O7\", \"size\"], columns=\"array\", values=\"mean\")\nwide[\"JPPC_lowest\"] = (wide[\"J-PPC\"] < wide[\"N-PPC\"]) & (wide[\"J-PPC\"] < wide[\"J-MC\"])\nprint(wide.round(3).to_string())\nprint(\"J-PPC lowest at every size, per reading:\")\nprint(wide.groupby(level=[0, 1]).JPPC_lowest.all().to_string())\n\nfig, ax = plt.subplots(figsize=(5.5, 3.8))\nfor arr, col, ls in [(\"N-PPC\", BLUE, \"-\"), (\"J-MC\", ORANGE, \"-\"), (\"J-PPC\", \"gray\", \"-\")]:\n    q = ndc[(ndc.O6 == \"a\") & (ndc.O7 == \"lda\") & (ndc.array == arr)]\n    ax.errorbar(q[\"size\"], q[\"mean\"], yerr=q[\"sd\"], color=col, lw=2, marker=\"o\", label=arr)\nax.axhline(0.2, color=\"gray\", lw=1, ls=\":\"); ax.set_ylim(0, 1)\nax.set_xlabel(\"neurons\"); ax.set_ylabel(\"finger-type CCGP\"); ax.legend(frameon=False); ax.set_title(\"O6 a, O7 a (mean, SD of 100 subsets)\")\nplt.show()\n\"\"\", tags=[\"claim:figs11-jppc-lower-matched-size\"])\n\nmd(r\"\"\"\n**Result: reproduced.** At every size from 50 to 250 neurons, under every reading of O6 and O7, the mean J-PPC finger-type CCGP is below the means of N-PPC and J-MC (see the table above; chance 0.2).\n\"\"\")\n\nmd(r\"\"\"\n## Blocked claims\n\nfig4c-contra-discriminative, fig4e-plan-vs-move, fig5a-contra-decoding, fig5bcd-npcc-data-requirements and fig5e-planning-decoding use the alternating-cues task with a No-Go condition; fig6-online-bmi, figs6-single-array-retrospective and figs7-left-hand-bmi use the online BMI sessions. The check below lists every session's task and conditions: all 12 are the ten-finger task, with no No-Go condition and no decoder output.\n\"\"\")\n\ncode(r\"\"\"\nprint(summary[[\"file\", \"subject\", \"task\", \"trials\"]].to_string())\nprint(\"conditions present in any file:\", sorted(set().union(*[set(s.trials.finger) for s in S])))\nprint(\"trial table columns:\", list(S[0].trials.columns))\nprint(f\"notebook run time so far: {(time.time() - T0) / 60:.1f} min\")\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| tenfinger-recording-counts | reproduced (counts before the 0.5 Hz exclusion) |\n| tenfinger-pooled-npcc-neurons | reproduced (1114 before exclusion) |\n| tenfinger-discriminative-fraction | not reproduced (about 48%, 38%, 65% against 66%, 57%, 78%) |\n| tenfinger-decoding-accuracy | reproduced |\n| tenfinger-error-structure | reproduced |\n| fig8b-matching-closer | reproduced, resting on an assumption (noise scaling of rsatoolbox) |\n| fig8a-npcc-index-distinct | reproduced |\n| fig8e-hand-ccgp | reproduced |\n| fig8e-finger-ccgp | reproduced (under O9 b; J-MC below the 0.9 margin of O9 a) |\n| jppc-finger-ccgp-low | partially reproduced, resting on an assumption (standard accuracy on the pseudo-population) |\n| figs11-jppc-lower-matched-size | reproduced |\n| fig4c, fig4e, fig5a, fig5bcd, fig5e | blocked, data_missing |\n| fig6-online-bmi, figs6, figs7 | blocked, data_missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.\n\n**How the analysis differs from the paper's.** The paper links no code. The 0.5 Hz exclusion, fold assignment, noise covariance, partitions, pseudo-trial matching and decoder of the CCGP are run under each reading the claims file names. Two choices are assumptions: the per-partition noise precision passed to rsatoolbox is that of the partition mean (the toolbox's documented input), and the standard accuracy that bounds CCGP is computed on the same pseudo-population. The CCGP null shuffles condition labels across pseudo-trials, and for random matching (O6 b) draws a new matching for each shuffle.\n\n**What was found about the dataset.** It holds the ten-finger task only (10 sessions of N, 2 of J), not the alternating-cues or BMI sessions the paper also reports. The subject identifiers are `P1` for participant N and `N1` for participant J, so `N1` does not mean N. Most units store their spike times out of time order. Trial columns `Run`, `TrialNumber`, `cue_on_time`, `cue_off_time` and `go_on_time` have no description, and the Delay screen onset is only implied by `cue_off_time`. The per-session unit counts the paper reports match the units before the 0.5 Hz exclusion; J-MC has 139 units in its first session against the paper's maximum of 130.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/000252-guan-2022/reproduce_guan_2022.ipynb\")\nprint(\"written\", len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

I drafted the conclusions from the prototype numbers, and will correct them against the executed output. Now the development run:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python build_nb.py && cd entries/000252-guan-2022 && time jupyter nbconvert --to notebook --execute reproduce_guan_2022.ipynb --output-dir $TMPDIR/exec --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
written 37 cells
[NbConvertApp] Making directory /tmp/claude-1001/exec
[NbConvertApp] Converting notebook reproduce_guan_2022.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 293444 bytes to /tmp/claude-1001/exec/reproduce_guan_2022.ipynb

real	6m49.468s
user	6m37.508s
sys	0m0.602s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('exec/reproduce_guan_2022.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='stream': print(f'--- cell {i}'); print(o.text[:9000])
        elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
EOF
date -u
```

```
<persisted-output>
Output too large (35.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5b0cb1dd-20d1-4c47-97b4-d6b907f306a5/tool-results/bcjrc4a9b.txt

Preview (first 2KB):
--- cell 1
dandiset 000252 version 0.230408.2207

--- cell 3
title: Finger_RL: human intracortical recordings during attempted finger movements of right and left hands
related: [('dcite:IsDescribedBy', 'https://doi.org/10.1101/2022.12.07.22283227 '), ('dcite:Continues', 'DANDI:000147')]

--- cell 3
assets in version: 12 | in draft: 12 | same asset ids: True

--- cell 3
loaded 12 files in 11 s
                                 file subject sex        date                               task  trials  runs per_condition  units_PPC  units_MC             electrodes  unsorted_units  spikes_outside_obs
0   sub-N1_ses-2019-02-12_ecephys.nwb      N1   M  2019-02-12  ten-finger press task, with delay     100     2         10-10        159       139  {'PPC': 96, 'MC': 95}             283                   0
1   sub-N1_ses-2019-12-20_ecephys.nwb      N1   M  2019-12-20  ten-finger press task, with delay     100     2         10-10        160       120  {'MC': 96, 'PPC': 96}             224                   0
2   sub-P1_ses-2015-08-12_ecephys.nwb      P1   F  2015-08-12  ten-finger press task, with delay     100     2         10-10        112         0            {'PPC': 96}             101                   0
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/5b0cb1dd-20d1-4c47-97b4-d6b907f306a5/tool-results/bcjrc4a9b.txt",
 "offset": 20
}
```

```
20	6   sub-P1_ses-2016-04-27_ecephys.nwb      P1   F  2016-04-27  ten-finger press task, with delay     100     2         10-10        116         0            {'PPC': 96}             108                   0
21	7   sub-P1_ses-2016-05-04_ecephys.nwb      P1   F  2016-05-04  ten-finger press task, with delay     100     2         10-10        110         0            {'PPC': 96}             108                   0
22	8   sub-P1_ses-2016-05-11_ecephys.nwb      P1   F  2016-05-11  ten-finger press task, with delay     100     2         10-10        118         0            {'PPC': 96}             113                   0
23	9   sub-P1_ses-2016-05-16_ecephys.nwb      P1   F  2016-05-16  ten-finger press task, with delay     100     2         10-10        109         0            {'PPC': 96}              96                   0
24	10  sub-P1_ses-2016-05-20_ecephys.nwb      P1   F  2016-05-20  ten-finger press task, with delay     100     2         10-10        105         0            {'PPC': 96}              97                   0
25	11  sub-P1_ses-2016-05-23_ecephys.nwb      P1   F  2016-05-23  ten-finger press task, with delay     100     2         10-10        113         0            {'PPC': 96}             100                   0
26	N1 M ['left motor cortex (MC), near hand knob', 'left posterior parietal cortex (PPC), superior parietal lobule (SPL)']
27	P1 F ['left posterior parietal cortex (PPC), junction of postcentral and intraparietal sulci (PC-IP)']
28	
29	--- cell 4
30	conditions: ['Li', 'Lm', 'Lp', 'Lr', 'Lt', 'Ri', 'Rm', 'Rp', 'Rr', 'Rt'] | hand: ['L', 'R'] | finger_type: ['i', 'm', 'p', 'r', 't']
31	finger == hand + finger_type in every trial: True
32	phase durations, s (median unless stated):
33	                                 file   iti   cue  delay_min  delay_max    go  go_min  ordered
34	0   sub-N1_ses-2019-02-12_ecephys.nwb  1.57  1.07       1.06       1.58  1.07    1.07     True
35	1   sub-N1_ses-2019-12-20_ecephys.nwb  2.09  1.61       0.86       1.14
[... 336 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
def rep(a,b):
    global s
    assert a in s, a[:60]; s=s.replace(a,b)
rep("""**Result: not reproduced.** Under every reading of O1 the Go-window percentages of discriminative neurons are 40 to 49% for N-PPC, 38% for J-PPC and 64 to 66% for J-MC, against 66%, 57% and 78%; all three are below the lower tolerance bounds (59.4%, 51.3% and 70.2%). Without FDR correction the percentages are still lower than the paper's (at most 55%, 46% and 69%), and no other analysis window gives more.""",
"""**Result: not reproduced.** Before the exclusion and under both readings of O1, the Go-window percentages of discriminative neurons are 40.4 to 48.9% for N-PPC, 37.6 to 38.1% for J-PPC and 63.7 to 65.6% for J-MC, against 66%, 57% and 78%; all three are below the lower tolerance bounds (59.4%, 51.3% and 70.2%). Without FDR correction they are still below the paper's values (at most 56.1%, 46.5% and 68.8%), FDR per session gives no more, and no other analysis window gives more than the Go window.""")
rep("""Under every reading of O1 and O2 the pooled accuracies are 71 to 73% for N-PPC (1000 trials), 68 to 70% for J-PPC and 78 to 79% for J-MC (200 trials each), within the tolerances of 70%, 66% and 75%, against a chance of 10%. The single seeds of O2 (b) stay within tolerance as well.""",
"""Under every reading of O1 and O2 the pooled accuracies are 71.4 to 73.0% for N-PPC (1000 trials), 68.0 to 70.0% for J-PPC and 78.0 to 78.5% for J-MC (200 trials each), within the tolerances of 70%, 66% and 75%, against a chance of 10%. The single seeds of O2 (b) range from 69.9 to 73.6%, 66.0 to 72.5% and 76.5 to 80.0%, all within tolerance.""")
rep("""Of the errors, 74 to 77% (N-PPC), 66 to 72% (J-PPC) and 63 to 65% (J-MC) confuse""","""Of the errors, 73.9 to 76.6% (N-PPC), 66.2 to 72.1% (J-PPC) and 62.8 to 65.3% (J-MC) confuse""")
rep("""and all values are within tolerance except N-PPC under shrinkage toward identity (1.70 and 1.71 against an upper bound of 1.79, still in; see the table). Under""","""and all values are within tolerance (the largest N-PPC value, 1.71 under shrinkage toward identity, against an upper bound of 1.79). Under""")
rep("""(for example, O4 (a) with diagonal shrinkage: right hand 2.16 and 2.96 against 0.62, left hand 1.30 and 2.23 against 0.57). The session counts in the table say how often the pattern holds in single sessions.""","""(for example, O1 (a), O4 (a) with diagonal shrinkage: right hand 2.16 and 2.96 against 0.62, left hand 1.30 and 2.23 against 0.57). In single sessions the pattern holds in both hands in 7 to 10 of the 10 sessions, depending on the reading.""")
rep("""(O9 a; the smallest ratio is printed above), so it is also above 0.55 (O9 b). Hand CCGP is 0.97 to 0.99 in N-PPC and J-PPC and 0.86 to 0.87 in J-MC.""","""(O9 a; the smallest ratio is 0.913), so it is also above 0.55 (O9 b). Hand CCGP is 0.970 to 0.990 in N-PPC and J-PPC and 0.860 to 0.870 in J-MC, against shuffle means of about 0.50.""")
rep("""N-PPC finger CCGP (0.92 to 0.95) is at least 0.9 of its standard accuracy, but J-MC finger CCGP (0.74 to 0.79) is 0.77 to 0.83 of the within-hand accuracy (O8 a) and below 0.9 also against O8 (b);""","""N-PPC finger CCGP (0.918 to 0.954) is at least 0.9 of its standard accuracy, but J-MC finger CCGP (0.735 to 0.790) is 0.770 to 0.823 of the within-hand accuracy (O8 a) and 0.775 to 0.857 of the accuracy over both hands (O8 b), below 0.9 in both;""")
rep("""**Result: jppc-finger-ccgp-low partially reproduced, resting on an assumption.** J-PPC finger-type CCGP is above chance (p < 0.001 under every reading) and far below the within-hand accuracy (ratio 0.33 to 0.44). With the linear SVM (O7 b) the CCGP is 0.35 to 0.37, within tolerance of 36%; with diagonal LDA it is 0.28 to 0.29, outside. The within-hand accuracy on the pseudo-population is 0.84 to 0.87, outside the tolerance of 65%, so under the adopted assumption no reading has both values within tolerance, and the claim is partial by its rule (p < 0.001 and CCGP below 0.9 of within-hand accuracy). In the per-session variant the within-hand accuracy is 0.69 (LDA) and 0.69 (SVM), within tolerance; with SVM CCGP it would be reproduced.""",
"""**Result: jppc-finger-ccgp-low partially reproduced, resting on an assumption.** J-PPC finger-type CCGP is 0.290 to 0.380 against a shuffle mean of 0.20, and far below the within-hand accuracy on the pseudo-population (0.828 to 0.890; ratio 0.333 to 0.447). The permutation p is below 0.001 in only one of the eight readings (O1 b, O6 a, linear SVM: p = 1/1002, CCGP 0.380); in the others it is 0.002 to 0.038, so the paper's p < 0.001 holds only in part. In that reading the CCGP is within tolerance of 36% but the within-hand accuracy (0.850) is outside the tolerance of 65%, so by the claim's rule (p < 0.001 and CCGP below 0.9 of the within-hand accuracy, a value out of tolerance) it is partially reproduced. In the per-session variant of standard accuracy the J-PPC within-hand accuracy is 0.690 (LDA) and 0.685 (SVM), within tolerance; with it the same reading would be reproduced, so the outcome rests on which population the standard accuracy is computed on.""")
rep("""| jppc-finger-ccgp-low | partially reproduced, resting on an assumption (standard accuracy on the pseudo-population) |""","""| jppc-finger-ccgp-low | partially reproduced, resting on an assumption (standard accuracy on the pseudo-population; p < 0.001 in one reading of eight) |""")
rep("""| tenfinger-discriminative-fraction | not reproduced (about 48%, 38%, 65% against 66%, 57%, 78%) |""","""| tenfinger-discriminative-fraction | not reproduced (at most 48.9%, 38.1%, 65.6% against 66%, 57%, 78%) |""")
open(p,'w').write(s)
EOF
date -u
```

```
Wed Nov  4 12:19:56 UTC 2026
Shell cwd was reset to
```

**Agent**

Now the entry files. First I check the schemas and the example attempt's full format.

**Agent calls Bash**

```bash
ls schemas; sed -n 60,400p attempts/001453-fouke-2025-01.yaml | grep -v "^    [a-z]" | head -150; cat entries/001453-fouke-2025/README.md | head -40
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1d-dc-faster-all-codes
  notes: Over all 21 codes, the median over fish and code values is 94.0 pixels/s for DC and 55.2
    With positions resampled to 30 Hz, 95.2 against 53.8 (p = 1.3e-08). DC are faster within
  deviations:
  - Tested over all stimulus codes without their names; the paper's figure uses nine whole-field
  - The comparison assumes one spatial scale for all rigs, which the files do not state.
- claim: fig1d-median-velocity
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1d-median-velocity
  measured:
  - 9.87
  - 6.41
  notes: All four readings put both values within tolerance; (a) median of stimulus medians DC
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])"; sed -n 1,30p attempts/001453-fouke-2025-01.yaml | tail -5; grep -n "assumed\|questions:\|verifications" attempts/*.yaml | head -5
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
[... 268 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));p=s['properties']
for k in ['findings','inputs']: print(k, json.dumps(p.get(k),indent=0)[:1800])
print(list(p))"
```

```
findings {
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
"metadata_insufficient",
"selection_undocumented",
"methods_unavailable",
"format_error",
[... 42 more lines not kept]
```

**Agent**

Now the entry files, then lock and run.

**Agent calls Bash**

```bash
cd entries/000252-guan-2022 && cat > entry.yaml <<'EOF'
schema_version: 1
name: 000252-guan-2022
type: reproduction
title: Ten-finger decoding and compositional finger coding in human PPC and MC (Guan et al. 2022)
description: Tests the ten-finger findings of Guan et al. (preprint 2022) on dandiset 000252, which
  holds sorted single-unit spikes from 10 sessions of participant N (PPC) and 2 sessions of
  participant J (PPC and MC) during the ten-finger press task. It counts the neurons, tests
  single-neuron selectivity, ten-finger decoding and its errors, the cross-validated distances
  between matching and non-matching fingers of the two hands, and the cross-condition
  generalization of hand and finger-type decoders. The alternating-cues and BMI sessions of the
  paper's Figures 4 to 6 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_guan_2022.ipynb
  title: Reproducing Guan et al. (2022) from dandiset 000252
  runtime_minutes: 7
helpers:
- fingers.py
related:
- id: dandi:000252/0.230408.2207
  relation: uses_data
- id: doi:10.1101/2022.12.07.22283227
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
remfile
requests
rsatoolbox
scikit-learn
scipy
EOF
cd $TMPDIR && . dev/bin/activate && python build_nb.py && cd  && python tools/entry.py lock entries/000252-guan-2022 2>&1 | tail -3
```

```
written 37 cells
wrote entries/000252-guan-2022/requirements.lock.txt
```

**Agent**

No claim looks misread, so I have no questions for a reader. Next: README and the attempt record, then `all`.

**Agent calls Write**

```json
{
 "file_path": "entries/000252-guan-2022/README.md",
 "content": "# Guan et al. (preprint 2022) from dandiset 000252\n\nTests the findings of [Guan et al. (2022)](https://doi.org/10.1101/2022.12.07.22283227) that can be\ntested on [DANDI:000252](https://dandiarchive.org/dandiset/000252/0.230408.2207). The dandiset holds\nthe ten-finger press task: 10 sessions of participant N (one PPC array) and 2 sessions of\nparticipant J (a PPC and an MC array), with sorted units and trial times. The alternating-cues\ntask and the BMI sessions of Figures 4 to 6 are not in it.\n\n| Claim | Outcome |\n|---|---|\n| Neurons per session and sessions in the ten-finger task | Reproduced (counts before the 0.5 Hz exclusion) |\n| 1111 N-PPC neurons pooled | Reproduced |\n| Most neurons discriminate the ten fingers (66%, 57%, 78%) | Not reproduced |\n| Ten-finger decoding accuracy (70%, 66%, 75%) | Reproduced |\n| Most errors are adjacent or matching fingers | Reproduced |\n| Matching fingers of the two hands are closer than non-matching ones | Reproduced, resting on an assumption |\n| N-PPC index finger distinct from middle and ring in both hands | Reproduced |\n| Hand decoders generalize across finger types | Reproduced |\n| Finger-type decoders generalize across hands (N-PPC, J-MC) | Reproduced |\n| J-PPC finger-type generalization is low (36% against 65%) | Partially reproduced, resting on an assumption |\n| J-PPC finger-type generalization lowest at matched population size | Reproduced |\n| Alternating-cues task, Figures 4 and 5 (five claims) | Blocked: data missing |\n| Online BMI, Figure 6 and Supplementary Figures 6 and 7 (three claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000252-guan-2022-01.yaml`](../../attempts/000252-guan-2022-01.yaml).\n\n- `reproduce_guan_2022.ipynb`: the analysis. It takes about seven minutes, most of it the\n  permutation tests of the cross-condition generalization.\n- `fingers.py`: streaming the files, firing rates in the paper's analysis windows, the 0.5 Hz\n  exclusion, diagonal LDA, single-neuron ANOVA with FDR, cross-validated Mahalanobis distances\n  (rsatoolbox) and cross-condition generalization. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/000252-guan-2022/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000252-guan-2022-01.yaml",
 "content": "schema_version: 2\nid: 000252-guan-2022-01\ndataset:\n  archive: dandi\n  id: \"000252\"\n  version: 0.230408.2207\n  doi: 10.48324/dandi.000252/0.230408.2207\npaper: doi:10.1101/2022.12.07.22283227\ndate: 2026-11-04\nentry: 000252-guan-2022\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/41825254986\noutcomes:\n- claim: tenfinger-recording-counts\n  outcome: reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:tenfinger-recording-counts\n  measured:\n  - 10\n  - 2\n  - 100\n  - 111.4\n  - 159.5\n  - 129.5\n  notes: The dandiset has 10 sessions of participant N and 2 of J, each of 100 trials (10 per\n    condition). Before the 0.5 Hz exclusion N-PPC has 111.4 units per session (102 to 119), J-PPC\n    159.5 (159 to 160) and J-MC 129.5 (120 to 139); the J-MC maximum of 139 is above the paper's\n    130 but inside the 10% widening of that bound (143). After the exclusion the means are 94.3\n    and 93.0 for N-PPC under O1 (a) and (b), outside tolerance, and 157.5 or 156.0 for J-PPC and\n    126.0 or 125.0 for J-MC. The paper's counts are those before the exclusion.\n  deviations:\n  - The counts that match are those before the 0.5 Hz exclusion, which the Methods (Feature\n    Extraction) say applies to all analyses; the criterion names this count among its readings.\n- claim: tenfinger-pooled-npcc-neurons\n  outcome: reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:tenfinger-pooled-npcc-neurons\n  measured: 1114\n  notes: 1114 N-PPC units over the 10 sessions before the exclusion (paper 1111), 943 under O1 (a)\n    and 930 under O1 (b), both outside tolerance.\n  deviations:\n  - As for tenfinger-recording-counts, the matching count is the one before the exclusion.\n- claim: tenfinger-discriminative-fraction\n  outcome: not_reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:tenfinger-discriminative-fraction\n  measured:\n  - 47.8\n  - 38.1\n  - 65.1\n  notes: One-way ANOVA of Go-window rates across the ten conditions, Benjamini-Hochberg over the\n    neurons of each array pooled over sessions. Under O1 (a) 47.8% of 943 N-PPC, 38.1% of 315 J-PPC\n    and 65.1% of 252 J-MC neurons have q below 0.05; under O1 (b) 48.9%, 38.1% and 65.6%; before\n    the exclusion 40.4%, 37.6% and 63.7%. All are below the lower tolerance bounds (59.4%, 51.3%,\n    70.2%). As variants, uncorrected p below 0.05 gives at most 56.1%, 46.5% and 68.8%, FDR per\n    session gives no more, and the Delay, Cue and ITI windows give fewer (0 to 49%). Ten-finger\n    decoding on the same rates matches the paper, so the gap is in the single-neuron test, not in\n    the data's information.\n  deviations:\n  - The Go window is used, as claims-file O11 says the text supports no other.\n  - Units with the same rate in every trial (5 N-PPC and 2 J-MC before the exclusion, none after it)\n    have no ANOVA p; they are counted in the FDR's m and as not discriminative.\n- claim: tenfinger-decoding-accuracy\n  outcome: reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:tenfinger-decoding-accuracy\n  measured:\n  - 72.2\n  - 69.5\n  - 78.5\n  notes: Diagonal LDA per session, stratified 8-fold, predictions pooled over sessions. Under O1 (a)\n    and O2 (a), 72.2% (N-PPC, 1000 trials), 69.5% (J-PPC, 200) and 78.5% (J-MC, 200); over all\n    readings of O1 (including no exclusion) and O2 the values are 71.4 to 73.0%, 68.0 to 70.0% and\n    78.0 to 78.5%, and single seeds of O2 (b) 69.9 to 73.6%, 66.0 to 72.5% and 76.5 to 80.0%, all\n    within tolerance. Chance is 10%; with shuffled labels per-session accuracies are 0.07 to 0.17.\n  deviations:\n  - The variance floor of the diagonal LDA (1e-9 of the largest variance, as scikit-learn's\n    GaussianNB) is a standard choice that only prevents division by zero.\n- claim: tenfinger-error-structure\n  outcome: reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:tenfinger-error-structure\n  measured:\n  - 76.6\n  - 72.1\n  - 62.8\n  notes: Under O1 (a) and O2 (a), 213 of 278 N-PPC errors (119 adjacent, 94 matching), 44 of 61 J-PPC\n    errors and 27 of 43 J-MC errors are adjacent or matching; over all readings the shares are 73.9\n    to 76.6%, 66.2 to 72.1% and 62.8 to 65.3%, within tolerance of 76%, 66% and 68%.\n- claim: fig8b-matching-closer\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:fig8b-matching-closer\n  measured:\n  - 1.42\n  - 3.06\n  - 0.22\n  notes: Under O4 (a), with each partition's precision scaled to that of the partition mean, the\n    non-matching minus matching difference is 1.42 (BCa 95% CI 1.19 to 1.64) in N-PPC, 3.06 (1.73\n    to 4.13) in J-MC and 0.22 (-0.10 to 0.67) in J-PPC for O1 (a) and O3 (a); over O1 and O3 the\n    values are 1.42 to 1.71, 2.99 to 3.38 and 0.19 to 0.22, all within tolerance, with N-PPC and J-MC\n    CIs above 0 and the J-PPC CI including 0 (also by the percentile CI, in all 18 readings). Under\n    O4 (b), and the unscaled variant O4 (a1), the sign pattern is the same but the values are about\n    a fifth as large (N-PPC 0.28 to 0.36, J-MC 0.51 to 0.68), outside tolerance, which would be\n    partially reproduced. One N-PPC unit with zero residual variance in a partition is dropped.\n  deviations:\n  - Assumed that the per-partition noise passed to rsatoolbox is the precision of the partition\n    mean, the single-trial precision times the 5 trials per condition in each partition. The\n    Methods say the toolbox (ref 57) incorporates the noise covariances of both folds, which is its\n    list-of-noises branch, and the toolbox's calc_rdm_crossnobis documents that this list must hold\n    the precision of the mean of each fold. The paper does not say how it computed the noise, and\n    the scaling changes the values about fivefold; the unscaled result is shown.\n  - Units with zero residual variance in a partition make the noise covariance singular and are\n    left out of that session's distance (one N-PPC unit); a standard choice.\n- claim: fig8a-npcc-index-distinct\n  outcome: reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:fig8a-npcc-index-distinct\n  notes: In the N-PPC distances averaged over 10 sessions, under every reading of O1, O3 and O4, the\n    index-middle and index-ring distances exceed the middle-ring distance in both hands (O1 a, O3 a,\n    O4 a, right 2.16 and 2.96 against 0.62, left 1.30 and 2.23 against 0.57). In single sessions the\n    pattern holds in both hands in 7 to 10 of 10 sessions. The outcome does not depend on the\n    noise scaling assumed for fig8b-matching-closer, as all readings agree.\n  deviations:\n  - The MDS of the figure is drawn by classical MDS of the clipped squared distances and aligned by\n    Generalized Procrustes with scaling; it is shown only and does not decide the outcome.\n- claim: fig8e-hand-ccgp\n  outcome: reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:fig8e-hand-ccgp\n  notes: In N-PPC (943 neurons under O1 a), J-PPC (315) and J-MC (252), under every reading of O1, O6\n    and O7, no one of 1001 shuffles reaches the hand CCGP (p = 1/1002). Hand CCGP is 0.970 to 0.990\n    in N-PPC and J-PPC and 0.860 to 0.870 in J-MC, against shuffle means near 0.50, and at least\n    0.913 of the hand accuracy on the same pseudo-population, so close by both O9 (a) and (b).\n  deviations:\n  - The shuffle permutes the ten condition labels across pseudo-trials and recomputes CCGP; the\n    paper says only that labels were shuffled 1001 times. For O6 (b) each shuffle uses a new random\n    matching of trials.\n  - Standard accuracy is computed on the same pseudo-population (assumption, see\n    jppc-finger-ccgp-low); the per-session variant does not change this outcome, as hand CCGP is\n    above 0.9 of either.\n- claim: fig8e-finger-ccgp\n  outcome: reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:fig8e-finger-ccgp\n  notes: In N-PPC and J-MC, under every reading, no shuffle reaches the finger-type CCGP (p =\n    1/1002). N-PPC CCGP is 0.918 to 0.954, at least 0.925 of its standard accuracy. J-MC CCGP is\n    0.735 to 0.790, 0.770 to 0.823 of the within-hand accuracy (O8 a) and 0.775 to 0.857 of the\n    accuracy over both hands (O8 b). Closeness holds for both arrays under O9 (b), a ratio above\n    0.55, and fails for J-MC under the 0.9 margin of O9 (a). The criterion asks for one reading, so\n    the claim is reproduced; under O9 (a) it would be partially reproduced.\n  deviations:\n  - As for fig8e-hand-ccgp, the shuffle scheme and the population of the standard accuracy are\n    choices the paper does not state.\n- claim: jppc-finger-ccgp-low\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:jppc-finger-ccgp-low\n  measured:\n  - 38.0\n  - 85.0\n  notes: J-PPC finger-type CCGP is 0.290 to 0.380 over the readings (shuffle mean 0.20), far below\n    the within-hand accuracy on the pseudo-population (0.828 to 0.890). The permutation p is below\n    0.001 in one of eight readings (O1 b, O6 a, linear SVM, p = 1/1002, CCGP 0.380, within-hand\n    0.850) and 0.002 to 0.038 in the others, so the paper's p below 0.001 holds only in that\n    reading. There the CCGP is within tolerance of 36% and the within-hand accuracy is outside the\n    tolerance of 65%, with CCGP below 0.9 of it, which the criterion calls partially reproduced. In\n    the per-session variant of standard accuracy J-PPC within-hand accuracy is 0.690 (LDA) and\n    0.685 (SVM), within tolerance, and the same reading would be reproduced.\n  deviations:\n  - Assumed that the standard (within-hand) accuracy is computed on the same pseudo-population as\n    CCGP, since the Methods (Compositionality of finger representations) call it an upper bound on\n    CCGP, which holds only for the same neurons. The Methods' offline classification trains a\n    separate classifier per session, and that reading, shown as a variant, gives values near the\n    paper's 65% and would change the outcome to reproduced.\n  - The shuffle scheme of the permutation test is not stated; condition labels are permuted across\n    pseudo-trials. The J-PPC p-values lie near the 0.001 bound, so the scheme can matter.\n- claim: figs11-jppc-lower-matched-size\n  outcome: reproduced\n  notebook: reproduce_guan_2022.ipynb\n  output: claim:figs11-jppc-lower-matched-size\n  notes: With 100 random subsets per size, at 50, 100, 150, 200 and 250 neurons and under every\n    reading of O6 and O7 (O1 a), the mean J-PPC finger-type CCGP (0.254 to 0.325) is below the\n    means of N-PPC (0.472 to 0.854) and J-MC (0.559 to 0.788) at the same size.\n  deviations:\n  - Run under O1 (a) only, as the pooled J-MC population (252) sets the largest size; O1 (b) changes\n    the populations by at most 13 neurons.\n- claim: fig4c-contra-discriminative\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the alternating-cues task with No-Go (N 4 sessions, J 3). All 12 files of the\n    dandiset are the ten-finger task, with conditions Rt to Lp and no No-Go; the dandiset's\n    metadata and the paper's Data Availability name no other source.\n- claim: fig4e-plan-vs-move\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Alternating-cues task not in the dandiset (see fig4c-contra-discriminative).\n- claim: fig5a-contra-decoding\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Alternating-cues task not in the dandiset (see fig4c-contra-discriminative).\n- claim: fig5bcd-npcc-data-requirements\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Alternating-cues task not in the dandiset (see fig4c-contra-discriminative).\n- claim: fig5e-planning-decoding\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Alternating-cues task not in the dandiset (see fig4c-contra-discriminative).\n- claim: fig6-online-bmi\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the online BMI sessions with the decoded class of each trial. The dandiset has none.\n    Its metadata says it continues DANDI:000147, which by its description holds participant N's\n    BMI reaction-time sessions of ref 46 (10 files, with in-session classified finger); the claims\n    file does not name it as a source of this paper's data and it holds nothing of participant J,\n    so it was not used. J's BMI sessions are not public anywhere the paper names.\n- claim: figs6-single-array-retrospective\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs J's BMI run-blocks with threshold crossings or sorted units; not in the dandiset nor\n    in DANDI:000147, which holds participant N only.\n- claim: figs7-left-hand-bmi\n  outcome: blocked\n  blocked_by: data_missing\n  notes: J's left-hand BMI sessions are not in the dandiset (see fig6-online-bmi).\nfindings:\n- kind: data_missing\n  statement: The dandiset holds only the ten-finger press task (10 sessions of N, 2 of J). The\n    alternating-cues task (Figures 1, 4 and 5, Supplementary Figures 2 to 5) and the online BMI\n    sessions of J (Figure 6b, Supplementary Figures 6 and 7) are not in it, though the paper's Data\n    Availability names only this dandiset. N's BMI sessions of ref 46 appear to be in DANDI:000147.\n- kind: format_error\n  statement: In 1509 of 1692 units the spike times are not stored in increasing time order, which\n    NWB expects. Counts in windows are unaffected once sorted, as this attempt does.\n- kind: metadata_insufficient\n  statement: The files name the participants P1 (the paper's N) and N1 (the paper's J); no mapping\n    to the paper's labels is given, and N1 is not participant N. The mapping follows from the sex\n    and electrode locations.\n- kind: metadata_insufficient\n  statement: The trial columns Run, TrialNumber, cue_on_time, cue_off_time and go_on_time have no\n    description. The Delay screen onset, which defines the paper's Delay window, is implied only by\n    cue_off_time.\n- kind: other\n  statement: The per-session unit counts the paper reports match the units in the files before\n    the 0.5 Hz exclusion that the Methods apply to all analyses; the J-MC session of 2019-02-12 has\n    139 units against the paper's stated maximum of 130.\n- kind: methods_unavailable\n  statement: For the authors. How was the noise precision passed to rsatoolbox for the\n    cross-validated Mahalanobis distance (Methods, Neural distance between fingers)? With two\n    partitions and each partition's single-trial precision the differences are about a fifth of the\n    paper's (N-PPC 0.28 against 1.56); with the precision of the partition mean, as the toolbox\n    documents for a list of noises, they match (1.42). This attempt assumed the latter.\n- kind: methods_unavailable\n  statement: For the authors. Was the standard (within-condition) accuracy compared with CCGP\n    computed on the pseudo-population or per session (Methods, Compositionality of finger\n    representations)? For J-PPC within-hand accuracy is 0.83 to 0.89 on the pseudo-population and\n    0.69 per session, against the paper's 65%. This attempt assumed the pseudo-population.\n- kind: methods_unavailable\n  statement: For the authors. What did the 1001 label shuffles of the CCGP permutation test permute,\n    and how were trials of different sessions matched in the pseudo-population? With condition\n    labels permuted across pseudo-trials, J-PPC finger-type CCGP has p from 0.001 to 0.038 over the\n    readings, against the paper's p below 0.001.\n- kind: methods_unavailable\n  statement: For the authors. With the Methods' one-way ANOVA on Go-window rates and FDR over pooled\n    neurons, 48%, 38% and 65% of N-PPC, J-PPC and J-MC neurons are discriminative in the ten-finger\n    task, against 66%, 57% and 78%. Which window, exclusion and correction gave the paper's values?\n"
}
```

```
File created successfully at: attempts/000252-guan-2022-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Check for colon-space inside plain scalars, then run the entry's check and full run:

**Agent calls Bash**

```bash
grep -nE "^\s+[^-#][^:]*: .*: |^    [a-zA-Z(].*: " attempts/000252-guan-2022-01.yaml | head; date -u; time python tools/entry.py all entries/000252-guan-2022 2>&1 | tail -15
```

```
14:    name: CatalystNeuro
16:    harness: Claude Code
17:    model: claude-opus-5-5
18:    protocol: pilot-13
20:    platform: GitHub Actions
21:    url: https://github.com/catalystneuro/encore/actions/runs/41825254986
Wed Nov  4 12:21:35 UTC 2026
Installed kernelspec registry-000252-guan-2022 in executed/000252-guan-2022/.venv/share/jupyter/kernels/registry-000252-guan-2022
0 error(s)
pass  reproduce_guan_2022.ipynb  (403 s)

real	6m49.610s
user	6m34.075s
sys	0m2.711s
```

**Agent**

Check passed and the run took 403 s. I'll compare the executed copy's outputs with the development run, since the locked environment could differ.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import nbformat
def txt(p):
    nb=nbformat.read(p,4); out=[]
    for c in nb.cells:
        if c.cell_type=='code':
            for o in c.outputs:
                if o.output_type=='stream': out.append(o.text)
                if o.output_type=='error': out.append('ERROR '+o.evalue)
    return '\n'.join(out).splitlines()
a=txt('exec/reproduce_guan_2022.ipynb'); b=txt('executed/000252-guan-2022/reproduce_guan_2022.ipynb')
import difflib
d=[l for l in difflib.unified_diff(a,b,lineterm='',n=0) if not l.startswith('@@')]
print(len(d)); print('\n'.join(d[:60]))
EOF
```

```
8
--- 
+++ 
-loaded 12 files in 11 s
+loaded 12 files in 10 s
-365 s
+357 s
-notebook run time so far: 6.8 min
+notebook run time so far: 6.6 min
Shell cwd was reset to
```

**Agent**

The numbers are identical between the two runs, and I checked each conclusion sentence against them. Now the handover:

**Agent calls Bash**

```bash
python tools/entry.py check entries/000252-guan-2022 2>&1 | tail -2; python tools/entry.py handover entries/000252-guan-2022 2>&1 | tail -5; ls executed/000252-guan-2022/handover; git status --short; date -u
```

```
0 error(s)
wrote executed/000252-guan-2022/handover
10.1101-2022.12.07.22283227.yaml
fingers.py
reproduce_guan_2022.ipynb
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
?? attempts/000252-guan-2022-01.yaml
?? entries/000252-guan-2022/
?? scripts
Wed Nov  4 12:28:50 UTC 2026
```

**Agent**

I finished steps 1 to 5 for DANDI:000252 against the claims file, and the handover package is built. `python tools/entry.py all` passed with 0 errors, and the executed outputs were identical to my development run. Of the 19 claims, 9 were reproduced, 1 partially reproduced, 1 not reproduced and 8 blocked; two outcomes rest on assumptions. The work is not verified yet, since the verifier comes next, and nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| tenfinger-recording-counts | reproduced (the paper's counts are those before the 0.5 Hz exclusion) |
| tenfinger-pooled-npcc-neurons | reproduced (1114 units, paper 1111) |
| tenfinger-discriminative-fraction | not reproduced (at most 48.9 / 38.1 / 65.6% against 66 / 57 / 78%) |
| tenfinger-decoding-accuracy | reproduced (72 / 70 / 79% against 70 / 66 / 75%) |
| tenfinger-error-structure | reproduced |
| fig8b-matching-closer | reproduced, resting on an assumption |
| fig8a-npcc-index-distinct | reproduced |
| fig8e-hand-ccgp | reproduced |
| fig8e-finger-ccgp | reproduced under O9 (b); J-MC misses the 0.9 margin of O9 (a) |
| jppc-finger-ccgp-low | partially reproduced, resting on an assumption; p < 0.001 in only 1 of 8 readings |
| figs11-jppc-lower-matched-size | reproduced |
| fig4c, fig4e, fig5a, fig5bcd, fig5e | blocked, data_missing (alternating-cues task not in the dataset) |
| fig6-online-bmi, figs6, figs7 | blocked, data_missing (BMI sessions not in the dataset) |

## 2. Dataset, assumptions, questions

**What the dataset holds.**
- Only the ten-finger task: 10 sessions of participant N and 2 of J, 100 trials each.
- There are no duplicate recordings, and the spikes share a clock with the trial table in all 12 sessions.
- I pinned version 0.230408.2207, the only published version. The draft lists the same assets.

**Findings recorded.**
- **Spike times out of order:** 1509 of 1692 units store their spike times out of time order (format_error).
- **Subject labels:** the files call participant N `P1` and participant J `N1`, with no mapping to the paper's labels.
- **Undescribed trial columns:** five trial columns have no description, and the Delay onset is only implied by `cue_off_time`.
- **Unit counts:** the paper's per-session counts match the units before the 0.5 Hz exclusion. One J-MC session has 139 units against the paper's stated maximum of 130.
- **Related dandiset:** DANDI:000147 seems to hold N's BMI sessions from the paper's ref 46. The claims file doesn't name it as a source, so I didn't use it.

**Assumptions.**
- **fig8b:** the noise precision passed to rsatoolbox is that of each partition's mean, as the toolbox's documentation requires for its list-of-noises input. Without that scaling the differences are about one fifth of the paper's.
- **jppc-finger-ccgp-low:** the standard accuracy that CCGP is compared with is computed on the same pseudo-population, because the Methods call it "an upper bound on CCGP". If it is computed per session instead, J-PPC within-hand accuracy is 69%, inside the paper's 65% tolerance.

**Questions for the paper's authors** (recorded as methods_unavailable findings): how the noise precision was passed to rsatoolbox; which population the standard accuracy uses; what the 1001 label shuffles permuted and how pseudo-trials were matched; and which method gave the selectivity fractions.

**Questions to a reader:** none. I found no misreading in the claims file.

## 3. Protocol issues

1. The claims-file readings O3 and O4 did not cover how the toolbox is called, which changes values about fivefold. I added a reading from the toolbox's documentation, adopted it as an assumption, and showed the unscaled result as a variant.
2. Several criteria count a claim as reproduced "under one reading". That made fig8e-finger reproduced through O9 (b) even though O9 (a) fails, and made jppc partial through a single reading out of eight. I applied the criteria as written and gave every reading's result in the notes.
3. Step 1.4 does not say whether the author should look at a related dandiset the claims file doesn't name, such as 000147, when deciding between data_missing and `elsewhere`. I read only its metadata, did not use it, and kept the claims as data_missing with a note.
4. The protocol has no rule for a pseudo-population null over random pairings. Where trials were matched at random (O6 b), I drew a new matching for each shuffle and recorded this as a deviation.

## 4. Runtime and failures

- The notebook runs in about 6.8 minutes. The whole session took from 12:02 to 12:29 UTC.
- Two errors came up during development and are fixed: a singular noise matrix from units with zero variance (one unit is now dropped and reported), and an early sortedness check that read the wrong array.
- Dotfiles (`.bashrc`, `.idea` and others) and a `scripts` folder are untracked in the repository root. I don't think I created them (`scripts` was already there when I first listed the root) and left them alone.

Files are in `entries/000252-guan-2022/`:
- `reproduce_guan_2022.ipynb`
- `fingers.py`
- `README.md`
- `entry.yaml`

The record is `attempts/000252-guan-2022-01.yaml`, and the handover package is in `executed/000252-guan-2022/handover/`.

## End of run

48 turns, 27 minutes, $4.22 at API prices, result: success.
