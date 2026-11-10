# burman-2023 · author-revise-2 · run 42803456145

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/burman-2023/verifier-2-report.md; ls entries/burman-2023 entries/burman-2023/*
```

```
Tue Nov 10 11:03:54 UTC 2026
**Verifier report, round 2: Burman et al. 2023 on DANDI:000458**

The claims file has 35 claims and the attempt record has 35 outcomes: 5 reproduced, 5 partially_reproduced and 25 blocked (24 data_missing, 1 methods_underspecified). Below, "main" means `reproduce_burman_2023.ipynb` and "model" means `network_model.ipynb`. Cell numbers are for the re-executed notebooks, so they differ from round 1.

### 1. Outcomes and assumptions

I agree with all 35 outcomes:
- **dataset-sessions-link:** reproduced.
- **fig4c-sample, fig4d-synchrony-lower-awake, fig4d-entropy-higher-awake:** partially_reproduced under A1F1, with the A1F2 exact match recorded as a deviation.
- **fig4-rate-higher-awake and figs6-rate-regressed:** reproduced.
- **fig4f-model-hyperpolarizing-less-activity:** reproduced.
- **fig4h-model-synchrony and fig4h-model-entropy:** partially_reproduced.
- **figs7-model-decoding:** reproduced. This holds even with the corrected statistic in §2a.
- **figs4-intrinsic-properties:** blocked, methods_underspecified.
- **The 24 patch-clamp claims:** blocked, data_missing.

No outcome sets `assumed: true`, so there is no assumption to assess.

One small gap in the claims file. For fig4c-sample, A1F1 keeps 721, which is inside 662 ± 66.2, and excludes 144, which is outside 203 ± 20.3 (main cell 19). The criterion's partial case, "only the total (865) is within 10%", does not literally cover this: the kept count is within tolerance too. Partial is still the sensible reading.
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls attempts/ 2>/dev/null | grep burman; ls questions | grep burman
```

```
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
634:### Round 2: with the author's conclusions
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,215p docs/protocol.md; sed -n 428,540p docs/protocol.md
```

````
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
### 4. Lock, check and run

```bash
[... 110 more lines not kept]
````

**Agent calls Bash**

```bash
grep -n "verifications" -A200 attempts/burman-2023-01.yaml | head -400
```

```
437:verifications:
438-- date: '2026-11-10'
439-  kind: agent
440-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)
441-  reviewed: The first executed notebooks (reproduce_burman_2023.ipynb and network_model.ipynb) with the
442-    conclusion cells and the summaries removed, the helper modules npx.py and network.py and the claims
443-    file, with the paper's full text (PMC11913778). The verifier queried the archive through the DANDI
444-    API and tested npx.measures, npx.histogram and read_session on a synthetic two-unit, three-trial
445-    session. It had no attempt record and could not see the two gists.
446-  results:
447-  - claim: dataset-sessions-link
448-    agrees: true
449-    outcome: reproduced
450-    reason: All 17 gist sessions are assets of 0.230317.0039, each has every units and trials field,
451-      and each has both epochs; 16 subjects. The clock check uses off-pulse windows on only 2 of 17
452-      files and relies on the evoked-count contrast for the other 15 (B5).
453-    response: The shifted-window check now runs on all 17 files (read_session counts the shifted windows
454-      as it streams the spike trains) with a Wilcoxon test per file and condition; 33 of 34 pairs pass
455-      at p below 0.001, and the one that does not (sub-569069 awake) is named in the notebook and the
456-      notes. Outcome unchanged.
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; sed -n 150,260p network.py; grep -n "seed\|random" network.py | head -40
```

```
dApre/dt  = -Apre  / tau_stdp : siemens (event-driven)
        dApost/dt = -Apost / tau_stdp : siemens (event-driven)
        ''',
        on_pre='''
        Apre += 1.*nsiemens
        w = clip(w + (Apost - beta * nsiemens) * eta, 0 * nsiemens, gmax)
        g_GABA_post += w''',
        on_post='''
        Apost += 1. * nsiemens
        w = clip(w + Apre * eta, 0 * nsiemens, gmax)
        ''')
    pop = {"exc": exc, "inh": inh}
    conns = {("exc", "exc"): (static_ex, 0.1, 0.1), ("exc", "inh"): (static_ex, 0.1, 0.1),
             ("inh", "inh"): (static_in, 0.1, 1.), ("inh", "exc"): (vogels, 0.1, 1.)}
    synapses = []
    for (a, b_), (model, p, w) in conns.items():
        s = b2.Synapses(pop[a], pop[b_], **model, namespace=syn_ns)
        s.connect(p=p)
        s.w = w * b2.nsiemens
        synapses.append(s)
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/burman-2023/ 2>&1; git log --oneline -8 -- executed/burman-2023 | cat; ls transcripts/burman-2023/
```

```
ls: cannot access 'executed/burman-2023/': No such file or directory
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
```

**Agent calls Bash**

```bash
cd  cat questions/burman-2023.yaml; cat transcripts/burman-2023/author-answers-report.md | head -50
```

```
# Questions from attempt burman-2023-01 (author revision after verifier round 1, 2026-11-10) about
# the claims file claims/burman-2023.yaml. Both were raised by the verifier as points about the
# claims file (verifier-1 report, B1 and B2). The attempt tests the claims as the file has them and
# shows the other reading as a variant; the outcomes stay as tested.
dandiset: "000458"
paper: doi:10.1016/j.neuron.2023.08.005
questions:
- claim: fig4c-sample
  also: [fig4d-synchrony-lower-awake, fig4d-entropy-higher-awake]
  asked: 2026-11-10
  question: >-
    The opening comment (N7) judges every Neuropixels claim under the Methods reading of the evoked
    rate (F1, a spike count over trials times 10 ms) and shows the gist's rate (F2, which sums the
    spikes' latencies in ms) as a variant. The paper's reported numbers are what F2 gives: the
    analysis gist, run unmodified on version 0.230317.0039, keeps 662 and excludes 203 units and
    gives synchrony 0.3253 and 0.3928 and entropy 1.3474 and 1.1106, the values of Figure 4C and
    4D; F1 gives 721 and 144, synchrony 0.3188 and 0.3862, entropy 1.3887 and 1.1502. Should the
    expected values of these claims be judged under F2, the reading the paper's numbers were
    computed with, keeping F1 as a variant, or does the Methods' wording take precedence as the
    file has it?
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
import json
nb=json.load(open('network_model.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=====',i,c['cell_type']); print(''.join(c['source'])[:3000])
E
```

```
===== 0 markdown
# Reproducing Burman et al. (2023): the network model (Figures 4E to 4H, S7)

**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)

**Data.** These claims are `data: elsewhere`: their data are generated by the paper's simulation
code, gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision
f6a05661c10051560aa381e334099efd8521617b, transcribed in `network.py` (its docstring lists the
differences, none of which changes the model). They use nothing from DANDI:000458 (version
0.230317.0039, read in `reproduce_burman_2023.ipynb`; the version constant is `npx.VERSION`).

**Text the claims were written from.** The version of record (PMC11913778) with STAR Methods; the
supplement (Figure S7) was not available.

| Claim | Here |
|---|---|
| fig4f-model-hyperpolarizing-less-activity | tested |
| fig4h-model-synchrony | tested |
[... 208 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "OMP\|THREADS\|venv\|env\[" tools/entry.py | head -30; ls ~/.cache 2>/dev/null; ls .venv* executed 2>/dev/null | head
```

```
466:    venv = (output_dir / ".venv").resolve()
467:    python = venv / "bin" / "python"
471:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
474:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
488:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
```

**Agent calls Bash**

```bash
cd entries/burman-2023; grep python entry.yaml; nproc; uv venv --quiet --python 3.13 $TMPDIR/v && uv pip install --quiet --python $TMPDIR/v/bin/python -r requirements.lock.txt 2>&1 | tail -3; $TMPDIR/v/bin/python -c "import sklearn,brian2;print(sklearn.__version__,brian2.__version__)"
```

```
python: "3.13"
4
1.9.1 2.11.0
```

**Agent calls Bash**

```bash
cd entries/burman-2023; cat > $TMPDIR/t1.py <<'E'
import os, sys, hashlib
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np, network
a = network.simulate(7, stimuli=10, repeats=5, spikes=True)
t,i = a["spikes"]
print(len(t), hashlib.md5(t.tobytes()+i.tobytes()).hexdigest(), a[-60]["accuracy"], a[-80]["accuracy"], np.nanmean(a[-80]["synchrony"]))
E
for k in 1 2; do $TMPDIR/v/bin/python $TMPDIR/t1.py 2>&1 | tail -1; done
```

```
ModuleNotFoundError: No module named 'network'
ModuleNotFoundError: No module named 'network'
```

**Agent calls Bash**

```bash
cd entries/burman-2023; for k in 1 2; do PYTHONPATH=. $TMPDIR/v/bin/python $TMPDIR/t1.py 2>&1 | tail -2; done
```

```
19093 9f0167fbbfcab054a2eeeff8d768a91d 0.96 1.0 0.8343783530405849
19093 9f0167fbbfcab054a2eeeff8d768a91d 0.96 1.0 0.8343783530405849
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; grep -n "16\.42\|16\.92\|1\.11e-12\|6\.52e-13\|0\.9848\|0\.9315\|0\.932\|0\.985" *.md | cut -c1-300
```

```
author-answers.md:194:network_model.ipynb **Result: reproduced.** Decoding accuracy is higher with shunting E_GABA, 0.9848 against 0.9315 on average (chance 0.01); D1 paired t = 16.92, p = 6.52e-13, and D2 holds, shunting higher in 20 of 20 runs. 
author-report.md:18:| figs7-model-decoding | reproduced: 0.985 against 0.932, shunting higher in 20 of 20 runs |
author-revise-1-report.md:13:- The decoding claim's notes said t = 16.92, p = 6.52e-13, which did not match the notebook's output. They now give the printed t = 16.42, p = 1.11e-12.
author-revise-1.md:1663:rep("D1 paired t = 16.92, p = 6.52e-13", "D1 paired t = 16.42, p = 1.11e-12")
author-revise-1.md:1872:197-  notes: Mean decoding accuracy 0.9848 shunting against 0.9315 hyperpolarizing (chance 0.01). D1, paired
author-revise-1.md:1873:198-    t test of the 20 per-run accuracies, t = 16.92, p = 6.52e-13; D2, shunting higher in 20 of 20 runs.
author-revise-1.md:1925:rep("t test of the 20 per-run accuracies, t = 16.92, p = 6.52e-13;", "t test of the 20 per-run accuracies, t = 16.42, p = 1.11e-12;")
author-revise-1.md:2102:    reason: Accuracy 0.985 shunting against 0.932 hyperpolarizing. D1 p = 1.1e-12; D2 higher in 20 of
author-revise-1.md:2105:    response: The notes gave t = 16.92 and p = 6.52e-13, which did not match the notebook; they now give
author-revise-1.md:2106:      the printed t = 16.42, p = 1.11e-12. Outcome unchanged.
author-revise-1.md:2206:network_ 19 D1 paired t = 16.42, p = 1.11e-12
author-revise-1.md:2260:- The decoding claim's notes said t = 16.92, p = 6.52e-13, which did not match the notebook's output. They now give the printed t = 16.42, p = 1.11e-12.
author.md:887:82.25458860397339 [16052.0, 23846.44295031674, 23846.44295031674] [(np.float64(0.974), np.float64(0.44), np.float64(0.788)), (np.float64(0.932), np.float64(0.182), np.float64(0.89))]
author.md:2443:3      2  hyperpolarizing     -80               927676                  800     8.7865        0.2042          0.8767    0.9328
autho
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; grep -n "hyperpolarizing   *-80" author-revise-1.md author.md author-answers.md | head -80 | cut -c1-200
```

```
author.md:2441:1      1  hyperpolarizing     -80               927971                  800     8.6719        0.1798          0.8909    0.9437
author.md:2443:3      2  hyperpolarizing     -80               927676                  800     8.7865        0.2042          0.8767    0.9328
author.md:2445:5      3  hyperpolarizing     -80               942619                  800     8.9146        0.1986          0.8813    0.9225
author.md:2447:7      4  hyperpolarizing     -80               913382                  800     8.6448        0.1955          0.8825    0.9527
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; sed -n 2180,2215p author-revise-1.md | cut -c1-250; grep -n "accuracy\|shunting  *hyperpolarizing" author-revise-1.md | head -40 | cut -c1-200
```

````
```

**Agent calls Bash**

```bash
cd executed/burman-2023 && python - <<'EOF'
import json, re
for nb in ('network_model.ipynb','reproduce_burman_2023.ipynb'):
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        if c['cell_type']!='code': continue
        out=''.join(''.join(o.get('text','')) for o in c['outputs'] if o.get('output_type')=='stream')
        for pat in ('D1 paired','run-to-run','eta in','identical spike','values differing','662 kept','conditions with evoked','A1F1 unrounded','units with a higher awake','Synchrony of the kept','Entropy \\[nats\\] of'):
            for line in out.splitlines():
                if re.search(pat, line): print(nb[:8], i, line[:200])
EOF
```

```
network_ 3 identical spike trains: True
[... 21 more lines not kept]
````

**Agent calls Bash**

```bash
cat /proc/cpuinfo | grep "model name" | head -1; cd transcripts/burman-2023; grep -n "model name\|EPYC\|Xeon" *.md | head
```

```
model name	: AMD EPYC 9V45 96-Core Processor
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t2.py <<'E'
import sys, numpy as np
from threadpoolctl import threadpool_limits
from scipy.sparse import csr_matrix
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
rng=np.random.default_rng(0)
y=np.repeat(np.arange(100),100)
proto=rng.poisson(1.0,(100,50))
X=csr_matrix(rng.poisson(proto[y]*0.8).astype(float))
for n in (1,2,4):
    with threadpool_limits(n):
        cv=StratifiedKFold(5,shuffle=True,random_state=3)
        print(n, np.mean(cross_val_score(KNeighborsClassifier(),X,y,cv=cv)))
E
$TMPDIR/v/bin/python $TMPDIR/t2.py; OMP_NUM_THREADS=1 $TMPDIR/v/bin/python $TMPDIR/t2.py
```

```
1 0.9616
2 0.9616
4 0.9616
1 0.9616
2 0.9616
4 0.9616
```

**Agent calls Bash**

```bash
cd  git diff 111844e5eb 822105a2df --stat | cat; git diff 111844e5eb 822105a2df -- entries/burman-2023/network.py | head -150
```

```
attempts/burman-2023-01.yaml                      |  348 +++-
 entries/burman-2023/README.md                     |    4 +-
 entries/burman-2023/entry.yaml                    |    2 +-
 entries/burman-2023/network.py                    |   49 +-
 entries/burman-2023/network_model.ipynb           |   80 +-
 entries/burman-2023/npx.py                        |   83 +-
 entries/burman-2023/reproduce_burman_2023.ipynb   |  166 +-
 questions/burman-2023.yaml                        |   51 +
 transcripts/burman-2023/author-revise-1-report.md |   21 +
 transcripts/burman-2023/author-revise-1.md        | 2272 +++++++++++++++++++++
 transcripts/burman-2023/verifier-1-report.md      |   39 +
 transcripts/burman-2023/verifier-1.md             |  473 +++++
 12 files changed, 3515 insertions(+), 73 deletions(-)
diff --git a/entries/burman-2023/network.py b/entries/burman-2023/network.py
index e9566c2b6d..266f757321 100644
--- a/entries/burman-2023/network.py
+++ b/entries/burman-2023/network.py
@@ -171,13 +171,17 @@ def simulate(seed, stimuli=100, repeats=100, verbose=False, periodic=True, spike
     net = b2.Network(exc, inh, *synapses, mon)
 
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; grep -n "entry.py\|OMP_NUM\|nbconvert\|papermill" author-revise-1.md | cut -c1-200 | head -30
```

```
623:cd  sed -n 1,60p tools/entry.py | head -80; ls -d .venv* $TMPDIR/* 2>/dev/null | head
629:    python tools/entry.py lock  entries/<name>   # pin the environment
630:    python tools/entry.py check entries/<name>   # validate metadata and conventions
631:    python tools/entry.py check entries/*/       # the same for every entry, in one process
632:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
633:    python tools/entry.py all   entries/<name>   # check, then run
634:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
1554:sed -i 's/| Multi-compartment model of Figure S4 | Blocked: other |/| Multi-compartment model of Figure S4 | Blocked: methods underspecified |/' README.md; grep -n "Figure S4" README.md; cd  && p
1578:cd ../.. && python tools/entry.py check entries/burman-2023 2>&1 | tail -2
1594:time python tools/entry.py all entries/burman-2023 2>&1 | grep -v MissingID | tail -15
2132:python tools/entry.py check entries/burman-2023 2>&1 | grep -v MissingID | tail -5
2170:cd  date -u; python tools/entry.py all entries/burman-2023 2>&1 | grep -v MissingID | tail -4; date -u
2219:cd entries/burman-2023 && sed -i 's/  runtime_minutes: 33/  runtime_minutes: 18/' entry.yaml && sed -i 's/on four processes, about 35 minutes./on four processes, about 20 minutes./' README.md && 
2248:No outcome changed. Every outcome the verifier gave is kept except one: figs4-intrinsic-properties stays blocked, but its reason changes from `other` to `methods_underspecified`, as the verifier
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; sed -n 1594,1625p author-revise-1.md | cut -c1-200; sed -n 2170,2180p author-revise-1.md | cut -c1-200; grep -n "D1 paired\|min (4 processes)" author.md author-revise-1.md author-answers.md | cut -c1-200
```

````
time python tools/entry.py all entries/burman-2023 2>&1 | grep -v MissingID | tail -15
```

