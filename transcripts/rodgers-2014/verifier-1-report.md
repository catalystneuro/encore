**A. Outcomes** (35 claims in the claims file; the notebook treats none as blocked)

| claim | outcome | reason |
|---|---|---|
| unit-table-link | reproduced | Cell 12: all 220 included units are found in their spike files (121 mPFC, 99 A1), all 220 match the region rule, 55 of 55 sessions are present, and n_trials matches in 55 of 55. |
| fig2a-above-chance | reproduced | Cell 15: 0 of 54 sessions fail the two-sided binomial test, so the criterion holds under both session readings. The median trial count is 736 under reading (a) and 699.5 under (b), both within 698±69.8. CR20B, CR21A and CR24A have both block medians within 85±8.5. |
| figs1a-go-better-than-nogo | reproduced | Cell 18: go is above nogo in 12 of 12 rat and block pairs. |
| fig2d-block-switch | reproduced | Cell 20: the first block trial is below the non-cue mean (0.56 vs 0.833 in localization, 0.496 vs 0.785 in pitch discrimination). Both blocks reach the mean at trial 6, which passes the 10-trial threshold and fails the 5-trial variant. |
| iti-median | reproduced | Cell 22: under reading (a) the median is 3.99 s and the IQR 2.65 to 5.23 s, all within tolerance. Reading (b) gives the same. |
| fig3c-pfc-rule-encoding | reproduced | Cell 24, reading (a): 76, 36 and 40, binomial p = 0.73. Reading (b) gives 81, outside tolerance. |
| fig4c-a1-rule-encoding | reproduced | Cell 24: reading (a) gives 36, 13 and 23 (p = 0.13). Reading (b) gives 35, 12 and 23, also within tolerance. |
| a1-rule-encoding-not-audresp-dependent | reproduced | Cell 29: 14 of 49 against 22 of 50, Fisher p = 0.144. The M4(b) variants give p = 0.39 and 0.21. |
| rule-encoding-effect-size | reproduced | Cell 31: 74.7% in mPFC and 99.8% in A1. |
| fig3ab-pfc-example-units | reproduced | Cell 33: 12.07 and 7.19 Hz, then 5.41 and 2.66 Hz, with 483 and 295 trials; both p < 1e-12. |
| fig4ab-a1-example-units | reproduced | Cell 35: 712 gives 8.01 and 4.76 Hz, 612 gives 10.07 and 2.00 Hz, with 312 and 253 trials; both p < 1e-11. The figure index has the panels swapped, which the criterion allows. |
| fig3d-pfc-interference | reproduced | Cell 37: n = 57. Interference is above hits in the non-preferred block (p = 0.0012) and below them in the preferred block (p = 0.0011). |
| fig4d-a1-interference | reproduced | Cell 37: n = 16. Interference is higher in the non-preferred than the preferred block, p = 0.0011 < 0.01. |
| figs2c-s3c-hold-by-trial-type | reproduced | Cell 41: in both regions all 6 non-interference comparisons have Bonferroni p = 1 and all 6 interference comparisons have Bonferroni p ≤ 0.035. |
| figs2f-s3f-bidirectional-vs-spont | reproduced | Cell 43: the pattern holds in 4 of 4 groups (largest p 0.025), and in the pooled variant. |
| fig5ab-single-unit-onset | reproduced | Cell 47, W = 3 s with the code's smoother: A1 0.550 s and mPFC 0.625 s, both above 0.35 s. W = 5 s gives the same. |
| fig5c-population-onset | reproduced | Cell 49: mPFC 2.725 s and A1 0.875 s, both within tolerance, and mPFC is earlier. |
| fig5d-go-nogo | reproduced | Cell 51, reading (a): nogo is above 0 and go below 0 in both regions (mPFC go p = 0.021). Reading (b) fails in A1, where only 28% of nogo bins are significant. |
| audresp-prevalence | reproduced | Cell 56, reading (a): 31 of 121 against 49 of 99, p = 0.0004. Reading (b) gives 46 and 61, outside tolerance (problem 1). |
| figs5cd-evoked-strength | reproduced | Cell 59: medians 0.116 and 0.019 extra spikes and 209.1% and 170.7% of baseline; p = 1.3e-9 and 6.1e-4. |
| figs5e-latency | reproduced | Cell 61: 19.75 against 16.75 ms, p = 0.010. These values come from the unit table's windows (problem 1). |
| fig6cd-baseline-evoked-correlation | reproduced | Cell 63: n = 43 and 17. A1 slope 0.977 (95% CI 0.48 to 1.48), p = 3e-4; mPFC p = 1.7e-5. |
| evoked-beyond-baseline-rare | reproduced | Cell 65, with the code's BH correction: 6 of 43, 4 of them CR12B and all 4 higher in pitch discrimination. Without correction the count is 12, which fails even the partial band (problem 3). |
| fig6e-decoding | reproduced | Cell 67: 21 and 17 ensembles of 49 and 31 units. The region effect has F = 39, p < 1e-4, with A1 higher. All four block t-tests give p > 0.05 even before adjustment. Leave-one-out gives the same. |
| figs5fg-tuning-vs-rule | reproduced | Cell 69: all four p > 0.15. Only 9 mPFC units are kept, so this test of an absence has little power. |
| figs5hi-stimulus-pairs | reproduced | Cell 71: 0 of 24 tests give p < 0.05. The smallest is 0.061 (A1, absolute raw values). |
| figs2gh-s3gh-rt-mt | reproduced | Cell 45: 0 of 8 t-tests are significant. The borderline one is A1 RT in localization, p = 0.0517. |
| figs2i-head-angle | reproduced | Cell 73: 26.92, 36.60 and 24.07 degrees. |
| figs2kl-s3kl-fev | reproduced | Cell 75: mPFC 94.1% and 5.9% with 3 units above 50%. A1 after dropping its one unit with p > 0.05: 83.0% and 17.0% with 1 unit above 50%. |
| posture-equalized-sign | reproduced | Cell 77, centred MAD: PRE 0.471 and 0.318, shuffle p = 0.0001. Switches are 1 of 16 (p = 0.0005) and 0 of 8 (p = 0.0078). |
| posture-equalized-magnitude | reproduced | Cell 79: p = 0.059 in mPFC and 0.141 in A1, both above 0.05. Equalized magnitude is lower in both regions (0.308 vs 0.418 in mPFC), so the absence holds only narrowly (problem 5). |
| fig7-disruption-by-block | reproduced | Cell 81: 6, 8 and 8 sessions. Pitch discrimination is significant in all three rats; localization in Z2 and Z3 only (Z1 p = 0.22). |
| fig7c-disruption-nogo | reproduced | Cell 83: each rat has a significant nogo impairment in one block, and the only significant go case is Z2 localization. |
| figs1bc-catch | reproduced | Cell 85: 0 of 8 Fisher tests give p < 0.05. |
| fig8-model | reproduced (depends on reading) | Cell 87: at N = 320 and SNR 0.0625 the best performance is 0.932 in both tasks. At SNR 0.25, performance is ≥ 0.99 for every task signal/noise value from 0.3 to 10, but only for 25 to 30% of the log-spaced gain samples (problem 2). |

