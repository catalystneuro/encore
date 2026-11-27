The one answered question changed `offline-bursts-above-shuffle` from not reproduced to reproduced, and that outcome rests on an assumption. The entry passes its checks (0 errors), the notebook runs cleanly from a fresh environment, and the handover is built. I did not verify my own work, and nothing is committed or pushed.

**Question: `offline-bursts-above-shuffle`.** I had asked how a shuffled population trace is thresholded before bursts are counted.
- **Answer:** "Changed." The paper does not settle the detail. The reader amended the criterion to list two readings, and the claim is reproduced under either, with the outcome marked as resting on the reading that gives it:
  - (a) each shuffled trace is z-scored again;
  - (b) each shuffled trace is held to the real trace's burst threshold (its mean plus 2 SD).
- **What I re-ran:** reading (b) is now a full reading, run under five seeds (the claim's second generator, seed plus 1, plus 1000 to 4000). Before, it was a single-seed variant.
- **Reading (b):** the true burst frequency is above the 95th percentile of the shuffles in all three recordings, and no shuffle reaches it. The outcome is the same under all five seeds.

  | Recording | True (bursts/min) | Shuffle mean | 95th percentile | Maximum |
  |---|---|---|---|---|
  | Ca_EEG2-1 Day 2 | 8.73 | 0.11 | 0.30 | 0.50 |
  | Ca_EEG3-4 Day 1 | 6.42 | 0.01 | 0.10 | 0.30 |
  | Ca_EEG3-4 Day 2 | 5.31 | 0.00 | 0.00 | 0.20 |

- **Reading (a):** the numbers are unchanged. The true frequency is below the shuffle mean in all three recordings (10.94, 8.81 and 8.48) under all five seeds, so this reading alone would give not reproduced.

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| offline-bursts-above-shuffle | not_reproduced | reproduced, `assumed: true` (reading b) |
| offline-skew-above-shuffle | reproduced | reproduced, unchanged (the answer says skew does not depend on the trace's scale) |

The other claims were not affected: no other questions were asked.

**What I updated:**
- **Notebook:** the claim's section now quotes the amended criterion, runs both readings under five seeds each, plots both sets of shuffles, and has a new Result paragraph. The summary table and the "differs from the paper" text are updated, and the skew conclusion notes that skew is unaffected.
- **Helper (`zaki.py`):** the docstring of `circular_shift_surrogates` now names readings (a) and (b).
- **README:** the outcome table and the paragraph on the burst claim are updated, and the stated run time is now about four minutes (it was three).
- **Attempt record (`attempts/zaki-2024-02.yaml`):**
  - The burst outcome is now reproduced with `assumed: true`. Its notes give both readings with seed ranges and say what the answer changed.
  - A new deviation states the assumption, citing the Extended Data Fig. 3l legend and the Methods "Burst participation analysis" passage.
  - The note on the skew claim and the `methods_unavailable` finding now mention the reader's answer. The finding still asks the paper's authors which thresholding they used.

The final run took 475 s, with peak memory of 0.88 GB.
