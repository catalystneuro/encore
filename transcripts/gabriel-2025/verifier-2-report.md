# Verifier report, round 2: Gabriel et al. 2025 (doi:10.1016/j.cub.2025.01.010), DANDI:001887 version 0.260902.1724

The claims file has 43 claims and the attempt record has 43 outcomes:

| Outcome | Count |
|---|---|
| Reproduced | 12 |
| Partially reproduced | 4 |
| Not reproduced | 5 |
| Blocked | 22 |

Six outcomes are marked `assumed: true`.

## 1. Outcomes

I agree with every outcome that does not rest on an assumption. The details:

- **Unchanged since round 1, agreed:**
  - data-neurons, fig1e, fig1f, fig1kl-overall (blocked), fig1kl-day1-categories, disc-tone (blocked), fig1k, fig1q, fig1pq, fig2-day1, fig2e, fig2f, fig3a-peak-preshock, fig3c (blocked), figs3gh and zenodo-dandiset-link.
  - fig1p (partially reproduced). It is weaker than the record says; see section 2.
  - figs1h (reproduced). p < 0.05 in 4 of 5 runs; 0.143 with the paper-bout shuffles.
- **Changed after round 1, agreed:**
  - fig1g and fig1h are now blocked (methods_underspecified).
  - data-registered-cells and the two fig1o claims are now blocked (not_runnable). Cell 8 shows `ta_rois` footprints in all 30 sessions, but no registration is deposited.
  - The 13 CILDS claims are blocked (not_runnable). The notes now say the block is the software, not the data. I accept this.
  - figs2 is blocked (not_runnable). Cell 8 lists every Behavior.mat field, and none is for jumping, rearing or escape. One reservation: the escape-excited part can be computed, and if it failed it would settle the claim as not_reproduced. The record's reason for not running it ("cannot decide the claim if it holds") only covers the case where it holds.

The six assumed outcomes:

| Claim | Outcome | Assumption | Stated? | Reasonable? | Do I agree? |
|---|---|---|---|---|---|
| fig1r-mixed-exit-day1 | partially | M2 | yes | Yes. The claims file ties M2 to the code's split. | Yes. Day 1 has p < 0.05 in 1 of 5 runs (cell 58), and the difference is positive in all of them. I withdraw my round-1 "blocked". |
| fig2-day2-tone-further | partially | H1 | yes | Yes. The Figure 2C/D histograms pool cells. | Yes. Exits hold in every run; entries hold only in the main run (cells 58, 61). |
| fig3a-decoding-shock-gt-ns | reproduced | C1 N1 and clock windows | yes | Yes. The Methods code success as 1 and use min-max normalised F1. | Yes, given the assumptions, but see the open concern below. On the paper's bouts it fails with all 9 mice and in the two-class cohort (cell 69). |
| fig3a-decoding-before-tone | reproduced | same | yes | yes | Same as above. |
| fig3b-feature-cells-enhance | not reproduced | C1 N1 | yes | Yes, consistent with fig3a. | Yes. Under C1 N1, E1 and E2 both fail for K1 and K2 in all cohorts (cell 75). Under C2, K2 passes both E1 and E2. |
| fig4b-hybrid-model-best | reproduced | clock windows | yes | yes | Yes. The Methods' update (U2) also passes on both tone readings (cell 80). |

**New concern on fig3a (not raised in round 1).** Whichever class is the majority in a group gets the higher F1:
- Under C1 N1, shocked mice score 0.481 against 0.134 before the tone (−5 to 0 s), as high as in the pre-shock epoch (0.489).
- Shocked mice average 6.6 successes in 9 trials, non-shocked mice 4.3 (cell 68).
- With failure as the positive class the direction reverses: under C2 N2, 0.214 below the non-shocked mice against 0.100 above zero for them (cell 71).

So the group difference may come from the share of successes rather than from decoding. A per-mouse decoder on shuffled labels would show whether it does.

## 2. Sentences the printed outputs do not support

**fig1p seed runs.**
- Cell 47: "with three other seeds p = 0.043, 0.050 and 0.025 … the difference 5.3 to 6.5 in every run". The attempt-record notes for fig1p and its round-1 response say the same.
- Cell 46 prints its own run on three other seeds: p = 0.068, 0.039 and 0.044, differences 4.87, 5.82 and 5.31, cells 88, 78 and 89. The paper-bout run gives a difference of 4.30.
- So the differences range from 4.3 to 6.5. Across the 8 printed runs, p ≥ 0.05 in 3 (0.0501, 0.068, 0.117). The cell-46 run is not reported anywhere.

