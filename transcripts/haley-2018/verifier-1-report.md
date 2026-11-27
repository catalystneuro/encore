**A. Outcomes (30 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| fig2a-stg1-traces | reproduced | Cell 23: 897_037 is rhythmic (proxy) 1.0 in every step and recovery. At 10.4, spikes per burst are 12.43 vs 13.10 and slow wave is 17.65 vs 18.03 mV. Both drops are small, and the state part rests on the PD-only proxy. |
| fig2bcd-stg1-measures | reproduced | Cell 25: readings (a) and (b) both hold: frequency +0.118 in acid and −0.266 in base, spikes at 5.5 −5.4, duty in base −0.048. |
| fig3a-stg-variability-examples | blocked (metadata_insufficient), partly testable | There is no state annotation in the archive (confirmed). The rhythmic/silent part could have been tested with the proxy (887_097, 887_105 and 887_145 fit it) and was not run. |
| fig3c-stg-rhythmic-fraction | not_reproduced | Cell 27: both ANOVAs and the 5.5 test pass, but 10.4 has p_corr 0.306 (0.22 to 0.61 across variants). n is 13, against an expected 15 with tolerance 0. The proxy overstates STG rhythmicity, so this failure is weak evidence. |
| stg-state-transitions | blocked (metadata_insufficient) | No annotation in the archive (confirmed). [STATE] allows annotating from lvn units, which the notebook did not try. |
| fig3d-stg-frequency | not_reproduced | Cell 29: acid ANOVA p = 1.6e-7 (the claim needs ≥ 0.05). 9.3 has p_corr 0.651; 10.4 passes (0.047). Every variant fails. See problem 4. |
| fig3e-stg-spikes-per-burst | reproduced | Cell 31: acid p 1.6e-11, base p 1e-6, 5.5 p_corr 3e-5 (lower). |
| fig3f-stg-duty-cycle | not_reproduced | Cell 33: both ANOVAs pass, but duty at 6.1 is lower than control (−0.023, p_corr 0.93), not higher. |
| fig3s2-stg-control-variability | reproduced | Cell 35: reading (b), Kruskal-Wallis p ≈ 0, holds for all three measures. Reading (a) fails for hz and duty. n is 13. |
| fig4a-ptx-example | reproduced (weak) | Cell 37: only 903_052 meets every part, and its PD label is doubtful (problem 5). |
| fig4bc-membrane-potential | reproduced | Cell 39: PD acid and LP base ANOVAs pass and all six t-tests pass, under both the Methods and code readings. The absence parts hold too (LP acid p 0.648, PD base p 0.128). |
| fig4de-spike-amplitude | partially_reproduced | Cell 41: acid effects and both 5.5 reductions hold, and PD base is absent as claimed. The LP base ANOVA (p 0.095) and LP 6.1 (p_corr 0.113) fail. |
| fig4fg-ptx-frequency | partially_reproduced | Cell 43: all four ANOVAs pass and 6 of 7 t-tests pass. LP at 8.3 rises (+2.2 Hz) instead of falling. |
| gastric-like-rhythm-counts | blocked (methods_underspecified), arguable | No 8.x codes in the archive (confirmed). The claims file gives a fallback (LG bursts alternating with DG on lgn/dgn) that was not attempted. |
| gastric-conditions-co-occur | blocked | Depends on the gastric counts claim. |
| fig5-gastric-recovery-example | blocked | Same reason as the gastric counts claim. The notebook does not list which experiments record lgn, dgn and ion. |
| fig6-cg1-measures | not_reproduced | Cell 45: LC spikes per burst fall in acid (−6.05) and duty rises in base (+0.018) under both readings. CG detection is doubtful (problem 2). |
| fig6a-cg2-less-rhythmic | reproduced | Cell 47: 887_093 CG2L meets the criterion with proxy factors 2, 3 and 5. |
| fig7b-cg-rhythmic-fraction | not_reproduced | Cell 49: acid ANOVA p 0.058 and 5.5 has p_corr 0.246. With factor 2 the acid ANOVA passes (p 0.023), which would make it partial, so the outcome depends on the proxy. |
| cg-state-transitions | blocked (metadata_insufficient) | No annotation in the archive. The proxy follows only the LC unit. |
| fig7c-cg-frequency | not_reproduced | Cell 51: base ANOVA p 0.0555 and 10.4 has p_corr 0.84. Every variant fails. |
| fig7d-cg-spikes-per-burst | not_reproduced | Cell 53: acid ANOVA p 0.54. There is no increase at 5.5 or 6.1; only 10.4 passes. |
| fig7e-cg-duty-cycle | reproduced | Cell 55: base p 4.8e-5, acid p 0.52, robust across variants. |
| fig7s2-cg-control-variability | reproduced | Cell 57: reading (b) holds for all three measures. |
| fig8a-ganglion-difference | not_reproduced | Cell 59: with sum coding all 6 ANOVA effects pass (both readings c and d), and STG is lower at 5.5 (p_corr 0.042). STG at 9.3 and 9.8 is not significantly higher (0.36, 0.21). The criterion's partial clause does not cover this pattern. |
| fig8b-individual-preparations | not_reproduced | Cell 61: STG "ceased" is at most 6+2 of 13 (expected 14 ± 1.4). CG reduced at 5.5 is 5 (expected 6 ± 0.6), and CG normal everywhere is 2 (expected 3). The 2 STG counted in the "+2" count only because of zero-filled missing files. |
| fig8b-cross-predictive | not_reproduced | Cell 63: reading (a) fails in both ganglia (877_121 in STG, 877_149 CG1L in CG). |
| baseline-frequency-correlations | not_reproduced | Cell 65: no combination holds. Extracellular PD has r ≤ 0.55 with p > 0.05, and the PTX PD acid correlation is r = −0.81. |
| robust-6-1-to-8-8 | reproduced (weak) | Cell 67: 0 significant decreases in either ganglion, under every proxy factor. The STG proxy is biased toward rhythmic, which favours this absence claim. |
| intact-depolarize-in-acid | reproduced | Cell 69: PD 7/7 and LP 5/5 preparations are depolarized at 5.5, with acid ANOVAs p 3e-11 and 7e-5 (both minimum-Vm readings). |

Totals: 11 reproduced, 2 partially_reproduced, 11 not_reproduced, 6 blocked. No claim states a chance level.

**B. Problems**

1. [affects a conclusion] The state proxy (`crabph.rhythmic_seconds`, `unit_measures`, `RHYTHM_GAP_FACTOR = 3`; cells 19–21) is the author's own construct. [STATE] asks for annotation from the definitions (PD, LP and PY on lvn; SC and LC on the trunk). The STG proxy counts state 3 as rhythmic. Outcomes change with the factor: fig7b's acid ANOVA is p 0.023, 0.058 and 0.29 at factors 2, 3 and 5, and the fig8a ganglion effect loses significance at factor 2 (acid, p 0.161) and factor 5 (base, p 0.061). Claims affected: fig2a, fig3c, fig6a, fig7b, fig8a, fig8b ×2 and robust.
2. [affects a conclusion] CG LC isolation is entirely the author's own: `unit_threshold` uses LC_FRAC/LC_PCTL, and `BURST_RULES["CG"] = (1.0 s, 1 spike)`. The [EXT] values of 0.3 s and 2 spikes appear only as a variant. The cell 19 tables show signs of mis-isolation:
   - 897_041 CG3L rises from 0.055 to 0.71 Hz at 10.4 with about 1 spike per burst.
   - 887_149 CG2L has 1.0 spike per burst and duty 0.000 at control.
   - 877_149 CG1L has 1.5 spikes per burst at control and 12.3 at 5.5.
   - 877_149 CG2L has about 25 spikes per burst, which looks like SC spikes merged in.

   There is no validation output. Claims affected: fig6-cg1, fig7b–e, fig7s2 and fig8a/b.
3. [does not affect a conclusion] A missing file is entered as 0 (`measure_frame` and `rhythmic_frame` with `missing="zero"`). The claims file says an empty bin is 0; a step with no file is invented data. This touches 4 CG units at 10.4, 2 STG preparations at 5.5 and 887_005 STG at 10.4. The "nan" variant was not run for fig8a (whose 5.5 Welch p_corr 0.0415 includes two invented STG zeros), fig8b or fig8b-cross. It changes no outcome here, but it should not be the main reading.
4. [affects a conclusion; claims file] fig3d's criterion treats "relatively invariant in acid" as a non-significant acid ANOVA. Under the claims file's own zero-bin rule, and with the paper's 14 of 15 STG silent at 5.5, the paper's acid ANOVA was almost certainly significant. The criterion probably misreads the text; I report this and do not correct it.
5. [affects a conclusion] fig4a (cell 37) depends on a single preparation, 903_052. Its PD-to-pdn spike match (cell 10) is 0.00–0.04 in every file, against 0.3–0.7 elsewhere. Its pH signal is also compressed: the "10.4" file estimates pH 9.75 and the "5.5" file 5.87. The notebook computed this PD label check and never used it.
6. [could affect fig4bc LP 8.8] The 903_056 8.8 file lasts 2.3 min, so its "last minute" is about 2 min into the step, not the end of a 15-min step (cell 10). The LP 8.8 t-test has p_corr 0.0198 with n = 9.
7. [affects blocked status] fig3a, stg-state-transitions and cg-state-transitions are blocked because of the proxy's limits, not the data's. lvn and trunk recordings exist, and [STATE] says to annotate from the definitions. For the gastric claims, the claims-file fallback was not attempted.
8. [does not affect a conclusion] fig3c expects n = 15. The archive has 13: 877_127 is absent (I confirmed this via the API), and 877_101 has no pdn channel. 877_101's lvn and its unnamed ME1_Vx channel were not tried as a PD source. CG has 14 of 15 (887_017 is absent, also confirmed).
9. [does not affect a conclusion] fig4a's readings (spikes/wave ≤ 1.5; ISI CV < 1 for "tonic") are the notebook's own, and it states them as assumptions. They are reasonable.
10. [does not affect a conclusion] [RM] says no t-tests after a non-significant ANOVA. The notebook runs them anyway, for example fig7b acid and the CG part of robust. No outcome changes.
11. [does not affect a conclusion; claims file] Reading (b) for fig3s2 and fig7s2 (Kruskal-Wallis on 48 bins per preparation, H ≈ 500) passes for almost any data. The fig8a criterion has no category for "ANOVAs hold, some t-tests fail".
12. Helper tests on synthetic inputs pass:
    - `rm_anova` F matches a classical one-way repeated-measures ANOVA.
    - The `mixed_anova` interaction F matches a classical split-plot ANOVA.
    - `bursts_from_spikes`, `burst_bins` (empty bin = 0) and `rhythmic_seconds` (10-s merge) behave as their docstrings say.

**C. Not checked, and the output that would allow it**

- Spike and LC isolation quality. Needed: per-unit spike-height histograms with the threshold marked, plus example trace overlays at control, 5.5 and 10.4, especially for 897_041 CG3L, 887_149 CG2L, 877_149 CG1L/CG2L and 887_141 STG.
- How well the proxy matches the paper's states. Needed: proxy fractions next to Figure 8B per preparation, or lvn LP/PY activity for a few preparations.
- The claim that pHCumulative.m sets a missing condition to 0. Needed: the quoted code lines.
- PD identity in 903_052. Needed: overlaid PD3, LP1 and pdn traces from one file.
- Whether the gastric and state claims could be tested. Needed: the README electrode list for every experiment (`pl["desc"]["electrodes"]`), showing which record lvn, lgn, dgn and ion. I did not download READMEs.
- Exact F and p values from the paper. Its statistics tables are images, so they are not in the text.
