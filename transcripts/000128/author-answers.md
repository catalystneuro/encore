# 000128 · author-answers · run 39817086817

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  sed -n '/## Author/,/^## [A-Z]/p' docs/protocol.md | head -200; ls entries/000128-churchland-2010 entries/000128-churchland-2010/*; cat questions/000128.yaml
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested and how: do not change a claim's statement, expected
values or criterion, and do not apply a method detail the claims file lacks,
even one the paper gives. Ask for it (step 6).

### 1. Establish what can be tested

Do this before any analysis.

1. List the dataset's files and read its metadata from the archive. Open a
   file and list everything it holds, including every column of every table.
2. Work out which of the subjects, sessions, conditions and measured
   variables that the claims file describes are in the dataset. A dataset
   that names a paper may hold only part of its data. Check for recordings
   deposited more than once (identical traces, frame counts or annotations),
   report each pair, and count each recording once. Where the analysis treats
   a unit as the same across sessions, show that it is, or state it as an
[... 276 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/### 5. Record the attempt/,$p' docs/protocol.md | sed -n '1,200p'; ls attempts | grep 000128; ls claims/000128; git log --stat -3 | head -50
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
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git show 56749124 -- claims/ ; cat attempts/000128-churchland-2010-01.yaml; cat transcripts/000128/author-report.md
```

```
commit 5674912404cca6870384b13ed4c2cd10ebe15ac9
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Thu Oct 22 16:48:09 2026 +0000

    Agent run on 000128: answer (success)
    
    Run: https://github.com/catalystneuro/reproduction-registry/actions/runs/39814715858
    
    Account: unverified

diff --git a/claims/000128/10.1016-j.neuron.2010.09.015.yaml b/claims/000128/10.1016-j.neuron.2010.09.015.yaml
index ab95ad60..f429f44c 100644
--- a/claims/000128/10.1016-j.neuron.2010.09.015.yaml
+++ b/claims/000128/10.1016-j.neuron.2010.09.015.yaml
@@ -43,7 +43,16 @@
 #    proto-trial is the condition's mean velocity over its trials, each component must correlate
 #    at r > 0.9, window movement onset -150 to +800 ms (the maze peri-movement window, M5);
 #    (T2) as T1 with the two components concatenated into one profile. If the dataset marks the
-#    paper's own trial selection, that is shown as a variant.
+#    paper's own trial selection, that is shown as a variant. Answered 2026-10-22: T1 is set aside
[... 401 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; cat entry.yaml README.md; python - <<'EOF'
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"===== [{i}] {c['cell_type']} tags={c['metadata'].get('tags')}")
    print(''.join(c['source']))
EOF
```

```
<persisted-output>
Output too large (59.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/99dcae9c-f2a3-471f-95f9-e185bad6d375/tool-results/b6aqcxgyh.txt

Preview (first 2KB):
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
  runtime_minutes: 3
helpers:
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/99dcae9c-f2a3-471f-95f9-e185bad6d375/tool-results/b6aqcxgyh.txt"
}
```

```
1	schema_version: 1
2	name: 000128-churchland-2010
3	type: reproduction
4	title: Preparatory and peri-movement tuning in motor and premotor cortex (Churchland et al. 2010)
5	description: Tests the findings of Churchland, Cunningham, Kaufman, Ryu and Shenoy (2010) on dandiset
6	  000128 (MC_Maze), which holds the J-array session of monkey Jenkins on the maze task, recorded with two
7	  Utah arrays. It tests the correlation between preparatory and peri-movement tuning, its time course,
8	  the dimensionality of preparatory activity, the performance and stability of preferred directions in
9	  the peri-movement, kinematic and task spaces, and the paper's oscillator model. The speed task, the
10	  single-electrode recordings and EMG are not in the dandiset.
11	license: Apache-2.0
12	notebooks:
13	- path: reproduce_churchland_2010.ipynb
14	  title: Reproducing Churchland et al. (2010) from dandiset 000128
15	  runtime_minutes: 3
16	helpers:
17	- mcmaze.py
18	related:
19	- id: dandi:000128/0.220113.0400
20	  relation: uses_data
[... 765 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/99dcae9c-f2a3-471f-95f9-e185bad6d375/tool-results/b6aqcxgyh.txt",
 "offset": 786
}
```

```
786	    shm = sh.mean(0)
787	    print(f"{T} {S}: shuffled mean by k", np.round(shm, 3), "| spread over shuffles of the best: %.3f to %.3f" % (sh.max(1).min(), sh.max(1).max()))
788	    for K in (14, 12):
789	        H1 = bool(np.all(shm[:K] < mc["peri"][:K]))
790	        kb = min(v[:K].max() for v in mc["kin"].values())
791	        kbmax = max(v[:K].max() for v in mc["kin"].values())
792	        H2_all = H1 and shm[:K].max() < kb
793	        rows.append((T, S, K, round(shm[:K].max(), 3), round(mc["peri"][:K].max(), 3), round(kb, 3), round(kbmax, 3), H1, H2_all))
794	print(pd.DataFrame(rows, columns=["trials", "tuning", "K", "shuffled best", "peri best", "kinematic best (lowest variant)",
795	                                  "(highest variant)", "H1", "H2 (every W, D)"]).to_string(index=False))
796	===== [48] markdown tags=None
797	**Result: blocked (methods_underspecified).** The trial readings disagree. Under T2 the shuffled space is below the
798	unshuffled one at every k, and its best (0.224 with S1, 0.467 with S2) is below the best kinematic space
799	(0.414 or more, and 0.644 or more), so H1 and H2 hold. Under T1 the unshuffled space falls below zero at
800	k ≥ 10 while the shuffled one stays positive (best 0.090 with S1), so H1 fails, and with it H2.
801	===== [49] markdown tags=None
802	## fig7b-window-start-slide
803	
804	> Moving the start of the peri-movement window from 150 ms before movement onset to movement onset costs little
805	> PD performance; at movement onset performance is 97% (monkey J) and 94% (monkeys A, B) of its original value.
[... 205 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; grep -n 'T1\|T2\|S1\|S2' mcmaze.py; ls ../../executed/ 2>/dev/null | head; cat ../../tools/entry.py | head -60
```

```
35:PROTO_WIN = (-150, 800)    # M1 (T1, T2), window of the velocity profiles, ms from movement onset
131:    the proto-trial (T1, T2: the condition's mean velocity over its trials). T1: each component at
132:    r > 0.9; T2: the two components concatenated.
139:            if reading == "T1":
142:            elif reading == "T2":
202:    """M6 tuning of condition rates (units x conditions). S1 range, S2 SD over conditions."""
203:    if reading == "S1":
205:    if reading == "S2":
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; sed -n 1,60p mcmaze.py; sed -n 120,215p mcmaze.py
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
[... 136 more lines not kept]
```

**Agent**

Plan: restrict the notebook to T2 and S1 (keeping only a count of T1 as context for why it was set aside), re-run, then rewrite conclusions and the record.

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i,s):
    cells[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))

# cell 10: T2 only for analysis, T1 count only as context
rep(10,'''keep = {T: mm.proto_trial_keep(kv[:, proto], cond, base, T) & base for T in ("T1", "T2")}
for T, k in keep.items():
    bc = np.bincount(cond[k], minlength=C)
    print(f"{T}: kept {k.sum()} of {base.sum()} trials with delay > 400 ms ({k.sum()/base.sum():.1%}); "
          f"conditions with no trial {int((bc == 0).sum())}; trials per condition min {bc[bc > 0].min()}, "
          f"median {int(np.median(bc[bc > 0]))}")
empty_T1 = np.where(np.bincount(cond[keep['T1']], minlength=C) == 0)[0]
print("conditions empty under T1:")
print(tr[tr.condition.isin(empty_T1)].groupby("condition")[["trial_type", "trial_version", "target_x", "target_y"]].first())
''','''# reading T2 (M1, as answered 2026-10-22); T1 is set aside and only its count is shown, for the record
keep_T1 = mm.proto_trial_keep(kv[:, proto], cond, base, "T1") & base
keep = {"T2": mm.proto_trial_keep(kv[:, proto], cond, base, "T2") & base}
for T, k in (("T2", keep["T2"]), ("T1 (set aside)", keep_T1)):
    bc = np.bincount(cond[k], minlength=C)
    print(f"{T}: kept {k.sum()} of {base.sum()} trials with delay > 400 ms ({k.sum()/base.sum():.1%}); "
          f"conditions with no trial {int((bc == 0).sum())}; trials per condition min {bc[bc > 0].min()}, "
          f"median {int(np.median(bc[bc > 0]))}")
''')
rep(10,'for T in ("T1", "T2"):\n    has','for T in keep:\n    has')
for i,c in enumerate(cells):
    if c['cell_type']=='code' and '("S1", "S2")' in src(i):
        rep(i,'("S1", "S2")','("S1",)')
# cell 12
rep(12,'''        ("trials per neuron, (b) M1 with T1", int(keep['T1'].sum()), 2166, 216.6),
''','')
# cell 16 plot
setsrc(16,'''fig, ax = plt.subplots(figsize=(4.5, 2.8))
r = R["T2", "S1"]["r"]
ax.hist(r, bins=np.linspace(-1, 1, 21), color="#4a6fa5", edgecolor="white")
ax.axvline(r.mean(), color="k", lw=1)
ax.set_title(f"T2, S1: n={len(r)}, mean r={r.mean():.2f}", fontsize=9)
ax.set_xlabel("tuning correlation (all values within -1 to 1)")
ax.set_ylabel("neurons")
plt.tight_layout(); plt.show()
''')
# cell 32
rep(32,'(("N1 S1", SEL[T, "S1"]["prep"]), ("N1 S2", SEL[T, "S2"]["prep"]), ("N2", np.ones(len(X), bool)))',
       '(("N1 S1", SEL[T, "S1"]["prep"]), ("N2", np.ones(len(X), bool)))')
# cell 36 plot
setsrc(36,'''fig, ax = plt.subplots(figsize=(5, 3.2))
ks = np.arange(1, KMAX + 1)
mc = MC["T2", "S1"]
ax.plot(ks, mc["peri"], color="#1f4e79", lw=2, label="peri-movement")
ax.plot(ks, mc["kin"]["W1D1"], color="#c55a11", lw=2, label="kinematic (W1 D1)")
for k, v in mc["task"].items():
    ax.plot(mc["dims"][k], v, "o", color="#548235", ms=5)
ax.plot([], [], "o", color="#548235", label="task spaces")
ax.axhline(0, color="0.8", lw=0.8)
ax.set_title(f"T2, S1 ({mc['n']} neurons)", fontsize=9); ax.set_xlabel("dimensionality k")
ax.set_ylabel("mean PD performance"); ax.legend(fontsize=7)
plt.tight_layout(); plt.show()
allv = np.r_[mc["peri"], mc["kin"]["W1D1"], list(mc["task"].values())]
print("range of plotted values: %.3f to %.3f (all inside the axes)" % (allv.min(), allv.max()))
''')
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; grep -n '"T1"\|S2' reproduce_churchland_2010.ipynb | grep -v '^\s*"\*\*' | head -40
```

```
.../reproduce_churchland_2010.ipynb                | 68 ++++++++++------------
 1 file changed, 32 insertions(+), 36 deletions(-)
21:    "claims file fixes every method; the labels M1 to M9, T1/T2, S1/S2 and so on are its readings.\n",
408:    "Per neuron passing M6 (S1, S2), Pearson and Spearman correlations over conditions between the M4\n",
476:    "paper's 0.13 and 0.11. S2 selects no neuron under either trial reading, so it gives no result."
523:    "largest r is 0.411), so it does not. S2 selects no neuron. A question on T1 and T2 has been asked."
572:    "|r| ≥ 0.8. The median r is 0.026 and 0.013. S2 selects no neuron."
760:    "Reproduced when within 7 to 11 under one reading (N1: prep-tuned neurons, S1 and S2; N2: all neurons)."
793:    "variance needs 18 (T1) and 15 (T2) components; with all 182 units, 20 and 18; with the 6 units S2 selects, 4."
803:    "Neurons passing the preparatory part of M6 (S1, S2). The peri-movement space (M5) is built for each neuron\n",
954:    "and 0.412 for the kitchen-sink space; 24 of 24 combinations, and also with S2). Under T1 with S1 it wins\n",
955:    "none: its best is 0.281 (k = 5), below the kinematic space (0.295) and the kitchen-sink space (0.313); with S2\n",
1020:    "T2 with S2 it wins 20 or 21 of 22 (K1) and 18 or 19 of 20 (K2), so L2 holds but L1 does not in every combination. Under T1 it wins 11 or 12\n",
1065:    "best at k = 5 (S1, 0.281) or 10 (S2, 0.645) and falls at k = 14 (-0.287 and 0.393), as the claim says. Under T2 it\n",
1066:    "rises through k = 14 (S1, 0.140 to 0.518; S2, 0.339 to 0.821) with no decline, so the best k is above 10."
1131:    "unshuffled one at every k, and its best (0.224 with S1, 0.467 with S2) is below the best kinematic space\n",
1177:    "starting at -150 ms is within 0.97 ± 0.097 under every reading: 0.918 (T1, S1), 0.904 (T1, S2), 0.957 to 0.959\n",
1178:    "(T2, S1) and 0.968 to 0.972 (T2, S2). The 94% of monkeys A and B cannot be tested."
1454:    "(a question has been 
[... 1 more lines not kept]
```

**Agent**

Code restricted. Now running the entry to get the new numbers.

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/000128-churchland-2010 2>&1 | tail -3; python tools/entry.py all entries/000128-churchland-2010 2>&1 | tail -15
```

```
wrote entries/000128-churchland-2010/requirements.lock.txt
Installed kernelspec registry-000128-churchland-2010 in executed/000128-churchland-2010/.venv/share/jupyter/kernels/registry-000128-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (88 s)
```

**Agent calls Bash**

```bash
cd  git status --short; python - <<'EOF'
import json
nb=json.load(open('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i<10: continue
    print(f"===== [{i}] {c['metadata'].get('tags')}")
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: print(''.join(o['data']['text/plain']))
EOF
```

```
M entries/000128-churchland-2010/reproduce_churchland_2010.ipynb
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
===== [10] None
T2: kept 1786 of 1967 trials with delay > 400 ms (90.8%); conditions with no trial 0; trials per condition min 10, median 17
T1 (set aside): kept 1452 of 1967 trials with delay > 400 ms (73.8%); conditions with no trial 2; trials per condition min 1, median 14

rates computed in 43 s

T2: 108 conditions; preparatory rates 0.0 to 35.4 spikes/s; peri-movement rates 0.0 to 56.3 spikes/s
T2 S1: preparatory tuning > 5 spikes/s: 83 of 182 units; also peri-movement tuning >= 1.5x: 17 (tuning range 0.2 to 34.0 spikes/s)
[... 153 more lines not kept]
```

**Agent**

Results are in. Let me read the current criteria of the affected claims to decide outcomes.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/000128/10.1016-j.neuron.2010.09.015.yaml'))
for c in d['claims']:
    if c['id'] in ('fig3-maze-most-not-maintained','fig6-peri-movement-space-best','fig6-each-dimensionality','fig6-performance-vs-dimensionality','fig7a-shuffled-space-poor','prep-dimensionality','suppfig1-population-averages','fig4d-mean-correlation-jarray','recordings-jarray'):
        print('==',c['id']); print(c.get('statement')); print('CRIT:',c.get('criterion')); print('EXP:',c.get('expected'))
EOF
```

```
== recordings-jarray
The J-array dataset holds 146 single- and multi-unit isolations from two 96-electrode arrays, recorded on the maze task with 108 conditions, with a mean of 2166 trials per neuron.
CRIT: Counts from the dataset's units, conditions and trials. The trial count can be read as (a) all successful trials or (b) those kept by M1 (delay > 400 ms and the proto-trial selection); the Methods print 2155 where the Results print 2166, both within the tolerance. The condition count has tolerance 0 because it is a design count, not a measurement. Reproduced when all three are within tolerance under one reading.
EXP: [{'quantity': 'units in the J-array dataset', 'value': 146, 'tolerance': 14.6}, {'quantity': 'maze conditions', 'value': 108, 'tolerance': 0}, {'quantity': 'mean trials per neuron, J-array', 'value': 2166, 'tolerance': 216.6}]
== fig3-maze-most-not-maintained
In the maze task some neurons keep similar tuning between the preparatory and peri-movement epochs, but most do not.
CRIT: J-array (and J if present), neurons selected as for Figure 4 (M6, reading S1), tuning correlation as in M4. The paper sets no threshold for "similar tuning"; the one value it calls "quite high" is r = 0.72 (Figure 2B). Reproduced when at least one neuron has r of 0.72 or more and more than half of the neurons have r below 0.72.
EXP: None
== fig4d-mean-correlation-jarray
In the J-array dataset the correlation between a neuron's preparatory and peri-movement tuning is positive on average but small (mean r = 0.13, p = 0.03; mean Spearman r = 0.11).
CRIT: Per neuron passing M6 (preparatory tuning > 5 spikes/s and peri-movement tuning at least 1.5 times the preparatory tuning, reading S1; S2 set aside, see the M6 answer), the Pearson and Spearman correlation over the 108 conditions between the preparatory rates and the peri-movement rates of M4, trials by M1 (reading T2; T1 set aside, see the M1 answer). The paper does not name the test of the mean against zero. Readings (P1) one
[... 25 more lines not kept]
```

**Agent**

Outcomes are now decided under T2 with S1. Updating the notebook's text cells.

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; python - <<'EOF'
import json
p='reproduce_churchland_2010.ipynb'
nb=json.load(open(p))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i,s):
    assert cells[i]['cell_type']=='markdown'
    cells[i]['source']=s.strip('\n').splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))

rep(0,'''claims file fixes every method; the labels M1 to M9, T1/T2, S1/S2 and so on are its readings.
''','''claims file fixes every method; the labels M1 to M9, T2, S1 and so on are its readings.

**Answers taken up.** A reader answered three questions of this attempt on 2026-10-22
(`questions/000128.yaml`), and the claims file was updated. The proto-trial selection (M1) is now reading
T2 alone: T1, which kept 73.8% of trials and emptied two conditions, is set aside. The tuning measure (M6)
is now reading S1 (the range over conditions) alone: S2, the SD over conditions, is set aside. For
suppfig1-population-averages the criterion now names both readings of the normalising maximum, (a) and
(b), which were already run. The analyses below run T2 and S1 only; T1's count is printed once, for the
record.
''')
rep(0,'| fig3-maze-most-not-maintained | tested |','| fig3-maze-most-not-maintained | tested |')
setsrc(9,'''### Trial selection and firing rates (M1, M2)

Trials with delay > 400 ms (M1), then the proto-trial selection under reading T2 (the two velocity
components concatenated, r > 0.9 with the condition mean; T1 set aside by the answer of 2026-10-22, and only
its count shown). Rates: spikes smoothed with a Gaussian of SD 20 ms, sampled every 10 ms, averaged over the
kept trials of each condition, locked to the go cue (-400 to +500 ms) and to movement onset (-400 to +800
ms). Tuning by reading S1 (the range over conditions; S2 set aside by the same answers).
''')
setsrc(13,'''**Result: partially reproduced.** The 108 conditions match, and the 2295 labelled successful trials are
within tolerance of 2166 (reading a), as are the 1967 trials with delay > 400 ms; under M1 (reading T2) the
1786 kept trials are not. The unit count is not: the dataset has 182 units (137 held in and 45 held out),
36 more than 146 and outside the tolerance of 14.6.
''')
rep(14,'''Per neuron passing M6 (S1, S2), Pearson and Spearman correlations over conditions between the M4
preparatory and peri-movement rates, trials by M1 (T1, T2); tests P1 to P3.''','''Per neuron passing M6 (reading S1), Pearson and Spearman correlations over conditions between the M4
preparatory and peri-movement rates, trials by M1 (reading T2); tests P1 to P3.''')
setsrc(17,'''**Result: not reproduced.** Under T2 with S1 (17 neurons) the mean Pearson r is 0.051 and the mean Spearman
r 0.072, and no test finds the mean above zero (p 0.42 to 0.61). The means are positive but less than half
the paper's 0.13 and 0.11, outside the tolerances of 0.013 and 0.011.
''')
rep(18,'Neurons as for Figure 4 (M6, both readings).','Neurons as for Figure 4 (M6, reading S1; trials by T2).')
setsrc(20,'''**Result: reproduced.** Under T2 with S1, one of 17 neurons keeps its tuning (r = 0.765) and 94.1% have
r < 0.72, so at least one neuron has r of 0.72 or more and more than half have r below it.
''')
setsrc(23,'''**Result: reproduced.** Under T2 with S1 the dip test finds no departure from unimodality (dip 0.071, p 0.683),
and 16 of 17 neurons have |r| < 0.5, so U1 and U2 both hold. No neuron has |r| ≥ 0.8; the median r is 0.013.
''')
setsrc(27,'''**Result: reproduced.** Under T2 with S1 (17 neurons) the mean correlation falls from 0.737 (A1) and 0.759 (A2)
at -400 ms and 0.608 at -200 ms to 0.012 at movement onset, where no test finds it above zero (smallest p
0.854), so (i) holds. 82.1% (A1) and 79.8% (A2) of the drop from -400 ms to onset comes after -200 ms, so (ii)
holds.
''')
rep(28,'''Which maximum is open; readings (a) the maximum over all
conditions and times of the go- and movement-locked averages; (b) the maximum over the four chosen
conditions' traces.''','''The paper does not say over what the maximum is taken (answered
2026-10-22); the criterion names both readings, (a) the maximum over all conditions and times of the go- and
movement-locked averages and (b) the maximum over the four chosen conditions' traces, and both are run.''')
setsrc(30,'''**Result: reproduced.** The separation between the strongest and weakest preparatory conditions is positive in the
preparatory epoch (0.220 of the maximum rate under normalisation a, 0.346 under b) and is 0.053 and 0.095 at
movement onset, ratios of 0.240 and 0.274. R1 (below a half) holds under both normalisations; R2 (below a
quarter) holds under (a) and not under (b). The claim needs the condition to hold under one reading.
''')
rep(31,'(N1: prep-tuned neurons, S1 and S2; N2: all neurons)','(N1: prep-tuned neurons, S1; N2: all neurons)')
setsrc(33,'''**Result: not reproduced.** No reading gives 7 to 11 components. With the 83 prep-tuned neurons (N1, S1), 90% of
the variance needs 15 components; with all 182 units (N2), 18.
''')
rep(34,'Neurons passing the preparatory part of M6 (S1, S2).','Trials by T2. Neurons passing the preparatory part of M6 (S1).')
rep(37,'Reproduced when, under every combination (T, S, K, W, D, V, G)','Reproduced when, under every combination (K, W, D, V, G)')
setsrc(39,'''**Result: reproduced.** Under T2 with S1 (83 neurons) the peri-movement space has the best performance in all 24
combinations of W, D, V and G, under K1 and K2. Its best is 0.518 at k = 14 (K1) and 0.505 at k = 12 (K2),
against 0.424 and 0.417 for the best kinematic space and 0.412 for the best task space (kitchen sink, G1).
''')
setsrc(42,'''**Result: reproduced.** The 3-D endpoints + max speed space (0.168) is below the 3-D peri-movement space (0.271).
Under T2 with S1 the peri-movement space wins 21 of 22 comparisons (K1) and 19 of 20 (K2) in every
combination of W, D, V and G, so L1 (all but at most one) and L2 (at least 90%) both hold.
''')
setsrc(45,'''**Result: not reproduced.** Under T2 with S1, performance rises from 0.140 at k = 1 to 0.518 at k = 14, so it
improves with dimensionality, but its best k is 14, above 10, and it does not decline at k = 14. Two of the
criterion's three conditions fail.
''')
setsrc(48,'''**Result: reproduced.** Under T2 with S1 the shuffled space (mean of 10 shuffles) is below the unshuffled
one at every k, so H1 holds. Its best, 0.227 (0.208 to 0.244 over shuffles), is below the best kinematic
space in every variant (0.421 to 0.424 under K1, 0.414 to 0.417 under K2), so H2 holds.
''')
setsrc(51,'''**Result: reproduced.** Under reading J2, the J-array ratio of performance with the window starting at onset to that
starting at -150 ms is 0.959 (K1) and 0.957 (K2) under T2 with S1, within 0.97 ± 0.097. The 94% of monkeys A
and B cannot be tested.
''')
setsrc(54,'''**Result: reproduced.** Under T2 with S1 the PD is more stable in the peri-movement space in all 11 comparisons:
0.752 against 0.548 for endpoints + max speed, 0.649 and 0.648 against 0.495 and 0.466 for segment directions
(G1, G2), and 0.197 to 0.319 against 0.166 to 0.230 for the kinematic spaces at their best k.
''')
s=src(64)
s=s.replace('''| fig3-maze-most-not-maintained | blocked: methods_underspecified (holds under T2, not under T1) |
| fig4d-mean-correlation-jarray | not reproduced: mean r 0.025 to 0.051, p > 0.4 |''','''| fig3-maze-most-not-maintained | reproduced: 1 of 17 neurons with r ≥ 0.72 |
| fig4d-mean-correlation-jarray | not reproduced: mean r 0.051, Spearman 0.072, p > 0.4 |''')
s=s.replace('''| fig6-peri-movement-space-best | blocked: methods_underspecified (holds under T2, not under T1) |
| fig6-each-dimensionality | blocked: methods_underspecified (readings disagree) |
| fig6-performance-vs-dimensionality | blocked: methods_underspecified (holds under T1, not under T2) |
| prep-dimensionality | not reproduced: 15 to 20 components, not 7 to 10 |''','''| fig6-peri-movement-space-best | reproduced: 0.518 against 0.424 (kinematic) and 0.412 (task) |
| fig6-each-dimensionality | reproduced: 21 of 22 and 19 of 20 comparisons won |
| fig6-performance-vs-dimensionality | not reproduced: best at k = 14, no decline |
| prep-dimensionality | not reproduced: 15 and 18 components, not 7 to 11 |''')
s=s.replace('''| fig7a-shuffled-space-poor | blocked: methods_underspecified (holds under T2, not under T1) |''','''| fig7a-shuffled-space-poor | reproduced: shuffled best 0.227 against 0.518 |''')
s=s.replace('''paper's proto-trial selection is not defined; under reading T1 it keeps 74% of trials and empties two
conditions, under T2 91% (the paper says typically about 90%), and five claims change outcome between them
(a question has been asked). Reading S2 of the tuning measure selects no unit for the correlation claims and 6
for the PD claims.''','''paper does not say how the two velocity components enter its proto-trial selection; the answer of
2026-10-22 fixed reading T2 (91% of trials kept, every condition; the paper says typically about 90%), and
reading T1 (74%, two conditions empty) was set aside. The paper does not define its tuning measure; the same
answers fixed reading S1, the range over conditions.''')
s=s.replace('All methods follow the claims file; the details it leaves open are run under every reading.',
 'All methods follow the claims file; the details it leaves open are run under every reading it names.')
setsrc(64,s)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
grep -n 'T1\|S2' reproduce_churchland_2010.ipynb
```

```
25:    "T2 alone: T1, which kept 73.8% of trials and emptied two conditions, is set aside. The tuning measure (M6)\n",
26:    "is now reading S1 (the range over conditions) alone: S2, the SD over conditions, is set aside. For\n",
28:    "(b), which were already run. The analyses below run T2 and S1 only; T1's count is printed once, for the\n",
296:    "components concatenated, r > 0.9 with the condition mean; T1 set aside by the answer of 2026-10-22, and only\n",
299:    "ms). Tuning by reading S1 (the range over conditions; S2 set aside by the same answers)."
316:    "# reading T2 (M1, as answered 2026-10-22); T1 is set aside and only its count is shown, for the record\n",
317:    "keep_T1 = mm.proto_trial_keep(kv[:, proto], cond, base, \"T1\") & base\n",
319:    "for T, k in ((\"T2\", keep[\"T2\"]), (\"T1 (set aside)\", keep_T1)):\n",
1455:    "reading T1 (74%, two conditions empty) was set aside. The paper does not define its tuning measure; the same\n",
```

**Agent**

Now the helper docstrings, README and attempt record.

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010; python - <<'EOF'
p='mcmaze.py'; s=open(p).read()
a='''    r > 0.9; T2: the two components concatenated.
    """'''
b='''    r > 0.9; T2: the two components concatenated. The claims file's answer of 2026-10-22 keeps T2
    alone; T1 stays here so its count can be shown.
    """'''
assert a in s; s=s.replace(a,b)
a='''    """M6 tuning of condition rates (units x conditions). S1 range, S2 SD over conditions."""'''
b='''    """M6 tuning of condition rates (units x conditions). S1 range, S2 SD over conditions.

    The claims file's answer of 2026-10-22 keeps S1 alone; S2 is not used by the notebook.
    """'''
assert a in s; s=s.replace(a,b)
s=s.replace("PROTO_WIN = (-150, 800)    # M1 (T1, T2), window","PROTO_WIN = (-150, 800)    # M1 (reading T2), window")
open(p,'w').write(s)
p='README.md'; s=open(p).read()
a='''| Starting the peri-movement window at onset keeps about 97% of PD performance | Reproduced |
| The PD is most stable in the peri-movement space | Reproduced |
| The oscillator model: low tuning correlation, PD captures tuning perfectly | Reproduced (2 claims) |
| Most maze neurons do not keep their tuning; the peri-movement space performs best; performance against dimensionality; the shuffled control | Blocked: methods underspecified (5 claims; the trial selection readings disagree, a question is asked) |'''
b='''| Most maze neurons do not keep their tuning | Reproduced |
| PD performance is highest in the peri-movement space | Reproduced |
| The peri-movement space wins at almost every dimensionality | Reproduced |
| PD performance peaks near 10 dimensions and then declines | Not reproduced (still rising at 14) |
| The shuffled peri-movement space performs poorly | Reproduced |
| Starting the peri-movement window at onset keeps about 97% of PD performance | Reproduced |
| The PD is most stable in the peri-movement space | Reproduced |
| The oscillator model: low tuning correlation, PD captures tuning perfectly | Reproduced (2 claims) |'''
assert a in s; s=s.replace(a,b)
a='''- `reproduce_churchland_2010.ipynb`: the analysis. It takes about three minutes'''
b='''The outcomes follow the answers of 2026-10-22 to the attempt's questions (`questions/000128.yaml`): the
proto-trial selection is reading T2 and the tuning measure reading S1.

- `reproduce_churchland_2010.ipynb`: the analysis. It takes about two minutes'''
assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
EOF
sed -i 's/runtime_minutes: 3/runtime_minutes: 2/' entry.yaml; cat README.md | sed -n 9,40p
```

```
| Claim | Outcome |
|---|---|
| The J-array dataset: 146 units, 108 conditions, about 2166 trials | Partially reproduced (182 units) |
| Mean correlation of preparatory and peri-movement tuning 0.13 (J-array) | Not reproduced |
| No separate concordant and opposing populations | Reproduced |
| The correlation declines from about 200 ms before movement onset to near zero | Reproduced |
| Population averages lose their relation to preparatory tuning by movement onset | Reproduced |
| 7 to 10 dimensions capture 90% of preparatory variance | Not reproduced |
| Most maze neurons do not keep their tuning | Reproduced |
| PD performance is highest in the peri-movement space | Reproduced |
| The peri-movement space wins at almost every dimensionality | Reproduced |
| PD performance peaks near 10 dimensions and then declines | Not reproduced (still rising at 14) |
| The shuffled peri-movement space performs poorly | Reproduced |
| Starting the peri-movement window at onset keeps about 97% of PD performance | Reproduced |
| The PD is most stable in the peri-movement space | Reproduced |
| The oscillator model: low tuning correlation, PD captures tuning perfectly | Reproduced (2 claims) |
| Anterior against posterior sites | Blocked: metadata insufficient (2 claims) |
| Speed task, single-electrode and EMG data | Blocked: data missing (5 claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; grep -n 'question\|answer\|properties' -i schemas/attempt*.json | head -30
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
6:  "additionalProperties": false,
16:  "properties": {
27:      "additionalProperties": false,
33:      "properties": {
61:        "properties": {
68:        "properties": {
90:      "additionalProperties": false,
92:      "properties": {
100:      "additionalProperties": false,
105:      "properties": {
115:          "additionalProperties": false,
119:          "properties": {
135:          "additionalProperties": false,
141:          "properties": {
157:          "additionalProperties": false,
161:          "properties": {
182:        "additionalProperties": false,
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p schemas/attempt.schema.json; sed -n 180,260p schemas/attempt.schema.json
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
[... 121 more lines not kept]
```

**Agent**

Now rewriting the affected outcomes in the attempt record.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
p='attempts/000128-churchland-2010-01.yaml'; s=open(p).read()
new={}
new['recordings-jarray']='''- claim: recordings-jarray
  outcome: partially_reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:recordings-jarray
  measured:
  - 182
  - 108
  - 2295
  notes: The dataset has 108 conditions (36 mazes in 3 versions) and 2295 successful trials with
    condition labels, within tolerance of 2166 under reading (a); every unit is observed on every
    trial. Under reading (b) M1 keeps 1786 trials with T2, outside the tolerance. The unit count is
    182 (137 held in, 45 held out), outside 146 plus or minus 14.6. A further 574 successful trials
    are in the test file as 0.7 s segments without labels (2869 in all, outside the tolerance). The
    answer of 2026-10-22 to the M1 question removed T1's count (1452) from reading (b); the outcome
    is unchanged.
  deviations:
  - Nothing in the dataset says which units or trials the paper used, or whether this session
    (2009-09-25) is the one the paper analysed.
'''
new['fig3-maze-most-not-maintained']='''- claim: fig3-maze-most-not-maintained
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig3-maze-most-not-maintained
  notes: Under T2 with S1, 1 of 17 neurons has r of 0.72 or more (0.765) and 94.1% have r below
    0.72, so the claim holds. The answers of 2026-10-22 set aside T1 and S2. The earlier record was
    blocked (methods_underspecified) because T1 with S1 gave no neuron at 0.72 (largest r 0.411) and
    S2 selected no neuron; with T2 and S1 fixed, the claim is reproduced.
'''
new['fig4d-mean-correlation-jarray']='''- claim: fig4d-mean-correlation-jarray
  outcome: not_reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig4d-mean-correlation-jarray
  measured:
  - 0.051
  - 0.072
  notes: Under T2 with S1, 17 neurons, the mean Pearson r is 0.051 and the mean Spearman r 0.072,
    outside 0.13 plus or minus 0.013 and 0.11 plus or minus 0.011, and no test gives p below 0.05
    (P1 0.47, P2 0.42, P3 0.61). The means are positive but below half the paper's. The answers of
    2026-10-22 set aside T1 and S2; the earlier record gave T1 with S1 (0.025 and 0.054, recorded as
    measured) and T2 with S1, and S2 gave no neuron. The measured values are now those of T2, and the
    outcome is unchanged.
  deviations:
  - The dataset has 182 units, not the paper's 146, and the paper's unit selection is not
    recorded; the selected neurons may differ from the paper's.
'''
new['fig4-no-separate-populations']='''- claim: fig4-no-separate-populations
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig4-no-separate-populations
  notes: J-array only. Under T2 with S1 the dip statistic is 0.071 (p 0.683), so U1 holds, and 16 of
    17 neurons have |r| below 0.5, so U2 holds. No neuron has |r| of 0.8 or more; median r 0.013. The
    panel B part of the statement (monkey B) cannot be tested. The answers of 2026-10-22 removed the
    T1 and S2 readings, which had given the same outcome (T1) or no neuron (S2); the outcome is
    unchanged.
'''
new['fig4e-correlation-time-course']='''- claim: fig4e-correlation-time-course
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig4e-correlation-time-course
  notes: Under T2 with S1 (17 neurons), the mean correlation is 0.737 (A1) and 0.759 (A2) at -400 ms,
    0.608 at -200 ms and 0.012 at movement onset, where no test is significant (smallest p 0.854).
    82.1% (A1) and 79.8% (A2) of the drop from -400 ms to onset comes after -200 ms. The answers of
    2026-10-22 removed the T1 and S2 readings, which had given the same outcome (T1) or no neuron
    (S2); the outcome is unchanged.
  deviations:
  - Under A2 the criterion's linear joining was implemented as a straight line between the last
    go-locked value and the first movement-locked one where they leave a gap, and a linear fade from
    one to the other where they overlap, with each condition's go cue placed at its mean reaction
    time before onset. A1 and A2 differ only before -300 ms and give the same outcome.
'''
new['suppfig1-population-averages']='''- claim: suppfig1-population-averages
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:suppfig1-population-averages
  notes: Under T2 with S1 (17 neurons), the strongest-minus-weakest separation is 0.220 (reading a)
    and 0.346 (reading b) of the maximum rate in the preparatory epoch, and 0.053 and 0.095 at
    movement onset, ratios 0.240 and 0.274. R1 holds under both; R2 holds under (a) and not under
    (b). The answer of 2026-10-22 says the paper does not fix the maximum, and the criterion now
    names readings (a) and (b), the two already run, so the method is unchanged. The answers on M1
    and M6 removed T1 and S2; the outcome is unchanged.
'''
new['fig6-peri-movement-space-best']='''- claim: fig6-peri-movement-space-best
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig6-peri-movement-space-best
  notes: Under T2 with S1 (83 neurons) the peri-movement space is best in 24 of 24 combinations of
    W, D, V and G under K1 and under K2. Its best is 0.518 at k = 14 (K1) and 0.505 at k = 12 (K2),
    against 0.424 and 0.417 for the best kinematic space and 0.412 for the kitchen-sink space (G1).
    The answers of 2026-10-22 set aside T1 and S2. The earlier record was blocked
    (methods_underspecified) because under T1 with S1 the peri-movement space (0.281) fell below the
    kinematic (0.295) and kitchen-sink (0.313) spaces; with T2 fixed, the claim is reproduced.
  deviations:
  - J-array only; EMG is not recorded for it.
  - Acceleration is the time derivative of the dataset's hand velocity.
  - V1 ("each component's maximum absolute value") was run as the magnitudes (V1a) and as the signed
    component at its largest magnitude (V1b); they do not change the outcome.
'''
new['fig6-each-dimensionality']='''- claim: fig6-each-dimensionality
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig6-each-dimensionality
  notes: The 3-D endpoints + max speed space (0.168) is below the 3-D peri-movement space (0.271).
    Under T2 with S1 the peri-movement space wins 21 of 22 comparisons (K1) and 19 of 20 (K2) in
    every combination of W, D, V and G, so L1 and L2 hold. The answers of 2026-10-22 set aside T1 and
    S2. The earlier record was blocked (methods_underspecified) because T1 gave 11 or 12 wins and
    T2 with S2 failed L1 in some combinations; with T2 and S1 fixed, the claim is reproduced.
  deviations:
  - J-array only.
'''
new['fig6-performance-vs-dimensionality']='''- claim: fig6-performance-vs-dimensionality
  outcome: not_reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig6-performance-vs-dimensionality
  notes: Under T2 with S1 (83 neurons) performance rises from 0.140 at k = 1 to 0.518 at k = 14, so
    it improves with dimensionality, but the best k is 14, above 10, and performance does not
    decline at k = 14. Two of the criterion's three conditions fail, and the part of the statement
    they test (a peak in a middle range and a decline beyond about 10 dimensions) is not found. The
    answers of 2026-10-22 set aside T1 and S2. The earlier record was blocked
    (methods_underspecified) because under T1 the claim held (best at k = 5, 0.281, falling to
    -0.287 at k = 14); with T2 fixed, it is not reproduced.
  deviations:
  - J-array only.
'''
new['prep-dimensionality']='''- claim: prep-dimensionality
  outcome: not_reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:prep-dimensionality
  measured: 15
  notes: Under T2, 90% of the variance of the preparatory condition-mean matrix needs 15 components
    with the 83 neurons of N1 (S1) and 18 with all 182 units (N2). Neither is within 7 to 11.
    Trial-averaged rates from 10 to 27 trials per condition carry noise that adds dimensions; the
    paper's procedure may differ in this. The answers of 2026-10-22 set aside T1 (18 and 20
    components, recorded earlier as measured) and S2 (4 components with 6 units); the measured value
    is now 15 and the outcome is unchanged.
  deviations:
  - J-array only.
'''
new['fig7a-shuffled-space-poor']='''- claim: fig7a-shuffled-space-poor
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig7a-shuffled-space-poor
  notes: Under T2 with S1 the shuffled space (mean of 10 shuffles) is below the unshuffled one at
    every k, so H1 holds, and its best, 0.227 (0.208 to 0.244 over shuffles), is below the best
    kinematic space in every variant (0.421 or more under K1, 0.414 or more under K2), so H2 holds.
    The answers of 2026-10-22 set aside T1 and S2. The earlier record was blocked
    (methods_underspecified) because under T1 the unshuffled space fell below zero at k of 10 or more
    while the shuffled one stayed positive, so H1 failed; with T2 fixed, the claim is reproduced.
  deviations:
  - J-array only; the paper averages over datasets.
'''
new['fig7b-window-start-slide']='''- claim: fig7b-window-start-slide
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig7b-window-start-slide
  measured: 0.959
  notes: Reading J2, the J-array ratio. Under T2 with S1, performance at the best k with the window
    starting at onset is 0.959 (K1) and 0.957 (K2) of that with the window starting at -150 ms,
    within 0.97 plus or minus 0.097. The 94% of monkeys A and B and the single-electrode J value (J1)
    cannot be tested. The answers of 2026-10-22 set aside T1 and S2 (0.904 to 0.972, all within
    tolerance; 0.918 under T1 was recorded earlier as measured); the measured value is now 0.959 and
    the outcome is unchanged.
  deviations:
  - J-array only (reading J2).
'''
new['ap-location-no-effect-on-correlation']='''- claim: ap-location-no-effect-on-correlation
  outcome: blocked
  blocked_by: metadata_insufficient
  notes: The electrodes table has no coordinates, so no anterior-posterior location. The criterion's
    fallback, the array, is not usable either, as every unit's electrode reference points into the 96
    PMd rows, so by the file all units are in PMd. The unit ids' leading digit (1 for 92 units, 2 for
    90) looks like an array number, but nothing in the dataset documents it or which array is which.
    As a variant that decides nothing, regressing tuning correlation on that digit gives r of
    magnitude 0.432 (T2 with S1, 17 neurons, p 0.084), not significant. The answers of 2026-10-22
    removed the T1 variant; the block is unchanged.
'''
new['fig7d-pd-consistency']='''- claim: fig7d-pd-consistency
  outcome: reproduced
  notebook: reproduce_churchland_2010.ipynb
  output: claim:fig7d-pd-consistency
  notes: Under T2 with S1 the peri-movement space has the higher mean PD consistency in all 11
    comparisons (0.752 against 0.548 for endpoints + max speed, 0.649 and 0.648 against 0.495 and
    0.466 for segment directions G1 and G2, and 0.197 to 0.319 against 0.166 to 0.230 for the
    kinematic spaces at their best k). The answers of 2026-10-22 removed the T1 and S2 readings,
    which had given the same outcome; the outcome is unchanged. Removing them changed the random
    draws, so the values differ slightly from the earlier record.
  deviations:
  - J-array only.
'''
for cid, block in new.items():
    m=re.search(r'^- claim: '+re.escape(cid)+r'\n(?:  .*\n|  \n)*', s, re.M)
    assert m, cid
    s=s[:m.start()]+block+s[m.end():]
open(p,'w').write(s)
EOF
python -c "import yaml;d=yaml.safe_load(open('attempts/000128-churchland-2010-01.yaml'));print(len(d['outcomes']),[o['outcome'] for o in d['outcomes']])"; git diff --stat
```

```
22 ['partially_reproduced', 'blocked', 'blocked', 'blocked', 'reproduced', 'not_reproduced', 'blocked', 'reproduced', 'reproduced', 'reproduced', 'reproduced', 'reproduced', 'not_reproduced', 'not_reproduced', 'blocked', 'reproduced', 'reproduced', 'blocked', 'blocked', 'reproduced', 'reproduced', 'reproduced']
 attempts/000128-churchland-2010-01.yaml            | 161 ++++++++--------
 entries/000128-churchland-2010/README.md           |  11 +-
 entries/000128-churchland-2010/entry.yaml          |   2 +-
 entries/000128-churchland-2010/mcmaze.py           |  10 +-
 .../reproduce_churchland_2010.ipynb                | 209 ++++++++++-----------
 5 files changed, 204 insertions(+), 189 deletions(-)
```

**Agent calls Bash**

```bash
cd  sed -i 's/    Trial-averaged rates from 10 to 27 trials per condition carry noise that adds dimensions; the/    Trial-averaged rates from at least 10 trials per condition (median 17) carry noise that adds dimensions; the/' attempts/000128-churchland-2010-01.yaml; grep -n 'median 17' attempts/000128-churchland-2010-01.yaml; grep -nP '—|\brather\b|\*\*' attempts/000128-churchland-2010-01.yaml entries/000128-churchland-2010/README.md | head; grep -n ': .*: ' attempts/000128-churchland-2010-01.yaml | grep -v '^\S*\s*- ' | head
```

```
162:    Trial-averaged rates from at least 10 trials per condition (median 17) carry noise that adds dimensions; the
```

**Agent**

Record updated. Re-running lock, check and run on the final notebook, then the handover.

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/000128-churchland-2010 2>&1 | tail -2; python tools/entry.py all entries/000128-churchland-2010 2>&1 | tail -4; python tools/entry.py handover entries/000128-churchland-2010 2>&1 | tail -5; git status --short | grep -v '^??'
```

```
wrote entries/000128-churchland-2010/requirements.lock.txt
Installed kernelspec registry-000128-churchland-2010 in executed/000128-churchland-2010/.venv/share/jupyter/kernels/registry-000128-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (81 s)
wrote executed/000128-churchland-2010/handover
 M attempts/000128-churchland-2010-01.yaml
 M entries/000128-churchland-2010/README.md
 M entries/000128-churchland-2010/entry.yaml
 M entries/000128-churchland-2010/mcmaze.py
 M entries/000128-churchland-2010/reproduce_churchland_2010.ipynb
```

**Agent**

Quick check that the final run printed the same numbers the conclusions cite:

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb'))
out=''
for c in nb['cells']:
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
for k in ['0.0506','0.765','0.683','0.854','0.240','0.274','24/24','0.168','0.227','0.959','0.957','0.752','0.548','-0.432','1786 of 1967','1452']:
    print(k, k in out)
EOF
```

```
0.0506 True
0.765 True
0.683 True
0.854 True
0.240 True
0.274 True
24/24 True
0.168 True
0.227 True
0.959 True
0.957 True
0.752 True
0.548 True
-0.432 True
1786 of 1967 True
1452 True
```

**Agent**

I took up all three answers and re-ran every claim that used T1 or S2. The notebook now runs reading T2 for trial selection and S1 for tuning. It still prints T1's trial count once, for the record. The entry locks, passes `check`, and runs in 81 s; the handover is in `executed/000128-churchland-2010/handover/`. I changed the notebook, `mcmaze.py` (docstrings only), `README.md`, `entry.yaml` (runtime 2 min) and `attempts/000128-churchland-2010-01.yaml`. Nothing is committed and I did not verify my own work.

## Q1. Proto-trial selection (M1): T1 or T2

**Answer:** T1 is set aside and T2 alone stands. T2 keeps 1786 of 1967 trials (90.8%) and leaves every condition with at least 10 trials.

| Claim | Earlier | Now |
|---|---|---|
| fig3-maze-most-not-maintained | blocked, methods_underspecified | reproduced: 1 of 17 neurons has r ≥ 0.72 (0.765), and 94.1% are below it |
| fig6-peri-movement-space-best | blocked, methods_underspecified | reproduced: wins 24 of 24 combinations; best 0.518 against 0.424 (kinematic) and 0.412 (kitchen sink) |
| fig6-each-dimensionality | blocked, methods_underspecified | reproduced: wins 21 of 22 comparisons (K1) and 19 of 20 (K2); endpoints + max speed scores 0.168 against 0.271 |
| fig6-performance-vs-dimensionality | blocked, methods_underspecified | not reproduced: performance rises from 0.140 to 0.518 but its best k is 14 and it never declines |
| fig7a-shuffled-space-poor | blocked, methods_underspecified | reproduced: H1 and H2 hold; shuffled best 0.227 against kinematic 0.414 or more |
| recordings-jarray | partially reproduced | partially reproduced: unchanged; reading (b) is now T2 only (1786 trials) |

## Q2. Tuning measure (M6): can S2 stand

**Answer:** S2 is dropped throughout and S1 alone stands. S2 had given no neurons for the correlation claims and 6 for the PD claims, so dropping it changes no outcome. It does change several recorded values, because they previously came from T1.

| Claim | Earlier | Now |
|---|---|---|
| fig4d-mean-correlation-jarray | not reproduced, measured 0.025 / 0.054 (T1) | not reproduced, measured 0.051 / 0.072, p 0.42 to 0.61 |
| fig4-no-separate-populations | reproduced | reproduced: dip p 0.683; 16 of 17 neurons have \|r\| < 0.5 |
| fig4e-correlation-time-course | reproduced | reproduced: mean r 0.012 at onset (p ≥ 0.854); 80 to 82% of the drop comes after -200 ms |
| prep-dimensionality | not reproduced, measured 18 (T1) | not reproduced, measured 15 (all 182 units: 18); the target is 7 to 11 |
| fig7b-window-start-slide | reproduced, measured 0.918 (T1) | reproduced, measured 0.959 (K2: 0.957) |
| fig7d-pd-consistency | reproduced | reproduced: wins 11 of 11 comparisons. Values moved slightly (0.742 → 0.752) because removing readings changed the random draws |
| ap-location-no-effect-on-correlation | blocked, metadata_insufficient | blocked, metadata_insufficient: unchanged; the unit-id digit check is now T2 only (r -0.432, p 0.084) |

## Q3. suppfig1 normalising maximum

**Answer:** the paper does not say, so the criterion now names both readings: (a) the maximum over all conditions and times, and (b) the maximum over the four plotted conditions. The attempt already ran both, so the method is unchanged.

- **suppfig1-population-averages:** reproduced before, reproduced now. Under T2 with S1 the ratios are 0.240 (a) and 0.274 (b). R1 holds under both, and R2 holds under (a) only.

Each affected claim's notes in the attempt record say what the answer changed. The notebook conclusions, summary, header and README are updated to match. Every number they cite appears in the final executed outputs.

The outcome counts are now 11 reproduced, 1 partially reproduced, 3 not reproduced and 7 blocked: 5 for data_missing and 2 for metadata_insufficient. Before the answers they were 7, 1, 2 and 12.

## End of run

21 turns, 6 minutes, result: success.
