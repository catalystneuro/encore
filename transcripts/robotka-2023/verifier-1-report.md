**Verifier report, round 1: Robotka et al. 2023 on CRCNS aa-5**

The claims file has 30 claims. The notebook runs tests for 19 of them and treats 11 as blocked.

### A. Outcomes

| claim id | outcome | reason |
|---|---|---|
| stimulus-set-link | reproduced | Cell 14: 4 birds, 110 stimuli, and the counts per call type match the paper exactly (diff 0 for all 10). |
| paper-good-units-link | partially_reproduced | Cell 8/10: 91 of the 100 listed units are in the dataset, and all 91 are auditory with all 110 stimuli. The 9 missing units all come from the `ZF4F_2t_190613_101015.old` site folder, which is not in the archive. 91 is at least 90. |
| auditory-units | reproduced | Cell 16: 287 auditory units (292 ± 29.2). Under reading (b), counted as pickles with vocalization trials, the total is 726 (730 ± 73) and the fraction 39.5% (40.1 ± 4.01). Under (a) the SNR ≥ 5 units are 414 or 491, which is out of tolerance. |
| inhibited-units | reproduced | Cell 18: 47 of 287 = 16.4% (46 ± 4.6; 15.7 ± 1.57). |
| fig3c-peak-call-types | reproduced (code zCT reading only) | Cell 24, reading (b): Di ranks first and So second; peak counts Di 53 and So 58 are in tolerance; Ag, Be, So and Di are 4 of the top 5. Under the Methods reading (a) the ranking is So > Ag > Di, which would be not_reproduced. |
| fig4a-unit-z-vs-zt | reproduced | Cell 26: 187 units (191 ± 19.1). Every reading puts both means in tolerance; reading (a) gives Z 10.68, Z+T 12.05, paired t(186) = 7.17, p < 1e-5. |
| good-units-100 | partially_reproduced | Cell 28, reading (b): the designated single run gives 89, one below the tolerance band of 90–110. Ten other seeds give 87–101 (8 of 10 in tolerance), and 100 repetitions give 91. ZF6M has 10 good units against the paper's 16, out of tolerance in every run shown. Reading (a) gives 77. Applied strictly to the one designated run, the outcome would be not_reproduced. |
| fig4b-ensemble-20 | reproduced (code CV reading) | Cell 30, reading (b): Z+T 43.15 and Z 30.36, rising at every size step, corrected t(138) = 9.53. Under the Methods exemplar CV (a), Z+T is 32.0 and Z is 24.1, which is partially_reproduced. |
| fig4b-top-ensembles | reproduced (code CV reading) | Cell 33, reading (b): re-estimated mean 48.8 for the top 10% and 50.4 for the top 5%; best ≥ 55. Under reading (a) the mean is about 34, so not reproduced. |
| fig4b-confusions | reproduced | Cell 35: all four named pairs are among the two largest off-diagonal entries of their row, under both readings. |
| figs4-per-bird-and-sex | blocked (other) | Cell 37: the test needs ensembles of 15 within each bird. ZF6M has only 10 good units (9 under reading a), so the test cannot be run. It could have been run on the paper's own listed units (see B5). |
| figs6-primary-vs-secondary | blocked (metadata_insufficient) | The dataset gives each unit only bird, site depth and electrode number. The histology needed to assign brain areas is not deposited (archive listing checked). |
| fig5e-volume | reproduced | Cell 43, reading (b): 1797 ensembles pass the PCC > 30% filter (1746 ± 174.6); slope positive, p < 0.05. R2adj is in tolerance only with the code window and the code's eigh axes (0.094). The Methods readings give 0.12, which is outside the ±0.01 tolerance but rounds to the printed 0.1. |
| fig5f-si-unrelated | reproduced | Cell 45: p ≥ 0.12 under every reading; under the Methods SI (a) with reading (b), p = 0.85. |
| fig5g-entropy-selectivity | reproduced | Cell 47: the Methods ES (b) gives a negative slope with p < 0.05 under both CV readings. The code's ES (a) gives this only under exemplar CV (p = 0.046 / 0.0066). Under the code's own pipeline (CV b with ES a) the slope is +18.9, p = 0.79. |
| fig5h-neural-noise | partially_reproduced | Cell 49: the slope is negative and significant under every reading. R2adj is 0.13–0.27, never within 0.1 ± 0.01. |
| fig5-multiple-regression | reproduced (eigh LDA variant) | Cell 51, reading (b) with eigh axes: R2adj 0.235–0.241 (0.22 ± 0.022), p < 0.001. With the Methods "largest" axes R2adj is 0.246–0.252, just outside tolerance. |
| pcs-variance | reproduced | Cell 22: the first five PCs explain 0.9244 of the variance (paper about 0.90; code printed 0.922). |
| table1-snr | reproduced | Cell 20, reading (a): mean 6.84 (7.42 ± 0.742), median 6.07 (6.5 ± 0.65). Reading (b) also passes (6.97, 6.20). |
| figs5-region-anova | blocked (metadata_insufficient) | Same as figs6: no area per unit in the archive. |
| fig6a-acoustic-clusters | blocked (data_missing) | The vocalization database is not in aa-5 (archive listing: only the site tars, one GUI notebook and the docs). |
| acoustic-labels-decoding | blocked (data_missing) | The stimuli's acoustic cluster labels are not in aa-5. |
| fig6c-number-of-clusters | blocked (data_missing), part testable | The call-type half (mean 10.83, median 9) needs only aa-5, and the criterion says to judge it on its own, but it was not run (B6). |
| fig6c-ari-call-over-acoustic | blocked (data_missing) | Needs acoustic labels. |
| figs10-ensemble-size | blocked (data_missing) | Needs acoustic labels. |
| anesth-auditory-units | blocked (other: data elsewhere, CRCNS aa-4) | Not part of aa-5. |
| anesth-decoding-better | blocked (other: aa-4) | Not part of aa-5. |
| anesth-regressions | blocked (other: aa-4) | Not part of aa-5. |
| figs9-per-region-regressions | blocked (metadata_insufficient; aa-4) | The awake part needs areas, which are not deposited. |
| anesth-primary-secondary-rate | blocked (other: aa-4) | Not part of aa-5. |

