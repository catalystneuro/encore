**Round-2 verification: Nakamuta et al. (2025), DANDI:002020 @ 0.261004.1410**

The claims file has 20 claims, and the attempt record gives an outcome for all 20: 2 reproduced, 2 not_reproduced, 16 blocked.

### 1. Outcomes

| Claim | Record | Agree? | Note |
|---|---|---|---|
| dishes-analysed | reproduced (assumed) | yes | The assumption is stated and reasonable: a missing date doesn't break a run. The result is fragile and the record says so: 7 dishes under S1/ii only, against 6, 2 or 4 under the other readings (cell 12). |
| activity-onset | blocked, metadata_insufficient | yes | Cell 5 prints "Days in vitro are unknown to this converter…". |
| fig1b-async-to-bursts | reproduced (assumed d0 = 2) | yes | The assumption is stated and reasonable. It holds for d0 = 2 to 5, O2 and O3; only d0 = 1 fails (cell 17). |
| fig1d-power-law-emerges | blocked, methods_underspecified | yes | The Poisson null gives the same b as the data, and λ₁/λ₁₀₀ never reaches about 19,930 (cells 9, 23). The claims file's quantity cannot be the paper's. |
| fig1e-example-dish | blocked | yes | |
| fig1f-transition-15div | blocked | yes | |
| fig1f-exponent-1p2 | blocked | yes | |
| fig1d-shuffle | blocked | yes | The early group has 0 to 6 recordings, mostly near silent (cell 31). |
| fig2b-spatial-structure | blocked (depends on fig2c) | yes | I withdraw my round-1 partially_reproduced, because the criterion is a conjunction. No resolution of fig2c's readings lets fig2b pass (cells 33, 39); the record says so. I could not see docs/protocol.md, so I take the dependency rule as the author states it. |
| fig2c-locality-spectrum | blocked | yes | The readings disagree: 12 of 56 hold (cell 33). |
| fig2d-locality-slope | blocked | yes | This changes my round-1 not_reproduced. The new O2/O3 readings hold under S1 M2 L1, and fig2c also holds under S1 M2 L1 O3 (cells 33, 42), so a passing combination exists. That pass rests on near-silent recordings from before onset, with 11 to 14 electrodes. |
| fig2d-shuffle-locality | blocked (depends on fig2c) | yes, with a caveat | The claim's own criterion fails in every set, because M2/L2 ratios are 0.12 to 0.73 (cell 45). It fails whatever fig2c turns out to be. |
| fig3c-avalanches-emerge | blocked, metadata_insufficient | **no → not_reproduced** | Cell 48 now covers all 56 readings. Wherever the shift is finite, the exponent is outside 1.5 ± 0.15 (1.13 to 2.53). The exponent is in tolerance only under S1 F2 (b), where 4 of 7 dishes never shift, so the median shift is infinite. No choice of DIV offset changes either fact, so the missing DIV is not what decides this claim. Cascade size as x is unambiguous here. |
| fig3d-decay-rates-correlated | not_reproduced | yes | No reading holds out of 8 (cell 52). |
| fig3ef-groups-cooccur | blocked | yes, but omission | Cell 56: under S1 F1 A2, reading (a) formally holds (p 0.0252, medians 3.7e-15 against 0.543) and so does reading (b) (pooled 6e-21 against 0.731). The Exponential group there is only 2 near-silent recordings. Neither the notebook nor the record reports this. Blocked still stands, because the readings disagree. |
| figs1-classified-by-avalanches | blocked | yes | |
| figs2-shuffle-breaks-cooccurrence | blocked | yes | |
| no-temporal-structure | not_reproduced (assumed d0) | yes | The assumption is stated, and the result holds under every d0. The effect is below one bin: the interpolated last-10 value of 0.063 s means the lag-1 autocorrelation is about 0 (cell 62). |
| fig4d-cauchy-model-power-law | blocked | yes | |
| fig4d-gaussian-model-no-power-law | blocked | yes | |

**Claims-file misreading (reported, not corrected).** The Figure 1D legend reads: "The vertical axis is the rank… The horizontal axis is the variance". The Methods say "minimize the mean squared error with respect to variance spectrum". Both conflict with the claims file's x = PC rank and favour raw-value error (F2). Cell 22 shows the rank-of-variance fit reaching the 0.1 scale. Under S2 F1 with d0 = 1 that variant meets the fig1d criterion in 4 of 7 dishes, a majority, which the record leaves unmentioned.

