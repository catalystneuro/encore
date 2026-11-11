# Verifier report, round 2: Mallory, Hardcastle et al. 2021 on DANDI:000053

**Counts.** These come from the claims file and the attempt record, not from any table. The claims file has 47 claims, and the attempt record has 47 outcomes, one per claim. The outcomes are 16 reproduced, 8 partially reproduced, 7 not reproduced and 16 blocked. Eleven outcomes are marked `assumed: true`: the ten Cohort 1 LN claims and supp9-eye.

## 1. Outcomes and assumptions

**Outcomes I agree with, and the assumptions are stated and reasonable:**
- headfixed-session-link, fig1b, fig4f, fig4j, fig4k, fig5a, fig5b, fig5-eye-position-stability, fig5av, fig6-nonlinear-temporal, fig6-eye-velocity-stability, fig7c, fig7e, supp4-eye, supp5-eye, supp7e.
- supp9-eye (assumed: reading (a); stated).
- The blocks of fig8c and fig8e, and of methods-hemispheres. For fig8c and fig8e, the trial tables are now printed (cells 13–14).

**Cohort 1 claims.** These are fig1c ×3, fig1d, fig2-shapes, fig2a, fig2b, fig2-stability, supp4-head and supp5-head. I agree with each outcome against its criterion on the printed numbers (free cells 14–44). The `assumed` statement names only readings (1a, 2a). Two further assumptions are left out:
- **Clock alignment.** The free notebook's clock check came out inconclusive (cell 7). The best lag has a median of −0.20 s for position and −0.40 s for pitch. By mouse it runs from −0.4 to +1.4 s, and only 0.18 and 0.24 of the strongest cells peak within 0.2 s. The notebook summary says the LN results "rest on the deposit's alignment", but the record does not. A misalignment would lower exactly the counts that fail: fig1c-pitch-roll (37 and 43), fig2-shapes and supp4-head.
- **Bin dropping.** Under (2a), 31% of the bins are dropped: the median kept fraction is 0.693 (cell 14). Reading (2b), clipping, would keep all of them, and the not-reproduced counts may depend on it.

**Head-fixed outcomes that depend on the fold reading, none of them marked `assumed`:**
- **fig7ab, reproduced.** This rests on reading (c) with fold 1. In the per-fold table, only fold 1 of 10 meets both parts of the rule (main cell 63). Under (1b), reading (c) with fold 1 gives 10 of 12 tests and 1 of 6 medians, and no fold meets both (folds cell 43). I agree only on the letter of the criterion ("under one reading"). The outcome should be marked `assumed: true`, and the record should say that it fails under (1b). Without that, I would record partially reproduced: the tests hold under (a) in both fold readings, with 2 of 6 medians.
- **fig5bv, partially reproduced.** Under (1b) every condition of the criterion holds (folds cell 28): KW P = 6.8e-6, linear vs higher P = 0.00024, quadratic vs higher P = 1.7e-5, and medians 0.855 and 0.838 within tolerance. The criterion's "under one reading" therefore gives reproduced. Keeping it partial means committing to (1a), which must be marked as assumed. That same commitment is what keeps fig7ab reproduced, so the two should be treated alike.
- **fig6-linear-nasal (partial) and fig6v (partial).** Both hold only under (1a). Under (1b), the nasal test gives P = 0.070 and fig6v gives neither part. The notes say so, but the flag is missing.

**Blocked claims:**
- **Cohort 2 claims (fig1c-azimuthal, fig2c ×5, fig3ab, fig3c, fig3e, supp9-head) and supp3-head as too_large.** These are acceptable on the measured estimate of about 3 h, or 3.2 h for supp3-head. However, the Cohort 1 part of fig1c-azimuthal-velocity-cells is already computed: Had = 10 cells (free cell 14), outside 12 ± 1.2. The claim can therefore be at most partially reproduced, and the record should report the 10.
- **supp3-eye.** Acceptable as a run-budget block.
- **supp12.** This needs one more head-fixed run of about 33 min. A separate notebook would fit the 60-min limit, as the 43-min readings notebook does, so the block is the run's time, not size.

## 2. Sentences the printed numbers do not support

