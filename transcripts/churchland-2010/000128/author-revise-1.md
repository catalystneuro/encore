# 000128 · author-revise-1 · run 39820139939

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat transcripts/000128/verifier-1-report.md; ls entries/000128-churchland-2010 entries/000128-churchland-2010/*; grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i "step 6\|Hand over"
```

```
**Verifier report: Churchland et al. 2010 on DANDI:000128 (round 1)**

**A. Outcomes**

The claims file has 22 claims. My outcomes: 11 reproduced, 1 partially reproduced, 3 not reproduced, 7 blocked.

| claim id | outcome | reason |
|---|---|---|
| recordings-jarray | partially_reproduced | Conditions are 108 (exact), and trials are 2295 under reading (a), within 2166 ± 216.6 (cell 12). The unit count is 182, outside 146 ± 14.6. The 137 "held-in" units that fall within tolerance are a Neural Latents Benchmark split, not a reading the claims file names, so the three counts do not all match under one reading. |
| recordings-single-electrode | blocked: data_missing | The archive holds one subject (Jenkins), two files and one array session; there are no single-electrode data for A, B or J. |
| fig2b-example-concordant-tuning | blocked: data_missing | Speed task (monkeys A and B) is not in the archive. |
| fig2ce-example-opposing-tuning | blocked: data_missing | Speed task is not in the archive. |
| fig3-maze-most-not-maintained | reproduced | Of 17 neurons, 1 has r ≥ 0.72 (0.765) and 94% have r < 0.72 (cell 17). This rests on a single neuron. |
| fig4d-mean-correlation-jarray | not_reproduced | Mean r = 0.051 and mean Spearman = 0.072, against 0.13 ± 0.013 and 0.11 ± 0.011. p = 0.42 to 0.61 under P1, P2 and P3 (cell 14, n = 17), so even the "partially reproduced" rule (positive mean with p < 0.05) fails. |
| fig4abc-mean-correlation-single-electrode | blocked: data_missing | No data from monkeys A, B or J (single electrode). |
| fig4-no-separate-populations | reproduced | Dip test p = 0.683 (U1 holds); 16 of 17 neurons have \|r\| < 0.5 (U2 holds); no neuron has \|r\| ≥ 0.8 (cell 19). |
| fig4e-correlation-time-course | reproduced | Under both A1 and A2, r falls from about 0.74 (−400 ms) to 0.61 (−200 ms) to 0.012 at onset. Smallest p at onset is 0.854, so (i) holds; 80 to 82% of the drop comes after −200 ms, so (ii) holds (cell 21). |
| suppfig1-population-averages | re
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,200p docs/protocol.md; sed -n 260,520p docs/protocol.md
```

```
### 5. Check

A second reader, in a separate run, checks the claims file against the paper:
that each statement says what the paper says, no more and no less; that each
quote is word for word (the quote checker, `tools/claims_check.py`, does this
mechanically); that each source points at the place; that the statistics are
the paper's and are results, not thresholds; that every part of every
criterion's method is taken from the paper or its code, as cited; and that the
paper's main findings each have a claim. The checker corrects what it can
show is wrong, and records each change, with its reason, under `checks` at
the end of the file. A claims file is ready for an attempt when its last check
says so.

### 6. Answer questions

When an attempt needs something the claims file does not give, the author asks
(author, step 6). A reader answers each question from the paper, in the claims
file, and marks it answered in `questions/<folder>.yaml`. An answer
the paper does not give is said to be that: the claim stays as it is, and the
author treats the detail as open (step 3, on details none of the sources fix).
[... 259 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/000128-churchland-2010/entry.yaml; ls attempts 2>/dev/null | grep 128; ls; ls attempts/*128* 2>/dev/null
```

```
schema_version: 1
name: 000128-churchland-2010
type: reproduction
title: Preparatory and peri-movement tuning in motor and premotor cortex (Churchland et al. 2010)
description: Tests the findings of Churchland, Cunningham, Kaufman, Ryu and Shenoy (2010) on dandiset
  000128 (MC_Maze), which holds the J-array session of monkey Jenkins on the maze task, recorded with two
  Utah arrays. It tests the correlation between preparatory and peri-movement tuning, its time course,
  the dimensionality of preparatory activity, the performance and stability of preferred directions in
  the peri-movement, kinematic and task spaces, and the paper's oscillator model. The speed task, the
  single-electrode recordings and EMG are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_churchland_2010.ipynb
  title: Reproducing Churchland et al. (2010) from dandiset 000128
  runtime_minutes: 2
helpers:
- mcmaze.py
related:
- id: dandi:000128/0.220113.0400
  relation: uses_data
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000128-churchland-2010-01.yaml; ls transcripts/000128 executed 2>/dev/null
```

```
Exit code 2
schema_version: 2
id: 000128-churchland-2010-01
dataset:
  archive: dandi
  id: "000128"
  version: 0.220113.0400
  doi: 10.48324/dandi.000128/0.220113.0400
paper: doi:10.1016/j.neuron.2010.09.015
date: 2026-10-22
entry: 000128-churchland-2010
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-10
  runner:
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "verifications\|^- claim\|^[a-z]" attempts/000128-churchland-2010-01.yaml; sed -n '/fig4e-correlation/,/fig7a/p' attempts/000128-churchland-2010-01.yaml
```

```
1:schema_version: 2
2:id: 000128-churchland-2010-01
3:dataset:
8:paper: doi:10.1016/j.neuron.2010.09.015
9:date: 2026-10-22
10:entry: 000128-churchland-2010
11:provenance:
22:outcomes:
23:- claim: recordings-jarray
41:- claim: recordings-single-electrode
47:- claim: fig2b-example-concordant-tuning
51:- claim: fig2ce-example-opposing-tuning
55:- claim: fig3-maze-most-not-maintained
63:- claim: fig4d-mean-correlation-jarray
79:- claim: fig4abc-mean-correlation-single-electrode
83:- claim: fig4-no-separate-populations
92:- claim: fig4e-correlation-time-course
106:- claim: suppfig1-population-averages
116:- claim: fig6-peri-movement-space-best
131:- claim: fig6-each-dimensionality
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims | grep 128; ls questions | grep 128; grep -l "verifications:" attempts/*.yaml | head -3; grep -n -A40 "verifications" schemas/*attempt* | head -120
```

```
000128
001285
000128.yaml
attempts/000003-senzai-2017-01.yaml
attempts/000004-chandravadia-2020-01.yaml
attempts/000005-yu-2016-01.yaml
303:    "verifications": {
304-      "type": "array",
305-      "items": {
306-        "type": "object",
307-        "additionalProperties": false,
308-        "required": [
309-          "date",
310-          "kind",
311-          "by",
312-          "results"
313-        ],
314-        "properties": {
315-          "date": {
316-            "type": "string",
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 343,400p schemas/*attempt*; grep -n -B2 -A30 "^verifications" attempts/000005-yu-2016-01.yaml | head -60; cat questions/000128.yaml | head -80; ls claims/000128
```

```
"type": "boolean"
                },
                "reason": {
                  "description": "The verifier's reason, in its own words.",
                  "type": "string"
                },
                "response": {
                  "description": "What the author changed or replied, kept apart from the verifier's reason.",
                  "type": "string"
                },
                "outcome": {
                  "description": "The outcome the verifier would give.",
                  "enum": [
                    "reproduced",
                    "partially_reproduced",
                    "not_reproduced",
                    "blocked"
                  ]
                }
              }
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,400p questions/000128.yaml; grep -n -A40 "id: prep-dimensionality" claims/000128/*.yaml; grep -n -A30 "id: recordings-jarray" claims/000128/*.yaml
```

```
and plotted times and (b) over the four plotted conditions, and both are run. The claim and
    its rule are unchanged.
  answered: 2026-10-22
396:- id: prep-dimensionality
397-  statement: Preparatory activity is moderately high-dimensional; depending on the dataset, 7 to 10
398-    dimensions capture 90% of its variance across conditions.
399-  source: Supplemental Experimental Procedures, Estimating the upper limit of PD performance; Results,
400-    PD performance in a variety of spaces, paragraph 2
401-  quote: This T-matrix also allows us to estimate the dimensionality of preparatory activity
402-    ... depending on the dataset, 7-10 dimensions were required to capture 90% of the data variance.
403-  expected:
404-    quantity: number of principal components for 90% of variance of the c x n preparatory matrix
405-    value: 8.65
406-    tolerance: 2.35
407-  criterion: The c x n matrix of M4 preparatory rates (one row per condition, one column per neuron,
408-    not normalised, columns mean-centred), PCA, the smallest number of components whose cumulative
409-    variance reaches 90%. The range 7 to 10 widened by 10% of each bound gives 6.3 to 11, so 7 to 11
410-    components. Which neurons enter is open; readings (N1) neurons passing the preparatory part of
411-    M6 (S1; S2 set aside, see the M6 answer); (N2) all neurons. Reproduced when the count is within the range under one reading.
412-- id: fig6e-summary-across-datasets
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print(i,c['cell_type'],c['metadata'].get('tags'),len(s.splitlines()),repr(s[:150]))
"; wc -l mcmaze.py; ls ../../executed/ 2>/dev/null | head
```

```
0 markdown None 51 '# Reproducing Churchland et al. (2010) from dandiset 000128\n\n**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical p'
1 code None 17 'import os\nos.environ.setdefault("OMP_NUM_THREADS", "1")\nos.environ.setdefault("OPENBLAS_NUM_THREADS", "1")\nimport time\nimport numpy as np\nimport panda'
2 markdown None 1 '## Data check'
3 code None 20 'meta = mm.version_metadata()\npub = {a["path"]: (a["blob"], a["size"]) for a in mm.list_assets(mm.VERSION)}\ndraft = {a["path"]: (a["blob"], a["size"]) '
4 code ['sanity'] 65 '# what was loaded: counts and ranges of every variable used\nprint("=== trials (train file) ===")\nprint("trials:", len(tr), "| split:", tr.split.value_'
5 markdown None 4 'The test file holds 574 more trials of the same session, as 0.7 s segments around movement onset\nwithout condition labels or behaviour, and only the 1'
6 code None 15 '# duplicates: spike counts of the held-in units in the test segments against the same window of every train trial\nheld_ids = units.unit_id[~units.held'
7 markdown None 6 '### Clocks\n\nHand speed is checked against the movement onset of the trial table, and the spikes against the trial\nevents by decoding the reach directi'
8 code None 29 'p_w, v_w, err = mm.kinematic_windows(sess, tr.move_onset_time.values, 400, 600)\nprint("largest timestamp error of the kinematic windows (s): %.2e" % e'
9 markdown None 7 '### Trial selection and firing rates (M1, M2)\n\nTrials with delay > 400 ms (M1), then the proto-trial selection under reading T2 (the two velocity\ncomp'
10 code None 47 'cond = tr.condition.values\nC = cond.max() + 1\nbase = tr.delay.values > mm.MIN_DELAY_MS\nmv = tr.move_onset_time.values\ngo = tr.go_cue_time.values\nkp, k'
11 markdown None 8 '## recordings-jarray\n\n> The J-array dataset holds 146 single- and multi-unit isolations from two 96-electrode arrays,\n> recorded on the maze task with'
12 code ['claim:recordings-jarray'] 10 'rows = [("units (all)", le
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; python -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [1,3,4,5,6,10,11,12,13,15,31,32,33,41,42,55,56]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 1
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import diptest
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import StratifiedKFold, cross_val_score
import mcmaze as mm

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
T_START = time.time()
print("dandiset", mm.DANDISET_ID, "version", mm.VERSION)
===== 3
meta = mm.version_metadata()
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; sed -n 1,120p mcmaze.py; ls ../../.venv* 2>/dev/null | head -2; which python; cat requirements.in
```

```
"""Loading and measures for dandiset 000128 (MC_Maze, monkey Jenkins, maze task, two Utah arrays).

Used by the reproduction of Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68:387-400.
Where a parameter comes from is said next to it: "M1" to "M9" are the method headers of the claims
file claims/000128/10.1016-j.neuron.2010.09.015.yaml (which cite the paper), and "standard choice"
marks a detail that the claims file calls a standard choice or that cannot change a result.

The data are streamed from the archive with remfile and h5py and read with pynwb; nothing is
written to disk.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import requests
import remfile
import h5py
import pynwb
from scipy.ndimage import gaussian_filter1d
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; timeout 900 python -c "
import mcmaze as mm, numpy as np
nwb,io=mm.open_nwb(mm.TRAIN_PATH)
for k,g in nwb.electrode_groups.items(): print(k, repr(g.description), repr(g.location), g.device)
for k,d in nwb.devices.items(): print('dev',k,d.description)
print(nwb.units.colnames, nwb.units.description if hasattr(nwb.units,'description') else '')
for c in nwb.units.columns: print(c.name, getattr(c,'description',''))
el=nwb.electrodes.to_dataframe(); print(el.head()); print(el.columns.tolist()); print(el.iloc[95:100])
tr=nwb.trials
print(tr.id.data[:10], tr.id.data[-10:], len(tr.id.data))
ids=np.asarray(tr.id.data[:]); print('trial id gaps', np.unique(np.diff(ids),return_counts=True))
for c in tr.columns: print(c.name, getattr(c,'description',''))
t,io2=mm.open_nwb(mm.TEST_PATH)
tt=t.trials.to_dataframe(); print(tt.head()); print(tt.index[:10].tolist(), tt.index.max())
allid=np.sort(np.r_[ids, tt.index.values]); print('combined', allid.min(), allid.max(), len(allid), len(np.unique(allid)))
print(nwb.experiment_description, nwb.session_description, nwb.notes if hasattr(nwb,'notes') else '')
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import mcmaze as mm, numpy as np
  File "entries/000128-churchland-2010/mcmaze.py", line 14, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/entry.py | head -80; ls ~/.cache 2>/dev/null; ls -a | grep venv; ls executed 2>/dev/null
```

```
Exit code 2
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
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 probe && uv pip install -q -p probe/bin/python -r entries/000128-churchland-2010/requirements.lock.txt && echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; timeout 900 $TMPDIR/probe/bin/python -c "
import mcmaze as mm, numpy as np
nwb,io=mm.open_nwb(mm.TRAIN_PATH)
for k,g in nwb.electrode_groups.items(): print(k, repr(g.description), repr(g.location), g.device)
for k,d in nwb.devices.items(): print('dev',k,d.description)
for c in nwb.units.columns: print(c.name, repr(getattr(c,'description','')))
el=nwb.electrodes.to_dataframe(); print(el.columns.tolist()); print(el.iloc[[0,1,95,96,97,191]])
tr=nwb.trials
ids=np.asarray(tr.id.data[:]); print(len(ids), ids.min(), ids.max(), 'trial id gaps', np.unique(np.diff(ids),return_counts=True))
for c in tr.columns: print(c.name, repr(getattr(c,'description','')))
t,io2=mm.open_nwb(mm.TEST_PATH)
tt=t.trials.to_dataframe(); print(tt.head(3)); print(tt.index.min(), tt.index.max())
allid=np.sort(np.r_[ids, tt.index.values]); print('combined', allid.min(), allid.max(), len(allid), len(np.unique(allid)))
for c in t.trials.columns: print('test', c.name, repr(getattr(c,'description','')))
print(repr(nwb.session_description)); print(repr(nwb.experiment_description))
"
```

```
electrode_group_M1 'Electrodes in an implanted Utah array in M1' 'Primary motor cortex' electrode_array_M1 pynwb.device.Device at 0x134814310681968
Fields:
  description: 96-electrode Utah array in M1
  manufacturer: Blackrock Microsystems

electrode_group_PMd 'Electrodes in implanted Utah Array in PMd' 'Dorsal premotor cortex' electrode_array_PMd pynwb.device.Device at 0x134814310261264
Fields:
  description: 96-electrode Utah array in PMd
  manufacturer: Blackrock Microsystems

dev electrode_array_M1 96-electrode Utah array in M1
dev electrode_array_PMd 96-electrode Utah array in PMd
heldout 'Whether the unit is held out in the test data (True) or not (False) in the Neural Latents Benchmark'
spike_times_index "Index for VectorData 'spike_times'"
spike_times 'the spike times for each unit'
obs_intervals_index "Index for VectorData 'obs_intervals'"
obs_intervals 'the observation intervals for each unit'
electrodes_index "Index for VectorData 'electrodes'"
electrodes 'the electrodes that each spike unit came from'
['x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name']
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; grep -rl "T-matrix" paper | head; grep -rn -i "T-matrix\|7-10 dim\|at least 7" paper | head -30
```

```
<persisted-output>
Output too large (69.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/1107a995-d0a1-4fd1-bbe8-04b391ab3640/tool-results/b9h7zzied.txt

Preview (first 2KB):
10.1016-j.neuron.2010.09.015.supp.pdf
10.1016-j.neuron.2010.09.015.txt
10.1038-nature11129.txt
paper/10.1016-j.neuron.2010.09.015.txt
paper/10.1016-j.neuron.2010.09.015.txt:7:Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC2991102 PMC2991102.1 2991102 2991102 NIHMS240235 21040842 10.1016/j.neuron.2010.09.015 NIHMS240235 NIHPA240235 1 Article Cortical preparatory activity: representation of movement or first cog in a dynamical machine? Churchland MM 1 Cunningham JP 1 3 Kaufman MT 2 Ryu SI 1 4 Shenoy KV 1 2 5 1 Dept. of Electrical Engineering, Stanford University, Stanford CA, 94305, USA 2 Neurosciences Program, Stanford University, Stanford CA, 94305, USA 3 Dept. of Engineering, University of Cambridge, Cambridge, UK 4 Dept. of Neurosurgery, Palo Alto Medical Foundation, Palo Alto CA, 94301, USA 5 Dept. of Bioengineering, Stanford University, Stanford CA, 94705, USA 4 11 2010 68 3 191982 387 400 06 10 2010 04 11 2011 04 11 2011 06 10 2011 14 10 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Summary The motor cortices are active during both movement and movement preparation. A common assumption is that preparatory activity constitutes a sub-threshold form of movement activity: a neuron active during rightwards movements becomes modestly active during preparation of a rightwards movement. We asked whether this pattern of activity is in fact observed. We found that it was not: at the level of a single neuron, preparatory tuning was weakly correlated with movement-period tuning. Yet somewhat paradoxically, preparatory tuning could be captured by a preferred directi
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o ".\{300\}7-10 dimensions.\{300\}" paper/10.1016-j.neuron.2010.09.015.txt; $TMPDIR/probe/bin/python -c "print()" ; (pdftotext paper/10.1016-j.neuron.2010.09.015.supp.pdf - 2>&1 | grep -n -i -B3 -A12 "upper limit" | head -60)
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -A12 "^  M5\|id: M5\|M5:" claims/000128/*.yaml | head -40; grep -n "^  M[0-9]\|- id: M" claims/000128/*.yaml | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  grep -n "M5\|M4" claims/000128/*.yaml | head -20
```

```
44:#    at r > 0.9, window movement onset -150 to +800 ms (the maze peri-movement window, M5);
63:# M4 Epochs. Preparatory rate, mean from 200 ms before the go cue to 100 ms after. Peri-movement
67:# M5 Peri-movement T-matrix. Condition-mean rates from 150 ms before movement onset to 800 ms after
190:  criterion: Speed task only, neurons passing M6, tuning correlation as in M4. The paper does not
202:    correlation as in M4. The paper sets no threshold for "similar tuning"; the one value it calls
229:    rates of M4, trials by M1 (reading T2; T1 set aside, see the M1 answer). The paper does not name the test of the mean against zero. Readings (P1) one-sample
274:    task peri-movement window as in M4, and for monkey J the four 27-condition sets analysed as
307:  criterion: Neurons as in fig4d. Per neuron, the M4 preparatory rates correlated over conditions with
353:    performance by M7 in (a) the peri-movement space (M5) for each k (M8, K1 and K2); (b) the
407:  criterion: The c x n matrix of M4 preparatory rates (one row per condition, one column per neuron,
```

**Agent calls Bash**

```bash
cd  sed -n 60,75p claims/000128/*.yaml
```

```
# M3 Movement onset. The paper does not say how it was detected. The movement onset marked in the
#    dataset is used; if the dataset marks none, this step is open and the claims that need it are
#    blocked as methods_underspecified unless the author asks a reader.
# M4 Epochs. Preparatory rate, mean from 200 ms before the go cue to 100 ms after. Peri-movement
#    rate for the tuning correlation, mean from 100 ms before to 350 ms after movement onset
#    (Methods, Correlations between preparatory and peri-movement tuning). The preparatory epoch of
#    the PD analyses is the same window (the Methods define one preparatory epoch).
# M5 Peri-movement T-matrix. Condition-mean rates from 150 ms before movement onset to 800 ms after
#    (maze) or 400 ms after (speed task), all neurons concatenated in each row (one row per
#    condition), without normalisation, leaving out the neuron whose preparatory tuning is being
#    fit; PCA over conditions (columns mean-centred), the first k scores form the c x k matrix S
#    (Results, Testing preparatory tuning in PCA-based spaces; Methods, PCA-based spaces;
#    Supplemental Figure 2).
# M6 Neuron selection. Neurons with more than 5 spikes/s of preparatory tuning for J-array, at
#    least 10 spikes/s for the single-electrode datasets (Methods, Neural recordings and datasets). For the
#    tuning correlation, also peri-movement tuning at least 1.5 times the preparatory tuning
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; python3 -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i in [0,9,17,20,23,29,30,35,39,45,51,54,64]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"; cat README.md
```

```
===== 0
# Reproducing Churchland et al. (2010) from dandiset 000128

**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
activity: representation of movement or first cog in a dynamical machine? *Neuron* 68:387-400,
doi:10.1016/j.neuron.2010.09.015.

**Dataset.** DANDI:000128 (MC_Maze, Neural Latents Benchmark), version `0.220113.0400`,
doi:10.48324/dandi.000128/0.220113.0400. The paper cites no version of the dataset (it predates it).
This is the only published version, so it is pinned. The draft (modified 2023-06-20) holds the same two
assets with the same blobs (checked below), so the choice changes nothing the analysis uses.

**Claims file.** `claims/000128/10.1016-j.neuron.2010.09.015.yaml`, written from the accepted author
manuscript in PubMed Central (PMC2991102) with its supplement, and checked by a second reader. The
claims file fixes every method; the labels M1 to M9, T2, S1 and so on are its readings.

**Answers taken up.** A reader answered three questions of this attempt on 2026-10-22
(`questions/000128.yaml`), and the claims file was updated. The proto-trial selection (M1) is now reading
T2 alone: T1, which kept 73.8% of trials and emptied two conditions, is set aside. The tuning measure (M6)
is now reading S1 (the range over conditions) alone: S2, the SD over conditions, is set aside. For
[... 248 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; cat > $TMPDIR/edit.py <<'EOF'
import json
p = "reproduce_churchland_2010.ipynb"
nb = json.load(open(p))
C = nb["cells"]
def src(i): return "".join(C[i]["source"])
def setsrc(i, s): C[i]["source"] = s.splitlines(keepends=True)
def rep(i, a, b):
    s = src(i); assert a in s, (i, a); setsrc(i, s.replace(a, b, 1))

# data check: electrode groups, trial ids, test file clock
rep(4, 'print("leading digit of unit id:"',
 'for k, g in nwb.electrode_groups.items():\n'
 '    print(f"electrode group {k}: {g.description!r}, location {g.location!r}, device {g.device.description!r}")\n'
 'print("electrodes table rows by group, first and last row:",\n'
 '      {gname: (int(np.where(el.group_name.values == gname)[0].min()), int(np.where(el.group_name.values == gname)[0].max()))\n'
 '       for gname in el.group_name.unique()})\n'
 'print("unit columns other than spikes and electrodes:", [c for c in nwb.units.colnames if c not in ("spike_times", "electrodes", "obs_intervals")],\n'
 '      "| none of them names an array")\n'
 'print("leading digit of unit id:"')
rep(4, 'print("test file has behaviour:", len(nwb_test.processing) > 0)',
 'print("test file has behaviour:", len(nwb_test.processing) > 0)\n'
 'tr_ids = np.asarray(nwb.trials.id.data[:])\n'
 'print("train trial ids: %d to %d, contiguous: %s" % (tr_ids.min(), tr_ids.max(), bool(np.all(np.diff(tr_ids) == 1))))\n'
 'print("test trial ids: %d to %d (they restart at 0); first test segment starts at %.1f s, segments are %.1f s apart:"\n'
 '      % (tt.index.min(), tt.index.max(), tt.start_time.iloc[0], np.median(np.diff(tt.start_time))),\n'
 '      "the test file has its own clock, not the session\'s")\n'
 'print("test file has a delay or success column:", any(c in tt.columns for c in ("delay", "success")))\n'
 'print("train success column description:", repr(nwb.trials["success"].description))')

# recordings-jarray table: only the claims file's readings get a verdict
setsrc(12, '''rows = [("units in the dataset", "count", len(units), 146, 14.6),
        ("units held in (benchmark split)", "not a reading", int((~units.heldout).sum()), 146, 14.6),
        ("conditions", "count", tr.condition.nunique(), 108, 0),
        ("trials, all successful trials of the session (train and test files)", "(a)", len(tr) + len(tt), 2166, 216.6),
        ("trials, successful trials with condition labels (train file)", "(a), train file only", len(tr), 2166, 216.6),
        ("trials, M1 with T2", "(b)", int(keep['T2'].sum()), 2166, 216.6),
        ("trials, delay > 400 ms only", "not a reading", int(base.sum()), 2166, 216.6)]
df = pd.DataFrame(rows, columns=["quantity", "reading", "dataset", "paper", "tolerance"])
df["within"] = (df.dataset - df.paper).abs() <= df.tolerance
print(df.to_string(index=False))
units_ok = bool(df.within[0])
print("\\nunits in the dataset within tolerance:", units_ok,
      "| so the three counts cannot all match under any reading of the trials")
''')
setsrc(13, '''**Result: partially reproduced.** The 108 conditions match. The dataset has 182 units, 36 more than 146 and
outside the tolerance of 14.6, so the three counts do not all match under any reading. Read as all successful
trials of the session, reading (a) gives 2869 trials (train and test files), outside the tolerance; counting the
train file alone, where trials carry condition labels, it gives 2295, within it. Under reading (b), M1 with T2,
the 1786 kept trials are outside it. The 137 held-in units and the 1967 trials with delay > 400 ms fall within
tolerance but are not readings the claims file names (the first is a Neural Latents Benchmark split), and they
decide nothing. The test file's trials have their own clock and no delay or success column, so whether they
belong to reading (a) cannot be settled from the file, and the train file's contiguous trial ids do not record
how many trials the benchmark packaging dropped.
''')

# fig4d per-neuron table
rep(15, 'print("\\nSD of r and range, per selection:")',
 'pt_all, qt_all = mm.tuning(D["T2"]["X"], "S1"), mm.tuning(D["T2"]["P"], "S1")\n'
 'v = R["T2", "S1"]\n'
 'per = pd.DataFrame({"unit id": units.unit_id.values[v["ids"]], "id digit": units.id_digit.values[v["ids"]],\n'
 '                    "prep tuning (spikes/s)": pt_all[v["ids"]].round(2), "peri tuning (spikes/s)": qt_all[v["ids"]].round(2),\n'
 '                    "r": v["r"].round(3), "Spearman": v["rs"].round(3)}).sort_values("r")\n'
 'print("\\nper neuron, T2 with S1 (selected neurons):")\n'
 'print(per.to_string(index=False))\n'
 'print("\\nSD of r and range, per selection:")')

# fig6-each: print lost comparisons
s = src(41)
s = s.replace('''                        comps = []
                        for base_name, variants in TASK_BASE.items():
                            n = variants[0] if len(variants) == 1 else next(v for v in variants if f"({V})" in v or f"({Gg})" in v)
                            d = mc["dims"][n]
                            comps.append(mc["peri"][d - 1] > mc["task"][n])
                        comps += list(mc["peri"][:K] > mc["kin"][W + Dd][:K])
''', '''                        comps, labels = [], []
                        for base_name, variants in TASK_BASE.items():
                            n = variants[0] if len(variants) == 1 else next(v for v in variants if f"({V})" in v or f"({Gg})" in v)
                            d = mc["dims"][n]
                            comps.append(mc["peri"][d - 1] > mc["task"][n])
                            labels.append(f"task {n} ({d}-D): peri {mc['peri'][d - 1]:.3f} vs {mc['task'][n]:.3f}")
                        comps += list(mc["peri"][:K] > mc["kin"][W + Dd][:K])
                        labels += [f"kinematic {W + Dd} k={k + 1}: peri {mc['peri'][k]:.3f} vs {mc['kin'][W + Dd][k]:.3f}" for k in range(K)]
                        for lab, c_ in zip(labels, comps):
                            if not c_:
                                lost.add((T, S, K, lab))
''')
s = s.replace("rows = []\n", "rows = []\nlost = set()\n", 1)
s += '''print("\\ncomparisons lost, in any combination of W, D, V and G:")
for item in sorted(lost):
    print("  ", *item)
kin_margin = {(T, S, k): min(mc["peri"][0] - v[0] for v in mc["kin"].values()) for (T, S), mc in MC.items() for k in [1]}
print("smallest margin of the peri-movement space over a kinematic space at k = 1:", {k: round(v, 4) for k, v in kin_margin.items()})
'''
setsrc(41, s)

# prep-dimensionality variants
s = src(32)
s += '''
# variants that decide nothing: the claims file fixes the c x n matrix of epoch means. The quoted supplement
# sentence says "This T-matrix", which may mean a conditions x (neurons x times) matrix (see questions/000128.yaml).
vrows = []
for T in D:
    G, M = D[T]["G"], D[T]["M"]
    for N, sel in (("N1 S1", SEL[T, "S1"]["prep"]), ("N2", np.ones(G.shape[0], bool))):
        for name, arr, tt_, w in (("prep T-matrix, -200 to +100 ms from go", G, tg, mm.PREP_WIN),
                                   ("peri T-matrix (M5), -150 to +800 ms from onset", M, tm, mm.TMAT_WIN)):
            ww = (tt_ >= w[0]) & (tt_ <= w[1])
            Tm = np.concatenate([arr[u][:, ww] for u in np.where(sel)[0]], axis=1)   # conditions x (neurons x times)
            Tc = Tm - Tm.mean(0)
            sv = np.linalg.svd(Tc, compute_uv=False) ** 2
            cum = np.cumsum(sv) / sv.sum()
            k90 = int(np.searchsorted(cum, 0.9) + 1)
            vrows.append((T, N, int(sel.sum()), name, Tm.shape[1], k90, 7 <= k90 <= 11, k90 >= 7))
print("\\nvariants (decide nothing):")
print(pd.DataFrame(vrows, columns=["trials", "neurons", "n", "matrix", "columns", "components for 90%", "within 7 to 11",
                                   "at least 7"]).to_string(index=False))
'''
setsrc(32, s)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False)
open(p, "a").write("\n")
EOF
python3 $TMPDIR/edit.py && git diff --stat
```

```
.../reproduce_churchland_2010.ipynb                | 91 ++++++++++++++++++----
 1 file changed, 74 insertions(+), 17 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; grep -n "def tuning" -A8 mcmaze.py; python3 - <<'EOF'
import json
p="reproduce_churchland_2010.ipynb"; nb=json.load(open(p)); C=nb["cells"]
s="".join(C[41]["source"])
a='''kin_margin = {(T, S, k): min(mc["peri"][0] - v[0] for v in mc["kin"].values()) for (T, S), mc in MC.items() for k in [1]}
print("smallest margin of the peri-movement space over a kinematic space at k = 1:", {k: round(v, 4) for k, v in kin_margin.items()})
'''
b='''for (T, S), mc in MC.items():
    print(f"{T} {S}: margin of the peri-movement space over each kinematic space at k = 1:",
          {k: round(mc["peri"][0] - v[0], 4) for k, v in mc["kin"].items()})
'''
assert a in s; C[41]["source"]=s.replace(a,b).splitlines(keepends=True)
json.dump(nb, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
git diff | head -5; git diff | tail -5
```

```
202:def tuning(x: np.ndarray, reading: str) -> np.ndarray:
203-    """M6 tuning of condition rates (units x conditions). S1 range, S2 SD over conditions.
204-
205-    The claims file's answer of 2026-10-22 keeps S1 alone; S2 is not used by the notebook.
206-    """
207-    if reading == "S1":
208-        return x.max(1) - x.min(1)
209-    if reading == "S2":
210-        return x.std(1)
diff --git a/entries/000128-churchland-2010/reproduce_churchland_2010.ipynb b/entries/000128-churchland-2010/reproduce_churchland_2010.ipynb
index 54152097..5241d6ff 100644
--- a/entries/000128-churchland-2010/reproduce_churchland_2010.ipynb
+++ b/entries/000128-churchland-2010/reproduce_churchland_2010.ipynb
@@ -161,6 +161,13 @@
+    "    print(f\"{T} {S}: margin of the peri-movement space over each kinematic space at k = 1:\",\n",
+    "          {k: round(mc[\"peri\"][0] - v[0], 4) for k, v in mc[\"kin\"].items()})\n"
    ]
   },
   {
```

**Agent**

Now running the entry to see the new numbers.

**Agent calls Bash**

```bash
cd  timeout 3000 python tools/entry.py all entries/000128-churchland-2010 2>&1 | tail -20
```

```
for (T, S), mc in MC.items():
    print(f"{T} {S}: endpoints + max speed {mc['task']['endpoints + max speed']:.3f}, peri-movement 3-D {mc['peri'][2]:.3f}")print("\ncomparisons lost, in any combination of W, D, V and G:")
for item in sorted(lost):
    print("  ", *item)
for (T, S), mc in MC.items():
    print(f"{T} {S}: margin of the peri-movement space over each kinematic space at k = 1:",
          {k: round(mc["peri"][0] - v[0], 4) for k, v in mc["kin"].items()})

------------------


  [36mCell[39m[36m [39m[32mIn[19][39m[32m, line 31[39m
[31m    [39m[31mprint(f"{T} {S}: endpoints + max speed {mc['task']['endpoints + max speed']:.3f}, peri-movement 3-D {mc['peri'][2]:.3f}")print("\ncomparisons lost, in any combination of W, D, V and G:")[39m
                                                                                                                             ^
[31mSyntaxError[39m[31m:[39m invalid syntax



0 error(s)
FAIL  reproduce_churchland_2010.ipynb  (89 s)
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; python3 - <<'EOF'
import json
p="reproduce_churchland_2010.ipynb"; nb=json.load(open(p)); C=nb["cells"]
for i in (4,15,32,41):
    s="".join(C[i]["source"]).replace(':.3f}")print(', ':.3f}")\nprint(').rstrip("\n")
    C[i]["source"]=s.splitlines(keepends=True)
json.dump(nb, open(p,"w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
cd ../..; timeout 3000 python tools/entry.py all entries/000128-churchland-2010 2>&1 | tail -5
```

```
Installed kernelspec registry-000128-churchland-2010 in executed/000128-churchland-2010/.venv/share/jupyter/kernels/registry-000128-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (120 s)
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'))
for i in [4,10,12,15,19,22,25,29,32,35,38,41,44,47,50,53,56,58,61]:
  c=nb['cells'][i]
  print('=====',i)
  for o in c.get('outputs',[]):
    if 'text' in o: print(''.join(o['text']))
    elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: print(''.join(o['data']['text/plain']))
"
```

```
===== 4
=== trials (train file) ===
trials: 2295 | split: {'train': 1721, 'val': 574} | success all True: True
trial_type values: 36 | maze_id values: 36 | trial_type <-> maze_id one to one: True
conditions (trial_type x trial_version): 108
trials per condition: min 17 median 22.0 max 27
targets      1           3
barriers False True  True 
version                   
0          789     0     0
1            0   750     0
2            0     0   756
delay (ms): min -3 max 999 | delay > 400 ms: 1967 | negative delay: 14
delay equals go - target onset (max |diff| ms): 0.0
rt (ms): min 218 max 1100 | rt equals move onset - go (max |diff| ms): 0.0
trial start to go cue (s): min 0.672; move onset to trial end (s): min 0.902
target positions (mm): x -130 to 133, y -86 to 86

=== units ===
units: 182 | held out: 45 | held in: 137
[... 218 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; cat > $TMPDIR/edit2.py <<'EOF'
import json
p = "reproduce_churchland_2010.ipynb"
nb = json.load(open(p)); C = nb["cells"]
def src(i): return "".join(C[i]["source"])
def setsrc(i, s): C[i]["source"] = s.rstrip("\n").splitlines(keepends=True)
def rep(i, a, b):
    s = src(i); assert a in s, (i, a); setsrc(i, s.replace(a, b, 1))
rep(41, 'round(mc["peri"][0] - v[0], 4)', 'round(float(mc["peri"][0] - v[0]), 4)')

setsrc(17, '''**Result: not reproduced.** Under T2 with S1 (17 neurons) the mean Pearson r is 0.051 and the mean Spearman
r 0.072, and no test finds the mean above zero (p 0.42 to 0.61). The means are positive but less than half
the paper's 0.13 and 0.11, outside the tolerances of 0.013 and 0.011. Only 17 of the 182 units pass the
selection (83 have preparatory tuning above 5 spikes/s, and 17 of these also have peri-movement tuning at least
1.5 times as strong), so the tests have little power; the per-neuron r runs from -0.355 to 0.765 (SD 0.283).''')
setsrc(20, '''**Result: reproduced.** Under T2 with S1, one of 17 neurons keeps its tuning (r = 0.765, unit 1581) and 94.1% have
r < 0.72, so at least one neuron has r of 0.72 or more and more than half have r below it. The first part rests
on that single neuron; the next largest r is 0.457.''')
setsrc(23, '''**Result: reproduced.** Under T2 with S1 the dip test finds no departure from unimodality (dip 0.071, p 0.683),
and 16 of 17 neurons have |r| < 0.5, so U1 and U2 both hold. No neuron has |r| ≥ 0.8; the median r is 0.013.
With 17 neurons the dip test has little power to find two populations, so U1 is weak evidence.''')
setsrc(30, src(30) + '''
The preparatory separation is positive by construction, since the conditions are ranked on the same
preparatory rates; the claims file asks for this ranking, and the test lies in the separation at onset.''')
setsrc(33, '''**Result: not reproduced.** No reading gives 7 to 11 components. With the 83 prep-tuned neurons (N1, S1), 90% of
the variance needs 15 components; with all 182 units (N2), 18. The main text says "at least 7-10 dimensions",
which 15 and 18 would meet, while the claim reads 7 to 10 as a range; and the quoted supplement sentence says
"This T-matrix", which may mean a conditions x (neurons x times) matrix where the claims file has the c x n
matrix of epoch means. Both are asked as a question (`questions/000128.yaml`), and the claim is decided as the
claims file states it. As variants that decide nothing, the conditions x (neurons x times) matrices need 55 to
61 components (preparatory window) and 56 to 60 (the M5 peri-movement window), further from 7 to 11.''')
setsrc(39, src(39) + ''' The best k is 14 under K1
and 12 under K2, the upper end of each range, so it is an edge value and not a peak.''')
setsrc(42, src(42) + ''' The one comparison lost in every combination
is the 2-D initial-velocity space (0.238 against 0.223 for the 2-D peri-movement space). At k = 1 the
peri-movement space beats the kinematic spaces by only 0.002 to 0.004.''')
setsrc(51, src(51) + ''' Both best k values (14 under K1, 12 under
K2) sit at the upper end of the range, so the ratio compares edge values.''')
setsrc(54, src(54) + ''' The kinematic comparisons are
taken at the best k, which is the upper end of the range (14 under K1, 12 under K2).''')
rep(55, "As a variant that decides nothing,",
 "The electrode groups are described as one array in M1 and one in PMd, but no unit column maps a unit to a\ngroup other than the electrode reference, and nothing maps the id digit to an array. As a variant that decides nothing,")

s = src(64)
s = s.replace("| recordings-jarray | partially reproduced: 108 conditions and 2295 trials match; 182 units against 146 |",
              "| recordings-jarray | partially reproduced: 108 conditions match; 182 units against 146; trials 2295 (train file) or 2869 (with the test file) under (a), 1786 under (b) |")
s = s.replace("| prep-dimensionality | not reproduced: 15 and 18 components, not 7 to 11 |",
              "| prep-dimensionality | not reproduced: 15 and 18 components, not 7 to 11 (a question on the claim's reading is open) |")
s = s.replace("All methods follow the claims file; the details it leaves open are run under every reading it names.",
              "All methods follow the claims file; the details it leaves open are run under every reading it names. The\n"
              "selection leaves 17 neurons for the correlation claims, so their tests have little power, and the best k\n"
              "of the PD analyses is at the upper end of the tested range.")
s = s.replace("574 trials sit in a test file as 0.7 s segments with no condition labels or\nbehaviour and only the 137 held-in units.",
              "574 trials sit in a test file as 0.7 s segments with no condition labels or\nbehaviour and only the 137 held-in units, on a clock of their own and with no delay or success column.")
setsrc(64, s)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
EOF
python3 $TMPDIR/edit2.py && python3 -c "
import json;nb=json.load(open('reproduce_churchland_2010.ipynb'))
print(''.join(nb['cells'][64]['source'])[-1600:])"
```

```
ndition; the paper says typically about 90%), and
reading T1 (74%, two conditions empty) was set aside. The paper does not define its tuning measure; the same
answers fixed reading S1, the range over conditions. Acceleration is the time derivative of the dataset's hand velocity. Movement onset is the
dataset's. All methods follow the claims file; the details it leaves open are run under every reading it names. The
selection leaves 17 neurons for the correlation claims, so their tests have little power, and the best k
of the PD analyses is at the upper end of the tested range.

What was found about the dataset. Every unit's electrode reference points into the PMd rows of the
electrodes table, so by the file all 182 units are in PMd, while the dataset describes two arrays; the unit
ids' leading digit (92 and 90 units) may be the array, undocumented. The electrodes have no coordinates, so no
anterior-posterior location. The dataset holds 182 units against the paper's 146, with no record of the
paper's unit or trial selection. 574 trials sit in a test file as 0.7 s segments with no condition labels or
behaviour and only the 137 held-in units, on a clock of their own and with no delay or success column. 14 trials have a negative delay (down to -3 ms). The behaviour
series' timestamps run on a 1 ms grid within trials with gaps between trials, and the spike times only cover
the trials; both share the trial table's clock as far as the checks show (hand speed rises at the marked
movement onset; reach direction is decoded from spikes after target onset, 0.661, and not before, 0.166).
```

**Agent calls Bash**

```bash
cd  cat >> questions/000128.yaml <<'EOF'
- claim: prep-dimensionality
  attempt: 000128-churchland-2010-01
  asked: 2026-10-22
  question: The claim's statement and its range of 7 to 11 read the paper's 7-10 as a two-sided range, but the
    main text says "at least 7-10 dimensions". Is the claim a range or a lower bound? And the quoted
    supplement sentence begins "This T-matrix"; does it mean the c x n matrix of preparatory epoch means
    that the criterion uses, or a conditions x (neurons x times) matrix of preparatory rates, or the
    peri-movement T-matrix of M5?
  passage: Results, PD performance in a variety of spaces, paragraph 2 ("because the dimensionality of
    preparatory activity itself is moderately high (at least 7-10 dimensions, methods)"); Supplemental
    Experimental Procedures, Estimating the upper limit of PD performance ("This T-matrix also allows us to
    estimate the dimensionality of preparatory activity").
  why: Raised by the round-1 verifier. On the c x n matrix the attempt finds 15 (N1) and 18 (N2) components,
    outside 7 to 11 but at least 7, so the outcome is not reproduced as a range and would be reproduced as a
    lower bound. On conditions x (neurons x times) matrices, run as variants that decide nothing, it finds
    55 to 61 components, which only a lower bound would accept.
EOF
tail -3 questions/000128.yaml; ls tools; grep -n "status\|answered" questions/000128.yaml | head
```

```
outside 7 to 11 but at least 7, so the outcome is not reproduced as a range and would be reproduced as a
    lower bound. On conditions x (neurons x times) matrices, run as variants that decide nothing, it finds
    55 to 61 components, which only a lower bound would accept.
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
papers_manifest.py
progress.py
readme_row.py
runner
site_assets
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p = "attempts/000128-churchland-2010-01.yaml"
s = open(p).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, a
    s = s.replace(a, b)
rep("""  notes: The dataset has 108 conditions (36 mazes in 3 versions) and 2295 successful trials with
    condition labels, within tolerance of 2166 under reading (a); every unit is observed on every
    trial. Under reading (b) M1 keeps 1786 trials with T2, outside the tolerance. The unit count is
    182 (137 held in, 45 held out), outside 146 plus or minus 14.6. A further 574 successful trials
    are in the test file as 0.7 s segments without labels (2869 in all, outside the tolerance). The
    answer of 2026-10-22 to the M1 question removed T1's count (1452) from reading (b); the outcome
    is unchanged.""",
"""  notes: The dataset has 108 conditions (36 mazes in 3 versions). The unit count is 182 (137 held in,
    45 held out), outside 146 plus or minus 14.6, so the three counts do not all match under any
    reading. Reading (a), all successful trials, gives 2869 with the 574 test-file segments, outside
    the tolerance, and 2295 counting the train file alone (the trials with condition labels), within
    it; every unit is observed on every train trial. The test file has its own clock and no delay or
    success column, so whether its trials belong to (a) cannot be settled from the file. Under
    reading (b) M1 keeps 1786 trials with T2, outside the tolerance. The 137 held-in units (a Neural
    Latents Benchmark split) and the 1967 trials with delay > 400 ms are printed but are not readings
    and decide nothing. The answer of 2026-10-22 to the M1 question removed T1's count (1452) from
    reading (b); the outcome is unchanged.""")
rep("""    0.72, so the claim holds. The answers""", """    0.72, so the claim holds. The first part rests on that one neuron (unit 1581); the next largest
    r is 0.457. The answers""")
rep("""    (P1 0.47, P2 0.42, P3 0.61). The means are positive but below half the paper's. The answers""",
"""    (P1 0.47, P2 0.42, P3 0.61). The means are positive but below half the paper's. Per-neuron r runs
    from -0.355 to 0.765 (SD 0.283); with 17 neurons the tests have little power. The answers""")
rep("""    17 neurons have |r| below 0.5, so U2 holds. No neuron has |r| of 0.8 or more; median r 0.013. The""",
"""    17 neurons have |r| below 0.5, so U2 holds. No neuron has |r| of 0.8 or more; median r 0.013.
    With 17 neurons the dip test has little power, so U1 is weak evidence. The""")
rep("""    (b). The answer of 2026-10-22 says the paper does not fix the maximum,""",
"""    (b). The preparatory separation is positive by construction, as the conditions are ranked on the
    same preparatory rates. The answer of 2026-10-22 says the paper does not fix the maximum,""")
rep("""    against 0.424 and 0.417 for the best kinematic space and 0.412 for the kitchen-sink space (G1).""",
"""    against 0.424 and 0.417 for the best kinematic space and 0.412 for the kitchen-sink space (G1).
    The best k is the upper end of each range, an edge value and not a peak.""")
rep("""    every combination of W, D, V and G, so L1 and L2 hold. The answers""",
"""    every combination of W, D, V and G, so L1 and L2 hold. The comparison lost is the 2-D
    initial-velocity space (0.238 against 0.223). At k = 1 the peri-movement space beats the kinematic
    spaces by 0.002 to 0.004 only. The answers""")
rep("""    Trial-averaged rates from at least 10 trials per condition (median 17) carry noise that adds dimensions; the
    paper's procedure may differ in this.""",
"""    Trial-averaged rates from at least 10 trials per condition (median 17) carry noise that adds
    dimensions; the paper's procedure may differ in this. The main text says "at least 7-10
    dimensions", which 15 and 18 would meet, and the supplement's "This T-matrix" may mean a
    conditions x (neurons x times) matrix; both are asked in questions/000128.yaml. As variants that
    decide nothing, such matrices need 55 to 61 components.""")
rep("""    cannot be tested. The answers of 2026-10-22 set aside T1 and S2 (0.904""",
"""    cannot be tested. Both best k values are the upper end of their range. The answers of 2026-10-22
    set aside T1 and S2 (0.904""")
rep("""    kinematic spaces at their best k). The answers""",
"""    kinematic spaces at their best k, which is the upper end of the range). The answers""")
rep("""    magnitude 0.432 (T2 with S1, 17 neurons, p 0.084), not significant.""",
"""    magnitude 0.432 (T2 with S1, 17 neurons, p 0.084), not significant. The electrode groups are
    described as one array in M1 and one in PMd, but no unit column other than the electrode
    reference maps a unit to a group.""")
open(p, "w").write(s)
EOF
grep -n "0.204\|0.197 to 0.319" attempts/000128-churchland-2010-01.yaml
```

```
234:    0.466 for segment directions G1 and G2, and 0.197 to 0.319 against 0.166 to 0.230 for the
```

**Agent**

Record notes updated. Now the `verifications` block and a small addition to the test-file finding.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p = "attempts/000128-churchland-2010-01.yaml"
s = open(p).read()
a = """    cannot enter a condition-mean analysis. None duplicates a train trial."""
assert a in s
s = s.replace(a, """    cannot enter a condition-mean analysis. None duplicates a train trial. The test file has a clock
    of its own (segment times restart at 0) and no delay or success column, and the train file's
    trial ids are contiguous, so the files do not record which session trials the packaging dropped.""")
s = s.rstrip("\n") + "\n" + """verifications:
- date: 2026-10-22
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The round-1 handover, the executed notebook with the conclusions and summary removed, the
    helper module and the claims file, with the paper under paper/.
  results:
  - claim: recordings-jarray
    agrees: true
    outcome: partially_reproduced
    reason: Conditions are 108 (exact), and trials are 2295 under reading (a), within 2166 plus or minus
      216.6. The unit count is 182, outside 146 plus or minus 14.6. The 137 held-in units that fall
      within tolerance are a Neural Latents Benchmark split, not a reading the claims file names, so the
      three counts do not all match under one reading. The table printed "within" for the held-in units
      and for the train-file trials, neither a reading in the claims file; reading (a), all successful
      trials, arguably includes the 574 test-file trials (2869, outside tolerance).
    response: The table now labels each row by reading. The held-in units and the delay > 400 ms count
      are marked as not readings, and reading (a) is shown both with the test file (2869) and for the
      train file alone (2295). The data check now prints that the test file has its own clock and no
      delay or success column and that the train trial ids are contiguous, so the dropped trials cannot
      be counted. The conclusion and notes were rewritten to match. Outcome unchanged.
  - claim: recordings-single-electrode
    agrees: true
    outcome: blocked
    reason: The archive holds one subject (Jenkins), two files and one array session; there are no
      single-electrode data for A, B or J.
    response: No change.
  - claim: fig2b-example-concordant-tuning
    agrees: true
    outcome: blocked
    reason: Speed task (monkeys A and B) is not in the archive.
    response: No change.
  - claim: fig2ce-example-opposing-tuning
    agrees: true
    outcome: blocked
    reason: Speed task is not in the archive.
    response: No change.
  - claim: fig3-maze-most-not-maintained
    agrees: true
    outcome: reproduced
    reason: Of 17 neurons, 1 has r of 0.72 or more (0.765) and 94% have r below 0.72. This rests on a
      single neuron; n = 17 gives the fig3 count little power.
    response: The fig4d cell now prints each selected neuron's id, id digit, preparatory and
      peri-movement tuning, r and Spearman r. The conclusion and notes say the first part rests on unit
      1581 and that the next largest r is 0.457. Outcome unchanged.
  - claim: fig4d-mean-correlation-jarray
    agrees: true
    outcome: not_reproduced
    reason: Mean r = 0.051 and mean Spearman = 0.072, against 0.13 plus or minus 0.013 and 0.11 plus or
      minus 0.011. p = 0.42 to 0.61 under P1, P2 and P3 (n = 17), so even the partially reproduced rule
      (positive mean with p < 0.05) fails. The selection leaves only 17 of 182 units; the code follows
      the claims file.
    response: The per-neuron table was added, and the conclusion and notes say that 17 neurons give the
      tests little power. Outcome unchanged.
  - claim: fig4abc-mean-correlation-single-electrode
    agrees: true
    outcome: blocked
    reason: No data from monkeys A, B or J (single electrode).
    response: No change.
  - claim: fig4-no-separate-populations
    agrees: true
    outcome: reproduced
    reason: Dip test p = 0.683 (U1 holds); 16 of 17 neurons have |r| below 0.5 (U2 holds); no neuron
      has |r| of 0.8 or more. n = 17 gives the dip test little power.
    response: The conclusion and notes now say the dip test has little power with 17 neurons. Outcome
      unchanged.
  - claim: fig4e-correlation-time-course
    agrees: true
    outcome: reproduced
    reason: Under both A1 and A2, r falls from about 0.74 (-400 ms) to 0.61 (-200 ms) to 0.012 at onset.
      Smallest p at onset is 0.854, so (i) holds; 80 to 82% of the drop comes after -200 ms, so (ii)
      holds.
    response: No change.
  - claim: suppfig1-population-averages
    agrees: true
    outcome: reproduced
    reason: Preparatory separation is positive (0.220 or 0.346). The ratio at onset is 0.240 (a) and
      0.274 (b), so R1 holds under both readings and R2 under (a). The preparatory separation is
      positive by construction, because conditions are ranked on the same preparatory rates; the claims
      file asks for this.
    response: The conclusion and notes now say the preparatory separation is positive by construction.
      Outcome unchanged.
  - claim: fig6-peri-movement-space-best
    agrees: true
    outcome: reproduced
    reason: Best peri-movement performance is 0.518 (K1) or 0.505 (K2). The best kinematic space reaches
      0.424 and the best task space 0.412. The peri-movement space wins 24 of 24 combinations under each
      K. J-array is the only dataset.
    response: The conclusion and notes now say the best k is the upper end of each range. Outcome
      unchanged.
  - claim: fig6-each-dimensionality
    agrees: true
    outcome: reproduced
    reason: Peri-movement wins 21 of 22 (K1) and 19 of 20 (K2) comparisons, so L1 and L2 both hold.
      Endpoints + max speed scores 0.168, below the 3-D peri-movement space at 0.271. The one lost
      comparison is not printed; it must be initial velocity (2-D, 0.238 against 0.223). Peri-movement
      beats kinematic at k = 1 by only 0.002 to 0.004.
    response: The cell now prints the lost comparisons, which are the 2-D initial-velocity space (0.238
      against 0.223) under K1 and K2, and the margins at k = 1 over each kinematic space (0.0024 to
      0.0041). The conclusion and notes say both. Outcome unchanged.
  - claim: fig6-performance-vs-dimensionality
    agrees: true
    outcome: not_reproduced
    reason: Performance rises almost monotonically to the edge of the range, with best k = 14 (0.518)
      and no decline after k = 10.
    response: No change.
  - claim: prep-dimensionality
    agrees: true
    outcome: not_reproduced
    reason: 15 components (N1) and 18 (N2) are needed for 90% of variance, outside 7 to 11. The main
      text says "at least 7-10 dimensions", while the claim treats 7 to 10 as a two-sided range, and 15
      would agree with "at least". The supplement's "This T-matrix" may mean a conditions x (neurons x
      times) matrix rather than the c x n epoch means the claims file uses. Reported as a possible
      misreading in the claims file, not corrected.
    response: Both points are asked as a question in questions/000128.yaml; the claim is decided as the
      claims file states it. The cell now also computes, as variants that decide nothing, 90%
      dimensionality on conditions x (neurons x times) matrices of the preparatory window and of the M5
      window, which need 55 to 61 components. The conclusion and notes say this. Outcome unchanged.
  - claim: fig6e-summary-across-datasets
    agrees: true
    outcome: blocked
    reason: Needs A, B, J and EMG; the archive's assets summary lists Units and ProcessingModule only,
      with no EMG.
    response: No change.
  - claim: fig7a-shuffled-space-poor
    agrees: true
    outcome: reproduced
    reason: Shuffled space is below the unshuffled one at every k (best 0.227 against 0.518) and below
      the worst kinematic variant (0.414 to 0.421), so H1 and H2 hold.
    response: No change.
  - claim: fig7b-window-start-slide
    agrees: true
    outcome: reproduced
    reason: J-array ratio is 0.959 (K1) or 0.957 (K2), within 0.97 plus or minus 0.097 under reading J2.
      The 0.94 value for monkeys A and B cannot be tested. The best k is an edge value, not a true peak.
    response: The conclusion and notes now say both best k values sit at the upper end of the range.
      Outcome unchanged.
  - claim: ap-location-no-effect-on-correlation
    agrees: true
    outcome: blocked
    reason: Asset and version metadata have no anatomical coordinates; x, y, z are all NaN and every
      unit points to PMd electrode rows. A two-level variant is possible only if the unit-id leading
      digit means the array; under that assumption p = 0.084, which would meet the criterion. The
      digit-to-array mapping is unverified, so the variant decides nothing.
    response: The data check now prints the electrode group descriptions (one array in M1, one in PMd),
      the rows of each group, and that no unit column other than the electrode reference names an
      array, so the digit stays unmapped. The per-neuron table gives each neuron's digit. Block
      unchanged.
  - claim: fig7c-anterior-posterior-performance
    agrees: true
    outcome: blocked
    reason: Same missing location data. A split by the id digit is not testable either, because the
      criterion needs to know which half is anterior.
    response: No change.
  - claim: fig7d-pd-consistency
    agrees: true
    outcome: reproduced
    reason: Peri-movement consistency is higher in 11 of 11 comparisons. J-array only. The best k in the
      kinematic comparisons is an edge value.
    response: The conclusion and notes now say the kinematic comparisons are taken at the upper end of
      the range. Outcome unchanged.
  - claim: fig8-model-weak-correlation
    agrees: true
    outcome: reproduced
    reason: 0.08 lies inside the central 95% (about -0.40 to 0.40) under all 8 readings. The criterion
      is weak; almost any small value would pass.
    response: No change; the criterion is the claims file's.
  - claim: fig8-model-pd-perfect
    agrees: true
    outcome: reproduced
    reason: Smallest R squared and smallest leave-one-out performance are both 1.0 under all readings.
    response: No change.
"""
open(p, "w").write(s)
EOF
grep -n '—\|rather' attempts/000128-churchland-2010-01.yaml questions/000128.yaml entries/000128-churchland-2010/reproduce_churchland_2010.ipynb | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i '390s/ matrix rather than the c x n/ matrix, not the c x n/' attempts/000128-churchland-2010-01.yaml; sed -n 388,392p attempts/000128-churchland-2010-01.yaml; grep -n ': [^ ]*: ' attempts/000128-churchland-2010-01.yaml | grep -v '^\s*-\? *[a-z_]*: ' | head; timeout 3000 python tools/entry.py all entries/000128-churchland-2010 2>&1 | tail -4
```

```
text says "at least 7-10 dimensions", while the claim treats 7 to 10 as a two-sided range, and 15
      would agree with "at least". The supplement's "This T-matrix" may mean a conditions x (neurons x
      times) matrix, not the c x n epoch means the claims file uses. Reported as a possible
      misreading in the claims file, not corrected.
    response: Both points are asked as a question in questions/000128.yaml; the claim is decided as the
Installed kernelspec registry-000128-churchland-2010 in executed/000128-churchland-2010/.venv/share/jupyter/kernels/registry-000128-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (121 s)
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;yaml.safe_load(open('questions/000128.yaml'));print('q ok')
import json;nb=json.load(open('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'))
for i in [12,32,41]:
  print(''.join(o.get('text','') for o in nb['cells'][i]['outputs'])[-700:])
"; git status --short
```

```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    print(''.join(o.get('text','') for o in nb['cells'][i]['outputs'])[-700:])
          ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: sequence item 0: expected str instance, list found
q ok
 M attempts/000128-churchland-2010-01.yaml
 M entries/000128-churchland-2010/reproduce_churchland_2010.ipynb
 M questions/000128.yaml
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
?? scripts
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'))
for i in [41]:
  print(''.join(''.join(o.get('text','')) for o in nb['cells'][i]['outputs'])[-500:])
"; git status --short --ignored scripts | head -3; git diff --stat
```

```
0  True    True    True    True    True
              14       21       21     22  True    True    True    True    True
T2 S1: endpoints + max speed 0.168, peri-movement 3-D 0.271

comparisons lost, in any combination of W, D, V and G:
   T2 S1 12 task initial velocity (2-D): peri 0.223 vs 0.238
   T2 S1 14 task initial velocity (2-D): peri 0.223 vs 0.238
T2 S1: margin of the peri-movement space over each kinematic space at k = 1: {'W1D1': 0.0041, 'W1D2': 0.0039, 'W2D1': 0.0032, 'W2D2': 0.0024}

?? scripts
 attempts/000128-churchland-2010-01.yaml            | 227 +++++++++++++++++++--
 .../reproduce_churchland_2010.ipynb                | 142 ++++++++++---
 questions/000128.yaml                              |  16 ++
 3 files changed, 335 insertions(+), 50 deletions(-)
```

**Agent**

No outcome changed. The verifier agreed with all 22 outcomes (11 reproduced, 1 partially reproduced, 3 not reproduced, 7 blocked). I re-ran the entry with `python tools/entry.py all entries/000128-churchland-2010`: it passed in 121 s and every earlier number came out the same. Round 1 is recorded under `verifications` in `attempts/000128-churchland-2010-01.yaml`, with the verifier's reason and my response for each claim. Nothing is committed.

**Corrected**
- **recordings-jarray table:** each row is now labelled with its reading. The 137 held-in units and the 1967 trials with delay over 400 ms are marked as not readings, since the first is a Neural Latents Benchmark split. Reading (a) now shows both 2869 trials (with the test file) and 2295 (train file alone). The conclusion and notes now say that the 182 units fail under every reading.
- **Conclusions and notes** now carry the verifier's caveats:
  - The correlation claims (fig4d, fig3, fig4-no-separate) rest on only 17 neurons, so their tests have little power, and fig3 rests on one neuron, unit 1581 (r = 0.765).
  - The preparatory separation in suppfig1 is positive by construction.
  - In the PD analyses (fig6-best, fig7b, fig7d) the best k sits at the top of the tested range, so it is not a true peak.

**Added outputs the verifier asked for**
- **fig4d:** a per-neuron table of unit id, id digit, preparatory and peri-movement tuning, r and Spearman r.
- **fig6-each-dimensionality:** the lost comparisons are printed. As the verifier inferred, it is the 2-D initial-velocity space, 0.238 against 0.223. The margins at k = 1 are 0.0024 to 0.0041.
- **Data check, test file:** it has its own clock, with ids and times restarting at 0, and no delay or success column. The train trial ids run without gaps, so the files do not record which trials the packaging dropped. I added this to the matching finding.
- **Data check, arrays:** the electrode-group descriptions name one array in M1 and one in PMd. No unit column other than the electrode reference ties a unit to an array, so the id digit still cannot be mapped and the two AP claims stay blocked.
- **prep-dimensionality:** variants on conditions × (neurons × times) matrices need 55 to 61 components. They do not decide the outcome.

**Not done, and why**
- **prep-dimensionality reading:** I did not change the claim. The main text says "at least 7-10 dimensions", while the claims file reads it as a range, and the supplement's "This T-matrix" is ambiguous. Both points are now a question in `questions/000128.yaml`. The claim stays not reproduced as the claims file states it; read as a lower bound, it would be met.
- **Which trials reading (a) covers:** I did not ask about this, because the outcome is partially reproduced however it is answered.
- **Supplement text:** I could not extract it here either, so the open T-matrix question rests only on the sentence quoted in the claims file.

## End of run

34 turns, 11 minutes, result: success.
