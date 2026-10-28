# openneuro-ds000228 · verifier-2 · run 40738455451

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 604
drwxr-xr-x 6 runner runner    4096 Oct 28 17:51 .
drwxr-xr-x 7 runner runner    4096 Oct 28 17:51 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 17:42 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 17:42 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 28 17:51 .claude
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .env
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .env.development
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .env.local
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .env.production
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .env.test
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .env.test.local
drwx------ 2 runner runner    4096 Oct 28 17:51 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 17:42 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 17:42 .github
-rw-r--r-- 1 runner runner       0 Oct 28 17:51 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 17:42 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 17:42 .mcp.json
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 10.1038-s41467-018-03399-2.yaml | head -80; wc -l *.yaml
```

```
# Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018) from OpenNeuro ds000228

Tests the findings of [Richardson et al. (2018)](https://doi.org/10.1038/s41467-018-03399-2) on
[OpenNeuro ds000228](https://openneuro.org/datasets/ds000228/versions/1.1.1), snapshot 1.1.1,
which holds movie-viewing fMRI of 122 children aged 3 to 12 and 33 adults, with the paper's own
preprocessed images, artifact and CompCor regressors, group ROIs and behavioural scores.

| Claims | Outcome |
|---|---|
| Sample, behaviour and motion (11 claims) | Reproduced |
| Inter-region correlations (15 claims) | 6 partially reproduced, 9 not reproduced |
| Reverse correlation (8 claims) | 1 reproduced, 3 partially reproduced, 4 not reproduced |
| Functional maturity (4 claims) | 3 reproduced, 1 not reproduced |
| Face regions (2 claims) | 1 reproduced, 1 not reproduced |
| Replication sample and hand-coded events (2 claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every behavioural number of the paper is recovered from participants.tsv. With the deposited
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat openneuro-ds000228-richardson-2018-01.yaml
```

```
<persisted-output>
Output too large (43KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/63e94cd8-825c-4de9-aafa-5205e5d4791e/tool-results/bnwses0hx.txt

Preview (first 2KB):
schema_version: 2
id: openneuro-ds000228-richardson-2018-01
dataset:
  archive: openneuro
  id: ds000228
  version: 1.1.1
  doi: 10.18112/openneuro.ds000228.v1.1.1
paper: doi:10.1038/s41467-018-03399-2
date: 2026-10-28
entry: openneuro-ds000228-richardson-2018
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "openneuro-ds000228-richardson-2018-01.yaml"
}
```

```
1	schema_version: 2
2	id: openneuro-ds000228-richardson-2018-01
3	dataset:
4	  archive: openneuro
5	  id: ds000228
6	  version: 1.1.1
7	  doi: 10.18112/openneuro.ds000228.v1.1.1
8	paper: doi:10.1038/s41467-018-03399-2
9	date: 2026-10-28
10	entry: openneuro-ds000228-richardson-2018
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
[... 773 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_richardson_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT:\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--- OUT:\n'+''.join(d['text/plain']))
            elif 'image/png' in d: print('--- [image]')
        elif o.get('output_type')=='error': print('--- ERROR', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -n "######## CELL" $TMPDIR/nb.txt | wc -l
```

```
2697 /tmp/claude-1001/nb.txt
123
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 900
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Richardson et al. (2018) on OpenNeuro ds000228, snapshot 1.1.1
4	
5	Paper: Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social brain
6	from age three to twelve years", Nature Communications 9, 1027,
7	[doi:10.1038/s41467-018-03399-2](https://doi.org/10.1038/s41467-018-03399-2).
8	
9	Dataset: [OpenNeuro ds000228](https://openneuro.org/datasets/ds000228/versions/1.1.1), snapshot
10	`1.1.1`, DOI 10.18112/openneuro.ds000228.v1.1.1. The paper cites the dataset on OpenfMRI
11	without a version; the claims file names snapshot 1.1.1, which is also the latest published
12	snapshot. Its CHANGES file says 1.1.1 only updated the citation to the paper (2023), so the
13	pinned snapshot holds the same data as 1.1.0. It is pinned because the claims file gives it and
14	the protocol pins the latest published version when the paper cites none.
15	
16	Claims: `claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml`, written from the version of
17	record and its Supplementary Information (Supplementary Tables 1 to 4 read from the PDF). Its
18	header labels the shared pipeline P1 to P9 and the open details O1 to O9; this notebook uses the
19	same labels.
20	
[... 880 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 900,
 "limit": 900
}
```

```
File content (30802 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 900,
 "limit": 600
}
```

```
900	######## CELL 26 [markdown]
901	### beh-fb-tom, beh-fb-age, beh-fb-dccs
902	
903	> False-belief failers and inconsistent performers score lower than passers on the remaining ToM
904	> items (means .55, .57 and .75). False-belief failers are younger than inconsistent performers
905	> and passers (mean ages 4.1, 4.8 and 5.2 years). False-belief failers have lower DCCS scores than
906	> the other two groups (means 1.73, 2.26, 2.33).
907	
908	Tukey HSD over the three groups (statsmodels `pairwise_tukeyhsd`), diffs under both scales of O9;
909	Kruskal-Wallis from scipy.
910	
911	######## CELL 27 [code]
912	def fb_tests(var):
913	    sub = young.dropna(subset=[var])
914	    out = sub.groupby("FB_Group")[var].agg(["mean", "sem", "count"]).loc[["fail", "inc", "pass"]]
915	    print(out.round(3).to_string())
916	    kw = stats.kruskal(*[sub.loc[sub.FB_Group == g, var] for g in ["pass", "inc", "fail"]])
917	    print(f"Kruskal-Wallis H = {kw.statistic:.2f}, p = {kw.pvalue:.2g}")
918	    for scale in ["z-scored (O9a)", "raw (O9b)"]:
919	        v = (sub[var] - sub[var].mean()) / sub[var].std() if scale.startswith("z") else sub[var]
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1500,
 "limit": 450
}
```

```
1500	            same_dir = (abs(rx) > abs(ry))
1501	            rows.append({"reading": reading_name(r), "williams": reading_w, "pair": f"{x} vs {y}", "r age x": rx, "r age y": ry,
1502	                         "r xy": rxy, "t": w["t"], "p_t": w["p_t"], "z": w["z"], "p_z": w["p_z"], "paper significant": should,
1503	                         "as paper": (sig and same_dir) if should else (not sig)})
1504	wil = pd.DataFrame(rows)
1505	print(wil[(wil.reading == reading_name(MAIN))].drop(columns="reading").to_string(float_format=lambda x: f"{x:.3g}"))
1506	print(wil.groupby(["reading", "williams"])["as paper"].sum().rename("comparisons as in the paper, of 10").to_string())
1507	--- OUT:
1508	               williams                  pair  r age x  r age y    r xy     t      p_t     z      p_z  paper significant  as paper
1509	0   a (partial, motion)         wToM vs wFace    0.367    0.106   0.265  2.51   0.0134  2.47   0.0137               True      True
1510	1   a (partial, motion)        wPain vs wFace    0.525    0.106   0.167  4.08 8.11e-05  3.92 8.97e-05               True      True
1511	2   a (partial, motion)        wToM vs wScene    0.367    0.288   0.222 0.752    0.454  0.75    0.453              False      True
1512	3   a (partial, motion)       wPain vs wScene    0.525    0.288   0.342  2.62  0.00982  2.58  0.00996              False     False
1513	4   a (partial, motion)           wToM vs wM1    0.367    0.227   0.222  1.32    0.191  1.31     0.19              False      True
1514	5   a (partial, motion)          wPain vs wM1    0.525    0.227   0.167  2.92  0.00425  2.86  0.00428              False     False
1515	6   a (partial, motion)           wToM vs wV1    0.367  -0.0686  -0.134  3.36  0.00104  3.27  0.00107               True      True
1516	7   a (partial, motion)          wPain vs wV1    0.525  -0.0686  -0.092  5.03 1.73e-06  4.76 1.97e-06               True      True
1517	8   a (partial, motion)  across vs aFaceScene   -0.247   0.0654   0.277 -2.95  
[... 432 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1950,
 "limit": 400
}
```

```
1950	        ax.axvspan(row.trs[0] - 0.5, row.trs[-1] + 0.5, fill=False, edgecolor="k", lw=0.8)
1951	    ax.set_ylabel(f"adult mean, {n} (z)"); ax.axhline(0, color="grey", lw=0.5)
1952	axes[1].set_xlabel("TR (shaded: found events; outlined: Supplementary Table 3)")
1953	plt.tight_layout(); plt.show()
1954	print("y ranges:", {n: (round(RC[(n, BEST_SPAN, BEST_O5)][0]["mean"].min(), 2), round(RC[(n, BEST_SPAN, BEST_O5)][0]["mean"].max(), 2)) for n in ["ToM", "Pain"]})
1955	--- [image]
1956	--- OUT:
1957	y ranges: {'ToM': (np.float64(-0.83), np.float64(0.79)), 'Pain': (np.float64(-0.88), np.float64(0.81))}
1958	
1959	
1960	######## CELL 84 [markdown]
1961	**Result: partially reproduced.** At p < .05 uncorrected (reading O5a, the best match to Supplementary Table 3; O6 makes no difference for these networks), all seven ToM events and 10 of 12 pain events of Supplementary Table 3 are found (P08 and P10 missed), but the counts are 9 ToM events (80 s) and 10 pain events (84 s), against 7 (68 s) and 12 (86 s). The ToM count matches under O5b and O5c (7 events, 56 s), where only 8 of 12 pain events are found. The pain time (84 s) is within tolerance; the ToM time is not under any reading.
1962	
1963	######## CELL 85 [markdown]
1964	### rc-overlap
1965	
1966	> ToM and pain events overlap at a single timepoint (the last of T05 and first of P05), less
1967	> overlap than chance in a permutation test.
1968	
1969	Permutations as Methods paragraph 10, 1000 per reading, seed fixed for this section.
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 2350,
 "limit": 400
}
```

```
2350	
2351	######## CELL 104 [markdown]
2352	## Functional maturity
2353	
2354	Each child's ToM (Pain) network timecourse before z-normalization, TRs 11 to 168, artifact
2355	timepoints left out, correlated (Pearson) with the adult mean timecourse (Methods paragraph 13).
2356	IRC measures are those of irc-age-within (M1 regressed), under each IRC reading.
2357	
2358	######## CELL 105 [code]
2359	def maturity(net):
2360	    adult_mean = np.nanmean(RAW[net].loc[adults.index].values, axis=0)[MOVIE]
2361	    out = {}
2362	    for s in children.index:
2363	        x = RAW[net].loc[s].values[MOVIE]; ok = np.isfinite(x)
2364	        out[s] = stats.pearsonr(x[ok], adult_mean[ok]).statistic
2365	    return pd.Series(out)
2366	MAT = pd.DataFrame({"mat_ToM": maturity("ToM"), "mat_Pain": maturity("Pain")})
2367	print(MAT.describe().round(3).to_string())
2368	--- OUT:
2369	       mat_ToM  mat_Pain
[... 329 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 80,200p 10.1038-s41467-018-03399-2.yaml; grep -n "^- id:\|^  - id:\|id: " 10.1038-s41467-018-03399-2.yaml | head -60
```

```
#    (b) full 9 mm spheres around the Supplementary Table 2 centers; (c) those spheres restricted
#    to voxels with data in each participant.
# O2 Artifact regressors. "motion artifact timepoints" as nuisance covariates is read as one
#    indicator regressor per artifact timepoint (a); (b) a single regressor marking all of them.
#    ART's composite-motion measure is used with its default definition, a standard choice.
# O3 TRs in the IRC analysis: (a) all 168; (b) TRs 11 to 168, as in the other timecourse analyses.
# O4 Scale of regression coefficients. The b values are on a scale the paper does not state; the
#    adult-child effect of b = -.97 on within-ToM correlation is about one s.d., so (a) outcome and
#    continuous predictors z-scored; (b) raw units. Criteria judge regressions on t, p and sign,
#    which do not depend on the scale, and report b under both readings.
# O5 Reverse-correlation threshold. The alpha of the per-timepoint one-tailed t-test is not given.
#    Readings: (a) p < .05 uncorrected; (b) p < .01 uncorrected; (c) p < .05 FDR-corrected over
#    the 158 timepoints. The reading whose events best match Supplementary Table 3 is reported.
# O6 Span of z-normalization (P6): (a) TRs 11 to 168; (b) all 168 TRs. Artifact timepoints (NaN)
#    are left out of the mean and s.d.
# O7 Child event magnitude (P8) taken from (a) the z-normalized network timecourse used in the
#    reverse correlation, (b) the same timecourse before z-normalization.
# O8 Partial Kendall tau: computed as the partial rank correlation of Kendall (the formula used
#    by R's ppcor), a standard choice; its p-value from the normal approximation.
# O9 Tukey HSD differences in the behavioral results (e.g. Pass-Fail diff = 1.2 for ToM, against
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=10.1038-s41467-018-03399-2.yaml; sed -n 260,302p $f; echo ----; sed -n 506,542p $f; echo ----; sed -n 732,876p $f
```

```
- id: beh-fb-tom
  statement: False-belief failers and inconsistent performers score lower than passers on the
    remaining ToM items (means .55, .57 and .75).
  source: Results, Behavioral results, paragraph 2
  quote: False-belief task failers and inconsistent performers did worse on the remaining ToM items than
    passers
  statistics:
  - about: Pass against Fail
    test: Tukey HSD test of ToM*FB-Group ANOVA
    statistic: diff = 1.2
    p: 0.00005
    p_relation: <
  - about: Pass against Inc
    test: Tukey HSD test of ToM*FB-Group ANOVA
    statistic: diff = 1.08
    p: 0.0001
    p_relation: <
  - about: Inc against Fail
    test: Tukey HSD test of ToM*FB-Group ANOVA
    statistic: diff = .16
[... 207 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=10.1038-s41467-018-03399-2.yaml; sed -n 877,1000p $f; echo ----; sed -n 1097,1305p $f
```

```
- id: rc-events
  statement: Reverse correlation on the adult network timecourses finds seven ToM events (68 s, mean
    length 9.7 s) and twelve pain events (86 s, mean length 7.2 s), at the times of Supplementary
    Table 3.
  source: Results, Reverse correlation analysis, paragraph 2; Figure 4a; Supplementary Figure 5;
    Supplementary Table 3
  quote: In adults, the reverse correlation analysis produced seven theory of mind events (68 s total,
    M(s.d.) length 9.7(4.2) s) and twelve pain events (86 s total, M(s.d.) length 7.2(4.7)s)
  expected:
  - quantity: ToM events
    value: 7
    tolerance: 0
  - quantity: pain events
    value: 12
    tolerance: 0
  - quantity: ToM event time
    value: 68
    tolerance: 6.8
    unit: s
  - quantity: pain event time
[... 314 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=10.1038-s41467-018-03399-2.yaml; sed -n 425,505p $f | grep -n -A8 "criterion"; sed -n 543,731p $f | grep -A10 "criterion:"; sed -n 1305,1427p $f | grep -B2 -A12 "criterion:"
```

```
37:  criterion: Pipeline P1 to P5, readings O1, O2 and O3. Rule S under any reading.
38-- id: irc-age-within
39-  statement: Among children, within-ToM and within-Pain correlations increase with age, controlling for
40-    motion.
41-  source: Results, Inter-region correlation analysis, paragraph 3; Figure 2
42-  quote: Among children, within-ToM and within-Pain network correlations increased significantly with
43-    age
44-  statistics:
45-  - about: within-ToM
--
63:  criterion: Pipeline P1 to P5 with M1 regressed out, readings O1 to O3. Rule S under any reading.
64-- id: irc-age-across
65-  statement: Among children, the across-network correlation decreases with age (becomes more
66-    anti-correlated), controlling for motion.
67-  source: Results, Inter-region correlation analysis, paragraph 3; Figure 2
68-  quote: Across-network correlations decreased significantly with age
69-  statistics:
70-  - test: Spearman partial correlation test, motion as covariate
71-    statistic: rs(119) = -.35
--
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "slice gap\|3.13" paper/10.1038-s41467-018-03399-2.txt | head; grep -n -i "remaining ToM\|homologous" paper/10.1038-s41467-018-03399-2.txt | head -5
```

Result: not kept, because it reads the paper's text.

**Agent**

**Round-2 verifier report: Richardson et al. 2018 on ds000228 v1.1.1**

Cell numbers below are the current ones; they have moved since round 1.

**1. Outcomes and assumptions**

The claims file has 42 claims, and the attempt record gives 42 outcomes. I agree with 41 of them.

**I disagree on one: rc-overlap (record says partially_reproduced).** This is a change from round 1, where I agreed and missed it.
- The criterion defines only a reproduced outcome: "one overlapping timepoint is found and p <= .01 under a reading". It does not invoke Rule S and has no partial clause.
- The overlap here is 0 against the paper's 1, with a tolerance of 0 (cell 86).
- For irc-williams, the record reasons that a criterion with no partial clause can only give reproduced or not reproduced. By that same reasoning, rc-overlap is not_reproduced.
- Partial could only be defended by applying Rule S's partial clause, which this criterion does not name. The record should state that reasoning, or change the outcome.

**I agree with the other 41, including the three changed since round 1** (irc-williams, rc-child-adult-timecourse, maturity-across). For maturity-across, within-ToM is also significant under O2b+O3b (p = .049, cell 106). The record does not say so, but it does not change the outcome.

**Assumed outcomes.** Five outcomes are marked `assumed: true`: irc-tom-behavior-age, irc-fb-across, rc-fb-no-difference, rc-3yo-events and maturity-within. Each is stated in the deviations, with the outcome it would have under the other reading, and each is reasonable:
- **O2a:** the deposited regressors are one indicator per artifact timepoint (cell 8).
- **O3a:** the Methods restrict to TRs 11 to 168 only in paragraphs 9 and 13, not for the inter-region correlations.
- **O7a:** the events and their peaks are defined on the z-normalized timecourse.
- **O6b:** Methods paragraph 9 order; this one is only a tie-break.

For rc-3yo-events, the criterion asks for "the reading that reproduced rc-events", and no reading did. Using the best-matching reading is a sensible extension, and the record should say it is one.

The rule for absence claims is now stated (cell 42). The claims file has no rule for absence claims under several readings, so this fills a gap. It is not a misreading.

**Misreadings in the claims file:** I found none. I checked the voxel-size counts against Methods (paper text line 1306: n = 3 seven-year-olds and 20 aged 8 to 12), and the record's metadata_error finding is correct.

**2. Sentences the printed outputs do not support**

- **Cell 55 and the record notes for irc-adult-vs-child.** Cell 55 says "all three t values are outside 10% of -5.7, -3.8 and 7.2 under every reading", and the record says "all three t values are out of tolerance under every reading (-6.23 to -7.05, …)". Cell 54 shows within-ToM t = -6.23 under O2a+O3b, which is inside the tolerance of -5.7 ± .57. The outcome stays partial.
- **Cell 122 (Summary).** "Every behavioural and demographic number of the paper is recovered exactly from participants.tsv". Several numbers are within tolerance but not exact:
  - mean ToM scores .517 and .610 against .54 and .63 (cell 15);
  - DCCS p .048 against .049 (cell 18);
  - Inc-Fail p .015 against .01 (cell 29);
  - DCCS b .148 against .16 (cell 40).

  beh-fb-tom also holds only under reading (a).
- **Entry README.** "the inter-region correlations are higher within networks and less negative across them than the paper reports". This holds for adults, but 3-year-old within-Pain is lower: .179 against .23 (cell 62), and non-bilateral Pain .146 against .17 (cell 68). The record's first finding cites 3-year-old within-ToM (.326 against .21) and leaves out the lower 3-year-old Pain value.
- **Record notes for irc-adult.** "so the offset is in the direction of a shared signal removed in the paper's processing". This is weakly supported. The shared-signal regressor also pushes both within-network values below the paper's (.286 and .258 against .48 and .35, cell 48), so it shows only the direction of the across-network shift. Cell 49's hedged wording ("would give an offset in this direction") is acceptable.
- **README:** the run time ("about three minutes") cannot be checked from the outputs, and cell 4 says loading alone takes about two minutes.

Every other "**Result:**" sentence and every other record note I checked matches the printed numbers.

**Round-1 reasons in the record.** The record gives my round-1 reasons in my own words, with problems 1, 2, 3, 4, 5 and 7 folded into the matching claims. One detail is missing: for replication-sample I gave blocked_by data_missing, and the record does not mention that. Its response explains why `other` is used (the checker does not allow data_missing on an `elsewhere` claim), which I accept.

**3. Round-1 points**

**Resolved:**
- **Problem 3:** the absence rule is now stated (cell 42), and the four outcomes are marked assumed.
- **Problem 4:** each bin is checked against its own bound (cell 90).
- **Problem 5:** reading (b) uses 159-TR timecourses (cell 86).
- **Problem 6:** acknowledged in the verification entry.
- **Problem 7:** the ranking is shown for all 8 readings (cell 66).
- **Problem 8:** the replicated-events check is added (cells 120 and 121).
- **Mask units:** the masks are in MNI mm. Sphere centroids are within 3.7 mm of their stated centres, and M1 and V1 are exact (cell 8).
- **Image scaling:** the images are int16 with no scaling (cell 8).

**Remaining, bearing on a conclusion:**
- **Problem 1, the IRC offset.** The mean matrices and diagnostic variants are now printed (cells 47 and 48), but the offset is still unexplained. It probably drives most of the inter-region, 3-year-old and maturity failures. The record states this, as a finding and in the irc-adult notes.
- **Problem 2, the O6 tie-break.** It is now recorded as an assumption, but rc-3yo-events is still partial under O6b and not reproduced under O6a.
- **The four absence claims** (irc-tom-behavior-age, irc-fb-across, rc-fb-no-difference, maturity-within) still flip between readings. The rule is now stated, so they are decided, but their outcomes rest on the assumed readings.
- **rc-overlap:** the new disagreement above.

**Remaining, not bearing on a conclusion:** per-participant artifact counts against the ART thresholds were not recomputed, as the record says.

## End of run

17 turns, 3 minutes, result: success.
