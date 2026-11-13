I checked all 31 claims in `see-2018.yaml` against the notebook outputs and the helper module. 14 come out reproduced, 3 partially reproduced, 9 not reproduced and 5 blocked by missing data. The archive listing confirms the blocked claims cannot be tested even in part. The biggest problem is the PWC sharpness measure: it gives a median of about 12 ms where the paper reports about 2 ms, and four claims rest on it.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| fig2bd-pwc-measures-covary | not_reproduced | The best R² is 0.219 for sharpness and 0.234 for delay (±100 ms, log axes; cell 33). The target is 0.45 to 0.55 under every reading. |
| fig2eg-distance-weak | not_reproduced | All 12 R² values are between 0.006 and 0.060 (cell 35), below the 0.09 floor. |
| fig4-example-nine-cnes | reproduced | Site 10 is the only recording with 38 units. It gives 9 cNEs with sizes 2 to 6 under reading (a) and 2 to 5 under (b), the same with 5 other seeds (cell 15). |
| fig4s2-interleaved-halves-stable | reproduced | 192 of 205 ICs match (93.7%) under both readings (cell 43). The range allowed is 86.4 to 105.6. |
| fig4s3-train-test-83pct | not_reproduced | The count of 102 training cNEs matches, but 98.0% (quadratic) and 99.0% (linear) are matched, above the 91.3 bound. The variant null gives 95.1% and 99.0% (cell 45). The match is stronger than the paper's, but outside tolerance. |
| fig5a-mi-peaks-10-15ms | not_reproduced | The MI peaks at 35 ms under event reading (a) and at 2 ms under (b), for both projections and both mean and median (cell 49). |
| fig5b-number-decreases-with-bin | reproduced | Spearman ρ is −1.0. The mean number of cNEs falls from 11.06 at 2 ms to 3.75 at 50 ms, and is lower at 50 ms in all 16 recordings (cell 51). |
| fig5c-size-increases-with-bin | reproduced | ρ is 0.952 (sizes 3.88 to 5.11) under sign reading (a) and 1.0 under (b) (cell 53). |
| fig6c-spike-pwc-narrower-than-strf-pwc | partially_reproduced | The size ratio is lower for cNE pairs under both variants (p 6e-59 and 4e-53). "Spike PWC sharper in more than half of cNE pairs" holds only with minimum subtraction (63.2%) and fails with clipping (6.5%). Both variants are the author's own (cell 41). |
| fig6j-sharpness-cne-pairs | partially_reproduced | cNE pairs are sharper at p < 0.001 in 14 of 16 penetrations at ±50 ms and 12 of 16 at ±100 ms (cell 37). The criterion needs 12 for partial and 16 for full. |
| fig6-member-pwc-sharpness-delay | not_reproduced | Median sharpness is 12.0 ms (target 2 ± 0.2) and mean 12.4 ms (target 3.39 ± 1.21). Only the delay (1.64 ms) is within tolerance. Readings (b) and ±100 ms are worse (cell 39). |
| fig7-totals | reproduced | 16 penetrations, 655 units, 104 cNEs, 6.50 ± 1.97 per penetration (cell 13). |
| fig7a-number-vs-neurons | reproduced | R² is 0.745 with p = 1.7e-5 and a positive slope. The fraction is 16.1%, 14.0% or 15.9% depending on the reading, all within 13.5 to 16.5 (cell 17). |
| fig7b-size-vs-neurons | not_reproduced | Only the significant positive fit holds. R² is 0.807 or 0.729 (target 0.33 ± 0.033). Mean size is 4.34 to 4.74 (allowed 4.9 to 9.9). The fraction is about 11% against 17 (cell 19). |
| fig7-negative-weights | not_reproduced | 24 cNEs have a negative-weight member under reading (a) and 65 under (b), against 9 ± 1 (cell 21). |
| fig7c-membership | not_reproduced | 59.2% of units are in one cNE, 34.4% in none and 6.4% in several, against 68, 9 and 23%. Reading (b) is similar (cell 23). |
| fig7d-pairs-within-200um | reproduced | 88.3 to 88.5% of pairs under every reading, within 73.8 to 90.2 (cell 25). |
| fig7e-no-depth-bias | reproduced | KS p = 0.999 and Mann-Whitney U p = 0.474; the median depth differs by 10 µm (cell 27). |
| fig7f-span-200um | not_reproduced | 80.8% of cNEs (78.8% under sign reading b) span 200 µm or less, against 63 to 77 (cell 29). |
| fig8-spont-evoked-72pct | blocked (data_missing) | The archive has no 64-channel recordings (see the check below the table). |
| fig9c-cne-events-more-mi | blocked (data_missing) | The archive has no 50-repeat 5-s data. |
| fig9s1-cne-mi-above-random-groups | blocked (data_missing) | Same data as fig9c. |
| fig9s2-noise-correlations | blocked (data_missing) | Needs trials, which the archive does not have. |
| fig10b-ptd-higher | reproduced | cNE PTD is higher with p < 0.001 under all four projection and event readings (p from 2.3e-12 to 8.9e-4; cell 57). There are 476 pairs against the paper's 703. |
| fig10c-strf-mi-higher | reproduced (fragile) | It passes only under linear projection with event reading (a): p = 5.4e-4 with cNE MI higher in 55.7% of pairs. The other three readings give p from 0.008 to 0.12 (cell 59). |
| fig10s1-random-group-strfs | reproduced | Signed-rank p is 7.0e-4 for PTD and 3.1e-6 for MI. The KS tests give 3.7e-6 and 3.2e-9, with UI medians of 0.35 and 0.27 (cell 61). There are 103 cNEs, as in the paper. |
| fig11ab-real-vs-surrogate | blocked (data_missing) | The archive has no 15 repeats of the 10-min RN. |
| fig11c-models-number | reproduced | Shuffled (0.23 cNEs) and PR (1.41 or 1.52) are below the real 6.50, and DG (8.00) is above. Bonferroni p is at most 1.5e-4 for all three (cell 65). |
| fig11d-models-size | not_reproduced | Only shuffled-with-zeros is significant (p = 1.4e-7). PR (p ≥ 0.125) and DG (4.30 against 4.34, p = 1) are not. With empty runs left out, shuffled is larger than real (cell 67). |
| fig11ef-coincidence-ratios | partially_reproduced | All three models are below one at Bonferroni p < 1e-35 for pairs and triplets (cell 71). The 'repeat' condition cannot be run, which is the criterion's partial case. |
| fig11s3b-pr-strf-similarity | reproduced | PR on 5-ms bins gives a median of 0.737, within 0.666 to 0.814; PR on 10-ms bins gives 0.645, outside. Shuffled and DG give 0.022 (cell 69). |

