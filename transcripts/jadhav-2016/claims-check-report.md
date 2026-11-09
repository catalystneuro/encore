The claims file is ready for an attempt. I corrected 18 claims and recorded the changes and the open points under `checks`. Nothing is committed or pushed.

**Checker result:** `39 claims, 39 quotes, 62 statistical values, 4 problems`. All 39 quotes match the text word for word. The 4 problems are p-values the checker could not find: 1e-11 (fig3de-ca1-precedes-pfc-peak) and 1e-7 (fig3e-onset-later-in-pfc, fig6e-glm-swr-prediction, fig6e-theta-trained-glm). The text prints these exponents with a replacement character ("10?11", "10?7"). I read each one in place and all four are correct. The 1e-7 in fig6e-glm-swr-prediction is the value I added.

**Changes, by claim:**
- **fig3-pfc-swr-modulation-fractions:** the "within 10 points" rule for "approximately equal" excited and inhibited counts is not in the paper. The criterion now says it is a choice made here.
- **Thresholds for "no difference" and group differences:** the paper sets p < 0.01 for comparisons between SWR-excited, SWR-inhibited and SWR-unmodulated cells (supplemental methods, Data Analysis). The file had used p < 0.05, or no threshold at all. I applied 0.01 in:
  - fig3de-ca1-precedes-pfc-peak and fig3e-onset-later-in-pfc (excited against inhibited)
  - fig4-swr-modulated-more-theta-locked (≤ 0.01, since the paper counts its own p = 0.01 as significant)
  - fig4-preferred-phase-concentration (made explicit)
  - fig5b-mean-rates and fig5c-spatial-coverage (threshold was missing)
  - fig5e-speed-correlation (0.05 kept as a variant)
  - fig5g-ensemble-cofiring (the file required p < 0.001, the reported level, not the threshold)
- **fig3f-swr-cross-covariance-lag:** two details are now named as open. One is the window for the peak or trough. The other is how the "13 ± 7 ms" was formed: the extreme of the mean curve, or the mean of each pair's extreme.
- **fig4a-preferred-phases:** the preferred phase was taken as the von Mises mean, but the Figure 4A legend defines it as the peak of each cell's phase histogram. The von Mises mean is now a variant.
- **fig6-swr-correlated-pairs:** which CA1 cells enter the 713 pairs is now open, with two readings: SWR-modulated CA1 cells only, or all CA1 cells.
- **fig6c-theta-predicts-swr-correlation:** the supplement describes its shuffle test only for spatial correlations. Using it here is now marked as an assumption.
- **fig6e-glm-swr-prediction:** added the reported cell-count effect (p < 10⁻⁷). Added a third reading for the ensemble-size groups (1, 2–3 and more than 3 cells, as on the Figure S4C axis).
- **fig6e-theta-trained-glm:** the criterion now requires that prediction improves with ensemble size. The comparison between the two model types now uses the paper's own test, a two-way ANOVA interaction.
- **figs4c-pfc-predicts-ca1:** added the ensemble-size groups from the Figure S4C axis, and the test and threshold for each part.
- **figs5-matched-selectivity:** the matching rule comes from the Figure S5 legend, not the supplemental methods. Citation corrected.
- **figs6-replay-content:** R is now defined per replay event, and each cell's measure is the correlation of R with its SWR response, as Figures S6A and S6B show. The supplemental methods call R a value per neuron; that conflict is recorded.

**Still open:**
- The PDF could not be rendered here, so the ensemble-size groups of Figure 6E are still unread. Three readings remain.
- The paper does not say whether its 0.01 threshold also covers comparisons with CA1 cells or the GLM ANOVAs. It calls p = 0.02 significant for the GLM, so those criteria keep 0.05.
- Table S1 has small inconsistencies: Y-track CA1 prints 163 where the rows sum to 162, and intermediate CA1 is 69 in Table S1 but 70 in the supplemental methods. The W-track numbers used as expected values are not affected.

Every main finding has a claim, and all claims come from this paper.
