# 000289 · author-revise-1 · run 40981435341

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000289/verifier-1-report.md; ls entries/000289-kutschireiter-2023 entries/000289-kutschireiter-2023/*;
```

```
Fri Oct 30 00:46:11 UTC 2026
**A. Outcomes** (13 claims, from the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| fig1-conflict-decreases-certainty | reproduced | Cell 12: (a) and (b) hold in 6 of 6 cases (κ_t = 1, 2, 5; γ_z = 1 and 10/s). For example, at κ_t = 5 and γ_z = 1, the full step gives 5.039 (confirmatory) against 4.904 (no observation) against 4.768 (opposite). |
| fig2h-bump-tracks-circkf | reproduced | Cell 14: at rates 15 and 10, the network-to-circKF difference is 0.016 and 0.021 rad, against circKF error of 0.483 and 0.491. Correlation over cue periods is 0.994 and 0.993. In darkness the amplitude falls from 7.21 to 1.22 (rate 15) and from 5.89 to 1.21 (rate 10), ending closer to κ* = 1. |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced | Cell 16: the largest accuracy difference is 0.0010 at rates ≥ 1/s and 0.0003 at ≥ 3/s, so all four combinations pass. At 0.01 to 0.1/s the attractor is less accurate (−0.073, −0.084, −0.057) and more certain (+0.82, +0.69, +0.49). |
| fig3b-bayesian-beats-conventional | reproduced | Cell 18: the optimal κ* is 1.7. The Bayesian attractor is more accurate at all 23 rates (smallest difference 0.0115) and strictly above from 0.1 to 10/s (smallest 0.034). The not-judged part fails: the smallest differences are at 0.01, 2 and 3/s, not at 0.01 and 0.03/s. |
| fig3c-update-weights | reproduced | Cell 20: the largest difference at ≥ 1/s is 0.0010 under reading (i) and 0.0062 under (ii), within both 0.02 and 0.05. Under both readings the largest difference is at 0.01/s. |
| fig3d-best-network-slow-decay | partially_reproduced | Cell 22: conditions 1, 2, 3 and 5 hold (best network κ* = 0.7, β = 0.3; the Bayesian attractor is 0.57% below it). Condition 4 fails: the maximum over κ* rises twice for β above the best (0.7→0.8 by +0.0008, 0.9→1 by +0.0014). Overall Spearman ρ is −0.98. |
| fig3f-noise-drop-below-70 | reproduced | Cell 24: untuned performance is 63.1% at SD 10 and 38.1% at SD 20 under both no
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i -E "^|" | head -0; wc -l docs/protocol.md; ls attempts 2>/dev/null | head; find . -path ./node_modules -prune -o -name "*000289*" -print | grep -v "^./.git/" | head -30
```

```
612 docs/protocol.md
000003-senzai-2017-01.yaml
000004-chandravadia-2020-01.yaml
000005-yu-2016-01.yaml
000005-yu-2016-02.yaml
000006-economo-2018-01.yaml
000006-economo-2018-02.yaml
000008-scala-2021-01.yaml
000009-guo-2017-01.yaml
000010-li-2015-01.yaml
000011-li-2016-01.yaml
./attempts/000289-kutschireiter-2023-01.yaml
./entries/000289-kutschireiter-2023
./claims/000289
./transcripts/000289
```

**Agent calls Bash**

```bash
cat docs/protocol.md
```

```
<persisted-output>
Output too large (35.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e79311da-ee43-4cee-a949-b48ffbd07ba1/tool-results/bhpzaf205.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

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

**Agent calls Bash**

```bash
cat attempts/000289-kutschireiter-2023-01.yaml; ls claims/000289 transcripts/000289; ls questions | grep 289
```

```
schema_version: 2
id: 000289-kutschireiter-2023-01
dataset:
  archive: dandi
  id: "000289"
  version: 0.240801.1040
  doi: 10.48324/dandi.000289/0.240801.1040
paper: doi:10.1073/pnas.2210622120
date: 2026-10-29
entry: 000289-kutschireiter-2023
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
[... 272 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -E "verification|round|proposed|step 6|^#" docs/protocol.md | head -80
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
174:verification"). A method detail the claims file lacks is not asked: the author
182:## Author
188:(step 6).
198:### 1. Establish what can be tested
275:     (step 6; see also chance levels, under "Record the attempt").
322:     claims file (reader, step 6), and a later run, `author-answers`,
325:### 2. Check the data against its description
333:a task variable in windows around the trial start does this; for continuous
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
439:- **`proposed`**: on an outcome, a change of outcome found after the last
[... 21 more lines not kept]
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
grep -l "verifications:" attempts/*.yaml | head -3; f=$(grep -l "verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -60; ls schema* docs | head -30
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
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; wc -l bra.py; python -c "
import json;nb=json.load(open('reproduce_kutschireiter_2023.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print(i,c['cell_type'],c.get('metadata',{}).get('tags'),len(s),repr(s[:100]))
"; cat entry.yaml; ls ../../questions | grep 289; ls ../../executed/ 2>/dev/null | grep 289
```

```
270 bra.py
0 markdown None 3022 '# Testing Kutschireiter et al. (2023) with dandiset 000289\n\nPaper. Kutschireiter A, Basnak MA, Wilso'
1 code None 687 'import time\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom concurrent.futures i'
2 markdown None 228 "## Data check\n\nThe paper's processed outputs, the connectome export, and the 15 imaging sessions of "
3 code ['sanity'] 1214 '# --- the paper\'s processed outputs\nfor name in ["figure2i.npz", "figure3d.npz", "figure4g.npz", "fi'
4 markdown None 393 'The processed outputs have the shapes the figure notebooks expect, accuracies lie in 0 to 1, and the'
5 code ['sanity'] 831 '# --- the hemibrain connectome export (v1.2): neurons of the three types and their names\nneurons, co'
6 markdown None 364 '46 EPG, 20 PEN1 and 42 Delta7 neurons. Every EPG and PEN1 instance names one protocerebral bridge\ngl'
7 code ['sanity'] 2439 '# --- dandiset 000289: every asset, and the cue-contrast sessions\nassets = bra.assets()\nprint("dandi'
8 markdown None 809 'The cue-contrast experiment is subjects 1 to 15, one session each ("fly presented with visual cues\no'
9 code ['sanity'] 1681 "# --- does the bump follow the cue on the session's clock? Bump phase (frequency 2 across the PB)\n# "
10 markdown None 557 'The bump phase locks to the cue position at high contrast (median coherence 0.79) and barely in\ndark'
11 markdown None 573 '## fig1-conflict-decreases-certainty\n\n> In the circular Kalman filter, an HD observation consistent '
12 code ['claim:fig1-conflict-decreases-certainty'] 1032 'rows = []\nfor gz in (1, 10):\n    alpha = flt.xi_fun_inv(gz * 0.01)\n    for k in (1, 2, 5):\n        u'
13 markdown None 256 '**Result: reproduced.** In all six cases (three certainties, two reliabilities) a confirmatory\nobser'
14 markdown None 668 '## fig2h-bump-tracks-circkf\n\n> In a simulated Bayesian ring attractor of 80 neurons, the bump positi'
15 code ['claim:fig2h-bump-tracks-circkf'] 891 'f2h = {}\nfor rate in
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/000289; python - <<'E'
import yaml
d=yaml.safe_load(open('10.1073-pnas.2210622120.yaml'))
print(d.keys())
for c in d['claims']:
    if c['id'] in ('fig4b-connectome-motifs','figs2-performance-independent-of-n','noise-effects-on-mu-and-kappa','fig4gh-drosophila-network-matches','fig3d-best-network-slow-decay'):
        print(yaml.dump(c,width=120,allow_unicode=True))
E
ls ../../questions | head;
```

```
dict_keys(['schema_version', 'dataset', 'paper', 'claims', 'checks'])
criterion: figure3d.npz holds MSE_array, the prior-weighted average accuracy over the grid of kappa* (0.1 to 2.5) and beta
  (0.1 to 8), normalized by the particle filter reference as in the notebook. The Bayesian ring attractor is kappa* = 1, beta
  = 1/(kappa_phi + kappa_v) = 0.5 (Methods). The best network is the grid maximum. Reproduced when (1) the best beta is at
  most 1 (the scanned values above 1 are 2, 4 and 8); (2) the best network differs from (1, 0.5) in kappa* or beta; (3) the
  Bayesian attractor's normalized performance is within 10% of the best (the paper's "similar", default tolerance); (4) for
  beta above the best, the maximum over kappa* falls as beta rises; (5) for beta above the best, the kappa* that maximizes
  performance is at least the best network's kappa*.
data: elsewhere
id: fig3d-best-network-slow-decay
quote: The network with the best performance overall had a slow bump decay speed (low β ), as expected ( Fig. 3 D and E ).
  While it featured similar performance to the Bayesian ring attractor, it had slightly different β and κ * parameters ...
  As the bump decay speed β increased further, performance dropped.
source: Results, Bayesian vs. Conventional Ring Attractors, paragraph 4; Fig. 3D
statement: Across ring attractors with different bump decay speeds and baseline amplitudes, the best network has a slow decay
  (low beta) and performs about as well as the Bayesian ring attractor; performance drops as decay speed increases, which
  a larger baseline amplitude partly offsets.
where: Zenodo doi:10.5281/zenodo.7615975 (BayesianRingAttractor v1.0, commit a9db6f9), data_processed/figure3d.npz with Figure3b,c,e,d_FigureS3.ipynb

criterion: The result is a derivation (SI Appendix, section 5); the Methods give the diffusion SD of kappa under additive
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; cat bra.py
```

```
"""Helpers for testing Kutschireiter, Basnak, Wilson & Drugowitsch (2023), "Bayesian inference in
ring attractor networks" (PNAS 120, e2210622120), with dandiset 000289.

The paper holds no recorded data. Its simulation claims are tested on the paper's own code and
processed outputs (Zenodo doi:10.5281/zenodo.7615975, BayesianRingAttractor v1.0, commit a9db6f9),
its connectome claim on the hemibrain connectome, and its one prediction about cue reliability on
the imaging data of dandiset 000289. Every source is read into memory; nothing is written to disk.

Where each parameter comes from:
- The claims file (claims/000289/10.1073-pnas.2210622120.yaml) gives every criterion: the
  information rates, the readings for unquantified words, the network parameters of the noise test,
  the decoder for bump amplitude.
- The paper's code fixes the rest: the objective() weighting (mean 0.5, SD 1 over log rate), the
  particle-filter reference, the Figure 2H simulation (run from the released notebook's own cells).
- Two patches are needed to run the released code, both named in the claims file's header:
  RNN_filter_Run gets a `z=None` argument (it uses z but has no such parameter), and the notebook
  Figure2h.ipynb calls vM_Projection_Run with `kappa_y=`, which the function names `kappa_v`.
- Standard choices that set only precision or speed are marked as such where they are made.
"""
import hashlib
[... 250 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/ 2>&1 | head; python -c "
import json;nb=json.load(open('entries/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
for i in [0,1,3,4,36,37,45,46,48,49,50,51]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
ls: cannot access 'executed/': No such file or directory
===== 0
# Testing Kutschireiter et al. (2023) with dandiset 000289

Paper. Kutschireiter A, Basnak MA, Wilson RI, Drugowitsch J (2023). Bayesian inference in ring
attractor networks. *PNAS* 120, e2210622120.
[doi:10.1073/pnas.2210622120](https://doi.org/10.1073/pnas.2210622120). The claims file was written
from the version of record (Europe PMC, PMC9992764) with its SI Appendix.

Dandiset. [DANDI:000289](https://dandiarchive.org/dandiset/000289/0.240801.1040), version
0.240801.1040, "Two-photon calcium imaging of EPG cells in Drosophila Melanogaster presented with
cues of varying reliability" (Basnak and Wilson). The paper cites no dandiset version. This is the
only published version and the most recent; the draft has the same 221 assets and size, so the
published version is pinned.

What the dandiset holds, and what the paper uses. The paper is a theory paper: every result is
a simulation, apart from a connectome comparison and one prediction. The dandiset holds two-photon
imaging of EPG neurons in the protocerebral bridge, with the cue position and trial tables, from a
separate study (Basnak et al., "Uncertainty and learning in a biological ring attractor", named in
the dandiset's description). So, as the claims file sets out:
[... 247 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import sys; sys.path.insert(0,'entries/000289-kutschireiter-2023')
import bra; c=bra.Code(); c.zip.extractall('dep')
" && ls dep/*/ && cat questions_example 2>/dev/null; head -40 questions/000005.yaml
```

```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    import bra; c=bra.Code(); c.zip.extractall('dep')
    ^^^^^^^^^^
  File "entries/000289-kutschireiter-2023/bra.py", line 28, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
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
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
ls -a  | head -40; which python; ls ~/.venv* .venv 2>&1 | head; sed -n 1,80p tools/entry.py | grep -n -i -E "venv|uv |python"
```

```
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
.gitmodules
.idea
.mcp.json
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -E "uv|venv" tools/entry.py | head -20; which uv
```

```
37:Requires `uv` on PATH, and `pyyaml`, `jsonschema` and `nbformat` to run this
335:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
345:    venv = (output_dir / ".venv").resolve()
346:    python = venv / "bin" / "python"
350:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
351:                ["uv", "pip", "install", "--quiet", "--python", str(python),
353:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
367:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv --quiet --python 3.13 dv && uv pip install --quiet --python dv/bin/python -r entries/000289-kutschireiter-2023/requirements.lock.txt && dv/bin/python -c "
import sys; sys.path.insert(0,'entries/000289-kutschireiter-2023')
import bra; c=bra.Code(); c.zip.extractall('dep')
" && ls dep/*/; echo $TMPDIR
```

```
Figure2a,c_FigureS1.ipynb
Figure2h.ipynb
Figure2i.ipynb
Figure3b,c,e,d_FigureS3.ipynb
Figure3f_FigureS4.ipynb
Figure4g,h.ipynb
FigureS2.ipynb
LICENSE
README.md
circularFiltering.py
data_processed
data_raw
environment.yml
network_filter.py
performance_scan_figure2i.py
performance_scan_figure3d.py
performance_scan_figure3f.py
performance_scan_figure4g.py
performance_scan_figureS2.py
/tmp/claude-1001
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dep/*/ && cat performance_scan_figure2i.py | head -150; grep -n -i "def performance\|def .*stats\|cos\|return" circularFiltering.py | head -40
```

```
import sys
import numpy as np
import circularFiltering as flt
from time import time

kappa_z_array = np.array([0.01,0.03,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,30,100])

# choose a kappa_z according to system variable
kappa_z = kappa_z_array[int(sys.argv[1])]

# choose kappa according to input variable
kappa = float(sys.argv[2])

# pass the number of iterations
nIter = 10000

# where to save
filename = "data_raw/figure2i/k="+str(kappa)+"_kz="+str(kappa_z)

# model parameters
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dep/*/ && for n in Figure2i.ipynb FigureS2.ipynb "Figure4g,h.ipynb" "Figure3b,c,e,d_FigureS3.ipynb"; do echo "=== $n"; python3 -c "
import json,sys;nb=json.load(open(sys.argv[1]))
for c in nb['cells']:
  if c['cell_type']=='code': print(''.join(c['source'])); print('---')
" "$n" | head -150; done; cat performance_scan_figureS2.py | head -60
```

```
=== Figure2i.ipynb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import circularFiltering as flt
from scipy.stats import vonmises
import matplotlib
import glob
import re
import os
matplotlib.rcParams.update({'font.size': 14,
                            'pdf.fonttype': 42,
                            'ps.fonttype': 42})
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})



