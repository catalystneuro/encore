I've finished the round-2 revision. No recorded outcome changed, as round 2 requires. I proposed blocked for two claims; a third verification round will decide those. `python tools/entry.py all entries/gable-2026` passes with 0 errors, the notebook ran in about 4.6 minutes, and every conclusion now matches the new run.

**Outcomes**
- **figs4-high-couplers-correlated:** stays partially reproduced, which is the outcome the round-1 revision gave. The verifier disagreed and would give not reproduced. I replaced the reading it found unreasonable (keeping both stored rows of a duplicated unit) with one that counts each such unit once. Under that reading 7 of 8 readings give not reproduced; the other reading, `bab`, gives partially reproduced. `baa` and `bab` differ only in which trials enter, which the paper leaves open. The claims file takes the outcome all readings give, and that rule already blocks the middle claim, so I proposed blocked (`methods_underspecified`).
- **figs4-lowest-couplers-correlated:** stays partially reproduced, now resting on 15 of 16 readings as the verifier asked. Counting units once leaves one reading, `bba`, reproduced at 0.0548, just inside the 0.054 tolerance edge. It differs from the adopted reading only in the firing-rate measure, which the paper leaves open. By the same rule I proposed blocked, although the verifier agreed with partially reproduced. The effect is positive and significant under all 16 readings; only its size is in question.
- **figs4-session-selection** (not reproduced) and **figs4-middle-couplers-not-correlated** (blocked) keep their outcomes. The selection's measured values are now under the adopted reading: 9 mice, 16 sessions, 501 and 5,060 pairs.

**Added or corrected**
- **Adopted reading:** now `baa`, with units stored twice counted once and only units above 0.5 Hz. I updated the notebook text, README, outcome notes and the question to the authors to match.
- **New outputs:**
  - NaN event counts by event type, which needed a small change to `alm_coupling.py`.
  - A list of the sessions where photostimulation onsets and laser power disagree.
  - The three KJ18 sessions with optogenetics metadata but no laser trace.
  - The outcome under each of the four readings with units counted once.
  - How far `baa` and `baa-r` are from the values the paper's code printed.
- **Sentences the verifier quoted:** all fixed (cells 6, 13 and 36, and findings 1, 8 and 11). Finding 1 no longer claims that the duplicate pairs change bin 5. Its new text says keeping every row changes the high-coupler outcome under most readings, which cell 29 shows.
- **Notes:** the high-coupler notes now say what the verifier pointed out. With every row kept, bins 5 and 7 sit nearer the code's printed values, so the paper may also have kept the duplicates; the code does not show it.
- **An error the new output exposed:** finding 5 said 558 timestamps were NaN. Only 140 photostimulation onsets are NaN. The other 418 events (126 sample, 121 delay, 130 GO, 41 photostimulation) have timestamps that fall outside every trial. Finding 5 now says this.
- **Record of round 1:** Problem 5 now includes the roughly 5% rejection rate with session offsets and the bias toward large sessions (0.046 against 0.039). Problem 2 is now described as raised to test the duplicated rows, not as advice to adopt them.
- **Record of round 2:** added under `verifications` with all 34 claim results and the review of finding 1. The verifier agreed it is critical, and it stays critical with the unshown bin-5 clause removed.

**Not done**
- The verifier reported no place where the claims file misreads the paper, so I added no question to `questions/gable-2026.yaml`.
- Nothing is committed or pushed; the workflow does that.