```
Installed kernelspec registry-burman-2023 in executed/burman-2023/.venv/share/jupyter/kernels/registry-burman-2023
0 error(s)
pass  reproduce_burman_2023.ipynb  (147 s)
pass  network_model.ipynb  (1091 s)

real	20m45.665s
user	58m24.918s
sys	0m25.587s
```

**Agent calls Bash**

```bash
cd executed/burman-2023 && python - <<'EOF'
import json
for nb, idx in (('network_model.ipynb', None), ('reproduce_burman_2023.ipynb', [8,12,13,22,23,24,30,31,32,33,34])):
[... 32 more lines not kept]
````

**Agent calls Bash**

```bash
cd transcripts/burman-2023; grep -n "shunting  *-60\|hyperpolarizing  *-80\|^seed\|^1  *0\.9" author-revise-1.md | head -50 | cut -c1-200
```

```
1194:seed=7
1669:seeds are not known.""")
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; sed -n 1625,1665p author-revise-1.md | cut -c1-250
```

````
=== network_model.ipynb [3]
spikes, periodic stimulus: 19093 | gist's whole-run array: 19093
identical spike trains: True
inhibitory-to-excitatory summed weight (nS): start 15905, after balancing 16646.9, after test 16646.9

=== network_model.ipynb [5]
Time elapsed: 8.72 seconds.
Time elapsed: 1.14 seconds.
excitatory spikes, gist: 19093 | network.simulate: 19093
identical spike trains: True
spike_counts (-80 mV): equal in 800 of 800 neurons
firing_rates (-80 mV): equal in 800 of 800 neurons
entropy (-80 mV): equal in 800 of 800 neurons
synchrony (-80 mV): equal in 800 of 800 neurons

=== network_model.ipynb [6]
147          0.8721    0.9361
[... 196 more lines not kept]
```

[... 21 more lines not kept]
````

**Agent calls Bash**

```bash
cd transcripts/burman-2023; sed -n 2438,2482p author.md | grep "0.8721"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; sed -n 2436,2485p author.md
```

````
=== cell 4 ['sanity']
20 runs in 31.7 min (4 processes); peak memory of this process 0.36 GB, of a child 2.17 GB
    seed        condition  E_GABA  spikes_in_condition  neurons_with_spikes  rate_mean  entropy_mean  synchrony_mean  accuracy
0      1         shunting     -60              2119560                  800    19.5021        0.4647          0.7782    0.9820
1      1  hyperpolarizing     -80               927971                  800     8.6719        0.1798          0.8909    0.9437
2      2         shunting     -60              2107732                  800    19.3281        0.4527          0.7828    0.9785
3      2  hyperpolarizing     -80               927676                  800     8.7865        0.2042          0.8767    0.9328
4      3         shunting     -60              2118960                  800    19.3958        0.4598          0.7791    0.9866
5      3  hyperpolarizing     -80               942619                  800     8.9146        0.1986          0.8813    0.9225
6      4         shunting     -60              2110248                  800    19.3885        0.4475          0.7842    0.9906
7      4  hyperpolarizing     -80               913382                  800     8.6448        0.1955          0.8825    0.9527
8      5         shunting     -60              2126850                  800    19.4938        0.4446          0.7869    0.9919
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/w/venv/bin/activate; uv pip list 2>/dev/null | grep -i -E "cython|setuptools|brian|scikit|requests|statsmodels|remfile|h5py|pynwb|numpy|scipy|pandas|matplotlib"
```
[... 29 more lines not kept]
````

**Agent calls Bash**

```bash
cd entries/burman-2023; cat > $TMPDIR/t3.py <<'E'
import os, time, pickle
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np, network
cap=[]
orig=network.cross_val_score
def cvs(est, X, y, cv):
    cap.append((X.copy(), y.copy())); return orig(est, X, y, cv=cv)
network.cross_val_score=cvs
t=time.time()
r=network.simulate(1)
print("min", (time.time()-t)/60, r[-60]["accuracy"], r[-80]["accuracy"], np.nanmean(r[-80]["synchrony"]))
pickle.dump(cap, open(os.environ["TMPDIR"]+"/cap1.pkl","wb"))
E
date -u; PYTHONPATH=. $TMPDIR/v/bin/python $TMPDIR/t3.py 2>&1 | tail -2; date -u
```

```
Tue Nov 10 11:07:28 UTC 2026
min 1.8915751258532205 0.984 0.9423999999999999 0.8909234741971116
Tue Nov 10 11:09:24 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t4.py <<'E'
import os, pickle, numpy as np
from threadpoolctl import threadpool_limits, threadpool_info
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
cap=pickle.load(open(os.environ["TMPDIR"]+"/cap1.pkl","rb"))
print([ (d['internal_api'], d['num_threads']) for d in threadpool_info()])
for X,y in cap:
    Xs=X[:, :50]
    print(type(X), X.dtype, X.shape)
    for n in (1,2,4):
        with threadpool_limits(n):
            print(n, np.mean(cross_val_score(KNeighborsClassifier(), Xs, y, cv=StratifiedKFold(5,shuffle=True,random_state=1))),
                  np.mean(cross_val_score(KNeighborsClassifier(), Xs.toarray(), y, cv=StratifiedKFold(5,shuffle=True,random_state=1))))
E
cd $TMPDIR; $TMPDIR/v/bin/python t4.py; OMP_NUM_THREADS=1 $TMPDIR/v/bin/python t4.py
```

```
[('openblas', 4), ('openmp', 4), ('openblas', 4)]
<class 'scipy.sparse._csr.csr_matrix'> float64 (10000, 50)
1 0.984 0.9824999999999999
2 0.984 0.982
4 0.984 0.982
<class 'scipy.sparse._csr.csr_matrix'> float64 (10000, 50)
1 0.9423999999999999 0.9442999999999999
2 0.9423999999999999 0.942
4 0.9423999999999999 0.942
[('openmp', 1), ('openblas', 1), ('openblas', 1)]
<class 'scipy.sparse._csr.csr_matrix'> float64 (10000, 50)
1 0.984 0.9824999999999999
2 0.984 0.982
4 0.984 0.9821
<class 'scipy.sparse._csr.csr_matrix'> float64 (10000, 50)
1 0.9423999999999999 0.9442999999999999
2 0.9423999999999999 0.942
4 0.9423999999999999 0.9410999999999999
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t5.py <<'E'
import os, pickle, numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import NearestNeighbors
cap=pickle.load(open(os.environ["TMPDIR"]+"/cap1.pkl","rb"))
for X,y in cap:
    Xs=X[:, :50]; tied=0; n=0
    for tr,te in StratifiedKFold(5,shuffle=True,random_state=1).split(Xs,y):
        d,_=NearestNeighbors(n_neighbors=6).fit(Xs[tr]).kneighbors(Xs[te])
        tied+=np.sum(np.isclose(d[:,4],d[:,5])); n+=len(te)
    print(tied/n)
E
cd $TMPDIR; $TMPDIR/v/bin/python t5.py
```

```
0.8098
0.9155
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t6.py <<'E'
import os, pickle, numpy as np, time
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
cap=pickle.load(open(os.environ["TMPDIR"]+"/cap1.pkl","rb"))
def ties(X, y, seed, orders=5):
    rng = np.random.default_rng(seed)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    tied, acc = 0, np.zeros(orders)
    for tr, te in cv.split(X, y):
        d, _ = NearestNeighbors(n_neighbors=6).fit(X[tr]).kneighbors(X[te])
        tied += np.sum(d[:, 4] == d[:, 5])
        for k in range(orders):
            p = rng.permutation(tr)
            acc[k] += KNeighborsClassifier().fit(X[p], y[p]).score(X[te], y[te]) / 5
    return tied / len(y), acc
for X,y in cap:
    t=time.time(); print(ties(X[:, :50], y, 1), time.time()-t)
E
cd $TMPDIR; $TMPDIR/v/bin/python t6.py
```

```
(np.float64(0.8098), array([0.9829, 0.9834, 0.9825, 0.9824, 0.984 ])) 2.8717358112335205
(np.float64(0.9155), array([0.942 , 0.9425, 0.9436, 0.9414, 0.9438])) 2.1361606121063232
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
import json
nb=json.load(open('reproduce_burman_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print('=====',i,c['cell_type']); print(s if c['cell_type']=='markdown' else s[:1500])
E
```

```
<persisted-output>
Output too large (30KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2bf9abb4-be50-4c5b-8dbe-6451d20dc4a6/tool-results/bje16vld3.txt

Preview (first 2KB):
===== 0 markdown
# Reproducing Burman et al. (2023) on DANDI:000458: Neuropixels claims

**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)

**Dataset.** [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), version
0.230317.0039 (doi:10.48324/dandi.000458/0.230317.0039), the Allen Institute recordings of Claar et
al. (2023) that the paper reuses (Figure 4A to 4D, Figure S6). This is the only published version
of the dandiset, and the one the paper's analysis code names in its docstring
(gist a77bcf5e, revision 43a13d89), so it is pinned. The draft has the same 24 assets (checked below).

**Text the claims were written from.** The version of record (Europe PMC, PMC11913778), with STAR
Methods; the supplement (Figures S1 to S7) was not available (claims file, opening comment).

[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
import json
nb=json.load(open('reproduce_burman_2023.ipynb'))
for i in (18,19,20,22,24,31,37):
    c=nb['cells'][i]
    print('=====',i,c['cell_type']); print(''.join(c['source'])[:2500])
E
grep -n "start_time\|start time" ../../attempts/burman-2023-01.yaml README.md
```

```
===== 18 markdown
## fig4c-sample

> After excluding 203 neurons with evoked rates below 0.1 Hz or above 200 Hz, 662 regular spiking
> neurons remain, from 17 recordings in 16 mice, a median of 34 per recording (1 to 93).

Judged under the Methods reading A1F1 (the spike count rate); A1F2, A2F1, A2F2 and the gist's
waveform cut are variants (claims file, N7).
===== 19 code
tables, kept = {}, {}
for name, (area, wf, rate) in npx.READINGS.items():
    T = npx.all_units(S, area, wf)
    ex = npx.excluded(T, rate)
    tables[name], kept[name] = T, T[~ex].copy()
rows = []
for name, (area, wf, rate) in npx.READINGS.items():
    T, K = tables[name], kept[name]
    per = K.groupby("session").size().reindex(npx.SESSIONS, fill_value=0)
    low = ((T[f"rate_{rate}_aw"] < 0.1) | (T[f"rate_{rate}_an"] < 0.1)).sum()
    high = ((T[f"rate_{rate}_aw"] > 200) | (T[f"rate_{rate}_an"] > 200)).sum()
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
import json
nb=json.load(open('reproduce_burman_2023.ipynb'))
for i in range(32,37):
    c=nb['cells'][i]
    print('=====',i,c['cell_type']); print(''.join(c['source'])[:3000])
E
sed -n 60,240p ../../attempts/burman-2023-01.yaml
```

```
===== 32 markdown
**Result: reproduced.** Under A1F1 the mean evoked rate is 14.0 Hz awake against 7.59 Hz under
isoflurane (paired t test, t = 12.36, p = 5.75e-32, table above), higher awake in 539 of 721 units
and 15 of 17 recordings; every reading gives the same direction.
===== 33 markdown
## figs6-rate-regressed

> The awake decrease in synchrony and increase in entropy remain after the effect of firing rate
> is regressed out.

Readings from the criterion: (R1) one linear regression of the measure on the evoked rate across
all unit and condition values, residuals compared by the paired t test; (R2) OLS of the measure on
condition and rate, condition coefficient tested; (R3) per unit, the awake minus isoflurane
difference of the measure regressed on the difference of rate, intercept tested. The rate is the
reading's own (F1 under A1F1).
===== 34 code
def regressed(K, measure, rate):
    a, b = K[measure + "_aw"], K[measure + "_an"]
    ok = a.notna() & b.notna()
    K = K[ok]
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; sed -n 1,56p network.py; date -u
```

```
"""The leaky integrate-and-fire network of Burman et al. (2023), Figures 4E to 4H and S7.