### 2. Sentences the printed numbers don't support

- **Cell 65 (Summary):** "the fitted b here (rank as x) is far below the paper's 0.1 boundary in every active recording, under every fit reading and fit range tried."
  - Cell 9: under F2, two active recordings are above 0.1 (23280 day 2 at 0.72 Hz, b 0.464; 23282 day 7, b 0.318).
  - Cell 22: the x/n variant gives a median b of 3.28 to 4.10.
- **README:** "far below the paper's 0.1 group boundary in every active recording". This is wrong for the same two F2 recordings.
- **Cell 0, and the record's methods_unavailable finding:** "b is about 0.001 to 0.03 in every active recording". This holds only under F1. Under F2 the median is 0.0000, 76 to 79% of b values are at the bound, and the maximum among active recordings is 0.46 (cell 9).
- **Cell 43, and the record's fig2d-locality-slope notes:** "Under L2 no reading holds: the moving average rises or does not fall significantly (Spearman -0.329 to 0.423)".
  - Cell 42 gives a range of −0.384 to 0.423.
  - S2 M1 L2 under O2/O3 falls significantly (ρ −0.384, p 0.036). That reading fails on its first value instead (0.36).
- **Cell 54, and the record's fig3d notes:** "Spearman is 0.026 to 0.217". The minimum printed in cell 52 is 0.0273.
- **Record, fig3ef notes:** "others 0.088 to 0.62". The maximum in cell 56 is 0.611.
- **Record, fig1d-shuffle notes:** the shuffle lowers c "without raising b (0.0043 against 0.0042)". That is true only for S1 F1. Under S1 F2, S2 F1 and S2 F2 the shuffle raises b significantly (Wilcoxon p ≤ 0.0004, cell 31), and the notes leave this out.
- **Missing conclusion:** fig1d-shuffle has no "**Result:**" cell. Cell 31 is followed directly by fig2c.
- **Stale text:** cells 0, 16, 32, 38, 44 and 61 still say "d0 = 1, 2, 3" or "d0 = 1 and 3"; the notebook now runs 1 to 5, O2 and O3. Cell 32 also says "the Spearman correlation does not depend on d0", which is false for O2/O3.
- **Record YAML:** the `outcomes:` key appears twice (lines 23 and 24). PyYAML accepts this; strict parsers reject it.

All other conclusion, Summary, README and notes sentences I checked match the printed outputs.

The attempt record restates my round-1 reasons faithfully and in my own terms for all 20 claims. It folds problems 3, 4, 6 to 11 and the "Not checked" items into the relevant claims.

### 3. Round-1 points

**Resolved:**
- **Problem 2:** fig3c is now complete, keeps dish 23302, and handles the never-shift case correctly.
- **Problem 3:** d0 = 4 and 5, plus per-dish O2/O3, are added.
- **Problems 4 and 5:** fig1e readings (b) and (c) and figs1 reading (b) are computed, and `fit_power` is used.
- **Problem 6:** disclosed.
- **Problem 7:** the interpolated variant, tie shares and percentiles are printed.
- **Problems 8 and 9:** bound shares are printed, there is a no-bound variant, and F2 keeps zero-count sizes.
- **Problem 10:** a per-electrode variant is added.
- **Problem 11:** both tie rules are shown, and rates are cut at 1,800 s.
- **All "Not checked" items:** the DIV text, eigenvalue ratios, avalanche readings and time-scale distributions are now printed.

**Remaining, bearing on a conclusion:**
1. **fig3c** should be not_reproduced, not blocked for metadata_insufficient. The failure does not depend on DIV (section 1).
2. **The b-scale problem (problem 1)** is raised with a reader and with the authors but is still open. Every PCA-threshold block rests on it. The "every active recording" wording overstates it (section 2).
3. **fig3ef:** the formal S1 F1 A2 pass under both readings should be reported, along with its 2-recording Exponential group.
4. **fig2d-locality-slope:** the only passing readings rest on near-silent pre-onset recordings under S1, and the record should say so as a caveat. The L2 range statement needs correcting.
5. **fig1d-shuffle:** it needs a Result cell. The notes should state that under three of four readings the shuffle does raise b significantly.
6. **Minor:** under O2/O3, the Spearman tests in fig1b, fig1f and fig2c use day instead of per-dish DIV. This is unlikely to change any outcome.
