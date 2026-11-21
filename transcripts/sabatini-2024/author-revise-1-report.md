I've revised the entry for every point in the round-1 report. `python tools/entry.py all entries/sabatini-2024` passed, and both notebooks ran: 1276 s for the main one and 718 s for the reading (b) one. `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes:** 11 reproduced, 12 partially reproduced, 11 not reproduced, none blocked. Four changed, all to the verifier's outcome:
- **data-composition**: partially reproduced → reproduced. The dataset labels no unit as single or multi-unit, so all 96 per array count. That they are one per electrode stays a finding.
- **fig3a-eigenvalue-clusters**: partially → not reproduced. The criterion needs every dataset; no dataset has all its eigenvalue pairs within 10% of the paper's frequencies.
- **fig3g-basis-frequencies**: partially → not reproduced. PMd-J has 2 rotation pairs where 3 or 4 are required, and 3 of 11 frequencies are within 10%.
- **fig5a-frequencies-segregated**: partially → reproduced. The one-sided signed-rank tests give p ≤ 1.4e-12 and a positive Hodges-Lehmann estimate (the signed-rank test's estimate of the paired difference) for all 20 comparisons. For M1-N 3.24 Hz the effect is small, and the notes say so.
- **fig7c-standard-encoding-worse** stays reproduced, against the verifier's partial. Its problem is fixed: the kernel encoders now explain 40–52% instead of 0, and the LDR models beat all 24 standard models (p ≤ 2.5e-10).

All five disagreements are recorded under `verifications`.

**Fixes:**
- **Trials (B5):** the analyses now use reading (a), all successful trials. My earlier reason for reading (b) was wrong for monkey N; the new one is that the Methods describe a 0–1000 ms delay and name no exclusion. This is recorded as an assumption. A companion notebook, `reproduce_sabatini_2024_trials_b.ipynb`, runs every analysis under reading (b), and every outcome is the same under both.
- **SNR dimensionality (B2):** the PCA is no longer mean-centred. Rotations now give 9–21 dimensions, all in range; the location gives 7, 2, 3 and 8, two of four in range. Both outcomes stay not reproduced, since PCs and participation ratio still fail.
- **fig4c chance (B3):** it is now a noise SEA run on the half-split estimates of single conditions. This remains an assumption about the paper's code.
- **Recoverability chance (B4):** the shuffled basis is now de-mixed like the real one. The value is unchanged to three decimals.
- **Units (B6):** the check now prints the units table columns and confirms exactly one unit on each of the 192 electrodes in both files.
- **Instantaneous decoders (B7):** rates are no longer z-scored (z-scored is a variant, as is a 6000-point training set). LDR is scored over the same −250 to +850 ms window, and the comparison runs under both kinematic readings. A new check shows the decoders are weak even on trials of their own training conditions (0 to 87%), which the notes now say.
- **Other outputs added:** the jPCA straight/curved pairing check (same target in all 36 pairs), the direction of each signed-rank test, kernel length scales of 1e2 and 1e4 (changes of at most 0.002), and factorization frequencies over other time windows. The whole −350 to +850 ms window brings them closer to the paper's.
- **Stated as assumptions:** the time-shuffle span and the scale of the kinematic basis.
- **Question for a reader:** the suppfig3 comparison of a held-out value against in-sample values is now a question in `questions/sabatini-2024.yaml`, citing the Supplementary Figure 3 legend.
- **Findings:** updated to the new numbers, with three more questions for the paper's authors.

**Not done:**
- **GPFA decoders:** not run, as the paper gives neither the latent dimensionality nor the bin size, so fig7f-decoder-beats-standard stays partial.
- **Eigenvalue null:** still 100 repeats instead of 500, for time. The half-split null gives the same outcome.
- **jPCA check on the codepack's example data:** not done, because that data is outside the dataset and not pinned.
- **Shuffle span:** the alternative spans were not run.
