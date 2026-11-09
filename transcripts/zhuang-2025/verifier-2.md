# 001177 · verifier-2 · run 40698843296

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 456
drwxr-xr-x 6 runner runner    4096 Oct 28 13:57 .
drwxr-xr-x 7 runner runner    4096 Oct 28 13:57 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 13:41 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 13:41 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 28 13:57 .claude
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .env
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .env.development
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .env.local
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .env.production
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .env.test
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .env.test.local
drwx------ 2 runner runner      40 Oct 28 13:57 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 13:41 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 13:41 .github
-rw-r--r-- 1 runner runner       0 Oct 28 13:57 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 13:41 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 13:41 .mcp.json
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 001177-zhuang-2025-01.yaml
```

```
<persisted-output>
Output too large (78.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/d44718bf-7e64-43a7-976f-2854d5cabb7b/tool-results/bklhdttq8.txt

Preview (first 2KB):
# Zhuang, Lemak, Sridhar & Nelson (2025) from DANDI:001177 and its Zenodo deposit

Tests the findings of [Zhuang et al. (2025)](https://doi.org/10.1093/brain/awaf312) on
[DANDI:001177](https://dandiarchive.org/dandiset/001177/0.250902.2127), which holds the striatal
recordings of Figures 4, 6 and S5 and S8, and on the paper's
[Zenodo deposit](https://doi.org/10.5281/zenodo.15258978), which holds its behaviour, histology,
rotarod and slice data.

The dandiset holds raw voltage, LFP and per-electrode threshold crossings for the paper's 18 mice,
but no sorted units, unit classes, optical labels, laser times or injection times, so the 14
electrophysiology claims are blocked. Of the 30 claims on the Zenodo data, 28 are tested, each
operant session recounted from its raw log.

| Claims | Outcome |
|---|---|
| Delayed/large choices at baseline, under PPX and A77636, and over repeated dosing (9 claims) | 9 reproduced |
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo ----; head -c 40000 001177-zhuang-2025-01.yaml
```

```
<persisted-output>
Output too large (41.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/d44718bf-7e64-43a7-976f-2854d5cabb7b/tool-results/bi8kkh5rg.txt

Preview (first 2KB):
# Zhuang, Lemak, Sridhar & Nelson (2025) from DANDI:001177 and its Zenodo deposit

Tests the findings of [Zhuang et al. (2025)](https://doi.org/10.1093/brain/awaf312) on
[DANDI:001177](https://dandiarchive.org/dandiset/001177/0.250902.2127), which holds the striatal
recordings of Figures 4, 6 and S5 and S8, and on the paper's
[Zenodo deposit](https://doi.org/10.5281/zenodo.15258978), which holds its behaviour, histology,
rotarod and slice data.

The dandiset holds raw voltage, LFP and per-electrode threshold crossings for the paper's 18 mice,
but no sorted units, unit classes, optical labels, laser times or injection times, so the 14
electrophysiology claims are blocked. Of the 30 claims on the Zenodo data, 28 are tested, each
operant session recounted from its raw log.

| Claims | Outcome |
|---|---|
| Delayed/large choices at baseline, under PPX and A77636, and over repeated dosing (9 claims) | 9 reproduced |
[... 16 more lines not kept]
```

**Agent**

Let me read the files directly.

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Zhuang, Lemak, Sridhar & Nelson (2025) from DANDI:001177 and its Zenodo deposit
2	
3	Tests the findings of [Zhuang et al. (2025)](https://doi.org/10.1093/brain/awaf312) on
4	[DANDI:001177](https://dandiarchive.org/dandiset/001177/0.250902.2127), which holds the striatal
5	recordings of Figures 4, 6 and S5 and S8, and on the paper's
6	[Zenodo deposit](https://doi.org/10.5281/zenodo.15258978), which holds its behaviour, histology,
7	rotarod and slice data.
8	
9	The dandiset holds raw voltage, LFP and per-electrode threshold crossings for the paper's 18 mice,
10	but no sorted units, unit classes, optical labels, laser times or injection times, so the 14
11	electrophysiology claims are blocked. Of the 30 claims on the Zenodo data, 28 are tested, each
12	operant session recounted from its raw log.
13	
14	| Claims | Outcome |
15	|---|---|
16	| Delayed/large choices at baseline, under PPX and A77636, and over repeated dosing (9 claims) | 9 reproduced |
17	| Washout, omissions and choice latencies (4 claims) | 1 reproduced, 3 partially reproduced (PPX washout rests on how the Bonferroni comparisons are made) |
18	| Hyperbolic fit parameters A, K and AUC (PPX, A77636, DREADD) | 1 reproduced, 1 partially reproduced, 1 not reproduced |
19	| DREADD delay discounting (mCherry, hM4Di, hM3Dq) | 1 reproduced, 1 partially reproduced |
20	| Rotarod, SNc cell counts, slice validation | 3 reproduced |
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "001177-zhuang-2025-01.yaml"
}
```

```
1	schema_version: 2
2	id: 001177-zhuang-2025-01
3	dataset:
4	  archive: dandi
5	  id: '001177'
6	  version: 0.250902.2127
7	  doi: 10.48324/dandi.001177/0.250902.2127
8	paper: doi:10.1093/brain/awaf312
9	date: '2026-10-28'
10	entry: 001177-zhuang-2025
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
[... 716 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "001177-zhuang-2025-01.yaml",
 "offset": 737
}
```

```
737	      both (p < 0.001), but the losses are 64.3% and 56.8%, outside 50 +/- 5. With all-controls normalisation
738	      DMS is 52.4% but DLS is 60.5% and DMS vs VS gives p = 0.052. Cell 43 has 45 parkinsonian mice where the
739	      paper has 44, and cohorts 3 and 4 have a single control each for the per-cohort normalisation (does not
740	      affect a conclusion).
741	    response: No change of outcome. The notebook now prints the cohorts with one control and the result without
742	      them (losses 65.7% and 58.1%, pattern holds), and says no mouse has sections in two cohorts, so the extra
743	      mouse cannot be identified.
744	  - claim: figs1d-snc-cells
745	    agrees: true
746	    outcome: reproduced
747	    reason: Control median 316, parkinsonian 187 cells/mm2, Mann-Whitney p = 0.00026 (n = 9 and 20). It stays
748	      below 0.002 whichever group the 3 unlinked mice are put in.
749	    response: No change of outcome.
750	  - claim: fig1c-rotarod
751	    agrees: true
752	    outcome: reproduced
753	    reason: Dunn control vs parkinsonian baseline p = 1e-15, baseline vs PPX p = 1.8e-5, baseline vs saline
754	      p = 0.83. Cell 47 uses 40 controls where the paper has 31 and applies Dunn's correction over 3 chosen
755	      pairs; neither is commented on, and the conclusions survive correction over all 10 pairs (does not affect
756	      a conclusion).
[... 341 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_zhuang_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain']))
            else: print('--OUT-- [',list(d),']')
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -n "######## CELL" $TMPDIR/nb.txt | head -100
```

```
2216 /tmp/claude-1001/nb.txt
2:######## CELL 0 [markdown]
34:######## CELL 1 [code]
53:######## CELL 2 [markdown]
60:######## CELL 3 [code]
134:######## CELL 4 [code]
165:######## CELL 5 [code]
178:######## CELL 6 [markdown]
195:######## CELL 7 [code]
285:######## CELL 8 [code]
318:######## CELL 9 [code]
347:######## CELL 10 [markdown]
357:######## CELL 11 [markdown]
362:######## CELL 12 [code]
411:######## CELL 13 [code]
467:######## CELL 14 [markdown]
473:######## CELL 15 [markdown]
482:######## CELL 16 [markdown]
493:######## CELL 17 [code]
542:######## CELL 18 [markdown]
[... 76 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 1100
}
```

```
File content (36341 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
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
2	######## CELL 0 [markdown]
3	# Zhuang, Lemak, Sridhar & Nelson (2025): what DANDI:001177 and the paper's Zenodo deposit support
4	
5	Paper: Zhuang X, Lemak J, Sridhar S, Nelson AB. "Aberrant striatal firing mediates impulsive
6	decision-making in a mouse model of Parkinson's disease." Brain (2025), doi:10.1093/brain/awaf312.
7	The claims file (`claims/001177/10.1093-brain-awaf312.yaml`) was written from the version of record
8	(Europe PMC full text, PMC12597312) with its supplement, and checked by a second reader.
9	
10	Data.
11	
12	- DANDI:001177, version 0.250902.2127, streamed. The paper cites the dandiset without a version
13	  ("Raw in vivo electrophysiology datasets have been deposited in DANDI
14	  (https://dandiarchive.org/dandiset/001177)"). This is the only published version; the draft was
15	  modified later (2026-09-03) with the same 56 assets and total size, so the published version is
16	  pinned, as the protocol asks when the paper names none. The dandiset holds the in vivo
17	  electrophysiology of Figures 4, 6F-K, S5 and S8.
18	- Zenodo record 15258978 (doi:10.5281/zenodo.15258978), the paper's deposit of its behaviour,
19	  histology, rotarod and slice data, which the claims file names for every `data: elsewhere`
20	  claim. It has one version. Its files are streamed into memory.
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 560
}
```

```
700	reading all: delay F(3, 178) = 38.15, p = 4.33e-19; control 91.7 -> 32.1 %, parkinsonian 85.7 -> 32.9 % (0 s -> 9 s)
701	reading stable: delay F(3, 40) = 2.14, p = 0.11; control 95.4 -> 82.4 %, parkinsonian 95.7 -> 58.8 % (0 s -> 9 s)
702	
703	--OUT--
704	<Figure size 400x300 with 1 Axes>
705	
706	######## CELL 24 [markdown]
707	**Result: reproduced.** Under reading (a) the delay effect is F(3, 178) = 38.15, p = 4e-19 (paper
708	F(3, 180) = 38.53), and the choice of the delayed/large reward falls from 91.7 to 32.1% in control
709	and from 85.7 to 32.9% in parkinsonian mice between 0 and 9 s. Under reading (b) the means also
710	fall (95.4 to 82.4%, 95.7 to 58.8%) but the delay effect is not significant (p = 0.11) in 12 mice,
711	which are the mice that discount least (above), so reading (b) does not bear on the claim.
712	
713	######## CELL 25 [markdown]
714	## fig1f-ctrl-ppx-no-change and fig1g-park-ppx-fewer-large
715	
716	> PPX did not change delay discounting in healthy control mice.
717	> In parkinsonian mice PPX reduced the likelihood of choosing the delayed/large reward at every delay.
718	
719	Split-plot ANOVA (unit = mouse x delay, see `icd.py`) of baseline against PPX ON, Bonferroni per
[... 540 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1259,
 "limit": 500
}
```

```
1259	
1260	######## CELL 54 [markdown]
1261	**Result: reproduced.** In the 14 mCherry mice with delay discounting files, CNO has no
1262	effect (F(1, 52) = 0.94, p = 0.34; paper F(1, 56) = 0.97, p = 0.33) and no per-delay comparison
1263	differs (all Bonferroni p = 1). The README lists 15 mCherry mice; R5.5 has no delay discounting
1264	file in the deposit.
1265	
1266	######## CELL 55 [code]
1267	for g in ["hM4Di", "hM3Dq"]:
1268	    for rb in ["all", "stable"]:
1269	        show(drug_test("DREADD", g, rb, "four"), f"{g}, baseline {rb}, CNO four")
1270	--OUT--
1271	hM4Di, baseline all, CNO four: mice 12, units 48, treatment F(1, 44) = 12.772, p = 0.000868; delay F(3, 44) = 7.67, p = 0.000315; interaction p = 0.594
1272	--OUT--
1273	
1274	 delay level  n  mean_baseline  mean_level     diff  p_bonf_pooled  p_bonf_paired
1275	     0    on 12        86.8084     82.5599  -4.2485         1.0000         0.8134
1276	     3    on 12        76.8779     65.3194 -11.5586         0.0220         0.1593
1277	     6    on 12        58.8832     52.1164  -6.7668         0.3777         0.2672
1278	     9    on 12        45.0875     39.3677  -5.7197         0.6223         0.7787
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1758
}
```

```
1758	to 6 (p = 0.0005 to 0.012). In random learning they are similar in sessions 2 to 6, but session 1
1759	success differs (65.9 against 86.9%, p = 0.003), against the criterion's "no session of random
1760	learning differs". Initiation latency differs in no random session.
1761	The columns read are those headed "% of TOTAL successful trials" and "TOTAL Latency to Trigger (s)"
1762	(blocked) and "% of succesful trials" and "CenterTriggerLatency (s)" (random), printed above.
1763	
1764	######## CELL 79 [markdown]
1765	## Correlations with striatal TH: fig3a-a-correlates-dms, fig3b-k-no-correlation, figs4-a77636-no-correlation
1766	
1767	A and K on the drug (four ON sessions) of each parkinsonian mouse against its normalized TH
1768	(per-cohort reading of fig1b-th-loss), Pearson correlation.
1769	
1770	######## CELL 80 [code]
1771	def corr_block(exp, label):
1772	    out = {}
1773	    for ron in ["four", "first"]:
1774	        on = params(per_mouse(exp, "parkinsonian", "on", ron))
1775	        P0 = th["per cohort"]
1776	        if ron == "four":
1777	            print(f"{label}: {len(on)} mice with a fit on the drug, {len(P0)} parkinsonian mice with TH; "
[... 440 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  - id:\|id: " 10.1093-brain-awaf312.yaml | head -60; grep -c "data: dataset\|data: elsewhere" 10.1093-brain-awaf312.yaml; grep -n "data:" 10.1093-brain-awaf312.yaml | sort | uniq -c | head; grep -o "data: [a-z]*" 10.1093-brain-awaf312.yaml | sort | uniq -c
```

```
82:  id: "001177"
85:- id: fig1b-th-loss
119:- id: figs1d-snc-cells
136:- id: fig1c-rotarod
164:- id: figs1ef-ppx-locomotion
190:- id: figs1-instrumental-learning
222:- id: fig1fg-baseline-similar
242:- id: fig1fg-delay-discounting
261:- id: fig1f-ctrl-ppx-no-change
281:- id: fig1g-park-ppx-fewer-large
316:- id: fig1ijk-ppx-a-k-auc
352:- id: figs2abc-sex-similar
368:- id: figs2de-omissions-low
399:- id: figs2gh-ppx-latency
428:- id: figs2ijk-ppx-washout
474:- id: fig2bc-a77636-locomotion
494:- id: fig2d-ctrl-a77636-no-change
508:- id: fig2e-park-a77636-fewer-large
539:- id: fig2fgh-a77636-k-auc
564:- id: figs3-a77636-washout-latency
[... 38 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1093-brain-awaf312.yaml",
 "limit": 680
}
```

```
1	# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
4	# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
5	# was added by the check of 2026-10-28.
6	#
7	# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
8	# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
9	# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
10	# statistics"). Figure panels of the main paper were not available as images; values in the main
11	# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
12	# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
13	#
14	# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
15	# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
16	# block of the delay discounting task (delay_discounting_task.py, phase2.py, phase3.py) and
17	# Summary_Cognitive.m, which averages each mouse's sessions within a condition, fits
18	# V = A/(1 + K*D) to the four delays with lsqcurvefit (start A = 1, K = 0.5, no bounds) and takes
19	# the AUC as the trapezoidal integral of the fitted values at D = 0, 3, 6, 9 s; (2)
20	# UCSF-Nelson-Lab/ICD-Cognitive-Arduino, tag ICD, commit f7cff8b (Zenodo doi:10.5281/zenodo.10703131),
[... 660 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1093-brain-awaf312.yaml",
 "offset": 905,
 "limit": 215
}
```

```
905	    value: 2
906	    unit: units
907	  criterion: Saline sessions (4 mice, 40 putative MSNs) classified as in the opening comment.
908	    Reproduced when at least 90% of units are 'no change' and the 'no change' count is within
909	    tolerance. The increase and decrease counts are reported without a tolerance (one or two units).
910	  data: dataset
911	- id: figs6-dreadd-validation
912	  statement: In slices CNO reduced optically evoked IPSCs from hM4Di-expressing iMSNs and increased
913	    the firing of hM3Dq-expressing dMSNs.
914	  source: Results, Chemogenetic manipulations of striatal neurons mimic the effect of pramipexole in
915	    parkinsonian mice, paragraph 1; Figure S6
916	  quote: Application of the DREADD agonist, clozapine-N-oxide (CNO), reduced oIPSC amplitude ...
917	    Application of CNO triggered a significant increase in firing rate
918	  statistics:
919	  - about: oIPSC amplitude
920	    test: Wilcoxon signed-rank
921	    p: 0.01
922	    p_relation: "<"
923	    n: 2 mice, 6 cells
924	  - about: dMSN firing to 300 pA
[... 195 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def rm_oneway" -A 40 icd.py; grep -n "def friedman_dunn" -A 30 icd.py; grep -n "def tracking_gaps" -A 20 icd.py
```

```
484:def rm_oneway(table: pd.DataFrame, reference: str) -> dict:
485-    """Repeated measures one-way ANOVA over the columns of `table` (complete rows), with
486-    Bonferroni-corrected paired t tests between every pair of columns (Table 1's reading), and as
487-    a variant Bonferroni comparisons on the ANOVA's pooled residual error, as GraphPad Prism makes
488-    them by default (`pairs_pooled`)."""
489-    t = table.dropna()
490-    y = t.to_numpy(float)
491-    n, k = y.shape
492-    grand = y.mean()
493-    ss_c = n * np.sum((y.mean(axis=0) - grand) ** 2)
494-    ss_s = k * np.sum((y.mean(axis=1) - grand) ** 2)
495-    ss_e = np.sum((y - grand) ** 2) - ss_c - ss_s
496-    df_c, df_e = k - 1, (k - 1) * (n - 1)
497-    F = (ss_c / df_c) / (ss_e / df_e)
498-    cols = list(t.columns)
499-    pairs = [(a, b) for i, a in enumerate(cols) for b in cols[i + 1:]]
500-    comps = {f"{a} vs {b}": min(1.0, stats.ttest_rel(t[a], t[b]).pvalue * len(pairs)) for a, b in pairs}
501-    se = np.sqrt(2 * (ss_e / df_e) / n)
502-    pooled = {f"{a} vs {b}": min(1.0, 2 * stats.t.sf(abs(t[b].mean() - t[a].mean()) / se, df_e) * len(pairs))
503-              for a, b in pairs}
[... 73 more lines not kept]
```

**Agent**

# Round 2 verification: Zhuang et al. 2025 (attempt 001177-zhuang-2025-01)

## 1. Outcomes

The claims file has 44 claims: 14 on the dataset and 30 elsewhere. The attempt record gives 18 reproduced, 8 partially reproduced, 2 not reproduced and 16 blocked (14 `data_missing`, 1 `metadata_insufficient`, 1 `other`). It tests 28 claims.

I agree with 43 of the 44 outcomes, including the fig5jl change to not_reproduced, which was my round-1 point. The one I disagree with is figs2ijk-ppx-washout.

Three outcomes rest on an assumption (`assumed: true`):

- **fig2bc-a77636-locomotion (injection at 20 min):** stated and reasonable. 25 of 26 files have a gap at 20.0–20.3 min (cell 90), and the Methods give a −20 to 0 min baseline.
- **fig5cf-cno-locomotion (same assumption):** stated and reasonable. The weak points are shown openly:
  - 12 files have no gap, and their per-minute velocity is printed (cell 92).
  - With only the files that have a gap, mCherry gives p = 0.16 or 0.22.
  - Only 3 hM4Di files have a gap, too few to test.
- **figs2ijk-ppx-washout (Bonferroni by paired t tests, not on the pooled error):** stated, but I do not think it is the better-supported choice.
  - The paper's printed p-values favour the pooled error. Baseline against OFF is K p = 0.01 and AUC p < 0.01. Pooled gives 0.028 and 0.0072; paired gives 0.063 and 0.039 (cells 32 and 35).
  - So pooled matches the paper's significance pattern in all six Table 1 and legend comparisons, and paired misses two.
  - Paired is closer only on ON against OFF AUC (0.0011 against 0.0019; pooled 0.0051), and both are significant there.
  - The record's case for paired rests only on Prism's guide. `icd.rm_oneway`'s own docstring (icd.py:487) says the pooled comparisons are "as GraphPad Prism makes them by default", and calls the paired tests "Table 1's reading" without support.
  - I would record reproduced, with the pooled error as the stated assumption. At least the record should give the evidence from the paper's p-values and resolve the docstring contradiction.

## 2. Text against printed outputs

I checked every Result conclusion, the Summary, the README and every outcome note. Except for the points below, every number matches the printed outputs.

- **"Every baseline session deposited (2 to 5 per mouse)"** (cell 94, and the record's `selection_undocumented` finding): cell 20 prints H2.1 with 1 baseline before its first drug session. The total number of baselines per mouse is never printed, so "2 to 5" is unsupported. The fig1fg notes correctly say "1 to 5" before the first drug session.
- **"No sorted units"** (README lines 9–10) and "the dandiset has no sorted, classified or optically identified units" (cell 0): cells 4 and 6 show two files with a units table that is "consistent with an unsorted and a sorted cluster per channel". The record's notes and the Summary ("no sorted units in 54 files, no unit labels in the other two") are accurate; the README and cell 0 overstate it.
- **"Twelve files (all 2023 H and J mice …)"** (cell 93) and "(the 2023 H and J mice …)" (fig5cf notes): H1 and J3 are also 2023 H and J files, and they have gaps at 17.7 and 18.5 min (cell 92).
  - The "with a gap at 19.5–21 min" subset counts 7 mCherry files, so H1 and J3 must have a second gap in that window.
  - The `gap_19_21` values are never printed. The count is printed but not checkable per file.
- **My round-1 reason for fig2bc** quotes p = 0.020 for the 10 listed parkinsonian mice, from my own recomputation. Cell 90 now prints p = 0.0137. My figure was off; the conclusion does not change.
- **My round-1 reasons are in the record in my own words.** Problem points 1–8 and 11 and the relevant part-C items are folded into the per-claim reasons. Two small things are left out, and neither affected a conclusion:
  - Problems 9 and 10 appear in no reason. Problem 10 is now answered by cell 8 and a finding.
  - The electrophysiology reasons drop my notes on the K4 "optoSession" file and on the draft version.

## 3. Round-1 points

**Resolved:**

- **Point 1:** both ON readings are run (first: r = 0.08). The unmatched IDs are listed: C3.1, E3.3, E4, H4.1, N1 and N5.1 have no histology; E6 has no PPX session; E3 and E3.2 are in no list.
- **Point 3:** all four ON/OFF pairs are run. The Dunn p for K is never below 0.19.
- **Points 5 to 9:** stated or tested.
- **Point 10:** cell 8 shows the shared files are training logs plus 18 and 14 baselines, with no drug or washout file.
- **Point 11:** recorded as a `paper_inconsistency` finding.
- **Every part-C item is now printed:** the log-event walk-through, the KRT and README sex search, the per-minute CNO velocity, the instrumental headers, the per-mouse stability CVs, and the `unit_name` values.

**Remaining, each bearing on a conclusion:**

- **figs2ijk-ppx-washout (point 4):** the pooled comparisons are now run, but the adopted paired choice is the weaker one (section 1). This decides partially reproduced against reproduced.
- **fig5cf-cno-locomotion (point 2):** resolved as far as the deposit allows and flagged as assumed. The significant mCherry slowing, which is what makes this partial, depends on the 5 mCherry files with no injection mark.
- **fig3a-a-correlates-dms:** 24 of the paper's 28 mice can be matched, and E3.3 against E3 or E3.2 cannot be settled from the deposit. Not reproduced stands under both ON readings and both normalisations. The missing 4 mice are the only route by which r could reach 0.46, which I think is unlikely.

On the claims file, I again found no misreading of the paper.

## End of run

17 turns, 3 minutes, result: success.
