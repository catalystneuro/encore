The reader's answer changed one claim, `ed3k-robust-to-controls`. It now comes out reproduced; before the answer it was partially reproduced. The full entry check and run passed with 0 errors (about 40 minutes), and the handover is built in `executed/000939-duszkiewicz-2024/handover/`. Nothing is committed or pushed, and I did not verify my own work.

**The question.** The claim said ADN-HD cells have higher multipeak scores than PoSub-HD cells. The paper's legend for Extended Data Fig. 3j gives the test (Mann-Whitney U, z = 4.25) but no direction. Its own counts of cells kept below 0.05 (69 of 97 ADN-HD, 789 of 1,602 PoSub-HD) point to lower ADN-HD scores.

**The answer.** The reader agreed the claims file had misread the paper and amended the claim. The statement now says only that multipeak scores differ between the two populations. The multipeak test counts in either direction at p < 0.05, and the three Fourier distance tests keep the paper's direction.

**What changed in the analysis.** The analysis itself is the same and gives the same numbers:
- **Fourier distance tests:** PoSub-HD spectra are closer to the FS signature than ADN-HD spectra under all three controls and all four readings, with p from 0.019 to 5e-22. That holds with multipeaked cells excluded (762 and 69 cells; paper 789 and 69), with noisy clusters excluded (1,399 and 81; paper 1,472 and 83) and at 10 cm/s (1,512 and 97).
- **Multipeak test:** z = 4.18, p = 3e-5 (paper z = 4.25). ADN-HD cells score lower than PoSub-HD cells (median 0.022 against 0.049), which the amended criterion now accepts.

**Outcome per affected claim:**

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| `ed3k-robust-to-controls` | partially reproduced | reproduced |

**Files updated:**
- **Notebook:** the claim's statement, a note on the amendment, a line that checks the amended criterion (both parts printed True in the run), the result cell and the summary row.
- **Entry README:** the claim's row now reads Reproduced.
- **Attempt record:** the outcome, with notes saying what the answer changed and what the outcome was before.
