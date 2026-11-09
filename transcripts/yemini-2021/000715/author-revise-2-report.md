No outcome changed in this round: every claim keeps the outcome the verifier last agreed with. I propose two changes to `blocked` (`methods_underspecified`) for round 3 to review. I re-ran the entry with `python tools/entry.py all`: the checks pass (0 errors) and all four notebooks pass. The conclusions now match the new numbers, and the handover is rebuilt.

**Proposed changes (written under `proposed`)**
- **tables6-tail-pvq-and-post-stimulus:** I agree with the verifier. The notebook's own rule says a claim whose outcome differs between the duplicate-removal readings is blocked. This claim holds in full under two readings and only in part under the third, so the rule blocks it, the same way it blocks fig6de.
- **fig7de-optimal-coloring-violations:** I removed the note saying the outcome does not depend on the sparsity. I then gave 2000 and 3000 the criterion's full 7,500 runs each. At 3000 the best 3-reporter value is 9.90%, which is inside the tolerance. At 1500 and 2000 it is 6.95% and 8.38%, below it. So the outcome depends on a setting the paper does not give: reproduced at 3000, partially reproduced at 1500 and 2000. These runs are in a new notebook, `optimal_coloring_sparsity.ipynb` (24 min), so that no notebook runs past its time limit.

**Outputs added**
- **Storey π0:** `wholebrain.py` now also estimates π0 with the bootstrap choice of λ, which is the default of MATLAB's `mafdr` (I checked this in the MathWorks documentation). A new cell prints π0 and the q-values each claim depends on, under λ = 0.5, the bootstrap and π0 = 1.
  - None of the outcomes change under the bootstrap estimate. fig6ef's largest q is 0.033 to 0.038.
  - With π0 = 1 (Benjamini-Hochberg, which is not Storey's method), AVF and AVJ reach q of 0.062 to 0.088.
  - fig6ef is now marked `assumed`.
- **Position-only, rotated starts, under the atlas variants:** 45.1 to 46.7% under three of the four variants, which is inside the tolerance, and 37.8 to 38.8% with 100 alternations. I kept "not reproduced" because the rotated start is not the paper's method.
- **fig7b:** the table now shows the best single worm after eight annotations for every alignment and ranking.

**Text corrected**
- fig7bc now states plainly that the best rotated-start reading misses the bound by 0.02 points, and says which class readings are inside the tolerance under each atlas variant. The summary sentence "changes no outcome" is qualified.
- The ms1-uncertain-first gap is now 3.5 to 7.8 points.
- The data_missing finding now says nine claims need the tails, not eight.
- The round-1 entry now says 16 unreviewed claims, not 15.
- The README is updated.
- The round-2 verification is recorded for all 32 claims, with the verifier's reasons and my responses.

**Numbers that moved on this machine.** The values at sparsity 100 came out at 1.71% with 30 reporters, against 1.72% with 27 earlier, even with fixed seeds. The SLSQP success count is 2,043 of 2,064, against 2,046 of 2,065 earlier. Reading b also moved in the last digit. The record uses this run's values and says the sparsity-100 results differ between machines.

**Not done**
- I did not measure how much replacing MATLAB's fmincon with SLSQP affects the detection. The verifier agrees this no longer bears on the outcome.
- I added no new reader question: the fig7de misreading is already asked in `questions/000715.yaml`.
- Nothing is committed, as instructed.