**Chance level.** The paper gives 10%. The notebook's pre-onset control gives 9.89% (cell 12). My synthetic null gives 10.0% for both PCC definitions and both CV schemes.

### B. Problems

1. **[affects a conclusion]** `aa5.decode`, `cv="trial"`, cells 28–33. The code's cross-validation trains on other trials of the same exemplar that is tested. On synthetic data with only exemplar-specific signal and no call-type signal, I get 18.3% with trial CV against 9.9% with exemplar CV. good-units-100, fig4b-ensemble-20 and fig4b-top-ensembles reach tolerance only under this variant. Under the Methods' exemplar hold-out they give 77 units, 32.0% and 34%. The claims file makes the Methods reading the main one, so adopting the code reading has to be stated as an assumption.
2. **[affects a conclusion]** Cell 28. The good-unit count depends on the seed (87–101 across seeds) and the designated run gives 89. Per-bird counts are not printed for the 10 extra seeds. ZF6M (10 against 16) is the stable deficit. Of the 91 paper units present, only 70 pass the threshold here under (b) and 51 under (a).
3. **[affects a conclusion]** Claims file, C11 ES reading (b). The Methods ES formula gives negative values here (mean −0.12, cell 41), but the Figure 5G legend says ES "ranges between 0 and 1". That is the same argument the claims file used to rule out C2(a) for SI. ES_b also falls mechanically as single-unit PCC rises, which makes a negative slope nearly built in. Under the reading the legend supports (ES_a), fig5g holds only with exemplar CV.
4. **[does not affect a conclusion]** Cell 33. The "best ensemble" is the maximum of 1000 single-repetition re-estimates, each with about 110 test trials. That is biased upward: the re-estimated best (95.0) exceeds the best first draw (88.4). The 100-repetition ensembles of cell 40 give best values of 68.4 under (b) and 41.1 under (a), so the ≥ 55 verdict under (b) stands.
5. **[affects a conclusion]** Cell 37, figs4-per-bird-and-sex. The variant on the paper's listed units was not run. All 9 missing listed units are ZF4F, so ZF6M keeps all its listed units (presumably 16; per-bird counts of the listed units are not printed) and ZF4F has 34. The paper-good-units-link criterion allows exactly this variant. The printed message ("15 or fewer … undefined for ns = 15") also misstates the cause: the birds have 9, 10 and 14 units, below 15.
6. **[affects a conclusion]** fig6c-number-of-clusters. The call-type values (UMAP + Ward, ARI-optimal cut, C12) need only aa-5 and were not computed.
7. **[does not affect a conclusion]** Cells 43 and 51. fig5e reaches R2adj tolerance only with the code window and eigh axes; fig5-multiple-regression only with eigh. These are code variants under the claims file's rule, so a reproduced verdict here rests on them.
8. **[does not affect a conclusion]** Cell 26 / C5. The Methods unit rule (≥ 2 trials of every stimulus, 125 units) was never run. Only the code's rule (110 distinct stimuli, 187 units) was used. The 191 in the paper matches the code's rule.
9. **[does not affect a conclusion]** `kde_matrix` / C4. The stored `spikeKDE` is used without checking that it is a 30 ms kernel, and the `KDE_BW` values (0.2, 3, 5, …) are not 0.03. The match to the code's 0.922 suggests it is the same KDE the code used. Also, `kde_matrix` treats a stimulus as spikeless when the sum of its spike times is 0, rather than when it has no spikes.
10. **[does not affect a conclusion]** `unit_regressors`. MRF projections are scaled by one SD pooled over all good units. That only shifts log volume by a constant, but if the code scales per unit the result could differ. I could not verify which it does.
11. **[does not affect a conclusion]** Cell 11 still contains an author conclusion ("Result: partially reproduced").

**Helper checks.** On synthetic inputs, `_rows` never put a held-out trial into training (0 of 2000 draws, with no NaN padding when every unit has ≥ 2 trials). `_gnb_posterior` matches sklearn GaussianNB to 3e-16. `selectivity_index` gives 0 and 1 at its extremes. `corrected_regression` reduces to ordinary R2 when ns is large.

### C. Could not check

- **The paper's code** (pinned commit). It was not available to me, so I could not confirm: ES normalization, MRF scaling (per unit or pooled), eigh on the non-symmetric matrix, the PCC > 30 filter, or that `plotConfusionsBird` uses n = 2 per sex. Printing the relevant code lines, or the code's own intermediate values (for example the per-unit ES and SI of the listed units), would settle these.
- **The KDE kernel.** A cell that recomputes a 30 ms Gaussian KDE from the spike times and compares it with the stored `spikeKDE` would settle B9.
- **Whether the vocalization database is public.** The paper gives no deposit, and I did not look outside the aa-5 archive.
- **good-units-100.** Needed: per-bird counts for each of the 10 seeds, and per-bird counts of the 91 listed units present.
- **figs4.** Needed: the ensemble-of-15 test run on the listed units.
- **fig6c call-type half.** Needed: mean and median optimal cluster number against call-type labels.
- **Missing 9 units.** Needed: whether the 9 `.old` units match pickles in `ZF4F_2t_190613_101015` by spike train rather than by name.