Chance levels: the paper's 50% for behaviour is the notebook's 0.5. The decoder scores are in-sample balanced accuracy, whose chance level is above 0.5, and the notebook does not estimate it. This does not affect the comparisons, which are between regions and between blocks.

**B. Problems**

1. [does not affect a conclusion] Cells 53 to 61. audresp-prevalence, figs5cd and figs5e-latency use the audresp class and window from `unit_db.csv`, as the claims file's main reading says. The latency claim is therefore a read of the code's table, not a measurement from spikes. When the windows are recomputed from spikes (reading b, cells 54 to 59), the claims do not hold:
   - responsive counts are 46 and 61, outside tolerance;
   - latency is 16.38 vs 16.25 ms with p = 0.41, so the latency difference disappears.

   The reports should say this.
2. [affects a conclusion] Cell 87, fig8-model. I checked `8-1-model/main1.py` at commit 390b608: the broad gains, x = gain/noise, and a symlog x axis limited to (-1, 10) are all the code's choices. "≥99% over most positive task signals" passes when counted over the plotted axis (all x from 0.3 to 10). It fails when counted over sampled gains (0.25 overall, 0.30 within the plot), because the log-spaced samples crowd near zero. Above the plot range (gain ≥ 83, so x > 10) performance falls to 0.5. My "reproduced" rests on the axis reading, which matches Figure 8B, and the claims file does not settle which reading is meant.
3. [affects a conclusion] Cell 65, evoked-beyond-baseline-rare. The Supplement says p < 0.05 and names no correction. The notebook ran both readings: BH gives 6 of 43 (passes); unadjusted gives 12 of 43, with 9 from CR12B and only 6 of those 9 higher in pitch discrimination (fails). The outcome holds only under the code's BH. Separately, the bootstrap p values come from one seed with 10,000 draws, and units just above the BH cut (about 0.008 at rank 7) are not shown.
4. [does not affect a conclusion] Cell 51, fig5d. The pass rests on reading (a). A1 nogo is significant in only 28% of the bins from 0.5 to 3 s, which is weak support for "elevated for at least several seconds" in A1.
5. [does not affect a conclusion] Cells 69 and 79 (figs5fg, posture-equalized-magnitude) and cell 45 (figs2gh A1 RT, p = 0.052). These are claims of absence with small samples (n = 9, 16, 8), and one p value is borderline. They pass the criteria, but there is no power check.
6. [does not affect a conclusion] Cell 47, `first_bin_of_interval`. 7 mPFC and 2 A1 units have a refbin that is not significant. They still get an onset, which is what the code does (`main3.py` marks them invalid; `main4.py` uses all of them). The criterion says the interval "contains the bin just before onset". With exact spike times instead of the code's discretized smoother, mPFC moves to 0.75 s, so the match depends on the code's smoother.
7. [does not affect a conclusion] Cell 20. The fold assumes 80-trial blocks that start at trial 1. The code checks this with `unique_or_error` on the block at each fold position; the notebook never checks it.
8. [does not affect a conclusion] Markdown cells 26, 27, 38 and 39 still contain the author's "Result: reproduced" text, although the conclusion cells were supposed to be removed. I formed the outcomes above from the outputs.

On synthetic inputs, `count_in_windows`, `first_bin_of_interval`, `stim_equalized_bootstrap`, `smoothed_trials` (mass conserved), `spont_rate` (10 Hz uniform input gives 9.96), `stand_mad_centered` and `signedrank_r` all behaved as documented.

**C. Not checked, and the output that would have let me**

- fig2d: the fold's alignment. A crosstab of fold position against the `block` column would settle it.
- evoked-beyond-baseline-rare: whether the count of 6 is stable. The per-unit bootstrap p values for all 43 A1 units, under two or three seeds, would show it.
- fig8: how robust the second condition is. Performance on the narrow linear gains (linspace -20 to 20) at SNR 0.25 would test it.
- fig5ab: the median onsets with the 9 invalid-interval units left out.
- fig6e: the in-sample decoder's chance level. Scores with shuffled labels would give it.
- Most other scripts of the code (only the four cited above were read), and anything that would need re-running the notebook or downloading the data. No claim was blocked, so I did not need to check the archive for blocked claims.