**Attempt record notes:**
- **supp4-eye:** "within-cell 1132, 771, 1062 and 1004 … pooled 885, 410, 925 and 871" and "(pooled 0.642, 0.638, 0.752 and 0.774)". These are round-1 numbers. Main cell 75 prints within-cell 1309 and 1178 for the velocity variables, pooled 1158 and 1024, and pooled fractions 0.916 and 0.898.
- **fig5a:** "preference reading (b) and both readings of explored range give P from 0.19 to 0.23". Under the reading now called (b), cell 36 gives P = 0.104.
- **fig5b:** "preference reading (b) gives 81 of 172, P = 0.493". Cell 39 gives (b) as 82 of 172, P = 0.594; 81 and 0.493 are variant (r).
- **fig6-nonlinear-temporal:** "39 to 41 of 78 temporal (P = 0.73 to 1.0). Ev dot asymmetric cells show no preference (P = 0.08 to 1.0)". Cell 54 gives 39 to 47 of 78, and Ev dot P from 0.0026 to 1.0.
- **fig1c-azimuthal-velocity-cells:** "The Cohort 1 count needs the Cohort 1 LN model, which did not finish within the 60-minute limit". It has finished, and the count is 10 (free cell 14).
- **fig1c-azimuthal and the five fig2c, fig3ab, fig3c, fig3e and supp9-head notes:** "about an hour per reading on four cores". The same notes then say "about 3 h".
- **Timings:**
  - Cohort 1: "32.4 min" throughout. Free cell 14 prints 31.4 min.
  - supp3-eye: "2099 s" and "33 min … (1961 s)". supp12: "(1961 s)". Main cell 24 prints 1989 s.
  - README: the freely moving notebook takes "about 43 minutes"; free cell 46 prints 39.2 min.

**Notebook text:**
- **Main cell 4:** "Every freely moving claim … needs them … so they are blocked." This is stale; those claims are now tested.
- **Main cell 22:** "The other reading of detail (1) is run for the counts". The readings notebook now runs every downstream analysis.
- **Free cell 8:** "The one claim tested here, fig1b, uses the behaviour alone, so it does not depend on the clock." This is stale, and it matters now that the LN claims are tested.
- **Folds cell 59 (Summary):** "The downstream outcomes do not change direction". The same paragraph lists fig6-linear losing its nasal test, fig6v failing in both parts and fig5bv meeting its medians. Its "fig7ab holds its tests under reading (a)" leaves out that reading (c), the one recorded, fails under (1b).
- **Main cell 64 and README:** neither says that fig7ab fails under (1b).

Every other "**Result:**" sentence, both Summary sections and the rest of the README match the printed outputs.

**Round-1 reasons.** The `verifications` entry covers all 47 claims. Its reasons are faithful paraphrases of my round-1 report.

## 3. Round-1 points

**Resolved:**
- **1.** The Cohort 1 LN claims are now run. Their remaining blocks rest on a measured estimate.
- **2.** The fig8 trial tables are printed and hold no track or landmark field.
- **4.** The literal preference reading is now run. No outcome changes.
- **5.** The symmetric velocity test is now included in supp4-eye.
- **6, for supp9-eye.** It is now tested.
- **7.** The compute_llh.m log 2 factor is now printed in the notebook and raised as a question for a reader.
- **9.** The fold assignment follows create_glm.m. That function drops NaN bins rather than range-excluded bins, so the match is by analogy; it does not affect a conclusion.
- **10.** fig6 stability is now also run on the classified cells.
- **8, for fig5 stability.** Under (1b), P = 0.0376.
- **Section C items.** The cell_info fields, the code conventions and the timing are now shown.

**Remaining, and bearing on a conclusion:**
- **Point 3:** reading (2b) is still not run anywhere. On Cohort 1, (1b) is not run either, even though one reading takes about 31 min. All ten Cohort 1 LN outcomes and the not-reproduced head-fixed outcomes rest on (2a).
- **Point 8, for fig7ab:** the reproduction rests on fold 1 alone and fails under (1b). It needs `assumed: true` or a downgrade to partial.
- **fig5bv:** it is reproduced under (1b) by its own criterion. It needs to be marked assumed, or recorded as reproduced.
- **Cohort 1 clock alignment:** inconclusive and not stated in the record. It bears on fig1c-pitch-roll, fig1d, fig2-shapes and supp4-head.
- **fig1c-azimuthal-velocity-cells:** the computed Cohort 1 count (10, outside tolerance) is not reported.
- **Point 6, for supp12:** it is blocked for a single run of about 33 min that would fit a separate notebook.
- **The stale record notes listed in section 2,** chiefly those for supp4-eye and fig6-nonlinear.