**Summary, cell 86.**
- "Every ROC, decoding and model result is shown on the paper's tone bouts too." Cells 68 and 76 say the modulated and non-modulated decoders (fig3b, fig3c) were not run on them. The README makes the same claim ("shows every result on the paper's windows too").
- "the Sidak and Fisher's LSD comparisons use t-tests corrected for the family, not Prism's pooled errors." Cell 57 computes Fisher's LSD from the ANOVA's pooled residual mean square, as the record's own deviation says.
- "the event-call counts stay below the paper's for tone onsets and platform events under every event window tried." Cell 36 shows several counts at or above the paper's:
  - Day 1 PlatEnt, non-shocked: 111/79 against the paper's 95/66.
  - Day 1 PlatExt, non-shocked: 73/62 against 66/67.
  - Day 1 PlatExt, shocked, 1 to 6 s window: 132/108 against 131/78.
  - Day 2 ToneOn, shocked: 34/34 against 34/37.
  - Day 2 ToneOn, non-shocked suppressed cells: 39 against 22.

  The gap holds only for day 1 tone onsets and day 2 shocked platform exits, which is how the record's finding words it.

**Attempt record, fig1f notes.** "the rule disagrees with the hand scoring on 26 of 358 trials … and 38 with the paper's bouts." This matches cell 26, but 358 is all trials, not the 252 hand-scored ones. Cells 11 and 13 give 24 of 252 (clock) and 36 (paper). The record's own response to round 1 says "228 of 252 agree", so the record contradicts itself.

**Cell 81 and the fig4b notes.** "With the Methods' update (U2) alpha is interior." Cell 80 shows α from 0.00 to 1.00, and α = 0 for F2, where all three models coincide. The minor ranges are also off: the multi-start rows give hybrid 0.0184 and GG p 0.0036.

**README and cell 0.** "about 35 minutes"; cell 85 prints 41.1 min. In the README table, fig3b is not marked as assumed (C1 N1).

**My round-1 reasons in the record.** They are stated faithfully, in my words. The one error is my own: for zenodo-dandiset-link I wrote "spread under 0.04 s", but cell 15 gives up to 0.050 (F7 day 1). The outcome is unaffected.

All other "Result:" sentences, the README rows and the record notes I checked match cells 7 to 84.

## 3. Round-1 points

**Resolved:**
- **Point 1, decoding cohort:** three cohorts are now run.
- **Point 3, tone windows:** the paper's bouts are now run for everything except fig3b and fig3c.
- **Point 4:** the CILDS and figs2 reasons are now stated.
- **Point 5, the R(t+1) update:** U2 is run and gives the same outcome on the clock windows.
- **Points 6 to 10:** now listed as deviations.
- **Section C:** the Behavior.mat and minian contents, the clock (label-lag) check, the event-call check, the R_t fit with several start points, and the hand-scored coding (cell 13) are all now printed.

**Still open, and bearing on a conclusion:**
- **Point 2, event-call counts.** The cause is explored but not found. It still drives fig1p's cell-count failure, the cell sets behind fig1q and disc-tone, and the mouse numbers in fig2e and fig2f (6/5 and 4/4 against the paper's 7/7 and 6/7).
- **fig1p fragility.** It is understated, as above.
- **fig3a base rate.** Without a shuffled-label control, the C1 N1 decoding difference behind fig3a-decoding-shock-gt-ns, fig3a-decoding-before-tone and the fig3b/3c baselines may reflect success rates rather than decoding.
- **fig3b and fig3c robustness.** Their cell sets use only BL-F1 and D1-P1-F1 (point 8), and the paper's bouts were not run for them. Robustness to the period and frame readings, which the claims file treats as deciding, is untested.
- **figs2.** The escape-excited part was not run, and if it failed it would settle the claim.
- **Point 5, the claims file's reading of the update.** I report this, not correct it. The claims file's R(t+1) still contradicts the Methods' formula, and under it α = 1 in every mouse (cell 80). Under U2 the hybrid model is lowest, but only just below avoid-only (0.0223 against 0.0233). The hybrid model contains both other models as special cases, and the one-way ANOVA the criterion uses does not test hybrid against avoid-only.
