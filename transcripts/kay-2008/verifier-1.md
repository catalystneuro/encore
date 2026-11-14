# kay-2008 · verifier-1 · run 43562775180

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 852
drwxr-xr-x 6 runner runner    4096 Nov 14 06:29 .
drwxr-xr-x 8 runner runner    4096 Nov 14 06:29 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 05:41 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 05:41 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 14 06:29 .claude
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .env
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .env.development
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .env.local
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .env.production
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .env.test
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .env.test.local
drwx------ 2 runner runner    4096 Nov 14 06:29 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 05:41 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 05:41 .github
-rw-r--r-- 1 runner runner       0 Nov 14 06:29 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 05:41 .idea
[... 39 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kay-2008.yaml"
}
```

```
1	# Claims for Kay, Naselaris, Prenger & Gallant (2008), Nature 452:352-355, "Identifying natural
2	# images from human brain activity", doi:10.1038/nature06713, on CRCNS data set vim-1.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
5	#
6	# Text read: the version of record with its supplement, as PyMuPDF text under paper/
7	# (10.1038-nature06713.txt): the Letter, its Methods, and the Supplementary Information
8	# (Supplementary Figures 1 to 11, Supplementary Table 1, Supplementary Discussion 1 to 3,
9	# Supplementary Methods 1 to 11). PDF pages were rendered only for Figure 4 and Supplementary
10	# Figures 4, 5 and 8, whose numbers the text garbles. The data set's description
11	# (paper/vim-1.data-description.txt) was read only to know what it holds; no claim comes from it.
12	#
13	# Code: the paper links no analysis code, so none was read. It names outside code for two steps:
14	# m-sequence generation by T. Liu (stimulus design only) and Gaussian kernel density estimation by
15	# A. Ihler (http://ttic.uchicago.edu/~ihler/code/), used for the set-size extrapolation.
16	#
17	# Data the paper used. Two subjects, S1 (author T.N., 33) and S2 (author K.N.K., 25). 4 T Varian
18	# INOVA scanner, 18 coronal slices over occipital cortex, 64 x 64 matrix, TR 1 s, nominal 2 x 2 x
19	# 2.5 mm. Stimuli are 20 x 20 degree greyscale natural photographs (500 x 500 px, circular mask),
20	# each trial 4 s, an image flashed ON-OFF-ON-OFF-ON (200 ms each) for 1 s then 3 s grey. Five scan
[... 662 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "vim1.py"
}
```

```
1	"""Loading and the identification pipeline of Kay, Naselaris, Prenger & Gallant (2008) for CRCNS vim-1.
2	
3	Kay et al. (2008), Nature 452:352-355, doi:10.1038/nature06713. Files are streamed from the public
4	CRCNS bucket (crcnsarchive, vim-1/); nothing is written to disk.
5	
6	The data set holds, per subject, the estimated (repeated-trial) responses of about 26,000 voxels to
7	the 1,750 model estimation images (`dataTrn`) and the 120 identification images (`dataVal`), z-scored
8	per voxel, with ROI labels (0 other, 1 V1, 2 V2, 3 V3, 4 V3A, 5 V3B, 6 V4, 7 LatOcc), and the
9	stimuli at full resolution (500 px over 20 degrees).
10	
11	Where the parameters come from (claims file `claims/kay-2008.yaml`, opening comment, P1 to P6 and
12	O1 to O7, which cite the Supplementary Methods; SM below):
13	
14	- Stimulus resolutions min(500, round(2 ** (9 - x / 8))), x = 0..24 (SM 6, "Stimulus
15	  pre-processing"); mean luminance over all stimuli subtracted (SM 6). Stimulus values are taken as
16	  linear in luminance (O4, an assumption: the goggles' response is not given).
17	- Down-sampling uses area averaging (a standard choice for a detail that should not change a
18	  result; SM 6 does not say how the stimuli were resampled).
19	- Gabor wavelet pyramid (SM 6, "Design of the wavelet pyramid"): f = 1, 2, 4, 8, 16 (and 32 at
20	  128 px) cycles per field of view, centres on an f x f grid at the cell centres (O3, standard
[... 641 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_kay_2008.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"\n===== CELL {i} [{c['cell_type']}] =====")
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if o['output_type']=='stream':
                t=''.join(o['text']); print('--- out:'); print(t[:6000])
            elif o['output_type'] in ('execute_result','display_data'):
                d=o['data']
                if 'text/plain' in d: print('--- res:'); print(''.join(d['text/plain'])[:4000])
                if 'image/png' in d: print('--- [image]')
            elif o['output_type']=='error':
                print('--- ERROR', o['ename'], o['evalue'])
EOF
```

```
<persisted-output>
Output too large (55.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/ebcd85b8-2b07-4e07-bdef-07d697d38488/tool-results/b4yzit7da.txt

Preview (first 2KB):
29

===== CELL 0 [markdown] =====
# Reproducing Kay et al. (2008) from CRCNS vim-1

**Paper.** Kay KN, Naselaris T, Prenger RJ, Gallant JL (2008). Identifying natural images from human
brain activity. *Nature* 452:352-355. [doi:10.1038/nature06713](https://doi.org/10.1038/nature06713).
The claims file `claims/kay-2008.yaml` was written from the version of record with its
Supplementary Information (Supplementary Figures 1 to 11, Supplementary Table 1, Supplementary
Discussion 1 to 3, Supplementary Methods 1 to 11; SM below).

**Data set.** CRCNS [vim-1](http://crcns.org/data-sets/vc/vim-1), doi:10.6080/K0QN64NG, read
anonymously from the public bucket `crcnsarchive` (`vim-1/`, no `live/` folder). CRCNS data sets are
not versioned, so the version is recorded as `unversioned` (docs/archives.md); the paper cites no
version, and the bucket holds a single copy, the one documented by the data set's readme version
1.2 of 2013-04-09. The MD5 sums of the files read, from the data set's `checksums.md5`, are:
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ebcd85b8-2b07-4e07-bdef-07d697d38488/tool-results/b4yzit7da.txt"
}
```

```
1	29
2	
3	===== CELL 0 [markdown] =====
4	# Reproducing Kay et al. (2008) from CRCNS vim-1
5	
6	**Paper.** Kay KN, Naselaris T, Prenger RJ, Gallant JL (2008). Identifying natural images from human
7	brain activity. *Nature* 452:352-355. [doi:10.1038/nature06713](https://doi.org/10.1038/nature06713).
8	The claims file `claims/kay-2008.yaml` was written from the version of record with its
9	Supplementary Information (Supplementary Figures 1 to 11, Supplementary Table 1, Supplementary
10	Discussion 1 to 3, Supplementary Methods 1 to 11; SM below).
11	
12	**Data set.** CRCNS [vim-1](http://crcns.org/data-sets/vc/vim-1), doi:10.6080/K0QN64NG, read
13	anonymously from the public bucket `crcnsarchive` (`vim-1/`, no `live/` folder). CRCNS data sets are
14	not versioned, so the version is recorded as `unversioned` (docs/archives.md); the paper cites no
15	version, and the bucket holds a single copy, the one documented by the data set's readme version
16	1.2 of 2013-04-09. The MD5 sums of the files read, from the data set's `checksums.md5`, are:
17	
18	| File | MD5 |
19	|---|---|
20	| EstimatedResponses.mat | 7b702b34d42ba612118d6ad99e86e217 |
[... 630 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ebcd85b8-2b07-4e07-bdef-07d697d38488/tool-results/b4yzit7da.txt",
 "offset": 650
}
```

```
650	            RO[subj, metric, cname] = 100 * (choice == np.arange(120)).mean()
651	        print(f"{subj} RO {metric}: O1a {RO[subj, metric, 'candA']:.1f}%, O1b {RO[subj, metric, 'candB']:.1f}% "
652	              f"({time.time() - t:.0f} s)")
653	        del L, C
654	gwp_mean = {name: np.mean([100 * (ID[s, name]["choice"] == np.arange(120)).mean() for s in ("S1", "S2")]) for name in READINGS}
655	for cname in ("candA", "candB"):
656	    w_ = np.mean([RO[s, "weighted", cname] for s in ("S1", "S2")])
657	    s_ = np.mean([RO[s, "standard", cname] for s in ("S1", "S2")])
658	    print(f"{cname}: mean over subjects, weighted {w_:.1f}% (paper 55), standard {s_:.1f}% (paper 42)")
659	print("GWP mean over subjects:", {k: round(v, 1) for k, v in gwp_mean.items()})
660	--- out:
661	S1 RO weighted: O1a 68.3%, O1b 68.3% (33 s)
662	
663	--- out:
664	S1 RO standard: O1a 59.2%, O1b 58.3% (31 s)
665	
666	--- out:
667	S2 RO weighted: O1a 38.3%, O1b 37.5% (28 s)
668	
669	--- out:
[... 228 more lines not kept]
```

**Agent**

Notebook, helper module and claims file read. Now checking the archive file list and a few paper passages.

**Agent calls Bash**

```bash
cd  curl -s --max-time 60 "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=vim-1/" | python3 -c "
import sys,re
x=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',x): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)<',x))
" | head -150
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "tuning curve|absolute|weighted luminance|Supplementary Figure 11|completely within|within the stimulus|42205|DC offset|single-trial|first-order|autoregress" 10.1038-nature06713.txt | head -60
```

```
192:activity patterns from single trials. Single-trial performance was
208:Subject S1, voxel 42205, area V1
246:orientation and spatial frequency tuning curves. Error bars
719:7. Example of ROI-averaged tuning curves .......................................................................... 8 
802:pairs are weighted and then summed. Finally, a DC offset is added. The weights are determined 
835:performed substantially worse than the GWP model. c–d, Single-trial results for subjects S1 and 
872:Supplementary Figure 7. Example of ROI-averaged tuning curves. Several of the 
874:spatial frequency tuning curve of a voxel to match the mean tuning curve across voxels in the 
876:tuning curve for area V1. The x axis indicates orientation and the y axis indicates predicted 
878:tuning curve is nearly flat. b, Example ROI-averaged spatial frequency tuning curve for area V1. 
880:frequency tuning curve is band-pass. 
953:Supplementary Figure 11. Relationship between receptive-field size and eccentricity. In the 
961:was not completely within the stimulus bounds were omitted before pooling.) For each bin with 
1210:presentation the first 6 trials were repeated at the end of the 168-trial sequence. In the repeatedtrial analysis, data collected during the initial 6 trials were ignored53,54. In the single-trial analysis, 
1252:The single-trial analysis produced, for each voxel, an estimate of the amplitude of the response (a 
1282:model estimation response, the ratio between the absolute value of the response and its standard 
1291:Single-trial analysis 
1299:model estimation and image identification runs as the single-trial model estimation responses 
1300:and single-trial image identification responses, respectively. Next, the single-trial model 
1302:standard deviation) was applied to the single-trial image identification responses. After this 
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 200,250p 10.1038-nature06713.txt; echo ----; sed -n 950,965p 10.1038-nature06713.txt; echo ----; sed -n 1578,1600p 10.1038-nature06713.txt; echo ----; sed -n 1695,1775p 10.1038-nature06713.txt; echo; sed -n 1290,1320p 10.1038-nature06713.txt
```

```
1,000 images (Fig. 4b). As set size increased tenfold from 100 to 1,000,
performance only declined slightly, from 92% to 82% (subject S1,
Orientation (°)
0
45
90 135
Response
a
Subject S1, voxel 42205, area V1
0
+
0
+
–
0.4
1.5
0.7
0.2
2.9
b
[... 186 more lines not kept]
```

**Agent**

Archive confirms no later S1 sessions, no 999-image library and no retinotopy scans; the 70 raw runs are present. Now testing helper functions on synthetic inputs.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, sys, types
for m in ("fsspec","h5py"):
    try: __import__(m)
    except ImportError: sys.modules[m]=types.ModuleType(m)
import vim1
rng=np.random.default_rng(0)
# area_matrix rows sum to 1 and resize keeps constant image
A=vim1.area_matrix(500,215); print("area rows sum1:",np.allclose(A.sum(1),1))
print("resize const:",np.allclose(vim1.resize_stack(np.ones((1,500,500),np.float32),128),1))
# gwp counts
W,t,M=vim1.gwp(64,5); print("64px channels",W.shape, "masks sum1",np.allclose(np.asarray(M.sum(1)).ravel(),1,atol=1e-4))
Wd=W.toarray(); print("unit length",np.allclose(np.linalg.norm(Wd,axis=0),1,atol=1e-4),"zero mean (excl lum)",np.abs(Wd[:,:-1].sum(0)).max())
# grating at level 3 orientation 2 -> energy max at that channel
g=vim1.gratings()[2,3,0][None]
E=vim1.gwp_channels(g,Wd,t,np.ones(t.shape[0],bool),False)[0]
tab=t[:-1]; best=np.argmax(E[:-1]); print("grating ori2 lev3 -> channel lev,ori",tab[best][0],tab[best][4])
# orientation bandwidth: energy across orientations at lev 3 center channel
# fit_gd recovers linear kernel
X=rng.standard_normal((1750,20)); k=rng.standard_normal(20); Y=(X@k+0.5*rng.standard_normal(1750))[:,None]+3
stop=rng.choice(1750,350,replace=False)
kk,dc,err,it=vim1.fit_gd(X,np.repeat(Y,60,1),stop,max_iter=20000)
print("fit_gd r(k):",np.corrcoef(kk[:,0],k)[0,1], "iters",it[0], "dc",dc[0])
# identify: perfect predictions -> 120/120; loo power
V=800; pred=rng.standard_normal((120,V)); meas=pred+1.0*rng.standard_normal((120,V))
pw=vim1.loo_power(meas,pred)
ch,_=vim1.identify_repeated(meas,pred,pw); print("identify noisy:",(ch==np.arange(120)).mean())
ch,_=vim1.identify_repeated(rng.standard_normal((120,V)),pred,pw); print("identify null:",(ch==np.arange(120)).mean())
# loo power check vs direct
j=5; keep=np.arange(120)!=j; print("loo ok",np.allclose(pw[j,3],np.corrcoef(meas[keep,3],pred[keep,3])[0,1]))
# boot_p: null -> uniform-ish
p=vim1.boot_p(rng.standard_normal((120,500)),rng.standard_normal((120,500)),rng,200); print("boot_p null frac<0.01:",(p<0.01).mean())
# fit_gaussian
yy,xx=np.mgrid[0:32,0:32]+0.5; env=np.exp(-((yy-10)**2+(xx-20)**2)/(2*3**2))+0.1
print("gauss fit",np.round(vim1.fit_gaussian(env),2),"(expect 10,20,3)")
# edge_keep: channel far outside dropped
W1,t1,M1=vim1.gwp(128,6); kp=vim1.edge_keep(t1,M1,128,20,(0,0),9.5); print("edge keep frac",kp.mean())
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls; which python3 uv pip pip3 2>/dev/null; python3 -m venv $TMPDIR/v && $TMPDIR/v/bin/pip -q install numpy scipy 2>&1 | tail -2
```

```
bunfig.toml
kay-2008.yaml
node_modules
package-lock.json
package.json
paper
pnpm-lock.yaml
reproduce_kay_2008.ipynb
scripts
vim1.py
yarn.lock
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip3
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python3 - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, sys, types
for m in ("fsspec","h5py"):
    sys.modules[m]=types.ModuleType(m)
import vim1
rng=np.random.default_rng(0)
A=vim1.area_matrix(500,215); print("area rows sum1:",np.allclose(A.sum(1),1))
print("resize const:",np.allclose(vim1.resize_stack(np.ones((1,500,500),np.float32),128),1))
W,t,M=vim1.gwp(64,5); print("64px channels",W.shape, "masks sum1",np.allclose(np.asarray(M.sum(1)).ravel(),1,atol=1e-4))
Wd=W.toarray(); print("unit length",np.allclose(np.linalg.norm(Wd,axis=0),1,atol=1e-4),"zero mean max",np.abs(Wd[:,:-1].sum(0)).max())
G=vim1.gratings()
for (o,s) in [(2,3),(5,1),(0,4)]:
    E=vim1.gwp_channels(G[o,s,0][None],Wd,t,np.ones(t.shape[0],bool),False)[0]
    tab=t[:-1]; b=np.argmax(E[:-1]); print(f"grating ori{o} lev{s} -> lev,ori",tab[b][0],tab[b][4])
X=rng.standard_normal((1750,20)); k=rng.standard_normal(20); Y=(X@k+0.5*rng.standard_normal(1750))[:,None]+3
stop=rng.choice(1750,350,replace=False)
kk,dc,err,it=vim1.fit_gd(X,np.repeat(Y,60,1),stop,max_iter=20000)
print("fit_gd r(k):",round(np.corrcoef(kk[:,0],k)[0,1],4), "iters",it[0], "dc",round(dc[0],3), "norm ratio", round(np.linalg.norm(kk[:,0])/np.linalg.norm(k),3))
V=800; pred=rng.standard_normal((120,V)); meas=pred+1.0*rng.standard_normal((120,V))
pw=vim1.loo_power(meas,pred)
ch,_=vim1.identify_repeated(meas,pred,pw); print("identify noisy:",(ch==np.arange(120)).mean())
ch,_=vim1.identify_repeated(rng.standard_normal((120,V)),pred,vim1.loo_power(rng.standard_normal((120,V)),pred)); print("identify null:",(ch==np.arange(120)).mean())
j=5; keep=np.arange(120)!=j; print("loo ok",np.allclose(pw[j,3],np.corrcoef(meas[keep,3],pred[keep,3])[0,1]))
p=vim1.boot_p(rng.standard_normal((120,500)),rng.standard_normal((120,500)),rng,200); print("boot_p null frac<0.01:",(p<0.01).mean(), "frac<0.05", (p<0.05).mean())
yy,xx=np.mgrid[0:32,0:32]+0.5; env=np.exp(-((yy-10)**2+(xx-20)**2)/(2*3**2))+0.1
print("gauss fit",np.round(vim1.fit_gaussian(env),2),"(expect 10,20,3)")
# orientation tuning of a single channel: energy vs grating orientation at its SF
c=[i for i in range(len(t)-1) if t[i][0]==3 and t[i][4]==0][27]
resp=[np.mean([vim1.gwp_channels(G[o,3,p][None],Wd,t,np.ones(t.shape[0],bool),False)[0][c] for p in range(16)]) for o in range(8)]
print("single channel ori tuning (lev3):",np.round(np.array(resp)/max(resp),3))
EOF
```

```
area rows sum1: True
resize const: True
64px channels (4096, 5457) masks sum1 True
unit length True zero mean max 2.861023e-06
grating ori2 lev3 -> lev,ori 3.0 2.0
grating ori5 lev1 -> lev,ori 1.0 5.0
grating ori0 lev4 -> lev,ori 4.0 0.0
fit_gd r(k): 0.9999 iters 5573 dc 2.978 norm ratio 1.0
identify noisy: 1.0
identify null: 0.008333333333333333
loo ok True
boot_p null frac<0.01: 0.006 frac<0.05 0.044
gauss fit [10. 20.  3.] (expect 10,20,3)
single channel ori tuning (lev3): [1.    0.394 0.026 0.001 0.001 0.001 0.026 0.394]
```

**Agent**

**A. Outcomes** (23 claims, counted from `kay-2008.yaml`; the notebook's status table also lists 23)

| Claim | Outcome | Reason |
|---|---|---|
| fig3-s1-repeated-120 | reproduced | Cell 11: 109/120 (90.8%) under O1a-O5a and O1b-O5a, within 92 ± 9.2. Both O5b readings give 75.8%, outside tolerance. Chance is 1/120, as in the paper. |
| fig4a-s2-repeated-120 | reproduced | Cell 11: 87/120 (72.5%, O1a-O5a) and 86/120 (71.7%, O1b-O5a), within 72 ± 7.2. O5b gives 46.7%. |
| fig4a-single-trial | blocked (too_large, weakly shown) | Not run. The cost estimate in cell 16 is inflated (problem 2). The 70 raw runs are on the archive, and reading O6(a) is testable. |
| fig4a-noise-ceiling | blocked (depends on single-trial) | Needs single-trial patterns. It becomes testable once those exist. |
| fig4b-set-size-1000 | blocked (data_missing) | The archive listing has no 999-image library. |
| fig4b-extrapolation | blocked (data_missing) | Needs the library. |
| fig4c-retinotopy-only-extrapolation | blocked (data_missing) | Needs the library. |
| suppm8-retinotopy-only-120 | reproduced (caveat, problem 4) | Cell 24: subject means 53.3% weighted (55 ± 5.5) and 43.8% standard (42 ± 4.2) on O1a voxels; 52.9% and 42.5% on O1b voxels. Both are below the GWP means (81.7% under O5a, 61.2% under O5b). |
| suppfig8-constrained-models | blocked (data_missing) | Needs the library. The orderings at set size 120, which the criterion allows as a non-deciding variant, were not shown. |
| time-two-months | blocked (data_missing) | The archive listing has only five sessions per subject. |
| time-fourteen-months | blocked (data_missing) | Same as above. |
| errors-similar-images | reproduced | Cell 22, reading (b), local contrast: median percentile 61 to 69, one-sided Wilcoxon p from 1.2e-5 to 3.1e-4 under all four model readings. Reading (a), luminance, fails (p ≥ 0.7). The random-choice null centres on 49.6. |
| suppfig4-500-voxels | partially_reproduced | The notebook calls this blocked, but cell 28 computes the two repeated-trial conditions and both meet the rule. S1 O1a-O5a: 90.8% at 500 voxels (the maximum), above 61.7% at 50. S2: 72.5% at 500 against a maximum of 73.3%, above 45.8% at 50. The criterion defines "partially" as the rule holding in two or three conditions; the two single-trial conditions are untested. |
| supptable1-voxel-counts | reproduced | Cell 18: all six counts match exactly. They come from the data set's own ROI labels. |
| supptable1-predictive-power-by-area | reproduced (caveat, problem 5) | Cell 19: 6/6 values within 10% and V1 > V2 > V3 in both subjects. This relies on counting voxels with missing values as non-significant. |
| supptable1-snr | blocked (too_large, weakly shown) | Not run. Partly testable: see problem 2 and section C. |
| methods-v4-poor | reproduced (fragile) | Cell 20: V4 is below V3 in both subjects, but in S1 only by 17.5% against 18.2% (about 11 voxels), from a single random seed. |
| fig2-representative-voxel | partially_reproduced | Cell 26: the receptive field is in the left hemifield and spatial-frequency tuning peaks at the top frequency under both readings. Under O5a, whose 5.45° field of view gives exactly the figure's 2.9 cycles/deg axis, the envelope peak is above the horizontal meridian (+0.24°) and the orientation max/min is 2.23 (16.2 with the DC offset), so "just below" and "broadband" fail. Both hold only under O5b with the DC offset removed (−0.47°, ratio 1.77). |
| suppfig7-roi-tuning | not_reproduced (incomplete) | Cell 27: in every reading run, spatial-frequency tuning peaks at the highest level (16 cycles/FOV) and the orientation range is 31% to 449% of the mean, against the < 10% rule. The model-I reading and the suppfig8 voxel-set reading were not run. |
| suppfig10-retinotopy-validation | blocked (data_missing) | The archive has no retinotopic mapping scans, only `Sub*_Anat_msk`. |
| suppfig11-rf-size-eccentricity | partially_reproduced | Cell 25: Spearman ρ is 0.54 to 0.68 with p < 1e-27 in every area, so receptive-field size rising with eccentricity holds. V1 < V2 < V3 holds in most bins only for the square bounds with 1° bins (5/8). With 0.5° bins it is 6/12, and with the circular bounds 3/6 and 3/9. |
| suppdisc1-classification-extension | not_reproduced | Cell 23: under every reading, S2's contrast metric is not above chance (1 or 2 of 120, p ≥ 0.26; the paper reports 7, p < 0.0001). S1's contrast count is 9 (SD) or 4 against the paper's 6. The luminance results meet the criterion. |
| suppm7-selected-voxels-v1 | not_reproduced | Cell 21: the V1 share of the selected voxels is 0.42 to 0.48 under all readings and both subjects. V1 is the largest share but never more than half. |

**B. Problems**

1. **[affects a conclusion]** suppfig4 is marked blocked although cell 28 computes and meets its two repeated-trial conditions. It should be partially_reproduced. Cell 28 also prints only two of the four O1/O5 combinations.
2. **[affects a conclusion]** The `too_large` estimate in cell 16 is not well founded. It times `lstsq` on a random dense matrix and scales it to all 10,228 V1–V3 voxels of both subjects and to the training runs as well. Reading O6(a) needs single-trial amplitudes only from the identification runs (1,392 × about 344 per session), and only for candidate voxels (1,574 + 1,086 under O1a). The per-area fractions for supptable1-snr could be estimated from a random voxel subsample. The 70 runs are on the archive (about 150 MB each). This bears on fig4a-single-trial, fig4a-noise-ceiling, supptable1-snr and the single-trial half of suppfig4.
3. **[affects a conclusion]** In `gratings()` and `tuning_of` (cells 26 and 27), the curves that include the DC offset depend on the arbitrary grating amplitude of 0.5. The docstring says the amplitude "does not change their shape", which is false once the DC offset is added. The fig2 "broadband" ratio (16.2 under O5a, 6.54 under O5b) and the suppfig7 "with DC" results are therefore not meaningful; only the curves without DC are scale-invariant.
4. **[affects a conclusion]** `ro_channels` is called with `full + MU` (cell 24), so the luminance channel is the absolute value relative to the grey background (0). SM8 defines it as "absolute deviation from mean luminance", paralleling the GWP model, which subtracts the mean (SM6), and `MU` = −0.074. The notebook does not state this deviation. The values sit within tolerance by 3.8 and 2.4 points.
5. **[affects a conclusion]** In cell 19, voxels dropped for missing values (345 in S1 V1–V3, 214 in S2) count as non-significant. Using only voxels without missing values, which the cell also prints, puts 3 of 6 within tolerance (S1 V3 20.1%, S2 V1 29.0%, S2 V2 23.7%), which would be partial. The notebook prints both but neither decides nor discusses which is right.
6. **[affects a conclusion]** In cell 25, the "circle" filter tests `ecc + 2 SD ≤ R`, a disc, not the ±2 SD square that SM5 and Fig 2 define as the receptive-field location. Fig 2's legend calls the white circle "the bounds of the stimulus", which makes the square-field-of-view reading, the only one that passes, the less supported one. The radius used is 9.5°, from the mask's area; the paper describes a 20° circle.
7. **[affects a conclusion]** suppfig7 readings (b) (grating-transformed weights of model I) and voxel set (b) were not run, although the criterion lists them. The outcome is not_reproduced only for the readings that were run.
8. **[does not affect a conclusion]** The O1a candidate p-values use all 120 identification images, including the one being identified. P5 requires leaving that image out. O1b, which has no such leak, gives 109 (same) and 86 against 87.
9. **[does not affect a conclusion]** The 100 bootstrap fits are replaced by one fit (a stated deviation). The 10-fit variant (cell 13) was run only for O5b, not for O5a, which carries the reproduced values. Under O5b it changed counts by at most 3.
10. **[does not affect a conclusion]** About 30% of initial fits stop at iteration 0 (cell 7), because the run stops at the first non-decrease with step 0.001. Those voxels get no model and p = 1. This is an unstated reading of the stopping rule; the Supplementary Table 1 fractions still match.
11. **[does not affect a conclusion as run]** Every result comes from one seed with one shared stopping set. That margin matters for methods-v4-poor in S1 (0.7 percentage points).
12. **[does not affect a conclusion]** `error_percentiles` (cell 22) includes the selected image among the "others", which caps the percentile at 99.2. The effect is negligible.
13. **Claims-file reading, reported not corrected:** fig4a-noise-ceiling gives 13 or 14 trials per image. Cell 4 shows 13, 14 or 15 presentations per image across all runs.
14. **Synthetic tests of `vim1.py`** passed:
    - `area_matrix` and `resize_stack`.
    - `gwp`: unit-length, zero-mean wavelets; masks sum to 1; gratings select the matching level and orientation.
    - `fit_gd` recovers a linear kernel (r = 0.9999).
    - `loo_power` matches a direct calculation.
    - `identify_repeated` gives 100% on informative synthetic data and 1/120 on null data.
    - `boot_p` under the null: 0.6% below 0.01 and 4.4% below 0.05.
    - `fit_gaussian` recovers the generating parameters exactly.

**C. Not checked, and what would have let me**

- Sensitivity to the seed: identification counts and the methods-v4-poor V4/V3 comparison across three or more seeds.
- O5a with bootstrap averaging: cell 13 run under O5a.
- The retinotopy-only model with mean-subtracted luminance: cell 24 with `full` in place of `full + MU`.
- Whether the voxels with missing values had usable data in the paper: per-area counts of missing values by session would show whether they are slab edges.
- suppfig11: overall median receptive-field size per area, and the strict filter (all four corners of the ±2 SD square inside a 10° circle).
- fig2: the orientation ratio without DC at other grating amplitudes, and the centre of a Gaussian fitted to the final-model envelope (the raw peak sits on a flat plateau, 0.94 to 1.0).
- Single-trial cost: timing of one real BRS single-trial fit on one voxel's identification runs.
- The 60-minute notebook limit cited in cell 17: docs/protocol.md is not available to me.

## End of run

13 turns, 6 minutes, $1.64 at API prices, result: success.
