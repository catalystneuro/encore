# wang-2019 · verifier-2 · run 44311729419

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 268
drwxr-xr-x 6 runner runner    4096 Nov 18 13:20 .
drwxr-xr-x 8 runner runner    4096 Nov 18 13:20 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 18 13:14 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 18 13:14 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 18 13:20 .claude
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .env
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .env.development
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .env.local
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .env.production
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .env.test
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .env.test.local
drwx------ 2 runner runner    4096 Nov 18 13:20 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 18 13:14 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 18 13:14 .github
-rw-r--r-- 1 runner runner       0 Nov 18 13:20 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 18 13:14 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 18 13:14 .mcp.json
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat wang-2019-01.yaml
```

```
<persisted-output>
Output too large (34.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/a7bdebc0-d380-4c3e-86ee-bf933598764c/tool-results/bvo1lcf30.txt

Preview (first 2KB):
# Wang, Morotti, Tapa et al. (2019) from SPARC dataset 212

Tests the findings of [Wang et al. (2019)](https://doi.org/10.1113/jp278016) that can be tested on
[SPARC:212](https://sparc.science/datasets/212), version 1
([doi:10.26275/lok5-wje6](https://doi.org/10.26275/lok5-wje6)). The dataset holds the authors'
per-heart summary tables for Figures 1 (heart rate), 2, 3, 5F and 7F, and the MATLAB myocyte models
of Figure 8. It holds no optical maps or traces.

| Claim | Outcome |
|---|---|
| SNS raises heart rate in rabbit and mouse (Fig. 1A, 1D) | Reproduced |
| Rabbit APD and CaTD shorten, CaT amplitude rises; mouse APD prolongs (Fig. 1) | Reproduced, on the first 20 s of the Fig. 2 series |
| Rabbit HR, APD and CaTD change monotonically over 60 s (Fig. 2A) | Partially reproduced |
| Mouse APD is biphasic, 50.9, 60.6 and 46.5 ms at 0, 15 and 60 s (Fig. 2D) | Reproduced |
| CaT amplitude rises similarly in both species (Fig. 2C, 2F) | Reproduced |
| Tyramine and noradrenaline mimic SNS (Fig. 3B, 3C) | Reproduced; for noradrenaline under one reading of "monotonic" |
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "wang-2019-01.yaml"
}
```

```
1	schema_version: 3
2	id: wang-2019-01
3	datasets:
4	- archive: sparc
5	  id: "212"
6	  version: "1"
7	  doi: 10.26275/lok5-wje6
8	  relation: primary
9	paper: doi:10.1113/jp278016
10	date: 2026-11-18
11	entry: wang-2019
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-16
20	  runner:
[... 509 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Wang, Morotti, Tapa et al. (2019) from SPARC dataset 212
2	
3	Tests the findings of [Wang et al. (2019)](https://doi.org/10.1113/jp278016) that can be tested on
4	[SPARC:212](https://sparc.science/datasets/212), version 1
5	([doi:10.26275/lok5-wje6](https://doi.org/10.26275/lok5-wje6)). The dataset holds the authors'
6	per-heart summary tables for Figures 1 (heart rate), 2, 3, 5F and 7F, and the MATLAB myocyte models
7	of Figure 8. It holds no optical maps or traces.
8	
9	| Claim | Outcome |
10	|---|---|
11	| SNS raises heart rate in rabbit and mouse (Fig. 1A, 1D) | Reproduced |
12	| Rabbit APD and CaTD shorten, CaT amplitude rises; mouse APD prolongs (Fig. 1) | Reproduced, on the first 20 s of the Fig. 2 series |
13	| Rabbit HR, APD and CaTD change monotonically over 60 s (Fig. 2A) | Partially reproduced |
14	| Mouse APD is biphasic, 50.9, 60.6 and 46.5 ms at 0, 15 and 60 s (Fig. 2D) | Reproduced |
15	| CaT amplitude rises similarly in both species (Fig. 2C, 2F) | Reproduced |
16	| Tyramine and noradrenaline mimic SNS (Fig. 3B, 3C) | Reproduced; for noradrenaline under one reading of "monotonic" |
17	| Propranolol abolishes the SNS response (Fig. 3D) | Not reproduced |
18	| Rate steps give a biphasic APD, exaggerated by SNS (Fig. 3E) | Reproduced |
19	| At constant pacing SNS prolongs APD without a biphasic response (Fig. 3F) | Reproduced, resting on an assumption |
20	| Base-apex APD change differs in rabbit (Fig. 5F) and mouse (Fig. 7F) | Reproduced |
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_wang_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== CELL {i} [{c['cell_type']}]")
    if c['cell_type']=='markdown': print(src)
    else:
        print(src[:1500] + ('...[trunc]' if len(src)>1500 else ''))
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            t=''.join(t) if isinstance(t,list) else t
            print('--- OUT:'); print(t)
            if o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
EOF
```

```
<persisted-output>
Output too large (115.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/a7bdebc0-d380-4c3e-86ee-bf933598764c/tool-results/bshbt3bfp.txt

Preview (first 2KB):
===== CELL 0 [markdown]
# Reproducing Wang et al. (2019) from SPARC dataset 212

**Paper.** Wang L, Morotti S, Tapa S, Francis Stuart SD, Jiang Y, Wang Z, Myles RC, Brack KE, Ng GA,
Bers DM, Grandi E, Ripplinger CM (2019). Different paths, same destination: divergent action
potential responses produce conserved cardiac fight-or-flight response in mouse and rabbit hearts.
*J Physiol* 597, 3867-3883. [doi:10.1113/jp278016](https://doi.org/10.1113/jp278016). The claims file
(`claims/wang-2019.yaml`) was written from the accepted author manuscript in PubMed Central
(PMC6675632), with Methods and figure legends; the paper has no supplement.

**Dataset.** [SPARC:212](https://sparc.science/datasets/212), "Sympathetic nerve stimulation of mouse
and rabbit hearts", version 1, [doi:10.26275/lok5-wje6](https://doi.org/10.26275/lok5-wje6), published
2022-01-05. Version 1 is the only published version, and the paper (2019) cites no version, so it is
the one pinned. Files are read from the public bucket `sparc-prod-aod-discover-publish50-use1` at the
object versions listed in that version's manifest.

[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/a7bdebc0-d380-4c3e-86ee-bf933598764c/tool-results/bshbt3bfp.txt"
}
```

```
1	===== CELL 0 [markdown]
2	# Reproducing Wang et al. (2019) from SPARC dataset 212
3	
4	**Paper.** Wang L, Morotti S, Tapa S, Francis Stuart SD, Jiang Y, Wang Z, Myles RC, Brack KE, Ng GA,
5	Bers DM, Grandi E, Ripplinger CM (2019). Different paths, same destination: divergent action
6	potential responses produce conserved cardiac fight-or-flight response in mouse and rabbit hearts.
7	*J Physiol* 597, 3867-3883. [doi:10.1113/jp278016](https://doi.org/10.1113/jp278016). The claims file
8	(`claims/wang-2019.yaml`) was written from the accepted author manuscript in PubMed Central
9	(PMC6675632), with Methods and figure legends; the paper has no supplement.
10	
11	**Dataset.** [SPARC:212](https://sparc.science/datasets/212), "Sympathetic nerve stimulation of mouse
12	and rabbit hearts", version 1, [doi:10.26275/lok5-wje6](https://doi.org/10.26275/lok5-wje6), published
13	2022-01-05. Version 1 is the only published version, and the paper (2019) cites no version, so it is
14	the one pinned. Files are read from the public bucket `sparc-prod-aod-discover-publish50-use1` at the
15	object versions listed in that version's manifest.
16	
17	**What the dataset holds.** No optical maps or traces. Its readme says: "There is no primary data,
18	only a derivative folder containing experimental optical mapping data summarized in the multi
19	spreadsheet excel table." The workbook `files/derivative/exp_data_Wang_et_al.xlsx` gives one value per
20	heart for Figure 1A and 1D (heart rate), Figure 2 (time courses of HR, APD80, CaTD80 and relative CaT
[... 618 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/a7bdebc0-d380-4c3e-86ee-bf933598764c/tool-results/bshbt3bfp.txt",
 "offset": 639,
 "limit": 500
}
```

```
639	                         "t": r["t"], "p": r["p"], "hearts in direction": n_dir,
640	                         "test holds": (r["p"] < 0.05) and np.sign(r["mean_diff"]) == direction,
641	                         "majority holds": n_dir > len(v) / 2})
642	    return pd.DataFrame(rows)
643	
644	fig1bc = direction_table("rabbit", {"APD80": -1, "CaTD80": -1, "CaT amplitude": 1})
645	print("Rabbit"); print(fig1bc.round(4).to_string(index=False))
646	--- OUT:
647	Rabbit
648	     variable direction         window  n  baseline      SNS  mean change       t      p  hearts in direction  test holds  majority holds
649	        APD80      down     a: at 20 s  4     173.2 148.5750     -24.6250 -2.0836 0.1286                    4       False            True
650	        APD80      down b: mean 5-20 s  4     173.2 156.4938     -16.7063 -1.9941 0.1401                    4       False            True
651	        APD80      down c: peak 5-20 s  4     173.2 148.5750     -24.6250 -2.0836 0.1286                    4       False            True
652	       CaTD80      down     a: at 20 s  4     199.4 159.8750     -39.5250 -4.5302 0.0201                    4        True            True
653	       CaTD80      down b: mean 5-20 s  4     199.4 168.0250     -31.3750 -4.9190 0.0161                    4        True            True
654	       CaTD80      down c: peak 5-20 s  4     199.4 159.8750     -39.5250 -4.5302 0.0201                    4        True            True
655	CaT amplitude        up     a: at 20 s  6       1.0   1.1217       0.1217  7.8085 0.0006                    6        True            True
656	CaT amplitude        up b: mean 5-20 s  6       1.0   1.0817       0.0817  5.7409 0.0022                    6        True            True
657	CaT amplitude        up c: peak 5-20 s  6       1.0   1.1217       0.1217  7.8085 0.0006                    6        True            True
658	
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/a7bdebc0-d380-4c3e-86ee-bf933598764c/tool-results/bshbt3bfp.txt",
 "offset": 1139,
 "limit": 460
}
```

```
1139	30.0  3  39.47  5.43  3.0     1.8667  2.0000  0.1835           0.5556                  0.3884
1140	40.0  3  40.03  5.08  3.0     2.4333  3.1650  0.0870           0.5172                  0.2272
1141	50.0  3  38.73  7.27  3.0     1.1333  0.6870  0.5630           0.7730                  0.5170
1142	60.0  3  39.50  6.80  3.0     1.9000  1.4777  0.2776           0.6229                  0.3884
1143	  repeated measures ANOVA over 3 hearts: F(9, 18) = 1.95, p = 0.109
1144	  monotonic (a) mean at every step: False; steps against: [(25.0, 30.0, -1.67), (40.0, 50.0, -1.3)]
1145	  monotonic (b) no significant step against: True; significant steps against: []
1146	--- propranolol + SNS: CaTD80 (expected down)
1147	      n   mean    sd    n  mean_diff       t       p  p_rm_holm_sidak  p_rm_pooled_holm_sidak
1148	time                                                                                         
1149	0.0   3  72.87  2.16  NaN        NaN     NaN     NaN              NaN                     NaN
1150	5.0   3  72.70  2.09  3.0    -0.1667 -2.5000  0.1296           0.6706                  0.8680
1151	10.0  3  72.53  2.68  3.0    -0.3333 -1.0483  0.4045           0.8691                  0.8680
1152	15.0  3  72.57  2.68  3.0    -0.3000 -0.8321  0.4929           0.8691                  0.8680
1153	20.0  3  72.87  2.23  3.0    -0.0000 -0.0000  1.0000           1.0000                  1.0000
1154	25.0  3  72.57  2.29  3.0    -0.3000 -1.9640  0.1885           0.7682                  0.8680
1155	30.0  3  72.13  2.49  3.0    -0.7333 -3.6168  0.0687           0.4728                  0.3207
1156	40.0  3  72.33  2.61  3.0    -0.5333 -1.8353  0.2079           0.7682                  0.5630
1157	50.0  3  72.23  2.80  3.0    -0.6333 -1.5618  0.2587           0.7762                  0.4204
1158	60.0  3  72.13  3.19  3.0    -0.7333 -1.0647  0.3986           0.8691                  0.3207
[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  - id:\|id: fig" wang-2019.yaml | head -40; grep -n -i "any reading\|partial\|either\|sigmaplot\|holm\|elsewhere\|registration" wang-2019.yaml; grep -n -i "sigmaplot\|holm\|sidak\|statistic" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "wang-2019.yaml",
 "limit": 250
}
```

```
1	# Claims for Wang, Morotti, Tapa et al. (2019), J Physiol, on SPARC dataset 212
2	# ("Sympathetic nerve stimulation of mouse and rabbit hearts").
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
4	# 2026-11-18, under protocol pilot-16 (docs/protocol.md), reader role.
5	#
6	# Text read: the accepted author manuscript in PubMed Central (PMC6675632), full text with
7	# Methods, Results, Discussion and figure legends (paper/10.1113-jp278016.txt). No PDF was
8	# supplied, so the figures themselves were not seen; claims rest on the text and legends. The
9	# paper cites no supplement.
10	#
11	# Code: the paper links only the published myocyte models, at
12	# https://somapp.ucdmc.ucdavis.edu/Pharmacology/bers/ (rabbit model in the Negroni et al. 2015
13	# / Bartos et al. 2017 lineage, mouse model of Morotti et al. 2014) and
14	# http://elegrandi.wixsite.com/grandilab/downloads. Both pages were listed on 2026-11-18; the
15	# MATLAB downloads sit behind a registration form (name, affiliation, email) and were not
16	# fetched. They hold no analysis of the optical maps: the paper did that analysis in Optiq
17	# (Cairn, UK), which is not open. No criterion below takes a detail from code.
18	#
19	# Data the paper used. Male C57BL/6J mice (12 to 16 weeks, n=13) and male New Zealand White
20	# rabbits (3.0 to 3.5 kg, n=9). Innervated hearts with spinal cord (C1 to T12),
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def against_time0" -A60 sns.py
```

```
193:def against_time0(w: pd.DataFrame) -> pd.DataFrame:
194-    """Each time point against time 0: reading (i), paired t-tests; reading (ii), a one-way repeated
195-    measures ANOVA over the hearts with complete data, then paired t-tests against time 0 on those
196-    hearts with the Holm-Sidak adjustment (assumption; see the module docstring)."""
197-    t0 = w.index.min()
198-    rows = []
199-    for t in w.index[w.index > t0]:
200-        rows.append({"time": t, **paired(w.loc[t0], w.loc[t])})
201-    out = pd.DataFrame(rows).set_index("time")
202-    complete = w.loc[:, w.notna().all()]
203-    out.attrs["anova_hearts"] = complete.shape[1]
204-    if complete.shape[1] >= 2:
205-        long = complete.stack().rename("value").reset_index()
206-        long["time"] = long["time"].astype(str)
207-        res = AnovaRM(long, "value", "heart", within=["time"]).fit().anova_table
208-        out.attrs["anova_F"] = float(res["F Value"].iloc[0])
209-        out.attrs["anova_df"] = (float(res["Num DF"].iloc[0]), float(res["Den DF"].iloc[0]))
210-        out.attrs["anova_p"] = float(res["Pr > F"].iloc[0])
211-        p = [paired(complete.loc[t0], complete.loc[t])["p"] for t in out.index]
212-        out["p_rm_holm_sidak"] = multipletests(p, method="holm-sidak")[1]
[... 41 more lines not kept]
```

**Agent**

**Verifier report, round 2: wang-2019-01 (doi:10.1113/jp278016, SPARC:212 v1)**

The claims file has 25 claims and the attempt record has 25 outcomes: 11 reproduced, 1 partially_reproduced, 1 not_reproduced and 12 blocked (8 data_missing, 4 not_runnable). Three outcomes are marked `assumed: true`: fig1bc, fig1ef and fig3f.

**1. Outcomes**

| Claim | Agree? | Note |
|---|---|---|
| fig1a, fig1d | Yes | |
| fig1bc (assumed) | Yes | The assumption, that the first 20 s of the Fig. 2 series stand in for the Fig. 1 hearts, is stated and reasonable. The notes now say that rabbit APD80 passes only on the majority reading (cell 18, p=0.13). |
| fig1ef (assumed) | Yes | Same assumption, stated. |
| fig2a partially_reproduced | No, I'd give not_reproduced | The criterion is "reproduced when … all three monotonic … and significant at 60 s" and has no partial rule, unlike fig2d, fig2cf and fig3abc. Partial is arguable under the protocol's general definition. But the reason given for it is false (see §2). |
| fig2d, fig2cf, fig3e, fig4g-5f, fig7f | Yes | fig4g-5f is borderline (p=0.0482, cell 47). |
| fig3abc reproduced | Yes | The criterion asks for "HR rising", which noradrenaline meets: HR stays above time 0 throughout (cell 34, 82.5 bpm at 59.75 s, p=0.023). The record's general rule ("counts a claim reproduced when it holds under any reading") is not in this criterion's text. The outcome stands anyway. |
| fig3d not_reproduced | Yes, by the criterion's rule | It rests on reading (i), APD80 at 10 s p=0.0101 (cell 38). See §2 on the pooled-error support. |
| fig3f reproduced (assumed) | Yes on the letter of reading (a) | The column pairing is stated and is the more plausible choice (4th of 120 assignments, cell 44). The whole effect is present at time 0 (+2.69 ms, p=0.036), and the change from time 0 does not differ at any time (p 0.18 to 0.94). The notes and cell 45 say this plainly. |
| 8 × data_missing | Yes | |
| fig8e, fig8f, fig8ij, fig9 not_runnable | Blocked yes; the reason is not established | "Octave cannot be installed without root" is untested. conda-forge ships Octave as a user-space install, and Octave has `ode15s`. "A Python lock file cannot hold it" describes a choice about the environment, not a property of the code. |

**2. Text checked against the printed outputs**

- **Cell 29:** "The 60 s SD (4.89 ms) is about half of the Abstract's 9.1." Cells 12, 27 and 28 print 4.94. The record has the correct value.
- **Cell 25, and the record's fig2a notes:** "heart rate rises and APD80 and CaTD80 shorten significantly from time 0 at 60 s under every significance reading". The record words it as "hold under every significance reading", and its verifications response says "for all three variables under every significance reading".
  - Cells 23 and 24 contradict this: APD80 at 60 s has Holm-Sidak p=0.1766 and "60 s sig (ii)" is False.
  - The first sentence of cell 25, and the record's own line "APD80 does not (p = 0.18)", also contradict it.
  - This sentence is the stated basis for the partial outcome.
- **Cell 25:** contains the typo "APD80 APD80 falls".
- **Cells 39 and 52 (Summary), and the record's fig3d notes and findings:** they count "APD80 at 25 s (p = 0.036)" as a pooled-error post hoc result.
  - The APD80 repeated measures ANOVA is not significant (p=0.109, cell 38), so under reading (ii) no post hoc comparison follows. Cell 24 gates the same comparison on ANOVA p<0.05 for fig2a.
  - Only the heart-rate comparisons (ANOVA p=0.031) qualify. They rise in 2 of 3 hearts: heart 1 goes from 226 to 224 bpm (cell 7). The paired p at 60 s is 0.24.
  - "The result does not rest on the one unadjusted test" therefore leans on a pooled error with n=3 and no sphericity correction.
- **"SigmaPlot's pooled-error Holm-Sidak" (cells 25 and 39):** the paper names no software (Methods, "Data analysis and statistics"). The phrase should read as a variant, not as the paper's method. My round-1 wording invited this.
- **Record fig2a notes, "APD80 p = 6e-5":** not visible in the outputs, which print 0.0001 at 4 dp. The two are consistent.
- **README:** the fig1bc/fig1ef row ("Reproduced, on the first 20 s…") leaves out that rabbit APD80 holds only on the majority reading. The rest of the README matches.
- **Cell 13, a supporting sentence, not a conclusion:** "In both species the whole-field change … lies in the range spanned by the base and apex changes". One rabbit heart, at −6.6 ms, lies outside both the base and the apex ranges (cell 12).
- **Everything else checks:** the other Result cells, the Summary, the README and the record's notes match the printed numbers. This includes fig3abc, fig3e, fig3f, fig2cf, fig2d (apart from the SD in cell 29), fig4g/fig7f, the 0.75 chance figure, 1.65 to 4.84 ms, and 400.9 against 380.3.
- **My round-1 reasons in the record:** they are restated faithfully, close to verbatim. Two small gaps:
  - My B6 example (rabbit APD80 at 60 s: paired p=0.021 against Holm-Sidak 0.18) is missing.
  - The simulation claims lost my blocked_by "other". They are now recorded as blocked, with "questionable" in the reason.

**3. Round-1 points**

Resolved:
- B3: the pairing evidence and the change-from-time-0 variant were added.
- B4: the notes now carry the substitution and the majority reading.
- B5: the weakness of reading (b) is now in the notes.
- B7, B8, B9, B10: now in the notes.
- C items resolved: raw Fig3 blocks and column B printed; Fig1 sheet printed (no window stated); `revisions/` listed (banner, manifest, readme, no data); instructions printed (Figure 8 only).

Partly resolved:
- B2 / fig3d: there is more evidence now, but the added pooled support is weaker than the record states (see §2).
- B6: the pooled-error variant was added, with no sphericity correction.

Remaining, bearing on a conclusion:
1. fig2a: the partial label rests on a false sentence about APD80 under reading (ii). I still give not_reproduced.
2. fig3d: drop the APD80 25 s pooled result, which follows a non-significant ANOVA. Restate the HR pooled result as 2 of 3 hearts with no sphericity correction. The outcome itself stands on reading (i).
3. fig8e, fig8f, fig8ij, fig9: not_runnable rests on an untested claim that Octave can't be installed. The claims file's "data elsewhere / registration form" still misreads the dataset; the record has passed this to a reader.
4. fig3f: the outcome stays on the letter of reading (a). The criterion does not exclude a difference already present at time 0, which is the only difference the data show.

Minor fixes: the SD in cell 29 (4.89 should be 4.94), the doubled "APD80" in cell 25, and the range sentence in cell 13.

## End of run

12 turns, 3 minutes, $1.22 at API prices, result: success.
