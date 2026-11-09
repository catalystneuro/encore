I've handled every point in the round-2 report. The verifier agreed with all 28 outcomes, and no outcome changed. Nothing is written under `proposed`, because none of the points calls for a different outcome.

**Corrections**
- **fig3c-home-cage-above-both-sessions:** the record notes, the notebook's conclusion and summary, and the README now say plainly that the outcome rests on the criterion's named variant (Bonferroni-corrected paired t, p = 0.038 / 0.035). It does not hold under Tukey's HSD (p = 0.30 / 0.19).
- **fig3d-gamma-rises-with-time-in-arena:**
  - The record and the notebook's conclusion now say that 20-s bins with the end anchor (r = 0.662, p = 6.9e-5) also fall within tolerance.
  - The record now keeps "but not proof of it" on the first-minute movement, and notes that some differences are small (403.9 against 389.2).
  - In the round-1 reason, "Asked for" now says the verifier suggested those outputs under what it could not check. I left its "620-780 s" as it wrote it, since that is its own wording; the round-2 response points to the 526 to 780 s that the notebook prints. I also changed "Asked for" to "suggested" in the round-1 figs5 reason, for the same reason.
- **fig3a-each-hemisphere-significant:** the p-values for rat 3's arena session 2 are now given for each epoch reading (p < 1e-100 for 2-s epochs as delivered; 7.1e-80 and 4.7e-93 with the peak-to-peak rule; 6.2e-30 and 6.8e-33 with 10-s epochs). Before, the text said "p < 1e-100 either way".
- **Summary cell:** it now says "and 15 claims", so the data_missing total reads as 16.
- **data_missing finding:** "bipolar recordings" is removed. That claim is blocked as metadata_insufficient, and that finding already covers it.
- **README:** I removed "It takes under a minute", because no printed output supports it.

**Run and record**
- `python tools/entry.py all entries/crcns-bf-1-nair-2018` passes with 0 errors, and the notebook ran in 20 s. I checked every number quoted in the new text against the re-executed outputs, and they match.
- Round 2 is recorded under `verifications`, with each claim's agreement, outcome, the verifier's reason in its own words, and my response.

**Not done**
- I added nothing to `questions/crcns-bf-1.yaml`. The verifier reported no new misreading of the paper. Its open points are the fig3b test choice and the fig3d bin width, and both are already asked there.
- The two fig3b not_reproduced outcomes still depend on the claims file's one-way ANOVA on per-rat means. Every within-rat test finds the effect, so the verifier says they reflect the choice of test more than the data. That question is waiting for a reader's answer.

Nothing is committed, as the workflow does that.
