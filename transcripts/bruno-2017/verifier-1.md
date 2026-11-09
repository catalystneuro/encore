# crcns-apl-1 · verifier-1 · run 42490762168

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *.y*ml *.json 2>/dev/null | head -300
```

```
total 348
drwxr-xr-x 6 runner runner    4096 Nov  8 15:03 .
drwxr-xr-x 7 runner runner    4096 Nov  8 15:03 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 14:37 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 14:37 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  8 15:03 .claude
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .env
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .env.development
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .env.local
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .env.production
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .env.test
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .env.test.local
drwx------ 2 runner runner    4096 Nov  8 15:03 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 14:37 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 14:37 .github
-rw-r--r-- 1 runner runner       0 Nov  8 15:03 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 14:37 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 14:37 .mcp.json
[... 323 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 300,800p 10.7554-elife.27342.yaml
```

```
Are_sequential_attractors_the_same.m); data, the correlation of S(A) with S(B); control, the
    correlation of S(A) with the null model E_ij = s_i s_j / T (Methods). Open details, all run,
    the correlation is Spearman (the code that is plotted) or Pearson; the control for a pair is
    that of its first program, or the larger of its two programs' controls. Reproduced when, under
    a reading, at least 26 of the 30 pairs (28 less its tolerance of 2.8) have a data correlation
    above their control.
- id: fig3h-perturbations-return
  statement: Of 19 spontaneous divergences from the trajectory, 17 (90%) returned to a recurrent
    state; the two that did not were consistent with the end of the evoked locomotion.
  source: Results, Joint population activity meets the conditions for a periodic attractor,
    paragraph 7; Materials and methods, Testing return to the same manifold after perturbation;
    Figure 3H
  quote: For the remaining 19 divergent periods, we then determined if the population activity
    returned to a recurrent state after the divergent point; that is, whether the density of
    recurrence returned above 90% or not. The majority (17/19) did
  expected:
  - quantity: divergent periods
    value: 19
    tolerance: 1.9
  - quantity: divergent periods that returned to above 90% recurrence