A transcription of the paper's simulation gist,
gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision
f6a05661c10051560aa381e334099efd8521617b (burman_et_al_2023_neuronal_network_simulation.py),
which the claims file names as the method of the model claims. Every parameter below is the
gist's, and matches the Methods ("Neuronal network simulations", Table 1): 800 excitatory and
200 inhibitory neurons, connection probability 10%, weights 0.1 nS and 1 nS, Vogels
inhibitory plasticity during a balancing set, E_GABA -60 mV then -80 mV in the excitatory
neurons, 100 input patterns of 1 ms pulses (M = 500 pA) every 25 ms, each repeated 100 times
per condition, and lognormal noise (M = 25 pA) changed every 10 ms.

Differences from the gist, none of which changes the model:

- The gist builds the stimulus as one array for the whole run (502,500 by 1,000 values,
  4 GB, copied again when given units), which does not fit the runner's memory with a second
  copy. The stimulus is periodic (the same 100 patterns in every 2,500 ms set), so here the
  TimedArray holds one set and is read at t modulo the set's length. The values each neuron
  receives at each time step are the same.
- Random seeds are fixed, one per run (protocol: fix every seed); the gist sets none. The
[... 37 more lines not kept]
```

**Agent**

Now I'll add the tie diagnostic to `network.py`.

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
p='network.py'; s=open(p).read()
old='''- The analysis returns the values the gist writes to its CSV (spike count, firing rate,
  entropy, synchrony per excitatory neuron, and the decoding accuracy) as arrays.
"""'''
new='''- The analysis returns the values the gist writes to its CSV (spike count, firing rate,
  entropy, synchrony per excitatory neuron, and the decoding accuracy) as arrays.
- In addition to the gist's accuracy, decoding_ties() reports how often the classifier's five
  nearest neighbours are tied with the sixth, and the accuracy when tied neighbours are chosen
  by other training orders (the spike counts are small integers, so most distances tie).
"""'''
assert old in s; s=s.replace(old,new)
old='''from sklearn.neighbors import KNeighborsClassifier
'''
new='''from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors
'''
s=s.replace(old,new)
old='''def simulate(seed,'''
new='''def decoding_ties(X, y, seed, orders=5):
    """The gist's decoder (5 nearest neighbours, 5-fold shuffled stratified cross-validation
    with the same folds as simulate) examined for ties. Returns the share of test trials whose
    fifth-nearest training trial is at the same distance as the sixth, so that the five
    neighbours are chosen by how ties are broken, and the mean accuracy for each of `orders`
    random orders of the training trials, which break those ties differently."""
    rng = np.random.default_rng(seed)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    tied, acc = 0, np.zeros(orders)
    for train, test in cv.split(X, y):
        d, _ = NearestNeighbors(n_neighbors=6).fit(X[train]).kneighbors(X[test])
        tied += int(np.sum(d[:, 4] == d[:, 5]))
        for k in range(orders):
            p = rng.permutation(train)
            acc[k] += KNeighborsClassifier().fit(X[p], y[p]).score(X[test], y[test]) / 5
    return tied / len(y), acc


def simulate(seed,'''
s=s.replace(old,new,1)
old='''        accuracy = np.mean(cross_val_score(KNeighborsClassifier(), X[:, :50], y, cv=cv))
'''
new='''        accuracy = np.mean(cross_val_score(KNeighborsClassifier(), X[:, :50], y, cv=cv))
        tied_share, accuracy_orders = decoding_ties(X[:, :50], y, seed)
'''
assert old in s; s=s.replace(old,new)
old='''entropy=entropy, synchrony=synchrony, accuracy=accuracy,'''
new='''entropy=entropy, synchrony=synchrony, accuracy=accuracy,
                           tied_share=tied_share, accuracy_orders=accuracy_orders,'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
E
cd $TMPDIR && cat > t7.py <<'E'
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import network
a = network.simulate(7, stimuli=10, repeats=5)
print(a[-60]["accuracy"], a[-60]["tied_share"], a[-60]["accuracy_orders"])
E
PYTHONPATH=entries/burman-2023 $TMPDIR/v/bin/python t7.py 2>&1 | tail -2
```

