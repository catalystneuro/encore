The round-1 revision is done. The entry passes `check` and runs from a clean environment in 286 s with no errors. Nothing is committed.

**Outcome changes**
- **fig6-nacl-unknown-interneurons:** partially reproduced → reproduced (assumed). With each trace z-scored, all six classes are significant under every FDR reading; on dF/F0 it is still 4 of 6. The verifier had agreed with partial, so round 2 should look at this one.
- **fig6gi-stimulus-specific-correlations:** reproduced → partially reproduced (assumed), as the verifier gave. Under the new main reading the odor pair is not separated (p = 0.17) and the split test gives 91/96/95. Only removing both members of a pair passes all three.
- **fig6-asj-ric:** still partially reproduced (assumed), now 5 of 6 parts. The verifier saw 4 of 6 under "both" and 3 of 6 under the other readings. Now the deposit and none readings give 6 of 6, both removed gives 4, and dF/F0 gives 3.
- **Blocked reasons:** fig7de is now `not_runnable`, since the solver is public but needs MATLAB. fig4bd and fig4e are now `other`: their input, Table S4, turned out to be public, and I did not take that analysis up. All three are still blocked.

**What I found and changed**
- **Grid spacing is wrong (new metadata finding):** in all 21 files, neurons sit at half their NeuroPAL x/y coordinates in the calcium segmentation, so the movie is binned 2×2 and its spacing is 0.533 µm, not the stated 0.267. The 5 µm rule now uses the corrected spacing.
- **Problem 1:** I added the deposit reading and a cross-tab. The rule's removals barely overlap the 126 traces the deposit lacks (20 under one, 27 under both). The paper's Table S6 shows it tested fewer traces per class than the deposit holds. Removing one member of a pair comes closest to its counts, so that is now the main reading, with deposit, both and none as variants.
- **Normalisation (new assumption):** Table S6's p values are matched far better by z-scored traces than by dF/F0 (rank correlation 0.90–0.96 against 0.62–0.73). That holds even on the deposit's own traces. Z-scoring is now the main reading for the response tests and the PCA, with dF/F0 and min-max scaling as variants.
- **FDR family:** Table S6's legend settles it: q values pool all three stimuli.
- **Storey q values (problem 4):** applied to the paper's own p values, my q code reproduces its q values at 0.05 in 273 of 285 tests, so the method stands. On our p values pi0 is 0.222, so q falls below p for many tests; Benjamini-Hochberg is now shown as a conservative check.
- **AWC:** I search all 21 files for ON/OFF, and none name it. The NeuroPAL image does carry the side: CyOFP1, the srsx-3 fluorophore according to Table S1, agrees with the deposit's labels in 19 of 21 heads. The claim stays blocked as its criterion requires a label. A variant using these image-derived labels gives p = 0.68 and 0.060.
- **Other fixes:**
  - The clock-check text is corrected (AWC gives no check) and a time-shift check on ASE is added.
  - The deposit turns out to be one frame later than the dandiset in every file.
  - AMSO and HMC are no longer tested.
  - The per-file distance and pair tables are printed, along with the deposit's own medians and the ASJ/RIC rows for every reading.
  - The summary cell, which held only the placeholder "SUMMARY", is now written.
  - The record's notes, inputs, findings and `verifications` are updated, along with the README.
- **Question for a reader:** in `questions/000541.yaml`, whether the median of 18 covers heads and tails together (problem 8). I did not change the claim.

**Not done**
- fig4bd and fig4e: their inputs are public but I did not take up the analysis.
- fig7de: I did not port the MATLAB solver.
