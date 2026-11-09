# 000289 · author-revise-2 · run 40985418805

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000289/verifier-2-report.md; ls entries/000289-kutschireiter-2023;
```

```
Fri Oct 30 01:25:17 UTC 2026
# Round 2 verification: Kutschireiter et al. 2023 with DANDI:000289

I agree with all 13 outcomes. The notebook's printed outputs support every number in the conclusions, the summary, the README and the record's notes, except four sentences: one swapped pair of ratios, one value that is never printed, one unproven independence claim, and one wrong description of the noise diagnostic. The record states my round-1 reasons faithfully. One new point bears on the noise claim's explanation, but not on its outcome.

## 1. Outcomes and assumptions

The claims file and the attempt record each have 13 claims and 13 outcomes, with matching ids. Notebook cell numbers have shifted by about one since round 1.

| Claim | Record | Agree? |
|---|---|---|
| fig1-conflict-decreases-certainty | reproduced | Yes (cell 13: 6 of 6 under (a) and (b)) |
| fig2h-bump-tracks-circkf | reproduced | Yes (cell 16) |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced | Yes (cell 19) |
| fig3b-bayesian-beats-conventional | reproduced | Yes (cell 22) |
| fig3c-update-weights | reproduced | Yes (cell 25) |
| fig3d-best-network-slow-decay | partially_reproduced | Yes. Condition 4 fails as written (cell 28). |
| fig3f-noise-drop-below-70 | reproduced | Yes (cell 31) |
| fig3f-retuning-reduces-drop | reproduced, measured 34.64 | Yes. 3 of 6 readings fall in 31.5 to 38.5%, and the SNR ratio is 1.05 to 3.00 (cell 34). |
| noise-effects-on-mu-and-kappa | partially_reproduced | Yes, as the criterion is written. Condition (2) fails in all 4 settings (cell 37). |
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls records/ 2>/dev/null | head; ls; cat questions/000289.yaml 2>/dev/null | head -50
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
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 409,500p docs/protocol.md; sed -n 592,640p docs/protocol.md; ls attempts | grep 289
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
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; wc -c *; python -c "
import json;nb=json.load(open('reproduce_kutschireiter_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source']); print('=====',i,c['cell_type'],len(s)); print(s[:300])
"
```

```
2977 README.md
16552 bra.py
  933 entry.yaml
70498 reproduce_kutschireiter_2023.ipynb
   52 requirements.in
 1163 requirements.lock.txt
92175 total
===== 0 markdown 3279
# Testing Kutschireiter et al. (2023) with dandiset 000289

