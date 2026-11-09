I addressed every point in the round-1 report and re-ran the entry. Three outcomes changed, the other 49 stayed the same, and the record now has 21 reproduced, 5 partially reproduced, 7 not reproduced and 19 blocked. The final `python tools/entry.py all entries/001371-prince-2025` passed in 1437 s, `check` reports 0 errors, and nothing is committed.

## What changed in the outcomes

The changes come from fixing the time grid (problem 6). The update-aligned decoding now uses the paper's code's grid: no 0.2 s bin straddles the cue, and the bin centres are the code's sample times (±0.1, ±0.3 … ±2.5 s). The round-1 grid is kept as a variant, and it reproduces the round-1 numbers exactly.

| Claim | Before | Now | Why |
|---|---|---|---|
| sfig3c-retrospective-unchanged | reproduced | not reproduced | p = 0.036 on the code's grid; 0.12 on the round-1 grid |
| fig5d-stay-hpc-below-switch | partially reproduced | reproduced | new arm p = 0.0094; 0.38 on the round-1 grid |
| fig7c-hpc-commitment-initial-arm | not reproduced | reproduced | p = 0.29; 0.040 on the round-1 grid |

All three outcomes depend on the 0.1 s difference between the two grids, and their notes say so.

fig2g-pfc-no-goal-increase stays not reproduced. It now fails under both model readings (new arm p = 0.016 and 0.030), where before only one reading failed.

## What I added or corrected

- **Spread (problem 1):** the paper's code, at the pinned commit, does measure to the outermost bins above the threshold, as the helper did. I added the first-crossing reading as a variant: it gives 0.14 against 0.37 bins, also PFC wider, so the outcome is the same.
- **Unlabelled units (problem 2):** their region cannot be recovered. None of the five units tables has an `electrodes` or `electrode_group` column (61 of 66 do), and the phy channel runs 0 to 63 on both probes. The notebook prints this.
- **Arm halves (problem 5):** they now follow the code's split, with a split over the bins that have a posterior as a variant. Both give three of the four contrasts, so sfig3ab stays partially reproduced. The bins of every zone are printed.
- **fig6e (problem 3):** I timed the CA1 half with the paper's procedure: about 1 h for the real labels and about 41 days with 1000 shuffles. The claim stays blocked as `too_large`.
- **LSTM claims (problem 4):** they stay `too_large`, since the protocol names that reason for an estimate over the notebook limit; I recorded the verifier's disagreement. The notebook now also prints the core count: 10.4 h in one process, at best 2.6 h on 4 cores. I did not run a subset of sessions, because the claim's values are means over all 66.
- **Smaller points:**
  - The equal-cell subsampling now has its own seed per session (problem 9).
  - I added a decoding-validation variant that scores only moving bins; it gives the same counts (problem 10).
  - The session where the two theta phases disagree has almost no spike phase locking, which explains it (problem 11).
- **Questions for a reader:** two added to `questions/001371.yaml`, on fig3c's whole-central-arm reading and on trial-mix's programmed probabilities. No claim was changed.
- **Record:** notes, measured values and deviations are updated, and the round is under `verifications`. Findings now include the spread mismatch between the Methods and the code, and a question for the paper's authors on which bins form the post-cue windows. The code's count of trials now changes two outcomes (sfig3c-retrospective-unchanged and sfig12-delay-hpc-no-outcome-difference).

## Not done

- **Kenward-Roger check (problem 7):** not done, because R, lme4 and lmerTest are not installed here. The deviation on the Wald tests stands.
- **Last run's markdown:** after the final run, the LSTM estimate came out at 10.4 h, so I changed that one figure in the markdown of both the notebook and its executed copy. Code and outputs are unchanged.
- **Your edit to `tools/runner/chain.sh`:** it was already modified before I started, and I left it as it was.
