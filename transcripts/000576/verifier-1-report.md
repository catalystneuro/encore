I've finished the checks and am writing up the verdicts. Of the 18 claims the notebook tested, none is reproduced in full. Three are partially reproduced, two are blocked because the paper's methods allow readings that disagree, and the rest are not reproduced. The 7 claims the notebook treats as blocked are genuinely blocked, since their data are not in the archive.

**A. Outcomes** (25 claims in the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| fig1b-delta-decrease | blocked (methods_underspecified) | Under the mixed model with the claims file's readings, it holds for `baseline` z-scoring in both amygdala sets (significant clusters cover 14.3 s for nSOZ and 15.6 s for all 14, against the abstract's 18 s) and for `amygdala` z-scoring over all 14. It fails for `amygdala` over nSOZ (smallest cluster p 0.072/0.056) and for `trial` under both sets (no clusters; cell 20). The criterion says to block when readings disagree. |
| fig1c-hgp-increase-first-2s | not_reproduced | 0 of 16 mixed-model readings and 0 of 16 t-test readings have a positive HGP cluster (cell 23). The closest is nSOZ with `baseline` z-scoring, p 0.056–0.062. The 60–150 and 60–250 Hz variants only give a cluster at 6.2–7.8 s (cell 24). |
| other-bands-no-effect | not_reproduced | Every reading that shows the delta effect also shows a significant cluster in another band (cell 27). `baseline` nSOZ has alpha at 13.3–15.9 s, p=0.016. `baseline` all14 has theta (p=0.002) and alpha. `amygdala` all14 has clusters in all four bands. Only `trial` z-scoring is clean, and it removes the delta effect as well. |
| table2-mi-values | not_reproduced | At most 6 of 28 values are within tolerance under any reading, and at most 23 of 28 signs agree (cell 29). Window (a) gives no HGP MI because there is no HGP group cluster. |
| fig1d-delta-hgp-mi-correlation | not_reproduced | r runs from −0.33 to +0.50 and no reading has p<0.05 (cell 33). The printed Table 2 values give r = −0.736. |
| nsoz-delta-hgp-mi-inverse | not_reproduced | r<0 in only 3 of 8 readings (cell 35). |
| table2-delta-reduced-12-of-14 | partially_reproduced | 11–13 negative, with negative values both inside and outside the SOZ, under window (a) wherever it is defined and under (c) except `trial` z-scoring (10). It fails under every per-amygdala window (b) reading (0–2 negative; most MIs are set to 0). The criterion requires every reading (cell 37). |
| table2-hgp-mi-positive-nsoz | not_reproduced | At best 5 of 7 nSOZ amygdalae are positive and the 7/7 + 6/7 count pattern is never matched (cell 39). |
| fig1e-hgp-not-delta-distinguishes-soz | not_reproduced | HGP p≥0.056 in all 16 rows (cell 41). Note that the printed Table 2 values would also fail the DELTA half (p 0.035/0.013). |
| hgp-soz-sensitivity-specificity | not_reproduced | Sensitivity reaches at most 5/7 and the 7/7 / 6/7 / 13/14 counts are never matched (cell 43). |
| fig1f-hgp-more-specific-than-delta | blocked (methods_underspecified) | Under the claims file's MI windows, HGP is never more specific: (a) is undefined and (b) gives ties or reverses. Under the notebook's added window (c), HGP is more specific for 3 of 4 z-scorings. The chi-square p (0.001–0.11) never approaches the paper's ~0.2 (cell 45). |
| neuron-count | partially_reproduced | 40 (over 442 s) or 42 (over observed epochs) units are above 1 Hz, both within 4.1 of 41. The units sit in 8 amygdalae, not 9 (cell 47). The 50 putative clusters cannot be tested: the dataset holds only the kept units. |
| fig3a-firing-increase-aversive | not_reproduced | Mean FRV is 0.007–0.033 Hz against 0.26 ± 0.15, with 23–27 of 42 units positive and Wilcoxon p ≈ 0.5 (cell 49). |
| fig3a-firing-gradual-sustained | not_reproduced | Both readings fail: the 0–2 s mean (0.31) is above the 2–24 s mean (0.018), the first peak is at 0.15 s, and 4 of the twelve 2 s bins are negative (cell 51). |
| fig3b-firing-hgp-no-condition-difference | partially_reproduced | No difference at the Fig. 3A time base (both spans, p 0.37/0.83) or with any per-block span. The means (0.083 and 0.096) are within the stated spreads. With 1.5 s and 15 s concatenated series, NEUTRAL > AVERSIVE at p=0.002 and 0.009 (cell 53). |
| fig3b-firing-muhgp-higher-aversive | blocked (data_missing) | Confirmed on the archive: each NWB file is 14–21 MB with variableMeasured LFP/Units/ElectricalSeries only. That is too small to hold 32 kHz microwire signals. |
| fig3c-ssi-frv-correlation | not_reproduced | r=0.255, p=0.11 (1 s) and r=0.403, p=0.009 (15 s), against 0.78. The "partially" condition needs p<0.05 under every reading, which the 1 s reading fails (cell 55). |
| fig3d-firing-correlations-modalities | partially_reproduced | The HGP part holds: 0.136 ± 0.24 (15 s) and 0.139 ± 0.20 (1.5 s), within 0.19 ± 0.17 (cell 57). The muHGP and BOLD parts and both Wilcoxon tests are untestable (data_missing). |
| fig4b-regression-firing-hgp | not_reproduced | R is within tolerance in 3 of 4 readings, but the FRV coefficient never reaches p<0.05 (0.07–0.65). The model p<1e-4 in only 2 of 4 readings (cell 59). |
| fig2-participant4-bold-correlations, table2-bold-correlations-group, table2-bold-correlation-values, bold-hgp-uncorrelated-low-mi, fig4c-regression-firing-bold, fig4d-hgp-bold-covariation | blocked (data_missing) | The archive lists 27 assets: 9 `_ecephys.nwb`, 9 `_ecephys+image.nwb` and 9 `.avi`, with no fMRI. The BOLD part is outside data (with_inputs). No part can be tested from the dandiset. For fig4d, only the firing-HGP axis exists. |

