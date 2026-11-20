# henry-2022 · verifier-2 · run 42992722315

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 684
drwxr-xr-x 6 runner runner    4096 Nov 11 10:54 .
drwxr-xr-x 7 runner runner    4096 Nov 11 10:54 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 09:08 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 09:08 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 11 10:54 .claude
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .env
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .env.development
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .env.local
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .env.production
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .env.test
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .env.test.local
drwx------ 2 runner runner    4096 Nov 11 10:54 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 09:08 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 09:08 .github
-rw-r--r-- 1 runner runner       0 Nov 11 10:54 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 09:08 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 09:08 .mcp.json
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -50 henry-2022.yaml; echo ----; head -80 henry-2022-01.yaml; ls .claude
```

```
# Henry & Kohn (2022) from CRCNS v4-2

Tests the findings of [Henry and Kohn (2022)](https://doi.org/10.1016/j.cub.2022.10.049) on
[CRCNS v4-2](https://doi.org/10.6080/K0736P4H), which holds the spike counts of the V1 and V4
populations recorded in two macaques viewing target gratings alone and amid distractors. The
receptive-field maps, the per-session coarse mapping and the waveforms are not in it.

| Claim | Outcome |
|---|---|
| 11 sessions, 22 populations, 396 V1 and 691 V4 units | Partially reproduced |
| V4 receptive fields many-fold larger (Figure 1B) | Blocked: data missing |
| Single-neuron discriminability slopes, V1 and V4, near and far (Figure 2A to 2C, four claims) | Reproduced |
| Population decoding example (Figure 2D, 2E) | Reproduced |
| V1 threshold elevation (Figure 2F) | Not reproduced |
| V4 threshold elevation (Figure 2F) | Partially reproduced |
| Pseudo-populations (Figure S3) | Reproduced |
| Noise correlations reduced (Figure 3A, 3B) | Reproduced |
| Shuffled decoding (Figure 3C) | Reproduced |
| Fano factors (Figure 3D, 3E, two claims) | Reproduced |
| V1 modulation indices (Figure 4A) | Partially reproduced |
[... 155 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "henry-2022-01.yaml",
 "offset": 80
}
```

```
80	  outcome: reproduced
81	  notebook: reproduce_henry_2022.ipynb
82	  output: claim:fig2c-farthest-spacing-slopes
83	  measured:
84	  - 0.728
85	  - 0.437
86	  notes: At 2.6 degrees V1 0.728 (0.647 to 0.798) and V4 0.437 (0.368 to 0.501), within 0.74 +/-
87	    0.08 and 0.44 +/- 0.07.
88	- claim: fig2c-v4-worse-all-spacings
89	  outcome: reproduced
90	  notebook: reproduce_henry_2022.ipynb
91	  output: claim:fig2c-v4-worse-all-spacings
92	  notes: V4 slopes 0.206, 0.297, 0.313, 0.437 against V1 0.580, 0.689, 0.641, 0.728 at 1.3 to 2.6
93	    degrees; the 95% CIs do not overlap at any spacing (reading b), and V4 is lower in each animal
94	    at every spacing.
95	- claim: fig2de-population-decoding-example
96	  outcome: reproduced
97	  notebook: reproduce_henry_2022.ipynb
98	  output: claim:fig2de-population-decoding-example
99	  notes: Monkey AL has the 84 cases (14 populations x 6 pairs). V4 with target-alone performance
[... 702 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
for fn in ['reproduce_henry_2022.ipynb','pseudo_populations.ipynb']:
    nb=json.load(open(fn))
    print('#'*20,fn)
    for i,c in enumerate(nb['cells']):
        src=''.join(c['source'])
        print(f'=== cell {i} [{c["cell_type"]}]')
        if c['cell_type']=='markdown':
            print(src)
        else:
            print(src if len(src)<1500 else src[:1500]+'\n...[src truncated]')
            for o in c.get('outputs',[]):
                if 'text' in o: print('--OUT--\n'+''.join(o['text']))
                elif 'data' in o:
                    d=o['data']
                    if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain'])[:3000])
                    else: print('--OUT-- [',list(d.keys()),']')
                elif o.get('output_type')=='error': print('--ERR--',o.get('ename'),o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -n '=== cell' $TMPDIR/nb.txt | wc -l
```

```
2744 /tmp/claude-1001/nb.txt
102
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	#################### reproduce_henry_2022.ipynb
2	=== cell 0 [markdown]
3	# Reproducing Henry & Kohn (2022) from CRCNS v4-2
4	
5	**Paper.** Henry CA, Kohn A (2022). Feature representation under crowding in macaque V1 and V4
6	neuronal populations. Current Biology 32, 5126-5137. doi:10.1016/j.cub.2022.10.049. The claims
7	file `claims/henry-2022.yaml` was written from the version of record (main text, STAR Methods
8	and Supplemental Information, as extracted from the PDF).
9	
10	**Dataset.** CRCNS v4-2, "Simultaneous extracellular recordings from visual areas V1 and V4 from
11	macaque monkeys viewing crowded displays" (doi:10.6080/K0736P4H), the paper's deposit. Files are
12	streamed from the public S3 bucket `crcnsarchive` under `v4-2/live/`; the zip is opened in place
13	and nothing is written to disk.
14	
15	**Version.** CRCNS data sets are not versioned (docs/archives.md), and the paper cites the data
16	set by its DOI only, so the version pinned is the one published under `v4-2/live/` (the bucket
17	holds no other), recorded as `unversioned`. Its data description is version 0.7 (9 Nov 2022). The
18	MD5 sums from the data set's `checksums.md5` for the files read are: `data.zip`
19	bdd60f999b997523151b9ae24a42b837 (checked against the bytes read, below) and
20	`docs/crcns_v4-2_data_description.pdf` 40f2f30456a87ad3999e8a929a424220.
[... 680 more lines not kept]
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
700	first, and the residuals do not reveal the pairing (data check), so reading (b) cannot be formed.
701	=== cell 19 [code]
702	RSC = {}
703	for area in AREAS:
704	    RSC[(area, None)] = np.concatenate([cw.pair_rsc(p, "alone") for p in pops(area)])
705	    for s in SP:
706	        RSC[(area, s)] = np.concatenate([cw.pair_rsc(p, "crowd", s) for p in pops(area)])
707	rows = []
708	for area in AREAS:
709	    a0 = RSC[(area, None)]
710	    for s in [None] + list(SP):
711	        x = RSC[(area, s)]
712	        ok = np.isfinite(a0) & np.isfinite(x)
713	        t = stats.ttest_rel(a0[ok], x[ok]) if s is not None else None
714	        rows.append(dict(area=area, condition="target alone" if s is None else SPL[s], pairs=len(x),
715	                         pairs_finite=int(np.isfinite(x).sum()), mean=np.nanmean(x),
716	                         sem=np.nanstd(x, ddof=1) / np.sqrt(np.isfinite(x).sum()),
717	                         paired_t=None if t is None else t.statistic, p=None if t is None else t.pvalue,
718	                         n_paired=int(ok.sum())))
719	f3 = pd.DataFrame(rows)
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
1400	31  single      1000   V4     2.6  244      0.910   0.884    0.931         0.437            0.480
1401	
1402	affine, trials recorded: V4 simulated slope below V1 at every spacing: True
1403	   measured_all     V1: simulated at or below measured at 4 of 4 spacings
1404	   measured_all     V4: simulated at or below measured at 3 of 4 spacings
1405	   measured_fitted  V1: simulated at or below measured at 4 of 4 spacings
1406	   measured_fitted  V4: simulated at or below measured at 4 of 4 spacings
1407	affine, trials 1000: V4 simulated slope below V1 at every spacing: True
1408	   measured_all     V1: simulated at or below measured at 4 of 4 spacings
1409	   measured_all     V4: simulated at or below measured at 1 of 4 spacings
1410	   measured_fitted  V1: simulated at or below measured at 4 of 4 spacings
1411	   measured_fitted  V4: simulated at or below measured at 3 of 4 spacings
1412	
1413	=== cell 51 [markdown]
1414	**Result: reproduced, under reading (a) of both open details (recorded trial counts, Figure 2C
1415	slopes over all neurons).** The simulated V4 slope is below the V1 slope at every spacing (0.243
1416	to 0.336 against 0.404 to 0.567), and the simulated slope is at or below the measured one at 4 of
1417	4 spacings in V1 and 3 of 4 in V4 (V4 at 1.3 degrees: 0.243 against 0.206). With 1000 trials per
1418	stimulus V4 is at or below the measured slope at only 1 of 4 spacings over all neurons (3 of 4
1419	against the fitted neurons' own slopes). On the random-split selection (below) the simulated V4
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 2100,
 "limit": 650
}
```

```
2100	
2101	=== cell 77 [markdown]
2102	With no crowding the estimate is biased upward: its mean is 1.17 to 1.18 in V1 (5th to 95th
2103	percentile 1.07 to 1.29) and 1.09 in V4 (1.02 to 1.16), because points near chance enter the fit
2104	by noise. The permutation nulls lie above 1 for the same reason, with medians of 1.37 to 1.63 in V1
2105	and 1.75 to 4.16 in V4 (main run), so each estimate is tested against a null with the same bias.
2106	
2107	=== cell 78 [code]
2108	for (mode, nt), d in TH[TH.area == "V1"].groupby(["mode", "ntrials"], sort=False):
2109	    k = d.set_index("spacing")
2110	    vals = abs(k.loc["1.3", "k"] - 1.31) <= 0.10 and abs(k.loc["2.6", "k"] - 1.15) <= 0.08
2111	    sig = [bool(k.loc[x, "p_perm"] < 0.05) for x in ("1.3", "1.6", "2.1", "2.6")]
2112	    print(f"{mode:6s} n={nt:4s}: V1 closest {k.loc['1.3', 'k']:.3f} +/- {k.loc['1.3', 'sem']:.3f}, farthest "
2113	          f"{k.loc['2.6', 'k']:.3f} +/- {k.loc['2.6', 'sem']:.3f}; values within: {vals}; p < 0.05 at 1.3, 1.6, 2.1, 2.6: {sig}")
2114	--OUT--
2115	main   n=fold: V1 closest 1.685 +/- 0.351, farthest 1.669 +/- 0.314; values within: False; p < 0.05 at 1.3, 1.6, 2.1, 2.6: [False, False, True, False]
2116	main   n=all : V1 closest 1.685 +/- 0.331, farthest 1.669 +/- 0.428; values within: False; p < 0.05 at 1.3, 1.6, 2.1, 2.6: [False, False, True, False]
2117	folds5 n=fold: V1 closest 1.738 +/- 0.312, farthest 1.517 +/- 0.265; values within: False; p < 0.05 at 1.3, 1.6, 2.1, 2.6: [False, False, False, False]
2118	folds5 n=all : V1 closest 1.738 +/- 0.295, farthest 1.517 +/- 0.226; values within: False; p < 0.05 at 1.3, 1.6, 2.1, 2.6: [False, False, False, False]
2119	
[... 626 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
d=yaml.safe_load(open('henry-2022.yaml'))
print(len(d['claims']))
for c in d['claims']:
    if c['id'] in ('fig2de-population-decoding-example','fig5-terms-covary','fig5de-simulated-discriminability','figs6-common-neuron-pool','fig4b-v4-modulation-indices','fig5bc-tuning-model-terms','fig2f-v1-threshold-elevation','fig4a-v1-modulation-indices','data-populations','figs3-pseudo-populations'):
        print('=====',c['id']); 
        for k,v in c.items():
            if k not in ('id','quote','source'): print(k,':',v)
"; python3 -c "
import yaml
d=yaml.safe_load(open('henry-2022-01.yaml'))
print(len(d['outcomes']), [o['claim'] for o in d['outcomes'] if o.get('assumed')])
import collections; print(collections.Counter(o['outcome'] for o in d['outcomes']))
print(set(c['id'] for c in yaml.safe_load(open('henry-2022.yaml'))['claims'])^set(o['claim'] for o in d['outcomes']))
"
```

```
32
===== data-populations
statement : Eleven sessions gave 22 neuronal populations in each area, of on average 19 +/- 1.9 V1 neurons and 31 +/- 3.4 V4 neurons, 396 V1 and 691 V4 neurons in the single-neuron analyses.
expected : [{'quantity': 'sessions of the distractor-spacing experiment', 'value': 11, 'tolerance': 0}, {'quantity': 'populations per area', 'value': 22, 'tolerance': 0}, {'quantity': 'mean V1 population size', 'value': 19, 'tolerance': 1.9, 'unit': 'neurons'}, {'quantity': 'mean V4 population size', 'value': 31, 'tolerance': 3.4, 'unit': 'neurons'}, {'quantity': 'V1 neurons', 'value': 396, 'tolerance': 40, 'unit': 'neurons'}, {'quantity': 'V4 neurons', 'value': 691, 'tolerance': 69, 'unit': 'neurons'}]
criterion : Counts are exact for sessions and populations. The selection is the Methods' one, "responses ≥ 1 s.d. above spontaneous rate", to the targets in isolation. The Methods do not say which response is compared (the mean over all isolated targets, or the best target) nor how the spontaneous rate and its SD are measured; the readings are (a) the mean count to the isolated targets against the mean plus 1 SD of the spontaneous count, (b) the largest of the per-orientation means against the same. Population sizes are tolerated by the reported SEM and neuron totals by 10%; the claim is reproduced when every value holds under one reading. The per-animal neuron counts of Figure S7 (V1 264 and 132, V4 288 and 403; which animal is which could not be read) are reported too.
===== fig2de-population-decoding-example
statement : In one animal at the nearest spacing, V4 population decoding performance with distractors tends to be lower than for targets alone when performance is above chance (p < 0.001), while in V1 the loss is not significant (p > 0.05).
statistics : [{'about': 'V4, target alone against with nearest distractors', 'p': 0.001, 'p_relation': '<', 'n': '84 cases (pairings of target stimuli across sessions), one animal'}, {'about': 'V1, target alone
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -B2 -A8 "Figure S6" 10.1016-j.cub.2022.10.049.txt | head -60
```

```
716-0.13 versus 0.67 ± 0.05, p = 0.002, paired t test). In additional analyses, we confirmed that the distinct decoding axes in V4 for
717-different displays do not arise from relying on distinct subsets
718:of neurons (Figure S6). Thus, changes in V4 representation
719-across displays do not result from dramatic changes in which
720-neurons were relevant for encoding target orientation but rather
721-from changes in the tuning of a common underlying pool of neurons between conditions.
722-In summary, V4 populations exhibit a more configurationdependent representation of target orientation than V1 populations. Thus, not only does V4 show a greater loss of stimulus
723-−9 −3
724-3
725-9
726-20
--
870-slightly along abscissa for visualization.
871-(D) Average V4 discriminability, same conventions as in (C).
872:See also Figure S6.
873-normalization mechanisms (which act divisively).34,35
874-The combination of additive facilitation and divisive
875-suppression would be expected to yield a ‘‘flattened’’
876-tuning curve, as we often observed.
877-In V4, neuronal receptive fields are a few-fold larger
[... 15 more lines not kept]
```

**Agent**

**Verifier report, round 2: Henry & Kohn 2022 on CRCNS v4-2**

The claims file has 32 claims and the attempt record has 32 outcomes, one per claim: 19 reproduced, 8 partially reproduced, 2 not reproduced and 3 blocked. Three of them are marked `assumed: true`: data-populations, fig5-terms-covary and fig5de-simulated-discriminability. A correction to my round-1 report: its opening sentence gave the counts as 17, 9, 3 and 3. That was wrong. My own round-1 table gives 19, 8, 2 and 3, the same as the record.

### 1. Outcomes and assumptions

I agree with all 32 outcomes. Each one follows from the claims-file criterion and the printed values.

The three assumptions are stated, and all three are reasonable:
- **data-populations:** It takes the blank epochs as the spontaneous condition, which are the only spontaneous data the files hold. The outcome is partial whichever way this goes, because the rule cannot regenerate 396 and 691 under either reading (cell 13).
- **fig5-terms-covary and fig5de-simulated-discriminability:** Both use the single even/odd split in stored order rather than the reliability averaged over 20 random splits (`REL_R`). That is the closer match to the paper's rule, which uses one split. Its counts also sit inside the range of single random splits (V1 143.8, range 126 to 163; V4 238.3, range 219 to 256; cell 38).
- The reason for each assumption is stated in the record and in the methods_unavailable finding.

Other outcomes rest on a reading the criterion allows; this is disclosed each time:
- fig2de uses V1 without the >0.5 restriction (cell 72).
- fig4b uses the t tests on log indices (cell 28).
- figs6 computes the driven fractions on 10 of 22 populations (cell 65).

### 2. Sentences the printed numbers do not support

- **Cell 77:** "The permutation nulls lie above 1 for the same reason ... so each estimate is tested against a null with the same bias." The no-crowding calibration has a mean of 1.17 in V1 and 1.09 in V4 (cell 76). The permutation null medians are 1.37 to 1.63 in V1 and 1.75 to 4.16 in V4 (cell 75). The null is shifted far more than the calibration, so "the same bias" is not shown. The fig2f-v1 sentence "near the medians of their permutation nulls" (cell 79, and the record notes) is accurate as stated, but it inherits this problem (see section 3).
- **Record, fig4a notes:** "each set with one value outside tolerance". Under within-orientation pooling at 2.6 degrees, both values are outside: 2.0 against 2.25 to 2.75, and 14.4 against 11.7 to 14.3 (cell 26). Cell 27 itself says "each far value misses by one neuron". Only the all-orientations pooling has one value out (1.8 out, 12.9 in).
- **Cell 66 and record, figs6:** "The fraction driven by targets (0.372 and 0.396, over the 22 populations) is in the range of Figure S6A, 0.3 to 0.5." Those means include the 12 populations in which no unit can be driven (cell 65: "Populations with no target-driven neuron: 12"). Over the 10 usable populations the same numbers give about 0.82 (V1) and 0.87 (V4), which is above S6A's range. So the agreement comes from averaging in 12 zeros.
- **Cell 66 and record, figs6:** "where any unit responds above the epochs labelled blank; in the other 12 no unit does". Cell 10 shows that 8% to 86% of V1 units and 23% to 75% of V4 units in those sessions do have a target-alone mean above their blank mean. What holds is that no unit exceeds the blank mean plus 1 SD.
- **Summary (cell 89):** "both are properties of the method as the paper describes it, not choices made here". This is said of both the decoders that keep no nonzero coefficient and the upward bias of the estimate. For the decoders it does not hold. The all-zero rate depends on the penalty grid's lower bound, C = 0.01, and the same paragraph lists that grid among the choices made here.
- **Record, methods_unavailable (5):** "5% to 18% of the decoders here have no nonzero coefficient". The printed fractions are of outer folds, not of decoders (cell 69).
- **Record, metadata_error finding:** "blank and distractor-only ... same mean counts as the target epochs (mean z against blank −0.18 to 0.16)". That range is for the target-alone z only. The distractor-only z in those sessions spans −0.29 to 0.37 (cell 9). This is minor.
- **README:** The table gives fig5-terms-covary and fig5de as "Reproduced", with no note that they rest on the even/odd selection. The notebook summary does carry that note.

Every other sentence I checked matches its output. That covers every "**Result:" cell, the Summary sections of both notebooks, the README, and the record notes. I recounted a sample by hand:
- fig7cd: 17 of 22 V1 and 16 of 22 V4 populations below the paper's means.
- fig5de: 3 of 4 spacings, and 1 of 4 with 1000 trials.
- fig4a: neuron counts 8 and 57, against 9 or 10 and 47 to 56 allowed.
- fig2f-v1: permutation p ranges.
- figs3: the closest pass, 0.52 against 0.63.

Round-1 reasons: the record gives my round-1 reasons nearly word for word, in my own words. Where a round-1 problem was merged into a reason, it is folded in accurately: B4 into fig4a, B2 into fig5bc, B1 into figs6, B10 into figs5, B3 into fig2de. "Agrees with all 32 outcomes" is correct.

### 3. Round-1 points

Resolved:
- **B1:** figs6 now says it covers 10 populations.
- **B3:** disclosed; the outcome still depends on that reading, which the criterion permits.
- **B4:** referred to `questions/henry-2022.yaml`.
- **B5, B6, B8, B9, B10, B11:** resolved. The wide grid shows the main run is not censored. The NaN null draws were 0% to 0.15% and changed no percentage. figs3 with 20 draws still passes 7 of 8 pairs. The point-slope check and the lower-first variant are in.
- **B2:** resolved as disclosure. The variant on random-split reliability was run for every tuning-model claim, and the two claims that change under it are marked assumed.
- **Section C:** every item was done. The contrast table is in cell 10. The `REL_R` fits are in cell 56. The null percentiles and the calibration are in cells 75 and 76. The decoder diagnostics are in cell 69. The fig7cd values per population are in cell 87. figs3 now uses 20 draws.

What remains that bears on a conclusion:
1. **fig2f-v1 (significance part) and fig2f-v4:** The permutation null is not calibrated. Its V1 medians (1.37 to 1.63) sit well above the no-crowding estimate (95th percentile 1.26 to 1.29). Judged against the calibration, V1 at 1.3 degrees (1.685) would count as significant. So the V1 significance pattern says little in either direction. The outcome stays not reproduced, because the values fail.
2. **fig2f, fig3c, figs3 and fig7cd values:** In 5% to 18% of folds the chosen decoder has no nonzero coefficient and predicts one class (cell 69). That pulls crowded performance toward chance and plausibly inflates k, for example V4 CA 10.9 and 18.5. The binomial calibration cannot capture it. Its effect on k and d′ was not measured, for instance by re-running with a grid that never leaves zero coefficients. This does not change any outcome: the values already fail, and the comparison in fig3c is internal. It bears on the "differs from the paper" reading.
3. **fig5-terms-covary and fig5de:** Only the decoder counts were shown across the 20 single random splits. V4 r and the fig5de comparison were not. Those two outcomes therefore rest on one particular split. Under `REL_R`, V4 r is −0.459 and V4 meets the fig5de comparison at 1 of 4 spacings, so both would fall below the criterion. Showing the distribution of r and of the fig5de count over single random splits would settle whether the stored-order split is typical.
4. **The section 2 wording errors:** the fig4a notes, the figs6 S6A comparison and its "no unit responds" wording, cell 77, and the Summary's "not choices made here". None of them changes an outcome, but each should be corrected.

## End of run

11 turns, 3 minutes, $1.66 at API prices, result: success.
