# yang-2025 · verifier-2 · run 45927151690

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 3696
drwxr-xr-x 6 runner runner     4096 Nov 27 02:28 .
drwxr-xr-x 8 runner runner     4096 Nov 27 02:28 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 27 02:14 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 27 02:14 .bashrc
drwxr-xr-x 5 runner runner     4096 Nov 27 02:28 .claude
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .env
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .env.development
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .env.development.local
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .env.local
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .env.production
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .env.production.local
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .env.test
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .env.test.local
drwx------ 2 runner runner     4096 Nov 27 02:28 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 27 02:14 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 27 02:14 .github
-rw-r--r-- 1 runner runner        0 Nov 27 02:28 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 27 02:14 .idea
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 27 02:14 .mcp.json
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -50 yang-2025.yaml; echo ----; head -50 yang-2025-02.yaml
```

```
# Yang, Ni, Sun, Xing, Wang, Zhang, Zhu & Xu (2025) from dandiset 001212

Tests the findings of [Yang et al. (2025)](https://doi.org/10.1109/tnsre.2025.3614867) that can be
tested on [DANDI:001212](https://dandiarchive.org/dandiset/001212/0.241023.0931), which holds 600 s,
4-channel LFP epochs around the seizures of 7 pilocarpine rats (DG, CA1, CA3, ANT), in 4 baseline
and 4 closed-loop stimulation groups per rat. The files carry no seizure or stimulation times, so
both are found from the LFP here, and every result that uses them rests on that assumption.

| Claim | Outcome |
|---|---|
| cf_w at onset is consistent within baseline groups, not between them (Table S1) | Reproduced (self-pairs reading) |
| R1's top cf_w node goes ANT, ANT, CA3, DG (Figure 2) | Reproduced |
| GC targets give 8 target and 20 non-target groups (Figure S2) | Partially reproduced |
| Target stimulation shortened seizures in every rat | Not reproduced |
| Some non-target stimulation lengthened seizures | Reproduced |
| Sites differ within R2, R3, R4, R5, R7, not R1, R6 | Partially reproduced |
| Target -0.26 against non-target 0.038 normalized duration | Not reproduced |
| Five named non-target groups shortened seizures, less than targets | Not reproduced |
| Same site as target shortens more, DG, CA3, ANT | Not reproduced |
| PSD ratio after target stimulation, alpha and theta or beta up, gamma down | Not reproduced |
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 50,400p yang-2025-02.yaml
```

```
in 6 rats with the onset thresholds 1.5 or 3; and in 2 or 3 rats with 250 Hz GC. The VAR fits are stable in
    all but 2 of 266 seizures, but their residuals are not white at the BIC order (Ljung-Box p < 0.05 in 83% of
    channel-windows at the median seizure).
  deviations:
  - Seizure onset is not in the dandiset and the paper gives no rule for it. Assumed, as reading (b) of the claims
    file's opening comment, an onset found from the LFP (1-45 Hz line length in 1 s windows, largest over channels
    of the ratio to the channel's median, above 2, with hysteresis down to 1.5); thresholds 1.5 and 3 are shown.
  - Conditional GC is computed here from OLS VAR fits (full and reduced regressions), not with the MVGC toolbox
    (Methods B, ref. 37), which obtains the reduced model by spectral factorization. Model order by BIC up to 20
    (a standard choice named in the claims file); the median order is 11 at 1 kHz. The residuals at that order are
    not white. Decimation to 250 Hz is shown as a variant.
  - The two readings of combining the 9 windows are the same number, as cf_w is linear in the GC matrix; the cf_w
    sign does not change Pearson r.
- claim: fig2-r1-target-shifts
  outcome: reproduced
  assumed: true
  notebook: reproduce_yang_2025.ipynb
  output: claim:fig2-r1-target-shifts
  notes: With cf_w as out-strength minus in-strength (reading (a)), 1 kHz GC and the main onset, the nodes with
    the highest mean cf_w in R1's four baseline groups are ANT, ANT, CA3 and DG, as named. The single-seizure top
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,700p yang-2025-02.yaml
```

```
left with trains are at their rat''s own pulse rate (a finding). Example spectrograms and traces per rat with
      onset, end and trains are added, with the comb score per group. The clock check now uses the seizure found
      without the trains: 0.989 of trains overlap it, 0.47 with a 30 s shift. Variants added: preceding baseline
      by the epoch dates, and groups with trains in most seizures. 2 to 4 of 8 target groups are below zero under
      all variants (R7 ANT -0.095 with its 3 stimulated seizures). Outcome unchanged.'
  - claim: fig3a-nontarget-can-lengthen
    agrees: true
    outcome: reproduced
    reason: 13/20 non-target groups have a positive mean (main), and 10 to 14 under the variants; the criterion
      needs 5 or more.
    response: No change; 13 of 20 after the re-run, 10 to 13 under the variants.
  - claim: fig3a-per-rat-site-differences
    agrees: true
    outcome: partially_reproduced
    reason: 5 of the 11 listed pairs are significant at the main settings, which meets the threshold of 5 exactly.
      R6 has significant pairs (DG-ANT), and R5 and R7 have none. The partial outcome is fragile. R3-07 (CA1) predates
      R3-06 by the session and epoch dates, so bi = index - 1 normalizes R3 CA1 to a later baseline; the R3 DG-CA1
      pair is one of the 5; the date-based order was not tested. Dunn tests are run even where KW is not significant
      (R5, R7); none of those reach significance anyway.
    response: 'Added the variant that takes the preceding baseline by the epoch dates (R3-07 against R3-04): 5 listed
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 50,600p yang-2025.yaml
```

```
<persisted-output>
Output too large (31.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/532c4f8c-bcde-4e72-82e9-27c2b5aeff20/tool-results/b32j3hdnd.txt

Preview (first 2KB):
#   segments of 30 min at least one hour from seizures, no visible motion artifact, 10 to 15
#   segments in early and late stages.
# - HFO (Methods E). Short line length detector of the HFO App, then manual review; six 30 min
#   interictal segments per recorded day.
# - Statistics (Methods G). Mean +- SEM; paired t-test or Mann-Whitney for two samples;
#   Kruskal-Wallis for several independent samples; alpha 0.05.
#
# Details these sources leave open, with the readings allowed, used by several claims.
# - Seizure onset and end. The paper gives no rule for marking them offline. Readings are (a)
#   seizure times deposited with the data; (b) onset and end marked from the LFP by a stated
#   amplitude or line-length rule, as an assumption. Seizure duration is end minus onset.
# - The sign of cf_w. Methods B defines it as "the difference between the weighted in-degree and
#   out-degree", but says high positive values mean strong driving and Figure 2 highlights the
#   "strongest causal outflows". Readings are (a) out-strength minus in-strength (causal outflow,
#   as the interpretation and Figure 2 imply); (b) in-strength minus out-strength, as worded.
# - GC settings. The VAR model order, the use of conditional (4-variable) against pairwise GC, any
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/532c4f8c-bcde-4e72-82e9-27c2b5aeff20/tool-results/b32j3hdnd.txt"
}
```

```
1	#   segments of 30 min at least one hour from seizures, no visible motion artifact, 10 to 15
2	#   segments in early and late stages.
3	# - HFO (Methods E). Short line length detector of the HFO App, then manual review; six 30 min
4	#   interictal segments per recorded day.
5	# - Statistics (Methods G). Mean +- SEM; paired t-test or Mann-Whitney for two samples;
6	#   Kruskal-Wallis for several independent samples; alpha 0.05.
7	#
8	# Details these sources leave open, with the readings allowed, used by several claims.
9	# - Seizure onset and end. The paper gives no rule for marking them offline. Readings are (a)
10	#   seizure times deposited with the data; (b) onset and end marked from the LFP by a stated
11	#   amplitude or line-length rule, as an assumption. Seizure duration is end minus onset.
12	# - The sign of cf_w. Methods B defines it as "the difference between the weighted in-degree and
13	#   out-degree", but says high positive values mean strong driving and Figure 2 highlights the
14	#   "strongest causal outflows". Readings are (a) out-strength minus in-strength (causal outflow,
15	#   as the interpretation and Figure 2 imply); (b) in-strength minus out-strength, as worded.
16	# - GC settings. The VAR model order, the use of conditional (4-variable) against pairwise GC, any
17	#   filtering, and how the 9 windows are combined are not given. Readings for combining are (a)
18	#   cf_w per window, then averaged; (b) GC matrices averaged, then cf_w. Model order by AIC or BIC
19	#   (the MVGC toolbox's own selection), capped at a stated maximum, is a standard choice. The test
20	#   behind "significantly high" cf_w is not given; readings are (a) the node with the largest mean
[... 448 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_yang_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"=== CELL {i} [{c['cell_type']}]")
    src=''.join(c['source'])
    if c['cell_type']=='markdown': print(src)
    else:
        print(src[:600] + ('...' if len(src)>600 else ''))
        for o in c.get('outputs',[]):
            if 'text' in o: print('OUT>',''.join(o['text']))
            elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: print('OUT>',''.join(o['data']['text/plain']))
            elif 'data' in o: print('OUT> [image]')
            if o.get('output_type')=='error': print('ERROR', o.get('ename'), o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -n "=== CELL" $TMPDIR/nb.txt | wc -l
```

```
1703 /tmp/claude-1001/nb.txt
55
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 600
}
```

```
1	=== CELL 0 [markdown]
2	# Reproducing Yang et al. (2025) from dandiset 001212
3	
4	**Paper.** Yang, Ni, Sun, Xing, Wang, Zhang, Zhu and Xu (2025), "Individualized Target Selection of
5	Closed-Loop Electrical Stimulation for the Treatment of Spontaneous Temporal Lobe Epilepsy", IEEE
6	Trans. Neural Syst. Rehabil. Eng. 33:4008-4016, doi:10.1109/tnsre.2025.3614867.
7	
8	**Dataset.** DANDI:001212, version `0.241023.0931` (doi:10.48324/dandi.001212/0.241023.0931),
9	streamed from the archive. The paper cites no version of the dandiset. This is the only published
10	version, and it is the most recent; the draft has the same 56 assets and size, so no other version
11	could match the claims file's description better.
12	
13	**Claims.** `claims/yang-2025.yaml`, written from the version of record and its supplement (Figures
14	S1 to S3, Table S1), checked by a second reader. The claims file decides what is tested; method
15	details it leaves open are taken from the paper, cited where used, and the readings it names are
16	all run.
17	
18	**What the dandiset holds.** For each of the 7 rats, 8 NWB files (4 baseline and 4 stimulation
19	groups); each file holds one 600 s, 4-channel (DG, CA1, CA3, ANT) LFP epoch per seizure at 1 kHz.
20	There are no seizure times, no stimulation times, no interictal recordings and no recording
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 600,
 "limit": 550
}
```

```
600	1 kHz                      in-out        1        0          5          3              15              17
601	                           out-in       18       12          8          4              20              22
602	1 kHz, onset threshold 1.5 in-out        2        0          5          3              15              17
603	                           out-in       16       11          7          5              19              21
604	1 kHz, onset threshold 3   in-out        0        0          8          2              12              18
605	                           out-in       17        6          7          1              23              21
606	250 Hz                     in-out        1        0          9          5              11              15
607	                           out-in       18       12          8          4              24              24
608	
609	Figure S2 labels applied to the dandiset's group order give 8 target groups by site; Figure S2's targets applied to the dandiset's order (target when the next file's site is in the preceding baseline's Figure S2 set): 9
610	
611	=== CELL 25 [markdown]
612	**Result: partially reproduced.** Under reading (a), the top node, with 1 kHz GC and cf_w as
613	out minus in, 18 of 28 baseline groups give the Figure S2 target set (R1, R3, R4 and R7 all four;
614	R2 one; R5 none; R6 one), and the labels of 20 of 28 stimulation groups agree with Figure S2 (8
615	groups are labelled target, as in the paper, but not the same 8). At 250 Hz 18 groups match and
616	24 labels agree. Reading (b), significance, matches 12 groups at most. The labels of all 28 groups
617	cannot agree under any reading: the dandiset's order of stimulated sites differs from Figure S2's
618	for R5 and R6, and Figure S2's own target sets applied to the dandiset's order label 9 groups
619	target, not 8.
[... 530 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1150,
 "limit": 560
}
```

```
1150	41              w1 paper    log2     1000  0.5-120         all  unadjusted  False  False  False  False      False       False            False
1151	42              w1 paper    log2     1000  0.5-120  stimulated  bonferroni  False  False  False  False      False       False            False
1152	43              w1 paper    log2     1000  0.5-120  stimulated  unadjusted  False  False  False  False      False       False            False
1153	44              w1 paper     rel     1000  0.5-120         all  bonferroni  False  False  False  False      False       False            False
1154	45              w1 paper     rel     1000  0.5-120         all  unadjusted  False  False  False  False      False       False            False
1155	46              w1 paper     rel     1000  0.5-120  stimulated  bonferroni  False  False  False  False      False       False            False
1156	47              w1 paper     rel     1000  0.5-120  stimulated  unadjusted  False  False  False  False      False       False            False
1157	48  w2 paper, no overlap    diff     1000  0.5-120         all  bonferroni  False  False  False  False      False       False            False
1158	49  w2 paper, no overlap    diff     1000  0.5-120         all  unadjusted  False  False  False  False      False       False            False
1159	50  w2 paper, no overlap    diff     1000  0.5-120  stimulated  bonferroni  False  False  False  False      False       False            False
1160	51  w2 paper, no overlap    diff     1000  0.5-120  stimulated  unadjusted  False  False   True  False      False       False            False
1161	52  w2 paper, no overlap    log2     1000  0.5-120         all  bonferroni  False  False  False  False      False       False            False
1162	53  w2 paper, no overlap    log2     1000  0.5-120         all  unadjusted  False  False  False  False      False       False            False
1163	54  w2 paper, no overlap    log2     1000  0.5-120  stimulated  bonferr
[... 541 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "Fig\. 5|IIS rate|paired|inset|HFO App|line length" 10.1109-tnsre.2025.3614867.txt | head -40
```

```
368:App [50], which employs the short line length detector method
372:line length of the signal [51]. The preprocessed signal is
373:divided into shorter time windows, and the short line length,
377:with short line lengths exceeding the threshold considered
417:comparing two paired samples, we use the paired T-test or
517:D. Target Stimulation Suppresses IIS Rate Short After
519:To further elucidate the mechanisms of effective electrical stimulation in epilepsy, IIS rates were analyzed 180s
521:Target stimulation significantly reduced the IIS rate within
523:(Fig. 5B). Effective electrical stimulation may modulate neural
527:During the interictal period, IIS rate at stimulated and
529:groups showed no significant differences (Fig. 5C). This suggests that the inhibitory effects of short-term closed-loop target
531:without inducing long-term neuroplasticity change. Fig. 5D
532:shows a positive correlation between interictal IIS rate and
534:IIS rate may predict increased seizure risk.
557:Fig. 5.
558:IIS rate. (A) IIS detection: 100s LFP signals in the interictal period, with detected IIS marked by red asterisks, the blue line as detection
559:threshold, and a single IIS highlighted in the gray rectangle. (B) IIS rate pre- and post-seizure. Left panel shows temporal distribution of IIS rates,
560:with each row representing IIS rate of one channel, and below is a histogram of IIS distribution across all channels. Right panel displays IIS rate
561:curves with an enlarged view in the rectangle. (C) IIS rate comparison between stimulation and non-stimulation sites. (D) Correlation between IIS
571:data are normalized to pre-stimulation data (paired T-test). Values are
[... 3 more lines not kept]
```

**Agent**

**Round 2 verifier report: yang-2025-02 (doi:10.1109/tnsre.2025.3614867, DANDI:001212 v0.241023.0931)**

The claims file has 19 claims. The attempt record gives 19 outcomes: 14 tested and 5 blocked (data_missing). Cell numbers below refer to the re-executed notebook, whose numbering differs from round 1.

### 1. Outcomes and assumptions

I agree with all 19 stated outcomes. Every tested outcome has `assumed: true`. Each states its assumption in its deviations, and each assumption is reasonable given what the dandiset holds:
- seizure onset and end found from the LFP, with thresholds 1.5 and 3 run as variants;
- stimulation trains found from the LFP artifact;
- GC from OLS VAR fits with BIC order;
- for PSD and HFO, a post window that ends at the next train, with the worded window run as a variant;
- the HFO App dialog defaults over the 600 s epoch;
- the 180 s before onset as the IIS threshold baseline.

Agreements with qualifications:
- **tables1-network-stable-short-term (reproduced):** this holds only under reading (d), self-pairs included. Under reading (c) it holds in 5 of 7 rats, which is partial (cell 20). The criterion allows reading (d), and the record states the dependence.
- **fig3a-per-rat-site-differences (partially reproduced):** this rests on the unadjusted Dunn reading and sits exactly at the threshold of 5. Bonferroni gives 4 (cell 32).
- **fig5b-iis-post-seizure (reproduced):** this rests on reading (b), the paired t-test over 30 autocorrelated time bins, which the claims file names. Reading (a) gives p = 0.0013, which is partial.
- **fig6e-ictal-ripples-no-difference (reproduced):** the absence holds under the all-channels reading only, with p = 0.061.
  - The stimulated-channel reading at the main window and threshold gives p = 0.037, and 5 of 12 readings are significant with target lower (cell 51).
  - The measure's magnitudes (+1.46 and +4.22) are far from the paper's (about −0.16 and −0.04).
  - The record states all of this.
- **Blocked claims (5):** data_missing is right for all five, as I confirmed in round 1.
- **The claims file:** I found no misreading of the paper. The R5 and R6 order conflict with Figure S2 is between the data and the paper.

### 2. Sentences the numbers do not support, or state incompletely

Almost every sentence in the conclusions, the Summary, the README and the attempt-record notes matches the printed outputs. The exceptions:

- **Cell 33, and the fig3a-per-rat-site-differences notes:** "R1 has no significant pair, but R6 has one (DG-ANT, Bonferroni p 0.037 …)".
  - This is true only after Bonferroni adjustment.
  - Under the unadjusted reading the outcome rests on, R6 has two significant pairs: DG-ANT (p = 0.006) and DG-CA1 (p = 0.0195) (cell 32).
- **Cell 44, and the fig4b-psd-target-bands notes:** "With the difference measure beta rises … (stimulated channel …), but alpha and gamma do not [differ]."
  - This is correct for 0.5–120 Hz.
  - With 0–500 Hz on the stimulated channel, gamma does hold (unadjusted; KW p = 0.036, Dunn p = 0.011 and 0.022), and cell 43 lists "beta,gamma" as holding in some reading. The conclusion does not mention this.
- **Finding on R7, attempt record and Summary:** "the spectrograms of the seizures without trains show no stimulation comb".
  - Cell 12 shows one example epoch each for R7-05 and R7-07, and none for R7-01 or R7-03.
  - Cell 11 shows 2–4 s runs at the rat's own pulse rate in 2 epochs of R7-01 and 4 of R7-03, against 4 of 267 baseline epochs. These may be trains the 4 s rule misses.
- **Deviation text (several claims):** "[the first version] missed every train of R3-07 and most of R7-01 and R5-07".
  - The R5-07 part cannot be checked here.
  - My round-1 counts did not list R5-07 among the groups with few trains.
- **Cell 43, and "72 readings" (cell 44 and the notes):** the rel and log2 measures are rank-equivalent, so they give identical KW and Dunn p values. A third of the readings are therefore duplicates. This does not change the outcome.

**My round-1 reasons in the attempt record:** they are stated in my words and are faithful. Minor omissions:
- the fig3a-per-rat reason leaves out my R6 Bonferroni p and the R5 and R7 KW p values;
- round-1 point 10 (variants the claims file does not name) appears in no reason. It did not affect a conclusion.

### 3. Round-1 points

**Resolved:**
- 1 (R3-07 order): the date-based variant now gives 5 pairs unadjusted and 4 adjusted, the same as the main reading.
- 3 (post window can include the next train): the window is now cut at the next train (48 of 228 seizures), and variants are run.
- 4 (circular clock check): the check now uses the seizure found without the trains, giving 0.989 at no shift against 0.47 at ±30 s.
- 5 (pre-window length): the distribution is printed, and a 5 s pre-window variant is run.
- 8 (Figure S2 order): the conclusion now says this.
- 9 (HFO parameters): the defaults were read from the HFO App source at commit 1ccff19. I did not verify the source.
- 2 (stimulation groups with few trains), largely resolved:
  - R3-07 now has 8 of 8 seizures with trains;
  - the baseline detections are 7 of 267, all at the rat's own pulse rate;
  - a variant keeping only groups with trains in most seizures is added.

**Remaining that bears on a conclusion:**
- **Point 6, reading (d) for tables1-network-stable-short-term:** "reproduced" holds only with self-pairs; without them the result is partial (5 of 7 rats).
- **Point 7, fig5b-iis-post-seizure:** "reproduced" holds only under the time-bin test. Seizure-channels give p = 0.0013 (partial), and with the rat as the unit p = 0.23.
- **Point 9, fig6e-ictal-ripples-no-difference:** the absence holds under one channel reading. 5 of 12 readings contradict it, and the measure does not resemble Figure 6E.
- **fig3a-per-rat-site-differences:** partial at exactly the threshold, on the unadjusted reading only. Under that reading R6 has two significant pairs.
- **New, VAR misspecification:** the residuals are non-white in 83% of channel-windows, and the median largest eigenvalue modulus is 0.993, close to instability (cell 18). The three network outcomes all rest on these fits (tables1-network-stable-short-term, fig2-r1-target-shifts and figs2-target-assignment).

**Remaining that does not change an outcome:**
- Possible missed trains in R7-01 and R7-03, described above.
- The 7 baseline seizures that carry trains stay in the sham and baseline sets; no variant leaves them out.
- Dunn tests are still run after a non-significant KW (R5, R7).

## End of run

12 turns, 3 minutes, $1.43 at API prices, result: success.
