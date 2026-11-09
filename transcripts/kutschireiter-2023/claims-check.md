# 000289 · claims-check · run 39990354647

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/000289/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; cat claims/000289/*.yaml; python tools/claims_check.py claims/000289/10.1073-pnas.2210622120.yaml paper/10.1073-pnas.2210622120.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/c5802308-6b94-4e1a-be20-5de3acf7485a/tool-results/b4sod73s3.txt"
}
```

```
1	## Reader
2	
3	### 1. Get the paper
4	
5	The workflow puts the paper's full text, and its PDF where there is one, under
6	`paper/`: the main text, the Methods, and the supplement. Read the text; open
7	the PDF only to read a figure or a table the text garbles. If the full text is
8	not there, or lacks the Methods or a supplement the results rest on, stop:
9	write no claims, and end with a report that names what is missing, so that it
10	can be supplied. Never write claims from the abstract. Do not copy figures.
11	Do not look at the dataset's data: its title and description on the archive
12	are enough to know which paper and which experiments it is meant to hold.
13	
14	### 2. Read the paper's code
15	
16	Read the code the paper links to before writing criteria. Say what it holds,
17	and record the repository and commit read. Where the Methods leave a choice
18	open and the code settles it, follow the code and say so. Where they disagree,
19	follow the Methods for the main result and name the code's choice as a
20	variant. When more sources disagree (the Methods, the analysis code, the
[... 495 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; ls; ls code 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2210622120.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the main text through the Neural Noise and Drosophila sections. Next, the Discussion, Methods and SI.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1073-pnas.2210622120.txt').read()
print(s[51400:95000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/c5802308-6b94-4e1a-be20-5de3acf7485a/tool-results/bc9mevz42.txt"
}
```

```
1	ngular velocity observations over time is called angular path integration. Angular path integration is inherently noisy, and therefore, uncertainty will grow progressively when HD observations are lacking. Our Bayesian ring attractor network is notable in explicitly treating angular path integration as a problem of probabilistic inference. Each angular velocity observation has limited reliability, and this causes the bump amplitude to decay in our network as long as HD observations are absent, in a manner that well approximates the certainty decay of an ideal observer. In this respect, our network differs from previous investigations of ring attractors having variable bump amplitude ( 55 ). Our work makes several testable predictions. First, we predict that the HD system should contain the connectivity motifs required for a Bayesian ring attractor. Our analysis of Drosophila brain connectome data supports this idea; we expect similar network motifs to be present in the HD networks of other animals, such as that of mice ( 15 , 19 ), monkeys ( 56 ), humans ( 57 ), or bats ( 58 ). In the future, it will be interesting to determine whether synaptic inhibition in these networks is nonlinear, as predicted by our models. Second, we predict that bump amplitude in the HD system should vary dynamically, with higher amplitudes in the presence of reliable external HD cues, such as salient visual landmarks. In particular, when bump amplitude is high, the bump’s position should be less sensitive to the appearance of new external HD cues. Notably, an experimental study from the mouse HD system provides some initial support for these predictions ( 19 ). This study found that the amplitude of population activity in HD neurons (what we call bump amplitude) increases in the presence of a reliable visual HD cue. Bump amplitude also varied spontaneously when all visual cues were absent (in darkness); intriguingly, when the bump amplitude was higher in darkness, the bump position was s
[... 168 more lines not kept]
```

**Agent**

Main text and Methods read. Now the SI Appendix, mainly sections 4 and 5 and the figure legends.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1073-pnas.2210622120.txt').read()
i=s.find('[SUPPLEMENT'); print(i)
import re
for m in re.finditer(r'Fig(ure)?\.? ?S\d', s): pass
for k in ['Supplementary Information','SI Appendix','Neural noise','Fig. S2','Figure S','hemibrain','PEN1']:
  print(k,[m.start() for m in re.finditer(k,s)][:40])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1073-pnas.2210622120.txt').read()
open('/tmp/claude/si.txt','w').write(s[108000:])
" 2>/dev/null || python3 -c "
import os
s=open('paper/10.1073-pnas.2210622120.txt').read()
open(os.environ['TMPDIR']+'/si.txt','w').write(s[108000:])"; echo $TMPDIR; fold -w 200 -s $TMPDIR/si.txt 2>/dev/null | wc -l
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; ls; f=$(ls -t */si.txt si.txt 2>/dev/null | head -1); echo $f; python3 -c "
import os
s=open('paper/10.1073-pnas.2210622120.txt').read()[108000:]
import textwrap
open(os.environ['TMPDIR']+'/si_w.txt','w').write('\n'.join(textwrap.fill(p,200) for p in s.split('\n')))"; wc -l $TMPDIR/si_w.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Fig\\. S\\d|Figure S\\d|^\\s*\\d\\. |Section|noise|Δ7|PEN|connectome|four|halve|independent of the number",
 "path": "/tmp/claude-1001/si_w.txt",
 "output_mode": "content",
 "head_limit": 150
}
```

```
96:Connectivity motifs in the Drosophila HD system connectome . . . . . . . . . . . . . . . . . . . . . . . . . . . .
99:A multi-network model mimicking the Drosophila HD system connectome . . . . . . . . . . . . . . . . . . . . .
120:The impact of neural noise on inference dynamics
123:The qualitative impact of neural noise on inference dynamics
127:How neural noise quantitatively impacts the dynamics of μt and κt . . . . . . . . . . . . . . . . . . . . . . . . .
130:The impact of neural noise on x1 and x2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
133:The impact of neural noise on μ and κ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
136:Neural noise models
150:1. Circular Kalman filtering
162:and HD φt, respectively, and are corrupted by zero-mean noise at each point in time:
460:the ‘true’ generative model in Eq. [S1], they automatically inherit the noise of the process that was used to generate φt.
684:histograms in Fig. S5.
689:2. Neural encoding example: encoding of the von Mises distribution with a linear probabilistic population code
694:the case of a linear probabilistic population code (lPPC) (6–8) with independent Poisson neural noise. The central idea behind
893:In Fig. S1, we demonstrate these limits (assuming ξ = 1 without loss of generality), and find numerically that linear scaling
894:of the population activity amplitude holds well even for small κt (e.g., κt ∼1, cf. Fig. S1f). In addition, the width of the profile
897:probability distribution (Fig. S1c), because an increase in certainty does not cause the bump to sharpen indefinitely.
928:where R collectively denotes the orthogonal other Fourier modes. In Fig. S1g-j, we confirm the proportionality of the amplitudes
934:3. Details on Bayesian ring attractor dynamics and parameter tuning
1278:Fortunately, the problem can be solved “backwards” using the analogy to coordinate transforms in Section C, thereby restricting
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '1301,1330p;2440,2495p;2650,2690p;2850,2945p' /tmp/claude-1001/si_w.txt
```

```
4. Details on Drosophila-like network
Relying on large-scale connectomics data of the Drosophila HD system (10, 11), we now ask if a Bayesian ring attractor can be
implemented in a network that obeys biological network connectivity constraints. Here we show how the motifs of this network
– and, by extension, any biological ring attractor network – could potentially implement dynamic Bayesian inference.
A. Connectivity motifs in the Drosophila HD system connectome. The ring attractor in the Drosophila HD system is composed
of three core cell types, called EPG, PEN1 and ∆7 neurons (10–12), cf. Fig. 4A,B. HD is represented as a bump of neural
activity in the EPG population (13). These neurons are recurrently connected with excitatory PEN1 neurons. When the fly
turns, this differentially activates PEN1 neurons in the right and left brain hemispheres, and because PEN1 neurons have
asymmetric (shifted) projections back to EPG neurons, they can rotate the bump of EPG activity in accordance with the fly’s
rotation (14, 15). This motif effectively establishes the velocity-modulated odd recurrent connectivity required to initiate turns
in ring attractor networks (Fig. 4D). Moreover, EPG neurons are recurrently connected with inhibitory ∆7 neurons, which
establishes broad inhibition (Fig. 4E). Finally, EPG neurons receive inhibitory inputs from so-called ER neurons, which send
HD information to EPG neurons (16–18) (Fig. 4F). In summary, the fly’s HD system is equipped with the basic motifs to
implement a Bayesian ring attractor.
B. A multi-network model mimicking the Drosophila HD system connectome. The main idea of the idealized network in the
previous section was to tune the network parameters such that the circKF (or the quadratic approximation of the circKF) was
implemented in the coefficients of the first Fourier mode. Here, we will use the connectome of the fruit fly Drosophila (10) to
build a recurrent neural network, and show that the quadratic approximation of the cir
[... 205 more lines not kept]
```

**Agent**

Now I check the code claims against the deposited repository, if it can be reached.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone -q https://github.com/DrugowitschLab/BayesianRingAttractor.git bra 2>&1 | tail -3; cd bra 2>/dev/null && git log --oneline -3 && git tag && ls -R | head -80
```

