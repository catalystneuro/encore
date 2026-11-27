## Report on round 2 of hasnain-2025-01

**Outcome changes: none.** All 19 outcomes are as in round 1.
- 11 claims stay blocked (`data_missing`).
- map-session-selection, both fig4d claims and fig4e stay not reproduced.
- fig4b and fig4c-alm stay partially reproduced.
- fig4c-medulla stays reproduced. It is now marked `seed_sensitive`, because under two of the five seeds the potent mean is 52.3%, just above its 51.92 limit.
- fig4f stays partially reproduced. The verifier would give not reproduced. I kept the outcome and recorded the disagreement under `response`: when region labels are shuffled only within each session, 0.1% of ALM units lack a medulla neighbour, against 25.7% observed. So the first part of the criterion holds and is not an effect of session clumping. The second part holds only in part.

**Added or corrected, by report point:**
- **Unit selection (B1):** the electrodes table has CCF x, y, z for each electrode but no region label. Among units classified good, the nearest other such unit carries the same label for 97.3% of them. Using that nearest-neighbour label, I formed two more readings of "good": G2 (`unit_quality`) and U2 (all units). Neither recovers the paper's counts. G2 gives 19 ALM and medulla sessions with about 2.5 times the paper's units.
  - A second notebook, `reproduce_hasnain_2025_g2.ipynb`, repeats the Figure 4 tests under G2. Under G2, fig4c-alm would be reproduced and fig4e would be reproduced with N2.
  - The outcomes still rest on G1 (`classification`), marked `assumed`. Its bilateral unit counts are near the paper's, while G2's are 2.7 to 2.9 times them. The G2 results are in the notes and in the finding that asks the authors.
- **Decoding (B2):** I added three variants: R2 over the whole span, the median over bins, and decoding with the example.m z-score. I also added per-bin R2 by epoch and the target variance at each bin. All R2 stay far below zero. R2 tracks the number of predictors per training trial (Spearman −0.61) more than the heavy tails (−0.24), so the cause is overfitting of a nearly unpenalized per-bin fit.
- **UMAP (B3):** the embedding is now also coloured by session, with the per-session null dimension and extent, the within-session shuffle null, and a variant without the session whose medulla has a null dimension of 1.
- **Selectivity (B5):** a shuffle within blocks of 30 trials and the share of right trials by fifth of the session. Drift does not explain the high values.
- **Text (B6):** every result text is rewritten from the new outputs.
- **Covariance (B9):** bins without tracking are now excluded from the total covariance. They are at most 0.1% of bins.
- **Trials:** the printed trial labels and sample-cue times showed that 446 correct and error trials had a 1.8 s or 0.3 s delay. They are now left out. I added a minor data finding (number 12): the trial table has no column for delay duration. I also printed the moving bins per epoch.
- **Record:** round 1 is recorded under `verifications`, with the verifier's reasons and my responses. Findings 1, 2, 7, 9 and 11 are updated in place, so the numbering is unchanged.
- **Run:** `python tools/entry.py all` passed: 27 minutes for the main notebook and 34 for the G2 notebook. A second full run gave identical outputs.

**Not done:**
- No `questions/hasnain-2025.yaml`. The verifier reported no misreading of the claims file. The two gaps it raised (the R2 denominator in M8, and whether the example.m variant counts as a reading) go to the paper's authors through the findings and claim notes.
- B7 (subspaces fitted on all trials, test trials included) is left as it is and stated. The fit is unsupervised and within one region.
- I did not commit or push.
