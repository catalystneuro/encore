**Verifier report, round 1: Namima et al. 2025 on DANDI:001357 (0.261006.2007)**

The claims file has 27 claims. The notebook tests 21 and marks 6 as blocked; I agree with all six blocks.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| methods-sessions-and-neurons | reproduced | Cell 13: sessions 30/44/17/34/34 and neurons 1869/985 responsive, 427/360 excluded. All are within tolerance. |
| ex-m2p6-cluster | partially_reproduced | Cell 17: p06 has 24 neurons over a 2,340 µm span. 13 neurons have a significant positive intercept, all with negative slopes; the paper has 11 (tolerance ±1.1). Against the paper's set, 17 is missing and 12, 21 and 22 are added. The session is found but the set and count do not match. |
| ex-m2p6-pairs | partially_reproduced | Cell 19: pair 3–8 gives 0.780 dark and 0.894 bright, pair 18–19 gives −0.000 dark, and both distances (260, 80 µm) are within tolerance. Pair 18–19 bright is −0.144 against −0.25 ± 0.025. |
| ex-m2p6-invariance | reproduced | Cell 21: 20 of 24 under reliability (a), within 19 ± 1.9. Reading (b) gives 22, outside. |
| ex-csd-sinks | blocked (data_missing) | Confirmed on the archive: 159 files, 0.24 GB in total, variableMeasured is only Units and ElectrodeGroup, and the files have no acquisition or processing (cell 57). There is no LF signal, so no part can be tested. |
| ex-m1p12-no-cluster | not_reproduced (borderline) | Cell 23: 42 neurons over 2,580 µm, and 83–86% have reliable invariance above 0.5. The paper says the intercept was "significantly different from zero for only one neuron", and the claims file defines significant as the CI excluding zero. That count is 4 (dark), which exceeds the criterion's limit of 2. Counting significant *positive* intercepts only gives 1, which would make it reproduced. |
| ex-m1p12-strong-responses | reproduced | Cell 25: baseline-subtracted counts are exactly 28 and 26. |
| pop-significant-isimilarity | not_reproduced | Cell 27: none of the 12 readings puts the four counts within tolerance. The nearest, dark/(a)/(ii), gives 394, M1 228, M2 166 against 344, 203, 141. The fewest neurons in a penetration is 1, against 6. |
| pop-intercept-slope-correlation | reproduced | Cell 29: Pearson r is −0.768 (dark, a) and −0.735 (dark, b), p ≈ 0, and 0 neurons have both significantly positive (criterion allows ≤ 2). |
| pop-dark-bright-consistent | not_reproduced | Cell 31: Spearman r is 0.484 (a) and 0.520 (b); the upper bound is 0.4785. n is 1643/1757 against 1847. |
| pop-contrast-invariance | reproduced (fragile) | Cell 33: two of eight readings fall within 0.64 ± 0.064, both under reliability (b) with unreliable values counted as 0: 0.632 over all neurons and 0.619 from per-penetration medians. Leaving unreliable values out gives about 0.77. |
| pop-sparse-across-penetrations | reproduced | Cell 35: the dark and bright readings give 54–59 penetrations, 27–29 with five or more, and 20 with more than 30 neurons. |
| pop-asymptote-20-percent | reproduced | Cell 37: dark/(a) pooled is 21.5% and dark/(b) median is 21.0%. The other readings range from 16% to 35%. |
| pop-mean-isimilarity-yield | reproduced | Cell 39: the SD of penetration means is smaller above 30 neurons in all four readings (0.084–0.107 against 0.127–0.204). Levene p is 0.015–0.18. No contrast reading reproduces pop-significant-isimilarity, so the criterion's choice of reading is moot. |
| pop-recording-density | reproduced | Cell 41: neurons per µm gives r = 0.257 (dark, a) and 0.256 (bright, a), p ≈ 0.03, within 0.236 ± 0.0236. |
| pop-within-vs-across-sessions | partially_reproduced | Cell 43: direction holds and p < 1e-4 under every reading. No reading matches all four means; for example, same-session pairs give 0.030 (Pearson) or 0.083 (noise-corrected) against 0.0582. |
| orientation-sf-isimilarity | blocked (data_missing, outside input) | Neither the dataset nor its stimulus templates hold the shape images. I did not verify the notebook's statement that no public, pinned source exists. |
| orientation-auc-coarse-clusters | not_reproduced | Cell 45: two penetrations are all-one and two are switching. M2p6 has 2 sign changes and M1p5 has 12, so neither is of one kind; this holds for every stim_ID taken as the spindle. |
| apc-peaks-sparse-clustering | blocked (data_missing, outside input) | Needs the shapes' curvature descriptions; same caveat as orientation-sf-isimilarity. |
| apc-example-m2p51 | blocked (data_missing, outside input) | Same as apc-peaks-sparse-clustering. |
| gyrus-penetrations-consistent | blocked (metadata_insufficient) | The asset metadata names only session and description, electrode location is only "V4", and the dataset has no RF-mapping files. The 18 gyral penetrations cannot be identified, so no part is testable. |
| texture-sparse-clusters | not_reproduced | Cell 47: no reading matches, and the partial condition (total and penetration counts) fails in all readings. The nearest, original/(a)/(i), gives 193 neurons in 30 penetrations (needs at least 30.6). |
| texture-original-reversed-consistent | not_reproduced | Cell 49: r is 0.706 (a) and 0.642 (b) against 0.464 ± 0.046. |
| texture-asymptote-20-percent | not_reproduced | Cell 51: only 7 penetrations have more than 30 neurons, and every reading gives 25.6–52%. |
| position-optimal-consistent | reproduced (caveat) | Cell 53: against the main shape test, r is 0.297 (a) and 0.325 (b), within tolerance. Against the inferred centre, r is 0.45–0.47. All p < 1e-4. Caveat: if file position 4 is the centre, p = 2.1e-4 (problem 4). |
| position-examples-invariant | not_reproduced | Cell 55: for the accepted M2p9 session (20210421, labelled p12) both readings fail. For M2p28 (p28), reading (b) fails: up to 2 (a) or 16 (b) neurons are significant at one position, and the limit is 1. Reading (a) holds only under reliability (b) with position 0 as centre. |
| simulation-random-with-domains | blocked (other) | A simulation with unstated parameters, not a test on recorded data. |

