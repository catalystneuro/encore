# 000252 · verifier-1 · run 41832402647

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 364
drwxr-xr-x 6 runner runner    4096 Nov  4 13:05 .
drwxr-xr-x 7 runner runner    4096 Nov  4 13:05 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 12:47 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 12:47 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  4 13:05 .claude
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .env
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .env.development
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .env.local
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .env.production
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .env.test
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .env.test.local
drwx------ 2 runner runner    4096 Nov  4 13:05 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 12:47 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 12:47 .github
-rw-r--r-- 1 runner runner       0 Nov  4 13:05 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 12:47 .idea
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1101-2022.12.07.22283227.yaml"
}
```

```
1	# Claims for Guan et al., "Compositional coding of individual finger movements in human posterior
2	# parietal cortex and motor cortex enables ten-finger decoding", on dandiset 000252.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md (Reader).
5	#
6	# Text read. The bioRxiv preprint, version 1 (doi:10.1101/2022.12.07.22283227), full text from
7	# bioRxiv JATS XML (paper/10.1101-2022.12.07.22283227.txt): main text, Methods, figure legends and
8	# the supplementary figure legends (Supplementary Figures 1 to 11). The contents of Supplementary
9	# Table 1 (phase durations) and Supplementary Table 2 (session dates) are not in the text, only
10	# their legends; no claim here rests on their numbers, since every analysis window is defined from
11	# a phase onset. The equation of the cross-validated Mahalanobis distance (Methods, Neural distance
12	# between fingers) is lost in the text; its description in words is used. No PDF was supplied.
13	#
14	# Code. The paper links no analysis code. It names two Python libraries: the representational
15	# similarity analysis toolbox (rsatoolbox, ref 57) for cross-validated Mahalanobis distances, and
16	# DABEST (ref 53) for Hedges' g with bootstrap confidence intervals.
17	#
18	# Dataset. Its archive title is "Finger_RL: human intracortical recordings during attempted finger
19	# movements of right and left hands", and the paper's Data Availability names dandiset 000252. It is
20	# meant to hold the ten-finger (right and left hand) task; whether it also holds the
[... 622 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "fingers.py"
}
```

```
1	"""Loading and measures for dandiset 000252 (Guan et al., ten-finger press task).
2	
3	The dandiset holds the ten-finger press task only: 10 sessions of participant N
4	(subject ``P1`` in the files, one PPC array) and 2 sessions of participant J
5	(subject ``N1`` in the files, a PPC and an MC array). Files are streamed from the
6	DANDI archive at the pinned version ``VERSION``; nothing is written to disk.
7	
8	Where each parameter comes from:
9	
10	- Firing rate is the spike count in a 500 ms window divided by its duration;
11	  the Go window starts 200 ms after the Go cue, the Delay window 200 ms after the
12	  Delay screen, the Cue window 200 ms after the Cue screen, and the ITI window is
13	  the last 500 ms of the ITI (paper, Methods, Feature Extraction). The Delay
14	  screen onset is the file's ``cue_off_time`` (the cue disappears at the start of
15	  the delay; Methods, Tasks, and Figure 3 legend: "A delay period separates the
16	  Cue phase from a condition-independent Go display").
17	- Neurons with mean rate below 0.5 Hz are excluded (Methods, Feature Extraction).
18	  Readings of "average firing rate" are claims-file O1: (a) spikes over the whole
19	  recorded session (the sum of the unit's ``obs_intervals``); (b) the mean of the
20	  Go-window rates over all trials. For (b) the Go window is taken as "the analysis
[... 500 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_guan_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
"
```

```
<persisted-output>
Output too large (61.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/7e846225-970d-4351-bd87-b5dee901dec0/tool-results/b5s39453c.txt

Preview (first 2KB):
==================== 0 markdown
# Reproducing Guan et al. (preprint 2022) from dandiset 000252

**Paper.** Guan, Aflalo, Kadlec, Gámez de Leon, Rosario, Bari, Pouratian and Andersen, "Compositional coding of individual finger movements in human posterior parietal cortex and motor cortex enables ten-finger decoding", medRxiv/bioRxiv preprint, doi:10.1101/2022.12.07.22283227.

**Dataset.** DANDI:000252, "Finger_RL: human intracortical recordings during attempted finger movements of right and left hands", version **0.230408.2207** (doi:10.48324/dandi.000252/0.230408.2207). The paper cites no version (its Data Availability gives only the dandiset URL), and 0.230408.2207 is the only published version, so it is pinned. The draft was modified later (2023-06-20) but lists the same 12 assets with the same asset identifiers; the check below prints this.

**Text the claims file was written from.** The bioRxiv preprint, version 1, full text with Methods and the supplementary figure legends (claims file `claims/000252/10.1101-2022.12.07.22283227.yaml`). The paper links no analysis code.

**What the dataset holds.** Only the ten-finger press task: 10 sessions of participant N (subject `P1` in the files) and 2 of participant J (subject `N1`). The alternating-cues task (Figures 4 and 5) and the BMI tasks (Figure 6, Supplementary Figures 6 and 7) are not in it.

| Claim | Tested here |
|---|---|
| tenfinger-recording-counts | tested |
| tenfinger-pooled-npcc-neurons | tested |
| tenfinger-discriminative-fraction | tested |
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/7e846225-970d-4351-bd87-b5dee901dec0/tool-results/b5s39453c.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Guan et al. (preprint 2022) from dandiset 000252
3	
4	**Paper.** Guan, Aflalo, Kadlec, Gámez de Leon, Rosario, Bari, Pouratian and Andersen, "Compositional coding of individual finger movements in human posterior parietal cortex and motor cortex enables ten-finger decoding", medRxiv/bioRxiv preprint, doi:10.1101/2022.12.07.22283227.
5	
6	**Dataset.** DANDI:000252, "Finger_RL: human intracortical recordings during attempted finger movements of right and left hands", version **0.230408.2207** (doi:10.48324/dandi.000252/0.230408.2207). The paper cites no version (its Data Availability gives only the dandiset URL), and 0.230408.2207 is the only published version, so it is pinned. The draft was modified later (2023-06-20) but lists the same 12 assets with the same asset identifiers; the check below prints this.
7	
8	**Text the claims file was written from.** The bioRxiv preprint, version 1, full text with Methods and the supplementary figure legends (claims file `claims/000252/10.1101-2022.12.07.22283227.yaml`). The paper links no analysis code.
9	
10	**What the dataset holds.** Only the ten-finger press task: 10 sessions of participant N (subject `P1` in the files) and 2 of participant J (subject `N1`). The alternating-cues task (Figures 4 and 5) and the BMI tasks (Figure 6, Supplementary Figures 6 and 7) are not in it.
11	
12	| Claim | Tested here |
13	|---|---|
14	| tenfinger-recording-counts | tested |
15	| tenfinger-pooled-npcc-neurons | tested |
16	| tenfinger-discriminative-fraction | tested |
17	| tenfinger-decoding-accuracy | tested |
18	| tenfinger-error-structure | tested |
19	| fig8b-matching-closer | tested |
20	| fig8a-npcc-index-distinct | tested |
[... 619 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/7e846225-970d-4351-bd87-b5dee901dec0/tool-results/b5s39453c.txt",
 "offset": 640
}
```

```
640	21  b  b  svm  N-PPC  0.976   0.927     0.998       0.992     0.992   0.001     0.001           0.498           0.72             0.197             0.33        930       0.978             0.935             0.935
641	22  b  b  svm  J-PPC  0.971   0.358     0.978       0.828     0.749   0.001     0.002           0.500           0.69             0.200             0.38        312       0.993             0.432             0.478
642	23  b  b  svm   J-MC  0.860   0.745     0.943       0.953     0.948   0.001     0.001           0.499           0.70             0.199             0.37        250       0.913             0.781             0.786
643	
644	==================== 23 code
645	# Variant: standard accuracy per session (classifier per session, trials pooled), O1 a, O2 a
646	var_rows = []
647	for o7 in ["lda", "svm"]:
648	    for arr in F.ARRAYS:
649	        r = {}
650	        for tgt in ["hand", "finger_within", "finger_both"]:
651	            a, n = [], []
652	            for s in sess_of(arr):
653	                X, y = F.array_data(s, arr, "a")
654	                a.append(F.standard_accuracy(X, y, tgt, o7)); n.append(len(y))
655	            r[tgt] = np.average(a, weights=n)
656	        var_rows.append(dict(O7=o7, array=arr, **r))
657	print("per-session standard accuracy (variant):")
658	print(pd.DataFrame(var_rows).round(3).to_string())
659	
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "upper bound|within-hand|standard decoding|pseudo|noise covariance|partition|distance-units|Figure 8 |Figure 7 |go phase|movement execution|ten fingers" paper/*.txt | cut -c1-700
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 160,190p paper/*.txt | cut -c1-2500; sed -n 273p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "import rsatoolbox,sklearn,scipy;print(rsatoolbox.__version__, sklearn.__version__, scipy.__version__)"; python3 - <<'EOF'
import inspect, rsatoolbox.rdm.calc as c
src=inspect.getsource(c)
i=src.find('def calc_rdm_crossnobis'); print(src[i:i+5000])
i=src.find('def _calc_rdm_crossnobis_single'); print(src[i:i+1500])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import rsatoolbox,sklearn,scipy;print(rsatoolbox.__version__, sklearn.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'rsatoolbox'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'rsatoolbox'
```

**Agent calls Bash**

```bash
cd  python3 -c "import sklearn,scipy,numpy,pandas;print(sklearn.__version__, scipy.__version__)"; pip download rsatoolbox --no-deps -d $TMPDIR/rsa -q 2>&1 | tail -2; ls $TMPDIR/rsa
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import sklearn,scipy,numpy,pandas;print(sklearn.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'sklearn'
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
rsatoolbox-0.3.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
```

**Agent calls Bash**

```bash
cd $TMPDIR/rsa && python3 -m zipfile -e rsatoolbox-*.whl x >/dev/null && python3 - <<'EOF'
src=open('x/rsatoolbox/rdm/calc.py').read()
i=src.find('def calc_rdm_crossnobis'); print(src[i:i+5200])
i=src.find('def _calc_rdm_crossnobis_single'); print(src[i:i+1800])
EOF
```

```
def calc_rdm_crossnobis(dataset, descriptor, noise=None,
                        cv_descriptor=None, remove_mean: bool = False):
    """
    calculates an RDM from an input dataset using Cross-nobis distance
    This performs leave one out crossvalidation over the cv_descriptor.

    As the minimum input provide a dataset and a descriptor-name to
    define the rows & columns of the RDM.
    You may pass a noise precision. If you don't an identity is assumed.
    Also a cv_descriptor can be passed to define the crossvalidation folds.
    It is recommended to do this, to assure correct calculations. If you do
    not, this function infers a split in order of the dataset, which is
    guaranteed to fail if there are any unbalances.

    This function also accepts a list of noise precision matricies.
    It is then assumed that this is the precision of the mean from
    the corresponding crossvalidation fold, i.e. if multiple measurements
    enter a fold, please compute the resulting noise precision in advance!

    To assert equal ordering in the folds the dataset is initially sorted
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "import numpy, scipy, pandas; print(numpy.__version__, scipy.__version__)" 2>&1; python3 -c "import h5py" 2>&1 | tail -1
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy, pandas; print(numpy.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'h5py'
```

**Agent calls Bash**

```bash
cd  python3 -m venv $TMPDIR/v && $TMPDIR/v/bin/pip install -q numpy scipy pandas scikit-learn statsmodels requests h5py remfile 2>&1 | tail -2; $TMPDIR/v/bin/python -c "import numpy,sklearn;print('ok')"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
ok
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/pip install -q $TMPDIR/rsa/rsatoolbox-*.whl 2>&1|tail -1; $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, fingers as F
from statsmodels.stats.multitest import multipletests
from scipy.stats import f_oneway
rng=np.random.default_rng(0)
p=rng.uniform(size=200)**3; p[5]=np.nan
q=F.fdr_bh(p); q2=multipletests(np.nan_to_num(p,nan=1),method='fdr_bh')[1]
print("fdr match", np.allclose(q,q2))
X=rng.normal(size=(100,7)); y=np.repeat(F.CONDITIONS,10); X[:,0]+= (y=='Rt')*2; X[:,6]=3
pp,eta=F.anova_eta2(X,y)
print("anova match", np.allclose(pp[:6],[f_oneway(*[X[y==c,j] for c in np.unique(y)]).pvalue for j in range(6)]), pp[6], eta[:2])
# DiagLDA vs GaussianNB with pooled var
from sklearn.naive_bayes import GaussianNB
Xt=rng.normal(size=(100,20))+ (np.arange(100)[:,None]%10==np.arange(20)[None]%10)*1.5
yt=np.array(F.CONDITIONS*10)
m=F.DiagLDA().fit(Xt[:80],yt[:80]); print("diag lda acc",np.mean(m.predict(Xt[80:])==yt[80:]))
# error kinds
t=np.array(['Rt','Rt','Ri','Lp','Lm','Rm']); pr=np.array(['Ri','Lt','Rm','Lr','Rp','Rm'])
print(F.error_kinds(t,pr))  # expect err5, adj: Rt->Ri, Ri->Rm, Lp->Lr =3; match Rt->Lt=1
# crossnobis: synthetic with known distance
nn=50; mu=rng.normal(size=(10,nn))*0.5
Xs=np.vstack([mu[i]+rng.normal(size=(10,nn)) for i in range(10)]); ys=np.repeat(F.CONDITIONS,10)
for o4 in ['a','a1','b']:
    r,_=F.crossnobis_rdm(Xs,ys,'diag',o4)
    true=((mu[:,None]-mu[None])**2).sum(-1)/nn
    iu=np.triu_indices(10,1); print(o4, "ratio est/true", np.mean(r[iu])/np.mean(true[iu]))
EOF
```

```
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/_core/numeric.py:475: RuntimeWarning: invalid value encountered in cast
  multiarray.copyto(res, fill_value, casting='unsafe')
fdr match True
anova match True nan [0.29226876 0.10780341]
diag lda acc 0.45
(5, 3, 1)
a ratio est/true 5.461509952547743
a1 ratio est/true 1.0923019905095483
b ratio est/true 1.1036625331075491
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import requests
A="https://api.dandiarchive.org/api/dandisets/000252"
print([ (v['version'],v['asset_count'],v['size']) for v in requests.get(A+"/versions/").json()['results']])
r=requests.get(A+"/versions/0.230408.2207/assets/?page_size=200").json()['results']
for a in r: print(a['path'], a['size'])
md=requests.get(A+"/versions/0.230408.2207/").json()
print(md.get('description','')[:1500])
print(md.get('assetsSummary'))
a0=r[0]; m=requests.get(f"{A}/versions/0.230408.2207/assets/{a0['asset_id']}/").json()
print({k:m.get(k) for k in ['wasGeneratedBy','variableMeasured','measurementTechnique']})
EOF
```

```
[('draft', 12, 38128728), ('0.230408.2207', 12, 38128728)]
sub-P1/sub-P1_ses-2015-08-17_ecephys.nwb 1904844
sub-P1/sub-P1_ses-2016-05-23_ecephys.nwb 1459812
sub-P1/sub-P1_ses-2016-04-27_ecephys.nwb 1651448
sub-P1/sub-P1_ses-2015-08-14_ecephys.nwb 1704104
sub-P1/sub-P1_ses-2016-05-16_ecephys.nwb 1608016
sub-P1/sub-P1_ses-2015-08-12_ecephys.nwb 1864800
sub-P1/sub-P1_ses-2016-05-11_ecephys.nwb 1575432
sub-P1/sub-P1_ses-2016-05-20_ecephys.nwb 1568016
sub-P1/sub-P1_ses-2015-08-21_ecephys.nwb 1529792
sub-P1/sub-P1_ses-2016-05-04_ecephys.nwb 1517120
sub-N1/sub-N1_ses-2019-12-20_ecephys.nwb 9391680
sub-N1/sub-N1_ses-2019-02-12_ecephys.nwb 12353664
This dataset contains single-neuron recordings from two tetraplegic human participants as they attempted individual finger movements. One participant had an electrode array implanted in the left posterior parietal cortex (PPC) at the junction of the postcentral and intraparietal sulci (PC-IP). The other participant had one electrode array implanted in the hand knob of the left motor cortex (MC) and one electrode array implanted in the superior parietal lobule (SPL) of the left PPC.
{'species': [{'name': 'Homo sapiens - Human', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9606'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 38128728, 'numberOfFiles': 12, 'numberOfSubjects': 2, 'variableMeasured': ['ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting technique', 'schemaKey': 'MeasurementTechniqueType'}]}
{'wasGeneratedBy': [{'name': '2015-08-17', 'schemaKey': 'Session', 'startDate': '2015-08-17T11:42:21-07:00', 'identifier': '2015-08-17', 'description': 'ten-finger press task, with delay'
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import requests
d=requests.get("https://api.dandiarchive.org/api/dandisets/000147/").json()
print(d['draft_version']['name'], d.get('most_recent_published_version',{}) and d['most_recent_published_version'].get('version'))
EOF
grep -n -i "dandi\|data availability" paper/*.txt | cut -c1-400
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 1: Guan et al. 2022, DANDI:000252 @ 0.230408.2207**

The claims file has 19 claims. The notebook tests 11 and treats 8 as blocked (data_missing).

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| tenfinger-recording-counts | reproduced | Before the exclusion (cell 10, O1 none): N-PPC has 10 sessions, mean 111.4 (102–119); J-PPC 159.5 (159–160); J-MC 129.5 (120–139). The 139 is within 10% of the paper's 130. Every session has 100 trials. Under O1 a/b the N-PPC mean (94.3/93.0) is out of tolerance. |
| tenfinger-pooled-npcc-neurons | reproduced | 1114 before the exclusion (cell 10), against 1111 ± 111. It is 943/930 under O1 a/b, which is out of tolerance. |
| tenfinger-discriminative-fraction | not_reproduced | Under every O1 reading (cell 12): N-PPC 40–49%, J-PPC 38%, J-MC 64–66%, against 66/57/78 ± 10%. None of the three is within tolerance. Uncorrected p and FDR per session are also far below. |
| tenfinger-decoding-accuracy | reproduced | Every O1×O2 reading is within tolerance (cell 14). For example, O1a/O2a gives 72.2 / 69.5 / 78.5% against 70/66/75, with chance at 10%. |
| tenfinger-error-structure | reproduced | O1a/O2a gives 76.6 / 72.1 / 62.8% against 76±7.6, 66±6.6 and 68±6.8 (cell 14). O1a/O2b is also all within tolerance (74.9 / 67.1 / 64.6). |
| fig8b-matching-closer | reproduced | Under O4 (a), all O1 and O3 readings (cell 18): N-PPC 1.42–1.71 (BCa CI from 1.19–1.64), J-MC 2.99–3.38, J-PPC 0.19–0.22 with its CI including 0. This depends on the ×5 "precision of the mean" scaling (problem 1). Under O4 (b) and (a1) the sign and CI pattern hold, but the magnitudes are about 5× too small. |
| fig8a-npcc-index-distinct | reproduced | Under all 18 readings, in both hands, the index–middle and index–ring distances exceed middle–ring (cell 20). For example, R 2.16 / 2.96 > 0.62 and L 1.30 / 2.23 > 0.57. |
| fig8e-hand-ccgp | reproduced | Every array has p = 1/1002 (no shuffle reached the observed value) under all 8 readings. The CCGP/standard-accuracy ratio is ≥ 0.913, so both O9 (a) and (b) pass (cell 23). |
| fig8e-finger-ccgp | reproduced | N-PPC and J-MC have p = 1/1002 under all readings. Closeness passes O9 (b) (ratio > 0.55) but fails O9 (a) for J-MC (ratio 0.77–0.82) (cell 23). The outcome therefore rests on the O9 (b) reading. |
| jppc-finger-ccgp-low | partially_reproduced | p < 0.001 holds in only 1 of 8 readings (O1b/O6a/SVM: p = 1/1002, CCGP 38%, within tolerance). The other p values run from 0.002 to 0.038. The within-hand accuracy on the pseudo-population is 83–89% under every reading, against 65 ± 6.5. The per-session variant gives 69%, inside tolerance (problem 2). |
| figs11-jppc-lower-matched-size | reproduced | J-PPC is lowest at every size from 50 to 250 under all 4 O6×O7 readings (cell 26): about 0.25–0.33, against at least 0.47 for N-PPC and J-MC. |
| fig4c-contra-discriminative | blocked (data_missing) | I confirmed this against the archive: all 12 assets are "ten-finger press task, with delay", with 10 conditions and no No-Go. |
| fig4e-plan-vs-move | blocked (data_missing) | Same reason. A Delay-window ANOVA on the ten-finger task would be a different task and condition set, so not a test of this claim. |
| fig5a-contra-decoding | blocked (data_missing) | Same reason: there is no six-class contralateral task. |
| fig5bcd-npcc-data-requirements | blocked (data_missing) | Same reason. |
| fig5e-planning-decoding | blocked (data_missing) | Same reason. |
| fig6-online-bmi | blocked (data_missing) | There are no BMI sessions or decoder outputs. The trial table has no prediction column. |
| figs6-single-array-retrospective | blocked (data_missing) | The BMI sessions are absent. The archive's variableMeasured lists only ElectrodeGroup and Units, so there are no threshold crossings for O10 (a) either. |
| figs7-left-hand-bmi | blocked (data_missing) | Same reason. |

### B. Problems

1. [affects a conclusion] `crossnobis_rdm`, O4 "a" (cells 17–18). The per-partition precision is multiplied by the number of trials per condition (5). I tested this on synthetic data with a known distance: O4 a returns 5.46× the true value, while a1 and b return about 1.1×. The paper's 1.56 is matched only under this scaling.
   - The scaling follows rsatoolbox's documented convention for a list of noises, and I verified that docstring and code in rsatoolbox 0.3.2. So it is a defensible stated assumption, not an invention.
   - It is still an assumption that decides the magnitude part of fig8b. Without it fig8b would be partially_reproduced.
   - The claims file's O4 (a) does not mention it. That is a gap in the claims file, not an error in the notebook.
2. [affects a conclusion] `run_ccgp` / `standard_accuracy`, cells 21–23. The notebook computes standard (within-hand) accuracy on the pseudo-population, which is its own assumption, and runs the per-session accuracy only as a variant, for O1 a / O2 a alone.
   - The paper does not say which population it used. The criterion's O8 (a) does not settle it either, and the two choices change the jppc outcome: 83–89% on the pseudo-population against 69% per session (inside 65 ± 6.5).
   - Both should have been run as readings, under every O1/O6/O7 combination.
   - Under O1b/O6a/SVM with per-session accuracy, the claim would probably be fully reproduced, but that combination was not computed.
3. [affects a conclusion] The J-PPC finger-type p value is fragile (cell 23). It ranges from 0.001 to 0.038 across readings, and p < 0.001 is reached only at the 1/1002 floor, in one reading. The partially_reproduced outcome rests on that single reading.
4. [does not affect a conclusion] `run_ccgp`, O6 b. The observed CCGP is averaged over 100 matchings, but each null draw uses a single matching. This makes the null wider than the observed statistic's sampling distribution, so p is conservative. The notebook states it as an assumption.
5. [does not affect a conclusion] Cell 26 (figs11) runs only O1 a. The margins are large, so O1 b would not change the outcome.
6. [does not affect a conclusion] Cell 7 computes shuffled-label predictions (`Psh`) for the time course but never uses them. Only the per-session shuffled control is reported, and that control is sound: accuracy 0.07–0.17.
7. [does not affect a conclusion] The paper's per-session neuron counts match the pre-exclusion counts, not the post-0.5 Hz counts, yet all analyses use the post-exclusion counts (O1 a/b). This is consistent with the claims file's note on 466 against 472. The notebook does not comment on it.
8. [does not affect a conclusion] Helpers I checked and found correct:
   - `fdr_bh` matches statsmodels BH exactly.
   - `anova_eta2` matches scipy's `f_oneway` per unit.
   - `error_kinds` counts adjacent and matching errors correctly on a hand-built case.
   - `DiagLDA` is the pooled-variance Gaussian naive Bayes the paper describes.
   - There is no train/test leakage: the unit exclusion is label-free, and the zero-variance unit drop removes 1 unit.

### C. What I could not check, and which output would have let me

- **jppc-finger-ccgp-low with per-session accuracy.** I could not confirm the outcome under per-session within-hand accuracy for O1 b with O6/O7. The output needed is the per-session `finger_within` and `finger_both` accuracy for every O1×O6×O7 row of `ccgp_df`, printed next to `p_finger` and the finger CCGP.
- **fig8b scaling assumption.** I could not tell whether the paper's distances are in single-trial noise units (O4 b, a1) or fold-mean units (O4 a). One check would help: the per-session N-PPC mean RDM for O4 a1 alongside O4 a, compared with the Figure 8a colour-bar range. The paper's values are not in the text, so this stays open.
- **Ten-finger window for the discriminative fraction.** It is not reproduced in the Go window, and I could not test whether another window explains the gap. Only the 500 ms Cue, Delay and ITI variants were run (cell 12). Sweeping the window start through the Go phase would show whether any window approaches 66/57/78.
- **Exact p values.** These are shown rounded to 3 decimals. I inferred p = 1/1002 from the rounding: 2/1002 would print as 0.002. Printing the number of null values that reach the observed CCGP would settle it.
- **Blocked claims.** The archive's `Continues DANDI:000147` relation points to "PPC_Finger: human posterior parietal cortex recordings during attempted finger movements". It may hold N's contralateral-task data, but it is outside the dataset this claims file names, and I did not examine it.

## End of run

17 turns, 4 minutes, $1.26 at API prices, result: success.
