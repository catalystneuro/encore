**Verifier report, round 2: Vinograd et al. 2024 on DANDI:001037 v0.260609.1402**

The claims file has 54 claims and the attempt record has 54 outcomes. The record gives 8 reproduced, 10 partially reproduced, 10 not reproduced and 26 blocked (25 data_missing, 1 methods_underspecified). I agree with 51 of the 54 as they stand. For the other three I would make one change (ed3h) and add two `assumed` flags (ed7f, ed8gi).

**1. Outcomes and assumptions**

I agree with these outcomes:
- The eight reproduced claims except ed3h-related consistency (see below).
- All ten not reproduced claims.
- The partially reproduced claims ed3f, ed4hi, fig1f, x1-time-constant-range, fig2gh, ed8b, ed8c, fig2no and ed9d.
- All 26 blocked claims.

Points that need a change:
- **ed3h-decode-engaged-from-observed (partially_reproduced).** I proposed this outcome in round 1, but the new four-seed run (rslds cell 26) changes the picture.
  - The observation-weights reading gives p = 0.0079 with seeds 0, 137 and 1337, and p = 0.15 with seed 1. That is the same pattern as ed3g, which is recorded as reproduced (assumed: seed 0).
  - With seed 0, both readings the criterion names give p = 0.0079.
  - Applying the ed3g rule gives reproduced (assumed: seed-0 fits), with the own-weights reading's fragility (1 of 4 seeds) in the notes. Otherwise the record should say why the two claims are treated differently.
- **ed7f-activated-x1-natural-levels (not_reproduced).** The outcome depends on leaving M70 out: p = 0.0043 without M70, p = 0.097 with it (stored cell 25). The exclusion is reasoned well (cells 7 and 9), but it is filed as a deviation without `assumed: true`. It should be flagged as assumed.
- **ed8gi-x1-stim-no-x2 (not_reproduced).** Here the outcome depends on keeping M70. Without M70 the smallest Dunn p is 0.061 (stored cell 31). The choice is stated and reasonable, but it should also be `assumed: true`. M70 is left out of ed7f and kept in ed8gi, and each choice happens to give "not reproduced", so marking both makes that visible.

Assumptions already marked:
- ed3g (seed 0), fig1m (paired test), ed4c and ed4d (matched cells), ed4g and ed4hi (baseline window): each is stated and reasonable.
- Matched cells: the identical cell counts in the two sessions of every mouse support the assumption more than the autocorrelation check does.

Claims-file notes:
- ed9d reading (b) says "the pattern holds across mice". The mean meets it (2.62, 3.22, 2.91); 2 of 7 single mice do. "Partially reproduced" is a fair reading, but the criterion is ambiguous.
- For ed10g, the criterion says "non-targeted neurons", following the legend of ED Fig. 10g. The Results decode from "follower x1 neurons", and the Methods (Terminology) define those with the 50 µm exclusion. So the criterion is looser than the paper, and the record follows the paper.

**2. Sentences the printed numbers do not support**

- **Wrong range of annotation times.** rslds cell 4 says "the first annotation comes 56 to 152 s after the start", and the record's finding repeats "start 56 to 152 s before the first annotation". The printed first annotations are 56.3 to 95.9 s (rslds cell 3), matching the 0.94 to 1.60 min baselines in cell 35.
- **Unprinted value.** Stored cell 32 and the ed8gi notes say M70's x2 projection falls "to about −3.8 in the 5 s before the first onset". No output prints this; only the baseline mean of −1.26 is printed (cell 31).
- **Run time.** The README says the cross-validation notebook "takes about 45 minutes". The output prints 255 fits in 28.0 min and a notebook run time of 30.2 min (CV cell 10).
- **Contradictory comparison.** The ed4g notes say "The x1 value of the engaging reading is within 1.6 +/- 0.2". That 1.68 is a count per baseline, and the record's own deviation says counts per baseline are not comparable with the paper's.
- **Bound stated too broadly.** The methods-cvr2 notes and CV cell 8 call the in-sample reconstruction a bound "no held-out reading can be expected to exceed". This holds for the neural R2 only. The sample code's latent R2 in sample averages 0.84 for observation with seed 0 (rslds cell 10). The outcome stands on the contiguous-block reading.
- **Rank pairing not shown.** The M70 finding says "cells 1, 2, 3, 5 and 22, ranking 1st, 2nd, 4th, 8th and 64th". Cell 9 sorts cells and ranks separately, so this cell-to-rank pairing is not shown.
- **Frames and seconds mixed.** The legacy-file finding says the earlier file "follows to 350 s (4426 frames)". 4426 frames is 443 s, and 350 s is the end of the BALB/c interval. The stored summary (cell 48) says "143 s longer", which is consistent with 443 s.
- **Start value.** ed8c (rslds cell 46 and notes) says "M70 from −5.90". The simulated trajectory starts at 0 by construction; −5.90 is its value at the end of ISI1.
- **Unclear wording.** Stored cell 20 says "only the first comparison could be tested as significant". The output shows Cb p = 0.38, 0.45, 1.0 and 1.0, so it is unclear what this means.

All other "Result" cells, the three summaries and the record's notes match the outputs.

The record's `reason` fields state my round-1 reasons accurately and in close paraphrase. Problem text is folded into the claims it concerned. The fig2gh reason now includes the onset + 211 detail, which I had marked as not affecting a conclusion.

**3. Round-1 points**

Resolved:
- **1 (M70 target list):** index shifts were tested, M70 is left out of ed7f, and the all-mice variant is shown.
- **2 (ed8c control):** the run without kicks was added and the outcome changed to partially reproduced.
- **3 (ed10g):** I withdraw this point; the paper's definition of follower cells supports the author.
- **3 (fig4hj):** I accept it as blocked, because it would reuse the underspecified weights of fig4ce. Since it uses no recorded data, methods_underspecified would label it more accurately than data_missing.
- **4 (methods-cvr2):** now not reproduced, and the held-out score is described as a reconstruction.
- **5 (baseline window):** now marked as assumed.
- **6 (seed):** the module header is corrected and the decoding claims are run with each of the four seeds.
- **7 (matched cells):** marked as assumed, with a data check.
- **8 (baseline windows):** ProjectionMetadata is printed per row, and the variant without M70 is shown.
- **9 (number of states by cross-validation):** acknowledged in CV cell 11.
- **10 (ed9d nesting):** stated in the notebook and notes.
- **11 (x2 sign):** every x2 target has a positive stored weight.
- **12 (small details):** onset + 210 and r₀ = 1 are fixed.
- **13 (result cells left in):** no longer applies.

Remaining points that bear on a conclusion:
- ed3h should be treated like ed3g, or the difference explained.
- ed7f and ed8gi need `assumed: true` for the M70 choice.
- The four wrong or unsupported statements above: annotation times of 56 to 152 s, the unprinted −3.8, the 45-minute run time and the ed4g tolerance comparison.
- **New point on ed4c and ed4d:** nothing shows that the five strongest x1 neurons are stable across seeds within one session. If they are not, the 4% cross-condition overlap says nothing about the paper's claim. A within-session, cross-seed overlap from the existing fits would settle it.

Points that do not bear on a conclusion:
- For the x2 sessions of M70, M18R and M79RL, the targeted-cell response is larger with indices shifted by 1 or 2 than unshifted (stored cell 9). No claim reads the x2 lists.
- The large negative x2 projections of M70 and M18R under x2 activation are still unexplained.
- `decay_tau`'s 10 s fit window is called a "standard" choice, but it can change the ed4hi decay constants, several of which sit at the fit bounds.
