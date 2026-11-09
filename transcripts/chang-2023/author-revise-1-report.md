I've worked through every point in the round-1 report. The entry re-runs cleanly with `tools/entry.py all` (about 15.7 minutes, `0 error(s)`), and `entry.py check` passes. Nothing is committed.

## Outcome changes
- **fig5b-first-hit-switches: partially reproduced → not reproduced.** The verifier was right. The criterion allows a partial outcome only when one condition fails. Here two fail: the block counts are 63 and 75, against the paper's 88 and 91.

All other outcomes stay as they were, and the verifier agreed with each of them. The new count is 18 reproduced, 8 partially reproduced, 2 not reproduced and 1 blocked.

## What I added or corrected
- **Run-to-run variation at the bootstrap edges (problems 1 and 3).**
  - The optogenetic intervals the claims judge are now re-run with ten other seeds, giving the mean and spread of each bound.
  - Only the fig6c ALM upper bound changes side: it averages -0.001 and is below 0 in 7 of 10 seeds. I kept fig6c as partially reproduced, judged on the main seed, and recorded the spread.
  - The figs6b ALM bound is below 0 in all ten seeds, so that "reproduced" holds.
  - fig1h and fig2c now print all five seeds and their mean. The five-seed means fall within tolerance in every area, but MM in fig1h is within tolerance in only 3 of 5 seeds. Both outcomes are kept on the main seed, and the record says they depend on the seed.
- **fig5b (problem 2).**
  - Added the count of blocks with a hit including first blocks: 87 and 91.
  - Added first-hit positions in trial numbers estimated from the gaps between rows (new helper `xm.estimated_trial_numbers`). The share of first hits by the trial after the cue is now 0.554 and 0.621, still above half.
  - The finding now explains that the paper's code returns one entry per block, so counting its entries gives 88 and 91.
- **fig6ij lick windows (problems 4 and 5).** I checked them against the paper's code at the pinned commit, and they are the code's. I added the code's "all laser trials" pooled rows for the detection task. These don't match the paper's detection intervals either. The criterion testing more than the paper reports is now in the notes.
- **figs4h.** The S2 mean over five seeds is 0.420 to 0.425. It is within tolerance in 1 of 5 seeds, at the edge, so the outcome is kept on the main seed.
- **Smaller points.**
  - Chance level above 0.5 in decoding (problem 7): this matches the larger block's share of trials (0.529 to 0.556).
  - Last 20 trials (problem 9): the gap pattern near the end of each session is printed. It is consistent with the files ending at the true end of the session but doesn't prove it.
  - Electrode coordinates (problem 11): x, y and z are now checked in all 49 files, and all are missing.
  - figs5 (problem 12): the notes now say the S1 and S2 point estimates are as large as MM's and ALM's, so the "no tracking" result rests on wide intervals.
- The README, the notebook's conclusions and summary, and the attempt record match the new numbers. The round is recorded under `verifications`, with the verifier's reasons in its own words and my response for each of the 29 claims.

## Not done
- **Problem 8 (normalization uses all trials, including the test fold):** no change. No labels are used in that step, and this classifier gives the same predictions whatever the scaling.
- **Problem 6 (session rule for the subspace analysis) and problem 10 (changed reading in figs4h):** no change beyond what is already recorded as deviations.
- **Last 20 trials:** the data can't settle whether they were removed.
- **Session YT086 2020-03-20:** a shared clock with the trial table is still not established, and the session stays in. It is named in the notebook.

An untracked `scripts/` directory appeared in the repository root. I didn't create it and left it alone.
