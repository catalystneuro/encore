# memar-2026 · verifier-1 · run 44915955230

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 192
drwxr-xr-x 6 runner runner   4096 Nov 21 17:24 .
drwxr-xr-x 8 runner runner   4096 Nov 21 17:24 ..
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 14:47 .bash_profile
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 14:47 .bashrc
drwxr-xr-x 5 runner runner   4096 Nov 21 17:24 .claude
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .env
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .env.development
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .env.development.local
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .env.local
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .env.production
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .env.production.local
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .env.test
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .env.test.local
drwx------ 2 runner runner   4096 Nov 21 17:24 .git
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 14:47 .gitconfig
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 14:47 .github
-rw-r--r-- 1 runner runner      0 Nov 21 17:24 .gitmodules
crw-rw-rw- 1 nobody nogroup  1, 3 Nov 21 14:47 .idea
[... 40 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "memar-2026.yaml"
}
```

```
1	# Claims for Ostadsharif Memar & Dehghani (2026), "Spatially Masked Regression Reveals Local and
2	# Distributed Predictability in Electrophysiological Recordings", doi:10.48550/arxiv.2606.11415.
3	#
4	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-21, protocol as stated in docs/protocol.md (pilot-18), Reader role.
6	#
7	# Text read. The arXiv preprint, version 1 (arXiv:2606.11415v1, dated 11 June 2026), full text as
8	# stored under paper/ (paper/10.48550-arxiv.2606.11415.txt, "Version: preprint"): main text,
9	# Material and Methods (sections II A to II H, Algorithms 1 to 4), Results, Discussion, and the
10	# appendix Tables II (iEEG) and III (EEG) and Figure 6. The paper has no separate supplement and
11	# cites none. No version of record was available. The PDF was not needed; the table values were
12	# read from the text, row by row in the column order the headers give.
13	#
14	# Code read. GitHub neurovium/SpatiallyMaskedRegression (linked in the paper's footnote and Code
15	# Availability), commit 244dcdbd67f217873c2a52b77485d97c6fa9bf0e (2026-06-24, after the preprint's
16	# date). It holds the model (ReconModel.py, model.py), intra-subject training and the EEG
17	# cross-subject path (train.py, main.py), the iEEG cross-subject path (similarity.py,
18	# generate_adj_matrix_ieeg_unseen.py, Test_new_subject_iEEG.py), the coverage experiment
19	# (run_coverage_experiment.py), surrogates (Load_preprocess_data.py), the neighborhood and mask
20	# (neighborhood.py), settings (configs/settings.yaml), a METHODS.md map from the paper to the code,
[... 517 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    print(f"\n===== CELL {i} [{c['cell_type']}] =====")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- out:'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--- out:'); print(''.join(d['text/plain']))
            else: print('--- out keys', list(d))
        elif o.get('output_type')=='error': print('--- ERROR', o['ename'], o['evalue'])
