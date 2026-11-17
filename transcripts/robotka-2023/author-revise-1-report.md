I've worked through every point of the round-1 report, re-run the entry twice from a clean environment (the final run passed in 46.5 minutes), and the record's numbers match that run exactly. `check` reports 0 errors and the handover package is rebuilt. Nothing is committed.

**Outcomes changed (allowed in this round)**
- **fig5e-volume:** partially reproduced → reproduced, resting on an assumption. With the code's cross-validation, sound window and discriminant axes, R2adj is 0.094 (tolerance 0.1 ± 0.01), F(1,68) = 7.28, p = 0.0088. The criterion names the window and axes as readings, and the paper's printed F comes from the code's choices. The Methods' choices give 0.120, outside tolerance.
- **fig5-multiple-regression:** partially reproduced → reproduced, resting on an assumption. With the code's axes R2adj is 0.238 to 0.241 (tolerance 0.22 ± 0.022).
- **good-units-100:** kept not reproduced, disagreement recorded. The verifier would say partially reproduced. The criterion takes the count from one run, which gives 89 (tolerance 90 to 110), and it has no partial outcome when the total is out of tolerance.
- Every other outcome is unchanged and matches the verifier's.

**Added or corrected**
- **Cross-validation (B1):** a synthetic check shows what the code's scheme measures. With units that respond only to individual exemplars and carry no call-type signal, it scores 78.2%; the Methods' scheme scores 9.8% (chance is 10%). This is now stated in the deviation, the notes and the question for the paper's authors.
- **good-units-100 (B2):** per-bird counts for each of the 10 seeds are printed; ZF6M has 8 to 14 good units in every one, never within 16 ± 1.6. Of the paper's 91 listed units in the dataset, 29, 14, 9 and 18 per bird are good here.
- **Entropy Selectivity (B3):** this is about the claims file's reading, so I added a question to `questions/robotka-2023.yaml` and kept fig5g reproduced as the file has it. The notes say that with the code's normalized ES alone the claim fails (slope +18.9, p = 0.79).
- **Best ensemble (B4):** now taken from the 100-repetition ensembles, 68.4%.
- **figs4 (B5):** run on the paper's listed units: female minus male 5.9 points, p = 0.70. It stays blocked, because the link claim keeps outcomes off the listed names. The printed cause is corrected: a bird needs at least 16 good units.
- **fig6c call-type half (B6):** computed with UMAP and Ward on the 1,800 Figure 5 ensembles (not the legend's 10,000, for time). Mean 10.45 and median 10 under the code reading's units; the claim stays blocked for the acoustic half.
- **fig4a (B8):** the Methods' unit rule (125 units) also falls within tolerance.
- **KDE (B9):** the stored KDE is a 30 ms Gaussian (correlation above 0.99 in 107 of 114 rows), scaled by trials/5; this is a new finding about the data. I fixed the spikeless-row test in `kde_matrix`; it changed no result.
- **Cell 11 (B11):** now stripped by the handover.
- **Paper's code:** the notebook now prints the lines of the paper's code behind ES normalization, MRF scaling (one pooled SD, which settles B10), `eigh`, the PCC > 30 filter and the 2-birds-per-sex test.
- **Missing 9 units:** they are listed with their electrodes beside the 18 pickles the dataset holds for that site.
- **Record and entry:** round 1 is recorded under `verifications`. The README, `entry.yaml` (runtime 47 minutes) and the lock (umap-learn added) are updated.

**Not done**
- The 9 `.old` units cannot be matched by spike train, because that sorting is not deposited.
- I did not search for the vocalization database outside aa-5 and the paper's code repository.
- The 10,000-ensemble clustering was not run, for time.
