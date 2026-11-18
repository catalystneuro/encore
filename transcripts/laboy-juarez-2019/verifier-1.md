# laboy-juarez-2019 · verifier-1 · run 43285761385

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; find . -maxdepth 2 -type f | head -50
```

```
total 288
drwxr-xr-x 6 runner runner    4096 Nov 12 19:32 .
drwxr-xr-x 8 runner runner    4096 Nov 12 19:32 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 19:00 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 19:00 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 12 19:32 .claude
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .env
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .env.development
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .env.local
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .env.production
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .env.test
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .env.test.local
drwx------ 2 runner runner    4096 Nov 12 19:32 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 19:00 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 19:00 .github
-rw-r--r-- 1 runner runner       0 Nov 12 19:32 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 19:00 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 19:00 .mcp.json
[... 60 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "laboy-juarez-2019.yaml"
}
```

```
1	# Claims for Laboy-Juarez, Langberg, Ahn & Feldman (2019), "Elementary motion sequence detectors in
2	# whisker somatosensory cortex", Nature Neuroscience 22, 1438-1449, doi:10.1038/s41593-019-0448-6,
3	# tested on CRCNS ssc-9 (primary; doi:10.6080/K0FJ2F13, "Extracellular recordings in mouse barrel
4	# cortex during single- and 2-whisker stimulation", whose description names this paper as the
5	# basis of its three experiments).
6	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
7	# protocol pilot-14 as stated in docs/protocol.md (Reader).
8	#
9	# Text read. paper/10.1038-s41593-019-0448-6.txt, the version of record (PDF supplied by a person,
10	# extracted with PyMuPDF), with the main text, figure legends, Methods, Data and Code availability,
11	# the Nature Research reporting summary, and the supplement (41593_2019_448_MOESM1_ESM.pdf), which
12	# holds the legends of Supplementary Figures 1 to 8. The PDF was not opened: every number used
13	# below is printed in the text or a legend. The Methods' sparseness and supralinearity formulas
14	# are garbled by the extraction; they are read here as the standard lifetime sparseness of Vinje
15	# and Gallant (ref. 28), S = (1 - E(r)^2 / E(r^2)) / (1 - 1/n), and as
16	# z = (mu_CWSW - (mu_CW + mu_SW)) / sqrt(se_CW^2 + se_SW^2), which is what the legible parts say.
17	# The data set's description (paper/ssc-9.data-description.txt) was read only to know what it
18	# holds; no claim comes from it.
19	#
20	# Code. The paper links none; "The Matlab code for performing the statistical and data analyses
[... 901 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "laboy-juarez-2019.yaml",
 "offset": 921
}
```

```
921	    tolerance: 5.6
922	  criterion: The alignment index is the Pearson correlation, over the eight combinations at the
923	    best dt, between linear predictions and residuals (measured minus 0.64 times linear) (Fig. 7f
924	    legend). The legend labels the outbound group "Best dt >= 0" in one panel and "> 0" in the
925	    other; 121 + 56 = 177 of 187; readings are (a) best dt = 0 excluded, (b) included with
926	    outbound, (c) units whose best-combination curve was set constant across dt (no best dt;
927	    Methods, dt smoothing) excluded, with best dt = 0 read as in (a) or (b). Reproduced when, under one reading, both t-tests give p < 0.05 with the inbound
928	    means higher; partially reproduced for one.
929	- id: fig7g-inbound-decoding
930	  statement: Spatial combination decoding was better for inbound-order stimuli than for
931	    outbound-order stimuli.
932	  source: Results, Order selectivity dominates dt tuning, paragraph 2; Figure 7g
933	  quote: spatial combination decoding was better for inbound order stimuli than outbound order
934	    stimuli (Fig. 7g)
935	  depends_on:
936	  - fig3e-identity-decoder
937	  criterion: The identity decoder retrained and tested within each 10 ms dt range of Fig. 7g
938	    ([-50,-41] to [41,50]), 1000 ensembles each. The ensemble size and units are not stated, and
939	    the decoder is "as in Fig. 4", whose decoders are built on CW-tuned or SW-tuned units apart;
940	    readings are (a) N = 187 from the selective units, (b) N = 100 from the selective units, (c)
[... 217 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" laboy-juarez-2019.yaml; grep "^- id:" laboy-juarez-2019.yaml | tr '\n' ' '; echo; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_laboy_juarez_2019.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== [{i}] {c['cell_type']} ===")
    print(src[:300])
EOF
```

```
<persisted-output>
Output too large (34.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4cc4ae2c-9c54-45a9-9362-a2c5fcbd3f61/tool-results/b8gofs5j6.txt

Preview (first 2KB):
50
- id: exp1-units - id: fig1b-somatotopy - id: exp1-cw-tuned-fraction - id: exp1-cw-sw-comparable-firing - id: supp1d-sw-tuning-broader - id: fig1d-best-sequence-exceeds-single - id: fig1e-best-combination-includes-cw - id: fig1f-cwsw-exceeds-swsw - id: fig1g-cwsw-sharper - id: supp2-sw-tuned-sharpest-cwsw - id: exp2-units - id: methods-dt-modulation - id: exp2-combination-selective-prevalence - id: fig2f-shuffle-abolishes-tuning - id: fig2f-most-selective-lower-firing - id: supp4-selectivity-at-high-rates - id: fig2g-best-combination-bias - id: fig3a-sharper-than-linear - id: fig3b-sharper-in-both-groups - id: fig3b-linear-sharper-in-selective - id: supp6-layers - id: fig3e-identity-decoder - id: fig3g-binary-decoder - id: fig4a-sw-tuned-sharper - id: fig4c-sw-tuned-decoding - id: fig5a-global-scaling - id: fig5bc-linearity-index - id: fig5c-pseudo-unit-shuffle - id: fig5c-sublinear-at-all-dt - id: supralinear-best-8-percent - id: fig6b-best-above-worst-below-scaled - id: fig6b-enhancement-not-different - id: fig6b-suppression-greater-selective - id: fig6c-enhancement-strongest-sw - id: fig7a-dt-half-width - id: fig7b-inbound-best-outbound-suboptimal - id: fig7c-pca - id: fig7e-pc1-best-suboptimal - id: fig7f-inbound-sharper - id: fig7g-inbound-decoding - id: supp8-order-decoding - id: exp3-units-cw-tuned - id: fig8c-awake-cw-stronger - id: fig8d-awake-best-sequence - id: exp3-combination-selective - id: fig8h-awake-linearity - id: fig8i-awake-sharper-than-linear - id: fig8j-awake-inbound-stronger - id: fig8k-awake-binary-decoder - id: fig8b-awake-behavior 
120
=== [0] markdown ===
# Reproducing Laboy-Juarez et al. (2019) from CRCNS ssc-9

Paper: Laboy-Juarez KJ, Langberg T, Ahn S, Feldman DE (2019). Elementary motion sequence detectors in whisker somato
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_laboy_juarez_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== [{i}] {c['cell_type']} ===")
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--'); print(''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain']))
                if 'image/png' in d: print('[image]')
            elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; echo $TMPDIR