```
a9db6f9 Update readme
668cb31 Added readme's to data_raw subfolders
a0de8e9 Update README.md
v1.0
.:
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
[... 50 more lines not kept]
```

**Agent**

The repository is reachable at the commit the file cites. I'll dump the notebooks' code cells to check the criteria's code details.

**Agent calls Bash**

```bash
cd $TMPDIR/bra && python3 - <<'E'
import json,glob
for f in sorted(glob.glob('*.ipynb')):
    nb=json.load(open(f))
    src='\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code')
    open(f+'.py','w').write(src)
    print(f, len(src))
E
wc -l *.py
```

```
Figure2a,c_FigureS1.ipynb 7142
Figure2h.ipynb 4870
Figure2i.ipynb 5531
Figure3b,c,e,d_FigureS3.ipynb 14052
Figure3f_FigureS4.ipynb 4907
Figure4g,h.ipynb 3627
FigureS2.ipynb 1838
  209 Figure2a,c_FigureS1.ipynb.py
  127 Figure2h.ipynb.py
  136 Figure2i.ipynb.py
  318 Figure3b,c,e,d_FigureS3.ipynb.py
  119 Figure3f_FigureS4.ipynb.py
   84 Figure4g,h.ipynb.py
   54 FigureS2.ipynb.py
  620 circularFiltering.py
  185 network_filter.py
   89 performance_scan_figure2i.py
   71 performance_scan_figure3d.py
   78 performance_scan_figure3f.py
   68 performance_scan_figure4g.py
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bra && cat Figure2h.ipynb.py Figure2i.ipynb.py "Figure3f_FigureS4.ipynb.py" FigureS2.ipynb.py
```

