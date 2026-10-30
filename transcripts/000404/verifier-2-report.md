**Round 2 verification: Athalye et al. 2023 (Curr Biol) on DANDI:000404 0.230605.2024**

The claims file has 29 claims and the attempt record has 29 outcomes: 20 reproduced, 6 partially reproduced, 1 not reproduced, 2 blocked.

## 1. Outcomes

I agree with 28 of the 29 outcomes and with figs5f's blocked status only conditionally (below).

| Claim | Outcome | Agree | Basis (cell) |
|---|---|---|---|
| conditions-per-session | reproduced | yes | 17 |
| figs1b-conditions-per-command | reproduced | yes | 20 |
| figs1d-command-subtrajectories-differ | reproduced | yes | 23 |
| figs1e-next-commands-differ | partially | yes | 23: G 1.873 > 1.844 |
| fig3d-population-distance | reproduced | yes | 26 |
| fig3b-single-neuron-distance | reproduced | yes | 28 |
| fig3e-fractions-significant | partially | yes | 30: at best 4/6, which matches the partial clause |
| fig4c-dynamics-predict-activity-given-command | reproduced | yes | 35 (code reading) |
| fig4de-condition-specific-activity-predicted | reproduced | yes | 46 |
| fig4f-condition-specific-component | partially | yes, as a judgment | 48. The criterion has no partial clause. |
| fig4g-majority-predicted | reproduced | yes | 50 |
| figs3-low-dimensional-decaying-dynamics | not reproduced | yes | 53: G4 has 5, J3 decoder-null has 1, G frequencies outside |
| fig5c-next-activity | reproduced | yes | 41: code reading, decoder-null G 8/9 (G1 p=0.007) |
| fig5d-four-dimensions | reproduced | yes | 56 |
| fig5e-next-command | partially | yes | 43 (see below) |
| fig5f-condition-specific-next-command | reproduced | yes | 59 |
| fig5h-turn-predicted | partially | yes, as a judgment | 61: sign test 7/9 G. A test fails, which no clause covers. |
| figs5b-dynamics-beyond-behavior | reproduced | yes | 64 |
| figs5f-nonlinear-no-better | blocked (not_runnable) | conditionally | not run (see 3) |
| figs3f-residual-early-late | reproduced | yes | 67 |
| figs4b-generalize-command-sets | reproduced | yes | 37: angle J 3/4, J3 p=0.321 |
| figs4g-generalize-condition-classes | reproduced | yes | 39: all classes 9/9 and 4/4 under the code reading |
| figs6cd-pairwise-distances-predicted | reproduced | yes | 70 |
| figs6g-distance-tracks-behavior | reproduced | yes | 72 |
| figs6k-next-command-pairs | reproduced | yes | 74 |
| fig6c-dynamics-reduce-input | reproduced, assumed | yes | ofc 8 and 14 |
| fig6d-decoder-null-dynamics-no-saving | reproduced, assumed | yes | ofc 8 (see below) |
| fig6g-ofc-uses-distinct-patterns | partially, assumed | yes | ofc 11 and 14 |
| monkey-j-linear-command | blocked (data_missing) | yes | 77. The criterion says blocked when the PPF update and parameters are absent. |

**fig5e.** Under the code reading every R² is within tolerance, but the condition-left-out pooled test for J gives p=0.003. The claim's statistics need p<0.001. Under the "analysed" reading the tests hold and J's R² are outside tolerance, which matches the partial clause exactly. So partial is defensible under either reading.

**The code reading of scored pairs (fig4c, fig5c, figs4b, figs4g).** It is not marked as assumed. That is acceptable for two reasons:
- It is cited to the paper's code, and the claims file takes code citations as written.
- The shuffle 95th percentiles under this reading match Table S1: 0.1282 and 0.1963 against 0.130 and 0.196 (cell 35), and 0.0543 and 0.0527 against 0.055 and 0.053 (cell 41).

