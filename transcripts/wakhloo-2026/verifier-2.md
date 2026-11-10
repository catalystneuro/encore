# wakhloo-2026 · verifier-2 · run 42796983909

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 320
drwxr-xr-x 6 runner runner    4096 Nov 10 10:35 .
drwxr-xr-x 7 runner runner    4096 Nov 10 10:34 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 10:11 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 10:11 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 10 10:34 .claude
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .env
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .env.development
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .env.local
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .env.production
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .env.test
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .env.test.local
drwx------ 2 runner runner    4096 Nov 10 10:34 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 10:11 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 10:11 .github
-rw-r--r-- 1 runner runner       0 Nov 10 10:34 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 10:11 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 10:11 .mcp.json
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; diff wakhloo-2026-01.yaml wakhloo-2026.yaml | head -50; head -c 3000 wakhloo-2026-01.yaml
```

```
# Wakhloo, Slatton & Chung (2026) from dandiset 000978

Tests the rat findings of [Wakhloo, Slatton and Chung (2026)](https://doi.org/10.1038/s41593-025-02183-y)
on [DANDI:000978](https://dandiarchive.org/dandiset/000978/0.240511.0307), the W-track learning data
of Tang, Shin and Jadhav (2023): spikes from PFC and CA1, position and trials of 8 rats over 8
sessions in one day. The paper's theory, its network simulations and its macaque and pose network
analyses are not about this dataset and are blocked.

| Claim | Outcome |
|---|---|
| Behavioural error falls over sessions 1 to 4, then plateaus | Reproduced |
| Readout error falls over learning in PFC and CA1, then plateaus | Reproduced |
| Readout error correlates with behaviour, R2 0.48 (CA1) and 0.51 (PFC) | Reproduced |
| Theory agrees well with the empirical readout error | Reproduced (criterion amended after a question; not reproduced before) |
| Total dimension drops over sessions 1 to 4 | Reproduced |
| Task-relevant dimension (GLM) increases over learning | Reproduced |
| Nearly every geometric measure increases over sessions 1 to 4 | Reproduced |
| After session 4 dimension rises and correlation falls | Reproduced |
| Quadratic mixed models of dimension, correlation, SNF significant (P < 1e-5) | Reproduced |
| No non-monotonic trend in SSF | Reproduced |
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,400p wakhloo-2026-01.yaml
```

```
A simulation of multilayer perceptrons (code/run_mlp_exps.py), not a finding on recorded data;
    the dataset cannot test it, and it was not run here.
- claim: fig3dg-mlp-geometry-tradeoff
  outcome: blocked
  blocked_by: other
  notes: A simulation of multilayer perceptrons, not a finding on recorded data; not run here.
- claim: fig4bf-pose-network-geometry
  outcome: blocked
  blocked_by: not_runnable
  notes: >-
    The data are the DeepLabCut parenting mouse benchmark, outside the dataset. Testing the claim
    needs a ResNet50 pose network trained as in the Methods; the paper's code README says the
    training "can take a few hours" and "must be executed in a separate Python 3.8 virtual
    environment" (code/setup_deeplabcut.py), which an entry locked to Python 3.13 cannot install,
    and which does not fit the run's time. Not attempted.
- claim: fig4g-pose-theory-r2
  outcome: blocked
  blocked_by: not_runnable
  notes: Needs the trained pose network of fig4bf-pose-network-geometry; not attempted.
- claim: fig5d-macaque-theory-and-ventral-stream
[... 321 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,700p wakhloo-2026-01.yaml
```

```
agrees: true
    outcome: blocked
    reason: Blocked (data_missing). Same as fig5d.
    response: Outcome and blocked_by (other) kept, as for fig5d-macaque-theory-and-ventral-stream.
  - claim: fig5h-macaque-snf-it
    agrees: true
    outcome: blocked
    reason: Blocked (data_missing). Same as fig5d.
    response: Outcome and blocked_by (other) kept, as for fig5d-macaque-theory-and-ventral-stream.
  - claim: optimal-code-disentangled
    agrees: true
    outcome: blocked
    reason: Blocked (other). Theory.
    response: Outcome kept.
  - claim: eq2-optimal-spectrum-flattens
    agrees: true
    outcome: blocked
    reason: Blocked (other). Theory, checked in the paper by numerical optimisation.
    response: Outcome kept.
  - claim: fig6ce-optimal-early-low-dim-high-corr
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_wakhloo_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== CELL {i} [{c['cell_type']}]")
    if c['cell_type']=='markdown':
        print(src)
    else:
        print(src[:1500] + ('...[trunc]' if len(src)>1500 else ''))
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--\n'+''.join(o['text']))
            elif 'data' in o and 'text/plain' in o['data']: print('--OUT--\n'+''.join(o['data']['text/plain']))
            elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
EOF
```

```
<persisted-output>
Output too large (98.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/02e73ba8-ffbd-49a4-bfff-a1759ea1484c/tool-results/b8vm457hx.txt

Preview (first 2KB):
===== CELL 0 [markdown]
# Wakhloo, Slatton & Chung (2026) on DANDI:000978

Paper: A. J. Wakhloo, W. Slatton and S. Chung, "Neural population geometry and optimal coding of
tasks with shared latent structure", *Nature Neuroscience* (2026),
doi:[10.1038/s41593-025-02183-y](https://doi.org/10.1038/s41593-025-02183-y). The paper reuses the
data of Tang, Shin and Jadhav (2023).

Dataset: [DANDI:000978](https://dandiarchive.org/dandiset/000978/0.240511.0307) "Single Day
W-Track Learning", version **0.240511.0307** (doi:10.48324/dandi.000978/0.240511.0307). The paper
cites this version (ref. 67, and the README of its code), and it is also the most recent published
version; the dandiset has three published versions, all made on 2024-05-11 within twenty minutes,
with the same nine assets and the same total size, so the choice does not change the data read.

Claims: `claims/wakhloo-2026.yaml`, written from the version of record (published 4 February 2026),
main text, figure legends and Methods; the Supplementary Information was not in the text read. The
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/02e73ba8-ffbd-49a4-bfff-a1759ea1484c/tool-results/b8vm457hx.txt"
}
```

```
1	===== CELL 0 [markdown]
2	# Wakhloo, Slatton & Chung (2026) on DANDI:000978
3	
4	Paper: A. J. Wakhloo, W. Slatton and S. Chung, "Neural population geometry and optimal coding of
5	tasks with shared latent structure", *Nature Neuroscience* (2026),
6	doi:[10.1038/s41593-025-02183-y](https://doi.org/10.1038/s41593-025-02183-y). The paper reuses the
7	data of Tang, Shin and Jadhav (2023).
8	
9	Dataset: [DANDI:000978](https://dandiarchive.org/dandiset/000978/0.240511.0307) "Single Day
10	W-Track Learning", version **0.240511.0307** (doi:10.48324/dandi.000978/0.240511.0307). The paper
11	cites this version (ref. 67, and the README of its code), and it is also the most recent published
12	version; the dandiset has three published versions, all made on 2024-05-11 within twenty minutes,
13	with the same nine assets and the same total size, so the choice does not change the data read.
14	
15	Claims: `claims/wakhloo-2026.yaml`, written from the version of record (published 4 February 2026),
16	main text, figure legends and Methods; the Supplementary Information was not in the text read. The
17	paper's code is github.com/awakhloo/population_geometry_optimal_coding at commit 9674a6c, which the
18	claims file and the helper `wtrack.py` cite for each method detail the Methods leave open.
19	
20	| Claim | Tested here |
[... 526 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/02e73ba8-ffbd-49a4-bfff-a1759ea1484c/tool-results/b8vm457hx.txt",
 "offset": 547,
 "limit": 400
}
```

```
547	
548	--OUT--
549	linear mixed model over sessions 1 to 4: slope -0.1662 per session, P = 5.8e-18
550	
551	===== CELL 16 [markdown]
552	**Result: reproduced.** The mean behavioural error over the 8 rats falls from 0.668 at session 1 to 0.157 at session 4 (a drop of 0.511, lower in 8 of 8 rats) and is 0.180 at session 8, a change of 0.023 after session 4. The linear mixed model over sessions 1 to 4 has a slope of -0.166 per session (P = 5.8e-18).
553	===== CELL 17 [markdown]
554	## fig7e-readout-error-learning
555	
556	The task-averaged readout error for position and velocity decreases over learning in PFC and CA1, then plateaus after session four.
557	
558	> These readout errors decrease over learning (Fig. 7e,f )
559	===== CELL 18 [code]
560	def plateau_check(g):
561	    e1, e4, e8 = s4_s1(g)
562	    return dict(s1=round(e1, 4), s4=round(e4, 4), s8=round(e8, 4), drop_1_4=round(e1 - e4, 4), change_4_8=round(e8 - e4, 4),
563	                holds=bool(e4 < e1 and e8 < e1 and abs(e8 - e4) < (e1 - e4)))
564	rows = []
565	for v in VARIANTS:
566	    for c in ["theory", "hebbian"]:
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/02e73ba8-ffbd-49a4-bfff-a1759ea1484c/tool-results/b8vm457hx.txt",
 "offset": 947,
 "limit": 310
}
```

```
947	 CA1  quad      ssf     0.00053 -0.000613  0.00127         0.947    0.944      0.875     0.001   0.00121  0.000896        0.36    0.313    0.419
948	 CA1  quad      dim      -0.409    -0.634   -0.414       1.8e-07 3.34e-08   1.35e-07    0.0532    0.0819    0.0538     7.9e-07 2.04e-07 6.03e-07
949	 CA1   lin      ssf      0.0075   0.00787  0.00754       0.00055  0.00106   0.000646       NaN       NaN       NaN         NaN      NaN      NaN
950	 CA1   lin task_dim       0.238     0.242    0.242       3.1e-06 2.07e-06   2.07e-06       NaN       NaN       NaN         NaN      NaN      NaN
951	gamma signs equal to the paper's in 14 of 14 models (19-unit variant)
952	
953	===== CELL 40 [markdown]
954	## mixed-quadratic-dim-corr-snf
955	
956	Quadratic mixed models of total dimension, correlation and SNF have linear and quadratic terms with P < 10^-5 in both areas, of opposite sign.
957	
958	> We found strong, significant effects for both the linear and quadratic terms in PFC and CA1 for the total dimension, correlation and SNF ( P < 10 −5 ; Supplementary Table 2 ). In each case, the sign of the quadratic term was the opposite of the linear term
959	===== CELL 41 [code]
960	for k, T in MIX.items():
961	    q = T[(T.model == "quad") & T.meas.isin(["dim", "corr", "snf"])]
962	    opp = bool(np.all(np.sign(q.gamma) != np.sign(q.eta)))
963	    for adj in ["raw", "adjusted"]:
964	        P = np.concatenate([q.p_gamma, q.p_eta]) if adj == "raw" else np.concatenate([q.p_gamma_adj, q.p_eta_adj])
965	        print(f"{k} | {adj}: P below 1e-5 {int((P < 1e-5).sum())} of 12, below 0.05 {int((P < 0.05).sum())} of 12, largest P {P.max():.2g}; opposite signs in all six: {opp}")
966	--OUT--
[... 287 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "assumed" wakhloo-2026-01.yaml wakhloo-2026.yaml | head; grep -c "^- id:" wakhloo-2026.yaml; grep -n "^- id:\|data_location\|data:" wakhloo-2026.yaml | head -60; grep -n -o ".\{150\}0\.49.\{100\}" paper/*.txt | head; python3 -c "
import json,re
nb=json.load(open('reproduce_wakhloo_2026.ipynb'))
o=''.join(nb['cells'][4]['outputs'][0]['text'])
mins=[float(l.split()[6]) for l in o.splitlines()[1:65]]
print(len(mins), sum(15<=m<=16 for m in mins), sum(15<=m<17 for m in mins))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_wakhloo_2026.ipynb'))
o=''.join(nb['cells'][4]['outputs'][0]['text'])
mins=[float(l.split()[5]) for l in o.splitlines()[1:65]]
print(len(mins), sum(15<=m<16 for m in mins), sum(15<=m<17 for m in mins), sum(15<=m<=16.0 for m in mins))"; sed -n 228,500p wakhloo-2026.yaml
```

```
64 34 53 36
- id: svc-hebbian-correlation
  statement: Across every analysis of the paper, the Hebbian readout error is strongly
    correlated with the empirical error of a linear support vector classifier trained on the
    same tasks, particularly in the brain data.
  source: Discussion, paragraph 3; Supplementary Fig. 3 (not in the text read)
  quote: Across every analysis reported in this paper, we found a strong correlation between
    SVC and Hebbian errors, particularly in the brain data
  criterion: Only the PFC and CA1 parts are tested on DANDI:000978. As in
    figures/SM-svm-comparison-fig.ipynb, per area, the squared Pearson correlation over the 64
    rat and session values (means over the 500 subsets of the shared pipeline) between the
    theoretical Hebbian error (Eq. 5) and the error of a linear SVC (scikit-learn LinearSVC,
    one per task, on the same 300 training and 200 test bins, utils.emp_error). The notebook
    loads an older results file (abstraction/results/<area>_results_nu_dt_0.5.npy) and does not
    cut it to sessions 1 to 8; the 64 values of the shared pipeline are used here. The empirical
    Hebbian error in place of the theoretical one is a variant. The paper sets no bound for
    "strong", and the Supplementary Fig. 3 values were not read. The readings are (a) a
    positive Pearson correlation with p < 0.05 in each area; (b) r2 of at least 0.5 in each
    area, a conventional bound named here as one. Reproduced when a reading holds in both
    areas; partially reproduced when it holds in one.
[... 254 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 500,530p wakhloo-2026.yaml; grep -n "def glm_summary" -A40 wtrack.py | grep -n "argmax\|nan\|\"\"\""
```

```
cross-validated D2 (rat_utils.format_glm_results, test_scores); the mean is over the 64
    rat and session values. The code does not compute the standard deviation; the readings are
    the population (ddof 0) and the sample (ddof 1) standard deviation over the 8 rats of each
    rat's mean over sessions. Whether units later replaced by the null model are counted with
    their own negative D2 (as test_scores does) or with 0 is a further pair of readings.
    Reproduced when all four values are within tolerance under one combination of readings.
    The cross-validation folds are random and the GLM fit may differ slightly from the
    paper's; the seed is a standard choice.
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig3bc-mlp-theory-tracks-error, statement "at every layer" changed to "across layers"; the
    Fig. 3b,c legend and the Results say only that theory closely tracks the empirical errors.
  - svc-hebbian-correlation, criterion now says that figures/SM-svm-comparison-fig.ipynb loads an
    older results file and uses all its sessions, so the 64 values of the shared pipeline are a
    choice; checked against the code at commit 9674a6c.
  - Checked against the code at commit 9674a6c, no change needed. 19 units for both areas
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,77p wakhloo-2026.yaml
```

```
# The rat pipeline, shared by every rat claim (Methods, Rat data processing and Readout
# analysis; the code where the Methods are silent, as cited).
# - Sessions are the epochs of each file that hold trials, in order, the first eight
#   (process_rats.py, rat_utils.get_trl_dat; the notebook uses sessions 1 to 8).
# - Spikes binned at 500 ms. Position interpolated to bin centres by Nadaraya-Watson smoothing
#   with a Gaussian kernel, bandwidth 0.05 s (code); x and y velocity from position
#   differences, smoothed the same way with bandwidth 0.7 s (code).
# - Only bins with speed of at least 4 cm/s (Methods). The readout code takes speed as the
#   norm of the smoothed x and y velocity (rat_utils.process_dat); the GLM code takes the
#   dataset's own speed column (rat_utils.get_all_lat).
# - Units of the area kept when their mean rate in that session, over the kept bins, exceeds
#   0.1 Hz (Methods; code). Each unit centred on its session mean and divided by its session
#   standard deviation plus 0.02 Hz (0.01 counts per bin in the code).
# - Latents are x and y position and x and y velocity (d = 4), z-scored within the session.
# - Per random subset, a random set of units (Methods say 19 PFC and 24 CA1 units; the code
#   uses 19 for both areas, so 19 for CA1 is a variant) and a random set of 500 bins. Psi, Phi
#   and Omega are the covariances of the jointly centred units and latents of those 500 bins;
#   dimension, correlation, SNF and SSF are Eqs. 6 to 9 and the theoretical error is Eq. 5
#   with p = 300 (utils.get_geometry, utils.theory_part). The empirical error is the Hebbian
#   readout of Eq. 3 trained on 300 of the 500 bins and tested on the other 200, averaged over
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -o ".\{200\}\(19 \|24 \)\(PFC\|CA1\|units\|neurons\).\{200\}" paper/*.txt; grep -n -o ".\{300\}participation ratio of the.\{200\}" paper/*.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent**

## 1. Outcomes

The claims file has 27 claims. The attempt record gives an outcome for all 27: 12 blocked, 12 reproduced and 3 partially reproduced. No outcome in the record or the claims file is marked `assumed: true`, so there are no assumptions to judge.

- **Blocked (12): I agree.**
  - The theory and simulation claims (eq1 ×2, fig3bc, fig3dg, optimal-code-disentangled, eq2, fig6ce) are blocked as `other`.
  - fig4bf and fig4g are blocked as `not_runnable`. fig5d, fig5e and fig5h are blocked as `other`.
  - In round 1 I gave `data_missing` for the fig4 and fig5 claims. The author answered that the claims file marks these `data: elsewhere` (claims file lines 137–197), so `data_missing` does not apply. I accept that; it does not change the outcomes.
- **Reproduced (12): I agree with all of them.** They are svc-hebbian-correlation, fig7d, fig7e, figs12c, fig7f, fig7g, fig7h (reading a), fig7hk, fig7-late-reversal, and the three quadratic mixed-model claims. Every number in their notes matches cells 15–61.
- **mixed-linear-ssf-task-dim, partially reproduced: I agree.** CA1 SSF has P = 0.00106 raw and 0.00134 adjusted (cell 50).
- **glm-cross-validated-d2, partially reproduced: I agree.** The PFC s.d. is 0.057–0.066 under every reading, against 0.022 ± 0.0022 (cell 56). The paper's own GLM fits give the same 0.0599 and 0.0640 (cell 57).
- **late-trends-match-optimal, partially reproduced: I agree under the claims file as written, with one caveat.**
  - The claims file takes the task-relevant dimension on 19-unit sets because the code does (`format_glm_results`, claims file lines 62–70).
  - The paper's Methods, however, use "19 PFC units and 24 CA1 units" for the geometric terms. They then compute the GLM dimensionality "Just as with previous analyses" (paper line 262). That points to 24 CA1 units here too. The claims file makes the Methods' 24 the main reading for the readout but takes the code's 19 for the task dimension.
  - I report this as a possible misreading of the paper and do not correct it. It bears on this outcome: with 24-unit sets, reading (b) holds in CA1 (task-dimension slope +0.0130, P = 0.86, cell 53), and the claim would be reproduced. The record and cell 54 both state this, and note that the slope is essentially flat.

## 2. Text against the printed outputs

Every "**Result:**" cell and the Summary (cell 62) match the outputs, except one sentence:

- **Cell 25:** "the mean absolute difference is 11.55% (PFC) and 10.69% (CA1) … close to the 11.6% and 9.0% of the paper's own results file". The paper's 9.0% is for 19 CA1 units (cell 10), while 10.69% is for 24 units. The like-for-like figures are 8.91% here and 9.04% in the paper's file (cell 24). The outcome is unaffected, since this measure is not judged.

**README:**
- "It takes about 33 minutes on 4 cores" is not supported: cell 63 prints "total run time 17.0 min".
- Everything else matches, including the 5684 GLM fits (cell 12) and per-session agreement "within a fraction of a percent" (cell 10, largest about 0.7%).

**Attempt record:**
- **glm-cross-validated-d2 notes and response:** "same session D2 (largest difference 1.8e-09)" is not printed anywhere. Cell 57 gives 9.3e-11 (PFC) and 2.3e-09 (CA1).
- **verifications.reviewed:** "two blocked pairs with a different blocked_by" is wrong. In round 1 I gave a different `blocked_by` for five claims: the fig4 pair and the fig5 three.
- **Findings:** "most 15 to 16" minutes is only just true: 36 of the 64 sessions are 15.0–16.0 min (cell 4).
- The other notes, deviations and findings match the outputs.

**My round-1 reasons:** the record states them faithfully, as close paraphrases of my round-1 report, under every claim. Problems 1–7 are each attached to a claim. Problem 8 (random train/test bins drawn from autocorrelated 500 ms bins, which makes the empirical errors optimistic, a feature the paper's method shares) appears nowhere in the record. I marked it as not affecting a conclusion, but it bears on how to read the fig7f and fig7e empirical errors.

## 3. Round-1 points

- **Resolved:**
  - **3, PFC D2 s.d.:** the cause is now found. The paper's own fits match this attempt's to 1e-9 and give the same 0.0599 and 0.0640, so the gap is in the paper's 0.022, not in the fitting. The finding is recorded, and the s.e.m. is printed (0.0226 PFC, 0.0380 CA1).
  - **4, best-score selection:** `glm_summary` now uses `np.argmax` with a corrected docstring. The single nan unit is handled through the nan-mean reading (0.281).
  - **6, mixed-model table:** `rat_stats.csv` is now printed beside the notebook's table (cell 39), with γ signs agreeing in 14 of 14 models.
  - **1 and 7:** stated in the record and not conclusion-bearing. The SVC still runs on 4 subsets per session; on those same subsets the theoretical error gives r² = 0.931 and 0.829.
- **Not resolved, by nature:** point 2 (24 vs 19 CA1 units) remains the cause of the partial outcome for mixed-linear-ssf-task-dim. It is recorded as a code_mismatch finding.
- **Correction to my round 1, conclusion-bearing:** I called point 5 (task dimension on 19-unit sets in the CA1 24-unit row) "does not affect a conclusion". That holds only for reading (a). Under reading (b), 24-unit sets make late-trends-match-optimal hold in CA1 (cell 53). Whether that outcome is partially reproduced or reproduced therefore depends on the claims file's 19-unit choice, which may misread the Methods (section 1).
- **Still open, not conclusion-bearing:** point 8 is missing from the record.

## End of run

14 turns, 2 minutes, $1.21 at API prices, result: success.
