**A. Outcomes (35 claims in the claims file: 32 tested, 3 blocked)**

| claim | my outcome | reason |
|---|---|---|
| recording-sample | partially_reproduced | Cell 11 gives 7 mice and 41 sessions with an open field (reading a). The 21 sessions and 3 mice with both structures come from the paper's mouse list (`DUAL`), not from the data. By the unit labels it is 24 sessions in 4 mice (Mouse20 has PoS units), which is outside tolerance. The archive also describes Mouse20 as "anterior thalamus and the post-subiculum". |
| supptable1-per-animal | partially_reproduced | Cell 13: 5 of 10 counts within tolerance under hd-b, 3 of 10 under hd-a, 4 or 5 under the session-rule variant. Mouse32 is 0 against 35 because its files have no head direction. |
| hd-cell-fraction | not_reproduced | Cell 14: no combination of readings puts all four counts in tolerance (thalamic HD 293/312 for all sessions; with the rule, 207/220 HD cells but only 593 recorded). Per-session thalamic fractions are 0.458 to 0.572, against 0.369 to 0.451. |
| hd-fraction-hd-shanks | reproduced | Cell 15, hd-a: 0.733 (mean over shank-sessions) and 0.736 (pooled), within 0.71±0.071. |
| ensemble-sizes | not_reproduced | Cell 16 under hd-a: ADn 7.51±4.39 and PoS 3.57±2.97 (reading a); readings b and c also fail. hd-b was not run (problem 1), and it could change this. |
| sleep-duration | reproduced | Cell 17, home-cage reading (a): 4.99±0.97 h against 5±1 h. |
| adn-pos-peak-rate | partially_reproduced | Cell 19: Mann-Whitney p = 1.9e-13 and 1.9e-18 pass. The ratios are 3.51 to 4.26, outside both 2.7–3.3 and 2.5–3. |
| adn-pos-hd-information | reproduced (marginal) | Cell 20, hd-b means: 1.384 and 1.004 bit/spike with p = 3.9e-11. The PoS mean is just above the lower bound of 0.999. Under hd-a the values fit but p = 4.5e-5 fails 1e-6. |
| supfig2a-unimodality | reproduced | Cell 21, hd-b with reading (a): 0.122 and 0.292, both within tolerance. |
| fig2a-rates-preserved | reproduced | Cell 23: all four r ≥ 0.64 with p ≈ 0 in every selection, so the r ≥ 0.5 reading passes. PoS r is below 0.7. |
| fig2b-pair-correlations-preserved | reproduced | Cell 25: every r is between 0.81 and 0.97, with p ≈ 0. |
| fig2f-sws-tenfold-faster | partially_reproduced | Cell 27: the median ratio is 11.7 to 12.3 for ADn-ADn and 5.6 to 6.1 for PoS-PoS. Both are above 5, with 88–96% of pairs faster in SWS and Wilcoxon p < 1e-3. Neither is within 9–11. |
| fig2e-decoded-speed | not_reproduced | Cell 28, reading (b): SWS/wake ratio is 6.0 (decoded wake) or 4.3 (actual), REM/wake 0.57 or 0.41. Reading (a) is degenerate (problem 3). |
| fig2f-rem-similar-to-wake | reproduced | Cell 29: median ratios 0.96 to 1.20, Wilcoxon p 0.17 to 0.66, for both pair types and every selection. |
| fig3a-packet-60-degrees | partially_reproduced | Cell 31: Pearson p < 1e-6 in 9 of 9 cases under hd-a rate-b, hd-b rate-a and hd-b rate-b. The crossing is within 54–66° in at most 8 of 9; PoS-PoS SWS reaches 102 to 108° in some readings. |
| fig3a-adn-stronger-than-pos | reproduced | Cell 32: ADn higher with p < 0.05 in every state and reading. Under hd-b rate-b p is 2.4e-11 to 6.3e-14, so the text's 1e-5 bound is met. Pair counts (480/150) are far from 345/55. |
| supfig5-rate-independent | not_reproduced | Cell 33: the region effect reaches p < 1e-7 in only 7 of 64 readings. Where it is significant (pairs below 60°), the rate-group effect is mostly significant too. Only 1 of 64 readings meets both conditions. |
| fig3b-packet-coherence | reproduced | Cell 34: every ensemble is above 0.05 in all states and both structures, with the mean summary and every reference and distance. The test has little power to fail (problem 9). |
| fig4b-noise-correlations | reproduced | Cell 36: all 16 readings hold for ADn-ADn and pooled pairs: positive at 0±15°, negative at 60±15°, Wilcoxon p < 1e-11. |
| fig4c-noise-adn-vs-pos | reproduced | Cell 37: both offset groups give p < 0.05 with ADn-ADn the most extreme in 12 of 16 readings, for example hd-b rate-b raw (p = 6e-13 and 6e-28). |
| fig4d-ole-near-bayesian | not_reproduced | Cell 38: ADn covariance OLE beats the signal OLE in 14 of 25 ensembles, Wilcoxon p = 0.156. Covariance/Bayes is 1.26, above the 1.25 margin. This rests on an assumed signal OLE (problem 4). |
| fig4e-ole-covariance | not_reproduced | Cell 39: the ADn median ratio is 0.990, not 0.5 or 0.67; ADn against PoS p = 0.275. There are 25 ADn and 5 PoS ensembles, against 20 and 8. Same caveat as fig4d. |
| decoding-tracks-hd | reproduced | Cell 41: median error 10.2° (ADn) and 14.4° (PoS), or 10.7° and 14.8° cross-validated, against the 30° threshold. |
| fig5b-sleep-tuning-similar | reproduced | Cell 42: median r is 0.81 to 0.98 in every state, in both directions. |
| fig5b-adn-decoded-tuning | reproduced | Cell 43: PoS cells score higher in all states, p = 7e-7, 5e-4 and 0.039 (paper: <1e-10, 0.018, 3e-6). Cell counts are 64 and 52, against 86 and 92. |
| fig5d-adn-predicts-pos-reliably | blocked (too_large) | Cell 53: the GLM was not run. The data needed are in the archive (problem 11). |
| fig5e-readout-windows | blocked (too_large) | Same as above. |
| fig5e-adn-predicts-pos | blocked (too_large) | Same as above. |
| fig6a-fast-oscillation | reproduced | Cell 45, pairs on different shanks: peaks at 165, 175 and 165 Hz, all inside 117–176 Hz. With same-shank pairs kept, the peak sits at the 285–300 Hz edge. |
| fig6b-adn-synchrony | reproduced | Cell 46, zpeak5 on different shanks: pooled Kruskal-Wallis p = 2.2e-24, each state p ≤ 2e-6, and the first group is above the last. |
| fig7-adn-pos-connections | not_reproduced | Cell 48: 4111 pairs against 6960. ADn→PoS is 4.57%, within tolerance, but PoS→ADn is 0.51% against 0.35±0.035%. Pyramidal fractions are 1.07% and 0.44%. The binomial test does pass. |
| fig7c-adn-triggered-pos-lfp | reproduced | Cell 49: power ratio 2.98 (jitter control) or 3.30 (random times). Sessions above control: 18 or 20 of 20. Wilcoxon p ≈ 1e-12. |
| fig7d-same-preferred-direction | reproduced | Cell 50: 11 pairs, Rayleigh p = 3e-4, Wilcoxon p = 0.41. |
| fig7e-driven-pos-hd-information | reproduced (fragile) | Cell 51: p = 0.040 with the Methods' baseline, but 0.075 with the jittered-baseline variant. 13 connected cells, against 11±1.1. |
| fig7e-interneurons-no-difference | reproduced | Cell 52: p = 0.45 to 0.59. With n = 8 and 51 (paper 13 and 79), the test has little power. |