---
T = 10 # simulation time
[... 486 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dep/*/ && grep -n -E "nIter|^T |^dt|T = |dt = " performance_scan_figure4g.py performance_scan_figure3d.py performance_scan_figure3f.py performance_scan_figureS2.py; sed -n 60,100p performance_scan_figureS2.py; grep -n "def circular_mean" -A8 circularFiltering.py
```

```
performance_scan_figure4g.py:13:nIter = 10000
performance_scan_figure4g.py:22:T = 20 # simulation time
performance_scan_figure4g.py:23:dt = 0.001 # step size
performance_scan_figure4g.py:33:phi_final = np.zeros([nIter])
performance_scan_figure4g.py:34:vonMises = np.zeros([nIter,2])
performance_scan_figure4g.py:35:vonMises_q = np.zeros([nIter,2])
performance_scan_figure4g.py:36:noUncert = np.zeros([nIter])
performance_scan_figure4g.py:37:CX = np.zeros([nIter,2])
performance_scan_figure4g.py:40:for i in range(0, nIter): # run for nIter iterations
performance_scan_figure3d.py:14:nIter = 10000
performance_scan_figure3d.py:17:T = 20 # simulation time
performance_scan_figure3d.py:18:dt = 0.01 # step size
performance_scan_figure3d.py:34:    phi_final = np.zeros([nIter])
performance_scan_figure3d.py:35:    network_flt = np.zeros([nIter,2])
performance_scan_figure3d.py:43:    for j in range(0, nIter): # run for nIter iterations
performance_scan_figure3f.py:15:nIter = 10000
performance_scan_figure3f.py:18:T = 20 # simulation time
performance_scan_figure3f.py:19:dt = 0.01 # step size
performance_scan_figure3f.py:35:    phi_final = np.zeros([nIter])
performance_scan_figure3f.py:36:    network_flt = np.zeros([nIter,2])
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper/; grep -l -i "S107\|neural noise" paper/* 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; pdftotext -layout paper/10.1073-pnas.2210622120.supp.pdf si.txt 2>&1 | head -2 || dv/bin/python -c "print('no pdftotext')"; grep -n -i "neural noise\|S10[5-9]\|S11[0-2]" si.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; uv pip install --quiet --python dv/bin/python pypdf && dv/bin/python -c "
import pypdf;r=pypdf.PdfReader('paper/10.1073-pnas.2210622120.supp.pdf')
open('si.txt','w').write('\n'.join(f'=== page {i+1}\n'+p.extract_text() for i,p in enumerate(r.pages)))
"; grep -n -i "neural noise\|(S10[5-9])\|(S11[0-2])\|^=== page" si.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1080,1260p $TMPDIR/si.txt
```

```
=== page 20
5. The impact of neural noise on inference dynamics
So far we have assumed the the only sources of noise were noisy inputs from angular velocity and HD observations. Here we
ask how the inference dynamics are impacted if the neurons that constitute the ring attractor are also noisy. We will do so in
three steps. First, we will make a qualitative observation of how such neural noise is expected to impact the dynamics ofµt
and κt. Second, we will derive expressions for the impact of such noise onµt and κt for different noise models. Third, we will
ask how we can ensure that neural noise has a minimal impact on the performed inference. For all steps we return to our
single-population ring attractor whose dynamics are described by Eq. [S49], and assume that neural noise impacts the activity
of neuronj by
drt,j =h (rt,j)dWt,j, [S106]
where h(·) is a function of neural activity, and thedWt,j’s are Brownian motion processes that are uncorrelated across neurons.
Different noise models correspond to different assumptions about the form ofh(·). As for large population sizesN, individual
neural noise can be averaged out and will have limited impact (22). Therefore, we assumeN to be sufficiently small for neural
noise to matter, but to be sufficiently large such that we can well-approximate various sums by their integral limit.
A. The qualitative impact of neural noise on inference dynamics.With neural noise, the population dynamics equation Eq. [S49]
becomes
drt(ϕ) =··· +Iextt (ϕ) +ηt(ϕ), [S107]
whereIextt (ϕ) is our model’s (stochastic) external input, and the newly addedηt(ϕ) captures the activity perturbations induced
by neural noise. This shows that we can interpret neural noise as yet another stochastic input to the network. This implies
that this noise impacts the dynamics forηt and κt (previously Eqs. [S56] & [S57]) through
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  python - <<'E'
import json;nb=json.load(open('entries/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
for i in [5,6,9,10,27,28,39,40,42,43]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
E
```

```
Fri Oct 30 00:48:15 UTC 2026
===== 5
# --- the hemibrain connectome export (v1.2): neurons of the three types and their names
neurons, conns = bra.hemibrain()
types = {"EPG": "EPG", "PEN_a(PEN1)": "PEN1", "Delta7": "Delta7"}
cx = neurons[neurons.type.isin(types)].copy()
cx["t"] = cx.type.map(types)
cx["g"] = cx.instance.map(bra.pb_glomerulus)
print("traced neurons:", len(neurons), "; connections:", len(conns), "; total synapses:", conns.weight.sum())
print(cx.groupby("t").agg(n=("bodyId", "size"), with_glomerulus=("g", lambda s: s.notna().sum())).to_string())
for t in ["EPG", "PEN1", "Delta7"]:
    print(t, "instances:", sorted(cx[cx.t == t].instance.unique())[:6], "...")
print("glomeruli named: EPG", sorted(cx[cx.t == 'EPG'].g.unique(), key=bra.PB_ORDER.index),
      "\n                 PEN1", sorted(cx[cx.t == 'PEN1'].g.unique(), key=bra.PB_ORDER.index))
===== 6
46 EPG, 20 PEN1 and 42 Delta7 neurons. Every EPG and PEN1 instance names one protocerebral bridge
glomerulus (EPG L8 to R8, PEN1 L9 to L2 and R2 to R9), which is reading (a) of the claim's sort.
No instance names an ellipsoid body or gall position, so reading (b) cannot be formed from the
names. Delta7 names list the glomeruli the neuron spans, not one position.
===== 9
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dep/*/ && grep -n "kappa_z\b\|kappa_z =" -m5 /dev/null; python3 -c "
import json;nb=json.load(open('Figure2h.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code':
    s=''.join(c['source'])
    if 'kappa_z' in s: print(s[:1500]); print('----')
" | head -60; python3 -c "
import json;nb=json.load(open('Figure3f_FigureS4.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code':
    s=''.join(c['source'])
    if 'array' in s: print(s[:1200]); print('----')
" | head -60; grep -n "array\|beta\|kappa_star" performance_scan_figure3d.py | head
```

```
####### simulation parameters
np.random.seed(42)
T = 15
dt = 0.01
t = np.arange(0,T,dt)
kappa_phi = 1 # inverse diffusion constant
kappa_v = 2 # precision of relative heading info
kappa_z = 15 # precision of absolute heading info (called gamma_z in manuscript)
alpha = flt.xi_fun_inv(kappa_z*dt) 

### create kappa_z depending on environment. If light is off, kappa_z is zero (maximally uninformative)
kappa_z_array = alpha * np.ones(int(T/dt)) # precision of absolute heading info
t_off = 5
t_on = 10
ind_off = int(t_off/dt)
ind_on = int(t_on/dt)
kappa_z_array[ind_off:ind_on] = 0 # maximally uninformative while light is off

### create hidden state trajectory and observation sequence
phi = np.zeros(int(T/dt)) # latent state
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dep/*/ && python3 -c "
import json;nb=json.load(open('Figure3b,c,e,d_FigureS3.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code':
    s=''.join(c['source'])
    if 'figure3d' in s: print(s[:2500]); print('----')
"; python3 -c "
import json;nb=json.load(open('Figure3f_FigureS4.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code':
    s=''.join(c['source'])
    if 'MSE_array[' in s: print(s[:2500]); print('----')
"
```

```
preprocess = False # only set to True if you want to re-run preprocessing on data in /data_raw

path_raw = 'data_raw/figure3d/'
path_processed = 'data_processed/'
----
kappa_star_array = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5])
beta_array = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9, 1, 2 ,4 ,8])
kappa_z_array = np.array([1.e-02, 3.e-02, 1.e-01, 2.e-01, 3.e-01, 4.e-01, 5.e-01, 6.e-01,
       7.e-01, 8.e-01, 9.e-01, 1.e+00, 2.e+00, 3.e+00, 4.e+00, 5.e+00,
       6.e+00, 7.e+00, 8.e+00, 9.e+00, 1.e+01, 3.e+01, 1.e+02])

if preprocess:
       MSE_array = np.zeros((len(kappa_star_array),len(beta_array)))
       for i in np.arange(len(kappa_star_array)):
              for j in np.arange(len(beta_array)):
                     filename = path_raw+"ntwkflt_k="+str(kappa_star_array[i])+"_beta="+str(beta_array[j])
                     data = np.load(filename+'.npz')
                     stats = data['stats']
                     MSE_array[i,j] = objective( stats[:,1] ,mu=mu_perf,sigma=sig_perf) 

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023 && python3 - <<'E'
p='bra.py'; s=open(p).read()
s=s.replace('''from scipy.stats import norm
''','''from scipy.special import i0e, i1e, ive
from scipy.optimize import brentq
from scipy.stats import norm
''')
s=s.replace('''    def notebook_cells(self, name):''','''    def source_lines(self, name, pattern):
        """The lines of a released script or notebook that match the regular expression, so that the
        notebook can show where a grid, an axis or a parameter is defined."""
        text = self.read(name).decode()
        if name.endswith(".ipynb"):
            text = "\\n".join(self.notebook_cells(name))
        return [ln.rstrip() for ln in text.splitlines() if re.search(pattern, ln)]

    def notebook_cells(self, name):''')
s=s.replace('''# ---------------------------------------------------------------------------------------------
# Figure 2H''','''def resultant_se(R, n=10000):
    """Monte Carlo standard error of an accuracy |m1| = |mean exp(i error)| over n independent runs
    (n = 10,000 in every performance_scan_*.py). Delta method with the mean error at 0, so that
    |m1| is about the mean of cos(error): SE = sd(cos error) / sqrt(n). Two values are returned:
    under von Mises errors with resultant R (var cos = (1 + A2) / 2 - R^2, A2 = I2/I0), and the
    distribution-free upper bound sqrt((1 - R^2) / n). A standard choice; it sets only how a
    difference is read, not a criterion."""
    R = np.atleast_1d(np.asarray(R, float))
    vm = np.empty_like(R)
    for k, r in enumerate(R):
        r = min(max(r, 1e-6), 1 - 1e-9)
        kap = brentq(lambda x: i1e(x) / i0e(x) - r, 1e-9, 1e6)
        a2 = ive(2, kap) / i0e(kap)
        vm[k] = np.sqrt(max((1 + a2) / 2 - r ** 2, 0) / n)
    return vm, np.sqrt((1 - R ** 2) / n)


def objective_se(se_per_rate, rates=RATES, mu=0.5, sigma=1.0):
    """Standard error of objective() when each rate's value has its own independent error: the
    objective is a fixed linear combination of the per-rate values (trapezoidal weights)."""
    x = np.log(rates)
    w = norm.pdf(x, loc=mu, scale=sigma)
    c = np.zeros(len(x))
    c[1:] += 0.5 * w[1:] * np.diff(x)
    c[:-1] += 0.5 * w[:-1] * np.diff(x)
    return np.sqrt(np.sum((c * np.asarray(se_per_rate)) ** 2))


# ---------------------------------------------------------------------------------------------
# Figure 2H''')
s=s.replace('''def rnn_batch(rng, runs, T, N, sigma_N, w_even, w_quad, tau=1.0, kappa_0=1.0, phi_0=0.0, dt=0.01,
              noise=None):''','''def rnn_batch(rng, runs, T, N, sigma_N, w_even, w_quad, tau=1.0, kappa_0=1.0, phi_0=0.0, dt=0.01,
              noise=None, inh_fixed=None, traces=None):''')
s=s.replace('''    standard normal draws (steps x runs x N) to reproduce a given run."""''','''    standard normal draws (steps x runs x N) to reproduce a given run.

    Diagnostics for the noise claim (not in RNN_filter_Run): `inh_fixed`, if given, replaces the
    global inhibition w_quad pi/N sum max(r, 0) by that constant, so that the noise acts only
    through the linear terms, as in the SI derivation (section 5, Eqs. S107 to S109, where the
    noise is one more input and the other dynamics are unchanged). `traces`, a dict, receives the
    run-mean global inhibition and zero mode (population mean rate) at every step."""''')
s=s.replace('''    mu[0], kappa[0] = decode(r)
    for i in range(1, steps):
        inh = w_quad * (np.pi / N) * np.maximum(r, 0).sum(1, keepdims=True)''','''    mu[0], kappa[0] = decode(r)
    if traces is not None:
        traces["inh"], traces["zero_mode"] = np.zeros(steps), np.zeros(steps)
    for i in range(1, steps):
        inh = w_quad * (np.pi / N) * np.maximum(r, 0).sum(1, keepdims=True)
        if traces is not None:
            traces["inh"][i - 1], traces["zero_mode"][i - 1] = inh.mean(), r.mean()
        if inh_fixed is not None:
            inh = inh_fixed''')
s=s.replace('''        mu[i], kappa[i] = decode(r)
    return mu, kappa''','''        mu[i], kappa[i] = decode(r)
    if traces is not None:
        traces["inh"][-1] = (w_quad * (np.pi / N) * np.maximum(r, 0).sum(1)).mean()
        traces["zero_mode"][-1] = r.mean()
    return mu, kappa''')
s=s.replace('''    theta = 2/N A r). Returns (phase, amplitude) per frame."""''','''    theta = 2/N A r). Returns (phase, amplitude) per frame.

    The phase is the angle of sum r_j exp(-i 2 pi k j / n), so a bump peaking at ROI angle theta
    gives phase -theta: ROIs are taken in order of decreasing angle. The sense in which the ROI
    order maps onto heading is not in the files, so the sign is a convention; the data check uses
    the phase only against the cue and shows that it locks to it with this sign. The amplitude, the
    only quantity the prediction uses, does not depend on the sign or on an offset."""''')
s=s.replace('''def raw_roi_fluorescence(f, frames, masks, projection="mean", smooth=4.0):''','''def raw_roi_fluorescence(f, frames, masks, projection="mean", smooth=4.0):
    """See _raw_roi; `smooth` may be a tuple of SDs, which returns a dict of results, one per SD,
    from one read of the frames."""
    if isinstance(smooth, (tuple, list)):
        return _raw_roi(f, frames, masks, projection, smooth)
    return _raw_roi(f, frames, masks, projection, (smooth,))[smooth]


def _raw_roi(f, frames, masks, projection, smooths):''')
s=s.replace('''    out = []
    for a, b in frames:
        v = d[a:b].astype(np.float32)
        p = v.mean(1) if projection == "mean" else v.max(1)
        if smooth:
            p = gaussian_filter(p, (0, smooth, smooth))
        out.append(p.reshape(p.shape[0], -1) @ m.T)
    return np.concatenate(out)''','''    out = {sm: [] for sm in smooths}
    for a, b in frames:
        v = d[a:b].astype(np.float32)
        p0 = v.mean(1) if projection == "mean" else v.max(1)
        for sm in smooths:
            p = gaussian_filter(p0, (0, sm, sm)) if sm else p0
            out[sm].append(p.reshape(p.shape[0], -1) @ m.T)
    return {sm: np.concatenate(v) for sm, v in out.items()}''')
open(p,'w').write(s)
E
grep -n "_raw_roi\|def raw_roi" -A3 bra.py | head -30
```

```
312:def raw_roi_fluorescence(f, frames, masks, projection="mean", smooth=4.0):
313:    """See _raw_roi; `smooth` may be a tuple of SDs, which returns a dict of results, one per SD,
314-    from one read of the frames."""
315-    if isinstance(smooth, (tuple, list)):
316:        return _raw_roi(f, frames, masks, projection, smooth)
317:    return _raw_roi(f, frames, masks, projection, (smooth,))[smooth]
318-
319-
320:def _raw_roi(f, frames, masks, projection, smooths):
321-    """Raw fluorescence per ROI from the TwoPhotonSeries for the given frame blocks: the volume is
322-    projected over planes (`projection`), smoothed in the plane with a Gaussian of SD `smooth`
323-    pixels, and averaged over each ROI's 2D mask (5 to 9 pixels on the PB midline). Neither the
```

**Agent calls Bash**

```bash
sed -i 's/projected over planes (`projection`), smoothed in the plane with a Gaussian of SD `smooth`/projected over planes (`projection`), smoothed in the plane with a Gaussian of each SD in `smooths`/' bra.py && time $TMPDIR/dv/bin/python - <<'E'
import numpy as np, bra
from scipy import stats
rng=np.random.default_rng(1)
print(bra.resultant_se([0.2,0.5,0.9]))
for N in (64,256):
  tr0={}
  _,k0=bra.rnn_batch(rng,1,5,N,0.0,1.5,0.5,traces=tr0)
  inh0=tr0['inh'][-1]
  for sig in (1.,2.):
    tr={}
    mu,k=bra.rnn_batch(rng,500,5,N,sig,1.5,0.5,traces=tr)
    muf,kf=bra.rnn_batch(rng,500,5,N,sig,1.5,0.5,inh_fixed=inh0)
    s=np.sqrt(2*sig**2/N*5)  # per-coordinate SD after 5s? var(dkappa)=2 sig^2/N dt -> per coordinate var
    pred=stats.rice(b=1/ s, scale=s).mean()
    print(N,sig,'inh0',round(inh0,3),'inh t=0.1,1,5',tr['inh'][[9,99,-1]].round(3),'zero',tr['zero_mode'][[9,99,-1]].round(3),
      'full end',k[-1].mean().round(3),'frozen end',kf[-1].mean().round(3),'rice',round(pred,3), 'frozen var',kf[-1].var().round(3))
E
```

```
(array([0.00685665, 0.00564546, 0.00142614]), array([0.00979796, 0.00866025, 0.0043589 ]))
64 1.0 inh0 0.5 inh t=0.1,1,5 [0.519 0.571 0.524] zero [-0.002  0.005 -0.003] full end 0.814 frozen end 1.079 rice 1.082 frozen var 0.144
64 2.0 inh0 0.5 inh t=0.1,1,5 [0.585 0.763 0.729] zero [-0.003 -0.002 -0.01 ] full end 0.635 frozen end 1.385 rice 1.352 frozen var 0.442
256 1.0 inh0 0.5 inh t=0.1,1,5 [0.52  0.568 0.527] zero [-0.     0.001  0.002] full end 0.823 frozen end 1.019 rice 1.02 frozen var 0.034
256 2.0 inh0 0.5 inh t=0.1,1,5 [0.586 0.763 0.707] zero [ 0.     0.005 -0.004] full end 0.427 frozen end 1.071 rice 1.082 frozen var 0.138

real	0m9.351s
user	0m35.393s
sys	0m0.100s
```

**Agent calls Bash**

```bash
date -u; $TMPDIR/dv/bin/python - <<'E'
import numpy as np, bra, io
c=bra.Code()
f2i=c.npz('figure2i.npz'); vq=f2i['vonMises_q_stats'][0,:,1]
g4=c.npz('figure4g.npz'); s2=c.npz('figureS2.npz')['MSE_array']
se,ub=bra.resultant_se(vq)
print(np.round(se,4)); print(np.round(ub,4))
print('S2 dev / (sqrt2 se):', np.round((s2-vq)/(np.sqrt(2)*se),1))
print('4g bq - 2i bq:', np.round(g4['vonMises_q_stats'][:,1]-vq,4))
print('obj se', bra.objective_se(se)/bra.objective(f2i['PF_stats'][0,:,1]))
print(np.argwhere(np.isnan(s2)))
E
```

```
Fri Oct 30 00:49:31 UTC 2026
[0.0071 0.007  0.0068 0.0065 0.0062 0.0059 0.0057 0.0055 0.0052 0.0051
 0.0049 0.0047 0.0037 0.0031 0.0027 0.0024 0.0022 0.002  0.0019 0.0017
 0.0017 0.0009 0.0005]
[0.01   0.01   0.0098 0.0095 0.0092 0.0089 0.0087 0.0085 0.0082 0.0081
 0.0079 0.0078 0.0069 0.0063 0.0058 0.0056 0.0053 0.0051 0.005  0.0047
 0.0047 0.0035 0.0026]
S2 dev / (sqrt2 se): [[-0.2 -0.2 -1.1 -1.1 -0.8 -0.   0.4  0.3 -0.9  1.1 -0.8 -0.6  0.6 -0.2
  -0.3  0.3  1.1  1.7  0.9  0.9  0.6  0.  -0.6]
 [-1.2 -1.2 -1.9  1.1  0.6 -0.   0.6  0.4  0.1 -0.6 -0.8  0.1  0.4 -0.7
   0.1  0.8  0.8  1.4  1.6 -1.4  0.2 -1.   0.3]
 [-0.5  0.1 -1.9  0.6 -0.6  1.1  0.2  1.3 -0.3  0.1 -1.3 -1.8 -0.3  0.4
  -0.9  1.1 -0.1 -0.4  1.1 -0.4  0.8 -1.4  0. ]
 [ 0.3 -0.9 -4.3 -0.4 -0.2  0.8 -0.2  1.3 -1.1  1.2  0.5 -2.   0.9  1.8
  -0.5  0.9 -0.1  0.1  1.5 -0.4  0.3 -1.3  1.2]
 [-0.2  0.9 -0.2  0.4  0.9 -0.5  0.5 -0.3 -0.   0.9  0.4  0.1  0.9  1.4
   1.  -0.3  1.6 -1.1  2.3 -1.6  0.1 -0.2  0.4]
 [ 0.2  0.  -1.5  1.3  1.2 -0.9  0.6  0.9  0.6  1.4  0.4 -2.   1.7  1.6
  -0.6 -0.8  1.1  0.1  0.6 -0.2  0.4 -2.   0.9]
 [ 0.   0.8 -1.3 -0.1  0.6 -1.1 -0.1  0.2 -0.9  0.2 -0.  -0.6  0.9  2.2
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'E'
import json
p='reproduce_kutschireiter_2023.ipynb'; nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(True)
def code(s,tags=None):
    return {"cell_type":"code","execution_count":None,"metadata":({"tags":tags} if tags else {}),"outputs":[],"source":s.splitlines(True)}
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.splitlines(True)}
s=src(0)
s=s.replace("| fig4b-connectome-motifs | hemibrain v1.2 export | tested (sorting reading (a) only) |","| fig4b-connectome-motifs | hemibrain v1.2 export | tested (sorting reading (a) only; reading (b) cannot be formed) |")
s=s.replace("| prediction-bump-amplitude-cue-reliability | dandiset 000289 | tested |","| prediction-bump-amplitude-cue-reliability | dandiset 000289 | tested; blocked (methods_underspecified) because its readings disagree |")
s=s.replace("No claim is blocked.","Every claim is tested. One, the prediction, is then blocked as `methods_underspecified` under the\nclaims file's own rule, because its readings give different outcomes (see its section).")
setsrc(0,s)
# fig3d: add SE
s=src(27)+'''
# Monte Carlo error of one grid cell: each cell is a separate scan of 10,000 runs per rate
# (performance_scan_figure3d.py), and the objective is linear in the per-rate accuracies. The
# per-rate SE is taken at the Bayesian attractor's accuracies (figure2i.npz), close to the networks'.
se_cell = bra.objective_se(bra.resultant_se(accB)[0]) / ref_pf
print("SE of one cell's normalized performance %.4f (upper bound %.4f); SE of a difference of two cells %.4f"
      % (se_cell, bra.objective_se(bra.resultant_se(accB)[1]) / ref_pf, np.sqrt(2) * se_cell))
print("rises of the maximum, in SEs of a difference:", (steps[steps > 0] / (np.sqrt(2) * se_cell)).round(2))
'''
setsrc(27,s)
E
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/edit1.py <<'E'
import json
p='reproduce_kutschireiter_2023.ipynb'; nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(True)
def code(s,tags=None):
    return {"cell_type":"code","execution_count":None,"metadata":({"tags":tags} if tags else {}),"outputs":[],"source":s.splitlines(True)}
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.splitlines(True)}
assert src(36).startswith("# the batched copy")
s=src(0)
s=s.replace("| fig4b-connectome-motifs | hemibrain v1.2 export | tested (sorting reading (a) only) |","| fig4b-connectome-motifs | hemibrain v1.2 export | tested (sorting reading (a) only; reading (b) cannot be formed) |")
s=s.replace("| prediction-bump-amplitude-cue-reliability | dandiset 000289 | tested |","| prediction-bump-amplitude-cue-reliability | dandiset 000289 | tested, then blocked (methods_underspecified): its readings disagree |")
s=s.replace("No claim is blocked.","Every claim is tested. One, the prediction, is then blocked as `methods_underspecified` under the\nclaims file's own rule, because its readings give different outcomes (see its section).")
setsrc(0,s)
# fig3d
setsrc(27, src(27)+'''
# Monte Carlo error of one grid cell: each cell is its own scan of 10,000 runs per rate
# (performance_scan_figure3d.py), and the objective is linear in the per-rate accuracies. The
# per-rate SE is taken at the Bayesian attractor's accuracies (figure2i.npz), close to the networks'.
se_cell = bra.objective_se(bra.resultant_se(accB)[0]) / ref_pf
print("SE of one cell's normalized performance %.4f (distribution-free bound %.4f); SE of a difference of two cells %.4f"
      % (se_cell, bra.objective_se(bra.resultant_se(accB)[1]) / ref_pf, np.sqrt(2) * se_cell))
print("rises of the maximum over kappa*, in SEs of a difference:", (steps[steps > 0] / (np.sqrt(2) * se_cell)).round(2))
''')
# noise
setsrc(36, src(36)+'''
# Diagnostics (the verifier's request). (i) In the full network, the run-mean global inhibition
# w_quad pi/N sum max(r, 0) and the zero mode (mean rate) over time. (ii) The same runs with the
# global inhibition held at its noise-free level, so the noise acts only as one more input to
# otherwise unchanged dynamics, as in SI section 5 (Eqs. S107 to S109). There the first Fourier
# mode is neutral (w_even - 1/tau - inhibition = 0 at kappa = 1), and SI Eq. S124 gives each
# coordinate of (x1, x2) the variance 2 sigma^2 / N per unit time, so the amplitude after T is
# Rice distributed: its mean is the SI prediction, above the starting 1.
rows = []
for N in (64, 256):
    tr0 = {}
    bra.rnn_batch(rng, 1, 5, N, 0.0, 1.5, 0.5, traces=tr0)
    inh0 = tr0["inh"][-1]
    for sig in (1.0, 2.0):
        tr = {}
        _, k = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5, traces=tr)
        _, kf = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5, inh_fixed=inh0)
        s_T = np.sqrt(2 * sig ** 2 / N * 5)
        rows.append(dict(N=N, sigma=sig, inh_noise_free=inh0,
                         inh_t01=tr["inh"][9], inh_t1=tr["inh"][99], inh_t5=tr["inh"][-1],
                         zero_mode_t5=tr["zero_mode"][-1], amp_end_full=k[-1].mean(),
                         amp_end_inh_fixed=kf[-1].mean(), se_inh_fixed=kf[-1].std(ddof=1) / np.sqrt(len(kf[-1])),
                         amp_end_SI_rice=stats.rice(b=1 / s_T, scale=s_T).mean()))
print("\\nglobal inhibition and zero mode in the full network, and the end amplitude with the inhibition held:")
print(pd.DataFrame(rows).round(4).to_string(index=False))
''')
# fig4gh
setsrc(42, src(42)+'''
# Monte Carlo error (10,000 runs per rate, performance_scan_figure4g.py). The two networks share
# their runs, so the SE of their difference is below that of two independent estimates, sqrt(2) SE.
se4 = bra.resultant_se(bqa)[0]
print("\\nSE of the attractor's accuracy at 0.1, 0.2, 0.3/s: %s; differences in units of sqrt(2) SE: %s"
      % (se4[2:5].round(4), (d4[2:5] / (np.sqrt(2) * se4[2:5])).round(2)))
print("the same Bayesian attractor in figure4g.npz (dt 0.001) and figure2i.npz (dt 0.01): largest |diff| %.4f at %g/s, %.2f sqrt(2) SE"
      % (np.abs(bqa - accB).max(), R[np.argmax(np.abs(bqa - accB))], np.abs(bqa - accB).max() / (np.sqrt(2) * se4[np.argmax(np.abs(bqa - accB))])))
''')
# figs2
setsrc(45, src(45)+'''
print("NaN cells (N, rate):", [(int(bra.N_S2[a]), float(R[b])) for a, b in np.argwhere(np.isnan(s2))])
# Monte Carlo error: each N is its own scan (performance_scan_figureS2.py, 10,000 runs per rate),
# independent of the reference runs (figure2i scan), so a difference has SE about sqrt(2) SE.
se2 = bra.resultant_se(ref2)
zs2 = (s2 - ref2) / (np.sqrt(2) * se2[0])
print("SE of the reference at 0.1/s: %.4f (bound %.4f); a difference of two independent values: %.4f"
      % (se2[0][2], se2[1][2], np.sqrt(2) * se2[0][2]))
print("N = 16 at 0.1/s: %.4f, %.1f SEs of a difference; |z| above 3 elsewhere: %d of %d"
      % ((s2 - ref2)[3, 2], zs2[3, 2], int(np.sum(np.abs(zs2) > 3)) - 1, int(np.isfinite(zs2).sum()) - 1))
print("at 0.1/s, every N minus the reference:", dict(zip(bra.N_S2.tolist(), (s2[:, 2] - ref2[2]).round(4))))
print("N = 16 at 0.1/s minus the mean of the other six N: %.4f" % (s2[3, 2] - np.delete(s2[:, 2], 3).mean()))
expected = np.nansum(2 * stats.norm.sf(0.02 / (np.sqrt(2) * se2[0]))) * len(bra.N_S2[bra.N_S2 >= 8]) 
print("cells with N >= 8 expected beyond 0.02 by sampling alone, if every network equalled the reference: %.2f" % expected)
''')
# prediction raw variants
s=src(49)
s=s.replace('''    F = bra.raw_roi_fluorescence(f, blocks, s["masks"], "mean", 4.0)
    t = s["t"][np.concatenate([np.arange(i, j) for i, j in blocks])]
    return F - np.percentile(F, 10, axis=0), t''','''    F = bra.raw_roi_fluorescence(f, blocks, s["masks"], "mean", (0, 2, 4))
    t = s["t"][np.concatenate([np.arange(i, j) for i, j in blocks])]
    return F, t''')
s=s.replace('''for s, (F, tF) in zip(sessions, raws):
    a_d = amplitude_by_contrast(s, s["dff"], s["t"])
    a_r = amplitude_by_contrast(s, F, tF)''','''for s, (Fs, tF) in zip(sessions, raws):
    F = Fs[4] - np.percentile(Fs[4], 10, axis=0)   # the main raw signal: smoothing 4 px, 10th percentile
    a_d = amplitude_by_contrast(s, s["dff"], s["t"])
    a_r = amplitude_by_contrast(s, F, tF)''')
s+='''
# raw-signal variants (the verifier's request): in-plane smoothing 0, 2, 4 px and baseline at the
# 5th, 10th or 20th percentile of each ROI, plus the baseline-normalized signal (F - F0) / F0
rows = []
for sm in (0, 2, 4):
    for pct in (5, 10, 20):
        for norm_ in ("F - F0", "(F - F0) / F0"):
            hl = []
            for s, (Fs, tF) in zip(sessions, raws):
                F0 = np.percentile(Fs[sm], pct, axis=0)
                X = Fs[sm] - F0 if norm_ == "F - F0" else (Fs[sm] - F0) / F0
                a_ = amplitude_by_contrast(s, X, tF)
                hl.append((a_[3], a_[2]))
            hl = np.array(hl)
            rows.append(dict(smooth_px=sm, baseline_pct=pct, signal=norm_, high_gt_low=int((hl[:, 0] > hl[:, 1]).sum()),
                             median_ratio=np.median(hl[:, 0] / hl[:, 1]),
                             p_wilcoxon=stats.wilcoxon(hl[:, 0], hl[:, 1], alternative="greater").pvalue))
rv = pd.DataFrame(rows)
print("\\nraw-signal variants, high against low contrast over 15 flies:")
print(rv.round(4).to_string(index=False))
print("variants with p < 0.05: %d of %d; with high > low in more than half the flies: %d of %d"
      % ((rv.p_wilcoxon < 0.05).sum(), len(rv), (rv.high_gt_low > 7).sum(), len(rv)))
'''
setsrc(49,s)
# synthetic test of bra.fourier, in the data check
setsrc(9, src(9)+'''
# bra.fourier on a synthetic bump at ROI angle 1.0 rad over 40 ROIs (two periods): phase sign and amplitude
_n = 40
_ph, _amp = bra.fourier((3 * np.cos(2 * np.pi * 2 * np.arange(_n) / _n - 1.0))[None, :])
print("synthetic bump at +1.000 rad, amplitude 3: phase %+.3f, amplitude %.3f (the phase sign is a convention, see bra.fourier)"
      % (_ph[0], _amp[0]))
print("ROIs per fly (frequency 2 assumes the ROIs span two bump periods):", [s["dff"].shape[1] for s in sessions])
''')
# new sanity cell after 3: source lines
new = code('''# Where the arrays and parameters used below are defined in the released code (lines printed from
# the deposit): the cue rate of Figure 2H, the columns of the stats arrays, the grids of Fig. 3, and
# the number of runs per setting of each scan.
for name, pat in [("Figure2h.ipynb", r"^kappa_z = |alpha = flt.xi_fun_inv|kappa_z_array\\[ind_off"),
                  ("Figure2i.ipynb", r"_stats\\[i,j,|noUncert_stats = np.zeros|vonMises_stats = np.zeros"),
                  ("Figure3b,c,e,d_FigureS3.ipynb", r"^kappa_array = |^\\s+1\\.6,|^\\s+2\\.5,|^\\s+7\\. |^kappa_star_array|^beta_array|MSE_array\\[i,j\\] =|MSE_array = np.array\\(\\[ objective\\(noUncert"),
                  ("Figure3f_FigureS4.ipynb", r"^kappa_star_array|^\\s+1\\.1, 1\\.2|^\\s+2\\.0, 2\\.1|^\\s+3\\.0, 3\\.2|^beta_array|^sigmaN_array|^N = |MSE_array\\[i,j\\] =|^ref = "),
                  ("FigureS2.ipynb", r"^N_array|MSE_array\\[i\\] ="),
                  ("Figure4g,h.ipynb", r"_stats\\[i,\\[0,1\\]\\]|_stats\\[i,2\\]")]:
    print("== " + name)
    print("\\n".join("   " + ln for ln in code.source_lines(name, pat)))
for name in ["performance_scan_figure2i.py", "performance_scan_figure3d.py", "performance_scan_figure3f.py",
             "performance_scan_figure4g.py", "performance_scan_figureS2.py"]:
    print("== %s: %s" % (name, "; ".join(ln.strip() for ln in code.source_lines(name, r"^nIter =|^T = |^dt = "))))
''', ['sanity'])
C.insert(4, new)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
E
cd entries/000289-kutschireiter-2023 && head -c 300 reproduce_kutschireiter_2023.ipynb | head -5; git diff --stat
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d212c268",
 entries/000289-kutschireiter-2023/bra.py | 87 ++++++++++++++++++++++++++++----
 1 file changed, 77 insertions(+), 10 deletions(-)
```

**Agent calls Bash**

```bash
sed -i 's/new = code(/new = code(/; s/C.insert(4, new)/new["id"] = "b7c41e02"; C.insert(4, new)/; s/len(bra.N_S2\[bra.N_S2 >= 8\]) $/len(bra.N_S2[bra.N_S2 >= 8])/' $TMPDIR/edit1.py && tail -c 50 reproduce_kutschireiter_2023.ipynb | od -c | tail -3 && python3 $TMPDIR/edit1.py && git diff --stat && python3 -c "import nbformat;nbformat.validate(nbformat.read('reproduce_kutschireiter_2023.ipynb',4));print('valid')"
```

```
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
 entries/000289-kutschireiter-2023/bra.py           |  87 ++++++++++++--
 .../reproduce_kutschireiter_2023.ipynb             | 131 +++++++++++++++++++--
 2 files changed, 196 insertions(+), 22 deletions(-)
valid
```

**Agent calls Bash**

```bash
python3 -c "
import json;nb=json.load(open('reproduce_kutschireiter_2023.ipynb'))
C=nb['cells']
sel=[1,3,4,19,22,28,43,46]
print('\n'.join(''.join(C[i]['source']) for i in sel))
" > $TMPDIR/t.py && grep -n "^m3d\|^g4 \|^s2 \|^accK\|^score\|^code = \|^for name, pat" $TMPDIR/t.py && time $TMPDIR/dv/bin/python $TMPDIR/t.py 2>&1 | tail -80
```

```
14:code = bra.Code()          # the paper's Zenodo deposit, in memory, md5 checked
41:for name, pat in [("Figure2h.ipynb", r"^kappa_z = |alpha = flt.xi_fun_inv|kappa_z_array\[ind_off"),
53:accK, accB, kK, kB = vm[0, :, 1], vq[0, :, 1], vm[0, :, 2], vq[0, :, 2]
67:score = np.array([bra.objective(nu[i, :, 1]) for i in range(len(bra.KAPPA_FIXED))])
79:m3d = code.npz("figure3d.npz")["MSE_array"] / ref_pf
106:g4 = code.npz("figure4g.npz")
122:s2 = code.npz("figureS2.npz")["MSE_array"]
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 7, in <module>
    import bra
ModuleNotFoundError: No module named 'bra'

real	0m1.912s
user	0m2.443s
sys	0m0.101s
```

**Agent calls Bash**

```bash
PYTHONPATH=. $TMPDIR/dv/bin/python $TMPDIR/t.py 2>&1 | grep -v "^data_processed\|^[A-Za-z0-9_,]*\.\(py\|ipynb\)$" | tail -120
```

```
vonMises_stats[i,[0,1]] = flt.circular_mean(flt.backToCirc(vonMises[:,0]-phi_final))
           vonMises_q_stats[i,[0,1]] = flt.circular_mean(flt.backToCirc(vonMises_q[:,0]-phi_final))
           CX_stats[i,[0,1]] = flt.circular_mean(flt.backToCirc(CX[:,0]-phi_final))
== performance_scan_figure2i.py: nIter = 10000; T = 20 # simulation time; dt = 0.01 # step size
== performance_scan_figure3d.py: nIter = 10000; T = 20 # simulation time; dt = 0.01 # step size
== performance_scan_figure3f.py: nIter = 10000; T = 20 # simulation time; dt = 0.01 # step size
== performance_scan_figure4g.py: nIter = 10000; T = 20 # simulation time; dt = 0.001 # step size
== performance_scan_figureS2.py: nIter = 10000; T = 20 # simulation time; dt = 0.01 # step size
  rate  acc_circKF  acc_attractor    diff  cert_circKF  cert_attractor
  0.01      0.1020         0.0292 -0.0729       0.1763          1.0006
  0.03      0.1529         0.0694 -0.0835       0.3076          1.0013
  0.10      0.2732         0.2159 -0.0573       0.5602          1.0525
  0.20      0.3552         0.3214 -0.0337       0.7931          1.1625
  0.30      0.4217         0.3966 -0.0251       0.9756          1.2657
  0.40      0.4677         0.4588 -0.0089       1.1226          1.3594
  0.50      0.5063         0.4947 -0.0116       1.2674          1.4644
  0.60      0.5359         0.5286 -0.0073       1.3900          1.5546
  0.70      0.5680         0.5657 -0.0023       1.4781          1.6158
  0.80      0.5809         0.5796 -0.0013       1.5643          1.6804
  0.90      0.6094         0.6081 -0.0012       1.6750          1.7668
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
PYTHONPATH=. $TMPDIR/dv/bin/python $TMPDIR/t.py 2>&1 | sed -n '/^== Figure2h/,/^== performance_scan_figure2i/p'
```

```
== Figure2h.ipynb
   kappa_z = 15 # precision of absolute heading info (called gamma_z in manuscript)
   alpha = flt.xi_fun_inv(kappa_z*dt)
   kappa_z_array[ind_off:ind_on] = 0 # maximally uninformative while light is off
== Figure2i.ipynb
       vonMises_stats = np.zeros([len_k,len_kz,3]) # 1st (bias + variance) and 2nd order statistics for each kappa_z,
       noUncert_stats = np.zeros([len_k,len_kz,2])
                   vonMises_stats[i,j,2] = np.mean(vonMises[:,1])
                   vonMises_q_stats[i,j,2] = np.mean(vonMises_q[:,1])
                   PF_stats[i,j,2] = np.mean(PF[:,1])
                   vonMises_stats[i,j,[0,1]] = flt.circular_mean(flt.backToCirc(vonMises[:,0]-phi_final))
                   vonMises_q_stats[i,j,[0,1]] = flt.circular_mean(flt.backToCirc(vonMises_q[:,0]-phi_final))
                   PF_stats[i,j,[0,1]] = flt.circular_mean(flt.backToCirc(PF[:,0]-phi_final))
== Figure3b,c,e,d_FigureS3.ipynb
   kappa_array = np.array([  0.1,   0.3,   0.9,   1. ,   1.1,   1.2,   1.3,   1.4,   1.5,
            1.6,   1.7,   1.8,   1.9,   2. ,   2.1,   2.2,   2.3,   2.4,
            2.5,   2.6,   2.7,   2.8,   2.9,   3. ,   4. ,   5. ,   6. ,
            7. ,   8. ,   9. ,  10. ,  30. , 100. ])
   MSE_array = np.array([ objective(noUncert_stats[i,:,1],mu=mu_perf,sigma=sig_perf) for i in np.arange(len(kappa_array))])
   kappa_array = np.arange(0.2,10,0.01) # own uncertainty right before update
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'E'
import json
p='reproduce_kutschireiter_2023.ipynb'; nb=json.load(open(p))
c=nb['cells'][4]; s=''.join(c['source'])
s=s.replace(r'''("Figure2i.ipynb", r"_stats\\[i,j,|noUncert_stats = np.zeros|vonMises_stats = np.zeros"),''',
 r'''("circularFiltering.py", r"def circular_mean|return phi_hat, r_hat"),
                  ("Figure2i.ipynb", r"_stats\\[i,j,|_stats\\[i,j\\] =|noUncert_stats = np.zeros|vonMises_stats = np.zeros"),''')
s=s.replace(r'''|^ref = "),''', r'''|^ref = |max_MSE\\[ind_sig\\] =|noretuning_MSE\\[ind_sig\\] =|idx_ref = idx"),''')
assert 'circularFiltering.py' in s and 'idx_ref' in s
c['source']=s.splitlines(True)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
E
python3 -c "
import json;nb=json.load(open('reproduce_kutschireiter_2023.ipynb'));print(''.join(nb['cells'][4]['source']))" | head -12; date -u
```

```
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
AssertionError
# Where the arrays and parameters used below are defined in the released code (lines printed from
# the deposit): the cue rate of Figure 2H, the columns of the stats arrays, the grids of Fig. 3, and
# the number of runs per setting of each scan.
for name, pat in [("Figure2h.ipynb", r"^kappa_z = |alpha = flt.xi_fun_inv|kappa_z_array\[ind_off"),
                  ("Figure2i.ipynb", r"_stats\[i,j,|noUncert_stats = np.zeros|vonMises_stats = np.zeros"),
                  ("Figure3b,c,e,d_FigureS3.ipynb", r"^kappa_array = |^\s+1\.6,|^\s+2\.5,|^\s+7\. |^kappa_star_array|^beta_array|MSE_array\[i,j\] =|MSE_array = np.array\(\[ objective\(noUncert"),
                  ("Figure3f_FigureS4.ipynb", r"^kappa_star_array|^\s+1\.1, 1\.2|^\s+2\.0, 2\.1|^\s+3\.0, 3\.2|^beta_array|^sigmaN_array|^N = |MSE_array\[i,j\] =|^ref = "),
                  ("FigureS2.ipynb", r"^N_array|MSE_array\[i\] ="),
                  ("Figure4g,h.ipynb", r"_stats\[i,\[0,1\]\]|_stats\[i,2\]")]:
    print("== " + name)
    print("\n".join("   " + ln for ln in code.source_lines(name, pat)))
for name in ["performance_scan_figure2i.py", "performance_scan_figure3d.py", "performance_scan_figure3f.py",
Fri Oct 30 00:51:14 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'E'
import json
p='reproduce_kutschireiter_2023.ipynb'; nb=json.load(open(p))
c=nb['cells'][4]; s=''.join(c['source'])
s=s.replace(r'''("Figure2i.ipynb", r"_stats\[i,j,|noUncert_stats = np.zeros|vonMises_stats = np.zeros"),''',
 r'''("circularFiltering.py", r"def circular_mean|return phi_hat, r_hat"),
                  ("Figure2i.ipynb", r"_stats\[i,j,|_stats\[i,j\] =|noUncert_stats = np.zeros|vonMises_stats = np.zeros"),''')
s=s.replace(r'''|^ref = "),''', r'''|^ref = |max_MSE\[ind_sig\] =|noretuning_MSE\[ind_sig\] =|idx_ref = idx"),''')
assert 'circularFiltering.py' in s and 'idx_ref' in s
c['source']=s.splitlines(True)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
E
PYTHONPATH=. $TMPDIR/dv/bin/python -c "
import bra;code=bra.Code()
print(code.source_lines('circularFiltering.py', r'def circular_mean|return phi_hat, r_hat'))
print(code.source_lines('Figure2i.ipynb', r'_stats\[i,j\] ='))
print(code.source_lines('Figure3f_FigureS4.ipynb', r'max_MSE\[ind_sig\] =|noretuning_MSE\[ind_sig\] =|idx_ref = idx'))"
```

```
['def circular_mean(phi,w=None):', '    return phi_hat, r_hat']
['                noUncert_stats[i,j] = flt.circular_mean(flt.backToCirc(noUncert - phi_final))', '                noUncert_stats[i,j] = flt.circular_mean(flt.backToCirc(noUncert - phi_final))']
['        idx_ref = idx', '    max_MSE[ind_sig] = np.nanmax(MSE_array)', '    noretuning_MSE[ind_sig] = MSE_array[idx_ref]']
```

**Agent calls Bash**

```bash
cd  && time python tools/entry.py all entries/000289-kutschireiter-2023 2>&1 | tail -20
```

```
Installed kernelspec registry-000289-kutschireiter-2023 in executed/000289-kutschireiter-2023/.venv/share/jupyter/kernels/registry-000289-kutschireiter-2023
0 error(s)
pass  reproduce_kutschireiter_2023.ipynb  (382 s)

real	6m28.718s
user	6m26.596s
sys	0m17.408s
```

**Agent calls Bash**

```bash
python3 - <<'E'
import json
nb=json.load(open('executed/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
for i in [10,37,40,50]:
    c=nb['cells'][i]
    print('=====',i,''.join(c['source'])[:60])
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        t=''.join(t)
        print(t[-6000:] if i==50 else t[-3500:])
E
```

```
===== 10 # --- does the bump follow the cue on the session's clock? B
zero contrast, phase-cue coherence by lag (frames): {-30: np.float64(0.078), -25: np.float64(0.084), -20: np.float64(0.093), -15: np.float64(0.103), -10: np.float64(0.106), -5: np.float64(0.116), 0: np.float64(0.13), 5: np.float64(0.124), 10: np.float64(0.112), 15: np.float64(0.115), 20: np.float64(0.102), 25: np.float64(0.104), 30: np.float64(0.104)}
low  contrast, phase-cue coherence by lag (frames): {-30: np.float64(0.375), -25: np.float64(0.38), -20: np.float64(0.396), -15: np.float64(0.42), -10: np.float64(0.436), -5: np.float64(0.463), 0: np.float64(0.533), 5: np.float64(0.532), 10: np.float64(0.483), 15: np.float64(0.457), 20: np.float64(0.442), 25: np.float64(0.428), 30: np.float64(0.403)}
high contrast, phase-cue coherence by lag (frames): {-30: np.float64(0.513), -25: np.float64(0.538), -20: np.float64(0.568), -15: np.float64(0.602), -10: np.float64(0.658), -5: np.float64(0.714), 0: np.float64(0.79), 5: np.float64(0.762), 10: np.float64(0.694), 15: np.float64(0.659), 20: np.float64(0.621), 25: np.float64(0.577), 30: np.float64(0.542)}
lag of peak coherence in high contrast, per fly (frames): [np.int64(0), np.int64(5), np.int64(0), np.int64(0), np.int64(0), np.int64(5), np.int64(5), np.int64(0), np.int64(0), np.int64(5), np.int64(0), np.int64(5), np.int64(5), np.int64(5), np.int64(0)]
median coherence in frames labelled high contrast: true labels 0.790, labels shifted one block 0.390
flies where the true labels give the higher coherence: 12 of 15
synthetic bump at +1.000 rad, amplitude 3: phase -1.000, amplitude 3.000 (the phase sign is a convention, see bra.fourier)
ROIs per fly (frequency 2 assumes the ROIs span two bump periods): [37, 38, 39, 41, 42, 43, 47, 41, 44, 44, 42, 43, 42, 44, 41]

===== 37 # the batched copy against the released RNN_filter_Run, same
batched vs released, max abs difference: position 1.11e-16, amplitude 4.44e-16

         mean_dmu        se         z           
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;nb=json.load(open('entries/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
for i in [5,12,13,14]: print('=====',i); print(''.join(nb['cells'][i]['source']))"
```

```
===== 5
The processed outputs have the shapes the figure notebooks expect, accuracies lie in 0 to 1, and the
particle filter reference computed from `figure2i.npz` equals the constant hard-coded in
`Figure3f_FigureS4.ipynb`, so the two notebooks normalize alike. The certainty stored for the
Bayesian ring attractor never falls below 1, its baseline kappa* (Methods), while the circKF's falls
to 0.18.
===== 12
## fig1-conflict-decreases-certainty

> In the circular Kalman filter, an HD observation consistent with the current estimate increases
> certainty, while one that strongly conflicts with it (opposite direction) decreases certainty.

The code's circKF step, `vM_Projection` (kappa_phi = 1, kappa_v = 1, dt = 0.01), from mu = 0 at
kappa_t = 1, 2, 5, with the per-step reliability xi_fun_inv(gamma_z dt) for gamma_z = 1/s and 10/s.
(a) is the vector addition alone (the code's update on the natural parameters); (b) is the full
step against the same step with no observation.
===== 13
rows = []
for gz in (1, 10):
    alpha = flt.xi_fun_inv(gz * 0.01)
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/edit2.py <<'E'
import json
p='entries/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'; nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(True)
def chk(i, start): assert src(i).startswith(start), (i, src(i)[:40])
chk(5,"The processed outputs")
setsrc(5, src(5)+'''
The lines printed from the released code fix what the arrays mean. In `Figure2h.ipynb`,
`kappa_z = 15` is commented "called gamma_z in manuscript" and enters as `xi_fun_inv(kappa_z*dt)`.
Every `*_stats` array holds `circular_mean` of the end errors in columns 0 and 1 (phase, then
`r_hat`, the accuracy |m1|) and, where present, the mean certainty in column 2; `noUncert_stats`
has the first two only, with axis 0 the 33 kappa* of `kappa_array`. In `figure3d.npz` and the
`figure3f` files, axis 0 is `kappa_star_array` and axis 1 `beta_array`, as the loops
`MSE_array[i,j]` show; the rows of `figureS2.npz` follow `N_array`. Every scan averages 10,000 runs
of 20 s per setting (dt 0.01; 0.001 for Fig. 4G), which sets the Monte Carlo error used in the
sections below: the standard error of an accuracy near 0.2 (0.1/s) is about 0.007, and that of a
difference between two independent scans about 0.010.
''')
chk(14,"**Result: reproduced.**")
setsrc(14, src(14)+''' Comparison (a) is a weak test: adding an observation of weight alpha at
the estimate or opposite to it gives kappa + alpha and |kappa - alpha|, so it holds for any
0 < alpha < 2 kappa; (b) is the informative comparison.
''')
chk(29,"**Result: partially reproduced.**")
setsrc(29, src(29).rstrip()+''' The two rises are 0.32 and 0.52 standard errors of a difference
between two grid cells (0.0026), so they are within the scan's sampling error; the criterion gives
no tolerance, so the outcome stays partial.
''')
chk(38,"**Result: partially reproduced.**")
setsrc(38, '''**Result: partially reproduced.** The batched network matches the released function to rounding
error. The position diffuses without bias: its mean change is within 2 standard errors of 0 in all
four settings (z = -0.74 to 0.82) and its variance grows at every second. The SD of the one-step
amplitude increments at N = 256 is half that at N = 64 (ratios 0.500 and 0.501). But in the full
network the mean amplitude does not drift upward: it falls throughout the run and ends below the
noise-free value of 1.0 in all four settings (0.42 to 0.83), so condition (2) fails as the criterion
runs it.

The diagnostics show why. The noise raises the rectified sum that drives the global inhibition,
from 0.5 without noise to 0.52 to 0.59 at 0.1 s and 0.57 to 0.76 at 1 s, and that extra inhibition
shrinks the bump; the zero mode stays near 0 (at most 0.014 in size). With the inhibition held at
its noise-free level, so that the noise is only one more input to otherwise unchanged dynamics as in
SI section 5, the mean amplitude rises: 1.08, 1.33, 1.01 and 1.07 after 5 s, against 1.08, 1.35, 1.02
and 1.08 from the Rice mean that SI Eq. S124 implies, each within 2.4 standard errors. So the
upward drift the SI derives is present in the noise's direct effect, and in the released network it
is outweighed by the noise's effect on the global inhibition. The criterion tests the full network;
whether that is what the paper claims is asked of a reader (questions/000289.yaml).
''')
chk(41,"**Result: reproduced")
setsrc(41, '''**Result: partially reproduced.** The criterion asks for both sorts, and only reading (a), by the
PB glomerulus in the name, can be formed; reading (b) cannot (data check). Under reading (a), and
counting any synapse, both parts hold. Left PEN1 neurons send their EPG output a mean of +0.56
glomeruli from their EPG input (10 of 10 positive) and right ones -0.48 (9 of 10 negative),
opposite directions, both different from 0 (Wilcoxon, printed above); with partners from both
sides, +0.37 and -0.35. Every Delta7 receives EPG input from at least 13 of the 16 glomeruli and
sends output to EPG neurons in at least 9. The output side depends on the threshold: counting only
glomeruli with at least 3 or 5 synapses, Delta7 outputs reach more than half the glomeruli in 7 and
0 of 42 neurons (printed above), while the inputs still do in 42 of 42.
''')
chk(44,"**Result: partially reproduced.**")
setsrc(44, src(44).rstrip()+''' The three differences above 0.01 are 1.95, 1.51 and 1.16 times
sqrt(2) standard errors (the SE of a difference of two independent scans; the two networks share
their runs, so the actual SE of their difference is smaller). The same Bayesian attractor differs
by 0.022 between figure4g.npz (dt 0.001) and figure2i.npz (dt 0.01) at 0.1/s, 2.2 such units, so the
0.01 bound is near the scans' sampling error at the low rates.
''')
chk(47,"**Result: partially reproduced.**")
setsrc(47, '''**Result: not reproduced.** Of the 7 x 23 values, one is more than 0.02 from the reference: N = 16
at 0.1/s, 0.041 below it. All others, N = 3 and 4 included, are within 0.019. Both readings (N of 8
and more, N of 16 and more) include N = 16, so neither holds, and the criterion requires both. The
one deviation is not sampling error: it is 4.3 standard errors of a difference of two independent
scans (0.0096), no other value is beyond 3, and it is 0.029 below the mean of the other six sizes at
the same rate. Sampling alone would put about 1.2 values beyond 0.02 if every network equalled the
reference, so the bound is near the scans' sampling error, but this value is far beyond it. At
every other network size and rate the accuracy is close to the reference. One value (N = 128 at
100/s) is missing in the stored array.
''')
chk(51,"**Result: blocked (methods_underspecified).**")
setsrc(51, src(51).rstrip()+''' Across 18 variants of the raw signal (smoothing 0, 2 or 4 pixels;
baseline at the 5th, 10th or 20th percentile; F - F0 or (F - F0) / F0), high exceeds low contrast
in more than half the flies in 16, and p < 0.05 in 9: in all nine F - F0 variants (p 0.021 to
0.042) and in none of the nine (F - F0) / F0 variants (p 0.11 to 0.89). The split between the
readings follows the division by the baseline, not the smoothing or the percentile.
''')
chk(52,"## Summary")
s=src(52)
s=s.replace("| fig4b-connectome-motifs | reproduced, assumed (one sort, any synapse) |","| fig4b-connectome-motifs | partially reproduced, assumed (one sort of two, any synapse) |")
s=s.replace("| figs2-performance-independent-of-n | partially reproduced |","| figs2-performance-independent-of-n | not reproduced |")
s=s.replace("re-run (10,000 trajectories per setting is beyond the time limit).","re-run (10,000 trajectories per setting is beyond the time limit); their Monte Carlo error is\nestimated from the stored accuracies.")
s=s.replace("checked against it.","checked against it, with a variant that holds the global inhibition at its noise-free level.")
assert "not reproduced |" in s and "Monte Carlo" in s and "noise-free level" in s
setsrc(52,s)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
E
python3 $TMPDIR/edit2.py && echo done
```

```
done
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023 && sed -i 's/and 1.08 from the Rice mean that SI Eq. S124 implies, each within 2.4 standard errors/and 1.08 from the Rice mean that SI Eq. S124 implies, each within 1.5 standard errors/' reproduce_kutschireiter_2023.ipynb && grep -c "within 1.5 standard" reproduce_kutschireiter_2023.ipynb; cat README.md
```

```
1
# Kutschireiter, Basnak, Wilson & Drugowitsch (2023) with dandiset 000289

Tests the findings of [Kutschireiter et al. (2023)](https://doi.org/10.1073/pnas.2210622120),
"Bayesian inference in ring attractor networks", a theory paper. The dandiset it is linked to,
[DANDI:000289](https://dandiarchive.org/dandiset/000289/0.240801.1040), holds two-photon imaging of
EPG neurons from a separate study of the same lab (Basnak et al.), which this paper does not analyse.

- Twelve claims are simulation or connectome results. They are tested on the paper's released code
  and processed outputs ([Zenodo 7615975](https://doi.org/10.5281/zenodo.7615975)) and on the public
  hemibrain v1.2 connectome export, not on the dandiset.
- One claim, the Discussion's prediction that bump amplitude is higher with a reliable cue, is
  tested on the dandiset's cue-contrast experiment (15 flies, visual cue at zero, low and high
  contrast).

| Claim | Outcome |
|---|---|
| A conflicting HD observation lowers the circKF's certainty, a confirming one raises it | Reproduced |
| An 80-neuron Bayesian ring attractor tracks the circKF, and its amplitude decays in darkness | Reproduced |
| The attractor matches the circKF's accuracy for reliable cues, not for unreliable ones | Reproduced |
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='README.md'; s=open(p).read()
s=s.replace("| Connectome motifs: shifted PEN1 projections, broad Delta7 inhibition | Reproduced (assumed) |","| Connectome motifs: shifted PEN1 projections, broad Delta7 inhibition | Partially reproduced (assumed; one sort of two) |")
s=s.replace("| Accuracy depends little on the number of neurons | Partially reproduced |","| Accuracy depends little on the number of neurons | Not reproduced (one value of 161) |")
s=s.replace("single-population network.","single-population network, with diagnostics of its global inhibition; the Monte Carlo error of\n  the stored accuracies.")
s=s.replace("It takes about nine minutes","It takes about seven minutes")
open(p,'w').write(s)
E
grep -n "Partially reproduced (assumed\|Not reproduced (one" README.md
```

```
26:| Connectome motifs: shifted PEN1 projections, broad Delta7 inhibition | Partially reproduced (assumed; one sort of two) |
28:| Accuracy depends little on the number of neurons | Not reproduced (one value of 161) |
```

**Agent calls Bash**

```bash
cd  ls schemas; grep -rn "questions" tools/entry.py | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent calls Write**

```json
{
 "file_path": "questions/000289.yaml",
 "content": "dandiset: \"000289\"\npaper: doi:10.1073/pnas.2210622120\nquestions:\n- claim: noise-effects-on-mu-and-kappa\n  asked: 2026-10-30\n  question: >-\n    Condition (2) of the criterion compares the mean end amplitude of the full released network\n    (RNN_filter_Run, with its rectified global inhibition) with a noise-free run. Does the paper\n    claim that upward drift for the full network, or only for the noise's direct effect on the\n    first Fourier mode, with the remaining dynamics unchanged, as SI section 5 derives it? If the\n    latter, should condition (2) be tested with the global inhibition held at its noise-free level,\n    or against the drift of SI Eqs. S122 and S123?\n  passage: >-\n    \"With neural noise, the population dynamics equation Eq. [S49] becomes dr_t(phi) = ... +\n    I_ext(phi) + eta_t(phi) [S107] ... This shows that we can interpret neural noise as yet another\n    stochastic input to the network.\" (SI Appendix, section 5A); \"<dkappa> = sigma_nn^2 / (kappa N)\n    dt\" (Eq. S123); \"it causes a positive drift and random diffusion of kappa_t\" (Results, The\n    Impact of Neural Noise on Inference Accuracy).\n  why: >-\n    In the full network the noise also raises the rectified sum that drives the global inhibition\n    (from 0.5 to 0.57 to 0.76 after 1 s), and the mean amplitude falls to 0.42 to 0.83 after 5 s,\n    so (2) fails and the claim is partially reproduced. With the inhibition held at its noise-free\n    level the mean amplitude rises to 1.01 to 1.33, matching the mean that SI Eq. S124 implies\n    (1.02 to 1.35), so (2) would hold and the claim would be reproduced.\n"
}
```

```
File created successfully at: questions/000289.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['verifications'],indent=1)[:3000])"
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
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'E'
p='attempts/000289-kutschireiter-2023-01.yaml'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep('''    (for example kappa_t 1, 10/s, 1.453 and 0.547) and for the full step against the step without
    observation (1.447 and 0.546 against 0.997).''','''    (for example kappa_t 1, 10/s, 1.453 and 0.547) and for the full step against the step without
    observation (1.447 and 0.546 against 0.997). The first comparison holds for any weight alpha
    between 0 and 2 kappa_t, so it is a weak test; the second is the informative one.''')
rep('''    them and may be sampling noise of the scan; this was not tested.''','''    them. With 10,000 runs per rate in each grid cell, the standard error of a cell's normalized
    performance is 0.0018 and that of a difference of two cells 0.0026, so the rises are 0.32 and
    0.52 standard errors, within sampling error. The criterion gives no tolerance, so condition 4
    fails as written.''')
rep('''    RNN_filter_Run the noise also enters the rectified sum that drives the global inhibition, which
    may explain the fall; the SI derivation is not checked here.''','''    RNN_filter_Run the noise also raises the rectified sum that drives the global inhibition (from
    0.5 without noise to 0.57 to 0.76 at 1 s), and the zero mode stays near 0. With the inhibition
    held at its noise-free level, so that the noise is only one more input to unchanged dynamics as
    in SI section 5 (Eqs. S107 to S109), the mean amplitude rises to 1.08, 1.33, 1.01 and 1.07 after
    5 s, within 1.5 standard errors of the mean that SI Eq. S124 implies (1.08, 1.35, 1.02, 1.08).
    So the SI's upward drift is present in the noise's direct effect, and in the released network
    the effect on the inhibition outweighs it. The criterion tests the full network; whether the
    paper claims the drift for the full network is asked of a reader (questions/000289.yaml).''')
rep('''- claim: fig4b-connectome-motifs
  outcome: reproduced''','''- claim: fig4b-connectome-motifs
  outcome: partially_reproduced''')
rep('''    Delta7 to EPG side depends on the threshold. Reading (b), by ellipsoid body or gall position,
    could not be run.''','''    Delta7 to EPG side depends on the threshold. Reading (b), by ellipsoid body or gall position,
    could not be run, and the criterion requires both, so the claim holds in part (changed from
    reproduced after verification round 1).''')
rep('''- claim: figs2-performance-independent-of-n
  outcome: partially_reproduced''','''- claim: figs2-performance-independent-of-n
  outcome: not_reproduced''')
rep('''    is within 0.019. Both readings include N 16, so neither holds as written. One value (N 128 at
    100/s) is missing (NaN) in the stored array.''','''    is within 0.019. Both readings include N 16, so neither holds, and the criterion requires both
    (changed from partially_reproduced after verification round 1). The deviation is not sampling
    error. With 10,000 runs per rate, the standard error of a difference of two independent scans
    at 0.1/s is 0.0096, and N 16 is 4.3 of them below the reference, with no other value beyond
    3, and 0.029 below the mean of the other six sizes at that rate. The 0.02 bound is near the
    sampling error at low rates (about 1.2 values beyond it expected by chance alone), but this
    value is far beyond it. One value (N 128 at 100/s) is missing (NaN) in the stored array.''')
rep('''    at 0.4/s and above the difference is at most 0.004.''','''    at 0.4/s and above the difference is at most 0.004.''') if False else None
rep('''    0.4/s and above the difference is at most 0.004. Mean certainties, reported only, are lower in''','''    0.4/s and above the difference is at most 0.004. The three differences above 0.01 are 1.95,
    1.51 and 1.16 times the standard error of a difference of two independent scans (the two
    networks share their runs, so the actual error is smaller), and the same Bayesian attractor
    differs by 0.022 between figure4g.npz and figure2i.npz at 0.1/s, so the 0.01 bound is near the
    sampling error there. Mean certainties, reported only, are lower in''')
rep('''    14 (p 0.21) and raw 11 of 14 (p 0.034). Question for the paper's authors (finding below). The''','''    14 (p 0.21) and raw 11 of 14 (p 0.034). Across 18 variants of the raw signal (smoothing 0, 2 or
    4 pixels, baseline at the 5th, 10th or 20th percentile, F - F0 or (F - F0) / F0), p is below
    0.05 in all nine F - F0 variants (0.021 to 0.042) and in none of the nine divided by F0 (0.11 to
    0.89), so the split between the readings follows the division by the baseline. Question for
    the paper's authors (finding below). The''')
rep('''    each ROI's 10th percentile. The projection and the smoothing were chosen as those that best
    reproduce the stored dF/F (median correlation over ROIs 0.93, against 0.66 without smoothing).''','''    each ROI's 10th percentile. The projection and the smoothing were chosen as those that best
    reproduce the stored dF/F (median correlation over ROIs 0.93, against 0.66 without smoothing).
    Smoothing 0 and 2 pixels, baselines at the 5th and 20th percentile and the baseline-divided
    signal are shown as variants.''')
rep('''- kind: code_mismatch
  statement: >-
    In the released single-population network (RNN_filter_Run) at the Bayesian ring attractor's
    parameters, additive neural noise lowers the mean bump amplitude (from 1.00 to 0.42 to 0.83
    after 5 s, N 64 and 256, noise SD 1 and 2). The Results and SI Appendix section 5 say the noise
    causes a positive drift of the amplitude.''','''- kind: code_mismatch
  statement: >-
    In the released single-population network (RNN_filter_Run) at the Bayesian ring attractor's
    parameters, additive neural noise lowers the mean bump amplitude (from 1.00 to 0.42 to 0.83
    after 5 s, N 64 and 256, noise SD 1 and 2). The Results and SI Appendix section 5 say the noise
    causes a positive drift of the amplitude. The fall comes from the noise raising the rectified
    sum that drives the global inhibition; with the inhibition held at its noise-free level the
    amplitude rises as SI Eq. S124 implies (1.01 to 1.33).''')
open(p,'w').write(s)
E
grep -n "4gh\|fig4gh" -A8 attempts/000289-kutschireiter-2023-01.yaml | grep -n "sampling"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n "1.95\|division by the baseline\|1.5 standard\|4.3 of them\|0.32 and\|weak test\|changed from" attempts/000289-kutschireiter-2023-01.yaml
```

```
48:    between 0 and 2 kappa_t, so it is a weak test; the second is the informative one.
105:    performance is 0.0018 and that of a difference of two cells 0.0026, so the rises are 0.32 and
149:    5 s, within 1.5 standard errors of the mean that SI Eq. S124 implies (1.08, 1.35, 1.02, 1.08).
174:    could not be run, and the criterion requires both, so the claim holds in part (changed from
200:    0.4/s and above the difference is at most 0.004. The three differences above 0.01 are 1.95,
215:    (changed from partially_reproduced after verification round 1). The deviation is not sampling
217:    at 0.1/s is 0.0096, and N 16 is 4.3 of them below the reference, with no other value beyond
239:    0.89), so the split between the readings follows the division by the baseline. Question for
```

**Agent calls Bash**

```bash
git log -1 --format=%ci b12dc10d4; tail -5 attempts/000289-kutschireiter-2023-01.yaml; head -30 transcripts/000289/verifier-1.md | cut -c1-300
```

````
2026-10-30 00:42:01 +0000
    parameters, additive neural noise lowers the mean bump amplitude (from 1.00 to 0.42 to 0.83
    after 5 s, N 64 and 256, noise SD 1 and 2). The Results and SI Appendix section 5 say the noise
    causes a positive drift of the amplitude. The fall comes from the noise raising the rectified
    sum that drives the global inhibition; with the inhibition held at its noise-free level the
    amplitude rises as SI Eq. S124 implies (1.01 to 1.33).
# 000289 · verifier-1 · run 40979919978

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `Tas

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; find . -maxdepth 2 -type f | head -50
```

```
total 156
drwxr-xr-x 6 runner runner   4096 Oct 30 00:37 .
drwxr-xr-x 7 runner runner   4096 Oct 30 00:37 ..
[... 16 more lines not kept]
````

**Agent calls Bash**

```bash
cat >> attempts/000289-kutschireiter-2023-01.yaml <<'E'
verifications:
- date: '2026-10-30'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: >-
    Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper. The verifier recomputed the prediction's
    p-values from the printed table, tested bra.fourier on a synthetic bump and checked the asset
    count of the dandiset version. Its report had no attempt record and gave its own outcome for
    each claim; 11 of 13 agree with the record, and fig4b-connectome-motifs and
    figs2-performance-independent-of-n do not.
  results:
  - claim: fig1-conflict-decreases-certainty
    agrees: true
    outcome: reproduced
    reason: >-
      (a) and (b) hold in 6 of 6 cases (kappa_t 1, 2, 5; gamma_z 1 and 10/s); at kappa_t 5 and
      gamma_z 1 the full step gives 5.039 (confirmatory) against 4.904 (no observation) against
      4.768 (opposite). Comparison (a) holds by construction for any 0 < alpha < 2 kappa, so it is
      a weak test, although it follows the criterion (B7).
    response: >-
      The conclusion and notes now say that (a) is a weak test and (b) the informative one.
      Outcome kept.
  - claim: fig2h-bump-tracks-circkf
    agrees: true
    outcome: reproduced
    reason: >-
      At rates 15 and 10 the network-to-circKF difference is 0.016 and 0.021 rad, against a circKF
      error of 0.483 and 0.491; correlation over cue periods 0.994 and 0.993. In darkness the
      amplitude falls from 7.21 to 1.22 and from 5.89 to 1.21, ending closer to kappa* 1. It could
      not check that kappa_z = 15 in Figure2h.ipynb is gamma_z.
    response: >-
      A data-check cell now prints the defining lines of the released code; Figure2h.ipynb has
      "kappa_z = 15 # precision of absolute heading info (called gamma_z in manuscript)". Outcome
      kept.
  - claim: fig2i-accuracy-and-certainty-vs-reliability
    agrees: true
    outcome: reproduced
    reason: >-
      The largest accuracy difference is 0.0010 at rates of 1/s and above and 0.0003 at 3/s and
      above, so all four combinations pass. At 0.01 to 0.1/s the attractor is less accurate
      (-0.073, -0.084, -0.057) and more certain (+0.82, +0.69, +0.49).
    response: No change needed.
  - claim: fig3b-bayesian-beats-conventional
    agrees: true
    outcome: reproduced
    reason: >-
      The optimal kappa* is 1.7. The Bayesian attractor is more accurate at all 23 rates (smallest
      difference 0.0115) and strictly above from 0.1 to 10/s (smallest 0.034). The not-judged part
      fails, the smallest differences being at 0.01, 2 and 3/s. It could not check the column
      meaning of noUncert_stats or the axis of KAPPA_FIXED.
    response: >-
      The data check now prints the lines that define them; noUncert_stats holds circular_mean
      (phase, r_hat) per kappa* of kappa_array (axis 0) and rate. Outcome kept.
  - claim: fig3c-update-weights
    agrees: true
    outcome: reproduced
    reason: >-
      The largest difference at 1/s and above is 0.0010 under reading (i) and 0.0062 under (ii),
      within both 0.02 and 0.05; under both readings the largest difference is at 0.01/s.
    response: No change needed.
  - claim: fig3d-best-network-slow-decay
    agrees: true
    outcome: partially_reproduced
    reason: >-
      Conditions 1, 2, 3 and 5 hold (best network kappa* 0.7, beta 0.3; the Bayesian attractor
      0.57% below it). Condition 4 fails, the maximum over kappa* rising twice above the best beta
      (+0.0008, +0.0014); overall Spearman rho -0.98. The two rises are probably sampling noise,
      but the criterion gives no tolerance (B3). It asked for the per-rate Monte Carlo SE and
      could not check the axis assignment of KSTAR_3D and BETA_GRID.
    response: >-
      Added the Monte Carlo error. The SE of a cell's normalized performance is 0.0018 and of a
      difference of two cells 0.0026, so the rises are 0.32 and 0.52 SE. The defining lines show
      axis 0 is kappa_star_array and axis 1 beta_array. Outcome kept, as the criterion has no
      tolerance.
  - claim: fig3f-noise-drop-below-70
    agrees: true
    outcome: reproduced
    reason: >-
      Untuned performance is 63.1% at SD 10 and 38.1% at SD 20 under both normalizations, all
      below 70%. Retuned performance is a maximum over noisy grid cells, which biases it upward;
      the paper's notebook does the same (B10).
    response: >-
      No change. The bias concerns the retuned performance, which this claim does not judge, and
      the analysis follows the paper's notebook. The defining lines of the Figure 3F grids are
      now printed.
  - claim: fig3f-retuning-reduces-drop
    agrees: true
    outcome: reproduced
    reason: >-
      3 of 6 readings fall in 31.5 to 38.5% (34.64 and 34.56 at SD 10; 31.67 for the
      pf-normalized mean over SD 1 to 10). Retuned SNR is at least the untuned SNR at every SD
      above 0 (ratio 1.05 to 3.00). The retuned maximum over noisy cells is biased upward (B10).
    response: >-
      No change; the analysis follows the paper's notebook, which takes the same maximum.
  - claim: noise-effects-on-mu-and-kappa
    agrees: true
    outcome: partially_reproduced
    reason: >-
      (1) holds (|z| at most 0.82, variance grows) and (3) holds (ratios 0.500 and 0.501). (2)
      fails in all four conditions, the mean end amplitude being 0.83, 0.65, 0.82 and 0.42
      against about 1.00 without noise. SI section 5 derives the noise's direct effect on the
      first Fourier mode and leaves the remaining dynamics unchanged, while the criterion compares
      the full network, where noise raises the rectified global inhibition; the failure of (2)
      may come from how the criterion turns the claim into a test, and the notebook does not
      separate the two effects (B1). It asked for the zero mode and global inhibition over time,
      or a run with the inhibition held at its noise-free level.
    response: >-
      Added both. The global inhibition rises from 0.5 to 0.57 to 0.76 at 1 s and the zero mode
      stays near 0. With the inhibition held at its noise-free level the mean amplitude rises to
      1.01 to 1.33, within 1.5 SE of the mean SI Eq. S124 implies. Outcome kept, as the criterion
      tests the full network; the question whether it should is added to questions/000289.yaml.
      The finding on the released code now names the cause.
  - claim: fig4b-connectome-motifs
    agrees: false
    outcome: partially_reproduced
    reason: >-
      Under reading (a) the offsets have opposite signs (left +0.56, right -0.48 on the same side)
      and all 42 Delta7 reach more than 8 EPG glomeruli for input and output at 1 synapse or more.
      Reading (b), which the criterion requires, cannot be formed because no instance name holds
      an EB or gall position. The Delta7 breadth depends on the synapse threshold (output in 42,
      7 and 0 of 42 at 1, 3 and 5 synapses); the connectome is v1.2, not v1.2.1 (B4).
    response: >-
      Outcome changed from reproduced to partially_reproduced: the criterion requires both sorts
      and only one can be formed. The conclusion now gives the threshold dependence of the
      output side in the text. Assumption and the v1.2 deviation kept.
  - claim: fig4gh-drosophila-network-matches
    agrees: true
    outcome: partially_reproduced
    reason: >-
      The largest difference is 0.019; reading (b) (0.02) holds and reading (a) (0.01) fails at
      0.1, 0.2 and 0.3/s, and the criterion needs both. The bounds are close to the run-to-run
      variability of the paper's outputs, the same attractor giving 0.2159 at 0.1/s in
      figure2i.npz and 0.1943 in figure4g.npz; the notebook gives no Monte Carlo SE, so the
      outcome rests on the claims file's bounds, not on a detectable effect (B2).
    response: >-
      Added the Monte Carlo SE. The three differences above 0.01 are 1.95, 1.51 and 1.16 times
      the SE of a difference of two independent scans (smaller in fact, as the networks share
      their runs); the figure2i and figure4g attractors differ by 2.2 such units at 0.1/s.
      Outcome kept, as the criterion fixes the bounds.
  - claim: figs2-performance-independent-of-n
    agrees: false
    outcome: not_reproduced
    reason: >-
      N 16 at 0.1/s deviates by 0.041, so both readings (N of 8 and more, N of 16 and more,
      within 0.02) fail; it is the only value above 0.02, and N 3 and 4 stay within 0.0186. The
      bound is close to the run-to-run variability and the notebook gives no Monte Carlo SE (B2).
      One NaN value for N 128 is skipped by nanmax and its rate is not printed (B8).
    response: >-
      Outcome changed from partially_reproduced to not_reproduced: both readings fail and the
      criterion requires both. The added Monte Carlo SE shows the deviation is not sampling
      error (4.3 SE of a difference, no other value beyond 3). The NaN cell is now printed (N 128
      at 100/s).
  - claim: prediction-bump-amplitude-cue-reliability
    agrees: true
    outcome: blocked
    reason: >-
      Three combinations show higher amplitude with the high-contrast cue (dF/F with (a), 10 of
      15 flies; raw with (a), 12 of 15; raw with (b), p 0.021); dF/F with (b) does not (p 0.138).
      The criterion blocks the claim when the readings differ; recomputing both p-values from the
      printed table gave the same results. The raw-signal details are the author's choices and
      only one variant is run (B5). bra.fourier returns phase -theta for a bump at theta and fixes
      k 2 across 37 to 47 ROIs (B6). Cell 0 says no claim is blocked (B9).
    response: >-
      Added 18 raw-signal variants (smoothing 0, 2, 4 pixels; baseline percentile 5, 10, 20; F -
      F0 or divided by F0): p is below 0.05 in all nine F - F0 variants and in none divided by F0.
      The bra.fourier docstring and the data check now state the phase sign (a convention, the
      amplitude does not depend on it) and print the ROI counts. Cell 0 now says the claim is
      tested, then blocked. Outcome kept.
E
python tools/entry.py check entries/000289-kutschireiter-2023 2>&1 | tail -5; date -u
```

```
0 error(s)
Fri Oct 30 01:00:05 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/000289-kutschireiter-2023 2>&1 | tail -3; date -u
```

```
Installed kernelspec registry-000289-kutschireiter-2023 in executed/000289-kutschireiter-2023/.venv/share/jupyter/kernels/registry-000289-kutschireiter-2023
0 error(s)
pass  reproduce_kutschireiter_2023.ipynb  (375 s)
Fri Oct 30 01:06:32 UTC 2026
```

**Agent**

Confirm the numbers are deterministic across the two runs (noise diagnostics, SE, raw variants):

**Agent calls Bash**

```bash
python3 - <<'E'
import json
nb=json.load(open('executed/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
def out(i):
    return ''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
o=out(37); print(o[o.find('global inhibition'):])
for i in (28,43,46): print(out(i)[-700:])
o=out(50); print(o[o.find('variants with'):])
E
git status --short
```

```
global inhibition and zero mode in the full network, and the end amplitude with the inhibition held:
  N  sigma  inh_noise_free  inh_t01  inh_t1  inh_t5  zero_mode_t5  amp_end_full  amp_end_inh_fixed  se_inh_fixed  amp_end_SI_rice
 64    1.0             0.5   0.5196  0.5695  0.5281        0.0007        0.8249             1.0756        0.0085           1.0824
 64    2.0             0.5   0.5863  0.7580  0.7253       -0.0144        0.6333             1.3328        0.0144           1.3522
256    1.0             0.5   0.5208  0.5653  0.5225        0.0007        0.8128             1.0134        0.0044           1.0197
256    2.0             0.5   0.5855  0.7591  0.7083       -0.0011        0.4242             1.0702        0.0084           1.0824

.9934  0.9942  0.988  0.9893  0.9725  0.9525  0.9322
best_kstar      0.3000  0.5000  0.7000  0.8000  0.8000  0.9000  1.1000  1.1000  1.100  1.0000  1.2000  1.6000  1.5000
conditions: {1: np.True_, 2: True, 3: np.True_, 4: False, 5: True}
steps of the maximum for beta above the best: [-0.0031 -0.0013 -0.0021 -0.0013  0.0008 -0.0062  0.0014 -0.0168 -0.02   -0.0203] ; rises: 2 of 10
variant, not judged: Spearman rho of beta and the maximum, beta >= best: -0.982 (p = 8.4e-08); drop from beta 0.3 to 8: 0.0689
SE of one cell's normalized performance 0.0018 (distribution-free bound 0.0032); SE of a difference of two cells 0.0026
rises of the maximum over kappa*, in SEs of a difference: [0.32 0.52]

       4.0690      4.3704
  9.00      0.8750 0.8767    0.0018           4.3071      4.6225
 10.00      0.8827 0.8845    0.0018           4.5206      4.8494
 30.00      0.9317 0.9337    0.0020           7.6173      8.0913
100.00      0.9617 0.9632    0.0015          13.8363     14.4548
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/runtime_minutes: 8/runtime_minutes: 7/' entries/000289-kutschireiter-2023/entry.yaml && python tools/entry.py check entries/000289-kutschireiter-2023 2>&1 | tail -1; grep -n "—\|rather" attempts/000289-kutschireiter-2023-01.yaml questions/000289.yaml entries/000289-kutschireiter-2023/README.md entries/000289-kutschireiter-2023/bra.py | head; grep -c "—\| rather" entries/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb
```

```
0 error(s)
0
```

**Agent**

I worked through every point in the round-1 report, re-ran the entry with `python tools/entry.py all`, and checks report 0 errors. The notebook runs in about 6.3 minutes and gave the same numbers on two runs. Nothing is committed.

**Outcomes changed (both now match the verifier's):**
- **fig4b-connectome-motifs**: reproduced → partially_reproduced. The criterion needs both sorts, and reading (b) can't be built because the hemibrain neuron names give only the protocerebral bridge glomerulus. It stays marked as resting on an assumption.
- **figs2-performance-independent-of-n**: partially_reproduced → not_reproduced. Both readings fail and the criterion needs both. The new Monte Carlo error estimate shows the one failing value (N = 16 at 0.1/s, 0.041 below the reference) is real. It is 4.3 standard errors of a difference, and no other value is beyond 3.

The other 11 outcomes are unchanged, and the verifier agreed with all of them.

**Added or corrected:**
- **Released code:** a data-check cell prints the lines of the paper's code that define what the verifier could not check:
  - `kappa_z = 15` is commented "called gamma_z in manuscript".
  - The columns of the `*_stats` arrays.
  - The axes of the Figure 3 grids.
  - The number of runs per scan (10,000).
- **Monte Carlo error:** each simulated accuracy averages 10,000 runs, and from that I estimated its standard error.
  - fig3d: the two rises that break condition 4 are 0.32 and 0.52 standard errors, so they are within sampling error. The outcome stays partial because the criterion gives no tolerance.
  - fig4gh: the differences above 0.01 are 1.16 to 1.95 standard errors, close to the sampling error. The outcome stays partial for the same reason.
- **Noise claim:** in the full network the noise raises the global inhibition (from 0.5 to between 0.57 and 0.76 at 1 s), which shrinks the bump. With the inhibition held at its noise-free level, the bump amplitude rises to 1.01–1.33. That is within 1.5 standard errors of what the paper's SI Eq. S124 predicts.
  - The outcome stays partially_reproduced, because the criterion tests the full network.
  - I added a question to `questions/000289.yaml` asking a reader whether it should test only the noise's direct effect, as the SI derivation does.
  - The finding about the released code now names this cause.
- **Prediction claim:** I ran 18 variants of the raw-fluorescence signal (smoothing, baseline percentile, with and without dividing by the baseline). The test passes (p < 0.05) in all 9 variants that don't divide by the baseline and in none of the 9 that do. So the split between readings comes from that division, and the claim stays blocked.
- **Smaller fixes:**
  - The header no longer says "No claim is blocked".
  - The missing value in the Fig. S2 data (N = 128 at 100/s) is now printed.
  - The fig1 notes say that comparison (a) is a weak test.
  - The bump decoder's reversed phase sign is documented as a convention; amplitude, the only thing the prediction uses, doesn't depend on it.
  - README, summary and `runtime_minutes` are updated.
- **Attempt record:** the `verifications` round is recorded, with the verifier's reasons and my response for each claim.

**Not done:** I did not re-run the paper's large simulation scans, which are beyond the time limit; the error estimates come from the stored results instead. The hemibrain v1.2.1 release (the version the paper cites) still needs a personal token, so the connectome remains the public v1.2 export.

## End of run

53 turns, 21 minutes, result: success.