```
%load_ext autoreload
%autoreload 2

import numpy as np
import matplotlib.pyplot as plt
import circularFiltering as flt
import matplotlib
matplotlib.rcParams.update({'font.size': 14,
                            'pdf.fonttype': 42,
                            'ps.fonttype': 42})
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
####### simulation parameters
np.random.seed(42)
T = 15
dt = 0.01
t = np.arange(0,T,dt)
kappa_phi = 1 # inverse diffusion constant
kappa_v = 2 # precision of relative heading info
kappa_z = 15 # precision of absolute heading info (called gamma_z in manuscript)
[... 417 more lines not kept]
```

**Agent**

Several code facts check out. Next: the Fig. 3 notebook, Fig. 4 notebook, the scan scripts, and the filter functions.

**Agent calls Bash**

```bash
cd $TMPDIR/bra && cat "Figure3b,c,e,d_FigureS3.ipynb.py" | grep -v "^\s*ax\|set_\|plt\.\|rcParams\|rc(" | head -250
```

```
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import circularFiltering as flt
from scipy.stats import vonmises
from scipy.stats import norm
import matplotlib
import glob
import os
import re
from matplotlib import rc
preprocess = False # only set to True if you want to re-run preprocessing on data in /data_raw

path_raw = 'data_raw/figure2i/'
path_processed = 'data_processed/'
kappa_z_array = ([1.e-02, 3.e-02, 1.e-01, 2.e-01, 3.e-01, 4.e-01, 5.e-01, 6.e-01,
       7.e-01, 8.e-01, 9.e-01, 1.e+00, 2.e+00, 3.e+00, 4.e+00, 5.e+00,
       6.e+00, 7.e+00, 8.e+00, 9.e+00, 1.e+01, 3.e+01, 1.e+02])

kappa_array = np.array([  0.1,   0.3,   0.9,   1. ,   1.1,   1.2,   1.3,   1.4,   1.5,
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bra && grep -v "^\s*ax\|set_\|plt\.\|rcParams\|rc(" "Figure4g,h.ipynb.py"; grep -n "nIter\|dt *=\|kappa_y\|kappa_v\|def objective\|N *=" performance_scan_*.py | head -60; grep -n "^def \|kappa_y\|kappa_v\|sigma\|noise" circularFiltering.py | head -80
```

