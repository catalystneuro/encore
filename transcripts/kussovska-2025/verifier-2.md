# kussovska-2025 · verifier-2 · run 42816134882

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 780
drwxr-xr-x 6 runner runner    4096 Nov 10 13:43 .
drwxr-xr-x 7 runner runner    4096 Nov 10 13:43 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 12:28 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 12:28 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 10 13:43 .claude
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .env
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .env.development
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .env.local
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .env.production
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .env.test
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .env.test.local
drwx------ 2 runner runner    4096 Nov 10 13:43 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 12:28 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 12:28 .github
-rw-r--r-- 1 runner runner       0 Nov 10 13:43 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 12:28 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 12:28 .mcp.json
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -50 kussovska-2025.yaml; echo ----; head -80 kussovska-2025-01.yaml
```

```
# Kussovska, Kim & Rungratsameetaweemana (2025) from dandiset 000469

Tests the findings of [Kussovska et al. (2025)](https://doi.org/10.1101/2025.10.31.684900) on
[DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), the human single-neuron
recordings of Kyzar et al. (2024) during a Sternberg working memory task, which the paper reuses.

| Claims | Outcome |
|---|---|
| Units by region, behavior (accuracy, load effect, reaction times) | Reproduced (6) |
| Load-modulated neurons (Fig. 1e) | Reproduced |
| RT-modulated neurons not significant (Fig. 1f) | Not reproduced; the paper's values come from the code's use of subject 1's reaction times for every neuron |
| Concept cells, single-cell and population persistence, cross-temporal decoding | Reproduced (6) |
| Maintenance decoding within participant, load 1 / load 2 | Reproduced / partially reproduced |
| Bin-width decoding / pairwise comparisons / load 2 | Partially reproduced / not reproduced / reproduced |
| dPCA state-space analyses (Fig. 3) | Reproduced (3); for Fig. 3h only with a dPCA setting other than the code's |
| Population bursts against the Poisson null, encoding and maintenance; loads 2 and 3 | Reproduced (3) |
| Burst differences between ACG groups and across epochs (Fig. 4f-j) | Partially reproduced (3) |
| ACG fits, cell-type clusters and their features, rodent validation, concept cell types | Reproduced (6) |
| Cell-type bursting (Fig. 6a-d), IN load dependence | Partially reproduced (6a,b), not reproduced (6c,d), reproduced (load dependence) |
| Load and RT modulation by cell type (Fig. 6e,f) | Reproduced (with one of the two cell-type readings) / not reproduced |
[... 147 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 80,2000p kussovska-2025-01.yaml
```

```
<persisted-output>
Output too large (69.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/ad2f576d-7745-475d-a221-e21e498c0353/tool-results/bo6nh9lxh.txt

Preview (first 2KB):
  notes: Median RT 1.084 s correct against 1.503 s incorrect, correct faster in 20 of 21 participants;
    p = 0.001 under both readings.
- claim: fig1e-load-modulated-neurons
  outcome: reproduced
  notebook: reproduce_kussovska_2025.ipynb
  output: claim:fig1e-load-modulated-neurons
  measured:
  - 20.4
  - 18.75
  - 10.53
  notes: Reading (a) with the code's shared permutation gives preSMA 20.40% (p = 0.000), vmPFC 18.75%
    (p = 0.009), dACC 10.53% (p = 0.025), all within tolerance; the within-participant permutation gives
    19.20%, 18.75%, 9.94% (p 0.000 to 0.018). With all trials (reading b) 22.80%, 21.88% and 12.87%, all
    significant. AMY and HPC are not significant under any reading.
  deviations:
  - The GLM is fitted by Newton's method in place of sklearn's PoissonRegressor; the largest slope difference
[... 27 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ad2f576d-7745-475d-a221-e21e498c0353/tool-results/bo6nh9lxh.txt"
}
```

```
1	  notes: Median RT 1.084 s correct against 1.503 s incorrect, correct faster in 20 of 21 participants;
2	    p = 0.001 under both readings.
3	- claim: fig1e-load-modulated-neurons
4	  outcome: reproduced
5	  notebook: reproduce_kussovska_2025.ipynb
6	  output: claim:fig1e-load-modulated-neurons
7	  measured:
8	  - 20.4
9	  - 18.75
10	  - 10.53
11	  notes: Reading (a) with the code's shared permutation gives preSMA 20.40% (p = 0.000), vmPFC 18.75%
12	    (p = 0.009), dACC 10.53% (p = 0.025), all within tolerance; the within-participant permutation gives
13	    19.20%, 18.75%, 9.94% (p 0.000 to 0.018). With all trials (reading b) 22.80%, 21.88% and 12.87%, all
14	    significant. AMY and HPC are not significant under any reading.
15	  deviations:
16	  - The GLM is fitted by Newton's method in place of sklearn's PoissonRegressor; the largest slope difference
17	    over 21 checked neurons is 1.1e-04.
18	  - The code's p is the fraction of null counts at or above the observed count without + 1, so p = 0.000
19	    is printed where the paper gives 0.001.
20	- claim: fig1f-rt-modulation-not-significant
[... 766 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ad2f576d-7745-475d-a221-e21e498c0353/tool-results/bo6nh9lxh.txt",
 "offset": 787
}
```

```
787	      gives 49–54. Per participant 4.14 ± 3.66 (cell 32). Problem 8: the downstream concept set is a single
788	      draw (code reading, seed 0); counts range 57–60 over seeds, and the Methods reading is not carried
789	      downstream.'
790	    response: 'No change to the analysis: the set used downstream is the reading that matches the paper
791	      for every seed, and a seed is a standard choice; its notes already give the range over seeds and
792	      the Methods'' reading.'
793	  - claim: fig2ab-single-cells-not-persistent
794	    agrees: true
795	    outcome: reproduced
796	    reason: 50 of 58 cells are not persistent under (a), 48 of 58 under (b) (cell 34).
797	    response: No change.
798	  - claim: fig2c-population-persistence
799	    agrees: true
800	    outcome: reproduced
801	    reason: 'Load 1: preferred trace above nonpreferred in 100% of bins, all bins significant (cell 36).'
802	    response: No change.
803	  - claim: ext1bc-persistence-by-load
804	    agrees: true
805	    outcome: reproduced
806	    reason: 'Significant bins: 1.00 at load 1, 1.00 at load 2, 0.60 at load 3 (cell 38).'
[... 272 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" kussovska-2025.yaml; grep -n "^- id:\|^  id:" kussovska-2025.yaml | head -60; grep -c "^- claim:" kussovska-2025-01.yaml; grep -c "^  - claim:" kussovska-2025-01.yaml
```

```
45
62:- id: units-by-region
96:- id: behavior-accuracy
112:- id: fig1c-accuracy-load1-vs-load3
129:- id: behavior-rt
148:- id: rt-in-vs-out-memory
164:- id: rt-correct-vs-incorrect
176:- id: fig1e-load-modulated-neurons
225:- id: fig1f-rt-modulation-not-significant
260:- id: concept-cells-count
293:- id: fig2ab-single-cells-not-persistent
313:- id: fig2c-population-persistence
339:- id: ext1bc-persistence-by-load
354:- id: fig2d-cross-temporal-localized
386:- id: ext1de-cross-temporal-load23
400:- id: fig2e-maintenance-decoding-amy-mtl
439:- id: ext1f-maintenance-decoding-load2
468:- id: fig2f-bin-width-decoding
514:- id: fig2f-bin-width-pairwise
551:- id: ext1g-bin-width-load2
[... 28 more lines not kept]
```

**Agent**

Now dump both notebooks' cells with outputs to text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json,os
for nb in ["reproduce_kussovska_2025.ipynb","dpca_kussovska_2025.ipynb"]:
    d=json.load(open(nb))
    out=[]
    for i,c in enumerate(d["cells"]):
        out.append(f"\n##### CELL {i} [{c['cell_type']}]\n"+"".join(c["source"]))
        for o in c.get("outputs",[]):
            if "text" in o: out.append("\n--- out:\n"+"".join(o["text"]))
            elif "data" in o and "text/plain" in o["data"]:
                out.append("\n--- out(data):\n"+"".join(o["data"]["text/plain"])[:4000])
            elif o.get("output_type")=="error": out.append("\n--- ERROR "+o.get("ename",""))
    open(os.environ["TMPDIR"]+"/"+nb+".txt","w").write("".join(out))
    print(nb,len(d["cells"]))
EOF
wc -l $TMPDIR/*.txt
```

```
reproduce_kussovska_2025.ipynb 149
dpca_kussovska_2025.ipynb 18
   403 /tmp/claude-1001/dpca_kussovska_2025.ipynb.txt
  4151 /tmp/claude-1001/reproduce_kussovska_2025.ipynb.txt
  4554 total
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/dpca_kussovska_2025.ipynb.txt"
}
```

```
1	
2	##### CELL 0 [markdown]
3	# Kussovska et al. (2025) on dandiset 000469: the dPCA state-space claims
4	
5	Paper. Kussovska D, Kim R, Rungratsameetaweemana N (2025). Neural heterogeneity shapes the
6	temporal structure of human working memory. bioRxiv,
7	[doi:10.1101/2025.10.31.684900](https://doi.org/10.1101/2025.10.31.684900). The claims file
8	(`claims/kussovska-2025.yaml`) was written from the bioRxiv full text posted on 1 November 2025.
9	
10	Dandiset. [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), version
11	0.231213.2047, the version the paper cites (see the header of `reproduce_kussovska_2025.ipynb`,
12	which tests the other claims and shows that the four published versions hold the same assets).
13	
14	This notebook tests the three claims on dPCA (Fig. 3), apart from the main notebook so that each
15	stays within the time limit. It streams the same files, finds the same concept cells (the code's
16	bootstrap, seed 0, as in the main notebook) and runs the 100 resampling splits of the paper's code
17	in parallel, each dPCA fit on one thread.
18	
19	| Claim | Tested here |
20	|---|---|
[... 384 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kussovska-2025.yaml",
 "offset": 565,
 "limit": 110
}
```

```
565	- id: fig3abc-trajectory-complexity
566	  statement: dPCA encoding trajectories of load 1 concept-cell activity made a single large
567	    excursion in state space, while maintenance trajectories were more complex, with multiple
568	    turns and changes in direction.
569	  source: Results, Encoding and maintenance occupy distinct neural subspaces, paragraph 2;
570	    Figure 3a-c
571	  quote: Applying dPCA revealed simple encoding trajectories characterized by a single large
572	    excursion in state space ... In contrast, maintenance trajectories were markedly more
573	    complex, with multiple turns and changes in direction
574	  depends_on:
575	  - concept-cells-count
576	  criterion: The dPCA fits of fig3d-encoding-vs-maintenance-separability. The paper gives no
577	    measure of complexity; the figure is a visual reading. The measure is open; readings are
578	    (a) tortuosity, the path length of each held-out stimulus trajectory in the first three
579	    stimulus dPCs divided by the largest distance from its start point; (b) the number of
580	    reversals of direction (sign changes of the derivative) summed over the first three
581	    stimulus dPCs. Reproduced when, under one reading, the median over stimuli and resampling
582	    splits is larger for maintenance than for encoding.
583	- id: fig3d-encoding-vs-maintenance-separability
584	  statement: Stimulus separation in dPCA space was higher during encoding than during
[... 90 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_kussovska_2025.ipynb.txt",
 "limit": 900
}
```

```
1	
2	##### CELL 0 [markdown]
3	# Reproducing Kussovska, Kim and Rungratsameetaweemana (2025) from dandiset 000469
4	
5	Paper. Kussovska D, Kim R, Rungratsameetaweemana N (2025). Neural heterogeneity shapes the
6	temporal structure of human working memory. bioRxiv,
7	[doi:10.1101/2025.10.31.684900](https://doi.org/10.1101/2025.10.31.684900). The claims file
8	(`claims/kussovska-2025.yaml`) was written from the bioRxiv full text posted on 1 November 2025
9	(main text, figure legends and Methods; the Extended Data figures and their legends were not in
10	the text read).
11	
12	Dandiset. [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), version
13	0.231213.2047 (Kyzar et al. 2024, human single neurons during a Sternberg working memory task).
14	This is the version the paper cites (Methods, Participants and data source, and Data
15	availability). The four published versions (0.231213.2047, 0.240122.1800, 0.240122.1812,
16	0.240123.1806) hold the same 41 assets with the same asset identifiers and sizes, which the data
17	check below confirms, so the version the paper's code downloads (0.240123.1806) gives the same
18	data.
19	
20	Paper's code. github.com/dariakussovska/heterogeneitywm at commit 5144fe8, the commit the
[... 880 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_kussovska_2025.ipynb.txt",
 "offset": 900,
 "limit": 800
}
```

```
900	    p = np.mean(np.abs(null) >= np.abs(obs), 0)
901	    frac = np.mean((p < 0.05) & (obs > 0))
902	    win = []
903	    for i in range(3):
904	        c = wm.count_in(SPK[n], t.maint.values + i, np.minimum(t.maint.values + i + 1, t.probe.values))
905	        o = c[pm].mean() - c[~pm].mean()
906	        nn = np.array([c[q].mean() - c[~q].mean() for q in perms])
907	        win.append(bool(o > 0 and np.mean(np.abs(nn) >= abs(o)) < 0.05))
908	    rows.append({"nid": n, "sub": NT["sub"].iat[n], "region": NT.region.iat[n], "pref_trials": int(pm.sum()),
909	                 "frac_bins_higher": frac, "M1": win[0], "M2": win[1], "M3": win[2]})
910	sc = pd.DataFrame(rows)
911	sc["persistent_a"] = sc.frac_bins_higher >= 0.5
912	sc["persistent_b"] = sc[["M1", "M2", "M3"]].all(1)
913	print(sc.round(2).to_string(index=False))
914	print(f"\n{len(sc)} concept cells; preferred load-1 trials per cell {sc.pref_trials.min()} to {sc.pref_trials.max()}")
915	print(f"persistent under (a): {sc.persistent_a.sum()}; not persistent: {(~sc.persistent_a).sum()}")
916	print(f"persistent under (b): {sc.persistent_b.sum()}; not persistent: {(~sc.persistent_b).sum()}")
917	print("cells significant in M1, M2, M3:", sc[["M1", "M2", "M3"]].sum().to_dict())
918	print("by participant (persistent a / cells):", sc.groupby("sub").agg(cells=("nid", "size"), pa=("persistent_a", "sum"), pb=("persistent_b", "sum")).T.to_dict())
919	for thr in [0.25, 0.75]:
[... 780 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_kussovska_2025.ipynb.txt",
 "offset": 1700,
 "limit": 700
}
```

```
1700	   tau_rise       tau_rise       48.3944            0.0621
1701	  tau_decay          Decay      498.9962            0.1109
1702	shipped table: R2 > 0.3 for 294, R2 >= 0.3 for 294; agreement on R2 > 0.3 with reading (a): 0.976
1703	paper: 294 (tolerance 264.6 to 323.4)
1704	
1705	##### CELL 76 [markdown]
1706	**Result: reproduced.** 316 neurons have R2 > 0.3 under reading (a) and 298 under reading (b),
1707	both within tolerance. The firing rate and ISI CV of reading (a) equal the code's shipped table
1708	exactly, and the normalized mean ACG and Royer burst index agree within 1% for 99% of neurons, so
1709	the code used every spike of the unit. The fit itself is a limitation of this attempt: the fitted
1710	R2 agrees with the shipped MATLAB values within 1% for only 48% of neurons and the time constants
1711	for 6 to 11% (printed above), as scipy's optimizer finds other local optima than MATLAB's.
1712	Classification at R2 > 0.3 agrees for 97.6% of neurons, but tau_rise is a clustering feature, so
1713	the cell types of fig5c differ from the paper's, and tau_decay defines the decay groups of the
1714	burst analyses. The round-1 run of this notebook, with the same code, gave 317 under reading (a), so
1715	one neuron's fit falls on either side of the threshold between runs, and with it the reading (a)
1716	types of a few neurons.
1717	##### CELL 77 [markdown]
1718	## fig5c-cell-type-clusters
1719	
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_kussovska_2025.ipynb.txt",
 "offset": 2400,
 "limit": 600
}
```

```
2400	methods/prominence/d1/real     AllFit 12         12.5          5.8          11  2.0 0.0037    NaN
2401	 methods/prominence/d2/own     All902 20         12.5          6.4          19  2.0 0.0001 0.0010
2402	 methods/prominence/d2/own     LowACG 12         52.5         39.5          10  4.0 0.0060 0.0121
2403	 methods/prominence/d2/own    HighACG 12         20.0         12.8           9  8.0 0.0150 0.0200
2404	 methods/prominence/d2/own ShortDecay 12         29.5         25.1          12  0.0 0.0022 0.0059
2405	 methods/prominence/d2/own  LongDecay 12         33.0         19.6          12  0.0 0.0022 0.0059
2406	 methods/prominence/d2/own    Concept  5         52.0         48.8           4  1.0 0.0796 0.0910
2407	 methods/prominence/d2/own         PY 12         67.5         49.7          11  6.0 0.0096 0.0154
2408	 methods/prominence/d2/own         IN 19         24.0         12.9          13 58.0 0.1365 0.1365
2409	 methods/prominence/d2/own     AllFit 12         12.5          7.0          11  2.0 0.0037    NaN
2410	methods/prominence/d2/real     All902 20         12.5          4.7          19  3.0 0.0001 0.0011
2411	methods/prominence/d2/real     LowACG 12         52.5         28.2          12  0.0 0.0022 0.0035
2412	methods/prominence/d2/real    HighACG 12         20.0         11.7           8 10.0 0.0229 0.0305
2413	methods/prominence/d2/real ShortDecay 12         29.5         20.1          12  0.0 0.0022 0.0035
2414	methods/prominence/d2/real  LongDecay 12         33.0         19.1          12  0.0 0.0022 0.0035
2415	methods/prominence/d2/real    Concept  5         52.0         50.8           4  4.0 0.3452 0.3452
2416	methods/prominence/d2/real         PY 12         67.5         35.1          12  0.0 0.0022 0.0035
2417	methods/prominence/d2/real         IN 19         24.0         10.9          14 43.0 0.0364 0.0416
2418	methods/prominence/d2/real     AllFit 12         12.5          5.8          11  2.0 0.0037    NaN
2419	own maintenance, code/height/d1/real: 
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_kussovska_2025.ipynb.txt",
 "offset": 3000,
 "limit": 600
}
```

```
3000	methods/prominence/d1/real    PY 12         64.0         43.9          12  0.0 0.0022 0.0025
3001	methods/prominence/d1/real    IN 19         29.0          6.9          18  5.0 0.0003 0.0012
3002	 methods/prominence/d2/own    PY 12         64.0         55.0          10 12.0 0.0342 0.0391
3003	 methods/prominence/d2/own    IN 19         29.0         13.4          16  7.0 0.0004 0.0016
3004	methods/prominence/d2/real    PY 12         64.0         43.7          12  0.0 0.0022 0.0025
3005	methods/prominence/d2/real    IN 19         29.0          6.9          18  4.0 0.0003 0.0010
3006	(a) Poisson null, types (a), maint_own:
3007	                   reading group  n  real_median  null_median  real_above    W      p   p_BH
3008	       code/height/d1/real    PY 12         91.5         69.2          12  0.0 0.0022 0.0089
3009	       code/height/d1/real    IN 19         95.0         84.5          15 34.0 0.0141 0.0376
3010	        code/height/d2/own    PY 12         91.5         95.7           5 30.0 0.4802 0.6730
3011	        code/height/d2/own    IN 19         95.0        105.0           5 28.0 0.0070 0.0495
3012	       code/height/d2/real    PY 12         91.5         69.7          12  0.0 0.0022 0.0089
3013	       code/height/d2/real    IN 19         95.0         83.4          14 37.0 0.0196 0.0522
3014	   code/prominence/d1/real    PY 12         67.5         34.4          12  0.0 0.0022 0.0044
3015	   code/prominence/d1/real    IN 19         24.0         10.6          14 44.0 0.0401 0.0642
3016	    code/prominence/d2/own    PY 12         67.5         49.3          11  6.0 0.0096 0.0322
3017	    code/prominence/d2/own    IN 19         24.0         12.8          13 56.0 0.1165 0.1332
3018	   code/prominence/d2/real    PY 12         67.5         35.1          12  0.0 0.0022 0.0057
3019	   code/prominence/d2/real    IN 19         24.0         10.8          14 42.0 0.0329 0.0527
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_kussovska_2025.ipynb.txt",
 "offset": 3600,
 "limit": 600
}
```

```
3600	0.030).
3601	##### CELL 129 [markdown]
3602	## fig6gh-in-concept-cv2
3603	
3604	> Interneuron concept cells had higher CV2 during maintenance than encoding on preferred load 1
3605	> trials but not on nonpreferred trials, while pyramidal concept cells showed stable CV2.
3606	
3607	Holt's CV2 of the interspike intervals of each cell's spikes concatenated over preferred (or
3608	nonpreferred) trials, in encoding (first image, 1 s) and maintenance (2.5 s); trials of load 1
3609	(Results) or of all loads (the code). Readings for PY: (a) encoding against maintenance within
3610	each trial type; (b) preferred against nonpreferred within each epoch.
3611	##### CELL 130 [code]
3612	def cv2_cell(n, loads, pref_flag, epoch, within=False):
3613	    t = T[NT["sub"].iat[n]]
3614	    t = t[t.load.isin(loads)]
3615	    pm = pref_mask(t, PREF[n], 1) if loads == [1] else ((t.img1 == PREF[n]) | ((t.load >= 2) & (t.img2 == PREF[n])) | ((t.load == 3) & (t.img3 == PREF[n]))).values
3616	    t = t[pm if pref_flag else ~pm]
3617	    on, win = (t.enc1.values, 1.0) if epoch == "enc" else (t.maint.values, 2.5)
3618	    sp = wm.epoch_spikes(SPK[n], on, on + win, win)
3619	    if within:
[... 533 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 672,900p kussovska-2025.yaml
```

```
- id: fig4c-encoding-bursts-vs-poisson
  statement: During encoding, population bursting did not exceed a rate-matched Poisson null for
    most neuronal groups; it differed from the null only for all neurons and for the low mean ACG
    amplitude group.
  source: Results, Bursting dynamics reorganize spiking activity between encoding and
    maintenance, paragraph 2; Figure 4c
  quote: During encoding, population bursting did not exceed a rate-matched Poisson null
    (Wilcoxon signed-rank; Fig. 4c) for most neuronal groups. Significant effects were detected
    for all neurons (W = 9.0, P = 0.003) and for the group with low mean ACG amplitude (W = 0.0,
    P = 0.012).
  statistics:
  - about: all neurons
    test: Wilcoxon signed-rank
    statistic: W = 9.0
    p: 0.003
    corrected: FDR
  - about: low mean ACG amplitude
    test: Wilcoxon signed-rank
    statistic: W = 0.0
    p: 0.012
[... 209 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1052,1200p kussovska-2025.yaml
```

```
- id: fig6ab-celltype-bursts-vs-null
  statement: Pyramidal populations showed elevated bursting over a null in both encoding and
    maintenance, whereas interneurons showed elevated bursting during maintenance but not during
    encoding.
  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons
    and pyramidal neurons, paragraph 2; Figure 6a,b and legend
  quote: >-
    Across participants, pyramidal populations showed elevated bursting during both encoding and
    maintenance relative to chance (label-shuffled null; Encoding: W = 1.0, P = 0.012;
    Maintenance: W = 0.0, P = 0.004; Fig. 6a–b). By contrast, interneurons exhibited elevated
    population bursting during maintenance (W = 5.0, P = 0.001) but not during encoding (W =
    41.0, P > 0.05)
  statistics:
  - about: PY, encoding
    test: Wilcoxon signed-rank
    statistic: W = 1.0
    p: 0.012
  - about: PY, maintenance
    test: Wilcoxon signed-rank
    statistic: W = 0.0
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def glm_fit" -A40 wm.py | head -60; grep -n "def pmap" -A15 wm.py
```

```
197:def glm_fit(counts_by_neuron, x_by_neuron, perms_by_neuron):
198-    """Real and permutation-null slopes for each neuron (Methods, Generalized linear model encoding
199-    analysis; main_1e,f.py:150-170). counts_by_neuron and x_by_neuron are per-neuron arrays;
200-    perms_by_neuron gives for each neuron an index array (n_perm x n_trials) that permutes its
201-    predictor. The predictor is z-scored before fitting (main_1e,f.py:128)."""
202-    n = len(counts_by_neuron)
203-    real, null = np.empty(n), None
204-    for j in range(n):
205-        x = np.asarray(x_by_neuron[j], float)
206-        xz = (x - x.mean()) / (x.std() + 1e-12)
207-        real[j] = poisson_slopes(counts_by_neuron[j], xz[None, :])[0]
208-        nb = poisson_slopes(counts_by_neuron[j], xz[perms_by_neuron[j]])
209-        if null is None:
210-            null = np.empty((n, len(nb)))
211-        null[j] = nb
212-    return real, null
213-
214-
215-def glm_groups(real, null, groups, alpha=0.05):
216-    """A neuron is significant when |b1| is at or above the 95th percentile ('higher' quantile) of
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "140 ms\|70 ms\|90th\|prominence" *.txt | head -20; grep -n -i "label-shuffled\|protect" *.txt | head
```

```
346:To characterize the evolving code, we quantified population bursts following recent primate and rodent studies [46, 53, 54]. A burst was defined as a transient increase in population activity within a 70-ms bin exceeding a 90th-percentile prominence threshold. To avoid averaging across trials and participants, spikes were concatenated per patient, binned and Gaussian-smoothed (σ = 40 ms), and burst candidates within 70 ms of a previous event were suppressed to prevent fragmentation of single events [58]. Parameters were selected by a small grid search (Extended Data Fig. 3a) and are consistent with reports that bursts typically span 50–100 ms [69]. Significance was assessed against a Poisson null model (100 surrogate iterations; see Methods) to determine whether observed bursts reflected meaningful neural dynamics rather than random fluctuations (Fig. 4a). Analyses were performed separately for encoding and maintenance to test whether temporal firing patterns differ across epochs. To examine how intrinsic firing properties shape these dynamics, we repeated all analyses in neuron groups stratified by mean autocorrelogram (ACG) amplitude (low vs. high) and ACG decay time constant (τdecay; short vs. long; Fig. 4b). We used a balanced design in which every participant contributed the same number of neurons for each analysis condition.
478:We identified transient bursts of spiking activity using a procedure adapted from [58]. All analyses were performed within participant (i.e., no pseudo-populations). For each neuron, spike times were concatenated across all trials within a given memory load to obtain a continuous spike train for that load. Separate spike-time series were extracted for the encoding and maintenance periods, allowing burst activity to be analyzed independently in each task period. Burst detection depended on two parameters: the spike-count bin width and the Gaussian kernel width used to smooth the instantaneous rate. To constrain detection to biologic
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "third" kussovska-2025.yaml | head; grep -n -i "M1\b.*M2\|1 s windows\|1-s\|three 1" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('kussovska-2025-01.yaml'))
from collections import Counter
print(len(d['outcomes']),Counter(o['outcome'] for o in d['outcomes']))
print([o['claim'] for o in d['outcomes'] if o.get('assumed')])
print(len([o for o in d['outcomes'] if o.get('assumed')]))
r=d['verifications'][0]['results'];print(len(r), Counter(x['agrees'] for x in r))
"
```

```
45 Counter({'reproduced': 31, 'not_reproduced': 7, 'partially_reproduced': 7})
['fig4c-encoding-bursts-vs-poisson', 'fig4d-maintenance-bursts-vs-poisson', 'fig4-acg-group-differences', 'fig4f-all-cells-epochs', 'fig4hj-group-epochs', 'ext2-bursts-loads23', 'fig6ab-celltype-bursts-vs-null', 'fig6cd-celltype-epochs', 'ext5bd-in-load-dependence', 'fig6e-load-modulation-in', 'fig6f-rt-modulation-in-concept', 'fig6gh-in-concept-cv2', 'ext5gh-py-decay-preferred', 'fig6i-py-bin-width-decoding', 'fig6j-in-bin-width-decoding', 'fig6kl-cross-temporal-by-type', 'ext5ij-load2-decoding-by-type']
17
45 Counter({True: 41, False: 4})
```

**Agent**

**Verifier report, round 2: Kussovska et al. 2025 on DANDI:000469 (0.231213.2047)**

The claims file has 45 claims and the attempt record has 45 outcomes: 31 reproduced, 7 partially reproduced, 7 not reproduced. Seventeen outcomes are marked `assumed: true`. I checked the re-executed main notebook (149 cells), the new dPCA notebook (`dpca_kussovska_2025.ipynb`, 18 cells), `wm.py`, the README and the record.

### 1. Outcomes and assumptions

**The 39 outcomes left as they were after round 1: I agree with all of them.** That includes fig6cd, now not reproduced as I said in round 1. The printed values in the re-run support each one; caveats on fig4c and fig6e are in section 3.

**The three dPCA claims, now tested: I agree with all three.**
- **fig3abc, reproduced.** Maintenance medians are higher than encoding under both measures and both trial readings (dpca cell 12). Most of the gap comes from the longer maintenance window: over the first 499 bins it is tortuosity 2.46–2.57 against 2.16, and 9 reversals against 8. The record says so. The rank-sum p values treat the 500 values as independent, which they are not, but the criterion uses only medians.
- **fig3d, reproduced, but only under reading (b).** That reading is the code's own trial-selection bug, which the record reports as a finding (dpca cell 9):
  - Reading (b): H = 457.62; maintenance in its own space against maintenance projected onto encoding, p = 0.077.
  - Reading (a), the same trials in both epochs: those two maintenance conditions differ (p = 0.019).
  - The criterion names (b) as a reading, so the outcome stands. It is the code's result, not one independent of it.
- **fig3h, reproduced** with `protect=[]` for the early half (H = 410 and 413; dpca cell 15). Under the code's own setting the early half separates less than the late half in all 100 splits. That setting gives H = 394 and 380, also inside the tolerance, but in the wrong direction. The record states this.

**fig4c, reproduced: I agree only by the letter of the criterion.** It now passes only under `methods/height/d1/real` (cells 90–91). The criterion calls the 1-bin spacing a variant and the 2-bin spacing the main reading.
- With 2 bins, low ACG has BH p = 0.0601, so it fails.
- In round 1 the same reading passed with 2 bins (BH p 0.038 / 0.048). One run-to-run change in the ACG fit moved it across 0.05.
- Under the main spacing the best result meets the criterion's partial condition: `code/prominence/d2` gives all neurons and low ACG, plus concept cells (BH p 0.045).
- I would record this as weak. The record's own wording ("rests on one named reading") understates that it is the 1-bin variant.

**fig4d, reproduced: I agree.** It now uses the criterion's own-maintenance reading, and the control in cell 95 justifies that choice. Under that reading, `methods/prominence` gives the pattern with all three threshold settings, and concept cells have BH p 0.09–0.35.

**fig6e, reproduced: I agree by the letter of the criterion, but the result is fragile.** IN concept cells are 3 of 15 = 20.00% with p = 0.038 (cell 124). This rests on:
- the reading (a) cell types, whose PY count (102) is outside the fig5c tolerance;
- a fit that kept one more neuron in round 1, giving 16 IN concept cells and 18.75%.

With the reading (b) types, which have the paper's 14 IN concept cells, the matched-trial result is 14.29% with p = 0.15. Partially reproduced would describe the evidence better. The notes do disclose all of this.

**The assumptions are both stated and reasonable.**
- *Reading (a) cell types (all spikes).* This is justified by the shipped table, which matches on firing rate, ISI CV, mean ACG and burst index. Every cell-type claim is also run with the (b) types.
- *Own-maintenance window for fig4d and fig6ab.* This is justified by the burst-free Poisson control.
- *One gap:* the τdecay groups come from a scipy fit that agrees with the shipped MATLAB τdecay for only 11% of neurons (cell 75). The record states this as a limitation but never compares its groups with groups built from the shipped `Decay` column (see section 3).

**The claims file misses one paper statement.** The Fig. 6c legend defines M1–M3 as "the first, second, and final thirds of the maintenance epoch". The fig4f and fig6cd criteria cite only the Methods' 1 s windows and the code's thirds of the whole train. Per-trial thirds of maintenance are a third reading that was not run.

### 2. Text against printed outputs

**Wrong against the printed numbers:**
- **Cell 35 (fig1e):** "preSMA (20.40%, p = 0.000), vmPFC (18.75%, p = 0.009) and dACC (10.53%, p = 0.025) … the within-participant permutation gives 19.20%, 18.75% and 9.94%". Cell 34 prints preSMA 20.000% (50 of 250), vmPFC p 0.007, dACC p 0.026, and within-participant preSMA 18.800%.
  - The record's fig1e notes repeat the same stale values, and `measured` lists 20.4.
  - These are the round-1 run's numbers. The outcome is unchanged, since 20.0 and 18.8 are both inside 17.64–21.56.
- **Cell 41:** "seed 0 gives the paper's regional shares exactly". The notebook prints HPC 18.97% and vmPFC 5.17%; the paper gives 18.96% and 5.15%. "Exactly" is too strong.
- **Cell 53:** "The shuffled maps had no supra-threshold cluster" sits next to "Only 3 of the 1,000 shuffled maps have a significant pair". Those three pairs are clusters of extent 1. It is the 95th percentile of extents that is 0.
- **Record finding (peak-rule question):** "Fig. 4c is reproduced under the Methods' height rule with the Methods' groups". It holds only with the 1-bin spacing, not the Methods' 140 ms (cell 90).
- **Record `acg-fit-yield` notes and finding:** "317 in an earlier run of the same code, so one unit lies at the threshold". The fig1e GLM also changed between runs (51 → 50 significant preSMA neurons), and it does not use the ACG fit. So the change is not explained by one neuron at the R2 threshold (see section 3).

**Everything else checks out.** Every other "**Result:" sentence in both notebooks, both Summary sections, the README table and the record's notes matches the printed outputs. The README's category counts add up to 45, and its run times (about 45 and 22 min) match the printed 45.9 and 21.6 min.

**Round-1 reasons.** The record states them faithfully, largely in my words, including problems 1, 3–9, 11 and 12, each attached to the claims they bear on. Two are missing from every `reason`:
- **Problem 2** (types (a) used downstream; claims never run with the (b) types). It appears only in the author's responses.
- **Problem 10** (the 0 s subject-9 trial).

### 3. Round-1 points

**Resolved:**
- **1** (dPCA): computed in the new notebook.
- **2** (types (b) downstream): run for every cell-type claim, plus PY_b and IN_b burst groups.
- **3** (2.8 s window): confirmed by the burst-free control. The own-maintenance reading is now run under every reading and recorded as a finding.
- **4** (M3 rates per second): now given for every group.
- **5** (ACG fit): stated as a limitation.
- **6** (cluster rule): extents and shuffled-map counts are printed.
- **7** (chance level): binomial tests against 20% added.
- **9** (trial-draw spread): stated.
- **10** (subject-9 trial): checked and recorded as a finding.
- **11** (no single burst reading): stated.
- **12** (cross-trial intervals): within-trial CV2 variant added; spike counts stated for ext5gh.

**Accepted with no change:** 8 (the downstream concept set is a single seed). It does not affect a conclusion.

**What remains that bears on a conclusion:**
1. **Results change between runs and this is not explained.** Seeds are fixed, yet:
   - ACG yield went 317 → 316;
   - fig1e preSMA went 51 → 50 significant neurons (a GLM result independent of the ACG fit);
   - fig4c low ACG at 2-bin spacing went 0.048 → 0.060;
   - fig6e IN concept went 18.75% → 20.00%.

   Both the fig4c and the fig6e outcomes sit on this instability. A likely cause is the GLM's `|b1| ≥` 95th-percentile-of-null rule, which can flip on floating-point ties. Two repeat runs and a stability check would settle it.
2. **fig4c rests on the 1-bin spacing variant.** Under the main 2-bin spacing the best result is partial.
3. **fig6e rests on the reading (a) types and fails with the paper-matching (b) types.** Partially reproduced would describe it better.
4. **The τdecay groups were never checked against groups built from the shipped `Decay` column** (11% agreement within 1%). This bears on short vs long τdecay in fig4-acg-group-differences, on fig4hj, and on the decay groups in fig4c, fig4d and ext2.
5. **Fig. 4 still has no single peak rule supporting it as a whole.** fig4c needs the height rule (and 1-bin spacing), while fig4d, fig4-acg, fig4hj, ext2 and ext5bd need prominence. This is disclosed, not resolved.
6. **fig3d passes only with the code's mis-selected maintenance trials, and fig3h only with a protect setting the code does not use.** Both are disclosed; the outcomes are the code's result under one reading.

## End of run

22 turns, 4 minutes, $3.06 at API prices, result: success.
