I've revised the attempt for the round-1 report. The entry re-ran cleanly (`python tools/entry.py all entries/mohebi-2019`: 0 errors, about 4 minutes), the attempt record passes its schema and the entry checks, and the round is recorded under `verifications`. Nothing is committed.

**Outcome changes.** All four claims where the verifier gave a different outcome now have the verifier's outcome, because the new numbers support it:
- **fig2efgh-tonic-firing-indifferent-to-reward-rate:** not_reproduced → partially_reproduced.
  - Firing changes little overall (median 0.5 Hz higher in high-reward blocks, signed-rank p = 0.0006).
  - But individual cells do change under every test that could detect it. On 1 min bins 18 of 27 cells differ. With a new circular-shift null, which allows for the bins not being independent, it is 9 of 27 (7 with the other median-block handling).
  - The block-mean test cannot reach p < 0.05 at all in 6 of 27 cells.
  - The assumption that the 1 min bin test is the right one is withdrawn.
- **retro-tagged-cells-resemble-others:** not_reproduced → reproduced, resting on an assumption. Neither cell changes under the block-mean test, which has enough power for these two cells, or under the circular-shift null (p = 0.27 and 0.85). Only the plain 1 min bin test flags one cell, and I set that test aside because it treats dependent bins as independent.
- **fig4e-light-on-alignment:** partially_reproduced → not_reproduced. The count of cells responding to Light-On misses 25 ± 2.5 under every window (16, 13, and 11 on trials with latency over 0.5 s). Not every responding cell is better aligned to Light-On under either reading (15 of 16, or 14 of 16 with the 4.5 ms kernel). Only the short-latency part of the claim holds.
- **fig5ab-weak-negative-rpe:** reproduced → partially_reproduced.
  - The pause count depends on how the pause is measured: 2 counting only intervals between spikes inside the window, 8 counting the window's edges, and 9 with a new reading using whole inter-spike intervals that overlap the window. The measured value is now 8.
  - The valley part cannot be tested. The smoothed minimum is 0 Hz on essentially every unrewarded trial with either kernel, so the authors' scripts were checked: neither computes a valley or a pause.

The tally is now 8 reproduced, 7 partially reproduced, 2 not reproduced and 20 blocked, the same as the verifier's.

**Added or corrected:**
- **Kernel:** the Pavlovian click and cue responses now also use the claims file's main reading of the smoothing kernel (4.5 ms instead of 20 ms). The cell counts fall to 7 and 4 of 27, so those outcomes are unchanged.
- **fig5a-early:** a circular-shift null now runs alongside the Pearson test. Only 1 and 2 of 29 cells are significant under it, so most of the original count may come from slow drift. The outcome stays not_reproduced, as the criterion asks for the Pearson test.
- **fig2:** the counts without the 1 ms pulse substitution are printed (22 and 17 cells pass both criteria), and the record now says the substitution is my choice, not the criterion's. I also noted that the tagging test's smallest p above zero is 0.0013.
- **Smaller fixes:**
  - The ed5 conclusion now says the 8 against 9 tone-set count comes from the data holding 8 IM-1037 cells where the Methods give 9.
  - ed8 now reports how many sessions hit the edge of the alpha grid.
  - The notebook says the all-segments firing rate is slightly overstated, because segment durations are not deposited.
  - I corrected one sentence of my own: dropping trials with latency under 0.5 s lowers the Light-On count to 11, which does not show that Center-In responses had raised it.
- The two questions to the paper's authors (on the tonic test and on the pause and valley) were updated with the new numbers.

**Not done:**
- I added no question for a reader to `questions/mohebi-2019.yaml`. The report names no place where the claims file misreads the paper; the kernel point is a choice between the paper's Methods and the authors' code.
- I did not run the ed1b proxy on the electrophysiology sessions. The verifier said it would not test the microdialysis claim.
- I did not change how the all-segments rate is computed, since the data set gives no segment durations to use instead; it does not affect any outcome.
