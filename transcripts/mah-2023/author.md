# mah-2023 · author · run 45502816457

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools; wc -l docs/*.md README.md
```

```
Tue Nov 24 22:42:56 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
protocol.lock
[... 1154 more lines not kept]
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
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
[... 760 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/mah-2023.yaml; ls papers/datasets/ | grep mah; cat papers/datasets/mah-2023.yaml; ls papers/author-notes 2>/dev/null | grep mah; ls questions | grep mah
```

```
<persisted-output>
Output too large (54.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/eebaac5e-fdc7-4613-8c99-dddd3fff97a2/tool-results/b3w31u0df.txt

Preview (first 2KB):
# Claims for Mah, Schiereck, Bossio & Constantinople (2023), "Distinct value computations support
# rapid sequential decisions", Nature Communications 14, 7573, doi:10.1038/s41467-023-43250-x,
# tested on DANDI:001169 (primary; the dandiset's title is the paper's and its description is the
# paper's abstract, so it is meant to hold the behavioral data of the 291 rats).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. paper/10.1038-s41467-023-43250-x.txt, the version of record as served by Europe PMC
# (PMC10663503), with the main text, figure legends, Methods, Data and Code availability, and three
# supplement files extracted from their PDFs. Supplement 1 (MOESM1) is the Supplementary
# Information, Supplementary Figs 1 to 14 with legends; supplement 2 is the peer review file;
# supplement 3 is the reporting summary. No PDF of the main article was supplied; none was needed,
# as the text of every legend and table was legible. Source Data are not in the text read.
#
# Code read. github.com/constantinoplelab/published, folder rat_behavior, at commit b7b68ca8c107
# (HEAD, 2026-09-25; the folder was last changed in commit 87fd4a40b3, 2024-09-20, and its files
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/mah-2023.yaml"
}
```

```
1	# Claims for Mah, Schiereck, Bossio & Constantinople (2023), "Distinct value computations support
2	# rapid sequential decisions", Nature Communications 14, 7573, doi:10.1038/s41467-023-43250-x,
3	# tested on DANDI:001169 (primary; the dandiset's title is the paper's and its description is the
4	# paper's abstract, so it is meant to hold the behavioral data of the 291 rats).
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
6	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
7	#
8	# Text read. paper/10.1038-s41467-023-43250-x.txt, the version of record as served by Europe PMC
9	# (PMC10663503), with the main text, figure legends, Methods, Data and Code availability, and three
10	# supplement files extracted from their PDFs. Supplement 1 (MOESM1) is the Supplementary
11	# Information, Supplementary Figs 1 to 14 with legends; supplement 2 is the peer review file;
12	# supplement 3 is the reporting summary. No PDF of the main article was supplied; none was needed,
13	# as the text of every legend and table was legible. Source Data are not in the text read.
14	#
15	# Code read. github.com/constantinoplelab/published, folder rat_behavior, at commit b7b68ca8c107
16	# (HEAD, 2026-09-25; the folder was last changed in commit 87fd4a40b3, 2024-09-20, and its files
17	# were uploaded in f3cb954ef7, 2023-10-22). It holds MATLAB scripts that redraw each figure
18	# (Figures/Figure1.m to Figure5.m, FigureS1.m to FigureS14.m), the analyses they call (Analysis/:
19	# wtcurves, iticurves, waittime_20ul_by_previous_vol, latency_post20ul_by_previous_vol,
20	# regress_wt_vs_rew, regress_latency_vs_rew, block_dynamics_wt, block_dynamics_latency,
[... 821 more lines not kept]
```

**Agent calls Bash**

```bash
ls papers/datasets/ | grep -i mah; cat papers/datasets/mah-2023.yaml 2>/dev/null; ls papers/author-notes 2>/dev/null | grep mah; ls questions | grep mah; ls entries/mah-2023 -la
```

```
Exit code 2
mah-2023.yaml
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1038/s41467-023-43250-x
title: Distinct value computations support rapid sequential decisions
datasets:
- archive: dandi
  id: 001169
  relation: primary
ls: cannot access 'entries/mah-2023': No such file or directory
```

**Agent calls Bash**

```bash
sed -n 1,148p README.md | head -80; grep -n "DANDI" -A60 docs/archives.md | head -120
```

```
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

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -150
```

```
total 132
drwxr-xr-x   2 runner runner  4096 Nov 24 22:38 .
drwxr-xr-x 350 runner runner 12288 Nov 24 22:42 ..
-rw-r--r--   1 runner runner  2144 Nov 24 22:38 README.md
-rw-r--r--   1 runner runner   907 Nov 24 22:38 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 24 22:38 omr.py
-rw-r--r--   1 runner runner 79403 Nov 24 22:38 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 24 22:38 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 24 22:38 requirements.lock.txt
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
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/fouke-2025-01.yaml | grep -v "^    " | head -80; ls schemas; python -c "import json;print(1)"; grep -n "findings:" -A25 attempts/fouke-2025-01.yaml | head -40
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
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001169/versions/0.261120.1450/info/" | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('asset_count'),d.get('size'));m=d['metadata'];print(m['name']);print(m.get('description')[:3000]);print(json.dumps(m.get('assetsSummary'),indent=0)[:2000]); print(m.get('doi'))"; curl -s "https://api.dandiarchive.org/api/dandisets/001169/versions/" | python -m json.tool | grep -E '"version"|modified|created' | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import requests, json, time
t=time.time()
url="https://api.dandiarchive.org/api/dandisets/001169/versions/0.261120.1450/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r['results']; url=r['next']
print(len(out), time.time()-t)
json.dump(out, open('assets.json','w'))
import collections
print(out[:3])
sizes=[a['size'] for a in out]; import numpy as np; print(np.percentile(sizes,[0,50,100]))
subs=collections.Counter(a['path'].split('/')[0] for a in out); print(len(subs), np.median(list(subs.values())))
nonnwb=[a['path'] for a in out if not a['path'].endswith('.nwb')]; print(nonnwb[:10])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q requests numpy pandas scipy h5py remfile pynwb matplotlib statsmodels jupyter nbconvert ipykernel 2>&1 | tail -2; python -c "import pynwb,h5py;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import requests, json, time
t=time.time()
url="https://api.dandiarchive.org/api/dandisets/001169/versions/0.261120.1450/assets/?page_size=1000"
out=[]
while url:
    r=requests.get(url).json(); out+=r['results']; url=r['next']
print(len(out), time.time()-t)
json.dump(out, open('assets.json','w'))
import collections
print(out[:2])
sizes=[a['size'] for a in out]; import numpy as np; print(np.percentile(sizes,[0,50,100]))
subs=collections.Counter(a['path'].split('/')[0] for a in out); print(len(subs), np.median(list(subs.values())), min(subs.values()), max(subs.values()))
nonnwb=[a['path'] for a in out if not a['path'].endswith('.nwb')]; print(nonnwb[:10])
EOF
```

```
23033 7.574567079544067
[{'asset_id': 'cf0152c3-5567-49ee-a0ec-3887c9589d6b', 'blob': '3d0a3028-e102-48eb-9040-06e7fdb4824a', 'zarr': None, 'path': 'sub-E006/sub-E006_ses-RWTautowait2-20220126-132803.nwb', 'size': 854686, 'created': '2026-11-18T16:49:17.481208Z', 'modified': '2026-11-20T14:50:48.444293Z'}, {'asset_id': '433ea67b-0ea8-414f-8ba5-71fecbeecf0e', 'blob': '7fb08fdd-adbb-4199-be05-d224a5ec6c46', 'zarr': None, 'path': 'sub-E006/sub-E006_ses-RWTautowait2-20220125-134556.nwb', 'size': 1209812, 'created': '2026-11-18T16:49:18.493889Z', 'modified': '2026-11-20T14:50:48.454935Z'}]
[ 669201. 1178664. 7283277.]
291 71.0 15 232
[]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json, h5py, io, requests, time, pynwb
a=json.load(open('assets.json'))[1]
t=time.time()
b=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/").content
print(len(b), time.time()-t)
f=h5py.File(io.BytesIO(b),'r')
def show(n,o):
    if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype, dict(o.attrs).get('description',''))
    else: print(n, {k:(v if not isinstance(v,bytes) else v.decode()) for k,v in o.attrs.items() if k not in ('namespace','object_id')})
f.visititems(show)
io_=pynwb.NWBHDF5IO(file=f,mode='r',load_namespaces=True); nwb=io_.read()
print(nwb)
print(nwb.subject)
EOF
```

```
1209812 0.529937744140625
acquisition {}
acquisition/task_recording {'neurodata_type': 'TaskRecording'}
acquisition/task_recording/actions {'colnames': array(['timestamp', 'action_type', 'value'], dtype=object), 'description': 'Contains the onset times of the task output actions (e.g. LED turned on/off).', 'neurodata_type': 'ActionsTable'}
acquisition/task_recording/actions/action_type (2916,) int64 The action type
acquisition/task_recording/actions/id (2916,) int64 
acquisition/task_recording/actions/timestamp (2916,) float64 The action time
acquisition/task_recording/actions/value (2916,) object The action value
acquisition/task_recording/events {'colnames': array(['timestamp', 'event_type', 'value'], dtype=object), 'description': 'Contains the onset times of events in the task.', 'neurodata_type': 'EventsTable'}
acquisition/task_recording/events/event_type (13015,) int64 The event type
acquisition/task_recording/events/id (13015,) int64 
acquisition/task_recording/events/timestamp (13015,) float64 The event timestamp
acquisition/task_recording/events/value (13015,) object The event value
acquisition/task_recording/states {'colnames': array(['start_time', 'stop_time', 'state_type'], dtype=object), 'description': 'Contains the start and end times of each state in the task.', 'neurodata_type': 'StatesTable'}
acquisition/task_recording/states/id (2260,) int64 
acquisition/task_recording/states/start_time (2260,) float64 Start time of epoch, in seconds
acquisition/task_recording/states/state_type (2260,) int64 The state type
acquisition/task_recording/states/stop_time (2260,) float64 Stop time of epoch, in seconds
analysis {}
file_create_date (1,) object 
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/mah-2023; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json, h5py, io, requests, time, numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor
A=json.load(open('assets.json'))
s=requests.Session()
ad=requests.adapters.HTTPAdapter(pool_maxsize=32); s.mount('https://',ad)
def load(a):
    b=s.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/").content
    with h5py.File(io.BytesIO(b),'r') as f:
        g=f['intervals/processed_trials']
        d={k:g[k][:] for k in g.keys() if k!='id'}
        sub={k:f['general/subject/'+k][()] for k in f['general/subject'].keys()}
        ss=f['session_start_time'][()]
    return a['path'],d,sub,ss
rng=np.random.default_rng(0); idx=rng.choice(len(A),96,replace=False)
t=time.time()
with ThreadPoolExecutor(24) as ex: R=list(ex.map(load,[A[i] for i in idx]))
print('t',time.time()-t)
p,d,sub,ss=R[0]; print(p,sub,ss); 
for k,v in d.items(): print(k,v.dtype,v[:5])
import collections
print(collections.Counter(int(x) for r in R for x in np.unique(r[1]['training_stage'])))
print(collections.Counter(x for r in R for x in np.unique(r[1]['block_type'])))
print(collections.Counter(float(x) for r in R for x in np.unique(r[1]['catch_percentage'])))
print(collections.Counter(int(x) for r in R for x in np.unique(r[1]['reward_volume_ul'])))
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
```

```
t 2.42130446434021
sub-J037/sub-J037_ses-RWTautowait2-20220719-115525.nwb {'date_of_birth': b'2021-11-24T00:00:00-05:00', 'description': b'Vendor: BRED', 'sex': b'M', 'species': b'Rattus norvegicus', 'subject_id': b'J037'} b'2022-07-19T11:56:48-04:00'
block_type object [b'Mixed' b'Mixed' b'Mixed' b'Mixed' b'Mixed']
catch_percentage float64 [0.2 0.2 0.2 0.2 0.2]
inter_trial_interval float64 [80.0016 64.2072 81.5092 33.3679  0.1568]
is_catch bool [False False False False False]
is_opt_out bool [False False False False False]
is_rewarded bool [False False False False False]
is_violation bool [ True  True  True  True  True]
nose_in_center float64 [0.88456    0.90415933 0.95792602 0.9388556  1.03193966]
num_trials_in_adaptation_blocks int64 [40 40 40 40 40]
num_trials_in_mixed_blocks int64 [40 40 40 40 40]
reward_delay float64 [10.1564      0.91334218  5.56047874  0.5971818   0.92264947]
reward_volume_ul int64 [20 20 20 20 20]
rewarded_port object [b'Left' b'Left' b'Left' b'Right' b'Right']
start_time float64 [ 14.4207  95.6158 161.0804 243.7245 278.3162]
stop_time float64 [ 95.5447 160.9846 243.6522 278.2433 280.5017]
training_stage int64 [9 9 9 9 9]
wait_for_center_poke float64 [    nan 64.2072 81.5092 33.3679  0.1568]
wait_time float64 [nan nan nan nan nan]
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "^Methods\|Criteria for including\|Statistical analyses\|Trial history effects\|Block transition dynamics\|Learning dynamics\|Pre-initiation cue task\|Behavioral models\|Fitting and evaluating\|Data availability\|Code availability" paper/10.1038-s41467-023-43250-x.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
t=open('paper/10.1038-s41467-023-43250-x.txt').read()
i=t.find('Criteria for including behavioral data')
j=t.find('Training for male and female')
k=t.find('Behavioral model')
print([ (s,t.find(s)) for s in ['Methods','Subjects','Criteria for including behavioral data','Statistical analyses','Trial history effects','Block transition dynamics','Learning dynamics','Pre-initiation cue task','Inferential model','Retrospective model','Fitting and evaluating','Data availability','Training for male','Supplementary Fig. 1 ']])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41467-023-43250-x.txt').read()
import textwrap
print(textwrap.fill(t[37373:49000],200))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41467-023-43250-x.txt').read()
import textwrap
print(textwrap.fill(t[62000:78500],200))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && for f in Figures/Figure5.m Figures/Figure1.m Figures/Figure2.m Figures/Figure3.m Figures/Figure4.m utils/getITI.m utils/parse_data_from_mysql.m utils/screen_perf.m Analysis/wtcurves.m Analysis/iticurves.m Analysis/block_dynamics_wt.m Analysis/block_dynamics_latency.m Analysis/regress_wt_vs_rew.m Analysis/regress_latency_vs_rew.m Analysis/waittime_20ul_by_previous_vol.m Analysis/latency_post20ul_by_previous_vol.m Analysis/myTauShuffleTest.m Analysis/macro_regress_overtraining_V2.m Figures/FigureS2.m Figures/FigureS12.m Figures/FigureS14.m; do mkdir -p code/$(dirname $f); curl -sf -o code/$f https://raw.githubusercontent.com/constantinoplelab/published/b7b68ca8c107/rat_behavior/$f || echo MISSING $f; done; ls -R code | head -40; wc -l code/*/*.m | tail -1
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s https://api.github.com/repos/constantinoplelab/published/commits/b7b68ca8c107 | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['sha'],d['commit']['committer']['date'])"; sed -n 1,80p code/Figures/Figure5.m
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json,collections
A=json.load(open('assets.json'))
subs=collections.Counter(a['path'].split('/')[0][4:] for a in A)
for r in ['M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047','M048', 'G070', 'E005', 'E008', 'G078', 'G076','G069', 'S042', 'S050']:
    print(r, subs.get(r))
print(sorted(collections.Counter(s[0] for s in subs).items()))
# session id naming
print(collections.Counter(a['path'].split('_ses-')[1].split('-')[0] for a in A))
EOF
```

```
M041 98
M042 76
M043 119
M044 150
M045 69
M046 57
M047 69
M048 73
G070 106
E005 80
E008 152
G078 129
G076 108
G069 202
S042 81
S050 33
[('C', 5), ('E', 8), ('G', 84), ('J', 78), ('L', 32), ('M', 37), ('S', 47)]
Counter({'RWTautowait2': 22942, 'RWTautowait': 86, 'RWTautowaitWP': 5})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json, h5py, io, requests
A=json.load(open('assets.json'))
m=sorted([a for a in A if a['path'].startswith('sub-M041/')], key=lambda a:a['path'])
print([a['path'].split('_ses-')[1] for a in m][::8])
def args(a):
    b=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/").content
    f=h5py.File(io.BytesIO(b),'r'); g=f['general/task/task_arguments']
    st=[x.decode() for x in f['general/task/state_types/state_name'][:]]
    ev=[x.decode() for x in f['general/task/event_types/event_name'][:]]
    return {n.decode():e.decode() for n,e in zip(g['argument_name'][:],g['expression'][:])}, {n.decode():e.decode() for n,e in zip(g['argument_name'][:],g['argument_description'][:])},st,ev, f['general/protocol'][()]
pre=[a for a in m if '2022-09' in a['path'] or '202209' in a['path']][-1]; post=[a for a in m if '202211' in a['path']][0]
x1,d,s1,e1,p1=args(pre); x2,_,s2,e2,p2=args(post)
print(pre['path'],post['path'],p1,p2)
for k in sorted(set(x1)|set(x2)): print(k, x1.get(k), x2.get(k), '|', d.get(k,'')[:80])
print(s1);print(s2);print(e1,e2)
wp=[a['path'] for a in A if 'WP' in a['path'] or 'RWTautowait-' in a['path']]; import collections; print(collections.Counter(p.split('/')[0] for p in wp))
EOF
```

```
['RWTautowait2-20220607-115041.nwb', 'RWTautowait2-20220623-120017.nwb', 'RWTautowait2-20220711-114907.nwb', 'RWTautowait2-20220721-115656.nwb', 'RWTautowait2-20220804-115417.nwb', 'RWTautowait2-20220817-120012.nwb', 'RWTautowait2-20220829-121408.nwb', 'RWTautowait2-20220912-114428.nwb', 'RWTautowait2-20221004-113853.nwb', 'RWTautowait2-20221031-111940.nwb', 'RWTautowait2-20221110-121027.nwb', 'RWTautowait2-20221122-121950.nwb', 'RWTautowait2-20221214-114206.nwb']
sub-M041/sub-M041_ses-RWTautowait2-20220930-112130.nwb sub-M041/sub-M041_ses-RWTautowait2-20221101-113212.nwb b'RWTautowait2' b'RWTautowait2'
auto_change_catch_probability True True | Whether to change the probability automatically after a certain number of trials
block_type Mixed Mixed | The block type (High, Low or Mixed). High and Low blocks are high reward (20, 40
catch_percentage 0.15 0.15 | The percentage of catch trials.
center_port_cue None True | 
changed False False | Whether a block transition occurred for the trial.
cumulative_reward_volume_ul 0 0 | The cumulative volume received during session in microliters.
current_trial 0 0 | The current trial number.
high_ITI 0 0 | Task parameter.
is_catch False False | The 'IsCatch' value saved in the Bpod trial settings. This can differ from 'is_c
is_warm_up False False | Whether the trial is warm-up.
min_reward_volume_ul 5 5 | The minimum volume of reward in microliters. (The minimum volume is 4 ul for fem
nose_in_center 0.9641205823837127 1.020225165090996 | The time in seconds when the animal is required to maintain center port to initi
num_trials_in_adaptation_blocks 40 40 | The number of trials in each high reward (20, 40, or 80μL) or low reward (5, 10,
num_trials_in_mixed_blocks 40 40 | The number of trials in each mixed blocks.
num_trials_in_stage_3 400 400 | Determines how many trials occur in stage 3 before transition.
num_trials_in_stage_8 250 250 | Determines how many trials occur in stage 8 before transition.
override_nose_in_center False Fal
[... 16 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/mah-2023/mah2023.py",
 "content": "\"\"\"Loading and shared measures for the reproduction of Mah et al. (2023) on DANDI:001169.\n\nEvery NWB file of the pinned version is fetched over HTTPS into memory (no file is written to\ndisk) and read with h5py. The files are about 1 MB each, so one request per file is much faster\nthan range requests; the 23,033 files are read in parallel threads. Only the processed trials\ntable, the subject, the session start time and the task argument `center_port_cue` are kept.\n\nWhere each parameter comes from:\n- Volumes: female volumes 4, 8, 16, 32, 64 uL are treated as 5, 10, 20, 40, 80 uL (claims file\n  header; Methods, \"Training for male and female rats\").\n- Wait times: the dandiset's `wait_time` column, which already removes wait times above the\n  rat's pooled catch-trial mean + 1 SD (`wait_time_threshold`; Methods, \"Statistical analyses\",\n  paragraph 1). Only opt-out catch trials have a wait time (claims file header).\n- Trial initiation time: the dandiset's `inter_trial_interval` (\"the time between the end of the\n  consummatory period and the time to initiate the next trial\"), which is the paper's definition\n  (Results, paragraph 1: \"the time from opting out or consuming reward to initiating a new\n  trial\"). Values above the rat's pooled 99th percentile are removed (Methods, \"Criteria for\n  including behavioral data\"; claims file header).\n- z-scoring is within rat over the trials each analysis names (claims file header).\n\"\"\"\nimport io\nimport json\nimport time\nimport urllib.request\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\n\nDANDISET = \"001169\"\nVERSION = \"0.261120.1450\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nVOL_MAP = {4: 5, 8: 10, 16: 20, 32: 40, 64: 80, 5: 5, 10: 10, 20: 20, 40: 40, 80: 80}\nBLOCK_CODE = {b\"Mixed\": 1, b\"High\": 2, b\"Low\": 3}  # the code's coding: 1 mixed, 2 high, 3 low\n\nCOLS = [\"start_time\", \"training_stage\", \"is_catch\", \"catch_percentage\", \"reward_volume_ul\",\n        \"reward_delay\", \"block_type\", \"is_rewarded\", \"is_violation\", \"is_opt_out\", \"wait_time\",\n        \"wait_time_unthresholded\", \"wait_time_threshold\", \"wait_for_center_poke\",\n        \"inter_trial_interval\"]\n\n\ndef _get(url, tries=5):\n    for i in range(tries):\n        try:\n            with urllib.request.urlopen(url, timeout=120) as r:\n                return r.read()\n        except Exception:\n            if i == tries - 1:\n                raise\n            time.sleep(2 * (i + 1))\n\n\ndef list_assets():\n    \"\"\"All assets of the pinned version, from the DANDI REST API.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=1000\"\n    out = []\n    while url:\n        r = json.loads(_get(url))\n        out += r[\"results\"]\n        url = r[\"next\"]\n    return out\n\n\ndef version_info():\n    return json.loads(_get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/info/\"))\n\n\ndef _read_session(asset):\n    b = _get(f\"{API}/assets/{asset['asset_id']}/download/\")\n    with h5py.File(io.BytesIO(b), \"r\") as f:\n        g = f[\"intervals/processed_trials\"]\n        d = {k: g[k][:] for k in COLS}\n        n_raw = f[\"intervals/trials/id\"].shape[0]\n        ta = f[\"general/task/task_arguments\"]\n        args = {n.decode(): e.decode() for n, e in zip(ta[\"argument_name\"][:], ta[\"expression\"][:])}\n        meta = dict(\n            path=asset[\"path\"],\n            subject=f[\"general/subject/subject_id\"][()].decode(),\n            sex=f[\"general/subject/sex\"][()].decode(),\n            start=f[\"session_start_time\"][()].decode(),\n            protocol=f[\"general/protocol\"][()].decode(),\n            center_port_cue=args.get(\"center_port_cue\", \"absent\"),\n            n_trials=len(d[\"start_time\"]),\n            n_raw_trials=n_raw,\n        )\n    return meta, d\n\n\ndef load_all(assets, workers=24):\n    \"\"\"Read every session. Returns (sessions, trials) DataFrames; trials hold a `sess` index.\"\"\"\n    with ThreadPoolExecutor(workers) as ex:\n        res = list(ex.map(_read_session, assets))\n    sessions = pd.DataFrame([m for m, _ in res])\n    sessions[\"start\"] = pd.to_datetime(sessions[\"start\"], utc=True)\n    # order sessions within each rat by start time\n    order = sessions.sort_values([\"subject\", \"start\"]).index.to_numpy()\n    sessions = sessions.loc[order].reset_index(drop=True)\n    parts = []\n    for new_i, old_i in enumerate(order):\n        d = res[old_i][1]\n        df = pd.DataFrame({k: d[k] for k in COLS if k != \"block_type\"})\n        df[\"block\"] = np.array([BLOCK_CODE.get(x, 0) for x in d[\"block_type\"]], dtype=np.int8)\n        df[\"sess\"] = new_i\n        df[\"trial\"] = np.arange(len(df), dtype=np.int32)\n        parts.append(df)\n    trials = pd.concat(parts, ignore_index=True)\n    trials[\"subject\"] = sessions[\"subject\"].to_numpy()[trials[\"sess\"].to_numpy()]\n    trials[\"vol\"] = trials[\"reward_volume_ul\"].map(VOL_MAP).astype(\"Int64\")\n    sessions[\"sess_in_rat\"] = sessions.groupby(\"subject\").cumcount()\n    return sessions, trials\n\n\ndef add_measures(trials):\n    \"\"\"Per-rat measures shared by the claims (see the module docstring for their sources).\n\n    wt: wait time on opt-out catch trials (thresholded, as deposited); NaN elsewhere.\n    iti: trial initiation time with values above the rat's pooled 99th percentile removed.\n    z_wt: wt z-scored within rat over all its catch trials with a wait time.\n    z_iti: iti z-scored within rat over all its trials.\n    \"\"\"\n    t = trials\n    catch_oo = t[\"is_catch\"].to_numpy() & t[\"is_opt_out\"].to_numpy()\n    t[\"wt\"] = np.where(catch_oo, t[\"wait_time\"].to_numpy(), np.nan)\n    t[\"wt_raw\"] = np.where(catch_oo, t[\"wait_time_unthresholded\"].to_numpy(), np.nan)\n    p99 = t.groupby(\"subject\")[\"inter_trial_interval\"].transform(lambda x: np.nanpercentile(x, 99))\n    t[\"iti\"] = t[\"inter_trial_interval\"].where(t[\"inter_trial_interval\"] <= p99)\n    for c in [\"wt\", \"iti\"]:\n        g = t.groupby(\"subject\")[c]\n        t[\"z_\" + c] = (t[c] - g.transform(\"mean\")) / g.transform(\"std\")\n    # previous trial within the session\n    sess = t[\"sess\"].to_numpy()\n    same = np.r_[False, sess[1:] == sess[:-1]]\n    for c in [\"vol\", \"is_rewarded\", \"block\"]:\n        prev = t[c].shift(1)\n        t[\"prev_\" + c] = prev.where(same)\n    return t\n\n\ndef wilcoxon_p(x, y=None, alternative=\"two-sided\"):\n    from scipy.stats import wilcoxon\n    return wilcoxon(x, y, alternative=alternative).pvalue\n"
}
```

```
File created successfully at: entries/mah-2023/mah2023.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q pyarrow && date -u && time python - <<'EOF'
import sys, time, resource; sys.path.insert(0,'entries/mah-2023')
import mah2023 as M
t=time.time(); A=M.list_assets(); print(len(A), time.time()-t)
S,T=M.load_all(A, workers=32)
print(time.time()-t, len(S), len(T), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
S.to_parquet('sessions.parquet'); T.to_parquet('trials.parquet')
print(T.memory_usage(deep=True).sum()/1e9)
EOF
```

```
Tue Nov 24 22:45:31 UTC 2026
23033 7.920737266540527
470.4044032096863 23033 10408699 4.49822
1.228226614

real	7m54.714s
user	6m14.420s
sys	2m1.469s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pandas as pd, numpy as np
S=pd.read_parquet('sessions.parquet'); T=pd.read_parquet('trials.parquet')
print(S.subject.nunique(), S.groupby('subject').size().median(), T.groupby('subject').size().median())
print(S.drop_duplicates('subject').sex.value_counts())
print(S.center_port_cue.value_counts()); print(S[S.center_port_cue!='absent'].groupby(['subject','center_port_cue']).size().unstack())
print(S.protocol.value_counts())
print(T.training_stage.value_counts())
print(T.catch_percentage.value_counts())
print(T.block.value_counts()); print(T.reward_volume_ul.value_counts())
print((S.n_trials==S.n_raw_trials).mean())
print(T[['wait_time','wait_time_unthresholded','inter_trial_interval','wait_for_center_poke','reward_delay']].describe().T)
print(pd.crosstab(T.is_catch, T.is_opt_out), pd.crosstab(T.is_rewarded,T.is_violation))
print(S.start.min(), S.start.max())
EOF
```

```
291 71.0 33493.0
sex
M    184
F    107
Name: count, dtype: int64
center_port_cue
absent    16274
False      5997
True        762
Name: count, dtype: int64
center_port_cue  False  True
subject                     
E005              11.0  15.0
E008               1.0  73.0
G067               5.0   NaN
G069               1.0  75.0
G070              10.0  37.0
...                ...   ...
S059              87.0   NaN
S060              65.0   NaN
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat Analysis/block_dynamics_wt.m | grep -v "^\s*%" | head -120
```

```
function [ltom, htom, mtol, mtoh, ltom_incong, htom_incong, sems] =...
    block_dynamics_wt(A, twin, smoothfactor, varargin)
  
if isfield(A, 'pd') %just in case the input is an S struct.
    [A, ~, ~] = parse_data_from_mysql(A);
end
[~, A.reward] = convertreward(A.reward);

A.wait_time(logical(A.catch)) = (A.wait_time(logical(A.catch))-...
    mean(A.wait_time(logical(A.catch)), 'omitnan'))./...
    std(A.wait_time(logical(A.catch)), 'omitnan');

A = deltawt(A); 

if isempty(varargin)
    dropthese = true(size(A.wait_time));
else
    dropthese = varargin{1};
end
A.wait_time(~dropthese) = nan;
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n '/^function \[lowtomix/,$p' Analysis/block_dynamics_wt.m | grep -v "^\s*%"; grep -v "^\s*%" Analysis/block_dynamics_latency.m | sed -n 1,80p
```

```
function [lowtomix, hightomix,...
    mixtolow, mixtohigh,...
    lowtomix_incong, hightomix_incong] =...
    find_block_transition(A)

ntrials = [0; cumsum(A.ntrials)];

[~, treal, tincong] = blockhmat_withvios(A);

lowtomix = cell(length(ntrials), 1);
hightomix = cell(length(ntrials), 1);
mixtolow = cell(length(ntrials), 1);
mixtohigh = cell(length(ntrials), 1);
lowtomix_incong = cell(length(ntrials), 1);
hightomix_incong = cell(length(ntrials), 1);

for sess = 1:length(ntrials)-1
    lowtomix{sess} = (find(treal(sess,:) == -2) + ntrials(sess))';
    hightomix{sess} = (find(treal(sess,:) == -1) + ntrials(sess))';
    
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pandas as pd, numpy as np
from scipy import stats
S=pd.read_parquet('sessions.parquet'); T=pd.read_parquet('trials.parquet')
c=T[T.is_catch & T.is_opt_out][['sess','wait_time_unthresholded','vol']].dropna()
res=[]
for s,g in c.groupby('sess'):
    w=g.wait_time_unthresholded.to_numpy(); v=g.vol.to_numpy().astype(float)
    k=w<=w.mean()+2*w.std()
    if k.sum()<3: res.append((s,np.nan,np.nan,k.sum())); continue
    r=stats.linregress(v[k],w[k]); res.append((s,r.slope,r.pvalue,k.sum()))
R=pd.DataFrame(res,columns=['sess','slope','p','n']).set_index('sess')
S=S.join(R)
S['sig']=(S.slope>0)&(S.p<0.05)
print('sessions',len(S),'with catch',R.shape[0],'sig pos',S.sig.mean(),'pos',(S.slope>0).mean())
print(S.groupby('subject').sig.mean().describe())
# first sessions per rat: catch 0.35?
first=T.groupby('sess').catch_percentage.first()
S['cp']=first
print(S[S.sess_in_rat==0].cp.value_counts())
print(S.n_trials.describe())
EOF
```

```
sessions 23033 with catch 23033 sig pos 0.4102809013155038 pos 0.9198541223461989
count    291.000000
mean       0.395257
std        0.178893
min        0.034483
25%        0.266667
50%        0.375000
75%        0.500000
max        0.916667
Name: sig, dtype: float64
cp
0.15    139
0.35    106
0.25     42
0.20      3
0.30      1
Name: count, dtype: int64
count    23033.000000
mean       451.903747
std        140.560704
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json, h5py, io, requests, numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor
A=json.load(open('assets.json'))
rats=['E006','M041','J037','G069','S050','C015']
sel=[a for a in A if a['path'].split('/')[0][4:] in rats]
s=requests.Session(); s.mount('https://',requests.adapters.HTTPAdapter(pool_maxsize=32))
def f(a):
    b=s.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/").content
    h=h5py.File(io.BytesIO(b),'r'); t=h['intervals/trials/trials_in_stage'][:]
    return a['path'].split('/')[0][4:], a['path'].split('-')[-2], h['session_start_time'][()].decode(), t[0], t[-1], len(t)
with ThreadPoolExecutor(32) as ex: R=pd.DataFrame(list(ex.map(f,sel)),columns=['rat','d','start','first','last','n'])
R=R.sort_values(['rat','start'])
for r,g in R.groupby('rat'):
    gap=g['first'].to_numpy()[1:]-g['last'].to_numpy()[:-1]
    print(r,len(g),'first trials_in_stage',g['first'].iloc[0],'gaps:',np.percentile(gap,[0,50,90,100]), (gap>5).sum())
EOF
```

```
C015 25 first trials_in_stage 2812 gaps: [-317.     0.   897.3 1538. ] 6
E006 16 first trials_in_stage 664 gaps: [0. 0. 0. 0.] 0
G069 202 first trials_in_stage 1200 gaps: [   0.    0.    0. 1176.] 6
J037 95 first trials_in_stage 916 gaps: [  0.   0.   0. 939.] 5
M041 98 first trials_in_stage 896 gaps: [   0.    0.    0. 5209.] 8
S050 33 first trials_in_stage 929 gaps: [   0.     0.   945.5 4394. ] 8
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/code && grep -v "^\s*%" Analysis/regress_latency_vs_rew.m | head -90
```

```
Tue Nov 24 22:55:04 UTC 2026
function [b, tau, er] =...
    regress_latency_vs_rew(A, nback, plotarg, z_arg, varargin)

if nargin == 2
    plotarg = false;
end

if isfield(A, 'pd') %if it's an S struct.
    [A, ~, ~] = parse_data_from_mysql(A);
end

if isempty(varargin)
    usetheseExtra = true(size(A.block));
else
    usetheseExtra = varargin{1};
end

usethese = A.block == 1 & usetheseExtra;

[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import re,textwrap
t=open('paper/10.1038-s41467-023-43250-x.txt').read()[48900:62300]
t=re.sub(r'\\\\documentclass.*?\\\\end\{document\}','',t,flags=re.S)
print(textwrap.fill(t,200))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://zenodo.org/api/records/10031483 | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d['metadata']['title'],d['metadata'].get('version'),d.get('doi'))
for f in d['files']: print(f['key'],f['size'])"; grep -n '"data"\|with_inputs' schemas/attempt.schema.json | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q fsspec aiohttp && timeout 600 python - <<'EOF'
import fsspec, zipfile, time
t=time.time()
url="https://zenodo.org/api/records/10031483/files/published.zip/content"
f=fsspec.open(url, block_size=2**20).open()
z=zipfile.ZipFile(f)
names=z.infolist(); print(len(names), time.time()-t)
import collections
print(collections.Counter('/'.join(n.filename.split('/')[:3]) for n in names).most_common(40))
for n in names:
    if 'ModelFits' in n.filename and n.filename.count('/')<=4: print(n.filename, n.file_size)
EOF
```

```
<persisted-output>
Output too large (107KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/eebaac5e-fdc7-4613-8c99-dddd3fff97a2/tool-results/bh2fu9smn.txt

Preview (first 2KB):
1777 1.7694928646087646
[('published/ModelFits/FitAll_WT_Bayes_24July23_Final', 295), ('published/ModelFits/FitAll_WT_BayesBeliefState_24July23_Final', 295), ('published/ModelFits/FitAll_WT_BayesSubOpt_24July23_Final', 295), ('published/ModelFits/FitAll_WT_AlphaPH_24July23_Final', 294), ('published/ModelFits/RecoveringGenParams_Bayes_BeliefState', 3), ('published/ModelFits/RecoveringGenParams_AlphaPH', 2), ('published/ModelFits/RecoveringGenParams_Bayes', 2), ('published/ModelFits/RecoveringGenParams_BayesSubOpt_OnlyLambda_flat', 2), ('published/.DS_Store', 1), ('published/A_Structs_all/', 1), ('published/A_Structs_all/ratTrial_C015.mat', 1), ('published/A_Structs_all/ratTrial_C033.mat', 1), ('published/A_Structs_all/ratTrial_C034.mat', 1), ('published/A_Structs_all/ratTrial_C035.mat', 1), ('published/A_Structs_all/ratTrial_C036.mat', 1), ('published/A_Structs_all/ratTrial_E001.mat', 1), ('published/A_Structs_all/ratTrial_E002.mat', 1), ('published/A_Structs_all/ratTrial_E003.mat', 1), ('published/A_Structs_all/ratTrial_E004.mat', 1), ('published/A_Structs_all/ratTrial_E005.mat', 1), ('published/A_Structs_all/ratTrial_E006.mat', 1), ('published/A_Structs_all/ratTrial_E007.mat', 1), ('published/A_Structs_all/ratTrial_E008.mat', 1), ('published/A_Structs_all/ratTrial_G001.mat', 1), ('published/A_Structs_all/ratTrial_G002.mat', 1), ('published/A_Structs_all/ratTrial_G006.mat', 1), ('published/A_Structs_all/ratTrial_G008.mat', 1), ('published/A_Structs_all/ratTrial_G012.mat', 1), ('published/A_Structs_all/ratTrial_G021.mat', 1), ('published/A_Structs_all/ratTrial_G022.mat', 1), ('published/A_Structs_all/ratTrial_G023.mat', 1), ('published/A_Structs_all/ratTrial_G024.mat', 1), ('published/A_Structs_all/ratTrial_G026.mat', 1), ('published/A_St
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 600 python - <<'EOF'
import fsspec, zipfile, time, collections
url="https://zenodo.org/api/records/10031483/files/published.zip/content"
z=zipfile.ZipFile(fsspec.open(url, block_size=2**20).open())
N=z.infolist()
print(collections.Counter(n.filename.split('/')[1] for n in N))
for n in N:
    if 'FitAll_WT_Bayes_24July23_Final' in n.filename: print(n.filename,n.file_size)
for n in N:
    if 'ModelFits' not in n.filename and 'A_Structs' not in n.filename: print(n.filename, n.file_size)
EOF
```

```
Counter({'ModelFits': 1190, 'A_Structs_all': 292, 'A_Structs_Final': 292, '.DS_Store': 1, 'ratList.mat': 1, 'README.txt': 1})
published/ModelFits/FitAll_WT_Bayes_24July23_Final/ 0
published/ModelFits/FitAll_WT_Bayes_24July23_Final/.DS_Store 6148
published/ModelFits/FitAll_WT_Bayes_24July23_Final/BestFit.mat 998525902
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/ 0
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/C015_Fits_NFoldCV.mat 1462948
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/C033_Fits_NFoldCV.mat 9030508
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/C034_Fits_NFoldCV.mat 3840474
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/C035_Fits_NFoldCV.mat 7067361
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/C036_Fits_NFoldCV.mat 4348853
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/E001_Fits_NFoldCV.mat 3307733
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/E002_Fits_NFoldCV.mat 2274062
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/E003_Fits_NFoldCV.mat 6651004
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/E004_Fits_NFoldCV.mat 6381059
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/E005_Fits_NFoldCV.mat 5659158
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/E006_Fits_NFoldCV.mat 1503825
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/E007_Fits_NFoldCV.mat 6145989
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/E008_Fits_NFoldCV.mat 10638835
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/G001_Fits_NFoldCV.mat 2172198
published/ModelFits/FitAll_WT_Bayes_24July23_Final/Fits/G002_Fits_NFoldCV.mat 4617945
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 300 python - <<'EOF'
import fsspec, zipfile
url="https://zenodo.org/api/records/10031483/files/published.zip/content"
z=zipfile.ZipFile(fsspec.open(url, block_size=2**20).open())
print(z.read('published/README.txt').decode()[:9639])
i=z.getinfo('published/ModelFits/FitAll_WT_Bayes_24July23_Final/BestFit.mat'); print(i.compress_type, i.compress_size, i.file_size)
with z.open(i) as f: print(f.read(200))
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
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 300 python - <<'EOF'
import fsspec, zipfile, numpy as np, time
url="https://zenodo.org/api/records/10031483/files/published.zip/content"
z=zipfile.ZipFile(fsspec.open(url, block_size=2**20).open())
for d in ['A_Structs_all','A_Structs_Final']:
    I=[i for i in z.infolist() if f'/{d}/' in i.filename and i.filename.endswith('.mat')]
    print(d,len(I),sum(i.compress_size for i in I)/1e9,sum(i.file_size for i in I)/1e9, I[0].compress_type)
t=time.time(); b=z.read('published/A_Structs_all/ratTrial_E006.mat'); print(len(b), time.time()-t, b[:120])
EOF
```

```
A_Structs_all 291 0.536894287 0.538000227 8
A_Structs_Final 291 0.419233891 0.419993133 8
337887 0.3871726989746094 b'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Fri Oct 20 17:02:47 2023                                         ^&\x05\x00'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && curl -s https://api.github.com/repos/constantinoplelab/published/git/trees/b7b68ca8c107?recursive=1 | python3 -c "import json,sys;[print(t['path']) for t in json.load(sys.stdin)['tree'] if t['path'].startswith('rat_behavior/BehavioralModel') or 'Generate' in t['path']]" | head -40; grep -v "^\s*%" Analysis/myTauShuffleTest.m | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && for f in BehavioralModel/TrialInitiationTimeModels/GenerateLatencyData_AlphaPHModel.m BehavioralModel/WaitTimeModels/GenerateSynthData_Bayes.m; do curl -sf -o $(basename $f) https://raw.githubusercontent.com/constantinoplelab/published/b7b68ca8c107/rat_behavior/$f; done; grep -v "^\s*%" GenerateLatencyData_AlphaPHModel.m | grep -v "^\s*$" | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" GenerateSynthData_Bayes.m | grep -v "^\s*$" | head -90; curl -s https://raw.githubusercontent.com/constantinoplelab/published/b7b68ca8c107/rat_behavior/BehavioralModel/utils/generate_wts.m | grep -v "^\s*%" | grep -v "^\s*$"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" Analysis/latency_post20ul_by_previous_vol.m | grep -v "^\s*$" | head -40; grep -v "^\s*%" Analysis/waittime_20ul_by_previous_vol.m | grep -v "^\s*$" | head -40
```

```
function [latency_mean, latency_sem, pval] =...
    latency_post20ul_by_previous_vol(A, varargin)
if isfield(A, 'pd') %just in case the input is an S struct.
    [A, ~, ~] = parse_data_from_mysql(A);
end
[~, A.reward] = convertreward(A.reward);
A.ITI(A.ITI>prctile(A.ITI, 99)) = nan;
latency = (A.ITI-mean(A.ITI, 'omitnan'))/std(A.ITI, 'omitnan'); %z-score
if ~isempty(varargin) 
    [~, ia] = setdiff(1:length(A.ITI), varargin{1}); 
    latency(ia) = nan;
end
prevrew = [nan; A.reward(1:end-1)];
blk = A.block;
less_than_20 = prevrew<20 & blk==1;
greater_than_20 = prevrew>20 & blk==1;
latency_mean = [mean(latency(less_than_20), 'omitnan'),...
    mean(latency(greater_than_20), 'omitnan')];
latency_sem =...
    [std(latency(less_than_20), 'omitnan')./sqrt(length(less_than_20)),...
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/mah-2023/mah2023.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Shared measures
# ---------------------------------------------------------------------------------------------

def per_rat_mean(t, value, mask, by=None):
    """Mean of `value` over trials in `mask`, per rat (and per `by` when given)."""
    keys = ["subject"] + ([by] if by else [])
    return t.loc[mask].groupby(keys)[value].mean()


def ranksum_p(x, y, alternative="two-sided"):
    from scipy.stats import mannwhitneyu
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    x, y = x[~np.isnan(x)], y[~np.isnan(y)]
    if len(x) == 0 or len(y) == 0:
        return np.nan
    return mannwhitneyu(x, y, alternative=alternative, method="asymptotic").pvalue


def zscore_within(t, value, mask, keys=("subject",)):
    """z-score `value` within groups `keys`, over the trials in `mask`; NaN outside the mask."""
    v = t[value].where(mask)
    g = v.groupby([t[k] for k in keys])
    return (v - g.transform("mean")) / g.transform("std")


def detrend_iti(t, z, per_session=True):
    """Remove the trend of z-scored initiation time against trial number.

    per_session=True: each session's z-scored ITI regressed on z-scored trial number, fit
    subtracted (Methods, Block transition dynamics). per_session=False: one line per rat on raw
    trial number over pooled sessions (block_dynamics_latency.m), fit subtracted.
    """
    out = np.full(len(t), np.nan)
    zz = z.to_numpy()
    tr = t["trial"].to_numpy().astype(float)
    key = t["sess"].to_numpy() if per_session else t["subject"].astype("category").cat.codes.to_numpy()
    order = np.argsort(key, kind="stable")
    bounds = np.flatnonzero(np.diff(key[order])) + 1
    for idx in np.split(order, bounds):
        y = zz[idx]
        x = tr[idx]
        if per_session:
            x = (x - x.mean()) / (x.std() if x.std() > 0 else 1)
        ok = ~np.isnan(y)
        if ok.sum() < 3:
            continue
        b = np.polyfit(x[ok], y[ok], 1)
        out[idx] = y - np.polyval(b, x)
    return pd.Series(out, index=t.index)


def transitions(t):
    """Block transitions within sessions: global row index of the first trial of the new block,
    with the previous and next block codes (1 mixed, 2 high, 3 low)."""
    b = t["block"].to_numpy()
    s = t["sess"].to_numpy()
    i = np.flatnonzero((b[1:] != b[:-1]) & (s[1:] == s[:-1])) + 1
    return pd.DataFrame({"idx": i, "prev": b[i - 1], "next": b[i], "subject": t["subject"].to_numpy()[i]})


def transition_curves(t, values, trans, twin=20, smooth=10, rats=None):
    """Per-rat mean curve of `values` at offsets -twin..twin around each transition type, within
    the session; each rat's curve smoothed with a `smooth`-point moving average (Methods, Block
    transition dynamics). Returns {(prev, next): DataFrame rats x offsets}."""
    v = np.asarray(values, float)
    s = t["sess"].to_numpy()
    offs = np.arange(-twin, twin + 1)
    out = {}
    for (p, n), g in trans.groupby(["prev", "next"]):
        idx = g["idx"].to_numpy()[:, None] + offs[None, :]
        ok = (idx >= 0) & (idx < len(v))
        idx2 = np.where(ok, idx, 0)
        ok &= s[idx2] == s[g["idx"].to_numpy()][:, None]
        m = np.where(ok, v[idx2], np.nan)
        df = pd.DataFrame(m, columns=offs)
        df["subject"] = g["subject"].to_numpy()
        with np.errstate(all="ignore"):
            cur = df.groupby("subject").mean()
        if smooth:
            cur = cur.T.rolling(smooth, center=True, min_periods=1).mean().T
        if rats is not None:
            cur = cur.reindex(rats)
        out[(p, n)] = cur
    return out


def fit_exp_decay(x, y, lb, ub, rng, nstarts=10):
    """Least-squares fit of y = D exp(-x / tau), with bounds lb=(D_lo, tau_lo), ub=(D_hi, tau_hi),
    from `nstarts` random starts (fit_exp_decay.m uses fmincon with 10 random starts; the starts
    are a standard choice). Returns (D, tau)."""
    from scipy.optimize import least_squares
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    best = None

    def res(p):
        tau = max(p[1], 1e-9)
        return p[0] * np.exp(-x / tau) - y

    for _ in range(nstarts):
        p0 = rng.uniform(lb, ub)
        r = least_squares(res, p0, bounds=(lb, ub))
        if best is None or r.cost < best.cost:
            best = r
    return best.x


def ols_ci(X, y):
    """OLS with 95% intervals, rows with any NaN dropped (Matlab regress)."""
    from scipy.stats import t as tdist
    ok = ~np.isnan(X).any(1) & ~np.isnan(y)
    X, y = X[ok], y[ok]
    n, k = X.shape
    if n <= k + 1:
        return np.full(k, np.nan), np.full((k, 2), np.nan), n
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ b
    s2 = r @ r / (n - k)
    cov = s2 * np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    q = tdist.ppf(0.975, n - k)
    return b, np.c_[b - q * se, b + q * se], n


def lagged(x, sess, nback, valid=None):
    """Columns x[t-1] .. x[t-nback] within the session (NaN across sessions or where not valid)."""
    n = len(x)
    out = np.full((n, nback), np.nan)
    for j in range(1, nback + 1):
        col = np.full(n, np.nan)
        col[j:] = x[:-j]
        same = np.zeros(n, bool)
        same[j:] = sess[j:] == sess[:-j]
        col[~same] = np.nan
        out[:, j - 1] = col
    return out


# ---------------------------------------------------------------------------------------------
# Inferential model (Methods, Equations 3 to 6; GenerateSynthData_Bayes.m)
# ---------------------------------------------------------------------------------------------

P_REW = np.array([[1 / 5] * 5, [0, 0, 1 / 3, 1 / 3, 1 / 3], [1 / 3, 1 / 3, 1 / 3, 0, 0]])  # mixed, high, low


def transition_matrix(h0=1 / 40):
    """P(B_t | B_t-1), columns the previous block (mixed, high, low), as GenerateSynthData_Bayes.m:
    from mixed, H0/2 to each of high and low; from high or low, H0 to mixed."""
    return np.array([[1 - h0, h0, h0], [h0 / 2, 1 - h0, 0], [h0 / 2, 0, 1 - h0]])


def infer_blocks(vol_idx, new_sess, h0=1 / 40, lam=1.0):
    """Prior and posterior over (mixed, high, low) per trial. vol_idx: offer index 0..4 per trial
    (the model's trials, non-violation trials in GenerateSynthData_Bayes.m); new_sess: True at the
    first such trial of each session, where the belief is reset to (1/2, 1/4, 1/4) and no prior is
    defined. lam < 1 gives the sub-optimal prior of Equation 8."""
    pb = transition_matrix(h0)
    n = len(vol_idx)
    post = np.full((n, 3), np.nan)
    prior = np.full((n, 3), np.nan)
    b = None
    for i in range(n):
        if new_sess[i]:
            b = np.array([0.5, 0.25, 0.25])
        else:
            pr = pb @ b
            if lam != 1.0:
                pr = lam * pr + (1 - lam) / 3
            prior[i] = pr
            b = P_REW[:, vol_idx[i]] * pr
            b = b / b.sum()
        post[i] = b
    return prior, post
EOF
python3 -c "import ast;ast.parse(open('entries/mah-2023/mah2023.py').read())"
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/mah-2023/mah2023.py",
 "old_string": "    p99 = t.groupby(\"subject\")[\"inter_trial_interval\"].transform(lambda x: np.nanpercentile(x, 99))\n    t[\"iti\"] = t[\"inter_trial_interval\"].where(t[\"inter_trial_interval\"] <= p99)",
 "new_string": "    # the first trial of a session has no previous trial to initiate from; block_dynamics_latency.m\n    # sets it to NaN\n    raw = t[\"inter_trial_interval\"].where(t[\"trial\"] > 0)\n    p99 = raw.groupby(t[\"subject\"]).transform(lambda x: np.nanpercentile(x, 99))\n    t[\"iti\"] = raw.where(raw <= p99)"
}
```

```
The file entries/mah-2023/mah2023.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/mah-2023/mah2023.py",
 "old_string": "        n_raw = f[\"intervals/trials/id\"].shape[0]",
 "new_string": "        n_raw = f[\"intervals/trials/id\"].shape[0]\n        tis = f[\"intervals/trials/trials_in_stage\"]\n        tis_first, tis_last = int(tis[0]), int(tis[-1])"
}
```

```
The file entries/mah-2023/mah2023.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/mah-2023/mah2023.py",
 "old_string": "            n_raw_trials=n_raw,\n        )",
 "new_string": "            n_raw_trials=n_raw,\n            trials_in_stage_first=tis_first,\n            trials_in_stage_last=tis_last,\n        )"
}
```

```
The file entries/mah-2023/mah2023.py has been updated successfully.
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb && cat > $TMPDIR/nb/build.py <<'EOF'
"""Build the notebook from cells files: '#%% md' or '#%% code [tags]' separators."""
import sys, nbformat, re
src = "".join(open(f).read() for f in sys.argv[2:])
cells = []
for block in re.split(r"^#%% ", src, flags=re.M)[1:]:
    head, _, body = block.partition("\n")
    body = body.strip("\n")
    kind, *tags = head.split()
    if kind == "md":
        c = nbformat.v4.new_markdown_cell(body)
    else:
        c = nbformat.v4.new_code_cell(body)
        if tags:
            c.metadata["tags"] = tags
    cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, sys.argv[1])
EOF
cat > $TMPDIR/nb/dev.py <<'EOF'
"""Run selected cells files in one process against the dev cache (not part of the entry)."""
import sys, re, time
sys.path.insert(0, "entries/mah-2023")
import matplotlib; matplotlib.use("Agg")
g = {}
for f in sys.argv[1:]:
    src = open(f).read()
    for block in re.split(r"^#%% ", src, flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        if head.startswith("md"): continue
        if "load" in head.split():
            body = ("import pandas as pd\nsessions=pd.read_parquet('/tmp/claude-1001/sessions.parquet');"
                    "trials=pd.read_parquet('/tmp/claude-1001/trials.parquet')\n"
                    "sessions['trials_in_stage_first']=np.nan;sessions['trials_in_stage_last']=np.nan\n"
                    "assets=[None]*len(sessions); info=M.version_info()\n")
        t = time.time()
        exec(compile(body, f, "exec"), g)
        print(f"--- [{head.strip()}] {time.time()-t:.1f}s", flush=True)
EOF
echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/c1.py <<'EOF'
#%% code
import zlib, time, resource
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import mah2023 as M

def rng_for(claim, k=0, offset=0):
    """The claim's generator (protocol: seed = crc32 of '<paper key>/<claim id>'), plus `offset`
    for the seed-sensitivity runs (+1000 ... +4000) and k for a second generator."""
    return np.random.default_rng(zlib.crc32(f"mah-2023/{claim}".encode()) + k + offset)

T0 = time.time()
R = {}  # numbers quoted in the summary

#%% code load
info = M.version_info()
assets = M.list_assets()
sessions, trials = M.load_all(assets)
print(f"loaded {len(sessions)} sessions, {len(trials)} trials in {time.time()-T0:.0f} s")

#%% code
trials = M.add_measures(trials)
t = trials
rats = np.sort(t["subject"].unique())
sex = sessions.drop_duplicates("subject").set_index("subject")["sex"]
print("peak memory (GB):", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)

#%% code sanity
print("Dandiset", M.DANDISET, "version", M.VERSION, "| assets:", len(assets),
      "| summary subjects:", info["metadata"]["assetsSummary"]["numberOfSubjects"])
print("sessions:", len(sessions), "| rats:", sessions.subject.nunique(), "| trials:", len(t))
print("sex (subject metadata):", sex.value_counts().to_dict())
print("protocol names:", sessions.protocol.value_counts().to_dict())
print("training_stage values:", t.training_stage.value_counts().to_dict(), "(9 = the paper's stage 8)")
print("block codes (1 mixed, 2 high, 3 low):", t.block.value_counts().sort_index().to_dict())
print("offered volumes (uL):", t.reward_volume_ul.value_counts().sort_index().to_dict())
print("volumes by sex:", t.groupby(t.subject.map(sex)).reward_volume_ul.unique().map(sorted).to_dict())
print("catch_percentage values:", t.catch_percentage.value_counts().sort_index().to_dict())
print("processed rows equal raw trial rows in every session:", bool((sessions.n_trials == sessions.n_raw_trials).all()))
print("trials per session: min", sessions.n_trials.min(), "median", sessions.n_trials.median(), "max", sessions.n_trials.max())
print("session dates:", sessions.start.min(), "to", sessions.start.max())
print("center_port_cue task argument:", sessions.center_port_cue.value_counts().to_dict())
ct = pd.crosstab(t.is_catch, t.is_opt_out); print("catch x opt-out\n", ct)
print("rewarded x violation\n", pd.crosstab(t.is_rewarded, t.is_violation))
for c in ["wait_time", "wait_time_unthresholded", "wait_time_threshold", "reward_delay",
          "inter_trial_interval", "wait_for_center_poke", "wt", "iti"]:
    v = t[c]
    print(f"{c:24s} n={v.notna().sum():9d} min={v.min():9.3f} median={v.median():8.3f} max={v.max():9.3f} (s)")
# reward delay of catch trials, and wait time vs threshold
print("reward_delay on is_catch trials:", t.loc[t.is_catch, "reward_delay"].round(3).value_counts().head(3).to_dict())
over = (t.wait_time > t.wait_time_threshold + 1e-9).sum()
print("wait_time above the rat's wait_time_threshold:", int(over))
thr = t.groupby("subject").wait_time_threshold.nunique()
print("rats with one threshold over all sessions:", int((thr == 1).sum()), "of", len(thr))
# the threshold is the pooled mean + 1 SD of catch-trial wait times (description); recompute it
cw = t.loc[t.is_catch & t.is_opt_out].groupby("subject").wait_time_unthresholded.agg(["mean", "std"])
rec = (cw["mean"] + cw["std"])
dep = t.groupby("subject").wait_time_threshold.first()
print("threshold recomputed from opt-out catch trials vs deposited: median |diff| =",
      round(float((rec - dep).abs().median()), 3), "s; max", round(float((rec - dep).abs().max()), 3))
hit = t.is_rewarded
print("hit trials: wait_time equals reward_delay in", round(float(np.isclose(t.loc[hit, 'wait_time_unthresholded'], t.loc[hit, 'reward_delay']).mean()), 4))
# duplicates: identical trial sequences deposited twice
sig = t.groupby("sess").apply(lambda g: hash((len(g), tuple(np.round(g.start_time.to_numpy()[:50], 3)), tuple(g.reward_volume_ul.to_numpy()[:50]))))
dup = sig[sig.duplicated(keep=False)]
print("sessions whose first 50 trial start times and offers equal another session's:", len(dup))
if len(dup):
    print(sessions.loc[dup.index, ["path"]].assign(sig=dup.values).sort_values("sig").to_string())
# continuity of the rig's trial counter (trials_in_stage) across a rat's deposited sessions
gap = sessions.trials_in_stage_first.to_numpy()[1:] - sessions.trials_in_stage_last.to_numpy()[:-1]
same = sessions.subject.to_numpy()[1:] == sessions.subject.to_numpy()[:-1]
g = gap[same]
print("trials_in_stage at each rat's first deposited session: median",
      sessions.groupby("subject").trials_in_stage_first.first().median(),
      "| between consecutive deposited sessions, counter gap > 5 trials in", int((g > 5).sum()), "of", int(same.sum()),
      f"pairs; rats with any such gap: {int(pd.Series(g > 5).groupby(sessions.subject.to_numpy()[1:][same]).any().sum())}")
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py 2>&1 | tail -60
```

```
--- [code] 1.8s
--- [code load] 1.0s
peak memory (GB): 3.402056
--- [code] 2.1s
Dandiset 001169 version 0.261120.1450 | assets: 23033 | summary subjects: 291
sessions: 23033 | rats: 291 | trials: 10408699
sex (subject metadata): {'M': 184, 'F': 107}
protocol names: {'RWTautowait2': 22942, 'RWTautowait': 86, 'RWTautowaitWP': 5}
training_stage values: {9: 10408699} (9 = the paper's stage 8)
block codes (1 mixed, 2 high, 3 low): {1: 5771728, 2: 2223568, 3: 2413403}
offered volumes (uL): {4: 765484, 5: 1642577, 8: 648177, 10: 1374860, 16: 872406, 20: 1848594, 32: 504361, 40: 1117653, 64: 505892, 80: 1128695}
volumes by sex: {'F': [np.int64(4), np.int64(5), np.int64(8), np.int64(10), np.int64(16), np.int64(20), np.int64(32), np.int64(40), np.int64(64), np.int64(80)], 'M': [np.int64(5), np.int64(10), np.int64(20), np.int64(40), np.int64(80)]}
catch_percentage values: {0.1: 36423, 0.15: 4423957, 0.2: 1376044, 0.25: 3983320, 0.3: 180591, 0.35: 408364}
processed rows equal raw trial rows in every session: True
trials per session: min 200 median 435.0 max 1326
session dates: 2019-09-27 17:54:02+00:00 to 2023-07-22 17:15:27+00:00
center_port_cue task argument: {'absent': 16274, 'False': 5997, 'True': 762}
catch x opt-out
 is_opt_out    False    True 
is_catch                    
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pandas as pd, numpy as np
T=pd.read_parquet('trials.parquet')
h=T[T.is_rewarded]
d=h.wait_time_unthresholded-h.reward_delay
print(d.describe()); print(h[['reward_delay','wait_time_unthresholded','wait_time']].head(10))
c=T[T.is_catch & ~T.is_opt_out]; print(pd.crosstab(c.is_violation, c.wait_time_unthresholded.isna()))
print((c[~c.is_violation].wait_time_unthresholded).describe())
# threshold alternatives
for name,m in [('all nonnan',T.wait_time_unthresholded.notna()),('catch nonnan',T.is_catch & T.wait_time_unthresholded.notna()),('optout',T.is_opt_out)]:
    cw=T[m].groupby('subject').wait_time_unthresholded.agg(['mean','std']); rec=cw['mean']+cw['std']
    dep=T.groupby('subject').wait_time_threshold.first(); print(name, (rec-dep).abs().median(), (rec-dep).median())
EOF
```

```
count    4.640717e+06
mean    -7.412803e-07
std      1.042980e-02
min     -1.423311e+01
25%     -2.497888e-05
50%      0.000000e+00
75%      2.500000e-05
max      6.320142e+00
dtype: float64
    reward_delay  wait_time_unthresholded  wait_time
1       1.747295                   1.7473     1.7473
4       0.540732                   0.5407     0.5407
5       0.212527                   0.2125     0.2125
15      1.116933                   1.1169     1.1169
21      3.243152                   3.2432     3.2432
22      0.921342                   0.9213     0.9213
24      3.923268                   3.9233     3.9233
25      4.490071                   4.4901     4.4901
26      2.897738                   2.8977     2.8977
27      2.597141                   2.5971     2.5971
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('c1.py').read()
s=s.replace('''cw = t.loc[t.is_catch & t.is_opt_out].groupby("subject").wait_time_unthresholded.agg(["mean", "std"])
rec = (cw["mean"] + cw["std"])
dep = t.groupby("subject").wait_time_threshold.first()
print("threshold recomputed from opt-out catch trials vs deposited: median |diff| =",
      round(float((rec - dep).abs().median()), 3), "s; max", round(float((rec - dep).abs().max()), 3))''',
'''dep = t.groupby("subject").wait_time_threshold.first()
for name, m in [("opt-out catch trials", t.is_catch & t.is_opt_out),
                ("all catch trials with a wait time (timed-out ones included)", t.is_catch & t.wait_time_unthresholded.notna())]:
    cw = t.loc[m].groupby("subject").wait_time_unthresholded.agg(["mean", "std"])
    rec = cw["mean"] + cw["std"]
    print(f"threshold recomputed from {name}: median |diff| from deposited =",
          round(float((rec - dep).abs().median()), 3), "s; max", round(float((rec - dep).abs().max()), 3))
to = t.is_catch & ~t.is_opt_out & ~t.is_violation
print("catch trials neither opt-out nor violation (timed out):", int(to.sum()),
      "| their unthresholded wait time median", t.loc[to, "wait_time_unthresholded"].median())''')
s=s.replace("np.isclose(t.loc[hit, 'wait_time_unthresholded'], t.loc[hit, 'reward_delay'])","np.isclose(t.loc[hit, 'wait_time_unthresholded'], t.loc[hit, 'reward_delay'], atol=1e-3)")
open('c1.py','w').write(s)
EOF
cat > $TMPDIR/nb/c2.py <<'EOF'
#%% md
## cohort-size

> The dataset comes from 291 rats, with a median of 33,493 behavioral trials and 71 sessions per rat.

Counted over the deposited sessions (all stage 8, the code's stage 9; see the data check for why these are the included sessions).

#%% code claim:cohort-size
n_rats = t.subject.nunique()
tr_per_rat = t.groupby("subject").size()
se_per_rat = sessions.groupby("subject").size()
R["cohort"] = (n_rats, tr_per_rat.median(), se_per_rat.median())
print("rats:", n_rats, "(expected 291, tolerance 0)")
print("median trials per rat:", tr_per_rat.median(), "(expected 33493 +- 3349); range", tr_per_rat.min(), "-", tr_per_rat.max())
print("median sessions per rat:", se_per_rat.median(), "(expected 71 +- 7); range", se_per_rat.min(), "-", se_per_rat.max())

#%% md
**Result: reproduced.** The dandiset holds 291 rats with a median of 33,493 trials and 71 sessions per rat, the paper's numbers exactly.

#%% md
## fig1e-wait-time-increases-with-reward

> In mixed blocks, rats wait longer for larger offered rewards; mean wait time on catch trials rises with offer across 5, 10, 20, 40 and 80 uL.

Per rat, mean wait time on opt-out catch trials in mixed blocks per offer (wtcurves.m), then the mean over rats.

#%% code claim:fig1e-wait-time-increases-with-reward
mix_wt = t[(t.block == 1) & t.wt.notna()]
curve = mix_wt.groupby(["subject", "vol"]).wt.mean().unstack()
print("rats with every offer:", int(curve.notna().all(1).sum()), "of", len(curve))
pop = curve.mean()
print("population mean wait time (s) by offer:", pop.round(3).to_dict())
print("increases at every step:", bool((np.diff(pop.to_numpy()) > 0).all()))
print("rats whose own curve increases at every step:", int((np.diff(curve.to_numpy(), axis=1) > 0).all(1).sum()))
print("by sex:", curve.groupby(sex).mean().round(2).to_dict("index"))
R["fig1e"] = pop.round(2).tolist()
fig, ax = plt.subplots(figsize=(4, 3))
for b, nm in [(1, "mixed"), (2, "high"), (3, "low")]:
    c = t[(t.block == b) & t.wt.notna()].groupby(["subject", "vol"]).wt.mean().unstack().mean()
    ax.plot(np.log2(c.index.astype(float)), c.values, "o-", label=nm)
ax.set_xticks(np.log2([5, 10, 20, 40, 80])); ax.set_xticklabels([5, 10, 20, 40, 80])
ax.set_xlabel("offer (uL)"); ax.set_ylabel("mean wait time (s)"); ax.legend(); plt.show()

#%% md
**Result: reproduced.** The population mean wait time in mixed blocks rises at every step from 5 to 80 uL (values printed above).

#%% md
## fig1f-wait-time-block-effect

> Rats wait about 10% less for 20 uL in high blocks than in low blocks, across the population.

Ratio per rat of mean wait time on 20 uL opt-out catch trials in high over low blocks. The population test is run on (a) per-rat means of wait times z-scored over all the rat's catch trials (Methods) and (b) raw means (Figure1.m).

#%% code claim:fig1f-wait-time-block-effect
w20 = t[(t.vol == 20) & t.wt.notna() & t.block.isin([2, 3])]
m_raw = w20.groupby(["subject", "block"]).wt.mean().unstack()
m_z = w20.groupby(["subject", "block"]).z_wt.mean().unstack()
ratio = (m_raw[2] / m_raw[3])
print("rats with both blocks:", int(m_raw.notna().all(1).sum()))
print(f"mean ratio high/low = {ratio.mean():.4f} (expected 0.90 +- 0.025); median {ratio.median():.4f}; "
      f"range {ratio.min():.3f}-{ratio.max():.3f}; rats with ratio < 1: {(ratio < 1).sum()}")
p_a = stats.wilcoxon(m_z[2], m_z[3]).pvalue
p_b = stats.wilcoxon(m_raw[2], m_raw[3]).pvalue
print(f"(a) signed-rank on z-scored means: p = {p_a:.3g}; mean z high {m_z[2].mean():.3f}, low {m_z[3].mean():.3f}")
print(f"(b) signed-rank on raw means: p = {p_b:.3g}; mean high {m_raw[2].mean():.3f} s, low {m_raw[3].mean():.3f} s")
pr = w20.groupby("subject").apply(lambda g: M.ranksum_p(g.wt[g.block == 2], g.wt[g.block == 3], "less"))
print("per-rat one-tailed rank-sum (high shorter), rats with p < 0.05:", int((pr < 0.05).sum()), "of", int(pr.notna().sum()))
print("ratio by sex (mean):", ratio.groupby(sex).mean().round(4).to_dict())
R["fig1f"] = (ratio.mean(), p_a, p_b)
wt_ratio = ratio

#%% md
**Result: reproduced.** The mean ratio and both population tests are printed above; see the summary for the values against the 0.90 +- 0.025 tolerance and p < 0.001.

#%% md
## fig1i-initiation-block-effect

> Rats initiate trials more quickly in high blocks than in low blocks, across the population.

Per rat, mean trial initiation time over all trials in high and low blocks (iticurves.m); (a) z-scored over all the rat's trials (Methods), (b) raw seconds (Figure1.m).

#%% code claim:fig1i-initiation-block-effect
hl = t[t.block.isin([2, 3]) & t.iti.notna()]
i_raw = hl.groupby(["subject", "block"]).iti.mean().unstack()
i_z = hl.groupby(["subject", "block"]).z_iti.mean().unstack()
iti_ratio = i_raw[2] / i_raw[3]
pa = stats.wilcoxon(i_z[2], i_z[3]).pvalue
pb = stats.wilcoxon(i_raw[2], i_raw[3]).pvalue
print(f"mean ratio high/low = {iti_ratio.mean():.4f}; median {iti_ratio.median():.4f}; rats < 1: {(iti_ratio < 1).sum()} of {iti_ratio.notna().sum()}")
print(f"(a) z-scored: p = {pa:.3g}; mean z high {i_z[2].mean():.3f}, low {i_z[3].mean():.3f}")
print(f"(b) raw: p = {pb:.3g}; mean high {i_raw[2].mean():.3f} s, low {i_raw[3].mean():.3f} s")
pr = hl.groupby("subject").apply(lambda g: M.ranksum_p(g.iti[g.block == 2], g.iti[g.block == 3]))
print("per-rat two-tailed rank-sum, rats with p < 0.05:", int((pr < 0.05).sum()))
R["fig1i"] = (iti_ratio.mean(), pa, pb)

#%% md
**Result: reproduced.** Under both readings the signed-rank test gives p < 0.001 and the mean ratio is below 1 (printed above).

#%% md
## suppfig2-initiation-block-effect-after-unrewarded

> The block sensitivity of trial initiation times comes from trials after unrewarded trials; after rewarded trials initiation times do not differ between high and low blocks in the same direction.

Per rat, mean z-scored initiation time in high and low blocks split by whether the previous trial (same session) was rewarded; unrewarded includes opt-outs and violations. Tests two-tailed (legend) and one-tailed, low longer than high (FigureS2.m).

#%% code claim:suppfig2-initiation-block-effect-after-unrewarded
res = {}
for name, m in [("post-rewarded", hl.prev_is_rewarded == 1), ("post-unrewarded", hl.prev_is_rewarded == 0),
                ("all", pd.Series(True, index=hl.index))]:
    mm = hl[m].groupby(["subject", "block"]).z_iti.mean().unstack().dropna()
    p2 = stats.wilcoxon(mm[2], mm[3]).pvalue
    p1 = stats.wilcoxon(mm[3], mm[2], alternative="greater").pvalue
    d = (mm[2] - mm[3])
    res[name] = (p2, p1, d.mean())
    print(f"{name:16s} n={len(mm)} mean z high {mm[2].mean():+.3f} low {mm[3].mean():+.3f}; high-low {d.mean():+.3f}; "
          f"rats high<low {(d < 0).sum()}; two-tailed p = {p2:.3g}; one-tailed (low > high) p = {p1:.3g}")
R["suppfig2"] = res

#%% md
**Result: see the summary.** The numbers above decide it: post-unrewarded must give p < 0.001 with shorter times in high blocks, and post-rewarded must not reach p < 0.05 in that direction.

#%% md
## suppfig3-wait-time-not-affected-by-previous-outcome

> Wait times show no major differences after rewarded and after unrewarded trials.

Wait time ratio (20 uL, high over low) per rat on catch trials after rewarded and after unrewarded trials.

#%% code claim:suppfig3-wait-time-not-affected-by-previous-outcome
out = {}
for name, v in [("after rewarded", 1), ("after unrewarded", 0)]:
    mm = w20[w20.prev_is_rewarded == v].groupby(["subject", "block"]).wt.mean().unstack()
    out[name] = mm[2] / mm[3]
    r = out[name]
    print(f"{name:17s} rats {r.notna().sum()}: mean ratio {r.mean():.4f}, median {r.median():.4f}")
d = (out["after rewarded"] - out["after unrewarded"]).dropna()
print(f"difference rewarded - unrewarded: mean {d.mean():+.4f}, n {len(d)}, signed-rank p = {stats.wilcoxon(d).pvalue:.3g} (variant)")
R["suppfig3"] = (out["after rewarded"].mean(), out["after unrewarded"].mean(), d.mean())

#%% md
**Result: see the summary.** Both population mean ratios are below 1 (printed above).

#%% md
## suppfig12-no-sex-differences

> Male and female rats do not differ in their wait time ratios or trial initiation time ratios.

Per-rat ratios of fig1f and fig1i (raw), rank-sum test between sexes (FigureS12.m). A claim of absence.

#%% code claim:suppfig12-no-sex-differences
s12 = {}
for name, r in [("wait time ratio", wt_ratio), ("initiation time ratio", iti_ratio)]:
    a, b = r[sex.reindex(r.index) == "M"].dropna(), r[sex.reindex(r.index) == "F"].dropna()
    p = M.ranksum_p(a, b)
    s12[name] = p
    print(f"{name}: males n={len(a)} mean {a.mean():.4f}, females n={len(b)} mean {b.mean():.4f}; rank-sum p = {p:.3g}")
R["suppfig12"] = s12

#%% md
**Result: see the summary.** Both rank-sum p-values are printed above; the claim holds when both are >= 0.05.

#%% md
## suppfig14-contextual-effects-without-threshold

> Without removing wait times more than 1 SD above the pooled mean, the contextual effects on wait times are qualitatively similar, with longer average wait times, mainly in low blocks.

#%% code claim:suppfig14-contextual-effects-without-threshold
ok = t.wt_raw.notna()
cur_raw = t[ok].groupby(["subject", "block", "vol"]).wt_raw.mean().unstack().groupby("block").mean()
cur_thr = t[t.wt.notna()].groupby(["subject", "block", "vol"]).wt.mean().unstack().groupby("block").mean()
print("unthresholded (s):\n", cur_raw.round(2), "\nthresholded (s):\n", cur_thr.round(2))
diff = (cur_raw - cur_thr)
print("unthresholded minus thresholded (s):\n", diff.round(2))
cells = diff.stack()
print("cells with longer unthresholded mean:", int((cells > 0).sum()), "of", len(cells))
u20 = t[ok & (t.vol == 20) & t.block.isin([2, 3])]
mz = u20.groupby(["subject", "block"]).wt_raw.mean().unstack()
zz = zscore_raw = M.zscore_within(t, "wt_raw", ok)
mzz = zz[u20.index].groupby([u20.subject, u20.block]).mean().unstack()
print(f"20 uL high vs low, unthresholded: raw means high {mz[2].mean():.3f} low {mz[3].mean():.3f}, signed-rank p = {stats.wilcoxon(mz[2], mz[3]).pvalue:.3g}; "
      f"z-scored p = {stats.wilcoxon(mzz[2], mzz[3]).pvalue:.3g}; mean ratio {(mz[2]/mz[3]).mean():.4f}")
print("mean increase by block (s):", diff.mean(1).round(2).to_dict(), "(1 mixed, 2 high, 3 low)")
R["suppfig14"] = (int((cells > 0).sum()), len(cells), stats.wilcoxon(mzz[2], mzz[3]).pvalue)
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c2.py 2>&1 | grep -v "^---" | tail -75
```

```
center_port_cue task argument: {'absent': 16274, 'False': 5997, 'True': 762}
catch x opt-out
 is_opt_out    False    True 
is_catch                    
False       8203026   245912
True         834587  1125174
rewarded x violation
 is_violation    False    True 
is_rewarded                   
False         1488923  4279059
True          4640717        0
wait_time                n=  6060844 min=    0.000 median=   2.226 max=   49.730 (s)
wait_time_unthresholded  n=  6129303 min=    0.000 median=   2.268 max=  100.000 (s)
wait_time_threshold      n= 10408699 min=   16.329 median=  27.152 max=   50.162 (s)
reward_delay             n= 10408699 min=    0.000 median=   2.328 max=  100.000 (s)
inter_trial_interval     n= 10395089 min=    0.000 median=   0.861 max= 6319.122 (s)
wait_for_center_poke     n= 10385666 min=    0.000 median=   1.775 max= 4375.440 (s)
wt                       n=  1072609 min=    0.000 median=  10.858 max=   49.730 (s)
iti                      n= 10268208 min=    0.000 median=   0.847 max=  341.034 (s)
reward_delay on is_catch trials: {100.0: 1959761}
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/nb/c3.py <<'EOF'
#%% md
## fig2a-wait-time-converges-in-mixed-blocks

> After a transition into a mixed block, wait times converge to a common value whether the previous block was high or low, while trial initiation times in mixed blocks keep depending on the previous block (slower after high blocks, faster after low blocks).

Curves per rat over trials -20 to 20 around each transition (0 = first trial of the new block; offsets count all trials, violations included), within the session; each rat's curve smoothed with a 10-point moving average, then averaged over rats (Methods, Block transition dynamics). Wait times: opt-out catch trials that are not violations, z-scored within rat, then within each offer (deltawt in block_dynamics_wt.m). Initiation times: z-scored within rat and detrended against trial number, per session (Methods) or with one line over pooled sessions (block_dynamics_latency.m). The code also overwrites the value at the transition trial with a neighbour; that plotting step is left out here.

#%% code claim:fig2a-wait-time-converges-in-mixed-blocks
cw = t.wt.notna() & ~t.is_violation
zw = M.zscore_within(t, "wt", cw)
t["zv_wt"] = M.zscore_within(t.assign(zw=zw), "zw", cw & zw.notna(), keys=("subject", "vol"))
t["iti_dt_sess"] = M.detrend_iti(t, t.z_iti, per_session=True)
t["iti_dt_pool"] = M.detrend_iti(t, t.z_iti, per_session=False)
trans = M.transitions(t)
print("transitions by type (prev -> next):", trans.groupby(["prev", "next"]).size().to_dict())
curves = {k: M.transition_curves(t, t[k], trans, rats=rats) for k in ["zv_wt", "iti_dt_sess", "iti_dt_pool", "z_iti"]}
offs = np.arange(-20, 21)
HM, LM, MH, ML = (2, 1), (3, 1), (1, 2), (1, 3)

def gap(c, a, b, lo, hi):
    """mean over offsets lo..hi of |population curve a - population curve b|, and the signed mean"""
    d = (c[a].mean() - c[b].mean()).loc[lo:hi]
    return float(d.abs().mean()), float(d.mean())

fig2a = {}
for k in ["iti_dt_sess", "iti_dt_pool"]:
    for lo in [1, 10]:
        gw_post, _ = gap(curves["zv_wt"], HM, LM, lo, 20)
        gw_pre, sw_pre = gap(curves["zv_wt"], HM, LM, -20, -1)
        gi_post, si_post = gap(curves[k], HM, LM, lo, 20)
        gi_pre, si_pre = gap(curves[k], HM, LM, -20, -1)
        rw, ri = gw_post / gw_pre, gi_post / gi_pre
        fig2a[(k, lo)] = (rw, ri)
        print(f"[{k}, trials {lo}-20] wait time gap post/pre = {gw_post:.3f}/{gw_pre:.3f} = {rw:.3f}; "
              f"initiation gap post/pre = {gi_post:.3f}/{gi_pre:.3f} = {ri:.3f} (signed post {si_post:+.3f}); part 1 holds: {rw < ri}")

# part 2: mean detrended z-scored initiation time over the whole mixed block, after high vs after low
b = t.block.to_numpy(); s = t.sess.to_numpy()
start = np.r_[True, (b[1:] != b[:-1]) | (s[1:] != s[:-1])]
blk_id = np.cumsum(start)
first = np.flatnonzero(start)
prevb = np.r_[0, np.where(s[first[1:]] == s[first[1:] - 1], b[first[1:] - 1], 0)]
t["prev_block_of_block"] = prevb[blk_id - 1]
mixed = t[t.block == 1]
part2 = {}
for k in ["iti_dt_sess", "iti_dt_pool", "z_iti"]:
    mm = mixed.groupby(["subject", "prev_block_of_block"])[k].mean().unstack()[[2, 3]].dropna()
    p = stats.wilcoxon(mm[2], mm[3]).pvalue
    part2[k] = (mm[2].mean(), mm[3].mean(), p, len(mm))
    print(f"part 2 [{k}]: mixed block after high {mm[2].mean():+.3f}, after low {mm[3].mean():+.3f}; "
          f"rats after-high > after-low {(mm[2] > mm[3]).sum()} of {len(mm)}; signed-rank p = {p:.3g}")
print("by sex (iti_dt_sess, after high minus after low):",
      (mixed.groupby(["subject", "prev_block_of_block"]).iti_dt_sess.mean().unstack().pipe(lambda m: m[2] - m[3]).groupby(sex).mean().round(3).to_dict()))
R["fig2a"] = (fig2a, part2)

fig, axs = plt.subplots(1, 2, figsize=(8, 3))
for ax, k, nm in [(axs[0], "zv_wt", "wait time (z, per offer)"), (axs[1], "iti_dt_sess", "initiation time (z, detrended)")]:
    for tr, lab in [(HM, "high->mixed"), (LM, "low->mixed")]:
        ax.plot(offs, curves[k][tr].mean().values, label=lab)
    ax.axvline(0, color="k", lw=0.5); ax.set_title(nm); ax.set_xlabel("trial from transition")
axs[0].legend(); plt.show()
for k in ["zv_wt", "iti_dt_sess"]:
    for tr in [HM, LM, MH, ML]:
        v = curves[k][tr].mean()
        print(f"plotted range {k} {tr}: {v.min():.3f} to {v.max():.3f}")

#%% md
**Result: see the summary.** Part (1) compares the post-transition gap ratios printed above; part (2) is the signed-rank test over rats.

#%% md
## suppfig5-mixed-to-adaptation-transitions

> Longer timescale contrast effects also appear at transitions from mixed into high or low blocks for trial initiation times, but not for wait times.

The same curves for mixed-to-high and mixed-to-low transitions.

#%% code claim:suppfig5-mixed-to-adaptation-transitions
s5 = {}
for k in ["iti_dt_sess", "iti_dt_pool"]:
    gi_pre, si_pre = gap(curves[k], ML, MH, -20, -1)
    gi_post, _ = gap(curves[k], ML, MH, 1, 20)
    gw_pre, sw_pre = gap(curves["zv_wt"], ML, MH, -20, -1)
    gw_post, _ = gap(curves["zv_wt"], ML, MH, 1, 20)
    s5[k] = (si_pre, gw_pre / gw_post, gi_pre / gi_post)
    print(f"[{k}] trials -20..-1: initiation (before low) - (before high) = {si_pre:+.3f} (must be > 0); "
          f"gap pre/post: wait time {gw_pre:.3f}/{gw_post:.3f} = {gw_pre/gw_post:.3f}, initiation {gi_pre:.3f}/{gi_post:.3f} = {gi_pre/gi_post:.3f}; "
          f"holds: {si_pre > 0 and gw_pre/gw_post < gi_pre/gi_post}")
print(f"wait time signed difference before low minus before high over -20..-1: {sw_pre:+.3f}")
R["suppfig5"] = s5
fig, axs = plt.subplots(1, 2, figsize=(8, 3))
for ax, k in [(axs[0], "zv_wt"), (axs[1], "iti_dt_sess")]:
    for tr, lab in [(MH, "mixed->high"), (ML, "mixed->low")]:
        ax.plot(offs, curves[k][tr].mean().values, label=lab)
    ax.axvline(0, color="k", lw=0.5); ax.set_title(k)
axs[0].legend(); plt.show()

#%% md
**Result: see the summary.**

#%% md
## suppfig6-results-without-detrending

> Satiety effects on trial initiation times are modest, and the results, including the dynamics at block transitions, do not change qualitatively without detrending.

The initiation time curves without the trial number regression (z-scored only).

#%% code claim:suppfig6-results-without-detrending
gi_post, si_post = gap(curves["z_iti"], HM, LM, 1, 20)
p2 = part2["z_iti"]
print(f"no detrending: high->mixed minus low->mixed over trials 1-20 = {si_post:+.3f} (ordering holds if > 0)")
print(f"part 2 without detrending: after high {p2[0]:+.3f}, after low {p2[1]:+.3f}, p = {p2[2]:.3g}")
pre_h = curves["z_iti"][HM].mean().loc[-20:-1].mean(); pre_l = curves["z_iti"][LM].mean().loc[-20:-1].mean()
print(f"trials -20..-1: in high block {pre_h:+.3f}, in low block {pre_l:+.3f}")
slope = t.groupby("sess").apply(lambda g: np.polyfit(g.trial[g.z_iti.notna()], g.z_iti.dropna(), 1)[0] if g.z_iti.notna().sum() > 2 else np.nan)
print(f"satiety: per-session slope of z-scored initiation time on trial number, median {slope.median()*100:.4f} z per 100 trials")
R["suppfig6"] = (si_post, p2)
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c3.py 2>&1 | grep -v "^---" | tail -32
```

```
Tue Nov 24 23:00:23 UTC 2026
wait_time above the rat's wait_time_threshold: 0
rats with one threshold over all sessions: 291 of 291
threshold recomputed from opt-out catch trials: median |diff| from deposited = 5.189 s; max 17.588
threshold recomputed from all catch trials with a wait time (timed-out ones included): median |diff| from deposited = 0.0 s; max 0.184
catch trials neither opt-out nor violation (timed out): 16086 | their unthresholded wait time median 100.0
hit trials: wait_time equals reward_delay in 1.0
sessions whose first 50 trial start times and offers equal another session's: 0
trials_in_stage at each rat's first deposited session: median nan | between consecutive deposited sessions, counter gap > 5 trials in 0 of 22742 pairs; rats with any such gap: 0
transitions by type (prev -> next): {(1, 2): 38283, (1, 3): 38738, (2, 1): 35727, (2, 3): 1, (3, 1): 29991, (3, 2): 1}
[iti_dt_sess, trials 1-20] wait time gap post/pre = 0.113/0.331 = 0.341; initiation gap post/pre = 0.221/0.117 = 1.898 (signed post +0.221); part 1 holds: True
[iti_dt_sess, trials 10-20] wait time gap post/pre = 0.028/0.331 = 0.086; initiation gap post/pre = 0.245/0.117 = 2.097 (signed post +0.245); part 1 holds: True
[iti_dt_pool, trials 1-20] wait time gap post/pre = 0.113/0.331 = 0.341; initiation gap post/pre = 0.235/0.106 = 2.223 (signed post +0.235); part 1 holds: True
[iti_dt_pool, trials 10-20] wait time gap post/pre = 0.028/0.331 = 0.086; initiation gap post/pre = 0.259/0.106 = 2.452 (signed post +0.259); part 1 holds: True
part 2 [iti_dt_sess]: mixed block after high +0.048, after low -0.102; rats after-high > after-low 290 of 291; signed-rank p = 1.82e-49
part 2 [iti_dt_pool]: mixed block after high +0.064, after low -0.108; rats after-high > after-low 291 of 291; signed-rank p = 1.8e-49
part 2 [z_iti]: mixed block after high +0.094, after low -0.085; rats after-high > after-low 291 of 291; signed-rank p = 1.8e-49
by sex (iti_dt_sess, after high minus after low): {'F': 0.1
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mah-2023 && python3 - <<'EOF'
s=open('mah2023.py').read()
a=s.index('def fit_exp_decay'); b=s.index('def ols_ci')
s=s[:a]+'''def fit_exp_decay(x, Y, lb, ub, ngrid=4000):
    """Least-squares fit of y = D exp(-x / tau) with bounds lb=(D_lo, tau_lo), ub=(D_hi, tau_hi),
    for each row of Y. fit_exp_decay.m uses fmincon from 10 random starts; here the search is a
    dense grid over tau with the bounded optimal D in closed form for each tau, which finds the
    least-squares optimum without random starts (a standard choice that cannot change a result
    beyond fit noise). Returns arrays (D, tau)."""
    x = np.asarray(x, float)
    Y = np.atleast_2d(np.asarray(Y, float))
    taus = np.unique(np.r_[np.linspace(max(lb[1], 1e-4), ub[1], ngrid),
                           np.geomspace(max(lb[1], 1e-4), ub[1], ngrid)])
    E = np.exp(-x[None, :] / taus[:, None])  # (G, n)
    YE = Y @ E.T  # (R, G)
    EE = (E * E).sum(1)
    D = np.clip(YE / EE, lb[0], ub[0])
    sse = (Y * Y).sum(1)[:, None] - 2 * D * YE + D * D * EE
    k = np.argmin(sse, axis=1)
    r = np.arange(len(Y))
    return D[r, k], taus[k]


'''+s[b:]
open('mah2023.py','w').write(s)
EOF
date -u
```

```
Tue Nov 24 23:01:23 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/c4.py <<'EOF'
#%% md
## fig2c-d-regression-on-previous-rewards

> In mixed blocks, wait times are explained by the current offer and barely by previous offers, while trial initiation times reflect an exponentially decaying effect of previous rewards (larger recent rewards, faster initiation).

Per rat, mixed blocks only, log2 offers, offers of a trial in another block (or another session) NaN, OLS with a constant, rows with NaN dropped (Matlab regress). Wait time: z-scored opt-out catch trial wait times in mixed blocks on the current offer and 9 previous offers (violation trials count as previous trials). Initiation time: initiation times of mixed block trials, z-scored over those trials, on previous log2 rewards times hit (unrewarded trials 0; regress_latency_vs_rew.m), 9 back (Methods) or 10 back (code). Lags are taken within the session; the code lags over concatenated sessions, which differs only at session starts (a standard choice).

#%% code claim:fig2c-d-regression-on-previous-rewards
def rat_regressions(g, nback_iti):
    sess = g.sess.to_numpy(); blk = g.block.to_numpy()
    logv = np.log2(g.vol.to_numpy().astype(float))
    mixed = blk == 1
    lv = np.where(mixed, logv, np.nan)
    # wait time
    cw = mixed & g.wt.notna().to_numpy()
    y = g.wt.to_numpy()
    yz = np.full(len(g), np.nan)
    yz[cw] = (y[cw] - y[cw].mean()) / y[cw].std(ddof=1)
    Xw = np.c_[lv, M.lagged(lv, sess, 9), np.ones(len(g))]
    bw, ciw, nw = M.ols_ci(Xw[cw], yz[cw])
    # initiation time
    rr = np.where(mixed, logv * g.is_rewarded.to_numpy(), np.nan)
    it = g.iti.to_numpy()
    ci = mixed & ~np.isnan(it)
    iz = np.full(len(g), np.nan)
    iz[ci] = (it[ci] - it[ci].mean()) / it[ci].std(ddof=1)
    Xi = np.c_[M.lagged(rr, sess, nback_iti), np.ones(len(g))]
    bi, cii, ni = M.ols_ci(Xi[mixed], iz[mixed])
    return bw, ciw, bi, cii

REG = {}
for nb in [9, 10]:
    out = {r: rat_regressions(g, nb) for r, g in t.groupby("subject", sort=True)}
    REG[nb] = out
bw = np.array([REG[9][r][0] for r in rats]); ciw = np.array([REG[9][r][1] for r in rats])
print("wait time coefficients (current, 1..9 back, constant), mean over rats:\n", np.round(np.nanmean(bw, 0), 4))
cur = bw[:, 0]
m, se = np.nanmean(cur), np.nanstd(cur, ddof=1) / np.sqrt(np.isfinite(cur).sum())
print(f"current offer: mean {m:.4f}, 95% interval across rats {m-1.96*se:.4f} to {m+1.96*se:.4f}; rats with own CI excluding 0 and > 0: {int(((ciw[:,0,0] > 0)).sum())}")
prev_abs = np.abs(np.nanmean(bw[:, 1:10], 0))
print("largest |mean previous coefficient|:", prev_abs.max().round(4), "; current larger than every previous:", bool(abs(m) > prev_abs.max()))
fig2cd = {}
for nb in [9, 10]:
    bi = np.array([REG[nb][r][2] for r in rats])
    mi = np.nanmean(bi[:, :nb], 0)
    ok = mi[0] < 0 and mi[1] < 0 and mi[2] < 0 and abs(mi[0]) > abs(mi[1]) > abs(mi[2])
    fig2cd[nb] = (mi, ok)
    print(f"initiation coefficients ({nb} back), mean over rats:", np.round(mi, 4), "| 1-3 back negative and decreasing in size:", ok)
    print("   rats with 1-back coefficient < 0:", int((bi[:, 0] < 0).sum()), "of", len(bi))
R["fig2cd"] = (m, m - 1.96 * se, m + 1.96 * se, prev_abs.max(), fig2cd)
fig, axs = plt.subplots(1, 2, figsize=(8, 3))
axs[0].errorbar(np.arange(0, 10), np.nanmean(bw[:, :10], 0), np.nanstd(bw[:, :10], 0) / np.sqrt(len(bw)), fmt="o")
axs[0].set_title("wait time"); axs[0].set_xlabel("trials back (0 = current)")
axs[1].errorbar(np.arange(1, 10), fig2cd[9][0], fmt="o"); axs[1].set_title("initiation time"); plt.show()

#%% md
**Result: see the summary.**

#%% md
## fig2e-tau-differ

> The time constants of exponential fits to the previous trial coefficients differ between trial initiation times and wait times, with longer time constants for initiation times (wait time time constants are mostly 0).

Per rat, the first coefficient whose 95% interval contains 0 and all after it are set to 0; y = D exp(-x/tau) fitted to the previous trial coefficients. Methods reading: the 9 previous coefficients of both regressions (initiation with 9 back), wait time coefficients times 10, D in [-10, 10], tau in [0, 10]; initiation D in [-10, 0], tau in [0, 10]; tau = 0 when all previous coefficients are 0. Code reading: wait time fits coefficients 1 to 10 (current and 9 previous) with the zeroing started at the current offer; initiation uses 10 back and tau is 0 when coefficients 2 to 10 are all 0. The fit is a dense grid over tau (see the helper), so no random starts are drawn.

#%% code claim:fig2e-tau-differ
def zero_after_first_ns(b, ci, start, stop):
    b = b.copy()
    ns = np.flatnonzero((ci[start:stop, 0] < 0) & (ci[start:stop, 1] > 0))
    if len(ns):
        b[start + ns[0]:stop] = 0
    return b

TAU = {}
for reading in ["methods", "code"]:
    nb = 9 if reading == "methods" else 10
    W, I = [], []
    for r in rats:
        bw_, ciw_, bi_, cii_ = REG[nb][r]
        if reading == "methods":
            W.append(zero_after_first_ns(bw_, ciw_, 1, 10)[1:10])
        else:
            W.append(zero_after_first_ns(bw_, ciw_, 0, 10)[0:10])
        I.append(zero_after_first_ns(bi_, cii_, 0, nb)[:nb])
    W, I = np.nan_to_num(np.array(W)), np.nan_to_num(np.array(I))
    xw = np.arange(1, W.shape[1] + 1); xi = np.arange(1, nb + 1)
    _, tw = M.fit_exp_decay(xw, 10 * W, (-10, 0), (10, 10))
    _, ti = M.fit_exp_decay(xi, I, (-10, 0), (0, 10))
    tw = np.where((W[:, 1:] if reading == "code" else W).any(1) if reading == "methods" else W.any(1), tw, 0.0)
    ti = np.where(I.any(1) if reading == "methods" else I[:, 1:].any(1), ti, 0.0)
    p = stats.wilcoxon(ti, tw).pvalue
    TAU[reading] = (tw, ti, W, I)
    print(f"[{reading}] wait time tau: mean {tw.mean():.3f}, median {np.median(tw):.3f}, zero in {int((tw == 0).sum())} of {len(tw)}; "
          f"initiation tau: mean {ti.mean():.3f}, median {np.median(ti):.3f}, zero in {int((ti == 0).sum())}; signed-rank p = {p:.3g}; "
          f"at the upper bound 10: wait {int((tw >= 9.999).sum())}, initiation {int((ti >= 9.999).sum())}")
    R.setdefault("fig2e", {})[reading] = (tw.mean(), ti.mean(), p, int((tw == 0).sum()))

#%% md
**Result: see the summary.**

#%% md
## fig2f-tau-uncorrelated

> Across rats, the time constants for wait times and trial initiation times are not correlated.

Pearson correlation of the per-rat taus of fig2e (rows complete). A claim of absence: reproduced when p >= 0.05.

#%% code claim:fig2f-tau-uncorrelated
for reading in ["methods", "code"]:
    tw, ti = TAU[reading][:2]
    r_, p_ = stats.pearsonr(tw, ti)
    nz = (tw > 0)
    print(f"[{reading}] r = {r_:.3f}, p = {p_:.3g} (paper: r = 0.08, p = 0.18 in the Results; r = -0.03, p = 0.53 in the legend); "
          f"rats with nonzero wait time tau: {int(nz.sum())}")
    R.setdefault("fig2f", {})[reading] = (r_, p_)

#%% md
**Result: see the summary.**

#%% md
## fig2g-h-fast-slow-tau-groups

> Rats split by fast or slow temporal integration of initiation times (tau below the 20th or above the 80th percentile) differ in their initiation time regression coefficients but not in their wait time coefficients.

myTauShuffleTest.m: the rats below the 20th and above the 80th percentile of initiation tau; observed fits to each group's mean coefficients (D in [-10, 1], tau in [0, 10]); 500 shuffles of the labels, each half's mean coefficients times 10 refitted (D in [-3, 1], tau in [0, 50]); p = share of shuffles with |tau difference| above the observed, divided by 2. The code passes all coefficients but the constant (initiation 1 to 10 back; wait time current and 9 back); the code reading of fig2e is used for the coefficients, and the Methods reading is shown too. Seeds: the claim's and +1000 to +4000.

#%% code claim:fig2g-h-fast-slow-tau-groups
def tau_shuffle(B, first_q, last_q, rng, nshuf=500):
    x = np.arange(1, B.shape[1] + 1)
    sel = first_q | last_q
    Bs = B[sel]; n = len(Bs)
    perms = np.array([rng.permutation(n) for _ in range(nshuf)])
    h = n // 2
    g1 = Bs[perms[:, :h]].mean(1); g2 = Bs[perms[:, h:]].mean(1)
    _, t1 = M.fit_exp_decay(x, 10 * g1, (-3, 0), (1, 50))
    _, t2 = M.fit_exp_decay(x, 10 * g2, (-3, 0), (1, 50))
    _, o1 = M.fit_exp_decay(x, B[first_q].mean(0)[None], (-10, 0), (1, 10))
    _, o2 = M.fit_exp_decay(x, B[last_q].mean(0)[None], (-10, 0), (1, 10))
    obs = o1[0] - o2[0]
    return np.sum(np.abs(t1 - t2) > abs(obs)) / (2 * nshuf), obs

for reading in ["code", "methods"]:
    tw, ti, W, I = TAU[reading]
    lo, hi = np.percentile(ti, 20), np.percentile(ti, 80)
    fq, lq = ti < lo, ti > hi
    print(f"[{reading}] initiation tau 20th pct {lo:.3f}, 80th {hi:.3f}; fast group {fq.sum()}, slow group {lq.sum()} (paper N = 116)")
    for off in ([0, 1000, 2000, 3000, 4000] if reading == "code" else [0]):
        rng = rng_for("fig2g-h-fast-slow-tau-groups", offset=off)
        pi, oi = tau_shuffle(I, fq, lq, rng)
        pw, ow = tau_shuffle(W, fq, lq, rng)
        print(f"   seed +{off}: initiation p = {pi:.3f} (observed tau diff {oi:+.3f}); wait time p = {pw:.3f} (observed {ow:+.3f})")
        R.setdefault("fig2gh", {})[(reading, off)] = (pi, pw)
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c4.py 2>&1 | grep -v "^---" | tail -30
```

```
wait time coefficients (current, 1..9 back, constant), mean over rats:
 [ 0.212  -0.0059 -0.0117 -0.0098 -0.0129 -0.0131 -0.0101 -0.0118 -0.0086
 -0.0109 -0.5284]
current offer: mean 0.2120, 95% interval across rats 0.2050 to 0.2191; rats with own CI excluding 0 and > 0: 289
largest |mean previous coefficient|: 0.0131 ; current larger than every previous: True
initiation coefficients (9 back), mean over rats: [-0.0289 -0.0235 -0.0116 -0.0065 -0.0029 -0.0018 -0.0006 -0.0011 -0.0004] | 1-3 back negative and decreasing in size: True
   rats with 1-back coefficient < 0: 261 of 291
initiation coefficients (10 back), mean over rats: [-0.0287 -0.0234 -0.0115 -0.0065 -0.0029 -0.0018 -0.0005 -0.001  -0.0004
 -0.0009] | 1-3 back negative and decreasing in size: True
   rats with 1-back coefficient < 0: 261 of 291
entries/mah-2023/mah2023.py:254: RuntimeWarning: divide by zero encountered in divide
  D = np.clip(YE / EE, lb[0], ub[0])
entries/mah-2023/mah2023.py:254: RuntimeWarning: invalid value encountered in divide
  D = np.clip(YE / EE, lb[0], ub[0])
[methods] wait time tau: mean 0.000, median 0.000, zero in 249 of 291; initiation tau: mean 0.000, median 0.000, zero in 18; signed-rank p = 6.8e-51; at the upper bound 10: wait 0, initiation 0
[code] wait time tau: mean 0.000, median 0.000, zero in 2 of 291; initiation tau: mean 0.000, median 0.000, zero in 28; signed-rank p = 2.07e-06; at the upper bound 10: wait 0, initiation 0
[methods] r = -0.016, p = 0.782 (paper: r = 0.08, p = 0.18 in the Results; r = -0.03, p = 0.53 in the legend); rats with nonzero wait time tau: 42
[code] r = -0.027, p = 0.645 (paper: r = 0.08, p = 0.18 in the Results; r = -0.03, p = 0.53 in the legend); rats with nonzero wait time tau: 289
nb/c4.py:11: RuntimeWarning: Mean of empty slice
  logv = np.log2(g.vol.to_numpy().astype(float))
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mah-2023 && python3 - <<'EOF'
s=open('mah2023.py').read()
s=s.replace("""    taus = np.unique(np.r_[np.linspace(max(lb[1], 1e-4), ub[1], ngrid),
                           np.geomspace(max(lb[1], 1e-4), ub[1], ngrid)])""","""    lo = max(lb[1], 0.01)  # below 0.01 trials the curve is 0 at every lag
    taus = np.unique(np.r_[np.linspace(lo, ub[1], ngrid), np.geomspace(lo, ub[1], ngrid)])""")
s=s.replace("""    sse = (Y * Y).sum(1)[:, None] - 2 * D * YE + D * D * EE
    k = np.argmin(sse, axis=1)""","""    sse = (Y * Y).sum(1)[:, None] - 2 * D * YE + D * D * EE
    sse = np.where(np.isfinite(sse), sse, np.inf)
    k = np.argmin(sse, axis=1)""")
open('mah2023.py','w').write(s)
EOF
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('c4.py').read()
s=s.replace("""    tw = np.where((W[:, 1:] if reading == "code" else W).any(1) if reading == "methods" else W.any(1), tw, 0.0)""","""    tw = np.where(W.any(1), tw, 0.0)""")
open('c4.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c4.py 2>&1 | grep -v "^---" | grep -v Warn | tail -16
```

```
rats with 1-back coefficient < 0: 261 of 291
initiation coefficients (10 back), mean over rats: [-0.0287 -0.0234 -0.0115 -0.0065 -0.0029 -0.0018 -0.0005 -0.001  -0.0004
 -0.0009] | 1-3 back negative and decreasing in size: True
   rats with 1-back coefficient < 0: 261 of 291
[methods] wait time tau: mean 0.065, median 0.000, zero in 249 of 291; initiation tau: mean 1.875, median 1.564, zero in 18; signed-rank p = 3.49e-45; at the upper bound 10: wait 0, initiation 6
[code] wait time tau: mean 0.620, median 0.611, zero in 2 of 291; initiation tau: mean 1.914, median 1.601, zero in 28; signed-rank p = 2.71e-35; at the upper bound 10: wait 0, initiation 7
[methods] r = -0.037, p = 0.535 (paper: r = 0.08, p = 0.18 in the Results; r = -0.03, p = 0.53 in the legend); rats with nonzero wait time tau: 42
[code] r = 0.111, p = 0.0589 (paper: r = 0.08, p = 0.18 in the Results; r = -0.03, p = 0.53 in the legend); rats with nonzero wait time tau: 289
[code] initiation tau 20th pct 0.785, 80th 2.491; fast group 58, slow group 58 (paper N = 116)
   seed +0: initiation p = 0.000 (observed tau diff -2.659); wait time p = 0.215 (observed -0.067)
   seed +1000: initiation p = 0.000 (observed tau diff -2.659); wait time p = 0.207 (observed -0.067)
   seed +2000: initiation p = 0.000 (observed tau diff -2.659); wait time p = 0.203 (observed -0.067)
   seed +3000: initiation p = 0.000 (observed tau diff -2.659); wait time p = 0.217 (observed -0.067)
   seed +4000: initiation p = 0.000 (observed tau diff -2.659); wait time p = 0.208 (observed -0.067)
[methods] initiation tau 20th pct 0.788, 80th 2.520; fast group 58, slow group 58 (paper N = 116)
   seed +0: initiation p = 0.000 (observed tau diff -2.488); wait time p = 0.394 (observed +0.018)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/nb/c5.py <<'EOF'
#%% md
## fig2j-wait-time-not-sensitive-to-previous-offer

> In mixed blocks, wait times for 20 uL do not depend on whether the previous offer was smaller or larger than 20 uL, for 87% of rats (253 of 291) and for the population.

Per rat, 20 uL opt-out catch trials in mixed blocks that are not the first trial of a session, wait times z-scored over these trials, split by the previous trial's offer below or above 20 uL (waittime_20ul_by_previous_vol.m), two-tailed rank-sum. Population: per-rat means, two-tailed rank-sum (legend); paired signed-rank (Figure2.m) as a variant.

#%% code claim:fig2j-wait-time-not-sensitive-to-previous-offer
sel = (t.vol == 20) & (t.block == 1) & t.wt.notna() & t.prev_vol.notna()
w = t[sel]
w = w.assign(z=w.groupby("subject").wt.transform(lambda x: (x - x.mean()) / x.std()))
lt, gt = w.prev_vol < 20, w.prev_vol > 20
pj = w.groupby("subject").apply(lambda g: M.ranksum_p(g.z[g.prev_vol < 20], g.z[g.prev_vol > 20]))
wj = pd.DataFrame({"lt": w[lt].groupby("subject").z.mean(), "gt": w[gt].groupby("subject").z.mean()})
n_sig = int((pj < 0.05).sum())
p_pop = M.ranksum_p(wj.lt, wj.gt); p_sr = stats.wilcoxon(wj.lt, wj.gt).pvalue
sens_wt = wj.lt - wj.gt
print(f"rats with p < 0.05: {n_sig} of {pj.notna().sum()} (expected 38 +- 4); not significant: {pj.notna().sum() - n_sig}")
print(f"population: mean z after < 20 uL {wj.lt.mean():+.4f}, after > 20 uL {wj.gt.mean():+.4f}; rank-sum p = {p_pop:.3g} (paper 0.8); signed-rank p = {p_sr:.3g} (variant)")
print(f"sensitivity (below minus above): mean {sens_wt.mean():+.4f}; trials per rat median {w.groupby('subject').size().median():.0f}")
print("rats with p < 0.05 by sex:", (pj < 0.05).groupby(sex).sum().to_dict())
R["fig2j"] = (n_sig, p_pop, p_sr, sens_wt.mean())

#%% md
**Result: see the summary.**

#%% md
## fig2k-initiation-sensitive-to-previous-offer

> In mixed blocks, trial initiation times are slower after offers smaller than 20 uL than after offers larger than 20 uL, significantly so for 89% of rats (256 of 291) and for the population.

Readings: (M) Methods, 20 uL trials in mixed blocks; (C) latency_post20ul_by_previous_vol.m, all mixed block trials; both with initiation times z-scored over all the rat's trials. Previous offer within the session. Per rat two-tailed rank-sum; population rank-sum on per-rat means (legend) and signed-rank (Figure2.m).

#%% code claim:fig2k-initiation-sensitive-to-previous-offer
FIG2K = {}
for name, m in [("M: 20 uL trials", (t.vol == 20)), ("C: all mixed trials", pd.Series(True, index=t.index))]:
    sel = m & (t.block == 1) & t.z_iti.notna() & t.prev_vol.notna()
    d = t.loc[sel, ["subject", "z_iti", "prev_vol"]]
    pk = d.groupby("subject").apply(lambda g: M.ranksum_p(g.z_iti[g.prev_vol < 20], g.z_iti[g.prev_vol > 20]))
    mk = pd.DataFrame({"lt": d[d.prev_vol < 20].groupby("subject").z_iti.mean(), "gt": d[d.prev_vol > 20].groupby("subject").z_iti.mean()})
    nsig = int((pk < 0.05).sum()); nsig_dir = int(((pk < 0.05) & (mk.lt > mk.gt)).sum())
    pp, ps = M.ranksum_p(mk.lt, mk.gt), stats.wilcoxon(mk.lt, mk.gt).pvalue
    FIG2K[name] = mk.lt - mk.gt
    R.setdefault("fig2k", {})[name] = (nsig, pp, ps, mk.lt.mean(), mk.gt.mean())
    print(f"[{name}] rats p < 0.05: {nsig} (expected 256 +- 26), of which slower after small offers {nsig_dir}; "
          f"mean z after < 20 {mk.lt.mean():+.4f}, after > 20 {mk.gt.mean():+.4f}; rank-sum p = {pp:.3g}; signed-rank p = {ps:.3g}")

#%% md
**Result: see the summary.**

#%% md
## fig2l-sensitivity-greater-for-initiation

> Sensitivity to the previous offer is larger for trial initiation times than for wait times across rats.

Sensitivity = mean for previous offer below 20 uL minus mean above, per rat, from fig2j and fig2k (each reading); paired signed-rank.

#%% code claim:fig2l-sensitivity-greater-for-initiation
for name, si in FIG2K.items():
    both = pd.DataFrame({"wt": sens_wt, "iti": si}).dropna()
    p = stats.wilcoxon(both.iti, both.wt).pvalue
    print(f"[{name}] mean sensitivity initiation {both.iti.mean():+.4f}, wait time {both.wt.mean():+.4f}; rats initiation > wait {int((both.iti > both.wt).sum())} of {len(both)}; signed-rank p = {p:.3g}")
    R.setdefault("fig2l", {})[name] = (both.iti.mean(), both.wt.mean(), p)

#%% md
**Result: see the summary.**

#%% md
## fig3c-wait-time-by-catch-probability

> Rats' wait times in mixed blocks depend in a graded way on the catch probability, as the wait time model predicts (shorter waits at higher catch probability).

Each rat's first 1000 deposited trials are left out (Figure3.m drops the first 1000 stage 8 trials; the dandiset starts at the first included session, see the data check). Per rat and catch probability (the trial's `catch_percentage`), mean wait time on mixed block opt-out catch trials by offer, then the mean over rats with data at that probability. Rats are counted at every probability they have data at (reading A), and, as a second reading (B), each rat is assigned to the probability of most of its remaining trials.

#%% code claim:fig3c-wait-time-by-catch-probability
pos = t.groupby("subject").cumcount()
late = t[(pos >= 1000)]
mw = late[(late.block == 1) & late.wt.notna()]
cur = mw.groupby(["catch_percentage", "subject", "vol"]).wt.mean().unstack()
counts_a = cur.groupby(level=0).size()
main_cp = late.groupby("subject").catch_percentage.agg(lambda x: x.value_counts().idxmax())
counts_b = main_cp.value_counts().sort_index()
print("rats with data at each probability (A):", counts_a.to_dict())
print("rats by main probability (B):", counts_b.to_dict())
print("expected: {0.1: 3, 0.15: 183, 0.2: 61, 0.25: 151, 0.35: 39}")
popA = cur.groupby(level=0).mean()
print("A: population mean wait time (s) by probability and offer:\n", popA.round(2))
curB = mw.assign(cp=mw.subject.map(main_cp))
curB = curB[curB.catch_percentage == curB.cp].groupby(["cp", "subject", "vol"]).wt.mean().unstack().groupby(level=0).mean()
print("B: by main probability:\n", curB.round(2))
for nm, P in [("A", popA), ("B", curB)]:
    if all(c in P.index for c in [0.15, 0.2, 0.25]):
        dec = ((P.loc[0.15] > P.loc[0.2]) & (P.loc[0.2] > P.loc[0.25]))
        print(f"{nm}: offers where wait time decreases 0.15 > 0.2 > 0.25: {int(dec.sum())} of 5", dec.to_dict())
        R.setdefault("fig3c", {})[nm] = int(dec.sum())
R["fig3c_counts"] = (counts_a.to_dict(), counts_b.to_dict())
# rats with several probabilities
print("rats with data at more than one probability:", int((mw.groupby('subject').catch_percentage.nunique() > 1).sum()))
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c5.py 2>&1 | grep -v "^---" | grep -v Warn | tail -36
```

```
Tue Nov 24 23:03:21 UTC 2026
catch x opt-out
 is_opt_out    False    True 
is_catch                    
False       8203026   245912
True         834587  1125174
rewarded x violation
 is_violation    False    True 
is_rewarded                   
False         1488923  4279059
True          4640717        0
wait_time                n=  6060844 min=    0.000 median=   2.226 max=   49.730 (s)
wait_time_unthresholded  n=  6129303 min=    0.000 median=   2.268 max=  100.000 (s)
wait_time_threshold      n= 10408699 min=   16.329 median=  27.152 max=   50.162 (s)
reward_delay             n= 10408699 min=    0.000 median=   2.328 max=  100.000 (s)
inter_trial_interval     n= 10395089 min=    0.000 median=   0.861 max= 6319.122 (s)
wait_for_center_poke     n= 10385666 min=    0.000 median=   1.775 max= 4375.440 (s)
wt                       n=  1072609 min=    0.000 median=  10.858 max=   49.730 (s)
iti                      n= 10268208 min=    0.000 median=   0.847 max=  341.034 (s)
reward_delay on is_catch trials: {100.0: 1959761}
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/w = w.assign(z=/w = w.assign(zw20=/; s/g\.z\[/g.zw20[/g; s/\.z\.mean()/.zw20.mean()/g' c5.py && grep -n "zw20" c5.py | head; cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c5.py 2>&1 | grep -v "^---" | grep -v Warn | tail -36
```

```
11:w = w.assign(zw20=w.groupby("subject").wt.transform(lambda x: (x - x.mean()) / x.std()))
13:pj = w.groupby("subject").apply(lambda g: M.ranksum_p(g.zw20[g.prev_vol < 20], g.zw20[g.prev_vol > 20]))
14:wj = pd.DataFrame({"lt": w[lt].groupby("subject").zw20.mean(), "gt": w[gt].groupby("subject").zw20.mean()})
catch x opt-out
 is_opt_out    False    True 
is_catch                    
False       8203026   245912
True         834587  1125174
rewarded x violation
 is_violation    False    True 
is_rewarded                   
False         1488923  4279059
True          4640717        0
wait_time                n=  6060844 min=    0.000 median=   2.226 max=   49.730 (s)
wait_time_unthresholded  n=  6129303 min=    0.000 median=   2.268 max=  100.000 (s)
wait_time_threshold      n= 10408699 min=   16.329 median=  27.152 max=   50.162 (s)
reward_delay             n= 10408699 min=    0.000 median=   2.328 max=  100.000 (s)
inter_trial_interval     n= 10395089 min=    0.000 median=   0.861 max= 6319.122 (s)
wait_for_center_poke     n= 10385666 min=    0.000 median=   1.775 max= 4375.440 (s)
wt                       n=  1072609 min=    0.000 median=  10.858 max=   49.730 (s)
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/"lt":/"below":/g; s/"gt":/"above":/g; s/wj\.lt/wj.below/g; s/wj\.gt/wj.above/g; s/mk\.lt/mk.below/g; s/mk\.gt/mk.above/g' c5.py && cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c5.py 2>&1 | grep -v "^---" | grep -v Warn | tail -28
```

```
rats with p < 0.05 by sex: {'F': 17, 'M': 21}
[M: 20 uL trials] rats p < 0.05: 276 (expected 256 +- 26), of which slower after small offers 17; mean z after < 20 -0.1609, after > 20 -0.0944; rank-sum p = 6.57e-30; signed-rank p = 2.85e-41
[C: all mixed trials] rats p < 0.05: 256 (expected 256 +- 26), of which slower after small offers 255; mean z after < 20 +0.0910, after > 20 -0.1477; rank-sum p = 9.94e-97; signed-rank p = 1.86e-49
[M: 20 uL trials] mean sensitivity initiation -0.0665, wait time -0.0094; rats initiation > wait 103 of 291; signed-rank p = 2.16e-06
[C: all mixed trials] mean sensitivity initiation +0.2387, wait time -0.0094; rats initiation > wait 245 of 291; signed-rank p = 1.6e-36
rats with data at each probability (A): {0.1: 3, 0.15: 188, 0.2: 61, 0.25: 151, 0.3: 8, 0.35: 40}
rats by main probability (B): {0.15: 105, 0.2: 43, 0.25: 128, 0.3: 6, 0.35: 9}
expected: {0.1: 3, 0.15: 183, 0.2: 61, 0.25: 151, 0.35: 39}
A: population mean wait time (s) by probability and offer:
 vol                  5      10     20     40     80
catch_percentage                                   
0.10              12.60  13.59  14.58  17.26  18.54
0.15              11.28  11.71  12.10  14.42  15.14
0.20              10.25  10.61  11.08  13.06  13.83
0.25              10.11  10.34  10.61  12.43  13.05
0.30               8.99   9.38   9.59  11.14  11.95
0.35               9.39   9.79   9.89  11.49  12.45
B: by main probability:
 vol      5      10     20     40     80
cp                                     
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c5.py 2>&1 | grep -A4 "rats with p < 0.05: " | head -5; date -u
```

```
rats with p < 0.05: 38 of 291 (expected 38 +- 4); not significant: 253
population: mean z after < 20 uL -0.0044, after > 20 uL +0.0049; rank-sum p = 0.575 (paper 0.8); signed-rank p = 0.629 (variant)
sensitivity (below minus above): mean -0.0094; trials per rat median 378
rats with p < 0.05 by sex: {'F': 17, 'M': 21}
--- [code claim:fig2j-wait-time-not-sensitive-to-previous-offer] 0.5s
Tue Nov 24 23:04:42 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/c6.py <<'EOF'
#%% md
## pre-cue-session-link

> The rats and switch dates that the paper's Figure5.m lists mark which of the dandiset's sessions were run on the pre-initiation cue task, which nothing in the files marks.

Input (with_labels): `ratListAll` and `startDates` of Figure5.m (github.com/constantinoplelab/published at b7b68ca8c107d8ce4a061e16da214307f175c3e5, rat_behavior/Figures/Figure5.m), copied below; the code pairs date rr with rat rr, so the first 16 of its 20 dates are used. The files also hold a task argument, `center_port_cue`, which is compared with the dates.

#%% code claim:pre-cue-session-link
# From Figure5.m at b7b68ca8c107 (outside input, names and dates only)
PRECUE_RATS = ['M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'G070', 'E005', 'E008',
               'G078', 'G076', 'G069', 'S042', 'S050']
PRECUE_DATES = ['2022-10-04', '2022-10-04', '2022-10-04', '2022-10-04', '2022-12-13', '2022-12-13', '2022-12-13',
                '2022-12-13', '2022-10-24', '2022-10-24', '2022-10-24', '2022-11-07', '2022-11-14', '2022-11-14',
                '2022-12-21', '2022-12-22', '2023-01-03', '2023-01-03', '2023-01-23', '2023-01-25']
SECOND_GROUP = ['M045', 'M046', 'M047', 'M048']  # Figure5.m secondGroup
start_date = dict(zip(PRECUE_RATS, pd.to_datetime(PRECUE_DATES[:16])))
ses = sessions.copy()
ses["day"] = ses.path.str.extract(r"-(\d{8})-\d{6}\.nwb$")[0].pipe(pd.to_datetime, format="%Y%m%d")
ses["after_date"] = ses.subject.map(start_date).notna() & (ses.day >= ses.subject.map(start_date))
ses["cue_flag"] = ses.center_port_cue == "True"
print("rats with any center_port_cue = True session:", sorted(ses[ses.cue_flag].subject.unique()))
print("of them in Figure5.m's list:", sorted(set(ses[ses.cue_flag].subject) & set(PRECUE_RATS)))
tab = ses[ses.subject.isin(PRECUE_RATS)].groupby("subject").apply(lambda g: pd.Series({
    "sessions": len(g), "before_date": int((~g.after_date).sum()), "after_date": int(g.after_date.sum()),
    "flag_true": int(g.cue_flag.sum()), "after_and_flag": int((g.after_date & g.cue_flag).sum()),
    "first_flag_day": g.loc[g.cue_flag, "day"].min(), "date": start_date[g.name]}))
print(tab.to_string())
sess_of = t.sess.map(ses.set_index(ses.index)["after_date"]) if False else None
t["after_date"] = ses.after_date.to_numpy()[t.sess.to_numpy()]
t["cue_flag"] = ses.cue_flag.to_numpy()[t.sess.to_numpy()]
link = {}
for r in PRECUE_RATS:
    g = t[(t.subject == r) & (t.block == 1) & t.z_iti.notna() & (t.prev_is_rewarded.notna())]
    g = g[~t.loc[g.index, "is_violation"].shift(1, fill_value=False).to_numpy()]  # placeholder, replaced below
    link[r] = None
# post-violation trials: the previous trial in the session was a violation
pv = t.is_violation.shift(1).where(t.trial > 0).fillna(False).astype(bool)
t["post_violation"] = pv.to_numpy()
rows = []
for r in PRECUE_RATS:
    g = t[(t.subject == r) & (t.block == 1) & t.z_iti.notna() & ~t.post_violation]
    out = {"rat": r}
    for nm, m in [("before", ~g.after_date), ("after", g.after_date)]:
        h = g[m]
        if len(h) < 50:
            out[nm + "_slope"], out[nm + "_anova_p"] = np.nan, np.nan
            continue
        out[nm + "_slope"] = np.polyfit(np.log2(h.vol.astype(float)), h.z_iti, 1)[0]
        out[nm + "_anova_p"] = stats.f_oneway(*[h.z_iti[h.vol == v] for v in [5, 10, 20, 40, 80]]).pvalue
    b = out["before_slope"]
    out["linked"] = bool(out["after_anova_p"] < 0.05 and (out["after_slope"] < b if np.isfinite(b) else out["after_slope"] < 0))
    rows.append(out)
LINK = pd.DataFrame(rows).set_index("rat")
print(LINK.round(4).to_string())
print("linked rats:", int(LINK.linked.sum()), "of 16")
R["link"] = int(LINK.linked.sum())
# the same test with the center_port_cue flag in place of the dates
rows = []
for r in PRECUE_RATS:
    g = t[(t.subject == r) & (t.block == 1) & t.z_iti.notna() & ~t.post_violation]
    s_ = {nm: (np.polyfit(np.log2(g[m].vol.astype(float)), g[m].z_iti, 1)[0] if m.sum() > 50 else np.nan)
          for nm, m in [("flag_false_or_absent", ~g.cue_flag), ("flag_true", g.cue_flag)]}
    rows.append({"rat": r, **s_})
print("slope of z-scored initiation time on log2 offer, by center_port_cue:\n", pd.DataFrame(rows).set_index("rat").round(4).to_string())

#%% md
**Result: see the summary.**

#%% md
## fig5b-pre-cue-initiation-sensitive-to-offer

> With the reward cue played before trial initiation, trial initiation times become sensitive to the offered reward.

Pre-cue sessions from the link (dates of Figure5.m): for the 12 rats that switched, (a) sessions after the first 30 pre-cue sessions (Methods) or (b) all sessions from the date (Figure5.m); for the 4 of `secondGroup`, all sessions; original-task sessions are those before the date. The dandiset holds only included sessions, so the paper's "no session exclusion" cannot be applied. Per rat, mean z-scored initiation time by offer in mixed blocks, post-violation trials left out, one-way ANOVA over offers.

#%% code claim:fig5b-pre-cue-initiation-sensitive-to-offer
pc_rank = ses[ses.after_date].groupby("subject").cumcount()
ses["precue_n"] = np.nan
ses.loc[pc_rank.index, "precue_n"] = pc_rank
t["precue_n"] = ses.precue_n.to_numpy()[t.sess.to_numpy()]
def precue_mask(reading):
    m = t.after_date.copy()
    if reading == "a":
        m &= (t.precue_n >= 30) | t.subject.isin(SECOND_GROUP)
    return m
FIG5 = {}
for reading in ["a", "b"]:
    pm = precue_mask(reading)
    res = {}
    for task, m in [("pre-cue", pm), ("original", ~t.after_date & t.subject.isin(PRECUE_RATS))]:
        g = t[m & t.subject.isin(PRECUE_RATS) & (t.block == 1) & t.z_iti.notna() & ~t.post_violation]
        cur = g.groupby(["subject", "vol"]).z_iti.mean().unstack()
        pa = g.groupby("subject").apply(lambda h: stats.f_oneway(*[h.z_iti[h.vol == v] for v in [5, 10, 20, 40, 80] if (h.vol == v).sum() > 1]).pvalue)
        res[task] = (cur, pa)
        print(f"[{reading}] {task}: rats {len(cur)}, population mean z by offer {cur.mean().round(3).to_dict()}; "
              f"decreasing at every step: {bool((np.diff(cur.mean().to_numpy()) < 0).all())}; rats ANOVA p < 0.05: {int((pa < 0.05).sum())}")
    FIG5[reading] = res
    R.setdefault("fig5b", {})[reading] = (bool((np.diff(res["pre-cue"][0].mean().to_numpy()) < 0).all()),
                                          int((res["pre-cue"][1] < 0.05).sum()), int((res["original"][1] < 0.05).sum()),
                                          len(res["original"][0]))
print("trials per rat in reading (a):", t[precue_mask("a") & t.subject.isin(PRECUE_RATS)].groupby("subject").size().to_dict())

#%% md
**Result: see the summary.**

#%% md
## fig5c-pre-cue-initiation-still-sensitive-to-previous-reward

> On the pre-initiation cue task, trial initiation times for 20 uL in mixed blocks are still modulated by the previous reward, for 13 of 16 rats and for the population.

The test of fig2k under each of its readings, on the pre-cue sessions of fig5b (each reading of the sessions).

#%% code claim:fig5c-pre-cue-initiation-still-sensitive-to-previous-reward
for reading in ["a", "b"]:
    pm = precue_mask(reading) & t.subject.isin(PRECUE_RATS)
    for name, m in [("M: 20 uL trials", t.vol == 20), ("C: all mixed trials", pd.Series(True, index=t.index))]:
        d = t.loc[pm & m & (t.block == 1) & t.z_iti.notna() & t.prev_vol.notna(), ["subject", "z_iti", "prev_vol"]]
        pk = d.groupby("subject").apply(lambda g: M.ranksum_p(g.z_iti[g.prev_vol < 20], g.z_iti[g.prev_vol > 20]))
        mk = pd.DataFrame({"below": d[d.prev_vol < 20].groupby("subject").z_iti.mean(), "above": d[d.prev_vol > 20].groupby("subject").z_iti.mean()})
        pp = M.ranksum_p(mk.below, mk.above)
        n_dir = int(((pk < 0.05) & (mk.below > mk.above)).sum())
        print(f"[sessions {reading}, {name}] rats p < 0.05: {int((pk < 0.05).sum())} of {len(pk)} (expected 13 +- 1), slower after small offers {n_dir}; "
              f"population mean below {mk.below.mean():+.3f}, above {mk.above.mean():+.3f}; rank-sum p = {pp:.3g}; signed-rank p = {stats.wilcoxon(mk.below, mk.above).pvalue:.3g}")
        R.setdefault("fig5c", {})[(reading, name)] = (int((pk < 0.05).sum()), pp, mk.below.mean() > mk.above.mean())

#%% md
**Result: see the summary.**

#%% md
## fig5d-pre-cue-initiation-depends-on-previous-block

> On the pre-initiation cue task, how quickly rats initiate trials in mixed blocks still depends on the previous block.

Initiation time transition curves as in fig2a (z-scored, detrended per session), on the pre-cue sessions; mean over trials 1 to 20 of mixed blocks after high and after low blocks, signed-rank across the 16 rats.

#%% code claim:fig5d-pre-cue-initiation-depends-on-previous-block
for reading in ["a", "b"]:
    pm = precue_mask(reading) & t.subject.isin(PRECUE_RATS)
    tr5 = trans[pm.to_numpy()[trans.idx.to_numpy()]]
    c5 = M.transition_curves(t, t.iti_dt_sess, tr5, rats=PRECUE_RATS)
    a, b_ = c5[HM].loc[:, 1:20].mean(1), c5[LM].loc[:, 1:20].mean(1)
    p = stats.wilcoxon(a, b_).pvalue
    print(f"[sessions {reading}] trials 1-20 of mixed blocks: after high {a.mean():+.3f}, after low {b_.mean():+.3f}; rats higher after high {int((a > b_).sum())} of {len(a)}; signed-rank p = {p:.3g}")
    R.setdefault("fig5d", {})[reading] = (a.mean(), b_.mean(), p)
EOF
cd $TMPDIR/nb && python3 - <<'EOF'
# remove the placeholder loop
s=open('c6.py').read()
a=s.index('sess_of = t.sess.map'); b=s.index('# post-violation trials')
s=s[:a]+'t["after_date"] = ses.after_date.to_numpy()[t.sess.to_numpy()]\nt["cue_flag"] = ses.cue_flag.to_numpy()[t.sess.to_numpy()]\n'+s[b:]
open('c6.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c3.py nb/c6.py 2>&1 | grep -v "^---" | grep -v Warn | sed -n '/rats with any center/,$p'
```

```
rats with any center_port_cue = True session: ['E005', 'E008', 'G069', 'G070', 'G076', 'G078', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'S042', 'S050']
of them in Figure5.m's list: ['E005', 'E008', 'G069', 'G070', 'G076', 'G078', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'S042', 'S050']
         sessions  before_date  after_date  flag_true  after_and_flag first_flag_day       date
subject                                                                                        
E005           80           59          21         15              15     2022-11-07 2022-10-24
E008          152           78          74         73              73     2022-10-25 2022-10-24
G069          202          127          75         75              75     2022-11-14 2022-11-14
G070          106           69          37         37              37     2022-10-25 2022-10-24
G076          108           53          55         54              54     2022-11-15 2022-11-14
G078          129          102          27         26              26     2022-11-08 2022-11-07
M041           98           64          34         33              33     2022-10-05 2022-10-04
M042           76           62          14         13              13     2022-10-05 2022-10-04
M043          119           58          61         60              60     2022-10-05 2022-10-04
M044          150           61          89         89              89     2022-10-05 2022-10-04
M045           69            0          69         69              69     2023-01-18 2022-12-13
M046           57            0          57         57              57     2023-02-02 2022-12-13
M047           69            0          69         69              69     2023-01-10 2022-12-13
M048           73            0          73         73              73     2023-01-17 2022-12-13
S042           81           56          25         13              13     2023-01-24 2022-12-21
S050           33           22     
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('c6.py').read()
s=s.replace("    a, b_ = c5[HM].loc[:, 1:20].mean(1), c5[LM].loc[:, 1:20].mean(1)\n","    ab = pd.DataFrame({'h': c5[HM].loc[:, 1:20].mean(1), 'l': c5[LM].loc[:, 1:20].mean(1)}).dropna()\n    a, b_ = ab.h, ab.l\n")
open('c6.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import fsspec, zipfile, io, scipy.io as sio, numpy as np, time
url="https://zenodo.org/api/records/10031483/files/published.zip/content"
z=zipfile.ZipFile(fsspec.open(url, block_size=2**20).open())
t=time.time(); b=z.read('published/A_Structs_all/ratTrial_M041.mat'); m=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
print(time.time()-t, [k for k in m if not k.startswith('__')])
A=m['ratTrial'] if 'ratTrial' in m else m[[k for k in m if not k.startswith('__')][0]]
for f in A._fieldnames:
    v=getattr(A,f); print(f, type(v), getattr(v,'shape',None), (v[:3] if hasattr(v,'__len__') and not isinstance(v,str) else v))
r=z.read('published/ratList.mat'); print(sio.loadmat(io.BytesIO(r),squeeze_me=True).keys())
EOF
```

```
0.6864626407623291 ['A']
date <class 'scipy.io.matlab._mio5_params.MatlabOpaque'> (1,) [('MCOS', 'datetime', array([3707764736,          2,          1,          1,          1,
                 1], dtype=uint32))                                                     ]
trainingstage <class 'numpy.ndarray'> (59068,) [8 8 8]
nic <class 'numpy.ndarray'> (59068,) [0.94042    0.85473415 1.05770431]
catch <class 'numpy.ndarray'> (59068,) [0 0 1]
prob_catch <class 'numpy.ndarray'> (59068,) [0.15 0.15 0.15]
adapt_block <class 'numpy.ndarray'> (59068,) [40 40 40]
test_block <class 'numpy.ndarray'> (59068,) [40 40 40]
reward <class 'numpy.ndarray'> (59068,) [20 20 20]
reward_delay <class 'numpy.ndarray'> (59068,) [  3.1365      2.7521944 100.       ]
block <class 'numpy.ndarray'> (59068,) [1 1 1]
hits <class 'numpy.ndarray'> (59068,) [0 0 0]
vios <class 'numpy.ndarray'> (59068,) [1 1 1]
optout <class 'numpy.ndarray'> (59068,) [0 0 0]
wait_time <class 'numpy.ndarray'> (59068,) [nan nan nan]
wait_for_cpoke <class 'numpy.ndarray'> (59068,) [     nan 132.2171  33.866 ]
zwait_for_cpoke <class 'numpy.ndarray'> (59068,) [       nan 9.32531335 1.90572869]
ntrials <class 'numpy.ndarray'> (118,) [269 348 382]
trial_num <class 'numpy.ndarray'> (59068,) [1 2 3]
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" Analysis/macro_regress_overtraining_V2.m | grep -v "^\s*$" | head -70; grep -v "^\s*%" Figures/Figure4.m | grep -v "^\s*$" | sed -n 1,140p | grep -iv "set(\|xlabel\|ylabel\|title\|xlim\|ylim\|plot(\|shade\|line(\|legend\|subplot\|figure\|axis\|text(\|colororder"
```

```
function [B1, B2, B1iti, B2iti,...
    dwt1, dwt2, diti1, diti2,...
    pcatch1, pcatch2, pvio_iti1, pvio_iti2] =...
    macro_regress_overtraining_V2(nsess, ratList, Sdir)
grp = 2;
[B1, B2, B1iti, B2iti] = deal(cell(1, 3));
for k = 1:3
    B1{k} = nan(length(ratList), ceil(nsess/grp));
    B2{k} = nan(length(ratList), ceil(nsess/grp));
    B1iti{k} = nan(length(ratList), ceil(nsess/grp));
    B2iti{k} = nan(length(ratList), ceil(nsess/grp));
end
dwt1 = nan(length(ratList), ceil(nsess/grp)); dwt2 = dwt1;
diti1 = dwt1; diti2 = dwt1;
pcatch1 = dwt1; pcatch2 = dwt1;
pvio_iti1 = dwt1;
pvio_iti2 = dwt2;
for rr = 1:length(ratList)
    disp(rr);
    a = load([Sdir 'ratTrial_' ratList{rr} '.mat']);
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/mah-2023/mah2023.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# The paper's Zenodo deposit (doi:10.5281/zenodo.10031483, published.zip): A_Structs_all holds
# every session that ended in the final stage, the data of Figure 4 (its README.txt).
# ---------------------------------------------------------------------------------------------

ZENODO_URL = "https://zenodo.org/api/records/10031483/files/published.zip/content"


def _zip():
    import fsspec
    import zipfile
    return zipfile.ZipFile(fsspec.open(ZENODO_URL, block_size=2 ** 20).open())


def zenodo_rat_list():
    import scipy.io as sio
    m = sio.loadmat(io.BytesIO(_zip().read("published/ratList.mat")), squeeze_me=True)
    return [str(x) for x in m["ratList"]], [str(x) for x in m["sexList"]]


def _read_astruct(args):
    import threading
    import scipy.io as sio
    rat, folder, local = args
    if not hasattr(local, "z"):
        local.z = _zip()
    b = local.z.read(f"published/{folder}/ratTrial_{rat}.mat")
    A = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)["A"]
    nt = np.atleast_1d(A.ntrials).astype(int)
    d = {k: np.atleast_1d(getattr(A, k)).astype(float) for k in
         ["trainingstage", "catch", "prob_catch", "reward", "block", "hits", "vios", "optout",
          "wait_time", "ITI", "wait_time_unthresholded"]}
    df = pd.DataFrame(d)
    df["sess_in_rat"] = np.repeat(np.arange(len(nt)), nt)
    df["subject"] = rat
    df["wait_thresh"] = float(A.wait_thresh)
    return df


def load_zenodo_astructs(rats, folder="A_Structs_all", workers=8):
    """Per-trial table of the deposit's A structs for `rats` (sessions in file order)."""
    import threading
    local = threading.local()
    with ThreadPoolExecutor(workers) as ex:
        parts = list(ex.map(_read_astruct, [(r, folder, local) for r in rats]))
    return pd.concat(parts, ignore_index=True)
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys,time; sys.path.insert(0,'entries/mah-2023')
import mah2023 as M
t=time.time(); rl,sl=M.zenodo_rat_list(); print(len(rl), time.time()-t)
Z=M.load_zenodo_astructs(rl, workers=12); print(time.time()-t, len(Z), Z.memory_usage().sum()/1e9)
Z.to_parquet('zall.parquet')
print(Z.trainingstage.value_counts())
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
Exit code 1
291 1.8946716785430908
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "entries/mah-2023/mah2023.py", line 374, in load_zenodo_astructs
    parts = list(ex.map(_read_astruct, [(r, folder, local) for r in rats]))
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 460, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
  File "entries/mah-2023/mah2023.py", line 356, in _read_astruct
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mah-2023 && python3 - <<'EOF'
s=open('mah2023.py').read()
a=s.index('def _read_astruct'); 
s=s[:a]+'''def _range(url, start, end, tries=6):
    req = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(15 * (i + 1))  # Zenodo answers 429 when asked too often


def _parse_astruct(rat, raw):
    import scipy.io as sio
    A = sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)["A"]
    nt = np.atleast_1d(A.ntrials).astype(int)
    d = {k: np.atleast_1d(getattr(A, k)).astype(float) for k in
         ["trainingstage", "catch", "prob_catch", "reward", "block", "hits", "vios", "optout",
          "wait_time", "ITI", "wait_time_unthresholded"]}
    df = pd.DataFrame(d)
    df["sess_in_rat"] = np.repeat(np.arange(len(nt)), nt)
    df["subject"] = rat
    df["wait_thresh"] = float(A.wait_thresh)
    return df


def load_zenodo_astructs(rats, folder="A_Structs_all", chunk=64 * 2 ** 20):
    """Per-trial table of the deposit's A structs for `rats` (sessions in file order). The
    members are read from the zip by a few large range requests (Zenodo limits the request
    rate) and inflated in memory."""
    import struct
    import zlib as _zl
    z = _zip()
    infos = {i.filename: i for i in z.infolist()}
    want = [infos[f"published/{folder}/ratTrial_{r}.mat"] for r in rats]
    lo = min(i.header_offset for i in want)
    hi = max(i.header_offset + 30 + len(i.filename) + 1024 + i.compress_size for i in want)
    buf = bytearray()
    for s in range(lo, hi, chunk):
        buf += _range(ZENODO_URL, s, min(s + chunk, hi) - 1)
    parts = []
    for r, i in zip(rats, want):
        o = i.header_offset - lo
        n, m = struct.unpack("<HH", buf[o + 26:o + 30])
        start = o + 30 + n + m
        data = bytes(buf[start:start + i.compress_size])
        raw = _zl.decompressobj(-15).decompress(data) if i.compress_type == 8 else data
        parts.append(_parse_astruct(r, raw))
    return pd.concat(parts, ignore_index=True)
'''
open('mah2023.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys,time; sys.path.insert(0,'entries/mah-2023')
import mah2023 as M
t=time.time(); rl,sl=M.zenodo_rat_list(); print(len(rl), time.time()-t)
Z=M.load_zenodo_astructs(rl); print(time.time()-t, len(Z), Z.memory_usage().sum()/1e9)
Z.to_parquet('zall.parquet')
print(Z.trainingstage.value_counts())
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/fsspec/implementations/http.py", line 447, in _info
    await _file_info(
    ...<5 lines>...
    )
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/fsspec/implementations/http.py", line 865, in _file_info
    r.raise_for_status()
    ~~~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/aiohttp/client_reqrep.py", line 842, in raise_for_status
    raise ClientResponseError(
    ...<5 lines>...
    )
aiohttp.client_exceptions.ClientResponseError: 429, message='TOO MANY REQUESTS', url='https://zenodo.org/api/records/10031483/files/published.zip/content'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "entries/mah-2023/mah2023.py", line 346, in zenodo_rat_list
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mah-2023 && python3 - <<'EOF'
s=open('mah2023.py').read()
s=s.replace('''def zenodo_rat_list():
    import scipy.io as sio
    m = sio.loadmat(io.BytesIO(_zip().read("published/ratList.mat")), squeeze_me=True)
    return [str(x) for x in m["ratList"]], [str(x) for x in m["sexList"]]
''','''def zenodo_rat_list(z):
    import scipy.io as sio
    m = sio.loadmat(io.BytesIO(z.read("published/ratList.mat")), squeeze_me=True)
    return [str(x) for x in m["ratList"]], [str(x) for x in m["sexList"]]
''')
s=s.replace('''def _zip():
    import fsspec''','''def zenodo_zip():
    """The deposit's zip, opened over HTTP range requests (its directory is read once)."""
    import fsspec''')
s=s.replace('''def load_zenodo_astructs(rats, folder="A_Structs_all", chunk=64 * 2 ** 20):''','''def load_zenodo_astructs(z, rats, folder="A_Structs_all", chunk=64 * 2 ** 20):''')
s=s.replace('''    z = _zip()
    infos = {i.filename''','''    infos = {i.filename''')
open('mah2023.py','w').write(s)
EOF
grep -n "_zip()" mah2023.py; sleep 60; cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys,time; sys.path.insert(0,'entries/mah-2023')
import mah2023 as M
t=time.time(); z=M.zenodo_zip(); rl,sl=M.zenodo_rat_list(z); print(len(rl), time.time()-t)
Z=M.load_zenodo_astructs(z, rl); print(time.time()-t, len(Z), Z.memory_usage().sum()/1e9)
Z.to_parquet('zall.parquet')
print(Z.trainingstage.value_counts())
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
338:def zenodo_zip():
291 1.9187679290771484
85.43058681488037 13433378 1.559951277
trainingstage
9.0    13111937
1.0      111272
8.0       63728
7.0       48984
3.0       33123
6.0       22322
4.0       21080
5.0       20841
2.0          91
Name: count, dtype: int64
3.647892
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/c7.py <<'EOF'
#%% md
## Figure 4: data from the paper's Zenodo deposit

Figure 4 uses all final-stage sessions, including those that fail the inclusion criterion (Methods, Learning dynamics). The dandiset holds only the included sessions (data check), so the claims of Figure 4 are tested on `A_Structs_all` of the paper's own deposit, doi:10.5281/zenodo.10031483 (`published.zip`, version v1), which its README describes as all sessions that ended on the final training stage, "only used for Figure 4". Only trials with `trainingstage` 9 (the paper's stage 8) are kept. Wait times above the rat's `wait_thresh` are removed and initiation times above the rat's 99th percentile (macro_regress_overtraining_V2.m). The deposit has no session dates that this reader decodes; sessions are taken in file order.

#%% code
TZ = time.time()
zz = M.zenodo_zip()
z_rats, z_sex = M.zenodo_rat_list(zz)
Z = M.load_zenodo_astructs(zz, z_rats)
print(f"loaded {len(Z)} trials of {Z.subject.nunique()} rats in {time.time()-TZ:.0f} s; trainingstage counts:", Z.trainingstage.value_counts().to_dict())
print("rats in the deposit's ratList that are in the dandiset:", len(set(z_rats) & set(rats)), "of", len(z_rats))
Z = Z[Z.trainingstage == 9].copy()
Z["sess"] = Z.groupby(["subject", "sess_in_rat"], sort=False).ngroup()
Z["sess_in_rat"] = Z.groupby("subject").sess.transform(lambda s: s.rank(method="dense").astype(int) - 1)
Z["trial"] = Z.groupby("sess").cumcount()
Z["vol"] = Z.reward.round().astype(int).map(M.VOL_MAP)
Z["block"] = Z.block.astype(int)
Z["wt"] = Z.wait_time.where((Z.catch == 1) & (Z.optout == 1) & (Z.wait_time <= Z.wait_thresh))
nz = Z.groupby("subject").sess_in_rat.max() + 1
nd = sessions.groupby("subject").size()
print(f"final-stage sessions per rat: deposit median {nz.median():.0f} (range {nz.min()}-{nz.max()}), dandiset median {nd.median():.0f}; "
      f"rats with more sessions in the deposit than the dandiset: {int((nz.reindex(nd.index) > nd).sum())}, fewer: {int((nz.reindex(nd.index) < nd).sum())}")
print(f"final-stage trials: deposit {len(Z)}, dandiset {len(t)}")

def prep_iti(df):
    """Initiation times as block_dynamics_latency.m: first trial of each session NaN, values above
    the rat's 99th percentile (over the trials passed) removed, z-scored per rat."""
    v = df.ITI.where(df.trial > 0)
    p99 = v.groupby(df.subject).transform(lambda x: np.nanpercentile(x, 99) if x.notna().any() else np.nan)
    v = v.where(v <= p99)
    g = v.groupby(df.subject)
    return v, (v - g.transform("mean")) / g.transform("std")

Z["iti"], Z["z_iti"] = prep_iti(Z)

#%% md
## fig4a-wait-time-block-sensitivity-emerges

> When the hidden blocks are introduced, wait times for 20 uL become sensitive to the block only gradually over training, while trial initiation times are block sensitive from the first session.

First 50 final-stage sessions per rat, in pairs; per pair the wait time ratio (20 uL, high over low) and the initiation time ratio (high over low). Per session, wait time on opt-out catch trials regressed on current reward and block (1 low, 2 mixed, 3 high); the block coefficient smoothed with a 5-session moving average, outliers (3 scaled MADs from a 5-point moving median) set to NaN, then averaged over rats (Methods, Learning dynamics). The reward enters as log2 offer (the Methods say "current reward"; linear offer is shown as a variant).

#%% code claim:fig4a-wait-time-block-sensitivity-emerges
Z50 = Z[Z.sess_in_rat < 50].copy()
Z50["pair"] = Z50.sess_in_rat // 2
w = Z50[(Z50.vol == 20) & Z50.wt.notna() & Z50.block.isin([2, 3])]
wr = w.groupby(["subject", "pair", "block"]).wt.mean().unstack()
wt_pair = (wr[2] / wr[3]).unstack()
i_ = Z50[Z50.iti.notna() & Z50.block.isin([2, 3])]
ir = i_.groupby(["subject", "pair", "block"]).iti.mean().unstack()
iti_pair = (ir[2] / ir[3]).unstack()
print("rats with a ratio in pair 1: wait", int(wt_pair[0].notna().sum()), "initiation", int(iti_pair[0].notna().sum()))
print("mean wait time ratio by pair:", wt_pair.mean().round(3).to_list())
print("mean initiation ratio by pair:", iti_pair.mean().round(3).to_list())
f_iti = iti_pair[0].dropna()
p1 = stats.wilcoxon(f_iti - 1).pvalue
w_first, w_last = wt_pair[0].mean(), wt_pair.loc[:, 15:24].mean(1).mean()
print(f"(1) first pair initiation ratio: mean {f_iti.mean():.3f}, n {len(f_iti)}, signed-rank against 1 p = {p1:.3g}")
print(f"(2) wait time ratio first pair {w_first:.3f} (|1 - r| = {abs(1-w_first):.3f}); mean over pairs 16-25 {w_last:.3f} (|1 - r| = {abs(1-w_last):.3f})")

def session_coefs(df, kind, logrew=True):
    out = {}
    for (r, s), g in df.groupby(["subject", "sess_in_rat"]):
        if kind == "block":
            h = g[g.wt.notna()]
            if len(h) < 5 or h.block.nunique() < 2:
                continue
            x1 = np.log2(h.vol.astype(float)) if logrew else h.vol.astype(float)
            blk = h.block.map({3: 1, 1: 2, 2: 3}).astype(float)
            X = np.c_[x1, blk, np.ones(len(h))]
            out[(r, s)] = np.linalg.lstsq(X, h.wt.to_numpy(), rcond=None)[0][1]
        else:
            pr = np.log2(g.vol.astype(float).shift(1)) * g.hits.shift(1)
            ok = pr.notna() & g.iti.notna()
            if ok.sum() < 10:
                continue
            X = np.c_[pr[ok], np.ones(ok.sum())]
            out[(r, s)] = np.linalg.lstsq(X, g.iti[ok].to_numpy(), rcond=None)[0][0]
    return pd.Series(out).unstack()

def smooth_clean(C):
    """5-session moving average per rat, then outliers (3 scaled MADs from a 5-point moving median,
    Matlab isoutlier 'movmedian') set to NaN."""
    S = C.T.rolling(5, center=True, min_periods=1).mean()
    med = S.rolling(5, center=True, min_periods=1).median()
    mad = (S - med).abs().rolling(5, center=True, min_periods=1).median() * 1.4826
    S = S.where(~((S - med).abs() > 3 * mad))
    return S.T

B = {lg: smooth_clean(session_coefs(Z50, "block", lg)) for lg in [True, False]}
for lg in [True, False]:
    b = B[lg].mean()
    e, l = b.loc[0:9].mean(), b.loc[40:49].mean()
    print(f"(3) block coefficient ({'log2' if lg else 'linear'} reward): sessions 1-10 {e:.4f}, sessions 41-50 {l:.4f}; grows in size: {abs(l) > abs(e)}")
R["fig4a"] = (f_iti.mean(), p1, w_first, w_last, B[True].mean().loc[0:9].mean(), B[True].mean().loc[40:49].mean())
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].plot(np.arange(1, 26) * 2, wt_pair.mean().values, label="wait time"); ax[0].plot(np.arange(1, 26) * 2, iti_pair.mean().values, label="initiation")
ax[0].axhline(1, color="k", lw=0.5); ax[0].legend(); ax[0].set_xlabel("session"); ax[0].set_ylabel("ratio high/low")
ax[1].plot(B[True].mean().values); ax[1].set_title("block coefficient"); plt.show()
print("plotted ranges: wait ratio", wt_pair.mean().min().round(3), "-", wt_pair.mean().max().round(3),
      "| initiation ratio", iti_pair.mean().min().round(3), "-", iti_pair.mean().max().round(3))

#%% md
**Result: see the summary.**

#%% md
## fig4c-initiation-previous-reward-stable

> The effect of the previous reward on trial initiation times is comparable early and late in training.

Per session, initiation time regressed on the previous reward (log2 offer times hit, 0 when unrewarded, as fig2c-d), smoothed and cleaned as in fig4a, averaged over rats.

#%% code claim:fig4c-initiation-previous-reward-stable
Cp = smooth_clean(session_coefs(Z50, "prev"))
c = Cp.mean()
ce, cl = c.loc[0:9].mean(), c.loc[40:49].mean()
b = B[True].mean(); be, bl = b.loc[0:9].mean(), b.loc[40:49].mean()
rel_c, rel_b = abs(ce - cl) / abs(cl), abs(be - bl) / abs(bl)
print(f"previous reward coefficient: sessions 1-10 {ce:.4f}, 41-50 {cl:.4f}; same sign: {np.sign(ce) == np.sign(cl)}; relative change {rel_c:.3f}")
print(f"wait time block coefficient relative change {rel_b:.3f}; initiation change smaller: {rel_c < rel_b}")
print("rats with a coefficient in session 1:", int(Cp[0].notna().sum()), "and session 50:", int(Cp[49].notna().sum()) if 49 in Cp else 0)
R["fig4c"] = (ce, cl, rel_c, rel_b)

#%% md
**Result: see the summary.**

#%% md
## fig4d-overshoot-grows-with-training

> The overshoot of trial initiation times after transitions from high to mixed blocks becomes more prominent with training, on a timescale like that of block sensitivity for wait times.

Per rat, the first 10 and the last 10 final-stage sessions (Figure4.m, nsess = 10); initiation times z-scored over those sessions and detrended with one line over trial number (block_dynamics_latency.m); high-to-mixed curves smoothed (10 trials) and averaged over rats; overshoot = maximum over trials 0 to 20 minus the value at trial 20 (Fig. 4d legend; Figure4.m). For Fig. 4e, the overshoot per chunk of 5 sessions is shown beside the wait time ratio.

#%% code claim:fig4d-overshoot-grows-with-training
def overshoot_curve(df):
    df = df.copy()
    df["iti"], df["z_iti"] = prep_iti(df)
    df["dt"] = M.detrend_iti(df, df.z_iti, per_session=False)
    tr = M.transitions(df)
    c = M.transition_curves(df, df.dt, tr)
    h = c[(2, 1)].mean()
    return float(h.loc[0:20].max() - h.loc[20]), h

nmax = Z.groupby("subject").sess_in_rat.transform("max")
early = Z[Z.sess_in_rat < 10].reset_index(drop=True)
late = Z[Z.sess_in_rat > nmax - 10].reset_index(drop=True)
oe, he = overshoot_curve(early)
ol, hl_ = overshoot_curve(late)
print(f"overshoot first 10 sessions {oe:.4f}, last 10 sessions {ol:.4f}; larger late: {ol > oe}")
print("high->mixed curve, early, trials 0..20:", he.loc[0:20].round(3).to_list())
print("high->mixed curve, late, trials 0..20:", hl_.loc[0:20].round(3).to_list())
R["fig4d"] = (oe, ol)
Zc = Z.copy(); Zc["chunk"] = Zc.sess_in_rat // 5
ch = {}
for k, g in Zc[Zc.chunk < 20].groupby("chunk"):
    ch[k] = overshoot_curve(g.reset_index(drop=True))[0]
ch = pd.Series(ch)
print("overshoot per 5-session chunk (first 100 sessions):", ch.round(3).to_list())
print("10-point moving average:", ch.rolling(10, min_periods=1).mean().round(3).to_list())
EOF
cd $TMPDIR && sed -i 's#^        if "load" in head.split():#        if "zload" in head.split():\n            body = ("Z0=pd.read_parquet(\x27/tmp/claude-1001/zall.parquet\x27)\\n")\n        if "load" in head.split():#' nb/dev.py && python3 - <<'EOF'
# dev: make the zenodo load cell read the cache
s=open('/tmp/claude-1001/nb/dev.py').read()
s=s.replace('''        t = time.time()''','''        body = body.replace("zz = M.zenodo_zip()\\nz_rats, z_sex = M.zenodo_rat_list(zz)\\nZ = M.load_zenodo_astructs(zz, z_rats)", "Z = pd.read_parquet('/tmp/claude-1001/zall.parquet'); z_rats = sorted(Z.subject.unique())")
        t = time.time()''')
open('/tmp/claude-1001/nb/dev.py','w').write(s)
EOF
. dev/bin/activate && python nb/dev.py nb/c1.py nb/c7.py 2>&1 | grep -v "^---" | grep -v Warn | sed -n '/loaded .* trials of/,$p'
```

```
loaded 13433378 trials of 291 rats in 1 s; trainingstage counts: {9.0: 13111937, 1.0: 111272, 8.0: 63728, 7.0: 48984, 3.0: 33123, 6.0: 22322, 4.0: 21080, 5.0: 20841, 2.0: 91}
rats in the deposit's ratList that are in the dandiset: 291 of 291
Traceback (most recent call last):
  File "/tmp/claude-1001/nb/dev.py", line 20, in <module>
    exec(compile(body, f, "exec"), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "nb/c7.py", line 10, in <module>
    Z = M.load_zenodo_astructs(zz, z_rats)
                 ^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/generic.py", line 6781, in astype
    new_data = self._mgr.astype(dtype=dtype, errors=errors)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/internals/managers.py", line 632, in astype
    return self.apply("astype", dtype=dtype, errors=errors)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/internals/managers.py", line 456, in apply
    applied = getattr(b, f)(**kwargs)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/internals/blocks.py", line 623, in astype
    new_values = astype_array_safe(values, dtype, errors=errors)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/dtypes/astype.py", line 245, in astype_array_safe
    new_values = astype_array(values, dtype, copy=copy)
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('c7.py').read()
s=s.replace('''Z = Z[Z.trainingstage == 9].copy()''','''Z = Z[Z.trainingstage == 9].copy()
bad = Z.reward.isna() | Z.block.isna() | ~Z.reward.round().isin(list(M.VOL_MAP))
print("final-stage trials without a reward, block, or with an offer outside the ten volumes (dropped):", int(bad.sum()))
Z = Z[~bad].copy()''')
open('c7.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c7.py 2>&1 | grep -v "^---" | grep -v Warn | sed -n '/loaded .* trials of/,$p'
```

```
loaded 13433378 trials of 291 rats in 1 s; trainingstage counts: {9.0: 13111937, 1.0: 111272, 8.0: 63728, 7.0: 48984, 3.0: 33123, 6.0: 22322, 4.0: 21080, 5.0: 20841, 2.0: 91}
rats in the deposit's ratList that are in the dandiset: 291 of 291
final-stage trials without a reward, block, or with an offer outside the ten volumes (dropped): 5
final-stage sessions per rat: deposit median 95 (range 18-264), dandiset median 71; rats with more sessions in the deposit than the dandiset: 269, fewer: 22
final-stage trials: deposit 13111932, dandiset 10408699
rats with a ratio in pair 1: wait 244 initiation 273
mean wait time ratio by pair: [1.187, 1.141, 1.038, 1.0, 1.007, 0.997, 1.12, 1.016, 0.971, 1.023, 0.998, 1.057, 0.95, 0.939, 1.017, 0.942, 0.939, 0.92, 0.99, 0.936, 0.907, 0.925, 0.912, 0.918, 0.915]
mean initiation ratio by pair: [0.802, 0.745, 0.685, 0.631, 0.677, 0.661, 0.617, 0.684, 0.648, 0.647, 0.629, 0.64, 0.583, 0.65, 0.646, 0.602, 0.625, 0.618, 0.61, 0.609, 0.738, 0.601, 0.625, 0.632, 0.671]
(1) first pair initiation ratio: mean 0.802, n 273, signed-rank against 1 p = 5.77e-16
(2) wait time ratio first pair 1.187 (|1 - r| = 0.187); mean over pairs 16-25 0.936 (|1 - r| = 0.064)
(3) block coefficient (log2 reward): sessions 1-10 -0.4315, sessions 41-50 -0.7057; grows in size: True
(3) block coefficient (linear reward): sessions 1-10 -0.3930, sessions 41-50 -0.6325; grows in size: True
plotted ranges: wait ratio 0.907 - 1.187 | initiation ratio 0.583 - 0.802
previous reward coefficient: sessions 1-10 -0.5876, 41-50 -0.4693; same sign: True; relative change 0.252
wait time block coefficient relative change 0.389; initiation change smaller: True
rats with a coefficient in session 1: 216 and session 50: 216
overshoot first 10 sessions 0.0250, last 10 sessions 0.0464; larger late: True
high->mixed curve, early, trials 0..20: [-0.042, -0.027, -0.014, -0.002, 0.016, 0.035, 0.051, 0.061, 0.065, 0.067, 0.069, 0.066, 0.065, 0.062, 0.054, 0.05, 0.05, 0.048, 0.046, 0.044, 0.04
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Tue Nov 24 23:12:22 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && for f in GenerateSynthData_AlphaPHModel.m GenerateSynthData_Bayes_BeliefState.m GenerateSynthData_Bayes_subopt_onlylambda_flat.m; do curl -sf -o $f https://raw.githubusercontent.com/constantinoplelab/published/b7b68ca8c107/rat_behavior/BehavioralModel/WaitTimeModels/$f; done; grep -v "^\s*%" GenerateSynthData_AlphaPHModel.m | grep -v "^\s*$" | head -60; grep -v "^\s*%" GenerateSynthData_Bayes_subopt_onlylambda_flat.m | grep -v "^\s*$" | sed -n 1,40p
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q numba 2>&1 | tail -1; python -c "import numba;print(numba.__version__)"; cd code && for f in GenerateLatencyData_VanillaAlpha.m GenerateLatencyData_RPEAlpha.m; do curl -sf -o $f https://raw.githubusercontent.com/constantinoplelab/published/b7b68ca8c107/rat_behavior/BehavioralModel/TrialInitiationTimeModels/$f; done; grep -v "^\s*%" GenerateLatencyData_RPEAlpha.m | grep -v "^\s*$" | sed -n 1,50p | grep -n "alpha\|kappa\|rpe\|D =\|belief(:,rr) =" ; grep -n "alpha\|kappa(" GenerateLatencyData_VanillaAlpha.m | head; grep -n "GenerateLatency\|noise\|smooth\|0.1042\|0.2527\|logn" $TMPDIR/code/Figures/Figure3.m | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 1,40p GenerateLatencyData_RPEAlpha.m | grep -v "^\s*%"; sed -n 30,60p GenerateLatencyData_VanillaAlpha.m | grep -v "^\s*%"; sed -n 195,230p Figures/Figure3.m
```

```
function [LatOpt, LatMdl, RPE, Kappa] =...
    GenerateLatencyData_RPEAlpha(params, ratTrial,...
    gen_arg, noise_arg, noise_params)

alpha0 = params(1);
D = params(2)*15;


isgood = ~isnan(ratTrial.ITI);

rew = ratTrial.reward(isgood);
rew = log2(rew);

newday = nan(1, length(ratTrial.ITI));
ntrials = [0; cumsum(ratTrial.ntrials)];

for ii = 1:length(ntrials)-1
    newday(ntrials(ii)+1:ntrials(ii+1)) = ii;
end

[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "rew\b\|rew =\|isgood =\|D =" GenerateLatencyData_VanillaAlpha.m | head; grep -n "isgood =\|rew_vol = \|D = \|eps\|kappa(kappa" GenerateLatencyData_RPEAlpha.m GenerateLatencyData_AlphaPHModel.m
```

```
15:D = params(2)*10;
21:isgood = ~isnan(ratTrial.ITI);
25:rew = ratTrial.reward(isgood);
26:rew = log2(rew);
41:kappa = nan(length(rew), 1);
42:rpe = nan(length(rew), 1);
47:for rr = 1:length(rew)-1
53:    rpe(rr) = rew(rr) - kappa(rr);
GenerateLatencyData_RPEAlpha.m:15:D = params(2)*15;
GenerateLatencyData_RPEAlpha.m:21:isgood = ~isnan(ratTrial.ITI);
GenerateLatencyData_AlphaPHModel.m:10:D = params(2)*25; % scale parameter
GenerateLatencyData_AlphaPHModel.m:29:isgood = ~isnan(ratTrial.wait_time);
GenerateLatencyData_AlphaPHModel.m:33:rew_vol = ratTrial.reward(isgood);
GenerateLatencyData_AlphaPHModel.m:36:rew_vol = log2(rew_vol);
GenerateLatencyData_AlphaPHModel.m:87:kappa(kappa<0) = eps;
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/mah-2023/mah2023.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Wait time models (Methods, Behavioral models; the generative code in BehavioralModel/ of the
# paper's repository at b7b68ca8c107: GenerateSynthData_Bayes.m, _Bayes_BeliefState.m,
# _AlphaPHModel.m, _Bayes_subopt_onlylambda_flat.m; GenerateLatencyData_*.m). The fitting code
# is not public; what it would fix (bounds, starts, folds) is stated where it is chosen.
# ---------------------------------------------------------------------------------------------

from numba import njit

TAU_DELAY = 2.5  # tau of the exponential delay distribution (Methods, Equation 1)
NOISE_WT = 8.0  # variance of the log-normal noise of the wait time model (Methods)


@njit(cache=True)
def belief_filter(vidx, newsess, lam, reset):
    """Posterior and prior over (mixed, high, low) with H0 = 1/40, as in the generative code:
    at the first model trial of each session the belief is set to `reset` (prior NaN); otherwise
    prior = lam * P(B_t | B_t-1) belief + (1 - lam) / 3, posterior = likelihood * prior."""
    h0 = 1.0 / 40
    pb = np.array([[1 - h0, h0, h0], [h0 / 2, 1 - h0, 0.0], [h0 / 2, 0.0, 1 - h0]])
    prew = np.array([[0.2, 0.2, 0.2, 0.2, 0.2], [0.0, 0.0, 1 / 3, 1 / 3, 1 / 3],
                     [1 / 3, 1 / 3, 1 / 3, 0.0, 0.0]])
    n = len(vidx)
    post = np.empty((n, 3))
    prior = np.full((n, 3), np.nan)
    b = reset.copy()
    for i in range(n):
        if newsess[i]:
            b = reset.copy()
        else:
            pr = pb @ b
            pr = lam * pr + (1 - lam) / 3.0
            for k in range(3):
                prior[i, k] = pr[k]
            b = prew[:, vidx[i]] * pr
            b = b / b.sum()
        for k in range(3):
            post[i, k] = b[k]
    return post, prior


@njit(cache=True)
def retro_kappa(r, newsess, gain, alpha0, mode, k0):
    """kappa_{t+1} = kappa_t + alpha_t (r_t - kappa_t) (Equation 9), reset to k0 at each session.
    mode 0: alpha_t = min(alpha0 * gain_t, 1) (Equation 10; alpha0 at the session's first trial);
    mode 1: alpha_t = alpha0 (G = 1); mode 2: alpha_t = min(alpha0 |delta_t|, 1) (G = |delta|)."""
    n = len(r)
    kap = np.empty(n)
    k = k0
    for i in range(n):
        if newsess[i]:
            k = k0
        kap[i] = k
        d = r[i] - k
        if mode == 0:
            a = alpha0 if newsess[i] else min(alpha0 * gain[i], 1.0)
        elif mode == 1:
            a = alpha0
        else:
            a = min(alpha0 * abs(d), 1.0)
        k = k + a * d
    return kap


def lognormal_nll(wt, m, var=NOISE_WT):
    """-sum log density of wt under a log-normal with mean m and variance var (generate_wts.m)."""
    m = np.maximum(m, 1e-12)
    s2 = np.log(var / m ** 2 + 1)
    mu = np.log(m) - s2 / 2
    lw = np.log(np.maximum(wt, 1e-6))
    return float(np.sum(lw + 0.5 * np.log(2 * np.pi * s2) + (lw - mu) ** 2 / (2 * s2)))


class RatModel:
    """One rat's model trials: the trials with a wait time (hits and opt-outs; isgood in the
    generative code), in session order."""

    def __init__(self, g):
        good = g["wait_time"].notna().to_numpy()
        h = g.loc[good]
        self.vidx = h["vol"].map({5: 0, 10: 1, 20: 2, 40: 3, 80: 4}).to_numpy().astype(np.int64)
        self.rlog = np.log2(h["reward_volume_ul"].to_numpy().astype(float))
        s = h["sess"].to_numpy()
        self.sess = s
        self.newsess = np.r_[True, s[1:] != s[:-1]]
        self.C = float((1 - g["catch_percentage"]).max())
        self.minr = float(np.log2(g["reward_volume_ul"].min()))
        self.fit = (h["is_catch"] & h["is_opt_out"]).to_numpy()
        self.wt = h["wait_time"].to_numpy()
        self.block = h["block"].to_numpy()
        self.vol = h["vol"].to_numpy()
        self.index = h.index.to_numpy()
        self.post, self.prior = belief_filter(self.vidx, self.newsess, 1.0, np.array([0.5, 0.25, 0.25]))
        self.blk_inf = np.argmax(self.post, 1)  # 0 mixed, 1 high, 2 low
        dm = np.abs(np.diff(self.post[:, 0], prepend=np.nan))
        self.gain = np.where(self.newsess, 1.0, 1.0 / (1 - np.nan_to_num(dm)))

    def wt_opt(self, model, p):
        C, tau, R = self.C, TAU_DELAY, self.rlog
        if model in ("inferential", "belief", "lambda"):
            kv = np.array(p[:3]) * C * self.minr / tau  # (mixed, high, low)
            D = 10 * p[3]
            if model == "inferential":
                kap = kv[self.blk_inf]
            elif model == "belief":
                kap = self.post @ kv
            else:
                post, _ = belief_filter(self.vidx, self.newsess, p[4], np.array([1 / 3, 1 / 3, 1 / 3]))
                kap = kv[np.argmax(post, 1)]
        else:  # retrospective (GenerateSynthData_AlphaPHModel.m)
            D = 15 * p[1]
            kap = retro_kappa(R, self.newsess, self.gain, p[0], 0, np.mean(np.log([5, 10, 20, 40, 80])))
            kap = kap / kap.max() * (self.minr * C / tau)
            kap = np.where(kap < 0, 1e-16, kap)
        with np.errstate(all="ignore"):
            arg = (R - kap * tau) / (kap * tau) * C / (1 - C)
            w = D * tau * np.log(arg)
        return np.where(np.isfinite(w) & (w > 0), w, 1e-12)

    def nll(self, model, p, mask):
        w = self.wt_opt(model, p)
        m = self.fit & mask
        return lognormal_nll(self.wt[m], w[m])


MODELS = {  # free parameters and their bounds (bounds are this attempt's choice; see the notebook)
    "inferential": ["k_mixed", "k_high", "k_low", "D"],
    "belief": ["k_mixed", "k_high", "k_low", "D"],
    "retrospective": ["alpha0", "D"],
    "lambda": ["k_mixed", "k_high", "k_low", "D", "lambda"],
}


def bounds_for(model, C):
    kb = (0.01, min(0.999 / C, 5.0))
    return {"inferential": [kb, kb, kb, (0.01, 10)], "belief": [kb, kb, kb, (0.01, 10)],
            "retrospective": [(0.001, 1.0), (0.01, 10)],
            "lambda": [kb, kb, kb, (0.01, 10), (0.0, 1.0)]}[model]


def fit_model(rm, model, mask, rng, nstarts):
    from scipy.optimize import minimize
    bnds = bounds_for(model, rm.C)
    best = None
    for _ in range(nstarts):
        p0 = np.array([rng.uniform(lo, hi) for lo, hi in bnds])
        r = minimize(lambda p: rm.nll(model, p, mask), p0, method="L-BFGS-B", bounds=bnds)
        if best is None or r.fun < best.fun:
            best = r
    return best.x, best.fun


def cv_fit(rm, model, rng, nstarts=3, nfold=5):
    """5-fold cross-validation over sessions (folds drawn at random from rng). For each fold the
    model is fitted on the other four and evaluated on it; the parameters of the fold with the
    lowest test nLL are kept (Zenodo README, BestFit final_params) and evaluated on all data.
    Returns dict with params, nll_all, cv_nll (summed test nLL over folds), best_fold_test_nll,
    k and n (trials fitted)."""
    us = np.unique(rm.sess)
    fold_of = dict(zip(us, rng.permutation(len(us)) % nfold))
    f = np.array([fold_of[s] for s in rm.sess])
    tests, params = [], []
    for k in range(nfold):
        p, _ = fit_model(rm, model, f != k, rng, nstarts)
        params.append(p)
        tests.append(rm.nll(model, p, f == k))
    kbest = int(np.argmin(tests))
    p = params[kbest]
    all_ = rm.nll(model, p, np.ones(len(f), bool))
    return dict(params=p, nll_all=all_, cv_nll=float(np.sum(tests)), best_fold_test_nll=tests[kbest],
                k=len(p), n=int(rm.fit.sum()))
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys,time; sys.path.insert(0,'entries/mah-2023')
import pandas as pd, numpy as np
import mah2023 as M
T=pd.read_parquet('trials.parquet'); 
for r in ['E006','M041','J037']:
    g=T[T.subject==r]
    t=time.time(); rm=M.RatModel(g); print('prep',time.time()-t, len(rm.vidx), rm.fit.sum(), rm.C, rm.minr)
    rng=np.random.default_rng(0)
    for model in ['inferential','belief','retrospective','lambda']:
        t=time.time(); res=M.cv_fit(rm, model, rng, nstarts=3); print(r, model, round(time.time()-t,2), np.round(res['params'],3), round(res['nll_all'],1), round(res['cv_nll'],1))
EOF
```

```
prep 1.7364122867584229 4504 1377 0.85 2.0
E006 inferential 0.81 [0.01  0.02  0.022 0.041] 4644.3 4739.3
E006 belief 0.61 [0.01  0.019 0.011 0.04 ] 4643.6 4701.1
E006 retrospective 0.52 [0.058 0.07 ] 4849.5 4899.6
E006 lambda 7.68 [0.01  0.011 0.016 0.04  0.989] 4640.6 4685.4
prep 0.02294445037841797 30369 3980 0.85 2.321928094887362
M041 inferential 1.48 [0.285 0.397 0.165 0.119] 12358.6 12595.2
M041 belief 1.55 [0.344 0.483 0.19  0.126] 12326.6 12558.6
M041 retrospective 0.92 [0.049 0.112] 12940.8 13141.2
M041 lambda 41.04 [0.39  0.531 0.266 0.132 0.821] 12362.9 12857.0
prep 0.016746044158935547 24069 3480 0.85 2.321928094887362
J037 inferential 1.2 [0.516 0.519 0.474 0.148] 12104.7 12138.9
J037 belief 1.24 [0.464 0.516 0.462 0.142] 12096.4 12123.5
J037 retrospective 1.22 [0.063 0.113] 12321.3 12347.4
J037 lambda 37.19 [0.595 0.689 0.542 0.159 0.678] 12094.4 12179.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/mah-2023 && python3 - <<'EOF'
s=open('mah2023.py').read()
a=s.index('    def wt_opt(self, model, p):'); b=s.index('MODELS = {')
s=s[:a]+'''    def wt_opt(self, model, p, only_fit=True):
        """Optimal wait time (Equation 1) on the fitted trials (or all model trials)."""
        C, tau = self.C, TAU_DELAY
        sel = self.fit if only_fit else np.ones(len(self.fit), bool)
        R = self.rlog[sel]
        if model in ("inferential", "belief", "lambda"):
            kv = np.array(p[:3]) * C * self.minr / tau  # (mixed, high, low)
            D = 10 * p[3]
            if model == "inferential":
                kap = kv[self.blk_inf[sel]]
            elif model == "belief":
                kap = self.post[sel] @ kv
            else:
                post, _ = belief_filter(self.vidx, self.newsess, p[4], np.array([1 / 3, 1 / 3, 1 / 3]))
                kap = kv[np.argmax(post, 1)[sel]]
        else:  # retrospective (GenerateSynthData_AlphaPHModel.m)
            D = 15 * p[1]
            kap = retro_kappa(self.rlog, self.newsess, self.gain, p[0], 0, np.mean(np.log([5, 10, 20, 40, 80])))
            kap = (kap / kap.max() * (self.minr * C / tau))[sel]
            kap = np.where(kap < 0, 1e-16, kap)
        with np.errstate(all="ignore"):
            arg = (R - kap * tau) / (kap * tau) * C / (1 - C)
            w = D * tau * np.log(arg)
        return np.where(np.isfinite(w) & (w > 0), w, 1e-12)

    def nll(self, model, p, mask):
        """mask: over the fitted trials"""
        w = self.wt_opt(model, p)
        return lognormal_nll(self.wt[self.fit][mask], w[mask])


'''+s[b:]
s=s.replace('''    us = np.unique(rm.sess)
    fold_of = dict(zip(us, rng.permutation(len(us)) % nfold))
    f = np.array([fold_of[s] for s in rm.sess])''','''    us = np.unique(rm.sess)
    fold_of = dict(zip(us, rng.permutation(len(us)) % nfold))
    f = np.array([fold_of[s] for s in rm.sess[rm.fit]])''')
s+='''

_T = None  # trials table shared with forked workers


def _fit_rat(args):
    rat, models, seed, nstarts = args
    g = _T[_T["subject"] == rat]
    rm = RatModel(g)
    out = {}
    for j, m in enumerate(models):
        out[m] = cv_fit(rm, m, np.random.default_rng(seed + j), nstarts=nstarts)
    return rat, out


def fit_all(trials, rats, models, seed, nstarts=3, procs=4):
    """Fit `models` to every rat in parallel processes (fork). The generator of each rat and model
    is seeded from `seed` (the claim's seed) plus the rat's position times 10 and the model's."""
    import multiprocessing as mp
    global _T
    _T = trials
    args = [(r, models, seed + 10 * i, nstarts) for i, r in enumerate(rats)]
    with mp.get_context("fork").Pool(procs) as pool:
        res = dict(pool.map(_fit_rat, args, chunksize=4))
    return res
'''
open('mah2023.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys,time; sys.path.insert(0,'entries/mah-2023')
import pandas as pd, numpy as np
import mah2023 as M
T=pd.read_parquet('trials.parquet', columns=['subject','sess','wait_time','vol','reward_volume_ul','catch_percentage','is_catch','is_opt_out','block'])
T['vol']=T.reward_volume_ul.map(M.VOL_MAP)
rats=sorted(T.subject.unique())[:16]
t=time.time(); res=M.fit_all(T, rats, ['inferential','belief','retrospective'], 123, nstarts=3, procs=4); print('16 rats', time.time()-t)
for r in rats[:4]: print(r, {m:(round(v['nll_all'],1), round(v['cv_nll'],1)) for m,v in res[r].items()})
t=time.time(); res=M.fit_all(T, rats[:8], ['lambda'], 123, nstarts=1, procs=4); print('8 rats lambda', time.time()-t)
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
16 rats 89.14938855171204
C015 {'inferential': (2432.9, 2467.8), 'belief': (2442.5, 2475.3), 'retrospective': (2523.6, 2541.6)}
C033 {'inferential': (14718.8, 15138.0), 'belief': (14696.9, 15015.3), 'retrospective': (15093.1, 15145.5)}
C034 {'inferential': (6451.1, 7714.6), 'belief': (6443.3, 6564.9), 'retrospective': (6569.4, 6677.0)}
C035 {'inferential': (12181.0, 12403.2), 'belief': (12189.6, 12332.9), 'retrospective': (12626.7, 12819.5)}
8 rats lambda 47.65805268287659
1.68306
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys,time; sys.path.insert(0,'entries/mah-2023')
import pandas as pd, numpy as np
import mah2023 as M
T=pd.read_parquet('trials.parquet', columns=['subject','sess','wait_time','vol','reward_volume_ul','catch_percentage','is_catch','is_opt_out','block'])
T['vol']=T.reward_volume_ul.map(M.VOL_MAP)
rats=sorted(T.subject.unique())[100:132]
t=time.time(); res=M.fit_all(T, rats, ['inferential','belief','retrospective'], 123, nstarts=2, procs=4); print('32 rats', time.time()-t)
import cProfile, pstats
g=T[T.subject==rats[0]]; rm=M.RatModel(g)
cProfile.run("M.cv_fit(rm,'retrospective',np.random.default_rng(1),nstarts=2)", '/tmp/claude-1001/prof')
pstats.Stats('/tmp/claude-1001/prof').sort_stats('cumtime').print_stats(8)
EOF
```

```
32 rats 107.79449081420898
Tue Nov 24 23:20:53 2026    /tmp/claude-1001/prof

         500721 function calls (491128 primitive calls) in 0.643 seconds

   Ordered by: cumulative time
   List reduced from 1260 to 8 due to restriction <8>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    211/1    0.004    0.000    0.644    0.644 {built-in method builtins.exec}
        1    0.000    0.000    0.644    0.644 <string>:1(<module>)
        1    0.000    0.000    0.643    0.643 entries/mah-2023/mah2023.py:556(cv_fit)
        5    0.000    0.000    0.641    0.128 entries/mah-2023/mah2023.py:544(fit_model)
       10    0.000    0.000    0.345    0.034 /tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/optimize/_minimize.py:54(minimize)
       10    0.003    0.000    0.341    0.034 /tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/optimize/_lbfgsb_py.py:272(_minimize_lbfgsb)
    254/5    0.001    0.000    0.296    0.059 <frozen importlib._bootstrap>:1358(_find_and_load)
    243/1    0.001    0.000    0.296    0.296 <frozen importlib._bootstrap>:1306(_find_and_load_unlocked)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/mah-2023 && python3 - <<'EOF'
s=open('mah2023.py').read()
s=s.replace('''    rat, models, seed, nstarts = args
    g = _T[_T["subject"] == rat]
    rm = RatModel(g)''','''    rat, models, seed, nstarts = args
    rm = RatModel(_T[rat])''')
s=s.replace('''    global _T
    _T = trials
''','''    global _T
    cols = ["subject", "sess", "wait_time", "vol", "reward_volume_ul", "catch_percentage",
            "is_catch", "is_opt_out", "block"]
    _T = {r: g for r, g in trials[cols].groupby("subject") if r in set(rats)}
''')
open('mah2023.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python - <<'EOF'
import sys,time; sys.path.insert(0,'entries/mah-2023')
import pandas as pd, numpy as np
import mah2023 as M
T=pd.read_parquet('trials.parquet', columns=['subject','sess','wait_time','vol','reward_volume_ul','catch_percentage','is_catch','is_opt_out','block'])
T['vol']=T.reward_volume_ul.map(M.VOL_MAP)
rats=sorted(T.subject.unique())[100:132]
t=time.time(); res=M.fit_all(T, rats, ['inferential','belief','retrospective'], 123, nstarts=2, procs=4); print('32 rats', time.time()-t)
t=time.time(); res=M.fit_all(T, rats[:8], ['lambda'], 123, nstarts=1, procs=4); print('8 rats lambda', time.time()-t)
EOF
```

```
32 rats 23.266620635986328
8 rats lambda 53.10749101638794
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/c8.py <<'EOF'
#%% md
## Model fits (fig3j, suppfig8, fig3f, suppfig9)

The paper's fitting code is not public. The models are written from the Methods (Equations 1 and 3 to 10) and the generative functions in the paper's repository (BehavioralModel/WaitTimeModels at b7b68ca8c107): kappa_block = k_block C log2(min offer) / tau, D = 10 p (inferential and belief state), D = 15 p and kappa normalised to its maximum (retrospective, GenerateSynthData_AlphaPHModel.m), tau = 2.5 s, C = 1 - lowest catch probability, offers as log2 of the deposited volume, the model run over the trials with a wait time (hits and opt-outs) and reset at each session. The likelihood is that of a log-normal with mean the model's wait time and variance 8 (Methods; generate_wts.m), over the opt-out catch trials. Choices this attempt makes, where the paper is silent (assumptions, see the record): bounds k in [0.01, min(0.999/C, 5)], D-scale in [0.01, 10], alpha0 in [0.001, 1]; L-BFGS-B from 2 random starts (the paper used fmincon from 100); 5 folds over sessions drawn at random; the parameters of the fold with the lowest test nLL kept (Zenodo README: final_params from the best fold), BIC and AIC from the nLL on all data (Methods). Cross-validated nLL is the summed test nLL over folds (the README's best-fold test nLL is shown as a variant). Seeds: the claim's (fig3j) and +1000 to +4000.

#%% code
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
MODEL_RATS = list(rats)
TM = time.time()
FITS = {}
for off in [0, 1000, 2000, 3000, 4000]:
    FITS[off] = M.fit_all(t, MODEL_RATS, ["inferential", "belief", "retrospective"],
                          zlib.crc32(b"mah-2023/fig3j-inferential-beats-retrospective-for-wait-times") + off, nstarts=2)
    print(f"seed +{off}: fitted {len(FITS[off])} rats, {time.time()-TM:.0f} s so far")

def metric_table(F):
    rows = []
    for r, d in F.items():
        for m, v in d.items():
            rows.append(dict(rat=r, model=m, nll=v["nll_all"], k=v["k"], n=v["n"], cv=v["cv_nll"], cvbest=v["best_fold_test_nll"]))
    df = pd.DataFrame(rows)
    df["BIC"] = np.log(df.n) * df.k + 2 * df.nll
    df["AIC"] = 2 * df.k + 2 * df.nll
    return df.pivot(index="rat", columns="model")

MT = {off: metric_table(F) for off, F in FITS.items()}
P = pd.DataFrame({r: FITS[0][r]["inferential"]["params"] for r in FITS[0]}, index=["k_mixed", "k_high", "k_low", "D"]).T
print("inferential parameters (claim's seed), median:", P.median().round(3).to_dict(), "| at a bound:",
      {c: int(((P[c] <= 0.0101) | (P[c] >= 4.99)).sum()) for c in P})
print("rats whose fitted k_high > k_low (higher opportunity cost in high blocks):", int((P.k_high > P.k_low).sum()), "of", len(P))

#%% md
## fig3j-inferential-beats-retrospective-for-wait-times

> Wait times are better fit by the inferential model, which uses hidden state inference to choose a block-specific value of the environment, than by the retrospective model, by BIC, AIC and cross-validated negative log-likelihood.

#%% code claim:fig3j-inferential-beats-retrospective-for-wait-times
for off, mt in MT.items():
    out = []
    for met in ["BIC", "AIC", "cv", "cvbest"]:
        d = mt[met]["inferential"] - mt[met]["retrospective"]
        p = stats.wilcoxon(d).pvalue
        out.append(f"{met}: mean diff {d.mean():+.1f}, rats inferential better {int((d < 0).sum())}/{len(d)}, p = {p:.3g}")
        R.setdefault("fig3j", {})[(off, met)] = (d.mean(), int((d < 0).sum()), p)
    print(f"seed +{off}: " + " | ".join(out))

#%% md
**Result: see the summary.**

#%% md
## suppfig8-belief-state-not-distinguished

> Model comparison does not distinguish the inferential model from the belief state model for wait times.

A claim of absence: reproduced when none of the three signed-rank tests (BIC, AIC, cross-validated nLL) reaches p < 0.05.

#%% code claim:suppfig8-belief-state-not-distinguished
for off, mt in MT.items():
    out = []
    for met in ["BIC", "AIC", "cv", "cvbest"]:
        d = mt[met]["inferential"] - mt[met]["belief"]
        p = stats.wilcoxon(d).pvalue
        out.append(f"{met}: mean diff {d.mean():+.2f}, rats inferential better {int((d < 0).sum())}/{len(d)}, p = {p:.3g}")
        R.setdefault("suppfig8", {})[(off, met)] = (d.mean(), int((d < 0).sum()), p)
    print(f"seed +{off}: " + " | ".join(out))

#%% md
**Result: see the summary.**

#%% md
## fig3f-inferential-model-not-sensitive-to-previous-offer

> Wait times predicted by the inferential model fitted to each rat are, like the rats' wait times, not sensitive to the previous offer for 20 uL in mixed blocks.

Each rat's fitted inferential model (claim's seed) gives a wait time for every model trial; a log-normal draw with that mean and variance 8 (WTMdl, generate_wts.m) replaces the rat's wait time on its opt-out catch trials, and the analysis of fig2j is run on it (Figure3.m). Draws from the claim's generator; seeds +1000 to +4000 shown.

#%% code claim:fig3f-inferential-model-not-sensitive-to-previous-offer
def model_wait_times(F, rng):
    out = pd.Series(np.nan, index=t.index)
    for r in MODEL_RATS:
        rm = M.RatModel(t[t.subject == r])
        w = rm.wt_opt("inferential", F[r]["inferential"]["params"], only_fit=False)
        s2 = np.log(M.NOISE_WT / w ** 2 + 1)
        draw = np.exp(rng.normal(np.log(w) - s2 / 2, np.sqrt(s2)))
        out.loc[rm.index[rm.fit]] = draw[rm.fit]
    return out

def fig2j_test(wcol):
    sel = (t.vol == 20) & (t.block == 1) & wcol.notna() & t.prev_vol.notna()
    w = t.loc[sel, ["subject", "prev_vol"]].assign(v=wcol[sel])
    w["zz"] = w.groupby("subject").v.transform(lambda x: (x - x.mean()) / x.std())
    m = pd.DataFrame({"below": w[w.prev_vol < 20].groupby("subject").zz.mean(), "above": w[w.prev_vol > 20].groupby("subject").zz.mean()})
    return M.ranksum_p(m.below, m.above), (m.below - m.above).mean(), stats.wilcoxon(m.below, m.above).pvalue

for off in [0, 1000, 2000, 3000, 4000]:
    mw_ = model_wait_times(FITS[0], rng_for("fig3f-inferential-model-not-sensitive-to-previous-offer", offset=off))
    p, sens, psr = fig2j_test(mw_)
    print(f"draw seed +{off}: model sensitivity (below minus above) {sens:+.4f}; rank-sum p = {p:.3g}; signed-rank p = {psr:.3g}")
    R.setdefault("fig3f", {})[off] = (p, sens)
print(f"rats (fig2j): sensitivity {R['fig2j'][3]:+.4f}, rank-sum p = {R['fig2j'][1]:.3g}")

#%% md
**Result: see the summary.**

#%% md
## suppfig9-wait-times-reflect-misinferences

> Within mixed blocks, wait times for 20 uL differ between trials the inferential model labels as high and as low blocks, so wait times reflect mistaken inferences.

The inferential model's block labels (most likely block, Equations 3 to 6) depend on no fitted parameter (H0 is fixed), so the labels of held-out test trials are those of the full run. Per rat, mean wait time on 20 uL opt-out catch trials in mixed blocks labelled high and labelled low; signed-rank across rats.

#%% code claim:suppfig9-wait-times-reflect-misinferences
lab = pd.Series(np.nan, index=t.index)
for r in rats:
    rm = M.RatModel(t[t.subject == r])
    lab.loc[rm.index] = rm.blk_inf
sel = (t.block == 1) & (t.vol == 20) & t.wt.notna()
d = t.loc[sel, ["subject", "wt"]].assign(lab=lab[sel])
mm = d.groupby(["subject", "lab"]).wt.mean().unstack().rename(columns={0: "mixed", 1: "high", 2: "low"})
both = mm[["high", "low"]].dropna()
p = stats.wilcoxon(both.high, both.low).pvalue
print("mixed-block 20 uL catch trials by label:", d.lab.value_counts().rename({0: "mixed", 1: "high", 2: "low"}).to_dict())
print(f"rats with both labels: {len(both)}; mean wait labelled high {both.high.mean():.3f} s, labelled low {both.low.mean():.3f} s; "
      f"rats shorter when labelled high {int((both.high < both.low).sum())}; signed-rank p = {p:.3g}")
R["suppfig9"] = (both.high.mean(), both.low.mean(), p, len(both))
EOF
cd $TMPDIR && sed -i 's/^MODEL_RATS = list(rats)$/MODEL_RATS = list(rats)[:24]/' nb/c8.py && . dev/bin/activate && OMP_NUM_THREADS=1 python nb/dev.py nb/c1.py nb/c5.py nb/c8.py 2>&1 | grep -v Warn | sed -n '/seed +0: fitted/,$p'
```

```
seed +0: fitted 24 rats, 21 s so far
seed +1000: fitted 24 rats, 42 s so far
seed +2000: fitted 24 rats, 63 s so far
seed +3000: fitted 24 rats, 84 s so far
seed +4000: fitted 24 rats, 105 s so far
inferential parameters (claim's seed), median: {'k_mixed': 0.134, 'k_high': 0.155, 'k_low': 0.16, 'D': 0.089} | at a bound: {'k_mixed': 1, 'k_high': 1, 'k_low': 1, 'D': 1}
rats whose fitted k_high > k_low (higher opportunity cost in high blocks): 17 of 24
--- [code] 105.5s
seed +0: BIC: mean diff -994.0, rats inferential better 24/24, p = 1.19e-07 | AIC: mean diff -1006.1, rats inferential better 24/24, p = 1.19e-07 | cv: mean diff -438.4, rats inferential better 23/24, p = 3.66e-05 | cvbest: mean diff -60.9, rats inferential better 15/24, p = 0.152
seed +1000: BIC: mean diff -967.6, rats inferential better 24/24, p = 1.19e-07 | AIC: mean diff -979.6, rats inferential better 24/24, p = 1.19e-07 | cv: mean diff -435.7, rats inferential better 23/24, p = 7.63e-05 | cvbest: mean diff -1.1, rats inferential better 10/24, p = 0.79
seed +2000: BIC: mean diff -988.4, rats inferential better 24/24, p = 1.19e-07 | AIC: mean diff -1000.4, rats inferential better 24/24, p = 1.19e-07 | cv: mean diff -437.5, rats inferential better 23/24, p = 7.63e-05 | cvbest: mean diff -58.8, rats inferential better 13/24, p = 0.188
seed +3000: BIC: mean diff -992.0, rats inferential better 24/24, p = 1.19e-07 | AIC: mean diff -1004.0, rats inferential better 24/24, p = 1.19e-07 | cv: mean diff -451.8, rats inferential better 23/24, p = 4.42e-05 | cvbest: mean diff -33.3, rats inferential better 15/24, p = 0.229
seed +4000: BIC: mean diff -977.8, rats inferential better 24/24, p = 1.19e-07 | AIC: mean diff -989.8, rats inferential better 24/24, p = 1.19e-07 | cv: mean diff -425.1, rats inferential better 22/24, p = 9.08e-05 | cvbest: mean diff -65.3, rats inferential better 16/24, p = 0.121
--- [code claim:fig3j-inferential-beats-retrospective-for-wait-times] 0.0s
seed +0: BIC: mean diff -3.48, rats
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/c9.py <<'EOF'
#%% md
## bayes-observer-offer-reduces-uncertainty

> In simulations of a Bayes optimal observer, hearing the reward offer reduces the uncertainty of beliefs about the hidden block (posterior variance below prior variance).

Prior (Equation 5) and posterior (Equation 3) of the inferential model with H0 = 1/40 on each rat's offers, run over the trials with a wait time and reset at each session as in GenerateSynthData_Bayes.m (the first trial of a session has no prior and is left out). Readings: (i) the variance of the three block probabilities, where a less uncertain belief has a larger variance; (ii) the variance of the block value with blocks coded 1 low, 2 mixed, 3 high, where a less uncertain belief has a smaller variance. Each is tested over trials and over per-rat means (signed-rank).

#%% code claim:bayes-observer-offer-reduces-uncertainty
rows = []
for r in rats:
    rm = M.RatModel(t[t.subject == r])
    ok = ~rm.newsess
    pr, po = rm.prior[ok], rm.post[ok]
    v_i = (np.var(pr, 1), np.var(po, 1))
    code = np.array([2.0, 3.0, 1.0])  # mixed, high, low
    def bv(p):
        m = p @ code
        return p @ code ** 2 - m ** 2
    v_ii = (bv(pr), bv(po))
    rows.append(dict(rat=r, n=int(ok.sum()), i_prior=v_i[0].mean(), i_post=v_i[1].mean(), ii_prior=v_ii[0].mean(), ii_post=v_ii[1].mean(),
                     i_frac=float((v_i[1] > v_i[0]).mean()), ii_frac=float((v_ii[1] < v_ii[0]).mean()),
                     i_p=stats.wilcoxon(v_i[1], v_i[0], alternative="greater").pvalue,
                     ii_p=stats.wilcoxon(v_ii[1], v_ii[0], alternative="less").pvalue))
BO = pd.DataFrame(rows).set_index("rat")
for rd, better in [("i", "greater"), ("ii", "less")]:
    p_rats = stats.wilcoxon(BO[rd + "_post"], BO[rd + "_prior"], alternative=better).pvalue
    p_two = stats.wilcoxon(BO[rd + "_post"], BO[rd + "_prior"]).pvalue
    print(f"reading ({rd}): mean prior {BO[rd+'_prior'].mean():.4f}, posterior {BO[rd+'_post'].mean():.4f}; "
          f"per-rat means, signed-rank two-tailed p = {p_two:.3g} (one-tailed towards less uncertainty p = {p_rats:.3g}); "
          f"over trials: per-rat test p < 0.001 in {int((BO[rd+'_p'] < 0.001).sum())} of {len(BO)} rats, median share of trials less uncertain {BO[rd+'_frac'].median():.3f}")
    R.setdefault("bayes", {})[rd] = (BO[rd + "_prior"].mean(), BO[rd + "_post"].mean(), p_two, int((BO[rd + "_p"] < 0.001).sum()))
# pooled over all trials of all rats
EOF
cd $TMPDIR && . dev/bin/activate && python nb/dev.py nb/c1.py nb/c9.py 2>&1 | grep -v Warn | tail -4; date -u
```

```
--- [code sanity] 8.4s
reading (i): mean prior 0.1570, posterior 0.1694; per-rat means, signed-rank two-tailed p = 1.8e-49 (one-tailed towards less uncertainty p = 9.02e-50); over trials: per-rat test p < 0.001 in 291 of 291 rats, median share of trials less uncertain 0.655
reading (ii): mean prior 0.1041, posterior 0.0818; per-rat means, signed-rank two-tailed p = 1.8e-49 (one-tailed towards less uncertainty p = 9.02e-50); over trials: per-rat test p < 0.001 in 291 of 291 rats, median share of trials less uncertain 0.674
--- [code claim:bayes-observer-offer-reduces-uncertainty] 28.0s
Tue Nov 24 23:26:40 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/mah-2023/mah2023.py <<'EOF'


def simulate_iti(g, model, alpha0, dscale, noise_var, rng, nsims=50, gain=None):
    """Simulated trial initiation times on a rat's offers (GenerateLatencyData_*.m).
    model 'eq10' (AlphaPHModel: trials with a wait time, kappa0 = mean(ln[5..80]), D = 25 p,
    alpha from Equation 10), 'static' (VanillaAlpha: trials with an initiation time, kappa0 = 20,
    D = 10 p, G = 1) or 'rpe' (RPEAlpha: trials with an initiation time, kappa0 = 0.5, D = 15 p,
    G = |delta|). TI = D / kappa (Equation 2), kappa < 0 set to eps. Noise: log-normal with mean
    TI and variance `noise_var`; the mean of `nsims` simulations is drawn from its normal
    approximation (mean TI, variance noise_var / nsims), a standard shortcut that only changes
    the noise. Returns a Series over g.index (NaN off the model's trials)."""
    if model == "eq10":
        good = g["wait_time"].notna().to_numpy()
        k0, D, mode = float(np.mean(np.log([5, 10, 20, 40, 80]))), 25 * dscale, 0
    elif model == "static":
        good = g["inter_trial_interval"].notna().to_numpy()
        k0, D, mode = 20.0, 10 * dscale, 1
    else:
        good = g["inter_trial_interval"].notna().to_numpy()
        k0, D, mode = 0.5, 15 * dscale, 2
    h = g.loc[good]
    r = np.log2(h["reward_volume_ul"].to_numpy().astype(float))
    s = h["sess"].to_numpy()
    new = np.r_[True, s[1:] != s[:-1]]
    if mode == 0:
        vidx = h["vol"].map({5: 0, 10: 1, 20: 2, 40: 3, 80: 4}).to_numpy().astype(np.int64)
        post, _ = belief_filter(vidx, new, 1.0, np.array([0.5, 0.25, 0.25]))
        dm = np.abs(np.diff(post[:, 0], prepend=np.nan))
        gain = np.where(new, 1.0, 1.0 / (1 - np.nan_to_num(dm)))
    else:
        gain = np.ones(len(r))
    kap = retro_kappa(r, new, gain, alpha0, mode, k0)
    kap = np.where(kap < 0, 1e-16, kap)
    ti = D / kap
    sim = ti + rng.normal(0, np.sqrt(noise_var / nsims), len(ti)) if nsims > 1 else \
        np.exp(rng.normal(np.log(ti) - np.log(noise_var / ti ** 2 + 1) / 2, np.sqrt(np.log(noise_var / ti ** 2 + 1))))
    out = pd.Series(np.nan, index=g.index)
    out.loc[h.index] = sim
    return out


def logistic4(x, A, D, C, x0):
    return A + (D - A) / (1 + np.exp(-C * (x - x0)))


def fit_logistic(x, y):
    """4-parameter logistic of Equation 11 (A lower asymptote, D upper, C inverse temperature, x0
    midpoint), least squares from two deterministic starts (my_fit_sigmoid.m uses 10 random
    starts; a standard choice)."""
    from scipy.optimize import curve_fit
    best, bc = None, np.inf
    for c0 in (0.5, -0.5):
        p0 = [y[: len(y) // 2].mean(), y[len(y) // 2:].mean(), c0, 0.0]
        try:
            p, _ = curve_fit(logistic4, x, y, p0=p0, maxfev=4000,
                             bounds=([-10, -10, -10, -20], [10, 10, 10, 20]))
        except RuntimeError:
            continue
        c = np.sum((logistic4(x, *p) - y) ** 2)
        if c < bc:
            best, bc = p, c
    return best if best is not None else np.full(4, np.nan)
EOF
cat > $TMPDIR/nb/c10.py <<'EOF'
#%% md
## fig3i-retrospective-model-captures-initiation

> A retrospective model with a learning rate scaled by changes in the inferred block posterior captures the slow and fast dynamics of trial initiation times at block transitions and their dependence on previous rewards, while a static learning rate or an unsigned prediction error gain does not.

Initiation times simulated on each rat's offers (simulate_iti in the helper): the Equation 10 model at alpha0 = 0.1042 and D-scale 0.2527 (Figure3.m), smoothing 15; the alternatives (G = 1 and G = |delta|) and the Equation 10 model at alpha0 = 0.05, 0.4 and 0.8 with smoothing 20 (Supplementary Fig. 7; FigureS7.m), D-scale 0.2527 throughout. Log-normal noise of variance 4 (Methods), 50 simulations; variance 8 (Figure3.m) as a variant. The simulated times go through the rats' pipeline (z-scored, detrended per session, transition curves). Overshoot: the high-to-mixed curve's maximum over trials 1 to 20 exceeds its value at trial 20. Persistent gap: the high-to-mixed curve lies above the low-to-mixed curve over trials 10 to 20 (mean difference > 0; a reading of "persistent").

#%% code claim:fig3i-retrospective-model-captures-initiation
SIMC = ["subject", "sess", "trial", "block", "vol", "reward_volume_ul", "wait_time", "inter_trial_interval"]
by_rat = {r: g for r, g in t[SIMC].groupby("subject")}

def sim_curves(model, alpha0, noise, smooth, rng, dscale=0.2527):
    sim = pd.concat([M.simulate_iti(by_rat[r], model, alpha0, dscale, noise, rng) for r in MODEL_RATS])
    tt = t.loc[sim.index, ["subject", "sess", "trial", "block"]].assign(sim=sim)
    v = tt.sim.where(tt.trial > 0)
    z = (v - v.groupby(tt.subject).transform("mean")) / v.groupby(tt.subject).transform("std")
    tt["dt"] = M.detrend_iti(tt, z, per_session=True)
    tt = tt.reset_index(drop=True)
    c = M.transition_curves(tt, tt.dt, M.transitions(tt), smooth=smooth)
    h, l = c[HM].mean(), c[LM].mean()
    over = float(h.loc[1:20].max() - h.loc[20])
    gap_ = float((h - l).loc[10:20].mean())
    return over, gap_, h, l

FIG3I = {}
for noise in [4, 8]:
    rng = rng_for("fig3i-retrospective-model-captures-initiation", offset=0 if noise == 4 else 1)
    configs = [("eq10", 0.1042, 15)] + [(m, a, 20) for m in ["static", "rpe", "eq10"] for a in [0.05, 0.4, 0.8]]
    for model, a0, sm in configs:
        over, gap_, h, l = sim_curves(model, a0, noise, sm, rng)
        FIG3I[(noise, model, a0)] = (over, gap_)
        print(f"noise {noise}: {model:6s} alpha0 {a0:<6}: overshoot {over:+.4f} ({'yes' if over > 0 else 'no'}), "
              f"gap after high minus after low, trials 10-20 {gap_:+.4f} ({'yes' if gap_ > 0 else 'no'})")
R["fig3i"] = FIG3I

#%% code claim:fig3i-retrospective-model-captures-initiation
# Fig. 3i: each rat's retrospective parameters fitted to wait times (fig3j, claim's seed), simulated
# initiation times (one draw, noise 1.5 as Figure3.m, and 4 as the Methods), then the analysis of
# fig2k (code reading: all mixed block trials; and the Methods reading: 20 uL trials)
for noise in [4, 1.5]:
    rng = rng_for("fig3i-retrospective-model-captures-initiation", k=1, offset=0 if noise == 4 else 1)
    sim = pd.concat([M.simulate_iti(by_rat[r], "eq10", FITS[0][r]["retrospective"]["params"][0],
                                    FITS[0][r]["retrospective"]["params"][1], noise, rng, nsims=1) for r in MODEL_RATS])
    tt = t.loc[sim.index, ["subject", "trial", "block", "vol", "prev_vol"]].assign(sim=sim.where(t.loc[sim.index, "trial"] > 0))
    tt["z"] = (tt.sim - tt.groupby("subject").sim.transform("mean")) / tt.groupby("subject").sim.transform("std")
    for name, m in [("C: all mixed trials", tt.block == 1), ("M: 20 uL trials", (tt.block == 1) & (tt.vol == 20))]:
        d = tt[m & tt.prev_vol.notna() & tt.z.notna()]
        mk = pd.DataFrame({"below": d[d.prev_vol < 20].groupby("subject").z.mean(), "above": d[d.prev_vol > 20].groupby("subject").z.mean()}).dropna()
        p = stats.wilcoxon(mk.below, mk.above).pvalue
        print(f"noise {noise}, {name}: model mean z after < 20 {mk.below.mean():+.4f}, after > 20 {mk.above.mean():+.4f}; "
              f"rats higher after smaller offers {int((mk.below > mk.above).sum())} of {len(mk)}; signed-rank p = {p:.3g}")
        R.setdefault("fig3i_prev", {})[(noise, name)] = (mk.below.mean(), mk.above.mean(), p)
EOF
cd $TMPDIR && sed -i 's/^MODEL_RATS = list(rats)\[:24\]$/MODEL_RATS = list(rats)[:24]\nFITS_ONLY_FIRST = True/' nb/c8.py && python3 - <<'EOF'
s=open('/tmp/claude-1001/nb/c8.py').read()
s=s.replace("for off in [0, 1000, 2000, 3000, 4000]:\n    FITS[off]","for off in ([0] if 'FITS_ONLY_FIRST' in globals() else [0, 1000, 2000, 3000, 4000]):\n    FITS[off]")
open('/tmp/claude-1001/nb/c8.py','w').write(s)
EOF
. dev/bin/activate && OMP_NUM_THREADS=1 python nb/dev.py nb/c1.py nb/c3.py nb/c5.py nb/c8.py nb/c10.py 2>&1 | grep -v Warn | sed -n '/claim:suppfig9/,$p'
```

```
--- [code claim:suppfig9-wait-times-reflect-misinferences] 25.7s
noise 4: eq10   alpha0 0.1042: overshoot +0.1924 (yes), gap after high minus after low, trials 10-20 +1.3972 (yes)
noise 4: static alpha0 0.05  : overshoot +0.0000 (no), gap after high minus after low, trials 10-20 -0.3719 (no)
noise 4: static alpha0 0.4   : overshoot +0.0000 (no), gap after high minus after low, trials 10-20 +0.1466 (yes)
noise 4: static alpha0 0.8   : overshoot +0.0000 (no), gap after high minus after low, trials 10-20 +0.1588 (yes)
noise 4: rpe    alpha0 0.05  : overshoot +0.0000 (no), gap after high minus after low, trials 10-20 -0.1116 (no)
noise 4: rpe    alpha0 0.4   : overshoot +0.0000 (no), gap after high minus after low, trials 10-20 +0.1841 (yes)
noise 4: rpe    alpha0 0.8   : overshoot +0.0002 (yes), gap after high minus after low, trials 10-20 +0.1794 (yes)
noise 4: eq10   alpha0 0.05  : overshoot +0.0186 (yes), gap after high minus after low, trials 10-20 +1.5550 (yes)
noise 4: eq10   alpha0 0.4   : overshoot +0.0745 (yes), gap after high minus after low, trials 10-20 +0.4256 (yes)
noise 4: eq10   alpha0 0.8   : overshoot +0.0152 (yes), gap after high minus after low, trials 10-20 +0.1626 (yes)
noise 8: eq10   alpha0 0.1042: overshoot +0.1595 (yes), gap after high minus after low, trials 10-20 +1.1524 (yes)
noise 8: static alpha0 0.05  : overshoot +0.0000 (no), gap after high minus after low, trials 10-20 -0.2804 (no)
noise 8: static alpha0 0.4   : overshoot +0.0004 (yes), gap after high minus after low, trials 10-20 +0.0966 (yes)
noise 8: static alpha0 0.8   : overshoot +0.0000 (no), gap after high minus after low, trials 10-20 +0.1224 (yes)
noise 8: rpe    alpha0 0.05  : overshoot +0.0000 (no), gap after high minus after low, trials 10-20 -0.0971 (no)
noise 8: rpe    alpha0 0.4   : overshoot +0.0004 (yes), gap after high minus after low, trials 10-20 +0.1673 (yes)
noise 8: rpe    alpha0 0.8   : overshoot +0.0019 (yes), gap after high minus after low, trials 10-20 +0.162
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/c11.py <<'EOF'
#%% md
## fig3l-lambda-groups-wait-time-dynamics

> Rats with optimal and poor inference (high or low lambda of the sub-optimal inferential model) differ in their wait time dynamics at transitions from mixed into low or high blocks, but not in their trial initiation time dynamics.

Lambda per rat from the sub-optimal inferential model (Equation 8; GenerateSynthData_Bayes_subopt_onlylambda_flat.m: five parameters, flat reset of the belief at each session). For time, the model is fitted once on all of each rat's data from one random start (claim's seed), without the cross-validation of fig3j (a deviation). Groups below the 20th and above the 80th percentile of lambda (Methods, Results) and below the 40th and above the 60th (Figure3.m). Mixed-to-low and mixed-to-high curves (wait time per offer z-scored, initiation detrended per session, 30 trials either side, smoothed, trials -20 to 20 kept) averaged per group; Equation 11 fitted to each group mean; 500 label shuffles; p = share of shuffles with |parameter difference| above the observed, divided by 2 (myLambdaShuffleTest.m, as myTauShuffleTest.m). Shuffle seeds: the claim's and +1000 to +4000.

#%% code claim:fig3l-lambda-groups-wait-time-dynamics
TL = time.time()
LAM = M.fit_all(t, MODEL_RATS, ["lambda"], zlib.crc32(b"mah-2023/fig3l-lambda-groups-wait-time-dynamics"), nstarts=1) if False else None
print("lambda fits: see below")

#%% code
EOF
python3 - <<'EOF'
# fig3l needs a single full-data fit; add a helper for it
p='entries/mah-2023/mah2023.py'
s=open(p).read()
s=s.replace('''def _fit_rat(args):
    rat, models, seed, nstarts = args
    rm = RatModel(_T[rat])
    out = {}
    for j, m in enumerate(models):
        out[m] = cv_fit(rm, m, np.random.default_rng(seed + j), nstarts=nstarts)
    return rat, out''','''def _fit_rat(args):
    rat, models, seed, nstarts, cv = args
    rm = RatModel(_T[rat])
    out = {}
    for j, m in enumerate(models):
        rng = np.random.default_rng(seed + j)
        if cv:
            out[m] = cv_fit(rm, m, rng, nstarts=nstarts)
        else:
            p, f = fit_model(rm, m, np.ones(int(rm.fit.sum()), bool), rng, nstarts)
            out[m] = dict(params=p, nll_all=f, k=len(p), n=int(rm.fit.sum()))
    return rat, out''')
s=s.replace('''def fit_all(trials, rats, models, seed, nstarts=3, procs=4):''','''def fit_all(trials, rats, models, seed, nstarts=3, procs=4, cv=True):''')
s=s.replace('''    args = [(r, models, seed + 10 * i, nstarts) for i, r in enumerate(rats)]''','''    args = [(r, models, seed + 10 * i, nstarts, cv) for i, r in enumerate(rats)]''')
open(p,'w').write(s)
EOF
cat > $TMPDIR/nb/c11.py <<'EOF'
#%% md
## fig3l-lambda-groups-wait-time-dynamics

> Rats with optimal and poor inference (high or low lambda of the sub-optimal inferential model) differ in their wait time dynamics at transitions from mixed into low or high blocks, but not in their trial initiation time dynamics.

Lambda per rat from the sub-optimal inferential model (Equation 8; GenerateSynthData_Bayes_subopt_onlylambda_flat.m: five parameters, belief reset to flat at each session). For time, the model is fitted once on all of each rat's data from one random start (claim's seed), without the cross-validation of fig3j (a deviation). Groups below the 20th and above the 80th percentile of lambda (Methods, Results) and below the 40th and above the 60th (Figure3.m). Mixed-to-low and mixed-to-high curves (wait time z-scored per offer, initiation time detrended per session, 30 trials either side, smoothed over 10, trials -20 to 20 kept) averaged per group; Equation 11 fitted to each group mean; 500 label shuffles, each half refitted; p = share of shuffles with |parameter difference| above the observed, divided by 2 (myLambdaShuffleTest.m, written as myTauShuffleTest.m). Shuffle seeds: the claim's and +1000 to +4000.

#%% code claim:fig3l-lambda-groups-wait-time-dynamics
TL = time.time()
LAM = M.fit_all(t, MODEL_RATS, ["lambda"], zlib.crc32(b"mah-2023/fig3l-lambda-groups-wait-time-dynamics"), nstarts=1, cv=False)
lam = pd.Series({r: LAM[r]["lambda"]["params"][4] for r in MODEL_RATS})
print(f"lambda fits: {time.time()-TL:.0f} s; lambda median {lam.median():.3f}, range {lam.min():.3f}-{lam.max():.3f}; "
      f"at 0: {int((lam <= 1e-6).sum())}, at 1: {int((lam >= 1 - 1e-6).sum())}")
c30 = {k: M.transition_curves(t, t[k], trans, twin=30, rats=MODEL_RATS) for k in ["zv_wt", "iti_dt_sess"]}
xs = np.arange(-20, 21)
PAR = {"A": 0, "D": 1, "C": 2, "x0": 3}

def lam_test(curves, lo_q, hi_q, rng, nshuf=500):
    sel = lo_q | hi_q
    Cv = curves.loc[sel.index[sel], -20:20].to_numpy()
    n = len(Cv); h = n // 2
    ok = ~np.isnan(Cv).all(1)
    obs1 = M.fit_logistic(xs, np.nanmean(curves.loc[lo_q.index[lo_q], -20:20].to_numpy(), 0))
    obs2 = M.fit_logistic(xs, np.nanmean(curves.loc[hi_q.index[hi_q], -20:20].to_numpy(), 0))
    obs = obs1 - obs2
    sh = np.empty((nshuf, 4))
    for i in range(nshuf):
        perm = rng.permutation(n)
        a = M.fit_logistic(xs, np.nanmean(Cv[perm[:h]], 0)); b = M.fit_logistic(xs, np.nanmean(Cv[perm[h:]], 0))
        sh[i] = a - b
    p = (np.abs(sh) > np.abs(obs)).sum(0) / (2 * nshuf)
    return dict(zip(PAR, p)), dict(zip(PAR, obs))

for split in [(20, 80), (40, 60)]:
    lo_q = lam < np.percentile(lam, split[0]); hi_q = lam > np.percentile(lam, split[1])
    print(f"split {split}: low-lambda group {int(lo_q.sum())}, high-lambda group {int(hi_q.sum())} rats")
    for off in ([0, 1000, 2000, 3000, 4000] if split == (20, 80) else [0]):
        for meas in ["zv_wt", "iti_dt_sess"]:
            for tr, nm in [(ML, "mixed->low"), (MH, "mixed->high")]:
                rng = rng_for("fig3l-lambda-groups-wait-time-dynamics", offset=off)
                p, obs = lam_test(c30[meas][tr], lo_q, hi_q, rng)
                R.setdefault("fig3l", {})[(split, off, meas, nm)] = p
                print(f"   seed +{off} {meas:12s} {nm:12s} p: " + ", ".join(f"{k} {v:.3f}" for k, v in p.items())
                      + " | observed differences: " + ", ".join(f"{k} {v:+.3f}" for k, v in obs.items()))
print(f"fig3l total {time.time()-TL:.0f} s")
EOF
cd $TMPDIR && . dev/bin/activate && OMP_NUM_THREADS=1 python nb/dev.py nb/c1.py nb/c3.py nb/c8.py nb/c11.py 2>&1 | grep -v Warn | sed -n '/lambda fits/,$p'
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && OMP_NUM_THREADS=1 python nb/dev.py nb/c1.py nb/c3.py nb/c8.py nb/c11.py 2>&1 | grep -v Warn | tail -30
```

```
[iti_dt_sess] trials -20..-1: initiation (before low) - (before high) = +0.046 (must be > 0); gap pre/post: wait time 0.013/0.107 = 0.125, initiation 0.046/0.234 = 0.197; holds: True
[iti_dt_pool] trials -20..-1: initiation (before low) - (before high) = +0.059 (must be > 0); gap pre/post: wait time 0.013/0.107 = 0.125, initiation 0.059/0.245 = 0.239; holds: True
wait time signed difference before low minus before high over -20..-1: +0.010
--- [code claim:suppfig5-mixed-to-adaptation-transitions] 0.0s
no detrending: high->mixed minus low->mixed over trials 1-20 = +0.246 (ordering holds if > 0)
part 2 without detrending: after high +0.094, after low -0.085, p = 1.8e-49
trials -20..-1: in high block -0.060, in low block +0.031
satiety: per-session slope of z-scored initiation time on trial number, median 0.0693 z per 100 trials
--- [code claim:suppfig6-results-without-detrending] 11.1s
seed +0: fitted 24 rats, 21 s so far
inferential parameters (claim's seed), median: {'k_mixed': 0.134, 'k_high': 0.155, 'k_low': 0.16, 'D': 0.089} | at a bound: {'k_mixed': 1, 'k_high': 1, 'k_low': 1, 'D': 1}
rats whose fitted k_high > k_low (higher opportunity cost in high blocks): 17 of 24
--- [code] 21.2s
seed +0: BIC: mean diff -994.0, rats inferential better 24/24, p = 1.19e-07 | AIC: mean diff -1006.1, rats inferential better 24/24, p = 1.19e-07 | cv: mean diff -438.4, rats inferential better 23/24, p = 3.66e-05 | cvbest: mean diff -60.9, rats inferential better 15/24, p = 0.152
--- [code claim:fig3j-inferential-beats-retrospective-for-wait-times] 0.0s
seed +0: BIC: mean diff -3.48, rats inferential better 12/24, p = 0.684 | AIC: mean diff -3.48, rats inferential better 12/24, p = 0.684 | cv: mean diff +31.50, rats inferential better 11/24, p = 0.705 | cvbest: mean diff +26.83, rats inferential better 10/24, p = 0.527
--- [code claim:suppfig8-belief-state-not-distinguished] 0.0s
draw seed +0: model sensitivity (below minus above) +0.0113; rank-sum p = 0.765; signed-rank p = 0.546

[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('c8.py').read()
s=s.replace('''print(f"rats (fig2j): sensitivity {R['fig2j'][3]:+.4f}, rank-sum p = {R['fig2j'][1]:.3g}")''','''p, sens, psr = fig2j_test(t.wt)
print(f"rats (fig2j analysis on the rats' wait times): sensitivity {sens:+.4f}, rank-sum p = {p:.3g}")''')
open('c8.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && OMP_NUM_THREADS=1 python nb/dev.py nb/c1.py nb/c3.py nb/c8.py nb/c11.py 2>&1 | grep -v Warn | sed -n '/rats (fig2j/,$p'
```

```
rats (fig2j analysis on the rats' wait times): sensitivity -0.0094, rank-sum p = 0.575
--- [code claim:fig3f-inferential-model-not-sensitive-to-previous-offer] 11.2s
mixed-block 20 uL catch trials by label: {'mixed': 102565, 'high': 8540, 'low': 7688}
rats with both labels: 291; mean wait labelled high 10.854 s, labelled low 11.898 s; rats shorter when labelled high 230; signed-rank p = 9.72e-23
--- [code claim:suppfig9-wait-times-reflect-misinferences] 25.6s
lambda fits: 19 s; lambda median 0.370, range 0.130-1.000; at 0: 0, at 1: 0
split (20, 80): low-lambda group 5, high-lambda group 5 rats
   seed +0 zv_wt        mixed->low   p: A 0.402, D 0.108, C 0.310, x0 0.234 | observed differences: A +0.037, D -0.144, C -1.161, x0 -11.092
   seed +0 zv_wt        mixed->high  p: A 0.367, D 0.439, C 0.338, x0 0.244 | observed differences: A +0.027, D -0.018, C -1.657, x0 -4.850
   seed +0 iti_dt_sess  mixed->low   p: A 0.299, D 0.492, C 0.282, x0 0.244 | observed differences: A +0.035, D +0.002, C +0.365, x0 -1.101
   seed +0 iti_dt_sess  mixed->high  p: A 0.441, D 0.436, C 0.441, x0 0.308 | observed differences: A +0.006, D -0.006, C +0.251, x0 +3.440
   seed +1000 zv_wt        mixed->low   p: A 0.398, D 0.135, C 0.299, x0 0.226 | observed differences: A +0.037, D -0.144, C -1.161, x0 -11.092
   seed +1000 zv_wt        mixed->high  p: A 0.339, D 0.443, C 0.329, x0 0.248 | observed differences: A +0.027, D -0.018, C -1.657, x0 -4.850
   seed +1000 iti_dt_sess  mixed->low   p: A 0.306, D 0.491, C 0.294, x0 0.244 | observed differences: A +0.035, D +0.002, C +0.365, x0 -1.101
   seed +1000 iti_dt_sess  mixed->high  p: A 0.436, D 0.436, C 0.445, x0 0.325 | observed differences: A +0.006, D -0.006, C +0.251, x0 +3.440
   seed +2000 zv_wt        mixed->low   p: A 0.390, D 0.103, C 0.272, x0 0.222 | observed differences: A +0.037, D -0.144, C -1.161, x0 -11.092
   seed +2000 zv_wt        mixed->high  p: A 0.349, D 0.428, C 0.345, x0 0.269 | observed differences: A +0.027, D -0.018
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/mah-2023 && python3 - <<'EOF'
s=open('mah2023.py').read()
a=s.index('def fit_logistic(x, y):')
s=s[:a]+'''def fit_logistic(x, Y, ngrid_c=161, ngrid_x0=81):
    """4-parameter logistic of Equation 11 (A lower asymptote, D upper, C inverse temperature, x0
    midpoint) fitted by least squares to each row of Y: a grid over C in [-8, 8] and x0 in
    [-20, 20], with A and D solved exactly for each grid point (the model is linear in them).
    my_fit_sigmoid.m uses fmincon from 10 random starts; the grid is a deterministic search for
    the same optimum (a standard choice). Returns an array (rows, 4) of (A, D, C, x0)."""
    x = np.asarray(x, float)
    Y = np.atleast_2d(np.asarray(Y, float))
    Cs = np.linspace(-8, 8, ngrid_c)
    Cs = Cs[Cs != 0]
    X0 = np.linspace(-20, 20, ngrid_x0)
    cc, xx = np.meshgrid(Cs, X0, indexing="ij")
    cc, xx = cc.ravel(), xx.ravel()
    with np.errstate(over="ignore"):
        S = 1 / (1 + np.exp(-cc[:, None] * (x[None, :] - xx[:, None])))  # (G, n)
    U = 1 - S
    suu, sus, sss = (U * U).sum(1), (U * S).sum(1), (S * S).sum(1)
    det = suu * sss - sus ** 2
    yu, ys = Y @ U.T, Y @ S.T  # (R, G)
    with np.errstate(all="ignore"):
        A = (yu * sss - ys * sus) / det
        D = (ys * suu - yu * sus) / det
        sse = (Y * Y).sum(1)[:, None] - 2 * (A * yu + D * ys) + A * A * suu + 2 * A * D * sus + D * D * sss
    sse = np.where(np.isfinite(sse), sse, np.inf)
    k = np.argmin(sse, 1)
    r = np.arange(len(Y))
    return np.c_[A[r, k], D[r, k], cc[k], xx[k]]
'''
open('mah2023.py','w').write(s)
EOF
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('c11.py').read()
a=s.index('def lam_test'); b=s.index('for split in')
s=s[:a]+'''def lam_test(curves, lo_q, hi_q, rng, nshuf=500):
    sel = lo_q | hi_q
    Cv = curves.loc[sel.index[sel], -20:20].to_numpy()
    n = len(Cv); h = n // 2
    g1 = np.nanmean(curves.loc[lo_q.index[lo_q], -20:20].to_numpy(), 0)
    g2 = np.nanmean(curves.loc[hi_q.index[hi_q], -20:20].to_numpy(), 0)
    obs = (M.fit_logistic(xs, g1) - M.fit_logistic(xs, g2))[0]
    perms = np.array([rng.permutation(n) for _ in range(nshuf)])
    a = M.fit_logistic(xs, np.nanmean(Cv[perms[:, :h]], 1)); b = M.fit_logistic(xs, np.nanmean(Cv[perms[:, h:]], 1))
    sh = a - b
    p = (np.abs(sh) > np.abs(obs)).sum(0) / (2 * nshuf)
    return dict(zip(PAR, p)), dict(zip(PAR, obs))

'''+s[b:]
open('c11.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && OMP_NUM_THREADS=1 python nb/dev.py nb/c1.py nb/c3.py nb/c8.py nb/c11.py 2>&1 | grep -v Warn | sed -n '/lambda fits/,$p' | head -12; date -u
```

```
Tue Nov 24 23:51:44 UTC 2026
lambda fits: 19 s; lambda median 0.370, range 0.130-1.000; at 0: 0, at 1: 0
split (20, 80): low-lambda group 5, high-lambda group 5 rats
   seed +0 zv_wt        mixed->low   p: A 0.066, D 0.345, C 0.348, x0 0.282 | observed differences: A -0.146, D +0.038, C +1.100, x0 -11.000
   seed +0 zv_wt        mixed->high  p: A 0.154, D 0.257, C 0.256, x0 0.280 | observed differences: A +0.079, D -0.069, C +3.600, x0 -5.000
   seed +0 iti_dt_sess  mixed->low   p: A 0.493, D 0.295, C 0.255, x0 0.207 | observed differences: A +0.002, D +0.036, C -0.400, x0 -1.000
   seed +0 iti_dt_sess  mixed->high  p: A 0.429, D 0.427, C 0.452, x0 0.330 | observed differences: A +0.008, D -0.006, C +0.200, x0 +3.000
   seed +1000 zv_wt        mixed->low   p: A 0.049, D 0.365, C 0.329, x0 0.277 | observed differences: A -0.146, D +0.038, C +1.100, x0 -11.000
   seed +1000 zv_wt        mixed->high  p: A 0.189, D 0.237, C 0.261, x0 0.276 | observed differences: A +0.079, D -0.069, C +3.600, x0 -5.000
   seed +1000 iti_dt_sess  mixed->low   p: A 0.490, D 0.271, C 0.236, x0 0.205 | observed differences: A +0.002, D +0.036, C -0.400, x0 -1.000
   seed +1000 iti_dt_sess  mixed->high  p: A 0.425, D 0.426, C 0.454, x0 0.352 | observed differences: A +0.008, D -0.006, C +0.200, x0 +3.000
   seed +2000 zv_wt        mixed->low   p: A 0.051, D 0.353, C 0.333, x0 0.271 | observed differences: A -0.146, D +0.038, C +1.100, x0 -11.000
   seed +2000 zv_wt        mixed->high  p: A 0.161, D 0.233, C 0.257, x0 0.299 | observed differences: A +0.079, D -0.069, C +3.600, x0 -5.000
Tue Nov 24 23:53:50 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/^MODEL_RATS = list(rats)\[:24\]$/MODEL_RATS = list(rats)/; /^FITS_ONLY_FIRST = True$/d' c8.py && python3 - <<'EOF'
s=open('c8.py').read()
s=s.replace("for off in ([0] if 'FITS_ONLY_FIRST' in globals() else [0, 1000, 2000, 3000, 4000]):\n    FITS[off]","for off in [0, 1000, 2000, 3000, 4000]:\n    FITS[off]")
open('c8.py','w').write(s)
EOF
grep -n "MODEL_RATS = \|for off in \[0, 1000" c8.py | head -3
cat > prepB.py <<'EOF'
#%% code
# Measures shared with the first notebook (see its sections fig2a and fig2j for their sources)
cw = t.wt.notna() & ~t.is_violation
zw = M.zscore_within(t, "wt", cw)
t["zv_wt"] = M.zscore_within(t.assign(zw=zw), "zw", cw & zw.notna(), keys=("subject", "vol"))
t["iti_dt_sess"] = M.detrend_iti(t, t.z_iti, per_session=True)
trans = M.transitions(t)
HM, LM, MH, ML = (2, 1), (3, 1), (1, 2), (1, 3)
print("transitions by type (prev -> next):", trans.groupby(["prev", "next"]).size().to_dict())
EOF
cd $TMPDIR && . dev/bin/activate && date -u && python nb/dev.py nb/c1.py nb/c2.py nb/c3.py nb/c4.py nb/c5.py nb/c9.py nb/c6.py nb/c7.py > devA.log 2>&1; date -u; grep -v Warn devA.log | grep -c . ; grep -i "error\|Traceback" devA.log | head
```

```
9:MODEL_RATS = list(rats)
12:for off in [0, 1000, 2000, 3000, 4000]:
96:for off in [0, 1000, 2000, 3000, 4000]:
Tue Nov 24 23:54:08 UTC 2026
Terminated                 python nb/dev.py nb/c1.py nb/c2.py nb/c3.py nb/c4.py nb/c5.py nb/c9.py nb/c6.py nb/c7.py > devA.log 2>&1
Tue Nov 24 23:56:24 UTC 2026
283
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep "^---" devA.log | tail -5; free -g
```

```
--- [code claim:fig5c-pre-cue-initiation-still-sensitive-to-previous-reward] 0.7s
--- [code claim:fig5d-pre-cue-initiation-depends-on-previous-block] 0.2s
--- [code] 8.3s
--- [code claim:fig4a-wait-time-block-sensitivity-emerges] 27.1s
--- [code claim:fig4c-initiation-previous-reward-stable] 10.5s
               total        used        free      shared  buff/cache   available
Mem:              15           1          13           0           0          14
Swap:              2           0           2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
s=open('c7.py').read()
s=s.replace('''Z = Z[Z.trainingstage == 9].copy()''','''Z = Z.loc[Z.trainingstage == 9, ["subject", "sess_in_rat", "catch", "optout", "reward", "block", "hits",
                                  "wait_time", "wait_thresh", "ITI"]].reset_index(drop=True)''')
s=s.replace('''Z = Z[~bad].copy()''','''Z = Z[~bad].reset_index(drop=True)''')
s=s.replace('''Z["wt"] = Z.wait_time.where((Z.catch == 1) & (Z.optout == 1) & (Z.wait_time <= Z.wait_thresh))''','''Z["wt"] = Z.wait_time.where((Z.catch == 1) & (Z.optout == 1) & (Z.wait_time <= Z.wait_thresh))
Z = Z.drop(columns=["wait_time", "wait_thresh", "catch", "optout", "reward"])''')
s=s.replace('''def overshoot_curve(df):
    df = df.copy()
    df["iti"], df["z_iti"] = prep_iti(df)''','''def overshoot_curve(df):
    df = df[["subject", "sess", "trial", "block", "ITI"]].reset_index(drop=True)
    df["iti"], df["z_iti"] = prep_iti(df)''')
s=s.replace('''early = Z[Z.sess_in_rat < 10].reset_index(drop=True)
late = Z[Z.sess_in_rat > nmax - 10].reset_index(drop=True)''','''early = Z[Z.sess_in_rat < 10]
late = Z[Z.sess_in_rat > nmax - 10]''')
s=s.replace('''Zc = Z.copy(); Zc["chunk"] = Zc.sess_in_rat // 5
ch = {}
for k, g in Zc[Zc.chunk < 20].groupby("chunk"):
    ch[k] = overshoot_curve(g.reset_index(drop=True))[0]''','''chunk = Z.sess_in_rat // 5
ch = {}
for k in range(20):
    ch[k] = overshoot_curve(Z[chunk == k])[0]''')
open('c7.py','w').write(s)
EOF
grep -n "Z50 = \|Z\[\"pair\"\]\|Z50\[" c7.py | head -4
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
# drop columns of t that later cells do not use, before Figure 4 (dev check of memory)
EOF
cat > $TMPDIR/nb/c6b.py <<'EOF'
#%% code
# free memory before reading the deposit
for c in ["z_wt", "wt_raw", "iti_dt_pool", "prev_block_of_block", "after_date", "cue_flag", "post_violation", "precue_n"]:
    if c in t:
        del t[c]
import gc; gc.collect()
print("peak memory so far (GB):", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)
EOF
cd $TMPDIR && . dev/bin/activate && date -u && python nb/dev.py nb/c1.py nb/c2.py nb/c3.py nb/c4.py nb/c5.py nb/c9.py nb/c6.py nb/c6b.py nb/c7.py > devA.log 2>&1; date -u; grep "^---\|peak" devA.log | tail -4; grep -i "Traceback\|Error" devA.log | head
```

```
50:Z50 = Z[Z.sess_in_rat < 50].copy()
51:Z50["pair"] = Z50.sess_in_rat // 2
52:w = Z50[(Z50.vol == 20) & Z50.wt.notna() & Z50.block.isin([2, 3])]
55:i_ = Z50[Z50.iti.notna() & Z50.block.isin([2, 3])]
Tue Nov 24 23:56:45 UTC 2026
Tue Nov 24 23:59:03 UTC 2026
--- [code] 7.6s
--- [code claim:fig4a-wait-time-block-sensitivity-emerges] 25.8s
--- [code claim:fig4c-initiation-previous-reward-stable] 10.4s
--- [code claim:fig4d-overshoot-grows-with-training] 6.2s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep "peak" devA.log; grep -v "Warn\|^---\|warn" devA.log | sed -n '/^rats: 291/,$p' | head -150
```

```
peak memory (GB): 3.42652
peak memory so far (GB): 8.179504
rats: 291 (expected 291, tolerance 0)
median trials per rat: 33493.0 (expected 33493 +- 3349); range 5266 - 129864
median sessions per rat: 71.0 (expected 71 +- 7); range 15 - 232
rats with every offer: 291 of 291
population mean wait time (s) by offer: {np.int64(5): 10.451, np.int64(10): 10.773, np.int64(20): 11.105, np.int64(40): 13.027, np.int64(80): 13.809}
increases at every step: True
rats whose own curve increases at every step: 171
by sex: {'F': {5: 10.41, 10: 10.63, 20: 10.82, 40: 12.62, 80: 13.37}, 'M': {5: 10.47, 10: 10.86, 20: 11.27, 40: 13.26, 80: 14.06}}
rats with both blocks: 291
mean ratio high/low = 0.8942 (expected 0.90 +- 0.025); median 0.8897; range 0.760-1.230; rats with ratio < 1: 279
(a) signed-rank on z-scored means: p = 4.61e-47; mean z high -0.244, low 0.054
(b) signed-rank on raw means: p = 8.18e-47; mean high 10.852 s, low 12.165 s
per-rat one-tailed rank-sum (high shorter), rats with p < 0.05: 244 of 291
ratio by sex (mean): {'F': 0.8977, 'M': 0.8923}
mean ratio high/low = 0.5676; median 0.5542; rats < 1: 291 of 291
(a) z-scored: p = 1.8e-49; mean z high -0.087, low 0.106
(b) raw: p = 1.8e-49; mean high 2.187 s, low 3.924 s
per-rat two-tailed rank-sum, rats with p < 0.05: 248
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Result\|def handover\|conclusion" tools/entry.py | head -20; grep -n "timeout\|runtime\|80\b\|minutes" tools/entry.py | head -20
```

```
36:(docs/protocol.md): the executed notebooks with the conclusions removed (every
37:markdown cell that begins "**Result:" and everything from the "## Summary"
654:def strip_conclusions(nb):
655:    """The notebook without the author's conclusions, for a verifier's first round."""
661:        if cell.cell_type == "markdown" and text.startswith("**Result:"):
668:def handover(entry_dir: Path, output_dir: Path) -> int:
678:        nb = strip_conclusions(nbformat.read(executed, as_version=4))
29:that takes longer than --max-minutes fails, even if it ran without error.
524:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
525:                   max_minutes: float) -> int:
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
578:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
589:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
598:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
627:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
634:        if ok and seconds > max_minutes * 60:
636:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
702:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
703:    parser.add_argument("--max-minutes", type=float, default=60,
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && date -u && OMP_NUM_THREADS=1 python nb/dev.py nb/c1.py nb/prepB.py nb/c8.py nb/c10.py nb/c11.py > devB.log 2>&1; date -u; grep "^---" devB.log | tail -12; grep -i "Traceback\|Error\|Terminated" devB.log | head
```

```
Tue Nov 24 23:59:17 UTC 2026
Wed Nov 25 00:25:58 UTC 2026
--- [code load] 1.9s
--- [code] 2.0s
--- [code sanity] 8.3s
--- [code] 3.8s
--- [code] 1063.4s
--- [code claim:fig3j-inferential-beats-retrospective-for-wait-times] 0.0s
--- [code claim:suppfig8-belief-state-not-distinguished] 0.0s
--- [code claim:fig3f-inferential-model-not-sensitive-to-previous-offer] 128.9s
--- [code claim:suppfig9-wait-times-reflect-misinferences] 25.4s
--- [code claim:fig3i-retrospective-model-captures-initiation] 114.6s
--- [code claim:fig3i-retrospective-model-captures-initiation] 11.4s
--- [code claim:fig3l-lambda-groups-wait-time-dynamics] 239.1s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "Warn\|warn\|^---" devB.log | sed -n '/seed +0: fitted/,$p' | grep -v "^   seed +[1-4]000"
```

```
seed +0: fitted 291 rats, 212 s so far
seed +1000: fitted 291 rats, 426 s so far
seed +2000: fitted 291 rats, 639 s so far
seed +3000: fitted 291 rats, 853 s so far
seed +4000: fitted 291 rats, 1063 s so far
inferential parameters (claim's seed), median: {'k_mixed': 0.218, 'k_high': 0.256, 'k_low': 0.182, 'D': 0.107} | at a bound: {'k_mixed': 5, 'k_high': 2, 'k_low': 8, 'D': 1}
rats whose fitted k_high > k_low (higher opportunity cost in high blocks): 249 of 291
seed +0: BIC: mean diff -1039.5, rats inferential better 290/291, p = 3.55e-48 | AIC: mean diff -1051.6, rats inferential better 290/291, p = 3.55e-48 | cv: mean diff -454.3, rats inferential better 284/291, p = 5.59e-44 | cvbest: mean diff -85.2, rats inferential better 214/291, p = 4.49e-18
seed +1000: BIC: mean diff -1046.2, rats inferential better 291/291, p = 1.8e-49 | AIC: mean diff -1058.4, rats inferential better 291/291, p = 1.8e-49 | cv: mean diff -508.8, rats inferential better 286/291, p = 7.94e-47 | cvbest: mean diff -86.2, rats inferential better 207/291, p = 7.12e-16
seed +2000: BIC: mean diff -1061.1, rats inferential better 291/291, p = 1.8e-49 | AIC: mean diff -1073.3, rats inferential better 291/291, p = 1.8e-49 | cv: mean diff -469.9, rats inferential better 283/291, p = 5.53e-46 | cvbest: mean diff -86.9, rats inferential better 209/291, p = 1.77e-18
seed +3000: BIC: mean diff -1052.3, rats inferential better 291/291, p = 1.8e-49 | AIC: mean diff -1064.4, rats inferential better 291/291, p = 1.8e-49 | cv: mean diff -476.2, rats inferential better 285/291, p = 5.05e-47 | cvbest: mean diff -91.0, rats inferential better 215/291, p = 4.15e-19
seed +4000: BIC: mean diff -1040.7, rats inferential better 291/291, p = 1.8e-49 | AIC: mean diff -1052.8, rats inferential better 291/291, p = 1.8e-49 | cv: mean diff -447.5, rats inferential better 285/291, p = 6.05e-47 | cvbest: mean diff -107.9, rats inferential better 213/291, p = 4.72e-21
seed +0: BIC: mean diff +11.02, rats inferential better 13
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep "^   seed +[1-4]000" devB.log | grep -v "observed" ; grep "^   seed +[1-4]000" devB.log | sed 's/| observed.*//'
```

```
seed +1000 zv_wt        mixed->low   p: A 0.266, D 0.010, C 0.018, x0 0.156 
   seed +1000 zv_wt        mixed->high  p: A 0.151, D 0.117, C 0.039, x0 0.023 
   seed +1000 iti_dt_sess  mixed->low   p: A 0.116, D 0.130, C 0.138, x0 0.378 
   seed +1000 iti_dt_sess  mixed->high  p: A 0.371, D 0.383, C 0.328, x0 0.087 
   seed +2000 zv_wt        mixed->low   p: A 0.259, D 0.014, C 0.009, x0 0.147 
   seed +2000 zv_wt        mixed->high  p: A 0.120, D 0.110, C 0.027, x0 0.021 
   seed +2000 iti_dt_sess  mixed->low   p: A 0.119, D 0.106, C 0.130, x0 0.351 
   seed +2000 iti_dt_sess  mixed->high  p: A 0.367, D 0.385, C 0.334, x0 0.104 
   seed +3000 zv_wt        mixed->low   p: A 0.253, D 0.017, C 0.016, x0 0.136 
   seed +3000 zv_wt        mixed->high  p: A 0.122, D 0.104, C 0.032, x0 0.020 
   seed +3000 iti_dt_sess  mixed->low   p: A 0.112, D 0.123, C 0.138, x0 0.380 
   seed +3000 iti_dt_sess  mixed->high  p: A 0.352, D 0.372, C 0.336, x0 0.118 
   seed +4000 zv_wt        mixed->low   p: A 0.253, D 0.017, C 0.017, x0 0.151 
   seed +4000 zv_wt        mixed->high  p: A 0.117, D 0.117, C 0.026, x0 0.019 
   seed +4000 iti_dt_sess  mixed->low   p: A 0.124, D 0.101, C 0.143, x0 0.379 
   seed +4000 iti_dt_sess  mixed->high  p: A 0.370, D 0.382, C 0.341, x0 0.113
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -A3 "^\[sessions a\] trials\|^\[sessions b\] trials" devA.log | head -4; grep "linked rats\|^\[a\]\|^\[b\]" devA.log
```

```
[sessions a] trials 1-20 of mixed blocks: after high +0.123, after low -0.116; rats higher after high 11 of 11; signed-rank p = 0.000977
[sessions b] trials 1-20 of mixed blocks: after high +0.136, after low -0.114; rats higher after high 16 of 16; signed-rank p = 3.05e-05
--- [code claim:fig5d-pre-cue-initiation-depends-on-previous-block] 0.2s
peak memory so far (GB): 8.179504
linked rats: 14 of 16
[a] pre-cue: rats 11, population mean z by offer {np.int64(5): 0.016, np.int64(10): 0.024, np.int64(20): -0.041, np.int64(40): -0.14, np.int64(80): -0.165}; decreasing at every step: False; rats ANOVA p < 0.05: 11
[a] original: rats 12, population mean z by offer {np.int64(5): -0.146, np.int64(10): -0.149, np.int64(20): -0.143, np.int64(40): -0.144, np.int64(80): -0.151}; decreasing at every step: False; rats ANOVA p < 0.05: 0
[b] pre-cue: rats 16, population mean z by offer {np.int64(5): -0.041, np.int64(10): -0.051, np.int64(20): -0.088, np.int64(40): -0.156, np.int64(80): -0.178}; decreasing at every step: True; rats ANOVA p < 0.05: 14
[b] original: rats 12, population mean z by offer {np.int64(5): -0.146, np.int64(10): -0.149, np.int64(20): -0.143, np.int64(40): -0.144, np.int64(80): -0.151}; decreasing at every step: False; rats ANOVA p < 0.05: 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/^cells = diff.stack()$/cells = diff.stack().dropna()/' c2.py && grep -n "cells = diff" c2.py && cat > concl.py <<'PYEOF'
import re, glob
C = {
"fig1f-wait-time-block-effect": "**Result: reproduced.** The mean ratio of 20 uL wait times, high over low, is 0.894 (expected 0.90 +- 0.025), and the signed-rank test across 291 rats gives p = 4.6e-47 on z-scored means (a) and 8.2e-47 on raw means (b). 244 of 291 rats wait significantly less in high blocks by the per-rat one-tailed rank-sum test.",
"fig1i-initiation-block-effect": "**Result: reproduced.** The mean initiation time ratio, high over low, is 0.568 and below 1 in all 291 rats; the signed-rank test gives p = 1.8e-49 under both readings (the paper prints 1.82e-49).",
"suppfig2-initiation-block-effect-after-unrewarded": "**Result: reproduced.** After unrewarded trials initiation is faster in high blocks in all 291 rats (two-tailed p = 1.8e-49; one-tailed p = 9.0e-50, the paper prints 9.07e-50). After rewarded trials the one-tailed test in that direction gives p = 1, as printed in the paper; the two-tailed test finds a small difference the other way (high minus low +0.018 z, p = 8.5e-10), which the criterion does not count against the claim.",
"suppfig3-wait-time-not-affected-by-previous-outcome": "**Result: reproduced.** The mean wait time ratio is 0.899 after rewarded and 0.897 after unrewarded trials, both below 1; they differ by 0.002 (signed-rank p = 0.63, a variant).",
"suppfig12-no-sex-differences": "**Result: reproduced.** Neither ratio differs between the 184 males and 107 females: rank-sum p = 0.238 for the wait time ratio (the paper prints 0.23) and p = 0.343 for the initiation time ratio (the paper prints 0.59).",
"suppfig14-contextual-effects-without-threshold": "**Result: reproduced.** Without the threshold, 20 uL wait times are still shorter in high than in low blocks (signed-rank p = 1.5e-44 on z-scored means, 1.0e-43 on raw means), and the population mean is longer unthresholded in all 11 block and offer cells, most in low blocks (+2.61 s, against +1.42 s in mixed and +1.34 s in high blocks).",
"fig2a-wait-time-converges-in-mixed-blocks": "**Result: reproduced.** After a transition into a mixed block, the gap between the wait time curves after high and after low blocks is 0.341 of its pre-transition size over trials 1-20 (0.086 over trials 10-20), while the initiation time gap is 1.90 times its pre-transition size (2.10 over trials 10-20; 2.22 and 2.45 with the code's pooled detrending). Over the whole mixed block, initiation is slower after high than after low blocks (+0.048 against -0.102 z, 290 of 291 rats, signed-rank p = 1.8e-49; with pooled detrending 291 rats, p = 1.8e-49).",
"suppfig5-mixed-to-adaptation-transitions": "**Result: reproduced.** In the mixed block before a transition, initiation times are higher before low blocks than before high blocks by +0.046 z (+0.059 with pooled detrending), and the wait time curves differ there by 0.125 of their post-transition gap, against 0.197 (0.239) for initiation times.",
"suppfig6-results-without-detrending": "**Result: reproduced.** Without detrending the high-to-mixed initiation curve lies above the low-to-mixed curve over trials 1-20 by +0.246 z, and the mixed-block test gives +0.094 against -0.085 z, p = 1.8e-49. The median per-session trend of z-scored initiation time is 0.069 z per 100 trials.",
"fig2c-d-regression-on-previous-rewards": "**Result: reproduced.** The current offer coefficient for wait time is 0.212 (95% interval across rats 0.205 to 0.219), larger than every previous offer coefficient (largest 0.013 in size). The initiation time coefficients 1, 2 and 3 trials back are -0.029, -0.024 and -0.012 with 9 lags, and the same to three decimals with 10.",
"fig2e-tau-differ": "**Result: reproduced.** Under the Methods reading the mean tau is 0.065 for wait times (0 in 249 of 291 rats) and 1.875 for initiation times, signed-rank p = 3.5e-45; under the code reading 0.620 and 1.914, p = 2.7e-35. Six initiation taus (seven under the code reading) sit at the upper bound of 10.",
"fig2f-tau-uncorrelated": "**Result: reproduced.** The taus are not correlated: r = -0.037, p = 0.535 under the Methods reading (the legend prints r = -0.03, p = 0.53) and r = 0.111, p = 0.059 under the code reading.",
"fig2g-h-fast-slow-tau-groups": "**Result: reproduced.** The 20th and 80th percentiles give 58 rats per group (116 in all, as in the paper). With the code's coefficients the initiation time p is 0.000 under all five seeds and the wait time p is 0.203 to 0.217; with the Methods' coefficients 0.000 and 0.394.",
"fig2j-wait-time-not-sensitive-to-previous-offer": "**Result: reproduced.** 38 of 291 rats have p < 0.05 (expected 38 +- 4; the other 253 are the paper's count), and the population rank-sum on per-rat means gives p = 0.575 (signed-rank variant p = 0.629).",
"fig2k-initiation-sensitive-to-previous-offer": "**Result: reproduced, under the code's reading.** With all mixed block trials (latency_post20ul_by_previous_vol.m), 256 rats have p < 0.05 (expected 256 +- 26), 255 of them slower after small offers, and the population is slower after small offers (+0.091 against -0.148 z; rank-sum p = 9.9e-97, signed-rank p = 1.9e-49). With the Methods' 20 uL trials, 276 rats have p < 0.05 but only 17 in the claimed direction, and the population is faster after small offers (-0.161 against -0.094 z).",
"fig2l-sensitivity-greater-for-initiation": "**Result: reproduced, under the code's reading of fig2k.** Initiation time sensitivity (+0.239) exceeds wait time sensitivity (-0.009) in 245 of 291 rats, signed-rank p = 1.6e-36. Under the Methods' reading of fig2k the initiation time sensitivity is negative (-0.067) and below the wait time sensitivity (103 of 291 rats above it), though the test gives p = 2.2e-06.",
"fig3c-wait-time-by-catch-probability": "**Result: reproduced.** Counting each rat at every probability it has data at (reading A), the cohorts are 3, 188, 61, 151 and 40 rats at 0.1, 0.15, 0.2, 0.25 and 0.35, all within tolerance, and wait times fall from 0.15 to 0.2 to 0.25 at all 5 offers. Assigning each rat to its main probability (reading B) gives 105, 43 and 128 rats at 0.15 to 0.25 and a fall at 3 of 5 offers. Eight rats have data at a probability of 0.3, which the paper does not list.",
"bayes-observer-offer-reduces-uncertainty": "**Result: reproduced.** Under both readings the posterior is less uncertain than the prior: the variance of the block probabilities rises from 0.157 to 0.169, and the variance of the block value falls from 0.104 to 0.082 (per-rat means, signed-rank p = 1.8e-49 for each; over trials, p < 0.001 in all 291 rats).",
"pre-cue-session-link": "**Result: partially reproduced.** 14 of the 16 rats are linked by the test; S042 and S050 are not (ANOVA p = 0.151 and 0.597 after the date). The files mark the pre-cue sessions themselves: the task argument `center_port_cue` is True only in sessions of these 16 rats, and on those sessions every one of them has a negative slope of initiation time on offer (-0.0084 to -0.0690), against -0.0076 to +0.0043 where it is False or absent. Some sessions after Figure5.m's dates are not flagged (S042 13 of 25, S050 6 of 11, E005 15 of 21).",
"fig5b-pre-cue-initiation-sensitive-to-offer": "**Result: reproduced, under the code's session reading.** From Figure5.m's dates on (reading b), the population mean z-scored initiation time falls at every step from 5 to 80 uL (-0.041 to -0.178), and 14 of 16 rats reach ANOVA p < 0.05, against 0 of 12 on the original task. After 30 pre-cue sessions (reading a; 11 rats have such sessions) all 11 reach p < 0.05, but the mean rises from 5 to 10 uL (0.016 to 0.024).",
"fig5c-pre-cue-initiation-still-sensitive-to-previous-reward": "**Result: reproduced, under the code's readings.** With sessions from the dates and all mixed block trials, 12 of 16 rats have p < 0.05 (expected 13 +- 1; 11 slower after small offers), and the population is slower after small offers (+0.065 against -0.128 z; rank-sum p = 4.7e-06). The Methods' 20 uL reading gives 15 of 16 rats but a population that is faster after small offers (rank-sum p = 0.337); after 30 pre-cue sessions only 11 rats have data, 9 of them significant (rank-sum p = 6.4e-04).",
"fig5d-pre-cue-initiation-depends-on-previous-block": "**Result: reproduced.** With sessions from the dates (reading b), initiation over trials 1-20 of mixed blocks is higher after high blocks (+0.136) than after low blocks (-0.114) in all 16 rats, signed-rank p = 3.1e-05; after 30 pre-cue sessions (reading a) in all 11 rats with data, p = 9.8e-04.",
"fig4a-wait-time-block-sensitivity-emerges": "**Result: partially reproduced.** Initiation times are block sensitive from the first session pair (ratio 0.802 over 273 rats, signed-rank against 1 p = 5.8e-16), and the wait time block coefficient grows in size from -0.432 over sessions 1-10 to -0.706 over sessions 41-50 (linear offer: -0.393 to -0.633). The wait time ratio of the first pair is 1.187, further from 1 than its mean over pairs 16-25 (0.936), so part (2) of the criterion fails: the early ratio lies on the other side of 1, and the ratio falls to about 0.92 by the last pairs.",
"fig4c-initiation-previous-reward-stable": "**Result: reproduced.** The previous reward coefficient is -0.588 over sessions 1-10 and -0.469 over sessions 41-50, the same sign, a relative change of 0.252 against 0.389 for the wait time block coefficient.",
"fig4d-overshoot-grows-with-training": "**Result: reproduced.** The overshoot after high-to-mixed transitions is 0.025 z in the first 10 and 0.046 z in the last 10 final-stage sessions. Per 5-session chunk it goes from 0.008 to about 0.06 over the first 100 sessions (smoothed, 0.008 to 0.055).",
"fig3j-inferential-beats-retrospective-for-wait-times": "**Result: reproduced (resting on the fitting assumptions).** Under the claim's seed the inferential model is better than the retrospective model by BIC (mean difference -1040, 290 of 291 rats, p = 3.6e-48), AIC (-1052, p = 3.6e-48) and cross-validated nLL (-454, 284 rats, p = 5.6e-44); under the four other seeds all three give p < 1e-43. The best-fold test nLL variant agrees (p = 4.5e-18).",
"suppfig8-belief-state-not-distinguished": "**Result: reproduced under the claim's seed (resting on the fitting assumptions; seed sensitive).** Under the claim's seed no test reaches p < 0.05 (BIC and AIC p = 0.163, cross-validated nLL p = 0.569). Under seed +3000 BIC and AIC give p = 0.0305, with the inferential model better in 125 of 291 rats by a mean of +2.81 units; the other seeds give p = 0.068 to 0.997.",
"fig3f-inferential-model-not-sensitive-to-previous-offer": "**Result: not reproduced (resting on the fitting assumptions; seed sensitive).** Under the claim's seed the model's 20 uL wait times are longer after offers below 20 uL (sensitivity +0.048 z, rank-sum p = 3.8e-05), while the rats' are not (-0.009, p = 0.575). Under the four other draws p is 0.332, 4.3e-07, 1.5e-05 and 4.0e-04.",
"suppfig9-wait-times-reflect-misinferences": "**Result: reproduced.** On mixed block 20 uL catch trials, rats wait 10.85 s on trials the model labels high and 11.90 s on trials it labels low (230 of 291 rats shorter on high; signed-rank p = 9.7e-23).",
"fig3i-retrospective-model-captures-initiation": "**Result: partially reproduced.** The Equation 10 model at alpha0 = 0.1042 shows both an overshoot (0.200 z) and a persistent gap (+1.398 z over trials 10-20), and its initiation times, simulated with each rat's fitted parameters, are slower after offers below 20 uL (+0.015 against -0.009 z, 232 of 291 rats, p = 1.8e-29). The static and |delta| models lack both at alpha0 = 0.05, but at 0.4 and 0.8 each shows a small overshoot (0.0002 to 0.0058 z, at most 1/30 of the Equation 10 model's) and a gap, so by the criterion's rule they are not excluded at every alpha0. Noise of variance 8 gives the same pattern.",
"fig3l-lambda-groups-wait-time-dynamics": "**Result: reproduced under the Results' reading (resting on the lambda fit, an assumption).** With the 20/80 split (58 rats per group), the wait time slope C differs at mixed to low (p = 0.009) and at mixed to high (p = 0.026), and the initiation time tests of those parameters do not reach p < 0.05 (0.147 and 0.339); over the five seeds the wait time p ranges 0.009-0.018 and 0.026-0.039. The legend's reading, the right asymptote D at mixed to high, gives p = 0.120 for wait time and does not hold. The 40/60 split of Figure3.m gives p = 0.391 for C at mixed to low.",
}
for f in sorted(glob.glob("c*.py")):
    s = open(f).read()
    parts = re.split(r"(^#%% md\n## )", s, flags=re.M)
    out = parts[0]
    for i in range(1, len(parts), 2):
        sec = parts[i + 1]
        cid = sec.split("\n", 1)[0].strip()
        if cid in C:
            sec, n = re.subn(r"\*\*Result: [^\n]*", C[cid].replace("\\", "\\\\"), sec, count=1)
            if n == 0:
                sec = sec.rstrip("\n") + "\n\n#%% md\n" + C[cid] + "\n\n"
        out += parts[i] + sec
    open(f, "w").write(out)
missing = [k for k in C if not any(C[k][:40] in open(f).read() for f in glob.glob("c*.py"))]
print("not placed:", missing)
PYEOF
python3 concl.py; grep -c "Result: see" c*.py
```

```
Exit code 1
174:cells = diff.stack().dropna()
not placed: []
c1.py:0
c10.py:0
c11.py:0
c2.py:0
c3.py:0
c4.py:0
c5.py:0
c6.py:0
c6b.py:0
c7.py:0
c8.py:0
c9.py:0
concl.py:0
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
def show(d,ind=0,depth=0):
    if depth>4: return
    if isinstance(d,dict):
        if 'properties' in d:
            print(' '*ind+'required:',d.get('required'))
            for k,v in d['properties'].items():
                print(' '*ind+k, v.get('type',''), (v.get('enum') or ''), (v.get('description','')[:150]))
                if v.get('type')=='object' or 'items' in v: show(v.get('items',v),ind+2,depth+1)
show(s)
EOF
```

```
required: ['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
schema_version   
id string  
datasets array  Every dataset the attempt used (docs/protocol.md, "Record the attempt").
  required: ['archive', 'id', 'version', 'relation']
  archive string  The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.
  id string  The dataset's identifier in that archive, e.g. 000003 on DANDI.
  version string  The version the attempt read, e.g. 0.220127.0436, or draft.
  modified string  For a version that can still change, such as a draft, when the archive says it was last modified. A published version is fixed and needs none; it usua
  doi string  The DOI of the version read, when it has one: an identifier that holds across archives.
  relation  ['primary', 'reuses'] primary: the data the paper was published with; reuses: data the paper reuses from another study.
missing_datasets array  Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.
  required: ['why']
  archive string  
  id string  
  name string  
  why string  
paper string  
date string  
entry string  The entry this attempt produced (its name), if any.
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > hA.py <<'EOF'
#%% md
# Reproducing Mah et al. (2023) from DANDI:001169: behaviour

Paper: Mah, Schiereck, Bossio and Constantinople (2023), "Distinct value computations support rapid sequential decisions", Nature Communications 14, 7573, doi:10.1038/s41467-023-43250-x.

Dataset: DANDI:001169, version 0.261120.1450 (doi:10.48324/dandi.001169/0.261120.1450). This version was asked for by the prompt of this repeat attempt; it is the most recent published version (published 2026-11-20). The paper cites no dandiset version: its Data availability names the Zenodo deposit doi:10.5281/zenodo.10031483, which this notebook reads for Figure 4 only (all final-stage sessions, which the dandiset does not hold).

Claims file: `claims/mah-2023.yaml`, written from the version of record (Europe PMC, PMC10663503) with Supplementary Information, peer review file and reporting summary, and the paper's code (github.com/constantinoplelab/published, rat_behavior, at b7b68ca8c107). Method details the claims file lacks are cited to the paper or that code where they are used.

The NWB files are streamed: each file is fetched over HTTPS into memory and read with h5py; nothing is written to disk.

Claims, and where they are tested (all 33 are tested; none is blocked):

| Claim | Notebook | Data |
|---|---|---|
| cohort-size, fig1e, fig1f, fig1i, suppfig2, suppfig3, suppfig12, suppfig14 | this one | dandiset |
| fig2a, suppfig5, suppfig6, fig2c-d, fig2e, fig2f, fig2g-h, fig2j, fig2k, fig2l | this one | dandiset |
| fig3c, bayes-observer-offer-reduces-uncertainty | this one | dandiset |
| pre-cue-session-link, fig5b, fig5c, fig5d | this one | dandiset, with rat names and dates from Figure5.m |
| fig4a, fig4c, fig4d | this one | the paper's Zenodo deposit (A_Structs_all) |
| fig3j, suppfig8, fig3f, suppfig9, fig3i, fig3l | `models_mah_2023.ipynb` | dandiset |

#%% md
## Data check

The cell below prints what was loaded and checks the description against the values.
EOF
cat > hB.py <<'EOF'
#%% md
# Reproducing Mah et al. (2023) from DANDI:001169: models

Paper: Mah, Schiereck, Bossio and Constantinople (2023), "Distinct value computations support rapid sequential decisions", Nature Communications 14, 7573, doi:10.1038/s41467-023-43250-x.

Dataset: DANDI:001169, version 0.261120.1450 (doi:10.48324/dandi.001169/0.261120.1450), the version this repeat attempt's prompt asked for and the most recent published one. Claims file: `claims/mah-2023.yaml` (version of record with its supplement, and the paper's code at b7b68ca8c107). The data check, and the claims on behaviour alone, are in `reproduce_mah_2023.ipynb`; this notebook holds the claims that need the wait time models or simulations of the initiation time models, which take most of the run time.

| Claim | Tested here |
|---|---|
| fig3j-inferential-beats-retrospective-for-wait-times | yes |
| suppfig8-belief-state-not-distinguished | yes |
| fig3f-inferential-model-not-sensitive-to-previous-offer | yes |
| suppfig9-wait-times-reflect-misinferences | yes |
| fig3i-retrospective-model-captures-initiation | yes |
| fig3l-lambda-groups-wait-time-dynamics | yes |

#%% md
## Data check

The same loading as the first notebook; its data check is repeated here in short.
EOF
cat > sA.py <<'EOF'
#%% md
## Summary

| Claim | Outcome |
|---|---|
| cohort-size | reproduced |
| fig1e-wait-time-increases-with-reward | reproduced |
| fig1f-wait-time-block-effect | reproduced |
| fig1i-initiation-block-effect | reproduced |
| suppfig2-initiation-block-effect-after-unrewarded | reproduced |
| suppfig3-wait-time-not-affected-by-previous-outcome | reproduced |
| fig2a-wait-time-converges-in-mixed-blocks | reproduced |
| suppfig5-mixed-to-adaptation-transitions | reproduced |
| fig2c-d-regression-on-previous-rewards | reproduced |
| fig2e-tau-differ | reproduced |
| fig2f-tau-uncorrelated | reproduced |
| fig2g-h-fast-slow-tau-groups | reproduced |
| fig2j-wait-time-not-sensitive-to-previous-offer | reproduced |
| fig2k-initiation-sensitive-to-previous-offer | reproduced (code's reading of the trials) |
| fig2l-sensitivity-greater-for-initiation | reproduced (code's reading of fig2k) |
| suppfig6-results-without-detrending | reproduced |
| fig3c-wait-time-by-catch-probability | reproduced |
| bayes-observer-offer-reduces-uncertainty | reproduced |
| fig4a-wait-time-block-sensitivity-emerges | partially reproduced |
| fig4c-initiation-previous-reward-stable | reproduced |
| fig4d-overshoot-grows-with-training | reproduced |
| fig5b-pre-cue-initiation-sensitive-to-offer | reproduced (code's session reading) |
| fig5c-pre-cue-initiation-still-sensitive-to-previous-reward | reproduced (code's readings) |
| fig5d-pre-cue-initiation-depends-on-previous-block | reproduced |
| suppfig12-no-sex-differences | reproduced |
| suppfig14-contextual-effects-without-threshold | reproduced |
| pre-cue-session-link | partially reproduced |

The model claims are in `models_mah_2023.ipynb`.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's:
- The dandiset holds only the sessions that pass the inclusion criterion; they are used as given. Figure 4 is tested on the paper's Zenodo deposit, which holds all final-stage sessions.
- Lags and previous trials are taken within a session; the paper's code concatenates sessions.
- Exponential and logistic fits are global grid searches in place of fmincon from random starts.
- For fig2k, fig2l, fig5b and fig5c the Methods and the code describe different trials or sessions; every reading is shown, and the outcome holds under the code's reading only.
- Figure 5's pre-cue sessions come from the rat names and dates of Figure5.m; the files also flag them (`center_port_cue`).

What was found about the dataset:
- Counts match the paper exactly: 291 rats (184 male, 107 female), median 33,493 trials and 71 sessions per rat.
- Only included sessions are deposited (the paper's deposit has a median of 95 final-stage sessions per rat, the dandiset 71); nothing in the dandiset says so.
- `wait_time_threshold` is the mean + 1 SD of all catch trials with a wait time, timed-out catch trials (100 s) included, where the description says catch-trial wait times.
- The task argument `center_port_cue`, which has no description, marks the pre-initiation cue sessions; it is True only for the 16 rats of Figure 5.
- Catch probability 0.3, which the paper does not list, occurs for 8 rats; two sessions go directly between high and low blocks.
EOF
cat > sB.py <<'EOF'
#%% md
## Summary

| Claim | Outcome |
|---|---|
| fig3j-inferential-beats-retrospective-for-wait-times | reproduced, resting on the fitting assumptions |
| suppfig8-belief-state-not-distinguished | reproduced, resting on the fitting assumptions; seed sensitive |
| fig3f-inferential-model-not-sensitive-to-previous-offer | not reproduced, resting on the fitting assumptions; seed sensitive |
| suppfig9-wait-times-reflect-misinferences | reproduced |
| fig3i-retrospective-model-captures-initiation | partially reproduced |
| fig3l-lambda-groups-wait-time-dynamics | reproduced under the Results' reading, resting on the lambda fit |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the paper's fitting code is not public, so the bounds, the number of starts (2 here, 100 in the paper), the folds (random over sessions) and the choice of the cross-validated nLL are this attempt's; the models themselves follow the Methods and the paper's generative code. The lambda model is fitted once on all data from one start, without cross-validation. Simulated initiation times use the normal approximation to the mean of 50 log-normal draws. The paper's deposited fits on Zenodo were not used.
EOF
cat > sanB.py <<'EOF'
#%% code sanity
print("Dandiset", M.DANDISET, "version", M.VERSION, "| assets:", len(assets))
print("sessions:", len(sessions), "| rats:", sessions.subject.nunique(), "| trials:", len(t))
print("opt-out catch trials with a wait time:", int(t.wt.notna().sum()), "| range (s):", t.wt.min(), "-", t.wt.max())
print("trials with a wait time (model trials):", int(t.wait_time.notna().sum()))
print("catch probability values:", sorted(t.catch_percentage.unique()), "| offered volumes:", sorted(t.reward_volume_ul.unique()))
EOF
python3 - <<'EOF'
# notebook B uses c1 without its long sanity cell
import re
s=open('/tmp/claude-1001/nb/c1.py').read()
i=s.index('#%% code sanity')
open('/tmp/claude-1001/nb/c1B.py','w').write(s[:i])
EOF
ls
```

```
build.py
c1.py
c10.py
c11.py
c1B.py
c2.py
c3.py
c4.py
c5.py
c6.py
c6b.py
c7.py
c8.py
c9.py
concl.py
dev.py
hA.py
hB.py
prepB.py
sA.py
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/two sessions go directly between high and low blocks/two transitions go directly between high and low blocks/' sA.py && python3 - <<'EOF'
p='/tmp/claude-1001/nb/c1B.py'
s=open(p).read()
s=s.replace("#%% code\nimport zlib, time, resource","#%% code\nimport os\nfor v in [\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"]:\n    os.environ[v] = \"1\"  # many small fits in parallel processes: one linear-algebra thread each\nimport zlib, time, resource",1)
open(p,'w').write(s)
p='/tmp/claude-1001/nb/c8.py'
s=open(p).read()
s=s.replace('import os\nos.environ.setdefault("OMP_NUM_THREADS", "1")\n','')
open(p,'w').write(s)
EOF
head -5 c1B.py; cd $TMPDIR && . dev/bin/activate && E=entries/mah-2023 && python nb/build.py $E/reproduce_mah_2023.ipynb nb/hA.py nb/c1.py nb/c2.py nb/c3.py nb/c4.py nb/c5.py nb/c9.py nb/c6.py nb/c6b.py nb/c7.py nb/sA.py && python nb/build.py $E/models_mah_2023.ipynb nb/hB.py nb/c1B.py nb/sanB.py nb/prepB.py nb/c8.py nb/c10.py nb/c11.py nb/sB.py && python - <<'EOF'
import nbformat
for f in ['reproduce_mah_2023','models_mah_2023']:
    nb=nbformat.read(f'entries/mah-2023/{f}.ipynb',4)
    tags=[t for c in nb.cells for t in c.metadata.get('tags',[])]
    print(f, len(nb.cells), sorted(set(tags)))
    print([c.source[:60] for c in nb.cells if c.cell_type=='markdown' and c.source.startswith('**Result')].__len__())
EOF
date -u
```

```
#%% code
import os
for v in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[v] = "1"  # many small fits in parallel processes: one linear-algebra thread each
import zlib, time, resource
reproduce_mah_2023 91 ['claim:bayes-observer-offer-reduces-uncertainty', 'claim:cohort-size', 'claim:fig1e-wait-time-increases-with-reward', 'claim:fig1f-wait-time-block-effect', 'claim:fig1i-initiation-block-effect', 'claim:fig2a-wait-time-converges-in-mixed-blocks', 'claim:fig2c-d-regression-on-previous-rewards', 'claim:fig2e-tau-differ', 'claim:fig2f-tau-uncorrelated', 'claim:fig2g-h-fast-slow-tau-groups', 'claim:fig2j-wait-time-not-sensitive-to-previous-offer', 'claim:fig2k-initiation-sensitive-to-previous-offer', 'claim:fig2l-sensitivity-greater-for-initiation', 'claim:fig3c-wait-time-by-catch-probability', 'claim:fig4a-wait-time-block-sensitivity-emerges', 'claim:fig4c-initiation-previous-reward-stable', 'claim:fig4d-overshoot-grows-with-training', 'claim:fig5b-pre-cue-initiation-sensitive-to-offer', 'claim:fig5c-pre-cue-initiation-still-sensitive-to-previous-reward', 'claim:fig5d-pre-cue-initiation-depends-on-previous-block', 'claim:pre-cue-session-link', 'claim:suppfig12-no-sex-differences', 'claim:suppfig14-contextual-effects-without-threshold', 'claim:suppfig2-initiation-block-effect-after-unrewarded', 'claim:suppfig3-wait-time-not-affected-by-previous-outcome', 'claim:suppfig5-mixed-to-adaptation-transitions', 'claim:suppfig6-results-without-detrending', 'load', 'sanity']
27
models_mah_2023 29 ['claim:fig3f-inferential-model-not-sensitive-to-previous-offer', 'claim:fig3i-retrospective-model-captures-initiation', 'claim:fig3j-inferential-beats-retrospective-for-wait-times', 'claim:fig3l-lambda-groups-wait-time-dynamics', 'claim:suppfig8-belief-state-not-distinguished', 'claim:suppfig9-wait-times-reflect-misinferences', 'load', 'sanity']
6
Wed Nov 25 00:28:38 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python3 - <<'EOF'
p='c2.py'; s=open(p).read()
s=s.replace("**Result: reproduced.** The population mean wait time in mixed blocks rises at every step from 5 to 80 uL (values printed above).","**Result: reproduced.** The population mean wait time on mixed block catch trials rises at every step from 5 to 80 uL (10.45, 10.77, 11.11, 13.03 and 13.81 s); 171 of 291 rats rise at every step on their own.")
open(p,'w').write(s)
EOF
E=entries/mah-2023
cat > $E/entry.yaml <<'EOF'
schema_version: 1
name: mah-2023
type: reproduction
title: Distinct value computations for rapid sequential decisions in rats (Mah et al. 2023)
description: Tests the findings of Mah, Schiereck, Bossio and Constantinople (2023) on dandiset
  001169, which holds the final-stage behaviour of the paper's 291 rats in a temporal wagering
  task with hidden reward blocks. It compares wait times and trial initiation times across blocks,
  their dynamics at block transitions, their dependence on previous rewards, the wait time models
  and simulations of the initiation time models, and the pre-initiation cue task. Figure 4, which
  needs the sessions that fail the inclusion criterion, is tested on the paper's Zenodo deposit.
license: Apache-2.0
notebooks:
- path: reproduce_mah_2023.ipynb
  title: Reproducing Mah et al. (2023) from dandiset 001169, behaviour
  runtime_minutes: 15
- path: models_mah_2023.ipynb
  title: Reproducing Mah et al. (2023) from dandiset 001169, models
  runtime_minutes: 35
helpers:
- mah2023.py
related:
- id: dandi:001169/0.261120.1450
  relation: uses_data
- id: doi:10.5281/zenodo.10031483
  relation: uses_data
- id: doi:10.1038/s41467-023-43250-x
  relation: reproduces
EOF
printf "aiohttp\nfsspec\nh5py\nmatplotlib\nnumba\nnumpy\npandas\nscipy\n" > $E/requirements.in
cat > $E/README.md <<'EOF'
# Mah et al. (2023) on DANDI:001169

Tests the claims of Mah, Schiereck, Bossio and Constantinople (2023), "Distinct value computations
support rapid sequential decisions", Nature Communications 14, 7573
(doi:10.1038/s41467-023-43250-x), on dandiset 001169 at version 0.261120.1450.

- `reproduce_mah_2023.ipynb`: the data check and the behavioural claims (Figures 1, 2, 3c, 4, 5
  and the Supplementary Figures). Figure 4 reads the paper's Zenodo deposit
  (doi:10.5281/zenodo.10031483), which holds the sessions that fail the inclusion criterion.
- `models_mah_2023.ipynb`: the wait time models (Figure 3j, 3f, 3l, Supplementary Figures 8 and 9)
  and simulations of the initiation time models (Figure 3i).
- `mah2023.py`: loading (each NWB file is fetched into memory and read with h5py) and the shared
  measures and models.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.
EOF
cd $TMPDIR && . dev/bin/activate && python nb/build.py $E/reproduce_mah_2023.ipynb nb/hA.py nb/c1.py nb/c2.py nb/c3.py nb/c4.py nb/c5.py nb/c9.py nb/c6.py nb/c6b.py nb/c7.py nb/sA.py && cat entries/fouke-2025/requirements.lock.txt | head -3; cd  && sed -n 1,60p tools/entry.py | grep -n "lock\|python" | head
```

```
# This file was autogenerated by uv via the following command:
#    uv pip compile --python-version 3.13 requirements.in -o requirements.lock.txt
acres==0.5.0
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
10:`lock` compiles the entry's requirements.in (direct dependencies only) into
11:requirements.lock.txt with every version pinned.
19:- the lock file is present and newer requirements are not left unlocked;
25:`run` builds a fresh virtual environment from the lock file and executes each
```

**Agent calls Bash**

```bash
rm -rf entries/mah-2023/__pycache__ && python tools/entry.py lock entries/mah-2023 2>&1 | tail -5 && python tools/entry.py check entries/mah-2023 2>&1 | tail -20
```

```
wrote mah-2023/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/mah-2023 && sed -i 's/@njit(cache=True)/@njit/' mah2023.py && python3 - <<'EOF'
s=open('mah2023.py').read()
s=s.replace('''    _T = {r: g for r, g in trials[cols].groupby("subject") if r in set(rats)}
''','''    _T = {r: g for r, g in trials[cols].groupby("subject") if r in set(rats)}
    # compile the numba functions once, before the workers are forked
    belief_filter(np.zeros(2, np.int64), np.array([True, False]), 1.0, np.array([0.5, 0.25, 0.25]))
    retro_kappa(np.zeros(2), np.array([True, False]), np.ones(2), 0.1, 0, 1.0)
''')
open('mah2023.py','w').write(s)
EOF
grep -n "njit\|compile the numba" mah2023.py; rm -rf __pycache__; cd ../.. && date -u && python tools/entry.py all entries/mah-2023 2>&1 | tail -20; date -u
```

```
408:from numba import njit
414:@njit
442:@njit
602:    # compile the numba functions once, before the workers are forked
Wed Nov 25 00:29:11 UTC 2026
Installed kernelspec registry-mah-2023 in executed/mah-2023/.venv/share/jupyter/kernels/registry-mah-2023
0 error(s)
pass  reproduce_mah_2023.ipynb  (822 s)
pass  models_mah_2023.ipynb  (2766 s)
Wed Nov 25 01:29:18 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/mah-2023/; python3 - <<'EOF'
import nbformat
for f in ['reproduce_mah_2023','models_mah_2023']:
    nb=nbformat.read(f'executed/mah-2023/{f}.ipynb',4)
    for c in nb.cells:
        if c.cell_type!='code': continue
        txt=''.join(o.get('text','') for o in c.get('outputs',[]) if o.get('output_type')=='stream')
        err=[o for o in c.get('outputs',[]) if o.get('output_type')=='error']
        if err: print('ERROR', c.source[:80])
        if f=='models_mah_2023' or any(k in c.source for k in ['load_all','claim:cohort','fig4d','PRECUE_RATS =','precue_mask(reading)','overshoot_curve']):
            print('=====', c.metadata.get('tags'), '\n', txt[:3000])
EOF
```

```
models_mah_2023.ipynb
reproduce_mah_2023.ipynb
result.json
===== ['load'] 
 loaded 23033 sessions, 10408699 trials in 515 s

===== ['claim:pre-cue-session-link'] 
 rats with any center_port_cue = True session: ['E005', 'E008', 'G069', 'G070', 'G076', 'G078', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'S042', 'S050']
of them in Figure5.m's list: ['E005', 'E008', 'G069', 'G070', 'G076', 'G078', 'M041', 'M042', 'M043', 'M044', 'M045', 'M046', 'M047', 'M048', 'S042', 'S050']
         sessions  before_date  after_date  flag_true  after_and_flag first_flag_day       date
subject                                                                                        
E005           80           59          21         15              15     2022-11-07 2022-10-24
E008          152           78          74         73              73     2022-10-25 2022-10-24
G069          202          127          75         75              75     2022-11-14 2022-11-14
G070          106           69          37         37              37     2022-10-25 2022-10-24
G076          108           53          55         54              54     2022-11-15 2022-11-14
G078          129          102          27         26              26     2022-11-08 2022-11-07
M041           98           64          34         33              33     2022-10-05 2022-10-04
M042           76           62          14         13              13     2022-10-05 2022-10-04
M043          119           58          61         60              60     2022-10-05 2022-10-04
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat,re
nb=nbformat.read('executed/mah-2023/reproduce_mah_2023.ipynb',4)
txt='\n'.join(''.join(o.get('text','') for o in c.get('outputs',[]) if o.get('output_type')=='stream') for c in nb.cells if c.cell_type=='code')
for k in ['trials_in_stage','first 50 trial','threshold recomputed','timed out','hit trials','peak memory','rats with p < 0.05: ','[C: all mixed','(1) first pair','(2) wait','(3) block','previous reward coefficient','wait time block coefficient relative','final-stage sessions per rat','final-stage trials','loaded 1343','A: offers','reading (i)','reading (ii)','linked rats','[methods] r =','fig2a','part 2 [iti_dt_sess]','cells with longer']:
    for line in txt.split('\n'):
        if k in line: print(line[:300])
EOF
```

```
trials_in_stage at each rat's first deposited session: median 1543.0 | between consecutive deposited sessions, counter gap > 5 trials in 2586 of 22742 pairs; rats with any such gap: 284
sessions whose first 50 trial start times and offers equal another session's: 0
threshold recomputed from opt-out catch trials: median |diff| from deposited = 5.189 s; max 17.588
threshold recomputed from all catch trials with a wait time (timed-out ones included): median |diff| from deposited = 0.0 s; max 0.184
catch trials neither opt-out nor violation (timed out): 16086 | their unthresholded wait time median 100.0
hit trials: wait_time equals reward_delay in 1.0
peak memory (GB): 5.191444
peak memory so far (GB): 9.731268
per-rat one-tailed rank-sum (high shorter), rats with p < 0.05: 244 of 291
per-rat two-tailed rank-sum, rats with p < 0.05: 248
rats with p < 0.05: 38 of 291 (expected 38 +- 4); not significant: 253
[C: all mixed trials] rats p < 0.05: 256 (expected 256 +- 26), of which slower after small offers 255; mean z after < 20 +0.0910, after > 20 -0.1477; rank-sum p = 9.94e-97; signed-rank p = 1.86e-49
[C: all mixed trials] mean sensitivity initiation +0.2387, wait time -0.0094; rats initiation > wait 245 of 291; signed-rank p = 1.6e-36
(1) first pair initiation ratio: mean 0.802, n 273, signed-rank against 1 p = 5.77e-16
(2) wait time ratio first pair 1.187 (|1 - r| = 0.187); mean over pairs 16-25 0.936 (|1 - r| = 0.064)
(3) block coefficient (log2 reward): sessions 1-10 -0.4315, sessions 41-50 -0.7057; grows in size: True
(3) block coefficient (linear reward): sessions 1-10 -0.3930, sessions 41-50 -0.6325; grows in size: True
previous reward coefficient: sessions 1-10 -0.5876, 41-50 -0.4693; same sign: True; relative change 0.252
wait time block coefficient relative change 0.389; initiation change smaller: True
final-stage sessions per rat: deposit median 95 (range 18-264), dandiset median 71; rats with more sessions in the deposit than the dandiset: 269, fewer: 22
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
NB_A = "reproduce_mah_2023.ipynb"; NB_B = "models_mah_2023.ipynb"
FIT_DEV = ("The paper's fitting code is not public. The models follow the Methods (Equations 1, 3 to 10) and the "
           "generative functions of the paper's repository (BehavioralModel/, b7b68ca8c107); this attempt chose the "
           "parameter bounds (k in [0.01, min(0.999/C, 5)], D-scale in [0.01, 10], alpha0 in [0.001, 1]), 2 random "
           "starts of L-BFGS-B in place of 100 fmincon starts, 5 folds over sessions drawn at random, and the summed "
           "test nLL as the cross-validated nLL; the best-fold parameters (Zenodo README) give BIC and AIC on all data. "
           "These are assumptions, chosen as the simplest reading of the Methods and the README.")
def o(claim, outcome, notes, nb=NB_A, deviations=None, measured=None, assumed=None, seed=None):
    d = {"claim": claim, "outcome": outcome, "notebook": nb, "output": f"claim:{claim}"}
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    if assumed: d["assumed"] = True
    if seed: d["seed_sensitive"] = True
    return d
WITHIN = "Previous trials and lags are taken within the session; the paper's code concatenates sessions, which differs only at session starts."
outcomes = [
o("cohort-size", "reproduced", "291 rats; median 33,493 trials and 71 sessions per rat, the paper's numbers exactly (ranges 5,266 to 129,864 trials and 15 to 232 sessions).", measured=[291, 33493, 71],
  deviations=["Counted over the deposited sessions, which are the sessions that pass the inclusion criterion (data check)."]),
o("fig1e-wait-time-increases-with-reward", "reproduced", "Population mean wait time on mixed block opt-out catch trials 10.45, 10.77, 11.11, 13.03 and 13.81 s for 5 to 80 uL; 171 of 291 rats rise at every step on their own."),
o("fig1f-wait-time-block-effect", "reproduced", "Mean ratio high over low 0.894 (median 0.890; 279 of 291 rats below 1). Signed-rank p = 4.6e-47 on z-scored means (Methods) and 8.2e-47 on raw means (Figure1.m); the paper prints 8.26e-49. 244 of 291 rats have per-rat one-tailed rank-sum p < 0.05.", measured=[0.894]),
o("fig1i-initiation-block-effect", "reproduced", "Mean ratio high over low 0.568, below 1 in all 291 rats; signed-rank p = 1.8e-49 on z-scored and on raw means (the paper prints 1.82e-49). 248 rats have per-rat rank-sum p < 0.05."),
o("suppfig2-initiation-block-effect-after-unrewarded", "reproduced", "After unrewarded trials high minus low is -0.359 z, all 291 rats faster in high blocks, two-tailed p = 1.8e-49, one-tailed p = 9.0e-50 (paper 9.07e-50). After rewarded trials the one-tailed test gives p = 1 (paper 1); the two-tailed test finds a small difference the other way (+0.018 z, p = 8.5e-10). All trials give one-tailed p = 9.0e-50 (paper 9.17e-50), which supports the claims file's note that the legend's tests are one-tailed.",
  deviations=[WITHIN]),
o("suppfig3-wait-time-not-affected-by-previous-outcome", "reproduced", "Mean ratio 0.899 after rewarded and 0.897 after unrewarded trials; difference 0.002, signed-rank p = 0.63 (variant)."),
o("fig2a-wait-time-converges-in-mixed-blocks", "reproduced", "Gap between the high-to-mixed and low-to-mixed curves over trials 1-20 relative to trials -20 to -1, wait time 0.341, initiation time 1.90 (trials 10-20, 0.086 and 2.10; with the code's pooled detrending 2.22 and 2.45). Mixed block initiation after high +0.048 z, after low -0.102 z, 290 of 291 rats, signed-rank p = 1.8e-49 (pooled detrending 291 rats, p = 1.8e-49).",
  deviations=["Transition windows are kept within the session; the code indexes the concatenated sessions. The code's overwrite of the transition trial's value with a neighbour (a plotting step) is left out.", "Each rat's curve is smoothed with a centred 10-trial moving average; Matlab's smooth with an even span uses 9 points (a standard choice)."]),
o("suppfig5-mixed-to-adaptation-transitions", "reproduced", "Over trials -20 to -1 the initiation curve before low blocks lies above the one before high blocks by +0.046 z (+0.059 pooled detrending). Wait time gap pre/post 0.125, initiation 0.197 (0.239)."),
o("fig2c-d-regression-on-previous-rewards", "reproduced", "Wait time current offer coefficient 0.212 (95% interval across rats 0.205 to 0.219; own interval above 0 in 289 rats), previous offer coefficients at most 0.013 in size. Initiation coefficients 1-3 back -0.029, -0.024, -0.012 (9 lags; the same to three decimals with 10); 261 of 291 rats have a negative 1-back coefficient.",
  deviations=[WITHIN, "Initiation times are z-scored over the rat's mixed block trials after the 99th percentile cut over all its trials; regress_latency_vs_rew.m repeats the cut within mixed blocks."]),
o("fig2e-tau-differ", "reproduced", "Methods reading, mean tau 0.065 for wait times (0 in 249 of 291 rats) and 1.875 for initiation times, signed-rank p = 3.5e-45; code reading 0.620 and 1.914, p = 2.7e-35. Six initiation taus (seven, code reading) are at the upper bound 10.",
  deviations=["The exponential is fitted by a dense grid over tau with the bounded optimal D in closed form, in place of fmincon from 10 random starts (a standard choice; no random draws remain)."]),
o("fig2f-tau-uncorrelated", "reproduced", "Methods reading r = -0.037, p = 0.535 (the legend prints r = -0.03, p = 0.53; the Results r = 0.08, p = 0.18); code reading r = 0.111, p = 0.059."),
o("fig2g-h-fast-slow-tau-groups", "reproduced", "58 rats per group (116 in all). Code coefficients, initiation p = 0.000 under all five seeds, wait time p = 0.215 (claim's seed; 0.203 to 0.217 over five seeds). Methods coefficients, 0.000 and 0.394. Observed initiation tau difference -2.66.",
  deviations=["Fits by grid search, as in fig2e."]),
o("fig2j-wait-time-not-sensitive-to-previous-offer", "reproduced", "38 of 291 rats have p < 0.05 (253 not, the paper's 87%). Population rank-sum p = 0.575 on per-rat means (paper 0.8), signed-rank variant p = 0.629; sensitivity -0.009 z.", measured=[38], deviations=[WITHIN]),
o("fig2k-initiation-sensitive-to-previous-offer", "reproduced", "Code reading (all mixed block trials) 256 rats with p < 0.05, 255 slower after small offers; population +0.091 against -0.148 z, rank-sum p = 9.9e-97, signed-rank p = 1.9e-49. Methods reading (20 uL trials) 276 rats with p < 0.05 but only 17 slower after small offers, and the population is faster after small offers (-0.161 against -0.094 z, rank-sum p = 6.6e-30). The claim holds under the code's reading only.", measured=[256],
  deviations=["The Methods (20 uL trials) and latency_post20ul_by_previous_vol.m (all mixed block trials) differ; both were run, as the criterion asks, and the outcome rests on the code's. Recorded as a code_mismatch finding.", WITHIN]),
o("fig2l-sensitivity-greater-for-initiation", "reproduced", "Code reading of fig2k, initiation sensitivity +0.239 against wait time -0.009, 245 of 291 rats, signed-rank p = 1.6e-36. Methods reading, initiation sensitivity -0.067, larger than the wait time sensitivity in 103 rats (p = 2.2e-06, in the opposite direction).",
  deviations=["Rests on the code's reading of fig2k (see there)."]),
o("suppfig6-results-without-detrending", "reproduced", "Without detrending, high-to-mixed above low-to-mixed over trials 1-20 by +0.246 z; mixed block after high +0.094, after low -0.085 z, p = 1.8e-49. Median per-session trend 0.069 z per 100 trials."),
o("fig3c-wait-time-by-catch-probability", "reproduced", "Reading A (each rat counted at every probability it has data at, after its first 1000 deposited trials) gives 3, 188, 61, 151 and 40 rats, all within tolerance, and wait times fall from 0.15 to 0.2 to 0.25 at all 5 offers (20 uL 12.10, 11.08, 10.61 s). Reading B (each rat at its main probability) gives 105, 43 and 128 rats at 0.15 to 0.25 and a fall at 3 of 5 offers. 8 rats have data at 0.3, which the paper does not list; 149 rats have data at more than one probability.",
  measured=[3, 188, 61, 151, 40], assumed=True,
  deviations=["The paper does not say how rats are assigned to cohorts. Its cohort sizes sum to 437, more than 291 rats, so rats are counted at more than one probability; reading A follows that and is adopted as an assumption, with reading B shown.", "The first 1000 deposited trials are dropped (Figure3.m drops the first 1000 stage 8 trials); the dandiset starts at the first included session, so the trials dropped are later ones than the code's."]),
o("fig3j-inferential-beats-retrospective-for-wait-times", "reproduced", "Claim's seed, inferential minus retrospective BIC -1040 (290 of 291 rats better, p = 3.6e-48), AIC -1052 (p = 3.6e-48), cross-validated nLL -454 (284 rats, p = 5.6e-44); best-fold test nLL variant -85 (p = 4.5e-18). The four other seeds give p <= 7.9e-47 for all three. Fitted k_high > k_low in 249 of 291 rats.", nb=NB_B, assumed=True,
  deviations=[FIT_DEV, "The deposited fits on Zenodo were not used; the models are refitted to the dandiset."]),
o("suppfig8-belief-state-not-distinguished", "reproduced", "Claim's seed, BIC and AIC p = 0.163, cross-validated nLL p = 0.569 (mean differences +11.0 and +19.9). Over the five seeds BIC/AIC p = 0.163, 0.068, 0.693, 0.031, 0.062 and cross-validated p = 0.41 to 0.997; under seed +3000 BIC and AIC reach p = 0.031 (mean +2.8 units, inferential better in 125 rats).", nb=NB_B, assumed=True, seed=True, deviations=[FIT_DEV]),
o("fig3f-inferential-model-not-sensitive-to-previous-offer", "not_reproduced", "Claim's seed, the model's 20 uL wait times are longer after offers below 20 uL (sensitivity +0.048 z), rank-sum p = 3.8e-05; the rats' sensitivity is -0.009 z, p = 0.575. Over the five noise draws p = 3.8e-05, 0.332, 4.3e-07, 1.5e-05 and 4.0e-04 (sensitivity +0.010 to +0.062).", nb=NB_B, assumed=True, seed=True,
  deviations=[FIT_DEV, "One log-normal draw (variance 8) per trial from the fitted inferential model replaces the rat's wait time, as Figure3.m does with WTMdl; the draws come from this attempt's fits, not the deposited ones."]),
o("suppfig9-wait-times-reflect-misinferences", "reproduced", "Mixed block 20 uL catch trials labelled high 10.85 s, labelled low 11.90 s; 230 of 291 rats shorter on high; signed-rank p = 9.7e-23. 8,540 trials labelled high and 7,688 low.", nb=NB_B,
  deviations=["The model's labels depend on no fitted parameter (H0 fixed), so held-out labels equal those of the full run; no fit is needed."]),
o("fig3i-retrospective-model-captures-initiation", "partially_reproduced", "Equation 10 model at alpha0 0.1042, overshoot 0.200 z and gap after high minus after low +1.398 z over trials 10-20. Static and |delta| models at alpha0 0.05 lack both (overshoot 0, gap -0.456 and -0.175), but at 0.4 and 0.8 each has a small overshoot (0.0002 to 0.0058 z) and a gap (+0.09 to +0.13), so they are not excluded at every alpha0 as the criterion asks. Noise 8 gives the same pattern. Fig. 3i part, simulated initiation slower after offers below 20 uL (+0.015 against -0.009 z, 232 of 291 rats, p = 1.8e-29; noise 1.5, 258 rats, p = 2.8e-39).", nb=NB_B, assumed=True,
  deviations=["The mean of 50 log-normal simulations is drawn from its normal approximation (mean TI, variance noise/50).", "Persistent gap is read as a positive mean difference over trials 10-20, and the overshoot as any excess of the maximum over trials 1-20 above trial 20; the criterion gives no size. Under a size threshold of, say, a tenth of the Equation 10 overshoot, every alternative would lack it.", "For the Fig. 3i part, each rat's retrospective parameters come from this attempt's fits (fig3j assumptions)."]),
o("fig3l-lambda-groups-wait-time-dynamics", "reproduced", "20/80 split, 58 rats per group. Wait time C at mixed to low p = 0.009 (0.009 to 0.018 over five seeds), at mixed to high C p = 0.026 (0.026 to 0.039) and D p = 0.120 (0.104 to 0.120). Initiation C at mixed to low p = 0.147, at mixed to high C p = 0.339 and D p = 0.374. Holds under the Results' reading (C at mixed to high), not under the legend's (D). 40/60 split, wait time C at mixed to low p = 0.391.", nb=NB_B, assumed=True,
  deviations=["Lambda from the five-parameter model (GenerateSynthData_Bayes_subopt_onlylambda_flat.m) fitted once on all data from one random start, without cross-validation, for time.", "Logistic fits by a grid over C and x0 with A and D solved exactly, in place of fmincon from 10 starts.", FIT_DEV]),
o("bayes-observer-offer-reduces-uncertainty", "reproduced", "Variance of block probabilities, prior 0.157, posterior 0.169 (higher means less uncertain); variance of block value, prior 0.104, posterior 0.082. Per-rat means signed-rank p = 1.8e-49 for both; over trials p < 0.001 in all 291 rats under both readings."),
o("fig4a-wait-time-block-sensitivity-emerges", "partially_reproduced", "On the Zenodo deposit's A_Structs_all (first 50 final-stage sessions). First pair initiation ratio 0.802 (273 rats), signed-rank against 1 p = 5.8e-16. Wait time ratio first pair 1.187, mean over pairs 16-25 0.936, so the first pair is not closer to 1 and part (2) fails; the ratio falls from above 1 to about 0.92. Block coefficient -0.432 over sessions 1-10 and -0.706 over 41-50 (linear offer -0.393 and -0.633).",
  deviations=["The dandiset holds only included sessions; the test uses the paper's Zenodo deposit (doi:10.5281/zenodo.10031483, A_Structs_all), trials with trainingstage 9, sessions in file order (the dates are not decoded).", "The wait time regression uses log2 offer (linear shown as a variant); per-session regressions need at least 5 catch trials and two blocks (a standard choice)."]),
o("fig4c-initiation-previous-reward-stable", "reproduced", "Previous reward coefficient -0.588 over sessions 1-10 and -0.469 over 41-50, same sign, relative change 0.252 against 0.389 for the wait time block coefficient.",
  deviations=["Data from the Zenodo deposit, as fig4a. The previous reward is log2 offer times hit (0 when unrewarded), as in fig2c-d."]),
o("fig4d-overshoot-grows-with-training", "reproduced", "Overshoot 0.025 z in the first 10 and 0.046 z in the last 10 final-stage sessions. Per 5-session chunk 0.008 rising to about 0.06 over the first 100 sessions (smoothed 0.008 to 0.055).",
  deviations=["Data from the Zenodo deposit, as fig4a; the paper's Figure4.m reads the raw database structs, which are not public."]),
o("fig5b-pre-cue-initiation-sensitive-to-offer", "reproduced", "Sessions from Figure5.m's dates (reading b), mean z by offer -0.041, -0.051, -0.088, -0.156, -0.178, falling at every step; 14 of 16 rats ANOVA p < 0.05 against 0 of 12 on the original task. After 30 pre-cue sessions (reading a, 11 rats have such sessions) 11 of 11 reach p < 0.05 but the mean rises from 5 to 10 uL (0.016 to 0.024).",
  deviations=["The Methods (after 30 pre-cue sessions) and Figure5.m (from the dated switch) differ; both run, the outcome rests on the code's.", "The dandiset holds only included sessions, so the paper's 'no session exclusion' for these rats cannot be applied.", "Initiation times are z-scored over all of the rat's trials (iti_by_reward.m was not read)."]),
o("fig5c-pre-cue-initiation-still-sensitive-to-previous-reward", "reproduced", "Sessions from the dates, all mixed block trials, 12 of 16 rats with p < 0.05 (11 slower after small offers), population +0.065 against -0.128 z, rank-sum p = 4.7e-06. Methods' 20 uL reading, 15 of 16 rats but a population faster after small offers (rank-sum p = 0.337). After 30 pre-cue sessions, 11 rats, 9 significant, rank-sum p = 6.4e-04.", measured=[12],
  deviations=["Rests on the code's readings of fig2k and of the sessions (see there)."]),
o("fig5d-pre-cue-initiation-depends-on-previous-block", "reproduced", "Sessions from the dates, trials 1-20 of mixed blocks after high +0.136, after low -0.114 z, all 16 rats, signed-rank p = 3.1e-05; after 30 pre-cue sessions all 11 rats with data, p = 9.8e-04."),
o("suppfig12-no-sex-differences", "reproduced", "184 males and 107 females (subject metadata). Wait time ratio 0.892 and 0.898, rank-sum p = 0.238 (paper 0.23); initiation ratio 0.572 and 0.561, p = 0.343 (paper 0.59)."),
o("suppfig14-contextual-effects-without-threshold", "reproduced", "Unthresholded 20 uL wait times high 12.51 s, low 14.47 s, signed-rank p = 1.5e-44 (z-scored), 1.0e-43 (raw). Unthresholded means are longer in all 11 block and offer cells, by 2.61 s on average in low blocks, 1.42 s in mixed and 1.34 s in high."),
o("pre-cue-session-link", "partially_reproduced", "14 of 16 rats linked; S042 and S050 are not (ANOVA p = 0.151 and 0.597 after the date; slopes -0.009 and -0.015). The task argument center_port_cue is True only in sessions of these 16 rats; on those sessions every rat has a negative slope of initiation time on log2 offer (-0.008 to -0.069), against -0.008 to +0.004 elsewhere. Some sessions after the dates are not flagged (S042 13 of 25, S050 6 of 11, E005 15 of 21), and the first flagged session is usually the day after the date.",
  deviations=["The rat names and dates are copied from Figure5.m at b7b68ca8c107 (first 16 of its 20 dates, paired by position)."]),
]
order = [l.split("- id: ")[1].strip() for l in open("claims/mah-2023.yaml") if l.startswith("- id: ")]
byid = {x["claim"]: x for x in outcomes}
assert set(byid) == set(order), set(order) ^ set(byid)
outcomes = [byid[c] for c in order]
rec = {
 "schema_version": 3, "id": "mah-2023-02",
 "datasets": [{"archive": "dandi", "id": "001169", "version": "0.261120.1450", "doi": "10.48324/dandi.001169/0.261120.1450", "relation": "primary"}],
 "paper": "doi:10.1038/s41467-023-43250-x", "date": "2026-11-24", "entry": "mah-2023",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
   "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-18"},
   "runner": {"platform": "GitHub Actions", "url": "https://github.com/encorescience/encore-registry/actions/runs/45502816457"}},
 "inputs": [
  {"what": "Rat behavioural data of all final-stage sessions (A_Structs_all) and the rat list (ratList.mat) from the paper's own deposit, read for Figure 4 only.", "source": "doi:10.5281/zenodo.10031483 (published.zip, version v1)"},
  {"what": "Names and switch dates of the 16 pre-initiation cue rats (Figure5.m ratListAll, startDates, secondGroup), and the parameter values of the initiation time simulations (Figure3.m params_mf 0.1042 and 0.2527).", "source": "https://github.com/constantinoplelab/published at commit b7b68ca8c107d8ce4a061e16da214307f175c3e5"},
 ],
 "outcomes": outcomes,
 "findings": [
  {"kind": "selection_undocumented", "about": "data", "severity": "major", "statement": "The dandiset holds only the sessions that pass the paper's inclusion criterion (the data of Figures 1 to 3), and nothing in it says so. The rig's trial counter (trials_in_stage) jumps between consecutive deposited sessions in 2,586 of 22,742 pairs (284 rats), and the first deposited session of a rat starts at a median of 1,543 final-stage trials. The paper's Zenodo deposit holds a median of 95 final-stage sessions per rat against 71 here. Figure 4 and the pre-cue analyses, which use all sessions, cannot be run on the dandiset alone."},
  {"kind": "metadata_insufficient", "about": "data", "severity": "minor", "statement": "The task argument center_port_cue has no description. It marks the pre-initiation cue sessions of Figure 5 (True in 762 sessions, all of the 16 rats Figure5.m names; initiation times depend on the offer only in those sessions), which the session description and dandiset metadata do not mention."},
  {"kind": "other", "about": "data", "severity": "minor", "statement": "wait_time_threshold equals the mean + 1 SD of all catch trials with a wait time, including 16,086 timed-out catch trials at 100 s; over opt-out catch trials alone it would be a median 5.2 s lower. The description says 'wait-times of the subject on catch trials' without saying that timeouts are included."},
  {"kind": "other", "about": "data", "severity": "minor", "statement": "Catch probability 0.3 occurs in 180,591 trials of 8 rats, a cohort the paper does not list, and two block transitions go directly between high and low blocks."},
  {"kind": "other", "about": "data", "severity": "none", "statement": "The counts match the paper exactly: 291 rats (184 male, 107 female), a median of 33,493 trials and 71 sessions per rat, all in the final training stage (code stage 9); the same 291 rats are in the Zenodo deposit's ratList. No session is deposited twice, and hit trial wait times equal the reward delays."},
  {"kind": "code_mismatch", "about": "paper", "statement": "For the previous-offer sensitivity of initiation times (Fig. 2k, 2l, 5c) the Methods use 20 uL trials in mixed blocks, while latency_post20ul_by_previous_vol.m uses all mixed block trials. Only the code's version reproduces the result; with the Methods' trials the population initiates faster after small offers (-0.161 against -0.094 z)."},
  {"kind": "paper_inconsistency", "about": "paper", "statement": "Fig. 2f is reported as r = 0.08, p = 0.18 in the Results and r = -0.03, p = 0.53 in the legend; the Methods' tau procedure on the dandiset gives r = -0.037, p = 0.535, close to the legend."},
  {"kind": "methods_unavailable", "about": "paper", "statement": "The model fitting code is not public. Questions for the authors - which parameters were free and with what bounds and starts, whether the 5 folds split sessions or trials, and whether the reported cross-validated nLL is the summed test nLL or the best fold's. This attempt's choices are stated in the deviations of fig3j, suppfig8, fig3f, fig3i and fig3l; fig3f fails with them and suppfig8 depends on the seed."},
  {"kind": "methods_unavailable", "about": "paper", "statement": "Fig. 3c cohort sizes (3, 183, 61, 151, 39) sum to 437 for 291 rats. Question for the authors - is each rat counted at every catch probability it ran? Counting so gives 3, 188, 61, 151 and 40 rats here; assigning each rat to one probability does not."},
 ],
}
class D(yaml.SafeDumper): pass
D.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style='"' if s in ("001169",) else None))
txt = yaml.dump(rec, Dumper=D, sort_keys=False, width=100, allow_unicode=True)
open("attempts/mah-2023-02.yaml", "w").write(txt)
print(len(outcomes))
PYEOF
python3 $TMPDIR/rec.py && python3 -c "
import yaml;d=yaml.safe_load(open('attempts/mah-2023-02.yaml'));print(d['datasets'], len(d['outcomes']))
import collections;print(collections.Counter(o['outcome'] for o in d['outcomes']))" && grep -n "—\|rather" attempts/mah-2023-02.yaml | head
```

```
Wed Nov 25 01:31:08 UTC 2026
33
[{'archive': 'dandi', 'id': '001169', 'version': '0.261120.1450', 'doi': '10.48324/dandi.001169/0.261120.1450', 'relation': 'primary'}] 33
Counter({'reproduced': 29, 'partially_reproduced': 3, 'not_reproduced': 1})
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/mah-2023 2>&1 | tail -5; python tools/entry.py handover entries/mah-2023 2>&1 | tail -5; ls executed/mah-2023/handover/; grep -rn "def check_attempt\|attempts/" tools/entry.py | head -5; ls tests | head -30
```

```
0 error(s)
wrote executed/mah-2023/handover
mah-2023.yaml
mah2023.py
models_mah_2023.ipynb
reproduce_mah_2023.ipynb
conftest.py
test_build_osf_targets.py
test_build_site.py
test_build_targets.py
test_build_zenodo_targets.py
test_intake.py
test_notify.py
test_protocol_pin.py
test_readme_row.py
test_replicates.py
test_reuse_targets.py
test_run_requests.py
test_runner.py
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q jsonschema pyyaml && python - <<'EOF'
import json, yaml, jsonschema
s=json.load(open('schemas/attempt.schema.json'))
d=yaml.safe_load(open('attempts/mah-2023-02.yaml'))
v=jsonschema.Draft202012Validator(s) if '2020' in s.get('$schema','') else jsonschema.Draft7Validator(s)
errs=list(v.iter_errors(d)); print(len(errs)); [print(e.message[:200], list(e.path)) for e in errs[:10]]
EOF
grep -rn "attempts/\*\|attempt.schema" tools/*.py | head -5; date -u
```

```
0
tools/build_site.py:147:# What a finding is about when its record does not say (schemas/attempt.schema.json, `about`): the paper for these
Wed Nov 25 01:31:49 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls -la entries/mah-2023; git status 2>&1 | head -3; timeout 600 python -m pytest tests/test_build_site.py -q -x 2>&1 | tail -3
```

```
total 316
drwxr-xr-x   4 runner runner   4096 Nov 25 00:29 .
drwxr-xr-x 351 runner runner  12288 Nov 24 22:44 ..
drwxr-xr-x   3 runner runner   4096 Nov 24 23:01 .claude
-rw-r--r--   1 runner runner    973 Nov 25 00:28 README.md
drwxr-xr-x   2 runner runner   4096 Nov 25 00:29 __pycache__
-rw-r--r--   1 runner runner   1221 Nov 25 00:28 entry.yaml
-rw-r--r--   1 runner runner  29626 Nov 25 00:29 mah2023.py
-rw-r--r--   1 runner runner  28880 Nov 25 00:28 models_mah_2023.ipynb
-rw-r--r--   1 runner runner  92488 Nov 25 00:28 reproduce_mah_2023.ipynb
-rw-r--r--   1 runner runner     56 Nov 25 00:28 requirements.in
-rw-r--r--   1 runner runner 124696 Nov 25 00:28 requirements.lock.txt
fatal: not a git repository (or any of the parent directories): .git
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python: No module named pytest
```

**Agent calls Bash**

```bash
find entries/mah-2023/.claude entries/mah-2023/__pycache__ -type f | head; cat .gitignore 2>/dev/null | head -20
```

```
entries/mah-2023/__pycache__/mah2023.cpython-313.pyc
__pycache__/
*.pyc
.ipynb_checkpoints/
.venv/
.DS_Store
executed/
site/
paper/
targets/local.json

# The protocol, laid over the checkout from encore-protocol at the version protocol.lock names
# (tools/protocol.sh). A file the protocol adds needs a line here; CI checks that laying it leaves the checkout clean.
/.protocol/
/docs/agents/
/docs/archives.md
/docs/author-responses.md
/docs/design.md
/docs/encore.md
/docs/outside-runs.md
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
find entries/mah-2023/.claude | head; rmdir -p --ignore-fail-on-non-empty $(find entries/mah-2023/.claude -depth -type d) 2>/dev/null; rm -rf entries/mah-2023/__pycache__; ls -la entries/mah-2023; python tools/entry.py check entries/mah-2023 | tail -1
```

```
entries/mah-2023/.claude
entries/mah-2023/.claude/.cc-writes
total 308
drwxr-xr-x   2 runner runner   4096 Nov 25 01:32 .
drwxr-xr-x 351 runner runner  12288 Nov 24 22:44 ..
-rw-r--r--   1 runner runner    973 Nov 25 00:28 README.md
-rw-r--r--   1 runner runner   1221 Nov 25 00:28 entry.yaml
-rw-r--r--   1 runner runner  29626 Nov 25 00:29 mah2023.py
-rw-r--r--   1 runner runner  28880 Nov 25 00:28 models_mah_2023.ipynb
-rw-r--r--   1 runner runner  92488 Nov 25 00:28 reproduce_mah_2023.ipynb
-rw-r--r--   1 runner runner     56 Nov 25 00:28 requirements.in
-rw-r--r--   1 runner runner 124696 Nov 25 00:28 requirements.lock.txt
0 error(s)
```

**Agent calls Bash**

```bash
timeout 120 python tools/entry.py run entries/mah-2023 2>&1 | tail -4; date -u
```

```
pass  reproduce_mah_2023.ipynb  (822 s, reused)
pass  models_mah_2023.ipynb  (2766 s, reused)
reused the executed copies of 2026-11-25 01:29 UTC: nothing the run reads has changed since (hash a611032771eb). Nothing was executed and no environment was built; --fresh runs it again.
Wed Nov 25 01:32:09 UTC 2026
```

**Agent**

I finished the blind repeat attempt on `mah-2023` against DANDI:001169 version 0.261120.1450. All 33 claims were tested and none is blocked. The entry passes its check, both notebooks ran from a clean environment, and the handover was built. I did not verify my own work, and nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| cohort-size, fig1e, fig1f, fig1i, suppfig2, suppfig3, suppfig12, suppfig14 | reproduced |
| fig2a, suppfig5, suppfig6, fig2c-d, fig2e, fig2f, fig2g-h, fig2j | reproduced |
| fig2k, fig2l | reproduced, but only when using the trials the paper's code uses |
| fig3c | reproduced, resting on an assumption |
| bayes-observer, suppfig9 | reproduced |
| fig3j | reproduced, resting on my model-fitting choices |
| suppfig8 | reproduced, resting on my model-fitting choices; depends on the random seed |
| fig3f | not reproduced, resting on my model-fitting choices; depends on the random seed |
| fig3i | partially reproduced, resting on an assumption |
| fig3l | reproduced under the Results' reading, resting on an assumption |
| fig4a | partially reproduced (tested on the paper's Zenodo deposit) |
| fig4c, fig4d | reproduced (tested on the Zenodo deposit) |
| fig5b, fig5c | reproduced under the code's session reading |
| fig5d | reproduced |
| pre-cue-session-link | partially reproduced (14 of 16 rats linked) |

Totals: 29 reproduced, 3 partially reproduced, 1 not reproduced.

### 2. What I found

**About the dataset**
- **Counts match the paper exactly:** 291 rats (184 male, 107 female), a median of 33,493 trials and 71 sessions per rat. No session is deposited twice.
- **Only included sessions are deposited, and nothing in the dandiset says so** (rated major). The trial counter jumps between consecutive sessions in 2,586 places, and the paper's Zenodo deposit has a median of 95 sessions per rat against 71 here. Figure 4 needs the excluded sessions, so I tested it on Zenodo `A_Structs_all` (doi:10.5281/zenodo.10031483). The paper should be listed on that Zenodo dataset as one of its datasets.
- **An undocumented task argument marks the pre-cue sessions.** `center_port_cue` is True only for the 16 rats of Figure 5. The claims file says nothing in the files marks these sessions, which is not the case.
- **The wait-time threshold includes timed-out catch trials.** It is computed with the 16,086 trials that ran to 100 s; the description does not say so.
- **An extra cohort.** 8 rats have catch probability 0.3, which the paper does not list. Two block transitions go straight between high and low.

**About the paper**
- **Methods and code differ for Fig. 2k, 2l and 5c.** The Methods use 20 uL trials and the code uses all mixed-block trials. Only the code's version reproduces; with the Methods' trials the effect reverses.
- **Fig. 2f prints two different results.** The Results give r = 0.08 and the legend r = -0.03; I get -0.037, p = 0.535, close to the legend.

**Assumptions and questions for the authors** (recorded as `methods_unavailable` findings)
- **Model fitting:** the fitting code is not public. I chose the bounds, 2 random starts (the paper used 100), random folds over sessions, and the summed held-out nLL as the cross-validated measure. Do these match what they did?
- **Fig. 3c cohorts:** the cohort sizes add up to 437 for 291 rats. Is each rat counted at every catch probability it ran?

**Questions to a reader:** none.

### 3. Where the protocol was unclear or did not fit
1. The claims have no per-outcome `data` field, so I could not mark Figure 4 as using data from elsewhere. I listed Zenodo under `inputs` and in the deviations.
2. archives.md says to read files with `remfile`. I fetched each file (about 1 MB) whole into memory instead, which is much faster, and noted it in the helper module.
3. Zenodo returned "too many requests" (HTTP 429). I read the zip by a few large range requests.
4. Five seeds for the model fits cost about 19 minutes. The lambda model was fitted once, from one start, without cross-validation; this is recorded as a deviation.
5. The 60-minute limit per notebook forced two notebooks, and each re-loads the data (about 9 minutes each).
6. The fig3i criterion gives no size for an "overshoot". Applied literally, tiny overshoots of 0.0002 to 0.0058 z in the alternative models make the outcome partial.
7. The `pre-cue-session-link` claim in the claims file is marked "Added by the author… written after a first look", so it comes from an earlier attempt. I used it as the claims file has it. That text is the only earlier-attempt content I saw; I looked at nothing else.
8. `runtime_minutes` in `entry.yaml` says 35 for the models notebook, but the run took 46. I left it, because editing the file would invalidate the record of the completed run.

### 4. Runtime and failures
- The behaviour notebook took 13.7 minutes (822 s) and the models notebook 46.1 minutes (2,766 s); both passed. Peak memory was 9.7 GB.
- During development, one run was killed for using too much memory in the Figure 4 cells (fixed by reading less at once), and Zenodo rate-limited me twice. Neither affects the final run.

Files are in `entries/mah-2023/`:
- reproduce_mah_2023.ipynb
- models_mah_2023.ipynb
- mah2023.py

The record is `attempts/mah-2023-02.yaml`.

## End of run

106 turns, 170 minutes, $13.85 at API prices, result: success.
