**Verifier report, round 2: Costabile et al. 2023 (eLife 83289) on DANDI:000235 to 000238**

The claims file has 35 claims. The attempt record gives 35 outcomes: 2 reproduced and 33 blocked. Of the blocked, 18 are too_large (12 fit claims and 6 anatomical), 1 is data_missing (fig6f) and 14 are other (not attempted: 9 simulation and 5 mouse).

### 1. Outcomes and assumptions

- **data-zebrafish-coverage, reproduced: agree.** Main notebook cells 24–25: 25 fish, 750 planes and 706,543 components, all exact. 434,651 components pass the cut, +0.41%, within the tolerance of 43,288.
  - The deviation says "the raw movie is assumed here" but the outcome is not marked `assumed: true`. The assumption is reasonable, and the outcome barely depends on it: the count moves about 4,000 per 0.01 of the cut, so only a large shift in brightness would move it out of tolerance. It is still an assumption and should be flagged as one.
- **figs6-train-test-uncorrelated, reproduced, `assumed: true`: agree.** Cells 28–30: the largest |median| is 0.051, under all four bout readings and in the orthogonalized variant. The assumption (bouts re-derived at 5 or 10 rad/s, relative segment angles, `sum_tail` as the direction metric) is stated and reasonable. Cell 17 shows the code's default of 2 rad/s gives 4.9 bouts/s, inside the noise, and the outcome does not change across readings.
- **The 12 fit claims, too_large: agree.** Cell 34 gives 164 h on one thread; subsample cell 12 gives 107 h on 4 CPUs, 214 h with the rotated controls.
- **The 6 anatomical claims, too_large: agree.** I accept the author's response. The claims file marks them `data: with_inputs` (Zenodo centroids), so the dependence on the fits is the binding block.
- **fig6f, data_missing: agree.** Cell 20: `colnames ['pixel_mask']`, no reference images; only the raw red movie is present in 175 of 175 planes.
- **The 14 data-elsewhere claims, other (not attempted): agree.** I also accept "other" rather than data_missing for the mouse claims, because the CSHL data are public.

### 2. Sentences the printed outputs do not support

- **Main cell 35:** "One fit of the paper's network takes 1.89 s on one thread here (median of fits 2 to 20; the first, 7.17 s …). That is 227 h on one thread …, 57 h on four". Cell 34 prints a median of 1.37 s, a first fit of 5.36 s, 164 h on one thread, 41 h on four, and 82 h with the controls.
- **Subsample cell 13, timing:** "In four processes a fit takes about 4 s, about 1.1 s of wall time per fit overall, so … about 130 h here, and twice that". Cells 5 and 12 print 3.08 s median per fit, 0.89 s of wall time per fit, 107 h and 214 h.
- **Subsample cell 13, cutoffs:** "…as figs6-mine-more-at-every-cutoff states". Cell 10 shows MINE's estimate below the linear model's at cutoff 0 (362,799 against 371,188). Under the claims file's criterion ("at every cutoff where either count is above zero") the point estimate fails there. Only the interval of the difference does not exclude zero. The same applies to "at 0 they are about equal" in the record's figs6-mine-more-at-every-cutoff notes. The 7 MINE fits with no test correlation probably account for part of this gap. This is an estimate and decides no outcome.
- **Attempt record, fig6d notes:** "median 1.89 s on one thread …; about 4 s, 1.08 s of wall time per fit …, about 130 h …, about 261 h". The outputs give 1.37 s, 3.08 s, 0.89 s, 107 h and 214 h.
  - The round-1 response says the earlier per-fit time "did not match the notebook and is corrected". It still does not match.
- **Attempt record, figs6-shuffle-enrichment notes:** "about 261 h". The output is 214 h.
- **Attempt record, fig6f notes:** "about 66 h on four CPUs". Subsample cell 12 prints 54 h; main cell 34 prints 21 h.
- **Attempt record, simulation and mouse notes:**

  | Claim | Record says | Cell 34 prints |
  |---|---|---|
  | fig1f | 0.2 h, 0.9 h for five seeds | 0.1 h, 0.6 h |
  | fig2e | 1.6 h and 8.1 h | 1.2 h and 5.9 h |
  | fig3 | 0.2 h | 0.1 h |
  | Mouse | 2.1 h | 1.5 h |

  All the stale numbers are about 1.38 times the printed ones (1.89/1.37 s). They appear to come from a previous execution.
- **Main cell 16:** "Calcium correlates with swim starts from 0 s … and not before it." Cell 14 shows a mean r of 0.086 to 0.108 at −5 to −1 s, already rising at −1 s. "Peaks 1.8 s after" is supported; "not before it" is overstated.
- **Finding 5 (tail jump):** "nothing in the files says which side of it is placed correctly". Cell 21 contradicts this:
  - In the 8 planes ending at 623.8 s, the start (−5.3 to −5.5 s) matches every other plane.
  - In the 2 starting at −133.5 s, the end (495.80 s) matches.
  - The sample counts (about 125,300 at 4 ms) match normal planes.
  - So the misplaced side is identifiable and correctable: shift it by 128.004 s.
- **README:** "well over 100 hours" is loose against the printed 107 h (214 h with the controls). Everything else in the README, the Summary (cell 36) and the other notes matches the outputs.

**My round-1 reasons in the record.** The `verifications` reasons state them faithfully and in my words. My B5 (clock-check misreading) and B7 (odd tail timestamps) appear in no reason, and B6 appears only in the author's response. None of them is claim-level, so this is acceptable.

### 3. Round-1 points

**Resolved:**
- **B1** (block reason for the data-elsewhere claims), **B2** (fig6f changed; anatomical and mouse reasons accepted, see section 1) and **B4** (the criterion weakness is recorded as a question for a reader).
- **B3, largely resolved.**
  - The linear model is now fit to all components: 26,326 reach sqrt(0.5), against about 25,300 implied by the paper.
  - A 600-fit MINE subsample was run.
  - The Taylor-based estimates were not run, with reasons given.
- **B5.** The wrap-around bug in `heldout_shift_r` is fixed. The held-out curve is now smooth (0.649 at 0 s, 0.663 at +3 s, 0.604 at −5 s) and is read correctly, as "within a few seconds".
- **B6** (the code does the same; the notebook prints 1,866 shared bins out of 47,480 bouts), **B7** (now a finding), and **B8 and B9** (both stated).
- **Everything in my "could not check" list:**
  - the raw-trace source is cited and an orthogonalized-predictor variant is added;
  - start times, rates, the end that carries the extra temperature, and a 0.2 s curve are printed;
  - the red channel is printed;
  - the tail steps are printed;
  - 20 timed fits and the core count (4) are printed;
  - the channel descriptions are printed.

**Remaining:** none of these changes an outcome. All are text corrections:
- the timing figures in cells 35 and 13 and in the record's notes do not match the outputs;
- "as figs6-mine-more-at-every-cutoff states", which the estimate fails at cutoff 0;
- the statement in finding 5 that the correct side cannot be told;
- `assumed: true` is missing on data-zebrafish-coverage.

### 4. Critical findings

No finding in the attempt record is rated `critical`.

The one finding closest to critical is finding 5, the 128.004 s tail-timestamp jump in 10 planes, rated `major`. It is shown in cell 21: one step of 128.004 s in each plane, against at most 0.70 s in all other planes. It is not critical. The jump is evident from the timestamp values, and the side that is displaced can be identified and corrected. It affects 10 of 925 planes, and no tested conclusion. I would rate it `minor` (evident and easy to work around), and `major` is defensible only for analyses that use those planes' bouts.
