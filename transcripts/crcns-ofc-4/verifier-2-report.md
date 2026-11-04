**Verifier report, round 2: crcns-ofc-4-schuck-2016-01**

The claims file has 29 claims and the attempt record has 29 outcomes: 7 blocked and 22 tested.

**1. Outcomes and assumptions**

I agree with all 29 stated outcomes. I have comments on four of them:

- **fig4b-error-vs-matched (not_reproduced, assumed):** I agree, but the outcome goes against the criterion as written. The criterion passes when trial 0 is lower than the matched courses at p < 0.05. Under voxel z-scoring with matched courses (a) it is: p = 0.0003 (cell 76).
  - The record adds a class-matched reading (c) and states it as an assumption. The confound behind it is real: Enter trials decode at 0.90%, Exit at 11.79% and Internal at 14.30% (cell 34).
  - The record says the paper's matched courses were "of the same mix" of classes. That is an inference. The paper says only "seven consecutive trials with no behavioral error" (Figure 4B legend).
  - Under voxel z-scoring, reading (c) is at floor: 1.59% against 1.42% and 0.88%. It could not show a drop, and the notes should say so.
  - The evidence that decides it is the map reading, where Enter trials are not at floor (8.02%). There, error trials are not lower under the criterion's readings (p ≥ 0.69) or under (c) (p ≥ 0.45).
- **figs5-euclidean-distance (reproduced, assumed):** This follows the criterion. The count control is stated: with correct-trial counts held constant, distance and error rate are not related. The assumption is reasonable, but the cited numbers are stale (see section 2).
- **supp-errors-stable-over-blocks (reproduced):** This rests on counting one error per block, the same as supp-errors-by-trial-class and fig4a. Those two are marked `assumed: true`; this one is not. It should be marked for consistency.
- **fig4a (partially_reproduced, assumed):** I agree by the criterion's wording. r = −0.268 lies inside the paper's CI, but p = 0.205 (cell 65).

The other `assumed: true` outcomes state reasonable assumptions:
- supp-errors-by-trial-class: one error per block, with the class taken from the trial before the block.
- supp-errors-not-by-age-category: the span reading.
- figs2c and fig4a: voxel z-scoring.

**2. Text the printed outputs do not support**

- **Cell 52 and the figs2c record notes (and the round-1 response):** "With maps z-scored by map, accuracy is 14.90% (outside tolerance, one-sided p = 0.018) and no component is above 50% (p >= 0.17)". Cell 51 prints 14.79%, one-sided p = 0.0247, and component p of 0.196, 0.443 and 0.295. The outcome is unchanged.
- **Cell 74 and the fig4b-decline record notes (and the response):**
  - "smallest p = 0.37" with voxel maps: cell 73 prints 0.321 (voxel/after/span, matched a, trial).
  - "span reading, matched courses (a), slope 1.45 percentage points per trial, p = 0.019": cell 73 prints 1.47, p = 0.0394. The interaction p = 0.030 matches.
- **Cell 81 and the figs5 record notes (and the response):** "mean partial r 0.075, one-sided p = 0.21; 0.087, p = 0.14". Cell 79 prints 0.072, p = 0.215 and 0.076, p = 0.175.
- **Cell 18 and the supp-errors-by-trial-class record notes:** "Exit and Internal are 1.18 to 1.20% together". Cell 17 prints 0.60% for the two together. The 1.18–1.20% is the most either class can reach if it is given all 44 unknown errors.
- **Cell 81 and the figs5 record notes:** "With the strict reading (37 errors, 16 participants)". The transition table uses all 39 strict states (cell 8, and the record's own fig5 deviation, "39 strict"). 37 is the fig4b count.
- **Cell 45:** "Under the two readings of O3 the result is the same or weaker". Previous category under O3 (a) with map z-scoring is stronger: p = 0.0129 against 0.038 (cell 44).
- **Cell 9 and the behavior-error-rate record notes:** "about half the blocks hold one designed trial besides the error trial". The least-squares fit (cell 8) gives 0.52 extra designed trials per block after an Exit trial, but 0.87 per other block. "Half" fits only the blocks after an Exit trial.
- **README and the Summary (cell 82):** "Enter trials decode worse than other trials on single volumes". This holds only under voxel z-scoring. With map z-scoring, Enter trials decode at 8.30% against 4.85% for Exit (cell 34).
- **README:** "It takes about four minutes". Cell 83 prints 5.4 min.
- **Summary (cell 82):** "Enter errors are 181 of 225 error blocks, 79%". 181 of 225 is 80%; 79% is 181 of 228 (cell 8).

All other Result sentences, the Summary, the README table and the record notes agree with the printed outputs.

The record's round-1 reasons put my points accurately in other words: problems 1–10 and the requests in C are carried over correctly. "27 of 29 agree" matches my round-1 table.

**3. Round-1 points**

Resolved:
- **1 (O3):** Both readings are now built from the error blocks; 16-way accuracy is 8.10–9.38% and the outcomes are unchanged (cell 38).
- **6:** I checked the code: reading (b) now uses the error trial as the trial two back.
- **7:** The comparison with '16rebuilt' is added.
- **8:** The helper now follows the Methods, and the conflict is recorded as a paper_inconsistency.
- **9:** A variant with by-participant category slopes is added (χ² = 54.1).
- **10:** Cell 4 now lists every variable of every run file, and none is a mask or coordinates.
- **C:** The block composition, the O3(b) result, the class-matched comparison and the trial-count control are all added.

Resolved as far as the data allow:
- **2 (error undercount):** The block composition is now shown. The bounds stay 1.98–3.10%, and the undercount is stated.

Still bearing on a conclusion:
- **3 (class confound):** Handled by reading (c), but the fig4b-error-vs-matched outcome now rests on a reading that is not in the claims file and is at floor under voxel z-scoring (see section 1).
- **4 (trial counts):** The control is done and shows no relation once counts are held constant. figs5 stays reproduced on the criterion's wording alone, with stale numbers.
- **5 (slow signal):** The slow component is now stated. One thing is unexplained: correct Enter trials decode at 0.90% under voxel z-scoring, far below the 6.25% chance level (cell 34). That suggests the volume 2 TRs after onset carries the previous (Exit) trial's state. If so, all three fig4b claims test signal lag more than errors.
- **New:** The stale numbers in cells 52, 74 and 81, and in the record, need correcting from the printed outputs.