```
0.96 0.38 [0.96 0.96 0.96 0.96 0.94]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
import json
p='network_model.ipynb'; nb=json.load(open(p)); C=nb['cells']
def setsrc(i, s): C[i]['source']=s.splitlines(keepends=True)
s=''.join(C[18]['source'])
s=s.rstrip('\n')+'''

The spike counts are small integers, so many training trials are at the same distance from a
test trial, and which of them are the five neighbours depends on how the classifier breaks ties.
That is not fixed by the seeds: the same spikes give somewhat different accuracies on different
machines and installations (earlier executions of this notebook printed D1 t = 16.92 and 16.42).
So the cell below also gives, per condition, the share of test trials whose fifth neighbour is
tied with the sixth, and D1 and D2 recomputed with tied neighbours chosen by five other random
orders of the training trials (`network.decoding_ties`).
'''
setsrc(18, s)
s=''.join(C[19]['source'])
old='print(f"\\nnotebook run time'
assert old in s
add='''tied = per_run.pivot(index="seed", columns="condition", values="tied_share")
print("\\ntest trials whose fifth neighbour is tied with the sixth: shunting %.2f to %.2f, hyperpolarizing %.2f to %.2f (share per run)"
      % (tied.shunting.min(), tied.shunting.max(), tied.hyperpolarizing.min(), tied.hyperpolarizing.max()))
orders = {cond: np.array([r[eg]["accuracy_orders"] for r in runs]) for eg, cond in zip(network.EGABA, ("shunting", "hyperpolarizing"))}
spread = {cond: (a.max(axis=1) - a.min(axis=1)) for cond, a in orders.items()}
print("range of a run's accuracy over the five training orders: shunting up to %.4f, hyperpolarizing up to %.4f"
      % (spread["shunting"].max(), spread["hyperpolarizing"].max()))
for k in range(orders["shunting"].shape[1]):
    sh, hy = orders["shunting"][:, k], orders["hyperpolarizing"][:, k]
    tk = stats.ttest_rel(sh, hy)
    print(f"training order {k + 1}: mean shunting {sh.mean():.4f}, hyperpolarizing {hy.mean():.4f}; "
          f"D1 t = {tk.statistic:.2f}, p = {tk.pvalue:.2e}; D2 {(sh > hy).sum()} of {len(sh)}")
'''
s=s.replace(old, add+old)
setsrc(19, s)
s=''.join(C[6]['source'])
old='synchrony_mean=np.nanmean(d["synchrony"]), accuracy=d["accuracy"]))'
assert old in s
s=s.replace(old,'synchrony_mean=np.nanmean(d["synchrony"]), accuracy=d["accuracy"],\n                         tied_share=d["tied_share"]))')
setsrc(6, s)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
E
git diff --stat; tail -c 200 network_model.ipynb | od -c | tail -3; git show HEAD:entries/burman-2023/network_model.ipynb | tail -c 50 | od -c | tail -3
```

```
entries/burman-2023/network.py          | 25 ++++++++++++++++++++++++-
 entries/burman-2023/network_model.ipynb | 25 +++++++++++++++++++++++--
 2 files changed, 47 insertions(+), 3 deletions(-)
0000260  \n       "   n   b   f   o   r   m   a   t   _   m   i   n   o
0000300   r   "   :       5  \n   }  \n
0000310
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
import json
p='reproduce_burman_2023.ipynb'; nb=json.load(open(p)); C=nb['cells']
assert ''.join(C[37]['source']).startswith('## Summary')
md={"cell_type":"markdown","metadata":{},"source":'''## Times from start_time

The claims file (N3) takes spike times from each trial's stop_time, as the gist does; the Methods
say only "following an electrical stimulus". Under A1F1 with times from start_time, the pulse
onset 0.4 ms earlier, the sample, the rate test and the regressions (synchrony and entropy are in
the variant tables of their claims above).'''.splitlines(keepends=True)}
code={"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":'''# Tst and Kst (A1F1, times from start_time) are built in the synchrony variants above
per = Kst.groupby("session").size().reindex(npx.SESSIONS, fill_value=0)
print("start_time, A1F1: selected %d, kept %d, excluded %d, recordings %d, mice %d, median %.0f per recording (%d to %d)"
      % (len(Tst), len(Kst), len(Tst) - len(Kst), (per > 0).sum(), Kst.subject.nunique(),
         per[per > 0].median(), per[per > 0].min(), per.max()))
r = npx.paired(Kst, "rate_F1")
print("evoked rate: " + ", ".join(f"{k} {v:.3g}" for k, v in r.items()))
reg_st = pd.DataFrame([dict(measure=m, **regressed(Kst, m, "F1")) for m in ("synchrony", "entropy")])
with pd.option_context("display.float_format", "{:.3g}".format):
    print(reg_st.to_string())'''.splitlines(keepends=True)}
C[37:37]=[md,code]
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
E
grep -n "def paired" -A25 npx.py | head -40
```

```
337:def paired(df, measure):
338-    """Mean and SEM per condition and the paired t test (scipy.stats.ttest_rel) over units with
339-    the measure defined in both conditions (N8)."""
340-    from scipy import stats
341-    a, b = df[measure + "_aw"], df[measure + "_an"]
342-    ok = a.notna() & b.notna()
343-    t = stats.ttest_rel(a[ok], b[ok])
344-    return dict(n=int(ok.sum()), awake=a[ok].mean(), awake_sem=a[ok].sem(),
345-                anesthetized=b[ok].mean(), anesthetized_sem=b[ok].sem(),
346-                t=float(t.statistic), p=float(t.pvalue), dropped=int((~ok).sum()))
347-
348-
349-# ---------------------------------------------------------------- the paper's own code
350-
351-GIST_URL = ("https://gist.githubusercontent.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf/raw/"
352-            "43a13d89441b7f56e835e84fa5811d9567917daf/burman_et_al_2023_neuropixel_data_analysis.py")
353-
354-
355-def run_gist(sessions):
356-    """Run the paper's analysis gist, unmodified, on sessions loaded by read_session, and return
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/burman-2023 2>&1 | grep -v MissingID | tail -8; date -u
```

```
Tue Nov 10 11:11:11 UTC 2026
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-burman-2023 in executed/burman-2023/.venv/share/jupyter/kernels/registry-burman-2023
0 error(s)
pass  reproduce_burman_2023.ipynb  (158 s)
pass  network_model.ipynb  (1199 s)
Tue Nov 10 11:33:55 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import json
for p in ('entries/burman-2023/reproduce_burman_2023.ipynb','entries/burman-2023/network_model.ipynb'):
    nb=json.load(open(p)); print(p, nb['nbformat_minor'], [i for i,c in enumerate(nb['cells']) if 'id' not in c][:5], len(nb['cells']))
"; git stash -q; python tools/entry.py check entries/burman-2023 2>&1 | grep -v MissingID | tail -3; git stash pop -q; git status --short
```

```
entries/burman-2023/reproduce_burman_2023.ipynb 5 [37, 38] 40
entries/burman-2023/network_model.ipynb 5 [] 22
0 error(s)
 M entries/burman-2023/network.py
 M entries/burman-2023/network_model.ipynb
 M entries/burman-2023/reproduce_burman_2023.ipynb
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
cd  python - <<'E'
import json, uuid
p='entries/burman-2023/reproduce_burman_2023.ipynb'; nb=json.load(open(p))
nb['cells'][37]['id']='start-time-md'; nb['cells'][38]['id']='start-time-variant'
# executed copy order of keys: id first like others
for i in (37,38):
    c=nb['cells'][i]; nb['cells'][i]={'cell_type':c['cell_type'],'id':c['id'],**{k:v for k,v in c.items() if k not in('cell_type','id')}}
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
E
python - <<'E'
import json
for nb,idx in (('executed/burman-2023/network_model.ipynb',[6,10,13,16,19]),('executed/burman-2023/reproduce_burman_2023.ipynb',[4,8,13,19,23,24,27,28,31,34,35,38])):
    d=json.load(open(nb))
    for i in idx:
        c=d['cells'][i]
        out=''.join(''.join(o.get('text','')) for o in c['outputs'] if o.get('output_type')=='stream')
        print(f'=== {nb[19:27]} [{i}]'); print(out[-3500:])
E
```

```
Exit code 1
=== 3/networ [6]
nting     -60              2111375                  800    19.4979        0.4569          0.7802    0.9810      0.8100
17     9  hyperpolarizing     -80               916273                  800     8.6990        0.1982          0.8804    0.9246      0.9086
18    10         shunting     -60              2106731                  800    19.4406        0.4532          0.7816    0.9824      0.8144
19    10  hyperpolarizing     -80               918057                  800     8.7604        0.2091          0.8740    0.9411      0.9118
20    11         shunting     -60              2122344                  800    19.3906        0.4513          0.7833    0.9883      0.8139
21    11  hyperpolarizing     -80               925992                  800     8.9094        0.2147          0.8721    0.9361      0.9124
22    12         shunting     -60              2102812                  800    19.4031        0.4476          0.7852    0.9857      0.8133
23    12  hyperpolarizing     -80               923217                  800     8.7615        0.2012          0.8777    0.9466      0.8991
24    13         shunting     -60              2132477                  800    19.6771        0.4409          0.7882    0.9829      0.8041
25    13  hyperpolarizing     -80               927808                  800     8.7719        0.1945          0.8817    0.9326      0.9123
26    14         shunting     -60              2110910                  800    19.4427        0.4553          0.7810    0.9815      0.7987
27    14  hyperpolarizing     -80               924724                  800     8.7510        0.1962          0.8817    0.9464      0.9122
28    15         shunting     -60              2122543                  800    19.5927        0.4588          0.7807    0.9891      0.8093
29    15  hyperpolarizing     -80               930883                  800     8.8552        0.2200          0.8690    0.9369      0.9073
30    16         shunting     -60            
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
for nb,idx in (('executed/burman-2023/network_model.ipynb',[3,5,16,19]),('executed/burman-2023/reproduce_burman_2023.ipynb',[4,8,28,31,34,35,38])):
    d=json.load(open(nb))
    for i in idx:
        c=d['cells'][i]
        out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]) if o.get('output_type')=='stream')
        print(f'=== {nb[19:27]} [{i}]'); print(out[-2500:])
E
```

```
=== 3/networ [3]
spikes, periodic stimulus: 19093 | gist's whole-run array: 19093
identical spike trains: True
inhibitory-to-excitatory summed weight (nS): start 15905, after balancing 16646.9, after test 16646.9

=== 3/networ [5]
Time elapsed: 8.70 seconds.
Time elapsed: 1.12 seconds.
excitatory spikes, gist: 19093 | network.simulate: 19093
identical spike trains: True
spike_counts (-80 mV): equal in 800 of 800 neurons
firing_rates (-80 mV): equal in 800 of 800 neurons
entropy (-80 mV): equal in 800 of 800 neurons
synchrony (-80 mV): equal in 800 of 800 neurons

=== 3/networ [16]
neurons 16000; peri-stimulus rate shunting 19.468 +- 0.026 Hz, hyperpolarizing 8.785 +- 0.020 Hz; paired t = 446.42, p = 0.00e+00
neurons with no peri-stimulus spike: shunting 0, hyperpolarizing 0
runs with lower mean rate under hyperpolarizing: 20 of 20
spikes over the whole condition (all 100 repeats), hyperpolarizing / shunting: 0.431 to 0.445
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; grep -n "minute\|tolerance\|0.001 to\|runtime" README.md entry.yaml
```

```
README.md:31:partial model outcomes are hyperpolarizing means 0.001 to 0.002 outside tolerances narrower than
README.md:35:- `reproduce_burman_2023.ipynb`: the Neuropixels claims. About two minutes, most of it streaming the
README.md:37:- `network_model.ipynb`: 20 runs of the paper's network model on four processes, about 20 minutes.
entry.yaml:15:  runtime_minutes: 3
entry.yaml:18:  runtime_minutes: 18
```

