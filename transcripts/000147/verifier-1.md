# 000147 · verifier-1 · run 38474180320

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `CronCreate`, `CronDelete`, `CronList`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `RemoteTrigger`, `ReportFindings`, `ScheduleWakeup`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Workflow`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls docs 2>/dev/null; cat *.yaml *.yml *.json 2>/dev/null | head -100
```

```
total 344
drwxr-xr-x 5 runner runner    4096 Oct 13 21:57 .
drwxr-xr-x 7 runner runner    4096 Oct 13 21:57 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 13 21:51 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 13 21:51 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 13 21:57 .claude
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .env
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .env.development
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .env.local
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .env.production
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .env.test
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .env.test.local
drwx------ 2 runner runner    4096 Oct 13 21:57 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 13 21:51 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 13 21:51 .github
-rw-r--r-- 1 runner runner       0 Oct 13 21:57 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 13 21:51 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 13 21:51 .mcp.json
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 100,300p 10.7554-elife.74478.yaml; cat ppcfingers.py
```

```
average PC-IP RDM was statistically typical (permutation test, p = 0.55).
  source: Results, Figure 2-figure supplement 4
- id: rdm-consistency
  statement: The finger RDMs were consistent across sessions, with an average pairwise correlation
    between session RDMs of r = 0.90 (SD 0.04, min 0.83, max 0.99).
  source: Results, "Representational structure did not trend toward task optimum"
  expected:
    quantity: mean pairwise Pearson correlation between session RDMs
    value: 0.90
    tolerance: 0.03
- id: fig3a-no-trend-to-unstructured
  statement: Over sessions the model fit did not trend from the able-bodied model toward the
    unstructured model (session by model interaction t(6) = 0.50, one-tailed p = 0.32).
  source: Figure 3a, Results
  criterion: In a regression of WUC on session index, model and their interaction, the interaction
    in the direction of the unstructured model is not significant (one-tailed p > 0.05).
- id: fig3b-confused-pairs-no-increase
  statement: The distances between the most confused finger pairs (middle-ring and ring-pinky) did
    not increase across sessions (one-tailed p > 0.99) or across runs within sessions (one-tailed
    p = 0.67).
[... 418 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_guan_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain'])[:5000])
            if 'image/png' in d: print('--[image]--')
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt
```

```
911 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Guan, Aflalo et al. (2022) from dandiset 000147
4	
5	Paper: Guan C, Aflalo T, Zhang CY, Amoruso E, Rosario ER, Pouratian N, Andersen RA (2022).
6	Stability of motor representations after paralysis. eLife 11:e74478.
7	[doi:10.7554/eLife.74478](https://doi.org/10.7554/eLife.74478). The paper is open access, and its
8	full text, figure legends and methods were used (eLife, PMC9555862).
9	
10	Data: [DANDI:000147](https://dandiarchive.org/dandiset/000147/0.221122.2256), version
11	0.221122.2256, streamed from the archive. The dandiset has two published versions, 0.220913.2243
12	and 0.221122.2256, with the same ten assets (same asset IDs and sizes). The later version is used
13	because its metadata names this paper; the earlier one names the bioRxiv preprint. The authors'
14	download script pins the earlier version, so the files are the ones the authors analysed.
15	
16	## What can and cannot be tested
17	
18	The paper records from a Utah array in the posterior parietal cortex (PC-IP) of one tetraplegic
19	participant, NS, over ten sessions on nine days, while she attempted to press the cued finger
20	(thumb T, index I, middle M, ring R, pinky P) or did nothing (No-Go, X). The dandiset holds the
[... 892 more lines not kept]
```

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC9555862/unicode" -o paper/pmc.json; ls -la paper; head -c 300 paper/pmc.json
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
d=json.load(open('paper/pmc.json'))
with open('paper/paper.txt','w') as f:
  for p in d[0]['documents'][0]['passages']:
    f.write('['+p['infons'].get('section_type','')+'|'+p['infons'].get('type','')+'] '+p['text']+'\n\n')
