**Round 2 verification: Hulsey et al. 2024 on DANDI:000678 (0.231004.2146)**

The claims file has 29 claims. The attempt record has 29 outcomes: 19 reproduced, 8 partially reproduced, 1 not reproduced and 1 blocked (data_missing). Only one outcome is marked `assumed: true`, fig2a-state-types.

**1. Outcomes**

I agree with all 29 stated outcomes. Two outcomes changed since round 1, and both changes are justified by the re-fit, which now uses 10 cross-validation initialisations and the corrected visual inputs.

- **fig2b-optimal-occupancy, now reproduced.** Indeterminate is 13.1 ± 1.6% and all three Wilcoxon p = 0.00024 (cell 23). The criterion is met.
- **fig3f-movement-index-inverted-u, now reproduced.** r² is 0.5737 under (a), inside [0.57, 0.69]. The shape holds (vertex 0.28) and p = 0.216 against pupil (cells 45, 49). The margin is 0.004, but the mean over 10 splits, 0.573, is also inside (cell 46).

The other outcomes I checked against the criteria:
- figs2-n-states stays reproduced by the criterion's range rule, although the expected largest count of 5 ± 0.5 is not reached (largest is 4). The notes say so.
- fig2c and figs4 remain partial for the reasons the notes give.
- fig5c-movement-index-best: the main reading gives 68.6 against 71.5%, p = 0.086, so the movement index does not exceed pupil and the claim is not reproduced.

The fig2a assumption is stated in the conclusion, the notes and the deviations, and it is reasonable. BW059's state 2 has no trial with posterior ≥ 0.8 in the sessions with the optimal state, so it is typed on all sessions. The outcome does not hinge on it: BW059 also has a typed avoid-left state, so the criterion holds either way.

fig3e now defines stationary as |speed| < 0.02. The claims file's reading (b) is signed speed < 0.02. The change is listed as a deviation and both rules give the same result (cell 42), so it needs no `assumed` flag.

**2. Statements the printed numbers do not support**

- **Cell 27 (fig2c):** "The dwells are longer than the paper's 37 and about 15 under every reading". This is wrong for the disengaged dwell. Cell 26 gives 14.0 under (a)(y), 13.8 under (a)(x) and 14.2–14.6 under (c), all at or below 15 and within tolerance. The attempt record's notes state this correctly, and the outcome is unaffected.
- **Cell 43 and the fig3e notes:** "Reading (a), speed exactly 0, leaves 1,821 trials". Cell 42 prints 1879 trials.
- **Cell 47 and the figs4 notes:** "locomotion speed gives 0.567 under (a)", also listed under `measured` as 0.567. Cell 45 prints 0.5700 ± 0.0854. It is outside tolerance either way.
- **Cell 90 and the figs7 notes:** "68.1% for locomotion speed (higher on average, p = 0.053)". Cell 89 prints p = 0.051.
- **figs8a notes:** "p below 0.001, 0.001…" for the optimal L*L weight. Cell 80 prints 0.001 at three decimals, which does not show it is below 0.001.
- **README:** "near 26 minutes on 4 cores" disagrees with cell 0's "about 27 minutes". Neither total is printed. The stage times in cell 0 (about 3, 15 and 7 minutes) are also above the printed 2.3, 12.9 and 5.7.

I checked every other sentence of the "Result:" cells, the Summary (cell 94), the README table and the record's notes against the outputs, and the numbers support them. That includes the cohort counts (14 sessions fail both counts and 3 fail one), the 38 sessions without post hoc pupil, the 118/23 visual stimulus sets, and the template distances for BW061 and BW048.

The attempt record states my round-1 reasons accurately and in substance in my own words. My separate problem points were folded into the matching claim's reason: B1 into figs2, B2 into fig5c-movement, B3 into fig3e, B4 into fig2a, B5 into fig2c, B6 into figs4, B7 into cohort and B8 into fig5c-state. Some detail was dropped (the disengaged values per fig2c reading, the chance-level note), but nothing is misstated.

**3. Round-1 points**

Resolved:
- **B1:** the cross-validation now runs 10 initialisations (cell 14).
- **B2:** the conclusion now says the variants keep pupil information and do not test the claim (cell 93).
- **B3:** stationary now uses |speed| < 0.02. The 214 backward trials it removes move the vertices by at most 0.1 (cell 42).
- **B4:** the distances to all six templates are now printed. Every state of BW061 and BW048 is nearest the template of its label (cell 20). The text now says that under M3 the sub-optimal matching cannot fail.
- **B5:** a variant without the extra zero-dwell epochs is shown. There are 3 such epochs and no number changes (cell 26).
- **B6:** a variant over 10 shuffled splits per mouse is shown. BW051's pupil r² ranges from 0.001 to 0.562, and the test results are unchanged (cell 46).
- **B7:** both counts are shown and the record notes the difference.
- **C, `visual_gabor_angle`:** the column exists, and the stimulus values were corrected to follow `get_stim_vals`.

Unchanged, without effect on a conclusion: B8, the 3/20 decoder runs. The smallest z is 4.87, so significance does not depend on it.

Still open, without effect on a conclusion:
- Which 381 sessions the paper used. This is now a question to the authors in the record.
- The stage 6 "no discernible change" part of distractor-response-rate is not tested, as the claims file says.
- 123 visual sessions have grating angles but only 118 get the 1/0.6/0.2 values. The other 5 are unexplained, but the per-session sets are printed and none is degenerate.

Bearing on a conclusion:
- The fig3f reproduced outcome sits 0.004 above the r² tolerance bound, on a single random split as the criterion specifies. The 10-split mean (0.573) supports it, so I accept the outcome, but it is marginal.
- The numerical mismatches in section 2 should be fixed in the text. None of them changes an outcome.
