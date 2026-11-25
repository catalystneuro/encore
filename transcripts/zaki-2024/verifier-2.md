# zaki-2024 · verifier-2 · run 45554072027

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 392
drwxr-xr-x 6 runner runner    4096 Nov 25 05:39 .
drwxr-xr-x 8 runner runner    4096 Nov 25 05:39 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 05:30 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 05:30 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 25 05:39 .claude
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .env
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .env.development
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .env.local
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .env.production
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .env.test
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .env.test.local
drwx------ 2 runner runner    4096 Nov 25 05:39 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 05:30 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 05:30 .github
-rw-r--r-- 1 runner runner       0 Nov 25 05:39 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 05:30 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 05:30 .mcp.json
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat zaki-2024-02.yaml
```

```
<persisted-output>
Output too large (43KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/53bcf76c-0903-4131-99d8-38e9affdba65/tool-results/blbg4eot0.txt

Preview (first 2KB):
# Zaki et al. (2024) from dandiset 000718

Tests the findings of [Zaki et al. (2024)](https://doi.org/10.1038/s41586-024-08168-4) that can be
tested on [DANDI:000718](https://dandiarchive.org/dandiset/000718/0.261122.2159), version
0.261122.2159. The dandiset holds two of the nine mice of the paper's calcium imaging and EEG/EMG
experiment (Figure 5, Extended Data Figures 9 and 10), Ca_EEG2-1 (1.5 mA) and Ca_EEG3-4 (0.25 mA),
with one offline recording per offline period. The mice of the one-hour offline experiments and of
the behaviour-only experiments are not in it.

| Claim | Outcome |
|---|---|
| The deposited mice are the source data's mice, with the same freezing | Reproduced |
| High-shock mouse froze more in aversive recall than low-shock mouse | Reproduced |
| Offline bursts more frequent than in circularly shifted data | Reproduced, under an assumption |
| Offline population activity more skewed than in circularly shifted data | Reproduced |
| Movement pauses about 1 s before bursts | Not reproduced |
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat zaki-2024.yaml | head -400
```

```
# Claims for Zaki et al. (2024), "Offline ensemble co-reactivation links memories across days",
# Nature 637, 145-155 (issue of January 2025, published online 6 November 2024), on dandiset 000718.
# Source: the full text, open access under CC BY (PMC11666460), read from its Results, figure and
# Extended Data legends and Methods.
# Quotes and statistics added 2026-10-19 from the full text (Europe PMC PMC11666460).
#
# When these criteria were written, the author had seen the data check only: the file list and
# metadata of version 0.260825.1902, the contents of every NWB file, the ranges and timestamps of
# the deconvolved traces, the sleep-state intervals of the three offline sessions (wake and quiet
# wake only), the cell registration tables of mouse Ca_EEG2-1 and the sizes of the four ensembles
# they give for its offline session (97 neutral, 80 aversive, 166 overlap, 282 remaining), the
# agreement of registered ROI centroids, the telemetry around the fear conditioning epoch, and,
# from the freezing check, the freezing fraction of four sessions (FC of both mice, neutral exposure
# of Ca_EEG2-1, and Recall2 of Ca_EEG3-4, 15.1%). The last of these is one of the four values the
# source-data-link claim compares. No burst, shuffle, locomotion or co-bursting analysis had been
# run. The author had also read the per-mouse values in the paper's source-data repository
# (denisecailab/RetrospectiveMemoryLinkingData_2024 at commit a508164), which list both deposited
# mice in Figure 5c and Extended Data Figure 9.
#
# The dandiset holds two of the nine mice of the calcium imaging and EEG/EMG experiment (Figure 5,
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,700p zaki-2024.yaml; echo ----; head -c 3000 zaki-2024-02.yaml
```

```
source: Extended Data Figure 8d, 8f and 8g; Results, Co-bursting of the overlap and neutral
    ensemble, paragraph 4
  quote: the co-bursting of the overlap and neutral ensembles was not different from the co-bursting
    of the overlap and aversive ensembles during the offline period ... these mice showed no
    differences in freezing in the neutral versus novel contexts during recall
  statistics:
  - about: co-bursting between ensemble pairs, normalized by chance (Extended Data Figure 8g)
    statistic: F2,10 = 1.29
    p: 0.32
    n: 6 mice
  - about: freezing, neutral against novel recall (Extended Data Figure 8d)
    statistic: t5 = 1.52
    p: 0.19
    n: 6 mice
- id: ed7-contexts-discriminable
  statement: Neural activity during neutral and aversive encoding is highly discriminable, with no
    difference between low- and high-shock mice.
  source: Extended Data Figure 7; Results, Co-bursting of the overlap and neutral ensemble,
    paragraph 4
  quote: We found that the neural activity patterns for neutral and aversive contexts were highly
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
cd  tail -c +3000 zaki-2024-02.yaml
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/53bcf76c-0903-4131-99d8-38e9affdba65/tool-results/brrrdyuyn.txt

Preview (first 2KB):
 true
  notebook: reproduce_zaki_2024.ipynb
  output: claim:offline-bursts-above-shuffle
  notes: Under reading (b), each surrogate thresholded at the true trace's mean plus 2 SD, the true
    burst frequency is above the 95th percentile of 1000 circular-shift surrogates in all three
    deposited offline recordings (Ca_EEG2-1 Day 2, 8.73 against a surrogate mean of 0.11 bursts per
    minute, 95th percentile 0.30, maximum 0.50; Ca_EEG3-4 Day 1, 6.42 against 0.01, 0.10 and 0.30;
    Ca_EEG3-4 Day 2, 5.31 against 0.00, 0.00 and 0.20), and no surrogate reaches the true value.
    Under the second generator's seed (the claim's plus 1) and that seed plus 1000 to 4000 the
    surrogate means range 0.10 to 0.11, 0.00 to 0.01 and 0.00, the 95th percentiles 0.30, 0.00 to
    0.10 and 0.00, and the outcome is the same under all five. Under reading (a), each surrogate
    z-scored again, the true frequency is below the surrogate mean in all three (10.94, 8.81 and
    8.48, 95th percentiles 12.14, 9.92 and 9.52; fraction of surrogates at or above the true value
    0.999, 1.000 and 1.000), with surrogate means 10.91 to 10.96, 8.78 to 8.85 and 8.48 to 8.57 under
    the claim's seed and the four others; that reading alone gives not reproduced. What the answer
    changed. This attempt first tested the criterion as it then stood, reading (a) only, and recorded
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/53bcf76c-0903-4131-99d8-38e9affdba65/tool-results/brrrdyuyn.txt"
}
```

```
1	 true
2	  notebook: reproduce_zaki_2024.ipynb
3	  output: claim:offline-bursts-above-shuffle
4	  notes: Under reading (b), each surrogate thresholded at the true trace's mean plus 2 SD, the true
5	    burst frequency is above the 95th percentile of 1000 circular-shift surrogates in all three
6	    deposited offline recordings (Ca_EEG2-1 Day 2, 8.73 against a surrogate mean of 0.11 bursts per
7	    minute, 95th percentile 0.30, maximum 0.50; Ca_EEG3-4 Day 1, 6.42 against 0.01, 0.10 and 0.30;
8	    Ca_EEG3-4 Day 2, 5.31 against 0.00, 0.00 and 0.20), and no surrogate reaches the true value.
9	    Under the second generator's seed (the claim's plus 1) and that seed plus 1000 to 4000 the
10	    surrogate means range 0.10 to 0.11, 0.00 to 0.01 and 0.00, the 95th percentiles 0.30, 0.00 to
11	    0.10 and 0.00, and the outcome is the same under all five. Under reading (a), each surrogate
12	    z-scored again, the true frequency is below the surrogate mean in all three (10.94, 8.81 and
13	    8.48, 95th percentiles 12.14, 9.92 and 9.52; fraction of surrogates at or above the true value
14	    0.999, 1.000 and 1.000), with surrogate means 10.91 to 10.96, 8.78 to 8.85 and 8.48 to 8.57 under
15	    the claim's seed and the four others; that reading alone gives not reproduced. What the answer
16	    changed. This attempt first tested the criterion as it then stood, reading (a) only, and recorded
17	    not reproduced, with reading (b) as a variant, and asked a reader whether the criterion should
18	    list both. The reader answered (questions/zaki-2024.yaml, 2026-11-25) that the paper does not fix
19	    the detail and amended the criterion to name both readings, reproduced under either, with the
20	    outcome marked as resting on the reading that gives it. The outcome changes from not reproduced
[... 541 more lines not kept]
```

**Agent**

No finding is rated critical. Next I'll dump the notebook outputs and check them against the conclusions.

**Agent calls Bash**

```bash
cd  grep -c '^- id:' zaki-2024.yaml; grep -c '^- claim:' zaki-2024-02.yaml; python3 - <<'E'
import json
nb=json.load(open('reproduce_zaki_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== cell {i} [{c['cell_type']}]")
    if c['cell_type']=='markdown': print(src)
    else:
        print(src[:600]+('...' if len(src)>600 else ''))
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            t=''.join(t)
            print('>>>',t[:6000])
E
```

```
<persisted-output>
Output too large (77.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/53bcf76c-0903-4131-99d8-38e9affdba65/tool-results/bstcjs3vn.txt

Preview (first 2KB):
26
26
=== cell 0 [markdown]
# Reproducing Zaki et al. (2024) on DANDI:000718

**Paper.** Zaki, Pennington, Morales-Rodriguez et al., "Offline ensemble co-reactivation links memories across days", *Nature* 637, 145-155 (2025), [doi:10.1038/s41586-024-08168-4](https://doi.org/10.1038/s41586-024-08168-4).

**Dataset.** [DANDI:000718](https://dandiarchive.org/dandiset/000718/0.261122.2159), version **0.261122.2159**, which this attempt was asked to use (it is a repeat attempt, made blind, on the data as they are now). It is the most recent published version. The claims file's description was written against version 0.260825.1902; three NWB files differ between the two versions, and the data check below shows that the values this analysis uses are the same in both. Files are streamed from the archive; nothing is downloaded.

**Text read.** The claims file (`claims/zaki-2024.yaml`) was written from the full text of the version of record (PMC11666460): Results, figure and Extended Data legends, and Methods. The paper's analysis code (github.com/denisecailab/RetrospectiveMemoryLinkingAnalysis_2024) is not public (404 when this attempt was made). The source-data repository the paper names under Data availability is read, at commit a508164, only for the link claim and as a reference value for one claim.

**What the dataset holds.** Two of the nine mice of the calcium imaging and EEG/EMG experiment (Figure 5, Extended Data Figures 9 and 10): Ca_EEG2-1 (1.5 mA) and Ca_EEG3-4 (0.25 mA), with one offline recording for each offline period deposited (Ca_EEG2-1: the first offline recording after aversive encoding; Ca_EEG3-4: the first after neutral and the first after aversive encoding).

| Claim | Tested here |
|---|---|
| source-data-link | tested (link, with the paper's 
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/53bcf76c-0903-4131-99d8-38e9affdba65/tool-results/bstcjs3vn.txt"
}
```

```
1	26
2	26
3	=== cell 0 [markdown]
4	# Reproducing Zaki et al. (2024) on DANDI:000718
5	
6	**Paper.** Zaki, Pennington, Morales-Rodriguez et al., "Offline ensemble co-reactivation links memories across days", *Nature* 637, 145-155 (2025), [doi:10.1038/s41586-024-08168-4](https://doi.org/10.1038/s41586-024-08168-4).
7	
8	**Dataset.** [DANDI:000718](https://dandiarchive.org/dandiset/000718/0.261122.2159), version **0.261122.2159**, which this attempt was asked to use (it is a repeat attempt, made blind, on the data as they are now). It is the most recent published version. The claims file's description was written against version 0.260825.1902; three NWB files differ between the two versions, and the data check below shows that the values this analysis uses are the same in both. Files are streamed from the archive; nothing is downloaded.
9	
10	**Text read.** The claims file (`claims/zaki-2024.yaml`) was written from the full text of the version of record (PMC11666460): Results, figure and Extended Data legends, and Methods. The paper's analysis code (github.com/denisecailab/RetrospectiveMemoryLinkingAnalysis_2024) is not public (404 when this attempt was made). The source-data repository the paper names under Data availability is read, at commit a508164, only for the link claim and as a reference value for one claim.
11	
12	**What the dataset holds.** Two of the nine mice of the calcium imaging and EEG/EMG experiment (Figure 5, Extended Data Figures 9 and 10): Ca_EEG2-1 (1.5 mA) and Ca_EEG3-4 (0.25 mA), with one offline recording for each offline period deposited (Ca_EEG2-1: the first offline recording after aversive encoding; Ca_EEG3-4: the first after neutral and the first after aversive encoding).
13	
14	| Claim | Tested here |
15	|---|---|
16	| source-data-link | tested (link, with the paper's source data) |
17	| ed9b-aversive-freezing-high-vs-low | tested |
18	| offline-bursts-above-shuffle | tested |
19	| offline-skew-above-shuffle | tested |
20	| burst-locomotio
[... 476 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/53bcf76c-0903-4131-99d8-38e9affdba65/tool-results/bstcjs3vn.txt",
 "offset": 497
}
```

```
497	for a, name in zip(ax, OFF):
498	    r = B[(0, name)]; v = Bb[(1, name)]
499	    a.hist(r["sur"], 30, color="0.6", label="(a) re-z-scored")
500	    a.hist(v["sur"], 30, color="C1", label="(b) true threshold"); a.axvline(r["true"], color="C0", ls="--")
501	    a.set_title(name, fontsize=9); a.set_xlabel("bursts per minute")
502	    print(f"{name}: surrogate range (a) {r['sur'].min():.2f} to {r['sur'].max():.2f}, (b) {v['sur'].min():.2f} to {v['sur'].max():.2f}; true {r['true']:.2f} (all inside the axes)")
503	ax[0].legend(fontsize=8)
504	plt.tight_layout(); plt.show()
505	
506	>>> Ca_EEG2-1 Day2 S1: surrogate range (a) 8.63 to 13.44, (b) 0.00 to 0.50; true 8.73 (all inside the axes)
507	Ca_EEG3-4 Day1 S1: surrogate range (a) 6.92 to 10.93, (b) 0.00 to 0.30; true 6.42 (all inside the axes)
508	Ca_EEG3-4 Day2 S1: surrogate range (a) 6.32 to 10.83, (b) 0.00 to 0.20; true 5.31 (all inside the axes)
509	
510	>>> <Figure size 1200x280 with 3 Axes>
511	=== cell 27 [code]
512	# Synthetic check of the two readings, on cells with no bursts (verifier, round 1). 600 independent AR(1) cells
513	# (coefficient 0.9) over 9000 frames (10 min at 15 Hz), alone and with a slow drift shared by all cells (a random
514	# walk smoothed over 60 s, at 4% of a cell's SD, which gives the mean trace a drift about as large as its noise).
515	# 200 surrogates of each reading; the claim's third generator (seed + 2).
516	rng = np.random.default_rng(seed("offline-bursts-above-shuffle") + 2)
[... 297 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o -i '.\{200\}quiet wake.\{200\}' paper/*.txt; grep -o -i '.\{150\}100 Hz.\{100\}' paper/*.txt; grep -o -i '.\{300\}computed for each of these shuffles.\{100\}' paper/*.txt; sed -n '1,200p' README.md | tail -n +15
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 2: Zaki et al. (2024) on DANDI:000718 v0.261122.2159**

The claims file holds 26 claims, and the attempt record gives 26 outcomes: 6 tested and 20 blocked (data_missing).

### 1. Outcomes and assumptions

| Claim | Record | Agree? | Assumption |
|---|---|---|---|
| source-data-link | reproduced | Yes. Both readings give 4 of 4 within tolerance (cell 19). | none |
| ed9b-aversive-freezing-high-vs-low | reproduced | Yes. 64.09 vs 8.82, 10 of 10 bins, U = 100, p = 1.83e-04 (cell 22). | none |
| offline-bursts-above-shuffle | reproduced, `assumed: true` | Yes, as the criterion gives it (cell 25). | Stated clearly (deviation 2, cell 28). It is not a well-supported reading: the record itself says (b) is "not the better-supported one" and is passed by drift-only cells (cell 27). The outcome follows from the criterion, but on a reading that cannot really fail. |
| offline-skew-above-shuffle | reproduced | Yes. True skew is above all surrogates, and every seed's 95th percentile is far below it (cell 30). | none |
| burst-locomotion-pause | not_reproduced | Yes. 0 of 3 recordings under both readings (cell 33). This holds at the lag of peak correlation and at every shift from −8 to +8 s (cell 34). | The shared clock is stated, and it is now tested by the shifts. |
| fig5c-wake-overlap-neutral-coburst | partially_reproduced | Yes, as the criterion permits (cell 37). | **Not marked `assumed`**, although the outcome rests on wake reading (b) alone. The record itself calls (b) the worse match to the paper. Under (a), OxN < OxA (25.9 vs 35.3; 8.2 vs 17.6). It should carry `assumed: true`, as the burst claim does. |
| fig5c-sleep-no-coburst-difference | blocked | Yes. Only wake and quiet wake are present (cells 3, 8). | — |
| fig5c-low-shock-wake-no-difference | blocked | Yes. Ca_EEG3-4's files hold the ophys and sleep modules only, and the only cell_registration module is in the Week file (cell 8). | — |
| ed9c-eeg-cohort-linking | blocked | Yes. The descriptive values are printed (cell 40). | — |
| ed9-ed10-sleep-unchanged | blocked | Yes. The one-mouse description is in cell 41. | Log RMS as the EMG feature is stated as an assumption, and it is reasonable. |
| The other 16 claims | blocked | Yes. The archive holds 2 subjects (cell 3). | — |

### 2. Statements the printed numbers do not support

- **Cell 35, with the same sentence in the record's burst-locomotion notes:** "Under neither reading is movement in the second before a burst lower than 3 to 5 s before it in any recording." The medians *are* lower before the burst in two recordings: 0.0303 vs 0.0356 for Ca_EEG2-1, and 0.0761 vs 0.0917 (0.0847 vs 0.1002 under onset) for Ca_EEG3-4 Day2 (cell 33). What the data support is "not significantly lower".
- **Cell 44, Summary:** "no pre-burst slowing in 0 of 3 recordings" is a double negative that says the opposite of the result. It should read "pre-burst slowing in 0 of 3".
- **Cell 45:** "Ensemble sizes … agree with the paper's source data." No comparison of ensemble sizes with the source data is printed. Cell 7 only prints the sizes (97/80/166/282).
- **Cell 28:** "above every surrogate in all three recordings … under the second generator's seed and the four others." Maxima and fractions are printed only for seed+1 (cell 25). For the other four seeds only 95th percentiles are printed. The statement is very likely true but not shown. Cell 31 says the same of the skew claim ("above every one … under all five seeds"), where again only the seed+0 maxima are printed (cell 30).
- **Cell 35 and the record's notes:** "Around random times movement in the later window is lower in Ca_EEG2-1 (p < 0.001), as movement declines over the recording."
  - The first generator gives p = 0.000 (cell 33), but the second gives 0.003 (cell 34), which is not below 0.001.
  - "Movement declines over the recording" is not printed anywhere.
- **Record, ed9-ed10 notes, and cell 42:** "awake 67% (after neutral) and 49% (after aversive) … against 93% at the same clock time the day before." The 93% reference is printed only for the post-neutral window (cell 41). There is no same-clock-time reference for the post-aversive window.
- **README:** "It takes about six minutes." Cell 44 prints a run time of 3.7 min.

Everything else in the Result cells, the Summary, the README and the record's notes matches the printed outputs. I checked in particular:
- the bursts under (a) and (b), and all five seed sets for each;
- the synthetic check (5.90 vs 2.60 under (b), mean 8.55 under (a), and the independent-cell values);
- the skew values;
- the shift table;
- the 1 s baseline variant;
- the fig5c tables and the source-data values 10.37 / 8.39;
- the 64 of 68 quiet-wake epochs scored as wake;
- the clock and dropout figures (−3780 to −2560 s, 113 s, 47 and 17 min);
- the sleep features.

The paper does say "during brief periods of quiet wake" (Results).

**Round-1 reasons:** the record's `reason` fields state my round-1 reasons faithfully, close to my own wording. The finding numbering in `reviewed` is correct: the webcam-description finding is 9.

### 3. Round-1 points

**Resolved:**
- B3, clock sensitivity: the shifts in cell 34 leave the result negative.
- B4, unequal windows: the 1 s baseline variant is in cell 34.
- B6 and B7: recorded as deviations.
- B9: now findings 4, 6 and 9.
- C1 to C3: cell 8 prints the ActivitySignal description, the processing modules and the quiet-wake definition.
- C4: done in cell 34.
- The descriptive tests for ed9c and ed9-ed10: cells 40 and 41.
- B5: recorded as deviations (the criterion's choice).

**Acknowledged but still bearing on a conclusion:**
- **B1:** offline-bursts-above-shuffle is reproduced only under reading (b). The record now documents, with its own synthetic check, that this reading is passed by co-variation alone, and has put the question to a reader. Under reading (a), the one that tests burst structure, the result is not reproduced. This remains a claims-file issue.
- **B2:** fig5c-wake rests on wake reading (b). The files define quiet wake as a waking state, and the Methods' scoring puts it in wake (cell 16), so reading (a) is the better match, and under it OxN < OxA. This is put to a reader, but the outcome is not marked `assumed` (see 1).

**Not resolvable from my materials:** C5, the amendment record `questions/zaki-2024.yaml`, which I do not have.

### 4. Critical findings

No finding in the attempt record is rated `critical`.

One rating I would change: finding 1 (rated `major`). It says the behaviour sessions of Ca_EEG2-1 are timestamped about 1 h later than the offline recordings and telemetry, and cell 15 shows this:
- the EEG match at +0.002 s with a difference of 0 V;
- telemetry dropouts that each fit their session if it started 1 h before its timestamp;
- OfflineDay2Session1 starting 2817 s before FC.

This is the "signals on different clocks" case of the definition. The files do not say which clock is right. Only a dropout analysis shows that the offset is about 1 h, and an analysis that takes the timestamps as given would misorder the first two post-FC offline recordings and misplace the post-encoding windows. I would rate it **critical**. The record's case for `major` is that the epochs table visibly contradicts the protocol, but that contradiction shows something is wrong, not what, and it does not undo the wrong result.

## End of run

11 turns, 2 minutes, $1.01 at API prices, result: success.
