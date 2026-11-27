# cambrainha-2025 · verifier-1 · run 45974929589

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 440
drwxr-xr-x 6 runner runner    4096 Nov 27 10:16 .
drwxr-xr-x 8 runner runner    4096 Nov 27 10:16 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 27 09:33 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 27 09:33 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 27 10:16 .claude
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .env
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .env.development
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .env.local
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .env.production
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .env.test
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .env.test.local
drwx------ 2 runner runner    4096 Nov 27 10:16 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 27 09:33 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 27 09:33 .github
-rw-r--r-- 1 runner runner       0 Nov 27 10:16 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 27 09:33 .idea
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "cambrainha-2025.yaml"
}
```

```
1	# Claims for Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), PRX Life,
2	# doi:10.1103/w49n-2vz8, "Criticality at Work: Scaling in the Mouse Cortex Enhances
3	# Performance", on dandiset 000713 (Allen Institute, Visual Behavior, Neuropixels).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.
6	#
7	# Text read. arXiv preprint 2410.23508 version 2 (15 Sep 2025), standing in for the PRX Life
8	# version of record, in paper/10.1103-w49n-2vz8.txt: main text, Appendix (Methods and
9	# Materials, sections 1 to 6), and the Supplemental Material (sections I to VIII and Figures
10	# S1 to S8). The PDF was opened to read Figures 3, 4, S1, S5, S7 and S8, whose axes the text
11	# garbles. Values read from figures are marked as such.
12	#
13	# Code read. None. The paper links no analysis code and no repository (the contributions
14	# statement says D.M.C. provided initial code and G.G.C. refined it, without a location).
15	#
16	# Data the paper used (Appendix 1, Figure 1A). The Allen Visual Behavior Neuropixels dataset
17	# (ref. 60, DANDI), which the dandiset's title names. Mice trained to lick on an image change.
18	# Each recording about 2 h 25 min, in three phases. Active: about 60 min of natural images in
19	# 250-ms flashes, a change-detection task with reward, lick port present. Non-natural images
20	# (NNI): Gabor patches for 15 min, full-field black and white flashes, and a gray screen for
[... 482 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "criticality.py"
}
```

```
1	"""Loading and measures for Cambrainha et al. (2025) on dandiset 000713.
2	
3	Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), "Criticality at Work: Scaling in
4	the Mouse Cortex Enhances Performance", PRX Life, doi:10.1103/w49n-2vz8. Claims in
5	claims/cambrainha-2025.yaml; the codes M1 to M8 and O1 to O11 below refer to the method notes
6	at the top of that file.
7	
8	Dandiset 000713 (Allen Institute, Visual Behavior Neuropixels) holds one NWB file per session
9	(153 sessions, 81 mice) with the sorted units of all probes (`units`, with the peak channel of
10	each unit and the channel's brain structure in `electrodes/location`), the stimulus
11	presentations by block (`intervals/*_presentations`, column `stimulus_block`) and the task
12	trials (`intervals/trials`). LFP is in separate probe files, which are not read. Files are
13	streamed from the archive at the pinned version with remfile and h5py (pynwb is slow to open
14	these files over the network and adds nothing here); nothing is written to disk. Only the
15	spike times of V1 (VISp) units are read.
16	
17	Where the parameters come from:
18	
19	- `BIN_S` 50 ms, `WIN_S` 30 s, `CV_MAX` 5 (M1, Appendix 1); `NCUT_DIV` 16, the kurtosis at
20	  Ncutoff = N/16 (M3, Appendix 3); `KAPPA = <psi^4>/<psi^2>^2` (Appendix 3).
[... 684 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    print(f'=== [{i}] {c[\"cell_type\"]}')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--out--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--data--'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        if o.get('output_type')=='error': print('ERROR', o.get('ename'), o.get('evalue'))
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
2128 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	53
2	=== [0] markdown
3	# Reproducing Cambrainha et al. (2025) from dandiset 000713
4	
5	Paper. Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), "Criticality at Work: Scaling in the Mouse Cortex Enhances Performance", PRX Life, doi:10.1103/w49n-2vz8. The claims file (`claims/cambrainha-2025.yaml`) was written from the arXiv preprint 2410.23508 version 2 (15 Sep 2025), with its Appendix and Supplemental Material; codes M1 to M8 and O1 to O11 below refer to the method notes at its top.
6	
7	Dataset. DANDI:000713 (Allen Institute, Visual Behavior Neuropixels), version 0.240702.1725 (doi:10.48324/dandi.000713/0.240702.1725). The paper cites the Allen dataset (its ref. 60) without a DANDI version; this is the only published version of the dandiset, and its draft has not changed since (both modified 2024-07-02), so it is pinned as the most recent published version. The files are streamed from the archive; nothing is downloaded.
8	
9	What is read. Per session file: the units table (peak channel, quality metrics, spike times of V1 units only), the electrodes table (structure of each channel), the stimulus presentation tables (stimulus blocks, image onsets and omitted flashes) and the trials table. The probe LFP files are not read.
10	
11	| claim | tested or blocked |
12	|---|---|
13	| sessions-selected | tested |
14	| fig3a-kurtosis-broader-than-surrogate | tested |
15	| fig3c-scaling-hit-rate-higher | analysed; blocked (methods_underspecified) after the analysis |
16	| fig3c-hit-rate-rises-with-threshold | analysed; blocked (methods_underspecified) after the analysis |
17	| fig3d-relative-gain-24 | tested |
18	| figs1-other-window-lengths | tested |
19	| figs2-strict-units | tested |
20	| fig4a-active-most-scaling | analysed; blocked (methods_underspecified) after the analysis |
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 700
}
```

```
700	        2000  a  b          46.341            0        NaN              no grid
701	        2000  b  a           8.808           74      0.716       not_reproduced
702	        2000  b  b           8.808           74      0.716       not_reproduced
703	        2000  c  a          19.931            0        NaN              no grid
704	        2000  c  b          22.321            0        NaN              no grid
705	        3000  a  a          24.447            0        NaN              no grid
706	        3000  a  b          52.572            0        NaN              no grid
707	        3000  b  a          13.371            0        NaN              no grid
708	        3000  b  b          13.371            0        NaN              no grid
709	        3000  c  a          15.730            0        NaN              no grid
710	        3000  c  b          20.738            0        NaN              no grid
711	        4000  a  a          35.462            0        NaN              no grid
712	        4000  a  b          45.790            0        NaN              no grid
713	        4000  b  a           8.600           79      0.684       not_reproduced
714	        4000  b  b           9.545           60      0.900 partially_reproduced
715	        4000  c  a          35.462            0        NaN              no grid
716	        4000  c  b          35.462            0        NaN              no grid
717	
718	best verdict over readings, per seed: {0: 'reproduced', 1000: 'partially_reproduced', 2000: 'not_reproduced', 3000: 'not_reproduced', 4000: 'partially_reproduced'}
719	
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1400,
 "limit": 730
}
```

```
File content (25043 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1400,
 "limit": 380
}
```

```
1400	      round(h2.kappa_a.median(), 3), ", passive", round(d[d.phase == "passive"].kappa_a.median(), 3),
1401	      ", NNI (a)", round(d[d.phase == "nni_a"].kappa_a.median(), 3), ", NNI (b)",
1402	      round(d[d.phase == "nni_b"].kappa_a.median(), 3))
1403	print("Mann-Whitney first against second half: p =", f"{stats.mannwhitneyu(h1.kappa_a, h2.kappa_a).pvalue:.2e}")
1404	--out--
1405	cv    O4 O6  kappa_surr_max  points        verdict  first_ge_second  second_gt_passive  passive_gt_nni
1406	 a nni_a  a          34.292       0        no grid              NaN                NaN             NaN
1407	 a nni_a  b          48.341       0        no grid              NaN                NaN             NaN
1408	 a nni_b  a          34.292       0        no grid              NaN                NaN             NaN
1409	 a nni_b  b          48.341       0        no grid              NaN                NaN             NaN
1410	 b nni_a  a           8.532     130 not_reproduced            0.623                1.0             0.0
1411	 b nni_a  b          10.302      94 not_reproduced            0.681                1.0             0.0
1412	 b nni_b  a           8.532     130 not_reproduced            0.623                1.0             0.0
1413	 b nni_b  b           8.806     124 not_reproduced            0.605                1.0             0.0
1414	 c nni_a  a          34.292       0        no grid              NaN                NaN             NaN
1415	 c nni_a  b          34.292       0        no grid              NaN                NaN             NaN
1416	 c nni_b  a          34.292       0        no grid              NaN                NaN             NaN
1417	 c nni_b  b          34.292       0        no grid              NaN                NaN             NaN
1418	
1419	median kurtosis (cv a): first half 6.389 , second half 6.026 , passive 5.534 , NNI (a) 6.994 , NNI (b) 7.216
[... 360 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1780,
 "limit": 350
}
```

```
1780	 b baa   b        64            2       1.453      0.775    1.473   0.114     0.049    0.046  0.032 0.030       2
1781	 b bab   a        64           38       1.451      0.775    1.427   0.113     0.048    0.046  0.099 0.029       2
1782	 b bab   b        64            4       1.453      0.775    1.434   0.114     0.049    0.046  0.099 0.030       2
1783	 b bba   a        64           20       1.451      0.793    1.434   0.113     0.048    0.052  0.107 0.029       2
1784	 b bba   b        64            2       1.453      0.794    1.473   0.114     0.049    0.052  0.032 0.030       2
1785	 b bbb   a        64           38       1.451      0.793    1.427   0.113     0.048    0.052  0.099 0.029       2
1786	 b bbb   b        64            4       1.453      0.794    1.434   0.114     0.049    0.052  0.099 0.030       2
1787	 c aaa   a        97           44       1.482      0.760    1.561   0.157     0.053    0.055  0.174 0.043       1
1788	 c aaa   b        97            1       1.489      0.755    1.532   0.161     0.053    0.054    NaN 0.042       1
1789	 c aab   a        97           86       1.482      0.760    1.557   0.157     0.053    0.055  0.183 0.043       1
1790	 c aab   b        97            2       1.489      0.755    1.449   0.161     0.053    0.054  0.176 0.042       1
1791	 c aba   a        97           44       1.482      0.740    1.561   0.157     0.053    0.057  0.174 0.043       1
1792	 c aba   b        97            1       1.489      0.769    1.532   0.161     0.053    0.065    NaN 0.042       1
1793	 c abb   a        97           86       1.482      0.740    1.557   0.157     0.053    0.057  0.183 0.043       1
1794	 c abb   b        97            2       1.489      0.769    1.449   0.161     0.053    0.065  0.176 0.042       1
1795	 c baa   a        97           44       1.442      0.769    1.561   0.099     0.046    0.040  0.174 0.022       2
1796	 c baa   b        97            1       1.446      0.767    1.532   0.100     0.046    0.03
[... 333 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i in [44,46,48]:
    c=nb['cells'][i]
    for o in c.get('outputs',[]):
        if 'text' in o:
            t=''.join(o['text']); print('=== ',i); print(t[5500:] if len(t)>6000 else '')
"
```

```
===  44
    2       1.446      0.795    1.449   0.100     0.046    0.045  0.176 0.021       2

largest number of means within tolerance under a reading: 2 ; readings with 3 or more: 0 of 48
per exponent, readings within tolerance: {'alpha': 24, 'beta': 46, 'mu': 0, 'z': 0}

main reading, session values (active):
        alpha    beta      mu       z
count  97.000  97.000  44.000  97.000
mean    1.481   0.760   1.569   0.156
std     0.053   0.056   0.178   0.043
min     1.347   0.570   1.197   0.056
25%     1.449   0.730   1.442   0.125
50%     1.487   0.772   1.551   0.159
75%     1.510   0.799   1.739   0.184
max     1.610   0.854   1.942   0.239

surrogate, main reading: {'alpha': '1.068 +/- 0.007', 'beta': '0.968 +/- 0.008', 'mu': '1.850 +/- 0.202', 'z': '0.037 +/- 0.011'}

===  46
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; grep -n -i -E "surrogat|kurtosis|CV|coefficient of variation|128|62 sessions|Eq. \(2\)|covariance|correlation matrix" 10.1103-w49n-2vz8.txt | head -120
```

```
1012 10.1103-w49n-2vz8.txt
72:Performance increases with kurtosis
77:Appendix). For each window, we calculated the covariance matrix Cij comprising all pairs of recorded neurons.
87:covariance eigenvectors. This procedure creates a flow
111:N covariance 
117:N≥128
125:coarse-graining of a unit time series, corresponding to projections onto a decreasing number of eigenvectors of the covariance
129:point. For each window, we used the kurtosis κ of the
132:Certain time windows exhibit clear signatures of nontrivial dynamics, as expected at a critical point, with kurtosis values significantly higher than those in the spikeshuffled (surrogate) data.
134:show results similar to surrogate data [Fig. 2B]. Across
135:62 sessions (from 44 mice), we observed a broad range
136:of kurtosis values, overlapping with the distribution from
137:the surrogate data [Fig. 3A]. As we depart from the Gaussian distribution, the distinction between windows with
139:this arbitrariness by establishing a kurtosis threshold κth:
146:above surrogate values, the average hit rate was consistently higher when calculated over scaling windows
147:than over no-scaling windows [Fig. 3C]. We have verified that higher kurtosis was associated to better performance [Fig. 3C], with relative performance gain reaching
151:were also analyzed and showed similar results, associating higher kurtosis with better performance (see the
157:(the lick port is removed). During this phase, the distribution of kurtoses across windows got closer to surrogate
162:lower levels in the kurtosis distribution was even more
175:Surrogate
[... 69 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-w49n-2vz8.txt",
 "offset": 390,
 "limit": 180
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t.py <<'EOF'
import sys; sys.path.insert(0,'.')
import numpy as np, criticality as cr
rng=np.random.default_rng(0)
# 1 Gaussian iid -> kappa ~3
X=rng.normal(size=(160,600)); print("gauss kappa", cr.momentum_kurtosis(X)[:2])
# 2 independent Poisson, heterogeneous rates (surrogate-like)
r=rng.lognormal(np.log(0.12),1.0,160); r=np.clip(r,0.005,2)
ks=[];kz=[]
for _ in range(200):
    X=rng.poisson(r[:,None]*np.ones((1,600))).astype(float); X=X[X.sum(1)>0]
    ks.append(cr.momentum_kurtosis(X)[0])
    Z=(X-X.mean(1,keepdims=True))/X.std(1,keepdims=True); kz.append(cr.momentum_kurtosis(Z)[0])
print("indep poisson cov-kappa: min %.2f med %.2f max %.2f"%(min(ks),np.median(ks),max(ks)))
print("indep poisson corr-kappa: min %.2f med %.2f max %.2f"%(min(kz),np.median(kz),max(kz)))
# 3 isi_shuffle preserves counts, within window
s=[np.sort(rng.uniform(10,40,50)), np.array([]), np.array([12.0])]
o=cr.isi_shuffle(s,10,40,rng); print("isi counts",[len(x) for x in o], "in window", all(((x>=10)&(x<40)).all() for x in o))
# 4 swap_shuffle preserves totals
h=rng.integers(0,2,300); H=cr.swap_shuffle(h,rng,50); print("swap totals preserved", (H.sum(1)==h.sum()).all(), "mean corr w/ orig", np.mean([np.corrcoef(h,x)[0,1] for x in H]).round(3))
# 5 hit_curves vs brute force
k=rng.uniform(3,15,500); hh=rng.integers(0,3,500); nn=hh+rng.integers(0,3,500); g=np.array([5.,8.,12.])
a,b,na,nb=cr.hit_curves(k,hh,nn,g)
for i,t in enumerate(g):
    m=k>t; assert np.isclose(a[i],hh[m].sum()/nn[m].sum()) and np.isclose(b[i],hh[~m].sum()/nn[~m].sum())
print("hit_curves ok")
# 6 real-space on independent Poisson -> alpha~1, beta~1, z~0
X=rng.poisson(0.2,(160,600)).astype(float)
rs=cr.real_space(X); print("indep RS", {k:round(v,3) if np.isscalar(v) else v for k,v in cr.fit_exponents(rs,160).items()})
# 7 correlated: shared latent
lat=np.repeat(rng.normal(size=60),10)
X=rng.poisson(0.2*np.exp(0.8*lat[None,:]+0.3*rng.normal(size=(160,1))) ).astype(float)
rs=cr.real_space(X); print("latent RS", {k:round(v,3) for k,v in cr.fit_exponents(rs,160).items()})
print("K",rs["K"],"n",rs["n"])
EOF
python3 $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 2, in <module>
    import numpy as np, criticality as cr
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  (pip install --user -q numpy h5py remfile 2>&1 | tail -2) ; python3 -c "import numpy; print(numpy.__version__)"
```

```
ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system: '/home/runner/.local/bin/f2py'

2.5.5
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/stub; touch $TMPDIR/stub/h5py.py $TMPDIR/stub/remfile.py; PYTHONPATH=$TMPDIR/stub python3 $TMPDIR/t.py
```

```
gauss kappa (np.float64(2.9824794034172615), np.float64(2.982479403417262))
indep poisson cov-kappa: min 3.14 med 3.32 max 3.52
indep poisson corr-kappa: min 3.71 med 4.25 max 6.72
isi counts [50, 0, 1] in window True
swap totals preserved True mean corr w/ orig -0.005
hit_curves ok
indep RS {'alpha': np.float64(1.07), 'beta': np.float64(0.95), 'mu': np.float64(0.417), 'mu_r2': np.float64(0.754), 'z': np.float64(0.006)}
latent RS {'alpha': np.float64(1.611), 'beta': np.float64(0.727), 'mu': np.float64(0.727), 'mu_r2': np.float64(0.848), 'z': np.float64(0.59)}
K [  1.   2.   4.   8.  16.  32.  64. 128.] n [160.  80.  40.  20.  10.   5.   2.   1.]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json, urllib.request
base="https://api.dandiarchive.org/api/dandisets/000713/versions/0.240702.1725/"
v=json.load(urllib.request.urlopen(base))
print(v.get("name"), v.get("status"), v.get("asset_count"))
paths=[];url=base+"assets/?page_size=1000"
while url:
    d=json.load(urllib.request.urlopen(url)); paths+= [a["path"] for a in d["results"]]; url=d["next"]
ses=[p for p in paths if p.endswith(".nwb") and "_probe-" not in p and not p.endswith("_image.nwb")]
print(len(paths), "session files", len(ses), "subjects", len(set(p.split("/")[0] for p in ses)))
EOF
```

```
Allen Institute - Visual Behavior - Neuropixels None None
4293 session files 153 subjects 81
Shell cwd was reset to
```

**Agent**

**Verification report, round 1: Cambrainha et al. 2025 on DANDI:000713 (0.240702.1725)**

The claims file has 18 claims. My outcomes: 3 reproduced, 2 partially reproduced, 12 not reproduced, 1 blocked. I disagree with the notebook on four of the five claims it treats as blocked (fig3c-scaling-hit-rate-higher, fig3c-hit-rate-rises-with-threshold, fig4a-active-most-scaling, figs8-halves-and-phase-order).

The main uncertainty is the surrogate chance level. The paper says the lowest surrogate kurtoses are around 6. The notebook gets a minimum of 2.80 and a 5th percentile of 3.16 (cell 17). My synthetic test of the helper gives 3.1–3.5 for independent Poisson units, so the kurtosis step as coded here may not match the paper's.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| sessions-selected | not_reproduced | All V1 units: 97 sessions and 68 mice with > 128 units (98 with ≥ 128). Default quality filters: 1 session (cell 15). The paper has 62 sessions and 44 mice; no reading of the criterion lands within tolerance. I confirmed 153 session files from 81 subjects on the DANDI API. |
| fig3a-kurtosis-broader-than-surrogate | partially_reproduced | The real windows spread more than the surrogates (IQR 1.98 vs 0.64), and some exceed κ_surr_max (real maximum 89.8 vs 34.3). The lowest surrogate kurtoses are 2.80 (minimum) and 3.16 (5th percentile), against 6 ± 0.6. That matches the criterion's partial clause. The "majority above κ_surr_max" condition fails (0.000), cell 17. |
| fig3c-scaling-hit-rate-higher | not_reproduced (notebook: blocked) | Under the adopted CV reading (a), the scaling hit rate is below the no-scaling hit rate at all 236 thresholds from 3 to 15 (e.g. κ=7: 0.615 vs 0.655; κ=12: 0.591 vs 0.642), cell 19. So any κ_surr_max up to 12.5, including the paper's ≈7, fails the test. The grid is empty only because of a few outlier surrogate windows. Only CV reading (b), which drops 83% of windows, passes. |
| fig3c-hit-rate-rises-with-threshold | not_reproduced (notebook: blocked) | Under CV (a) from κ = 3 to 12.5, the Spearman correlation is −0.64 and the hit rate falls from 0.641 to 0.587 (cell 22). From κ = 7 to 12 it is flat at 0.615–0.630, then drops to 0.591 (cell 19). |
| fig3d-relative-gain-24 | not_reproduced | Under CV (a), the largest gain over all thresholds is −1.19%; the gain at κ=12 (−7.9%) is below the gain at κ=8 (−3.0%), cell 24. No reading gives 24 ± 3% together with a rise from 8 to 12. |
| figs1-other-window-lengths | not_reproduced | Neither the 10-s nor the 60-s windows pass under any reading. 60-s gains at κ=12 are −8.1% / −3.6% (CV a); the 10-s onset is 10.55 (cell 26). |
| figs2-strict-units | not_reproduced | Session counts are 68 (good units) and 1 (default filters), against 43 ± 4.3. Under CV (a) on good units, the gain at κ=12 is −15.9% (cell 28). |
| fig4a-active-most-scaling | not_reproduced (notebook: blocked) | The NNI phase has the most high-kurtosis windows, not the fewest: at κ=7 the fractions above are NNI 0.50, active 0.31, passive 0.15. Only 16 of 97 sessions have a higher median kurtosis in active than in NNI (cell 30). Under CV (b), where a grid exists, the order holds at 0% of points. |
| fig4-exponents-active | not_reproduced | At most 2 of 4 means fall within tolerance. μ is 1.43–1.57 (paper 0.73); z is 0.10–0.17 (paper 0.3 ± 0.1), cell 44. |
| fig4-exponents-passive | not_reproduced | 48 of 48 readings fail, with at most 1 mean within tolerance. Passive z is not higher than active (0.152 vs 0.156, p = 0.37), cell 46. |
| fig4-exponents-nni | not_reproduced | 96 of 96 readings fail, with at most 1 mean within tolerance; μ ≈ 1.33 against 0.38 (cell 48). |
| fig4bc-static-exponents-trend | partially_reproduced | Holds the same way under all 144 readings: active α and β differ from trivial (p ≈ 1e-17), and the α and β orderings hold. The z ordering fails (active 0.156 > passive 0.152), cell 50. |
| figs3-exponents-stable-with-threshold | blocked (methods_underspecified) | Here the start of the threshold grid changes the outcome, and no adopted-reading grid from the paper's ≈7 was run. Under CV (b) (8.55–12), α, β and z are stable but μ has fewer than 10 sessions. On the CV (a) variant grid 4–12, NNI z departs by 0.084 against an SD of 0.056 (cell 52). |
| figs4-initial-kurtosis-poor-predictor | reproduced | Spearman 0.18 for the active phase and 0.19 for all phases pooled, both below 0.3 (cell 34). |
| figs5a-firing-rate-order | reproduced | Under CV (a), active < NNI < passive at 141 of 141 points, with ρ ≤ −0.976 in every phase (cell 36). |
| figs5c-hit-rate-firing-rate-nonmonotonic | reproduced | The below-threshold hit rate rises from 0.601 to 0.751, then falls to 0.654, with SEs of 0.037 or less. This holds under every reading and every seed (cell 38). |
| figs7-fatigue-halves | not_reproduced | Under CV (a) the gains are negative in both halves (first half −8.0% / −11.2%, second half −6.8% / −20.3% at κ 8 / 12). Only CV (b) passes, with 4–6 trials above κ=12 (cell 40). |
| figs8-halves-and-phase-order | not_reproduced (notebook: blocked) | The passive > NNI condition fails: median kurtosis is 5.53 for passive and 6.99 for NNI (a) (cell 32). Under CV (b) passive exceeds NNI at 0% of points. |

### B. Problems

1. **[affects a conclusion]** `surr_max`, cells 10–11: blocking on κ_surr_max.
   - The blocking rests on the single largest of 11,639 surrogate values. Only 5 surrogate windows exceed 15 (cell 17), and the maximum swings between 24 and 35 across seeds.
   - Windows with as few as 2 active units are included, where N_cutoff is forced to 1 (cell 7: 14 windows have fewer than 64 units).
   - The notebook never identifies which windows set the maximum.
   - For fig3c (both claims), fig4a and figs8, the outcome is the same for any grid start up to 12.5, so they should be not_reproduced rather than blocked.
2. **[affects a conclusion]** `momentum_kurtosis`: the surrogate chance level (2.8–3.6) does not match the paper's (≈6).
   - On independent Poisson data, the helper gives κ of 3.1–3.5 with covariance input and 3.7–6.7 with z-scored (correlation-matrix) input. That second reading was never run.
   - The notebook does not apply this mismatch consistently: it blocks five claims for it, but treats fig3d, figs1, figs2 and figs7, which use the same kurtosis, as tested.
3. **[affects a conclusion; claims file]** O5, used in cell 10: trial density.
   - The paper (Appendix 5) has "three to five trials" per 30-s window. The go hit/miss reading gives 0–4, median 2.
   - About 682 trials per session over 120 windows would give about 5.7 per window. This suggests the paper counted more trials, for example aborted trials as failures. O5 offers no such reading.
   - Every hit-rate claim depends on this.
4. **[affects a conclusion; claims file]** O9 and `fit_exponents`: the μ fit.
   - Both claims-file readings fit ranks 1 to K, which includes the noise floor of the spectrum. Only 1.7% (reading a) or 4.3% (reading b) of windows reach r² ≥ 0.85 (cell 42).
   - So μ rests on 44, 18 and 7 sessions (active, passive, NNI).
   - If μ fell within tolerance, fig4-exponents-active would become partially reproduced, since α (reading b) and β are already within.
5. **[affects a conclusion]** Selection, cells 7 and 15: every downstream claim runs on 97 sessions and 68 mice, not the paper's 62 and 44. This follows the claims file's main reading, but no reading recovers the paper's set.
6. **[does not affect a conclusion]** `stable_eval`, cell 52: it evaluates every 10th grid point, not every point as the criterion says.
7. **[does not affect a conclusion]** `boot_curves`: it uses 10⁴ Poisson-bootstrap resamples instead of 10⁵ resamples with replacement. This is stated; the SEs only set margins.
8. **[does not affect a conclusion]** Cell 24: reading (b) of the fig3d maximum picks points with 2–21 trials (e.g. 54.9% at κ = 39.5 from 2 trials; ∞ under CV b). None is within tolerance either way.
9. **[does not affect a conclusion]** Cell 50: test (a) compares active and surrogate session values as unpaired, although they come from the same windows. The p-values are tiny either way.

Checks that passed:
- Every number derives from the loaded data.
- On synthetic data the helpers behave correctly: Gaussian κ ≈ 3; the ISI shuffle keeps spike counts and keeps spikes inside the window; the trial swap keeps hit totals; `hit_curves` matches a brute-force count; independent Poisson gives α 1.07, β 0.95, z 0.006.
- The O3 poolings are identical, as cell 13 shows and the algebra requires.
- Rejecting CV reading (b) is reasonable: the paper calls excluded windows rare artefacts, and (b) drops 83% of windows. Reading (c) drops 1.8% and gives the same outcomes as (a).
- There is no train/test structure, so no leakage.
- The archive holds every variable the blocked claims need (spike times, stimulus blocks, trials), and the notebook read them. The blocks are about method, not data.

### C. What I could not check, and which output would settle it

- **Which surrogate windows set κ_surr_max:** a print of their N, firing rate and session, and κ_surr_max after dropping windows with N < 64 or N < 128. This decides whether the grid is really empty.
- **The blocked claims at the paper's level:** fig3c, fig4a, figs8 and figs3 run under CV (a) with the grid starting at the paper's ≈7 and at the 99th and 99.9th percentiles of the surrogate kurtosis. This would settle figs3 in particular.
- **The surrogate chance level:** momentum-space kurtosis with z-scored input, to see whether the paper's ≈6 is recovered.
- **Trial density:** hit rates with aborted and catch trials counted, plus trials per window under each reading, to compare with "three to five".
- **μ fit range:** μ fitted over the upper ranks only (for example ranks up to K/2), with its r² pass rate.
- **Figures:** I did not render the PDF, so I could not compare the real-window kurtosis distribution or the curves with Figures 3A, 3C, 4A and S8.

## End of run

17 turns, 5 minutes, $1.89 at API prices, result: success.
