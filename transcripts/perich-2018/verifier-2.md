# 000688 · verifier-2 · run 41211605294

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 768
drwxr-xr-x 6 runner runner    4096 Oct 31 15:09 .
drwxr-xr-x 7 runner runner    4096 Oct 31 15:09 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 14:45 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 14:45 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 31 15:09 .claude
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .env
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .env.development
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .env.local
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .env.production
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .env.test
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .env.test.local
drwx------ 2 runner runner    4096 Oct 31 15:09 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 14:45 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 14:45 .github
-rw-r--r-- 1 runner runner       0 Oct 31 15:09 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 14:45 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 14:45 .mcp.json
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000688-perich-2018-01.yaml
```

```
<persisted-output>
Output too large (44.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/405171b9-1c76-4cf0-9773-427d5a8545e9/tool-results/bp16nibeh.txt

Preview (first 2KB):
# Perich, Gallego & Miller (2018) from dandiset 000688

Tests the findings of [Perich et al. (2018)](https://doi.org/10.1016/j.neuron.2018.09.030) that can
be tested on [DANDI:000688](https://dandiarchive.org/dandiset/000688/0.250122.1735). The dandiset
holds the Baseline epoch of the dual-array center-out sessions of Monkeys C and M, about 200 reward
trials each. The curl field, visuomotor rotation and Washout trials are not in it, and nothing marks
which sessions are the paper's.

| Claim | Outcome |
|---|---|
| Units per session and units above 5 Hz | Partially reproduced (assumed) |
| PMd has more dimensions than M1 (medians 14 and 8.5) | Reproduced (assumed) |
| PMd stays higher-dimensional in subsamples of equal size | Reproduced (assumed) |
| The null/potent index is centered on zero | Reproduced (assumed) |
| Output-null activity leads output-potent by 35 ms in Baseline | Partially reproduced (assumed) |
| 23 claims on the Force, Rotation and Washout trials | Blocked: data missing |
[... 27 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "000688-perich-2018-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000688-perich-2018-01
3	dataset:
4	  archive: dandi
5	  id: "000688"
6	  version: 0.250122.1735
7	  doi: 10.48324/dandi.000688/0.250122.1735
8	paper: doi:10.1016/j.neuron.2018.09.030
9	date: '2026-10-31'
10	entry: 000688-perich-2018
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 583 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_perich_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}] id={c.get('id')}")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--', o.get('ename'), o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -n "######## CELL" $TMPDIR/nb.txt
```

```
1617 /tmp/claude-1001/nb.txt
2:######## CELL 0 [markdown] id=3b594348
34:######## CELL 1 [code] id=d17eaa18
77:######## CELL 2 [markdown] id=bcb5d84d
82:######## CELL 3 [code] id=4496b9b3
253:######## CELL 4 [markdown] id=9eb10a5f
267:######## CELL 5 [code] id=298f84fe
318:######## CELL 6 [markdown] id=4e8c15a4
329:######## CELL 7 [code] id=efb2f673
402:######## CELL 8 [markdown] id=27dc7fbe
428:######## CELL 9 [code] id=bf9734a4
593:######## CELL 10 [markdown] id=11966106
598:######## CELL 11 [markdown] id=c310bb8a
611:######## CELL 12 [code] id=865e12fa
690:######## CELL 13 [code] id=b0a985e1
712:######## CELL 14 [markdown] id=2b75ac06
725:######## CELL 15 [markdown] id=062db055
741:######## CELL 16 [code] id=cda888a0
832:######## CELL 17 [code] id=76645d96
941:######## CELL 18 [code] id=c9e93fa1
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 720
}
```

```
1	
2	######## CELL 0 [markdown] id=3b594348
3	# Reproducing Perich, Gallego & Miller (2018) from dandiset 000688
4	
5	**Paper.** Perich MG, Gallego JA, Miller LE (2018). A neural population mechanism for rapid
6	learning. *Neuron* 100, 964-976.
7	[doi:10.1016/j.neuron.2018.09.030](https://doi.org/10.1016/j.neuron.2018.09.030). The claims file
8	was written from the accepted author manuscript in PubMed Central (PMC6250582), with its eight
9	supplement files (Figures S1 to S7 and their legends); this attempt read the same text.
10	
11	**Dandiset.** [DANDI:000688](https://dandiarchive.org/dandiset/000688/0.250122.1735), version
12	0.250122.1735. The paper cites no DANDI version (it predates the dandiset). This is the only
13	published version; the draft has the same 111 files and was modified two days later, so the
14	published version is pinned.
15	
16	**What the dandiset holds.** 111 sessions of four monkeys (C, J, M, T) in center-out (CO) and
17	random-target (RT) reaching, with sorted units, cursor kinematics and a trial table. The trial
18	tables have no column for the epoch (Baseline, Force or Rotation, Washout) or the perturbation,
19	and none of the files is described as a curl field or visuomotor rotation session. The dual-array
20	(M1 and PMd) center-out sessions of Monkeys C (2016) and M (February and March 2014) have unit
[... 700 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 720,
 "limit": 500
}
```

```
720	(within 10% of 918) and 1565 PMd (outside). Rates over every trial of the file give the same counts
721	within 10 units. Monkey M has few PMd units above 5 Hz (6 to 21 per session). The pooled verdicts
722	in the first table are for each whole set, not for 16 sessions; the second cell gives the test on
723	16 sessions.
724	
725	######## CELL 15 [markdown] id=062db055
726	## fig3b-pmd-higher-dimensional
727	
728	> In every session the PMd manifold had more dimensions than the M1 manifold (median 14 against 8.5).
729	
730	Method from STAR Methods, Dimensionality reduction, paragraph 2 (helper `dimensionality`): Baseline
731	reward trials, rates as M2, trial-averaged per target; noise from differences between random pairs
732	of trials to the same target, 1000 repetitions, the 99% limit of each noise eigenvalue. Readings:
733	threshold rule (a) or (b) (O9), window (a) target onset to acquisition or (b) the whole trial (O3),
734	kernel width as a standard deviation or a full width at half maximum (O4), and the scale of the
735	noise, which the paper does not give (raw differences, the text's wording; difference / sqrt 2;
736	difference / sqrt(2K), the noise of an average of K trials). All units of each area are used.
737	The claims file expected the kernel reading (O4) not to change an outcome; here it does, and the
738	results are shown under both. The paper's 16 sessions are 9 of the 14 Monkey C candidates and the 7
739	Monkey M sessions; the medians are also computed for every such choice.
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1219,
 "limit": 400
}
```

```
1219	## figs4c-null-potent-index-centered
1220	
1221	> Single neurons contributed to both output-potent and output-null subspaces; the null/potent index
1222	> was centered on zero with virtually no neurons near -1 or 1.
1223	
1224	Index per PMd neuron from the product of the PCA loading matrix (16 PMd components) and V (M3, O7),
1225	as (sum of absolute potent weights - sum of absolute null weights) / (sum of both); the sum of
1226	squares is the second reading. Reproduced when the mean over neurons lies between -0.1 and 0.1 and
1227	fewer than 1% of neurons have an absolute index above 0.9. All PMd units of the candidate sessions
1228	are pooled. The control shuffles the potent weights across neurons against the null weights, 1000
1229	times per session (STAR Methods, "randomly shuffling the weights across neurons").
1230	
1231	######## CELL 25 [code] id=5fc9e5e5
1232	rng = np.random.default_rng(5)
1233	rows, pooled = [], {}
1234	for (sid, window, kern), fit in fits.items():
1235	    for power in (1, 2):
1236	        idx = perich.null_potent_index(fit["PMd"]["axes"], fit["potent"], fit["null"], power)
1237	        pooled.setdefault((window, kern, power), {})[sid] = idx
1238	summ = []
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^  - id:\|^[a-z_]*:" 10.1016-j.neuron.2018.09.030.yaml | head -80
```

```
123:schema_version: 2
124:dataset:
127:paper: doi:10.1016/j.neuron.2018.09.030
128:claims:
703:checks:
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuron.2018.09.030.yaml"
}
```

```
1	# Claims for Perich, Gallego & Miller (2018), "A Neural Population Mechanism for Rapid Learning",
2	# Neuron 100, 964-976, on dandiset 000688.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
5	# pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the accepted author manuscript in PubMed Central (PMC6250582, NIHMS1507895), as served
8	# by ncbi_pmc, not the version of record: main text, figure legends 1 to 7 and STAR Methods, with
9	# its eight supplement files (NIHMS1507895-supplement-1 to -8). Supplements 1 to 7 are the main
10	# Figures 1 to 7 as images; supplement 8 holds Figures S1 to S7 with their legends. Figure panels
11	# and the p-values printed inside them (Figures 3E, S5F, S7A, S7D) were read from the PDFs. The
12	# figure letters of the manuscript do not all agree with the Results: the Results cite Figure 3E,F,G
13	# and 4E where the legends call the same panels 3E, 3F, 3G and 4D; Figure 6 has two panels "d" in
14	# its legend (the lag histogram is panel C in the image). Sources below give both where they differ.
15	#
16	# Code: the paper links no code. Data and Software Availability says "Custom code was used to
17	# process the neural and kinematic data ... This code may be shared upon reasonable request", and
18	# names the MATLAB functions used (cov, pca, factoran, glmfit, mahal). No repository was read. Every
19	# method below is from the STAR Methods, the legends or the Results.
20	#
[... 701 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|KERNEL_SD_S\|LAGS_S\|CANDIDATE" perich.py | head -40
```

```
16:  STAR Methods, Dimensionality reduction (M2). `KERNEL_SD_S` holds both readings of the width
69:CANDIDATE_SESSIONS = [
82:KERNEL_SD_S = {"sd": 0.100, "fwhm": 0.100 / 2.3548}  # O4 readings
88:LAGS_S = np.round(np.arange(-0.35, 0.3501, 0.01), 3)
92:def asset_urls() -> dict[str, str]:
104:def _text(x):
108:def read_metadata(url: str) -> dict:
132:def load_session(sid: str, url: str) -> dict:
165:def _acquisition_times(trials, corners, t, pos):
180:def initial_errors(sess, onset_frac=0.2, after_s=0.150):
207:def load_sessions(sids, urls, workers=8):
212:def baseline_trials(sess: dict, window: str) -> pd.DataFrame:
219:def trial_bounds(tr: pd.DataFrame, window: str):
226:def binned(spikes, starts, ends, bin_s):
235:def smooth(counts_list, bin_s, kernel_sd_s):
240:def mean_rates(spikes, tr):
247:def pca_axes(X: np.ndarray, k: int):
254:def subspaces(m1_latent: np.ndarray, pmd_latent: np.ndarray):
265:def null_potent_index(loadings: np.ndarray, potent: np.ndarray, null: np.ndarray, power: int = 1):
273:def target_averages(rates_list, target_ids, n_bins):
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "perich.py",
 "offset": 283,
 "limit": 130
}
```

```
283	def _eigs(X):
284	    """Eigenvalues (descending) of the covariance of data (..., time, neurons), from the smaller Gram matrix."""
285	    Xc = X - X.mean(-2, keepdims=True)
286	    rows, cols = X.shape[-2:]
287	    G = np.swapaxes(Xc, -1, -2) @ Xc if cols <= rows else Xc @ np.swapaxes(Xc, -1, -2)
288	    ev = np.clip(np.linalg.eigvalsh(G)[..., ::-1], 0, None) / (rows - 1)
289	    out = np.zeros(X.shape[:-2] + (cols,))
290	    out[..., :ev.shape[-1]] = ev[..., :cols]
291	    return out
292	
293	
294	def dimensionality(rates_list, target_ids, rng, n_bins=None, reps=NOISE_REPS, chunk=100):
295	    """Machens et al. (2010) style dimensionality, as the Methods adapt it (O9 readings).
296	
297	    Data: trial-averaged rates per target, trials aligned on the window start and cut to n_bins
298	    (default the shortest trial). Noise: the difference between two random trials to the same
299	    target, concatenated over targets, `reps` times; the 99th percentile of each noise eigenvalue.
300	    The scale of the noise is not given; readings: "raw" (the difference, as the text says),
301	    "sqrt2" (difference / sqrt 2, the single-trial noise) and "sqrt2K" (difference / sqrt(2 K),
302	    the noise of an average of K trials, K the mean number of trials per target).
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" 10.1016-j.neuron.2018.09.030.yaml; python3 -c "
import yaml;r=yaml.safe_load(open('000688-perich-2018-01.yaml'));from collections import Counter
print(len(r['outcomes']),Counter(o['outcome'] for o in r['outcomes']));print(len(r['verifications'][0]['results']))
c={x['id'] for x in yaml.safe_load(open('10.1016-j.neuron.2018.09.030.yaml'))['claims']};print(c^{o['claim'] for o in r['outcomes']})"
```

```
28
28 Counter({'blocked': 23, 'reproduced': 3, 'partially_reproduced': 2})
28
set()
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "gaussian\|machens\|random pairs\|subtract" 10.1016-j.neuron.2018.09.030.txt | head -20
```

```
234:the variability across trials ( Machens et al.,
584:memory ( Machens et al., 2010 ). In the
620:has been described in prefrontal cortex for decision-making ( Mante et al., 2013 ), working memory ( Machens et al., 2010 ), and rule-learning ( Durstewitz et al., 2010 ), in the motor
748:for each trial with a non-causal Gaussian kernel of width 100 ms to compute
761:method developed by ( Machens et al.,
767:the trial-to-trial variation in the activity of each neuron. We subtracted
768:the activity of each neuron between random pairs of trials for each reach
835:each time point by subtracting the value at a reference point and normalizing by
859:extend Gaussian multilinear regression approaches to the Poisson statistics
931:to the R 2 commonly used in model-fitting with Gaussian
944:are smaller in magnitude than those typically found with the Gaussian
1099:adapting to an external force field . Neuron 30 , 593 – 607 . 11395017 10.1016/s0896-6273(01)00301-4 Machens CK , Romo R , and Brody CD ( 2010 ). Functional, but not anatomical,
1764:for each of the eight targets. Neural activity was smoothed with a Gaussian kernel, aligned to the go cue (indicat-
```

**Agent calls Bash**

```bash
cd paper; sed -n 755,780p 10.1016-j.neuron.2018.09.030.txt; sed -n 228,240p 10.1016-j.neuron.2018.09.030.txt
```

```
the firing of nearly all individual neurons. For the control in Figure S7F , we
repeated our analysis using Factor Analysis (factoran in Matlab, The
Mathworks Inc) instead of PCA to achieve the dimensionality reduction. We
assumed the same dimensionalities for M1 and PMd that we used for the PCA
analysis (8 and 16, respectively). For the output-null and output-potent subspace analysis described
below, we needed to select dimensionalities for M1 and PMd. We adapted a
method developed by ( Machens et al.,
2010 ) to estimate the dimensionality of our recorded populations.
In brief, PCA provides an orthogonal basis set (the principal axes) with the
same dimensionality as the neural input. However, the variance captured by
many of the higher dimensions (with the smallest eigenvalues) is typically
quite small. We estimated the noise in the neural activity patterns using
the trial-to-trial variation in the activity of each neuron. We subtracted
the activity of each neuron between random pairs of trials for each reach
direction. This gave an estimate of the variation in spiking of each neuron
(trial-to-trial noise) across targets. We then ran PCA on the neural
“noise” provided by this difference for all targets. We
repeated this 1000 times, giving a distribution of eigenvalues for each of
these noise dimensions. We used the 99% limit of these distributions to
estimate the amount of noise variance explained for each dimension. This
[... 19 more lines not kept]
```

**Agent**

**Verifier report, round 2: Perich, Gallego & Miller 2018 on DANDI:000688 (0.250122.1735)**

The claims file has 28 claims and the attempt record has 28 outcomes, one for each claim: 3 reproduced, 2 partially_reproduced and 23 blocked (data_missing).

### 1. Outcomes and assumptions

| Claim | Record | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| methods-neuron-counts | partially_reproduced, assumed | Yes | Yes. The per-session ranges hold only if C 2016-09-29 (PMd 114) is not one of the paper's sessions, which is true for 715 of 2002 choices. The pooled >5 Hz counts fail under every choice. |
| fig3b-pmd-higher-dimensional | reproduced, assumed | Yes, but fragile | Partly. The noise scale (difference / √(2K)) is stated, along with the fact that it was chosen after the other scales gave 0. It is a reasonable assumption. The FWHM-kernel reading is stated. Not stated as something the outcome rests on: the 21-session set. Over 16-session choices the medians are within tolerance in only 910 of 2002 (cell 17); the rest would be partial. The record names the session set as an assumption for fig6c but not here. |
| figs4d-dimensionality-robust-to-size | reproduced, assumed | Yes | Yes. It rests on the same noise scale, but PMd > M1 holds under rule (b) at every size, under both kernels, both windows and both session sets (cell 21). |
| figs4c-null-potent-index-centered | reproduced, assumed | Yes | Yes. The adopted reading (absolute values) is the claims file's first reading. One of eight readings fails at 0.100085 (cell 25). Judged alone, Monkey M would fail (0.109). Both points are stated. |
| fig6c-null-leads-potent | partially_reproduced, assumed | Yes, as the criterion applies on 21 sessions. Weak. | Both assumptions are stated: all 21 sessions and the SD kernel. Under the main reading only 763 of 2002 (38%) 16-session choices are significant. With the FWHM kernel no reading is significant (p ≥ 0.18, cell 28), which would make it not reproduced. |
| 23 blocked claims | blocked, data_missing | Yes | Not applicable. No Force, Rotation or Washout trials (cells 3–8). |

**A point I missed in round 1, which bears on fig3b, fig6c and figs4c.** Lines 85–87 of the claims file say that when the readings of an open detail disagree, the claim is blocked as methods_underspecified. The fig3b and fig6c criteria instead say "under one reading". O4 (the kernel width) is named in neither criterion, and the claims file expected it "not to change an outcome".

- The record applies "one reading" to O4 without mentioning the header rule.
- No single kernel reading supports both outcomes:
  - FWHM: fig3b reproduced, fig6c not reproduced.
  - SD: fig3b partial, fig6c partial.
- The record picks the favourable kernel for each claim.

The record should say which rule governs O4 and state the inconsistency between the two claims. This is an internal inconsistency in the claims file, not a misreading of the paper.

### 2. Sentences the outputs do not support

- **Cell 4:** "plus four later Monkey M sessions (2014-09-29, 2014-12-03, 2015-05 and 2015-06) whose PMd counts (22 to 124) and reward counts (194 to 733) do not fit the paper's ranges."
  - Cell 3 lists 13 later dual-array CO sessions, not four.
  - Their rewards run from 174, not 194. The June 2015 sessions (174–196) fall inside the Baseline range.
  - M 2014-09-29 (PMd 124) and M 2015-05-12 (PMd 60, M1 30) are inside the widened Monkey M ranges. 2015-05-12 is excluded only by its 443 rewards, while C 2016-10-13 and 2016-10-21, which are also outside the reward range, are kept.
  - Little effect on the conclusions: the 7 February–March sessions match the paper's bounds exactly (66, 121 and 26 in cell 12).
- **Cell 0:** these sessions "have unit counts that match the paper's ranges". C 2016-09-29 does not (cell 12).
- **Cell 8:** "in every session the mean absolute deviation of the first eight reward trials is close to that of the last eight, except in C 2016-09-23 and C 2016-10-11".
  - M 2014-03-03 gives 14.0 against 6.4, with signed means of 10.2 and 3.3 and a significant trend (p = 0.019). M 2014-02-03 and 2014-02-18 give 9.1/5.6 and 8.8/4.8 (cell 7).
  - The cell does not mention that C 2016-10-11 has a significant decreasing absolute deviation (rho −0.21, p = 0.003).
  - This affects no conclusion.
- **Cell 23 and the figs4d notes in the record:** "both areas fall at small sizes (… M1 8.52 to 8.03)".
  - The M1 means at 60 and 70 neurons (8.53 and 8.65) equal or exceed the all-neuron mean.
  - The 40-neuron mean covers 17 sessions, against 21 for "all".
  - In window (b) with the FWHM kernel, M1 at 40 (6.74) exceeds "all" (6.52) (cell 21).
  - A fall in M1 is not shown. This is outside the criterion.
- **Record finding (metadata_error):** "the cursor never enters the square … Monkey M 2014-02-03 and 2014-02-18". Cell 7 gives 0.01 for both.
- **Record verification, figs4d reason:** "25 subsamples with 100 noise repetitions were used instead of 100". My point was 25 subsamples instead of 100, and 100 noise repetitions instead of 1000. The record's other restatements of my round-1 reasons are faithful, including the archive check appended to each blocked claim.

All other numbers in the conclusions of cells 14, 19, 23, 26 and 31, the Summary (cell 33), the README and the record's notes match the printed outputs.

### 3. Round-1 points

**Resolved:**
- 1: session dependence of fig6c is now tested and stated.
- 2: edge maxima are flagged; without them the mean is −20.5 ms, p = 0.034.
- 5: the figs4d justification is corrected.
- 8: the cut-off warning is read and recorded as a finding.
- 9: signed errors are now printed.
- 10: the pooled verdict is relabelled.
- 11: the Monkey M bias is stated.

From "could not check":
- The FWHM values per session and the medians over 16-session choices are printed.
- The unrounded figs4c mean is printed.
- The lag curves are plotted for all four window and resolution readings.
- The warning text is truncated in the source.
- The acquisition-time check is consistent: movement ends 0.09–0.15 s after the assumed acquisition time.

**Partly resolved, does not affect a conclusion:**
- 6: 100 subsamples are now used, but still 100 noise repetitions; this is stated.
- 7: the window (b) alignment is stated as a deviation but not changed.

**Remaining, bearing on a conclusion:**
1. **Kernel width (point 3):** now stated, but there is the cross-claim inconsistency and the unaddressed header rule from part 1. This affects fig3b and fig6c, and figs4c through its one failing reading.
2. **fig6c session set:** stated, but the result holds for only 38% of 16-session choices (51% for any of the 8 readings).
3. **fig3b session set:** reproduced in 910 of 2002 16-session choices. This should be named as part of what the outcome rests on.
4. **Noise scale (point 4):** stated and sent to the authors as a question. The synthetic check (cell 18) does not tell the scales apart, since raw and √2 also return 5 there. The choice rests on the other scales giving 0 on the real data.
5. **Whether the units are the paper's sort:** still open. It bears on methods-neuron-counts.

## End of run

15 turns, 3 minutes, result: success.
