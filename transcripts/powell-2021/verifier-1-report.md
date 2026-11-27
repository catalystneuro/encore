**A. Outcomes**

The claims file has 22 claims. The notebook tests 17 and treats 5 as blocked. My tally: 10 reproduced, 4 partially reproduced, 3 not reproduced, 5 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| fig2-spontaneous-11-to-30 | blocked (data_missing) | The spontaneous set (Haddad & Marder 2018) is not in the record. Its 12 files are evoked_data.mat, the evoked-prep zips, and 941_003/941_006 (June 2019). |
| fig2a-less-regular-at-high-temperature | blocked (data_missing) | Same as above. 830_116_2 is not in the record. |
| fig3-evoked-7-to-21-in-9-of-10 | reproduced (on the criterion's literal wording) | Cell 16 reports 8 of 10, failing 901_062 and 901_086. But the code also requires bins 7 and 21 to be present, which the criterion does not ask. 901_062 never reaches 21 C (0 s, T_max 19.3) and has bursts in every bin it was held at, so the literal reading gives 9 of 10. If 21 C must be reached, it is 8 of 10, which would fail the tolerance of 0. 10 evoked preparations: exact. |
| fig3s1-spontaneous-and-evoked-similar | blocked (data_missing), partly testable | 941_006.zip holds only raw ABF files and crabsort classifier files (network/dgn, lgn, lvn, pdn), with no spike times. The other three preparations (901_062, 901_080, 901_086) are in evoked_data.mat and could have been tested. |
| fig4b-periods-decrease-all-preps | reproduced | Cell 19: 10 of 10 under both readings and both burst rules. |
| fig4c-q10-about-2 | not_reproduced | Cell 22, main (Methods) Q10: 1–3 of 10 have both Q10s in range, under both ranges and both the all-bins and held-steps variants. Only the code's per-burst variant with range (b) gives 8 of 10. |
| fig4c-q10-pd-lg-not-different | reproduced | Cell 24: p = 0.190 (all bins) and 0.479 (steps), both ≥ 0.05. The code rule with the code Q10 gives t = 1.272, p = 0.235, exactly the paper's values. |
| fig4s1-slowdown-after-stimulation | reproduced | Cell 26: positive slope at 8 of 9 temperatures under both burst rules. |
| fig4s2-gastric-without-pyloric-pacemaker | blocked (data_missing) | The 2020 PD-hyperpolarization set (999_017) is not in the record. |
| fig4s2-rhythm-counts | blocked (data_missing) | Same as above. |
| fig5a-example-ratios | reproduced (fragile) | Cell 28, reading (a): 10.96 at 7 C and 10.87 at 23 C, both within 10% of the labels and within 0.2 of an integer. At 7 C the "closest" cycle is a near-tie (T_LG 9.244 vs 9.245, ratios 10.96 vs 10.02), and the one chosen reads as ~11 where the paper says ~10. Reading (b) fails at 23 C (median 14.0). |
| fig5d-lg-pd-integer-coupled | reproduced | Cell 30, Methods rule, code shuffle: every bin from 7 to 21 C has p < 0.0056 and D ≥ 0.223 > 0.216. This is stable across 5 seeds. The paper's p < 1e-5 is missed at 17, 19 and 21 C (p up to 4.9e-4). |
| fig5d-dg-pd-not-coupled | reproduced | Cell 33, code shuffle: no bin with p < 0.0056 (smallest p 0.082) across 5 seeds. In the permutation variant, 11 and 15 C are significant. |
| fig5e-lg-area-exceeds-dg | partially_reproduced | Cell 35: LG > DG in 8/8 bins, which holds. The DG ± SEM interval overlaps the shuffled interval in only 1/8 bins (1–4 across seeds), never "most". |
| fig5f-ratio-independent-of-temperature | reproduced | Cell 37: Methods rule p = 0.311 (n = 3850). Code rule p = 0.880 with n = 3799, exactly the paper's values. |
| fig5f-ratio-range | not_reproduced | Cell 39: the 2.5th percentile is 7.03–7.04 under both readings, above 5.5. The upper end (26.0) passes. |
| fig6b-lg-phase-locked | partially_reproduced | Cell 41, sample (a): all 41 combinations have p < 0.05 (max 0.008). Four fail p < 4.4e-4, and z min is 4.74 < 6.75. Variant (b) with the code rule gives z 7.49–45.44, max p 4.5e-4, which matches the paper's numbers. |
| fig6b-lg-start-counts | partially_reproduced | Cell 43, Methods rule: LG 3908 (in tolerance) and fraction 0.339 (in tolerance), but DG 3573 exceeds 3228 + 322.8. With the code rule all three pass, and pooling temperatures with ≥ 100 gives exactly LG 3816. |
| fig6b-lg-phase-constant | partially_reproduced | Cell 45: no trend (p = 0.651 / 0.289; code rule rho = −0.310, p = 0.456, exactly the paper). But bin means of 0.416–0.494 (all starts) and 0.337–0.504 (first 40) put 4–6 bins outside 0.45–0.55. |
| fig6c-lg-spiking-drops-near-pd-end | not_reproduced | Cell 47: the value at 23 C is < 1, but the Spearman rho with temperature is positive (+0.15 / +0.17; +0.64 without 23 C) under both readings. The dip near PD end gets shallower from 7 to 21 C. |
| fig6e-dg-not-phase-locked | reproduced | Cell 49: p ≥ 0.05 in 16 of 35 combinations. Median DG z is 3.4 against LG 22.6. The DG ranges (p down to 1.4e-8, z up to 16) exceed the paper's ranges, which the claims file already notes are inconsistent with each other. |
| fig6f-dg-spiking-no-drop | reproduced | Cell 51: holds at 8 of 8 temperatures (DG 0.89–1.09). |

**B. Problems**

1. [affects a conclusion] Cell 16, `evoked_7_21`: the code requires `{7, 21} ⊆` held bins with a rhythm. The criterion only asks for a rhythm in "every bin the preparation was held at". This added requirement is not stated as an assumption, and the notebook's headline 8 of 10 depends on it. The literal criterion gives 9 of 10 (901_062 is never at 21 C). Both counts should be reported. The Methods' "in some preparations, 19°C was the warmest" fits two preparations topping out at 19 C.
2. [affects a conclusion] fig3s1 is marked blocked as a whole, but three of its four preparations (901_062, 901_080, 901_086) have LG spike times in evoked_data.mat. Their spontaneous (before first stimulation, 11 C) and evoked LG periods, means ± SD, could be tested. The count of evoked preparations with pre-stimulation LG bursting at 11 C could also be tested. Only 941_006 has no spike times; its zip has only raw ABF files and classifier .mat files, as I checked in the Zenodo preview.
3. [affects a conclusion; a claims-file issue, reported not corrected] The paper's own statistics match the code variants exactly, not the Methods readings the claims file makes main:
   - t = 1.272, p = 0.235: code rule with per-burst Q10.
   - n = 3799, p = 0.88: code rule.
   - LG 3816: code rule, pooled over temperatures with ≥ 100 starts.
   - rho = −0.310, p = 0.456: code rule, all starts.
   - z 7.49–45.44: code rule, first 50.

   This is strong evidence the figures were produced with crabsort's ISI-count rule (≥ 6 spikes) and the code's sampling. fig4c-q10-about-2 is not reproduced only under the Methods Q10; the code variant gives 8 of 10. Under the code variants, fig6b-lg-start-counts would be reproduced, and so would fig6b-lg-phase-locked: the code-rule first-50 numbers match the paper's figures, though one p is 4.5e-4 against the 4.4e-4 cutoff.
4. [affects a conclusion; a claims-file issue] In fig5d-lg-pd-integer-coupled, the "reproduced" clause (p < 0.05/9, D > 0.216) contradicts the "partial" clause ("some D or p miss the reported bounds", where the reported bound is p < 1e-5). No reading meets both p < 1e-5 and D > 0.216 in every bin: the draw shuffle misses p at 17–21 C, and the permutation misses D at 21 C. I applied the explicit reproduced clause.
5. [does not affect a conclusion] `stg.q10_methods` uses the bin centre for T, not the measured temperature. For the 9 and 13 C pass-through bins the exponent is 5, which produces LG Q10s of 98 and 181 from 1–2 bursts. The held-steps reading mitigates this, and the outcome is the same either way.
6. [does not affect a conclusion] Cell 26 and `phase_tables`/`spike_pdf_table` keep only odd rounded temperatures, so stretches or events at even rounded temperatures are silently dropped. How many are dropped is not printed.
7. [does not affect a conclusion] Cell 43: the fraction under reading (a) is taken over combinations with at least one start (0.339). Over all 90 combinations it would be 0.544. The author chose this without stating it as an assumption, though both are shown.
8. [does not affect a conclusion] Cell 35: preparation-bins with a single preparation get SEM 0, so overlap there is a point test. This makes "overlaps" harder to meet at 13 and 17 C.
9. I tested the helpers on synthetic inputs and they behave correctly: `bursts` (5- vs 6-spike rule), `rayleigh` (matches astropy p, z = nR²), `ks_2samp_asymp` (matches scipy asymp), `measure_phase`, `integer_coupling`, `integerness`, `q10_methods`/`q10_code` (Q10 = 2.000 on a synthetic Q10 = 2 rhythm). The data checks (cells 7–13: clock alignment, duplicate recordings, preparation identity) are sound.

**C. Not checked**

- I did not read crabsort `computePeriods` or the gastric repo, so the ISI-count burst rule rests on the helper's description. The exact matches in problem 3 support it.
- I could not check whether 901_062's run stopped at 19 C because no rhythm could be evoked at 21 C. A printout of 901_062's stimulation blocks and temperatures at the end of the recording would help.
- For fig3s1, the notebook would need per-preparation LG burst counts and periods before the first stimulation at 11 C, for all ten preparations.
- For fig5e, which shuffle `plotIntegerCoupling.m` uses for the area (one pooled permutation vs independent draws) cannot be confirmed without the code. A run with independent draws would show whether the overlap result depends on it.
- The number of stretches and events dropped by the odd-temperature filter (problem 6) is not printed.
- I did not view the notebook's figures (cells 20 and 37), only their printed ranges.