fig5c's outcome rests on this reading. Under the other two readings decoder-null G is 7/9. For fig5e, J's shuffle 95th percentile (0.2083) matches Table S1's 0.188 less well.

**The assumed outcomes (fig6c, fig6d, fig6g).** The assumption is Monkey J's 100 ms decoder, fitted by least squares. It is stated, and it is reasonable: it accounts for 0.995–0.998 of the velocity, against 0.984–0.994 for the summed 5 ms gain. It carries weight only for fig6d. Under the summed-gain reading, J1's Wilcoxon test gives p=0.0016, and fig6d's criterion would then say not reproduced. The record discloses this.

## 2. Sentences the numbers do not support

- **Attempt record, fig3e notes:** "Every combination of readings puts four of the six fractions within tolerance". Cell 30 shows 3 within tolerance for the shuffle null with neurons over significant tuples, at both min_conds values. Cell 31 ("Under the best combinations") is correct.
- **Cell 7:** "the linear map accounts for 98.7 to 99.6%". Cell 6 gives 0.9889–0.9957, so 98.9 to 99.6.
- **ofc_simulations cell 4:** "variance accounted for 0.98 to 1 on the updates". Cell 3 has G2 vel_y at 0.96672.
- **ofc_simulations cell 9 and fig6d notes:** "under that reading the absence … holds only in part". fig6d's criterion has no partial outcome: a single session's Wilcoxon p<0.05 means not reproduced. Cell 15's "fails in one Monkey J session" is accurate.
- **Cell 54 and figs3 notes:** "leaves every count … unchanged". The Hz variant (cell 53) refits only the full model, so this holds for the full-model counts only.

Everything else checks against the outputs: every other "Result:" conclusion, both Summary sections, the README table and text, and all remaining record notes and findings. The README and both summaries agree with the record's 29 outcomes.

The record states my round-1 reasons faithfully, in my own words, with the problems folded into the right claims. One of those reasons was my own error: I said J3 falls below 0.18 under both readings of fig4f. Under reading (b) it is 0.196 (cell 48). The record's notes have it right, and the outcome does not change.

## 3. Round-1 points

**Resolved:**
- **Problem 1:** every model is now scored against the shuffle on its own pairs, the code's reading is the main one, and it is corroborated by Table S1.
- **Problem 2:** monkey-j is now blocked as its criterion directs, with the rewarded-trial and no-offset readings shown.
- **Problem 4:** the code's pairwise matching is used and the regression is predicted on true; slopes match the paper (0.225, 0.301, 0.357, 0.434 against 0.221, 0.317, 0.350, 0.449).
- **Problems 5, 6 and 9:** each has its variant computed.
- **Problem 7:** answered by citing the code, which does the same.
- **The Monkey J decoder sensitivity run for fig6:** done.

**Accepted unchanged (no effect on a conclusion):** problems 8 and 10.

**Remaining, bearing on a conclusion:**
1. **figs5f is still untested.** The blocker is a build-isolation failure installing `ssm`, not missing data. I cannot verify that failure. By the record's own estimate the 4 J sessions take about 3 h on one core. A standard workaround (installing without build isolation, or with Cython and numpy pre-installed) would let at least J and the code's G subset be tested.
2. **fig6d depends on the J decoder reading.** Under the summed 5 ms gain it would be not reproduced. The fitted reading is reasonable, but the outcome is fragile.
3. **fig5c depends on the code's scored-pair reading.** Under the other readings decoder-null G is 7/9. I cannot check the code citation itself, though the Table S1 match supports it.
4. **Unchanged from round 1, cannot be checked here:** Monkey J's condition classes, its fixed clockwise labels and the outside target list (`jeev_obs_positions_from_amy.mat`). They affect conditions-per-session, figs4g and every Monkey J tuple analysis.
5. **Partial verdicts the criteria do not provide for:** fig4f (no partial clause at all) and fig5h (a test fails with values in tolerance; the partial clause covers only the reverse). Both are the author's judgment, which I agreed with in round 1 and still do.
