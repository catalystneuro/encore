# temmar-2025 · author-revise-1 · run 43255078150

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md | head -c 200000 | wc -c; ls entries/temmar-2025 transcripts/temmar-2025; cat transcripts/temmar-2025/verifier-1-report.md
```

**Agent calls Bash**

```bash
cat docs/protocol.md
```

```
<persisted-output>
Output too large (38.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b34755d3-192a-46ed-8a0d-7096d467d181/tool-results/b7a4abcwd.txt

Preview (first 2KB):
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
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

```
Thu Nov 12 16:10:31 UTC 2026
38977
entries/temmar-2025:
README.md
decoding.ipynb
entry.yaml
link.py
multiday.ipynb
requirements.in
requirements.lock.txt
signals.ipynb

transcripts/temmar-2025:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author.md
claims-check-report.md
[... 59 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b34755d3-192a-46ed-8a0d-7096d467d181/tool-results/b7a4abcwd.txt"
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
ls attempts | grep temmar; wc -l attempts/temmar-2025-01.yaml entries/temmar-2025/*; cat entries/temmar-2025/entry.yaml; ls questions | grep temmar; ls executed/temmar-2025 2>/dev/null; git log --oneline | head
```

```
temmar-2025-01.yaml
   333 attempts/temmar-2025-01.yaml
    20 entries/temmar-2025/README.md
   624 entries/temmar-2025/decoding.ipynb
    28 entries/temmar-2025/entry.yaml
   422 entries/temmar-2025/link.py
   382 entries/temmar-2025/multiday.ipynb
     9 entries/temmar-2025/requirements.in
  1152 entries/temmar-2025/requirements.lock.txt
  1128 entries/temmar-2025/signals.ipynb
  4098 total
schema_version: 1
name: temmar-2025
type: reproduction
title: Long-term intracortical neural activity and kinematics, LINK (Temmar et al. 2025)
description: Tests the findings of Temmar et al. (2025) on dandiset 001201, which holds 312 sessions of
  spiking-band power, threshold crossings and finger kinematics from one macaque over 3.5 years. It checks
  the dataset's counts and contents, the decline of neural signals over time, single-channel tuning,
  same-day and cross-day decoding with ridge regression and an LSTM, and multi-day training. The LSTM
  analyses run on subsets of sessions for time, and the continual fine-tuning is too large to run.
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/temmar-2025-01.yaml
```

```
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
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
[... 313 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l claims/temmar-2025.yaml questions/temmar-2025.yaml; cat questions/temmar-2025.yaml; ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/temmar-2025.yaml"
}
```

```
1	# Claims for Temmar et al. (2025), "Long-term Intracortical Neural activity and Kinematics
2	# (LINK)", NeurIPS 2025 Datasets and Benchmarks track, on dandiset 001201.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
4	# 2026-11-12, protocol pilot-14 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record (open-access PDF from the Curran Associates NeurIPS 2025
7	# proceedings, extracted to paper/10.52202-085713-4642.txt), main text, figure legends and
8	# checklist, and the supplement (Supplementary Materials and Appendices, from OpenReview):
9	# Appendix A (task, implants, feature extraction), B (curation, file format), C (analysis
10	# methods) and Figures S1 to S6. The paper reports no statistical test for any finding; its
11	# findings are slopes of linear fits, counts, R2 values and visual descriptions of figures.
12	#
13	# Code read: github.com/chesteklab/LINK_dataset at commit 5e1c36a1282f90abb8d96963920a8b1fdd27a6e7
14	# (2026-10-20). It holds the NWB-to-pickle converter (utils/), the signal-change analysis
15	# (data_processing/signal_changes: mean SBP per channel and day, active channels, participation
16	# ratio), single-channel tuning (data_processing/single_channel_tuning/tuning_utils.py), the
17	# population PCA analysis (data_processing/pop_level_analyses/population_level_analyses.py),
18	# single-day RR and LSTM decoders and their cross-day evaluation (data_processing/bci_decoding),
19	# the multi-day training (data_processing/stability/stability, which calls an outside library,
20	# "neuraldecoding", not in the repository) and the continual fine-tuning
[... 544 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; cat README.md requirements.in; python - <<'EOF'
import json
for nb in ['multiday.ipynb']:
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        print(f"--- [{i}] {c['cell_type']} {c.get('metadata',{}).get('tags','')}")
        print(''.join(c['source']))
EOF
```

```
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
[... 238 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
for nb in ['executed/temmar-2025/multiday.ipynb','executed/temmar-2025/decoding.ipynb']:
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        if c['cell_type']!='code': continue
        out=''
        for o in c.get('outputs',[]):
            if 'text' in o: out+=''.join(o['text'])
            elif 'data' in o and 'text/plain' in o['data']: out+=''.join(o['data']['text/plain'])[:300]
        print(f"=== {nb[-15:]} [{i}]"); print(out[:3000])
EOF
```

```
=== /multiday.ipynb [1]
312 sessions; on single-session days 294; eligible day-0 sessions 283 (the Figure 5A legend reports 283 days)
day-0 sessions: ['2020-03-02', '2020-11-05', '2021-03-22', '2021-06-08', '2021-07-28', '2021-09-14', '2022-01-24', '2022-04-11', '2022-08-01', '2022-10-12', '2023-03-10', '2023-06-21']

=== /multiday.ipynb [3]
loaded 282 sessions in 364 s; peak memory 3.34 GB

=== /multiday.ipynb [4]
sessions loaded: 282 | by year: {2020: 31, 2021: 115, 2022: 91, 2023: 45}
training bins 16632 to 27756, test bins 4093 to 7497
SBP (stored units): 0.056 to 250.587
  hold-out idx_pos: 0.000 to 1.000
  hold-out mrs_pos: 0.000 to 1.000
  hold-out idx_vel: -0.290 to 0.448
  hold-out mrs_vel: -0.407 to 0.341

=== /multiday.ipynb [6]
24 fits in 8.3 min; seconds per fit 73 to 76
days spanned by the 5 training sessions: 7 to 24
evaluations per model: 2 to 80
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "e−0\|e^\|exp\|Figure 5\|fine-tun\|UPDATE" paper/10.52202-085713-4642.txt | head -40; sed -n 1,80p tools/entry.py | head -5; grep -n "def \|subprocess\|parallel" tools/entry.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 330,420p paper/10.52202-085713-4642.txt; sed -n 500,600p tools/entry.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/temmar-2025; cat link.py
```

```
"""Loading and measures for the LINK dataset (DANDI:001201), used by the notebooks of the
temmar-2025 entry, which test Temmar et al. (2025), NeurIPS Datasets and Benchmarks.

Where each parameter comes from is given next to it, as one of:
- "claim <id>": the claims file's criterion for that claim (claims/temmar-2025.yaml), which cites
  the paper or its code (github.com/chesteklab/LINK_dataset at 5e1c36a);
- "paper, <passage>": a detail the claims file lacks, taken from the paper (protocol, author 1.6);
- "assumption": a choice the paper leaves open, stated as such;
- "standard choice": a detail that cannot change a result.

The data are streamed from the archive (remfile + h5py); nothing is written to disk.
"""
from __future__ import annotations

import os
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
[... 402 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; python - <<'EOF'
import json
for nb in ['decoding.ipynb']:
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        print(f"--- [{i}] {c['cell_type']} {c.get('metadata',{}).get('tags','')}")
        print(''.join(c['source']))
EOF
```

```
--- [0] markdown 
# Temmar et al. (2025), LINK: same-day and cross-day decoding (Figure 4, Appendix C.1)

Paper: doi:10.52202/085713-4642. Dataset: DANDI:001201, version 0.261026.1912, streamed (the most recent
published version; the paper cites none, and the three published versions hold the same assets, see
`signals.ipynb`). Claims file: `claims/temmar-2025.yaml`. Code read: github.com/chesteklab/LINK_dataset at
5e1c36a.

| Claim | Tested here |
|---|---|
| fig4a-sameday-stable | RR on all 312 sessions, the LSTM on every 16th session |
| fig4a-lstm-beats-rr | on the LSTM sessions |
| fig4bc-dof-accuracy | RR on all sessions, LSTM on its sessions |
| fig4d-cross-day-decay | RR and LSTM decoders of the LSTM sessions, tested on every session within 100 days |
| suppc1-shuffle-baseline | RR on all sessions, LSTM on its sessions |
| fig2a-irregular-shifts | all days, with the R2 above |

Why a subset for the LSTM. One LSTM of the paper's size (2000 iterations, batch 64, 20 bins, 300 hidden
units) takes about 105 s to train alone on one CPU thread of this runner, and about 200 s when four train at once
(timed while preparing; the cell below prints the time of each fit). 312 of them, four at a time, take
[... 363 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; grep -l "verifications:" attempts/*.yaml | head -3; f=$(grep -l "verifications:" attempts/*.yaml | head -1); awk '/^verifications:/,0' $f | head -60; ls questions | head; cat questions/$(ls questions | head -1) | head -40
```

```
Thu Nov 12 16:12:54 UTC 2026
attempts/amjad-2025-01.yaml
attempts/armstrong-2026-01.yaml
attempts/ashworth-2025-01.yaml
verifications:
- date: '2026-10-15'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
    reward_blocks). It had no attempt record and took the claims from the claims file.
  results:
  - claim: insertion-yield
    agrees: true
    outcome: blocked
    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
      "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -30 questions/ashworth-2025.yaml; grep -n "temmar\|questions" tools/entry.py | head
```

```
dandiset: "001708"
paper: doi:10.64898/2025.12.15.693905
questions:
- claim: figs3-neutral-unmodulated
  asked: 2026-11-05
  question: >-
    The criterion takes the trials of all NEUTRAL units of all files, and expects 32 cells with 69
    and 70 trials. The dataset has 36 NEUTRAL units. Four are in 'evoked' files, labelled "NEUT";
    the other 32, labelled "Neutral", are the ongoing and evoked/ongoing cells. The 36 give 76 to 79
    trials. The paper's n = 32 is the second set, which is also the set of the ongoing analyses.
    Should the criterion take the 32 NEUTRAL cells of the 'ongoing' and 'evoked/ongoing' files?
  passage: >-
    "In contrast, NEUTRAL-cells (n = 32; 69 withdrawal-aligned and 70 heat-aligned trials) exhibited
    no discernible modulation associated with either heat onset or withdrawal behavior" (Results,
    Evoked ON/OFF activity unfolds over multiple timescales, paragraph 9). The Methods (Experiments,
    paragraph 4) count 24 NEUTRAL cells in the evoked protocol and 12 in the ongoing protocol, 36 in
    all.
  why: >-
    With all 36 units the cell count (36 against 32 +- 3.2) and the withdrawal-aligned trial count
    (76 to 78 against 69 +- 6.9) fall outside tolerance, and the claim is partially reproduced.
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; python -c "
import link; A=link.assets(); print(A.head(3).to_string()); c=A.groupby('date').size(); print(A[A.date.map(c)==2].path.head(4).tolist())"; python - <<'EOF'
import json
d=json.load(open('signals.ipynb'))
for i,c in enumerate(d['cells']):
    s=''.join(c['source'])
    if 'fig3e' in s or 'array_name' in s or 'figs5' in s: print(f"--- [{i}] {c['cell_type']}"); print(s[:3500])
EOF
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import link; A=link.assets(); print(A.head(3).to_string()); c=A.groupby('date').size(); print(A[A.date.map(c)==2].path.head(4).tolist())
    ^^^^^^^^^^^
  File "entries/temmar-2025/link.py", line 18, in <module>
    import h5py
ModuleNotFoundError: No module named 'h5py'
--- [0] markdown
# Temmar et al. (2025), LINK: the dataset, neural signals and tuning over time

Paper: Temmar, Gill, Wang et al., "Long-term Intracortical Neural activity and Kinematics (LINK): An
intracortical neural dataset for chronic brain-machine interfaces, neuroscience, and machine learning",
NeurIPS 2025 Datasets and Benchmarks, doi:10.52202/085713-4642.

Dataset: DANDI:001201, version 0.261026.1912 (doi:10.48324/dandi.001201/0.261026.1912), streamed.
The paper cites no version, so the most recent published one is pinned. The dandiset has three
published versions (0.251023.2336, 0.261015.2153, 0.261026.1912); the cell below shows that the
three list the same 312 assets with the same asset identifiers, so the data the analysis uses do not
differ between them.

[... 197 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -a executed/temmar-2025/; ls executed/temmar-2025/.venv/bin/python && executed/temmar-2025/.venv/bin/python -c "import torch, h5py; print(torch.__version__)"; nproc; free -g
```

```
.
..
.clean-run.json
.venv
decoding.ipynb
multiday.ipynb
result.json
signals.ipynb
executed/temmar-2025/.venv/bin/python
2.15.0+cpu
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
Swap:              2           0           2
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; ../../executed/temmar-2025/.venv/bin/python -c "
import link; A=link.assets(); print(A.head(3).to_string()); c=A.groupby('date').size(); print(A[A.date.map(c)==2].path.head(4).tolist())"
```

```
path                              asset_id      size       date
0  sub-Monkey-N/sub-Monkey-N_ses-20200127_ecephys.nwb  c002a9a1-664d-4a69-af02-ba810046c4fb  45005026 2020-01-27
1  sub-Monkey-N/sub-Monkey-N_ses-20200130_ecephys.nwb  9d1820f1-7583-4faf-bbd0-7e9fb7001ca4  43863496 2020-01-30
2  sub-Monkey-N/sub-Monkey-N_ses-20200204_ecephys.nwb  ea07a2e3-d5f4-4036-9b62-93d1f89cba64  43052898 2020-02-04
['sub-Monkey-N/sub-Monkey-N_ses-20211015_obj-1wbkdus_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20211015_obj-a6r2sq_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220225_obj-1n9hlgs_ecephys.nwb', 'sub-Monkey-N/sub-Monkey-N_ses-20220225_obj-1o8kg92_ecephys.nwb']
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR && cat > $TMPDIR/mk_finetune.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
C = []
def md(s): C.append(nbf.v4.new_markdown_cell(s))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s)
    if tags: c.metadata["tags"] = tags
    C.append(c)

md("""# Temmar et al. (2025), LINK: continual fine-tuning (Figure 5B)

Paper: doi:10.52202/085713-4642. Dataset: DANDI:001201, version 0.261026.1912, streamed (the most recent
published version; the paper cites none, and the three published versions hold the same assets, see
`signals.ipynb`). Claims file: `claims/temmar-2025.yaml`. Code read: github.com/chesteklab/LINK_dataset at
5e1c36a.

| Claim | Here |
|---|---|
| fig5b-finetune | 30 s fine-tuning on all 20 seed days under both normalisation readings; 120 s and 300 s on 2 of the 20 seed days under the code's normalisation |

Why a subset. One LSTM iteration takes about 0.037 s with four fits at once (`decoding.ipynb` and
`multiday.ipynb` print the fit times). The 20 seed days are followed by 1146 sessions within 200 days.
Fine-tuning is continual, so each seed's sessions are fine-tuned one after the other. The 30 s arm (50
iterations per session) costs about 57,000 iterations per normalisation reading, about 9 minutes with
four chains at once, and runs in full under both readings. The 120 s and 300 s arms (250 and 500
iterations) would cost about 1.2 million iterations under the two readings, about 3 hours, so they run
on two seed days only (the 6th and 16th of the 20, chosen before any result), under the normalisation of
the code. The 60 s arm is not in the criterion and is not run.""")

code("""import os, time, resource
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import link

T0 = time.time()
ITERS = int(os.environ.get("LINK_DEV_ITERS", link.LSTM_ITERS))       # 2000 (paper); lowered only while developing
FT_SCALE = float(os.environ.get("LINK_DEV_FTSCALE", "1"))            # 1 = the criterion's iterations; lowered only while developing
N_SEEDS = int(os.environ.get("LINK_DEV_NSEEDS", "20"))               # 20 (paper); lowered only while developing
HORIZON = 200      # paper, Section 4.3: fine-tuned for up to 200 days after the seed day
EVAL_EVERY = 5     # score every 5th hold-out bin (cost), as in the other notebooks
# claim fig5b-finetune: the last 30, 120 or 300 s (1500, 6000, 15000 bins) of the training trials, 50, 250, 500 iterations
DURATIONS = {30: (1500, 50), 120: (6000, 250), 300: (15000, 500)}
LONG_SEEDS = [5, 15]   # the seed days given the 120 s and 300 s arms (positions in STARTING_DAYS; see above)
# claim fig5b-finetune: STARTING_DAYS of continual_learning_lstm.py
STARTING_DAYS = ["2020-07-08", "2020-10-02", "2020-12-12", "2021-02-27", "2021-04-05", "2021-05-05", "2021-06-16",
                 "2021-07-09", "2021-07-29", "2021-08-19", "2021-09-14", "2021-10-27", "2022-01-17", "2022-02-21",
                 "2022-04-01", "2022-04-21", "2022-06-01", "2022-08-05", "2022-09-01", "2022-09-30"]
SEEDS = [pd.Timestamp(d) for d in STARTING_DAYS][:N_SEEDS]
LONG_SEEDS = [i for i in LONG_SEEDS if i < len(SEEDS)]
A = link.assets()
dates = sorted(A["date"].unique())
print(f"{len(A)} sessions on {len(dates)} days; seed days in the dataset: {sum(d in set(dates) for d in SEEDS)} of {len(SEEDS)}")
LATER = {d0: [d for d in dates if d0 < d <= d0 + pd.Timedelta(days=HORIZON)] for d0 in SEEDS}
print("later days within 200 days, per seed: %d to %d, %d in all" % (
    min(map(len, LATER.values())), max(map(len, LATER.values())), sum(map(len, LATER.values()))))""")

md("""## Load the sessions needed

Every day from the first seed day to 200 days after the last. On a day with two sessions the CO session
is used (claim fig5b-finetune). Each session is split into its first 300 trials (training) and the 75
after them (hold-out), as in the other notebooks.""")

code("""need = sorted(set(SEEDS) | {d for v in LATER.values() for d in v})
rows_by_date = {d: A[A["date"] == d] for d in need}


def load(d):
    out = []
    for aid in rows_by_date[d]["asset_id"]:
        s = link.read_session(aid, tcr=False)
        (xtr, ytr), (xte, yte) = link.split(s)
        out.append({"date": d, "style": s["style"], "xtr": xtr, "ytr": ytr, "xte": xte, "yte": yte})
    co = [o for o in out if o["style"] == "CO"]
    return d, (co[0] if len(out) > 1 and co else out[0]), len(out)


t = time.time()
with ThreadPoolExecutor(4) as ex:
    loaded = list(ex.map(load, need))
SES = {d: s for d, s, _ in loaded}
two = [d for d, _, n in loaded if n > 1]
print(f"loaded {len(SES)} days in {time.time() - t:.0f} s; two-session days {len(two)}, CO used on "
      f"{sum(SES[d]['style'] == 'CO' for d in two)}; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")""")

code("""L5 = pd.DataFrame([{"date": d, "style": s["style"], "train_bins": len(s["xtr"]), "test_bins": len(s["xte"])} for d, s in SES.items()])
print("days loaded:", len(L5), "| by year:", L5["date"].dt.year.value_counts().sort_index().to_dict(),
      "| styles:", L5["style"].value_counts().to_dict())
print("training bins %d to %d (the 300 s arm uses the last 15000), hold-out bins %d to %d" % (
    L5["train_bins"].min(), L5["train_bins"].max(), L5["test_bins"].min(), L5["test_bins"].max()))
print("SBP (stored units): %.3f to %.3f" % (min(s["xte"].min() for s in SES.values()), max(s["xte"].max() for s in SES.values())))
yk = np.vstack([s["yte"] for s in SES.values()])
for n, a, b in zip(link.KIN_NAMES, yk.min(0), yk.max(0)):
    print(f"  hold-out {n}: {a:.3f} to {b:.3f}")""", ["sanity"])

md("""## Seed decoders, and the curves without fine-tuning

On each seed day an LSTM is trained as in `decoding.ipynb` (Appendix C.1: first 300 trials, input
z-scored on them, 2000 iterations, seed 42). Without fine-tuning it is then evaluated on the hold-out of
every later day within 200 days, under the two comparisons the criterion names: (a) input normalisation
held at the seed day's, the procedure of the single-session curve of fig5a-multiday-short-term; (b)
normalisation refit on the test day's training trials, the procedure of the LSTM curve of
fig4d-cross-day-decay. Both are computed here from these 20 seed decoders, so that the comparison has
the same seed days as the fine-tuning.""")

code("""def z(x, mu, sd):
    return ((x - mu) / sd).astype(np.float32)


def r2(state, onorm, s, mu, sd):
    p = link.lstm_predict(state, onorm, z(s["xte"], mu, sd), every=EVAL_EVERY)
    return link.r2_per_output(s["yte"][::EVAL_EVERY], p).mean()


def seed_task(si):
    t0 = time.time()
    d0 = SEEDS[si]
    s = SES[d0]
    mu, sd = link.zparams(s["xtr"])
    state, onorm = link.lstm_train([(z(s["xtr"], mu, sd), s["ytr"])], seed=42, iters=ITERS)
    fit_s = time.time() - t0
    rows = [{"seed": si, "rel": 0, "arm": "none", "norm": norm, "r2": r2(state, onorm, s, mu, sd)} for norm in ("a", "b")]
    for d in LATER[d0]:
        t = SES[d]
        rows.append({"seed": si, "rel": (d - d0).days, "arm": "none", "norm": "a", "r2": r2(state, onorm, t, mu, sd)})
        rows.append({"seed": si, "rel": (d - d0).days, "arm": "none", "norm": "b", "r2": r2(state, onorm, t, *link.zparams(t["xtr"]))})
    return si, state, onorm, (mu, sd), rows, fit_s


t = time.time()
with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
    SR = list(ex.map(seed_task, range(len(SEEDS))))
SEEDFIT = {si: (state, onorm, norm) for si, state, onorm, norm, _, _ in SR}
fits = np.array([r[5] for r in SR])
print(f"{len(SR)} seed LSTMs in {(time.time() - t) / 60:.1f} min; seconds per fit {fits.min():.0f} to {fits.max():.0f}")
FT = pd.DataFrame([row for r in SR for row in r[4]])
print("day-0 R2 of the seed decoders: mean %.3f, range %.3f to %.3f" % (
    FT[(FT["rel"] == 0) & (FT["norm"] == "a")]["r2"].mean(), FT[(FT["rel"] == 0) & (FT["norm"] == "a")]["r2"].min(),
    FT[(FT["rel"] == 0) & (FT["norm"] == "a")]["r2"].max()))""")

md("""## Continual fine-tuning

For each seed and each later day in date order, the current decoder is fine-tuned on the last 30, 120 or
300 s of that day's training trials, with 50, 250 or 500 iterations, the learning rate falling linearly
from 2e-4 to 1e-5, and the seed day's output normaliser kept (claim fig5b-finetune). The training noise
and the batch are those of the seed training (the criterion fixes the rest of the training as in
fig4a-sameday-stable). It is then evaluated on that day's hold-out. Input normalisation is (i) held at
the seed day's parameters, or (ii) refit on the fine-tuning samples of each day and used for that day's
hold-out, as continual_learning_lstm.py does (UPDATE_NEURAL_SCALER True).""")

code("""def chain_task(arg):
    si, dur, norm = arg
    t0 = time.time()
    state, onorm, (mu, sd) = SEEDFIT[si]
    nb, iters = DURATIONS[dur]
    iters = max(1, int(round(iters * FT_SCALE)))
    d0 = SEEDS[si]
    rows = []
    for d in LATER[d0]:
        t = SES[d]
        xf, yf = t["xtr"][-nb:], t["ytr"][-nb:]
        if norm == "ii":
            mu, sd = link.zparams(xf)
        state, _ = link.lstm_train([(z(xf, mu, sd), yf)], seed=42, iters=iters, init_state=state, out_norm=onorm)
        rows.append({"seed": si, "rel": (d - d0).days, "arm": f"{dur} s", "norm": norm, "r2": r2(state, onorm, t, mu, sd)})
    return rows, time.time() - t0, len(LATER[d0]) * iters


jobs = [(si, dur, "ii") for dur in (300, 120) for si in LONG_SEEDS]
jobs += sorted([(si, 30, norm) for si in range(len(SEEDS)) for norm in ("i", "ii")], key=lambda j: -len(LATER[SEEDS[j[0]]]))
t = time.time()
with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
    CH = list(ex.map(chain_task, jobs))
print(f"{len(jobs)} fine-tuning chains in {(time.time() - t) / 60:.1f} min; {sum(c[2] for c in CH)} iterations; "
      f"{sum(c[1] for c in CH) / sum(c[2] for c in CH):.3f} s per iteration (including evaluation) with four at once")
FT = pd.concat([FT, pd.DataFrame([row for c in CH for row in c[0]])], ignore_index=True)
print("evaluations:", FT.groupby(["arm", "norm"]).size().to_dict())""")

md("""## fig5b-finetune

> Continual daily fine-tuning of an LSTM on 30 s to 5 min of each new session's data, over up to 200 days
> from 20 seed days, reduces both short- and long-term decay, and with 120 s or 300 s later decoders
> outperform the day-0 decode.

Per relative day, the mean R2 across seeds; then the mean over relative days 1 to 10 and 100 to 200.""")

code("""def window_means(d, seeds=None):
    if seeds is not None:
        d = d[d["seed"].isin(seeds)]
    c = d.groupby("rel")["r2"].mean()
    return c.loc[1:10].mean(), c.loc[100:200].mean(), int(c.loc[1:10].size), int(c.loc[100:200].size)


cmp_ = {k: window_means(FT[(FT["arm"] == "none") & (FT["norm"] == k)]) for k in ("a", "b")}
ft30 = {k: window_means(FT[(FT["arm"] == "30 s") & (FT["norm"] == k)]) for k in ("i", "ii")}
rows = []
for fn in ("i", "ii"):
    for cn in ("a", "b"):
        rows.append({"fine-tuning norm": fn, "comparison": cn,
                     "30 s, days 1-10": ft30[fn][0], "comparison, days 1-10": cmp_[cn][0],
                     "30 s, days 100-200": ft30[fn][1], "comparison, days 100-200": cmp_[cn][1],
                     "30 s better in both": ft30[fn][0] > cmp_[cn][0] and ft30[fn][1] > cmp_[cn][1]})
print("30 s arm, all %d seeds (relative days with data: 1-10 %d, 100-200 %d):" % (len(SEEDS), ft30["i"][2], ft30["i"][3]))
print(pd.DataFrame(rows).round(3).to_string(index=False))
day0 = FT[(FT["arm"] == "none") & (FT["rel"] == 0) & (FT["norm"] == "a")].set_index("seed")["r2"]
print("mean day-0 R2 of the seed decoders: all %d seeds %.3f; the %d seeds with the long arms %.3f" % (
    len(day0), day0.mean(), len(LONG_SEEDS), day0.loc[LONG_SEEDS].mean()))
for arm in ("30 s", "120 s", "300 s"):
    for fn in ("i", "ii"):
        d = FT[(FT["arm"] == arm) & (FT["norm"] == fn)]
        if not len(d):
            continue
        n10, far, _, nfar = window_means(d, LONG_SEEDS)
        print(f"{arm}, norm ({fn}), the {len(LONG_SEEDS)} long-arm seeds: mean R2 days 1-10 {n10:.3f}, days 100-200 {far:.3f} "
              f"({nfar} relative days); above their mean day-0 R2 ({day0.loc[LONG_SEEDS].mean():.3f}): {far > day0.loc[LONG_SEEDS].mean()}")
print("per long-arm seed, mean R2 over days 100-200 against its own day-0 R2:")
for si in LONG_SEEDS:
    parts = []
    for arm in ("none", "30 s", "120 s", "300 s"):
        nm = "b" if arm == "none" else "ii"
        d = FT[(FT["arm"] == arm) & (FT["norm"] == nm) & (FT["seed"] == si) & FT["rel"].between(100, 200)]
        parts.append(f"{arm} {d['r2'].mean():.3f} (n {len(d)})")
    print(f"  seed {SEEDS[si].date()}: day 0 {day0.loc[si]:.3f}; " + ", ".join(parts))
fig, axs = plt.subplots(1, 2, figsize=(10, 3), sharey=True)
for ax, fn, cn in ((axs[0], "i", "a"), (axs[1], "ii", "b")):
    for arm, nm in (("none", cn), ("30 s", fn), ("120 s", fn), ("300 s", fn)):
        d = FT[(FT["arm"] == arm) & (FT["norm"] == nm)]
        if len(d):
            c = d.groupby("rel")["r2"].mean()
            ax.plot(c.index, c, ".", ms=3, label=f"{arm} ({nm})")
    ax.set_xlabel("days after the seed day"); ax.legend(fontsize=7)
axs[0].set_ylabel("mean R2"); axs[0].set_ylim(-2, 1); axs[1].set_ylim(-2, 1); plt.show()
allc = FT.groupby(["arm", "norm", "rel"])["r2"].mean()
print("plotted means: %.3f to %.3f; %d of %d below the axis floor of -2" % (allc.min(), allc.max(), (allc < -2).sum(), len(allc)))""", ["claim:fig5b-finetune"])

md("""**Result: ...**""")

md("""## Summary

| Claim | Outcome |
|---|---|
| fig5b-finetune | ... |
""")

code("""print(f"notebook time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")""")

nb.cells = C
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "finetune.ipynb")
PYEOF
cd entries/temmar-2025 && ../../executed/temmar-2025/.venv/bin/python $TMPDIR/mk_finetune.py && ls
```

```
README.md
__pycache__
decoding.ipynb
entry.yaml
finetune.ipynb
link.py
multiday.ipynb
requirements.in
requirements.lock.txt
signals.ipynb
```

**Agent calls Bash**

```bash
../../executed/temmar-2025/.venv/bin/python -c "import json;print(json.load(open('multiday.ipynb'))['metadata'])"; export LINK_DEV_ITERS=50 LINK_DEV_FTSCALE=0.1 LINK_DEV_NSEEDS=6; time ../../executed/temmar-2025/.venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR --output ft_dev.ipynb finetune.ipynb 2>&1 | tail -5; ../../executed/temmar-2025/.venv/bin/python - <<'EOF'
import json,os
d=json.load(open(os.environ['TMPDIR']+'/ft_dev.ipynb'))
for c in d['cells']:
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
EOF
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
[NbConvertApp] Converting notebook finetune.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 74033 bytes to /tmp/claude-1001/ft_dev.ipynb

real	9m8.574s
user	21m1.050s
sys	0m39.342s
312 sessions on 303 days; seed days in the dataset: 6 of 6
later days within 200 days, per seed: 32 to 85, 372 in all

loaded 138 days in 171 s; two-session days 1, CO used on 1; peak memory 1.79 GB

days loaded: 138 | by year: {2020: 25, 2021: 113} | styles: {'CO': 85, 'RD': 53}
training bins 17082 to 27756 (the 300 s arm uses the last 15000), hold-out bins 4199 to 7497
SBP (stored units): 0.056 to 250.587
  hold-out idx_pos: 0.000 to 1.000
  hold-out mrs_pos: 0.000 to 1.000
  hold-out idx_vel: -0.205 to 0.448
  hold-out mrs_vel: -0.407 to 0.341
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s = open('mk_finetune.py').read()
s = s.replace('EVAL_EVERY = 5     # score every 5th hold-out bin (cost), as in the other notebooks',
 'EVAL_EVERY = 10    # score every 10th hold-out bin (cost; a standard choice, the other notebooks use every 5th)')
open('mk_finetune.py','w').write(s)
EOF
grep -n "EVAL_EVERY = " mk_finetune.py; date -u
```

```
43:EVAL_EVERY = 10    # score every 10th hold-out bin (cost; a standard choice, the other notebooks use every 5th)
Thu Nov 12 16:24:25 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s = open('mk_finetune.py').read()
# parametrise
s = s.replace('import nbformat as nbf\n', 'import nbformat as nbf, sys\nMODE = sys.argv[1]\n')
s = s.replace('nbf.write(nb, "finetune.ipynb")', 'nbf.write(nb, "finetune.ipynb" if MODE == "30" else "finetune_long.ipynb")')
open('mk_finetune.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/mk_finetune.py <<'PYEOF'
import nbformat as nbf, sys
MODE = sys.argv[1]          # "30": finetune.ipynb; "long": finetune_long.ipynb
LONG = MODE == "long"
nb = nbf.v4.new_notebook()
C = []
def md(s): C.append(nbf.v4.new_markdown_cell(s))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s)
    if tags: c.metadata["tags"] = tags
    C.append(c)

HEAD = """Paper: doi:10.52202/085713-4642. Dataset: DANDI:001201, version 0.261026.1912, streamed (the most recent
published version; the paper cites none, and the three published versions hold the same assets, see
`signals.ipynb`). Claims file: `claims/temmar-2025.yaml`. Code read: github.com/chesteklab/LINK_dataset at
5e1c36a.
"""
if not LONG:
    md("# Temmar et al. (2025), LINK: continual fine-tuning, 30 s arm (Figure 5B)\n\n" + HEAD + """
| Claim | Here |
|---|---|
| fig5b-finetune | 30 s fine-tuning on all 20 seed days under both normalisation readings, and both comparisons; the 120 s and 300 s arms are in `finetune_long.ipynb` |

Why the claim is split. One LSTM iteration takes about 0.037 s with four fits at once (`decoding.ipynb`
and `multiday.ipynb` print the fit times), and scoring a hold-out about 0.75 s. The 20 seed days are
followed by 1146 sessions within 200 days. Fine-tuning is continual, so each seed's sessions are
fine-tuned one after the other. The 30 s arm (50 iterations per session) runs in full here under both
normalisation readings, about 40 minutes. The 120 s and 300 s arms (250 and 500 iterations per session)
would take about 3 hours under both readings, over the 60-minute limit of a notebook and the time of
this run; they run in `finetune_long.ipynb` on two of the 20 seed days under one reading. The 60 s arm
is not in the criterion and is not run.""")
else:
    md("# Temmar et al. (2025), LINK: continual fine-tuning, 120 s and 300 s arms (Figure 5B)\n\n" + HEAD + """
| Claim | Here |
|---|---|
| fig5b-finetune | the 120 s and 300 s arms, on 2 of the 20 seed days, under the code's normalisation (reading ii); the 30 s arm and the comparisons are in `finetune.ipynb` |

Why a subset. The 120 s and 300 s arms fine-tune each later session for 250 and 500 iterations, one
session after the other. On all 20 seed days under both normalisation readings that is about 1.2 million
iterations, about 3 hours at 0.037 s per iteration with four fits at once. Here they run on two seed days,
the 6th and 16th of the 20 (2021-05-05 and 2022-04-01, chosen before any result), under reading (ii), the
normalisation of continual_learning_lstm.py, about 30 minutes. Reading (i) is not run for these arms.""")

code(f"""import os, time, resource
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import link

T0 = time.time()
ITERS = int(os.environ.get("LINK_DEV_ITERS", link.LSTM_ITERS))       # 2000 (paper); lowered only while developing
FT_SCALE = float(os.environ.get("LINK_DEV_FTSCALE", "1"))            # 1 = the criterion's iterations; lowered only while developing
HORIZON = 200      # paper, Section 4.3: fine-tuned for up to 200 days after the seed day
EVAL_EVERY = 10    # score every 10th hold-out bin (cost; a standard choice, the other notebooks use every 5th)
# claim fig5b-finetune: the last 30, 120 or 300 s (1500, 6000, 15000 bins) of the training trials, 50, 250, 500 iterations
DURATIONS = {{30: (1500, 50), 120: (6000, 250), 300: (15000, 500)}}
# claim fig5b-finetune: STARTING_DAYS of continual_learning_lstm.py
STARTING_DAYS = ["2020-07-08", "2020-10-02", "2020-12-12", "2021-02-27", "2021-04-05", "2021-05-05", "2021-06-16",
                 "2021-07-09", "2021-07-29", "2021-08-19", "2021-09-14", "2021-10-27", "2022-01-17", "2022-02-21",
                 "2022-04-01", "2022-04-21", "2022-06-01", "2022-08-05", "2022-09-01", "2022-09-30"]
{"USE = [5, 15]      # the 6th and 16th seed days (see above)" if LONG else "USE = list(range(int(os.environ.get('LINK_DEV_NSEEDS', '20'))))   # all 20 seed days; fewer only while developing"}
SEEDS = [pd.Timestamp(STARTING_DAYS[i]) for i in USE]
A = link.assets()
dates = sorted(A["date"].unique())
print(f"{{len(A)}} sessions on {{len(dates)}} days; seed days used {{[d.date().isoformat() for d in SEEDS]}}, in the dataset: "
      f"{{sum(d in set(dates) for d in SEEDS)}} of {{len(SEEDS)}}")
LATER = {{d0: [d for d in dates if d0 < d <= d0 + pd.Timedelta(days=HORIZON)] for d0 in SEEDS}}
print("later days within 200 days, per seed: %d to %d, %d in all" % (
    min(map(len, LATER.values())), max(map(len, LATER.values())), sum(map(len, LATER.values()))))""")

md("""## Load the sessions needed

Every seed day and every day up to 200 days after it. On a day with two sessions the CO session is used
(claim fig5b-finetune). Each session is split into its first 300 trials (training) and the 75 after them
(hold-out), as in the other notebooks.""")

code("""need = sorted(set(SEEDS) | {d for v in LATER.values() for d in v})
rows_by_date = {d: A[A["date"] == d] for d in need}


def load(d):
    out = []
    for aid in rows_by_date[d]["asset_id"]:
        s = link.read_session(aid, tcr=False)
        (xtr, ytr), (xte, yte) = link.split(s)
        out.append({"date": d, "style": s["style"], "xtr": xtr, "ytr": ytr, "xte": xte, "yte": yte})
    co = [o for o in out if o["style"] == "CO"]
    return d, (co[0] if len(out) > 1 and co else out[0]), len(out)


t = time.time()
with ThreadPoolExecutor(4) as ex:
    loaded = list(ex.map(load, need))
SES = {d: s for d, s, _ in loaded}
two = [d for d, _, n in loaded if n > 1]
print(f"loaded {len(SES)} days in {time.time() - t:.0f} s; two-session days {len(two)}, CO used on "
      f"{sum(SES[d]['style'] == 'CO' for d in two)}; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")""")

code("""L5 = pd.DataFrame([{"date": d, "style": s["style"], "train_bins": len(s["xtr"]), "test_bins": len(s["xte"])} for d, s in SES.items()])
print("days loaded:", len(L5), "| by year:", L5["date"].dt.year.value_counts().sort_index().to_dict(),
      "| styles:", L5["style"].value_counts().to_dict())
print("training bins %d to %d (the 300 s arm uses the last 15000), hold-out bins %d to %d" % (
    L5["train_bins"].min(), L5["train_bins"].max(), L5["test_bins"].min(), L5["test_bins"].max()))
print("SBP (stored units): %.3f to %.3f" % (min(s["xte"].min() for s in SES.values()), max(s["xte"].max() for s in SES.values())))
yk = np.vstack([s["yte"] for s in SES.values()])
for n, a, b in zip(link.KIN_NAMES, yk.min(0), yk.max(0)):
    print(f"  hold-out {n}: {a:.3f} to {b:.3f}")""", ["sanity"])

if not LONG:
    md("""## Seed decoders, and the curves without fine-tuning

On each seed day an LSTM is trained as in `decoding.ipynb` (Appendix C.1: first 300 trials, input
z-scored on them, 2000 iterations, seed 42). Without fine-tuning it is then evaluated on the hold-out of
every later day within 200 days, under the two comparisons the criterion names: (a) input normalisation
held at the seed day's, the procedure of the single-session curve of fig5a-multiday-short-term; (b)
normalisation refit on the test day's training trials, the procedure of the LSTM curve of
fig4d-cross-day-decay. Both are computed here from these 20 seed decoders, so that the comparison has
the same seed days as the fine-tuning.""")
else:
    md("""## Seed decoders

On each of the two seed days an LSTM is trained as in `decoding.ipynb` and `finetune.ipynb` (Appendix
C.1: first 300 trials, input z-scored on them, 2000 iterations, seed 42), and scored on its own hold-out
(the day-0 decode) and, without fine-tuning, on each later day under reading (b) of the comparison.""")

code("""def z(x, mu, sd):
    return ((x - mu) / sd).astype(np.float32)


def r2(state, onorm, s, mu, sd):
    p = link.lstm_predict(state, onorm, z(s["xte"], mu, sd), every=EVAL_EVERY)
    return link.r2_per_output(s["yte"][::EVAL_EVERY], p).mean()


def seed_task(si):
    t0 = time.time()
    d0 = SEEDS[si]
    s = SES[d0]
    mu, sd = link.zparams(s["xtr"])
    state, onorm = link.lstm_train([(z(s["xtr"], mu, sd), s["ytr"])], seed=42, iters=ITERS)
    fit_s = time.time() - t0
    rows = [{"seed": si, "rel": 0, "arm": "none", "norm": norm, "r2": r2(state, onorm, s, mu, sd)} for norm in ("a", "b")]
    for d in LATER[d0]:
        t = SES[d]
        rows.append({"seed": si, "rel": (d - d0).days, "arm": "none", "norm": "b", "r2": r2(state, onorm, t, *link.zparams(t["xtr"]))})
        if NONE_A:
            rows.append({"seed": si, "rel": (d - d0).days, "arm": "none", "norm": "a", "r2": r2(state, onorm, t, mu, sd)})
    return si, state, onorm, (mu, sd), rows, fit_s


NONE_A = %s
t = time.time()
with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
    SR = list(ex.map(seed_task, range(len(SEEDS))))
SEEDFIT = {si: (state, onorm, norm) for si, state, onorm, norm, _, _ in SR}
fits = np.array([r[5] for r in SR])
print(f"{len(SR)} seed LSTMs in {(time.time() - t) / 60:.1f} min; seconds per fit {fits.min():.0f} to {fits.max():.0f}")
FT = pd.DataFrame([row for r in SR for row in r[4]])
d0r = FT[(FT["rel"] == 0) & (FT["norm"] == "a")]["r2"]
print("day-0 R2 of the seed decoders: mean %%.3f, range %%.3f to %%.3f" %% (d0r.mean(), d0r.min(), d0r.max()))""" % ("False" if LONG else "True"))

md("""## Continual fine-tuning

For each seed and each later day in date order, the current decoder is fine-tuned on the last 30, 120 or
300 s of that day's training trials, with 50, 250 or 500 iterations, the learning rate falling linearly
from 2e-4 to 1e-5, and the seed day's output normaliser kept (claim fig5b-finetune). The training noise
and the batch are those of the seed training, which the criterion fixes as in fig4a-sameday-stable; a
new Adam optimiser starts each day (a standard choice; the criterion does not say). The decoder is then
evaluated on that day's hold-out. Input normalisation is (i) held at the seed day's parameters, or (ii)
refit on the fine-tuning samples of each day and used for that day's hold-out, as
continual_learning_lstm.py does (UPDATE_NEURAL_SCALER True).""")

code("""def chain_task(arg):
    si, dur, norm = arg
    t0 = time.time()
    state, onorm, (mu, sd) = SEEDFIT[si]
    nb, iters = DURATIONS[dur]
    iters = max(1, int(round(iters * FT_SCALE)))
    d0 = SEEDS[si]
    rows = []
    for d in LATER[d0]:
        t = SES[d]
        xf, yf = t["xtr"][-nb:], t["ytr"][-nb:]
        if norm == "ii":
            mu, sd = link.zparams(xf)
        state, _ = link.lstm_train([(z(xf, mu, sd), yf)], seed=42, iters=iters, init_state=state, out_norm=onorm)
        rows.append({"seed": si, "rel": (d - d0).days, "arm": f"{dur} s", "norm": norm, "r2": r2(state, onorm, t, mu, sd)})
    return rows, time.time() - t0, len(LATER[d0]) * iters


%s
t = time.time()
with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
    CH = list(ex.map(chain_task, jobs))
print(f"{len(jobs)} fine-tuning chains in {(time.time() - t) / 60:.1f} min; {sum(c[2] for c in CH)} iterations; "
      f"{sum(c[1] for c in CH) / sum(c[2] for c in CH):.3f} s per iteration (including evaluation) with four at once")
FT = pd.concat([FT, pd.DataFrame([row for c in CH for row in c[0]])], ignore_index=True)
print("evaluations:", FT.groupby(["arm", "norm"]).size().to_dict())""" % (
    'jobs = [(si, dur, "ii") for dur in (300, 120) for si in range(len(SEEDS))]' if LONG else
    'jobs = sorted([(si, 30, norm) for si in range(len(SEEDS)) for norm in ("i", "ii")], key=lambda j: -len(LATER[SEEDS[j[0]]]))'))

md("""## fig5b-finetune%s

> Continual daily fine-tuning of an LSTM on 30 s to 5 min of each new session's data, over up to 200 days
> from 20 seed days, reduces both short- and long-term decay, and with 120 s or 300 s later decoders
> outperform the day-0 decode.

Per relative day, the mean R2 across seeds; then the mean over relative days 1 to 10 and 100 to 200.""" % (
    ": 120 s and 300 s" if LONG else ": 30 s"))

if not LONG:
    code("""def window_means(d):
    c = d.groupby("rel")["r2"].mean()
    return c.loc[1:10].mean(), c.loc[100:200].mean(), int(c.loc[1:10].size), int(c.loc[100:200].size)


cmp_ = {k: window_means(FT[(FT["arm"] == "none") & (FT["norm"] == k)]) for k in ("a", "b")}
ft30 = {k: window_means(FT[(FT["arm"] == "30 s") & (FT["norm"] == k)]) for k in ("i", "ii")}
rows = []
for fn in ("i", "ii"):
    for cn in ("a", "b"):
        rows.append({"fine-tuning norm": fn, "comparison": cn,
                     "30 s, days 1-10": ft30[fn][0], "comparison, days 1-10": cmp_[cn][0],
                     "30 s, days 100-200": ft30[fn][1], "comparison, days 100-200": cmp_[cn][1],
                     "30 s better in both": ft30[fn][0] > cmp_[cn][0] and ft30[fn][1] > cmp_[cn][1]})
print("30 s arm, %d seeds (relative days with data: 1-10 %d, 100-200 %d):" % (len(SEEDS), ft30["i"][2], ft30["i"][3]))
print(pd.DataFrame(rows).round(3).to_string(index=False))
day0 = FT[(FT["arm"] == "none") & (FT["rel"] == 0) & (FT["norm"] == "a")].set_index("seed")["r2"]
print("mean day-0 R2 of the %d seed decoders %.3f" % (len(day0), day0.mean()))
for fn in ("i", "ii"):
    print(f"30 s, norm ({fn}): mean R2 days 100-200 {ft30[fn][1]:.3f}, above the mean day-0 R2: {ft30[fn][1] > day0.mean()}")
per = FT[FT["rel"].between(1, 200)].pivot_table(index=["seed", "rel"], columns=["arm", "norm"], values="r2")
for fn, cn in (("i", "a"), ("ii", "b")):
    for lab, lo, hi in (("1-10", 1, 10), ("100-200", 100, 200)):
        d = per[per.index.get_level_values("rel").to_series().between(lo, hi).to_numpy()]
        diff = d[("30 s", fn)] - d[("none", cn)]
        print(f"paired, days {lab}, 30 s ({fn}) minus no fine-tuning ({cn}): {len(diff)} evaluations, higher in "
              f"{(diff > 0).mean():.3f}, mean difference {diff.mean():+.3f}")
fig, axs = plt.subplots(1, 2, figsize=(10, 3), sharey=True)
for ax, fn, cn in ((axs[0], "i", "a"), (axs[1], "ii", "b")):
    for arm, nm in (("none", cn), ("30 s", fn)):
        c = FT[(FT["arm"] == arm) & (FT["norm"] == nm)].groupby("rel")["r2"].mean()
        ax.plot(c.index, c, ".", ms=3, label=f"{arm} ({nm})")
    ax.set_xlabel("days after the seed day"); ax.legend(fontsize=7)
axs[0].set_ylabel("mean R2"); axs[0].set_ylim(-2, 1); plt.show()
allc = FT.groupby(["arm", "norm", "rel"])["r2"].mean()
print("plotted means: %.3f to %.3f; %d of %d below the axis floor of -2" % (allc.min(), allc.max(), (allc < -2).sum(), len(allc)))""", ["claim:fig5b-finetune"])
else:
    code("""day0 = FT[(FT["arm"] == "none") & (FT["rel"] == 0) & (FT["norm"] == "a")].set_index("seed")["r2"]
print("day-0 R2 of the 2 seed decoders:", {SEEDS[i].date().isoformat(): round(v, 3) for i, v in day0.items()}, "mean %.3f" % day0.mean())
rows = []
for arm, nm in (("none", "b"), ("120 s", "ii"), ("300 s", "ii")):
    d = FT[(FT["arm"] == arm) & (FT["norm"] == nm)]
    c = d.groupby("rel")["r2"].mean()
    rows.append({"arm": arm, "norm": nm, "mean R2 days 1-10": c.loc[1:10].mean(), "mean R2 days 100-200": c.loc[100:200].mean(),
                 "relative days 100-200": int(c.loc[100:200].size), "above mean day-0 R2": c.loc[100:200].mean() > day0.mean()})
    for si in range(len(SEEDS)):
        e = d[(d["seed"] == si) & d["rel"].between(100, 200)]
        rows.append({"arm": f"  seed {SEEDS[si].date()}", "norm": nm, "mean R2 days 1-10": d[(d["seed"] == si) & d["rel"].between(1, 10)]["r2"].mean(),
                     "mean R2 days 100-200": e["r2"].mean(), "relative days 100-200": len(e),
                     "above mean day-0 R2": e["r2"].mean() > day0.loc[si]})
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("(per seed, the comparison is with that seed's own day-0 R2)")
fig, ax = plt.subplots(figsize=(7, 3))
for arm, nm in (("none", "b"), ("120 s", "ii"), ("300 s", "ii")):
    c = FT[(FT["arm"] == arm) & (FT["norm"] == nm)].groupby("rel")["r2"].mean()
    ax.plot(c.index, c, ".", ms=3, label=f"{arm} ({nm})")
ax.axhline(day0.mean(), color="k", lw=0.8, label="mean day-0 R2")
ax.set_xlabel("days after the seed day"); ax.set_ylabel("mean R2"); ax.legend(fontsize=7); plt.show()
allc = FT.groupby(["arm", "norm", "rel"])["r2"].mean()
print("plotted means: %.3f to %.3f (axes auto-scaled, no point outside)" % (allc.min(), allc.max()))""", ["claim:fig5b-finetune"])

md("""**Result: ...**""")

md("""## Summary

| Claim | Outcome |
|---|---|
| fig5b-finetune | ... |
""")

code("""print(f"notebook time {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")""")

nb.cells = C
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "finetune.ipynb" if not LONG else "finetune_long.ipynb")
PYEOF
cd entries/temmar-2025 && P=../../executed/temmar-2025/.venv/bin/python && $P $TMPDIR/mk_finetune.py 30 && $P $TMPDIR/mk_finetune.py long && ls *.ipynb
```

```
decoding.ipynb
finetune.ipynb
finetune_long.ipynb
multiday.ipynb
signals.ipynb
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; P=../../executed/temmar-2025/.venv/bin/python; export LINK_DEV_ITERS=30 LINK_DEV_FTSCALE=0.05 LINK_DEV_NSEEDS=2; for n in finetune finetune_long; do $P -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR --output ${n}_dev.ipynb $n.ipynb 2>&1 | grep -v WARN | tail -3; $P - $n <<'EOF'
import json,os,sys
d=json.load(open(os.environ['TMPDIR']+f'/{sys.argv[1]}_dev.ipynb'))
for c in d['cells']:
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        if o.get('output_type')=='error': print(o['ename'], o['evalue'])
EOF
done; date -u
```

```
[NbConvertApp] Converting notebook finetune.ipynb to notebook
[NbConvertApp] Writing 56552 bytes to /tmp/claude-1001/finetune_dev.ipynb
312 sessions on 303 days; seed days used ['2020-07-08', '2020-10-02'], in the dataset: 2 of 2
later days within 200 days, per seed: 32 to 43, 75 in all

loaded 56 days in 70 s; two-session days 0, CO used on 0; peak memory 0.95 GB

days loaded: 56 | by year: {2020: 25, 2021: 31} | styles: {'CO': 38, 'RD': 18}
training bins 17082 to 27756 (the 300 s arm uses the last 15000), hold-out bins 4318 to 7497
SBP (stored units): 0.056 to 250.587
  hold-out idx_pos: 0.000 to 1.000
  hold-out mrs_pos: 0.000 to 1.000
  hold-out idx_vel: -0.205 to 0.448
  hold-out mrs_vel: -0.407 to 0.338

2 seed LSTMs in 0.2 min; seconds per fit 4 to 4
day-0 R2 of the seed decoders: mean 0.016, range 0.010 to 0.021

4 fine-tuning chains in 0.3 min; 300 iterations; 0.194 s per iteration (including evaluation) with four at once
evaluations: {('30 s', 'i'): 75, ('30 s', 'ii'): 75, ('none', 'a'): 77, ('none', 'b'): 77}
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; sed -i 's/the 6th and 16th of the 20 (2021-05-05 and 2022-04-01, chosen before any result)/the 6th and 16th of the 20 (2021-05-05 and 2022-04-21, chosen before any result)/' $TMPDIR/mk_finetune.py; grep -c "2022-04-21, chosen" $TMPDIR/mk_finetune.py; P=../../executed/temmar-2025/.venv/bin/python; $P $TMPDIR/mk_finetune.py 30 && $P $TMPDIR/mk_finetune.py long
```

```
1
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; cat > $TMPDIR/ed_multi.py <<'PYEOF'
import nbformat as nbf
nb = nbf.read("multiday.ipynb", as_version=4)
c = nb.cells
c[0].source = """# Temmar et al. (2025), LINK: multi-day training (Figure 5A)

Paper: doi:10.52202/085713-4642. Dataset: DANDI:001201, version 0.261026.1912, streamed (the most recent
published version; the paper cites none, and the three published versions hold the same assets, see
`signals.ipynb`). Claims file: `claims/temmar-2025.yaml`. Code read: github.com/chesteklab/LINK_dataset at
5e1c36a.

| Claim | Here |
|---|---|
| fig5a-multiday-short-term | tested on 12 day-0 sessions, 1 and 5 training sessions |
| fig5a-long-term-decay | tested on the same models |
| fig5b-finetune | in `finetune.ipynb` and `finetune_long.ipynb` |

Why a subset. Each LSTM takes about 75 s to train when four train at once on this runner (the cell
below prints the times). The paper trains 5 LSTMs on each of 283 day-0 sessions, 1415 fits, about 7.4
hours here with four at once, over the 60-minute limit of a notebook. The criteria of both Figure 5A
claims compare only 1 and 5 training sessions, so only those two are trained, on 12 day-0 sessions
spread evenly over the eligible ones, chosen before any result was seen: 24 fits."""
c[5].source = """## Train and evaluate

The LSTM and its training are those of `decoding.ipynb` (Appendix C.1). For k training sessions the
training bins of the k sessions are z-scored together (one mean and SD per channel), the windows never
cross a session boundary, and the model sees 2000 batches in all. Every model is then evaluated on the
hold-out trials of each session within 180 days after day 0, with input normalisation held at the
training parameters (Appendix C.1, "For the analyses in Figure 5"; norm "train"). As the variant the
criterion names, each model is also evaluated with the normalisation refit on the test session's
training trials, as the code's multi-day trainer does (norm "test"). The code variant's other
differences (90/10 split, no noise, skipping only the first 5 sessions) would need the models retrained
and are not run."""
c[6].source = c[6].source.replace(
"""        p = link.lstm_predict(state, onorm, ((s["xte"] - mu) / sd).astype(np.float32), every=EVAL_EVERY)
        rows.append({"day0": d0, "k": k, "test": s["date"], "rel": rel,
                     "r2": link.r2_per_output(s["yte"][::EVAL_EVERY], p).mean()})""",
"""        for norm, (m_, s_) in (("train", (mu, sd)), ("test", link.zparams(s["xtr"]))):
            p = link.lstm_predict(state, onorm, ((s["xte"] - m_) / s_).astype(np.float32), every=EVAL_EVERY)
            rows.append({"day0": d0, "k": k, "test": s["date"], "rel": rel, "norm": norm,
                         "r2": link.r2_per_output(s["yte"][::EVAL_EVERY], p).mean()})""")
c[6].source = c[6].source.replace('MD.groupby(["day0", "k"]).size().min(), MD.groupby(["day0", "k"]).size().max()',
                                  'MD.groupby(["day0", "k", "norm"]).size().min(), MD.groupby(["day0", "k", "norm"]).size().max()')
c[8].source = '''rows = []
CURVE = {}
for norm in ("train", "test"):
    M_ = MD[MD["norm"] == norm]
    curve = M_.groupby(["k", "rel"])["r2"].mean().unstack(0)
    CURVE[norm] = curve
    for k in (1, 5):
        c = curve[k].dropna()
        d0 = c.get(0, np.nan)
        near = c.loc[1:5].mean()
        rows.append({"norm": norm, "k": k, "day0 R2": d0, "mean R2 days 1-5": near, "drop": d0 - near,
                     "mean days 6-30": c.loc[6:30].mean(), "mean days 31-180": c.loc[31:180].mean(),
                     "relative days with data 1-5": int(c.loc[1:5].notna().sum())})
T = pd.DataFrame(rows)
print(T.round(4).to_string(index=False))
for norm in ("train", "test"):
    a, b = T[(T["norm"] == norm) & (T["k"] == 1)].iloc[0], T[(T["norm"] == norm) & (T["k"] == 5)].iloc[0]
    print(f"norm {norm}: days 1-5 higher with 5 sessions: {b['mean R2 days 1-5'] > a['mean R2 days 1-5']}; "
          f"drop smaller: {b['drop'] < a['drop']}; day 0 lower: {b['day0 R2'] < a['day0 R2']}")
for norm in ("train", "test"):
    per = MD[MD["norm"] == norm].pivot_table(index=["day0", "test"], columns="k", values="r2")
    per["rel"] = [(t - d).days for d, t in per.index]
    for lab, sel in (("day 0", per["rel"] == 0), ("days 1-5", per["rel"].between(1, 5)),
                     ("days 6-180", per["rel"].between(6, 180))):
        d = per[sel]
        print(f"norm {norm}, paired, {lab}: {len(d)} evaluations, 5 sessions higher in {(d[5] > d[1]).mean():.3f}, "
              f"mean difference {(d[5] - d[1]).mean():+.4f}")
per = MD[MD["norm"] == "train"].pivot_table(index=["day0", "test"], columns="k", values="r2")
per["rel"] = [(t - d).days for d, t in per.index]
print("per day 0 (day-0 R2, k=1 / k=5):")
print(per[per["rel"] == 0][[1, 5]].round(3).to_string())'''
c[11].source = '''def dexp(x, a, b, c, d):
    return a * np.exp(b * x) + c * np.exp(d * x)


P0 = {"criterion": {1: (0.374, 0.00365, 0.134, 0.140), 5: (0.374, 0.00365, 0.134, 0.140)},
      # the fitted curves printed in the Figure 5A panel (read from the figure, as the verifier reported them)
      "legend": {1: (0.229, -0.183, 0.268, -0.006), 5: (0.134, -0.140, 0.374, -0.004)}}
FITS = {}
for norm in ("train", "test"):
    for start in ("criterion", "legend"):
        fitres = {}
        for k in (1, 5):
            c = CURVE[norm][k].dropna()
            x = c.index.to_numpy(float)
            try:
                p, cov = curve_fit(dexp, x, c.to_numpy(), p0=P0[start][k], maxfev=10000)
                se = np.sqrt(np.diag(cov))
                fast, slow = (1, 3) if abs(p[1]) > abs(p[3]) else (3, 1)
                res = c.to_numpy() - dexp(x, *p)
                fitres[k] = {"params": p, "se": se, "fast": fast, "slow": slow, "drop5": dexp(0, *p) - dexp(5, *p),
                             "rmse": float(np.sqrt(np.mean(res ** 2)))}
                print(f"norm {norm}, start {start}, k={k}: a={p[0]:.4f} b={p[1]:.4f} c={p[2]:.4f} d={p[3]:.5f}; initial rate "
                      f"{p[fast]:.4f} (95% {p[fast] - 1.96 * se[fast]:.4f} to {p[fast] + 1.96 * se[fast]:.4f}); long-term rate "
                      f"{p[slow]:.5f} (95% {p[slow] - 1.96 * se[slow]:.5f} to {p[slow] + 1.96 * se[slow]:.5f}); predicted drop "
                      f"day 0 to 5 {fitres[k]['drop5']:.4f}; residual RMS {fitres[k]['rmse']:.4f}; points {len(c)}")
            except Exception as e:
                print(f"norm {norm}, start {start}, k={k}: fit failed: {e}")
        FITS[(norm, start)] = fitres
        if len(fitres) == 2:
            f1, f5 = fitres[1], fitres[5]
            lo = lambda f, j: f["params"][j] - 1.96 * f["se"][j]
            hi = lambda f, j: f["params"][j] + 1.96 * f["se"][j]
            overlap = not (hi(f1, f1["slow"]) < lo(f5, f5["slow"]) or hi(f5, f5["slow"]) < lo(f1, f1["slow"]))
            print(f"  norm {norm}, start {start}: initial rate more negative for k=1:", f1["params"][f1["fast"]] < f5["params"][f5["fast"]],
                  "| larger predicted drop to day 5 for k=1:", f1["drop5"] > f5["drop5"],
                  "| long-term rate intervals overlap:", overlap,
                  "| long-term rate difference (k=1 minus k=5): %.5f" % (f1["params"][f1["slow"]] - f5["params"][f5["slow"]]))
fig, axs = plt.subplots(1, 2, figsize=(11, 3))
for ax, norm in zip(axs, ("train", "test")):
    for k in (1, 5):
        c = CURVE[norm][k].dropna()
        ax.plot(c.index, c, ".", ms=3, label=f"{k} session(s)")
        if k in FITS[(norm, "criterion")]:
            xx = np.arange(0, HORIZON + 1)
            ax.plot(xx, dexp(xx, *FITS[(norm, "criterion")][k]["params"]))
    ax.set_title(f"normalisation: {norm} day"); ax.set_xlabel("days after day 0"); ax.set_ylabel("R2"); ax.legend()
plt.show()
for norm in ("train", "test"):
    print("plotted mean R2, norm %s: %.3f to %.3f" % (norm, np.nanmin(CURVE[norm].to_numpy()), np.nanmax(CURVE[norm].to_numpy())))'''
# drop the fig5b cells (13, 14, 15)
del c[13:16]
nbf.write(nb, "multiday.ipynb")
print([x.source[:40] for x in nb.cells])
PYEOF
../../executed/temmar-2025/.venv/bin/python $TMPDIR/ed_multi.py
```

```
['# Temmar et al. (2025), LINK: multi-day ', 'import os, time, resource\nimport numpy a', '## Load the sessions needed\n\nFor each da', 'need = set()\nfor i in day0_idx:\n    need', 'L3 = pd.DataFrame([{"date": v["date"], "', '## Train and evaluate\n\nThe LSTM and its ', 'def task(arg):\n    i, k = arg\n    t0 = t', '## fig5a-multiday-short-term\n\n> Training', 'rows = []\nCURVE = {}\nfor norm in ("train', '**Result: reproduced, on 12 day-0 sessio', '## fig5a-long-term-decay\n\n> Double-expon', 'def dexp(x, a, b, c, d):\n    return a * ', '**Result: not reproduced.** Fit to the m', '## Summary\n\n| Claim | Outcome |\n|---|---', 'print(f"notebook time {(time.time() - T0']
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/mk_finetune.py'
s=open(p).read()
s=s.replace('''Here they run on two seed days,
the 6th and 16th of the 20 (2021-05-05 and 2022-04-21, chosen before any result), under reading (ii), the
normalisation of continual_learning_lstm.py, about 30 minutes. Reading (i) is not run for these arms.''',
'''Here they run on four seed days,
the 1st, 6th, 11th and 16th of the 20 (2020-07-08, 2021-05-05, 2021-09-14 and 2022-04-21, chosen before
any result), under reading (ii), the normalisation of continual_learning_lstm.py, about 30 minutes.
Reading (i) is not run for these arms.''')
s=s.replace('| fig5b-finetune | the 120 s and 300 s arms, on 2 of the 20 seed days,','| fig5b-finetune | the 120 s and 300 s arms, on 4 of the 20 seed days,')
s=s.replace('they run in `finetune_long.ipynb` on two of the 20 seed days under one reading.','they run in `finetune_long.ipynb` on four of the 20 seed days under one reading.')
s=s.replace('USE = [5, 15]      # the 6th and 16th seed days (see above)','USE = [0, 5, 10, 15]   # the 1st, 6th, 11th and 16th seed days (see above)')
s=s.replace("""On each of the two seed days""","""On each of the four seed days""")
s=s.replace('''jobs = [(si, dur, "ii") for dur in (300, 120) for si in range(len(SEEDS))]''','''jobs = sorted([(si, dur, "ii") for dur in (300, 120) for si in range(len(SEEDS))], key=lambda j: -len(LATER[SEEDS[j[0]]]) * j[1])''')
s=s.replace('print("day-0 R2 of the 2 seed decoders:"','print("day-0 R2 of the 4 seed decoders:"')
open(p,'w').write(s)
EOF
grep -n "four seed\|USE = \|jobs = sorted" $TMPDIR/mk_finetune.py; P=../../executed/temmar-2025/.venv/bin/python; $P $TMPDIR/mk_finetune.py 30 && $P $TMPDIR/mk_finetune.py long
$P - <<'EOF'
import nbformat as nbf
nb = nbf.read("multiday.ipynb", as_version=4)
c=nb.cells
c[1].source=c[1].source.replace('N_DAY0 = int(os.environ.get("LINK_DEV_NDAY0", "12"))              # 12 day-0 sessions (see above)','N_DAY0 = int(os.environ.get("LINK_DEV_NDAY0", "24"))              # 24 day-0 sessions (see above)')
c[0].source=c[0].source.replace("tested on 12 day-0 sessions","tested on 24 day-0 sessions").replace("on 12 day-0 sessions\nspread evenly over the eligible ones, chosen before any result was seen: 24 fits.","on 24 day-0 sessions\nspread evenly over the eligible ones: 48 fits. (Round 1 of the verification used 12; the number was doubled\nafter it, as the verifier found 12 too few, and the 24 are chosen by the same rule.)")
print(c[0].source[-400:]); print(c[1].source)
nbf.write(nb,"multiday.ipynb")
EOF
```

```
39:iterations, about 3 hours at 0.037 s per iteration with four fits at once. Here they run on four seed days,
63:{"USE = [0, 5, 10, 15]   # the 1st, 6th, 11th and 16th seed days (see above)" if LONG else "USE = list(range(int(os.environ.get('LINK_DEV_NSEEDS', '20'))))   # all 20 seed days; fewer only while developing"}
124:On each of the four seed days an LSTM is trained as in `decoding.ipynb` and `finetune.ipynb` (Appendix
201:    'jobs = sorted([(si, dur, "ii") for dur in (300, 120) for si in range(len(SEEDS))], key=lambda j: -len(LATER[SEEDS[j[0]]]) * j[1])' if LONG else
202:    'jobs = sorted([(si, 30, norm) for si in range(len(SEEDS)) for norm in ("i", "ii")], key=lambda j: -len(LATER[SEEDS[j[0]]]))'))
out 7.4
hours here with four at once, over the 60-minute limit of a notebook. The criteria of both Figure 5A
claims compare only 1 and 5 training sessions, so only those two are trained, on 24 day-0 sessions
spread evenly over the eligible ones: 48 fits. (Round 1 of the verification used 12; the number was doubled
after it, as the verifier found 12 too few, and the 24 are chosen by the same rule.)
import os, time, resource
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from scipy.optimize import curve_fit
import link

T0 = time.time()
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; P=../../executed/temmar-2025/.venv/bin/python; export LINK_DEV_ITERS=20 LINK_DEV_NDAY0=3; $P -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR --output md_dev.ipynb multiday.ipynb 2>&1 | grep -v WARN | tail -2; $P - <<'EOF'
import json,os,sys
d=json.load(open(os.environ['TMPDIR']+'/md_dev.ipynb'))
for c in d['cells']:
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:3000])
        if o.get('output_type')=='error': print(o['ename'], o['evalue'])
EOF
date -u
```

```
[NbConvertApp] Converting notebook multiday.ipynb to notebook
[NbConvertApp] Writing 90971 bytes to /tmp/claude-1001/md_dev.ipynb
312 sessions; on single-session days 294; eligible day-0 sessions 283 (the Figure 5A legend reports 283 days)
day-0 sessions: ['2020-03-02', '2021-11-01', '2023-06-21']

loaded 78 sessions in 98 s; peak memory 1.17 GB

sessions loaded: 78 | by year: {2020: 20, 2021: 11, 2022: 41, 2023: 6}
training bins 17074 to 26945, test bins 4278 to 7134
SBP (stored units): 0.606 to 71.872
  hold-out idx_pos: 0.000 to 1.000
  hold-out mrs_pos: 0.000 to 1.000
  hold-out idx_vel: -0.249 to 0.448
  hold-out mrs_vel: -0.312 to 0.338

6 fits in 0.6 min; seconds per fit 2 to 6
days spanned by the 5 training sessions: 7 to 9
evaluations per model: 2 to 48

 norm  k  day0 R2  mean R2 days 1-5    drop  mean days 6-30  mean days 31-180  relative days with data 1-5
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; cat > $TMPDIR/ed_dec.py <<'PYEOF'
import nbformat as nbf
nb = nbf.read("decoding.ipynb", as_version=4)
c = nb.cells
assert c[0].source.startswith("# Temmar")
c[0].source = c[0].source.replace("""| fig4a-sameday-stable | RR on all 312 sessions, the LSTM on every 16th session |
| fig4a-lstm-beats-rr | on the LSTM sessions |""", """| fig4a-sameday-stable | RR on all 312 sessions, the LSTM on every 16th session |
| fig4a-lstm-beats-rr | on every session with an LSTM: every 16th, the 12 with the highest RR R2, and those of July to November 2022 |""")
c[0].source = c[0].source.replace("| fig2a-irregular-shifts | all days, with the R2 above |", "| fig2a-irregular-shifts | all days, with the R2 above and an LSTM on every session of July to November 2022 |")
old = c[0].source[c[0].source.index("Why a subset for the LSTM."):]
c[0].source = c[0].source.replace(old, """Why a subset for the LSTM. One LSTM of the paper's size (2000 iterations, batch 64, 20 bins, 300 hidden
units) takes about 77 s to train when four train at once on this runner (the cell below prints the time of
each fit). 312 of them, four at a time, take about 1.7 hours, over the 60-minute limit of a notebook. The
LSTM is therefore trained on every 16th session in date order (20 sessions), chosen before any result was
seen; the claims on trends and distributions over the dataset are tested on those. Two further sets are
added after round 1 of the verification, each chosen by a rule fixed before its result: the 12 sessions
with the highest RR R2 not already among the 20, where an LSTM is likeliest to fall below RR
(fig4a-lstm-beats-rr), and every session from July to November 2022 (fig2a-irregular-shifts). Ridge
regression is cheap and runs on every session.""")
# keep training data for every session (extra LSTMs are chosen after the RR fits)
c[3].source = c[3].source.replace("""    if i % LSTM_EVERY == 0:
        rec["xtr_z"] = ((xtr - mu) / sd).astype(np.float32)
        rec["ytr"] = ytr
    return rec""", """    rec["xtr_z"] = ((xtr - mu) / sd).astype(np.float32)   # kept for every session: the extra LSTMs are chosen after the RR fits
    rec["ytr"] = ytr
    return rec""")
assert "kept for every session" in c[3].source
# extra LSTMs after cell 7
extra_md = nbf.v4.new_markdown_cell("""## Further LSTMs

Same training, on the 12 sessions with the highest RR same-day R2 that are not among the 20, and on
every session from July to November 2022 that is not among them. They are scored on their own hold-out
only (no shuffles or cross-day tests).""")
extra_code = nbf.v4.new_code_cell("""rr_rank = sorted((s for s in SES if s["i"] not in set(LSTM_IDX)), key=lambda s: -s["r2_rr"].mean())
TOP_IDX = [s["i"] for s in rr_rank[:12]]
WIN_IDX = [s["i"] for s in SES if pd.Timestamp("2022-07-01") <= s["date"] <= pd.Timestamp("2022-11-30") and s["i"] not in set(LSTM_IDX)]
EXTRA_IDX = sorted(set(TOP_IDX) | set(WIN_IDX))
t = time.time()
with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
    XRES = list(ex.map(lstm_task, EXTRA_IDX, [42] * len(EXTRA_IDX), [False] * len(EXTRA_IDX)))
for r in XRES:
    SES_BY_I[r["i"]]["r2_lstm"] = r["r2"]
xf = np.array([r["fit_s"] for r in XRES])
print(f"{len(XRES)} further LSTMs ({len(TOP_IDX)} highest-RR sessions, {len(WIN_IDX)} July-November 2022 sessions, "
      f"{len(set(TOP_IDX) & set(WIN_IDX))} in both) in {(time.time() - t) / 60:.1f} min; seconds per fit {xf.min():.0f} to {xf.max():.0f}")
print("RR R2 of the 12 highest-RR sessions: %.3f to %.3f" % (min(SES_BY_I[i]["r2_rr"].mean() for i in TOP_IDX), max(SES_BY_I[i]["r2_rr"].mean() for i in TOP_IDX)))
for s in SES:
    s.pop("xtr_z", None); s.pop("ytr", None)""")
c.insert(8, extra_md); c.insert(9, extra_code)
# now indices shift by 2: fig4a-sameday code at 11
i = next(k for k, x in enumerate(c) if "claim:fig4a-sameday-stable" in x.metadata.get("tags", []))
s = c[i].source
s = s.replace('''L = SD.dropna(subset=["lstm"])''', '''SD["set"] = ["every 16th" if i in set(LSTM_IDX) else ("highest RR" if i in set(TOP_IDX) else "") for i in SD["i"]]
SD["window"] = SD["i"].isin(WIN_IDX) | (SD["date"].between("2022-07-01", "2022-11-30") & SD["i"].isin(LSTM_IDX))
LALL = SD.dropna(subset=["lstm"])
L = LALL[LALL["i"].isin(LSTM_IDX)]''')
s = s.replace('''print(f"Pearson r between RR and LSTM same-day R2 over {len(L)} sessions: {pc.statistic:.3f}, p = {pc.pvalue:.2g}")''',
'''print(f"Pearson r between RR and LSTM same-day R2 over {len(L)} sessions: {pc.statistic:.3f}, p = {pc.pvalue:.2g}")
pc2 = stats.pearsonr(LALL["rr"], LALL["lstm"])
print(f"variant, every session with an LSTM (n = {len(LALL)}, not a sample of the dataset: it adds the 12 highest-RR and the "
      f"July-November 2022 sessions): Pearson r {pc2.statistic:.3f}, p = {pc2.pvalue:.2g}")''')
c[i].source = s
i = next(k for k, x in enumerate(c) if "claim:fig4a-lstm-beats-rr" in x.metadata.get("tags", []))
c[i].source = c[i].source.replace('L = L.assign(diff=L["lstm"] - L["rr"])', '''L = LALL.assign(diff=LALL["lstm"] - LALL["rr"])
for lab, d in (("every 16th", L[L["i"].isin(LSTM_IDX)]), ("12 highest RR", L[L["i"].isin(TOP_IDX)]),
               ("July-November 2022", L[L["i"].isin(WIN_IDX)])):
    print(f"{lab}: {len(d)} sessions, LSTM above RR on {(d['diff'] > 0).sum()}, difference {d['diff'].min():.3f} to {d['diff'].max():.3f}")''')
c[i].source = c[i].source.replace('''print("sessions where RR is not below the LSTM:"''', '''print("highest RR R2 among the sessions with an LSTM: %.3f; highest over all 312: %.3f" % (L["rr"].max(), SD["rr"].max()))
print("sessions where RR is not below the LSTM:"''')
# suppc1
i = next(k for k, x in enumerate(c) if "claim:suppc1-shuffle-baseline" in x.metadata.get("tags", []))
c[i].source += '''
W = SH[SH["lstm_session"]].pivot_table(index="i", columns=["decoder", "reading"], values="r2")
tol = {"RR": (-0.166, 0.0166), "LSTM": (-0.156, 0.0156)}
for rd in ("a", "b", "trials"):
    inr = {d: (W[(d, rd)] - tol[d][0]).abs() <= tol[d][1] for d in tol}
    print(f"reading {rd}: of the {len(W)} LSTM sessions, RR within tolerance on {int(inr['RR'].sum())}, LSTM on "
          f"{int(inr['LSTM'].sum())}, both on {int((inr['RR'] & inr['LSTM']).sum())}")
rra = SH[(SH["decoder"] == "RR") & (SH["reading"] == "a")]["r2"]
print("RR, reading (a), all 312 sessions: within tolerance on %d (%.3f)" % (((rra + 0.166).abs() <= 0.0166).sum(), ((rra + 0.166).abs() <= 0.0166).mean()))'''
# fig2a
i = next(k for k, x in enumerate(c) if "claim:fig2a-irregular-shifts" in x.metadata.get("tags", []))
s = c[i].source
s = s.replace('''shifts = []
for d in DM.index:
    win = DM[(DM.index < d) & (DM.index >= d - pd.Timedelta(days=30))]
    if len(win) < 3:
        shifts.append(np.nan); continue
    med = win.median(); mad = (win - med).abs().median()
    shifts.append(int(((DM.loc[d] - med).abs() > 3 * mad.where(mad > 0, np.nan)).sum()))
SHF = pd.Series(shifts, index=DM.index)''', '''def shift_counts(by_sessions):
    out = []
    for n, d in enumerate(DM.index):
        if by_sessions:
            win = DM.iloc[max(0, n - 30):n]       # variant: the preceding 30 recording days
        else:
            win = DM[(DM.index < d) & (DM.index >= d - pd.Timedelta(days=30))]
        if len(win) < 3:
            out.append(np.nan); continue
        med = win.median(); mad = (win - med).abs().median()
        out.append(int(((DM.loc[d] - med).abs() > 3 * mad.where(mad > 0, np.nan)).sum()))
    return pd.Series(out, index=DM.index)


SHF = shift_counts(False)''')
s = s.replace('''w = (SD["date"] >= "2022-07-01") & (SD["date"] <= "2022-11-30")
for col, d in (("rr", SD), ("lstm", SD.dropna(subset=["lstm"]))):
    ww = (d["date"] >= "2022-07-01") & (d["date"] <= "2022-11-30")
    lo, hi = np.percentile(d[col], [10, 90])
    print(f"{col}: sessions in window {ww.sum()}, median R2 there {d.loc[ww, col].median():.3f}; "
          f"10th to 90th percentile over all {len(d)} sessions {lo:.3f} to {hi:.3f}")''', '''for lab, S_ in (("30 calendar days (main)", SHF), ("variant, 30 preceding recording days", shift_counts(True))):
    iw = (S_.index >= "2022-07-01") & (S_.index <= "2022-11-30")
    print(f"{lab}: shifting channels per day, median {S_[iw].median():.1f} in the window against {S_[~iw].median():.1f} outside; "
          f"days with >= 5: {(S_[iw] >= 5).mean():.3f} of window days, {(S_[~iw] >= 5).sum() / S_[~iw].notna().sum():.3f} of other days; "
          f"days with >= 20: {(S_[iw] >= 20).mean():.3f} and {(S_[~iw] >= 20).sum() / S_[~iw].notna().sum():.3f}")
print("shifting channels per day by quarter (median):", SHF.groupby(SHF.index.to_period("Q")).median().to_dict())
wsel = SD["date"].between("2022-07-01", "2022-11-30")
lo, hi = np.percentile(SD["rr"], [10, 90])
print(f"rr: sessions in window {wsel.sum()}, median R2 there {SD.loc[wsel, 'rr'].median():.3f}; "
      f"10th to 90th percentile over all {len(SD)} sessions {lo:.3f} to {hi:.3f}")
ev = SD[SD["i"].isin(LSTM_IDX)]
lo, hi = np.percentile(ev["lstm"], [10, 90])
lw = SD[wsel].dropna(subset=["lstm"])
print(f"lstm: sessions in window with an LSTM {len(lw)} of {wsel.sum()}, median R2 there {lw['lstm'].median():.3f}; "
      f"10th to 90th percentile over the {len(ev)} every-16th sessions (the sample of all sessions) {lo:.3f} to {hi:.3f}")
lw3 = lw[lw["i"].isin(LSTM_IDX)]
print(f"  as in round 1, the {len(lw3)} window sessions among the every-16th: median {lw3['lstm'].median():.3f}")
lo2, hi2 = np.percentile(LALL["lstm"], [10, 90])
print(f"  variant, percentiles over every session with an LSTM (n = {len(LALL)}): {lo2:.3f} to {hi2:.3f}")
print(f"  LSTM minus RR in the window: median {(lw['lstm'] - lw['rr']).median():.3f}; over the every-16th sessions {(ev['lstm'] - ev['rr']).median():.3f}")''')
c[i].source = s
nbf.write(nb, "decoding.ipynb")
print("ok")
PYEOF
../../executed/temmar-2025/.venv/bin/python $TMPDIR/ed_dec.py
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; ../../executed/temmar-2025/.venv/bin/python - <<'EOF'
import nbformat as nbf
nb = nbf.read("decoding.ipynb", as_version=4)
i = next(k for k, x in enumerate(nb.cells) if "claim:fig4a-lstm-beats-rr" in x.metadata.get("tags", []))
s = nb.cells[i].source
s = s.replace('L = LALL.assign(', 'LB = LALL.assign(').replace('L[L["i"]', 'LB[LB["i"]').replace('worse = L[L["diff"] <= 0]', 'worse = LB[LB["diff"] <= 0]')
s = s.replace("""f"LSTM above RR on {(L['diff'] > 0).sum()} of {len(L)} sessions ({(L['diff'] > 0).mean():.3f}); "
      f"difference median {L['diff'].median():.3f}, range {L['diff'].min():.3f} to {L['diff'].max():.3f}\"""",
 """f"LSTM above RR on {(LB['diff'] > 0).sum()} of {len(LB)} sessions ({(LB['diff'] > 0).mean():.3f}); "
      f"difference median {LB['diff'].median():.3f}, range {LB['diff'].min():.3f} to {LB['diff'].max():.3f}\"""")
s = s.replace('(L["rr"].max(), SD["rr"].max())', '(LB["rr"].max(), SD["rr"].max())')
nb.cells[i].source = s
print(s)
nbf.write(nb, "decoding.ipynb")
EOF
```

```
LB = LALL.assign(diff=LALL["lstm"] - LALL["rr"])
for lab, d in (("every 16th", LB[LB["i"].isin(LSTM_IDX)]), ("12 highest RR", LB[LB["i"].isin(TOP_IDX)]),
               ("July-November 2022", LB[LB["i"].isin(WIN_IDX)])):
    print(f"{lab}: {len(d)} sessions, LSTM above RR on {(d['diff'] > 0).sum()}, difference {d['diff'].min():.3f} to {d['diff'].max():.3f}")
worse = LB[LB["diff"] <= 0]
print(f"LSTM above RR on {(LB['diff'] > 0).sum()} of {len(LB)} sessions ({(LB['diff'] > 0).mean():.3f}); "
      f"difference median {LB['diff'].median():.3f}, range {LB['diff'].min():.3f} to {LB['diff'].max():.3f}")
print("highest RR R2 among the sessions with an LSTM: %.3f; highest over all 312: %.3f" % (LB["rr"].max(), SD["rr"].max()))
print("sessions where RR is not below the LSTM:", worse[["date", "style", "rr", "lstm"]].to_dict("records"))
if len(worse):
    with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
        extra = list(ex.map(lstm_task, [i for i in worse["i"] for _ in (1, 2)],
                            [sd_ for _ in worse["i"] for sd_ in (1, 2)], [False] * (2 * len(worse))))
    for r in extra:
        print(f"  session {SES_BY_I[r['i']]['date'].date()} seed {r['seed']}: LSTM R2 {r['r2'].mean():.3f} "
              f"(RR {SES_BY_I[r['i']]['r2_rr'].mean():.3f})")
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; P=../../executed/temmar-2025/.venv/bin/python; $P - <<'EOF'
import nbformat as nbf
nb = nbf.read("decoding.ipynb", as_version=4)
c = nb.cells[9]
c.source = c.source.replace('''
for s in SES:
    s.pop("xtr_z", None); s.pop("ytr", None)''', '')
assert "pop" not in c.source
nbf.write(nb, "decoding.ipynb")
EOF
export LINK_DEV_ITERS=20 LINK_SUBSET=40; $P -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR --output dec_dev.ipynb decoding.ipynb 2>&1 | grep -v WARN | tail -2; $P - <<'EOF'
import json,os,sys
d=json.load(open(os.environ['TMPDIR']+'/dec_dev.ipynb'))
for c in d['cells']:
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:2500])
        if o.get('output_type')=='error': print(o['ename'], o['evalue'])
EOF
date -u
```

```
[NbConvertApp] Converting notebook decoding.ipynb to notebook
[NbConvertApp] Writing 109453 bytes to /tmp/claude-1001/dec_dev.ipynb
40 sessions; LSTM iterations 20

loaded and fit RR on 40 sessions in 78 s; peak memory 1.61 GB
test trials per session: {75: 40} | test bins: 4130 to 6061
training bins: 16708 to 22975

sessions by style: {'RD': 24, 'CO': 16} | by year: {2020: 6, 2021: 15, 2022: 13, 2023: 6}
days: 40 | sessions with an LSTM: 3
test trials per session: {75: 40}
hold-out SBP (stored units, microvolts): 0.556 to 40.167
  hold-out idx_pos: 0.000 to 1.000
  hold-out mrs_pos: 0.000 to 1.000
  hold-out idx_vel: -0.286 to 0.359
  hold-out mrs_vel: -0.312 to 0.270
training-bin SD per channel: 0.139 to 14.088 (no channel constant)

same-day RR R2 (mean of 4 outputs): median 0.293, range 0.183 to 0.414

[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "executed\|clean-run\|STAMP\|markdown" tools/entry.py | head -40; cat executed/temmar-2025/.clean-run.json | head -20
```

```
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
27:directory. The executed copies
28:go to --output-dir (default: executed/<name>/, which git ignores). A notebook
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
31:a hash of everything the run read (`hash` prints it) and of each executed
36:(docs/protocol.md): the executed notebooks with the conclusions removed (every
37:markdown cell that begins "**Result:" and everything from the "## Summary"
39:executed/<name>/handover/. Run the entry first.
65:STAMP = ".clean-run.json"                 # beside the executed copies: what they were made from (entry_hash)
67:REUSE_DAYS = 30                           # executed copies older than this are made again
446:    """The text each claim-tagged cell of an executed notebook printed, by tag."""
463:    `before` (its executed notebooks). The entry moves to the new version only when nothing differs; otherwise
478:            differ.append(f"{nb['path']}: no earlier executed copy in {before} to compare with")
515:    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
518:        stamp = json.loads((output_dir / STAMP).read_text())
539:        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
540:              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
542:    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
581:        (output_dir / STAMP).write_text(json.dumps({
595:        if cell.cell_type == "markdown" and text.startswith("## Summary"):
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; P=../../executed/temmar-2025/.venv/bin/python; $P - <<'EOF'
import nbformat as nbf
nb = nbf.read("signals.ipynb", as_version=4)
c = nb.cells[55]
assert "fig3e" in nb.cells[54].source
c.source += '''
print("channel 47 in the electrodes table (Figure S1 places it on the medial array, row 5, column 5):",
      el.loc[47, ["id", "array_name", "bank", "row", "col"]].to_dict())
print("channels per array and bank:", el.groupby(["array_name", "bank"]).size().to_dict())'''
nbf.write(nb, "signals.ipynb")
nb = nbf.read("decoding.ipynb", as_version=4)
i = next(k for k, x in enumerate(nb.cells) if "claim:fig2a-irregular-shifts" in x.metadata.get("tags", []))
s = nb.cells[i].source
s = s.replace('''days with >= 5: {(S_[iw] >= 5).mean():.3f} of window days''', '''days with >= 5: {(S_[iw] >= 5).sum() / S_[iw].notna().sum():.3f} of window days''')
s = s.replace('''days with >= 20: {(S_[iw] >= 20).mean():.3f} and''', '''days with >= 20: {(S_[iw] >= 20).sum() / S_[iw].notna().sum():.3f} and''')
s = s.replace('''print("shifting channels per day by quarter (median):", SHF.groupby(SHF.index.to_period("Q")).median().to_dict())''',
 '''print("shifting channels per day by quarter (median):", {str(k): v for k, v in SHF.groupby(SHF.index.to_period("Q")).median().items()})''')
nb.cells[i].source = s
i = next(k for k, x in enumerate(nb.cells) if "claim:suppc1-shuffle-baseline" in x.metadata.get("tags", []))
nb.cells[i].source = nb.cells[i].source.replace('print("RR, reading (a), all 312 sessions: within tolerance on %d (%.3f)" % (', 'print("RR, reading (a), all %d sessions: within tolerance on %d (%.3f)" % (len(rra), ')
nbf.write(nb, "decoding.ipynb")
EOF
grep -n "of window days\|all %d sessions" decoding.ipynb | head; grep -n "channel 47" signals.ipynb
```

```
566:    "print(\"RR, reading (a), all %d sessions: within tolerance on %d (%.3f)\" % (len(rra), ((rra + 0.166).abs() <= 0.0166).sum(), ((rra + 0.166).abs() <= 0.0166).mean()))"
628:    "          f\"days with >= 5: {(S_[iw] >= 5).sum() / S_[iw].notna().sum():.3f} of window days, {(S_[~iw] >= 5).sum() / S_[~iw].notna().sum():.3f} of other days; \"\n",
1064:    "print(\"channel 47 in the electrodes table (Figure S1 places it on the medial array, row 5, column 5):\",\n",
1074:    "**Result: not reproduced.** With the arrays as the files label them, the medial channels' circular median angles are near -130 degrees (extension of both fingers): 2 of 64 (0.031) fall in the flexion sector of -22.5 to 112.5 degrees. Most lateral channels are tuned to flexion (12 to 88 degrees), and 2 of 32 (0.062) fall in the extension sector. The pattern is the paper's with the array names swapped: read that way, 81.2% of the file's lateral channels are in the flexion sector and 92.2% of its medial channels in the extension sector, though more of the flexion channels are within 45 degrees of IDX flexion (17) than of MRS flexion (11). The files' labels agree with Figure S1 (channel 47 is medial, row 5, column 5) and with the lower SBP of the lateral bank (figs4), so the files and this sentence of the paper disagree on which array is which, or the paper's angles have another sign convention."
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; python3 - <<'EOF'
s=open('entry.yaml').read()
s=s.replace("""same-day and cross-day decoding with ridge regression and an LSTM, and multi-day training. The LSTM
  analyses run on subsets of sessions for time, and the continual fine-tuning is too large to run.""","""same-day and cross-day decoding with ridge regression and an LSTM, multi-day training and continual
  fine-tuning. The LSTM analyses run on subsets of sessions for time; the 120 s and 300 s fine-tuning
  arms run on 4 of the 20 seed days.""")
s=s.replace("""- path: decoding.ipynb
  title: Same-day and cross-day decoding (Figure 4, Appendix C.1)
  runtime_minutes: 33
- path: multiday.ipynb
  title: Multi-day training and fine-tuning (Figure 5)
  runtime_minutes: 27""","""- path: decoding.ipynb
  title: Same-day and cross-day decoding (Figure 4, Appendix C.1)
  runtime_minutes: 40
- path: multiday.ipynb
  title: Multi-day training (Figure 5A)
  runtime_minutes: 30
- path: finetune.ipynb
  title: Continual fine-tuning, 30 s arm (Figure 5B)
  runtime_minutes: 45
- path: finetune_long.ipynb
  title: Continual fine-tuning, 120 s and 300 s arms on 4 seed days (Figure 5B)
  runtime_minutes: 35""")
open('entry.yaml','w').write(s)
EOF
grep -n "description" -A4 entry.yaml | head; cd ../..; python tools/entry.py check entries/temmar-2025 2>&1 | tail -20; date -u
```

```
5:description: Tests the findings of Temmar et al. (2025) on dandiset 001201, which holds 312 sessions of
6-  spiking-band power, threshold crossings and finger kinematics from one macaque over 3.5 years. It checks
7-  the dataset's counts and contents, the decline of neural signals over time, single-channel tuning,
8-  same-day and cross-day decoding with ridge regression and an LSTM, multi-day training and continual
9-  fine-tuning. The LSTM analyses run on subsets of sessions for time; the 120 s and 300 s fine-tuning
error: attempts/temmar-2025-01.yaml: no cell tagged 'claim:fig5b-finetune' in multiday.ipynb
1 error(s)
Thu Nov 12 16:40:03 UTC 2026
```

**Agent calls Bash**

```bash
cd  python tools/entry.py --help 2>&1 | head -20
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

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
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='attempts/temmar-2025-01.yaml'
s=open(p).read()
s=s.replace("""- claim: fig5b-finetune
  outcome: blocked
  blocked_by: too_large
  notebook: multiday.ipynb""","""- claim: fig5b-finetune
  outcome: blocked
  blocked_by: too_large
  notebook: finetune.ipynb""")
open(p,'w').write(s)
EOF
python tools/entry.py check entries/temmar-2025 2>&1 | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  unset LINK_DEV_ITERS LINK_SUBSET LINK_DEV_NDAY0 LINK_DEV_FTSCALE LINK_DEV_NSEEDS; env | grep LINK_; setsid nohup python tools/entry.py all entries/temmar-2025 > $TMPDIR/run.log 2>&1 < /dev/null & disown; sleep 20; cat $TMPDIR/run.log; ps aux | grep -c nbconvert; date -u
```

```
Installed kernelspec registry-temmar-2025 in executed/temmar-2025/.venv/share/jupyter/kernels/registry-temmar-2025
4
Thu Nov 12 16:41:02 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls paper; grep -n -i "impedance\|all categories\|0.54\|February\|2024" paper/*.txt | head -20; ls paper/*supp*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1168,1178p paper/*.txt; echo ---; sed -n 1216,1230p paper/*.txt; echo ---; sed -n 246,252p paper/*.txt; echo; sed -n 1412,1426p paper/*.txt; echo; sed -n 1300,1308p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "questions/temmar-2025.yaml",
 "content": "dandiset: \"001201\"\npaper: doi:10.52202/085713-4642\nquestions:\n- claim: figs5-active-inactive-slopes\n  asked: 2026-11-12\n  question: >-\n    The claim expects the inactive channels' slope to be +0.54e-3 per day, the sign as Appendix C.2\n    prints it. The same paragraph calls that slope \"near 0\", and Section 4.1 says \"All categories saw\n    steady decreases in average SBP over time\", which covers the active and inactive groups of Figure\n    S5. A positive slope is not a decrease, so the printed value may have lost its minus sign. Should\n    the expected value be -0.54e-3, or should the claim keep +0.54e-3 and record the conflict with\n    Section 4.1?\n  passage: >-\n    \"The slopes of the best-fit lines here were −1.29 × 10−3, and 0.54 × 10−3. As might be expected,\n    the slope for the inactive channels was near 0\" (Appendix C.2, paragraph after Figure S3); \"All\n    categories saw steady decreases in average SBP over time.\" (Section 4.1, paragraph 2).\n  why: >-\n    The data give -0.536e-3 per day for the inactive channels (channel-session points, stored values),\n    the printed size with the opposite sign. Against +0.54e-3 +- 0.054e-3 it is outside tolerance and\n    the claim is not reproduced; against -0.54e-3 it is inside, and with the active slope (-1.261e-3,\n    inside -1.29e-3 +- 0.129e-3) and the lower SBP of inactive channels the claim would be reproduced.\n- claim: fig3e-array-tuning\n  asked: 2026-11-12\n  question: >-\n    The criterion follows the sentence of Section 4.2: medial channels tuned to MRS flexion (some IDX\n    flexion), lateral channels to extension of both fingers. The verifier reports that the panels of\n    Figure 3E, which the claim cites as its source, show the reverse: the Lateral bank tuned to\n    flexion, and the Medial 1 and Medial 2 banks near -135 degrees (extension of both), and that Figure\n    3C agrees with the panels (channels 0 to 31 near 0 to 90 degrees, channels 32 to 95 near -135 to\n    -180). The claims file does not mention this contradiction. Should the claim follow the figure,\n    or keep the sentence and name the contradiction?\n  passage: >-\n    \"it appears that channels in the medial array (see Figure 1) are mainly tuned to MRS flexion, with\n    some IDX flexion, while channels in the lateral array are more tuned to extension of both DOF.\"\n    (Section 4.2, paragraph 1); Figure 3E legend, \"Per-channel tuning ranges across the dataset,\n    grouped by bank ... We separated each bank into separate plots.\"\n  why: >-\n    With the files' array labels (bank A = Lateral, which also gives the lowest SBP and the\n    shallowest slope of Figure S4, and places channel 47 on the medial array as Figure S1 does), 2 of\n    64 medial channels are in the flexion sector and 2 of 32 lateral channels in the extension sector,\n    so the claim as written is not reproduced. Read as the figure shows it, lateral channels tuned to\n    flexion and medial channels to extension, the data match: 81% of lateral channels are in the\n    flexion sector and 92% of medial channels in the extension sector.\n- claim: dataset-contents\n  asked: 2026-11-12\n  question: >-\n    The criterion asks for an electrodes table with an impedance column in every file, and partially\n    reproduces the claim when a few files lack a part. Appendix A.2 says that a session with no\n    impedance measured within three weeks has no impedances reported. Should the criterion accept a\n    session without impedances when none were measured within three weeks, as the paper describes the\n    deposit?\n  passage: >-\n    \"Each electrode is labeled with the impedance measurement closest in time to the date of the\n    session. If no impedances were recorded within three weeks of a session, no impedances are\n    reported for that session.\" (Appendix A.2); \"Impedance measurements as described above are\n    included in the imp column.\" (Appendix B.3, Electrodes).\n  why: >-\n    81 of 312 files have no imp column, and that alone makes the claim partially reproduced. Every\n    other part (the six series, the trials columns, bank, row and column, the 20 ms bins) is present\n    in every file. If a missing impedance is the documented behaviour, the claim would be reproduced,\n    provided the 81 sessions are the ones without a measurement within three weeks, which the files\n    do not let anyone check.\n- claim: dataset-sessions\n  asked: 2026-11-12\n  question: >-\n    The claims file's opening comment says the 312 sessions run from January 2020 to February 2024.\n    In Appendix B.1 that range describes the candidate days reviewed before curation (453 days), not\n    the final dataset. The final dataset spans 1,242 days (Section 3), which from January 2020 ends in\n    June 2023, and the files run from 2020-01-27 to 2023-06-22. Should the comment say the sessions run\n    from January 2020 to June 2023?\n  passage: >-\n    \"we reviewed all experimental notes from Monkey N from January 2020 ... to February 2024 ... After\n    this first pass, we were left with 453 days spanning from January 2020 to February 2024.\"\n    (Appendix B.1, Initial Candidate Selection); \"on 303 days spanning 1,242 days\" (Section 3).\n  why: >-\n    It cannot change an outcome: no criterion uses the end date. It misdescribes the data the paper\n    used, so a reader of the claims file would look for sessions after June 2023 that are not in the\n    dataset or the paper.\n"
}
```

```
File created successfully at: questions/temmar-2025.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -c transcripts/temmar-2025/verifier-1.md; head -c 3000 transcripts/temmar-2025/verifier-1.md; grep -o "api.dandiarchive[^ ]*" transcripts/temmar-2025/verifier-1.md | sort | uniq | head; cat $TMPDIR/run.log
```

````
32089 transcripts/temmar-2025/verifier-1.md
# temmar-2025 · verifier-1 · run 43245219974

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *claims* 2>/dev/null | head -300
```

```
total 444
drwxr-xr-x 6 runner runner    4096 Nov 12 16:00 .
drwxr-xr-x 8 runner runner    4096 Nov 12 16:00 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 15:12 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 15:12 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 12 16:00 .claude
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env.development
[... 40 more lines not kept]
````

**Agent calls Bash**

```bash
cd  grep -n -i "dandiarchive\|curl\|requests.get\|\.pdf\|synthetic\|import link" transcripts/temmar-2025/verifier-1.md | head -20
```

```
395: "file_path": "paper/10.52202-085713-4642.pdf",
407:d=fitz.open('paper/10.52202-085713-4642.pdf')
410:d=fitz.open('paper/10.52202-085713-4642.supp-Supplementary_Material.pdf')
444:d=fitz.open('paper/10.52202-085713-4642.pdf')
458:d=fitz.open('paper/10.52202-085713-4642.pdf')
461:s=fitz.open('paper/10.52202-085713-4642.supp-Supplementary_Material.pdf')
483:d=fitz.open('paper/10.52202-085713-4642.pdf')
512:import link, pandas as pd
533:d=fitz.open('paper/10.52202-085713-4642.pdf')
604:14. [does not affect a conclusion] I tested the helpers on synthetic inputs and they behave correctly: circ_median/circ_iqr across the ±180° wrap, channel_tuning (angle −135° recovered, lag 3 found), participation_ratio (about 5 for 5 independent channels), and trial_directions sectors. I found no train/test leakage in decoding: normalisers and output z-scoring are fitted on training bins only.
```

**Agent calls Bash**

```bash
cd  sed -n 505,530p transcripts/temmar-2025/verifier-1.md
```

````
Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import link, pandas as pd
A=link.assets(); print(len(A), A['size'].sum()/1e9,'GB', A['size'].min()/1e6, A['size'].max()/1e6)
S=['2020-07-08','2020-10-02','2020-12-12','2021-02-27','2021-04-05','2021-05-05','2021-06-16','2021-07-09','2021-07-29','2021-08-19','2021-09-14','2021-10-27','2022-01-17','2022-02-21','2022-04-01','2022-04-21','2022-06-01','2022-08-05','2022-09-01','2022-09-30']
d=set(A['date']); print(sum(pd.Timestamp(x) in d for x in S))
c=A.groupby('date').size(); print(c[c>1].index.date.tolist())
m=link.version_metadata(); print(m.get('assetsSummary'))
"
```

```
312 12.563287466 GB 33.98229 57.29309
20
[datetime.date(2021, 10, 15), datetime.date(2022, 2, 25), datetime.date(2022, 4, 8), datetime.date(2022, 4, 15), datetime.date(2022, 4, 29), datetime.date(2022, 5, 13), datetime.date(2022, 8, 10), datetime.date(2022, 9, 21), datetime.date(2022, 11, 2)]
{'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 12563287466, 'numberOfFiles': 312, 'numberOfSubjects': 1, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}
[... 5 more lines not kept]
````

**Agent calls Bash**

```bash
sleep 600; cat $TMPDIR/run.log; date -u
```

```
Installed kernelspec registry-temmar-2025 in executed/temmar-2025/.venv/share/jupyter/kernels/registry-temmar-2025
Thu Nov 12 16:51:53 UTC 2026
```

**Agent calls Bash**

```bash
sleep 240; cat $TMPDIR/run.log; date -u
```

```
Installed kernelspec registry-temmar-2025 in executed/temmar-2025/.venv/share/jupyter/kernels/registry-temmar-2025
Thu Nov 12 16:55:56 UTC 2026
```

**Agent calls Bash**

```bash
ps aux --sort=-%cpu | head -8 | cut -c1-200; ls -la executed/temmar-2025/
```

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
runner         1 60.0  0.0   3804  1492 ?        Ss   16:55   0:00 bwrap --new-session --die-with-parent --setenv GIT_CONFIG_KEY_0 safe.directory --setenv GIT_CONFIG_VALUE_0 
runner         2 50.0  0.0   9772  5452 ?        S    16:55   0:00 /bin/bash -c source /home/runner/.claude/shell-snapshots/snapshot-bash-1794499831408-7n6yh8.sh 2>/dev/null || true && export TMPDIR=/
runner         4  0.0  0.0   9964  4172 ?        R    16:55   0:00 ps aux --sort=-%cpu
runner         5  0.0  0.0  17596  7620 ?        S    16:55   0:00 head -8
runner         6  0.0  0.0  17536  7480 ?        S    16:55   0:00 cut -c1-200
total 396
drwxr-xr-x 3 runner runner   4096 Nov 12 16:40 .
drwxr-xr-x 3 runner runner   4096 Nov 12 16:10 ..
drwxr-xr-x 5 runner runner   4096 Nov 12 16:40 .venv
-rw-r--r-- 1 runner runner 113507 Nov 12 15:40 decoding.ipynb
-rw-r--r-- 1 runner runner  58387 Nov 12 15:55 multiday.ipynb
-rw-r--r-- 1 runner runner    343 Nov 12 15:55 result.json
-rw-r--r-- 1 runner runner 210975 Nov 12 15:21 signals.ipynb
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; ../../executed/temmar-2025/.venv/bin/python -c "
import link, pandas as pd
A=link.assets(); dates=sorted(A.date.unique())
S=['2020-07-08','2020-10-02','2020-12-12','2021-02-27','2021-04-05','2021-05-05','2021-06-16','2021-07-09','2021-07-29','2021-08-19','2021-09-14','2021-10-27','2022-01-17','2022-02-21','2022-04-01','2022-04-21','2022-06-01','2022-08-05','2022-09-01','2022-09-30']
for i,s in enumerate(S):
    d0=pd.Timestamp(s); L=[d for d in dates if d0<d<=d0+pd.Timedelta(days=200)]; print(i,s,len(L), sum(1 for d in L if (d-d0).days>=100))
"
```

```
0 2020-07-08 32 18
1 2020-10-02 43 27
2 2020-12-12 54 36
3 2021-02-27 85 53
4 2021-04-05 81 43
5 2021-05-05 77 32
6 2021-06-16 68 18
7 2021-07-09 63 19
8 2021-07-29 59 20
9 2021-08-19 52 22
10 2021-09-14 48 28
11 2021-10-27 57 37
12 2022-01-17 60 22
13 2022-02-21 64 29
14 2022-04-01 63 35
15 2022-04-21 57 35
16 2022-06-01 47 20
17 2022-08-05 50 16
18 2022-09-01 45 22
19 2022-09-30 41 30
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; P=../../executed/temmar-2025/.venv/bin/python; python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/mk_finetune.py'
s=open(p).read()
s=s.replace('''Here they run on four seed days,
the 1st, 6th, 11th and 16th of the 20 (2020-07-08, 2021-05-05, 2021-09-14 and 2022-04-21, chosen before
any result), under reading (ii), the normalisation of continual_learning_lstm.py, about 30 minutes.
Reading (i) is not run for these arms.''','''Here they run on two seed days,
the 3rd and 16th of the 20 (2020-12-12 and 2022-04-21, followed by 54 and 57 days within 200 days), under
reading (ii), the normalisation of continual_learning_lstm.py, about 25 minutes. The two were chosen
before any result, to lie apart in the dataset and to keep the longest chain short enough for the run's
time. Reading (i) is not run for these arms.''')
s=s.replace('| fig5b-finetune | the 120 s and 300 s arms, on 4 of the 20 seed days,','| fig5b-finetune | the 120 s and 300 s arms, on 2 of the 20 seed days,')
s=s.replace('they run in `finetune_long.ipynb` on four of the 20 seed days under one reading.','they run in `finetune_long.ipynb` on two of the 20 seed days under one reading.')
s=s.replace('USE = [0, 5, 10, 15]   # the 1st, 6th, 11th and 16th seed days (see above)','USE = [2, 15]      # the 3rd and 16th seed days (see above)')
s=s.replace("On each of the four seed days","On each of the two seed days")
s=s.replace('print("day-0 R2 of the 4 seed decoders:"','print("day-0 R2 of the 2 seed decoders:"')
open(p,'w').write(s)
EOF
grep -c "USE = \[2, 15\]" $TMPDIR/mk_finetune.py; $P $TMPDIR/mk_finetune.py 30 && $P $TMPDIR/mk_finetune.py long
$P - <<'EOF'
import nbformat as nbf
nb = nbf.read("multiday.ipynb", as_version=4)
c=nb.cells
c[1].source=c[1].source.replace('"24"))              # 24 day-0 sessions (see above)','"12"))              # 12 day-0 sessions (see above)')
c[0].source=c[0].source.replace("tested on 24 day-0 sessions","tested on 12 day-0 sessions").replace("on 24 day-0 sessions\nspread evenly over the eligible ones: 48 fits. (Round 1 of the verification used 12; the number was doubled\nafter it, as the verifier found 12 too few, and the 24 are chosen by the same rule.)","on 12 day-0 sessions\nspread evenly over the eligible ones, chosen before any result was seen: 24 fits.")
assert "12 day-0 sessions (see above)" in c[1].source and "24 fits." in c[0].source
nbf.write(nb,"multiday.ipynb")
nb = nbf.read("decoding.ipynb", as_version=4)
c=nb.cells
c[0].source=c[0].source.replace("| fig4a-lstm-beats-rr | on every session with an LSTM: every 16th, the 12 with the highest RR R2, and those of July to November 2022 |","| fig4a-lstm-beats-rr | on every session with an LSTM: every 16th, and the 12 with the highest RR R2 |")
c[0].source=c[0].source.replace("| fig2a-irregular-shifts | all days, with the R2 above and an LSTM on every session of July to November 2022 |","| fig2a-irregular-shifts | all days, with the R2 above |")
c[0].source=c[0].source.replace("""seen; the claims on trends and distributions over the dataset are tested on those. Two further sets are
added after round 1 of the verification, each chosen by a rule fixed before its result: the 12 sessions
with the highest RR R2 not already among the 20, where an LSTM is likeliest to fall below RR
(fig4a-lstm-beats-rr), and every session from July to November 2022 (fig2a-irregular-shifts). Ridge
regression is cheap and runs on every session.""","""seen; the claims on trends and distributions over the dataset are tested on those. After round 1 of the
verification, 12 sessions are added for fig4a-lstm-beats-rr: those with the highest RR R2 not already
among the 20, where an LSTM is likeliest to fall below RR, chosen by that rule before their result. An
LSTM on every session from July to November 2022 (42 more fits, about 14 minutes) did not fit in the
run's time with the fine-tuning of Figure 5B, and was not run. Ridge regression is cheap and runs on
every session.""")
c[8].source="""## Further LSTMs

Same training, on the 12 sessions with the highest RR same-day R2 that are not among the 20. They are
scored on their own hold-out only (no shuffles or cross-day tests)."""
c[9].source=c[9].source.replace("EXTRA_IDX = sorted(set(TOP_IDX) | set(WIN_IDX))","EXTRA_IDX = sorted(TOP_IDX)")
c[9].source=c[9].source.replace('''print(f"{len(XRES)} further LSTMs ({len(TOP_IDX)} highest-RR sessions, {len(WIN_IDX)} July-November 2022 sessions, "
      f"{len(set(TOP_IDX) & set(WIN_IDX))} in both) in {(time.time() - t) / 60:.1f} min; seconds per fit {xf.min():.0f} to {xf.max():.0f}")''','''print(f"{len(XRES)} further LSTMs on the highest-RR sessions ({len(set(TOP_IDX) & set(WIN_IDX))} of them in July to November 2022) "
      f"in {(time.time() - t) / 60:.1f} min; seconds per fit {xf.min():.0f} to {xf.max():.0f}")''')
assert "EXTRA_IDX = sorted(TOP_IDX)" in c[9].source and "further LSTMs on the highest" in c[9].source
nbf.write(nb,"decoding.ipynb")
EOF
grep -n "July-November 2022\", LB" decoding.ipynb | head -3; date -u
```

```
1
Thu Nov 12 16:56:56 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; P=../../executed/temmar-2025/.venv/bin/python; $P - <<'EOF'
import nbformat as nbf
nb = nbf.read("decoding.ipynb", as_version=4)
for c in nb.cells:
    c.source = c.source.replace('("July-November 2022", LB[LB["i"].isin(WIN_IDX)])', '("of these, in July-November 2022", LB[LB["i"].isin(WIN_IDX)])')
    c.source = c.source.replace('it adds the 12 highest-RR and the "\n      f"July-November 2022 sessions)', 'it adds the 12 highest-RR "\n      f"sessions)')
nbf.write(nb, "decoding.ipynb")
EOF
grep -n "of these, in July\|adds the 12" decoding.ipynb; sed -i 's/arms run on 4 of the 20 seed days./arms run on 2 of the 20 seed days./; s/120 s and 300 s arms on 4 seed days/120 s and 300 s arms on 2 seed days/' entry.yaml; python3 - <<'EOF'
s=open('entry.yaml').read()
s=s.replace("runtime_minutes: 40\n- path: multiday","runtime_minutes: 30\n- path: multiday").replace("title: Multi-day training (Figure 5A)\n  runtime_minutes: 30","title: Multi-day training (Figure 5A)\n  runtime_minutes: 20").replace("on 2 seed days (Figure 5B)\n  runtime_minutes: 35","on 2 seed days (Figure 5B)\n  runtime_minutes: 25")
open('entry.yaml','w').write(s)
EOF
sed -n 1,40p entry.yaml
```

```
314:    "print(f\"variant, every session with an LSTM (n = {len(LALL)}, not a sample of the dataset: it adds the 12 highest-RR \"\n",
356:    "               (\"of these, in July-November 2022\", LB[LB[\"i\"].isin(WIN_IDX)])):\n",
schema_version: 1
name: temmar-2025
type: reproduction
title: Long-term intracortical neural activity and kinematics, LINK (Temmar et al. 2025)
description: Tests the findings of Temmar et al. (2025) on dandiset 001201, which holds 312 sessions of
  spiking-band power, threshold crossings and finger kinematics from one macaque over 3.5 years. It checks
  the dataset's counts and contents, the decline of neural signals over time, single-channel tuning,
  same-day and cross-day decoding with ridge regression and an LSTM, multi-day training and continual
  fine-tuning. The LSTM analyses run on subsets of sessions for time; the 120 s and 300 s fine-tuning
  arms run on 2 of the 20 seed days.
license: Apache-2.0
python: "3.13"
notebooks:
- path: signals.ipynb
  title: The dataset, neural signals and tuning over time (Figures 2, 3, S2, S4, S5)
  runtime_minutes: 10
- path: decoding.ipynb
  title: Same-day and cross-day decoding (Figure 4, Appendix C.1)
[... 17 more lines not kept]
```

**Agent**

Starting the full run now in the foreground (estimated about 110 minutes).

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/temmar-2025 2>&1 | tail -30; date -u
```

```
Exit code 143
Command timed out after 2h 0m 0s
Thu Nov 12 16:57:08 UTC 2026
```

**Agent calls Bash**

```bash
cd  date -u; ls -la executed/temmar-2025/; cat executed/temmar-2025/result.json
```

```
Thu Nov 12 18:57:12 UTC 2026
total 440
drwxr-xr-x 3 runner runner   4096 Nov 12 16:57 .
drwxr-xr-x 3 runner runner   4096 Nov 12 16:10 ..
drwxr-xr-x 5 runner runner   4096 Nov 12 16:57 .venv
-rw-r--r-- 1 runner runner 121847 Nov 12 17:42 decoding.ipynb
-rw-r--r-- 1 runner runner  96747 Nov 12 18:05 multiday.ipynb
-rw-r--r-- 1 runner runner    343 Nov 12 15:55 result.json
-rw-r--r-- 1 runner runner 211653 Nov 12 17:06 signals.ipynb
{
 "entry": "temmar-2025",
 "python": "3.13",
 "results": [
  {
   "notebook": "signals.ipynb",
   "ok": true,
   "seconds": 544,
   "error": null
  },
  {
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  executed/temmar-2025/.venv/bin/python - <<'EOF'
import json
for nb in ['executed/temmar-2025/decoding.ipynb','executed/temmar-2025/multiday.ipynb']:
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        if c['cell_type']!='code': continue
        out=''
        for o in c.get('outputs',[]):
            if 'text' in o: out+=''.join(o['text'])
            elif o.get('output_type')=='error': out+=o['ename']+o['evalue']
        print(f"=== {nb[-15:]} [{i}]"); print(out[:4000])
d=json.load(open('executed/temmar-2025/signals.ipynb'))
for c in d['cells']:
    if 'channel 47' in ''.join(c['source']):
        for o in c.get('outputs',[]):
            if 'text' in o: print(''.join(o['text']))
EOF
```

```
=== /decoding.ipynb [1]
312 sessions; LSTM iterations 2000

=== /decoding.ipynb [3]
loaded and fit RR on 312 sessions in 610 s; peak memory 6.48 GB
test trials per session: {75: 312} | test bins: 4093 to 7497
training bins: 16632 to 27756

=== /decoding.ipynb [4]
sessions by style: {'CO': 156, 'RD': 156} | by year: {2020: 43, 2021: 117, 2022: 107, 2023: 45}
days: 303 | sessions with an LSTM: 20
test trials per session: {75: 312}
hold-out SBP (stored units, microvolts): 0.056 to 250.587
  hold-out idx_pos: 0.000 to 1.000
  hold-out mrs_pos: 0.000 to 1.000
  hold-out idx_vel: -0.290 to 0.448
  hold-out mrs_vel: -0.407 to 0.341
training-bin SD per channel: 0.137 to 14.173 (no channel constant)

=== /decoding.ipynb [5]
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; timeout 60 curl -sL "https://api.github.com/search/code?q=repo:chesteklab/LINK_dataset+curve_fit" | head -c 300; timeout 60 curl -sL "https://raw.githubusercontent.com/chesteklab/LINK_dataset/5e1c36a1282f90abb8d96963920a8b1fdd27a6e7/data_plotting/stability_plotter.ipynb" -o sp.ipynb; ls -la sp.ipynb; grep -o "def [a-z_]*exp[^\\\\]*\\\\n[^\\\\]*" sp.ipynb | head; grep -o "p0[^\\\\]*" sp.ipynb | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  rm entries/temmar-2025/finetune.ipynb entries/temmar-2025/finetune_long.ipynb; rm -rf entries/temmar-2025/__pycache__; python3 - <<'EOF'
p='entries/temmar-2025/entry.yaml'
s=open(p).read()
s=s.replace("""- path: finetune.ipynb
  title: Continual fine-tuning, 30 s arm (Figure 5B)
  runtime_minutes: 45
- path: finetune_long.ipynb
  title: Continual fine-tuning, 120 s and 300 s arms on 2 seed days (Figure 5B)
  runtime_minutes: 25
""","")
s=s.replace("""same-day and cross-day decoding with ridge regression and an LSTM, multi-day training and continual
  fine-tuning. The LSTM analyses run on subsets of sessions for time; the 120 s and 300 s fine-tuning
  arms run on 2 of the 20 seed days.""","""same-day and cross-day decoding with ridge regression and an LSTM, and multi-day training. The LSTM
  analyses run on subsets of sessions for time, and the continual fine-tuning is too large to run.""")
s=s.replace("runtime_minutes: 30\n- path: multiday","runtime_minutes: 36\n- path: multiday").replace("title: Multi-day training (Figure 5A)\n  runtime_minutes: 20","title: Multi-day training (Figure 5A; Figure 5B is not run)\n  runtime_minutes: 24")
open(p,'w').write(s)
p='attempts/temmar-2025-01.yaml'
s=open(p).read()
s=s.replace("""  blocked_by: too_large
  notebook: finetune.ipynb
  output: claim:fig5b-finetune
""","""  blocked_by: too_large
""")
open(p,'w').write(s)
EOF
python tools/entry.py check entries/temmar-2025 2>&1 | tail -5; git status --short
```

```
0 error(s)
 M attempts/temmar-2025-01.yaml
 M entries/temmar-2025/decoding.ipynb
 M entries/temmar-2025/entry.yaml
 M entries/temmar-2025/multiday.ipynb
 M entries/temmar-2025/signals.ipynb
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
 M tools/site_assets/progress.js
?? .bash_profile
?? .bashrc
?? .gitconfig
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; ../../executed/temmar-2025/.venv/bin/python - <<'EOF'
import nbformat as nbf
def res(nb, tag_after, text):
    i = next(k for k, x in enumerate(nb.cells) if tag_after in x.metadata.get("tags", []))
    j = i + 1
    assert nb.cells[j].cell_type == "markdown" and nb.cells[j].source.startswith("**Result:"), nb.cells[j].source[:50]
    nb.cells[j].source = text
# ---------------- decoding
nb = nbf.read("decoding.ipynb", as_version=4)
c0 = nb.cells[0]
c0.source = c0.source.replace("""units) takes about 77 s to train when four train at once on this runner (the cell below prints the time of
each fit). 312 of them, four at a time, take about 1.7 hours, over the 60-minute limit of a notebook.""", """units) takes 77 s (round 1) to 148 s (this run) to train when four train at once on this runner (the cell
below prints the time of each fit). 312 of them, four at a time, take 1.7 to 3.2 hours, over the 60-minute
limit of a notebook.""")
assert "148 s" in c0.source
res(nb, "claim:fig4a-sameday-stable", """**Result: reproduced, with the LSTM on 20 of 312 sessions.** Same-day R2 shows no decline: the RR slope over all 312 sessions is +0.0020 per year (p = 0.58) and the LSTM slope over its 20 every-16th sessions +0.0064 per year (p = 0.56). The two decoders' R2 correlate across those 20 sessions (Pearson r = 0.582, p = 0.007); over all 32 sessions with an LSTM, which add the 12 highest-RR sessions and so are not a sample of the dataset, r = 0.807 (p = 2.4e-08). RR without input normalisation, as the code fits it, gives the same slope (+0.0019 per year, p = 0.58). Median R2 is 0.296 for RR and 0.591 for the LSTM. The by-year LSTM medians include the 12 added sessions.""")
res(nb, "claim:fig4a-lstm-beats-rr", """**Result: reproduced on the 32 sessions tested.** The LSTM's same-day R2 is above RR's on 20 of 20 every-16th sessions (by 0.223 to 0.385) and on all 12 sessions with the highest RR R2 outside them (RR 0.390 to 0.467, LSTM higher by 0.182 to 0.300), 32 of 32 in all, so no session needed the extra seeds. The 12 include the session with the highest RR R2 of all 312 (0.467). The other 280 sessions were not tested with the LSTM.""")
res(nb, "claim:suppc1-shuffle-baseline", """**Result: partially reproduced.** Shuffled hold-out data give negative R2 for both decoders under every reading. Under reading (a), raw bins permuted, the LSTM's median over its 20 sessions is -0.154, within the tolerance of -0.156, but RR's median over 312 sessions is -0.223, outside the tolerance of -0.166 +- 0.0166. Single sessions can match: RR is within tolerance on 33 of 312 sessions (0.106), and of the 20 LSTM sessions RR is within tolerance on 1, the LSTM on 8, and both on 1. Under reading (b), whole windows permuted, the medians are -0.410 (RR) and -0.596 (LSTM), and whole trials give -0.409 and -0.533; no LSTM session has either value within tolerance under those readings.""")
res(nb, "claim:fig2a-irregular-shifts", """**Result: partially reproduced.** By the criterion's rule, 38 of 42 days from July to November 2022 have five or more channels shifting on the same day (up to 66), so the shift part holds. The rule does not single out that period: 0.974 of the window's days and 0.975 of the other days with a 30-day baseline have five or more, and the median count is 17 in the window against 20 outside; with the 30 preceding recording days as the baseline, 0.952 against 0.903 and 13 against 12. Decoding in the window: RR's median same-day R2 there (0.321, 45 sessions) is inside the 10th to 90th percentile range of all sessions (0.220 to 0.360). The LSTM's median over the 3 window sessions among the every-16th is 0.652, just above the 90th percentile of the 20 every-16th sessions (0.651), so that part fails, in the direction of better decoding. With the 3 window sessions among the 12 highest-RR sessions added, a selection biased towards high R2, the median is 0.659. The LSTM's margin over RR in the window (median 0.287) is close to its margin over the every-16th sessions (0.301).""")
for c in nb.cells:
    if c.cell_type == "markdown" and c.source.startswith("## Summary"):
        c.source = c.source.replace("| fig4a-lstm-beats-rr | reproduced on the 20 sessions tested |", "| fig4a-lstm-beats-rr | reproduced on the 32 sessions tested |")
        c.source = c.source.replace("the LSTM is trained on 20 of the 312 sessions (every 16th), for time;", "the LSTM is trained on 20 of the 312 sessions (every 16th), and on the 12 other sessions with the highest RR R2 for fig4a-lstm-beats-rr, for time;")
nbf.write(nb, "decoding.ipynb")
# ---------------- multiday
nb = nbf.read("multiday.ipynb", as_version=4)
c0 = nb.cells[0]
c0.source = c0.source.replace("| fig5b-finetune | in `finetune.ipynb` and `finetune_long.ipynb` |", "| fig5b-finetune | blocked, too large (see the attempt record) |")
c0.source = c0.source.replace("""Why a subset. Each LSTM takes about 75 s to train when four train at once on this runner (the cell
below prints the times). The paper trains 5 LSTMs on each of 283 day-0 sessions, 1415 fits, about 7.4
hours here with four at once,""", """Why a subset. Each LSTM takes 75 s (round 1) to 150 s (this run) to train when four train at once on
this runner (the cell below prints the times). The paper trains 5 LSTMs on each of 283 day-0 sessions,
1415 fits, 7 to 15 hours here with four at once,""")
assert "150 s" in c0.source and "blocked, too large (see" in c0.source
res(nb, "claim:fig5a-multiday-short-term", """**Result: reproduced, on 12 day-0 sessions, under both normalisations.** With input normalisation held at the training parameters (Appendix C.1, the criterion's reading), five training sessions against one raise the mean R2 over relative days 1 to 5 from -0.502 to -0.251, shrink the drop from day 0 to those days from 1.089 to 0.791, and lower day-0 R2 from 0.587 to 0.540 (lower on 11 of 12 day-0 sessions); paired over the 16 evaluations at 1 to 5 days, five sessions are better in 81% of them. With the normalisation refit on each test session, as the code's trainer does, the same three hold: 0.372 to 0.418 at days 1 to 5, a drop of 0.215 against 0.086, and day 0 lower, 0.587 against 0.503. Under that reading R2 after day 0 is positive (mean 0.27 over days 31 to 180 with five sessions), near the values of Figure 5A; under the training-day reading it is negative.""")
res(nb, "claim:fig5a-long-term-decay", """**Result: not reproduced, under the criterion's starting values; the outcome rests on them.** Started from the criterion's initial values (0.374, 0.00365, 0.134, 0.140), the fits with the training day's normalisation are degenerate: for one session a component of near-zero amplitude with rate 0.180 is the "initial" one, and for five sessions two components of opposing amplitude grow. The initial rate is not more negative for one session and the predicted drop to day 5 is not larger (-0.009 against 0.014). With the test day's normalisation the initial rate is still not more negative for one session (0.034 against 0.014), though the predicted drop is larger (0.006 against 0.003). Started from the values printed in the Figure 5A panel (negative rates), the fits have lower residuals and all three conditions hold under both normalisations: training day, initial rate -0.906 against -0.182, drop to day 5 1.237 against 0.416, long-term rates -0.0033 (-0.0057 to -0.0009) and 0.0010 (-0.0028 to 0.0049), intervals overlapping; test day, -0.601 against -0.535, drop 0.256 against 0.122, long-term rates -0.0046 (-0.0064 to -0.0029) and -0.0031 (-0.0041 to -0.0022), overlapping. The long-term intervals overlap in every fit. Residual RMS is 0.38 to 0.65 with the training day's normalisation and 0.09 to 0.11 with the test day's.""")
for c in nb.cells:
    if c.cell_type == "markdown" and c.source.startswith("## Summary"):
        c.source = """## Summary

| Claim | Outcome |
|---|---|
| fig5a-multiday-short-term | reproduced (12 day-0 sessions, both normalisations) |
| fig5a-long-term-decay | not reproduced under the criterion's starting values; reproduced from the starting values of the Figure 5A panel |
| fig5b-finetune | blocked, too large (not in this notebook) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's: 12 of the 283 day-0 sessions, and only 1 and 5 training sessions, for time; scored on every 5th test bin; of the code's variant of the multi-day trainer, only the refit of input normalisation on the test data is run (the 90/10 split and the training without noise are not).

What was found about the dataset: dropping the 9 two-session days, the first 10 sessions and the last session (which has no later session) leaves 283 day-0 sessions, the count in the Figure 5A legend."""
nbf.write(nb, "multiday.ipynb")
# ---------------- signals
nb = nbf.read("signals.ipynb", as_version=4)
for c in nb.cells:
    if c.cell_type == "markdown" and c.source.startswith("**Result: not reproduced.** With the arrays as the files label them"):
        c.source = c.source.replace("The files' labels agree with Figure S1 (channel 47 is medial, row 5, column 5)", "The files' labels agree with Figure S1 (the table gives channel 47 as Medial, bank B, row 5, column 5)")
        assert "bank B, row 5" in c.source
    if c.cell_type == "markdown" and c.source.startswith("## Summary"):
        c.source = c.source.replace("| figs5-active-inactive-slopes | partially reproduced (inactive slope of opposite sign) |", "| figs5-active-inactive-slopes | not reproduced (inactive slope of opposite sign; asked of a reader) |")
        c.source = c.source.replace("| fig3e-array-tuning | not reproduced |", "| fig3e-array-tuning | not reproduced (asked of a reader) |")
        c.source = c.source.replace("| fig5b-finetune | multiday.ipynb | blocked, too large |", "| fig5b-finetune | none | blocked, too large |")
    if c.cell_type == "markdown" and c.source.startswith("# Temmar"):
        c.source = c.source.replace("| fig5b-finetune | multiday.ipynb | blocked, too large |", "| fig5b-finetune | none | blocked, too large |")
nbf.write(nb, "signals.ipynb")
EOF
grep -n "figs5-active-inactive-slopes" signals.ipynb | head; grep -n "Result: partially reproduced\|Result: reproduced\|Result: not" signals.ipynb | grep -i "figs5\|inactive" | head
```

```
39:    "| figs5-active-inactive-slopes | this one | tested |\n",
716:    "## figs5-active-inactive-slopes\n",
731:     "claim:figs5-active-inactive-slopes"
1094:    "| figs5-active-inactive-slopes | not reproduced (inactive slope of opposite sign; asked of a reader) |\n",
757:    "**Result: partially reproduced.** With the stored values and channel-session points (fit reading a), the active channels' slope is -1.261e-03 per day, within the tolerance of -1.29e-3, and inactive channels have the lower mean SBP (2.15 against 3.74). The inactive slope is -5.36e-04: the size of the supplement's 0.54e-3, with the opposite sign, so it is outside the tolerance. The negative sign agrees with Section 4.1 (\"All categories saw steady decreases in average SBP\"). Fit reading (b) gives -1.162e-03 and -4.50e-04."
```

**Agent calls Bash**

```bash
cd entries/temmar-2025; ../../executed/temmar-2025/.venv/bin/python - <<'EOF'
import nbformat as nbf
nb = nbf.read("signals.ipynb", as_version=4)
for c in nb.cells:
    if c.cell_type == "markdown" and c.source.startswith("**Result: partially reproduced.** With the stored values and channel-session points"):
        c.source = c.source.replace("**Result: partially reproduced.**", "**Result: not reproduced.**") + " The criterion reproduces the claim only when both slopes are within tolerance and gives no partial outcome, so the opposite sign decides it. Whether the supplement's +0.54e-3 lost a minus sign is asked of a reader (questions/temmar-2025.yaml); against -0.54e-3 the claim would be reproduced."
nbf.write(nb, "signals.ipynb")
EOF
grep -c "lost a minus sign" signals.ipynb; date -u
```

```
1
Thu Nov 12 18:59:00 UTC 2026
```

**Agent calls Bash**

```bash
cd  cat >> questions/temmar-2025.yaml <<'EOF'
- claim: fig5a-long-term-decay
  asked: 2026-11-12
  question: >-
    The criterion fits a*exp(b*x) + c*exp(d*x) from initial values (0.374, 0.00365, 0.134, 0.140),
    which it gives as those of stability_plotter.ipynb. Both rates in these values are positive, so
    the fit starts from two growing components. The fitted curves printed in the Figure 5A panel, as
    the verifier read them, have negative rates (0.229e^-0.183x + 0.268e^-0.006x for one session and
    0.134e^-0.140x + 0.374e^-0.004x for five), and the initial values are the five-session
    coefficients with the signs of the rates dropped. That suggests the code fits a*exp(-b*x) +
    c*exp(-d*x), so that the criterion's form, or its initial values, misread the code. Should the
    criterion use the code's form, or start from negative rates?
  passage: >-
    "A double-exponential fit (Fig. 5A) to the single-session and 5-session conditions over all
    evaluation sessions (within 180 days of day 0) show steeper decays in the single-session case"
    (Section 4.3, paragraph 3), and the fitted equations printed in Figure 5A.
  why: >-
    From the criterion's initial values the fits are degenerate (a near-zero component with rate
    +0.18 for one session, two growing components for five) and the claim is not reproduced. Started
    from the panel's values, the fits have lower residuals and all three conditions of the criterion
    hold, under both normalisations (training day, initial rates -0.906 against -0.182, drop to day 5
    1.237 against 0.416, long-term intervals overlapping).
EOF
cd entries/temmar-2025; python3 - <<'EOF'
s=open('README.md').read()
s=s.replace("""| `multiday.ipynb` | multi-day training (Figure 5A) and the size of the fine-tuning (Figure 5B) |""","""| `multiday.ipynb` | multi-day training (Figure 5A) |""")
s=s.replace("""The LSTM is trained on 20 of the 312 sessions and the multi-day comparison on 12 of 283 day-0 sessions,
for time; the continual fine-tuning of Figure 5B is too large to run here.""","""The LSTM is trained on 20 of the 312 sessions (and on the 12 other sessions with the highest ridge
regression R2, for one claim) and the multi-day comparison on 12 of 283 day-0 sessions, for time; the
continual fine-tuning of Figure 5B is too large to run here.""")
open('README.md','w').write(s)
EOF
cat README.md | head -20
```

```
# Temmar et al. (2025), LINK, from dandiset 001201

Tests the findings of [Temmar et al. (2025)](https://doi.org/10.52202/085713-4642) on
[DANDI:001201](https://dandiarchive.org/dandiset/001201/0.261026.1912), which holds 312 sessions of
spiking-band power (SBP), threshold crossings and the kinematics of two finger groups from Monkey N,
recorded on 303 days over 3.5 years.

| Notebook | Claims |
|---|---|
| `signals.ipynb` | dataset counts and contents, throughput, SBP decline, active channels, participation ratio, bank and activity slopes, population drift, trajectories, tuning (Figures 2, 3, S2, S4, S5) |
| `decoding.ipynb` | same-day and cross-day decoding with ridge regression and an LSTM, the shuffle baseline, irregular SBP shifts (Figure 4, Appendix C.1) |
| `multiday.ipynb` | multi-day training (Figure 5A) |

The LSTM is trained on 20 of the 312 sessions (and on the 12 other sessions with the highest ridge
regression R2, for one claim) and the multi-day comparison on 12 of 283 day-0 sessions, for time; the
continual fine-tuning of Figure 5B is too large to run here. The outcomes, the reasons and
the differences from the paper's method are in the attempt record,
[`attempts/temmar-2025-01.yaml`](../../attempts/temmar-2025-01.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='attempts/temmar-2025-01.yaml'
s=open(p).read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n==count, (n,a[:80])
    s=s.replace(a,b)
old_dev="""  - The LSTM is trained on 20 of the 312 sessions (every 16th in date order, chosen before any result), for time;
    one fit takes about 194 s with four at once, so all 312 would take about 4.2 hours of fitting."""
new_dev="""  - The LSTM is trained on 20 of the 312 sessions (every 16th in date order, chosen before any result), for time;
    one fit takes 77 s (round 1) to 148 s (round 2) with four at once, so all 312 would take 1.7 to 3.2 hours of
    fitting, over the 60-minute limit of a notebook."""
rep(old_dev,new_dev,count=s.count(old_dev))
# fig2a
rep("""    a 30-day baseline, so it does not single out that period. RR's median same-day R2 in the window is 0.321 (45
    sessions), inside its 10th to 90th percentile range of 0.220 to 0.360. The LSTM's is 0.652 (3 sessions), just
    above its 90th percentile of 0.651 over 20 sessions, so that part fails, in the direction of better decoding.""",
"""    a 30-day baseline, so it does not single out that period (0.974 of window days and 0.975 of other days have
    five or more; median 17 shifting channels a day in the window against 20 outside; with the 30 preceding
    recording days as baseline, 0.952 against 0.903). RR's median same-day R2 in the window is 0.321 (45
    sessions), inside its 10th to 90th percentile range of 0.220 to 0.360. The LSTM's is 0.652 (3 sessions), just
    above its 90th percentile of 0.651 over 20 sessions, so that part fails, by 0.001, in the direction of better
    decoding. Adding the 3 window sessions among the 12 highest-RR sessions, a selection biased towards high R2,
    gives 0.659. An LSTM on all 45 window sessions was not run, for time.""")
# figs5
rep("""- claim: figs5-active-inactive-slopes
  outcome: partially_reproduced""","""- claim: figs5-active-inactive-slopes
  outcome: not_reproduced""")
rep("""    are -1.162e-03 and -4.50e-04.
  deviations:
  - Each session classifies""","""    are -1.162e-03 and -4.50e-04. The criterion reproduces the claim only when both slopes are within tolerance
    and names no partial outcome, so the inactive slope decides it. Whether the supplement's +0.54e-3 lost its
    minus sign is asked of a reader in questions/temmar-2025.yaml; against -0.54e-3 the claim would be reproduced.
  deviations:
  - Each session classifies""")
# fig3e
rep("""Figure S1 (channel 47 medial, row 5, column 5) and with Figure S4""","""Figure S1 (the electrodes table gives channel 47 as Medial, bank B, row 5, column 5) and with Figure S4""")
rep("""    is between the files and this sentence of the paper, or a sign convention of the paper's tuning angles.
  deviations:""","""    is between the files and this sentence of the paper, or a sign convention of the paper's tuning angles. The
    verifier reports that the panels of Figure 3E and Figure 3C show the files' pattern, so the sentence of Section
    4.2 and the figure disagree; whether the claim should follow the figure is asked of a reader.
  deviations:""")
# fig4a-sameday
rep("""    Pearson r between the two over the 20 sessions 0.582 (p = 0.007). RR without input normalisation, as the code
    fits it, gives +0.0019 per year (p = 0.58). Median R2, RR 0.296, LSTM 0.591.""","""    Pearson r between the two over the 20 sessions 0.582 (p = 0.007); over all 32 sessions with an LSTM, which add
    the 12 highest-RR sessions and are not a sample of the dataset, r = 0.807 (p = 2.4e-08). RR without input
    normalisation, as the code fits it, gives +0.0019 per year (p = 0.58). Median R2, RR 0.296, LSTM 0.591.""")
# lstm beats
rep("""  notes: LSTM above RR on 20 of 20 sessions, by 0.223 to 0.385 (median 0.301), so no extra seeds were needed. RR's
    highest same-day R2 over all 312 sessions, 0.467, is below the lowest LSTM R2 seen, 0.514; the other 292 sessions
    were not tested with the LSTM.""","""  notes: LSTM above RR on 20 of 20 every-16th sessions, by 0.223 to 0.385, and on all 12 of the other sessions with
    the highest RR R2 (RR 0.390 to 0.467, LSTM higher by 0.182 to 0.300), 32 of 32 in all, so no extra seeds were
    needed. The 12 include the session with the highest RR R2 of all 312 (0.467). The other 280 sessions were not
    tested with the LSTM.""")
i=s.index("- claim: fig4a-lstm-beats-rr")
j=s.index("- claim: fig4bc-dof-accuracy")
blk=s[i:j]
blk2=blk.replace(new_dev, new_dev+"""
  - The 12 sessions with the highest RR same-day R2 outside the 20 were added after round 1 of the verification,
    chosen by that rule before their LSTM result, as the sessions where the LSTM is likeliest to fall below RR.""")
s=s[:i]+blk2+s[j:]
# fig4d
rep("""    and with the signed offset and test-day normalisation the sharp-then-stable part fails. With the training
    day's normalisation RR's mean R2 is -13.4 to -17.9 past day 0.""","""    and with the signed offset and test-day normalisation the sharp-then-stable part fails. With the training
    day's normalisation RR's mean R2 is -13.4 to -17.9 past day 0. The pass is narrow: the LSTM's early drop
    exceeds its later drop by 0.017 (0.207 against 0.190) and r exceeds 0.9 by 0.003, over 20 decoders.""")
# fig2d
rep("""    would. 2020Q2 has one session.'""","""    would. 2020Q2 has one session. The failure is marginal: 2023Q2 is 25.5% from the median.'""")
# suppc1
rep("""    to -0.149). Reading (b) gives -0.410 (RR) and -0.596 (LSTM); whole trials give -0.409 and -0.533.""","""    to -0.149). Reading (b) gives -0.410 (RR) and -0.596 (LSTM); whole trials give -0.409 and -0.533. As the
    paper used one session, single sessions were counted: under (a) RR is within tolerance on 33 of 312 sessions,
    and of the 20 LSTM sessions RR is within tolerance on 1, the LSTM on 8 and both on 1; under (b) and whole
    trials, none.""")
# fig5a short
rep("""    on 11 of 12). R2 after day 0 is negative because input normalisation is held at the training parameters. 283
    day-0 sessions are eligible, as the legend reports, when the last session, with nothing after it, is left out.
  deviations:
  - 12 of the 283 day-0 sessions, evenly spaced and chosen before any result, and only 1 and 5 training sessions
    (the two the criterion compares), for time; the paper trains 1415 LSTMs, about 19 hours here.
  - Scored on every 5th test bin; the code's variant of the multi-day trainer was not run.""","""    on 11 of 12). R2 after day 0 is negative because input normalisation is held at the training parameters. With
    the normalisation refit on each test session, the code's variant, the three also hold (days 1 to 5, 0.372 to
    0.418; drop 0.215 against 0.086; day 0, 0.587 against 0.503), and R2 after day 0 is positive (0.18 to 0.42),
    near Figure 5A. 283 day-0 sessions are eligible, as the legend reports, when the last session, with nothing
    after it, is left out.
  deviations:
  - 12 of the 283 day-0 sessions, evenly spaced and chosen before any result, and only 1 and 5 training sessions
    (the two the criterion compares), for time; the paper trains 1415 LSTMs, 7 to 15 hours here.
  - Scored on every 5th test bin. Of the code's variant of the multi-day trainer, the refit of input
    normalisation on the test data is run; its 90/10 split and training without noise would need the models
    retrained and are not.""")
# fig5a long
rep("""    likely too noisy for this fit; the raw comparison of fig5a-multiday-short-term does show the smaller early drop
    with five sessions.
  deviations:""","""    likely too noisy for this fit; the raw comparison of fig5a-multiday-short-term does show the smaller early drop
    with five sessions. Two variants were run after round 1 of the verification. With the test day's
    normalisation and the criterion's initial values, the initial rate is still not more negative for one session
    (0.034 against 0.014). Started from the values printed in the Figure 5A panel (negative rates), the fits have
    lower residuals and all three conditions hold under both normalisations (training day, initial rates -0.906
    against -0.182, drop to day 5 1.237 against 0.416, long-term rates -0.0033 and 0.0010 with overlapping
    intervals; test day, -0.601 against -0.535, drop 0.256 against 0.122, long-term rates -0.0046 and -0.0031,
    overlapping). The outcome is the criterion's and rests on its initial values, which start from growing
    components; whether they misread the code is asked of a reader.
  deviations:""")
# fig5b
rep("""  notes: Estimated from the 20 seed days, 32 to 85 later sessions each within 200 days (1146 in all), the four durations'
    iterations and the two normalisation readings, 2,446,600 training iterations, about 16.5 hours at the measured
    0.097 s per iteration with four fits at once, beyond the 60-minute notebook limit and the run. Not run.""","""  notes: The 20 seed days are in the dataset and are followed by 32 to 85 sessions each within 200 days (1146 in
    all). With the four durations' iterations and the two normalisation readings this is 2,446,600 training
    iterations, 6.3 hours at the 0.037 s per iteration measured in round 1 with four fits at once, and twice that
    at round 2's fit times (148 s per 2000 iterations), beyond the 60-minute notebook limit and the run. The 30 s
    arm alone (20 seed fits and 1146 fine-tunes of 50 iterations, under both readings) was written as a notebook
    after round 1 and started in this run; it had not finished after 52 minutes and was stopped by the run's time
    limit, so it is not in the entry and supplies no number. The 120 s and 300 s arms on 2 seed days were not
    started. No part was tested.""")
open(p,'w').write(s)
EOF
python tools/entry.py check entries/temmar-2025 2>&1 | tail -3; date -u
```

```
Traceback (most recent call last):
  File "<stdin>", line 63, in <module>
  File "<stdin>", line 6, in rep
AssertionError: (0, '    and with the signed offset and test-day normalisation the sharp-then-stable ')
0 error(s)
Thu Nov 12 18:59:51 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -n "13.4 to -17.9\|2020Q2 has one\|whole trials give -0.409\|on 11 of 12). R2\|smaller early drop\|16.5 hours" attempts/temmar-2025-01.yaml
```

```
147:    would. 2020Q2 has one session.'
245:    day's normalisation RR's mean R2 is -13.4 to -17.9 past day 0.
261:    to -0.149). Reading (b) gives -0.410 (RR) and -0.596 (LSTM); whole trials give -0.409 and -0.533.
272:    on 11 of 12). R2 after day 0 is negative because input normalisation is held at the training parameters. 283
288:    likely too noisy for this fit; the raw comparison of fig5a-multiday-short-term does show the smaller early drop
297:    iterations and the two normalisation readings, 2,446,600 training iterations, about 16.5 hours at the measured
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec1.py <<'EOF'
p='attempts/temmar-2025-01.yaml'
s=open(p).read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n==count, (n,a[:80])
    s=s.replace(a,b)
old_dev="""  - The LSTM is trained on 20 of the 312 sessions (every 16th in date order, chosen before any result), for time;
    one fit takes about 194 s with four at once, so all 312 would take about 4.2 hours of fitting."""
new_dev="""  - The LSTM is trained on 20 of the 312 sessions (every 16th in date order, chosen before any result), for time;
    one fit takes 77 s (round 1) to 148 s (round 2) with four at once, so all 312 would take 1.7 to 3.2 hours of
    fitting, over the 60-minute limit of a notebook."""
rep(old_dev,new_dev,count=s.count(old_dev))
rep("""    a 30-day baseline, so it does not single out that period. RR's median same-day R2 in the window is 0.321 (45
    sessions), inside its 10th to 90th percentile range of 0.220 to 0.360. The LSTM's is 0.652 (3 sessions), just
    above its 90th percentile of 0.651 over 20 sessions, so that part fails, in the direction of better decoding.""",
"""    a 30-day baseline, so it does not single out that period (0.974 of window days and 0.975 of other days have
    five or more; median 17 shifting channels a day in the window against 20 outside; with the 30 preceding
    recording days as baseline, 0.952 against 0.903). RR's median same-day R2 in the window is 0.321 (45
    sessions), inside its 10th to 90th percentile range of 0.220 to 0.360. The LSTM's is 0.652 (3 sessions), just
    above its 90th percentile of 0.651 over 20 sessions, so that part fails, by 0.001, in the direction of better
    decoding. Adding the 3 window sessions among the 12 highest-RR sessions, a selection biased towards high R2,
    gives 0.659. An LSTM on all 45 window sessions was not run, for time.""")
rep("""- claim: figs5-active-inactive-slopes
  outcome: partially_reproduced""","""- claim: figs5-active-inactive-slopes
  outcome: not_reproduced""")
rep("""    are -1.162e-03 and -4.50e-04.
  deviations:
  - Each session classifies""","""    are -1.162e-03 and -4.50e-04. The criterion reproduces the claim only when both slopes are within tolerance
    and names no partial outcome, so the inactive slope decides it. Whether the supplement's +0.54e-3 lost its
    minus sign is asked of a reader in questions/temmar-2025.yaml; against -0.54e-3 the claim would be reproduced.
  deviations:
  - Each session classifies""")
rep("""Figure S1 (channel 47 medial, row 5, column 5) and with Figure S4""","""Figure S1 (the electrodes table gives channel 47 as Medial, bank B, row 5, column 5) and with Figure S4""")
rep("""    is between the files and this sentence of the paper, or a sign convention of the paper's tuning angles.
  deviations:""","""    is between the files and this sentence of the paper, or a sign convention of the paper's tuning angles. The
    verifier reports that the panels of Figure 3E and Figure 3C show the files' pattern, so the sentence of Section
    4.2 and the figure disagree; whether the claim should follow the figure is asked of a reader.
  deviations:""")
rep("""    Pearson r between the two over the 20 sessions 0.582 (p = 0.007). RR without input normalisation, as the code
    fits it, gives +0.0019 per year (p = 0.58). Median R2, RR 0.296, LSTM 0.591.""","""    Pearson r between the two over the 20 sessions 0.582 (p = 0.007); over all 32 sessions with an LSTM, which add
    the 12 highest-RR sessions and are not a sample of the dataset, r = 0.807 (p = 2.4e-08). RR without input
    normalisation, as the code fits it, gives +0.0019 per year (p = 0.58). Median R2, RR 0.296, LSTM 0.591.""")
rep("""  notes: LSTM above RR on 20 of 20 sessions, by 0.223 to 0.385 (median 0.301), so no extra seeds were needed. RR's
    highest same-day R2 over all 312 sessions, 0.467, is below the lowest LSTM R2 seen, 0.514; the other 292 sessions
    were not tested with the LSTM.""","""  notes: LSTM above RR on 20 of 20 every-16th sessions, by 0.223 to 0.385, and on all 12 of the other sessions with
    the highest RR R2 (RR 0.390 to 0.467, LSTM higher by 0.182 to 0.300), 32 of 32 in all, so no extra seeds were
    needed. The 12 include the session with the highest RR R2 of all 312 (0.467). The other 280 sessions were not
    tested with the LSTM.""")
i=s.index("- claim: fig4a-lstm-beats-rr")
j=s.index("- claim: fig4bc-dof-accuracy")
blk=s[i:j]
assert new_dev in blk
blk2=blk.replace(new_dev, new_dev+"""
  - The 12 sessions with the highest RR same-day R2 outside the 20 were added after round 1 of the verification,
    chosen by that rule before their LSTM result, as the sessions where the LSTM is likeliest to fall below RR.""")
s=s[:i]+blk2+s[j:]
rep("""    day's normalisation RR's mean R2 is -13.4 to -17.9 past day 0.""","""    day's normalisation RR's mean R2 is -13.4 to -17.9 past day 0. The pass is narrow: the LSTM's early drop
    exceeds its later drop by 0.017 (0.207 against 0.190) and r exceeds 0.9 by 0.003, over 20 decoders.""")
rep("""    would. 2020Q2 has one session.'""","""    would. 2020Q2 has one session. The failure is marginal: 2023Q2 is 25.5% from the median.'""")
rep("""    to -0.149). Reading (b) gives -0.410 (RR) and -0.596 (LSTM); whole trials give -0.409 and -0.533.""","""    to -0.149). Reading (b) gives -0.410 (RR) and -0.596 (LSTM); whole trials give -0.409 and -0.533. As the
    paper used one session, single sessions were counted: under (a) RR is within tolerance on 33 of 312 sessions,
    and of the 20 LSTM sessions RR is within tolerance on 1, the LSTM on 8 and both on 1; under (b) and whole
    trials, none.""")
open(p,'w').write(s)
print("part 1 ok")
EOF
python3 $TMPDIR/rec1.py; sed -n 265,300p attempts/temmar-2025-01.yaml
```

```
part 1 ok
    one fit takes 77 s (round 1) to 148 s (round 2) with four at once, so all 312 would take 1.7 to 3.2 hours of
    fitting, over the 60-minute limit of a notebook.
  - Both decoders' cross-day curves use the 20 LSTM sessions' decoders, each tested on every session within 100
    days (1,088 evaluations per decoder and normalisation), scored on every 5th test bin for time.
  - The criterion names two readings each of offset and normalisation; the outcome holds under one pair of the four.
- claim: suppc1-shuffle-baseline
  outcome: partially_reproduced
  notebook: decoding.ipynb
  output: claim:suppc1-shuffle-baseline
  measured:
  - -0.223
  - -0.154
  notes: All shuffles give negative R2. Under reading (a), raw bins permuted, the LSTM median is -0.154 (20 sessions),
    inside -0.156 +- 0.0156, and RR's -0.223 (312 sessions), outside -0.166 +- 0.0166 (per-session range -0.363
    to -0.149). Reading (b) gives -0.410 (RR) and -0.596 (LSTM); whole trials give -0.409 and -0.533. As the
    paper used one session, single sessions were counted: under (a) RR is within tolerance on 33 of 312 sessions,
    and of the 20 LSTM sessions RR is within tolerance on 1, the LSTM on 8 and both on 1; under (b) and whole
    trials, none.
  deviations:
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec2.py <<'EOF'
p='attempts/temmar-2025-01.yaml'
s=open(p).read()
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n==count, (n,a[:80])
    s=s.replace(a,b)
rep("""    on 11 of 12). R2 after day 0 is negative because input normalisation is held at the training parameters. 283
    day-0 sessions are eligible, as the legend reports, when the last session, with nothing after it, is left out.
  deviations:
  - 12 of the 283 day-0 sessions, evenly spaced and chosen before any result, and only 1 and 5 training sessions
    (the two the criterion compares), for time; the paper trains 1415 LSTMs, about 19 hours here.
  - Scored on every 5th test bin; the code's variant of the multi-day trainer was not run.""","""    on 11 of 12). R2 after day 0 is negative because input normalisation is held at the training parameters. With
    the normalisation refit on each test session, the code's variant, the three also hold (days 1 to 5, 0.372 to
    0.418; drop 0.215 against 0.086; day 0, 0.587 against 0.503), and R2 after day 0 is positive (mean 0.18 to
    0.34 over days 6 to 180), near Figure 5A. 283 day-0 sessions are eligible, as the legend reports, when the
    last session, with nothing after it, is left out.
  deviations:
  - 12 of the 283 day-0 sessions, evenly spaced and chosen before any result, and only 1 and 5 training sessions
    (the two the criterion compares), for time; the paper trains 1415 LSTMs, 7 to 15 hours here.
  - Scored on every 5th test bin. Of the code's variant of the multi-day trainer, the refit of input
    normalisation on the test data is run; its 90/10 split and training without noise would need the models
    retrained and are not.""")
rep("""    with five sessions.
  deviations:""","""    with five sessions. Two variants were run after round 1 of the verification. With the test day's
    normalisation and the criterion's initial values, the initial rate is still not more negative for one session
    (0.034 against 0.014). Started from the values printed in the Figure 5A panel (negative rates), the fits have
    lower residuals and all three conditions hold under both normalisations (training day, initial rates -0.906
    against -0.182, drop to day 5 1.237 against 0.416, long-term rates -0.0033 and 0.0010 with overlapping
    intervals; test day, -0.601 against -0.535, drop 0.256 against 0.122, long-term rates -0.0046 and -0.0031,
    overlapping). The outcome is the criterion's and rests on its initial values, which start from growing
    components; whether they misread the code is asked of a reader.
  deviations:""")
rep("""  notes: Estimated from the 20 seed days, 32 to 85 later sessions each within 200 days (1146 in all), the four durations'
    iterations and the two normalisation readings, 2,446,600 training iterations, about 16.5 hours at the measured
    0.097 s per iteration with four fits at once, beyond the 60-minute notebook limit and the run. Not run.""","""  notes: The 20 seed days are in the dataset and are followed by 32 to 85 sessions each within 200 days (1146 in
    all). With the four durations' iterations and the two normalisation readings this is 2,446,600 training
    iterations, 6.3 hours at the 0.037 s per iteration measured in round 1 with four fits at once, and about twice
    that at round 2's fit times (148 s per 2000 iterations), beyond the 60-minute notebook limit and the run. The
    30 s arm alone (20 seed fits and 1146 fine-tunes of 50 iterations, under both readings) was written as a
    notebook after round 1 and started in this run; it had not finished after 52 minutes when the run's time
    limit stopped it, so it is not in the entry and supplies no number. The 120 s and 300 s arms on 2 seed days
    were not started. No part was tested.""")
open(p,'w').write(s)
print("part 2 ok")
EOF
python3 $TMPDIR/rec2.py; grep -n "verifications" attempts/temmar-2025-01.yaml; tail -5 attempts/temmar-2025-01.yaml; date -u
```

```
part 2 ok
    angles use another sign.
- kind: code_mismatch
  statement: In bci_decoding/nn_utils.py, train_model calls add_training_noise(inputs, noise_neural_std, noise_bias_std),
    whose parameters are (x, bias_neural_std, noise_neural_std), so the code adds a bias of SD 0.1 and white noise
    of SD 0.2, the reverse of Appendix C.1 (noise 0.1, bias 0.2).
Thu Nov 12 19:00:29 UTC 2026
```

**Agent calls Bash**

```bash
cd  cat >> attempts/temmar-2025-01.yaml <<'EOF'
verifications:
- date: '2026-11-12'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)
  reviewed: >-
    The first executed notebooks (signals.ipynb, decoding.ipynb, multiday.ipynb) with the conclusion
    cells and the summaries removed, the helper module link.py and the claims file, with the paper's full
    text and supplement (the PDFs read for Figures 3, 5 and S1). The verifier listed the archive's assets
    and version metadata through the DANDI API with the helper, and tested the helpers on synthetic inputs
    (circ_median and circ_iqr across the wrap, channel_tuning, participation_ratio, trial_directions). It
    had no attempt record and took the claims from the claims file.
  results:
  - claim: dataset-sessions
    agrees: true
    outcome: reproduced
    reason: >-
      signals [11]: 312 files, 303 days, span 1242 days, 9 two-session days (all CO+RD), and every
      session has 375 trials. No implant date in the files, so the comparison with days 349 to 1591 is
      skipped, as the criterion allows. Separately, the claims file's header says the data run to
      "February 2024", but the data end on 2023-06-22, which fits the 1242-day span.
    response: >-
      No change to the outcome. The header's "February 2024" comes from Appendix B.1, where it is the
      range of the candidate days before curation; it is asked of a reader in questions/temmar-2025.yaml.
  - claim: dataset-contents
    agrees: true
    outcome: partially_reproduced
    reason: >-
      signals [13]: all series, trials columns and electrode columns are present except imp, which is
      missing in 81 of 312 files. Bins are 0.02 s apart (within 1 ms) with gaps between runs. Velocity
      matches the forward difference of position everywhere except the 72 bins before gaps. Appendix A.2
      says impedances are left out when none was measured within 3 weeks of a session. The 81 files
      without impedances fit the paper's own rule, which the dataset-contents criterion does not account
      for.
    response: >-
      Outcome kept, as the criterion asks for the column in every file. Whether the criterion should
      accept a session without impedances under the rule of Appendix A.2 is asked of a reader in
      questions/temmar-2025.yaml.
  - claim: figs2-throughput-improves
    agrees: true
    outcome: reproduced
    reason: >-
      signals [15]: the slope is positive with p < 0.05 under all three readings (a, +0.24 bits/s per
      year, p = 6e-8; b, p = 8e-37; c, p = 3e-20). 998 trials shorter than the 750 ms hold become NaN
      under readings (a) and (c); that is under 1% of trials, and reading (b) has none and is also
      significant.
    response: No change.
  - claim: fig2a-sbp-decline
    agrees: true
    outcome: reproduced
    reason: >-
      signals [17]: reading (b) applies, because the stored unit is volts with conversion 1e-6, so stored
      values are microvolts. That gives -0.0338 µV/month (tolerance -0.033 +- 0.0033) and -1.110e-3 per
      day, the supplement's number. Reading (a) gives -0.0084.
    response: No change.
  - claim: fig2a-irregular-shifts
    agrees: true
    outcome: partially_reproduced
    reason: >-
      decoding [20]: the shift part holds (38 of 42 days in the window have 5 or more shifting
      channels). RR's median in the window lies inside its 10th-90th percentile range. The LSTM's median
      (0.652, from 3 sessions) lies just above its 90th percentile (0.651, from 20 sessions), so the
      second part fails. The shift rule flags 5 or more channels on 237 of 243 days outside the window,
      so it cannot pick out the July-November 2022 period, and the shift part holds trivially. The LSTM
      part fails by 0.001, on 3 sessions, and in the "better" direction. It asked for per-day shift
      counts compared with a baseline rate, and the reading where the 30-day window counts sessions.
    response: >-
      Outcome kept. The cell now prints the baseline rate (0.974 of window days and 0.975 of other days
      have 5 or more shifting channels; median 17 against 20) and the variant with the 30 preceding
      recording days as the window (0.952 against 0.903); neither singles out the period, which the notes
      now say. The LSTM was added on the 12 highest-RR sessions (3 of them in the window), which gives a
      window median of 0.659 from a selection biased towards high R2; an LSTM on all 45 window sessions
      was not run, for time.
  - claim: fig2b-active-channels-decrease
    agrees: true
    outcome: reproduced
    reason: >-
      signals [19]: slope -0.0177 channels/day, p = 2.6e-12. The first 30 days average 44.6 active
      channels, the last 30 average 25.9.
    response: No change.
  - claim: fig2c-pr-decline
    agrees: true
    outcome: reproduced
    reason: >-
      signals [21]: -0.0708 PR/month (tolerance -0.07 +- 0.007). The every-session variant gives -0.0720.
    response: No change.
  - claim: fig2c-ten-dimensions
    agrees: true
    outcome: reproduced
    reason: >-
      signals [23]: reading (a) holds on 0.848 of days and reading (b) on 1.000. Reading (c) holds on
      only 0.446.
    response: No change.
  - claim: figs4-bank-slopes
    agrees: true
    outcome: reproduced
    reason: >-
      signals [25], stored-µV reading: lateral -5.84e-4, medial 1 -1.34e-3, medial 2 -1.40e-3, all
      channels -1.11e-3, all within tolerance. Lateral mean SBP (2.19) is below both medial banks (2.55,
      3.57).
    response: No change.
  - claim: figs5-active-inactive-slopes
    agrees: false
    outcome: not_reproduced
    reason: >-
      signals [27]: the active slope (-1.261e-3) is within tolerance, and inactive channels have lower
      SBP. The inactive slope is -0.536e-3 against an expected +0.54e-3, so it is outside tolerance under
      both fit readings. Its size matches to 1% with the opposite sign. The paper prints "0.54 x 10^-3"
      for inactive channels, calls it "near 0", and says in Section 4.1 that all categories decreased;
      the claims file reads the value as positive, which suggests a dropped minus sign. Under that
      reading the claim would be reproduced.
    response: >-
      Outcome changed from partially_reproduced to not_reproduced, as the verifier gives it, because the
      criterion reproduces the claim only when both slopes are within tolerance and names no partial
      outcome. The sign of the printed slope is asked of a reader in questions/temmar-2025.yaml.
  - claim: fig2d-population-drift
    agrees: true
    outcome: partially_reproduced
    reason: >-
      signals [29]: the centroid moves 17.0 between the first and last quarter, against a within-quarter
      SD of 2.02, so movement holds. Three quarters (2021Q1, 2022Q3, 2023Q2) are more than 25% from the
      median SD, where the rule allows at most two, so stable spread fails. 2023Q2 misses by only 0.01,
      and 2020Q2 is a single session. The partial outcome is marginal.
    response: Outcome kept; the notes now say the failure is marginal (2023Q2 is 25.5% from the median).
  - claim: fig2e-trajectories-separable
    agrees: true
    outcome: reproduced
    reason: >-
      signals [31], main alignment: accuracy 0.212 in 2020 and 0.220 in 2023, against chance 1/8 (binomial
      p < 1e-200 both years), above the majority class (0.16-0.18) and permuted labels (about 0.12). The
      code variant also holds. With k_sd = 1 the onset is almost always the first bin after the baseline,
      so trajectories are in effect aligned to trial start; this follows the paper's stated method. A PCA
      fitted per day and trials of about 43 days pooled into one classifier can only lower accuracy.
    response: No change; both points do not affect the conclusion, as the verifier says.
  - claim: fig3b-two-channels
    agrees: true
    outcome: reproduced
    reason: >-
      signals [35]: channel 7's median angle is 81 degrees, its circular IQR 18.6 degrees, and its strength
      0.0245 (median over channels 0.0070). Channel 32's IQR is 146.9 degrees, above the median IQR of 46.9.
      Mean TCR is 3.1 Hz for channel 7 and 36.5 Hz for channel 32.
    response: No change.
  - claim: fig3cd-tuning-stable
    agrees: true
    outcome: reproduced
    reason: >-
      signals [37]: under the 90-degree reading, 0.771 of all channels and 0.774 of active channels have a
      small IQR. Under the 45-degree reading it is 0.479 and 0.453.
    response: No change.
  - claim: fig3d-weak-channels-low-tcr
    agrees: true
    outcome: reproduced
    reason: >-
      signals [39]: Spearman rho = 0.925 (p = 3e-41). Mann-Whitney p = 5e-11 (median TCR 0.40 Hz vs 0.87
      Hz).
    response: No change.
  - claim: fig3e-array-tuning
    agrees: true
    outcome: not_reproduced
    reason: >-
      signals [41]: only 3% of medial channels fall in the flexion sector, and only 6% of lateral channels
      in the extension sector; medial medians cluster at about -130 degrees, lateral ones at 0-90. This is
      the reverse of the sentence in Section 4.2, but it matches the paper's own Figures 3C and 3E. The
      criterion follows the text; the Figure 3E panels are labelled the other way, and the claims file
      does not mention the contradiction. It asked for channel 47's array_name, row and col, to check the
      file labels against Figure S1.
    response: >-
      Outcome kept. The cell now prints channel 47 from the electrodes table (Medial, bank B, row 5,
      column 5, as Figure S1 has it). Whether the claim should follow Figure 3E is asked of a reader in
      questions/temmar-2025.yaml.
  - claim: fig4a-sameday-stable
    agrees: true
    outcome: reproduced
    reason: >-
      decoding [9]: neither slope is negative with p < 0.05 (RR over 312 sessions +0.002/yr, p = 0.58;
      LSTM over 20 sessions +0.006/yr, p = 0.56). The RR-LSTM Pearson r is 0.582 (p = 0.007), but only over
      20 sessions. The stated reason for the subset (4.3 h at 200 s per fit) conflicts with the measured
      77 s per fit, which is about 1.7 h.
    response: >-
      Outcome kept. The time is corrected: fits took 77 s in round 1 and 148 s in this run, so all 312
      would take 1.7 to 3.2 hours, still over the 60-minute notebook limit. The correlation over all 32
      sessions with an LSTM is shown as a variant (r = 0.807), noted as not a sample of the dataset.
  - claim: fig4a-lstm-beats-rr
    agrees: true
    outcome: reproduced
    reason: >-
      decoding [11]: the LSTM beats RR on 20 of 20 sessions, by at least 0.223. The highest RR R2 on any
      of the 312 sessions (0.467) is below the lowest LSTM R2 (0.514), but 292 sessions have no LSTM. 20
      of 312 sessions is weak support for the universal "every day" claim. It asked for LSTM R2 on all
      312 sessions, or at least on the sessions with the highest RR R2.
    response: >-
      Outcome kept. The LSTM is now trained on the 12 sessions with the highest RR R2 outside the 20,
      including the highest of all 312; it beats RR on all 12 (by 0.182 to 0.300), 32 of 32 in all. All
      312 were not run, for time.
  - claim: fig4bc-dof-accuracy
    agrees: true
    outcome: reproduced
    reason: >-
      decoding [13]: for both decoders, both position medians exceed both velocity medians, and MRS
      exceeds IDX for position and velocity.
    response: No change.
  - claim: fig4d-cross-day-decay
    agrees: true
    outcome: reproduced
    reason: >-
      decoding [16]: holds only under absolute offsets with test-day normalisation, where the LSTM is
      better at every offset, the short-term drop is 0.207 against a later drop of 0.190, and r = 0.903.
      Signed offsets with test-day normalisation fail narrowly (drops 0.19 vs 0.21, r = 0.887). The pass
      depends on one of four reading pairs, and on margins of 0.017 and 0.003, with 20 decoders.
    response: Outcome kept; the notes now give the two margins and the number of decoders.
  - claim: suppc1-shuffle-baseline
    agrees: true
    outcome: partially_reproduced
    reason: >-
      decoding [18], reading (a): the LSTM median is -0.154, within tolerance. The RR median is -0.223,
      outside -0.166 +- 0.017. Reading (b) gives -0.60 and -0.41, both outside. All values are negative,
      consistent with the paper's chance reference. It asked for the number of sessions where both
      shuffled R2 values fall within tolerance, as the paper used a single unnamed session.
    response: >-
      Outcome kept. The cell now counts sessions within tolerance; under reading (a) RR is within it on
      33 of 312 sessions, and of the 20 LSTM sessions both decoders are within it on 1; under reading (b)
      and whole trials on none.
  - claim: fig5a-multiday-short-term
    agrees: true
    outcome: reproduced
    reason: >-
      multiday [8], 12 of 283 day-0 sessions, training-day normalisation; the comparisons of 5 against 1
      session hold, but all these R2 values are far below Figure 5A. The criterion requires the code
      variant (normalisation refit on the test day) to be shown, and it was not run; the 1-vs-5
      comparisons could change under it. Only 12 day-0 sessions were run, giving 16 evaluations at days
      1-5.
    response: >-
      Outcome kept. The models are now also evaluated with the normalisation refit on each test session.
      All three comparisons hold under it too (days 1 to 5, 0.418 against 0.372; drop 0.086 against
      0.215; day 0, 0.503 against 0.587), with R2 after day 0 near Figure 5A. The code's 90/10 split and
      training without noise were not run, and the 12 day-0 sessions were kept, for time.
  - claim: fig5a-long-term-decay
    agrees: true
    outcome: not_reproduced
    reason: >-
      multiday [10]: the initial rate is not more negative for 1 session, and the predicted drop to day 5
      is not larger; the long-term intervals overlap. Both fits are degenerate, so this outcome tells us
      little. The starting values (positive rates) come from the criterion, but the paper's legend shows
      negative rates, and no fit was run from the legend's values. It asked for the fits recomputed with
      the test-day normalisation, and a fit started from the legend's values.
    response: >-
      Outcome kept, as the criterion fixes the starting values. Both variants are now run. With test-day
      normalisation and the criterion's values the initial rate is still not more negative for 1 session.
      From the legend's values the fits have lower residuals and all three conditions hold under both
      normalisations. The notes say the outcome rests on the starting values, and whether the criterion's
      values misread the code is asked of a reader in questions/temmar-2025.yaml.
  - claim: fig5b-finetune
    agrees: true
    outcome: blocked
    reason: >-
      multiday [12]: the full run is estimated at 6.3 h. The archive holds all 20 seed days and all 312
      files (12.6 GB), so no data are missing, and part of the claim could have been run. The 30 s arm
      alone (20 seed fits plus 1,146 fine-tunes of 50 iterations, about 15-25 min for both normalisation
      readings) could have tested half of the criterion; a subset of seeds would have made 120 s and
      300 s feasible. Neither was run.
    response: >-
      Not done. A notebook for the 30 s arm under both readings and one for the 120 s and 300 s arms on 2
      seed days were written; the 30 s notebook ran 52 minutes in this run without finishing (fits were
      about twice as slow as in round 1) and the run's time ran out, so neither is in the entry and the
      claim stays blocked as too_large. The notes give the estimate with this run's fit times.
EOF
python tools/entry.py check entries/temmar-2025 2>&1 | tail -5; date -u
```

```
error: attempts/temmar-2025-01.yaml: not valid YAML: mapping values are not allowed in this context
  in "<unicode string>", line 261, column 86
1 error(s)
Thu Nov 12 19:01:24 UTC 2026
```

**Agent calls Bash**

```bash
cd  sed -n 255,265p attempts/temmar-2025-01.yaml
```

```
notebook: decoding.ipynb
  output: claim:fig4d-cross-day-decay
  notes: Under absolute offset and test-day normalisation, the LSTM is above RR at all 101 offsets; LSTM 0.583,
    0.376, 0.186 and RR 0.294, 0.088, -0.005 at day 0, 1 to 5 days and 90 to 100 days; normalised curves correlate
    at r = 0.903. Under the other three pairs the LSTM is also better at every offset, but r is 0.887, 0.526 and
    0.391, and with the signed offset and test-day normalisation the sharp-then-stable part fails. With the training
    day's normalisation RR's mean R2 is -13.4 to -17.9 past day 0. The pass is narrow: the LSTM's early drop
    exceeds its later drop by 0.017 (0.207 against 0.190) and r exceeds 0.9 by 0.003, over 20 decoders.
  deviations:
  - The LSTM is trained on 20 of the 312 sessions (every 16th in date order, chosen before any result), for time;
    one fit takes 77 s (round 1) to 148 s (round 2) with four at once, so all 312 would take 1.7 to 3.2 hours of
```

**Agent calls Bash**

```bash
cd  sed -i 's/The pass is narrow: the LSTM/The pass is narrow; the LSTM/; s/The failure is marginal: 2023Q2/The failure is marginal, as 2023Q2/' attempts/temmar-2025-01.yaml; python tools/entry.py check entries/temmar-2025 2>&1 | tail -5; python3 - <<'EOF'
import yaml,re
d=yaml.safe_load(open('attempts/temmar-2025-01.yaml'))
txt=open('attempts/temmar-2025-01.yaml').read()
# find plain-scalar lines with ': ' inside notes/deviations (rough check)
for o in d['outcomes']:
    for k in ('notes',):
        v=o.get(k,'')
        if '—' in v or 'rather' in v: print('style',o['claim'])
print(sum(1 for o in d['outcomes']), [ (o['claim'],o['outcome']) for o in d['outcomes'] if o['outcome']!='reproduced'])
yaml.safe_load(open('questions/temmar-2025.yaml')); print('questions ok')
EOF
grep -n "—\|rather" attempts/temmar-2025-01.yaml questions/temmar-2025.yaml | head
```

```
error: attempts/temmar-2025-01.yaml: not valid YAML: mapping values are not allowed in this context
  in "<unicode string>", line 280, column 57
1 error(s)
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "[a-z)]: [a-z(]" attempts/temmar-2025-01.yaml | grep -v "^\s*[0-9]*:\s*-\? \?[a-z_]*: " | grep -v ">-" | head -20
```

```
280:    paper used one session, single sessions were counted: under (a) RR is within tolerance on 33 of 312 sessions,
467:      signals [25], stored-µV reading: lateral -5.84e-4, medial 1 -1.34e-3, medial 2 -1.40e-3, all
498:      signals [31], main alignment: accuracy 0.212 in 2020 and 0.220 in 2023, against chance 1/8 (binomial
549:      Outcome kept. The time is corrected: fits took 77 s in round 1 and 148 s in this run, so all 312
584:      decoding [18], reading (a): the LSTM median is -0.154, within tolerance. The RR median is -0.223,
```

**Agent calls Bash**

```bash
cd  sed -i '280s/single sessions were counted: under (a)/single sessions were counted. Under (a)/' attempts/temmar-2025-01.yaml; python tools/entry.py check entries/temmar-2025 2>&1 | tail -5; python3 -c "
import yaml
d=yaml.safe_load(open('attempts/temmar-2025-01.yaml'))
print(len(d['outcomes']), [(o['claim'],o['outcome']) for o in d['outcomes'] if o['outcome']!='reproduced'])
yaml.safe_load(open('questions/temmar-2025.yaml')); print('q ok')"; grep -n "—\| rather" attempts/temmar-2025-01.yaml questions/temmar-2025.yaml entries/temmar-2025/*.ipynb | head; date -u
```

```
0 error(s)
24 [('dataset-contents', 'partially_reproduced'), ('fig2a-irregular-shifts', 'partially_reproduced'), ('figs5-active-inactive-slopes', 'not_reproduced'), ('fig2d-population-drift', 'partially_reproduced'), ('fig3e-array-tuning', 'not_reproduced'), ('suppc1-shuffle-baseline', 'partially_reproduced'), ('fig5a-long-term-decay', 'not_reproduced'), ('fig5b-finetune', 'blocked')]
q ok
Thu Nov 12 19:01:51 UTC 2026
```

**Agent calls Bash**

```bash
cd  executed/temmar-2025/.venv/bin/python - <<'EOF'
import nbformat as nbf
for n in ("signals.ipynb", "decoding.ipynb", "multiday.ipynb"):
    src = nbf.read(f"entries/temmar-2025/{n}", as_version=4)
    ex = nbf.read(f"executed/temmar-2025/{n}", as_version=4)
    assert len(src.cells) == len(ex.cells), n
    k = 0
    for a, b in zip(src.cells, ex.cells):
        assert a.cell_type == b.cell_type
        if a.cell_type == "code":
            assert a.source == b.source, (n, a.source[:60])
        elif a.source != b.source:
            b.source = a.source; k += 1
    nbf.write(ex, f"executed/temmar-2025/{n}")
    print(n, "markdown cells updated:", k)
EOF
date -u
```

```
signals.ipynb markdown cells updated: 4
decoding.ipynb markdown cells updated: 6
multiday.ipynb markdown cells updated: 4
Thu Nov 12 19:01:59 UTC 2026
```

**Agent**

I made the round-1 revisions, but the full re-run with `python tools/entry.py all` did not finish: it hit the 2-hour command limit. Three of the four notebooks ran: signals, decoding and multiday. The fine-tuning notebook I added had run 52 minutes without finishing when it was stopped, so fig5b-finetune stays blocked (`too_large`). The code in the three executed notebooks matches the source cell for cell, I updated their conclusion cells by hand to the new numbers, and `entry.py check` passes. The workflow's own run will execute them again, because the conclusion text changed.

**Outcomes**
- **figs5-active-inactive-slopes:** changed from partially reproduced to not reproduced, as the verifier said. The criterion has no partial outcome. The inactive slope is −0.536e-3 against an expected +0.54e-3: the same size with the opposite sign.
- **fig5a-long-term-decay:** stays not reproduced under the criterion's starting values. Started from the values printed in the Figure 5A panel, the fits have lower residuals and all three conditions hold under both normalisations. The record now says the outcome rests on the starting values.
- **fig5b-finetune:** still blocked, and no part of it was tested.
- **All other outcomes:** unchanged; the verifier agreed with them.

**Added**
- **fig5a, test-day normalisation:** the models are now also scored with normalisation refit on each test day. fig5a-multiday-short-term holds under both readings, and with test-day normalisation R2 after day 0 is near Figure 5A's.
- **fig4a-lstm-beats-rr:** LSTMs on the 12 sessions with the highest RR R2, including the highest of all 312. The LSTM beats RR on all of them, 32 of 32 sessions in all.
- **fig2a-irregular-shifts:** a baseline rate for the shift rule. It flags 97.4% of days in July to November 2022 and 97.5% of other days, so it does not pick out that period. Also a variant counting the preceding 30 recording days.
- **suppc1-shuffle-baseline:** a count of sessions within tolerance. Under reading (a), RR is within it on 33 of 312 sessions; both decoders are within it on 1 of the 20 LSTM sessions.
- **fig3e-array-tuning:** channel 47 printed from the electrodes table: Medial, bank B, row 5, column 5, as Figure S1 has it.
- **Corrections:** the LSTM fit times, which were 77 s per fit in round 1 and 148 s in this run, so all 312 would take 1.7 to 3.2 hours; the fig4d and fig2d margins; the fig5b estimate.
- **Records:** the round under `verifications` for all 24 claims. `questions/temmar-2025.yaml` now asks a reader five things: the sign of the inactive slope (figs5), Figure 3E against Section 4.2 (fig3e), the impedance rule of Appendix A.2 (dataset-contents), the claims file's "February 2024" (dataset-sessions), and the criterion's starting values for the fit (fig5a-long-term-decay).

**Not done**
- **fig5b-finetune:** I wrote two notebooks, one for the 30 s arm and one for the 120 s and 300 s arms on 2 seed days. I removed both from the entry and the record because they produced no numbers.
- **More LSTMs:** none on all 45 sessions of July to November 2022 or on all 312, and the code's 90/10 split and training without noise for Figure 5A were not run. All were left out for time.
- **More fig5a day-0 sessions:** I kept 12 instead of doubling them, for time.
- **A lost first run:** my first attempt to run the entry in the background was killed when the command returned, which cost about 15 minutes.

Nothing is committed.

## End of run

68 turns, 172 minutes, $7.68 at API prices, result: success.
