# cambrainha-2025 · author-revise-1 · run 45981609398

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/cambrainha-2025/verifier-1-report.md; ls entries/cambrainha-2025 entries/cambrainha-2025/*
```

```
Fri Nov 27 10:28:59 UTC 2026
**Verification report, round 1: Cambrainha et al. 2025 on DANDI:000713 (0.240702.1725)**

The claims file has 18 claims. My outcomes: 3 reproduced, 2 partially reproduced, 12 not reproduced, 1 blocked. I disagree with the notebook on four of the five claims it treats as blocked (fig3c-scaling-hit-rate-higher, fig3c-hit-rate-rises-with-threshold, fig4a-active-most-scaling, figs8-halves-and-phase-order).

The main uncertainty is the surrogate chance level. The paper says the lowest surrogate kurtoses are around 6. The notebook gets a minimum of 2.80 and a 5th percentile of 3.16 (cell 17). My synthetic test of the helper gives 3.1–3.5 for independent Poisson units, so the kurtosis step as coded here may not match the paper's.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| sessions-selected | not_reproduced | All V1 units: 97 sessions and 68 mice with > 128 units (98 with ≥ 128). Default quality filters: 1 session (cell 15). The paper has 62 sessions and 44 mice; no reading of the criterion lands within tolerance. I confirmed 153 session files from 81 subjects on the DANDI API. |
| fig3a-kurtosis-broader-than-surrogate | partially_reproduced | The real windows spread more than the surrogates (IQR 1.98 vs 0.64), and some exceed κ_surr_max (real maximum 89.8 vs 34.3). The lowest surrogate kurtoses are 2.80 (minimum) and 3.16 (5th percentile), against 6 ± 0.6. That matches the criterion's partial clause. The "majority above κ_surr_max" condition fails (0.000), cell 17. |
| fig3c-scaling-hit-rate-higher | not_reproduced (notebook: blocked) | Under the adopted CV reading (a), the scaling hit rate is below the no-scaling hit rate at all 236 thresholds from 3 to 15 (e.g. κ=7: 0.615 vs 0.655; κ=12: 0.591 vs 0.642), cell 19. So any κ_surr_max up to 12.5, including the paper's ≈7, fails the test. The grid is empty only because of a few outlier surrogate windows. Only CV reading (b), which drops 83% of windows, passes. |
| fig3c-hit-rat
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
779 docs/protocol.md
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
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,370p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

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
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 370,640p docs/protocol.md
```

```
### 2. Check the data against its description

Descriptive metadata is often wrong. For every quantity the analysis uses,
check the description against the values: units and ranges, sampling rates,
counts of subjects, sessions, trials and cells, the size of an arena, which
conditions exist. Show that every data stream shares the clock of the trial
tables, using a contrast between conditions where an overall check cannot
tell a response from an offset (with spikes and a trial table only, decoding
a task variable in windows around the trial start does this; for continuous
sessions, decoding the annotations with the labels shifted in time), and name any
session where this could not be established. A description that a check
supports but does not prove is reported as consistent with the data, not as
shown. Where they disagree, trust the data, say so in the notebook,
and record it as a finding.

### 3. Write the entry

An entry is a directory `entries/<paper>/` holding
`entry.yaml`, `requirements.in`, one or more notebooks, and usually a helper
module.
[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep camb; wc -l attempts/cambrainha-2025-01.yaml claims/cambrainha-2025.yaml entries/cambrainha-2025/criticality.py; ls questions | grep camb; ls executed/cambrainha-2025 2>/dev/null; cat entries/cambrainha-2025/entry.yaml
```

```
cambrainha-2025-01.yaml
  362 attempts/cambrainha-2025-01.yaml
  501 claims/cambrainha-2025.yaml
  703 entries/cambrainha-2025/criticality.py
 1566 total
reproduce_cambrainha_2025.ipynb
result.json
schema_version: 1
name: cambrainha-2025
type: reproduction
title: Kurtosis of coarse-grained V1 activity and task performance (Cambrainha et al. 2025)
description: Tests the findings of Cambrainha, Castro, de Vasconcelos, Carelli and Copelli (2025)
  on dandiset 000713, the Allen Institute Visual Behavior Neuropixels data. It computes, per 30-s
  window of V1 spiking, the kurtosis after momentum-space coarse graining and its ISI-shuffled
  surrogate, relates it to the hit rate of the change-detection task, compares the active,
  passive and non-natural image phases, and fits the real-space renormalization exponents.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_cambrainha_2025.ipynb
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/cambrainha-2025-01.yaml
```

```
schema_version: 3
id: cambrainha-2025-01
datasets:
- archive: dandi
  id: "000713"
  version: 0.240702.1725
  doi: 10.48324/dandi.000713/0.240702.1725
  relation: primary
paper: doi:10.1103/w49n-2vz8
date: 2026-11-27
entry: cambrainha-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-18
  runner:
[... 342 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python -c "
import json;nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print(i,c['cell_type'],c.get('metadata',{}).get('tags'),len(s.splitlines()),repr(s[:120]))
"; cat ../../executed/cambrainha-2025/result.json | head -50
```

```
0 markdown None 30 '# Reproducing Cambrainha et al. (2025) from dandiset 000713\n\nPaper. Cambrainha, Castro, de Vasconcelos, Carelli & Copell'
1 code None 30 'import os\nos.environ.setdefault("OMP_NUM_THREADS", "1")\nos.environ.setdefault("OPENBLAS_NUM_THREADS", "1")\nos.environ.se'
2 markdown None 3 '## Survey of the dataset\n\nEvery session file is opened and its units, electrodes and trials tables are read (metadata an'
3 code None 13 'assets = cr.session_assets()\nwith ThreadPoolExecutor(12) as ex:\n    survey = pd.DataFrame(list(ex.map(cr.survey, assets)'
4 markdown None 5 '## Processing every session\n\nAll sessions with at least 128 V1 units (reading (a) of O1, counting both > 128 and >= 128)'
5 code None 12 'proc = survey[survey.visp_all >= cr.MIN_UNITS].reset_index(drop=True)\nasset_of = {a["path"]: a for a in assets}\nstrict_o'
6 markdown None 1 '## Data check'
7 code ['sanity'] 74 'ok = [r for r in results if "error" not in r]\nsessions_ok = ok\nW_all = cr.window_table(ok)\nsel_gt = set(proc.path[proc.v'
8 markdown None 6 'The checks above show:\n\n- 153 session files from 81 mice, no session deposited twice (identifiers unique, and no two ses'
9 markdown None 3 '## Common definitions\n\nThe analysis set is the sessions with more than 128 V1 units (O1 (a)). Readings named in the clai'
10 code None 50 'W = W_all[(W_all.units == "all") & W_all.path.isin(sel_gt)].copy()\nmouse_of = dict(zip(survey.path, survey.subject))\nW["'
11 markdown None 8 '## How readings decide\n\nThe claims file lists readings of details the paper leaves open (O1 to O11). Following the proto'
12 markdown None 1 'The two poolings of O3 give the same number: psi is normalised to unit variance for every unit (Eq. 5), so the pooled <p'
13 code None 3 'd = W[W.length == 30]\nprint("largest |kappa_a - kappa_b| over windows:", float(np.abs(d.kappa_a - d.kappa_b).max()),\n   '
14 markdown None 5 "## sessions-selected\n\n> Of the dataset's sessions, 62 (from 44 mice) have more than 128 recor
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
ls ../../paper/; grep -n "def " criticality.py | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,78p criticality.py; sed -n 150,300p criticality.py
```

```
"""Loading and measures for Cambrainha et al. (2025) on dandiset 000713.

Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), "Criticality at Work: Scaling in
the Mouse Cortex Enhances Performance", PRX Life, doi:10.1103/w49n-2vz8. Claims in
claims/cambrainha-2025.yaml; the codes M1 to M8 and O1 to O11 below refer to the method notes
at the top of that file.

Dandiset 000713 (Allen Institute, Visual Behavior Neuropixels) holds one NWB file per session
(153 sessions, 81 mice) with the sorted units of all probes (`units`, with the peak channel of
each unit and the channel's brain structure in `electrodes/location`), the stimulus
presentations by block (`intervals/*_presentations`, column `stimulus_block`) and the task
trials (`intervals/trials`). LFP is in separate probe files, which are not read. Files are
streamed from the archive at the pinned version with remfile and h5py (pynwb is slow to open
these files over the network and adds nothing here); nothing is written to disk. Only the
spike times of V1 (VISp) units are read.

Where the parameters come from:

- `BIN_S` 50 ms, `WIN_S` 30 s, `CV_MAX` 5 (M1, Appendix 1); `NCUT_DIV` 16, the kurtosis at
  Ncutoff = N/16 (M3, Appendix 3); `KAPPA = <psi^4>/<psi^2>^2` (Appendix 3).
[... 209 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../../paper; grep -n -i "kurtosis\|covariance\|eigen\|surrogate\|normaliz\|three to five\|CV" 10.1103-w49n-2vz8.txt | head -120
```

```
23:performance remains unexplored. Here, we use a phenomenological renormalization group approach
47:Recently, a novel phenomenological renormalization
50:complex systems. Inspired by the renormalization group
72:Performance increases with kurtosis
77:Appendix). For each window, we calculated the covariance matrix Cij comprising all pairs of recorded neurons.
78:By diagonalizing this matrix, we obtained a set of eigenvectors from which projectors were created. When projecting the activity of each neuron over all eigenvectors,
82:eigenvalues for projection, we generated an increasingly
86:normalized distribution of this activity as we chose fewer
87:covariance eigenvectors. This procedure creates a flow
111:N covariance 
112:eigenvectors
118:FIG. 1. The phenomenological renormalization group applied to mouse brain data. (A) In the first part (Active) of the Allen
125:coarse-graining of a unit time series, corresponding to projections onto a decreasing number of eigenvectors of the covariance
126:matrix (N, N/2, N/4, . . .). The variance of the activity is normalized to 1.
129:point. For each window, we used the kurtosis κ of the
132:Certain time windows exhibit clear signatures of nontrivial dynamics, as expected at a critical point, with kurtosis values significantly higher than those in the spikeshuffled (surrogate) data.
134:show results similar to surrogate data [Fig. 2B]. Across
136:of kurtosis values, overlapping with the distribution from
137:the surrogate data [Fig. 3A]. As we depart from the Gaussian distribution, the distinction between windows with
139:this arbitrariness by establishing a kurtosis threshold κth:
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 395,465p 10.1103-w49n-2vz8.txt; sed -n 520,560p 10.1103-w49n-2vz8.txt
```

```
shown a second time in the same order as before, but
this time the lick apparatus is retracted. The raw electrophysiological data were preprocessed and sorted into
spike trains using the Kilosort2 algorithm [52]. We selected all 62 sessions from the dataset that had more
than 128 recorded units, which included both single-unit
activity (SUA) and multiunit activity (MUA). The data
were then divided into these three experimental phases,
binned into 50-ms intervals, and segmented into 30-s windows for analysis.
We excluded from the analysis temporal windows
based on the coefficient of variance (CV)
CV = σ
μ,
(1)
where μ and σ are the mean and the standard deviation
of the activity across the window. Windows where CV >
5 were excluded, as such high values are not typically
observed in awake mice and likely result from the chosen
window size, indicating artefacts.
2.
Surrogate data
Throughout our analysis, we compared our results with
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../entries/cambrainha-2025; sed -n 462,610p criticality.py
```

```
def analyse_window(spikes, t0, t1, rng_list, do_real_space=True, surr_real_space=True):
    """Everything computed on one window: counts, CVs, kurtosis, surrogates, real space."""
    nb = int(round((t1 - t0) / BIN_S))
    ws = window_spikes(spikes, t0, t1)
    X = bin_spikes(ws, t0, nb)
    active = X.sum(1) > 0
    Xa = X[active]
    rec = dict(t0=t0, t1=t1, n_units=int(len(spikes)), N=int(active.sum()),
               n_silent=int((~active).sum()), rate=float(X.mean()),
               spikes=int(X.sum()))
    rec["cv_a"], rec["cv_b"], rec["cv_c"] = cv_readings(X)
    rec["kappa_a"], rec["kappa_b"], rec["kappa0_a"], rec["kappa0_b"] = momentum_kurtosis(Xa)
    if do_real_space:
        rec["rs"] = real_space(Xa)
    wa = [s for s, a in zip(ws, active) if a]
    for si, rng in enumerate(rng_list):
        S = bin_spikes(isi_shuffle(wa, t0, t1, rng), t0, nb)
        S = S[S.sum(1) > 0]
        ka, kb, _, _ = momentum_kurtosis(S)
        rec[f"surr{si}_kappa_a"], rec[f"surr{si}_kappa_b"] = ka, kb
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/t; cat > $TMPDIR/t/z.py <<'EOF'
import time, numpy as np, sys
sys.path.insert(0,'.')
import criticality as cr
t=time.time()
assets=cr.session_assets()
import random
for a in assets[:6]:
    s=cr.survey(a)
    if s['visp_all']>=200: break
print(a['path'], s['visp_all'], time.time()-t)
d=cr.load_session(a); sp=d['spikes']; spans=cr.phase_spans(d['blocks'])
def mk(X, z):
    N=X.shape[0]; D=X-X.mean(1,keepdims=True)
    if z: D=D/D.std(1,keepdims=True)
    C=D@D.T/X.shape[1]; w,U=np.linalg.eigh(C); k=max(N//16,1); Uk=U[:,-k:]
    psi=Uk@(Uk.T@D); sd=psi.std(1,keepdims=True); psi=psi/sd
    p2=psi**2; return np.mean(p2**2)/np.mean(p2)**2
rng=np.random.default_rng(0)
out=[]
for (t0,t1) in cr.tile(spans['active'],30)[:40]:
    ws=cr.window_spikes(sp,t0,t1); X=cr.bin_spikes(ws,t0,600); act=X.sum(1)>0; Xa=X[act]
    wa=[s for s,q in zip(ws,act) if q]
    S=cr.bin_spikes(cr.isi_shuffle(wa,t0,t1,rng),t0,600); S=S[S.sum(1)>0]
    out.append((mk(Xa,0),mk(Xa,1),mk(S,0),mk(S,1)))
o=np.array(out); print("real cov, real corr, surr cov, surr corr")
print(np.percentile(o,[0,5,50,95,100],axis=0).round(2)); print(time.time()-t)
EOF
python $TMPDIR/t/z.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t/z.py", line 1, in <module>
    import time, numpy as np, sys
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls ../../.venv* ../../executed/cambrainha-2025 2>/dev/null; ls -a ../.. | head -30; grep -n "venv" ../../tools/entry.py | head
```

```
../../executed/cambrainha-2025:
reproduce_cambrainha_2025.ipynb
result.json
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
.gitconfig
.github
.gitignore
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 venv && uv pip install -q --python venv/bin/python -r entries/cambrainha-2025/requirements.lock.txt 2>&1 | tail -3; ls venv/bin | head
```

```
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
bids-validator-deno
bst
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025 && $TMPDIR/venv/bin/python $TMPDIR/t/z.py
```

```
sub-506940/sub-506940_ses-20200817T222149.nwb 231 6.1779625415802
real cov, real corr, surr cov, surr corr
[[ 3.67  9.5   3.2   9.12]
 [ 4.43 12.55  3.23 10.44]
 [ 5.67 27.28  3.52 20.79]
 [ 8.67 43.03  4.12 40.15]
 [ 9.68 57.28  4.76 55.78]]
10.940966606140137
```

**Agent calls Bash**

```bash
sed -n 1,140p ../../claims/cambrainha-2025.yaml
```

```
# Claims for Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), PRX Life,
# doi:10.1103/w49n-2vz8, "Criticality at Work: Scaling in the Mouse Cortex Enhances
# Performance", on dandiset 000713 (Allen Institute, Visual Behavior, Neuropixels).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.
#
# Text read. arXiv preprint 2410.23508 version 2 (15 Sep 2025), standing in for the PRX Life
# version of record, in paper/10.1103-w49n-2vz8.txt: main text, Appendix (Methods and
# Materials, sections 1 to 6), and the Supplemental Material (sections I to VIII and Figures
# S1 to S8). The PDF was opened to read Figures 3, 4, S1, S5, S7 and S8, whose axes the text
# garbles. Values read from figures are marked as such.
#
# Code read. None. The paper links no analysis code and no repository (the contributions
# statement says D.M.C. provided initial code and G.G.C. refined it, without a location).
#
# Data the paper used (Appendix 1, Figure 1A). The Allen Visual Behavior Neuropixels dataset
# (ref. 60, DANDI), which the dandiset's title names. Mice trained to lick on an image change.
# Each recording about 2 h 25 min, in three phases. Active: about 60 min of natural images in
# 250-ms flashes, a change-detection task with reward, lick port present. Non-natural images
# (NNI): Gabor patches for 15 min, full-field black and white flashes, and a gray screen for
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A28 "id: fig3c-scaling\|id: fig3c-hit-rate\|id: fig4a\|id: figs8\|id: figs3-" ../../claims/cambrainha-2025.yaml | grep -v "^--$" | head -170
```

```
151:- id: fig3c-scaling-hit-rate-higher
152-  statement: In the active phase, for any kurtosis threshold above the surrogate values, the
153-    hit rate pooled over scaling windows is higher than over no-scaling windows and higher
154-    than the trial-shuffled control.
155-  source: Results A, paragraph 3; Figure 3C
156-  quote: For any value of κth above surrogate values, the average hit rate was consistently higher
157-    when calculated over scaling windows than over no-scaling windows [Fig. 3C] ... we confirmed
158-    that the results were better than those obtained when hits and misses were shuffled within
159-    each session
160-  criterion: Hit rates as in M5 (Eqs. 11 and 12), trial shuffle as in M6 (500 repetitions), on
161-    active-phase windows with trials as in O5, at each kappa_th of the grid of O7 from
162-    kappa_surr_max (O6) to 12.5. Reproduced when, under one reading, the scaling hit rate
163-    exceeds both the no-scaling hit rate and the mean trial-shuffled hit rate at every grid
164-    point. Partially reproduced when it holds at 90% or more of grid points and every failure is
165-    within one bootstrap SE (O8) of the comparator. Not reproduced otherwise.
166-  depends_on:
167-  - fig3a-kurtosis-broader-than-surrogate
168:- id: fig3c-hit-rate-rises-with-threshold
169-  statement: As the threshold rises and only windows of higher kurtosis count as scaling, the hit
170-    rate over the scaling windows rises.
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 -c "
import json;nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i in [1,3,5,9,10,11,12]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
/bin/bash: line 1: cd: entries/cambrainha-2025: No such file or directory
===== 1
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
import time
import zlib
import itertools
import resource
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

import criticality as cr

PAPER = "cambrainha-2025"
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; sed -n 300,462p criticality.py; sed -n 610,703p criticality.py
```

```
used = np.zeros(n, bool)
    pairs = []
    target = n // 2
    for o in order:
        i, j = iu[o], ju[o]
        if not used[i] and not used[j]:
            used[i] = used[j] = True
            pairs.append((i, j))
            if len(pairs) == target:
                break
    return pairs


def _autocorr_tau(Y):
    """tau_c (s): where the cluster-averaged autocorrelation reaches 1/e (O9)."""
    Yc = Y - Y.mean(1, keepdims=True)
    var = (Yc ** 2).mean(1)
    ok = var > 0
    Yc, var = Yc[ok], var[ok]
    T = Y.shape[1]
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
p='criticality.py'; s=open(p).read()
old='''def momentum_kurtosis(X):
    """Kurtosis after momentum-space coarse graining (M3, Eqs. 2 to 5), and before (kappa_0).

    X holds the binned counts of the units active in the window. Returns
    (kappa_a, kappa_b, kappa0_a, kappa0_b) under the two poolings of O3.
    """
    N = X.shape[0]
    D = X - X.mean(1, keepdims=True)
    C = D @ D.T / X.shape[1]'''
new='''def momentum_kurtosis(X, zscore=False):
    """Kurtosis after momentum-space coarse graining (M3, Eqs. 2 to 5), and before (kappa_0).

    X holds the binned counts of the units active in the window. Returns
    (kappa_a, kappa_b, kappa0_a, kappa0_b) under the two poolings of O3. With `zscore`, each
    unit's counts are z-scored before Eq. 2, so that C is the correlation matrix (a variant the
    verifier asked for, as in some momentum-space analyses; Eq. 2 prints the covariance).
    """
    N = X.shape[0]
    D = X - X.mean(1, keepdims=True)
    if zscore:
        D = D / D.std(1, keepdims=True)
    C = D @ D.T / X.shape[1]'''
assert old in s; s=s.replace(old,new)
old='''    rec["kappa_a"], rec["kappa_b"], rec["kappa0_a"], rec["kappa0_b"] = momentum_kurtosis(Xa)
'''
new='''    rec["kappa_a"], rec["kappa_b"], rec["kappa0_a"], rec["kappa0_b"] = momentum_kurtosis(Xa)
    if rng_list:
        rec["kappa_z"] = momentum_kurtosis(Xa, zscore=True)[0]
'''
assert old in s; s=s.replace(old,new)
old='''        rec[f"surr{si}_kappa_a"], rec[f"surr{si}_kappa_b"] = ka, kb
'''
new='''        rec[f"surr{si}_kappa_a"], rec[f"surr{si}_kappa_b"] = ka, kb
        if si == 0:
            rec["surr0_kappa_z"] = momentum_kurtosis(S, zscore=True)[0]
'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n "auto_rewarded\|aborted\|catch" criticality.py
```

```
177:        trials = {k: tr[k][:] for k in ["start_time", "stop_time", "go", "catch", "aborted",
178:                                         "auto_rewarded", "hit", "miss",
588:    """Go trials with an outcome (O5): change trials that are hits or misses; catch and aborted
592:    go = t["go"].astype(bool) & ~t["aborted"].astype(bool) & (t["hit"].astype(bool)
594:    auto = t["auto_rewarded"].astype(bool) & ~t["aborted"].astype(bool)
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
p='criticality.py'; s=open(p).read()
old='''def trials_per_window('''
new='''def session_trials_counted(r, reading):
    """Trial-count variants for the trial density of Appendix 5 ("three to five trials" per
    30-s window), asked for by the verifier; not readings of O5. "go": O5 (a). "go+aborted":
    also aborted trials, as failures. "all": every trial (go, catch, aborted, auto-rewarded),
    a hit counting as success. Go trials are placed at their change time, the others at their
    start time. Returns (times, hit) arrays."""
    t = r["trials"]
    ab = t["aborted"].astype(bool)
    go = t["go"].astype(bool) & ~ab & (t["hit"].astype(bool) | t["miss"].astype(bool))
    hit = t["hit"].astype(bool)
    times = np.where(go, t["change_time_no_display_delay"], t["start_time"])
    if reading == "go":
        keep = go
    elif reading == "go+aborted":
        keep = go | ab
    else:
        keep = np.ones(len(hit), bool)
    return np.asarray(times)[keep], hit[keep].astype(int)


def trials_per_window('''
assert old in s; s=s.replace(old,new,1)
old='''    else:
        sp = rs["spectra"].get(64)
        if sp is not None:
            rank = np.arange(1, len(sp) + 1)
            pos = sp > 0
            s, r2 = _fit(np.log(rank[pos] / 64), np.log(sp[pos]))
            m = -s
    return dict('''
new='''    elif mu == "c":
        # variant asked for by the verifier: as (a), ranks 1 to K/2 only (upper half)
        xs, ys = [], []
        for k, sp in rs["spectra"].items():
            if k >= 16:
                rank = np.arange(1, len(sp) + 1)
                pos = (sp > 0) & (rank <= k // 2)
                xs.append(np.log(rank[pos] / k))
                ys.append(np.log(sp[pos]))
        if xs:
            s, r2 = _fit(np.concatenate(xs), np.concatenate(ys))
            m = -s
    else:
        # (b), and variant (d): as (b), ranks 1 to 32 only
        sp = rs["spectra"].get(64)
        if sp is not None:
            rank = np.arange(1, len(sp) + 1)
            pos = (sp > 0) & ((rank <= 32) if mu == "d" else True)
            s, r2 = _fit(np.log(rank[pos] / 64), np.log(sp[pos]))
            m = -s
    return dict('''
assert old in s; s=s.replace(old,new,1)
open(p,'w').write(s)
EOF
grep -n "mu (a) is one fit" criticality.py
```

```
53:  fitted). mu (a) is one fit of log lambda on log(rank/K) pooled over all K >= 16; (b) the
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
p='criticality.py'; s=open(p).read()
old='''  spectrum at K = 64, ranks 1 to 64. Windows with r^2 < 0.85 lose their mu (Appendix 4c).'''
new='''  spectrum at K = 64, ranks 1 to 64. Windows with r^2 < 0.85 lose their mu (Appendix 4c).
  Variants of mu asked for by the verifier, not readings of O9: (c) as (a) and (d) as (b), over
  ranks 1 to K/2 only, leaving out the noise floor of the spectrum.
- Correlation-matrix variant (asked for by the verifier): the kurtosis of M3 with each unit's
  counts z-scored before Eq. 2 (`kappa_z`, real windows and the claim-seed surrogate).'''
assert old in s; s=s.replace(old,new,1)
old='''            elif kr == "a":
                out["mu_b"], out["mu_r2_b"] = f["mu"], f["mu_r2"]
    return out'''
new='''            elif kr == "a":
                out["mu_b"], out["mu_r2_b"] = f["mu"], f["mu_r2"]
    for v in "cd":
        f = fit_exponents(rs, N, "a", "a", v)
        out[f"mu_{v}"], out[f"mu_r2_{v}"] = f["mu"], f["mu_r2"]
    return out'''
assert old in s; s=s.replace(old,new,1)
open(p,'w').write(s)
EOF
python3 -c "
import json;nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i in [7,18,21,22,25,28]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 7
ok = [r for r in results if "error" not in r]
sessions_ok = ok
W_all = cr.window_table(ok)
sel_gt = set(proc.path[proc.visp_all > cr.MIN_UNITS])
print("sessions processed:", len(ok), "; with > 128 V1 units (the analysis set):", len(sel_gt),
      "from", proc[proc.path.isin(sel_gt)].subject.nunique(), "mice")
print("V1 units per analysed session: min", proc[proc.path.isin(sel_gt)].visp_all.min(),
      "median", proc[proc.path.isin(sel_gt)].visp_all.median(),
      "max", proc[proc.path.isin(sel_gt)].visp_all.max())
print("spike times sorted within every unit:", all(r["spikes_sorted"] for r in ok))

# Stimulus blocks: names, order and durations
blk = []
for r in ok:
    for b, (name, s0, s1, n) in sorted(r["blocks"].items()):
        blk.append(dict(path=r["meta"]["path"], block=b, name=name.split("_presentations")[0],
                        start=s0, dur_min=(s1 - s0) / 60, n=n))
blk = pd.DataFrame(blk)
print("\nstimulus blocks (minutes), over sessions:")
[... 343 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 -c "
import json;nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i in [37,40,55,57,66,69]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 37


def ccdf(x, g):
    x = np.sort(x)
    return 1 - np.searchsorted(x, g, side="right") / len(x)


def order_eval(groups, g, strict_first=None):
    """Fractions above each threshold per group; the order holds where each group's fraction
    exceeds the next (>= for pairs listed in `strict_first`)."""
    F = {k: ccdf(v, g) for k, v in groups.items()}
    keys = list(groups)
    anyp = np.any([F[k] > 0 for k in keys], 0)
    ok = np.ones(len(g), bool)
    for a, b in zip(keys[:-1], keys[1:]):
        ok &= (F[a] >= F[b]) if strict_first and (a, b) in strict_first else (F[a] > F[b])
    return F, anyp, ok


[... 249 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; cat > $TMPDIR/t/dev.py <<'EOF'
"""dev harness: python dev.py prep | python dev.py run START END"""
import json, sys, pickle, os, time
os.chdir('entries/cambrainha-2025')
sys.path.insert(0, '.')
import matplotlib; matplotlib.use('Agg')
nb = json.load(open('reproduce_cambrainha_2025.ipynb'))
src = lambda i: ''.join(nb['cells'][i]['source'])
ns = {}
P = os.environ['TMPDIR'] + '/t/state.pkl'
if sys.argv[1] == 'prep':
    exec(src(1), ns); exec(src(3), ns)
    c5 = src(5).replace('.reset_index(drop=True)\n', '.iloc[::int(os.environ.get("EVERY","10"))].reset_index(drop=True)\n', 1)
    exec(c5, ns)
    pickle.dump({k: ns[k] for k in ['assets', 'survey', 'proc', 'results', 'asset_of', 'strict_of']}, open(P, 'wb'))
else:
    a, b = int(sys.argv[2]), int(sys.argv[3])
    exec(src(1), ns); ns.update(pickle.load(open(P, 'rb')))
    for i in range(6, b + 1):
        c = nb['cells'][i]
        if c['cell_type'] != 'code': continue
        if i < a and i not in (7, 10, 13) and i not in [int(x) for x in os.environ.get('ALSO', '').split(',') if x]: continue
        t = time.time()
        if i >= a: print(f'##### cell {i}')
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf if i < a else sys.stdout):
            exec(src(i), ns)
        if i >= a: print(f'##### cell {i} done {time.time()-t:.1f}s')
EOF
date -u; time EVERY=10 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py prep 2>&1 | tail -5
```

```
Exit code 143
Command timed out after 30m 0s
Fri Nov 27 10:32:53 UTC 2026
```

**Agent calls Bash**

```bash
date -u; cd entries/cambrainha-2025; timeout 600 $TMPDIR/venv/bin/python -c "
import time,sys; sys.path.insert(0,'.'); import criticality as cr
t=time.time(); a=cr.session_assets(); print(len(a), time.time()-t, flush=True)
s=cr.survey(a[0]); print(time.time()-t, flush=True)
r=cr.process_session(a[0],[0,1,2,3,4],[5,6,7,8,9],()); print(time.time()-t, len(r['windows']), flush=True)
"; date -u
```

```
Fri Nov 27 11:03:02 UTC 2026
153 2.18733811378479
3.915194511413574
38.05859684944153 750
Fri Nov 27 11:03:40 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/t/dev.py'; s=open(p).read()
s=s.replace("""    exec(src(1), ns); exec(src(3), ns)""","""    import concurrent.futures as cf, multiprocessing as mp, functools
    cf.ProcessPoolExecutor = functools.partial(cf.ProcessPoolExecutor, mp_context=mp.get_context('spawn'))
    exec(src(1), ns); exec(src(3), ns); print('survey done', flush=True)""")
open(p,'w').write(s)
EOF
date -u; time EVERY=10 timeout 900 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py prep 2>&1 | tail -5; date -u
```

```
Fri Nov 27 11:03:50 UTC 2026
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
concurrent.futures.process.BrokenProcessPool: A process in the process pool was terminated abruptly while the future was running or pending.

real	8m22.846s
user	0m58.956s
sys	0m6.109s
Fri Nov 27 11:12:13 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i in [3,5]:
  for o in nb['cells'][i].get('outputs',[]): print(o.get('text','')[:1500] if 'text' in o else o.keys())
"; free -g; nproc
```

```
['session files: 153  subjects: 81\n', "session types: {'EPHYS_1_images_G_3uL_reward': 74, 'EPHYS_1_images_H_3uL_reward': 71, 'EPHYS_1_images_G_5uL_reward': 4, 'EPHYS_1_images_H_5uL_reward': 4}\n", "structures with 'VIS' in their name: [np.str_('VIS'), np.str_('VISal'), np.str_('VISam'), np.str_('VISl'), np.str_('VISp'), np.str_('VISpm'), np.str_('VISrl'), np.str_('VISrll')]\n", 'duplicated session identifiers: 0 ; sessions sharing total spike count and unit count: 0\n', '       n_units  visp_all  visp_good  visp_default  visp_valid  n_trials\n', 'count    153.0     153.0      153.0         153.0       153.0     153.0\n', 'mean    2085.1     141.0      121.8          53.2       141.0     682.4\n', 'std      447.3      47.7       42.7          23.6        47.7     174.1\n', 'min     1103.0       0.0        0.0           0.0         0.0     429.0\n', '25%     1785.0     113.0       95.0          38.0       113.0     574.0\n', '50%     2024.0     144.0      125.0          50.0       144.0     631.0\n', '75%     2364.0     169.0      148.0          70.0       169.0     729.0\n', 'max     3388.0     294.0      268.0         132.0       294.0    1597.0\n']
['executed/cambrainha-2025/.venv/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice\n', '  return _methods._mean(a, axis=axis, dtype=dtype,\n']
['executed/cambrainha-2025/.venv/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide\n', '  ret = ret.dtype.type(ret / rcount)\n']
['processed 98 sessions in 22.3 min; failed: []\n', 'peak memory of a worker (GB): 1.19\n']
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           4          14
Swap:              2           0           2
4
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/t/dev.py'; s=open(p).read()
s=s.replace("""    import concurrent.futures as cf, multiprocessing as mp, functools
    cf.ProcessPoolExecutor = functools.partial(cf.ProcessPoolExecutor, mp_context=mp.get_context('spawn'))
""","""    import concurrent.futures as cf
    class Serial:
        def __init__(self, *a, **k): pass
        def __enter__(self): return self
        def __exit__(self, *a): pass
        def map(self, f, jobs): return [f(j) for j in jobs]
    cf.ProcessPoolExecutor = Serial
""")
open(p,'w').write(s)
EOF
date -u; time EVERY=16 timeout 900 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py prep 2>&1 | tail -5; date -u
```

```
Fri Nov 27 11:12:27 UTC 2026
75%     2364.0     169.0      148.0          70.0       169.0     729.0
max     3388.0     294.0      268.0         132.0       294.0    1597.0
survey done
processed 7 sessions in 4.0 min; failed: []
peak memory of a worker (GB): 0.17

real	8m44.716s
user	13m50.354s
sys	0m4.734s
Fri Nov 27 11:21:11 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; time $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 13 13 2>&1 | tail;
```

```
dandiset 000713 version 0.240702.1725
##### cell 13
largest |kappa_a - kappa_b| over windows: 1.4210854715202004e-14 ; surrogate: 2.1316282072803006e-14
##### cell 13 done 0.0s

real	0m1.324s
user	0m1.515s
sys	0m0.120s
```

**Agent calls Bash**

```bash
cd  sed -n 250,300p claims/cambrainha-2025.yaml
```

```
- id: fig4-exponents-active
  statement: In the active phase the real-space scaling exponents are alpha 1.41 +/- 0.05, beta
    0.77 +/- 0.04, mu 0.73 +/- 0.08 and z 0.3 +/- 0.1 (mean and SD across sessions).
  source: Results B, paragraph 3; Figures 4B to 4E
  quote: For the active phase, we obtained α1 = 1.41±0.05, β1 = 0.77±0.04, μ1 = 0.73 ± 0.08 and z1 =
    0.3 ± 0.1 [Figs. 4B-4E]
  expected:
  - quantity: alpha, active, mean across sessions
    value: 1.41
    tolerance: 0.05
  - quantity: beta, active, mean across sessions
    value: 0.77
    tolerance: 0.04
  - quantity: mu, active, mean across sessions
    value: 0.73
    tolerance: 0.08
  - quantity: z, active, mean across sessions
    value: 0.3
    tolerance: 0.1
  criterion: Exponents as in M7 with the readings of O9 and O10, on active-phase windows (O2).
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 498,520p paper/10.1103-w49n-2vz8.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/t/cells; cd $TMPDIR/t/cells; cat > A_md.md <<'EOF'
## The surrogate reference

Asked for by the verifier in round 1. Which surrogate windows set kappa_surr_max, how it changes when windows with few active units are left out, and its upper percentiles, which serve below as alternative starts of the threshold grids. Then the kurtosis with each unit's counts z-scored before Eq. 2 (the correlation matrix in place of the covariance), to see whether the paper's lowest surrogate kurtoses of about 6 (Appendix 3) are recovered by it.
EOF
cat > A.py <<'EOF'
S30 = W[(W.length == 30) & W.phase.isin(["active", "passive", "nni_a"])]
cols = ["path", "phase", "t0", "n_units", "N", "n_silent", "rate", "cv_a", "kappa_a", "surr0_kappa_a"]
print("the ten surrogate windows of largest kurtosis (claim seed, active, passive and NNI (a)):")
top = S30.sort_values("surr0_kappa_a", ascending=False).head(10)[cols].copy()
top["path"] = top.path.str.split("/").str[0]
print(top.round(3).to_string(index=False))
print("surrogate windows above 15:", int((S30.surr0_kappa_a > 15).sum()), "of", len(S30),
      "; in the active phase:", int((S30[S30.phase == "active"].surr0_kappa_a > 15).sum()))
print("Spearman correlation of the surrogate kurtosis with N:",
      round(stats.spearmanr(S30.N, S30.surr0_kappa_a)[0], 3), "; with the firing rate:",
      round(stats.spearmanr(S30.rate, S30.surr0_kappa_a)[0], 3))
rows = []
for s in range(5):
    for ph, phases in [("active", ["active"]), ("all phases", ["active", "passive", "nni_a"])]:
        d = S30[S30.phase.isin(phases)]
        for lab, m in [("all", d.N > 0), ("N >= 64", d.N >= 64), ("N >= 128", d.N >= 128)]:
            x = d[m][f"surr{s}_kappa_a"]
            rows.append(dict(seed_offset=SEED_OFFSETS[s], phases=ph, windows=lab, n=int(m.sum()),
                             max=x.max(), p999=np.percentile(x, 99.9), p99=np.percentile(x, 99),
                             p95=np.percentile(x, 95), median=x.median(), min=x.min()))
SREF = pd.DataFrame(rows)
print("\nsurrogate kurtosis by window set (cv a, no window is excluded under it):")
print(SREF[SREF.seed_offset == 0].round(2).to_string(index=False))
print("\nover the five seeds, active phase, all windows:")
print(SREF[(SREF.phases == "active") & (SREF.windows == "all")].round(2).to_string(index=False))
sa = SREF[(SREF.seed_offset == 0) & (SREF.phases == "active")].set_index("windows")
# Alternative starts of the threshold grids (verifier, round 1): the paper's value read from
# Figures 3C, 3D and 4A (M4), the 99th and 99.9th percentiles of the active surrogate kurtoses,
# and the maximum over active surrogate windows with at least 128 active units.
STARTS = {"paper 7": 7.0, "p99": float(sa.loc["all", "p99"]), "p99.9": float(sa.loc["all", "p999"]),
          "max N>=128": float(sa.loc["N >= 128", "max"])}
print("\nalternative grid starts:", {k: round(v, 2) for k, v in STARTS.items()})

# Correlation-matrix variant (z-scored counts before Eq. 2)
rows = []
for ph in ["active", "passive", "nni_a"]:
    d = S30[S30.phase == ph]
    for lab, col in [("data, covariance (Eq. 2)", "kappa_a"), ("surrogate, covariance (Eq. 2)", "surr0_kappa_a"),
                     ("data, correlation", "kappa_z"), ("surrogate, correlation", "surr0_kappa_z")]:
        x = d[col]
        rows.append(dict(phase=ph, kurtosis=lab, min=x.min(), p5=np.percentile(x, 5), median=x.median(),
                         p95=np.percentile(x, 95), max=x.max(),
                         iqr=np.subtract(*np.percentile(x, [75, 25]))))
print("\nkurtosis at N/16 with covariance and with correlation input:")
print(pd.DataFrame(rows).round(2).to_string(index=False))
da = S30[S30.phase == "active"]
print("active windows whose real correlation-input kurtosis exceeds their surrogate's:",
      f"{np.mean(da.kappa_z > da.surr0_kappa_z):.3f}; covariance input: {np.mean(da.kappa_a > da.surr0_kappa_a):.3f}")
print("Spearman correlation of the two real kurtoses across active windows:",
      round(stats.spearmanr(da.kappa_a, da.kappa_z)[0], 3))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/t/cells; cat > B_md.md <<'EOF'
## Trial density

Asked for by the verifier in round 1. Appendix 5 says "within each 30-s window only three to five trials are performed". The trials per active window under O5 (a), and, as variants outside O5, with aborted trials counted as failures and with every trial counted, a hit as success; then the scaling and no-scaling hit rates under each. The last lines repeat the comparison with the correlation-input kurtosis.
EOF
cat > B.py <<'EOF'
def add_counted(df, reading):
    h = np.zeros(len(df), int)
    n = np.zeros(len(df), int)
    for p, idx in df.groupby("path").indices.items():
        times, hit = cr.session_trials_counted(res_of[p], reading)
        h[idx], n[idx] = cr.trials_per_window(df.t0.values[idx], df.t1.values[idx], times, hit)
    return h, n


g315 = grid(3, 15)
rows, TD = [], {}
print("trials per session (all trials of the trials table): median",
      int(np.median([len(res_of[p]["trials"]["hit"]) for p in sel_gt])), "; active windows per session: median",
      int(ACT.groupby("path").size().median()))
for reading in ["go", "go+aborted", "all"]:
    h, n = add_counted(ACT, reading)
    TD[reading] = (h, n)
    k = ACT.kappa_a.values
    hra, hrb, na, nb = cr.hit_curves(k, h, n, g315)
    v = (na > 0) & (nb > 0)
    at = lambda x, th: float(x[np.isclose(g315, th)][0])
    rows.append(dict(trials=reading, per_window_median=np.median(n), per_window_mean=n.mean(),
                     frac_windows_3_to_5=np.mean((n >= 3) & (n <= 5)), hit_rate=h.sum() / n.sum(),
                     scal_above_noscal_3_to_15=np.mean((hra > hrb)[v]), hr_scaling_8=at(hra, 8),
                     hr_noscaling_8=at(hrb, 8), hr_scaling_12=at(hra, 12), hr_noscaling_12=at(hrb, 12)))
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("windows by number of go trials with an outcome (O5 a):",
      pd.Series(TD["go"][1]).value_counts().sort_index().to_dict())

# The correlation-input kurtosis (variant): hit rates over its own range of thresholds
kz = ACT.kappa_z.values
gz = grid(np.percentile(kz, 5), np.percentile(kz, 95))
hra, hrb, na, nb = cr.hit_curves(kz, ACT.hits_a.values, ACT.trials_a.values, gz)
v = (na > 0) & (nb > 0)
print(f"\ncorrelation-input kurtosis, thresholds {gz[0]} to {gz[-1]} (its 5th to 95th percentile), O5 (a):",
      f"scaling above no scaling at {np.mean((hra > hrb)[v]):.3f} of {int(v.sum())} points;",
      f"at the lowest point {hra[0]:.3f} against {hrb[0]:.3f}, at the highest {hra[v][-1]:.3f} against {hrb[v][-1]:.3f}")
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/t/cells; cat > C.py <<'EOF'
# Verifier round 1: the criterion with the grid started below kappa_surr_max, under CV (a) and (c).
# For each start from 3 to 12.45 the criterion is applied to the points from the start to 12.5.
def verdict_from(cur, start, hi=12.5):
    c = cur[(cur.kappa_th >= start - 1e-9) & (cur.kappa_th <= hi + 1e-9)]
    valid = (c.trials_above > 0) & (c.trials_below > 0)
    pas = valid & (c.hr_scaling > c.hr_noscaling) & (c.hr_scaling > c.hr_shuffled)
    if not valid.any():
        return "no grid", np.nan
    frac = pas[valid].mean()
    fails = valid & ~pas
    within = bool(np.all((np.maximum(c.hr_noscaling, c.hr_shuffled) - c.hr_scaling)[fails] <= c.se_scaling[fails]))
    return ("reproduced" if pas[valid].all() else "partially_reproduced" if frac >= 0.9 and within
            else "not_reproduced"), frac


rows, cnt = [], []
for cv in ["a", "c"]:
    for auto in AUTOS:
        _, cur = fig3c_eval(ACT, cv, auto, "a", np.random.default_rng(S3C), np.random.default_rng(S3C + 1),
                            ksm=3.0, hi=12.5)
        for name, st in STARTS.items():
            v, f = verdict_from(cur, st)
            c_ = cur[cur.kappa_th >= st - 1e-9]
            rows.append(dict(cv=cv, auto=auto, start=name, kappa_start=round(st, 2), points=len(c_), frac_pass=f,
                             hr_scaling_start=c_.hr_scaling.iloc[0], hr_noscaling_start=c_.hr_noscaling.iloc[0],
                             hr_shuffled_start=c_.hr_shuffled.iloc[0], se_start=c_.se_scaling.iloc[0], verdict=v))
        vs = [verdict_from(cur, st)[0] for st in grid(3, 12.45)]
        cnt.append(dict(cv=cv, auto=auto, starts=len(vs), **pd.Series(vs).value_counts().to_dict()))
print("grid from each alternative start to 12.5:")
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("\nverdicts over every start from 3 to 12.45:")
print(pd.DataFrame(cnt).fillna(0).to_string(index=False))
EOF
cat > D.py <<'EOF'
# Verifier round 1: the criterion with the grid started below kappa_surr_max (CV (a) and (c))
rows, cnt = [], []
for cv in ["a", "c"]:
    for auto in AUTOS:
        for name, st in STARTS.items():
            r = rises_eval(ACT, cv, auto, "a", np.random.default_rng(S3R), lo_override=st)
            rows.append(dict(start=name, **{k: r.get(k) for k in ["cv", "auto", "lo", "grid_points", "spearman",
                                                                   "hr_lo", "hr_hi", "se_lo", "se_hi", "diff",
                                                                   "verdict"]}))
        d = kept(ACT, cv)
        k, h, n = d.kappa_a.values, d[f"hits_{auto}"].values, d[f"trials_{auto}"].values
        gf = grid(3, 12.5)
        hra, _, _, _ = cr.hit_curves(k, h, n, gf)
        se = cr.boot_curves(k, h, n, gf, np.random.default_rng(S3R))[0]
        vs = []
        for i in range(len(gf) - 1):
            x, y, s_ = gf[i:], hra[i:], se[i:]
            m = np.isfinite(y)
            rho = stats.spearmanr(x[m], y[m])[0]
            last = np.where(m)[0][-1]
            vs.append("reproduced" if rho > 0 and y[last] - y[0] > s_[last] + s_[0] else "not_reproduced")
        cnt.append(dict(cv=cv, auto=auto, starts=len(vs), **pd.Series(vs).value_counts().to_dict(),
                        reproduced_starts=", ".join(str(gf[i]) for i, v in enumerate(vs) if v == "reproduced")[:200]))
print("grid from each alternative start to 12.5:")
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("\nverdicts over every start from 3 to 12.45 (one bootstrap draw serves every start):")
print(pd.DataFrame(cnt).fillna(0).to_string(index=False))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/t/cells; cat > E.py <<'EOF'
# Verifier round 1: the criterion with the grid started below kappa_surr_max (CV (a) and (c))
def fig4a_from(groups, nni, st, hi=15):
    g = grid(st, hi)
    F, anyp, ok = order_eval(groups, g)
    frac = ok[anyp].mean() if anyp.any() else np.nan
    fn = F[nni][0]
    v = ("reproduced" if anyp.any() and ok[anyp].all() and fn > 0.5 else
         "partially_reproduced" if anyp.any() and (frac >= 0.9 or ok[anyp].all()) else "not_reproduced")
    return dict(points=int(anyp.sum()), frac_order=frac, F_active=F["active"][0], F_passive=F["passive"][0],
                F_nni=fn, verdict=v)


rows, cnt = [], []
for cv in ["a", "c"]:
    d = kept(W[W.length == 30], cv)
    for nni in ["nni_a", "nni_b"]:
        groups = {p: d[d.phase == p].kappa_a.values for p in ["active", "passive", nni]}
        for name, st in STARTS.items():
            rows.append(dict(cv=cv, O4=nni, start=name, kappa_start=round(st, 2), **fig4a_from(groups, nni, st)))
        vs = [fig4a_from(groups, nni, st)["verdict"] for st in grid(3, 14.95)]
        cnt.append(dict(cv=cv, O4=nni, starts=len(vs), **pd.Series(vs).value_counts().to_dict()))
print("grid from each alternative start to 15:")
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("\nverdicts over every start from 3 to 14.95:")
print(pd.DataFrame(cnt).fillna(0).to_string(index=False))
EOF
cat > F.py <<'EOF'
# Verifier round 1: the criterion with the grid started below kappa_surr_max (CV (a) and (c))
def figs8_from(groups, st, hi=15):
    g = grid(st, hi)
    Fh, anyp, ok = order_eval(groups, g, strict_first={("first", "second")})
    pair = lambda a, b, ge=False: float(np.mean((Fh[a] >= Fh[b] if ge else Fh[a] > Fh[b])[anyp]))
    v = ("reproduced" if ok[anyp].all() else
         "partially_reproduced" if pair("passive", "nni") == 1.0 else "not_reproduced")
    return dict(points=int(anyp.sum()), first_ge_second=pair("first", "second", True),
                second_gt_passive=pair("second", "passive"), passive_gt_nni=pair("passive", "nni"), verdict=v)


rows, cnt = [], []
for cv in ["a", "c"]:
    d = kept(W[W.length == 30], cv)
    h1, h2 = halves(d[d.phase == "active"])
    for nni in ["nni_a", "nni_b"]:
        groups = {"first": h1.kappa_a.values, "second": h2.kappa_a.values,
                  "passive": d[d.phase == "passive"].kappa_a.values, "nni": d[d.phase == nni].kappa_a.values}
        for name, st in STARTS.items():
            rows.append(dict(cv=cv, O4=nni, start=name, kappa_start=round(st, 2), **figs8_from(groups, st)))
        vs = [figs8_from(groups, st)["verdict"] for st in grid(3, 14.95)]
        cnt.append(dict(cv=cv, O4=nni, starts=len(vs), **pd.Series(vs).value_counts().to_dict()))
print("grid from each alternative start to 15:")
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("\nverdicts over every start from 3 to 14.95:")
print(pd.DataFrame(cnt).fillna(0).to_string(index=False))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/t/cells; cat > G.py <<'EOF'


def stable_eval(cv, g, reading=("a", "a", "a"), phases=("active", "passive", "nni_a")):
    """The criterion at every point of the grid g (session values computed once per point)."""
    rows = []
    for ph in phases:
        base = SV[(ph, cv, reading, "a")]
        per = [session_values(ph, cv, reading, "a", kmin=th) for th in g]
        for e in EXP:
            allv = base[e].mean()
            sd = per[0][e].std() if len(g) and len(per[0]) else np.nan
            dep = [abs(s_[e].mean() - allv) for s_ in per if len(s_) and s_[e].notna().sum() >= 10]
            worst = max(dep) if dep else 0.0
            rows.append(dict(cv=cv, phase=ph, exponent=e, all_windows=allv, sd_at_lo=sd, points=len(dep),
                             largest_departure=worst, within=bool(len(dep) > 0 and worst <= sd)))
    return pd.DataFrame(rows)


def stable_verdict(t):
    ok_e = t.groupby("exponent").within.all()
    return ("reproduced" if ok_e.all() else "partially_reproduced" if ok_e.sum() >= 3 else "not_reproduced"), \
        ",".join(ok_e.index[~ok_e])


rows = []
for cv in CVS:
    for sm in SMAXS:
        ksm = surr_max(cv, "a", sm)
        g = grid(ksm, 12)
        row = dict(cv=cv, start=f"O6 ({sm})", kappa_start=ksm, grid_points=len(g))
        if len(g):
            t = stable_eval(cv, g)
            print(f"cv {cv}, O6 {sm}, every point of the grid from {g[0]} to 12:")
            print(t.round(3).to_string(index=False))
            row["verdict"], row["failing"] = stable_verdict(t)
        else:
            row["verdict"] = "no grid"
        rows.append(row)
# Verifier round 1: grids started below kappa_surr_max (CV (a) and (c))
for cv in ["a", "c"]:
    for name, st in STARTS.items():
        g = grid(st, 12)
        t = stable_eval(cv, g)
        print(f"cv {cv}, start {name}, every point of the grid from {g[0]} to 12:")
        print(t.round(3).to_string(index=False))
        v, f = stable_verdict(t)
        rows.append(dict(cv=cv, start=name, kappa_start=st, grid_points=len(g), verdict=v, failing=f))
print("\nverdicts:")
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("\nvariant, thresholds 4 to 12 in steps of 0.5, cv a:")
VS3 = stable_eval("a", np.arange(4, 12.01, 0.5))
print(VS3.round(3).to_string(index=False))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/t/cells; cat > H.py <<'EOF'
# Verifier round 1: mu fitted over the upper ranks only (ranks 1 to K/2), variants (c) of O9 (a)
# and (d) of O9 (b); not readings of the claims file.
R = FITS[FITS.kind == "real"]
print("mu windows with r^2 >= 0.85 (real):", {v: f"{(R[f'mu_r2_{v}'] >= cr.MU_R2_MIN).mean():.3f}" for v in "abcd"})
print("median r^2:", {v: round(float(R[f"mu_r2_{v}"].median()), 3) for v in "abcd"})
rows = []
for ph, key in [("active", "active"), ("passive", "passive"), ("nni_a", "nni"), ("nni_b", "nni")]:
    for cv in ["a", "c"]:
        for kr in "ab":
            for fs in "ab":
                for mv in "cd":
                    s = session_values(ph, cv, (kr, fs, mv), "a")
                    row = dict(phase=ph, cv=cv, O9=kr + fs + mv, sessions_mu=int(s.mu.notna().sum()))
                    within = 0
                    for e in EXP:
                        m = s[e].mean()
                        row[f"{e}_mean"] = m
                        within += abs(m - EXPECTED[key][e][0]) <= EXPECTED[key][e][1]
                    row["mu_sd"] = s.mu.std()
                    row["within"] = within
                    rows.append(row)
MUV = pd.DataFrame(rows)
print(MUV.round(3).to_string(index=False))
print("\nlargest number of means within tolerance per phase with these variants:",
      MUV.groupby("phase").within.max().to_dict())
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/t/cells; cat > I.py <<'EOF'
# Verifier round 1: the surrogate comparison paired by session (Wilcoxon signed-rank), main reading
A_ = SV[("active", "a", ("a", "a", "a"), "a")]
Su_ = session_values("active", "a", ("a", "a", "a"), "a", kind="surrogate")
j = A_.join(Su_, rsuffix="_surr", how="inner")
print(f"paired by session ({len(j)} sessions): alpha active - surrogate {np.mean(j.alpha - j.alpha_surr):.3f},",
      f"p = {stats.wilcoxon(j.alpha - j.alpha_surr).pvalue:.1e}; beta {np.mean(j.beta - j.beta_surr):.3f},",
      f"p = {stats.wilcoxon(j.beta - j.beta_surr).pvalue:.1e}")
EOF
cat > J.py <<'EOF'
# Verifier round 1: reading (b) of the maximum, restricted to thresholds with at least 30 trials
# on each side (a variant)
rows = []
for cv in CVS:
    d = kept(ACT, cv)
    k = d.kappa_a.values
    for auto in AUTOS:
        gall = grid(np.floor(k.min() * 20) / 20, np.ceil(k.max() * 20) / 20)
        hra, hrb, na, nb = cr.hit_curves(k, d[f"hits_{auto}"].values, d[f"trials_{auto}"].values, gall)
        gain = (hra - hrb) / hrb * 100
        m = (na >= 30) & (nb >= 30)
        i = np.where(m)[0][np.nanargmax(gain[m])]
        rows.append(dict(cv=cv, auto=auto, max_gain_pct=gain[i], at_kappa=gall[i], trials_above=na[i]))
print("\nlargest gain over thresholds with at least 30 trials on each side:")
print(pd.DataFrame(rows).round(2).to_string(index=False))
EOF
cd entries/cambrainha-2025; cp reproduce_cambrainha_2025.ipynb $TMPDIR/t/nb_backup.ipynb; python3 - <<'EOF'
import json, os
T = os.environ['TMPDIR'] + '/t/cells/'
p = 'reproduce_cambrainha_2025.ipynb'; nb = json.load(open(p))
C = nb['cells']
def src(text): 
    lines = text.splitlines(True)
    if lines and lines[-1].endswith('\n'): lines[-1] = lines[-1][:-1]
    return lines
def code(f, tag=None):
    c = dict(cell_type='code', execution_count=None, metadata={}, outputs=[], source=src(open(T + f).read()))
    if tag: c['metadata']['tags'] = [tag]
    return c
def md(f): return dict(cell_type='markdown', metadata={}, source=src(open(T + f).read()))
def append(i, f):
    s = ''.join(C[i]['source']).rstrip('\n') + '\n' + open(T + f).read().rstrip('\n')
    C[i]['source'] = src(s)
tag = lambda i: C[i]['metadata']['tags'][0]
# by original index, from the end so indices hold
C[69]['source'] = src(open(T + 'G.py').read().rstrip('\n'))
append(66, 'I.py')
C.insert(58, code('H.py', tag(57)))
C.insert(41, code('F.py', tag(40)))
C.insert(38, code('E.py', tag(37)))
append(28, 'J.py')
C.insert(26, code('D.py', tag(25)))
C.insert(23, code('C.py', tag(22)))
for c in [code('B.py'), md('B_md.md'), code('A.py'), md('A_md.md')][::-1][::-1]:
    pass
C[14:14] = [md('A_md.md'), code('A.py'), md('B_md.md'), code('B.py')]
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
for i, c in enumerate(C):
    print(i, c['cell_type'], c['metadata'].get('tags'), repr(''.join(c['source'])[:60]))
EOF
```

```
0 markdown None '# Reproducing Cambrainha et al. (2025) from dandiset 000713\n'
1 code None 'import os\nos.environ.setdefault("OMP_NUM_THREADS", "1")\nos.e'
2 markdown None '## Survey of the dataset\n\nEvery session file is opened and i'
3 code None 'assets = cr.session_assets()\nwith ThreadPoolExecutor(12) as '
4 markdown None '## Processing every session\n\nAll sessions with at least 128 '
5 code None 'proc = survey[survey.visp_all >= cr.MIN_UNITS].reset_index(d'
6 markdown None '## Data check'
7 code ['sanity'] 'ok = [r for r in results if "error" not in r]\nsessions_ok = '
8 markdown None 'The checks above show:\n\n- 153 session files from 81 mice, no'
9 markdown None '## Common definitions\n\nThe analysis set is the sessions with'
10 code None 'W = W_all[(W_all.units == "all") & W_all.path.isin(sel_gt)].'
11 markdown None '## How readings decide\n\nThe claims file lists readings of de'
12 markdown None 'The two poolings of O3 give the same number: psi is normalis'
13 code None 'd = W[W.length == 30]\nprint("largest |kappa_a - kappa_b| ove'
14 markdown None '## The surrogate reference\n\nAsked for by the verifier in rou'
15 code None 'S30 = W[(W.length == 30) & W.phase.isin(["active", "passive"'
16 markdown None '## Trial density\n\nAsked for by the verifier in round 1. Appe'
17 code None 'def add_counted(df, reading):\n    h = np.zeros(len(df), int)'
18 markdown None "## sessions-selected\n\n> Of the dataset's sessions, 62 (from "
19 code ['claim:sessions-selected'] 'rows = []\nfor col, label in [("visp_all", "O1 (a) all V1 uni'
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; date -u; time $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 14 17 2>&1 | grep -v Warning | tail -80
```

```
Fri Nov 27 11:23:38 UTC 2026
dandiset 000713 version 0.240702.1725
##### cell 15
the ten surrogate windows of largest kurtosis (claim seed, active, passive and NNI (a)):
      path   phase       t0  n_units   N  n_silent  rate  cv_a  kappa_a  surr0_kappa_a
sub-545994 passive 5213.164      171  87        84 0.031 3.886   54.844         49.979
sub-545994 passive 5243.164      171  12       159 0.002 3.167   39.274         46.794
sub-553253   nni_a 4166.630      136 127         9 0.115 1.167   19.571          9.658
sub-553253   nni_a 3716.630      136 126        10 0.136 1.110   14.433          8.983
sub-553253 passive 8179.444      136 126        10 0.170 1.018    7.588          8.299
sub-553253  active  445.003      136 123        13 0.151 0.938    7.155          8.142
sub-553253  active 3265.003      136 128         8 0.175 1.121   10.070          7.819
sub-545994 passive 5453.164      171  78        93 0.011 1.600   89.407          7.637
sub-545994 passive 5483.164      171 135        36 0.034 1.646   25.653          7.620
sub-553253   nni_a 4046.630      136 127         9 0.121 1.296   14.832          7.568
surrogate windows above 15: 2 of 2035 ; in the active phase: 0
Spearman correlation of the surrogate kurtosis with N: -0.326 ; with the firing rate: -0.219

surrogate kurtosis by window set (cv a, no window is excluded under it):
 seed_offset     phases  windows    n   max  p999  p99  p95  median  min
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 255,290p paper/10.1103-w49n-2vz8.txt; grep -n -i "hit rate\|aborted\|false alarm\|catch" paper/10.1103-w49n-2vz8.txt | head -40; cat questions/cambrainha-2025.yaml 2>/dev/null | head -30; ls questions | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftoppm mutool gs convert magick 2>/dev/null; $TMPDIR/venv/bin/python -c "import fitz" 2>&1; python3 -c "import fitz; print('fitz ok')" 2>&1; cat questions/README.md | head -40; cat questions/bennett-2024.yaml | head -30
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print('fitz ok')
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
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
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/t/cells; cat > K.py <<'EOF'
# Variant outside O5, asked for by the verifier (trial density): aborted trials counted as
# failures, or every trial counted, under CV (a). Asked of a reader (questions file).
def shuffled_counted(reading):
    def f(d, auto, rng=np.random.default_rng(S3C), reps=REPS):
        out = np.zeros((reps, len(d)))
        for p, idx in d.groupby("path").indices.items():
            times, hit = cr.session_trials_counted(res_of[p], reading)
            H = cr.swap_shuffle(hit, rng, reps)
            o = np.argsort(d.t0.values[idx])
            s0, s1 = d.t0.values[idx][o], d.t1.values[idx][o]
            wi = np.searchsorted(s0, times, side="right") - 1
            inside = (wi >= 0) & (times < s1[np.clip(wi, 0, None)])
            for k_ in np.where(inside)[0]:
                out[:, idx[o[wi[k_]]]] += H[:, k_]
        return out
    return f


rows, cnt, CUR_T = [], [], {}
for reading in ["go+aborted", "all"]:
    A_t = ACT.copy()
    A_t["hits_a"], A_t["trials_a"] = TD[reading]
    _, cur = fig3c_eval(A_t, "a", "a", "a", None, np.random.default_rng(S3C + 1), ksm=3.0, hi=12.5,
                        sh_cache=lambda d, auto, r=reading: shuffled_counted(r)(d, auto))
    CUR_T[reading] = cur
    for name, st in {"O6 (a)": surr_max("a", "a", "a"), **STARTS}.items():
        v, f = verdict_from(cur, st)
        c_ = cur[cur.kappa_th >= st - 1e-9]
        rows.append(dict(trials=reading, start=name, kappa_start=round(st, 2), frac_pass=f,
                         hr_scaling_start=c_.hr_scaling.iloc[0] if len(c_) else np.nan,
                         hr_noscaling_start=c_.hr_noscaling.iloc[0] if len(c_) else np.nan,
                         hr_shuffled_start=c_.hr_shuffled.iloc[0] if len(c_) else np.nan, verdict=v))
    vs = [verdict_from(cur, st)[0] for st in grid(3, 12.45)]
    cnt.append(dict(trials=reading, starts=len(vs), **pd.Series(vs).value_counts().to_dict()))
    k, h, n = A_t.kappa_a.values, A_t.hits_a.values, A_t.trials_a.values
    gall = grid(np.floor(k.min() * 20) / 20, np.ceil(k.max() * 20) / 20)
    hra, hrb, na, nb = cr.hit_curves(k, h, n, gall)
    gain = (hra - hrb) / hrb * 100
    both = (na > 0) & (nb > 0)
    i = np.where(both)[0][np.nanargmax(gain[both])]
    at = lambda th: float(gain[np.isclose(gall, th)][0])
    m7 = both & (gall >= 7 - 1e-9) & (gall <= 12.5 + 1e-9)
    j = np.where(m7)[0][np.nanargmax(gain[m7])]
    print(f"{reading}: relative gain at 8 {at(8):.2f} %, at 12 {at(12):.2f} %; largest over all thresholds "
          f"{gain[i]:.2f} % at {gall[i]} ({na[i]:.0f} trials above); largest from 7 to 12.5 {gain[j]:.2f} % at {gall[j]}")
    s_ = cur[(cur.kappa_th >= 7 - 1e-9)]
    m = s_.hr_scaling.notna()
    print(f"   scaling hit rate from 7 to 12.5: Spearman {stats.spearmanr(s_.kappa_th[m], s_.hr_scaling[m])[0]:.3f}, "
          f"{s_.hr_scaling.iloc[0]:.3f} at 7 (SE {s_.se_scaling.iloc[0]:.3f}) and {s_.hr_scaling[m].iloc[-1]:.3f} "
          f"at {s_.kappa_th[m].iloc[-1]} (SE {s_.se_scaling[m].iloc[-1]:.3f})")
print("\nfig3c criterion with these trials, from each start to 12.5:")
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("\nverdicts over every start from 3 to 12.45:")
print(pd.DataFrame(cnt).fillna(0).to_string(index=False))
EOF
cd entries/cambrainha-2025; python3 - <<'EOF'
import json, os
T = os.environ['TMPDIR'] + '/t/cells/'
p = 'reproduce_cambrainha_2025.ipynb'; nb = json.load(open(p)); C = nb['cells']
assert C[27]['source'][0].startswith('# Verifier round 1')
src = open(T+'K.py').read().rstrip('\n').splitlines(True)
C.insert(28, dict(cell_type='code', execution_count=None, metadata={'tags': ['claim:fig3c-scaling-hit-rate-higher']}, outputs=[], source=src))
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
EOF
date -u; time $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 25 32 2>&1 | grep -v Warning | tail -120
```

```
Fri Nov 27 11:24:21 UTC 2026
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
dandiset 000713 version 0.240702.1725
##### cell 25
cv auto O6  kappa_surr_max  grid_points  points_with_trials  frac_pass failures_within_SE  hr_scaling_lo  hr_noscaling_lo  hr_shuffled_lo  hr_scaling_hi  hr_noscaling_hi  trials_above_hi              verdict
 a    a  a           8.142           88                88.0      0.648              False          0.701            0.830           0.762            1.0            0.815              8.0       not_reproduced
 a    a  b          49.979            0                 NaN        NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN              no grid
 a    b  a           8.142           88                88.0      0.648              False          0.705            0.833           0.766            1.0            0.817              8.0       not_reproduced
 a    b  b          49.979            0                 NaN        NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN              no grid
 b    a  a           8.142           88                88.0      0.443              False          0.609            0.793           0.734            1.0            0.744              2.0       not_reproduced
 b    a  b           8.983           71                71.0      0.549              False          0.628            0.761           0.718            1.0            0.744              2.0       not_reproduced
 b    b  a           8.142           88                88.0      0.443              False          0.609            0.795           0.735            1.0            0.746              2.0       not_reproduced
 b    b  b           8.983           71                71.0      0.549              False          0.628            0.764          
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; time ALSO=15,17 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 27 32 2>&1 | grep -v "Warning\|nanvar" | tail -80
```

```
dandiset 000713 version 0.240702.1725
##### cell 27
Traceback (most recent call last):
  File "/tmp/claude-1001/t/dev.py", line 34, in <module>
    exec(src(i), ns)
    ~~~~^^^^^^^^^^^^
  File "<string>", line 19, in <module>
NameError: name 'fig3c_eval' is not defined

real	0m1.424s
user	0m1.614s
sys	0m0.124s
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; time ALSO=15,17,25 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 27 32 2>&1 | grep -v "Warning\|nanvar" | tail -80
```

```
##### cell 28 done 1.1s
##### cell 31
cv auto O6  kappa_surr_max   lo  grid_points  spearman  hr_lo  hr_hi  kappa_hi  trials_hi  se_lo  se_hi  diff    verdict
 a    a  a           8.142 8.15           88     0.921  0.701    1.0      12.5        8.0  0.041    0.0 0.299 reproduced
 a    a  b          49.979  NaN            0       NaN    NaN    NaN       NaN        NaN    NaN    NaN   NaN    no grid
 a    b  a           8.142 8.15           88     0.921  0.705    1.0      12.5        8.0  0.041    0.0 0.295 reproduced
 a    b  b          49.979  NaN            0       NaN    NaN    NaN       NaN        NaN    NaN    NaN   NaN    no grid
 b    a  a           8.142 8.15           88     0.548  0.609    1.0      12.5        2.0  0.058    0.0 0.391 reproduced
 b    a  b           8.983 9.00           71     0.473  0.628    1.0      12.5        2.0  0.086    0.0 0.372 reproduced
 b    b  a           8.142 8.15           88     0.548  0.609    1.0      12.5        2.0  0.058    0.0 0.391 reproduced
 b    b  b           8.983 9.00           71     0.473  0.628    1.0      12.5        2.0  0.086    0.0 0.372 reproduced
 c    a  a           8.142 8.15           88     0.921  0.701    1.0      12.5        8.0  0.041    0.0 0.299 reproduced
 c    a  b           9.658 9.70           57     0.744  0.833    1.0      12.5        8.0  0.054    0.0 0.167 reproduced
 c    b  a           8.142 8.15           88     0.921  0.705    1.0      12.5        8.0  0.041    0.0 0.295 reproduced
 c    b  b           9.658 9.70           57     0.744  0.833    1.0      12.5        8.0  0.054    0.0 0.167 reproduced

variant (not the criterion): main reading over the thresholds 3 to 12.5
cv auto O6  kappa_surr_max  lo  grid_points  spearman  hr_lo  hr_hi  kappa_hi  trials_hi  se_lo  se_hi  diff    verdict
 a    a  a           8.142 3.0          191     0.348  0.816    1.0      12.5        8.0  0.013    0.0 0.184 reproduced

[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
import json
p = 'reproduce_cambrainha_2025.ipynb'; nb = json.load(open(p)); C = nb['cells']
s = ''.join(C[27]['source'])
s = s.replace('''rows, cnt = [], []
for cv in ["a", "c"]:''', '''def spans_of(g, vs, target):
    """The starts g at which the verdict is `target`, as runs (lo-hi)."""
    m = np.array([v == target for v in vs])
    out, i = [], 0
    while i < len(m):
        if m[i]:
            j = i
            while j + 1 < len(m) and m[j + 1]:
                j += 1
            out.append(f"{g[i]}-{g[j]}" if j > i else f"{g[i]}")
            i = j + 1
        else:
            i += 1
    return ", ".join(out) if out else "none"


rows, cnt = [], []
for cv in ["a", "c"]:''', 1)
s = s.replace('''        vs = [verdict_from(cur, st)[0] for st in grid(3, 12.45)]
        cnt.append(dict(cv=cv, auto=auto, starts=len(vs), **pd.Series(vs).value_counts().to_dict()))''',
'''        gs = grid(3, 12.45)
        vs = [verdict_from(cur, st)[0] for st in gs]
        cnt.append(dict(cv=cv, auto=auto, starts=len(vs), **pd.Series(vs).value_counts().to_dict(),
                        reproduced_at=spans_of(gs, vs, "reproduced"),
                        partial_at=spans_of(gs, vs, "partially_reproduced")))''')
C[27]['source'] = s.splitlines(True)
s = ''.join(C[28]['source'])
s = s.replace('''    vs = [verdict_from(cur, st)[0] for st in grid(3, 12.45)]
    cnt.append(dict(trials=reading, starts=len(vs), **pd.Series(vs).value_counts().to_dict()))''',
'''    gs = grid(3, 12.45)
    vs = [verdict_from(cur, st)[0] for st in gs]
    cnt.append(dict(trials=reading, starts=len(vs), **pd.Series(vs).value_counts().to_dict(),
                    reproduced_at=spans_of(gs, vs, "reproduced"), partial_at=spans_of(gs, vs, "partially_reproduced")))''')
C[28]['source'] = s.splitlines(True)
s = ''.join(C[32]['source'])
s = s.replace('''reproduced_starts=", ".join(str(gf[i]) for i, v in enumerate(vs) if v == "reproduced")[:200]))''',
 '''reproduced_at=spans_of(gf[:-1], vs, "reproduced")))''')
C[32]['source'] = s.splitlines(True)
for i in (44, 48):
    s = ''.join(C[i]['source'])
    for a in ['vs = [fig4a_from(groups, nni, st)["verdict"] for st in grid(3, 14.95)]', 'vs = [figs8_from(groups, st)["verdict"] for st in grid(3, 14.95)]']:
        if a in s:
            s = s.replace(a, 'gs = grid(3, 14.95)\n        ' + a.replace('grid(3, 14.95)', 'gs'))
    s = s.replace('**pd.Series(vs).value_counts().to_dict()))', '**pd.Series(vs).value_counts().to_dict(),\n                        reproduced_at=spans_of(gs, vs, "reproduced"), partial_at=spans_of(gs, vs, "partially_reproduced")))')
    C[i]['source'] = s.splitlines(True)
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
EOF
time ALSO=15,17,25 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 27 28 2>&1 | grep -v "Warning\|nanvar" | tail -60
```

```
dandiset 000713 version 0.240702.1725
##### cell 27
grid from each alternative start to 12.5:
cv auto      start  kappa_start  points  frac_pass  hr_scaling_start  hr_noscaling_start  hr_shuffled_start  se_start        verdict
 a    a    paper 7         7.00     111      0.514             0.760               0.839              0.774     0.026 not_reproduced
 a    a        p99         6.47     121      0.471             0.775               0.842              0.782     0.022 not_reproduced
 a    a      p99.9         7.87      93      0.613             0.712               0.834              0.764     0.037 not_reproduced
 a    a max N>=128         7.82      94      0.606             0.721               0.833              0.763     0.036 not_reproduced
 a    b    paper 7         7.00     111      0.514             0.765               0.841              0.779     0.026 not_reproduced
 a    b        p99         6.47     121      0.471             0.780               0.844              0.786     0.022 not_reproduced
 a    b      p99.9         7.87      93      0.613             0.714               0.837              0.769     0.036 not_reproduced
 a    b max N>=128         7.82      94      0.606             0.723               0.836              0.768     0.036 not_reproduced
 c    a    paper 7         7.00     111      0.514             0.760               0.839              0.774     0.026 not_reproduced
 c    a        p99         6.47     121      0.471             0.775               0.842              0.782     0.022 not_reproduced
 c    a      p99.9         7.87      93      0.613             0.712               0.834              0.764     0.037 not_reproduced
 c    a max N>=128         7.82      94      0.606             0.721               0.833              0.763     0.036 not_reproduced
 c    b    paper 7         7.00     111      0.514             0.765               0.841              0.779     0.026 not_reproduced
 c    b        p99         6.47     121     
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; (ALSO=15,17 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 34 34 2>&1 | grep -v "Warning\|nanvar" | tail -12; ALSO=15,17,25,27 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 43 48 2>&1 | grep -v "Warning\|nanvar" | grep -A40 "cell 44\|cell 48" ) 2>&1 | cut -c1-250
```

```
dandiset 000713 version 0.240702.1725
##### cell 44
cv    O4 O6  kappa_surr_max  points  frac_order  F_active_lo  F_passive_lo  F_nni_lo        verdict
 a nni_a  a          8.1421     138         0.0       0.0977        0.1299    0.3053 not_reproduced
 a nni_a  b         49.9789       0         NaN          NaN           NaN       NaN        no grid
 a nni_b  a          8.1421     138         0.0       0.0977        0.1299    0.3883 not_reproduced
 a nni_b  b         49.9789       0         NaN          NaN           NaN       NaN        no grid
 b nni_a  a          8.1421     138         0.0       0.2067        0.2046    0.5156 not_reproduced
 b nni_a  b          8.9831     121         0.0       0.0913        0.1239    0.4688 not_reproduced
 b nni_b  a          8.1421     138         0.0       0.2067        0.2046    0.5902 not_reproduced
 b nni_b  b         10.5958      89         0.0       0.0192        0.0461    0.3934 not_reproduced
 c nni_a  a          8.1421     138         0.0       0.0977        0.1233    0.3053 not_reproduced
 c nni_a  b          9.6585     107         0.0       0.0322        0.0544    0.1905 not_reproduced
 c nni_b  a          8.1421     138         0.0       0.0977        0.1233    0.3883 not_reproduced
 c nni_b  b         10.5958      89         0.0       0.0131        0.0254    0.1355 not_reproduced

fraction of windows above kappa_th, cv a, thresholds 3 to 15 (not the criterion's grid):
 kappa_th  active  passive  nni_a  nni_b
      3.0  1.0000   1.0000 1.0000 1.0000
      4.0  0.9881   0.9774 0.9720 1.0000
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; ALSO=15,17 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 35 35 2>&1 | grep -v "Warning\|nanvar" | tail -14; ALSO=15,17,25,27,44 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 48 49 2>&1 | grep -v "Warning\|nanvar" | grep -A30 "cell 49"
```

```
4000  b  b           10.75                   34.48
        4000  c  a            8.54                   22.75
        4000  c  b           10.75                   22.75
points of the plotted gain outside -60 to 60 %: 0

largest gain over thresholds with at least 30 trials on each side:
cv auto  max_gain_pct  at_kappa  trials_above
 a    a          6.37      10.1          30.0
 a    b          6.02      10.1          30.0
 b    a         -2.62       9.2          33.0
 b    b         -2.93       9.2          33.0
 c    a          6.37      10.1          30.0
 c    b          6.02      10.1          30.0
##### cell 35 done 0.4s
##### cell 49
grid from each alternative start to 15:
cv    O4      start  kappa_start  points  first_ge_second  second_gt_passive  passive_gt_nni        verdict
 a nni_a    paper 7         7.00     161            0.851              0.025             0.0 not_reproduced
 a nni_a        p99         6.47     171            0.801              0.053             0.0 not_reproduced
 a nni_a      p99.9         7.87     143            0.958              0.000             0.0 not_reproduced
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
import json
p = 'reproduce_cambrainha_2025.ipynb'; nb = json.load(open(p)); C = nb['cells']
for i in (45, 49):
    s = ''.join(C[i]['source']); n0 = s
    for a in ['vs = [fig4a_from(groups, nni, st)["verdict"] for st in grid(3, 14.95)]', 'vs = [figs8_from(groups, st)["verdict"] for st in grid(3, 14.95)]']:
        if a in s:
            s = s.replace(a, 'gs = grid(3, 14.95)\n        ' + a.replace('grid(3, 14.95)', 'gs'))
    s = s.replace('**pd.Series(vs).value_counts().to_dict()))', '**pd.Series(vs).value_counts().to_dict(),\n                        reproduced_at=spans_of(gs, vs, "reproduced"),\n                        partial_at=spans_of(gs, vs, "partially_reproduced")))')
    assert s != n0
    C[i]['source'] = s.splitlines(True)
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
EOF
date -u; time ALSO=15,17 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 63 80 2>&1 | grep -v "Warning\|nanvar\|var = \|return _meth\|ret = " | grep -A45 "cell 63\|cell 66\|cell 75\|cell 78" | cut -c1-220 | head -230
```

```
Fri Nov 27 11:26:12 UTC 2026
##### cell 66
cv  O9 O10  sessions  sessions_mu  alpha_mean  beta_mean  mu_mean  z_mean  alpha_sd  beta_sd  mu_sd  z_sd  within
 a aaa   a         7            2       1.475      0.765    1.399   0.166     0.072    0.070  0.168 0.020       1
 a aaa   b         7            0       1.479      0.757      NaN   0.170     0.072    0.067    NaN 0.021       1
 a aab   a         7            5       1.475      0.765    1.548   0.166     0.072    0.070  0.254 0.020       1
 a aab   b         7            1       1.479      0.757    1.324   0.170     0.072    0.067    NaN 0.021       1
 a aba   a         7            2       1.475      0.744    1.399   0.166     0.072    0.068  0.168 0.020       1
 a aba   b         7            0       1.479      0.781      NaN   0.170     0.072    0.080    NaN 0.021       1
 a abb   a         7            5       1.475      0.744    1.548   0.166     0.072    0.068  0.254 0.020       1
 a abb   b         7            1       1.479      0.781    1.324   0.170     0.072    0.080    NaN 0.021       1
 a baa   a         7            2       1.423      0.778    1.399   0.106     0.056    0.041  0.168 0.014       2
 a baa   b         7            0       1.423      0.776      NaN   0.106     0.056    0.039    NaN 0.016       2
 a bab   a         7            5       1.423      0.778    1.548   0.106     0.056    0.041  0.254 0.014       2
 a bab   b         7            1       1.423      0.776    1.324   0.106     0.056    0.039    NaN 0.016       2
 a bba   a         7            2       1.423      0.806    1.399   0.106     0.056    0.052  0.168 0.014       2
 a bba   b         7            0       1.423      0.808      NaN   0.106     0.056    0.050    NaN 0.016       2
 a bbb   a         7            5       1.423      0.806    1.548   0.106     0.056    0.052  0.254 0.014       2
 a bbb   b         7            1       1.423      0.808    1.324   0.106     0.056    0.050    NaN 0.016       2
 b aaa   a         
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; time ALSO=15,17,63,65,69 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 76 79 2>&1 | grep -v "Warning\|nanvar\|var = \|return _meth\|ret = " | grep -v "^ a \|^ b \|^ c " | cut -c1-220 | head -120
```

```
dandiset 000713 version 0.240702.1725
##### cell 76
Traceback (most recent call last):
  File "/tmp/claude-1001/t/dev.py", line 34, in <module>
    exec(src(i), ns)
    ~~~~^^^^^^^^^^^^
  File "<string>", line 3, in <module>
NameError: name 'READ9' is not defined

real	0m1.417s
user	0m1.590s
sys	0m0.142s
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 -c "
import json;nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  if i>58: print(i,c['cell_type'],c['metadata'].get('tags'),repr(''.join(c['source'])[:50]))
"
```

```
59 markdown None '**Result: reproduced.** Under every reading the hi'
60 markdown None '## figs7-fatigue-halves\n\n> In each half of the act'
61 code ['claim:figs7-fatigue-halves'] 'rows = []\nfor cv in CVS:\n    h1, h2 = halves(kept('
62 markdown None '**Result: not reproduced**, resting on CV (a), an '
63 markdown None '## Real-space exponents (fig4 claims)\n\nPer window,'
64 code None 't0 = time.time()\nfit_rows = []\nfor r in sessions_o'
65 markdown None '## fig4-exponents-active\n\n> In the active phase th'
66 code ['claim:fig4-exponents-active'] 'MA = means_table("active", "active")\nshow = ["cv",'
67 code ['claim:fig4-exponents-active'] '# Verifier round 1: mu fitted over the upper ranks'
68 markdown None '**Result: not reproduced.** No reading puts more t'
69 markdown None '## fig4-exponents-passive\n\n> In the passive phase '
70 code ['claim:fig4-exponents-passive'] '\n\ndef mwu(a, b):\n    a, b = np.asarray(a, float), '
71 markdown None '**Result: not reproduced.** All 48 readings fail. '
72 markdown None '## fig4-exponents-nni\n\n> With non-natural images t'
73 code ['claim:fig4-exponents-nni'] 'rows = []\nfor nni in ["nni_a", "nni_b"]:\n    M = m'
74 markdown None '**Result: not reproduced.** All 96 readings fail, '
75 markdown None '## fig4bc-static-exponents-trend\n\n> In the active '
76 code ['claim:fig4bc-static-exponents-trend'] 'rows = []\nfor cv in CVS:\n    for reading in READ9:'
77 markdown None '**Result: partially reproduced.** Under every read'
78 markdown None '## figs3-exponents-stable-with-threshold\n\n> Expone'
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; time ALSO=15,17,64,70 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 76 79 2>&1 | grep -v "Warning\|nanvar\|var = \|return _meth\|ret = " | grep -v "^ a \|^ b \|^ c " | cut -c1-220 | head -150
```

```
dandiset 000713 version 0.240702.1725
Traceback (most recent call last):
  File "/tmp/claude-1001/t/dev.py", line 34, in <module>
    exec(src(i), ns)
    ~~~~^^^^^^^^^^^^
  File "<string>", line 28, in <module>
NameError: name 'show' is not defined

real	0m7.655s
user	0m7.862s
sys	0m0.109s
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; time ALSO=15,17,64,66,70 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 76 79 2>&1 | grep -v "Warning\|nanvar\|var = \|return _meth\|ret = " | grep -v "^ a \|^ b \|^ c " | cut -c1-220 | head -150
```

```
dandiset 000713 version 0.240702.1725
##### cell 76
cv  O9 O10    O4            test  p_alpha   p_beta  deviation               d_alpha                d_beta                     z  order_alpha  order_beta  order_z              verdict

verdicts over all readings: {'partially_reproduced': 68, 'reproduced': 52, 'not_reproduced': 24}
paired by session (7 sessions): alpha active - surrogate 0.406, p = 1.6e-02; beta -0.199, p = 1.6e-02
##### cell 76 done 0.3s
##### cell 79
cv a, O6 a, every point of the grid from 8.15 to 12:
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
cv b, O6 a, every point of the grid from 8.15 to 12:
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
cv b, O6 b, every point of the grid from 9.0 to 12:
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
cv c, O6 a, every point of the grid from 8.15 to 12:
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
cv c, O6 b, every point of the grid from 9.7 to 12:
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
cv a, start paper 7, every point of the grid from 7.0 to 12:
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; timeout 4500 python tools/entry.py all entries/cambrainha-2025 2>&1 | tail -15; date -u
```

```
Fri Nov 27 11:27:25 UTC 2026
[32m   2429[39m     [38;5;28;01mraise[39;00m [38;5;167;01mTypeError[39;00m([33m"[39m[33mCannot index by location index with a non-integer key[39m[33m"[39m)
[32m   2431[39m [38;5;66;03m# validate the location[39;00m
[32m-> [39m[32m2432[39m [30;43mself[39;49m[30;43m.[39;49m[30;43m_validate_integer[39;49m[30;43m([39;49m[30;43mkey[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43maxis[39;49m[30;43m)[39;49m
[32m   2434[39m [38;5;28;01mreturn[39;00m [38;5;28mself[39m.obj._ixs(key, axis=axis)

[36mFile [39m[32m~/work/encore-registry/encore-registry/executed/cambrainha-2025/.venv/lib/python3.13/site-packages/pandas/core/indexing.py:2365[39m, in [36m_iLocIndexer._validate_integer[39m[34m(self, key, axis)[39m
[32m   2363[39m len_axis = [38;5;28mlen[39m([38;5;28mself[39m.obj._get_axis(axis))
[32m   2364[39m [38;5;28;01mif[39;00m key >= len_axis [38;5;129;01mor[39;00m key < -len_axis:
[32m-> [39m[32m2365[39m     [38;5;28;01mraise[39;00m [38;5;167;01mIndexError[39;00m([33m"[39m[33msingle positional indexer is out-of-bounds[39m[33m"[39m)

[31mIndexError[39m: single positional indexer is out-of-bounds


0 error(s)
FAIL  reproduce_cambrainha_2025.ipynb  (1290 s)
Fri Nov 27 11:49:09 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls -la executed/cambrainha-2025/; python3 -c "
import json;nb=json.load(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  for o in c.get('outputs',[]):
    if o.get('output_type')=='error': print(i, o['ename'], ''.join(c['source'])[:80])
"
```

```
total 384
drwxr-xr-x 3 runner runner   4096 Nov 27 11:27 .
drwxr-xr-x 3 runner runner   4096 Nov 27 10:28 ..
drwxr-xr-x 5 runner runner   4096 Nov 27 11:27 .venv
-rw-r--r-- 1 runner runner 369352 Nov 27 10:10 reproduce_cambrainha_2025.ipynb
-rw-r--r-- 1 runner runner   4110 Nov 27 11:49 result.json
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;r=json.load(open('executed/cambrainha-2025/result.json')); e=r['results'][0]['error']; print(e[:3000] if isinstance(e,str) else e)
" | sed 's/\x1b\[[0-9;]*m//g' | head -60
```

```
9m In[13], line 41
     37         for name, st in STARTS.items():
     38             v, f = verdict_from(cur, st)
     39             c_ = cur[cur.kappa_th >= st - 1e-9]
     40             rows.append(dict(cv=cv, auto=auto, start=name, kappa_start=round(st, 2), points=len(c_), frac_pass=f,
---> 41                              hr_scaling_start=c_.hr_scaling.iloc[0], hr_noscaling_start=c_.hr_noscaling.iloc[0],
     42                              hr_shuffled_start=c_.hr_shuffled.iloc[0], se_start=c_.se_scaling.iloc[0], verdict=v))
     43         gs = grid(3, 12.45)
     44         vs = [verdict_from(cur, st)[0] for st in gs]

File ~/work/encore-registry/encore-registry/executed/cambrainha-2025/.venv/lib/python3.13/site-packages/pandas/core/indexing.py:1342, in _LocationIndexer.__getitem__(self, key)
   1340 maybe_callable = com.apply_if_callable(key, self.obj)
   1341 maybe_callable = self._raise_callable_usage(key, maybe_callable)
-> 1342 return self._getitem_axis(maybe_callable, axis=axis)

File ~/work/encore-registry/encore-registry/executed/cambrainha-2025/.venv/lib/python3.13/site-packages/pandas/core/indexing.py:2432, in _iLocIndexer._getitem_axis(self, key, axis)
   2429     raise TypeError("Cannot index by location index with a non-integer key")
   2431 # validate the location
-> 2432 self._validate_integer(key, axis)
   2434 return self.obj._ixs(key, axis=axis)
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
import json
p = 'reproduce_cambrainha_2025.ipynb'; nb = json.load(open(p)); C = nb['cells']
def rep(i, a, b, count=1):
    s = ''.join(C[i]['source']); assert s.count(a) >= 1, (i, a); s = s.replace(a, b) ; C[i]['source'] = s.splitlines(True)
# C (27)
rep(27, '''            c_ = cur[cur.kappa_th >= st - 1e-9]
            rows.append(dict(cv=cv, auto=auto, start=name, kappa_start=round(st, 2), points=len(c_), frac_pass=f,
                             hr_scaling_start=c_.hr_scaling.iloc[0], hr_noscaling_start=c_.hr_noscaling.iloc[0],
                             hr_shuffled_start=c_.hr_shuffled.iloc[0], se_start=c_.se_scaling.iloc[0], verdict=v))''',
'''            c_ = cur[cur.kappa_th >= st - 1e-9]
            rows.append(dict(cv=cv, auto=auto, start=name, kappa_start=round(st, 2), points=len(c_), frac_pass=f,
                             hr_scaling_start=first(c_.hr_scaling), hr_noscaling_start=first(c_.hr_noscaling),
                             hr_shuffled_start=first(c_.hr_shuffled), se_start=first(c_.se_scaling), verdict=v))''')
rep(27, '''def spans_of(g, vs, target):''', '''def first(s):
    return s.iloc[0] if len(s) else np.nan


def spans_of(g, vs, target):''')
rep(28, '''                         hr_scaling_start=c_.hr_scaling.iloc[0] if len(c_) else np.nan,
                         hr_noscaling_start=c_.hr_noscaling.iloc[0] if len(c_) else np.nan,
                         hr_shuffled_start=c_.hr_shuffled.iloc[0] if len(c_) else np.nan, verdict=v))''',
'''                         hr_scaling_start=first(c_.hr_scaling), hr_noscaling_start=first(c_.hr_noscaling),
                         hr_shuffled_start=first(c_.hr_shuffled), verdict=v))''')
rep(45, '''    g = grid(st, hi)
    F, anyp, ok = order_eval(groups, g)''', '''    g = grid(st, hi)
    if len(g) == 0:
        return dict(points=0, verdict="no grid")
    F, anyp, ok = order_eval(groups, g)''')
rep(49, '''    g = grid(st, hi)
    Fh, anyp, ok = order_eval(groups, g, strict_first={("first", "second")})''', '''    g = grid(st, hi)
    if len(g) == 0:
        return dict(points=0, verdict="no grid")
    Fh, anyp, ok = order_eval(groups, g, strict_first={("first", "second")})''')
rep(79, '''    for name, st in STARTS.items():
        g = grid(st, 12)
        t = stable_eval(cv, g)''', '''    for name, st in STARTS.items():
        g = grid(st, 12)
        if len(g) == 0:
            rows.append(dict(cv=cv, start=name, kappa_start=st, grid_points=0, verdict="no grid"))
            continue
        t = stable_eval(cv, g)''')
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/t/dev.py'; s=open(p).read()
s=s.replace("""        if i >= a: print(f'##### cell {i} done""","""        if i == 15 and os.environ.get('EXTRA'): ns['STARTS']['test13'] = 13.0
        if i >= a: print(f'##### cell {i} done""")
open(p,'w').write(s)
EOF
EXTRA=1 ALSO=15,17,25,44,48,64,66,70 $TMPDIR/venv/bin/python $TMPDIR/t/dev.py run 27 79 2>&1 | grep -i "test13\|error\|Traceback\|done" | cut -c1-200
```

```
a    a     test13        13.00       0        NaN               NaN                 NaN                NaN       NaN        no grid
 a    b     test13        13.00       0        NaN               NaN                 NaN                NaN       NaN        no grid
 c    a     test13        13.00       0        NaN               NaN                 NaN                NaN       NaN        no grid
 c    b     test13        13.00       0        NaN               NaN                 NaN                NaN       NaN        no grid
##### cell 27 done 2.1s
go+aborted     test13        13.00        NaN               NaN                 NaN                NaN              no grid
       all     test13        13.00        NaN               NaN                 NaN                NaN              no grid
##### cell 28 done 1.2s
##### cell 31 done 7.4s
    test13  a    a  NaN            0       NaN    NaN    NaN    NaN    NaN   NaN    no grid
    test13  a    b  NaN            0       NaN    NaN    NaN    NaN    NaN   NaN    no grid
    test13  c    a  NaN            0       NaN    NaN    NaN    NaN    NaN   NaN    no grid
    test13  c    b  NaN            0       NaN    NaN    NaN    NaN    NaN   NaN    no grid
##### cell 32 done 6.4s
##### cell 35 done 0.4s
##### cell 38 done 11.5s
##### cell 41 done 3.9s
##### cell 44 done 0.1s
 a nni_a     test13        13.00      41         0.0     0.005      0.012  0.067 not_reproduced
 a nni_b     test13        13.00      41         0.0     0.005      0.012  0.077 not_reproduced
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; timeout 4500 python tools/entry.py all entries/cambrainha-2025 2>&1 | tail -5 | cut -c1-300; date -u
```

```
Fri Nov 27 11:50:48 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbfor
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-cambrainha-2025 in executed/cambrainha-2025/.venv/share/jupyter/kernels/registry-cambrainha-2025
0 error(s)
pass  reproduce_cambrainha_2025.ipynb  (1837 s)
Fri Nov 27 12:21:39 UTC 2026
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t/show.py <<'EOF'
import json, sys
nb = json.load(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i in map(int, sys.argv[1:]):
    c = nb['cells'][i]
    print(f'===== cell {i}')
    for o in c.get('outputs', []):
        if 'text' in o: print(''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: print(''.join(o['data']['text/plain']))
EOF
python3 $TMPDIR/t/show.py 15 17 | grep -v Warning
```

```
===== cell 15
the ten surrogate windows of largest kurtosis (claim seed, active, passive and NNI (a)):
      path   phase       t0  n_units   N  n_silent  rate  cv_a  kappa_a  surr0_kappa_a
sub-545994 passive 5213.164      171  87        84 0.031 3.886   54.844         48.341
sub-545994 passive 5243.164      171  12       159 0.002 3.167   39.274         36.497
sub-510589  active 1167.614      227 182        45 0.170 0.529   22.664         34.292
sub-546508  active  688.268      157 131        26 0.117 2.621   39.485         26.940
sub-536211   nni_a 4620.421      148 131        17 0.131 0.748   27.362         25.817
sub-527294  active   93.203      206 199         7 0.138 1.643   36.763         22.891
sub-536211   nni_a 4680.421      148 130        18 0.133 0.738   36.293         19.474
sub-563326   nni_a 4769.350      167 150        17 0.126 0.815   26.761         18.879
sub-536211   nni_a 4830.421      148 127        21 0.118 0.770   28.371         18.622
sub-560962   nni_a 3628.930      183 157        26 0.124 0.474   20.914         17.540
surrogate windows above 15: 13 of 28335 ; in the active phase: 5
Spearman correlation of the surrogate kurtosis with N: -0.197 ; with the firing rate: -0.435


surrogate kurtosis by window set (cv a, no window is excluded under it):
 seed_offset     phases  windows     n   max  p999  p99  p95  median  min
           0     active      all 11639 34.29 10.43 6.51 5.06    3.64 2.80
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/t/show.py 25 27 28 31 32 | grep -v "Warning\|nanvar\|var = " | cut -c1-260
```

```
===== cell 25
cv auto O6  kappa_surr_max  grid_points        verdict  frac_pass  points_with_trials failures_within_SE  hr_scaling_lo  hr_noscaling_lo  hr_shuffled_lo  hr_scaling_hi  hr_noscaling_hi  trials_above_hi
 a    a  a          34.292            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN
 a    a  b          48.341            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN
 a    b  a          34.292            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN
 a    b  b          48.341            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN              NaN              NaN
 b    a  a           8.532           80 not_reproduced      0.675                80.0              False          0.641            0.600           0.691            1.0            0.602              7.0
 b    a  b          10.302           44     reproduced      1.000                44.0               True          0.778            0.601           0.723            1.0            0.602              7.0
 b    b  a           8.532           80 not_reproduced      0.662                80.0              False          0.647            0.602           0.692            1.0            0.604              7.0
 b    b  b          10.302           44     reproduced      1.000                44.0               True          0.778            0.603           0.733            1.0            0.604              7.0
 c    a  a          34.292            0        no grid        NaN                 NaN                NaN            NaN              NaN             NaN            NaN 
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/t/show.py 35 45 49 | grep -v "Warning\|nanvar\|var = \|gain = " | cut -c1-200 | tail -75
```

```
3000  c  a           15.73                     NaN
        3000  c  b           20.74                     NaN
        4000  a  a           35.46                     NaN
        4000  a  b           45.79                     NaN
        4000  b  a            8.60                   66.14
        4000  b  b            9.54                   66.14
        4000  c  a           35.46                     NaN
        4000  c  b           35.46                     NaN
points of the plotted gain outside -60 to 60 %: 0


largest gain over thresholds with at least 30 trials on each side:
cv auto  max_gain_pct  at_kappa  trials_above
 a    a         -1.19      9.85        1344.0
 a    b          0.85     20.80          43.0
 b    a         29.41     10.30          36.0
 b    b         29.05     10.30          36.0
 c    a         10.82     20.55          31.0
 c    b         10.10     20.55          31.0

[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/t/show.py 67 76 | grep -v "Warning\|nanvar\|var = " | grep -v "^ c \| b \(aa\|ab\|ba\|bb\)" | cut -c1-200 | head -60; python3 $TMPDIR/t/show.py 79 | grep -v "Warning\|nanvar\|var = " | tail -70
```

```
===== cell 67
mu windows with r^2 >= 0.85 (real): {'a': '0.017', 'b': '0.043', 'c': '0.999', 'd': '1.000'}
median r^2: {'a': 0.733, 'b': 0.759, 'c': 0.97, 'd': 0.986}

  phase cv  O9  sessions_mu  alpha_mean  beta_mean  mu_mean  z_mean  mu_sd  within
 active  a aac           97       1.481      0.760    1.062   0.156  0.072       1
 active  a aad           97       1.481      0.760    1.060   0.156  0.070       1
 active  a abc           97       1.481      0.740    1.062   0.156  0.072       1
 active  a abd           97       1.481      0.740    1.060   0.156  0.070       1
 active  a bac           97       1.442      0.769    1.062   0.099  0.072       2
 active  a bad           97       1.442      0.769    1.060   0.099  0.070       2
 active  a bbc           97       1.442      0.794    1.062   0.099  0.072       2
 active  a bbd           97       1.442      0.794    1.060   0.099  0.070       2
 active  c aac           97       1.482      0.760    1.059   0.156  0.069       1
 active  c aad           97       1.482      0.760    1.058   0.156  0.068       1
 active  c abc           97       1.482      0.740    1.059   0.156  0.069       1
 active  c abd           97       1.482      0.740    1.058   0.156  0.068       1
 active  c bac           97       1.442      0.769    1.059   0.099  0.069       2
 active  c bad           97       1.442      0.769    1.058   0.099  0.068       2
 active  c bbc           97       1.442      0.794    1.059   0.099  0.069       2
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/t/show.py 76 | tail -4; python3 $TMPDIR/t/show.py 82 64 | tail -12
```

```
/tmp/claude-1001/ipykernel_53/1857160491.py:36: Pandas4Warning: The 'lsuffix' and 'rsuffix' keywords in DataFrame.join are deprecated and will be removed in a future version. Use the 'suffixes' keyword instead.
  j = A_.join(Su_, rsuffix="_surr", how="inner")

===== cell 82
notebook run time: 30.5 min

===== cell 64
per-window fits: 64236 in 75 s
windows with a failed fit (NaN), per quantity, real windows:
{'beta_aa': 1, 'alpha_a': 1, 'z_a': 1, 'mu_a': 9, 'beta_ab': 54, 'mu_b': 14, 'beta_ba': 14, 'alpha_b': 14, 'z_b': 14, 'beta_bb': 69, 'mu_c': 9, 'mu_d': 14}
mu windows with r^2 >= 0.85 (real): reading a 0.017, reading b 0.043

session values computed: 192 (97 s)
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/t/show.py 76 | grep -i "paired\|verdicts"; date -u
```

```
verdicts over all readings: {'partially_reproduced': 144}
paired by session (97 sessions): alpha active - surrogate 0.413, p = 1.2e-17; beta -0.208, p = 1.2e-17
Fri Nov 27 12:22:24 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 -c "
import json;nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i in [0,8,23,29,33,36,46,50,68,77,80,81]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 0
# Reproducing Cambrainha et al. (2025) from dandiset 000713

Paper. Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), "Criticality at Work: Scaling in the Mouse Cortex Enhances Performance", PRX Life, doi:10.1103/w49n-2vz8. The claims file (`claims/cambrainha-2025.yaml`) was written from the arXiv preprint 2410.23508 version 2 (15 Sep 2025), with its Appendix and Supplemental Material; codes M1 to M8 and O1 to O11 below refer to the method notes at its top.

Dataset. DANDI:000713 (Allen Institute, Visual Behavior Neuropixels), version 0.240702.1725 (doi:10.48324/dandi.000713/0.240702.1725). The paper cites the Allen dataset (its ref. 60) without a DANDI version; this is the only published version of the dandiset, and its draft has not changed since (both modified 2024-07-02), so it is pinned as the most recent published version. The files are streamed from the archive; nothing is downloaded.

What is read. Per session file: the units table (peak channel, quality metrics, spike times of V1 units only), the electrodes table (structure of each channel), the stimulus presentation tables (stimulus blocks, image onsets and omitted flashes) and the trials table. The probe LFP files are not read.

| claim | tested or blocked |
|---|---|
| sessions-selected | tested |
| fig3a-kurtosis-broader-than-surrogate | tested |
| fig3c-scaling-hit-rate-higher | analysed; blocked (methods_underspecified) after the analysis |
| fig3c-hit-rate-rises-with-threshold | analysed; blocked (methods_underspecified) after the analysis |
| fig3d-relative-gain-24 | tested |
| figs1-other-window-lengths | tested |
| figs2-strict-units | tested |
| fig4a-active-most-scaling | analysed; blocked (methods_underspecified) after the analysis |
| fig4-exponents-active | tested |
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/t/show.py 79 | grep -A14 "cv a, start paper 7\|cv a, start p99,\|cv b, O6 a"
```

```
cv b, O6 a, every point of the grid from 8.55 to 12:
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
 b  active    alpha        1.495     0.063      48              0.028    True
 b  active     beta        0.748     0.082      48              0.035    True
 b  active       mu        1.438     0.114       0              0.000   False
 b  active        z        0.172     0.052      48              0.014    True
 b passive    alpha        1.473     0.058      61              0.033    True
 b passive     beta        0.757     0.075      61              0.013    True
 b passive       mu        1.335     0.139       0              0.000   False
 b passive        z        0.161     0.069      61              0.039    True
 b   nni_a    alpha        1.438     0.055      70              0.025    True
 b   nni_a     beta        0.819     0.066      70              0.017    True
 b   nni_a       mu        1.337     0.016       0              0.000   False
 b   nni_a        z        0.222     0.119      70              0.053    True

--
cv a, start paper 7, every point of the grid from 7.0 to 12:
cv   phase exponent  all_windows  sd_at_lo  points  largest_departure  within
 a  active    alpha        1.481     0.052     101              0.008    True
 a  active     beta        0.760     0.055     101              0.011    True
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; cat > $TMPDIR/t/md.py <<'PYEOF'
import json, uuid
p = 'reproduce_cambrainha_2025.ipynb'; nb = json.load(open(p)); C = nb['cells']
def setmd(i, start, text):
    assert ''.join(C[i]['source']).startswith(start), (i, ''.join(C[i]['source'])[:60])
    C[i]['source'] = text.strip('\n').splitlines(True)
def mdcell(text):
    return dict(cell_type='markdown', metadata={}, source=text.strip('\n').splitlines(True))

hdr = ''.join(C[0]['source'])
hdr = hdr.replace('| fig3c-scaling-hit-rate-higher | analysed; blocked (methods_underspecified) after the analysis |', '| fig3c-scaling-hit-rate-higher | tested |')
hdr = hdr.replace('| fig3c-hit-rate-rises-with-threshold | analysed; blocked (methods_underspecified) after the analysis |', '| fig3c-hit-rate-rises-with-threshold | tested |')
hdr = hdr.replace('| fig4a-active-most-scaling | analysed; blocked (methods_underspecified) after the analysis |', '| fig4a-active-most-scaling | tested |')
hdr = hdr.replace('| figs3-exponents-stable-with-threshold | analysed; blocked (methods_underspecified) after the analysis |', '| figs3-exponents-stable-with-threshold | tested |')
hdr = hdr.replace('| figs8-halves-and-phase-order | analysed; blocked (methods_underspecified) after the analysis |', '| figs8-halves-and-phase-order | tested |')
old = 'The dataset holds everything the claims need, so every claim was analysed. Five are blocked after the analysis because, under the readings adopted, their threshold grid starts at a surrogate maximum above the plotted range (see "How readings decide"). The outcomes are in the summary at the end.'
assert old in hdr
hdr = hdr.replace(old, 'The dataset holds everything the claims need, so every claim was tested. This is the revision after the first verification round: the five claims the first version blocked, because their threshold grid started at a surrogate maximum above the plotted range, are now judged on grids started at every threshold below it (see "How readings decide"), and the sections "The surrogate reference" and "Trial density" and the cells marked "Verifier round 1" add the outputs the verifier asked for. The outcomes are in the summary at the end.')
C[0]['source'] = hdr.splitlines(True)

s = ''.join(C[11]['source'])
old = s[s.index('Where the adopted reading leaves a criterion'):]
s = s.replace(old, '''The adopted reading of O6 (the largest surrogate kurtosis) puts kappa_surr_max at 34.29 in the active phase and 48.34 over all phases, above the plotted ranges, so the criteria's grids are empty. That maximum is set by a few surrogate windows (13 of 28335 above 15), not by windows with few active units (section "The surrogate reference"). For the claims judged on a grid from kappa_surr_max, the criterion is therefore also applied with the grid started at every threshold from 3 up to the top of the plotted range, and at four named starts: the paper's value of about 7 (M4, read from Figures 3C, 3D and 4A), the 99th and 99.9th percentiles of the active surrogate kurtoses, and the maximum over windows with at least 128 active units. Where every start gives the same outcome, that is the outcome, and the start does not matter. Where the starts disagree (figs3-exponents-stable-with-threshold), the paper's value of about 7 is adopted as an assumption.

The paper's surrogate reference (lowest kurtoses around 6, kappa_surr_max about 7) is far from the one computed here (minimum 2.80, median 3.64 in the active phase), and the correlation-matrix variant does not recover it either (section "The surrogate reference"). So the kurtosis computed here may differ from the paper's. This is tested directly by fig3a-kurtosis-broader-than-surrogate and stated as a question for the authors. The claims that compare windows above and below a kurtosis threshold are still judged, because the hit rate, phase order and exponent results here do not depend on where the threshold or the grid start is put (for example, under CV (a) the scaling hit rate is below the no-scaling hit rate at every threshold from 3 to 15). Their outcomes rest on the kurtosis of Eqs. 2 to 5 as printed being the paper's, and each says so.''')
C[11]['source'] = s.splitlines(True)

A_md = '''**Surrogate reference.** The largest surrogate kurtosis (34.29, active phase) comes from a window with 182 active units, a rate of 0.170 spikes per bin and a CV (a) of 0.53, so it is not a window with few units: leaving out windows with fewer than 64 or 128 active units leaves the active maximum at 34.29 (over all phases it falls from 48.34 to 34.29 with at least 128 units). Only 13 of 28335 surrogate windows lie above 15. The 99th percentile of the active surrogate kurtoses is 6.51 (6.51 to 6.75 over the five seeds) and the 99.9th 10.43 (10.43 to 13.38). With z-scored counts (the correlation matrix), the surrogate kurtoses are much higher (active minimum 4.09, 5th percentile 7.10, median 15.88, maximum 524.10) and overlap the real ones (median 22.07): a real window exceeds its own surrogate in 78.0% of active windows, against 99.0% with the covariance. Neither input gives lowest surrogate kurtoses of 6 +/- 0.6 together with a surrogate maximum near 7.'''
B_md = '''**Trial density.** Under O5 (a) an active window holds a median of 2 go trials with an outcome (mean 1.94), and 31.9% of windows hold three to five. Counting aborted trials as failures gives a median of 5 (mean 5.28; 60.4% of windows with three to five), as Appendix 5 describes, but an overall hit rate of 0.236; counting every trial gives 5 (5.58; 62.1%) and 0.223. Under either variant the scaling hit rate is above the no-scaling one at about half the thresholds from 3 to 15 (54.8% and 53.1%), higher at 8 (0.259 against 0.232 with aborted trials) and lower at 12 (0.184 against 0.237). Whether the paper counts aborted trials is asked of a reader (questions file); the claims are tested with O5 as written. With the correlation-input kurtosis, the scaling hit rate is above the no-scaling one at 16.4% of 805 thresholds over its 5th to 95th percentile.'''

setmd(29, '**Result: blocked', '''**Result: not reproduced**, resting on the CV reading (a), an assumption, and on the kurtosis of Eqs. 2 to 5 as printed. Under CV (a) and (c) the criterion's grid from kappa_surr_max (34.29) is empty; started at any threshold from 3 to 12.45 (190 starts, O5 (a) and (b)), it gives not reproduced at every start. From the paper's value of 7 the scaling hit rate exceeds both comparators at none of 111 points (CV (a), O5 (a)); at 7 it is 0.615 against 0.655 for no scaling and 0.605 trial-shuffled, and over thresholds 3 to 15 it is above both at none of 236 points (0.625 against 0.645 at 8, 0.591 against 0.642 at 12). Counting aborted trials or every trial (variants outside O5, asked of a reader) gives not reproduced at every start too (47.7% and 44.1% of points from 7). Only CV (b), which keeps 1937 of 11639 active windows and which the adopted reading rejects, passes: from 8.55 at 67.5% of 80 points (not reproduced) and from 10.30 (O6 (b)) at all 44 points (reproduced), with 7 trials above 12.5.''')
setmd(33, '**Result: blocked', '''**Result: not reproduced**, resting on CV (a), an assumption, and on the kurtosis of Eqs. 2 to 5 as printed. The criterion's grid is empty under CV (a) and (c); started at any threshold from 3 to 12.45, it gives not reproduced at all 190 starts. From the paper's value of 7 (CV (a), O5 (a)) the Spearman correlation is -0.248 and the scaling hit rate goes from 0.615 to 0.587; from 3 it is -0.64 (0.641 to 0.587). Under CV (c) from 7 the correlation is 0.205 but the rise, 0.002, is below the sum of the SEs (0.008 and 0.039). With aborted trials counted (a variant) the scaling hit rate falls from 0.261 at 7 to 0.174 at 12.5 (Spearman -0.998). Only CV (b) gives a rise (Spearman 0.917 from 8.55 and 0.784 from 10.30).''')
s = ''.join(C[36]['source']).rstrip('\n') + ' Over thresholds with at least 30 trials on each side, the largest gain is -1.19 % under CV (a) (0.85 % with O5 (b)), 10.82 % under CV (c) and 29.41 % under CV (b), at 10.30 with 36 trials above it; the last is within 24 +/- 3 % only to within its own SE, is not a reading of the criterion, and the gain at 12 under CV (b) is not compared on enough trials to settle the rise from 8 to 12. With aborted trials counted (a variant, printed under fig3c-scaling-hit-rate-higher) the gain is 11.72 % at 8 and -22.40 % at 12, at most 15.45 % from 7 to 12.5.'
C[36]['source'] = s.splitlines(True)
setmd(46, '**Result: blocked', '''**Result: not reproduced**, resting on CV (a), an assumption, and on the kurtosis of Eqs. 2 to 5 as printed. The criterion's grid from kappa_surr_max is empty under CV (a) and (c); started at any threshold from 3 to 14.95, it gives not reproduced at all 240 starts, under both NNI readings. From the paper's value of 7 the order active > passive > NNI holds at none of 161 points: the fractions above 7 are 0.311 active, 0.146 passive and 0.499 NNI (a), so the NNI phase has the most high-kurtosis windows, not the fewest, while active exceeds passive as the paper says. The median kurtosis of a session is higher in the active phase than in NNI (a) in only 16 of 97 sessions, and higher than in passive in 88. Where the criterion's own grid exists (CV (b)), the order holds at none of the points (0 of 130 and of 94).''')
setmd(50, '**Result: blocked', '''**Result: not reproduced**, resting on CV (a), an assumption, and on the kurtosis of Eqs. 2 to 5 as printed. Started at any threshold from 3 to 14.95, the criterion gives not reproduced at all 240 starts. From the paper's value of 7 (CV (a), NNI (a)) the first half is at or above the second at every point and the second half above passive at 98.8% of points, but passive lies above NNI at none. Median kurtosis (CV (a)): first half 6.389, second half 6.026 (Mann-Whitney p = 1.4e-42), passive 5.534, NNI 6.994 (a) and 7.216 (b). The second half is lower than the first, as the paper says, but the NNI phase has the highest kurtosis, not the lowest. Where the criterion's own grid exists (CV (b)), passive lies above NNI at none of the points.''')
s = ''.join(C[68]['source']).rstrip('\n') + ' Fitting mu over ranks 1 to K/2 only (variants (c) and (d), outside O9, asked for by the verifier), 99.9% and 100% of windows pass r^2 >= 0.85 and every session has a mu, but mu is 1.06 +/- 0.07 in the active phase, still above 0.73 +/- 0.08; with these variants at most two means are within tolerance (alpha and beta, with the K range (b)), so the outcome does not change.'
C[68]['source'] = s.splitlines(True)
s = ''.join(C[77]['source']).rstrip('\n') + ' Paired by session with its surrogate (Wilcoxon signed-rank, 97 sessions), alpha exceeds the surrogate value by 0.413 and beta falls short of it by 0.208, p = 1.2e-17 for each.'
C[77]['source'] = s.splitlines(True)
setmd(80, '**Result: blocked', '''**Result: not reproduced**, resting on CV (a) and on the grid start of 7, the paper's value of kappa_surr_max (M4), both assumptions. The criterion's grid from kappa_surr_max (34.29) is empty under CV (a) and (c). From 7 to 12 (101 points, every point evaluated), alpha and beta stay within one SD of their all-window values in every phase, mu in the active phase (largest departure 0.122 against an SD of 0.197), and z in the active and passive phases; in NNI (a), z departs by 0.083 against an SD of 0.058, and mu has no point with 10 sessions in the passive and NNI phases. Two exponents fail, so the claim is not reproduced. Counting an exponent with no evaluable point as passing would leave z alone failing, which gives partially reproduced. The starts disagree: from the 99th percentile (6.51) the outcome is the same, from the 99.9th (10.43) and under CV (b) only mu fails (partially reproduced).''')

s = ''.join(C[81]['source'])
for c in ['fig3c-scaling-hit-rate-higher', 'fig3c-hit-rate-rises-with-threshold', 'fig4a-active-most-scaling', 'figs3-exponents-stable-with-threshold', 'figs8-halves-and-phase-order']:
    a = f'| {c} | blocked: methods underspecified |'; assert a in s
    s = s.replace(a, f'| {c} | not reproduced (assumed) |')
old = 'The surrogate maximum is set by a few windows (34.29 in the active phase), which leaves the plotted threshold ranges above it empty.'
assert old in s
s = s.replace(old, 'The surrogate maximum is set by a few windows (34.29 in the active phase), which leaves the plotted threshold ranges above it empty; the claims judged on those grids are judged with the grid started at every threshold below it, and give the same outcome at every start except figs3-exponents-stable-with-threshold, where the paper\'s value of about 7 is adopted. The correlation matrix in place of the covariance does not recover the paper\'s surrogate kurtoses either.')
old = 'Active windows hold 0 to 4 go trials (median 2), not the "three to five" of the Appendix.'
assert old in s
s = s.replace(old, 'Active windows hold 0 to 4 go trials (median 2), not the "three to five" of the Appendix; counting aborted trials as failures gives a median of 5.')
C[81]['source'] = s.splitlines(True)

C.insert(18, mdcell(B_md))
C.insert(16, mdcell(A_md))
# cell ids for every cell lacking one
for c in C:
    if 'id' not in c:
        c['id'] = uuid.uuid4().hex[:8]
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
PYEOF
python3 $TMPDIR/t/md.py && python3 -c "
import json;nb=json.load(open('reproduce_cambrainha_2025.ipynb')); print(nb['nbformat'], nb['nbformat_minor'], len(nb['cells']))"
```

```
4 5 85
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
import json
p = 'reproduce_cambrainha_2025.ipynb'; nb = json.load(open(p)); C = nb['cells']
n = 0
for c in C:
    s = ''.join(c['source']); o = s
    s = s.replace(' and 29.41 % under CV (b), at 10.30 with 36 trials above it; the last is within 24 +/- 3 % only to within its own SE, is not a reading of the criterion, and the gain at 12 under CV (b) is not compared on enough trials to settle the rise from 8 to 12.', ' and 29.41 % under CV (b), at 10.30 with 36 trials above it, outside 24 +/- 3 %.')
    s = s.replace('j = A_.join(Su_, rsuffix="_surr", how="inner")', 'j = A_.merge(Su_, left_index=True, right_index=True, suffixes=("", "_surr"))')
    if s != o: n += 1; c['source'] = s.splitlines(True)
print(n)
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
EOF
cat README.md
```

```
2
# Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025) from dandiset 000713

Tests the findings of [Cambrainha et al. (2025)](https://doi.org/10.1103/w49n-2vz8), "Criticality
at Work: Scaling in the Mouse Cortex Enhances Performance", on
[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute Visual
Behavior Neuropixels data. For each 30-s window of V1 spiking it computes the kurtosis after
momentum-space coarse graining and an ISI-shuffled surrogate, relates it to the hit rate of the
change-detection task, compares the active, passive and non-natural image phases, and fits the
real-space renormalization exponents.

| Claim | Outcome |
|---|---|
| 62 sessions (44 mice) have more than 128 V1 units | Not reproduced |
| Kurtosis spans a broad range above the surrogates, lowest surrogates around 6 | Partially reproduced (assumed) |
| Hit rate over scaling windows is higher than over no-scaling windows and the shuffle | Blocked: methods underspecified |
| Hit rate over scaling windows rises with the threshold | Blocked: methods underspecified |
| Relative performance gain reaches 24% | Not reproduced |
| Similar results with 10-s and 60-s windows | Not reproduced |
| Similar results with strictly sorted units (43 sessions) | Not reproduced (assumed) |
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 - <<'EOF'
p='README.md'; s=open(p).read()
for a in ['| Hit rate over scaling windows is higher than over no-scaling windows and the shuffle | Blocked: methods underspecified |',
          '| Hit rate over scaling windows rises with the threshold | Blocked: methods underspecified |',
          '| More windows above threshold in active than passive than non-natural images | Blocked: methods underspecified |',
          '| Exponents stable with the kurtosis threshold | Blocked: methods underspecified |',
          '| Second half has lower kurtosis, non-natural images the lowest | Blocked: methods underspecified |']:
    assert a in s; s=s.replace(a, a.replace('Blocked: methods underspecified', 'Not reproduced (assumed)'))
old='''The surrogate maximum here is set by a few windows
(34.29), which leaves the threshold ranges of five claims empty; they are blocked, with every
reading shown in the notebook.'''
assert old in s
s=s.replace(old,'''The surrogate maximum here is set by a few windows
(34.29), which leaves the threshold ranges of five claims empty; they are judged with the range
started at every threshold below it, which gives the same outcome at every start for four of them,
and from the paper's value of about 7 for the fifth.''')
open(p,'w').write(s)
EOF
date -u
```

```
Fri Nov 27 12:23:59 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python3 -c "
import json;nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  for l in s.split('\n'):
    if ('blocked' in l.lower() or 'rather' in l or '—' in l) : print(i, l[:300])
"
```

```
0 | claim | tested or blocked |
0 The dataset holds everything the claims need, so every claim was tested. This is the revision after the first verification round: the five claims the first version blocked, because their threshold grid started at a surrogate maximum above the plotted range, are now judged on grids started at every t
```

**Agent calls Bash**

```bash
cd  date -u; timeout 4500 python tools/entry.py all entries/cambrainha-2025 2>&1 | grep -v "MissingID\|_validate" | tail -4 | cut -c1-300; date -u
```

```
Fri Nov 27 12:24:12 UTC 2026
Installed kernelspec registry-cambrainha-2025 in executed/cambrainha-2025/.venv/share/jupyter/kernels/registry-cambrainha-2025
0 error(s)
pass  reproduce_cambrainha_2025.ipynb  (1778 s)
Fri Nov 27 12:54:05 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']=='code':
    t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    for key in ['alternative grid starts','paired by session','verdicts:\n','exceeds their surrogate','scaling above no scaling at']:
      if key in t: j=t.index(key); print(i, t[j:j+250].replace('\n',' | '))
"
```

```
15 alternative grid starts: {'paper 7': 7.0, 'p99': 6.51, 'p99.9': 10.43, 'max N>=128': 34.29} |  | kurtosis at N/16 with covariance and with correlation input: |   phase                      kurtosis  min    p5  median   p95    max   iqr |  active      data, c
15 exceeds their surrogate's: 0.780; covariance input: 0.990 | Spearman correlation of the two real kurtoses across active windows: 0.39 | 
18 scaling above no scaling at 0.164 of 805 points; at the lowest point 0.640 against 0.657, at the highest 0.634 against 0.641 | 
78 paired by session (97 sessions): alpha active - surrogate 0.413, p = 1.2e-17; beta -0.208, p = 1.2e-17 | 
81 verdicts: | cv      start  kappa_start  grid_points              verdict failing |  a     O6 (a)       34.292            0              no grid     NaN |  a     O6 (b)       48.341            0              no grid     NaN |  b     O6 (a)        8.532
```

**Agent calls Bash**

```bash
cd  grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); awk '/^verifications:/,0' $f | head -60; grep -n "verifications\|proposed\|response\|agrees" tools/entry.py | head -30
```

```
attempts/amjad-2025-01.yaml
attempts/andrews-2024-01.yaml
attempts/armstrong-2026-01.yaml
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
      not in the archive.
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 395,450p tools/entry.py; grep -rn "verifications" schemas/ 2>/dev/null | head -5; ls schemas 2>/dev/null | head
```

```
if not any(tag in c.metadata.get("tags", []) for c in cells):
                        report.error(where, f"finding {n}: no cell tagged {tag!r} in {shown}")
        # A later review of an earlier attempt's findings (`findings_review`) rates those about the data, each once,
        # by its number in the record; an attempt that rates its own findings (pilot-18 on) has no such review.
        seen = set()
        for item in (attempt.get("findings_review") or {}).get("findings") or []:
            number, its = item["finding"], attempt.get("findings") or []
            if number > len(its) or number in seen:
                report.error(where, f"`findings_review` names finding {number} " + ("twice" if number in seen else
                                    f"and the record has {len(its)} findings"))
            elif its[number - 1].get("severity"):
                report.error(where, f"`findings_review` rates finding {number}, which the attempt rated itself")
            seen.add(number)
        # A verification round's review of a finding points at the finding by its number in the record.
        for r, rnd in enumerate(attempt.get("verifications") or [], 1):
            for item in rnd.get("findings") or []:
                if item["finding"] > len(attempt.get("findings") or []):
                    report.error(where, f"verification round {r} reviews finding {item['finding']}, and the record "
                                        f"has {len(attempt.get('findings') or [])} findings")
        # The latest round that reviewed a claim decides it; a third round may review only some. Round 1
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['verifications'],indent=1)[:3500])"
```

```
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
     "person",
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "import yaml; print(yaml.__version__)"; python3 -c "import ruamel.yaml" 2>&1 | tail -1; date -u
```

```
6.0.4
ModuleNotFoundError: No module named 'ruamel'
Fri Nov 27 12:54:44 UTC 2026
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "- claim: fig3c-scaling-hit-rate-higher\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig3c-scaling-hit-rate-higher\n  notes: The criterion's grid runs from kappa_surr_max to 12.5. Under the adopted CV reading (a),\n    kappa_surr_max is 34.29 (O6 (a)) or 48.34 (O6 (b)), and under (c) 34.29, so the grid is empty\n    and the criterion cannot be applied. The surrogate reference here (minimum 2.80, median 3.64,\n    maximum 34.29) is far from the paper's (lowest about 6, maximum about 7), so the procedures\n    differ, and the claim is blocked as the protocol asks for a reference far from the paper's.\n    Only CV reading (b), which keeps 1937 of 11639 active windows, gives a grid. From 8.55 the\n    scaling hit rate beats both comparators at 67.5% of 80 points (not reproduced); from 10.30\n    (O6 (b)) at all 44 points (reproduced), with 7 trials above 12.5. Under the seed variants that\n    reading gives partially reproduced (+1000, +4000), not reproduced (+2000) and no grid (+3000).\n    Over the thresholds 3 to 15 under CV (a), not the criterion's grid, the scaling hit rate is\n    above both comparators at none of 236 points (0.625 against 0.645 for no scaling at 8, 0.591\n    against 0.642 at 12; trial-shuffled 0.596 and 0.602). Trials placed by start time give 31.2%\n    of points under CV (b). Question for the authors. How is the kurtosis computed so that\n    surrogate windows give values of 6 or more, and is kappa_surr_max the maximum over every\n    surrogate window or a summary less sensitive to single windows?\n  deviations:\n  - Readings of method details (O2, O6) decide only where they agree, and otherwise the reading\n    the paper best supports is adopted (protocol, reader step 3 and author step 1.6), though the\n    criterion says reproduced under one reading. Taken as written, the criterion would give\n    reproduced, from CV (b) with O6 (b) alone, under the claim seed only.",
 "new_string": "- claim: fig3c-scaling-hit-rate-higher\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig3c-scaling-hit-rate-higher\n  notes: Under the adopted CV reading (a), and under (c), kappa_surr_max is 34.29 (O6 (a)) or 48.34\n    (O6 (b)), so the criterion's grid to 12.5 is empty. Started at any threshold from 3 to 12.45\n    (190 starts, CV (a) and (c), O5 (a) and (b)), the criterion gives not reproduced at every start,\n    so the outcome does not depend on where kappa_surr_max lies. From the paper's value of 7 (M4)\n    the scaling hit rate exceeds both comparators at none of 111 points (CV (a), O5 (a)); at 7 it\n    is 0.615 against 0.655 for no scaling and 0.605 trial-shuffled. Over the thresholds 3 to 15 it\n    is above both at none of 236 points (0.625 against 0.645 at 8, 0.591 against 0.642 at 12). The\n    99th and 99.9th percentiles of the active surrogate kurtoses (6.51 and 10.43) give 0 of 120 and\n    0 of 42 points. Counting aborted trials as failures, or every trial (variants outside O5, asked\n    of a reader), gives not reproduced at every start as well (47.7% and 44.1% of points from 7).\n    Only CV reading (b), which keeps 1937 of 11639 active windows, gives the criterion's own grid.\n    From 8.55 the scaling hit rate beats both comparators at 67.5% of 80 points (not reproduced);\n    from 10.30 (O6 (b)) at all 44 points (reproduced), with 7 trials above 12.5. Under the seed\n    variants that reading gives partially reproduced (+1000, +4000), not reproduced (+2000) and no\n    grid (+3000). Trials placed by start time give 31.2% of points under CV (b). The outcome rests\n    on the kurtosis of Eqs. 2 to 5 as printed, whose surrogate reference here (minimum 2.80, median\n    3.64) is far from the paper's (lowest about 6, maximum about 7); see the findings.\n  deviations:\n  - CV readings disagree (b gives reproduced from 10.30, a and c not reproduced at every start);\n    reading (a) is adopted as an assumption, as for fig3a-kurtosis-broader-than-surrogate.\n  - The grid from kappa_surr_max (O6) is empty under CV (a) and (c); the criterion is applied with\n    the grid started at every threshold from 3 to 12.45, and gives the same outcome at each.\n  - The surrogate reference computed here is far from the paper's. The claim is still judged, not\n    blocked, because its result is the same at every threshold and every grid start; the\n    difference in the kurtosis itself is judged by fig3a-kurtosis-broader-than-surrogate."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "- claim: fig3c-hit-rate-rises-with-threshold\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig3c-hit-rate-rises-with-threshold\n  notes: Blocked for the reason of fig3c-scaling-hit-rate-higher; under CV (a) and (c) the grid\n    from kappa_surr_max to 12.5 is empty. Under CV (b) the scaling hit rate rises (Spearman 0.917\n    from 8.55 and 0.784 from 10.30, rises of 0.359 and 0.222 against SE sums of 0.039 and 0.073;\n    reproduced, and so under four seed variants, with no grid under +3000). Over 3 to 12.5 under\n    CV (a), a variant, the Spearman correlation is -0.64 and the hit rate falls from 0.641 to 0.587.\n  deviations:\n  - As for fig3c-scaling-hit-rate-higher.",
 "new_string": "- claim: fig3c-hit-rate-rises-with-threshold\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig3c-hit-rate-rises-with-threshold\n  notes: Under CV (a) and (c) the grid from kappa_surr_max to 12.5 is empty; started at any\n    threshold from 3 to 12.45, the criterion gives not reproduced at all 190 starts (O5 (a) and\n    (b)). From the paper's value of 7 (CV (a), O5 (a)) the Spearman correlation is -0.248 and the\n    scaling hit rate goes from 0.615 to 0.587; from 3 it is -0.64 (0.641 to 0.587). Under CV (c)\n    from 7 the correlation is 0.205 but the rise, 0.002, is below the sum of the SEs (0.008 and\n    0.039). With aborted trials counted as failures (a variant outside O5) the scaling hit rate\n    falls from 0.261 at 7 to 0.174 at 12.5 (Spearman -0.998). Under CV (b) the scaling hit rate\n    rises (Spearman 0.917 from 8.55 and 0.784 from 10.30, rises of 0.359 and 0.222 against SE sums\n    of 0.039 and 0.073; reproduced, and so under four seed variants, with no grid under +3000).\n  deviations:\n  - As for fig3c-scaling-hit-rate-higher."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "- claim: fig4a-active-most-scaling\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig4a-active-most-scaling\n  notes: Under the adopted readings (CV (a), O6 (b)) the grid from kappa_surr_max (48.34) to 15 is\n    empty, as under every reading of CV (a) and (c), for the reason given under\n    fig3c-scaling-hit-rate-higher. Where a grid exists (CV (b)), the order active > passive > NNI\n    holds at none of the points (0 of 130 and of 94). Over 3 to 15 under CV (a), a variant, the NNI fraction is above the active one\n    at every printed threshold from 5 (0.895 against 0.848 at 5, 0.321 against 0.167 at 8), and\n    active is above passive. The median kurtosis of a session is higher in the active phase than\n    in NNI (a) in 16 of 97 sessions and higher than in the passive phase in 88.",
 "new_string": "- claim: fig4a-active-most-scaling\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:fig4a-active-most-scaling\n  notes: Under the adopted readings (CV (a), O6 (b)) the grid from kappa_surr_max (48.34) to 15 is\n    empty, as under every reading of CV (a) and (c). Started at any threshold from 3 to 14.95, the\n    criterion gives not reproduced at all 240 starts, under CV (a) and (c) and both NNI readings.\n    From the paper's value of 7 the order active > passive > NNI holds at none of 161 points; the\n    fractions above 7 are 0.311 active, 0.146 passive and 0.499 NNI (a). Over 3 to 15 the NNI\n    fraction is above the active one at every printed threshold from 5 (0.895 against 0.848 at 5,\n    0.321 against 0.167 at 8), and active is above passive. The median kurtosis of a session is\n    higher in the active phase than in NNI (a) in 16 of 97 sessions and higher than in the passive\n    phase in 88. Where the criterion's own grid exists (CV (b)), the order holds at none of the\n    points (0 of 130 and of 94)."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "- claim: figs8-halves-and-phase-order\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs8-halves-and-phase-order\n  notes: Blocked for the grid, as fig4a-active-most-scaling. Where a grid exists (CV (b)), the\n    second half lies above passive at every point, passive above NNI at none, and the first half at\n    or above the second at 60 to 68% of points. Median kurtosis (CV (a)), first half 6.389, second",
 "new_string": "- claim: figs8-halves-and-phase-order\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs8-halves-and-phase-order\n  notes: The grid from kappa_surr_max is empty under CV (a) and (c); started at any threshold from 3\n    to 14.95, the criterion gives not reproduced at all 240 starts. From the paper's value of 7\n    (CV (a), NNI (a)) the first half is at or above the second at every point and the second half\n    above passive at 98.8% of points, but passive lies above NNI at none. Where the criterion's own\n    grid exists (CV (b)), the second half lies above passive at every point, passive above NNI at\n    none, and the first half at or above the second at 60 to 68% of points. Median kurtosis (CV\n    (a)), first half 6.389, second"
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "- claim: figs3-exponents-stable-with-threshold\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs3-exponents-stable-with-threshold\n  notes: Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty, for the reason\n    given under fig3c-scaling-hit-rate-higher. Under CV (b) (grids from 8.55 and 10.35) alpha, beta\n    and z stay within one SD of their all-window values in every phase, and mu has no point with 10\n    sessions. On thresholds 4 to 12 under CV (a), a variant, alpha and beta stay within one SD in\n    every phase, mu and z in the active and passive phases; in NNI z departs by 0.083 against an SD\n    of 0.056 and mu has no point with 10 sessions.\n  deviations:\n  - The grid was evaluated at every tenth point of the 0.05 grid, to keep the run short.",
 "new_string": "- claim: figs3-exponents-stable-with-threshold\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_cambrainha_2025.ipynb\n  output: claim:figs3-exponents-stable-with-threshold\n  notes: Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty. From the paper's\n    value of 7 to 12 (CV (a), 101 points, every point evaluated), alpha and beta stay within one SD\n    of their all-window values in every phase, mu in the active phase (largest departure 0.122\n    against an SD of 0.197) and z in the active and passive phases. In NNI (a) z departs by 0.083\n    against an SD of 0.058, and mu has no point with 10 sessions in the passive and NNI phases. Two\n    exponents fail, so not reproduced. Counting an exponent with no evaluable point as passing\n    would leave z alone failing (partially reproduced). The 99th percentile start (6.51) gives the\n    same as 7; the 99.9th percentile start (10.43), and CV (b) from 8.55 and 10.30, fail for mu alone\n    (partially reproduced), as z stays within one SD there. On thresholds 4 to 12 in steps of 0.5\n    (CV (a)) NNI z departs by 0.083 against an SD of 0.056.\n  deviations:\n  - The grid from kappa_surr_max (O6) is empty under CV (a) and (c). The grid starts disagree (7 and\n    the 99th percentile give not reproduced, the 99.9th percentile partially reproduced), so the\n    paper's value of about 7 for kappa_surr_max, read from Figures 3C, 3D and 4A (claims file, M4),\n    is adopted as an assumption.\n  - CV reading (a) is adopted as an assumption, as for fig3a-kurtosis-broader-than-surrogate.\n  - An exponent with no grid point where 10 sessions contribute is counted as not shown stable."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    two poolings of O3 give identical values (psi has unit variance per unit, so the pooled\n    kurtosis is the mean of the unit kurtoses).",
 "new_string": "    two poolings of O3 give identical values (psi has unit variance per unit, so the pooled\n    kurtosis is the mean of the unit kurtoses). The largest surrogate window (34.29) has 182 active\n    units, a rate of 0.170 spikes per bin and a CV (a) of 0.53; leaving out windows with fewer than\n    64 or 128 active units leaves the active maximum at 34.29, and 13 of 28335 surrogate windows lie\n    above 15. The 99th and 99.9th percentiles of the active surrogate kurtoses are 6.51 and 10.43.\n    With z-scored counts (the correlation matrix in place of the covariance of Eq. 2, a variant the\n    verifier asked for) the active surrogate kurtoses have a minimum of 4.09, a 5th percentile of\n    7.10, a median of 15.88 and a maximum of 524.10, and overlap the real ones (median 22.07; a real\n    window exceeds its surrogate in 78.0% of windows); neither input recovers lowest surrogate\n    kurtoses of 6 +/- 0.6 together with a maximum near 7."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    ranges from -26.88% to -1.19%, with bootstrap SEs of 1.2% to 7.8% at the printed thresholds.",
 "new_string": "    ranges from -26.88% to -1.19%, with bootstrap SEs of 1.2% to 7.8% at the printed thresholds.\n    Over thresholds with at least 30 trials on each side, the largest gain is -1.19% under CV (a)\n    (0.85% with O5 (b)), 10.82% under CV (c) and 29.41% under CV (b), at 10.30 on 36 trials. With\n    aborted trials counted as failures (a variant outside O5) the gain is 11.72% at 8 and -22.40%\n    at 12, at most 15.45% from 7 to 12.5."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    mu and z under none. Surrogate windows give alpha 1.068 and beta 0.968.",
 "new_string": "    mu and z under none. Surrogate windows give alpha 1.068 and beta 0.968. Fitting mu over ranks 1\n    to K/2 only (variants outside O9, asked for by the verifier), 99.9% of windows pass the r^2 rule\n    and every session has a mu, but mu is 1.062 +/- 0.072, still outside 0.73 +/- 0.08; at most two\n    means are within tolerance with these variants too."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    passive and 0.192 NNI, so it does not move away from 0 from active to passive. The surrogate\n    exponents use the claim seed of the fig3a surrogate only; the Wilcoxon reading needs no\n    surrogate and gives the same outcome.",
 "new_string": "    passive and 0.192 NNI, so it does not move away from 0 from active to passive. The surrogate\n    exponents use the claim seed of the fig3a surrogate only; the Wilcoxon reading needs no\n    surrogate and gives the same outcome. Paired by session with its surrogate (Wilcoxon\n    signed-rank, 97 sessions), alpha exceeds the surrogate value by 0.413 and beta falls short of it\n    by 0.208, p = 1.2e-17 for each."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the findings statements.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    matched. Question for the authors. What exactly is pooled and normalised when the kurtosis is\n    computed (Eq. 5 prints phi_i inside the sum), and how are silent units handled?",
 "new_string": "    matched. With z-scored counts (the correlation matrix) the surrogate kurtoses are higher\n    (minimum 4.09, median 15.88, maximum 524.10 in the active phase) and overlap the real ones, so\n    that reading does not match either. Question for the authors. What exactly is pooled and\n    normalised when the kurtosis is computed (Eq. 5 prints phi_i inside the sum), is the covariance\n    or the correlation matrix diagonalised, and how are silent units handled?"
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "  statement: The surrogate maximum kappa_surr_max (about 7 in Figure 3) is, as defined here, set by a\n    few windows (34.29 in the active phase, 24.45 to 35.46 over seeds), which leaves every plotted\n    threshold range empty and blocks five claims. Question for the authors. Is kappa_surr_max the\n    maximum over every surrogate window of all sessions, one surrogate per window, or another\n    summary?",
 "new_string": "  statement: The surrogate maximum kappa_surr_max (about 7 in Figure 3) is, as defined here, set by a\n    few windows (34.29 in the active phase, 24.45 to 35.46 over seeds; 13 of 28335 surrogate windows\n    above 15), which leaves every plotted threshold range empty. The windows that set it are not\n    windows with few active units. Five claims are judged with the range started at every threshold\n    below it. Question for the authors. Is kappa_surr_max the maximum over every surrogate window of\n    all sessions, one surrogate per window, or another summary?"
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    windows pass here, for the fit pooled over K >= 16). Here alpha and beta come out near\n    the paper's values (1.48 and 0.76 active), mu about twice (1.58) and z about half (0.16).",
 "new_string": "    windows pass here, for the fit pooled over K >= 16). Here alpha and beta come out near\n    the paper's values (1.48 and 0.76 active), mu about twice (1.58) and z about half (0.16).\n    Fitted over ranks 1 to K/2 only, mu passes the r^2 rule in 99.9% of windows and is 1.06."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    Appendix 5 says three to five trials are performed in each window; the paper's count may\n    include aborted or catch trials.",
 "new_string": "    Appendix 5 says three to five trials are performed in each window. Counting aborted trials as\n    well gives a median of 5 per window (60.4% of windows with three to five), so the paper's count\n    may include aborted trials; the files do not say which trials the paper counted."
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> attempts/cambrainha-2025-01.yaml <<'EOF'
verifications:
- date: 2026-11-27
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module criticality.py and the claims file, with the paper's full text. The verifier tested the
    helpers on synthetic data and checked the session files on the DANDI API. Report in
    transcripts/cambrainha-2025/verifier-1-report.md.
  results:
  - claim: sessions-selected
    agrees: true
    outcome: not_reproduced
    reason: All V1 units give 97 sessions and 68 mice with more than 128 units (98 with at least
      128); the default quality filters give 1 session. The paper has 62 sessions and 44 mice, and no
      reading of the criterion lands within tolerance. The verifier confirmed 153 session files from
      81 subjects on the DANDI API. Every downstream claim runs on 97 sessions and 68 mice, not the
      paper's 62 and 44; this follows the claims file's main reading, but no reading recovers the
      paper's set.
    response: No change. The analysis set stays the claims file's main reading (O1 (a)); the
      difference is a finding (selection_undocumented) and is stated in the summary.
  - claim: fig3a-kurtosis-broader-than-surrogate
    agrees: true
    outcome: partially_reproduced
    reason: The real windows spread more than the surrogates (IQR 1.98 against 0.64) and some exceed
      kappa_surr_max (89.8 against 34.3). The lowest surrogate kurtoses are 2.80 (minimum) and 3.16
      (5th percentile), against 6 +/- 0.6, which matches the criterion's partial clause; the majority
      condition fails. The surrogate chance level (2.8 to 3.6) does not match the paper's (about 6);
      on independent Poisson data the helper gives 3.1 to 3.5 with covariance input and 3.7 to 6.7
      with z-scored input, a reading that was never run. The notebook never identifies which windows
      set the maximum, which is set by the single largest of 11639 surrogate values (only 5 above
      15) and swings between 24 and 35 across seeds.
    response: Added the section "The surrogate reference". The largest surrogate window has 182
      active units (rate 0.170, CV 0.53); dropping windows with fewer than 64 or 128 units leaves the
      active maximum at 34.29. The kurtosis with z-scored input is now computed for every window and
      its surrogate (helper, `kappa_z`); it gives surrogate kurtoses of 4.09 (minimum), 7.10 (5th
      percentile) and 15.88 (median), overlapping the real ones, so it does not recover the paper's
      reference either. Outcome unchanged.
  - claim: fig3c-scaling-hit-rate-higher
    agrees: false
    outcome: not_reproduced
    reason: Under the adopted CV reading (a) the scaling hit rate is below the no-scaling hit rate at
      all 236 thresholds from 3 to 15 (0.615 against 0.655 at 7, 0.591 against 0.642 at 12), so any
      kappa_surr_max up to 12.5, including the paper's value of about 7, fails the test. The grid is
      empty only because of a few outlier surrogate windows. Only CV reading (b), which drops 83% of
      windows, passes. The blocking on kappa_surr_max rests on the single largest surrogate value,
      and the notebook applies the chance-level mismatch inconsistently, blocking five claims for it
      while testing fig3d, figs1, figs2 and figs7, which use the same kurtosis.
    response: Changed to not_reproduced, as the verifier gives. The criterion is now applied with the
      grid started at every threshold from 3 to 12.45 and at the paper's 7, the 99th and 99.9th
      surrogate percentiles and the maximum over windows with at least 128 units; every start gives
      not reproduced under CV (a) and (c). Variants counting aborted trials, or every trial, give the
      same. The claims that use the kurtosis are now treated alike, all tested.
  - claim: fig3c-hit-rate-rises-with-threshold
    agrees: false
    outcome: not_reproduced
    reason: Under CV (a) from 3 to 12.5 the Spearman correlation is -0.64 and the hit rate falls
      from 0.641 to 0.587. From 7 to 12 it is flat at 0.615 to 0.630, then drops to 0.591.
    response: Changed to not_reproduced. Every start from 3 to 12.45 gives not reproduced under CV (a)
      and (c); from 7 the Spearman correlation is -0.248 (CV (a)), and under CV (c) the rise of 0.002
      is below the sum of its SEs.
  - claim: fig3d-relative-gain-24
    agrees: true
    outcome: not_reproduced
    reason: Under CV (a) the largest gain over all thresholds is -1.19%, and the gain at 12 (-7.9%)
      is below that at 8 (-3.0%). No reading gives 24 +/- 3% together with a rise from 8 to 12.
      Reading (b) of the maximum picks points with 2 to 21 trials (54.9% at 39.5 from 2 trials;
      infinite under CV (b)), though none is within tolerance either way.
    response: Added the largest gain over thresholds with at least 30 trials on each side (-1.19% CV
      (a), 10.82% CV (c), 29.41% CV (b), all outside tolerance), and the gain with aborted trials
      counted (11.72% at 8, -22.40% at 12). Outcome unchanged.
  - claim: figs1-other-window-lengths
    agrees: true
    outcome: not_reproduced
    reason: Neither the 10-s nor the 60-s windows pass under any reading. 60-s gains at 12 are -8.1%
      and -3.6% (CV (a)); the 10-s onset is 10.55.
    response: No change.
  - claim: figs2-strict-units
    agrees: true
    outcome: not_reproduced
    reason: Session counts are 68 (good units) and 1 (default filters), against 43 +/- 4.3. Under CV
      (a) on good units, the gain at 12 is -15.9%.
    response: No change.
  - claim: fig4a-active-most-scaling
    agrees: false
    outcome: not_reproduced
    reason: The NNI phase has the most high-kurtosis windows, not the fewest; at 7 the fractions
      above are NNI 0.50, active 0.31, passive 0.15. Only 16 of 97 sessions have a higher median
      kurtosis in active than in NNI. Under CV (b), where a grid exists, the order holds at 0% of
      points.
    response: Changed to not_reproduced. Every start from 3 to 14.95 gives not reproduced, under CV
      (a) and (c) and both NNI readings.
  - claim: fig4-exponents-active
    agrees: true
    outcome: not_reproduced
    reason: At most 2 of 4 means fall within tolerance; mu is 1.43 to 1.57 (paper 0.73) and z 0.10 to
      0.17 (paper 0.3 +/- 0.1). Both claims-file readings of mu fit ranks 1 to K, which includes the
      noise floor of the spectrum; only 1.7% (a) or 4.3% (b) of windows reach r^2 >= 0.85, so mu
      rests on 44, 18 and 7 sessions (active, passive, NNI). If mu fell within tolerance the claim
      would become partially reproduced, as alpha (reading b) and beta already are within.
    response: Added mu fitted over ranks 1 to K/2 (helper, mu variants (c) and (d)). 99.9% of windows
      then pass the r^2 rule, but mu is 1.062 in the active phase, outside 0.73 +/- 0.08, and at most
      two means are within tolerance, so the outcome is unchanged. The fit range is asked of a reader
      (questions file).
  - claim: fig4-exponents-passive
    agrees: true
    outcome: not_reproduced
    reason: 48 of 48 readings fail, with at most 1 mean within tolerance. Passive z is not higher than
      active (0.152 against 0.156, p = 0.37).
    response: No change; with mu over ranks 1 to K/2 passive mu is 0.964, outside 0.61 +/- 0.05.
  - claim: fig4-exponents-nni
    agrees: true
    outcome: not_reproduced
    reason: 96 of 96 readings fail, with at most 1 mean within tolerance; mu is about 1.33 against
      0.38.
    response: No change; with mu over ranks 1 to K/2 NNI mu is 0.945, outside 0.38 +/- 0.04.
  - claim: fig4bc-static-exponents-trend
    agrees: true
    outcome: partially_reproduced
    reason: Holds the same way under all 144 readings. Active alpha and beta differ from trivial (p
      about 1e-17), and the alpha and beta orderings hold; the z ordering fails (active 0.156 above
      passive 0.152). Test (a) compares active and surrogate session values as unpaired, although
      they come from the same windows; the p-values are tiny either way.
    response: Added the paired Wilcoxon signed-rank test (97 sessions, p = 1.2e-17 for alpha and
      beta). Outcome unchanged.
  - claim: figs3-exponents-stable-with-threshold
    agrees: true
    outcome: blocked
    reason: Here the start of the threshold grid changes the outcome, and no grid from the paper's
      value of about 7 was run under the adopted readings. Under CV (b) (8.55 to 12) alpha, beta and
      z are stable but mu has fewer than 10 sessions. On the CV (a) variant grid 4 to 12, NNI z
      departs by 0.084 against an SD of 0.056. stable_eval evaluates every 10th grid point, not every
      point as the criterion says.
    response: Changed to not_reproduced, resting on the grid start of 7 (the claims file's M4) as an
      assumption. Every grid point is now evaluated. From 7 to 12 under CV (a), NNI z departs by
      0.083 against an SD of 0.058 and mu has no point with 10 sessions in the passive and NNI
      phases; the 99th percentile start gives the same, the 99.9th percentile start partially
      reproduced (mu alone).
  - claim: figs4-initial-kurtosis-poor-predictor
    agrees: true
    outcome: reproduced
    reason: Spearman 0.18 for the active phase and 0.19 for all phases pooled, both below 0.3.
    response: No change.
  - claim: figs5a-firing-rate-order
    agrees: true
    outcome: reproduced
    reason: Under CV (a), active < NNI < passive at 141 of 141 points, with rho of -0.976 or lower in
      every phase.
    response: No change.
  - claim: figs5c-hit-rate-firing-rate-nonmonotonic
    agrees: true
    outcome: reproduced
    reason: The below-threshold hit rate rises from 0.601 to 0.751, then falls to 0.654, with SEs of
      0.037 or less, under every reading and every seed. boot_curves uses 10^4 Poisson-bootstrap
      resamples in place of 10^5 resamples with replacement; this is stated, and the SEs only set
      margins.
    response: No change; the bootstrap stays as stated in the deviations.
  - claim: figs7-fatigue-halves
    agrees: true
    outcome: not_reproduced
    reason: Under CV (a) the gains are negative in both halves (first half -8.0% and -11.2%, second
      half -6.8% and -20.3% at 8 and 12). Only CV (b) passes, with 4 to 6 trials above 12. Every
      hit-rate claim depends on the trial density, which is 0 to 4 per window (median 2) under the
      go hit or miss reading against the paper's three to five; about 682 trials per session over
      120 windows would give about 5.7, so the paper may have counted more trials, for example
      aborted trials as failures, which O5 offers no reading for.
    response: Added the section "Trial density". Counting aborted trials as failures gives a median
      of 5 trials per window, as Appendix 5 says, and an overall hit rate of 0.236; under it the
      fig3c and fig3d tests still fail. O5 is asked of a reader (questions file); outcomes are
      tested on O5 as written. Outcome unchanged.
  - claim: figs8-halves-and-phase-order
    agrees: false
    outcome: not_reproduced
    reason: The passive > NNI condition fails, median kurtosis being 5.53 for passive and 6.99 for
      NNI (a); under CV (b) passive exceeds NNI at 0% of points.
    response: Changed to not_reproduced. Every start from 3 to 14.95 gives not reproduced; passive
      lies above NNI at no point.
EOF
mkdir -p questions; cat > questions/cambrainha-2025.yaml <<'EOF'
dandiset: "000713"
paper: doi:10.1103/w49n-2vz8
questions:
- claim: fig3c-scaling-hit-rate-higher
  asked: 2026-11-27
  question: O5 reads the trials of Eqs. 11 and 12 as go trials with outcome hit or miss, leaving out
    catch and aborted trials. With that reading an active 30-s window holds a median of 2 trials (0
    to 4), where Appendix 5 says three to five; counting aborted trials as failures gives a median of
    5. Does "total number of tasks" in Eqs. 11 and 12 include aborted trials (or every trial), so
    that O5 should name that reading? The question bears on every hit-rate claim (fig3c-scaling-hit-rate-higher,
    fig3c-hit-rate-rises-with-threshold, fig3d-relative-gain-24, figs1-other-window-lengths,
    figs2-strict-units, figs5c-hit-rate-firing-rate-nonmonotonic, figs7-fatigue-halves).
  passage: Within each 30-s window only three to five trials are performed, leading to poor
    statistical estimation of performance on a window-to-window basis. (Appendix 5, Hit rate); Hit
    rate (Scaling) = Total number of sucessful tasks (windows with kappa > kappa_th) / Total number of
    tasks (windows with kappa > kappa_th) (Eq. 11)
  why: Counting aborted trials as failures lowers the overall hit rate from 0.641 to 0.236 and
    changes the hit-rate curves. Here it does not change the outcome of fig3c-scaling-hit-rate-higher
    (not reproduced at every grid start), but it moves the relative gain at kappa 8 from -2.99% to
    11.72%, so it could change the outcome of other hit-rate claims in another attempt.
- claim: fig4-exponents-active
  asked: 2026-11-27
  question: Both readings of mu in O9 fit the within-cluster spectrum over ranks 1 to K, which takes
    in the noise floor of the spectrum, and only 1.7% (a) or 4.3% (b) of windows then pass the r^2 of
    0.85 that the paper uses to discard poor fits. Does the paper's fit of Eq. 9 cover the whole
    spectrum, or only its upper ranks (for example ranks up to K/2, as in other phenomenological
    renormalization analyses), so that O9 should name that reading? The question bears on
    fig4-exponents-active, fig4-exponents-passive, fig4-exponents-nni and
    figs3-exponents-stable-with-threshold.
  passage: The spectrum of eigenvalues of the covariance matrix [Eq. 2] when ordered in descending
    order should follow lambda = A (K/rank)^mu. (Eq. 9) ... Time windows with a fit quality of r2 <
    0.85 for this power-law have their corresponding exponent discarded (Appendix 4c)
  why: With ranks 1 to K/2, 99.9% of windows pass the r^2 rule and mu is 1.06 in the active phase,
    against 1.58 under reading (a) and 0.73 in the paper. Here it does not change any outcome, as mu
    stays outside tolerance, but it decides how many sessions carry a mu, which matters for the
    session counts of the mu tests and for figs3-exponents-stable-with-threshold, where mu has no
    threshold with 10 sessions under the claims file's readings.
EOF
python3 -c "import yaml; yaml.safe_load(open('attempts/cambrainha-2025-01.yaml')); yaml.safe_load(open('questions/cambrainha-2025.yaml')); print('ok')"; date -u
```

```
ok
Fri Nov 27 12:56:44 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
for f in ['attempts/cambrainha-2025-01.yaml','questions/cambrainha-2025.yaml']:
    d = yaml.safe_load(open(f))
    def walk(x, path=''):
        if isinstance(x, dict):
            for k, v in x.items(): walk(v, path + '.' + str(k))
        elif isinstance(x, list):
            for i, v in enumerate(x): walk(v, path + f'[{i}]')
        elif isinstance(x, str):
            for bad in [': ', '—', 'rather']:
                if bad in x: print(f, path, repr(bad), x[max(0, x.index(bad)-40):x.index(bad)+20])
    walk(d)
EOF
python tools/entry.py check entries/cambrainha-2025 2>&1 | tail -15
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  git diff --stat; grep -n "outcome: \|assumed" attempts/cambrainha-2025-01.yaml | head -40; ls tools | grep -i valid
```

```
attempts/cambrainha-2025-01.yaml                   |  347 +++++--
 entries/cambrainha-2025/README.md                  |   15 +-
 entries/cambrainha-2025/criticality.py             |   54 +-
 .../reproduce_cambrainha_2025.ipynb                |  561 ++++++++++-
 tools/agent_run.py                                 |   22 +-
 tools/author_notes.py                              |    4 +-
 tools/blind.sh                                     |    2 +-
 tools/build_site.py                                | 1005 ++++++++++++++++----
 tools/colab.py                                     |    6 +-
 tools/conversion_issue.py                          |    2 +-
 tools/entry.py                                     |   29 +
 tools/get_papers.sh                                |    8 +-
 tools/notify.py                                    |    4 +-
 tools/paper_match.py                               |   15 +-
 tools/papers_manifest.py                           |    2 +-
 tools/runner/chain.sh                              |   39 +-
 tools/runner/cutover_paper_first.py                |    2 +-
 tools/runner/merge_claims.sh                       |    1 +
 tools/runner/merge_match.sh                        |    2 +
 tools/runner/run_requests.py                       |    2 +-
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff attempts/cambrainha-2025-01.yaml | head -60
```

```
diff --git a/attempts/cambrainha-2025-01.yaml b/attempts/cambrainha-2025-01.yaml
index 35c3871..bc543bb 100644
--- a/attempts/cambrainha-2025-01.yaml
+++ b/attempts/cambrainha-2025-01.yaml
@@ -54,7 +54,15 @@ outcomes:
     pooled give the same. Over the five seeds kappa_surr_max is 34.29, 25.15, 25.47, 24.45 and
     35.46 and the minimum 2.80, 2.57, 2.55, 2.82 and 2.83; the outcome is the same under each. The
     two poolings of O3 give identical values (psi has unit variance per unit, so the pooled
-    kurtosis is the mean of the unit kurtoses).
+    kurtosis is the mean of the unit kurtoses). The largest surrogate window (34.29) has 182 active
+    units, a rate of 0.170 spikes per bin and a CV (a) of 0.53; leaving out windows with fewer than
+    64 or 128 active units leaves the active maximum at 34.29, and 13 of 28335 surrogate windows lie
+    above 15. The 99th and 99.9th percentiles of the active surrogate kurtoses are 6.51 and 10.43.
+    With z-scored counts (the correlation matrix in place of the covariance of Eq. 2, a variant the
+    verifier asked for) the active surrogate kurtoses have a minimum of 4.09, a 5th percentile of
+    7.10, a median of 15.88 and a maximum of 524.10, and overlap the real ones (median 22.07; a real
+    window exceeds its surrogate in 78.0% of windows); neither input recovers lowest surrogate
+    kurtoses of 6 +/- 0.6 together with a maximum near 7.
   deviations:
   - CV readings disagree (a and b partially reproduced, c not reproduced); reading (a), the CV of
[... 40 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    3.64) is far from the paper's (lowest about 6, maximum about 7); see the findings.",
 "new_string": "    3.64) is far from the paper's (lowest about 6, maximum about 7). Question for the authors, as in\n    the findings. How is the kurtosis computed so that surrogate windows give values of 6 or more,\n    and is kappa_surr_max the maximum over every surrogate window or a summary less sensitive to\n    single windows?"
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/cambrainha-2025-01.yaml",
 "old_string": "    (CV (a)) NNI z departs by 0.083 against an SD of 0.056.",
 "new_string": "    (CV (a)) NNI z departs by 0.083 against an SD of 0.056. Question for the authors, as for\n    fig3c-scaling-hit-rate-higher. What is kappa_surr_max, the start of the Figure S3 range?"
}
```

```
The file attempts/cambrainha-2025-01.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
d=yaml.safe_load(open('attempts/cambrainha-2025-01.yaml'))
import re
def walk(x):
    if isinstance(x,dict): [walk(v) for v in x.values()]
    elif isinstance(x,list): [walk(v) for v in x]
    elif isinstance(x,str) and (': ' in x or 'rather' in x or '—' in x): print(x[:80])
walk(d); print(len(d['outcomes']), len(d['verifications'][0]['results']))"; python tools/entry.py check entries/cambrainha-2025 2>&1 | tail -3; git status --short | grep -v "^ M tools\|^?? tools"; date -u
```

```
18 18
0 error(s)
 M attempts/cambrainha-2025-01.yaml
 M entries/cambrainha-2025/README.md
 M entries/cambrainha-2025/criticality.py
 M entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb
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
?? docs/outside-runs.md
?? questions/cambrainha-2025.yaml
?? scripts
Fri Nov 27 12:57:26 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb')); print(sum(len(c.get('outputs',[])) for c in nb['cells']))"; timeout 120 python tools/entry.py run entries/cambrainha-2025 2>&1 | tail -3
```

```
0
pass  reproduce_cambrainha_2025.ipynb  (1778 s, reused)
reused the executed copies of 2026-11-27 12:54 UTC: nothing the run reads has changed since (hash 55b309d65473). Nothing was executed and no environment was built; --fresh runs it again.
```

**Agent**

I went through every point in the round-1 report and re-ran the entry with `python tools/entry.py all`. It passed in 29.6 min, and `entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **Four claims now agree with the verifier:** fig3c-scaling-hit-rate-higher, fig3c-hit-rate-rises-with-threshold, fig4a-active-most-scaling and figs8-halves-and-phase-order go from blocked to `not_reproduced`, marked as resting on an assumption. I applied each criterion with the threshold grid started at every value from 3 up to the top of its range (190 or 240 starts), and at four named starts: the paper's value of about 7, the 99th and 99.9th surrogate percentiles (6.51, 10.43), and the maximum over windows with at least 128 units. Every start fails under the CV readings (a) and (c). From 7, the scaling hit rate is 0.615 against 0.655 for no-scaling windows. Above 7, the non-natural image phase has 0.499 of windows, the active phase 0.311.
- **figs3-exponents-stable-with-threshold goes from blocked to `not_reproduced`**, although the verifier had agreed with blocked. Here the grid start does change the result: from 7 and from the 99th percentile it fails (non-natural image z departs by 0.083 against an SD of 0.058, and mu has no threshold with 10 sessions in two phases). From the 99.9th percentile only mu fails, which would be partially reproduced. I adopted the paper's value of about 7 (claims file, M4) as an assumption, and round 2 will review this change.
- All other outcomes are unchanged.

**Outputs added for the verifier's open checks**
- **Which windows set the surrogate maximum:** the largest surrogate value (34.29) comes from an ordinary window with 182 active units. Dropping windows with fewer than 64 or 128 units leaves it at 34.29. Only 13 of 28,335 surrogate windows lie above 15.
- **Correlation-matrix kurtosis** (z-scored counts, a new `kappa_z` column in `criticality.py`): surrogate minimum 4.09, median 15.88. It overlaps the real windows and does not recover the paper's reference of about 6 either.
- **Trial density:** counting aborted trials as failures gives a median of 5 trials per window, matching the paper's "three to five", but an overall hit rate of 0.236. The fig3c tests still fail under it.
- **mu fitted over ranks 1 to K/2:** 99.9% of windows now pass the r² rule, but mu is 1.06 against the paper's 0.73, so the exponent outcomes stay the same.
- Smaller fixes:
  - figs3 now evaluates every grid point, not every tenth.
  - fig4bc has a paired Wilcoxon test against the surrogates (p = 1.2e-17).
  - fig3d gives its largest gain restricted to thresholds with at least 30 trials on each side.

**Record and questions**
- `questions/cambrainha-2025.yaml` (new) asks a reader two things: whether O5 should count aborted trials, and whether O9 should fit mu over the upper ranks only. I did not change the claims.
- In `attempts/cambrainha-2025-01.yaml`, round 1 is recorded under `verifications` with the verifier's reasons and my responses. I updated the notes of the changed claims and the statements of four findings, keeping the findings in order. The notebook's conclusions, summary and README match the new numbers.

**Not done**
- No `findings` entry for round 1: none of the findings is rated critical, and that review only happens in round 2.
- No change to the 10⁴ Poisson bootstrap or to the 97-session analysis set; both are stated as deviations, and the verifier rated neither as affecting a conclusion.
- I could not compare against the paper's figures, because there is no PDF renderer here.
- `runtime_minutes: 30` in `entry.yaml` is left as it is, since the run took 29.6 min and editing the file would force another full run.

## End of run

99 turns, 149 minutes, $5.87 at API prices, result: success.