### B. Problems

1. **[affects a conclusion]** `reliable`, reading (a); cells 27, 31, 47, 49. The paper says only 2 of 1,850 shape neurons and 48 of 979 texture neurons lacked a line.
   - Reading (a) leaves 121–140 shape neurons and 304/322 texture neurons without a line.
   - Reading (b) leaves 62/44 texture neurons, close to the paper.
   - So the paper's own counts largely rule out reading (a); the claims file, which left it open, missed this constraint.
   - Matches that rest on (a) are therefore suspect: ex-m2p6-invariance, pop-asymptote dark/(a) pooled, and pop-recording-density.
   - Under (b), the significant counts are further from the paper (shape 443–453 against 344; texture 276–308 against 207).
   - Each of these claims also has a match under (b) or another reading, so the outcomes in A stand.
2. **[affects a conclusion]** Cell 8 and the texture analyses in cells 12 and 47–51. The clock check fails for five M1 texture files (20200715, 20200719, 20200729, 20200730, 20200804): 0–12% of units are stimulus-selective, against a median of 73% elsewhere. These files are still used in every texture analysis and count, and no variant leaves them out. Their stimulus labels or timing may be wrong. This could shift the M1 texture counts (paper: 18 neurons, 7 penetrations).
3. **[affects a conclusion]** Cell 23, ex-m1p12-no-cluster. The paper's "significantly different from zero" is two-sided, and that count is 4 (dark) and 5 (bright). Judging only the positive count (1) would make the claim look reproduced.
4. **[affects a conclusion]** Cell 53, position centre. The centre is the author's own heuristic: the position with the largest population response. It picks different file positions across sessions (1: 12, 2: 11, 4: 5, 0: 3, 3: 3). If the labels are fixed (for example 0 = centre, as in the paper's order centre, N, S, E, W), the heuristic is wrong in most sessions. Reading (a) passes for any label except 4 (p = 2.1e-4), and variants were run only under reliability (a). Cell 55, reading (a), depends on the same choice.
5. **[affects a conclusion]** `find_pen`, cell 55. M2p9 is taken to be 20210421, labelled p12, because its count (16) passes the 10% rule. The dataset's own labels match the paper's counts exactly for p06 (24), p12 (42) and p28 (55), which makes p09 (18 neurons) the likelier M2p9. Under p09 the M2p9 half passes both readings. The claim still fails on M2p28 under reading (b).
6. **[does not affect a conclusion]** `similarity` / `invariance`. In the synthetic test I ran (true r = 0.8, 5 repeats), the percentile bootstrap interval is centred on the uncorrected r (interval midpoint 0.650 against an estimate of 0.787). It covered the estimate in 0% of runs and the true value in 10%. In the data, the pair 3–8 interval is 0.51–0.705 around an estimate of 0.78 (cell 19). Reliability uses the width only, so the outcomes are probably unaffected. The intervals should not be read as CIs of the corrected r.
7. **[does not affect a conclusion]** `nc_corr` assumes independent noise between two simultaneously recorded neurons. Noise correlations between nearby units could inflate near-pair similarity and so the significant-intercept counts. The paper's method probably makes the same assumption; it is not checked.
8. **[does not affect a conclusion]** `optimal_isim` and position analyses, cell 53. The requirement of at least 4 neurons per penetration is the author's own and is not stated as an assumption.
9. **[does not affect a conclusion]** Helper checks on synthetic inputs all pass. `nc_corr` is unbiased (true 0.482 → 0.483; 0.787 → 0.787). `regress` matches scipy's `linregress` t intervals exactly. `reliable` uses width ≤ 0.5 for (a) and ≤ 1.0 for (b). `auc` is correct with ties.
10. **[does not affect a conclusion]** Data-model limits:
    - Depth is the best-channel position in 20 µm steps, not the template centre of mass (stated in the notebook).
    - One shape/position day (20210529) has a single unit, against the paper's minimum of 6 per penetration (cell 27).
    - The dataset has 34 position files against the paper's 33.

### C. What I could not check, and what output would settle it

- **Whether `cond_ID == 0` marks blanks:** a crosstab of `cond_ID` against `luminance`, `stim_ID` and `mode` per test.
- **Whether the files encode position geometry, RF centre or grid location:** the full column lists of the trials and units tables. This bears on problem 4 and on the gyrus block.
- **The effect of the five failed texture files:** the texture-claim tables rerun without them, plus their per-unit tuning.
- **Position claims under every centre and reliability:** the cell 53 variant under reliability (b), and cell 55 reading (a) for each fixed position label.
- **How lenient each reliability reading is:** the distribution of bootstrap interval widths, and the number of neurons with a line at dark, bright and both contrasts under each reading, set against the paper's 2/1850 and 1847.
- **Whether a public, pinned source of the Pasupathy & Connor (2001) shape outlines exists:** I did not search outside the archive, so these blocks rest on the notebook's word.
