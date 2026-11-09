# 001357 · verifier-1 · run 41414423834

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; find . -maxdepth 2 -type f | head -50
```

```
total 352
drwxr-xr-x 6 runner runner    4096 Nov  2 08:46 .
drwxr-xr-x 7 runner runner    4096 Nov  2 08:46 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:37 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:37 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  2 08:46 .claude
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .env
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .env.development
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .env.local
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .env.production
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .env.test
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .env.test.local
drwx------ 2 runner runner    4096 Nov  2 08:46 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:37 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:37 .github
-rw-r--r-- 1 runner runner       0 Nov  2 08:46 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:37 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:37 .mcp.json
[... 56 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1523-jneurosci.1893-23.2024.yaml"
}
```

```
1	# Claims for Namima, Kempkes, Zamarashkina, Owen & Pasupathy (2025), "High-Density Recording
2	# Reveals Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4",
3	# J Neurosci 45(5) e1893232024, on dandiset 001357.
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
5	# pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF), with
8	# the main text, Materials and Methods, and figure legends. The paper has no supplement. The PDF
9	# was not opened; the text was enough.
10	#
11	# Code: the paper links no analysis code and gives no code or data availability statement. The
12	# only software it names for the experiments is the stimulus software, "Pype2; Mazer, 2013", with
13	# no link; the first reader read pype3 (github.com/mazerj/pype3, HEAD at
14	# 49056d6f7e02bb217b2f044dba6ec7a33173b4ca on 2026-10-21), a later version. It
15	# runs the stimuli and the fixation task and holds none of the analyses, so it settles no method
16	# detail here. The analyses were written in MATLAB (fit.m, confint.m, conv2.m, the cortex-lab
17	# Spikes toolbox) by the authors and are not public. The noise-corrected correlation follows
18	# Pospisil and Bair (2021, J Neurosci 41 5638), which the paper cites and does not link; its method
19	# is taken from this paper's Methods alone.
20	#
[... 857 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_namima_2025.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1575 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	58
2	==================== 0 markdown
3	# Reproducing Namima et al. (2025) from dandiset 001357
4	
5	**Paper.** Namima, Kempkes, Zamarashkina, Owen and Pasupathy (2025), "High-Density Recording Reveals
6	Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4", J Neurosci 45(5)
7	e1893232024, doi:10.1523/jneurosci.1893-23.2024.
8	
9	**Dataset.** DANDI:001357, version 0.261006.2007 (doi:10.48324/dandi.001357/0.261006.2007), streamed
10	from the archive. The paper cites no version of the dataset. This is the only published version,
11	and so the most recent; the draft has the same 159 assets and size, and a draft can change, so the
12	published version is pinned.
13	
14	**Claims.** `claims/001357/10.1523-jneurosci.1893-23.2024.yaml`, written by a reader from the version
15	of record (main text, Methods and figure legends; the paper has no supplement) and checked by a
16	second reader.
17	
18	| Claim | Tested here |
19	|---|---|
20	| methods-sessions-and-neurons | tested |
[... 739 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 760,
 "limit": 820
}
```

```
760	    for mk in ("M1", "M2"):
761	        s_ = ok & (N.monkey == mk)
762	        print(f"    {mk}: Spearman r = {stats.spearmanr(x[s_], y[s_])[0]:.3f}, n = {int(s_.sum())}")
763	--OUT--
764	reliability a: Spearman r = 0.484, p = 2.9e-97, n = 1643; within 0.435 +/- 0.0435: False
765	    M1: Spearman r = 0.463, n = 840
766	    M2: Spearman r = 0.500, n = 803
767	reliability b: Spearman r = 0.520, p = 2.6e-122, n = 1757; within 0.435 +/- 0.0435: False
768	    M1: Spearman r = 0.506, n = 918
769	    M2: Spearman r = 0.532, n = 839
770	
771	==================== 32 markdown
772	## pop-contrast-invariance
773	
774	> More than half of the neurons are well driven and contrast invariant, with a median correlation
775	> between dark and bright responses of 0.64.
776	==================== 33 code
777	rows = []
778	for rd in "ab":
779	    rel = N[f"inv_rel_{rd}"]
[... 797 more lines not kept]
```

**Agent**

Notebook read. Next, the helper module.

**Agent calls Read**

```json
{
 "file_path": "v4clusters.py"
}
```

```
1	"""Loading and measures for dandiset 001357 (Namima et al. 2025, J Neurosci 45 e1893232024).
2	
3	Where each parameter comes from:
4	
5	- DANDISET and VERSION: the most recent published version, the only one (the paper cites none).
6	- WINDOW = (0.030, 0.200) s after the photodiode onset (`pdOnTS`): Materials and Methods, Data
7	  analysis, Firing rate computation ("computed within a 30-200 ms window after stimulus onset");
8	  photodiode onset from Experimental design ("Stimulus onset times were based on photodiode
9	  detection").
10	- Baseline: the same window on blank presentations (`cond_ID` 0), same passage ("Baseline FRs were
11	  similarly computed during blank stimulus presentations").
12	- RESPONSIVE_RATE = 5 spikes/s above baseline for one stimulus at either contrast: Materials and
13	  Methods, Dataset and data inclusion criteria, paragraph 2.
14	- Dark and bright shapes are `luminance` 4 and 12 cd/m2 (Visual stimuli: "darker or brighter than
15	  the background luminance (4 or 12 cd/m2)"). The files also hold `luminance` 8, which the paper
16	  does not use; it is left out.
17	- Texture versions: `mode` 0 original, 1 contrast-reversed, 2 spectral noise (the column's own
18	  description); mode 2 is not used in the paper and is left out.
19	- Depth: the files give `depth`, "distance from the electrode tip", in 20 um steps (the position of
20	  the unit's best channel), not the template center of mass of the Methods (Depth from the most
[... 396 more lines not kept]
```

**Agent**

The notebook and helper have been read. Now I'll check the archive for the blocked claims and test the helper functions on synthetic data.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import requests, json, collections
API="https://api.dandiarchive.org/api"
v=requests.get(f"{API}/dandisets/001357/versions/0.261006.2007/",timeout=60).json()
print(json.dumps(v.get("assetsSummary"),indent=0)[:1500])
print(v.get("description"))
url=f"{API}/dandisets/001357/versions/0.261006.2007/assets/?page_size=500"
rows=[]
while url:
    p=requests.get(url,timeout=60).json(); rows+=p["results"]; url=p.get("next")
print(len(rows))
print(collections.Counter(r["path"].split("_")[-1] for r in rows))
print([r["path"] for r in rows][:5])
print(sum(r["size"] for r in rows)/1e9,"GB")
a=rows[0]
m=requests.get(f"{API}/dandisets/001357/versions/0.261006.2007/assets/{a['asset_id']}/",timeout=60).json()
print(json.dumps(m,indent=1)[:5000])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import urllib.request, json, collections
API="https://api.dandiarchive.org/api"
def get(u): return json.load(urllib.request.urlopen(u,timeout=60))
v=get(f"{API}/dandisets/001357/versions/0.261006.2007/")
print(json.dumps(v.get("assetsSummary"))[:1500])
print(v.get("description"))
url=f"{API}/dandisets/001357/versions/0.261006.2007/assets/?page_size=500"
rows=[]
while url:
    p=get(url); rows+=p["results"]; url=p.get("next")
print(len(rows))
print(collections.Counter(r["path"].split("_")[-1] for r in rows))
print([r["path"] for r in rows][:5])
print(sum(r["size"] for r in rows)/1e9,"GB")
a=rows[0]
m=get(f"{API}/dandisets/001357/versions/0.261006.2007/assets/{a['asset_id']}/")
print(json.dumps(m,indent=1)[:4000])
EOF
```

```
{"species": [{"name": "Macaca mulatta - Rhesus monkey", "schemaKey": "SpeciesType", "identifier": "http://purl.obolibrary.org/obo/NCBITaxon_9544"}], "approach": [{"name": "electrophysiological approach", "schemaKey": "ApproachType"}], "schemaKey": "AssetsSummary", "dataStandard": [{"name": "Neurodata Without Borders (NWB)", "schemaKey": "StandardsType", "identifier": "RRID:SCR_015242"}], "numberOfBytes": 241533432, "numberOfFiles": 159, "numberOfSubjects": 2, "variableMeasured": ["Units", "ElectrodeGroup"], "measurementTechnique": [{"name": "spike sorting technique", "schemaKey": "MeasurementTechniqueType"}, {"name": "surgical technique", "schemaKey": "MeasurementTechniqueType"}]}
We used high-density Neuropixels probes in two awake monkeys (one female and one male) to characterize the shape and texture tuning of dozens of neurons simultaneously. The shape set included 15 simple geometric shapes each presented at eight different rotations in 45° increments, resulting in a total of 120 shape stimuli. Shapes were filled with a uniform color, either darker or brighter than the background luminance. The texture stimulus set was composed of 40 naturalistic grayscale textures. Each texture image was presented in three versions: original, contrast-reversed, or spectrally-matched noise

More detailed information associated with this dataset is described in https://doi.org/10.1523/JNEUROSCI.1893-23.2024 
159
Counter({'ecephys.nwb': 159})
['sub-Z08115/sub-Z08115_ses-20190726SL_ecephys.nwb', 'sub-Z08115/sub-Z08115_ses-20190723SL_ecephys.nwb', 'sub-Z08115/sub-Z08115_ses-20190717SL_ecephys.nwb', 'sub-Z08115/sub-Z08115_ses-20190718SL_ecephys.nwb', 'sub-Z08115/sub-Z08115_ses-20190719SL_ecephys.nwb']
0.241533432 GB
{
 "id": "dandiasset:70893b9c-ef41-4294-9692-2cfec03c58b0",
 "path": "sub-Z08115/sub-Z08115_ses-20190726SL_ecephys.nwb",
 "access": [
  {
   "schemaKey": "AccessRequirements",
   "status": "dandi:OpenAccess"
  }
 ],
 "digest": {
  "dandi:dandi-etag": "70565470158dce17038
[... 110 more lines not kept]
```

**Agent**

The archive has 159 NWB files, 0.24 GB in total, with only Units and ElectrodeGroup. That rules out an LF signal, and there are no RF-mapping files. Next, synthetic tests of the helper functions.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' 2>&1 | grep -v Warning
import sys, types
for mod in ("h5py","remfile","requests"):
    sys.modules[mod]=types.ModuleType(mod)
import numpy as np, v4clusters as V
from scipy import stats
rng=np.random.default_rng(0)
m=120
# two neurons with true signal corr rho, Poisson noise, n repeats
def sim(rho, n, amp=6, rng=rng, noisecorr=0.0):
    z1=rng.standard_normal(m); z2=rho*z1+np.sqrt(1-rho**2)*rng.standard_normal(m)
    lam1=amp*np.exp(0.4*z1); lam2=amp*np.exp(0.4*z2)
    a=rng.poisson(lam1[:,None],(m,n)).astype(float); b=rng.poisson(lam2[:,None],(m,n)).astype(float)
    true=np.corrcoef(np.sqrt(lam1),np.sqrt(lam2))[0,1]
    return np.stack([a,b]), true
for rho in (0.0,0.5,0.8):
    est=[];tr=[];raw=[];lo=[];hi=[]
    for k in range(40):
        arr,t=sim(rho,5)
        nrep=np.full(m,5)
        r,l,h=V.similarity(arr,nrep,f"t{k}",n_boot=200)
        est.append(r[0,1]);tr.append(t);lo.append(l[0,1]);hi.append(h[0,1])
        mx=np.sqrt(arr).mean(2); raw.append(np.corrcoef(mx)[0,1])
    est,tr,lo,hi=map(np.array,(est,tr,lo,hi))
    print(f"rho {rho}: true {tr.mean():.3f} nc {np.nanmean(est):.3f} raw {np.mean(raw):.3f} | boot interval mid {np.nanmean((lo+hi)/2):.3f}, width {np.nanmean(hi-lo):.3f}, est inside interval {np.mean((est>=lo)&(est<=hi)):.2f}, coverage of true {np.mean((tr>=lo)&(tr<=hi)):.2f}")
# regress vs scipy linregress
x=rng.random(20)*2000; y=0.5-0.0002*x+0.1*rng.standard_normal(20)
f=V.regress(x,y); lr=stats.linregress(x,y)
t=stats.t.ppf(.975,18)
print("regress", round(f['intercept'],5), round(lr.intercept,5), round(f['i_lo'],5), round(lr.intercept-t*lr.intercept_stderr,5), round(f['s_lo'],8), round(lr.slope-t*lr.stderr,8))
# reliable readings
print(V.reliable(np.array([.5,.5,.5]),np.array([0,0,0.]),np.array([0.4,0.8,1.2]),"a"), V.reliable(np.array([.5,.5,.5]),np.array([0,0,0.]),np.array([0.4,0.8,1.2]),"b"))
# auc
print("auc", V.auc([3,4,5],[1,2,3]), "expected", (1+1+1+1+1+1+1+1+0.5)/9)
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls executed/001357-namima-2025/.venv/bin/python 2>&1; which -a python3 python; ls ~/.local/bin 2>/dev/null | head; uv --version 2>&1 | head -1
```

```
ls: cannot access 'executed/001357-namima-2025/.venv/bin/python': No such file or directory
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
uv 0.13.6 (x86_64-unknown-linux-gnu)
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q vv 2>&1 | tail -2; uv pip install -q --python vv/bin/python numpy scipy pandas 2>&1 | tail -3; vv/bin/python -c "import numpy,scipy,pandas;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/vv/bin/python - <<'EOF' 2>&1 | grep -v Warning
import sys, types
for mod in ("h5py","remfile","requests"):
    sys.modules[mod]=types.ModuleType(mod)
import numpy as np, v4clusters as V
from scipy import stats
rng=np.random.default_rng(0)
m=120
def sim(rho, n, amp=6):
    z1=rng.standard_normal(m); z2=rho*z1+np.sqrt(1-rho**2)*rng.standard_normal(m)
    lam1=amp*np.exp(0.4*z1); lam2=amp*np.exp(0.4*z2)
    a=rng.poisson(lam1[:,None],(m,n)).astype(float); b=rng.poisson(lam2[:,None],(m,n)).astype(float)
    true=np.corrcoef(np.sqrt(lam1),np.sqrt(lam2))[0,1]
    return np.stack([a,b]), true
for rho in (0.0,0.5,0.8):
    est=[];tr=[];raw=[];lo=[];hi=[]
    for k in range(40):
        arr,t=sim(rho,5)
        nrep=np.full(m,5)
        r,l,h=V.similarity(arr,nrep,f"t{k}",n_boot=200)
        est.append(r[0,1]);tr.append(t);lo.append(l[0,1]);hi.append(h[0,1])
        mx=np.sqrt(arr).mean(2); raw.append(np.corrcoef(mx)[0,1])
    est,tr,lo,hi=map(np.array,(est,tr,lo,hi))
    print(f"rho {rho}: true {tr.mean():.3f} nc {np.nanmean(est):.3f} raw {np.mean(raw):.3f} | boot interval mid {np.nanmean((lo+hi)/2):.3f}, width {np.nanmean(hi-lo):.3f}, est inside {np.mean((est>=lo)&(est<=hi)):.2f}, coverage of true {np.mean((tr>=lo)&(tr<=hi)):.2f}")
x=rng.random(20)*2000; y=0.5-0.0002*x+0.1*rng.standard_normal(20)
f=V.regress(x,y); lr=stats.linregress(x,y)
t=stats.t.ppf(.975,18)
print("regress", round(f['intercept'],5), round(lr.intercept,5), round(f['i_lo'],5), round(lr.intercept-t*lr.intercept_stderr,5), round(f['s_lo'],8), round(lr.slope-t*lr.stderr,8))
print(V.reliable(np.array([.5,.5,.5]),np.array([0,0,0.]),np.array([0.4,0.8,1.2]),"a"), V.reliable(np.array([.5,.5,.5]),np.array([0,0,0.]),np.array([0.4,0.8,1.2]),"b"))
print("auc", V.auc([3,4,5],[1,2,3]), "expected", 8.5/9)
EOF
```

```
rho 0.0: true -0.014 nc -0.016 raw -0.017 | boot interval mid -0.015, width 0.175, est inside 1.00, coverage of true 0.82
rho 0.5: true 0.482 nc 0.483 raw 0.399 | boot interval mid 0.395, width 0.184, est inside 0.60, coverage of true 0.53
rho 0.8: true 0.787 nc 0.787 raw 0.650 | boot interval mid 0.650, width 0.155, est inside 0.00, coverage of true 0.10
regress 0.48618 0.48618 0.38935 0.38935 -0.00027421 -0.00027421
[ True False False] [ True  True False]
auc 0.9444444444444444 expected 0.9444444444444444
```

**Agent calls Grep**

```json
{
 "pattern": "confidence limit|bootstrap|Pospisil|aggregate RF|center of mass|sink|5 spikes|optimal position|variance-to-mean|unreliable|good",
 "path": "paper/10.1523-jneurosci.1893-23.2024.txt",
 "output_mode": "content",
 "-i": true
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1893-23.2024.txt",
 "offset": 360,
 "limit": 70
}
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 1: Namima et al. 2025 on DANDI:001357 (0.261006.2007)**

The claims file has 27 claims. The notebook tests 21 and marks 6 as blocked; I agree with all six blocks.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| methods-sessions-and-neurons | reproduced | Cell 13: sessions 30/44/17/34/34 and neurons 1869/985 responsive, 427/360 excluded. All are within tolerance. |
| ex-m2p6-cluster | partially_reproduced | Cell 17: p06 has 24 neurons over a 2,340 µm span. 13 neurons have a significant positive intercept, all with negative slopes; the paper has 11 (tolerance ±1.1). Against the paper's set, 17 is missing and 12, 21 and 22 are added. The session is found but the set and count do not match. |
| ex-m2p6-pairs | partially_reproduced | Cell 19: pair 3–8 gives 0.780 dark and 0.894 bright, pair 18–19 gives −0.000 dark, and both distances (260, 80 µm) are within tolerance. Pair 18–19 bright is −0.144 against −0.25 ± 0.025. |
| ex-m2p6-invariance | reproduced | Cell 21: 20 of 24 under reliability (a), within 19 ± 1.9. Reading (b) gives 22, outside. |
| ex-csd-sinks | blocked (data_missing) | Confirmed on the archive: 159 files, 0.24 GB in total, variableMeasured is only Units and ElectrodeGroup, and the files have no acquisition or processing (cell 57). There is no LF signal, so no part can be tested. |
| ex-m1p12-no-cluster | not_reproduced (borderline) | Cell 23: 42 neurons over 2,580 µm, and 83–86% have reliable invariance above 0.5. The paper says the intercept was "significantly different from zero for only one neuron", and the claims file defines significant as the CI excluding zero. That count is 4 (dark), which exceeds the criterion's limit of 2. Counting significant *positive* intercepts only gives 1, which would make it reproduced. |
| ex-m1p12-strong-responses | reproduced | Cell 25: baseline-subtracted counts are exactly 28 and 26. |
| pop-significant-isimilarity | not_reproduced | Cell 27: none of the 12 readings puts the four counts within tolerance. The nearest, dark/(a)/(ii), gives 394, M1 228, M2 166 against 344, 203, 141. The fewest neurons in a penetration is 1, against 6. |
| pop-intercept-slope-correlation | reproduced | Cell 29: Pearson r is −0.768 (dark, a) and −0.735 (dark, b), p ≈ 0, and 0 neurons have both significantly positive (criterion allows ≤ 2). |
| pop-dark-bright-consistent | not_reproduced | Cell 31: Spearman r is 0.484 (a) and 0.520 (b); the upper bound is 0.4785. n is 1643/1757 against 1847. |
| pop-contrast-invariance | reproduced (fragile) | Cell 33: two of eight readings fall within 0.64 ± 0.064, both under reliability (b) with unreliable values counted as 0: 0.632 over all neurons and 0.619 from per-penetration medians. Leaving unreliable values out gives about 0.77. |
| pop-sparse-across-penetrations | reproduced | Cell 35: the dark and bright readings give 54–59 penetrations, 27–29 with five or more, and 20 with more than 30 neurons. |
| pop-asymptote-20-percent | reproduced | Cell 37: dark/(a) pooled is 21.5% and dark/(b) median is 21.0%. The other readings range from 16% to 35%. |
| pop-mean-isimilarity-yield | reproduced | Cell 39: the SD of penetration means is smaller above 30 neurons in all four readings (0.084–0.107 against 0.127–0.204). Levene p is 0.015–0.18. No contrast reading reproduces pop-significant-isimilarity, so the criterion's choice of reading is moot. |
| pop-recording-density | reproduced | Cell 41: neurons per µm gives r = 0.257 (dark, a) and 0.256 (bright, a), p ≈ 0.03, within 0.236 ± 0.0236. |
| pop-within-vs-across-sessions | partially_reproduced | Cell 43: direction holds and p < 1e-4 under every reading. No reading matches all four means; for example, same-session pairs give 0.030 (Pearson) or 0.083 (noise-corrected) against 0.0582. |
| orientation-sf-isimilarity | blocked (data_missing, outside input) | Neither the dataset nor its stimulus templates hold the shape images. I did not verify the notebook's statement that no public, pinned source exists. |
| orientation-auc-coarse-clusters | not_reproduced | Cell 45: two penetrations are all-one and two are switching. M2p6 has 2 sign changes and M1p5 has 12, so neither is of one kind; this holds for every stim_ID taken as the spindle. |
| apc-peaks-sparse-clustering | blocked (data_missing, outside input) | Needs the shapes' curvature descriptions; same caveat as orientation-sf-isimilarity. |
| apc-example-m2p51 | blocked (data_missing, outside input) | Same as apc-peaks-sparse-clustering. |
| gyrus-penetrations-consistent | blocked (metadata_insufficient) | The asset metadata names only session and description, electrode location is only "V4", and the dataset has no RF-mapping files. The 18 gyral penetrations cannot be identified, so no part is testable. |
| texture-sparse-clusters | not_reproduced | Cell 47: no reading matches, and the partial condition (total and penetration counts) fails in all readings. The nearest, original/(a)/(i), gives 193 neurons in 30 penetrations (needs at least 30.6). |
| texture-original-reversed-consistent | not_reproduced | Cell 49: r is 0.706 (a) and 0.642 (b) against 0.464 ± 0.046. |
| texture-asymptote-20-percent | not_reproduced | Cell 51: only 7 penetrations have more than 30 neurons, and every reading gives 25.6–52%. |
| position-optimal-consistent | reproduced (caveat) | Cell 53: against the main shape test, r is 0.297 (a) and 0.325 (b), within tolerance. Against the inferred centre, r is 0.45–0.47. All p < 1e-4. Caveat: if file position 4 is the centre, p = 2.1e-4 (problem 4). |
| position-examples-invariant | not_reproduced | Cell 55: for the accepted M2p9 session (20210421, labelled p12) both readings fail. For M2p28 (p28), reading (b) fails: up to 2 (a) or 16 (b) neurons are significant at one position, and the limit is 1. Reading (a) holds only under reliability (b) with position 0 as centre. |
| simulation-random-with-domains | blocked (other) | A simulation with unstated parameters, not a test on recorded data. |

### B. Problems

1. **[affects a conclusion]** `reliable`, reading (a); cells 27, 31, 47, 49. The paper says only 2 of 1,850 shape neurons and 48 of 979 texture neurons lacked a line.
   - Reading (a) leaves 121–140 shape neurons and 304/322 texture neurons without a line.
   - Reading (b) leaves 62/44 texture neurons, close to the paper.
   - So the paper's own counts largely rule out reading (a); the claims file, which left it open, missed this constraint.
   - Matches that rest on (a) are therefore suspect: ex-m2p6-invariance, pop-asymptote dark/(a) pooled, and pop-recording-density.
   - Under (b), the significant counts are further from the paper (shape 443–453 against 344; texture 276–308 against 207).
   - Each of these claims also has a match under (b) or another reading, so the outcomes in A stand.
2. **[affects a conclusion]** Cell 8 and the texture analyses in cells 12 and 47–51. The clock check fails for five M1 texture files (20200715, 20200719, 20200729, 20200730, 20200804): 0–12% of units are stimulus-selective, against a median of 73% elsewhere. These files are still used in every texture analysis and count, and no variant leaves them out. Their stimulus labels or timing may be wrong. This could shift the M1 texture counts (paper: 18 neurons, 7 penetrations).
3. **[affects a conclusion]** Cell 23, ex-m1p12-no-cluster. The paper's "significantly different from zero" is two-sided, and that count is 4 (dark) and 5 (bright). Judging only the positive count (1) would make the claim look reproduced.
4. **[affects a conclusion]** Cell 53, position centre. The centre is the author's own heuristic: the position with the largest population response. It picks different file positions across sessions (1: 12, 2: 11, 4: 5, 0: 3, 3: 3). If the labels are fixed (for example 0 = centre, as in the paper's order centre, N, S, E, W), the heuristic is wrong in most sessions. Reading (a) passes for any label except 4 (p = 2.1e-4), and variants were run only under reliability (a). Cell 55, reading (a), depends on the same choice.
5. **[affects a conclusion]** `find_pen`, cell 55. M2p9 is taken to be 20210421, labelled p12, because its count (16) passes the 10% rule. The dataset's own labels match the paper's counts exactly for p06 (24), p12 (42) and p28 (55), which makes p09 (18 neurons) the likelier M2p9. Under p09 the M2p9 half passes both readings. The claim still fails on M2p28 under reading (b).
6. **[does not affect a conclusion]** `similarity` / `invariance`. In the synthetic test I ran (true r = 0.8, 5 repeats), the percentile bootstrap interval is centred on the uncorrected r (interval midpoint 0.650 against an estimate of 0.787). It covered the estimate in 0% of runs and the true value in 10%. In the data, the pair 3–8 interval is 0.51–0.705 around an estimate of 0.78 (cell 19). Reliability uses the width only, so the outcomes are probably unaffected. The intervals should not be read as CIs of the corrected r.
7. **[does not affect a conclusion]** `nc_corr` assumes independent noise between two simultaneously recorded neurons. Noise correlations between nearby units could inflate near-pair similarity and so the significant-intercept counts. The paper's method probably makes the same assumption; it is not checked.
8. **[does not affect a conclusion]** `optimal_isim` and position analyses, cell 53. The requirement of at least 4 neurons per penetration is the author's own and is not stated as an assumption.
9. **[does not affect a conclusion]** Helper checks on synthetic inputs all pass. `nc_corr` is unbiased (true 0.482 → 0.483; 0.787 → 0.787). `regress` matches scipy's `linregress` t intervals exactly. `reliable` uses width ≤ 0.5 for (a) and ≤ 1.0 for (b). `auc` is correct with ties.
10. **[does not affect a conclusion]** Data-model limits:
    - Depth is the best-channel position in 20 µm steps, not the template centre of mass (stated in the notebook).
    - One shape/position day (20210529) has a single unit, against the paper's minimum of 6 per penetration (cell 27).
    - The dataset has 34 position files against the paper's 33.

### C. What I could not check, and what output would settle it

- **Whether `cond_ID == 0` marks blanks:** a crosstab of `cond_ID` against `luminance`, `stim_ID` and `mode` per test.
- **Whether the files encode position geometry, RF centre or grid location:** the full column lists of the trials and units tables. This bears on problem 4 and on the gyrus block.
- **The effect of the five failed texture files:** the texture-claim tables rerun without them, plus their per-unit tuning.
- **Position claims under every centre and reliability:** the cell 53 variant under reliability (b), and cell 55 reading (a) for each fixed position label.
- **How lenient each reliability reading is:** the distribution of bootstrap interval widths, and the number of neurons with a line at dark, bright and both contrasts under each reading, set against the paper's 2/1850 and 1847.
- **Whether a public, pinned source of the Pasupathy & Connor (2001) shape outlines exists:** I did not search outside the archive, so these blocks rest on the notebook's word.

## End of run

15 turns, 4 minutes, $1.65 at API prices, result: success.