Paper. Kutschireiter A, Basnak MA, Wilson RI, Drugowitsch J (2023). Bayesian inference in ring
attractor networks. *PNAS* 120, e2210622120.
[doi:10.1073/pnas.2210622120](https://doi.org/10.1073/pnas.2210622120). The claims file was written

===== 1 code 687
import time
import numpy as np
import pandas as pd
from scipy import stats
from concurrent.futures import ThreadPoolExecutor
[... 332 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('reproduce_kutschireiter_2023.ipynb'))
for i in [11,28,29,36,37,38,49,50,51,52]:
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source']))
    if c['cell_type']=='code':
        for o in c.get('outputs',[]): print('--OUT--'); print(''.join(o.get('text','')) or o.get('data',{}).get('text/plain',''))
"
```

```
===== 11
The bump phase locks to the cue position at high contrast (median coherence 0.79) and barely in
darkness (0.13), and in every fly the coupling peaks at lag 0 or 5 frames (0 to 0.55 s), the
lags closest to 0 that were tested, so the dF/F and the cue position share a clock. Frames the trials table labels high contrast show stronger coupling than the same frames
with the labels shifted by one block, (median 0.79 against 0.39, 12 of 15 flies), which is consistent with the trials table being on
the same clock. This is consistent with the data, not a proof.
===== 28
m3d = code.npz("figure3d.npz")["MSE_array"] / ref_pf
i, j = np.unravel_index(np.nanargmax(m3d), m3d.shape)
kb, bb = bra.KSTAR_3D[i], bra.BETA_GRID[j]
bay = m3d[list(bra.KSTAR_3D).index(1.0), list(bra.BETA_GRID).index(0.5)]
print("normalized performance range %.4f to %.4f, NaN cells %d" % (np.nanmin(m3d), np.nanmax(m3d), np.isnan(m3d).sum()))
print("best network: kappa* = %g, beta = %g, performance %.4f; Bayesian (1, 0.5): %.4f, %.2f%% below the best"
      % (kb, bb, m3d[i, j], bay, 100 * (m3d[i, j] - bay) / m3d[i, j]))
above = bra.BETA_GRID > bb
best_per_beta = np.nanmax(m3d, 0)
kstar_per_beta = bra.KSTAR_3D[np.nanargmax(m3d, 0)]
print(pd.DataFrame(dict(beta=bra.BETA_GRID, max_over_kstar=best_per_beta, best_kstar=kstar_per_beta)).round(4).T.to_string())
steps = np.diff(best_per_beta[j:])
c = {1: bb <= 1, 2: (kb, bb) != (1.0, 0.5), 3: (m3d[i, j] - bay) / m3d[i, j] <= 0.10,
[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "def \|inh\|5 to 9\|mask" bra.py | head -80
```

```
69:def _get(url, md5):
82:    def __init__(self):
88:    def read(self, name):
91:    def npz(self, name):
94:    def source_lines(self, name, pattern):
102:    def notebook_cells(self, name):
106:    def _module(self):
121:def objective(values, mu=0.5, sigma=1.0, rates=RATES):
129:def resultant_se(R, n=10000):
146:def objective_se(se_per_rate, rates=RATES, mu=0.5, sigma=1.0):
159:def run_figure2h(code, rate=15):
175:def circ_diff(a, b):
181:def rnn_batch(rng, runs, T, N, sigma_N, w_even, w_quad, tau=1.0, kappa_0=1.0, phi_0=0.0, dt=0.01,
182:              noise=None, inh_fixed=None, traces=None):
185:    Same update, term by term: decay, even recurrence (2/N w_even cos), quadratic inhibition
189:    Diagnostics for the noise claim (not in RNN_filter_Run): `inh_fixed`, if given, replaces the
190:    global inhibition w_quad pi/N sum max(r, 0) by that constant, so that the noise acts only
193:    run-mean global inhibition and zero mode (population mean rate) at every step."""
202:    def decode(r):
208:        traces["inh"], traces["zero_mode"] = np.zeros(steps), np.zeros(steps)
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 175,225p bra.py; sed -n 312,335p bra.py
```

```
def circ_diff(a, b):
    return np.angle(np.exp(1j * (np.asarray(a) - np.asarray(b))))


# ---------------------------------------------------------------------------------------------
# Neural noise: a batched copy of RNN_filter_Run, checked against it in the notebook
def rnn_batch(rng, runs, T, N, sigma_N, w_even, w_quad, tau=1.0, kappa_0=1.0, phi_0=0.0, dt=0.01,
              noise=None, inh_fixed=None, traces=None):
    """RNN_filter_Run (circularFiltering.py) for `runs` independent runs at once, with no angular
    velocity input (w_odd = 0, dy = 0), no HD input (I_ext = 0) and stoch_corr = 0 (claims file).
    Same update, term by term: decay, even recurrence (2/N w_even cos), quadratic inhibition
    (pi/N sum of rectified rates), additive noise sigma_N sqrt(dt) N(0,1). `noise` may pass the
    standard normal draws (steps x runs x N) to reproduce a given run.

    Diagnostics for the noise claim (not in RNN_filter_Run): `inh_fixed`, if given, replaces the
    global inhibition w_quad pi/N sum max(r, 0) by that constant, so that the noise acts only
    through the linear terms, as in the SI derivation (section 5, Eqs. S107 to S109, where the
    noise is one more input and the other dynamics are unchanged). `traces`, a dict, receives the
    run-mean global inhibition and zero mode (population mean rate) at every step."""
    steps = int(T / dt)
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,120p bra.py; ls ~/.cache 2>/dev/null; grep -rn "cache\|CACHE" bra.py | head
```

```
KSTAR_3F = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6,
                     1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.2, 3.4,
                     3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0])
SIGMAS_3F = np.array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 15, 20])
N_3F = 64
REF_PF_3F = 0.6912447327304075  # Figure3f_FigureS4.ipynb, "performance of particle filter as reference"
N_S2 = np.array([3, 4, 8, 16, 32, 64, 128])  # FigureS2.ipynb, N_array


def _get(url, md5):
    data = requests.get(url, timeout=600).content
    got = hashlib.md5(data).hexdigest()
    if got != md5:
        raise ValueError(f"{url}: md5 {got}, expected {md5}")
    return data


# ---------------------------------------------------------------------------------------------
# The paper's code and processed outputs
class Code:
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import sys; sys.path.insert(0,'entries/000289-kutschireiter-2023')
import bra; c=bra.Code()
print([n for n in c.names if 'scan' in n.lower() or '3d' in n.lower()])
print(c.read('performance_scan_figure3d.py').decode() if 'performance_scan_figure3d.py' in c.names else '')
" 2>&1 | head -150
```

```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    import bra; c=bra.Code()
    ^^^^^^^^^^
  File "entries/000289-kutschireiter-2023/bra.py", line 28, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls executed/ 2>/dev/null; ls -a executed/000289-kutschireiter-2023 2>/dev/null; grep -n "venv\|python" tools/entry.py | head -20
```

```
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
335:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
345:    venv = (output_dir / ".venv").resolve()
346:    python = venv / "bin" / "python"
348:    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
350:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
351:                ["uv", "pip", "install", "--quiet", "--python", str(python),
353:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
363:            [str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
367:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
380:        {"entry": entry["name"], "python": PYTHON_VERSION, "results": results}, indent=1) + "\n")
```

**Agent**

No executed copy exists yet, so I'll build a dev venv in $TMPDIR to explore.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.12 dev && uv pip install -q --python dev/bin/python -r entries/000289-kutschireiter-2023/requirements.lock.txt 2>&1 | tail -3; ls dev/bin | head
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
deactivate.bat
f2py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import sys; sys.path.insert(0,'entries/000289-kutschireiter-2023')
import bra; c=bra.Code()
print([n for n in c.names if 'scan' in n.lower()])
print(c.read('performance_scan_figure3d.py').decode())
" 2>&1 | head -150
```

```
['performance_scan_figure2i.py', 'performance_scan_figure3d.py', 'performance_scan_figure3f.py', 'performance_scan_figure4g.py', 'performance_scan_figureS2.py']
import sys
import numpy as np
import circularFiltering as flt
from time import time

kappa_z_array = np.array([0.01,0.03,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,30,100])
len_kz = len(kappa_z_array)

# translate input varibles
kappa_star = float(sys.argv[1])
beta = float(sys.argv[2])

# number of iterations to average
nIter = 10000

# model parameters
T = 20 # simulation time
dt = 0.01 # step size
t = np.arange(0,T,dt)
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023; python -c "
import json;nb=json.load(open('reproduce_kutschireiter_2023.ipynb'))
for i in [8,9,10,46,47]:
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source']))
    if c['cell_type']=='code':
        for o in c.get('outputs',[]): print('--OUT--'); print(''.join(o.get('text','')) or o.get('data',{}).get('text/plain',''))
"; cat README.md
```

```
===== 8
# --- dandiset 000289: every asset, and the cue-contrast sessions
assets = bra.assets()
print("dandiset", bra.DANDISET, "version", bra.VERSION, ": assets", len(assets),
      "; total size %.0f GB" % (sum(a["size"] for a in assets) / 1e9))
subj = lambda a: int(a["path"].split("/")[0][4:])
contrast_assets = sorted([a for a in assets if subj(a) <= 15], key=subj)

def load(a):
    f = bra.open_nwb(a)
    s = bra.read_session(f)
    s["path"] = a["path"]
    return s

with ThreadPoolExecutor(8) as ex:
    sessions = list(ex.map(load, contrast_assets))
print("loaded %d sessions in %.0f s" % (len(sessions), time.time() - started))
rows = []
for s in sessions:
    tr = s["trials"]
[... 150 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000289-kutschireiter-2023/bra.py",
 "old_string": "              noise=None, inh_fixed=None, traces=None):",
 "new_string": "              noise=None, inh_fixed=None, inh_per_amp=None, traces=None):"
}
```

```
The file entries/000289-kutschireiter-2023/bra.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000289-kutschireiter-2023/bra.py",
 "old_string": "    global inhibition w_quad pi/N sum max(r, 0) by that constant, so that the noise acts only\n    through the linear terms, as in the SI derivation (section 5, Eqs. S107 to S109, where the\n    noise is one more input and the other dynamics are unchanged). `traces`, a dict, receives the\n    run-mean global inhibition and zero mode (population mean rate) at every step.\"\"\"",
 "new_string": "    global inhibition w_quad pi/N sum max(r, 0) by that constant. This removes two things at once:\n    the noise's effect on the inhibition, and the inhibition's dependence on the amplitude, which is\n    the restoring force toward kappa* (the first mode becomes neutral). `inh_per_amp`, if given,\n    replaces the inhibition by `inh_per_amp` times the decoded amplitude of each run, the value a\n    noise-free cosine bump of that amplitude would give: the restoring force is kept and only the\n    noise's own contribution to the rectified sum is removed. `traces`, a dict, receives the\n    run-mean global inhibition and zero mode (population mean rate) at every step.\"\"\""
}
```

```
The file entries/000289-kutschireiter-2023/bra.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000289-kutschireiter-2023/bra.py",
 "old_string": "            inh = inh_fixed\n        dW",
 "new_string": "            inh = inh_fixed\n        if inh_per_amp is not None:\n            inh = inh_per_amp * kappa[i - 1][:, None]\n        dW"
}
```

```
The file entries/000289-kutschireiter-2023/bra.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd $TMPDIR && time dev/bin/python -c "
import sys; sys.path.insert(0,'entries/000289-kutschireiter-2023')
import bra, numpy as np
rng=np.random.default_rng(1)
for N in (64,256):
    tr0={}; _,k0=bra.rnn_batch(rng,1,5,N,0.0,1.5,0.5,traces=tr0); inh0=tr0['inh'][-1]; print(N,'inh0',inh0,k0[-1])
    for sig in (1.,2.):
        tr={}
        _,k=bra.rnn_batch(rng,2000,5,N,sig,1.5,0.5,inh_per_amp=inh0/k0[-1,0],traces=tr)
        print(sig, [k[int(t/0.01)-1].mean().round(3) for t in (0.1,0.5,1,2,5)], k[-1].std(ddof=1)/np.sqrt(2000), tr['inh'][-1])
"
```

```
64 inh0 0.49996704679822984 [1.00073801]
1.0 [np.float64(1.001), np.float64(1.003), np.float64(1.002), np.float64(1.008), np.float64(1.003)] 0.004024287644944897 0.5948383183530845
2.0 [np.float64(1.0), np.float64(1.013), np.float64(1.024), np.float64(1.031), np.float64(1.049)] 0.007098937585232291 0.8729859346538634
256 inh0 0.4999979421660304 [1.00004609]
1.0 [np.float64(1.001), np.float64(1.002), np.float64(1.002), np.float64(1.004), np.float64(1.002)] 0.0019500685002274065 0.59419988794426
2.0 [np.float64(1.001), np.float64(1.0), np.float64(1.007), np.float64(1.011), np.float64(1.006)] 0.003985931441418191 0.8583024201939277

real	0m17.963s
user	1m9.244s
sys	0m0.422s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import numpy as np
rng=np.random.default_rng(0)
for N,sig in [(64,1),(64,2),(256,1),(256,2)]:
    s=np.sqrt(2*sig**2/N); x=np.zeros((20000,2)); x[:,0]=1; dt=0.01
    for i in range(500):
        k=np.hypot(*x.T)[:,None]; x=x+0.5*(1-k)*x*dt+s*np.sqrt(dt)*rng.standard_normal(x.shape)
    print(N,sig,np.hypot(*x.T).mean())
"
```

```
64 1 1.0037299887649003
64 2 1.0367452275292885
256 1 1.001763160756653
256 2 1.004684679214398
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023 && sed -n 265,290p bra.py
```

```
import remfile
    url = f"{DANDI_API}/assets/{asset['asset_id']}/download/"
    return h5py.File(remfile.File(url), "r")


def read_session(f):
    """dF/F per PB midline ROI, the cue position, the trials table, and metadata."""
    rrs = f["processing/ophys/Fluorescence/RoiResponseSeries"]
    pos = f["processing/behavior/Position/SpatialSeries"]
    out = {
        "description": f["session_description"][()].decode(),
        "subject": f["general/subject/subject_id"][()].decode(),
        "rate_meta": float(f["general/optophysiology/imaging_plane/imaging_rate"][()]),
        "dff": rrs["data"][:],
        "t": rrs["timestamps"][:],
        "cue": pos["data"][:],
        "t_cue": pos["timestamps"][:],
        "cue_unit": pos["data"].attrs.get("unit"),
        "tps_shape": f["acquisition/TwoPhotonSeries/data"].shape,
        "t_tps": f["acquisition/TwoPhotonSeries/timestamps"][:],
[... 6 more lines not kept]
```

**Agent**

Now the notebook edits.

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023 && cat > $TMPDIR/edit.py <<'EOF'
import json
p = "reproduce_kutschireiter_2023.ipynb"
nb = json.load(open(p))
C = nb["cells"]
def src(i): return "".join(C[i]["source"])
def setsrc(i, s): C[i]["source"] = s.splitlines(keepends=True)
def rep(i, old, new):
    s = src(i); assert s.count(old) == 1, (i, old); setsrc(i, s.replace(old, new))

# cell 8: mask sizes
rep(8, 'print("identical dF/F pairs', '''npix = [int((m > 0).sum()) for s in sessions for m in s["masks"]]
print("ROI mask sizes, pixels with nonzero weight per ROI: min %d, median %g, max %d over %d ROIs; mask array shape of sub-1:"
      % (min(npix), np.median(npix), max(npix), len(npix)), sessions[0]["masks"].shape)
print("identical dF/F pairs''')
# cell 11: lag in seconds
rep(11, "lag 0 or 5 frames (0 to 0.55 s)", "lag 0 or 5 frames (5 frames is 0.54 s at 9.18 Hz and 0.64 s at 7.87 Hz)")
# cell 28: independence of grid cells
rep(28, '''# Monte Carlo error of one grid cell: each cell is its own scan of 10,000 runs per rate
# (performance_scan_figure3d.py), and the objective is linear in the per-rate accuracies.''',
'''# Monte Carlo error of one grid cell: each cell is its own scan of 10,000 runs per rate, a separate
# process of performance_scan_figure3d.py started with (kappa*, beta) as arguments. The script sets
# no seed, so numpy's global generator is seeded from the operating system in each process and the
# cells' trajectories are independent. The objective is linear in the per-rate accuracies.
print("performance_scan_figure3d.py, lines that set the grid cell or a seed:",
      code.source_lines("performance_scan_figure3d.py", r"sys\\.argv|seed|nIter ="))''')
# cell 29
rep(29, "between two grid cells (0.0026), so",
    "between two grid cells (0.0026; the scan script sets no seed and runs each cell as its own\nprocess, so the cells' trajectories are independent), so")
# cell 37: amplitude-matched control
rep(37, '''# otherwise unchanged dynamics, as in SI section 5 (Eqs. S107 to S109). There the first Fourier
# mode is neutral (w_even - 1/tau - inhibition = 0 at kappa = 1), and SI Eq. S124 gives each
# coordinate of (x1, x2) the variance 2 sigma^2 / N per unit time, so the amplitude after T is
# Rice distributed: its mean is the SI prediction, above the starting 1.''',
'''# a constant. This changes two things at once: it removes the noise's effect on the inhibition, and
# the inhibition's dependence on the amplitude, the restoring force toward kappa* = 1, so the first
# mode is neutral (w_even - 1/tau - inhibition = 0). SI Eq. S124 gives each coordinate of (x1, x2)
# the variance 2 sigma^2 / N per unit time, so the amplitude after T is Rice distributed.
# (iii) The verifier's cleaner control: the inhibition set to the value a noise-free cosine bump of
# the run's decoded amplitude gives (inh_per_amp times kappa), so the restoring force is kept and only
# the noise's own contribution to the rectified sum is removed. Its reference is the reduced
# two-dimensional SDE of the first mode, dx = (w_even - 1/tau - w_quad kappa) x dt + noise of
# variance 2 sigma^2 / N per coordinate and unit time, which has the SI's Ito drift sigma^2/(kappa N).''')
rep(37, '''        _, kf = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5, inh_fixed=inh0)
        s_T = np.sqrt(2 * sig ** 2 / N * 5)''',
'''        _, kf = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5, inh_fixed=inh0)
        _, ka = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5, inh_per_amp=inh0 / k_nf)
        s_T = np.sqrt(2 * sig ** 2 / N * 5)
        x = np.tile([1.0, 0.0], (20000, 1))
        for _ in range(499):
            kx = np.hypot(x[:, 0], x[:, 1])[:, None]
            x = x + (0.5 - 0.5 * kx) * x * 0.01 + np.sqrt(2 * sig ** 2 / N * 0.01) * rng.standard_normal(x.shape)''')
rep(37, '''    inh0 = tr0["inh"][-1]''', '''    inh0, k_nf = tr0["inh"][-1], _k0[-1, 0]''')
rep(37, '''    bra.rnn_batch(rng, 1, 5, N, 0.0, 1.5, 0.5, traces=tr0)''', '''    _, _k0 = bra.rnn_batch(rng, 1, 5, N, 0.0, 1.5, 0.5, traces=tr0)''')
rep(37, '''                         amp_end_SI_rice=stats.rice(b=1 / s_T, scale=s_T).mean()))''',
'''                         amp_end_SI_rice=stats.rice(b=1 / s_T, scale=s_T).mean(),
                         amp_noise_free=k_nf, amp_end_inh_of_amp=ka[-1].mean(),
                         se_inh_of_amp=ka[-1].std(ddof=1) / np.sqrt(len(ka[-1])),
                         amp_end_2d_sde=np.hypot(x[:, 0], x[:, 1]).mean()))''')
rep(37, '''print("\\nglobal inhibition and zero mode in the full network, and the end amplitude with the inhibition held:")
print(pd.DataFrame(rows).round(4).to_string(index=False))''',
'''dg = pd.DataFrame(rows)
print("\\nglobal inhibition and zero mode in the full network, and the end amplitude with the inhibition held:")
print(dg.iloc[:, :11].round(4).to_string(index=False))
print("\\nend amplitude with the inhibition set by the decoded amplitude (iii), against the noise-free run and the 2-D SDE:")
dg["z_vs_noise_free"] = (dg.amp_end_inh_of_amp - dg.amp_noise_free) / dg.se_inh_of_amp
dg["z_vs_2d_sde"] = (dg.amp_end_inh_of_amp - dg.amp_end_2d_sde) / dg.se_inh_of_amp
print(dg[["N", "sigma", "amp_noise_free", "amp_end_inh_of_amp", "se_inh_of_amp", "amp_end_2d_sde",
          "z_vs_noise_free", "z_vs_2d_sde", "amp_end_full"]].round(4).to_string(index=False))''')
# cell 51: swapped ratios
rep(51, "(median high/low ratio 1.12 and\n1.11)", "(median high/low ratio 1.11 and\n1.12)")
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
EOF
python $TMPDIR/edit.py && git diff --stat
```

```
Exit code 2
/bin/bash: line 1: cd: entries/000289-kutschireiter-2023: No such file or directory
python: can't open file '/tmp/claude-1001/edit.py': [Errno 2] No such file or directory
```

**Agent calls Bash**

```bash
pwd; head -c 300 reproduce_kutschireiter_2023.ipynb | head -5; tail -c 200 reproduce_kutschireiter_2023.ipynb | od -c | tail -3
```

```
entries/000289-kutschireiter-2023
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d212c268",
0000260  \n       "   n   b   f   o   r   m   a   t   _   m   i   n   o
0000300   r   "   :       5  \n   }  \n
0000310
```

**Agent**

I'll rerun the same script from the entry directory (the heredoc was skipped because `cd` failed).

**Agent calls Bash**

```bash
cat > $TMPDIR/edit.py <<'EOF'
import json
p = "reproduce_kutschireiter_2023.ipynb"
nb = json.load(open(p))
C = nb["cells"]
def src(i): return "".join(C[i]["source"])
def setsrc(i, s): C[i]["source"] = s.splitlines(keepends=True)
def rep(i, old, new):
    s = src(i); assert s.count(old) == 1, (i, old); setsrc(i, s.replace(old, new))

rep(8, 'print("identical dF/F pairs', '''npix = [int((m > 0).sum()) for s in sessions for m in s["masks"]]
print("ROI mask sizes, pixels with nonzero weight per ROI: min %d, median %g, max %d over %d ROIs; mask array shape of sub-1:"
      % (min(npix), np.median(npix), max(npix), len(npix)), sessions[0]["masks"].shape)
print("identical dF/F pairs''')
rep(11, "lag 0 or 5 frames (0 to 0.55 s)", "lag 0 or 5 frames (5 frames is 0.54 s at 9.18 Hz and 0.64 s at 7.87 Hz)")
rep(28, '''# Monte Carlo error of one grid cell: each cell is its own scan of 10,000 runs per rate
# (performance_scan_figure3d.py), and the objective is linear in the per-rate accuracies.''',
'''# Monte Carlo error of one grid cell: each cell is its own scan of 10,000 runs per rate, a separate
# process of performance_scan_figure3d.py started with (kappa*, beta) as arguments. The script sets
# no seed, so numpy's global generator is seeded from the operating system in each process and the
# cells' trajectories are independent. The objective is linear in the per-rate accuracies.
print("performance_scan_figure3d.py, lines that set the grid cell or a seed:",
      code.source_lines("performance_scan_figure3d.py", r"sys\\.argv|seed|nIter ="))''')
rep(29, "between two grid cells (0.0026), so",
    "between two grid cells (0.0026; the scan script sets no seed and runs each cell as its own\nprocess, so the cells' trajectories are independent), so")
rep(37, '''# otherwise unchanged dynamics, as in SI section 5 (Eqs. S107 to S109). There the first Fourier
# mode is neutral (w_even - 1/tau - inhibition = 0 at kappa = 1), and SI Eq. S124 gives each
# coordinate of (x1, x2) the variance 2 sigma^2 / N per unit time, so the amplitude after T is
# Rice distributed: its mean is the SI prediction, above the starting 1.''',
'''# a constant. This changes two things at once: it removes the noise's effect on the inhibition, and
# the inhibition's dependence on the amplitude, the restoring force toward kappa* = 1, so the first
# mode is neutral (w_even - 1/tau - inhibition = 0). SI Eq. S124 gives each coordinate of (x1, x2)
# the variance 2 sigma^2 / N per unit time, so the amplitude after T is Rice distributed.
# (iii) The verifier's cleaner control: the inhibition set to the value a noise-free cosine bump of
# the run's decoded amplitude gives (inh_per_amp times kappa), so the restoring force is kept and only
# the noise's own contribution to the rectified sum is removed. Its reference is the reduced
# two-dimensional SDE of the first mode, dx = (w_even - 1/tau - w_quad kappa) x dt + noise of
# variance 2 sigma^2 / N per coordinate and unit time, which has the SI's Ito drift sigma^2/(kappa N).''')
rep(37, '''        _, kf = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5, inh_fixed=inh0)
        s_T = np.sqrt(2 * sig ** 2 / N * 5)''',
'''        _, kf = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5, inh_fixed=inh0)
        _, ka = bra.rnn_batch(rng, 2000, 5, N, sig, 1.5, 0.5, inh_per_amp=inh0 / k_nf)
        s_T = np.sqrt(2 * sig ** 2 / N * 5)
        x = np.tile([1.0, 0.0], (20000, 1))
        for _ in range(499):
            kx = np.hypot(x[:, 0], x[:, 1])[:, None]
            x = x + (0.5 - 0.5 * kx) * x * 0.01 + np.sqrt(2 * sig ** 2 / N * 0.01) * rng.standard_normal(x.shape)''')
rep(37, '''    inh0 = tr0["inh"][-1]''', '''    inh0, k_nf = tr0["inh"][-1], _k0[-1, 0]''')
rep(37, '''    bra.rnn_batch(rng, 1, 5, N, 0.0, 1.5, 0.5, traces=tr0)''', '''    _, _k0 = bra.rnn_batch(rng, 1, 5, N, 0.0, 1.5, 0.5, traces=tr0)''')
rep(37, '''                         amp_end_SI_rice=stats.rice(b=1 / s_T, scale=s_T).mean()))''',
'''                         amp_end_SI_rice=stats.rice(b=1 / s_T, scale=s_T).mean(),
                         amp_noise_free=k_nf, amp_end_inh_of_amp=ka[-1].mean(),
                         se_inh_of_amp=ka[-1].std(ddof=1) / np.sqrt(len(ka[-1])),
                         amp_end_2d_sde=np.hypot(x[:, 0], x[:, 1]).mean()))''')
rep(37, '''print("\\nglobal inhibition and zero mode in the full network, and the end amplitude with the inhibition held:")
print(pd.DataFrame(rows).round(4).to_string(index=False))''',
'''dg = pd.DataFrame(rows)
print("\\nglobal inhibition and zero mode in the full network, and the end amplitude with the inhibition held:")
print(dg.iloc[:, :11].round(4).to_string(index=False))
print("\\nend amplitude with the inhibition set by the decoded amplitude (iii), against the noise-free run and the 2-D SDE:")
dg["z_vs_noise_free"] = (dg.amp_end_inh_of_amp - dg.amp_noise_free) / dg.se_inh_of_amp
dg["z_vs_2d_sde"] = (dg.amp_end_inh_of_amp - dg.amp_end_2d_sde) / dg.se_inh_of_amp
print(dg[["N", "sigma", "amp_noise_free", "amp_end_inh_of_amp", "se_inh_of_amp", "amp_end_2d_sde",
          "z_vs_noise_free", "z_vs_2d_sde", "amp_end_full"]].round(4).to_string(index=False))''')
rep(51, "(median high/low ratio 1.12 and\n1.11)", "(median high/low ratio 1.11 and\n1.12)")
s = json.dumps(nb, indent=1, ensure_ascii=False) + "\n"
open(p, "w").write(s)
EOF
python $TMPDIR/edit.py && git diff --stat
```

```
entries/000289-kutschireiter-2023/bra.py           | 13 +++--
 .../reproduce_kutschireiter_2023.ipynb             | 55 ++++++++++++++++------
 2 files changed, 50 insertions(+), 18 deletions(-)
```

**Agent calls Bash**

```bash
cd  && date -u && time python tools/entry.py all entries/000289-kutschireiter-2023 2>&1 | tail -20; date -u
```

```
Fri Oct 30 01:28:02 UTC 2026
print("performance_scan_figure3d.py, lines that set the grid cell or a seed:",
      code.source_lines("performance_scan_figure3d.py", r"sys\.argv|seed|nIter =")) The
# per-rate SE is taken at the Bayesian attractor's accuracies (figure2i.npz), close to the networks'.
se_cell = bra.objective_se(bra.resultant_se(accB)[0]) / ref_pf
print("SE of one cell's normalized performance %.4f (distribution-free bound %.4f); SE of a difference of two cells %.4f"
      % (se_cell, bra.objective_se(bra.resultant_se(accB)[1]) / ref_pf, np.sqrt(2) * se_cell))
print("rises of the maximum over kappa*, in SEs of a difference:", (steps[steps > 0] / (np.sqrt(2) * se_cell)).round(2))

------------------


  [36mCell[39m[36m [39m[32mIn[12][39m[32m, line 25[39m
[31m    [39m[31mcode.source_lines("performance_scan_figure3d.py", r"sys\.argv|seed|nIter =")) The[39m
                                                                                  ^
[31mSyntaxError[39m[31m:[39m invalid syntax



0 error(s)
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023 && python - <<'EOF'
import json
p = "reproduce_kutschireiter_2023.ipynb"
nb = json.load(open(p)); c = nb["cells"][28]
s = "".join(c["source"])
old = '''nIter =")) The
# per-rate SE is taken'''
assert s.count(old) == 1
s = s.replace(old, '''nIter ="))
# The per-rate SE is taken''')
c["source"] = s.splitlines(keepends=True)
open(p, "w").write(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
EOF
cd  && time python tools/entry.py all entries/000289-kutschireiter-2023 2>&1 | tail -20; date -u
```

```
Installed kernelspec registry-000289-kutschireiter-2023 in executed/000289-kutschireiter-2023/.venv/share/jupyter/kernels/registry-000289-kutschireiter-2023
0 error(s)
pass  reproduce_kutschireiter_2023.ipynb  (391 s)

real	6m38.334s
user	11m36.896s
sys	0m23.231s
Fri Oct 30 01:35:29 UTC 2026
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('executed/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
for i in [8,10,28,37,46,50,53]:
    c=nb['cells'][i]
    print('=====',i)
    for o in c.get('outputs',[]): print(''.join(o.get('text','')) or ''.join(o.get('data',{}).get('text/plain','')))
"
```

```
===== 8
dandiset 000289 version 0.240801.1040 : assets 221 ; total size 761 GB

loaded 15 sessions in 26 s
sub                                   description  rois  frames  planes  dur_s  frame_hz  meta_hz  dff_min  dff_max  cue_min  cue_max  same_clock blocks                 block_s
  1 fly presented with visual cues of varying con    37   11020      12 1200.0      9.18     9.18    -0.47     3.90    0.002    6.281        True 213123 195 200 200 200 200 205
  2 fly presented with visual cues of varying con    38   11020      12 1200.0      9.18     9.18    -0.81     4.33    0.000    6.283        True  31212     195 200 200 200 405
  3 fly presented with visual cues of varying con    39   11020      12 1200.0      9.18     9.18    -0.40     4.12    0.000    6.283        True 121323 195 200 200 200 200 205
  4 fly presented with visual cues of varying con    41    9446      14 1200.0      7.87     9.18    -0.37     3.64    0.000    6.283        True 121323 195 200 200 200 200 205
  5 fly presented with visual cues of varying con    42   11020      12 1200.0      9.18     9.18    -0.82     3.72    0.001    6.281        True 312123 195 200 200 200 200 205
  6 fly presented with visual cues of varying con    43   11020      12 1200.0      9.18     9.18    -0.44     4.25    0.000    6.283        True 213123 195 200 200 200 200 205
  7 fly presented with visual cues of varying con    47   11020      12 1200.0      9.18     9.18    -0.84     4.36    0.001    6.282        True 121323 196 200 200 200 200 204
  8 fly presented with visual cues of varying con    41   11020      12 1200.0      9.18     9.18    -0.40     3.30    0.000    6.283        True 312123 196 200 200 200 200 204
  9 fly presented with visual cues of varying con    44   11020      12 1200.0      9.18     9.18    -0.53     5.24    0.001    6.281        True 213123 195 200 200 200 200 205
 10 fly presented with visual cues of varying con    44    9446      14 1200.0      7.87     9.18    -0.59     7.87    0.00
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000289-kutschireiter-2023 && python - <<'EOF'
import json
p = "reproduce_kutschireiter_2023.ipynb"
nb = json.load(open(p)); C = nb["cells"]
def rep(i, old, new):
    s = "".join(C[i]["source"]); assert s.count(old) == 1, (i, old)
    C[i]["source"] = s.replace(old, new).splitlines(keepends=True)
rep(9, "No session duplicates another.\n", "No session duplicates another. The ROI masks are 2D (one plane of 256 x 128 pixels) and\nhave 3 to 11 pixels each (median 7).\n")
s = "".join(C[38]["source"])
i = s.index("The diagnostics show why.")
C[38]["source"] = (s[:i] + """The diagnostics show why. The noise raises the rectified sum that drives the global inhibition,
from 0.5 without noise to 0.52 to 0.59 at 0.1 s and 0.57 to 0.77 at 1 s; the zero mode stays near 0
(at most 0.01 in size). Holding the inhibition at its noise-free constant (ii) makes the mean
amplitude rise to 1.08, 1.38, 1.01 and 1.08 after 5 s, against 1.08, 1.35, 1.02 and 1.08 from the
Rice mean that SI Eq. S124 implies, each within 1.9 standard errors. That shows the SI's noise term
is right, but this control changes two things at once: it removes the noise's effect on the
inhibition and also the restoring force toward kappa* = 1, which leaves a free random walk of the
first mode. The control (iii) removes only the first: the inhibition follows the decoded amplitude
as it would for a noise-free bump. Then the mean amplitude after 5 s is 1.002, 1.045, 1.003 and
1.005, at or above the noise-free 1.000 to 1.001 in all four settings (z = 0.35, 6.2, 1.3 and 1.1)
and within 1.2 standard errors of the reduced two-dimensional SDE of the first mode. So with the
restoring force kept, the noise's direct effect gives a small upward drift, clearly resolved only at
N = 64 and SD 2, and the fall of the amplitude in the released network comes from the noise's own
contribution to the rectified sum that drives the global inhibition. The criterion tests the full
network; whether that is what the paper claims is asked of a reader (questions/000289.yaml).
""").splitlines(keepends=True)
rep(52, "The\nROI masks are 5 to 9 pixels on the PB midline, and the stored", "The\nROI masks are 3 to 11 pixels, and the stored")
open(p, "w").write(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
EOF
sed -i 's/averaged over each ROI'"'"'s 2D mask (5 to 9 pixels on the PB midline)/averaged over each ROI'"'"'s 2D mask (3 to 11 pixels, printed in the data check)/' bra.py
sed -i 's/Not reproduced (one value of 161)/Not reproduced (one value of 160)/' README.md
grep -n "3 to 11\|160" bra.py README.md; python -c "
import json;nb=json.load(open('reproduce_kutschireiter_2023.ipynb'));print(''.join(nb['cells'][52]['source'])[-600:])"
```

```
bra.py:328:    pixels, and averaged over each ROI's 2D mask (3 to 11 pixels, printed in the data check). Neither the
README.md:28:| Accuracy depends little on the number of neurons | Not reproduced (one value of 160) |
set. The dandiset holds no data of this paper, which is a theory
paper; its related resources point to a bioRxiv preprint of this paper (version 4) for a study whose
data it holds (Basnak et al., in preparation). In the cue-contrast experiment, `imaging_rate` says
9.18 Hz for every file, while sub-4 and sub-10 are imaged at 7.87 Hz (0.127 s frames, 14 planes);
sub-2 has one high-contrast block, not two, and a last block of 405 s labelled low contrast. The
ROI masks are 3 to 11 pixels, and the stored dF/F agrees with the raw imaging
only after spatial smoothing, which the files do not describe.
```

**Agent calls Bash**

```bash
sed -n 325,331p bra.py
```

```
def _raw_roi(f, frames, masks, projection, smooths):
    """Raw fluorescence per ROI from the TwoPhotonSeries for the given frame blocks: the volume is
    projected over planes (`projection`), smoothed in the plane with a Gaussian of each SD in `smooths`
    pixels, and averaged over each ROI's 2D mask (3 to 11 pixels, printed in the data check). Neither the
    projection nor the extent of an ROI is stated in the files; the notebook picks them by agreement
    with the stored dF/F, and shows the alternatives."""
    from scipy.ndimage import gaussian_filter
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000289-kutschireiter-2023/bra.py",
 "old_string": "    pixels, and averaged over each ROI's 2D mask (3 to 11 pixels, printed in the data check). Neither the\n    projection nor the extent of an ROI is stated in the files; the notebook picks them by agreement\n    with the stored dF/F, and shows the alternatives.\"\"\"",
 "new_string": "    pixels, and averaged over each ROI's 2D mask (3 to 11 pixels, printed in the data check).\n    Neither the projection nor the extent of an ROI is stated in the files; the notebook picks them\n    by agreement with the stored dF/F, and shows the alternatives.\"\"\""
}
```

```
The file entries/000289-kutschireiter-2023/bra.py has been updated successfully.
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p = "reproduce_kutschireiter_2023.ipynb"
nb = json.load(open(p)); C = nb["cells"]
s = "".join(C[47]["source"]); old = "Sampling alone would put about 1.2 values beyond 0.02 if every network equalled the\nreference"
assert s.count(old) == 1, s
C[47]["source"] = s.replace(old, "Sampling alone would put about 1.2 of the values with N of 8 and more beyond 0.02 if every\nnetwork equalled the reference").splitlines(keepends=True)
open(p, "w").write(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
EOF
grep -n "verifications\|^  - id\|^- id\|round\|proposed" ../../attempts/000289-kutschireiter-2023-01.yaml | head -60; wc -l ../../attempts/000289-kutschireiter-2023-01.yaml
```

```
103:    0.0008 (beta 0.7 to 0.8) and 0.0014 (0.9 to 1). The two rises are smaller than the falls around
175:    reproduced after verification round 1).
215:    (changed from partially_reproduced after verification round 1). The deviation is not sampling
305:verifications:
473 ../../attempts/000289-kutschireiter-2023-01.yaml
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000289-kutschireiter-2023-01
3	dataset:
4	  archive: dandi
5	  id: "000289"
6	  version: 0.240801.1040
7	  doi: 10.48324/dandi.000289/0.240801.1040
8	paper: doi:10.1073/pnas.2210622120
9	date: 2026-10-29
10	entry: 000289-kutschireiter-2023
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 454 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat questions/000289.yaml | sed -n 20,200p; ls schemas; grep -n "fig4b\|figs2" -A30 claims/000289*.yaml 2>/dev/null | grep -n "criterion\|statement\|reading\|mostly" | head -30; ls claims | grep 289
```

```
In the full network the noise also raises the rectified sum that drives the global inhibition
    (from 0.5 to 0.57 to 0.76 after 1 s), and the mean amplitude falls to 0.42 to 0.83 after 5 s,
    so (2) fails and the claim is partially reproduced. With the inhibition held at its noise-free
    level the mean amplitude rises to 1.01 to 1.33, matching the mean that SI Eq. S124 implies
    (1.02 to 1.35), so (2) would hold and the claim would be reproduced.
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
000289
```

**Agent calls Bash**

```bash
ls claims/000289; grep -n "id: fig4b\|id: figs2" -A40 claims/000289/*.yaml | head -110; grep -rn "questions" docs/protocol.md | head; ls questions | head;
```

```
10.1073-pnas.2210622120.yaml
315:- id: fig4b-connectome-motifs
316-  statement: >-
317-    The connectivity among EPG, Delta7 and PEN1 neurons in the hemibrain connectome resembles the
318-    connectivity of a network that implements the approximate circular Kalman filter, with shifted
319-    PEN1 to EPG projections and broad EPG to Delta7 to EPG inhibition.
320-  source: Fig. 4 B and C legends; SI Appendix, section 4A
321-  quote: >-
322-    The connectivity profile of a recurrent neural network (RNN) ( Fig. 2 D – F ) that implements
323-    an approximate circKF is strikingly similar to the connectivity of neurons in the Drosophila HD
324-    system.
325-  data: elsewhere
326-  where: >-
327-    neuPrint hemibrain:v1.2.1 (Scheffer et al. 2020, eLife 9, e57443), synapse counts between EPG,
328-    Delta7 and PEN1 neurons
329-  criterion: >-
330-    Fig. 4B legend: connections from hemibrain:v1.2.1, total synapse count per cell pair as the
331-    connection strength, neurons sorted by spatial position as a proxy for preferred HD, Delta7 to
332-    Delta7 omitted. The code does not hold this analysis. Sorting is open; readings: (a) by the
333-    protocerebral bridge glomerulus in the neuron's name (L9 to R9), (b) by the ellipsoid body or
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 169,182p docs/protocol.md; sed -n 305,325p docs/protocol.md
```

```
### 6. Answer questions

A reader is asked only when the author or a verifier believes the claims file
misreads the paper: a wrong expected value, the wrong panel, a claim that does
not say what the paper says (author, step 1.6, and "Hand over for
verification"). A method detail the claims file lacks is not asked: the author
takes it from the paper. The reader, who has not seen the data, checks each
question against the paper and decides whether the claims file is to change.
Where it is, the reader amends the claim, and the question's `answer` says
what changed and why, citing the passage; where it is not, the answer says why
the claim stands. The reader marks each question answered in
`questions/<folder>.yaml`.

## Author
     assumption.
   - Only when there is no defensible basis for a choice, so that any choice
     would be arbitrary, is the claim blocked as `methods_underspecified`,
     with the result of every reading that was run.
   - In either case the question is for the paper's authors, not a reader,
     so that they can confirm or correct the choice: state it in the claim's
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; grep -rho "[^.]*sorted by[^.]*\.[^.]*\." paper/ | head -5; grep -rho "[^.]*mostly independent[^.]*\." paper/ | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
p = "questions/000289.yaml"
s = open(p).read()
old = """    In the full network the noise also raises the rectified sum that drives the global inhibition
    (from 0.5 to 0.57 to 0.76 after 1 s), and the mean amplitude falls to 0.42 to 0.83 after 5 s,
    so (2) fails and the claim is partially reproduced. With the inhibition held at its noise-free
    level the mean amplitude rises to 1.01 to 1.33, matching the mean that SI Eq. S124 implies
    (1.02 to 1.35), so (2) would hold and the claim would be reproduced.
"""
assert old in s
new = """    In the full network the noise also raises the rectified sum that drives the global inhibition
    (from 0.5 to 0.57 to 0.77 after 1 s), and the mean amplitude falls to 0.42 to 0.83 after 5 s,
    so (2) fails and the claim is partially reproduced. With the inhibition held at its noise-free
    level the mean amplitude rises to 1.01 to 1.38, matching the mean that SI Eq. S124 implies
    (1.02 to 1.35), so (2) would hold and the claim would be reproduced. With the inhibition set by
    the decoded amplitude, which keeps the restoring force and removes only the noise's own
    contribution to the inhibition, the mean amplitude ends at 1.002 to 1.045, above the noise-free
    1.000 to 1.001 in all four settings, so (2) would also hold.
- claim: fig4b-connectome-motifs
  asked: 2026-10-30
  question: >-
    The criterion requires two sorts of the neurons, (a) by the protocerebral bridge glomerulus in
    the neuron's name and (b) by the ellipsoid body or gall position in the name. Hemibrain instance
    names give only the PB glomerulus for EPG and PEN1 neurons (EPG(PB08)_L1, PEN_a(PB06a)_R2), so
    reading (b) cannot be formed from the names. The legend names one sort, "spatial position". Is
    reading (b) part of the claim, or should the claim be judged on a sort that the connectome's
    names allow?
  passage: >-
    "Neurons were sorted by their spatial position as a proxy for their preferred HD. The total
    number of synaptic connections between each cell pair was taken to indicate the functional
    connection strength between these cells." (Fig. 4B legend)
  why: >-
    Under reading (a), counting any synapse, both parts of the criterion hold (left PEN1 +0.56,
    right PEN1 -0.48 glomeruli; every Delta7 reaches more than half the EPG glomeruli for input and
    output). Because reading (b) cannot be formed and the criterion requires both, the outcome is
    partially reproduced; with reading (a) alone it would be reproduced.
- claim: figs2-performance-independent-of-n
  asked: 2026-10-30
  question: >-
    The paper says accuracy is "mostly independent" of N. The criterion requires every value with N
    of 8 and more (or 16 and more) to be within 0.02 of the reference at every rate. Does "mostly"
    allow single exceptions, so that a criterion over all values is tighter than the paper's claim?
  passage: >-
    "Network inference performance is mostly independent of the number of neurons N in the Bayesian
    ring attractor network." (SI Appendix, Fig. S2 legend)
  why: >-
    Of the 160 stored values, one (N 16 at 0.1/s, 0.041 below the reference, 4.3 standard errors of
    a difference) is beyond 0.02, and every other value, N 3 and 4 included, is within 0.019. The
    outcome is not reproduced on that one value; a criterion that allows isolated exceptions would
    give reproduced or partially reproduced.
"""
open(p, "w").write(s.replace(old, new))
EOF
python -c "import yaml;print(len(yaml.safe_load(open('questions/000289.yaml'))['questions']))"
```

```
3
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml",
 "old_string": "    0.52 standard errors, within sampling error. The criterion gives no tolerance, so condition 4\n    fails as written.",
 "new_string": "    0.52 standard errors, within sampling error. The cells are independent samples, since\n    performance_scan_figure3d.py runs each (kappa*, beta) as its own process and sets no seed (its\n    lines are printed). The criterion gives no tolerance, so condition 4 fails as written."
}
```

```
The file attempts/000289-kutschireiter-2023-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml",
 "old_string": "    RNN_filter_Run the noise also raises the rectified sum that drives the global inhibition (from\n    0.5 without noise to 0.57 to 0.76 at 1 s), and the zero mode stays near 0. With the inhibition\n    held at its noise-free level, so that the noise is only one more input to unchanged dynamics as\n    in SI section 5 (Eqs. S107 to S109), the mean amplitude rises to 1.08, 1.33, 1.01 and 1.07 after\n    5 s, within 1.5 standard errors of the mean that SI Eq. S124 implies (1.08, 1.35, 1.02, 1.08).\n    So the SI's upward drift is present in the noise's direct effect, and in the released network\n    the effect on the inhibition outweighs it. The criterion tests the full network; whether the\n    paper claims the drift for the full network is asked of a reader (questions/000289.yaml).",
 "new_string": "    RNN_filter_Run the noise also raises the rectified sum that drives the global inhibition (from\n    0.5 without noise to 0.57 to 0.77 at 1 s), and the zero mode stays near 0. With the inhibition\n    held at its noise-free constant the mean amplitude rises to 1.08, 1.38, 1.01 and 1.08 after 5 s,\n    within 1.9 standard errors of the mean that SI Eq. S124 implies (1.08, 1.35, 1.02, 1.08). That\n    control removes both the noise's effect on the inhibition and the restoring force toward\n    kappa* 1, so it confirms the SI's noise term but does not isolate the cause. With the inhibition\n    set to the value a noise-free bump of the decoded amplitude gives, which keeps the restoring\n    force, the mean amplitude ends at 1.002, 1.045, 1.003 and 1.005, above the noise-free 1.000 to\n    1.001 in all four settings (z 0.35, 6.2, 1.3, 1.1) and within 1.2 standard errors of the\n    reduced two-dimensional SDE of the first mode. So the noise's direct effect gives a small upward\n    drift, and in the released network the fall comes from the noise's own contribution to the\n    rectified sum that drives the inhibition. The criterion tests the full network; whether the\n    paper claims the drift for the full network is asked of a reader (questions/000289.yaml)."
}
```

```
The file attempts/000289-kutschireiter-2023-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml",
 "old_string": "    Of the 161 values in figureS2.npz (7 network sizes, 23 rates), one is more than 0.02 from the",
 "new_string": "    Of the 160 values in figureS2.npz (7 network sizes, 23 rates, one missing), one is more than 0.02 from the"
}
```

```
The file attempts/000289-kutschireiter-2023-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml",
 "old_string": "    sampling error at low rates (about 1.2 values beyond it expected by chance alone), but this\n    value is far beyond it. One value (N 128 at 100/s) is missing (NaN) in the stored array.",
 "new_string": "    sampling error at low rates (about 1.2 of the values with N of 8 and more expected beyond it by\n    chance alone), but this value is far beyond it. One value (N 128 at 100/s) is missing (NaN) in\n    the stored array. Whether \"mostly independent\" allows single exceptions is asked of a reader\n    (questions/000289.yaml)."
}
```

```
The file attempts/000289-kutschireiter-2023-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml",
 "old_string": "    could not be run, and the criterion requires both, so the claim holds in part (changed from\n    reproduced after verification round 1).",
 "new_string": "    could not be run, and the criterion requires both, so the claim holds in part (changed from\n    reproduced after verification round 1). Whether reading (b) belongs to the claim is asked of a\n    reader (questions/000289.yaml)."
}
```

```
The file attempts/000289-kutschireiter-2023-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml",
 "old_string": "    the baseline). The ROI masks are a few pixels each on the PB midline, and the dF/F agrees with",
 "new_string": "    the baseline). The ROI masks are 2D, 3 to 11 pixels each (median 7), and the dF/F agrees with"
}
```

```
The file attempts/000289-kutschireiter-2023-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/000289-kutschireiter-2023-01.yaml",
 "old_string": "    causes a positive drift of the amplitude. The fall comes from the noise raising the rectified\n    sum that drives the global inhibition; with the inhibition held at its noise-free level the\n    amplitude rises as SI Eq. S124 implies (1.01 to 1.33).",
 "new_string": "    causes a positive drift of the amplitude. With the inhibition set to the value a noise-free bump\n    of the decoded amplitude gives, which keeps the restoring force and removes only the noise's own\n    contribution to the rectified sum that drives the inhibition, the mean amplitude ends at 1.002\n    to 1.045, above the noise-free value, so the fall comes from that contribution."
}
```

```
The file attempts/000289-kutschireiter-2023-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p = "attempts/000289-kutschireiter-2023-01.yaml"
s = open(p).read()
s = s.replace("""    Of the 160 values in figureS2.npz (7 network sizes, 23 rates, one missing), one is more than 0.02 from the
    quadratic circKF reference,""", """    Of the 160 values in figureS2.npz (7 network sizes, 23 rates, one missing), one is more than
    0.02 from the quadratic circKF reference,""")
s += """- date: '2026-10-30'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: >-
    Round 2. The full executed notebook of the first revision with its conclusions and summary, the
    helper module, the README, the attempt record and the claims file, with the paper. The verifier
    checked each outcome, each assumption and each sentence of the conclusions against the printed
    outputs, and whether its round-1 points were resolved. It agreed with all 13 outcomes.
  results:
  - claim: fig1-conflict-decreases-certainty
    agrees: true
    outcome: reproduced
    reason: Cell 13 gives 6 of 6 under (a) and (b).
    response: No change needed.
  - claim: fig2h-bump-tracks-circkf
    agrees: true
    outcome: reproduced
    reason: Supported by cell 16.
    response: No change needed.
  - claim: fig2i-accuracy-and-certainty-vs-reliability
    agrees: true
    outcome: reproduced
    reason: Supported by cell 19.
    response: No change needed.
  - claim: fig3b-bayesian-beats-conventional
    agrees: true
    outcome: reproduced
    reason: Supported by cell 22.
    response: No change needed.
  - claim: fig3c-update-weights
    agrees: true
    outcome: reproduced
    reason: Supported by cell 25.
    response: No change needed.
  - claim: fig3d-best-network-slow-decay
    agrees: true
    outcome: partially_reproduced
    reason: >-
      Condition 4 fails as written (cell 28). "Each cell is its own scan" is used to compute the SE
      of a difference between two grid cells (0.0026), which gives the "0.32 and 0.52 SE, within
      sampling error" verdict, but nothing printed shows that the grid cells use independent
      trajectories; if the scan reuses trajectories, that SE is too large. This affects only the
      "within sampling error" reading; condition 4 fails as written either way.
    response: >-
      The notebook now prints the lines of performance_scan_figure3d.py that set the grid cell
      (kappa_star and beta from sys.argv) and shows that the script sets no seed, so each cell is a
      separate process with its own operating-system seed and independent trajectories. The
      conclusion and the notes say so. Outcome kept.
  - claim: fig3f-noise-drop-below-70
    agrees: true
    outcome: reproduced
    reason: Supported by cell 31.
    response: No change needed.
  - claim: fig3f-retuning-reduces-drop
    agrees: true
    outcome: reproduced
    reason: >-
      3 of 6 readings fall in 31.5 to 38.5%, and the SNR ratio is 1.05 to 3.00 (cell 34). B10 is
      not changed; the retuned performance is still a maximum over noisy grid cells, which biases it
      upward, and the reduction values (34.64%) depend on it. The record keeps it because the
      paper's notebook does the same, which is acceptable.
    response: No change; the analysis follows the paper's notebook, as the verifier accepts.
  - claim: noise-effects-on-mu-and-kappa
    agrees: true
    outcome: partially_reproduced
    reason: >-
      As the criterion is written, condition (2) fails in all 4 settings (cell 37). Criterion (2)
      tests the drift on the full network, while SI section 5 derives only the noise term's own
      contribution (B1, forwarded to a reader). The inh_fixed control replaces the whole inhibition
      term with a constant; that term is the only one that depends on amplitude, the decay that
      pulls the bump back to kappa* 1, so the first mode turns neutral and the amplitude is a free
      2-D random walk. The control changes two things at once and shows that the SI's noise term is
      correct, but not that the noise's effect on the inhibition is what outweighs the drift in the
      full network. Cell 38, the bra.rnn_batch docstring ("the other dynamics are unchanged") and
      the record ("the fall comes from the noise raising the rectified sum") go beyond what the
      diagnostic shows. A cleaner control would keep the inhibition at the value implied by the
      decoded amplitude alone.
    response: >-
      Added the cleaner control. bra.rnn_batch takes inh_per_amp, which sets the inhibition to the
      value a noise-free cosine bump of each run's decoded amplitude gives; this keeps the restoring
      force and removes only the noise's own contribution to the rectified sum. The mean amplitude
      after 5 s is then 1.002, 1.045, 1.003 and 1.005, above the noise-free 1.000 to 1.001 in all
      four settings (z 0.35, 6.2, 1.3, 1.1) and within 1.2 SE of a direct simulation of the reduced
      two-dimensional SDE of the first mode. Cell 38, the docstring, the notes and the code_mismatch
      finding now say that the constant-inhibition control removes both effects, and base the cause
      on the new control. The re-run changed the constant-inhibition numbers slightly (1.08, 1.38,
      1.01, 1.08, within 1.9 SE of the Rice means; inhibition 0.57 to 0.77 at 1 s), and the text
      and the question to the reader were updated to them. Outcome kept.
  - claim: fig4b-connectome-motifs
    agrees: true
    outcome: partially_reproduced
    reason: >-
      The criterion needs two sorts and only reading (a) can be formed (cells 6 and 40). Both
      assumptions (any synapse counts as a connection; the offset measure) are stated and
      reasonable. The criterion offers an ellipsoid-body or gall sort "in the name" that hemibrain
      names cannot provide, then requires both sorts, so the partial outcome comes from how the
      criterion is written, not from the connectome.
    response: >-
      Added a question for a reader (questions/000289.yaml) on whether reading (b) belongs to the
      claim; the notes say it is asked. Outcome kept.
  - claim: fig4gh-drosophila-network-matches
    agrees: true
    outcome: partially_reproduced
    reason: >-
      Reading (a) fails at 0.1, 0.2 and 0.3/s (cell 43). The differences are 1.16 to 1.95 SE; the
      outcome rests on the criterion's bounds, and the record says so.
    response: No change needed.
  - claim: figs2-performance-independent-of-n
    agrees: true
    outcome: not_reproduced
    reason: >-
      N 16 at 0.1/s is 0.0414 off, both readings fail (cell 46); it is 4.3 SE off, so not noise.
      The paper says "mostly independent", but the criterion requires every one of the 161 cells to
      be within 0.02, and the outcome rests on one cell. The README's "one value of 161" is wrong,
      as there are 160 values (one is NaN), and the record's "about 1.2 values expected" leaves out
      that the expectation covers N of 8 and more only.
    response: >-
      README and notes now say 160 values; the notes and the conclusion say the 1.2 covers N of 8
      and more. Added a question for a reader on whether "mostly" allows single exceptions. Outcome
      kept.
  - claim: prediction-bump-amplitude-cue-reliability
    agrees: true
    outcome: blocked
    reason: >-
      dF/F with reading (b) gives p 0.138; the other three combinations hold (cell 50). Cell 51
      swaps the median high/low ratios (dF/F 1.120, raw 1.112 in cell 50); the record has them the
      right way round. "The ROI masks are 5 to 9 pixels on the PB midline" in the summary is never
      printed; the figure appears only in a bra.py docstring.
    response: >-
      Cell 51 now gives 1.11 for raw and 1.12 for dF/F in the right order. The data check prints
      the mask sizes (3 to 11 pixels, median 7, over 628 ROIs), and the summary, cell 9, the
      docstring and the metadata_insufficient finding now use them. Cell 11 now gives the lag of 5
      frames as 0.54 s at 9.18 Hz and 0.64 s at 7.87 Hz. Outcome kept.
"""
open(p, "w").write(s)
EOF
python tools/entry.py check entries/000289-kutschireiter-2023 2>&1 | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
git diff | grep "^+" | grep -n "—\|rather" ; date -u; python tools/entry.py all entries/000289-kutschireiter-2023 2>&1 | tail -3; date -u
```

```
Fri Oct 30 01:37:28 UTC 2026
Installed kernelspec registry-000289-kutschireiter-2023 in executed/000289-kutschireiter-2023/.venv/share/jupyter/kernels/registry-000289-kutschireiter-2023
0 error(s)
pass  reproduce_kutschireiter_2023.ipynb  (396 s)
Fri Oct 30 01:44:12 UTC 2026
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('executed/000289-kutschireiter-2023/reproduce_kutschireiter_2023.ipynb'))
for i in [8,28,37,53]:
    t=''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
    print('=====',i); print(t[-1500:] if i==37 else '\n'.join(l for l in t.splitlines() if 'mask' in l or 'seed' in l or 'ran in' in l or 'rises' in l))
"; git status --short
```

```
===== 8
ROI mask sizes, pixels with nonzero weight per ROI: min 3, median 7, max 11 over 628 ROIs; mask array shape of sub-1: (37, 256, 128)
===== 28
steps of the maximum for beta above the best: [-0.0031 -0.0013 -0.0021 -0.0013  0.0008 -0.0062  0.0014 -0.0168 -0.02   -0.0203] ; rises: 2 of 10
performance_scan_figure3d.py, lines that set the grid cell or a seed: ['kappa_star = float(sys.argv[1])', 'beta = float(sys.argv[2])', 'nIter = 10000']
rises of the maximum over kappa*, in SEs of a difference: [0.32 0.52]
===== 37
p.float64(0.501)} True

global inhibition and zero mode in the full network, and the end amplitude with the inhibition held:
  N  sigma  inh_noise_free  inh_t01  inh_t1  inh_t5  zero_mode_t5  amp_end_full  amp_end_inh_fixed  se_inh_fixed  amp_end_SI_rice
 64    1.0             0.5   0.5196  0.5695  0.5281        0.0007        0.8249             1.0756        0.0085           1.0824
 64    2.0             0.5   0.5889  0.7680  0.7279       -0.0096        0.6394             1.3802        0.0148           1.3522
256    1.0             0.5   0.5202  0.5662  0.5231       -0.0022        0.8214             1.0114        0.0044           1.0197
256    2.0             0.5   0.5877  0.7587  0.7071       -0.0019        0.4297             1.0820        0.0084           1.0824

end amplitude with the inhibition set by the decoded amplitude (iii), against the noise-free run and the 2-D SDE:
  N  sigma  amp_noise_free  amp_end_inh_of_amp  se_inh_of_amp  amp_end_2d_sde  z_vs_noise_free  z_vs_2d_sde  amp_end_full
 64    1.0          1.0007              1.0021         0.0039          1.0037           0.3501      -0.3970        0.8249
 64    2.0          1.0007              1.0453         0.0071          1.0373           6.2475       1.1210        0.6394
[... 21 more lines not kept]
```

**Agent**

I made all of the round-2 report's corrections and added the noise control it suggested. **No outcome changed and nothing is proposed for round 3:** the verifier agreed with all 13 outcomes, and nothing I found argues for changing one. The entry was re-run with `python tools/entry.py all`: the check reports 0 errors and the notebook passes (6.5 min). Every number in the conclusions, record, README and question file matches the new outputs.

**Noise claim (the main point)**
- **New control:** `bra.rnn_batch` has a new option, `inh_per_amp`, that does what the verifier suggested. It sets the inhibition to the value a noise-free bump of each run's decoded amplitude would give. This keeps the force that pulls the amplitude back to 1 and removes only the noise's own contribution to the inhibition.
- **Result:** the mean amplitude after 5 s is 1.002, 1.045, 1.003 and 1.005, above the noise-free value (about 1.000) in all four settings. Only N = 64 at noise SD 2 clearly exceeds sampling error (z = 6.2). These values agree, within 1.2 standard errors, with a direct simulation of the reduced two-dimensional equation for the bump.
- **What it shows:** the fall of the amplitude in the full network comes from the noise's extra contribution to the inhibition. That was previously asserted without a control that isolated it.
- **Text corrected:** cell 38, the `rnn_batch` docstring, the record's notes and the `code_mismatch` finding now say that the old fixed-inhibition control removed two things at once.
- **Numbers shifted:** the re-run changed the fixed-inhibition figures slightly, to 1.08, 1.38, 1.01 and 1.08 (within 1.9 standard errors, up from 1.5), with inhibition 0.57 to 0.77 at 1 s. The text and the existing question to the reader now use these.

**Other corrections**
- **Prediction claim (cell 51):** the swapped ratios are fixed. They now read dF/F 1.12 and raw 1.11.
- **ROI masks:** the data check now prints the mask sizes: 3 to 11 pixels, median 7, over 628 ROIs. The old figure of "5 to 9 pixels on the PB midline" was never printed and was wrong. The summary, cell 9, the docstring and the finding are updated.
- **fig3d:** the notebook now prints the lines of the paper's scan script that set each grid cell. The script sets no random seed and runs each cell as a separate process, so the cells are independent samples. The "within sampling error" verdict stands, and the conclusion and notes now say why.
- **Minor fixes:**
  - Cell 11: a 5-frame lag is 0.54 s at 9.18 Hz and 0.64 s at 7.87 Hz.
  - figs2: the README and notes say 160 values, not 161.
  - figs2: the "about 1.2 expected" now says it covers N of 8 and more only.

**Questions for a reader:** I added two to `questions/000289.yaml`, both on places where the verifier says the criterion is tighter than the paper. Neither claim was changed.
- **fig4b:** is reading (b), a sort the hemibrain names cannot provide, really part of the claim?
- **figs2:** does "mostly independent" allow a single exception?

**Record:** round 2 is added under `verifications`, with all 13 results marked as agreeing, the verifier's reasons in its own words, and my responses.

**Not done:** B10 (the retuned performance is biased upward) is left as it was, since the paper's notebook does the same and the verifier accepted that. Nothing was committed.

## End of run

46 turns, 19 minutes, result: success.