**B. Problems**

1. [affects a conclusion] Cells 26, 30, 53 and 55. Where the criteria require every reading, the notebook judges against one it chose itself: `baseline` z-scoring for other-bands and the MI claims, and the 1 s concatenated reading for fig3b. Adopting `baseline` as "FieldTrip's zscore" is the author's own assumption, not the paper's. For fig1b, the readings disagree, which the criterion says should be blocked.
2. [affects a conclusion] `normalise('baseline')`. The SD is taken over 20 samples of the 2 s baseline clip, smoothed over 1 s, so it rests on roughly 2 independent values. This inflates and destabilises the z-values (MIs of −4.8 and 4.0 in cell 29) and drives the MI-based results under that reading.
3. [affects a conclusion] Cells 28–29. MI window (c), fixed windows of 0–2 s and 0–24 s, is the author's own reading and not in the claims file. Window (b) sets MI to 0 when an amygdala has no cluster, also the author's choice, which makes (b) degenerate. The table2-delta-12, fig1f and fig1d judgements depend on these choices.
4. [affects a conclusion] Cell 55, SSI. The paper defines SSI over neurons on *different* microwires. The notebook uses every other unit in the amygdala, including units on the same wire, and never checked whether the units table records the microwire. This bears on fig3c and fig4b.
5. [affects a conclusion] `condition_corr`/`series` with span "concat". Smoothing (7.5 s and 15 s) runs over the whole session before the per-condition mask, so neighbouring opposite-condition blocks and baseline clips mix into each condition's series. In the "1.5s" series the bins also straddle epoch boundaries. These are the two readings that find a difference in fig3b.
6. [affects a conclusion] Cell 15. `trialsd` is a reading the claims file does not list. It is labelled as added, but it enters the hold counts for fig1b and the MI claims.
7. [does not affect a conclusion] Cells 11 and 47. Units are in subjects 1, 2, 3, 4 and 7, while the paper's Table 1 puts MUA in 1, 2, 3, 4, 5 R and 8 L. File ages differ for subjects 2 and 8. Together these hint that dandiset and paper patient numbers may not match; the notebook did not pursue this.
8. [does not affect a conclusion] Cell 43. The Clopper–Pearson interval for 7/7 is 59–100, against the paper's printed 66–100. The paper's bound matches a one-sided 95% interval (0.05^(1/7) ≈ 0.65). This is a claims-file reading that does not reproduce the printed CI, and the notebook did not comment on it.
9. [does not affect a conclusion] `normalise`/`envelope`. The 1 s centred boxcar lets activity from 0–0.5 s leak into the −1 to 0 s baseline window, slightly reducing early HGP effects. The readings fig1c fails under are far from threshold, so the outcome stands.
10. [does not affect a conclusion] Cell 13. The spike–iEEG clock alignment is only weakly supported (24 of 42 units, p=0.042). The firing claims rest on trial times from the same file, so this matters little.
11. [does not affect a conclusion] The helpers pass my synthetic tests:
    * `lmm_t` equals the patient fixed-effects OLS t exactly.
    * `clusters` finds the correct runs.
    * `cluster_test` has a 5% false-positive rate on null data.
    * `envelope` scales by a constant (0.76 at 80 Hz because of the 2nd-order filter applied forwards and backwards), which z-scoring removes.
12. [does not affect a conclusion] Claims file versus the paper's own numbers: on the printed Table 2 values, DELTA MI also differs between SOZ and nSOZ (p 0.035/0.013), so fig1e's "not DELTA" half conflicts with Table 2 itself.

**C. Not checked**

- **Microwire identity for SSI:** the plots could not show this. Printing the units table's columns and the electrode rows each unit points to would show whether a microwire is recorded.
- **Fig. 1-style curves per amygdala:** I could not compare the per-amygdala delta and HGP time courses with Fig. 1B and 1C. A table of each amygdala's A−N difference in 2 s bins would have allowed it.
- **fig3b readings:** the notebook gives no per-block-masked version of the 1.5 s and 15 s concatenated readings, with smoothing inside each block. That would show whether problem 5 explains the difference.
- **Methods 4.8 baseline variants:** the variants (mean of all epochs, previous epoch) were never run.
- **Firing-rate check against the data descriptor:** a PSTH per unit aligned to trial onset would have let me compare the computed mean rate of 4.65 Hz with the descriptor's 1.66 Hz.
- **Patient mapping:** no output tested the dandiset-to-paper patient mapping, for example per-amygdala MIs under a swap of subjects 2 and 7, or 5/8 against 7.
