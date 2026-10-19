# 001712 · verifier-1 · run 39209668461

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls docs paper 2>/dev/null; cat *claims* 2>/dev/null | head -200
```

```
total 776
drwxr-xr-x 5 runner runner    4096 Oct 19 06:30 .
drwxr-xr-x 7 runner runner    4096 Oct 19 06:30 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 06:23 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 06:23 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 19 06:30 .claude
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .env
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .env.development
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .env.local
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .env.production
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .env.test
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .env.test.local
drwx------ 2 runner runner    4096 Oct 19 06:30 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 06:23 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 06:23 .github
-rw-r--r-- 1 runner runner       0 Oct 19 06:30 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 06:23 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 06:23 .mcp.json
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1101-2025.09.12.675910.yaml
```

```
# Claims for Davatolhagh, Couto, Melin, Oesch, Findling, Morales, Hong, International Brain
# Laboratory & Churchland (2025), bioRxiv preprint version 1, on dandiset 001712.
# Source: the full text of the preprint (CC-BY-NC-ND), read from its Results, figure legends,
# Methods and Supplementary Table 1.
#
# When these criteria were written, the author had seen the data check only: the dandiset's
# file list and metadata, the trial table's columns, counts and value ranges, the sampling
# rates and timestamps of the imaging and video-derived series, the orthonormality of the SVD
# spatial components, and the speed of streaming the body camera video. No claim's analysis
# had been run. The author had read the encoding-model code of the lab (churchlandlab/chiCa at
# commit d98b3c6), which the paper links for its linear encoding analyses.
#
# The dandiset holds one session of one mouse (FD-28), with no genotype in the files, the
# dandiset metadata or the public IBL database. The paper's findings that compare Nrxn1a KO
# with wild-type mice (8 against 11 mice, 10 sessions each) cannot be tested. The findings
# that the paper states for both genotypes, or for every mouse, are tested on this one session.
#
# Method choices fixed here, where the Methods are silent:
# - Reaction time is the wheel movement onset minus the stimulus onset (the paper's "time to
#   first movement"). A rightward choice is a counter-clockwise wheel turn, which moves the
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_davatolhagh_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'=== CELL {i} [{c[\"cell_type\"]}] ===')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:4000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT(data)--'); print(''.join(d['text/plain'])[:4000])
            if 'image/png' in d: print('[image]')
        if o.get('output_type')=='error': print('ERROR', o.get('ename'), o.get('evalue'))
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
982 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== CELL 0 [markdown] ===
2	# Reproducing Davatolhagh et al. (2025) from dandiset 001712
3	
4	**Paper.** Davatolhagh MF, Couto J, Melin M, Oesch LT, Findling C, Morales P, Hong I, International
5	Brain Laboratory, Churchland AK (2025). Altered use of prior expectations and modified neural
6	dynamics in a mouse model of autism. bioRxiv, version 1.
7	[doi:10.1101/2025.09.12.675910](https://doi.org/10.1101/2025.09.12.675910). This attempt used the
8	full text of the preprint (CC-BY-NC-ND).
9	
10	**Dandiset.** [DANDI:001712](https://dandiarchive.org/dandiset/001712/draft), version `draft`. The
11	paper cites no version, and the dandiset has no published version: the archive lists only the
12	draft. The draft is used, with its modification time (2026-05-28T10:04:28Z) and the ids and sizes
13	of the three assets read, which the next cell checks against the archive. A draft can change; if
14	the check reports a difference, the numbers below may not match the attempt record.
15	
16	**What the dandiset holds.** One session (2023-11-14) of one mouse, FD-28, in the biased
17	choice-world task with widefield imaging: a processed NWB file, a raw NWB file and three camera
18	videos. The paper analyses 11 wild-type and 8 Nrxn1a knockout mice with 10 sessions each. The
19	genotype of FD-28 is not stated in the files, the dandiset's metadata, or the public IBL
20	database. The findings that compare genotypes cannot be tested; those that the paper states for
[... 736 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 757
}
```

```
757	for name, r in pk_odd.items():
758	    vals = ev @ uim[:, r["pixel"]]
759	    sel_even = idx % 2 == 0
760	    a, b = (vals[sel_even & strong & right], vals[sel_even & strong & ~right]) if name == "right_minus_left" else (vals[sel_even & strong & ~right], vals[sel_even & strong & right])
761	    _, p = stats.mannwhitneyu(a, b, alternative="greater")
762	    print(f"Odd-trial {name} peak: row {r['row']}, column {r['col']} ({r['side']}); even trials: {np.median(a):.4f} against {np.median(b):.4f}, p = {p:.2g}")
763	# Variant: correct trials only and 100% contrast only.
764	for label, sel in (("correct trials", correct.to_numpy()), ("100% contrast", (trials.gabor_stimulus_contrast == 100).to_numpy())):
765	    m = (ev[sel & strong & right].mean(0) - ev[sel & strong & ~right].mean(0)) @ uim
766	    pr, pl = int(np.argmax(m)), int(np.argmax(-m))
767	    print(f"Variant, {label}: right-minus-left peak column {pr % W}, left-minus-right peak column {pl % W} (midline {midline})")
768	# Variant: peaks only among pixels brighter than the median of the mean image and 20 pixels or more from the frame edge.
769	yy, xx = np.mgrid[:H, :W]
770	mask = ((mean_img > np.median(mean_img)) & (yy >= 20) & (yy < H - 20) & (xx >= 20) & (xx < W - 20)).ravel()
771	print(f"Variant mask: {mask.sum()} of {mask.size} pixels")
772	for name, m in (("right_minus_left", rmap), ("left_minus_right", -rmap)):
773	    p = int(np.flatnonzero(mask)[np.argmax(m[mask])]); y, x = divmod(p, W)
774	    vals = ev @ uim[:, p]
775	    a, b = (vals[strong & right], vals[strong & ~right]) if name == "right_minus_left" else (vals[strong & ~right], vals[strong & right])
776	    _, pv = stats.mannwhitneyu(a, b, alternative="greater")
[... 207 more lines not kept]
```

**Agent**

Notebook read. Now the helper module.

**Agent calls Read**

```json
{
 "file_path": "wfprior.py"
}
```

```
1	"""Loading and measures for the widefield and behaviour session of dandiset 001712.
2	
3	Davatolhagh et al. (2025), bioRxiv, doi:10.1101/2025.09.12.675910.
4	
5	The dandiset holds one session of one mouse (sub-FD-28): a processed NWB file (trials, wheel,
6	pose, pupil, ROI motion energy, licks, and the widefield SVD components), a raw NWB file
7	(the widefield frames and sync events) and three camera videos. Files are streamed from the
8	archive; nothing is written to disk.
9	
10	The dandiset has no published version, so the draft is read. `DRAFT_ASSETS` gives the asset
11	ids and sizes this entry was written against, and `check_assets` reports any difference.
12	
13	Where the parameters come from:
14	
15	- Reaction time is the wheel movement onset minus the stimulus onset, the paper's "time to
16	  first movement" (Figure 1E). A rightward choice is a counter-clockwise turn (the trial
17	  table's description: it moves the stimulus leftward, which centres a right stimulus).
18	- The psychometric function is the lapse-and-erf form used by the IBL (IBL et al. 2021, the
19	  paper's reference 10): P(right) = gL + (1 - gL - gR) * Phi((c - bias) / sigma).
20	- The subjective prior is an action-kernel model (the paper's Methods cite the ActionKernel
[... 417 more lines not kept]
```

**Agent**

Helper module read. Next I'll fetch the paper text to check the methods for RT, the encoding model and the VISp analysis.

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL -A "Mozilla/5.0" "https://www.biorxiv.org/content/10.1101/2025.09.12.675910v1.full" -o paper/full.html; ls -la paper; grep -c "" paper/full.html; grep -o "<title>.*</title>" paper/full.html | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  cat paper/full.html; echo; curl -sL "https://api.biorxiv.org/details/biorxiv/10.1101/2025.09.12.675910" | head -c 3000; echo; curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1101/2025.09.12.675910&format=json&resultType=core" | python3 -c "import json,sys; d=json.load(sys.stdin); [print(r.get('id'),r.get('source'),r.get('pmcid'),r.get('fullTextIdList'),r.get('isOpenAccess')) for r in d['resultList']['result']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  curl -sL -A "Mozilla/5.0" "https://www.biorxiv.org/content/early/2025/09/13/2025.09.12.675910.source.xml" -o paper/source.xml; ls -la paper; head -c 300 paper/source.xml; echo; curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/PPR1083702/fullTextXML" -o paper/epmc.xml; ls -la paper; head -c 300 paper/epmc.xml
```

Result: the fetched text is not kept.

**Agent calls ToolSearch**

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```

Result: no output.

**Agent calls WebFetch**

```json
{
 "url": "https://www.biorxiv.org/content/10.1101/2025.09.12.675910v1.full",
 "prompt": "Quote verbatim: (1) the Methods text on reaction time / time to first movement and Figure 1E legend; (2) the Methods on the linear encoding model: predictors, video SVD, cameras used, cross-validation, how cvR2 is computed (pixels, brain mask, z-scoring, trial windows), shuffles; (3) Figure 3B legend and methods for contralateral VISp response; (4) Figure 2E-G methods on block switch fits; (5) imaging frame rate and indicator."
}
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sleep 60; cd  curl -sL -A "Mozilla/5.0 (X11; Linux x86_64)" "https://www.biorxiv.org/content/10.1101/2025.09.12.675910v1.full-text" -o paper/full.html; ls -la paper/full.html; head -c 200 paper/full.html
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  rm -f paper/full.html paper/source.xml paper/epmc.xml; curl -sL "https://api.biorxiv.org/details/biorxiv/10.1101/2025.09.12.675910" -o paper/biorxiv_details_abstract.json; ls paper
curl -s "https://api.dandiarchive.org/api/dandisets/001712/versions/draft/" -o $TMPDIR/meta.json; python3 - <<'E'
import json,os
d=json.load(open(os.environ['TMPDIR']+'/meta.json'))
for k in ['name','description','keywords','assetsSummary','relatedResource','dateModified','version']:
    print(k, json.dumps(d.get(k),indent=0)[:1500])
E
curl -s "https://api.dandiarchive.org/api/dandisets/001712/versions/draft/assets/?page_size=100" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['count']); [print(a['path'],a['size']) for a in d['results']]"
curl -s "https://api.dandiarchive.org/api/dandisets/001712/versions/" | python3 -c "import json,sys; d=json.load(sys.stdin); print([ (v['version'],v['modified']) for v in d['results']])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/001712/versions/draft/assets/3102badd-5260-498a-aaaf-acec7d7960e7/" | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('wasAttributedTo'),indent=1)); print(json.dumps(d.get('wasGeneratedBy'),indent=1)[:1500])"
```

Result: the fetched text is not kept.

**Agent**

Archive confirms one subject (FD-28) with no genotype at the asset or dandiset level, so the blocked statuses hold. Now testing the helper functions on synthetic data.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t.py <<'E'
import sys; sys.path.insert(0,'.')
import numpy as np
try:
    import wfprior as wf
except Exception as e:
    print("import failed", e); 
    import types, importlib.util
    for m in ['h5py','remfile','dandi','dandi.dandiapi']:
        sys.modules.setdefault(m, types.ModuleType(m))
    sys.modules['dandi.dandiapi'].DandiAPIClient=object
    import wfprior as wf
rng=np.random.default_rng(0)
# ridge vs closed form
n,p,k=500,20,3
X=rng.normal(size=(n,p)); Y=X@rng.normal(size=(p,k))+rng.normal(size=(n,k))*3
Xte=rng.normal(size=(50,p))
pred,al=wf._ridge_fold(X,Y,Xte)
xm,ym=X.mean(0),Y.mean(0)
for j in range(k):
    a=al[j]; Xc=X-xm
    b=np.linalg.solve(Xc.T@Xc+a*np.eye(p),Xc.T@(Y[:,j]-ym[j]))
    # brute GCV
    best=None
    for aa in wf.ALPHAS:
        H=Xc@np.linalg.solve(Xc.T@Xc+aa*np.eye(p),Xc.T)
        r=(Y[:,j]-ym[j])-H@(Y[:,j]-ym[j]); g=n*(r@r)/(n-np.trace(H))**2
        if best is None or g<best[0]: best=(g,aa)
    print("ridge pred err",np.abs((Xte-xm)@b+ym[j]-pred[:,j]).max(),"alpha",a,"brute",best[1])
# pixel R2 vs explicit
from scipy.stats import ortho_group
U=ortho_group.rvs(30,random_state=1)[:10]  # 10 comps x 30 pixels orthonormal rows
T=2000; Xd=rng.normal(size=(T,5)); Yc=Xd@rng.normal(size=(5,10))+rng.normal(size=(T,10))
tp=np.tile(np.arange(20),T//20)
fo=wf.folds(tp,np.random.default_rng(1))
print("fold sizes",[len(f) for f in fo], "per-tp balance", np.unique(np.bincount(tp[fo[0]])))
r=wf.fit_model(Xd,Yc,[0,1],fo,[],np.random.default_rng(2),U.T)
# explicit pixel
pix=Yc@U
vals=[];pool=[]
for te in fo:
    tr=np.setdiff1d(np.arange(T),te)
    Xtr,Xte_=Xd[tr].copy(),Xd[te].copy(); m,s=Xtr[:,:2].mean(0),Xtr[:,:2].std(0)
    Xtr[:,:2]=(Xtr[:,:2]-m)/s; Xte_[:,:2]=(Xte_[:,:2]-m)/s
    pr,_=wf._ridge_fold(Xtr,Yc[tr],Xte_)
    pp=pr@U; yt=pix[te]
    vals.append(np.mean(1-((yt-pp)**2).sum(0)/((yt-yt.mean(0))**2).sum(0)))
    # pooled over pixel space (U not full-rank in pixel; pooled uses components)
print("pixel_mean",r['pixel_mean'],"explicit",np.mean(vals))
# psychometric recovery
c=np.repeat([-100,-25,-12.5,-6.25,0,6.25,12.5,25,100],300)
pr=wf.psychometric(c,-7,17,0.1,0.02); y=(rng.random(len(c))<pr).astype(float)
print({k:round(float(v),3) for k,v in wf.fit_psychometric(c,y).items()})
# bin_to_frames
ft=np.arange(0,10,0.032); ts=np.arange(0,10,0.001); v=np.sin(ts)
b=wf.bin_to_frames(ts,v,ft)[:,0]; print("bin err",np.abs(b-np.sin(ft)).max())
# frame_index
print(wf.frame_index(ft,np.array([0.015,0.017,0.0,9.99])))
E
python3 $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 2, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls node_modules; which -a python python3 uv pip 2>/dev/null; ls ~/.venv* /opt 2>/dev/null | head; python3 -m pip --version
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.16/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.16/x64/bin/pip
/usr/bin/pip
/bin/pip
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipx
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv -q $TMPDIR/venv && uv pip install -q --python $TMPDIR/venv/bin/python numpy scipy pandas 2>&1 | tail -2; $TMPDIR/venv/bin/python $TMPDIR/t.py
```

```
import failed No module named 'h5py'
ridge pred err 1.3322676295501878e-14 alpha 10.0 brute 10.0
ridge pred err 1.0436096431476471e-14 alpha 17.78279410038923 brute 17.78279410038923
ridge pred err 2.1760371282653068e-14 alpha 10.0 brute 10.0
fold sizes [200, 200, 200, 200, 200, 200, 200, 200, 200, 200] per-tp balance [10]
pixel_mean 0.7629772440926624 explicit 0.7629772440926624
{'bias': -8.256, 'sigma': 17.31, 'lapse_left': 0.1, 'lapse_right': 0.013, 'nll': 1181.226, 'n': 2700.0}
bin err 0.007499850001197497
[  0   1   0 312]
```

**Agent**

**Verification report, round 1: Davatolhagh et al. 2025 (doi:10.1101/2025.09.12.675910) on DANDI 001712 (draft)**

The claims file lists 18 claims. The notebook tests 7 and marks 11 blocked for missing data. No attempt record was among my materials, so these counts come from the claims file and the notebook's code cells. bioRxiv refused every request from this host (Cloudflare error 1015, then HTTP 429), so I read only the abstract, saved as `paper/biorxiv_details_abstract.json`. For methods I relied on the claims file's account of the paper.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1c-psychometric | reproduced | Cell 16: Spearman rho is 1.000 over 9 signed contrasts. P(right) at +100% minus -100% is 0.887 (needs ≥0.5). The lapse-and-erf fit is reported (bias -6.8, sigma 17.0, lapses 0.116 and 0.0). |
| fig1d-psychometric-params-genotype | blocked (data_missing) | One mouse and no genotype anywhere (checked below). |
| fig1e-rt-contrast | not_reproduced | Cell 19: rho is -0.053 with p = 0.15, which fails the p < 0.05 requirement. The median at 0% (0.089 s) does exceed the median at 100% (0.081 s). The result depends on how anticipatory movements are handled: with RT > 0.15 s, p = 0.0006 (see B2). |
| fig1f-rt-genotype | blocked (data_missing) | Genotype comparison. |
| fig1g-learning-genotype | blocked (data_missing) | One session only, and no genotype. |
| fig2bc-prior-shift | reproduced | Cell 21: at 0% contrast P(right) is 74/89 in right blocks against 37/73 in left blocks, one-sided Fisher p = 9.2e-6. Differences at each contrast and per-block biases (+2.9 vs -16.5) are reported and point the right way. |
| fig2bd-ko-smaller-shift | blocked (data_missing) | Genotype comparison. |
| fig2ef-block-adaptation | reproduced | Cell 24: A = 0.48, B = 1.00, tau = 25.1 trials, all within the criterion. Trials 20–39 vs 0–4: 0.827 vs 0.543, Fisher p = 2.7e-6. The fit is weak: B sits at its upper bound and tau has SE 16 (B3). |
| fig2g-ko-slower-adaptation | blocked (data_missing) | Genotype comparison. |
| fig3b-contralateral-visual | not_reproduced | Cell 27: both peaks lie left of the midline, and the Mann-Whitney p values (0.053, 0.14) exceed 0.05. Both peaks are frame-corner pixels outside the brain, so the failure is an artefact of the criterion (B1). Even so, the evidence that the response is visual is weak. |
| fig3c-ko-elevated-activity | blocked (data_missing) | Genotype comparison. |
| fig3d-ko-higher-correlation | blocked (data_missing) | Genotype comparison. |
| fig3e-ko-higher-variance | blocked (data_missing) | Genotype comparison. |
| fig4c-full-cvr2 | partially_reproduced | Cell 33: the best reading is (a), full model cvR2 = 0.471. That is above 0.3 but below the range of 0.486–0.660. Readings (b) 0.422 and (c) 0.126 also miss, as do all three with the intercept subtracted (0.09–0.14). |
| fig4cd-movement-dominates | partially_reproduced | Cell 36: movement ΔR² is 0.104 / 0.119 / 0.067 under readings a / b / c, and task ΔR² is 0.017 / 0.015 / 0.013. Movement exceeds task under every reading and task is below a fifth of movement, but movement ΔR² is nowhere near 0.297–0.440. |
| fig4cd-ko-more-movement | blocked (data_missing) | Genotype comparison. |
| figs2-ko-elevated-motion | blocked (data_missing) | Genotype comparison. |
| figs3-ko-higher-unique | blocked (data_missing) | Genotype comparison, and no unique-variance model was run. |

**Blocked claims, checked against the archive:**
- The draft has 5 assets, one subject (FD-28) and one session. Draft is the only version.
- The asset's `wasAttributedTo` record has sex, strain (C57BL/6) and age, and no genotype.
- The dandiset description says "CNTNALP2 knockout", which contradicts Nrxn1a in the paper and in the file's keywords.
- No genotype contrast can be tested. The single-session quantities behind fig3c–e and figs2 (dF/F level, correlations, variance, motion energy) are in the data and could be computed, but with no comparison group they cannot test these claims.
- fig1g needs the training history, which is not in the archive.
- The notebook's blocked status is correct for all 11.
- The paper states no chance level for any selection, so there was nothing to compare.

### B. Problems

1. **[affects a conclusion] fig3b, cells 27–28.** No brain mask is applied.
   - Both "peaks" are at frame corners: (0,0) and (539,2). Mean fluorescence there is 534 and 926, against a 5th percentile of 1538.
   - With the post hoc mask (bright pixels, 20-pixel margin), the peaks fall on opposite sides of the midline (columns 199 and 481) with p of about 1e-15. That would make the outcome partially_reproduced.
   - However, the evoked window (0.1–0.4 s) contains the choice movement: median onset is 0.086 s (cell 12). The right-vs-left difference first exceeds its null only at 0.256 s (cell 12).
   - So the lateralization could come from the movement, not the visual stimulus. The notebook never separates the two, for example with trials where RT > 0.4 s.
2. **[affects a conclusion] fig1e, cell 19.**
   - The median RT is 0.069 s, and 149 of 899 onsets fall at or before stimulus onset (cell 5). Both point to `wheel_movement_onset_time` capturing many anticipatory movements, not visually driven ones.
   - The verdict changes with the RT floor: p = 0.15 overall, 0.068 for RT > 0.08 s, 0.0006 for RT > 0.15 s.
   - The RT distribution was never compared with the paper's Figure 1E.
3. **[does not affect a conclusion] fig2ef, `adaptation` (cell 24).**
   - B is pinned at its bound of 1.0.
   - tau has SE 16.1, so its plausible range extends past 40.
   - The curve is fitted unweighted to per-trial means whose n varies; the last block has only 9 trials.
   - The Fisher test carries the result on its own.
4. **[affects a conclusion: magnitude for fig4c and fig4cd] cell 30 and `body_video_components`.**
   - The movement set is reduced: no left or right camera video components, and the body video is binned 16×16 down to 1280 pixels.
   - Without the video components, movement ΔR² drops from 0.10 to 0.04. Under reading (c) it falls below task ΔR² (0.010 vs 0.015).
   - Movement ΔR² therefore depends heavily on the video regressors, and the shortfall against 0.30–0.44 may come from this reduced design. The claims file pre-specified this design, so the criterion outcome stands.
5. **[does not affect a conclusion] `segment_frames` and `folds` (cells 30–31).** Train and test data overlap.
   - Folds are random at the row level, so frames from the same trial land in both training and test sets. This follows chiCa.
   - 8,971 of 63,770 rows are the same imaging frame entered twice, because the stimulus and feedback windows overlap. Their Y and movement values are identical.
   - This can only inflate cvR2. The values are already below range, so the outcomes would not change.
6. **[does not affect a conclusion] `fit_model`, reading (b), and the pooled reading (a).** Both are computed over all 345,600 pixels, brain and non-brain, because the files hold no mask or atlas registration (cell 8).
7. **[does not affect a conclusion] "intercept only" model (cell 31).**
   - It shuffles all task and movement columns and keeps them, which is not a true intercept-only model.
   - Its ridge penalty differs (178 vs 56). The "minus intercept" readings may be slightly off.
8. **[does not affect a conclusion] Metadata inconsistencies.** The notebook reports all of these and works around them correctly:
   - The imaging plane says GCaMP6f while the paper and keywords say GCaMP6s.
   - The raw file states an imaging rate of 15 Hz; the timestamps give 31.2 Hz.
   - The wheel description says counter-clockwise is positive, but counter-clockwise choices turn with negative velocity. Choice labels were validated against rewards (cell 5) and used as given.
   - The dandiset text says CNTNALP2.
9. **[does not affect a conclusion] Assumptions never checked.**
   - The three ROI motion energies are assumed to be the whisker pads and body (cell 10).
   - The action-kernel form of the subjective prior is assumed (`fit_action_kernel`).

**Helper tests on synthetic data:**
- `_ridge_fold` matches closed-form ridge to 1e-14, and its GCV-chosen penalty matches a brute-force GCV.
- The per-pixel R² in `fit_model` matches an explicit pixel-space computation.
- `folds` gives equal folds balanced per time point.
- `fit_psychometric` recovers its generating parameters to within sampling error.
- `bin_to_frames` and `frame_index` behave correctly.

### C. What I could not check

- **The paper's full text** was unavailable here because bioRxiv rate-limited the host. I could not verify against the paper:
  - the RT definition and the Figure 1E values;
  - the encoding-model windows, the movement regressors and cameras used, and whether cvR2 is computed over masked or atlas-aligned pixels;
  - the Figure 3B analysis window.
- **Outputs that would have let me check more:**
  - RT histograms, plus the contrast correlation using response time (choice registration minus stimulus onset). This would show whether fig1e fails only because of anticipatory onsets.
  - An evoked map and peak test with a brain mask fixed in advance, restricted to trials with RT > 0.4 s, and a time course aligned to movement onset. This would separate a visual from a motor lateralization for fig3b.
  - cvR2 with folds grouped by trial and duplicate frames removed. This would show how large the leakage in B5 is.
  - The distribution of per-target ridge penalties, including the fraction at the grid edges.
  - Bootstrap confidence intervals for A, B and tau in fig2ef.
  - The fig4c/d readings with the left and right camera video components included, to test whether the reduced movement set explains the low movement ΔR².

## End of run

18 turns, 4 minutes, result: success.