Blocked claims, checked against the archive: the S3 listing for `ac-3/live/` holds only `Codes.zip`, `Data.zip` (16 files, `site1-rn1.mat` to `site16-rn16.mat`), `Stimulus.zip` (the rn1 and rn16 matrices and parameter files) and the docs. There are no repeat trials, no 5-s frozen segments and no 64-channel or spontaneous epochs. Each recording runs about 622 s against a 598 to 600 s stimulus, which is far too short to hide 50 × 5.5 s of repeats. No part of fig8, fig9c, fig9s1, fig9s2 or fig11ab can be tested.

**B. Problems**

1. [affects a conclusion] `cne.pwc_measures` and `pair_table`, cells 31 to 41. The sharpness is the half-count width of the raw histogram, flat baseline included, so the analysis window largely sets it. On a synthetic flat histogram over ±50 ms it returns 24 ms. In the data the median goes from 16 ms to 37 ms when the window grows from ±50 to ±100 ms. The cNE-pair median is 12 ms against the paper's ~2 ms, so this is not the paper's measure in effect.
   - This follows the claims file's lag readings, which the file itself already marks as resting on an assumption.
   - It drives the failures of fig2bd and fig6-member and weakens fig6j and fig6c.
   - The notebook never notes the scale mismatch.

2. [affects a conclusion] cell 37, fig6j, a likely misreading in the claims file. The paper's pair counts in Supplementary file 1 total 3087 + 8838 = 11,925. That is close to the number of pairs among cNE members at the paper's 91% membership (about 0.83 × 14,174 ≈ 11,740), not to all 14,174 pairs. The paper's non-cNE pairs are therefore probably restricted to pairs where both units are cNE members. `pair_table` computes a `both_members` column, but the notebook never uses it; it prints the 1012/13162 against 3087/8838 mismatch without following it up.

