# 000959 · author-revise-1 · run 41260225916

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000959/verifier-1-report.md; ls entries/000959-fan-2024 entries/000959-fan-2024/*
```

```
Sun Nov  1 01:17:55 UTC 2026
# Verifier report, round 1: Fan et al. 2024 (DANDI:000959, version 0.261020.0242)

The claims file holds 36 claims. My outcomes: 23 reproduced, 4 partially reproduced, 2 not reproduced and 7 blocked.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| design-days-per-area | reproduced | Cell 7 gives 15/15/15 days for L Eyes, 12/12/12 for T Eyes and 5/5/5 for T Mouth. Every count matches. |
| design-sessions-per-day | partially_reproduced | Cell 9: monkey L has a mean of 6.02 control runs per day, against an expected 5 ± 0.5. Every other mean, range and the duration hold (L social 10.0, range 9–11; T social 14.0, range 14; T control 5; about 296 s). |
| fig1e-stim-counts-comparable | reproduced | Cell 12: the smallest FDR-corrected p is 0.908 for stimulations and 0.942 for shams, so all exceed 0.90. |
| figs1d-stim-counts-nonsocial | reproduced | Cell 13: no corrected p is below 0.05. Not all exceed 0.10, though: shams between monkeys give corrected p = 0.082 (OFC and dmPFC). |
| figs1e-eyes-more-than-face | reproduced | Cell 16: under both readings and both event sets, the corrected p ranges from 1.1e-7 to 4.4e-5, which is below 10⁻⁴. Eyes are higher in every case. |
| figs1e-eyes-vs-rdm-comparable | not_reproduced | Cell 17: under the deciding reading (a, the day's total), Eyes exceed RDM with corrected p of 0.0004, 0.00003 and 0.0004. Reading (b, the mean per run) gives p of 0.40–0.52 (see B1). |
| fig2a-density-map-ofc | reproduced | Cell 21: the OFC stimulation-minus-sham sum is positive in the Face and in the Eyes, under both normalisations (z-score 7.47 and 3.71; total 0.0093 and 0.0046). |
| fig2c-ofc-social-gaze-distance | reproduced | Cell 23, Methods reading: combined p = 0.00021, L p = 0.0067, T p = 0.016, all with negative medians. |
| fig2c-dmpfc-accg-no-distance-effect | reproduced | Cell 25: dmPFC p = 0.21, ACCg p = 0.39. |
| fig2e-ofc-contralateral | reproduced | Cell 28, Methods reading: contralateral p = 0.000
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
612 docs/protocol.md
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
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/000959-fan-2024/entry.yaml | head -150; wc -l entries/000959-fan-2024/*; ls claims* questions 2>/dev/null | head; ls
```

```
schema_version: 1
name: 000959-fan-2024
type: reproduction
title: Closed-loop OFC microstimulation and dynamic social attention (Fan et al. 2024)
description: Tests the findings of Fan, Dal Monte, Nair, Fagan and Chang (2024) on dandiset 000959,
  which holds the gaze, pupil, fixation events and stimulation times of every run of the 81 Eyes and
  15 Mouth stimulation days of two stimulated monkeys. It compares social gaze distance, its
  hemifield split, inter-looking interval, reciprocation latency, the partner's gaze, fixation counts
  and durations, pupil size and the trial counts between microstimulation and sham trials. The causal
  decomposition and the saccade analyses are not run.
license: Apache-2.0
notebooks:
- path: reproduce_fan_2024.ipynb
  title: Reproducing Fan et al. (2024) from dandiset 000959
  runtime_minutes: 12
helpers:
- microstim.py
related:
- id: dandi:000959/0.261020.0242
  relation: uses_data
[... 44 more lines not kept]
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

**Agent calls Bash**

```bash
ls attempts | grep 000959; ls questions | grep 000959; ls claims/000959*; cat questions/000959.yaml 2>/dev/null | head -50; ls transcripts/000959
```

```
000959-fan-2024-01.yaml
10.1016-j.neuron.2024.05.004.yaml
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
```

**Agent calls Bash**

```bash
cat attempts/000959-fan-2024-01.yaml; ls questions | head;
```

```
schema_version: 2
id: 000959-fan-2024-01
dataset:
  archive: dandi
  id: "000959"
  version: 0.261020.0242
  doi: 10.48324/dandi.000959/0.261020.0242
paper: doi:10.1016/j.neuron.2024.05.004
date: 2026-10-31
entry: 000959-fan-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
[... 413 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "verifications:" attempts/*.yaml | head -3; f=$(grep -l "verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -60
```

```
attempts/000003-senzai-2017-01.yaml
attempts/000004-chandravadia-2020-01.yaml
attempts/000005-yu-2016-01.yaml
verifications:
- date: '2026-10-16'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper. The verifier queried the archive metadata and tested
    helper functions on synthetic inputs. Its report had no attempt record and gave its own outcome for
    each claim; all 31 agree with the record.
  results:
  - claim: unit-counts
    agrees: true
    outcome: partially_reproduced
    reason: GC 609 is inside 527 to 645, but MC 568 is outside 450 to 550.
    response: No change needed.
  - claim: first-stage-labels
    agrees: true
    outcome: partially_reproduced
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python -c "
import json;nb=json.load(open('reproduce_fan_2024.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print(i,c['cell_type'],c.get('metadata',{}).get('tags',[]),len(s.splitlines()),'|',s.splitlines()[0][:100] if s else '')
"; ls ../../executed/000959-fan-2024 2>/dev/null
```

```
Exit code 2
0 markdown [] 40 | # Reproducing Fan et al. (2024) from dandiset 000959
1 code [] 46 | import time
2 markdown [] 1 | ## Data check
3 code ['sanity'] 83 | t_start = time.time()
4 markdown [] 4 | **Clock check.** Each trial was triggered online by an M1 fixation in the targeted ROI, so the
5 code [] 21 | def inside_rate(tr, ev, shift):
6 markdown [] 4 | ## design-days-per-area
7 code ['claim:design-days-per-area'] 5 | kept = trials[trials.kept]
8 markdown [] 1 | **Result: reproduced.** Every day holds kept stimulation and sham trials: 15 Eyes days per area for 
9 markdown [] 4 | ## design-sessions-per-day
10 code ['claim:design-sessions-per-day'] 10 | eyes_days = meta[meta.roi == "Eyes"]
11 markdown [] 1 | **Result: partially reproduced.** Monkey L has 10.0 social runs per day (9 to 11) and 6.02 control r
12 markdown [] 7 | ## fig1e-stim-counts-comparable and figs1d-stim-counts-nonsocial
13 code [] 20 | def count_tests(cond):
14 code ['claim:fig1e-stim-counts-comparable'] 8 | summ, t = count_tests("Social")
15 markdown [] 1 | **Result: reproduced.** Of the 24 rank-sum tests on the social runs, the smallest FDR-corrected p is
16 code ['claim:figs1d-stim-counts-nonsocial'] 7 | summ, t = count_tests("Dot")
17 markdown [] 1 | **Result: reproduced.** No corrected p is below 0.05 (smallest 0.108 for stimulations, 0.082 for sha
18 markdown [] 13 | ## figs1e-eyes-more-than-face and figs1e-eyes-vs-rdm-comparable
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000959; nproc; free -g | head -2; head -c 1500 transcripts/000959/answer-report.md; echo; head -c 1500 transcripts/000959/author-answers-report.md
```

```
10.1016-j.neuron.2024.05.004.yaml
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
There were no questions to answer, so I changed nothing.

- **No questions file:** `questions/000959.yaml` doesn't exist. It isn't on this branch, and no commit on any branch has ever contained it.
- **The author asked none:** The author report (`transcripts/000959/author-report.md:52`) says "Questions to a reader: none." The only author run so far (commit 04019a5fe) wrote no questions file.
- **Two questions in the attempt record are not for a reader:** `attempts/000959-fan-2024-01.yaml` (around lines 408 and 414) has two "Question for the paper's authors" entries, on the inter-looking interval and on M2's reciprocation latency. They are addressed to the paper's authors, not to a reader, and they don't say the claims file misreads the paper.

I didn't touch `claims/000959/`, didn't create a questions file, and didn't run `tools/claims_check.py`, since no quote changed. If a questions file is expected for this attempt, it needs to be supplied before a reader run can answer it.

There were no questions, so nothing changed. `questions/000959.yaml` does not exist on this branch, and no commit on any branch has ever contained it.

- **Why no questions:** in my earlier author run I asked a reader nothing. My report says "Questions to a reader: none." The reader's answer run found nothing to answer and changed nothing (`transcripts/000959/answer-report.md`).
- **The claims file is the same:** `claims/000959/` has had no commits since my author run, so no claim's statement, expected values or criterion was amended.
- **The open questions are for the paper's authors:** the three in the attempt record (whether a face event on the trial sample counts as a look back with latency 0, which reference M2's reciprocation latency is measured from, and which side the bootstrap p-value take
[... 9 more lines not kept]
```

**Agent**

Let me read the relevant claims in the claims file.

**Agent calls Bash**

```bash
cd claims/000959; python - <<'EOF'
import yaml
d=yaml.safe_load(open('10.1016-j.neuron.2024.05.004.yaml'))
print([k for k in d if k!='claims'])
for c in d['claims']:
    if c['id'] in ('figs1e-eyes-vs-rdm-comparable','fig5a-trigger-duration-unchanged','fig5cd-saccade-counts-unchanged','fig5e-h-saccade-kinematics-unchanged','figs4a-causal-strength-no-stim-effect','ofc-slope-unchanged-by-epoch','fig4c-dmpfc-slope-late-greater','methods-eyes-vs-mouth-bootstrap','design-sessions-per-day'):
        print(yaml.dump(c,width=120,sort_keys=False)); print('-----')
EOF
```

```
['schema_version', 'dataset', 'paper', 'checks']
id: design-sessions-per-day
statement: Each day held on average 10 live social gaze sessions (9 to 11) and 5 non-social control sessions (4 to 8) for
  monkey L, and 15 social (14 to 15) and 5 control sessions for monkey T, each 300 s long.
source: STAR Methods, Experimental setup, paragraph 2
quote: Each data collection day consisted of a total of alternating 10 live social gaze sessions and 5 non-social control
  sessions on average for monkey L (9-11 social and 4-8 control sessions across all days) and alternating 15 live social gaze
  sessions and 5 non-social control sessions on average for monkey T (14-15 social and 5 control sessions across all days).
  Each session lasted 300 sec.
expected:
- quantity: mean social sessions per day, monkey L
  value: 10
  tolerance: 1
- quantity: mean control sessions per day, monkey L
  value: 5
  tolerance: 0.5
- quantity: mean social sessions per day, monkey T
  value: 15
  tolerance: 1.5
- quantity: mean control sessions per day, monkey T
[... 247 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "not_runnable" schemas/ | head; grep -rn -A12 "blocked_by" schemas/*.json 2>/dev/null | grep -i enum -A10 | head -20; ls schemas
```

```
schemas/attempt.schema.json:209:              "not_runnable",
schemas/attempt.schema.json:277:                  "not_runnable",
schemas/attempt.schema.json-203-            "enum": [
schemas/attempt.schema.json-204-              "data_missing",
schemas/attempt.schema.json-205-              "metadata_insufficient",
schemas/attempt.schema.json-206-              "methods_underspecified",
schemas/attempt.schema.json-207-              "data_unreadable",
schemas/attempt.schema.json-208-              "too_large",
schemas/attempt.schema.json-209-              "not_runnable",
schemas/attempt.schema.json-210-              "other"
schemas/attempt.schema.json-211-            ]
schemas/attempt.schema.json-212-          },
schemas/attempt.schema.json-213-          "notes": {
--
schemas/attempt.schema.json-271-                "enum": [
schemas/attempt.schema.json-272-                  "data_missing",
schemas/attempt.schema.json-273-                  "metadata_insufficient",
schemas/attempt.schema.json-274-                  "methods_underspecified",
schemas/attempt.schema.json-275-                  "data_unreadable",
schemas/attempt.schema.json-276-                  "too_large",
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
which octave matlab; curl -sI https://github.com/accyang/causal-decomposition-analysis | head -3; curl -s https://api.github.com/repos/accyang/causal-decomposition-analysis/contents | python -c "import json,sys; [print(x['name']) for x in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -o cd.zip https://github.com/accyang/causal-decomposition-analysis/raw/master/causal_decomposition_20180901.zip && unzip -o -q cd.zip -d cd && find cd -type f | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/cd/causal_decomposition; cat causal_decomposition.m; head -80 eemd/eemd.m
```

```
% Function for calculate absolute and relative causal strengths  
% of a pair of time series
%
% Syntax: causal_matrix = causal_decomposition(s1,s2,rnoise,nensemble)
% Parameters:
% s1: time series 1
% s2: time series 2
% rnoise: the level of noise used in ensemble empirical mode decomposition
%         the rnoise value represents the fraction of standard deviation of
%         time series (e.g., 0.1)
% nensemble: the number of ensemble to average the results of noise-assisted
%            empirical mode decomposition. 
%            The error of IMFs equals to rnoise/sqrt(nensemble)        
% 
% Output:
% The output of causal_decomposition function contains a four by n matrix, 
% where n is the number of IMFs decomposed from the data. The first column 
% in the matrix indicates the relative causal strength from first time series 
% to the second time series and vise versa in the second column. The third 
% column indicates the absolute causal strength from the first time series 
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL https://raw.githubusercontent.com/accyang/causal-decomposition-analysis/master/README.md | head -60; sed -n 80,200p cd/causal_decomposition/eemd/eemd.m | grep -n -i "default\|numImf\|maxSift" | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat entries/000959-fan-2024/microstim.py
```

```
"""Loading and measures for the closed-loop microstimulation gaze data of dandiset 000959.

Fan, Dal Monte, Nair, Fagan & Chang (2024), Neuron 112, 2631-2644,
doi:10.1016/j.neuron.2024.05.004. The claims file is claims/000959/10.1016-j.neuron.2024.05.004.yaml.

Each NWB file holds one 300-s run (a "session" in the paper) of one day: M1's gaze (pixels,
1 kHz), in social runs M2's gaze, pupil size, the stimulation and sham times
(`stimulation_events`), the ROIs of the day (`roi_definitions`), and fixation events as
interval tables (`m1_all`, `m1_eye`, `m1_wholeface`, ..., `m2_*`, `mutual_*`). The
`session_description` names the date, run, subject, stimulated region, triggering ROI (Eyes or
Mouth) and condition (Social, or Dot for the non-social RDM control). Files are read over HTTP
into memory at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial selection (the claims file's opening comment, from the paper's code): a trial is kept
  when its time lies within the valid run (non-NaN `t`) and more than 5 s before the run's last
  valid sample; the first trial of each run is dropped. Trials are grouped by their own label.
- Post-gaze epoch: fixations whose start lies in [0, 1.5) s after the trial (claims file,
  opening comment; STAR Methods, Fixation density map, "within 1.5 sec after the onset").
[... 354 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python -c "
import json;nb=json.load(open('reproduce_fan_2024.ipynb'))
for i in [1,3,5,10,25,27,60,91,92,93,95]:
  print('=== cell',i); print(''.join(nb['cells'][i]['source']))
"
```

```
=== cell 1
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from scipy.stats import mannwhitneyu, wilcoxon
from statsmodels.stats.multitest import multipletests

import microstim as ms

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
AREAS = ["OFC", "dmPFC", "ACCg"]


def signrank(a, b=None):
    """Two-sided Wilcoxon signed-rank test (scipy's default method: exact for small n
    without ties). Returns (n, p)."""
[... 293 more lines not kept]
```

**Agent calls Bash**

```bash
cat requirements.in; python -c "import h5py, PyEMD, statsmodels, scipy; print(scipy.__version__)"; ls ../../executed 2>/dev/null | head; ls ~/.cache 2>/dev/null
```

```
Exit code 2
EMD-signal
h5py
matplotlib
numpy
pandas
requests
scipy
statsmodels
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, PyEMD, statsmodels, scipy; print(scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/entry.py | grep -n "venv\|def \|uv" | head -30
```

```
37:Requires `uv` on PATH, and `pyyaml`, `jsonschema` and `nbformat` to run this
70:    def __init__(self):
73:    def error(self, where, message: str) -> None:
78:def dataset_id(record: dict) -> str | None:
```

**Agent calls Bash**

```bash
cd  uv venv -q $TMPDIR/dev && uv pip install -q --python $TMPDIR/dev/bin/python -r entries/000959-fan-2024/requirements.lock.txt ipykernel 2>&1 | tail -2; $TMPDIR/dev/bin/python -c "import PyEMD, h5py; print('ok')"
```

```
/tmp/claude-1001/dev/lib/python3.13/site-packages/PyEMD/CEEMDAN.py:63: SyntaxWarning: invalid escape sequence '\e'
  Scale for added noise (:math:`\epsilon`) which multiply std :math:`\sigma`:
/tmp/claude-1001/dev/lib/python3.13/site-packages/PyEMD/EEMD.py:41: SyntaxWarning: invalid escape sequence '\h'
  Standard deviation of Gaussian noise (:math:`\hat\sigma`).
ok
```

**Agent**

Now a dev script to load all runs once and cache them (development only; the notebook still streams).

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; date -u; time $TMPDIR/dev/bin/python -c "
import pickle, microstim as ms
assets = ms.list_assets()
runs = ms.load_all(assets)
pickle.dump(runs, open('$TMPDIR/runs.pkl','wb'))
print(len(runs))
"; date -u
```

```
Sun Nov  1 01:19:43 UTC 2026
1705

real	7m22.647s
user	7m23.387s
sys	3m44.308s
Sun Nov  1 01:27:06 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; cat > $TMPDIR/dev_base.py <<'EOF'
import pickle, sys, time
sys.path.insert(0, '.')
import numpy as np, pandas as pd
import microstim as ms
import json
nb = json.load(open('reproduce_fan_2024.ipynb'))
runs = pickle.load(open(sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].endswith('.pkl') else __import__('os').environ['TMPDIR'] + '/runs.pkl', 'rb'))
meta, trials, events = ms.prepare(runs)
exec(''.join(nb['cells'][1]['source']))
import matplotlib; matplotlib.use('Agg')
EOF
cat > $TMPDIR/inv1.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR'] + '/dev_base.py').read())
print("t_first range", meta.t_first.min(), meta.t_first.max(), "t_last", meta.t_last.min(), meta.t_last.max())
print("event start", events.start.min(), events.start.max(), "trial times", trials.time.min(), trials.time.max())
mwf = events[(events.who=='m1')&(events.table=='mutual_wholeface')]
print("mutual counts", {t: int(((events.who=='m1')&(events.table==t)).sum()) for t in ['mutual_wholeface','mutual_eye','mutual_face','mutual_mouth']})
print(events.table.unique())
eyes_days = meta[meta.roi == "Eyes"]
L = eyes_days[(eyes_days.subject=='L')]
spd = L.groupby(['date','cond']).size().unstack()
d8 = spd[spd.Dot==8].index
for d in d8:
    g = L[L.date==d]
    print(d, g[g.cond=='Dot'].sort_values('run').run.tolist(), 'social', g[g.cond=='Social'].sort_values('run').run.tolist(), 'dot lengths', (g[g.cond=='Dot'].t_last-g[g.cond=='Dot'].t_first).round(0).tolist(), 'trials', [int((trials.run_id==r).sum()) for r in g[g.cond=='Dot'].sort_values('run').run_id])
EOF
$TMPDIR/dev/bin/python $TMPDIR/inv1.py
```

```
/bin/bash: line 1: cd: entries/000959-fan-2024: No such file or directory
t_first range 13.757 9659.214 t_last 310.23900000000003 9955.055
event start 13.757 9953.872000000001 trial times 15.554 9945.824
mutual counts {'mutual_wholeface': 5896, 'mutual_eye': 3098, 'mutual_face': 2525, 'mutual_mouth': 273}
<StringArray>
[          'm1_all',    'm1_everywhere',           'm1_eye',         'm1_mouth',        'm1_neface',      'm1_nenmface',     'm1_wholeface',           'm2_all',    'm2_everywhere',
           'm2_eye',         'm2_mouth',        'm2_neface',      'm2_nenmface',     'm2_wholeface',      'mutual_face', 'mutual_wholeface',       'mutual_eye',     'mutual_mouth']
Length: 18, dtype: str
01022020 [1, 2, 3, 4, 5, 6, 7, 8] social [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] dot lengths [296.0, 297.0, 296.0, 296.0, 296.0, 296.0, 296.0, 296.0] trials [13, 16, 15, 19, 20, 24, 22, 25]
01032020 [1, 2, 3, 4, 5, 6, 7, 8] social [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] dot lengths [296.0, 296.0, 296.0, 297.0, 296.0, 297.0, 296.0, 296.0] trials [13, 22, 16, 24, 15, 21, 25, 23]
01072020 [1, 2, 3, 4, 5, 6, 7, 8] social [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] dot lengths [297.0, 296.0, 297.0, 296.0, 296.0, 296.0, 296.0, 296.0] trials [17, 22, 23, 18, 21, 27, 24, 25]
01102020 [1, 2, 3, 4, 5, 6, 7, 8] social [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] dot lengths [296.0, 297.0, 296.0, 296.0, 296.0, 296.0, 296.0, 296.0] trials [29, 28, 31, 27, 34, 31, 31, 27]
01132020 [1, 2, 3, 4, 5, 6, 7, 8] social [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] dot lengths [297.0, 296.0, 296.0, 296.0, 296.0, 297.0, 296.0, 296.0] trials [25, 22, 29, 25, 27, 19, 28, 24]
01172020 [1, 2, 3, 4, 5, 6, 7, 8] social [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] dot lengths [297.0, 296.0, 296.0, 296.0, 297.0, 297.0, 296.0, 296.0] trials [24, 23, 23, 20, 25, 22, 24, 19]
01222020 [1, 2, 3, 4, 5, 6, 7, 8] social [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] dot lengths [296.0, 296.0, 297.0, 297.0, 296.0, 296.0, 296.0, 297.0] trials [28, 27, 23, 23, 21, 25, 17, 21]
01242020 [1, 2, 
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python -c "
import json;nb=json.load(open('reproduce_fan_2024.ipynb'))
print(''.join(nb['cells'][19]['source']))"; cat > $TMPDIR/inv2.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR'] + '/dev_base.py').read())
m1 = events[events.who=='m1']
a = set(zip(m1[m1.table=='m1_mouth'].run_id, m1[m1.table=='m1_mouth'].start.round(4)))
b = set(zip(m1[m1.table=='m1_neface'].run_id, m1[m1.table=='m1_neface'].start.round(4)))
print('m1_mouth', len(a), 'in m1_neface', len(a&b), 'neface', len(b))
soc = trials[trials.kept & (trials.cond == "Social") & (trials.roi == "Eyes")].copy()
ev = events[(events.who == "m1") & events.table.isin(["m1_eye","mutual_eye"])]
p = ms.window_pairs(soc, ev, -10.0, 0.0005)
p = p[p.stop >= p.start - p.lag]
soc['inside'] = soc.index.isin(p.trial)
print(soc.groupby(['region','type']).inside.agg(['mean','size']))
print(soc.groupby(['subject','type']).inside.mean())
# day level stim-sham fraction inside
dm = soc.groupby(['date','region','subject','type']).inside.mean().unstack('type')
for r in AREAS:
    x = dm.xs(r, level='region'); print(r, 'median stim-sham inside', np.median(x.stim-x.sham), signrank(x.stim, x.sham))
# for those not inside: nearest eye event start after, end before
out = soc[~soc.inside]
nxt = ms.window_pairs(out, ev, 0.0005, 2.0).groupby('trial').lag.min()
prv = ms.window_pairs(out, ev, -10, 0.0005)
prv['endlag'] = prv.stop - (prv.start - prv.lag)
prv = prv[prv.endlag < 0].groupby('trial').endlag.max()
print('not inside:', len(out))
print('next eye start within (s) quantiles', nxt.reindex(out.index).quantile([.1,.25,.5,.75,.9]).round(3).to_dict(), 'none within 2s', nxt.reindex(out.index).isna().mean())
print('prev eye end before (s) quantiles', prv.reindex(out.index).quantile([.1,.25,.5,.75,.9]).round(3).to_dict())
# any M1 event in progress at the trial
evall = events[(events.who=='m1') & events.table.isin(['m1_all','mutual_wholeface'])]
pa = ms.window_pairs(out, evall, -10.0, 0.0005); pa = pa[pa.stop >= pa.start - pa.lag]
print('of not inside: inside any M1 event', out.index.isin(pa.trial).mean(), pa.drop_duplicates('trial').target.value_counts().to_dict())
# gaze at trial sample inside Eyes ROI?
inroi=[]
for i,row in out.iterrows():
    r = runs[row.run_id]
    inroi.append(np.nan)
EOF
$TMPDIR/dev/bin/python $TMPDIR/inv2.py
```

```
def roi_counts(evset):
    e = events[(events.roi == "Eyes") & (events.who == "m1")]
    if evset == "M1-only":
        e = e[~e.mutual]
    # non-eye Face: m1_neface, and mutual_face for mutual events (m1_wholeface = m1_eye + m1_neface)
    sel = {"Eyes": (e.cond == "Social") & e.table.isin(["m1_eye", "mutual_eye"]),
           "neFace": (e.cond == "Social") & e.table.isin(["m1_neface", "mutual_face"]),
           "RDM": (e.cond == "Dot") & (e.table == "m1_eye")}
    runs_ = meta[meta.roi == "Eyes"]
    out = {}
    for name, s in sel.items():
        cond = "Dot" if name == "RDM" else "Social"
        per_run = e[s].groupby("run_id").size().reindex(runs_[runs_.cond == cond].run_id, fill_value=0)
        rr = runs_.set_index("run_id").loc[per_run.index]
        df = pd.DataFrame({"n": per_run.to_numpy(), "date": rr.date.to_numpy(), "region": rr.region.to_numpy(),
                           "subject": rr.subject.to_numpy()})
        out[name] = df.groupby(["date", "region", "subject"]).n.agg(["sum", "mean"])
    return pd.concat(out, axis=1).reset_index()


[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python -c "
import json;nb=json.load(open('reproduce_fan_2024.ipynb'))
for i in [0,57,59,61,96,100]: print('=== cell',i); print(''.join(nb['cells'][i]['source']))"
```

```
=== cell 0
# Reproducing Fan et al. (2024) from dandiset 000959

**Paper.** Fan, Dal Monte, Nair, Fagan & Chang (2024), "Closed-loop microstimulations of the
orbitofrontal cortex during real-life gaze interaction enhance dynamic social attention",
Neuron 112, 2631-2644, doi:10.1016/j.neuron.2024.05.004.

**Claims.** `claims/000959/10.1016-j.neuron.2024.05.004.yaml`, written from the accepted author
manuscript (PMC11309918) with its supplement, and the paper's code
(github.com/changlabneuro/microstim-ofc-social-attention at cc0bf994).

**Dataset.** DANDI:000959, version 0.261020.0242. The paper cites the dandiset without a
version. Two versions are published, 0.260531.2104 and 0.261020.0242; the most recent is pinned,
as the protocol asks when the paper cites none. The data check below compares the two asset
lists: both hold the same 1705 assets with the same identifiers, paths and sizes, so the choice
does not change the data.

Each file is one 300-s run (a "session" in the paper) and holds M1's gaze and pupil at 1 kHz,
M2's gaze and pupil in social runs, the stimulation and sham times, the day's ROIs, and
fixation events as interval tables (M1-only, M2-only and mutual events by ROI). Files are read
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; grep -rn -i "otero" paper/* | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -sL -m 30 -o /dev/null -w "%{http_code}\n" http://smc.neuralcorrelate.com/sw/microsaccade-detection/; curl -s -m 30 "https://api.github.com/search/repositories?q=otero-millan+microsaccade" | python -c "import json,sys; d=json.load(sys.stdin); [print(x['full_name'], x['language'], x['description']) for x in d.get('items',[])[:10]]"; grep -n -i "saccade" paper/10.1016-j.neuron.2024.05.004.txt | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.github.com/repos/ocular-motor-lab/otero-millan_et_al_microsaccade_detection/commits?per_page=3" | python -c "import json,sys; [print(c['sha'], c['commit']['author']['date'], c['commit']['message'][:60]) for c in json.load(sys.stdin)]"; curl -s "https://api.github.com/repos/ocular-motor-lab/otero-millan_et_al_microsaccade_detection/git/trees/HEAD?recursive=1" | python -c "import json,sys; [print(x['path'], x.get('size')) for x in json.load(sys.stdin)['tree']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://raw.githubusercontent.com/ocular-motor-lab/otero-millan_et_al_microsaccade_detection/ce2c10dc6d8c38348b31e479751ac0da8cda6e6e; for f in Example.m ClusterDetection/SaccadeDetectorCluster.m ClusterDetection/SaccadeDetector.m; do curl -s $B/$f -o $(basename $f); done; cat Example.m; cat SaccadeDetectorCluster.m
```

```
%%
% this script shows how to use the microsaccade detection method
% published in Otero-Millan et al. Journal of Vision 2014

% Set up variables --------------------------------------------------------
folder = fileparts(mfilename('fullpath'));
if ( isempty( folder) )
    folder = pwd;
end
folder = [folder '\data'];


% =========================================================================
% EDIT THIS ===============================================================
% Make sure to fill the variables samples with the eye movement data in the
% proper colums. In blinks mark all the samples that are not good data. In
% most VOG systems it is best to remove 100 ms before and after the blink
% to remove all artifacts.
% =========================================================================
    session = 'test';
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://raw.githubusercontent.com/ocular-motor-lab/otero-millan_et_al_microsaccade_detection/ce2c10dc6d8c38348b31e479751ac0da8cda6e6e/%2BClusterDetection; for f in SaccadeDetectorCluster.m SaccadeDetector.m EyeMovRecording.m; do curl -s $B/$f -o $f; done; wc -l *.m; cat SaccadeDetectorCluster.m
```

```
68 Example.m
  309 EyeMovRecording.m
  320 SaccadeDetector.m
  294 SaccadeDetectorCluster.m
  991 total
classdef SaccadeDetectorCluster < ClusterDetection.SaccadeDetector
    %SACCADEDETECTORCLUSTER Implementation of the saccade detection method
    %using kmeans
    %
    % Jorge Otero-Millan, [removed: an e-mail address] 2/17/2014
    %
    
    properties
        MINIPI = 0; % minimum inter peak interval
        RATEOFPEAKS = 5; % number of peaks per second
        MINPEAKVEL = 1;
        
        featureSelection
        
        NumMaxClusters
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat SaccadeDetector.m; cat EyeMovRecording.m
```

```
classdef SaccadeDetector < handle
    %SACCADEDETECTOR Summary of this class goes here
    %   Detailed explanation goes here
    %
    % Jorge Otero-Millan, [removed: an e-mail address] 2/17/2014
    %
    
    properties
        MIN_ISI = 30;
        SACCADELIMITTH = 5;
        SACCADELIMITTHACC = 0;
    end
    
    methods(Static=true)
        
        function saccadeDetector = getSaccadeDetector( )
            saccadeDetector = ClusterDetection.SaccadeDetectorCluster( );
            saccadeDetector.Init( );
        end
    end
[... 609 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/inv3.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR'] + '/dev_base.py').read())
for d in ['08142019', '12102019', '12132019']:
    g = meta[(meta.date==d)&(meta.cond=='Social')]
    rel = set()
    for rid in g.run_id:
        ro = runs[rid]['rois']; e = ms._centre(ro['roi_m1_eyes'])
        rel.add((tuple(np.round(ro['roi_m1_face']-np.r_[e,e],1)), tuple(np.round(ro['roi_m1_eyes']-np.r_[e,e],1))))
    print(d, g.region.iloc[0], g.subject.iloc[0], len(rel), rel)
EOF
$TMPDIR/dev/bin/python $TMPDIR/inv3.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/inv3.py", line 1, in <module>
    exec(open(__import__('os').environ['TMPDIR'] + '/dev_base.py').read())
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 4, in <module>
ModuleNotFoundError: No module named 'microstim'
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024 && $TMPDIR/dev/bin/python $TMPDIR/inv3.py
```

```
08142019 dmPFC L 2 {((np.float64(-86.2), np.float64(-53.0), np.float64(90.6), np.float64(111.7)), (np.float64(-83.1), np.float64(-48.1), np.float64(83.1), np.float64(48.1))), ((np.float64(-73.8), np.float64(-35.0), np.float64(73.4), np.float64(95.7)), (np.float64(-63.4), np.float64(-36.7), np.float64(63.4), np.float64(36.7)))}
12102019 dmPFC L 2 {((np.float64(-110.5), np.float64(-64.9), np.float64(83.4), np.float64(91.6)), (np.float64(-63.4), np.float64(-36.7), np.float64(63.4), np.float64(36.7))), ((np.float64(-98.4), np.float64(-57.5), np.float64(83.2), np.float64(96.5)), (np.float64(-79.8), np.float64(-46.2), np.float64(79.8), np.float64(46.2)))}
12132019 ACCg L 2 {((np.float64(-102.8), np.float64(-50.6), np.float64(81.8), np.float64(90.7)), (np.float64(-52.2), np.float64(-30.2), np.float64(52.2), np.float64(30.2))), ((np.float64(-87.4), np.float64(-58.3), np.float64(97.5), np.float64(101.4)), (np.float64(-61.3), np.float64(-35.5), np.float64(61.3), np.float64(35.5)))}
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='microstim.py'
s=open(p).read()
s=s.replace('''def _dec(x):''','''def file_layout(asset_id: str) -> dict:
    """Names of the top-level groups of one file and of the groups under `intervals`,
    `processing` (if any), `acquisition` and `scratch`."""
    content = requests.get(f"{API}/assets/{asset_id}/download/", timeout=300).content
    with h5py.File(io.BytesIO(content), "r") as f:
        out = {"/": sorted(f.keys())}
        for g in ["intervals", "processing", "acquisition", "scratch", "analysis"]:
            out[g] = sorted(f[g].keys()) if g in f else None
    return out


def _dec(x):''',1)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nbedit.py <<'EOF'
import json, sys
P = 'reproduce_fan_2024.ipynb'
nb = json.load(open(P))
def src(i): return ''.join(nb['cells'][i]['source'])
def setsrc(i, s): nb['cells'][i]['source'] = s.splitlines(keepends=True)
def rep(i, old, new):
    s = src(i)
    assert s.count(old) == 1, (i, old[:60], s.count(old))
    setsrc(i, s.replace(old, new))
def save(): json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
head -c 300 reproduce_fan_2024.ipynb | cat -A | head -5; tail -c 50 reproduce_fan_2024.ipynb | cat -A
```

```
{$
 "cells": [$
  {$
   "cell_type": "markdown",$
   "id": "eb842472",$
3"$
  }$
 },$
 "nbformat": 4,$
 "nbformat_minor": 5$
}$
```

**Agent calls Bash**

```bash
cat > $TMPDIR/e1.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR'] + '/nbedit.py').read())
# sanity: file layout, time ranges, mutual totals
rep(3, '''print(f"loaded {len(runs)} runs in {(time.time() - t_start) / 60:.1f} min")
''', '''print(f"loaded {len(runs)} runs in {(time.time() - t_start) / 60:.1f} min")
lay = ms.file_layout(assets.asset_id.iloc[0])
print("groups of one file,", assets.path.iloc[0])
for g, names in lay.items():
    print(f"  {g}: {names}")
print("tables named like saccade in any group of that file:",
      [n for names in lay.values() if names for n in names if "sacc" in n.lower()])
''')
rep(3, '''print("event start indices are 1-based''', '''print("times (s): first valid sample", round(meta.t_first.min(), 3), "to", round(meta.t_first.max(), 3),
      "; last valid sample", round(meta.t_last.min(), 3), "to", round(meta.t_last.max(), 3),
      "; event starts", round(events.start.min(), 3), "to", round(events.start.max(), 3),
      "; trial times", round(trials.time.min(), 3), "to", round(trials.time.max(), 3),
      "(all below the 1e6 s run offset used by window_pairs)")
print("event start indices are 1-based''')
rep(3, '''alls = set(''', '''print("  mutual_wholeface:", len(mw), "events; mutual_eye + mutual_face + mutual_mouth:",
      sum(int((m1.table == t).sum()) for t in ["mutual_eye", "mutual_face", "mutual_mouth"]),
      "(mutual_face is the face outside Eyes and Mouth)")
mo = set(zip(m1[m1.table == "m1_mouth"].run_id, m1[m1.table == "m1_mouth"].start.round(4)))
ne = set(zip(m1[m1.table == "m1_neface"].run_id, m1[m1.table == "m1_neface"].start.round(4)))
print("  m1_mouth events:", len(mo), "of which in m1_neface:", len(mo & ne), "(m1_neface is the face outside Eyes, Mouth included)")
alls = set(''')
# sessions: L control run listing
rep(10, '''print("number of social runs per day, monkey T:"''', '''d8 = spd.loc["L"][spd.loc["L", "Dot"] == 8].index
l8 = eyes_days[(eyes_days.subject == "L") & eyes_days.date.isin(d8) & (eyes_days.cond == "Dot")]
print("monkey L days with 8 control runs:", len(d8), "; their control run numbers:",
      sorted({tuple(sorted(g.run)) for _, g in l8.groupby("date")}),
      "; run length (s)", round((l8.t_last - l8.t_first).min(), 1), "to", round((l8.t_last - l8.t_first).max(), 1),
      "; kept trials per run", trials[trials.kept & trials.run_id.isin(l8.run_id)].groupby("run_id").size().agg(["min", "median", "max"]).to_dict())
print("number of social runs per day, monkey T:"''')
# figs1e: non-eye face adds mutual_mouth
rep(19, '''    # non-eye Face: m1_neface, and mutual_face for mutual events (m1_wholeface = m1_eye + m1_neface)
    sel = {"Eyes": (e.cond == "Social") & e.table.isin(["m1_eye", "mutual_eye"]),
           "neFace": (e.cond == "Social") & e.table.isin(["m1_neface", "mutual_face"]),''', '''    # non-eye Face: m1_neface (Mouth included), and mutual_face and mutual_mouth for mutual events
    # (m1_wholeface = m1_eye + m1_neface; mutual_wholeface = mutual_eye + mutual_face + mutual_mouth)
    sel = {"Eyes": (e.cond == "Social") & e.table.isin(["m1_eye", "mutual_eye"]),
           "neFace": (e.cond == "Social") & e.table.isin(["m1_neface", "mutual_face", "mutual_mouth"]),''')
save()
EOF
$TMPDIR/dev/bin/python $TMPDIR/e1.py
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/e2.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR'] + '/nbedit.py').read())
rep(27, '''    rid = soc[soc.date == date].run_id.iloc[0]
    ro = runs[rid]["rois"]
    e = ms._centre(ro["roi_m1_eyes"])
    masks = {}
    for nm, key in [("face", "roi_m1_face"), ("eyes", "roi_m1_eyes")]:
        r = ro[key]
        xs = np.sort((r[[0, 2]] - e[0]) * ms.DEG_PER_PX * (-1 if subject == "T" else 1))
        ys = np.sort((r[[1, 3]] - e[1]) * ms.DEG_PER_PX)
        masks[nm] = (gx >= xs[0]) & (gx <= xs[1]) & (gy >= ys[0]) & (gy <= ys[1])
''', '''    # squares inside the ROI, relative to the Eyes centre, in every social run of the day
    # (three recalibrated days have two ROI sets; the intersection keeps the squares common to both)
    masks = {"face": np.ones_like(gx, bool), "eyes": np.ones_like(gx, bool)}
    for rid in soc[soc.date == date].run_id.unique():
        ro = runs[rid]["rois"]
        e = ms._centre(ro["roi_m1_eyes"])
        for nm, key in [("face", "roi_m1_face"), ("eyes", "roi_m1_eyes")]:
            r = ro[key]
            xs = np.sort((r[[0, 2]] - e[0]) * ms.DEG_PER_PX * (-1 if subject == "T" else 1))
            ys = np.sort((r[[1, 3]] - e[1]) * ms.DEG_PER_PX)
            masks[nm] &= (gx >= xs[0]) & (gx <= xs[1]) & (gy >= ys[0]) & (gy <= ys[1])
''')
rep(27, '''print("squares inside the ROIs per day, median:", hm.n_face_squares.median(), hm.n_eye_squares.median())''',
'''print("squares inside the ROIs per day, median:", hm.n_face_squares.median(), hm.n_eye_squares.median())
print("recalibrated days and their regions:", meta[meta.date.isin(nvar)].groupby("date").region.first().to_dict())''')
rep(27, '''    a.set_xlabel("deg (contra <- -> ipsi for L)")''', '''    a.set_xlabel("deg from the Eyes centre (ipsi <- -> contra)")''')
rep(27, '''sgn = np.where(pairs.subject == "T", -1.0, 1.0)''', '''sgn = np.where(pairs.subject == "T", -1.0, 1.0)   # negative dx is ipsilateral for both monkeys''')
save()
EOF
$TMPDIR/dev/bin/python $TMPDIR/e2.py
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/e3.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR'] + '/nbedit.py').read())
setsrc(60, '''rows = []
for reading, mkey in [("methods", "social"), ("code", "social, code reading")]:
    rng = np.random.default_rng(959)
    for h in [None, "contra", "ipsi"]:
        e = dist[(reading, h)][1]
        e = e[e.region == "OFC"].assign(eff=lambda d: d.stim - d.sham).dropna(subset=["eff"])
        m = mouth_dm[(mkey, h)]
        m = m[m.region == "OFC"].assign(eff=lambda d: d.stim - d.sham).dropna(subset=["eff"])
        mouth_med = np.median(m.eff)
        for pool in ["all", "T"]:
            x = (e if pool == "all" else e[e.subject == "T"]).eff.to_numpy()
            boots = np.median(rng.choice(x, size=(1000, 5), replace=True), axis=1)
            pa = np.mean(boots >= mouth_med)
            pb = min(1.0, 2 * min(np.mean(boots >= mouth_med), np.mean(boots <= mouth_med)))
            rows.append(dict(fixations=reading, hemifield=h or "both", eyes_days=pool, n_eyes=len(x), n_mouth=len(m),
                             eyes_median=np.median(x), boot_median=np.median(boots), mouth_median=mouth_med,
                             p_a_one_sided=pa, p_b_two_sided=pb))
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f"{v:.4g}"))
print("\\ncontralateral, all Eyes days, p under readings (a) and (b) for five other seeds:")
for reading, mkey in [("methods", "social"), ("code", "social, code reading")]:
    e = dist[(reading, "contra")][1]
    e = e[e.region == "OFC"].assign(eff=lambda d: d.stim - d.sham).dropna(subset=["eff"]).eff.to_numpy()
    m = mouth_dm[(mkey, "contra")]
    mm = np.median((m[m.region == "OFC"].stim - m[m.region == "OFC"].sham).dropna())
    for seed in range(1, 6):
        b = np.median(np.random.default_rng(seed).choice(e, size=(1000, 5), replace=True), axis=1)
        print(f"  {reading} fixations, seed {seed}: (a) {np.mean(b >= mm):.3f}  (b) {min(1, 2 * min(np.mean(b >= mm), np.mean(b <= mm))):.3f}")
''')
rep(59, '''Day effects are stimulation minus sham day means (Methods fixation reading).''',
'''Day effects are stimulation minus sham day means, under the Methods fixation reading (M1-only
and mutual events) and, as a variant, the code's (M1-only events).''')
setsrc(95, '''trig = {}
for rd, tabs in [("a", ["m1_eye", "mutual_eye"]), ("b", ["m1_eye"])]:
    ev = events[(events.who == "m1") & events.table.isin(tabs)]
    p = ms.window_pairs(soc, ev, -10.0, 0.0005)
    p = p[p.stop >= p.start - p.lag]
    p["dur"] = (p.stop - p.start) * 1000
    t = soc.copy()
    t["trig"] = t.index.map(p.groupby("trial").dur.max()).astype(float)
    trig[rd] = t
    print(f"reading ({rd}): trials with an Eyes event in progress {int(t.trig.notna().sum())} of {len(t)}; "
          f"median duration {t.trig.median():.0f} ms")
    show(day_table(ms.day_means(t, "trig"), subjects=(None,)), "duration (ms), day level", degrees=False)

# the trials with no Eyes event in progress (reading a)
t = trig["a"].assign(none=lambda d: d.trig.isna())
print("\\nfraction of trials with no Eyes event in progress, by area and trial type:")
print(t.groupby(["region", "type"]).none.agg(["mean", "size"]).unstack("type").round(3))
print("by monkey and trial type:")
print(t.groupby(["subject", "type"]).none.mean().unstack("type").round(3))
dn = t.groupby(["date", "region", "subject", "type"]).none.mean().unstack("type").reset_index()
print("stimulation minus sham fraction per day, signed-rank over days:")
show(day_table(dn, subjects=(None,)), "", degrees=False)
out = t[t.none]
ev_a = events[(events.who == "m1") & events.table.isin(["m1_eye", "mutual_eye"])]
nxt = ms.window_pairs(out, ev_a, 0.0005, 2.0).groupby("trial").lag.min().reindex(out.index)
print(f"of the {len(out)} trials with none: an Eyes event starts within 20 ms after the trial in "
      f"{int((nxt <= 0.02).sum())}, within 2 s in {int(nxt.notna().sum())}")
anyev = events[(events.who == "m1") & events.table.isin(["m1_everywhere", "m1_neface", "mutual_face", "mutual_mouth"])]
pa = ms.window_pairs(out, anyev, -10.0, 0.0005)
pa = pa[pa.stop >= pa.start - pa.lag].drop_duplicates("trial")
print("  inside another M1 event at the trial time:", len(pa), "; by table:", pa.table.value_counts().to_dict())

# variant: an Eyes event that starts within 20 ms after the trial counts as the trigger
ev = ev_a
p2 = ms.window_pairs(soc, ev, -10.0, 0.0205)
p2 = p2[(p2.stop >= p2.start - p2.lag) | (p2.lag > 0)]
p2["dur"] = (p2.stop - p2.start) * 1000
tv = soc.copy()
tv["trig"] = tv.index.map(p2.sort_values("lag").groupby("trial").dur.first()).astype(float)
print(f"\\nvariant, Eyes event in progress or starting within 20 ms (reading a): {int(tv.trig.notna().sum())} trials")
show(day_table(ms.day_means(tv, "trig"), subjects=(None,)), "duration (ms), day level", degrees=False)
''')
save()
EOF
$TMPDIR/dev/bin/python $TMPDIR/e3.py
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/run_nb.py <<'EOF'
import json, sys, os, pickle, io, contextlib, time
sys.path.insert(0, '.')
import matplotlib; matplotlib.use('Agg')
nb = json.load(open('reproduce_fan_2024.ipynb'))
show_cells = set(int(x) for x in sys.argv[1].split(',')) if len(sys.argv) > 1 and sys.argv[1] else set()
skip = set(int(x) for x in sys.argv[2].split(',')) if len(sys.argv) > 2 and sys.argv[2] else set()
stop = int(sys.argv[3]) if len(sys.argv) > 3 else 10**6
g = {}
for i, c in enumerate(nb['cells']):
    if i > stop: break
    if c['cell_type'] != 'code' or i in skip: continue
    s = ''.join(c['source'])
    s = s.replace('runs = ms.load_all(assets)', 'runs = pickle.load(open(os.environ["TMPDIR"] + "/runs.pkl", "rb"))')
    g.update(pickle=pickle, os=os)
    t0 = time.time()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(s, f'cell{i}', 'exec'), g)
    if i in show_cells:
        print(f'===== cell {i} ({time.time()-t0:.1f}s)'); print(buf.getvalue())
    else:
        print(f'cell {i} {time.time()-t0:.1f}s', file=sys.stderr)
EOF
date -u; $TMPDIR/dev/bin/python $TMPDIR/run_nb.py 3,10,20,22,27,60,95 92,98 2>&1 | grep -v "^cell " ; date -u
```

```
Sun Nov  1 01:29:57 UTC 2026
===== cell 3 (10.9s)
version 0.261020.0242: 1705 assets, 26.0 GB; version 0.260531.2104: 1705 assets; rows not shared: 0
loaded 1705 runs in 0.1 min
groups of one file, sub-L/sub-L_ses-20190718_obj-1wqjp5d_behavior.nwb
  /: ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'intervals', 'processing', 'scratch', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time']
  intervals: ['m1_all', 'm1_everywhere', 'm1_eye', 'm1_mouth', 'm1_neface', 'm1_nenmface', 'm1_wholeface']
  processing: []
  acquisition: ['EyeTracking_m1', 'pupil_m1', 'roi_definitions', 'stimulation_events', 't']
  scratch: ['stimulated_region', 'stimulation_condition', 'stimulation_roi']
  analysis: []
tables named like saccade in any group of that file: []

The description, the scratch fields and the file name agree: True
runs by subject, triggering ROI, region and condition:
cond                  Dot  Social
subject roi   region             
L       Eyes  ACCg     91     150
              OFC      92     150
              dmPFC    88     150
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 120,200p $TMPDIR/cd/causal_decomposition/eemd/eemd.m; ls $TMPDIR/dev/lib/python3.13/site-packages/PyEMD/
```

```
end

function [Y, NoiseLevel, NE, numImf, runCEEMD, maxSift, typeSpline,toModifyBC,randType,seedNo, IsInputOkay] = parse_checkProperty(Y, NoiseLevel, NE, numImf, varargin)
% Default Parameters
runCEEMD = 0; % Original EEMD
maxSift = 10; % maxSift = 10
typeSpline = 2;
toModifyBC = 1;
randType = 2;
seedNo = 1; % now
checkSignal = 0;
IsInputOkay = true;

if(~isempty(varargin{1}))

for iArg = 1 : length(varargin{1});
    
if(iArg == 1)
   runCEEMD = varargin{1}{iArg};
   if(runCEEMD ~= 0 && runCEEMD ~= 1)
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('reproduce_fan_2024.ipynb'))
print(''.join(nb['cells'][89]['source']))"
```

```
allsoc = trials[(trials.cond == "Social") & (trials.roi == "Eyes")]
ns = pd.DataFrame({
    "a_kept": allsoc[allsoc.kept & (allsoc.type == "stim")].groupby("date").size(),
    "b_all": allsoc[allsoc.type == "stim"].groupby("date").size()}).fillna(0).astype(int)
ns = ns.join(meta.drop_duplicates("date").set_index("date")[["subject", "region"]])
for col in ["a_kept", "b_all"]:
    ok = ns[col] >= 90
    print(f"reading ({col}): days with at least 90 stimulations {int(ok.sum())} of {len(ns)}; excluded:")
    print(ns[~ok].sort_values(["subject", "region"]).to_string())
named = ["08122019", "12222021", "11052021", "12172021", "11042021"]
print("\nthe five days the code names:")
print(ns.loc[named].to_string())
print("stimulations per day, quantiles (a):", ns.a_kept.quantile([0, 0.1, 0.5, 1]).to_dict())
```

**Agent**

Now a quick timing test of PyEMD with the Yang code's settings before writing the cell.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > t_emd.py <<'EOF'
import time, numpy as np
from PyEMD import EEMD, EMD
from scipy.interpolate import CubicSpline
rng = np.random.default_rng(4)
sig = np.cumsum(rng.normal(size=150)); sig = (sig - sig.mean()) / sig.std()
for label, emd in [("default sifting", EMD()), ("10 fixed sifts", EMD(FIXE=10))]:
    e = EEMD(trials=100, noise_width=0.2, ext_EMD=emd, parallel=False, separate_trends=False)
    e.noise_seed(4)
    t0 = time.time(); imfs = e.eemd(sig, max_imf=6); dt = time.time() - t0
    print(label, f"100 ensembles {dt:.2f}s, imfs {imfs.shape}")
e = EEMD(trials=1000, noise_width=0.2, ext_EMD=EMD(FIXE=10), parallel=False); e.noise_seed(4)
t0 = time.time(); imfs = e.eemd(sig, max_imf=6); print("1000 ens", time.time()-t0, imfs.shape)
e = EEMD(trials=1000, noise_width=0.2, ext_EMD=EMD(FIXE=10), parallel=True, processes=4); e.noise_seed(4)
t0 = time.time(); imfs = e.eemd(sig, max_imf=6); print("1000 ens 4 proc", time.time()-t0, imfs.shape)
x = np.linspace(0, 149, 25); y = rng.normal(size=25); tt = np.arange(150.)
t0 = time.time()
for _ in range(2000): CubicSpline(x, y)(tt)
print("one spline fit + evaluation (us):", (time.time()-t0)/2000*1e6)
EOF
$TMPDIR/dev/bin/python t_emd.py 2>&1 | grep -v Warning
```

```
default sifting 100 ensembles 0.58s, imfs (7, 150)
10 fixed sifts 100 ensembles 1.85s, imfs (7, 150)
1000 ens 18.52447009086609 (7, 150)
1000 ens 4 proc 8.829447984695435 (7, 150)
one spline fit + evaluation (us): 109.75754261016846
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024 && cat > $TMPDIR/e4.py <<'EOF'
exec(open(__import__('os').environ['TMPDIR'] + '/nbedit.py').read())
rep(3, '''print("  mutual_wholeface:", len(mw), "events;''', '''print("  mutual_wholeface:", int((m1.table == "mutual_wholeface").sum()), "events;''')
setsrc(91, '''## Causal decomposition claims (blocked)

figs4a-causal-strength-no-stim-effect, figs4b-causal-strength-no-epoch-effect,
ofc-slope-unchanged-by-epoch, fig4c-dmpfc-slope-late-greater, fig4d-dmpfc-slope-permutation and
dmpfc-slope-positive all rest on the relative causal strength of each trial, from the causal
decomposition of Yang, Peng and Huang (2018), which is built on ensemble empirical mode
decomposition (EEMD). The Yang et al. code (`causal_decomposition.m`, release
causal_decomposition_20180901 at github.com/accyang/causal-decomposition-analysis) normalises both
series, runs one EEMD of each, then for each IMF removes it from each series and runs one EEMD of
each again: 2 + 2 x (number of IMFs) EEMDs per trial. Its `eemd.m` sifts a fixed 10 times per IMF
(`maxSift = 10`, the default). Neither the noise level nor the ensemble size has a default in
that code; its example call uses noise 0.35 and 1,000 ensembles. The claims file's reading (a)
takes noise 0.2 and 1,000 ensembles, and reading (b), the code's settings, is taken here as the
example's 0.35 and 1,000, so both readings need 1,000 ensembles and cost the same (the noise
level does not change the work).

The cell below times one EEMD of one 150-bin series with PyEMD set to the Yang code's sifting (10
fixed sifts), at 1,000 ensembles on one core and on four processes, and counts the trials each
claim needs: every social Eyes trial for figs4a and figs4b, and the first 90 stimulation trials of
each of the 76 epoch days for the four slope claims (by area). It also gives a floor for any
implementation: the number of cubic-spline envelopes the decomposition fits, times the measured
cost of one scipy spline fit on 150 points.''')
setsrc(92, '''from PyEMD import EEMD, EMD

rng_c = np.random.default_rng(4)
sig = np.cumsum(rng_c.normal(size=150))
sig = (sig - sig.mean()) / sig.std()
cost = {}
for label, kw in [("one core", dict(parallel=False)), ("four processes", dict(parallel=True, processes=4))]:
    eemd = EEMD(trials=1000, noise_width=0.2, ext_EMD=EMD(FIXE=10), **kw)
    eemd.noise_seed(4)
    t0 = time.time()
    imfs = eemd.eemd(sig)
    cost[label] = time.time() - t0
n_imf = imfs.shape[0]
per_eemd = cost["one core"]
n_eemd = 2 + 2 * n_imf          # Yang et al. (2018), causal_decomposition.m
per_trial = per_eemd * n_eemd
print(f"EEMD of one 150-bin series, 1,000 ensembles, 10 fixed sifts: {cost['one core']:.1f} s on one core, "
      f"{cost['four processes']:.1f} s on four processes; {n_imf} IMFs; {n_eemd} EEMDs per trial; "
      f"{per_trial:.0f} CPU s per trial")
from scipy.interpolate import CubicSpline
xk, tt = np.linspace(0, 149, 25), np.arange(150.0)
t0 = time.time()
for _ in range(1000):
    CubicSpline(xk, rng_c.normal(size=25))(tt)
spline_s = (time.time() - t0) / 1000
n_splines = 1000 * (n_imf - 1) * 10 * 2 * n_eemd   # ensembles x IMFs x sifts x two envelopes x EEMDs
print(f"one spline fit and evaluation: {spline_s * 1e6:.0f} us; splines per trial {n_splines:,}; "
      f"floor per trial {n_splines * spline_s:.0f} s at this cost, {n_splines * 10e-6:.0f} s at 10 us per spline")

epoch_days = ns[ns.a_kept >= 90]
n90 = epoch_days.groupby("region").size() * 90
need = {"figs4a, figs4b: every social Eyes trial": len(soc),
        "slope claims: first 90 stimulations of the 76 epoch days": int(n90.sum())}
need.update({f"  of which {r} days ({int(n90[r] / 90)})": int(n90[r]) for r in AREAS})
speed4 = cost["one core"] / cost["four processes"]
rows = [dict(subset=k, trials=v, cpu_hours=v * per_trial / 3600, wall_hours_4_processes=v * per_trial / 3600 / speed4,
             floor_cpu_hours_10us=v * n_splines * 10e-6 / 3600) for k, v in need.items()]
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f"{v:.1f}"))
print("notebook limit: 1 hour of wall time")''')
setsrc(93, '''**Result: blocked (too_large).** At the Yang code's settings, which both readings share (1,000 ensembles, 10 fixed sifts), the smallest subset any of the six claims needs, the OFC epoch days of ofc-slope-unchanged-by-epoch, takes the CPU and wall hours printed above, and figs4a needs every social trial. Each is far beyond the one-hour limit of a notebook, and the spline floor shows that a compiled implementation at 10 us per spline would still exceed it for every subset. The relative causal strength is therefore not computed and the six claims that use it are blocked.

## Saccade claims''')
save()
EOF
$TMPDIR/dev/bin/python $TMPDIR/e4.py && $TMPDIR/dev/bin/python $TMPDIR/run_nb.py 92 98,95,60 2>&1 | grep -v "^cell \|Warning\|escape\|Scale\|Standard"
```

```
===== cell 92 (27.8s)
EEMD of one 150-bin series, 1,000 ensembles, 10 fixed sifts: 18.5 s on one core, 9.1 s on four processes; 7 IMFs; 16 EEMDs per trial; 296 CPU s per trial
one spline fit and evaluation: 117 us; splines per trial 1,920,000; floor per trial 224 s at this cost, 19 s at 10 us per spline
                                                  subset  trials  cpu_hours  wall_hours_4_processes  floor_cpu_hours_10us
                 figs4a, figs4b: every social Eyes trial   19474     1599.6                   787.1                 103.9
slope claims: first 90 stimulations of the 76 epoch days    6840      561.8                   276.5                  36.5
                                  of which OFC days (25)    2250      184.8                    90.9                  12.0
                                of which dmPFC days (25)    2250      184.8                    90.9                  12.0
                                 of which ACCg days (26)    2340      192.2                    94.6                  12.5
notebook limit: 1 hour of wall time
```

**Agent calls Bash**

```bash
date -u
```

```
Sun Nov  1 01:32:52 UTC 2026
```

**Agent calls Bash**

```bash
cat >> microstim.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Saccade detection: a Python port of the unsupervised clustering method of Otero-Millan et al.
# (2014, J Vis 14(2):18), from the authors' MATLAB code at
# github.com/ocular-motor-lab/otero-millan_et_al_microsaccade_detection, commit ce2c10dc
# (+ClusterDetection/SaccadeDetectorCluster.m, SaccadeDetector.m, EyeMovRecording.m), the
# software the paper's key resources table names. Defaults of that code are kept: 5 velocity
# peaks per second of valid data, 20 ms between peaks, saccade limits at 5 deg/s, a 6-point
# Bartlett differentiator, features log peak velocity and log peak acceleration before and
# after the peak, whitened, k-means with 2 to 4 clusters chosen by the mean silhouette
# (squared Euclidean, as MATLAB's default), and clusters with mean displacement above 0.2 deg
# taken as saccades. The recording is one eye (M1's), positions in degrees (pixels times
# DEG_PER_PX, an assumption: the paper does not say what units it passed). Invalid samples are
# NaN gaze, padded by 100 ms on each side, as Example.m of that code advises for blinks; the
# first 1 s and last 10 ms of the recording are cropped (EyeMovRecording.GetTrials).
# Differences from the MATLAB code: scipy's k-means (Lloyd iterations from the same starting
# centres; MATLAB's default also runs batch updates only) in place of MATLAB's kmeans.
# ---------------------------------------------------------------------------------------------

SAC_RATE_OF_PEAKS = 5
SAC_MIN_IPI_MS = 20
SAC_LIMIT_DEG_S = 5.0
SAC_MIN_DISPLACEMENT_DEG = 0.2
SAC_BLINK_PAD_MS = 100


def _differentiate(x, rate):
    """EyeMovRecording.Differenciate: causal 6-point Bartlett filter, difference, shifted."""
    w = np.array([0.0, 0.4, 0.8, 0.8, 0.4, 0.0])
    w = w / w.sum()
    xf = np.zeros_like(x)
    for k in range(6):  # filter(w, 1, x), with NaN propagating as in MATLAB
        xf[k:] += w[k] * x[:len(x) - k] if k else w[k] * x
    dxf = np.diff(xf, axis=0) * rate
    v = np.zeros_like(x)
    v[:-3] = dxf[2:]
    return v


def _find_peaks(data, mindist, npeaks):
    """SaccadeDetectorCluster.myfindpeaks: greedy highest local maxima, each the highest point
    within +-mindist samples, other maxima within mindist of an accepted one discarded."""
    with np.errstate(invalid="ignore"):
        d = np.diff(data)
        cand = np.flatnonzero((d[:-1] >= 0) & (d[1:] <= 0)) + 1
    vals = data[cand]
    filled = np.where(np.isnan(data), -np.inf, data)
    from scipy.ndimage import maximum_filter1d
    wmax = maximum_filter1d(filled, size=2 * mindist + 1, mode="nearest")
    order = np.lexsort((cand, -vals))     # highest first, ties by position (MATLAB max)
    removed = np.zeros(len(cand), bool)
    out = []
    for j in order:
        if len(out) >= npeaks:
            break
        if removed[j]:
            continue
        c = cand[j]
        removed[j] = True
        lo, hi = max(0, c - mindist), min(len(data) - 1, c + mindist)
        if not (vals[j] < filled[lo:hi + 1]).any():
            out.append(c)
            a, b = np.searchsorted(cand, [c - mindist, c + mindist + 1])
            removed[a:b] = True
    return np.sort(np.array(out, int))


def _kmeans_silhouette_choice(X, vels, max_k=4):
    """SaccadeDetectorCluster.ClusterPeaks: k-means for 2..max_k clusters from velocity-ranked
    starting centres; clusters renumbered by mean peak velocity (0 = fastest); keep the k whose
    two-group (fastest cluster against the rest) mean silhouette is highest, stopping when it
    no longer grows by 1%."""
    from scipy.cluster.vq import kmeans2
    smax, best = 0.0, None
    rank = np.argsort(vels, kind="stable")
    D = ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)   # squared Euclidean (MATLAB default)
    for k in range(2, max_k + 1):
        size = len(vels) // k
        starts = np.array([X[rank[i * size:(i + 1) * size]].mean(0) for i in range(k)])
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            _, lab = kmeans2(X, starts, minit="matrix", iter=100, missing="warn")
        means = np.array([vels[lab == i].mean() if (lab == i).any() else -np.inf for i in range(k)])
        new = np.empty(k, int)
        new[np.argsort(-means, kind="stable")] = np.arange(k)
        lab = new[lab]
        two = np.minimum(lab, 1)
        a = np.array([D[i, two == two[i]].sum() / max((two == two[i]).sum() - 1, 1) for i in range(len(X))])
        b = np.array([D[i, two != two[i]].mean() if (two != two[i]).any() else 0 for i in range(len(X))])
        s = np.where(np.maximum(a, b) > 0, (b - a) / np.maximum(a, b), 0).mean()
        if smax * 1.01 > s:
            break
        smax, best = s, lab
    return best


def detect_saccades(gx, gy, rate=1000.0):
    """Saccades of one recording (positions in degrees). Returns a DataFrame with start and end
    sample indices (0-based, inclusive), amplitude, displacement (deg), peak velocity (deg/s),
    and start and end positions."""
    n = len(gx)
    pos = np.column_stack([gx, gy])
    vxy = _differentiate(pos, rate)
    vel = np.hypot(vxy[:, 0], vxy[:, 1])
    axy = _differentiate(vxy, rate)
    acc = np.hypot(axy[:, 0], axy[:, 1])
    # valid samples: within the cropped recording, not within 100 ms of a NaN sample,
    # in stretches longer than 0.1 s
    bad = np.isnan(gx) | np.isnan(gy)
    pad = int(SAC_BLINK_PAD_MS * rate / 1000)
    if bad.any():
        from scipy.ndimage import binary_dilation
        bad = binary_dilation(bad, np.ones(2 * pad + 1, bool))
    t0, t1 = int(1.0 * rate), n - 1 - int(0.01 * rate)
    valid = ~bad
    valid[:t0] = False
    valid[t1 + 1:] = False
    edges = np.diff(np.r_[0, valid.astype(int), 0])
    vs, ve = np.flatnonzero(edges == 1), np.flatnonzero(edges == -1)
    for a, b in zip(vs, ve):
        if (b - a) / rate <= 0.1:
            valid[a:b] = False
    npk = int(np.ceil(valid[t0:t1 + 1].sum() / rate * SAC_RATE_OF_PEAKS))
    empty = pd.DataFrame(columns=["start", "end", "amplitude", "displacement", "peak_velocity",
                                  "x0", "y0", "x1", "y1"])
    if npk == 0:
        return empty
    pk = _find_peaks(vel[t0:t1 + 1], int(round(SAC_MIN_IPI_MS * rate / 1000)), npk) + t0
    # saccade limits: last sample under 5 deg/s before the peak, first after it
    below = np.flatnonzero(vel < SAC_LIMIT_DEG_S)   # NaN compares False, as in MATLAB
    starts, ends = np.empty(len(pk), int), np.empty(len(pk), int)
    for i, p in enumerate(pk):
        k = np.searchsorted(below, p) - 1
        if k >= 0 and below[k] >= t0:
            starts[i] = min(below[k] + 1, p - 1)
        else:
            seg = vel[t0:p]
            starts[i] = t0 + int(np.nanargmin(seg)) + 1 if np.isfinite(seg).any() else t0
        k = np.searchsorted(below, p + 1)
        if k < len(below) and below[k] <= t1:
            ends[i] = max(below[k] - 1, p + 1)
        else:
            seg = vel[p + 1:t1 + 1]
            ends[i] = p + int(np.nanargmin(seg)) if np.isfinite(seg).any() else t1
    # merge overlapping saccades (CreateYesNo)
    u = np.zeros(ends.max() + 2)
    u[starts] += 1
    u[ends] -= 1
    u = np.cumsum(u)
    starts = np.flatnonzero(np.diff(np.r_[0, u]) > 0)
    ends = np.flatnonzero(np.diff(np.r_[u, 0]) < 0)
    if len(starts) != len(ends):
        raise RuntimeError("saccade limits do not pair")
    cs = np.r_[0, np.cumsum(~valid)]
    ok = (cs[ends + 1] - cs[starts]) == 0          # FindValidSaccades
    starts, ends = starts[ok], ends[ok]
    if len(starts) < 10:
        return empty
    # properties (GetSaccadeProps) and features (GetFeatures)
    pv = np.empty(len(starts))
    pvi = np.empty(len(starts), int)
    acs = np.empty(len(starts))
    acb = np.empty(len(starts))
    amp = np.empty(len(starts))
    for i, (a, b) in enumerate(zip(starts, ends)):
        seg = vel[a:b + 1]
        j = int(np.argmax(seg))
        pv[i], pvi[i] = seg[j], j + 1                  # MATLAB 1-based index within the saccade
        acs[i] = acc[a:min(a + pvi[i], len(acc) - 1) + 1].max()
        acb[i] = acc[min(a + pvi[i], b):b + 1].max()
        amp[i] = np.hypot(np.ptp(gx[a:b + 1]), np.ptp(gy[a:b + 1]))
    disp = np.hypot(gx[ends] - gx[starts], gy[ends] - gy[starts])
    feats = []
    for f in [pv, acs, acb]:
        with np.errstate(divide="ignore"):
            lf = np.log(f)
        lf[lf == -np.inf] = lf[lf != -np.inf].min()
        feats.append((lf - lf.mean()) / lf.std(ddof=1))
    X = np.column_stack(feats)
    C = np.cov(X, rowvar=False)
    D, V = np.linalg.eigh(C)
    W = (X - X.mean(0)) @ (V * np.sqrt(1.0 / (D + 0.1)))
    X = W[:, D / D[-1] > 0.05]
    lab = _kmeans_silhouette_choice(X, pv)
    is_sac = np.zeros(len(starts), bool)
    for c in range(lab.max()):                          # every cluster but the slowest
        if disp[lab == c].mean() > SAC_MIN_DISPLACEMENT_DEG:
            is_sac[lab == c] = True
    s, e = starts[is_sac], ends[is_sac]
    return pd.DataFrame({"start": s, "end": e, "amplitude": amp[is_sac], "displacement": disp[is_sac],
                         "peak_velocity": pv[is_sac], "x0": gx[s], "y0": gy[s], "x1": gx[e], "y1": gy[e]})
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='microstim.py'; s=open(p).read()
s=s.replace("""        smax, best = s, lab
    return best""","""        smax, best = s, lab
    return best if best is not None else lab""")
open(p,'w').write(s)
EOF
cat > $TMPDIR/t_sac.py <<'EOF'
import sys, io, time, h5py, requests, numpy as np, pandas as pd
sys.path.insert(0,'.')
import microstim as ms
a = ms.list_assets()
a = a[a.path.str.contains('sub-T')].iloc[[5]]
c = requests.get(f"{ms.API}/assets/{a.asset_id.iloc[0]}/download/").content
f = h5py.File(io.BytesIO(c),'r')
print(f['session_description'][()])
g = f['acquisition/EyeTracking_m1/spatialseries/data'][:]
t = f['acquisition/t/data'][:]
print(len(g), np.isnan(g[:,0]).mean(), np.isnan(t).sum())
t0=time.time()
s = ms.detect_saccades(g[:,0]*ms.DEG_PER_PX, g[:,1]*ms.DEG_PER_PX)
print('time', time.time()-t0, 'n saccades', len(s))
print(s.describe().round(2).to_string())
# compare with fixation intervals
fx = f['intervals/m1_all']
print('fixations', len(fx['m1_start_index'][:]))
EOF
$TMPDIR/dev/bin/python $TMPDIR/t_sac.py
```

```
b'data_11042021 run_7 | subject=T | region=ACCg | roi=Eyes | condition=Social'
301592 0.058469720682246214 5077
time 0.35520482063293457 n saccades 169
           start        end  amplitude  displacement  peak_velocity      x0      y0      x1      y1
count     169.00     169.00     169.00        169.00         169.00  169.00  169.00  169.00  169.00
mean   148702.57  149658.03      23.31         16.99         808.69   61.16    9.00   61.70    8.50
std     93435.40   93455.37       9.28         11.05         196.33   15.23   11.99   14.37   13.34
min      3795.00    4264.00       7.22          0.23         575.98   22.99  -17.15   23.51  -15.21
25%     58341.00   58715.00      15.96          8.70         671.66   52.03    0.89   52.23   -1.08
50%    155611.00  156992.00      22.98         14.42         781.99   62.68    6.11   62.63    4.32
75%    237079.00  239131.00      28.80         23.40         902.00   72.48   14.02   72.58   13.75
max    300622.00  300948.00      51.19         49.95        1927.34   94.16   47.39   94.12   52.44
fixations 457
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/t_sac.py <<'EOF'
pos = np.column_stack([g[:,0], g[:,1]])*ms.DEG_PER_PX
v = ms._differentiate(pos, 1000.); vel = np.hypot(v[:,0], v[:,1])
print('velocity quantiles', np.nanpercentile(vel,[5,25,50,75,95,99]).round(1))
s0 = fx['m1_start_index'][:].astype(int)-1; e0 = fx['m1_end_index'][:].astype(int)
inf = np.concatenate([vel[a:b] for a,b in zip(s0,e0)])
print('within fixations', np.nanpercentile(inf,[5,25,50,75,95]).round(1))
print('raw step px quantiles in fixations', np.nanpercentile(np.abs(np.diff(g[s0[3]:e0[3],0])),[50,90,99]))
print(g[s0[3]:s0[3]+30,0])
EOF
$TMPDIR/dev/bin/python $TMPDIR/t_sac.py 2>&1 | tail -8
```

```
within fixations [ 15.9  40.1  67.6 106.4 196.4]
raw step px quantiles in fixations [1.60003662 4.59997559 8.        ]
[1624.59997559 1625.09997559 1623.70001221 1619.90002441 1617.09997559
 1615.40002441 1614.59997559 1613.90002441 1612.79998779 1612.40002441
 1616.79998779 1621.79998779 1625.40002441 1624.40002441 1623.29998779
 1624.79998779 1627.70001221 1630.5        1634.59997559 1637.29998779
 1632.40002441 1624.79998779 1618.40002441 1620.29998779 1622.29998779
 1622.5        1621.90002441 1623.         1624.70001221 1626.29998779]
```

**Agent calls Bash**

```bash
cd  python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']['properties']; print(list(o.keys())); print(json.dumps(o.get('data'),indent=0)[:400]); print(json.dumps(s['properties'].get('inputs'),indent=0)[:1500]); print(json.dumps(s['properties']['verifications'],indent=0)[:2500])"
```

```
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
null
{
"description": "Everything the attempt used that is not in the dataset.",
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"what",
"source"
],
"properties": {
"what": {
"type": "string",
"minLength": 1
},
"source": {
"description": "A DOI, or a repository URL with the commit read.",
"type": "string",
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.github.com/repos/changlabneuro/microstim-ofc-social-attention/git/trees/cc0bf994?recursive=1" | python -c "
import json,sys; d=json.load(sys.stdin); 
for x in d.get('tree',[]):
  p=x['path']
  if any(k in p.lower() for k in ['sacc','otero','cluster','eyemov']): print(p)
print(len(d.get('tree',[])), d.get('message'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B="https://raw.githubusercontent.com/changlabneuro/microstim-ofc-social-attention/cc0bf994"; for f in script/detect_microsaccades.m script/run_saccade_detection.m script/label_saccades.m; do echo "=== $f"; curl -s "$B/$f"; done | head -250
```

```
=== script/detect_microsaccades.m
function saccs = detect_microsaccades(pos_deg, fs, data_folder)

% this code depends on the microsaccade detection toolbox from 
% Unsupervised clustering method to detect microsaccades, Otero-Millan et 
% al. 2014, available here: http://smc.neuralcorrelate.com/sw/microsaccade-detection/

session = 'test';
    
samples = [];
samples(:, 1) = 1:size(pos_deg, 2);
samples(:, 2:3) = pos_deg';
samples(:, 4:5) = pos_deg';
blinks = any( isnan(samples), 2 );

% Loads the recording and prepares it por processing
recording = ClusterDetection.EyeMovRecording.Create( data_folder, session, samples, blinks, fs );

% Runs the saccade detection
[saccades stats] = recording.FindSaccades();
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; for r in changlabneuro/bfw nfagan/bfw; do curl -s "https://api.github.com/repos/$r" | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('full_name'), d.get('default_branch'), d.get('message'))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.github.com/repos/nfagan/bfw/commits?per_page=1" | python -c "import json,sys; d=json.load(sys.stdin); print(d[0]['sha'], d[0]['commit']['author']['date'])"; curl -s "https://api.github.com/repos/nfagan/bfw/git/trees/master?recursive=1" | python -c "
import json,sys; d=json.load(sys.stdin)
for x in d['tree']:
  if 'px2deg' in x['path'] or 'is_fixation' in x['path']: print(x['path'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://raw.githubusercontent.com/nfagan/bfw/11bb850f86d047f04e228a5405c765ae2d519764/%2Bbfw/px2deg.m"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
old_doc = s[s.index("# taken as saccades. The recording"):s.index("# Differences from the MATLAB code")]
new_doc = """# taken as saccades. The call follows the paper's own code (changlabneuro/microstim-ofc-social-
# attention at cc0bf994, script/run_saccade_detection.m and script/detect_microsaccades.m): M1's
# gaze from the first non-NaN time sample, in degrees (bfw.px2deg, the same factor as
# DEG_PER_PX), passed as both eyes, at 1 kHz, with every NaN sample marked as a blink (no
# padding); the detector then crops the first 1 s and last 10 ms of the recording
# (EyeMovRecording.GetTrials).
"""
s = s.replace(old_doc, new_doc)
s = s.replace("SAC_BLINK_PAD_MS = 100\n", "")
s = s.replace("""    # valid samples: within the cropped recording, not within 100 ms of a NaN sample,
    # in stretches longer than 0.1 s
    bad = np.isnan(gx) | np.isnan(gy)
    pad = int(SAC_BLINK_PAD_MS * rate / 1000)
    if bad.any():
        from scipy.ndimage import binary_dilation
        bad = binary_dilation(bad, np.ones(2 * pad + 1, bool))
""", """    # valid samples: within the cropped recording, not NaN, in stretches longer than 0.1 s
    bad = np.isnan(gx) | np.isnan(gy)
""")
# read_run: detect saccades in social runs
s = s.replace("""    events = pd.concat(ev, ignore_index=True)
    meta["index_time_max_err"] = float(np.max(idx_check))""", """    events = pd.concat(ev, ignore_index=True)
    meta["index_time_max_err"] = float(np.max(idx_check))

    # saccades of M1 in social runs (Otero-Millan et al. 2014, as the paper's code calls it)
    sacc = None
    if cond == "Social":
        f0 = int(np.flatnonzero(~np.isnan(t))[0])
        sacc = detect_saccades(g1[f0:, 0] * DEG_PER_PX, g1[f0:, 1] * DEG_PER_PX)
        if len(sacc):
            sacc["start"] = sacc.start.astype(int) + f0
            sacc["end"] = sacc.end.astype(int) + f0
            sacc["start_time"] = t[sacc.start.to_numpy()]
            sacc["end_time"] = t[sacc.end.to_numpy()]
            for c in ["x0", "y0", "x1", "y1"]:
                sacc[c] = sacc[c].astype(float) / DEG_PER_PX   # back to pixels""")
s = s.replace("return dict(meta=meta, trials=trials, rois=rois, events=events, pupil=pup)",
              "return dict(meta=meta, trials=trials, rois=rois, events=events, pupil=pup, saccades=sacc)")
open(p,'w').write(s)
EOF
grep -n "SAC_BLINK\|pad" microstim.py | head
```

```
415:# padding); the detector then crops the first 1 s and last 10 ms of the recording
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
s=s.replace("""                sacc[c] = sacc[c].astype(float) / DEG_PER_PX   # back to pixels""","""                sacc[c] = sacc[c].astype(float) / DEG_PER_PX   # back to pixels
            sacc = sacc.dropna(subset=["start_time", "end_time"]).reset_index(drop=True)""")
open(p,'w').write(s)
EOF
cat > $TMPDIR/t_sac2.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'.')
import microstim as ms
a = ms.list_assets()
for aid in a[a.path.str.contains('sub-T')].asset_id.iloc[[5, 40]]:
    t0=time.time(); r = ms.read_run(aid); print(r['meta']['desc'], 'time', round(time.time()-t0,2))
    s = r['saccades']
    if s is None: continue
    print(len(s), 'dur ms quantiles', np.percentile(s.end-s.start,[5,25,50,75,95]), 'amp', np.percentile(s.amplitude,[5,50,95]).round(2), 'pv', np.percentile(s.peak_velocity,[5,50,95]).round(0))
EOF
$TMPDIR/dev/bin/python $TMPDIR/t_sac2.py
```

```
data_11042021 run_7 | subject=T | region=ACCg | roi=Eyes | condition=Social time 1.05
236 dur ms quantiles [ 370.75  592.    806.5  1140.75 1794.25] amp [ 9.85 18.88 39.84] pv [ 497.  695. 1089.]
data_11082021 run_4 | subject=T | region=OFC | roi=Eyes | condition=Dot time 0.68
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; date -u; $TMPDIR/dev/bin/python -c "
import pickle, microstim as ms, time
t0=time.time()
assets = ms.list_assets()
runs = ms.load_all(assets)
pickle.dump(runs, open('$TMPDIR/runs.pkl','wb'))
print(len(runs), (time.time()-t0)/60)
"; date -u
```

```
Sun Nov  1 01:36:12 UTC 2026
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    runs = ms.load_all(assets)
  File "entries/000959-fan-2024/microstim.py", line 220, in load_all
    runs = list(ex.map(lambda a: read_run(a, sess), assets.asset_id))
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 453, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
  File "entries/000959-fan-2024/microstim.py", line 220, in <lambda>
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
old = """    for i, (a, b) in enumerate(zip(starts, ends)):
        seg = vel[a:b + 1]
        j = int(np.argmax(seg))
        pv[i], pvi[i] = seg[j], j + 1                  # MATLAB 1-based index within the saccade
        acs[i] = acc[a:min(a + pvi[i], len(acc) - 1) + 1].max()
        acb[i] = acc[min(a + pvi[i], b):b + 1].max()"""
new = """    nanmax = lambda x: np.nanmax(x) if np.isfinite(x).any() else np.nan   # MATLAB max skips NaN
    for i, (a, b) in enumerate(zip(starts, ends)):
        seg = vel[a:b + 1]
        j = int(np.nanargmax(seg)) if np.isfinite(seg).any() else 0
        pv[i], pvi[i] = seg[j], j + 1                  # MATLAB 1-based index within the saccade
        acs[i] = nanmax(acc[a:min(a + pvi[i], len(acc) - 1) + 1])
        acb[i] = nanmax(acc[min(a + pvi[i], b):b + 1])"""
assert old in s; s = s.replace(old, new)
old2 = """    disp = np.hypot(gx[ends] - gx[starts], gy[ends] - gy[starts])
"""
new2 = """    disp = np.hypot(gx[ends] - gx[starts], gy[ends] - gy[starts])
    keep = np.isfinite(pv) & np.isfinite(acs) & np.isfinite(acb)   # NaN velocity next to a gap
    starts, ends, pv, acs, acb, amp, disp = (v[keep] for v in (starts, ends, pv, acs, acb, amp, disp))
"""
assert old2 in s; s = s.replace(old2, new2)
open(p,'w').write(s)
EOF
date -u; $TMPDIR/dev/bin/python -c "
import pickle, microstim as ms, time
t0=time.time()
assets = ms.list_assets()
runs = ms.load_all(assets)
pickle.dump(runs, open('$TMPDIR/runs.pkl','wb'))
print(len(runs), (time.time()-t0)/60)
import numpy as np
s=[r['saccades'] for r in runs if r['saccades'] is not None]
print(len(s), sum(len(x) for x in s))
"; date -u
```

```
Sun Nov  1 01:36:42 UTC 2026
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    runs = ms.load_all(assets)
  File "entries/000959-fan-2024/microstim.py", line 220, in load_all
    runs = list(ex.map(lambda a: read_run(a, sess), assets.asset_id))
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 453, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
  File "entries/000959-fan-2024/microstim.py", line 220, in <lambda>
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
old = """    starts = np.flatnonzero(np.diff(np.r_[0, u]) > 0)
    ends = np.flatnonzero(np.diff(np.r_[u, 0]) < 0)
    if len(starts) != len(ends):
        raise RuntimeError("saccade limits do not pair")
"""
new = """    st2 = np.flatnonzero(np.diff(np.r_[0, u]) > 0)
    en2 = np.flatnonzero(np.diff(np.r_[u, 0]) < 0)
    merged_as_union = len(st2) != len(en2)
    if merged_as_union:   # the MATLAB code would stop here; merge overlapping intervals instead
        o = np.argsort(starts, kind="stable")
        st2, en2 = [starts[o[0]]], [ends[o[0]]]
        for a, b in zip(starts[o[1:]], ends[o[1:]]):
            if a <= en2[-1]:
                en2[-1] = max(en2[-1], b)
            else:
                st2.append(a)
                en2.append(b)
        st2, en2 = np.array(st2), np.array(en2)
    starts, ends = st2, en2
"""
assert old in s; s = s.replace(old, new)
s = s.replace("""    return pd.DataFrame({"start": s, "end": e, "amplitude": amp[is_sac], "displacement": disp[is_sac],
                         "peak_velocity": pv[is_sac], "x0": gx[s], "y0": gy[s], "x1": gx[e], "y1": gy[e]})""",
"""    out = pd.DataFrame({"start": s, "end": e, "amplitude": amp[is_sac], "displacement": disp[is_sac],
                        "peak_velocity": pv[is_sac], "x0": gx[s], "y0": gy[s], "x1": gx[e], "y1": gy[e]})
    out.attrs.update(n_peaks=len(pk), n_candidates=len(pv), n_clusters=int(lab.max() + 1),
                     merged_as_union=merged_as_union)
    return out""")
s = s.replace("""            sacc = sacc.dropna(subset=["start_time", "end_time"]).reset_index(drop=True)""",
"""            sacc = sacc.dropna(subset=["start_time", "end_time"]).reset_index(drop=True)
        meta.update({f"sacc_{k}": v for k, v in sacc.attrs.items()})""")
open(p,'w').write(s)
EOF
grep -n "attrs" microstim.py
```

```
127:                gaze_unit=_dec(f["acquisition/EyeTracking_m1/spatialseries/data"].attrs["unit"]),
128:                rate=float(f["acquisition/t/starting_time"].attrs["rate"]))
210:        meta.update({f"sacc_{k}": v for k, v in sacc.attrs.items()})
602:    out.attrs.update(n_peaks=len(pk), n_candidates=len(pv), n_clusters=int(lab.max() + 1),
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='microstim.py'; s=open(p).read()
s = s.replace("""\n        meta.update({f"sacc_{k}": v for k, v in sacc.attrs.items()})""", "")
s = s.replace("""        sacc = detect_saccades(g1[f0:, 0] * DEG_PER_PX, g1[f0:, 1] * DEG_PER_PX)
""", """        sacc = detect_saccades(g1[f0:, 0] * DEG_PER_PX, g1[f0:, 1] * DEG_PER_PX)
        meta.update({f"sacc_{k}": v for k, v in sacc.attrs.items()})
""")
open(p,'w').write(s)
EOF
date -u; $TMPDIR/dev/bin/python -c "
import pickle, microstim as ms, time
t0=time.time()
assets = ms.list_assets()
runs = ms.load_all(assets)
pickle.dump(runs, open('$TMPDIR/runs.pkl','wb'))
print(len(runs), (time.time()-t0)/60)
import numpy as np, pandas as pd
m = pd.DataFrame([r['meta'] for r in runs]); m=m[m.cond=='Social']
print(m[[c for c in m if c.startswith('sacc_')]].describe())
print('union', m.sacc_merged_as_union.sum())
s=[r['saccades'] for r in runs if r['saccades'] is not None]
print(len(s), sum(len(x) for x in s))
"; date -u
```

```
Sun Nov  1 01:37:32 UTC 2026
1705 12.470001538594564
       sacc_n_peaks  sacc_n_candidates  sacc_n_clusters
count   1179.000000        1179.000000      1179.000000
mean    1377.607294         671.108567         2.465649
std       48.768790         305.956246         0.752674
min     1044.000000         209.000000         2.000000
25%     1357.000000         402.000000         2.000000
50%     1384.000000         557.000000         2.000000
75%     1409.000000         977.000000         3.000000
max     1472.000000        1314.000000         4.000000
union 202
1179 454642
Sun Nov  1 01:50:01 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; cat > $TMPDIR/sacc_cells.py <<'PYEOF'
MD1 = '''## fig5cd-saccade-counts-unchanged

> The numbers of microsaccades and macrosaccades in the post-gaze epoch did not differ between
> microstimulation and sham trials for OFC or dmPFC.

The files hold no saccade events (data check). Saccades are detected here with a Python port of
the Otero-Millan et al. (2014) unsupervised clustering detector, from the authors' MATLAB code at
a pinned commit, called as the paper's own code calls it (`script/run_saccade_detection.m` and
`script/detect_microsaccades.m` of the paper's repository at cc0bf994): M1's gaze in degrees
from the first valid time sample, 1 kHz, NaN samples as blinks (`microstim.detect_saccades`).
This makes the claim `with_inputs` for that software, as the claims file says. A saccade is a
microsaccade when it lies strictly within an M1 fixation of the files (all M1 fixations, M1-only
and mutual), reading (a), the claims file's; reading (b) is the paper's code
(`script/label_saccades.m`): its start at least 50 samples after a fixation's start and at least
50 before its end. Counts per trial are of saccades starting in [0, 1.5) s after the trial; day
means per trial type; signed-rank over days.'''

CODE1 = '''sac = []
for k, r in enumerate(runs):
    if r["saccades"] is not None and len(r["saccades"]):
        sac.append(r["saccades"].assign(run_id=k))
sac = pd.concat(sac, ignore_index=True).merge(meta[["run_id", "date", "subject", "region", "roi", "cond"]], on="run_id")
sac["duration_ms"] = (sac.end - sac.start + 1)
sm = meta[meta.cond == "Social"]
print(f"social runs: {len(sm)}; saccades detected: {len(sac)} ({len(sac) / len(sm):.0f} per run); "
      f"velocity peaks per run, median {sm.sacc_n_peaks.median():.0f}; candidate events after limits and validity, "
      f"median {sm.sacc_n_candidates.median():.0f}; clusters chosen: {sm.sacc_n_clusters.value_counts().sort_index().to_dict()}")
print("runs where the MATLAB merge of overlapping saccades would not pair starts and ends (merged as a union here):",
      int(sm.sacc_merged_as_union.sum()), "of", len(sm))
print("saccade duration (ms) quantiles:", sac.duration_ms.quantile([0.05, 0.25, 0.5, 0.75, 0.95]).to_dict())
print("amplitude (deg) quantiles:", sac.amplitude.quantile([0.05, 0.5, 0.95]).round(2).to_dict(),
      "; peak velocity (deg/s) quantiles:", sac.peak_velocity.quantile([0.05, 0.5, 0.95]).round(0).to_dict())

# the velocity floor during fixations, against the detector's 5 deg/s saccade limit (one run)
r0 = runs[int(sm.run_id.iloc[0])]
fx0 = events[(events.run_id == sm.run_id.iloc[0]) & (events.table == "m1_all")]
print("(velocity inside fixations is shown in the next cell)")

# micro or macro: (a) strictly within an M1 fixation, (b) start at least 50 ms after a fixation's
# start and 50 ms before its end (label_saccades.m)
fixall = events[(events.who == "m1") & events.table.isin(["m1_all", "mutual_wholeface"]) & (events.cond == "Social")]
sp = ms.window_pairs(sac.assign(time=sac.start_time), fixall, -30.0, 0.0005)
sp["sac_start"] = sp.start - sp.lag
sp["sac_end"] = sac.loc[sp.trial, "end_time"].to_numpy()
in_a = sp[(sp.start < sp.sac_start) & (sp.sac_end < sp.stop)].trial.unique()
in_b = sp[(sp.sac_start - sp.start >= 0.050) & (sp.stop - sp.sac_start >= 0.050)].trial.unique()
sac["micro_a"] = sac.index.isin(in_a)
sac["micro_b"] = sac.index.isin(in_b)
print(f"microsaccades: reading (a) {int(sac.micro_a.sum())} ({sac.micro_a.mean():.3f}), "
      f"reading (b) {int(sac.micro_b.sum())} ({sac.micro_b.mean():.3f}) of {len(sac)}")

ssoc = sac[sac.roi == "Eyes"]
wp = ms.window_pairs(soc, ssoc.assign(start=ssoc.start_time), 0.0, ms.POST_GAZE_S)
sc = soc.copy()
for rd in ["a", "b"]:
    sc[f"micro_{rd}"] = sc.index.map(wp[wp[f"micro_{rd}"]].groupby("trial").size()).fillna(0)
    sc[f"macro_{rd}"] = sc.index.map(wp[~wp[f"micro_{rd}"]].groupby("trial").size()).fillna(0)
print("saccades per post-gaze epoch, means (a):", sc[["micro_a", "macro_a"]].mean().round(3).to_dict(),
      "(b):", sc[["micro_b", "macro_b"]].mean().round(3).to_dict())
rows = []
for rd in ["a", "b"]:
    for what in ["micro", "macro"]:
        for a in AREAS:
            rows.append(dict(reading=rd, saccades=what, **day_test(ms.day_means(sc, f"{what}_{rd}"), a)))
sct = pd.DataFrame(rows)
print(sct.to_string(index=False, float_format=lambda v: f"{v:.4g}"))
for rd in ["a", "b"]:
    x = sct[(sct.reading == rd) & sct.region.isin(["OFC", "dmPFC"])]
    print(f"reading ({rd}): OFC and dmPFC tests with p < 0.05: {int((x.p < 0.05).sum())} of {len(x)}")
print("by monkey, reading (a):")
rows = [dict(saccades=w, **day_test(ms.day_means(sc, f"{w}_a"), a, s)) for w in ["micro", "macro"] for a in ["OFC", "dmPFC"] for s in ["L", "T"]]
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f"{v:.4g}"))'''

CODE1b = '''# velocity during the files' fixations, against the detector's 5 deg/s saccade limit
import h5py, io
rid0 = int(sm.run_id.iloc[0])
with h5py.File(io.BytesIO(requests.get(f"{ms.API}/assets/{meta.asset_id[rid0]}/download/", timeout=300).content), "r") as f:
    g0 = f["acquisition/EyeTracking_m1/spatialseries/data"][:] * ms.DEG_PER_PX
v0 = ms._differentiate(g0, 1000.0)
vel0 = np.hypot(v0[:, 0], v0[:, 1])
fi = [(int(a), int(b)) for a, b in zip(*[np.searchsorted(runs[rid0]["trials"].time.to_numpy() * 0, 0)] * 2)] if False else None
t_run = None
ev0 = events[(events.run_id == rid0) & (events.table == "m1_all")]
print("run", meta.path[rid0])
print("velocity (deg/s) of all valid samples, quantiles:", np.nanpercentile(vel0, [5, 25, 50, 75, 95]).round(1))
print("fraction of valid samples under the 5 deg/s limit:", round(float(np.nanmean(vel0 < 5)), 4))'''
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
import os
p = os.environ['TMPDIR'] + '/sacc_cells.py'; s = open(p).read()
s = s.replace('''
# the velocity floor during fixations, against the detector's 5 deg/s saccade limit (one run)
r0 = runs[int(sm.run_id.iloc[0])]
fx0 = events[(events.run_id == sm.run_id.iloc[0]) & (events.table == "m1_all")]
print("(velocity inside fixations is shown in the next cell)")
''', '')
i = s.index("CODE1b = '''")
s = s[:i] + """CODE1b = '''# the detector's velocity on one social run, during the files' fixations, against its 5 deg/s
# limit for the start and end of a saccade
import io
import h5py
rid0 = int(sm.run_id.iloc[0])
with h5py.File(io.BytesIO(requests.get(f"{ms.API}/assets/{meta.asset_id[rid0]}/download/", timeout=300).content), "r") as f:
    g0 = f["acquisition/EyeTracking_m1/spatialseries/data"][:] * ms.DEG_PER_PX
    t0_ = f["acquisition/t/data"][:]
v0 = ms._differentiate(g0, 1000.0)
vel0 = np.hypot(v0[:, 0], v0[:, 1])
ev0 = events[(events.run_id == rid0) & (events.table == "m1_all")]
ok_t = ~np.isnan(t0_)
idx = np.flatnonzero(ok_t)
a0 = idx[np.searchsorted(t0_[ok_t], ev0.start.to_numpy())]
b0 = idx[np.minimum(np.searchsorted(t0_[ok_t], ev0.stop.to_numpy()), ok_t.sum() - 1)]
infix = np.concatenate([vel0[a:b] for a, b in zip(a0, b0)])
print("run", meta.path[rid0], "; fixations", len(ev0))
print("velocity (deg/s) inside fixations, quantiles 5/25/50/75/95%:", np.nanpercentile(infix, [5, 25, 50, 75, 95]).round(1),
      "; fraction under 5 deg/s:", round(float(np.nanmean(infix < 5)), 4))
print("velocity (deg/s) of all samples, median:", round(float(np.nanmedian(vel0)), 1),
      "; fraction under 5 deg/s:", round(float(np.nanmean(vel0 < 5)), 4))'''
"""
open(p,'w').write(s)
EOF
echo
```

```
(Bash completed with no output)
```

**Agent**

Now the kinematics cell.

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; cat >> $TMPDIR/sacc_cells.py <<'PYEOF'

MD2 = '''## fig5e-h-saccade-kinematics-unchanged

> Microstimulations of OFC or dmPFC did not change macrosaccade peak velocity, the slope of peak
> velocity on amplitude, or that slope by saccade direction.

The first macrosaccade starting in the post-gaze epoch of each trial (both readings of the
macrosaccade). Day mean peak velocity per trial type, signed-rank. Per day, a least-squares
line of peak velocity on amplitude for stimulation and for sham trials (at least 3 saccades
each), the slope difference tested against zero by signed-rank; the permutation test shuffles
the trial labels 1,000 times within each day, takes the median slope difference over days for
each shuffle, and gives the fraction of shuffled medians beyond the real median, on its side.
Direction groups II, IC, CI and CC by the hemifields of the start and end positions (against the
centre of `roi_m2_face`), slope difference against zero per group. Seed 5 (a standard choice).'''

CODE2 = '''def slope(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or np.ptp(x) == 0:
        return np.nan
    return np.polyfit(x, y, 1)[0]


def hemi_of(x, m2x, subject):
    right = x > m2x
    return np.where((subject == "T") == right, "I", "C")


rng_k = np.random.default_rng(5)
kin_rows, perm_rows, dir_rows = [], [], []
for rd in ["a", "b"]:
    mac = wp[~wp[f"micro_{rd}"]].sort_values(["trial", "lag"]).drop_duplicates("trial")
    fm = soc.loc[mac.trial, ["date", "region", "subject", "type", "m2face_x"]].assign(
        pv=mac.peak_velocity.to_numpy(), amp=mac.amplitude.to_numpy(),
        d=[a + b for a, b in zip(hemi_of(mac.x0.to_numpy(), soc.loc[mac.trial, "m2face_x"].to_numpy(), soc.loc[mac.trial, "subject"].to_numpy()),
                                 hemi_of(mac.x1.to_numpy(), soc.loc[mac.trial, "m2face_x"].to_numpy(), soc.loc[mac.trial, "subject"].to_numpy()))])
    print(f"reading ({rd}): trials with a first macrosaccade {len(fm)} of {len(soc)}; direction groups {fm.d.value_counts().to_dict()}")
    for a in AREAS:
        kin_rows.append(dict(reading=rd, test="peak velocity", **day_test(ms.day_means(fm, "pv"), a)))
    sd = []
    for (date, region, subject), g in fm.groupby(["date", "region", "subject"]):
        s1, s0 = slope(g[g.type == "stim"].amp, g[g.type == "stim"].pv), slope(g[g.type == "sham"].amp, g[g.type == "sham"].pv)
        null = []
        lab = g.type.to_numpy()
        for _ in range(1000):
            pl = rng_k.permutation(lab)
            null.append(slope(g.amp[pl == "stim"], g.pv[pl == "stim"]) - slope(g.amp[pl == "sham"], g.pv[pl == "sham"]))
        sd.append(dict(date=date, region=region, subject=subject, diff=s1 - s0, null=np.array(null)))
        for dg, gg in g.groupby("d"):
            dir_rows.append(dict(reading=rd, date=date, region=region, group=dg,
                                 diff=slope(gg[gg.type == "stim"].amp, gg[gg.type == "stim"].pv) - slope(gg[gg.type == "sham"].amp, gg[gg.type == "sham"].pv)))
    sd = pd.DataFrame(sd)
    for a in AREAS:
        x = sd[(sd.region == a) & sd["diff"].notna()]
        n, p = signrank(x["diff"])
        kin_rows.append(dict(reading=rd, test="slope difference against zero", region=a, subject="both", n=n,
                             median_diff=np.median(x["diff"]), mean_diff=np.mean(x["diff"]), p=p))
        real = np.median(x["diff"])
        nullm = np.nanmedian(np.vstack(x.null.to_numpy()), axis=0)
        pp = np.mean(nullm >= real) if real >= 0 else np.mean(nullm <= real)
        kin_rows.append(dict(reading=rd, test="slope difference, permutation", region=a, subject="both", n=len(x),
                             median_diff=real, mean_diff=np.nan, p=pp))
kin = pd.DataFrame(kin_rows)
print(kin.to_string(index=False, float_format=lambda v: f"{v:.4g}"))
dr = pd.DataFrame(dir_rows).dropna(subset=["diff"])
dtab = pd.DataFrame([dict(reading=rd, region=a, group=gname, n=signrank(g["diff"])[0], median_diff=np.median(g["diff"]), p=signrank(g["diff"])[1])
                     for (rd, a, gname), g in dr.groupby(["reading", "region", "group"])])
print("\\nslope difference by direction group, against zero:")
print(dtab.to_string(index=False, float_format=lambda v: f"{v:.4g}"))
for rd in ["a", "b"]:
    x = pd.concat([kin[(kin.reading == rd) & kin.region.isin(["OFC", "dmPFC"])].p,
                   dtab[(dtab.reading == rd) & dtab.region.isin(["OFC", "dmPFC"])].p])
    print(f"reading ({rd}): OFC and dmPFC tests with p < 0.05: {int((x < 0.05).sum())} of {len(x)}")'''
PYEOF
python - <<'EOF'
import os
exec(open(os.environ['TMPDIR'] + '/sacc_cells.py').read())
for c in [CODE1, CODE1b, CODE2]: compile(c, 'x', 'exec')
print('ok')
EOF
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; cat > $TMPDIR/e5.py <<'EOF'
import os, uuid
exec(open(os.environ['TMPDIR'] + '/nbedit.py').read())
exec(open(os.environ['TMPDIR'] + '/sacc_cells.py').read())
s = src(93)
s = s[:s.index('\n\n## Saccade claims')]
setsrc(93, s)
assert src(100).startswith('## Summary')
def cell(kind, text, tag=None):
    c = {"cell_type": kind, "id": uuid.uuid4().hex[:8], "metadata": {}, "source": text.splitlines(keepends=True)}
    if tag: c["metadata"]["tags"] = [tag]
    if kind == "code": c.update(execution_count=None, outputs=[])
    return c
new = [cell("markdown", MD1), cell("code", CODE1, "claim:fig5cd-saccade-counts-unchanged"),
       cell("code", CODE1b, "claim:fig5cd-saccade-counts-unchanged"), cell("markdown", "**Result: TBD.**"),
       cell("markdown", MD2), cell("code", CODE2, "claim:fig5e-h-saccade-kinematics-unchanged"), cell("markdown", "**Result: TBD.**")]
nb['cells'][100:100] = new
save()
EOF
$TMPDIR/dev/bin/python $TMPDIR/e5.py; date -u; $TMPDIR/dev/bin/python $TMPDIR/run_nb.py 101,102,105 92,98,60,27 2>&1 | grep -v "^cell \|Warning\|escape\|Scale\|Standard"; date -u
```

```
Sun Nov  1 01:51:17 UTC 2026
===== cell 101 (4.1s)
social runs: 1179; saccades detected: 454642 (386 per run); velocity peaks per run, median 1384; candidate events after limits and validity, median 557; clusters chosen: {2.0: 817, 3.0: 175, 4.0: 187}
runs where the MATLAB merge of overlapping saccades would not pair starts and ends (merged as a union here): 202 of 1179
saccade duration (ms) quantiles: {0.05: 41.0, 0.25: 77.0, 0.5: 147.0, 0.75: 383.0, 0.95: 1062.0}
amplitude (deg) quantiles: {0.05: 3.02, 0.5: 13.71, 0.95: 34.58} ; peak velocity (deg/s) quantiles: {0.05: 274.0, 0.5: 620.0, 0.95: 1150.0}
microsaccades: reading (a) 79753 (0.175), reading (b) 257222 (0.566) of 454642
saccades per post-gaze epoch, means (a): {'micro_a': 0.516, 'macro_a': 1.968} (b): {'micro_b': 1.275, 'macro_b': 1.208}
reading saccades region subject  n  median_diff  mean_diff        p
      a    micro    OFC    both 27      0.01739    0.02366  0.06923
      a    micro  dmPFC    both 27   -0.0001139   -0.00283   0.8889
      a    micro   ACCg    both 27      0.03018    0.08268 0.008889
      a    macro    OFC    both 27      -0.0694   -0.06774  0.04356
      a    macro  dmPFC    both 27     -0.03392   -0.04047   0.2386
      a    macro   ACCg    both 27        -0.05   -0.09441 0.003878
      b    micro    OFC    both 27     0.007194   -0.01335   0.7317
      b    micro  dmPFC    both 27     -0.06384   -0.03284   0.1482
      b    micro   ACCg    both 27      0.03465    0.03891   0.2792
      b    macro    OFC    both 27     0.007895   -0.03073   0.6938
      b    macro  dmPFC    both 27    -0.007204   -0.01046   0.9341
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python -c "
import json;nb=json.load(open('reproduce_fan_2024.ipynb'))
for i in [18,21,23,28,66,94]: print('=== cell',i); print(''.join(nb['cells'][i]['source']))"
```

```
=== cell 18
## figs1e-eyes-more-than-face and figs1e-eyes-vs-rdm-comparable

> The stimulated monkeys made significantly more fixations per day on the partner's Eyes than on
> the non-eye Face, for days of all three stimulated areas.

> The number of fixations on the partner's Eyes per day was comparable to the number of
> fixations on the RDM stimulus, for days of all three areas.

Day counts under the claims' readings (a) the day's total and (b) the mean per run. The events
counted: M1's fixations in the ROI, the M1-only events plus the M1 side of mutual events (the
Methods' "total number of gaze fixations ... of the stimulated monkey"), with M1-only events as
the variant (the code's event tables). RDM fixations are the M1 events labelled Eyes in the Dot
runs (the RDM ROI is the Eyes ROI's location and size). FDR over the 15 tests of the claims file.
=== cell 21
**Result: reproduced.** Under both day counts and both event sets, Eyes fixations exceed non-eye Face fixations for every area, with corrected p at most 4.4e-05, below 10^-4 (median day totals of 384 to 408 Eyes against 129 to 177 non-eye Face fixations).
=== cell 23
**Result: not reproduced.** Under the paper's reading (a), the day's total, Eyes fixations exceed RDM fixations for every area (corrected p = 0.00036, 0.000025 and 0.00041 for OFC, dmPFC and ACCg; median differences of 177 to 241 fixations per day), since a day holds about twice as many social runs as control runs. Under the code's reading (b), the mean per run, the counts are comparable (corrected p = 0.40, 0.40 and 0.52), as the paper reports.
=== cell 28
**Result: reproduced.** The day-averaged OFC stimulation minus sham density summed over the whole Face is positive under both normalisations (7.47 z-scored, 0.0093 by total), and so is the sum over the Eyes (3.71 and 0.0046); it is positive in each monkey under each. The dmPFC and ACCg sums over the whole Face are negative under both. 10,771 of 53,542 post-gaze fixations lie outside the 40-
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; $TMPDIR/dev/bin/python $TMPDIR/run_nb.py 19,25,30,37 92,98,60,27,102,105,101,95 40 2>&1 | grep -v "^cell \|Warning\|escape\|Scale\|Standard"
```

```
===== cell 19 (2.0s)
fixations per day (reading a, the day's total), M1 and mutual events:
         Eyes neFace    RDM
          sum    sum    sum
region                     
ACCg    382.0  171.0  180.0
OFC     384.0  179.0  211.0
dmPFC   408.0  134.0  177.0

===== cell 25 (1.7s)
social trials with no fixation in [0, 1.5) s: 1270 of 19474
trials per day and type, quantiles: {0.0: 50.0, 0.5: 123.5, 1.0: 170.0}
trial distance (pixels) range: 1.7 1494.1

===== cell 30 (0.0s)
fixations: methods
region subject  n  median_diff  mean_diff         p  median_diff_deg
   OFC    both 27       -17.87     -23.73 0.0002089          -0.7032
   OFC       L 15       -22.43     -27.46  0.006714          -0.8827
   OFC       T 12       -14.02     -19.07   0.01611          -0.5518
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; cat > $TMPDIR/e6.py <<'EOF'
import os
exec(open(os.environ['TMPDIR'] + '/nbedit.py').read())
def find(prefix):
    idx = [i for i, c in enumerate(nb['cells']) if src(i).startswith(prefix)]
    assert len(idx) == 1, (prefix, idx); return idx[0]
rep(18, '''RDM fixations are the M1 events labelled Eyes in the Dot
runs''', '''The non-eye Face is the files' `m1_neface` table, which includes the Mouth, plus
`mutual_face` and `mutual_mouth` for mutual events (`mutual_face` is the face outside the Eyes and
the Mouth; data check). RDM fixations are the M1 events labelled Eyes in the Dot
runs''')
setsrc(21, '''**Result: reproduced.** Under both day counts and both event sets, Eyes fixations exceed non-eye Face fixations for every area, with corrected p at most 3.1e-05, below 10^-4 (median day totals of 382 to 408 Eyes against 134 to 179 non-eye Face fixations).''')
setsrc(23, '''**Result: not reproduced.** Under the paper's reading (a), the day's total, Eyes fixations exceed RDM fixations for every area (corrected p = 0.00036, 0.000025 and 0.00041 for OFC, dmPFC and ACCg; median differences of 177 to 241 fixations per day), since a day holds about twice as many social runs as control runs. Under the code's reading (b), the mean per run, the counts are comparable (corrected p = 0.40, 0.40 and 0.52), as the paper reports. Whether the claims file's choice of reading (a) as the deciding one misreads the paper is asked of a reader (`questions/000959.yaml`); the outcome is judged on the claims file as it stands.''')
setsrc(28, '''**Result: reproduced.** The day-averaged OFC stimulation minus sham density summed over the whole Face is positive under both normalisations (7.47 z-scored, 0.0093 by total), and so is the sum over the Eyes (3.71 and 0.0046); it is positive in each monkey under each. The dmPFC and ACCg sums over the whole Face are negative under both. 10,771 of 53,542 post-gaze fixations lie outside the 40-degree grid. The three recalibrated days, whose ROI squares are now the intersection over their runs, are dmPFC and ACCg days, so the OFC sums do not depend on them.''')
setsrc(61, '''**Result: not reproduced.** With the Methods fixations, the bootstrap medians of the OFC Eyes effects for contralateral fixations are not significantly below the Mouth median using all Eyes days (p = 0.078 one-sided, 0.156 two-sided; 0.059 to 0.070 one-sided over five other seeds), while for both hemifields combined the one-sided p is 0.043, where the paper finds no difference. With monkey T's Eyes days the contralateral p is 0.037 one-sided (0.074 two-sided) and the combined p is also 0.037. The ipsilateral p values are 0.30 and 0.35. With the code's M1-only fixations, the contralateral p is 0.049 one-sided (0.040 to 0.049 over five other seeds) and 0.006 with monkey T's days, closer to the paper's 0.009 and 0.005, but both hemifields combined gives 0.050 (all days) and 0.036 (monkey T), and the paper's pattern needs the combined p not below 0.05 for both. Neither reading, nor either fixation set, gives the paper's pattern.''')
setsrc(96, '''**Result: partially reproduced.** The duration of the Eyes event in progress at the trial does not differ for OFC (p = 0.61 with mutual events, 0.36 without), as the paper reports, but for dmPFC it is longer on stimulation trials (median day difference 31 ms, p = 0.019; 28 ms, p = 0.028 without mutual events), where the paper reports p = 0.269. The 5,695 trials with no Eyes event in progress (29%) are spread evenly over areas and trial types (27.3% to 30.1%; stimulation minus sham per day, dmPFC p = 0.069, OFC 0.58); 4,227 of them fall inside another M1 fixation, mostly outside the face or on the non-eye face, and 609 have an Eyes event starting within 20 ms after the trial. Counting those 609 as the trigger leaves the result unchanged (dmPFC p = 0.020, OFC 0.58).''')
rep(94, '''Readings: (a) M1-only and mutual Eyes events, (b) M1-only.''', '''Readings: (a) M1-only and mutual Eyes events, (b) M1-only. The trials with no Eyes event in
progress are broken down by area and trial type, and a variant counts an Eyes event that starts
within 20 ms after the trial as the trigger.''')
save()
EOF
$TMPDIR/dev/bin/python $TMPDIR/e6.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; cat > $TMPDIR/e7.py <<'EOF'
import os
exec(open(os.environ['TMPDIR'] + '/nbedit.py').read())
assert src(103).startswith('**Result: TBD') and src(106).startswith('**Result: TBD') and src(107).startswith('## Summary')
setsrc(103, '''**Result: partially reproduced.** With the claims file's reading (a), a microsaccade lying strictly within an M1 fixation, microsaccade counts do not change for OFC (p = 0.069) or dmPFC (p = 0.89), and macrosaccade counts do not change for dmPFC (p = 0.24), but OFC stimulation trials have fewer macrosaccades (median day difference -0.069 per epoch, p = 0.044; paper 0.055, also the closest to significance of its four tests). With the code's reading (b), none of the four tests gives p < 0.05 (smallest 0.15). The detector, run as the paper's code calls it, finds 386 saccades per run with a median duration of 147 ms (95th percentile 1,062 ms): on these data the gaze velocity inside fixations has a median of about 20 deg/s and is under the detector's 5 deg/s saccade limit for only about 5% of samples, so many detected saccades extend over several fixations. In 202 of the 1,179 social runs the MATLAB code's merge of overlapping saccades would not pair starts and ends; they are merged as a union here.''')
setsrc(106, '''**Result: reproduced.** With reading (a) of the macrosaccade, none of the 14 OFC and dmPFC tests gives p < 0.05: peak velocity OFC p = 0.052 and dmPFC 0.88 (paper 0.848 and 1), slope difference against zero 0.70 and 0.59 (paper 0.665, 0.904), permutation 0.28 and 0.19 (paper 0.515, 0.164), and by direction group the smallest is 0.071 (OFC CI). With the code's reading (b), 3 of the 14 do (dmPFC slope difference 0.030, OFC IC 0.048, dmPFC CC 0.037), so the result depends on how microsaccades are told from macrosaccades; ACCg, outside the claim, gives p below 0.05 for two direction groups under (a).''')
rep(0, '''| fig5cd-saccade-counts-unchanged, fig5e-h-saccade-kinematics-unchanged | blocked, not_runnable (saccade detection by MATLAB code not in the dataset) |''',
'''| fig5cd-saccade-counts-unchanged, fig5e-h-saccade-kinematics-unchanged | tested, with outside software (a Python port of the Otero-Millan et al. 2014 saccade detector, pinned; the dataset holds no saccades) |''')
s = src(107)
s = s.replace('''| fig5a-trigger-duration-unchanged | not reproduced |
| fig5b-pupil-unchanged | reproduced |
| fig5cd-saccade-counts-unchanged, fig5e-h-saccade-kinematics-unchanged | blocked, not_runnable |''', '''| fig5a-trigger-duration-unchanged | partially reproduced |
| fig5b-pupil-unchanged | reproduced |
| fig5cd-saccade-counts-unchanged (with outside software) | partially reproduced |
| fig5e-h-saccade-kinematics-unchanged (with outside software) | reproduced |''')
s = s.replace('''The causal decomposition and the saccade detection were not run.''', '''The causal decomposition was not run (its cost is timed in the notebook). Saccades were detected
with a Python port of the Otero-Millan et al. (2014) detector, called as the paper's code calls
it; the port uses scipy's k-means, and in 202 social runs merges overlapping saccades as a union
where the MATLAB code would stop.''')
s = s.replace('''Neither the files nor the paper give the padding of the Eyes ROI.''', '''Neither the files nor the paper give the padding of the Eyes ROI. The files hold no saccade
events. `mutual_face` is the face outside the Eyes and the Mouth while `m1_neface` includes the
Mouth; the table descriptions do not say so.''')
setsrc(107, s)
save()
EOF
$TMPDIR/dev/bin/python $TMPDIR/e7.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py check entries/000959-fan-2024 2>&1 | tail -15
```

```
Sun Nov  1 01:53:57 UTC 2026
0 error(s)
```

**Agent calls Bash**

```bash
cd  date -u; timeout 7000 python tools/entry.py all entries/000959-fan-2024 2>&1 | tail -20; date -u
```

```
Sun Nov  1 01:54:02 UTC 2026
Installed kernelspec registry-000959-fan-2024 in executed/000959-fan-2024/.venv/share/jupyter/kernels/registry-000959-fan-2024
0 error(s)
pass  reproduce_fan_2024.ipynb  (874 s)
Sun Nov  1 02:08:45 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls executed/000959-fan-2024/; python - <<'EOF'
import json
nb = json.load(open('executed/000959-fan-2024/reproduce_fan_2024.ipynb'))
for i in [3, 10, 19, 20, 22, 27, 60, 92, 95, 101, 102, 105, 108]:
    c = nb['cells'][i]
    out = ''.join(''.join(o.get('text', '')) for o in c.get('outputs', []) if o.get('output_type') == 'stream')
    errs = [o for o in c.get('outputs', []) if o.get('output_type') == 'error']
    print(f'=== {i}', 'ERROR' if errs else '')
    print(out[-3500:] if i in (3,) else out)
EOF
```

```
reproduce_fan_2024.ipynb
result.json
=== 3 
     OFC      92     150
              dmPFC    88     150
T       Eyes  ACCg     60     168
              OFC      60     168
              dmPFC    60     168
        Mouth ACCg     25      75
              OFC      25      75
              dmPFC    25      75

days by subject, triggering ROI and region:
region         ACCg  OFC  dmPFC
subject roi                    
L       Eyes     15   15     15
T       Eyes     12   12     12
        Mouth     5    5      5
days with more than one region: 0
runs sharing sample count and time span: 0 ; runs sharing all trial times: 0 ; identifiers shared by a Social and a Dot run (run numbers restart per condition): 526 ; (date, condition, run) repeated: 0
[... 328 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 questions/000005.yaml; cat entries/000959-fan-2024/README.md
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
    to exc-vm-touch-whisking.
  passage: Touch latency was identified as the latency from touch onset to the time when dVm/dt
    crossed baseline (3x s.d. of the dVm/dt between 0 and 25 ms before touch). All touch-spike PSTHs
    were constructed with a bin size of 1 ms. (Online Methods, Data analysis)
  why: At the full sampling rate two of the five whole-cell FS cells cross the threshold at 0.0 and
    0.3 ms and the mean latency is 1.88 ms (not reproduced); in 1 ms bins the mean over three cells
    is 3.67 to 4.17 ms (within 4.0 +- 0.4). For the thalamic and cortical light the full rate gives
    0.1 ms for both, the 1 ms bins 5.0 and 2.0 ms.
  answer: >-
    The recording's sampling rate, not 1 ms bins. The Methods give 1 ms bins for spike PSTHs
    only ("All touch-spike PSTHs were constructed with a bin size of 1 ms"), and the paper's Vm
    latencies are not on a 1 ms grid. The FS onset has "median, 4.2 ms, n = 7 neurons" and the E
[... 54 more lines not kept]
```

**Agent**

Now the questions file, README and entry.yaml.

**Agent calls Bash**

```bash
cd  grep -n "Figure S1\|S1E\|per day was comparable" paper/10.1016-j.neuron.2024.05.004.txt | head; grep -n -i "total number of gaze fixations" paper/10.1016-j.neuron.2024.05.004.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat > questions/000959.yaml <<'EOF'
dandiset: "000959"
paper: doi:10.1016/j.neuron.2024.05.004
questions:
- claim: figs1e-eyes-vs-rdm-comparable
  asked: 2026-11-01
  question: The criterion decides the outcome on reading (a), the day's total number of fixations,
    and shows reading (b), the mean per session (the paper's code), as a variant. Does the paper's
    "all p > 0.30" for Eyes against RDM fit reading (a)? A day holds 10 to 15 live social gaze
    sessions but about 5 control sessions, so day totals of Eyes fixations (social sessions) and
    RDM fixations (control sessions) differ by the number of sessions alone. Should the deciding
    reading be (b), the mean per session, or should the claim say that the comparison is judged on
    totals regardless?
  passage: In addition, the total number of fixations on partner's Eyes per day was comparable to
    fixations on the RDM stimulus for days involving the three stimulated regions (Fig. S1E, top, all
    p > 0.30) (Results, opening section, paragraph 2); For each of the ROIs, we calculated the total
    number of gaze fixations and the average duration per fixation of the stimulated monkey for each
    day. Wilcoxon signed rank test was used to compare each variable between Eyes and non-eye Face,
    as well as Eyes and RDM stimulus. (STAR Methods, Frequency of microstimulations and regions of
    interest); Each data collection day consisted of a total of alternating 10 live social gaze
    sessions and 5 non-social control sessions on average for monkey L ... and alternating 15 live
    social gaze sessions and 5 non-social control sessions on average for monkey T (STAR Methods,
    Experimental setup)
  why: The verifier of round 1 reports this as a misreading of the paper by the claims file. Under
    reading (a) Eyes fixations exceed RDM fixations for every area (corrected p 0.00036, 0.000025 and
    0.00041; median differences 177 to 241 per day), so the claim is not reproduced; under reading
    (b) the corrected p are 0.40, 0.40 and 0.52, all above 0.30 as the paper reports, so it would be
    reproduced. The numbers of sessions per day make reading (a) unable to give comparable counts
    unless per-session rates differ by about a factor of two.
EOF
python -c "import yaml; yaml.safe_load(open('questions/000959.yaml')); print('ok')"
```

```
ok
```

**Agent calls Bash**

```bash
cd  grep -rn "questions/" tools/*.py | head -5; ls schemas
```

```
tools/datasets.py:9:files in the repository (claims/, questions/, transcripts/, attempt branches, the paper store) are
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent**

Now README and entry.yaml.

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='README.md'; s=open(p).read()
s=s.replace("| Eyes fixations comparable to RDM fixations | Not reproduced under the Methods' day total; comparable under the code's mean per run |",
"| Eyes fixations comparable to RDM fixations | Not reproduced under the Methods' day total; comparable under the code's mean per run (asked of a reader) |")
s=s.replace("| Trigger fixation duration unchanged | Not reproduced (dmPFC p = 0.019) |",
"| Trigger fixation duration unchanged | Partially reproduced (OFC unchanged; dmPFC p = 0.019) |")
s=s.replace("| Saccade counts and kinematics (two claims) | Blocked: not runnable (MATLAB detection, no saccades in the files) |",
"| Saccade counts unchanged (with outside software) | Partially reproduced (OFC macrosaccades p = 0.044, paper 0.055) |\n| Saccade kinematics unchanged (with outside software) | Reproduced |")
s=s.replace("""and holds the measures.""", """and holds the measures, including a Python port of the Otero-Millan et al. (2014) saccade
detector (github.com/ocular-motor-lab/otero-millan_et_al_microsaccade_detection at ce2c10dc), called
as the paper's own code calls it; the files hold no saccade events, so the two saccade claims use
that outside software.""")
open(p,'w').write(s)
p='entry.yaml'; s=open(p).read()
s=s.replace("""and the trial counts between microstimulation and sham trials. The causal
  decomposition and the saccade analyses are not run.""","""and the trial counts between microstimulation and sham trials, and detects saccades with a port of
  the Otero-Millan et al. (2014) detector to test their counts and kinematics. The causal
  decomposition is not run; its cost is timed.""")
s=s.replace("runtime_minutes: 12","runtime_minutes: 15")
open(p,'w').write(s)
EOF
grep -n "pressure\|description" entry.yaml; sed -n 1,12p entry.yaml
```

```
5:description: Tests the findings of Fan, Dal Monte, Nair, Fagan and Chang (2024) on dandiset 000959,
schema_version: 1
name: 000959-fan-2024
type: reproduction
title: Closed-loop OFC microstimulation and dynamic social attention (Fan et al. 2024)
description: Tests the findings of Fan, Dal Monte, Nair, Fagan and Chang (2024) on dandiset 000959,
  which holds the gaze, pupil, fixation events and stimulation times of every run of the 81 Eyes and
  15 Mouth stimulation days of two stimulated monkeys. It compares social gaze distance, its
  hemifield split, inter-looking interval, reciprocation latency, the partner's gaze, fixation counts
  and durations, pupil size and the trial counts between microstimulation and sham trials, and detects saccades with a port of
  the Otero-Millan et al. (2014) detector to test their counts and kinematics. The causal
  decomposition is not run; its cost is timed.
license: Apache-2.0
```

**Agent calls Bash**

```bash
cd  grep -n "verif" tools/entry.py | head -40
```

```
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
31:`handover` builds what a verifier is given in its first round
279:        for rnd in (attempt.get("verifications") or [])[1:]:
295:            verified = agreed.get(outcome.get("claim"))
296:            if verified and outcome.get("outcome") != verified:
298:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
299:                                    "and verify it in another round")
387:    """The notebook without the author's conclusions, for a verifier's first round."""
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec1.py <<'PYEOF'
p = 'attempts/000959-fan-2024-01.yaml'
s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)

rep("""  notes: Under both day counts (a, total; b, mean per run) and both event sets (M1-only and mutual,
    M1-only), Eyes fixations exceed non-eye Face fixations for every area, corrected p from 1.1e-07 to
    4.4e-05, all below 1e-4. Median day totals are 384 to 408 Eyes and 129 to 177 non-eye Face
    fixations.""", """  notes: Under both day counts (a, total; b, mean per run) and both event sets (M1-only and mutual,
    M1-only), Eyes fixations exceed non-eye Face fixations for every area, corrected p from 1.1e-07 to
    3.1e-05, all below 1e-4. Median day totals are 382 to 408 Eyes and 134 to 179 non-eye Face
    fixations.""")
rep("""  - The non-eye Face is the files' m1_neface table (with mutual_face for mutual events); the
    notebook shows that m1_wholeface equals m1_eye plus m1_neface in every run.""", """  - The non-eye Face is the files' m1_neface table, which includes the Mouth, with mutual_face and
    mutual_mouth for mutual events (mutual_face is the face outside the Eyes and the Mouth; the
    notebook shows that m1_wholeface equals m1_eye plus m1_neface and that mutual_wholeface equals
    mutual_eye plus mutual_face plus mutual_mouth).""")
rep("""    reports; M1-only events give the same pattern under both readings.
  deviations:""", """    reports; M1-only events give the same pattern under both readings. Whether the claims file's
    deciding reading (a) misreads the paper, given about twice as many social runs as control runs
    per day, is asked of a reader in questions/000959.yaml; the outcome is judged on the claims file
    as it stands.
  deviations:""")
rep("""    run's Eyes ROI centre, and the ROI squares are those whose centres lie in the day's ROI
    rectangle, a standard choice; pixels are converted with 27 cm at 50 cm over 768 pixels (claims
    file, opening comment).""", """    run's Eyes ROI centre, and the ROI squares are those whose centres lie in the ROI rectangle,
    relative to the Eyes centre, of every social run of the day, a standard choice; the three
    recalibrated days, which have two ROI sets, are dmPFC and ACCg days. Pixels are converted with
    27 cm at 50 cm over 768 pixels (claims file, opening comment).""")
rep("""    significant, the reverse of the paper's pattern.
  deviations:
  - Seed 959 is a standard choice; five other seeds are shown.""", """    significant, the reverse of the paper's pattern. With the code's M1-only fixations, contralateral
    p = 0.049 (a) with all days (0.040 to 0.049 over five other seeds) and 0.006 with monkey T's days,
    ipsilateral 0.30 and 0.35, but both hemifields 0.050 and 0.036, so that fixation set does not give
    the paper's pattern either.
  deviations:
  - Seed 959 is a standard choice; five other seeds are shown.""")

old_cd = s[s.index("- claim: figs4a-causal-strength-no-stim-effect"):s.index("- claim: figs4b-causal-strength-no-epoch-effect")]
new_cd = """- claim: figs4a-causal-strength-no-stim-effect
  outcome: blocked
  blocked_by: too_large
  notebook: reproduce_fan_2024.ipynb
  output: claim:figs4a-causal-strength-no-stim-effect
  notes: The relative causal strength needs the causal decomposition of Yang, Peng and Huang (2018),
    whose code runs 2 + 2 x (number of IMFs) ensemble EMDs per trial, each with 10 fixed sifts per
    IMF. Neither the noise level nor the ensemble size has a default in that code, and its example
    uses 1,000 ensembles, as does the claims file's reading (a), so both readings cost the same. One
    EEMD of one 150-bin series with 1,000 ensembles takes 18.3 s on one core with PyEMD (9.2 s on four
    processes) and yields 7 IMFs, so a trial takes about 293 CPU s, and the 19,474 social Eyes trials
    about 1,590 CPU hours (about 790 hours of wall time on four processes). A compiled implementation
    at 10 microseconds per cubic-spline envelope would still need about 104 CPU hours. The notebook
    limit is one hour. The trials, distances and epochs the analysis would use are all in the
    dataset.
"""
s = s.replace(old_cd, new_cd)
rep("""- claim: ofc-slope-unchanged-by-epoch
  outcome: blocked
  blocked_by: too_large
  notes: Depends on figs4a-causal-strength-no-stim-effect, blocked by the cost of the causal
    decomposition.""", """- claim: ofc-slope-unchanged-by-epoch
  outcome: blocked
  blocked_by: too_large
  notes: Depends on figs4a-causal-strength-no-stim-effect, blocked by the cost of the causal
    decomposition. This claim needs only the first 90 stimulation trials of the 25 OFC epoch days,
    2,250 trials, which the notebook times at about 183 CPU hours (92 hours of wall time on four
    processes; about 12 CPU hours even at 10 microseconds per spline envelope), beyond the one-hour
    notebook limit.""")
for c in ["fig4c-dmpfc-slope-late-greater", "fig4d-dmpfc-slope-permutation", "dmpfc-slope-positive"]:
    i = s.index(f"- claim: {c}\n")
    j = s.index("\n- claim:", i + 5)
    block = s[i:j]
    nb = block.rstrip() + """ The 2,250 stimulation trials of the 25 dmPFC epoch days alone take about
    183 CPU hours in the notebook's timing (2,340 for ACCg, about 191), beyond the one-hour notebook
    limit."""
    s = s[:i] + nb + s[j:]

old5a = s[s.index("- claim: fig5a-trigger-duration-unchanged"):s.index("- claim: fig5b-pupil-unchanged")]
new5a = """- claim: fig5a-trigger-duration-unchanged
  outcome: partially_reproduced
  notebook: reproduce_fan_2024.ipynb
  output: claim:fig5a-trigger-duration-unchanged
  notes: Under reading (a), M1-only and mutual Eyes events, the event in progress at the trial is
    longer on stimulation trials for dmPFC (median day difference 31 ms, p = 0.019; paper 0.269),
    not for OFC (8 ms, p = 0.61; paper 0.302). Reading (b), M1-only events, gives dmPFC 28 ms, p =
    0.028 and OFC p = 0.36. The claim holds for OFC and not for dmPFC. ACCg, outside the claim,
    gives 0.30 and 0.13. 13,779 of 19,474 trials fall inside an offline Eyes event under (a), 12,647
    under (b); the 5,695 others under (a) are spread evenly over areas and trial types (27.3% to
    30.1%; stimulation minus sham per day, dmPFC p = 0.069, OFC 0.58), 4,227 of them fall inside
    another M1 fixation (2,036 outside the face, 1,600 on the non-eye face), and 609 have an Eyes
    event starting within 20 ms after the trial. Counting those as the trigger gives dmPFC p = 0.020
    and OFC 0.58.
  deviations:
  - The triggering fixation is taken as the offline (EyeMMV) Eyes event that contains the trial
    time; the online fixation that triggered the trial is not in the files.
"""
s = s.replace(old5a, new5a)

oldsac = s[s.index("- claim: fig5cd-saccade-counts-unchanged"):s.index("findings:")]
newsac = """- claim: fig5cd-saccade-counts-unchanged
  outcome: partially_reproduced
  notebook: reproduce_fan_2024.ipynb
  output: claim:fig5cd-saccade-counts-unchanged
  notes: With the claims file's reading (a), a microsaccade lying strictly within an M1 fixation,
    microsaccade counts do not change for OFC (p = 0.069; paper 0.456) or dmPFC (0.89; paper 0.581)
    and macrosaccade counts do not change for dmPFC (0.24; paper 0.230), but OFC stimulation trials
    have fewer macrosaccades (median day difference -0.069 per post-gaze epoch, p = 0.044; paper
    0.055). One of the four tests fails. With the paper's code's labelling, reading (b), none does
    (smallest 0.15). ACCg, outside the claim, gives p = 0.009 (micro) and 0.004 (macro) under (a).
    The detector finds 454,642 saccades in the 1,179 social runs (386 per run), median duration 147
    ms (95th percentile 1,062 ms), median amplitude 13.7 degrees; in one run the gaze velocity inside
    fixations has a median of 19.7 deg/s and is under the detector's 5 deg/s saccade limit for 5.4%
    of samples, so many detected saccades span several fixations. In 202 of the 1,179 runs the
    MATLAB code's merge of overlapping saccades would not pair starts and ends.
  deviations:
  - The dataset holds no saccade events. Saccades are detected with a Python port of the
    Otero-Millan et al. (2014) detector, from the authors' MATLAB code at a pinned commit (inputs),
    with that code's defaults, called as the paper's code calls it (script/run_saccade_detection.m
    and script/detect_microsaccades.m at cc0bf994; M1's gaze in degrees from the first valid time
    sample, passed as both eyes, NaN samples as blinks). The claim is with_inputs for that software,
    as the claims file says.
  - The port uses scipy's k-means (Lloyd iterations from the same starting centres) in place of
    MATLAB's kmeans, and merges overlapping saccades as a union in the 202 runs where the MATLAB code
    would stop with an error.
  - The fixations that define a microsaccade are the files' M1 fixations (M1-only and mutual), the
    EyeMMV events the claims file names; the paper's code detects its own fixations
    (is_fixation with 20, 10 and 0.03), and its labelling, reading (b), counts a saccade as a
    microsaccade when its start is at least 50 samples after a fixation's start and before its end
    (script/label_saccades.m).
- claim: fig5e-h-saccade-kinematics-unchanged
  outcome: reproduced
  notebook: reproduce_fan_2024.ipynb
  output: claim:fig5e-h-saccade-kinematics-unchanged
  notes: With reading (a) of the macrosaccade, none of the 14 OFC and dmPFC tests gives p below
    0.05. Peak velocity of the first macrosaccade, OFC p = 0.052 and dmPFC 0.88 (paper 0.848, 1);
    slope difference against zero 0.70 and 0.59 (paper 0.665, 0.904); permutation 0.28 and 0.19
    (paper 0.515, 0.164); by direction group the smallest p is 0.071 (OFC CI; paper all above 0.47
    and 0.31). With the paper's code's labelling, reading (b), 3 of the 14 give p below 0.05 (dmPFC
    slope difference 0.030, OFC IC 0.048, dmPFC CC 0.037), so the result depends on how microsaccades
    are told from macrosaccades. 15,961 of 19,474 trials have a first macrosaccade under (a), 11,354
    under (b).
  deviations:
  - Saccades as in fig5cd-saccade-counts-unchanged (a Python port of the Otero-Millan et al. 2014
    detector, with_inputs). Slopes are least-squares lines over at least 3 saccades per trial type
    and day; the permutation seed 5 is a standard choice. Hemifields of the saccade's start and end
    are taken against the centre of roi_m2_face, as for the fixations.
"""
s = s.replace(oldsac, newsac)
open(p, 'w').write(s)
PYEOF
python $TMPDIR/rec1.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec2.py <<'PYEOF'
p = 'attempts/000959-fan-2024-01.yaml'
s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
rep("\nfindings:\n", """
inputs:
- what: The Otero-Millan et al. (2014) unsupervised clustering saccade detector (MATLAB), ported to
    Python in microstim.py for the two saccade claims
  source: https://github.com/ocular-motor-lab/otero-millan_et_al_microsaccade_detection at commit
    ce2c10dc6d8c38348b31e479751ac0da8cda6e6e
- what: The paper's code, read for how it calls the saccade detector and labels microsaccades
    (script/run_saccade_detection.m, script/detect_microsaccades.m, script/label_saccades.m)
  source: https://github.com/changlabneuro/microstim-ofc-social-attention at commit cc0bf994
- what: bfw.px2deg, the pixel to degree conversion the paper's code uses (same factor as the claims
    file's)
  source: https://github.com/nfagan/bfw at commit 11bb850f86d047f04e228a5405c765ae2d519764
- what: The causal decomposition code of Yang, Peng and Huang (2018), read for the steps and
    settings whose cost is timed (no result computed with it)
  source: https://github.com/accyang/causal-decomposition-analysis, release file
    causal_decomposition_20180901.zip
findings:
""")
rep("""    monkey T, where the paper reports 15 on average (14 to 15). Either some runs were not analysed in
    the paper or the counts in the paper are off; the files do not say which runs the paper used.""",
"""    monkey T, where the paper reports 15 on average (14 to 15). Either some runs were not analysed in
    the paper or the counts in the paper are off; the files do not say which runs the paper used. On
    the 14 monkey L days with 8 control runs, the runs are numbered 1 to 8, each 295.8 to 296.9 s
    long with 9 to 32 kept trials, so nothing in the files marks any of them as extra.""")
s = s.rstrip('\n') + """
- kind: metadata_insufficient
  statement: The fixation tables are named alike but cut the face differently. m1_neface (and
    m2_neface) is the face outside the Eyes and includes the Mouth (all 23,641 m1_mouth events are
    in it), while mutual_face is the face outside both the Eyes and the Mouth (mutual_wholeface
    equals mutual_eye plus mutual_face plus mutual_mouth). The table descriptions do not say so.
- kind: other
  statement: The files hold no saccade events. Run on M1's gaze as the paper's code calls it, the
    Otero-Millan et al. (2014) detector finds 386 saccades per social run with a median duration of
    147 ms and a 95th percentile of 1,062 ms; the gaze velocity inside fixations (median about 20
    deg/s in one run) is above the detector's 5 deg/s saccade limit for about 95% of samples, so many
    detected saccades span several fixations. In 202 of 1,179 social runs, the MATLAB code's merge of
    overlapping saccades yields unequal numbers of starts and ends, where that code would stop with
    an error. Whether the paper's gaze was filtered before detection is not stated.
"""
open(p, 'w').write(s)
PYEOF
python $TMPDIR/rec2.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec3.py <<'PYEOF'
import yaml
p = 'attempts/000959-fan-2024-01.yaml'
R = [
("design-days-per-area", True, "reproduced", "Cell 7 gives 15/15/15 days for L Eyes, 12/12/12 for T Eyes and 5/5/5 for T Mouth. Every count matches.", "No change needed."),
("design-sessions-per-day", True, "partially_reproduced", "Cell 9: monkey L has a mean of 6.02 control runs per day, against an expected 5 ± 0.5. Every other mean, range and the duration hold (L social 10.0, range 9–11; T social 14.0, range 14; T control 5; about 296 s).", "Added the listing the verifier asked for: the 14 monkey L days with 8 control runs all have runs numbered 1 to 8, each 295.8 to 296.9 s long with 9 to 32 kept trials, so nothing marks any as extra; added to the finding. Outcome kept."),
("fig1e-stim-counts-comparable", True, "reproduced", "Cell 12: the smallest FDR-corrected p is 0.908 for stimulations and 0.942 for shams, so all exceed 0.90.", "No change needed."),
("figs1d-stim-counts-nonsocial", True, "reproduced", "Cell 13: no corrected p is below 0.05. Not all exceed 0.10, though: shams between monkeys give corrected p = 0.082 (OFC and dmPFC).", "No change needed; the notes already say the paper's all p > 0.10 does not hold for two sham tests."),
("figs1e-eyes-more-than-face", True, "reproduced", "Cell 16: under both readings and both event sets, the corrected p ranges from 1.1e-7 to 4.4e-5, which is below 10^-4. Eyes are higher in every case.", "Following the verifier's question on the mutual tables, the notebook now shows that mutual_face excludes the Mouth while m1_neface includes it, and the non-eye Face count adds mutual_mouth for mutual events. Corrected p now 1.1e-07 to 3.1e-05. Outcome kept."),
("figs1e-eyes-vs-rdm-comparable", True, "not_reproduced", "Cell 17: under the deciding reading (a, the day's total), Eyes exceed RDM with corrected p of 0.0004, 0.00003 and 0.0004. Reading (b, the mean per run) gives p of 0.40–0.52. The deciding reading (a) compares day totals over 10–15 social runs with totals over about 5 control runs, which is bound to differ; the paper's all p > 0.30 fits only reading (b). This looks like a misreading in the claims file (B1).", "Added the question to questions/000959.yaml for a reader, as the protocol asks, and said so in the notebook and the notes. The claim is tested as the claims file has it; outcome kept."),
("fig2a-density-map-ofc", True, "reproduced", "Cell 21: the OFC stimulation-minus-sham sum is positive in the Face and in the Eyes, under both normalisations (z-score 7.47 and 3.71; total 0.0093 and 0.0046). The x-axis label is reversed for monkey L (B7), and the ROI masks use the first social run of each day while distances use each run's own ROIs; three recalibrated days are affected (B8).", "Corrected the axis label (negative is ipsilateral for both monkeys). The ROI squares are now those inside the ROI of every social run of the day; the notebook prints that the three recalibrated days are dmPFC and ACCg days, so the OFC sums are unchanged. Outcome kept."),
("fig2c-ofc-social-gaze-distance", True, "reproduced", "Cell 23, Methods reading: combined p = 0.00021, L p = 0.0067, T p = 0.016, all with negative medians.", "No change needed. The sanity cell now prints the range of all trial and event times (13.8 to 9,955 s), which confirms the 1e6 s run offset in window_pairs is valid (B12)."),
("fig2c-dmpfc-accg-no-distance-effect", True, "reproduced", "Cell 25: dmPFC p = 0.21, ACCg p = 0.39.", "No change needed."),
("fig2e-ofc-contralateral", True, "reproduced", "Cell 28, Methods reading: contralateral p = 0.00048 (negative), ipsilateral p = 0.058, contralateral vs ipsilateral p = 0.046 with contralateral more negative. Per monkey: L 0.018/0.073, T 0.012/0.30, against the paper's 0.015/0.073 and 0.012/0.204.", "No change needed."),
("fig2e-dmpfc-accg-no-hemifield-effect", True, "reproduced", "Cell 29: all six p are 0.10 or higher.", "No change needed."),
("fig2f-nonsocial-no-distance-effect", True, "reproduced", "Cell 31: OFC 0.22, dmPFC 0.64, ACCg 0.50.", "No change needed."),
("fig2gh-nonsocial-no-hemifield-effect", True, "reproduced", "Cell 32: all nine combined tests give p of 0.16 or higher.", "No change needed."),
("methods-ofc-distance-longer-windows", True, "reproduced", "Cell 34, Methods reading. 2 s: combined 0.003, L 0.012, T 0.23. 3 s: combined 0.003, L 0.007, T 0.20.", "No change needed."),
("methods-ofc-no-change-in-fixation-number", True, "reproduced", "Cell 37, reading (a): no per-monkey test is below 0.05 (smallest 0.121). The combined two-monkey whole-Face count at 1.5 s changes with OFC stimulation (p = 0.025), outside the per-monkey criterion and not reported by the paper (B9).", "No change needed; the notes already report the combined p = 0.025 as outside the claim."),
("methods-ofc-longer-face-looking", True, "partially_reproduced", "Cell 39 (a): all the tests hold (OFC whole Face 0.0025, dmPFC 0.80, ACCg 0.93, OFC Eyes 0.039). Under the median reading the combined (52.8 ms) and monkey L (65.1 ms) differences fall within tolerance, but monkey T's (46.2 ms, against 39.5 ± 3.95) does not. Under the mean reading none of the three falls within tolerance.", "No change needed."),
("methods-mouth-stimulation-no-effect", True, "reproduced", "Cell 41: 0 of 27 tests give p < 0.05, and the values are close to the paper's. With 5 days this test cannot fall below 0.0625, so it is uninformative (B11).", "No change needed; the notes already say the test cannot reach 0.05 with 5 days."),
("methods-eyes-vs-mouth-bootstrap", True, "not_reproduced", "Cell 43: the contralateral test over all Eyes days gives p = 0.078 (a) or 0.156 (b), robust across seeds (0.059–0.070). Both hemifields combined gives 0.043 (a), where the paper has 0.799, so the pattern is inverted. Neither reading satisfies the rule. The bootstrap runs only the Methods fixation reading; under the code's M1-only reading the gap is larger, so the variant might differ (B4).", "Added the bootstrap under the code's M1-only fixations: contralateral p = 0.049 (a) with all days (0.040 to 0.049 over five seeds) and 0.006 with monkey T, ipsilateral 0.30 and 0.35, both hemifields 0.050 and 0.036. It does not give the paper's pattern either. Outcome kept."),
("fig3b-ofc-inter-looking-interval", True, "reproduced", "Cell 47: OFC p = 0.044 (stimulation shorter), dmPFC 0.77, ACCg 0.34. OFC p = 0.044 depends on excluding events that start at the trial sample (91 trials); counting them gives p = 0.058. The strict choice follows the criterion, but the result sits at the threshold (B5).", "No change needed; the notes and the conclusion already give p = 0.058 when those events count, and the question is put to the paper's authors in the findings."),
("ili-nonsocial-no-effect", True, "reproduced", "Cell 49: OFC 0.70, dmPFC 0.13, ACCg 0.84.", "No change needed."),
("ili-missing-trials-41", True, "reproduced", "Cell 51: 41.3% under reading (a) and 39.9% under (b), both within 41 ± 4.1.", "No change needed."),
("figs3b-ili-trial-level", True, "reproduced", "Cell 54: OFC p = 0.017 (stimulation shorter), dmPFC 0.39, ACCg 0.62.", "No change needed."),
("figs3c-reciprocation-day-level-none", True, "reproduced", "Cell 58: OFC 0.11, dmPFC 0.56, ACCg 0.32. Trials with no sequence: 86.4% (a) and 85.1% (b), both within 86 ± 8.6.", "No change needed."),
("fig3d-ofc-reciprocation-latency", True, "reproduced", "Cell 60: OFC p = 0.023 (stimulation shorter), dmPFC 0.72, ACCg 0.36.", "No change needed. The tie rule in reciprocation (B13) is recorded as a standard choice in the deviations of figs3c-reciprocation-day-level-none."),
("partner-monkey-unchanged", True, "partially_reproduced", "Cell 62: under reading (a) of the M2 reciprocation latency, dmPFC gives p = 0.044. The criterion needs no p < 0.05 under every reading. The distance and inter-looking-interval tests, and reading (b), all hold.", "No change needed."),
("figs4a-causal-strength-no-stim-effect", True, "blocked", "Cell 66 estimates 680 CPU hours with PyEMD. That is plausible, but the estimate times one 100-ensemble single-threaded run multiplied by 10, applies it to all 19,474 social trials, never times reading (b), and does not consider running in parallel or a faster EMD implementation; too_large is plausible but not demonstrated (B3).", "Replaced the estimate: one EEMD at 1,000 ensembles with the Yang code's 10 fixed sifts is timed directly on one core (18.3 s) and on four processes (9.2 s). Reading (b), the Yang code's settings, needs 1,000 ensembles as well (the code has no default; its example uses 1,000), so both readings cost the same. The notebook gives CPU and wall hours per subset (every social trial about 1,590 CPU hours; the 2,250 OFC epoch trials about 183) and a floor for a compiled implementation at 10 microseconds per spline envelope (12 to 104 CPU hours). Outcome kept, blocked as too_large."),
("figs4b-causal-strength-no-epoch-effect", True, "blocked", "Same as figs4a-causal-strength-no-stim-effect: too_large is plausible but not demonstrated (B3).", "As for figs4a-causal-strength-no-stim-effect. Outcome kept."),
("epoch-days-76-of-81", True, "reproduced", "Cell 64, reading (a): 76 days, and the five excluded are exactly the dates the code names.", "No change needed."),
("ofc-slope-unchanged-by-epoch", True, "blocked", "Same as figs4a-causal-strength-no-stim-effect. The epoch and slope claims need only the first 90 stimulation trials per day, about 6,840 trials over 76 days, or about 2,430 for the OFC days alone (B3).", "The notebook now costs this subset: the 2,250 stimulation trials of the 25 OFC epoch days take about 183 CPU hours (92 hours of wall time on four processes, about 12 CPU hours at the compiled floor), beyond the one-hour limit. Outcome kept."),
("fig4c-dmpfc-slope-late-greater", True, "blocked", "Same as figs4a-causal-strength-no-stim-effect (B3).", "Costed per subset as for ofc-slope-unchanged-by-epoch (dmPFC days about 183 CPU hours, ACCg about 191). Outcome kept."),
("fig4d-dmpfc-slope-permutation", True, "blocked", "Same as figs4a-causal-strength-no-stim-effect (B3).", "Costed per subset as for ofc-slope-unchanged-by-epoch. Outcome kept."),
("dmpfc-slope-positive", True, "blocked", "Same as figs4a-causal-strength-no-stim-effect (B3).", "Costed per subset as for ofc-slope-unchanged-by-epoch. Outcome kept."),
("fig5a-trigger-duration-unchanged", False, "partially_reproduced", "Cell 68: OFC holds (p = 0.61 / 0.36), but dmPFC triggering fixations are longer after stimulation under both readings (p = 0.019 / 0.028; paper 0.269). 29% of trials (5,695 of 19,474) have no M1 Eyes event in progress at the trial time; this selection is left uninvestigated, and the failing dmPFC test depends on it (B6).", "Changed the outcome from not_reproduced to partially_reproduced: the claim of absence holds for OFC and fails for dmPFC, so it holds in part. Added the breakdown asked for: the trials with no Eyes event in progress are spread evenly over areas and trial types (27.3% to 30.1%; per day stimulation minus sham, dmPFC p = 0.069), 4,227 of them fall inside another M1 fixation and 609 have an Eyes event starting within 20 ms after the trial; counting those leaves dmPFC p = 0.020."),
("fig5b-pupil-unchanged", True, "reproduced", "Cell 70: 0 of 70 bins below 0.05 in each area (smallest p: 0.31, 0.51, 0.11).", "No change needed."),
("fig5cd-saccade-counts-unchanged", True, "blocked", "The archive holds no saccade events; gaze at 1 kHz is present, so the claim could be tested after an Otero-Millan detection run. The notebook's reason, not_runnable, is not an allowed reason. The claims file prescribes a with_inputs run, the detection software is public, and this was not attempted or costed (B2).", "not_runnable is one of the protocol's block reasons, but the claim is now tested: the detector's MATLAB code (pinned commit) is ported to Python and called as the paper's own code calls it, with the sanity cell listing the groups of a file (no saccade or processing tables). Outcome changed from blocked to partially_reproduced: under the claims file's reading, OFC macrosaccades are fewer after stimulation (p = 0.044; paper 0.055), the other three tests hold; under the paper's code's labelling none fails."),
("fig5e-h-saccade-kinematics-unchanged", True, "blocked", "Same as fig5cd-saccade-counts-unchanged (B2).", "Tested with the same detector; outcome changed from blocked to reproduced under the claims file's reading (0 of 14 tests below 0.05); the paper's code's labelling gives 3 of 14."),
]
lines = ["verifications:", "- date: '2026-11-01'", "  kind: agent",
         "  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
         "  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the helper module and the claims file, with the paper. The verifier tested helper functions on synthetic inputs and checked signrank against a normal approximation. Its report had no attempt record and gave its own outcome for each claim; 35 of 36 agree with the record as it then stood.",
         "  results:"]
out = {"results": [dict(claim=c, agrees=a, outcome=o, reason=r, response=resp) for c, a, o, r, resp in R]}
txt = yaml.dump(out, sort_keys=False, allow_unicode=True, width=100)
body = "\n".join("  " + l for l in txt.splitlines()[1:])
s = open(p).read().rstrip("\n")
s += "\n" + "\n".join(lines) + "\n" + body + "\n"
open(p, "w").write(s)
d = yaml.safe_load(open(p))
print(len(d["verifications"][0]["results"]), len(d["outcomes"]))
PYEOF
python $TMPDIR/rec3.py
```

```
36 36
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/000959-fan-2024 2>&1 | tail -15; grep -n "—\|rather" attempts/000959-fan-2024-01.yaml questions/000959.yaml entries/000959-fan-2024/README.md entries/000959-fan-2024/microstim.py | head; python -c "
import json;nb=json.load(open('entries/000959-fan-2024/reproduce_fan_2024.ipynb'))
s=''.join(''.join(c['source']) for c in nb['cells']); print('emdash' , '—' in s, 'rather', 'rather' in s)"; date -u
```

```
0 error(s)
emdash False rather False
Sun Nov  1 02:11:17 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import json, yaml, jsonschema
s=json.load(open('schemas/attempt.schema.json')); d=yaml.safe_load(open('attempts/000959-fan-2024-01.yaml'))
jsonschema.validate(d, s); print('valid')
"; git status --short
```

```
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    jsonschema.validate(d, s); print('valid')
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/jsonschema/validators.py", line 1332, in validate
    raise error
jsonschema.exceptions.ValidationError: datetime.date(2026, 10, 31) is not of type 'string'

Failed validating 'type' in schema['properties']['date']:
    {'type': 'string', 'format': 'date'}

On instance['date']:
    datetime.date(2026, 10, 31)
 M attempts/000959-fan-2024-01.yaml
 M entries/000959-fan-2024/README.md
 M entries/000959-fan-2024/entry.yaml
 M entries/000959-fan-2024/microstim.py
 M entries/000959-fan-2024/reproduce_fan_2024.ipynb
?? .bash_profile
?? .bashrc
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json, yaml, jsonschema, datetime
s=json.load(open('schemas/attempt.schema.json')); d=yaml.safe_load(open('attempts/000959-fan-2024-01.yaml'))
d['date']=str(d['date'])
jsonschema.validate(d, s); print('valid')
"; git status --short scripts .idea | head; git diff --stat
```

```
valid
?? .idea
?? scripts
 attempts/000959-fan-2024-01.yaml                 | 414 ++++++++++++++++++--
 entries/000959-fan-2024/README.md                |  12 +-
 entries/000959-fan-2024/entry.yaml               |   7 +-
 entries/000959-fan-2024/microstim.py             | 232 ++++++++++-
 entries/000959-fan-2024/reproduce_fan_2024.ipynb | 472 +++++++++++++++++++----
 5 files changed, 1024 insertions(+), 113 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/000959-fan-2024; python - <<'EOF'
p='entry.yaml'; s=open(p).read()
s=s.replace("""  hemifield split, inter-looking interval, reciprocation latency, the partner's gaze, fixation counts
  and durations, pupil size and the trial counts between microstimulation and sham trials, and detects saccades with a port of
  the Otero-Millan et al. (2014) detector to test their counts and kinematics. The causal
  decomposition is not run; its cost is timed.""","""  hemifield split, inter-looking interval, reciprocation latency, the partner's gaze, fixation counts
  and durations, pupil size and the trial counts between microstimulation and sham trials, and
  detects saccades with a port of the Otero-Millan et al. (2014) detector to test their counts and
  kinematics. The causal decomposition is not run; its cost is timed.""")
open(p,'w').write(s)
EOF
cd ../..; python tools/entry.py check entries/000959-fan-2024 2>&1 | tail -2
```

```
0 error(s)
```

**Agent**

I addressed all 13 points in the round-1 report. The entry re-ran cleanly (`python tools/entry.py all`, 14.4 min), every conclusion matches the new numbers, and `check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **fig5a-trigger-duration-unchanged**: not reproduced → partially reproduced, which is what the verifier gave. The claim holds for OFC (p = 0.61) but not dmPFC (p = 0.019). The verifier also wanted the trials with no Eyes fixation in progress at the trial time examined (29%). They are spread evenly over areas and trial types (27.3% to 30.1%). Counting the 609 trials whose Eyes fixation starts within 20 ms after the trial leaves dmPFC at p = 0.020.
- **fig5cd-saccade-counts-unchanged**: blocked → partially reproduced. `not_runnable` is in fact an allowed block reason, but the verifier was right that the detector's code is public. I ported its MATLAB code (pinned commit) to Python in `microstim.py` and called it the way the paper's own repository does. Under the claims file's definition of a microsaccade, OFC trials have fewer macrosaccades after stimulation (p = 0.044; the paper has 0.055); the other three tests hold. Under the paper's code's labelling, none of the four fails.
- **fig5e-h-saccade-kinematics-unchanged**: blocked → reproduced. None of the 14 OFC and dmPFC tests gives p < 0.05; under the paper's code's labelling, 3 of 14 do.

**Two things about the saccade results**
- On these data the detected events run long (median 147 ms, 95th percentile 1,062 ms). In the run I checked, gaze speed inside fixations is above the detector's 5 deg/s cut-off about 95% of the time, so many detected saccades span several fixations.
- In 202 of the 1,179 social runs the MATLAB code's merging step would stop with an error. The port merges overlapping saccades into one there instead.

Both are recorded as findings.

**Added or corrected**
- **Reader question:** the verifier's point that the claims file may misread the Eyes-versus-RDM comparison (day totals over twice as many social runs as control runs) is now in `questions/000959.yaml`. The claim is unchanged and keeps its not reproduced outcome.
- **Causal-decomposition cost:** I re-timed it with the settings of the decomposition code itself (1,000 ensembles, 10 fixed sifts). That code has no default ensemble size and its example uses 1,000, so both readings cost the same. Every subset is still far over the one-hour notebook limit:

| Subset | CPU hours | Hours on 4 processes | Floor for a compiled version |
|---|---|---|---|
| All social trials (figs4a, figs4b) | about 1,590 | about 790 | about 104 CPU h |
| First 90 stimulations, 25 OFC days (smallest slope-claim subset) | about 183 | about 92 | about 12 CPU h |

  The six claims stay blocked as `too_large`.
- **Eyes-versus-Mouth bootstrap:** now also run with the code's M1-only fixations. Contralateral p is 0.049 over all days and 0.006 for monkey T, but both hemifields combined gives 0.050 and 0.036, so it still does not match the paper's pattern. The outcome stays not reproduced.
- **Outputs the verifier asked for:**
  - one file's groups, which contain no saccade or processing tables;
  - the range of all trial and event times (13.8 to 9,955 s), which confirms the time offset used to pair trials with fixations is safe;
  - mutual-table counts: `mutual_face` excludes the Mouth while `m1_neface` includes it, so the non-eye Face count now adds `mutual_mouth` (corrected p is now 1.1e-07 to 3.1e-05, outcome unchanged);
  - the control-run listing for monkey L's 8-run days: runs 1 to 8, all full length, nothing marks any as extra.
- **Density map:** fixed the reversed x-axis label. The ROI squares are now those inside the ROI of every run of the day. The three recalibrated days are dmPFC and ACCg days, so the OFC result is unaffected.
- **Attempt record:** the round is recorded under `verifications` (35 of 36 claims agreed). I added `inputs` (detector code, the paper's code, the pixel-to-degree function, the decomposition code) and two findings. The README and `entry.yaml` are updated.

**Not done**
- I did not switch the signed-rank test to MATLAB's normal approximation. The verifier's own check showed no p-value crossing 0.05.
- No change was needed for the points reported as not affecting a conclusion: the inter-looking-interval threshold, the combined fixation-count test, the 5-day Mouth test and the tie rule. Each was already stated in the notes.

## End of run

83 turns, 54 minutes, result: success.