"; wc -c paper/paper.txt; grep -n -i -E "chance|leave-one-out|Ledoit|FDR|0.1 Hz|gaze|cue location|bootstrap|t\(6\)|t\(8\)|t\(82\)|84|4016|4080|L-ratio|noise ceiling|calibration|control task" paper/paper.txt | cut -c1-400
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '43,53p;61,63p;93,93p;101,124p;228,230p;240,242p;256,340p' paper/paper.txt | cut -c1-3000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -E "grid|data availab|dandi|github|fingers_rsa" paper/paper.txt | cut -c1-1200 | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000147/versions/0.221122.2256/" | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d.get(k) for k in ['name','description','assetsSummary','relatedResource','wasGeneratedBy']},indent=1)[:4000])"; curl -s "https://api.dandiarchive.org/api/dandisets/000147/versions/0.221122.2256/assets/?page_size=100" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['count']); [print(a['path'],a['size'],a['asset_id']) for a in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000147/versions/0.221122.2256/assets/ee3b7230-36b6-479b-bfd0-bff5e3e5aa9c/" | python3 -c "import json,sys; d=json.load(sys.stdin); [d.pop(k,None) for k in ['digest','contentUrl']]; print(json.dumps(d,indent=1)[:3500])"; curl -s "https://api.github.com/repos/AndersenLab-Caltech/fingers_rsa/git/trees/6915bf863ad1339e6fc8c6886032cd0f70fd8b10?recursive=1" | python3 -c "import json,sys; d=json.load(sys.stdin); [print(t['path']) for t in d.get('tree',[]) if 'model' in t['path'].lower() or t['path'].endswith(('.hdf5','.mat','.csv','.npy'))]; print(d.get('message',''))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://raw.githubusercontent.com/AndersenLab-Caltech/fingers_rsa/6915bf863ad1339e6fc8c6886032cd0f70fd8b10; for f in models/.gitignore scripts/config/rsa/models/muscle_somatomorphic.yaml scripts/config/rsa/models/able_bodied.yaml; do echo "== $f"; curl -s "$B/$f"; done; curl -s "https://api.github.com/repos/AndersenLab-Caltech/fingers_rsa/git/trees/6915bf863ad1339e6fc8c6886032cd0f70fd8b10?recursive=1" | python3 -c "import json,sys; d=json.load(sys.stdin); [print(t['path']) for t in d['tree'] if any(k in t['path'].lower() for k in ['muscle','somat','usage','ejaz','gaze','location','lratio','l_ratio'])]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://raw.githubusercontent.com/AndersenLab-Caltech/fingers_rsa/6915bf863ad1339e6fc8c6886032cd0f70fd8b10; curl -s "https://api.github.com/repos/AndersenLab-Caltech/fingers_rsa/git/trees/6915bf863ad1339e6fc8c6886032cd0f70fd8b10?recursive=1" | python3 -c "import json,sys; d=json.load(sys.stdin); [print(t['path']) for t in d['tree'] if t['path'].endswith(('.py','.md','.yaml'))]" > $TMPDIR/files.txt; wc -l $TMPDIR/files.txt; for f in $(grep -E '\.py$|README' $TMPDIR/files.txt); do curl -s "$B/$f" | grep -n -i -E "somatomorph|muscle|usage|\.mat|ejaz|model_dir|models/" | sed "s|^|$f: |"; done | head -40; echo; curl -s "$B/scripts/config/task/override/cue_location.yaml"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, ppcfingers as pf
from statsmodels.stats.weightstats import DescrStatsW
rng=np.random.default_rng(0)
# crossnobis: known means, identity noise
N=50; reps=40
mu={c: rng.normal(0,1,N)*(0 if c in 'MRP' else 1) for c in pf.FINGERS}
mu['R']=mu['M'].copy(); mu['P']=mu['M']+0.5
y=np.repeat(pf.FINGERS+['X'],reps)
X=np.stack([ (mu[c] if c!='X' else np.zeros(N)) + rng.normal(0,1,N) for c in y])
d=pf.crossnobis_rdm(X,y)
true=np.array([np.sum((mu[a]-mu[b])**2)/N for a,b in pf.PAIRS])
print(np.round(d,3)); print(np.round(true,3))
# null: all same -> ~0
X0=rng.normal(0,1,(len(y),N)); print('null mean', pf.crossnobis_rdm(X0,y).mean().round(4))
# diag lda
y2=np.repeat(np.array(list('ABC')),30); X2=rng.normal(0,1,(90,20)); X2[y2=='B',0]+=3
print('lda acc', (pf.diag_lda_cv(X2,y2,None)==y2).mean(), 'null', (pf.diag_lda_cv(rng.normal(0,1,(90,20)),y2,None)==y2).mean())
v=np.array([.8,.9,.85]); w=np.array([300,400,350])
print(pf.weighted_sd(v,w), DescrStatsW(v,weights=w,ddof=1).std)
# fold_ids blocks?
print(pf.fold_ids(np.tile(list('TIMRP'),16))[:40])
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
cd  ls ~/.venv* /opt 2>/dev/null | head; which -a python python3 uv pip 2>/dev/null; python3 -m venv $TMPDIR/v && $TMPDIR/v/bin/pip -q install numpy pandas scikit-learn statsmodels scipy 2>&1 | tail -2
```

```
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipx
pipx_bin
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
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, ppcfingers as pf
from statsmodels.stats.weightstats import DescrStatsW
rng=np.random.default_rng(0)
N=50; reps=40
mu={c: rng.normal(0,1,N) for c in pf.FINGERS}
mu['R']=mu['M'].copy(); mu['P']=mu['M']+0.5
y=np.repeat(pf.FINGERS+['X'],reps)
X=np.stack([ (mu[c] if c!='X' else np.zeros(N)) + rng.normal(0,1,N) for c in y])
d=pf.crossnobis_rdm(X,y)
true=np.array([np.sum((mu[a]-mu[b])**2)/N for a,b in pf.PAIRS])
print(pf.PAIR_NAMES); print(np.round(d,3)); print(np.round(true,3))
X0=rng.normal(0,1,(len(y),N)); print('null mean', pf.crossnobis_rdm(X0,y).mean().round(4))
# few-trial regime like per-run: 8 trials per finger, 95 neurons
y8=np.repeat(pf.FINGERS+['X'],8); X8=np.stack([(mu[c] if c!='X' else np.zeros(N)) + rng.normal(0,1,N) for c in y8])
print('per-run-like', np.round(pf.crossnobis_rdm(X8,y8),2))
y2=np.repeat(np.array(list('ABC')),30); X2=rng.normal(0,1,(90,20)); X2[y2=='B',0]+=3
print('lda acc', (pf.diag_lda_cv(X2,y2,None)==y2).mean(), 'null', (pf.diag_lda_cv(rng.normal(0,1,(90,20)),y2,None)==y2).mean())
v=np.array([.8,.9,.85]); w=np.array([300,400,350])
print(pf.weighted_sd(v,w), DescrStatsW(v,weights=w,ddof=1).std)
yy=np.tile(list('TIMRPX'),8); print(pf.fold_ids(yy))
EOF
```

```
['TI', 'TM', 'TR', 'TP', 'IM', 'IR', 'IP', 'MR', 'MP', 'RP']
[ 2.336e+00  1.845e+00  1.819e+00  2.198e+00  1.919e+00  1.927e+00
  2.270e+00 -1.000e-03  2.750e-01  2.830e-01]
[2.054 1.728 1.728 1.876 1.675 1.675 1.919 0.    0.25  0.25 ]
null mean 0.0092
per-run-like [ 9.87 10.22 10.8   9.28  8.66  7.93  8.8   0.05  0.87  1.54]
lda acc 0.5666666666666667 null 0.26666666666666666
0.04056547951056765 0.04056547951056765
[0 0 0 0 0 0 0 0 1 0 1 0 1 1 1 1 2 1 1 2 2 1 2 1 2 3 2 2 3 2 2 3 3 3 3 2 3
 4 3 4 4 3 4 4 4 4 4 4]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, ppcfingers as pf
from sklearn.covariance import OAS
y=np.repeat(pf.FINGERS,8); f=pf.fold_ids(y)
for k in range(5): print(k, [(y[f==k]==c).sum() for c in pf.FINGERS])
c=OAS(assume_centered=True).fit(np.zeros((5,10))).covariance_; print('cov of zero residuals max', np.abs(c).max())
EOF
```

```
0 [np.int64(2), np.int64(2), np.int64(1), np.int64(2), np.int64(1)]
1 [np.int64(2), np.int64(1), np.int64(2), np.int64(2), np.int64(1)]
2 [np.int64(2), np.int64(1), np.int64(2), np.int64(1), np.int64(2)]
3 [np.int64(1), np.int64(2), np.int64(2), np.int64(1), np.int64(2)]
4 [np.int64(1), np.int64(2), np.int64(1), np.int64(2), np.int64(2)]
cov of zero residuals max 0.0
```

**Agent**

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| recording-counts | reproduced | Cell 8: 95.8 (SD 6.7) units and 408.0 (SD 40.8) trials per session, 4080 trials in total. |
| fig1b-online-accuracy | reproduced | Cell 10: 0.8596 over 4016 trials, trial-weighted SD 0.036. The paper's chance level is 17%; the notebook's shuffle null has mean 0.169 (1/6 = 0.167), so the two agree. Session 1 has 64 No-Go trials in the data, not the 84 in the Methods; 4080 − 64 = 4016 matches the paper's own total. |
| fig1b-errors-middle-ring-pinky | reproduced, under one reading | Cell 12: 264/379 = 0.697 when the denominator is errors between two fingers. With all errors it is 0.468, and with errors on finger trials 0.592. The paper does not name the denominator, but only the first reading gives "the majority (70%)". |
| fig1s4a-offline-accuracy | reproduced | Cell 14: diagonal LDA with leave-one-out gives 0.934 (SD 0.016) over 4080 trials. That is within ±0.02 of 0.92. The authors' 8-fold pipeline gives 0.924. |
| fig1s4b-calibration-accuracy | blocked (data_missing) | The archive has 10 assets, all with the session description "individual-finger press, main task". The trial counts (4080) match the main task only. |
| fig1s5-tuned-fraction | reproduced | Cell 16: 0.879 with FDR over all units pooled (0.875 with FDR per session), against 0.89 ± 0.05. No units fell below 0.1 Hz. |
| fig1s6a-gaze-regression | blocked (metadata_insufficient), partly testable | `cue_location` is a 1–12 index with no map to screen coordinates. The authors' repo config (`task/override/cue_location.yaml`) also lists only 1–12. The regression could have been run under row-major and column-major 3×4 layouts. Given 1s6b, it is not safe to assume r² ≈ 0. |
| fig1s6b-gaze-classification | not_reproduced | Cell 18: pooled cue-location accuracy is 0.1154. The shuffle null's 95% range is 0.0755–0.0944 (max 0.0998), and 0 of 500 shuffles reach the observed value. The within-finger null and finger-mean removal give the same picture (0.117), and 5 of 10 sessions have binomial p < 0.05. The finger half of the criterion holds (0.934 against a null of 0.155–0.181). The effect is small (11.5% against 8.3%), but the criterion fails. |
| fig1s6c-control-task | blocked (data_missing) | The control task is not in any of the 10 assets (same evidence as for 1s4b). |
| fig2d-rdm-structure | reproduced | Cell 20: the largest of the middle/ring/pinky distances is 0.482 and the smallest thumb distance is 0.641 (max-scaled). The criterion holds in 9 of 10 individual sessions. |
| fig2f-able-bodied-over-unstructured | reproduced | Cell 22: the WUC difference is 0.0998, bootstrap 95% CI 0.074–0.127, higher in 10 of 10 sessions. Paired p = 5.9e-5 against the paper's 5.7e-5. |
| fig2s5-mc-over-pcip | reproduced | Cell 24: MC minus PC-IP CI is 0.060–0.112. Mean WUC with MC is 0.969, against a lower noise ceiling of 0.984 (margin −0.015, within the criterion's −0.05). The MC WUC reaches the lower ceiling in only 1 of 10 sessions. The p-value is 7.9e-5 against the paper's 1.9e-6. |
| fig2-typical-among-individuals | blocked (data_missing) | Individual-participant fMRI RDMs are in neither the dandiset nor the authors' archived repo. The repo's `models/` holds only three .hdf5 files: MC, PC-IP and unstructured. |
| rdm-consistency | reproduced (borderline) | Cell 26: mean r = 0.928 (SD 0.041, min 0.817, max 0.990) against 0.90 ± 0.03. |
| fig3a-no-trend-to-unstructured | reproduced, weakly | Cell 28: interaction t(16) = 1.47, one-tailed p = 0.080, so the criterion is met. The statistic is three times the paper's t(6) = 0.50, the p-value is near the threshold, and WUC with PC-IP itself falls over sessions (p = 0.038). |
| fig3b-confused-pairs-no-increase | reproduced | Cell 30: the session coefficient is negative (t = −3.56, one-tailed p = 0.996) and so is the run coefficient (t = −1.05, p = 0.85). The same holds in all variants. |
| fig3s1-all-pairs-small-decrease | reproduced on the criterion; significance only partly | Cell 32: both coefficients are negative and f² is 0.0064 and 0.0119 (< 0.02). The paper's significant session decrease (p = 0.004) appears only with the session noise covariance (p = 0.0055). In the main variant it is p = 0.052. |
| fig4e-muscle-before-somatotopy | blocked (data_missing) | The Muscle, Somatomorphic and Usage RDMs are named in the repo's configs (`muscle_somatomorphic.yaml`), but the .hdf5 files are gitignored and not in the archived commit or the dandiset. Time-resolved RDMs could be computed from the data; the decomposition cannot. |
| fig4s1-model-selection | blocked (data_missing) | Same component models missing. |
| fig4s4-well-isolated-units | blocked (data_missing) | The asset metadata lists only Units and ElectrodeGroup as measured variables. No waveforms or L-ratio are described, so the well-isolated subset cannot be defined. |

**B. Problems**

1. [affects a conclusion] Cell 12: three denominators are reported and only one matches the paper. Nothing in the paper fixes that choice, so the outcome for the 70% claim depends on an assumed definition.
2. [affects a conclusion] Cell 18: cue location is decodable above every shuffle, contrary to the paper's 1s6b. The notebook shows this robustly (two nulls, finger-mean removal, the authors' pipeline at 0.1115). It does not show screen- or run-level location counts, which would rule out a temporal-structure artefact. The design (each location once per 12-trial screen) makes such an artefact unlikely.
3. [affects a conclusion, weakly] Cell 28: the df is 16 against the paper's 6, and the model specification may differ from the authors'. With p = 0.08, a slightly different specification could cross 0.05.
4. [does not affect a conclusion] `crossnobis_rdm` / `run_rdms` (cells 30, 32): per-run RDMs use fold covariances from about 8 trials. In folds holding one trial of a finger, that finger's residuals are exactly zero. The covariance therefore has rank of about 3 across about 95 units, OAS shrinks toward a tiny identity, and the distances inflate. Per-run means are 5.06 against 0.68 for whole sessions; my synthetic test gave about 5× inflation, while session-sized data was unbiased (null mean 0.009). Directions are unchanged across variants, but the significance of the fig3s1 session term depends on the variant.
5. [does not affect a conclusion] `load_model_rdm`: the condition-order assert runs only if `pattern_descriptors/condition` exists, and the notebook never prints whether it did. The printed vectors are consistent with T, I, M, R, P order (thumb pairs are largest in the PC-IP model).
6. [does not affect a conclusion] Cell 30: the run-term df is 83 (85 runs), against the paper's 82. The paper itself also reports t(74) for the same test.
7. [does not affect a conclusion] Cell 22/24: the bootstrap "t-test" is a reconstruction, which explains p = 7.9e-5 against the paper's 1.9e-6. The criteria use CIs, so outcomes are unaffected.
8. [does not affect a conclusion] `tuning_pvalues`: the 0.1 Hz exclusion uses the in-window rate across all trials (minimum 0.113 Hz), while the paper may mean the session-wide rate. At most a few units could change.
9. [does not affect a conclusion] Helpers I tested on synthetic data: `weighted_sd` matches DescrStatsW(ddof=1), `diag_lda_cv` sits at chance on null data, and `crossnobis_rdm` recovers known distances (about 10% shrinkage bias) with a zero-distance pair giving −0.001. I found no train/test leakage in the classification or RDM code. Model RDMs come from the authors' repo, not the dandiset, and the notebook says so.

**C. What I could not check**

- Whether `start_time` is exactly the cue. The notebook infers it from the decoding curve (chance before the start, above 0.4 at 0.6 s). A trials-table column description, or the epoch/screen structure, would settle it.
- Whether the location decoding in 1s6b reflects gaze or trial structure. A table of `cue_location` against run and screen (trial_number // 12), and location accuracy with folds split by screen, would decide it.
- What the gaze regression would give. Cross-validated r² under row-major and column-major layouts would make 1s6a partly testable.
- The units table's column names (waveform_mean, quality metrics). Printing them would have confirmed the 4s4 block directly; the API metadata only implies it.
- Whether the model .hdf5 files carry condition descriptors. Printing that would close problem 5.
- The authors' exact regression specification for fig3a (the df of 6 is unexplained).

I saved the paper's full text (PMC9555862) under `paper/`. I did not download the dandiset or run the notebook.

## End of run

17 turns, 4 minutes, result: success.
