I've revised the attempt for verifier round 2. No outcome changed and nothing is proposed for a third round. The entry re-ran cleanly (`entry.py all`: 0 errors, the notebook passes in 131 s), and the corrected text matches the new run's numbers.

**Outcomes:** all 20 are the same as before. The one change is that fig7b-window-start-slide now carries `assumed: true`. The verifier pointed out that under the range reading of tuning, which the rest of the attempt uses, the fig7b ratio is undefined. So that "not reproduced" rests only on the SD reading (7 or 8 units). A new deviation in the record says this, and the notebook conclusion, the summary table and the README now mark it as an assumption.

**Corrected (in the notebook, the attempt record, and the README where it applied):**
- **fig4e:** under the SD reading it is partially reproduced in 11 of 12 readings, not 10. The twelfth reading is described as neither a pass nor a partial.
- **suppfig1:** the claim that the strongest trace on top at -150 ms comes mostly from noise shared within trials now says "suggests" instead of stating it as shown. It gives the verifier's reason: each disjoint half uses about half the trials.
- **Summary, SD reading:**
  - It no longer says the peri-movement space "performs best". It now says that space has the highest mean in 5 of 6 settings (the kinematic space is higher with O3b/O4b, 0.134 against 0.129) and that no difference is significant (p 0.47 to 0.98).
  - The summary had said these units have "clearer tuning", but no output showed it. I added an output to cell 11: their split-half reliability has a median of 0.57, against 0.20 over all units. The summary cites it and notes that the units are selected on the same trials.
- **fig7d deviation:** raw and z-scored axes agree in 11 of 12 pairs, not "23 of 24 readings". The pair that differs is named.
- **fig7c:** the conclusion and notes now say that under the SD reading the upper limit (0.123) is below the best peri-movement performance (0.209), so it is not a ceiling.
- **Round-1 record for fig6d:** I removed the round-1 problem 6 from the recorded reason, because the verifier had marked it as not affecting a conclusion.
- **Round 2** is recorded under `verifications`, with the verifier's agreement, outcome, reason and my response for each of the 20 claims.

**Not done:**
- fig7c still runs only with the default movement-onset and proto-trial settings (O3a/O4a). The record says so, the verifier noted it, and the claim is blocked anyway.
- No questions were added to `questions/000140.yaml`, because the verifier found no place where the claims file misreads the paper.
- Nothing is committed. The working tree also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others), and I left them alone.
