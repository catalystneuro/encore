None of the 20 outcomes changed. The verifier agreed with every one: 18 reproduced, persistent-activity not reproduced, and probe-cells-mfc blocked because the methods are underspecified. The entry re-ran with `python tools/entry.py all`: the checks pass with 0 errors and the notebook runs in about 330 s. A second run gave the same numbers.

**What I added in reply to the report:**
- **Tie handling (problem 1):** `perm_ttest` and `signflip_test` now take a `ties` option that counts permuted values equal to the observed one (`>=`). The main reading still uses the strict `>`, because the paper's code (`permutationTest.m`) uses it, and the record now says so. A variant reruns the same permutations with ties counted:
  - maintenance-cells-mfc: label shuffling stays at 140 and 139, sign flipping drops from 144/143 to 142/141, and all stay within tolerance;
  - probe-cells-mfc: label shuffling gives 108 and 103 (outside tolerance), sign flipping 118 and 111 (inside), so the readings still disagree and the claim stays blocked.
- **Seed repeats for sternberg-concept-mtl (problem 4):** three more seeds give 95 to 97 (two-sided) and 99 to 100 (one-sided), all within tolerance.
- **Probe seeds (problem 3):** each extra seed now prints its tolerance flag.
- **Data checks in cell 5:**
  - Encoding 2 and 3 timestamps are 0 exactly when the trial's load leaves them out, which the pooled encoding rate relies on.
  - The notebook now lists trials with under 0.5 s from fixation to Encoding 1. This found a third odd trial: subject 9, load 3, where the fixation and Encoding 1 onsets are 0.03 ms apart, so the baseline window falls on the image. I added it to the "other" finding and the summary. All three odd trials are kept, as the paper's code keeps them.
- **Text updates:** the conclusion cells and record notes for sternberg-concept-mtl, maintenance-cells-mfc and probe-cells-mfc now give the new numbers, and the deviation for maintenance-cells-mfc explains the tie rule.
- **Verification record:** round 1 is recorded under `verifications` with all 20 claims, each with `agrees: true`, the verifier's reason and my response.

**What I did not do, and why:**
- **Subjects 13 and 14 (problem 6):** the conclusion cell, the summary and the record already say these may be the same patient. The verifier saw the notebook with those cells removed, so I made no change.
- **screening-concept-mfc seed sensitivity (problem 2):** the notebook already shows the four seeds and the 20,000-permutation re-test (26 units, within tolerance), so there was nothing new to add.
- **Problems 7 and 8:** the verifier says neither needs a change.
- **No questions file:** the verifier found no place where the claims file misreads the paper, so I added no question.

Nothing is committed, as instructed.