**Agent calls Bash**

```bash
cd entries/burman-2023; sed -n 20,45p README.md; sed -n 10,20p entry.yaml
```

```
| Model: entropy higher with shunting E_GABA (0.451 against 0.197 nats) | Partially reproduced |
| Model: shunting networks decoded more accurately | Reproduced |
| Multi-compartment model of Figure S4 | Blocked: methods underspecified |
| Patch-clamp findings of Figures 1 to 3 and S1 to S5 (24 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The three partial outcomes on the dandiset come from the evoked rate used to exclude neurons. The
claims are judged under the Methods' rate, a spike count; under the rate the paper's own code
computes, which sums spike latencies, the dandiset gives the paper's numbers exactly. The two
partial model outcomes are hyperpolarizing means 0.001 to 0.002 outside tolerances narrower than
the spread between runs. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/burman-2023-01.yaml`](../../attempts/burman-2023-01.yaml).

- `reproduce_burman_2023.ipynb`: the Neuropixels claims. About two minutes, most of it streaming the
  units and trials of 24 files.
- `network_model.ipynb`: 20 runs of the paper's network model on four processes, about 20 minutes.
- `npx.py`: loading the dandiset and the per-unit measures (rate, entropy, synchrony) of the paper's
  code. Other notebooks on this dandiset can import it.
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
p='README.md'; s=open(p).read()
reps=[("partial model outcomes are hyperpolarizing means 0.001 to 0.002 outside tolerances narrower than\nthe spread between runs.",
"partial model outcomes are hyperpolarizing means 0.0011 and 0.0024 outside tolerances narrower than\nthe spread between runs."),
("About two minutes, most of it streaming the\n  units and trials of 24 files.",
"About 2.5 to 3.5 minutes (2.5 on the last\n  run, 3.5 on a slower runner), most of it streaming the units and trials of 24 files."),
("on four processes, about 20 minutes.",
"on four processes, about 20 minutes on the last\n  run and 43 minutes on a slower runner."),]
for a,b in reps:
    assert a in s, a; s=s.replace(a,b)
open(p,'w').write(s)
E
sed -i 's/  runtime_minutes: 18/  runtime_minutes: 20/' entry.yaml; date -u
```

```
Tue Nov 10 11:34:23 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
import json
p='network_model.ipynb'; nb=json.load(open(p)); C=nb['cells']
def rep(i, old, new):
    s=''.join(C[i]['source']); assert old in s, old; C[i]['source']=s.replace(old,new).splitlines(keepends=True)
rep(18, "That is not fixed by the seeds: the same spikes give somewhat different accuracies on different\nmachines and installations (earlier executions of this notebook printed D1 t = 16.92 and 16.42).",
"That is not fixed by the seeds: executions of this notebook on different runners, with the same\nper-run rate, entropy and synchrony, have printed D1 t = 16.92 (p = 6.52e-13) and t = 16.42\n(p = 1.11e-12) from slightly different per-run accuracies.")
rep(20, "D1 paired t = 16.42, p = 1.11e-12, and D2 holds, shunting higher in 20 of 20 runs.",
"D1 paired t = 16.42, p = 1.11e-12, and D2 holds, shunting higher in 20 of 20 runs. Most test trials have a tie at the fifth neighbour (0.80 to 0.81 of them under shunting, 0.90 to 0.92 under hyperpolarizing), so the accuracies depend on how ties are broken; over five other training orders a run's accuracy moves by at most 0.0020 (shunting) and 0.0045 (hyperpolarizing), D1 gives t = 16.35 to 17.22 (p at most 1.20e-12) and D2 holds in 20 of 20 runs each time. The conclusion does not depend on the tie-breaking.")
rep(21, "| figs7-model-decoding | reproduced |", "| figs7-model-decoding | reproduced (under every tie-breaking order tried) |")
rep(21, "entropy and synchrony as the gist; in every full run the learning rate in the compiled synapse\ncode is 0.1 during balancing and 0 during the test (checked above).",
"entropy and synchrony as the gist; in every full run the learning rate in the compiled synapse\ncode is 0.1 during balancing and 0 during the test (checked above). The seeds fix the spikes but\nnot the decoding accuracy exactly, as the classifier's ties between equally distant trials are\nbroken differently on different runners; the decoding conclusion holds under each tie-breaking\norder tried.")
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')

p='reproduce_burman_2023.ipynb'; nb=json.load(open(p)); C=nb['cells']
assert ''.join(C[39]['source']).startswith('## Summary')
i=39
rep(39, "The three partial\noutcomes are this difference: the effects are there, at the paper's significance, with means a\nlittle off under the Methods' rate.",
"The three partial\noutcomes are this difference: the effects are there, at the paper's significance, with the\nexcluded count (144 against 203) and the means a little off under the Methods' rate.")
rep(39, "with every field needed, and their labels and clocks pass the checks above.",
"with every field needed, and their labels pass the checks above; the clocks pass in 33 of 34\nfile and condition pairs, the exception being sub-569069 awake, whose evoked count is not above\nthe shifted-window count (ratio 1.07, p = 0.591).")
# result markdown for start_time
C[37]['source']=(''.join(C[37]['source'])+'''

With times from start_time, 734 units are kept and 131 excluded (median 37 per recording, 8 to
96); the evoked rate is higher awake (14.9 against 8.14 Hz, p = 9.58e-35); with the rate regressed
out synchrony stays lower and entropy higher awake under R1, R2 and R3 (all p below 1e-11). The
directions are those under stop_time.''').splitlines(keepends=True)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
E
grep -n "569069" ../../attempts/burman-2023-01.yaml | head -3
```

```
47:    0.001); the exception is the awake trials of sub-569069_ses-20210312 (1.55 against 1.45 spikes per
455:      at p below 0.001, and the one that does not (sub-569069 awake) is named in the notebook and the
```

**Agent calls Bash**

```bash
cd  sed -n 40,50p attempts/burman-2023-01.yaml; python - <<'E'
import json
d=json.load(open('executed/burman-2023/reproduce_burman_2023.ipynb'))
out=''.join(''.join(o.get('text','')) for o in d['cells'][8]['outputs'] if o.get('output_type')=='stream')
print([l for l in out.splitlines() if '569069' in l or 'ratio' in l.lower() or 'session ' in l][:5])
E
```

```
waveform_duration in its units table, stimulus_type, behavioral_epoch, is_valid, estim_target_region
    and stop_time in its trials table, and awake and isoflurane electrical trials. They hold 16 subjects
    (sub-569073 twice, one MOs and one SSp session). Unit ids equal row numbers in every file, so the
    gist's keying of units by row and lookup by id select the same units. The version holds seven more
    files, six with EEG only and sub-599017 with units and SSp stimulation, which the gist does not read.
    The clock check covers all 17 files. In 33 of 34 file and condition pairs, spikes 2 to 12 ms after the
    pulse exceed those of the same window 1.5 s before and after it (1.5 to 39 times, Wilcoxon p below
    0.001); the exception is the awake trials of sub-569069_ses-20210312 (1.55 against 1.45 spikes per
    trial, p = 0.59), whose isoflurane trials, on the same file clock, pass (2.2 times, p = 2e-12).
- claim: fig4c-sample
  outcome: partially_reproduced
['                    session   condition  trials  units  evoked  shift -1.5 s  shift +1.5 s  evoked / shifted  wilcoxon p', '12  sub-569069_ses-20210312       awake     357     29    1.55          1.53          1.36              1.07       0.591', '13  sub-569069_ses-20210312  isoflurane     359     29   0.967          0.39         0.482              2.22    2.13e-12']
```

**Agent calls Bash**

```bash
cd entries/burman-2023; python - <<'E'
import json
p='reproduce_burman_2023.ipynb'; nb=json.load(open(p)); C=nb['cells']
s=''.join(C[39]['source'])
old="sub-569069 awake, whose evoked count is not above\nthe shifted-window count (ratio 1.07, p = 0.591)."
assert old in s
C[39]['source']=s.replace(old,"sub-569069 awake, whose evoked count is only 1.07\ntimes the shifted-window count (p = 0.591).").splitlines(keepends=True)
s=''.join(C[37]['source']); head, res = s.split('\n\nWith times from start_time, ')
C[37]['source']=head.splitlines(keepends=True)
C.insert(39, {"cell_type":"markdown","id":"start-time-result","metadata":{},"source":("**Result.** With times from start_time, "+res).splitlines(keepends=True)})
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
for i in (37,38,39,40): print(i, ''.join(C[i]['source'])[:150].replace('\n',' '))
E
```

```
37 ## Times from start_time  The claims file (N3) takes spike times from each trial's stop_time, as the gist does; the Methods say only "following an ele
38 # Tst and Kst (A1F1, times from start_time) are built in the synchrony variants above per = Kst.groupby("session").size().reindex(npx.SESSIONS, fill_v
39 **Result.** With times from start_time, 734 units are kept and 131 excluded (median 37 per recording, 8 to 96); the evoked rate is higher awake (14.9 
40 ## Summary  | Claim | Outcome | |---|---| | dataset-sessions-link | reproduced | | fig4c-sample | partially reproduced (exact under the gist's rate) |
```

**Agent calls Bash**

```bash
cd  sed -n 636,760p attempts/burman-2023-01.yaml; grep -n "^[a-z_]*:" attempts/burman-2023-01.yaml
```

```
agrees: true
    outcome: blocked
    reason: The version has 24 assets, all behavior+ecephys NWB files holding Units, ElectricalSeries, LFP
      and behavior, with no intracellular recordings; a DANDI search for Burman, Akerman and gramicidin
      returns no dandiset. No part can be tested (data_missing).
    response: No change.
  - claim: fig2j-awake-df-zero
    agrees: true
    outcome: blocked
    reason: The version has 24 assets, all behavior+ecephys NWB files holding Units, ElectricalSeries, LFP
      and behavior, with no intracellular recordings; a DANDI search for Burman, Akerman and gramicidin
      returns no dandiset. No part can be tested (data_missing).
    response: No change.
  - claim: fig2k-conductance-same
    agrees: true
    outcome: blocked
    reason: The version has 24 assets, all behavior+ecephys NWB files holding Units, ElectricalSeries, LFP
      and behavior, with no intracellular recordings; a DANDI search for Burman, Akerman and gramicidin
      returns no dandiset. No part can be tested (data_missing).
    response: No change.
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas 2>/dev/null; grep -rn "verifications" --include=*.json --include=*.py -l . 2>/dev/null | grep -v executed | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
./tests/test_entry_tool.py
./tests/test_build_site.py
./schemas/attempt.schema.json
./tools/entry.py
./tools/build_site.py
```

**Agent calls Bash**

```bash
cd  python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
def find(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items():
            if k in ('verifications','proposed'): print(path+'/'+k, json.dumps(v)[:1500])
            find(v,path+'/'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): find(v,path+f'[{i}]')
find(s)"
```

```
/properties/outcomes/items/properties/proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "reason": {"type": "string", "minLength": 1}}}
/properties/verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}}}}
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/burman-2023-01.yaml'; s=open(p).read()
old="    Timing from start_time, the pulse onset 0.4 ms earlier, is shown as a variant and keeps the direction.\n"
new=("    Timing from start_time, the pulse onset 0.4 ms earlier, is run as a variant under A1F1: 734 units kept\n"
     "    and 131 excluded, and synchrony, entropy, the rate test and the regressions keep their direction.\n")