```
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import circularFiltering as flt
from scipy.stats import vonmises
from scipy.stats import norm
import matplotlib
import glob
import re
import os
                            'pdf.fonttype': 42,
                            'ps.fonttype': 42})
from matplotlib import rc
preprocess = False # only set to True if you want to re-run preprocessing on data in /data_raw

path_raw = 'data_raw/figure4g/'
path_processed = 'data_processed/'
# make unique list of parameter values
fileNames = glob.glob(os.path.join(path_raw+"*.npz"))
kappa_z_array = np.array( [ re.findall('(?<=kappaz=)(.*)(?=\.)', name) for name in fileNames ] )[:,0]
[... 155 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bra && sed -n 18,34p circularFiltering.py; sed -n 160,187p circularFiltering.py; sed -n 438,521p circularFiltering.py; sed -n 1,40p performance_scan_figure4g.py; sed -n 40,60p performance_scan_figure3f.py
```

```
def A_Bessel(kappa): 
    """Computes the ratio of Bessel functions."""
    r = i1(kappa)/i0(kappa)
    return r

def xi_fun_inv(dt):
    """Computes the inverse of the ratio of Bessel functions by root-finding."""
    f = lambda alpha: alpha * A_Bessel(alpha) - dt
    sol = root_scalar(f,bracket=[0.001,50],method='brentq')
    alpha = sol.root
    return alpha

def f_kappa(kappa): 
    """ Computes the precision decay function in the circKF. """
    f = A_Bessel(kappa)/(kappa-A_Bessel(kappa)-kappa*A_Bessel(kappa)**2)
    return f

    
    Output:
    mu_out      - mean estimate after update
[... 171 more lines not kept]
```

**Agent**

The code confirms most of the header. Two more things to check: whether `RNN_filter_Run` can run at all (its body uses `z`, which is not a parameter), and the Fig. 2H decoder scaling.

**Agent calls Bash**

```bash
cd $TMPDIR/bra && grep -n "^z\b\|^z *=\|global" circularFiltering.py; python3 -c "
import numpy as np, circularFiltering as f
try:
  f.RNN_filter_Run(0.05,N=8,w_even=1.5,w_quad=0.5,tau=1,kappa_0=1,sigma_N=1)
  print('ok')
except Exception as e: print(type(e).__name__, e)
print(f.xi_fun_inv(0.1), f.xi_fun_inv(0.01))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, circularFiltering as f
ModuleNotFoundError: No module named 'numpy'
```

**Agent**

