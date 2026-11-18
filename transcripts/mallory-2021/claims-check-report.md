The file is ready for an attempt (`ready: true`). I made ten corrections, each backed by the paper, and nothing is committed.

**Checker result:** `claims/mallory-2021.yaml: 42 claims, 42 quotes, 54 statistical values, 2 problems`. The two problems are p-values it could not find: P = 2.0e-7 in fig2c-velocity-extrema-near-zero and P = 8.0e-4 in supp7e-eye-velocity-extrema-near-zero. Both are printed in the Supplementary Fig. 7d/e legend, so I left them unchanged. All quotes passed.

**Changes, by claim:**
- **Opening comment:** it said 8 bins for pitch, roll and all three head velocities. The Methods give 8 bins only for pitch, roll and azimuthal head velocity. The bin count for pitch and roll velocity is now marked as not given, with 8 as a standard choice.
- **fig1c-pitch-roll-velocity-rare:** the limit was 10 of 179 for both counts, described as twice the reported count. Twice 4 is 8, so the limits are now 8 (pitch velocity) and 10 (roll velocity).
- **fig2-pitch-roll-shapes:** for roll, the criterion only asked that quadratic be the largest class. The paper says the majority of roll cells are quadratic (28 of 53), so it now asks for more than half.
- **fig2c-symmetric-asymmetric-classes, fig2c-asymmetric-direction-similar:** the paper names no test for these Z and P values. The criteria now say the binomial test is inferred from the other preference tests in the same paragraph.
- **fig4f-eye-movement-distributions:** the vertical eye velocity percentiles (−2.83 ± 0.55 and 3.15 ± 0.68, Fig. 4i legend) had been left out without a reason. I added them, put the velocity ranges in the statement, and changed the rule to seven of eight values (partial for four to six).
- **fig6v-asymmetric-more-stable:** added the horizontal eye velocity nonlinear-asymmetric median (0.94), which the statement covers. The criterion now says the medians are reported against their tolerances.
- **fig8e-joint-cells-preserve-eye-tuning:** the criterion used a signed-rank test the previous writer chose. It now uses the paper's own Fig. 8c test (two-sided rank-sum at α 0.0033) on the cells that encode both position and eye position. That is marked as a reading and an assumption, with signed-rank as a variant.
- **supp3-low-false-positives:** the criterion said "every variable". It now lists the six variables per dataset that the legend reports, which do not include pitch or roll velocity.
- **supp7e-eye-velocity-extrema-near-zero:** added the legend's entropy test (P = 1.0e-4), as the matching head velocity claim already records its entropy test.
- **supp9-correlation-contributions:** removed "follow the same order" from the statement. The paper does not say it and the criterion does not test it.

**Still open** (recorded under `checks`):
- The eight details the opening comment already lists remain unsettled by the paper or its code. They include how folds are built, how the range restriction works, how the contribution is normalised, what "explored" means, cell preference, the symmetric-cell rule, the Fig. 8 tuning curves and pooled P values.
- Eye units: the Methods say "fraction of eye width", while the Results and Fig. 4 legend use 1/100 of eye width. Reading the preset bounds as percent is an interpretation.
- The paper does not say whether the 6 Fig. 8 sessions are among the 11 landmark sessions.
- Three criteria turn words into thresholds of their own: "few", "nearly all" (as 90%) and "not falsely detected" (as at most 10%). Each criterion says so.

The paper's main findings each have a claim, and every claim comes from this paper.