assert s.count(old)==5; s=s.replace(old,new)
old="""    rate is asked of a reader (questions/burman-2023.yaml).
  deviations:
  - Judged under the Methods reading A1F1, as the claims file requires. The paper's numbers come out exactly
    under the gist's rate (A1F2, A2F2), which sums spike latencies where a count is expected; this claim
    holds fully only under that variant.
  - Trials of all stimulus currents and depths of a session are pooled and times are taken from stop_time,
    as the claims file (N3) gives from the gist; the Methods say only "following an electrical stimulus".
    Timing from start_time, the pulse onset 0.4 ms earlier, is run as a variant under A1F1: 734 units kept
    and 131 excluded,"""
assert s.count(old)==1, s.count(old)
s=s.replace(old, old.replace("    rate is asked of a reader (questions/burman-2023.yaml).\n",
 "    rate is asked of a reader (questions/burman-2023.yaml). The criterion's partial case (only the total\n"
 "    within 10%) does not literally cover this result, where the kept count is within tolerance too and\n"
 "    the excluded count is not; partial is the reading closest to it, and the gap is asked of a reader.\n"),1)
old="""  notes: Mean decoding accuracy 0.9848 shunting against 0.9315 hyperpolarizing (chance 0.01). D1, paired
    t test of the 20 per-run accuracies, t = 16.42, p = 1.11e-12; D2, shunting higher in 20 of 20 runs.
"""
assert old in s
new="""  notes: Mean decoding accuracy 0.9848 shunting against 0.9315 hyperpolarizing (chance 0.01). D1, paired
    t test of the 20 per-run accuracies, t = 16.42, p = 1.11e-12 in this execution; D2, shunting higher
    in 20 of 20 runs. The spike counts the classifier uses are small integers, and in 0.80 to 0.81 of
    the test trials under shunting and 0.90 to 0.92 under hyperpolarizing the fifth-nearest training
    trial is at the same distance as the sixth, so the accuracy depends on how ties are broken, which
    differs between runners. Executions on different runners, with the same per-run rate, entropy and
    synchrony, printed t = 16.92, p = 6.52e-13 (the first execution and the one verifier round 2 read)
    and t = 16.42, p = 1.11e-12 (the round-1 revision and this one). With tied neighbours chosen by five
    other random orders of the training trials, a run's accuracy moves by at most 0.0020 (shunting) and
    0.0045 (hyperpolarizing), D1 gives t = 16.35 to 17.22 (p at most 1.20e-12) and D2 holds in 20 of 20
    runs each time, so the outcome does not depend on the tie-breaking.
"""
s=s.replace(old,new)
old="""  - The cross-validation shuffle is seeded with the run's seed (the gist sets none), a standard choice
    that cannot change the outcome.
"""
assert old in s
new="""  - The cross-validation shuffle is seeded with the run's seed (the gist sets none). The seeds fix the
    spikes and the folds but not the accuracy exactly, as the classifier's ties between equally distant
    trials are broken differently on different runners; the notebook shows D1 and D2 under five other
    tie-breaking orders, and all give the same outcome.
"""
s=s.replace(old,new)
open(p,'w').write(s)
E
grep -n "0.230317\|seeded" attempts/burman-2023-01.yaml | head
```

```
6:  version: 0.230317.0039
7:  doi: 10.48324/dandi.000458/0.230317.0039
39:  notes: All 17 files the gist lists are in version 0.230317.0039, each with spike_times, location and
240:  - The cross-validation shuffle is seeded with the run's seed (the gist sets none). The seeds fix the
436:  statement: Version 0.230317.0039 holds 18 files with units and electrical stimulation awake and under
468:    reason: All 17 gist sessions are assets of 0.230317.0039, each has every units and trials field,
```

**Agent calls Bash**

```bash
cd  cat >> questions/burman-2023.yaml <<'E'
- claim: fig4c-sample
  asked: 2026-11-10
  question: >-
    The criterion gives reproduced when kept and excluded are both within 10% of 662 and 203, and
    partially reproduced when only the total (865) is within 10%. Under the Methods reading A1F1
    the kept count, 721, is within 662 +- 66.2 and the excluded count, 144, is outside 203 +- 20.3,
    a case neither branch names. The attempt gives partially reproduced. Should the partial case
    read "the total, and at most one of kept and excluded, within 10%", or is another outcome
    meant for this case?
  passage: >-
    Methods, Pre-processing of Neuropixels dataset, "Neurons with an average evoked firing rate
    below 0.1 Hz or above 200 Hz in either condition (awake/anesthesia) were excluded from further
    analysis (203 neurons). The 662 remaining neurons derived from 17 recordings in 16 mice".
  why: >-
    Raised by the verifier in round 2 as a small gap in the claims file. The outcome does not change
    under either reading of the gap; the wording of the criterion does.
E
python -c "import yaml;yaml.safe_load(open('questions/burman-2023.yaml'))"; grep -n "fig4c-sample" -A30 claims/burman-2023.yaml | grep -n "criterion" -A8 | head -12
```

```
41:689-  criterion: Synchrony (N6) per neuron and condition over the kept neurons, mean and SEM, paired t test
42-690-    (N8). Method N1 to N8 of the opening comment (Methods and the analysis gist), judged under the Methods
43-691-    reading A1F1, with A1F2, A2F1, A2F2 and the gist's waveform cut (> 0.4 ms) shown as variants (N7).
44-692-    Reproduced when both means are within tolerance and the paired t test gives awake lower at p < 0.001;
45-693-    partially reproduced when the direction and test hold but a mean is outside tolerance.
46-694-- id: fig4d-entropy-higher-awake
47-695-  statement: Peri-stimulus histogram entropy is higher awake than under isoflurane (1.347 against 1.111
48-696-    nats), so responses are more variable in time.
49-697-  source: Figure 4C and 4D (bottom); Results, Shunting inhibition promotes local network desynchronization
--
69:717-  criterion: Entropy (N5) per neuron and condition over the kept neurons, mean and SEM, paired t test
70-718-    (N8). Method N1 to N8 of the opening comment (Methods and the analysis gist), judged under the Methods
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;c=yaml.safe_load(open('claims/burman-2023.yaml'))
cl=c['claims'] if isinstance(c,dict) else c
for x in cl:
    if x['id']=='fig4c-sample': print(x['criterion'])
"
```

```
Counts of regular spiking units in the stimulated area (N2) before and after the exclusion (N7), per recording. Method N1 to N8 of the opening comment (Methods and the analysis gist), judged under the Methods reading A1F1, with A1F2, A2F1, A2F2 and the gist's waveform cut shown as variants (N7). Reproduced when the numbers kept and excluded are within tolerance and the recording and mouse counts are 17 and 16; partially reproduced when only the total (865) is within 10%. The per-recording median and range are reported under each reading.
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
p='attempts/burman-2023-01.yaml'
rec=yaml.safe_load(open(p))
outs={o['claim']:o for o in rec['outcomes']}
PC="Agrees with all 35 outcomes; the 24 patch-clamp claims are blocked, data_missing."
R={}
R['dataset-sessions-link']=("Reproduced. The Summary of the main notebook (cell 37) overstates the clocks: \"their labels and clocks pass the checks above\" is too strong, as main cell 8 passes 33 of 34 pairs and sub-569069 awake fails (ratio 1.07, p = 0.591); main cell 9 and the attempt notes state this correctly. The README's \"About two minutes\" for the main notebook does not match: cell 4 took 196 s to load, and cell 35 prints 3.5 min.",
 "The Summary now says the clocks pass in 33 of 34 file and condition pairs and names sub-569069 awake, with its ratio and p. The README now gives 2.5 to 3.5 minutes (2.5 in this execution, 3.5 in the one reviewed). Outcome unchanged.")
R['fig4c-sample']=("Partially reproduced under A1F1, with the A1F2 exact match recorded as a deviation. A small gap in the claims file: A1F1 keeps 721, inside 662 +- 66.2, and excludes 144, outside 203 +- 20.3; the criterion's partial case, \"only the total (865) is within 10%\", does not literally cover this, as the kept count is within tolerance too, but partial is still the sensible reading. The deviation says timing from start_time \"is shown as a variant and keeps the direction\", but the start_time variant is run only for synchrony and entropy, and no kept or excluded counts are printed for it. The Summary's \"with means a little off under the Methods' rate\" also covers this claim, which is about counts, not means: 144 excluded against 203. Whether the claim should be judged under the gist's rate is pending with a reader; until it is answered the partial outcome stands.",
 "A start_time section in the main notebook now prints the sample under A1F1 with times from start_time (734 kept, 131 excluded, median 37, 8 to 96), and the deviation says what it shows. The Summary now names the excluded count (144 against 203) as well as the means. The gap in the criterion is noted in the outcome's notes and added to questions/burman-2023.yaml for a reader; the claim is unchanged. Outcome unchanged.")
for c in ('fig4d-synchrony-lower-awake','fig4d-entropy-higher-awake'):
    R[c]=("Partially reproduced under A1F1, with the A1F2 exact match recorded as a deviation. Whether the claim should be judged under the gist's rate is pending with a reader; until it is answered the partial outcome stands.",
     "The start_time deviation now says what the variant run shows under A1F1 (kept and excluded counts, and that every measure keeps its direction). Outcome unchanged.")
R['fig4-rate-higher-awake']=("Reproduced. The deviation says timing from start_time \"is shown as a variant and keeps the direction\", but the start_time variant is run only for synchrony and entropy; no rate test is printed for it.",
 "The start_time section now prints the paired rate test under A1F1 with times from start_time (14.9 against 8.14 Hz, p = 9.58e-35), and the deviation says what it shows. Outcome unchanged.")
R['figs6-rate-regressed']=("Reproduced. The deviation says timing from start_time \"is shown as a variant and keeps the direction\", but no regression is printed for start_time. The Figure S6 legend is still unavailable; the outcome does not depend on it, since every reading agrees.",
 "The start_time section now prints R1, R2 and R3 under A1F1 with times from start_time; synchrony stays lower and entropy higher awake, all p below 1e-11. Outcome unchanged.")
R['fig4f-model-hyperpolarizing-less-activity']=("Reproduced. The README's \"about 20 minutes\" for the model notebook does not match: model cell 6 prints \"20 runs in 40.6 min\", and cell 19 prints a total run time of 43.0 min.",
 "The README now gives about 20 minutes (19.9 in this execution) and 43 minutes on a slower runner, and entry.yaml gives 20. Outcome unchanged.")
for c,miss in (('fig4h-model-synchrony','0.0011'),('fig4h-model-entropy','0.0024')):
    R[c]=("Partially reproduced. The README's \"hyperpolarizing means 0.001 to 0.002 outside tolerances\" does not match model cells 11 and 14, which give misses of 0.0011 and 0.0024. Whether the fig4h tolerances should allow for differences between seeds is pending with a reader; until it is answered the two partial model outcomes stand.",
     "The README now gives the misses as 0.0011 and 0.0024. Outcome unchanged.")