```

```
1957 /tmp/claude-1001/nb.txt
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== [0] markdown ===
2	# Reproducing Laboy-Juarez et al. (2019) from CRCNS ssc-9
3	
4	Paper: Laboy-Juarez KJ, Langberg T, Ahn S, Feldman DE (2019). Elementary motion sequence detectors in whisker somatosensory cortex. Nature Neuroscience 22, 1438-1449. doi:10.1038/s41593-019-0448-6.
5	
6	Dataset: CRCNS ssc-9, "Extracellular recordings in mouse barrel cortex during single- and 2-whisker stimulation", doi:10.6080/K0FJ2F13, read from the public bucket at `https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip`. CRCNS data sets are not versioned (docs/archives.md), so the version is recorded as `unversioned`, pinned by the MD5 sums of the files read, from the data set's `checksums.md5`: `data.zip` 2e7a774017619e76c46db85722587be3 (the only data file; the docs are `crcns_ssc-9_data_description.pdf` d5d1590c38b8eea45e070e8cdfc4827f, version 0.6 of May 13, 2019). There is one published version, the one the paper's Data availability statement points to (crcns.org), so it is the one used; the next cell checks the sum.
7	
8	Claims file: `claims/laboy-juarez-2019.yaml`, written from the version of record with its supplement. The paper links no code (available on request), so every method below comes from the claims file, the Methods, the legends and the supplement; details taken from the paper cite the passage.
9	
10	Claims tested and blocked (outcomes are in the summary at the end):
11	
12	| Claim | Status |
13	|---|---|
14	| exp1-units to supp2-sw-tuned-sharpest-cwsw (experiment 1, 10 claims) | tested |
15	| exp2-units to supp8-order-decoding (experiment 2, 31 claims) | tested |
16	| exp3-units-cw-tuned to fig8k-awake-binary-decoder (experiment 3, 8 claims) | tested |
17	| fig8b-awake-behavior | blocked: the files hold no lick times or trial types |
18	=== [1] code ===
19	import hashlib
20	import fsspec
[... 719 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "lj2019.py"
}
```

```
1	"""Loading and measures for CRCNS ssc-9 (Laboy-Juarez, Langberg, Ahn & Feldman 2019).
2	
3	The data set is one zip, ``ssc-9/live/data.zip``, in the public S3 bucket ``crcnsarchive``.
4	It is opened in place over range requests (fsspec and zipfile, docs/archives.md, "CRCNS"); each
5	MATLAB file is read into memory, reduced to spike counts per trial, and dropped.
6	
7	Where each parameter comes from:
8	
9	- Response window, 0 to 125 ms after the onset of the first deflected whisker: claims file,
10	  "Common method" (Methods, "Analysis of neuronal data" and "dt smoothing").
11	- Whisker labels: the data descriptor (paper/ssc-9.data-description.txt and its PDF figure).
12	  Experiments 1 and 2 use the grid 1 4 7 / 2 5 8 / 3 6 9 (columns caudal to rostral, rows
13	  dorsal to ventral), CW = 5; experiment 3 uses 6 7 8 / 3 4 5 / 1 2 9, CW = 4.
14	- dt sign: negative dt means the SW leads the CW (Fig. 1c legend, "negative dt (SW precedes
15	  CW)"), so dt = t_SW - t_CW.
16	- Experiment 3 epochs have no deflection times. DeltaT is the time of the second whisker in
17	  DeflectedWs minus that of the first, and epoch time 0 is the first deflection in time; this is
18	  shown from the latency of the CW response in the notebook's data check (a finding, the data
19	  descriptor does not say it).
20	- Poisson likelihood ratio test of responsiveness across the nine whiskers and sham: Methods,
[... 600 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 740,
 "limit": 620
}
```

```
740	    print(rec, f"{time.time() - t0:.0f} s", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, flush=True)
741	S2 = U2[["unit", "file", "recording", "depth", "animal"]].merge(pd.DataFrame(rows2), on=["unit", "recording"])
742	S2["layer"] = S2.depth.apply(L.layer_of)
743	print(len(S2), "unit-sets;", S2.unit.nunique(), "units")
744	--OUT--
745	20160225:10da10 8 s 3.661836
746	
747	--OUT--
748	20160316:2dc362 10 s 3.661836
749	
750	--OUT--
751	20160325:946652 24 s 3.661836
752	
753	--OUT--
754	20160406:237ffc 45 s 3.661836
755	
756	--OUT--
757	20160504:6b0f02 57 s 3.661836
758	
759	--OUT--
[... 600 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1359,
 "limit": 600
}
```

```
1359	
1360	=== [82] markdown ===
1361	### fig7a-dt-half-width
1362	
1363	> For their best combinations, combination-selective units had sharp dt tuning with an average half-width of about 10 ms around the best dt; suboptimal combinations had weaker, broader dt tuning.
1364	=== [83] code ===
1365	lags = np.arange(-100, 101)
1366	def aligned(g):
1367	    best, sub = [], []
1368	    for _, r in g.iterrows():
1369	        cv = CUR[(r.unit, r.set)]["curves"] / CUR[(r.unit, r.set)]["curves"].max()
1370	        A = np.full((8, len(lags)), np.nan)
1371	        A[:, 100 - r.j_best: 100 - r.j_best + 101] = cv
1372	        best.append(A[r.c_best]); sub.extend(np.delete(A, r.c_best, axis=0))
1373	    return np.array(best), np.array(sub)
1374	def halfwidth(curve, mode):
1375	    c = curve[np.isfinite(curve)] if False else curve
1376	    pk = c[100]
1377	    lvl = (pk + np.nanmin(c)) / 2 if mode == "halfway" else pk / 2
1378	    left = np.where(np.isfinite(c[:100]) & (c[:100] <= lvl))[0]
[... 580 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; cat ssc-9.data-description.txt | head -150; wc -l *.txt
```

```
Data descriptor: of the data set CRCNS:ssc-9, not a paper. It describes the data set's files and how they were recorded.
Version: as published by CRCNS.org, https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/docs/crcns_ssc-9_data_description.pdf
Source: the CRCNS data set's documentation (ssc-9/live/docs/crcns_ssc-9_data_description.pdf)
Stored: 2026-11-06
Extracted: PyMuPDF, dehyphenated, NFKC
------------------------------------------------------------------------
##### ssc-9/live/docs/crcns_ssc-9_data_description.pdf
Page 1 of 4 
CRCNS.org ssc-9 data description 
Version 0.6 (May 13, 2019) 
Extracellular recordings in mouse barrel cortex during single- and 2-whisker stimulation 
Keven J. Laboy-Juárez, Tomer Langberg, Seoiyoung Ahn, and Daniel E. Feldman 
 
Summary 
The data set consists of acute extracellular recordings in primary whisker 
somatosensory cortex (S1) of awake and anesthetized mice during passive whisker 
stimulation, delivered with a 3x3 array of piezoelectric actuators. The recording 
electrode was placed in the cortical column corresponding to the whisker in the center of 
the array; thus, the stimulated whiskers were the columnar whisker (CW) of the column 
being recorded and 8 surrounding whiskers (SWs). Neural activity is described by the 
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "caudal|rostral|direction" 10.1038-s41593-019-0448-6.txt | head -60
```

```
76:Spatially asymmetric, sublinear suppression for suboptimal combinations and near-linearity for preferred combinations sharpened combination tuning relative to linearly predicted tuning. This resembles computation of motion direction selectivity in 
317:motion contrast19, we presented both same-direction and oppositedirection CW–SW deflections (termed correlated and anti-correlated stimuli, respectively). Single-whisker stimuli and a subset of 
479:Caudal
481:Rostral
578:a strong bias toward the rostral within-row SW and SWs ventral 
602:(1 out of 8) (Fig. 3e). Accuracy was highest for the CW–SW combination involving the rostral within-row SW (82% for N = 187) and 
1162:toward CW–SW combinations that include rostral and ventral 
1163:SWs matches the prevalence of rostrocaudal contact sequences 
1722:direction selectivity (DS) in mammalian retina. Barlow–Levick 
1724:responses to the null direction of visual motion while the preferred 
1725:direction lacks inhibition44–46. DS can also involve selective facilitation for the preferred direction47–49. Sublinear integration for nonoptimal CW–SW combinations and near-linear integration for the 
1783:distribution of directional tuning for global motion in the mouse 
1847:	44.	Barlow, H. B. & Levick, W. R. The mechanism of directionally selective units 
1849:	45.	Mauss, A. S., Vlasits, A., Borst, A. & Feller, M. Visual circuits for direction 
1858:and offset, delayed inhibition computes directional selectivity in Drosophila. 
1863:	48.	Livingstone, M. S. Mechanisms of direction selectivity in macaque V1. 
1866:visual cortex. I. Mechanisms of direction and speed selectivity in extrastriate 
1907:(coordinates: 1.5 mm rostral, 3.3 mm lateral of bregma). The target column  
1927:at 5-mm distance from the face. Each whisker was deflected rostrocaudally with a 
1944:deflections (9 whiskers with a peak deflection amplitude in either the rostral or 
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1920,2080p 10.1038-s41593-019-0448-6.txt
```

```
electrode with DiI, perfusing the mouse and recovering DiI staining in cytochrome 
oxidase-stained flattened tangential sections, which show the L4 barrels.
Whisker stimulation. Calibrated deflections were independently applied to a 3 × 3 
grid of whiskers, centered on the columnar whisker for the recorded column (either 
C1 or D1). Stimuli were controlled using custom software in Igor Pro (Wavemetrics). 
Each whisker was trimmed to 8 mm in length and inserted into a glass tube carried 
on a piezoelectric bender actuator. The piezo was positioned to deflect the whisker 
at 5-mm distance from the face. Each whisker was deflected rostrocaudally with a 
triphasic waveform that was previously shown to optimally drive S1 neurons and 
captured most of the evoked response variance in S1 (first common filter)19 (Fig. 1a). 
The waveform was 40 ms in duration, 300 μm in peak amplitude (3.8° deflection) 
and had a mean frequency content of 53 Hz. The waveform resembles a linear 
combination of position and velocity filters, which are two kinematic features that 
are strongly represented across the whisker-to-barrel system19,51,52.
Experiments 1 and 2 differed in the stimulus set that was applied. Experiment 
1 had a total of 261 unique stimuli as follows: 9 single-whisker deflections and 252 
two-whisker sequences (that is, 9 choose 2 spatial combinations, each of which 
was delivered at 7 Δt values: 0, ±10, ±25 and ±50 ms) (Fig. 1a). Each singlewhisker stimulus was delivered 125–175 times (136.67 ± 14), and each two-whisker 
sequence was delivered 40–150 times (82.76 ± 35). Thus, experiment 1 sampled all 
possible two-whisker combinations within the 3 × 3 grid at a subset of Δt values. 
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/null.py <<'EOF'
import numpy as np, lj2019 as L, time
rng=np.random.default_rng(0)
KER=L.gaussian_kernels(101,L.SDS)
def sim(rates_fn, nunits=30, nshuf=1000):
    ps=[];stat=[]
    for u in range(nunits):
        comb=np.repeat(np.arange(8),101*10); dti=np.tile(np.repeat(np.arange(101),10),8)
        lam=rates_fn(comb,dti)
        y=rng.poisson(lam).astype(float)
        curves=np.zeros((8,101));kidx=[]
        for c in range(8):
            s=comb==c
            cv,ki,st,_=L.fast_dt_smooth(y[s],dti[s],rng,KER)
            curves[c]=cv;kidx.append(ki);stat.append(st)
        csi=L.sparseness(curves.T)
        sh=L.shuffle_csi(y,comb,dti,kidx,KER,rng,n_shuf=nshuf)
        p,_=L.mahalanobis_p(csi,sh); ps.append(p)
    ps=np.array(ps); stat=np.array(stat)
    return ps, {s:np.mean(stat==s) for s in ['monotonic','unsmoothed','modulated']}
t=time.time()
for lam0 in [0.3,1.0]:
    ps,st=sim(lambda c,d: np.full(c.shape,lam0))
    print('null lam',lam0,'frac p<0.05',np.mean(ps<0.05),'p quantiles',np.round(np.quantile(ps,[.1,.5,.9]),3),st, f'{time.time()-t:.0f}s',flush=True)
EOF
timeout 3000 python3 $TMPDIR/null.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/null.py", line 1, in <module>
    import numpy as np, lj2019 as L, time
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* ~/.local/bin 2>/dev/null; which -a python python3 uv pip pip3 conda 2>/dev/null; ls /opt 2>/dev/null
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config

/home/runner/.local/bin:
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
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip3
/usr/bin/pip3
/bin/pip3
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for p in /opt/hostedtoolcache/Python/3.13.18/x64/bin/python /usr/bin/python3.14; do $p -c "import numpy,scipy,pandas;print('ok')" 2>&1 | tail -1; done
```

```
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  uv venv $TMPDIR/venv -q && uv pip install -q --python $TMPDIR/venv/bin/python numpy scipy pandas fsspec scikit-learn 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import numpy,scipy;print(numpy.__version__)"
```

```
2.5.4
```

**Agent calls Bash**

```bash
cd  timeout 3500 $TMPDIR/venv/bin/python $TMPDIR/null.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/null.py", line 1, in <module>
    import numpy as np, lj2019 as L, time
ModuleNotFoundError: No module named 'lj2019'
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=. timeout 3500 $TMPDIR/venv/bin/python $TMPDIR/null.py
```

```
null lam 0.3 frac p<0.05 0.3333333333333333 p quantiles [0.015 0.136 0.383] {'monotonic': np.float64(0.7125), 'unsmoothed': np.float64(0.0), 'modulated': np.float64(0.2875)} 27s
null lam 1.0 frac p<0.05 0.43333333333333335 p quantiles [0.012 0.094 0.501] {'monotonic': np.float64(0.7083333333333334), 'unsmoothed': np.float64(0.0), 'modulated': np.float64(0.2916666666666667)} 54s
```

**Agent**

Synthetic null result: with no combination or dt tuning at all, the shuffle test gives p < 0.05 for 33 to 43% of units, far above the nominal 5%. Now checking which part causes it.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/null2.py <<'EOF'
import numpy as np, lj2019 as L, time
rng=np.random.default_rng(1)
KER=L.gaussian_kernels(101,L.SDS)
def one(mode,lam0=0.5,nshuf=1000):
    comb=np.repeat(np.arange(8),101*10); dti=np.tile(np.repeat(np.arange(101),10),8)
    y=rng.poisson(np.full(comb.shape,lam0)).astype(float)
    curves=np.zeros((8,101));kidx=[]
    for c in range(8):
        s=comb==c
        if mode=='const':
            curves[c]=y[s].mean(); kidx.append(None)
        elif mode=='fixed':
            raw=np.bincount(dti[s],weights=y[s],minlength=101)/np.bincount(dti[s],minlength=101)
            ki=int(np.where(L.SDS==5.1)[0][0]); curves[c]=KER[ki]@raw; kidx.append(ki)
        else:
            cv,ki,st,_=L.fast_dt_smooth(y[s],dti[s],rng,KER); curves[c]=cv; kidx.append(ki)
    csi=L.sparseness(curves.T)
    sh=L.shuffle_csi(y,comb,dti,kidx,KER,rng,n_shuf=nshuf)
    p,dm=L.mahalanobis_p(csi,sh)
    # also a 1-D test: mean CSI over dt
    p1=(1+np.sum(sh.mean(1)>=csi.mean()))/(1+len(sh))
    ev=np.linalg.eigvalsh(np.cov(sh,rowvar=False))
    return p,p1,(ev>1e-10*ev.max()).sum()
for mode in ['const','fixed','cv']:
    r=np.array([one(mode) for _ in range(30)])
    print(mode,'maha p<.05:',np.mean(r[:,0]<0.05),' mean-CSI one-sided p<.05:',np.mean(r[:,1]<0.05),' rank kept median',np.median(r[:,2]),flush=True)
EOF
PYTHONPATH=. timeout 3500 $TMPDIR/venv/bin/python $TMPDIR/null2.py
```

```
const maha p<.05: 0.03333333333333333  mean-CSI one-sided p<.05: 0.03333333333333333  rank kept median 1.0
fixed maha p<.05: 0.1  mean-CSI one-sided p<.05: 0.0  rank kept median 47.0
cv maha p<.05: 0.3  mean-CSI one-sided p<.05: 0.1  rank kept median 28.5
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dec.py <<'EOF'
import numpy as np, lj2019 as L
rng=np.random.default_rng(2)
def make(nunits, pref_p, gain=0.6, base=0.5, ntr=100):
    probs,labs=[],[]
    for u in range(nunits):
        pref=rng.choice(8,p=pref_p)
        rates=np.full(8,base); rates[pref]+=gain
        y=np.repeat(np.arange(8),ntr); x=rng.poisson(rates[y])
        probs.append(L.heldout_prob_rows(x,y,8,rng)); labs.append(y)
    return L.Pool(probs,labs,8)
for name,pp in [('uniform prefs',np.full(8,1/8)),('35% prefer class 0',np.r_[0.35,np.full(7,0.65/7)])]:
    pool=make(150,pp)
    for N in [10,50,150]:
        a=pool.accuracy(N,500,rng)
        print(name,N,'mean',a.mean().round(3),'per class',a.mean(0).round(2))
EOF
PYTHONPATH=. timeout 3000 $TMPDIR/venv/bin/python $TMPDIR/dec.py
```

```
uniform prefs 10 mean 0.28 per class [0.34 0.39 0.24 0.23 0.35 0.18 0.25 0.26]
uniform prefs 50 mean 0.52 per class [0.66 0.69 0.47 0.46 0.61 0.38 0.44 0.46]
uniform prefs 150 mean 0.782 per class [0.9  0.92 0.72 0.7  0.91 0.6  0.74 0.78]
35% prefer class 0 10 mean 0.268 per class [0.54 0.23 0.18 0.21 0.26 0.21 0.24 0.26]
35% prefer class 0 50 mean 0.487 per class [0.89 0.44 0.32 0.47 0.41 0.45 0.47 0.45]
35% prefer class 0 150 mean 0.725 per class [0.99 0.73 0.53 0.72 0.65 0.73 0.75 0.7 ]
```

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ssc-9/" | sed 's/<Contents>/\n/g' | grep -o '<Key>[^<]*</Key><LastModified>[^<]*</LastModified><ETag>[^<]*</ETag><Size>[^<]*' | sed 's/<[^>]*>/ /g'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ssc-9/" | head -c 3000; echo; curl -s -m 30 -I https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/filelist.txt; echo; curl -s -m 30 https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/checksums.md5; echo; cd $TMPDIR; $TMPDIR/venv/bin/python - <<'EOF'
import fsspec, zipfile
z=zipfile.ZipFile(fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip",block_size=2**16).open())
for i in z.infolist(): print(i.filename, i.file_size)
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/venv/bin/python - <<'EOF'
import urllib.request, zipfile, io
URL="https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip"
class R(io.RawIOBase):
    def __init__(s): s.pos=0; s.size=169025319
    def seekable(s): return True
    def readable(s): return True
    def seek(s,o,w=0):
        s.pos = o if w==0 else s.pos+o if w==1 else s.size+o; return s.pos
    def tell(s): return s.pos
    def read(s,n=-1):
        if n<0: n=s.size-s.pos
        if n==0: return b""
        req=urllib.request.Request(URL,headers={"Range":f"bytes={s.pos}-{s.pos+n-1}"})
        d=urllib.request.urlopen(req).read(); s.pos+=len(d); return d
z=zipfile.ZipFile(R())
for i in z.infolist(): print(i.filename, i.file_size)
EOF
```

```
Experiment1/ 0
Experiment1/20170515.mat 197920064
Experiment1/20170605.mat 187229784
Experiment1/20170513.mat 121144216
Experiment1/20170621.mat 268508984
Experiment1/20170510.mat 234340312
Experiment2/ 0
Experiment2/20160506.mat 37575384
Experiment2/20160504.mat 295982744
Experiment2/20160909.mat 177090632
Experiment2/20160808.mat 110691368
Experiment2/20160406.mat 227210616
Experiment2/20160817.mat 314003976
Experiment2/20160829.mat 99185816
Experiment2/20160803.mat 288344288
Experiment2/20160325.mat 132898224
Experiment2/20160316.mat 13991576
Experiment2/20160225.mat 46108640
Experiment2/20160914.mat 547630272
Experiment3/ 0
[... 7 more lines not kept]
```

**Agent**

No lick or trial-type files in the archive: the zip holds only the 23 session .mat files, and the descriptor lists no lick fields. A few more paper checks remain.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "maximal evoked|spikes per stim|spikes/stim|half-width|0\.81|Hz\)" 10.1038-s41593-019-0448-6.txt | head -30
```

```
66:SW (Fig. 1b, lower). CW-tuned and SW-tuned neurons had comparable spontaneous activity (1.28 ± 0.24 Hz and 2.08 ± 0.4 Hz, respectively) and maximal evoked firing (4.8 ± 0.48 spikes per stimulus 
67:and 4.56 ± 0.64 spikes per stimulus, respectively), but tuning was 
180:(spikes per stimulus)
182:(spikes per stimulus)
226:Spikes per stimulus
234:Spikes per stimulus
255:Spikes per stimulus
535:0.2 spikes per stimulus
564:(Fig. 2e) and maximal evoked firing rate (Supplementary Fig. 4). 
862:half-width of ~10 ms around the best Δt. Suboptimal combinations 
1023:rate during whisker stimulation periods was low (0.32 ± 0.10 Hz). 
1054:(spikes per stimulus)
1065:∆t (spikes per stimulus)
1200:enhancement (spikes per stimulus)
1226:(spikes per stimulus)
1296:(spikes per stimulus)
1299:(spikes per stimulus)
1553:(spikes per stimulus)
1554:Linear prediction (spikes per stimulus)
1589:0.5 spikes per stimulus
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 170,260p 10.1038-s41593-019-0448-6.txt | tr '\n' ' ' | head -c 2500; echo; sed -n 2365,2385p 10.1038-s41593-019-0448-6.txt
```

```
1 2 3 4 0 0 1 1 2 3 2 3 Best single whisker (spikes per stimulus) Best sequence (spikes per stimulus) CW–SW SW–SW Single whisker γ D1 D2 C1 0 0.2 0.4 0.6 0.8 E1 β E2 δ C2 γ D1 D2 C1 E1 β E2 δ C2 Whisker 2 D1 0 0.5 1 1.5 D2 E1 γ β δ C1 E2 C2 D1 D2 E1 γ β δ C1 E2 C2 b Cell 1, D1 column Cell 2, D1 column Spikes per stimulus None Whisker 2 Whisker 1  None Sequences γ, D1 D1, E2 Spikes per stimulus –1.5 –0.5 0.5 1.5 2.5 –1.5 –0.5 0.5 1.5 2.5 Best SW response (z-scored) CW response (z-scored) 2 –2 0 No. of units 20 CW-tuned SW-tuned e Spikes per stimulus 0 0.2 0.4 0.6 CW 
Diversity of combination tuning in S1. 
Combination tuning curves of 30 combination-selective units, chosen to be representative of the population. Asterisks
denote peak responses. Best ∆t’s are shown in the top left of each unit. 

=== page 5 ===
Supplementary Figure 4 
Relationship between firing rate and combination selectivity (CSI). 
(a)  Mean relationship between CSI and evoked firing rate to the best combination stimulus (large circles: mean, bars:
SEM), for all combination-selective (n = 187)  and non-selective (n = 264) units  in Experiment 2.  For stimuli at best ∆t. 
Small circles are individual units. (b) Distribution of mean evoked firing rate for best CW-SW combinations at best ∆t.
Each histogram bar corresponds to a firing rate bin from (a).  (c) Mean peak-aligned combination-tuning curves for 
combination-selective units with low firing rate (<0.81 spikes/stim, corresponding to the first two bins in (a) and (b).  N =
95 units. Left, tuning calculated from total spiking.  Right, tuning calculated after subtraction of mean spontaneous firing
rate of each unit.  Grey, tuning observed after shuffling spike counts across stimuli and trials. (d), Same as (c), but for 
combination-selective high firing rate units (>= 0.81 spikes/stim, corresponding to bins 3-10 in (a) and (b).  N = 92 units.
(e), Same as (d), but for non-selective high firing rate units. N = 91 units.  Shaded regions are SEM. As
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 850,880p 10.1038-s41593-019-0448-6.txt; grep -n -i "Fig. 7\b\|Figure 7\|^Fig. 7" 10.1038-s41593-019-0448-6.txt | head; grep -n -B2 -A25 "^Fig. 7 |" 10.1038-s41593-019-0448-6.txt | head -60
```

```
when we examined the relationship between nonlinear enhancement or suppression and the ranked strength of single-whisker 
SW responses, combination-selective units nonlinearly enhanced 
combinations that involved the strongest single SW (P = 1.2 × 10–8, 
one-factor ANOVA), while nonselective units showed an opposite, 
much weaker trend (P = 0.03) (Fig. 6c). Thus, combination-selective 
units achieve sharp combination tuning by having sharper linearly 
predicted tuning (that is, spatially asymmetric single-whisker tuning) (Fig. 3c) and by enhancing responses relative to the global 
sublinearity for combinations involving the strongest SW (or, equivalently, shielding these responses from sublinear suppression). The 
individual measurements underlying these findings are provided in 
Supplementary Fig. 7.
Tuning for Δt reveals space–time inseparability. Combinationselective neurons were also tuned for Δt. For the best CW–SW 
combinations, these units had sharp Δt tuning, with an average 
half-width of ~10 ms around the best Δt. Suboptimal combinations 
had weaker, broader Δt tuning around the best Δt of units (Fig. 7a). 
Mean Δt tuning, calculated after standard Δt smoothing, showed a 
minimum response at −10 ms Δt (Fig. 7b). The best combinations 
evoked maximal responses at −30 to −50 ms Δt (SW leads CW, 
corresponding to inbound motion toward the CW), while suboptimal combinations evoked weaker responses overall, with maximal 
a
CW-tuned units
[... 43 more lines not kept]
```

**Agent**

## A. Outcomes (50 claims in the claims file; the notebook tests 49 and treats 1 as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| exp1-units | reproduced | Cell 13, caudal singles with sham (a): 160 units, 144 responsive, layers 36/48/46/14. All are within tolerance. |
| fig1b-somatotopy | reproduced | Cell 16: the CW mean is largest (0.517), followed by rostral (0.368) and caudal (0.327) within-row. |
| exp1-cw-tuned-fraction | reproduced | Cell 18 (a): 87 CW-tuned, 57 SW-tuned, fraction 0.604. All within tolerance. |
| exp1-cw-sw-comparable-firing | not_reproduced | Spontaneous rates fit: 1.33 and 2.05 Hz. Maximal evoked firing is 0.58 and 0.60 spikes per stimulus against 4.8 and 4.56 (cell 20). Read as Hz over the 125 ms window, the same values are 4.65 and 4.80, which would match (see B4). |
| supp1d-sw-tuning-broader | reproduced | Cell 22 (a): p = 0.00072, SW-tuned broader. |
| fig1d-best-sequence-exceeds-single | reproduced | Slope 1.211 with intercept (1.345 through the origin); 143 of 144 units (99.3%) above the diagonal. |
| fig1e-best-combination-includes-cw | partially_reproduced | Main reading: 0.688 and 0.862 pass, but SW-tuned 0.421 is below the bound of 0.423 by about one unit. Same-direction variant (ii): 0.694, 0.851, 0.456, all within (cell 33; see B5). |
| fig1f-cwsw-exceeds-swsw | reproduced | Cell 28: 99 of 144 units above the diagonal, paired p = 1e-6, under both readings. |
| fig1g-cwsw-sharper | reproduced | CW-SW sparseness above SW-SW at 55 of 55 values of N. |
| supp2-sw-tuned-sharpest-cwsw | reproduced | SW-tuned above CW-tuned at 55 of 55 values of N. |
| exp2-units | reproduced | 247 units in the files (246 after dropping a duplicate). Under O2 (a) and sham (a), 231 correlated and 232 anti-correlated sets are responsive; all within tolerance. |
| methods-dt-modulation | not_reproduced | Cell 40: monotonic 0.574 (expected 0.33) and unsmoothed 0.000 (expected 0.23). Only the constant total, 2127, is within tolerance. Zero padding (cell 41) gives 0.011. |
| exp2-combination-selective-prevalence | not_reproduced | Cell 43: 318 selective and 145 nonselective sets (expected 187 and 264); 189 cells (expected 129); fractions 0.77, 0.64, 0.73. Both FDR families fail. |
| fig2f-shuffle-abolishes-tuning | reproduced | Measured CSI 0.033 against 0.000 shuffled. Under (a), the shuffled first point is 0.011 above the rest, inside that point's s.e.m. of 0.027. This is computed on 318 sets, not 187 (B1). |
| fig2f-most-selective-lower-firing | reproduced | Both spontaneous and evoked firing are lower in the most selective quarter, p < 1e-9 (cell 49). Same 318-set caveat. |
| supp4-selectivity-at-high-rates | not_reproduced | Group counts are 178 / 140 / 28 against 95 / 92 / 91. The peak test after spontaneous subtraction holds (ratio 22.9). |
| fig2g-best-combination-bias | reproduced | Rayleigh p = 1.1e-22. All 8 SWs appear as a best combination; rostral within-row is the most frequent (150); ventral 210 against dorsal 63. |
| fig3a-sharper-than-linear | reproduced | O3 (a) / O2 (a): p = 3e-43, and 91.1% of sets have measured CSI above linear. |
| fig3b-sharper-in-both-groups | reproduced | Both groups p < 1e-7 with measured higher (cell 57), but the groups are 318 and 145 sets. |
| fig3b-linear-sharper-in-selective | reproduced | p = 7.3e-5 with the selective sets higher (cell 59). Same group caveat. |
| supp6-layers | partially_reproduced | ANOVA p = 2.4e-5, with the L2/3 and L4 means above L5 and L6. Layer count L6 = 53 is outside 45 ± 4.5. |
| fig3e-identity-decoder | not_reproduced | At N = 187: 0.135 (expected 0.42). Rostral within-row 0.986, every other combination at most 0.04. The linear-prediction decoder is not lower by more than the sum of the s.d.s. |
| fig3g-binary-decoder | not_reproduced | N = 10: 0.61 to 0.62 under the best readings, below 0.63. N = 100: 0.82. |
| fig4a-sw-tuned-sharper | reproduced | O2 (a): 174 CW-tuned and 289 SW-tuned, both within tolerance; p = 3.6e-7 with SW-tuned higher. |
| fig4c-sw-tuned-decoding | not_reproduced | Reading (a): SW-tuned is lower at N = 100 and 150. Reading (b): CW-tuned at N = 150 is 0.132, not above 0.125 + 2 × 0.061. |
| fig5a-global-scaling | reproduced | Slope 0.636, R² 0.926 (centred), 3704 combinations. |
| fig5bc-linearity-index | partially_reproduced | No reading has both means within tolerance. Under (b, a), best 0.964 is within and nonoptimal 0.652 is within 10%; p = 1.8e-77. |
| fig5c-pseudo-unit-shuffle | reproduced | 0.680 and 0.671 (0.684 and 0.678 with 10,000 pseudo-units). |
| fig5c-sublinear-at-all-dt | reproduced | Peak nonoptimal index 0.703 against 0.909 for the best combination, p = 2e-61. |
| supralinear-best-8-percent | reproduced | Only under (a) with the selective sets: 0.0723, against a bound of 0.072. All-sets reading gives 0.093 (fails). Fragile, and the selective set is inflated (B1). |
| fig6b-best-above-worst-below-scaled | reproduced | All four paired tests p < 1e-6 in the stated directions. |
| fig6b-enhancement-not-different | not_reproduced | p = 0.0096; the difference is 0.045 (cell 77). |
| fig6b-suppression-greater-selective | reproduced | Bonferroni ×8: 0.0085 and 0.0008, with the selective sets more negative. |
| fig6c-enhancement-strongest-sw | partially_reproduced | Selective: p = 1.6e-9 with rank 1 largest. Nonselective: p = 0.17, so the second part fails. |
| fig7a-dt-half-width | partially_reproduced | All 318 sets: 16.5 / 14.9 / undefined. Excluding the 70 sets whose best curve is constant (an alignment artefact, B2): 11.5 ms under (a). The suboptimal curve is lower at the best dt, but its half-width is undefined. |
| fig7b-inbound-best-outbound-suboptimal | partially_reproduced | Best peaks at −50 ms, suboptimal at +42 ms and lies below. The minimum is at 0, −6 or −3 ms under the three readings, never −10 ± 1. The criterion gives no partial rule. |
| fig7c-pca | partially_reproduced | Modulated counts 373 and 1204 are within tolerance; PC1 crosses zero at 0 ms; PC2 is U-shaped. Three PCs explain 0.836, above the 0.825 bound. |
| fig7e-pc1-best-suboptimal | partially_reproduced | Selective: best −2.37 against suboptimal +0.21, p = 8.9e-8. The nonselective difference is 0.59 of the selective one (needs under a third), and PC2 differs (p = 0.005). |
| fig7f-inbound-sharper | partially_reproduced | Only reading (c) passes both tests (p = 0.03 and 1.3e-7). Its counts are 134 and 112 against 121 and 56. Under (a) and (b), the CSI test gives p ≈ 0.1. |
| fig7g-inbound-decoding | not_reproduced | Inbound-minus-outbound differences are 0.014 to 0.019 against mean bootstrap s.d. 0.057 to 0.075. |
| supp8-order-decoding | not_reproduced | 0.581 and 0.570 at N = 100, against a bound of 0.585. The selective-set miss (0.004) is within Monte Carlo error (s.e. ≈ 0.0065), so this outcome is fragile. |
| exp3-units-cw-tuned | reproduced | 81 units, 74 responsive, 46 CW-tuned; mean single-whisker tuning is largest at the CW. |
| fig8c-awake-cw-stronger | not_reproduced | Ratio 1.71 is within tolerance and the awake tuning is sharper, but t-test p = 0.0021, not < 0.001. |
| fig8d-awake-best-sequence | reproduced | Slope 1.234 (b) or 1.300 (a); 98.6% of units above. |
| exp3-combination-selective | reproduced | 27 of 74 (0.365); CW-containing best sequence in 0.704 of selective and 0.784 of all units. All within tolerance. |
| fig8h-awake-linearity | partially_reproduced | Best 0.941 is within; suboptimal 0.723 misses 0.71 ± 0.009 but is within 10%; p = 1.5e-16. |
| fig8i-awake-sharper-than-linear | reproduced | p = 9e-9; 94.6% of units above linear. |
| fig8j-awake-inbound-stronger | reproduced | Both readings: p < 1e-13, and −40 ms is highest. |
| fig8k-awake-binary-decoder | reproduced | Accuracy rises with N, reaching 0.815 (a) and 0.829 (b) at N = 25. |
| fig8b-awake-behavior | blocked (data_missing) | I checked the archive: the S3 listing and filelist.txt hold only data.zip, checksums and the descriptor. The zip holds only 23 per-session .mat files, and the descriptor documents no lick or Go/No-go fields. No part is testable. |

Totals: 28 reproduced, 10 partially reproduced, 11 not reproduced, 1 blocked.

## B. Problems

1. **[affects a conclusion]** The shuffle selectivity test is anti-conservative (cell 36; `L.fast_dt_smooth`, `L.shuffle_csi`, `L.mahalanobis_p`), and the notebook never checks its calibration.
   - On synthetic Poisson units with no combination or dt tuning, run through the notebook's own helpers, p < 0.05 for 33% (λ = 0.3) and 43% (λ = 1.0) of units.
   - With every curve held constant the test is calibrated (3%). With a fixed kernel it gives 10%; with the cross-validated kernel, 30%.
   - So the inflation comes mainly from choosing the kernel on the measured data, which is what the Methods describe, plus small-sample bias from the pseudo-inverse Mahalanobis distance.
   - The result is 318 selective sets against 187. That changes the group used in every selective-group claim: fig2f ×2, supp4, fig3b ×2, fig3e, fig3g, fig4c, fig6b ×3, fig6c, fig7a/b/e/f/g, supp8 and supralinear (d).

2. **[affects a conclusion]** `derive` (cell 45): when the best combination's curve is constant (90 sets, 70 of them selective), `argmax` breaks the tie at dt = −50 ms. The markdown flags this, but most analyses still use it:
   - fig7a aligns flat curves at lag 0, which raises the half-width from 11.5 to 16.5 ms.
   - fig7f readings (a) and (b) count these 70 sets as inbound.
   - The decoder windows and O3 (b) for these sets sit at an arbitrary ±5 ms around −50.

3. **[affects a conclusion]** methods-dt-modulation (cell 40, `fast_dt_smooth`): "unsmoothed" never wins (0%). In my synthetic runs at λ = 1, where the 1e-3 floor rarely binds, it also never won. So the paper's 23% likely comes from a scoring choice the notebook does not explore. The zero-padding reading (1.1%) shows the outcome is very sensitive to these details.
   - Minor: the unused `dt_smooth` defines "monotonic" differently from `fast_dt_smooth`.

4. **[affects a conclusion]** exp1-cw-sw-comparable-firing: this is a claims-file issue, copied from the paper. The paper's "4.8 ± 0.48 spikes per stimulus" cannot be a per-stimulus mean: the Fig. 1d axis tops out near 4 spikes per stimulus. The notebook's values in Hz (0.581/0.125 = 4.65; 0.601/0.125 = 4.80) match all four expected values. The claims file should name a Hz reading; the notebook did not run one.

5. **[affects a conclusion]** Cell 11: the main experiment 1 analysis pools opposite-direction pair trials in the two 20170510 recordings into sequence means. The paper's 261 stimuli include no opposite-direction pairs. Variant (ii), which drops them, flips fig1e from a one-unit miss to a pass.

6. **[affects a conclusion]** Two outcomes sit on a boundary at the level of sampling noise:
   - supp8 (cell 103): 0.581 against a bound of 0.585, with Monte Carlo s.e. ≈ 0.0065.
   - supralinear (cell 73): 0.0723 against a bound of 0.072, and only on the inflated selective set.

7. **[does not affect a conclusion]** fig7a reading (b) averages over only 74 of 318 sets that have a defined half-width.

8. **[does not affect a conclusion]** fig7g (cell 101): the positive dt ranges (0–9 … 30–39, 41–50) leave out +40 ms and are not mirror images of the negative ranges. The decoder is near chance either way.

9. **[does not affect a conclusion]** supp4 runs only O3 (a). The counts are too far off for O3 (b) to rescue them.

10. **[does not affect a conclusion]** Two recordings in experiment 2 have no sham trials, so their units are tested on the nine whiskers alone. Experiment 3 cannot apply the lick exclusion. Both are stated in the notebook.

11. **[does not affect a conclusion]** The decoder helpers (`heldout_prob_rows`, `Pool.accuracy`) pass a synthetic check: accuracy rises with N, there is no train/test leakage, and they do not collapse under a 35% preference bias. The near-chance real decoding therefore reflects weak single-trial tuning in the inflated selective pool, not a bug I could find.

Things I checked that hold: the whisker grids for both experiments match the descriptor's figure order and its D1 example; dt = t_SW − t_CW; the experiment 3 epoch clock is consistent with the PSTH and clock checks (cells 7 and 9); the MD5 matches; no numbers are hard-coded.

## C. What I could not check, and the output that would settle it

- **Calibration on real data:** shuffle-test p-values for real sets with counts permuted across combinations within each dt (a real-data null), and a histogram of `p_shuffle`.
- **Experiment 3 field names:** printing `u._fieldnames` for one experiment 3 unit, which would confirm there are no lick or trial-type fields. The descriptor does not document `DeltaT` or `experiment`, nor the spikes up to 424 s after epoch onset.
- **The 20170510 direction coding:** raw `directionWs` and `timeWs` for a few mixed-direction trials, to tell whether this is a coding flip or real stimuli.
- **Experiment 1 claims under sham (b):** fig1e, fig1d and fig1b recomputed with the 147-unit, 89-CW-tuned set.
- **Fig. 7a, 7b and 7f with the constant-curve sets excluded or given NaN best dt:** reported under every listed reading.
- **Monte Carlo s.e. for decoder accuracies near a bound** (supp8, fig3g), with more ensembles.
- **Selective-group claims on a group of the paper's size:** for example the 187 sets with the smallest shuffle p-values, to show whether the decoder and Fig. 6 and 7 results depend on the inflated selective set.

## End of run

28 turns, 9 minutes, $2.78 at API prices, result: success.
