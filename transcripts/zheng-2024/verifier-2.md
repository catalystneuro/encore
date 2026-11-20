# zheng-2024 · verifier-2 · run 44741537958

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 436
drwxr-xr-x 6 runner runner    4096 Nov 20 13:43 .
drwxr-xr-x 8 runner runner    4096 Nov 20 13:43 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 20 13:07 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 20 13:07 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 20 13:43 .claude
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .env
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .env.development
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .env.local
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .env.production
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .env.test
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .env.test.local
drwx------ 2 runner runner    4096 Nov 20 13:43 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 20 13:07 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 20 13:07 .github
-rw-r--r-- 1 runner runner       0 Nov 20 13:43 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 20 13:07 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 20 13:07 .mcp.json
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; diff zheng-2024-01.yaml zheng-2024.yaml | head -50; wc -l *.yaml
```

```
# Zheng, Huszár, Hainmueller, Bartos, Williams & Buzsáki (2024) from dandiset 000552

Tests the electrophysiology findings of [Zheng et al. (2024)](https://doi.org/10.1016/j.celrep.2024.114702)
on [DANDI:000552](https://dandiarchive.org/dandiset/000552/0.261113.1035), the CA1 silicon-probe
recordings of mice running a spontaneous alternation task on a figure-8 maze, three of which also ran
in novel mazes. It detects place fields and their step-like switches in 45 familiar and 8 novel
sessions, and tests electrode drift on the wide-band signal of one session. The two-photon imaging of
Figure 7 is not deposited.

| Claim | Outcome |
|---|---|
| Population vectors decorrelate with trial lag (Fig. 1D) | Reproduced |
| Faster drift in novel environments over lags 1 to 10 (Fig. 1E) | Reproduced |
| No difference over lags 11 to 30 (Fig. 1E) | Reproduced |
| Field peak rates decorrelate, field locations stay correlated (Fig. 1H) | Reproduced |
| Field-location distance still grows with lag (Fig. 1I) | Reproduced |
| The 40% step filter removes 212 of 3,184 putative switching fields | Not reproduced |
| 19% of familiar and 31% of novel fields switch (Fig. 2D) | Not reproduced |
| Switching is graded by experience (Fig. 2E) | Reproduced |
| Step models beat polynomials for over 96% of fields (Fig. 3D to F) | Partially reproduced |
[... 91 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "zheng-2024-01.yaml"
}
```

```
1	schema_version: 3
2	id: zheng-2024-01
3	datasets:
4	- archive: dandi
5	  id: "000552"
6	  version: 0.261113.1035
7	  doi: 10.48324/dandi.000552/0.261113.1035
8	  relation: reuses
9	paper: doi:10.1016/j.celrep.2024.114702
10	date: 2026-11-20
11	entry: zheng-2024
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 875 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_zheng_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}] ########")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--\n'+''.join(o['data']['text/plain']))
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -n "######## CELL" $TMPDIR/nb.txt | wc -l
```

```
2583 /tmp/claude-1001/nb.txt
109
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	
2	######## CELL 0 [markdown] ########
3	# Reproducing Zheng et al. (2024) from dandiset 000552
4	
5	Paper: Zheng, Huszár, Hainmueller, Bartos, Williams and Buzsáki (2024), "Perpetual step-like restructuring of hippocampal circuit dynamics", Cell Reports 43, 114702, doi:10.1016/j.celrep.2024.114702. The claims file (`claims/zheng-2024.yaml`) was written from the author manuscript in PubMed Central (PMC11485410) with the STAR Methods and the supplement of the version of record.
6	
7	Dataset: DANDI:000552, "High density CA1 recordings on a figure-8 maze" (Huszár et al. 2022), version 0.261113.1035, streamed from the archive.
8	
9	Why this version. The paper cites 0.230630.2304. That version's units tables hold spike times only: no putative cell type, which the paper's selection of putative pyramidal cells needs for every claim, and no light-responsive label, which the ChR2 claim needs; its trial tables also mark familiar trials as not familiar in at least one session. Version 0.261113.1035 is a re-conversion of the same sessions from the lab's files (its release notes), with the lab's CellExplorer cell types, the light-responsive label built from the paper's criteria, per-environment position and named epochs. The data-check section shows that the spike times of a session are identical in the two versions and that the cited one lacks the labels. The protocol asks for the cited version; it does not hold the variables the claims need, so the later version is pinned and the departure is recorded.
10	
11	Code read for method details: the paper's code, github.com/samdeoxys1/within-session-representationl-drift at tag v0.0 (commit 93d6e33d813291e0a5a0dcce39a335fc2d8ce13c, Zenodo doi:10.5281/zenodo.13247193).
12	
13	| Claim | Tested |
14	|---|---|
15	| fig1d-pv-decorrelation, fig1e-novel-drift-faster, fig1e-later-lags-no-difference | tested |
16	| fig1h-rate-decorrelates-location-stable, fig1i-location-mse-increases | tested |
17	| switch-step-size-filter, fig2d-switch-fra
[... 683 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 700
}
```

```
700	######## CELL 31 [markdown] ########
701	### `fig2e-switch-fraction-by-experience`
702	
703	> The fraction of switching fields per session is lowest in animals that experienced only the familiar maze (median 0.15), higher in familiar sessions of animals that also experienced a novel environment that day (0.22) and highest in novel sessions (0.3).
704	
705	Paper (Results, Within-session representational drift, paragraph 3; Figure 2E): "These animals had higher fractions of switching fields ("Familiar" in Figure 2E) than the "Familiar only" animals"
706	
707	"Familiar" sessions are the familiar-maze sessions of e13_26m1, e15_13f1 and e16_3m2; 11 here, as e13_26m1_210913 is not in the dandiset.
708	
709	######## CELL 32 [code] ########
710	# claim:fig2e-switch-fraction-by-experience
711	SF = FD.groupby(["session", "animal", "env", "familiar"]).sw.mean().reset_index()
712	SF["group"] = np.where(~SF.familiar, "Novel", np.where(SF.animal.isin(sw.NOVEL_ANIMALS), "Familiar", "Familiar only"))
713	print(SF.groupby("group").sw.agg(["count", "median", "min", "max"]).round(3).to_string())
714	grp = {k: g.sw.values for k, g in SF.groupby("group")}
715	for a, b in [("Familiar only", "Familiar"), ("Familiar", "Novel"), ("Familiar only", "Novel")]:
716	    print(f"{a} against {b}: rank-sum p = {stats.ranksums(grp[a], grp[b]).pvalue:.2g}, medians {np.median(grp[a]):.3f} and {np.median(grp[b]):.3f}")
717	--OUT--
718	               count  median    min    max
719	group                                     
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1400,
 "limit": 700
}
```

```
1400	for fam, g in TR.groupby("familiar"):
1401	    print(f"{'familiar' if fam else 'novel'}: switches per field on the last two trials of a session, ON {g[g.trial >= g.n_sess - 2].on.mean():.4f}, OFF {g[g.trial >= g.n_sess - 2].off.mean():.4f}; on other trials from the fourth on, ON {g[(g.trial >= 3) & (g.trial < g.n_sess - 2)].on.mean():.4f}, OFF {g[(g.trial >= 3) & (g.trial < g.n_sess - 2)].off.mean():.4f}")
1402	for fam, g in TR[(TR.trial >= 3) & (TR.trial < TR.n_sess - 2)].groupby("familiar"):
1403	    g = g.copy(); g["tz"] = g.groupby("session").trial.transform(lambda x: (x - x.mean()) / x.std())
1404	    for k in ("on", "off"):
1405	        pr = stats.pearsonr(g.tz, g[k])
1406	        print(f"variant, trials from the fourth to the third from last, {'familiar' if fam else 'novel'} {k.upper()}: trials {len(g)}, r = {pr[0]:.3f} (p = {pr[1]:.2g})")
1407	--OUT--
1408	novel ON: trials 312, Pearson r = 0.051 (p = 0.37); Spearman variant rho = 0.044 (p = 0.44)
1409	novel OFF: trials 312, Pearson r = -0.021 (p = 0.71); Spearman variant rho = -0.057 (p = 0.32)
1410	familiar ON: trials 1166, Pearson r = 0.072 (p = 0.014); Spearman variant rho = 0.074 (p = 0.011)
1411	familiar OFF: trials 1166, Pearson r = -0.002 (p = 0.94); Spearman variant rho = 0.013 (p = 0.65)
1412	trials per session: 9 to 68
1413	variant, trials from the fourth on, novel ON: trials 288, r = -0.083 (p = 0.16)
1414	variant, trials from the fourth on, novel OFF: trials 288, r = -0.145 (p = 0.014)
1415	variant, trials from the fourth on, familiar ON: trials 1031, r = -0.065 (p = 0.037)
1416	variant, trials from the fourth on, familiar OFF: trials 1031, r = -0.125 (p = 6e-05)
1417	novel: switches per field on the last two trials of a session, ON 0.0002, OFF 0.0005; on other trials from the fourth on, ON 0.0080, OFF 0.0053
1418	familiar: switches per field on the last two trials of a session, ON 0.0009, OFF 0.0003; on other trials from the fourth on, ON 0.0059, OFF 0.0037
1419	variant, trials from the fou
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 2100,
 "limit": 500
}
```

```
2100	def fp_rate(within_turn, nsess=200, nshuf=200):
2101	    hits = 0
2102	    for _ in range(nsess):
2103	        n = 30; trials = {"L": np.arange(0, n, 2), "R": np.arange(1, n, 2)}
2104	        m = np.zeros(n, int); evs = []
2105	        for k in range(60):
2106	            trs = trials["L" if k % 2 else "R"]; nf = len(trs)
2107	            pos = np.array([rng_fp.integers(2, nf - 1)]) if rng_fp.random() < 0.3 else np.array([], int)
2108	            if len(pos):
2109	                evs.append((trs, pos)); m[trs[pos]] += 1
2110	        stat = (m * (m - 1) // 2).sum()
2111	        M = np.zeros((nshuf, n), int)
2112	        for trs, pos in evs:
2113	            lo, hi = (2, len(trs) - 1) if within_turn else (2, n - 1)
2114	            base = pos if within_turn else trs[pos]
2115	            span = hi - lo; sh = rng_fp.integers(span - 1, size=nshuf)
2116	            newp = lo + (base[None, :] - lo + sh[:, None]) % span
2117	            idx = trs[newp] if within_turn else newp
2118	            np.add.at(M, (np.repeat(np.arange(nshuf), len(pos)), idx.ravel()), 1)
2119	        hits += ((M * (M - 1) // 2).sum(1) >= stat).mean() < 0.05
[... 465 more lines not kept]
```

**Agent**

Notebook read through. Now checking the claims file's criteria for the claims whose outcome changed or rests on an assumption.

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  - id:\|^  id:" zheng-2024.yaml | head -50; grep -c "^- id:" zheng-2024.yaml
```

```
82:- id: fig1d-pv-decorrelation
98:- id: fig1e-novel-drift-faster
124:- id: fig1e-later-lags-no-difference
147:- id: fig1h-rate-decorrelates-location-stable
163:- id: fig1i-location-mse-increases
178:- id: switch-step-size-filter
196:- id: fig2d-switch-fractions
233:- id: fig2e-switch-fraction-by-experience
272:- id: fig3df-step-beats-polynomial-fields
292:- id: fig3df-polynomial-beats-step-population
308:- id: figs4g-population-vectors-gradual
345:- id: fig3k-switch-abrupt
371:- id: figs5-switchers-drive-drift
405:- id: fig4-glm-deviance
437:- id: fig4-delay-zone-more-switching
450:- id: fig4di-switching-decreases-with-trial
500:- id: fig4-behavior-not-predictive
518:- id: figs8-speed-no-trend
550:- id: fig4no-head-scans-not-related
566:- id: figs9-splitter-switching
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 98,124p zheng-2024.yaml; sed -n 405,566p zheng-2024.yaml; sed -n 728,849p zheng-2024.yaml; sed -n 915,981p zheng-2024.yaml
```

```
- id: fig1e-novel-drift-faster
  statement: Over trial lags 1 to 10, population vectors decorrelate faster (a more negative slope)
    in novel than in familiar environments.
  source: Results, Within-session representational drift, paragraph 1; Figure 1E
  quote: Linear regression revealed that drift was significantly faster in novel environments
    (larger negative slope) within the first 1-10 trial lags
  statistics:
  - test: Wilcoxon rank-sum test
    p: 0.02
    statistic: Cohen's d = 0.58
    n: 106 session and turn units
  expected:
  - quantity: number of session and turn units, lags 1 to 10
    value: 106
    tolerance: 10.6
  - quantity: Cohen's d, familiar against novel slopes, lags 1 to 10
    value: 0.58
    tolerance: 0.058
  depends_on:
  - fig1d-pv-decorrelation
[... 358 more lines not kept]
```

**Agent**

Checking the paper's Figure S8, S1 and 4D legends to test the assumptions the changed outcomes rest on.

**Agent calls Bash**

```bash
cd paper; grep -n -i "Figure S8\|S8C\|S8A" *.txt | head; grep -n -i "Figure S1[^0-9]\|S1H\|amplitude" *.txt | head -20
```

```
147:Are “switches” in place field activity affected by sensory, cognitive, or behavioral factors? To investigate, we used a Poisson generalized linear model to predict the number of place field switches per trial within five distinct segments of the maze (delay zone, central arm, left/right choice arm, return side arm, and pre-delay zone; Figure 4K). The number of switches was predicted from four categorical variables—animal identifier, maze segment (“position”), current trial correct/incorrect, and previous trial correct/incorrect—and three numeric variables: trial number, average speed, and number of active place fields. The model explained 20% of the deviance for switching ON and 14% for switching OFF. We examined the importance of each predictor by leaving it out and computing the decrease in cross-validated explained deviance compared to the full model. We found that the variables that explained most of the variance were the animal labels (i.e., individual differences), the maze corridors, and the number of place fields, for both switching ON and switching OFF fields (Figures 4A–4C, 4F, and 4G). Trial numbers (Z scored within a session) contributed less to switching ON but more to switching OFF. The contribution from position and trial suggested that the occurrence of switching was not homogeneous across space and time. Although the distribution of switching across arms was variable across sessions and animals (Figure S6), consistently more ON/OFF switching occurred in the delay zone (Figures 4B–4G, 4E, and 4J). However, we did not find any reliable behavioral signature (average speed, variability of speed, or fraction of time spent locomoting; see STAR Methods) or neural signature (average pyramidal cell or interneuron activities or excitation/inhibition [E/I] ratio) that separated the delay zone from other parts of the maze (Figure S7). As expected, switching probability decreased as a function of the trial number, reflecting the graded influence of novelty d
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 665,700p *.txt; grep -n -i "speed.*trial\|trial.*speed" *.txt | grep -iv "^147" | head -20
```

```
Fig. S1. Switching dynamics is not an artifact of electrode drift 
A) The mean amplitude of each clustered spike (dots) averaged over all spikes that occurred 
during the post-sleep vs pre-sleep session, for an example session. The color indicates 
whether the neuron had switching fields during the behavior session. The unit is in the 
template space of Kilosort. B) Same information as in A, showing the average post minus 
pre waveform amplitude for each neuron, separated into the categories as in A. C) 
Ratemaps of example switching neurons also argue against electrode drift as the 
explanation of the main finding of the paper. Top: one field (between the vertical lines) 
switched ON in the middle of the session, while the other field of the same neuron was 
stable throughout the session. Middle: the place field switched OFF first and then back 
ON again. The neuron had sporadic activities outside of the field while the field was 
OFF. Bottom: the neuron with a field that switched OFF (between the vertical lines) and 
another field that switched ON later in the session. D) A ratemap of an example switch-ON, 
switch-OFF neuron (neuron 150). E) Waveforms of three example neurons (99, 184, 313) 
recorded from the same site as the neuron in D. The 3 neurons had the maximum amplitude on 
the same silicon probe site.  Shown are the averages from spikes that occurred 20s before (blue) 
and after (orange) the switch of the place field in D. The shaded region marks the 95% confidence 
intervals (CI). F) Same displays as in D and E, except the switching off is highlighted and serves 
as the reference for G. H) (left and middle) 2D histograms of the Post- vs Pre-switch spike 
amplitudes for neurons recorded simultaneously with switcher (reference) neurons. Each data 
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 836,846p *.txt
```

```
Fig. S8: Relationship between speed and switching and trial. A) Number of switch-ON fields 
normalized by the number of fields versus the average speed within an arm on a given trial. B) 
Same as A, for switch-OFF fields. C) Speed (z-scored within each session) vs trial. Blue - 
familiar environment (Pearson r = 0.01, p = 3 x 10–11). Orange - novel environments (Pearson r = 
–0.02, p = 0.78).
```

**Agent**

Checking the remaining criteria (figs14, figs13, fig1e-later) before writing up.

**Agent calls Bash**

```bash
cd  sed -n 124,147p zheng-2024.yaml; sed -n 578,623p zheng-2024.yaml; sed -n 864,892p zheng-2024.yaml; sed -n 308,345p zheng-2024.yaml | grep -A8 criterion
```

```
- id: fig1e-later-lags-no-difference
  statement: Over trial lags 11 to 20 and 21 to 30 no significant difference in decorrelation slope
    between novel and familiar environments was detected.
  source: Results, Within-session representational drift, paragraph 1; Figure 1E
  quote: we failed to detect a significant difference between novel and familiar environments over a
    range of 11-20 or 21-30 trial lags
  statistics:
  - about: lags 11 to 20
    test: Wilcoxon rank-sum test
    p: 0.3
    statistic: Cohen's d = 0.54
    n: 26 session and turn units
  - about: lags 21 to 30
    test: Wilcoxon rank-sum test
    p: 0.68
    statistic: Cohen's d = -0.35
    n: 8 session and turn units
  depends_on:
  - fig1d-pv-decorrelation
  criterion: A claim of absence. Slopes as in fig1e-novel-drift-faster over lags 11 to 20 and 21
[... 87 more lines not kept]
```

**Agent**

**Verifier report, round 2: Zheng et al. 2024 on DANDI:000552 (0.261113.1035)**

The claims file has 32 claims and the attempt record has 32 outcomes. 29 claims are tested in full, figs1 is tested on one session, and 2 are blocked. Cell numbers are 0-based notebook cell indices.

### 1. Outcomes

I agree with every outcome except as noted below.

- **No change from round 1, and I agree:** fig1d, fig1e-novel, fig1e-later, fig1h, fig1i, switch-step-size-filter, fig2d, fig2e, fig3df (both), figs4g, fig3k, figs5, fig4-delay-zone, fig4-behavior, figs9, figs13 (3 of 5), fig5c, fig5d, multifield, figs12, fig6, fig6f, figs14, figs2, fig7, figs15.
  - **fig6:** familiar ON is 10 of 45 sessions under every seed (10 to 11), which is one session beyond the "within one session" allowance. The within-turn null is now conservative (false-positive rate 0.035, cell 91).
- **fig4-glm-deviance, partially reproduced:** I agree; it remains a judgment, since the criterion's partial clause does not cover this case. One nuance: the measured values given are reading (a), and the held-out OFF value of 0.128 is within tolerance only under the claim's seed. Under the other four seeds it is 0.114 to 0.121 (cell 55). Reading (b), in-sample 0.202 and 0.145, holds without depending on the seed and would be the better measured value. The outcome is a criterion gap, so `assumed: true` would fit.
- **fig4di, partially reproduced, assumed (trials from the fourth on):** the assumption is stated and reasonable; the trial counts 1031/288 match the legend's 1029/281. The record now says plainly that the decrease disappears once the last two trials are also left out (no correlation significant, cell 64). I agree.
- **figs8, now reproduced, assumed (per frame of forward locomotion):** the assumption is stated and the outcome is acceptable, but it is weak.
  - The paper's two values point to different units: familiar p = 3e-11 implies about 4×10⁵ samples, novel p = 0.78 about 200.
  - Per trial, both r are well outside tolerance (0.154 and −0.148). Per trial over all frames they are −0.082 and −0.261 (cell 67).
  - Within cell 67, the code comment still calls per-trial "the main, as the claim's legend plots one point per trial". That contradicts the adopted reading, and the Figure S8C legend says no such thing.
- **fig4no, partially reproduced, assumed (per position bin):** the assumption is stated and reasonable, and matches my round-1 outcome. The margin is very thin: 9.73 against 10.0 head-scan trials per bin in the central arm and the delay zone (cell 70).
- **figs1, now not reproduced on one session, assumed (peak-to-trough amplitude):** I agree only as a one-session result, and the assumption is misplaced.
  - The adopted switch time (the animal at the field's peak) is not one of the criterion's two readings.
  - Under the criterion's reading (a), the trial start, neither test is significant (p = 0.32 and 0.88), which would be reproduced.
  - Under reading (b), entry into the field, OFF gives p = 0.00023, and with trough depth p = 0.031 (cell 104).
  - So the outcome depends on the switch-time reading more than on the amplitude definition, and the record should flag that as the assumption.
  - Also unflagged: the 1,382 pairs reuse the same ~140 neighbours across switches from 32 units, so the pairs are not independent and the p values are inflated. Every change is at most about 1% of the amplitude, and only 1 of the 45 sessions was tested.
- **figs14:** the OFF fraction (0.436 against 0.2) depends on reducing the shuffle threshold to a mean over the field's bins. This is stated as a deviation but not flagged `assumed`. It does not change the partial outcome.

### 2. Sentences the outputs do not support

- **Cell 42:** "below the expected 0.54 to 0.77 for orders 1 and 3". Order 2 (0.510) is also below 0.54.
- **Summary, cell 107:** "under it the Familiar against Novel test … gives p = 0.058, and no other outcome would differ". The trial-averaged variant reran only the cell-50 and cell-52 summaries plus multifield (cell 52). The GLM, fig6, figs12, figs14, figs13, figs5 and fig4di were not rerun, so this cannot be claimed for them.
- **Cell 105 and the figs1 notes:** "The changes are about 1% of the amplitude in every reading" / "Every change is about 1%". At the code's switch time the OFF change is 0.03% (relative 0.0003). The supported wording is "at most about 1%".
- **Cell 71 and the fig4no notes:** "bin 50 … at the end of the choice arms". Cell 70 prints the bin's segment as return_side; it is the first bin past the 111 cm cut. This is consistent with the paper's "between green and red sections", but it is not inside the choice arm.
- **Cell 21:** "In 52 session and environment units (fields per unit 79 to 711)". Cell 20 prints 53 units; 52 have slopes. Trivial.
- **Cell 8:** "The x and y of the novel figure-8 maze carry no scale (the file says so)". No output shows this.

Everything else in the Results, the Summary, the README (including the timings: 1,353 s of pipeline runs and 473 s of streaming) and the record's notes matches the printed outputs.

The record states my round-1 reasons faithfully, near-verbatim, with my problem numbers attached.

### 3. Round-1 points

**Resolved:**
- **Problem 1 (figs8):** all readings are now run; the remaining doubt is covered in section 1.
- **Problem 2 (fig6):** the null is now within-turn, and the lag-1 variant and false-positive rates are shown.
- **Problem 3 (figs12):** three selections, including the code's, are shown; no change of outcome.
- **Problem 4 (GLM):** the gap in the partial clause is stated.
- **Problem 6 (fig4di):** the trailing zeros are shown and stated.
- **Problem 7 (fig1h):** now uses per-lag averages.
- **Problem 8 (cell 5 mislabel):** fixed.
- **Problem 9 (data version):** unchanged and still reasonable.
- **Requested outputs 1–7:** all added.

**Remaining, and bearing on a conclusion:**
1. **Upstream counts are still low under every variant**: 2,794–2,825 putative fields against 3,184 ± 318; familiar switching 1,884–1,933 against 2,310 ± 231. The cause is not found. This drives switch-step-size-filter, fig2d and multifield.
2. **fig2d hinges on two things**: the familiar OFF fraction is 0.0014 short, and the tie rule (647 fields tied). With ties broken toward the larger K, all four fractions are within tolerance, which would make it partially reproduced. The smaller-K rule is cited to the code, which is not under `paper/`, so I cannot verify it. The same applies to the new figs12 code_mismatch finding (windows swapped).
3. **figs1**: the switch-time reading, non-independent pairs and one session, as in section 1.
4. **figs8**: the per-frame reading is fragile, and the cell-67 comment contradicts it.
5. **fig4-glm-deviance**: held-out OFF is within tolerance under one seed only.

### 4. Critical findings

No finding in the record is rated `critical`.

One part of finding 1 (rated `major`) would be critical if taken alone. In the cited version, `is_familiar_maze` is False for 28 of the 30 familiar trials of e16_3m1_210201 (cell 7). That is a wrong label that nothing in the file reveals. The pinned version corrects it, so the `major` rating is right for the finding as a whole, which also covers the missing cell-type and light-responsive labels. Only one session was checked, so how far the mis-flag extends in the cited version is unknown.

## End of run

15 turns, 3 minutes, $1.84 at API prices, result: success.
