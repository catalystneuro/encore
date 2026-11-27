**Verifier report, round 1: Yang (2026) on DANDI:000363**

The claims file has 25 claims and the notebook tests all 25, with none blocked. My outcomes are 15 reproduced and 10 partially reproduced, with none not reproduced or blocked. I checked the helper functions on synthetic inputs and they behave as specified. `fractions` gives the right joint, choice and action values. `match` keeps the side and lick direction, stays within the 100 ms caliper and never reuses a control. `residual` is about 0 under the null and positive when shifted. `control_splits` gives the expected split energy. `mouse_summary` and `_side_diff` weight correctly. `decode` gives 0.52 on random labels and about 0.75 with a signal, so there is no label leakage.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| session-counts | reproduced | Cell 13: 168 photoinhibition sessions. With early-lick laser trials dropped, every region count equals Table 1 exactly (19/93, 13/48, 10/31, 16/71, 8/35). |
| table1-early-joint-fraction | reproduced | Cell 15: own,fill,licks gives 0.0549 / 0.0601 / 0.0844 / 0.0587 / 0.0521, 5/5 within tolerance, all below 0.10. Lowest is medulla, not ALM; the claim reports this but does not require it. |
| table1-early-axis-fractions | reproduced | Cell 18: 10/10 values within tolerance under both "fill" readings. |
| axes-cosine | reproduced | Cell 20, signed cosine: thalamus 0.297, ALM 0.523, and the other three regions lie between them. |
| fig1e-laser-vs-control-split | partially_reproduced | Cell 22: every mouse ratio is above 1 (minimum 1.16). ALM 147–156 and highest other 7.6–8.8 are within tolerance. Lowest other is 2.73–2.84 (striatum) against 3.3 ± 0.33, out under every reading and seed. |
| fig1-1b-corrected-joint-fraction | partially_reproduced | Cell 24: no combination of correction and reading puts both medulla and thalamus in tolerance; the nearest miss is thalamus 0.1094 against an upper bound of 0.1089. All region means are below 0.15. |
| fig1-1c-fraction-vs-neurons | reproduced | Cell 26: pooled Spearman ρ = −0.366, p = 3e-10, n = 278. |
| fig1-1d-without-video-regression | reproduced | Cell 28: thalamus 0.1158, within 0.109 ± 0.0109 and above 0.0844. Every region is below 0.15. |
| fig1b-example-session | partially_reproduced | Cell 64: ses-20200922T135318 has 130 units and joint fraction 0.0528, both within tolerance. The rule picks ses-20210419T161140 instead, by a distance margin of 0.0001 (0.00200 against 0.00210). |
| table1-decoding-early-vs-prelick | partially_reproduced | Cell 52: pre-lick accuracy exceeds early in every region, but only 7/10 values are within tolerance (6–7 across seeds; 8 needed). Early accuracies are low in ALM, striatum and medulla. Only M8 reading (b) was run (problem 1). |
| fig2a-decoding-rises-after-go | reproduced | Cell 54: the 250 ms bin is 0.721–0.782, delay bins 0.540–0.588, and the 250 ms bin is above every delay bin. Holds for both bin steps and all seeds. |
| matched-reaction-time | reproduced | Cell 34: median 0.2885 s, quartiles 0.2202 and 0.3848 s. |
| fig2d-choice-share-flat | partially_reproduced | Cell 56: early means fall outside 0.0315–0.0506 (thalamus 0.053 or 0.068, midbrain 0.0309) and striatum pre-lick (0.0248) is out. A rise beyond the SEM appears in medulla only. Midbrain's raw mean does rise (+0.006, below its SEM), so a literal "does not rise" reading would give not_reproduced (problem 5). |
| fig2e-action-share-rises | partially_reproduced | Cell 58: the rise holds in every region and medulla is largest (0.128, within tolerance). Lowest pre-lick (0.030 in thalamus) and lowest early (0.019–0.022) are out. |
| fig2b-go-aligned-joint-fraction | partially_reproduced | Cell 60, early-fraction entries: 5/5 values at 250 ms are within tolerance. Delay bins leave 0.036–0.088 (medulla 0.099 at −600 ms, thalamus 0.034–0.035) under both bin steps. |
| fig2-1-energy-outside-subspace | partially_reproduced | Cell 62: ALM peaks in the onset bin and falls after it in both readings. Reading (b) gives an onset bin of 25.8, within tolerance, but thalamus reaches 1.185 (above 1.1). Reading (a) keeps the other regions below 1.1, but its onset bin is 9.8. "Before onset" is 0.03–0.05 against 0.09 ± 0.009 in both. |
| fig3a-matched-pairs | reproduced | Cell 32: 2,667 pairs (each session counted once), median \|ΔRT\| 1.3 ms, largest 99.1 ms. |
| table1-prelick-residual | reproduced | Cell 36, closest/drop/mean: 1.552 / 1.358 / 2.912 / 0.762 / 0.528, 5/5 within tolerance, no mouse ≤ 0, for all five seeds. |
| fig3e-residual-ratio | reproduced | Cell 38: 5/5 within tolerance under both ratio readings. |
| fig3-1ab-distances-scale | reproduced | Cell 40: thalamus 20.0 above midbrain 12.07; Spearman ρ = 0.99, p ≈ 1e-216. |
| fig3-1d-matching-keeps-distance | reproduced | Cell 42: matched laser-control distance exceeds control-control in every region. Matching lowers the laser-control distance by 0.35–0.95. |
| fig3-1c-alm-early-residual | reproduced | Cell 44, on the two-50 ms-bin reading: 12.59 ± 2.00, ratio to pre-lick 8.1. On the single 20–120 ms window the claims file implies, it is 18.36, which would be partial (problem 3). |
| fig3c-residual-time-course | reproduced | Cell 46: 7/7 values within tolerance and every named peak bin holds, for all five seeds. |
| fig3c-late-residuals | reproduced | Cell 48: 5/5 regions inside the bounds at the claim seed, but only 4/5 at seeds +1000, +3000 and +4000 (problem 2). |
| fig3b-example-plane | partially_reproduced | Cell 66: the separation is smaller at Go in every variant. The plane fraction is 0.70–1.00 against 0.25 and PC1 is 0.035–0.085 against 0.04 ± 0.004; both are out. |