Numpy isn't installed here, but `z` is neither a parameter of `RNN_filter_Run` nor a module global (the grep found nothing), so the function raises NameError. I'm editing the file now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "old_string": "#     functions in circularFiltering.py take kappa_v; a rerun needs that keyword renamed.",
 "new_string": "#     functions in circularFiltering.py take kappa_v; a rerun needs that keyword renamed.\n#   - RNN_filter_Run uses z in its body but has no z parameter, and the module defines no z, so\n#     it raises NameError as released (performance_scan_figure3f.py passes z=z); a rerun needs\n#     z=None added to its signature.\n#   - Figure4g,h.ipynb reads the information rates from the file names in data_raw/figure4g/,\n#     which is empty; the rates are the 23 listed in performance_scan_figure4g.py (0.01 to 100).\n#   - Fig. 3C: the notebook computes the weight as arctan2(alpha, kappa) / (pi/2) with alpha =\n#     xi_fun_inv(rate * 0.1), a 100-ms observation; the Methods give w = (1/pi) tan^-1(kappa_z dt /\n#     kappa_t) and the legend a 10-ms observation."
}
```

```
The file claims/000289/10.1073-pnas.2210622120.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "old_string": "    The update is the vector addition of Fig. 1 D and E and the observation term of Eq. 9 (kappa\n    changes by kappa_z cos(z - mu) dt). From the code's circKF (vM_Projection_Run, kappa_phi = 1,\n    kappa_v = 1, dt = 0.01), take a state with certainty kappa_t (any of 1, 2, 5) and apply one step\n    with an HD observation at z = mu (confirmatory) and one at z = mu + pi (opposite), with an\n    observation reliability below kappa_t. Compare the certainty after the step with (a) the\n    certainty before it and (b) the certainty after the same step with no observation (kappa_z = 0).\n    Reproduced when, under both comparisons and every kappa_t, the confirmatory observation gives\n    higher and the opposite one lower certainty.",
 "new_string": "    The update is the vector addition of Fig. 1 D and E and the observation term of Eq. 9 (kappa\n    changes by kappa_z cos(z - mu) dt). In the code's circKF step (vM_Projection in\n    circularFiltering.py, kappa_phi = 1, kappa_v = 1, dt = 0.01) the observation enters as that\n    vector addition on the natural parameters, followed by the prediction step. Take a state with\n    certainty kappa_t (any of 1, 2, 5) and apply one step with an HD observation at z = mu\n    (confirmatory) and one at z = mu + pi (opposite). The paper fixes no single reliability for\n    this; use the per-step reliabilities the Methods give, xi_fun_inv(gamma_z dt) for gamma_z = 1/s\n    (Fig. 3E) and 10/s (Fig. 2H). Compare (a) the certainty right after the observation update with\n    the certainty before it (the update of Fig. 1 D and E alone, before the prediction step), and\n    (b) the certainty after the full step with the certainty after the same step with no\n    observation (kappa_z = 0). Reproduced when, under both comparisons, every kappa_t and both\n    reliabilities, the confirmatory observation gives higher and the opposite one lower certainty."
}
```

```
The file claims/000289/10.1073-pnas.2210622120.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "old_string": "    second reading of the cue strength. Bump position and amplitude are decoded as in the Methods\n    (x = A r, position arctan2(x2, x1), amplitude the vector length). The paper",
 "new_string": "    second reading of the cue strength. Bump position and amplitude are decoded as in the Methods\n    (x = A r, position arctan2(x2, x1), amplitude the vector length), with the notebook's scaling\n    x = (2/N) A r, which puts the amplitude on the scale of kappa. The paper"
}
```

```
The file claims/000289/10.1073-pnas.2210622120.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "old_string": "    In the notebook, Fig. 3C plots the weight w = atan(kappa_z dt / kappa_t) / (pi/2) as a map\n    and draws on it each model's mean certainty against information rate: circKF\n    (vonMises_stats[0,:,2]) and Bayesian attractor (vonMises_q_stats[0,:,2]), both as Fisher\n    information xi(kappa); the conventional attractor is a constant kappa*. Compute, at each of\n    the 23 rates, the weight for a 90 degree observation under the circKF's and under the\n    attractor's mean certainty. The paper gives no bound for \"close\"; readings: the absolute\n    weight difference is at most (a) 0.02 or (b) 0.05 at every rate of 1/s and above. Reproduced\n    when both readings hold and the largest difference falls at rates below 1/s (Fig. S3, \"only\n    deviates ... for very uninformative observations\").",
 "new_string": "    In the notebook, Fig. 3C plots the weight for a 90 degree observation as a map over the\n    observation's and the posterior's informativeness and draws on it each model's mean certainty\n    against information rate: circKF (vonMises_stats[0,:,2]) and Bayesian attractor\n    (vonMises_q_stats[0,:,2]), both as Fisher information xi(kappa); the conventional attractor is\n    a constant kappa*. Compute, at each of the 23 rates, the weight under the circKF's and under\n    the attractor's mean certainty, with the per-observation reliability alpha = xi_fun_inv(rate x\n    Delta t). The Methods and the code differ on the weight: readings (i) the Methods, w = (1/pi)\n    tan^-1(alpha / kappa) with Delta t = 0.01 (10-ms observation, Fig. 3C legend and Methods);\n    (ii) the notebook, w = arctan2(alpha, kappa) / (pi/2) with Delta t = 0.1. The paper gives no\n    bound for \"close\"; readings: the absolute weight difference is at most (a) 0.02 or (b) 0.05 at\n    every rate of 1/s and above. Reproduced when every combination holds and the largest\n    difference falls at rates below 1/s (Fig. S3, \"only deviates ... for very uninformative\n    observations\")."
}
```

```
The file claims/000289/10.1073-pnas.2210622120.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "old_string": "    normalizations of fig3f-noise-drop-below-70. Reproduced when the reduction is within 31.5 to\n    38.5% under every reading and the retuned",
 "new_string": "    normalizations of fig3f-noise-drop-below-70. These are readings of which number the 35% is,\n    so the value part holds when the reduction is within 31.5 to 38.5% under at least one of them\n    (every reading is shown). Reproduced when the value part holds and the retuned"
}
```

```
The file claims/000289/10.1073-pnas.2210622120.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "old_string": "    RNN_filter_Run at the Bayesian ring attractor's parameters (kappa* = 1, beta = 0.5, tau = 1),\n    with no HD input",
 "new_string": "    RNN_filter_Run (with z=None added to its signature, see the code notes above) at the Bayesian\n    ring attractor's parameters (kappa* = 1, beta = 0.5, tau = 1, so w_even = 1.5 and w_quad = 0.5\n    as in performance_scan_figure3f.py; stoch_corr 0, since it corrects for angular velocity\n    input, which is absent here), with no HD input"
}
```

```
The file claims/000289/10.1073-pnas.2210622120.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000289/10.1073-pnas.2210622120.yaml",
 "old_string": "    From figure4g.npz as Figure4g,h.ipynb reads it, compare the Drosophila-like network (CX_stats)\n    with the Bayesian ring attractor (vonMises_q_stats) at every information rate stored.",
 "new_string": "    From figure4g.npz as Figure4g,h.ipynb reads it, compare the Drosophila-like network (CX_stats)\n    with the Bayesian ring attractor (vonMises_q_stats of the same file, same runs, dt = 0.001) at\n    every information rate stored (the 23 rates of performance_scan_figure4g.py, since the\n    notebook's glob over the empty data_raw/figure4g/ yields none)."
}
```

```
The file claims/000289/10.1073-pnas.2210622120.yaml has been updated successfully.
```

**Agent**

Now the `checks` entry.

**Agent calls Bash**

```bash
cd  grep -n "^checks\|^[a-z_]*:" claims/000289/*.yaml; tail -3 claims/000289/*.yaml; grep -rn "checks:" -A8 claims/000294/*.yaml | head -20
```

```
72:schema_version: 2
73:dataset:
76:paper: doi:10.1073/pnas.2210622120
77:claims:
    blocked as methods_underspecified when they differ. The second half of the prediction (a high
    bump amplitude makes the bump position less sensitive to new cues) has no measure in the paper
    and is not tested.
519:checks:
520-- date: 2026-10-23
521-  kind: agent
522-  model: claude-opus-5-5
523-  ready: true
524-  changes:
525-  - mea-electrodes-and-rates. Methods 5.2 say APWaveform was recorded at high sampling rates (typically 200 kHz); the criterion required 20 kHz for every patch series. It now accepts 20 or 200 kHz for APWaveform.
526-  - fig3b-ap-initiates-distal-ais. The protocol (IDrest 300%, averaged spike cutouts) is now taken from 7-AIS-test.ipynb. The -20 mV crossing as the initiation time was a choice not in the paper; it is now one of two readings, with the AP peak time.
527-  - fig4b-extra-better-than-soma. The criterion fixed the Holm family at the three soma comparisons, which the paper does not say; the code corrects over all six pairs. Both are now readings.
```

**Agent calls Bash**

```bash
cd  cat >> claims/000289/10.1073-pnas.2210622120.yaml <<'E'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header. Added three code points read in BayesianRingAttractor commit a9db6f9 that the criteria rely on (RNN_filter_Run has no z parameter and raises NameError as released; Figure4g,h.ipynb takes its rates from the empty data_raw; the Fig. 3C weight in the notebook differs from the Methods in scale and observation duration).
  - fig1-conflict-decreases-certainty. Comparison (a) mixed the prediction decay into the step, so a confirmatory observation weaker than the decay would fail, and the reliability was left to the analyst ("below kappa_t"). Comparison (a) is now the observation update alone (the vector addition in vM_Projection, Fig. 1 D and E), and the reliabilities are the Methods' per-step values for gamma_z = 1/s and 10/s.
  - fig2h-bump-tracks-circkf. Named the decoder scaling (2/N) A r used by Figure2h.ipynb; the Methods' x = A r has no scale, and the decay test compares the amplitude with kappa* = 1.
  - fig3c-update-weights. The criterion used the notebook's weight without saying that the Methods define w with 1/pi and a 10-ms observation while the notebook uses 2/pi and 100 ms; the per-observation reliability was not given. Both are now readings, with alpha = xi_fun_inv(rate x Delta t).
  - fig3f-retuning-reduces-drop. The noise level and normalization are readings of which number the 35% is; protocol step 3 says such a number is reproduced when it matches under any reading. The criterion required every reading; now any, with all shown.
  - noise-effects-on-mu-and-kappa. RNN_filter_Run cannot run as released; the criterion now says z=None must be added. The network weights (w_even 1.5, w_quad 0.5, from performance_scan_figure3f.py) and stoch_corr (0, as there is no angular velocity input) are now stated.
  - fig4gh-drosophila-network-matches. Stated that the reference is vonMises_q_stats of figure4g.npz (same runs, dt 0.001) and where the rates come from.
  - Open. Several criteria judge unquantified words ("similar", "close", "indistinguishable", "mostly", "broad") with thresholds the paper does not give (0.01 and 0.02 accuracy, 0.9 correlation, 0.02 and 0.05 weight, more than half of positions). They are named as readings, but an outcome that hinges on them rests on the reader's bounds.
  - Open. fig3b-bayesian-beats-conventional requires the Bayesian attractor to be at least as accurate at all 23 rates; at 30 and 100/s both are near 1 and the conventional runs (kappa* other than 0.1) use different trajectories, so sampling noise alone could give a small negative difference.
  - Open. prediction-bump-amplitude-cue-reliability. The paper gives no experimental method; the test readings (per-fly majority, one-sided Wilcoxon over flies) and signal readings are the reader's, named as such. The dataset belongs to a different study (Basnak et al.), which this paper does not analyse.
  - Coverage checked. Each main finding (circKF conflict effect, network tracking, attractor vs conventional, beta and kappa* scan, neural noise, connectome motifs, Drosophila network, network size, prediction) has a claim; all claims come from this paper and its code. No statistics are reported in the paper, and none are recorded.
E
python tools/claims_check.py claims/000289/10.1073-pnas.2210622120.yaml paper/10.1073-pnas.2210622120.txt; grep -nP '—|rather' claims/000289/*.yaml | grep -v "^[0-9]*:  *[a-z]" | head; grep -n "rather" claims/000289/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/000289/*.yaml | grep -n ': ' | grep -v '^\s*[0-9]*:\s*\(- \)\?\(date\|kind\|model\|ready\|changes\):'; git status --short
```

```
M claims/000289/10.1073-pnas.2210622120.yaml
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

**Agent**

The checker passes: `claims/000289/10.1073-pnas.2210622120.yaml: 13 claims, 13 quotes, 0 statistical values, 0 problems`. The file is ready for an attempt (`ready: true`), with the open points below recorded under `checks`.

The paper is a theory and simulation paper. It has no imaging data and reports no statistical tests. The dataset belongs to a different study (Basnak et al.), so only the prediction claim points at it. I checked the code details in the criteria against the paper's repository (DrugowitschLab/BayesianRingAttractor, commit a9db6f9).

**Changes, by claim**
- **Header:** I added three code facts the criteria rely on:
  - `RNN_filter_Run` uses `z` but has no `z` parameter, so it fails (NameError) as released.
  - `Figure4g,h.ipynb` reads its information rates from an empty folder.
  - The Fig. 3C weight in the notebook differs from the Methods: it is scaled by 2/π, not 1/π, and assumes a 100-ms observation, not 10 ms.
- **fig1-conflict-decreases-certainty:** Comparison (a) included the certainty decay of the prediction step, and the observation strength was left to the analyst, which could change the outcome. Comparison (a) now tests the observation update alone (the vector addition of Fig. 1 D and E). The strengths are now the per-step values from the Methods for information rates of 1/s and 10/s.
- **fig2h-bump-tracks-circkf:** I stated the notebook's decoder scaling, (2/N)·A·r. The decay test compares the amplitude with the baseline κ* = 1, so the scale matters.
- **fig3c-update-weights:** The Methods' weight (1/π, 10-ms observation) and the notebook's (2/π, 100 ms) are now both readings, and I said how the observation strength is computed from the rate.
- **fig3f-retuning-reduces-drop:** Which noise level and normalization the 35% refers to are readings of one reported number. The protocol says such a number counts as reproduced if it matches under any reading; the criterion had required all of them, and now requires any.
- **noise-effects-on-mu-and-kappa:** The criterion now says the code fix the run needs (adding `z=None`). It also states the network weights and sets the angular-velocity correction term to 0, since there is no angular-velocity input.
- **fig4gh-drosophila-network-matches:** The reference is now the Bayesian attractor results stored in the same file (same runs, time step 0.001), and the rates come from the scan script.

**Open**
- **Thresholds for vague words:** Several criteria judge words like "similar", "close", "indistinguishable", "mostly" and "broad" with cut-offs the paper does not give. They are named as readings, but an outcome that depends on them rests on the claim writer's bounds.
- **fig3b:** The criterion requires the Bayesian attractor to be at least as accurate at all 23 rates. At the two highest rates both models are near 1 and were run on different trajectories, so sampling noise alone could make the difference slightly negative.
- **prediction-bump-amplitude-cue-reliability:** The paper gives no experimental method. The test readings (a per-fly majority, or a one-sided Wilcoxon test over flies) and the choice of signal are the claim writer's, named as such.

Every main finding has a claim, and all claims come from this paper and its code. I did not commit anything.

## End of run

30 turns, 4 minutes, result: success.