R['figs7-model-decoding']=("Reproduced, and this holds even with the corrected statistic. Model cell 20 and the attempt notes say \"D1 paired t = 16.42, p = 1.11e-12\", but model cell 19 prints t = 16.92, p = 6.52e-13, which the printed per-run accuracies give; 16.42 matches the earlier run, not this one. So the accuracies differ between executions, though the cross-validation is seeded and the other model numbers repeat exactly, which does not fit the deviation's implication that the seeding makes the run deterministic. The reason should be explained, or the deviation's wording changed.",
 "The cause is ties. The classifier's inputs are small integer spike counts, and in 0.80 to 0.92 of the test trials the fifth-nearest training trial is as near as the sixth, so the five neighbours depend on how ties are broken, which differs between runners (a full run of seed 1 on this runner gives 0.9840 and 0.9424 from the same spikes that gave 0.9820 and 0.9437 in the execution reviewed). Executions on different runners printed t = 16.92 and t = 16.42; this one printed t = 16.42, p = 1.11e-12, which cell 20 and the notes now give, with the other value named. network.decoding_ties now gives the share of tied trials and the accuracy under five other training orders; D1 gives t = 16.35 to 17.22 and D2 holds in 20 of 20 runs each time. The deviation now says that the seeds fix the spikes and folds but not the tie-breaking. Outcome unchanged.")
R['figs4-intrinsic-properties']=("Blocked, methods_underspecified. The legends of Figures S4, S6 and S7 are still unavailable; the block on figs4 depends on them.",
 "No change.")
results=[]
for o in rec['outcomes']:
    c=o['claim']
    reason,resp=R.get(c,(PC,"No change."))
    results.append(dict(claim=c, agrees=True, outcome=o['outcome'], reason=reason, response=resp))
assert len(results)==35
rnd=dict(date='2026-11-10', kind='agent',
  by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)',
  reviewed=('Round 2: the full executed notebooks of the round-1 revision as re-executed in the author-answers run (reproduce_burman_2023.ipynb and network_model.ipynb, with conclusions and summaries), the helper modules npx.py and network.py, the claims file, the attempt record and the README, with the paper\'s full text. It could not see questions/burman-2023.yaml.'),
  results=results)
txt=yaml.safe_dump([rnd], sort_keys=False, width=104, allow_unicode=True)
open(p,'a').write(txt)
yaml.safe_load(open(p))
E
tail -30 attempts/burman-2023-01.yaml | head -20
```

```
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
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
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 82, in compose_node
    node = self.compose_sequence_node(anchor)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 111, in compose_sequence_node
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/is run as a variant under A1F1: 734 units kept/is run as a variant under A1F1, with 734 units kept/' attempts/burman-2023-01.yaml; grep -c "with 734 units kept" attempts/burman-2023-01.yaml; python -c "import yaml;yaml.safe_load(open('attempts/burman-2023-01.yaml'))" && echo ok; grep -n ": .*: " attempts/burman-2023-01.yaml | grep -v "^ *[0-9]*: *- \|'" | head
```

```
5
ok
```

**Agent**

Now re-run the append script (saved earlier only in the heredoc, so I'll repeat it).

**Agent calls Bash**

```bash
cd  sed -n 74,82p attempts/burman-2023-01.yaml
```

```
under the gist's rate (A1F2, A2F2), which sums spike latencies where a count is expected; this claim
    holds fully only under that variant.
  - Trials of all stimulus currents and depths of a session are pooled and times are taken from stop_time,
    as the claims file (N3) gives from the gist; the Methods say only "following an electrical stimulus".
    Timing from start_time, the pulse onset 0.4 ms earlier, is run as a variant under A1F1, with 734 units kept
    and 131 excluded, and synchrony, entropy, the rate test and the regressions keep their direction.
  - The Methods' waveform cut (>= 0.4 ms) and the gist's (> 0.4 ms) select the same units, as no unit
    has a duration of exactly 0.4 ms; readings A1 and A2 also select the same 865 units, as the SSp sessions
    hold only SSp-ll and SSp-tr units.
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/burman-2023-01.yaml'; s=open(p).read()
old="""    Timing from start_time, the pulse onset 0.4 ms earlier, is run as a variant under A1F1, with 734 units kept
    and 131 excluded, and synchrony, entropy, the rate test and the regressions keep their direction.
"""
new="""    Timing from start_time, the pulse onset 0.4 ms earlier, is run as a variant under A1F1, with 734
    units kept and 131 excluded, and synchrony, entropy, the rate test and the regressions keep their
    direction.
"""
assert s.count(old)==5; open(p,'w').write(s.replace(old,new))
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
p='attempts/burman-2023-01.yaml'
rec=yaml.safe_load(open(p))
PC="Agrees with all 35 outcomes; the 24 patch-clamp claims are blocked, data_missing."
R={}
R['dataset-sessions-link']=("Reproduced. The Summary of the main notebook (cell 37) overstates the clocks: \"their labels and clocks pass the checks above\" is too strong, as main cell 8 passes 33 of 34 pairs and sub-569069 awake fails (ratio 1.07, p = 0.591); main cell 9 and the attempt notes state this correctly. The README's \"About two minutes\" for the main notebook does not match: cell 4 took 196 s to load, and cell 35 prints 3.5 min.",
 "The Summary now says the clocks pass in 33 of 34 file and condition pairs and names sub-569069 awake, with its ratio and p. The README now gives 2.5 to 3.5 minutes (2.5 in this execution, 3.5 in the one reviewed). Outcome unchanged.")
R['fig4c-sample']=("Partially reproduced under A1F1, with the A1F2 exact match recorded as a deviation. A small gap in the claims file: A1F1 keeps 721, inside 662 +- 66.2, and excludes 144, outside 203 +- 20.3; the criterion's partial case, \"only the total (865) is within 10%\", does not literally cover this, as the kept count is within tolerance too, but partial is still the sensible reading. The deviation says timing from start_time \"is shown as a variant and keeps the direction\", but the start_time variant is run only for synchrony and entropy, and no kept or excluded counts are printed for it. The Summary's \"with means a little off under the Methods' rate\" also covers this claim, which is about counts, not means: 144 excluded against 203. Whether the claim should be judged under the gist's rate is pending with a reader; until it is answered the partial outcome stands.",
 "A start_time section in the main notebook now prints the sample under A1F1 with times from start_time (734 kept, 131 excluded, median 37, 8 to 96), and the deviation says what it shows. The Summary now names the excluded count (144 against 203) as well as the means. The gap in the criterion is noted in the outcome's notes and added to questions/burman-2023.yaml for a reader; the claim is unchanged. Outcome unchanged.")
for c in ('fig4d-synchrony-lower-awake','fig4d-entropy-higher-awake'):
    R[c]=("Partially reproduced under A1F1, with the A1F2 exact match recorded as a deviation. Whether the claim should be judged under the gist's rate is pending with a reader; until it is answered the partial outcome stands.",
     "The start_time deviation now says what the variant run shows under A1F1 (kept and excluded counts, and that every measure keeps its direction). Outcome unchanged.")
R['fig4-rate-higher-awake']=("Reproduced. The deviation says timing from start_time \"is shown as a variant and keeps the direction\", but the start_time variant is run only for synchrony and entropy; no rate test is printed for it.",
 "The start_time section now prints the paired rate test under A1F1 with times from start_time (14.9 against 8.14 Hz, p = 9.58e-35), and the deviation says what it shows. Outcome unchanged.")
R['figs6-rate-regressed']=("Reproduced. The deviation says timing from start_time \"is shown as a variant and keeps the direction\", but no regression is printed for start_time. The Figure S6 legend is still unavailable; the outcome does not depend on it, since every reading agrees.",
 "The start_time section now prints R1, R2 and R3 under A1F1 with times from start_time; synchrony stays lower and entropy higher awake, all p below 1e-11. Outcome unchanged.")
R['fig4f-model-hyperpolarizing-less-activity']=("Reproduced. The README's \"about 20 minutes\" for the model notebook does not match: model cell 6 prints \"20 runs in 40.6 min\", and cell 19 prints a total run time of 43.0 min.",
 "The README now gives about 20 minutes (19.9 in this execution) and 43 minutes on a slower runner, and entry.yaml gives 20. Outcome unchanged.")
for c in ('fig4h-model-synchrony','fig4h-model-entropy'):
    R[c]=("Partially reproduced. The README's \"hyperpolarizing means 0.001 to 0.002 outside tolerances\" does not match model cells 11 and 14, which give misses of 0.0011 and 0.0024. Whether the fig4h tolerances should allow for differences between seeds is pending with a reader; until it is answered the two partial model outcomes stand.",
     "The README now gives the misses as 0.0011 and 0.0024. Outcome unchanged.")
R['figs7-model-decoding']=("Reproduced, and this holds even with the corrected statistic. Model cell 20 and the attempt notes say \"D1 paired t = 16.42, p = 1.11e-12\", but model cell 19 prints t = 16.92, p = 6.52e-13, which the printed per-run accuracies give; 16.42 matches the earlier run, not this one. So the accuracies differ between executions, though the cross-validation is seeded and the other model numbers repeat exactly, which does not fit the deviation's implication that the seeding makes the run deterministic. The reason should be explained, or the deviation's wording changed.",
 "The cause is ties. The classifier's inputs are small integer spike counts, and in 0.80 to 0.92 of the test trials the fifth-nearest training trial is as near as the sixth, so the five neighbours depend on how ties are broken, which differs between runners (a full run of seed 1 on this runner gives 0.9840 and 0.9424 from the same spikes that gave 0.9820 and 0.9437 in the execution reviewed). Executions on different runners printed t = 16.92 and t = 16.42; this one printed t = 16.42, p = 1.11e-12, which cell 20 and the notes now give, with the other value named. network.decoding_ties now gives the share of tied trials and the accuracy under five other training orders; D1 gives t = 16.35 to 17.22 and D2 holds in 20 of 20 runs each time. The deviation now says that the seeds fix the spikes and folds but not the tie-breaking. Outcome unchanged.")
R['figs4-intrinsic-properties']=("Blocked, methods_underspecified. The legends of Figures S4, S6 and S7 are still unavailable; the block on figs4 depends on them.", "No change.")
results=[]
for o in rec['outcomes']:
    reason,resp=R.get(o['claim'],(PC,"No change."))
    results.append(dict(claim=o['claim'], agrees=True, outcome=o['outcome'], reason=reason, response=resp))
assert len(results)==35 and set(R)<=set(o['claim'] for o in rec['outcomes'])
rnd=dict(date='2026-11-10', kind='agent',
  by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)',
  reviewed=("Round 2: the full executed notebooks of the round-1 revision as re-executed in the author-answers run (reproduce_burman_2023.ipynb and network_model.ipynb, with conclusions and summaries), the helper modules npx.py and network.py, the claims file, the attempt record and the README, with the paper's full text. It could not see questions/burman-2023.yaml."),
  results=results)
open(p,'a').write(yaml.safe_dump([rnd], sort_keys=False, width=104, allow_unicode=True))
r=yaml.safe_load(open(p)); print(len(r['verifications']))
E
python tools/entry.py check entries/burman-2023 2>&1 | grep -v MissingID | tail -5
```

```
2
0 error(s)
```

**Agent calls Bash**

```bash
cd transcripts/burman-2023; sed -n 185,196p author-answers.md | cut -c1-300; grep -n "executed\|handover" verifier-2.md | head -8 | cut -c1-200
```

````
```

