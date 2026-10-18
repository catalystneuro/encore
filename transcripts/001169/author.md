# 001169 · author · run 39139945045

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts tools
```

```
# Protocol for an attempt

Version: `pilot-7`. Record this version in the attempt's provenance.

This is what an agent, or a person, does to attempt a target and deposit the
result. It is written from the eight pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

There are two roles. The **author** makes the attempt. The **verifier** checks
it and must not be the author: for agents, a separate run with a separate
context that has not seen the author's reasoning.

Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
`verifier-2`, `author-revise-2`, and, when the last of these proposes changes
of outcome, `verifier-3` and `author-revise-3`. Each run's transcript and final report are
kept in [`transcripts/<dandiset>/`](../transcripts).

## Author

[... 509 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -400
```

```
# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
with the methods available to it. **A "not reproduced" or "partially
reproduced" outcome is not a finding that the paper is wrong.** It can come
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
ls -R entries/001453-fouke-2025 claims/001453; cat attempts/001453-fouke-2025-01.yaml; cat claims/001453/*.yaml; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in
```

```
<persisted-output>
Output too large (48KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/28bd715c-d49f-4326-a417-29a357f11328/tool-results/b4ntov54q.txt

Preview (first 2KB):
claims/001453:
10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
schema_version: 1
id: 001453-fouke-2025-01
dandiset: "001453"
dandiset_version: 0.250518.1950
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/28bd715c-d49f-4326-a417-29a357f11328/tool-results/b4ntov54q.txt"
}
```

```
1	claims/001453:
2	10.1016-j.cub.2025.04.027.yaml
3	
4	entries/001453-fouke-2025:
5	README.md
6	entry.yaml
7	omr.py
8	reproduce_fouke_2025.ipynb
9	requirements.in
10	requirements.lock.txt
11	schema_version: 1
12	id: 001453-fouke-2025-01
13	dandiset: "001453"
14	dandiset_version: 0.250518.1950
15	paper: doi:10.1016/j.cub.2025.04.027
16	date: 2026-10-14
17	entry: 001453-fouke-2025
18	provenance:
19	  kind: agent
20	  accountable:
[... 843 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat README.md; python -c "
import nbformat
nb=nbformat.read('reproduce_fouke_2025.ipynb',4)
for i,c in enumerate(nb.cells[:8]):
    print('---',i,c.cell_type,c.metadata.get('tags'))
    print(c.source[:2500])
print(len(nb.cells))
for i,c in enumerate(nb.cells): print(i,c.cell_type,c.metadata.get('tags'),c.source[:80].replace(chr(10),' '))
"; head -80 omr.py
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
[... 318 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/entry.py; ls schemas; grep -n "001169" -A12 targets/dandisets.json | head -40
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
- each notebook, or a helper it imports, names the dandiset the entry uses;
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 4134,4170p targets/dandisets.json; curl -s https://api.dandiarchive.org/api/dandisets/001169/ | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/001169/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL -o paper/paper.html "https://www.nature.com/articles/s41467-023-43250-x"; ls -la paper; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s41467-023-43250-x&format=json" | python -m json.tool | grep -E '"(pmcid|isOpenAccess|title)"'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10663503/fullTextXML" -o paper/fulltext.xml; ls -la paper; python - <<'EOF'
import re
x=open('paper/fulltext.xml').read()
# strip tags but keep paragraph breaks
x=re.sub(r'<(title)>',r'\n\n## ',x)
x=re.sub(r'</(p|title|caption)>','\n',x)
x=re.sub(r'<[^>]+>','',x)
import html
x=html.unescape(x)
open('paper/fulltext.txt','w').write(x)
print(len(x))
EOF
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "paper/fulltext.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/fulltext.txt",
 "offset": 250,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text is open access (PMC10663503). Now listing the dandiset.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import requests, json, collections
V="0.260825.1909"
url=f"https://api.dandiarchive.org/api/dandisets/001169/versions/{V}/assets/?page_size=1000"
rows=[]
while url:
    r=requests.get(url).json(); rows+= r['results']; url=r['next']
print(len(rows))
import pickle; pickle.dump(rows,open('/tmp/claude/assets.pkl','wb')) if False else None
json.dump(rows,open('paper/assets.json','w'))
subs=collections.Counter(a['path'].split('/')[0] for a in rows)
print(len(subs)); print(list(subs.items())[:10])
print([a['path'] for a in rows[:5]])
sz=[a['size'] for a in rows]; import numpy as np; print(np.percentile(sz,[0,50,100]))
print(collections.Counter(a['path'].rsplit('.',1)[-1] for a in rows))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which python; python --version; uv --version; ls ~/.cache 2>/dev/null; python -c "import yaml,nbformat,jsonschema; print('ok')"
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
Python 3.13.16
uv 0.13.1 (x86_64-unknown-linux-gnu)
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 scratch && VIRTUAL_ENV=$TMPDIR/scratch uv pip install -q dandi h5py remfile pynwb pandas scipy statsmodels matplotlib requests 2>&1 | tail -3; echo $TMPDIR
```

```
/tmp/claude-1001
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import requests, json, collections
V="0.260825.1909"
url=f"https://api.dandiarchive.org/api/dandisets/001169/versions/{V}/assets/?page_size=1000"
rows=[]
while url:
    r=requests.get(url).json(); rows+= r['results']; url=r['next']
print(len(rows))
json.dump(rows,open('paper/assets.json','w'))
subs=collections.Counter(a['path'].split('/')[0] for a in rows)
print(len(subs)); print(list(subs.items())[:10])
print([a['path'] for a in rows[:5]])
sz=[a['size'] for a in rows]; import numpy as np; print(np.percentile(sz,[0,50,100]))
print(collections.Counter(a['path'].rsplit('.',1)[-1] for a in rows))
print(collections.Counter('_'.join(x.split('-')[0] for x in a['path'].split('/')[-1].split('_')[1:]) for a in rows))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import json, collections, numpy as np
rows=json.load(open('paper/assets.json'))
proto=collections.Counter(a['path'].split('_ses-')[1].rsplit('-',2)[0] for a in rows)
print(proto)
per=collections.Counter(a['path'].split('/')[0] for a in rows)
v=np.array(list(per.values())); print(v.min(), np.median(v), v.max())
print(collections.Counter(a['path'].split('/')[0][4] for a in rows))
# subjects by prefix letters
print(collections.Counter(s[4] for s in per))
EOF
curl -s "https://api.dandiarchive.org/api/dandisets/001169/versions/0.260825.1909/" | python -m json.tool > paper/dandiset_meta.json; python -c "
import json; m=json.load(open('paper/dandiset_meta.json'))
for k in ['description','assetsSummary','relatedResource','wasGeneratedBy','contributor','keywords','citation']:
    print(k, json.dumps(m.get(k),indent=1)[:2500])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import time
from dandi.dandiapi import DandiAPIClient
import remfile, h5py, pynwb
t=time.time()
c=DandiAPIClient()
ds=c.get_dandiset("001169","0.260825.1909")
a=ds.get_asset_by_path('sub-C015/sub-C015_ses-RWTautowait-20191017-093757.nwb')
url=a.get_content_url(follow_redirects=1, strip_query=True)
print(url)
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
    else:
        print(name+'/', dict((k,v) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
f.visititems(show)
print(time.time()-t)
EOF
```

```
https://dandiarchive.s3.amazonaws.com/blobs/973/107/973107bd-cd62-4720-ad12-fcc37097ed29
acquisition/ {}
acquisition/task_recording/ {'neurodata_type': 'TaskRecording'}
acquisition/task_recording/actions/ {'colnames': array(['timestamp', 'action_type', 'value'], dtype=object), 'description': 'Contains the onset times of the task output actions (e.g. LED turned on/off).', 'neurodata_type': 'ActionsTable'}
acquisition/task_recording/actions/action_type (1739,) int64 {'description': 'The action type', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
acquisition/task_recording/actions/id (1739,) int64 {'neurodata_type': 'ElementIdentifiers'}
acquisition/task_recording/actions/timestamp (1739,) float64 {'description': 'The action time', 'neurodata_type': 'VectorData'}
acquisition/task_recording/actions/value (1739,) object {'description': 'The action value', 'neurodata_type': 'VectorData'}
acquisition/task_recording/events/ {'colnames': array(['timestamp', 'event_type', 'value'], dtype=object), 'description': 'Contains the onset times of events in the task.', 'neurodata_type': 'EventsTable'}
acquisition/task_recording/events/event_type (4745,) int64 {'description': 'The event type', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
acquisition/task_recording/events/id (4745,) int64 {'neurodata_type': 'ElementIdentifiers'}
acquisition/task_recording/events/timestamp (4745,) float64 {'description': 'The event timestamp', 'neurodata_type': 'VectorData'}
acquisition/task_recording/events/value (4745,) object {'description': 'The event value', 'neurodata_type': 'VectorData'}
acquisition/task_recording/states/ {'colnames': array(['start_time', 'stop_time', 'state_type'], dtype=object), 'description': 'Contains the start and end times of each state in the task.', 'neurodata_type': 'StatesTable'}
acquisition/task_recording/states/id (1192,) int64 {'neurodata_type': 'ElementIdentifiers'}
acquisition/task_recording/states/start_time
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd  curl -s https://zenodo.org/api/records/10031483 | python -c "
import json,sys; r=json.load(sys.stdin); print(r['metadata']['title'], r['metadata'].get('version'), r['metadata']['publication_date']); print(r['metadata']['description'][:2000])
for f in r['files']: print(f['key'], f['size'])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --filter=blob:none --sparse https://github.com/constantinoplelab/published.git && cd published && git sparse-checkout set rat_behavior && git log -1 --format='%H %cd' && find rat_behavior -type f | head -100 && find rat_behavior -type f | wc -l
```

```
b7b68ca8c107d8ce4a061e16da214307f175c3e5 Fri Sep 25 05:57:44 2026 -0400
rat_behavior/.DS_Store
rat_behavior/Figures/FigureS4.m
rat_behavior/Figures/FigureS3.m
rat_behavior/Figures/FigureS10.m
rat_behavior/Figures/FigureS9.m
rat_behavior/Figures/Figure3.m
rat_behavior/Figures/FigureS11.m
rat_behavior/Figures/FigureS6.m
rat_behavior/Figures/FigureS14.m
rat_behavior/Figures/FigureS12.m
rat_behavior/Figures/FigureS13.m
rat_behavior/Figures/FigureS5.m
rat_behavior/Figures/FigureS2.m
rat_behavior/Figures/FigureS1.m
rat_behavior/Figures/Figure1.m
rat_behavior/Figures/Figure5.m
rat_behavior/Figures/Figure2.m
rat_behavior/Figures/Figure3.asv
rat_behavior/Figures/FigureS7.m
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; cat README.md; cat Figures/Figure1.m
```

```
# rat_behavior: analysis of rat behavior in a temporal wagering task

This is the code used in [Mah, A., Schiereck, S.S., Bossio, V., Constantinople, C.M. (2023). Distinct value computations support rapid sequential decisions. Nature Communications, 2023](https://www.nature.com/articles/s41467-023-43250-x)

The analyses are broken to two primary sets:
1. Analysis of rat's behavior during the task
2. Analysis of behavioral models fit to the rat's behavior
	
## Data
The data associated with this work can be found on Zenodo at LINK TO COME

## Demos
Figures directory contains code to generate every figure in the paper

## Code dependencies
This project was developed with Matlab 2019a, and uses the following toolboxes
  Curve Fitter
	Optimization
	Signal Analyzer

[... 267 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; for f in Analysis/wtcurves.m Analysis/iticurves.m Analysis/getITI.m utils/convertreward.m utils/selectratlist.m; do echo "=== $f"; cat $f; done
```

```
=== Analysis/wtcurves.m
function [hi, lo, mix, p] = wtcurves(A, varargin)
%block 1 is test block.
%block 2 = high adaptation block.
%block 3 = low adaptation block.

A.reward = convertreward(A.reward);
rvec = 1:5;

hi.wt = nan(1, length(rvec));
hi.er = nan(1, length(rvec));

lo.wt = nan(1, length(rvec));
lo.er = nan(1, length(rvec));

mix.wt = nan(1, length(rvec));
mix.er = nan(1, length(rvec));

% A.wait_time(A.wait_time>=A.wt_thresh) = nan;
if ~isempty(varargin)
[... 225 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; cat Figures/Figure2.m | head -250
```

```
function [WT, Lat] = Figure2(datadir, codedir)
%Figure2 - Wait and trial initiation times use distinct estimates of the 
% value of the environment. 
%   datadir = directory of dataset
%   codedir = director of code

%% Set up paths
s = pathsep;
pathStr = [s, path, s];
onPath  = contains(pathStr,...
    codedir, 'IgnoreCase', ispc);

if ~onPath % only add code dir to path if it already isn't
    addpath(genpath(codedir))
end

%% Load data

a = load([datadir filesep 'ratList.mat']);
ratList = a.ratList; % list of rats
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; for f in Analysis/waittime_20ul_by_previous_vol.m Analysis/latency_post20ul_by_previous_vol.m Analysis/block_dynamics_wt.m Analysis/block_dynamics_latency.m Analysis/regress_wt_vs_rew.m Analysis/regress_latency_vs_rew.m utils/fit_exp_decay.m utils/get_tau.m utils/blockhmat_withvios.m; do echo "=== $f"; cat $f; done
```

```
=== Analysis/waittime_20ul_by_previous_vol.m
function [wait_time_mean, pval] =...
    waittime_20ul_by_previous_vol(A, varargin)
%waittime_20ul_by_previous_vol Finds wait time on 20 uL trials in mixed 
% blocks divded into whether the previous volume is < 20 uL or > 20 uL.
%   Input: A - A struct (if you accidentally put in S struct, code will
%       convert)
%          varargin = vector of trials within the A struct that you want to
%          analyze.
%
%   Output: wait_time_mean - Average wait time for < 20 uL and > 20 uL
%       wait_time_sem - SEM for wait time for < 20 uL and > 20 uL

if isfield(A, 'pd') %just in case the input is an S struct.
    [A, ~, ~] = parse_data_from_mysql(A);
end

[~, rew] = convertreward(A.reward);
wt = A.wait_time;

[... 763 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/catalystneuro/constantinople-lab-to-nwb.git && cd constantinople-lab-to-nwb && git log -1 --format='%H %cd' && find . -path ./.git -prune -o -type f -print | grep -v '\.git/' | head -80
```

```
bf2bf769dbd3ae68b6b1016e0d9980ebf78c83af Fri Feb 14 13:37:36 2025 +0100
./freeze_dependencies.py
./pyproject.toml
./.github/workflows/test-install.yml
./.github/workflows/auto-publish.yml
./.github/workflows/add-to-dashboard.yml
./LICENSE
./make_env.yml
./.gitignore
./.pre-commit-config.yaml
./dandi.md
./src/constantinople_lab_to_nwb/another_conversion/__init__.py
./src/constantinople_lab_to_nwb/utils/add_optogenetics_series.py
./src/constantinople_lab_to_nwb/utils/__init__.py
./src/constantinople_lab_to_nwb/utils/fix_xml_openephys.py
./src/constantinople_lab_to_nwb/utils/get_subject_metadata.py
./src/constantinople_lab_to_nwb/general_interfaces/bpodbehaviorinterface.py
./src/constantinople_lab_to_nwb/general_interfaces/__init__.py
./src/constantinople_lab_to_nwb/schierek_embargo_2024/metadata/schierek_embargo_2024_general_metadata.yaml
./src/constantinople_lab_to_nwb/schierek_embargo_2024/metadata/schierek_embargo_2024_optogenetics_stimulation_metadata.yaml
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/constantinople-lab-to-nwb/src/constantinople_lab_to_nwb/mah_2024; cat mah_2024_notes.md interfaces/mah_2024_processedbehaviorinterface.py mah_2024_convert_all_sessions.py metadata/mah_2024_behavior_metadata.yaml | head -500
```

```
# Notes concerning the mah_2024 conversion

### Schematic of behavioral paradigm

From: [Distinct value computations support rapid sequential decisions](https://www.nature.com/articles/s41467-023-43250-x/figures/1)

<img src="behavioral_paradigm_from_article.png" alt="paradigm" width="800"/>

LED illumination from the center port indicated that the animal could initiate a trial by poking its nose in that 
port - upon trial initiation the center LED turned off.
While in the center port, rats needed to maintain center  fixation for a duration drawn uniformly from [0.8, 1.2] seconds.
During the fixation period, a tone played from both speakers, the frequency of which indicated the volume of the offered
water reward for that trial [1, 2, 4, 8, 16kHz, indicating 5, 10, 20, 40, 80μL rewards]. 

Following the fixation period, one of the two side LEDs was illuminated, indicating that the reward might be delivered 
at that port; the side was randomly chosen on  each trial.This event (side LED ON) also initiated a variable and 
unpredictable delay period, which was randomly drawn from an exponential distribution with mean=2.5s. 
The reward port LED remained illuminated for the duration of the delay period, and rats were not required to maintain 
fixation during this period, although they tended to fixate in the reward port. When reward was available, the reward 
port LED turned off, and rats could collect the offered reward by nose poking in that port. The rat could also choose to
[... 481 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/constantinople-lab-to-nwb/src/constantinople_lab_to_nwb/mah_2024; sed -n 200,400p mah_2024_convert_all_sessions.py; grep -n "column_name_mapping\|ITI\|wait_for_cpoke\|zwait\|inter_trial\|wait_thresh" -n mah_2024_convert_session.py mah_2024_convert_all_sessions.py
```

```
)

            session_to_nwb(
                raw_behavior_file_path=raw_behavior_file_path,
                processed_behavior_file_path=processed_behavior_file_path,
                date_index=date_index,
                nwbfile_path=nwbfile_path,
                column_name_mapping=column_name_mapping,
                column_descriptions=column_descriptions,
                subject_metadata=subject_metadata,
                overwrite=overwrite,
            )


if __name__ == "__main__":

    # Parameters for conversion
    processed_behavior_folder_path = Path(r"/Volumes/T9/Constantinople/published/A_Structs_Final")
    raw_behavior_folder_path = Path(r"/Volumes/T9/Constantinople/raw_Bpod")
    rat_info_folder_path = Path(r"/Volumes/T9/Constantinople/Rat_info")
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; cat > $TMPDIR/bench.py <<'EOF'
import json, time, numpy as np, h5py, remfile, sys
from concurrent.futures import ThreadPoolExecutor
rows=json.load(open('paper/assets.json'))
import random; random.seed(0); sample=random.sample(rows,int(sys.argv[1]))
COLS=['block_type','reward_volume_ul','is_catch','is_rewarded','is_violation','is_opt_out','wait_time','wait_time_unthresholded','wait_time_threshold','inter_trial_interval','training_stage','start_time']
def url(a): return f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
def s3(a):
    return a.get('blob')
def read(a):
    import requests
    t=time.time()
    u=requests.head(url(a),allow_redirects=False).headers['Location'].split('?')[0]
    with h5py.File(remfile.File(u),'r') as f:
        g=f['intervals/processed_trials']
        d={c:g[c][:] for c in COLS}
        d['subject']=f['general/subject/subject_id'][()]
    return time.time()-t, len(d['wait_time'])
t=time.time()
with ThreadPoolExecutor(int(sys.argv[2])) as ex: res=list(ex.map(read,sample))
el=time.time()-t
print(el, el/len(sample)*23034/60, 'min est', np.median([r[0] for r in res]))
EOF
$PY $TMPDIR/bench.py 64 16
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; cat > $TMPDIR/bench2.py <<'EOF'
import json, time, numpy as np, h5py, io, sys, requests
from concurrent.futures import ThreadPoolExecutor
rows=json.load(open('paper/assets.json'))
print(rows[0].keys())
import random; random.seed(1); sample=random.sample(rows,int(sys.argv[1]))
COLS=['block_type','reward_volume_ul','is_catch','is_rewarded','is_violation','is_opt_out','wait_time','wait_time_unthresholded','wait_time_threshold','inter_trial_interval','training_stage','start_time']
sess=requests.Session()
ad=requests.adapters.HTTPAdapter(pool_maxsize=64); sess.mount('https://',ad)
def read(a):
    t=time.time()
    b=sess.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/").content
    with h5py.File(io.BytesIO(b),'r') as f:
        g=f['intervals/processed_trials']
        d={c:g[c][:] for c in COLS}
    return time.time()-t, len(b)
t=time.time()
with ThreadPoolExecutor(int(sys.argv[2])) as ex: res=list(ex.map(read,sample))
el=time.time()-t
mb=sum(r[1] for r in res)/1e6
print(el, el/len(sample)*23034/60, 'min est', np.median([r[0] for r in res]), mb/el,'MB/s')
EOF
$PY $TMPDIR/bench2.py 200 32
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; sed -i 's#sess.get(f"https://api.dandiarchive.org/api/assets/{a\[.asset_id.\]}/download/")#sess.get(f"https://dandiarchive.s3.amazonaws.com/blobs/{a[\x27blob\x27][:3]}/{a[\x27blob\x27][3:6]}/{a[\x27blob\x27]}")#' $TMPDIR/bench2.py; grep sess.get $TMPDIR/bench2.py; $PY $TMPDIR/bench2.py 400 64
```

```
b=sess.get(f"https://dandiarchive.s3.amazonaws.com/blobs/{a['blob'][:3]}/{a['blob'][3:6]}/{a['blob']}").content
dict_keys(['asset_id', 'blob', 'zarr', 'path', 'size', 'created', 'modified'])
6.794792413711548 6.521302019059658 min est 0.8975948095321655 69.87660109260787 MB/s
```

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import json, h5py, io, requests, numpy as np
rows=json.load(open('paper/assets.json'))
def get(a):
    b=requests.get(f"https://dandiarchive.s3.amazonaws.com/blobs/{a['blob'][:3]}/{a['blob'][3:6]}/{a['blob']}").content
    return h5py.File(io.BytesIO(b),'r')
for p in ['sub-G001','sub-J031']:
    a=[r for r in rows if r['path'].startswith(p+'/')][0]
    print(a['path'])
    f=get(a)
    print(list(f['intervals/processed_trials'].keys()))
    ta=f['general/task/task_arguments']
    for n,d,e in zip(ta['argument_name'][:],ta['argument_description'][:],ta['expression'][:]): print(' ',n,'|',e,'|',d[:80])
    print('states',f['general/task/state_types/state_name'][:])
    print('events',f['general/task/event_types/event_name'][:])
    for k in ['session_description','session_id','experiment_description','general/protocol','general/related_publications','general/keywords','session_start_time','general/subject/age','general/subject/sex','general/subject/species','general/subject/description','general/subject/subject_id','general/session_id','general/experiment_description']:
        try: print(k, f[k][()])
        except Exception as e: print(k,'missing')
    g=f['intervals/processed_trials']
    import pandas as pd
    df=pd.DataFrame({k:g[k][:] for k in g.keys() if k!='id'})
    print(df.head(12).to_string()); print(df.describe().T.to_string())
    t=f['intervals/trials']; print(t['catch_percentage'][:5], t['training_stage'][:5], t['is_warm_up'][:5].sum(), len(t['start_time']))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; wc -l Figures/*.m Analysis/*.m BehavioralModel/*/*.m; grep -n "load\|datadir\|Struct" Figures/Figure3.m Figures/Figure4.m Figures/Figure5.m Figures/FigureS2.m Figures/FigureS12.m | head -60
```

```
256 Figures/Figure1.m
   422 Figures/Figure2.m
   580 Figures/Figure3.m
   308 Figures/Figure4.m
   238 Figures/Figure5.m
    64 Figures/FigureS1.m
    32 Figures/FigureS10.m
   108 Figures/FigureS11.m
   169 Figures/FigureS12.m
   108 Figures/FigureS13.m
   101 Figures/FigureS14.m
   294 Figures/FigureS2.m
   283 Figures/FigureS3.m
    82 Figures/FigureS4.m
   114 Figures/FigureS5.m
   105 Figures/FigureS6.m
    99 Figures/FigureS7.m
   118 Figures/FigureS8.m
    98 Figures/FigureS9.m
   181 Analysis/block_dynamics_latency.m
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; VIRTUAL_ENV=$TMPDIR/scratch uv pip install -q remotezip 2>&1|tail -1; $PY - <<'EOF'
from remotezip import RemoteZip
import collections
url="https://zenodo.org/records/10031483/files/published.zip?download=1"
with RemoteZip(url) as z:
    infos=z.infolist()
    print(len(infos))
    agg=collections.defaultdict(lambda:[0,0])
    for i in infos:
        parts=i.filename.split('/')
        key='/'.join(parts[:2]) if len(parts)>2 else i.filename
        agg[key][0]+=1; agg[key][1]+=i.file_size
    for k,v in sorted(agg.items()): print(k, v[0], round(v[1]/1e9,3),'GB')
    import json; json.dump([(i.filename,i.file_size,i.compress_size) for i in infos], open('paper/zenodo_list.json','w'))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
from remotezip import RemoteZip
url="https://zenodo.org/records/10031483/files/published.zip?download=1"
with RemoteZip(url) as z:
    print(z.read('published/README.txt').decode()[:5000])
    names=[i.filename for i in z.infolist()]
    a=[n for n in names if 'A_Structs_Final' in n][:3]; print(a)
    b=z.read(a[1]); print(len(b), b[:128])
    s=[n for n in names if 'A_Structs_all' in n][:3]; print(s)
    m=[n for n in names if 'ModelFits' in n]; print(m[:20]); 
    import collections; print(collections.Counter(n.split('/')[2] if n.count('/')>2 else '' for n in m))
EOF
```

```
This behavioral and modeling data was used and described in the following paper:

Mah, A., Schiereck, S.S., Bossio, V., Constantinople, C.M. (2023). Distinct value computations support rapid sequential decisions. Nature Communications.

The dataset comprises 1) Behavioral data for the value-based decision making task in rats, and 2) computational models fit to the rat behavioral data. All files are Matlab data (.mat) files.

The code to analyze this data and generate all figures in Mah et al., 2023 is available at https://github.com/constantinoplelab/published/tree/main/rat_behavior. Data was analyzed using Matlab 2023a with the following additional toolboxes:
	Curve Fitter
	Optimization
	Signal Analyzer

-----------------------------------------------------------------------------------------------------Useful files
-----------------------------------------------------------------------------------------------------

ratList.mat - Matlab struct containing rat identifiers and sex.
	ratList - a list of rat identifiers (291 x 1)
	sexList - sex of each rat. Rows correspond to identifiers in ratList (291 x 1)


-----------------------------------------------------------------------------------------------------Rat Datasets
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; cat BehavioralModel/WaitTimeModels/GenerateSynthData_Bayes.m BehavioralModel/WaitTimeModels/GenerateSynthData_AlphaPHModel.m BehavioralModel/utils/generate_wts.m Analysis/model_comparison.m
```

```
function [WTOpt, WTMdl, BlkInf, Belief, Prior, Kappa] =...
    GenerateSynthData_Bayes(params, ratTrial,...
    noise_arg, gen_arg, noise_params)
