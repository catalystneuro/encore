# strickland-2022 · verifier-2 · run 43355485089

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 384
drwxr-xr-x 6 runner runner    4096 Nov 13 03:04 .
drwxr-xr-x 8 runner runner    4096 Nov 13 03:04 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 02:55 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 02:55 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 13 03:04 .claude
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .env
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .env.development
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .env.local
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .env.production
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .env.test
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .env.test.local
drwx------ 2 runner runner    4096 Nov 13 03:04 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 02:55 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 02:55 .github
-rw-r--r-- 1 runner runner       0 Nov 13 03:04 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 02:55 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 13 02:55 .mcp.json
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat strickland-2022-01.yaml
```

```
<persisted-output>
Output too large (43.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/d878c1cb-f5b1-4122-b0fb-8f3be6bd5ce8/tool-results/bgj37va5c.txt

Preview (first 2KB):
# Strickland and McDannald (2022) from CRCNS bst-3

Tests the findings of [Strickland and McDannald (2022)](https://doi.org/10.1038/s41467-022-34021-1)
on CRCNS data set [bst-3](https://doi.org/10.6080/K0Q23XGR), which holds 1812 brainstem single
units recorded with Neuropixels in ten rats during probabilistic fear discrimination, the cube file
of binned and normalized firing that the paper's scripts build from them, and those scripts.

| Claim | Outcome |
|---|---|
| The units match the paper's Source Data cluster rows (link) | Reproduced |
| Suppression ordered danger > uncertainty > safety, F(2,142) = 149.2 | Reproduced |
| Every rat discriminates | Reproduced |
| 1812 units, 73 sessions, 965 from females, per-subject totals | Reproduced |
| 21 regions and their unit counts | Reproduced |
| 21 cue clusters of 24 to 219 units | Reproduced |
| Cue PC1 (29.7%) is ordered danger > uncertainty > safety | Reproduced |
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/d878c1cb-f5b1-4122-b0fb-8f3be6bd5ce8/tool-results/bgj37va5c.txt"
}
```

```
1	# Strickland and McDannald (2022) from CRCNS bst-3
2	
3	Tests the findings of [Strickland and McDannald (2022)](https://doi.org/10.1038/s41467-022-34021-1)
4	on CRCNS data set [bst-3](https://doi.org/10.6080/K0Q23XGR), which holds 1812 brainstem single
5	units recorded with Neuropixels in ten rats during probabilistic fear discrimination, the cube file
6	of binned and normalized firing that the paper's scripts build from them, and those scripts.
7	
8	| Claim | Outcome |
9	|---|---|
10	| The units match the paper's Source Data cluster rows (link) | Reproduced |
11	| Suppression ordered danger > uncertainty > safety, F(2,142) = 149.2 | Reproduced |
12	| Every rat discriminates | Reproduced |
13	| 1812 units, 73 sessions, 965 from females, per-subject totals | Reproduced |
14	| 21 regions and their unit counts | Reproduced |
15	| 21 cue clusters of 24 to 219 units | Reproduced |
16	| Cue PC1 (29.7%) is ordered danger > uncertainty > safety | Reproduced |
17	| PC1 comes from k1 to k9 (505 units), k1 and k2 most | Reproduced |
18	| Danger latency correlates with PC1 contribution (R2 = 0.41) | Not reproduced |
19	| k1 to k9 form a correlated subnetwork, k3 the exception | Reproduced |
20	| k1 and k2 are hubs of the cue subnetwork | Partially reproduced (assumption) |
[... 756 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_strickland_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n=========== CELL {i} [{c['cell_type']}] ===========")
    src=''.join(c['source'])
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('--- OUT ---\n'+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--- OUT(data) ---\n'+''.join(d['text/plain'])[:3000])
            elif o.get('output_type')=='error': print('ERROR', o.get('ename'), o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; python3 -c "import json;nb=json.load(open('reproduce_strickland_2022.ipynb'));print(len(nb['cells']))"
```

```
2560 /tmp/claude-1001/nb.txt
100
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
2	=========== CELL 0 [markdown] ===========
3	# Reproducing Strickland and McDannald (2022) from CRCNS bst-3
4	
5	**Paper.** Strickland JA, McDannald MA (2022). Brainstem networks construct threat probability and
6	prediction error from neuronal building blocks. *Nature Communications* 13:6192.
7	[doi:10.1038/s41467-022-34021-1](https://doi.org/10.1038/s41467-022-34021-1). The claims file
8	(`claims/strickland-2022.yaml`) was written from the version of record (PMC9582012) with its
9	Supplementary Information and Source Data workbook.
10	
11	**Data set.** CRCNS [bst-3](https://crcns.org/data-sets/brainstem/bst-3),
12	[doi:10.6080/K0Q23XGR](https://doi.org/10.6080/K0Q23XGR), "Neuropixels recordings from 21 brainstem
13	regions in rats during fear discrimination", read from the public bucket
14	(`crcnsarchive/bst-3/live/data.zip`, 367,964,637 bytes, last modified 2026-02-11). CRCNS data sets
15	are not versioned, so the version is recorded as `unversioned`; the MD5 sums of the bucket's
16	`checksums.md5` are printed below (data.zip `4ee6c433f5255693d5e85bcca6819cd4`), so that a later
17	change can be detected. The paper cites the data set by its DOI and no version; there is only the
18	one published copy (`live/`, descriptor version 0.6 of 2022-11-29), so it is the one pinned.
19	
20	**What the data set holds.** One MATLAB file per single unit (1812, spike times and the session's
[... 680 more lines not kept]
```

**Agent**

Reading the notebook outputs now; the attempt record has 30 outcomes, which matches the claims file count to be checked next.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 700
}
```

```
700	sess_sex = np.array([k[2:4] in bst3.FEMALE for k in keys]).astype(int)
701	sd1c = np.array([r[1:4] for r in sheets["Figure 1c"][1:] if r[0] is not None], float)
702	print("Source Data Fig. 1c:", sd1c.shape[0], "sessions; means", sd1c.mean(0).round(3))
703	rows = []
704	vals = {}
705	for empty in ("code", "zero", "drop"):
706	    Y = []
707	    n_empty = 0
708	    for k in keys:
709	        r = bst3.suppression_ratios(S[k]["cue"], S[k]["poke"], empty)
710	        n_empty += int(np.isnan(bst3.suppression_ratios(S[k]["cue"], S[k]["poke"], "drop")).sum())
711	        Y.append([np.nanmean(r[0:4]), np.nanmean(r[4:12]), np.nanmean(r[12:16])])
712	    Y = np.array(Y)
713	    vals[empty] = Y
714	    a = bst3.mixed_anova_cue_by_group(Y, sess_sex)
715	    rows.append({"empty trials": {"code": "set to 1 (script)", "zero": "set to 0 (sr-a)", "drop": "left out (sr-b)"}[empty],
716	                 "danger": Y[:, 0].mean(), "uncertainty": Y[:, 1].mean(), "safety": Y[:, 2].mean(),
717	                 "F cue x sex (a-a)": a["F_mixed"], "df a-a": a["df_mixed"], "p a-a": a["p_mixed"],
718	                 "F repeated (a-b)": a["F_rm"], "df a-b": a["df_rm"], "p a-b": a["p_rm"]})
719	print("Trials with no pokes in either period:", n_empty, "of", 16 * len(keys))
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1399,
 "limit": 600
}
```

```
1399	
1400	=========== CELL 46 [markdown] ===========
1401	**Result: partially reproduced.** With the Methods' measure (danger firing, 14 intervals) as r
1402	squared, the Source Data column's "R2", k2 (0.503) and k1 (0.462) have the two highest means, both
1403	within tolerance (0.466 +- 0.047 and 0.424 +- 0.042), but not every t-test passes: k1 does not exceed
1404	k3 (p = 0.42) or k4 (p = 0.12), and k2 does not exceed k3 (p = 0.014) at 0.05/7 or 0.05/8. With r,
1405	k1 and k3 are the two highest. The Source Data per-unit values equal, in all nine clusters, r squared
1406	computed on the full 42-value cue rows (all three cues), not on danger firing; with that measure
1407	k1 (0.424) and k2 (0.466) are the two highest and each exceeds all seven of k3 to k9 at both
1408	thresholds.
1409	
1410	=========== CELL 47 [markdown] ===========
1411	## fig2g-cue-anatomy
1412	
1413	> Neurons of every cue cluster were found in at least six brainstem regions, and subnetwork neurons,
1414	> including the k1 and k2 hubs, were concentrated in the deep layer of the superior colliculus and
1415	> the subdivisions of the periaqueductal gray.
1416	
1417	=========== CELL 48 [code] ===========
1418	nreg = [len(set(region[L1_cue == k])) for k in range(1, 22)]
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1999,
 "limit": 600
}
```

```
1999	
2000	
2001	=========== CELL 73 [markdown] ===========
2002	**Result: fig4b-phasic-network and fig4b-tonic-network partially reproduced.** Under L1 every
2003	profile condition holds: k1 to k3 have higher temporal indices than every one of k6 to k9 under both
2004	t-a and t-b; in the first second k1 fires more to uncertainty shock than to danger (2.58, 1.59), k2
2005	more to danger (2.85, 1.44), and k3 is suppressed on both (-0.97, -0.90); k6 is the only cluster
2006	inhibited to surprising shock (-0.88, below its other means), and k7 and k8 increase most to it
2007	(0.82, 0.31) with seconds 5 to 10 above half the first second. The network parts fail with the
2008	Pearson correlation the criterion names: the mean r within k1 to k3 is -0.329 against 0.008 with the
2009	other clusters, and within k6 to k9 -0.250 against 0.000, because k3 and k6 change firing in the
2010	opposite direction to their fellow clusters. With r squared, the coefficient the Methods name
2011	("Pearson's correlation coefficient (R2)") and the script plots, both network parts hold (0.539
2012	against 0.076; 0.505 against 0.110), and both claims would be reproduced; whether the criterion
2013	should allow r squared, as the one for fig2e does, is asked of a reader. Under L2 the tonic network
2014	part holds in none of the 20 seeds with r and in all 20 with r squared, and the phasic network part
2015	in 10 and 15.
2016	
2017	=========== CELL 74 [markdown] ===========
2018	## fig4e-network-pca
[... 543 more lines not kept]
```

**Agent**

Notebook read. Now checking the claims file criteria for the claims whose outcomes changed or rest on assumptions.

**Agent calls Bash**

```bash
cd  grep -n "^  - id:\|^- id:" strickland-2022.yaml | head -50; grep -c "^- id:\|^  - id:" strickland-2022.yaml
```

```
141:- id: source-data-cluster-link
155:- id: fig1c-suppression-order
188:- id: figs2-each-rat-discriminates
202:- id: units-sessions-subjects
254:- id: fig1e-regions
284:- id: fig2b-cue-clusters
307:- id: fig2c-cue-pc1-ordered
328:- id: fig2c-pc1-contribution
356:- id: fig2d-danger-latency
387:- id: fig2e-cue-subnetwork
406:- id: fig2f-cue-hubs
439:- id: fig2g-cue-anatomy
454:- id: fig3a-cluster-signals
475:- id: fig3b-signal-pca
504:- id: fig3c-subnetwork-lesion
520:- id: fig3d-supranetwork-lesion
535:- id: fig3e-network-anatomy
559:- id: fig4b-outcome-clusters
580:- id: fig4c-positive-prediction-error
607:- id: fig4b-phasic-network
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,140p strickland-2022.yaml | grep -n -i -A6 "k-means\|median\|seed\|L2\|L1\|assum\|partial\|level" | head -120
```

```
10:# (head cap, surgery, acquisition, sorting, z-score normalization, heat plots, k-means, PCA,
11-# latency, correlations, hubs, regression, lesion PCA, anatomy, chi-square), Supplementary
12-# Figures 1 to 7 (legends; the panels are garbled in the extraction) and Supplementary Tables 1
13-# and 2 (read from the extracted cells; Table 2's column layout is garbled, its row and subject
14-# totals are not). The Source Data workbook (41467_2022_34021_MOESM4_ESM.xlsx) was read with a
15-# small XML parser; numbers marked "Source Data" below come from it. The supplement PDF could not
16-# be rendered (no poppler), so no panel was read as an image. The CRCNS data descriptor
--
59:#  - Cue matrix (Supplementary Methods, K-means clustering and PCA). 1812 x 42, per cue 14 1-s
60-#    intervals from 2 s before cue onset to 2 s after cue offset, columns 1-14 danger, 15-28
61-#    uncertainty (all 8 trials), 29-42 safety.
62-#  - Outcome matrix. 1812 x 80, per trial type 20 500-ms intervals over the 10 s from shock offset,
63-#    columns 1-20 danger, 21-40 uncertainty shock, 41-60 uncertainty omission, 61-80 safety.
64:#  - K-means (Supplementary Methods, K-means clustering). MATLAB kmeans, number of clusters 21
65-#    (cue) and 11 (outcome), chosen by the paper by inspecting solutions for 1 to 25 and 1 to 20
66:#    clusters. No option, replicate count or seed is given. Standard choice, MATLAB's defaults
67:#    (squared Euclidean distance, k-means++ seeding, one replicate); since one replicate depends
68:#    on the seed, a solution's result is reported as the median over 20 seeds, and the best of
69-#    20 replicates (lowest summed distance) is shown as a variant.
70:#  - Cluster labels, two readings. (L1) The paper's own membership. Source Data sheets
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 328,440p strickland-2022.yaml; sed -n 504,535p strickland-2022.yaml; sed -n 607,650p strickland-2022.yaml; sed -n 818,860p strickland-2022.yaml
```

```
- id: fig2c-pc1-contribution
  statement: PC1 firing information originated from nine clusters (k1 to k9), a minority of
    neurons (505 of 1812, 27.9%), with k1 and k2 contributing most per unit.
  source: Results, paragraphs 3 and 4; Figure 2c; Source Data Fig. 2c
  quote: PC1 firing information originated from nine clusters (k1–k9; Fig. 2c and Supplementary
    Fig. S5 ) composed of a minority of neurons (505/1812, 27.9%)
  depends_on:
  - fig2c-cue-pc1-ordered
  expected:
  - quantity: neurons in the nine clusters contributing most to PC1
    value: 505
    tolerance: 50.5
  - quantity: PC1 contribution per unit of k1 (Source Data Fig. 2c)
    value: 0.121
    tolerance: 0.012
    unit: percent variance per neuron
  - quantity: PC1 contribution per unit of k2 (Source Data Fig. 2c)
    value: 0.113
    tolerance: 0.011
    unit: percent variance per neuron
[... 212 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,140p strickland-2022.yaml | grep -n -i -B2 -A8 "reading\b\|readings\|absence\|open," | head -80; sed -n 860,900p strickland-2022.yaml
```

```
46-#  - Suppression ratio (Methods, Calculating suppression ratios). Per trial, baseline rate = pokes
47-#    in the 20 s before cue onset x 3, cue rate = pokes in the 10-s cue x 6, ratio = (baseline -
48:#    cue) / (baseline + cue). Open, (sr-a) a trial with no pokes in either period set to 0, or
49-#    (sr-b) left out of means. A session's value for a cue is the mean over its trials of that
50-#    cue (uncertainty pooling its 8 trials).
51-#  - Normalized firing (Supplementary Methods, Z-score normalization). Per unit and trial, firing
52-#    rate in 250-ms bins; the trial's baseline (mean rate over the 2 s before cue onset) is
53-#    subtracted; the differential firing is z-scored across all trials and bins of the unit.
54:#    Open, (n-a) baseline per trial, or (n-b) the mean baseline of that trial type ("baseline
55:#    firing rate (2 s prior to cue onset) specific to that trial type"). Open, the epoch is given
56-#    both as "from 20 s prior to cue onset to 20 s following cue offset" (w-a, 200 bins) and as
57-#    "a total of 240 bins" (w-b, 60 s from 20 s before cue onset). Mean over trials per trial type,
58-#    then 250-ms bins averaged into 1-s intervals (cue) or 500-ms intervals (outcome).
59-#  - Cue matrix (Supplementary Methods, K-means clustering and PCA). 1812 x 42, per cue 14 1-s
60-#    intervals from 2 s before cue onset to 2 s after cue offset, columns 1-14 danger, 15-28
61-#    uncertainty (all 8 trials), 29-42 safety.
62-#  - Outcome matrix. 1812 x 80, per trial type 20 500-ms intervals over the 10 s from shock offset,
63-#    columns 1-20 danger, 21-40 uncertainty shock, 41-60 uncertainty omission, 61-80 safety.
--
68-#    on the seed, a solution's result is reported as the median over 20 seeds, and the best of
[... 68 more lines not kept]
```

**Agent**

# Round 2 verifier report: Strickland and McDannald (2022), attempt strickland-2022-01

## 1. Outcomes

The claims file has 30 claims, and the attempt record has 30 outcomes: 23 reproduced, 6 partially reproduced, 1 not reproduced, 0 blocked. **I agree with all 30.** In round 1 I disagreed on four of them. All four are now settled:

- **fig2c-pc1-contribution (reproduced):** I now agree. The claims file's standard for a k-means result is the median over 20 seeds. On that measure the nine largest clusters hold 481 units, within 505 ± 50.5. Single seeds range from 360 to 590, and 13 of 20 are within tolerance (cell 35). The L1 part matches Source Data to 0.0003 (cell 34).
- **fig4b-phasic-network and fig4b-tonic-network (partially reproduced):** These are now judged with Pearson r, as the criterion says. Every profile part holds and the network part fails: within −0.329 against 0.008 for phasic, −0.250 against 0.000 for tonic (cell 72). Under the criterion that is partial.
- **fig5e-no-anatomical-bias (reproduced, assumed):** I accept this. My round-1 "partial" was my own call, not one of the criterion's levels. The claims file's own check log keeps reading p-b "for Fig. 5e only". Under p-b the largest differential is 4.48, which equals Source Data. The record now states the assumption and that p-b passes by construction. It also reports p-a: 9.82, with a permutation p of 0.001 (cell 93).

**Assumptions flagged `assumed: true`:**
- **fig2f (r squared):** stated and reasonable. The Methods write "(R2)" and the Source Data column is headed R2. With r, k1 and k3 are the two highest means, so the claim would not even be partial (cell 45).
- **fig5e (p-b):** stated and reasonable, for the reason above.

**One assumption that is not flagged:** cue-outcome-membership-independent is judged on L1. Under L2 the median goodness-of-fit p values are 0.048 (phasic) and 0.011 (tonic), and only 4 of 20 seeds pass (cell 96). Its criterion only says "reported under L1 and L2", so choosing L1 to decide is a judgment that would flip the outcome. That judgment is reasonable and the notes state it, but it should carry `assumed: true`.

## 2. Sentences the printed outputs do not support

- **Cell 61, and the attempt record's fig3d-supranetwork-lesion notes:** both say PC2's "probability peak [is] in the first cue second". Cell 58 prints `PC2 |prob| peak s` = 2, the index into cue seconds 1 to 10 plus one, so the peak is in the second cue second. The criterion only needs the first half, so the outcome stands.
- **Cell 73:** "k6 is the only cluster inhibited to surprising shock". Cell 72 shows a negative uncertainty-shock mean for k3 (−0.14), k4 (−0.31), k5 (−0.18) and k9 (−0.24) as well.
- **Cell 73:** the tonic network fails "because k3 and k6 change firing in the opposite direction to their fellow clusters". This is incomplete for the tonic network. The r matrix in cell 72 shows k9 anticorrelated with k7 (−0.60) and k8 (−0.79) and positively correlated with k6 (0.67), so k6 and k9 together oppose k7 and k8. The record's own wording, "k6 is anticorrelated with k7 and k8", is accurate.
- **Cell 88:** "L2 gives 47.80 and 30.92%, out of tolerance". Only PC1 is out of tolerance. 30.92 lies inside 33.4 ± 3.34 (30.06 to 36.74).

Every other "Result" sentence (cells 14 to 97), the Summary (cell 99), the README table and text, and the record's notes and findings agree with the printed outputs. I checked counts, p values, the seed medians, the 4-of-20 count, the 9-of-10 animals and the latency counts.

**Round-1 reasons in the record:** the verification entries give my round-1 reasons in my words. Each claim's problem points have been folded into its reason. The only omission is minor: the Source Data latency R² values (0.508 and 0.394) are left out of the fig2d reason, though they appear in the notes.

## 3. Round-1 points

**Resolved:**
- **Point 1 (fig4b r against r²):** on the attempt's side, the outcomes now follow the criterion.
- **Point 4 (L2 resting on one seed):** fig2c-pc1-contribution and cue-outcome now use all 20 seeds. Elsewhere L2 is only a variant.
- **Point 5 (latency markdown):** corrected. Cell 11 also shows that no script computes the latency.
- **Point 6:** v-b now runs on s-c, giving 0.263 against 0.266 (cell 59).
- **Point 7 (Fig. 4f k7/k8 labels):** explained as swapped labels. The rows labelled k7 hold 111 k7 values and 60 k8 values (cell 78).
- **Point 8:** `z.ms500` is now recomputed from the spike times, largest difference 9.5e-13 (cell 5).
- **Round-1 section C:** script passages are now printed (cell 11). They cover subject mapping, region remap, regression terms, PE/shock column order, lesion shuffles, the outcome hub r², and empty trials set to 1. L2 now runs per seed. s-c stability is shown: standard deviation 0.0001, and the subnetwork lesion's weight is above the supranetwork's in 0 of 10 runs (cell 60).

**Still open, bearing on a conclusion:**
- **fig4b-phasic/tonic:** the claims file allows r and r² for fig2e but only r here. With r² both claims would be reproduced. This is a claims-file inconsistency, now referred to a reader.
- **fig5e:** the threshold comes from the same quantity it tests, so p-b cannot fail. The reproduced outcome adds nothing beyond the Source Data link, and the Results' reading (p-a) fails. This is a claims-file design flaw.
- **fig2f:** Source Data matches the 42-column r², not the Methods' danger-only measure. This is a paper inconsistency; the outcome is partial under the criterion.
- **fig3c/3d:** the criteria compare unit-norm weights. With loadings, fig3c would pass (0.709 against 0.680). This is a claims-file weakness, referred to a reader.
- **fig2d:** how the paper computed its latencies is still unknown; the record lists it as a finding.
- **cue-outcome-membership-independent:** the L1 judgment should be flagged `assumed: true` (section 1).
- **Shuffle function:** it is not in the data set. The lesion matrices still match the Source Data percentages to within 0.04 points.

## End of run

13 turns, 3 minutes, $1.57 at API prices, result: success.
