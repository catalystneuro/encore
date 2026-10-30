No outcome changed. All 38 stay as round 2 verified them: 27 reproduced, 1 partially reproduced, 2 not reproduced and 8 blocked. Nothing is proposed for a third round. `python tools/entry.py all entries/000351-jeong-2022` passes with 0 errors, and every conclusion matches the new numbers.

**What I added or corrected**

- **fig4hi-delay-change-dopamine-unchanged:**
  - The outcome is now marked `assumed: true`, with a deviation stating the assumption: the paper's fit was bounded the same way as here.
  - The conclusion (cell 68), cell 10, the Summary and the notes now say plainly that the test cannot detect a change in this data. The code's bounds bind on both scales, the percent variant cannot fit at all, and an unbounded fit finds a change in every animal (t = 7.84).
  - I removed the two sentences the verifier said the outputs don't support: "the code's bounds suit a fraction" and "does not depend on the scale".
  - A new `methods_unavailable` finding asks the authors which dF/F scale the bounds were set for.
  - The verifier said the claims file does not misread the paper here, so I added nothing to `questions/000351.yaml`.
- **Experiment 7 trials with no dF/F (new point):**
  - A new output counts these trials. In HJ-FP-WT-stGtACR-M2's last session, CS1 trials 1 to 17 have no dF/F. Elsewhere only a few reward responses are missing, in three sessions.
  - fig6i-lower-cs1-asymptote now has a variant that uses WT-M2's previous session instead. Its value moves from 0.459 to 0.462 and the test gives t = 1.70, p = 0.117, so that outcome holds.
  - A new note explains how these trials affect the Fig 6D and 6I claims.
- **fig4p-background-faster-decay:** each animal's sum over the 50 trials before the change is now printed. The unsupported sentence "HJ-FP-M6's pre-change sum is near 0" is replaced with the values (37.3 and 288.1).
- **Other text fixes:**
  - Session length in cell 6 is now 481 to 4810.
  - The consummatory t values in cell 45 are now 6.30 to 6.49.
  - The per-animal range in cell 102 is now 0.30 to 0.71.
  - The Summary keeps the clock caveat for the 27 sessions.
  - For the missing sessions, only M4 Day38 is now stated as missing. The other six days are worded as "suggests" in the record notes, the `data_missing` finding, the README and the Summary.
- **Record:**
  - Round 2 is recorded under `verifications`, with the verifier's reasons and my responses for all 38 claims.
  - I added the round-1 remark the verifier said was missing (cell 43's count of 0 trials without a dopamine value) to the fig4ef round-1 reason.

**Not done**

- **Simulation claims:** I kept the blocked reason as `not_runnable`. The verifier now leaves this open and says it changes no conclusion.
- **Abruptness t values:** they still differ from the paper's (15.3 against 22.9, and 9.7 against 5.67), and I have not found the cause. The verifier says this does not affect a conclusion.