[... 342 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_bruno_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--');print(''.join(o['data']['text/plain'])[:6000])
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
2129 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Header placeholder
3	==================== 1 code
4	import os
5	os.environ.setdefault("OMP_NUM_THREADS", "1")
6	os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
7	import time
8	import resource
9	import warnings
10	
11	import numpy as np
12	import pandas as pd
13	import matplotlib.pyplot as plt
14	import statsmodels.api as sm
15	from scipy import stats
16	
17	import apl
18	
19	warnings.filterwarnings("ignore", category=RuntimeWarning)
20	pd.set_option("display.width", 220)
[... 818 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 839,
 "limit": 700
}
```

```
839	reading's recurrence analysis).
840	==================== 28 code
841	t0 = time.time()
842	MAN = {k: apl.run_manifold(recs, sds[k.split("/")[0]], RUNS[k], n_shuffle=100, seed=1)
843	       for k in ["own/min80", "own/le80", "pooled/min80", "pooled/le80"]}
844	print(f"comparisons in {time.time() - t0:.0f} s")
845	def haus_table(k, axes, ps):
846	    rows = []
847	    for m in MAN[k]:
848	        for (i, j) in apl.PAIRS:
849	            h, c = m[(axes, ps, i, j)]
850	            rows.append({"prep": m["prep"], "pair": f"{i + 1},{j + 1}", "H": h, "ctrl_mean": np.mean(c),
851	                         "ctrl_2sem": 2 * np.std(c, ddof=1) / np.sqrt(c.size), "dims": m["k_prog1" if axes == "prog1" else "k_common"]})
852	    return pd.DataFrame(rows)
853	--OUT--
854	comparisons in 203 s
855	
856	==================== 29 markdown
857	## fig3c-same-manifold
858	
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1538,
 "limit": 600
}
```

```
1538	
1539	==================== 49 markdown
1540	## fig5b-period-changes
1541	
1542	> Over a response the orbital period may slow, speed up or not change; all three occur among the 30
1543	> responses.
1544	==================== 50 code
1545	t0 = time.time()
1546	PC = {}
1547	rows = []
1548	for k in ["own/min80", "pooled/le80", "own/le80", "pooled/min80"]:
1549	    out = []
1550	    for n, o in enumerate(RUNS[k]):
1551	        w = o["windows"][-1]
1552	        hi = np.flatnonzero(w["dens"] > 0.9)
1553	        sl = slice(hi[0], hi[-1] + 1)
1554	        wt = 1 / w["sddelay"]
1555	        wt[~np.isfinite(wt)] = 0
1556	        wt = wt * w["dens"]
1557	        r, p, nw = apl.weighted_spearman(w["mid_t"][sl], w["mdelay"][sl], wt[sl], 10000, np.random.default_rng(500 + n))
[... 573 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "apl.py"
}
```

```
1	"""Loading and measures for CRCNS data set apl-1 (Bruno & Frost 2017).
2	
3	Bruno, Frost & Humphries (2017), "A spiral attractor network drives rhythmic locomotion",
4	eLife 6:e27342, doi:10.7554/elife.27342. The data set (doi:10.6080/K0SN074B) holds the spike
5	times of 30 voltage-sensitive dye recordings (10 preparations, 3 evoked bouts each), the P10
6	nerve spikes of 9 of them, and neuron coordinates on the photodiode array. Files are streamed
7	from the public S3 bucket ``crcnsarchive`` and read in memory; nothing is written to disk.
8	
9	Where the parameters come from. "Methods" is the paper's Materials and methods; "code" is the
10	paper's analysis code, https://github.com/mdhumphries/AplysiaAttractorAnalysis at commit
11	e5f28e986eb3165df1441a49eee4e07c25ee01fe, as cited by the claims file.
12	
13	- Stimulation onset 30 s, offset 32.5 s: Methods (Imaging) and the data description.
14	- Spike-density functions: 10 ms grid, Gaussian kernel to +/-5 SD with unit area (Methods,
15	  Spike-train analysis; code DataSet_Properties.m). The SD is open (claim fig2b-dimensions):
16	  ``sd_mode`` 'sqrt12' (median ISI / sqrt(12)), 'twelve' (median ISI / 12, as the extracted
17	  text prints), 'own' (median ISI of the recording, the code's choice of width) and 'pooled'
18	  (the code's running median over the recordings of the same bout number read so far). The
19	  median ISI uses the ISIs of every neuron after stimulation onset (code).
20	- PCA on the covariance of the post-onset spike-density functions, mean-centred (Methods,
[... 769 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "coalesc" paper/10.7554-elife.27342.txt | head -30; echo ----; grep -n -i -E "caudal|rostral|lateral|orient|medial" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -E "orient|caudal|rostral|lateral|medial|x |y |coordinat|map|ensemble|cluster|type|oscillat|readme" paper/apl-1.data-description.txt | head -40; wc -l paper/apl-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=apl-1/" | head -c 4000; echo;
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=apl-1/" | grep -o "<Key>[^<]*</Key><LastModified>[^<]*</LastModified><ETag>[^<]*</ETag><ChecksumAlgorithm>[^<]*</ChecksumAlgorithm><ChecksumType>[^<]*</ChecksumType><Size>[0-9]*" | sed -E 's/<Key>([^<]*)<.*<Size>/\1 /'; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/filelist.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  for f in live/plot_maps.m orig/0_README.txt; do echo "== $f"; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/$f; echo; done; sed -n 100,157p paper/apl-1.data-description.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  timeout 600 python3 -c "
import numpy as np, apl
from scipy import stats
# kernel area and centring
for sd in (0.243, 0.3, 0.02):
    h=apl.kernel(sd); x=np.arange(h.size); print('kernel',sd,round(h.sum(),6),'centre offset bins',round((h*x).sum()-(h.size-1)/2,3))
# sdf of a single spike at 50 s integrates to 1
s=apl.sdf_matrix([np.array([50.0])],0.3,100); print('sdf area',s.sum()*apl.DT,'peak at',np.argmax(s)*apl.DT)
# n_pcs
ev=np.array([5,3,1,1]); print('min80',apl.n_pcs(ev,0.8,'min80'),'le80',apl.n_pcs(ev,0.8,'le80'))
# recurrence on a 12 s periodic orbit in 3 PCs, built as fake Program
class F(apl.Program):
    def __init__(s,X,t):
        s.pcs=X; s.stimbins=t; s.d=X.shape[1]
t=np.arange(30,123,0.01); ph=2*np.pi*(t-30)/12
rng=np.random.default_rng(0)
X=np.column_stack([np.cos(ph),np.sin(ph),0.3*np.cos(2*ph)])+0.02*rng.standard_normal((t.size,3))
P=F(X,t); P.recurrence(); dom,pk=P.dominant(); print('peaks',[(p['lo'],p['hi'],p['n'],round(p['mean'],2)) for p in pk])
w=P.windows(); print('dens first',w['dens'][:3],'mid',w['mid_t'][:2])
ids=dom['ids'][:200]; e,n=P.local_linear(ids); st=apl.emax_stats(e,n); print('a',st['a'],'b',st['b'],'period',2*np.pi/st['b']*0.01,'npts min',n.min())
# weighted spearman: null
x=np.arange(50.); y=rng.standard_normal(50); print('wsp null',apl.weighted_spearman(x,y,np.ones(50),2000,rng)[:2], 'vs scipy', stats.spearmanr(x,y))
y2=x+rng.standard_normal(50)*5; print('wsp trend',apl.weighted_spearman(x,y2,np.ones(50),2000,rng)[:2])
# iterate_outliers
d=np.concatenate([rng.normal(0,0.05,300),rng.normal(0.5,0.05,20)]); print('iterout',apl.iterate_outliers(d))
print('hellinger same',apl.hellinger(np.array([.1,.2,.9]),np.array([.1,.2,.9])),'disjoint',apl.hellinger(np.zeros(5),np.ones(5)))
# p10 locking: neuron spikes followed 10ms later by p10
nt=np.sort(rng.uniform(34,120,200)); print('lock',apl.p10_locking(nt,np.sort(nt+0.010)))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, apl
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* /usr/local/bin/python* 2>/dev/null; which -a python python3; for p in $(which -a python3 python); do $p -c "import numpy,scipy,fsspec;print('$p ok')" 2>&1 | tail -1; done; ls ~/.venv* ~/venv 2>/dev/null | head
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v && ./v/bin/pip -q install numpy scipy fsspec 2>&1 | tail -2; ./v/bin/python -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
2.5.4 1.18.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  timeout 900 $TMPDIR/v/bin/python -c "
import numpy as np, apl
from scipy import stats
for sd in (0.243, 0.3, 0.02):
    h=apl.kernel(sd); x=np.arange(h.size); print('kernel',sd,round(h.sum(),6),'centre offset bins',round((h*x).sum()-(h.size-1)/2,3))
s=apl.sdf_matrix([np.array([50.0])],0.3,100); print('sdf area',s.sum()*apl.DT,'peak at',np.argmax(s)*apl.DT)
s=apl.sdf_matrix([np.array([50.0])],0.2437,100); print('sdf sd .2437 peak at',np.argmax(s)*apl.DT, 'mean t', (s[:,0]*np.arange(s.shape[0])*apl.DT).sum()/s.sum())
ev=np.array([5,3,1,1]); print('min80',apl.n_pcs(ev,0.8,'min80'),'le80',apl.n_pcs(ev,0.8,'le80'))
class F(apl.Program):
    def __init__(s,X,t):
        s.pcs=X; s.stimbins=t; s.d=X.shape[1]
t=np.arange(30,123,0.01); ph=2*np.pi*(t-30)/12
rng=np.random.default_rng(0)
X=np.column_stack([np.cos(ph),np.sin(ph),0.3*np.cos(2*ph)])+0.02*rng.standard_normal((t.size,3))
P=F(X,t); P.recurrence(); dom,pk=P.dominant(); print('peaks',[(p['lo'],p['hi'],p['n'],round(p['mean'],2)) for p in pk])
w=P.windows(); print('dens first',w['dens'][:3],'mid',w['mid_t'][:2])
ids=dom['ids'][::20]; e,n=P.local_linear(ids); st=apl.emax_stats(e,n); print('a',st['a'],'b',st['b'],'period',2*np.pi/st['b']*0.01,'npts min',n.min(), 'median', np.median(n))
x=np.arange(50.); y=rng.standard_normal(50); print('wsp null',apl.weighted_spearman(x,y,np.ones(50),2000,rng)[:2], 'vs scipy', stats.spearmanr(x,y))
y2=x+rng.standard_normal(50)*5; print('wsp trend',apl.weighted_spearman(x,y2,np.ones(50),2000,rng)[:2])
d=np.concatenate([rng.normal(0,0.05,300),rng.normal(0.5,0.05,20)]); print('iterout',apl.iterate_outliers(d))
print('hellinger same',apl.hellinger(np.array([.1,.2,.9]),np.array([.1,.2,.9])),'disjoint',apl.hellinger(np.zeros(5),np.ones(5)))
nt=np.sort(rng.uniform(34,120,200)); print('lock',apl.p10_locking(nt,np.sort(nt+0.010)))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 17, in <module>
    ids=dom['ids'][::20]; e,n=P.local_linear(ids); st=apl.emax_stats(e,n); print('a',st['a'],'b',st['b'],'period',2*np.pi/st['b']*0.01,'npts min',n.min(), 'median', np.median(n))
                                                                                                                  ~~~~~~~^~~~~~~~
ZeroDivisionError: float division by zero
kernel 0.243 1.0 centre offset bins 0.0
kernel 0.3 1.0 centre offset bins -0.0
kernel 0.02 1.0 centre offset bins 0.0
sdf area 1.0 peak at 50.0
sdf sd .2437 peak at 50.01 mean t 50.0084999495205
min80 2 le80 2
peaks [(11.0, 12.0, 975, 11.37)]
dens first [1. 1. 1.] mid [37.5 38.5]
```

**Agent calls Bash**

```bash
cd  timeout 900 $TMPDIR/v/bin/python -c "
import numpy as np, apl
from scipy import stats
class F(apl.Program):
    def __init__(s,X,t):
        s.pcs=X; s.stimbins=t; s.d=X.shape[1]
t=np.arange(30,123,0.01); 
rng=np.random.default_rng(0)
ph=2*np.pi*(t-30)/12
r=1*np.exp(-(t-30)/200)
X=np.column_stack([r*np.cos(ph),r*np.sin(ph),0.3*np.cos(2*ph)+0.05*np.sin(2*np.pi*t/37)])
P=F(X,t); P.recurrence(); dom,pk=P.dominant(); print('theta',P.theta,'peaks',[(p['lo'],p['hi'],p['n'],round(p['mean'],2)) for p in pk], 'recurrent frac', np.mean(~np.isnan(P.delay[:,-1])))
ids=dom['ids'][::25]; e,n=P.local_linear(ids); st=apl.emax_stats(e,n); print('a',st['a'],'b',st['b'],'period',2*np.pi/st['b']*0.01,'npts min',n.min(), 'median', np.median(n), 'n_used',st['n_used'],len(n))
print('eig dims', apl.eig_dimensions(st['eigs']))
x=np.arange(50.); y=rng.standard_normal(50); print('wsp null',apl.weighted_spearman(x,y,np.ones(50),2000,rng)[:2], 'vs scipy', stats.spearmanr(x,y))
y2=x+rng.standard_normal(50)*5; print('wsp trend',apl.weighted_spearman(x,y2,np.ones(50),2000,rng)[:2])
d=np.concatenate([rng.normal(0,0.05,300),rng.normal(0.5,0.05,20)]); print('iterout',apl.iterate_outliers(d))
print('hellinger same',apl.hellinger(np.array([.1,.2,.9]),np.array([.1,.2,.9])),'disjoint',apl.hellinger(np.zeros(5),np.ones(5)))
nt=np.sort(rng.uniform(34,120,200)); print('lock',apl.p10_locking(nt,np.sort(nt+0.010)), 'unrelated', apl.p10_locking(nt, np.sort(rng.uniform(30,123,2000))))
"
```

```
theta [0.13211414 0.21148054 0.32447433] peaks [(11.0, 12.0, 7691, 11.31)] recurrent frac 0.9861520707783049
a 2.2343605870861032e-05 b 0.0026518490850801716 period 23.69360059940828 npts min 303 median 363.0 n_used 308 308
eig dims {'mean_unique': array([ 2.23436059e-05, -4.57401052e-05]), 'p_complex1': 0.5064935064935064, 'p_complex12': 1.0}
wsp null (0.3445378151260504, 0.01649175412293853) vs scipy SignificanceResult(statistic=np.float64(0.34453781512605036), pvalue=np.float64(0.01427911456311786))
wsp trend (0.9417046818727491, 0.0004997501249375312)
iterout (-0.00526634311629924, 0.0405252197089534, 39)
hellinger same 0.0 disjoint 1.0
lock (1.0, 200) unrelated (0.14, 200)
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" 10.7554-elife.27342.yaml; grep "^- id:" 10.7554-elife.27342.yaml | tr '\n' ' '
```

```
30
- id: dataset-size - id: fig1d-slow-oscillation - id: fig1e-decaying-rate - id: fig2b-dimensions - id: fig2ef-periodic-recurrence - id: fig2e-single-dominant-orbit - id: fig2s2-threshold-robust - id: fig3a-coalescence - id: fig3c-same-manifold - id: fig3s1a-common-axes - id: fig3d-initial-conditions - id: fig3f-pairwise-similarity - id: fig3h-perturbations-return - id: fig3i-same-manifold-after - id: fig4bc-stable-spiral - id: fig4c-orbital-period - id: fig4s1a-contracting-dimensions - id: fig4s1b-rotation-dominant - id: fig5b-period-changes - id: fig5c-no-relation-contraction - id: fig6d-decode-p10 - id: fig6s1-no-p10-motorneurons - id: fig6s2-dimensions-p10 - id: fig7a-long-tailed-participation - id: fig7f-strongly-variable-neurons - id: halving-participation - id: fig7s1-rate-synchrony - id: fig7s2-no-invariant-core - id: fig7gh-robust-to-participation - id: fig8-caudolateral
```

**Agent**

# Verifier report, round 1: Bruno, Frost & Humphries 2017 (eLife 27342) on CRCNS apl-1

The claims file has 30 claims. My outcomes: 21 reproduced, 4 partially reproduced, 3 not reproduced, 2 blocked.

## A. Outcomes

| claim | outcome | reason |
|---|---|---|
| dataset-size | partially_reproduced | Cell 10 gives 10 preparations, 30 recordings and 1131 neurons, all exact. Only 12 of 30 recordings hold 108 to 198 neurons; the range is 75 to 160, which matches the data description, not the paper's 120 to 180. |
| fig1d-slow-oscillation | reproduced | Cell 12: the weighted peak of the grand mean spectrum is 0.0486 Hz, and 30 of 30 recordings lie in (0, 0.11] Hz. |
| fig1e-decaying-rate | reproduced | Cell 14: 30 of 30 responses decrease under both reading (a) (R < -0.2) and reading (b) (negative slope). |
| fig2b-dimensions | reproduced | Cell 16, code count (le80) with either the recording's own or the pooled median ISI: 28 of 30 counts in 3.6 to 8.8, and neurons/dimensions above 10 in 30 of 30. It fails under the Methods count (min80: ratio above 10 in only 29 of 30) and under both printed SDs (22 to 76 dimensions). |
| fig2ef-periodic-recurrence | reproduced | Cell 20: in all readings but one, more than 15 and fewer than 30 dominant periods lie in 9 to 16.5 s (adopted reading: 26 of 30, median 12.7 s). The exception is twelve/le80 with the mean period (13 of 30). |
| fig2e-single-dominant-orbit | reproduced | Cell 22: 29 of 30 responses have more than 50% of points in the dominant peak (27 of 30 counting all recurrent points); there are 1 to 4 peaks. |
| fig2s2-threshold-robust | reproduced | Cell 24: reading (a) holds at 5% and at 2% in every reading, Spearman 0.70 to 0.97 with p < 1e-4. |
| fig3a-coalescence | not_reproduced | Cell 26: coalescence comes within one period of onset in only 11 to 14 of 30 responses (27 required), and 16 to 20 of 30 measured from offset. The proportion recurrent after coalescence exceeds 50% in 30 of 30. |
| fig3c-same-manifold | reproduced | Cell 30: 29 of 30 pairs pass with recurrent points and 28 of 30 with the code's points. With the code's points the failing pairs are exactly (4; 1,2) and (4; 1,3), as in the paper. |
| fig3s1a-common-axes | reproduced | Cell 32: 27 to 30 of 30 pairs pass (26 required). |
| fig3d-initial-conditions | reproduced | Cell 34: the transient distance exceeds both other distances in 30 of 30 pairs. Medians: transient about 45, onset about 9.3, coalesced about 14. |
| fig3f-pairwise-similarity | reproduced | Cell 36: 27 to 30 of 30 pairs pass in every variant. Pearson with the larger control fails exactly (7; 1,3) and (7; 2,3), as in the paper. |
| fig3h-perturbations-return | reproduced | Cell 38, own/le80: 18 kept with 16 returned (mean period) and 19 kept with 17 returned (median period), both within tolerance. It fails under the adopted own/min80 reading (16 kept, 15 returned) and under the pooled readings. |
| fig3i-same-manifold-after | reproduced | Cell 40: 13 or 14 under own/le80 with reading (a), and under own/min80 or pooled/le80 with reading (b), all within 14 ± 1.4. The result depends strongly on the reading (range 9 to 17). |
| fig4bc-stable-spiral | partially_reproduced | Cell 42: the grand mean is a stable spiral in every reading, but only 6 to 9 of the 10 preparations have two of three spiral responses (adopted reading: 8; preparations 3 and 4 have 1 each). |
| fig4c-orbital-period | partially_reproduced | Cell 44: the mean linear-model period is 10.45 s (own/min80) and 10.12 s (pooled/min80), within 10 ± 1, but 13.55 s and 12.22 s under le80, the count under which fig2b holds. It is uncorrelated with the recurrence periods (r = -0.06, p = 0.74), so "consistent with" is not supported. |
| fig4s1a-contracting-dimensions | not_reproduced | Cell 46: only 8 to 11 of 30 responses have all dimension means negative (more than 15 required). |
| fig4s1b-rotation-dominant | reproduced | Cell 48: p_complex12 exceeds 0.5 in 30 of 30 responses in every reading (minimum 0.73). |
| fig5b-period-changes | reproduced | Cell 50, adopted reading: 12 slowing, 4 speeding and 14 unchanged; 31 to 73 windows per response, within 27.9 to 79.2. (own/le80 has a minimum of 27 windows, just below the range.) |
| fig5c-no-relation-contraction | reproduced | Cell 52: p ranges from 0.064 to 0.47 across readings, never below 0.05. The adopted reading is borderline (R = -0.34, p = 0.064). |
| fig6d-decode-p10 | not_reproduced | Cell 56: mean R − 2 s.e.m. is above 0 in 8 of 9 responses under all three windowings. Preparation 4, bout 1 has mean forecast R = -0.06. |
| fig6s1-no-p10-motorneurons | reproduced | Cell 54: the largest locking value is 0.522; no neuron reaches 0.9 in any program. |
| fig6s2-dimensions-p10 | reproduced | Cell 58: under le80, all 9 counts lie in 2.7 to 5.5 and the 90% count is at least twice the 80% count. The 90% models are not better: MAE is worse (p = 0.0195, 7 of 9 worse) and R² does not differ (p = 0.25). |
| fig7a-long-tailed-participation | reproduced | Cell 62: skewness is positive in 30 of 30 responses, and the fraction of neurons above 0.5 is at most 0.40. |
| fig7f-strongly-variable-neurons | reproduced | Cell 64: all 10 preparations have at least 4 strongly variable neurons, under both readings and both pools. |
| halving-participation | reproduced | Cell 66: 6 preparations under reading (a) (top neuron) and 9 under reading (b) (top 10%), against more than one required. |
| fig7s1-rate-synchrony | reproduced | Cell 68, main reading (rate from offset, matched pairs): mean R² 0.491 against 0.5 ± 0.05, and 0.239 against 0.23 ± 0.023. |
| fig7gh-robust-to-participation | partially_reproduced | Cell 70, adopted own/min80: one slope is significant with recurrent points (total change, p = 0.031) and one with the code's points (Hellinger, p = 0.028). Under pooled/le80 neither slope is significant. |
| fig7s2-no-invariant-core | blocked (other) | Cell 71 is a placeholder; nothing was computed. The data are not missing (see B.8). |
| fig8-caudolateral | blocked (metadata_insufficient) | I confirmed this in the archive (see B.9). Cell 73's quadrant counts decide nothing without the array's orientation. |

## B. Problems

1. **[affects a conclusion] The adopted reading fails fig2b (cells 17 and 18, `ADOPT = "own/min80"`).** Under the Methods count, fig2b fails (ratio above 10 in only 29 of 30). Every single-reading downstream analysis uses this reading: decoding, participation, fig7gh and fig8. Several outcomes reverse between min80 and le80: fig3h (fails / passes), fig4c (passes / fails) and fig7gh (fails / passes). No single reading makes the whole chain hold, and the notebook does not say so.
2. **[affects a conclusion] fig7gh was run under only 2 of the 4 readings (cell 70).** own/le80 and pooled/min80 are missing, and the outcome flips between the two readings that were run.
3. **[affects a conclusion] fig6d was decoded only under own/min80 (cell 56, `decode_program` hard-codes `"min80"`).** The le80 and pooled readings that the criterion carries over from fig2b were not run. So it is unknown whether preparation 4, bout 1 fails under every reading.
4. **[affects a conclusion] fig3h and fig3i are reading-shopped.** Eight readings (plus code-rule variants) were run. The target counts are met in only a few of them, and not under the adopted reading. The criterion allows "under a reading", but this success is weak evidence.
5. **[does not affect a conclusion] Asymmetric history search in fig6s2 (cell 56).** The 90% models search only 50, 100, 150 and 200 ms; the 80% models search 50 to 200 ms in 10 ms steps. This favours the 80% models, the direction of the claim. A like-for-like comparison was available from `by_history` but was not shown. The 90% MAE was worse by a median of 1.56, so this is unlikely to reverse the result.
6. **[does not affect a conclusion] fig6s2 mixes readings.** The counts pass only under le80, but the forecasts compare min80 against min90 dimensions.
7. **[does not affect a conclusion] Strict inequality where the paper says "at least" (`summarise`, `divergences`).** Coalescence and divergence use `dens > 0.9` where the paper says "at least 90%". With a 500-point denominator the effect is negligible.
8. **[affects a conclusion] fig7s2 is labelled blocked although it is testable.** The archive holds all 30 spike-time sets, which is everything the ensemble typing needs. The paper links the code toolbox (consensus clustering and spike-train typing), and the claims file names those scripts. A partial test is also possible with no typing: the top 10% by maximum participation and their median maximum change, from `PART`.
9. **[does not affect a conclusion] fig8 is correctly blocked.** I listed the archive (S3 prefix `apl-1/`): the `live/` files above plus `plot_maps.m`, `plot_rasters.m`, `load_raw_data.m`, the docs, `rawdata.tar.gz` and `orig/`. `plot_maps.m` plots `floor(x*10)`, `floor(y*10)` on the diode template with `YDir` normal and no anatomical labels. The description only names left and right preparations. Nothing gives which way is caudal or lateral. One part is testable without orientation: whether the top-fifth neurons concentrate in a single quadrant (left: 15 of 21 in x−y−). Separately, the range test is nearly empty as run: pooling the equal-width fifths over 8 preparations leaves 1 to 2 neurons in the top fifth.
10. **[does not affect a conclusion] fig1d may be measuring the rate decay, not an oscillation (cell 12).** The grand mean spectrum's maximum is at the lowest non-zero bin (0.0076 Hz). The criterion passes, but there is no pre-stimulus or detrended comparison to tell the two apart.
11. **[does not affect a conclusion] Helper checks on synthetic inputs.**
    - These behaved correctly: kernel unit area and centring, SDF area, `n_pcs`, recurrence on a smooth 12 s orbit (peak at 11.3 s; the code's first-entry rule biases it low), `weighted_spearman` (matches scipy with unit weights), `hellinger`, `p10_locking`, and `iterate_outliers`. `iterate_outliers` also trims some core points, but that is the code's rule.
    - On a toy orbit, the mean-imaginary-part period came out about 2× the true period, because real maximum eigenvalues contribute b = 0. This is inherent to the criterion's method. In the real data p_complex1 is high, so the effect is smaller.

## C. What I could not check

- **The ≥100-neighbour filter.** It never removed a point (`n_used == n_all` in all 30, cell 42). A histogram of `npts` per response would show whether the filter is meaningful.
- **Why coalescence is late (fig3a).** The recurrence-density time course of a few responses, and the density in the first windows, would show whether late coalescence is real. Windows can only start at 35 s, so the earliest possible value is 7.5 s after onset.
- **Whether the fig6d failure is robust.** Decoding under own/le80 and pooled/le80, plus a plot of P10 against the forecast for preparation 4, bout 1, would settle it.
- **fig7gh's remaining readings.** The regressions under own/le80 and pooled/min80 were not run.
- **The fig6s2 comparison on equal history grids.** The 80% models restricted to 50, 100, 150 and 200 ms.
- **fig7s2.** There are no outputs at all.

## End of run

19 turns, 6 minutes, $2.07 at API prices, result: success.
