# sabatini-2024 · verifier-2 · run 46113624976

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 772
drwxr-xr-x 6 runner runner    4096 Nov 28 07:09 .
drwxr-xr-x 8 runner runner    4096 Nov 28 07:09 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 28 05:45 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 28 05:45 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 28 07:09 .claude
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .env
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .env.development
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .env.local
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .env.production
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .env.test
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .env.test.local
drwx------ 2 runner runner    4096 Nov 28 07:09 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 28 05:45 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 28 05:45 .github
-rw-r--r-- 1 runner runner       0 Nov 28 07:08 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 28 05:45 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 28 05:45 .mcp.json
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -50 sabatini-2024.yaml; echo ----; head -80 sabatini-2024-02.yaml; grep -c "" sabatini-2024*.yaml
```

```
# Sabatini and Kaufman (2024) on DANDI:000070

Tests the findings of [Sabatini and Kaufman (2024)](https://doi.org/10.1038/s41467-024-51308-7),
"Reach-dependent reorientation of rotational dynamics in motor cortex", on
[DANDI:000070](https://dandiarchive.org/dandiset/000070/0.261122.2046) version 0.261122.2046, using the
two maze sessions the paper names (monkey J 2009-09-18, monkey N 2010-09-23). Four datasets are analysed
separately: M1-J, PMd-J, M1-N, PMd-N.

- `reproduce_sabatini_2024.ipynb`: data check, temporal basis factorization, single-condition dynamics,
  jPCA and the geometry of the rotations.
- `reproduce_sabatini_2024_kinematics.ipynb`: prediction of rotations, LDR encoding and single-trial LDR
  decoding.
- `ldr.py`: loading (streamed from the archive) and the measures, with the source of each parameter.

| Claims | Outcome |
|---|---|
| Factorization variance, shuffle control, recoverability; jPCA variance; single-condition LDS; location distinct from rotations; rotation and location prediction; location tracks direction; LDR encoding, its controls and decoding | Reproduced |
| Data composition; basis frequencies; jPCA R2; plane alignment and its jPCA link; frequency segregation; excursion angles; location alignment; kinematics predict location; curvature decoding; decoder comparison of Figure 7f (all but GPFA) | Partially reproduced |
| Duration warping; single LDS; eigenvalue clusters and distances; eigenvalues from kinematics; model comparison; jPCA variance correlation; orientation and location dimensionality; no output-potent dependence | Not reproduced |

[... 141 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "sabatini-2024-02.yaml",
 "offset": 80,
 "limit": 500
}
```

```
80	  outcome: reproduced
81	  notebook: reproduce_sabatini_2024.ipynb
82	  output: claim:jpca-variance-explained
83	  notes: Activity in the retained jPCA planes holds 9.1%, 10.6%, 10.8% and 6.8% of the variance (s.d. 5.3 to 8.5% across conditions),
84	    all inside 6.3 to 13.2% (6.4% to 11.4% on the offline onset). With the cross-condition mean added back to the reconstruction
85	    it would be 71.6% to 80.9%. Units are unsorted threshold crossings (see data-composition).
86	  deviations:
87	  - jPCA implemented from its description (see jpca-fit-r2).
88	  - Trials are aligned on the file's move_begins_time, its movement onset time; the paper says only aligned to movement onset
89	    (Methods, Subjects, behavior and data pre-processing). The offline onset in the file is 25 ms (J) and 52 ms (N) earlier
90	    in the median. Assumption, as the online onset is the one the file names movement onset. The claims whose numbers depend
91	    most on the onset (fig3g, tbf-variance-explained, the jPCA claims, single-lds-variance, fig2c, fig3a, fig3i, rotation-orientation-dimensionality)
92	    were recomputed on offline_move_onset_time (notebook 1, cell variant-offline-onset) and keep their outcomes.
93	  - The units are the dataset's unsorted threshold crossings, all 96 per array, where the paper used sorted single units and
94	    stable multi-units (Methods, Subjects, behavior and data pre-processing).
95	- claim: single-lds-variance
96	  outcome: not_reproduced
97	  notebook: reproduce_sabatini_2024.ipynb
98	  output: claim:single-lds-variance
99	  notes: A single LDS over all conditions explains 77.3%, 81.3%, 82.6% and 78.6% from -150 ms on (79.6% to 86.5% over the
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "sabatini-2024-02.yaml",
 "offset": 580,
 "limit": 490
}
```

```
580	    92.9% and 88.0% (inside 63.9 to 95.7%), against nulls of 42.2% to 62.7%, with signed-rank p < 0.0001, under both kinematic
581	    bases and the other seeds. The kernel result holds at every OU length scale from 10 to 10^4 (80.8% to 92.9%, reading svd),
582	    so it does not rest on the scale of the reach parameters. Units are unsorted threshold crossings (see data-composition).
583	  deviations:
584	  - Reach parameters as the least-squares coefficients of the condition's hand path on two kinematic basis functions, the
585	    top two velocity singular vectors over all conditions of both sessions integrated to position (reading svd) or their skew-normal
586	    fits (reading skewnormal; paper, Methods, Extracting kinematic basis functions); results are shown under both.
587	  - Hand positions are taken relative to each trial's position at -350 ms before the reach parameters are fitted. The code
588	    regresses the positions on the basis without an intercept (predictDataUsingTBFandKinCondStructure.m) and the paper does
589	    not say where the origin is; the basis functions start at zero, so the start is subtracted. Assumption.
590	  - Trials are aligned on the file's move_begins_time, its movement onset time; the paper says only aligned to movement onset
591	    (Methods, Subjects, behavior and data pre-processing). The offline onset in the file is 25 ms (J) and 52 ms (N) earlier
592	    in the median. Assumption, as the online onset is the one the file names movement onset. The claims whose numbers depend
593	    most on the onset (fig3g, tbf-variance-explained, the jPCA claims, single-lds-variance, fig2c, fig3a, fig3i, rotation-orientation-dimensionality)
594	    were recomputed on offline_move_onset_time (notebook 1, cell variant-offline-onset) and keep their outcomes.
595	  - The units are the dataset's unsorted threshold crossings, all 96 per array, where the paper used sorted single units and
596	    stable multi-units (Methods, Subjects, behavior
[... 467 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
for nb in ['reproduce_sabatini_2024.ipynb','reproduce_sabatini_2024_kinematics.ipynb']:
    d=json.load(open(nb))
    out=open('/tmp/claude/'+nb+'.txt' if False else nb+'.dump.txt','w') if False else None
    import os
    p=os.environ.get('TMPDIR','/tmp/claude')+'/'+nb+'.txt'
    with open(p,'w') as f:
        for i,c in enumerate(d['cells']):
            f.write(f"\n===== CELL {i} [{c['cell_type']}] id={c.get('id')} tags={c.get('metadata',{}).get('tags')}\n")
            f.write(''.join(c['source'])+'\n')
            for o in c.get('outputs',[]):
                if 'text' in o: f.write('--- OUT:\n'+''.join(o['text']))
                elif 'data' in o:
                    if 'text/plain' in o['data'] and 'image/png' not in o['data']: f.write('--- OUT:\n'+''.join(o['data']['text/plain'])+'\n')
                    elif 'image/png' in o['data']: f.write('--- [image]\n')
                elif o.get('output_type')=='error': f.write('--- ERROR '+o['ename']+': '+o['evalue']+'\n')
    print(p, len(d['cells']))
EOF
wc -l $TMPDIR/*.txt
```

```
/tmp/claude-1001/reproduce_sabatini_2024.ipynb.txt 90
/tmp/claude-1001/reproduce_sabatini_2024_kinematics.ipynb.txt 46
  1752 /tmp/claude-1001/reproduce_sabatini_2024.ipynb.txt
  1204 /tmp/claude-1001/reproduce_sabatini_2024_kinematics.ipynb.txt
  2956 total
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_sabatini_2024.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] id=c000 tags=None
3	# Sabatini & Kaufman (2024) on DANDI:000070: dynamics (notebook 1 of 2)
4	
5	Paper: D. A. Sabatini and M. T. Kaufman, "Reach-dependent reorientation of rotational dynamics in
6	motor cortex", Nat. Commun. 15:7007 (2024), doi:10.1038/s41467-024-51308-7. The claims file
7	(`claims/sabatini-2024.yaml`) was written from the version of record (PMC11325044) and its
8	supplement.
9	
10	Dataset: DANDI:000070, "Neural population dynamics during reaching", version **0.261122.2046**
11	(doi:10.48324/dandi.000070/0.261122.2046). The paper cites the dandiset without a version (it was
12	published in August 2024, before the first published version of December 2025), so the most recent
13	published version is pinned. The two sessions the paper's Data availability statement names are read:
14	`sub-Jenkins_ses-20090918` and `sub-Nitschke_ses-20100923`. The file names of this version match the
15	paper's (the Nitschke date is 2010 in both).
16	
17	This notebook tests the claims on the temporal basis factorization (TBF), single-condition dynamics,
18	jPCA and the geometry of the rotations. Notebook 2 (`reproduce_sabatini_2024_kinematics.ipynb`) tests
19	the claims on prediction, encoding and decoding.
20	
[... 607 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_sabatini_2024.ipynb.txt",
 "offset": 628,
 "limit": 560
}
```

```
628	    print(f"{n}: basis of the normalised data, rotation frequencies {np.round(sorted(set(np.round(tn['freq'][inds], 2))), 2)} Hz "
629	          f"(original basis {np.round(sorted(set(np.round(TBF[n]['freq'][TBF[n]['freq'] > 0], 2))), 2)})")
630	def code_rot_act(n, c):
631	    tb, r = TBF[n], ROT[n]
632	    inds = np.where(tb["freq"] > 0)[0]
633	    ok = ~np.isnan(tb["B"][:, 0])
634	    meanL = tb["L"].mean(0)
635	    return r["sn"][:, None] * ((tb["L"][c][:, inds] - meanL[:, inds]) @ tb["B"][ok][:, inds].T)
636	F4D = []
637	for n in NAMES:
638	    r = ROT[n]
639	    rv = {"a": np.array([a.var(1, ddof=1).sum() for a in NORM[n]["act"]]),
640	          "b": np.array([np.nansum(np.var(code_rot_act(n, c), axis=1, ddof=1)) for c in range(72)])}
641	    for p in range(PLANES[n]):
642	        jv = np.nansum(np.nanvar(r["rot"][:, 2 * p:2 * p + 2], axis=2, ddof=1), axis=1)
643	        for basis in ("a", "b"):
644	            rr = stats.pearsonr(jv, rv[basis])
645	            F4D.append(dict(basis=basis, dataset=n, plane=p + 1, rho=rr[0], p=rr[1]))
646	F4D = pd.DataFrame(F4D)
647	print(F4D.round(4).to_string(index=False))
[... 540 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_sabatini_2024.ipynb.txt",
 "offset": 1188,
 "limit": 570
}
```

```
1188	        den = (Dc ** 2).sum()
1189	        for j in range(72):
1190	            Q = np.linalg.qr(L[j][:, inds2])[0]
1191	            r = Dc - Q @ (Q.T @ Dc)
1192	            out[i, j] = max(0, 1 - (r ** 2).sum() / den)
1193	    return out
1194	
1195	GEO = {}
1196	T = time.time()
1197	NOISE = {(n, k): noise_loadings(DS[n], TBF[n], ldr.rng("fig4b-plane-alignment", k), 36)
1198	         for n in NAMES for k in SEED_OFFSETS}
1199	for n in NAMES:
1200	    tb = TBF[n]
1201	    gr = ldr.groups(tb)
1202	    L1, L2 = NOISE[(n, 0)]
1203	    ok = ~np.isnan(tb["B"][:, 0])
1204	    comps = {}
1205	    for f, inds in gr:
1206	        obs = ai_matrix(tb["L"], tb["B"], inds)
1207	        noise = np.array([[ldr.alignment_index(L1[r, c][:, inds] @ tb["B"][ok][:, inds].T, L2[r, c][:, inds])
[... 546 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_sabatini_2024_kinematics.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] id=c000 tags=None
3	# Sabatini & Kaufman (2024) on DANDI:000070: prediction, encoding and decoding (notebook 2 of 2)
4	
5	Paper: doi:10.1038/s41467-024-51308-7; dataset DANDI:000070 version 0.261122.2046 (the most recent
6	published version; the paper cites none), sessions `sub-Jenkins_ses-20090918` and
7	`sub-Nitschke_ses-20100923` as named in the paper's Data availability statement. The claims file was written
8	from the version of record and its supplement. Notebook 1 holds the data check and the claims on the
9	factorization and dynamics; this one recomputes the factorization (the same cross-validation, seed and k)
10	and tests:
11	
12	| claim | here |
13	|---|---|
14	| fig5c-rotations-predict-rotations, fig6b-location-predicts-rotations, fig6c-location-tracks-direction, fig6e-kinematics-predict-location, fig7c-ldr-encoding, suppfig7a-not-memorization, fig7c-standard-encoding-worse, fig7f-ldr-decoding, trial-curvature-decoding, suppfig8-no-output-potent-dependence | tested |
15	| fig7f-decoder-beats-standard | tested here, without the GPFA decoders |
16	
17	===== CELL 1 [code] id=c001 tags=None
18	import time, resource, warnings
19	import numpy as np
20	import pandas as pd
[... 663 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_sabatini_2024_kinematics.ipynb.txt",
 "offset": 684,
 "limit": 530
}
```

```
684	PMd-J (svd): kernel 78.2%, nearest neighbour 71.6%, signed-rank p = 0.00015; kernel higher with p < 0.01: True
685	--- OUT:
686	PMd-J (skewnormal): kernel 80.2%, nearest neighbour 72.3%, signed-rank p = 6.3e-07; kernel higher with p < 0.01: True
687	--- OUT:
688	M1-N (svd): kernel 88.8%, nearest neighbour 82.3%, signed-rank p = 3.4e-12; kernel higher with p < 0.01: True
689	--- OUT:
690	M1-N (skewnormal): kernel 88.6%, nearest neighbour 82.4%, signed-rank p = 1.8e-11; kernel higher with p < 0.01: True
691	--- OUT:
692	PMd-N (svd): kernel 79.8%, nearest neighbour 70.5%, signed-rank p = 4.3e-11; kernel higher with p < 0.01: True
693	--- OUT:
694	PMd-N (skewnormal): kernel 79.6%, nearest neighbour 72.6%, signed-rank p = 9.6e-12; kernel higher with p < 0.01: True
695	
696	===== CELL 25 [markdown] id=c025 tags=None
697	**Result: reproduced.** With sextants held out, kernel encoding (78.2% to 88.8%) beats nearest-neighbour regression (70.5% to 82.4%) in every dataset under both kinematic bases, with p from 3.4e-12 to 1.5e-4.
698	
699	===== CELL 26 [markdown] id=c026 tags=None
700	## fig7c-standard-encoding-worse
701	> Standard instantaneous encoding models (linear multi-parameter, kernel regression on position, kernel
702	> regression on velocity) were substantially outperformed by both linear and nonlinear LDR encoding.
703	
[... 502 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  id:\|^    id:" sabatini-2024.yaml | head -50; grep -c "^- id:" sabatini-2024.yaml
```

```
80:- id: data-composition
103:- id: jpca-fit-r2
128:- id: jpca-variance-explained
143:- id: single-lds-variance
156:- id: fig2c-condition-lds-variance
172:- id: fig3a-eigenvalue-clusters
188:- id: fig3c-eigenvalue-distance-auc
208:- id: suppfig2-eigenvalues-from-kinematics
230:- id: fig3g-basis-frequencies
244:- id: tbf-variance-explained
256:- id: tbf-shuffle-control
275:- id: fig3h-recoverability
296:- id: fig3i-duration-warping
331:- id: suppfig3-model-comparison
347:- id: fig4b-plane-alignment
372:- id: fig4c-subspace-excursion-angles
388:- id: rotation-orientation-dimensionality
405:- id: fig4d-jpca-variance-correlation
429:- id: fig4f-plane-alignment-explains-jpca
447:- id: fig5a-frequencies-segregated
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk 'NR<755' sabatini-2024-02.yaml | grep -c "^- claim:"; awk 'NR<755' sabatini-2024-02.yaml | grep -A1 "^- claim:" | grep outcome: | sort | uniq -c; sed -n 50,80p sabatini-2024.yaml; sed -n 296,346p sabatini-2024.yaml; sed -n 690,740p sabatini-2024.yaml
```

```
34
     10   outcome: not_reproduced
     11   outcome: partially_reproduced
     13   outcome: reproduced
#   curved condition's target and barrier with a distractor added. The author reports how many of
#   36 straight and 36 curved each gives.
# - Trials. The paper gives no trial selection beyond the task; readings are (a) all successful
#   trials of the 72 conditions, (b) successful trials with a delay above 400 ms as in the original
#   studies. The counts are compared with 1469 and 2014.
# - Temporal basis factorization (TBF). SVD of the (neurons x conditions)-by-time matrix of
#   condition-averaged rates; top k temporal singular vectors are the basis functions, k by
#   cross-validation over two halves of the trials, 100 folds, maximising held-out variance
#   explained (code crossValidateDimensionalityBasisFxns.m tests k = 1 to 20 and raises an even k
#   by one); de-mixed by fitting an LDS to the basis functions and projecting onto its
#   eigenvectors (code eigTransform.m, which then replaces the basis by damped sinusoids of the
#   fitted frequencies and half-lives). getBasisFxns.m computes max-normalised rates but runs the
#   SVD on the unnormalised ones; the unnormalised SVD is the code's choice.
# - Population variance explained, per condition, is 1 minus the summed variance over neurons of
#   the residual over the summed variance of the data, negative values set to 0 (code
#   getVarExplained.m). Reported means and s.d. are across conditions.
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 80,128p sabatini-2024.yaml; sed -n 230,244p sabatini-2024.yaml; sed -n 405,447p sabatini-2024.yaml; sed -n 491,508p sabatini-2024.yaml
```

```
- id: data-composition
  statement: Two monkeys (J and N) performed the maze task with 72 conditions (36 straight, 36
    curved); a PMd and an M1 array in each monkey gave 79 to 118 units per array; 1469 trials for
    monkey J and 2014 for monkey N.
  source: Results, paragraph 1; Methods, Subjects, behavior and data pre-processing; Figure 7 legend
  quote: We refer to the 72 unique combinations of target and virtual barrier positions as
    "conditions". Simultaneous single- and multi-unit electrophysiological recordings were made
    with a pair of 96-electrode Utah arrays in each monkey, implanted in PMd and in M1, yielding
    79–118 units per array.
  expected:
  - quantity: conditions per monkey
    value: 72
    tolerance: 0
  - quantity: trials, monkey J
    value: 1469
    tolerance: 146.9
  - quantity: trials, monkey N
    value: 2014
    tolerance: 201.4
  criterion: Conditions and trials under the readings of the shared method. Reproduced when, under
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -i "conversion\|meters" *.txt | head; cd  grep -n -i "conversion" ldr.py | head; grep -n -i "cross-validated\|Supplementary Fig. 3\|Supplementary Figure 3" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "conversion\|1000\b\|\*= 1e3\|mm" ldr.py | head -20; grep -n -i "when cross-validated\|cross-validated" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 2: Sabatini & Kaufman 2024 on DANDI:000070 (34 claims in the claims file; 34 outcomes in the attempt record: 13 reproduced, 11 partially reproduced, 10 not reproduced)**

Cell indices below count from 0 within each notebook: nb1 is `reproduce_sabatini_2024.ipynb`, nb2 is `reproduce_sabatini_2024_kinematics.ipynb`.

### 1. Outcomes and assumptions

- **Outcomes.** I agree with all 34 stated outcomes. None of the numeric mismatches in section 2 changes an outcome.
- **Outcome changed since round 1.** fig7f-decoder-beats-standard went from blocked to partially_reproduced. I agree.
  - All 14 non-GPFA decoders are now run per dataset (nb2 cell 41).
  - LDR is higher with p < 0.001 in 56/56 comparisons under both bases (nb2 cell 42).
  - The criterion's partial clause, "all but the GPFA decoders", applies.
- **Outcomes marked `assumed: true`.** Each assumption is stated and reasonable:
  - suppfig2, fig6e, fig7c-ldr-encoding, suppfig7a, fig7c-standard-encoding-worse, fig7f-ldr-decoding and trial-curvature-decoding: hand positions measured from each trial's start.
  - fig6e: the paper's kernel length scales. The sweep in nb2 cell 17 shows the outcome does not depend on them.
  - fig7f-decoder-beats-standard: the training subset of 4,000 or 12,000 samples, and velocity integrated from the true position at −260 ms. The integration, if anything, favours the standard decoders.
  - suppfig8: no EMG in the files, and the code's centring. The variant centring gives the same outcome.
- **The online-onset assumption.** Every claim's deviations state it as "Assumption". `assumed: true` is not set for the notebook-1 claims, though.
  - The offline-onset variant (nb1 cell 86) covers fig3g, tbf-variance-explained, the jPCA R² and variance, single-lds-variance, fig2c, fig3a, fig3i (reading b, truncate only) and rotation-orientation-dimensionality. Those outcomes do not rest on the assumption.
  - It does not cover fig3c, fig4b, fig4c, fig4d, fig4f, fig5a, suppfig6a/b/c, suppfig3, suppfig2, tbf-shuffle-control, fig3h or any notebook-2 claim. Strictly, those outcomes still rest on an untested assumption. This is minor: no recomputed claim moved.

### 2. Sentences the printed outputs do not support

None of these changes an outcome. Many of the conclusions quote numbers that differ slightly from this execution's printouts.

- **nb1 cell 43 (fig2c)**, also in the record's notes and response:
  - Text: "the single-condition LDSs explain 83.4%, 90.7%, 92.9% and 94.4% (91.0% for PMd-N at 5)".
  - Cell 42 prints 83.2, 90.5, 92.8 and 94.1 (90.9 at k = 5).
- **nb1 cell 60 (suppfig3)**, also in the record's notes:
  - Text: "in-sample single-condition LDS (83.4%, 90.7%, 92.9%, 94.4%)".
  - Cell 59 prints 83.2, 90.5, 92.8 and 94.1.
  - The record's held-out LDS "67.5%, 77.0%, 83.6%, 78.6%" (notes and response): cell 59 prints 67.5, 76.8, 83.5 and 78.4.
- **nb1 cell 48 (fig3a)**, also in the record:
  - Text: "0.63, 1.75 and 3.19 Hz (M1-N)". Cell 47 prints 1.74.
  - The response says "M1-N 1.75 Hz in the new run", which is not what was printed.
- **nb1 cell 52 (fig3c)**, also the record's `measured`:
  - Text: "0.717, 0.669, 0.660 and 0.580" (halves null). Cell 51 prints 0.716, 0.670, 0.660 and 0.581.
  - Text: "0.797, 0.729, 0.646 and 0.592" (Poisson null). Printed: 0.796, 0.731, 0.646 and 0.594.
  - Text: norm distance "0.577 to 0.787". Printed: 0.579–0.786.
  - Text: seeds "0.577 to 0.717". Cell 54 prints 0.579–0.716.
- **nb1 cell 57 (suppfig2)**, also the record's `measured` 0.243:
  - Text: "0.243 … (0.243 and 0.296 under the skew-normal basis)". Cell 56 prints 0.244 under both bases.
  - Text: "per dataset it is 0.149 to 0.476". Printed: 0.150–0.474.
  - Text: "each conjugate pair once gives 0.235 and 0.291". Printed: 0.237 and 0.291.
- **nb1 cell 24 (fig3i)**, also in the record:
  - Text: "The warped correlations move by at most 0.004 over the five seeds."
  - PMd-N under reading (a) runs from −0.304 to −0.299, a change of 0.005 (cell 23).
- **nb1 cell 36 (fig4f)**, also in the record:
  - Text: "rho 0.843 to 0.952 … for four of the six planes". Those four include M1-N plane 2 at 0.816, so the range is 0.816–0.952 (cell 35).
  - Text: "(0.826 to 0.947)" for the code's input. Printed: 0.824–0.947 (M1-N plane 2, 0.8235).
- **nb1 cell 87 (offline variant)**, also in the record's fig2c notes:
  - Text: "explains 79.6% to 89.8%". Cell 86 prints `lds_ve` of 0.792–0.897, i.e. 79.2–89.7%.
- **Record, fig3a notes** (no conclusion cell states this):
  - Text: "0.87 … 3.07 … (2 of 10)" on the offline onset.
  - Cell 86 prints 0.86 and 3.06. Its 3 of 10 are within 10%: 1.54, 1.53 and 2.74 (inside 2.25–2.75).
- **nb2 cell 11 (fig6b)**, also in the record:
  - Text: "against a null of 31.1% to 44.1%". Cell 10 prints 44.0, 35.7, 44.8 and 29.2, i.e. 29.2–44.8%.
  - The response says "(PMd-N 1.3e-11), as printed". Cell 10 prints 6.7e-12.
- **nb2 cell 33 (fig7f-ldr-decoding)**, also in the record's notes and its fig7f-decoder notes:
  - Text: "88.6% to 93.0% for skewnormal". Cell 32 prints 88.4–92.8.
  - Text: null "5.4% to 10.4%". Printed: 5.4–10.1 (svd) or 5.8–10.5 (skewnormal).
  - Text: seeds "86.8% to 94.5%". Printed: 87.2–94.5 (svd) or 86.7–93.9 (skewnormal).
  - The response says these "are corrected to the printed values"; they are not.
- **nb2 cell 39 (suppfig8)**, also in the record, which adds "under both bases":
  - Text: "p = 4.5e-10 to 8.6e-06". Cell 38 prints 4.53e-10 to 3.66e-06 (svd), or 2.45e-10 to 1.11e-05 over both bases.
  - Text: per-variable centring "p = 8.4e-11 to 4.1e-06". Printed: 8.43e-11 to 2.79e-06 (svd), 3.56e-06 (skewnormal).
- **Record, fig6e notes:** seeds "OU … 40.5% to 83.3%". Cell 17 prints up to 0.832 (svd) or 0.834 (skewnormal).
- **Record, `sanity` finding:** "Hand positions are in mm with a conversion of 0.001 to meters". No printed output shows the conversion.

Everything else checks out against the printed outputs: the other "Result" cells, both Summary sections, the README (13/11/10, matching the record) and the remaining notes.

**My round-1 reasons in the record.** They are stated faithfully and in my own words for all 34 claims, including problems 1, 3–12. Problem 2 (the alignment event) appears in no `reason` field; it is only addressed in the responses.

### 3. Round-1 points

**Resolved:**
- **1 (fig3i).** The per-trial reading is run, the span text is corrected, and the end+100 variant is added. The outcome is not reproduced under every reading.
- **2 (onset).** The offline variant covers the claims that depend most on the onset, and their outcomes hold. The rest is as in section 1.
- **4 (fig4d/f).** The basis is now re-extracted from normalised data as the main reading.
- **5 (length scales).** The scale of the reach parameters is printed and the length scales are swept.
- **6 (decoders).** The decoders are now run.
- **7 (units).** The notes now disclose it.
- **8, 9, 11 and 12.**

**Remaining, bearing on a conclusion:**
- **Problem 3, a claims-file misreading (suppfig3).** The legend calls the comparison cross-validated, but the main reading compares held-out TBF with in-sample LDS. Scored like for like on held-out data from −160 ms, TBF beats LDS and jPCA in 4/4 (nb1 cell 59). That would make the claim reproduced. The outcome correctly stays as the claims file decides, and the question has been put to a reader.
- **Problem 7 (unsorted threshold crossings).** This is a data limitation and cannot be fixed. It remains a plausible cause of the dimensionality failures: single-lds-variance, rotation-orientation-dimensionality and suppfig6b.

**Remaining, not bearing on a conclusion:**
- **Problem 10 (suppfig8).** The notebook's "code" centring subtracts each sample's mean over the four variables. That is consistent with `mean(kinParams, 2)` only if `kinParams` is samples × 4. The notebook centres neurons as N × samples, which suggests the per-variable variant is the code's actual operation. I still cannot check `removePotent.m`. Both centrings give p < 0.036 in every dataset, so the outcome stands.
- **Mismatched numbers.** The numbers in section 2 should be brought into line with the printouts.

### 4. Critical findings

No finding in the attempt record is rated `critical`.

Of the findings that do have a severity, both are rated reasonably:
- **Finding 1 (unsorted units, `major`).** nb1 cell 5 shows it: the units table description says "Threshold crossings on each electrode, not sorted", with 96 units per array. The file states this openly, so the data are not wrong. Because every population analysis changes, `major` is right.
- **Finding 2 (missing `maze_condition`, `minor`).** nb1 cell 4 shows `conds` NaN for Nitschke 2010-09-20 and 2010-09-22, but the finding names no cell.

## End of run

16 turns, 3 minutes, $2.29 at API prices, result: success.
