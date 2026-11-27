# clark-2026 · verifier-2 · run 45888231485

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 1272
drwxr-xr-x 6 runner runner    4096 Nov 26 22:12 .
drwxr-xr-x 8 runner runner    4096 Nov 26 22:12 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 20:01 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 20:01 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 26 22:12 .claude
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .env
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .env.development
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .env.local
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .env.production
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .env.test
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .env.test.local
drwx------ 2 runner runner    4096 Nov 26 22:12 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 20:01 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 20:01 .github
-rw-r--r-- 1 runner runner       0 Nov 26 22:12 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 20:01 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 20:01 .mcp.json
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -50 clark-2026.yaml; echo ----; cat clark-2026-01.yaml
```

```
<persisted-output>
Output too large (57.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/d2e6b181-37b8-423c-b62a-a4d18aa1c413/tool-results/b59c7c9dz.txt

Preview (first 2KB):
# Clark, Abbott & Sompolinsky (2026) on dandiset 000939

Tests the findings of [Clark, Abbott & Sompolinsky (2026)](https://doi.org/10.1038/s41593-026-02452-4)
on [DANDI:000939](https://dandiarchive.org/dandiset/000939/0.240528.1542), the postsubiculum
recordings of Duszkiewicz et al. (2024) that the paper reuses, at the version the paper cites. The
1,533 head-direction tuning curves are rebuilt from the NWB files with the paper's procedure; they
match the paper's cached curves on Zenodo to 1e-14 Hz.

| Claim | Outcome |
|---|---|
| Session, unit and head-direction cell counts (link) | Reproduced |
| Tuning curves match the paper's cache (link, with the Zenodo input) | Reproduced |
| Heterogeneous, irregularly spaced peaks (Fig. 1e) | Reproduced |
| Peak numbers, data and generative process (Fig. 5d legend) | Reproduced |
| Mean and fluctuation profiles (Fig. 1f,g) | Reproduced |
| Centers of mass uniform, Kuiper test (Fig. 3a,b) | Reproduced |
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -40 clark-2026.yaml; grep -n "^[a-z_]*:" clark-2026.yaml clark-2026-01.yaml
```

```
# Clark, Abbott & Sompolinsky (2026) on dandiset 000939

Tests the findings of [Clark, Abbott & Sompolinsky (2026)](https://doi.org/10.1038/s41593-026-02452-4)
on [DANDI:000939](https://dandiarchive.org/dandiset/000939/0.240528.1542), the postsubiculum
recordings of Duszkiewicz et al. (2024) that the paper reuses, at the version the paper cites. The
1,533 head-direction tuning curves are rebuilt from the NWB files with the paper's procedure; they
match the paper's cached curves on Zenodo to 1e-14 Hz.

| Claim | Outcome |
|---|---|
| Session, unit and head-direction cell counts (link) | Reproduced |
| Tuning curves match the paper's cache (link, with the Zenodo input) | Reproduced |
| Heterogeneous, irregularly spaced peaks (Fig. 1e) | Reproduced |
| Peak numbers, data and generative process (Fig. 5d legend) | Reproduced |
| Mean and fluctuation profiles (Fig. 1f,g) | Reproduced |
| Centers of mass uniform, Kuiper test (Fig. 3a,b) | Reproduced |
| Correlation function approaches circulant form (Fig. 3c, S13) | Reproduced |
| Generative fit (sigma, beta, b) of about (1.42, 2.77, 1.73) (Fig. 4) | Partially reproduced |
| Generative profiles, peak counts, peak heights, flip symmetry, information (Fig. 5a to f) | Reproduced (5 claims) |
| Recorded bump tracks head direction (Fig. 2l) | Reproduced |
[... 88 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "clark-2026-01.yaml"
}
```

```
1	schema_version: 3
2	id: clark-2026-01
3	datasets:
4	- archive: dandi
5	  id: 000939
6	  version: 0.240528.1542
7	  doi: 10.48324/dandi.000939/0.240528.1542
8	  relation: reuses
9	paper: doi:10.1038/s41593-026-02452-4
10	date: 2026-11-26
11	entry: clark-2026
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 749 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    if c['cell_type']=='markdown':
        print(f"=== [{i}] MD\n{src}")
    else:
        print(f"=== [{i}] CODE ({len(src.splitlines())} lines)")
        if len(sys.argv)>2: print(src)
        for o in c.get('outputs',[]):
            if 'text' in o: print(''.join(o['text']))
            elif 'data' in o and 'text/plain' in o['data']:
                if 'image/png' in o['data']: print('[image]')
                else: print(''.join(o['data']['text/plain']))
            elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
for n in tuning_curves network network_grid theory model_sims; do python3 $TMPDIR/dump.py $n.ipynb > $TMPDIR/$n.txt; wc -c $TMPDIR/$n.txt; done
```

```
56296 /tmp/claude-1001/tuning_curves.txt
25885 /tmp/claude-1001/network.txt
10233 /tmp/claude-1001/network_grid.txt
16267 /tmp/claude-1001/theory.txt
23708 /tmp/claude-1001/model_sims.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/tuning_curves.txt"
}
```

```
1	=== [0] MD
2	# Clark, Abbott & Sompolinsky (2026): the tuning-curve claims, on DANDI:000939
3	
4	Paper. D. G. Clark, L. F. Abbott, H. Sompolinsky, "Symmetries and continuous attractors in
5	disordered neural circuits", Nature Neuroscience (2026), doi:10.1038/s41593-026-02452-4. The
6	claims file `claims/clark-2026.yaml` was written from the version of record (main text, Methods,
7	figure legends and the Supplementary Information).
8	
9	Dataset. DANDI:000939 (Duszkiewicz et al. 2024, postsubiculum of freely moving mice), pinned
10	at version 0.240528.1542 (doi:10.48324/dandi.000939/0.240528.1542). This is the version the
11	paper cites (claims file, opening comment). Later versions exist (0.250207.0025 to
12	0.261016.2310); the cell below shows that every file changed after this version (new names with
13	session ids and sizes of about 24 GB), so the cited version is the one that holds the files the
14	paper's code read. The paper reuses this dataset (`relation: reuses`).
15	
16	Outside input. The paper's cached tuning curves, `mouse_data/tc_data.npz` in Zenodo
17	doi:10.5281/zenodo.21827768 (version 1.0), read by range requests from the record's tar and
18	checked against the record's MD5. It is used only by the link claim `tuning-curves-match-cache`.
19	Everything else is computed from the NWB files, streamed from the archive.
20	
[... 604 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/tuning_curves.txt",
 "offset": 625
}
```

```
625	=== [47] CODE (7 lines)
626	data: median 0.927; fraction below 0.5 0.2368 (363 curves); below 0 0.1031 (158 curves)
627	
628	fitted params, seed +0: median 0.834; below 0.5 0.2814 (ratio to data 1.19); below 0 0.1175 (ratio 1.14)
629	
630	fitted params, seed +1000: median 0.832; below 0.5 0.2797 (ratio to data 1.18); below 0 0.1178 (ratio 1.14)
631	
632	fitted params, seed +2000: median 0.834; below 0.5 0.2796 (ratio to data 1.18); below 0 0.1170 (ratio 1.14)
633	
634	fitted params, seed +3000: median 0.839; below 0.5 0.2760 (ratio to data 1.17); below 0 0.1161 (ratio 1.13)
635	
636	fitted params, seed +4000: median 0.833; below 0.5 0.2814 (ratio to data 1.19); below 0 0.1198 (ratio 1.16)
637	
638	paper params, seed +0: median 0.846; below 0.5 0.2681 (ratio to data 1.13); below 0 0.1087 (ratio 1.06)
639	
640	paper params, seed +1000: median 0.843; below 0.5 0.2676 (ratio to data 1.13); below 0 0.1093 (ratio 1.06)
641	
642	paper params, seed +2000: median 0.845; below 0.5 0.2671 (ratio to data 1.13); below 0 0.1079 (ratio 1.05)
643	
644	paper params, seed +3000: median 0.849; below 0.5 0.2626 (ratio to data 1.11); below 0 0.1075 (ratio 1.04)
[... 107 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/network.txt"
}
```

```
1	=== [0] MD
2	# Clark, Abbott & Sompolinsky (2026): the data-derived network, on DANDI:000939
3	
4	Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`, written from the
5	version of record and its supplement.
6	
7	Dataset. DANDI:000939 at version 0.240528.1542, the version the paper cites; every file
8	was replaced in later versions (see `tuning_curves.ipynb`, "Files and versions").
9	
10	The tuning curves are computed from the streamed NWB files as in `tuning_curves.ipynb`
11	(`hdring.load_all_curves`). The network is built and run as in the paper's
12	`notebooks/data_driven_attractor.ipynb`, `spurious_fixed_points.ipynb` and `ring/data_driven.py`
13	(commit 245726f), in numpy and float32 (the paper's simulations use float32 torch tensors).
14	The lambda and c grid of Supplementary Figs. 8 and 9 is in `network_grid.ipynb`; the
15	simulations of the generative-process and rank-four networks are in `model_sims.ipynb`.
16	
17	| claim | tested here |
18	|---|---|
19	| fig2b-sorted-weights-mexican-hat | yes |
20	| fig2ef-data-network-quasicontinuous | yes |
[... 292 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/network_grid.txt"
}
```

```
1	=== [0] MD
2	# Clark, Abbott & Sompolinsky (2026): the lambda and c grid of the data-derived network
3	
4	Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. Dataset.
5	DANDI:000939 at version 0.240528.1542, the version the paper cites (see
6	`tuning_curves.ipynb` for why).
7	
8	One claim: `figs8-s9-lambda-and-c` (Supplementary Note 3, section 8.4; Supplementary Figs. 8 and
9	9), run as `data_driven_reconstruction.ipynb` cell 10: lambda in 1e-12 to 1e-2, c in 0 to 1.5,
10	T 30 s, tau 50 ms, step tau/10 = 5 ms, initial conditions at regularly spaced target angles with
11	noise of standard deviation 3. The paper's notebook runs 100 initial conditions at each of the
12	42 grid points; here 20 are run at each point (every 500th target angle), to keep the entry's
13	run within its time limit, and 100 at the points the criterion reads at c 0 and c 1 (a deviation,
14	recorded in the attempt). The paper's own flow errors (err_grid of
15	`pc_convergence_grid.npz` in the Zenodo record doi:10.5281/zenodo.21827768) are read for
16	comparison.
17	=== [1] CODE (10 lines)
18	loaded and prepared in 133 s; curves (1533, 100); X (10000, 1533)
19	
20	=== [2] CODE (8 lines)
[... 129 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/theory.txt"
}
```

```
1	=== [0] MD
2	# Clark, Abbott & Sompolinsky (2026): the mean-field theory and the large-N spectra
3	
4	Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. Dataset.
5	DANDI:000939 at version 0.240528.1542, the version the paper cites (see
6	`tuning_curves.ipynb`).
7	
8	These claims are on the paper's theory and simulations (`data: elsewhere`, the paper's code at
9	commit 245726f), except `fig7c-dmft-integrates-behavior`, which drives the mean-field equations
10	with the head direction of mouse A3707 from the dataset. The mean-field code is a copy of the
11	paper's `ring/dmft.py` (`ring_dmft.py` in this entry, MIT licence, imports of torch removed).
12	
13	| claim | data | tested here |
14	|---|---|---|
15	| fig7-dmft-mexican-hat-and-stability | elsewhere | yes |
16	| fig7de-dmft-timescales | elsewhere | yes |
17	| fig7c-dmft-integrates-behavior | dataset | yes |
18	| fig6cd-eigenvalues-real-degenerate | elsewhere | yes |
19	| fig6fg-disordered-eigenvectors | elsewhere | yes |
20	=== [1] CODE (12 lines)
[... 205 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/model_sims.txt"
}
```

```
1	=== [0] MD
2	# Clark, Abbott & Sompolinsky (2026): the simulations of the generative-process and rank-four networks
3	
4	Paper. doi:10.1038/s41593-026-02452-4; claims file `claims/clark-2026.yaml`. Dataset.
5	DANDI:000939 at version 0.240528.1542, the version the paper cites (see `tuning_curves.ipynb`).
6	
7	These three claims use no recorded data (`data: elsewhere`): each runs a notebook of the
8	paper's code at commit 245726f, repeated here in numpy (`hdring.py`). The networks are built
9	from the idealized generative process (`ring/tc.py`, `gen_tuning_curves_idealized`; sigma
10	1.4211, beta 2.7659, 500 angles, lambda 1e-8) or from random rank-four loadings. Every random
11	draw comes from the claim's seed; the paper's notebooks use numpy seeds 42 and 123.
12	
13	| claim | data | tested here |
14	|---|---|---|
15	| figs1-s2-spectrum-does-not-fix-symmetry | elsewhere | yes |
16	| figs11-s12-global-stability-model | elsewhere | yes |
17	| figs10-robustness-comparable | elsewhere | yes |
18	| fig8-grid-scores-and-torus | elsewhere | no, blocked (too large) |
19	=== [1] CODE (9 lines)
20	=== [2] CODE (9 lines)
[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  - id:\|^  id:" clark-2026.yaml | head -50; grep -c "^- id:" clark-2026.yaml; sed -n 700,760p clark-2026.yaml
```

```
62:- id: hd-cell-selection
99:- id: tuning-curves-match-cache
116:- id: fig1e-heterogeneous-peaks
133:- id: fig5d-peak-numbers
164:- id: fig1fg-mean-and-fluctuation-profiles
189:- id: fig3ab-centers-of-mass-uniform
228:- id: fig3c-correlation-approaches-circulant
253:- id: fig4-generative-fit
286:- id: fig5ab-profiles-match
304:- id: fig5c-peak-counts-match
322:- id: fig5d-peak-heights-match
336:- id: fig5e-flip-symmetry-match
353:- id: fig5f-information-match
366:- id: fig2b-sorted-weights-mexican-hat
389:- id: fig2ef-data-network-quasicontinuous
413:- id: fig2gi-circulant-noise-collapses
441:- id: fig2jk-velocity-integration
463:- id: fig2l-recorded-bump-tracks-hd
484:- id: figs8-s9-lambda-and-c
509:- id: figs11b-data-network-global-stability
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 413,440p clark-2026.yaml; echo ...; sed -n 484,526p clark-2026.yaml; echo ...; sed -n 577,700p clark-2026.yaml
```

```
- id: fig2gi-circulant-noise-collapses
  statement: The optimal weights keep a continuum of stable heterogeneous states; their circulant
    average gives bumps identical up to translation, while the circulant matrix plus the scrambled
    residuals collapses onto a few discrete states within 30 s, so the optimal weights are not a
    noisy circulant matrix.
  source: Results, Dynamics of the data-derived network model, paragraphs 4 and 5; Fig. 2c,d,g to
    i; Supplementary Note 3, section 8.2
  quote: The optimal weights (Fig. 2b) maintain a continuum of stable, heterogeneous states (Fig.
    2g). Averaging the sorted weights along ... diagonals gives a circulant matrix (Fig. 2c) whose
    bumps are identical up to translation ... this network collapses onto a few discrete states
    within the 30-s window (Fig. 2i)
  data: dataset
  depends_on:
  - fig2b-sorted-weights-mexican-hat
  criterion: As in data_driven_attractor.ipynb. The sorted matrix; its circulant version, the
    average over circular diagonals; and the circulant plus noise, the residuals (circulant minus
    sorted) with all off-diagonal entries shuffled together, the asymmetric version used in Fig.
    2d,i (numpy seed 42); both surrogates multiplied by 1.275. Each is run with c 1 from 100
    initial conditions at regularly spaced manifold points with input-current noise of standard
    deviation 2.5, for 30 s. A final state's position is the neuron index of the peak of its
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 685,706p clark-2026.yaml; grep -n -i "partial" clark-2026.yaml | head -30
```

```
- id: figs1-s2-spectrum-does-not-fix-symmetry
  statement: Eigenvalue degeneracy suggests but does not fix the symmetry group, since ensembles
    matching the model's second-order statistics, and hence its spectrum, can differ beyond second
    order and give different symmetry groups and attractors (a single ring for Gaussian loadings,
    the full torus for mixture-of-Gaussians loadings, in a rank-four network).
  source: Discussion, Low-rank networks, symmetry and degeneracy, paragraph 1; Supplementary Figs.
    1 and 2
  quote: we can construct ensembles that match our model’s second-order statistics and hence its
    spectrum, while differing beyond second order, yielding different symmetry groups and attractor
    structures (Supplementary Figs. 1 and 2)
  data: elsewhere
  where: github.com/davidclark1/symmetries-continuous-attractors at commit 245726f,
    notebooks/weight_matrix_analyses.ipynb (simulation code; no recorded data)
  criterion: Run the notebook's rank-four Gaussian and mixture-of-Gaussians networks (initial
    amplitude 5 for the Gaussian and 0.45 for the mixture, as the notebook sets them). The
    notebook computes no eigenvalues; the supplement says the two share them by construction.
    Reproduced when the eigenvalues of the two weight matrices, computed here, agree within 5%
    (threshold chosen here, open) and their dynamics differ as the legends describe. With Gaussian loadings (N 10,000, K 4, 40 initial conditions, 10 tau) the
    final states form a ring in the dominant doublet and collapse to the origin in the
    subdominant one (a single ring). With mixture loadings they form a ring in both doublets (the
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 253,286p clark-2026.yaml; sed -n 322,336p clark-2026.yaml
```

```
- id: fig4-generative-fit
  statement: A single parameter set of the generative process, fitted to the two-point
    correlation function pooled over mice, is (sigma, beta, b) of about (1.42, 2.77, 1.73).
  source: Results, Statistical generative process, paragraph 5; Fig. 4d to f; Methods, Model
    settings, Setting 2
  quote: This yields (σ, β, b) ≈ (1.42, 2.77, 1.73; Fig. 4d–f) and tuning curves closely
    resembling the experimental ones (Fig. 4g)
  data: dataset
  depends_on:
  - hd-cell-selection
  expected:
  - quantity: Fourier decay scale sigma
    value: 1.42
    tolerance: 0.142
  - quantity: sharpness beta
    value: 2.77
    tolerance: 0.345
  - quantity: soft threshold b
    value: 1.73
    tolerance: 0.173
[... 29 more lines not kept]
```

**Agent**

**Verifier report, round 2: Clark, Abbott & Sompolinsky (2026) on DANDI:000939 (0.240528.1542)**

The claims file has 30 claims. The attempt record has 30 outcomes: 21 reproduced, 4 partially_reproduced, 1 not_reproduced, 1 blocked (fig8), and 3 reproduced resting on an assumption (figs11b, figs10, figs11-s12). Five notebooks are present now; in round 1 there were four. `model_sims.ipynb` is new.

### 1. Outcomes and assumptions

**Outcomes I agree with, unchanged since round 1.** I agree with all 26 outcomes I gave in round 1, except figs11b, which is discussed below. Checked against the claims file again, the outcomes for fig4, fig2gi, figs8-s9 and fig7de follow from the printed values.
- **No partial rule.** The criteria for fig4, figs8-s9 and figs1-s2 contain no "partially" rule. Read strictly, they give `not_reproduced`. I accept `partially_reproduced` as the fair description in each case, but it comes from the protocol's general reading, not from the criterion.

**Changed or new outcomes:**
- **figs11b, `reproduced`, `assumed: true`.** I agree.
  - The assumption is stated: the threshold comes from the fig2ef protocol run with the same 5-ms step. It is reasonable, and it is the reference on the same footing that I asked for in round 1.
  - Any threshold here sits at the noise floor. The real evidence is that final distances are about 1e-3 against median starting distances of 1.6 to 700 (cell 22).
- **figs10, `reproduced`, `assumed`.** I agree.
  - The continuum rule (at least 31 of 34 states) is stated and reasonable. It does not decide the outcome: both networks keep 34 states at noise 0, against 8 and 9 at 0.4 (cell 11).
- **figs11-s12, `reproduced`, `assumed`, `seed_sensitive`.** I agree.
  - The threshold assumption (the network's own fig2ef-protocol run) is stated and reasonable.
  - Part of the assumption is stated only in notebook cell 6, not in the record's deviations: it reads the criterion's "every final state" and "all … converge" as "at least 95%, as in figs11b". Under a strict "every", the claim seed fails at standard deviation 10: 0.97 within, with one state at 0.01146 against 0.01121 (cell 7).
- **figs1-s2, `partially_reproduced`, `seed_sensitive`.** I agree, with two reservations.
  - The criterion has no partial rule (see above).
  - The criterion's 5% test on two finite matrices measures sampling noise: the population eigenvalues are identical by construction (100, 100, 25, 25; cell 4). I report this as a weakness in the claims file's chosen threshold.
- **fig8, `blocked` (`too_large`).** I agree.

### 2. Statements the printed outputs do not support

- **theory cell 9 and the fig7de notes:** "reaches 20.5 tau at beta 1.1 and sigma 100". Cell 8 prints 19.513 at sigma 100. The maximum of 20.521 is at some other sigma.
  - The notes also say "the failures come from the grid's large sigma" and "Over sigma 1 to 10 the timescales stay within a few tau". The divergence time's "decreasing" test fails at small sigma (11 and 10 increases), and only sigma 1 and 100 are printed.
- **theory cell 6, fig7 notes and finding 4:** "mostly at small beta and large sigma" (finding 4: "mostly beta below 0.1 or sigma near 100"). Cell 5 lists only 8 of the 293 points.
- **network_grid cell 5 and figs8-s9 notes:** "1 to 4 of 100" diverge and "96 to 100 of 100" collapse "at every lambda". At lambda 1e-10 and 1e-6, n is 20 (4 and 16, 3 and 17; cell 4).
- **figs14 notes:** "Without setting one aside, two of the four pairs pass." The variant in network cell 19 prints within [0.027 0 0 0.0359] against next [0.1389 0.183 0.0002 0], which gives 3 of 4.
- **network cell 23:** "Every final state is on the manifold at the resolution of the reference (largest final distance 0.0015…)". Final maxima reach 0.00153 and 0.00154, above the 5-ms reference of 0.00141 (cell 22); only 97–100% are within it.
- **model_sims cell 12 and figs10 notes:** "The two fragment alike over the whole range."
  - At noise 0.4 the disordered network ends in fewer states under every seed: 4–8 against 9–12.
  - Under the claim seed it has fewer states at every level from 0.4 on, and about twice the median drift (cell 11).
  - The criterion is met, but "alike" overstates it.
- **Finding 3:** the two minima's errors "differ by less than the sampling noise of 500,000 samples". In float64 the ranges do not overlap: 0.00853–0.00894 for the chosen point against 0.00907–0.01006 for the paper's (tuning_curves cell 33). The ranking flips only with float32 under one seed and in the paper's cached grid.
- **Run times:**
  - The fig8 notes say the five notebooks take "77 minutes per run", and the README gives per-notebook times of 15, 22, 8, 2 and 31 minutes.
  - The printed totals are 1139, 2254, 611, 154 and 3042 s, which make 7,200 s (120 min).
- **tuning_curves cell 0:** later files have "sizes of about 24 GB". Cell 3 prints 12.7 to 30.2 GB.

Every other "**Result:**" sentence, Summary section, README row and note I checked matches the printed values.

**My round-1 reasons in the record:** the attempt record states them faithfully and in substance in my own words, for all 30 claims.

### 3. Round-1 points

| point | status |
|---|---|
| 1. fig4 | Resolved: all the outputs I asked for are printed, plus the paper's cached grid. `partial` stands on the tolerance. |
| 2. widths compared with `==` | Resolved. |
| 3. fig2gi | Resolved as far as the attempt can go: seeds, the angle-shift test and the wrap-mode variant are all added. **Remains, and bears on the outcome:** the criterion's 50 states cannot be reached; this is a claims-file defect, now sent to a reader. |
| 4. figs8-s9 | The paper's err_grid has been added and agrees. The grid still uses 20 initial conditions at most points (the 8 points the criterion reads use 100). **Remains, and bears on the outcome:** the claims file reads err(1e-8) < err(1e-12) more strictly than the supplement, and λ 1e-2 at c 1 does not collapse (radius 4.6 against 3.9). |
| 5. figs11b | Resolved by the 5-ms reference; the outcome now rests on a stated assumption. |
| 6. figs14 | Resolved: documented (but see the miscount in section 2). |
| 7. fig7 | Resolved: the bump amplitude is printed. **Remains:** the criterion tests only eigenvalue 2. The output contradicts the statement's "except the symmetry-induced zero" at 293 of 800 points, where the bump is not flat (median amplitude 0.95). That gap in the claims file bears on how much the `reproduced` covers. |
| 8. minor points | Resolved. |
| 9. untested claims | Resolved: three are tested and fig8 is blocked with a stated reason. |

**Other points that bear on a conclusion:**
- figs1-s2's 5% threshold sits at the level of sampling noise.
- figs11-s12 reads "every" as 95% without saying so in the record.
- Three outcomes are `partial` under criteria that have no partial rule.

### 4. Critical findings

None of the four findings in the attempt record is rated `critical`.
- **Findings 1 and 2** are rated `none`. They are supported by tuning_curves cells 3, 6, 8 and 10, and `none` is right.
- **Findings 3 and 4** concern the paper and carry no severity.

## End of run

16 turns, 3 minutes, $1.58 at API prices, result: success.
