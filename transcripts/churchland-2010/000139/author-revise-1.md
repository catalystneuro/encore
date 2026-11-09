# 000139 · author-revise-1 · run 40768760256

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000139/verifier-1-report.md; ls entries/000139-churchland-2010 entries/000139-churchland-2010/*; ls questions | head
```

```
Wed Oct 28 21:08:08 UTC 2026
**A. Outcomes** (23 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| j-array-recordings | partially_reproduced | 152 units, within 146 ± 14.6. There are 27 conditions (9 mazes × 3 versions), not 108, and 250 trials (cell 13). The criterion gives "partial" when units match and conditions are a subset. Caveat: the paper says J-array interleaved all 108 conditions, so this 27-condition session (2009-09-29) is almost certainly a different recording, and the unit match is a coincidence. |
| fig4d-mean-correlation-j-array | partially_reproduced | Mean r is 0.14–0.21 across the 8 selection readings (main reading 0.172, t-test p = 0.042) with p < 0.05 in 5 of 8. That is inside 0.054–0.231 but outside 0.13 ± 0.013. The one reading with both means in tolerance (b/medoid/separate: 0.141, 0.119) has p ≥ 0.08 (cell 15). |
| fig4abc-mean-correlation-other-datasets | blocked (data_missing) | The archive API lists 2 assets, both one Jenkins array session. There are no speed-task or single-electrode data. |
| fig4-broad-unimodal | reproduced | In every reading r runs from about −0.5 to 0.68, mean 0.14–0.21, and the dip test p ≥ 0.195. No neuron has \|r\| > 0.8 (cell 17). With n = 15–20 the dip test has little power. |
| fig4e-correlation-time-course | reproduced (borderline) | 22 of 32 readings meet the criterion. The value at onset is 0.02–0.15, and the decline starts at −257 to −325 ms, at the edge of the −300 to −100 window. In the main selection only splice reading (a) with both thresholds passes (cell 19). |
| suppfig1-population-psth-weak-movement-tuning | reproduced (nominal) | The onset difference is smaller than the preparatory difference in 16/16 readings and less than half in 12/16. With the main reading's Figure-4 neurons the ratio is 0.94 (cell 21). See problem 6. |
| fig6d-perimovement-best-j-array | reproduced | Under every S, kinematic-window and replication reading, the peri-movement best (0.117 for S a, 0.226 for
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '1,400p' | grep -n "" | sed -n '1,60p'; wc -l docs/protocol.md
```

```
1:# Protocol for an attempt
2:
3:Version: `pilot-12`. Record this version in the attempt's provenance.
4:
5:This is what agents, or people, do to attempt a target and deposit the
6:result. A target is a dataset in a public archive and a paper it names. How
7:each archive's datasets are named, versioned and read is in
8:[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9:([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10:
11:An attempt has three roles, each a separate run with a separate context:
12:
13:- The **reader** reads the paper and writes the claims file: every finding,
14:  and how each is to be tested, taken from the paper. A second reader checks
15:  it against the paper. Readers never see the dataset's data.
16:- The **author** tests the claims on the dataset. It reads the paper to
17:  understand the claims, but the claims file binds it: it cannot change a
18:  claim's statement, expected values or criterion. A method detail the file
19:  lacks it takes from the paper, citing the passage, and it asks a reader
20:  only when it believes the file misreads the paper.
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 100,612p docs/protocol.md
```

```
<persisted-output>
Output too large (29.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/46ceab93-7403-4085-a0c8-bafe44685240/tool-results/b9agwu0fi.txt

Preview (first 2KB):
   - `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^##\|^###" docs/protocol.md
```

```
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
592:### Round 2: with the author's conclusions
604:### Round 3: proposed changes
```

**Agent calls Bash**

```bash
sed -n 182,500p docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.

[... 300 more lines not kept]
```

**Agent**

Starting round-1 revision. Reading the attempt record and notebook structure next.

**Agent calls Bash**

```bash
ls attempts | grep 000139; wc -l attempts/000139*; cat entries/000139-churchland-2010/entry.yaml; wc -l entries/000139-churchland-2010/maze.py; cat questions/000139.yaml 2>/dev/null | head -50; ls executed/ 2>/dev/null | head
```

```
000139-churchland-2010-01.yaml
368 attempts/000139-churchland-2010-01.yaml
schema_version: 1
name: 000139-churchland-2010
type: reproduction
title: Preparatory activity and a PD in peri-movement space (Churchland et al. 2010)
description: Tests the findings of Churchland, Cunningham, Kaufman, Ryu and Shenoy (2010) on dandiset
  000139 (MC_Maze_Medium), one session of monkey J on the maze task recorded with two Utah arrays and
  cut to 250 labelled trials over 27 conditions for the Neural Latents Benchmark. It tests the weak
  correlation between preparatory and peri-movement tuning, the performance of a preferred direction
  in peri-movement, kinematic and task spaces, the controls of Figure 7, and the simulation of Figure
  8. The speed-task and single-electrode datasets and the EMG are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_churchland_2010.ipynb
  title: Reproducing Churchland et al. (2010) from dandiset 000139
  runtime_minutes: 7
helpers:
- maze.py
related:
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000139-churchland-2010-01.yaml
```

```
schema_version: 2
id: 000139-churchland-2010-01
dataset:
  archive: dandi
  id: "000139"
  version: 0.220113.0408
  doi: 10.48324/dandi.000139/0.220113.0408
paper: doi:10.1016/j.neuron.2010.09.015
date: 2026-10-28
entry: 000139-churchland-2010
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
[... 348 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims | grep 139; wc -l claims/000139*; grep -n "^- id\|^  - id\|id:" claims/000139.yaml | head -40
```

```
000139
0 claims/000139
wc: claims/000139: Is a directory
grep: claims/000139.yaml: No such file or directory
```

**Agent calls Bash**

```bash
ls claims/000139; wc -l claims/000139/*
```

```
10.1016-j.neuron.2010.09.015.yaml
532 claims/000139/10.1016-j.neuron.2010.09.015.yaml
```

**Agent calls Read**

```json
{
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol as stated in docs/protocol.md (version pilot-12).
4	#
5	# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
6	# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
7	# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
8	# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
9	# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
10	# them. The paper links no code, so every method below comes from the Methods, the legends or the
11	# supplement.
12	#
13	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
14	# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
15	# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
16	# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
17	# trials with delays above 400 ms analysed. Four datasets. Monkeys A and B, speed task, 28
18	# conditions (7 directions, 2 distances, 2 instructed speeds), single electrodes, 64 and 74
19	# single units. Monkey J, maze task, single electrodes, 172 single units, recorded on four sets of
20	# 27 conditions each (about 53 neurons per set; population analyses done per set, then averaged).
[... 513 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010; python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'),len(s)); print(s[:300])
"
```

```
===== 0 markdown None 2437
# Churchland et al. (2010) on dandiset 000139 (MC_Maze_Medium)

**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
activity: representation of movement or first cog in a dynamical machine? *Neuron* 68, 387-400.
doi:10.1016/j.neuron.2010.09.015.

**Dat
===== 1 code None 372
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import diptest
import maze as M

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 200)
[... 470 more lines not kept]
```

**Agent calls Bash**

```bash
cat maze.py
```

```
"""Loading and measures for dandiset 000139 (MC_Maze_Medium), used to test
Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400.

Where each parameter comes from:

- Version: the only published version of the dandiset (``VERSION``).
- Trials kept: delays above 400 ms (claims file, opening comment, from Methods,
  Task design and behavior). Trials whose horizontal and vertical velocity
  profiles correlate with a reference proto-trial at r > 0.9 (Supplemental
  Experimental Procedures, Task design and behavioral control). The
  proto-trial and how the two profiles are combined are open; the claims file
  names the readings, implemented in ``proto_keep``. The window over which the
  profiles are correlated is not given; 150 ms before to 800 ms after movement
  onset (the maze-task peri-movement window of Methods, PCA-based spaces) is
  used, an assumption.
- Movement onset: reading (a) the dataset's ``move_onset_time``; reading (b)
  the first time after the go cue at which hand speed exceeds 10% of the
  trial's peak speed (the threshold is a standard choice; the paper does not
  give one).
- Rates: spike trains smoothed with a Gaussian of 20 ms standard deviation
[... 386 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [0,1,3,7,9,13,25,28,30,38,41,50,58,63,66]:
  c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
"
```

```
===== 0
# Churchland et al. (2010) on dandiset 000139 (MC_Maze_Medium)

**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
activity: representation of movement or first cog in a dynamical machine? *Neuron* 68, 387-400.
doi:10.1016/j.neuron.2010.09.015.

**Dataset.** DANDI:000139, "MC_Maze_Medium", version **0.220113.0408**, streamed from the archive.
This is the only published version of the dandiset (the other is the draft), so it is pinned; the
paper cites no version. The dandiset holds one session of monkey Jenkins (2009-09-29) on the maze
task, recorded with two Utah arrays, cut for the Neural Latents Benchmark into 250 training and
validation trials (with behaviour and trial labels) and 100 test trials (700 ms segments, no
condition labels, held-in units only).

**Claims.** `claims/000139/10.1016-j.neuron.2010.09.015.yaml`, written from the NIH author manuscript
(PMC2991102) with its supplement, and checked by a second reader. Methods the claims file leaves
open are taken from the paper (cited where used) or, where the paper is silent, run under every
reading the claims file names.

| Claim | Tested here |
[... 425 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../..; ls paper; grep -n -i "upper limit\|every neuron" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; (pdftotext 10.1016-j.neuron.2010.09.015.supp.pdf $TMPDIR/supp.txt && grep -n -i -B3 -A12 "upper limit of PD" $TMPDIR/supp.txt | head -80) || python -c "import pypdf"
```

```
Exit code 1
/bin/bash: line 1: pdftotext: command not found
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
```

**Agent calls Bash**

```bash
python -c "import fitz" 2>&1; ls .venv 2>/dev/null | head; python -c "
import re
t=open('paper/10.1016-j.neuron.2010.09.015.txt').read()
for m in re.finditer('(?i)upper limit',t): print(t[max(0,m.start()-300):m.start()+500].replace('\n',' ')); print('---')
" | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls; ls executed 2>/dev/null; sed -n 1,60p tools/entry.py | head -80; python -c "import pynwb, remfile, diptest; print('ok')"
```

```
Exit code 1
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
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 dev && uv pip install -q -p dev/bin/python -r entries/000139-churchland-2010/requirements.lock.txt 2>&1 | tail -3; dev/bin/python -c "import pynwb, diptest; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/w && cat > $TMPDIR/w/run_upto.py <<'EOF'
import json, sys, pickle, time, os
import matplotlib; matplotlib.use("Agg")
os.chdir("entries/000139-churchland-2010")
sys.path.insert(0, ".")
nb = json.load(open("reproduce_churchland_2010.ipynb"))
upto = int(sys.argv[1])
ns = {}
t0 = time.time()
for i, c in enumerate(nb["cells"][:upto + 1]):
    if c["cell_type"] != "code": continue
    src = "".join(c["source"]).replace("plt.show()", "plt.close('all')")
    exec(compile(src, f"cell{i}", "exec"), ns)
    print("cell", i, "done", round(time.time() - t0, 1), flush=True)
keep = {k: v for k, v in ns.items() if k in sys.argv[2].split(",")}
pickle.dump(keep, open(os.environ["TMPDIR"] + "/w/state.pkl", "wb"))
EOF
cd $TMPDIR/w && timeout 3000 ../dev/bin/python run_upto.py 32 tr,units,st,cond,conds,RD,d0,F6,F6_all,SEL_READINGS,tb,on_b,MAIN,KS,dims,el,sel_table,neuron_table 2>&1 | grep -v Warning | tail -20
```

```
a          a       b      0.117            6     0.016           2       0.03 initial velocity       0.068          True
a          b       a      0.117            6     0.022           2       0.03 initial velocity       0.068          True
a          b       b      0.117            6     0.022           2       0.03 initial velocity       0.068          True
b          a       a      0.226           13     0.019           4       0.03 initial velocity       0.184          True
b          a       b      0.226           13     0.019           4       0.03 initial velocity       0.184          True
b          b       a      0.226           13     0.024           2       0.03 initial velocity       0.184          True
b          b       b      0.226           13     0.024           2       0.03 initial velocity       0.184          True
Points below the axis floor (-0.5): 12 of 207 | min -2.319
cell 30 done 52.6
onset  proto  combine  neurons  peri_best_min  kin_best_max  task_best  peri_highest_all  peri_highest_any
    a   mean separate       85          0.000        -0.019     -0.015              True              True
    a   mean   concat       76          0.117         0.024      0.030              True              True
    a medoid separate       86         -0.042        -0.028     -0.028             False              True
    a medoid   concat       77          0.076         0.019      0.027              True              True
    b   mean separate       81          0.038        -0.003     -0.003              True              True
    b   mean   concat       74          0.120         0.033      0.040              True              True
    b medoid separate       89         -0.024        -0.025     -0.024              True              True
    b medoid   concat       77          0.091         0.021      0.028              True              True
Best peri-movement performance (S a) among neurons of array 1 and 2: {1: np.float64(0.291), 2: np.float64(-0.006)
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/w && cat > probe.py <<'EOF'
import sys; sys.path.insert(0, "entries/000139-churchland-2010")
import maze as M
nwb, f = M.open_nwb(M.TRAIN_PATH)
print(nwb.session_description, "|", nwb.identifier, "|", nwb.session_id, "|", nwb.experiment_description, "|", nwb.institution, nwb.lab)
for k, g in nwb.electrode_groups.items():
    print("group", k, "| desc", g.description, "| loc", g.location, "| device", g.device.name, g.device.description)
print("electrodes cols", nwb.electrodes.colnames)
print(nwb.electrodes.to_dataframe().head(3).T)
print(nwb.electrodes.to_dataframe().location.value_counts() if "location" in nwb.electrodes.colnames else "")
print("units cols", nwb.units.colnames, "| desc", nwb.units.description)
for c in nwb.units.colnames:
    try: print(c, "|", nwb.units[c].description)
    except Exception as e: print(c, e)
print(list(f["units"].keys()))
print(list(f["general"].keys()), list(f["general/extracellular_ephys"].keys()))
for k in f["general/extracellular_ephys/electrodes"].keys(): print(k, f["general/extracellular_ephys/electrodes"][k][:5])
EOF
../dev/bin/python probe.py 2>&1 | grep -v Warn
```

```
Wed Oct 28 21:13:51 UTC 2026
Data from monkey Jenkins performing center-out delayed reaching task. This file contains trials from the full session on 2009-09-29 that can be used for training models for the Neural Latents Benchmark. | 80434ca8-0b94-11ec-8a4f-bfff5c83b3dd | medium | Center-out delayed reaching task with maze barriers. | Stanford University Shenoy
group electrode_group_M1 | desc Electrodes in an implanted Utah array in M1 | loc Primary motor cortex | device electrode_array_M1 96-electrode Utah array in M1
group electrode_group_PMd | desc Electrodes in implanted Utah Array in PMd | loc Dorsal premotor cortex | device electrode_array_PMd 96-electrode Utah array in PMd
electrodes cols ('x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name')
id                                                          1  ...                                                  3
x                                                         NaN  ...                                                NaN
y                                                         NaN  ...                                                NaN
z                                                         NaN  ...                                                NaN
imp                                                       NaN  ...                                                NaN
location                                                  PMd  ...                                                PMd
filtering                                             1000 Hz  ...                                            1000 Hz
group       electrode_group_PMd pynwb.ecephys.ElectrodeGro...  ...  electrode_group_PMd pynwb.ecephys.ElectrodeGro...
group_name                                electrode_group_PMd  ...                                electrode_group_PMd

[8 rows x 3 columns]
location
PMd    96
M1     96
Name: count, dtype: int64
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && ../dev/bin/python -c "
import sys; sys.path.insert(0, 'entries/000139-churchland-2010')
import maze as M
nwb,f=M.open_nwb(M.TRAIN_PATH); print(nwb.related_publications, nwb.keywords[:])
" 2>&1 | grep -v Warn; curl -s https://api.dandiarchive.org/api/dandisets/000128/versions/0.220113.0400/info/ | head -c 600; echo; curl -s "https://api.dandiarchive.org/api/dandisets/000128/versions/0.220113.0400/assets/?page_size=5" | head -c 800
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/w && timeout 300 ../dev/bin/python -c "
import h5py, remfile, requests
m=requests.get('https://api.dandiarchive.org/api/dandisets/000128/versions/0.220113.0400/assets/26e85f09-39b7-480f-b337-278a8f034007/').json()
u=[x for x in m['contentUrl'] if 's3' in x][0]
f=h5py.File(remfile.File(u),'r')
print(f['session_description'][()], f['session_start_time'][()], f['units/id'].shape)
" 2>&1 | tail -2
```

```
b'Data from monkey Jenkins performing center-out delayed reaching task. This file contains trials from the full session on 2009-09-25 that can be used for training models for the Neural Latents Benchmark.' b'2009-09-25T00:00:00-07:00' (182,)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && ../dev/bin/python -c "
import pickle; s=pickle.load(open('state.pkl','rb')); tr=s['tr']
print(tr.columns.tolist()); print(tr.index[:5].tolist(), tr.index.min(), tr.index.max()); print(tr.start_time.min(), tr.stop_time.max())
print(tr[['start_time','maze_id','trial_type','trial_version']].head(12))
" 2>&1 | grep -v Warn
```

```
['start_time', 'stop_time', 'trial_type', 'trial_version', 'maze_id', 'success', 'target_on_time', 'go_cue_time', 'move_onset_time', 'rt', 'delay', 'num_targets', 'target_pos', 'num_barriers', 'barrier_pos', 'active_target', 'split']
[0, 1, 2, 3, 4] 0 249
0.0 772.876
    start_time  maze_id  trial_type  trial_version
id                                                
0          0.0       22           8              1
1          2.9       20           6              2
2          5.6       85          12              0
3          8.5       84          11              0
4         11.2       21           7              0
5         13.8       14           4              1
6         17.0       12           2              2
7         19.9       22           8              2
8         23.1       21           7              0
9         26.0       13           3              2
10        29.4       20           6              0
11        32.6       14           4              0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && ../dev/bin/python -c "
import pickle,numpy as np; s=pickle.load(open('state.pkl','rb')); tr=s['tr']
g=np.diff(tr.start_time.values); print(np.percentile(g,[0,5,25,50,75,95,100]).round(2)); print((tr.stop_time.values[:-1]-tr.start_time.values[1:]).round(3)[:10]); print(np.sort(g)[-10:].round(1)); print(tr.split.values[:20])
print((tr.start_time.values[1:]-tr.stop_time.values[:-1]).max())
" 2>&1 | grep -v Warn
```

```
[2.1  2.54 2.9  3.1  3.3  3.6  4.1 ]
[-0.064 -0.029 -0.084 -0.089 -0.044 -0.039 -0.049 -0.039 -0.109 -0.029]
[3.7 3.8 3.8 3.8 3.9 3.9 3.9 4.  4.  4.1]
<StringArray>
[  'val',   'val',   'val', 'train', 'train', 'train', 'train',   'val',
 'train', 'train', 'train', 'train',   'val', 'train', 'train', 'train',
   'val',   'val', 'train', 'train']
Length: 20, dtype: str
0.10900000000003729
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > dev1.py <<'EOF'
import pickle, sys, time, numpy as np, pandas as pd
sys.path.insert(0, "entries/000139-churchland-2010")
import maze as M
from scipy import stats
globals().update(pickle.load(open("state.pkl", "rb")))
KS = list(range(1, 15))
def neuron_sets(d, how):
    tp = M.tuning_strength(d["prep"], how); tq = M.tuning_strength(d["peri"], how)
    prep_ok = tp > 5; return prep_ok, prep_ok & (tq >= 1.5 * tp)
t0 = time.time()
# --- P1 threshold null
sel = d0["sel"]
cnt = M.bin_spikes(st, tr.go_cue_time.values, M.PREP)[sel].sum(2).astype(float) / ((M.PREP[1] - M.PREP[0]) / 1000)
c_sel = cond[sel]
def rng_pass(cs):
    Xc = np.stack([cnt[cs == c].mean(0) for c in conds]); return M.tuning_strength(Xc, "range") > 5
obs = rng_pass(c_sel)
rng = np.random.default_rng(9)
sh = np.array([rng_pass(rng.permutation(c_sel)).sum() for _ in range(20)])
print("observed pass (count-based)", obs.sum(), "smoothed-based", neuron_sets(d0,"range")[0].sum(), "| shuffled median", np.median(sh), "range", sh.min(), sh.max())
print(time.time()-t0)
EOF
../dev/bin/python dev1.py 2>&1 | grep -v Warn
```

```
observed pass (count-based) 75 smoothed-based 76 | shuffled median 59.0 range 53 65
0.34380245208740234
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > dev2.py <<'EOF'
exec(open("dev1.py").read().split("t0 = time.time()")[0])
t0=time.time()
sel = d0["sel"]; c_sel = cond[sel]
cnt = M.bin_spikes(st, tr.go_cue_time.values, M.PREP)[sel].sum(2).astype(float) / ((M.PREP[1] - M.PREP[0]) / 1000)
rngp = np.random.default_rng(9)
Xc = np.stack([cnt[c_sel == c].mean(0) for c in conds]); obs_rng = M.tuning_strength(Xc, "range")
null = np.array([M.tuning_strength(np.stack([cnt[cs == c].mean(0) for c in conds]), "range") for cs in [rngp.permutation(c_sel) for _ in range(200)]])
p_unit = ((null >= obs_rng).sum(0) + 1) / 201
prep_ok = neuron_sets(d0, "range")[0]
print("passers", prep_ok.sum(), "of which permutation p<0.05:", (prep_ok & (p_unit < 0.05)).sum(), "| all units p<0.05", (p_unit<0.05).sum())
print(time.time()-t0)
# Fig6 null: shuffle each neuron's prep rates over conditions
X = d0["prep"]; fit = F6["fit"]
Gu = M.grams_per_unit(d0["mv_rate"], M.MOVE_WIN[0]); Gt = Gu.sum(0)
Gk = M.kinematic_gram(d0["pos"], d0["vel"], M.MOVE_WIN[0], len(units) - 1)
rng6 = np.random.default_rng(60)
nulls = {}
for draw in range(10):
    Xs = X.copy()
    for n in fit: Xs[:, n] = X[rng6.permutation(len(conds)), n]
    for R in "ab":
        nulls.setdefault(("peri", R), []).append(M.perf_curves_pca(Xs, Gt, Gu, fit, KS, R == "b").mean(0))
        nulls.setdefault(("kin", R), []).append(M.perf_curves_pca(Xs, Gk, None, fit, KS, R == "b").mean(0))
    for nm, S in F6["spaces"].items():
        nulls.setdefault(nm, []).append(np.mean([M.pd_performance_fixed(Xs[:, n], S) for n in fit]))
    print("draw", draw, time.time()-t0, flush=True)
for k, v in nulls.items():
    v = np.array(v); print(k, np.round(v.mean(0), 3), "| sd", np.round(v.std(0).max(), 3))
EOF
../dev/bin/python dev2.py 2>&1 | grep -v Warn
```

```
passers 76 of which permutation p<0.05: 42 | all units p<0.05 54
0.3916957378387451
draw 0 8.367883443832397
draw 1 16.284095764160156
draw 2 24.211738109588623
draw 3 32.131858110427856
draw 4 40.04879832267761
draw 5 47.98017764091492
draw 6 55.91684031486511
draw 7 63.88731837272644
draw 8 71.85984253883362
draw 9 79.8232352733612
('peri', 'a') [-0.12  -0.171 -0.222 -0.284 -0.363 -0.44  -0.519 -0.614 -0.717 -0.859
 -1.134 -1.548 -1.953 -2.732] | sd 0.173
('kin', 'a') [-0.119 -0.17  -0.227 -0.285 -0.353 -0.429 -0.513 -0.628 -0.754 -0.893
 -1.097 -1.507 -1.73  -3.685] | sd 0.403
('peri', 'b') [-0.102 -0.132 -0.141 -0.164 -0.181 -0.214 -0.25  -0.26  -0.263 -0.277
 -0.293 -0.297 -0.302 -0.308] | sd 0.025
('kin', 'b') [-0.112 -0.168 -0.222 -0.278 -0.346 -0.399 -0.439 -0.489 -0.559 -0.682
 -0.805 -0.93  -0.993 -1.068] | sd 0.084
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > dev3.py <<'EOF'
exec(open("dev1.py").read().split("t0 = time.time()")[0])
t0=time.time()
sel = d0["sel"]
mo = tr.move_onset_time.values
go_b = M.bin_spikes(st, tr.go_cue_time.values, M.GO_WIN)
mv_b = M.bin_spikes(st, mo, M.MOVE_WIN)
print("binned", time.time()-t0)
def half_means(h):
    m = np.zeros(len(tr), bool)
    for c in conds:
        ii = np.where(sel & (cond == c))[0]; m[ii[h::2]] = True
    cc = cond[m]
    go_r = M.smooth_rate(M.cond_mean(go_b[m].astype(np.float32), cc, conds))
    mv_r = M.smooth_rate(M.cond_mean(mv_b[m].astype(np.float32), cc, conds))
    return dict(go_rate=go_r, mv_rate=mv_r, prep=M.window_mean(go_r, M.PREP, M.GO_WIN[0]))
H = [half_means(0), half_means(1)]
def supp1_cv(rank_d, meas_d, idx):
    nc = len(conds); ranks = [nc - 1, 2 * (nc - 1) // 3, (nc - 1) // 3, 0]
    go_tr, mv_tr = [], []
    for n in idx:
        o = np.argsort(rank_d["prep"][:, n])
        mx = max(meas_d["go_rate"][:, n].max(), meas_d["mv_rate"][:, n].max())
        go_tr.append(meas_d["go_rate"][o[ranks], n] / mx); mv_tr.append(meas_d["mv_rate"][o[ranks], n] / mx)
    go_tr = np.mean(go_tr, 0); mv_tr = np.mean(mv_tr, 0)
    g0, m0 = M.GO_WIN[0], M.MOVE_WIN[0]
    return (go_tr[0, M.PREP[0]-g0:M.PREP[1]-g0] - go_tr[3, M.PREP[0]-g0:M.PREP[1]-g0]).mean(), mv_tr[0, -m0] - mv_tr[3, -m0]
for nm, mask in zip(["both", "prep only"], neuron_sets(d0, "range")[::-1]):
    idx = np.where(mask)[0]
    res = [supp1_cv(H[0], H[1], idx), supp1_cv(H[1], H[0], idx)]
    pdf = np.mean([r[0] for r in res]); odf = np.mean([r[1] for r in res])
    print(nm, len(idx), "cv prep diff", round(pdf,3), "onset diff", round(odf,3), "ratio", round(odf/pdf,3), [np.round(r,3) for r in res])
    res = [supp1_cv(H[0], H[0], idx), supp1_cv(H[1], H[1], idx)]
    print("  same-half", [np.round(r,3) for r in res])
# CV dimensionality
prep_ok = neuron_sets(d0, "range")[0]
A, B = H[0]["prep"][:, prep_ok], H[1]["prep"][:, prep_ok]
def cv_dim(A, B):
    Ac = A - A.mean(0); Bc = B - B.mean(0)
    U, s, Vt = np.linalg.svd(Ac, full_matrices=False)
    sig = np.array([(Ac @ v) @ (Bc @ v) for v in Vt])  # cross-validated variance along each PC of A
    return sig
s1 = cv_dim(A, B); s2 = cv_dim(B, A); sig = (s1 + s2) / 2
cum = np.cumsum(sig) / sig[sig > 0].sum()
print("cv signal var per PC", np.round(sig[:15] / sig[sig>0].sum(), 3))
print("k for 90% of cv signal", int(np.searchsorted(cum, 0.9) + 1), "| peak of cumsum", cum.max().round(3), "at", cum.argmax()+1)
# same split, raw count for comparison on each half
for Z in (A, B):
    ev = M.explained(Z @ Z.T); print("half raw k90", int(np.searchsorted(np.cumsum(ev), 0.9)+1))
print(time.time()-t0)
EOF
../dev/bin/python dev3.py 2>&1 | grep -v Warn
```

```
binned 1.0347683429718018
both 17 cv prep diff 0.04 onset diff 0.045 ratio 1.115 [array([0.042, 0.04 ]), array([0.038, 0.049])]
  same-half [array([0.119, 0.078]), array([0.104, 0.057])]
prep only 76 cv prep diff 0.055 onset diff 0.03 ratio 0.545 [array([0.054, 0.022]), array([0.057, 0.039])]
  same-half [array([0.139, 0.036]), array([0.119, 0.029])]
cv signal var per PC [0.357 0.201 0.102 0.121 0.066 0.039 0.028 0.016 0.014 0.007 0.007 0.006
 0.008 0.005 0.012]
k for 90% of cv signal 7 | peak of cumsum 0.995 at 20
half raw k90 15
half raw k90 15
2.460977554321289
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > dev4.py <<'EOF'
exec(open("dev1.py").read().split("t0 = time.time()")[0])
t0=time.time()
X = d0["prep"]
rng7c = np.random.default_rng(70)
prep_ok0 = neuron_sets(d0, "range")[0]
Gu_all = M.grams_per_unit(d0["mv_rate"], M.MOVE_WIN[0])
def half_perf(members, R):
    mem = np.where(members)[0]; fit = np.where(members & prep_ok0)[0]
    Gu = Gu_all[mem]; Gt = Gu.sum(0); Gp = M.prep_grams(X[:, mem]); loc = {n: i for i, n in enumerate(mem)}
    peri = np.mean([M.pd_performance_pca(X[:, n], Gt - Gu[loc[n]], [6], R == "b")[0] for n in fit])
    up_in = np.mean([M.pd_performance_pca(X[:, n], Gp.sum(0), KS, R == "b") for n in fit], 0)
    up_ex = np.mean([M.pd_performance_pca(X[:, n], Gp.sum(0) - Gp[loc[n]], KS, R == "b") for n in fit], 0)
    return peri, up_in[5], up_in.max(), up_ex[5], up_ex.max(), len(fit)
rows = []
for R in "ab":
    res = {"all": half_perf(np.ones(len(units), bool), R), "array 1": half_perf(units.id_array.values == 1, R), "array 2": half_perf(units.id_array.values == 2, R)}
    rand = []
    for _ in range(20):
        m = np.zeros(len(units), bool); m[rng7c.choice(len(units), len(units) // 2, replace=False)] = True
        rand += [half_perf(m, R), half_perf(~m, R)]
    for nm, v in res.items():
        rows.append(dict(S=R, subset=nm, n=v[5], perf=v[0], up_in6=v[1], up_inb=v[2], up_ex6=v[3], up_exb=v[4], n_in6=v[0]/v[1], n_inb=v[0]/v[2], n_ex6=v[0]/v[3]))
    rr = np.array(rand)
    rows.append(dict(S=R, subset="random", n=rr[:,5].mean(), perf=rr[:,0].mean(), up_in6=rr[:,1].mean(), up_inb=rr[:,2].mean(), up_ex6=rr[:,3].mean(), up_exb=rr[:,4].mean(),
                     n_in6=(rr[:,0]/rr[:,1]).mean(), n_inb=(rr[:,0]/rr[:,2]).mean(), n_ex6=(rr[:,0]/rr[:,3]).mean()))
    print(R, "random n_in6 sd", (rr[:,0]/rr[:,1]).std().round(3), "min/max", (rr[:,0]/rr[:,1]).min().round(3), (rr[:,0]/rr[:,1]).max().round(3))
print(pd.DataFrame(rows).round(3).to_string())
print(time.time()-t0)
EOF
../dev/bin/python dev4.py 2>&1 | grep -v Warn
```

```
a random n_in6 sd 0.153 min/max 0.067 0.869
b random n_in6 sd 0.103 min/max 0.352 0.736
   S   subset     n   perf  up_in6  up_inb  up_ex6  up_exb  n_in6  n_inb  n_ex6
0  a      all  76.0  0.117   0.176   0.178   0.061   0.068  0.667  0.657  1.937
1  a  array 1  35.0  0.271   0.356   0.575   0.128   0.212  0.761  0.472  2.111
2  a  array 2  41.0 -0.060   0.150   0.161  -0.107  -0.008 -0.402 -0.374  0.560
3  a   random  38.0  0.095   0.211   0.277  -0.043   0.046  0.455  0.350 -0.711
4  b      all  76.0  0.145   0.205   0.300   0.115   0.184  0.707  0.483  1.258
5  b  array 1  35.0  0.270   0.352   0.616   0.170   0.335  0.766  0.438  1.581
6  b  array 2  41.0  0.049   0.214   0.341   0.055   0.055  0.230  0.144  0.892
7  b   random  38.0  0.140   0.250   0.417   0.084   0.114  0.564  0.336 -0.740
161.91738080978394
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010 && python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [14,17,20,23,26,33,36,39,42,45,48,51,54,57,61,64,67,70,73,74]:
  c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
"
```

```
===== 14
**Result: partially reproduced.** The dandiset holds 152 units (within 146 +/- 14.6) from two
arrays, 75 and 77 by unit id, but 27 conditions (9 mazes in 3 versions), not 108, and 250 labelled
trials per unit (350 with the unlabelled test segments) against the paper's 2166. That the 9 mazes are
among the paper's 108 conditions is consistent with the data (same monkey, task and three-version
design) but cannot be shown from the files.
===== 17
**Result: partially reproduced, resting on the reading of the trial selection and of the tuning
measure.** Under the main reading 17 neurons pass both thresholds; the mean Pearson r is 0.172 and the
mean Spearman r 0.139, both outside tolerance (0.13 +/- 0.013, 0.11 +/- 0.011), and the mean is above
zero by the t-test (p = 0.0422) and the Fisher-z t-test (p = 0.0443), not by the Wilcoxon test (p =
0.0714). No reading puts both means in tolerance with p < 0.05. The mean r lies in 0.054 to 0.231 in
all 8 selection readings, with p < 0.05 by some test in 5 of them, so the outcome depends on the
selection reading. The SD measure of tuning leaves no neuron passing both thresholds. With these few
trials per condition the counts move with the thresholds (threshold table).
===== 20
**Result: reproduced.** In every selection reading the correlations run from negative (-0.36 to
-0.50) to positive (0.54 to 0.68) values, the mean is 0.141 to 0.207, no neuron has |r| > 0.8, and the
dip test does not reject unimodality (p = 0.195 to 0.993). Under the main reading n = 17, mean 0.172,
SD 0.321, dip p = 0.788. The sample is small.
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010 && python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [16,22,53,69]:
  c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
print(nb['cells'][13]['metadata'], nb['cells'][13].keys())
"
```

```
Exit code 1
/bin/bash: line 1: cd: entries/000139-churchland-2010: No such file or directory
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [16,22]:
  c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
print(nb['cells'][13]['metadata'], nb['cells'][13].keys())
"
```

```
===== 16
def corr_set(d, mask):
    idx = np.where(mask)[0]
    r = np.array([np.corrcoef(d["prep"][:, i], d["peri"][:, i])[0, 1] for i in idx])
    rs = np.array([stats.spearmanr(d["prep"][:, i], d["peri"][:, i])[0] for i in idx])
    return idx, r, rs

def mean_tests(r):
    if len(r) < 3:
        return dict(p_t=np.nan, p_wilcoxon=np.nan, p_fisher_t=np.nan)
    return dict(p_t=stats.ttest_1samp(r, 0).pvalue, p_wilcoxon=stats.wilcoxon(r).pvalue,
                p_fisher_t=stats.ttest_1samp(np.arctanh(np.clip(r, -0.999999, 0.999999)), 0).pvalue)

rows = []
for r_ in SEL_READINGS:
    for how in ["range", "sd"]:
        d = condition_data(*r_)
        _, both = neuron_sets(d, how)
        idx, r, rs = corr_set(d, both)
        t = mean_tests(r)
[... 99 more lines not kept]
```

**Agent**

Now writing the notebook edit script.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/edit_nb.py <<'PYEOF'
import json, uuid
P = "entries/000139-churchland-2010/reproduce_churchland_2010.ipynb"
nb = json.load(open(P))
C = nb["cells"]
def src(i): return "".join(C[i]["source"])
def setsrc(cell, s):
    lines = s.split("\n"); cell["source"] = [l + "\n" for l in lines[:-1]] + [lines[-1]]
def code(s, tags=None):
    c = dict(cell_type="code", execution_count=None, id=uuid.uuid4().hex[:8], metadata={"tags": tags} if tags else {}, outputs=[], source=[])
    setsrc(c, s); return c
def md(s):
    c = dict(cell_type="markdown", id=uuid.uuid4().hex[:8], metadata={}, source=[]); setsrc(c, s); return c
def find(start):
    hits = [i for i, c in enumerate(C) if "".join(c["source"]).startswith(start)]
    assert len(hits) == 1, (start, hits); return hits[0]
def append(i, s): setsrc(C[i], src(i) + "\n" + s)
def replace(i, a, b):
    s = src(i); assert a in s, (i, a); setsrc(C[i], s.replace(a, b))

# --- j-array-recordings: identity outputs
i = find("n_units = len(units)")
append(i, '''print("Session description in the file:", D["nwb"].session_description)
gap = tr.start_time.values[1:] - tr.stop_time.values[:-1]
print("Trial timeline: first trial starts at", tr.start_time.min(), "s; next trial start minus trial end ranges from",
      gap.min().round(3), "to", gap.max().round(3), "s. The kept trials abut or overlap, so the timeline was rebuilt and cannot",
      "show which other trials or conditions the session held.")''')

# --- neurons: threshold noise reference
i = find("def neuron_sets(d, how):")
C.insert(i + 1, md('''Noise reference for the 5 spikes/s threshold (added in response to the verifier, round 1). The
paper accepts the lower array threshold "given the higher signal-to-noise ratio provided by the higher
trial count" (Methods, Neural recordings and datasets); here there are 6 to 10 trials per condition.
The same range measure on spike counts in the preparatory window, with condition labels shuffled
among the kept trials (200 draws), shows how many units pass from noise alone, and a per-unit
permutation p-value marks the units whose tuning is distinguishable from noise.'''))
C.insert(i + 2, code('''rng_thr = np.random.default_rng(5)
c_sel0 = cond[sel0]
cnt_prep = go0[sel0]
def range_counts(cs):
    return M.tuning_strength(np.stack([cnt_prep[cs == c].mean(0) for c in conds]), "range")
rng_obs = range_counts(c_sel0)
rng_null = np.array([range_counts(rng_thr.permutation(c_sel0)) for _ in range(200)])
p_tune = ((rng_null >= rng_obs).sum(0) + 1) / (len(rng_null) + 1)
n_null = (rng_null > 5).sum(1)
print("Units with a preparatory range above 5 spikes/s (window counts, main selection): observed", int((rng_obs > 5).sum()),
      "of", len(units), "| labels shuffled: median", int(np.median(n_null)), "range", n_null.min(), "to", n_null.max())
tuned_perm = pdn & (p_tune < 0.05)
print("PD neurons (range above 5 spikes/s):", int(pdn.sum()), "| of them with permutation p < 0.05:", int(tuned_perm.sum()),
      "| all units with p < 0.05:", int((p_tune < 0.05).sum()), "(expected by chance about", round(0.05 * len(units), 1), ")")
print("Split-half reliability, PD neurons with permutation p < 0.05: median r",
      np.round(np.median(rel[p_tune[np.where(pdn)[0]] < 0.05]), 3), "| the others:", np.round(np.median(rel[p_tune[np.where(pdn)[0]] >= 0.05]), 3))'''))

# --- supp1: cross-validated ranking
i = find("def supp1(d, mask):")
append(i, '''# Cross-validated variant (verifier, round 1): conditions ranked on the odd trials of each condition and the traces
# measured on the even trials, and the reverse, averaged; removes the regression to the mean of ranking and measuring
# on the same trials. Main selection only.
go_b = M.bin_spikes(st, tr.go_cue_time.values, M.GO_WIN)
mv_b = M.bin_spikes(st, tr.move_onset_time.values, M.MOVE_WIN)
def half_means(h):
    m = np.zeros(len(tr), bool)
    for c in conds:
        ii = np.where(d0["sel"] & (cond == c))[0]
        m[ii[h::2]] = True
    go_r = M.smooth_rate(M.cond_mean(go_b[m].astype(np.float32), cond[m], conds))
    mv_r = M.smooth_rate(M.cond_mean(mv_b[m].astype(np.float32), cond[m], conds))
    return dict(go_rate=go_r, mv_rate=mv_r, prep=M.window_mean(go_r, M.PREP, M.GO_WIN[0]))
HALF = [half_means(0), half_means(1)]
def supp1_cv(rank_d, meas_d, idx):
    nc = len(conds)
    ranks = [nc - 1, 2 * (nc - 1) // 3, (nc - 1) // 3, 0]
    go_tr, mv_tr = [], []
    for n in idx:
        o = np.argsort(rank_d["prep"][:, n])
        mx = max(meas_d["go_rate"][:, n].max(), meas_d["mv_rate"][:, n].max())
        go_tr.append(meas_d["go_rate"][o[ranks], n] / mx); mv_tr.append(meas_d["mv_rate"][o[ranks], n] / mx)
    go_tr = np.mean(go_tr, 0); mv_tr = np.mean(mv_tr, 0)
    g0, m0 = M.GO_WIN[0], M.MOVE_WIN[0]
    return (go_tr[0, M.PREP[0] - g0: M.PREP[1] - g0] - go_tr[3, M.PREP[0] - g0: M.PREP[1] - g0]).mean(), mv_tr[0, -m0] - mv_tr[3, -m0]
rows = []
for nset, mask in zip(["both thresholds", "preparatory only (variant)"], neuron_sets(d0, "range")[::-1]):
    idx = np.where(mask)[0]
    for how, pairs in [("cross-validated", [(0, 1), (1, 0)]), ("same half (biased)", [(0, 0), (1, 1)])]:
        res = np.array([supp1_cv(HALF[a], HALF[b], idx) for a, b in pairs])
        pdf, odf = res.mean(0)
        rows.append(dict(neurons=nset, n=len(idx), ranking=how, prep_diff=round(pdf, 3), onset_diff=round(odf, 3),
                         ratio=round(odf / pdf, 3), a_smaller=odf < pdf, b_less_than_half=odf / pdf < 0.5))
print("Half-trial variants, main selection:")
print(pd.DataFrame(rows).to_string(index=False))''')

# --- fig6d: paper's upper limit reference
i = find("def fig6d_judge(F):")
replace(i, 'upper_best=F["curves"][("upper", R)].mean(0).max().round(3),',
        'upper_best=F["curves"][("upper", R)].mean(0).max().round(3),\n                                 upper_incl_best=F["curves"][("upper incl. neuron", R)].mean(0).max().round(3),')
# --- chance levels and permutation-tuned variant after the robustness cell
i = find("F6_all = {MAIN: F6}")
C.insert(i + 1, md('''Chance level of each space (added in response to the verifier, round 1). The Results say "Points
above zero indicate performance considerably better than chance". Each fitted neuron's preparatory
rates are shuffled over conditions (10 draws) and the performance of every space is recomputed.
Then the comparison is repeated on the PD neurons whose preparatory tuning is distinguishable from
noise (permutation p < 0.05, above).'''))
C.insert(i + 2, code('''rng6 = np.random.default_rng(60)
X0, fit0 = d0["prep"], F6["fit"]
Gu0 = M.grams_per_unit(d0["mv_rate"], M.MOVE_WIN[0]); Gt0 = Gu0.sum(0)
Gk0 = M.kinematic_gram(d0["pos"], d0["vel"], M.MOVE_WIN[0], len(units) - 1)
NULL = {}
for draw in range(10):
    Xs = X0.copy()
    for n in fit0:
        Xs[:, n] = X0[rng6.permutation(len(conds)), n]
    for R in "ab":
        NULL.setdefault(("peri", R), []).append(M.perf_curves_pca(Xs, Gt0, Gu0, fit0, KS, R == "b").mean(0))
        NULL.setdefault(("kinematic win a rep a", R), []).append(M.perf_curves_pca(Xs, Gk0, None, fit0, KS, R == "b").mean(0))
    for nm, S in F6["spaces"].items():
        NULL.setdefault(nm, []).append(np.mean([M.pd_performance_fixed(Xs[:, n], S) for n in fit0]))
NULL = {k: np.array(v) for k, v in NULL.items()}
print("Chance: mean performance with conditions shuffled (10 draws), by k:")
print(pd.DataFrame({f"{k[0]} | S {k[1]}": v.mean(0) for k, v in NULL.items() if isinstance(k, tuple)}, index=KS).T.round(3).to_string())
print("Largest SD over draws of a curve point:", round(max(v.std(0).max() for k, v in NULL.items() if isinstance(k, tuple)), 3))
null_task = pd.Series({k: v.mean() for k, v in NULL.items() if not isinstance(k, tuple)})
print(pd.DataFrame({"dim": dims, "observed": task_tab, "chance": null_task.round(3)}).to_string())
for key in [("peri", "a"), ("peri", "b"), ("kinematic win a rep a", "a"), ("kinematic win a rep a", "b")]:
    obs = F6["curves"][key].mean(0); ch = NULL[key].mean(0)
    print(key, "| observed above chance at every k:", bool((obs > ch).all()), "| observed - chance, k = 1..14:", np.round(obs - ch, 3))
print("Task spaces above chance:", int((task_tab > null_task).sum()), "of", len(task_tab))
# variant: PD neurons whose tuning passes the permutation test
fitp = np.where(tuned_perm)[0]
rows = []
for R in "ab":
    peri = M.perf_curves_pca(X0, Gt0, Gu0, fitp, KS, R == "b").mean(0)
    kin = M.perf_curves_pca(X0, Gk0, None, fitp, KS, R == "b").mean(0)
    task = {nm: np.mean([M.pd_performance_fixed(X0[:, n], S) for n in fitp]) for nm, S in F6["spaces"].items()}
    bt = max(task, key=task.get)
    rows.append(dict(S=R, neurons=len(fitp), peri_best=peri.max().round(3), peri_best_k=KS[peri.argmax()], peri_k14=peri[-1].round(3),
                     kin_best=kin.max().round(3), kin_best_k=KS[kin.argmax()], task_best=round(task[bt], 3), task_best_space=bt,
                     seg_dirs_t=round(task["segment dirs (t)"], 3), init_vel=round(task["initial velocity"], 3),
                     endpoints_max_speed=round(task["endpoints + max speed"], 3), peri_highest=bool(peri.max() > max(kin.max(), task[bt]))))
print("Variant, PD neurons with permutation p < 0.05 (kinematic window a, replication a):")
print(pd.DataFrame(rows).to_string(index=False))'''))

# --- dimensionality peak: against chance
i = find("rows = []\nfor (nm, R), v in F6[\"curves\"].items():")
append(i, '''for R in "ab":
    ch = NULL[("peri", R)].mean(0)
    print(f"S {R}: chance curve of the peri-movement space from {ch[0]:.3f} (k = 1) to {ch[-1]:.3f} (k = 14);",
          f"fall from k = 6 to k = 14 {ch[5] - ch[-1]:.3f}")''')

# --- maze task spaces: chance
i = find("rows = []\nfor seg in [\"segment dirs (t)\", \"segment dirs (l)\"]:")
append(i, '''print("Chance (conditions shuffled):", {k: round(null_task[k], 3) for k in ["segment dirs (t)", "segment dirs (l)", "initial velocity", "endpoints + max speed"]})
print("Selection readings with segment dirs (t) > 0:", sum(F6_all[r_]["task"]["segment dirs (t)"].mean() > 0 for r_ in SEL_READINGS),
      "| initial velocity > 0:", sum(F6_all[r_]["task"]["initial velocity"].mean() > 0 for r_ in SEL_READINGS), "of", len(SEL_READINGS))''')

# --- preparatory dimensionality: cross-validated
i = find("rows = []\nfor r_ in SEL_READINGS:\n    d = condition_data(*r_)\n    prep_ok, _ = neuron_sets(d, \"range\")\n    for nset")
append(i, '''# Noise-corrected variant (verifier, round 1): PCs from the odd-trial condition means, their variance measured as the
# cross product of odd- and even-trial projections (and the reverse, averaged), so that noise independent between the
# halves drops out. Count of PCs for 90% of the summed cross-validated variance. Main selection, window counts.
def cv_dim(A, B):
    Ac, Bc = A - A.mean(0), B - B.mean(0)
    Vt = np.linalg.svd(Ac, full_matrices=False)[2]
    return np.array([(Ac @ v) @ (Bc @ v) for v in Vt])
for nset, mask in [("a PD neurons", pdn), ("b all units", np.ones(len(units), bool))]:
    A_, B_ = halves[0][:, mask], halves[1][:, mask]
    sig = (cv_dim(A_, B_) + cv_dim(B_, A_)) / 2
    cum = np.cumsum(sig) / sig.sum()
    raw = [int(np.searchsorted(np.cumsum(M.explained(Z @ Z.T)), 0.9) + 1) for Z in (A_, B_)]
    print(f"{nset}: cross-validated PCs for 90% = {int(np.searchsorted(cum, 0.9) + 1)}",
          f"| first 10 shares {np.round(sig[:10] / sig.sum(), 3)}",
          f"| plain count on each half {raw}")''')

# --- AP section: label outputs
i = find("## Anterior and posterior sites")
C.insert(i + 1, code('''eg_df = D["nwb"].electrodes.to_dataframe()
print("Electrode table columns:", list(eg_df.columns), "| location by row:",
      {loc: (int(eg_df.index[eg_df.location == loc].min()), int(eg_df.index[eg_df.location == loc].max())) for loc in eg_df.location.unique()},
      "(electrode ids)")
for k, g in D["nwb"].electrode_groups.items():
    print("Group", k, "| location:", g.location, "| description:", g.description, "| device:", g.device.description)
print("Units table columns:", list(D["nwb"].units.colnames), "| description:", D["nwb"].units.description)
print("Location of the electrodes the units reference:", units.electrode_group_in_file.value_counts().to_dict(),
      "| prefix 1 rows", units.electrode_row[units.id_array == 1].min(), "to", units.electrode_row[units.id_array == 1].max(),
      "; prefix 2 rows", units.electrode_row[units.id_array == 2].min(), "to", units.electrode_row[units.id_array == 2].max())
print("Nothing in the units or electrode tables ties id prefix 1 or 2 to PMd or M1.")''', ["sanity"]))

# --- 7C: paper's normalizer
i = find("rng7c = np.random.default_rng(70)")
setsrc(C[i], '''rng7c = np.random.default_rng(70)
prep_ok0 = neuron_sets(d0, "range")[0]
Gu_all = M.grams_per_unit(d0["mv_rate"], M.MOVE_WIN[0])

def half_perf(members, R):
    """6-D peri-movement performance of the PD neurons in `members`, from a space built from
    `members` only, and the upper limit from the same units at 6-D and at its best k. The upper
    limit's T-matrix holds every neuron of the half, the fitted one included (Supplemental
    Experimental Procedures, Estimating the upper limit: "each row containing the mean preparatory
    activity for every neuron"); the variant without the fitted neuron is also returned."""
    mem = np.where(members)[0]
    fit = np.where(members & prep_ok0)[0]
    Gu = Gu_all[mem]; Gt = Gu.sum(0)
    Gp = M.prep_grams(X[:, mem])
    loc = {n: i for i, n in enumerate(mem)}
    peri = np.mean([M.pd_performance_pca(X[:, n], Gt - Gu[loc[n]], [6], R == "b")[0] for n in fit])
    up_in = np.mean([M.pd_performance_pca(X[:, n], Gp.sum(0), KS, R == "b") for n in fit], 0)
    up_ex = np.mean([M.pd_performance_pca(X[:, n], Gp.sum(0) - Gp[loc[n]], KS, R == "b") for n in fit], 0)
    return peri, up_in[5], up_in.max(), up_ex[5], up_ex.max(), len(fit)

rows = []
for R in "ab":
    res = {"all": half_perf(np.ones(len(units), bool), R),
           "array 1": half_perf(units.id_array.values == 1, R),
           "array 2": half_perf(units.id_array.values == 2, R)}
    rand = []
    for _ in range(20):
        m = np.zeros(len(units), bool); m[rng7c.choice(len(units), len(units) // 2, replace=False)] = True
        rand += [half_perf(m, R), half_perf(~m, R)]
    rand = np.array(rand)
    for nm, (p, ui6, uib, ue6, ueb, n) in res.items():
        rows.append(dict(S=R, subset=nm, neurons=n, perf_6d=round(p, 3), upper_6d=round(ui6, 3), upper_best=round(uib, 3),
                         norm_a=round(p / ui6, 3), norm_b=round(p / uib, 3), upper_excl_6d=round(ue6, 3), norm_excl_6d=round(p / ue6, 3)))
    rows.append(dict(S=R, subset="random halves (20 splits)", neurons=rand[:, 5].mean(), perf_6d=round(rand[:, 0].mean(), 3),
                     upper_6d=round(rand[:, 1].mean(), 3), upper_best=round(rand[:, 2].mean(), 3),
                     norm_a=round((rand[:, 0] / rand[:, 1]).mean(), 3), norm_b=round((rand[:, 0] / rand[:, 2]).mean(), 3),
                     upper_excl_6d=round(rand[:, 3].mean(), 3), norm_excl_6d=round((rand[:, 0] / rand[:, 3]).mean(), 3)))
    print(f"S {R}, random halves: normalized (a) SD {(rand[:, 0] / rand[:, 1]).std():.3f}, range {(rand[:, 0] / rand[:, 1]).min():.3f} to "
          f"{(rand[:, 0] / rand[:, 1]).max():.3f}; (b) SD {(rand[:, 0] / rand[:, 2]).std():.3f}")
f7c = pd.DataFrame(rows)
print(f7c.to_string(index=False))
for R in "ab":
    for nrm in ["norm_a", "norm_b", "norm_excl_6d"]:
        t = f7c[f7c.S == R].set_index("subset")[nrm]
        a1, a2, rnd = t["array 1"], t["array 2"], t["random halves (20 splits)"]
        print(f"S {R}, {nrm}: both > 0: {a1 > 0 and a2 > 0}; both within 10% of random ({rnd:.3f}): "
              f"{abs(a1 - rnd) <= 0.1 * abs(rnd) and abs(a2 - rnd) <= 0.1 * abs(rnd)}; array 1 higher: {a1 > a2}")''')
json.dump(nb, open(P, "w"), indent=1, ensure_ascii=False)
open(P, "a").write("\n")
print("ok", len(C))
PYEOF
cp reproduce_churchland_2010.ipynb $TMPDIR/w/nb_backup.ipynb && python $TMPDIR/w/edit_nb.py && git diff --stat
```

```
ok 80
 .../reproduce_churchland_2010.ipynb                | 242 ++++++++++++++++++---
 1 file changed, 214 insertions(+), 28 deletions(-)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
P="reproduce_churchland_2010.ipynb"; nb=json.load(open(P))
for c in nb["cells"]:
    if c["cell_type"]=="code" and "".join(c["source"]).startswith("rng6 = np.random.default_rng(60)"):
        c["metadata"]={"tags":["claim:fig6d-perimovement-best-j-array"]}
json.dump(nb, open(P,"w"), indent=1, ensure_ascii=False); open(P,"a").write("\n")
EOF
git diff reproduce_churchland_2010.ipynb | head -30; date -u
```

```
diff --git a/entries/000139-churchland-2010/reproduce_churchland_2010.ipynb b/entries/000139-churchland-2010/reproduce_churchland_2010.ipynb
index 456020c68..269c784ee 100644
--- a/entries/000139-churchland-2010/reproduce_churchland_2010.ipynb
+++ b/entries/000139-churchland-2010/reproduce_churchland_2010.ipynb
@@ -339,6 +339,44 @@
     "      \"| max\", M.tuning_strength(d0[\"prep\"], \"sd\").max().round(2))"
    ]
   },
+  {
+   "cell_type": "markdown",
+   "id": "265d2940",
+   "metadata": {},
+   "source": [
+    "Noise reference for the 5 spikes/s threshold (added in response to the verifier, round 1). The\n",
+    "paper accepts the lower array threshold \"given the higher signal-to-noise ratio provided by the higher\n",
+    "trial count\" (Methods, Neural recordings and datasets); here there are 6 to 10 trials per condition.\n",
+    "The same range measure on spike counts in the preparatory window, with condition labels shuffled\n",
+    "among the kept trials (200 draws), shows how many units pass from noise alone, and a per-unit\n",
+    "permutation p-value marks the units whose tuning is distinguishable from noise."
+   ]
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && time python tools/entry.py all entries/000139-churchland-2010 2>&1 | tail -15
```

```
Installed kernelspec registry-000139-churchland-2010 in executed/000139-churchland-2010/.venv/share/jupyter/kernels/registry-000139-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (606 s)

real	10m39.869s
user	10m31.924s
sys	0m4.327s
```

**Agent**

Notebook runs cleanly (10 min). Reading the new outputs.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/show.py <<'EOF'
import json, sys
nb = json.load(open("executed/000139-churchland-2010/reproduce_churchland_2010.ipynb"))
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code": continue
    s = "".join(c["source"])
    if not any(s.startswith(k) for k in sys.argv[1:]): continue
    print("=====", i)
    for o in c["outputs"]:
        if "text" in o: print("".join(o["text"])[-6000:])
EOF
python $TMPDIR/w/show.py "n_units" "rng_thr" "def supp1" "rng6" "def fig6d_judge"
```

```
===== 11
Units with a preparatory range above 5 spikes/s (window counts, main selection): observed 75 of 152 | labels shuffled: median 59 range 51 to 67
PD neurons (range above 5 spikes/s): 76 | of them with permutation p < 0.05: 43 | all units with p < 0.05: 56 (expected by chance about 7.6 )
Split-half reliability, PD neurons with permutation p < 0.05: median r 0.611 | the others: 0.141

===== 15
Units: 152 (expected 146 +/- 14.6) -> within tolerance: True
Units per array (id prefix): 1 -> 75 | 2 -> 77 | electrodes per array in the table: {'electrode_group_PMd': 96, 'electrode_group_M1': 96}
Conditions: 27 (expected 108) | mazes 9 x versions 3
maze_id values: [np.int64(12), np.int64(13), np.int64(14), np.int64(20), np.int64(21), np.int64(22), np.int64(83), np.int64(84), np.int64(85)]
Trials per neuron: train+val file 250 ; with the 100 test segments 350 (paper: 2166 in the Results, 2155 in the Methods; reported only)
Session description in the file: Data from monkey Jenkins performing center-out delayed reaching task. This file contains trials from the full session on 2009-09-29 that can be used for training models for the Neural Latents Benchmark.
Trial timeline: first trial starts at 0.0 s; next trial start minus trial end ranges from 0.014 to 0.109 s. The kept trials abut or overlap, so the timeline was rebuilt and cannot show which other trials or conditions the session held.

===== 27
onset  proto  combine                    neurons  n  prep_diff  onset_diff  ratio  a_smaller  b_less_than_half
    a   mean separate            both thresholds 16      0.098       0.027  0.272       True              True
    a   mean separate preparatory only (variant) 85      0.130       0.012  0.094       True              True
    a   mean   concat            both thresholds 17      0.108       0.101  0.942       True             False
    a   mean   concat preparatory only (variant) 76      0.140       0.030  0.213       True              True
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
python $TMPDIR/w/show.py "rows = []
for (nm" "rows = []
for seg" "rows = []
for r_ in SEL_READINGS:
    d = condition_data(*r_)
    prep_ok, _ = neuron_sets(d, \"range\")
    for nset" "eg_df" "rng7c" "rows = []
for r_ in SEL_READINGS:
    for how in [\"range\", \"sd\"]:
        prep_ok"
```

```
===== 42
                space S     k1  best  best_k    k14  above_k1  best_k_2_10  k14_below_best  all_three
                 peri a -0.006 0.117       6 -0.980      True         True            True       True
                upper a -0.014 0.068       5 -0.838      True         True            True       True
kinematic win a rep a a  0.008 0.016       2 -2.005      True         True            True       True
kinematic win a rep b a  0.008 0.016       2 -2.011      True         True            True       True
kinematic win b rep a a  0.011 0.022       2 -2.317      True         True            True       True
kinematic win b rep b a  0.011 0.022       2 -2.319      True         True            True       True
                 peri b -0.004 0.226      13  0.226      True        False            True      False
                upper b -0.015 0.184       8  0.098      True         True            True       True
kinematic win a rep a b  0.007 0.019       4 -0.196      True         True            True       True
kinematic win a rep b b  0.007 0.019       4 -0.196      True         True            True       True
kinematic win b rep a b  0.010 0.024       2 -0.187      True         True            True       True
kinematic win b rep b b  0.009 0.024       2 -0.187      True         True            True       True
('a', 'mean', 'separate') peri best k (S a): 4 k14 below best: True | (S b): 11 True
('a', 'mean', 'concat') peri best k (S a): 6 k14 below best: True | (S b): 13 True
('a', 'medoid', 'separate') peri best k (S a): 2 k14 below best: True | (S b): 11 True
('a', 'medoid', 'concat') peri best k (S a): 6 k14 below best: True | (S b): 14 False
('b', 'mean', 'separate') peri best k (S a): 6 k14 below best: True | (S b): 14 False
('b', 'mean', 'concat') peri best k (S a): 6 k14 below best: True | (S b): 14 False
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls questions | tail -5; cat questions/$(ls questions | tail -1) | head -40; ls schemas
```

```
figshare-24639285.yaml
figshare-24949470.yaml
figshare-26877211.yaml
openneuro-ds002778.yaml
openneuro-ds004752.yaml
# Questions from attempt openneuro-ds004752-dimakopoulos-2022-01 (author revisions after verifier rounds 1
# and 2, 2026-10-28) about claims/openneuro-ds004752/10.7554-elife.78677.yaml, asked under docs/protocol.md,
# "Hand over for verification". The verifier reported these as places where the claims file misreads
# the paper or leaves a test open; the claims were tested as the file has them.
dataset: OPENNEURO:ds004752
paper: doi:10.7554/elife.78677
questions:
- claim: fig4d-reversal-all
  asked: 2026-10-28
  question: Should reading d2 (the minimum of ΔGranger over 4 to 8 Hz in encoding and the maximum in
    maintenance) be kept as a reading that can decide fig4d-reversal-all, table1-heschl-dgranger-correct
    and balanced-correct-subset, and the d2 readings of fig4bc-auditory-strongest, scalp-temporal-laplacian
    and fig4e-lpfc-no-reversal? Taking the minimum in one period and the maximum in the other gives a
    negative encoding value and a positive maintenance value by construction, so the sign pattern these
    criteria test, and the paired test between the periods, hold under d2 whether or not there is a
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
import pprint
def find(d,key,path=''):
    if isinstance(d,dict):
        for k,v in d.items():
            if k==key: print(path+'/'+k); print(json.dumps(v,indent=1)[:3000])
            find(v,key,path+'/'+k)
find(s,'verifications')
"; grep -l "verifications:" attempts/*.yaml | head -3
```

```
/properties/verifications
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A25 "^verifications:" attempts/000005-yu-2016-01.yaml | head -40; git log --oneline -3 -- transcripts/000139/verifier-1-report.md
```

```
222:verifications:
223-- date: 2026-10-19
224-  kind: agent
225-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
226-    notebook)
227-  reviewed: The handover of the first run, the executed notebook with the conclusions and summary
228-    removed, the helper module and the claims file. The verifier also read the paper's public page,
229-    with the supplementary legends.
230-  results:
231-  - claim: vpm-touch
232-    agrees: true
233-    outcome: reproduced
234-    reason: 20 of 24 VPM units are touch-responsive (0.83, criterion at least 0.5), the same test
235-      with spikes moved to the next trial gives 0.00, and results are consistent across all 6 mice.
236-    response: No change of outcome.
237-  - claim: vpm-whisking
238-    agrees: true
239-    outcome: reproduced
240-    reason: 21 of 24 are modulated by the trial-shift test (0.88) and the whisking rate is above the
241-      quiet rate in 23 of 24. On spikes moved one trial the test still marks 0.12 against a nominal
[... 7 more lines not kept]
```

**Agent**

Now updating the conclusion cells and summary with the new numbers.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/edit_md.py <<'PYEOF'
import json
P = "entries/000139-churchland-2010/reproduce_churchland_2010.ipynb"
nb = json.load(open(P)); C = nb["cells"]
def setsrc(cell, s):
    lines = s.split("\n"); cell["source"] = [l + "\n" for l in lines[:-1]] + [lines[-1]]
def find(start):
    hits = [i for i, c in enumerate(C) if "".join(c["source"]).startswith(start)]
    assert len(hits) == 1, (start, hits); return hits[0]
def rep(i, a, b):
    s = "".join(C[i]["source"]); assert a in s, (i, a); setsrc(C[i], s.replace(a, b))
def put(start, s): setsrc(C[find(start)], s)

i = find("# Churchland et al. (2010)")
rep(i, "| fig6-maze-task-spaces | run; blocked after the analysis (methods_underspecified) |", "| fig6-maze-task-spaces | tested |")
rep(i, "| prep-activity-more-anterior | tested (AP read as the array) |", "| prep-activity-more-anterior | run; blocked after the analysis (metadata_insufficient: which array is PMd) |")
rep(i, "or, where the paper is silent, run under every\nreading the claims file names.",
    "or, where the paper is silent, run under every\nreading the claims file names. This version answers the first verification round: the outputs it\nasked for are added in the sections they concern, each marked as added in response to the verifier.")

put("**Result: partially reproduced.** The dandiset holds 152", '''**Result: partially reproduced.** The dandiset holds 152 units (within 146 +/- 14.6) from two
arrays, 75 and 77 by unit id, but 27 conditions (9 mazes in 3 versions), not 108, and 250 labelled
trials per unit (350 with the unlabelled test segments) against the paper's 2166. The criterion's
partial outcome applies because the units match and the conditions are a 27-condition maze set. The
file describes its trials as taken from the session of 2009-09-29, and its rebuilt trial timeline
cannot show whether that session also held other mazes. The paper's J-array dataset interleaved all
108 conditions, so if this session ran only these 27 it is a different recording and the match of
the unit count says nothing about the paper's dataset; nothing in the files settles which.''')

i = find("**Result: reproduced, resting on the reading of the neurons and the time range.**")
rep(i, "zero (p = 0.0036). 22 of 32 combinations meet the criterion.",
    "zero (p = 0.0036). 22 of 32 combinations meet the criterion. The splice maps the go-locked trace\nto movement time with the median RT (354 ms), an assumption: the paper does not say where it splices.\nThe decline under the spliced trace (-263 ms) falls near the splice point (-254 ms).")

put("**Result: reproduced under the claims file's reading (a), not under (b).**", '''**Result: reproduced under the claims file's reading (a), not under (b).** Under the main reading
(17 neurons) the strongest-minus-weakest difference of normalized rate is 0.108 in the preparatory
window and 0.101 at movement onset, a ratio of 0.942: smaller, but not less than half. Under the
separate-profile selections the ratio is 0.184 to 0.357, and with all preparatory neurons 0.047 to
0.213. That the difference shows "little relationship" by onset holds only in those variants.
Ranking and measuring on the same trials favours the claim: with conditions ranked on half the
trials and measured on the other half, the preparatory difference of the 17 neurons falls to 0.040
and the onset difference (0.045) is no longer smaller (ratio 1.115); with all preparatory neurons it
is 0.055 against 0.030 (ratio 0.545). So under the legend's method the claim holds, but on these
data the result for the claim's neurons does not survive cross-validation.''')

put("**Result: reproduced, resting on the tuning measure.** Under the main reading the best", '''**Result: reproduced, resting on the tuning measure.** Under the main reading the best
peri-movement performance is 0.117 (k = 6) with S fixed and 0.226 (k = 13) with S recomputed, above
the best kinematic space (0.016 to 0.024) and the best task space (initial velocity, 0.030) under all
8 combinations of S, kinematic window and replication. Over the selection readings the peri-movement
space is highest under every combination in 7 of 8 and under some in the eighth. All performances are
low: the split-half reliability of the preparatory tuning is a median r of 0.374. The paper's upper
limit, whose T-matrix includes the fitted neuron, is 0.178 (S fixed) and 0.300 (recomputed); the
variant without the fitted neuron (0.068, 0.184) is below the peri-movement best and so is no upper
limit here. Neurons of array 1 carry most of the performance (best 0.291, array 2 -0.006).

Every space is above its chance level at every dimensionality: with conditions shuffled, the
peri-movement space gives -0.120 to -2.732 (S fixed) and -0.102 to -0.308 (recomputed), the task
spaces -0.172 to -1.128, so the paper's "above zero is better than chance" holds here too. Only 59
of 152 units pass the 5 spikes/s range with labels shuffled against 75 observed, and 43 of the 76 PD
neurons have tuning distinguishable from noise (permutation p < 0.05). On those 43 the result is
stronger: peri-movement best 0.336 (S fixed) and 0.415 (recomputed), against 0.116 to 0.117 for the
kinematic space and 0.143 for the best task space (segment directions, time segments).''')

put("**Result: reproduced, resting on the reading of S.**", '''**Result: reproduced, resting on the reading of S.** With S fixed (adopted, below) the
peri-movement curve rises from -0.006 at k = 1 to 0.117 at k = 6 and falls to -0.980 at k = 14; the
kinematic curves peak at k = 2 and fall to about -2. With S recomputed in each fold the peri-movement
curve peaks at k = 13 (0.226), outside 2 to 10, and is nearly flat above k = 10. S fixed is adopted
because the Methods describe one matrix S per space and refit only the PD on the remaining
conditions. The chance curves show that the two readings penalize extra dimensions differently:
with conditions shuffled the peri-movement curve falls by 2.292 from k = 6 to k = 14 with S fixed
and by 0.094 with S recomputed, so under the recomputed reading little decline is possible even for
noise. With S fixed the best k is 2 to 6 in all 8 selection readings.''')

put("**Result: blocked, the segment division is not settled.**", '''**Result: reproduced, resting on segments equal in time.** The claims file names both segment
divisions as readings, and the criterion holds under one: under the main reading segment directions
with segments equal in time (0.008) and initial velocity (0.030) are above zero, and endpoints +
maximum speed (-0.045) falls below the 3-D peri-movement space (0.052 and 0.065, reading a) and below
both (reading b). With segments equal in path length segment directions are below zero (-0.027). All
three are far above their chance levels (-0.429, -0.172 and -0.222). The result is fragile across the
trial selection: segment directions (time) are above zero in 2 of 8 selection readings and initial
velocity in 4. On the 43 PD neurons whose tuning passes the permutation test it is clearer: segment
directions 0.143, initial velocity 0.102, endpoints + maximum speed 0.020.''')

i = find("**Result: not reproduced.** 90% of the variance of the preparatory matrix")
rep(i, "noise more than the structure of preparatory activity.",
    "noise more than the structure of preparatory activity. A count that removes noise independent\nbetween halves of the trials (cross-validated PCA, odd against even trials) gives 7 PCs for both\nthe PD neurons and all units, inside 6.3 to 11, while the plain count on each half gives 15 to 16.\nThe criterion's count is the plain one, so the outcome stands, but the failure is likely due to the\nfew trials per condition here.")

i = find("## Anterior and posterior sites")
setsrc(C[i], '''## Anterior and posterior sites

The electrode table gives no positions (x, y, z are empty), so AP location can only be read as
the array (reading (b) of the claims file): PMd anterior, M1 posterior. The table's location column
puts PMd on electrode ids 1 to 96 and M1 on 97 to 192, but every unit references a PMd row; the
array is read from the unit id (prefix 1 or 2). Prefix 1 is taken as PMd because the electrode table
lists the PMd group first. This is an assumption that the files cannot check (cell below).''')

put("**Result: not reproduced, resting on the tuning measure and on array 1 being PMd.**", '''**Result: blocked (metadata_insufficient), after the analysis.** The direction of the comparison
depends on which array is PMd, and nothing in the files says (cell above). With the range measure 35
of 75 units on array 1 (0.467) and 41 of 77 on array 2 (0.532) pass the preparatory threshold under
the main reading (Fisher p = 0.5165); array 1 has the lower fraction in every selection reading.
With the SD measure array 1 is higher (4 of 75 against 1 of 77, p = 0.2064). If array 1 is PMd the
range result goes against the claim; if it is M1 the result favours it, without reaching p < 0.05 in
any reading. With labels shuffled 59 of 152 units pass the range threshold, so the fractions are
largely noise.''')

put("**Result: not reproduced.** Neither half is within 10%", '''**Result: not reproduced.** With the paper's upper limit (its T-matrix holds every neuron of
the half, the fitted one included; Supplemental Experimental Procedures, Estimating the upper limit)
neither array is within 10% of the random halves under any reading: at 6-D with S fixed array 1 gives
0.761, array 2 -0.402 and random halves 0.455 (SD 0.153 over splits); with S recomputed 0.766, 0.230
and 0.564; at the best k 0.472, -0.374 and 0.350 (S fixed) and 0.438, 0.144 and 0.336 (recomputed).
Array 2 is below zero with S fixed. Array 1 is higher in every reading, which is "anterior higher"
only if array 1 is PMd. The variant without the fitted neuron, which the round-1 notebook used, gives
upper limits at or below zero and ratios from -0.740 to 2.111. Unnormalized 6-D performance is 0.271
on array 1 and -0.060 on array 2 (S fixed; 0.270 and 0.049 recomputed): the peri-movement space
captures tuning on array 1 but hardly on array 2. The within-10% test fails for both halves, so the
outcome does not depend on which array is PMd.''')

i = find("## Summary")
s = "".join(C[i]["source"])
s = s.replace("| suppfig1-population-psth-weak-movement-tuning | reproduced under reading (a) only |",
              "| suppfig1-population-psth-weak-movement-tuning | reproduced under reading (a) only; not under cross-validated ranking |")
s = s.replace("| fig6-maze-task-spaces | blocked: methods underspecified (segment division) |",
              "| fig6-maze-task-spaces | reproduced, resting on segments equal in time |")
s = s.replace("| fig7c-anterior-posterior-performance | not reproduced |",
              "| fig7c-anterior-posterior-performance | not reproduced (paper's upper limit) |")
s = s.replace("| prep-activity-more-anterior | not reproduced, AP read as the array |",
              "| prep-activity-more-anterior | blocked: metadata insufficient (which array is PMd) |")
s = s.replace("speed-task and single-electrode datasets are not in the dandiset.",
              "speed-task and single-electrode datasets are not in the dandiset.\nWith 6 to 10 trials per condition the 5 spikes/s threshold passes 59 of 152 units on shuffled\nlabels (75 observed); only 43 of the 76 PD neurons have tuning distinguishable from noise, and on\nthem the Figure 6 results are stronger.")
s = s.replace("electrode table, although the unit ids", "electrode table (whose location column puts M1 on ids 97 to 192), although the unit ids")
s = s.replace("Nothing in the files links this\nsession (2009-09-29) to the paper's J-array dataset",
              "Nothing in the files links this\nsession (2009-09-29) to the paper's J-array dataset or says which id prefix is PMd")
setsrc(C[i], s)
json.dump(nb, open(P, "w"), indent=1, ensure_ascii=False); open(P, "a").write("\n")
print("ok")
PYEOF
python $TMPDIR/w/edit_md.py
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010; python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
s=''.join([c for c in nb['cells'] if ''.join(c['source']).startswith('## Summary')][0]['source']); print(s[-1800:])"; cat README.md
```

```
|

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The paper's J-array dataset has 108 conditions and
about 2166 trials per neuron; this dandiset has 27 conditions and 6 to 10 kept trials per
condition, so condition means are noisy (split-half reliability of preparatory tuning, median r =
0.374) and every PD performance is low (best about 0.1 to 0.2). The tuning strength is read as the
range across conditions; the SD reading leaves almost no neuron above 5 spikes/s. The proto-trial is
the condition-mean velocity profile with the two profiles concatenated (the reading closest to the
paper's ~90% of trials kept); the other readings are shown. S is fixed across folds where the two
readings differ. AP location is read as the array, and the array from the unit id. EMG, the
speed-task and single-electrode datasets are not in the dandiset.
With 6 to 10 trials per condition the 5 spikes/s threshold passes 59 of 152 units on shuffled
labels (75 observed); only 43 of the 76 PD neurons have tuning distinguishable from noise, and on
them the Figure 6 results are stronger.

**What was found about the dataset.** The units' electrode references all point to PMd rows of the
electrode table (whose location column puts M1 on ids 97 to 192), although the unit ids give 77 units on a second array whose references (rows 14 to
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p="README.md"; s=open(p).read()
s=s.replace("| Segment directions and initial velocity perform reasonably well | Blocked: methods underspecified |","| Segment directions and initial velocity perform reasonably well | Reproduced (segments equal in time) |")
s=s.replace("| Preparatory activity more prevalent anteriorly | Not reproduced |","| Preparatory activity more prevalent anteriorly | Blocked: metadata insufficient (which array is PMd) |")
s=s.replace("from the unit ids.\n","from the unit ids, and the files do not say which id prefix is PMd.\n")
s=s.replace("about seven minutes.","about ten minutes.")
open(p,"w").write(s)
p="entry.yaml"; s=open(p).read(); s=s.replace("runtime_minutes: 7","runtime_minutes: 10"); open(p,"w").write(s)
EOF
git diff --stat; date -u
```

```
entries/000139-churchland-2010/README.md           |   8 +-
 entries/000139-churchland-2010/entry.yaml          |   2 +-
 .../reproduce_churchland_2010.ipynb                | 366 +++++++++++++++++----
 3 files changed, 304 insertions(+), 72 deletions(-)
Wed Oct 28 21:34:01 UTC 2026
```

**Agent**

Now updating the attempt record.

**Agent calls Bash**

```bash
cd  && cat > $TMPDIR/w/edit_att.py <<'PYEOF'
P = "attempts/000139-churchland-2010-01.yaml"
s = open(P).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)

# j-array-recordings
rep("""    the session (2009-09-29) to the paper's J-array dataset.
  deviations:""", """    the session (2009-09-29) to the paper's J-array dataset. The paper's J-array dataset interleaved
    all 108 conditions; the file says its trials come from the full session of 2009-09-29, and its
    trial timeline is rebuilt (each trial starts 0.014 to 0.109 s after the previous one ends), so the
    files cannot show whether that session held other mazes. If it ran only these 27 conditions it is
    a different recording, and the unit count match says nothing about the paper's dataset. Outside
    the notebook (not used for the outcome), the MC_Maze dandiset 000128 of the same benchmark, with
    108 conditions, is a session of 2009-09-25 with 182 units. Whether the criterion's partial clause
    should apply to a session that may not be the J-array recording is asked of a reader
    (questions/000139.yaml).
  deviations:""")

# fig4e
rep("""    maps the go-locked trace (-200 to +100 ms) to movement time with the median RT (354 ms) and
    continues with the movement-locked trace; where the paper splices is not given.""",
"""    maps the go-locked trace (-200 to +100 ms) to movement time with the median RT (354 ms) and
    continues with the movement-locked trace; where the paper splices is not given, and the median RT
    is an assumption. The decline under the spliced trace (-263 ms) falls near the splice point (-254
    ms); the movement-locked trace alone gives -307 ms.""")

# supp1
rep("""    supported under those readings and with all preparatory neurons (ratio 0.047 to 0.213), not
    under the concatenated-profile readings.""",
"""    supported under those readings and with all preparatory neurons (ratio 0.047 to 0.213), not
    under the concatenated-profile readings. Ranking the conditions and measuring on the same noisy
    rates favours the claim. With conditions ranked on half of each condition's trials and measured
    on the other half (main selection), the preparatory difference of the 17 neurons falls to 0.040
    and the onset difference (0.045) is no longer smaller (ratio 1.115); with all 76 preparatory
    neurons it is 0.055 against 0.030 (ratio 0.545). The outcome follows the legend's method, which
    the criterion names; on these data the result for the claim's neurons does not survive
    cross-validation.""")
rep("""    rate is 0.108 in the preparatory window""", """    rate is 0.108 in the preparatory window""")

# fig6d
rep("""    low; the split-half reliability of preparatory tuning is a median r of 0.374 and the estimated
    upper limit (0.068, S fixed) is below the peri-movement best. The array-1 neurons reach 0.291 and
    the array-2 neurons -0.006.""",
"""    low; the split-half reliability of preparatory tuning is a median r of 0.374. The paper's upper
    limit (T-matrix including the fitted neuron) is 0.178 with S fixed and 0.300 recomputed; the
    variant without the fitted neuron (0.068, 0.184) is below the peri-movement best and is no upper
    limit. The array-1 neurons reach 0.291 and the array-2 neurons -0.006. Every space is above its
    chance level (conditions shuffled, 10 draws) at every k; chance is -0.120 to -2.732 for the
    peri-movement space with S fixed, -0.102 to -0.308 recomputed, and -0.172 to -1.128 for the task
    spaces. With 6 to 10 trials per condition the 5 spikes/s threshold passes 59 of 152 units on
    shuffled labels against 75 observed, and 43 of the 76 PD neurons have tuning distinguishable from
    noise (permutation p < 0.05). On those 43 the peri-movement best is 0.336 (S fixed) and 0.415
    (recomputed), against 0.116 to 0.117 kinematic and 0.143 for the best task space.""")

# dimensionality peak
rep("""    and is flat above k = 10 (0.221 to 0.226), so the criterion fails under that reading. With S fixed
    the best k is 2 to 6 in all 8 selection readings.""",
"""    and is flat above k = 10 (0.221 to 0.226), so the criterion fails under that reading. With S fixed
    the best k is 2 to 6 in all 8 selection readings; with S recomputed it is 11 to 14. The chance
    curves (conditions shuffled) show the two readings penalize extra dimensions differently: the
    peri-movement chance curve falls by 2.292 from k = 6 to k = 14 with S fixed and by 0.094 with S
    recomputed, so under the recomputed reading little decline is possible even for noise. The
    verifier would give partially reproduced; the outcome is kept on the adopted reading and the
    disagreement recorded.""")

# maze task spaces
rep("""- claim: fig6-maze-task-spaces
  outcome: blocked
  blocked_by: methods_underspecified
  notebook""", """- claim: fig6-maze-task-spaces
  outcome: reproduced
  assumed: true
  notebook""")
rep("""  notes: Under the main reading initial velocity is above zero (0.030) and endpoints + maximum speed
    (-0.045) is below the 3-D peri-movement space (0.052 S fixed, 0.065 recomputed) and below initial
    velocity. Segment directions are above zero with segments equal in time (0.008) and below with
    segments equal in path length (-0.027), so the two readings give different outcomes, and the
    paper ("the individual horizontal and vertical displacements after dividing the reach trajectory
    into three segments", Methods, Task spaces) does not say which. Neither choice has a basis in the
    paper. In the other selection readings segment directions are -0.156 to 0.008 and initial
    velocity -0.028 to 0.040. The question is asked of the paper's authors (findings).""",
"""  measured:
  - 0.008
  - 0.030
  - -0.045
  notes: The claims file names both segment divisions as readings, and the criterion holds under one.
    Under the main reading segment directions with segments equal in time (0.008) and initial
    velocity (0.030) are above zero, and endpoints + maximum speed (-0.045) is below the 3-D
    peri-movement space (0.052 S fixed, 0.065 recomputed; reading a) and below both (reading b).
    With segments equal in path length segment directions are -0.027, below zero. All three are far
    above their chance levels (conditions shuffled; -0.429, -0.172 and -0.222). The result is
    fragile across the trial selection; segment directions with time segments are above zero in 2
    of 8 selection readings (-0.156 to 0.008) and initial velocity in 4 (-0.028 to 0.040). On the 43
    PD neurons whose tuning passes a permutation test it is clearer (segment directions 0.143,
    initial velocity 0.102, endpoints + maximum speed 0.020). Measured values are segment directions
    (time), initial velocity and endpoints + maximum speed. The segment division is asked of the
    paper's authors (findings).
  deviations:
  - Rests on segments equal in time, the reading under which the criterion holds; the paper ("the
    individual horizontal and vertical displacements after dividing the reach trajectory into three
    segments", Methods, Task spaces) does not say how the segments are divided.
  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.""")

# preparatory dimensionality
rep("""    count is 17, so with 6 to 10 trials per condition it measures noise more than the structure of
    preparatory activity; the paper had about 20 per condition and 108 conditions.""",
"""    count is 17, so with 6 to 10 trials per condition it measures noise more than the structure of
    preparatory activity; the paper had about 20 per condition and 108 conditions. A count that
    removes noise independent between halves of the trials (cross-validated PCA, odd against even
    trials) gives 7 PCs for both the PD neurons and all units, inside 6.3 to 11, while the plain
    count on each half gives 15 to 16. The criterion's count is the plain one, so the outcome stands;
    the failure is likely due to the few trials per condition.""")

# 7C
rep("""  notes: No half is within 10% of the random halves' normalized value under any reading of S or of
    the upper limit. The normalization is unstable because the upper limits are near zero or
    negative (6-D upper limit -0.107 on array 2, -0.043 averaged over random halves, S fixed), so the
    ratios range from -0.740 to 8.000. Unnormalized 6-D performance is 0.271 on array 1 (PMd) and
    -0.060 on array 2 (M1) with S fixed, 0.270 and 0.049 recomputed, against 0.095 and 0.140 for
    random halves; the peri-movement space captures tuning on array 1 but hardly on array 2.""",
"""  notes: With the paper's upper limit (T-matrix including the fitted neuron) neither array is within
    10% of the random halves' normalized value under any reading of S or of the upper limit's
    dimensionality. At 6-D with S fixed array 1 gives 0.761, array 2 -0.402 and random halves 0.455
    (SD 0.153 over the 40 halves); with S recomputed 0.766, 0.230 and 0.564; at the best k of the
    upper limit 0.472, -0.374 and 0.350 (S fixed) and 0.438, 0.144 and 0.336 (recomputed). Array 2 is
    below zero with S fixed. Array 1 is higher in every reading. Since the within-10% test fails for
    both halves, the outcome does not depend on which array is PMd. The variant without the fitted
    neuron, used in round 1, gives upper limits at or below zero and ratios from -0.740 to 2.111.
    Unnormalized 6-D performance is 0.271 on array 1 and -0.060 on array 2 with S fixed, 0.270 and
    0.049 recomputed, against 0.095 and 0.140 for random halves.""")
rep("""  - Random halves are 20 random splits of the units into two equal halves, a standard choice.""",
"""  - Random halves are 20 random splits of the units into two equal halves, a standard choice.
  - The upper limit's T-matrix holds every neuron of the half, the fitted one included, as the
    Supplemental Experimental Procedures (Estimating the upper limit of PD performance) give it, "T
    was c x n with each row containing the mean preparatory activity for every neuron".""")

# prep anterior
rep("""- claim: prep-activity-more-anterior
  outcome: not_reproduced
  assumed: true
  notebook""", """- claim: prep-activity-more-anterior
  outcome: blocked
  blocked_by: metadata_insufficient
  notebook""")
rep("""  notes: With the range measure 35 of 75 units on array 1 (0.467) and 41 of 77 on array 2 (0.532)
    pass the 5 spikes/s preparatory threshold (Fisher p = 0.517), and array 1 has the lower fraction
    in all 8 selection readings. With the SD measure array 1 is higher (4 of 75 against 1 of 77, p =
    0.206). The outcome depends on array 1 being PMd; if it were M1 the range result would favour the
    anterior array (still not at p < 0.05). With 6 to 10 trials per condition the range threshold
    also passes noise, and noise ranges grow with firing rate.
  deviations:
  - AP location read as the array and array 1 taken as PMd (see ap-location-no-effect-j-array);
    tuning measured as the range, as adopted in fig4d-mean-correlation-j-array.""",
"""  notes: Blocked after the analysis. The direction of the comparison depends on which unit id prefix
    is PMd, and the files cannot say; the electrode table's location column puts PMd on ids 1 to 96
    and M1 on 97 to 192, but every unit references a PMd row, the x, y, z columns are empty, and the
    units table has no location. With the range measure 35 of 75 units on array 1 (0.467) and 41 of
    77 on array 2 (0.532) pass the 5 spikes/s preparatory threshold (Fisher p = 0.517), and array 1
    has the lower fraction in all 8 selection readings; with the SD measure array 1 is higher (4 of
    75 against 1 of 77, p = 0.206). If array 1 is PMd the range result goes against the claim; if it
    is M1 it favours it, without reaching p < 0.05 in any reading. With labels shuffled 59 of 152
    units pass the range threshold, so the fractions are largely noise.
  deviations:
  - AP location read as the array; tuning measured as the range, as adopted in
    fig4d-mean-correlation-j-array.""")

# some neurons
rep("""    in at least one other space than in the peri-movement space at its best k (6 and 13).""",
"""    in at least one other space than in the peri-movement space at its best k (6 and 13). One value
    is compared with the best of 12 alternatives on noisy rates, so a large fraction is expected from
    noise alone; the claim asks only for at least one neuron.""")

# finding about segment
rep("""    perform above zero with time segments (0.008) and below with path segments (-0.027), which
    decides fig6-maze-task-spaces, blocked for this reason.""",
"""    perform above zero with time segments (0.008) and below with path segments (-0.027), which
    decides fig6-maze-task-spaces, reproduced under time segments.""")
rep("""  statement: The electrode table's x, y, z and impedance columns are empty, so the anterior-posterior
    location of a unit cannot be read; the array is known only through the unit id convention, which
    the files do not describe.""",
"""  statement: The electrode table's x, y, z and impedance columns are empty, so the anterior-posterior
    location of a unit cannot be read; the array is known only through the unit id convention, which
    the files do not describe, and nothing says whether id prefix 1 or 2 is the PMd array. This
    blocks prep-activity-more-anterior.""")
open(P, "w").write(s)
print("ok")
PYEOF
python $TMPDIR/w/edit_att.py
```

```
ok
```

**Agent**

Now the verifications block.

**Agent calls Bash**

```bash
cat > $TMPDIR/w/ver.py <<'PYEOF'
import textwrap, yaml
R = [
("j-array-recordings", True, "partially_reproduced",
 "152 units, within 146 +/- 14.6. There are 27 conditions (9 mazes x 3 versions), not 108, and 250 trials. The criterion gives partial when units match and conditions are a subset. Caveat, the paper says J-array interleaved all 108 conditions, so this 27-condition session (2009-09-29) is almost certainly a different recording, and the unit match is a coincidence. The notebook never addresses identity, which the claims file left to the author (problem 7).",
 "Outcome kept. The notebook now prints the file's session description and the trial timeline (trials abut, so it is rebuilt and cannot show which other conditions the session held), and the conclusion and notes say that if the session ran only these 27 conditions it is a different recording and the unit match says nothing about the paper's dataset. Whether the criterion's partial clause should apply is asked of a reader in questions/000139.yaml."),
("fig4d-mean-correlation-j-array", True, "partially_reproduced",
 "Mean r is 0.14 to 0.21 across the 8 selection readings (main reading 0.172, t-test p = 0.042) with p < 0.05 in 5 of 8. That is inside 0.054 to 0.231 but outside 0.13 +/- 0.013. The one reading with both means in tolerance (b/medoid/separate, 0.141, 0.119) has p >= 0.08. The main reading passes only on the t-test (Wilcoxon p = 0.071; problem 10). Applying 5 spikes/s to the SD measure leaves 0 neurons, so that reading is degenerate rather than tested (problem 9).",
 "No change of outcome. The notes already state that the main reading passes on the t-test and the Fisher-z test but not the Wilcoxon test, and that the SD reading leaves no neuron; the SD reading is one the claims file names, so it is shown, not dropped."),
("fig4abc-mean-correlation-other-datasets", True, "blocked",
 "The archive API lists 2 assets, both one Jenkins array session. There are no speed-task or single-electrode data.",
 "No change."),
("fig4-broad-unimodal", True, "reproduced",
 "In every reading r runs from about -0.5 to 0.68, mean 0.14 to 0.21, and the dip test p >= 0.195. No neuron has |r| > 0.8. With n = 15 to 20 the dip test has little power.",
 "No change; the notes already state the low power."),
("fig4e-correlation-time-course", True, "reproduced",
 "Borderline. 22 of 32 readings meet the criterion. The value at onset is 0.02 to 0.15, and the decline starts at -257 to -325 ms, at the edge of the -300 to -100 window. In the main selection only splice reading (a) with both thresholds passes. Splice reading (a) maps the go-locked trace using the median RT (354 ms), an author choice not labelled an assumption; the decline times under (a) sit next to the splice at -254 ms, but reading (b) gives similar values (problem 8).",
 "No change of outcome. The median-RT splice is now stated as an assumption in the conclusion and the deviation, with the splice point (-254 ms) next to the decline (-263 ms)."),
("suppfig1-population-psth-weak-movement-tuning", True, "reproduced",
 "Nominal. The onset difference is smaller than the preparatory difference in 16/16 readings and less than half in 12/16; with the main reading's Figure-4 neurons the ratio is 0.94. Conditions are ranked by the same noisy preparatory rates used to measure the preparatory difference, so regression to the mean inflates that difference but not the onset difference, which favours the claim; ranking on odd trials and measuring on even trials would remove it (problem 6).",
 "Outcome kept, as the criterion follows the legend's method. The cross-validated variant was added. With conditions ranked on half the trials and measured on the other half, the 17 neurons give 0.040 (preparatory) against 0.045 (onset), ratio 1.115, so reading (a) fails; all 76 preparatory neurons give 0.055 against 0.030 (ratio 0.545). The conclusion and notes say the result for the claim's neurons does not survive cross-validation."),
("fig6d-perimovement-best-j-array", True, "reproduced",
 "Under every S, kinematic-window and replication reading the peri-movement best (0.117 for S a, 0.226 for S b) beats the kinematic best (<= 0.024) and the task best (0.030). One selection reading (a/medoid/separate) fails, and there all spaces are <= 0. The 5 spikes/s threshold, with about 9 trials per condition, lets most untuned units pass, which dilutes every Figure 6 and 7 magnitude (problem 1). Neither the paper's chance statement nor a null is checked (problem 5). Velocity enters the kinematic space unsmoothed while acceleration comes from smoothed velocity, a minor point (problem 11).",
 "No change of outcome. Added a label-shuffled reference for the threshold (59 of 152 units pass on shuffled labels against 75 observed) and a per-unit permutation test (43 of 76 PD neurons with p < 0.05); on those 43 the peri-movement best is 0.336 and 0.415 against 0.117 kinematic and 0.143 task. Added a chance level for every space (conditions shuffled), all below zero, and every space is above its chance at every k. The paper's upper limit (including the fitted neuron) is now shown, 0.178 and 0.300. The kinematic velocity is left as the dataset's hand velocity; it is not changed because the kinematic best (<= 0.024) is far below the peri-movement best and smoothing a 1 kHz velocity trace with a 20 ms Gaussian cannot close that gap, though this was not run."),
("fig6-perimovement-best-each-dimensionality", True, "reproduced",
 "The peri-movement space wins 90.9 to 95.5% of comparisons in every reading, above the 80% line.",
 "No change."),
("fig6-dimensionality-peak", False, "partially_reproduced",
 "It holds under S reading (a), best k = 6, k = 14 at -0.98. It fails under S (b), best k = 13, k = 14 equals the best, and best k is 11 to 14 in every selection reading. The result rests on an open reading. A random PCA space under S (b) gives about -0.1 flat across k, against -0.18 to -1.34 under S (a), so the missing decline above k = 10 under (b) partly reflects how out-of-sample projection shrinks the left-out condition's scores, and the two S readings are not on the same footing (problem 5).",
 "Outcome kept, reproduced resting on S fixed, with the disagreement recorded. S fixed is the reading adopted from the Methods (one matrix S per space, only the PD refitted), and the outcome is marked as resting on it. The chance curves the verifier asked for were added and agree with its point; the peri-movement chance curve falls by 2.292 from k = 6 to 14 with S fixed and by 0.094 with S recomputed, so the recomputed reading can show little decline even for noise. This is now in the conclusion and the notes."),
("fig6-maze-task-spaces", False, "reproduced",
 "Marginal. Main selection gives segment directions (time-split) 0.008 > 0, initial velocity 0.030 > 0, endpoints + max speed -0.045, below both references. The notebook's blocked, methods_underspecified is not supported, because the criterion supplies the readings (problem 4). It is fragile, segment directions are > 0 in only 2 of 8 selection readings, and the length-split variant fails.",
 "Outcome changed from blocked (methods_underspecified) to reproduced, resting on segments equal in time. The claims file names both segment divisions as readings, and a claim is reproduced when it holds under one of them. Chance levels were added (-0.429, -0.172, -0.222), and the fragility over selection readings is stated (2 of 8 and 4 of 8). On the 43 PD neurons with tuning distinguishable from noise the result is clearer (0.143, 0.102, 0.020)."),
("fig6abc-perimovement-best-other-datasets", True, "blocked",
 "Confirmed on the archive that monkeys A and B, single-electrode J and EMG are absent.",
 "No change."),
("fig6e-summary-rank", True, "blocked",
 "Needs A, B, J and EMG, all absent from the archive.",
 "No change."),
("fig6-preparatory-dimensionality", True, "not_reproduced",
 "12 to 19 PCs reach 90% in all 32 readings, against 6.3 to 11. The shuffled-label reference gives 17, so the count is dominated by noise from about 9 trials per condition (problem 1). A noise-corrected 90%-variance dimensionality, for example cross-validated PCA on split halves, would have settled the conclusion.",
 "No change of outcome. Added cross-validated PCA (odd against even trials); it gives 7 PCs for both the PD neurons and all units, inside 6.3 to 11, against 15 to 16 for the plain count on each half. The notes say the criterion's count is the plain one, so the outcome stands, and that the failure is likely due to the few trials per condition."),
("fig7a-shuffled-space-poor", True, "reproduced",
 "Shuffled best is -0.069 (S a) and -0.010 (S b), below the peri-movement best and below the kinematic and task bests.",
 "No change."),
("fig7b-window-start-slide", True, "reproduced",
 "Fractions are 0.911 / 0.853 / 0.962 / 0.937. Three are within 0.97 +/- 0.097 and all four are within 0.846 to 1.067.",
 "No change."),
("ap-location-no-effect-j-array", True, "reproduced",
 "Regression on array gives p = 0.53 to 0.91 in every reading. The p-value does not depend on which array is anterior, so the unverified labelling (problem 3) does not matter here. Power is low (n = 15 to 20).",
 "No change."),
("ap-location-no-effect-other-datasets", True, "blocked",
 "Single-electrode data are absent from the archive.",
 "No change."),
("fig7c-anterior-posterior-performance", True, "not_reproduced",
 "Within 10% of random halves fails under every reading. Raw 6-D performance for the posterior half is -0.060 (S a) and 0.049 (S b); its normalized > 0 pass under S a only comes from dividing two negative numbers. The upper limit used excludes the fitted neuron, while the Supplemental Experimental Procedures say the preparatory T-matrix holds every neuron, the notebook's own upper incl. neuron curve; the excluding version is not an upper limit on this data and produces meaningless ratios. The paper's reading was never run for 7C (problem 2). The array labels are unverified (problem 3).",
 "No change of outcome. Figure 7C is now run with the paper's upper limit (fitted neuron included) as the main reading, the round-1 variant kept for comparison. Neither array is within 10% of random halves under any reading (6-D, S fixed, 0.761 and -0.402 against 0.455), so the outcome does not depend on which array is PMd; the notes say array 1 is higher, which is anterior only if array 1 is PMd."),
("prep-activity-more-anterior", False, "blocked",
 "Blocked, metadata_insufficient. The direction depends on which id prefix is PMd. The electrode x, y, z are NaN and every unit points at a PMd row, so the file cannot say. As labelled, the range measure gives fewer passing units anterior; swapping the labels reverses that. No reading reaches Fisher p < 0.05. The archive API metadata hold no electrode locations either.",
 "Outcome changed from not_reproduced to blocked, metadata_insufficient, as the verifier gives it. The notebook now prints the electrode table's location column, the electrode groups and the units table columns; none ties an id prefix to PMd or M1. The notes keep the numbers under both labellings and the label-shuffled reference (59 of 152 units pass on noise)."),
("fig7d-pd-consistency", True, "reproduced",
 "The peri-movement space has the higher mean in all comparisons, 0.698 vs 0.597, 0.613 vs 0.605, 0.615 vs 0.542, 0.729 vs 0.670. The segment-directions (time-split) gap is negligible (Wilcoxon p = 0.90).",
 "No change; the notes already call the time-split comparison a tie in practice."),
("some-neurons-better-elsewhere", True, "reproduced",
 "60/76 neurons (S a) and 44/76 (S b) do better in some other space. This is expected from noise when one value is compared with the best of 12 alternatives.",
 "No change of outcome; the notes now say a large fraction is expected from noise and that the claim asks only for at least one neuron."),
("high-dimensional-task-spaces-underperform", True, "reproduced",
 "Kitchen sink (-0.24 / -0.22) and segment directions are below the peri-movement space at the same k and at the best k, under both S readings.",
 "No change."),
("fig8-linear-dynamics-simulation", True, "reproduced",
 "Under the 360-step reading the central 95% of r over 1000 draws (about -0.40 to 0.40) contains 0.08, and performance is 1.0. The check is weak; the distribution is centred on 0 and very wide.",
 "No change; the criterion fixes the test."),
]
def block(key, text, ind):
    assert ": " not in text and " #" not in text, text
    lines = textwrap.wrap(text, 100 - ind - len(key) - 2, break_on_hyphens=False)
    first = f"{' ' * ind}{key}: {lines[0]}"
    rest = textwrap.wrap(" ".join(lines[1:]), 100 - ind - 2, break_on_hyphens=False) if len(lines) > 1 else []
    return "\n".join([first] + [" " * (ind + 2) + l for l in rest])
out = ["verifications:", "- date: 2026-10-28", "  kind: agent",
       "  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the",
       "    notebook), verifier-1",
       "  reviewed: The handover of the first run, the executed notebook with the conclusions and summary",
       "    removed, the helper module and the claims file, with the paper under paper/ and the archive's",
       "    API.", "  results:"]
for c, a, o, r, resp in R:
    out += [f"  - claim: {c}", f"    agrees: {'true' if a else 'false'}", f"    outcome: {o}", block("reason", r, 4), block("response", resp, 4)]
txt = "\n".join(out) + "\n"
P = "attempts/000139-churchland-2010-01.yaml"
s = open(P).read()
assert "verifications:" not in s
s = s.rstrip("\n") + "\n" + txt
open(P, "w").write(s)
d = yaml.safe_load(open(P))
print(len(d["verifications"][0]["results"]), [o["outcome"] for o in d["outcomes"]])
PYEOF
python $TMPDIR/w/ver.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 183,190p attempts/000139-churchland-2010-01.yaml
```

```
at k = 14; the kinematic curves peak at k = 2 (0.016 to 0.022) and fall to about -2 at k = 14.
    With S recomputed in each fold the peri-movement curve peaks at k = 13 (0.226), outside 2 to 10,
    and is flat above k = 10 (0.221 to 0.226), so the criterion fails under that reading. With S fixed
    the best k is 2 to 6 in all 8 selection readings; with S recomputed it is 11 to 14. The chance
    curves (conditions shuffled) show the two readings penalize extra dimensions differently: the
    peri-movement chance curve falls by 2.292 from k = 6 to k = 14 with S fixed and by 0.094 with S
    recomputed, so under the recomputed reading little decline is possible even for noise. The
    verifier would give partially reproduced; the outcome is kept on the adopted reading and the
```

**Agent calls Bash**

```bash
sed -i 's/penalize extra dimensions differently: the/penalize extra dimensions differently; the/' attempts/000139-churchland-2010-01.yaml && python -c "
import yaml; d=yaml.safe_load(open('attempts/000139-churchland-2010-01.yaml'))
print(len(d['verifications'][0]['results']), [(o['claim'],o['outcome']) for o in d['outcomes']])
import re
for i,l in enumerate(open('attempts/000139-churchland-2010-01.yaml')):
    t=l.strip()
    if re.search(r'\S: ', t) and not re.match(r'^(- )?[a-z_]+: ', t): print(i+1, t)
"
```

```
23 [('j-array-recordings', 'partially_reproduced'), ('fig4d-mean-correlation-j-array', 'partially_reproduced'), ('fig4abc-mean-correlation-other-datasets', 'blocked'), ('fig4-broad-unimodal', 'reproduced'), ('fig4e-correlation-time-course', 'reproduced'), ('suppfig1-population-psth-weak-movement-tuning', 'reproduced'), ('fig6d-perimovement-best-j-array', 'reproduced'), ('fig6-perimovement-best-each-dimensionality', 'reproduced'), ('fig6-dimensionality-peak', 'reproduced'), ('fig6-maze-task-spaces', 'reproduced'), ('fig6abc-perimovement-best-other-datasets', 'blocked'), ('fig6e-summary-rank', 'blocked'), ('fig6-preparatory-dimensionality', 'not_reproduced'), ('fig7a-shuffled-space-poor', 'reproduced'), ('fig7b-window-start-slide', 'reproduced'), ('ap-location-no-effect-j-array', 'reproduced'), ('ap-location-no-effect-other-datasets', 'blocked'), ('fig7c-anterior-posterior-performance', 'not_reproduced'), ('prep-activity-more-anterior', 'blocked'), ('fig7d-pd-consistency', 'reproduced'), ('some-neurons-better-elsewhere', 'reproduced'), ('high-dimensional-task-spaces-underperform', 'reproduced'), ('fig8-linear-dynamics-simulation', 'reproduced')]
```

**Agent**

Record parses. Now the reader question for j-array-recordings.

**Agent calls Bash**

```bash
sed -n 40,60p questions/openneuro-ds004752.yaml; python - <<'EOF'
import re
t=open('paper/10.1016-j.neuron.2010.09.015.txt').read()
for k in ['interleaved','27 conditions','108 conditions']:
    for m in re.finditer(k,t): print(k,'::',t[max(0,m.start()-250):m.start()+200].replace('\n',' ')); print('--')
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "questions/000139.yaml",
 "content": "# Questions from attempt 000139-churchland-2010-01 (author revision after verifier round 1,\n# 2026-10-28) about claims/000139/10.1016-j.neuron.2010.09.015.yaml, asked under docs/protocol.md,\n# \"Hand over for verification\". The verifier reported this as a place where the claims file may\n# misread the paper; the claim was tested as the file has it.\ndataset: DANDI:000139\npaper: doi:10.1016/j.neuron.2010.09.015\nquestions:\n- claim: j-array-recordings\n  asked: 2026-10-28\n  question: Should the criterion's partial outcome (\"the units match and the dataset holds a subset of\n    the 108 conditions\") apply to a dataset of 27 conditions? The paper says the J-array dataset\n    interleaved all 108 conditions in one recording, and that 27-condition subsets were used only for\n    the single-electrode monkey J dataset. A session that ran only 27 conditions would then be a\n    different recording from the J-array dataset, and a match of its unit count with the paper's 146\n    would not bear on the claim. Should the claim instead be not reproduced, or blocked as the J-array\n    recording not being in the dataset, when the conditions are not the 108?\n  passage: For the monkey J-array dataset, all 108 conditions were interleaved in the standard way\n    (Methods, Task design); The same 108 conditions were used for the J and J-array datasets. For the\n    former a given neuron was recorded using one of four 27-condition subsets (Figure 3 legend). The\n    criterion cites Methods, Task design for the 27-condition subsets.\n  why: The dandiset holds 152 units over 27 conditions (9 mazes in 3 versions) from a session of\n    2009-09-29, with a rebuilt trial timeline that cannot show whether the session held other mazes.\n    The attempt gives partially reproduced under the criterion as written; the verifier agreed but\n    noted the session is almost certainly a different recording and the unit match a coincidence. If\n    the partial clause does not apply, the outcome would be not reproduced or blocked.\n"
}
```

```
File created successfully at: questions/000139.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
head -8 questions/000005.yaml; grep -rn "questions/" tools/*.py | head -5
```

```
dandiset: "000005"
paper: doi:10.1038/nn.4412
questions:
- claim: fs-vm-touch-whisking
  asked: 2026-10-20
  question: At what resolution is dVm/dt of the touch-aligned average Vm taken for the latency rule,
    the recording's own sampling rate (10 or 20 kHz) or the average in 1 ms bins as for the spike
    PSTH? The same question applies to the laser-onset latencies of exc-thalamus-photoinhibition and
tools/datasets.py:9:files in the repository (claims/, questions/, transcripts/, attempt branches, the paper store) are
```

**Agent calls Bash**

```bash
grep -l "^dataset:" questions/*.yaml | head -3; head -3 $(grep -l "^dataset: DANDI" questions/*.yaml | head -1) 2>/dev/null
```

```
questions/000139.yaml
questions/dryad-4j0zpc8hz.yaml
questions/dryad-bvq83bkk9.yaml
# Questions from attempt 000139-churchland-2010-01 (author revision after verifier round 1,
# 2026-10-28) about claims/000139/10.1016-j.neuron.2010.09.015.yaml, asked under docs/protocol.md,
# "Hand over for verification". The verifier reported this as a place where the claims file may
```

**Agent calls Bash**

```bash
sed -i 's/^dataset: DANDI:000139$/dandiset: "000139"/' questions/000139.yaml && python -c "import yaml;print(yaml.safe_load(open('questions/000139.yaml'))['dandiset'])"; date -u
```

```
000139
Wed Oct 28 21:35:53 UTC 2026
```

**Agent**

Fixing one print statement (trials abut but don't overlap), then the final full run.

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010 && python - <<'EOF'
import json
P="reproduce_churchland_2010.ipynb"; nb=json.load(open(P))
n=0
for c in nb["cells"]:
    s="".join(c["source"])
    a='"s. The kept trials abut or overlap, so the timeline was rebuilt and cannot",\n      "show which other trials or conditions the session held.")'
    if a in s:
        s=s.replace(a,'"s, leaving no room for the failed or other trials a session holds, so the timeline was rebuilt",\n      "and cannot show which other trials or conditions the session held.")'); n+=1
        L=s.split("\n"); c["source"]=[l+"\n" for l in L[:-1]]+[L[-1]]
json.dump(nb,open(P,"w"),indent=1,ensure_ascii=False); open(P,"a").write("\n"); print(n)
EOF
cd  && python tools/entry.py all entries/000139-churchland-2010 2>&1 | tail -4
```

```
1
Installed kernelspec registry-000139-churchland-2010 in executed/000139-churchland-2010/.venv/share/jupyter/kernels/registry-000139-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (623 s)
```

**Agent**

Passes (623 s). Confirming the rerun reproduced the same numbers.

**Agent calls Bash**

```bash
python $TMPDIR/w/show.py "n_units" "rng_thr" | grep -E "Trial timeline|observed|PD neurons"; python $TMPDIR/w/show.py "rng7c" | grep -E "array|random halves \(" | head -8; python $TMPDIR/w/show.py "rng6" | tail -3; python $TMPDIR/w/show.py "def supp1" | tail -5; git status --short
```

```
Units with a preparatory range above 5 spikes/s (window counts, main selection): observed 75 of 152 | labels shuffled: median 59 range 51 to 67
PD neurons (range above 5 spikes/s): 76 | of them with permutation p < 0.05: 43 | all units with p < 0.05: 56 (expected by chance about 7.6 )
Split-half reliability, PD neurons with permutation p < 0.05: median r 0.611 | the others: 0.141
Trial timeline: first trial starts at 0.0 s; next trial start minus trial end ranges from 0.014 to 0.109 s, leaving no room for the failed or other trials a session holds, so the timeline was rebuilt and cannot show which other trials or conditions the session held.
a                   array 1     35.0    0.271     0.356       0.575   0.761   0.472          0.128         2.111
a                   array 2     41.0   -0.060     0.150       0.161  -0.402  -0.374         -0.107         0.560
a random halves (20 splits)     38.0    0.095     0.211       0.277   0.455   0.350         -0.043        -0.711
b                   array 1     35.0    0.270     0.352       0.616   0.766   0.438          0.170         1.581
b                   array 2     41.0    0.049     0.214       0.341   0.230   0.144          0.055         0.892
b random halves (20 splits)     38.0    0.140     0.250       0.417   0.564   0.336          0.084        -0.740
S a, norm_a: both > 0: False; both within 10% of random (0.455): False; array 1 higher: True
S a, norm_b: both > 0: False; both within 10% of random (0.350): False; array 1 higher: True
a       43      0.336            7    -0.164     0.116           3      0.143 segment dirs (t)       0.143     0.102                 0.02          True
b       43      0.415           14     0.415     0.117           3      0.143 segment dirs (t)       0.143     0.102                 0.02          True

           both thresholds 17    cross-validated      0.040       0.045  1.115      False             False
           both thresholds 17 same half (biased)      0.112       0.068  
[... 19 more lines not kept]
```

**Agent**

I've worked through all 12 points in the verifier's report and re-run the entry. `python tools/entry.py all` passes: 0 check errors, the notebook runs in 623 s, and a second run gave the same numbers. Nothing is committed.

## Outcome changes
- **fig6-maze-task-spaces**: blocked (methods_underspecified) → **reproduced**, resting on segments equal in time. The verifier was right that the claims file names both segment divisions, and the criterion holds under one of them. Segment directions score 0.008, initial velocity 0.030 and endpoints + maximum speed −0.045. Chance for those three is −0.429, −0.172 and −0.222. The record says the result is fragile: segment directions are above zero in only 2 of 8 trial-selection readings.
- **prep-activity-more-anterior**: not_reproduced → **blocked (metadata_insufficient)**, as the verifier gave it. The notebook now prints the electrode location column, the electrode groups and the units columns. None of them says whether unit-id prefix 1 or 2 is the PMd array.
- **fig6-dimensionality-peak**: kept as reproduced, resting on S computed once from all conditions (the reading I took from the Methods). The verifier would give partially reproduced, and the record says so. The new chance curves support its point: with conditions shuffled, the curve falls 2.292 from k = 6 to 14 with S fixed but only 0.094 with S recomputed in each fold.

## Added or corrected
- **5 spikes/s threshold (problem 1)**: with condition labels shuffled, 59 of 152 units still pass, against 75 observed. Only 43 of the 76 neurons used for the preferred-direction analyses have tuning distinguishable from noise. On those 43 the Figure 6 result is stronger: peri-movement best 0.336, against 0.116 kinematic and 0.143 task.
- **Chance levels (problem 5)**: every space is below zero by chance and above its chance level at every dimensionality, which supports the paper's "above zero is better than chance".
- **Figure 7C (problem 2)**: now run with the paper's upper limit, which includes the fitted neuron (Supplemental Experimental Procedures: "every neuron"). It stays **not reproduced**: array 1 scores 0.761, array 2 −0.402 and random halves 0.455. Neither half is within 10% of random, so the outcome doesn't depend on which array is PMd.
- **Supplemental Figure 1 (problem 6)**: added a version that ranks conditions on half the trials and measures on the other half. For the claim's 17 neurons the onset difference (0.045) is then no longer smaller than the preparatory one (0.040). I kept the outcome as **reproduced**, because the criterion follows the paper's legend and the verifier agreed with it. The notes say plainly that the result doesn't survive cross-validation.
- **Preparatory dimensionality**: a noise-corrected count (cross-validated PCA) gives 7 PCs, inside 6.3 to 11. The outcome stays **not reproduced**, since the criterion uses the plain count (12). The notes say the failure is likely due to the few trials per condition.
- **Recording identity (problem 7)**: the notebook prints the file's session description and shows the trial timeline was rebuilt. I added a reader question to `questions/000139.yaml`: does the criterion's partial clause fit a 27-condition session, when the paper says the J-array recording interleaved all 108 conditions?
- **Smaller fixes**: the median reaction-time splice in fig4e is now labelled an assumption (problem 8), and the some-neurons-better-elsewhere notes now say most of its fraction is expected from noise.
- The README, the summary, the header, the runtime (10 min) and the `verifications` round-1 record are updated.

## Not done
- **Unsmoothed kinematic velocity (problem 11)**: not changed. The kinematic best (≤ 0.024) is far below the peri-movement best. I said why in the record but did not run the smoothed version.
- **SD tuning measure (problem 9)**: it leaves no neurons, but it is a reading the claims file names, so it stays shown rather than dropped.
- I did not rerun the Figure 4 correlations on the 43 noise-robust neurons.
- One unused check: outside the notebook, I looked up the benchmark's 108-condition dandiset 000128. It is a 2009-09-25 session with 182 units. The record mentions this but no outcome relies on it.

## End of run

54 turns, 39 minutes, result: success.
