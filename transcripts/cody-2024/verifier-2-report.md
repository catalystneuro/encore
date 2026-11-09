**Round 2 verification: 001256-cody-2024-01 (Cody et al. 2024, DANDI:001256)**

The claims file has 24 claims, and the attempt record has 24 outcomes: 7 reproduced, 6 not_reproduced, 3 partially_reproduced and 8 blocked (5 methods_underspecified, 3 data_missing).

## 1. Outcomes

I agree with 22 outcomes and disagree with 2 (fig4c-wt-contrast-zx1-effects and fig4-wt-posthoc).

| Claim | Record | Agree? | Note |
|---|---|---|---|
| fig1f-tone-response-inverse-u | reproduced | yes | 318 cells; p = 1.0e-10 to 7.3e-08 and top bin 21-32 in all 32 readings (cell 12). It holds under every variant (cell 71). |
| fig1g-reliability-intermediate | reproduced | yes | p = 1.1e-09 to 6.2e-07; top bin 21-32 (cell 17). |
| fig1h-cgc-largest-intermediate | reproduced | yes | p = 2.5e-17 to 1.1e-09; top bin always interior (cell 20). |
| fig1h-cgc-evident-all-bins | not_reproduced | yes | Bin 32-43 has p ≥ 0.17 under every test (cell 22). |
| fig1i-baseline-contrast-interaction | reproduced | yes | On the readings whose counts match, p_int = 0.0061 to 0.040 (cell 25). Under the single pass p_int = 0.17, which would make it partial (cell 71). |
| fig1i-contrast-effect-intermediate-only | not_reproduced | yes | On the matching readings, both Bonferroni families flag only 54-65 (cell 27). |
| fig2b-evoked-pd-whole-drc | not_reproduced | yes, with reservation | See section 3, item a. |
| fig2c-evoked-pd-1-2s | blocked (methods_underspecified) | yes | A+B pooled trials p = 0.011; every other reading p ≥ 0.099 (cell 32). |
| fig2e-drc-responses-no-difference | not_reproduced | yes | p ≤ 7.7e-07 in all 24 readings, including C57BL6/J only (cell 35). |
| fig3b-lme-coefficients | reproduced | yes, with reservation | See section 3, item a. |
| fig3c-lme-likelihood-ratio | not_reproduced | yes | With all trials, LRT p = 0.0013 to 0.015 (cell 40). |
| fig4c-wt-contrast-zx1-effects | blocked (methods_underspecified) | **no** | Terms passing per reading: [5, 5, 4, 3]; the interaction is significant in all four (cell 43). So every reading meets the partial condition, and the readings differ only on whether the full condition holds. I read the criterion's partial clause as applying under every reading, which gives **partially_reproduced**. Blocking is a possible literal reading, but the readings agree on the partial level. |
| fig4-wt-posthoc | partially_reproduced | **no** | The criterion has no partial level. Its "solely on HIGH" part fails: ZX1 on LOW has p = 0.0496 (cell 46). The parts that hold are not robust either. Under round-1 cleaning without AA0319/AA0334, ZX1 on HIGH has p = 0.31 and ZX1 on LOW p = 0.00011, the reverse pattern (cell 71). The notes do not mention this variant. **not_reproduced.** |
| fig4f-ko-no-contrast-effect | blocked (methods_underspecified) | yes | The contrast slope is significant in 3 of 4 readings; the criterion says a disagreement between readings is methods_underspecified. |
| fig4f-ko-zx1-slope | not_reproduced | yes | 0 of 4 readings meet the criterion; KO p = 0.20 to 0.33 (cell 50). |
| Fig. 5 (3 claims) | blocked (data_missing) | yes | |
| fig6a-baseline-pd-drift | partially_reproduced | yes | As in round 1: the drift is present in both experiments, but the ACSF and ZX1 confidence intervals do not overlap. |
| fig6b-acsf-contrast-effect | partially_reproduced | yes (changed from round 1) | The intercept effect now holds under every reading (Tukey p = 2.6e-05 within ACSF) and under every cleaning variant. The slope effect fails under every reading. The criterion has no partial level, so this is accepted for consistency with fig6a. |
| fig6c-no-baseline-evoked-correlation | blocked (methods_underspecified) | yes | No listed reading matches the count of 240. D-all is significant (p = 0.00025) and the other 8 listed readings are not (cell 60). |
| methods-baseline-evoked-correlation | blocked (methods_underspecified) | yes | No reading matches both counts, and the listed readings disagree (cell 62). |
| fig6d-ko-reduced-high-contrast | reproduced | yes | b = -7.51, p = 0.00052; the fit converged with subject variance 45.4 (cell 65). Under the single pass p = 0.20. |
| discussion-zx1-wt-like-ko | reproduced | yes | 10.49 and 11.17, both within 10 ± 2.5 (cell 68). |