EOF
python3 $TMPDIR/dump.py reproduce_memar_2026.ipynb
```

```
<persisted-output>
Output too large (43.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/300857d0-5d15-4e8d-b0a7-3ff798a5672d/tool-results/b2gobzgpo.txt

Preview (first 2KB):
===== CELL 0 [markdown] =====
# Spatially Masked Regression on AJILE12: intra-subject, cross-subject, masking and coverage

Ostadsharif Memar & Dehghani (2026), "Spatially Masked Regression Reveals Local and Distributed
Predictability in Electrophysiological Recordings", arXiv:2606.11415 (doi:10.48550/arxiv.2606.11415).
The claims file `claims/memar-2026.yaml` was written from the arXiv preprint, version 1, and its
code at commit 244dcdbd of github.com/neurovium/SpatiallyMaskedRegression.

Dataset: DANDI:000055 (AJILE12), version 0.220127.0436 (doi:10.48324/dandi.000055/0.220127.0436).
Why this version: the paper cites the dataset (Peterson et al. 2022) but no version of it. 0.220127.0436
is the only published version and the most recent; the draft (modified 2026-02-12) has the same
55 assets and size, and a draft can change. The files are streamed; nothing is written to disk.

This notebook tests the intra-subject and cross-subject claims. `masking_coverage.ipynb` tests the
mask sweep and the electrode coverage, and `surrogates_lagged.ipynb` the surrogate, lagged and
full-mask claims; each loads the data again. The EEG claims rest on a dataset the paper names without
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/300857d0-5d15-4e8d-b0a7-3ff798a5672d/tool-results/b2gobzgpo.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Spatially Masked Regression on AJILE12: intra-subject, cross-subject, masking and coverage
4	
5	Ostadsharif Memar & Dehghani (2026), "Spatially Masked Regression Reveals Local and Distributed
6	Predictability in Electrophysiological Recordings", arXiv:2606.11415 (doi:10.48550/arxiv.2606.11415).
7	The claims file `claims/memar-2026.yaml` was written from the arXiv preprint, version 1, and its
8	code at commit 244dcdbd of github.com/neurovium/SpatiallyMaskedRegression.
9	
10	Dataset: DANDI:000055 (AJILE12), version 0.220127.0436 (doi:10.48324/dandi.000055/0.220127.0436).
11	Why this version: the paper cites the dataset (Peterson et al. 2022) but no version of it. 0.220127.0436
12	is the only published version and the most recent; the draft (modified 2026-02-12) has the same
13	55 assets and size, and a draft can change. The files are streamed; nothing is written to disk.
14	
15	This notebook tests the intra-subject and cross-subject claims. `masking_coverage.ipynb` tests the
16	mask sweep and the electrode coverage, and `surrogates_lagged.ipynb` the surrogate, lagged and
17	full-mask claims; each loads the data again. The EEG claims rest on a dataset the paper names without
18	an accession (BNCI Horizon 2020, Ofner et al. 2017) that is not in DANDI:000055 and is not tested.
19	
20	| Claim | Here |
[... 653 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py masking_coverage.ipynb; python3 $TMPDIR/dump.py surrogates_lagged.ipynb
```

```
===== CELL 0 [markdown] =====
# Spatially Masked Regression on AJILE12: mask sweep and electrode coverage

Ostadsharif Memar & Dehghani (2026), arXiv:2606.11415, on DANDI:000055 version 0.220127.0436
(the only published version; see `reproduce_memar_2026.ipynb` for the header, the version choice
and the full data check). Claims tested here: fig4a-mask-sweep-ieeg and fig5a-coverage-ieeg.
Settings and deviations as in `reproduce_memar_2026.ipynb` (every 10th sample for the gradient
steps, 200 epochs).

===== CELL 1 [code] =====
import os, time, zlib, json, resource
import numpy as np
import pandas as pd
from scipy import stats
import smr

T0 = time.time()
PAPER = "memar-2026"
def seed(claim):
    return zlib.crc32(f"{PAPER}/{claim}".encode())
[... 499 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "smr.py"
}
```

```
1	"""Loading and measures for testing Ostadsharif Memar & Dehghani (2026), "Spatially Masked
2	Regression", on AJILE12 (DANDI:000055).
3	
4	Where each parameter comes from:
5	
6	- Trials. 2 s windows centred on the start of each wrist movement event of the `reaches` table
7	  (the same times as processing/behavior/ReachEvents), every session of a subject pooled. Claims
8	  file, opening comment, "Which movement events", reading (a), and "Which recording days".
9	- Preprocessing. The steps and their order are the paper's (Methods II A a): DC removal and linear
10	  detrending, 0.5 to 150 Hz Butterworth band-pass, 60 Hz notch, 120 Hz low-pass, |z| > 5 replaced
11	  by the channel median, common average reference, per-channel z-scoring across time. Filter
12	  orders (4th-order Butterworth, zero phase with filtfilt; notch Q = 30) are the paper's code
13	  (utils.preprocess_iEEG), which the claims file read. The code's median filter and Hilbert
14	  envelope are left out, as the claims file says.
15	  Where preprocessing is applied is open (claims file, readings a and b):
16	  (a) `continuous`: the paper's order (preprocess, then segment). The whole recording is 16 GB a
17	      file, so each event is read with 5 s of padding on each side, filtered, and cut to its
18	      centre; the statistics of the |z| > 5 step and of the z-scoring are taken over all the
19	      event windows of the session, standing in for the whole recording. An approximation of
20	      reading (a), stated as such.
[... 605 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; grep -n -i -E "dcor|distance cov|dCov|sqrt|end-match|end match|Non-local|nonlocal|non-local|rest|AAL|ceil|surrogate" *.txt | head -80
```

```
1962 10.48550-arxiv.2606.11415.txt
grep: 10.48550-arxiv.2606.11415.txt: binary file matches
```

**Agent calls Bash**

```bash
cd paper; grep -a -n -i -E "dcor|distance cov|dCov|sqrt|end-match|end match|non-local|nonlocal|rest |AAL|surrogate|Eq|\(1[0-4]\)" *.txt | head -100
```

```
27:channels reflect both local redundancy and broader distributed structure. Surrogates that preserve selected marginal or
66:tice, these dependencies are frequently estimated from elec-
84:and frequency-dependent attenuation, causing fast compo-
95:for how we interpret these signals16. Consequently, pairwise
113:“how much of this signal is contained in the rest of the array,
122:be predicted from the rest of the array? This viewpoint res-
136:(SMR) model that explicitly separates local from nonlocal
192:low-pass for residual high-frequency noise, |z| > 5 artifact
212:were band-pass filtered, notch-filtered at line frequency, and
231:Non-local Electrode
237:and the regression step estimates the target from the remaining nonlocal channels. Varying the mask size provides a controlled way to compare
250:Number of nearest electrodes
291:of k = 9 electrodes whose recording sites are nearest to elec-
340:can rely only on nonlocal predictors. Comparing performance
411:constraint are equivalent ways of enforcing local exclusion;
423:Require: Signals X(s) ∈RNs×T, neighborhood mask K(s) ∈
492:subsequent evaluation on the held-out test set.
507:[j,i] need not be equal. Recon-
511:subsequently used in the cross-subject analyses. Model pa-
519:Require: Target subject signals X(s), reference subjects
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 180,215p *.txt; echo ----; sed -n 820,1030p *.txt; echo ----; sed -n 1170,1200p *.txt; sed -n 1265,1280p *.txt; sed -n 1745,1760p *.txt
```

```
(5 right, 7 left), and electrode locations varied significantly
across subjects.
Fig. 6 shows the electrode configurations
and the distribution of implanted brain regions across sub-
jects. During this period, subjects engaged in routine hos-
pital activities such as eating, watching TV, and socializing.
Simultaneously, video recordings were used to identify in-
stances of upper-limb movement, which served as behavioral
annotations aligned with the neural data.
The neural data
were preprocessed (DC removal and linear detrending, 0.5–
150 Hz Butterworth band-pass, 60 Hz notch filtering, a 120 Hz
low-pass for residual high-frequency noise, |z| > 5 artifact
rejection by per-channel replacement with the channel me-
dian, Common Average Reference, and per-channel z-scoring
across time), and were segmented into 2-second trials centered
on movement events.
b.
Upper Limb Movements EEG25: This EEG dataset
was recorded to investigate both motor execution and mo-
[... 292 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 280,300p *.txt; grep -a -n -E "x, ?z|\(x|y\)|projection|plane" *.txt | head; python3 -c "import dcor, numpy; print(dcor.__version__)"
```

```
Exit code 1
because field recordings are spatially mixed due to volume
conduction. If all predictors are allowed, a linear model will
typically assign large weights to nearby channels and com-
paratively small weights to more distant ones. Such a model
is useful for reconstruction, but it is poorly suited for asking
how much predictive structure remains once the dominant lo-
cal contribution is removed thus limiting its effectiveness for
uncovering broader spatial dependencies..
We therefore define, for each electrode i of subject s, a
neighborhood set N (s)(i) containing the channels spatially
closest to the target. For both modalities, N (s)(i) is the set
of k = 9 electrodes whose recording sites are nearest to elec-
trode i under a fixed projected Euclidean distance: for EEG
we use the in-plane distance in the (x,y) coordinates of the
standardized scalp montage, while for iEEG we use the (x,z)
projection of the MNI electrode coordinates (the electrode it-
self, at distance zero, is excluded). This coordinate-based con-
struction yields a neighborhood of fixed size across electrodes
and avoids relying on either a standardized montage labeling
[... 11 more lines not kept]
```

**Agent**

Progress: I've read all three notebooks, `smr.py`, the claims file and the relevant Methods text. Next I'm testing the helpers on synthetic data.

**Agent calls Bash**

```bash
cd  python3 -c "
import importlib
for m in ['numpy','scipy','sklearn','h5py','remfile','requests','dcor','pandas']:
    try: importlib.import_module(m); print(m,'ok')
    except Exception as e: print(m,'MISSING')
"
```

```
numpy MISSING
scipy MISSING
sklearn MISSING
h5py MISSING
remfile MISSING
requests MISSING
dcor MISSING
pandas MISSING
```

**Agent calls Bash**

```bash
cd $TMPDIR && (uv --version; pip --version; python3 --version) 2>&1; timeout 120 pip install --target $TMPDIR/py numpy scipy scikit-learn dcor 2>&1 | tail -2
```

```
uv 0.13.9 (x86_64-unknown-linux-gnu)
pip 26.3 from /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/pip (python 3.13)
Python 3.13.18

Successfully installed array-api-compat-1.16.0 cloudpickle-3.1.3 dcor-0.7 joblib-1.6.0 llvmlite-0.50.0 narwhals-2.29.0 numba-0.68.1 numpy-2.5.5 scikit-learn-1.9.1 scipy-1.18.1 threadpoolctl-3.8.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
timeout 120 pip install --target $TMPDIR/py h5py remfile requests 2>&1 | tail -1
cd  cat > $TMPDIR/t.py <<'EOF'
import sys; sys.path.insert(0, sys.argv[1]); sys.path.insert(0,'.')
import numpy as np, math, smr, dcor
rng=np.random.default_rng(0)
# 1 dcor vs paper Eqs 8-14
def dc_paper(u,v):
    a=np.abs(u[:,None]-u[None]); b=np.abs(v[:,None]-v[None])
    A=a-a.mean(0)-a.mean(1)[:,None]+a.mean(); B=b-b.mean(0)-b.mean(1)[:,None]+b.mean()
    return np.sqrt((A*B).mean())/np.sqrt(np.sqrt((A*A).mean()*(B*B).mean()))
u=rng.normal(size=(3,300)); v=u+rng.normal(size=(3,300))
print("dcor", smr.dcor_rows(u,v), [dc_paper(u[i],v[i]) for i in range(3)])
# 2 mask counts
nbr=smr.neighbours(rng.normal(size=(30,3)))
for m in (0,.25,.5,.75,1):
    A=smr.mask_matrix(nbr,m,rng); print(m,"ceil masked nbrs", 9-np.mean([A[i,nbr[i]].sum() for i in range(30)]), "self", A.diagonal().any(),
      "round", 9-np.mean([smr.mask_matrix(nbr,m,rng,rule='round')[i,nbr[i]].sum() for i in range(30)]))
L=smr.mask_matrix(nbr,0,rng,mode='local'); print("local fan", L.sum(1)[:3], "self", L.diagonal().any())
# 3 fit recovers known linear map
n,T,R=12,200,300
X=rng.normal(size=(R,n,T)).astype(np.float32)
Wt=rng.normal(size=(n,n))*0.3; np.fill_diagonal(Wt,0)
Y=np.einsum('ij,rjt->rit',Wt,X)
X[:, :6]=Y[:, :6]+0.1*rng.normal(size=(R,6,T))
xz=smr.zscore_trials(X); tr,va,te=smr.split_64_16_20(R)
allow=np.ones((n,n),bool); np.fill_diagonal(allow,False)
W,b,be,ne=smr.fit_smr(xz,tr,va,allow,rng,max_epoch=300,decim=5)
pred=smr.predict(xz[te],W,b)
print("fit: dc first 6 targets", smr.score(xz[te],pred,np.arange(len(te)))[:6].round(3), "epochs",ne)
# compare with lstsq
Xtr=xz[tr].transpose(0,2,1).reshape(-1,n)
for i in range(3):
    idx=np.where(allow[i])[0]; w=np.linalg.lstsq(Xtr[:,idx],Xtr[:,i],rcond=None)[0]
    print(" target",i,"max |W-lstsq|", np.abs(W[i,idx]-w).max().round(3))
# 4 lag features
x=np.arange(2*1*40,dtype=np.float32).reshape(2,1,40)
f=smr.features(x,True); print("lags",smr.lag_samples(), f[0,:12].T)
# 5 surrogates
s=rng.normal(size=(4,3,1000)).cumsum(-1)
for k in ("phase","iaaft","block"):
    z=smr.surrogate(s,k,rng)
    amp_err=np.abs(np.abs(np.fft.fft(z,axis=-1))-np.abs(np.fft.fft(s,axis=-1))).max()/np.abs(np.fft.fft(s,axis=-1)).max()
    print(k,"rel amp spec err",round(amp_err,4),"sorted equal",np.allclose(np.sort(z,-1),np.sort(s,-1)),"mean equal",np.allclose(z.mean(-1),s.mean(-1),atol=1e-4))
# 6 transfer with permuted identical subject
P=rng.permutation(n); Ma=rng.normal(size=(n,n))
C=np.corrcoef(np.vstack([X[:,:, :].transpose(1,0,2).reshape(n,-1), X[:,P].transpose(1,0,2).reshape(n,-1)]))[:n,n:]
Me,mt=smr.transfer(C,Ma[np.ix_(P,P)])
print("transfer recovers M:", np.allclose(Me,Ma), mt.all())
EOF
python3 $TMPDIR/t.py $TMPDIR/py
```

```
WARNING: Target directory /tmp/claude-1001/py/bin already exists. Specify --upgrade to force replacement.
dcor [0.65202324 0.63123108 0.61942819] [np.float64(0.6520232369975117), np.float64(0.6312310773406091), np.float64(0.6194281870871047)]
0 ceil masked nbrs 0.0 self False round 0.0
0.25 ceil masked nbrs 3.0 self False round 2.0
0.5 ceil masked nbrs 5.0 self False round 4.0
0.75 ceil masked nbrs 7.0 self False round 7.0
1 ceil masked nbrs 9.0 self False round 9.0
local fan [9 9 9] self False
fit: dc first 6 targets [0.899 0.808 0.849 0.881 0.969 0.973] epochs 300
 target 0 max |W-lstsq| 0.021
 target 1 max |W-lstsq| 0.119
 target 2 max |W-lstsq| 0.019
lags [0, 10, 15, 25, 30] [[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]]
phase rel amp spec err 0.0 sorted equal False mean equal True
iaaft rel amp spec err 0.0099 sorted equal True mean equal True
block rel amp spec err 0.1224 sorted equal True mean equal True
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; PYTHONPATH=$TMPDIR/py python3 - <<'EOF'
import requests, collections
API="https://api.dandiarchive.org/api"
v=requests.get(f"{API}/dandisets/000055/versions/0.220127.0436/info/",timeout=60).json()
md=v["metadata"]
print(v.get("asset_count"), v.get("size"))
print("measurementTechnique", [m.get("name") for m in md.get("assetsSummary",{}).get("measurementTechnique",[])])
print("variableMeasured", md.get("assetsSummary",{}).get("variableMeasured"))
print("approach", [a.get("name") for a in md.get("assetsSummary",{}).get("approach",[])])
print(md.get("description","")[:600])
out=[];url=f"{API}/dandisets/000055/versions/0.220127.0436/assets/?page_size=200"
while url:
    r=requests.get(url,timeout=60).json(); out+=r["results"]; url=r["next"]
print(len(out), collections.Counter(a["path"].split("_")[-1] for a in out))
print([a["path"] for a in out if not a["path"].endswith("ecephys.nwb")])
EOF
```

```
55 845869698341
measurementTechnique ['behavioral technique', 'multi electrode extracellular electrophysiology recording technique', 'analytical technique', 'surgical technique']
variableMeasured ['Position', 'ProcessingModule', 'ElectricalSeries', 'ElectrodeGroup']
approach ['behavioral approach', 'electrophysiological approach']
Understanding the neural basis of human movement in naturalistic scenarios is critical for expanding neuroscience research beyond constrained laboratory paradigms. The neural correlates of unstructured, spontaneous movements in completely naturalistic settings have rarely been studied, due in large part to a lack of available data. Here, we present our Annotated Joints in Long-term Electrocorticography for 12 human participants (AJILE12) dataset, the largest human neurobehavioral dataset that is publicly available; the dataset was recorded opportunistically during passive clinical epilepsy mon
55 Counter({'behavior+ecephys.nwb': 55})
[]
Shell cwd was reset to
```

**Agent**

**A. Outcomes** (20 claims in the claims file: 11 iEEG claims tested, 9 EEG claims blocked)

| Claim | My outcome | Reason |
|---|---|---|
| intra-ieeg-mean | reproduced | Reading a gives 0.602 ± 0.058 and reading b gives 0.570 ± 0.066. Both fall inside 0.553 ± 0.068 (main nb cell 11), and five seeds give 0.598 to 0.602 (cell 13). Reading a sits near the upper edge (0.621). The m = 0 variant would be 0.712, which is outside (masking nb cell 6). |
| table2-ieeg-intra-subjects | partially_reproduced | 8 of 12 subjects are within tolerance under preprocessing reading b and 4 of 12 under reading a (cell 15). Spearman ρ is 0.78 and 0.71. The outcome depends on reading b. |
| cross-ieeg-mean | reproduced | The mean is 0.340 to 0.351 under all four readings (C from all or val trials, paired or concatenated), inside 0.389 ± 0.064 (cell 17). The SD across subjects (about 0.106) is larger than the paper's 0.064, and sub-12 (0.647) is an outlier. |
| table2-ieeg-cross-subjects | not_reproduced | 0 of 12 subjects are within tolerance under every reading, and Spearman ρ is 0.14 to 0.28 (cell 19). |
| cross-below-intra-ieeg | reproduced | Under every reading the cross average (0.34 to 0.35) is below intra (0.602), and cross-ieeg-mean is reproduced. 11 or 12 of 12 subjects have cross below intra (cell 21). |
| fig4a-mask-sweep-ieeg | reproduced | The average falls at every step: 0.712, 0.673, 0.650, 0.628, 0.602. All 12 subjects fall at every step, and the result holds with the round rule (masking nb cells 6, 8). |
| full-mask-above-zero-ieeg | reproduced | Reading b: the m = 1.0 average of 0.602 is above the phase-shuffle average of 0.201, in 12 of 12 subjects. Reading a also holds, with the smallest electrode at 0.226 (surrogates nb cell 12). |
| fig5a-coverage-ieeg | not_reproduced | All 0.712 > Non-local 0.602 > Local 0.567, so the required order All > Local > Non-local fails. Local beats Non-local in only 2 of 12 subjects (masking nb cell 10). Only one reading of the open trial details was run (problems 1 and 2). |
| lagged-ieeg-no-gain | reproduced | Lagged 0.603 against instantaneous 0.602. That is within 0.554 ± 0.067, and the difference is +0.3%, under the 10% bound (surrogates nb cell 14). |
| surrogate-ieeg | reproduced | Phase 0.201 (tolerance 0.181 ± 0.029), IAAFT 0.184 (0.232 ± 0.060) and block 0.229 (0.201 ± 0.168) are all within tolerance and all below the original (cell 8). Only reading a (no end matching) was run. |
| surrogate-order-ieeg | not_reproduced | IAAFT (0.184) is lowest, not phase (0.201). Phase is lowest in 0 of 12 subjects, and reading b's order also fails (cell 10). Only the surrogate reading without end matching was run (problem 3). |
| intra-eeg-mean | blocked (data_missing) | The EEG data are not in DANDI:000055 (see section C). |
| intra-eeg-above-ieeg | blocked (data_missing) | Needs the EEG values. The iEEG half (0.602 or 0.570) is available. |
| cross-eeg-mean | blocked (data_missing) | EEG not in the dataset. |
| transfer-penalty-larger-ieeg | blocked (data_missing) | Needs the EEG values. The iEEG half could have been computed but was not reported: ratio about 0.58, difference about 0.25 (0.35 / 0.602). |
| lagged-eeg-no-gain | blocked (data_missing) | EEG not in the dataset. |
| fig4b-mask-sweep-eeg | blocked (data_missing) | EEG not in the dataset. |
| fig5b-coverage-eeg | blocked (data_missing) | EEG not in the dataset. |
| surrogate-eeg | blocked (data_missing) | EEG not in the dataset. |
| surrogate-order-eeg | blocked (data_missing) | EEG not in the dataset. |

**Archive check for the blocked claims.** I queried the API for the version info and asset list of 000055 at 0.220127.0436. It has 55 assets, all `sub-XX_ses-N_behavior+ecephys.nwb` for 12 subjects. The measurement technique is extracellular electrophysiology and the measured variables are ElectricalSeries and Position. There is no scalp EEG. No EEG claim can be tested here. For intra-eeg-above-ieeg and transfer-penalty-larger-ieeg, only the iEEG side can be computed.

**B. Problems**

1. [affects a conclusion] Movement-event reading (b), movement plus rest trials, is never run and never mentioned as skipped. `smr.load_session` uses only `intervals/reaches`. The files hold `intervals/epochs` with labels (1427 rows in sub-01 ses-3, cell 3), so the reading was probably feasible. The claims file requires every reading. Under the "one reading" rule, the not_reproduced outcomes (table2-ieeg-cross-subjects, fig5a-coverage-ieeg, surrogate-order-ieeg) and the partial one (table2-ieeg-intra-subjects) are therefore provisional.
2. [affects a conclusion] Preprocessing reading (b), epoch-wise, is run only for intra-ieeg-mean and table2-ieeg-intra-subjects (main cell 10). It is not run for:
   - cross-subject (cell 17; donors are reading-a weights only)
   - the mask sweep and coverage (masking nb cells 6, 10)
   - surrogates and lagged (surrogates nb cells 6, 8, 14)

   Reading b moved table2-intra from 4/12 to 8/12, so it can matter. fig5a, surrogate-order-ieeg and table2-cross were judged on reading a only.
3. [affects a conclusion] Surrogate reading (b), end-matched segmentation, is not run (surrogates nb cell 7). The stated reason, unequal lengths, is weak. Algorithm 4 shuffles each channel independently, so the time alignment across channels is already destroyed. The usual end-matching practice is to pick one fixed-length sub-segment per series, or one common length per trial, which gives equal-length trials. End matching removes the wrap-around discontinuity that phase randomisation creates. It could lower the phase-shuffle value (0.201) below IAAFT (0.184), and that is the comparison surrogate-order-ieeg turns on.
4. [does not affect a conclusion] The speed deviations (every 10th sample, 200 epochs) were checked on one subject, at m = 1.0 with the instantaneous model only (surrogates nb cell 16, difference 0.0003). The following were not checked:
   - the lagged model, with 5× the parameters
   - the Local model
   - surrogate fits

   With 200 epochs, an undertrained lagged model could understate a gain. A gain would have to exceed 10% to change the outcome, so the effect is unlikely to matter.
5. [does not affect a conclusion] In four files the `reaches` table and `ReachEvents` disagree by 8 to 24 h for some events (cell 3: sub-01 ses-7, sub-04 ses-3, sub-06 ses-3, sub-08 ses-4). The notebook drops only the events past the recording end and keeps the rest of the `reaches` times from those files without checking which table is right. If those times are wrong, trials are mislocated. The claims do not depend on movement locking, so the effect is likely small.
6. [does not affect a conclusion] `load_session` reads ElectricalSeries `starting_time` but never checks that it is 0 before computing `i0 = round(t·FS)`. The clock check (cell 8) supports alignment in 10 of 12 subjects. It shows no event-locked high-gamma change in sub-02 (|t| = 2.65 against a null 95th percentile of 3.30) or sub-09 (3.09 against 3.42), and the notebook does not discuss these.
7. [does not affect a conclusion] Overlapping 2 s windows from closely spaced reaches can put the same samples in both train and test (`split_64_16_20`), and in both the val and test halves in `cross_subject`. The trials are also z-scored across trials before the split (`zscore_trials`). This follows the paper's code, but the overlap was never quantified.
8. [does not affect a conclusion] Reading (b) trials are stored as float16 (`load_subject`), which loses precision before fitting. The effect on DistCorr is negligible.
9. [does not affect a conclusion] Electrodes without coordinates are dropped (16 in sub-03, 8 in sub-12; `drop_uncoordinated`). This is stated as the attempt's own choice, and it is reasonable.
10. [does not affect a conclusion] intra-ieeg-mean asks for its variants to be reported. The m = 0 variant (0.712, outside tolerance) appears only in the masking notebook and not in the intra-ieeg-mean section. The round variant is identical to ceil at m = 1.0. The atlas variant cannot be run: every `location` is "unknown" (cell 3), and I agree with that.
11. [does not affect a conclusion] The notebook's SD across electrodes (0.07 to 0.15, cell 11) is about 3× the paper's (0.02 to 0.04). That is a sign the pipelines differ, and the notebook does not discuss it.

**Helper tests on synthetic inputs** all passed:
- `dcor_rows` matches Eqs. 8 to 14 exactly.
- `mask_matrix` masks 0, 3, 5, 7 and 9 neighbours with ceil and 0, 2, 4, 7 and 9 with round, never lets the target predict itself, and Local has fan-in 9.
- `fit_smr` recovers a planted linear map (DistCorr 0.8 to 0.97).
- `features` gives lag offsets of 0, 10, 15, 25 and 30 samples, with zero padding.
- `surrogate`: phase keeps the amplitude spectrum exactly; IAAFT keeps the exact value distribution with about a 1% spectrum error; block keeps the values.
- `transfer` recovers M from a permuted copy of the same subject.

The claims file's reading of the paper (the (x, z) neighbourhood, Eq. 14 as unsquared dCor, the Local/Non-local definitions, the Table II legend) matches the text. I found no misreading.

**C. What I could not check, and the output that would have let me**

- Whether rest trials are available for event reading (b). The `intervals/epochs` label counts per file, and a run under that reading.
- Reading (b) results for cross-subject, the mask sweep, coverage, surrogates and lagged.
- End-matched phase surrogates. Their values per subject.
- Which event table is right in the four mismatched files. A per-event comparison of `reaches` and `ReachEvents` times in those files, and the ElectricalSeries `starting_time` for every file.
- The amount of train/test overlap. The fraction of trials per subject whose window overlaps another trial.
- Convergence of the lagged, Local and surrogate fits. Epochs run and median best epoch for those runs, as cell 11 gives for the instantaneous run.
- Cross-subject spread within a subject. The SD across electrodes for each subject, to compare with the paper's 0.004 to 0.016.
- Subject order against Figure 6. The text gives only the totals (5 right, 7 left), and those match the data's x signs. A per-subject electrode plot would allow the comparison.
- The iEEG half of intra-eeg-above-ieeg and transfer-penalty-larger-ieeg. The intra/cross ratio and difference, printed.

## End of run

15 turns, 4 minutes, $1.28 at API prices, result: success.