### B. Problems

1. **[affects a conclusion]** Cells 49/50, decoding. The markdown says no region entry passes the 40-trial / 15-per-direction rule with laser trials alone. The cell's own output says 26 entries do. So M8 reading (a), laser trials only, was never run, though it could have been for 26 entries. The Methods sentence "There is no paired trial without laser" points towards that reading. This leaves table1-decoding-early-vs-prelick (partial at 7/10), fig2a, and set (a) of fig2d/fig2e untested under one of the readings the claims file allows.
2. **[affects a conclusion]** `mam.seed`. Every random step uses `crc32("yang-2026/<claim>") + k`. The paper and the criteria name seed 17 (Methods, Statistics; claims M8 and M9, fig1e, fig3-1d). Seed 17 is never run, and the notebook does not state this as an assumption. Most results are stable across the five seeds. fig3c-late-residuals is not: it is reproduced at seed +0 and +2000 and partial at the other three.
3. **[affects a conclusion]** Cell 44, fig3-1c. The two-50 ms-bin early residual is the notebook's own reading. It rests on a Methods passage ("primary window … divided into 50 ms bins. The same pairs were scored in the early window"). The claims file does not list this as open, and its criterion ("M4, M5 window") reads as one 100 ms window, which gives 18.36. The reading is reasonable: it matches the paper's 12.6 ± 2.0 almost exactly. Still, the outcome turns on it, and the claims file misses an open detail here.
4. **[affects a conclusion]** Cell 64, fig1b-example-session. Selection is run only under the primary reading (own, fill, licks), and it is decided by 0.0001. Under the other M3/M5 readings both the ALM mouse mean and the session fractions change, so the rule might select ses-20200922T135318. Those readings were not run.
5. **[affects a conclusion]** fig2d criterion. The partial clause, "mouse-level choice fraction does not rise in at least four regions", does not say whether the SEM line applies. Midbrain rises by +0.006, less than its SEM of 0.006. The notebook's count of 4 non-rising regions uses the SEM rule. Without it the count is 3 and the outcome becomes not_reproduced. This is an ambiguity in the claims file, not a code error.
6. **[does not affect a conclusion]** Cell 11 onward. Only the early-lick-dropped reading of M1 is carried past the session counts. That follows the claims file's "best-matching combination first" rule, but reading (a), keeping them, is not run for any other claim.
7. **[does not affect a conclusion]** `decode`. z-scoring and the unit SD screen use all control trials, test fold included, before cross-validation. No labels are used, and the synthetic null gives 0.52.
8. **[does not affect a conclusion]** Cell 22. With 0 small sides, the "disjoint" and "independent" columns are the same method on different random draws, not two readings.
9. **[does not affect a conclusion]** Cell 49 markdown. "At most 67 bilateral trials and a median of 36" per session is printed by no cell.
10. **[does not affect a conclusion]** M5 "drop" reading (`axes`). Because the tongue is undetected in 82% of trials (cell 8), dropping trials without keypoints removes about 82% of control trials from the choice-axis fit, not just from the regression. That explains why the "drop" readings diverge. It is a legitimate reading of the claims file but worth knowing.

### C. What I could not check

- **Laser-only decoding:** accuracies for the 26 qualifying entries. Adding them would settle problem 1.
- **Seed 17:** results at seed 17 for the splits, folds and matching, for any claim. Above all for fig3c-late-residuals, along with which region fails at seeds +1000, +3000 and +4000; cell 48 prints only the count.
- **Example session under other readings:** the fig1b rule's selection and candidate distances under the other seven readings.
- **Bilateral trials per session:** a cell printing the per-session counts of bilateral and laser trials, to support the "67 / 36" statement.
- **The data:** I did not download it, as instructed. Every number derives from streamed arrays in cells 1–8, and the internal checks there look sound: the laser effect in ALM is in every session, the tongue detections line up with the lick times, and the onsets fall within 0.7 ms of the session median. Since no claim is blocked, no archive check was needed for step 4.
