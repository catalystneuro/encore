I've written the claims file at `claims/000115/10.1016-j.neuron.2021.07.029.yaml`. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** I read the PubMed Central accepted author manuscript (PMC8497431), not the version of record. It has the main text, STAR Methods, all figure legends, and the supplement PDF (Supplementary Figures 1 to 8) extracted into the same `.txt`. I did not need the PDF, and I did not use the bioRxiv preprint text for claims.

**Code read.** The analysis code is LorenFrankLab/Gillespie_Neuron_2021, tag v1.0, commit 1be6a6a7, which is what the Zenodo record 5140706 points to. The criteria follow its MATLAB scripts. The ripple detector, the linearisation and the clusterless decoder itself are not in that repository; the paper cites them as separate software, and the file names them.

**Counts.**
- 33 claims, all with quotes.
- 14 claims carry statistics, 27 entries in all.
- 33 criteria.
- 9 claims carry expected values with tolerances: session and block counts, the remote fractions (35.1/41.1/34.5/47.2%), the ~95% continuous share, the >90% same-segment check, the previous goal share (~20%) and fold change (~2), the R² values of Figures 4C and 7, and the 0.5 misclassification rate.

**Where the Methods and the code disagree** (Methods used for the main result, code run as a variant):
- **Figure 3B/C null:** the Methods say 5000 random draws; the code makes 100 per session and pools them. Three readings are named: 5000 per session pooled, 100 per session pooled, and 5000 over the subject's pooled events.
- **Figure 3D/E/8B GLM trials:** the Methods exclude the first trial block. The code includes it, with the previous goal predictor set to zero there. The legend's trial counts look like the code's (711 search trials, against 534 after the first block in Figure 5A).
- **Figure 5D:** the Methods say 1000 subsamples; the code uses 100.

**Details the paper leaves open, with the readings named:**
- **Figure 5D classification:** a random draw from the fitted probability (the code) or a 0.5 threshold.
- **Figure 4B "late" trials:** task phase ≥5, or the code's >4, which puts errors after four rewards into both the early and the late set. The early set is task phase <5, which matches the legend's counts.
- **Figure 4C reward count:** including the current trial's reward (the code) or rewards before the trial.
- **Figure 7:**
  - "never rewarded" means the code's "not yet a previous goal" or the text's "never a goal in the session";
  - the "5 trials ago" bar is exactly 5 (the code) or 5 or more (the text's wording).
- **Figure 5E measure:** the code's fraction conditional on which arm was visited, or the legend's "fraction of all trials".
- **Figure 6A/B:** the Bonferroni correction is over 80 tests in the legend and 81 in the code. "A few trials" for the visit decay is read as 3 or 5.
- **The >90% same-segment check:** computed over all SWRs or over spatially continuous SWRs only.
- **"Main results unchanged" under the controls:** read as the patterns of Figures 3D/E and 5B.
- **Supplementary Figure 3B:** the text says median deviation; the code computes the mean, which is shown as a variant.
- **Supplementary Figure 3D:** the legend gives no test, so the code's rank-sum test of first against last goal visit is used.

**Missing:** nothing a claim needed is missing from the paper. The paper reports the GLM 99% confidence intervals only in figures, so they are not recorded as statistics; the criteria compare them with 1.
