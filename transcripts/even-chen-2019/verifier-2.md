# 000121 · verifier-2 · run 38972089200

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper 2>/dev/null; ls docs 2>/dev/null
```

```
Exit code 2
total 500
drwxr-xr-x 5 runner runner    4096 Oct 16 21:58 .
drwxr-xr-x 7 runner runner    4096 Oct 16 21:58 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:43 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:43 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 16 21:58 .claude
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .env
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .env.development
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .env.local
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .env.production
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .env.test
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .env.test.local
drwx------ 2 runner runner    4096 Oct 16 21:58 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:43 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:43 .github
-rw-r--r-- 1 runner runner       0 Oct 16 21:58 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:43 .idea
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat round-1-report.md; echo ======; cat README.md; echo =====; cat 000121-even-chen-2019-01.yaml
```

```
<persisted-output>
Output too large (41.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/fb57412d-e4b4-4739-b562-4ed2f6fdb4cf/tool-results/bhocd7hmf.txt

Preview (first 2KB):
**A. Outcomes** (20 claims, from the claims file; the notebook tests 19 and treats 1 as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| session-configurations | partially_reproduced | Cell 17: 8 of 12 sessions match the Methods. All 4 mismatches are R horizontal and vertical exchanged: 01-15/16 lie on the x axis, 01-17/18 on the y axis. The 5 J sessions match. |
| r-trial-counts | partially_reproduced | Cell 19, grouped by Methods dates: ring 3584 and vertical 3842 are within tolerance; horizontal 4156 (paper 3699) and 3-rings 1340 (paper 912) are not, under every reading. Grouped by geometry, 3 of 4 match, so the Methods' date labels look swapped. |
| j-sessions-complete | blocked (data_missing) | I checked the API myself: version 0.220124.2156 (and 0.210815.0703) lists 12 assets, 5 of them J. No per-session counts are in the paper, so only a lower-bound consistency check is possible, not a test. |
| delays-and-times | partially_reproduced | Cell 21. Reaction times (J 332, R 305 ms) and reach times under reading (b) (J 587, R 486 ms) are within tolerance, and R's RT–delay correlation holds (p=1.8e-205). It fails on: J's RT–delay correlation (p=0.21); R delays running to 1000 ms (bound 990, uniform to 1000); no-delay fractions of 19.8% (J) and 0.2% (R). |
| channels-task-correlated | reproduced | Cell 23: J 72 (expected 74±7.4), R 80 (expected 80). |
| pca-variance | not_reproduced | Cell 25: all 6 J values and R PCs 2–6 are within tolerance, but R PC1 is 72.8 against a lower bound of 72.9. The criterion's partial case requires all R values within, so by its letter this is not reproduced. It is a 0.14-point miss, and the result depends on the day-mean choice (the trial-window variant gives 80.5). |
| spatial-plane-variance | not_reproduced | Cell 27:
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "round-1-report.md"
}
```

```
1	**A. Outcomes** (20 claims, from the claims file; the notebook tests 19 and treats 1 as blocked)
2	
3	| Claim | Outcome | Reason |
4	|---|---|---|
5	| session-configurations | partially_reproduced | Cell 17: 8 of 12 sessions match the Methods. All 4 mismatches are R horizontal and vertical exchanged: 01-15/16 lie on the x axis, 01-17/18 on the y axis. The 5 J sessions match. |
6	| r-trial-counts | partially_reproduced | Cell 19, grouped by Methods dates: ring 3584 and vertical 3842 are within tolerance; horizontal 4156 (paper 3699) and 3-rings 1340 (paper 912) are not, under every reading. Grouped by geometry, 3 of 4 match, so the Methods' date labels look swapped. |
7	| j-sessions-complete | blocked (data_missing) | I checked the API myself: version 0.220124.2156 (and 0.210815.0703) lists 12 assets, 5 of them J. No per-session counts are in the paper, so only a lower-bound consistency check is possible, not a test. |
8	| delays-and-times | partially_reproduced | Cell 21. Reaction times (J 332, R 305 ms) and reach times under reading (b) (J 587, R 486 ms) are within tolerance, and R's RT–delay correlation holds (p=1.8e-205). It fails on: J's RT–delay correlation (p=0.21); R delays running to 1000 ms (bound 990, uniform to 1000); no-delay fractions of 19.8% (J) and 0.2% (R). |
9	| channels-task-correlated | reproduced | Cell 23: J 72 (expected 74±7.4), R 80 (expected 80). |
10	| pca-variance | not_reproduced | Cell 25: all 6 J values and R PCs 2–6 are within tolerance, but R PC1 is 72.8 against a lower bound of 72.9. The criterion's partial case requires all R values within, so by its letter this is not reproduced. It is a 0.14-point miss, and the result depends on the day-mean choice (the trial-window variant gives 80.5). |
11	| spatial-plane-variance | not_reproduced | Cell 27: at best 3 of 7 values are within tolerance under any pairing of readings (4 needed for partial). J is 40–54% against 48–68%. Shuffle p is 0.005–0.16 against the paper's <1e-4. |
12	| plane
[... 43 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

**Agent calls Read**

```json
{
 "file_path": "000121-even-chen-2019-01.yaml"
}
```

```
1	# Even-Chen, Sheffer, Vyas, Ryu & Shenoy (2019) from dandiset 000121
2	
3	Tests the findings of [Even-Chen et al. (2019)](https://doi.org/10.1371/journal.pcbi.1006808) on
4	[DANDI:000121](https://dandiarchive.org/dandiset/000121/0.220124.2156), which holds 12 sessions of
5	delayed center-out reaching recorded with Utah arrays: all 7 sessions of monkey R and 5 of the 16
6	of monkey J.
7	
8	| Claim | Outcome |
9	|---|---|
10	| Sessions have the configurations the Methods list | Partially reproduced |
11	| R's trial counts per configuration | Partially reproduced |
12	| J's 16 sessions | Blocked: data missing |
13	| Delays, reaction and reach times | Partially reproduced |
14	| 74 (J) and 80 (R) channels tuned to target position | Reproduced |
15	| Variance of the top PCs of condition averages | Not reproduced |
16	| Variance in the spatial plane per task | Not reproduced |
17	| Time course of the state in the spatial plane | Partially reproduced |
18	| Single-trial neural deviations predict the hand at maximum speed | Reproduced |
19	| The speed axis varies with speed within a distance | Partially reproduced |
20	| Distance information remains after removing speed | Reproduced |
[... 24 more lines not kept]
```

```
1	schema_version: 1
2	id: 000121-even-chen-2019-01
3	dandiset: "000121"
4	dandiset_version: 0.220124.2156
5	paper: doi:10.1371/journal.pcbi.1006808
6	date: 2026-10-16
7	entry: 000121-even-chen-2019
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	outcomes:
17	- claim: session-configurations
18	  outcome: partially_reproduced
19	  notebook: reproduce_even_chen_2019.ipynb
20	  output: claim:session-configurations
[... 524 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_even_chen_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--\n'+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain'])[:5000])
            elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
```

```
<persisted-output>
Output too large (125.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/fb57412d-e4b4-4739-b562-4ed2f6fdb4cf/tool-results/bxn81rsze.txt

Preview (first 2KB):
######## CELL 0 [markdown]
# Reproducing Even-Chen et al. (2019) from dandiset 000121

Paper. Even-Chen N, Sheffer B, Vyas S, Ryu SI, Shenoy KV (2019). Structure and variability of
delay activity in premotor cortex. *PLOS Computational Biology* 15(2), e1006808.
[doi:10.1371/journal.pcbi.1006808](https://doi.org/10.1371/journal.pcbi.1006808). This attempt
used the full text, which is open access.

Dandiset. [DANDI:000121](https://dandiarchive.org/dandiset/000121/0.220124.2156), version
0.220124.2156. The paper cites no DANDI version (it predates the dandiset; its data statement
points to a Stanford zip file that now returns HTTP 403). This is the most recent published
version. The earlier published version, 0.210815.0703, holds the same 12 files (same blobs and
sizes) and differs only in metadata; the draft holds no files (see the data check).

What the dandiset holds. 12 sessions of delayed center-out reaching with two Utah arrays: all
7 sessions of monkey R and 5 of the 16 of monkey J (ring 1 of 4, vertical 2 of 4, 3-rings 2 of 4,
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/fb57412d-e4b4-4739-b562-4ed2f6fdb4cf/tool-results/bxn81rsze.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Even-Chen et al. (2019) from dandiset 000121
4	
5	Paper. Even-Chen N, Sheffer B, Vyas S, Ryu SI, Shenoy KV (2019). Structure and variability of
6	delay activity in premotor cortex. *PLOS Computational Biology* 15(2), e1006808.
7	[doi:10.1371/journal.pcbi.1006808](https://doi.org/10.1371/journal.pcbi.1006808). This attempt
8	used the full text, which is open access.
9	
10	Dandiset. [DANDI:000121](https://dandiarchive.org/dandiset/000121/0.220124.2156), version
11	0.220124.2156. The paper cites no DANDI version (it predates the dandiset; its data statement
12	points to a Stanford zip file that now returns HTTP 403). This is the most recent published
13	version. The earlier published version, 0.210815.0703, holds the same 12 files (same blobs and
14	sizes) and differs only in metadata; the draft holds no files (see the data check).
15	
16	What the dandiset holds. 12 sessions of delayed center-out reaching with two Utah arrays: all
17	7 sessions of monkey R and 5 of the 16 of monkey J (ring 1 of 4, vertical 2 of 4, 3-rings 2 of 4,
18	horizontal none). Each file has a trials table, hand, cursor and eye positions, threshold
19	crossings of the 192 electrodes as units, and LFP.
20	
[... 498 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/fb57412d-e4b4-4739-b562-4ed2f6fdb4cf/tool-results/bxn81rsze.txt",
 "offset": 519,
 "limit": 480
}
```

```
519	    if s["monkey"] != "R":
520	        continue
521	    t = s["trials"]
522	    co = t[t.center_out]
523	    rows.append({"date": s["date"], "Methods": s["methods_config"], "file": s["config"],
524	                 "(a) successful, delayed": int((co.successful & (co.delay >= premotor.MIN_DELAY_S)).sum()),
525	                 "(b) delayed, any outcome": int((co.delay >= premotor.MIN_DELAY_S).sum()),
526	                 "(c) successful, with no-delay": int(co.successful.sum()),
527	                 "(b) also without a go cue": int((~(co.delay < premotor.MIN_DELAY_S)).sum()),
528	                 "(a) in the layout only": int((co.successful & (co.delay >= premotor.MIN_DELAY_S) & co.in_layout).sum())})
529	counts = pd.DataFrame(rows)
530	print(counts.to_string(index=False))
531	readings = ["(a) successful, delayed", "(b) delayed, any outcome", "(c) successful, with no-delay",
532	            "(b) also without a go cue", "(a) in the layout only"]
533	for grouping in ("Methods", "file"):
534	    g = counts.groupby(grouping)[readings].sum().reindex(list(R_EXPECTED))
535	    g["paper"] = pd.Series(R_EXPECTED)
536	    print(f"\nGrouped by the configuration of the {grouping}:")
537	    print(g.to_string())
538	    for r in readings:
[... 460 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/fb57412d-e4b4-4739-b562-4ed2f6fdb4cf/tool-results/bxn81rsze.txt",
 "offset": 999,
 "limit": 470
}
```

```
999	    ax[i].plot(1000 * centers, timecourse[m][0], color="tab:blue")
1000	    ax[i].axvline(0, color="grey", lw=0.5)
1001	    ax[i].set(title=f"monkey {m}", xlabel="time from target onset (ms)", ylabel="distance from delay state (mm)")
1002	plt.tight_layout()
1003	plt.show()
1004	print("Plotted ranges (mm):", {m: (float(round(np.nanmin(timecourse[m][0]), 1)), float(round(np.nanmax(timecourse[m][0]), 1))) for m in "JR"})
1005	--OUT--
1006	J: d0 53.8 mm, dmin 6.8 mm; divergence (D < 0.9) at 70 ms, convergence (D < 0.1) at 270 ms after target onset
1007	   thresholds 0.8 and 0.1: 150 and 270 ms
1008	   thresholds 0.95 and 0.2: 70 and 230 ms
1009	   thresholds 0.9 and 0.05: 70 and 390 ms
1010	   D(t) every 40 ms from -90 ms: {-90: 1.03, -50: 1.02, -10: 0.96, 30: 1.0, 70: 0.89, 110: 0.85, 150: 0.68, 190: 0.4, 230: 0.19, 270: 0.08, 310: 0.12, 350: 0.1, 390: 0.03, 430: 0.0, 470: 0.04, 510: 0.12, 550: 0.17, 590: 0.2, 630: 0.24, 670: nan}
1011	   conditions with at least 5 trials per bin: 0 to 96
1012	   D over the bins before target onset (-200 to 0 ms): mean 1.01, SD 0.03, range 0.96 to 1.03; pre-onset bins below 0.9: 0 of 10
1013	   variant, converged state from trials whose delay window starts after the bin (bins up to 430 ms with at least half the conditions): divergence 70 ms, convergence 250 ms; minimum at 410 ms; pre-onset D SD 0.03
1014	   state before target onset, mean over trials (mm): x -2.1, y -30.4
1015	
1016	--OUT--
1017	R: d0 47.3 mm, dmin 10.2 mm; divergence (D < 0.9) at 90 ms, convergence (D < 0.1) at 350 ms after target onset
1018	   thresholds 0.8 and 0.1: 130 and 350 ms
[... 450 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1371-journal.pcbi.1006808.yaml"
}
```

```
1	# Claims for Even-Chen, Sheffer, Vyas, Ryu & Shenoy (2019) on dandiset 000121.
2	# Source: the full text of the paper (PLOS Computational Biology, open access), read from the
3	# journal's JATS XML: Methods, Results and figure legends.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list and
6	# metadata of both published versions, every group and column of the files, the trials tables of
7	# all 12 sessions (counts, target positions, delays, success flags), the time span and count of
8	# spikes of every unit, the hand samples of two sessions, and one check of which array is which
9	# (on one session per monkey: live channels, the number of channels whose 200 ms pre-go count
10	# regresses significantly on target x and y, and 5-fold SVM decoding of ring targets in windows
11	# before the target, before the go cue and after it). That check found 66 significant channels
12	# of 95 live ones for R (0124) and 57 for J (1015) on units 96 to 191, so it bears on
13	# channels-task-correlated. No other claim's analysis had been run.
14	#
15	# The paper names no analysis code, and its data link (stanford.edu/~shenoy/Data/...zip) returns
16	# 403. The conversion code (catalystneuro/shenoy-lab-to-nwb, commit 319acb4) was read; it settles
17	# how the units and trial times were made (see the notebook header).
18	#
19	# The dandiset holds all 7 sessions of monkey R and 5 of the 16 of monkey J (ring 1 of 4,
20	# vertical 2 of 4, 3-rings 2 of 4, horizontal 0 of 4). Results for J use those 5 sessions.
[... 333 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/fb57412d-e4b4-4739-b562-4ed2f6fdb4cf/tool-results/bxn81rsze.txt",
 "offset": 1468,
 "limit": 460
}
```

```
1468	horizontal          24          6.96      1.00
1469	ring                36         13.42      0.78
1470	vertical            24         38.21      0.67
1471	   conditions with the condition mean nearer the origin than the median: 0.67 below 45; farther: 0.83
1472	
1473	--OUT--
1474	<Figure size 900x430 with 2 Axes>
1475	
1476	######## CELL 54 [markdown]
1477	**Result: reproduced.** The major axis lies within 45 degrees of the direction of the condition
1478	mean for 69 of 96 conditions in J (median 21.0 degrees, Wilcoxon p = 4.1e-08) and 99 of 132 in R
1479	(median 19.3 degrees, p = 8.0e-10). The median ratio of major to minor axis is 1.35 (J) and
1480	1.56 (R).
1481	
1482	######## CELL 55 [markdown]
1483	## on-greater-than-off
1484	
1485	> The mean absolute on-axis (distance) deviation of the neural state is larger than the off-axis
1486	> (direction) deviation, in each task (J p = 9e-7 ring, 4e-7 horizontal, 1e-8 vertical, 3e-14
1487	> 3-rings; R 8e-3, 4e-7, 2e-7 and 0.19).
[... 437 more lines not kept]
```

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL -o paper/pcbi.1006808.xml "https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1006808&type=manuscript"; ls -la paper; head -c 300 paper/pcbi.1006808.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import re
x=open('paper/pcbi.1006808.xml').read()
t=re.sub(r'<[^>]+>',' ',x); t=re.sub(r'\s+',' ',t)
open('paper/pcbi.1006808.txt','w').write(t)
for kw in ['F test','F-test','4d','inset','Welch','t-test','day','2017','delay was','horizontal']:
  for m in re.finditer(kw,t):
    print('==',kw,':',t[max(0,m.start()-300):m.start()+300]); 
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import re
t=open('paper/pcbi.1006808.txt').read()
i=t.find('Fig 4 ');
for m in re.finditer(r'\( d \)',t): print('==',t[m.start()-200:m.start()+900])
for kw in ['range','400 ms','reaction time','reach time','first PC','top six','center']:
  for m in re.finditer(kw,t): print('##',kw,':',t[max(0,m.start()-250):m.start()+250])
"
```

Result: not kept, because it reads the paper's text.

**Agent**

**Round 2 verification: Even-Chen et al. 2019 (doi:10.1371/journal.pcbi.1006808) on DANDI:000121, version 0.220124.2156**

The claims file has 20 claims, and the attempt record gives an outcome for all 20: 6 reproduced, 7 partially reproduced, 6 not reproduced, 1 blocked (data_missing). The paper's JATS XML and a text extraction are saved in `paper/`.

**1. Stated outcomes**

I agree with all 20 outcomes. Two need a comment:

- **plane-timecourse (partially_reproduced).** By the letter of the criterion this is reproduced. All four main times are within tolerance (cell 35: 70/90 ms and 270/350 ms; R's 350 ms sits exactly on its bound). I accept the downgrade, because R's divergence cannot be told from baseline noise: 6 of the 10 pre-onset bins are below 0.9. The record should say plainly that this is a judgment beyond the criterion. That matters because pca-variance follows the letter in the other direction: its variant passes (80.5%) and the outcome is not raised.
- **distance-error-and-plane-projection (reproduced).** This is correct by the criterion. The claim also says projection raises the error "to the level of the direction errors", and the paper gives p > .05 for every ring in J and R. In cell 73 this holds for only 1 of 6 rings (J 4 cm, p = 0.46). The notes disclose it.

**2. Sentences the printed outputs do not support**

- **Cell 36:** "J's times are robust". This is true only for the two checks added (pre-onset SD 0.03, and the non-overlapping converged state). Under the other thresholds in cell 35, J diverges at 150 ms (threshold 0.8, outside 0 to 100 ms) and converges at 390 ms (threshold 0.05, outside 250 to 350 ms). The same cell gives "(convergence 310 ms)" for R's variant without saying it is also outside 400 ± 50 ms. The attempt record's notes repeat "J's times are robust".
- **Cell 39:** "off axis J 0.101, R 0.083, p at most 3.0e-21". J's p is 3.1e-21 (cell 38).
- **Cell 42:** "Split by task and session, 110 to 180 trials per distance". No per-task, per-session trial counts are printed in cell 41.
- **Summary (cell 75):** the array labelled PMd "has 29 silent channels and no target signal". Cell 26 prints 40 of 96 of those channels as significant for R when sessions are pooled. Cell 9 shows up to 6 significant delay channels and 16 movement channels per session. Cell 10's wording, "almost no target information", fits the decoding results. "No target signal" does not. The record's electrode_group finding should also mention the 40 of 96.
- **Attempt record, delays-and-times notes:** "the means are 342 ms (J) and 340 ms (R), just inside". Only R's value is just inside (bound 342). J's 342 ms is well inside its range of 311 to 381 ms. Cell 24 states this correctly.

Every other sentence I checked matches the printed numbers. That covers the "**Result:**" cells 18 to 74, the Summary, the README and the record's notes and findings. The checks include:
- the trial-count percentages;
- the 484 to 1963 s gaps between trials;
- 99.93 to 99.95% of spikes inside trials;
- the 12 of 13 PCA values within tolerance;
- the share of seven plane values within tolerance under any pairing (at most three);
- the threshold ranges of 10 to 150 ms and 230 to 390 ms;
- the per-session counts;
- the Fig 4d inset restriction, which I confirmed against the paper's legend.

The record states my round-1 reasons faithfully and in my own wording. Each problem from round 1 is attached to the claim it bears on. The only cuts are minor details, such as B3's per-session rate range, and those are covered in the responses.

**3. Round-1 points**

Resolved:
- **B1:** the variant with onset searched only after the go cue is added, the share of early onsets is printed, and the conclusion says R's mean matches only because those trials are kept.
- **B2:** with deviations from session × condition means the correlations barely change.
- **B3:** spikes fall within trials, so the main day mean is the rate over trial time.
- **B4:** the pre-onset spread of D and the non-overlapping converged state are added, the outcome is changed to partial, and "starts at the center" is addressed.
- **B5:** counts per task and session are added.
- **B6:** the per-session p values now print correctly.
- **B7:** the ring task is dropped from the per-task test.
- **B8:** a paired test is added and the leak is recorded.
- **B9:** the reading that counts failed trials without a go cue is added.
- **B10 to B13:** each is now stated in the notebook.

Under C:
- Done: spikes between trials, session confounds, divergence robustness.
- Cannot be settled: whether the horizontal/vertical swap comes from the paper or the conversion, and the paper's trial subsets (912 trials, 2237 held-out).

Still open and bearing on a conclusion:
- **plane-timecourse:** the record should say the outcome is a judgment beyond the criterion, and should note that both monkeys' times depend on the threshold.
- **distance-error-and-plane-projection:** the part of the claim about projected error matching the direction errors holds for 1 of 6 rings. The test also compares against unrestricted arc errors, while the paper's Fig 4d inset uses errors within the 4 cm ring's range. The restricted comparison was not run.
- **pca-variance:** this stays fragile. The outcome depends on how the day's mean is taken (72.8% against 80.5% for R's PC1). The choice is now justified and disclosed, so nothing more is needed beyond the statement already made.

## End of run

15 turns, 3 minutes, result: success.
