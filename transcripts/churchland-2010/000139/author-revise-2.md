# 000139 · author-revise-2 · run 40776557344

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000139/verifier-2-report.md; ls entries/000139-churchland-2010 entries/000139-churchland-2010/*
```

```
Wed Oct 28 22:02:58 UTC 2026
# Round 2 verification: Churchland et al. (2010) on DANDI:000139, version 0.220113.0408

Counts below come from the claims file and the attempt record: 23 claims, 23 outcomes. Cell numbers refer to the current notebook, which is renumbered since round 1.

## 1. Outcomes

| Claim | Outcome in the record | Agree? | Notes on the assumption |
|---|---|---|---|
| j-array-recordings | partially_reproduced | Yes, with a caveat | The criterion's "partial" needs the 27 conditions to be a subset of the paper's 108. The notes say this "cannot be shown", yet the outcome is not marked `assumed: true`. It should be. |
| fig4d-mean-correlation-j-array | partially_reproduced (assumed) | Yes | The tuning measure (range) and the proto-trial (condition mean, profiles concatenated) are stated and reasonable. The main reading passes on the t-test only (p = 0.042), and 3 of 8 selection readings fail (cell 18). |
| fig4abc-mean-correlation-other-datasets | blocked, data_missing | Yes | |
| fig4-broad-unimodal | reproduced (assumed) | Yes | Low power is stated. |
| fig4e-correlation-time-course | reproduced (assumed) | Yes, borderline | The splice assumption is stated, but its consequence is understated (§3). |
| suppfig1-population-psth-weak-movement-tuning | reproduced (assumed) | Yes, nominally | Criterion reading (a) holds in 16 of 16 rows. The cross-validated ranking breaks it for the claim's 17 neurons (ratio 1.115, cell 27). The record says so plainly. |
| fig6d-perimovement-best-j-array | reproduced (assumed) | Yes | Holds under all 8 combinations of the S, kinematic-window and replication readings. It is clearer on the 43 units whose tuning passes a permutation test (cell 36). |
| fig6-perimovement-best-each-dimensionality | reproduced (assumed) | Yes | 0.909 to 0.955 (cell 39). |
| fig6-dimensionality-peak | reproduced (assumed, S fixed) | **Yes. I am changing my round-1 position.** | The new chance curves show the recomputed-S reading cannot produce 
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; wc -l entries/000139-churchland-2010/*; ls questions/ | grep 139; ls attempts 2>/dev/null | head; git show --stat HEAD~1 | head -30
```

```
1:# Protocol for an attempt
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
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 409,500p docs/protocol.md; cat attempts/000139-churchland-2010-01.yaml | head -80; grep -n "verifications" -A60 attempts/000139-churchland-2010-01.yaml | head -120
```

```
### 5. Record the attempt

Write `attempts/<entry name>-<nn>.yaml`.

- **One outcome per claim**, including blocked ones. The outcome describes the
  result, not the method:
  - `reproduced`: the result matches the claim.
  - `partially_reproduced`: the effect is present but weaker, or holds only in
    part.
  - `not_reproduced`: the analysis ran and the result differs.
  - `blocked`: the claim could not be tested; give `blocked_by` and say why.
    When the paper states a chance level or false-positive rate for a
    selection, compute it with your procedure. If yours is far from the
    paper's, the procedures differ, and the outcome is `blocked` with
    `methods_underspecified` even though the analysis ran.

  The criterion decides the outcome. Where the claim's statement says more
  than the criterion tests (a p-value, a second condition), the notes say
  whether that part holds.
- **`deviations`**: every way the test differed from the paper's method or
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "fig4e\|suppfig1\|fig7c\|j-array-recordings" attempts/000139-churchland-2010-01.yaml | head -40; cat entries/000139-churchland-2010/README.md; cat questions/000139.yaml | tail -40
```

```
23:- claim: j-array-recordings
26:  output: claim:j-array-recordings
101:- claim: fig4e-correlation-time-course
105:  output: claim:fig4e-correlation-time-course
120:- claim: suppfig1-population-psth-weak-movement-tuning
124:  output: claim:suppfig1-population-psth-weak-movement-tuning
289:- claim: fig7c-anterior-posterior-performance
293:  output: claim:fig7c-anterior-posterior-performance
436:  - claim: j-array-recordings
473:  - claim: fig4e-correlation-time-course
484:  - claim: suppfig1-population-psth-weak-movement-tuning
596:  - claim: fig7c-anterior-posterior-performance
# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000139

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
be tested on [DANDI:000139](https://dandiarchive.org/dandiset/000139/0.220113.0408) (MC_Maze_Medium).
The dandiset holds one session of monkey J on the maze task, with two Utah arrays (152 units) and 250
labelled trials over 27 conditions, cut for the Neural Latents Benchmark. The paper's J-array dataset
had 108 conditions and about 2166 trials per neuron, so every measure here rests on far fewer trials.
The speed-task and single-electrode datasets and the EMG are not in the dandiset.
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010; python - <<'E'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(f"=== cell {i} [{c['cell_type']}] {len(s)} chars")
    print(s[:300].replace('\n','\n   '))
E
```

```
=== cell 0 [markdown] 2599 chars
# Churchland et al. (2010) on dandiset 000139 (MC_Maze_Medium)
   
   **Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
   activity: representation of movement or first cog in a dynamical machine? *Neuron* 68, 387-400.
   doi:10.1016/j.neuron.2010.09.015.
   
   **Dat
=== cell 1 [code] 372 chars
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
[... 505 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [16,24,25,28,37,72,79]:
    c=nb['cells'][i]
    print(f"=== cell {i}");print(''.join(c['source']))
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            print('--OUT--'); print(''.join(o.get('text', o.get('data',{}).get('text/plain',''))))
E
```

```
=== cell 16
**Result: partially reproduced.** The dandiset holds 152 units (within 146 +/- 14.6) from two
arrays, 75 and 77 by unit id, but 27 conditions (9 mazes in 3 versions), not 108, and 250 labelled
trials per unit (350 with the unlabelled test segments) against the paper's 2166. The criterion's
partial outcome applies because the units match and the conditions are a 27-condition maze set. The
file describes its trials as taken from the session of 2009-09-29, and its rebuilt trial timeline
cannot show whether that session also held other mazes. The paper's J-array dataset interleaved all
108 conditions, so if this session ran only these 27 it is a different recording and the match of
the unit count says nothing about the paper's dataset; nothing in the files settles which.
=== cell 24
def corr_trace(prep, rate):
    """prep (c, n), rate (c, n, T) -> per-neuron correlation at each time (n, T)."""
    a = prep - prep.mean(0)
    b = rate - rate.mean(0)
    num = (a[:, :, None] * b).sum(0)
    den = np.sqrt((a ** 2).sum(0))[:, None] * np.sqrt((b ** 2).sum(0))
    return num / den

rt_med = int(np.median(tr.rt[d0["sel"]]))
def fig4e_traces(d, mask):
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
c=nb['cells'][24]
for o in c.get('outputs',[]):
    print(''.join(o.get('text', o.get('data',{}).get('text/plain',''))))
E
grep -n "fig4e-correlation-time-course" -A40 ../../claims/000139/*.yaml | head -60
```

```
202:- id: fig4e-correlation-time-course
203-  statement: The correlation between preparatory tuning and peri-movement activity at a single
204-    time point begins to decline about 200 ms before movement onset and is near zero by movement
205-    onset.
206-  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 2; Figure
207-    4E
208-  quote: The correlation with preparatory activity began to decline ∼200 ms prior to movement
209-    onset, and reached values near zero by movement onset
210-  depends_on:
211-  - fig4d-mean-correlation-j-array
212-  criterion: Per neuron, the preparatory rate vector correlated with the vector of
213-    condition-mean rates at each single time point (20 ms Gaussian, Figure 4E legend), averaged
214-    over neurons. The trace is the one spliced from the go-cue-locked and movement-locked means
215-    (Supplemental Experimental Procedures, Computing the mean firing rate, which names Figure 4E);
216-    where the splice falls is not given. Open, the time range, which the paper does not give
217-    beyond starting where preparatory tuning is correlated with itself (Figure 4E legend);
218-    readings (a) the spliced trace from the preparatory window through 100 ms after movement
219-    onset, (b) the movement-locked trace alone from 400 ms before to 100 ms after onset. Open, the
220-    neurons; readings (a) those of Figure 4A to 4D (both thresholds), (b) all neurons
221-    passing the preparatory threshold. Open, "near zero"; readings (a) the mean at onset is not
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../..; ls executed/000139-churchland-2010/ 2>/dev/null; sed -n 340,408p docs/protocol.md | head -80; cat tools/entry.py | grep -n "def \|add_parser\|argv" | head -40
```

```
### 3. Write the entry

An entry is a directory `entries/<folder>-<first author>-<year>/` holding
`entry.yaml`, `requirements.in`, one or more notebooks, and usually a helper
module.

- **Stream the data** from the archive, at a pinned version of the dataset
  ([archives.md](archives.md)). Do not download files to disk or read local
  paths.
- **Compute every result from the data.** No embedded numbers, arrays or
  images, and no figures read from files.
- **Fix every random seed**, and give each claim's section its own generator,
  so that adding a cell earlier does not change its numbers.
- **Put loading and reusable measures in a helper module**, so later notebooks
  on the dataset can import it. Say in its docstring where a parameter comes
  from: the claim's criterion (which cites the paper or its code), the
  passage of the paper it was taken from (author, step 1.6), an assumption
  (say what and why), or a standard choice for a detail that cannot change a
  result (say so).
- **Keep it fast.** Reduce the data to what the analysis needs as it loads.
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000139-churchland-2010 2>&1 | tail -15; ls executed/000139-churchland-2010/
```

```
Installed kernelspec registry-000139-churchland-2010 in executed/000139-churchland-2010/.venv/share/jupyter/kernels/registry-000139-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (642 s)

real	11m18.213s
user	11m11.237s
sys	0m5.208s
reproduce_churchland_2010.ipynb
result.json
```

**Agent calls Bash**

```bash
python - <<'E'
import json
nb=json.load(open('executed/000139-churchland-2010/reproduce_churchland_2010.ipynb'))
for i in [3,24,36,71]:
  c=nb['cells'][i]
  print("=== cell",i)
  for o in c.get('outputs',[]):
    print(''.join(o.get('text', o.get('data',{}).get('text/plain',''))))
E
```

```
=== cell 3
Assets at 0.220113.0408
  sub-Jenkins/sub-Jenkins_ses-medium_desc-test_ecephys.nwb  695928 bytes
  sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb  76604764 bytes
Subject: Jenkins Macaca mulatta | session start 2009-09-29 00:00:00-07:00
Train file: trials 250 | splits {'train': 188, 'val': 62} | success {True: 250}
Test file: trials 100 columns ['start_time', 'stop_time', 'move_onset_time', 'split'] | units 114
Conditions (trial_type x trial_version): 27 | maze_id values: 9 | trial_version counts: {0: 81, 1: 86, 2: 83}
Each condition has one maze_id: True
Trials per condition: min 8 max 10
num_targets by version: {0: array([1]), 1: array([1]), 2: array([3])} | barriers by version: {0: [np.int64(0)], 1: [np.int64(8), np.int64(9)], 2: [np.int64(8), np.int64(9)]}
Delay (ms): range -3 to 998 | trials with delay > 400 ms: 235
Delay column equals go - target times (ms): max |diff| 0.0
rt column equals move - go times (ms): max |diff| 0.0 | rt range 247 989 | median 355.0
Trial duration (s): 2.066 to 4.066 | movement onset to trial end at least 0.959 s | trial start to movement onset at least 0.988 s

Units: 152 | heldout 38 | held-in 114
Spike times sorted in every unit: True
Spikes per unit: min 89 max 9891
Test-file units are the held-in train units: True
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "PREP\s*=\|GO_WIN\s*=\|MOVE_WIN\s*=" entries/000139-churchland-2010/maze.py; sed -n 95,125p attempts/000139-churchland-2010-01.yaml; sed -n 285,310p attempts/000139-churchland-2010-01.yaml; grep -n "round\|^- date\|reviewed" attempts/000139-churchland-2010-01.yaml | tail; tail -30 attempts/000139-churchland-2010-01.yaml
```

```
59:GO_WIN = (-600, 500)      # stored go-locked bins
60:MOVE_WIN = (-600, 1000)   # stored move-locked bins
61:PREP = (-200, 100)        # relative to go cue
  notes: In every selection reading the per-neuron correlations run from negative (-0.36 to -0.50)
    to positive (0.54 to 0.68) values, the mean is 0.141 to 0.207, no neuron has |r| > 0.8 while 13
    to 18 have |r| < 0.5, and Hartigan's dip test does not reject unimodality (p = 0.195 to 0.993).
    Main reading n = 17, SD 0.321, dip p = 0.788. With 15 to 20 neurons the test has little power.
  deviations:
  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.
- claim: fig4e-correlation-time-course
  outcome: reproduced
  assumed: true
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig4e-correlation-time-course
  notes: With the neurons of Figure 4D and the spliced trace, mean r is 0.703 at 400 ms before onset,
    0.492 at 200 ms before and 0.118 at onset (not above zero, t-test p = 0.127), and the decline
    begins at -263 ms. These two readings meet the criterion in 7 of 8 selection readings. The
    movement-locked trace alone puts the decline at -307 ms, just outside -300 to -100, and with all
    preparatory neurons the onset value (0.107, n = 76) is above zero (p = 0.0036) and above 0.1;
    22 of 32 combinations meet the criterion.
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010 && python - <<'E'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
c=nb['cells'][24]; s=''.join(c['source'])
old='print("Median RT used for the splice (ms):", rt_med)\n'
assert old in s
s=s.replace(old, old+'''print("Go-locked part of the splice: go cue -200 to +100 ms, the preparatory window", M.PREP,
      "| mapped to", -200 - rt_med, "to", 100 - rt_med, "ms from movement onset")
print("Readings meeting the criterion, of 8 selection readings, by neurons and time range:")
print(f4e.assign(meets=ok4e).groupby(["neurons", "time_range"]).meets.sum().to_string())
''')
lines=s.split('\n'); c['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
git diff --stat; tail -c 50 reproduce_churchland_2010.ipynb | od -c | tail -3
```

```
entries/000139-churchland-2010/reproduce_churchland_2010.ipynb | 4 ++++
 1 file changed, 4 insertions(+)
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent calls Bash**

```bash
cd ../..; python - <<'E'
import json
nb=json.load(open('executed/000139-churchland-2010/reproduce_churchland_2010.ipynb'))
print(''.join(nb['cells'][0]['source']))
for o in nb['cells'][11]['outputs']: print(''.join(o.get('text','')))
print(''.join(nb['cells'][78]['source']))
E
```

```
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
reading the claims file names. This version answers the first verification round: the outputs it
asked for are added in the sections they concern, each marked as added in response to the verifier.

| Claim | Tested here |
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010 && python - <<'E'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
def setsrc(i, s):
    lines=s.split('\n'); nb['cells'][i]['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
def rep(i, old, new):
    s=''.join(nb['cells'][i]['source']); assert old in s, (i, old); setsrc(i, s.replace(old,new))

rep(0, """This version answers the first verification round: the outputs it
asked for are added in the sections they concern, each marked as added in response to the verifier.""",
"""This version answers the first and second verification rounds: the outputs they
asked for are added in the sections they concern, each marked as added in response to the verifier.""")

setsrc(16, """**Result: partially reproduced, resting on the 27 conditions being among the paper's 108.** The
dandiset holds 152 units (within 146 +/- 14.6) from two arrays, 75 and 77 by unit id, but 27
conditions (9 mazes in 3 versions), not 108, and 250 labelled trials per unit against the paper's
2166. The test file adds 100 unlabelled segments for the 114 held-in units only; the 38 held-out
units have the 250 trials alone. The criterion's partial outcome applies when the units match and
the conditions are a subset of the 108; that these 27 are among them is assumed, as nothing in the
files shows it. The file describes its trials as taken from the session of 2009-09-29, and its
rebuilt trial timeline cannot show whether that session also held other mazes. The paper's J-array
dataset interleaved all 108 conditions, so if this session ran only these 27 it is a different
recording and the match of the unit count says nothing about the paper's dataset; nothing in the
files settles which.""")

setsrc(25, """**Result: reproduced, resting on the reading of the neurons and the time range; in the main
selection it rests on the splice.** With the neurons of Figure 4D and the spliced trace (readings a,
a: the legend places 4E with 4A to 4D, and the Supplemental Experimental Procedures name the spliced
trace for 4E), the main reading gives a mean r of 0.703 at 400 ms before onset, 0.492 at 200 ms
before and 0.118 at onset, not above zero (t-test p = 0.1267), and the decline begins at -263 ms.
These two readings meet the criterion in 7 of 8 selection readings.

The splice decides this result. Its go-locked part, go cue -200 to +100 ms, is the preparatory
window itself, mapped to movement time with the median RT (354 ms, an assumption: the paper does not
say where it splices) as -554 to -254 ms. The reference value at 400 ms before onset is therefore
taken inside the window the preparatory rate is averaged over, and the decline at -263 ms is the end
of that window shifted by the median RT, not a time read from the data. In the main selection no
other combination meets the criterion: with the movement-locked trace alone the decline begins at
-307 ms, just outside -300 to -100, and with all preparatory neurons the onset value (0.107) is above
zero (p = 0.0036) and above 0.1. Without the splice the criterion is met by the movement-locked trace
with all preparatory neurons in 6 of 8 selection readings (decline at -283 to -299 ms, onset value
0.054 to 0.098) and with the neurons of Figure 4D in 3 of 8 (decline at -298 to -300 ms, at the edge
of the window). So the outcome holds under the criterion through those readings, with the decline at
the early edge of -300 to -100 ms. 22 of 32 combinations meet the criterion.""")

rep(37, """Every space is above its chance level at every dimensionality: with conditions shuffled, the
peri-movement space gives -0.120 to -2.732 (S fixed) and -0.102 to -0.308 (recomputed), the task
spaces -0.172 to -1.128, so the paper's "above zero is better than chance" holds here too. Only 59
of 152 units pass the 5 spikes/s range with labels shuffled against 75 observed, and 43 of the 76 PD
neurons""", """Chance was computed for the peri-movement space, the kinematic space with window a and
replication a (both readings of S) and the task spaces, and each is above its chance level at every
dimensionality: with conditions shuffled, the peri-movement space gives -0.120 to -2.732 (S fixed)
and -0.102 to -0.308 (recomputed), the task spaces -0.172 to -1.128, so the paper's "above zero is
better than chance" holds for these spaces. Chance was not computed for kinematic window b,
replication b or the upper limits. With labels shuffled a median of 59 of 152 units pass the
5 spikes/s range, against 75 observed, so noise alone matches most of the passing count; 43 of the 76 PD
neurons""")

rep(72, """gives
upper limits at or below zero and ratios from -0.740 to 2.111.""", """gives
6-D upper limits from -0.107 to 0.170, at or below zero in 2 of 8 (array 2 and random halves, S
fixed), and ratios from -0.740 to 2.111.""")

rep(79, "every PD performance is low (best about 0.1 to 0.2)", "every PD performance is low (best 0.117 with S fixed, 0.226 recomputed)")
rep(79, "the 5 spikes/s threshold passes 59 of 152 units on shuffled\nlabels (75 observed);", "the 5 spikes/s threshold passes a median of 59 of 152 units on\nshuffled labels (75 observed);")
rep(79, "| fig4e-correlation-time-course | reproduced, resting on readings |", "| fig4e-correlation-time-course | reproduced, resting on readings; in the main selection on the splice |")
rep(79, "| j-array-recordings | partially reproduced (152 units, but 27 of the 108 conditions and 250 trials) |", "| j-array-recordings | partially reproduced (152 units, but 27 conditions, assumed among the 108, and 250 trials) |")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
git diff --stat
```

```
.../reproduce_churchland_2010.ipynb                | 78 ++++++++++++++--------
 1 file changed, 49 insertions(+), 29 deletions(-)
```

**Agent calls Bash**

```bash
cd ../.. && python - <<'E'
p='entries/000139-churchland-2010/README.md'
s=open(p).read()
R=[("| 146 units, 108 conditions in the J-array dataset | Partially reproduced |","| 146 units, 108 conditions in the J-array dataset | Partially reproduced (27 conditions, assumed among the 108) |"),
("| Correlation declines from 200 ms before onset to near zero | Reproduced |","| Correlation declines from 200 ms before onset to near zero | Reproduced; in the main selection only through the splice, elsewhere with the decline near -300 ms |"),
("| Population PSTHs show weak movement tuning by onset | Reproduced |","| Population PSTHs show weak movement tuning by onset | Reproduced under reading (a) only; not under cross-validated ranking |"),
("| Performance peaks at middle dimensionality | Reproduced |","| Performance peaks at middle dimensionality | Reproduced, resting on S fixed across folds |"),
("| Linear dynamical system simulation (Figure 8) | Reproduced |","| Linear dynamical system simulation (Figure 8) | Reproduced (full-cycle reading of the gray interval) |"),
("(the proto-trial, the\ntuning measure, whether the PCA space is recomputed in each cross-validation fold)",
 "(the proto-trial, the\ntuning measure, whether the PCA space is recomputed in each cross-validation fold, where the Figure 4E\ntrace is spliced, and the length of the Figure 8 gray interval)")]
for a,b in R:
    assert a in s, a; s=s.replace(a,b)
open(p,'w').write(s)
E
grep -n "readings of methods" -A3 entries/000139-churchland-2010/README.md
```

```
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
AssertionError: (the proto-trial, the
tuning measure, whether the PCA space is recomputed in each cross-validation fold)
36:Several outcomes rest on readings of methods the paper leaves open (the proto-trial, the tuning
37-measure, whether the PCA space is recomputed in each cross-validation fold); the notebook runs each
38-reading, and the attempt record,
39-[`attempts/000139-churchland-2010-01.yaml`](../../attempts/000139-churchland-2010-01.yaml), says which
```

**Agent calls Bash**

```bash
python - <<'E'
p='entries/000139-churchland-2010/README.md'
s=open(p).read()
R=[("| 146 units, 108 conditions in the J-array dataset | Partially reproduced |","| 146 units, 108 conditions in the J-array dataset | Partially reproduced (27 conditions, assumed among the 108) |"),
("| Correlation declines from 200 ms before onset to near zero | Reproduced |","| Correlation declines from 200 ms before onset to near zero | Reproduced; in the main selection only through the splice, elsewhere with the decline near -300 ms |"),
("| Population PSTHs show weak movement tuning by onset | Reproduced |","| Population PSTHs show weak movement tuning by onset | Reproduced under reading (a) only; not under cross-validated ranking |"),
("| Performance peaks at middle dimensionality | Reproduced |","| Performance peaks at middle dimensionality | Reproduced, resting on S fixed across folds |"),
("| Linear dynamical system simulation (Figure 8) | Reproduced |","| Linear dynamical system simulation (Figure 8) | Reproduced (full-cycle reading of the gray interval) |"),
("(the proto-trial, the tuning\nmeasure, whether the PCA space is recomputed in each cross-validation fold)",
 "(the proto-trial, the tuning\nmeasure, whether the PCA space is recomputed in each cross-validation fold, where the Figure 4E\ntrace is spliced, the length of the Figure 8 gray interval)")]
for a,b in R:
    assert a in s, a; s=s.replace(a,b)
open(p,'w').write(s)
E
git diff entries/000139-churchland-2010/README.md | head -50
```

```
diff --git a/entries/000139-churchland-2010/README.md b/entries/000139-churchland-2010/README.md
index 7dcca41b4..6314b5e64 100644
--- a/entries/000139-churchland-2010/README.md
+++ b/entries/000139-churchland-2010/README.md
@@ -9,14 +9,14 @@ The speed-task and single-electrode datasets and the EMG are not in the dandiset
 
 | Claim | Outcome |
 |---|---|
-| 146 units, 108 conditions in the J-array dataset | Partially reproduced |
+| 146 units, 108 conditions in the J-array dataset | Partially reproduced (27 conditions, assumed among the 108) |
 | Mean preparatory vs peri-movement correlation 0.13 (J-array) | Partially reproduced |
 | Correlations broad and unimodal | Reproduced |
-| Correlation declines from 200 ms before onset to near zero | Reproduced |
-| Population PSTHs show weak movement tuning by onset | Reproduced |
+| Correlation declines from 200 ms before onset to near zero | Reproduced; in the main selection only through the splice, elsewhere with the decline near -300 ms |
+| Population PSTHs show weak movement tuning by onset | Reproduced under reading (a) only; not under cross-validated ranking |
 | Peri-movement space gives the best PD performance | Reproduced |
 | Peri-movement space best at almost every dimensionality | Reproduced |
-| Performance peaks at middle dimensionality | Reproduced |
+| Performance peaks at middle dimensionality | Reproduced, resting on S fixed across folds |
[... 21 more lines not kept]
```

**Agent**

Notebook and README text are fixed. Next: the question for a reader about fig7c, then the attempt record.

**Agent calls Bash**

```bash
grep -n "id: fig7c" -A22 claims/000139/*.yaml; grep -n "Figure 7\|7C\|randomly divided" paper/*.txt | grep -v nature | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat >> questions/000139.yaml <<'E'
- claim: fig7c-anterior-posterior-performance
  asked: 2026-10-28
  question: The criterion reads "only slightly different" as within 10% of the random halves'
    normalized value. On this dataset the random halves themselves vary far more than that (SD 0.153
    around 0.455 with S fixed, range 0.067 to 0.869 over 40 halves), so a band of +/- 0.046 would
    usually reject a random half. Should "only slightly different" instead be judged against the
    spread of the random halves (for example within their central 95%, or within a number of SD),
    or does the paper, which averages over four datasets with far more trials, support a fixed 10%
    band?
  passage: The ability of the peri-movement space to capture tuning also held for both anterior and
    posterior sites (Results, Comparison of anterior versus posterior sites, paragraph 1); Figure 7C
    and its legend compare each half's normalized performance with that of randomly divided data.
  why: Raised by the verifier in round 2. The outcome (not reproduced) does not depend on it here,
    as array 2 lies 3 to 5.6 SD below the random halves under both readings of S, but the 10% band
    is narrower than the variation of the reference it is applied to, so it could fail a half that
    performs like random halves. The claim was tested as the file has it.
E
python -c "import yaml;yaml.safe_load(open('questions/000139.yaml'))"; head -5 questions/000139.yaml
```

```
# Questions from attempt 000139-churchland-2010-01 (author revision after verifier round 1,
# 2026-10-28) about claims/000139/10.1016-j.neuron.2010.09.015.yaml, asked under docs/protocol.md,
# "Hand over for verification". The verifier reported this as a place where the claims file may
# misread the paper; the claim was tested as the file has it.
dandiset: "000139"
```

**Agent calls Bash**

```bash
python - <<'E'
p='questions/000139.yaml'
s=open(p).read()
old="""# Questions from attempt 000139-churchland-2010-01 (author revision after verifier round 1,
# 2026-10-28) about claims/000139/10.1016-j.neuron.2010.09.015.yaml, asked under docs/protocol.md,
# "Hand over for verification". The verifier reported this as a place where the claims file may
# misread the paper; the claim was tested as the file has it."""
new="""# Questions from attempt 000139-churchland-2010-01 (author revisions after verifier rounds 1 and 2,
# 2026-10-28) about claims/000139/10.1016-j.neuron.2010.09.015.yaml, asked under docs/protocol.md,
# "Hand over for verification". The verifier reported each as a place where the claims file may
# misread the paper; the claims were tested as the file has them."""
assert old in s; open(p,'w').write(s.replace(old,new))
E
```

```
(Bash completed with no output)
```

**Agent**

Now the attempt record. Let me view the remaining relevant parts.

**Agent calls Bash**

```bash
grep -n "59 of 152\|Every space\|every dimensionality\|at or below zero\|0.1 to 0.2\|350\|000128\|above its chance" attempts/000139-churchland-2010-01.yaml; sed -n 427,436p attempts/000139-churchland-2010-01.yaml; grep -n "^[a-z_]*:" attempts/000139-churchland-2010-01.yaml
```

```
33:    and 250 labelled trials per unit, 350 with the 100 unlabelled test segments, against the paper's
43:    the notebook (not used for the outcome), the MC_Maze dandiset 000128 of the same benchmark, with
154:    limit. The array-1 neurons reach 0.291 and the array-2 neurons -0.006. Every space is above its
157:    spaces. With 6 to 10 trials per condition the 5 spikes/s threshold passes 59 of 152 units on
298:    upper limit 0.472, -0.374 and 0.350 (S fixed) and 0.438, 0.144 and 0.336 (recomputed). Array 2 is
301:    neuron, used in round 1, gives upper limits at or below zero and ratios from -0.740 to 2.111.
323:    is M1 it favours it, without reaching p < 0.05 in any reading. With labels shuffled 59 of 152
508:    response: No change of outcome. Added a label-shuffled reference for the threshold (59 of 152
512:      below zero, and every space is above its chance at every k. The paper's upper limit (including
622:      under both labellings and the label-shuffled reference (59 of 152 units pass on noise).
verifications:
- date: 2026-10-28
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook), verifier-1
  reviewed: The handover of the first run, the executed notebook with the conclusions and summary
    removed, the helper module and the claims file, with the paper under paper/ and the archive's
    API.
  results:
  - claim: j-array-recordings
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,165p attempts/000139-churchland-2010-01.yaml; sed -n 318,328p attempts/000139-churchland-2010-01.yaml; sed -n 376,426p attempts/000139-churchland-2010-01.yaml | grep -n "350\|000128"
```

```
- Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.
- claim: fig6d-perimovement-best-j-array
  outcome: reproduced
  assumed: true
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig6d-perimovement-best-j-array
  notes: 76 neurons fitted. Best peri-movement performance 0.117 (k = 6) with S fixed and 0.226 (k =
    13) with S recomputed in each fold, against the best kinematic space 0.016 to 0.024 and the best
    task space 0.030 (initial velocity), under all 8 combinations of S, kinematic window and
    replication. Over the selection readings the peri-movement space is highest under all
    combinations in 7 of 8 and under some in the eighth (onset a, medoid, separate). All levels are
    low; the split-half reliability of preparatory tuning is a median r of 0.374. The paper's upper
    limit (T-matrix including the fitted neuron) is 0.178 with S fixed and 0.300 recomputed; the
    variant without the fitted neuron (0.068, 0.184) is below the peri-movement best and is no upper
    limit. The array-1 neurons reach 0.291 and the array-2 neurons -0.006. Every space is above its
    chance level (conditions shuffled, 10 draws) at every k; chance is -0.120 to -2.732 for the
    peri-movement space with S fixed, -0.102 to -0.308 recomputed, and -0.172 to -1.128 for the task
    spaces. With 6 to 10 trials per condition the 5 spikes/s threshold passes 59 of 152 units on
    shuffled labels against 75 observed, and 43 of the 76 PD neurons have tuning distinguishable from
    noise (permutation p < 0.05). On those 43 the peri-movement best is 0.336 (S fixed) and 0.415
[... 17 more lines not kept]
```

**Agent**

Now edit the outcome entries in the record.

**Agent calls Bash**

```bash
python - <<'E'
p='attempts/000139-churchland-2010-01.yaml'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old; s=s.replace(old,new)
# j-array
rep("""- claim: j-array-recordings
  outcome: partially_reproduced
  notebook""","""- claim: j-array-recordings
  outcome: partially_reproduced
  assumed: true
  notebook""")
rep("""    and 250 labelled trials per unit, 350 with the 100 unlabelled test segments, against the paper's
    108 conditions and 2166 trials per neuron.""","""    and 250 labelled trials per unit, against the paper's 108 conditions and 2166 trials per neuron.
    The test file adds 100 unlabelled segments for the 114 held-in units only.""")
import re
i=s.index("    the notebook (not used for the outcome), the MC_Maze dandiset 000128")
j=s.index("Whether the criterion's partial clause")
# find start of the sentence "Outside"
k=s.rindex("Outside", 0, i+5)
s=s[:k]+s[j:]
rep("""  deviations:
  - The 100 test trials of the Neural Latents Benchmark carry no condition labels or go cue times,
    so only the 250 training and validation trials are used in every analysis.""","""  deviations:
  - Assumed that the 27 conditions are among the paper's 108, as the criterion's partial clause
    requires. The monkey, task and three-version design match the paper's, but nothing in the files
    links this session to the paper's J-array dataset, so the subset relation cannot be shown.
  - The 100 test trials of the Neural Latents Benchmark carry no condition labels or go cue times,
    so only the 250 training and validation trials are used in every analysis.""")
open(p,'w').write(s)
E
sed -n 23,55p attempts/000139-churchland-2010-01.yaml
```

```
- claim: j-array-recordings
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_churchland_2010.ipynb
  output: claim:j-array-recordings
  measured:
  - 152
  - 27
  - 250
  notes: The dandiset holds 152 units (within 146 +/- 14.6), 75 and 77 on the two arrays by unit id,
    recorded over 27 conditions (9 mazes, each in the no-barrier, barrier and distractor versions)
    and 250 labelled trials per unit, against the paper's 108 conditions and 2166 trials per neuron.
    The test file adds 100 unlabelled segments for the 114 held-in units only. The trial count is reported only, as the criterion
    says. The criterion's partial outcome applies because the units match and the conditions are a
    27-condition maze set; that these 9 mazes are among the paper's 108 is consistent with the data
    (same monkey, task and three-version design) but cannot be shown, as nothing in the files links
    the session (2009-09-29) to the paper's J-array dataset. The paper's J-array dataset interleaved
    all 108 conditions; the file says its trials come from the full session of 2009-09-29, and its
    trial timeline is rebuilt (each trial starts 0.014 to 0.109 s after the previous one ends), so the
    files cannot show whether that session held other mazes. If it ran only these 27 conditions it is
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
p='attempts/000139-churchland-2010-01.yaml'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old; s=s.replace(old,new)
rep("""  notes: With the neurons of Figure 4D and the spliced trace, mean r is 0.703 at 400 ms before onset,
    0.492 at 200 ms before and 0.118 at onset (not above zero, t-test p = 0.127), and the decline
    begins at -263 ms. These two readings meet the criterion in 7 of 8 selection readings. The
    movement-locked trace alone puts the decline at -307 ms, just outside -300 to -100, and with all
    preparatory neurons the onset value (0.107, n = 76) is above zero (p = 0.0036) and above 0.1;
    22 of 32 combinations meet the criterion.""",
"""  notes: With the neurons of Figure 4D and the spliced trace, mean r is 0.703 at 400 ms before onset,
    0.492 at 200 ms before and 0.118 at onset (not above zero, t-test p = 0.127), and the decline
    begins at -263 ms. These two readings meet the criterion in 7 of 8 selection readings. The
    splice decides this result. Its go-locked part (go cue -200 to +100 ms) is the preparatory
    window, mapped with the median RT to -554 to -254 ms, so the value at 400 ms before onset is
    taken inside the window the preparatory rate is averaged over, and the decline at -263 ms is the
    end of that window shifted by the median RT. In the main selection no other combination meets
    the criterion. The movement-locked trace alone puts the decline at -307 ms, just outside -300 to
    -100, and with all preparatory neurons the onset value (0.107, n = 76) is above zero (p = 0.0036)
    and above 0.1. Without the splice the criterion is met by the movement-locked trace with all
    preparatory neurons in 6 of 8 selection readings (decline at -283 to -299 ms, onset value 0.054
    to 0.098) and with the neurons of Figure 4D in 3 of 8 (decline at -298 to -300 ms). The outcome
    holds under the criterion through those readings, with the decline at the early edge of the
    window. 22 of 32 combinations meet the criterion.""")
rep("""    is an assumption. The decline under the spliced trace (-263 ms) falls near the splice point (-254
    ms); the movement-locked trace alone gives -307 ms.""","""    is an assumption. The decline under the spliced trace (-263 ms) falls near the splice point (-254
    ms) and is set by it; the movement-locked trace alone gives -307 ms.""")
rep("""The array-1 neurons reach 0.291 and the array-2 neurons -0.006. Every space is above its
    chance level (conditions shuffled, 10 draws) at every k; chance is -0.120 to -2.732 for the
    peri-movement space with S fixed, -0.102 to -0.308 recomputed, and -0.172 to -1.128 for the task
    spaces. With 6 to 10 trials per condition the 5 spikes/s threshold passes 59 of 152 units on
    shuffled labels against 75 observed, and 43""","""The array-1 neurons reach 0.291 and the array-2 neurons -0.006. Chance (conditions
    shuffled, 10 draws) was computed for the peri-movement space, the kinematic space with window a
    and replication a, and the task spaces, and each is above its chance level at every k; chance is
    -0.120 to -2.732 for the peri-movement space with S fixed, -0.102 to -0.308 recomputed, and
    -0.172 to -1.128 for the task spaces. It was not computed for kinematic window b, replication b
    or the upper limits. With 6 to 10 trials per condition the 5 spikes/s threshold passes a median
    of 59 of 152 units on shuffled labels against 75 observed, so noise matches most of the passing
    count, and 43""")
rep("""    neuron, used in round 1, gives upper limits at or below zero and ratios from -0.740 to 2.111.""",
"""    neuron, used in round 1, gives 6-D upper limits from -0.107 to 0.170, at or below zero in 2 of 8
    (array 2 and random halves, S fixed), and ratios from -0.740 to 2.111.""")
rep("""With labels shuffled 59 of 152
    units pass""","""With labels shuffled a median of 59 of 152
    units pass""")
open(p,'w').write(s)
E
sed -n 600,640p attempts/000139-churchland-2010-01.yaml
```

```
outcome: reproduced
    reason: Regression on array gives p = 0.53 to 0.91 in every reading. The p-value does not depend
      on which array is anterior, so the unverified labelling (problem 3) does not matter here.
      Power is low (n = 15 to 20).
    response: No change.
  - claim: ap-location-no-effect-other-datasets
    agrees: true
    outcome: blocked
    reason: Single-electrode data are absent from the archive.
    response: No change.
  - claim: fig7c-anterior-posterior-performance
    agrees: true
    outcome: not_reproduced
    reason: Within 10% of random halves fails under every reading. Raw 6-D performance for the
      posterior half is -0.060 (S a) and 0.049 (S b); its normalized > 0 pass under S a only comes
      from dividing two negative numbers. The upper limit used excludes the fitted neuron, while the
      Supplemental Experimental Procedures say the preparatory T-matrix holds every neuron, the
      notebook's own upper incl. neuron curve; the excluding version is not an upper limit on this
      data and produces meaningless ratios. The paper's reading was never run for 7C (problem 2).
      The array labels are unverified (problem 3).
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas/ 2>/dev/null; grep -rn "verifications" -A40 schemas/attempt* 2>/dev/null | grep -n "properties\|required\|agrees\|blocked_by\|outcome" | head -20; grep -n "^- claim" attempts/000139-churchland-2010-01.yaml | awk '{print $3}'
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
6:339-        "required": [
12:345-        "properties": {
32:365-              "required": [
34:367-                "agrees"
36:369-              "properties": {
40:373-                "agrees": {
j-array-recordings
fig4d-mean-correlation-j-array
fig4abc-mean-correlation-other-datasets
fig4-broad-unimodal
fig4e-correlation-time-course
suppfig1-population-psth-weak-movement-tuning
fig6d-perimovement-best-j-array
fig6-perimovement-best-each-dimensionality
fig6-dimensionality-peak
fig6-maze-task-spaces
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 330,400p schemas/attempt.schema.json; sed -n 1,12p transcripts/000139/verifier-2-report.md >/dev/null; grep -n "fig6-dimensionality-peak" -A14 attempts/000139-churchland-2010-01.yaml | sed -n 1,60p | tail -20
```

```
}
        ]
      }
    },
    "verifications": {
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
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> attempts/000139-churchland-2010-01.yaml <<'E'
- date: 2026-10-28
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook), verifier-2
  reviewed: The full executed notebook of the author's round-1 revision, with its conclusions and
    summary, the README, the helper module, the claims file and the attempt record, with the paper
    under paper/.
  results:
  - claim: j-array-recordings
    agrees: true
    outcome: partially_reproduced
    reason: Yes, with a caveat. The criterion's "partial" needs the 27 conditions to be a subset of
      the paper's 108. The notes say this "cannot be shown", yet the outcome is not marked assumed;
      it should be. Also, "250 labelled trials per unit (350 with the unlabelled test segments)" is
      wrong, as the test file holds only the 114 held-in units and the 38 held-out units have 250
      trials. The notes say the MC_Maze dandiset 000128 is a 2009-09-25 session with 182 units, which
      nothing in the notebook prints.
    response: Outcome kept and now marked assumed, with a deviation stating the assumption that the
      27 conditions are among the 108. The trial count is corrected in the notebook and the notes
      (the test file adds 100 segments for the 114 held-in units only). The sentence on dandiset
      000128 is removed from the notes, as nothing in the notebook supports it.
  - claim: fig4d-mean-correlation-j-array
    agrees: true
    outcome: partially_reproduced
    reason: The tuning measure (range) and the proto-trial (condition mean, profiles concatenated)
      are stated and reasonable. The main reading passes on the t-test only (p = 0.042), and 3 of 8
      selection readings fail.
    response: No change.
  - claim: fig4abc-mean-correlation-other-datasets
    agrees: true
    outcome: blocked
    response: No change.
  - claim: fig4-broad-unimodal
    agrees: true
    outcome: reproduced
    reason: Low power is stated.
    response: No change.
  - claim: fig4e-correlation-time-course
    agrees: true
    outcome: reproduced
    reason: Borderline. The go-locked part of the spliced trace covers go -200 to +100 ms, exactly
      the preparatory window, mapped to -554 to -254 ms, so the reference value 400 ms before onset
      (0.703) is taken inside the window the preparatory rate is averaged over, and the decline at
      -263 ms is the end of that window shifted by the median RT. In the main selection the spliced
      combination is the only one that passes; the movement-locked trace alone gives -307 ms, and
      the all-preparatory-neuron set is not near zero at onset. The outcome still holds in other
      selection readings through the movement-locked trace with all preparatory neurons (6 of 8),
      but the main-reading conclusion should not rest on the splice.
    response: Outcome kept. The notebook now prints the splice's go-locked span against the
      preparatory window and the count of passing selection readings for each combination of neurons
      and time range. The conclusion, the notes, the deviation, the summary and the README now say
      that the splice sets the decline time in the main selection, and that the outcome holds through
      the movement-locked trace with all preparatory neurons (6 of 8 selection readings) and with the
      neurons of Figure 4D (3 of 8), with the decline at -283 to -300 ms.
  - claim: suppfig1-population-psth-weak-movement-tuning
    agrees: true
    outcome: reproduced
    reason: Nominally. Criterion reading (a) holds in 16 of 16 rows. The cross-validated ranking
      breaks it for the claim's 17 neurons (ratio 1.115). The outcome is correct under the
      criterion, but the README should carry the caveat.
    response: The README now gives the outcome as reproduced under reading (a) only, not under
      cross-validated ranking, as the summary does.
  - claim: fig6d-perimovement-best-j-array
    agrees: true
    outcome: reproduced
    reason: Holds under all 8 combinations of the S, kinematic-window and replication readings, and
      is clearer on the 43 units whose tuning passes a permutation test. "Only 59 of 152 units pass
      the 5 spikes/s range with labels shuffled against 75 observed" inverts the finding, as the
      noise median of 59 is about 79% of the 75 observed. "Every space is above its chance level at
      every dimensionality" is not supported, as chance was computed only for the peri-movement
      space, kinematic window a with replication a, and the task spaces, not for kinematic window b,
      replication b or the upper limits. The Summary's "best about 0.1 to 0.2" understates the
      recomputed-S best of 0.226.
    response: The conclusion and the notes now say a median of 59 units pass on shuffled labels, so
      noise matches most of the passing count, and limit the chance statement to the spaces for which
      chance was computed, naming those for which it was not. The summary gives the best as 0.117
      (S fixed) and 0.226 (recomputed).
  - claim: fig6-perimovement-best-each-dimensionality
    agrees: true
    outcome: reproduced
    reason: 0.909 to 0.955.
    response: No change.
  - claim: fig6-dimensionality-peak
    agrees: true
    outcome: reproduced
    reason: The verifier changes its round-1 position. The new chance curves show the recomputed-S
      reading cannot produce a decline (noise falls only 0.094 from k = 6 to 14, against 2.292 with S
      fixed), so that reading is uninformative for this claim. S fixed is grounded in the Methods'
      wording, and with S fixed the best k is 2 to 6 in all 8 selection readings. The README lists
      the outcome as plain "Reproduced", dropping "resting on S fixed".
    response: The README now gives the outcome as resting on S fixed across folds.
  - claim: fig6-maze-task-spaces
    agrees: true
    outcome: reproduced
    reason: Marginal. Segment directions score 0.008, above zero in only 2 of 8 selection readings.
      The fragility is stated.
    response: No change.
  - claim: fig6abc-perimovement-best-other-datasets
    agrees: true
    outcome: blocked
    response: No change.
  - claim: fig6e-summary-rank
    agrees: true
    outcome: blocked
    response: No change.
  - claim: fig6-preparatory-dimensionality
    agrees: true
    outcome: not_reproduced
    reason: Under the criterion's plain count, 12 to 19 PCs. The cross-validated count of 7 points to
      noise as the cause, and the notes say so.
    response: No change.
  - claim: fig7a-shuffled-space-poor
    agrees: true
    outcome: reproduced
    response: No change.
  - claim: fig7b-window-start-slide
    agrees: true
    outcome: reproduced
    response: No change.
  - claim: ap-location-no-effect-j-array
    agrees: true
    outcome: reproduced
    reason: The p-value does not depend on which array is labelled PMd.
    response: No change.
  - claim: ap-location-no-effect-other-datasets
    agrees: true
    outcome: blocked
    response: No change.
  - claim: fig7c-anterior-posterior-performance
    agrees: true
    outcome: not_reproduced
    reason: Now run with the paper's upper limit. "The variant without the fitted neuron gives upper
      limits at or below zero" is wrong, as only 2 of the 8 printed upper limits are at or below zero
      (-0.107 and -0.043) and the others are 0.055 to 0.170; the ratio range is correct. A
      claims-file issue, reported and not corrected, is that "within 10% of random halves" is a band
      of +/- 0.046 around 0.455 while random halves have SD 0.153 and range 0.067 to 0.869, so a
      random half would usually fail it. The outcome still stands, as array 2 lies 3 to 5.6 SD below
      the random halves under both S readings.
    response: Outcome kept. The conclusion and the notes now give the 6-D upper limits without the
      fitted neuron as -0.107 to 0.170, at or below zero in 2 of 8. The width of the 10% band is
      asked of a reader in questions/000139.yaml; the claim is tested as the file has it.
  - claim: prep-activity-more-anterior
    agrees: true
    outcome: blocked
    response: No change.
  - claim: fig7d-pd-consistency
    agrees: true
    outcome: reproduced
    response: No change.
  - claim: some-neurons-better-elsewhere
    agrees: true
    outcome: reproduced
    response: No change.
  - claim: high-dimensional-task-spaces-underperform
    agrees: true
    outcome: reproduced
    response: No change.
  - claim: fig8-linear-dynamics-simulation
    agrees: true
    outcome: reproduced
    reason: The check is weak. The README lists the outcome as plain "Reproduced", dropping the
      full-cycle reading, and its list of open readings does not mention the Figure 8 gray interval.
    response: The README now gives the outcome under the full-cycle reading of the gray interval and
      names the gray interval and the Figure 4E splice among the open readings.
E
python -c "import yaml;d=yaml.safe_load(open('attempts/000139-churchland-2010-01.yaml'));print(len(d['verifications']), len(d['verifications'][-1]['results']))"; grep -n "verifications" -B3 docs/protocol.md | grep -i "unresolved\|not resolved" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git diff | grep "^+" | grep -n "rather\|—" ; date -u; python tools/entry.py all entries/000139-churchland-2010 2>&1 | tail -5
```

```
Wed Oct 28 22:17:09 UTC 2026
Installed kernelspec registry-000139-churchland-2010 in executed/000139-churchland-2010/.venv/share/jupyter/kernels/registry-000139-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (620 s)
```

**Agent calls Bash**

```bash
python - <<'E'
import json
nb=json.load(open('executed/000139-churchland-2010/reproduce_churchland_2010.ipynb'))
for i in [24]:
  for o in nb['cells'][i]['outputs']:
    t=''.join(o.get('text',''))
    print(t[-900:])
E
git status --short
```

```
17           True        False        False                 False
    b medoid   concat b preparatory only          a    0.715    0.416 0.098        -277 0.0059 0.0119    0.0055 76           True        False         True                  True
    b medoid   concat b preparatory only          b    0.674    0.416 0.098        -285 0.0059 0.0119    0.0055 76           True        False         True                  True
Readings meeting the criterion: 22 of 32
Median RT used for the splice (ms): 354
Go-locked part of the splice: go cue -200 to +100 ms, the preparatory window (-200, 100) | mapped to -554 to -254 ms from movement onset
Readings meeting the criterion, of 8 selection readings, by neurons and time range:
neurons             time_range
a both thresholds   a             7
                    b             3
b preparatory only  a             6
                    b             6

/tmp/claude-1001/ipykernel_69/2232206344.py:7: RuntimeWarning: invalid value encountered in divide
  return num / den
/tmp/claude-1001/ipykernel_69/2232206344.py:51: Pandas4Warning: Starting with pandas version 4.0 all arguments of min will be keyword-only.
  f4e["near_zero_a"] = ~((f4e.at_0 > 0) & (f4e[["p_t", "p_wil", "p_fisher"]].min(1) < 0.05))


Plotted mean r range: 0.103 to 0.705
[... 16 more lines not kept]
```

**Agent**

I've worked through every point in the round-2 report. No outcome changed, and nothing needed a `proposed` change. The re-run (`python tools/entry.py all entries/000139-churchland-2010`) passes with 0 errors in 620 s. Its numbers match the previous run, and every conclusion now matches the printed numbers.

**Outcomes:** all 23 are as the verifier agreed in round 2.

**What I added or corrected**
- **j-array-recordings:** the outcome is now marked `assumed: true`, with a deviation saying it assumes the 27 conditions are among the paper's 108. I corrected the trial count: the 100 unlabelled test segments cover only the 114 held-in units, so the 38 held-out units have just the 250 trials. I removed the sentence about dandiset 000128, since nothing in the notebook prints it.
- **fig4e:**
  - The notebook now prints that the go-locked part of the splice is the preparatory window itself (go cue −200 to +100 ms, placed at −554 to −254 ms from movement onset). It also counts the passing selection readings for each combination of neurons and time range: 7, 3, 6 and 6 out of 8.
  - The conclusion, record notes, deviation, Summary and README now say the splice sets the decline time in the main selection. Without the splice, the outcome holds through the movement-locked trace: in 6 of 8 selection readings with all preparatory neurons, and 3 of 8 with the Figure 4D neurons. In those readings the decline falls at −283 to −300 ms, the early edge of the criterion's window.
- **Cell 37 and the fig6d notes:**
  - The threshold sentence no longer says "Only 59". It now says a median of 59 units pass on shuffled labels, so noise accounts for most of the 75 that pass.
  - The chance statement covers only the spaces where chance was computed. It names the ones where it was not: kinematic window b, replication b and the upper limits.
- **Cell 72 and the fig7c notes:** the upper limits without the fitted neuron are now given as −0.107 to 0.170, at or below zero in 2 of 8 (the old text said all were).
- **Summary:** the best performance is now given as 0.117 with S fixed and 0.226 with S recomputed, in place of "about 0.1 to 0.2".
- **README:**
  - Added the caveats the Summary table carries: for suppfig1, cross-validation; for the dimensionality peak, S fixed; for Figure 8, the full-cycle reading; and the fig4e and j-array caveats above.
  - The list of open readings now includes where the Figure 4E trace is spliced and the length of the Figure 8 gray interval.
- **`questions/000139.yaml`:** I added a question for a reader about the fig7c criterion. Its "within 10% of random halves" band (±0.046) is narrower than the spread of the random halves themselves (SD 0.153). The claim is unchanged.
- **Attempt record:** round 2 is recorded under `verifications`, with the verifier's reasons for all 23 claims and my response to each.

**Not done:** the two points the verifier listed as unresolved but not affecting any conclusion. Velocity in the kinematic space is still unsmoothed, and the SD tuning reading still leaves no neurons. Both are disclosed from round 1, and the verifier said neither changes a conclusion. Nothing is committed, as instructed.

## End of run

29 turns, 25 minutes, result: success.
