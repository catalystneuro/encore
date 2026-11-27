# clark-2026 · claims · run 45808934433

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,200p docs/protocol.md; ls -la paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 40,
 "limit": 160
}
```

```
40	on DANDI and `<archive>-<id>` otherwise ([archives.md](archives.md)). The
41	pipeline is described in [pipeline.md](pipeline.md).
42	
43	## Reader
44	
45	### 1. Get the paper
46	
47	The workflow puts the paper's full text, and its PDF where there is one, under
48	`paper/`: the main text, the Methods, and the supplement. Read the text; open
49	the PDF only to read a figure or a table the text garbles. If the full text is
50	not there, or lacks the Methods or a supplement the results rest on, stop:
51	write no claims, and end with a report that names what is missing, so that it
52	can be supplied. Never write claims from the abstract. Do not copy figures.
53	Do not look at the dataset's data: its title and description on the archive
54	are enough to know which paper and which experiments it is meant to hold. A
55	data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
56	documentation) is a longer description, to be read for that alone; it is not
57	the paper, and no claim comes from it.
58	
59	### 2. Read the paper's code
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/clark-2026.yaml 2>/dev/null; ls papers | head; grep -rl "clark-2026" --include=*.yaml . | head; head -60 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n "=== page\|=== supp\|^Supplementary\|Methods$\|^Results\|Data availability\|Code availability" paper/*.txt | head -150; grep -A20 "000939" targets/reuse.yaml | head -40
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text present: main text, Methods and supplement (version of record). Reading the main text now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02452-4.txt",
 "offset": 60,
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02452-4.txt",
 "offset": 959,
 "limit": 1230
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02452-4.txt",
 "offset": 2188,
 "limit": 815
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk 'NR>3000' *.txt | grep -n -i "N_\?data\|mouse\|mice\|experimental\|recording\|dandi\|Kuiper\|pooled\|fit" | head -120
```

```
206:Ndata
208:Ndata = 1,533
2564:the generative-process fits of the main-text section ‘Statistical generative process’ (Setting 2; Methods, ‘Model
2597:which we have provided statistical evidence in the mouse data. Indeed, the corrections this procedure makes
2747:Supplementary Figure 7: Effect of double normalization on tuning curves (Ndata = 1,533). Teal lines show cross-validated,
2794:directly from recordings, using measured tuning curves and binned spike counts. Here we show that it is the
2851:Supplementary Figure 8: Attractor stability across parameter values (N = Ndata = 1,533, softplus activation). Each
2903:λ (N = Ndata = 1,533, softplus activation). Flow error is the mean squared flow on the target manifold.
3049:β = 2.77, error-function activation). b, Data-derived network (N = Ndata = 1,533, uniform inhibition c = 1, softplus
3095:in experimental data (four example mice). a, Centered and variance-normalized correlation functions over random
3098:and variance-normalized correlation function of each mouse’s full set of neurons, Nfull ∈{117, 93, 90, 86}.
3106:optimal weight matrix J of the main-text section ‘Dynamics of the data-derived network model’ (N = Ndata = 1,533,
3109:of the Nθ×Ndata matrix Φ. b, Networks constructed from generative-process samples of increasing size (generative-process
4124:• Flexibility for matching experimental data. The Darshan and Rivkind [11] model produces a
4126:instead allows arbitrary correlation functions for the input currents. It provides enough freedom to fit
4127:experimental head-direction tuning curves quantitatively with only three parameters.
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02452-4.txt",
 "offset": 5516,
 "limit": 620
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "distinct Fourier\|minimiz\|grid search\|Sinkhorn\|Euclidean norm\|time-reversed\|square environment\|100,000\|zthresh\|peak count\|mexican hat" 10.1038-s41593-026-02452-4.txt | head -60; sed -n 3000,3090p 10.1038-s41593-026-02452-4.txt
```

```
34:recovers the ingredients of classical ring attractors, namely, Mexican hat 
49:support Turing pattern formation, typically through a Mexican hat 
276:weights. E, excitatory; I, inhibitory. b, Circulant, Mexican hat weight profile 
319:Mexican hat interactions and continuous symmetry. Spontaneous symmetry breaking then generates stable bump states through a Turing 
385:squares, minimizing the loss function
471:approximate Mexican hat structure (Fig. 2b; a similar ordering can be 
720:all recordings by minimizing the difference between the empirical 
850:of peak counts per tuning curve across detection thresholds zthresh, 
987:Minimized error at σ
1111:as a function of σ, minimized over b and β, where the error is the Euclidean norm 
1113:correlation functions over the first 20 distinct Fourier coefficients. The dashed 
1137:because its rows hold the Fourier coefficients of independently sampled tuning curves and the Gaussian process leaves distinct Fourier 
1174:modulated by global activity, as we explain), Mexican hat interactions 
1200:to the eigenvalues of J. JJ(Δθ) has the Mexican hat profile characteristic 
1231:Peak count
1237:Peak count
1249:Peak count
1256:zthresh = 1.0
1257:zthresh = 0.5
1258:zthresh = 0
[... 115 more lines not kept]
```

**Agent**

Text is complete. Now the supplement's Fourier-coefficient section, which may say how the generative-process fit is computed.

**Agent calls Bash**

```bash
sed -n 5317,5515p 10.1038-s41593-026-02452-4.txt | grep -v "^[0-9.−-]*$" | head -150
```

```
=== page 30 ===
Supplementary Note 2: Large-N theory of the model
Fourier coefficients of correlation functions
This section computes the Fourier coefficients of the correlation functions used in the paper. These are wrapped
functions, and thus their coefficients follow from the Poisson summation formula (Eq. 28).
Wrapped Gaussian. Consider first the wrapped Gaussian correlation function (same as Eq. 6 in the main
text)
Γx(∆θ) =
∞
�
p=−∞
exp
�
2σ2(∆θ + 2πp)2
�
We identify f(x) = exp(−1
2σ2x2), which has Fourier transform
ˆf(k) = 1
2π
�∞
[... 130 more lines not kept]
```

**Agent**

Next, the paper's code on GitHub.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/davidclark1/symmetries-continuous-attractors 2>&1 | tail -3; cd symmetries-continuous-attractors 2>/dev/null && git log -1 --format="%H %cd" && find . -type f -not -path "./.git/*" | head -80
```

```
245726fa78457e10cdcf17e6be36fba1dec98061 Tue Aug 11 11:18:11 2026 -0400
./figures/dmft_theory.pdf
./figures/asymmetric_models.png
./figures/external/digitize_nayebi_fig3a.py
./figures/external/crops/t7c2_autocorr.png
./figures/external/crops/t7c1_spike.png
./figures/external/crops/t7c2_spike.png
./figures/external/crops/t7c2_rate.png
./figures/external/crops/t7c1_autocorr.png
./figures/external/crops/t7c3_rate.png
./figures/external/crops/t7c3_autocorr.png
./figures/external/crops/t7c1_rate.png
./figures/external/crops/t7c3_spike.png
./figures/external/composite_hafting_panelA.py
./figures/external/hafting2005_grid_ratemaps.png
./figures/external/README.md
./figures/normalized_covariance_eigenvectors.png
./figures/left_right_singular_vectors.png
./figures/spurious_fixed_points.pdf
./figures/low_rank_mixture_torus.pdf
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/symmetries-continuous-attractors && cat data/README.md README.md | head -120 && wc -l ring/*.py && cat ring/data.py
```

````
# `data/`: cached intermediate results

**This directory is empty in the repository. Download its contents from Zenodo:**

    https://doi.org/10.5281/zenodo.21827767

Unpack the archive here, so that the `.npz` files sit directly in `data/` and `tc_data.npz`
sits in `data/mouse_data/`. There are 21 files totalling 2.13 GB. Verify the download with:

```bash
md5sum -c CHECKSUMS.md5
```

The notebooks load these files instead of re-running the expensive simulations and fits, so
the figure-plotting cells finish quickly. The notebooks will not run without these files.

## Where each file comes from

Every cache can be rebuilt with the code in this repository; only the three files marked
below also need the raw recordings. The
[... 482 more lines not kept]
````

**Agent**

The code settles several Methods details (100 log-spaced smoothing widths, 10 ms bins, `wake_square` epoch). Now the analysis notebook for Figs 1, 3, 4, 5.

**Agent calls Bash**

```bash
cd $TMPDIR/symmetries-continuous-attractors && python3 -c "
import json
nb=json.load(open('notebooks/data_and_generative_model.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print('#### cell',i,c['cell_type'])
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain')
            if t: print('>>OUT:', ''.join(t)[:1500])
" > $TMPDIR/nb1.txt; wc -l $TMPDIR/nb1.txt
```

```
1115 /tmp/claude-1001/nb1.txt
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb1.txt"
}
```

```
1	#### cell 0 markdown
2	# Mouse head-direction data: statistics and model comparison
3	
4	Characterizes the tuning curves of HD cells from the Peyrache et al. recordings and
5	compares them against the fitted generative model.
6	
7	**Produces** Figures 1, 3, 4 and 5 and Supplementary Figure S13.
8	
9	**Reads** `data/mouse_data/tc_data.npz`, `data/grid_search_results.npz` and
10	`data/analysis_results.npz`. With `REGENERATE_CACHES = True` it writes
11	`data/gamma_phi_info.npz` (the input to `python -m ring.gp_opt`) and rebuilds
12	`data/analysis_results.npz`.
13	#### cell 1 code
14	# Regeneration switches (default off so a normal run cannot overwrite committed figures/caches):
15	SAVE_FIGURES = False
16	REGENERATE_CACHES = False
17	
18	# Standard library
19	
20	# Third-party libraries
[... 1096 more lines not kept]
```

**Agent**

The notebook shows the cell selection (`is_head_direction` and nonzero curves, giving 1,533) and the Kuiper output. Now the helper functions it calls.

**Agent calls Bash**

```bash
cd $TMPDIR/symmetries-continuous-attractors && cat ring/analysis.py && sed -n 1,132p ring/fn.py
```

```
"""Tuning-curve statistics + model-vs-data comparison for the paper analysis.

Provides circular-statistics primitives (COM, centering, peak-finding),
per-mouse aggregate computations, scalar comparison metrics (peak counts,
peak values, flip symmetry, bits-per-spike), and a Kuiper-test-with-
FDR-correction pipeline. The top-level ``analyze_tuning_curves`` runs all
four comparison metrics on data vs model and returns a dict; the npz
serialization round-trip uses ``save_analysis_results`` /
``load_analysis_results``. Consumed by
``notebooks/data_and_generative_model.ipynb`` and ``ring/plot.py``.
"""
import numpy as np
from astropy.stats import kuiper
from scipy.stats import pearsonr
from statsmodels.stats.multitest import multipletests


# --- Core tuning-curve operations ------------------------------------------

def circular_center_of_mass(tuning_curves):
[... 487 more lines not kept]
```

**Agent**

Now the generative-process fit code (`gp_opt.py`) and `tc.py`.

**Agent calls Bash**

```bash
cd $TMPDIR/symmetries-continuous-attractors && cat ring/gp_opt.py; sed -n 1,123p ring/tc.py | grep -v "^\s*$" | head -90
```

```
"""Grid-search optimizer for the (scale, bias, beta) tuning-curve generative parameters.

Walks a (scale, bias, beta) grid, generates ``Phi_m`` samples from each parameter
triple, computes the resulting Fourier-space covariance, and compares to a
target ``Gamma_phi_data_ft`` (typically derived from real mouse data in
``notebooks/data_and_generative_model.ipynb``).

Run as a script to (re)produce ``grid_search_results.npz``::

    python -m ring.gp_opt

Public surface used by notebooks: ``gen_Phi_m`` and ``compute_cov_from_params``
(see e.g. ``data_and_generative_model.ipynb``); the other functions support the
script flow.
"""
from pathlib import Path

import numpy as np
import torch

[... 354 more lines not kept]
```

**Agent**

Fit code read: grid of 20×30×30 over (σ, b, β), 500,000 samples, loss over the first 20 rFFT coefficients. Now the Fig. 2 code (data-derived network and the recording overlap).

**Agent calls Bash**

```bash
cd $TMPDIR/symmetries-continuous-attractors && for n in closing_the_loop data_driven_attractor data_driven_reconstruction; do python3 -c "
import json,sys
nb=json.load(open('notebooks/$n.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print('#### cell',i,c['cell_type'])
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain')
            if t: print('>>OUT:', ''.join(t)[:800])
" > $TMPDIR/$n.txt; wc -l $TMPDIR/$n.txt; done; grep -n "^def \|^    \"\"\"" ring/data_driven.py | head -60
```

```
273 /tmp/claude-1001/closing_the_loop.txt
650 /tmp/claude-1001/data_driven_attractor.txt
456 /tmp/claude-1001/data_driven_reconstruction.txt
31:def load_tuning_curve_data():
32:    """(internal) Load tuning curves from ``TC_DATA_PATH``, dropping all-zero rows.
44:    """
57:def prepare_Phi(tcs, hd_mask):
58:    """(internal) Select HD-classified units, mean-normalize, and transpose to (N_theta, N)."""
65:def load_data_Phi():
66:    """Load ``Phi`` for the HD-classified subset of mouse units.
72:    """
79:def nonlin(x, beta=2):
80:    """Softplus nonlinearity. Thin wrapper around ``fn.softplus(x, beta)``."""
84:def inv_nonlin(phi, beta=2):
85:    """(internal) Inverse softplus: ``log(exp(beta * phi) - 1) / beta``.
88:    """
99:def resample_curves_fft(X, N_new):
100:    """(internal) FFT-based resampling of curves from ``N_original`` to ``N_new`` points.
110:    """
119:def _sinkhorn_normalize(Phi, n_iter=1000):
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v "^\s*#\|set_\|ax\.\|plt\.\|fig\.\|style\." closing_the_loop.txt | head -200
```

```
Projects binned spiking from one Peyrache session onto that session's measured tuning
curves, giving the empirical order parameter m(θ, t) next to the animal's true head
direction.

**Produces** no paper figure. With `REGENERATE_CACHES = True` it writes
`data/closing_the_loop.npz`, which `data_driven_attractor.ipynb` uses for Figure 2's
closed-loop panels, and `data/hd_timeseries.npz`, the head-direction trace that
`dmft.ipynb` uses when rebuilding its own caches.

**Reads** `data/mouse_data/tc_data.npz` and the raw recordings (52 GB,
[DANDI 000939](https://dandiarchive.org/dandiset/000939); point `RING_DATA_DIR` at your
download). This is the only notebook that needs the raw recordings.
REGENERATE_CACHES = False

import numpy as np
from pynwb import NWBHDF5IO
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from ring import data
from ring import style
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v "^\s*#\|set_\|ax[0-9A-Za-z_\[\], ]*\.\|plt\.\|fig\.\|style\.\|legend\|text(" data_driven_attractor.txt | grep -v "^\s*$" | head -260
```

```
Fits recurrent weights to the measured HD tuning curves, characterizes the resulting
attractor, and tests it against circulant surrogates and a real velocity drive.
**Produces** Figure 2 (`figures/data_driven_attractor.pdf`), assembled in the final cell;
every panel below is a component of it.
**Reads** `data/mouse_data/tc_data.npz`, `data/closing_the_loop.npz`,
`data/convergence_pcs.npz`, `data/convergence_distances.npz`,
`data/surrogate_bump_sims.npz`, `data/surrogate_spectra.npz` and
`data/velocity_integration_sims.npz`.
REGENERATE_CACHES = False
SAVE_FIGURES = False
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from ring import data_driven, style
import numpy as np
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt
import numpy as np
import scipy
Solves for `J` such that the measured tuning curves `X` are a fixed point of the network, i.e. `X ≈ Φ Jᵀ`, with ridge regularization `lamda=1e-8`; the printed error confirms the fit. The resampling runs at `N_theta=10000`.
[... 241 more lines not kept]
```

**Agent**

Key settings found (noise 3.0 on input currents, 100 initial conditions, 30 s, dt = τ/50, ridge 1e-8). Now the network-construction helpers.

**Agent calls Bash**

```bash
cd $TMPDIR/symmetries-continuous-attractors && sed -n 1,290p ring/data_driven.py | grep -v '^\s*$' ; sed -n 520,670p ring/data_driven.py | grep -v '^\s*$'
```

```
"""Data-driven ring-attractor toolkit.
Builds the empirical weight matrix ``J`` from mouse tuning curves, runs
the resulting recurrent network with closed-loop head-direction drive,
projects trajectories into PC space, and plots them. Consumed primarily
by ``notebooks/data_driven_attractor.ipynb`` (Fig 3 producer) and the
``data_driven_analyses`` / ``grid_sims`` chains.
"""
from pathlib import Path
import numpy as np
import torch
from scipy.ndimage import gaussian_filter1d
from tqdm import tqdm
from . import sim
from . import fn
from . import regression
from . import analysis
from . import style  # noqa: F401  (imported for the matplotlib rcParams side effect)
# Paths resolve relative to the ring/ package (not the notebook cwd) so they
# work regardless of where the consumer runs from.
TC_DATA_PATH = str(Path(__file__).parent.parent / "data" / "mouse_data" / "tc_data.npz")
[... 336 more lines not kept]
```

**Agent**

Now `regression.py` (the weight solve) and `sim.py`.

**Agent calls Bash**

```bash
cd $TMPDIR/symmetries-continuous-attractors && grep -v '^\s*$' ring/regression.py | sed -n 1,101p; grep -n "def run_sim" -A80 ring/sim.py | grep -v '^\S*\s*$' | grep -v '"""' | sed -n 1,90p
```

```
"""Ridge regression for tuning-curve-to-weight inference.
Solves the regularized least-squares problem ``X ≈ J @ Phi`` for the weight
matrix ``J``, with three options for handling the ``N_theta`` vs ``N``
asymmetry: ``primal``, ``dual``, and ``leave_one_out``.
"""
import numpy as np
def compute_J(X, Phi, lamda, method='opt'):
    """Solve ridge regression ``X ≈ J @ Phi`` with diagonal subtraction.
    Removes the autapse (self-coupling) by subtracting a diagonal correction
    from the unconstrained solution ``J_uc``; the returned ``J`` has zero
    diagonal in the relevant inner product.
    Parameters
    ----------
    X : ndarray, shape (N_theta, N)
        Target activity (e.g. preactivations or trajectories).
    Phi : ndarray, shape (N_theta, N)
        Predictor activity (e.g. tuning curves).
    lamda : float
        Ridge regularization strength, in the ``N``-normalized convention
        described below.
[... 138 more lines not kept]
```

**Agent**

Last code check: the Supp. Fig. 14 spectrum cell in the reconstruction notebook.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -i "S14\|eigvals\|spectr\|S7\|S9\|lamda" data_driven_reconstruction.txt | head -40; ls ~/.cache 2>/dev/null | head -2; cd  ls tools/claims_check.py; head -40 claims/clark-2024.yaml
```

```
2:# Normalization, spectrum, and convergence of the data-driven attractor
6:**Produces** Supplementary Figures S7 (`double_normalization.pdf`),
7:S8 (`pca_convergence.png`), S9 (`error_vs_regularization.pdf`) and
8:S14 (`data_and_subsample_spectra.png`).
40:J, J_prime = data_driven.compute_weights(X, Phi, lamda=1e-8)
48:## Supplementary Figure S14 (left): eigenvalues and singular vectors of the data-fit `J`
50:Spectrum of the fitted weight matrix and the leading left singular vectors of `Φ`. The near-degenerate cluster of real eigenvalues just above 1 (boxed in the complex-plane panel) is the signature of the continuous attractor. The compose cell below re-renders this content as the left half of Supplementary Fig. S14.
52:w = np.linalg.eigvals(J)
95:Compose Supplementary Fig. S14 in full: data-fit spectrum (a) + subsample convergence (b).
110:# --- Panel A quantities (mouse-data fit; identical to the data_spectrum cell) ---
111:w = np.linalg.eigvals(J)
115:beta, scale, lamda_sub, N_theta_sub = 2.7659, 1.4211, 1e-8, 500
163:    Jb, Jb_uc = data_driven.compute_weights(X=Xb, Phi=Phib, lamda=lamda_sub)
164:    wb = np.linalg.eigvals(Jb)
193:    plt.savefig("../figures/data_and_subsample_spectra.png", bbox_inches="tight", dpi=400)
197:## Supplementary Figure S7: effect of the extra cross-neuron normalization
283:# Ten decades of ridge, centred on the operating value lamda = 1e-8 at index 2. The
285:lamda_vals = [1e-12, 1e-10, 1e-8, 1e-6, 1e-4, 1e-2]
317:    for lam_idx, lamda in enumerate(lamda_vals):
319:        J, J_prime = data_driven.compute_weights(X, Phi, lamda=lamda)
[... 55 more lines not kept]
```

**Agent**

I have what I need from the paper and code. Checking the checker's accepted fields before writing.

**Agent calls Bash**

```bash
grep -n "'\w*'" tools/claims_check.py | grep -i "field\|key\|kind\|data\|allowed" | head -30; grep -n "^ *kind:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c
```

```
259 agent
     79 link
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/claims_check.py; grep -n "data:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[:5000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
d=json.dumps(s,indent=1); i=d.find('\"where\"'); print(d[i:i+6000])"
```

```
"where": {
      "description": "For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     },
     "datasets": {
      "description": "Only when the paper is tested on more than one dataset: the folder names of those this claim rests on.",
      "type": "array",
      "items": {
       "type": "string"
      },
      "minItems": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
[... 187 more lines not kept]
```

**Agent**

Before writing, one check: which surrogate (symmetric or asymmetric scrambled noise) Fig. 2d,i uses.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "circ_plus_noise" data_driven_attractor.txt | head; grep -n "A3707\|117\|mouse_names\|omega" data_driven_attractor.txt | head
```

```
181:        'circ_plus_noise': SCALE_FACTOR * (J_circ + J_noise_scrambled),
182:        'circ_plus_noise_sym': SCALE_FACTOR * (J_circ + J_noise_scrambled_sym),
271:matrix_keys = ['orig', 'srt', 'circ', 'circ_plus_noise_sym', 'circ_plus_noise']
387:circ_plus_noise_sym
388:circ_plus_noise
582:plot_weight_matrix(ax_circ_noise, mat_results['circ_plus_noise'], "circulant+noise")
609:plot_simulation_results(ax_convg3, sim_results['circ_plus_noise'], "circulant+noise", titlepad=0)
404:    hd, omega, data_dt = data_driven.load_hd_and_omega() 
405:    omega_interp = interp1d(np.arange(len(omega))*data_dt, omega)
412:    # Define omega functions
413:    omega_funcs = [
415:        omega_interp  # Real head direction signal
420:    for i, omega_func in enumerate(omega_funcs):
424:            J_prime=J_prime, omega_func=omega_func
430:        # Resample omega at correct times
432:        omega_rs = omega_func(t)
435:        hd_target = np.cumsum(omega_rs) * T_eval
Shell cwd was reset to
```

**Agent**

Fig. 2d,i uses the asymmetric scrambled residuals. Checking how other claims files mark findings that rest on simulation only.

**Agent calls Bash**

```bash
grep -l -i "simulation\|theor" claims/*.yaml | head; grep -h -B2 -A6 -i "no recorded data\|model alone\|simulation only\|theoretical result" claims/*.yaml | head -60
```

```
claims/andrews-2024.yaml
claims/athalye-2023.yaml
claims/brudner-2026.yaml
claims/bruno-2017.yaml
claims/buccino-2020.yaml
claims/buccino-2024.yaml
claims/burman-2023.yaml
claims/chartrand-2023.yaml
claims/clark-2024.yaml
claims/daume-2024-phase.yaml
  data: elsewhere
  where: github.com/PeyracheLab/MehrotraLevenstein_2023 at commit 4ee34f3, Model/ (simulation
    code; no recorded data)
  criterion: Run Figure3.m and FigureS3b.m to FigureS3d.m with the parameters of the Methods
    table (Parameters for AdWC model). Reproduced when, for each of the three gradients, the
    slope of threshold-crossing time against position is non-zero at UD in all parameter
    combinations swept, as the scripts compute it.
- id: fig3f-ih-gradient
  statement: A gradient of an h current (Ih) in the model produces synchronous UD transitions
--
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/symmetries-continuous-attractors && for n in spectra grid_sims dmft spurious_fixed_points weight_matrix_analyses; do echo "=== $n"; python3 -c "
import json
nb=json.load(open('notebooks/$n.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='markdown': print('MD:', ''.join(c['source'])[:400])
    else:
        for o in c.get('outputs',[]):
            t=o.get('text')
            if t: print('>>OUT:', ''.join(t)[:300])
"; done 2>&1 | head -150
```

```
=== spectra
MD: # Spectra of disordered vs. circulant ring-attractor weights

Builds two weight matrices with matched eigenvalue spectra, namely the model's `J` derived
from disordered tuning curves and a circulant matrix plus i.i.d. noise, and compares their
spectra and eigenvector structure. The point is that spectrum alone does not distinguish
the two; the eigenvector geometry does.

**Produces** Figure 6 (`fi
MD: ## Idealized tuning-curve model

Local definitions for the idealized (non-data-driven) tuning-curve family: an erf nonlinearity, wrapped-Gaussian-covariance tuning curves, and the closed-form effective weight profile used to build the circulant comparison matrix.
MD: ## DMFT effective weight profile

Computes the translation-invariant weight profile `J_dmft` and gain `alpha` from sampled tuning curves. The profile and the gain define the circulant matrix in the comparison below; the parameters (`beta`, `scale`) are the fitted values used throughout the paper.
MD: ## Build the two weight matrices

Generates the model's `J` from disordered tuning curves (sorted by tuning-curve centre of mass so the ring structure is visible), then builds `J2` as the matched circulant plus i.i.d. Gaussian noise of scale `g`. `sample_tcs` can consume a varying number of random draws depending on the BLAS library, so the `np.random.seed(45)` immediately before the `J2` noise dr
MD: ## Figure 6: spectra and eigenvector structure

[... 127 more lines not kept]
```

**Agent**

I've read the paper, supplement and code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/clark-2026.yaml",
 "content": "# Claims for Clark, Abbott & Sompolinsky (2026), Nature Neuroscience, \"Symmetries and continuous\n# attractors in disordered neural circuits\", doi:10.1038/s41593-026-02452-4, on dandiset 000939.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-26,\n# protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read. The version of record (PDF supplied by a person, extracted to text): main text,\n# figure legends, Methods, Data and Code availability and the Reporting Summary, and the\n# Supplementary Information PDF (41593_2026_2452_MOESM1_ESM.pdf, Supplementary Notes 1 to 4 with\n# Supplementary Figs. 1 to 16). No figure page was opened; no number below is read from a figure.\n#\n# Data the paper used, as it reports them. Recordings of Duszkiewicz et al. (Nat. Neurosci. 2024)\n# from the postsubiculum of freely moving mice, DANDI 000939 (version cited 0.240528.1542). 31\n# recording sessions, one per mouse, 2,691 units, of which 1,533 carry the dataset's\n# head-direction label (significant head-direction information against a time-reversed control,\n# a label set by the original authors and distributed with the dataset). Only the epoch of\n# square-environment exploration is analysed (tag wake_square in the NWB epochs table). Nine mice\n# also had an optogenetic epoch, recorded separately and never analysed (files named +ogen.nwb);\n# they contribute 315 of the 1,533 cells. Measured variables used are the head direction\n# (processing/behavior/CompassDirection/head-direction, with timestamps), the spike times of each\n# unit, and the unit labels is_head_direction (and is_excitatory, is_fast_spiking). The four mice\n# with most head-direction cells are A3707 (117), A3716 (93), A3711 (90) and A3706 (86).\n# Fig. 2k and Fig. 7c use the head-direction trace of A3707 as an angular velocity input.\n#\n# Code read. github.com/davidclark1/symmetries-continuous-attractors at commit\n# 245726fa78457e10cdcf17e6be36fba1dec98061 (11 August 2026; archived as Zenodo\n# doi:10.5281/zenodo.21829584). It holds the package ring (data.py builds tuning curves from the\n# NWB files; analysis.py the centers of mass, peak counts, flip symmetry, information and the\n# Kuiper test; gp_opt.py the generative-process fit; data_driven.py and regression.py the\n# data-derived network; dmft.py the mean-field theory) and eleven notebooks, one per figure group\n# (data_and_generative_model for Figs. 1, 3, 4, 5 and S13; data_driven_attractor and\n# closing_the_loop for Fig. 2; spectra for Fig. 6; dmft for Fig. 7; grid_sims for Fig. 8 and\n# S15; weight_matrix_analyses for S1 to S4 and S10; data_driven_reconstruction for S7 to S9 and\n# S14; spurious_fixed_points for S11 and S12). The notebooks print the Kuiper results and the\n# fitted parameters. The paper's cached intermediate results are on Zenodo,\n# doi:10.5281/zenodo.21827768 (the code's README gives 21827767), including the tuning curves\n# mouse_data/tc_data.npz.\n#\n# Method choices the Methods leave open and the code settles (ring/data.py,\n# notebooks/data_and_generative_model.ipynb). Head direction is binned as floor(hd / (2 pi /\n# 100)); each head-direction sample counts as one 10-ms time bin; the epoch runs from the\n# timestamp nearest the wake_square start to that nearest its stop; untracked (NaN) samples are\n# dropped. Spikes are counted in 10-ms bins from the epoch start. The eight segments are\n# contiguous chunks of the epoch's head-direction samples, alternating between the two\n# partitions. Zero-rate bins are set to 1e-3 times the curve's mean before smoothing. The\n# smoothing widths are 100 values, logspace(-1, 2, 100) bins, applied with a circular\n# (wrap-around) Gaussian filter; for each partition the width maximising the Poisson\n# log-likelihood of the other partition's 10-ms spike counts is kept; the final curve is the mean\n# of the two partitions' smoothed curves. Units are kept when is_head_direction is true and the\n# final curve is not all zero; each curve is then divided by its mean over the 100 bins. The\n# center of mass uses the grid 2 pi (a - 1) / 100. These curves are used for every statistic and\n# for the generative-process fit; the network construction adds two further steps\n# (Supplementary Note 3, section 8.1).\n#\n# Details none of the paper, supplement or code fixes, and that a criterion needs, are named as\n# open in the criteria below with the readings the text allows. They are, in short, the measures\n# of agreement and the thresholds behind words such as \"comparable\", \"match\", \"approaches\",\n# \"tracks\", \"a few\" and \"within ~1 s\".\nschema_version: 2\npaper: doi:10.1038/s41593-026-02452-4\nclaims:\n- id: hd-cell-selection\n  kind: link\n  statement: The dandiset holds the 31 sessions, one per mouse, with 2,691 units, of which 1,533\n    carry the head-direction label; nine of the mice have an optogenetic file and contribute 315\n    of those cells; the four mice with most head-direction cells have 117, 93, 90 and 86.\n  source: Methods, Statistics and reproducibility, Sample size and Data exclusions; Fig. 2 legend;\n    Supplementary Fig. 13 legend\n  quote: The size of the dataset was fixed by the original study, namely 31 recording sessions, 1\n    per mouse, comprising 2,691 units, of which Ndata = 1,533 were classified as head-direction\n    cells\n  data: dataset\n  expected:\n  - quantity: sessions (mice)\n    value: 31\n    tolerance: 0\n  - quantity: units in all sessions\n    value: 2691\n    tolerance: 0\n  - quantity: units labelled head-direction with a non-zero tuning curve\n    value: 1533\n    tolerance: 0\n  - quantity: head-direction cells in the nine mice with an optogenetic epoch\n    value: 315\n    tolerance: 0\n  - quantity: head-direction cells of mouse A3707\n    value: 117\n    tolerance: 0\n  criterion: Counts are taken from the units tables of the NWB files, one file per session (the\n    +ogen.nwb file where a session has one, as ring/data.py chooses). The tolerances are zero\n    because the labels are distributed with the dataset and the paper reports exact counts. The\n    paper calls the 1,533 cells excitatory, while the code selects on is_head_direction alone;\n    the readings are (a) is_head_direction, as the code, and (b) is_head_direction and\n    is_excitatory. The link holds when the counts match under one reading; the count under the\n    other is reported. The counts for A3716, A3711 and A3706 (93, 90 and 86) are reported too.\n- id: tuning-curves-match-cache\n  kind: link\n  statement: Tuning curves computed from the dandiset with the paper's procedure agree with the\n    tuning curves in the paper's cached results on Zenodo.\n  source: Methods, Data processing, Tuning-curve estimation; Data availability\n  quote: The cached intermediate results used by the analysis notebooks are publicly available via\n    Zenodo at https://doi.org/10.5281/zenodo.21827768\n  data: with_inputs\n  depends_on:\n  - hd-cell-selection\n  criterion: Tuning curves computed as in the opening comment (ring/data.py, process_file, with\n    N_theta 100, the 100 widths, K 4) are compared with opt_tcs in mouse_data/tc_data.npz of the\n    Zenodo record, unit by unit in the same session order. The link holds when, over the 1,533\n    head-direction units, the Pearson correlation between the computed and cached\n    partition-averaged curves is at least 0.99 for at least 95% of units; partially when that\n    holds for at least 80%. The fraction of units whose chosen smoothing widths match exactly is\n    reported. Both thresholds are chosen here, as the paper reports no comparison.\n- id: fig1e-heterogeneous-peaks\n  statement: Mouse head-direction cells are heterogeneous, with variable numbers of irregularly\n    spaced peaks, unlike the classical prediction of tuning curves identical up to shifts.\n  source: Results, Failure of classical ring-attractor models, paragraph 3; Fig. 1e\n  quote: Mouse head-direction cells instead show substantial heterogeneity, with variable numbers\n    of irregularly spaced peaks (Fig. 1e)\n  data: dataset\n  depends_on:\n  - hd-cell-selection\n  criterion: Peaks are local maxima of the unit-mean, cross-validated curves (100 bins, circular)\n    whose z-score (value minus the curve's mean, over its standard deviation across angles) is\n    above zthresh, as in Methods equation (17) and analysis.find_local_maxima; zthresh 1, the\n    threshold of Fig. 5d. Reproduced when more than one peak count occurs among the 1,533 curves\n    and the angular separations between the two highest peaks of the multi-peaked curves are\n    spread, with an interquartile range above pi/4. The paper gives no measure of irregular\n    spacing; this one is chosen here and named as open, and the full distribution of\n    separations is shown.\n- id: fig5d-peak-numbers\n  statement: At zthresh 1, all 1,533 experimental curves have at least one peak, 412 have at least\n    two and 55 at least three; of 100,000 generative-process samples, 24,271 have at least two\n    and 1,043 at least three.\n  source: Fig. 5d legend\n  quote: using the 1,533, 412 and 55 experimental curves and the 100,000, 24,271 and 1,043\n    generative-process samples that have at least 1, 2 and 3 peaks\n  data: dataset\n  depends_on:\n  - hd-cell-selection\n  expected:\n  - quantity: experimental curves with at least one peak (zthresh 1)\n    value: 1533\n    tolerance: 153\n  - quantity: experimental curves with at least two peaks (zthresh 1)\n    value: 412\n    tolerance: 41\n  - quantity: experimental curves with at least three peaks (zthresh 1)\n    value: 55\n    tolerance: 5.5\n  - quantity: generative-process samples with at least two peaks, of 100,000\n    value: 24271\n    tolerance: 2427\n  - quantity: generative-process samples with at least three peaks, of 100,000\n    value: 1043\n    tolerance: 104\n  criterion: Peaks as in fig1e-heterogeneous-peaks (analysis.get_peak_values, zthresh 1). The\n    generative samples are drawn as in the notebook (gp_opt.gen_Phi_m at the fitted parameters\n    scale 1.4211, bias 1.7307, beta 2.7659, N_samples 100,000, N_theta 100, numpy seed 42, each\n    sample divided by its mean). The seed's draws may not be reproduced exactly, which the 10%\n    tolerance covers.\n- id: fig1fg-mean-and-fluctuation-profiles\n  statement: Aligned by their circular centers of mass within each of the 31 mice, the tuning\n    curves have unimodal, symmetric mean profiles, but fluctuations about them comparable in\n    magnitude to the means, and both profiles are consistent across mice.\n  source: Results, Failure of classical ring-attractor models, paragraph 3; Fig. 1f,g\n  quote: When tuning curves are aligned within each of the 31 mice by their circular centers of\n    mass, the mean profiles are unimodal and symmetric (Fig. 1f), but the fluctuations about them\n    are comparable in magnitude to the means (Fig. 1g), violating the classical prediction of zero\n    fluctuations. Both mean and fluctuation profiles are consistent across mice\n  data: dataset\n  depends_on:\n  - hd-cell-selection\n  criterion: Each unit-mean curve is rolled so that its center of mass falls on bin 0\n    (analysis.center_tuning_curves), and per mouse the mean and standard deviation across neurons\n    are taken at each of the 100 offsets (compute_mean_and_std_profiles_for_all_mice); the mouse\n    average is the mean of the 31 per-mouse profiles. The paper gives no measures for these\n    words, so they are fixed here and named as open. Unimodal, the mouse-average mean profile has\n    one local maximum, at offset 0 within 2 bins. Symmetric, its Pearson correlation with its\n    reflection about offset 0 is at least 0.9. Comparable in magnitude, the peak of the\n    mouse-average standard deviation profile is between half and twice the peak of the\n    mouse-average mean profile (reading a), or the standard deviation exceeds half the mean at\n    offset 0 (reading b). Consistent across mice, the median over mice of the correlation of each\n    mouse's profile with the mouse average is at least 0.9, for the mean and for the standard\n    deviation. Reproduced when all four hold (the third under one reading); partially when the\n    third holds with one other.\n- id: fig3ab-centers-of-mass-uniform\n  statement: Within each session the tuning-curve centers of mass are distributed uniformly; the\n    Kuiper test rejects uniformity in 2 of 31 sessions before correction and in none after\n    Benjamini-Hochberg correction, with corrected P values from 0.59 to 0.97.\n  source: Results, Statistical generative process, paragraph 2; Methods, Statistics and\n    reproducibility, Statistical tests; Fig. 3a,b\n  quote: the Kuiper test rejects uniformity in 2 of 31 sessions (P < 0.05) before\n    multiple-comparison correction and in none after Benjamini–Hochberg correction, where the\n    corrected P values across the 31 sessions range from 0.59 to 0.97\n  statistics:\n  - about: uniformity of center-of-mass angles within each session, lowest corrected P\n    test: Kuiper test, two-sided, against the uniform distribution on [0, 2 pi)\n    p: 0.59\n    corrected: Benjamini-Hochberg false discovery rate at 5%\n    n: 31 sessions, 1,533 neurons\n  data: dataset\n  depends_on:\n  - hd-cell-selection\n  expected:\n  - quantity: sessions with uncorrected P below 0.05\n    value: 2\n    tolerance: 0\n  - quantity: sessions significant after Benjamini-Hochberg correction\n    value: 0\n    tolerance: 0\n  - quantity: lowest corrected P\n    value: 0.59\n    tolerance: 0.059\n  - quantity: highest corrected P\n    value: 0.97\n    tolerance: 0.097\n  criterion: A claim of absence, judged on the paper's test. Centers of mass of the unit-mean\n    curves (Methods equation (14), analysis.circular_center_of_mass); per session the Kuiper test\n    against the uniform CDF x / 2 pi (astropy.stats.kuiper), then Benjamini-Hochberg over the 31\n    P values (statsmodels multipletests, fdr_bh, alpha 0.05). Reproduced when no session is\n    significant after correction, not reproduced when any is; the corrected and uncorrected P\n    values are reported either way. The counts of 2 and 0 are exact (tolerance 0) because they\n    are counts of sessions; the range of corrected P values follows the rule for a reported\n    range.\n- id: fig3c-correlation-approaches-circulant\n  statement: Within a mouse, the two-point correlation function of the tuning curves approaches a\n    circulant form as more neurons are included, as does the centered and variance-normalized\n    correlation function, whose leading eigenvectors are Fourier modes, as circular symmetry\n    predicts.\n  source: Results, Statistical generative process, paragraph 3; Fig. 3c; Supplementary Fig. 13\n  quote: This function approaches a circulant form (Fig. 3c), as does the centered and\n    variance-normalized correlation function, whose eigenvectors converge to Fourier modes\n    (Supplementary Fig. 13), both being predictions of circular symmetry\n  data: dataset\n  depends_on:\n  - hd-cell-selection\n  criterion: For the four mice with most cells (A3707, A3716, A3711, A3706), the correlation\n    function of equation (4) over random subsets of 5, 10, 20, 40 and 80 neurons, and the\n    centered and variance-normalized version of Supplementary Fig. 13 (each angle centered and\n    divided by its standard deviation across the subset's neurons, as the notebook does). The\n    paper shows single random subsets (seed 42) and gives no measure, so one is fixed here and\n    named as open. The distance from circulant form is the Frobenius norm of the matrix minus the\n    circulant matrix obtained by averaging it along its circular diagonals, over the Frobenius\n    norm of the matrix, averaged over 100 random subsets per size. Reproduced when, for each\n    mouse and both functions, the distance at 80 neurons is below that at 5 neurons and falls\n    across the sizes with at most one increase; and when the leading four eigenvectors of each\n    mouse's full centered and normalized function each have at least 80% of their power at one\n    Fourier frequency, with eigenvectors 1 and 2 sharing frequency 1 (threshold chosen here,\n    open). Partially reproduced when one of the two parts holds.\n- id: fig4-generative-fit\n  statement: A single parameter set of the generative process, fitted to the two-point\n    correlation function pooled over mice, is (sigma, beta, b) of about (1.42, 2.77, 1.73).\n  source: Results, Statistical generative process, paragraph 5; Fig. 4d to f; Methods, Model\n    settings, Setting 2\n  quote: This yields (σ, β, b) ≈ (1.42, 2.77, 1.73; Fig. 4d–f) and tuning curves closely\n    resembling the experimental ones (Fig. 4g)\n  data: dataset\n  depends_on:\n  - hd-cell-selection\n  expected:\n  - quantity: Fourier decay scale sigma\n    value: 1.42\n    tolerance: 0.142\n  - quantity: sharpness beta\n    value: 2.77\n    tolerance: 0.345\n  - quantity: soft threshold b\n    value: 1.73\n    tolerance: 0.173\n  criterion: As in ring/gp_opt.py and the notebook. The data target is the power spectrum of the\n    1,533 unit-mean curves (fn.calc_C, the mean over neurons of the squared moduli of the rfft\n    with norm forward). The model spectrum is computed the same way from 500,000 samples of the\n    Gaussian process (Fourier coefficients of the wrapped Gaussian exp(-n^2 / 2 sigma^2) / (sqrt(2\n    pi) sigma), as tc.wrapped_gaussian_cov) passed through the softplus of equation (19) and\n    divided by their means. The error is the Euclidean norm of the difference over the first 20\n    coefficients (indices 0 to 19, Fig. 4d legend), minimised over the grid sigma in linspace(1,\n    2, 20), b in linspace(0.01, 5, 30) and beta in linspace(0.01, 10, 30), seed 42. The tolerance\n    on beta is one step of that grid (0.345), larger than 10% (0.277), because the fit can only\n    land on grid points; the others are 10%, which is about one grid step for b and nearly three\n    for sigma.\n- id: fig5ab-profiles-match\n  statement: The center-of-mass-aligned mean and fluctuation profiles predicted by the fitted\n    generative process match those of the data.\n  source: Results, Statistical generative process, paragraph 6; Fig. 5a,b\n  quote: The predicted center-of-mass-aligned mean and fluctuation profiles match the data (Fig.\n    5a,b\n  data: dataset\n  depends_on:\n  - fig1fg-mean-and-fluctuation-profiles\n  - fig4-generative-fit\n  criterion: Generative profiles from 100,000 samples at the fitted parameters, unit-mean\n    normalized and aligned as for the data (plot.plot_mean_std_profiles with opt_params, numpy\n    seed 42). The paper gives no measure of match; the readings named here are (a) the\n    generative profile lies within the range of the 31 individual mouse profiles at no fewer\n    than 90% of the 100 offsets, and (b) its peak is within 10% of the peak of the mouse-average\n    profile. Reproduced when, under one reading, both the mean and the standard deviation\n    profiles match; partially when only one does. The fit is rerun on these data\n    (fig4-generative-fit); the profiles at the paper's parameters are shown as a variant.\n- id: fig5c-peak-counts-match\n  statement: The generative process reproduces the distribution of peak counts per tuning curve\n    across detection thresholds, with the strongest agreement at the higher thresholds.\n  source: Results, Statistical generative process, paragraph 6; Fig. 5c\n  quote: The process also reproduces the distribution ... of peak counts per tuning curve across\n    detection thresholds zthresh, with strongest agreement at higher thresholds (Fig. 5c)\n  data: dataset\n  depends_on:\n  - fig5d-peak-numbers\n  - fig4-generative-fit\n  criterion: Peak-count histograms for 1 to 5 peaks, normalized to sum to one\n    (analysis.compute_peak_counts), for the 1,533 curves and 100,000 generative samples, at\n    zthresh 1, 0.5 and 0. The paper gives no measure of agreement; the readings are (a) total\n    variation distance and (b) Hellinger distance between the two histograms. Reproduced when,\n    under one reading, the distance at zthresh 1 is the smallest of the three and is below 0.15\n    (threshold chosen here, open); partially when the distance at zthresh 1 is smaller than at\n    zthresh 0 but above 0.15. The distances are reported at every threshold.\n- id: fig5d-peak-heights-match\n  statement: The generative process reproduces the full distributions of tuning-curve values at\n    the three highest peaks.\n  source: Results, Statistical generative process, paragraph 6; Fig. 5d\n  quote: and the full distributions of tuning-curve values at the three highest peaks (Fig. 5d)\n  data: dataset\n  depends_on:\n  - fig5d-peak-numbers\n  - fig4-generative-fit\n  criterion: Heights of the three highest peaks at zthresh 1 (analysis.get_peak_values), for the\n    curves that have them. The paper gives no measure; for each of the three peaks, the median\n    generative height is within 10% of the median data height (reading a), or the two-sample\n    Kolmogorov-Smirnov distance is below 0.15 (reading b; threshold chosen here, open).\n    Reproduced when, under one reading, all three peaks agree; partially when one or two do.\n- id: fig5e-flip-symmetry-match\n  statement: The generative process captures the distribution of flip-symmetry correlations,\n    particularly its strongly asymmetric tail.\n  source: Results, Statistical generative process, paragraph 6; Fig. 5e\n  quote: It captures the distribution of flip-symmetry correlations ρflip (each curve’s\n    correlation with its center-of-mass reflection), particularly the strongly asymmetric tail\n    (Fig. 5e, inset)\n  data: dataset\n  depends_on:\n  - fig4-generative-fit\n  criterion: The flip-symmetry correlation of Methods equation (15), computed as\n    analysis.compute_symmetry_scores (the curve against its reflection about its center-of-mass\n    bin, np.roll(tc, -2 com - 1) reversed). The paper does not say where the tail begins; the\n    readings are curves with correlation below (a) 0.5 and (b) 0. Reproduced when, under one\n    reading, the generative fraction in the tail is within a factor of 1.5 of the data fraction\n    (threshold chosen here, open), and the data have such curves at all. The medians of the two\n    distributions are reported.\n- id: fig5f-information-match\n  statement: The generative process captures the distribution of head-direction information.\n  source: Results, Statistical generative process, paragraph 6; Fig. 5f; Methods, Tuning-curve\n    statistics, equation (16)\n  quote: and the distribution of head-direction information IHD (ref. 48; Fig. 5f)\n  data: dataset\n  depends_on:\n  - fig4-generative-fit\n  criterion: Information per curve as equation (16), the mean over the 100 bins of the unit-mean\n    curve times its base-2 logarithm (analysis.compute_bits_per_spike). The paper gives no\n    measure; the readings are (a) generative median within 10% of the data median, and (b)\n    two-sample Kolmogorov-Smirnov distance below 0.15 (threshold chosen here, open). Reproduced\n    under either reading.\n- id: fig2b-sorted-weights-mexican-hat\n  statement: The optimized data-derived weight matrix looks unstructured in arbitrary order, and\n    ordering neurons by their tuning-curve centers of mass reveals a noisy approximate Mexican hat\n    structure.\n  source: Results, Dynamics of the data-derived network model, paragraph 1; Fig. 2a,b\n  quote: Ordering neurons by the circular centers of mass of their tuning curves reveals a noisy\n    approximate Mexican hat structure (Fig. 2b\n  data: dataset\n  depends_on:\n  - hd-cell-selection\n  criterion: The network is built as in notebooks/data_driven_attractor.ipynb and Supplementary\n    Note 3, section 8.1. From the 1,533 unit-mean curves, input currents by the inverse softplus\n    (beta 2), smoothed with a circular Gaussian filter of 2 bins, softplus again, Sinkhorn-Knopp\n    normalization of both axes (1,000 alternating sweeps, data_driven._sinkhorn_normalize),\n    inverse softplus, zero-padded Fourier resampling to 10,000 angles, softplus; weights by\n    regression.compute_J (dual form, lambda 1e-8, zero diagonal, Methods equation (39)). The\n    matrix is shown before the uniform shift by c, as Supplementary Note 3, section 8.3, says.\n    Neurons are sorted by the center of mass of the resampled curves (sort_weight_matrix). The\n    profile is the mean of the sorted matrix along each circular diagonal (the first row of the\n    notebook's create_circularized_matrix). Reproduced when the profile is highest at offsets\n    near 0 and falls below its mean over offsets at intermediate offsets, with local excitation\n    and longer-range inhibition; the paper gives no measure of noise and none is judged.\n- id: fig2ef-data-network-quasicontinuous\n  statement: Started at regularly spaced manifold points perturbed by noise, the data-derived\n    network's trajectories return to the manifold within about 1 s and then persist over 30 s, an\n    order-of-magnitude separation between convergence and drift timescales.\n  source: Results, Dynamics of the data-derived network model, paragraph 3; Fig. 2e,f\n  quote: Initialized at regularly spaced manifold points perturbed by noise, trajectories return to\n    the manifold within ~1 s (Fig. 2f) and then persist over 30 s (Fig. 2e), an order-of-magnitude\n    separation between convergence and drift timescales\n  data: dataset\n  depends_on:\n  - fig2b-sorted-weights-mexican-hat\n  criterion: The network of fig2b-sorted-weights-mexican-hat with softplus beta 2, tau 50 ms, Euler\n    step 1 ms, uniform inhibition c 1 (the mean stabilizer of Supplementary equation (137)), 100\n    initial conditions at every 100th of the 10,000 manifold angles with independent Gaussian\n    noise of standard deviation 3 added to the input currents (run_convergence_analysis), run for\n    30 s and saved every 10 ms. Distance is the smallest Euclidean distance between the firing\n    rates and the 10,000 target firing-rate points, over the square root of N\n    (compute_distances_to_ring). The thresholds are not given and are named as open. Returns\n    within about 1 s, the median distance at 1 s is at most one tenth of that at 0 s (reading a),\n    or at most twice its value at 20 s (reading b). Persists, the manifold angle of each\n    trajectory (the angle of its nearest target point) moves by less than 2 pi / 20 between 1 s\n    and 30 s for at least 90% of trajectories (reading c), or the 100 final angles occupy at\n    least 50 distinct bins of width 2 pi / 100 (reading d). Reproduced when one of (a, b) and one\n    of (c, d) hold.\n- id: fig2gi-circulant-noise-collapses\n  statement: The optimal weights keep a continuum of stable heterogeneous states; their circulant\n    average gives bumps identical up to translation, while the circulant matrix plus the scrambled\n    residuals collapses onto a few discrete states within 30 s, so the optimal weights are not a\n    noisy circulant matrix.\n  source: Results, Dynamics of the data-derived network model, paragraphs 4 and 5; Fig. 2c,d,g to\n    i; Supplementary Note 3, section 8.2\n  quote: The optimal weights (Fig. 2b) maintain a continuum of stable, heterogeneous states (Fig.\n    2g). Averaging the sorted weights along ... diagonals gives a circulant matrix (Fig. 2c) whose\n    bumps are identical up to translation ... this network collapses onto a few discrete states\n    within the 30-s window (Fig. 2i)\n  data: dataset\n  depends_on:\n  - fig2b-sorted-weights-mexican-hat\n  criterion: As in data_driven_attractor.ipynb. The sorted matrix; its circulant version, the\n    average over circular diagonals; and the circulant plus noise, the residuals (circulant minus\n    sorted) with all off-diagonal entries shuffled together, the asymmetric version used in Fig.\n    2d,i (numpy seed 42); both surrogates multiplied by 1.275. Each is run with c 1 from 100\n    initial conditions at regularly spaced manifold points with input-current noise of standard\n    deviation 2.5, for 30 s. A final state's position is the neuron index of the peak of its\n    activity, smoothed across sorted neurons with a Gaussian of 2.5 neurons, as the figure is\n    drawn. The paper gives no count or similarity measure; these are fixed here and named as\n    open. Final positions within 2 pi / 50 of each other (31 neurons) are merged into one state.\n    Reproduced when the sorted optimal matrix keeps at least 50 distinct states, the circulant\n    plus noise matrix at most 10, and the circulant matrix's final states are shifts of one\n    another (each correlates at least 0.99 with the best circular shift of the first). Partially\n    reproduced when the contrast between the optimal and the circulant plus noise holds alone.\n    The symmetric scrambled version is shown as a variant.\n- id: fig2jk-velocity-integration\n  statement: With the velocity-coupling weights added, the data-derived network's overlap order\n    parameter tracks a constant angular velocity input of 0.8 rad/s accurately and follows the\n    more complex trajectory of the mouse's own head-direction behaviour.\n  source: Results, Dynamics of the data-derived network model, paragraph 6; Fig. 2j,k; Methods,\n    Angular velocity integration\n  quote: m(θ, t) tracks the input accurately (Fig. 2j), and the network also follows the more\n    complex trajectories of the behavioral data (Fig. 2k)\n  data: dataset\n  depends_on:\n  - fig2b-sorted-weights-mexican-hat\n  criterion: As in the notebook's run_analysis. J and J' (the solution for the angular derivative\n    of the targets, Methods equation (41)), c 1, tau 50 ms, step 1 ms, started at the target\n    state of angle 0 and run for 110 s; omega is 0.8 rad/s from 20 s on (j), or the angular\n    velocity of A3707's wake_square head direction (k), with gaps interpolated on the circle,\n    unwrapped, 2,000 still samples prepended, smoothed with a Gaussian of 10 samples and\n    differenced (data_driven.preprocess_hd_data). The first 20 s are dropped. m(theta, t) is\n    equation (5) with the target firing rates; the target is the integral of omega. The paper\n    gives no measure of tracking; the readings are (a) the median absolute circular difference\n    between the angle of the peak of m and the target is below pi/8, and (b) the circular\n    correlation between them is at least 0.9 (thresholds chosen here, open). Reproduced when both\n    inputs track under one reading; partially when only the constant input does.\n- id: fig2l-recorded-bump-tracks-hd\n  statement: The overlap order parameter computed directly from the recordings, with the measured\n    tuning curves and binned spike counts of one mouse, forms a bump that tracks the animal's head\n    direction.\n  source: Results, Dynamics of the data-derived network model, paragraph 7; Fig. 2l\n  quote: The resulting bump tracks the animal’s head direction (Fig. 2l) and closely resembles\n    that of the model (Fig. 2k)\n  data: dataset\n  depends_on:\n  - hd-cell-selection\n  criterion: Mouse A3707 (the session with most head-direction cells, 117), wake_square epoch, as\n    in notebooks/closing_the_loop.ipynb. Spike counts of the 117 cells in 10-ms bins, averaged in\n    100-ms bins (10 bins), each cell's counts and curve divided by the mean of its curve; m is the\n    mean over cells of curve times counts at each of the 100 angles. The curves are those of the\n    whole session (mean of the two partitions), as the code uses. The paper gives no measure;\n    the readings are (a) the median absolute circular difference between the angle of the peak\n    of m and the mean head direction in the same 100-ms bin is below pi/8, and (b) their circular\n    correlation is at least 0.9 (thresholds chosen here, open). Bins with untracked head direction\n    are left out. Reproduced under either reading. Curves from one partition applied to the\n    other partition's spikes are shown as a variant.\n- id: figs8-s9-lambda-and-c\n  statement: In the data-derived network, with no uniform inhibition activity diverges or\n    collapses to the origin, small c leaves the collapse, a large regularization destroys the\n    manifold, and the flow error rises at both large and small lambda, with lambda 1e-8 just above\n    its minimum.\n  source: Supplementary Note 3, section 8.4; Supplementary Figs. 8 and 9\n  quote: At c = 0 the activity either diverges or collapses to the origin, depending on the\n    initial condition. Any c > 0 in the grid prevents the divergence, but small c leaves the\n    collapse. Additionally, λ can be too large ... Supplementary Fig. 9 shows the mean squared\n    flow rising with larger λ and also rising at small λ, where the optimization kernel becomes\n    ill-conditioned\n  data: dataset\n  depends_on:\n  - fig2b-sorted-weights-mexican-hat\n  criterion: As in notebooks/data_driven_reconstruction.ipynb, the lambda values 1e-12, 1e-10,\n    1e-8, 1e-6, 1e-4 and 1e-2 and the c values of its grid, 100 perturbed initial conditions,\n    trajectories projected on the top two principal components of the target manifold. Collapse\n    to the origin, final firing rates with a norm below one tenth of the manifold's (threshold\n    chosen here, open); divergence, non-finite or growing states. Flow error, the mean squared\n    flow on the target manifold. Reproduced when c 0 gives divergence or collapse, the largest\n    lambda gives collapse at c 1, and the flow error at 1e-8 is lower than at 1e-2 and at 1e-12.\n- id: figs11b-data-network-global-stability\n  statement: In the data-derived network, initial conditions far from the manifold converge to\n    points on it, with no spurious attractors, and initial conditions close to the origin converge\n    to one or a few states on the ring.\n  source: Supplementary Note 3, section 9.2; Supplementary Fig. 11b; Results, Dynamics of the\n    data-derived network model, paragraph 3\n  quote: Across the whole range, initial conditions converged to points on the target manifold,\n    with no spurious attractors apparent elsewhere in state space. In the data-derived network,\n    initial conditions close to the origin converge to one or a small number of states on the ring\n  data: dataset\n  depends_on:\n  - fig2b-sorted-weights-mexican-hat\n  criterion: Initial states i.i.d. Gaussian with zero mean and per-neuron standard deviations 1,\n    10, 50, 100 and 1,000, run for 30 s with c 1 (spurious_fixed_points.ipynb). Reproduced when,\n    at every standard deviation, at least 95% of final states lie within the distance to the\n    manifold reached at 20 s in fig2ef-data-network-quasicontinuous (threshold chosen here, open),\n    and at standard deviation 1 the final manifold angles fall in at most 5 states merged as in\n    fig2gi-circulant-noise-collapses.\n- id: figs14-data-spectrum-doublets\n  statement: In the data-derived weight matrix the leading eigenvalues are approximately real and\n    come in visible but inexact doublets.\n  source: Discussion, From world structure to circuit structure, paragraph 3; Supplementary Fig.\n    14a\n  quote: In our data-derived ... weight matrix, the eigenvalues are approximately real, and the\n    doublets are visible but not exact (Supplementary Fig. 14)\n  data: dataset\n  depends_on:\n  - fig2b-sorted-weights-mexican-hat\n  criterion: Eigenvalues of the matrix of fig2b-sorted-weights-mexican-hat (np.linalg.eigvals),\n    sorted by real part. The paper gives no measure; one is fixed here and named as open. Among\n    the leading 11 eigenvalues, approximately real, the absolute imaginary part is under 10% of\n    the real part; doublets, after setting aside the one eigenvalue that does not pair (the\n    constant mode, as in Fig. 6c), the gap within each consecutive pair is smaller than the gap\n    to the next pair for at least three of the first four pairs, and not every pair is exactly\n    equal (not exact).\n- id: fig6cd-eigenvalues-real-degenerate\n  statement: For tuning curves from the generative process at large N, the optimal weight matrix\n    has real, doubly degenerate eigenvalues, the products of the input-current and firing-rate\n    Fourier coefficients scaled by the average activation slope, and they match numerical\n    diagonalization at N = 2,500, with the ninth eigenvalue the unpaired constant mode.\n  source: Results, Weights in the large-network limit, paragraphs 3 and 4; Fig. 6c,d\n  quote: These eigenvalues are real and doubly degenerate, features inherited from ... and they\n    match numerical diagonalization at N = 2,500 (Fig. 6c,d)\n  data: elsewhere\n  where: github.com/davidclark1/symmetries-continuous-attractors at commit 245726f,\n    notebooks/spectra.ipynb (simulation code; no recorded data)\n  criterion: Run spectra.ipynb with N 2,500, sigma 1.42, beta 2.77, error-function activation,\n    N_theta 500, lambda 1e-8 (Methods, Settings 3, Simulation details). Reproduced when the\n    leading real parts pair up and agree with equation (9) as the notebook computes it, within\n    10%, and the imaginary parts of the leading eigenvalues are under 10% of their real parts.\n- id: fig6fg-disordered-eigenvectors\n  statement: Spectral embedding finds rings in a circulant matrix with weak noise, whose\n    eigenvectors are Fourier modes, but not in the model, whose eigenvector point clouds are\n    structureless, while eigenvalue degeneracy is present in every case, so degeneracy is proposed\n    as a robust signature of ring-attractor structure.\n  source: Results, Weights in the large-network limit, paragraphs 6 to 8; Fig. 6b,e,f,g\n  quote: This procedure reveals rings in circulant matrices, whose eigenvectors are Fourier modes,\n    but not in our model, where the point clouds from Vx and Vφ are structureless (Fig. 6f ...\n    Eigenvalue degeneracy, however, is present in every one of these cases\n  data: elsewhere\n  where: github.com/davidclark1/symmetries-continuous-attractors at commit 245726f,\n    notebooks/spectra.ipynb (simulation code; no recorded data)\n  criterion: Run spectra.ipynb (the model matrix, and the circulant matrix with the same large-N\n    eigenvalues plus Gaussian noise of standard deviation 0.1 / sqrt(N)). For the leading\n    eigenvector pairs of J J^T, the radius of each neuron's point from the origin; ring, a\n    coefficient of variation of the radius below 0.2; structureless, above 0.4 (thresholds chosen\n    here, open). Reproduced when the circulant pairs are rings, the model pairs are\n    structureless, and both spectra show the doublets.\n- id: fig7-dmft-mexican-hat-and-stability\n  statement: In the mean-field theory the effective interactions are circulant with a Mexican hat\n    profile set by sigma and beta; at a bump state all Jacobian eigenvalues have negative real\n    parts except the symmetry-induced zero, the uniform state has a real positive eigenvalue for\n    all sigma and beta (a Turing instability), and fixing Q destabilizes the bump.\n  source: Results, Dynamical mean-field theory, paragraphs 3 to 6; Fig. 7a,b,d,e,f\n  quote: has the Mexican hat profile characteristic of pattern-forming systems, with shape set by\n    the Fourier decay scale ... σ and sharpness β (Fig. 7a) ... At a bump state, all eigenvalues of\n    M(θ, θ′) have negative real parts except the symmetry-induced zero (Fig. 7f, teal curve)\n    ... a real, positive eigenvalue ... for all σ and β (a Turing instability) ... Fixing Q at Γx(0)\n    for all time, a manipulation with no analog in the high-dimensional network, destabilizes the\n    bump, producing a positive eigenvalue (Fig. 7f, orange)\n  data: elsewhere\n  where: github.com/davidclark1/symmetries-continuous-attractors at commit 245726f,\n    notebooks/dmft.ipynb and ring/dmft.py (theory code; no recorded data)\n  criterion: Run dmft.ipynb over its 40 by 20 grid of beta and sigma. Reproduced when the\n    interaction profiles of Fig. 7a are positive at 0 and negative at some offset for every\n    sigma and beta shown, the bump's second eigenvalue is negative and the uniform state's\n    leading eigenvalue positive at every grid point, and with Q fixed the bump has a positive\n    eigenvalue at sigma 1.42 and beta 2.77.\n- id: fig7c-dmft-integrates-behavior\n  statement: Under angular velocity input from mouse behaviour, the mean-field traveling-bump\n    solutions track head direction by integrating angular velocity, matching the network\n    simulations and the recordings.\n  source: Results, Dynamical mean-field theory, paragraph 5; Fig. 7c\n  quote: These solutions track head direction by integrating angular velocity (Fig. 7c), matching\n    both the network simulations (Fig. 2j,k) and the recordings (Fig. 2l)\n  data: dataset\n  depends_on:\n  - fig2jk-velocity-integration\n  criterion: Run dmft.ipynb's velocity simulation with sigma 1.42 and beta 2.77, Euler step 1 ms\n    (Methods equations (43) to (45)), driven by the angular velocity of A3707 prepared as in\n    fig2jk-velocity-integration (the hd_timeseries from closing_the_loop.ipynb), first 20 s\n    dropped. Tracking judged with the readings and thresholds of fig2jk-velocity-integration;\n    reproduced under either.\n- id: fig8-grid-scores-and-torus\n  statement: In the toroidal extension, sampled input-current maps show a continuous spread of grid\n    scores, as experimental grid scores do, the mean grid score rises monotonically with eta, the\n    network of 25,000 neurons converges to the toroidal manifold, and the weight matrix has\n    eigenvalue degeneracies in multiples of six, the first few sixfold.\n  source: Results, Grid cells, paragraphs 3 to 5; Fig. 8b,c,f; Supplementary Fig. 15\n  quote: The sampled maps produce the continuous spread of grid scores, as seen in the data (Fig.\n    8b,c). The mean grid score rises monotonically with η ... The network converges to the\n    toroidal manifold from nearby initial conditions (Fig. 8f). The weight matrix at large N\n    exhibits eigenvalue degeneracies in multiples of six, with the first few being sixfold\n  data: elsewhere\n  where: github.com/davidclark1/symmetries-continuous-attractors at commit 245726f,\n    notebooks/grid_sims.ipynb (simulation code; no recorded data). The experimental grid scores\n    of Fig. 8b are digitized from Nayebi et al. (NeurIPS 2021, Fig. 3a) by\n    figures/external/digitize_nayebi_fig3a.py, from data of Mallory et al. (Nat. Commun. 2021)\n  criterion: Run grid_sims.ipynb (sigma 12.12, nu 3, 1,000 maps for each eta in 0.2 to 1.0 for\n    the grid scores; sigma 4.04, beta 2.5, nu 1, N 25,000 for the network; N 2,500, lambda 1e-8\n    for the spectrum). Reproduced when the mean grid score increases at every step of eta, the\n    final network states lie closer to the target manifold than the initial ones for every\n    initial condition, and the leading eigenvalues after the constant mode fall in groups of six\n    within 10% of each other.\n- id: figs10-robustness-comparable\n  statement: Under added weight noise the disordered network and a circulant network with\n    proportional eigenvalues fragment into discrete states alike, so the two are comparably\n    robust.\n  source: Supplementary Note 3, section 9.1; Supplementary Fig. 10; Discussion, Order and disorder\n  quote: Across the range, the two systems are comparably robust\n  data: elsewhere\n  where: github.com/davidclark1/symmetries-continuous-attractors at commit 245726f,\n    notebooks/weight_matrix_analyses.ipynb (simulation code; no recorded data)\n  criterion: Run the notebook's weight-noise sweep (N 2,500, sigma 1.42, beta 2.77, noise levels 0\n    to 1, 34 initial conditions, 120 s). Reproduced when both networks keep a continuum at noise 0\n    and neither does at 0.4, as the supplement states, with the number of final states (merged\n    as in fig2gi-circulant-noise-collapses) reported for each level.\n- id: figs11-s12-global-stability-model\n  statement: In the generative-process network of 2,500 neurons, initial conditions far from the\n    manifold converge to it with no spurious attractors, and with growing N the dynamics approach\n    the mean-field behaviour, reliably converging to a ring by N = 1,000.\n  source: Supplementary Note 3, section 9.2; Supplementary Figs. 11a and 12\n  quote: By N = 1,000 the target manifold resembles a geometric ring and initial conditions\n    reliably converge to it\n  data: elsewhere\n  where: github.com/davidclark1/symmetries-continuous-attractors at commit 245726f,\n    notebooks/spurious_fixed_points.ipynb (simulation code; no recorded data)\n  criterion: Run spurious_fixed_points.ipynb. Reproduced when, at N 2,500, every final state lies\n    on the target manifold for all initial standard deviations (1 to 1,000), and at N 1,000 all\n    perturbed initial conditions converge to it, judged as in figs11b-data-network-global-stability.\n- id: figs1-s2-spectrum-does-not-fix-symmetry\n  statement: Eigenvalue degeneracy suggests but does not fix the symmetry group, since ensembles\n    matching the model's second-order statistics, and hence its spectrum, can differ beyond second\n    order and give different symmetry groups and attractors.\n  source: Discussion, Low-rank networks, symmetry and degeneracy, paragraph 1; Supplementary Figs.\n    1 and 2\n  quote: we can construct ensembles that match our model’s second-order statistics and hence its\n    spectrum, while differing beyond second order, yielding different symmetry groups and attractor\n    structures (Supplementary Figs. 1 and 2)\n  data: elsewhere\n  where: github.com/davidclark1/symmetries-continuous-attractors at commit 245726f,\n    notebooks/weight_matrix_analyses.ipynb (simulation code; no recorded data)\n  criterion: Run the notebook's rank-four Gaussian and mixture-of-Gaussians networks. Reproduced\n    when the two have the same leading eigenvalues within 5% and their dynamics differ as the\n    supplement's figures describe, a torus for the Gaussian loadings and separate rings for the\n    mixture (the notebook's printed ring radii and drift are reported).\n"
}
```

```
File created successfully at: claims/clark-2026.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Checking the Supp. Fig. 1 and 2 legends so that the last criterion matches what they show.

**Agent calls Bash**

```bash
sed -n 4005,4020p paper/*.txt; sed -n 4053,4065p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I had the two supplementary figures the wrong way round. Correcting that criterion.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/clark-2026.yaml",
 "old_string": "    when the two have the same leading eigenvalues within 5% and their dynamics differ as the\n    supplement's figures describe, a torus for the Gaussian loadings and separate rings for the\n    mixture (the notebook's printed ring radii and drift are reported).",
 "new_string": "    when the two have the same leading eigenvalues within 5% and their dynamics differ as the\n    legends describe. With Gaussian loadings (N 10,000, K 4, 40 initial conditions, 10 tau) the\n    final states form a ring in the dominant doublet and collapse to the origin in the\n    subdominant one (a single ring). With mixture loadings they form a ring in both doublets (the\n    full torus). Collapse is a final radius below one tenth of the ring radius (threshold chosen\n    here, open). The notebook's printed ring radii and drift are reported."
}
```

```
The file claims/clark-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/clark-2026.yaml",
 "old_string": "  statement: Eigenvalue degeneracy suggests but does not fix the symmetry group, since ensembles\n    matching the model's second-order statistics, and hence its spectrum, can differ beyond second\n    order and give different symmetry groups and attractors.",
 "new_string": "  statement: Eigenvalue degeneracy suggests but does not fix the symmetry group, since ensembles\n    matching the model's second-order statistics, and hence its spectrum, can differ beyond second\n    order and give different symmetry groups and attractors (a single ring for Gaussian loadings,\n    the full torus for mixture-of-Gaussians loadings, in a rank-four network)."
}
```

```
The file claims/clark-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/clark-2026.yaml paper/10.1038-s41593-026-02452-4.txt; echo "exit $?"; grep -n -- "—\|rather" claims/clark-2026.yaml; python3 -c "
import yaml,re
d=yaml.safe_load(open('claims/clark-2026.yaml'))
print(len(d['claims']))
" ; grep -n "[^\"'|>]: " claims/clark-2026.yaml | grep -v "^[0-9]*:\s*-\? *[a-z_]*: " | head
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes: 29 claims, 29 quotes, 0 problems. One last check that no plain-scalar value contains a colon-space.

**Agent calls Bash**

```bash
python3 -c "
import yaml
d=yaml.safe_load(open('claims/clark-2026.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+'/'+str(i))
    elif isinstance(x,str) and ': ' in x: print(p, x[:80])
walk(d)
c=d['claims']; print('criteria',sum('criterion' in x for x in c),'stats',sum('statistics' in x for x in c),'expected',sum('expected' in x for x in c))
from collections import Counter; print(Counter(x.get('data','dataset') for x in c), Counter(x.get('kind','finding') for x in c))
"; git status --short claims/
```

```
criteria 29 stats 1 expected 4
Counter({'dataset': 21, 'elsewhere': 7, 'with_inputs': 1}) Counter({'finding': 27, 'link': 2})
?? claims/clark-2026.yaml
```

**Agent**

I wrote `claims/clark-2026.yaml`, and the quote checker passes it with 0 problems. Nothing was committed.

**Text read.** The version of record (a PDF supplied by a person, extracted to text): main text, figure legends, Methods, Data and Code availability, the Reporting Summary, and the full Supplementary Information (Notes 1 to 4, Supp. Figs. 1 to 16). Nothing a claim needed was missing, and I opened no figure pages.

**Code read.** `github.com/davidclark1/symmetries-continuous-attractors` at commit `245726fa78457e10cdcf17e6be36fba1dec98061`. It settled most of the method details the Methods leave open, and the opening comment lists them. Two discrepancies:
- **Cell selection.** The paper calls the 1,533 cells "excitatory", but the code selects on `is_head_direction` alone.
- **Zenodo record for the cached results.** The paper cites 21827768 and the code's README gives 21827767.

**Claims.** 29 in all: 27 findings and 2 link checks.
- All 29 have quotes and a criterion; none needed an `inferred` note.
- One has statistics: the Kuiper test with Benjamini–Hochberg correction (lowest corrected P = 0.59).
- Four have expected values: cell counts, Fig. 5d peak numbers, Kuiper counts and P range, and the fitted (σ, β, b).
- Data: 21 use the dataset alone. One link check also needs the paper's cached tuning curves on Zenodo. Seven are theory or simulation claims (Figs. 6, 7a/d–f and 8, Supp. Figs. 1, 2 and 10–12) marked `elsewhere`, with the code repository as their source.

**Open details and the readings named:**
- **Cell selection:** (a) `is_head_direction` alone, as the code does; (b) also `is_excitatory`.
- **Fig. 1f,g "comparable in magnitude":** (a) the SD peak is between half and twice the mean peak; (b) the SD exceeds half the mean at offset 0. The thresholds I fixed for "unimodal", "symmetric" and "consistent across mice" are also flagged as open.
- **Fig. 3c "approaches circulant":** relative distance from the diagonal-averaged circulant matrix, falling as the subset grows. Supp. Fig. 13 adds an 80% single-frequency power test on the eigenvectors.
- **Fig. 5a,b "match":** (a) the model profile lies within the range of the 31 mouse profiles; (b) its peak is within 10% of the mouse average.
- **Fig. 5c agreement:** (a) total variation distance; (b) Hellinger distance.
- **Fig. 5d, 5f:** median within 10%, or Kolmogorov–Smirnov distance below 0.15.
- **Fig. 5e, where the tail begins:** correlation below (a) 0.5 or (b) 0.
- **Fig. 2f "within ~1 s":** (a) distance at 1 s at most a tenth of the starting distance; (b) at most twice its value at 20 s. **"Persist over 30 s":** (c) angle drift under 2π/20 for 90% of trajectories; (d) at least 50 distinct final bins.
- **Fig. 2i "a few discrete states":** at most 10 states after merging within 2π/50, against at least 50 for the optimal weights.
- **Tracking (Figs. 2j,k, 2l, 7c):** (a) median circular error below π/8; (b) circular correlation of at least 0.9.
- **Also flagged as open:** the thresholds for Supp. Fig. 14 ("approximately real", "doublets"), the collapse and spurious-state thresholds in Supp. Figs. 8, 11 and 12, and the ring-versus-structureless test in Fig. 6f,g.
- **Fit tolerance on β:** set to one grid step (0.345), not the default 10% (0.277), because the paper's grid search can only land on grid points.

**Missing from the paper.** Nothing a claim needed. The paper simply reports no quantitative measure of agreement for most of its qualitative findings, which is why the readings above are named as open.

## End of run

39 turns, 7 minutes, $3.50 at API prices, result: success.
