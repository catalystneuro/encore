The file is ready for an attempt (`ready: true`). Nothing was committed.

**Checker result:** `claims/andreassen-2022.yaml: 28 claims, 28 quotes, 32 statistical values, 3 problems`. The three problems are p-values printed only in table images: 0.233 in Table S1, and 0.008 and 0.03 in Table S10. I read them from the rendered supplement pages and they match. I also checked every other recorded statistic against those pages (Tables S1 to S10), and the rest match too.

**Changes, by claim:**
- **fig1c-ctmax-similar-across-ages:** the file left open whether the adult mean of 41.0 °C is over 15 or 16 fish. Table S3 settles it: Model 2 gives 41.36 − 0.41 = 40.95 °C over 15 fish, and Model 1 gives 40.82 °C over all 16. So it is the 15-fish mean, and I removed the open question.
- **figs1a-swim-speed-no-treatment-difference:** the expected 2.9 mm/s is now tied to the intercept of the swim speed model (2.90). The model with treatment has a different intercept (2.55).
- **fig2e-depolarization-spread:** the expected value 11 ± 2.2 s did not match the 9 to 13.2 s range its own criterion states. It is now 11.1 ± 2.1.
- **fig2d-recovery-after-depolarization:**
  - The expected value is now 12.75 ± 3.75 min, to match the stated 9 to 16.5 min.
  - I dropped the reading that used the experiment 5 recovery time (return to 0% ΔF/F0). Table S8 puts that measure at about 2.5 min in normoxia, so it is not the 10 to 15 min recovery. The Fig. 2D legend describes that recovery as the return of normal activity and calcium peaks.
  - I replaced the made-up "median" rule with two readings: the mean over fish, and each fish.
- **discussion-depolarization-magnitude:** the expected value is now 4.55 ± 0.95, to match the stated 3.6 to 5.5.
- **Header:** I noted that Table S7 prints the heading "Model 2.1" over two columns; the caption shows the second is Model 2.2.
- **checks:** added the 2026-11-26 entry at the end of the file.

**Still open** (recorded in the check entry):
- **figs3d-medulla-drops-before-depolarization:** "sharply" is judged by a threshold of half the window maximum. The paper does not give this threshold; the claim says so, and any outcome would rest on that assumption.
- **figs4ab-light-response-amplitude-falls** and **fig6c-light-responsiveness-by-oxygen:** a Spearman test, a decline rule and 1 °C bins are not from the paper.
- **Several claims:** these details are also left open: how outlier quartiles are computed (fig5a), temperature bins (fig2f, figs2a, fig5d, fig6c), Q10 endpoints, and how p-values were obtained for the mixed models. The deposited R script may settle them; neither reader has opened it.
- **Coverage:** each of the paper's main findings has a claim, and every claim comes from this paper.
