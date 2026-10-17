**Round 2 verifier report: Chang et al. 2023 on DANDI 000232 (0.240510.2038)**

Cell indices below refer to the re-executed notebook (89 cells). The cell numbers in my round-1 report refer to the earlier run.

**1. Outcomes**

The claims file has 29 claims and the attempt record has 29 outcomes: 28 tested and 1 blocked. I agree with all 29.

- **Reproduced (19):** fig1e-recording-counts, fig6-session-counts, fig1d-performance, fig1d-outcome-fractions, fig2d, fig2e, fig2f, fig3b, fig3c, fig3de, figs3, fig4f, fig5de, figs5, figs6b, fig6d, figs7gh, fig6-ppc, fig6fg.
- **Partially reproduced (7):**
  - fig1h: 3 of 4 areas within tolerance.
  - fig2c: S1 is out of tolerance, but MM and ALM are both above S1 and S2.
  - fig4c: p = 0.004.
  - fig4e: 1 of 4 areas within tolerance.
  - figs4ef: 7 of 8 judgements match.
  - figs4h: S2 is 0.422.
  - fig6c: the ALM interval reaches 0.005.
- **Not reproduced (2):**
  - fig5b: both counts fail. The author has now made the change I asked for in round 1.
  - fig6ij: the detection-task MM interval on short laser trials is [0.045, 0.483].
- **Blocked (1):** fig1e-probe-locations, data_missing.

**2. Statements the printed numbers do not support**

- **"No other bound of the optogenetic claims changes side over the ten seeds."** (attempt record, fig6c notes). The Summary in cell 87 says the same: "no other optogenetic call changes". Two problems:
  - The seed check in cell 72 leaves out the fig6ij laser-only CIs.
  - For figs6b ALM, the code-variant interval does change side. Its main draw gives an upper bound of +0.002, which includes 0 (cell 71). In 9 of 10 other seeds it is below 0 (cell 72).
  - The statement holds only for the Methods-resampling calls of the claims in the `judged` list.
- **Cell 24:** "consistent with the last rows being the end of the session, **not with 20 trials cut after them**". A lower gap rate in the last 20 rows (4.5% against 12.7%) does not tell these two cases apart. The attempt record correctly leaves this clause out.
- **Cell 39 and the fig3b notes:** "The shuffled medians are above 0.5 by about as much as the larger block's share of correct trials".
  - What the numbers show is that the shuffled medians are about *equal to* that share (0.526 to 0.564 against 0.529 to 0.556).
  - "As expected of a classifier weighted by class priors" is an interpretation that no output in the notebook shows.
  - This affects no outcome.
- **Cell 61:** "S2 is 0.10 above it (0.32)". The difference is 0.102, and the criterion fails at more than 0.1, so rounding to 0.10 hides the failure. The attempt record correctly says "0.422 against 0.32".
- **figs4h deviation (cell 56 and record):** "left 1 of 10 S1 sessions and none in S2 and MM".
  - Session counts are not printed. Only resample counts are: 193/300 for S1, 0 for S2 and MM, 195/300 for ALM.
  - Those resample counts fit 1 session in S1 and 1 in ALM, but ALM is not mentioned.
- **Cell 87 Summary:** "With other seeds fig1h MM is within tolerance in 3 of 5, fig2c ALM in 2 of 5". These counts include the main seed, but "with other seeds" suggests they do not.
- **README:** "about 15 minutes, a quarter of it streaming the files". Streaming took 131 s of 14.7 min (cells 1 and 88), which is about 15%.
- **Cell 0 (introduction):** "141 optogenetic behaviour sessions". The dandiset holds 130 (cells 1 and 19).

Everything else checks out against the outputs. That covers every other "**Result:**" sentence (cells 17 to 86), the rest of the Summary, the README table and the attempt record's notes and findings. Specific checks I made:

- the seed ranges for fig1h and fig2c;
- the fig3c bounds, within 0.011 of the paper;
- fig5de, within 0.023;
- fig6c with code resampling, within 0.015;
- the fig5b counts 63, 75, 87, 91, 88 and 91 and fractions 0.571, 0.652, 0.554 and 0.621;
- the fig6ij values.

**My round-1 reasons in the attempt record:** they are stated faithfully and in my own words. They include the B-problems I attached to each claim and my "agrees: false" on fig5b. One omission: the clock part of B11 (YT086 2020-03-20, MM) is not recorded anywhere in the attempt record. It appears only in notebook cell 11.

**3. Round-1 points**

Resolved:

- **B1:** ten seeds were added (cell 72).
- **B2:** the count of blocks with a hit including first blocks (87 and 91) and trial-number estimates were added. The by-cue+1 condition holds either way.
- **B3:** five seeds were added (cell 29).
- **B4:** the author checked the windows against the code. I cannot see the code, so I accept this as stated.
- **B5, B6, B10, B12:** now recorded.
- **B7:** class balance is printed. The wording issue is listed above.
- **B8:** the response is accepted.
- **B11, coordinates part:** 49 of 49 files checked.

Not settled, with no effect on any conclusion:

- **B9:** the gap pattern is printed but does not settle whether the last 20 trials are missing. Reading (a) passes, and the criterion allows either reading.
- **B11, clock part:** not checked further.

Remaining points that bear on a conclusion:

1. **fig6c depends on the draw.** The ALM upper bound under Methods resampling averages −0.001 (SD 0.003) and is below 0 in 7 of 10 seeds. The outcome flips between partially reproduced and reproduced with the seed, and also with the choice of resampling. The record discloses this.
2. **fig1h and fig2c are judged on the main seed.** On the five-seed means, all four areas are within tolerance for both claims (fig1h: MM 35.6; fig2c: S1 5.0, inside 4.5 ± 0.56). Both would then be reproduced. On single seeds:
   - fig1h is reproduced in 3 of 5;
   - fig2c is reproduced in none, because S1 or ALM falls outside every time.

   The record discloses the main-seed choice.
3. **fig4c and fig4e: the units of the soft-normalization offset are still unknown.** The Methods normalization gives p = 0.004 for fig4c. The code's normalization gives p = 0.001, which would meet the criterion. The fig4e magnitudes may also depend on it.
4. **fig6ij:** the one failing CI uses the detection-task window, which covers the laser (the code's window). The paper's detection CIs match none of the short, long or pooled rows, so it is unclear which trials the paper used.
5. **fig5b:** the outcome is correct under the criterion. The paper's 88 and 91 equal the total block counts, and the record lists this as a paper inconsistency.

I did not view the figure images.