```
network_model.ipynb **Result: partially reproduced.** Over the 16,000 pooled neurons synchrony is lower with shunting E_GABA, 0.7833 against 0.8789 (paired t = -134.60; p underflows to 0, below 0.001), and lower in all 20 runs. The shunting mean is within 0.784 +- 0.001; the hyperpolarizing mean is 

network_model.ipynb **Result: partially reproduced.** Entropy is higher with shunting E_GABA, 0.4516 against 0.2014 nats (paired t = 93.09; p underflows to 0, below 0.001), and higher in all 20 runs. The shunting mean is within 0.451 +- 0.002; the hyperpolarizing mean is 0.0024 above the upper bound

network_model.ipynb **Result: reproduced.** The peri-stimulus rate is lower with hyperpolarizing E_GABA, 8.785 against 19.468 Hz over 16,000 neurons (paired t = 446.42, p below 0.05), and lower in all 20 runs; over whole conditions the hyperpolarizing network fires 0.431 to 0.445 times the spikes of

network_model.ipynb **Result: reproduced.** Decoding accuracy is higher with shunting E_GABA, 0.9848 against 0.9315 on average (chance 0.01); D1 paired t = 16.92, p = 6.52e-13, and D2 holds, shunting higher in 20 of 20 runs. 

reproduce_burman_2023.ipynb **Result: reproduced.** All 17 files are in version 0.230317.0039, each with the units fields (spike_times read through its index, location, waveform_duration) and the trial fields the code uses, and with awake and isoflurane electrical trials. 
388:The claims file has 35 claims and the attempt record has 35 outcomes: 5 reproduced, 5 partially_reproduced and 25 blocked (24 data_missing, 1 methods_underspecified). Below, "main" means `reproduc
````

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/burman-2023-01.yaml'; s=open(p).read()
import re
i=s.index("reviewed: 'Round 2"); j=s.index("\n  results:", i)
old=s[i:j]; print(old)
new="reviewed: Round 2, the full executed notebooks after the round-1 revision (reproduce_burman_2023.ipynb\n    and network_model.ipynb, with conclusions and summaries), the helper modules npx.py and network.py,\n    the claims file, the attempt record and the README, with the paper's full text. It could not see\n    questions/burman-2023.yaml."
s=s[:i]+new+s[j:]; open(p,'w').write(s)
import yaml; yaml.safe_load(open(p))
E
tail -c 1 attempts/burman-2023-01.yaml | od -c | head -1
```

```
reviewed: 'Round 2: the full executed notebooks of the round-1 revision as re-executed in the author-answers
    run (reproduce_burman_2023.ipynb and network_model.ipynb, with conclusions and summaries), the helper
    modules npx.py and network.py, the claims file, the attempt record and the README, with the paper''s full
    text. It could not see questions/burman-2023.yaml.'
0000000  \n
```

**Agent calls Bash**

```bash
cd  git diff | grep "^+" | grep -n "—\|rather" ; date -u; python tools/entry.py all entries/burman-2023 2>&1 | grep -v MissingID | tail -5; date -u
```

```
Tue Nov 10 11:36:51 UTC 2026
Installed kernelspec registry-burman-2023 in executed/burman-2023/.venv/share/jupyter/kernels/registry-burman-2023
0 error(s)
pass  reproduce_burman_2023.ipynb  (152 s)
pass  network_model.ipynb  (1028 s)
Tue Nov 10 11:56:41 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
for nb,idx in (('executed/burman-2023/network_model.ipynb',[6,10,13,16,19]),('executed/burman-2023/reproduce_burman_2023.ipynb',[8,13,19,23,24,28,31,34,35,38])):
    d=json.load(open(nb))
    for i in idx:
        c=d['cells'][i]
        out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]) if o.get('output_type')=='stream')
        keep=[l for l in out.splitlines() if any(k in l for k in ('min','SE','paired','D1','D2','tied','range','order','mean accuracy','33 of','kept','A1F1 ','start_time','evoked rate','synchrony ','entropy ','units with','recordings with','holds','expected direction'))]
        print(f'=== {nb[19:27]} [{i}]'); print('\n'.join(keep[:20]))
E
```

```
=== 3/networ [6]
20 runs in 17.0 min (4 processes); peak memory of this process 0.41 GB, of a child 2.05 GB
    seed        condition  E_GABA  spikes_in_condition  neurons_with_spikes  rate_mean  entropy_mean  synchrony_mean  accuracy  tied_share
=== 3/networ [10]
  shunting 0.7833 +- 0.0005 (SEM), hyperpolarizing 0.8789 +- 0.0006
  paired t test t = -134.60, p = 0.00e+00
  range shunting 0.432 to 0.898, hyperpolarizing 0.283 to 0.974
runs with lower mean synchrony under shunting: 20 of 20; per-run means shunting 0.7782 to 0.7882, hyperpolarizing 0.8661 to 0.8909
shunting: run-to-run SE of the mean 0.0006; pooled mean 0.7833 is 1.3 SE from 0.784
hyperpolarizing: run-to-run SE of the mean 0.0013; pooled mean 0.8789 is 1.6 SE from 0.881
=== 3/networ [13]
entropy (nats): neurons 16000, defined in both conditions 16000 (dropped 0)
  shunting 0.4516 +- 0.0020 (SEM), hyperpolarizing 0.2014 +- 0.0019
  paired t test t = 93.09, p = 0.00e+00
  range shunting 0.000 to 1.462, hyperpolarizing 0.000 to 1.386
runs with higher mean entropy under shunting: 20 of 20; per-run means shunting 0.4409 to 0.4647, hyperpolarizing 0.1798 to 0.2217
shunting: run-to-run SE of the mean 0.0014; pooled mean 0.4516 is 0.4 SE from 0.451
hyperpolarizing: run-to-run SE of the mean 0.0023; pooled mean 0.2014 is 1.9 SE from 0.197
synchrony: plotted 1,000 of 16000 neurons, range 0.527 to 0.964, none outside the axes
entropy: plotted 1,000 of 16000 neurons, range 0.000 to 1.335, none outside the axes
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "20 minutes\|2.5 to 3.5" entries/burman-2023/README.md; sed -i 's/about 20 minutes on the last/about 17 minutes on the last/' entries/burman-2023/README.md; sed -i 's/  runtime_minutes: 20/  runtime_minutes: 17/' entries/burman-2023/entry.yaml; python - <<'E'
p='attempts/burman-2023-01.yaml'; s=open(p).read()
import re
n=s.count("19.9 in this execution"); print(n)
s=s.replace("The README now gives about 20 minutes (19.9 in this execution)","The README now gives about 17 minutes (17.0 in this execution)")
s=s.replace("and entry.yaml gives 20.","and entry.yaml gives 17.")
open(p,'w').write(s)
E
grep -n "17 minutes\|19.9\|gives 17" entries/burman-2023/README.md attempts/burman-2023-01.yaml
```

```
35:- `reproduce_burman_2023.ipynb`: the Neuropixels claims. About 2.5 to 3.5 minutes (2.5 on the last
37:- `network_model.ipynb`: 20 runs of the paper's network model on four processes, about 20 minutes on the last
1
entries/burman-2023/README.md:37:- `network_model.ipynb`: 20 runs of the paper's network model on four processes, about 17 minutes on the last
attempts/burman-2023-01.yaml:814:    response: The README now gives about 17 minutes (17.0 in this execution) and 43 minutes on a slower runner,
attempts/burman-2023-01.yaml:815:      and entry.yaml gives 17. Outcome unchanged.
```

**Agent calls Bash**

```bash
cd  grep -n "16\.\|decod" entries/burman-2023/README.md; python tools/entry.py check entries/burman-2023 2>&1 | grep -v MissingID | tail -2; git status --short | grep -v "^??"; git diff | grep "^+" | grep -c "—\| rather"
```

```
21:| Model: shunting networks decoded more accurately | Reproduced |
0 error(s)
 M attempts/burman-2023-01.yaml
 M entries/burman-2023/README.md
 M entries/burman-2023/entry.yaml
 M entries/burman-2023/network.py
 M entries/burman-2023/network_model.ipynb
 M entries/burman-2023/reproduce_burman_2023.ipynb
 M questions/burman-2023.yaml
0
```

**Agent calls Bash**

```bash
cd  python -c "
import json
for p in ('entries/burman-2023/reproduce_burman_2023.ipynb','entries/burman-2023/network_model.ipynb'):
    nb=json.load(open(p)); print(p, sum(len(c.get('outputs',[])) for c in nb['cells']))
"; python tools/entry.py handover entries/burman-2023 2>&1 | tail -1; date -u
```

```
entries/burman-2023/reproduce_burman_2023.ipynb 0
entries/burman-2023/network_model.ipynb 0
wrote executed/burman-2023/handover
Tue Nov 10 11:57:17 UTC 2026
```

**Agent**

I went through every point in the round-2 report. None of the 35 outcomes changed and none is marked `proposed`: 5 reproduced, 5 partially reproduced, 25 blocked. The entry was re-run twice with `python tools/entry.py all entries/burman-2023`; the final run had 0 check errors and both notebooks passed (main 152 s, model 1028 s). Every conclusion matches that run's numbers. Nothing is committed.

**Why the decoding statistic changes between runs (figs7):**
- **Cause:** ties among nearest neighbours. The classifier's inputs are small whole-number spike counts. In 80 to 92% of test trials, the fifth-nearest training trial is exactly as close as the sixth, so which five neighbours count depends on how the tie is broken. That differs between runner machines; the random seeds don't control it.
- **Evidence:** a full run of seed 1 here gave accuracies 0.9840 and 0.9424. The run the verifier read gave 0.9820 and 0.9437, with the same synchrony (0.8909). Executions on different runners have printed t = 16.92 or t = 16.42.
- **New check:** `network.decoding_ties` reports the share of tied trials and redoes the decoding with five other orders of the training trials, which break the ties differently. The paired t ranges from 16.35 to 17.22 (p at most 1.20e-12), and shunting is higher in 20 of 20 runs every time. The conclusion doesn't depend on how ties are broken.
- **Text:** this run printed t = 16.42, p = 1.11e-12. The result cell and notes now give that value and name the other one. The seeding deviation no longer implies the run is deterministic.

**Other corrections:**
- **Start-time variant:** a new section in the main notebook now actually prints the sample count (734 kept, 131 excluded), the rate test (14.9 against 8.14 Hz, p = 9.58e-35) and the three regressions (all p below 1e-11). The five deviations now say what it shows.
- **Main notebook summary:**
  - Clocks: it now says they pass in 33 of 34 pairs, and names sub-569069 awake (1.07 times, p = 0.591).
  - Counts: it now names the excluded count (144 against 203) alongside the means.
- **README:** tolerance misses corrected to 0.0011 and 0.0024. Run times now 2.5 to 3.5 min for the main notebook and 17 to 43 min for the model, depending on the runner; `entry.yaml` now says 17.
- **Question for a reader:** I added the verifier's criterion gap for fig4c-sample to `questions/burman-2023.yaml`. The kept count is within tolerance and the excluded count is not, a case the criterion's partial clause doesn't name. The claim itself is unchanged.
- **Record:** round 2 is recorded under `verifications` with all 35 claims agreed, the verifier's reasons quoted or closely paraphrased, and my responses.

**Not done:**
- The two questions from round 1 (whether to judge the Neuropixels claims under the gist's rate, and whether the model tolerances should allow for differences between seeds) are still waiting for a reader. The outcomes stay as tested until they are answered.
- The legends of Figures S4, S6 and S7 are still unavailable, so figs4 stays blocked.
- The schema only allows per-claim entries, so the README run-time point is recorded under dataset-sessions-link (main notebook) and fig4f-model-hyperpolarizing-less-activity (model notebook).

## End of run

64 turns, 54 minutes, $2.68 at API prices, result: success.