**B. Problems**

1. [affects a conclusion] Cell 16 (ensemble-sizes) counts hd-a cells only. Under hd-b, from cell 14 and cell 16's session counts: ADn 312/39 = 8.0 (tolerance 7.56–9.24) and PoS 120/23 = 5.2 (4.5–5.5). Both means could pass, but the s.d. was never computed. The 23 PoS sessions include Mouse20's 3; without them it is 120/20 = 6.0.
2. [does not affect a conclusion] `decode_session` forms ensembles from hd-a cells only. So hd-b was never run for the decoding claims (decoding-tracks-hd, fig2e, fig3b, fig4d,e, fig5b), for the HD-cell sets of fig6 and fig7, or for ensemble-sizes reading (c). This explains why there are 5 PoS ensembles against the paper's 8. The ADn results that decide fig4d,e would not change.
3. [affects a conclusion] `decode_session`, speed reading (a): `bayes_decode` returns whole degrees, so speeds over 10 ms steps come in multiples of 100 deg/s. The median is 0 in waking and REM and 100 in SWS, which gives a ratio of inf. Reading (a) of fig2e was therefore never really tested; a mean, or decoding finer than 1°, would have been needed.
4. [affects a conclusion] `ole_fit`, signal reading: Q is ⟨FFᵀ⟩ off the diagonal, with the diagonal replaced by the observed ⟨rrᵀ⟩. That is the author's own assumption. The claim's criterion takes Q "from the tuning curves read at the head direction", and the plain reading (all of Q from ⟨FFᵀ⟩) was not run. With the author's version, the two OLEs differ only by the off-diagonal noise terms (ratio 0.99), so the not_reproduced outcome of fig4d and fig4e depends on this choice.
5. [affects a conclusion] Cell 11 takes the "both structures" sessions and mice from the paper's list (`DUAL`) rather than from the data. Mouse20 has PoS-labelled units in 3 sessions, and the archive describes those files as recording post-subiculum. The notebook is also inconsistent: Mouse20's 8 PoS units are kept in cells 14, 16 and 21 but excluded in cells 48 to 52.
6. [does not affect a conclusion] Cells 13 and 14: the notebook's 727 recorded thalamic cells match the paper's 720 by coincidence. Mouse32's 105 cells are missing, and ADn cells from sessions the paper discarded in the dual mice are added. Mouse32 and Mouse28-140314 have no head direction; the archive's variableMeasured lists no CompassDirection or Position for them. Mouse32's 35 HD cells should be reported as untestable (data_missing), not as a 0-against-35 miss.
7. [does not affect a conclusion] Cell 33: the peak-rate grouping uses `peak_a` even under hd-b, and the mean-rate grouping uses waking rates for the SWS and REM tests.
8. [does not affect a conclusion] `fit_speed` and cells 27 and 29: 387 pairs end at the grid edges or at 0 deg/s, so ratios of inf and log(0) go into the Wilcoxon tests. Cell 29 drops v_REM = 0 but not v_wake = 0. The medians are robust to this.
9. [does not affect a conclusion] `coherence`: there is no negative control, such as shuffled decoded angles. With the "random" reference, coherence is about 0.9 almost by construction, and with the "decoded" reference in waking it is 0.5 by construction. The 0.05 threshold the criterion fixes can hardly fail.
10. [does not affect a conclusion] Cell 46 tests "falls" as first group above last group only; the means are not monotonic (they rise again at 120–150°). Cell 48: the dandiset can give at most about 4765 ADn×PoS same-session pairs (Σ n_adn·n_pos in cell 5), so 6960 cannot be reached. The notebook does not say so. Mouse28-140314 (588 pairs) is dropped because it has no head direction, although connection detection does not need it.
11. [does not affect a conclusion] Cell 53: the GLM claims are blocked for compute, not for data. The archive has all 21 sessions with both regions, and all but two have scored sleep. A reduced window grid for fig5d and fig5e-adn-predicts-pos, or the GLM in a run of its own, would have tested at least part of them. The partial run over 14 sessions was thrown away.
12. [does not affect a conclusion] Two outcomes are borderline. fig7e-driven depends on the baseline (p 0.040 against 0.075). adn-pos-hd-information passes by 0.005 bit/spike.

Helper functions I tested on synthetic inputs all behaved correctly: `vm_fit_a`, `vm_fit_b`, `rayleigh_p`, `n_peaks`, `ang_corr`, `fit_speed` (recovered 30 and 300 deg/s), `mono_test` (sign of lag correct, no false positives in 1000 null correlograms), `ccg_counts` direction, and `hd_information` (≈0 for a uniform cell, positive for a tuned one).

**C. What I could not check**

- **ensemble-sizes under hd-b:** the s.d. needs cell 16 run with `hd_b`, with and without Mouse20.
- **fig4d,e:** needs the OLE with signal Q = ⟨FFᵀ⟩ in full.
- **fig2e reading (a):** needs mean speeds, or decoding finer than 1°.
- **The wake interval:** no output shows that the `sleep_states` "wake" interval coincides with the open-field epoch; the overlap should be printed. Durations of 21–56 min suggest it does.
- **Mouse20's PoS units:** whether they are real PoS cells (probe or electrode location) is not shown.
- **fig3b:** coherence under a shuffled-angle control.
- **fig2f:** quality of the speed fits per pair; the residual and grid-edge pairs by state would show it.
- **fig7:** number of pairs per session, set against the 6960.
- **GLM:** the timing log, and results from at least one session.
