I wrote `claims/robotka-2023.yaml`. The quote checker passes with 0 problems. Nothing was committed, and the other untracked files in the working tree were there before this run.

**Text read:** the version of record, with the STAR Methods and the full supplement (SI Figs 1 to 11 and their legends, at the end of the PDF). Table 1 was read from the text. I did not open the PDF, since no figure or table was garbled. I also read the analysis code, `ftheunissen/Ensemble-Code-Cell-Reports-2022` at commit f2d2376. Its printed outputs match the Figure 5 statistics: F(1,79) = 8.975, 6.73 and 8.75, and F(4,76) = 5.832.

**Claims:** 28 in all: 27 findings plus one link claim checking the stimulus set.
- 27 have quotes. The other one, the Table 1 SNR claim, is marked `inferred` because its values appear only in the table.
- 14 have statistics.
- All 28 have criteria.
- Data: 20 use this dataset alone, 5 need outside inputs (`with_inputs`), and 3 use the anesthetized dataset CRCNS aa-4, which is a separate deposit (`elsewhere`).

**Details the paper leaves open, with the readings named.** These are recorded once in the opening comment as shared rules C1 to C12, which the claims refer to.
- **Response strength Z:** the Methods read as subtracting the mean; the code divides by the SD only. This does not affect any decoder result.
- **Per-call-type Z for the selectivity index:** (a) the mean of trial Z over the call type; (b) the code's mean(d)/sd(d) within each call type.
- **Cross-validation:** (a) the Methods hold out one exemplar stimulus per call type; (b) the code holds out one random trial of every stimulus, repeated 100 times for ensembles.
- **PCC:** (a) the mean of the row-normalized diagonal; (b) the code's trace over the number of test trials.
- **The 1,746 ensembles:** (a) the code keeps the 1,800 sampled ensembles with PCC above 30%, a filter the Methods never state; (b) all 1,800.
- **Top ensembles:** the Results and Figure 4 legend say top 10%, the Methods say top 5%.
- **Sound window for the MPS:** the Methods say the first 500 ms; the code uses 500 ms before to 500 ms after onset.
- **LDA axes:** the Methods' "first three", read as the three largest eigenvalues. The code's `eigh` puts the smallest first, so its literal choice is run as a variant. The regressions use log volume, as in the code.
- **Neural noise:** variance (Results and code) or SD (Figure 5 legend).
- **Entropy Selectivity:** the diagonal normalized to sum 1 (code) or used as is (Methods formula).
- **Neural clustering:** UMAP then Ward linkage (code), or Ward linkage alone (Methods).
- **Auditory t-test:** n − 1 degrees of freedom (standard) or n (code).
- **Smaller ones:**
  - The auditory count is 607 in the Methods but 609 in SI Fig 2.
  - The printed p = 0.21 for t(80) = −0.808 is a one-sided value.
  - The combined anesthetized regression is printed as F(2,341) with four regressors.
  - The per-region F(4,125) and F(4,170) match neither dataset's corrected sample size, so the dataset behind them is read as anesthetized.
  - The ensemble size for the sex comparison is read as 15 units.

**Missing material a claim needs:**
- **Vocalization database:** the acoustic clustering claims (Fig 6, the acoustic-label decoding, SI Fig 10) need the lab's database (3,405 bouts from 45 birds). The paper gives no deposit for it, and the code reads parameter and segment tables that are not in the repository.
- **Anatomical areas:** the area claims (SI Figs 5, 6, 9) need each unit's area. If the dataset does not hold it, those claims cannot be tested.
- **Spike-sorting quality indices:** the Qisi and Qacc indices in Table 1 need full spike trains, which the dataset does not hold, so they are not claimed.
