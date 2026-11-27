# clark-2026 · author-revise-1 · run 45861210425

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/clark-2026/verifier-1-report.md; ls entries/clark-2026 entries/clark-2026/*
```

```
Thu Nov 26 16:49:28 UTC 2026
**Verifier report, round 1: Clark, Abbott & Sompolinsky (2026) on DANDI:000939 (0.240528.1542)**

The claims file has 30 claims. The four notebooks test 26 of them; the other 4 appear in no notebook. No notebook treats any claim as blocked. I confirmed through the archive API that the pinned version has 31 assets, 9 of them `+ogen.nwb`, as `tuning_curves.ipynb` cell 3 shows.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| hd-cell-selection | reproduced | tuning_curves cell 10: 31 sessions, 2,691 units, 1,533 head-direction units under both readings, 0 dropped by nz_mask, 9 opto mice with 315 cells, and counts of 117/93/90/86 for the right mice. |
| tuning-curves-match-cache | reproduced | Cell 12: Pearson r = 1.000000 for 100% of 1,533 units; largest curve difference 1.4e-14. The cache's labels and session order equal the data's. |
| fig1e-heterogeneous-peaks | reproduced | Cell 16: peak counts of 1 to 6 occur; the interquartile range of the separation between the two highest peaks is 1.382 rad, above π/4. |
| fig5d-peak-numbers | reproduced | Cell 18: the data give exactly 1,533/412/55. Generative samples over five seeds give 23,908–24,267 curves with ≥2 peaks and 1,001–1,082 with ≥3, all within tolerance. |
| fig1fg-mean-and-fluctuation-profiles | reproduced | Cell 20: one maximum, at offset 0; symmetry r = 0.9998; sd/mean = 0.56, so both readings hold; median consistency r is 0.996 (mean) and 0.974 (sd). |
| fig3ab-centers-of-mass-uniform | reproduced | Cell 22: 2 sessions with uncorrected P < 0.05, 0 after BH correction, corrected P from 0.592 to 0.968. |
| fig3c-correlation-approaches-circulant | reproduced | Cell 24: the distance from circulant form falls monotonically for all 4 mice and both functions, under all 5 seeds. The leading 4 eigenvectors have ≥0.89 Fourier purity, and eigenvectors 1 and 2 are at frequency 1. |
| fig4-generative-fit | partially_reproduced | Cell 26: the 500k-sample pass chooses σ 1.4737 and
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
ls; ls attempts* 2>/dev/null | head; find . -path ./node_modules -prune -o -name "*clark-2026*" -print | grep -v "^./.git/" | head -30; wc -l docs/protocol.md
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
executed
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md
```

```
<persisted-output>
Output too large (46.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f315cfdc-8563-4ceb-a8ad-9e5cb40503e4/tool-results/bc9oboetl.txt

Preview (first 2KB):
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
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/clark-2026-01.yaml; ls transcripts/clark-2026 executed/clark-2026
```

```
schema_version: 3
id: clark-2026-01
datasets:
- archive: dandi
  id: "000939"
  version: 0.240528.1542
  doi: 10.48324/dandi.000939/0.240528.1542
  relation: reuses
paper: doi:10.1038/s41593-026-02452-4
date: 2026-11-26
entry: clark-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-18
  runner:
[... 406 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs; grep -n "^#" protocol.md | head -80
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
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
755:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 199,
 "limit": 440
}
```

```
199	## Author
200	
201	The workflow puts the paper under `paper/`, as for the reader. Read it to
202	understand the claims, their data and their figures. The claims file still
203	decides what is tested: do not change a claim's statement, expected values or
204	criterion. A method detail the claims file lacks is taken from the paper
205	(step 6).
206	
207	**Time.** An author run is stopped five hours after it starts, and whatever
208	is not recorded by then is lost. The prompt says when the run started and the
209	time by which to finish. Check the clock (`date -u`) between steps. When that
210	time comes, stop analysing and finish: record each claim not yet tested as
211	blocked, `too_large` where the computation is what stopped it, saying how far
212	it got, then write the attempt record and run the entry's checks. A record
213	with some claims blocked for time is worth more than a run that is cut off.
214	
215	### 1. Establish what can be tested
216	
217	Do this before any analysis.
218	
[... 420 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; ls schemas; grep -l "verifications:" attempts/*.yaml | head -3; python - <<'E'
import json,glob
for f in glob.glob('schemas/*attempt*'):
    print(f)
E
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
attempts/amjad-2025-01.yaml
attempts/andrews-2024-01.yaml
attempts/armstrong-2026-01.yaml
schemas/attempt.schema.json
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));
print(json.dumps(s['properties']['verifications'],indent=1)[:4000]);
d=s.get('\$defs',s.get('definitions',{}));print(list(d))
"; grep -n -A40 "^verifications:" attempts/armstrong-2026-01.yaml | head -60
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
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml
c=yaml.safe_load(open('claims/clark-2026.yaml'))
print([k for k in c if k!='claims'])
for cl in c['claims']:
    if cl['id'] in ('fig2gi-circulant-noise-collapses','figs8-s9-lambda-and-c','figs11b-data-network-global-stability','figs11-s12-global-stability-model','figs1-s2-spectrum-does-not-fix-symmetry','figs10-robustness-comparable','fig8-grid-scores-and-torus','figs14-data-spectrum-doublets'):
        print(yaml.safe_dump(cl,width=120))
E
```

```
['schema_version', 'paper', 'checks']
criterion: As in data_driven_attractor.ipynb. The sorted matrix; its circulant version, the average over circular diagonals;
  and the circulant plus noise, the residuals (circulant minus sorted) with all off-diagonal entries shuffled together, the
  asymmetric version used in Fig. 2d,i (numpy seed 42); both surrogates multiplied by 1.275. Each is run with c 1 from 100
  initial conditions at regularly spaced manifold points with input-current noise of standard deviation 2.5, for 30 s. A final
  state's position is the neuron index of the peak of its activity, smoothed across sorted neurons with a Gaussian of 2.5
  neurons, as the figure is drawn. The paper gives no count or similarity measure; these are fixed here and named as open.
  Final positions within 2 pi / 50 of each other (31 neurons) are merged into one state. Reproduced when the sorted optimal
  matrix keeps at least 50 distinct states, the circulant plus noise matrix at most 10, and the circulant matrix's final states
  are shifts of one another (each correlates at least 0.99 with the best circular shift of the first). Partially reproduced
  when the contrast between the optimal and the circulant plus noise holds alone. The symmetric scrambled version is shown
  as a variant.
data: dataset
depends_on:
- fig2b-sorted-weights-mexican-hat
id: fig2gi-circulant-noise-collapses
quote: The optimal weights (Fig. 2b) maintain a continuum of stable, heterogeneous states (Fig. 2g). Averaging the sorted
  weights along ... diagonals gives a circulant matrix (Fig. 2c) whose bumps are identical up to translation ... this network
  collapses onto a few discrete states within the 30-s window (Fig. 2i)
source: Results, Dynamics of the data-derived network model, paragraphs 4 and 5; Fig. 2c,d,g to i; Supplementary Note 3, section
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; wc -l *.py; cat entry.yaml README.md | head -80; python - <<'E'
import json
for nb in ['tuning_curves','network','network_grid','theory']:
    d=json.load(open(nb+'.ipynb'))
    print('==',nb,len(d['cells']))
    for i,c in enumerate(d['cells']):
        src=''.join(c['source'])
        print(i,c['cell_type'],c['metadata'].get('tags'),len(src),src[:80].replace('\n',' | '))
E
```

```
546 hdring.py
  384 ring_dmft.py
  930 total
schema_version: 1
name: clark-2026
type: reproduction
title: Symmetries and continuous attractors in disordered neural circuits (Clark, Abbott and Sompolinsky 2026)
description: Tests the findings of Clark, Abbott and Sompolinsky (2026) on dandiset 000939, the
  postsubiculum recordings of Duszkiewicz et al. (2024) that the paper reuses. It rebuilds the
  1,533 head-direction tuning curves from the NWB files with the paper's procedure, checks them
  against the paper's cached curves, and tests the tuning-curve statistics, the fitted
  generative process, the data-derived network and its dynamics, and the mean-field theory.
license: Apache-2.0
python: "3.13"
notebooks:
- path: tuning_curves.ipynb
  title: Tuning curves, their statistics and the generative process
  runtime_minutes: 18
- path: network.ipynb
  title: The data-derived network and its dynamics
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/davidclark1/symmetries-continuous-attractors repo 2>&1 | tail -2; cd repo && git checkout -q 245726fa78457e10cdcf17e6be36fba1dec98061 && ls notebooks ring
```

```
notebooks:
closing_the_loop.ipynb
data_and_generative_model.ipynb
data_driven_attractor.ipynb
data_driven_reconstruction.ipynb
dmft.ipynb
grid_sims.ipynb
mexican_hat_and_asymmetry.ipynb
reservoir_rnn.ipynb
spectra.ipynb
spurious_fixed_points.ipynb
weight_matrix_analyses.ipynb

ring:
__init__.py
analysis.py
data.py
data_driven.py
dmft.py
fn.py
[... 8 more lines not kept]
```

**Agent**

Paper code cloned. Next I look at the spurious_fixed_points and weight_matrix_analyses notebooks to cost the untested claims.

**Agent calls Bash**

```bash
cd $TMPDIR/repo/notebooks && python - <<'E'
import json
for nb in ['spurious_fixed_points','weight_matrix_analyses']:
    d=json.load(open(nb+'.ipynb'))
    print('=====',nb)
    for i,c in enumerate(d['cells']):
        if c['cell_type']!='code': 
            print(i,'MD',''.join(c['source'])[:300]);continue
        print(i,'CODE\n',''.join(c['source'])[:2500])
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream': print('  OUT:',''.join(o['text'])[:600])
E
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f315cfdc-8563-4ceb-a8ad-9e5cb40503e4/tool-results/bzz3n05vy.txt

Preview (first 2KB):
===== spurious_fixed_points
0 MD # Spurious fixed points and finite-N dynamics

Asks whether the network's attractor is only the encoded ring or whether other stable
states exist, approached from two directions: initial conditions far off the ring, and
networks too small to support a continuous attractor.

**Produces** Supplementar
1 CODE
 # Regeneration switches (default off so a normal run cannot overwrite committed figures/caches):
SAVE_FIGURES = False
REGENERATE_CACHES = False

import numpy as np
from ring import data_driven, sim
from tqdm import tqdm
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f315cfdc-8563-4ceb-a8ad-9e5cb40503e4/tool-results/bzz3n05vy.txt"
}
```

```
1	===== spurious_fixed_points
2	0 MD # Spurious fixed points and finite-N dynamics
3	
4	Asks whether the network's attractor is only the encoded ring or whether other stable
5	states exist, approached from two directions: initial conditions far off the ring, and
6	networks too small to support a continuous attractor.
7	
8	**Produces** Supplementar
9	1 CODE
10	 # Regeneration switches (default off so a normal run cannot overwrite committed figures/caches):
11	SAVE_FIGURES = False
12	REGENERATE_CACHES = False
13	
14	import numpy as np
15	from ring import data_driven, sim
16	from tqdm import tqdm
17	import matplotlib.pyplot as plt
18	from ring import style
19	from ring.seed import set_global_seed
20	import scipy
[... 945 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; grep -n "^def \|^    \"\"\"\|^[A-Z_]* = " hdring.py | head -80
```

```
21:DANDISET = "000939"
23:VERSION = "0.240528.1542"
24:API = "https://api.dandiarchive.org/api"
25:PAPER_KEY = "clark-2026"
28:DATA_DT = 0.01
29:N_THETA = 100
30:SIGMA_VALS = np.logspace(-1, 2, 100)
31:K_FOLDS = 4
34:ZENODO_TAR = "https://zenodo.org/api/records/21827768/files/symmetries_caches_v1.tar/content"
38:def seed(claim_id, k=0):
39:    """Seed of a claim's k-th generator (protocol, "Take every random seed from the claim")."""
43:def list_assets(version=VERSION):
44:    """All assets of the dandiset at the pinned version, as dicts (path, size, asset_id)."""
56:def asset_s3_url(asset_id, version=VERSION):
62:def session_order(assets):
63:    """Sessions in the order of the paper's code (ring/data.py, get_session_info).
67:    """
79:def _strs(x):
83:def load_session(asset_id, hd_only=True, version=VERSION):
84:    """Read what the analysis needs from one NWB file, by streaming.
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; sed -n 428,546p hdring.py; python -c "
import json;d=json.load(open('theory.ipynb'));print(''.join(d['cells'][14]['source']))"
```

```
/bin/bash: line 1: cd: entries/clark-2026: No such file or directory
def prepare_network_curves(Phi_data, N_theta=10000, sigma=2, n_sinkhorn=1000):
    """data_driven.prepare_smoothed_normalized_resampled_tuning_curves (Supplementary Note 3,
    section 8.1): inverse softplus (beta 2), circular Gaussian smoothing of 2 bins, softplus,
    Sinkhorn-Knopp normalization of both axes (1,000 sweeps), inverse softplus, Fourier
    resampling to N_theta angles, softplus. Input (N, 100); returns X, Phi of shape (N_theta, N)."""
    P = Phi_data.T.copy()
    X = inv_softplus(P, 2.0)
    Ps = nonlin(gaussian_filter1d(X, sigma=sigma, axis=0, mode="wrap"))
    for _ in range(n_sinkhorn):
        Ps /= Ps.mean(1, keepdims=True)
        Ps /= Ps.mean(0, keepdims=True)
    Xr = resample_curves_fft(inv_softplus(Ps, 2.0), N_theta)
    return Xr, nonlin(Xr)


def compute_J(X, Phi, lamda):
    """regression.compute_J (method opt): primal when N_theta >= N, else dual. Zero diagonal."""
    N_theta, N = Phi.shape
    if N_theta >= N:
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; sed -n 1,200p ring/sim.py | head -120; grep -n "def nonlin_idealized" -A8 ring/fn.py; grep -n "def gen_tuning_curves_idealized" -A30 ring/tc.py
```

```
"""ODE simulation of the ring-attractor dynamical system.

``run_sim`` performs Euler integration of

    tau * dx/dt = -x + J @ phi(x) + omega(t) * J' @ phi(x) + stabilizer

on GPU/CPU torch tensors, with optional periodic save of state and an
early-stop check that fires when per-batch derivatives plateau.
"""
import numpy as np
import torch
from . import fn


def run_sim(T, tau, dt, T_eval, J, x_init,
            nonlin=fn.unity_erf,
            omega_func=None, J_prime=None,
            target_mean=None, const=np.nan,
            return_derivs=False,
            break_if_stopped=True,
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
import json
d=json.load(open('../../executed/clark-2026/network.ipynb'))
for i in [5,10,13,19,22]:
    c=d['cells'][i]
    print('#### cell',i); print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('OUT>',''.join(o['text']))
E
```

```
#### cell 5
t = time.time()
X, Phi = H.prepare_network_curves(Phi_data)
J, J_prime = H.compute_weights(X, Phi, lamda=1e-8)
err = np.mean((X - Phi @ J.T) ** 2)
N = J.shape[0]
print(f"X, Phi {X.shape}; J {J.shape}; built in {time.time()-t:.0f} s")
print(f"err = {err!r} (paper's notebook: 1.7152363818838536e-08)")
print("diagonal of J is zero:", np.allclose(np.diag(J), 0), "| J range", J.min().round(4), J.max().round(4))
print("Sinkhorn result: mean over neurons of Phi at each angle, range", Phi.mean(1).min().round(4), Phi.mean(1).max().round(4))
Phi32 = Phi.astype(np.float32); Phi_sq = (Phi32 ** 2).sum(1)
OUT> X, Phi (10000, 1533); J (1533, 1533); built in 3 s
err = np.float64(1.715236379732375e-08) (paper's notebook: 1.7152363818838536e-08)
diagonal of J is zero: True | J range -0.1308 0.1509
Sinkhorn result: mean over neurons of Phi at each angle, range 1.0 1.0

#### cell 10
def run_2ef(sd):
    rng = np.random.default_rng(sd)
    x0 = X[::100].T + rng.standard_normal((N, 100)) * 3.0
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
import json
for nb,cells in [('tuning_curves',[13,33]),('theory',[5]),('network_grid',[4])]:
    d=json.load(open(f'../../executed/clark-2026/{nb}.ipynb'))
    for i in cells:
        c=d['cells'][i]
        print('####',nb,i); print(''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: print('OUT>',''.join(o['text'])[:3000])
E
```

```
/bin/bash: line 1: cd: entries/clark-2026: No such file or directory
#### tuning_curves 13
b, md5_calc, md5_listed = H.read_zenodo_member("mouse_data/tc_data.npz")
print("tc_data.npz MD5", md5_calc, "listed", md5_listed, "match:", md5_calc == md5_listed)
cache = H.load_npz_bytes(b)
c_names = cache["mouse_names"]; c_nums = cache["mouse_nums"]; c_hd = cache["hd_mask"]
print("cache: units", len(c_hd), "head-direction", int(c_hd.sum()), "sessions", len(cache["unit_counts"]))
print("cache session order equals ours:", [str(n) for n in pd.unique(c_names)] == [d["subject"] for d in sessions])
print("cache unit counts equal ours:", list(cache["unit_counts"]) == list(tab.units))
print("cache hd labels equal ours:", np.array_equal(c_hd, np.concatenate([d["sess"]["is_hd"] for d in sessions])),
      "| exc labels:", np.array_equal(cache["exc_mask"], np.concatenate([d["sess"]["is_exc"] for d in sessions])),
      "| fs labels:", np.array_equal(cache["fs_mask"], np.concatenate([d["sess"]["is_fs"] for d in sessions])))
ours_opt = np.concatenate([d["opt"] for d in sessions]); ours_sig = np.concatenate([d["sig"] for d in sessions])
ours_plain = np.concatenate([d["plain"] for d in sessions])
c_opt = cache["opt_tcs"][c_hd]; c_sig = cache["opt_sigmas"][c_hd]; c_plain = cache["plain_tcs"][c_hd]
r = np.array([np.corrcoef(a.mean(0), b_.mean(0))[0, 1] for a, b_ in zip(ours_opt, c_opt)])
print("units compared:", len(r))
print(f"Pearson r of partition-averaged curves: min {r.min():.6f}, median {np.median(r):.6f}; fraction >= 0.99: {(r >= 0.99).mean():.4f}")
print("max abs difference of partition-averaged curves (Hz):", float(np.abs(ours_opt.mean(1) - c_opt.mean(1)).max()))
print("max abs difference of plain curves (Hz):", float(np.abs(ours_plain - c_plain).max()))
[... 288 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; sed -n 200,236p hdring.py; grep -rn "err_grid" $TMPDIR/repo/notebooks/data_driven_reconstruction.ipynb | head -5
```

```
opt_sig[u, k] = sigma_vals[j]
    return plain, opt, opt_sig


def read_zenodo_member(name):
    """Read one member of the Zenodo cache tar by range requests, and check its MD5.

    Returns (bytes, md5 computed, md5 listed in the record's CHECKSUMS.md5).
    """
    import fsspec
    import tarfile

    listed = {}
    for line in requests.get(ZENODO_MD5, timeout=60).text.splitlines():
        if line.strip():
            h, p = line.split()
            listed[p] = h
    with fsspec.open(ZENODO_TAR, block_size=2**20).open() as fh:
        tf = tarfile.open(fileobj=fh, mode="r:")
        for mem in tf:
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; grep -n "ZENODO_MD5 =" hdring.py; python - <<'E'
import json
d=json.load(open('/tmp/x.ipynb' if False else __import__('os').environ['TMPDIR']+'/repo/notebooks/data_driven_reconstruction.ipynb'))
for c in d['cells']:
    s=''.join(c['source'])
    if 'err_grid' in s or 'np.savez' in s or 'np.load' in s: print('-----\n',s[:1800])
E
python -c "
import hdring as H,requests
t=requests.get(H.ZENODO_MD5,timeout=60).text
print(t)"
```

```
Exit code 1
35:ZENODO_MD5 = "https://zenodo.org/api/records/21827768/files/CHECKSUMS.md5/content"
-----
 # ================================
# Convergence grid: run + save + plot
# ================================

import torch

# --- Grid
c_vals = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5]
# Ten decades of ridge, centred on the operating value lamda = 1e-8 at index 2. The
# value is in the N-normalized convention; see regression.compute_J.
lamda_vals = [1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 1e-2]

# --- Global sim params
T, tau = 30, 0.05
T_eval = tau # tau / 5.
dt = tau / 10. # tau / 50.
N_ics = 100
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; PY=../../executed/clark-2026/.venv/bin/python; $PY -c "
import hdring as H,requests
print(requests.get(H.ZENODO_MD5,timeout=60).text)"; curl -s https://zenodo.org/api/records/21827768 | python -c "import json,sys;d=json.load(sys.stdin);print([(f['key'],f['size']) for f in d['files']])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/clark-2026; PY=../../executed/clark-2026/.venv/bin/python; time $PY -c "
import hdring as H, numpy as np
for m in ['pc_convergence_grid.npz','grid_search_results.npz','spurious_fixed_points.npz']:
    b,a,l=H.read_zenodo_member(m); print(m,len(b),a==l)
    z=H.load_npz_bytes(b)
    for k in z.files:
        try: v=z[k]; print('  ',k,v.shape,v.dtype, v if v.size<50 else '')
        except Exception as e: print('  ',k,'ERR',e)
"
```

```
pc_convergence_grid.npz 70567320 True
   pcs_grid ERR Object arrays cannot be loaded when allow_pickle=False
   pcs_traj3_grid ERR Object arrays cannot be loaded when allow_pickle=False
   err_grid (6, 7) float64 [[3.78923866e-09 3.78923866e-09 3.78923866e-09 3.78923866e-09
  3.78923866e-09 3.78923866e-09 3.78923866e-09]
 [1.34645794e-10 1.34645794e-10 1.34645794e-10 1.34645794e-10
  1.34645794e-10 1.34645794e-10 1.34645794e-10]
 [1.71523638e-08 1.71523638e-08 1.71523638e-08 1.71523638e-08
  1.71523638e-08 1.71523638e-08 1.71523638e-08]
 [4.64254721e-06 4.64254721e-06 4.64254721e-06 4.64254721e-06
  4.64254721e-06 4.64254721e-06 4.64254721e-06]
 [4.87196741e-04 4.87196741e-04 4.87196741e-04 4.87196741e-04
  4.87196741e-04 4.87196741e-04 4.87196741e-04]
 [2.08414736e-02 2.08414736e-02 2.08414736e-02 2.08414736e-02
  2.08414736e-02 2.08414736e-02 2.08414736e-02]]
   c_vals (7,) float64 [0.   0.25 0.5  0.75 1.   1.25 1.5 ]
   lamda_vals (6,) float64 [1.e-12 1.e-10 1.e-08 1.e-06 1.e-04 1.e-02]
   T () int64 30
   tau () float64 0.05
   dt () float64 0.005
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/clark-2026; PY=../../executed/clark-2026/.venv/bin/python; time $PY -c "
import hdring as H, numpy as np
b,a,l=H.read_zenodo_member('grid_search_results.npz'); z=H.load_npz_bytes(b); L=z['loss_vals']
o=np.argsort(L.ravel())[:8]
for f in o:
    i,j,k=np.unravel_index(f,L.shape); print(i,j,k,z['scale_vals'][i].round(4),z['bias_vals'][j].round(4),z['beta_vals'][k].round(4),L[i,j,k])
print('at ours', L[9,7,9])
"
```

```
Thu Nov 26 16:56:20 UTC 2026
8 10 8 1.4211 1.7307 2.7659 0.008898164406421858
9 7 9 1.4737 1.2145 3.1103 0.008999878726433265
9 3 14 1.4737 0.5262 4.8328 0.010512173737006851
9 4 12 1.4737 0.6983 4.1438 0.011793416918134115
9 9 8 1.4737 1.5586 2.7659 0.011820157733328791
9 2 18 1.4737 0.3541 6.2107 0.012069793552455842
10 3 14 1.5263 0.5262 4.8328 0.01210391267017347
10 2 18 1.5263 0.3541 6.2107 0.0142126248073461
at ours 0.008999878726433265

real	0m12.233s
user	0m1.174s
sys	0m0.091s
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo/notebooks && python - <<'E'
import json
d=json.load(open('weight_matrix_analyses.ipynb'))
s=''.join(d['cells'][10]['source']); i=s.find('def run_and_measure'); print(s[i:i+4000])
d=json.load(open('spurious_fixed_points.ipynb'))
s=''.join(d['cells'][3]['source']); i=s.find('Second row'); print(s[i:i+2500])
E
grep -n "def compute_distances_to_ring" -A25 $TMPDIR/repo/ring/data_driven.py | head -40
```

```
def run_and_measure(J_base, x_init, f_weights, label):
    """Run dynamics, measure overlaps and maxima."""

    # Perturb weights
    J_noisy = J_base + np.random.randn(*J_base.shape) * f_weights * J_base.std()

    # Run simulation
    x_dyn_final, X_dyn, finished = sim.run_sim(
        T=T_total,
        tau=tau,
        dt=dt,
        T_eval=T_eval,
        J=torch.Tensor(J_noisy).to(device),
        x_init=torch.Tensor(x_init).to(device),
        nonlin=phi_fn,
        break_if_stopped=False,
    )

    # Overlap order parameter
    m_dyn = (1.0 / N) * torch.einsum(
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; sed -n 1,20p hdring.py; grep -n "^from\|^import" hdring.py
```

```
"""Loading and measures for the attempt on Clark, Abbott & Sompolinsky (2026) on DANDI:000939.

Every procedure here follows the paper's code, github.com/davidclark1/symmetries-continuous-attractors
at commit 245726fa78457e10cdcf17e6be36fba1dec98061 (the "ring" package), as the claims file
(claims/clark-2026.yaml) cites it. Each function names the function of the paper's code it
repeats. The paper's code imports torch; the parts used here are rewritten in numpy so that the
entry needs no GPU stack. Where a parameter comes from somewhere else it is said so.

Data are streamed from the DANDI archive (remfile and h5py); nothing is downloaded to disk.
"""
import hashlib
import io
import zlib

import h5py
import numpy as np
import remfile
import requests
from scipy.ndimage import gaussian_filter1d

[... 9 more lines not kept]
```

**Agent**

Now I'll extend the helper: selectable nonlinearity in `simulate`, and the idealized generative model.

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
s=open('hdring.py').read()
s=s.replace('''def simulate(J, x0, T, tau=0.05, dt=0.001, c=1.0, save_every=None, J_prime=None, omega=None,
             on_save=None, dtype=np.float32):''','''def simulate(J, x0, T, tau=0.05, dt=0.001, c=1.0, save_every=None, J_prime=None, omega=None,
             on_save=None, dtype=np.float32, phi=None):''')
s=s.replace('''    t = T - dt (run_sim's loop is range(1, N_t))."""
    J = J.astype(dtype)''','''    t = T - dt (run_sim's loop is range(1, N_t)).
    phi replaces the softplus when given (nonlin_idealized for the generative-process networks,
    which spurious_fixed_points.ipynb and weight_matrix_analyses.ipynb run with c 0, no stabilizer)."""
    phi = phi or nonlin
    J = J.astype(dtype)''')
s=s.replace('''        for i in range(1, N_t):
            r = nonlin(x)
            drive = J @ r''','''        for i in range(1, N_t):
            r = phi(x)
            drive = J @ r''')
s=s.replace('''            drive = J @ r + dtype(c) * (dtype(1.0) - r.mean(0))[None, :]''','''            drive = J @ r
            if c:
                drive += dtype(c) * (dtype(1.0) - r.mean(0))[None, :]''')
s+='''

# ---------------------------------------------------------------- the idealized generative process
# ring/tc.py and ring/fn.py, as spectra.ipynb, spurious_fixed_points.ipynb and
# weight_matrix_analyses.ipynb use them (sigma 1.4211, beta 2.7659, lambda 1e-8).

def nonlin_idealized(x, beta=2.7659):
    """ring/fn.py, nonlin_idealized: 1 + unity_erf(beta x), unity_erf(x) = erf(sqrt(pi) x / 2).
    Keeps the dtype of x."""
    from scipy.special import erf
    return 1 + erf(x * x.dtype.type(np.sqrt(np.pi) / 2 * beta))


def gen_idealized(n, n_theta, rng, scale=1.4211, beta=2.7659):
    """ring/tc.py, gen_tuning_curves_idealized with sample_tcs, from a seeded Generator.
    Returns X, Phi of shape (n_theta, n)."""
    gft = wrapped_gaussian_ft(scale, n_theta)
    nf = len(gft)
    Z = (rng.standard_normal((nf, n)) + 1j * rng.standard_normal((nf, n))) / np.sqrt(2.0)
    Z[0] = Z[0].real * np.sqrt(2.0)
    Xg = np.fft.irfft(Z * np.sqrt(gft)[:, None], axis=0, norm="forward")
    return Xg, nonlin_idealized(Xg, beta)
'''
open('hdring.py','w').write(s)
E
grep -n "def wrapped_gaussian_ft" -A6 hdring.py; grep -n "unity_erf\|def gen_idealized" theory.ipynb | head
```

```
311:def wrapped_gaussian_ft(scale, N_theta=N_THETA, eq_var=1.0):
312-    """ring/tc.py, wrapped_gaussian_cov (Fourier side)."""
313-    n = np.arange(N_theta // 2 + 1)
314-    return (eq_var / np.sqrt(2 * np.pi) / scale) * np.exp(-n ** 2 / (2 * scale ** 2))
315-
316-
317-def sample_z(rng, N_samples, N_freq, dtype=np.float64):
300:    "def unity_erf(x): return erf(np.sqrt(np.pi) * x / 2.0)\n",
301:    "def gen_idealized(n, n_theta, rng):\n",
308:    "    return Xg, 1 + unity_erf(BETA * Xg)\n",
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
s=open('hdring.py').read()
s=s.replace('''            drive = J @ r
            if c:
                drive += dtype(c) * (dtype(1.0) - r.mean(0))[None, :]''','''            drive = J @ r + dtype(c) * (dtype(1.0) - r.mean(0))[None, :]''')
open('hdring.py','w').write(s)
E
cat > $TMPDIR/t_s11.py <<'E'
import time, numpy as np, sys
sys.path.insert(0,'.')
import hdring as H
rng=np.random.default_rng(1)
t=time.time()
X,P=H.gen_idealized(2500,500,rng)
J=H.compute_J(X,P,1e-8)
print('J',time.time()-t, J.shape, X.shape)
x0=rng.standard_normal((2500,170)).astype(np.float32)
t=time.time()
H.simulate(J,x0,T=1.0,dt=0.005,c=0.0,phi=H.nonlin_idealized)
print('200 steps 170 cols',time.time()-t)
x0=rng.standard_normal((2500,34)).astype(np.float32)
t=time.time()
H.simulate(J,x0,T=1.0,dt=0.005,c=0.0,phi=H.nonlin_idealized)
print('200 steps 34 cols',time.time()-t)
E
time ../../executed/clark-2026/.venv/bin/python $TMPDIR/t_s11.py
```

```
J 0.15061473846435547 (2500, 2500) (500, 2500)
200 steps 170 cols 2.2634334564208984
200 steps 34 cols 0.541715145111084

real	0m3.383s
user	0m12.771s
sys	0m0.118s
```

**Agent calls Bash**

```bash
cd  grep -n "def \|parallel\|Pool\|ThreadPool\|--fresh\|timeout" tools/entry.py | head -60
```

```
33:so, without executing anything; --fresh executes all the same.
77:    def __init__(self):
80:    def error(self, where, message: str) -> None:
85:def dataset_id(record: dict) -> str | None:
94:def dataset_ids(record: dict) -> list[str]:
99:def claims_paths() -> list[Path]:
105:def claims_target(data: dict) -> tuple:
110:def lookup(index: dict, attempt: dict):
119:def schema(name: str) -> Draft202012Validator:
130:def _parsed(text: str):
138:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
144:def load(report: Report, path: Path):
152:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
161:def _plain(value):
172:def code_of(notebook_path: Path) -> str:
179:def check(entry_dir: Path) -> Report:
467:def _local_data(code: str, start: int) -> bool:
480:def _derivation_checks(report: Report, where, code: str) -> None:
499:def python_of(entry_dir: Path) -> str:
513:def set_python(entry_dir: Path, version: str) -> None:
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 625,682p tools/entry.py
```

```
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo/notebooks && python - <<'E'
import json
d=json.load(open('weight_matrix_analyses.ipynb'))
s=''.join(d['cells'][19]['source']); i=s.find('def _solve_q'); print(s[i:])
for c in d['cells'][15:19]:
    if c['cell_type']=='markdown': print(''.join(c['source']))
E
```

```
def _solve_q(target):
    lo, hi = 0., 1.
    while _E_phi_prime(hi) > target:
        hi *= 2
    for _ in range(200):
        mid = .5 * (lo + hi)
        lo, hi = (mid, hi) if _E_phi_prime(mid) > target else (lo, mid)
    return .5 * (lo + hi)

pred_radius = np.array([np.sqrt(_solve_q(1. / sd ** 2)) / (np.sqrt(D_mix) * sd ** 2)
                        for sd in doublet_std])
print("predicted ring radii (normalized kappa):", np.round(pred_radius, 4))
for d in range(D_mix):
    fin = all_kappas_mix[d][-1]
    r = np.linalg.norm(fin, axis=0)
    drift = np.angle(np.exp(1j * (np.arctan2(fin[1], fin[0]) - angle0_mix[d])))
    print(f"  doublet {d + 1}: radius {r.mean():.4f} +/- {r.std():.4f}, "
          f"|angle drift| <= {np.abs(drift).max():.4f} rad")

## Supplementary Figure S1: low-rank comparison model
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/s1.py <<'E'
import time, numpy as np, sys
sys.path.insert(0,'entries/clark-2026')
import hdring as H
T0=time.time()
N, K = 10000, 4
STD = np.array([10., 5.])
def gaussian_net(rng):
    M = rng.standard_normal((N, 4)) * np.repeat(STD, 2)[None, :]
    return M
def mixture_net(rng):
    group = rng.integers(0, 2, size=N); z = rng.standard_normal((N, 2))
    M = np.zeros((N, 4)); comp = np.sqrt(2) * STD
    for d in range(2):
        M[group == d, 2*d:2*d+2] = comp[d] * z[group == d]
    return M
def eig_lowrank(M):
    return np.sort(np.linalg.eigvalsh(M.T @ M / N))[::-1]
def run_gauss(M, rng, r0=5.0, n_init=40, dt=0.1, T=10):
    even = np.arange(n_init) * 2*np.pi / n_init
    ang0 = np.stack([even, rng.permutation(even)])
    sub = [M[:, 2*d:2*d+2] / np.std(M[:, 2*d:2*d+2], axis=0) for d in range(2)]
    x = sum(r0 * sub[d] @ np.array([np.cos(ang0[d]), np.sin(ang0[d])]) for d in range(2))
    for i in range(1, int(T/dt)):
        x = (1-dt)*x + dt*(M @ (M.T @ np.tanh(x)) / N)
    P = np.tanh(x)
    kap = [(M[:, 2*d:2*d+2].T @ P) / N / np.std(M[:, 2*d:2*d+2], axis=0)[:, None] for d in range(2)]
    return kap, ang0
def run_mix(M, rng, r0=0.45, n_init=40, dt=0.1, T=10):
    even = np.arange(n_init) * 2*np.pi / n_init
    ang0 = np.stack([even, rng.permutation(even)])
    sc = np.repeat([np.std(M[:, 2*d:2*d+2]) for d in range(2)], 2)
    kap0 = np.zeros((4, n_init))
    for d in range(2):
        kap0[2*d] = r0*np.cos(ang0[d]); kap0[2*d+1] = r0*np.sin(ang0[d])
    x = (M / sc[None, :]) @ kap0
    for i in range(int(T/dt)):
        P = np.tanh(x)
        traj = (M.T @ P) / N / sc[:, None]
        x = (1-dt)*x + dt*(M @ (M.T @ P) / N)
    return [traj[2*d:2*d+2] for d in range(2)], ang0
def ring_stats(kap, ang0):
    r = np.linalg.norm(kap, axis=0); a = np.arctan2(kap[1], kap[0]) % (2*np.pi)
    s = np.sort(a); gap = np.diff(np.r_[s, s[0] + 2*np.pi]).max()
    drift = np.abs(np.angle(np.exp(1j*(a - ang0))))
    return dict(r_med=np.median(r), r_cv=r.std()/r.mean(), gap=gap, drift=drift.max())
sd = H.seed("figs1-s2-spectrum-does-not-fix-symmetry")
for k in range(5):
    s=sd+1000*k
    Mg = gaussian_net(np.random.default_rng(s)); Mm = mixture_net(np.random.default_rng(s+1))
    eg, em = eig_lowrank(Mg), eig_lowrank(Mm)
    kg, ag = run_gauss(Mg, np.random.default_rng(s+2)); km, am = run_mix(Mm, np.random.default_rng(s+3))
    print(s, eg.round(2), em.round(2), (np.abs(eg-em)/eg).max().round(4))
    for lab,kk,aa in (('gauss',kg,ag),('mix',km,am)):
        print('  ',lab,[{q:round(float(v),4) for q,v in ring_stats(kk[d],aa[d]).items()} for d in range(2)])
print(time.time()-T0)
E
cd  time executed/clark-2026/.venv/bin/python $TMPDIR/dev/s1.py
```

```
4129464829 [102.72  97.48  25.4   24.7 ] [97.4  96.55 25.97 25.79] 0.0518
   gauss [{'r_med': 0.8011, 'r_cv': 0.0059, 'gap': 0.3591, 'drift': 0.3757}, {'r_med': 0.0121, 'r_cv': 0.3135, 'gap': 1.2202, 'drift': 3.0798}]
   mix [{'r_med': 0.5587, 'r_cv': 0.0063, 'gap': 0.3752, 'drift': 0.3123}, {'r_med': 0.5711, 'r_cv': 0.0029, 'gap': 0.3813, 'drift': 0.2391}]
4129465829 [102.18  98.28  25.25  24.54] [99.72 96.02 25.81 24.23] 0.0241
   gauss [{'r_med': 0.794, 'r_cv': 0.0057, 'gap': 0.4517, 'drift': 0.3075}, {'r_med': 0.0116, 'r_cv': 0.4205, 'gap': 0.611, 'drift': 2.9522}]
   mix [{'r_med': 0.5682, 'r_cv': 0.0072, 'gap': 0.5578, 'drift': 0.3679}, {'r_med': 0.5676, 'r_cv': 0.0094, 'gap': 0.5454, 'drift': 0.4063}]
4129466829 [100.09  96.91  24.87  23.97] [101.72  99.25  26.15  23.87] 0.0512
   gauss [{'r_med': 0.8, 'r_cv': 0.0035, 'gap': 0.315, 'drift': 0.1553}, {'r_med': 0.0206, 'r_cv': 0.2413, 'gap': 0.5689, 'drift': 3.1173}]
   mix [{'r_med': 0.5699, 'r_cv': 0.0071, 'gap': 0.5521, 'drift': 0.4332}, {'r_med': 0.573, 'r_cv': 0.0153, 'gap': 0.4384, 'drift': 0.6522}]
4129467829 [100.63  98.49  25.39  24.81] [104.18  96.99  25.64  24.32] 0.0352
   gauss [{'r_med': 0.7998, 'r_cv': 0.0022, 'gap': 0.3247, 'drift': 0.2395}, {'r_med': 0.0138, 'r_cv': 0.3851, 'gap': 0.6668, 'drift': 3.0766}]
   mix [{'r_med': 0.5728, 'r_cv': 0.0107, 'gap': 0.5175, 'drift': 0.5353}, {'r_med': 0.566, 'r_cv': 0.0066, 'gap': 0.4921, 'drift': 0.416}]
4129468829 [99.92 98.74 25.73 24.69] [104.24 100.24  24.39  23.96] 0.0522
   gauss [{'r_med': 0.7985, 'r_cv': 0.0022, 'gap': 0.3534, 'drift': 0.1868}, {'r_med': 0.0239, 'r_cv': 0.4321, 'gap': 1.5967, 'drift': 3.0974}]
   mix [{'r_med': 0.5689, 'r_cv': 0.0067, 'gap': 0.4779, 'drift': 0.3467}, {'r_med': 0.5621, 'r_cv': 0.0067, 'gap': 0.5612, 'drift': 0.3894}]
2.199493169784546

real	0m2.597s
user	0m8.361s
sys	0m1.481s
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/s11.py <<'E'
import time, numpy as np, sys
sys.path.insert(0,'entries/clark-2026')
import hdring as H
T0=time.time()
STDS = (1, 10, 50, 100, 1000)
def model_net(n, rng):
    X, P = H.gen_idealized(n, 500, rng)
    return X, P, H.compute_J(X, P, 1e-8)
def dist(P32, Psq, xf):
    return H.nearest_target(P32, H.nonlin_idealized(xf.astype(np.float32)), Psq)
def reference(X, P32, Psq, J, rng, T=30.0):
    n = X.shape[1]
    x0 = X[::5].T + rng.standard_normal((n, 100)) * 3.0
    rec = {}
    def on_save(t, x):
        if abs(t - 20.0) < 1e-6 or t == 0.0: rec[round(t)] = dist(P32, Psq, x)[1]
    xf = H.simulate(J, x0, T=T, dt=0.005, c=0.0, phi=H.nonlin_idealized, save_every=0.1, on_save=on_save)
    return rec, dist(P32, Psq, xf)[1]
sd = H.seed("figs11-s12-global-stability-model")
for k in range(1):
    s = sd + 1000*k
    t=time.time()
    X, P, J = model_net(2500, np.random.default_rng(s))
    P32 = P.astype(np.float32); Psq = (P32**2).sum(1)
    rec, dfin = reference(X, P32, Psq, J, np.random.default_rng(s+1))
    thr = rec[20].max()
    print('ref', rec[0].min(), np.median(rec[0]), 'at 20', np.median(rec[20]), thr, 'final', np.median(dfin), dfin.max(), time.time()-t)
    rng = np.random.default_rng(s+2)
    x0 = np.concatenate([rng.standard_normal((2500, 34)) * sv for sv in STDS], axis=1)
    xf = H.simulate(J, x0, T=30.0, dt=0.005, c=0.0, phi=H.nonlin_idealized)
    idx, d = dist(P32, Psq, xf); _, d0 = dist(P32, Psq, x0.astype(np.float32))
    for q, sv in enumerate(STDS):
        sl = slice(34*q, 34*q+34)
        print(sv, 'init med', np.median(d0[sl]).round(3), 'final med', np.median(d[sl]), 'max', d[sl].max(), 'within', np.mean(d[sl] <= thr), 'states', H.count_states(idx[sl], 500, 10), 'finite', np.isfinite(xf[:, sl]).all())
    print(time.time()-t)
    for n in (50, 100, 250, 500, 1000):
        rng = np.random.default_rng(s + 3)
        Xn, Pn, Jn = model_net(n, rng)
        Pn32 = Pn.astype(np.float32); Pnsq = (Pn32**2).sum(1)
        th_idx = (np.arange(34) * 500 / 34).round().astype(int)
        x0 = Xn[th_idx].T + rng.standard_normal((n, 34)) * 0.1 * np.sqrt(n)
        xf = H.simulate(Jn, x0, T=30.0, dt=0.005, c=0.0, phi=H.nonlin_idealized)
        idx, d = dist(Pn32, Pnsq, xf); _, d0 = dist(Pn32, Pnsq, x0.astype(np.float32))
        recn, _ = reference(Xn, Pn32, Pnsq, Jn, np.random.default_rng(s + 4))
        print(n, 'init med', np.median(d0).round(3), 'final med', np.median(d).round(5), 'max', d.max().round(5), 'within N2500 thr', np.mean(d <= thr), 'within own', np.mean(d <= recn[20].max()), 'own thr', recn[20].max().round(5), 'states', H.count_states(idx, 500, 10))
    print(time.time()-t)
E
cd  time executed/clark-2026/.venv/bin/python $TMPDIR/dev/s11.py
```

```
ref 1.099209342215126 1.1282625999881837 at 20 0.005442582243714874 0.01120589466700465 final 0.005595580220711377 0.011026724173252926 37.889583110809326
1 init med 1.207 final med 0.005031705084515956 max 0.009995891090587603 within 1.0 states {'single': 18, 'greedy': 22, 'bins': 27} finite True
10 init med 1.293 final med 0.005687264830298804 max 0.011458874472620369 within 0.9705882352941176 states {'single': 13, 'greedy': 16, 'bins': 18} finite True
50 init med 1.301 final med 0.006111971749289485 max 0.010994831779622056 within 1.0 states {'single': 14, 'greedy': 17, 'bins': 20} finite True
100 init med 1.299 final med 0.004596901013279142 max 0.010576121336200789 within 1.0 states {'single': 20, 'greedy': 23, 'bins': 25} finite True
1000 init med 1.304 final med 0.005041084753346624 max 0.010975155815855007 within 1.0 states {'single': 13, 'greedy': 18, 'bins': 21} finite True
109.89731788635254
50 init med 0.631 final med 0.46424 max 0.83559 within N2500 thr 0.23529411764705882 within own 1.0 own thr 0.8963 states {'single': 10, 'greedy': 12, 'bins': 13}
100 init med 0.805 final med 0.00416 max 0.01 within N2500 thr 1.0 within own 1.0 own thr 0.01263 states {'single': 16, 'greedy': 17, 'bins': 20}
250 init med 0.962 final med 0.00575 max 0.46411 within N2500 thr 0.8823529411764706 within own 0.9411764705882353 own thr 0.46411 states {'single': 14, 'greedy': 18, 'bins': 22}
500 init med 1.058 final med 0.00615 max 0.01166 within N2500 thr 0.9705882352941176 within own 1.0 own thr 0.03267 states {'single': 18, 'greedy': 20, 'bins': 22}
1000 init med 1.127 final med 0.00542 max 0.01038 within N2500 thr 1.0 within own 1.0 own thr 0.01137 states {'single': 22, 'greedy': 22, 'bins': 27}
136.29116940498352

real	2m16.712s
user	8m59.770s
sys	0m0.190s
```

**Agent calls Bash**

```bash
cd entries/clark-2026; grep -n "class DMFTModel\|def __init__\|self.J =\|self.J=" ring_dmft.py | head; grep -n "import" ring_dmft.py | head
```

```
47:class DMFTModel:
90:    def __init__(self, N_theta=1000, scale=1.5, g=2.0, lamda=1e-12):
151:        self.J = np.fft.irfft(self.J_ft, norm='forward')
3:used by the attempt clark-2026 for the mean-field claims. The only changes: the imports of
4:ring.fn and ring.tc (which import torch) are replaced by their numpy functions, defined below,
24:import numpy as np
25:from scipy.linalg import circulant
26:from scipy.special import erf
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/s10.py <<'E'
import time, numpy as np, sys
sys.path.insert(0,'entries/clark-2026')
import hdring as H, ring_dmft as D, scipy.linalg
N, NT, NI = 2500, 500, 34
sd = H.seed("figs10-robustness-comparable")
rng = np.random.default_rng(sd)
X, P = H.gen_idealized(N, NT, rng)
J = H.compute_J(X, P, 1e-8)
row = D.DMFTModel(N_theta=N, scale=1.4211, g=2.7659).J - 1
Jc = scipy.linalg.circulant(row); Jc *= (1.0 / Jc[0, 0]) * (10.0 / N)
n = np.arange(N); n = np.minimum(n, N - n)
pat = 4 * np.exp(-(n / (0.15 * N)) ** 2) - 2
x_circ = np.array([np.roll(pat, r) for r in (np.arange(NI) * N / NI).round().astype(int)]).T
x_dis = X[(np.arange(NI) * NT / NI).round().astype(int)].T
def add_noise(x, f, rng): return x + rng.standard_normal(x.shape) * f * x.std(0, keepdims=True)
r2 = np.random.default_rng(sd + 1)
x0d, x0c = add_noise(x_dis, 0.025, r2), add_noise(x_circ, 0.025, r2)
print(Jc[0,:3], J.std(), Jc.std())
def theta(xf, lab):
    if lab == "disordered":
        m = P @ H.nonlin_idealized(xf.astype(np.float64)) / N
        return m.argmax(0), NT
    return xf.argmax(0), N
for f in (0.0, 0.4):
    for lab, Jb, x0 in (("disordered", J, x0d), ("circ", Jc, x0c)):
        t = time.time()
        Jn = Jb + np.random.default_rng(sd + 2).standard_normal(Jb.shape) * f * Jb.std()
        xi, nn = theta(x0, lab)
        xf = H.simulate(Jn, x0, T=12.0, dt=0.005, c=0.0, phi=H.nonlin_idealized)
        ti, nn = theta(xf, lab)
        drift = np.abs(((ti - xi) / nn * 2*np.pi + np.pi) % (2*np.pi) - np.pi)
        print(f, lab, H.count_states(ti, nn, nn / 50), 'median drift', np.median(drift).round(3), time.time() - t)
E
cd  time executed/clark-2026/.venv/bin/python $TMPDIR/dev/s10.py
```

```
[0.004      0.00399992 0.00399967] 0.0012205531181284706 0.0016001832780260855
0.0 disordered {'single': 34, 'greedy': 34, 'bins': 34} median drift 0.0 6.369560241699219
0.0 circ {'single': 34, 'greedy': 34, 'bins': 34} median drift 0.025 6.579349994659424
0.4 disordered {'single': 20, 'greedy': 22, 'bins': 27} median drift 0.069 6.296101093292236
0.4 circ {'single': 23, 'greedy': 23, 'bins': 24} median drift 0.113 6.434888124465942

real	0m26.249s
user	1m43.434s
sys	0m0.162s
```

**Agent calls Bash**

```bash
date -u; cd entries/clark-2026; python -c "
import json;d=json.load(open('theory.ipynb'))
for i in [0,1,3,19,20]: print('---',i);print(''.join(d['cells'][i]['source']))"
```

```
Thu Nov 26 17:02:35 UTC 2026
--- 0
# Clark, Abbott & Sompolinsky (2026): the mean-field theory and the large-N spectra

Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. Dataset.
DANDI:000939 at version 0.240528.1542, the version the paper cites (see
`tuning_curves.ipynb`).

These claims are on the paper's theory and simulations (`data: elsewhere`, the paper's code at
commit 245726f), except `fig7c-dmft-integrates-behavior`, which drives the mean-field equations
with the head direction of mouse A3707 from the dataset. The mean-field code is a copy of the
paper's `ring/dmft.py` (`ring_dmft.py` in this entry, MIT licence, imports of torch removed).

| claim | data | tested here |
|---|---|---|
| fig7-dmft-mexican-hat-and-stability | elsewhere | yes |
| fig7de-dmft-timescales | elsewhere | yes |
| fig7c-dmft-integrates-behavior | dataset | yes |
| fig6cd-eigenvalues-real-degenerate | elsewhere | yes |
| fig6fg-disordered-eigenvectors | elsewhere | yes |
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 179,300p tools/entry.py | grep -n "sanity\|claim:\|Result\|error(" | head -40
```

```
8:        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")
13:        report.error(rel / name, "notebook is not listed in entry.yaml")
15:        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
19:            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")
23:        report.error(rel, "no requirements.in")
25:        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
29:            report.error(rel / "requirements.lock.txt", f"locked for Python {locked_for.group(1)}, but entry.yaml "
36:                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")
47:            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
50:                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
57:            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
58:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
59:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
63:                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
66:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
88:                    report.error(path.relative_to(ROOT), f"claim {c['id']!r} depends on {other!r}, which is not in the file")
102:                report.error(where, f"dataset {used.get('id')} version {version!r} differs from {pinned!r} in entry.yaml")
108:                report.error(where, f"reconciliation: no attempt record {rec.get('earlier')!r}")
113:                    report.error(where, f"reconciliation: give each of the {n_then} findings of "
118:                        report.error(where
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/build_model.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
C = []
def md(s): C.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)
md(r"""
# Clark, Abbott & Sompolinsky (2026): the simulations of the generative-process and rank-four networks

Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. Dataset.
DANDI:000939 at version 0.240528.1542, the version the paper cites (see `tuning_curves.ipynb`).

These three claims use no recorded data (`data: elsewhere`): each runs a notebook of the
paper's code at commit 245726f, repeated here in numpy (`hdring.py`). The networks are built
from the idealized generative process (`ring/tc.py`, `gen_tuning_curves_idealized`; sigma
1.4211, beta 2.7659, 500 angles, lambda 1e-8) or from random rank-four loadings. Every random
draw comes from the claim's seed; the paper's notebooks use numpy seeds 42 and 123.

| claim | data | tested here |
|---|---|---|
| figs1-s2-spectrum-does-not-fix-symmetry | elsewhere | yes |
| figs11-s12-global-stability-model | elsewhere | yes |
| figs10-robustness-comparable | elsewhere | yes |
| fig8-grid-scores-and-torus | elsewhere | no, blocked (too large) |
""")
code(r"""
import os, time, resource
import numpy as np
import pandas as pd
import scipy.linalg
import hdring as H
import ring_dmft as D

T0 = time.time()
SCALE, BETA, N_THETA, LAMDA = 1.4211, 2.7659, 500, 1e-8
""")
code(r"""
# The generative-process network of 2,500 neurons under the seed of figs11-s12, as the check of
# what the simulations below are built from (no recorded data enter this notebook).
sd11 = H.seed("figs11-s12-global-stability-model")
X25, P25 = H.gen_idealized(2500, N_THETA, np.random.default_rng(sd11), SCALE, BETA)
J25 = H.compute_J(X25, P25, LAMDA)
print("X, Phi", X25.shape, "| J", J25.shape, "| diagonal of J zero:", bool(np.allclose(np.diag(J25), 0)))
print(f"input currents: mean {X25.mean():.3f}, sd {X25.std():.3f} (the process has unit variance); "
      f"firing rates range {P25.min():.3f} to {P25.max():.3f} (1 + erf, bounded by 0 and 2)")
print(f"reconstruction error mean((X - Phi J^T)^2) {np.mean((X25 - P25 @ J25.T) ** 2):.3e}")
""", ["sanity"])

md(r"""
## figs1-s2-spectrum-does-not-fix-symmetry

> Eigenvalue degeneracy suggests but does not fix the symmetry group, since ensembles matching
> the model's second-order statistics, and hence its spectrum, can differ beyond second order and
> give different symmetry groups and attractors (a single ring for Gaussian loadings, the full
> torus for mixture-of-Gaussians loadings, in a rank-four network).

As `weight_matrix_analyses.ipynb`, cells 16 and 19: N 10,000, J = M M^T / N, loading standard
deviations 10 and 5 for the two doublets; the mixture gives each neuron one doublet with
standard deviation sqrt(2) times as large, so that the second moments are the same. Dynamics x <-
(1 - dt) x + dt J tanh(x), dt 0.1 for 10 tau, 40 initial conditions with evenly spaced angles in
both doublets, permuted independently (amplitude 5 for the Gaussian, 0.45 in kappa units for the
mixture). J tanh(x) is computed as M (M^T tanh(x)) / N, the same product. The nonzero eigenvalues of
J = M M^T / N are those of the 4 by 4 matrix M^T M / N, which is how they are computed.

Measures (the claims file fixes collapse; the rest are standard choices). kappa in units of the
loading standard deviation, as the paper's notebook. A doublet forms a ring when its 40 final radii
vary by less than 10% (coefficient of variation) and their angles leave no gap wider than 2 pi /
10; it collapses when its median final radius is below one tenth of the ring radius of the
dominant doublet.
""")
code(r"""
N1, STD1 = 10000, np.array([10., 5.])
def gaussian_M(draw):
    return draw((N1, 4)) * np.repeat(STD1, 2)[None, :]
def mixture_M(group, z):
    M = np.zeros((N1, 4)); comp = np.sqrt(2) * STD1
    for d in range(2):
        M[group == d, 2 * d:2 * d + 2] = comp[d] * z[group == d]
    return M
def eig_lowrank(M):
    return np.sort(np.linalg.eigvalsh(M.T @ M / N1))[::-1]
def run_gauss(M, perm, r0=5.0, n_init=40, dt=0.1, T=10):
    even = np.arange(n_init) * 2 * np.pi / n_init
    ang0 = np.stack([even, perm(even)])
    sub = [M[:, 2 * d:2 * d + 2] / np.std(M[:, 2 * d:2 * d + 2], axis=0) for d in range(2)]
    x = sum(r0 * sub[d] @ np.array([np.cos(ang0[d]), np.sin(ang0[d])]) for d in range(2))
    for i in range(1, int(T / dt)):
        x = (1 - dt) * x + dt * (M @ (M.T @ np.tanh(x)) / N1)
    P = np.tanh(x)
    return [(M[:, 2 * d:2 * d + 2].T @ P) / N1 / np.std(M[:, 2 * d:2 * d + 2], axis=0)[:, None] for d in range(2)], ang0
def run_mix(M, perm, r0=0.45, n_init=40, dt=0.1, T=10):
    even = np.arange(n_init) * 2 * np.pi / n_init
    ang0 = np.stack([even, perm(even)])
    sc = np.repeat([np.std(M[:, 2 * d:2 * d + 2]) for d in range(2)], 2)
    kap0 = np.zeros((4, n_init))
    for d in range(2):
        kap0[2 * d] = r0 * np.cos(ang0[d]); kap0[2 * d + 1] = r0 * np.sin(ang0[d])
    x = (M / sc[None, :]) @ kap0
    for i in range(int(T / dt)):
        P = np.tanh(x)
        traj = (M.T @ P) / N1 / sc[:, None]     # kappa before the step, as the paper's loop
        x = (1 - dt) * x + dt * (M @ (M.T @ P) / N1)
    return [traj[2 * d:2 * d + 2] for d in range(2)], ang0
def ring_stats(kap, ang0):
    r = np.linalg.norm(kap, axis=0); a = np.arctan2(kap[1], kap[0]) % (2 * np.pi)
    s = np.sort(a); gap = np.diff(np.r_[s, s[0] + 2 * np.pi]).max()
    drift = np.abs(np.angle(np.exp(1j * (a - ang0))))
    return dict(radius=np.median(r), cv=r.std() / r.mean(), gap=gap, drift_max=drift.max(),
                ring=bool(r.std() / r.mean() < 0.1 and gap < 2 * np.pi / 10))
def judge_s1(eg, em, kg, ag, km, am):
    rel = np.abs(eg - em) / eg
    g = [ring_stats(kg[d], ag[d]) for d in range(2)]; m = [ring_stats(km[d], am[d]) for d in range(2)]
    g_collapse = g[1]["radius"] < 0.1 * g[0]["radius"]
    m_collapse = min(m[0]["radius"], m[1]["radius"]) < 0.1 * max(m[0]["radius"], m[1]["radius"])
    dyn = g[0]["ring"] and g_collapse and m[0]["ring"] and m[1]["ring"] and not m_collapse
    return rel, g, m, g_collapse, m_collapse, dyn
sd1 = H.seed("figs1-s2-spectrum-does-not-fix-symmetry")
t = time.time()
rows = []
for k in range(5):
    s = sd1 + 1000 * k
    rg = np.random.default_rng(s); rm = np.random.default_rng(s + 1)
    Mg = gaussian_M(rg.standard_normal)
    Mm = mixture_M(rm.integers(0, 2, size=N1), rm.standard_normal((N1, 2)))
    eg, em = eig_lowrank(Mg), eig_lowrank(Mm)
    kg, ag = run_gauss(Mg, np.random.default_rng(s + 2).permutation)
    km, am = run_mix(Mm, np.random.default_rng(s + 3).permutation)
    rel, g, m, gc, mc, dyn = judge_s1(eg, em, kg, ag, km, am)
    rows.append(dict(seed=s, eig_gauss=eg.round(2).tolist(), eig_mix=em.round(2).tolist(), max_rel_diff=round(float(rel.max()), 4),
                     within_5pct=bool(rel.max() <= 0.05), dynamics_as_described=dyn))
    print(f"seed {s}: Gaussian doublet 1 radius {g[0]['radius']:.4f} (cv {g[0]['cv']:.4f}, largest angle gap {g[0]['gap']:.3f}), "
          f"doublet 2 radius {g[1]['radius']:.4f} (collapse {gc}); mixture radii {m[0]['radius']:.4f} (cv {m[0]['cv']:.4f}, gap {m[0]['gap']:.3f}) "
          f"and {m[1]['radius']:.4f} (cv {m[1]['cv']:.4f}, gap {m[1]['gap']:.3f}), rings {m[0]['ring']} {m[1]['ring']}; "
          f"mixture angle drift at most {m[0]['drift_max']:.3f} and {m[1]['drift_max']:.3f} rad")
    if k == 0:
        K0 = (kg, km)
print(pd.DataFrame(rows).to_string(index=False))
print("population eigenvalues (the second moments both ensembles share): 100, 100, 25, 25")
# variant: the paper's own realization, numpy's legacy generator with seed 42 as the notebook seeds it
rs = np.random.RandomState(42); Mg42 = rs.randn(N1, 4) * np.repeat(STD1, 2)[None, :]
rs = np.random.RandomState(42); Mm42 = mixture_M(rs.randint(0, 2, size=N1), rs.randn(N1, 2))
eg42, em42 = eig_lowrank(Mg42), eig_lowrank(Mm42)
print("variant, the paper's seed-42 matrices: Gaussian", eg42.round(2), "| mixture", em42.round(2),
      "| largest relative difference", (np.abs(eg42 - em42) / eg42).max().round(4))
# the mean-field ring radii the paper's notebook prints for the mixture (cell 19)
_z = np.linspace(-30., 30., 200001)
def _E_phi_prime(q):
    w = np.exp(-_z ** 2 / (2 * q)) / np.sqrt(2 * np.pi * q)
    return np.trapezoid((1. - np.tanh(_z) ** 2) * w, _z)
def _solve_q(target):
    lo, hi = 0., 1.
    while _E_phi_prime(hi) > target:
        hi *= 2
    for _ in range(200):
        mid = .5 * (lo + hi)
        lo, hi = (mid, hi) if _E_phi_prime(mid) > target else (lo, mid)
    return .5 * (lo + hi)
print("predicted mixture ring radii (paper's notebook prints 0.5642 0.5636 for its own realization):",
      np.round([np.sqrt(_solve_q(1. / sd ** 2)) / (np.sqrt(2) * sd ** 2) for sd in STD1], 4))
print(f"time {time.time()-t:.0f} s")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 4, figsize=(10, 2.5))
for a_, kap, lab in zip(ax, [K0[0][0], K0[0][1], K0[1][0], K0[1][1]], ["Gaussian, doublet 1", "Gaussian, doublet 2", "mixture, doublet 1", "mixture, doublet 2"]):
    a_.scatter(kap[0], kap[1], s=4); a_.set_xlim(-1, 1); a_.set_ylim(-1, 1); a_.set_aspect(1); a_.set_title(lab, fontsize=8)
plt.tight_layout(); plt.show()
print("final kappa range:", min(float(np.abs(k).max()) for k in K0[0] + K0[1]).__round__(3), "to", max(float(np.abs(k).max()) for k in K0[0] + K0[1]).__round__(3), "(axes -1 to 1)")
""", ["claim:figs1-s2-spectrum-does-not-fix-symmetry"])
md(r"""**Result: RESULT_S1**""")

md(r"""
## figs11-s12-global-stability-model

> In the generative-process network of 2,500 neurons, initial conditions far from the manifold
> converge to it with no spurious attractors, and with growing N the dynamics approach the
> mean-field behaviour, reliably converging to a ring by N = 1,000.

As `spurious_fixed_points.ipynb`: N 2,500, 500 angles, lambda 1e-8, nonlinearity 1 + erf, no
uniform inhibition, tau 50 ms, Euler step 5 ms, 30 s; 34 initial states i.i.d. Gaussian with
standard deviation 1, 10, 50, 100 and 1,000 (Supplementary Fig. 11a); and for N 50, 100, 250,
500 and 1,000, the 34 regularly spaced manifold points plus noise of standard deviation 0.1
sqrt(N) (Supplementary Fig. 12). The distance to the manifold is the distance of the firing rates to
the nearest of the 500 target points, over sqrt(N), as in `figs11b-data-network-global-stability`.

The criterion judges "as in figs11b", whose threshold is the largest distance at 20 s of the
fig2ef protocol. For this network that protocol is run on the network itself (assumption): the 100
regularly spaced manifold points plus noise of standard deviation 3, with the same step (5 ms),
and the largest distance at 20 s is the threshold. For Supplementary Fig. 12 the threshold is that
of the 2,500-neuron network, a fixed normalized distance (assumption); the threshold of each N's own
reference run is shown as a variant. On the manifold means at least 95% of final states within the
threshold, as in figs11b.
""")
code(r"""
STDS = (1, 10, 50, 100, 1000)
def model_net(n, rng):
    X, P = H.gen_idealized(n, N_THETA, rng, SCALE, BETA)
    return X, P, H.compute_J(X, P, LAMDA)
def dist_to(P32, Psq, x):
    return H.nearest_target(P32, H.nonlin_idealized(x.astype(np.float32), BETA), Psq)
def reference_run(X, P32, Psq, J, rng):
    # the fig2ef protocol on this network: 100 regularly spaced manifold points plus noise sd 3
    n = X.shape[1]
    x0 = X[::N_THETA // 100].T + rng.standard_normal((n, 100)) * 3.0
    rec = {}
    def on_save(tt, x):
        if abs(tt - 20.0) < 1e-6 or tt == 0.0:
            rec[round(tt)] = dist_to(P32, Psq, x)[1]
    xf = H.simulate(J, x0, T=30.0, dt=0.005, c=0.0, phi=lambda v: H.nonlin_idealized(v, BETA), save_every=0.1, on_save=on_save)
    rec["final"] = dist_to(P32, Psq, xf)[1]
    return rec
def s11a(X, P, J, sd):
    P32 = P.astype(np.float32); Psq = (P32 ** 2).sum(1)
    ref = reference_run(X, P32, Psq, J, np.random.default_rng(sd + 1))
    rng = np.random.default_rng(sd + 2)
    x0 = np.concatenate([rng.standard_normal((X.shape[1], 34)) * sv for sv in STDS], axis=1)
    xf = H.simulate(J, x0, T=30.0, dt=0.005, c=0.0, phi=lambda v: H.nonlin_idealized(v, BETA))
    idx, d = dist_to(P32, Psq, xf); _, d0 = dist_to(P32, Psq, x0)
    out = {sv: dict(init_med=np.median(d0[34 * q:34 * q + 34]), final_med=np.median(d[34 * q:34 * q + 34]), final_max=d[34 * q:34 * q + 34].max(),
                    finite=bool(np.isfinite(xf[:, 34 * q:34 * q + 34]).all()), idx=idx[34 * q:34 * q + 34], d=d[34 * q:34 * q + 34]) for q, sv in enumerate(STDS)}
    return ref, out
t = time.time()
res11 = {}
for k in range(5):
    s = sd11 + 1000 * k
    X, P, J = (X25, P25, J25) if k == 0 else model_net(2500, np.random.default_rng(s))
    ref, out = s11a(X, P, J, s)
    thr = ref[20].max()
    res11[s] = (ref, out, thr)
    print(f"seed {s}: reference (fig2ef protocol) distance at 0 s median {np.median(ref[0]):.3f}, at 20 s median {np.median(ref[20]):.5f}, largest {thr:.5f}, at the end median {np.median(ref['final']):.5f}")
    for sv, o in out.items():
        print(f"   sd {sv}: finite {o['finite']}, distance at the start median {o['init_med']:.3f}, final median {o['final_med']:.5f}, largest {o['final_max']:.5f}, "
              f"within the threshold {np.mean(o['d'] <= thr):.2f}, within 2x {np.mean(o['d'] <= 2 * thr):.2f}; final angles as states {H.count_states(o['idx'], N_THETA, N_THETA / 50)}")
    print(f"   all standard deviations with at least 95% within: {all(np.mean(o['d'] <= thr) >= 0.95 for o in out.values())}", flush=True)
THR25 = res11[sd11][2]
print(f"time {time.time()-t:.0f} s")
""", ["claim:figs11-s12-global-stability-model"])
code(r"""
t = time.time()
rows = []
for k in range(5):
    s = sd11 + 1000 * k
    thr = res11[s][2]
    for n in (50, 100, 250, 500, 1000):
        rng = np.random.default_rng(s + 3 + n)
        Xn, Pn, Jn = model_net(n, rng)
        Pn32 = Pn.astype(np.float32); Pnsq = (Pn32 ** 2).sum(1)
        th_idx = (np.arange(34) * N_THETA / 34).round().astype(int)
        x0 = Xn[th_idx].T + rng.standard_normal((n, 34)) * 0.1 * np.sqrt(n)
        xf = H.simulate(Jn, x0, T=30.0, dt=0.005, c=0.0, phi=lambda v: H.nonlin_idealized(v, BETA))
        idx, d = dist_to(Pn32, Pnsq, xf); _, d0 = dist_to(Pn32, Pnsq, x0)
        own = reference_run(Xn, Pn32, Pnsq, Jn, np.random.default_rng(s + 4 + n))[20].max() if k == 0 else np.nan
        cs = H.count_states(idx, N_THETA, N_THETA / 50)
        rows.append(dict(seed=s, N=n, init_median=round(float(np.median(d0)), 3), final_median=float(np.median(d)), final_max=float(d.max()),
                         within_N2500_threshold=round(float(np.mean(d <= thr)), 2), own_threshold=own,
                         within_own=round(float(np.mean(d <= own)), 2) if k == 0 else np.nan, states_bins=cs["bins"], states_single=cs["single"]))
tab12 = pd.DataFrame(rows)
with pd.option_context("display.float_format", "{:.5f}".format):
    print(tab12.to_string(index=False))
n1000 = tab12[tab12.N == 1000]
print("N 1,000, at least 95% within the 2,500-neuron threshold, by seed:", dict(zip(n1000.seed, n1000.within_N2500_threshold >= 0.95)))
print(f"time {time.time()-t:.0f} s")
""", ["claim:figs11-s12-global-stability-model"])
md(r"""**Result: RESULT_S11**""")

md(r"""
## figs10-robustness-comparable

> Under added weight noise the disordered network and a circulant network with proportional
> eigenvalues fragment into discrete states alike, so the two are comparably robust.

As `weight_matrix_analyses.ipynb`, cell 10: the generative-process network (N 2,500, 500 angles,
lambda 1e-8) and the circulant network built from the mean-field interaction profile
(`DMFTModel(N_theta=2500).J - 1`, scaled so that its diagonal is 10 / N); weight noise of standard
deviation f times the matrix's standard deviation, f 0, 0.2, 0.4, 0.6, 0.8 and 1.0; 34 initial
conditions (regularly spaced manifold points for the disordered network, shifted Gaussian bumps
for the circulant one) with noise of 0.025 times each state's standard deviation; 120 s, step 5
ms, no uniform inhibition. The encoded angle is the argmax of the overlap m (disordered) or of
the input currents (circulant), as the notebook's `theta_max`.

Final angles are merged into states as in `fig2gi-circulant-noise-collapses` (within 2 pi / 50).
The criterion does not say how many states make a continuum among 34 initial conditions spaced 2 pi
/ 34 apart; a network keeps a continuum here when at least 31 (90%) remain distinct under all three
merging readings (assumption).
""")
code(r"""
NW, NI = 2500, 34
F_W = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
row = D.DMFTModel(N_theta=NW, scale=SCALE, g=BETA).J - 1
J_circ = scipy.linalg.circulant(row); J_circ *= (1.0 / J_circ[0, 0]) * (10.0 / NW)
nn_ = np.arange(NW); nn_ = np.minimum(nn_, NW - nn_)
pat = 4 * np.exp(-(nn_ / (0.15 * NW)) ** 2) - 2
x_circ = np.array([np.roll(pat, r) for r in (np.arange(NI) * NW / NI).round().astype(int)]).T
def setup10(s):
    X, P = H.gen_idealized(NW, N_THETA, np.random.default_rng(s), SCALE, BETA)
    J = H.compute_J(X, P, LAMDA)
    x_dis = X[(np.arange(NI) * N_THETA / NI).round().astype(int)].T
    r2 = np.random.default_rng(s + 1)
    noisy = lambda x: x + r2.standard_normal(x.shape) * 0.025 * x.std(0, keepdims=True)
    return X, P, J, noisy(x_dis), noisy(x_circ)
def angle_of(x, lab, P):
    if lab == "disordered":
        return (P @ H.nonlin_idealized(x.astype(np.float64), BETA) / NW).argmax(0), N_THETA
    return x.argmax(0), NW
def run10(Jb, x0, f, lab, P, rng):
    Jn = Jb + rng.standard_normal(Jb.shape) * f * Jb.std()
    rec = {}
    def on_save(tt, x):
        if round(tt, 3) % 30 == 0:
            rec[round(tt)] = angle_of(x, lab, P)[0]
    xf = H.simulate(Jn, x0, T=120.0, dt=0.005, c=0.0, phi=lambda v: H.nonlin_idealized(v, BETA), save_every=30.0, on_save=on_save)
    a, n = angle_of(xf, lab, P)
    rec["final"] = a
    return rec, n
def summarize10(rec, n):
    cs = H.count_states(rec["final"], n, n / 50)
    drift = np.abs(((rec["final"] - rec[0]) / n * 2 * np.pi + np.pi) % (2 * np.pi) - np.pi)
    return cs, float(np.median(drift)), float(drift.max())
sd10 = H.seed("figs10-robustness-comparable")
t = time.time()
X10, P10, J10, x0d, x0c = setup10(sd10)
rw = np.random.default_rng(sd10 + 2)
rows = []
for f in F_W:
    for lab, Jb, x0 in (("disordered", J10, x0d), ("circulant", J_circ, x0c)):
        rec, n = run10(Jb, x0, f, lab, P10, rw)
        cs, dmed, dmax = summarize10(rec, n)
        st_t = {tt: H.count_states(rec[tt], n, n / 50)["bins"] for tt in (30, 60, 90)}
        rows.append(dict(f_w=f, network=lab, single=cs["single"], greedy=cs["greedy"], bins=cs["bins"], bins_at_30_60_90s=list(st_t.values()),
                         median_drift_rad=round(dmed, 3), max_drift_rad=round(dmax, 3), continuum=min(cs.values()) >= 31))
    print(f"f_w {f} done at {time.time()-t:.0f} s", flush=True)
tab10 = pd.DataFrame(rows)
print(tab10.to_string(index=False))
c0 = tab10[tab10.f_w == 0.0].continuum.all(); c4 = (~tab10[tab10.f_w == 0.4].continuum).all()
print(f"both keep a continuum at f_w 0: {c0}; neither does at 0.4: {c4}")
# seed check at f_w 0.4, the level the criterion reads for fragmentation (the network, the initial noise and the weight noise)
for k in range(1, 5):
    s = sd10 + 1000 * k
    _, Pk, Jk, xdk, xck = setup10(s)
    rwk = np.random.default_rng(s + 2)
    line = []
    for lab, Jb, x0 in (("disordered", Jk, xdk), ("circulant", J_circ, xck)):
        rec, n = run10(Jb, x0, 0.4, lab, Pk, rwk)
        cs, dmed, _ = summarize10(rec, n)
        line.append(f"{lab} states {cs}, median drift {dmed:.3f} rad")
    print(f"seed {s}, f_w 0.4: " + "; ".join(line), flush=True)
print(f"time {time.time()-t:.0f} s")
""", ["claim:figs10-robustness-comparable"])
md(r"""**Result: RESULT_S10**""")

md(r"""
## fig8-grid-scores-and-torus

Blocked (too large). The network of 25,000 neurons needs a 25,000 by 25,000 weight matrix (5 GB
in float64, 2.5 GB in float32), fitted by regression on 25,000 by 25,000 kernels and simulated,
and the grid-score sweep 1,000 maps for each eta. It was not started.
""")
md(r"""
## Summary

SUMMARY_TABLE
""")
code(r"""print(f"total time {time.time()-T0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB")""")
nb.cells = C
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, "entries/clark-2026/model_sims.ipynb")
PYEOF
cd  executed/clark-2026/.venv/bin/python $TMPDIR/dev/build_model.py && echo ok; python -c "import json;print(json.load(open('entries/clark-2026/theory.ipynb'))['metadata'])"
```

```
ok
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python'}}
```

**Agent calls Bash**

```bash
cd entries/clark-2026; ../../executed/clark-2026/.venv/bin/python - <<'E'
import json,os
d=json.load(open('model_sims.ipynb'))
rep=[("T=30.0","T=2.0"),("tt - 20.0","tt - 1.0"),("ref[20]","ref[1]"),("[20].max()","[1].max()"),("T=120.0","T=1.0"),("save_every=30.0","save_every=0.3"),("round(tt, 3) % 30 == 0","True"),("(30, 60, 90)","(0, 0, 0)")]
for c in d['cells']:
    s=''.join(c['source'])
    for a,b in rep: s=s.replace(a,b)
    c['source']=s
json.dump(d,open(os.environ['TMPDIR']+'/dev/model_test.ipynb','w'))
E
cp hdring.py ring_dmft.py $TMPDIR/dev/; cd $TMPDIR/dev; time executed/clark-2026/.venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=registry-clark-2026 --output model_test_out.ipynb model_test.ipynb 2>&1 | tail -3
```

```
[NbConvertApp] Converting notebook model_test.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 83982 bytes to model_test_out.ipynb

real	1m0.354s
user	3m49.849s
sys	0m0.700s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'E'
import json
d=json.load(open('model_test_out.ipynb'))
for c in d['cells']:
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:1500])
        if o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
E
```

```
X, Phi (500, 2500) | J (2500, 2500) | diagonal of J zero: True
input currents: mean -0.011, sd 1.002 (the process has unit variance); firing rates range 0.000 to 2.000 (1 + erf, bounded by 0 and 2)
reconstruction error mean((X - Phi J^T)^2) 2.585e-10

seed 4129464829: Gaussian doublet 1 radius 0.8011 (cv 0.0059, largest angle gap 0.359), doublet 2 radius 0.0121 (collapse True); mixture radii 0.5587 (cv 0.0063, gap 0.375) and 0.5711 (cv 0.0029, gap 0.381), rings True True; mixture angle drift at most 0.312 and 0.239 rad
seed 4129465829: Gaussian doublet 1 radius 0.7940 (cv 0.0057, largest angle gap 0.452), doublet 2 radius 0.0116 (collapse True); mixture radii 0.5682 (cv 0.0072, gap 0.558) and 0.5676 (cv 0.0094, gap 0.545), rings True True; mixture angle drift at most 0.368 and 0.406 rad

seed 4129466829: Gaussian doublet 1 radius 0.8000 (cv 0.0035, largest angle gap 0.315), doublet 2 radius 0.0206 (collapse True); mixture radii 0.5699 (cv 0.0071, gap 0.552) and 0.5730 (cv 0.0153, gap 0.438), rings True True; mixture angle drift at most 0.433 and 0.652 rad
seed 4129467829: Gaussian doublet 1 radius 0.7998 (cv 0.0022, largest angle gap 0.325), doublet 2 radius 0.0138 (collapse True); mixture radii 0.5728 (cv 0.0107, gap 0.517) and 0.5660 (cv 0.0066, gap 0.492), rings True True; mixture angle drift at most 0.535 and 0.416 rad

seed 4129468829: Gaussian doublet 1 radius 0.7985 (cv 0.0022, largest angle gap 0.353), doublet 2 radius 0.0239 (collapse True); mixture radii 0.5689 (cv 0.0067, gap 0.478) and 0.5621 (cv 0.0067, gap 0.561), rings True True; mixture angle drift at most 0.347 and 0.389 rad
      seed                     eig_gauss                        eig_mix  max_rel_diff  within_5pct  dynamics_as_described
4129464829   [102.72, 97.48, 25.4, 24.7]    [97.4, 96.55, 25.97, 25.79]        0.0518        False                   True
4129465829 [102.18, 98.28, 25.25, 24.54]   [99.72, 96.02, 25.81, 24.23]        0.0241         True                   True
4129466829 [100
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/clark-2026; python - <<'E'
import json
d=json.load(open('tuning_curves.ipynb'))
for i in [32,34,13,14,0,55]:
    print('---',i); print(''.join(d['cells'][i]['source']))
E
```

```
Thu Nov 26 17:05:38 UTC 2026
--- 32
## fig4-generative-fit

> A single parameter set of the generative process, fitted to the two-point correlation
> function pooled over mice, is (sigma, beta, b) of about (1.42, 2.77, 1.73).

The grid is the criterion's (`ring/gp_opt.py`: sigma in linspace(1, 2, 20), b in linspace(0.01,
5, 30), beta in linspace(0.01, 10, 30); error over the first 20 coefficients). The criterion
asks for 500,000 samples per evaluation; on this runner's CPUs that is about 3 hours for the
18,000 points. So the whole grid is first evaluated with 25,000 samples, the same draws for every
point (common random numbers, float32 as the paper's torch run on a GPU), and the 30 best points
are then evaluated again with 500,000 fresh samples each, which decide the minimum. This is a
deviation, recorded in the attempt; the shortlist pass and the final pass are both shown.
--- 34
**Result: partially reproduced.** With the final pass of 500,000 samples the minimum is at sigma
1.4737, b 1.2145, beta 3.1103 under all five seeds: sigma (1.42 within 0.142) and beta (2.77
within 0.345) match and b (1.73 within 0.173) does not. The paper's grid point (1.4211, 1.7307,
2.7659) is the minimum of the 25,000-sample shortlist pass and the second best in the final pass
(error 0.0095 against 0.0089); in the float32 variant it is the better of the two under the
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
import json
d=json.load(open('tuning_curves.ipynb'))
c=d['cells'][13]; s=''.join(c['source'])
s=s.replace('''print(f"chosen widths equal for both partitions: {same_sig.all(1).mean():.4f} of units; per partition: {same_sig.mean():.4f}")''',
'''print(f"chosen widths equal (==) for both partitions: {same_sig.all(1).mean():.4f} of units; per partition: {same_sig.mean():.4f}")
close_sig = np.isclose(ours_sig, c_sig, rtol=1e-9, atol=0)
print(f"chosen widths equal to rounding (np.isclose, rtol 1e-9; the cache stores e.g. 0.09999999999999999 for 0.1): {close_sig.all(1).mean():.4f} of units; per partition: {close_sig.mean():.4f}")''')
c['source']=s
c=d['cells'][33]; s=''.join(c['source'])
s=s.replace('''for kk in range(5):
    sd = sd0 + 1000 * kk
    fp = final_pass(L, np.random.default_rng(sd + 1))   # second generator of the claim: seed + 1
    fits[sd] = fp[0]
    if kk == 0:
        fp0 = fp
    print(f"seed {sd}: final pass (500,000 samples) best sigma {fp[0][1]:.4f}, b {fp[0][2]:.4f}, beta {fp[0][3]:.4f}, error {fp[0][0]:.5f}")''',
'''PAPER_GRID = (scale_vals[8], bias_vals[10], beta_vals[8])   # the grid point nearest the paper's parameters
for kk in range(5):
    sd = sd0 + 1000 * kk
    # 90 points under the claim's seed (variant: more than the 30 of the other seeds), 30 under the others
    fp = final_pass(L, np.random.default_rng(sd + 1), n_best=90 if kk == 0 else 30)   # second generator of the claim: seed + 1
    fp30 = sorted(fp, key=lambda r: r[4])[:30]   # the 30 best of the shortlist, the main pass
    fp30 = sorted(fp30)
    fits[sd] = fp30[0]
    if kk == 0:
        fp0, fp0_90 = fp30, fp
    pp = [r for r in fp30 if np.isclose(r[1], PAPER_GRID[0]) and np.isclose(r[2], PAPER_GRID[1]) and np.isclose(r[3], PAPER_GRID[2])][0]
    print(f"seed {sd}: final pass (500,000 samples) best sigma {fp30[0][1]:.4f}, b {fp30[0][2]:.4f}, beta {fp30[0][3]:.4f}, error {fp30[0][0]:.5f}; "
          f"at the paper's grid point {pp[0]:.5f} (rank {fp30.index(pp) + 1} of 30)")
print(f"variant, the 90 best of the shortlist at 500,000 samples (claim's seed): best sigma {fp0_90[0][1]:.4f}, b {fp0_90[0][2]:.4f}, beta {fp0_90[0][3]:.4f}, "
      f"error {fp0_90[0][0]:.5f}; best of points 31 to 90 of the shortlist {min(r[0] for r in sorted(fp0_90, key=lambda r: r[4])[30:]):.5f}")''')
s=s.replace('''paper_pt = (scale_vals[8], bias_vals[10], beta_vals[8])''','''paper_pt = PAPER_GRID''')
s=s.replace('''print("minimum error over b and beta at each sigma''','''# variant: a float32 final pass over all 30 shortlisted points, claim's seed (fourth generator, seed + 3)
rng32 = np.random.default_rng(sd0 + 3)
f32 = sorted((err32((r[1], r[2], r[3]), rng32), r[1], r[2], r[3]) for r in fp0)
print("float32 final pass over the 30 shortlisted points, the five best:", [(round(e, 5), round(a, 4), round(b_, 4), round(c_, 4)) for e, a, b_, c_ in f32[:5]])
# variant: the paper's own cached error grid (grid_search_results.npz in the Zenodo record, loss_vals over the same grid)
bz, m1, m2 = H.read_zenodo_member("grid_search_results.npz")
gz = H.load_npz_bytes(bz); Lp = gz["loss_vals"]
print("paper's cached grid: MD5 match", m1 == m2, "| same grid:", bool(np.allclose(gz["scale_vals"], scale_vals) and np.allclose(gz["bias_vals"], bias_vals) and np.allclose(gz["beta_vals"], beta_vals)))
for f in np.argsort(Lp.ravel())[:5]:
    a_, b_, c_ = np.unravel_index(f, Lp.shape)
    print(f"   paper's cached error {Lp[a_, b_, c_]:.5f} at sigma {scale_vals[a_]:.4f}, b {bias_vals[b_]:.4f}, beta {beta_vals[c_]:.4f}")
print(f"paper's cached error at the point chosen here (1.4737, 1.2145, 3.1103): {Lp[9, 7, 9]:.5f}; at the paper's point {Lp[8, 10, 8]:.5f}; difference {(Lp[9, 7, 9] / Lp[8, 10, 8] - 1) * 100:.1f}%")
print("minimum error over b and beta at each sigma''')
c['source']=s
json.dump(d,open('tuning_curves.ipynb','w'),indent=1,ensure_ascii=False); open('tuning_curves.ipynb','a').write('\n')
E
git diff --stat tuning_curves.ipynb
```

```
entries/clark-2026/tuning_curves.ipynb | 95 ++--------------------------------
 1 file changed, 3 insertions(+), 92 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/clark-2026; git diff tuning_curves.ipynb | head -30; git show HEAD:entries/clark-2026/tuning_curves.ipynb | head -c 600
```

```
diff --git a/entries/clark-2026/tuning_curves.ipynb b/entries/clark-2026/tuning_curves.ipynb
index b9b3c27..ac6c516 100644
--- a/entries/clark-2026/tuning_curves.ipynb
+++ b/entries/clark-2026/tuning_curves.ipynb
@@ -302,32 +302,7 @@
      "claim:tuning-curves-match-cache"
     ]
    },
-   "source": [
-    "b, md5_calc, md5_listed = H.read_zenodo_member(\"mouse_data/tc_data.npz\")\n",
-    "print(\"tc_data.npz MD5\", md5_calc, \"listed\", md5_listed, \"match:\", md5_calc == md5_listed)\n",
-    "cache = H.load_npz_bytes(b)\n",
-    "c_names = cache[\"mouse_names\"]; c_nums = cache[\"mouse_nums\"]; c_hd = cache[\"hd_mask\"]\n",
-    "print(\"cache: units\", len(c_hd), \"head-direction\", int(c_hd.sum()), \"sessions\", len(cache[\"unit_counts\"]))\n",
-    "print(\"cache session order equals ours:\", [str(n) for n in pd.unique(c_names)] == [d[\"subject\"] for d in sessions])\n",
-    "print(\"cache unit counts equal ours:\", list(cache[\"unit_counts\"]) == list(tab.units))\n",
-    "print(\"cache hd labels equal ours:\", np.array_equal(c_hd, np.concatenate([d[\"sess\"][\"is_hd\"] for d in sessions])),\n",
-    "      \"| exc labels:\", np.array_equal(cache[\"exc_mask\"], np.concatenate([d[\"sess\"][\"is_exc\"] for d in sessions])),\n",
-    "      \"| fs labels:\", np.array_equal(cache[\"fs_mask\"], np.concatenate([d[\"sess\"][\"is_fs\"] for d in sessions])))\n",
-    "ours_opt = np.concatenate([d[\"opt\"] for d in sessions]); ours_sig = np.concatenate([d[\"sig\"] for d in sessions])\n",
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nbfix.py <<'E'
import json, sys
for p in sys.argv[1:]:
    d = json.load(open(p))
    for c in d['cells']:
        if isinstance(c['source'], str):
            c['source'] = c['source'].splitlines(keepends=True)
    s = json.dumps(d, indent=1, ensure_ascii=False) + "\n"
    open(p, 'w').write(s)
E
cd entries/clark-2026; python $TMPDIR/nbfix.py tuning_curves.ipynb model_sims.ipynb; git diff --stat tuning_curves.ipynb; git show HEAD:entries/clark-2026/tuning_curves.ipynb > $TMPDIR/o.ipynb; python $TMPDIR/nbfix.py $TMPDIR/o.ipynb; git show HEAD:entries/clark-2026/tuning_curves.ipynb | diff -q - $TMPDIR/o.ipynb && echo sameformat
```

```
Exit code 1
 entries/clark-2026/tuning_curves.ipynb | 36 +++++++++++++++++++++++++++-------
 1 file changed, 29 insertions(+), 7 deletions(-)
Files - and /tmp/claude-1001/o.ipynb differ
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo; grep -o "gaussian_filter1d([^)]*)" notebooks/data_driven_attractor.ipynb | sort | uniq -c; grep -rn "gaussian_filter1d(" ring/*.py | head
```

```
1 gaussian_filter1d(x_save, sigma=sigma, axis=0)
ring/data.py:293:                smoothed_tcs[i] = gaussian_filter1d(tuning_curve, sigma=sigma_vals[i], mode='wrap')
ring/data_driven.py:168:    X_smooth = gaussian_filter1d(X, axis=0, sigma=sigma, mode='wrap')
ring/data_driven.py:654:    hd_unwrap_smooth = gaussian_filter1d(hd_unwrap, sigma=smoothing_sigma)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
import json
d=json.load(open('network.ipynb'))
src=lambda i: ''.join(d['cells'][i]['source'])
# fig2gi
s=src(13)
old='''def positions(xf):
    return gaussian_filter1d(xf.astype(np.float64), sigma=2.5, axis=0).argmax(0)'''
assert old in s
s=s.replace(old,'''def positions(xf, mode="reflect"):
    # data_driven_attractor.ipynb smooths with gaussian_filter1d's default mode (reflect), as here
    return gaussian_filter1d(xf.astype(np.float64), sigma=2.5, axis=0, mode=mode).argmax(0)''')
old='''def run_final(M, sd):
    rng = np.random.default_rng(sd)
    x0 = X_srt[::int(X_srt.shape[0] / 100)].T + rng.standard_normal((N, 100)) * 2.5
    return H.simulate(M, x0, T=30.0, dt=0.001, c=1.0)'''
assert old in s
s=s.replace(old,'''def run_final(M, sd, return_x0=False):
    rng = np.random.default_rng(sd)
    x0 = X_srt[::int(X_srt.shape[0] / 100)].T + rng.standard_normal((N, 100)) * 2.5
    xf = H.simulate(M, x0, T=30.0, dt=0.001, c=1.0)
    return (xf, x0) if return_x0 else xf''')
old='''for key, M in mats.items():
    xf = run_final(M, sd0 + 1)   # second generator of the claim: initial-condition noise'''
assert old in s
s=s.replace(old,'''for key, M in mats.items():
    xf, x0_gi = run_final(M, sd0 + 1, return_x0=True)   # second generator of the claim: initial-condition noise''')
old='''    print(f"{key}: states single {cs['single']}'''
s=s.replace(old,'''    cs_wrap = H.count_states(positions(xf, "wrap"), N, W)
    print(f"{key}: states (smoothing mode wrap, variant) single {cs_wrap['single']}, greedy {cs_wrap['greedy']}, bins {cs_wrap['bins']}")
    print(f"{key}: states single {cs['single']}''')
old='''print("reference: initial positions, states", H.count_states(positions(X_srt[::int(X_srt.shape[0] / 100)].T), N, W))'''
assert old in s
s=s.replace(old,old+'''
# the continuum tested directly: the manifold angle (nearest target point) of each sorted-matrix
# trajectory at the start (noisy initial state) and at the end
Phi_srt32_ = Phi32[:, order]
i0, _ = H.nearest_target(Phi_srt32_, H.nonlin(x0_gi.astype(np.float32)), Phi_srt_sq)
i1, d1 = H.nearest_target(Phi_srt32_, H.nonlin(res_gi["sorted"][0]), Phi_srt_sq)
shift = H.circ_diff(2 * np.pi * i1 / X.shape[0], 2 * np.pi * i0 / X.shape[0])
print(f"sorted matrix, initial-to-final manifold angle shift: median {np.median(shift):.4f} rad, 90th percentile {np.percentile(shift, 90):.4f}, max {shift.max():.4f}; "
      f"under 2 pi / 50 for {np.mean(shift < 2 * np.pi / 50):.2f} of trajectories; final angles in {len(np.unique(np.floor(i1 / (X.shape[0] / 50))))} of 50 bins")''')
old='''# seed check on the random parts (shuffle and initial noise) of the circulant plus noise matrix
for k in range(1, 5):
    sd = sd0 + 1000 * k
    A_k, _ = scrambled(np.random.default_rng(sd))
    pos = positions(run_final(1.275 * (J_circ + A_k), sd + 1))
    print(f"seed {sd}: circ_plus_noise states", H.count_states(pos, N, W))'''
assert old in s
s=s.replace(old,'''# seed check on the random parts: the shuffle and initial noise of the circulant plus noise matrix,
# and the initial noise of the sorted matrix
for k in range(1, 5):
    sd = sd0 + 1000 * k
    A_k, _ = scrambled(np.random.default_rng(sd))
    pos = positions(run_final(1.275 * (J_circ + A_k), sd + 1))
    xs_k, x0_k = run_final(J_srt, sd + 1, return_x0=True)
    a0, _ = H.nearest_target(Phi_srt32_, H.nonlin(x0_k.astype(np.float32)), Phi_srt_sq)
    a1, _ = H.nearest_target(Phi_srt32_, H.nonlin(xs_k), Phi_srt_sq)
    sh = H.circ_diff(2 * np.pi * a1 / X.shape[0], 2 * np.pi * a0 / X.shape[0])
    print(f"seed {sd}: circ_plus_noise states", H.count_states(pos, N, W), "| sorted states", H.count_states(positions(xs_k), N, W),
          f"| sorted, manifold-angle shift median {np.median(sh):.4f} rad, max {sh.max():.4f}, final angles in {len(np.unique(np.floor(a1 / (X.shape[0] / 50))))} of 50 bins", flush=True)''')
d['cells'][13]['source']=s
# figs14
s=src(19)
old='''print("eigenvalues: real range"'''
assert old in s
s=s.replace(old,'''# variants: the constant mode is not unique (eigenvectors 5 to 7 tie in their overlap with the
# uniform vector), so each of the three is set aside in turn; and pairs that are complex
# conjugates (equal real parts by construction) are marked
conj = lambda a_, b_: abs(a_.imag) > 1e-9 and np.isclose(a_, np.conj(b_))
for u_ in (4, 5, 6):
    rest_c = np.delete(lead, u_)
    pr = [(rest_c[2 * p], rest_c[2 * p + 1]) for p in range(4)]
    wi = [a_.real - b_.real for a_, b_ in pr]; tn = [rest_c[2 * p + 1].real - rest_c[2 * p + 2].real for p in range(4)]
    ok = [w_ < n_ for w_, n_ in zip(wi, tn)]; cj = [conj(a_, b_) for a_, b_ in pr]
    print(f"variant, eigenvalue {u_ + 1} set aside: within < next {ok}, complex-conjugate pairs {cj}; pairs passing that are not conjugates {sum(o_ and not c_ for o_, c_ in zip(ok, cj))} of 4")
print("eigenvalues: real range"''')
d['cells'][19]['source']=s
# figs11b
s=src(22)
old='''t = time.time()
print(f"thresholds from fig2ef at 20 s: largest {D20_MAX:.5f}, median {D20_MED:.5f}")'''
assert old in s
s=s.replace(old,'''t = time.time()
print(f"thresholds from fig2ef at 20 s (1-ms step, as fig2ef): largest {D20_MAX:.5f}, median {D20_MED:.5f}")
# the reference on the same footing as the runs below: the fig2ef protocol (its seed, its 100 noisy
# manifold starts) with the 5-ms step of spurious_fixed_points.ipynb, distance at 20 s and at the end
rng_ref = np.random.default_rng(H.seed("fig2ef-data-network-quasicontinuous"))
x0_ref = X[::100].T + rng_ref.standard_normal((N, 100)) * 3.0
ref5 = {}
def on_save_ref(tt, x):
    if abs(tt - 20.0) < 1e-6:
        ref5[20] = H.nearest_target(Phi32, H.nonlin(x), Phi_sq)[1]
xf_ref = H.simulate(J, x0_ref, T=30.0, dt=0.005, c=1.0, save_every=0.1, on_save=on_save_ref)
ref5["end"] = H.nearest_target(Phi32, H.nonlin(xf_ref), Phi_sq)[1]
D20_MAX5 = ref5[20].max()
print(f"fig2ef protocol with the 5-ms step: distance at 20 s median {np.median(ref5[20]):.5f}, largest {D20_MAX5:.5f}; at the end (29.995 s) median {np.median(ref5['end']):.5f}, largest {ref5['end'].max():.5f}")''')
old='''        line.append(f"sd {sv}: finite {fin}, median dist {np.median(dist):.5f}, max {dist.max():.5f}, within largest {np.mean(dist <= D20_MAX):.2f}, within median {np.mean(dist <= D20_MED):.2f}")'''
assert old in s
s=s.replace(old,'''        line.append(f"sd {sv}: finite {fin}, median dist {np.median(dist):.5f}, max {dist.max():.5f}, within largest (5-ms reference) {np.mean(dist <= D20_MAX5):.2f}, "
                    f"within largest (1-ms fig2ef) {np.mean(dist <= D20_MAX):.2f}, within median {np.mean(dist <= D20_MED):.2f}")''')
old='''    print(f"seed {sd}: " + "; ".join(line) + f"; sd 1 final angles as states: {cs}")'''
assert old in s
s=s.replace(old,'''    print(f"seed {sd}: " + "; ".join(line) + f"; sd 1 final angles as states: {cs}")
    print(f"   at least 95% within the 5-ms reference at every standard deviation: {all(np.mean(o[1] <= D20_MAX5) >= 0.95 for o in out.values())}; "
          f"within the 1-ms one: {all(np.mean(o[1] <= D20_MAX) >= 0.95 for o in out.values())}", flush=True)''')
old='''def run_s11b(sd):
    rng = np.random.default_rng(sd)
    out = {}
    for sv in (1, 10, 50, 100, 1000):
        x0 = rng.standard_normal((N, 34)) * sv'''
assert old in s
s=s.replace(old,'''INIT_D = {}
def run_s11b(sd):
    rng = np.random.default_rng(sd)
    out = {}
    for sv in (1, 10, 50, 100, 1000):
        x0 = rng.standard_normal((N, 34)) * sv
        INIT_D.setdefault(sd, {})[sv] = np.median(H.nearest_target(Phi32, H.nonlin(x0.astype(np.float32)), Phi_sq)[1])''')
old='''print("sd 1 final manifold angles (rad), claim seed:"'''
assert old in s
s=s.replace(old,'''print("median initial distance to the manifold by standard deviation, claim seed:", {k_: round(float(v_), 3) for k_, v_ in INIT_D[H.seed("figs11b-data-network-global-stability")].items()})
print("sd 1 final manifold angles (rad), claim seed:"''')
d['cells'][22]['source']=s
json.dump(d,open('network.ipynb','w'),indent=1,ensure_ascii=False)
E
python $TMPDIR/nbfix.py network.ipynb; git diff --stat network.ipynb
```

```
entries/clark-2026/network.ipynb | 66 ++++++++++++++++++++++++++++++++++------
 1 file changed, 56 insertions(+), 10 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/clark-2026; grep -n "def \|return" ring_dmft.py | sed -n 1,80p
```

```
32:    def unity_erf(x):
33:        return erf(np.sqrt(np.pi) * x / 2.)
39:    def wrapped_gaussian_cov(eq_var, scale, N_theta, backend='numpy'):
44:        return Gamma, Gamma_ft
90:    def __init__(self, N_theta=1000, scale=1.5, g=2.0, lamda=1e-12):
103:    def compute_F_function(self):
114:        def F(C_11, C_22, C_12):
118:            return 1 + t_12
120:        def dF_dC12(C_11, C_22, C_12):
123:            return (g**2) * (2/np.pi) * 1./np.sqrt(B)
125:        def dF_dC11(C_11, C_22, C_12):
130:            return dF_dA * dA_dC11
136:    def compute_Gamma(self):
143:    def compute_J_and_U(self):
155:    def rfft_sum(self, x):
157:        return x[0].real + 2 * x[1:].real.sum()
159:    def J_m_prod(self, m):
162:        return np.fft.irfft(self.J_ft * m_ft, norm='forward')
164:    def J_deriv_m_hat_prod(self, m_hat):
170:        return np.fft.irfft(J_deriv_ft * m_hat_ft, norm='forward')
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; sed -n 282,306p ring_dmft.py
```

```
def compute_bump_jacobian(self, exclude_Q=False):
        """Compute the Jacobian and eigenvalues at the bump solution.

        Parameters
        ----------
        exclude_Q : bool, default False
            If True, omit the Q-fluctuation contribution.

        Returns
        -------
        jac : ndarray, shape (N_theta, N_theta)
            Jacobian matrix at the bump.
        eigenvals : ndarray, shape (N_theta,)
            Eigenvalues sorted by descending real part.
        """
        G1 = self.dF_dC12(self.Gamma_x[0], self.Gamma_x[0], self.Gamma_x)
        G2 = self.dF_dC11(self.Gamma_x[0], self.Gamma_x[0], self.Gamma_x)

        T1 = G1[:, None] * circulant(self.J)
        T2 = G2[:, None] * 2 * self.J[None, :] if not exclude_Q else 0.
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; sed -n 90,135p ring_dmft.py
```

```
def __init__(self, N_theta=1000, scale=1.5, g=2.0, lamda=1e-12):
        self.N_theta = N_theta
        self.scale = scale
        self.g = g
        self.lamda = lamda
        self.theta = np.arange(N_theta) * 2 * np.pi / N_theta
        self.dtheta = self.theta[1] - self.theta[0]

        self.nonlin = lambda x: 1 + fn.unity_erf(self.g * x)
        self.compute_F_function()
        self.compute_Gamma()
        self.compute_J_and_U()

    def compute_F_function(self):
        """(internal) Derive the nonlinear covariance map ``F`` and its derivatives.

        Sets three instance attributes:

        - ``self.F(C_11, C_22, C_12)``: the 2-point Gaussian average of the
          erf-based nonlinearity for joint variances/covariance ``C_*``.
[... 25 more lines not kept]
```

**Agent**

Now the theory and grid notebooks.

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
import json
d=json.load(open('theory.ipynb'))
s=''.join(d['cells'][5]['source'])
old='''        bump[i, j] = mdl.compute_bump_jacobian()[1][:5]'''
assert old in s
s=s.replace(old,'''        bump[i, j] = mdl.compute_bump_jacobian()[1][:5]
        m_b = mdl.F(mdl.Gamma_x[0], mdl.Gamma_x[0], mdl.Gamma_x)   # the bump the Jacobian is taken at
        amp[i, j] = m_b.max() - m_b.min()''')
s=s.replace('''bump = np.zeros((40, 20, 5), complex); homo = np.zeros((40, 20, 5), complex)''','''bump = np.zeros((40, 20, 5), complex); homo = np.zeros((40, 20, 5), complex); amp = np.zeros((40, 20))''')
old='''print("bump eigenvalue 3 (first after'''
assert old in s
s=s.replace(old,'''nz = bump[..., 0].real < -1e-6
print(f"bump amplitude (max - min of m): at the {int(nz.sum())} points without a zero mode median {np.median(amp[nz]):.3e}, range {amp[nz].min():.3e} to {amp[nz].max():.3e}; "
      f"at the other {int((~nz).sum())} median {np.median(amp[~nz]):.3e}, range {amp[~nz].min():.3e} to {amp[~nz].max():.3e}")
print(f"points with amplitude below 1e-3: {int((amp < 1e-3).sum())}, of which without a zero mode {int((nz & (amp < 1e-3)).sum())}; "
      f"largest bump eigenvalue 1 where the amplitude is at least 1e-3: {bump[..., 0].real[amp >= 1e-3].min():.3e} (most negative)")
'''+old)
d['cells'][5]['source']=s
json.dump(d,open('theory.ipynb','w'),indent=1,ensure_ascii=False)

d=json.load(open('network_grid.ipynb'))
s=''.join(d['cells'][4]['source'])
old='''        n_ic = 100 if (c in (0, 1.0) and lam in (1e-12, 1e-8, 1e-4, 1e-2)) else 20'''
assert old in s
s=s.replace(old,'''        n_ic = 100   # every grid point, as the paper's run_convergence_grid (N_ics 100)''')
old='''part4 = errs[1e-8] < errs[1e-2] and errs[1e-8] < errs[1e-12]'''
assert old in s
s=s.replace(old,old+'''
# the paper's own flow errors, err_grid of pc_convergence_grid.npz in the Zenodo record (same lambda grid)
bz, m1, m2 = H.read_zenodo_member("pc_convergence_grid.npz")
pz = H.load_npz_bytes(bz)
err_p = dict(zip(pz["lamda_vals"].tolist(), pz["err_grid"][:, 0].tolist()))
print("paper's cached flow errors: MD5 match", m1 == m2, "| N_ics", int(pz["N_ics"]), "dt", float(pz["dt"]), "noise", float(pz["noise_std"]))
print("   lambda: paper / here:", {f"{k:g}": f"{err_p[k]:.3e} / {errs[k]:.3e}" for k in lamdas})
print("   in the paper's values, 1e-8 below 1e-2:", err_p[1e-8] < err_p[1e-2], "| below 1e-12:", err_p[1e-8] < err_p[1e-12], "| lambda of the minimum:", min(err_p, key=err_p.get))''')
d['cells'][4]['source']=s
json.dump(d,open('network_grid.ipynb','w'),indent=1,ensure_ascii=False)
E
python $TMPDIR/nbfix.py theory.ipynb network_grid.ipynb; git diff --stat .
```

```
entries/clark-2026/hdring.py           | 31 ++++++++++++++--
 entries/clark-2026/network.ipynb       | 66 ++++++++++++++++++++++++++++------
 entries/clark-2026/network_grid.ipynb  | 11 ++++--
 entries/clark-2026/theory.ipynb        | 11 ++++--
 entries/clark-2026/tuning_curves.ipynb | 36 +++++++++++++++----
 5 files changed, 131 insertions(+), 24 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/clark-2026; ../../executed/clark-2026/.venv/bin/python - <<'E'
import json,ast
for nb in ['tuning_curves','network','network_grid','theory','model_sims']:
    d=json.load(open(nb+'.ipynb'))
    for i,c in enumerate(d['cells']):
        if c['cell_type']=='code':
            try: ast.parse(''.join(c['source']))
            except SyntaxError as e: print(nb,i,e)
print('parsed')
import ring_dmft as D, numpy as np
mdl=D.DMFTModel(N_theta=500, scale=100.0, g=0.01)
m=mdl.F(mdl.Gamma_x[0], mdl.Gamma_x[0], mdl.Gamma_x); print(m.max()-m.min(), mdl.compute_bump_jacobian()[1][:2].real)
mdl=D.DMFTModel(N_theta=500, scale=1.42, g=2.77)
m=mdl.F(mdl.Gamma_x[0], mdl.Gamma_x[0], mdl.Gamma_x); print(m.max()-m.min())
E
```

```
parsed
9.904122960213702e-05 [-2.50952739e-06 -2.50966105e-06]
0.749125318909416
```

**Agent calls Bash**

```bash
date -u; cd  ls questions/ | head; cat questions/clark-2026.yaml 2>/dev/null | head -50; ls questions | grep -v clark | head -2 | xargs -I{} sh -c 'echo == {}; head -30 questions/{}'
```

```
Thu Nov 26 17:07:50 UTC 2026
README.md
asari-2009.yaml
ashworth-2025.yaml
athalye-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
berg-2020.yaml
boran-2022.yaml
bouchard-2013.yaml
== README.md
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
amended and why. Each question has `claim`, `question`, `passage`, `why` (how the misreading could
change the outcome), and, once answered, `answer` and `answered` (a date). Method details the claims
file lacks are not asked here: the author takes them from the paper, and a detail the paper does not
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; grep -il "Fig. 2" paper/* | head; grep -n -i "continuum of stable\|sits just above\|just above the minimum\|ill-conditioned" -r paper/ | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 5770,5795p paper/10.1038-s41593-026-02452-4.txt; sed -n 490,520p paper/10.1038-s41593-026-02452-4.txt; grep -n "Fig. 2 |\|^Fig. 2\b\|Figure 2 |" paper/10.1038-s41593-026-02452-4.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 616,640p paper/10.1038-s41593-026-02452-4.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
q={'questions':[
{'claim':'fig2gi-circulant-noise-collapses',
 'question':'The criterion places each final state by the peak neuron of its smoothed input currents across the 1,533 sorted neurons, merges positions within 31 neurons, and asks the sorted optimal matrix to keep at least 50 states. Fig. 2g plots the steady states against the manifold coordinate theta, so the continuum the paper shows is one of manifold angles. Should a state be placed by its manifold angle (for example the angle of the nearest target point), with the 50 states counted on that coordinate?',
 'passage':'Results, Dynamics of the data-derived network model, "The optimal weights (Fig. 2b) maintain a continuum of stable, heterogeneous states (Fig. 2g)"; Fig. 2 legend, "g-i, Steady-state activity across ordered neurons at manifold coordinate theta, not to be confused with tuning curves across theta".',
 'why':'On the criterion\'s position measure the 50 states cannot be reached by any matrix. The heterogeneous currents of the 1,533 neurons peak on few neurons, so even the 100 initial states give only 24 to 33 states (single linkage, greedy and bins), and the sorted matrix keeps 24 to 31; the claim is then partially reproduced. Placed by the manifold angle of the nearest target point, the sorted matrix keeps all 50 bins of width 2 pi / 50 while the circulant plus noise keeps 7, which would make the claim reproduced if the circulant shift test also holds.'},
{'claim':'figs8-s9-lambda-and-c',
 'question':'The criterion asks for the flow error at lambda 1e-8 to be lower than at 1e-2 and at 1e-12. The supplement says lambda 1e-8 "sits just above the minimum", with the error rising at small lambda where the kernel is ill-conditioned; it does not say that 1e-8 is below 1e-12. Should the test be that the flow error rises at both ends of the grid, with its minimum below 1e-8 and the error at 1e-8 still small?',
 'passage':'Supplementary Note 3, section 8.4, "Supplementary Fig. 9 shows the mean squared flow rising with larger lambda and also rising at small lambda, where the optimization kernel becomes ill-conditioned. The value lambda = 10^-8 used in the paper sits just above the minimum, beyond the ill-conditioned regime but with the flow error still negligible."',
 'why':'Here the flow error is lowest at lambda 1e-10 and rises on both sides, and the error at 1e-8 (1.7e-8) is above that at 1e-12 (about 3e-9). The paper\'s own cached errors (err_grid of pc_convergence_grid.npz on Zenodo) are the same, 1.7e-8 at 1e-8 and 3.8e-9 at 1e-12, so the part fails on the paper\'s numbers as well. Under the supplement\'s wording this part would hold, and the claim would then turn on the test of collapse at lambda 1e-2 and c 1 alone.'},
]}
open('questions/clark-2026.yaml','w').write(yaml.safe_dump(q,sort_keys=False,width=100,allow_unicode=True))
E
cat questions/clark-2026.yaml | head -20
```

```
questions:
- claim: fig2gi-circulant-noise-collapses
  question: The criterion places each final state by the peak neuron of its smoothed input currents across
    the 1,533 sorted neurons, merges positions within 31 neurons, and asks the sorted optimal matrix to
    keep at least 50 states. Fig. 2g plots the steady states against the manifold coordinate theta, so
    the continuum the paper shows is one of manifold angles. Should a state be placed by its manifold
    angle (for example the angle of the nearest target point), with the 50 states counted on that coordinate?
  passage: Results, Dynamics of the data-derived network model, "The optimal weights (Fig. 2b) maintain
    a continuum of stable, heterogeneous states (Fig. 2g)"; Fig. 2 legend, "g-i, Steady-state activity
    across ordered neurons at manifold coordinate theta, not to be confused with tuning curves across
    theta".
  why: On the criterion's position measure the 50 states cannot be reached by any matrix. The heterogeneous
    currents of the 1,533 neurons peak on few neurons, so even the 100 initial states give only 24 to
    33 states (single linkage, greedy and bins), and the sorted matrix keeps 24 to 31; the claim is then
    partially reproduced. Placed by the manifold angle of the nearest target point, the sorted matrix
    keeps all 50 bins of width 2 pi / 50 while the circulant plus noise keeps 7, which would make the
    claim reproduced if the circulant shift test also holds.
- claim: figs8-s9-lambda-and-c
  question: The criterion asks for the flow error at lambda 1e-8 to be lower than at 1e-2 and at 1e-12.
    The supplement says lambda 1e-8 "sits just above the minimum", with the error rising at small lambda
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python -c "
import json
for nb,cells in [('network',[0,12,18,21,24]),('network_grid',[0,3,6])]:
    d=json.load(open(nb+'.ipynb'))
    for i in cells: print('---',nb,i);print(''.join(d['cells'][i]['source']))
"
```

```
--- network 0
# Clark, Abbott & Sompolinsky (2026): the data-derived network, on DANDI:000939

Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`, written from the
version of record and its supplement.

Dataset. DANDI:000939 at version 0.240528.1542, the version the paper cites; every file
was replaced in later versions (see `tuning_curves.ipynb`, "Files and versions").

The tuning curves are computed from the streamed NWB files as in `tuning_curves.ipynb`
(`hdring.load_all_curves`). The network is built and run as in the paper's
`notebooks/data_driven_attractor.ipynb`, `spurious_fixed_points.ipynb` and `ring/data_driven.py`
(commit 245726f), in numpy and float32 (the paper's simulations use float32 torch tensors).
The lambda and c grid of Supplementary Figs. 8 and 9 is in `network_grid.ipynb`.

| claim | tested here |
|---|---|
| fig2b-sorted-weights-mexican-hat | yes |
| fig2ef-data-network-quasicontinuous | yes |
| fig2gi-circulant-noise-collapses | yes |
[... 106 more lines not kept]
```

**Agent**

Updating the markdown descriptions and entry.yaml to match the new analyses.

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
import json
def edit(nb, i, old, new):
    d=json.load(open(nb+'.ipynb'))
    s=''.join(d['cells'][i]['source'])
    assert old in s, (nb,i,old[:40])
    d['cells'][i]['source']=s.replace(old,new)
    json.dump(d,open(nb+'.ipynb','w'),indent=1,ensure_ascii=False)
edit('network_grid',0,'''The paper's notebook runs 100 initial conditions at each of the
42 grid points; here 20 are run at each point (every 500th target angle), to keep the notebook
within its time limit, and 100 at the points the criterion reads at c 0 and c 1 (a deviation,
recorded in the attempt).''','''As in the paper's notebook, 100 initial conditions are run at each of
the 42 grid points (every 100th target angle). The paper's own flow errors (err_grid of
`pc_convergence_grid.npz` in the Zenodo record doi:10.5281/zenodo.21827768) are read for
comparison.''')
edit('network_grid',6,'''Differences from the paper's method. 20 initial conditions at most grid points, 100 at the
points the criterion reads; collapse is read in two ways, as the claims file's words leave open.''','''Differences from the paper's method. Collapse is read in two ways, as the claims file's words
leave open; random draws come from the claim's seed. The seed check runs 20 initial conditions
at the four points the criterion reads.''')
edit('network',21,'''The final firing rates are compared
with the distance to the manifold reached at 20 s in fig2ef (the largest over its 100
trajectories, reading 1, or their median, reading 2).''','''The final firing rates are compared
with the distance to the manifold reached at 20 s in fig2ef, the largest over its 100
trajectories. The final distances sit at the network's resolution (about 1e-3), and the fig2ef
run uses a 1-ms step where this one uses 5 ms, which leaves the final states slightly farther
from the targets; so the threshold is taken from the fig2ef protocol (its seed and its 100 noisy
starts) run with the 5-ms step of these runs (assumption). The largest and median fig2ef
distances with the 1-ms step are shown as variants.''')
edit('network',0,'''The lambda and c grid of Supplementary Figs. 8 and 9 is in `network_grid.ipynb`.''','''The lambda and c grid of Supplementary Figs. 8 and 9 is in `network_grid.ipynb`; the
simulations of the generative-process and rank-four networks are in `model_sims.ipynb`.''')
edit('tuning_curves',0,'''| simulation-only claims (data: elsewhere) | see the attempt record |''','''| simulation-only claims (data: elsewhere) | in theory.ipynb and model_sims.ipynb |''')
edit('tuning_curves',32,'''are then evaluated again with 500,000 fresh samples each, which decide the minimum. This is a
deviation, recorded in the attempt; the shortlist pass and the final pass are both shown.''','''are then evaluated again with 500,000 fresh samples each, which decide the minimum. This is a
deviation, recorded in the attempt; the shortlist pass and the final pass are both shown. As
variants: the 90 best points at 500,000 samples under the claim's seed, a float32 final pass over
the 30, and the paper's own cached error grid (`grid_search_results.npz` in the Zenodo record,
the same grid).''')
E
python $TMPDIR/nbfix.py network.ipynb network_grid.ipynb tuning_curves.ipynb
python - <<'E'
s=open('entry.yaml').read()
s=s.replace('''- path: theory.ipynb
  title: Mean-field theory and large-N spectra
  runtime_minutes: 4''','''- path: theory.ipynb
  title: Mean-field theory and large-N spectra
  runtime_minutes: 4
- path: model_sims.ipynb
  title: Simulations of the generative-process and rank-four networks
  runtime_minutes: 32''')
s=s.replace("runtime_minutes: 10\n","runtime_minutes: 21\n").replace("runtime_minutes: 25\n","runtime_minutes: 33\n")
open('entry.yaml','w').write(s)
E
grep -n runtime entry.yaml; cd ../..; date -u
```

```
15:  runtime_minutes: 18
18:  runtime_minutes: 33
21:  runtime_minutes: 21
24:  runtime_minutes: 4
27:  runtime_minutes: 32
Thu Nov 26 17:08:43 UTC 2026
```

**Agent calls Bash**

```bash
cd  executed/clark-2026/.venv/bin/python -c "import numpy;print(numpy.__version__)"; python tools/entry.py check entries/clark-2026 2>&1 | tail -15
```

```
2.5.5
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/clark-2026; ../../executed/clark-2026/.venv/bin/python - <<'E'
import json,os
T=os.environ['TMPDIR']+'/dev/'
d=json.load(open('network.ipynb'))
for i,c in enumerate(d['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='code':
        s=s.replace("T=30.0","T=0.6").replace("tt - 20.0","tt - 0.5").replace("ref5[20]","ref5.get(20, ref5['end'])" if False else "ref5[20]")
        s=s.replace("abs(tt - 0.5) < 1e-6","abs(tt - 0.5) < 1e-6")
        if 'claim:fig2jk-velocity-integration' in c['metadata'].get('tags',[]): s="pass"
        if 'claim:fig2ef' in str(c['metadata'].get('tags',[])): s=s.replace("np.argmin(np.abs(tt - 20))","np.argmin(np.abs(tt - 0.5))").replace("np.argmin(np.abs(tt - 1))","np.argmin(np.abs(tt - 0.2))").replace("for k in range(5)","for k in range(1)")
    c['source']=s
json.dump(d,open(T+'net_test.ipynb','w'))
d=json.load(open('tuning_curves.ipynb'))
for i,c in enumerate(d['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='code':
        if i==33:
            s=s.replace("def grid_pass(rng, N=25000)","def grid_pass(rng, N=500)").replace("100000, rng)","2000, rng)").replace("H.sample_z(rng, 100000, 51","H.sample_z(rng, 2000, 51")
        elif i>33: s="pass"
    c['source']=s
json.dump(d,open(T+'tc_test.ipynb','w'))
E
cp hdring.py ring_dmft.py $TMPDIR/dev/; cd $TMPDIR/dev; for nb in tc_test net_test; do /usr/bin/time -f "%e s" executed/clark-2026/.venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --ExecutePreprocessor.kernel_name=registry-clark-2026 --output ${nb}_out.ipynb $nb.ipynb 2>&1 | grep -v WARNING | tail -4; done
```

```
[31mIndexError[39m: list index out of range

Command exited with non-zero status 1
191.33 s
[NbConvertApp] Converting notebook net_test.ipynb to notebook
[NbConvertApp] Writing 588446 bytes to net_test_out.ipynb
151.32 s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; executed/clark-2026/.venv/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.kernel_name=registry-clark-2026 --output tc_test_out.ipynb tc_test.ipynb >/dev/null 2>&1; python - <<'E'
import json
d=json.load(open('tc_test_out.ipynb'))
for i in [13,33]:
    for o in d['cells'][i].get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[-2500:])
        if o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'],'\n'.join(o['traceback'][-3:])[-1500:])
d=json.load(open('net_test_out.ipynb'))
for i in [13,19,22]:
    for o in d['cells'][i].get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[-3000:])
        if o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
E
```

```
tc_data.npz MD5 6e1f3a17ab67e2e0eb8fac35d89e2d57 listed 6e1f3a17ab67e2e0eb8fac35d89e2d57 match: True
cache: units 2691 head-direction 1533 sessions 31
cache session order equals ours: True
cache unit counts equal ours: True
cache hd labels equal ours: True | exc labels: True | fs labels: True
units compared: 1533
Pearson r of partition-averaged curves: min 1.000000, median 1.000000; fraction >= 0.99: 1.0000
max abs difference of partition-averaged curves (Hz): 1.4210854715202004e-14
max abs difference of plain curves (Hz): 0.0
chosen widths equal (==) for both partitions: 0.7841 of units; per partition: 0.8855
chosen widths equal to rounding (np.isclose, rtol 1e-9; the cache stores e.g. 0.09999999999999999 for 0.1): 1.0000 of units; per partition: 1.0000
where the widths differ, max abs curve difference: 2.1316282072803006e-14 | our width range there: (0.1, 93.26033468832199) | cache width range there: (0.09999999999999999, 93.260334688322)

shortlist pass (25,000 samples) in 4 s: minimum at sigma 1.3684, b 5.0000, beta 2.4214, error 0.01090

ERR IndexError list index out of range [31mIndexError[39m                                Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[14][39m[32m, line 43[39m
[32m     39[39m     fp30 = sorted(fp30)
[32m     40[39m     fits[sd] = fp30[[32m0[39m]
[32m     41[39m     [38;5;28;01mif[39;00m kk == [32m0[39m:
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
import json
d=json.load(open('tuning_curves.ipynb'))
s=''.join(d['cells'][33]['source'])
old='''    pp = [r for r in fp30 if np.isclose(r[1], PAPER_GRID[0]) and np.isclose(r[2], PAPER_GRID[1]) and np.isclose(r[3], PAPER_GRID[2])][0]
    print(f"seed {sd}: final pass (500,000 samples) best sigma {fp30[0][1]:.4f}, b {fp30[0][2]:.4f}, beta {fp30[0][3]:.4f}, error {fp30[0][0]:.5f}; "
          f"at the paper's grid point {pp[0]:.5f} (rank {fp30.index(pp) + 1} of 30)")'''
assert old in s
s=s.replace(old,'''    pp = [r for r in fp30 if np.isclose(r[1], PAPER_GRID[0]) and np.isclose(r[2], PAPER_GRID[1]) and np.isclose(r[3], PAPER_GRID[2])]
    at_paper = f"at the paper's grid point {pp[0][0]:.5f} (rank {fp30.index(pp[0]) + 1} of 30)" if pp else "the paper's grid point is not among the 30"
    print(f"seed {sd}: final pass (500,000 samples) best sigma {fp30[0][1]:.4f}, b {fp30[0][2]:.4f}, beta {fp30[0][3]:.4f}, error {fp30[0][0]:.5f}; " + at_paper)''')
d['cells'][33]['source']=s
json.dump(d,open('tuning_curves.ipynb','w'),indent=1,ensure_ascii=False)
E
python $TMPDIR/nbfix.py tuning_curves.ipynb
../../executed/clark-2026/.venv/bin/python - <<'E'
import json,os
T=os.environ['TMPDIR']+'/dev/'
d=json.load(open('tuning_curves.ipynb'))
for i,c in enumerate(d['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='code':
        if i==33:
            s=s.replace("def grid_pass(rng, N=25000)","def grid_pass(rng, N=500)").replace("100000, rng)","2000, rng)").replace("H.sample_z(rng, 100000, 51","H.sample_z(rng, 2000, 51")
        elif i>33: s="pass"
    c['source']=s
json.dump(d,open(T+'tc_test.ipynb','w'))
E
cd $TMPDIR/dev; executed/clark-2026/.venv/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.kernel_name=registry-clark-2026 --output tc_test_out.ipynb tc_test.ipynb >/dev/null 2>&1; python - <<'E'
import json
d=json.load(open('tc_test_out.ipynb'))
for o in d['cells'][33].get('outputs',[]):
    if 'text' in o: print(''.join(o['text'])[-2500:])
    if o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
E
```

```
shortlist pass (25,000 samples) in 4 s: minimum at sigma 1.3684, b 5.0000, beta 2.4214, error 0.01090

seed 444120632: final pass (500,000 samples) best sigma 1.4737, b 0.5262, beta 4.8328, error 0.01143; the paper's grid point is not among the 30

seed 444121632: final pass (500,000 samples) best sigma 1.4737, b 0.5262, beta 4.8328, error 0.00876; the paper's grid point is not among the 30

seed 444122632: final pass (500,000 samples) best sigma 1.4737, b 0.5262, beta 4.8328, error 0.01008; the paper's grid point is not among the 30

seed 444123632: final pass (500,000 samples) best sigma 1.5263, b 0.5262, beta 4.8328, error 0.01072; the paper's grid point is not among the 30

seed 444124632: final pass (500,000 samples) best sigma 1.4737, b 0.5262, beta 4.8328, error 0.01070; the paper's grid point is not among the 30
variant, the 90 best of the shortlist at 500,000 samples (claim's seed): best sigma 1.4737, b 1.2145, beta 3.1103, error 0.00809; best of points 31 to 90 of the shortlist 0.00809
final pass, claim seed, the ten best of the 30:
 error_500k  sigma      b   beta  error_25k
     0.0114 1.4737 0.5262 4.8328     0.0172
     0.0128 1.5263 0.3541 6.2107     0.0184
     0.0129 1.4737 0.3541 6.2107     0.0161
     0.0130 1.4737 1.5586 2.7659     0.0175
     0.0142 1.5263 0.5262 4.8328     0.0197
     0.0143 1.4211 3.4514 2.4214     0.0192
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
import json
def edit(nb, i, old, new):
    d=json.load(open(nb+'.ipynb'))
    s=''.join(d['cells'][i]['source'])
    assert old in s, (nb,i,old[:40])
    d['cells'][i]['source']=s.replace(old,new)
    json.dump(d,open(nb+'.ipynb','w'),indent=1,ensure_ascii=False)
edit('network_grid',4,'''        n_ic = 100   # every grid point, as the paper's run_convergence_grid (N_ics 100)''','''        n_ic = 100 if (c in (0, 1.0) and lam in (1e-12, 1e-8, 1e-4, 1e-2)) else 20''')
edit('network_grid',0,'''As in the paper's notebook, 100 initial conditions are run at each of
the 42 grid points (every 100th target angle).''','''The paper's notebook runs 100 initial conditions at each of the
42 grid points; here 20 are run at each point (every 500th target angle), to keep the entry's
run within its time limit, and 100 at the points the criterion reads at c 0 and c 1 (a deviation,
recorded in the attempt).''')
edit('network_grid',6,'''Differences from the paper's method. Collapse is read in two ways, as the claims file's words
leave open; random draws come from the claim's seed. The seed check runs 20 initial conditions
at the four points the criterion reads.''','''Differences from the paper's method. 20 initial conditions at most grid points, 100 at the
points the criterion reads; collapse is read in two ways, as the claims file's words leave open;
random draws come from the claim's seed.''')
E
python $TMPDIR/nbfix.py network_grid.ipynb; sed -i 's/runtime_minutes: 21$/runtime_minutes: 11/' entry.yaml; cd ../..; python tools/entry.py check entries/clark-2026 | tail -2; date -u
```

```
0 error(s)
Thu Nov 26 17:22:34 UTC 2026
```

**Agent**

Starting the full run now (estimated about 100 minutes; ends around 19:05 UTC).

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/clark-2026 2>&1 | tail -30; date -u
```

```
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
0 error(s)
pass  tuning_curves.ipynb  (894 s)
pass  network.ipynb  (1313 s)
pass  network_grid.ipynb  (480 s)
pass  theory.ipynb  (110 s)
pass  model_sims.ipynb  (1835 s)
Thu Nov 26 18:40:02 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
def show(nb, cells, tail=6000):
    d=json.load(open(f'executed/clark-2026/{nb}.ipynb'))
    for i in cells:
        print('####',nb,i)
        for o in d['cells'][i].get('outputs',[]):
            if 'text' in o: print(''.join(o['text'])[-tail:])
show('tuning_curves',[13,33])
show('theory',[5])
show('network_grid',[4],2500)
E
```

```
#### tuning_curves 13
tc_data.npz MD5 6e1f3a17ab67e2e0eb8fac35d89e2d57 listed 6e1f3a17ab67e2e0eb8fac35d89e2d57 match: True
cache: units 2691 head-direction 1533 sessions 31
cache session order equals ours: True
cache unit counts equal ours: True
cache hd labels equal ours: True | exc labels: True | fs labels: True
units compared: 1533
Pearson r of partition-averaged curves: min 1.000000, median 1.000000; fraction >= 0.99: 1.0000
max abs difference of partition-averaged curves (Hz): 1.4210854715202004e-14
max abs difference of plain curves (Hz): 0.0
chosen widths equal (==) for both partitions: 0.7841 of units; per partition: 0.8855
chosen widths equal to rounding (np.isclose, rtol 1e-9; the cache stores e.g. 0.09999999999999999 for 0.1): 1.0000 of units; per partition: 1.0000
where the widths differ, max abs curve difference: 2.1316282072803006e-14 | our width range there: (0.1, 93.26033468832199) | cache width range there: (0.09999999999999999, 93.260334688322)

#### tuning_curves 33
shortlist pass (25,000 samples) in 220 s: minimum at sigma 1.4211, b 1.7307, beta 2.7659, error 0.00613

seed 444120632: final pass (500,000 samples) best sigma 1.4737, b 1.2145, beta 3.1103, error 0.00894; at the paper's grid point 0.00947 (rank 2 of 30)

seed 444121632: final pass (500,000 samples) best sigma 1.4737, b 1.2145, beta 3.1103, error 0.00874; at the paper's grid point 0.00907 (rank 2 of 30)
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
def show(nb, cells, tail=7000):
    d=json.load(open(f'executed/clark-2026/{nb}.ipynb'))
    for i in cells:
        print('####',nb,i)
        for o in d['cells'][i].get('outputs',[]):
            if 'text' in o: print(''.join(o['text'])[-tail:])
show('network',[10],1500)
show('network',[13,19,22])
E
```

```
#### network 10
seed 944155936: median distance at 0 s 1.9661, 1 s 0.08163, 20 s 0.00068, 29.90 s 0.00062; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 77 of 100 bins (d) True; median movement 0.0025 rad
   median distance over time (s): {0.0: 1.96608, 0.1: 0.34276, 0.2: 0.20625, 0.3: 0.17919, 0.5: 0.1423, 1.0: 0.08163, 2.0: 0.02749, 5.0: 0.00122, 10.0: 0.0007, 20.0: 0.00068, 29.9: 0.00062}

seed 944156936: median distance at 0 s 1.9694, 1 s 0.08004, 20 s 0.00070, 29.90 s 0.00076; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 76 of 100 bins (d) True; median movement 0.0025 rad

seed 944157936: median distance at 0 s 1.9800, 1 s 0.08096, 20 s 0.00067, 29.90 s 0.00072; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 75 of 100 bins (d) True; median movement 0.0028 rad

seed 944158936: median distance at 0 s 1.9585, 1 s 0.07638, 20 s 0.00068, 29.90 s 0.00066; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 70 of 100 bins (d) True; median movement 0.0025 rad

seed 944159936: median distance at 0 s 1.9766, 1 s 0.07784, 20 s 0.00067, 29.90 s 0.00075; (a) True (b) False; angle moved under 2pi/20 between 1 s and the end: 1.00 (c) True; final angles in 77 of 100 bins (d) True; median movement 0.0028 rad
time 324 s

distance range 7.027345037573693e-05 2.1230659900698385

#### network 13
sorted: states (smoothing mode wrap, variant) single 24, greedy 25, bins 31
sorted: states single 24, greedy 25, bins 31; distinct peak neurons 41; peak height range 7.84 to 11.49

circulant: states (smoothing mode wrap, variant) single 2, greedy 39, bins 50
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
d=json.load(open('executed/clark-2026/model_sims.ipynb'))
for i,c in enumerate(d['cells']):
    if c['cell_type']!='code': continue
    print('####',i)
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[-9000:])
        if o.get('output_type')=='error': print('ERR')
E
```

```
#### 1
#### 2
X, Phi (500, 2500) | J (2500, 2500) | diagonal of J zero: True
input currents: mean -0.011, sd 1.002 (the process has unit variance); firing rates range 0.000 to 2.000 (1 + erf, bounded by 0 and 2)
reconstruction error mean((X - Phi J^T)^2) 2.585e-10

#### 4
seed 4129464829: Gaussian doublet 1 radius 0.8011 (cv 0.0059, largest angle gap 0.359), doublet 2 radius 0.0121 (collapse True); mixture radii 0.5587 (cv 0.0063, gap 0.375) and 0.5711 (cv 0.0029, gap 0.381), rings True True; mixture angle drift at most 0.312 and 0.239 rad
seed 4129465829: Gaussian doublet 1 radius 0.7940 (cv 0.0057, largest angle gap 0.452), doublet 2 radius 0.0116 (collapse True); mixture radii 0.5682 (cv 0.0072, gap 0.558) and 0.5676 (cv 0.0094, gap 0.545), rings True True; mixture angle drift at most 0.368 and 0.406 rad

seed 4129466829: Gaussian doublet 1 radius 0.8000 (cv 0.0035, largest angle gap 0.315), doublet 2 radius 0.0206 (collapse True); mixture radii 0.5699 (cv 0.0071, gap 0.552) and 0.5730 (cv 0.0153, gap 0.438), rings True True; mixture angle drift at most 0.433 and 0.652 rad
seed 4129467829: Gaussian doublet 1 radius 0.7998 (cv 0.0022, largest angle gap 0.325), doublet 2 radius 0.0138 (collapse True); mixture radii 0.5728 (cv 0.0107, gap 0.517) and 0.5660 (cv 0.0066, gap 0.492), rings True True; mixture angle drift at most 0.535 and 0.416 rad

seed 4129468829: Gaussian doublet 1 radius 0.7985 (cv 0.0022, largest angle gap 0.353), doublet 2 radius 0.0239 (collapse True); mixture radii 0.5689 (cv 0.0067, gap 0.478) and 0.5621 (cv 0.0067, gap 0.561), rings True True; mixture angle drift at most 0.347 and 0.389 rad
      seed                     eig_gauss                        eig_mix  max_rel_diff  within_5pct  dynamics_as_described
4129464829   [102.72, 97.48, 25.4, 24.7]    [97.4, 96.55, 25.97, 25.79]        0.0518        False                   True
4129465829 [102.18, 98.28, 25.25, 24.54]   [99.72, 96.02, 25.81, 24.23]        0.0241         True                  
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python -c "
import json
for nb,cells in [('network',[14,20,23]),('network_grid',[5]),('theory',[6])]:
    d=json.load(open(nb+'.ipynb'))
    for i in cells: print('---',nb,i);print(''.join(d['cells'][i]['source']))
"
```

```
--- network 14
**Result: partially reproduced.** The circulant plus scrambled residuals collapses to 4 states (2
to 7 over five seeds; the symmetric version to 2), and the circulant matrix's 100 final states are
exact shifts of one another (correlation 1.0000). The sorted optimal matrix keeps 24, 25 or 31
states under the three merging readings, short of the criterion's 50; its initial states already
give only 24 to 33 under this position measure, so the 50 cannot be reached by it. With the
position read as the manifold angle of the nearest target point (variant), the sorted matrix keeps
all 50 bins of 2 pi / 50, at a median distance of 0.0008 from the manifold, and the circulant plus
noise 7. The contrast between the optimal matrix and the circulant plus noise holds.
--- network 20
**Result: reproduced.** The leading 10 eigenvalues have imaginary parts at most 6.8% of their real
parts. After setting aside the fifth (1.0894, whose eigenvector is closest to uniform), the four
leading pairs have gaps of 0.027, 0.000, 0.0002 and 0.000 within, each smaller than the gap to the
next pair (0.139, 0.183, 0.036, 0.0002); the first pair (1.4384 and 1.4113) is not exact.
--- network 23
**Result: partially reproduced.** Every final state is on the manifold at the resolution of the
fig2ef reference (largest final distance 0.0015 against 2 at the start of fig2ef), with none
elsewhere, and at standard deviation 1 all 34 final angles fall in one state (1.69 to 1.70 rad),
under all five seeds. The criterion's threshold, the largest distance at 20 s in fig2ef (0.00132),
is met by 91% to 100% of final states, below the 95% asked at standard deviations 10, 50 and 1000
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/md_edits.py <<'PYEOF'
import json, sys
E = {}
E[('tuning_curves', 14)] = """**Result: reproduced.** The record's MD5 matches, and the cache has the same session order, unit
counts and labels as the files. All 1,533 recomputed partition-averaged curves correlate at r =
1.000000 with the cached ones (largest absolute difference 1.4e-14 Hz). The chosen widths are
equal to rounding (np.isclose) for both partitions in all units (1.0000); compared with == they
agree in 78% of units only because the cache stores values such as 0.09999999999999999 where the
grid here has 0.1."""
E[('tuning_curves', 34)] = """**Result: partially reproduced.** With the final pass of 500,000 samples the minimum is at sigma
1.4737, b 1.2145, beta 3.1103 under all five seeds: sigma (1.42 within 0.142) and beta (2.77
within 0.345) match and b (1.73 within 0.173) does not. The paper's grid point (1.4211, 1.7307,
2.7659) is the minimum of the 25,000-sample shortlist pass and second in the final pass under
every seed (0.00907 to 0.01006, against 0.00853 to 0.00894 for the chosen point). Taking the 90
best shortlist points to 500,000 samples changes nothing (the best of points 31 to 90 has error
0.01796). A float32 final pass over the 30 points also puts the chosen point first (0.00889
against 0.00916). In the paper's own cached error grid the two points are 1.1% apart (0.00890 at
the paper's point, 0.00900 at the chosen one): the surface has two near-equal minima along a
ridge in b and beta, and which wins depends on the draws and the arithmetic."""
E[('network', 14)] = """**Result: partially reproduced.** The circulant plus scrambled residuals collapses to 4 states (2
to 7 over five seeds; the symmetric version to 2), and the circulant matrix's 100 final states are
exact shifts of one another (correlation 1.0000). The sorted optimal matrix keeps 24, 25 or 31
states under the three merging readings (24 to 26 and 31 to 32 over five seeds), short of the
criterion's 50; its initial states already give only 24 to 33 under this position measure, so the
50 cannot be reached by it (a question for a reader). Wrap-mode smoothing gives the same counts.
Read on the manifold angle, the sorted matrix keeps the continuum: each trajectory's angle moves
from its start by a median of 0.0050 rad (largest 0.0565, all under 2 pi / 50), the final angles
fill all 50 bins of 2 pi / 50 under all five seeds, at a median distance of 0.0008 from the
manifold, and the circulant plus noise fills 7. The contrast between the optimal matrix and the
circulant plus noise holds."""
E[('network', 20)] = """**Result: reproduced.** The leading 10 eigenvalues have imaginary parts at most 6.8% of their real
parts. After setting aside the fifth (1.0894, whose eigenvector is closest to uniform), the four
leading pairs have gaps of 0.027, 0.000, 0.0002 and 0.000 within, each smaller than the gap to the
next pair (0.139, 0.183, 0.036, 0.0002); the first pair (1.4384 and 1.4113) is not exact. The
evidence is weaker than the count: pairs 2 and 4 are complex conjugates, equal in real part by
construction, so 2 of the 4 passing pairs are not conjugates; eigenvectors 5 to 7 tie in their
overlap with the uniform vector (0.041), and setting aside the sixth or the seventh in place of the
fifth also passes 4 of 4 (2 and 1 of them not conjugates)."""
E[('network', 23)] = """**Result: reproduced (resting on an assumption).** Every final state is on the manifold at the
resolution of the reference (largest final distance 0.0015, against median starting distances of
1.6 to 700), with none elsewhere, and at standard deviation 1 all 34 final angles fall in one state
(1.69 to 1.70 rad), under all five seeds. Against the fig2ef protocol run with the same 5-ms step
(largest distance at 20 s 0.00141), 97% to 100% of final states are within at every standard
deviation, under all five seeds. Against the 1-ms fig2ef threshold (0.00132), the variant, 91% to
100% are within, below 95% at standard deviations 10, 50 and 1,000 under the claim's seed (0.94,
0.91, 0.94); the final distances sit at the network's resolution, about 1e-3, where the step of
the reference decides the test."""
E[('network_grid', 5)] = """**Result: partially reproduced.** At c 0 some runs diverge at every lambda up to 1e-4 (1 to 4 of
100), and under reading (ii) of collapse nearly all others fall to the homogeneous state (96 to
100 of 100, radius 0.65 to 0.80 against 39 for the manifold) at every lambda; under reading (i) no
run collapses, since the homogeneous state keeps a firing-rate norm of 17.3 to 17.7. No c above 0
diverges up to lambda 1e-4, and c 0.25 still leaves the collapse (12 of 20 at lambda 1e-8 under
reading ii). At lambda 1e-2 the manifold is lost for c up to 0.75 (all 20 collapse under reading
ii), but at c 1 the states keep a radius of 4.6, just above the collapse threshold of 3.9, so the
criterion's test at c 1 fails. The flow error rises at large lambda (2.1e-2 at 1e-2) and at small
lambda from 1.3e-10 at 1e-10 to 3.6e-9 at 1e-12, but 1e-8 (1.7e-8) is not below 1e-12, so that
part of the criterion fails too. The paper's cached flow errors agree to three digits from 1e-10
to 1e-2 (3.8e-9 at 1e-12) and fail the same part: the supplement says only that 1e-8 sits just
above the minimum, which holds, and this reading of the criterion is asked of a reader."""
E[('theory', 6)] = """**Result: reproduced.** All twelve interaction profiles of Fig. 7a are positive at 0 (4.9 to 38.5)
and negative at some offset (minimum -1.5 to -6.0). Over the 40 by 20 grid the bump's second
eigenvalue is negative at every point (largest -4.7e-8, effectively zero at some points) and the
uniform state's leading eigenvalue is real and positive at every point (smallest 4.7e-5). With Q
fixed the bump at sigma 1.4211 and beta 2.7659 has a positive eigenvalue (0.446). At 293 of the 800
grid points no zero eigenvalue is found at the bump (the leading one is below -1e-6, down to
-0.22), mostly at small beta and large sigma; the bump there is not flat (amplitude, max - min of
m, median 0.95, below 1e-3 at only 6 of them), so its missing zero mode is not explained by a
vanishing bump. The criterion tests only the second eigenvalue."""
E[('model_sims', 5)] = """**Result: partially reproduced.** The dynamics differ as the legends describe under all five seeds:
with Gaussian loadings the final states form a ring in the dominant doublet (radius 0.80, radii
varying by at most 0.6%, largest angle gap 0.32 to 0.45 rad) and collapse in the subdominant one
(radius 0.012 to 0.024, below one tenth of 0.80); with mixture loadings both doublets form rings
(radii 0.56 to 0.57, the mean-field prediction 0.5642 and 0.5636). The eigenvalues of the two
matrices agree within 5.2% under the claim's seed, just outside the 5% asked (5.18%; 2.4% to 5.2%
over the five seeds, within 5% under two), so that part fails narrowly. The two ensembles share
their second moments (population eigenvalues 100, 100, 25 and 25), and each finite matrix
deviates from them by sampling; the paper's own seed-42 matrices agree within 3.3%."""
E[('model_sims', 9)] = """**Result: reproduced (resting on an assumption).** In the 2,500-neuron network, from every initial
spread (standard deviation 1 to 1,000, median starting distance 1.2 to 1.3) at least 97% of final
states lie within the threshold of the network's own fig2ef-protocol run (largest distance at 20
s 0.0112), none diverges, and all lie within twice it. At N 1,000 all 34 perturbed initial
conditions end within that threshold (largest final distance 0.0106), and the final angles keep 28
of 50 bins. Smaller networks converge less reliably: at N 50 only 6% to 21% of states end within
the threshold over the five seeds. Under four more seeds one (the fourth) falls below 95% at
standard deviation 50 (0.94) and at N 1,000 (0.94); the others hold."""
E[('model_sims', 12)] = """**Result: reproduced (resting on an assumption).** Without weight noise both networks keep all 34
states (34 under every merging reading, median drift 0.013 rad for the disordered network and
0.025 for the circulant one). At noise 0.4 neither does: the disordered network ends in 8 states
and the circulant in 9 (4 to 8 and 9 to 12 over five seeds). The two fragment alike over the whole
range, from 13 to 15 and 11 states at 0.2 to 4 and 8 at 1.0, with median drifts of 0.29 to 0.47
rad and 0.16 to 0.30 rad. Both already fragment at noise 0.2, which the criterion does not test."""
E[('model_sims', 14)] = """## Summary

| claim | outcome |
|---|---|
| figs1-s2-spectrum-does-not-fix-symmetry | partially reproduced (seed sensitive) |
| figs11-s12-global-stability-model | reproduced (assumed, seed sensitive) |
| figs10-robustness-comparable | reproduced (assumed) |
| fig8-grid-scores-and-torus | blocked (too large) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Differences from the paper's method. The paper's torch simulations are repeated in numpy
float32; every random draw comes from the claim's seed, not numpy seeds 42 and 123; the rank-four
products J tanh(x) are taken through the loadings, and the eigenvalues through the 4 by 4 Gram
matrix, which are the same quantities. The thresholds for convergence (figs11-s12) and for a
continuum (figs10) are this attempt's assumptions, stated in each section."""
E[('network', 24)] = None   # summary table: patched below
paths = sys.argv[1:]
for (nb, i), text in E.items():
    for root in paths:
        p = f"{root}/{nb}.ipynb"
        d = json.load(open(p))
        c = d['cells'][i]
        assert c['cell_type'] == 'markdown', (p, i)
        s = ''.join(c['source'])
        if text is None:
            s = s.replace("| figs11b-data-network-global-stability | partially reproduced |", "| figs11b-data-network-global-stability | reproduced (assumed) |")
        else:
            assert s.startswith("**Result") or s.startswith("## Summary"), (p, i, s[:30])
            s = text
        c['source'] = s.splitlines(keepends=True)
        open(p, 'w').write(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
print("ok")
PYEOF
python $TMPDIR/md_edits.py entries/clark-2026 executed/clark-2026
```

```
ok
```

**Agent calls Bash**

```bash
date -u; cd  python - <<'E'
import json
s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']['properties']; print(list(o))
print(json.dumps(s['properties']['findings']['items'].get('properties',{}).keys().__repr__()))
E
grep -n "round\|verif" tools/entry.py | sed -n 1,40p
```

```
Thu Nov 26 18:41:33 UTC 2026
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
"dict_keys(['kind', 'statement', 'found', 'about', 'severity', 'datasets'])"
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
35:`handover` builds what a verifier is given in its first round
408:        # A verification round's review of a finding points at the finding by its number in the record.
409:        for r, rnd in enumerate(attempt.get("verifications") or [], 1):
412:                    report.error(where, f"verification round {r} reviews finding {item['finding']}, and the record "
414:        # The latest round that reviewed a claim decides it; a third round may review only some. Round 1
415:        # does not bind: the revision after it may change outcomes, and round 2 reviews them.
417:        for rnd in (attempt.get("verifications") or [])[1:]:
436:            verified = agreed.get(outcome.get("claim"))
437:            if verified and outcome.get("outcome") != verified:
439:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
440:                                    "and verify it in another round")
660:        seconds = round(time.time() - started)
675:            "entry": entry["name"], "hash": entry_hash(entry_dir), "finished": round(time.time()),
684:    """The notebook without the author's conclusions, for a verifier's first round."""
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
p = 'attempts/clark-2026-01.yaml'
r = yaml.safe_load(open(p))
O = {o['claim']: o for o in r['outcomes']}

# ---- inputs
r['inputs'][0]['what'] = ("The paper's cached tuning curves, mouse_data/tc_data.npz of the record's tar "
  "symmetries_caches_v1.tar, read by range requests and checked against the record's CHECKSUMS.md5 (MD5 "
  "6e1f3a17ab67e2e0eb8fac35d89e2d57), used by the link claim tuning-curves-match-cache. Two more members of the same "
  "tar, read the same way and checked against their MD5, are used only as variants for comparison: "
  "grid_search_results.npz (the paper's error grid of the Fig. 4 fit, MD5 a48c2eb26c3a6a095d901938dc63efc1) in "
  "fig4-generative-fit, and pc_convergence_grid.npz (its err_grid, the flow error by lambda, MD5 "
  "60476aacc7f2eb2000a7c718846f46fc) in figs8-s9-lambda-and-c.")
r['inputs'][1]['what'] = ("The paper's code (package ring and its notebooks), read for every method detail and repeated in "
  "numpy in hdring.py; ring/dmft.py is copied as ring_dmft.py without its torch imports (MIT licence). The "
  "simulation-only claims (data elsewhere) run this code, in theory.ipynb and model_sims.ipynb.")

# ---- outcomes
o = O['tuning-curves-match-cache']
o['notes'] = ("The cache's session order, unit counts and three label columns equal the files'. All 1,533 recomputed "
  "partition-averaged curves correlate with the cached ones at r = 1.000000 (largest absolute difference 1.4e-14 Hz; "
  "plain curves identical). The chosen smoothing widths are equal to rounding (np.isclose, rtol 1e-9) for both "
  "partitions in every unit; an exact comparison (==) gives 78.4% of units only because the cache stores values such "
  "as 0.09999999999999999 where the grid here has 0.1. The labels in the files match the paper's per-unit table, and "
  "the dataset's measures match the cached values unit by unit.")
o = O['fig4-generative-fit']
o['notes'] = ("The final pass (500,000 samples) puts the minimum at sigma 1.4737, beta 3.1103, b 1.2145 under all five "
  "seeds (errors 0.0085 to 0.0089). Sigma and beta are within tolerance (beta by 0.34 of 0.345); b is 0.52 from 1.73, "
  "outside 0.173. The paper's grid point (sigma 1.4211, b 1.7307, beta 2.7659) is the minimum of the 25,000-sample "
  "shortlist pass (error 0.0061) and second in the final pass under every seed (0.00907 to 0.01006). Taking the 90 best "
  "shortlist points to 500,000 samples under the claim's seed gives the same minimum (the best of points 31 to 90 has "
  "error 0.0180). A float32 final pass over the 30 points (draws and transform in float32, as the paper's torch run) "
  "also ranks the chosen point first (0.00889 against 0.00916); evaluated at the two points alone, float32 favours the "
  "paper's point under the claim's seed (0.00902 against 0.00920) and the chosen one under the other four. In the "
  "paper's own cached error grid (grid_search_results.npz, same grid) the paper's point is the minimum (0.00890) and "
  "the chosen point second (0.00900), 1.1% apart. The error surface has two near-equal minima along a ridge in b and "
  "beta, and which wins depends on the draws and the arithmetic; the claims file's tolerance does not cover the "
  "second one. The fig5 claims are tested at both parameter sets and give the same outcomes.")
o = O['fig2gi-circulant-noise-collapses']
o['notes'] = ("The circulant plus scrambled residuals ends in 4 states under all three merging readings (2 to 7 over five "
  "seeds; the symmetric version 2), and the circulant's 100 final states are exact shifts (correlation 1.0000 with "
  "the best shift of the first). The sorted optimal matrix keeps 24 (single linkage), 25 (greedy) or 31 (bins) "
  "states, short of 50, and 24 to 26 and 31 to 32 under the five seeds of the initial noise. The position measure the "
  "criterion fixes (peak neuron of the smoothed currents) gives only 24 to 33 states even for the 100 initial states, "
  "so 50 is out of its reach; this is asked of a reader (questions/clark-2026.yaml), since Fig. 2g plots the steady "
  "states against the manifold coordinate. Smoothing in wrap mode in place of the default reflect mode (the paper's "
  "plotting code uses the default) gives the same counts. Read on the manifold angle of the nearest target point, the "
  "sorted matrix keeps the continuum: each trajectory's angle moves from its start by a median 0.0050 rad (largest "
  "0.057, all under 2 pi / 50), the final angles fill all 50 bins under all five seeds, at a median distance of 0.0008 "
  "from the manifold, while the circulant plus noise fills 7 and the circulant 47. The contrast between the optimal "
  "matrix and the circulant plus noise holds, which the criterion rates partial.")
o['deviations'][1] = ("The residual shuffle and initial noise come from the claim's seed (numpy seed 42 in the paper). "
  "The seed check reruns the circulant plus noise matrix (shuffle and initial noise) and the sorted matrix (initial "
  "noise), the parts with random draws.")
o = O['figs14-data-spectrum-doublets']
o['notes'] = ("The leading 10 eigenvalues have |Im| at most 6.8% of Re. Setting aside the fifth (1.0894, the eigenvector "
  "closest to uniform), the gaps within the first four pairs (0.027, 0.000, 0.0002, 0.000) are each below the gap to "
  "the next pair (0.139, 0.183, 0.036, 0.0002); the first pair (1.4384, 1.4113) is not exact. The evidence is weaker "
  "than the count: pairs 2 and 4 are complex conjugates, equal in real part by construction, so only pairs 1 and 3 are "
  "doublets of distinct real eigenvalues; eigenvectors 5 to 7 tie in their overlap with the uniform vector (0.041 "
  "each), and setting aside the sixth or the seventh also passes 4 of 4 pairs (2 and 1 of them not conjugates). "
  "Without setting one aside, two of the four pairs pass. The criterion as written is met.")
o['deviations'][0] = ("The unpaired eigenvalue is identified as the one whose eigenvector overlaps most with the uniform "
  "vector (the constant mode, as the criterion says), a standard choice; eigenvectors 5 to 7 tie, and each is set "
  "aside in turn as a variant, with the same outcome.")
o = O['figs11b-data-network-global-stability']
o['outcome'] = 'reproduced'
o['assumed'] = True
o['notes'] = ("From every initial spread (standard deviation 1 to 1,000, median starting distance 1.6 to 700) all 34 final "
  "states lie within 0.0016 of the manifold, with none elsewhere, and at standard deviation 1 all 34 end in one state "
  "(1.69 to 1.70 rad), under all five seeds. The threshold the criterion names, the distance reached at 20 s in "
  "fig2ef, is taken from the fig2ef protocol (its seed and its 100 noisy starts) run with the 5-ms step of these runs "
  "(largest distance at 20 s 0.00141); against it 97% to 100% of final states are within at every standard deviation "
  "under all five seeds. Against the 1-ms fig2ef run (largest 0.00132), the reading of round 1, 91% to 100% are "
  "within, below 95% at standard deviations 10, 50 and 1,000 under the claim's seed (0.94, 0.91, 0.94); against its "
  "median (0.00068) 29% to 65%. The final distances sit at the network's resolution, about 1e-3, where the step of the "
  "reference decides the test.")
o['deviations'] = [("The threshold is the largest distance at 20 s of the fig2ef protocol run with the 5-ms step of "
  "spurious_fixed_points.ipynb, not of the fig2ef run itself (1-ms step, as data_driven_attractor.ipynb). The claims "
  "file leaves the threshold open; a reference on the same integrator as the runs it judges is assumed, since the 1-ms "
  "run sits slightly closer to the targets and the final distances are at the network's resolution. The 1-ms "
  "thresholds (largest and median) are shown as variants and fail the 95% at three standard deviations.")]
o = O['figs8-s9-lambda-and-c']
o['notes'] = o['notes'].replace("The flow error is 2.6e-9, 1.3e-10,", "The flow error is 3.6e-9, 1.3e-10,")
o['notes'] = o['notes'].replace("so that part of the\n    criterion fails.", "so that part of the criterion fails.")
o['notes'] += (" The paper's cached flow errors (err_grid of pc_convergence_grid.npz) agree to three digits from 1e-10 to "
  "1e-2 and give 3.8e-9 at 1e-12, so the same part fails on the paper's numbers; the supplement says only that 1e-8 "
  "sits just above the minimum, which holds, and whether the criterion misreads it is asked of a reader "
  "(questions/clark-2026.yaml).")
o = O['fig7-dmft-mexican-hat-and-stability']
o['notes'] = ("All twelve profiles of Fig. 7a are positive at 0 (4.9 to 38.5) and negative at some offset (minimum -1.5 to "
  "-6.0). On the 40 by 20 grid the bump's second eigenvalue is negative everywhere (largest -4.7e-8, effectively zero "
  "at some points) and the uniform state's leading eigenvalue is real (|Im| below 1e-16) and positive everywhere "
  "(smallest 4.7e-5). With Q fixed, the bump at sigma 1.4211 and beta 2.7659 has eigenvalue 0.446. At 293 of 800 grid "
  "points, mostly small beta and large sigma, no zero eigenvalue is found at the bump (the leading one is below -1e-6, "
  "down to -0.22); the bump there is not flat (amplitude, max - min of m, median 0.95, below 1e-3 at 6 of the 293), so "
  "the missing zero mode is not explained by a vanishing bump. The criterion tests only the second eigenvalue.")
o = O['fig8-grid-scores-and-torus']
o['notes'] = ("Not started. The network of 25,000 neurons needs a 25,000 by 25,000 weight matrix (5 GB in float64) fitted "
  "by regression and simulated, and the grid-score sweep 1,000 maps for each eta; with the five notebooks of this "
  "entry taking 77 minutes per run, it did not fit in the five hours of the revision run either.")
o = O['figs10-robustness-comparable']
for k in ('blocked_by',): o.pop(k, None)
o.update(outcome='reproduced', notebook='model_sims.ipynb', output='claim:figs10-robustness-comparable', assumed=True,
  measured=[34, 34, 8, 9])
o['notes'] = ("Without weight noise both networks keep all 34 states under every merging reading (median drift 0.013 rad "
  "for the disordered network, 0.025 for the circulant). At noise 0.4 the disordered network ends in 8 states and the "
  "circulant in 9 (4 to 8 and 9 to 12 over five seeds), so neither keeps a continuum. Final states for each noise "
  "level 0, 0.2, 0.4, 0.6, 0.8 and 1.0 (bins), disordered 34, 15, 8, 8, 6, 4 and circulant 34, 11, 9, 12, 9, 8, with "
  "median drifts of 0.29 to 0.47 rad and 0.16 to 0.30 rad from noise 0.2 on; the two fragment alike, and both already "
  "at 0.2, which the criterion does not test. Measured gives the states at noise 0 (disordered, circulant) and at 0.4.")
o['deviations'] = [
  ("A network keeps a continuum when at least 31 of its 34 final angles (90%) remain distinct states under all three "
   "merging readings of fig2gi (within 2 pi / 50). The criterion does not say how many states make a continuum among 34 "
   "initial conditions spaced 2 pi / 34 apart; this is assumed. The counts are given for each level, and at 0 and 0.4 "
   "they are far from the threshold (34 against 8 and 9)."),
  ("Draws from the claim's seed (the paper's numpy seed 123); the seed check reruns noise 0.4, the level the criterion "
   "reads for fragmentation, with a new network, initial noise and weight noise for each seed."),
  "Simulated in numpy float32 (the paper's torch float32); the angle read at 0, 30, 60 and 90 s and at the end (119.995 s)."]
o = O['figs11-s12-global-stability-model']
o.pop('blocked_by', None)
o.update(outcome='reproduced', notebook='model_sims.ipynb', output='claim:figs11-s12-global-stability-model', assumed=True,
  seed_sensitive=True, measured=[1.0, 1.0])
o['notes'] = ("At N 2,500 the fraction of final states within the threshold (the largest distance at 20 s of the network's "
  "own fig2ef-protocol run, 0.0112) is 1.00, 0.97, 1.00, 1.00 and 1.00 at standard deviations 1, 10, 50, 100 and 1,000, "
  "none diverges, and all are within twice the threshold; from median starting distances of 1.2 to 1.3. At N 1,000 all "
  "34 perturbed initial conditions end within that threshold (largest final distance 0.0106). Smaller networks converge "
  "less reliably: at N 50, 6% to 21% within over the five seeds, at N 100 53% to 100%. Under the four other seeds the "
  "N 2,500 test holds for three; the fourth gives 0.94 at standard deviation 50, and 0.94 at N 1,000. Measured gives "
  "the smallest fraction within at N 2,500 rounded (0.97 to 1.0) and the fraction at N 1,000.")
o['measured'] = [0.97, 1.0]
o['deviations'] = [
  ("Judged as in figs11b, whose threshold comes from a fig2ef run on the same network: here the fig2ef protocol (100 "
   "regularly spaced manifold points plus noise of standard deviation 3, 5-ms step, 30 s) is run on the 2,500-neuron "
   "generative network itself, and its largest distance at 20 s is the threshold. For N 1,000 and the smaller networks "
   "the same fixed normalized threshold is used, since each N's own reference run is nearly the protocol it would judge; "
   "the own thresholds are shown as a variant (all 34 within at N 1,000). This is assumed."),
  ("Draws from the claim's seed (the paper's numpy seed 42); the distance to the manifold is that of the firing rates to "
   "the nearest of the 500 target points, over sqrt(N), as figs11b.")]
o = O['figs1-s2-spectrum-does-not-fix-symmetry']
o.pop('blocked_by', None)
o.update(outcome='partially_reproduced', notebook='model_sims.ipynb', output='claim:figs1-s2-spectrum-does-not-fix-symmetry',
  seed_sensitive=True, measured=[0.0518])
o['notes'] = ("The dynamics differ as the legends describe under all five seeds. With Gaussian loadings the final states "
  "form a ring in the dominant doublet (radius 0.80, coefficient of variation at most 0.006, largest angle gap 0.32 to "
  "0.45 rad) and collapse in the subdominant one (radius 0.012 to 0.024, below one tenth of the ring radius); with mixture "
  "loadings both doublets form rings (radii 0.56 to 0.57; the notebook's mean-field prediction 0.5642 and 0.5636, "
  "largest angle drift 0.24 to 0.65 rad). The four nonzero eigenvalues of the two matrices differ by at most 5.18% under "
  "the claim's seed (Gaussian 102.72, 97.48, 25.40, 24.70; mixture 97.40, 96.55, 25.97, 25.79), just outside the 5% "
  "asked, and by 2.4% to 5.2% over the five seeds (within 5% under two). The two ensembles share their second moments "
  "(population eigenvalues 100, 100, 25, 25) and each finite matrix deviates from them by sampling; the paper's own "
  "seed-42 matrices agree within 3.3%. The dynamics part holds and the eigenvalue part fails narrowly.")
o['deviations'] = [
  ("The nonzero eigenvalues of J = M M^T / N are computed as those of the 4 by 4 matrix M^T M / N, which are the same, and "
   "J tanh(x) as M (M^T tanh(x)) / N."),
  ("A doublet forms a ring when its 40 final radii vary by less than 10% and their angles leave no gap wider than 2 pi / "
   "10, a standard choice (the values are far from both limits); collapse as the claims file fixes it."),
  "Draws from the claim's seed (the paper's numpy seed 42); the paper's seed-42 matrices are shown as a variant."]

# ---- findings
r['findings'][2]['statement'] = ("The generative fit of Fig. 4 has two near-equal minima on the paper's grid, (sigma, b, "
  "beta) = (1.4211, 1.7307, 2.7659) and (1.4737, 1.2145, 3.1103), whose errors differ by less than the sampling noise of "
  "500,000 samples (0.0085 to 0.0101 depending on the draws and on float32 or float64 arithmetic). In the paper's own "
  "cached error grid on Zenodo they are 1.1% apart (0.00890 and 0.00900). The reported b of 1.73 is one of two choices "
  "the fitting procedure can return.")
r['findings'][3]['statement'] = ("In the mean-field stability grid of Fig. 7d,e (dmft.ipynb, run_analysis), at 293 of the "
  "800 grid points, mostly beta below 0.1 or sigma near 100, the bump Jacobian has no zero eigenvalue (its leading "
  "eigenvalue is below -1e-6, down to -0.22), although the bump there is not flat (amplitude median 0.95). So at those "
  "points the analytic bump the code linearizes about does not show the symmetry-induced zero mode the Results describe.")
yaml.safe_dump(r, open(p, 'w'), sort_keys=False, width=100, allow_unicode=True)
print('ok')
PYEOF
python $TMPDIR/rec.py
```

```
ok
```

**Agent calls Bash**

```bash
cd  grep -n "2.6e-9\|3.6e-9" attempts/clark-2026-01.yaml; grep -n "rounded (0.97" attempts/clark-2026-01.yaml
```

```
308:    error is 3.6e-9, 1.3e-10, 1.7e-8, 4.6e-6, 4.9e-4 and 2.1e-2 from lambda 1e-12 to 1e-2; it rises at
422:    within at N 2,500 rounded (0.97 to 1.0) and the fraction at N 1,000.'
```

**Agent**

Now the verification round record.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/ver.py <<'PYEOF'
import yaml
p = 'attempts/clark-2026-01.yaml'
r = yaml.safe_load(open(p))
for o in r['outcomes']:
    if o['claim'] == 'figs11-s12-global-stability-model':
        o['notes'] = o['notes'].replace("Measured gives the smallest fraction within at N 2,500 rounded (0.97 to 1.0) and the fraction at N 1,000.",
                                        "Measured gives the smallest fraction within at N 2,500 and the fraction at N 1,000.")
NOCHANGE = "Outcome kept; nothing in the report bears on it beyond agreement."
R = [
 ('hd-cell-selection', True, 'reproduced', "Cell 10 shows 31 sessions, 2,691 units, 1,533 head-direction units under both readings, 0 dropped by nz_mask, 9 opto mice with 315 cells, and counts of 117/93/90/86 for the right mice.", NOCHANGE),
 ('tuning-curves-match-cache', True, 'reproduced', "Cell 12: Pearson r = 1.000000 for 100% of 1,533 units, largest curve difference 1.4e-14, and the cache's labels and session order equal the data's. Problem 2: the printed fraction of smoothing widths that match exactly (0.784) is wrong, as the comparison uses == on floats and the cache stores values like 0.09999999999999999 where the notebook has 0.1; np.isclose would give the real fraction.",
  "Outcome kept. The cell now also compares the widths with np.isclose (rtol 1e-9): they agree for both partitions in every unit (1.0000); the == fraction is kept and labelled, and the conclusion and notes now say the widths agree to rounding."),
 ('fig1e-heterogeneous-peaks', True, 'reproduced', "Cell 16: peak counts of 1 to 6 occur, and the interquartile range of the separation between the two highest peaks is 1.382 rad, above pi/4.", NOCHANGE),
 ('fig5d-peak-numbers', True, 'reproduced', "Cell 18: the data give exactly 1,533/412/55, and generative samples over five seeds give 23,908 to 24,267 curves with at least 2 peaks and 1,001 to 1,082 with at least 3, all within tolerance. Problem 8: the samples come from a numpy Generator, not the legacy seed 42, but all 5 seeds fall within tolerance.", "Outcome kept. The use of the claim's seed in place of the legacy seed 42 is already a recorded deviation."),
 ('fig1fg-mean-and-fluctuation-profiles', True, 'reproduced', "Cell 20: one maximum, at offset 0; symmetry r = 0.9998; sd/mean = 0.56, so both readings hold; median consistency r is 0.996 (mean) and 0.974 (sd).", NOCHANGE),
 ('fig3ab-centers-of-mass-uniform', True, 'reproduced', "Cell 22: 2 sessions with uncorrected P < 0.05, 0 after BH correction, corrected P from 0.592 to 0.968.", NOCHANGE),
 ('fig3c-correlation-approaches-circulant', True, 'reproduced', "Cell 24: the distance from circulant form falls monotonically for all 4 mice and both functions under all 5 seeds; the leading 4 eigenvectors have at least 0.89 Fourier purity, and eigenvectors 1 and 2 are at frequency 1.", NOCHANGE),
 ('fig4-generative-fit', True, 'partially_reproduced', "Cell 26: the 500k-sample pass chooses sigma 1.4737 and beta 3.1103, within tolerance, but b 1.2145, outside 1.73 +- 0.173, under all 5 seeds. Problem 1: the paper's point and the chosen one are a near-tie (0.0089 and 0.0095) along a ridge where b and beta trade off; the 25k shortlist with 30 re-evaluated points is the author's deviation, which probably did not change the outcome since both points were re-run at 500k; the float32 variant was run only at the two points and favours the chosen point in 4 of 5 seeds; the 500k error at the paper's point is shown for one seed only. It asked for that error under all 5 seeds, a float32 final pass over all 30 shortlisted points, and 500k errors for more than the top 30.",
  "Outcome kept. The cell now prints the 500k error at the paper's grid point under every seed (0.00907 to 0.01006, second of 30 each time, against 0.00853 to 0.00894 for the chosen point), takes the 90 best shortlist points to 500k under the claim's seed (same minimum; the best of points 31 to 90 has 0.0180), and runs a float32 final pass over all 30 (chosen point first, 0.00889 against 0.00916). As a further variant it reads the paper's own cached error grid from Zenodo (grid_search_results.npz): the paper's point is its minimum (0.00890) and the chosen point second (0.00900), 1.1% apart. Notes and finding 3 updated."),
 ('fig5ab-profiles-match', True, 'reproduced', "Cell 30: the profiles lie within the mouse range at 0.97 or more of offsets and the peaks differ by 3.0% (mean) and 1.3% (sd), at both the fitted and the paper's parameters.", NOCHANGE),
 ('fig5c-peak-counts-match', True, 'reproduced', "Cell 32: total variation is 0.022 at zthresh 1, 0.065 at 0.5 and 0.128 at 0; smallest at zthresh 1 and below 0.15.", NOCHANGE),
 ('fig5d-peak-heights-match', True, 'reproduced', "Cell 34, reading (a): the medians differ by 0.8%, 1.5% and 5.3% for the three peaks. Reading (b) fails for peak 3 (KS distance 0.186).", NOCHANGE),
 ('fig5e-flip-symmetry-match', True, 'reproduced', "Cell 36: the generative fraction in the tail is 1.19 times the data's below 0.5 and 1.14 times below 0, both within 1.5 times; medians 0.927 (data) and 0.834 (generative).", NOCHANGE),
 ('fig5f-information-match', True, 'reproduced', "Cell 38: the medians differ by 6.2% and the KS distance is 0.138, so both readings hold (KS only narrowly).", NOCHANGE),
 ('fig2l-recorded-bump-tracks-hd', True, 'reproduced', "Cell 40: reading (a) holds, with a median error of 0.168 rad against pi/8; reading (b) narrowly fails (circular r 0.896); applying each partition's curves to the other's spikes gives 0.172 and 0.177 rad. Problem 8: the curves are fitted on the same spikes they are tested on, and the cross-partition variant shows this does not matter.", "Outcome kept; the cross-partition variant was already in the notes."),
 ('fig2b-sorted-weights-mexican-hat', True, 'reproduced', "Network cell 7: the profile peaks at offset -8; 88% of intermediate offsets lie below the profile's mean, and 80% are negative.", NOCHANGE),
 ('fig2ef-data-network-quasicontinuous', True, 'reproduced', "Cell 9: readings (a) and (c) hold under all 5 seeds; the median distance falls from 1.97 at 0 s to 0.082 at 1 s, and the manifold angle moves a median 0.0025 rad. Reading (b) fails, because the distance keeps falling until about 5 s.", NOCHANGE),
 ('fig2gi-circulant-noise-collapses', True, 'partially_reproduced', "Cell 11: the circulant-plus-noise matrix ends in 2 to 7 states (at most 10 under all 5 seeds) and the circulant's final states are exact shifts; the sorted matrix ends in 24 to 31 states, short of 50, so the partial rule applies. Problem 3, a defect in the claims file: on 1,533 neurons 50 states merged within 31 neurons cannot be reached (a synthetic test of count_states on 103 evenly spaced positions gives 1, 35 and 50; the initial states give 24 to 33); the nearest-target variant is the author's own measure; the sorted matrix was run under one seed only; gaussian_filter1d uses reflect mode, not wrap, on a ring (problem 8). It asked for the initial-to-final angle shift of each sorted-matrix trajectory.",
  "Outcome kept, as tested on the claims file. The misreading is added to questions/clark-2026.yaml for a reader: Fig. 2g plots the steady states against the manifold coordinate, which supports placing states by manifold angle. Added the initial-to-final manifold-angle shift of each sorted-matrix trajectory (median 0.0050 rad, largest 0.057, all under 2 pi / 50; final angles in all 50 bins), the sorted matrix under the four other seeds (24 to 26 and 31 to 32 states on the criterion's measure, 50 of 50 bins on the manifold angle), and wrap-mode smoothing as a variant (same counts). The paper's plotting code uses the default mode, so the default is kept."),
 ('fig2jk-velocity-integration', True, 'reproduced', "Cell 13: the median error is 0.011 rad for the constant input and 0.013 rad for A3707's behaviour; circular r = 1.000 for both.", NOCHANGE),
 ('figs8-s9-lambda-and-c', True, 'partially_reproduced', "Network_grid cell 4: at c 0 there is divergence or collapse (reading ii) and no c > 0 diverges, but lambda 1e-2 at c 1 does not collapse (radius 4.6 against 3.9) and err(1e-8) = 1.7e-8 is not below err(1e-12) = 3.6e-9 (minimum at 1e-10). Problem 4: the criterion's err(1e-8) < err(1e-12) is stricter than Supplementary Note 3, section 8.4, which says 1e-8 sits just above the minimum, and the output fits the paper's wording, a claims-file misreading; reading (i) cannot detect collapse, as the collapsed state has norm about 17, and reading (ii) is the sensible one; 34 of the 42 grid points ran 20 initial conditions, not 100. It asked for 100 initial conditions everywhere and the paper's cached flow errors per lambda.",
  "Outcome kept, as tested on the claims file. The misreading is added to questions/clark-2026.yaml. The cell now reads the paper's err_grid (pc_convergence_grid.npz on Zenodo): it matches to three digits from 1e-10 to 1e-2 and gives 3.8e-9 at 1e-12, so the same part fails on the paper's numbers. The notes gave 2.6e-9 at 1e-12, a slip; they now give 3.6e-9, as printed. The 100 initial conditions at every point were not run: with the new claims added in this revision the entry's run had to stay under two hours, and the grid was kept as in round 1 (100 at the eight points the criterion reads)."),
 ('figs11b-data-network-global-stability', True, 'partially_reproduced', "Cell 17: at standard deviation 1 every final state merges into 1 state, but at several standard deviations only 91 to 94% of final states fall within the largest fig2ef distance at 20 s, against 95%. Problem 5: that threshold comes from 100 fig2ef runs at 20 s with a 1-ms step and is compared with 34 runs at 30 s with a 5-ms step, a comparison against the noise floor (final maxima 0.00118 to 0.00154 against 0.00132); with 34 runs the 95% rule fails as soon as 2 exceed it, so pass or fail is close to chance. It asked for the fig2ef distance with a 5-ms step as a reference on the same footing, and the initial distances.",
  "Outcome changed to reproduced, resting on an assumption. The threshold assumed in round 1 was not on the footing of the runs it judged, so it was revised: the fig2ef protocol (its seed and 100 noisy starts) is now run with the 5-ms step of these runs, and its largest distance at 20 s (0.00141) is the threshold. Against it 97% to 100% of final states are within at every standard deviation under all five seeds. The 1-ms thresholds are kept as variants (fail at three standard deviations under the claim's seed), and the median initial distances are printed (1.6 to 700)."),
 ('figs14-data-spectrum-doublets', True, 'reproduced', "Cell 15: the largest |Im|/Re among the leading 10 is 0.068, and 4 of 4 pairs are tighter than the gap to the next pair. Problem 6: pairs 2 and 4 are complex-conjugate pairs, equal in real part by construction, so they count as doublets trivially; the eigenvalue set aside as the constant mode is an arbitrary pick, as eigenvectors 5 to 7 tie at a uniform overlap of 0.041; only pairs 1 and 3 are real evidence, so the criterion as written passes on weak evidence.",
  "Outcome kept, as the criterion is met as written. The cell now marks complex-conjugate pairs and sets aside each of eigenvalues 5, 6 and 7 in turn (4 of 4 pairs pass each time, 2, 2 and 1 of them not conjugates); the conclusion and notes say the evidence rests on pairs 1 and 3."),
 ('fig6cd-eigenvalues-real-degenerate', True, 'reproduced', "Theory cell 11, claim seed: the largest relative difference from equation (9) is 5.0%; eigenvalues are real and paired, and the 9th is the Fourier-0 mode. One of 5 seeds exceeds 10% (13.6%).", "Outcome kept; it was already marked seed_sensitive."),
 ('fig6fg-disordered-eigenvectors', True, 'reproduced', "Cell 13: the model's pair CVs are 0.52 to 0.53 (structureless) and the circulant's 0.063 to 0.072 (ring); both spectra have 4 of 4 doublets, under all 5 seeds.", NOCHANGE),
 ('fig7-dmft-mexican-hat-and-stability', True, 'reproduced', "Cell 5: all 12 profiles have a Mexican hat; the bump's second eigenvalue is below 0 and the uniform state's first above 0 at all 800 grid points; with Q fixed the leading eigenvalue is +0.446. Problem 7: at 293 of 800 grid points the bump Jacobian has no zero mode (eigenvalue 1 as low as -0.22), so a bump state is not shown to exist there; the largest second eigenvalue is -4.7e-8, effectively zero; the criterion checks only eigenvalue 2. It asked for the bump amplitude at the 293 points.",
  "Outcome kept. The cell now prints the amplitude (max - min of m) of the bump the Jacobian is taken at: median 0.95 at the 293 points without a zero mode (below 1e-3 at 6 of them), so the bump is not flat there. The conclusion, the notes and finding 4 say so, and that the largest second eigenvalue is effectively zero."),
 ('fig7de-dmft-timescales', True, 'not_reproduced', "Cell 7: 'a few tau' fails for both timescales (bump convergence up to 20.5 tau; uniform divergence down to 0.15 tau); 'decreasing' fails for the divergence time, and the max/min ratio over sigma reaches 24.3 for it.", NOCHANGE),
 ('fig7c-dmft-integrates-behavior', True, 'reproduced', "Cell 9: median error 0.0315 rad, circular r 0.998.", NOCHANGE),
 ('fig8-grid-scores-and-torus', False, None, "Not tested: no notebook cell, and the notebook points to an attempt record the verifier did not have. The claim needs only the paper's code, not the archive. Problem 9: it has no outputs in any notebook, so it has no outcome.",
  "Kept blocked (too_large): the 25,000-neuron network and the grid-score sweep do not fit the run's time. model_sims.ipynb now states the block in its own section."),
 ('figs10-robustness-comparable', False, None, "Not tested: no notebook cell, and the notebook points to an attempt record the verifier did not have. The claim needs only the paper's code, not the archive. Problem 9: it has no outputs in any notebook, so it has no outcome.",
  "Tested in the new notebook model_sims.ipynb, now reproduced, resting on an assumption (a continuum is at least 31 of 34 distinct states): both networks keep 34 states at noise 0, and at 0.4 end in 8 (disordered) and 9 (circulant), 4 to 8 and 9 to 12 over five seeds."),
 ('figs11-s12-global-stability-model', False, None, "Not tested: no notebook cell, and the notebook points to an attempt record the verifier did not have. The claim needs only the paper's code, not the archive. Problem 9: it has no outputs in any notebook, so it has no outcome.",
  "Tested in model_sims.ipynb, now reproduced, resting on an assumption (the threshold from the network's own fig2ef-protocol run) and seed sensitive: at N 2,500 97% to 100% of final states are within at every standard deviation and all at N 1,000, under the claim's seed; one of four other seeds gives 0.94 at standard deviation 50 and at N 1,000."),
 ('figs1-s2-spectrum-does-not-fix-symmetry', False, None, "Not tested: no notebook cell, and the notebook points to an attempt record the verifier did not have. The claim needs only the paper's code, not the archive. Problem 9: it has no outputs in any notebook, so it has no outcome.",
  "Tested in model_sims.ipynb, now partially reproduced and seed sensitive: the dynamics differ as described under all five seeds, but the eigenvalues of the two matrices differ by 5.18% under the claim's seed, just outside the 5% asked (2.4% to 5.2% over five seeds; the paper's seed-42 matrices 3.3%)."),
]
res = []
for claim, ag, out, reason, resp in R:
    d = dict(claim=claim, agrees=ag)
    if out: d['outcome'] = out
    d['reason'] = reason
    d['response'] = resp
    res.append(d)
assert len(res) == len(r['outcomes']) == len({x['claim'] for x in res})
assert {x['claim'] for x in res} == {o['claim'] for o in r['outcomes']}
r['verifications'] = [dict(date='2026-11-26', kind='agent',
  by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
  reviewed=("Round 1. The executed notebooks of the first run (tuning_curves, network, network_grid, theory) with the "
    "conclusion cells and the summaries removed, the helper modules and the claims file, with the paper; not the attempt "
    "record. The verifier checked the pinned version's assets through the archive API (31, 9 of them +ogen.nwb) and ran a "
    "synthetic test of count_states. It gave its own outcome for the 26 claims with outputs, all agreeing with the record "
    "as it then stood, and none for the four claims blocked for time, which had no outputs. Problems 3 and 4 report places "
    "where the claims file misreads the paper; both are added to questions/clark-2026.yaml and the claims are tested as "
    "the file has them. No finding was rated critical, so no finding was reviewed. Report in "
    "transcripts/clark-2026/verifier-1-report.md."),
  results=res)]
yaml.safe_dump(r, open(p, 'w'), sort_keys=False, width=100, allow_unicode=True)
print('ok')
PYEOF
python $TMPDIR/ver.py && python tools/entry.py check entries/clark-2026 2>&1 | tail -5; date -u
```

```
ok
0 error(s)
Thu Nov 26 18:43:35 UTC 2026
```

**Agent calls Bash**

```bash
cd  sed -i 's/is above that at 1e-12 (about 3e-9)/is above that at 1e-12 (3.6e-9)/' questions/clark-2026.yaml; grep -c "3.6e-9" questions/clark-2026.yaml; python - <<'E'
import yaml,json
from jsonschema import Draft202012Validator
s=json.load(open('schemas/attempt.schema.json'))
r=yaml.safe_load(open('attempts/clark-2026-01.yaml'))
errs=list(Draft202012Validator(s).iter_errors(r)); print('schema errors',len(errs)); [print(e.message[:200]) for e in errs[:5]]
E
grep -n "—\|rather" attempts/clark-2026-01.yaml questions/clark-2026.yaml entries/clark-2026/*.ipynb entries/clark-2026/README.md | head
```

```
1
schema errors 1
datetime.date(2026, 11, 26) is not of type 'string'
```

**Agent calls Bash**

```bash
cd entries/clark-2026; python - <<'E'
s=open('README.md').read()
rep=[("| Global stability of the data network (Supplementary Fig. 11b) | Partially reproduced |","| Global stability of the data network (Supplementary Fig. 11b) | Reproduced (assumed) |"),
("| Grid cells, weight noise, finite-N stability of the model, rank-four ensembles | Blocked: too large for the run's time |",
"| Weight-noise robustness, disordered and circulant (Supplementary Fig. 10) | Reproduced (assumed) |\n| Global and finite-N stability of the generative network (Supplementary Figs. 11a, 12) | Reproduced (assumed, seed sensitive) |\n| Spectrum does not fix the symmetry, rank-four ensembles (Supplementary Figs. 1, 2) | Partially reproduced (seed sensitive) |\n| Grid cells and the toroidal network (Fig. 8) | Blocked: too large for the run's time |"),
("- `theory.ipynb`: the mean-field theory and the large-N spectra (about 3 minutes).","- `theory.ipynb`: the mean-field theory and the large-N spectra (about 2 minutes).\n- `model_sims.ipynb`: the simulations of the generative-process and rank-four networks (about\n  31 minutes)."),
("(about 17 minutes, most of it the generative fit)","(about 15 minutes, most of it the generative fit)"),
("their dynamics (about 25 minutes)","their dynamics (about 22 minutes)"),
("- `network_grid.ipynb`: the lambda and c grid (about 9 minutes).","- `network_grid.ipynb`: the lambda and c grid (about 8 minutes)."),
]
for a,b in rep:
    if a not in s: print('MISSING',a[:60])
    s=s.replace(a,b)
open('README.md','w').write(s)
E
grep -n "network.ipynb\`" README.md; sed -i 's/runtime_minutes: 18$/runtime_minutes: 15/; s/runtime_minutes: 33$/runtime_minutes: 22/; s/runtime_minutes: 11$/runtime_minutes: 8/; s/runtime_minutes: 4$/runtime_minutes: 2/; s/runtime_minutes: 32$/runtime_minutes: 31/' entry.yaml; grep runtime entry.yaml
```

```
MISSING their dynamics (about 25 minutes)
45:- `network.ipynb`: the data-derived network, its weights, dynamics and spectrum (about 25 minutes).
  runtime_minutes: 15
  runtime_minutes: 22
  runtime_minutes: 8
  runtime_minutes: 2
  runtime_minutes: 31
```

**Agent calls Bash**

```bash
cd entries/clark-2026; sed -i 's/dynamics and spectrum (about 25 minutes)/dynamics and spectrum (about 22 minutes)/' README.md; cd ../..; python tools/entry.py check entries/clark-2026 | tail -2; python tools/entry.py handover entries/clark-2026 2>&1 | tail -2; git status --short | head -30
```

```
0 error(s)
wrote executed/clark-2026/handover
 M attempts/clark-2026-01.yaml
 M entries/clark-2026/README.md
 M entries/clark-2026/entry.yaml
 M entries/clark-2026/hdring.py
 M entries/clark-2026/network.ipynb
 M entries/clark-2026/network_grid.ipynb
 M entries/clark-2026/theory.ipynb
 M entries/clark-2026/tuning_curves.ipynb
 M tools/agent_run.py
 M tools/author_notes.py
 M tools/blind.sh
 M tools/build_site.py
 M tools/colab.py
 M tools/conversion_issue.py
 M tools/entry.py
 M tools/get_papers.sh
 M tools/notify.py
 M tools/paper_match.py
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git status --short | grep -v "^ M tools\|^?? tools\|^?? docs"; sed -n '/claim: figs1-s2/,/^- claim/p' attempts/clark-2026-01.yaml | head -40
```

```
M attempts/clark-2026-01.yaml
 M entries/clark-2026/README.md
 M entries/clark-2026/entry.yaml
 M entries/clark-2026/hdring.py
 M entries/clark-2026/network.ipynb
 M entries/clark-2026/network_grid.ipynb
 M entries/clark-2026/theory.ipynb
 M entries/clark-2026/tuning_curves.ipynb
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
?? entries/clark-2026/model_sims.ipynb
?? questions/clark-2026.yaml
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la --time-style=+%H:%M .bashrc .gitconfig .mcp.json scripts .idea .vscode 2>&1 | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 16:41 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 16:41 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 16:41 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 16:41 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 16:41 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 16:41 scripts
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
for root in ['entries/clark-2026','executed/clark-2026']:
    p=f'{root}/network.ipynb'; d=json.load(open(p)); c=d['cells'][24]; s=''.join(c['source'])
    old="come from each claim's seed."
    assert old in s
    s=s.replace(old,"come from each claim's seed; the threshold of figs11b comes from the fig2ef protocol run with the\n5-ms step of the runs it judges (assumption).")
    c['source']=s.splitlines(keepends=True)
    open(p,'w').write(json.dumps(d,indent=1,ensure_ascii=False)+"\n")
E
cp -r executed/clark-2026 $TMPDIR/exec_run1_backup 2>/dev/null; rm -rf $TMPDIR/exec_run1_backup/.venv; ls $TMPDIR/exec_run1_backup; date -u
```

```
handover
model_sims.ipynb
network.ipynb
network_grid.ipynb
result.json
theory.ipynb
tuning_curves.ipynb
Thu Nov 26 18:44:36 UTC 2026
```

**Agent**

Running the entry once more so the executed copies and the run stamp match the final notebooks (about 77 minutes, until about 20:02 UTC).

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/clark-2026 2>&1 | tail -8; date -u
```

```
Installed kernelspec registry-clark-2026 in executed/clark-2026/.venv/share/jupyter/kernels/registry-clark-2026
0 error(s)
pass  tuning_curves.ipynb  (944 s)
pass  network.ipynb  (1313 s)
pass  network_grid.ipynb  (471 s)
pass  theory.ipynb  (106 s)
pass  model_sims.ipynb  (1793 s)
Thu Nov 26 20:01:56 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,os,re
B=os.environ['TMPDIR']+'/exec_run1_backup'
tim=re.compile(r'(\d+ s\b|in \d+ s|time \d+ s|done at \d+ s|peak memory [\d.]+ GB|total time \d+ s)')
for nb in ['tuning_curves','network','network_grid','theory','model_sims']:
    a=json.load(open(f'{B}/{nb}.ipynb')); b=json.load(open(f'executed/clark-2026/{nb}.ipynb'))
    nd=0
    for i,(ca,cb) in enumerate(zip(a['cells'],b['cells'])):
        ta=''.join(''.join(o.get('text','')) for o in ca.get('outputs',[]))
        tb=''.join(''.join(o.get('text','')) for o in cb.get('outputs',[]))
        la=[tim.sub('T',x) for x in ta.splitlines()]; lb=[tim.sub('T',x) for x in tb.splitlines()]
        for x,y in zip(la,lb):
            if x!=y: nd+=1; print(nb,i,'\n  A',x[:300],'\n  B',y[:300])
        if len(la)!=len(lb): print(nb,i,'line count differs')
    print(nb,'differing lines',nd)
E
```

```
tuning_curves differing lines 0
network differing lines 0
network_grid differing lines 0
theory differing lines 0
model_sims differing lines 0
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/clark-2026 | tail -1; python tools/entry.py run entries/clark-2026 2>&1 | tail -1; date -u
```

```
0 error(s)
reused the executed copies of 2026-11-26 20:01 UTC: nothing the run reads has changed since (hash 6da5313f131c). Nothing was executed and no environment was built; --fresh runs it again.
Thu Nov 26 20:02:13 UTC 2026
```

**Agent**

I worked through every point in the round-1 report. Four outcomes changed, the entry passes its checks, and the last full run (77 min) matches the run before it line for line. Nothing is committed.

**Outcome changes**
- **figs11b (global stability of the data network): partially reproduced → reproduced, resting on an assumption.** I revised the threshold the verifier found unfair (problem 5). It now comes from the fig2ef runs redone with the same 5-ms step as the runs it judges, not from the 1-ms fig2ef run. Under it, 97% to 100% of final states are within the threshold at every spread, under all five seeds. The old 1-ms threshold is kept as a variant and still fails the 95% at three spreads.
- **Three claims that were blocked for time are now tested**, in a new notebook, `model_sims.ipynb`:
  - **figs1-s2 (spectrum does not fix the symmetry): partially reproduced, seed sensitive.** The dynamics match the legends under all five seeds. The eigenvalues of the two networks differ by 5.18% under the claim's seed, just outside the 5% asked. Over the five seeds they differ by 2.4% to 5.2%, and the paper's own seed-42 matrices differ by 3.3%.
  - **figs11-s12 (global and finite-N stability of the model): reproduced, resting on an assumption, seed sensitive.** The assumption is a threshold taken from the network's own fig2ef-style run. One of the four extra seeds gives 0.94, just under the 95%.
  - **figs10 (robustness to weight noise): reproduced, resting on an assumption.** I counted a network as keeping a continuum when at least 31 of its 34 states stay distinct. Both networks keep all 34 at noise 0; at noise 0.4 they end in 8 and 9 states.
- **fig8 stays blocked** as too large.

**Added or corrected**
- **fig4:** I added the outputs the verifier asked for. They are the paper's grid point at 500,000 samples under all five seeds (second each time), 90 points instead of 30 (same minimum), and a float32 pass over all 30 (same minimum). I also read the paper's own cached error grid from Zenodo: its two best points are 1.1% apart. The outcome stays partially reproduced.
- **Smoothing widths:** compared with `np.isclose`, the widths match the cache in 100% of units. The 78% figure was an artefact of comparing floats with `==`.
- **fig2gi:** I added each trajectory's angle shift under the sorted matrix (median 0.0050 rad, all 50 bins filled), the sorted matrix under all five seeds, and wrap-mode smoothing as a variant.
- **figs8-s9:**
  - The paper's cached flow errors agree with mine and fail the same part of the criterion.
  - My notes had the error at λ 1e-12 as 2.6e-9. The notebook prints 3.6e-9, and the notes now say so.
- **figs14:** the notebook now marks the complex-conjugate pairs and sets aside each tied candidate for the constant mode in turn. The notes say the evidence rests on only two real pairs.
- **fig7:** the bump is not flat at the 293 grid points without a zero mode (median amplitude 0.95). I updated the related finding, and the fig4 one.
- **Questions for a reader** (`questions/clark-2026.yaml`):
  - fig2gi: the 50 states the criterion asks for cannot be reached with its position measure.
  - figs8-s9: the error at λ 1e-8 is required to be lower than at 1e-12, which is stricter than the supplement's "just above the minimum".

  Neither claim was changed.
- **Records:** round 1 is recorded under `verifications` for all 30 claims. For the four claims the verifier could not test, I set `agrees: false` with no outcome. No finding is rated critical, so no finding review was needed. The README, summaries and runtimes are updated.

**Not done**
- **100 starting states at every grid point in figs8-s9.** Before the run I estimated the whole entry at close to the two-hour command limit, so I kept 100 only at the eight points the criterion reads. The grid notebook then took only 8 minutes, so this would in fact have fitted.
- **Fig. 8 (grid cells):** still too large to run.

## End of run

82 turns, 193 minutes, $10.50 at API prices, result: success.
