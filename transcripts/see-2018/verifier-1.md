# see-2018 · verifier-1 · run 43381851989

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 324
drwxr-xr-x 6 runner runner    4096 Nov 13 07:19 .
drwxr-xr-x 8 runner runner    4096 Nov 13 07:19 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 06:52 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 06:52 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 13 07:19 .claude
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .env
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .env.development
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .env.local
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .env.production
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .env.test
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .env.test.local
drwx------ 2 runner runner    4096 Nov 13 07:19 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 06:52 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 06:52 .github
-rw-r--r-- 1 runner runner       0 Nov 13 07:19 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 06:52 .idea
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat see-2018.yaml
```

```
<persisted-output>
Output too large (48.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/bac84791-8358-4d86-8d49-0d1641b903dd/tool-results/bw0oihjh0.txt

Preview (first 2KB):
# Claims for See, Atencio, Sohal & Schreiner (2018), eLife 7, e35587, on CRCNS ac-3.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
# files; only its description on crcns.org (paper/ac-3.data-description.txt) was read, for what
# the dataset is meant to hold.
#
# Text read: the version of record (PMC6017807, Europe PMC full-text XML, flattened), with its
# figure legends, figure supplement legends and Materials and methods; and Supplementary file 1
# (elife-35587-supp1-v2.xlsx, the table of statistical tests with test, N and exact p for each
# panel), which the text file reproduces at its end. No PDF was supplied; every value used here is
# printed in the text, a legend or Supplementary file 1. Figure axes were not read.
#
# Code read: the paper links one repository, the dichotomized Gaussian (DG) implementation of
# Macke et al., https://github.com/mackelab/CorBinian, read at commit 8ebb12d (2021-07-26; the
# paper cites the 2017 state, which is not pinned). It holds the DG fit (findLatentGaussian01.m)
# and sampler (sampleDichGauss01.m) for binary vectors with given means and covariances. The
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/bac84791-8358-4d86-8d49-0d1641b903dd/tool-results/bw0oihjh0.txt"
}
```

```
1	# Claims for See, Atencio, Sohal & Schreiner (2018), eLife 7, e35587, on CRCNS ac-3.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
3	# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
4	# files; only its description on crcns.org (paper/ac-3.data-description.txt) was read, for what
5	# the dataset is meant to hold.
6	#
7	# Text read: the version of record (PMC6017807, Europe PMC full-text XML, flattened), with its
8	# figure legends, figure supplement legends and Materials and methods; and Supplementary file 1
9	# (elife-35587-supp1-v2.xlsx, the table of statistical tests with test, N and exact p for each
10	# panel), which the text file reproduces at its end. No PDF was supplied; every value used here is
11	# printed in the text, a legend or Supplementary file 1. Figure axes were not read.
12	#
13	# Code read: the paper links one repository, the dichotomized Gaussian (DG) implementation of
14	# Macke et al., https://github.com/mackelab/CorBinian, read at commit 8ebb12d (2021-07-26; the
15	# paper cites the 2017 state, which is not pinned). It holds the DG fit (findLatentGaussian01.m)
16	# and sampler (sampleDichGauss01.m) for binary vectors with given means and covariances. The
17	# paper's own analysis code (MATLAB) is not linked; the PCA/ICA code was supplied privately by
18	# Lopes-dos-Santos (Acknowledgements). The dataset's sample STRF code is the dataset's, not the
19	# paper's, and was not read.
20	#
[... 814 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_see_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            else: print('--OUT-- [',list(d.keys()),']')
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1415 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing See et al. (2018) from CRCNS ac-3
3	
4	**Paper.** See JZ, Atencio CA, Sohal VS, Schreiner CE (2018). Coordinated neuronal ensembles in
5	primary auditory cortical columns. *eLife* 7:e35587,
6	[doi:10.7554/eLife.35587](https://doi.org/10.7554/eLife.35587). The claims file
7	(`claims/see-2018.yaml`) was written from the version of record (PMC6017807) with its figure
8	legends, Materials and methods, and Supplementary file 1.
9	
10	**Data set.** [CRCNS ac-3](https://doi.org/10.6080/K09021X1) (See, Atencio & Schreiner 2018),
11	read from the public bucket `crcnsarchive` under `ac-3/live/`, zip files opened in place.
12	CRCNS data sets are not versioned, so the version is recorded as `unversioned`, the only one
13	published; the paper cites the data set by its DOI and no version. The files read have these MD5
14	sums in the data set's `checksums.md5`: `Data.zip` 3140d6178de9c044932901795a4cc817,
15	`Stimulus.zip` ce43beade196882598cecddff5520d7b (the notebook prints the listing it read).
16	The data descriptor is version 0.6 (March 28, 2018).
17	
18	**What the data set holds.** 16 recordings (`site1` to `site16`), 8 with the DMR (`rn1`) and 8
19	with the RN (`rn16`), 655 units, the 10-min stimuli and their triggers: the 32-channel columnar
20	recordings behind Figures 1 to 7, 10 and 11C to F. It does not hold the 50 repeats of the 5-s
[... 750 more lines not kept]
```

**Agent**

Read the first half of the notebook (cNE detection, Fig. 2, 4, 6J, 7). Continuing with the rest.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 771,
 "limit": 650
}
```

```
771	==================== 39 code
772	cp = pairs[pairs.cne_pair]
773	rows = []
774	for lag in (50, 100):
775	    s_, d_ = cp[f"sharp_{lag}"].dropna(), cp[f"delay_{lag}"].dropna()
776	    rows.append({"lags": lag, "reading": "(a) pooled", "median_sharp": s_.median(), "mean_sharp": s_.mean(),
777	                 "sd_sharp": s_.std(), "mean_abs_delay": d_.mean(), "sd_delay": d_.std(), "pairs": len(s_)})
778	    g = cp.groupby("site")
779	    ms, md, mm = g[f"sharp_{lag}"].mean(), g[f"delay_{lag}"].mean(), g[f"sharp_{lag}"].median()
780	    rows.append({"lags": lag, "reading": "(b) per penetration", "median_sharp": mm.mean(), "mean_sharp": ms.mean(),
781	                 "sd_sharp": ms.std(), "mean_abs_delay": md.mean(), "sd_delay": md.std(), "pairs": len(ms)})
782	print(pd.DataFrame(rows).round(2).to_string(index=False))
783	print("\nfraction of cNE pairs with peak delay 0 or 1 ms (+-50): %.2f" % (cp.delay_50 <= 1).mean())
784	print("non-cNE pairs, +-50 ms: median sharpness %.1f ms, mean %.1f ms" % (
785	    pairs[~pairs.cne_pair].sharp_50.median(), pairs[~pairs.cne_pair].sharp_50.mean()))
786	--OUT--
787	 lags             reading  median_sharp  mean_sharp  sd_sharp  mean_abs_delay  sd_delay  pairs
788	   50          (a) pooled         12.00       12.42      5.59            1.64      4.31   1012
789	   50 (b) per penetration         12.22       12.46      2.13            1.49      1.02     16
790	  100          (a) pooled         33.00       32.06     11.12            2.25      8.14   1012
[... 626 more lines not kept]
```

**Agent**

Notebook read. Now the helper module.

**Agent calls Read**

```json
{
 "file_path": "cne.py"
}
```

```
1	"""Loading and cNE measures for CRCNS ac-3 (See, Atencio & Schreiner), used by See et al. (2018).
2	
3	See JZ, Atencio CA, Sohal VS, Schreiner CE (2018). Coordinated neuronal ensembles in primary
4	auditory cortical columns. eLife 7:e35587, doi:10.7554/eLife.35587.
5	
6	The data set CRCNS ac-3 (doi:10.6080/K09021X1) is not versioned; it is read as `unversioned`
7	from the public bucket crcnsarchive, under ac-3/live/, by opening the zip files in place over
8	range requests. Nothing is written to disk. Data.zip holds one MATLAB file per recording
9	(`site<k>-<stim>.mat`, 16 files): `spk`, one struct per unit (spike times in ms, `position` as
10	[lateral offset, depth below the surface] in um, `probechan`, `meanwaveform`), and `trigger`,
11	the stimulus triggers in samples at 20 kHz. Stimulus.zip holds the stimulus envelopes
12	(`stim_mat`, 64 carriers by 0.5-ms columns, 667 columns per trigger) for rn1 (the DMR) and rn16
13	(the RN, the sum of 16 DMRs).
14	
15	Where the parameters come from:
16	
17	- cNE detection (`detect`) follows the claims file's opening comment, from Materials and
18	  methods, Detection of coordinated neuronal ensembles: 10-ms bins, z-scored rows, eigenvalues
19	  of the correlation matrix above the Marcenko-Pastur bound (1 + sqrt(n/T))^2 (the claims file's
20	  reading, Lopes-dos-Santos et al. 2013), fastICA on the significant PCs, membership at the mean
[... 855 more lines not kept]
```

**Agent**

Notebook and helper read. Next: checking the paper's sharpness definition, testing helpers on synthetic inputs, and querying the archive.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "sharpness|half of the|folded|PWC" 10.7554-elife.35587.txt | head -60
```

```
29:Electrode used, sample recording, STRFs, and PWCs. ( A ) Electrode schematic. ( B ) Sample recording from one electrode channel. ( C ) Sample STRFs obtained after spike sorting. Numbers 1–4 indicate the positions and STRFs of pairs of neurons whose PWCs are plotted in ( D ). ( D ) Example PWCs from two pairs of neurons (1–2 and 3–4). Neurons 3 and 4 exhibit a sharper PWC than neurons 1 and 2 despite having approximately similar STRFs and pairwise distances. Dashed lines represent 99% confidence intervals.
31:## Electrode used, sample recording, STRFs, and PWCs.
33:( A ) Electrode schematic. ( B ) Sample recording from one electrode channel. ( C ) Sample STRFs obtained after spike sorting. Numbers 1–4 indicate the positions and STRFs of pairs of neurons whose PWCs are plotted in ( D ). ( D ) Example PWCs from two pairs of neurons (1–2 and 3–4). Neurons 3 and 4 exhibit a sharper PWC than neurons 1 and 2 despite having approximately similar STRFs and pairwise distances. Dashed lines represent 99% confidence intervals.
35:We first examined response synchrony between simultaneously recorded single units using Pearson’s correlation analysis at 10-ms temporal resolution. Pairs of neurons in the same column with similar STRFs could nonetheless exhibit widely differing pairwise correlation (PWC) functions ( Figure 1D ). For example, the PWC between pairs of neurons with similar receptive fields, recorded from channels of equal intra-pair distances, could differ in peak correlation magnitude, width and delay ( Figure 1C and D ). Pearson’s correlation values (or correlation coefficients), PWC absolute peak delays and sharpness are depicted in Figure 2A for one neuron (#15) with all other recorded neurons in the same penetration. Significant PWCs were evident for most pairs in this penetration but low correlation coefficients and broader correlation widths were dominant. Across all penetrations, PWCs were fairly heterogeneous but sharpness and delay covaried with correlation
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, cne
from scipy import stats
# pwc_measures: peak at +3, triangular
lags=np.arange(-50,51); c=np.maximum(0,10-np.abs(lags-3)).astype(float)
print("pwc tri", cne.pwc_measures(c))
c2=c+5  # baseline
print("pwc tri+baseline", cne.pwc_measures(c2))
# pwc histogram
a=np.array([100.,200.]); b=np.array([103.,199.,300.])
h=cne.pwc(a,b,5); print("pwc", h, len(h))
# bvn
from scipy.stats import multivariate_normal as mvn
for h_,k_,r in [(0.3,-1.2,0.5),(-2,-2.5,0.9),(1,0.5,-0.7)]:
    print(cne.bvn_cdf(h_,k_,r), mvn(cov=[[1,r],[r,1]]).cdf([h_,k_]))
# DG fit
rng=np.random.default_rng(0)
g=np.array([-1.5,-1.8,-2.0]); lam=np.array([[1,.4,.2],[.4,1,.3],[.2,.3,1]])
x=cne.sample_dg(g,lam,400000,rng)
g2,l2=cne.fit_dg(x); print("dg", g2, np.round(l2,3))
# ICA recovery: 30 units, 2 assemblies
T=60000; n=30
s=np.zeros((n,T)); base=rng.poisson(0.2,(n,T)).astype(float)
for mem in ([0,1,2,3],[10,11,12]):
    ev=rng.random(T)<0.01
    for m in mem: base[m]+=ev
d=cne.detect(base.astype(np.float32),1,n_shuffles=20)
print("n",d["n"],[ (m["pos"].tolist(),m["neg"].tolist()) for m in d["members"]["a"]], d["thresholds"]["a"])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls /usr/bin/python3* ; which -a python python3 uv pip 2>/dev/null; ls ~/.venv* /opt 2>/dev/null | head
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
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip
/usr/bin/pip
/bin/pip
/opt:
actionarchivecache
az
containerd
google
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  /opt/hostedtoolcache/Python/3.13.18/x64/bin/python -c "import numpy, scipy, fsspec; print('ok')" 2>&1 || (uv venv $TMPDIR/v -q && uv pip install -q --python $TMPDIR/v/bin/python numpy scipy fsspec 2>&1 | tail -2; $TMPDIR/v/bin/python -c "import numpy,scipy;print('venv ok')")
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy, fsspec; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
venv ok
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, cne
from scipy import stats
lags=np.arange(-50,51); c=np.maximum(0,10-np.abs(lags-3)).astype(float)
print("pwc tri", cne.pwc_measures(c))
print("pwc tri+baseline 1/bin", cne.pwc_measures(c+1))
print("flat", cne.pwc_measures(np.ones(101)+np.eye(101)[50]*5))
a=np.array([100.,200.]); b=np.array([103.,199.,300.])
h=cne.pwc(a,b,5); print("pwc", h, len(h))
from scipy.stats import multivariate_normal as mvn
for h_,k_,r in [(0.3,-1.2,0.5),(-2,-2.5,0.9),(1,0.5,-0.7)]:
    print(cne.bvn_cdf(h_,k_,r), mvn(cov=[[1,r],[r,1]]).cdf([h_,k_]))
rng=np.random.default_rng(0)
g=np.array([-1.5,-1.8,-2.0]); lam=np.array([[1,.4,.2],[.4,1,.3],[.2,.3,1]])
x=cne.sample_dg(g,lam,400000,rng)
g2,l2=cne.fit_dg(x); print("dg", g2, np.round(l2,3))
T=60000; n=30
base=rng.poisson(0.2,(n,T)).astype(float)
for mem in ([0,1,2,3],[10,11,12]):
    ev=rng.random(T)<0.01
    for m in mem: base[m]+=ev
d=cne.detect(base.astype(np.float32),1,n_shuffles=20)
print("n",d["n"],[ (m["pos"].tolist(),m["neg"].tolist()) for m in d["members"]["a"]], d["thresholds"]["a"])
# coincidence ratio
bb=np.array([[1,1,0,1],[1,0,0,1]],bool); print("CR",cne.coincidence_ratio(bb))
# to_stim_ms
site={"trigger":np.array([20000.,26667,33334])}
print(cne.to_stim_ms(site,np.array([999.,1000,1333.35,1500,2000.1,2100])))
# segment_index / sta alignment: spike at 50ms with 5ms bins -> last bin before is idx 9 (45-50)
print(cne.segment_index(np.array([50.0,52.0]),5,100,20))
EOF
```

```
pwc tri (3.0, 3.0)
pwc tri+baseline 1/bin (6.0, 3.0)
flat (24.0, 0.0)
pwc [0 0 0 0 1 0 0 0 1 0 0] 11
0.10364661613573975 0.10364661613573972
0.005332931061066141 0.005332931061066137
0.5359975995753287 0.5359975995753287
dg [-1.49639785 -1.8028295  -1.99200964] [[1.    0.397 0.197]
 [0.397 1.    0.29 ]
 [0.197 0.29  1.   ]]
n 2 [([0, 1, 2, 3], []), ([10, 11, 12], [])] (np.float64(-0.26233324670869873), np.float64(0.28438921663858074))
CR 1.0
[         nan   0.         333.5        500.22498875          nan
          nan]
[]
```

**Agent**

Helpers pass synthetic tests (PWC histogram, sharpness, bivariate normal CDF, DG fit, ICA recovering planted assemblies, CR). Now checking the archive for the blocked claims.

**Agent calls Bash**

```bash
cd  curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live/filelist.txt | head -100; echo; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ac-3/" | head -c 3000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import zipfile, fsspec
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live"
for n in ("Data.zip","Stimulus.zip","Codes.zip"):
    z=zipfile.ZipFile(fsspec.open(f"{B}/{n}",block_size=2**16).open())
    for i in z.infolist(): print(n, i.filename, i.file_size)
EOF
grep -i -E "repeat|spontan|64|H3|frozen|5-s|5 s" paper/ac-3.data-description.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  uv pip install -q --python $TMPDIR/v/bin/python aiohttp requests 2>&1|tail -1; $TMPDIR/v/bin/python - <<'EOF'
import zipfile, fsspec
B="https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live"
for n in ("Data.zip","Stimulus.zip","Codes.zip"):
    z=zipfile.ZipFile(fsspec.open(f"{B}/{n}",block_size=2**16).open())
    for i in z.infolist(): print(n, i.filename, i.file_size)
EOF
grep -n -i -E "repeat|spontan|64|H3|frozen|trial" paper/ac-3.data-description.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked all 31 claims in `see-2018.yaml` against the notebook outputs and the helper module. 14 come out reproduced, 3 partially reproduced, 9 not reproduced and 5 blocked by missing data. The archive listing confirms the blocked claims cannot be tested even in part. The biggest problem is the PWC sharpness measure: it gives a median of about 12 ms where the paper reports about 2 ms, and four claims rest on it.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| fig2bd-pwc-measures-covary | not_reproduced | The best R² is 0.219 for sharpness and 0.234 for delay (±100 ms, log axes; cell 33). The target is 0.45 to 0.55 under every reading. |
| fig2eg-distance-weak | not_reproduced | All 12 R² values are between 0.006 and 0.060 (cell 35), below the 0.09 floor. |
| fig4-example-nine-cnes | reproduced | Site 10 is the only recording with 38 units. It gives 9 cNEs with sizes 2 to 6 under reading (a) and 2 to 5 under (b), the same with 5 other seeds (cell 15). |
| fig4s2-interleaved-halves-stable | reproduced | 192 of 205 ICs match (93.7%) under both readings (cell 43). The range allowed is 86.4 to 105.6. |
| fig4s3-train-test-83pct | not_reproduced | The count of 102 training cNEs matches, but 98.0% (quadratic) and 99.0% (linear) are matched, above the 91.3 bound. The variant null gives 95.1% and 99.0% (cell 45). The match is stronger than the paper's, but outside tolerance. |
| fig5a-mi-peaks-10-15ms | not_reproduced | The MI peaks at 35 ms under event reading (a) and at 2 ms under (b), for both projections and both mean and median (cell 49). |
| fig5b-number-decreases-with-bin | reproduced | Spearman ρ is −1.0. The mean number of cNEs falls from 11.06 at 2 ms to 3.75 at 50 ms, and is lower at 50 ms in all 16 recordings (cell 51). |
| fig5c-size-increases-with-bin | reproduced | ρ is 0.952 (sizes 3.88 to 5.11) under sign reading (a) and 1.0 under (b) (cell 53). |
| fig6c-spike-pwc-narrower-than-strf-pwc | partially_reproduced | The size ratio is lower for cNE pairs under both variants (p 6e-59 and 4e-53). "Spike PWC sharper in more than half of cNE pairs" holds only with minimum subtraction (63.2%) and fails with clipping (6.5%). Both variants are the author's own (cell 41). |
| fig6j-sharpness-cne-pairs | partially_reproduced | cNE pairs are sharper at p < 0.001 in 14 of 16 penetrations at ±50 ms and 12 of 16 at ±100 ms (cell 37). The criterion needs 12 for partial and 16 for full. |
| fig6-member-pwc-sharpness-delay | not_reproduced | Median sharpness is 12.0 ms (target 2 ± 0.2) and mean 12.4 ms (target 3.39 ± 1.21). Only the delay (1.64 ms) is within tolerance. Readings (b) and ±100 ms are worse (cell 39). |
| fig7-totals | reproduced | 16 penetrations, 655 units, 104 cNEs, 6.50 ± 1.97 per penetration (cell 13). |
| fig7a-number-vs-neurons | reproduced | R² is 0.745 with p = 1.7e-5 and a positive slope. The fraction is 16.1%, 14.0% or 15.9% depending on the reading, all within 13.5 to 16.5 (cell 17). |
| fig7b-size-vs-neurons | not_reproduced | Only the significant positive fit holds. R² is 0.807 or 0.729 (target 0.33 ± 0.033). Mean size is 4.34 to 4.74 (allowed 4.9 to 9.9). The fraction is about 11% against 17 (cell 19). |
| fig7-negative-weights | not_reproduced | 24 cNEs have a negative-weight member under reading (a) and 65 under (b), against 9 ± 1 (cell 21). |
| fig7c-membership | not_reproduced | 59.2% of units are in one cNE, 34.4% in none and 6.4% in several, against 68, 9 and 23%. Reading (b) is similar (cell 23). |
| fig7d-pairs-within-200um | reproduced | 88.3 to 88.5% of pairs under every reading, within 73.8 to 90.2 (cell 25). |
| fig7e-no-depth-bias | reproduced | KS p = 0.999 and Mann-Whitney U p = 0.474; the median depth differs by 10 µm (cell 27). |
| fig7f-span-200um | not_reproduced | 80.8% of cNEs (78.8% under sign reading b) span 200 µm or less, against 63 to 77 (cell 29). |
| fig8-spont-evoked-72pct | blocked (data_missing) | The archive has no 64-channel recordings (see the check below the table). |
| fig9c-cne-events-more-mi | blocked (data_missing) | The archive has no 50-repeat 5-s data. |
| fig9s1-cne-mi-above-random-groups | blocked (data_missing) | Same data as fig9c. |
| fig9s2-noise-correlations | blocked (data_missing) | Needs trials, which the archive does not have. |
| fig10b-ptd-higher | reproduced | cNE PTD is higher with p < 0.001 under all four projection and event readings (p from 2.3e-12 to 8.9e-4; cell 57). There are 476 pairs against the paper's 703. |
| fig10c-strf-mi-higher | reproduced (fragile) | It passes only under linear projection with event reading (a): p = 5.4e-4 with cNE MI higher in 55.7% of pairs. The other three readings give p from 0.008 to 0.12 (cell 59). |
| fig10s1-random-group-strfs | reproduced | Signed-rank p is 7.0e-4 for PTD and 3.1e-6 for MI. The KS tests give 3.7e-6 and 3.2e-9, with UI medians of 0.35 and 0.27 (cell 61). There are 103 cNEs, as in the paper. |
| fig11ab-real-vs-surrogate | blocked (data_missing) | The archive has no 15 repeats of the 10-min RN. |
| fig11c-models-number | reproduced | Shuffled (0.23 cNEs) and PR (1.41 or 1.52) are below the real 6.50, and DG (8.00) is above. Bonferroni p is at most 1.5e-4 for all three (cell 65). |
| fig11d-models-size | not_reproduced | Only shuffled-with-zeros is significant (p = 1.4e-7). PR (p ≥ 0.125) and DG (4.30 against 4.34, p = 1) are not. With empty runs left out, shuffled is larger than real (cell 67). |
| fig11ef-coincidence-ratios | partially_reproduced | All three models are below one at Bonferroni p < 1e-35 for pairs and triplets (cell 71). The 'repeat' condition cannot be run, which is the criterion's partial case. |
| fig11s3b-pr-strf-similarity | reproduced | PR on 5-ms bins gives a median of 0.737, within 0.666 to 0.814; PR on 10-ms bins gives 0.645, outside. Shuffled and DG give 0.022 (cell 69). |

Blocked claims, checked against the archive: the S3 listing for `ac-3/live/` holds only `Codes.zip`, `Data.zip` (16 files, `site1-rn1.mat` to `site16-rn16.mat`), `Stimulus.zip` (the rn1 and rn16 matrices and parameter files) and the docs. There are no repeat trials, no 5-s frozen segments and no 64-channel or spontaneous epochs. Each recording runs about 622 s against a 598 to 600 s stimulus, which is far too short to hide 50 × 5.5 s of repeats. No part of fig8, fig9c, fig9s1, fig9s2 or fig11ab can be tested.

**B. Problems**

1. [affects a conclusion] `cne.pwc_measures` and `pair_table`, cells 31 to 41. The sharpness is the half-count width of the raw histogram, flat baseline included, so the analysis window largely sets it. On a synthetic flat histogram over ±50 ms it returns 24 ms. In the data the median goes from 16 ms to 37 ms when the window grows from ±50 to ±100 ms. The cNE-pair median is 12 ms against the paper's ~2 ms, so this is not the paper's measure in effect.
   - This follows the claims file's lag readings, which the file itself already marks as resting on an assumption.
   - It drives the failures of fig2bd and fig6-member and weakens fig6j and fig6c.
   - The notebook never notes the scale mismatch.

2. [affects a conclusion] cell 37, fig6j, a likely misreading in the claims file. The paper's pair counts in Supplementary file 1 total 3087 + 8838 = 11,925. That is close to the number of pairs among cNE members at the paper's 91% membership (about 0.83 × 14,174 ≈ 11,740), not to all 14,174 pairs. The paper's non-cNE pairs are therefore probably restricted to pairs where both units are cNE members. `pair_table` computes a `both_members` column, but the notebook never uses it; it prints the 1012/13162 against 3087/8838 mismatch without following it up.

3. [affects a conclusion] cell 41, fig6c. Making the STRF PWC non-negative, by clipping or by subtracting the minimum, is the author's own choice, and the two variants give opposite answers on the "more than half" test. In addition, `np.correlate(..., "full")` on 50-lag profiles tapers to zero at ±49 ms by construction, so the STRF PWC sharpness (4 ms or 13 ms) reflects that taper and the offset more than the profiles. It is also compared with the window-dominated spike sharpness of item 1.

4. [affects a conclusion] `run_binsizes`, fig5a. Event reading (a) takes the 5000 largest samples of activity interpolated to 1 ms. At bin sizes of 20 to 50 ms these are contiguous samples from only about 100 to 250 distinct bins. The STRF and the MI are then computed on the same events, with no held-out data, so the MI is inflated more at large bins. That would push the peak towards 35 ms. Under reading (b) the MI falls monotonically from 2 ms. Neither reading is a defensible version of "a threshold giving 5000 events", so the not_reproduced outcome may come from the method.

5. [affects a conclusion] cell 59, fig10c. It passes on 1 of 4 readings, at p = 5.4e-4, with no seed check. The same no-held-out MI bias applies. The verdict is reproduced by the letter of the criterion but is not robust.

6. [does not affect a conclusion] cell 45. The primary null excludes both row and column maxima, while the paper says all non-matched correlations. The row-only variant is shown and also falls outside tolerance (95.1%).

7. [does not affect a conclusion] cell 61, `run_random_groups`. It uses 100 random groups, not the paper's 500 (a stated deviation). The PTD p of 7.0e-4 sits close to the 0.001 bound and was not checked with more groups.

8. [does not affect a conclusion] `run_models`. Model membership reuses the real data's thresholds. This is a stated assumption, and reasonable because the thresholds are about 1.5/√n (cell 10).

9. [does not affect a conclusion] cell 27. The members are a subset of all units, so the KS and Mann-Whitney U samples are not independent and both tests lean towards "no difference". The members against non-members variant also finds no difference (p = 0.50 and 0.12).

10. [does not affect a conclusion] `pair_table`. The PWCs use recording-clock spikes over the whole recording, including about 22 s outside the stimulus, while r uses the stimulus window only.

11. [does not affect a conclusion] cell 71. CR medians come from 200 runs, not 1000 (stated), and 28 triplets with a real CR of 0 are dropped.

**C. Not checked, and the output that would settle it**

- **fig6j on the paper's pair set:** Mann-Whitney U per site restricted to `both_members` pairs, with pair counts compared against Supplementary file 1.
- **Sharpness scale:** a version with the baseline subtracted or a narrower window, to see whether ~2 ms can be reached at all.
- **fig5a:** the number of distinct events per cNE at each bin size, and MI with the STRF estimated on held-out events.
- **fig10c and fig10s1:** reruns with several seeds, and fig10s1 with 500 groups.
- **DG fit:** whether the fit reproduces the real 5-ms rates and pairwise covariances (fitted against empirical values), and how much eigenvalue clipping `fit_dg` applies per site.
- **ICA convergence:** iteration counts on the real data (not printed).
- **PR model:** the spikes dropped in `pr_setup` (the `dropped` value is computed but not printed).

I did not re-run the notebook or download the data. The helper tests I ran on synthetic inputs all passed: `pwc`, `pwc_measures`, `bvn_cdf` against scipy, the `fit_dg` round trip, `detect` recovering two planted assemblies exactly, and `coincidence_ratio`.

## End of run

16 turns, 4 minutes, $1.62 at API prices, result: success.
