# 000139 · verifier-2 · run 40774914482

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 508
drwxr-xr-x 6 runner runner    4096 Oct 28 21:57 .
drwxr-xr-x 7 runner runner    4096 Oct 28 21:57 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:47 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:47 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 28 21:56 .claude
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .env
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .env.development
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .env.local
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .env.production
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .env.test
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .env.test.local
drwx------ 2 runner runner      40 Oct 28 21:57 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:47 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:47 .github
-rw-r--r-- 1 runner runner       0 Oct 28 21:56 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:47 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 21:47 .mcp.json
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000139-churchland-2010-01.yaml
```

```
<persisted-output>
Output too large (44.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/292a47e9-3404-4771-ac00-8d9ea99716bc/tool-results/bk9eymixk.txt

Preview (first 2KB):
# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000139

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
be tested on [DANDI:000139](https://dandiarchive.org/dandiset/000139/0.220113.0408) (MC_Maze_Medium).
The dandiset holds one session of monkey J on the maze task, with two Utah arrays (152 units) and 250
labelled trials over 27 conditions, cut for the Neural Latents Benchmark. The paper's J-array dataset
had 108 conditions and about 2166 trials per neuron, so every measure here rests on far fewer trials.
The speed-task and single-electrode datasets and the EMG are not in the dandiset.

| Claim | Outcome |
|---|---|
| 146 units, 108 conditions in the J-array dataset | Partially reproduced |
| Mean preparatory vs peri-movement correlation 0.13 (J-array) | Partially reproduced |
| Correlations broad and unimodal | Reproduced |
| Correlation declines from 200 ms before onset to near zero | Reproduced |
| Population PSTHs show weak movement tuning by onset | Reproduced |
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/292a47e9-3404-4771-ac00-8d9ea99716bc/tool-results/bk9eymixk.txt"
}
```

```
1	# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000139
2	
3	Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
4	be tested on [DANDI:000139](https://dandiarchive.org/dandiset/000139/0.220113.0408) (MC_Maze_Medium).
5	The dandiset holds one session of monkey J on the maze task, with two Utah arrays (152 units) and 250
6	labelled trials over 27 conditions, cut for the Neural Latents Benchmark. The paper's J-array dataset
7	had 108 conditions and about 2166 trials per neuron, so every measure here rests on far fewer trials.
8	The speed-task and single-electrode datasets and the EMG are not in the dandiset.
9	
10	| Claim | Outcome |
11	|---|---|
12	| 146 units, 108 conditions in the J-array dataset | Partially reproduced |
13	| Mean preparatory vs peri-movement correlation 0.13 (J-array) | Partially reproduced |
14	| Correlations broad and unimodal | Reproduced |
15	| Correlation declines from 200 ms before onset to near zero | Reproduced |
16	| Population PSTHs show weak movement tuning by onset | Reproduced |
17	| Peri-movement space gives the best PD performance | Reproduced |
18	| Peri-movement space best at almost every dimensionality | Reproduced |
19	| Performance peaks at middle dimensionality | Reproduced |
20	| Segment directions and initial velocity perform reasonably well | Reproduced (segments equal in time) |
[... 675 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1016-j.neuron.2010.09.015.yaml
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/292a47e9-3404-4771-ac00-8d9ea99716bc/tool-results/bdym7dtqm.txt

Preview (first 2KB):
# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol as stated in docs/protocol.md (version pilot-12).
#
# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
# them. The paper links no code, so every method below comes from the Methods, the legends or the
# supplement.
#
# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/292a47e9-3404-4771-ac00-8d9ea99716bc/tool-results/bdym7dtqm.txt"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol as stated in docs/protocol.md (version pilot-12).
4	#
5	# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
6	# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
7	# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
8	# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
9	# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
10	# them. The paper links no code, so every method below comes from the Methods, the legends or the
11	# supplement.
12	#
13	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
14	# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
15	# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
16	# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
17	# trials with delays above 400 ms analysed. Four datasets. Monkeys A and B, speed task, 28
18	# conditions (7 directions, 2 distances, 2 instructed speeds), single electrodes, 64 and 74
19	# single units. Monkey J, maze task, single electrodes, 172 single units, recorded on four sets of
20	# 27 conditions each (about 53 neurons per set; population analyses done per set, then averaged).
[... 513 more lines not kept]
```

**Agent**

Now the notebook: extracting cell sources and printed outputs.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n===== CELL {i} [{c['cell_type']}] =====")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT ---'); print(''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']:
            print('--- OUT ---'); print(''.join(o['data']['text/plain']))
        elif o.get('output_type')=='error': print('--- ERR ---', o.get('ename'), o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -n "===== CELL" $TMPDIR/nb.txt | head -100
```

```
1926 /tmp/claude-1001/nb.txt
2:===== CELL 0 [markdown] =====
48:===== CELL 1 [code] =====
67:===== CELL 2 [markdown] =====
70:===== CELL 3 [code] =====
176:===== CELL 4 [markdown] =====
185:===== CELL 5 [code] =====
223:===== CELL 6 [markdown] =====
237:===== CELL 7 [code] =====
288:===== CELL 8 [markdown] =====
295:===== CELL 9 [code] =====
354:===== CELL 10 [markdown] =====
362:===== CELL 11 [code] =====
385:===== CELL 12 [markdown] =====
392:===== CELL 13 [code] =====
406:===== CELL 14 [markdown] =====
412:===== CELL 15 [code] =====
436:===== CELL 16 [markdown] =====
446:===== CELL 17 [markdown] =====
454:===== CELL 18 [code] =====
[... 61 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 620
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Churchland et al. (2010) on dandiset 000139 (MC_Maze_Medium)
4	
5	**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
6	activity: representation of movement or first cog in a dynamical machine? *Neuron* 68, 387-400.
7	doi:10.1016/j.neuron.2010.09.015.
8	
9	**Dataset.** DANDI:000139, "MC_Maze_Medium", version **0.220113.0408**, streamed from the archive.
10	This is the only published version of the dandiset (the other is the draft), so it is pinned; the
11	paper cites no version. The dandiset holds one session of monkey Jenkins (2009-09-29) on the maze
12	task, recorded with two Utah arrays, cut for the Neural Latents Benchmark into 250 training and
13	validation trials (with behaviour and trial labels) and 100 test trials (700 ms segments, no
14	condition labels, held-in units only).
15	
16	**Claims.** `claims/000139/10.1016-j.neuron.2010.09.015.yaml`, written from the NIH author manuscript
17	(PMC2991102) with its supplement, and checked by a second reader. Methods the claims file leaves
18	open are taken from the paper (cited where used) or, where the paper is silent, run under every
19	reading the claims file names. This version answers the first verification round: the outputs it
20	asked for are added in the sections they concern, each marked as added in response to the verifier.
[... 600 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 620,
 "limit": 520
}
```

```
620	    """prep (c, n), rate (c, n, T) -> per-neuron correlation at each time (n, T)."""
621	    a = prep - prep.mean(0)
622	    b = rate - rate.mean(0)
623	    num = (a[:, :, None] * b).sum(0)
624	    den = np.sqrt((a ** 2).sum(0))[:, None] * np.sqrt((b ** 2).sum(0))
625	    return num / den
626	
627	rt_med = int(np.median(tr.rt[d0["sel"]]))
628	def fig4e_traces(d, mask):
629	    idx = np.where(mask)[0]
630	    r0 = M.MOVE_WIN[0]
631	    mv_t = np.arange(-400, 101)
632	    mv_c = corr_trace(d["prep"][:, idx], d["mv_rate"][:, idx, mv_t[0] - r0: mv_t[-1] + 1 - r0])
633	    g0 = M.GO_WIN[0]
634	    go_t = np.arange(-200, 101)
635	    go_c = corr_trace(d["prep"][:, idx], d["go_rate"][:, idx, go_t[0] - g0: go_t[-1] + 1 - g0])
636	    # reading (a): go-locked part mapped to movement time with the median RT, then movement-locked
637	    go_tm = go_t - rt_med
638	    keep_mv = mv_t > go_tm[-1]
639	    sp_t = np.concatenate([go_tm, mv_t[keep_mv]])
[... 500 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1139,
 "limit": 450
}
```

```
1139	===== CELL 39 [code] =====
1140	TASK_SETS = {"pk, t": ["endpoints + max speed", "initial velocity", "endpoints + orth. excursion", "endpoints + viapoint",
1141	                       "endpoints + max velocity (pk)", "endpoints + halfpoint", "segment dirs (t)", "kitchen sink (t)"],
1142	             "ex, l": ["endpoints + max speed", "initial velocity", "endpoints + orth. excursion", "endpoints + viapoint",
1143	                       "endpoints + max velocity (ex)", "endpoints + halfpoint", "segment dirs (l)", "kitchen sink (l)"]}
1144	rows = []
1145	for R in "ab":
1146	    peri = F6["curves"][("peri", R)].mean(0)
1147	    for kw in "ab":
1148	        for rep in "ab":
1149	            kin = F6["curves"][(f"kinematic win {kw} rep {rep}", R)].mean(0)
1150	            for ts, names in TASK_SETS.items():
1151	                wins = [peri[i] > kin[i] for i in range(len(KS))]
1152	                wins += [peri[dims[nm] - 1] > F6["task"][nm].mean() for nm in names]
1153	                rows.append(dict(S=R, kin_window=kw, kin_rep=rep, task_variant=ts, comparisons=len(wins),
1154	                                 peri_wins=int(sum(wins)), fraction=round(np.mean(wins), 3)))
1155	f6e = pd.DataFrame(rows)
1156	print(f6e.to_string(index=False))
1157	print("Fraction range over readings:", f6e.fraction.min(), "to", f6e.fraction.max())
1158	--- OUT ---
[... 430 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1588,
 "limit": 340
}
```

```
1588	Location of the electrodes the units reference: {'electrode_group_PMd': 152} | prefix 1 rows 0 to 89 ; prefix 2 rows 14 to 94
1589	Nothing in the units or electrode tables ties id prefix 1 or 2 to PMd or M1.
1590	
1591	
1592	===== CELL 64 [markdown] =====
1593	### ap-location-no-effect-j-array
1594	
1595	> For the J-array dataset the correlation between preparatory and peri-movement tuning does not
1596	> depend on anterior-posterior location (r = 0.20, p = 0.27).
1597	
1598	===== CELL 65 [code] =====
1599	rows = []
1600	for r_ in SEL_READINGS:
1601	    d = condition_data(*r_)
1602	    idx, r, _ = corr_set(d, neuron_sets(d, "range")[1])
1603	    ap = (units.id_array.values[idx] == 1).astype(float)  # 1 = PMd (anterior)
1604	    if len(r) > 2 and 0 < ap.sum() < len(ap):
1605	        lr = stats.linregress(ap, r)
1606	        rows.append(dict(onset=r_[0], proto=r_[1], combine=r_[2], n=len(r), n_pmd=int(ap.sum()), r=round(lr.rvalue, 3),
1607	                         p=round(lr.pvalue, 4), mean_r_pmd=round(r[ap == 1].mean(), 3), mean_r_m1=round(r[ap == 0].mean(), 3)))
[... 320 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def perf_curves_pca\|def pd_performance_pca\|def prep_grams\|def grams_per_unit" -A30 maze.py | head -150
```

```
250:def pd_performance_pca(x, G, ks, recompute):
251-    """Leave-one-condition-out PD performance for one neuron in a PCA-based space.
252-    x (c,) preparatory rates; G (c x c) uncentered Gram matrix of the T-matrix (without
253-    the neuron). recompute: False = S from all conditions, only the regression leaves the
254-    condition out (reading a); True = PCA redone on the remaining conditions and the
255-    left-out condition projected onto its components (reading b). Returns perf per k."""
256-    c = len(x)
257-    kmax = max(ks)
258-    pred = np.zeros((len(ks), c))
259-    if not recompute:
260-        S = pca_scores(G, kmax)
261-    for l in range(c):
262-        train = np.delete(np.arange(c), l)
263-        if recompute:
264-            Gc, cross = _centered_parts(G, train, l)
265-            w, U = np.linalg.eigh(Gc)
266-            o = np.argsort(w)[::-1][:kmax]
267-            w, U = np.clip(w[o], 1e-12, None), U[:, o]
268-            S_train = U * np.sqrt(w)
269-            s_l = (cross @ U) / np.sqrt(w)
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^PREP\|^PERI\|^TMAT\|^GO_WIN\|^MOVE_WIN\|^STEP_MS\|^SIGMA" maze.py
```

```
59:GO_WIN = (-600, 500)      # stored go-locked bins
60:MOVE_WIN = (-600, 1000)   # stored move-locked bins
61:PREP = (-200, 100)        # relative to go cue
62:PERI = (-100, 350)        # relative to movement onset
63:TMAT = (-150, 800)        # peri-movement T-matrix, maze task
64:SIGMA_MS = 20
65:STEP_MS = 10
```

**Agent**

# Round 2 verification: Churchland et al. (2010) on DANDI:000139, version 0.220113.0408

Counts below come from the claims file and the attempt record: 23 claims, 23 outcomes. Cell numbers refer to the current notebook, which is renumbered since round 1.

## 1. Outcomes

| Claim | Outcome in the record | Agree? | Notes on the assumption |
|---|---|---|---|
| j-array-recordings | partially_reproduced | Yes, with a caveat | The criterion's "partial" needs the 27 conditions to be a subset of the paper's 108. The notes say this "cannot be shown", yet the outcome is not marked `assumed: true`. It should be. |
| fig4d-mean-correlation-j-array | partially_reproduced (assumed) | Yes | The tuning measure (range) and the proto-trial (condition mean, profiles concatenated) are stated and reasonable. The main reading passes on the t-test only (p = 0.042), and 3 of 8 selection readings fail (cell 18). |
| fig4abc-mean-correlation-other-datasets | blocked, data_missing | Yes | |
| fig4-broad-unimodal | reproduced (assumed) | Yes | Low power is stated. |
| fig4e-correlation-time-course | reproduced (assumed) | Yes, borderline | The splice assumption is stated, but its consequence is understated (§3). |
| suppfig1-population-psth-weak-movement-tuning | reproduced (assumed) | Yes, nominally | Criterion reading (a) holds in 16 of 16 rows. The cross-validated ranking breaks it for the claim's 17 neurons (ratio 1.115, cell 27). The record says so plainly. |
| fig6d-perimovement-best-j-array | reproduced (assumed) | Yes | Holds under all 8 combinations of the S, kinematic-window and replication readings. It is clearer on the 43 units whose tuning passes a permutation test (cell 36). |
| fig6-perimovement-best-each-dimensionality | reproduced (assumed) | Yes | 0.909 to 0.955 (cell 39). |
| fig6-dimensionality-peak | reproduced (assumed, S fixed) | **Yes. I am changing my round-1 position.** | The new chance curves show the recomputed-S reading cannot produce a decline: noise falls only 0.094 from k = 6 to 14, against 2.292 with S fixed (cell 42). The recomputed reading is therefore uninformative for this claim. S fixed is grounded in the Methods' wording, and with S fixed the best k is 2 to 6 in all 8 selection readings. |
| fig6-maze-task-spaces | reproduced (assumed, segments equal in time) | Yes, marginal | Segment directions score 0.008. That is above zero in only 2 of 8 selection readings (cell 45). The fragility is stated. |
| fig6abc-perimovement-best-other-datasets | blocked, data_missing | Yes | |
| fig6e-summary-rank | blocked, data_missing | Yes | |
| fig6-preparatory-dimensionality | not_reproduced | Yes | Under the criterion's plain count, 12 to 19 PCs. The cross-validated count of 7 (cell 54) points to noise as the cause, and the notes say so. |
| fig7a-shuffled-space-poor | reproduced (assumed) | Yes | |
| fig7b-window-start-slide | reproduced (assumed) | Yes | |
| ap-location-no-effect-j-array | reproduced (assumed) | Yes | The p-value does not depend on which array is labelled PMd. |
| ap-location-no-effect-other-datasets | blocked, data_missing | Yes | |
| fig7c-anterior-posterior-performance | not_reproduced (assumed) | Yes | Now run with the paper's upper limit. See the claims-file note under §3. |
| prep-activity-more-anterior | blocked, metadata_insufficient | Yes | |
| fig7d-pd-consistency | reproduced (assumed) | Yes | |
| some-neurons-better-elsewhere | reproduced (assumed) | Yes | |
| high-dimensional-task-spaces-underperform | reproduced (assumed) | Yes | |
| fig8-linear-dynamics-simulation | reproduced (assumed, full cycle) | Yes | The check is weak. |

## 2. Sentences the printed numbers do not support

- **Cell 37:** "Only 59 of 152 units pass the 5 spikes/s range with labels shuffled against 75 observed".
  - "Only" inverts the finding. The noise median of 59 is about 79% of the 75 observed (cell 11), so most of the passing count is matched by noise. The Summary and the record state the same numbers neutrally.
- **Cell 37:** "Every space is above its chance level at every dimensionality". The record's fig6d notes say the same.
  - Chance was computed only for the peri-movement space, kinematic window a with replication a, and the task spaces (cell 36). It was not computed for kinematic window b, replication b, or the upper limits.
- **Cell 72:** "The variant without the fitted neuron … gives upper limits at or below zero and ratios from -0.740 to 2.111". The record's fig7c notes say the same.
  - Only 2 of the 8 printed upper limits without the fitted neuron are at or below zero: −0.107 and −0.043. The others are 0.055 to 0.170 (cell 71). The ratio range is correct.
- **Cell 16:** "250 labelled trials per unit (350 with the unlabelled test segments)". The record's j-array notes say the same.
  - The test file holds only the 114 held-in units (cell 3). The 38 held-out units have 250 trials, not 350.
- **j-array-recordings notes** say the MC_Maze dandiset 000128 is a 2009-09-25 session with 182 units. Nothing in the notebook prints this. It is marked "not used for the outcome", which is acceptable, but no output supports it.
- **README** lists "Performance peaks at middle dimensionality", "Population PSTHs show weak movement tuning by onset" and the Figure 8 simulation as plain "Reproduced".
  - It drops what the Summary table keeps: "resting on S fixed", "reading (a) only; not under cross-validated ranking", and "full-cycle reading".
  - The README's list of open readings does not mention the Figure 8 gray interval.
- **Summary**, "best about 0.1 to 0.2": a small understatement. The recomputed-S best is 0.226 (cell 32).

Every other number in the conclusions, the Summary and the record notes matches the printed outputs. That includes the fig4d failing-reading p values (0.052, 0.056, 0.080), the 7 of 8 and 22 of 32 counts for fig4e, the threshold-table ranges, the fig7c values and SD, and the chance-curve falls.

**My round-1 reasons in the record.** They are faithful and in my words. My problems 1, 5, 8, 9, 10 and 11 have been folded into the per-claim reasons. Problem 5 is attached to both fig6d and the dimensionality peak, which is reasonable.

## 3. Round-1 points

**Resolved:**
1. The threshold noise. It is quantified (59 vs 75 units pass; 43 of the 76 units fitted in the PD analyses pass a permutation test), and a variant on the 43 tuned units was added.
2. The Figure 7C normalizer. The paper's upper limit is now the main reading.
3. The array labels, as far as the files allow. The metadata are printed, and every outcome is now either independent of the labels or blocked.
4. fig6-maze-task-spaces. It was changed from blocked to reproduced.
5. Chance levels. They were added; only the "every space" wording above remains.
6. The Supplemental Figure 1 ranking bias. A cross-validated variant was run and disclosed.
7. The wrong recording. It is disclosed and referred to a reader. Only the missing `assumed` flag remains.
8. The Wilcoxon p-value. It is disclosed.

**Not resolved, no effect on a conclusion:**
- Velocity is unsmoothed in the kinematic space. This was not run, but the gap to the peri-movement space is large.
- The SD tuning measure leaves no neurons, so that reading is degenerate. This is disclosed.

**Still bearing on a conclusion:**
- **fig4e: the splice sets the decline time.** This sharpens my round-1 problem 8.
  - The go-locked part of the spliced trace covers go −200 to +100 ms. That is exactly the preparatory window (`maze.PREP`), mapped to −554 to −254 ms.
  - So the reference value "400 ms before onset" (0.703) is taken inside the window the preparatory rate is averaged over. The decline at −263 ms is the end of that window shifted by the median RT.
  - In the main selection, this spliced combination is the only one that passes (cell 24). The movement-locked trace alone gives −307 ms, and the all-preparatory-neuron set is not near zero at onset.
  - The outcome still holds in other selection readings through the movement-locked trace with all preparatory neurons (6 of 8). But the main-reading conclusion should not rest on the splice.
- **suppfig1: the result for the claim's 17 neurons does not survive cross-validation.** The outcome is correct under the criterion, but the README should carry the caveat.
- **j-array-recordings: the outcome rests on an unprovable subset relation.** It should carry `assumed: true`.
- **fig7c: the criterion's band is narrower than random variation (claims-file issue).** This is reported, not corrected.
  - "Within 10% of random halves" is a band of ±0.046 around 0.455, but random halves themselves have SD 0.153 and range 0.067 to 0.869 (cell 71). A random half would usually fail it.
  - The outcome still stands, because array 2 lies 3 to 5.6 SD below the random halves under both S readings.

## End of run

13 turns, 3 minutes, result: success.