%GenerateSynthData_Bayes - generates synthetic wait times
%for optimal Bayes model.
% Inputs:
%   params - Parameter vector. [kappa_mi, kappa_hi, kappa_lo, D, lambda]
%       kappa_mi, kappa_hi, kappa_lo - opportunity costs for each block.
%       D - scaling parameter 
%           ALL PARAMS ARE IN [0, 1]
%   ratTrial - Struct containing rat's data. Saved under server at
%       BehavioralModel/Data/ratTrial_ratname
%   noise_arg - What type of noise model. Always use 'logn'
%   gen_arg - Whether to generate noisy data (WTMdl) or not. Logical
%   noise_params - Variance of the noise. Always use 8
% Outputs:
%   WTOpt - Optimal wait times
%   WTMdl - Noisy wait times generate from WTOpt with constant variance
%   BlkInf - Inferred block
%   Belief - Posterior probability distribution over blocks for each trial
[... 425 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
L=json.load(open('paper/zenodo_list.json'))
for n,s,c in L:
    if 'Fits/' not in n and 'A_Structs' not in n: print(n,s)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; cat Analysis/myTauShuffleTest.m Analysis/wtByPCatch.m; sed -n 1,80p Figures/FigureS12.m; sed -n 1,120p Figures/FigureS2.m
```

```
function [shuffleTauDiff, observedTauDiff, pval] =...
    myTauShuffleTest(first_q, last_q, myBetas, Nshuffle)
Betas = myBetas(first_q | last_q,:);
nrats = size(Betas, 1);

shuffleTau = nan(Nshuffle, 2);

for ii = 1:Nshuffle
    fprintf('shuffle %d out of %d\n', ii, Nshuffle)
    shuffleLatency = randperm(nrats)';
    
    group1 = shuffleLatency(1:floor(nrats)/2);
    Betas1 = mean(Betas(group1,1:end-1));
    [~, bestFit1] = fit_exp_decay(1:10, 10*Betas1, 10,...
        [-3 0], [1 50]);
    shuffleTau(ii,1) = bestFit1(2);
    
    group2 = shuffleLatency(floor(nrats)/2+1:end);
    Betas2 = mean(Betas(group2,1:end-1));
    [~, bestFit2] = fit_exp_decay(1:10, 10*Betas2, 10,...
[... 290 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; sed -n 1,160p Figures/Figure4.m; sed -n 1,80p Figures/Figure5.m
```

```
function [] = Figure4(datadir, codedir)
%Figure4 - Block sensitivity for wait times requires structure learning
%   datadir = directory of dataset
%   codedir = director of code

%% Set up paths
s = pathsep;
pathStr = [s, path, s];
onPath  = contains(pathStr,...
    codedir, 'IgnoreCase', ispc);

if ~onPath % only add code dir to path if it already isn't
    addpath(genpath(codedir))
end

%% Analyze data

a = load([datadir filesep 'ratList.mat']);
ratList = a.ratList; % List of rats

[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; cat Analysis/macro_regress_overtraining_V2.m; sed -n 160,308p Figures/Figure4.m | grep -v "^ *%" | head -150
```

```
function [B1, B2, B1iti, B2iti,...
    dwt1, dwt2, diti1, diti2,...
    pcatch1, pcatch2, pvio_iti1, pvio_iti2] =...
    macro_regress_overtraining_V2(nsess, ratList, Sdir)

%this version compares early sessions in training stage 9 from the S
%struct, instead of the A struct, which has already been curated. cmc
%11/16/22.
% updated to incorporate into Figure 3 code. avm 27 Jan 2023
grp = 2;

[B1, B2, B1iti, B2iti] = deal(cell(1, 3));

for k = 1:3
    B1{k} = nan(length(ratList), ceil(nsess/grp));
    B2{k} = nan(length(ratList), ceil(nsess/grp));
    B1iti{k} = nan(length(ratList), ceil(nsess/grp));
    B2iti{k} = nan(length(ratList), ceil(nsess/grp));
end

[... 298 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; cat Analysis/regress_trials_blocksv2.m; cd  python - <<'EOF'
import json, collections
rows=json.load(open('paper/assets.json'))
for r in ['M041','M045','G070','E005','S042','S050']:
    ses=sorted(a['path'].split('_ses-')[1] for a in rows if a['path'].startswith(f'sub-{r}/'))
    print(r, len(ses), ses[0], ses[-1], sum(s.split('-')[1]>='20221004' for s in ses))
print([a['path'] for a in rows if 'RWTautowait2-2022' in a['path'] and a['path'].count('-')>4][:5])
print([a['path'] for a in rows if 'WP' in a['path']])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import json, h5py, io, requests, numpy as np
rows=json.load(open('paper/assets.json'))
def get(a):
    b=requests.get(f"https://dandiarchive.s3.amazonaws.com/blobs/{a['blob'][:3]}/{a['blob'][3:6]}/{a['blob']}").content
    return h5py.File(io.BytesIO(b),'r')
def args(p):
    a=[r for r in rows if r['path'].endswith(p)][0]
    f=get(a); ta=f['general/task/task_arguments']
    d={n.decode():e.decode() for n,e in zip(ta['argument_name'][:],ta['expression'][:])}
    st=[s.decode() for s in f['general/task/state_types/state_name'][:]]
    at=[s.decode() for s in f['general/task/action_types/action_name'][:]]
    return d,st,at,f
ses={}
for r in ['M041']:
    ss=sorted(a['path'] for a in rows if a['path'].startswith(f'sub-{r}/'))
    early=[s for s in ss if s.split('-')[3]<'20221004'][0]; late=[s for s in ss if s.split('-')[3]>='20221104'][0]
    d1,s1,a1,f1=args(early); d2,s2,a2,f2=args(late)
    print(early, late)
    print('args only early', set(d1)-set(d2), 'only late', set(d2)-set(d1))
    print({k:(d1[k],d2[k]) for k in d1 if k in d2 and d1[k]!=d2[k]})
    print(s1,s2,a1,a2)
    # actions timing relative to states
    for f in (f1,f2):
        acts=f['acquisition/task_recording/actions']; print(acts['timestamp'][:6], acts['value'][:6], acts['action_type'][:6])
        stt=f['acquisition/task_recording/states']; names=[s.decode() for s in f['general/task/state_types/state_name'][:]]
        print([(names[i], round(a,3), round(b,3)) for i,a,b in zip(stt['state_type'][:12], stt['start_time'][:12], stt['stop_time'][:12])])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import json, h5py, io, requests, numpy as np
rows=json.load(open('paper/assets.json'))
def get(a):
    b=requests.get(f"https://dandiarchive.s3.amazonaws.com/blobs/{a['blob'][:3]}/{a['blob'][3:6]}/{a['blob']}").content
    return h5py.File(io.BytesIO(b),'r')
def args(p):
    a=[r for r in rows if r['path']==p][0]
    f=get(a); ta=f['general/task/task_arguments']
    d={n.decode():e.decode() for n,e in zip(ta['argument_name'][:],ta['expression'][:])}
    st=[s.decode() for s in f['general/task/state_types/state_name'][:]]
    at=[s.decode() for s in f['general/task/action_types/action_name'][:]]
    return d,st,at,f
date=lambda s: s.split('_ses-')[1].split('-')[1]
ss=sorted((a['path'] for a in rows if a['path'].startswith('sub-M041/')), key=date)
early=[s for s in ss if date(s)<'20221004'][-1]; late=[s for s in ss if date(s)>='20221104'][0]
d1,s1,a1,f1=args(early); d2,s2,a2,f2=args(late)
print(early, late)
print('args only early', set(d1)-set(d2), 'only late', set(d2)-set(d1))
print({k:(d1[k],d2[k]) for k in d1 if k in d2 and d1[k]!=d2[k]})
print(s1,s2,a1,a2)
for f in (f1,f2):
    acts=f['acquisition/task_recording/actions']; print(acts['timestamp'][:6], acts['value'][:6], acts['action_type'][:6])
    stt=f['acquisition/task_recording/states']; names=[s.decode() for s in f['general/task/state_types/state_name'][:]]
    print([(names[i], round(a,3), round(b,3)) for i,a,b in zip(stt['state_type'][:14], stt['start_time'][:14], stt['stop_time'][:14])])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY -c "
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); d=c.get_dandiset('001169','0.260825.1909')
it=d.get_assets()
a=next(it); print(type(a), a.path, getattr(a,'blob',None)); print(a.get_content_url(follow_redirects=1, strip_query=True))
"; nproc; free -g
```

```
<class 'dandi.dandiapi.RemoteBlobAsset'> sub-C015/sub-C015_ses-RWTautowait-20191017-093757.nwb 973107bd-cd62-4720-ad12-fcc37097ed29
https://dandiarchive.s3.amazonaws.com/blobs/973/107/973107bd-cd62-4720-ad12-fcc37097ed29
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           4          14
Swap:              2           0           2
```

**Agent calls Write**

```json
{
 "file_path": "entries/001169-mah-2023/wagering.py",
 "content": "\"\"\"Loading and measures for the temporal wagering task of dandiset 001169.\n\nMah, Schiereck, Bossio & Constantinople (2023), Nature Communications 14:7573,\ndoi:10.1038/s41467-023-43250-x.\n\nEach NWB file holds one session of one rat. The analysis uses the table\n`intervals/processed_trials`, which the conversion\n(https://github.com/catalystneuro/constantinople-lab-to-nwb, commit bf2bf76) filled from the\npaper's processed per-rat structs (`A_Structs_Final` in Zenodo 10.5281/zenodo.10031483), the\ncatch probability from the raw trials table (`intervals/trials/catch_percentage`), and the\ntask argument `center_port_cue` of the pre-initiation cue sessions. Each file is about 1 MB\nand is read whole into memory from the archive at the pinned version, in parallel; nothing is\nwritten to disk.\n\nWhere the parameters come from. The paper's analysis code is\nhttps://github.com/constantinoplelab/published/tree/main/rat_behavior at commit\nb7b68ca8c107d8ce4a061e16da214307f175c3e5; the function it follows is named in each docstring.\n\n- Rewards of 4, 8, 16, 32 and 64 uL (some female rats) are treated as 5, 10, 20, 40 and\n  80 uL (Methods; `convertreward.m`).\n- Trial initiation times above the 99th percentile of the rat's pooled distribution are\n  removed (Methods; `iticurves.m` and others).\n- `wait_time` is the conversion's copy of the processed wait time, already thresholded at the\n  rat's mean + 1 SD (Methods, Statistical analyses).\n- Blocks: 1 mixed, 2 high, 3 low, as in the paper's structs.\n- Block transitions in the first 40 trials of a session are ignored (`blockhmat_withvios.m`).\n- Model constants (H0 = 1/40, delay time constant 2.5 s, log-normal noise of variance 8 s,\n  reward and block probabilities) are from the Methods and the generative model code\n  (`GenerateSynthData_Bayes.m`, `GenerateSynthData_AlphaPHModel.m`).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport threading\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import optimize, stats\n\nDANDISET_ID = \"001169\"\nDANDISET_VERSION = \"0.260825.1909\"\n\nBLOCK_CODE = {\"Mixed\": 1, \"High\": 2, \"Low\": 3}\nSTANDARD_VOLUMES = np.array([5, 10, 20, 40, 80])\nVOLUME_TO_STANDARD = {4: 5, 5: 5, 8: 10, 10: 10, 16: 20, 20: 20, 32: 40, 40: 40, 64: 80, 80: 80}\n\nTRIAL_COLUMNS = [\"block_type\", \"reward_volume_ul\", \"is_catch\", \"is_rewarded\", \"is_violation\",\n                 \"is_opt_out\", \"wait_time\", \"wait_time_unthresholded\", \"wait_time_threshold\",\n                 \"inter_trial_interval\", \"wait_for_center_poke\", \"training_stage\", \"start_time\"]\n\n\n# ----------------------------------------------------------------------------------------\n# Loading\n# ----------------------------------------------------------------------------------------\n\ndef blob_url(blob_id: str) -> str:\n    return f\"https://dandiarchive.s3.amazonaws.com/blobs/{blob_id[:3]}/{blob_id[3:6]}/{blob_id}\"\n\n\ndef asset_list() -> pd.DataFrame:\n    \"\"\"Path, size and content URL of every asset at the pinned version.\"\"\"\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        rows = [{\"path\": a.path, \"size\": a.size, \"blob\": a.blob} for a in dandiset.get_assets()]\n    assets = pd.DataFrame(rows).sort_values(\"path\").reset_index(drop=True)\n    assets[\"url\"] = assets.blob.map(blob_url)\n    return assets\n\n\ndef _text(value) -> str:\n    return value.decode() if isinstance(value, bytes) else str(value)\n\n\ndef read_session(content: bytes) -> tuple[dict, pd.DataFrame]:\n    \"\"\"Session metadata and the processed trials of one NWB file held in memory.\"\"\"\n    with h5py.File(io.BytesIO(content), \"r\") as f:\n        g = f[\"intervals/processed_trials\"]\n        trials = pd.DataFrame({c: g[c][:] for c in TRIAL_COLUMNS})\n        raw = f[\"intervals/trials\"]\n        trials[\"catch_percentage\"] = raw[\"catch_percentage\"][:]\n        args = f[\"general/task/task_arguments\"]\n        arguments = {_text(n): _text(e) for n, e in zip(args[\"argument_name\"][:], args[\"expression\"][:])}\n        subject = f[\"general/subject\"]\n        meta = {\n            \"subject_id\": _text(subject[\"subject_id\"][()]),\n            \"sex\": _text(subject[\"sex\"][()]),\n            \"species\": _text(subject[\"species\"][()]),\n            \"session_id\": _text(f[\"general/session_id\"][()]),\n            \"session_start\": _text(f[\"session_start_time\"][()]),\n            \"protocol\": _text(f[\"general/protocol\"][()]),\n            \"n_raw_trials\": len(raw[\"start_time\"]),\n            \"center_port_cue\": arguments.get(\"center_port_cue\", \"absent\"),\n            \"has_age\": \"age\" in subject,\n            \"processed_columns\": tuple(sorted(g.keys())),\n        }\n    trials[\"block_type\"] = [BLOCK_CODE[_text(b)] for b in trials[\"block_type\"]]\n    return meta, trials\n\n\n_local = threading.local()\n\n\ndef _fetch(url: str) -> bytes:\n    if not hasattr(_local, \"session\"):\n        _local.session = requests.Session()\n    for attempt in range(5):\n        response = _local.session.get(url, timeout=120)\n        if response.ok:\n            return response.content\n    response.raise_for_status()\n\n\ndef _load_one(row) -> tuple[dict, pd.DataFrame]:\n    meta, trials = read_session(_fetch(row.url))\n    meta[\"path\"] = row.path\n    return meta, trials\n\n\ndef load_all(assets: pd.DataFrame, max_workers: int = 48) -> tuple[pd.DataFrame, pd.DataFrame]:\n    \"\"\"Sessions and trials of every asset. Trials are in session order (by start time) and\n    in trial order within a session; `session` indexes the sessions table.\"\"\"\n    with ThreadPoolExecutor(max_workers) as pool:\n        results = list(pool.map(_load_one, assets.itertuples()))\n    sessions = pd.DataFrame([m for m, _ in results])\n    sessions[\"n_trials\"] = [len(t) for _, t in results]\n    sessions[\"start\"] = pd.to_datetime(sessions.session_start, utc=True)\n    order = sessions.sort_values([\"subject_id\", \"start\"]).index.to_numpy()\n    sessions = sessions.loc[order].reset_index().rename(columns={\"index\": \"file_index\"})\n    parts = []\n    for k, i in enumerate(order):\n        t = results[i][1]\n        t.insert(0, \"session\", np.int32(k))\n        t.insert(1, \"trial\", np.arange(len(t), dtype=np.int32))\n        parts.append(t)\n    trials = pd.concat(parts, ignore_index=True)\n    trials[\"rat\"] = sessions.subject_id.to_numpy()[trials.session]\n    trials[\"reward\"] = trials.reward_volume_ul.map(VOLUME_TO_STANDARD).astype(np.int16)\n    for c in [\"wait_time\", \"wait_time_unthresholded\", \"wait_time_threshold\", \"inter_trial_interval\",\n              \"wait_for_center_poke\", \"start_time\", \"catch_percentage\"]:\n        trials[c] = trials[c].astype(np.float32 if c != \"start_time\" else np.float64)\n    trials[\"block_type\"] = trials.block_type.astype(np.int8)\n    trials[\"rat\"] = trials.rat.astype(\"category\")\n    return sessions, trials\n"
}
```

```
File created successfully at: entries/001169-mah-2023/wagering.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001169-mah-2023; PY=$TMPDIR/scratch/bin/python; VIRTUAL_ENV=$TMPDIR/scratch uv pip install -q pyarrow 2>&1|tail -1; time $PY - <<'EOF'
import time, wagering as w, os
t=time.time()
assets=w.asset_list(); print(len(assets), time.time()-t)
sessions, trials = w.load_all(assets)
print(time.time()-t, len(sessions), len(trials), trials.memory_usage(deep=True).sum()/1e6)
d=os.environ['TMPDIR']
sessions.drop(columns=['processed_columns']).assign(cols=sessions.processed_columns.map(lambda x:','.join(x))).to_parquet(f'{d}/sessions.parquet')
trials.to_parquet(f'{d}/trials.parquet')
assets.to_parquet(f'{d}/assets.parquet')
EOF
```

```
23034 15.871451377868652
534.0805578231812 23034 10408925 676.583786

real	8m59.950s
user	10m4.300s
sys	1m56.783s
```

**Agent calls Bash**

```bash
cd entries/001169-mah-2023; PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import pandas as pd, numpy as np, os
d=os.environ['TMPDIR']
S=pd.read_parquet(f'{d}/sessions.parquet'); T=pd.read_parquet(f'{d}/trials.parquet')
print(S.columns.tolist())
print(S.sex.value_counts(), S.groupby('subject_id').sex.first().value_counts())
print(S.species.value_counts()); print('has_age', S.has_age.sum())
print(S.protocol.value_counts())
print(S.center_port_cue.value_counts())
print(S[S.center_port_cue!='absent'].groupby('subject_id').center_port_cue.value_counts())
print('n_raw==n_proc', (S.n_raw_trials==S.n_trials).mean())
print(S.cols.value_counts())
per=S.groupby('subject_id').agg(n=('n_trials','size'), tr=('n_trials','sum'))
print('rats',len(per),'median sessions',per.n.median(),'median trials',per.tr.median())
print(T.training_stage.value_counts())
print(T.reward_volume_ul.value_counts().sort_index())
print(T.groupby('rat',observed=True).reward_volume_ul.min().value_counts())
print(T.block_type.value_counts())
print(T.catch_percentage.value_counts().sort_index())
print(T[['wait_time','wait_time_unthresholded','inter_trial_interval','wait_for_center_poke']].describe().T)
EOF
```

```
['file_index', 'subject_id', 'sex', 'species', 'session_id', 'session_start', 'protocol', 'n_raw_trials', 'center_port_cue', 'has_age', 'path', 'n_trials', 'start', 'cols']
sex
M    14950
F     8084
Name: count, dtype: int64 sex
M    184
F    107
Name: count, dtype: int64
species
Rattus norvegicus    23034
Name: count, dtype: int64
has_age 1181
protocol
RWTautowait2     22943
RWTautowait         86
RWTautowaitWP        5
Name: count, dtype: int64
center_port_cue
absent    16274
False      5998
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001169-mah-2023; PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import pandas as pd, numpy as np, os, hashlib
d=os.environ['TMPDIR']
S=pd.read_parquet(f'{d}/sessions.parquet'); T=pd.read_parquet(f'{d}/trials.parquet')
cue=S[S.center_port_cue=='True'].groupby('subject_id').size(); print(cue.to_string())
print(S[S.has_age].subject_id.unique()[:20], S[S.has_age].subject_id.nunique())
# duplicates: hash of reward sequence + ITI rounded
T['k']=T.inter_trial_interval.round(3).astype(str)+'_'+T.reward_volume_ul.astype(str)
h=T.groupby('session').k.apply(lambda s: hashlib.md5(''.join(s).encode()).hexdigest())
S['h']=h.values
dup=S[S.duplicated('h',keep=False)].sort_values('h')
print('dup sessions', len(dup)); print(dup[['subject_id','session_id','n_trials','h']].head(30).to_string())
# sessions on the same date per rat
S['date']=S.session_id.str.split('-').str[1]
dd=S[S.duplicated(['subject_id','date'],keep=False)]
print('same-date pairs', len(dd)); print(dd[['subject_id','session_id','n_trials']].head(20).to_string())
print(S[S.session_id.str.count('-')>2][['subject_id','session_id','n_trials']])
EOF
```

```
Exit code 1
subject_id
E005    15
E008    73
G069    75
G070    37
G076    54
G078    26
M041    33
M042    13
M043    60
M044    89
M045    69
M046    57
M047    69
M048    73
S042    13
S050     6
<ArrowStringArray>
['C015', 'C033', 'C034', 'C035', 'C036', 'E001', 'E002', 'E006', 'J011',
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001169-mah-2023; PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
import pandas as pd, numpy as np, os
d=os.environ['TMPDIR']
S=pd.read_parquet(f'{d}/sessions.parquet'); T=pd.read_parquet(f'{d}/trials.parquet')
# fingerprint: n_trials, sum of ITI, sum of reward, first trial start_time
g=T.groupby('session')
fp=pd.DataFrame({'n':g.size(),'iti':g.inter_trial_interval.sum().round(2),'rew':g.reward_volume_ul.sum(),'wt':g.wait_time.sum().round(2)})
S=S.join(fp)
dup=S[S.duplicated(['n','iti','rew','wt'],keep=False)].sort_values(['n','iti'])
print('dup sessions by fingerprint', len(dup)); print(dup[['subject_id','session_id','n_trials','iti','rew']].head(30).to_string())
S['date']=S.session_id.str.split('-').str[1]
dd=S[S.duplicated(['subject_id','date'],keep=False)]
print('same rat same date', len(dd)); print(dd[['subject_id','session_id','n_trials','iti','rew']].head(20).to_string())
print(S[S.session_id.str.count('-')>2][['subject_id','session_id','n_trials']])
# start_time continuity within sessions
st=T.groupby('session').start_time.apply(lambda s: (np.diff(s.values)<=0).sum())
print('non-increasing start times', (st>0).sum())
print('session start range', S.start.min(), S.start.max())
EOF
```

```
dup sessions by fingerprint 2
      subject_id                      session_id  n_trials          iti   rew
13780       L011  RWTautowait2-20221004-095612-x       226  1636.920044  5935
13781       L011    RWTautowait2-20221004-095612       226  1636.920044  5935
same rat same date 40
     subject_id                    session_id  n_trials          iti    rew
284        C036  RWTautowait2-20191217-114651       376  4722.819824  10580
285        C036  RWTautowait2-20191217-135823       236  3801.899902   6890
1154       G008  RWTautowait2-20200807-101101       319  2393.449951   7120
1155       G008  RWTautowait2-20200807-132104       359  3063.409912  10510
1386       G022  RWTautowait2-20201008-101139       427  2537.760010   9812
1387       G022  RWTautowait2-20201008-102726       390  2609.659912   9184
1678       G026  RWTautowait2-20210513-100942       514  2929.100098  10812
1679       G026  RWTautowait2-20210513-140900       421  4436.770020   8520
4213       G057  RWTautowait2-20220518-134519       707   771.489990  13116
4214       G057  RWTautowait2-20220518-172414       589  2222.790039  13604
4808       G067  RWTautowait2-20220413-101211       582  2948.479980  11932
4809       G067  RWTautowait2-20220413-153323       489  3154.580078  11292
4812       G067  RWTautowait2-20220418-152733       819  2107.709961  16624
4813       G067  RWTautowait2-20220418-153548       356  3904.179932   6848
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; sed -n 1,140p Figures/Figure3.m; grep -n "Generate\|alpha\|params" Figures/FigureS7.m | head -30; sed -n 1,98p Figures/FigureS9.m | grep -v "^ *%" | head -80
```

```
function [BestFit_mf, BestFit_mb,...
    BestFit_mb_lambda] = Figure3(datadir, codedir)
%Figure3 - Computational modeling reveals distinct value computations for 
% wait time and trial initiation
%   datadir = directory of dataset
%   codedir = director of code

%% Set up paths
s = pathsep;
pathStr = [s, path, s];
onPath  = contains(pathStr,...
    codedir, 'IgnoreCase', ispc);

if ~onPath % only add code dir to path if it already isn't
    addpath(genpath(codedir))
end

%% Load model fits - takes a while
disp('loading data. may take a while.')
mdl1 = 'AlphaPH';
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/scratch/bin/python; $PY - <<'EOF'
from remotezip import RemoteZip
import scipy.io as sio, io, numpy as np, time, pandas as pd, os
url="https://zenodo.org/records/10031483/files/published.zip?download=1"
t=time.time()
with RemoteZip(url) as z:
    b=z.read('published/A_Structs_Final/ratTrial_L011.mat')
    rl=sio.loadmat(io.BytesIO(z.read('published/ratList.mat')),simplify_cells=True)
print(time.time()-t)
A=sio.loadmat(io.BytesIO(b),simplify_cells=True)['A']
for k,v in A.items(): print(k, type(v), getattr(v,'shape',None) if not isinstance(v,(str,float,int)) else v)
print(A['ntrials'][:5], len(A['ntrials']), A['date'][:3])
print(rl.keys(), len(rl['ratList']), pd.Series(rl['sexList']).value_counts())
d=os.environ['TMPDIR']
S=pd.read_parquet(f'{d}/sessions.parquet')
print(S[S.subject_id=='L011'].n_trials.tolist()[:10], (S.subject_id=='L011').sum())
EOF
```

```
5.400875806808472
date <class 'scipy.io.matlab._mio5_params.MatlabOpaque'> (1,)
trainingstage <class 'numpy.ndarray'> (71870,)
nic <class 'numpy.ndarray'> (71870,)
catch <class 'numpy.ndarray'> (71870,)
prob_catch <class 'numpy.ndarray'> (71870,)
adapt_block <class 'numpy.ndarray'> (71870,)
test_block <class 'numpy.ndarray'> (71870,)
reward <class 'numpy.ndarray'> (71870,)
reward_delay <class 'numpy.ndarray'> (71870,)
block <class 'numpy.ndarray'> (71870,)
hits <class 'numpy.ndarray'> (71870,)
vios <class 'numpy.ndarray'> (71870,)
optout <class 'numpy.ndarray'> (71870,)
wait_time <class 'numpy.ndarray'> (71870,)
wait_for_cpoke <class 'numpy.ndarray'> (71870,)
zwait_for_cpoke <class 'numpy.ndarray'> (71870,)
ntrials <class 'numpy.ndarray'> (204,)
trial_num <class 'numpy.ndarray'> (71870,)
side <class 'numpy.ndarray'> (71870,)
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json
for n in ['claims','attempt','entry']:
    s=json.load(open(f'schemas/{n}.schema.json')); print(n, json.dumps(s)[:3500]); print()
"
```

```
claims {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": "Claims proposed for one target (a dandiset and one of its papers)", "description": "Draft. To be revised after the pilot.", "type": "object", "additionalProperties": false, "required": ["schema_version", "dandiset", "paper", "claims"], "properties": {"schema_version": {"const": 1}, "dandiset": {"type": "string", "pattern": "^[0-9]{6}$"}, "paper": {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}, "claims": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["id", "statement", "source"], "properties": {"id": {"description": "Stable within the file, e.g. fig2b.", "type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}, "statement": {"description": "The finding in one or two sentences, in words. Not a copy of the figure.", "type": "string", "minLength": 1}, "source": {"description": "Where the paper shows it, e.g. 'Figure 2B' or 'Results, paragraph 3'.", "type": "string"}, "expected": {"description": "The reported numbers the claim rests on, each with a tolerance: one, or a list.", "oneOf": [{"$ref": "#/$defs/expected"}, {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/expected"}}]}, "criterion": {"description": "For a claim without a number, how it will be judged. Written before the analysis is run.", "type": "string"}, "depends_on": {"description": "Ids of claims in this file whose result this one uses.", "type": "array", "items": {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}}, "data": {"description": "What the claim's test uses: the dandiset alone (the default); the dandiset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dandiset; the dandiset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in another public archive, which the dandiset does not hold (`elsewhere`), counted apart from both. Outside sources that a test 
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; cat Analysis/myLambdaShuffleTest.m utils/my_fit_sigmoid.m; sed -n 140,330p Figures/Figure3.m | grep -v "^ *%" | grep -n "lambda\|prctile\|Shuffle\|sigmoid\|block_dynamics\|final_params\|N ="
```

```
function [shuffleDist, trueDiff, pvals, trueParams] =...
    myLambdaShuffleTest(dataLo, dataHi, nPerms, twin)

niters = 10;
xs = -(twin-10):(twin-10);

% myNorm = @(x) x-mean(x(1:twin));
myNorm = @(x) x;

[group1Params, group2Params] = deal(nan(size(dataLo, 1), 4));

dataAll = [dataLo; dataHi];
dataAll = dataAll(:, 11:end-10);
nRats = size(dataAll, 1);

for ii = 1:nPerms
    disp(ii)
    shuffleI = randperm(nRats); % shuffle indicies
    i1 = shuffleI(1:floor(nRats/2)); % first half goes to group 1
    i2 = shuffleI(floor(nRats/2)+1:end); % second half goes to group 2
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/published/rat_behavior; sed -n 1,141p BehavioralModel/WaitTimeModels/GenerateSynthData_Bayes_subopt_onlylambda_flat.m | grep -v "^ *%" | sed -n 1,90p; grep -n "twin3\|smoothfactor =" Figures/Figure3.m
```

```
function [WTOpt, WTMdl, BlkInf, RPE, Belief, Kappa, Prior] =...
    GenerateSynthData_Bayes_subopt_onlylambda_flat(params, ratTrial,...
    noise_arg, gen_arg, noise_params)

H0 = 1/40;

tau = ratTrial.tau;
C = max(1-ratTrial.prob_catch);

min_rew = min(ratTrial.reward); 

kappa_mi = params(1)*C*log2(min_rew)/tau;
kappa_hi = params(2)*C*log2(min_rew)/tau;
kappa_lo = params(3)*C*log2(min_rew)/tau;
D = params(4)*10;
lambda = params(5);

p_rew = nan(3, 5);
p_rew(1,:) = [1/5 1/5 1/5 1/5 1/5]; % mixed block
p_rew(2,:) = [0 0 1/3 1/3 1/3];
[... 89 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001169/10.1038-s41467-023-43250-x.yaml",
 "content": "# Claims for Mah, Schiereck, Bossio & Constantinople (2023) on dandiset 001169.\n# Source: the full text, open access (Nature Communications 14:7573; PMC10663503), read from its\n# Results, figure legends and Methods, and the paper's analysis code\n# (github.com/constantinoplelab/published, rat_behavior, commit b7b68ca).\n#\n# When these criteria were written, the author had seen the data check only: the file list and\n# metadata, the per-rat counts of sessions and trials (291 rats, median 71 sessions and 33,493\n# trials), the sex of each subject (184 M, 107 F), the reward volumes, block codes, training\n# stage and catch probabilities in the files, the duplicated session of rat L011, and that the\n# 16 rats of Figure 5 have sessions flagged with the task argument `center_port_cue`. The author\n# had also read one rat's struct in the Zenodo deposit to see its fields. No claim's analysis\n# had been run.\n#\n# Method choices fixed here. Where the Methods leave a choice open, the paper's code settles it;\n# where the Methods and the code disagree, the Methods give the main result and the code's\n# choice is shown as a variant. Per rat, as in the code: wait times are the files' thresholded\n# `wait_time` on catch trials the rat opted out of; trial initiation times are\n# `inter_trial_interval` with values above the rat's pooled 99th percentile removed; rewards of\n# female rats (4 to 64 uL) are treated as 5 to 80 uL; blocks are mixed, high and low; sessions\n# are in order of their start time and the duplicated L011 session is counted once.\n#\n# Tolerances. Counts of records the dandiset should hold exactly (rats, sessions, trials, sexes)\n# have tolerance 0, as they count the same records. The \"~10 percent\" of fig1f-wait-time-block\n# is given with 2.5 percentage points, as the text states it as an approximation. Other numbers\n# use 10% of the reported value. Reported p-values are not tolerances; the criteria name the\n# test and its threshold, and the notes compare the magnitudes.\nschema_version: 1\ndandiset: \"001169\"\npaper: doi:10.1038/s41467-023-43250-x\nclaims:\n- id: dataset-counts\n  statement: Data from 291 Long-Evans rats (184 male, 107 female), with a median of 71 sessions and\n    33,493 trials per rat.\n  source: Results, first section; Methods, Subjects\n  expected:\n  - quantity: rats\n    value: 291\n    tolerance: 0\n  - quantity: median sessions per rat\n    value: 71\n    tolerance: 0\n  - quantity: median trials per rat\n    value: 33493\n    tolerance: 0\n  - quantity: male rats\n    value: 184\n    tolerance: 0\n  - quantity: female rats\n    value: 107\n    tolerance: 0\n  criterion: Counted from the files, each session once. Reproduced when every count matches.\n    Partially reproduced when the rats match and a median differs by less than 10%. The paper\n    also gives 160 male and 114 female rats (Methods, Training for male and female rats); that\n    figure is reported against the data as well.\n- id: zenodo-link\n  statement: The dandiset holds the paper's processed per-rat data (A_Structs_Final in the Zenodo\n    deposit) for every rat, session and trial, with the same values.\n  source: Data availability; Zenodo 10.5281/zenodo.10031483\n  data: with_inputs\n  criterion: Rats are matched by identifier and sessions by their order and trial counts (the\n    structs keep session dates as MATLAB datetime objects that are not read here). Reproduced\n    when all 291 rats match in session count and per-session trial counts and the trial values\n    used here (reward, block, catch, violation, rewarded, opt-out, wait time, trial initiation\n    time) are equal for every trial, up to float rounding. Partially reproduced when at least\n    90% of rats match in full. The structs' catch probability is compared with the raw trials'\n    catch_percentage, which the analysis uses in its place.\n- id: fig1f-wait-time-block\n  statement: Rats waited about 10% less for 20 uL in high blocks than in low blocks (p = 8.26e-49,\n    two-tailed Wilcoxon signed-rank test, N = 291).\n  source: Results, first section; Figure 1d to 1f\n  expected:\n  - quantity: reduction of wait time for 20 uL, high against low blocks\n    value: 10\n    tolerance: 2.5\n    unit: percent\n  criterion: Per rat, the mean wait time on 20 uL catch trials in high and in low blocks. Two\n    readings of the reduction; (a) one minus the mean over rats of the ratio high/low (the\n    line in Figure 1f), (b) one minus the ratio of the population means. Reproduced when one\n    reading is within tolerance and a two-tailed signed-rank test across rats finds high below\n    low at p < 0.05, using per-rat means of z-scored wait times as the Methods state (the\n    code's test on raw means is a variant). Partially reproduced when the test holds and no\n    reading is within tolerance.\n- id: fig1i-initiation-block\n  statement: Rats initiated trials more quickly in high than in low blocks (p = 1.82e-49, two-tailed\n    Wilcoxon signed-rank test, N = 291).\n  source: Results, first section; Figure 1g to 1i\n  criterion: Per rat, the mean trial initiation time over all trials in high and in low blocks.\n    Reproduced when a two-tailed signed-rank test across rats on per-rat means of z-scored\n    times (Methods) finds high below low at p < 0.05. The code's test on raw means and the\n    mean ratio high/low are shown as variants.\n- id: figs2-unrewarded-drive\n  statement: Block sensitivity of trial initiation times is largely driven by initiation times that\n    follow unrewarded trials.\n  source: Results, first section; Supplementary Fig. 2; Methods\n  criterion: As FigureS2.m, per rat the mean z-scored initiation time in low minus high blocks,\n    separately for trials that follow a rewarded and an unrewarded trial. Reproduced when the\n    post-unrewarded difference is larger than the post-rewarded one by a two-sided signed-rank\n    test at p < 0.05, with a larger median.\n- id: figs12-no-sex-difference\n  statement: Male and female rats did not differ in their contextual effects (wait time and trial\n    initiation time ratios).\n  source: Methods, Training for male and female rats; Supplementary Fig. 12\n  criterion: A claim of absence, judged on the code's test (FigureS12.m), a two-sided Wilcoxon\n    rank-sum test of the per-rat wait time ratio (20 uL, high/low) and of the initiation time\n    ratio (high/low) between males and females. Reproduced when neither test has p < 0.05.\n- id: fig2a-wait-time-converges\n  statement: At transitions from high or low blocks into mixed blocks, wait times converge to a\n    common value regardless of the previous block.\n  source: Results, second section; Figure 2a\n  criterion: Per rat, the code's change in z-scored wait time around transitions (block_dynamics_wt,\n    20 trials either side, 10-point smoothing), for low-to-mixed minus high-to-mixed. The\n    difference before the switch is its mean over trials -20 to -6, after the switch its mean\n    over trials +11 to +20, each averaged over rats. Reproduced when the after/before ratio is\n    at most 0.25; partially reproduced when it is above 0.25 and at most 0.5; not reproduced\n    above 0.5.\n- id: fig2b-initiation-previous-block\n  statement: Trial initiation times in mixed blocks depend strongly on the previous block, unlike\n    wait times.\n  source: Results, second section; Figure 2b; Supplementary Fig. 4\n  criterion: The same measure with the code's initiation time dynamics (block_dynamics_latency,\n    detrended within sessions). Reproduced when the after/before ratio is at least 0.25 and the\n    per-rat after-switch difference is above zero by a two-sided signed-rank test at p < 0.05.\n    Partially reproduced when the test holds and the ratio is below 0.25.\n- id: fig2cd-regression-kernels\n  statement: Wait times are explained by the current reward, while trial initiation times reflect\n    an exponentially weighted effect of previous rewards.\n  source: Results, second section; Figure 2c and 2d\n  criterion: Regressions in mixed blocks as in the Methods; wait times of catch trials (z-scored)\n    on the current and 9 previous log2 rewards, initiation times (z-scored) on 9 previous log2\n    rewards with rewards of unrewarded trials set to 0, each with a constant. Reproduced when,\n    across rats, the wait time coefficient of the current reward is above zero and the\n    initiation time coefficient of the previous reward is below zero (two-sided signed-rank, p\n    < 0.05 each), the mean wait time coefficient one trial back is under a quarter of the\n    current one in magnitude, and the mean initiation time coefficients fall in magnitude from\n    1 to 3 to 6 trials back. Partially reproduced when the wait time or the initiation time\n    part holds, not both. The code's 10 previous rewards for initiation times are a variant.\n- id: fig2e-tau-differ\n  statement: The time constants of exponentials fit to the previous-reward coefficients differ\n    between trial initiation and wait times (p = 1.30e-49, two-tailed signed-rank test, N = 291).\n  source: Results, second section; Figure 2e\n  depends_on:\n  - fig2cd-regression-kernels\n  criterion: Per rat, the coefficients from the first one whose 95% CI contains 0 are set to 0\n    and an exponential is fit to the lags as in regress_*_vs_rew.m (tau 0 when all previous\n    coefficients are 0). Reproduced when the initiation time taus exceed the wait time taus by\n    a two-sided signed-rank test at p < 0.05, with a larger median.\n- id: fig2f-tau-uncorrelated\n  statement: The time constants of trial initiation and wait times are not correlated across rats\n    (Pearson; r = -0.03, p = 0.53 in the legend; r = 0.08, p = 0.18 in the text; N = 291).\n  source: Results, second section; Figure 2f\n  depends_on:\n  - fig2e-tau-differ\n  criterion: A claim of absence, judged on the paper's test, a Pearson correlation of the two taus\n    across rats. Reproduced when p >= 0.05; not reproduced when p < 0.05. The value of r is\n    given either way.\n- id: fig2gh-fast-slow-groups\n  statement: Rats with fast and slow trial initiation time constants (below the 20th or above the\n    80th percentile) differ in their initiation time coefficients (p = 0.02, one-tailed\n    permutation test, N = 116) but not in their wait time coefficients (p = 0.1).\n  source: Results, second section; Figure 2g and 2h\n  depends_on:\n  - fig2e-tau-differ\n  criterion: As myTauShuffleTest.m, the difference of taus fit to the two groups' mean coefficients\n    against 500 random splits of the same rats, with the code's p-value. Reproduced when the\n    initiation time p < 0.05 and the wait time p >= 0.05; partially reproduced when one of the\n    two holds. The group size is reported against N = 116.\n- id: fig2j-wait-time-previous-reward\n  statement: For most rats (253 of 291), wait times for 20 uL in mixed blocks did not differ with\n    the previous reward offer; 38 rats had p < 0.05, and the population p = 0.8.\n  source: Results, second section; Figure 2j\n  expected:\n  - quantity: rats with p < 0.05 (two-tailed rank-sum, previous offer below against above 20 uL)\n    value: 38\n    tolerance: 3.8\n  criterion: As waittime_20ul_by_previous_vol.m, z-scored wait times on 20 uL catch trials in mixed\n    blocks, split by the previous trial's offer. The population part is a claim of absence,\n    judged on the legend's test, a two-tailed Wilcoxon rank-sum test of the per-rat means (the\n    code's signed-rank test is a variant). Reproduced when the count is within tolerance and the\n    population test has p >= 0.05; partially reproduced when one of the two holds.\n- id: fig2k-initiation-previous-reward\n  statement: For 89% of rats (256 of 291) trial initiation times in mixed blocks were modulated by\n    the previous reward (p < 0.05 each); population p = 1.84e-49.\n  source: Results, second section; Figure 2k\n  expected:\n  - quantity: rats with p < 0.05 (two-tailed rank-sum, previous offer below against above 20 uL)\n    value: 256\n    tolerance: 25.6\n  criterion: Z-scored initiation times in mixed blocks split by the previous offer. The Methods use\n    trials offering 20 uL; the code uses all mixed-block trials (variant). Reproduced when the\n    count is within tolerance and the legend's population test (two-tailed rank-sum of per-rat\n    means) finds slower initiation after offers below 20 uL at p < 0.05; partially reproduced\n    when one of the two holds.\n- id: fig2l-sensitivity-differs\n  statement: Sensitivity to the previous offer is larger for trial initiation times than for wait\n    times (p = 6.21e-38, two-tailed signed-rank test, N = 291).\n  source: Results, second section; Figure 2l\n  depends_on:\n  - fig2j-wait-time-previous-reward\n  - fig2k-initiation-previous-reward\n  criterion: Sensitivity is the mean after offers below 20 uL minus the mean after offers above,\n    per rat, from the two claims above. Reproduced when the initiation time sensitivity exceeds\n    the wait time sensitivity by a two-sided signed-rank test at p < 0.05.\n- id: fig3c-catch-probability\n  statement: Wait times in mixed blocks depend in a graded way on the catch probability, as the\n    wait time model predicts; the cohorts held 3, 183, 61, 151 and 39 rats at catch probabilities\n    0.1, 0.15, 0.2, 0.25 and 0.35.\n  source: Results, third section; Figure 3c; Methods, Statistical analyses\n  expected:\n  - quantity: rats at catch probability 0.1\n    value: 3\n    tolerance: 0.3\n  - quantity: rats at catch probability 0.15\n    value: 183\n    tolerance: 18.3\n  - quantity: rats at catch probability 0.2\n    value: 61\n    tolerance: 6.1\n  - quantity: rats at catch probability 0.25\n    value: 151\n    tolerance: 15.1\n  - quantity: rats at catch probability 0.35\n    value: 39\n    tolerance: 3.9\n  criterion: As Figure3.m, catch trials in mixed blocks after each rat's first 1000 trials, mean\n    wait time per rat for each reward and catch probability, averaged over rats; a rat counts\n    for a probability when it has such trials. The model (Equation 1) predicts shorter waits at\n    higher catch probability. Reproduced when the counts are within tolerance and the mean over\n    rewards of the population wait times falls strictly from 0.15 to 0.2 to 0.25 to 0.35;\n    partially reproduced when one of the two holds. A second reading of the counts, rats with\n    any trial at that probability, is also shown.\n- id: fig3j-model-comparison\n  statement: Wait times are better fit by the inferential model, which uses hidden state inference,\n    than by the retrospective model (BIC, p = 1.07e-37, two-tailed signed-rank test, N = 291).\n  source: Results, third section; Figure 3j; Supplementary Fig. 8\n  criterion: Both models as in the generative code (GenerateSynthData_Bayes.m and\n    GenerateSynthData_AlphaPHModel.m), fit per rat by maximum likelihood to catch-trial wait\n    times in all blocks under log-normal noise of variance 8, with beliefs and the running\n    average updated over all non-violation trials. The inferential model is fit from 20 random\n    starts, the retrospective one on a grid of 40 baseline learning rates refined locally.\n    BIC = k log(n) + 2 nLL, with n the number of fitted trials. Reproduced when BIC is lower for\n    the inferential model by a two-sided signed-rank test at p < 0.05, with a positive median\n    difference (retrospective minus inferential).\n- id: figs9-misinference\n  statement: Wait times in mixed blocks reflect mistaken inferences; wait times for 20 uL are shorter\n    when the inferential model infers a high block than when it infers a low block (p << 0.001,\n    signed-rank test, N = 291).\n  source: Results, third section; Supplementary Fig. 9\n  criterion: The inferred block is the most probable block of the inferential model, which does not\n    depend on its fitted parameters. As FigureS9.m, per rat the mean wait time on 20 uL catch\n    trials in mixed blocks inferred as high and as low. Reproduced when inferred high is below\n    inferred low by a two-sided signed-rank test at p < 0.05.\n- id: fig3l-inference-quality\n  statement: Rats with good and poor inference (lambda above the 80th or below the 20th percentile)\n    differ in wait time dynamics at transitions from mixed into low or high blocks, but not in\n    trial initiation time dynamics.\n  source: Results, third section; Figure 3l (mixed to low slope p = 0.02, mixed to high right\n    asymptote p = 0.003; trial initiation p = 0.15 and 0.21)\n  depends_on:\n  - fig3j-model-comparison\n  criterion: Lambda fit per rat with the suboptimal-prior model (GenerateSynthData_Bayes_subopt_onlylambda_flat.m)\n    on a grid of 11 values from 0 to 1, the other parameters refit at each. Groups below the 20th\n    and above the 80th percentile (Methods and legend; the code's 40th and 60th are a variant).\n    Logistic fits to the group means of the code's transition dynamics (30 trials either side,\n    the central 41 trials fit) and 500 label shuffles, with the code's p-value (myLambdaShuffleTest.m).\n    Reproduced when, for wait times, the slope (mixed to low) or the right asymptote (mixed to\n    high) differs at p < 0.05 and, for initiation times, neither does; partially reproduced when\n    one of the two parts holds.\n- id: fig3h-dynamic-learning-rate\n  statement: A retrospective model of trial initiation times needs a learning rate scaled by changes\n    in the inferred block to capture both the slow and fast dynamics at block transitions; a\n    static or RPE-scaled learning rate does not.\n  source: Results, third section; Figure 3g to 3i; Supplementary Fig. 7\n- id: fig4a-wait-ratio-learning\n  statement: Over training in the final stage, the wait time ratio (20 uL, high/low) fell gradually\n    toward its final value, while the trial initiation time ratio was below 1 from the first\n    session.\n  source: Results, fourth section; Figure 4a\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.10031483 (A_Structs_all)\n  criterion: As macro_regress_overtraining_V2.m, the first 50 sessions per rat in pairs, ratios from\n    regress_trials_blocksv2.m (non-violation trials). Reproduced when the per-rat initiation time\n    ratio of the first pair is below 1 (two-sided signed-rank against 1, p < 0.05) and the wait\n    time ratio of the first pair is above its mean over pairs 16 to 25 (two-sided signed-rank, p <\n    0.05); partially reproduced when one of the two holds.\n- id: fig4bc-regression-learning\n  statement: Over training, the block and reward coefficients for wait times grew gradually, while\n    the previous-reward coefficient for trial initiation times was comparable early and late.\n  source: Results, fourth section; Figure 4b and 4c\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.10031483 (A_Structs_all)\n  criterion: Coefficients from regress_trials_blocksv2.m per session pair. Reproduced when the\n    magnitudes of the wait time block and reward coefficients are larger in pairs 16 to 25 than in\n    the first pair (two-sided signed-rank, p < 0.05 each), and the population mean of the initiation\n    time coefficient over the last 50 sessions is within a factor of 1.5 of its mean over the first\n    50; partially reproduced when the wait time part or the initiation time part holds, not both.\n- id: fig4de-overshoot-learning\n  statement: The overshoot of trial initiation times after high-to-mixed transitions grew with\n    training, on a timescale similar to the block sensitivity of wait times.\n  source: Results, fourth section; Figure 4d and 4e\n- id: fig5b-precue-offer\n  statement: With the reward cue played before trial initiation, trial initiation times became\n    sensitive to the offered reward.\n  source: Results, fifth section; Figure 5b\n  criterion: Sessions flagged with center_port_cue true. Per rat, the slope of z-scored initiation\n    time against log2 offer in mixed blocks. Reproduced when the slopes in cue sessions are below\n    zero (two-sided signed-rank, p < 0.05) and, for rats with sessions of the original task,\n    below their slopes there (post-violation trials excluded in the original task, as the\n    Methods state; two-sided signed-rank, p < 0.05). Partially reproduced when only the first part\n    holds.\n- id: fig5c-precue-previous-reward\n  statement: In the pre-initiation cue task, trial initiation times for 20 uL in mixed blocks were\n    still modulated by the previous reward (p < 0.05 for 13 of 16 rats; population p = 1.03e-4,\n    two-tailed rank-sum test).\n  source: Results, fifth section; Figure 5c\n  expected:\n  - quantity: rats with p < 0.05\n    value: 13\n    tolerance: 1.3\n  criterion: All cue sessions in the dandiset (the dandiset holds only sessions that passed the\n    inclusion criteria, so the paper's 30-session wait after the switch cannot be counted as it\n    did; dropping each switched rat's first 30 cue sessions here is a variant). Per rat, the\n    initiation times of trials offering 20 uL in mixed blocks split by the previous offer, as in\n    fig2k-initiation-previous-reward. Reproduced when the count is within tolerance and the\n    population rank-sum test finds slower initiation after offers below 20 uL at p < 0.05;\n    partially reproduced when one of the two holds.\n- id: fig5d-precue-previous-block\n  statement: In the pre-initiation cue task, trial initiation times in mixed blocks still depended on\n    the previous block.\n  source: Results, fifth section; Figure 5d\n  criterion: The measure of fig2b-initiation-previous-block on the cue sessions. Reproduced when the\n    after/before ratio is at least 0.25 and the per-rat after-switch difference is above zero by a\n    two-sided signed-rank test at p < 0.05; partially reproduced when the test holds and the ratio\n    is below 0.25.\n"
}
```

```
File created successfully at: claims/001169/10.1038-s41467-023-43250-x.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Claims are written (26, including 3 blocked or outside-data ones). Now implementing the measures in the helper module.

**Agent calls Bash**

```bash
cat >> entries/001169-mah-2023/wagering.py <<'EOF'


def drop_duplicate_sessions(sessions: pd.DataFrame, trials: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Remove sessions that repeat an earlier session of the same rat trial for trial (same trial
    count, rewards, blocks and trial initiation times). Returns the kept sessions, their
    trials (sessions renumbered) and the removed sessions."""
    g = trials.groupby("session", sort=True)
    fingerprint = pd.DataFrame({
        "n": g.size(),
        "rewards": g.reward_volume_ul.apply(lambda s: hash(s.to_numpy().tobytes())),
        "blocks": g.block_type.apply(lambda s: hash(s.to_numpy().tobytes())),
        "iti": g.inter_trial_interval.apply(lambda s: hash(np.nan_to_num(s.to_numpy(), nan=-1).tobytes())),
    })
    fingerprint["subject_id"] = sessions.subject_id.to_numpy()
    duplicated = fingerprint.duplicated(keep="first").to_numpy()
    removed = sessions[duplicated]
    keep = np.flatnonzero(~duplicated)
    new_index = np.full(len(sessions), -1)
    new_index[keep] = np.arange(len(keep))
    trials = trials[~duplicated[trials.session.to_numpy()]].copy()
    trials["session"] = new_index[trials.session.to_numpy()].astype(np.int32)
    return sessions.iloc[keep].reset_index(drop=True), trials.reset_index(drop=True), removed


# ----------------------------------------------------------------------------------------
# Per-rat arrays
# ----------------------------------------------------------------------------------------

def rat_arrays(trials: pd.DataFrame, sessions: pd.DataFrame) -> dict[str, dict]:
    """For each rat, its trials in order as numpy arrays (the fields of the paper's A struct)."""
    cue = sessions.center_port_cue.eq("True").to_numpy()
    out = {}
    for rat, t in trials.groupby("rat", observed=True, sort=True):
        session = t.session.to_numpy()
        _, sess_local = np.unique(session, return_inverse=True)
        out[rat] = {
            "session": sess_local,
            "trial": t.trial.to_numpy(),
            "reward": t.reward.to_numpy().astype(float),            # 5 to 80 uL
            "volume": t.reward_volume_ul.to_numpy().astype(float),  # as offered (4 to 80 uL)
            "block": t.block_type.to_numpy().astype(int),
            "catch": t.is_catch.to_numpy(),
            "vios": t.is_violation.to_numpy(),
            "hits": t.is_rewarded.to_numpy(),
            "optout": t.is_opt_out.to_numpy(),
            "wait_time": t.wait_time.to_numpy().astype(float),
            "iti": t.inter_trial_interval.to_numpy().astype(float),
            "prob_catch": np.round(t.catch_percentage.to_numpy().astype(float), 3),
            "cue": cue[session],
        }
    return out


def subset(A: dict, mask: np.ndarray) -> dict:
    """The trials of a rat selected by a boolean mask, sessions renumbered."""
    B = {k: v[mask] for k, v in A.items()}
    _, B["session"] = np.unique(B["session"], return_inverse=True)
    return B


def clean_iti(iti: np.ndarray) -> np.ndarray:
    """Trial initiation times with values above the 99th percentile set to NaN (Methods)."""
    out = iti.copy()
    out[out > np.nanpercentile(out, 99)] = np.nan
    return out


def zscore(x: np.ndarray) -> np.ndarray:
    return (x - np.nanmean(x)) / np.nanstd(x, ddof=1)


def ranksum(x, y, alternative="two-sided") -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    x, y = x[~np.isnan(x)], y[~np.isnan(y)]
    if len(x) == 0 or len(y) == 0:
        return np.nan
    return stats.mannwhitneyu(x, y, alternative=alternative).pvalue


def signrank(x, y=None) -> float:
    x = np.asarray(x, float)
    d = x if y is None else x - np.asarray(y, float)
    d = d[~np.isnan(d)]
    return stats.wilcoxon(d).pvalue


def matlab_smooth(y: np.ndarray, span: int = 5) -> np.ndarray:
    """Moving average as MATLAB's smooth(y, span): an even span is reduced by one and the
    window shrinks symmetrically at the ends. NaNs are left out of each window's mean."""
    y = np.asarray(y, float)
    if span % 2 == 0:
        span -= 1
    half = span // 2
    n = len(y)
    out = np.full(n, np.nan)
    for i in range(n):
        h = min(half, i, n - 1 - i)
        w = y[i - h:i + h + 1]
        if np.any(~np.isnan(w)):
            out[i] = np.nanmean(w)
    return out


# ----------------------------------------------------------------------------------------
# Figure 1: block sensitivity
# ----------------------------------------------------------------------------------------

def wait_curves(A: dict) -> dict:
    """Mean wait time per block and reward on catch trials the rat opted out of (wtcurves.m),
    the same on wait times z-scored over all catch trials (Methods), and the one-tailed
    rank-sum p of 20 uL high < low."""
    use = A["optout"] & A["catch"]
    z = np.full(len(use), np.nan)
    z[A["catch"]] = zscore(A["wait_time"][A["catch"]])
    out = {}
    for b in (1, 2, 3):
        for r in STANDARD_VOLUMES:
            sel = use & (A["block"] == b) & (A["reward"] == r)
            out[(b, r)] = np.nanmean(A["wait_time"][sel]) if sel.any() else np.nan
            out[("z", b, r)] = np.nanmean(z[sel]) if sel.any() else np.nan
    wt = A["wait_time"]
    out["p"] = ranksum(wt[use & (A["block"] == 2) & (A["reward"] == 20)],
                       wt[use & (A["block"] == 3) & (A["reward"] == 20)], "less")
    return out


def initiation_by_block(A: dict) -> dict:
    """Mean trial initiation time per block, raw and z-scored, over all trials (iticurves.m),
    and the one-tailed rank-sum p of high < low."""
    L = clean_iti(A["iti"])
    z = zscore(L)
    out = {}
    for b in (1, 2, 3):
        out[b] = np.nanmean(L[A["block"] == b])
        out[("z", b)] = np.nanmean(z[A["block"] == b])
    out["p"] = ranksum(L[A["block"] == 2], L[A["block"] == 3], "less")
    return out


def initiation_by_previous_outcome(A: dict) -> dict:
    """FigureS2.m: z-scored initiation time in low and high blocks after rewarded and after
    unrewarded trials (the previous trial in the rat's sequence)."""
    L = clean_iti(A["iti"])
    z = zscore(L)
    prev_hit = np.r_[False, A["hits"][:-1]]
    prev_unrew = np.r_[False, ~A["hits"][:-1]]
    out = {}
    for name, m in (("rewarded", prev_hit), ("unrewarded", prev_unrew)):
        sel = m & ~np.isnan(L)
        out[name] = (np.nanmean(z[sel & (A["block"] == 3)]), np.nanmean(z[sel & (A["block"] == 2)]))
    return out


# ----------------------------------------------------------------------------------------
# Figure 2: previous-offer sensitivity, transitions, regressions
# ----------------------------------------------------------------------------------------

def wait_by_previous_offer(A: dict) -> tuple[float, float, float]:
    """waittime_20ul_by_previous_vol.m: z-scored wait times on 20 uL catch trials in mixed
    blocks (opted out), after offers below and above 20 uL, and the two-tailed rank-sum p."""
    idx = np.flatnonzero((A["reward"] == 20) & (A["block"] == 1) & A["optout"] & A["catch"])
    idx = idx[idx > 0]
    wt = A["wait_time"]
    z = (wt - np.nanmean(wt[idx])) / np.nanstd(wt[idx], ddof=1)
    prev = A["reward"][idx - 1]
    lo, hi = z[idx[prev < 20]], z[idx[prev > 20]]
    return np.nanmean(lo), np.nanmean(hi), ranksum(lo, hi)


def initiation_by_previous_offer(A: dict, only_20ul: bool = True) -> tuple[float, float, float]:
    """latency_post20ul_by_previous_vol.m: z-scored initiation times in mixed blocks after
    offers below and above 20 uL, and the two-tailed rank-sum p. With only_20ul, trials
    offering 20 uL only (Methods); without, all mixed-block trials (the code)."""
    L = clean_iti(A["iti"])
    z = zscore(L)
    prev = np.r_[np.nan, A["reward"][:-1]]
    base = A["block"] == 1
    if only_20ul:
        base = base & (A["reward"] == 20)
    lo, hi = z[base & (prev < 20)], z[base & (prev > 20)]
    return np.nanmean(lo), np.nanmean(hi), ranksum(lo, hi)


def _transitions(A: dict) -> dict[int, np.ndarray]:
    """Global indices of the first trial of each new block, by kind (blockhmat_withvios.m):
    +1 mixed to high, +2 mixed to low, -1 high to mixed, -2 low to mixed. Transitions in the
    first 40 trials of a session are ignored, as in the code."""
    block, session, trial = A["block"], A["session"], A["trial"]
    d = np.r_[0, np.diff(block)]
    d[np.r_[True, session[1:] != session[:-1]]] = 0
    within = np.zeros(len(block), int)
    starts = np.flatnonzero(np.r_[True, session[1:] != session[:-1]])
    for s, e in zip(starts, np.r_[starts[1:], len(block)]):
        within[s:e] = np.arange(e - s)
    d[within < 40] = 0
    return {k: np.flatnonzero(d == k) for k in (1, 2, -1, -2)}


def wait_dynamics(A: dict, twin: int = 20, smoothfactor: int = 10) -> dict[int, np.ndarray]:
    """block_dynamics_wt.m: change in z-scored wait time on catch trials around transitions,
    relative to the mean for each reward; windows on the rat's pooled trial sequence."""
    wt = A["wait_time"].copy()
    c = A["catch"]
    wt[c] = zscore(wt[c])
    good = c & ~A["vios"]
    for r in STANDARD_VOLUMES:
        m = good & (A["reward"] == r)
        if m.sum() > 1:
            wt[m] = zscore(wt[m])
    n = len(wt)
    out = {}
    for kind, idx in _transitions(A).items():
        rows = np.full((max(len(idx), 1), 2 * twin + 1), np.nan)
        for j, t in enumerate(idx):
            these = np.arange(t - twin, t + twin + 1)
            ok = (these >= 0) & (these < n)
            ok[ok] &= good[these[ok]]
            rows[j, ok] = wt[these[ok]]
        mean = np.nanmean(rows, axis=0) if len(idx) else np.full(2 * twin + 1, np.nan)
        mean[twin] = mean[twin - 2]
        out[kind] = matlab_smooth(mean, smoothfactor)
    return out


def initiation_dynamics(A: dict, twin: int = 20, smoothfactor: int = 10, detrend: bool = True) -> dict[int, np.ndarray]:
    """block_dynamics_latency.m: z-scored initiation time around transitions, within sessions,
    after subtracting a linear fit on trial number pooled over sessions (satiety detrend)."""
    l = A["iti"].copy()
    session, trial = A["session"], A["trial"]
    l[np.r_[True, session[1:] != session[:-1]]] = np.nan
    l[l > np.nanpercentile(l, 99)] = np.nan
    z = zscore(l)
    n_sess = session.max() + 1
    lengths = np.bincount(session, minlength=n_sess)
    width = lengths.max()
    mat = np.full((n_sess, width), np.nan)
    within = np.zeros(len(l), int)
    starts = np.r_[0, np.cumsum(lengths)[:-1]]
    within = np.arange(len(l)) - starts[session]
    mat[session, within] = z
    x = np.tile(np.arange(1, width + 1), n_sess)
    s = mat.ravel()
    ok = ~np.isnan(s)
    if detrend:
        b = np.polyfit(x[ok], s[ok], 1)
        regline = b[0] * np.arange(1, width + 1) + b[1]
    else:
        regline = np.zeros(width)
    out = {}
    for kind, idx in _transitions(A).items():
        rows = []
        for t in idx:
            ss, w = session[t], within[t]
            these = np.arange(w - twin, w + twin + 1)
            ok = (these >= 0) & (these < width)
            row = np.full(2 * twin + 1, np.nan)
            row[ok] = mat[ss, these[ok]] - regline[these[ok]]
            rows.append(row)
        mean = np.nanmean(rows, axis=0) if rows else np.full(2 * twin + 1, np.nan)
        if kind == 2:
            mean[twin] = mean[twin - 2]
        else:
            mean[twin] = mean[twin - 1]
        mean[twin - 1] = np.nan
        out[kind] = matlab_smooth(mean, smoothfactor)
    return out


def ols(y: np.ndarray, X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Least squares as MATLAB's regress: rows with any NaN dropped; coefficients and their
    95% confidence intervals."""
    ok = ~np.isnan(y) & ~np.isnan(X).any(axis=1)
    y, X = y[ok], X[ok]
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    dof = len(y) - X.shape[1]
    resid = y - X @ b
    s2 = resid @ resid / dof
    cov = s2 * np.linalg.pinv(X.T @ X)
    half = stats.t.ppf(0.975, dof) * np.sqrt(np.diag(cov))
    return b, np.c_[b - half, b + half]


def fit_exp_decay(x, y, rng, iters=10, lower=(-50, -50), upper=(50, 50)) -> np.ndarray:
    """fit_exp_decay.m: y = a exp(-x / tau) by least squares from random starts within the
    bounds; returns (a, tau) of the best start."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    lower, upper = np.asarray(lower, float), np.asarray(upper, float)

    def mse(p):
        with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
            r = y - p[0] * np.exp(-x / p[1])
        return np.nanmean(r ** 2) if np.all(np.isfinite(r[~np.isnan(y)])) else 1e12

    best, best_val = None, np.inf
    upper_eff = upper.copy()
    lower_eff = np.maximum(lower, [lower[0], 1e-6])
    for _ in range(iters):
        p0 = rng.random(2) * (upper - lower) + lower
        p0 = np.clip(p0, lower_eff, upper_eff)
        res = optimize.minimize(mse, p0, method="L-BFGS-B", bounds=list(zip(lower_eff, upper_eff)))
        if res.fun < best_val:
            best, best_val = res.x, res.fun
    return best


def regress_wait_on_rewards(A: dict, nback: int, rng) -> tuple[np.ndarray, float]:
    """regress_wt_vs_rew.m: z-scored wait times on mixed-block catch trials (opted out)
    regressed on the current and nback-1 previous log2 offers (rewards outside mixed blocks
    NaN, the first trials padded with 0, as the code), with a constant. Coefficients from the
    first one whose 95% CI contains 0 are set to 0; tau from an exponential fit."""
    use = A["optout"] & A["catch"] & (A["block"] == 1)
    WT = np.full(len(use), np.nan)
    WT[use] = zscore(A["wait_time"][use])
    R = np.log2(A["volume"])
    R[A["block"] != 1] = np.nan
    X = np.full((len(R), nback + 1), np.nan)
    for j in range(nback):
        X[:, j] = np.r_[np.zeros(j), R[:len(R) - j]]
    X[:, -1] = 1.0
    b, ci = ols(WT[use], X[use])
    nonsig = np.flatnonzero((ci[:, 0] < 0) & (ci[:, 1] > 0))
    if len(nonsig):
        b[nonsig[0]:-1] = 0
    fit = fit_exp_decay(np.arange(1, nback + 1), 10 * b[:nback], rng, 10, (-10, 0), (10, 10))
    tau = 0.0 if np.all(b[1:-1] == 0) else fit[1]
    return b, tau


def regress_initiation_on_rewards(A: dict, nback: int, rng) -> tuple[np.ndarray, float]:
    """regress_latency_vs_rew.m: z-scored initiation times in mixed blocks regressed on the
    nback previous log2 rewards received (0 after unrewarded trials; NaN outside mixed blocks
    and before the first trial), with a constant; zeroing and tau as for wait times."""
    use = A["block"] == 1
    L = A["iti"][use].copy()
    L[L > np.nanpercentile(L, 99)] = np.nan
    L = zscore(L)
    R = np.log2(A["volume"]) * A["hits"]
    R[A["block"] != 1] = np.nan
    X = np.full((len(R), nback + 1), np.nan)
    for j in range(1, nback + 1):
        X[:, j - 1] = np.r_[np.full(j, np.nan), R[:len(R) - j]]
    X[:, -1] = 1.0
    b, ci = ols(L, X[use])
    nonsig = np.flatnonzero((ci[:, 0] < 0) & (ci[:, 1] > 0))
    if len(nonsig):
        b[nonsig[0]:-1] = 0
    fit = fit_exp_decay(np.arange(1, nback + 1), b[:nback], rng, 10, (-10, 0), (0, 10))
    tau = 0.0 if np.all(b[1:-1] == 0) else fit[1]
    return b, tau


def tau_shuffle_test(first: np.ndarray, last: np.ndarray, betas: np.ndarray, n_shuffle: int, rng,
                     consistent: bool = False) -> tuple[float, float]:
    """myTauShuffleTest.m: tau of an exponential fit to the mean coefficients (without the
    constant) of the two groups, against random halves of the same rats; p as the code
    computes it, the count of |shuffled difference| > |observed| over 2 * n_shuffle. The code
    fits the shuffled groups to 10 x coefficients with bounds (-3, 0) to (1, 50) and the
    observed groups to the coefficients with bounds (-10, 0) to (1, 10); with consistent=True
    the observed groups are fit as the shuffled ones."""
    B = betas[first | last][:, :-1]
    x = np.arange(1, B.shape[1] + 1)
    n = len(B)
    shuffled = np.empty(n_shuffle)
    for i in range(n_shuffle):
        perm = rng.permutation(n)
        g1, g2 = perm[: n // 2], perm[n // 2:]
        t1 = fit_exp_decay(x, 10 * B[g1].mean(0), rng, 10, (-3, 0), (1, 50))[1]
        t2 = fit_exp_decay(x, 10 * B[g2].mean(0), rng, 10, (-3, 0), (1, 50))[1]
        shuffled[i] = t1 - t2
    if consistent:
        t1 = fit_exp_decay(x, 10 * betas[first][:, :-1].mean(0), rng, 10, (-3, 0), (1, 50))[1]
        t2 = fit_exp_decay(x, 10 * betas[last][:, :-1].mean(0), rng, 10, (-3, 0), (1, 50))[1]
    else:
        t1 = fit_exp_decay(x, betas[first][:, :-1].mean(0), rng, 10, (-10, 0), (1, 10))[1]
        t2 = fit_exp_decay(x, betas[last][:, :-1].mean(0), rng, 10, (-10, 0), (1, 10))[1]
    observed = t1 - t2
    return observed, np.sum(np.abs(shuffled) > abs(observed)) / (2 * n_shuffle)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> entries/001169-mah-2023/wagering.py <<'EOF'


# ----------------------------------------------------------------------------------------
# Figure 3: wait time models
# ----------------------------------------------------------------------------------------

H0 = 1 / 40
DELAY_TAU = 2.5
NOISE_VARIANCE = 8.0
P_REWARD = np.array([[1 / 5] * 5, [0, 0, 1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3, 0, 0]])
P_BLOCK = np.array([[1 - H0, H0, H0], [H0 / 2, 1 - H0, 0], [H0 / 2, 0, 1 - H0]])
REWARD_INDEX = {5: 0, 10: 1, 20: 2, 40: 3, 80: 4}


def model_inputs(A: dict) -> dict:
    """What the wait time models use: the non-violation trials in order (beliefs and the
    running average are updated over these), the session starts among them, the offered
    volumes, and the catch trials the rat opted out of with a wait time (fitted)."""
    good = ~A["vios"]
    session = A["session"][good]
    starts = np.r_[True, session[1:] != session[:-1]]
    volume = A["volume"][good]
    fitted = (A["catch"] & A["optout"] & ~np.isnan(A["wait_time"]))[good]
    return {
        "good": good,
        "rew_idx": np.array([REWARD_INDEX[r] for r in A["reward"][good].astype(int)]),
        "R": np.log2(volume),
        "starts": starts,
        "fitted": fitted,
        "wt": A["wait_time"][good],
        "C": np.max(1 - A["prob_catch"]),
        "min_R": np.log2(volume.min()),
        "n_trials": len(A["reward"]),
    }


def beliefs(M: dict, lam: np.ndarray | None = None) -> np.ndarray:
    """Posterior over (mixed, high, low) on each trial. With lam None, the optimal model of
    GenerateSynthData_Bayes.m (belief reset to [1/2, 1/4, 1/4] at a session start); with a
    vector of lambdas, the suboptimal-prior model of
    GenerateSynthData_Bayes_subopt_onlylambda_flat.m for each (reset to [1/3, 1/3, 1/3]);
    returns (n_lambda, n_trials, 3) then."""
    lik = P_REWARD[:, M["rew_idx"]].T
    n = len(lik)
    if lam is None:
        out = np.empty((n, 3))
        b = np.array([0.5, 0.25, 0.25])
        for t in range(n):
            if M["starts"][t]:
                b = np.array([0.5, 0.25, 0.25])
            else:
                b = lik[t] * (P_BLOCK @ b)
                b = b / b.sum()
            out[t] = b
        return out
    lam = np.asarray(lam, float)[:, None]
    out = np.empty((len(lam), n, 3))
    flat = np.full(3, 1 / 3)
    b = np.tile(flat, (len(lam), 1))
    for t in range(n):
        if M["starts"][t]:
            b = np.tile(flat, (len(lam), 1))
        else:
            prior = lam * (b @ P_BLOCK.T) + (1 - lam) * flat
            b = lik[t] * prior
            b = b / b.sum(axis=1, keepdims=True)
        out[:, t] = b
    return out


def lognormal_nll(wt_obs: np.ndarray, wt_pred: np.ndarray) -> float:
    """Negative log likelihood of observed wait times under log-normal noise with mean wt_pred
    and variance NOISE_VARIANCE (generate_wts.m)."""
    pred = np.clip(wt_pred, 1e-3, None)
    s2 = np.log(NOISE_VARIANCE / pred ** 2 + 1)
    mu = np.log(pred) - s2 / 2
    x = wt_obs
    ll = -np.log(x) - 0.5 * np.log(2 * np.pi * s2) - (np.log(x) - mu) ** 2 / (2 * s2)
    return -np.sum(ll)


def _wait_from_kappa(R, kappa, C, D):
    with np.errstate(divide="ignore", invalid="ignore"):
        arg = (R - kappa * DELAY_TAU) / (kappa * DELAY_TAU) * C / (1 - C)
        wt = D * DELAY_TAU * np.log(arg)
    return np.where(np.isfinite(wt), wt, 1e-3)


def inferential_nll(params, M, inferred) -> float:
    """GenerateSynthData_Bayes.m: kappa of the most probable block; params in [0, 1] are
    (kappa mixed, kappa high, kappa low, D/10)."""
    f = M["fitted"]
    scale = M["C"] * M["min_R"] / DELAY_TAU
    kappa = np.asarray(params[:3])[inferred[f]] * scale
    wt = _wait_from_kappa(M["R"][f], kappa, M["C"], 10 * params[3])
    return lognormal_nll(M["wt"][f], wt)


def fit_inferential(M: dict, inferred: np.ndarray, rng, starts: int = 20, x0=None) -> tuple[np.ndarray, float]:
    bounds = [(1e-4, 1)] * 4
    best, best_val = None, np.inf
    inits = [np.asarray(x0)] if x0 is not None else []
    inits += [rng.random(4) for _ in range(starts)]
    for p0 in inits:
        res = optimize.minimize(inferential_nll, np.clip(p0, 1e-4, 1), args=(M, inferred),
                                method="L-BFGS-B", bounds=bounds)
        if res.fun < best_val:
            best, best_val = res.x, res.fun
    return best, best_val


def retrospective_kappa(M: dict, alphas: np.ndarray, belief_mixed: np.ndarray) -> np.ndarray:
    """GenerateSynthData_AlphaPHModel.m: running average of log2 offers with the learning rate
    alpha0 / (1 - |change in P(mixed)|), capped at 1, reset at session starts; then scaled as
    the code does. Returns (n_alpha, n_trials)."""
    alphas = np.asarray(alphas, float)
    R = M["R"]
    n = len(R)
    k0 = np.mean(np.log([5, 10, 20, 40, 80]))
    kappa = np.empty((len(alphas), n))
    kappa[:, 0] = k0
    k = np.full(len(alphas), k0)
    for t in range(n - 1):
        if M["starts"][t]:
            k = np.full(len(alphas), k0)
            a = alphas
        else:
            a = np.minimum(alphas / (1 - abs(belief_mixed[t] - belief_mixed[t - 1])), 1)
        kappa[:, t] = k
        k = k + a * (R[t] - k)
    kappa[:, n - 1] = k
    kappa = kappa / kappa.max(axis=1, keepdims=True) * (R.min() * M["C"] / DELAY_TAU)
    kappa[kappa < 0] = np.finfo(float).eps
    return kappa


def fit_retrospective(M: dict, belief_mixed: np.ndarray, alphas: np.ndarray) -> tuple[np.ndarray, float]:
    """Grid over the baseline learning rate; D/15 in [0, 1] fit at each by bounded search."""
    f = M["fitted"]
    kappas = retrospective_kappa(M, alphas, belief_mixed)[:, f]
    R, wt_obs = M["R"][f], M["wt"][f]
    best, best_val = None, np.inf
    for a, kap in zip(alphas, kappas):
        def nll(d):
            wt = _wait_from_kappa(R, kap, M["C"], 15 * d)
            return lognormal_nll(wt_obs, np.where(wt < 0, np.finfo(float).eps, wt))
        res = optimize.minimize_scalar(nll, bounds=(1e-4, 1), method="bounded")
        if res.fun < best_val:
            best, best_val = np.array([a, res.x]), res.fun
    return best, best_val


def sigmoid(x, p):
    return p[3] + (p[0] - p[3]) / (1 + np.exp(-p[1] * (x - p[2])))


def fit_sigmoid(x, y, rng, iters: int = 10) -> np.ndarray:
    """my_fit_sigmoid.m: (right asymptote, slope, midpoint, left asymptote) by least squares
    from random starts within bounds (-5, 0, 0, -5) to (5, 5, 30, 5)."""
    lb, ub = np.array([-5, 0, 0, -5.0]), np.array([5, 5, 30, 5.0])
    best, best_val = None, np.inf
    for _ in range(iters):
        p0 = rng.random(4) * (ub - lb) + lb
        res = optimize.minimize(lambda p: np.sum((y - sigmoid(x, p)) ** 2), p0, method="L-BFGS-B",
                                bounds=list(zip(lb, ub)))
        if res.fun < best_val:
            best, best_val = res.x, res.fun
    return best


def lambda_shuffle_test(lo: np.ndarray, hi: np.ndarray, n_perm: int, twin: int, rng) -> tuple[np.ndarray, np.ndarray]:
    """myLambdaShuffleTest.m: sigmoid parameters of the two groups' mean curves (central
    2 * (twin - 10) + 1 trials) against random halves; returns the observed difference (high
    minus low lambda) and the code's p per parameter."""
    xs = np.arange(-(twin - 10), twin - 10 + 1)
    allr = np.vstack([lo, hi])[:, 10:-10]
    n = len(allr)
    diffs = np.empty((n_perm, 4))
    for i in range(n_perm):
        perm = rng.permutation(n)
        g1 = np.nanmean(allr[perm[: n // 2]], axis=0)
        g2 = np.nanmean(allr[perm[n // 2:]], axis=0)
        diffs[i] = fit_sigmoid(xs, g1, rng) - fit_sigmoid(xs, g2, rng)
    true = fit_sigmoid(xs, np.nanmean(hi[:, 10:-10], axis=0), rng) - fit_sigmoid(xs, np.nanmean(lo[:, 10:-10], axis=0), rng)
    p = np.sum(np.abs(diffs) > np.abs(true), axis=0) / (2 * n_perm)
    return true, p


# ----------------------------------------------------------------------------------------
# The paper's processed data on Zenodo (outside input)
# ----------------------------------------------------------------------------------------

ZENODO_URL = "https://zenodo.org/records/10031483/files/published.zip?download=1"
STRUCT_FIELDS = ["reward", "block", "catch", "vios", "hits", "optout", "wait_time", "ITI",
                 "prob_catch", "ntrials", "wait_thresh"]


def load_zenodo_structs(folder: str, max_workers: int = 8) -> dict[str, dict]:
    """The per-rat structs in `published/<folder>/` of Zenodo 10.5281/zenodo.10031483, read
    from the zip archive with range requests, held in memory."""
    import scipy.io as sio
    from remotezip import RemoteZip

    with RemoteZip(ZENODO_URL) as z:
        names = [i.filename for i in z.infolist()
                 if i.filename.startswith(f"published/{folder}/ratTrial_") and i.filename.endswith(".mat")]
    local = threading.local()

    def read(name):
        if not hasattr(local, "zip"):
            local.zip = RemoteZip(ZENODO_URL)
        A = sio.loadmat(io.BytesIO(local.zip.read(name)), simplify_cells=True)["A"]
        return name.split("ratTrial_")[1][:-4], {k: np.asarray(A[k]) for k in STRUCT_FIELDS if k in A}

    with ThreadPoolExecutor(max_workers) as pool:
        return dict(pool.map(read, sorted(names)))
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/001169-mah-2023; PY=$TMPDIR/scratch/bin/python; cat > $TMPDIR/prep.py <<'EOF'
import pandas as pd, numpy as np, os, pickle, time
import wagering as w
d=os.environ['TMPDIR']
S=pd.read_parquet(f'{d}/sessions.parquet'); T=pd.read_parquet(f'{d}/trials.parquet')
S2,T2,removed=w.drop_duplicate_sessions(S,T)
print('removed', removed[['subject_id','session_id']].to_string())
t=time.time(); rats=w.rat_arrays(T2,S2); print('rat arrays', time.time()-t)
pickle.dump((S2,rats),open(f'{d}/rats.pkl','wb'))
EOF
$PY $TMPDIR/prep.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/prep.py", line 2, in <module>
    import wagering as w
ModuleNotFoundError: No module named 'wagering'
```

**Agent calls Bash**

```bash
cd entries/001169-mah-2023 && PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/prep.py
```

```
removed       subject_id                    session_id
13781       L011  RWTautowait2-20221004-095612
rat arrays 0.6468408107757568
```

**Agent calls Bash**

```bash
sed -i 's/order = sessions.sort_values(\["subject_id", "start"\]).index.to_numpy()/order = sessions.sort_values(["subject_id", "start", "session_id"]).index.to_numpy()/' wagering.py && grep -n 'sort_values(\["subject_id"' wagering.py && cat > $TMPDIR/t1.py <<'EOF'
import pandas as pd, numpy as np, os, pickle, time
import wagering as w
from scipy import stats
d=os.environ['TMPDIR']
S,rats=pickle.load(open(f'{d}/rats.pkl','rb'))
names=sorted(rats)
t=time.time()
wc={r:w.wait_curves(rats[r]) for r in names}; print('wc',time.time()-t)
ic={r:w.initiation_by_block(rats[r]) for r in names}; print('ic',time.time()-t)
hi=np.array([wc[r][(2,20)] for r in names]); lo=np.array([wc[r][(3,20)] for r in names])
print('ratio mean', np.nanmean(hi/lo), 'pop', np.nanmean(hi)/np.nanmean(lo), stats.wilcoxon(hi,lo).pvalue)
zh=np.array([wc[r][('z',2,20)] for r in names]); zl=np.array([wc[r][('z',3,20)] for r in names]); print('z p', stats.wilcoxon(zh,zl).pvalue, np.mean(zh<zl))
ih=np.array([ic[r][2] for r in names]); il=np.array([ic[r][3] for r in names]); print('iti ratio', np.mean(ih/il), stats.wilcoxon(ih,il).pvalue, stats.wilcoxon([ic[r][('z',2)] for r in names],[ic[r][('z',3)] for r in names]).pvalue)
t=time.time()
wd={r:w.wait_dynamics(rats[r]) for r in names}; print('wd',time.time()-t)
idn={r:w.initiation_dynamics(rats[r]) for r in names}; print('id',time.time()-t)
for nm,dd in (('wt',wd),('iti',idn)):
    diff=np.array([dd[r][-2]-dd[r][-1] for r in names])
    m=np.nanmean(diff,0); pre=np.nanmean(m[0:15]); post=np.nanmean(m[31:41]); print(nm, pre, post, post/pre, stats.wilcoxon(np.nanmean(diff[:,31:41],1)).pvalue)
    print(np.round(m,3))
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t1.py
```

```
132:    order = sessions.sort_values(["subject_id", "start", "session_id"]).index.to_numpy()
entries/001169-mah-2023/wagering.py:367: RuntimeWarning: Mean of empty slice
  mean = np.nanmean(rows, axis=0) if len(idx) else np.full(2 * twin + 1, np.nan)
wc 0.713141918182373
ic 1.8175687789916992
ratio mean 0.8942493605440434 pop 0.8920534896343852 8.178177273922927e-47
z p 4.608483388378442e-47 0.9587628865979382
iti ratio 0.5617046612520491 1.8425951011266964e-49 1.823645343849845e-49
wd 2.8803558349609375
id 6.562686204910278
wt 0.3302483273301978 0.022019271946059536 0.06667489317529118 0.248201707039435
[ 0.375  0.329  0.327  0.32   0.326  0.32   0.318  0.321  0.323  0.324
  0.333  0.339  0.328  0.334  0.337  0.34   0.341  0.345  0.35   0.337
  0.319  0.309  0.293  0.266  0.242  0.213  0.18   0.145  0.119  0.099
  0.078  0.058  0.048  0.039  0.031  0.019  0.013  0.012  0.004 -0.003
 -0.001]
iti 0.12073805264787771 -0.25562381534488887 -2.1171768944327276 1.823645343849845e-49
[ 0.151  0.142  0.13   0.128  0.125  0.122  0.121  0.116  0.115  0.114
  0.113  0.111  0.111  0.108  0.105  0.103  0.103  0.077  0.041 -0.002
 -0.051 -0.105 -0.154 -0.205 -0.217 -0.26  -0.278 -0.288 -0.291 -0.291
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t2.py <<'EOF'
import pandas as pd, numpy as np, os, pickle, time
import wagering as w
from scipy import stats
d=os.environ['TMPDIR']
S,rats=pickle.load(open(f'{d}/rats.pkl','rb'))
names=sorted(rats)
rng=np.random.default_rng(1)
t=time.time()
W=[w.regress_wait_on_rewards(rats[r],10,rng) for r in names]; print('wreg',time.time()-t)
I9=[w.regress_initiation_on_rewards(rats[r],9,rng) for r in names]; print('ireg',time.time()-t)
I10=[w.regress_initiation_on_rewards(rats[r],10,rng) for r in names]
bw=np.array([b for b,_ in W]); tw=np.array([t for _,t in W])
bi=np.array([b for b,_ in I9]); ti=np.array([t for _,t in I9]); ti10=np.array([t for _,t in I10])
print('wt coef mean', np.round(bw.mean(0),3)); print('iti coef mean', np.round(bi.mean(0),4))
print('tau wt median', np.median(tw), (tw==0).mean(), 'tau iti median', np.median(ti), (ti==0).mean())
print('signrank', stats.wilcoxon(tw,ti).pvalue, stats.wilcoxon(tw,ti10).pvalue)
print('pearson', stats.pearsonr(ti,tw), stats.pearsonr(ti10,tw))
t=time.time()
pw=[w.wait_by_previous_offer(rats[r]) for r in names]; pi=[w.initiation_by_previous_offer(rats[r],True) for r in names]; pic=[w.initiation_by_previous_offer(rats[r],False) for r in names]
print('prev',time.time()-t)
pw=np.array(pw); pi=np.array(pi); pic=np.array(pic)
print('wt sig', (pw[:,2]<0.05).sum(), stats.mannwhitneyu(pw[:,0],pw[:,1]).pvalue, stats.wilcoxon(pw[:,0],pw[:,1]).pvalue)
print('iti20 sig', (pi[:,2]<0.05).sum(), stats.mannwhitneyu(pi[:,0],pi[:,1]).pvalue, stats.wilcoxon(pi[:,0],pi[:,1]).pvalue)
print('itiall sig', (pic[:,2]<0.05).sum(), stats.mannwhitneyu(pic[:,0],pic[:,1]).pvalue, stats.wilcoxon(pic[:,0],pic[:,1]).pvalue)
sw=pw[:,0]-pw[:,1]; si=pi[:,0]-pi[:,1]; sic=pic[:,0]-pic[:,1]
print('sens', stats.wilcoxon(sw,si).pvalue, stats.wilcoxon(sw,sic).pvalue)
pickle.dump((bw,tw,bi,ti,ti10,[b for b,_ in I10]),open(f'{d}/taus.pkl','wb'))
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t2.py 2>&1 | grep -v Warning
```

```
wreg 43.45722699165344
ireg 78.92892646789551
wt coef mean [ 0.211 -0.003  0.    -0.     0.     0.     0.     0.     0.     0.
 -0.531]
iti coef mean [-0.0307 -0.023  -0.0107 -0.0051 -0.002  -0.0009 -0.0003 -0.0003 -0.0002
  0.1418]
tau wt median 0.0 0.852233676975945 tau iti median 1.7696308853880869 0.0859106529209622
signrank 2.4486635277430198e-45 3.194025618592212e-45
pearson PearsonRResult(statistic=np.float64(0.10327974116975569), pvalue=np.float64(0.07858701910850835)) PearsonRResult(statistic=np.float64(0.14906420857285899), pvalue=np.float64(0.010892113287203149))
prev 1.8235063552856445
wt sig 38 0.7075212490005257 0.8080692880124083
iti20 sig 265 9.712075121209824e-25 9.356008857768286e-29
itiall sig 255 9.339836666563738e-97 1.8425951011266964e-49
sens 2.1916206392546393e-08 6.087016886054449e-38
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t3.py <<'EOF'
import pandas as pd, numpy as np, os, pickle, time
import wagering as w
d=os.environ['TMPDIR']
S,rats=pickle.load(open(f'{d}/rats.pkl','rb'))
names=sorted(rats)
rng=np.random.default_rng(3)
alphas=np.geomspace(1e-3,1,40)
for r in names[:6]:
    t=time.time()
    M=w.model_inputs(rats[r]); b=w.beliefs(M); inf=b.argmax(1); t1=time.time()-t
    p_inf,nll_inf=w.fit_inferential(M,inf,rng,20); t2=time.time()-t
    p_ret,nll_ret=w.fit_retrospective(M,b[:,0],alphas); t3=time.time()-t
    n=M['fitted'].sum()
    bic_i=4*np.log(n)+2*nll_inf; bic_r=2*np.log(n)+2*nll_ret
    print(r, len(M['R']), n, round(t1,2), round(t2,2), round(t3,2), np.round(p_inf,3), round(nll_inf,1), np.round(p_ret,4), round(nll_ret,1), 'dBIC', round(bic_r-bic_i,1))
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t3.py 2>&1 | grep -v Warning
```

```
C015 4647 691 0.02 0.63 0.73 [0.556 1.    0.682 0.143] 2425.3 [0.0492 0.0953] 2512.6 dBIC 161.6
C033 27437 4229 0.12 2.16 2.48 [0.397 0.533 0.437 0.092] 14688.1 [0.0492 0.0754] 14966.7 dBIC 540.6
C034 11807 1509 0.05 0.98 1.15 [0.594 0.453 0.386 0.097] 6444.7 [0.1194 0.073 ] 6536.7 dBIC 169.5
C035 20071 3810 0.09 1.89 2.14 [0.18  0.173 0.215 0.087] 12169.2 [0.0588 0.0926] 12636.9 dBIC 918.9
C036 14446 2073 0.06 1.15 1.35 [0.551 0.732 0.427 0.129] 8678.8 [0.2894 0.095 ] 8738.2 dBIC 103.6
E001 10490 2385 0.05 2.57 2.75 [0.007 0.016 0.007 0.055] 7177.5 [0.1425 0.1105] 7670.7 dBIC 970.9
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t4.py <<'EOF'
import pandas as pd, numpy as np, os, h5py, io, requests
d=os.environ['TMPDIR']
S=pd.read_parquet(f'{d}/sessions.parquet'); A=pd.read_parquet(f'{d}/assets.parquet')
def raw(path):
    url=A.set_index('path').url[path]
    f=h5py.File(io.BytesIO(requests.get(url).content),'r')
    rec=f['acquisition/task_recording']
    st_names=[s.decode() for s in f['general/task/state_types/state_name'][:]]
    ev_names=[s.decode() for s in f['general/task/event_types/event_name'][:]]
    states=pd.DataFrame({'name':np.array(st_names)[rec['states/state_type'][:]],'start':rec['states/start_time'][:],'stop':rec['states/stop_time'][:]})
    events=pd.DataFrame({'name':np.array(ev_names)[rec['events/event_type'][:]],'t':rec['events/timestamp'][:],'value':[v.decode() for v in rec['events/value'][:]]})
    acts=pd.DataFrame({'t':rec['actions/timestamp'][:]})
    tr=f['intervals/trials']; trials=pd.DataFrame({'start':tr['start_time'][:],'stop':tr['stop_time'][:]})
    g=f['intervals/processed_trials']; proc=pd.DataFrame({k:g[k][:] for k in ['inter_trial_interval','wait_time_unthresholded','is_opt_out','is_rewarded','is_violation','start_time']})
    return states,events,acts,trials,proc
for path in [S[S.center_port_cue=='True'].path.iloc[5], S[S.center_port_cue=='False'].path.iloc[5]]:
    states,events,acts,trials,proc=raw(path)
    print(path, len(trials), (trials.start.values==proc.start_time.values).all())
    # ITI check
    ci=events[(events.name=='center_port_poke')&(events.value=='In')].t.values
    first_ci=np.array([ci[(ci>=s)&(ci<e)].min() if ((ci>=s)&(ci<e)).any() else np.nan for s,e in zip(trials.start,trials.stop)])
    lat=first_ci-trials.start.values
    prev_unrew=np.r_[False, ~proc.is_rewarded.values[:-1]]
    dd=lat[prev_unrew]-proc.inter_trial_interval.values[prev_unrew]
    print(' ITI diff (prev unrewarded) median abs', np.nanmedian(np.abs(dd)), np.nanpercentile(np.abs(dd),95))
    # wait time check
    wsp=states[states.name=='wait_for_side_poke'].start.values; oo=states[states.name=='opt_out'].start.values
    tr_of=lambda t: np.searchsorted(trials.start.values,t,side='right')-1
    w=pd.Series(wsp,index=tr_of(wsp)).groupby(level=0).first(); o=pd.Series(oo,index=tr_of(oo)).groupby(level=0).first()
    wt=(o-w).dropna(); pw=proc.wait_time_unthresholded.values[wt.index]
    print(' WT diff median abs', np.nanmedian(np.abs(wt.values-pw)), np.nanpercentile(np.abs(wt.values-pw),95), len(wt))
    # sound before nose in center
    nic=states[states.name=='nose_in_center'].groupby(lambda i: 0).size()
    wfp=states[states.name=='wait_for_poke']
    a=acts.t.values
    inside=[((a>s+0.001)&(a<e-0.001)).any() for s,e in zip(wfp.start,wfp.stop)]
    print(' fraction of wait_for_poke states with a sound', np.mean(inside), len(wfp))
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t4.py
```

```
sub-E005/sub-E005_ses-RWTautowait2-20221116-133232.nwb 217 True
 ITI diff (prev unrewarded) median abs 2.4424906541753444e-14 1.1293188606487092e-13
 WT diff median abs 2.398081733190338e-14 7.922551503725116e-14 18
 fraction of wait_for_poke states with a sound 0.6728110599078341 217
sub-E005/sub-E005_ses-RWTautowait2-20221025-135229.nwb 295 True
 ITI diff (prev unrewarded) median abs 2.6510044159877566e-14 1.2423395645555502e-13
 WT diff median abs 2.6645352591003757e-14 1.0906830993917535e-13 27
 fraction of wait_for_poke states with a sound 0.7288135593220338 295
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/t4.py <<'EOF'
print('---')
for lab in ['True','False','absent']:
    for path in S[S.center_port_cue==lab].path.sample(3,random_state=1):
        states,events,acts,trials,proc=raw(path)
        a=np.sort(acts.t.values); wfp=states[states.name=='wait_for_poke']
        at_start=[(np.abs(a-s)<0.005).any() for s in wfp.start]
        per_trial=len(a)/len(trials)
        print(lab, path.split('/')[0], round(np.mean(at_start),3), round(per_trial,2))
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t4.py 2>&1 | sed -n '/---/,$p'
```

```
---
True sub-G069 1.0 6.26
True sub-M046 1.0 6.47
True sub-M044 1.0 6.73
False sub-G077 1.0 6.37
False sub-S056 1.0 6.17
False sub-M051 1.0 6.87
absent sub-L015 1.0 6.16
absent sub-S020 1.0 6.65
absent sub-J001 1.0 6.54
```

**Agent**

The processed initiation and wait times match the raw Bpod events to 1e-13 s. Sound actions carry no identity, so the pre-cue flag can't be checked from raw events. Now writing the notebook.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "\"\"\"Builds entries/001169-mah-2023/reproduce_mah_2023.ipynb (scratch script, not committed).\"\"\"\nimport nbformat as nbf\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Mah et al. (2023) from dandiset 001169\n\n**Paper.** Mah A, Schiereck SS, Bossio V, Constantinople CM (2023). Distinct value computations\nsupport rapid sequential decisions. *Nature Communications* 14:7573.\n[doi:10.1038/s41467-023-43250-x](https://doi.org/10.1038/s41467-023-43250-x). This attempt used\nthe full text, which is open access (PMC10663503), and the paper's analysis code\n(github.com/constantinoplelab/published, `rat_behavior`, commit b7b68ca).\n\n**Dandiset.** [DANDI:001169](https://dandiarchive.org/dandiset/001169/0.260825.1909), version\n0.260825.1909. The paper cites no DANDI version (its data statement points to Zenodo); this is\nthe only published version, and the draft has the same 23,034 assets and size, so it is pinned.\n\n**What the dandiset holds.** One NWB file per session: 23,034 sessions of 291 rats in the\ntemporal wagering task, with the raw Bpod states, events and actions, the raw trials table, and\na table of processed trials that the conversion filled from the paper's per-rat structs\n(`A_Structs_Final` on Zenodo). No neural data; the paper has none.\n\n**Outside inputs.** The paper's processed structs on Zenodo\n([10.5281/zenodo.10031483](https://doi.org/10.5281/zenodo.10031483)) are read for one claim,\n`zenodo-link`, which compares them with the dandiset. The Figure 4 claims use the structs of all\nfinal-stage sessions (`A_Structs_all`), which the dandiset does not hold; they are in the second\nnotebook, `reproduce_mah_2023_fig4.ipynb`.\n\nEach file is about 1 MB and is read whole into memory, in parallel; loading takes about nine\nminutes. Random numbers (exponential and model fits from random starts, shuffles) come from a\ngenerator per claim section with a fixed seed.\n\n| Claim | Data | Status |\n|---|---|---|\n| dataset-counts | dandiset | tested |\n| zenodo-link | with inputs (Zenodo) | tested |\n| fig1f-wait-time-block | dandiset | tested |\n| fig1i-initiation-block | dandiset | tested |\n| figs2-unrewarded-drive | dandiset | tested |\n| figs12-no-sex-difference | dandiset | tested |\n| fig2a-wait-time-converges | dandiset | tested |\n| fig2b-initiation-previous-block | dandiset | tested |\n| fig2cd-regression-kernels | dandiset | tested |\n| fig2e-tau-differ | dandiset | tested |\n| fig2f-tau-uncorrelated | dandiset | tested |\n| fig2gh-fast-slow-groups | dandiset | tested |\n| fig2j-wait-time-previous-reward | dandiset | tested |\n| fig2k-initiation-previous-reward | dandiset | tested |\n| fig2l-sensitivity-differs | dandiset | tested |\n| fig3c-catch-probability | dandiset | tested |\n| fig3j-model-comparison | dandiset | tested |\n| figs9-misinference | dandiset | tested |\n| fig3l-inference-quality | dandiset | tested |\n| fig3h-dynamic-learning-rate | dandiset | blocked: methods underspecified |\n| fig4a-wait-ratio-learning | elsewhere (Zenodo) | tested in the second notebook |\n| fig4bc-regression-learning | elsewhere (Zenodo) | tested in the second notebook |\n| fig4de-overshoot-learning | dandiset | blocked: data missing |\n| fig5b-precue-offer | dandiset | tested |\n| fig5c-precue-previous-reward | dandiset | tested |\n| fig5d-precue-previous-block | dandiset | tested |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nfor var in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ[var] = \"1\"\n\nimport time\nimport warnings\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport wagering as w\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\n\nstarted = time.time()\nassets = w.asset_list()\nsessions_all, trials_all = w.load_all(assets)\nprint(f\"loaded {len(sessions_all)} files ({assets['size'].sum() / 1e9:.1f} GB) from dandiset \"\n      f\"{w.DANDISET_ID} version {w.DANDISET_VERSION} in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nS, T = sessions_all, trials_all\nprint(\"Assets:\", len(assets), \"; all NWB:\", bool(assets.path.str.endswith(\".nwb\").all()))\nprint(\"Subjects (folders):\", assets.path.str.split(\"/\").str[0].nunique(), \"; subject ids in files:\", S.subject_id.nunique())\nprint(\"Sessions:\", len(S), \"; trials:\", len(T))\nprint(\"Species in files:\", S.species.unique().tolist())\nprint(\"Sex per rat:\", S.groupby(\"subject_id\").sex.agg(lambda s: \"/\".join(sorted(set(s)))).value_counts().to_dict())\nprint(\"Protocol per session:\", S.protocol.value_counts().to_dict())\nprint(\"Training stage values in processed trials:\", T.training_stage.value_counts().to_dict())\nprint(\"Subjects with an age in the files:\", S[S.has_age].subject_id.nunique(), \"of\", S.subject_id.nunique())\nprint(\"Processed and raw trial tables have the same length in every file:\", bool((S.n_raw_trials == S.n_trials).all()))\nprint(\"Columns of processed_trials (same in every file):\", S.processed_columns.nunique() == 1)\nprint(\"  \", list(S.processed_columns.iloc[0]))\nprint(\"Session start times:\", S.start.min(), \"to\", S.start.max())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe dandiset's summary (291 subjects, *Rattus norvegicus*) agrees with the files, and every rat\nhas one sex. The processed trials give the training stage as 9 for every trial; the paper says\nall data are from stage 8, and the Zenodo README says that code 9 is the paper's stage 8, which\nthe NWB files do not say. Ages are absent for 275 of 291 rats (the Methods give 6 to 24 months).\nThe processed table has no catch probability: the conversion's column mapping spells the\nstruct's `prob_catch` as `prob_cacth`, so it was not copied. The raw trials table has\n`catch_percentage`, which is used in its place (compared with the struct in `zenodo-link`).\n\"\"\")\n\ncode(r\"\"\"\n# Recordings deposited twice: sessions of the same rat identical trial for trial.\nsessions, trials, removed = w.drop_duplicate_sessions(sessions_all, trials_all)\nprint(\"Sessions identical to another of the same rat (removed):\")\nprint(removed[[\"subject_id\", \"session_id\", \"n_trials\", \"path\"]].to_string(index=False))\nkept_twin = sessions[(sessions.subject_id.isin(removed.subject_id)) &\n                     (sessions.start.isin(removed.start))]\nprint(\"kept:\", kept_twin[[\"subject_id\", \"session_id\", \"n_trials\", \"path\"]].to_string(index=False, header=False))\nsessions[\"date\"] = sessions.session_id.str.split(\"-\").str[1]\nsame_day = sessions[sessions.duplicated([\"subject_id\", \"date\"], keep=False)]\nprint(f\"\\nRats with two different sessions on one date: {same_day.subject_id.nunique()} \"\n      f\"({len(same_day)} sessions); their trial counts differ, so these are separate sessions.\")\nprint(\"Session ids with a suffix:\", sessions_all[sessions_all.session_id.str.count(\"-\") > 2].session_id.tolist())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nOne session is deposited twice: rat L011's session of 2022-10-04 appears as\n`RWTautowait2-20221004-095612` and `RWTautowait2-20221004-095612-x`, with identical trials. It\nis counted once from here on. The other same-day pairs are different sessions. The session\n`L004 ... -edit` has no twin.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Offered volumes (uL) by sex, trials:\")\nprint(pd.crosstab(T.reward_volume_ul, sessions_all.sex.to_numpy()[T.session]).to_string())\nmin_vol = T.groupby(\"rat\", observed=True).reward_volume_ul.min()\nsex = sessions_all.groupby(\"subject_id\").sex.first()\nprint(\"Rats whose smallest offer is 4 uL, by sex:\", sex[min_vol[min_vol == 4].index].value_counts().to_dict(),\n      \"; 5 uL:\", sex[min_vol[min_vol == 5].index].value_counts().to_dict())\nprint(\"\\nOffers (standardised) per block, trials:\")\nprint(pd.crosstab(trials.block_type.map({1: \"mixed\", 2: \"high\", 3: \"low\"}), trials.reward).to_string())\n# Block length in completed (non-violation) trials, for blocks that end inside a session.\nb = trials.block_type.to_numpy(); s = trials.session.to_numpy(); v = trials.is_violation.to_numpy()\nnew = np.r_[True, (b[1:] != b[:-1]) | (s[1:] != s[:-1])]\nblock_id = np.cumsum(new)\nends_in_session = np.r_[(s[1:] == s[:-1]) & (b[1:] != b[:-1]), False]\ncompleted = pd.Series(~v).groupby(block_id).sum()\nclosed = pd.Series(ends_in_session).groupby(block_id).any()\nprint(\"\\nCompleted trials in blocks that end within a session:\", completed[closed].describe()[[\"count\", \"min\", \"50%\", \"max\"]].to_dict())\nprint(\"Share of such blocks with exactly 40 completed trials:\", round(float((completed[closed] == 40).mean()), 3))\nfirst_block = trials.groupby(\"session\").block_type.first()\nprint(\"First block of each session:\", first_block.map({1: \"mixed\", 2: \"high\", 3: \"low\"}).value_counts().to_dict())\nprint(\"\\nCatch probability (raw trials, catch_percentage):\", trials.catch_percentage.round(3).value_counts().sort_index().to_dict())\nprint(\"Catch trials by catch probability, share of trials:\",\n      trials.groupby(trials.catch_percentage.round(2)).is_catch.mean().round(3).to_dict())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nOffers are 5 to 80 uL for 192 rats and 4 to 64 uL for 99 female rats, as the Methods describe\nfor some females; they are standardised to 5 to 80 uL below. Low blocks offer only 5, 10 and\n20 uL, high blocks 20, 40 and 80 uL, mixed blocks all five. Blocks change after a median of 40\ncompleted trials and every session starts with a mixed block, as the Methods state. The files'\ncatch probabilities include 0.30, which the paper's list of cohorts (0.1, 0.15, 0.2, 0.25 and\n0.35) does not have; the realised share of catch trials follows each stated probability.\n\"\"\")\n\ncode(r\"\"\"\nwt = trials.wait_time.to_numpy(); wtu = trials.wait_time_unthresholded.to_numpy(); thr = trials.wait_time_threshold.to_numpy()\nboth = ~np.isnan(wtu)\nprint(\"Trials with a wait time (unthresholded):\", int(both.sum()), \"; opt-out or rewarded among them:\",\n      round(float((trials.is_opt_out | trials.is_rewarded)[both].mean()), 4))\nprint(\"Wait time equals the unthresholded value where that is at most the threshold:\",\n      bool(np.allclose(wt[both & (wtu <= thr)], wtu[both & (wtu <= thr)])),\n      \"; NaN where above:\", bool(np.isnan(wt[both & (wtu > thr)]).all()), f\"({int((both & (wtu > thr)).sum())} trials)\")\nprint(\"Thresholds per rat (s):\", trials.groupby(\"rat\", observed=True).wait_time_threshold.first().describe()[[\"min\", \"50%\", \"max\"]].round(1).to_dict())\nprint(\"One threshold per rat:\", bool((trials.groupby(\"rat\", observed=True).wait_time_threshold.nunique() == 1).all()))\nprint(\"Unthresholded wait times (s):\", np.nanpercentile(wtu, [0, 50, 99, 100]).round(2).tolist())\niti = trials.inter_trial_interval.to_numpy()\nprint(\"Trial initiation times (s), percentiles 0, 50, 99, 100:\", np.nanpercentile(iti, [0, 50, 99, 100]).round(2).tolist(),\n      \"; missing:\", int(np.isnan(iti).sum()))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n`wait_time` is the unthresholded wait time with values above the rat's threshold removed, one\nthreshold per rat, as the descriptions say (the Methods say one standard deviation above the\npooled mean). Wait times and trial initiation times are in seconds; the largest initiation times\n(minutes to hours) are pauses, which the analysis removes at each rat's 99th percentile, as the\nMethods do.\n\"\"\")\n\ncode(r\"\"\"\n# The processed times against the raw Bpod events of the same files, for a sample of sessions.\nimport h5py, io, requests\n\ndef raw_check(row):\n    content = requests.get(row.url, timeout=120).content\n    with h5py.File(io.BytesIO(content), \"r\") as f:\n        rec = f[\"acquisition/task_recording\"]\n        st_names = np.array([x.decode() for x in f[\"general/task/state_types/state_name\"][:]])\n        ev_names = np.array([x.decode() for x in f[\"general/task/event_types/event_name\"][:]])\n        states = pd.DataFrame({\"name\": st_names[rec[\"states/state_type\"][:]], \"start\": rec[\"states/start_time\"][:]})\n        ev = pd.DataFrame({\"name\": ev_names[rec[\"events/event_type\"][:]], \"t\": rec[\"events/timestamp\"][:],\n                           \"value\": [x.decode() for x in rec[\"events/value\"][:]]})\n        tstart, tstop = f[\"intervals/trials/start_time\"][:], f[\"intervals/trials/stop_time\"][:]\n        g = f[\"intervals/processed_trials\"]\n        proc = {k: g[k][:] for k in (\"inter_trial_interval\", \"wait_time_unthresholded\", \"is_rewarded\", \"start_time\")}\n    cin = np.sort(ev[(ev.name == \"center_port_poke\") & (ev.value == \"In\")].t.to_numpy())\n    first_in = np.array([cin[(cin >= a) & (cin < b)].min() if ((cin >= a) & (cin < b)).any() else np.nan\n                         for a, b in zip(tstart, tstop)])\n    prev_unrewarded = np.r_[False, ~proc[\"is_rewarded\"][:-1]]\n    d_iti = (first_in - tstart - proc[\"inter_trial_interval\"])[prev_unrewarded]\n    trial_of = lambda t: np.searchsorted(tstart, t, side=\"right\") - 1\n    side = states[states.name == \"wait_for_side_poke\"]; opt = states[states.name == \"opt_out\"]\n    side = pd.Series(side.start.to_numpy(), index=trial_of(side.start.to_numpy())).groupby(level=0).first()\n    opt = pd.Series(opt.start.to_numpy(), index=trial_of(opt.start.to_numpy())).groupby(level=0).first()\n    waited = (opt - side).dropna()\n    d_wt = waited.to_numpy() - proc[\"wait_time_unthresholded\"][waited.index.to_numpy()]\n    return {\"session\": row.session_id, \"same_trial_starts\": bool(np.allclose(tstart, proc[\"start_time\"])),\n            \"n_iti\": int(np.sum(~np.isnan(d_iti))), \"max_abs_iti_diff_s\": np.nanmax(np.abs(d_iti)),\n            \"n_optout\": len(d_wt), \"max_abs_wait_diff_s\": np.nanmax(np.abs(d_wt)) if len(d_wt) else np.nan}\n\nsample = sessions_all.merge(assets[[\"path\", \"url\"]], on=\"path\").sample(24, random_state=0)\nwith ProcessPoolExecutor(4) as pool:\n    checks = pd.DataFrame(list(pool.map(raw_check, sample.itertuples())))\nprint(checks.to_string(index=False))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nIn 24 sessions drawn at random, the processed trial initiation time after an unrewarded trial\nequals the time from the trial's start to its first center poke in the raw events, and the\nprocessed wait time of an opt-out trial equals the time from the side light (`wait_for_side_poke`)\nto the opt-out (`opt_out`), to within the precision printed; the processed and raw trials start\nat the same times. The processed measures and the raw events therefore share one clock. The\nblock contrast itself (initiation and wait times by block, `fig1f` and `fig1i` below) shows\nthat the trial labels line up with the behaviour.\n\"\"\")\n\ncode(r\"\"\"\ncue = sessions[sessions.center_port_cue == \"True\"]\nprint(\"Sessions with center_port_cue true:\", len(cue), \"in\", cue.subject_id.nunique(), \"rats; with it false:\",\n      int((sessions.center_port_cue == \"False\").sum()), \"; argument absent:\", int((sessions.center_port_cue == \"absent\").sum()))\nFIG5_RATS = [\"M041\", \"M042\", \"M043\", \"M044\", \"M045\", \"M046\", \"M047\", \"M048\", \"G070\", \"E005\", \"E008\",\n             \"G078\", \"G076\", \"G069\", \"S042\", \"S050\"]   # the rats listed in the paper's Figure5.m\nprint(\"Same rats as Figure5.m:\", sorted(cue.subject_id.unique()) == sorted(FIG5_RATS))\nper_rat = sessions[sessions.subject_id.isin(FIG5_RATS)].groupby(\"subject_id\").agg(\n    cue_sessions=(\"center_port_cue\", lambda s: int((s == \"True\").sum())),\n    other_sessions=(\"center_port_cue\", lambda s: int((s != \"True\").sum())),\n    first_cue=(\"start\", lambda s: None))\nfor r in per_rat.index:\n    ss = sessions[sessions.subject_id == r]\n    per_rat.loc[r, \"first_cue\"] = ss[ss.center_port_cue == \"True\"].start.min().date()\n    per_rat.loc[r, \"last_other\"] = ss[ss.center_port_cue != \"True\"].start.max().date() if (ss.center_port_cue != \"True\").any() else None\nprint(per_rat.to_string())\nprint(\"\\nTrials in cue sessions:\", int(trials.session.isin(cue.index).sum()), \"of\", len(trials))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe 762 sessions flagged with the task argument `center_port_cue` belong to exactly the 16 rats\nthat the paper's Figure 5 code lists, and in each rat they follow its sessions of the original\ntask, so the flag is consistent with the pre-initiation cue task; four rats (M045 to M048) have\nonly cue sessions, as the Methods say four rats were trained only on it. The raw files cannot\nconfirm the flag: every sound is stored as the same action (\"sound_output\", \"On\") without its\nidentity. These sessions are part of the paper's main data (`A_Structs_Final`, from which the\nconversion was made), so they enter the analyses of Figures 1 to 3 as in the paper; the Methods\ndo not say so.\n\"\"\")\n\ncode(r\"\"\"\nrats = w.rat_arrays(trials, sessions)\nnames = sorted(rats)\nsex_of = sessions.groupby(\"subject_id\").sex.first()\nprint(len(names), \"rats;\", \"trials per rat:\", pd.Series({r: len(rats[r][\"reward\"]) for r in names}).describe()[[\"min\", \"50%\", \"max\"]].to_dict())\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## dataset-counts\n\n> Data from 291 Long-Evans rats (184 male, 107 female), with a median of 71 sessions and 33,493\n> trials per rat.\n\"\"\")\n\ncode(r\"\"\"\nper = sessions.groupby(\"subject_id\").agg(sessions=(\"n_trials\", \"size\"), trials=(\"n_trials\", \"sum\"))\ncounts = {\"rats\": len(per), \"median sessions per rat\": per.sessions.median(), \"median trials per rat\": per.trials.median(),\n          \"male rats\": int((sex_of == \"M\").sum()), \"female rats\": int((sex_of == \"F\").sum())}\nexpected = {\"rats\": 291, \"median sessions per rat\": 71, \"median trials per rat\": 33493, \"male rats\": 184, \"female rats\": 107}\nprint(pd.DataFrame({\"dandiset\": counts, \"paper\": expected}).to_string())\nper_all = sessions_all.groupby(\"subject_id\").agg(sessions=(\"n_trials\", \"size\"), trials=(\"n_trials\", \"sum\"))\nprint(\"\\nWith the duplicated L011 session counted twice: median sessions\", per_all.sessions.median(),\n      \", median trials\", per_all.trials.median())\nprint(\"Sessions per rat, range:\", per.sessions.min(), \"to\", per.sessions.max(), \"; trials per rat:\", per.trials.min(), \"to\", per.trials.max())\nprint(\"The Methods also give 160 male and 114 female rats (274 in all).\")\n\"\"\", [\"claim:dataset-counts\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The files hold 291 rats, 184 male and 107 female, with a median of 71\nsessions and 33,493 trials per rat, each session counted once; all five numbers match the paper.\nThe second count in the Methods (160 male and 114 female) does not match the files, nor the\npaper's own 291 rats.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## zenodo-link\n\n> The dandiset holds the paper's processed per-rat data (A_Structs_Final in the Zenodo deposit)\n> for every rat, session and trial, with the same values.\n\nThe structs are read from the Zenodo zip archive with range requests (about 0.4 GB).\n\"\"\")\n\ncode(r\"\"\"\nstarted = time.time()\nstructs = w.load_zenodo_structs(\"A_Structs_Final\")\nprint(f\"read {len(structs)} structs in {time.time() - started:.0f} s\")\nFIELDS = {\"reward\": \"volume\", \"block\": \"block\", \"catch\": \"catch\", \"vios\": \"vios\", \"hits\": \"hits\",\n          \"optout\": \"optout\", \"wait_time\": \"wait_time\", \"ITI\": \"iti\", \"prob_catch\": \"prob_catch\"}\nrows = []\nfor r in sorted(set(structs) | set(names)):\n    Z, A = structs.get(r), rats.get(r)\n    row = {\"rat\": r, \"in_zenodo\": Z is not None, \"in_dandiset\": A is not None}\n    if Z is not None and A is not None:\n        nt_z = np.atleast_1d(Z[\"ntrials\"]).astype(int)\n        nt_d = np.bincount(A[\"session\"])\n        row.update(sessions_zenodo=len(nt_z), sessions_dandiset=len(nt_d), same_sessions=np.array_equal(nt_z, nt_d))\n        if row[\"same_sessions\"]:\n            for zf, af in FIELDS.items():\n                a = A[af].astype(float); z = np.asarray(Z[zf], float).ravel()\n                row[zf] = bool(np.allclose(a, z, atol=1e-3 if zf == \"prob_catch\" else 1e-4, equal_nan=True))\n    rows.append(row)\nlink = pd.DataFrame(rows)\nprint(\"Rats in both:\", int((link.in_zenodo & link.in_dandiset).sum()), \"; only Zenodo:\", link[~link.in_dandiset].rat.tolist(),\n      \"; only dandiset:\", link[~link.in_zenodo].rat.tolist())\nprint(\"Rats with the same sessions (count and trials per session):\", int(link.same_sessions.sum()))\nprint(link[link.same_sessions == False][[\"rat\", \"sessions_zenodo\", \"sessions_dandiset\"]].to_string(index=False))\nprint(\"\\nRats whose values match, per field:\")\nprint(link[list(FIELDS)].sum().astype(int).to_string())\nmismatch = link[link.same_sessions == True][list(FIELDS)].eq(False).any(axis=1)\nprint(\"Rats matching in every field:\", int((~mismatch).sum()), \"of\", int(link.same_sessions.sum()))\n\"\"\", [\"claim:zenodo-link\"])\n\ncode(r\"\"\"\n# The structs before the duplicate was removed: does L011 have 205 sessions on Zenodo?\nnz = len(np.atleast_1d(structs[\"L011\"][\"ntrials\"]))\nprint(\"L011 sessions on Zenodo:\", nz, \"; in the dandiset with the duplicate:\", int((sessions_all.subject_id == \"L011\").sum()))\n\"\"\", [\"claim:zenodo-link\"])\n\nmd(r\"\"\"\n**Result: reproduced.** All 291 rats are in both, and every rat has the same sessions (count and\ntrials per session) once the duplicated L011 session is counted once; the Zenodo struct of\nL011 has 204 sessions, the dandiset 205. For every rat, the reward, block, catch, violation,\nreward delivered, opt-out, wait time and trial initiation time of every trial match, and the\ncatch probability of the raw trials matches the structs' `prob_catch`. The dandiset holds the\npaper's processed data in full.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig1f-wait-time-block\n\n> Rats waited about 10% less for 20 uL in high blocks than in low blocks (p = 8.26e-49,\n> two-tailed Wilcoxon signed-rank test, N = 291).\n\"\"\")\n\ncode(r\"\"\"\nwc = {r: w.wait_curves(rats[r]) for r in names}\nhi = np.array([wc[r][(2, 20)] for r in names]); lo = np.array([wc[r][(3, 20)] for r in names])\nzhi = np.array([wc[r][(\"z\", 2, 20)] for r in names]); zlo = np.array([wc[r][(\"z\", 3, 20)] for r in names])\nratio = hi / lo\nprint(f\"(a) 1 - mean of per-rat ratios: {100 * (1 - np.nanmean(ratio)):.2f}%   (b) 1 - ratio of population means: \"\n      f\"{100 * (1 - np.nanmean(hi) / np.nanmean(lo)):.2f}%   [expected 10 +- 2.5]\")\nprint(f\"Signed-rank, per-rat means of z-scored wait times (Methods): p = {w.signrank(zhi, zlo):.3g}; \"\n      f\"high below low in {np.sum(zhi < zlo)} of {np.sum(~np.isnan(zhi - zlo))} rats\")\nprint(f\"Variant, raw means (Figure1.m): p = {w.signrank(hi, lo):.3g}; high below low in {np.sum(hi < lo)} rats\")\npw = np.array([wc[r][\"p\"] for r in names])\nprint(f\"Rats with p < 0.05 (one-tailed rank-sum, as the code): {np.sum(pw < 0.05)} of {len(names)}\")\nprint(\"Per-rat ratio, range:\", np.nanmin(ratio).round(3), \"to\", np.nanmax(ratio).round(3), \"; median\", np.nanmedian(ratio).round(3))\nfor s_ in (\"M\", \"F\"):\n    m = np.array([sex_of[r] == s_ for r in names])\n    print(f\"  {s_}: {m.sum()} rats, mean ratio {np.nanmean(ratio[m]):.3f}, signed-rank p = {w.signrank(zhi[m], zlo[m]):.3g}\")\nno_cue = {r: w.subset(rats[r], ~rats[r][\"cue\"]) for r in names}\nwc_nc = {r: w.wait_curves(no_cue[r]) for r in names if len(no_cue[r][\"reward\"])}\nr_nc = np.array([wc_nc[r][(2, 20)] / wc_nc[r][(3, 20)] for r in wc_nc])\nprint(f\"Variant without the pre-cue sessions: mean ratio {np.nanmean(r_nc):.3f} over {np.sum(~np.isnan(r_nc))} rats\")\n\nfig, axes = plt.subplots(1, 2, figsize=(9, 3.2))\nfor b, c, lab in ((1, \"k\", \"mixed\"), (2, \"r\", \"high\"), (3, \"b\", \"low\")):\n    m = np.array([[wc[r][(b, v)] for v in w.STANDARD_VOLUMES] for r in names])\n    axes[0].errorbar(range(5), np.nanmean(m, 0), np.nanstd(m, 0) / np.sqrt(np.sum(~np.isnan(m), 0)), color=c, label=lab)\naxes[0].set_xticks(range(5), w.STANDARD_VOLUMES); axes[0].set_xlabel(\"offer (uL)\"); axes[0].set_ylabel(\"mean wait time (s)\"); axes[0].legend()\naxes[1].hist(ratio[~np.isnan(ratio)], 30, color=\"0.6\"); axes[1].axvline(1, color=\"k\", ls=\"--\"); axes[1].axvline(np.nanmean(ratio), color=\"k\")\naxes[1].set_xlabel(\"wait time ratio, 20 uL high/low\"); axes[1].set_ylabel(\"rats\")\nplt.tight_layout(); plt.show()\nprint(\"All per-rat ratios are inside the histogram's axis.\")\n\"\"\", [\"claim:fig1f-wait-time-block\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Rats waited 10.6% less for 20 uL in high than in low blocks by either\nreading (10.58% and 10.79%), and the signed-rank test on z-scored wait times finds high below low\n(p = 4.6e-47, 279 of 291 rats). The code's test on raw means gives p = 8.2e-47 against the\npaper's 8.26e-49. The effect holds in males and in females.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig1i-initiation-block\n\n> Rats initiated trials more quickly in high than in low blocks (p = 1.82e-49, two-tailed\n> Wilcoxon signed-rank test, N = 291).\n\"\"\")\n\ncode(r\"\"\"\nib = {r: w.initiation_by_block(rats[r]) for r in names}\nih = np.array([ib[r][2] for r in names]); il = np.array([ib[r][3] for r in names])\nzih = np.array([ib[r][(\"z\", 2)] for r in names]); zil = np.array([ib[r][(\"z\", 3)] for r in names])\nprint(f\"Signed-rank, per-rat means of z-scored initiation times (Methods): p = {w.signrank(zih, zil):.3g}; \"\n      f\"high below low in {np.sum(zih < zil)} of {len(names)} rats\")\nprint(f\"Variant, raw means (Figure1.m): p = {w.signrank(ih, il):.3g}\")\nprint(f\"Mean ratio high/low {np.mean(ih / il):.3f} (range {np.min(ih / il):.3f} to {np.max(ih / il):.3f})\")\npi_ = np.array([ib[r][\"p\"] for r in names])\nprint(f\"Rats with p < 0.05 (one-tailed rank-sum, as the code): {np.sum(pi_ < 0.05)} of {len(names)}\")\nprint(\"Smallest p the two-sided signed-rank test can give for 291 rats all in one direction:\",\n      f\"{w.signrank(np.ones(291) + np.arange(291) * 1e-6):.3g}\")\nfor s_ in (\"M\", \"F\"):\n    m = np.array([sex_of[r] == s_ for r in names])\n    print(f\"  {s_}: mean ratio {np.mean(ih[m] / il[m]):.3f}, signed-rank p = {w.signrank(zih[m], zil[m]):.3g}\")\n\"\"\", [\"claim:fig1i-initiation-block\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Every rat initiated trials faster in high than in low blocks (291 of\n291), p = 1.8e-49 on z-scored and on raw means, the smallest p this test gives for 291 rats and\nthe value the paper reports (1.82e-49). The mean ratio high/low is 0.56.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## figs2-unrewarded-drive\n\n> Block sensitivity of trial initiation times is largely driven by initiation times that follow\n> unrewarded trials.\n\"\"\")\n\ncode(r\"\"\"\npo = {r: w.initiation_by_previous_outcome(rats[r]) for r in names}\nd_rew = np.array([po[r][\"rewarded\"][0] - po[r][\"rewarded\"][1] for r in names])\nd_unrew = np.array([po[r][\"unrewarded\"][0] - po[r][\"unrewarded\"][1] for r in names])\nprint(f\"Low minus high, z-scored initiation time; after rewarded: median {np.nanmedian(d_rew):.3f}, \"\n      f\"after unrewarded: median {np.nanmedian(d_unrew):.3f}\")\nprint(f\"Signed-rank, after unrewarded against after rewarded: p = {w.signrank(d_unrew, d_rew):.3g}; \"\n      f\"larger after unrewarded in {np.sum(d_unrew > d_rew)} of {np.sum(~np.isnan(d_unrew - d_rew))} rats\")\nprint(f\"Each against zero: after rewarded p = {w.signrank(d_rew):.3g}, after unrewarded p = {w.signrank(d_unrew):.3g}\")\n\"\"\", [\"claim:figs2-unrewarded-drive\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The block difference in z-scored initiation time is larger after\nunrewarded trials (median 0.69) than after rewarded ones (median 0.08), p = 6.6e-49 by signed\nrank, larger in 290 of 291 rats.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## figs12-no-sex-difference\n\n> Male and female rats did not differ in their contextual effects (wait time and trial\n> initiation time ratios).\n\"\"\")\n\ncode(r\"\"\"\nmale = np.array([sex_of[r] == \"M\" for r in names])\nlat_ratio = ih / il\nprint(f\"Wait time ratio: males median {np.nanmedian(ratio[male]):.3f} ({male.sum()}), females median \"\n      f\"{np.nanmedian(ratio[~male]):.3f} ({(~male).sum()}); rank-sum p = {w.ranksum(ratio[male], ratio[~male]):.3g}\")\nprint(f\"Initiation time ratio: males median {np.median(lat_ratio[male]):.3f}, females median \"\n      f\"{np.median(lat_ratio[~male]):.3f}; rank-sum p = {w.ranksum(lat_ratio[male], lat_ratio[~male]):.3g}\")\n\"\"\", [\"claim:figs12-no-sex-difference\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** The wait time ratios of males and females do not differ (p = 0.47),\nbut the initiation time ratios do (p = 0.0021, medians 0.54 in males and 0.60 in females), so the\ncode's test finds a sex difference in one of the two contextual effects.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig2a-wait-time-converges\n\n> At transitions from high or low blocks into mixed blocks, wait times converge to a common\n> value regardless of the previous block.\n\n## fig2b-initiation-previous-block\n\n> Trial initiation times in mixed blocks depend strongly on the previous block, unlike wait times.\n\"\"\")\n\ncode(r\"\"\"\nwd = {r: w.wait_dynamics(rats[r]) for r in names}\nidn = {r: w.initiation_dynamics(rats[r]) for r in names}\nidn_raw = {r: w.initiation_dynamics(rats[r], detrend=False) for r in names}\nx = np.arange(-20, 21)\nPRE, POST = (x >= -20) & (x <= -6), (x >= 11) & (x <= 20)\n\ndef transition_summary(dyn, label):\n    diff = np.array([dyn[r][-2] - dyn[r][-1] for r in dyn])     # low-to-mixed minus high-to-mixed\n    m = np.nanmean(diff, 0)\n    pre, post = np.nanmean(m[PRE]), np.nanmean(m[POST])\n    per_rat_post = np.nanmean(diff[:, POST], 1)\n    print(f\"{label}: before {pre:.3f}, after {post:.3f}, after/before {post / pre:.3f}; per-rat after: median \"\n          f\"{np.nanmedian(per_rat_post):.3f}, above zero in {np.sum(per_rat_post > 0)} of {np.sum(~np.isnan(per_rat_post))}, \"\n          f\"signed-rank p = {w.signrank(per_rat_post):.3g}\")\n    late = (x >= 6) & (x <= 20)\n    print(f\"   variant window +6 to +20: after/before {np.nanmean(m[late]) / pre:.3f}\")\n    return diff, m\n\nwd_diff, wd_m = transition_summary(wd, \"Wait time (fig2a)\")\nid_diff, id_m = transition_summary(idn, \"Initiation time (fig2b)\")\n_ = transition_summary(idn_raw, \"Initiation time, not detrended (variant)\")\nfor s_, m_ in ((\"M\", male), (\"F\", ~male)):\n    for lab, dd in ((\"wait\", wd_diff), (\"initiation\", id_diff)):\n        mm = np.nanmean(dd[m_], 0)\n        print(f\"  {s_} {lab}: after/before {np.nanmean(mm[POST]) / np.nanmean(mm[PRE]):.3f}\")\n\nfig, axes = plt.subplots(1, 2, figsize=(9, 3.2))\nfor ax, dyn, lab in ((axes[0], wd, \"delta z wait time\"), (axes[1], idn, \"z initiation time (detrended)\")):\n    for kind, c in ((-2, \"b\"), (-1, \"r\")):\n        arr = np.array([dyn[r][kind] for r in names])\n        ax.plot(x, np.nanmean(arr, 0), color=c, label={-2: \"low to mixed\", -1: \"high to mixed\"}[kind])\n    ax.axvline(0, color=\"k\", lw=0.5); ax.set_xlabel(\"trials from block switch\"); ax.set_ylabel(lab)\naxes[0].legend(); plt.tight_layout(); plt.show()\nfor lab, dyn in ((\"wait\", wd), (\"initiation\", idn)):\n    arr = np.array([np.nanmean([dyn[r][k] for r in names], 0) for k in (-2, -1)])\n    print(f\"{lab}: plotted range {np.nanmin(arr):.3f} to {np.nanmax(arr):.3f}\")\n\"\"\", [\"claim:fig2a-wait-time-converges\", \"claim:fig2b-initiation-previous-block\"])\n\nmd(r\"\"\"\n**Result: reproduced** (fig2a). Before the switch, wait times after low blocks are 0.33 z above\nthose after high blocks; 11 to 20 trials into the mixed block the difference is 0.022, a ratio\nof 0.067, under the criterion's 0.25.\n\n**Result: not reproduced** (fig2b), by the criterion as written. Initiation times in mixed blocks\ndo depend strongly on the previous block, but with the opposite sign to the one the criterion\nassumed: after low blocks rats initiate faster than after high blocks (difference -0.26 z\nagainst +0.12 before the switch, ratio -2.1; per-rat difference below zero in most rats). The\ncriterion required the difference to keep its sign. The reversal is the incentive contrast and\novershoot that the paper itself describes for Figure 2b, so the data agree with the paper's\nstatement; the outcome reflects a criterion written with the wrong sign before the analysis.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig2cd-regression-kernels\n\n> Wait times are explained by the current reward, while trial initiation times reflect an\n> exponentially weighted effect of previous rewards.\n\n## fig2e-tau-differ\n\n> The time constants of exponentials fit to the previous-reward coefficients differ between trial\n> initiation and wait times (p = 1.30e-49, two-tailed signed-rank test, N = 291).\n\n## fig2f-tau-uncorrelated\n\n> The time constants of trial initiation and wait times are not correlated across rats.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(2002)\nstarted = time.time()\nreg_wt = [w.regress_wait_on_rewards(rats[r], 10, rng) for r in names]\nreg_i9 = [w.regress_initiation_on_rewards(rats[r], 9, rng) for r in names]\nreg_i10 = [w.regress_initiation_on_rewards(rats[r], 10, rng) for r in names]\nprint(f\"regressions and fits in {time.time() - started:.0f} s\")\nb_wt = np.array([b for b, _ in reg_wt]); tau_wt = np.array([t for _, t in reg_wt])\nb_i9 = np.array([b for b, _ in reg_i9]); tau_i9 = np.array([t for _, t in reg_i9])\nb_i10 = np.array([b for b, _ in reg_i10]); tau_i10 = np.array([t for _, t in reg_i10])\nprint(\"Mean wait time coefficients (current, 1 to 9 back; after zeroing):\", np.round(b_wt[:, :10].mean(0), 4).tolist())\nprint(\"Mean initiation time coefficients (1 to 9 back; after zeroing):\", np.round(b_i9[:, :9].mean(0), 4).tolist())\nprint(f\"Wait time, current reward coefficient above zero: {np.sum(b_wt[:, 0] > 0)} rats, signed-rank p = {w.signrank(b_wt[:, 0]):.3g}\")\nprint(f\"Initiation time, previous reward coefficient below zero: {np.sum(b_i9[:, 0] < 0)} rats, signed-rank p = {w.signrank(b_i9[:, 0]):.3g}\")\nprint(f\"|mean wait coefficient 1 back| / mean current = {abs(b_wt[:, 1].mean()) / b_wt[:, 0].mean():.3f}\")\nmi = np.abs(b_i9[:, :9].mean(0))\nprint(f\"|mean initiation coefficient| at 1, 3 and 6 back: {mi[0]:.4f}, {mi[2]:.4f}, {mi[5]:.4f}\")\nprint(\"Rats with every previous wait time coefficient zeroed:\", int(np.sum(np.all(b_wt[:, 1:10] == 0, 1))))\n\"\"\", [\"claim:fig2cd-regression-kernels\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The current offer raises wait times (coefficient above zero in 291 of\n291 rats, p = 1.8e-49), and the mean coefficient one trial back is 1.4% of it; initiation times\nfall with the previous reward (below zero in 287 rats, p = 7.6e-49), with mean coefficients\nfalling from 0.031 one trial back to 0.011 three back and 0.0009 six back.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Tau, wait times: median {np.median(tau_wt):.2f} (0 in {np.sum(tau_wt == 0)} rats); initiation times \"\n      f\"(9 back, Methods): median {np.median(tau_i9):.2f} (0 in {np.sum(tau_i9 == 0)} rats)\")\nprint(f\"Signed-rank, initiation against wait time taus: p = {w.signrank(tau_i9, tau_wt):.3g}; \"\n      f\"initiation larger in {np.sum(tau_i9 > tau_wt)} rats, smaller in {np.sum(tau_i9 < tau_wt)}\")\nprint(f\"Variant, 10 back (Figure2.m): median {np.median(tau_i10):.2f}, p = {w.signrank(tau_i10, tau_wt):.3g}\")\nprint(\"Tau ranges: wait\", tau_wt.min().round(2), \"to\", tau_wt.max().round(2), \"; initiation\", tau_i9.min().round(2), \"to\", tau_i9.max().round(2))\n\"\"\", [\"claim:fig2e-tau-differ\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Initiation time taus (median 1.77 trials) exceed wait time taus (median\n0, as in 248 rats no previous coefficient survives), p = 2.4e-45 against the paper's 1.30e-49.\n\"\"\")\n\ncode(r\"\"\"\nr9, p9 = stats.pearsonr(tau_i9, tau_wt)\nr10, p10 = stats.pearsonr(tau_i10, tau_wt)\nprint(f\"Pearson, initiation (9 back, Methods) against wait time taus: r = {r9:.3f}, p = {p9:.3g}  (paper: r = -0.03, p = 0.53 \"\n      \"in the legend; r = 0.08, p = 0.18 in the text)\")\nprint(f\"Variant, 10 back (Figure2.m): r = {r10:.3f}, p = {p10:.3g}\")\nnz = tau_wt > 0\nr_nz, p_nz = stats.pearsonr(tau_i9[nz], tau_wt[nz])\nprint(f\"Variant, the {nz.sum()} rats with a wait time tau above 0: r = {r_nz:.3f}, p = {p_nz:.3g}\")\n\"\"\", [\"claim:fig2f-tau-uncorrelated\"])\n\nmd(r\"\"\"\n**Result: reproduced.** With 9 previous rewards, as the Methods state, the two taus are not\ncorrelated (r = 0.10, p = 0.079). With the code's 10 they are (r = 0.15, p = 0.011), so the\nresult depends on that choice; the paper itself gives two different values of r.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig2gh-fast-slow-groups\n\n> Rats with fast and slow trial initiation time constants differ in their initiation time\n> coefficients (p = 0.02, permutation test, N = 116) but not in their wait time coefficients\n> (p = 0.1).\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(2003)\nfor label, taus, bi in ((\"9 back (Methods)\", tau_i9, b_i9), (\"10 back (Figure2.m)\", tau_i10, b_i10)):\n    first = taus < np.percentile(taus, 20); last = taus > np.percentile(taus, 80)\n    print(f\"{label}: fast {first.sum()} rats, slow {last.sum()} rats, N = {first.sum() + last.sum()}\")\n    for name, betas in ((\"initiation\", bi), (\"wait\", b_wt)):\n        obs, p = w.tau_shuffle_test(first, last, betas, 500, rng)\n        obs_c, p_c = w.tau_shuffle_test(first, last, betas, 500, rng, consistent=True)\n        print(f\"   {name} coefficients: tau difference {obs:.3f}, p = {p:.3f}; with the observed groups fit as the \"\n              f\"shuffled ones, {obs_c:.3f}, p = {p_c:.3f}\")\n\"\"\", [\"claim:fig2gh-fast-slow-groups\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** By the code's test, the fast and slow groups (58 and 59 rats) do not\ndiffer in their initiation time coefficients (p = 0.27) and differ in their wait time\ncoefficients (p = 0.0); with the paper's 116 rats as the group size the counts match. Under the\ncode's own scaling the observed tau and the shuffled ones are fit differently, and fitting them\nalike gives initiation p = 0.0 and wait p = 0.0.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig2j-wait-time-previous-reward\n\n> For most rats (253 of 291), wait times for 20 uL in mixed blocks did not differ with the previous\n> reward offer; 38 rats had p < 0.05, and the population p = 0.8.\n\n## fig2k-initiation-previous-reward\n\n> For 89% of rats (256 of 291) trial initiation times in mixed blocks were modulated by the\n> previous reward (p < 0.05 each); population p = 1.84e-49.\n\n## fig2l-sensitivity-differs\n\n> Sensitivity to the previous offer is larger for trial initiation times than for wait times\n> (p = 6.21e-38, two-tailed signed-rank test, N = 291).\n\"\"\")\n\ncode(r\"\"\"\npw_ = np.array([w.wait_by_previous_offer(rats[r]) for r in names])\nprint(f\"Wait time, 20 uL catch trials in mixed blocks: rats with p < 0.05: {np.sum(pw_[:, 2] < 0.05)} (expected 38 +- 3.8)\")\nprint(f\"Population, rank-sum of per-rat means (legend): p = {w.ranksum(pw_[:, 0], pw_[:, 1]):.3g}; \"\n      f\"signed-rank (Figure2.m, variant): p = {w.signrank(pw_[:, 0], pw_[:, 1]):.3g}\")\nprint(f\"Mean z after offers below 20: {np.nanmean(pw_[:, 0]):.3f}, above 20: {np.nanmean(pw_[:, 1]):.3f}\")\nprint(\"Trials per rat in the test, below/above:\", end=\" \")\ncnt = []\nfor r in names:\n    A = rats[r]; idx = np.flatnonzero((A[\"reward\"] == 20) & (A[\"block\"] == 1) & A[\"optout\"] & A[\"catch\"]); idx = idx[idx > 0]\n    cnt.append((np.sum(A[\"reward\"][idx - 1] < 20), np.sum(A[\"reward\"][idx - 1] > 20)))\ncnt = np.array(cnt); print(\"median\", np.median(cnt, 0).tolist(), \"; fewest\", cnt.min(0).tolist())\n\"\"\", [\"claim:fig2j-wait-time-previous-reward\"])\n\nmd(r\"\"\"\n**Result: reproduced.** 38 rats have p < 0.05, the paper's count, and the population test finds\nno effect (rank-sum p = 0.71; the code's signed-rank p = 0.81, the paper's 0.8).\n\"\"\")\n\ncode(r\"\"\"\npi20 = np.array([w.initiation_by_previous_offer(rats[r], True) for r in names])\npiall = np.array([w.initiation_by_previous_offer(rats[r], False) for r in names])\nfor label, arr in ((\"trials offering 20 uL (Methods)\", pi20), (\"all mixed-block trials (Figure2.m, variant)\", piall)):\n    print(f\"{label}: rats with p < 0.05: {np.sum(arr[:, 2] < 0.05)} (expected 256 +- 25.6); slower after offers below 20 in \"\n          f\"{np.sum(arr[:, 0] > arr[:, 1])} rats\")\n    print(f\"   population rank-sum (legend): p = {w.ranksum(arr[:, 0], arr[:, 1]):.3g}; signed-rank: p = {w.signrank(arr[:, 0], arr[:, 1]):.3g}\")\nnc = np.array([w.initiation_by_previous_offer(no_cue[r], True) for r in names])\nprint(f\"Variant without pre-cue sessions, 20 uL trials: {np.sum(nc[:, 2] < 0.05)} rats with p < 0.05\")\n\"\"\", [\"claim:fig2k-initiation-previous-reward\"])\n\nmd(r\"\"\"\n**Result: reproduced.** On trials offering 20 uL, as the Methods state, 265 rats have p < 0.05\n(within 256 +- 25.6) and the population rank-sum test finds slower initiation after offers below\n20 uL (p = 1.3e-47). The code's reading, all mixed-block trials, gives 255 rats and the paper's\np = 1.84e-49 by signed rank.\n\"\"\")\n\ncode(r\"\"\"\nsens_wt = pw_[:, 0] - pw_[:, 1]\nfor label, arr in ((\"20 uL trials (Methods)\", pi20), (\"all mixed-block trials (code, variant)\", piall)):\n    sens_i = arr[:, 0] - arr[:, 1]\n    print(f\"{label}: sensitivity median, initiation {np.nanmedian(sens_i):.3f}, wait {np.nanmedian(sens_wt):.3f}; \"\n          f\"signed-rank p = {w.signrank(sens_i, sens_wt):.3g}; initiation larger in {np.sum(sens_i > sens_wt)} rats\")\n\"\"\", [\"claim:fig2l-sensitivity-differs\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The sensitivity to the previous offer is larger for initiation than for\nwait times (p = 2.2e-08 on 20 uL trials; with the code's all mixed-block trials p = 6.1e-38, the\npaper's 6.21e-38).\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig3c-catch-probability\n\n> Wait times in mixed blocks depend in a graded way on the catch probability; the cohorts held 3,\n> 183, 61, 151 and 39 rats at catch probabilities 0.1, 0.15, 0.2, 0.25 and 0.35.\n\"\"\")\n\ncode(r\"\"\"\nPROBS = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35]\nby_p, n_with, n_any = {}, {}, {}\nfor p in PROBS:\n    m = []\n    for r in names:\n        A = rats[r]; keep = np.arange(len(A[\"reward\"])) >= 1000\n        use = (A[\"block\"] == 1) & (A[\"prob_catch\"] == p) & A[\"catch\"] & keep\n        m.append([np.nanmean(A[\"wait_time\"][use & (A[\"reward\"] == v)]) if (use & (A[\"reward\"] == v)).any() else np.nan\n                  for v in w.STANDARD_VOLUMES])\n    m = np.array(m)\n    by_p[p] = m\n    n_with[p] = int(np.sum(np.any(~np.isnan(m), 1)))\n    n_any[p] = int(np.sum([np.any(rats[r][\"prob_catch\"] == p) for r in names]))\ntable = pd.DataFrame({\"rats (code's selection)\": n_with, \"rats with any trial\": n_any,\n                      \"paper\": {0.1: 3, 0.15: 183, 0.2: 61, 0.25: 151, 0.3: None, 0.35: 39},\n                      \"mean wait (s), over rewards\": {p: np.nanmean(np.nanmean(by_p[p], 0)) for p in PROBS}})\nfor i, v in enumerate(w.STANDARD_VOLUMES):\n    table[f\"{v} uL\"] = [np.nanmean(by_p[p][:, i]) for p in PROBS]\nprint(table.round(2).to_string())\nmeans = [np.nanmean(np.nanmean(by_p[p], 0)) for p in (0.15, 0.2, 0.25, 0.35)]\nprint(\"Strictly falling from 0.15 to 0.2 to 0.25 to 0.35:\", bool(np.all(np.diff(means) < 0)))\n# Within rats that had two probabilities: paired comparison of mean wait (all rewards) at 0.15 and 0.25.\npair = [(np.nanmean(by_p[0.15][i]), np.nanmean(by_p[0.25][i])) for i in range(len(names))\n        if np.any(~np.isnan(by_p[0.15][i])) and np.any(~np.isnan(by_p[0.25][i]))]\npair = np.array(pair)\nprint(f\"Rats with both 0.15 and 0.25: {len(pair)}; shorter at 0.25 in {np.sum(pair[:, 1] < pair[:, 0])}, \"\n      f\"signed-rank p = {w.signrank(pair[:, 1], pair[:, 0]):.3g}\")\n\"\"\", [\"claim:fig3c-catch-probability\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** The rat counts per catch probability (6, 169, 66, 158 and 132 by the\ncode's selection) match the paper's for 0.15, 0.2 and 0.25 but not for 0.1 (3) or 0.35 (39), and\nthe mean wait time does not fall steadily with catch probability (8.3, 6.8, 7.0 and 7.4 s at\n0.15, 0.2, 0.25 and 0.35). Within the rats that had both 0.15 and 0.25, waits are shorter at\n0.25 in most rats. The files also hold a probability of 0.3 for 25 rats, which the paper does not list.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig3j-model-comparison\n\n> Wait times are better fit by the inferential model, which uses hidden state inference, than by\n> the retrospective model (BIC, p = 1.07e-37, two-tailed signed-rank test, N = 291).\n\n## figs9-misinference\n\n> Wait times for 20 uL are shorter when the inferential model infers a high block than when it\n> infers a low block (p << 0.001, signed-rank test, N = 291).\n\n## fig3l-inference-quality\n\n> Rats with good and poor inference (lambda above the 80th or below the 20th percentile) differ in\n> wait time dynamics at transitions from mixed into low or high blocks, but not in trial\n> initiation time dynamics.\n\nThe models are fit per rat in four processes; each rat's random starts come from its own\ngenerator, seeded from the claim's seed and the rat's index.\n\"\"\")\n\ncode(r\"\"\"\nALPHAS = np.geomspace(1e-3, 1, 40)\nLAMBDAS = np.linspace(0, 1, 11)\n\ndef fit_rat(item):\n    M, seed = item\n    rng = np.random.default_rng(seed)\n    b = w.beliefs(M)\n    inferred = b.argmax(1)\n    p_inf, nll_inf = w.fit_inferential(M, inferred, rng, starts=20)\n    p_ret, nll_ret = w.fit_retrospective(M, b[:, 0], ALPHAS)\n    lam_b = w.beliefs(M, LAMBDAS)\n    lam_nll = [w.fit_inferential(M, lam_b[k].argmax(1), rng, starts=0, x0=p_inf)[1] for k in range(len(LAMBDAS))]\n    return {\"p_inf\": p_inf, \"nll_inf\": nll_inf, \"p_ret\": p_ret, \"nll_ret\": nll_ret, \"lam_nll\": np.array(lam_nll),\n            \"inferred\": inferred, \"n_fit\": int(M[\"fitted\"].sum()), \"n_trials\": M[\"n_trials\"]}\n\nstarted = time.time()\ninputs = {r: w.model_inputs(rats[r]) for r in names}\nseeds = np.random.SeedSequence(2004).spawn(len(names))\nwith ProcessPoolExecutor(4) as pool:\n    fits = dict(zip(names, pool.map(fit_rat, [(inputs[r], s) for r, s in zip(names, seeds)], chunksize=4)))\nprint(f\"fit {len(fits)} rats in {time.time() - started:.0f} s\")\n\"\"\", [\"claim:fig3j-model-comparison\", \"claim:figs9-misinference\", \"claim:fig3l-inference-quality\"])\n\ncode(r\"\"\"\nn_fit = np.array([fits[r][\"n_fit\"] for r in names]); n_all = np.array([fits[r][\"n_trials\"] for r in names])\nnll_inf = np.array([fits[r][\"nll_inf\"] for r in names]); nll_ret = np.array([fits[r][\"nll_ret\"] for r in names])\nfor label, n in ((\"n = fitted trials\", n_fit), (\"variant, n = all trials\", n_all)):\n    bic_inf = 4 * np.log(n) + 2 * nll_inf; bic_ret = 2 * np.log(n) + 2 * nll_ret\n    d = bic_ret - bic_inf\n    print(f\"{label}: delta BIC (retrospective - inferential) median {np.median(d):.1f}, range {d.min():.1f} to {d.max():.1f}; \"\n          f\"inferential better in {np.sum(d > 0)} of {len(d)} rats; signed-rank p = {w.signrank(bic_ret, bic_inf):.3g}\")\naic_d = (2 * 2 + 2 * nll_ret) - (2 * 4 + 2 * nll_inf)\nprint(f\"AIC: inferential better in {np.sum(aic_d > 0)} rats, p = {w.signrank(aic_d):.3g}\")\nprint(\"Fitted trials per rat:\", int(n_fit.min()), \"to\", int(n_fit.max()))\np_ret = np.array([fits[r][\"p_ret\"] for r in names])\nprint(\"Retrospective baseline learning rate, median\", np.median(p_ret[:, 0]).round(3), \"; at the grid's ends:\",\n      int(np.sum(p_ret[:, 0] <= ALPHAS[0])), \"low,\", int(np.sum(p_ret[:, 0] >= ALPHAS[-1])), \"high\")\np_inf = np.array([fits[r][\"p_inf\"] for r in names])\nprint(\"Inferential parameters at a bound (1e-4 or 1):\", int(np.sum(np.any((p_inf <= 1.0001e-4) | (p_inf >= 0.9999), 1))), \"rats\")\n\"\"\", [\"claim:fig3j-model-comparison\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The inferential model has the lower BIC in 290 of 291 rats (median\ndifference 312), p = 2.0e-49 by signed rank (paper 1.07e-37); AIC agrees.\n\"\"\")\n\ncode(r\"\"\"\nmis_hi, mis_lo = [], []\nfor r in names:\n    A, f = rats[r], fits[r]\n    good = ~A[\"vios\"]\n    inf = np.full(len(A[\"reward\"]), -1); inf[good] = f[\"inferred\"]\n    sel = (A[\"block\"] == 1) & A[\"catch\"] & (A[\"reward\"] == 20)\n    mis_hi.append(np.nanmean(A[\"wait_time\"][sel & (inf == 1)]) if (sel & (inf == 1)).any() else np.nan)\n    mis_lo.append(np.nanmean(A[\"wait_time\"][sel & (inf == 2)]) if (sel & (inf == 2)).any() else np.nan)\nmis_hi, mis_lo = np.array(mis_hi), np.array(mis_lo)\nok = ~np.isnan(mis_hi - mis_lo)\nprint(f\"Rats with both inferences on 20 uL mixed-block catch trials: {ok.sum()}\")\nprint(f\"Mean wait, inferred high {np.nanmean(mis_hi):.2f} s, inferred low {np.nanmean(mis_lo):.2f} s; shorter when inferred high in \"\n      f\"{np.sum(mis_hi[ok] < mis_lo[ok])} rats; signed-rank p = {w.signrank(mis_hi, mis_lo):.3g}\")\n\"\"\", [\"claim:figs9-misinference\"])\n\nmd(r\"\"\"\n**Result: reproduced.** In mixed blocks, wait times for 20 uL are shorter when the model infers a\nhigh block (mean 7.6 s) than a low block (8.8 s), in 263 of 291 rats, p = 1.6e-37.\n\"\"\")\n\ncode(r\"\"\"\nlam_nll = np.array([fits[r][\"lam_nll\"] for r in names])\nlam = LAMBDAS[lam_nll.argmin(1)]\nprint(\"Fitted lambda, counts per grid value:\", dict(zip(LAMBDAS.round(1), np.bincount(lam_nll.argmin(1), minlength=len(LAMBDAS)))))\nwd30 = {r: w.wait_dynamics(rats[r], 30, 10) for r in names}\nid30 = {r: w.initiation_dynamics(rats[r], 30, 10) for r in names}\nrng = np.random.default_rng(2005)\nresults = []\nfor label, lo_pct, hi_pct in ((\"20th/80th (Methods)\", 20, 80), (\"40th/60th (Figure3.m, variant)\", 40, 60)):\n    lo_g = lam < np.percentile(lam, lo_pct); hi_g = lam > np.percentile(lam, hi_pct)\n    print(f\"{label}: poor inference {lo_g.sum()} rats, good {hi_g.sum()} rats\")\n    for meas, dyn in ((\"wait\", wd30), (\"initiation\", id30)):\n        for kind, tr in ((2, \"mixed to low\"), (1, \"mixed to high\")):\n            arr = np.array([dyn[r][kind] for r in names])\n            diff, p = w.lambda_shuffle_test(arr[lo_g], arr[hi_g], 500, 30, rng)\n            results.append({\"split\": label, \"measure\": meas, \"transition\": tr, \"slope diff\": diff[1], \"p slope\": p[1],\n                            \"right asymptote diff\": diff[0], \"p right asymptote\": p[0]})\nprint(pd.DataFrame(results).round(4).to_string(index=False))\n\"\"\", [\"claim:fig3l-inference-quality\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** Lambda fit on the grid splits the rats as the Methods say, but the\nlogistic fits do not separate the groups as the paper reports: by the code's test, neither the\nwait time slope from mixed to low nor the right asymptote from mixed to high differs at p < 0.05\nbetween rats with good and poor inference, so the wait time part fails.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig3h-dynamic-learning-rate (blocked)\n\n> A retrospective model of trial initiation times needs a learning rate scaled by changes in the\n> inferred block to capture both the slow and fast dynamics at block transitions; a static or\n> RPE-scaled learning rate does not.\n\nBlocked, methods underspecified. The paper did not fit the trial initiation time models; it\nsimulated them with hand-chosen parameters on one rat's trial sequence (Figure3.m, FigureS7.m)\nand judged by eye which captures the dynamics. Neither the paper nor the code states a measure of\n\"capturing\" the dynamics that a test could apply.\n\n## fig4de-overshoot-learning (blocked)\n\nBlocked, data missing. Figure 4d and 4e use the per-session raw structs (`S_Structs`), which hold\nthe sessions of training the processed structs leave out. They are not in the dandiset, which holds\nonly `A_Structs_Final`, nor in the Zenodo deposit, whose zip holds `A_Structs_Final`,\n`A_Structs_all`, `ModelFits` and `ratList.mat` only.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## fig5b-precue-offer\n\n> With the reward cue played before trial initiation, trial initiation times became sensitive to\n> the offered reward.\n\n## fig5c-precue-previous-reward\n\n> In the pre-initiation cue task, trial initiation times for 20 uL in mixed blocks were still\n> modulated by the previous reward (p < 0.05 for 13 of 16 rats; population p = 1.03e-4).\n\n## fig5d-precue-previous-block\n\n> In the pre-initiation cue task, trial initiation times in mixed blocks still depended on the\n> previous block.\n\"\"\")\n\ncode(r\"\"\"\ncue_rats = sorted(r for r in names if rats[r][\"cue\"].any())\ncue_data = {r: w.subset(rats[r], rats[r][\"cue\"]) for r in cue_rats}\norig_data = {r: w.subset(rats[r], ~rats[r][\"cue\"]) for r in cue_rats if (~rats[r][\"cue\"]).any()}\n\ndef offer_slope(A, drop_post_violation):\n    L = w.zscore(w.clean_iti(A[\"iti\"]))\n    use = (A[\"block\"] == 1) & ~np.isnan(L)\n    if drop_post_violation:\n        use &= ~np.r_[False, A[\"vios\"][:-1]]\n    return np.polyfit(np.log2(A[\"reward\"][use]), L[use], 1)[0]\n\nslope_cue = pd.Series({r: offer_slope(cue_data[r], False) for r in cue_rats})\nslope_orig = pd.Series({r: offer_slope(orig_data[r], True) for r in orig_data})\nprint(pd.DataFrame({\"cue sessions\": pd.Series({r: cue_data[r][\"session\"].max() + 1 for r in cue_rats}),\n                    \"slope, cue\": slope_cue, \"slope, original\": slope_orig}).round(3).to_string())\nprint(f\"Cue slopes below zero: {np.sum(slope_cue < 0)} of {len(slope_cue)}, signed-rank p = {w.signrank(slope_cue):.3g}\")\nboth_ = slope_orig.index\nprint(f\"Cue below original, {len(both_)} rats: {np.sum(slope_cue[both_] < slope_orig)}; signed-rank p = \"\n      f\"{w.signrank(slope_cue[both_], slope_orig):.3g}\")\n\"\"\", [\"claim:fig5b-precue-offer\"])\n\nmd(r\"\"\"\n**Result: reproduced.** In cue sessions initiation times fall with the offered volume in all 16\nrats (signed-rank p = 3.1e-05), and for the 12 rats with sessions of the original task the slope\nis steeper in cue sessions than in the original task in all 12 (p = 0.00049).\n\"\"\")\n\ncode(r\"\"\"\ndef precue_previous(data, only_20ul):\n    arr = pd.DataFrame({r: w.initiation_by_previous_offer(data[r], only_20ul) for r in data}, index=[\"below\", \"above\", \"p\"]).T\n    return arr\n\nlate_data = {}\nfor r in cue_rats:\n    A = rats[r]\n    if (~A[\"cue\"]).any():\n        cue_sess = np.unique(A[\"session\"][A[\"cue\"]])\n        keep = A[\"cue\"] & np.isin(A[\"session\"], cue_sess[30:])\n    else:\n        keep = A[\"cue\"]\n    if keep.any():\n        late_data[r] = w.subset(A, keep)\nfor label, data, only in ((\"all cue sessions, 20 uL trials (main)\", cue_data, True),\n                          (\"all cue sessions, all mixed trials (code, variant)\", cue_data, False),\n                          (\"after each switched rat's first 30 cue sessions, 20 uL trials (variant)\", late_data, True)):\n    arr = precue_previous(data, only)\n    print(f\"{label}: {len(arr)} rats; p < 0.05 in {np.sum(arr.p < 0.05)} (expected 13 +- 1.3); slower after offers below 20 in \"\n          f\"{np.sum(arr.below > arr.above)}; population rank-sum p = {w.ranksum(arr.below, arr.above):.3g}, signed-rank p = \"\n          f\"{w.signrank(arr.below, arr.above):.3g}\")\nprint(precue_previous(cue_data, True).round(4).to_string())\n\"\"\", [\"claim:fig5c-precue-previous-reward\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** In all cue sessions, 11 of 16 rats have p < 0.05 on 20 uL\ntrials, outside 13 +- 1.3, while the population rank-sum test finds slower initiation after\noffers below 20 uL (p = 0.00033). The code's reading (all mixed-block trials) gives 14 rats.\n\"\"\")\n\ncode(r\"\"\"\ncue_dyn = {r: w.initiation_dynamics(cue_data[r]) for r in cue_rats}\n_ = transition_summary(cue_dyn, \"Initiation time, cue sessions (fig5d)\")\norig_dyn = {r: w.initiation_dynamics(orig_data[r]) for r in orig_data}\n_ = transition_summary(orig_dyn, \"Same rats, original task (reference)\")\n\"\"\", [\"claim:fig5d-precue-previous-block\"])\n\nmd(r\"\"\"\n**Result: not reproduced**, by the criterion as written. As in fig2b, initiation times in the\nmixed block depend on the previous block with the sign reversed (faster after low blocks), so the\nafter/before ratio is negative; the criterion required the sign to persist.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------\nmd(r\"\"\"\n## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n| Claim | Outcome |\n|---|---|\n| dataset-counts | reproduced |\n| zenodo-link | reproduced |\n| fig1f-wait-time-block | reproduced |\n| fig1i-initiation-block | reproduced |\n| figs2-unrewarded-drive | reproduced |\n| figs12-no-sex-difference | not reproduced |\n| fig2a-wait-time-converges | reproduced |\n| fig2b-initiation-previous-block | not reproduced (criterion's sign) |\n| fig2cd-regression-kernels | reproduced |\n| fig2e-tau-differ | reproduced |\n| fig2f-tau-uncorrelated | reproduced |\n| fig2gh-fast-slow-groups | not reproduced |\n| fig2j-wait-time-previous-reward | reproduced |\n| fig2k-initiation-previous-reward | reproduced |\n| fig2l-sensitivity-differs | reproduced |\n| fig3c-catch-probability | not reproduced |\n| fig3j-model-comparison | reproduced |\n| figs9-misinference | reproduced |\n| fig3l-inference-quality | not reproduced |\n| fig3h-dynamic-learning-rate | blocked (methods underspecified) |\n| fig4a-wait-ratio-learning | see the second notebook |\n| fig4bc-regression-learning | see the second notebook |\n| fig4de-overshoot-learning | blocked (data missing) |\n| fig5b-precue-offer | reproduced |\n| fig5c-precue-previous-reward | partially reproduced |\n| fig5d-precue-previous-block | not reproduced (criterion's sign) |\n\n**How the analysis differs from the paper's.** The paper's per-rat measures are recomputed from\nthe dandiset with the paper's MATLAB code as the guide; where the Methods and the code disagree,\nthe Methods give the main result and the code's choice is shown (z-scored against raw means for\nFigure 1, 9 against 10 previous rewards, 20 uL trials against all mixed-block trials, the\npercentile split of Figure 3l). The models of Figure 3 are refit here: from 20 random starts (the\npaper used 100), on catch-trial wait times with beliefs updated over non-violation trials, which\nthe published code does not show, and with lambda on a grid of 11 values. Exponential and\nlogistic fits use scipy in place of MATLAB's fmincon. The pre-cue claims use the cue sessions the\ndandiset holds, which passed the paper's inclusion criteria, where the paper used all of them.\n\n**What was found about the dandiset.** It holds the paper's processed data for all 291 rats in\nfull, with the same values as the Zenodo structs, plus the raw Bpod events, which agree with the\nprocessed times. Its problems are small: one session deposited twice (L011), the catch\nprobability missing from the processed table (a typo in the conversion), the training stage coded\nas 9 without saying it is the paper's stage 8, ages missing for most rats, sounds stored without\ntheir identity, and the pre-cue sessions of Figure 5 included among the main data with only a task\nargument to mark them.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/001169-mah-2023/reproduce_mah_2023.ipynb\")\nprint(\"written\", len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
$TMPDIR/scratch/bin/python $TMPDIR/build_nb.py && cat > $TMPDIR/run_cells.py <<'EOF'
import nbformat, sys, os, io, contextlib, time
import matplotlib; matplotlib.use("Agg")
nb = nbformat.read("reproduce_mah_2023.ipynb", 4)
start, stop = int(sys.argv[1]), int(sys.argv[2])
g = globals()
d = os.environ["TMPDIR"]
codes = [c for c in nb.cells if c.cell_type == "code"]
for i, c in enumerate(codes):
    if i < start or i >= stop:
        if i == 0:
            src = c.source.split("started = time.time()")[0] + (
                "import pandas as pd\nassets=pd.read_parquet(f'{os.environ[\"TMPDIR\"]}/assets.parquet')\n"
                "sessions_all=pd.read_parquet(f'{os.environ[\"TMPDIR\"]}/sessions.parquet')\n"
                "sessions_all['processed_columns']=sessions_all.cols.str.split(',').map(tuple)\n"
                "trials_all=pd.read_parquet(f'{os.environ[\"TMPDIR\"]}/trials.parquet')\n")
            exec(src, g)
        continue
    t = time.time()
    print(f"===== cell {i} {c.metadata.get('tags')}")
    exec(c.source, g)
    print(f"----- {time.time()-t:.0f} s")
EOF
echo ok
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 2, in <module>
    import nbformat as nbf
ModuleNotFoundError: No module named 'nbformat'
ok
```

**Agent calls Bash**

```bash
python $TMPDIR/build_nb.py && VIRTUAL_ENV=$TMPDIR/scratch uv pip install -q nbformat 2>&1|tail -1; cat > $TMPDIR/run_cells.py <<'EOF'
import nbformat, sys, os, time
import matplotlib; matplotlib.use("Agg")
nb = nbformat.read("reproduce_mah_2023.ipynb", 4)
stop = int(sys.argv[1]) if len(sys.argv) > 1 else 999
g = globals()
codes = [c for c in nb.cells if c.cell_type == "code"]
for i, c in enumerate(codes[:stop]):
    src = c.source
    if i == 0:
        src = src.split("started = time.time()")[0] + (
            "assets=pd.read_parquet(f'{os.environ[\"TMPDIR\"]}/assets.parquet')\n"
            "sessions_all=pd.read_parquet(f'{os.environ[\"TMPDIR\"]}/sessions.parquet')\n"
            "sessions_all['processed_columns']=sessions_all.cols.str.split(',').map(tuple)\n"
            "trials_all=pd.read_parquet(f'{os.environ[\"TMPDIR\"]}/trials.parquet')\n")
    t = time.time()
    print(f"===== cell {i} {c.metadata.get('tags')}", flush=True)
    exec(src, g)
    print(f"----- {time.time()-t:.0f} s", flush=True)
EOF
PYTHONPATH=. timeout 3000 $TMPDIR/scratch/bin/python $TMPDIR/run_cells.py 2>&1 | tee $TMPDIR/run1.log | grep -v "^$" | head -400
```

```
written 75 cells
===== cell 0 None
----- 4 s
===== cell 1 ['sanity']
Assets: 23034 ; all NWB: True
Subjects (folders): 291 ; subject ids in files: 291
Sessions: 23034 ; trials: 10408925
Species in files: ['Rattus norvegicus']
Sex per rat: {'M': 184, 'F': 107}
Protocol per session: {'RWTautowait2': 22943, 'RWTautowait': 86, 'RWTautowaitWP': 5}
Training stage values in processed trials: {9: 10408925}
Subjects with an age in the files: 16 of 291
Processed and raw trial tables have the same length in every file: True
Columns of processed_trials (same in every file): True
   ['block_type', 'id', 'inter_trial_interval', 'is_catch', 'is_opt_out', 'is_rewarded', 'is_violation', 'nose_in_center', 'num_trials_in_adaptation_blocks', 'num_trials_in_mixed_blocks', 'reward_delay', 'reward_volume_ul', 'rewarded_port', 'start_time', 'stop_time', 'training_stage', 'wait_for_center_poke', 'wait_time', 'wait_time_threshold', 'wait_time_unthresholded', 'z_scored_wait_for_center_poke']
Session start times: 2019-09-27 17:54:02+00:00 to 2023-07-22 17:15:27+00:00
----- 0 s
===== cell 2 ['sanity']
Sessions identical to another of the same rat (removed):
subject_id                   session_id  n_trials                                                   path
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
s=s.replace('''def raw_check(row):
    content = requests.get(row.url, timeout=120).content''','''def raw_check(item):
    session_id, url = item
    content = requests.get(url, timeout=120).content''')
s=s.replace('''return {"session": row.session_id,''','''return {"session": session_id,''')
s=s.replace('''checks = pd.DataFrame(list(pool.map(raw_check, sample.itertuples())))''','''checks = pd.DataFrame(list(pool.map(raw_check, zip(sample.session_id, sample.url))))''')
s=s.replace('''print("\\nCatch probability (raw trials, catch_percentage):", trials.catch_percentage.round(3).value_counts().sort_index().to_dict())
print("Catch trials by catch probability, share of trials:",
      trials.groupby(trials.catch_percentage.round(2)).is_catch.mean().round(3).to_dict())''','''pc = trials.catch_percentage.astype(float).round(3)
print("\\nCatch probability (raw trials, catch_percentage):", pc.value_counts().sort_index().to_dict())
print("Share of catch trials at each catch probability:", trials.is_catch.groupby(pc).mean().round(3).to_dict())''')
s=s.replace('''print("kept:", kept_twin[["subject_id", "session_id", "n_trials", "path"]].to_string(index=False, header=False))''','''print("Kept:")
print(kept_twin[["subject_id", "session_id", "n_trials", "path"]].to_string(index=False))''')
open(p,'w').write(s)
EOF
grep -n "raw_check\|pc = trials" $TMPDIR/build_nb.py | head
```

```
181:pc = trials.catch_percentage.astype(float).round(3)
223:def raw_check(item):
253:    checks = pd.DataFrame(list(pool.map(raw_check, zip(sample.session_id, sample.url))))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001169-mah-2023 && python $TMPDIR/build_nb.py && PYTHONPATH=. timeout 3500 $TMPDIR/scratch/bin/python $TMPDIR/run_cells.py 2>&1 | tee $TMPDIR/run1.log | grep -v "^$" | sed -n '/cell 5/,$p' | head -300
```

```
written 75 cells
===== cell 5 ['sanity']
                     session  same_trial_starts  n_iti  max_abs_iti_diff_s  n_optout  max_abs_wait_diff_s
RWTautowait2-20230710-144305               True    315        4.485301e-13        93         1.532700e+00
RWTautowait2-20210317-114013               True    335        2.905726e-11        50         5.448086e-11
RWTautowait2-20220404-135343               True    140        4.547474e-13        59         1.208400e+00
RWTautowait2-20201007-153038               True    229        5.811529e-11        53         8.120971e-11
RWTautowait2-20220407-134314               True    175        3.907985e-13        48         1.984800e+00
RWTautowait2-20210920-102823               True    202        4.540257e-13        32         3.265200e+00
RWTautowait2-20230717-145206               True    405        8.906209e-13        99         3.981630e+01
RWTautowait2-20221020-155919               True    199        4.547474e-13       108         4.353300e+00
RWTautowait2-20221025-135215               True    128        1.971756e-13        31         1.246600e+00
RWTautowait2-20220825-134110               True    362        3.899103e-13       103         8.342600e+00
RWTautowait2-20230720-094603               True    169        3.410605e-13        49         1.341500e+00
RWTautowait2-20220523-114505               True    210        4.218847e-13        57         1.130470e+01
RWTautowait2-20220608-100746               True    144        4.451994e-13        26         7.460699e-13
RWTautowait2-20230418-122257               True    246        4.380385e-13        56         8.890000e-02
RWTautowait2-20221216-161212               True    423        4.547474e-13        59         7.538000e-01
RWTautowait2-20221216-104100               True    133        4.263256e-13        30         1.272800e+00
RWTautowait2-20220405-100635               True    198        3.885347e-13        47         1.379000e+00
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t5.py <<'EOF'
import pandas as pd, numpy as np, os, h5py, io, requests
d=os.environ['TMPDIR']
S=pd.read_parquet(f'{d}/sessions.parquet'); A=pd.read_parquet(f'{d}/assets.parquet')
row=S[S.session_id=='RWTautowait2-20210727-103222'].merge(A,on='path').iloc[0]
f=h5py.File(io.BytesIO(requests.get(row.url).content),'r')
rec=f["acquisition/task_recording"]
st_names=np.array([x.decode() for x in f["general/task/state_types/state_name"][:]])
states=pd.DataFrame({"name": st_names[rec["states/state_type"][:]], "start": rec["states/start_time"][:], "stop": rec["states/stop_time"][:]})
tstart=f["intervals/trials/start_time"][:]
g=f["intervals/processed_trials"]; proc=pd.DataFrame({k:g[k][:] for k in ['wait_time_unthresholded','is_opt_out','is_catch','is_rewarded','reward_delay']})
states['trial']=np.searchsorted(tstart,states.start.values,side='right')-1
side=states[states.name=='wait_for_side_poke'].groupby('trial').start.first(); opt=states[states.name=='opt_out'].groupby('trial').start.first()
dd=(opt-side).dropna(); diff=dd-proc.wait_time_unthresholded.values[dd.index]
bad=diff[np.abs(diff)>0.01]
print(len(dd), len(bad))
for t in bad.index[:3]:
    print(t, proc.iloc[t].to_dict(), 'diff', bad[t])
    print(states[states.trial==t][['name','start','stop']].assign(rel=lambda x: x.start-side[t]).to_string())
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t5.py
```

```
104 7
4 {'wait_time_unthresholded': 2.6426999999999907, 'is_opt_out': True, 'is_catch': False, 'is_rewarded': False, 'reward_delay': 2.6426521364306494} diff 83.99279999997486
                  name        start         stop       rel
12       wait_for_poke  599074.2299  599527.8675 -454.6685
13      nose_in_center  599527.8675  599528.8964   -1.0309
14              go_cue  599528.8964  599528.8984   -0.0020
15  wait_for_side_poke  599528.8984  599531.5411    0.0000
16     announce_reward  599531.5411  599615.5339    2.6427
17             opt_out  599615.5339  599615.7339   86.6355
18          stop_sound  599615.7339  599615.7340   86.8355
26 {'wait_time_unthresholded': 3.3155, 'is_opt_out': True, 'is_catch': False, 'is_rewarded': False, 'reward_delay': 3.315488778894031} diff 5.6524000000469385
                   name        start         stop     rel
130       wait_for_poke  599958.5022  599959.0201 -1.6072
131      nose_in_center  599959.0201  599960.1074 -1.0893
132              go_cue  599960.1074  599960.1094 -0.0020
133  wait_for_side_poke  599960.1094  599963.4249  0.0000
134     announce_reward  599963.4249  599969.0773  3.3155
135             opt_out  599969.0773  599969.2773  8.9679
136          stop_sound  599969.2773  599969.2774  9.1679
37 {'wait_time_unthresholded': 8.962000000000002, 'is_opt_out': True, 'is_catch': False, 'is_rewarded': False, 'reward_delay': 8.961979562766004} diff 1.20540000003483
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='wagering.py'
s=open(p).read()
start=s.index('def load_zenodo_structs')
s=s[:start]+'''def _get_range(url: str, first: int, last: int) -> bytes:
    """Bytes first to last (inclusive) of a URL, retrying when the server asks to slow down."""
    import time
    for attempt in range(8):
        r = requests.get(url, headers={"Range": f"bytes={first}-{last}"}, timeout=600)
        if r.status_code == 206:
            return r.content
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(float(r.headers.get("Retry-After", 10 * (attempt + 1))))
            continue
        r.raise_for_status()
        raise IOError(f"range request answered with status {r.status_code}")
    raise IOError(f"range request failed after retries: {url}")


def load_zenodo_structs(folder: str) -> dict[str, dict]:
    """The per-rat structs in `published/<folder>/` of Zenodo 10.5281/zenodo.10031483. The zip's
    directory is read first; the members of the folder, which lie together in the archive,
    are then read with one range request and decompressed in memory."""
    import struct
    import zipfile
    import zlib

    import scipy.io as sio

    head = requests.head(ZENODO_URL, allow_redirects=True, timeout=60)
    size = int(head.headers["Content-Length"])
    tail = _get_range(ZENODO_URL, size - 65536, size - 1)
    eocd = tail.rfind(b"PK\\x05\\x06")
    cd_size, cd_offset = struct.unpack("<II", tail[eocd + 12:eocd + 20])
    if cd_offset == 0xFFFFFFFF:          # zip64: read the zip64 end record through its locator
        loc = tail.rfind(b"PK\\x06\\x07")
        z64 = struct.unpack("<Q", tail[loc + 8:loc + 16])[0]
        rec = _get_range(ZENODO_URL, z64, z64 + 55)
        cd_size, cd_offset = struct.unpack("<QQ", rec[40:56])
    directory = _get_range(ZENODO_URL, cd_offset, cd_offset + cd_size - 1)
    archive = zipfile.ZipFile.__new__(zipfile.ZipFile)
    members = []
    pos = 0
    while pos < len(directory) and directory[pos:pos + 4] == b"PK\\x01\\x02":
        (method, csize, usize, nlen, xlen, clen, offset) = (
            struct.unpack("<H", directory[pos + 10:pos + 12])[0],
            *struct.unpack("<II", directory[pos + 20:pos + 28]),
            *struct.unpack("<HHH", directory[pos + 28:pos + 34]),
            struct.unpack("<I", directory[pos + 42:pos + 46])[0])
        name = directory[pos + 46:pos + 46 + nlen].decode()
        extra = directory[pos + 46 + nlen:pos + 46 + nlen + xlen]
        if 0xFFFFFFFF in (csize, usize, offset):   # zip64 sizes and offset in the extra field
            i = 0
            while i < len(extra):
                tag, ln = struct.unpack("<HH", extra[i:i + 4])
                if tag == 1:
                    vals = list(struct.unpack("<" + "Q" * (ln // 8), extra[i + 4:i + 4 + ln]))
                    if usize == 0xFFFFFFFF:
                        usize = vals.pop(0)
                    if csize == 0xFFFFFFFF:
                        csize = vals.pop(0)
                    if offset == 0xFFFFFFFF:
                        offset = vals.pop(0)
                i += 4 + ln
        if name.startswith(f"published/{folder}/ratTrial_") and name.endswith(".mat"):
            members.append((name, method, csize, offset))
        pos += 46 + nlen + xlen + clen
    del archive
    first = min(m[3] for m in members)
    last = max(m[3] + m[2] for m in members) + 1024
    blob = _get_range(ZENODO_URL, first, min(last, size - 1))
    out = {}
    for name, method, csize, offset in sorted(members):
        h = offset - first
        nlen, xlen = struct.unpack("<HH", blob[h + 26:h + 30])
        data = blob[h + 30 + nlen + xlen:h + 30 + nlen + xlen + csize]
        raw = zlib.decompress(data, -15) if method == 8 else data
        A = sio.loadmat(io.BytesIO(raw), simplify_cells=True)["A"]
        out[name.split("ratTrial_")[1][:-4]] = {k: np.asarray(A[k]) for k in STRUCT_FIELDS if k in A}
    return out
'''
open(p,'w').write(s)
EOF
cat > $TMPDIR/t6.py <<'EOF'
import time, wagering as w
t=time.time(); s=w.load_zenodo_structs("A_Structs_Final"); print(len(s), time.time()-t, list(s['L011'].keys()))
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t6.py
```

```
291 99.88226008415222 ['reward', 'block', 'catch', 'vios', 'hits', 'optout', 'wait_time', 'ITI', 'prob_catch', 'ntrials', 'wait_thresh']
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='wagering.py'
s=open(p).read()
s=s.replace("    archive = zipfile.ZipFile.__new__(zipfile.ZipFile)\n","").replace("    del archive\n","").replace("    import zipfile\n","")
open(p,'w').write(s)
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
s=s.replace('''    side = states[states.name == "wait_for_side_poke"]; opt = states[states.name == "opt_out"]
    side = pd.Series(side.start.to_numpy(), index=trial_of(side.start.to_numpy())).groupby(level=0).first()
    opt = pd.Series(opt.start.to_numpy(), index=trial_of(opt.start.to_numpy())).groupby(level=0).first()
    waited = (opt - side).dropna()''','''    side = states[states.name == "wait_for_side_poke"]; opt = states[states.name == "opt_out"]
    side = pd.Series(side.start.to_numpy(), index=trial_of(side.start.to_numpy())).groupby(level=0).first()
    opt = pd.Series(opt.start.to_numpy(), index=trial_of(opt.start.to_numpy())).groupby(level=0).first()
    waited = (opt - side).dropna()
    waited = waited[proc["is_catch"][waited.index.to_numpy()]]   # catch trials: the rat waited until it opted out''')
s=s.replace('''proc = {k: g[k][:] for k in ("inter_trial_interval", "wait_time_unthresholded", "is_rewarded", "start_time")}''','''proc = {k: g[k][:] for k in ("inter_trial_interval", "wait_time_unthresholded", "is_rewarded", "is_catch", "start_time")}''')
s=s.replace('''"n_optout": len(d_wt), "max_abs_wait_diff_s"''','''"n_catch_optout": len(d_wt), "max_abs_wait_diff_s"''')
s=s.replace('''processed wait time of an opt-out trial equals the time from the side light''','''processed wait time of a catch trial equals the time from the side light''')
open(p,'w').write(s)
EOF
grep -n "is_catch\"\]\[waited" $TMPDIR/build_nb.py
```

```
246:    waited = waited[proc["is_catch"][waited.index.to_numpy()]]   # catch trials: the rat waited until it opted out
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/run_cells.py'
s=open(p).read()
s=s.replace('''            "trials_all=pd.read_parquet(f'{os.environ[\\"TMPDIR\\"]}/trials.parquet')\\n")''','''            "trials_all=pd.read_parquet(f'{os.environ[\\"TMPDIR\\"]}/trials.parquet')\\n"
            "import pickle\\n_orig=w.load_zenodo_structs\\n"
            "def _cached(folder):\\n"
            "    fn=f'{os.environ[\\"TMPDIR\\"]}/z_{folder}.pkl'\\n"
            "    if os.path.exists(fn): return pickle.load(open(fn,'rb'))\\n"
            "    s=_orig(folder); pickle.dump(s,open(fn,'wb')); return s\\n"
            "w.load_zenodo_structs=_cached\\n")''')
open(p,'w').write(s)
EOF
grep -n "_cached" $TMPDIR/run_cells.py | head -3; python $TMPDIR/build_nb.py && PYTHONPATH=. timeout 3500 $TMPDIR/scratch/bin/python $TMPDIR/run_cells.py 2>&1 | tee $TMPDIR/run1.log | grep -v "^$" | sed -n '/cell 5/,$p' | head -400
```

```
16:            "def _cached(folder):\n"
20:            "w.load_zenodo_structs=_cached\n")
written 75 cells
===== cell 5 ['sanity']
                     session  same_trial_starts  n_iti  max_abs_iti_diff_s  n_catch_optout  max_abs_wait_diff_s
RWTautowait2-20230710-144305               True    315        4.485301e-13              78         5.924150e-13
RWTautowait2-20210317-114013               True    335        2.905726e-11              46         5.448086e-11
RWTautowait2-20220404-135343               True    140        4.547474e-13              51         4.174439e-13
RWTautowait2-20201007-153038               True    229        5.811529e-11              49         8.120971e-11
RWTautowait2-20220407-134314               True    175        3.907985e-13              39         3.552714e-13
RWTautowait2-20210920-102823               True    202        4.540257e-13              27         5.861978e-13
RWTautowait2-20230717-145206               True    405        8.906209e-13              78         9.947598e-13
RWTautowait2-20221020-155919               True    199        4.547474e-13              93         8.490986e-13
RWTautowait2-20221025-135215               True    128        1.971756e-13              26         2.451372e-13
RWTautowait2-20220825-134110               True    362        3.899103e-13              93         6.554757e-13
RWTautowait2-20230720-094603               True    169        3.410605e-13              43         2.469136e-13
RWTautowait2-20220523-114505               True    210        4.218847e-13              45         4.192202e-13
RWTautowait2-20220608-100746               True    144        4.451994e-13              26         7.460699e-13
RWTautowait2-20230418-122257               True    246        4.380385e-13              52         7.673862e-13
RWTautowait2-20221216-161212               True    423        4.547474e-13              47         7.851497e-13
[... 212 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t7.py <<'EOF'
import pickle, os, numpy as np, pandas as pd
d=os.environ['TMPDIR']
Z=pickle.load(open(f'{d}/z_A_Structs_Final.pkl','rb'))
S,rats=pickle.load(open(f'{d}/rats.pkl','rb'))
tot_missing_s=0; tot_missing_t=0
for r in ['G001','G002','G006','G008','G022','J006','M015','M017','S028']:
    nz=np.atleast_1d(Z[r]['ntrials']).astype(int); nd=np.bincount(rats[r]['session'])
    from collections import Counter
    cz,cd=Counter(nz),Counter(nd)
    print(r, len(nz), len(nd), 'only zenodo', sorted((cz-cd).elements()), 'only dandiset', sorted((cd-cz).elements()), 'same multiset', cz==cd)
    if cz==cd:
        # find order differences
        i=np.flatnonzero(nz!=nd)[:6]; print('  first differing positions', i, nz[i], nd[i])
        ss=S[S.subject_id==r].reset_index(drop=True); print(ss.loc[i,['session_id','n_trials']].to_string())
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t7.py
```

```
G001 34 32 only zenodo [np.int64(221), np.int64(387)] only dandiset [] same multiset False
G002 75 75 only zenodo [] only dandiset [] same multiset True
  first differing positions [60 61 62 63 64 65] [309 256 369 286 263 317] [488 309 233 256 369 286]
                      session_id  n_trials
60  RWTautowait2-20200622-102743       488
61  RWTautowait2-20200623-111140       309
62  RWTautowait2-20200625-105735       233
63  RWTautowait2-20200626-101913       256
64  RWTautowait2-20200629-102408       369
65  RWTautowait2-20200630-101726       286
G006 85 85 only zenodo [] only dandiset [] same multiset True
  first differing positions [45 46 47 48 49 50] [451 678 326 501 377 566] [581 468 451 678 326 501]
                      session_id  n_trials
45  RWTautowait2-20200622-131031       581
46  RWTautowait2-20200623-124052       468
47  RWTautowait2-20200624-134840       451
48  RWTautowait2-20200625-123130       678
49  RWTautowait2-20200626-123539       326
50  RWTautowait2-20200629-121819       501
G008 134 134 only zenodo [] only dandiset [] same multiset True
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='wagering.py'
s=open(p).read()
a=s.index('def fit_exp_decay')
b=s.index('def regress_wait_on_rewards')
s=s[:a]+'''def fit_exp_decay(x, y, lower=(-50, -50), upper=(50, 50)) -> np.ndarray:
    """y = a exp(-x / tau) by least squares within bounds, as fit_exp_decay.m. The code uses
    fmincon from 10 random starts; here tau is searched on a grid of 5000 values within its
    bounds with a solved in closed form (and clipped to its bounds) at each, which finds the
    global minimum without random starts. Returns (a, tau)."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = ~np.isnan(y)
    x, y = x[ok], y[ok]
    taus = np.linspace(max(lower[1], 1e-3), upper[1], 5000)
    E = np.exp(-x[None, :] / taus[:, None])
    a = np.clip((E @ y) / np.sum(E ** 2, axis=1), lower[0], upper[0])
    mse = np.mean((y[None, :] - a[:, None] * E) ** 2, axis=1)
    k = int(np.argmin(mse))
    return np.array([a[k], taus[k]])


'''+s[b:]
s=s.replace('def regress_wait_on_rewards(A: dict, nback: int, rng) -> tuple[np.ndarray, float]:','def regress_wait_on_rewards(A: dict, nback: int) -> tuple[np.ndarray, float]:')
s=s.replace('def regress_initiation_on_rewards(A: dict, nback: int, rng) -> tuple[np.ndarray, float]:','def regress_initiation_on_rewards(A: dict, nback: int) -> tuple[np.ndarray, float]:')
s=s.replace('fit = fit_exp_decay(np.arange(1, nback + 1), 10 * b[:nback], rng, 10, (-10, 0), (10, 10))','fit = fit_exp_decay(np.arange(1, nback + 1), 10 * b[:nback], (-10, 0), (10, 10))')
s=s.replace('fit = fit_exp_decay(np.arange(1, nback + 1), b[:nback], rng, 10, (-10, 0), (0, 10))','fit = fit_exp_decay(np.arange(1, nback + 1), b[:nback], (-10, 0), (0, 10))')
s=s.replace('fit_exp_decay(x, 10 * B[g1].mean(0), rng, 10, (-3, 0), (1, 50))','fit_exp_decay(x, 10 * B[g1].mean(0), (-3, 0), (1, 50))')
s=s.replace('fit_exp_decay(x, 10 * B[g2].mean(0), rng, 10, (-3, 0), (1, 50))','fit_exp_decay(x, 10 * B[g2].mean(0), (-3, 0), (1, 50))')
s=s.replace('fit_exp_decay(x, 10 * betas[first][:, :-1].mean(0), rng, 10, (-3, 0), (1, 50))','fit_exp_decay(x, 10 * betas[first][:, :-1].mean(0), (-3, 0), (1, 50))')
s=s.replace('fit_exp_decay(x, 10 * betas[last][:, :-1].mean(0), rng, 10, (-3, 0), (1, 50))','fit_exp_decay(x, 10 * betas[last][:, :-1].mean(0), (-3, 0), (1, 50))')
s=s.replace('fit_exp_decay(x, betas[first][:, :-1].mean(0), rng, 10, (-10, 0), (1, 10))','fit_exp_decay(x, betas[first][:, :-1].mean(0), (-10, 0), (1, 10))')
s=s.replace('fit_exp_decay(x, betas[last][:, :-1].mean(0), rng, 10, (-10, 0), (1, 10))','fit_exp_decay(x, betas[last][:, :-1].mean(0), (-10, 0), (1, 10))')
assert 'rng, 10' not in s.split('def tau_shuffle_test')[1].split('def ')[0]
open(p,'w').write(s)
EOF
grep -n "fit_exp_decay(" wagering.py
```

```
431:def fit_exp_decay(x, y, lower=(-50, -50), upper=(50, 50)) -> np.ndarray:
465:    fit = fit_exp_decay(np.arange(1, nback + 1), 10 * b[:nback], (-10, 0), (10, 10))
488:    fit = fit_exp_decay(np.arange(1, nback + 1), b[:nback], (-10, 0), (0, 10))
508:        t1 = fit_exp_decay(x, 10 * B[g1].mean(0), (-3, 0), (1, 50))[1]
509:        t2 = fit_exp_decay(x, 10 * B[g2].mean(0), (-3, 0), (1, 50))[1]
512:        t1 = fit_exp_decay(x, 10 * betas[first][:, :-1].mean(0), (-3, 0), (1, 50))[1]
513:        t2 = fit_exp_decay(x, 10 * betas[last][:, :-1].mean(0), (-3, 0), (1, 50))[1]
515:        t1 = fit_exp_decay(x, betas[first][:, :-1].mean(0), (-10, 0), (1, 10))[1]
516:        t2 = fit_exp_decay(x, betas[last][:, :-1].mean(0), (-10, 0), (1, 10))[1]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
s=s.replace('''rng = np.random.default_rng(2002)
started = time.time()
reg_wt = [w.regress_wait_on_rewards(rats[r], 10, rng) for r in names]
reg_i9 = [w.regress_initiation_on_rewards(rats[r], 9, rng) for r in names]
reg_i10 = [w.regress_initiation_on_rewards(rats[r], 10, rng) for r in names]''','''started = time.time()
reg_wt = [w.regress_wait_on_rewards(rats[r], 10) for r in names]
reg_i9 = [w.regress_initiation_on_rewards(rats[r], 9) for r in names]
reg_i10 = [w.regress_initiation_on_rewards(rats[r], 10) for r in names]''')
# zenodo link
a=s.index('FIELDS = {"reward": "volume"')
b=s.index('""", ["claim:zenodo-link"])')
s=s[:a]+'''FIELDS = {"reward": "volume", "block": "block", "catch": "catch", "vios": "vios", "hits": "hits",
          "optout": "optout", "wait_time": "wait_time", "ITI": "iti", "prob_catch": "prob_catch"}

def session_keys(arrays, bounds):
    # One key per session: its trial count and the values of every compared field, rounded.
    keys = []
    for a, b in zip(bounds[:-1], bounds[1:]):
        parts = [str(b - a)]
        for f in arrays:
            v = np.round(np.asarray(f[a:b], float), 3)
            parts.append(np.nan_to_num(v, nan=-999).tobytes().hex())
        keys.append("|".join(parts))
    return keys

rows = []
for r in sorted(set(structs) | set(names)):
    Z, A = structs.get(r), rats.get(r)
    row = {"rat": r, "in_zenodo": Z is not None, "in_dandiset": A is not None}
    if Z is not None and A is not None:
        nt_z = np.atleast_1d(Z["ntrials"]).astype(int)
        nt_d = np.bincount(A["session"])
        kz = session_keys([np.asarray(Z[f], float).ravel() for f in FIELDS], np.r_[0, np.cumsum(nt_z)])
        kd = session_keys([A[f].astype(float) for f in FIELDS.values()], np.r_[0, np.cumsum(nt_d)])
        cz, cd = pd.Series(kz).value_counts(), pd.Series(kd).value_counts()
        only_z = int((cz.sub(cd, fill_value=0) > 0).sum()); only_d = int((cd.sub(cz, fill_value=0) > 0).sum())
        missing_trials = int(sum(int(k.split("|")[0]) * int(n) for k, n in cz.sub(cd, fill_value=0).items() if n > 0))
        row.update(sessions_zenodo=len(nt_z), sessions_dandiset=len(nt_d),
                   same_order=bool(kz == kd), same_set=bool(only_z == 0 and only_d == 0),
                   only_zenodo=only_z, only_dandiset=only_d, trials_only_zenodo=missing_trials)
    rows.append(row)
link = pd.DataFrame(rows)
print("Rats in both:", int((link.in_zenodo & link.in_dandiset).sum()), "; only Zenodo:", link[~link.in_dandiset].rat.tolist(),
      "; only dandiset:", link[~link.in_zenodo].rat.tolist())
print("Rats whose sessions match in order, trial counts and every compared value (criterion):", int(link.same_order.sum()))
print("Rats whose sessions match as a set, ignoring order:", int(link.same_set.sum()))
print("\\nRats that differ:")
print(link[~link.same_order][["rat", "sessions_zenodo", "sessions_dandiset", "same_set", "only_zenodo", "only_dandiset",
                               "trials_only_zenodo"]].to_string(index=False))
print("\\nSessions on Zenodo with no identical session in the dandiset:", int(link.only_zenodo.sum()),
      f"({int(link.trials_only_zenodo.sum())} trials, {link.trials_only_zenodo.sum() / sum(len(np.asarray(z['reward']).ravel()) for z in structs.values()):.5f} of all);",
      "sessions in the dandiset with no identical one on Zenodo:", int(link.only_dandiset.sum()))
'''+s[b:]
s=s.replace('''# The structs before the duplicate was removed: does L011 have 205 sessions on Zenodo?
nz = len(np.atleast_1d(structs["L011"]["ntrials"]))
print("L011 sessions on Zenodo:", nz, "; in the dandiset with the duplicate:", int((sessions_all.subject_id == "L011").sum()))''','''nz = len(np.atleast_1d(structs["L011"]["ntrials"]))
print("L011 sessions on Zenodo:", nz, "; in the dandiset with the duplicate:", int((sessions_all.subject_id == "L011").sum()))
# Where the order differs: the sessions of the dandiset in start-time order, against the structs' order.
for r in link[(~link.same_order) & link.same_set].rat:
    nt_z = np.atleast_1d(structs[r]["ntrials"]).astype(int); nt_d = np.bincount(rats[r]["session"])
    i = int(np.flatnonzero(nt_z != nt_d)[0])
    ss = sessions[sessions.subject_id == r].reset_index(drop=True)
    moved = ss[ss.n_trials == nt_d[i]].session_id.tolist()
    print(f"{r}: first different position {i}; the dandiset's session there ({moved[0]}, {nt_d[i]} trials) is at position "
          f"{int(np.flatnonzero(nt_z == nt_d[i])[0])} in the struct")''')
# fig3l
a=s.index('''lam_nll = np.array([fits[r]["lam_nll"] for r in names])''')
b=s.index('''""", ["claim:fig3l-inference-quality"])''')
s=s[:a]+'''lam_nll = np.array([fits[r]["lam_nll"] for r in names])
lam = LAMBDAS[lam_nll.argmin(1)]
print("Fitted lambda, rats per grid value:", dict(zip(LAMBDAS.round(1).tolist(), np.bincount(lam_nll.argmin(1), minlength=len(LAMBDAS)).tolist())))
wd30 = {r: w.wait_dynamics(rats[r], 30, 10) for r in names}
id30 = {r: w.initiation_dynamics(rats[r], 30, 10) for r in names}

def shuffle_job(job):
    lo_rows, hi_rows, seed = job
    return w.lambda_shuffle_test(lo_rows, hi_rows, 500, 30, np.random.default_rng(seed))

jobs, labels = [], []
splits = (("20th/80th (Methods), ties at the cut included", 20, 80), ("40th/60th (Figure3.m, variant)", 40, 60))
for k, (label, lo_pct, hi_pct) in enumerate(splits):
    lo_g = lam <= np.percentile(lam, lo_pct); hi_g = lam >= np.percentile(lam, hi_pct)
    if lo_pct == 40:
        lo_g = lam < np.percentile(lam, lo_pct); hi_g = lam > np.percentile(lam, hi_pct)
    print(f"{label}: poor inference {lo_g.sum()} rats (lambda <= {lam[lo_g].max():.1f}), good {hi_g.sum()} rats (lambda >= {lam[hi_g].min():.1f})")
    for meas, dyn in (("wait", wd30), ("initiation", id30)):
        for kind, tr in ((2, "mixed to low"), (1, "mixed to high")):
            arr = np.array([dyn[r][kind] for r in names])
            jobs.append((arr[lo_g], arr[hi_g], 2005 + len(jobs)))
            labels.append({"split": label.split(" ")[0], "measure": meas, "transition": tr})
started = time.time()
with ProcessPoolExecutor(4) as pool:
    out = list(pool.map(shuffle_job, jobs))
print(f"shuffles in {time.time() - started:.0f} s")
res = pd.DataFrame([{**l, "slope diff": d[1], "p slope": p[1], "right asymptote diff": d[0], "p right asymptote": p[0]}
                    for l, (d, p) in zip(labels, out)])
print(res.round(4).to_string(index=False))
'''+s[b:]
open(p,'w').write(s)
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
python $TMPDIR/build_nb.py && PYTHONPATH=. timeout 5000 $TMPDIR/scratch/bin/python $TMPDIR/run_cells.py 2>&1 | tee $TMPDIR/run2.log | grep -v "^$" | sed -n '/cell 9 /,$p' | grep -v "^RWTautowait" | head -300
```

```
written 75 cells
===== cell 9 ['claim:zenodo-link']
read 291 structs in 0 s
Rats in both: 291 ; only Zenodo: [] ; only dandiset: []
Rats whose sessions match in order, trial counts and every compared value (criterion): 0
Rats whose sessions match as a set, ignoring order: 0
Rats that differ:
 rat  sessions_zenodo  sessions_dandiset  same_set  only_zenodo  only_dandiset  trials_only_zenodo
C015               25                 25     False           25             25                7248
C033               98                 98     False           98             98               52316
C034               58                 58     False           58             58               19827
C035               66                 66     False           66             66               45764
C036               49                 49     False           49             49               20624
E001               45                 45     False           45             45               17634
E002               29                 29     False           29             29               13722
E003              104                104     False          104            104               38230
E004               69                 69     False           69             69               40105
E005               80                 80     False           80             80               30000
E006               16                 16     False           16             16                7106
E007               89                 89     False           89             89               30181
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
a=s.index('def session_keys(arrays, bounds):')
b=s.index('link = pd.DataFrame(rows)')
s=s[:a]+'''EXACT = ["reward", "block", "catch", "vios", "hits", "optout"]
CLOSE = {"wait_time": 1e-4, "ITI": 1e-4, "prob_catch": 1e-6}   # float32 in the NWB files

def sessions_of(get, bounds):
    # Per session: a key from its trial count and integer fields, and its float fields.
    out = []
    for a, b in zip(bounds[:-1], bounds[1:]):
        key = str(b - a) + "|" + "|".join(np.asarray(get(f)[a:b], float).astype(np.int64).tobytes().hex() for f in EXACT)
        out.append((key, {f: np.asarray(get(f)[a:b], float) for f in CLOSE}))
    return out

rows = []
for r in sorted(set(structs) | set(names)):
    Z, A = structs.get(r), rats.get(r)
    row = {"rat": r, "in_zenodo": Z is not None, "in_dandiset": A is not None}
    if Z is not None and A is not None:
        nt_z = np.atleast_1d(Z["ntrials"]).astype(int)
        nt_d = np.bincount(A["session"])
        sz = sessions_of(lambda f: np.asarray(Z[f], float).ravel(), np.r_[0, np.cumsum(nt_z)])
        sd = sessions_of(lambda f: A[FIELDS[f]].astype(float), np.r_[0, np.cumsum(nt_d)])
        pool_d = {}
        for k, v in sd:
            pool_d.setdefault(k, []).append(v)
        matched, unmatched_z, float_bad = 0, [], 0
        for k, v in sz:
            cands = pool_d.get(k, [])
            hit = next((i for i, c in enumerate(cands) if all(np.allclose(c[f], v[f], atol=t, equal_nan=True) for f, t in CLOSE.items())), None)
            if hit is None:
                unmatched_z.append(int(k.split("|")[0]))
                float_bad += bool(cands)
            else:
                cands.pop(hit); matched += 1
        row.update(sessions_zenodo=len(nt_z), sessions_dandiset=len(nt_d),
                   same_order=bool(len(sz) == len(sd) and all(a[0] == b[0] for a, b in zip(sz, sd)) and len(unmatched_z) == 0),
                   only_zenodo=len(unmatched_z), only_dandiset=sum(len(v) for v in pool_d.values()),
                   trials_only_zenodo=int(sum(unmatched_z)), float_mismatch=float_bad)
        row["same_set"] = row["only_zenodo"] == 0 and row["only_dandiset"] == 0
    rows.append(row)
'''+s[b:]
s=s.replace('''print(link[~link.same_order][["rat", "sessions_zenodo", "sessions_dandiset", "same_set", "only_zenodo", "only_dandiset",
                               "trials_only_zenodo"]].to_string(index=False))''','''print(link[~link.same_order][["rat", "sessions_zenodo", "sessions_dandiset", "same_set", "only_zenodo", "only_dandiset",
                               "trials_only_zenodo", "float_mismatch"]].to_string(index=False))''')
open(p,'w').write(s)
EOF
cd entries/001169-mah-2023 && python $TMPDIR/build_nb.py && PYTHONPATH=. timeout 5000 $TMPDIR/scratch/bin/python $TMPDIR/run_cells.py 2>&1 | tee $TMPDIR/run2.log | grep -v "^$" | sed -n '/cell 9 /,$p' | grep -v "^RWTautowait" | head -300
```

```
written 75 cells
===== cell 9 ['claim:zenodo-link']
read 291 structs in 0 s
Rats in both: 291 ; only Zenodo: [] ; only dandiset: []
Rats whose sessions match in order, trial counts and every compared value (criterion): 273
Rats whose sessions match as a set, ignoring order: 283
Rats that differ:
 rat  sessions_zenodo  sessions_dandiset  same_set  only_zenodo  only_dandiset  trials_only_zenodo  float_mismatch
G001               34                 32     False            2              0                 608               0
G002               75                 75      True            0              0                   0               0
G006               85                 85      True            0              0                   0               0
G008              134                134      True            0              0                   0               0
G022               88                 87     False            1              0                 405               0
G026               86                 85     False            1              0                 452               0
G052               51                 50     False            1              0                 527               0
G060               54                 53     False            1              0                 589               0
J006               97                 97      True            0              0                   0               0
J011               78                 77     False            1              0                 371               0
J023               95                 94     False            1              0                 364               0
J058              101                101      True            0              0                   0               0
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='wagering.py'
s=open(p).read()
s=s.replace('''    taus = np.linspace(max(lower[1], 1e-3), upper[1], 5000)
    E = np.exp(-x[None, :] / taus[:, None])
    a = np.clip((E @ y) / np.sum(E ** 2, axis=1), lower[0], upper[0])
    mse = np.mean((y[None, :] - a[:, None] * E) ** 2, axis=1)
    k = int(np.argmin(mse))''','''    taus = np.linspace(max(lower[1], 0.01), upper[1], 5000)
    E = np.exp(-x[None, :] / taus[:, None])
    a = np.clip((E @ y) / np.sum(E ** 2, axis=1), lower[0], upper[0])
    mse = np.mean((y[None, :] - a[:, None] * E) ** 2, axis=1)
    k = int(np.nanargmin(np.where(np.isfinite(mse), mse, np.inf)))''')
s=s.replace('''def sigmoid(x, p):
    return p[3] + (p[0] - p[3]) / (1 + np.exp(-p[1] * (x - p[2])))
''','''def sigmoid(x, p):
    return p[3] + (p[0] - p[3]) / (1 + np.exp(np.clip(-p[1] * (x - p[2]), -500, 500)))


def _sigmoid_sse(p, x, y):
    s = 1 / (1 + np.exp(np.clip(-p[1] * (x - p[2]), -500, 500)))
    r = y - (p[3] + (p[0] - p[3]) * s)
    ds = s * (1 - s)
    grad = -2 * np.array([r @ s, r @ ((p[0] - p[3]) * ds * (x - p[2])), r @ (-(p[0] - p[3]) * ds * p[1]), r @ (1 - s)])
    return r @ r, grad
''')
s=s.replace('''        res = optimize.minimize(lambda p: np.sum((y - sigmoid(x, p)) ** 2), p0, method="L-BFGS-B",
                                bounds=list(zip(lb, ub)))''','''        res = optimize.minimize(_sigmoid_sse, p0, args=(x, y), jac=True, method="L-BFGS-B", bounds=list(zip(lb, ub)))''')
s=s.replace('def lambda_shuffle_test(lo: np.ndarray, hi: np.ndarray, n_perm: int, twin: int, rng)','def lambda_shuffle_test(lo: np.ndarray, hi: np.ndarray, n_perm: int, twin: int, rng)')
open(p,'w').write(s)
EOF
cat > $TMPDIR/t8.py <<'EOF'
import numpy as np, time, wagering as w, pickle, os
from scipy import optimize
x=np.arange(-20,21.); rng=np.random.default_rng(0)
y=w.sigmoid(x,[0.3,0.4,5,-0.2])+rng.normal(0,0.02,41)
t=time.time(); 
for _ in range(20): p=w.fit_sigmoid(x,y,rng)
print(p, (time.time()-t)/20)
print(w.fit_exp_decay(np.arange(1,10), -0.03*np.exp(-np.arange(1,10)/1.7), (-10,0),(0,10)))
print(w.fit_exp_decay(np.arange(1,10), np.r_[-0.03, np.zeros(8)], (-10,0),(0,10)))
# test inferential starts 10 vs 20
d=os.environ['TMPDIR']; S,rats=pickle.load(open(f'{d}/rats.pkl','rb'))
for r in sorted(rats)[:12]:
    M=w.model_inputs(rats[r]); inf=w.beliefs(M).argmax(1)
    a=w.fit_inferential(M,inf,np.random.default_rng(1),10)[1]; b=w.fit_inferential(M,inf,np.random.default_rng(2),40)[1]
    print(r, round(a,3), round(b,3))
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t8.py
```

```
[ 0.30549555  0.36453245  5.02719758 -0.20577095] 0.045897948741912845
[-0.02999031  1.70064613]
[-9.43943421  0.17386877]
C015 2425.266 2425.266
C033 14688.087 14688.087
C034 6444.653 6444.653
C035 12169.227 12169.227
C036 8678.802 8678.802
E001 7177.466 7177.466
E002 6248.108 6248.108
E003 22275.38 22275.38
E004 13253.511 13253.511
E005 12720.048 12720.048
E006 4624.708 4624.708
E007 8723.963 8723.963
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
s=s.replace('''def shuffle_job(job):
    lo_rows, hi_rows, seed = job
    return w.lambda_shuffle_test(lo_rows, hi_rows, 500, 30, np.random.default_rng(seed))''','''def shuffle_job(job):
    lo_rows, hi_rows, n_perm, seed = job
    return w.lambda_shuffle_test(lo_rows, hi_rows, n_perm, 30, np.random.default_rng(seed))''')
s=s.replace('''            jobs.append((arr[lo_g], arr[hi_g], 2005 + len(jobs)))''','''            jobs.append((arr[lo_g], arr[hi_g], 500 if k == 0 else 200, 2005 + len(jobs)))''')
s=s.replace('''splits = (("20th/80th (Methods), ties at the cut included", 20, 80), ("40th/60th (Figure3.m, variant)", 40, 60))''','''splits = (("20th/80th (Methods), ties at the cut included; 500 shuffles", 20, 80),
          ("40th/60th (Figure3.m, variant); 200 shuffles", 40, 60))''')
open(p,'w').write(s)
EOF
cd entries/001169-mah-2023 && python $TMPDIR/build_nb.py && PYTHONPATH=. timeout 5000 $TMPDIR/scratch/bin/python $TMPDIR/run_cells.py 2>&1 | tee $TMPDIR/run3.log | grep -v "^$" | sed -n '/cell 16 /,/cell 21 /p;/cell 24 /,/cell 28 /p'
```

```
written 75 cells
===== cell 16 ['claim:fig2cd-regression-kernels']
regressions and fits in 6 s
Mean wait time coefficients (current, 1 to 9 back; after zeroing): [0.211, -0.0033, 0.0, -0.0003, 0.0003, 0.0, 0.0, 0.0, 0.0, 0.0]
Mean initiation time coefficients (1 to 9 back; after zeroing): [-0.0307, -0.023, -0.0107, -0.0051, -0.002, -0.0009, -0.0003, -0.0003, -0.0002]
Wait time, current reward coefficient above zero: 289 rats, signed-rank p = 3.83e-49
Initiation time, previous reward coefficient below zero: 249 rats, signed-rank p = 1.27e-37
|mean wait coefficient 1 back| / mean current = 0.016
|mean initiation coefficient| at 1, 3 and 6 back: 0.0307, 0.0107, 0.0009
Rats with every previous wait time coefficient zeroed: 248
----- 6 s
===== cell 17 ['claim:fig2e-tau-differ']
Tau, wait times: median 0.00 (0 in 248 rats); initiation times (9 back, Methods): median 1.63 (0 in 25 rats)
Signed-rank, initiation against wait time taus: p = 1.52e-44; initiation larger in 262 rats, smaller in 5
Variant, 10 back (Figure2.m): median 1.64, p = 2.16e-44
Tau ranges: wait 0.0 to 1.58 ; initiation 0.0 to 10.0
----- 0 s
===== cell 18 ['claim:fig2f-tau-uncorrelated']
Pearson, initiation (9 back, Methods) against wait time taus: r = 0.023, p = 0.696  (paper: r = -0.03, p = 0.53 in the legend; r = 0.08, p = 0.18 in the text)
Variant, 10 back (Figure2.m): r = 0.023, p = 0.691
[... 48 more lines not kept]
```

**Agent**

The model and shuffle results are in. In Fig 3l, the wait-time right asymptote gives p = 0.003, the same as the paper. Now writing the Figure 4 notebook, which uses `A_Structs_all` from Zenodo.

**Agent calls Bash**

```bash
cat >> wagering.py <<'EOF'


# ----------------------------------------------------------------------------------------
# Figure 4: training (A_Structs_all from Zenodo)
# ----------------------------------------------------------------------------------------

def _ordinal(volume: np.ndarray) -> np.ndarray:
    """convertreward.m: offered volume to its rank 1 to 5."""
    return np.array([{5: 1, 10: 2, 20: 3, 40: 4, 80: 5}[VOLUME_TO_STANDARD[int(v)]] for v in volume], float)


def regress_trials_blocks(Z: dict, idx: np.ndarray) -> dict:
    """regress_trials_blocksv2.m (tback = 1) on the non-violation trials among idx of a struct
    (with wait times above the threshold and initiation times above the 99th percentile
    already removed): wait time ratio 20 uL high/low, initiation time ratio high/low, the wait
    time coefficients of reward and block (blocks coded low 1, mixed 2, high 3; no constant)
    and the initiation time coefficient of the previous reward (no constant)."""
    keep = idx[~Z["vios"][idx].astype(bool)]
    block = Z["block"][keep].astype(int)
    block = np.select([block == 3, block == 2, block == 1], [1, 3, 2])
    wt = Z["wait_time"][keep].astype(float).copy()
    wt[Z["optout"][keep] == 0] = np.nan
    rew = _ordinal(Z["reward"][keep])
    iti = Z["ITI"][keep].astype(float)
    prev = np.r_[0, rew[:-1]]
    Y, Y2 = zscore(wt), zscore(iti)
    out = {}
    ok = ~np.isnan(Y)
    out["b_reward"], out["b_block"] = (np.linalg.lstsq(np.c_[rew, block][ok], Y[ok], rcond=None)[0]
                                       if ok.sum() > 2 else (np.nan, np.nan))
    ok2 = ~np.isnan(Y2)
    out["b_iti_prev"] = np.linalg.lstsq(prev[ok2, None], Y2[ok2], rcond=None)[0][0] if ok2.sum() > 2 else np.nan
    with np.errstate(invalid="ignore", divide="ignore"):
        out["wt_ratio"] = np.nanmean(wt[(block == 3) & (rew == 3)]) / np.nanmean(wt[(block == 1) & (rew == 3)])
        out["iti_ratio"] = np.nanmean(iti[block == 3]) / np.nanmean(iti[block == 1])
    return out


def training_pairs(Z: dict, nsess: int = 50, grp: int = 2) -> tuple[pd.DataFrame, pd.DataFrame]:
    """macro_regress_overtraining_V2.m: the measures of regress_trials_blocks for the first and
    the last nsess sessions in groups of grp, one row per group (NaN where the rat has too few
    sessions)."""
    Z = dict(Z)
    Z["wait_time"] = Z["wait_time"].astype(float).copy()
    Z["wait_time"][Z["wait_time"] > float(Z["wait_thresh"])] = np.nan
    Z["ITI"] = Z["ITI"].astype(float).copy()
    Z["ITI"][Z["ITI"] > np.nanpercentile(Z["ITI"], 99)] = np.nan
    nt = np.atleast_1d(Z["ntrials"]).astype(int)
    starts = np.r_[0, np.cumsum(nt)]
    n = len(nt)
    first, last = [], []
    for k in range(0, nsess, grp):
        for rows, sess in ((first, np.arange(k, k + grp)), (last, np.arange(n - nsess + k, n - nsess + k + grp))):
            if sess.max() >= n or sess.min() < 0:
                rows.append({})
            else:
                idx = np.arange(starts[sess.min()], starts[sess.max() + 1])
                rows.append(regress_trials_blocks(Z, idx))
    cols = ["wt_ratio", "iti_ratio", "b_reward", "b_block", "b_iti_prev"]
    return pd.DataFrame(first, columns=cols), pd.DataFrame(last, columns=cols)
EOF
cat > $TMPDIR/t9.py <<'EOF'
import os, pickle, time, numpy as np, wagering as w
fn=f"{os.environ['TMPDIR']}/z_A_Structs_all.pkl"
t=time.time()
if os.path.exists(fn): Z=pickle.load(open(fn,'rb'))
else:
    Z=w.load_zenodo_structs("A_Structs_all"); pickle.dump(Z,open(fn,'wb'))
print(len(Z), time.time()-t)
t=time.time()
res={r:w.training_pairs(Z[r]) for r in sorted(Z)}
print(time.time()-t)
import pandas as pd
F=np.array([res[r][0].to_numpy() for r in sorted(Z)])
print(np.nanmean(F,0).round(3)[:5]); print(np.nanmean(F,0).round(3)[15:25])
print(sorted(Z)[:3], {k:np.shape(v) for k,v in Z[sorted(Z)[0]].items()})
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t9.py
```

```
entries/001169-mah-2023/wagering.py:829: RuntimeWarning: Mean of empty slice
  out["wt_ratio"] = np.nanmean(wt[(block == 3) & (rew == 3)]) / np.nanmean(wt[(block == 1) & (rew == 3)])
entries/001169-mah-2023/wagering.py:830: RuntimeWarning: Mean of empty slice
  out["iti_ratio"] = np.nanmean(iti[block == 3]) / np.nanmean(iti[block == 1])
entries/001169-mah-2023/wagering.py:814: RuntimeWarning: invalid value encountered in cast
  block = Z["block"][keep].astype(int)
entries/001169-mah-2023/wagering.py:217: RuntimeWarning: Mean of empty slice
  return (x - np.nanmean(x)) / np.nanstd(x, ddof=1)
/tmp/claude-1001/scratch/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
291 178.48796486854553
9.691016435623169
[[ 2.673  0.855  0.011 -0.015 -0.003]
 [ 1.083  0.832  0.019 -0.028 -0.003]
 [ 1.136  0.792  0.034 -0.049 -0.003]
 [ 1.958  0.734  0.046 -0.067 -0.004]
 [ 2.278  0.764  0.057 -0.081 -0.004]]
[[ 0.968  0.636  0.138 -0.191 -0.005]
 [ 0.963  0.624  0.139 -0.193 -0.006]
 [ 0.923  0.676  0.152 -0.211 -0.006]
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='wagering.py'
s=open(p).read()
s=s.replace('''    return np.array([{5: 1, 10: 2, 20: 3, 40: 4, 80: 5}[VOLUME_TO_STANDARD[int(v)]] for v in volume], float)''','''    rank = {4: 1, 5: 1, 8: 2, 10: 2, 16: 3, 20: 3, 32: 4, 40: 4, 64: 5, 80: 5}
    return np.array([rank.get(int(v), np.nan) if np.isfinite(v) else np.nan for v in volume], float)''')
s=s.replace('''    block = Z["block"][keep].astype(int)
    block = np.select([block == 3, block == 2, block == 1], [1, 3, 2])''','''    block = Z["block"][keep].astype(float)
    block = np.select([block == 3, block == 2, block == 1], [1.0, 3.0, 2.0], default=np.nan)''')
s=s.replace('''    ok = ~np.isnan(Y)
    out["b_reward"], out["b_block"] = (np.linalg.lstsq(np.c_[rew, block][ok], Y[ok], rcond=None)[0]
                                       if ok.sum() > 2 else (np.nan, np.nan))
    ok2 = ~np.isnan(Y2)''','''    ok = ~np.isnan(Y) & ~np.isnan(rew) & ~np.isnan(block)
    out["b_reward"], out["b_block"] = (np.linalg.lstsq(np.c_[rew, block][ok], Y[ok], rcond=None)[0]
                                       if ok.sum() > 2 else (np.nan, np.nan))
    ok2 = ~np.isnan(Y2) & ~np.isnan(prev)''')
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
sed -i 's/STRUCT_FIELDS = \["reward", "block", "catch", "vios", "hits", "optout", "wait_time", "ITI",/STRUCT_FIELDS = ["reward", "block", "catch", "vios", "hits", "optout", "wait_time", "ITI", "trainingstage",/' wagering.py && grep -n "STRUCT_FIELDS =" -A1 wagering.py && cat >> wagering.py <<'EOF'


def remove_outliers(x: np.ndarray, window: int = 5) -> np.ndarray:
    """MATLAB's isoutlier(x, 'movmedian', 5) set to NaN: points more than three scaled median
    absolute deviations from the median of their moving window."""
    x = np.asarray(x, float).copy()
    half = window // 2
    out = x.copy()
    for i in range(len(x)):
        w_ = x[max(0, i - half):i + half + 1]
        w_ = w_[~np.isnan(w_)]
        if len(w_) == 0 or np.isnan(x[i]):
            continue
        med = np.median(w_)
        mad = 1.4826 * np.median(np.abs(w_ - med))
        if abs(x[i] - med) > 3 * mad:
            out[i] = np.nan
    return out
EOF
cat > $TMPDIR/build_nb2.py <<'EOF'
import nbformat as nbf
cells = []
def md(s): cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    cells.append(c)

md(r"""
# Mah et al. (2023), Figure 4: training, from the paper's Zenodo deposit

**Paper.** Mah A, Schiereck SS, Bossio V, Constantinople CM (2023). Distinct value computations
support rapid sequential decisions. *Nature Communications* 14:7573.
[doi:10.1038/s41467-023-43250-x](https://doi.org/10.1038/s41467-023-43250-x). Full text used
(open access, PMC10663503), with the paper's code (github.com/constantinoplelab/published,
`rat_behavior`, commit b7b68ca).

**Data.** Figure 4 uses every session of the final training stage (`A_Structs_all`), including
the early sessions that the inclusion criteria remove. The dandiset
([DANDI:001169](https://dandiarchive.org/dandiset/001169/0.260825.1909), version 0.260825.1909)
holds only the included sessions (`A_Structs_Final`), so these claims are tested on the structs the
paper deposited on Zenodo ([10.5281/zenodo.10031483](https://doi.org/10.5281/zenodo.10031483),
version 1), read from its zip archive with range requests and held in memory (about 0.5 GB). The
dandiset is used only to count its sessions per rat. The other claims are in
`reproduce_mah_2023.ipynb`. No random numbers are drawn here.

| Claim | Data | Status |
|---|---|---|
| fig4a-wait-ratio-learning | elsewhere (Zenodo) | tested |
| fig4bc-regression-learning | elsewhere (Zenodo) | tested |
| fig4de-overshoot-learning | dandiset | blocked (data missing; see the main notebook) |
""")

code(r"""
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import wagering as w

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200)

started = time.time()
structs = w.load_zenodo_structs("A_Structs_all")
print(f"read {len(structs)} structs from Zenodo in {time.time() - started:.0f} s")
assets = w.asset_list()
""")

md("## Data check")

code(r"""
names = sorted(structs)
info = pd.DataFrame({r: {"sessions_all": len(np.atleast_1d(structs[r]["ntrials"])),
                         "trials_all": len(structs[r]["reward"]),
                         "trials_without_block": int(np.isnan(structs[r]["block"].astype(float)).sum()),
                         "stages": "/".join(str(int(s)) for s in np.unique(structs[r]["trainingstage"][~np.isnan(structs[r]["trainingstage"].astype(float))]))}
                     for r in names}).T
info["sessions_dandiset"] = assets.path.str.split("/").str[0].str[4:].value_counts().reindex(names).fillna(0).astype(int)
print("Rats:", len(names), "; same rats as the dandiset:", sorted(names) == sorted(assets.path.str.split("/").str[0].str[4:].unique()))
print(info[["sessions_all", "sessions_dandiset", "trials_all", "trials_without_block"]].astype(float).describe().loc[["min", "50%", "max"]].to_string())
print("Training stage codes present, rats:", info.stages.value_counts().to_dict())
print("Rats with more sessions here than in the dandiset:", int((info.sessions_all > info.sessions_dandiset).sum()),
      "; fewer:", int((info.sessions_all < info.sessions_dandiset).sum()))
print("Rats with at least 50 sessions here:", int((info.sessions_all >= 50).sum()))
print("Reward volumes:", sorted(np.unique(np.concatenate([structs[r]["reward"] for r in names])).tolist()))
print("Block codes:", sorted(np.unique(np.concatenate([structs[r]["block"].astype(float) for r in names])).tolist()))
""", ["sanity"])

md(r"""
The deposit holds all 291 rats. It has more sessions per rat than the dandiset for most rats,
which is what the Zenodo README says: these structs keep every session that ended in the final
stage, before the inclusion criteria; some trials carry earlier stage codes and no block, and
they are left out of the block measures, as the code leaves them out (its regressions drop rows
with NaN). Stage 9 is the paper's stage 8 (README). The duplicated L011 session of the dandiset is
not a concern here.
""")

code(r"""
started = time.time()
pairs = {r: w.training_pairs(structs[r]) for r in names}
print(f"measures for {len(pairs)} rats in {time.time() - started:.0f} s")
first = {m: np.array([pairs[r][0][m].to_numpy() for r in names]) for m in pairs[names[0]][0].columns}
last = {m: np.array([pairs[r][1][m].to_numpy() for r in names]) for m in pairs[names[0]][0].columns}

def population(x):
    # Figure4.m: per-rat smoothing over groups (span 5), outliers removed, then the mean over rats.
    sm = np.array([w.remove_outliers(w.matlab_smooth(row, 5)) for row in x])
    return np.nanmean(sm, 0)
""")

md(r"""
## fig4a-wait-ratio-learning

> Over training in the final stage, the wait time ratio (20 uL, high/low) fell gradually toward
> its final value, while the trial initiation time ratio was below 1 from the first session.
""")

code(r"""
wt1, it1 = first["wt_ratio"][:, 0], first["iti_ratio"][:, 0]
wt_late = np.nanmean(first["wt_ratio"][:, 15:25], 1)
print(f"Initiation time ratio, sessions 1 and 2: median {np.nanmedian(it1):.3f} over {np.sum(~np.isnan(it1))} rats; below 1 in "
      f"{np.sum(it1 < 1)}; signed-rank against 1 p = {w.signrank(it1 - 1):.3g}")
d = wt1 - wt_late
print(f"Wait time ratio, sessions 1 and 2: median {np.nanmedian(wt1):.3f}; sessions 31 to 50 (mean of pairs 16 to 25): median "
      f"{np.nanmedian(wt_late):.3f}; first above later in {np.sum(d > 0)} of {np.sum(~np.isnan(d))} rats; signed-rank p = {w.signrank(d):.3g}")
print(f"Wait time ratio, sessions 1 and 2, below 1 in {np.sum(wt1 < 1)} of {np.sum(~np.isnan(wt1))} rats; signed-rank against 1 p = {w.signrank(wt1 - 1):.3g}")
print("Rats per pair with a wait time ratio:", np.sum(~np.isnan(first["wt_ratio"]), 0).tolist())
print("Medians per pair, wait:", np.round(np.nanmedian(first["wt_ratio"], 0), 3).tolist())
print("Medians per pair, initiation:", np.round(np.nanmedian(first["iti_ratio"], 0), 3).tolist())
print("Last 50 sessions, medians per pair, wait:", np.round(np.nanmedian(last["wt_ratio"], 0), 3).tolist())
pw, pi_ = population(first["wt_ratio"]), population(first["iti_ratio"])
xs = np.arange(2, 51, 2)
fig, ax = plt.subplots(figsize=(5, 3.2))
ax.plot(xs, pw, color="#8B6DB0", label="wait time"); ax.plot(xs, pi_, color="#5DBD77", label="trial initiation time")
ax.axhline(1, color="k", lw=0.8); ax.set_xlabel("training session (pairs)"); ax.set_ylabel("ratio high/low"); ax.legend()
plt.tight_layout(); plt.show()
print("Plotted (Figure4.m's smoothing and outlier removal): wait", np.round(np.nanmin(pw), 3), "to", np.round(np.nanmax(pw), 3),
      "; initiation", np.round(np.nanmin(pi_), 3), "to", np.round(np.nanmax(pi_), 3))
""", ["claim:fig4a-wait-ratio-learning"])

md(r"""
**Result: TBD**
""")

md(r"""
## fig4bc-regression-learning

> Over training, the block and reward coefficients for wait times grew gradually, while the
> previous-reward coefficient for trial initiation times was comparable early and late.
""")

code(r"""
for m, label in (("b_block", "wait time, block"), ("b_reward", "wait time, reward")):
    a, b = np.abs(first[m][:, 0]), np.abs(np.nanmean(first[m][:, 15:25], 1))
    print(f"|{label}| coefficient: sessions 1 and 2 median {np.nanmedian(a):.3f}; sessions 31 to 50 median {np.nanmedian(b):.3f}; "
          f"larger later in {np.sum(b > a)} of {np.sum(~np.isnan(a - b))} rats; signed-rank p = {w.signrank(b - a):.3g}")
    print("   medians per pair:", np.round(np.nanmedian(first[m], 0), 3).tolist())
e, l = np.nanmean(first["b_iti_prev"]), np.nanmean(last["b_iti_prev"])
print(f"Initiation time, previous reward coefficient: mean over the first 50 sessions {e:.4f}, over the last 50 {l:.4f}, ratio {l / e:.3f}")
pe, pl = np.nanmean(first["b_iti_prev"], 1), np.nanmean(last["b_iti_prev"], 1)
print(f"   per rat, first against last 50 (rats with both): signed-rank p = {w.signrank(pl - pe):.3g}; medians {np.nanmedian(pe):.4f} and {np.nanmedian(pl):.4f}")
print("   medians per pair, first 50:", np.round(np.nanmedian(first["b_iti_prev"], 0), 4).tolist())
""", ["claim:fig4bc-regression-learning"])

md(r"""
**Result: TBD**
""")

md(r"""
## Summary

TBD
""")

nb = nbf.v4.new_notebook(); nb.cells = cells
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "entries/001169-mah-2023/reproduce_mah_2023_fig4.ipynb")
print("written")
EOF
python $TMPDIR/build_nb2.py && cat > $TMPDIR/run2.py <<'EOF'
import nbformat, os, pickle, time
import matplotlib; matplotlib.use("Agg")
nb = nbformat.read("reproduce_mah_2023_fig4.ipynb", 4)
g = globals()
for i, c in enumerate([c for c in nb.cells if c.cell_type == "code"]):
    src = c.source
    if i == 0:
        src = src.replace('structs = w.load_zenodo_structs("A_Structs_all")', 'structs = pickle.load(open(os.environ["TMPDIR"] + "/z_A_Structs_all.pkl", "rb"))')
        src = src.replace('assets = w.asset_list()', 'assets = pd.read_parquet(os.environ["TMPDIR"] + "/assets.parquet")')
    print("=====", i, flush=True); exec(src, g)
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/run2.py
```

```
Exit code 1
719:STRUCT_FIELDS = ["reward", "block", "catch", "vios", "hits", "optout", "wait_time", "ITI", "trainingstage",
720-                 "prob_catch", "ntrials", "wait_thresh"]
written
===== 0
read 291 structs from Zenodo in 0 s
===== 1
Traceback (most recent call last):
  File "/tmp/claude-1001/run2.py", line 10, in <module>
    print("=====", i, flush=True); exec(src, g)
                                   ~~~~^^^^^^^^
  File "<string>", line 5, in <module>
KeyError: 'trainingstage'
```

**Agent calls Bash**

```bash
rm -f $TMPDIR/z_A_Structs_all.pkl && PYTHONPATH=. $TMPDIR/scratch/bin/python -c "
import wagering as w, pickle, os
Z=w.load_zenodo_structs('A_Structs_all'); pickle.dump(Z,open(os.environ['TMPDIR']+'/z_A_Structs_all.pkl','wb'))
" && PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/run2.py
```

```
===== 0
read 291 structs from Zenodo in 0 s
===== 1
Rats: 291 ; same rats as the dandiset: True
     sessions_all  sessions_dandiset  trials_all  trials_without_block
min          19.0               15.0      8309.0                   0.0
50%          99.0               71.0     43232.0                   0.0
max         265.0              232.0    140484.0                   5.0
Training stage codes present, rats: {'7/8/9': 106, '1/2/3/4/5/6/7/8/9': 78, '8/9': 76, '6/7/8/9': 26, '1/3/4/5/6/7/8/9': 2, '1/2/3/9': 1, '5/6/7/8/9': 1, '9': 1}
Rats with more sessions here than in the dandiset: 269 ; fewer: 22
Rats with at least 50 sessions here: 265
Reward volumes: [4, 5, 8, 10, 16, 20, 32, 40, 64, 80]
Block codes: [1.0, 2.0, 3.0, nan]
===== 2
measures for 291 rats in 16 s
===== 3
Initiation time ratio, sessions 1 and 2: median 0.749 over 145 rats; below 1 in 107; signed-rank against 1 p = 5.38e-07
Wait time ratio, sessions 1 and 2: median 0.936; sessions 31 to 50 (mean of pairs 16 to 25): median 0.917; first above later in 64 of 126 rats; signed-rank p = 0.233
Wait time ratio, sessions 1 and 2, below 1 in 72 of 132 rats; signed-rank against 1 p = 0.872
Rats per pair with a wait time ratio: [132, 193, 202, 216, 251, 275, 282, 283, 285, 280, 283, 281, 278, 279, 278, 277, 274, 271, 276, 273, 268, 268, 268, 262, 257]
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t10.py <<'EOF'
import os, pickle, numpy as np, wagering as w
Z=pickle.load(open(os.environ['TMPDIR']+'/z_A_Structs_all.pkl','rb'))
names=sorted(Z); pairs={r:w.training_pairs(Z[r]) for r in names}
b=np.array([pairs[r][0].b_reward.iloc[0] for r in names]); print('nan',np.isnan(b).sum(),'zero',(b==0).sum(), 'n',len(b))
r=[r for r in names if pairs[r][0].b_reward.iloc[0]==0][0]; print(r)
A=Z[r]; nt=np.atleast_1d(A['ntrials']); idx=np.arange(nt[0]+nt[1])
print('optout', A['optout'][idx].sum(), 'catch', A['catch'][idx].sum(), 'stage', np.unique(A['trainingstage'][idx]), 'blocks', np.unique(A['block'][idx]), 'wt nonnan', np.sum(~np.isnan(A['wait_time'][idx].astype(float))), 'thresh', A['wait_thresh'])
EOF
PYTHONPATH=. $TMPDIR/scratch/bin/python $TMPDIR/t10.py 2>&1 | grep -v Warn
```

```
out["wt_ratio"] = np.nanmean(wt[(block == 3) & (rew == 3)]) / np.nanmean(wt[(block == 1) & (rew == 3)])
  out["iti_ratio"] = np.nanmean(iti[block == 3]) / np.nanmean(iti[block == 1])
  return (x - np.nanmean(x)) / np.nanstd(x, ddof=1)
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
nan 80 zero 1 n 291
G044
optout 26 catch 34 stage [7 8] blocks [1] wt nonnan 377 thresh 31.05881398910587
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
new = [
# dataset-counts
r"""**Result: reproduced.** The files hold 291 rats, 184 male and 107 female, with a median of 71
sessions and 33,493 trials per rat, each session counted once; all five numbers match the paper.
The other count in the Methods (160 male and 114 female, 274 rats) matches neither the files nor
the paper's 291.""",
# zenodo-link (two cells before it, one conclusion)
r"""**Result: partially reproduced.** All 291 rats are in both. 273 rats (94%) match the Zenodo
structs in full, session by session in the same order with the same trial counts and values, at
least the 90% the criterion asks for partial reproduction, not all 291. Ignoring order, 283 rats
match. Nine sessions of the structs (3,645 trials, 0.035% of all) are missing from the dandiset,
in eight rats (G001 two, G022, G026, G052, G060, J011, J023, S028). In 10 rats the sessions are
the same but in another order: the dandiset orders them by start time, and the structs place
some sessions later (for several rats, those of 2020-06-22). Every session in the dandiset has an
identical session on Zenodo (after the duplicate of L011 is removed; the L011 struct has 204
sessions, the dandiset 205), and in matched sessions the raw trials' catch probability equals the
structs' `prob_catch`.""",
# fig1f
r"""**Result: reproduced.** Rats waited 10.58% (reading a) or 10.79% (reading b) less for 20 uL
in high than in low blocks, within 10 +- 2.5, and the signed-rank test on per-rat means of
z-scored wait times finds high below low (p = 4.6e-47, 279 of 291 rats). The code's test on raw
means gives p = 8.2e-47, against the paper's 8.26e-49. The effect holds in males (p = 3.8e-30)
and females (p = 1.2e-18).""",
# fig1i
r"""**Result: reproduced.** 290 of 291 rats initiated trials faster in high than in low blocks;
the signed-rank test on z-scored means gives p = 1.82e-49, the paper's value, and on raw means
p = 1.84e-49. The mean ratio high/low is 0.562.""",
# figs2
r"""**Result: reproduced.** The block difference in z-scored initiation time (low minus high) is
larger after unrewarded trials (median 0.347) than after rewarded ones (median -0.017) in 291 of
291 rats, p = 1.8e-49 by signed rank.""",
# figs12
r"""**Result: reproduced.** Males and females do not differ in the wait time ratio (medians 0.887
and 0.892, rank-sum p = 0.24) or in the initiation time ratio (medians 0.552 and 0.540, p = 0.56).""",
# fig2a/2b
r"""**Result: reproduced** (fig2a-wait-time-converges). Before the switch, wait times after low
blocks are 0.330 z above those after high blocks; 11 to 20 trials into the mixed block the
difference is 0.022, a ratio of 0.067, within the criterion's 0.25 (0.170 for trials 6 to 20).

**Result: not reproduced** (fig2b-initiation-previous-block), by the criterion as written.
Initiation times in mixed blocks depend strongly on the previous block, but with the sign
reversed: the difference (after low minus after high) is 0.121 z before the switch and -0.256
after it, a ratio of -2.12, and it is below zero in 290 of 291 rats (signed-rank p = 1.8e-49).
The criterion required the difference to stay above zero. The reversal (faster after low blocks,
slower after high blocks) is the incentive-contrast effect and overshoot that the paper describes
for Figure 2b, so the data agree with the paper's statement; the outcome comes from a criterion
written with the wrong sign before the analysis.""",
# fig2cd
r"""**Result: reproduced.** The current offer raises wait times (coefficient above zero in 289 of
291 rats, p = 3.8e-49), and the mean coefficient one trial back is 1.6% of it in magnitude;
initiation times fall with the previous reward (coefficient below zero in 249 rats, p = 1.3e-37),
with mean coefficients falling in magnitude from 0.0307 one trial back to 0.0107 three back and
0.0009 six back.""",
# fig2e
r"""**Result: reproduced.** Initiation time taus (median 1.63 trials) exceed wait time taus (median
0; in 248 rats no previous coefficient survives), larger in 262 rats and smaller in 5, p = 1.5e-44
against the paper's 1.30e-49.""",
# fig2f
r"""**Result: reproduced.** The two taus are not correlated (r = 0.023, p = 0.70); with the code's
10 previous rewards r = 0.023, p = 0.69. The paper gives two different values, r = -0.03 in the
legend and r = 0.08 in the text.""",
# fig2gh
r"""**Result: reproduced.** With 9 previous rewards the fast and slow groups have 57 and 58 rats (N
= 115; 116 with the code's 10). By the code's test the groups differ in their initiation time
coefficients (p < 0.002, none of 500 shuffles as extreme; paper p = 0.02) and not in their wait
time coefficients (p = 0.21; paper p = 0.1). The wait time result depends on the code's
inconsistent fits: when the observed groups are fit as the shuffled ones, the wait time p is
also below 0.002.""",
# fig2j
r"""**Result: reproduced.** 38 rats have p < 0.05, the paper's count, and the population rank-sum
test finds no effect (p = 0.71; the code's signed-rank p = 0.81, the paper's 0.8).""",
# fig2k
r"""**Result: reproduced.** On trials offering 20 uL, as the Methods state, 265 rats have p < 0.05,
within 256 +- 25.6, and the population rank-sum test finds slower initiation after offers below
20 uL (p = 9.7e-25). The code's reading, all mixed-block trials, gives 255 rats and the paper's
p = 1.84e-49 by signed rank.""",
# fig2l
r"""**Result: reproduced.** The sensitivity to the previous offer is larger for initiation than for
wait times (p = 2.2e-08 on 20 uL trials, larger in 183 rats); with the code's all mixed-block
trials p = 6.09e-38, the paper's 6.21e-38.""",
# fig3c
r"""**Result: reproduced.** By the code's selection the counts are 3, 188, 61, 151 and 40 rats at
catch probabilities 0.1 to 0.35, each within tolerance of the paper's 3, 183, 61, 151 and 39, and
the mean wait time falls strictly from 12.93 s at 0.15 to 11.77, 11.31 and 10.60 s at 0.2, 0.25
and 0.35. Within the 59 rats with both 0.15 and 0.25, 56 wait less at 0.25 (p = 7.7e-10). The files
also hold a probability of 0.3 (8 rats by the code's selection), which the paper does not list.""",
# fig3j
r"""**Result: reproduced.** The inferential model has the lower BIC in 291 of 291 rats (median
difference 847), p = 1.8e-49 by signed rank (paper 1.07e-37); counting all trials in n, or using
AIC, gives the same.""",
# figs9
r"""**Result: reproduced.** In mixed blocks, wait times for 20 uL are shorter when the model infers
a high block (mean 10.87 s) than a low block (11.91 s), in 230 of 291 rats, p = 1.1e-22.""",
# fig3l
r"""**Result: reproduced.** Lambda fit on the grid lies at 0 for 61 rats and at 1 for 108, so the
20th and 80th percentiles fall on these ends and the groups are those rats (61 and 108). For wait
times the right asymptote from mixed to high blocks differs between them (p = 0.003, the paper's
value), while the slope from mixed to low does not (p = 0.34; paper 0.02). For initiation times
neither differs (slope from mixed to low p = 0.32, right asymptote from mixed to high p = 0.11).
With the code's 40th and 60th percentiles (110 and 108 rats), the initiation time slope from mixed
to high differs (p = 0.0075), which that split would count against the claim.""",
# fig5b
r"""**Result: reproduced.** In cue sessions initiation times fall with the offered volume in all 16
rats (signed-rank p = 3.1e-05), and in all 12 rats with sessions of the original task the slope is
steeper in cue sessions than in the original task (p = 0.00049).""",
# fig5c
r"""**Result: reproduced.** In all cue sessions, 14 of 16 rats have p < 0.05 on 20 uL trials, within
13 +- 1.3, and the population rank-sum test finds slower initiation after offers below 20 uL (p =
0.04; 12 of 16 rats in that direction). The result is fragile: the code's reading (all
mixed-block trials) gives 12 rats (p = 1.9e-06), and keeping only sessions after each switched
rat's first 30 cue sessions leaves 11 rats, 10 with p < 0.05, and a population p of 0.47.""",
# fig5d
r"""**Result: not reproduced**, by the criterion as written. As in fig2b, initiation times in the
mixed block depend on the previous block with the sign reversed: the difference is 0.105 z before
the switch and -0.263 after (ratio -2.51), below zero in 15 of 16 rats (p = 9.2e-05). The same
rats in the original task show the same reversal (ratio -2.83). The criterion required the sign to
persist; the data agree with the paper's statement of a dependence on the previous block.""",
]
parts = re.split(r'(md\(r"""\n\*\*Result:.*?"""\))', s, flags=re.S)
idx = [i for i,pt in enumerate(parts) if pt.startswith('md(r"""\n**Result:')]
print(len(idx), len(new))
assert len(idx)==len(new)
for i,t in zip(idx,new):
    parts[i] = 'md(r"""\n' + t + '\n""")'
s=''.join(parts)
# fig2e: tau at bound print
s=s.replace('''print("Tau ranges: wait", tau_wt.min().round(2), "to", tau_wt.max().round(2), "; initiation", tau_i9.min().round(2), "to", tau_i9.max().round(2))''','''print("Tau ranges: wait", tau_wt.min().round(2), "to", tau_wt.max().round(2), "; initiation", tau_i9.min().round(2), "to", tau_i9.max().round(2),
      "; initiation taus at the upper bound of 10:", int(np.sum(tau_i9 >= 9.99)))''')
open(p,'w').write(s)
EOF
grep -c "Result:" $TMPDIR/build_nb.py
```

```
21 21
22
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
s=s.replace('''coefficients (p < 0.002, none of 500 shuffles as extreme; paper p = 0.02) and not in their wait
time coefficients (p = 0.21; paper p = 0.1). The wait time result depends on the code's
inconsistent fits: when the observed groups are fit as the shuffled ones, the wait time p is
also below 0.002.''','''coefficients (p = 0, no shuffle of 500 as extreme; paper p = 0.02) and not in their wait time
coefficients (p = 0.21; paper p = 0.1). The wait time result depends on the code's inconsistent
fits: when the observed groups are fit as the shuffled ones, the wait time p is also 0.''')
s=s.replace('''completed trials and every session starts with a mixed block, as the Methods state. The files'
catch probabilities''','''completed trials, as the Methods state, but 456 of 23,034 sessions start with a high or low block
where the Methods say the first block is always mixed. The files'
catch probabilities''')
a=s.index('| fig4a-wait-ratio-learning | see the second notebook |')
s=s.replace('| fig4a-wait-ratio-learning | see the second notebook |','| fig4a-wait-ratio-learning | partially reproduced (second notebook) |')
s=s.replace('| fig4bc-regression-learning | see the second notebook |','| fig4bc-regression-learning | reproduced (second notebook) |')
s=s.replace('| zenodo-link | reproduced |','| zenodo-link | partially reproduced |')
s=s.replace('| figs12-no-sex-difference | not reproduced |','| figs12-no-sex-difference | reproduced |')
s=s.replace('| fig2gh-fast-slow-groups | not reproduced |','| fig2gh-fast-slow-groups | reproduced |')
s=s.replace('| fig3c-catch-probability | not reproduced |','| fig3c-catch-probability | reproduced |')
s=s.replace('| fig3l-inference-quality | not reproduced |','| fig3l-inference-quality | reproduced |')
s=s.replace('| fig5c-precue-previous-reward | partially reproduced |','| fig5c-precue-previous-reward | reproduced |')
a=s.index('**How the analysis differs from the paper\'s.**')
b=s.index('nb = nbf.v4.new_notebook()')
s=s[:a]+'''**How the analysis differs from the paper's.** The per-rat measures are recomputed from the
dandiset with the paper's MATLAB code as the guide. Where the Methods and the code disagree, the
Methods give the main result and the code's choice is shown: z-scored against raw means for
Figure 1, 9 against 10 previous rewards, trials offering 20 uL against all mixed-block trials,
rank-sum against signed-rank tests in Figure 2j and 2k, and the percentile split of Figure 3l.
The models of Figure 3 are refit here: from 20 random starts (the paper used 100), on catch-trial
wait times with beliefs updated over non-violation trials (the published code does not show the
fitting), without cross-validation, and with lambda on a grid of 11 values, which ties many rats
at 0 and 1. Exponentials are fit by a grid over tau in place of fmincon, and logistic fits use
scipy. The pre-cue claims use the cue sessions the dandiset holds, which passed the paper's
inclusion criteria, where the paper used all of them. Two criteria (fig2b and fig5d) were written
with the wrong sign for the dependence on the previous block; the data show the dependence, with
the incentive-contrast reversal the paper describes.

**What was found about the dandiset.** It holds the paper's processed data for all 291 rats, with
the same values as the Zenodo structs, plus the raw Bpod events, which agree with the processed
times. Nine sessions of the structs (0.035% of trials) are missing; one session (L011) is deposited
twice; sessions of 10 rats are in a different order from the structs. The processed table lacks
the catch probability (a typo in the conversion's column mapping); the training stage is coded 9
without saying that it is the paper's stage 8; ages are missing for 275 rats; sounds are stored
without their identity; 456 sessions start with a high or low block; and the 762 pre-cue sessions
of Figure 5 are among the main data, marked only by a task argument. The early training sessions
that Figure 4 uses are not in the dandiset (they are on Zenodo), and the raw structs behind Figure
4d, 4e and 5 are in neither.
""")

'''+s[b:]
open(p,'w').write(s)

p='/tmp/claude-1001/build_nb2.py'
s=open(p).read()
s=s.replace('''md(r"""
**Result: TBD**
""")

md(r"""
## fig4bc''','''md(r"""
**Result: partially reproduced.** The initiation time ratio is below 1 in the first two sessions
(median 0.749, below 1 in 107 of 145 rats, p = 5.4e-07). The wait time ratio of the first two
sessions (median 0.936) is not higher than over sessions 31 to 50 (median 0.917; higher in 64 of
126 rats, p = 0.23), and does not differ from 1 (p = 0.87), so the gradual fall is not shown by the
criterion's test; the medians per pair fall slowly, to 0.86 to 0.89 in the last pairs.
""")

md(r"""
## fig4bc''')
s=s.replace('''md(r"""
**Result: TBD**
""")

md(r"""
## Summary

TBD
""")''','''md(r"""
**Result: reproduced.** The wait time coefficients grow with training: the block coefficient in
magnitude from a median 0.110 in sessions 1 and 2 to 0.211 over sessions 31 to 50 (larger in 144 of
205 rats, p = 9.3e-08), the reward coefficient from 0.072 to 0.148 (148 of 205, p = 5.8e-09). The
initiation time coefficient of the previous reward has the same mean over the first and the last
50 sessions (-0.0051 and -0.0051, ratio 0.99).
""")

md(r"""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig4a-wait-ratio-learning | partially reproduced |
| fig4bc-regression-learning | reproduced |
| fig4de-overshoot-learning | blocked (data missing) |

**How the analysis differs from the paper's.** The measures follow macro_regress_overtraining_V2.m
and regress_trials_blocksv2.m; the tests compare per-rat values of the first session pair with
sessions 31 to 50, which the paper does not test. The code's smoothing of each rat's coefficients
applies only to the block coefficient (a loop variable left from an earlier loop); the tests here
use unsmoothed values.

**What was found.** The early final-stage sessions behind Figure 4a to 4c are not in the dandiset;
they are public on Zenodo, where these claims were tested. The structs there include trials of
earlier training stages, as the Zenodo README says.
""")''')
open(p,'w').write(s)
EOF
python $TMPDIR/build_nb.py && python $TMPDIR/build_nb2.py
```

```
written 75 cells
written
```

**Agent calls Bash**

```bash
cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001169-mah-2023
type: reproduction
title: Distinct value computations in a temporal wagering task (Mah et al. 2023)
description: Tests the findings of Mah, Schiereck, Bossio and Constantinople (2023) on dandiset 001169,
  which holds 23,034 behavioral sessions of 291 rats in a temporal wagering task with hidden reward
  blocks. It reproduces the block effects on wait and trial initiation times, their dynamics at block
  transitions and their dependence on previous rewards, the comparison of inferential and
  retrospective wait time models, and the pre-initiation cue experiment, and compares the dandiset
  with the paper's processed data on Zenodo. A second notebook tests the training effects of Figure 4
  on the Zenodo structs, which hold sessions the dandiset does not.
license: Apache-2.0
notebooks:
- path: reproduce_mah_2023.ipynb
  title: Reproducing Mah et al. (2023) from dandiset 001169
  runtime_minutes: 25
- path: reproduce_mah_2023_fig4.ipynb
  title: Mah et al. (2023), Figure 4, from the paper's Zenodo deposit
  runtime_minutes: 5
helpers:
- wagering.py
related:
- id: dandi:001169/0.260825.1909
  relation: uses_data
- id: doi:10.1038/s41467-023-43250-x
  relation: reproduces
- id: doi:10.5281/zenodo.10031483
  relation: uses_data
EOF
cd  && python tools/entry.py lock entries/001169-mah-2023 2>&1 | tail -5 && python tools/entry.py check entries/001169-mah-2023 2>&1 | tail -20
```

```
wrote entries/001169-mah-2023/requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
grep -n "max.minutes\|max_minutes\|timeout" tools/entry.py | head
```

```
28:that takes longer than --max-minutes fails, even if it ran without error.
282:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
304:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
311:        if ok and seconds > max_minutes * 60:
313:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
371:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
372:    parser.add_argument("--max-minutes", type=float, default=30,
392:    return run(entry_dir, output_dir, args.timeout, args.max_minutes)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/001169-mah-2023 2>&1 | tail -30
```

```
Installed kernelspec registry-001169-mah-2023 in executed/001169-mah-2023/.venv/share/jupyter/kernels/registry-001169-mah-2023
0 error(s)
pass  reproduce_mah_2023.ipynb  (1081 s)
pass  reproduce_mah_2023_fig4.ipynb  (141 s)

real	20m32.755s
user	38m32.028s
sys	2m8.232s
```

**Agent**

Both notebooks ran clean (18 and 2.4 minutes). Checking the executed outputs against the conclusions.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import nbformat
for f in ['executed/001169-mah-2023/reproduce_mah_2023.ipynb','executed/001169-mah-2023/reproduce_mah_2023_fig4.ipynb']:
    nb=nbformat.read(f,4)
    for i,c in enumerate(nb.cells):
        if c.cell_type!='code': continue
        txt=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
        errs=[o for o in c.outputs if o.output_type=='error']
        print(f'--- [{i}] {c.metadata.get("tags")}'); print(txt[:3500] if 'RWTautowait2-2' not in txt[:200] else txt[:400]+' ...')
        if errs: print('ERROR', errs)
EOF
```

```
--- [1] None
loaded 23034 files (27.5 GB) from dandiset 001169 version 0.260825.1909 in 524 s

--- [3] ['sanity']
Assets: 23034 ; all NWB: True
Subjects (folders): 291 ; subject ids in files: 291
Sessions: 23034 ; trials: 10408925
Species in files: ['Rattus norvegicus']
Sex per rat: {'M': 184, 'F': 107}
Protocol per session: {'RWTautowait2': 22943, 'RWTautowait': 86, 'RWTautowaitWP': 5}
Training stage values in processed trials: {9: 10408925}
Subjects with an age in the files: 16 of 291
Processed and raw trial tables have the same length in every file: True
Columns of processed_trials (same in every file): True
   ['block_type', 'id', 'inter_trial_interval', 'is_catch', 'is_opt_out', 'is_rewarded', 'is_violation', 'nose_in_center', 'num_trials_in_adaptation_blocks', 'num_trials_in_mixed_blocks', 'reward_delay', 'reward_volume_ul', 'rewarded_port', 'start_time', 'stop_time', 'training_stage', 'wait_for_center_poke', 'wait_time', 'wait_time_threshold', 'wait_time_unthresholded', 'z_scored_wait_for_center_poke']
Session start times: 2019-09-27 17:54:02+00:00 to 2023-07-22 17:15:27+00:00

--- [5] ['sanity']
Sessions identical to another of the same rat (removed):
subject_id                     session_id  n_trials                                                     path
[... 335 more lines not kept]
```

**Agent**

Outputs match the conclusions. A few markdown fixes are needed; since markdown cells carry no outputs, I'll apply the same edits to the source and executed copies without a 20-minute rerun.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import nbformat
edits = {
 "entries/001169-mah-2023/reproduce_mah_2023.ipynb": [
  ("""0; in 248 rats no previous coefficient survives), larger in 262 rats and smaller in 5, p = 1.5e-44
against the paper's 1.30e-49.""", """0; in 248 rats no previous coefficient survives), larger in 262 rats and smaller in 5, p = 1.5e-44
against the paper's 1.30e-49. Nine initiation time taus are at the fit's upper bound of 10.""")],
 "entries/001169-mah-2023/reproduce_mah_2023_fig4.ipynb": [
  ("""The deposit holds all 291 rats. It has more sessions per rat than the dandiset for most rats,
which is what the Zenodo README says: these structs keep every session that ended in the final
stage, before the inclusion criteria; some trials carry earlier stage codes and no block, and
they are left out of the block measures, as the code leaves them out (its regressions drop rows
with NaN). Stage 9 is the paper's stage 8 (README). The duplicated L011 session of the dandiset is
not a concern here.""", """The deposit holds all 291 rats. It has more sessions than the dandiset for 269 rats, as the
Zenodo README leads one to expect: these structs keep every session that ended in the final stage,
before the inclusion criteria, and their first sessions hold trials of earlier stages. For 22 rats
it has fewer sessions than the dandiset, which that description does not explain. A few trials
(at most 5 per rat) have no block; they are left out of the block measures, as the code's
regressions drop rows with NaN. Stage 9 is the paper's stage 8 (README).""")],
}
for path, reps in edits.items():
    for f in (path, path.replace("entries/", "executed/")):
        nb = nbformat.read(f, 4)
        n = 0
        for c in nb.cells:
            if c.cell_type == "markdown":
                for a, b in reps:
                    if a in c.source:
                        c.source = c.source.replace(a, b); n += 1
        nbformat.write(nb, f)
        print(f, n)
EOF
# keep the scratch builders in sync
python - <<'EOF'
for p,a,b in [('/tmp/claude-1001/build_nb.py',"""against the paper's 1.30e-49.\n\"\"\")""","""against the paper's 1.30e-49. Nine initiation time taus are at the fit's upper bound of 10.\n\"\"\")""")]:
    s=open(p).read(); assert a in s; s=s.replace(a,b,1); open(p,'w').write(s)
EOF
echo ok
```

```
entries/001169-mah-2023/reproduce_mah_2023.ipynb 1
executed/001169-mah-2023/reproduce_mah_2023.ipynb 1
entries/001169-mah-2023/reproduce_mah_2023_fig4.ipynb 1
executed/001169-mah-2023/reproduce_mah_2023_fig4.ipynb 1
ok
```

**Agent**

Now the entry README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/001169-mah-2023/README.md",
 "content": "# Mah, Schiereck, Bossio & Constantinople (2023) from dandiset 001169\n\nTests the findings of [Mah et al. (2023)](https://doi.org/10.1038/s41467-023-43250-x) on\n[DANDI:001169](https://dandiarchive.org/dandiset/001169/0.260825.1909), which holds 23,034\nbehavioral sessions of 291 rats in a temporal wagering task with hidden reward blocks. The\npaper has no neural data.\n\n| Claim | Outcome |\n|---|---|\n| 291 rats, 184 male and 107 female; median 71 sessions and 33,493 trials | Reproduced |\n| The dandiset holds the paper's processed data on Zenodo | Partially reproduced (9 sessions missing, 10 rats in another order) |\n| Rats wait about 10% less for 20 uL in high than in low blocks | Reproduced |\n| Rats initiate trials faster in high than in low blocks | Reproduced |\n| Block effects on initiation times come mostly after unrewarded trials | Reproduced |\n| No difference between males and females | Reproduced |\n| Wait times converge in mixed blocks whatever the previous block | Reproduced |\n| Initiation times in mixed blocks depend on the previous block | Not reproduced (criterion's sign; see below) |\n| Regression kernels: wait times on the current reward, initiation times on previous rewards | Reproduced |\n| Time constants differ, and are not correlated | Reproduced |\n| Fast and slow initiation-time rats differ in initiation but not wait time kernels | Reproduced |\n| Previous offer: no effect on wait times (38 rats), an effect on initiation times (256 rats) | Reproduced |\n| Graded effect of catch probability; cohort sizes | Reproduced |\n| The inferential model fits wait times better than the retrospective model (BIC) | Reproduced |\n| Wait times follow the model's mistaken inferences | Reproduced |\n| Quality of inference separates wait time, not initiation time, dynamics | Reproduced |\n| A dynamic learning rate is needed for initiation time dynamics | Blocked: methods underspecified |\n| Training: wait time ratio falls gradually, initiation ratio below 1 at once (Zenodo data) | Partially reproduced |\n| Training: wait time coefficients grow, initiation coefficient stable (Zenodo data) | Reproduced |\n| Training: overshoot grows | Blocked: data missing |\n| Pre-initiation cue: initiation times follow the offer, the previous reward and the previous block | Reproduced, reproduced, not reproduced (criterion's sign) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe two claims on the dependence of initiation times on the previous block are not reproduced\nby their criteria, which assumed the dependence keeps its sign after the switch. The data show a\nstrong dependence with the sign reversed, the incentive-contrast effect the paper describes.\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/001169-mah-2023-01.yaml`](../../attempts/001169-mah-2023-01.yaml).\n\n- `reproduce_mah_2023.ipynb`: the analysis of the dandiset, and its comparison with the paper's\n  structs on Zenodo. It takes about 18 minutes: 9 to read the files, 6 to fit the models.\n- `reproduce_mah_2023_fig4.ipynb`: the training claims of Figure 4, on the structs of all\n  final-stage sessions that the paper deposited on Zenodo, which the dandiset does not hold.\n  About 3 minutes.\n- `wagering.py`: loading, the per-rat measures of the paper's code, the wait time models, and\n  reading the Zenodo structs. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/001169-mah-2023/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/001169-mah-2023-01.yaml",
 "content": "schema_version: 1\nid: 001169-mah-2023-01\ndandiset: \"001169\"\ndandiset_version: 0.260825.1909\npaper: doi:10.1038/s41467-023-43250-x\ndate: 2026-10-18\nentry: 001169-mah-2023\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\ninputs:\n- what: The paper's processed per-rat structs A_Structs_Final, compared with the dandiset in\n    zenodo-link, and A_Structs_all (every session of the final stage), on which the Figure 4 claims\n    are tested. Read from the zip archive with range requests.\n  source: Zenodo doi:10.5281/zenodo.10031483 (version 1, published.zip)\n- what: The list of the 16 rats of the pre-initiation cue experiment in Figure5.m, compared with\n    the sessions the dandiset flags with center_port_cue; the analysis parameters followed\n    throughout (named in the helper module's docstrings).\n  source: https://github.com/constantinoplelab/published (rat_behavior) at commit\n    b7b68ca8c107d8ce4a061e16da214307f175c3e5\noutcomes:\n- claim: dataset-counts\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:dataset-counts\n  measured:\n  - 291\n  - 71\n  - 33493\n  - 184\n  - 107\n  notes: The files hold 291 rats, 184 male and 107 female, with a median of 71 sessions and 33,493\n    trials per rat (sessions per rat 15 to 232), with the duplicated L011 session counted once; the\n    medians are the same with it counted twice. The Methods also give 160 male and 114 female rats\n    (274), which matches neither the files nor the paper's 291.\n- claim: zenodo-link\n  outcome: partially_reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:zenodo-link\n  notes: All 291 rats are in both. 273 rats (94%) match the Zenodo structs in full, session by\n    session in the same order, with the same trial counts and the same reward, block, catch,\n    violation, reward delivered, opt-out, wait time, trial initiation time and catch probability on\n    every trial. Ignoring order, 283 rats match. Nine struct sessions (3,645 trials, 0.035%) are\n    missing from the dandiset, in eight rats (G001 two, G022, G026, G052, G060, J011, J023, S028).\n    In 10 rats the same sessions are in another order (the dandiset by start time; the structs place\n    some sessions later, for several rats those of 2020-06-22). Every dandiset session has an\n    identical struct session once the duplicated L011 session is removed (struct 204 sessions,\n    dandiset 205). The raw trials' catch_percentage equals the structs' prob_catch in every matched\n    session.\n  deviations:\n  - Sessions are compared by trial count and values; the structs' session dates (MATLAB datetime\n    objects) are not read.\n- claim: fig1f-wait-time-block\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig1f-wait-time-block\n  measured: 10.58\n  notes: Reading (a), one minus the mean per-rat ratio, gives 10.58% and reading (b) 10.79%, both\n    within 10 +- 2.5. The signed-rank test on per-rat means of z-scored wait times finds high below\n    low, p = 4.6e-47, in 279 of 291 rats; on raw means (the code) p = 8.2e-47 against the paper's\n    8.26e-49. Males p = 3.8e-30, females p = 1.2e-18. Without the pre-cue sessions the mean ratio is\n    0.894.\n  deviations:\n  - The Methods z-score wait times for the population test; the code uses raw means. Both are shown.\n- claim: fig1i-initiation-block\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig1i-initiation-block\n  notes: 290 of 291 rats initiate faster in high than in low blocks; signed-rank p = 1.82e-49 on\n    z-scored means (the paper's value) and 1.84e-49 on raw means. Mean ratio high/low 0.562 (0.311\n    to 1.016).\n- claim: figs2-unrewarded-drive\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:figs2-unrewarded-drive\n  notes: The low minus high difference of z-scored initiation times is a median 0.347 after\n    unrewarded trials and -0.017 after rewarded ones; larger after unrewarded in 291 of 291 rats,\n    signed-rank p = 1.8e-49.\n- claim: figs12-no-sex-difference\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:figs12-no-sex-difference\n  notes: Rank-sum tests between 184 males and 107 females; wait time ratio medians 0.887 and 0.892, p\n    = 0.24; initiation time ratio medians 0.552 and 0.540, p = 0.56.\n- claim: fig2a-wait-time-converges\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2a-wait-time-converges\n  notes: Low-to-mixed minus high-to-mixed change in z-scored wait time is 0.330 before the switch\n    (trials -20 to -6) and 0.022 after it (trials +11 to +20), a ratio of 0.067; 0.170 over trials +6\n    to +20. Males -0.007, females 0.207.\n  deviations:\n  - The before and after windows and the 0.25 threshold were chosen here; the paper shows the\n    convergence in a figure without a test.\n- claim: fig2b-initiation-previous-block\n  outcome: not_reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2b-initiation-previous-block\n  notes: The difference (after low minus after high block, detrended z-scored initiation time) is\n    0.121 before the switch and -0.256 after it, a ratio of -2.12; it is below zero in 290 of 291 rats\n    (signed-rank p = 1.8e-49), and the same without detrending (ratio -2.48). The criterion required a\n    ratio of at least 0.25 and a difference above zero, so the outcome is not reproduced. The\n    dependence on the previous block is strong, with the sign reversed (faster after low, slower\n    after high blocks); that reversal is the incentive-contrast effect and overshoot the paper\n    describes for Figure 2b, so the data agree with the statement. The criterion was written with\n    the wrong sign before the analysis.\n  deviations:\n  - The criterion assumed that the dependence keeps its sign after the switch; the paper does not\n    state a sign or a test.\n- claim: fig2cd-regression-kernels\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2cd-regression-kernels\n  notes: The current-reward coefficient for wait times is above zero in 289 of 291 rats (p = 3.8e-49)\n    and the mean coefficient one back is 1.6% of it. The previous-reward coefficient for initiation\n    times is below zero in 249 rats (p = 1.3e-37); mean magnitudes 0.0307, 0.0107 and 0.0009 at 1, 3\n    and 6 back.\n  deviations:\n  - As the code does, the lagged rewards run across session boundaries and the first trials are\n    padded (zeros for wait times, NaN for initiation times).\n- claim: fig2e-tau-differ\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2e-tau-differ\n  notes: Initiation time taus median 1.63 trials (0 in 25 rats, 9 at the upper bound of 10), wait time\n    taus median 0 (0 in 248 rats); initiation larger in 262 rats, smaller in 5; signed-rank p = 1.5e-44\n    against the paper's 1.30e-49. With the code's 10 previous rewards p = 2.2e-44.\n  deviations:\n  - The exponential is fit by least squares over a grid of 5000 taus with the amplitude in closed\n    form, not by fmincon from random starts.\n  - Initiation times are regressed on 9 previous rewards (Methods); the code uses 10 (variant).\n- claim: fig2f-tau-uncorrelated\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2f-tau-uncorrelated\n  notes: Pearson r = 0.023, p = 0.70 (10 previous rewards, r = 0.023, p = 0.69; the 43 rats with a\n    wait time tau above 0, r = 0.058, p = 0.71). The paper gives r = -0.03, p = 0.53 in the legend and\n    r = 0.08, p = 0.18 in the text.\n- claim: fig2gh-fast-slow-groups\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2gh-fast-slow-groups\n  notes: Fast and slow groups of 57 and 58 rats (N = 115; 116 with 10 previous rewards). By the code's\n    test the initiation time coefficients differ (tau difference -3.0, p = 0, no shuffle of 500 as\n    extreme; paper 0.02) and the wait time coefficients do not (p = 0.21; paper 0.1). The code fits\n    the observed groups and the shuffled ones with different scaling and bounds; fitting them alike,\n    the wait time p is also 0, so the wait time part rests on that choice.\n  deviations:\n  - Exponential fits by grid search, as in fig2e-tau-differ.\n- claim: fig2j-wait-time-previous-reward\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2j-wait-time-previous-reward\n  measured: 38\n  notes: 38 rats have p < 0.05 (the paper's count). Population rank-sum p = 0.71; the code's\n    signed-rank p = 0.81 (paper 0.8). Mean z after offers below 20 uL -0.007, above 0.005.\n  deviations:\n  - The legend's rank-sum test is the main population test; the code's signed-rank test is shown.\n- claim: fig2k-initiation-previous-reward\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2k-initiation-previous-reward\n  measured: 265\n  notes: On trials offering 20 uL (Methods), 265 rats have p < 0.05 and the population rank-sum\n    test finds slower initiation after offers below 20 uL (p = 9.7e-25; 227 rats in that direction).\n    The code's reading, all mixed-block trials, gives 255 rats, 290 in that direction, and signed-rank\n    p = 1.84e-49, the paper's value, which suggests the paper's numbers come from the code's reading.\n  deviations:\n  - The Methods restrict to trials offering 20 uL; the code uses all mixed-block trials (variant).\n- claim: fig2l-sensitivity-differs\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig2l-sensitivity-differs\n  notes: Initiation time sensitivity median 0.081 against wait time -0.003; signed-rank p = 2.2e-08,\n    larger in 183 rats. With the code's all mixed-block trials p = 6.09e-38 (paper 6.21e-38).\n- claim: fig3c-catch-probability\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig3c-catch-probability\n  measured:\n  - 3\n  - 188\n  - 61\n  - 151\n  - 40\n  notes: Counts by the code's selection are within tolerance of 3, 183, 61, 151 and 39. Mean wait\n    times over rewards fall from 12.93 s at 0.15 to 11.77, 11.31 and 10.60 s at 0.2, 0.25 and 0.35 (15.32\n    s at 0.1, 3 rats). In the 59 rats with both 0.15 and 0.25, 56 wait less at 0.25 (p = 7.7e-10). The\n    second reading (any trial at the probability) gives 200 rats at 0.15 and 112 at 0.35. A catch\n    probability of 0.3 (8 rats) is in the files and not in the paper.\n- claim: fig3j-model-comparison\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig3j-model-comparison\n  notes: BIC is lower for the inferential model in 291 of 291 rats (median difference 847, 30 to 4262);\n    signed-rank p = 1.8e-49 (paper 1.07e-37). The same with n as all trials and with AIC. Baseline\n    learning rates of the retrospective model median 0.119, none at the grid's ends; 7 rats have an\n    inferential parameter at a bound.\n  deviations:\n  - Models refit here; 20 random starts where the paper used 100, no cross-validation, and the\n    retrospective model on a grid of 40 learning rates.\n  - The likelihood uses catch-trial wait times the rat opted out of, and beliefs are updated over all\n    non-violation trials; the published code holds the generative models but not the fitting, so\n    these choices are this attempt's.\n- claim: figs9-misinference\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:figs9-misinference\n  notes: Mean wait on 20 uL mixed-block catch trials 10.87 s when the model infers a high block and\n    11.91 s when it infers a low block; shorter in 230 of 291 rats, signed-rank p = 1.1e-22.\n  deviations:\n  - Beliefs are updated over all non-violation trials (see fig3j-model-comparison).\n- claim: fig3l-inference-quality\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig3l-inference-quality\n  notes: Lambda on the grid is 0 for 61 rats and 1 for 108, so the 20th and 80th percentiles fall on\n    the grid's ends and the groups are those rats. Wait times differ in the right asymptote from mixed\n    to high (p = 0.003, the paper's value) and not in the slope from mixed to low (p = 0.34; paper\n    0.02). Initiation times differ in neither (slope mixed to low p = 0.32, right asymptote mixed to\n    high p = 0.11). With the code's 40th and 60th percentiles (110 and 108 rats, 200 shuffles) the\n    initiation time slope from mixed to high differs (p = 0.0075), against the claim.\n  deviations:\n  - Lambda is fit on a grid of 11 values with the other parameters refit from the optimal model's\n    fit, which ties many rats at 0 and 1; the groups include the ties at the cuts.\n  - Logistic fits use scipy with an analytic gradient in place of fmincon.\n  - The Methods give the 20th and 80th percentiles; the code uses the 40th and 60th (variant).\n- claim: fig3h-dynamic-learning-rate\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: The paper did not fit the trial initiation time models; it simulated them with hand-chosen\n    parameters on one rat's trials (Figure3.m, FigureS7.m) and judged by eye which captures the\n    transition dynamics. No measure of capturing the dynamics is stated that a test could apply. The\n    data the simulations need (each rat's trial sequence) are in the dandiset.\n- claim: fig4a-wait-ratio-learning\n  outcome: partially_reproduced\n  notebook: reproduce_mah_2023_fig4.ipynb\n  output: claim:fig4a-wait-ratio-learning\n  notes: On the Zenodo A_Structs_all, the initiation time ratio of the first two sessions is a median\n    0.749, below 1 in 107 of 145 rats (p = 5.4e-07). The wait time ratio of the first two sessions\n    (median 0.936) is not above its value over sessions 31 to 50 (median 0.917; higher in 64 of 126\n    rats, p = 0.23) and does not differ from 1 (p = 0.87). Medians per pair fall slowly, from 0.93 to\n    0.86 to 0.89 in the last pairs, so the gradual change is small and the criterion's test does not\n    find it.\n  deviations:\n  - The test of pair 1 against sessions 31 to 50 was chosen here; the paper shows the curves.\n  - Only 132 rats have a wait time ratio in the first pair, as early sessions lack high or low blocks.\n- claim: fig4bc-regression-learning\n  outcome: reproduced\n  notebook: reproduce_mah_2023_fig4.ipynb\n  output: claim:fig4bc-regression-learning\n  notes: The magnitude of the wait time block coefficient grows from a median 0.110 (sessions 1 and\n    2) to 0.211 (sessions 31 to 50), larger in 144 of 205 rats (p = 9.3e-08); the reward coefficient\n    from 0.072 to 0.148 (148 of 205, p = 5.8e-09). The initiation time coefficient of the previous\n    reward has mean -0.0051 over both the first and the last 50 sessions (ratio 0.99; per rat p = 0.42).\n  deviations:\n  - The code smooths only the block coefficient of each rat (a loop variable left from an earlier\n    loop); the tests use unsmoothed values.\n- claim: fig4de-overshoot-learning\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Figure 4d and 4e use the per-session raw structs (S_Structs), with the sessions the processed\n    structs leave out. They are not in the dandiset, which was converted from A_Structs_Final, nor in\n    the Zenodo deposit, whose zip holds only A_Structs_Final, A_Structs_all, ModelFits and ratList.mat.\n- claim: fig5b-precue-offer\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig5b-precue-offer\n  notes: In the 762 cue sessions, the slope of z-scored initiation time on log2 offer in mixed blocks is\n    below zero in all 16 rats (-0.060 to -0.145; p = 3.1e-05), and in all 12 rats with sessions of the\n    original task it is below their slope there (-0.007 to 0.007; p = 0.00049).\n  deviations:\n  - Only the cue sessions that passed the paper's inclusion criteria are in the dandiset; the paper\n    used all of them.\n- claim: fig5c-precue-previous-reward\n  outcome: reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig5c-precue-previous-reward\n  measured: 14\n  notes: In all cue sessions, 14 of 16 rats have p < 0.05 on 20 uL trials and the population rank-sum\n    test finds slower initiation after offers below 20 uL (p = 0.04; 12 of 16 rats in that direction).\n    Fragile; the code's reading (all mixed-block trials) gives 12 rats and p = 1.9e-06, and keeping\n    only sessions after each switched rat's first 30 cue sessions in the dandiset leaves 11 rats, 10\n    with p < 0.05, population p = 0.47.\n  deviations:\n  - All cue sessions in the dandiset are used; the paper used sessions after 30 cue sessions, counted\n    over all sessions, which the dandiset does not hold.\n- claim: fig5d-precue-previous-block\n  outcome: not_reproduced\n  notebook: reproduce_mah_2023.ipynb\n  output: claim:fig5d-precue-previous-block\n  notes: In cue sessions the difference (after low minus after high block) is 0.105 before the switch\n    and -0.263 after (ratio -2.51), below zero in 15 of 16 rats (p = 9.2e-05); the same rats in the\n    original task give -2.83. The criterion required the sign to persist, so the outcome is not\n    reproduced; the dependence on the previous block is present, reversed as in fig2b.\n  deviations:\n  - The criterion assumed that the dependence keeps its sign (see fig2b-initiation-previous-block).\nfindings:\n- kind: data_missing\n  statement: Nine sessions of the paper's A_Structs_Final (3,645 trials, 0.035%) are not in the\n    dandiset, in rats G001 (two), G022, G026, G052, G060, J011, J023 and S028. Every other session of\n    the 291 rats is present with identical values.\n- kind: other\n  statement: Rat L011's session of 2022-10-04 is deposited twice, as RWTautowait2-20221004-095612 and\n    RWTautowait2-20221004-095612-x, with identical trials; the paper's struct has it once.\n- kind: other\n  statement: The processed trials table has no catch probability. The conversion's column mapping\n    spells the struct's prob_catch as prob_cacth, so it was not copied; catch_percentage in the raw\n    trials table has the same values.\n- kind: selection_undocumented\n  statement: The 762 sessions of the pre-initiation cue task (16 rats, Figure 5) are part of the main\n    data (A_Structs_Final) that Figures 1 to 3 analyse, and the Methods do not say so. In the files\n    they are marked only by the task argument center_port_cue; the session metadata and the\n    protocol name do not distinguish them.\n- kind: metadata_insufficient\n  statement: Sounds are stored as one action type (sound_output, value On) without their identity, so\n    the reward tones, the pre-initiation cue and other sounds cannot be told apart in the raw data.\n- kind: metadata_insufficient\n  statement: The training stage is 9 on every trial; the paper's final stage is stage 8, and only the\n    Zenodo README says that code 9 is that stage.\n- kind: metadata_insufficient\n  statement: Ages are missing for 275 of 291 rats; the Methods give 6 to 24 months.\n- kind: other\n  statement: For 10 rats the order of sessions differs from the paper's structs (the dandiset follows\n    start times; the structs place some sessions later, for several rats those of 2020-06-22). The\n    code's measures that cross session boundaries can differ slightly.\n- kind: other\n  statement: 456 of 23,034 sessions start with a high or low block; the Methods say the first block\n    of each session is mixed.\n- kind: other\n  statement: The files hold a catch probability of 0.3 (180,591 trials), which the paper's list of\n    catch probability cohorts (0.1, 0.15, 0.2, 0.25 and 0.35) does not include.\n- kind: data_missing\n  statement: The early final-stage sessions behind Figure 4a to 4c (A_Structs_all) are not in the\n    dandiset; they are public on Zenodo. The raw structs behind Figure 4d, 4e and Figure 5 (S_Structs,\n    with every session) are in neither.\n- kind: paper_inconsistency\n  statement: The Methods give 184 male and 107 female rats in one place and 160 male and 114 female\n    in another; the files and the paper's rat list hold 184 and 107.\n- kind: paper_inconsistency\n  statement: Figure 2f gives r = -0.03, p = 0.53 in the legend and r = 0.08, p = 0.18 in the text for the\n    same correlation; Figure 3l gives N = 116 and initiation time p = 0.15 and 0.21 in the legend and N =\n    180 and p = 0.3 and 0.2 in the text.\n- kind: code_mismatch\n  statement: The analysis code differs from the Methods in several choices that this attempt shows as\n    variants. Figure 1 tests raw means where the Methods z-score; the initiation time regression uses 10\n    previous rewards where the Methods say 9; the previous-offer analysis of initiation times uses all\n    mixed-block trials where the Methods say trials offering 20 uL; Figure 2j and 2k use signed-rank\n    tests where the legends say rank-sum; Figure 3l splits at the 40th and 60th percentiles where the\n    Methods and legend say 20th and 80th. The paper's reported p-values for Figure 2k and 2l match the\n    code's choices.\n- kind: code_mismatch\n  statement: The permutation test of Figure 2g and 2h (myTauShuffleTest.m) fits the shuffled groups to\n    10 times the coefficients with tau bounded by 50 and the observed groups to the coefficients with\n    tau bounded by 10. Fitting both alike, the wait time groups also differ (p = 0), against the\n    paper's p = 0.1.\n- kind: code_mismatch\n  statement: Figure5.m lists 20 start dates for its 16 rats, so the dates and rats do not align.\n"
}
```

```
File created successfully at: attempts/001169-mah-2023-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml,re
for f in ['attempts/001169-mah-2023-01.yaml','claims/001169/10.1038-s41467-023-43250-x.yaml']:
    d=yaml.safe_load(open(f))
    txt=open(f).read()
    # find ': ' inside values (after the key)
    for i,l in enumerate(txt.splitlines(),1):
        s=l.strip()
        if s.startswith('#'): continue
        body=re.sub(r'^-?\s*[a-z_]+:\s','',s)
        if ': ' in body: print(f,i,l)
    print(f,'ok')
c=yaml.safe_load(open('claims/001169/10.1038-s41467-023-43250-x.yaml'))
a=yaml.safe_load(open('attempts/001169-mah-2023-01.yaml'))
print(len(c['claims']), len(a['outcomes']), set(x['id'] for x in c['claims'])^set(x['claim'] for x in a['outcomes']))
EOF
python tools/entry.py check entries/001169-mah-2023
```

```
attempts/001169-mah-2023-01.yaml ok
claims/001169/10.1038-s41467-023-43250-x.yaml ok
26 26 set()
0 error(s)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import nbformat
nb=nbformat.read('executed/001169-mah-2023/reproduce_mah_2023.ipynb',4)
print(nb.cells[-1].source[:1800])
src=nbformat.read('entries/001169-mah-2023/reproduce_mah_2023.ipynb',4)
print(all(a.source==b.source for a,b in zip(nb.cells,src.cells)), len(nb.cells), len(src.cells))
nb2=nbformat.read('executed/001169-mah-2023/reproduce_mah_2023_fig4.ipynb',4); src2=nbformat.read('entries/001169-mah-2023/reproduce_mah_2023_fig4.ipynb',4)
print(all(a.source==b.source for a,b in zip(nb2.cells,src2.cells)))
EOF
git status --short
```

```
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| dataset-counts | reproduced |
| zenodo-link | partially reproduced |
| fig1f-wait-time-block | reproduced |
| fig1i-initiation-block | reproduced |
| figs2-unrewarded-drive | reproduced |
| figs12-no-sex-difference | reproduced |
| fig2a-wait-time-converges | reproduced |
| fig2b-initiation-previous-block | not reproduced (criterion's sign) |
| fig2cd-regression-kernels | reproduced |
| fig2e-tau-differ | reproduced |
| fig2f-tau-uncorrelated | reproduced |
| fig2gh-fast-slow-groups | reproduced |
| fig2j-wait-time-previous-reward | reproduced |
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la .bash_profile .bashrc .gitconfig .profile .ripgreprc .zprofile .zshrc .mcp.json scripts .idea .vscode 2>&1 | head -30; ls entries/001169-mah-2023 paper | head
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 18 15:18 scripts
entries/001169-mah-2023:
README.md
__pycache__
entry.yaml
reproduce_mah_2023.ipynb
reproduce_mah_2023_fig4.ipynb
requirements.in
requirements.lock.txt
wagering.py
```

**Agent calls Bash**

```bash
cd  rm -rf entries/001169-mah-2023/__pycache__; git check-ignore -v paper executed | head; python tools/entry.py handover entries/001169-mah-2023 && ls -R executed/001169-mah-2023/handover | head -20
```

```
.gitignore:8:paper/	paper
.gitignore:6:executed/	executed
wrote executed/001169-mah-2023/handover
executed/001169-mah-2023/handover:
10.1038-s41467-023-43250-x.yaml
reproduce_mah_2023.ipynb
reproduce_mah_2023_fig4.ipynb
wagering.py
```

**Agent calls Bash**

```bash
cd  python -c "
import nbformat
for f in ['reproduce_mah_2023.ipynb','reproduce_mah_2023_fig4.ipynb']:
    nb=nbformat.read('executed/001169-mah-2023/handover/'+f,4)
    print(f, len(nb.cells), sum('**Result' in c.source for c in nb.cells), sum('## Summary' in c.source for c in nb.cells))
"; git status --short | grep -v "^?? \.\|scripts"
```

```
reproduce_mah_2023.ipynb 53 0 0
reproduce_mah_2023_fig4.ipynb 10 0 0
?? attempts/001169-mah-2023-01.yaml
?? claims/001169/
?? entries/001169-mah-2023/
```

**Agent**

I've finished steps 1 to 5 for dandiset 001169 and run `handover` (step 6); nothing is committed. `entry.py check` reports 0 errors, and `entry.py all` passed both notebooks from a clean environment. I used the full text, which is open access (PMC10663503), saved under `paper/`.

The dandiset is pinned at 0.260825.1909. The paper cites no DANDI version, and this is the only published one; the draft has the same assets and size. The header of `reproduce_mah_2023.ipynb` says so.

### 1. Outcome per claim (26)

| Claim | Outcome |
|---|---|
| dataset-counts | reproduced |
| zenodo-link (with inputs) | partially reproduced |
| fig1f-wait-time-block | reproduced |
| fig1i-initiation-block | reproduced |
| figs2-unrewarded-drive | reproduced |
| figs12-no-sex-difference | reproduced |
| fig2a-wait-time-converges | reproduced |
| fig2b-initiation-previous-block | not reproduced (wrong sign in my criterion, see point 1 below) |
| fig2cd-regression-kernels | reproduced |
| fig2e-tau-differ | reproduced |
| fig2f-tau-uncorrelated | reproduced |
| fig2gh-fast-slow-groups | reproduced |
| fig2j-wait-time-previous-reward | reproduced |
| fig2k-initiation-previous-reward | reproduced |
| fig2l-sensitivity-differs | reproduced |
| fig3c-catch-probability | reproduced |
| fig3j-model-comparison | reproduced |
| figs9-misinference | reproduced |
| fig3l-inference-quality | reproduced |
| fig3h-dynamic-learning-rate | blocked, methods_underspecified |
| fig4a-wait-ratio-learning (Zenodo data) | partially reproduced |
| fig4bc-regression-learning (Zenodo data) | reproduced |
| fig4de-overshoot-learning | blocked, data_missing |
| fig5b-precue-offer | reproduced |
| fig5c-precue-previous-reward | reproduced (fragile) |
| fig5d-precue-previous-block | not reproduced (same wrong sign as fig2b) |

Several numbers match the paper exactly, for example 38 rats in Fig 2j, p = 1.82e-49 in Fig 1i and p = 0.003 in Fig 3l.

### 2. What was found about the dandiset
- **Completeness:** it holds 291 rats and 23,034 sessions, converted from the paper's processed data on Zenodo. 273 of 291 rats match that data exactly, trial by trial.
- **Missing sessions:** 9 sessions (3,645 trials, 0.035%) in 8 rats are missing.
- **Duplicate:** one session of rat L011 is deposited twice (a second copy with a `-x` suffix).
- **Session order:** 10 rats have their sessions in a different order from the Zenodo data.
- **Raw events:** the raw Bpod events agree with the processed initiation and wait times to about 1e-11 s.
- **Missing catch probability:** the processed table has no catch probability, because the conversion code misspells `prob_catch` as `prob_cacth`. The raw trials table has the same values.
- **Pre-cue sessions:** the 762 sessions of the Figure 5 pre-cue task are mixed into the main data. Only a task argument, `center_port_cue`, marks them, and the Methods don't mention it. Sounds are stored without their identity, so the raw data can't confirm that flag.
- **Metadata:** training stage is coded 9 without saying it is the paper's stage 8, ages are missing for 275 rats, and 456 sessions start with a high or low block although the Methods say every session starts mixed.
- **Data elsewhere:** the early sessions behind Figure 4 are only on Zenodo. The raw per-session structs behind Fig 4d, 4e and Fig 5 are not public anywhere.
- **Paper and code:** I recorded paper inconsistencies (two different male/female counts, two different r values for Fig 2f) and several places where the code differs from the Methods.

### 3. Where the protocol was unclear, wrong or missing something
1. **A criterion written wrong before the analysis.** For fig2b and fig5d I assumed the dependence on the previous block keeps its sign. The data show it reversed, which is the incentive-contrast effect the paper itself describes. The protocol only covers ties, not a criterion that turns out mis-specified. I judged by the letter (not reproduced), explained it in the notes, and left any change to the revision after verifier round 1.
2. **Methods versus code versus "several readings".** For fig2k the Methods say trials offering 20 uL, the code uses all mixed-block trials, and the paper's p-values match the code. The two rules point different ways. I used the Methods as the main result and showed the code as a variant.
3. **The paper's own deposit as outside data.** The Zenodo data is what the dandiset was converted from. I made a standalone `with_inputs` link claim that nothing depends on, and tested Figure 4 as `elsewhere`, although that data partly overlaps the dandiset.
4. **Tolerances.** I used 0 for exact counts and ±2.5 points for "~10 percent", each with a reason given in the claims file.
5. **"Stream, do not download".** Range-request streaming took about 5 s per file, too slow for 23k files. Each ~1 MB file is read whole into memory instead, never to disk; the notebook header says so.
6. **Runtime.** The 10-minute aim isn't reachable: reading 23k files alone takes 9 minutes. The main notebook takes 18 minutes, under the 30-minute limit.
7. **Clock check.** The suggested decoding check doesn't fit behaviour-only data. I compared the processed times against the raw events on 24 random sessions instead.
8. **Ties at a percentile cut.** Fitting lambda on a grid left many rats tied at 0 and 1, so the 20th/80th percentile cut fell on the ties. I included the tied rats in each group and recorded it as a deviation.
9. **MATLAB optimiser not available.** I replaced fmincon with scipy and a grid search, and recorded it as a deviation rather than calling the method not runnable.

### 4. Runtime and failures
`entry.py all` took 20.5 minutes: 1,081 s for the main notebook and 141 s for the Figure 4 notebook.

Failures during development, all fixed before the final run:
- Zenodo returned 429 (too many requests) to parallel range reads, so the loader now reads them with one range request.
- A pickling error in the raw-event check.
- A NaN bug in the exponential fit.
- An empty percentile split before I handled the ties.

My first draft of the conclusions had placeholder numbers. All of them were rewritten from the executed outputs.

Two markdown corrections were applied identically to the source notebooks and the executed copies, without re-running, since markdown cells carry no outputs.

The root-level untracked entries (`.bashrc`, `scripts`, and others) are sandbox device mounts, not files I created. They should stay out of the commit.

## End of run

98 turns, 122 minutes, result: success.
