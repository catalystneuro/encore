# kussovska-2025 · author-revise-2 · run 42828154641

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/kussovska-2025/verifier-2-report.md; ls entries/kussovska-2025 entries/kussovska-2025/*
```

```
Tue Nov 10 13:54:54 UTC 2026
**Verifier report, round 2: Kussovska et al. 2025 on DANDI:000469 (0.231213.2047)**

The claims file has 45 claims and the attempt record has 45 outcomes: 31 reproduced, 7 partially reproduced, 7 not reproduced. Seventeen outcomes are marked `assumed: true`. I checked the re-executed main notebook (149 cells), the new dPCA notebook (`dpca_kussovska_2025.ipynb`, 18 cells), `wm.py`, the README and the record.

### 1. Outcomes and assumptions

**The 39 outcomes left as they were after round 1: I agree with all of them.** That includes fig6cd, now not reproduced as I said in round 1. The printed values in the re-run support each one; caveats on fig4c and fig6e are in section 3.

**The three dPCA claims, now tested: I agree with all three.**
- **fig3abc, reproduced.** Maintenance medians are higher than encoding under both measures and both trial readings (dpca cell 12). Most of the gap comes from the longer maintenance window: over the first 499 bins it is tortuosity 2.46–2.57 against 2.16, and 9 reversals against 8. The record says so. The rank-sum p values treat the 500 values as independent, which they are not, but the criterion uses only medians.
- **fig3d, reproduced, but only under reading (b).** That reading is the code's own trial-selection bug, which the record reports as a finding (dpca cell 9):
  - Reading (b): H = 457.62; maintenance in its own space against maintenance projected onto encoding, p = 0.077.
  - Reading (a), the same trials in both epochs: those two maintenance conditions differ (p = 0.019).
  - The criterion names (b) as a reading, so the outcome stands. It is the code's result, not one independent of it.
- **fig3h, reproduced** with `protect=[]` for the early half (H = 410 and 413; dpca cell 15). Under the code's own setting the early half separates less than the late half in all 100 splits. That setting gives H = 394 and 380, also inside the tolerance, but in the wrong direction. The record states this.

**fig4c,
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md; ls attempts* 2>/dev/null; ls; ls questions | grep kuss; find . -path ./node_modules -prune -o -name "*kussovska*" -print | grep -v "^./paper"
```

```
654 docs/protocol.md
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
345:### 2. Check the data against its description
360:### 3. Write the entry
428:### 4. Lock, check and run
440:### 5. Record the attempt
502:### 6. Hand over for verification
540:## Repeat attempts
582:## Local and remote datasets
605:## Verifier
609:### Round 1: without the author's conclusions
[... 296 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,654p docs/protocol.md
```

```
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
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 478 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/kussovska-2025-01.yaml; ls questions/ | grep kuss; ls transcripts/kussovska-2025; date -u
```

```
1156 attempts/kussovska-2025-01.yaml
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
Tue Nov 10 13:54:59 UTC 2026
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kussovska-2025-01.yaml"
}
```

```
1	schema_version: 3
2	id: kussovska-2025-01
3	datasets:
4	- archive: dandi
5	  id: 000469
6	  version: 0.231213.2047
7	  doi: 10.48324/dandi.000469/0.231213.2047
8	  relation: reuses
9	paper: doi:10.1101/2025.10.31.684900
10	date: '2026-11-10'
11	entry: kussovska-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 781 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kussovska-2025-01.yaml",
 "offset": 802
}
```

```
802	- kind: methods_unavailable
803	  statement: 'Question for the authors: over which window are the Poisson surrogates of the maintenance
804	    burst test drawn? The code draws them on [0, 2.8 s] for every trial (main_4c,d,6a,b.py:13 and 288-289)
805	    while each trial''s maintenance ends at the probe, 2.53 to 2.84 s after onset, and burst-free trains
806	    then exceed the null. Here Fig. 4d is reproduced over each trial''s own maintenance with the Methods''
807	    groups and the prominence rule, and not with the code''s groups.'
808	verifications:
809	- date: '2026-11-10'
810	  kind: agent
811	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
812	  reviewed: 'Round 1: the executed notebook reproduce_kussovska_2025.ipynb with the conclusion cells and
813	    the summary removed, the helper module wm.py and the claims file, with the paper''s full text. The
814	    verifier queried the archive and tested group_bursts on synthetic Poisson data; it had no attempt
815	    record. It could not check the code repository.'
816	  results:
817	  - claim: units-by-region
818	    agrees: true
819	    outcome: reproduced
820	    reason: 902 units from 21 patients; AMY 259, HPC 190, dACC 171, preSMA 250, vmPFC 32, all exact (cell
821	      16).
[... 336 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; wc -l wm.py; cat entry.yaml; grep -n "hash(\|PYTHONHASHSEED\|set(\|default_rng\|np.random.seed\|def \|Pool\|pmap" wm.py | head -150
```

```
868 wm.py
schema_version: 1
name: kussovska-2025
type: reproduction
title: Neural heterogeneity and the temporal structure of human working memory (Kussovska et al. 2025)
description: Tests the findings of Kussovska, Kim and Rungratsameetaweemana (2025) on dandiset 000469,
  the human single-neuron recordings of Kyzar et al. (2024) during a Sternberg working memory task.
  It covers behavior, GLM load and reaction-time modulation, concept cells, persistence and
  decoding of the maintained image, population bursts, autocorrelogram-based cell types and their
  bursting, task modulation and decoding, and, in a second notebook, the dPCA state-space analyses.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_kussovska_2025.ipynb
  title: Reproducing Kussovska et al. (2025) from dandiset 000469
  runtime_minutes: 46
- path: dpca_kussovska_2025.ipynb
  title: The dPCA state-space claims of Kussovska et al. (2025) from dandiset 000469
  runtime_minutes: 22
helpers:
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; sed -n 1,35p wm.py; sed -n 160,240p wm.py; sed -n 335,410p wm.py; sed -n 679,705p wm.py
```

```
"""Loading and shared measures for DANDI:000469 (Kyzar et al. 2024), as used by Kussovska, Kim and
Rungratsameetaweemana (2025), "Neural heterogeneity shapes the temporal structure of human working
memory" (bioRxiv doi:10.1101/2025.10.31.684900).

The data are streamed from the archive at a pinned version (DANDISET_VERSION, the version the paper
cites in Methods, Participants and data source). Only the Sternberg file of each subject is read
(sub-<n>_ses-2), as the paper's code does (01_data_extraction.py:417 of
github.com/dariakussovska/heterogeneitywm at commit 5144fe8); only the spike times, the electrode
locations and the trials table are read, not the waveforms or the stimulus images.
"""
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000469"
DANDISET_VERSION = "0.231213.2047"
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff 443f5b4724 7906b08125 --stat; git diff 443f5b4724 7906b08125 -- entries/kussovska-2025/wm.py | head -300
```

```
attempts/kussovska-2025-01.yaml                    |  674 ++-
 entries/kussovska-2025/README.md                   |   11 +-
 entries/kussovska-2025/dpca_kussovska_2025.ipynb   |  463 ++
 entries/kussovska-2025/entry.yaml                  |    7 +-
 .../kussovska-2025/reproduce_kussovska_2025.ipynb  |  572 ++-
 entries/kussovska-2025/requirements.in             |    1 +
 entries/kussovska-2025/requirements.lock.txt       |   22 +-
 entries/kussovska-2025/wm.py                       |  172 +-
 .../kussovska-2025/author-revise-1-report.md       |   36 +
 transcripts/kussovska-2025/author-revise-1.md      | 4612 ++++++++++++++++++++
 transcripts/kussovska-2025/verifier-1-report.md    |   92 +
 transcripts/kussovska-2025/verifier-1.md           |  704 +++
 12 files changed, 7015 insertions(+), 351 deletions(-)
diff --git a/entries/kussovska-2025/wm.py b/entries/kussovska-2025/wm.py
index 9e0558a235..e62d93c0d0 100644
--- a/entries/kussovska-2025/wm.py
+++ b/entries/kussovska-2025/wm.py
@@ -487,23 +487,32 @@ def epoch_spikes(spikes, starts, ends, win):
 
 
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff 443f5b4724 7906b08125 -- entries/kussovska-2025/requirements.lock.txt entries/kussovska-2025/requirements.in | grep "^[+-]" | grep -v "hash"
```

```
--- a/entries/kussovska-2025/requirements.in
+++ b/entries/kussovska-2025/requirements.in
+scikit-posthocs
--- a/entries/kussovska-2025/requirements.lock.txt
+++ b/entries/kussovska-2025/requirements.lock.txt
-    # via -r requirements.in
+    # via
+    #   -r requirements.in
+    #   scikit-posthocs
+    #   seaborn
+    #   scikit-posthocs
+    #   seaborn
+    #   scikit-posthocs
+    #   seaborn
+scikit-posthocs==0.17.1 \
+    # via -r requirements.in
+    #   scikit-posthocs
+seaborn==0.13.2 \
+    # via scikit-posthocs
-    # via -r requirements.in
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/k; for c in 443f5b4724 7906b08125; do git show $c:entries/kussovska-2025/reproduce_kussovska_2025.ipynb > $TMPDIR/k/$c.ipynb; python -c "
import json,sys
nb=json.load(open('$TMPDIR/k/$c.ipynb'))
for i,c in enumerate(nb['cells']):
    print('#### CELL',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
" > $TMPDIR/k/$c.txt; done; diff $TMPDIR/k/443f5b4724.txt $TMPDIR/k/7906b08125.txt | head -150
```

```
37c37
< | fig3abc-trajectory-complexity, fig3d-encoding-vs-maintenance-separability, fig3h-early-vs-late-maintenance | blocked (too large; the time of one dPCA fit is measured below) |
---
> | fig3abc-trajectory-complexity, fig3d-encoding-vs-maintenance-separability, fig3h-early-vs-late-maintenance | tested in the second notebook, `dpca_kussovska_2025.ipynb` |
150a151,166
> # The two trials with a degenerate epoch (both in subject 9): which analyses they enter.
> t9 = T[9]
> for name, d in [("maintenance", t9.maint_dur.values), ("fixation", (t9.enc1 - t9.fix_start).values)]:
>     j = int(np.argmin(d))
>     print(f"subject 9, shortest {name}: trial {t9.trial.iat[j]}, load {t9.load.iat[j]}, {d[j]:.6f} s (next shortest {np.sort(d)[1]:.3f} s)")
> j = int(np.argmin((t9.enc1 - t9.fix_start).values))
> keep = np.arange(len(t9)) != j
> dev = []
> for n in NT.nid[NT["sub"] == 9]:
>     r = wm.count_in(SPK[n], t9.fix_start.values, t9.enc1.values) / (t9.enc1 - t9.fix_start).values
>     dev.append((int(wm.count_in(SPK[n], t9.fix_start.values[j:j + 1], t9.enc1.values[j:j + 1])[0]),
>                 abs(r[keep].mean() - FIX[n][0]), abs(r[keep].std(ddof=1) - FIX[n][1])))
> dev = np.array(dev)
> print(f"subject 9's neurons with a spike in the 31 us fixation: {int((dev[:, 0] > 0).sum())} of {len(dev)}; leaving that trial out "
>       f"changes the fixation mean rate by at most {dev[:, 1].max():.3f} Hz and its s.d. by at most {dev[:, 2].max():.3f} Hz")
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "CELL" $TMPDIR/k/7906b08125.txt | sed -n 1,200p | awk 'NR<200' | head -160
```

```
1:#### CELL 0 markdown None
47:#### CELL 1 code None
84:#### CELL 2 markdown None
88:#### CELL 3 code ['sanity']
101:#### CELL 4 markdown None
106:#### CELL 5 code ['sanity']
117:#### CELL 6 markdown None
123:#### CELL 7 code ['sanity']
167:#### CELL 8 markdown None
181:#### CELL 9 code ['sanity']
205:#### CELL 10 markdown None
213:#### CELL 11 code ['sanity']
233:#### CELL 12 markdown None
237:#### CELL 13 code ['sanity']
278:#### CELL 14 markdown None
286:#### CELL 15 markdown None
291:#### CELL 16 code ['claim:units-by-region']
297:#### CELL 17 markdown None
300:#### CELL 18 markdown None
304:#### CELL 19 code ['claim:behavior-accuracy']
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 404,500p $TMPDIR/k/7906b08125.txt; sed -n 1093,1140p $TMPDIR/k/7906b08125.txt
```

```
#### CELL 33 markdown None
## fig1e-load-modulated-neurons

> During maintenance a significant proportion of neurons in the preSMA (19.6%), vmPFC (18.75%) and
> dACC (10.53%) was modulated by memory load.

Spike counts in the first 2.5 s of maintenance, a Poisson GLM on the z-scored predictor fitted by
Newton's method (the same maximum-likelihood fit as the code's unpenalised `PoissonRegressor`;
checked against sklearn below), 1,000 permutations with seed 17. Trial readings: (a) the code's
96 load-matched trials (`new_trial_info.xlsx`: subject 1's `new_trial_id`s, each neuron's count
from its own session's trial with the same id), with the permutation shared over the trial vector
(the code) or drawn within each participant (Methods); (b) all trials of each participant,
permuted within participant.
#### CELL 34 code ['claim:fig1e-load-modulated-neurons']
REG = {g: NT.nid[NT.region == g].values for g in ["AMY", "HPC", "dACC", "preSMA", "vmPFC"]}
NP = 1000


def glm_design(pred, trials, perm, seed=17):
    rng = np.random.default_rng(seed)
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed 2>/dev/null | head; ls -a entries/kussovska-2025; which python; python --version; sed -n 1,60p tools/entry.py | head -80; nproc; free -g
```

```
.
..
.claude
README.md
dpca_kussovska_2025.ipynb
entry.yaml
reproduce_kussovska_2025.ipynb
requirements.in
requirements.lock.txt
wm.py
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Python 3.13.18
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv -q -p 3.13 $TMPDIR/venv && uv pip install -q -p $TMPDIR/venv/bin/python -r entries/kussovska-2025/requirements.lock.txt ipykernel nbconvert 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"; date -u
```

```
2.5.4 1.18.1
Tue Nov 10 13:56:06 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import json
nb=json.load(open('entries/kussovska-2025/reproduce_kussovska_2025.ipynb'))
for i,c in enumerate(nb['cells'][:15]):
    print('#### CELL',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
"
```

```
#### CELL 0 markdown None
# Reproducing Kussovska, Kim and Rungratsameetaweemana (2025) from dandiset 000469

Paper. Kussovska D, Kim R, Rungratsameetaweemana N (2025). Neural heterogeneity shapes the
temporal structure of human working memory. bioRxiv,
[doi:10.1101/2025.10.31.684900](https://doi.org/10.1101/2025.10.31.684900). The claims file
(`claims/kussovska-2025.yaml`) was written from the bioRxiv full text posted on 1 November 2025
(main text, figure legends and Methods; the Extended Data figures and their legends were not in
the text read).

Dandiset. [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), version
0.231213.2047 (Kyzar et al. 2024, human single neurons during a Sternberg working memory task).
This is the version the paper cites (Methods, Participants and data source, and Data
availability). The four published versions (0.231213.2047, 0.240122.1800, 0.240122.1812,
0.240123.1806) hold the same 41 assets with the same asset identifiers and sizes, which the data
check below confirms, so the version the paper's code downloads (0.240123.1806) gives the same
data.

Paper's code. github.com/dariakussovska/heterogeneitywm at commit 5144fe8, the commit the
claims file read. Four of its shipped tables are outside inputs here:
[... 265 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; cat > $TMPDIR/k/load.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, wm
T0=time.time()
sessions = wm.load_all()
BY = {s["sub"]: s for s in sessions}
NT = wm.neuron_table(sessions)
T = {s["sub"]: wm.trial_frame(s) for s in sessions}
SPK = [wm.spikes_of(BY, r) for _, r in NT.iterrows()]
FIX = [wm.fixation_stats(SPK[n], T[NT["sub"].iat[n]]) for n in range(len(NT))]
INFO = wm.code_table("data/new_trial_info.xlsx")
FINAL = wm.code_table("data/new_trial_final.xlsx")
SHIP_REG = wm.code_table("data/all_neuron_brain_regions_cleaned.xlsx")
SHIP_CM = wm.code_table("data/cell_analysis/Cell_metrics.xlsx")
pickle.dump(dict(NT=NT,T=T,SPK=SPK,FIX=FIX,INFO=INFO,FINAL=FINAL,SHIP_REG=SHIP_REG,SHIP_CM=SHIP_CM), open("/tmp/claude-1001/k_state.pkl" if False else __import__('os').environ['TMPDIR']+"/k/state.pkl","wb"))
print(time.time()-T0)
EOF
time $TMPDIR/venv/bin/python $TMPDIR/k/load.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/k/load.py", line 1, in <module>
    import pickle, time, numpy as np, pandas as pd, wm
ModuleNotFoundError: No module named 'wm'

real	0m1.555s
user	0m1.701s
sys	0m0.105s
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; time PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/k/load.py
```

```
13.226516723632812

real	0m14.073s
user	0m3.592s
sys	0m0.403s
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; cat > $TMPDIR/k/glm.py <<'EOF'
import pickle, os, numpy as np, pandas as pd, wm, time
S=pickle.load(open(os.environ['TMPDIR']+"/k/state.pkl","rb")); globals().update(S)
ids1 = INFO[INFO.subject_id == 1].new_trial_id.values
REG = {g: NT.nid[NT.region == g].values for g in ["AMY", "HPC", "dACC", "preSMA", "vmPFC"]}
NP=1000
def glm_design(pred, trials, perm, seed=17):
    rng = np.random.default_rng(seed)
    shared = np.array([rng.permutation(len(ids1)) for _ in range(NP)])
    subperm, Y, X, P = {}, [], [], []
    for n in range(len(NT)):
        sub = NT["sub"].iat[n]
        t = T[sub].set_index("trial")
        if trials == "matched":
            rows = INFO[INFO.subject_id == sub].set_index("new_trial_id").loc[ids1, "trial_id"].values
        else:
            rows = t.index.values
        tt = t.loc[rows]
        Y.append(wm.count_in(SPK[n], tt.maint.values, tt.maint.values + 2.5))
        X.append(tt["load" if pred == "load" else "rt"].values)
        if perm == "shared":
            P.append(shared)
        else:
            if sub not in subperm:
                subperm[sub] = np.array([rng.permutation(len(rows)) for _ in range(NP)])
            P.append(subperm[sub])
    return Y, X, P
t0=time.time()
Y,X,P=glm_design("load","matched","shared")
real,null=wm.glm_fit(Y,X,P)
print("fit s",time.time()-t0)
absn=np.abs(null); thr=np.quantile(absn,0.95,axis=1,method="higher")
rel=np.abs(np.abs(real)-thr)/np.maximum(thr,1e-300)
print("neurons with |b1| within 1e-6 rel of thr:", (rel<1e-6).sum(), " within 1e-9:", (rel<1e-9).sum())
# how many null values tie with real
ties=(np.abs(absn-np.abs(real)[:,None])<=1e-9*np.maximum(np.abs(real)[:,None],1e-12)).sum(1)
print("neurons with any null tied to real (1e-9):", (ties>0).sum())
sig=np.abs(real)>=thr
for nm,idx in REG.items():
    near=idx[rel[idx]<1e-6]
    print(nm, sig[idx].sum(), "near-tie neurons", len(near), "their sig", sig[near].astype(int).tolist(), [f"{rel[i]:.1e}" for i in near])
np.save(os.environ['TMPDIR']+"/k/glm_load.npy", np.c_[real, null])
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/k/glm.py
```

```
fit s 8.9957115650177
neurons with |b1| within 1e-6 rel of thr: 8  within 1e-9: 8
neurons with any null tied to real (1e-9): 848
AMY 14 near-tie neurons 3 their sig [0, 1, 0] ['5.7e-16', '0.0e+00', '2.7e-16']
HPC 9 near-tie neurons 0 their sig [] []
dACC 18 near-tie neurons 0 their sig [] []
preSMA 50 near-tie neurons 4 their sig [1, 1, 1, 0] ['0.0e+00', '0.0e+00', '0.0e+00', '4.0e-16']
vmPFC 6 near-tie neurons 1 their sig [0] ['1.6e-16']
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; cat > $TMPDIR/k/acg.py <<'EOF'
import pickle, os, numpy as np, pandas as pd, wm, time, sys
S=pickle.load(open(os.environ['TMPDIR']+"/k/state.pkl","rb")); globals().update(S)
N=int(sys.argv[1])
t0=time.time()
rows=wm.pmap(lambda n: wm.acg_features(SPK[n]), [(n,) for n in range(N)]) if False else None
from joblib import Parallel, delayed
def f(n): return wm.acg_features(SPK[n])
rows=Parallel(n_jobs=4)(delayed(f)(n) for n in range(N))
F=pd.DataFrame(rows); print("s",time.time()-t0)
F.to_pickle(os.environ['TMPDIR']+f"/k/featA_{N}.pkl")
print((F.r2>0.3).sum())
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/k/acg.py 40
```

```
s 9.74337100982666
14
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; cat > $TMPDIR/k/acgstab.py <<'EOF'
import pickle, os, numpy as np, pandas as pd, wm, time
from scipy.optimize import least_squares
S=pickle.load(open(os.environ['TMPDIR']+"/k/state.pkl","rb")); globals().update(S)
def fits(n):
    nar=wm.acg(np.asarray(SPK[n],float),0.0005,201)
    y_all=np.array(nar,float); y_all[99:102]=0
    x=np.arange(1,101)/2; y=y_all[(x*2).astype(int)+100]
    if not np.all(np.isfinite(y)): return [np.nan]*4
    a0=np.array([20,1,30,2,0.5,5,1.5,2],float)
    lb=np.array([1,0.1,0,0,-30,0,0.1,0],float); ub=np.array([500,50,500,15,50,20,5,100],float)
    out=[]
    for a,yy in [(a0,y),(a0*(1+1e-9),y),(a0,y*(1+1e-12)),(a0*(1-1e-9),y)]:
        r=least_squares(lambda p: wm._acg_model(p,x)-yy,a,bounds=(lb,ub),method="trf",max_nfev=2000)
        sst=np.sum((yy-yy.mean())**2); out.append(1-np.sum(r.fun**2)/sst if sst>0 else np.nan)
    return out
from joblib import Parallel, delayed
t0=time.time()
R=np.array(Parallel(n_jobs=4)(delayed(fits)(n) for n in range(len(NT))))
print("s",time.time()-t0)
np.save(os.environ['TMPDIR']+"/k/acgstab.npy",R)
c=R>0.3
print("R2>0.3 counts per perturbation:", c.sum(0))
print("neurons whose classification changes under any perturbation:", int((c.any(1)&~c.all(1)).sum()))
print("max |R2 change|:", np.nanmax(np.abs(R[:,1:]-R[:,[0]])))
print("neurons with R2 change > 1e-3:", int((np.abs(R[:,1:]-R[:,[0]])>1e-3).any(1).sum()))
print("R2 nearest 0.3:", np.sort(np.abs(R[:,0]-0.3))[:5])
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/k/acgstab.py
```

```
s 454.2266206741333
R2>0.3 counts per perturbation: [316 315 317 316]
neurons whose classification changes under any perturbation: 2
max |R2 change|: 0.3091939945808464
neurons with R2 change > 1e-3: 61
R2 nearest 0.3: [0.00114277 0.00187139 0.00244205 0.00305477 0.00325326]
```

**Agent calls Bash**

```bash
cd  grep -n "id: fig4c" -A40 claims/kussovska-2025.yaml; grep -n "id: fig6e" -A40 claims/kussovska-2025.yaml
```

```
672:- id: fig4c-encoding-bursts-vs-poisson
673-  statement: During encoding, population bursting did not exceed a rate-matched Poisson null for
674-    most neuronal groups; it differed from the null only for all neurons and for the low mean ACG
675-    amplitude group.
676-  source: Results, Bursting dynamics reorganize spiking activity between encoding and
677-    maintenance, paragraph 2; Figure 4c
678-  quote: During encoding, population bursting did not exceed a rate-matched Poisson null
679-    (Wilcoxon signed-rank; Fig. 4c) for most neuronal groups. Significant effects were detected
680-    for all neurons (W = 9.0, P = 0.003) and for the group with low mean ACG amplitude (W = 0.0,
681-    P = 0.012).
682-  statistics:
683-  - about: all neurons
684-    test: Wilcoxon signed-rank
685-    statistic: W = 9.0
686-    p: 0.003
687-    corrected: FDR
688-  - about: low mean ACG amplitude
689-    test: Wilcoxon signed-rank
690-    statistic: W = 0.0
691-    p: 0.012
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 712,730p claims/kussovska-2025.yaml; sed -n 1189,1215p claims/kussovska-2025.yaml
```

```
candidates "within 70 ms of a previous event were suppressed", run as a variant with a
    spacing of 1 bin. Surrogate threshold;
    the real data's (code) or each surrogate's own. Groups; (a) median split within participant
    on mean ACG amplitude and on tau decay, participants with fewer than 5 neurons in a group
    left out (Methods), (b) the code's 6 lowest and 6 highest of participants with at least 10
    neurons (lines 52, 95-120, 164-172); groups use neurons with R2 > 0.3 (acg-fit-yield);
    "all neurons" is all 902 (code, line 183; participants with at least 10 neurons, line 185)
    or the 294 fitted neurons; concept cells need at
    least 3 per participant (code) or 5 (Methods). Reproduced when, under one reading, all
    neurons and low ACG differ from the null with corrected p < 0.05 and the other four groups
    do not; partially reproduced when the two named groups differ and one other does too.
- id: fig4d-maintenance-bursts-vs-poisson
  statement: During maintenance, bursting exceeded the Poisson null for all neurons pooled and
    for the low and high mean ACG and short and long tau decay groups, but not for concept
    cells.
  source: Results, Bursting dynamics reorganize spiking activity between encoding and
    maintenance, paragraph 3; Figure 4d
  quote: During maintenance, bursting exceeded the Poisson null across most groups (Fig. 4d)
  statistics:
  depends_on:
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1138,1180p $TMPDIR/k/7906b08125.txt; sed -n 1264,1370p $TMPDIR/k/7906b08125.txt
```

```
#### CELL 76 markdown None
**Result: reproduced.** 316 neurons have R2 > 0.3 under reading (a) and 298 under reading (b),
both within tolerance. The firing rate and ISI CV of reading (a) equal the code's shipped table
exactly, and the normalized mean ACG and Royer burst index agree within 1% for 99% of neurons, so
the code used every spike of the unit. The fit itself is a limitation of this attempt: the fitted
R2 agrees with the shipped MATLAB values within 1% for only 48% of neurons and the time constants
for 6 to 11% (printed above), as scipy's optimizer finds other local optima than MATLAB's.
Classification at R2 > 0.3 agrees for 97.6% of neurons, but tau_rise is a clustering feature, so
the cell types of fig5c differ from the paper's, and tau_decay defines the decay groups of the
burst analyses. The round-1 run of this notebook, with the same code, gave 317 under reading (a), so
one neuron's fit falls on either side of the threshold between runs, and with it the reading (a)
types of a few neurons.
#### CELL 77 markdown None
## fig5c-cell-type-clusters

> Spectral clustering on firing rate, mean normalised ACG and ACG rise time constant split the 294
> neurons into two clusters, 92 putative pyramidal neurons and 202 putative interneurons.
#### CELL 78 code ['claim:fig5c-cell-type-clusters']
TYPES = {}
for reading in ["a", "b"]:
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; sed -n 457,610p wm.py
```

```
def concat_trials(spike_lists, win):
    """Concatenate per-trial relative spike times (each in [0, win]) into one train."""
    parts = [np.asarray(s) + i * win for i, s in enumerate(spike_lists) if len(s)]
    return np.concatenate(parts) if parts else np.array([])


def spectral_types(features, random_state=42):
    """Spectral clustering on standardised firing rate, normalised mean ACG and tau_rise
    (07_spectral_clustering.py: StandardScaler, SpectralClustering(n_clusters=2,
    affinity='nearest_neighbors', random_state=42)). The cluster with the higher median firing
    rate is labelled IN (Results, Feature-based classification, paragraph 3)."""
    from sklearn.cluster import SpectralClustering
    from sklearn.preprocessing import StandardScaler
    X = StandardScaler().fit_transform(features[["firing_rate", "acg_norm", "tau_rise"]].values)
    lab = SpectralClustering(n_clusters=2, affinity="nearest_neighbors",
                             random_state=random_state).fit_predict(X)
    fr = features["firing_rate"].values
    in_label = 0 if np.median(fr[lab == 0]) > np.median(fr[lab == 1]) else 1
    return np.where(lab == in_label, "IN", "PY"), lab

[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1485,1616p $TMPDIR/k/7906b08125.txt
```

```
#### CELL 100 markdown None
## fig4f-all-cells-epochs

> At the population level, load 1 burst rates increased from encoding to each of the three 1 s
> maintenance windows and to the probe.

Burst detection of fig4c per epoch (encoding and probe 1 s, maintenance up to 3 s); M1 to M3 are
(a) the Methods' 1 s windows from maintenance onset (peaks counted by their time in the trial; M3
runs from 2 s to the end of maintenance, 0.5 to 0.8 s) or (b) the code's thirds of the whole
concatenated train. Paired two-sided Wilcoxon, BH over the 10 pairs of periods, per group and load.
#### CELL 101 code ['claim:fig4f-all-cells-epochs']
PER = ["enc", "M1", "M2", "M3", "probe"]
rows = []
for grule, G in GR.items():
    for rule in ["prominence", "height"]:
        for mr in ["methods", "code"]:
            for L in [1, 2, 3]:
                for g, subs in G.items():
                    for sub, nids in subs.items():
                        c = wm.epoch_burst_counts({"enc": [EP[(n, L, "enc")] for n in nids],
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1697,1800p $TMPDIR/k/7906b08125.txt
```

```
#### CELL 116 markdown None
## fig6cd-celltype-epochs

> Pyramidal burst rates stayed stable across task epochs at every load, whereas interneuron burst
> rates changed from encoding to each maintenance window and to the probe in load 1 trials.
#### CELL 117 code ['claim:fig6cd-celltype-epochs']
for g in ["PY", "IN", "PY_b", "IN_b"]:
    for L in [1, 2, 3]:
        print(f"\n{g}, load {L}:")
        print(epoch_table(g, L).to_string(index=False))
#### CELL 118 code ['claim:fig6cd-celltype-epochs']
for (grule, rule, mr), x0 in EPB.groupby(["grule", "rule", "mread"]):
    if grule != "code":
        continue
    for sfx, tlab in [("", "a"), ("_b", "b")]:
        qin = epoch_tests(x0[(x0.group == "IN" + sfx) & (x0.load == 1)])[0]
        py_sig = {L: int(sum(v < 0.05 for v in epoch_tests(x0[(x0.group == "PY" + sfx) & (x0.load == L)])[0].values())) for L in [1, 2, 3]}
        print(f"types ({tlab}), {rule}/M-{mr}: IN encoding vs M1, M2, M3, probe corrected p "
              f"{[round(qin[f'enc-{k}'], 4) for k in ['M1', 'M2', 'M3', 'probe']]}; PY pairs with corrected p < 0.05 by load {py_sig}")
#### CELL 119 markdown None
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 516,545p $TMPDIR/k/7906b08125.txt
```

```
#### CELL 40 code ['claim:concept-cells-count']
CCR = {}
rates = []
for n in range(len(NT)):
    t = T[NT["sub"].iat[n]]
    rates.append((wm.count_in(SPK[n], (t.enc1 + 0.2).values, (t.enc1 + 1.0).values) / 0.8, t.img1.values))
rows = []
for reading in ["methods", "code"]:
    for seed in range(10):
        rng = np.random.default_rng(seed)
        res = pd.DataFrame([wm.concept_test(r, im, rng, reading=reading) for r, im in rates], columns=["pref", "p", "sig"])
        CCR[(reading, seed)] = res
        reg = NT.region[res.sig.values].value_counts()
        rows.append({"reading": reading, "seed": seed, "concept": int(res.sig.sum()),
                     **{f"%{g}": round(100 * reg.get(g, 0) / max(res.sig.sum(), 1), 2) for g in ["AMY", "HPC", "dACC", "preSMA", "vmPFC"]}})
cc_tab = pd.DataFrame(rows)
print(cc_tab.to_string(index=False))
print("\nrange of counts:", cc_tab.groupby("reading").concept.agg(["min", "max"]).to_dict("index"))
CONCEPT = CCR[("code", 0)].sig.values
PREF = CCR[("code", 0)].pref.values
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
p='wm.py'; s=open(p).read()
old='''def glm_groups(real, null, groups, alpha=0.05):
    """A neuron is significant when |b1| is at or above the 95th percentile ('higher' quantile) of
    its |null|; a group's p is the fraction of null counts of significant neurons at or above the
    observed count (main_1e,f.py:172-205; no + 1, as in the code). groups: {name: index array}."""
    absn = np.abs(null)
    thr = np.quantile(absn, 1 - alpha, axis=1, method="higher")
    sig = np.abs(real) >= thr
    sig_null = absn >= thr[:, None]'''
new='''def glm_groups(real, null, groups, alpha=0.05, ties="in"):
    """A neuron is significant when |b1| is at or above the 95th percentile ('higher' quantile) of
    its |null|; a group's p is the fraction of null counts of significant neurons at or above the
    observed count (main_1e,f.py:172-205; no + 1, as in the code). groups: {name: index array}.
    The slope depends on the data only through sum(x * y), so a permutation often gives exactly the
    real slope, and a neuron can sit on its own threshold; floating-point rounding (which differs
    between machines) then decides the comparison. ties 'in' counts values within a relative 1e-9
    of the threshold as at it, the code's '>=' in exact arithmetic, so the result does not depend on
    rounding; 'out' counts them as below it (a stability check); 'raw' compares the floats as they
    are, as the code does."""
    absn = np.abs(null)
    thr = np.quantile(absn, 1 - alpha, axis=1, method="higher")
    eps = {"in": -1e-9, "out": 1e-9, "raw": 0.0}[ties]
    sig = np.abs(real) >= thr * (1 + eps)
    sig_null = absn >= (thr * (1 + eps))[:, None]'''
assert old in s; s=s.replace(old,new)
old2='''def fit_acg(acg_narrow):'''
new2='''def fit_acg(acg_narrow, start_scale=1.0):'''
assert old2 in s; s=s.replace(old2,new2)
old3='''    R2 and the parameters."""
    from scipy.optimize import least_squares'''
new3='''    R2 and the parameters. start_scale multiplies the start point (1 + 1e-9 or 1 - 1e-9 in the
    notebook's check of how far the fit depends on rounding)."""
    from scipy.optimize import least_squares'''
assert old3 in s; s=s.replace(old3,new3)
old4='''    a0 = np.array([20, 1, 30, 2, 0.5, 5, 1.5, 2], float)
    lb'''
new4='''    a0 = np.array([20, 1, 30, 2, 0.5, 5, 1.5, 2], float) * start_scale
    lb'''
assert old4 in s; s=s.replace(old4,new4)
open(p,'w').write(s)
EOF
grep -n "eps\b\|ties" wm.py | head
```

```
215:def glm_groups(real, null, groups, alpha=0.05, ties="in"):
221:    between machines) then decides the comparison. ties 'in' counts values within a relative 1e-9
227:    eps = {"in": -1e-9, "out": 1e-9, "raw": 0.0}[ties]
228:    sig = np.abs(real) >= thr * (1 + eps)
229:    sig_null = absn >= (thr * (1 + eps))[:, None]
488:    (the code's parse_spike_entry keeps 0 <= t <= TRIAL_WIN)."""
563:            order = np.lexsort((ff, v))  # stable, ties by neuron id as in the code
869:    """Sign changes of the time derivative (zero steps skipped), summed over the dimensions of a
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; cat > $TMPDIR/k/dev2.py <<'EOF'
import pickle, os, numpy as np, pandas as pd, wm, time
from joblib import Parallel, delayed
D=os.environ['TMPDIR']+"/k/"
S=pickle.load(open(D+"state.pkl","rb")); globals().update(S)
t0=time.time()
def f(n): return wm.acg_features(SPK[n])
FA=pd.DataFrame(Parallel(n_jobs=4)(delayed(f)(n) for n in range(len(NT))))
print("feat s",time.time()-t0, (FA.r2>0.3).sum())
def refit(n, sc):
    r=wm.fit_acg(wm.acg(np.asarray(SPK[n],float),0.0005,201), sc)
    return r["tau_decay"], r["tau_rise"], r["r2"]
PERT={}
for sc in [1+1e-9, 1-1e-9]:
    t0=time.time()
    PERT[sc]=np.array(Parallel(n_jobs=4)(delayed(refit)(n,sc) for n in range(len(NT))))
    print("refit s", time.time()-t0, (PERT[sc][:,2]>0.3).sum())
rates=[]
for n in range(len(NT)):
    t = T[NT["sub"].iat[n]]
    rates.append((wm.count_in(SPK[n], (t.enc1 + 0.2).values, (t.enc1 + 1.0).values) / 0.8, t.img1.values))
rng = np.random.default_rng(0)
res = pd.DataFrame([wm.concept_test(r, im, rng, reading="code") for r, im in rates], columns=["pref", "p", "sig"])
CONCEPT=res.sig.values; print("concept", CONCEPT.sum())
pickle.dump(dict(FA=FA,PERT=PERT,CONCEPT=CONCEPT), open(D+"dev2.pkl","wb"))
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/k/dev2.py; date -u
```

```
entries/kussovska-2025/wm.py:412: RuntimeWarning: invalid value encountered in scalar divide
  "acg_norm": np.nanmean(wn), "burst_royer": np.mean(wide[502:505]) / np.mean(wide[699:800]),
feat s 130.82197833061218 316
refit s 128.65051198005676 315
refit s 130.56993913650513 316
concept 58
Tue Nov 10 14:12:42 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
p='wm.py'; s=open(p).read()
s=s.replace('def fit_acg(acg_narrow, start_scale=1.0):','def fit_acg(acg_narrow, start_scale=1.0, data_scale=1.0):')
s=s.replace('''start_scale multiplies the start point (1 + 1e-9 or 1 - 1e-9 in the
    notebook's check of how far the fit depends on rounding).""''','''start_scale multiplies the start point and data_scale the ACG (by 1 +/- 1e-9
    and 1 + 1e-12 in the notebook's check of how far the fit depends on rounding)."""''')
s=s.replace('''    y = y_all[(x * 2).astype(int) + 100]
    a0''','''    y = y_all[(x * 2).astype(int) + 100] * data_scale
    a0''')
open(p,'w').write(s)
EOF
sed -n 370,395p wm.py
```

```
def fit_acg(acg_narrow, start_scale=1.0, data_scale=1.0):
    """fit_ACG.m of CellExplorer: bins -0.5 to +0.5 ms set to zero, the triple exponential fitted at
    lags 0.5 to 50 ms from the start point a0 within bounds lb, ub, by bounded nonlinear least
    squares (scipy's trust-region reflective, as MATLAB's fit uses). Returns tau_decay, tau_rise,
    R2 and the parameters. start_scale multiplies the start point and data_scale the ACG (by 1 +/- 1e-9
    and 1 + 1e-12 in the notebook's check of how far the fit depends on rounding).""""
    from scipy.optimize import least_squares
    y_all = np.array(acg_narrow, float)
    y_all[99:102] = 0
    x = np.arange(1, 101) / 2
    y = y_all[(x * 2).astype(int) + 100] * data_scale
    a0 = np.array([20, 1, 30, 2, 0.5, 5, 1.5, 2], float) * start_scale
    lb = np.array([1, 0.1, 0, 0, -30, 0, 0.1, 0], float)
    ub = np.array([500, 50, 500, 15, 50, 20, 5, 100], float)
    if not np.all(np.isfinite(y)):
        return dict(tau_decay=np.nan, tau_rise=np.nan, r2=np.nan)
    res = least_squares(lambda p: _acg_model(p, x) - y, a0, bounds=(lb, ub), method="trf",
                        max_nfev=2000)
    sse = np.sum(res.fun ** 2)
    sst = np.sum((y - y.mean()) ** 2)
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; sed -i 's|fit rounding).""""|fit rounding)."""|' wm.py; sed -i 's|R2 and the parameters. start_scale multiplies the start point and data_scale the ACG (by 1 +/- 1e-9\n|&|' wm.py; python -c "import ast;ast.parse(open('wm.py').read())" && sed -n 373,376p wm.py
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import ast;ast.parse(open('wm.py').read())
               ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/ast.py", line 50, in parse
    return compile(source, filename, mode, flags,
                   _feature_version=feature_version, optimize=optimize)
  File "<unknown>", line 376
    and 1 + 1e-12 in the notebook's check of how far the fit depends on rounding).""""
                                                                                     ^
SyntaxError: unterminated string literal (detected at line 376)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/kussovska-2025/wm.py",
 "old_string": "    R2 and the parameters. start_scale multiplies the start point and data_scale the ACG (by 1 +/- 1e-9\n    and 1 + 1e-12 in the notebook's check of how far the fit depends on rounding).\"\"\"\"",
 "new_string": "    R2 and the parameters. start_scale multiplies the start point and data_scale the ACG (by\n    1 +/- 1e-9 and 1 + 1e-12 in the notebook's check of how far the fit depends on rounding).\"\"\""
}
```

```
The file entries/kussovska-2025/wm.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python -c "import ast;ast.parse(open('wm.py').read())"; cat > $TMPDIR/k/dev3.py <<'EOF'
import pickle, os, numpy as np, pandas as pd, wm, time
from joblib import Parallel, delayed
D=os.environ['TMPDIR']+"/k/"
S=pickle.load(open(D+"state.pkl","rb")); globals().update(S)
globals().update(pickle.load(open(D+"dev2.pkl","rb")))
def refit(n):
    r=wm.fit_acg(wm.acg(np.asarray(SPK[n],float),0.0005,201), 1.0, 1+1e-12)
    return r["tau_decay"], r["tau_rise"], r["r2"]
PERT["data"]=np.array(Parallel(n_jobs=4)(delayed(refit)(n) for n in range(len(NT))))
pickle.dump(dict(FA=FA,PERT=PERT,CONCEPT=CONCEPT), open(D+"dev2.pkl","wb"))
V={"main":FA}
for k,a in PERT.items():
    F=FA.copy(); F["tau_decay"],F["tau_rise"],F["r2"]=a[:,0],a[:,1],a[:,2]; V[str(k)]=F
RN=np.load(D+"glm_load.npy"); real,null=RN[:,0],RN[:,1:]
for k,F in V.items():
    d = F[F.r2 > 0.3].dropna(subset=["firing_rate", "acg_norm", "tau_rise"])
    ty,_=wm.spectral_types(d); TY=np.array([None]*len(NT),dtype=object); TY[d.index.values]=ty
    TG = {"IN": np.where(TY == "IN")[0], "IN concept": np.where((TY == "IN") & CONCEPT)[0],
      "PY": np.where(TY == "PY")[0], "PY concept": np.where((TY == "PY") & CONCEPT)[0]}
    print(k, "yield",len(d),"PY",(ty=="PY").sum(),"IN",(ty=="IN").sum())
    for ties in ["in","out","raw"]:
        df,_=wm.glm_groups(real,null,TG,ties=ties)
        print("  ",ties, df[["group","n","significant","percent","p"]].round(3).values.tolist())
REG = {g: NT.nid[NT.region == g].values for g in ["AMY", "HPC", "dACC", "preSMA", "vmPFC"]}
for ties in ["in","out","raw"]:
    df,_=wm.glm_groups(real,null,REG,ties=ties); print("fig1e",ties,df[["group","significant","percent","p"]].round(3).values.tolist())
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/k/dev3.py 2>&1 | grep -v Warn
```

```
main yield 316 PY 102 IN 214
   in [['IN', 214, 30, 14.019, 0.001], ['IN concept', 15, 3, 20.0, 0.04], ['PY', 102, 6, 5.882, 0.478], ['PY concept', 12, 0, 0.0, 1.0]]
   out [['IN', 214, 30, 14.019, 0.0], ['IN concept', 15, 3, 20.0, 0.036], ['PY', 102, 6, 5.882, 0.338], ['PY concept', 12, 0, 0.0, 1.0]]
   raw [['IN', 214, 30, 14.019, 0.001], ['IN concept', 15, 3, 20.0, 0.038], ['PY', 102, 6, 5.882, 0.43], ['PY concept', 12, 0, 0.0, 1.0]]
1.000000001 yield 315 PY 103 IN 212
   in [['IN', 212, 30, 14.151, 0.001], ['IN concept', 15, 3, 20.0, 0.04], ['PY', 103, 6, 5.825, 0.489], ['PY concept', 12, 0, 0.0, 1.0]]
   out [['IN', 212, 30, 14.151, 0.0], ['IN concept', 15, 3, 20.0, 0.036], ['PY', 103, 6, 5.825, 0.347], ['PY concept', 12, 0, 0.0, 1.0]]
   raw [['IN', 212, 30, 14.151, 0.001], ['IN concept', 15, 3, 20.0, 0.038], ['PY', 103, 6, 5.825, 0.438], ['PY concept', 12, 0, 0.0, 1.0]]
0.999999999 yield 316 PY 101 IN 215
   in [['IN', 215, 30, 13.953, 0.001], ['IN concept', 16, 3, 18.75, 0.044], ['PY', 101, 6, 5.941, 0.472], ['PY concept', 11, 0, 0.0, 1.0]]
   out [['IN', 215, 30, 13.953, 0.0], ['IN concept', 16, 3, 18.75, 0.039], ['PY', 101, 6, 5.941, 0.327], ['PY concept', 11, 0, 0.0, 1.0]]
   raw [['IN', 215, 30, 13.953, 0.001], ['IN concept', 16, 3, 18.75, 0.042], ['PY', 101, 6, 5.941, 0.418], ['PY concept', 11, 0, 0.0, 1.0]]
data yield 317 PY 102 IN 215
   in [['IN', 215, 30, 13.953, 0.001], ['IN concept', 16, 3, 18.75, 0.044], ['PY', 102, 6, 5.882, 0.477], ['PY concept', 11, 0, 0.0, 1.0]]
   out [['IN', 215, 30, 13.953, 0.0], ['IN concept', 16, 3, 18.75, 0.039], ['PY', 102, 6, 5.882, 0.334], ['PY concept', 11, 0, 0.0, 1.0]]
   raw [['IN', 215, 30, 13.953, 0.001], ['IN concept', 16, 3, 18.75, 0.042], ['PY', 102, 6, 5.882, 0.426], ['PY concept', 11, 0, 0.0, 1.0]]
fig1e in [['AMY', 16, 6.178, 0.355], ['HPC', 9, 4.737, 0.663], ['dACC', 18, 10.526, 0.03], ['preSMA', 51, 20.4, 0.0], ['vmPFC', 7, 21.875, 0.003]]
fig1e out [['AMY', 13, 5.019, 0.372], ['HPC', 9, 4.737, 0.473], 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; cat >> $TMPDIR/k/glm.py <<'EOF'
for key in [("load","matched","within"),("load","all","within"),("rt","matched","shared"),("rt","all","within")]:
    Y,X,P=glm_design(*key); r,nl=wm.glm_fit(Y,X,P)
    for ties in ["in","out","raw"]:
        df,_=wm.glm_groups(r,nl,REG,ties=ties); print(key,ties,df[["group","significant","percent","p"]].round(3).values.tolist())
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/k/glm.py 2>&1 | tail -12
```

```
('load', 'matched', 'within') in [['AMY', 16, 6.178, 0.368], ['HPC', 10, 5.263, 0.554], ['dACC', 17, 9.942, 0.029], ['preSMA', 48, 19.2, 0.0], ['vmPFC', 6, 18.75, 0.008]]
('load', 'matched', 'within') out [['AMY', 13, 5.019, 0.375], ['HPC', 9, 4.737, 0.491], ['dACC', 17, 9.942, 0.008], ['preSMA', 47, 18.8, 0.0], ['vmPFC', 6, 18.75, 0.004]]
('load', 'matched', 'within') raw [['AMY', 14, 5.405, 0.453], ['HPC', 10, 5.263, 0.497], ['dACC', 17, 9.942, 0.018], ['preSMA', 47, 18.8, 0.0], ['vmPFC', 6, 18.75, 0.007]]
('load', 'all', 'within') in [['AMY', 15, 5.792, 0.452], ['HPC', 13, 6.842, 0.226], ['dACC', 22, 12.865, 0.0], ['preSMA', 57, 22.8, 0.0], ['vmPFC', 7, 21.875, 0.003]]
('load', 'all', 'within') out [['AMY', 12, 4.633, 0.496], ['HPC', 11, 5.789, 0.26], ['dACC', 22, 12.865, 0.0], ['preSMA', 57, 22.8, 0.0], ['vmPFC', 7, 21.875, 0.003]]
('load', 'all', 'within') raw [['AMY', 13, 5.019, 0.566], ['HPC', 12, 6.316, 0.267], ['dACC', 22, 12.865, 0.0], ['preSMA', 57, 22.8, 0.0], ['vmPFC', 7, 21.875, 0.003]]
('rt', 'matched', 'shared') in [['AMY', 23, 8.88, 0.02], ['HPC', 15, 7.895, 0.089], ['dACC', 17, 9.942, 0.029], ['preSMA', 43, 17.2, 0.0], ['vmPFC', 2, 6.25, 0.46]]
('rt', 'matched', 'shared') out [['AMY', 23, 8.88, 0.017], ['HPC', 15, 7.895, 0.08], ['dACC', 17, 9.942, 0.026], ['preSMA', 43, 17.2, 0.0], ['vmPFC', 2, 6.25, 0.447]]
('rt', 'matched', 'shared') raw [['AMY', 23, 8.88, 0.02], ['HPC', 15, 7.895, 0.089], ['dACC', 17, 9.942, 0.029], ['preSMA', 43, 17.2, 0.0], ['vmPFC', 2, 6.25, 0.46]]
('rt', 'all', 'within') in [['AMY', 28, 10.811, 0.0], ['HPC', 18, 9.474, 0.017], ['dACC', 21, 12.281, 0.001], ['preSMA', 35, 14.0, 0.0], ['vmPFC', 2, 6.25, 0.45]]
('rt', 'all', 'within') out [['AMY', 28, 10.811, 0.0], ['HPC', 18, 9.474, 0.013], ['dACC', 21, 12.281, 0.001], ['preSMA', 35, 14.0, 0.0], ['vmPFC', 2, 6.25, 0.441]]
('rt', 'all', 'within') raw [['AMY', 28, 10.811, 0.0], ['HPC', 18, 9.474, 0.017], ['dACC', 21, 12.281, 0.001], ['preSMA', 35, 14.0, 0.0], ['vmPFC', 2, 6.25, 0
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; sed -i 's/def glm_groups(real, null, groups, alpha=0.05, ties="in"):/def glm_groups(real, null, groups, alpha=0.05, ties="raw"):/' wm.py; cat > $TMPDIR/k/dev4.py <<'EOF'
import pickle, os, numpy as np, pandas as pd, wm, time
from scipy.stats import wilcoxon
D=os.environ['TMPDIR']+"/k/"
S=pickle.load(open(D+"state.pkl","rb")); globals().update(S)
globals().update(pickle.load(open(D+"dev2.pkl","rb")))
EP={}
for n in range(len(NT)):
    t_all=T[NT["sub"].iat[n]]; t=t_all[t_all.load==1]
    EP[n]=wm.epoch_spikes(SPK[n], t.enc1.values, t.enc1.values+1.0, 1.0)
V={"main":FA}
for k,a in PERT.items():
    F=FA.copy(); F["tau_decay"],F["tau_rise"],F["r2"]=a[:,0],a[:,1],a[:,2]; V[str(k)]=F
# shipped decay variant
F=FA.copy(); F["tau_decay"]=SHIP_CM["Decay"].values; V["shipDecay"]=F
FAM=["All902","LowACG","HighACG","ShortDecay","LongDecay","Concept"]
t0=time.time()
for k,F in V.items():
    for grule in ["methods","code"]:
        G=wm.burst_groups(NT,F,CONCEPT,np.array([None]*len(NT)),grule)
        for rule,dist in [("height",1),("height",2),("prominence",2)]:
            if grule=="code" and rule=="height": continue
            rows=[]
            for g in FAM:
                for sub,nids in G[g].items():
                    rng=np.random.default_rng(wm.stable_seed(g,sub,"enc",rule,dist,"real",grule))
                    rc,sc,_,_=wm.group_bursts([EP[n] for n in nids],1.0,rng,rule,dist,"real")
                    rows.append((g,sub,rc,sc))
            df=pd.DataFrame(rows,columns=["g","sub","real","sur"])
            ps=[wilcoxon(df[df.g==g].real,df[df.g==g].sur,zero_method="pratt",method="asymptotic").pvalue for g in FAM]
            q=wm.bh(ps)
            print(k,grule,rule,dist,dict(zip(FAM,np.round(q,4))))
    print(time.time()-t0)
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/k/dev4.py 2>&1 | grep -v Warn
```

```
main methods height 1 {'All902': np.float64(0.0041), 'LowACG': np.float64(0.0362), 'HighACG': np.float64(0.7954), 'ShortDecay': np.float64(0.3647), 'LongDecay': np.float64(0.8927), 'Concept': np.float64(0.8927)}
main methods height 2 {'All902': np.float64(0.0041), 'LowACG': np.float64(0.0451), 'HighACG': np.float64(0.8744), 'ShortDecay': np.float64(0.1688), 'LongDecay': np.float64(0.8927), 'Concept': np.float64(0.8927)}
main methods prominence 2 {'All902': np.float64(0.002), 'LowACG': np.float64(0.0086), 'HighACG': np.float64(0.0497), 'ShortDecay': np.float64(0.0153), 'LongDecay': np.float64(0.0421), 'Concept': np.float64(0.138)}
main code prominence 2 {'All902': np.float64(0.002), 'LowACG': np.float64(0.0181), 'HighACG': np.float64(0.3465), 'ShortDecay': np.float64(0.3465), 'LongDecay': np.float64(0.2041), 'Concept': np.float64(0.0568)}
9.669554948806763
1.000000001 methods height 1 {'All902': np.float64(0.0041), 'LowACG': np.float64(0.0362), 'HighACG': np.float64(0.6995), 'ShortDecay': np.float64(0.6995), 'LongDecay': np.float64(0.6995), 'Concept': np.float64(0.8927)}
1.000000001 methods height 2 {'All902': np.float64(0.0041), 'LowACG': np.float64(0.0362), 'HighACG': np.float64(0.6995), 'ShortDecay': np.float64(0.6995), 'LongDecay': np.float64(0.6995), 'Concept': np.float64(0.8927)}
1.000000001 methods prominence 2 {'All902': np.float64(0.002), 'LowACG': np.float64(0.0057), 'HighACG': np.float64(0.0497), 'ShortDecay': np.float64(0.0057), 'LongDecay': np.float64(0.0497), 'Concept': np.float64(0.138)}
1.000000001 code prominence 2 {'All902': np.float64(0.002), 'LowACG': np.float64(0.0086), 'HighACG': np.float64(0.3465), 'ShortDecay': np.float64(0.1895), 'LongDecay': np.float64(0.1895), 'Concept': np.float64(0.0568)}
19.097894430160522
0.999999999 methods height 1 {'All902': np.float64(0.0041), 'LowACG': np.float64(0.0289), 'HighACG': np.float64(0.8339), 'ShortDecay': np.float64(0.8339), 'LongDecay': np.float64(0.8339), 'Concept': np.float64(0.8927)}
0.999999999 meth
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1375,1484p $TMPDIR/k/7906b08125.txt
```

```
#### CELL 93 markdown None
## fig4d-maintenance-bursts-vs-poisson

> During maintenance, bursting exceeded the Poisson null for all neurons pooled and for the low and
> high mean ACG and short and long tau decay groups, but not for concept cells.

Maintenance windows of 2.8 s from onset (the code's), each trial cut at the probe.
#### CELL 94 code ['claim:fig4d-maintenance-bursts-vs-poisson']
# The 2.8 s window of the code: trials concatenated with a stride of 2.8 s, real spikes cut at the
# probe (2.53 to 2.84 s), surrogate spikes uniform over the whole 2.8 s.
BURST_M = show_bursts("maint")
print(BURST_M.round(4).to_string(index=False))
for reading, o in BURST_M.groupby("reading", sort=False):
    ok = {g: bool((o[o.group == g].p_BH < 0.05).iloc[0] and (o[o.group == g].real_above > o[o.group == g].n / 2).iloc[0])
          for g in ["All902", "LowACG", "HighACG", "ShortDecay", "LongDecay"]}
    print(f"{reading}: five named groups above the null {all(ok.values())} {ok}; concept cells corrected p "
          f"{o[o.group == 'Concept'].p_BH.iloc[0]:.3f}")
#### CELL 95 code ['claim:fig4d-maintenance-bursts-vs-poisson']
# The criterion's own-maintenance reading under every reading: each trial's own maintenance (at
# most 2.8 s) concatenated with stride = its duration, surrogate spikes drawn within it.
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "claim:" tools/entry.py | head -20; grep -n "proposed" -A12 schemas/*.json | head -60
```

```
420:            if tag.startswith("claim:"):
schemas/attempt.schema.json:303:          "proposed": {
schemas/attempt.schema.json-304-            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
schemas/attempt.schema.json-305-            "type": "object",
schemas/attempt.schema.json-306-            "additionalProperties": false,
schemas/attempt.schema.json-307-            "required": [
schemas/attempt.schema.json-308-              "outcome",
schemas/attempt.schema.json-309-              "reason"
schemas/attempt.schema.json-310-            ],
schemas/attempt.schema.json-311-            "properties": {
schemas/attempt.schema.json-312-              "outcome": {
schemas/attempt.schema.json-313-                "enum": [
schemas/attempt.schema.json-314-                  "reproduced",
schemas/attempt.schema.json-315-                  "partially_reproduced",
--
schemas/claims.schema.json:3:  "title": "Claims proposed for one target (a dataset and one of its papers)",
schemas/claims.schema.json-4-  "description": "Draft. To be revised after the pilot.",
schemas/claims.schema.json-5-  "type": "object",
schemas/claims.schema.json-6-  "additionalProperties": false,
schemas/claims.schema.json-7-  "required": [
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,440p tools/entry.py; sed -n 300,340p schemas/attempt.schema.json; grep -n '"verifications"' -A80 schemas/attempt.schema.json | grep -n '"' | head -60
```

```
def lock(entry_dir: Path, version: str | None = None) -> int:
    """Pin every package, with its hashes, for the entry's Python version, which entry.yaml then records."""
    version = version or python_of(entry_dir)
    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--generate-hashes", "--python-version", version,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        set_python(entry_dir, version)
        print(f"wrote {entry_dir.name}/requirements.lock.txt (Python {version}, with hashes)")
    return r.returncode


def tagged_outputs(notebook: Path) -> dict[str, str]:
    """The text each claim-tagged cell of an executed notebook printed, by tag."""
    import nbformat
    nb = nbformat.read(notebook, as_version=4)
    out = {}
    for cell in nb.cells:
        for tag in cell.get("metadata", {}).get("tags", []):
            if tag.startswith("claim:"):
                text = []
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
p='wm.py'; s=open(p).read()
old='''def epoch_burst_counts(neuron_trials_by_epoch, rule="prominence", distance=2, mreading="methods"):'''
new='''def epoch_burst_counts(neuron_trials_by_epoch, rule="prominence", distance=2, mreading="methods",
                       mdurs=None):'''
assert old in s; s=s.replace(old,new)
old='''    bins of the whole concatenated train (lines 216-219)."""'''
new='''    bins of the whole concatenated train (lines 216-219); 'trial': peaks counted by their time
    within the trial in the first, second and final thirds of that trial's own maintenance
    (mdurs, each trial's maintenance duration, at most 3 s), the Fig. 6c legend's "first, second,
    and final thirds of the maintenance epoch"."""'''
assert old in s; s=s.replace(old,new)
old='''    else:
        thirds = np.array_split(np.arange(len(sm)), 3)'''
new='''    elif mreading == "trial":
        t_all = pk * BURST_BIN
        d = np.minimum(np.asarray(mdurs, float), win)[np.minimum((t_all // win).astype(int), len(mdurs) - 1)]
        t_in = t_all % win
        third = np.floor(3 * t_in / np.where(d > 0, d, np.inf)).astype(int)
        for i in range(3):
            out[f"M{i + 1}"] = int(np.sum((third == i) & (t_in < d)))
    else:
        thirds = np.array_split(np.arange(len(sm)), 3)'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n "BURST_BIN =" wm.py; sed -n '/^def burst_peaks/,/^def concat/p' wm.py
```

```
427:BURST_BIN = 0.07      # s, Methods and code line 12
def burst_peaks(sm, threshold, rule="prominence", distance=2):
    """Peaks of the smoothed population count. rule 'prominence': prominence at or above the
    threshold (the code, lines 251-255, and the Results); rule 'height': local peaks whose smoothed
    value exceeds the threshold (Methods). distance in bins (2 bins = 140 ms, Methods and code)."""
    import scipy.signal as signal
    kw = {"distance": distance} if distance and distance > 1 else {}
    if rule == "prominence":
        pk, _ = signal.find_peaks(sm, prominence=threshold, **kw)
    else:
        pk, _ = signal.find_peaks(sm, height=np.nextafter(threshold, np.inf), **kw)
    return pk


def concat_trials(spike_lists, win):
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
p='wm.py'; s=open(p).read()
old='''def cv2_holt(isi):'''
new='''def refit_acg(spikes, start_scale=1.0, data_scale=1.0):
    """tau_decay, tau_rise and R2 of the ACG fit of one neuron with the start point or the ACG
    scaled (fit_acg), for the check of how far the fit depends on rounding."""
    r = fit_acg(acg(np.asarray(spikes, float), 0.0005, 201), start_scale, data_scale)
    return r["tau_decay"], r["tau_rise"], r["r2"]


def cv2_holt(isi):'''
s=s.replace(old,new,1); open(p,'w').write(s)
EOF
python -c "import ast;ast.parse(open('wm.py').read())"; date -u
```

```
Tue Nov 10 14:18:05 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import json
nb=json.load(open('entries/kussovska-2025/reproduce_kussovska_2025.ipynb'))
for i in [41,53,92,99,115,146,147,148]:
    c=nb['cells'][i]
    print('#### CELL',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
"
```

```
#### CELL 41 markdown None
**Result: reproduced.** Under the code's bootstrap (reading b) the count is 57 to 60 over ten
seeds, all within tolerance, with the amygdala share 70.18 to 72.41% and the hippocampus share
17.24 to 19.30%; seed 0 gives the paper's regional shares exactly (41, 11, 1, 2 and 3 cells). The
Methods' bootstrap (reading a) finds 49 to 54 cells, within tolerance only for two seeds. The
per-participant spread is 4.14 +/- 3.66 over the 14 participants with a concept cell, close to
the paper's 4 +/- 4. The set used in later sections is reading (b), seed 0 (a standard choice of
seed); it shares 57 of its 58 cells with the code's shipped list.
#### CELL 53 markdown None
**Result: reproduced.** Under every reading, 17 training bins in encoding or early maintenance
have off-diagonal pairs kept above chance, and no maintenance training bin generalizes to more
than 0.18 of the maintenance test bins, so the clusters are localized. The shuffled maps had no
supra-threshold cluster (their 95th-percentile extent is 0), so the Methods' cluster rule removes
nothing here. Only 3 of the 1,000 shuffled maps have a significant pair after BH, one pair each,
so the 95th percentile of their extent is 0, while the largest real cluster spans 26 bins; the
rule as run cannot remove any real cluster. The one- and
two-sided binomial tests keep the same pairs, as only accuracies above 20% are kept and both
tests then reject at the same counts.
#### CELL 92 markdown None
**Result: reproduced.** Under the Methods' groups with the height rule and the real threshold
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
p='wm.py'; s=open(p).read()
old='''def burst_groups(NT, feats, concept, types, rule="code"):'''
new='''def group_bursts_seeded(neuron_trials, win, seed, rule="prominence", distance=2, thr_mode="real", durs=None):
    """group_bursts with its own generator from a seed, for running groups in parallel processes.
    Returns (real count, mean surrogate count)."""
    rc, sc, _, _ = group_bursts(neuron_trials, win, np.random.default_rng(seed), rule, distance, thr_mode,
                                durs=durs)
    return rc, sc


def burst_groups(NT, feats, concept, types, rule="code"):'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
python -c "import ast;ast.parse(open('wm.py').read())"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/k && cat > $TMPDIR/k/edit_nb.py <<'PYEOF'
import nbformat, sys
P = "entries/kussovska-2025/reproduce_kussovska_2025.ipynb"
nb = nbformat.read(P, as_version=4)
C = nb.cells

def find(sub, start=0):
    hits = [i for i, c in enumerate(C) if sub in c.source and i >= start]
    assert len(hits) >= 1, sub
    return hits[0]

def code(src, tags):
    c = nbformat.v4.new_code_cell(src); c.metadata["tags"] = tags; return c

def md(src):
    return nbformat.v4.new_markdown_cell(src)

# ---- fig1e: tie check after the GLM cell
i = find('print("\\npaper: preSMA 19.6% (P = 0.001)')
C.insert(i + 1, code('''# Stability check. The slope depends on the data only through sum(x * y), so a permutation of the
# three load levels often gives exactly the real slope, and a neuron can sit on its own threshold.
# The comparison '>=' is then decided by floating-point rounding, which can differ between machines
# and runs. 'raw' (above) compares the floats as the code does; 'in' counts values within a relative
# 1e-9 of the threshold as at it (the code's rule in exact arithmetic), 'out' as below it.
for key in [("load", "matched", "shared"), ("load", "matched", "within"), ("load", "all", "within"),
            ("rt", "matched", "shared"), ("rt", "all", "within")]:
    (real, null), _, _ = GLM[key]
    thr = np.quantile(np.abs(null), 0.95, axis=1, method="higher")
    at = np.abs(np.abs(real) - thr) <= 1e-9 * thr
    print(f"\\n{key[0]}, trials {key[1]}, permutation {key[2]}: {int(at.sum())} neurons have |b1| within a relative 1e-9 "
          f"of their threshold {NT.region[at].value_counts().to_dict()}")
    tab = {ties: wm.glm_groups(real, null, REG, ties=ties)[0].set_index("group") for ties in ["raw", "in", "out"]}
    print(pd.DataFrame({f"{ties}_{c}": tab[ties][c] for ties in tab for c in ["significant", "percent", "p"]}).round(3).to_string())''',
    ["claim:fig1e-load-modulated-neurons", "claim:fig1f-rt-modulation-not-significant"]))

# ---- fig1e conclusion
i = find("**Result: reproduced.** Under reading (a) with the code's shared permutation, preSMA")
C[i].source = """**Result: reproduced.** Under reading (a) with the code's shared permutation, preSMA (20.00%,
50 of 250, p = 0.000), vmPFC (18.75%, p = 0.007) and dACC (10.53%, p = 0.026) are each within
tolerance with p < 0.05; the within-participant permutation gives 18.80%, 18.75% and 9.94%, also
within tolerance. With all trials (reading b) the three regions stay significant with higher
percentages (22.80%, 21.88%, 12.87%). The amygdala and hippocampus are not significant under any
reading. The stability check shows why these counts moved between runs: with load as the
predictor 8 neurons (4 in preSMA) have |b1| equal to their own null threshold up to rounding, so
the counts depend on the last bits of the fit. Counting those ties as significant (`in`) or not
(`out`), the shared permutation gives preSMA 51 or 47 neurons (20.40% or 18.80%) and vmPFC 21.88%
or 18.75%, so vmPFC leaves the tolerance when ties count; the within-participant permutation stays
within tolerance for all three regions under every tie rule (preSMA 18.80 to 19.20%, vmPFC 18.75%,
dACC 9.94%, p at most 0.029). The outcome does not depend on the rounding. With reaction time as
the predictor no neuron sits on its threshold, and the counts do not change."""

# ---- concept cells "exactly"
i = find("seed 0 gives the paper's regional shares exactly")
C[i].source = C[i].source.replace("seed 0 gives the paper's regional shares exactly (41, 11, 1, 2 and 3 cells)",
    "seed 0 gives regional shares within 0.02 points of the paper's (41, 11, 1, 2 and 3 cells; HPC\n18.97% against 18.96%, vmPFC 5.17% against 5.15%)")

# ---- fig2d contradictory sentence
i = find("The shuffled maps had no\nsupra-threshold cluster")
C[i].source = C[i].source.replace(""" The shuffled maps had no
supra-threshold cluster (their 95th-percentile extent is 0), so the Methods' cluster rule removes
nothing here.""", "")

# ---- acg-fit-yield stability cell after the fit cell
i = find('print("paper: 294 (tolerance 264.6 to 323.4)")')
C.insert(i + 1, code('''# Stability check of the fit. The same fit is rerun with the start point scaled by 1 + 1e-9 and
# 1 - 1e-9 and with the ACG scaled by 1 + 1e-12, changes at the level of floating-point rounding.
# Each variant keeps the other features of reading (a) and replaces tau_decay, tau_rise and R2.
FEATV = {"main": FEAT["a"]}
for name, ss, ds in [("start x (1 + 1e-9)", 1 + 1e-9, 1.0), ("start x (1 - 1e-9)", 1 - 1e-9, 1.0), ("ACG x (1 + 1e-12)", 1.0, 1 + 1e-12)]:
    r = np.array(wm.pmap(wm.refit_acg, [(SPK[n], ss, ds) for n in range(len(NT))]))
    FEATV[name] = FEAT["a"].assign(tau_decay=r[:, 0], tau_rise=r[:, 1], r2=r[:, 2])
TYPESV = {}
rows = []
for name, F in FEATV.items():
    d = F[F.r2 > 0.3].dropna(subset=["firing_rate", "acg_norm", "tau_rise"])
    ty, _ = wm.spectral_types(d)
    types = np.array([None] * len(NT), dtype=object)
    types[d.index.values] = ty
    TYPESV[name] = types
    dr2 = np.abs(F.r2.values - FEAT["a"].r2.values)
    rows.append({"fit": name, "R2>0.3": int((F.r2 > 0.3).sum()),
                 "class changed": int(((F.r2 > 0.3).values != (FEAT["a"].r2 > 0.3).values).sum()),
                 "|dR2|>1e-3": int(np.nansum(dr2 > 1e-3)), "max |dR2|": round(float(np.nanmax(dr2)), 3),
                 "|d tau_decay|>1%": int(np.nansum(np.abs(F.tau_decay.values - FEAT["a"].tau_decay.values) > 0.01 * np.abs(FEAT["a"].tau_decay.values))),
                 "PY": int((types == "PY").sum()), "IN": int((types == "IN").sum()),
                 "PY concept": int(((types == "PY") & CONCEPT).sum()), "IN concept": int(((types == "IN") & CONCEPT).sum()),
                 "types changed": int((types != TYPESV["main"]).sum())})
print(pd.DataFrame(rows).to_string(index=False))''', ["claim:acg-fit-yield", "claim:fig5c-cell-type-clusters", "claim:fig5kl-concept-cell-types"]))

i = find("**Result: reproduced.** 316 neurons have R2 > 0.3 under reading (a)")
C[i].source = """**Result: reproduced.** 316 neurons have R2 > 0.3 under reading (a) and 298 under reading (b),
both within tolerance. The firing rate and ISI CV of reading (a) equal the code's shipped table
exactly, and the normalized mean ACG and Royer burst index agree within 1% for 99% of neurons, so
the code used every spike of the unit. The fit itself is a limitation of this attempt: the fitted
R2 agrees with the shipped MATLAB values within 1% for only 48% of neurons and the time constants
for 6 to 11% (printed above), as scipy's optimizer finds other local optima than MATLAB's.
Classification at R2 > 0.3 agrees for 97.6% of neurons, but tau_rise is a clustering feature, so
the cell types of fig5c differ from the paper's, and tau_decay defines the decay groups of the
burst analyses. The stability check shows that the fit is not stable at the level of rounding:
changes of 1e-9 in the start point or 1e-12 in the ACG move R2 by more than 1e-3 for dozens of
neurons and give 315 to 317 well-fit neurons (the round-1 run of this notebook gave 317), with
the reading (a) types of a few neurons changing. A run on another machine can therefore give any
of these, and the cell-type counts and decay groups downstream move with them; the results that
depend on them are checked under each variant (after ext2-bursts-loads23 and in fig6e)."""

# ---- fig4f: per-trial thirds reading
i = find("Burst detection of fig4c per epoch (encoding and probe 1 s, maintenance up to 3 s)")
C[i].source = """Burst detection of fig4c per epoch (encoding and probe 1 s, maintenance up to 3 s); M1 to M3 are
(a) the Methods' 1 s windows from maintenance onset (peaks counted by their time in the trial; M3
runs from 2 s to the end of maintenance, 0.5 to 0.8 s), (b) the code's thirds of the whole
concatenated train, or (c) the first, second and final thirds of each trial's own maintenance
(peaks counted by their time in the trial), the reading of the Fig. 6c legend ("the first, second,
and final thirds of the maintenance epoch"), which the claims file does not list and which is run
here as a variant (`M-trial`; see questions/kussovska-2025.yaml). Paired two-sided Wilcoxon, BH
over the 10 pairs of periods, per group and load."""
i = find('for mr in ["methods", "code"]:\n            for L in [1, 2, 3]:')
C[i].source = C[i].source.replace('for mr in ["methods", "code"]:', 'for mr in ["methods", "code", "trial"]:').replace(
    '''"probe": [EP[(n, L, "probe")] for n in nids]}, rule, 2, mr)''',
    '''"probe": [EP[(n, L, "probe")] for n in nids]}, rule, 2, mr,
                                                  mdurs=T[sub][T[sub].load == L].maint_dur.values)''')
assert "mdurs=T[sub]" in C[i].source

# ---- variant section after the ext2 conclusion
i = find("**Result: reproduced.** Under the Methods' groups with the prominence rule, with either\nwindow reading")
new = [md("""### Fit-dependent groups: stability, and decay groups from the shipped tau decay

The low and high ACG and short and long tau decay groups, and the PY and IN groups, are built from
the ACG fit. The cell below rebuilds every group from each fit variant of the acg-fit-yield check,
and from the main features with tau decay replaced by the code's shipped MATLAB value
(`Cell_metrics.xlsx`, column `Decay`, an outside input used for comparison only), and reruns the
encoding (fig4c), 2.8 s and own maintenance (fig4d, fig4-acg-group-differences) and epoch (fig4hj,
ext2) analyses for the groups that change, with the real threshold, each group's seed unchanged."""),
code('''VAR = {k: (F, TYPESV[k]) for k, F in FEATV.items() if k != "main"}
VAR["shipped tau decay"] = (FEAT["a"].assign(tau_decay=SHIP_CM["Decay"].values), TY)
GRV = {}
for vname, (F, ty) in VAR.items():
    for grule in ["code", "methods"]:
        G = wm.burst_groups(NT, F, CONCEPT, ty, grule)
        GRV[(vname, grule)] = G
        ov = {g: f"{sum(len(set(G[g].get(s, [])) & set(GR[grule][g].get(s, []))) for s in GR[grule][g])}/{sum(len(v) for v in GR[grule][g].values())}"
              for g in ["LowACG", "HighACG", "ShortDecay", "LongDecay", "PY", "IN"]}
        print(f"{vname}, {grule} groups: neurons shared with the main groups {ov}")
RCONF = [c for c in CONFIGS if c[2] == "real"]
jobs, keys = [], []
for (vname, grule), G in GRV.items():
    for g in FAM:
        if G[g] == GR[grule][g]:
            continue
        for rule, dist, thr in RCONF:
            for epoch, key, win in [("enc", "enc", 1.0), ("maint", "maint28", 2.8), ("maint_own", "maint28", 2.8)]:
                for sub, nids in G[g].items():
                    jobs.append(([EP[(n, 1, key)] for n in nids], win, wm.stable_seed(g, sub, epoch, rule, dist, thr, grule),
                                 rule, dist, thr, MDUR[sub] if epoch == "maint_own" else None))
                    keys.append(dict(variant=vname, grule=grule, rule=rule, dist=dist, thr=thr, epoch=epoch, group=g, sub=sub))
res = wm.pmap(wm.group_bursts_seeded, jobs)
NEW = pd.DataFrame([dict(**k, real=r[0], sur=r[1]) for k, r in zip(keys, res)])
print(f"{len(jobs)} group bursts rerun")


def variant_br(vname):
    """The burst table of a variant: rerun rows for the groups that change, the main rows otherwise."""
    new = NEW[NEW.variant == vname].drop(columns="variant")
    keep = BR[BR.thr == "real"].merge(new[["grule", "group"]].drop_duplicates(), how="left", indicator=True)
    return pd.concat([keep[keep._merge == "left_only"].drop(columns="_merge"), new], ignore_index=True)


def acg_four(df):
    out = {}
    for e in ["enc", "maint"]:
        x = df[df.epoch == e].pivot(index="sub", columns="group", values="real")
        for a, b in [("LowACG", "HighACG"), ("ShortDecay", "LongDecay")]:
            xx = x[[a, b]].dropna()
            out[(e, a)] = (xx[a].median(), xx[b].median(), wilcoxon(xx[b], xx[a], zero_method="wilcox").pvalue)
    return out


rows = []
for vname in ["main"] + list(VAR):
    df0 = BR[BR.thr == "real"] if vname == "main" else variant_br(vname)
    for (grule, rule, dist), df in df0.groupby(["grule", "rule", "dist"]):
        o = real_vs_null(df[df.epoch == "enc"], FAM, ())
        named, others = fig4c_rule(o)
        ok, pc = fig4d_rule(real_vs_null(df[df.epoch == "maint_own"], FAM, ()))
        r = {"variant": vname, "reading": f"{grule}/{rule}/d{dist}/real",
             "4c named": named, "4c others": ",".join(others) or "-",
             "4c LowACG q": round(float(o[o.group == "LowACG"].p_BH.iloc[0]), 4),
             "4d five": all(ok.values()), "4d fail": ",".join(k for k, v in ok.items() if not v) or "-",
             "4d concept q": round(pc, 3)}
        if dist == 2:
            a4 = acg_four(df)
            r.update({"low>high enc p": round(a4[("enc", "LowACG")][2], 4) if a4[("enc", "LowACG")][0] > a4[("enc", "LowACG")][1] else "lower",
                      "low>high maint p": round(a4[("maint", "LowACG")][2], 4) if a4[("maint", "LowACG")][0] > a4[("maint", "LowACG")][1] else "lower",
                      "short>long enc p": round(a4[("enc", "ShortDecay")][2], 4) if a4[("enc", "ShortDecay")][0] > a4[("enc", "ShortDecay")][1] else "lower",
                      "short-long maint p": round(a4[("maint", "ShortDecay")][2], 4)})
        rows.append(r)
print(pd.DataFrame(rows).to_string(index=False))

# Epoch analyses (fig4hj, ext2) for the variants' changed ACG and decay groups.
erows = []
for (vname, grule), G in GRV.items():
    for g in ["HighACG", "LongDecay", "LowACG", "ShortDecay"]:
        for rule in ["prominence", "height"]:
            for mr in ["methods", "code", "trial"]:
                for L in [1, 2, 3]:
                    for sub, nids in G[g].items():
                        c = wm.epoch_burst_counts({"enc": [EP[(n, L, "enc")] for n in nids],
                                                   "maint": [EP[(n, L, "maint3")] for n in nids],
                                                   "probe": [EP[(n, L, "probe")] for n in nids]}, rule, 2, mr,
                                                  mdurs=T[sub][T[sub].load == L].maint_dur.values)
                        erows.append(dict(variant=vname, grule=grule, rule=rule, mread=mr, load=L, group=g, sub=sub, **c))
EPV = pd.concat([EPB.assign(variant="main"), pd.DataFrame(erows)], ignore_index=True)
rows = []
for (vname, grule, rule, mr), x0 in EPV.groupby(["variant", "grule", "rule", "mread"], sort=False):
    q = {g: epoch_tests(x0[(x0.group == g) & (x0.load == 1)])[0] for g in ["HighACG", "LongDecay", "LowACG", "ShortDecay"]}
    med = {g: x0[(x0.group == g) & (x0.load == 1)][PER].median() for g in ["HighACG", "LongDecay"]}
    hi = [k for k in ["M1", "M2", "probe"] if q["HighACG"][f"enc-{k}"] < 0.05 and med["HighACG"][k] > med["HighACG"]["enc"]]
    lo = [k for k in ["M1", "M2", "M3"] if q["LongDecay"][f"enc-{k}"] < 0.05 and med["LongDecay"][k] > med["LongDecay"]["enc"]]
    e2 = {}
    for g in ["HighACG", "LongDecay"]:
        e2[g] = all(all(x0[(x0.group == g) & (x0.load == L)][k].median() > x0[(x0.group == g) & (x0.load == L)]["enc"].median()
                        for k in ["M1", "M2", "M3"]) for L in [1, 2, 3])
    rows.append({"variant": vname, "reading": f"{grule}/{rule}/M-{mr}", "4hj high ACG up at": ",".join(hi) or "-",
                 "4hj long decay up at": ",".join(lo) or "-",
                 "4hj sig pairs low ACG, short decay": f"{sum(v < 0.05 for v in q['LowACG'].values())}, {sum(v < 0.05 for v in q['ShortDecay'].values())}",
                 "ext2 high ACG": e2["HighACG"], "ext2 long decay": e2["LongDecay"]})
print(pd.DataFrame(rows).to_string(index=False))''',
["claim:fig4c-encoding-bursts-vs-poisson", "claim:fig4d-maintenance-bursts-vs-poisson", "claim:fig4-acg-group-differences",
 "claim:fig4hj-group-epochs", "claim:ext2-bursts-loads23"]),
md("**Result: (stability check, filled in after the run)**")]
for k, c in enumerate(new):
    C.insert(i + 1 + k, c)

# ---- fig6e: variants of the fit
i = find('print("paper: IN 14.36% (P = 0.002), IN concept 21.42% (P = 0.032)')
C.insert(i + 1, code('''# Stability check: the cell types of each fit variant of acg-fit-yield, and the tie rules of fig1e.
rows = []
for vname, ty in TYPESV.items():
    TGv = {"IN": np.where(ty == "IN")[0], "IN concept": np.where((ty == "IN") & CONCEPT)[0],
           "PY": np.where(ty == "PY")[0], "PY concept": np.where((ty == "PY") & CONCEPT)[0]}
    for key in [("load", "matched", "shared"), ("load", "matched", "within"), ("load", "all", "within")]:
        (real, null), _, _ = GLM[key]
        for ties in ["raw", "in", "out"]:
            df = wm.glm_groups(real, null, TGv, ties=ties)[0].set_index("group")
            rows.append({"fit": vname, "trials": key[1], "perm": key[2], "ties": ties,
                         **{f"{g} %": round(df.at[g, "percent"], 2) for g in TGv}, **{f"{g} p": round(df.at[g, "p"], 3) for g in TGv},
                         "IN concept n": int(df.at["IN concept", "n"])})
FE = pd.DataFrame(rows)
FE["criterion met"] = (FE["IN %"].between(14.36 - 1.436, 14.36 + 1.436) & (FE["IN p"] < 0.05)
                       & FE["IN concept %"].between(21.42 - 2.142, 21.42 + 2.142) & (FE["IN concept p"] < 0.05)
                       & (FE["PY p"] >= 0.05) & (FE["PY concept p"] >= 0.05))
print(FE.to_string(index=False))
print("\\nfits under which the criterion is met by at least one reading:",
      FE[FE.ties == "raw"].groupby("fit")["criterion met"].any().to_dict())''', ["claim:fig6e-load-modulation-in"]))

nbformat.write(nb, P)
print("ok", len(nb.cells))
PYEOF
cd  && git stash list | head -2; cp entries/kussovska-2025/reproduce_kussovska_2025.ipynb $TMPDIR/k/nb_backup.ipynb; python $TMPDIR/k/edit_nb.py
```

```
ok 155
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import nbformat
P="entries/kussovska-2025/reproduce_kussovska_2025.ipynb"
nb=nbformat.read(P,as_version=4)
for c in nb.cells:
    if c.source.startswith("FEAT = {}\nfor reading in"):
        old='''FEAT = {}
for reading in ["a", "b"]:
    rows = []
    for n in range(len(NT)):
        s = SPK[n]
        if reading == "b":
            t = T[NT["sub"].iat[n]]
            keep = np.zeros(len(s), bool)
            for a_, b_ in zip(t.fix_start.values, t.timestamps_Response.values):
                i, j = np.searchsorted(s, [a_, b_])
                keep[i:j] = True
            f = wm.acg_features(s[keep])
            f["firing_rate"] = len(s) / (s[-1] - s[0])
        else:
            f = wm.acg_features(s)
        rows.append(f)
    FEAT[reading] = pd.DataFrame(rows)'''
        new='''FEAT = {}
for reading in ["a", "b"]:
    spikes = []
    for n in range(len(NT)):
        s = SPK[n]
        if reading == "b":
            t = T[NT["sub"].iat[n]]
            keep = np.zeros(len(s), bool)
            for a_, b_ in zip(t.fix_start.values, t.timestamps_Response.values):
                i, j = np.searchsorted(s, [a_, b_])
                keep[i:j] = True
            s = s[keep]
        spikes.append(s)
    rows = wm.pmap(wm.acg_features, [(s,) for s in spikes])  # 4 processes; each neuron's fit is independent
    if reading == "b":
        for n, f in enumerate(rows):
            f["firing_rate"] = len(SPK[n]) / (SPK[n][-1] - SPK[n][0])
    FEAT[reading] = pd.DataFrame(rows)'''
        assert old in c.source; c.source=c.source.replace(old,new); print("done")
nbformat.write(nb,P)
EOF
grep -n "import itertools" $TMPDIR/k/7906b08125.txt
```

```
done
1044:import itertools
```

**Agent calls Bash**

```bash
cd  python -c "
import nbformat
nb=nbformat.read('entries/kussovska-2025/reproduce_kussovska_2025.ipynb',as_version=4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code': print(i, c.metadata.get('tags'), c.source[:60].replace(chr(10),' | '))
"
```

```
1 None import time | import warnings |  | import matplotlib.pyplot as plt
3 ['sanity'] # Versions: the same assets in every published version. | vers
5 ['sanity'] subj = pd.DataFrame([{"sub": s["sub"], "age": s["subject"]["
7 ['sanity'] tr = pd.concat(T.values()) | rows = [] | for sub, t in T.items()
9 ['sanity'] # Clock check by contrast: image selectivity of each neuron 
11 ['sanity'] # Duplicate recordings: identical spike trains or identical 
13 ['sanity'] # Link of the code's trial tables to the dataset's trials (n
16 ['claim:units-by-region'] cnt = NT.region.value_counts() | print("patients:", NT["sub"].
19 ['claim:behavior-accuracy'] acc = tr.groupby("sub").correct.mean() * 100 | print(acc.round
22 ['claim:fig1c-accuracy-load1-vs-load3'] al = tr.groupby(["sub", "load"]).correct.mean().unstack() | pr
25 ['claim:behavior-rt'] c = tr[tr.correct == 1] | med = c.groupby("sub").rt.median() | m
28 ['claim:rt-in-vs-out-memory'] rng = np.random.default_rng(11) |  |  | def paired_signflip(d, rng
31 ['claim:rt-correct-vs-incorrect'] rng = np.random.default_rng(12) | d = tr.groupby(["sub", "corr
34 ['claim:fig1e-load-modulated-neurons'] REG = {g: NT.nid[NT.region == g].values for g in ["AMY", "HP
35 ['claim:fig1e-load-modulated-neurons', 'claim:fig1f-rt-modulation-not-significant'] # Stability check. The slope depends on the data only throug
38 ['claim:fig1f-rt-modulation-not-significant'] for key in [("rt", "matched", "shared"), ("rt", "matched", "
41 ['claim:concept-cells-count'] CCR = {} | rates = [] | for n in range(len(NT)): |     t = T[NT["s
44 ['claim:fig2ab-single-cells-not-persistent'] CELLS_C = np.where(CONCEPT)[0] |  |  | def pref_mask(t, pref, load
47 ['claim:fig2c-population-persistence'] def population_persistence(load, seed=42): |     D = {"enc": [
50 ['claim:ext1bc-persistence-by-load'] for load in [1, 2, 3]: |     out, sig, sigp = PERSIST[load] |   
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
import nbformat, os
nb=nbformat.read('reproduce_kussovska_2025.ipynb',as_version=4)
idx=[1,7,13,34,35,38,41,76,77,80,92,93,96,97,100,103,106,107,110,113,122,123,126,129,130]
out=["import itertools, time as _t, pickle"]
for i in idx:
    out.append(f"print('\\n######## CELL {i}', flush=True); _t0=_t.time()")
    out.append(nb.cells[i].source)
    out.append(f"print('## cell {i} took', round(_t.time()-_t0,1), 's', flush=True)")
open(os.environ['TMPDIR']+'/k/harness.py','w').write("\n".join(out))
EOF
date -u; MPLBACKEND=Agg PYTHONPATH=. timeout 3500 $TMPDIR/venv/bin/python $TMPDIR/k/harness.py > $TMPDIR/k/harness.log 2>&1; echo exit $?; date -u; grep "took\|Error\|Traceback" $TMPDIR/k/harness.log
```

```
Tue Nov 10 14:20:38 UTC 2026
exit 0
Tue Nov 10 14:40:10 UTC 2026
## cell 1 took 14.9 s
## cell 7 took 0.1 s
## cell 13 took 0.1 s
## cell 34 took 67.1 s
## cell 35 took 0.3 s
## cell 38 took 0.1 s
## cell 41 took 7.2 s
## cell 76 took 203.9 s
## cell 77 took 320.3 s
## cell 80 took 0.0 s
## cell 92 took 252.9 s
## cell 93 took 0.0 s
## cell 96 took 0.3 s
## cell 97 took 44.4 s
## cell 100 took 2.8 s
## cell 103 took 24.4 s
## cell 106 took 9.1 s
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; awk '/######## CELL 34/,/######## CELL 41/' harness.log | grep -v "^## cell"
```

```
######## CELL 34
largest |slope - sklearn slope| over 21 neurons: 1.13e-04
neurons with no maintenance spikes in the matched trials: 0

load, trials matched, permutation shared:
 group   n  significant  percent  null_mean     p
   AMY 259           14    5.405     13.341 0.463
   HPC 190            9    4.737      9.693 0.595
  dACC 171           18   10.526      8.703 0.026
preSMA 250           50   20.000     12.769 0.000
 vmPFC  32            6   18.750      1.621 0.007

load, trials matched, permutation within:
 group   n  significant  percent  null_mean     p
   AMY 259           14    5.405     13.347 0.453
   HPC 190           10    5.263      9.711 0.497
  dACC 171           17    9.942      8.711 0.018
preSMA 250           47   18.800     12.748 0.000
 vmPFC  32            6   18.750      1.627 0.007

[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; awk '/######## CELL 77/,/######## CELL 80/' harness.log; awk '/######## CELL 92/,/######## CELL 96/' harness.log | head -120
```

```
######## CELL 77
               fit  R2>0.3  class changed  |dR2|>1e-3  max |dR2|  |d tau_decay|>1%  PY  IN  PY concept  IN concept  types changed
              main     316              0           0      0.000                 0 102 214          12          15              0
start x (1 + 1e-9)     315              1          35      0.171               159 103 212          12          15              3
start x (1 - 1e-9)     316              2          39      0.309               167 101 215          11          16              3
 ACG x (1 + 1e-12)     317              1          34      0.309               161 102 215          11          16              2
## cell 77 took 320.3 s

######## CELL 80
######## CELL 92
group rule code: {'All902': '20 participants, 897 neurons', 'AllFit': '12 participants, 269 neurons', 'LowACG': '12 participants, 72 neurons', 'HighACG': '12 participants, 72 neurons', 'ShortDecay': '12 participants, 72 neurons', 'LongDecay': '12 participants, 72 neurons', 'Concept': '9 participants, 52 neurons', 'PY': '12 participants, 95 neurons', 'IN': '19 participants, 214 neurons', 'PY_b': '12 participants, 90 neurons', 'IN_b': '18 participants, 196 neurons'}
group rule methods: {'All902': '20 participants, 897 neurons', 'AllFit': '12 participants, 269 neurons', 'LowACG': '12 participants, 132 neurons', 'HighACG': '12 participants, 132 neurons', 'ShortDecay': '12 participants, 132 neurons', 'LongDecay': '12 participants, 132 neurons', 'Concept': '5 participants, 39 neurons', 'PY': '12 participants, 95 neurons', 'IN': '19 participants, 214 neurons', 'PY_b': '12 participants, 90 neurons', 'IN_b': '18 participants, 196 neurons'}
                   reading      group  n  real_median  null_median  real_above    W      p   p_BH
       code/height/d1/real     All902 20         41.5         33.1          16 13.0 0.0006 0.0047
       code/height/d1/real     LowACG 12         42.5         43.2           6 32.0 0.5829 0.9302
       code/height/d1/real    HighA
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; awk '/######## CELL 113/,/######## CELL 122/' harness.log; awk '/######## CELL 130/,0' harness.log
```

```
######## CELL 113
start x (1 + 1e-9), code groups: neurons shared with the main groups {'LowACG': '71/72', 'HighACG': '72/72', 'ShortDecay': '70/72', 'LongDecay': '71/72', 'PY': '94/95', 'IN': '212/214'}
start x (1 + 1e-9), methods groups: neurons shared with the main groups {'LowACG': '131/132', 'HighACG': '132/132', 'ShortDecay': '130/132', 'LongDecay': '131/132', 'PY': '94/95', 'IN': '212/214'}
start x (1 - 1e-9), code groups: neurons shared with the main groups {'LowACG': '70/72', 'HighACG': '72/72', 'ShortDecay': '69/72', 'LongDecay': '71/72', 'PY': '93/95', 'IN': '214/214'}
start x (1 - 1e-9), methods groups: neurons shared with the main groups {'LowACG': '130/132', 'HighACG': '132/132', 'ShortDecay': '129/132', 'LongDecay': '131/132', 'PY': '93/95', 'IN': '214/214'}
ACG x (1 + 1e-12), code groups: neurons shared with the main groups {'LowACG': '71/72', 'HighACG': '72/72', 'ShortDecay': '70/72', 'LongDecay': '71/72', 'PY': '94/95', 'IN': '214/214'}
ACG x (1 + 1e-12), methods groups: neurons shared with the main groups {'LowACG': '131/132', 'HighACG': '132/132', 'ShortDecay': '130/132', 'LongDecay': '131/132', 'PY': '94/95', 'IN': '214/214'}
shipped tau decay, code groups: neurons shared with the main groups {'LowACG': '72/72', 'HighACG': '72/72', 'ShortDecay': '47/72', 'LongDecay': '49/72', 'PY': '95/95', 'IN': '214/214'}
shipped tau decay, methods groups: neurons shared with the main groups {'LowACG': '132/132', 'HighACG': '132/132', 'ShortDecay': '107/132', 'LongDecay': '110/132', 'PY': '95/95', 'IN': '214/214'}
5400 group bursts rerun
           variant                    reading  4c named                    4c others  4c LowACG q  4d five                             4d fail  4d concept q low>high enc p low>high maint p  short>long enc p  short-long maint p
              main        code/height/d1/real     False                            -       0.9302    False LowACG,HighACG,ShortDecay,LongDecay         0.244            NaN              NaN               
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; awk '/######## CELL 103/,/######## CELL 106/' harness.log | grep -i "reading\|trial\|^All\|M3 under"; awk '/######## CELL 123/,/######## CELL 129/' harness.log
```

```
All902, load 1 (medians are bursts per window; q is BH over the 10 pairs):
                     reading  n  med_enc  med_M1  med_M2  med_M3  med_probe  med_M3_per_s   q_M1   q_M2   q_M3  q_probe  min_q_other  q_M1-M2  q_M1-M3
         code/height/M-trial 20     41.5    41.0    39.5    35.5       41.0           NaN 0.7836 0.9532 0.3489   0.9532       0.3489   1.0000   0.3489
     code/prominence/M-trial 20      6.0    16.5    13.0    13.0        5.5           NaN 0.0006 0.0006 0.0007   0.6800       0.0006   0.0155   0.1348
      methods/height/M-trial 20     41.5    41.0    39.5    35.5       41.0           NaN 0.7836 0.9532 0.3489   0.9532       0.3489   1.0000   0.3489
  methods/prominence/M-trial 20      6.0    16.5    13.0    13.0        5.5           NaN 0.0006 0.0006 0.0007   0.6800       0.0006   0.0155   0.1348
AllFit, load 1 (medians are bursts per window; q is BH over the 10 pairs):
                     reading  n  med_enc  med_M1  med_M2  med_M3  med_probe  med_M3_per_s   q_M1   q_M2   q_M3  q_probe  min_q_other  q_M1-M2  q_M1-M3
         code/height/M-trial 12     43.0    43.5    40.0    40.0       45.0           NaN 0.5632 0.4367 0.1562   0.5632       0.1562   0.4367   0.4258
     code/prominence/M-trial 12      6.5    16.5    12.5    12.0        5.5           NaN 0.0024 0.0342 0.0220   0.4579       0.0024   0.0360   0.0360
      methods/height/M-trial 12     43.0    43.5    40.0    40.0       45.0           NaN 0.5632 0.4367 0.1562   0.5632       0.1562   0.4367   0.4258
  methods/prominence/M-trial 12      6.5    16.5    12.5    12.0        5.5           NaN 0.0024 0.0342 0.0220   0.4579       0.0024   0.0360   0.0360
M3 under reading (a) lasts 0.67 s on average; its median rate per second, all neurons, prominence: 17.1 against M1 17.0
######## CELL 123
types (a), height/M-code: IN encoding vs M1, M2, M3, probe corrected p [np.float64(0.2118), np.float64(0.122), np.float64(0.1252), np.float64(0.4519)]; PY pairs with corrected p < 0.05 by load {1: 0, 2:
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^\*\*2\|^2\.\|^10\.\|Problem 2\|Problem 10\|^\*\*10\|^### \|^#### " transcripts/kussovska-2025/verifier-1-report.md | head -40
```

```
5:### A. Outcomes
55:### B. Problems
59:2. **[affects a conclusion]** Cells 59 and 67 onward: everything downstream uses `TY = TYPES["a"]`. That reading's PY count (102) is outside tolerance, and it yields 16 IN concept cells against the paper's 14. Reading (b) matches fig5c and fig5kl, but was carried into only one GLM configuration (cell 91). Claims never run with the (b) types: fig6ab, fig6cd, ext5bd, fig6f, fig6gh, ext5gh, fig6i, fig6j, fig6kl, ext5ij, and the PY/IN burst groups. The cell type is an open detail that can change these outcomes, e.g. IN concept 3/14 = 21.4% in fig6e.
75:10. **[does not affect a conclusion]** Cell 7: one subject-9 trial has 0 s maintenance and 0 s fixation. It is kept in every analysis (fixation statistics, maintenance windows) and never excluded or checked.
81:### C. Not checked, and what would have allowed it
```

**Agent calls Bash**

```bash
cd  python -c "
import nbformat
nb=nbformat.read('entries/kussovska-2025/reproduce_kussovska_2025.ipynb',as_version=4)
for i in [104,108,111,124,127,131]:
    print('####',i); print(nb.cells[i].source)
"
```

```
#### 104
**Result: partially reproduced.** Under the prominence rule all 902 neurons burst more in each of
M1, M2 and M3 than in encoding (medians 6 against 14 to 17, BH p 0.0003 to 0.035) under both
window readings, but the probe does not differ from encoding under any reading (BH p 0.61 to
0.71; medians 6.0 and 5.5). Three of the four comparisons hold. Under the Methods' windows M3 runs
from 2 s to the end of maintenance (0.67 s on average), so its count is low; per second its median
is 16.6 (prominence) and 43.2 (height), against 17 and 46.5 in M1 (`med_M3_per_s`). The M3
decreases of the height rule under these windows come from the shorter window. The outcome is
decided on the code's thirds, where all three windows have the same length.
#### 108
**Result: partially reproduced.** With the prominence rule, the code's thirds and the code's
groups, long tau decay neurons increase from encoding to M1, M2 and M3 and the low ACG, short tau
decay and concept groups have no significant pair, but high ACG neurons increase at M1 and M2 and
not at the probe (BH p 0.38). With the Methods' groups the short tau decay group has 4
significant pairs. The increases hold for one of the two groups.
#### 111
**Result: reproduced.** Under the Methods' groups with the prominence rule, with either
window reading, all cells, high ACG and long tau decay neurons have more bursts in each maintenance
window than in encoding at loads 2 and 3, as at load 1. Under the code's groups the long tau
decay group does not at loads 2 and 3; under the height rule the pattern does not hold.
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/k/edit2.py <<'PYEOF'
import nbformat
P = "entries/kussovska-2025/reproduce_kussovska_2025.ipynb"
nb = nbformat.read(P, as_version=4)
C = nb.cells
def find(sub):
    h = [i for i, c in enumerate(C) if sub in c.source]; assert len(h) == 1, (sub, h); return h[0]
def rep(sub, old, new):
    i = find(sub); assert old in C[i].source, old; C[i].source = C[i].source.replace(old, new)

# fig4c
i = find("**Result: reproduced.** Under the Methods' groups with the height rule and the real threshold")
C[i].source = """**Result: reproduced.** Under the Methods' groups with the height rule and the real threshold
and a spacing of 1 bin, all neurons (BH p 0.0054) and the low ACG group (0.0483) differ from the
Poisson null and the other four groups do not (BH p 0.36 to 0.89). The outcome rests on that
spacing, which the criterion runs as a variant (the Results' 70 ms); with its main spacing of 2
bins the low ACG group gives BH p 0.060 under the same groups and rule, and the best result under
the main spacing is the code's groups with the prominence rule, where all neurons and low ACG
differ but the concept group does too (BH p 0.045), the criterion's partial outcome. The Methods'
groups with prominence make every group but concept cells differ; with the code's groups and the
height rule the low ACG group does not differ. The reading this outcome rests on is the height
rule, under which, in fig4-acg-group-differences, low ACG neurons burst less than high ACG
neurons; the claims of Fig. 4 that hold under the prominence rule are not supported by the same
rule as this one. How this result moves with the ACG fit is checked after ext2-bursts-loads23."""

# fig4-acg
rep("**Result: partially reproduced.** Under the prominence rule the low ACG group bursts more than",
    "rule the low ACG group bursts less than the high ACG group.",
    "rule the low ACG group bursts less than the high ACG group. The tau decay groups come from this\nattempt's fit; groups built from the code's shipped tau decay are tested after ext2-bursts-loads23.")

# fig4f
rep("**Result: partially reproduced.** Under the prominence rule all 902 neurons burst more in each of",
    "decided on the code's thirds, where all three windows have the same length.",
    "decided on the code's thirds, where all three windows have the same length. The per-trial thirds\nof the Fig. 6c legend (`M-trial`, a variant) give the same: under the prominence rule M1, M2 and M3\nare above encoding (BH p 0.0006 to 0.0007) and the probe is not (0.68).")

# fig4hj
rep("**Result: partially reproduced.** With the prominence rule, the code's thirds and the code's",
    "The increases hold for one of the two groups.",
    "The increases hold for one of the two groups. With the per-trial thirds (`M-trial`) and the code's\ngroups, high ACG rise at M1 and M2 and long tau decay only at M1, and no reading makes high ACG rise\nto the probe.")

# ext2
rep("**Result: reproduced.** Under the Methods' groups with the prominence rule, with either\nwindow reading",
    "with either\nwindow reading, all cells",
    "with each of the three\nwindow readings (including the per-trial thirds), all cells")

# variant section result
i = find("**Result: (stability check, filled in after the run)**")
C[i].source = """**Result (stability check).** The fit variants change 0 to 3 neurons in each ACG, tau decay
and cell-type group; the shipped tau decay changes the decay groups more (47 and 49 of 72 neurons
kept in the code's short and long groups, 107 and 110 of 132 in the Methods'). fig4c: the Methods'
groups with the height rule and a spacing of 1 bin give the paper's pattern under the main fit,
under each of the three fit variants and with the shipped tau decay (low ACG BH p 0.0385 to
0.0483); with a spacing of 2 bins they give it under the three fit variants (0.0385 to 0.0483) but
not under the main fit or with the shipped tau decay (0.0601). So fig4c holds with the 1-bin
spacing under every fit, and with the 2-bin spacing it depends on rounding. fig4d: with the
Methods' groups and the prominence rule the five named groups exceed the null over each trial's
own maintenance under every variant, and concept cells do not (BH p 0.225 and 0.345).
fig4-acg-group-differences: with this attempt's tau decay, short does not exceed long in encoding
under the prominence rule for any fit (p 0.06 to 0.20); with the shipped tau decay it does (p
0.0078 with the code's groups, 0.0205 with the Methods'), while low ACG exceeds high ACG in both
epochs (p 0.0005) and short and long do not differ in maintenance (p 0.074 and 0.35). With the
paper's own tau decay the claim's whole pattern appears, so its shortfall here may come from this
attempt's fit; the shipped values are an outside input used for comparison only, and the outcome
is not changed. fig4hj: under every variant high ACG never rise to the probe, and with the code's
groups and thirds long tau decay rise at M1, M2 and M3 and low ACG and short tau decay have no
significant pair. ext2: with the Methods' groups and the prominence rule high ACG and long tau
decay exceed encoding at every load with the code's thirds and with the per-trial thirds under
every variant; with the Methods' 1 s windows long tau decay fails under the three fit variants and
the shipped tau decay."""

# fig6cd
rep("**Result: not reproduced.** With the prominence rule and the code's thirds, PY have no",
    "IN rise at M1 to M3 (BH p 0.0058 to 0.0074) but not at the probe (1.0).",
    "IN rise at M1 to M3 (BH p 0.0058 to 0.0074) but not at the probe (1.0). The per-trial thirds of\nthe Fig. 6c legend (`M-trial`) give the same: PY have no significant pair at any load, and IN rise\nat M1 to M3 (BH p 0.0073 to 0.032; types b 0.016 to 0.028) but not at the probe (0.65; types b 1.0).")

# ext5bd
rep("**Result: reproduced.** With the prominence rule the measure rises from load 1 to load 3 under",
    "under\nboth window readings and either group rule (code's thirds 3.67, 5.00 and 7.00; Methods' windows\n6.67, 5.67 and 7.00)",
    "under\nall three window readings and either group rule (code's thirds 3.67, 5.00 and 7.00; Methods' windows\n6.67, 5.67 and 7.00; per-trial thirds 4.67, 5.67 and 7.00)")

# fig6e
i = find("**Result: reproduced.** With the types of reading (a), matched trials and the shared")
C[i].source = """**Result: reproduced.** With the types of reading (a), matched trials and the shared
permutation, IN are load-modulated (14.02%, 30 of 214, p = 0.001) and so are IN concept cells
(20.00%, 3 of 15, p = 0.038), both within tolerance, while PY (5.88%, p = 0.43) and PY concept
cells (0%, p = 1.0) are not. The outcome rests on the cell types, and the stability check shows
that these move with rounding: two of the four fits (the main one and the start point x (1 + 1e-9))
give 15 IN concept cells and meet the criterion, and the other two give 16 IN concept cells, of
which 3 are load-modulated (18.75%, p 0.037 to 0.047), below the tolerance of 19.28 to 23.56%,
under every reading and tie rule. The tie rule of fig1e does not change the IN concept count. With
reading (b) of the types (14 IN concept cells, the paper's number), matched trials, 2 are
significant (14.29%, p = 0.15) under either permutation; with all trials 3 are (21.43%, p = 0.033,
within tolerance), but then IN give 17.68% (above tolerance) and PY 10.00% with p = 0.041. The
load modulation of IN and IN concept cells, and its absence in PY, hold under every fit; the IN
concept percentage falls within tolerance only under half of the fits, so this attempt proposes
partially reproduced (see the attempt record)."""

nbformat.write(nb, P); print("ok")
PYEOF
python $TMPDIR/k/edit2.py
```

```
ok
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import nbformat
P="entries/kussovska-2025/reproduce_kussovska_2025.ipynb"
nb=nbformat.read(P,as_version=4)
for c in nb.cells:
    if "give 15 IN concept cells and meet the criterion" in c.source:
        old="""give 15 IN concept cells and meet the criterion, and the other two give 16 IN concept cells, of
which 3 are load-modulated (18.75%, p 0.037 to 0.047), below the tolerance of 19.28 to 23.56%,
under every reading and tie rule."""
        new="""give 15 IN concept cells and meet the criterion, and the other two give 16 IN concept cells, of
which 3 are load-modulated with matched trials (18.75%, p 0.037 to 0.047, below the tolerance of
19.28 to 23.56%) under every permutation and tie rule, and 4 with all trials (25.00%, above it)."""
        assert old in c.source; c.source=c.source.replace(old,new)
nbformat.write(nb,P)
EOF
python -c "
import nbformat
nb=nbformat.read('entries/kussovska-2025/reproduce_kussovska_2025.ipynb',as_version=4)
print(nb.cells[-1].source)" | sed -n 1,5p
```

```
## Summary

| Claim | Outcome |
|---|---|
| units-by-region | reproduced |
```

**Agent**

Now the summary table and the "How the analysis differs" paragraph.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import nbformat
P="entries/kussovska-2025/reproduce_kussovska_2025.ipynb"
nb=nbformat.read(P,as_version=4)
c=nb.cells[-1]
reps=[("| fig4c-encoding-bursts-vs-poisson | reproduced |","| fig4c-encoding-bursts-vs-poisson | reproduced (Methods' groups, height rule, 1-bin spacing variant) |"),
("| fig6e-load-modulation-in | reproduced (types of reading a; not with the types of reading b) |",
 "| fig6e-load-modulation-in | reproduced (types of reading a under two of four fits; not with the types of reading b); partially reproduced proposed |"),
("""counts match the paper's; only fig6e differs between the two (reproduced with the types of
reading a, not with those of b).""","""counts match the paper's; only fig6e differs between the two (reproduced with the types of
reading a, not with those of b). The scipy fit is not stable at the level of rounding: changes of
1e-9 in its start point give 315 to 317 well-fit neurons and move the types and groups of a few
neurons, which explains why counts changed between runs; the fit-dependent results are rerun under
each variant, and only fig6e changes (its IN concept share is within tolerance under two of the
four fits). The GLM's significance rule compares slopes that are often tied exactly with a null
slope, so a few neurons sit on their threshold; the results are shown with ties counted in and
out. M1 to M3 are also run as the per-trial thirds of the Fig. 6c legend, a reading the claims
file does not list (asked in questions/kussovska-2025.yaml); no outcome changes with it.""")]
for a,b in reps:
    assert a in c.source, a; c.source=c.source.replace(a,b)
nbformat.write(nb,P)
EOF
cat entries/kussovska-2025/README.md
```

```
# Kussovska, Kim & Rungratsameetaweemana (2025) from dandiset 000469

Tests the findings of [Kussovska et al. (2025)](https://doi.org/10.1101/2025.10.31.684900) on
[DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), the human single-neuron
recordings of Kyzar et al. (2024) during a Sternberg working memory task, which the paper reuses.

| Claims | Outcome |
|---|---|
| Units by region, behavior (accuracy, load effect, reaction times) | Reproduced (6) |
| Load-modulated neurons (Fig. 1e) | Reproduced |
| RT-modulated neurons not significant (Fig. 1f) | Not reproduced; the paper's values come from the code's use of subject 1's reaction times for every neuron |
| Concept cells, single-cell and population persistence, cross-temporal decoding | Reproduced (6) |
| Maintenance decoding within participant, load 1 / load 2 | Reproduced / partially reproduced |
| Bin-width decoding / pairwise comparisons / load 2 | Partially reproduced / not reproduced / reproduced |
| dPCA state-space analyses (Fig. 3) | Reproduced (3); for Fig. 3h only with a dPCA setting other than the code's |
| Population bursts against the Poisson null, encoding and maintenance; loads 2 and 3 | Reproduced (3) |
| Burst differences between ACG groups and across epochs (Fig. 4f-j) | Partially reproduced (3) |
| ACG fits, cell-type clusters and their features, rodent validation, concept cell types | Reproduced (6) |
| Cell-type bursting (Fig. 6a-d), IN load dependence | Partially reproduced (6a,b), not reproduced (6c,d), reproduced (load dependence) |
| Load and RT modulation by cell type (Fig. 6e,f) | Reproduced (with one of the two cell-type readings) / not reproduced |
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p="entries/kussovska-2025/README.md"; s=open(p).read()
a="| Load and RT modulation by cell type (Fig. 6e,f) | Reproduced (with one of the two cell-type readings) / not reproduced |"
b="| Load and RT modulation by cell type (Fig. 6e,f) | Reproduced (with one of the two cell-type readings, and under two of four rounding-level variants of the ACG fit; partially reproduced is proposed) / not reproduced |"
assert a in s; s=s.replace(a,b); open(p,"w").write(s)
EOF
python tools/entry.py check entries/kussovska-2025 2>&1 | tail -5; date -u
```

```
0 error(s)
Tue Nov 10 14:42:05 UTC 2026
```

**Agent calls Bash**

```bash
cd  (time python tools/entry.py all entries/kussovska-2025) > $TMPDIR/k/run.log 2>&1; echo exit $?; tail -15 $TMPDIR/k/run.log; date -u
```

```
exit 0
Installed kernelspec registry-kussovska-2025 in executed/kussovska-2025/.venv/share/jupyter/kernels/registry-kussovska-2025
0 error(s)
pass  reproduce_kussovska_2025.ipynb  (3132 s)
pass  dpca_kussovska_2025.ipynb  (1368 s)

real	75m8.683s
user	250m36.625s
sys	1m5.138s
Tue Nov 10 15:57:16 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - > $TMPDIR/k/exec.txt <<'EOF'
import nbformat
nb=nbformat.read('executed/kussovska-2025/reproduce_kussovska_2025.ipynb',as_version=4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        t="".join(o.get('text','') or str(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
        print(f"######## CELL {i} {c.metadata.get('tags')}\n{t}")
EOF
grep -c "" $TMPDIR/k/exec.txt; diff <(awk '/######## CELL 34 /,/######## CELL 41 /' $TMPDIR/k/exec.txt | grep -v "^##") <(awk '/######## CELL 34$/,/######## CELL 41$/' $TMPDIR/k/harness.log | grep -v "^##") | head; grep -n "Traceback\|Error" $TMPDIR/k/exec.txt | head
```

```
2264
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; for c in 34 35 77 92 103 113 123 126 130; do a=$(awk -v s="######## CELL $c " '$0 ~ "^"s {f=1; next} /^######## CELL/ {f=0} f' exec.txt | md5sum); b=$(awk -v s="######## CELL $c" '$0==s {f=1; next} /^######## CELL|^## cell/ {f=0} f' harness.log | md5sum); echo "$c $a $b"; done
```

```
34 e630c72765dab1c3e1808a44302c76cc  - 8a43a543b6b65a763b4ee932987ee3f2  -
35 ce7701d08f45b23bff538a250cf05117  - 61f5b05cfc92ca3ce4f4df93463f80a9  -
77 26b53753735dd62fccce246c09945a08  - 6e9c2c35e637ff8971cfe684d3ad5ac7  -
92 734f7b03cfc730e4fec9941c7a5394d2  - 022a55714e4196920d5424c959b23a0a  -
103 2937e7feac1e96c0816a3847a6f04a91  - cd3f3c6d3673f005cf42627f262de220  -
113 929a894064e31e1615d46e86a76d4e0c  - 6b67c9458b71d037a4612dae35a36237  -
123 f9d5e643591967ce37ad10df806ba726  - e32445f1822b2e3368b21b83957e8693  -
126 8d92951cd820b7cb1fa542fdf7138a01  - 475e14cc360f2acaa3886ce4d740848e  -
130 5a4cb25c732989b2ed6a90b0bf488fd2  - ea0eaa3637e91de25e349e22143805ce  -
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; awk '/######## CELL 77 /{f=1} /######## CELL 80 /{f=0} f' exec.txt; awk '/######## CELL 35 /{f=1} /######## CELL 38 /{f=0} f' exec.txt | head -20
```

```
######## CELL 77 ['claim:acg-fit-yield', 'claim:fig5c-cell-type-clusters', 'claim:fig5kl-concept-cell-types']
               fit  R2>0.3  class changed  |dR2|>1e-3  max |dR2|  |d tau_decay|>1%  PY  IN  PY concept  IN concept  types changed
              main     316              0           0      0.000                 0 102 214          12          15              0
start x (1 + 1e-9)     315              1          35      0.171               159 103 212          12          15              3
start x (1 - 1e-9)     316              2          39      0.309               167 101 215          11          16              3
 ACG x (1 + 1e-12)     317              1          34      0.309               161 102 215          11          16              2

######## CELL 35 ['claim:fig1e-load-modulated-neurons', 'claim:fig1f-rt-modulation-not-significant']

load, trials matched, permutation shared: 8 neurons have |b1| within a relative 1e-9 of their threshold {'preSMA': 4, 'AMY': 3, 'vmPFC': 1}
        raw_significant  raw_percent  raw_p  in_significant  in_percent   in_p  out_significant  out_percent  out_p
group                                                                                                              
AMY                  14        5.405  0.463              16       6.178  0.355               13        5.019  0.372
HPC                   9        4.737  0.595               9       4.737  0.663                9        4.737  0.473
dACC                 18       10.526  0.026              18      10.526  0.030               18       10.526  0.021
preSMA               50       20.000  0.000              51      20.400  0.000               47       18.800  0.000
vmPFC                 6       18.750  0.007               7      21.875  0.003                6       18.750  0.005

load, trials matched, permutation within: 5 neurons have |b1| within a relative 1e-9 of their threshold {'AMY': 3, 'HPC': 1, 'preSMA': 1}
        raw_significant  raw_percent  raw_p  i
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; for c in 92 103 113 123 126 130; do awk -v s="######## CELL $c " 'index($0,s)==1 {f=1; next} /^######## CELL/ {f=0} f' exec.txt | sed 's/ *$//' | grep -v "^$" > e$c.txt; awk -v s="######## CELL $c" '$0==s {f=1; next} /^######## CELL|^## cell/ {f=0} f' harness.log | sed 's/ *$//' | grep -v "^$" > h$c.txt; echo "$c: $(diff e$c.txt h$c.txt | wc -l) diff lines"; done; diff e103.txt h103.txt | head
```

```
92: 0 diff lines
103: 0 diff lines
113: 0 diff lines
123: 0 diff lines
126: 0 diff lines
130: 0 diff lines
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/k; awk '/######## CELL 107 /{f=1} /######## CELL 113 /{f=0} f' exec.txt; grep -A2 "CELL 153" exec.txt
```

```
######## CELL 107 ['claim:fig4hj-group-epochs']
code/height/M-code: high ACG up at {'M1': False, 'M2': False, 'probe': False}; long tau decay up at {'M1': False, 'M2': False, 'M3': False}; significant pairs in low ACG, short tau decay, concept {'LowACG': 0, 'ShortDecay': 0, 'Concept': 0}
code/height/M-methods: high ACG up at {'M1': False, 'M2': False, 'probe': False}; long tau decay up at {'M1': True, 'M2': False, 'M3': False}; significant pairs in low ACG, short tau decay, concept {'LowACG': 6, 'ShortDecay': 5, 'Concept': 5}
code/height/M-trial: high ACG up at {'M1': False, 'M2': False, 'probe': False}; long tau decay up at {'M1': False, 'M2': False, 'M3': False}; significant pairs in low ACG, short tau decay, concept {'LowACG': 0, 'ShortDecay': 0, 'Concept': 0}
code/prominence/M-code: high ACG up at {'M1': True, 'M2': True, 'probe': False}; long tau decay up at {'M1': True, 'M2': True, 'M3': True}; significant pairs in low ACG, short tau decay, concept {'LowACG': 0, 'ShortDecay': 0, 'Concept': 0}
code/prominence/M-methods: high ACG up at {'M1': True, 'M2': True, 'probe': False}; long tau decay up at {'M1': True, 'M2': False, 'M3': False}; significant pairs in low ACG, short tau decay, concept {'LowACG': 6, 'ShortDecay': 0, 'Concept': 5}
code/prominence/M-trial: high ACG up at {'M1': True, 'M2': True, 'probe': False}; long tau decay up at {'M1': True, 'M2': False, 'M3': False}; significant pairs in low ACG, short tau decay, concept {'LowACG': 0, 'ShortDecay': 0, 'Concept': 0}
methods/height/M-code: high ACG up at {'M1': False, 'M2': False, 'probe': False}; long tau decay up at {'M1': False, 'M2': False, 'M3': False}; significant pairs in low ACG, short tau decay, concept {'LowACG': 0, 'ShortDecay': 0, 'Concept': 0}
methods/height/M-methods: high ACG up at {'M1': True, 'M2': True, 'probe': False}; long tau decay up at {'M1': False, 'M2': False, 'M3': False}; significant pairs in low ACG, short tau decay, concept {'LowACG': 6, 'ShortDecay': 6, 'Concept': 0}
methods/h
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/  runtime_minutes: 46/  runtime_minutes: 52/' entries/kussovska-2025/entry.yaml; sed -i 's/the analysis, about 45 minutes on four CPUs/the analysis, about 52 minutes on four CPUs/' entries/kussovska-2025/README.md; grep -n "runtime\|minutes" entries/kussovska-2025/entry.yaml entries/kussovska-2025/README.md; ls questions | head -3; cat questions/$(ls questions | head -1) | head -40
```

```
entries/kussovska-2025/entry.yaml:15:  runtime_minutes: 52
entries/kussovska-2025/entry.yaml:18:  runtime_minutes: 22
entries/kussovska-2025/README.md:32:- `reproduce_kussovska_2025.ipynb`: the analysis, about 52 minutes on four CPUs.
entries/kussovska-2025/README.md:33:- `dpca_kussovska_2025.ipynb`: the dPCA claims (Fig. 3), about 22 minutes on four CPUs.
README.md
ashworth-2025.yaml
athalye-2023.yaml
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
amended and why. Each question has `claim`, `question`, `passage`, `why` (how the misreading could
change the outcome), and, once answered, `answer` and `answered` (a date). Method details the claims
file lacks are not asked here: the author takes them from the paper, and a detail the paper does not
settle is a question for the paper's authors, recorded in the claim's notes and as a
`methods_unavailable` finding in the attempt. Files from before protocol `pilot-11` also hold
questions about method details, asked under the earlier rule.
```

**Agent calls Bash**

```bash
cd  cat questions/ashworth-2025.yaml | head -30; grep -rn "Fig. 6c\|thirds" paper/ 2>/dev/null | head; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "questions/kussovska-2025.yaml",
 "content": "dandiset: \"000469\"\npaper: doi:10.1101/2025.10.31.684900\nquestions:\n- claim: fig6cd-celltype-epochs\n  asked: 2026-11-10\n  question: >-\n    The criterion reads M1 to M3 as the Methods' three consecutive 1 s windows from maintenance\n    onset or as the code's thirds of the whole concatenated train. The Fig. 6c legend defines them\n    as \"the first, second, and final thirds of the maintenance epoch\", that is, thirds of each\n    trial's own maintenance (2.53 to 2.84 s here). Should the criterion list this as a third reading\n    of M1 to M3, here and in the claims that use the same windows (fig4f-all-cells-epochs,\n    fig4hj-group-epochs, ext2-bursts-loads23, ext5bd-in-load-dependence)?\n  passage: >-\n    Fig. 6 legend, panel c, \"Burst counts across task epochs (encoding; maintenance M1, M2, M3;\n    probe) in load 1 trials for pyramidal neurons (PY), where M1, M2, and M3 denote the first,\n    second, and final thirds of the maintenance epoch.\" The Results (Distinct temporal activity\n    patterns, paragraph 3) say \"Dividing the maintenance period into three consecutive 1 s windows\n    (M1-M3) yielded the same pattern\", and the Methods (Burst detection) give 1 s windows.\n  why: >-\n    The three readings count different bursts in M3: the Methods' third window runs from 2 s to\n    the end of maintenance (0.5 to 0.8 s), the code's thirds split the trials and not the\n    maintenance, and the legend's thirds last 0.84 to 0.95 s each. The verifier of round 2 noted\n    that the claims file misses the legend's reading. It was run here as a variant (M-trial) for\n    all five claims and gives the same outcomes as the readings the criteria list (for fig6cd, PY\n    have no significant pair at any load and IN rise at M1 to M3 but not at the probe), so it does\n    not change an outcome here.\n- claim: fig4f-all-cells-epochs\n  asked: 2026-11-10\n  question: >-\n    As for fig6cd-celltype-epochs, the criterion's M1 to M3 are the Methods' 1 s windows or the\n    code's thirds of the concatenated train; should the per-trial thirds of the maintenance epoch,\n    the definition of the Fig. 6c legend, be added as a reading?\n  passage: >-\n    Fig. 6 legend, panel c, \"M1, M2, and M3 denote the first, second, and final thirds of the\n    maintenance epoch\"; Methods, Burst detection, three 1 s windows.\n  why: >-\n    The M3 count depends on the window: under the Methods' windows M3 lasts 0.67 s on average and\n    its count is lower. Under the legend's thirds (run here as a variant, M-trial) all neurons\n    burst more in M1, M2 and M3 than in encoding (BH p 0.0006 to 0.0007) and the probe does not\n    differ (0.68), as under the listed readings, so the outcome does not change here.\n"
}
```

```
File created successfully at: questions/kussovska-2025.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
s=open('attempts/kussovska-2025-01.yaml').read()
d=yaml.safe_load(s)
for w in [100,102,105]:
    out=yaml.safe_dump(d,sort_keys=False,width=w,allow_unicode=True)
    print(w, out==s, sum(a!=b for a,b in zip(out.splitlines(),s.splitlines())))
EOF
```

```
100 True 0
102 False 1121
105 False 1104
```

**Agent calls Bash**

```bash
cat > $TMPDIR/k/rec.py <<'PYEOF'
import yaml
P = "attempts/kussovska-2025-01.yaml"
d = yaml.safe_load(open(P))
O = {o["claim"]: o for o in d["outcomes"]}

def addnote(c, text):
    O[c]["notes"] = O[c]["notes"].rstrip() + " " + text

# fig1e
O["fig1e-load-modulated-neurons"]["measured"] = [20.0, 18.75, 10.53]
O["fig1e-load-modulated-neurons"]["notes"] = (
    "Reading (a) with the code's shared permutation gives preSMA 20.00% (50 of 250, p = 0.000), vmPFC 18.75% "
    "(p = 0.007), dACC 10.53% (p = 0.026), all within tolerance; the within-participant permutation gives 18.80%, "
    "18.75%, 9.94% (p 0.000 to 0.018). With all trials (reading b) 22.80%, 21.88% and 12.87%, all significant. AMY "
    "and HPC are not significant under any reading. With load as the predictor 8 neurons (4 in preSMA) have |b1| "
    "equal to their own null threshold up to rounding, as the slope depends on the data only through sum(x * y), so "
    "the counts depend on floating-point rounding (the round-1 run gave preSMA 51). Counting those ties as "
    "significant or not, the shared permutation gives preSMA 51 or 47 and vmPFC 21.88% (outside tolerance) or "
    "18.75%; the within-participant permutation stays within tolerance for all three regions under every tie rule.")
O["fig1e-load-modulated-neurons"]["deviations"].append(
    "Significance compares the floats as the code does; ties of |b1| with the null threshold within a relative 1e-9 "
    "are also counted in and out as a stability check (wm.glm_groups).")
addnote("fig1f-rt-modulation-not-significant",
        "With reaction time as the predictor no neuron sits on its null threshold, so the counts do not depend on rounding.")

# acg-fit-yield
O["acg-fit-yield"]["notes"] = (
    "316 neurons with R2 > 0.3 when all spikes are used (reading a) and 298 with spikes within trials (reading b); "
    "R2 >= 0.3 gives the same. The firing rate and ISI CV equal the code's shipped table, and normalised mean ACG "
    "and burst index agree within 1% for 99% of neurons; the fitted R2 agrees within 1% for 48% of neurons, "
    "tau_rise for 6% and tau_decay for 11%, and the threshold classification for 97.6%. The fit is not stable at "
    "the level of rounding: rerun from a start point scaled by 1 + 1e-9 or 1 - 1e-9, or on the ACG scaled by "
    "1 + 1e-12, it moves R2 by more than 1e-3 for 34 to 39 neurons (at most 0.31) and tau_decay by more than 1% for "
    "159 to 167, and gives 315, 316 and 317 well-fit neurons (the round-1 run gave 317), all within tolerance. The "
    "scipy fit is a limitation of this attempt; tau_rise is a clustering feature, so the cell types differ from the "
    "paper's.")
addnote("fig5c-cell-type-clusters",
        "Under the rounding-level variants of the reading (a) fit (acg-fit-yield) reading (a) gives PY 101 to 103 and IN 212 to 215.")
O["fig5kl-concept-cell-types"]["notes"] = (
    "Reading (b) types: 11 PY and 14 IN concept cells; median Royer burst index PY 0.949 against IN 0.390, Holt "
    "CV2 1.217 against 0.991. Reading (a): 12 and 15, also within tolerance, same ordering; under the rounding-level "
    "variants of the fit (acg-fit-yield) 11 or 12 PY and 15 or 16 IN concept cells (the round-1 run had 11 and 16).")

# fig4c
O["fig4c-encoding-bursts-vs-poisson"]["notes"] = (
    "Under the Methods' groups with the height rule, the real threshold and a spacing of 1 bin (the Results' 70 ms, "
    "which the criterion runs as a variant), all neurons (W = 14, BH p 0.0054) and low ACG (W = 7, 0.0483) differ "
    "from the Poisson null and the other four groups do not (BH p 0.36 to 0.89). The outcome rests on that variant: "
    "with the criterion's main spacing of 2 bins low ACG has BH p 0.060, and the best result under the main spacing "
    "is the code's groups with the prominence rule, where all neurons and low ACG differ but concept cells do too "
    "(BH p 0.045), the criterion's partial outcome. With the Methods' groups and prominence every group but concept "
    "cells differs; with the code's groups and the height rule low ACG does not differ. Under the rounding-level "
    "variants of the ACG fit and with the code's shipped tau decay, the 1-bin reading gives the pattern every time "
    "(low ACG BH p 0.0385 to 0.0483), and the 2-bin reading under the three fit variants only (0.0385 to 0.0483; "
    "0.0601 under the main fit and the shipped tau decay). The reading is the height rule, under which low ACG "
    "neurons burst less than high ACG neurons (fig4-acg-group-differences), so no single peak rule supports Fig. 4 "
    "as a whole.")
addnote("fig4d-maintenance-bursts-vs-poisson",
        "The Methods' groups with the prominence rule give the pattern over each trial's own maintenance under every "
        "rounding-level variant of the ACG fit and with the code's shipped tau decay (concept cells BH p 0.225 and 0.345).")
O["fig4-acg-group-differences"]["notes"] = (
    "Prominence rule: low ACG bursts more than high ACG in encoding and maintenance in 12 of 12 participants "
    "(p = 0.0005, BH over 28 pairs at most 0.0017), and short and long tau decay do not differ in maintenance (p 0.62 "
    "to 0.85); short tau decay does not exceed long tau decay in encoding (p 0.20 code groups, 0.086 Methods groups; "
    "0.06 to 0.20 under the rounding-level variants of the fit). Height rule: low ACG bursts less than high ACG. "
    "With tau decay groups built from the code's shipped MATLAB tau decay (an outside input, for comparison only; "
    "47 and 49 of the 72 code-group neurons shared with this attempt's short and long groups) short exceeds long in "
    "encoding (p 0.0078 code groups, 0.0205 Methods groups) and they do not differ in maintenance (p 0.074, 0.35), "
    "the claim's whole pattern, so the shortfall here may come from this attempt's fit of tau decay.")
O["fig4-acg-group-differences"]["deviations"].append(
    "Decay groups from the code's shipped Cell_metrics.xlsx column Decay are run for comparison only; no outcome rests on them.")
addnote("fig4f-all-cells-epochs",
        "The per-trial thirds of maintenance of the Fig. 6c legend, a reading the claims file does not list (asked in "
        "questions/kussovska-2025.yaml), give the same under the prominence rule: M1 to M3 above encoding (BH p 0.0006 "
        "to 0.0007), the probe not (0.68).")
addnote("fig4hj-group-epochs",
        "With the per-trial thirds of the Fig. 6c legend (a variant) and the code's groups high ACG rise at M1 and M2 "
        "and long tau decay at M1 only; no reading makes high ACG rise to the probe, also under the rounding-level "
        "variants of the fit and with the code's shipped tau decay.")
O["ext2-bursts-loads23"]["notes"] = (
    "With the Methods' groups and the prominence rule, under each of the three window readings (the Methods' 1 s "
    "windows, the code's thirds and the per-trial thirds of the Fig. 6c legend, a variant), all cells, high ACG and "
    "long tau decay have more bursts in each maintenance window than in encoding (median over participants) at loads "
    "1, 2 and 3. With the code's groups long tau decay does not at loads 2 and 3; with the height rule the pattern "
    "does not hold. Under the rounding-level variants of the fit and with the code's shipped tau decay the pattern "
    "holds with the code's thirds and the per-trial thirds; with the Methods' windows long tau decay fails.")
addnote("fig6cd-celltype-epochs",
        "The per-trial thirds of the Fig. 6c legend (a variant; asked in questions/kussovska-2025.yaml) give the same: "
        "PY no significant pair at any load, IN up at M1 to M3 (BH p 0.0073 to 0.032; types b 0.016 to 0.028) and not "
        "at the probe (0.65; types b 1.0).")
addnote("ext5bd-in-load-dependence",
        "Per-trial thirds of the Fig. 6c legend (a variant): 4.67, 5.67, 7.00 (types b 4.83, 5.83, 6.83).")

# fig6e
O["fig6e-load-modulation-in"]["notes"] = (
    "Types of reading (a), matched trials, shared permutation: IN 14.02% (30 of 214, p = 0.001) and IN concept "
    "20.00% (3 of 15, p = 0.038), both within tolerance; PY 5.88% (p = 0.43) and PY concept 0% (p = 1.0) not "
    "significant. The outcome rests on the types, which move with rounding: of four fits that differ only by "
    "rounding-level changes (acg-fit-yield), two give 15 IN concept cells and meet the criterion, and two give 16, "
    "with 3 load-modulated (18.75%, p 0.037 to 0.047, outside tolerance) with matched trials under every permutation "
    "and tie rule; the round-1 run, whose fit kept 317 neurons, also had 16 and 18.75%. Types of reading (b): IN "
    "concept 14.29% (p = 0.15) with matched trials; with all trials 21.43% (p = 0.033) but IN 17.68% and PY 10.00% "
    "with p = 0.041. Under every fit IN and IN concept cells are load-modulated (p < 0.05) and PY are not.")
O["fig6e-load-modulation-in"]["proposed"] = {
    "outcome": "partially_reproduced",
    "reason": (
        "The stability check added in round 2 (reproduce_kussovska_2025.ipynb, the fit variants of acg-fit-yield and "
        "the second fig6e cell) shows that the criterion is met under two of four ACG fits that differ only at the "
        "level of floating-point rounding; under the other two there are 16 IN concept cells and the IN concept share "
        "is 18.75% (p 0.037 to 0.047), below the tolerance of 19.28 to 23.56%, under every permutation and tie rule, "
        "and with the types of reading (b), which match the paper's counts, it is 14.29% (p = 0.15). The load "
        "modulation of IN and IN concept cells and its absence in PY hold under every fit, so the effect is present "
        "but the percentage the criterion tests is met only in part.")}

# findings
for f in d["findings"]:
    if f["statement"].startswith("Question for the authors: which peak rule detects population bursts"):
        f["statement"] = (
            "Question for the authors: which peak rule detects population bursts, a smoothed value above the 90th "
            "percentile (Methods) or a prominence at or above it (Results and code), and what are the threshold of "
            "the surrogates and the minimum spacing (140 ms in the Methods, 70 ms in the Results)? Fig. 4c is "
            "reproduced only under the Methods' height rule with the Methods' groups and a spacing of 70 ms (1 bin); "
            "with the Methods' 140 ms low ACG has BH p 0.060, and under the code's prominence rule concept cells also "
            "differ from the null.")
    if f["statement"].startswith("The ACG features of the code's shipped Cell_metrics.xlsx"):
        f["statement"] = (
            "The ACG features of the code's shipped Cell_metrics.xlsx (firing rate, normalised mean ACG, burst index, "
            "ISI CV) are recomputed from the dandiset's spike times to within 1% for 99% of units, using every spike "
            "of the unit; the fitted R2 and time constants come from MATLAB's optimizer and differ for part of the "
            "units in a scipy port, which gives 316 well-fit units in place of 294. The triple-exponential fit is "
            "sensitive at the level of rounding: changing its start point by a factor 1 +/- 1e-9 or the ACG by "
            "1 + 1e-12 moves R2 by more than 1e-3 for 34 to 39 units and gives 315 to 317 well-fit units, so results "
            "built on it (cell types, tau decay groups) can differ between machines.")
d["findings"].append({"kind": "other", "statement": (
    "In the paper's GLM test (01_task/main_1e,f.py:172-205) a neuron is significant when |b1| is at or above the "
    "95th percentile of its permutation null. With load (three levels) as the predictor, the slope depends on the "
    "data only through sum(x * y), so many permutations give exactly the real slope, and 8 of the 902 neurons have "
    "|b1| equal to their threshold; floating-point rounding then decides them. Counting them in or out moves preSMA "
    "between 47 and 51 significant neurons and vmPFC between 6 and 7 with the code's shared permutation.")})
open(P, "w").write(yaml.safe_dump(d, sort_keys=False, width=100, allow_unicode=True))
print("ok")
PYEOF
python $TMPDIR/k/rec.py
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/k/rec2.py <<'PYEOF'
import yaml
P = "attempts/kussovska-2025-01.yaml"
d = yaml.safe_load(open(P))
r1 = {r["claim"]: r for r in d["verifications"][0]["results"]}
P2 = ("Problem 2: everything downstream uses the reading (a) types, whose PY count (102) is outside tolerance and "
      "which yield 16 IN concept cells against the paper's 14; the claim was never run with the (b) types, an open "
      "detail that can change the outcome.")
for c in ["fig6ab-celltype-bursts-vs-null", "fig6cd-celltype-epochs", "ext5bd-in-load-dependence", "fig6e-load-modulation-in",
          "fig6f-rt-modulation-in-concept", "fig6gh-in-concept-cv2", "ext5gh-py-decay-preferred", "fig6i-py-bin-width-decoding",
          "fig6j-in-bin-width-decoding", "fig6kl-cross-temporal-by-type", "ext5ij-load2-decoding-by-type"]:
    r1[c]["reason"] = r1[c]["reason"].rstrip() + " " + P2
P10 = ("Problem 10 (does not affect a conclusion): one subject-9 trial has 0 s maintenance and 0 s fixation; it is "
       "kept in every analysis (fixation statistics, maintenance windows) and never excluded or checked.")
R10 = (" Problem 10: the data check now prints both subject-9 trials (0 s maintenance, trial 29; 31 us fixation, "
       "trial 89), shows that no neuron fires in that fixation and that leaving it out changes the fixation statistics "
       "little, and the maintenance trial is recorded as a finding; both are kept, as in the code.")
for c in ["fig2c-population-persistence", "fig4d-maintenance-bursts-vs-poisson"]:
    r1[c]["reason"] = r1[c]["reason"].rstrip() + " " + P10
    r1[c]["response"] = ("" if r1[c]["response"] == "No change." else r1[c]["response"].rstrip()) + R10
    r1[c]["response"] = r1[c]["response"].strip()

G = ("One of the 39 outcomes left as they were after round 1; the printed values in the re-run support it.")
reasons = {
 "fig1e-load-modulated-neurons": (
  "Agrees. Cell 35 says preSMA 20.40% (p = 0.000), vmPFC p = 0.009, dACC p = 0.025 and, within participant, "
  "preSMA 19.20%, but cell 34 prints preSMA 20.000% (50 of 250), vmPFC p 0.007, dACC p 0.026 and within-participant "
  "preSMA 18.800%; the record's notes repeat the round-1 values and measured lists 20.4. The outcome is unchanged, "
  "since 20.0 and 18.8 are both inside 17.64-21.56. The fig1e GLM went from 51 to 50 significant preSMA neurons "
  "between runs with fixed seeds; a likely cause is the |b1| >= 95th-percentile-of-null rule flipping on "
  "floating-point ties."),
 "fig1f-rt-modulation-not-significant": G,
 "concept-cells-count": (
  "Agrees. Cell 41 says 'seed 0 gives the paper's regional shares exactly', but the notebook prints HPC 18.97% and "
  "vmPFC 5.17% against the paper's 18.96% and 5.15%, so 'exactly' is too strong. Point 8 (the downstream concept "
  "set is a single seed) is accepted with no change; it does not affect a conclusion."),
 "fig2d-cross-temporal-localized": (
  "Agrees. Cell 53 has 'The shuffled maps had no supra-threshold cluster' next to 'Only 3 of the 1,000 shuffled maps "
  "have a significant pair'; those three pairs are clusters of extent 1, and it is the 95th percentile of extents "
  "that is 0. Point 6 (cluster rule) is resolved."),
 "fig2e-maintenance-decoding-amy-mtl": G + " Point 7 (chance level) is resolved by the binomial tests against 20%.",
 "fig2f-bin-width-decoding": G + " Points 7 (chance level) and 9 (trial-draw spread) are resolved.",
 "fig3abc-trajectory-complexity": (
  "Agrees (now tested). Maintenance medians are higher than encoding under both measures and both trial readings "
  "(dpca cell 12). Most of the gap comes from the longer maintenance window: over the first 499 bins tortuosity is "
  "2.46-2.57 against 2.16, and 9 reversals against 8, which the record says. The rank-sum p values treat the 500 "
  "values as independent, which they are not, but the criterion uses only medians."),
 "fig3d-encoding-vs-maintenance-separability": (
  "Agrees, but only under reading (b), the code's own trial-selection bug, which the record reports as a finding "
  "(dpca cell 9): H = 457.62, maintenance in its own space against maintenance projected onto encoding p = 0.077; "
  "under reading (a), the same trials in both epochs, those two conditions differ (p = 0.019). The criterion names "
  "(b) as a reading, so the outcome stands; it is the code's result, not one independent of it."),
 "fig3h-early-vs-late-maintenance": (
  "Agrees, with protect=[] for the early half (H = 410 and 413; dpca cell 15). Under the code's own setting the "
  "early half separates less than the late half in all 100 splits; that setting gives H = 394 and 380, also inside "
  "the tolerance, but in the wrong direction. The record states this, and the outcome is the code's result under "
  "one reading."),
 "fig4c-encoding-bursts-vs-poisson": (
  "Agrees only by the letter of the criterion. It now passes only under methods/height/d1/real (cells 90-91); the "
  "criterion calls the 1-bin spacing a variant and the 2-bin spacing the main reading. With 2 bins low ACG has BH "
  "p = 0.0601, so it fails; in round 1 the same reading passed with 2 bins (BH p 0.038 / 0.048), so one "
  "run-to-run change in the ACG fit moved it across 0.05. Under the main spacing the best result, code/prominence/d2, "
  "meets the criterion's partial condition (all neurons and low ACG, plus concept cells, BH p 0.045). I would record "
  "this as weak; the record's wording ('rests on one named reading') understates that it is the 1-bin variant. "
  "Fig. 4 still has no single peak rule supporting it as a whole."),
 "fig4d-maintenance-bursts-vs-poisson": (
  "Agrees. It now uses the criterion's own-maintenance reading, and the control in cell 95 justifies that choice; "
  "under it methods/prominence gives the pattern with all three threshold settings, and concept cells have BH p "
  "0.09-0.35. Point 3 (2.8 s window) is resolved. The τdecay groups were never checked against groups built from "
  "the shipped Decay column."),
 "fig4-acg-group-differences": (
  "Agrees. The τdecay groups come from a scipy fit that agrees with the shipped MATLAB τdecay for only 11% of "
  "neurons (cell 75); the record states this as a limitation but never compares its groups with groups built from "
  "the shipped Decay column, which bears on short vs long τdecay here. No single peak rule supports Fig. 4 as a "
  "whole (disclosed, not resolved)."),
 "fig4f-all-cells-epochs": (
  "Agrees. Point 4 (M3 rates per second) is resolved. The claims file misses one paper statement: the Fig. 6c "
  "legend defines M1-M3 as 'the first, second, and final thirds of the maintenance epoch', while the criterion cites "
  "only the Methods' 1 s windows and the code's thirds of the whole train; per-trial thirds of maintenance are a "
  "third reading that was not run."),
 "fig4hj-group-epochs": (
  "Agrees. The τdecay groups were never checked against groups built from the shipped Decay column, which bears on "
  "this claim; no single peak rule supports Fig. 4 as a whole."),
 "ext2-bursts-loads23": (
  "Agrees. The τdecay groups were never checked against groups built from the shipped Decay column, which bears on "
  "the decay groups here."),
 "acg-fit-yield": (
  "Agrees. The notes and the finding say '317 in an earlier run of the same code, so one unit lies at the "
  "threshold', but the fig1e GLM also changed between runs (51 to 50 significant preSMA neurons) and does not use "
  "the ACG fit, so the change is not explained by one neuron at the R2 threshold. Results change between runs with "
  "fixed seeds (ACG yield 317 to 316, fig4c low ACG 0.048 to 0.060, fig6e IN concept 18.75% to 20.00%); two repeat "
  "runs and a stability check would settle it. Point 5 (ACG fit) is stated as a limitation."),
 "fig5c-cell-type-clusters": G + " Point 2 (types b downstream) is resolved.",
 "fig5kl-concept-cell-types": G,
 "fig6cd-celltype-epochs": (
  "Agrees; now not reproduced, as I said in round 1. The claims file misses the Fig. 6c legend's definition of "
  "M1-M3 as thirds of the maintenance epoch, a third reading that was not run."),
 "fig6e-load-modulation-in": (
  "Agrees by the letter of the criterion, but the result is fragile. IN concept cells are 3 of 15 = 20.00% with "
  "p = 0.038 (cell 124). This rests on the reading (a) cell types, whose PY count (102) is outside the fig5c "
  "tolerance, and on a fit that kept one more neuron in round 1, giving 16 IN concept cells and 18.75%. With the "
  "reading (b) types, which have the paper's 14 IN concept cells, the matched-trial result is 14.29% with p = 0.15. "
  "Partially reproduced would describe the evidence better; the notes do disclose all of this."),
 "fig6gh-in-concept-cv2": G + " Point 12 (cross-trial intervals) is resolved by the within-trial CV2 variant.",
 "ext5gh-py-decay-preferred": G + " Point 12 is resolved; spike counts are stated.",
 "ext5bd-in-load-dependence": G + " No single peak rule supports Fig. 4 as a whole (disclosed, not resolved).",
}
NC = "No change."
responses = {
 "fig1e-load-modulated-neurons": (
  "Conclusion and notes corrected to this run's numbers, and measured to 20.0. A stability check now counts the "
  "neurons whose |b1| equals their null threshold up to rounding (8 with the shared permutation, 4 in preSMA) and "
  "gives every result with these ties counted in and out: the shared permutation moves preSMA between 47 and 51 and "
  "vmPFC between 6 and 7 (21.88%, outside tolerance, with ties in), and the within-participant permutation stays "
  "within tolerance for all three regions under every rule, so the outcome does not depend on rounding. Recorded "
  "as a finding. Outcome unchanged."),
 "fig1f-rt-modulation-not-significant": "The tie check is also run for reaction time: no neuron sits on its threshold. Outcome unchanged.",
 "concept-cells-count": "'Exactly' replaced by the printed shares and the paper's (HPC 18.97 against 18.96%, vmPFC 5.17 against 5.15%). Outcome unchanged.",
 "fig2d-cross-temporal-localized": "The sentence that the shuffled maps had no supra-threshold cluster is removed; the conclusion keeps that 3 of 1,000 shuffled maps have one significant pair and that the 95th percentile of their extents is 0. Outcome unchanged.",
 "fig4c-encoding-bursts-vs-poisson": (
  "Conclusion, notes and the peak-rule finding now say that the outcome rests on the 1-bin spacing, which the "
  "criterion runs as a variant, and that under the main 2-bin spacing the best result is the partial one. A "
  "stability check reruns the groups under three rounding-level variants of the ACG fit and with the shipped tau "
  "decay: the 1-bin reading gives the pattern every time (low ACG BH p 0.0385 to 0.0483), the 2-bin reading under "
  "the three fit variants and not under the main fit or the shipped tau decay (0.0601). This explains the "
  "round-1 to round-2 change. The outcome is kept as verified, since the criterion reproduces under one of the "
  "readings it names and that reading holds under every fit."),
 "fig4d-maintenance-bursts-vs-poisson": "The stability check and the shipped-tau-decay groups give the same pattern with the Methods' groups and the prominence rule under every variant. Outcome unchanged.",
 "fig4-acg-group-differences": (
  "Decay groups built from the shipped Decay column are now run (47 and 49 of 72 code-group neurons shared): with "
  "them short tau decay exceeds long in encoding (p 0.0078 and 0.0205) and they do not differ in maintenance, the "
  "claim's whole pattern, so the shortfall may come from this attempt's fit; the notes say so. The shipped values "
  "are an outside input used for comparison only, so the outcome is kept as verified."),
 "fig4f-all-cells-epochs": (
  "The per-trial thirds of the Fig. 6c legend are run as a third reading (M-trial) and the place where the claims "
  "file misses it is asked in questions/kussovska-2025.yaml; it gives the same result (M1 to M3 above encoding, "
  "probe not). Outcome unchanged."),
 "fig4hj-group-epochs": "The shipped-tau-decay groups, the fit variants and the per-trial thirds are run; high ACG never rise to the probe under any of them. Outcome unchanged.",
 "ext2-bursts-loads23": "The shipped-tau-decay groups, the fit variants and the per-trial thirds are run; with the Methods' groups and the prominence rule the pattern holds with the code's thirds and the per-trial thirds under every variant. Outcome unchanged.",
 "acg-fit-yield": (
  "A stability check reruns the fit from a start point scaled by 1 +/- 1e-9 and on the ACG scaled by 1 + 1e-12: R2 "
  "moves by more than 1e-3 for 34 to 39 neurons and the yield is 315 to 317, so the fit is sensitive at the level "
  "of rounding, which explains the run-to-run changes of the yield, types and groups; the GLM change has a separate "
  "cause, ties at the threshold (fig1e). Notes and finding corrected. Results built on the fit are rerun under each "
  "variant. Repeat runs on this machine give the same numbers (the full re-run here matches the development run "
  "exactly), so the variants stand for runs on other machines. Outcome unchanged."),
 "fig5c-cell-type-clusters": "Type counts under the fit variants are printed (reading a PY 101 to 103). Outcome unchanged.",
 "fig5kl-concept-cell-types": "Concept-cell type counts under the fit variants are printed (11 or 12 PY, 15 or 16 IN). Outcome unchanged.",
 "fig6cd-celltype-epochs": "The per-trial thirds are run as a variant and asked in questions/kussovska-2025.yaml; they give the same result (IN not different at the probe). Outcome unchanged.",
 "ext5bd-in-load-dependence": "The per-trial thirds are run as a variant; the measure rises under the prominence rule. Outcome unchanged.",
 "fig6e-load-modulation-in": (
  "The fit variants show that two of four rounding-level fits give 15 IN concept cells and meet the criterion and "
  "two give 16, with 18.75% (outside tolerance) under every permutation and tie rule. The verified outcome is kept "
  "and partially reproduced is proposed under proposed, with this analysis in the notebook."),
 "fig3d-encoding-vs-maintenance-separability": NC,
 "fig3h-early-vs-late-maintenance": NC,
}
results = []
for o in d["outcomes"]:
    c = o["claim"]
    results.append({"claim": c, "agrees": True, "outcome": o["outcome"], "reason": reasons.get(c, G),
                    "response": responses.get(c, NC)})
d["verifications"].append({
    "date": "2026-11-10", "kind": "agent",
    "by": "Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)",
    "reviewed": ("Round 2: the full executed notebooks reproduce_kussovska_2025.ipynb (149 cells) and "
                 "dpca_kussovska_2025.ipynb (18 cells) with their conclusions and summaries, wm.py, the README and "
                 "the attempt record after the round-1 revision."),
    "results": results})
open(P, "w").write(yaml.safe_dump(d, sort_keys=False, width=100, allow_unicode=True))
print(len(results))
PYEOF
python $TMPDIR/k/rec2.py; cd  python tools/entry.py check entries/kussovska-2025 2>&1 | tail -5; date -u
```

```
45
0 error(s)
Tue Nov 10 16:00:09 UTC 2026
```

**Agent calls Bash**

```bash
cd  git diff -U0 | grep "^+" | grep -n "—\|rather" | head; grep -n "—\| rather" questions/kussovska-2025.yaml; git status --short
```

```
M attempts/kussovska-2025-01.yaml
 M entries/kussovska-2025/README.md
 M entries/kussovska-2025/entry.yaml
 M entries/kussovska-2025/reproduce_kussovska_2025.ipynb
 M entries/kussovska-2025/wm.py
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
?? questions/kussovska-2025.yaml
?? scripts
```

**Agent**

I made no outcome changes, as round 2 requires. One change is proposed for round 3: **fig6e-load-modulation-in**, reproduced → partially reproduced. The entry was re-run with `python tools/entry.py all entries/kussovska-2025`: both notebooks pass (52 min and 23 min), `check` reports 0 errors, and the conclusions match the new numbers.

**Why fig6e is proposed as partial.** I refitted the ACG model with changes the size of floating-point rounding (the start point ×(1 ± 1e-9), the ACG ×(1 + 1e-12)). Two of the four fits give 15 IN concept cells and meet the criterion. The other two give 16, and the IN concept share drops to 18.75% (p 0.037 to 0.047), below the tolerance, under every permutation and tie rule. With the types of reading (b) it is 14.29% (p = 0.15). The load modulation of IN and IN concept cells, and its absence in PY, holds under every fit. The reason is under `proposed` and the analysis is in the notebook.

**Run-to-run instability (the verifier's main open point), now explained:**
- **GLM:** with load as the predictor, 8 neurons have |b1| exactly equal to their own null threshold, so rounding decides whether they count. Counting them in or out moves preSMA between 47 and 51 neurons and vmPFC between 6 and 7. fig1e still holds under every tie rule with the within-participant permutation. I added this as a finding.
- **ACG fit:** the rounding-size changes above give 315 to 317 well-fit neurons and move R2 by more than 1e-3 for 34 to 39 neurons. This is why the yield, cell types, fig4c and fig6e moved between runs. A repeat run on this machine gives identical numbers, so the variants stand in for runs on other machines.

**Other additions:**
- **fig4c:** I rebuilt the groups under each fit variant and with the shipped τdecay. With the 1-bin spacing the pattern holds every time (low ACG BH p 0.0385 to 0.0483). With the criterion's main 2-bin spacing it holds under 3 of the 5. The conclusion, notes and peak-rule finding now say the outcome rests on the 1-bin variant and that the best result under the main spacing is partial.
- **τdecay groups from the shipped `Decay` column:** fig4d, fig4hj and ext2 keep their outcomes with these groups. For fig4-acg-group-differences they give the claim's whole pattern: short exceeds long in encoding (p 0.0078 and 0.0205). So the partial outcome may come from my fit. The shipped values are an outside input used only for comparison, so I kept the outcome and said this in the notes.
- **Per-trial thirds of maintenance (Fig. 6c legend):** run as a third M1–M3 reading for fig4f, fig4hj, ext2, fig6cd and ext5bd. It changes no outcome. The claims file's omission is now a question in the new `questions/kussovska-2025.yaml`, for fig6cd and fig4f; the claims themselves are unchanged.

**Text corrections:**
- **fig1e:** the stale values are fixed in cell 35, the record's notes, and `measured` (now 20.0).
- **concept-cells-count:** "exactly" is removed from the seed-0 regional shares.
- **fig2d:** the sentence contradicting the shuffled-map counts is removed.
- **Findings:** the acg-fit-yield and peak-rule findings are corrected.
- **Round-1 reasons:** problems 2 and 10 are added to the claims they bear on.
- **Round 2:** recorded under `verifications` for all 45 claims.

**Not done:**
- No repeat runs on other machines. The rounding-size variants and tie rules stand in for them.
- fig3d and fig3h are unchanged; their dependence on the code's trial selection and protect setting was already disclosed.
- fig4c and fig4-acg-group-differences keep their verified outcomes, for the reasons given above.

**Code changes:**
- `wm.py`: `glm_groups` takes a tie rule, and the fit takes the rounding-size changes.
- The ACG feature cell now runs in parallel; its results are unchanged.
- `entry.yaml` and the README now give the 52-minute run time.

Nothing is committed. Untracked dotfiles and a `scripts` directory in the repository root were not created by this work, and I left them alone.

## End of run

71 turns, 126 minutes, $7.04 at API prices, result: success.