**Assumptions.**
- The jump rule (drop any trial whose raw trace steps by more than a factor 2 between tracked frames) is stated and has a physical rationale.
  - It is broader than the problem it fixes. `n_jumps` runs on the raw trace before the Hampel filter. It therefore also drops trials whose only fault is a single-frame spike that the filter removes: 118 trials in 15 mice, not just the runs in AA0319 and AA0334.
  - This choice moves fig4c, fig4-wt-posthoc and fig6c.
- `assumed: true` is missing from 6 outcomes: fig2c, fig2e, fig4c, fig4f-ko-no-contrast-effect, fig6c and methods-corr.
  - fig2e may not need it, since its test uses no pupil data.
  - Five of them list the cleaning assumption as a deviation and should carry the flag (fig2c, fig4c, fig4f-ko-no-contrast-effect, fig6c, methods-corr).
  - For fig4c and fig6c the outcome itself depends on the cleaning. Under round-1 cleaning fig4c would be not_reproduced (interaction p = 0.25). Under the single pass, two listed fig6c readings match the count and both are significant (p = 0.032 and 0.00095), which gives not_reproduced (cell 71).
- Group A from the `pupilPTinContrast` label is a stated, reasonable choice. Its effect on outcomes is in section 3, item a.

## 2. Text against the outputs

Almost every sentence I checked matches the printed numbers. These do not:

- **Findings, Fig. 2c question:** "Pooled trials of both groups give p = 0.0098, each group alone p = 0.12 and 0.16." These are round-1 values; cell 32 now gives 0.011, 0.099 and 0.16.
- **Findings, GCA-weights question:** "the ZnT3-WT ZX1 slope weight is -3.8 to -7.7". These are round-1 values; cell 50 gives -4.12 to -8.24.
- **Cell 28 and the fig1i-contrast notes:** "with 91 comparisons it is the only one in 13 of 16 such readings". The 16 "all" readings include the across-trials SD readings, which have 1504 or 1669 values, not the 2185 or 2304 the sentence names (cell 27).
- **Cell 55 and the fig6a notes:** "No cleaning variant gives overlapping intervals." Cell 71 checks only ZX1 reading (a) against ACSF under each cleaning.
- **Cell 27:** it labels the "all" pairing (2185 values, outside tolerance) as the "main reading", but the fig1i outcome uses the "both" pairing.
- **README:** "Several of the Figure 4 and 6 outcomes change with the cleaning." Figure 1 changes too: the fig1i interaction has p = 0.17 under the single pass (cell 71). The notebook's Summary does say this.

**My round-1 reasons in the record:** all 24 are stated faithfully in my own words, and agrees/outcome match my round-1 table.

## 3. Round-1 points

**Resolved:**
1. fig4f-ko-zx1-slope is now evaluated on its own criterion and is not_reproduced.
2. The residual artifacts in AA0319 and AA0334 are gone: maxima are now 78.3 and 70.9, the per-animal top-5 table is in cell 6, and the largest trial maximum is 3.09× its animal's median. The trial-drop rule used to get there is broader than needed (section 1).
3. fig6c and methods-corr are now decided on the listed readings only, and every cleaning variant is shown.
4. GCA fits now use several optimizers and print diagnostics. Every fit converged away from the boundary, the cell means include the intercept, and the fig6d genotype intercept now has p = 0.39.
5. A group A variant without AA0335 has been run.
6. A C57BL6/J-only variant of Fig. 2e has been run.
7. The Fig. 3 across-trials SD readings are now included.
8. A DRC structure crosstab is in cell 10. Block order is balanced, and stimDelay is 10 s only for AA0327's ZX1 trials, whose pupil dilates after that onset.
9. Added readings are marked `in_claims_file`.

Point 10 was reported only, and no fix was expected.

All the round-1 "could not check" items are done, except a comparison of the Wald z tests against lmer with Satterthwaite df. That remains a stated deviation.

**Remaining points that bear on a conclusion:**
- **a. Group A composition (fig2b, fig3b).** AA0335 is a ZnT3-WT mouse, and the paper's group A has 8 C57BL6/J mice. Without AA0335 (cell 71):
  - fig2b: group A trials give p = 0.028 while the others stay above 0.05. The readings would disagree, giving methods_underspecified instead of not_reproduced.
  - fig3b: the baseline term has p = 0.087 in the below-50% trials, which gives partially_reproduced instead of reproduced.

  The notes report both numbers, but the outcomes rest on keeping AA0335 without saying so.
- **b. fig4c** should be partially_reproduced, not blocked.
- **c. fig4-wt-posthoc** should be not_reproduced: the criterion has no partial level, the "solely on HIGH" part fails at p = 0.0496, and the result is fragile across cleanings.
- **d.** Outcomes that depend on the new trial-drop rule (fig4c, fig4-wt-posthoc, fig6c) or on the cleaning (fig6d, fig1i) need `assumed: true` where it is missing. The jump rule's reach (118 trials in 15 mice) should be stated as the reason those outcomes move.
- **e.** The two stale numbers in the findings (Fig. 2c question, GCA weights) need updating.