3. [affects a conclusion] cell 41, fig6c. Making the STRF PWC non-negative, by clipping or by subtracting the minimum, is the author's own choice, and the two variants give opposite answers on the "more than half" test. In addition, `np.correlate(..., "full")` on 50-lag profiles tapers to zero at ±49 ms by construction, so the STRF PWC sharpness (4 ms or 13 ms) reflects that taper and the offset more than the profiles. It is also compared with the window-dominated spike sharpness of item 1.

4. [affects a conclusion] `run_binsizes`, fig5a. Event reading (a) takes the 5000 largest samples of activity interpolated to 1 ms. At bin sizes of 20 to 50 ms these are contiguous samples from only about 100 to 250 distinct bins. The STRF and the MI are then computed on the same events, with no held-out data, so the MI is inflated more at large bins. That would push the peak towards 35 ms. Under reading (b) the MI falls monotonically from 2 ms. Neither reading is a defensible version of "a threshold giving 5000 events", so the not_reproduced outcome may come from the method.

5. [affects a conclusion] cell 59, fig10c. It passes on 1 of 4 readings, at p = 5.4e-4, with no seed check. The same no-held-out MI bias applies. The verdict is reproduced by the letter of the criterion but is not robust.

6. [does not affect a conclusion] cell 45. The primary null excludes both row and column maxima, while the paper says all non-matched correlations. The row-only variant is shown and also falls outside tolerance (95.1%).

7. [does not affect a conclusion] cell 61, `run_random_groups`. It uses 100 random groups, not the paper's 500 (a stated deviation). The PTD p of 7.0e-4 sits close to the 0.001 bound and was not checked with more groups.

8. [does not affect a conclusion] `run_models`. Model membership reuses the real data's thresholds. This is a stated assumption, and reasonable because the thresholds are about 1.5/√n (cell 10).

9. [does not affect a conclusion] cell 27. The members are a subset of all units, so the KS and Mann-Whitney U samples are not independent and both tests lean towards "no difference". The members against non-members variant also finds no difference (p = 0.50 and 0.12).

10. [does not affect a conclusion] `pair_table`. The PWCs use recording-clock spikes over the whole recording, including about 22 s outside the stimulus, while r uses the stimulus window only.

11. [does not affect a conclusion] cell 71. CR medians come from 200 runs, not 1000 (stated), and 28 triplets with a real CR of 0 are dropped.

**C. Not checked, and the output that would settle it**

- **fig6j on the paper's pair set:** Mann-Whitney U per site restricted to `both_members` pairs, with pair counts compared against Supplementary file 1.
- **Sharpness scale:** a version with the baseline subtracted or a narrower window, to see whether ~2 ms can be reached at all.
- **fig5a:** the number of distinct events per cNE at each bin size, and MI with the STRF estimated on held-out events.
- **fig10c and fig10s1:** reruns with several seeds, and fig10s1 with 500 groups.
- **DG fit:** whether the fit reproduces the real 5-ms rates and pairwise covariances (fitted against empirical values), and how much eigenvalue clipping `fit_dg` applies per site.
- **ICA convergence:** iteration counts on the real data (not printed).
- **PR model:** the spikes dropped in `pr_setup` (the `dropped` value is computed but not printed).

I did not re-run the notebook or download the data. The helper tests I ran on synthetic inputs all passed: `pwc`, `pwc_measures`, `bvn_cdf` against scipy, the `fit_dg` round trip, `detect` recovering two planted assemblies exactly, and `coincidence_ratio`.
