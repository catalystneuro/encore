All 22 outcomes are unchanged, and none has a `proposed` change. The round-2 verifier agreed with every outcome, and nothing in my revision gave a reason to change one. I re-ran `python tools/entry.py all entries/000128-churchland-2010` after the last edit: it passes with 0 errors, `entry.py check` also gives 0 errors, and the conclusions match the new numbers.

**Text corrected to match the outputs:**
- **fig4d (cell 17 and notes):** the "less than half" sentence now holds only where it is true. The Pearson mean, 0.051, is below half of 0.13 (0.065). The Spearman mean, 0.072, is 65% of 0.11.
- **fig8-model-weak-correlation (cell 59 and notes):** the range is now given for each reading. The lower bounds run from -0.430 to -0.385 and the upper bounds from 0.350 to 0.428, where the old text gave the outer envelope "-0.43 to 0.43". The verifier's round-1 reason ("about -0.40 to 0.40") stays in the record as it gave it.
- **Summary (cell 64):** T2 is now described as 1786 trials, which is 90.8% of the 1967 trials with delay > 400 ms and 77.8% of all 2295 train trials. T1's 73.8% is now stated as a share of the same base. The README contains no such percentage, so it needed no change.
- **Notes on several claims:** I removed values from the earlier record that the notebook no longer prints. These were in fig4d, fig6-performance-vs-dimensionality, fig7b and prep-dimensionality, which the verifier listed. I did the same for fig3, fig6-peri-movement-space-best and fig6-each-dimensionality, which it did not list.

**prep-dimensionality:**
- The verifier withdrew its T-matrix point, and I checked the supplement text myself. It defines the matrix as "T was c×n …", which is the claims file's matrix. So I removed the conditions × (neurons × times) variants from cell 32, since they test a reading the paper rules out.
- Cell 33 and the notes now quote that definition. They also say that "all neurons" points to reading N2, which gives 18 components.
- I added the maximum trial count per condition to cell 10. It is 22, not the 27 the verifier wrote, and the texts now say 10 to 22.
- The question in `questions/000128.yaml` no longer asks about the T-matrix. It now asks only whether the claim is a range or a lower bound, and quotes the supplement's "7-10 dimensions were required" next to the main text's "at least".

**Record:** round 2 is now under `verifications` in the attempt record, with the verifier's reasons and my response for each of the 22 claims.

**Not done:** the verifier's remaining point about fig4d, that the paper's unit and trial selection is not recorded, cannot be settled with this dataset. It stays a recorded deviation. Nothing is committed, as the workflow commits the changes.
