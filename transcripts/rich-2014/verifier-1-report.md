**Verifier report, round 1: Rich, Liaw & Lee 2014 (CRCNS hc-31)**

The claims file holds 27 claims. The notebook tests 26 and treats one (figs3-cluster-quality) as blocked. My outcomes are judged on F-a (fields recomputed from spikes and position), as the claims file directs. Where the two pass readings P-a and P-b give different outcomes, I apply the claims file's rule that the outcome is "the one all its readings give". The notebook instead takes P-a, which is the author's own assumption (problem 1).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| cell-counts | reproduced | Cell 18: 63/58/24/57/51, total 253, exact match. |
| figs3-cluster-quality | blocked (data_missing) | Cell 20: no finite L-ratio or isolation distance for any unit. The archive lists only resSave.mat, one LFP channel per rat, import code and docs, so there are no unclustered spikes. The proxy (rho 0.42 for isolation distance) is not the paper's measure. The RUN1 cluster info was never checked (problem 7). |
| fig1-recruitment-by-section | reproduced | Cell 22: both counts are at least 1 in epochs 2–4 under P-a and P-b. |
| fig2-individual-poisson | reproduced | Cell 25: 57 (P-a) and 56 (P-b) cells have 6 or more fields, inside 61±6.1. 0 cells are significant after FDR under every E and S reading. |
| fig2bc-population-bias | reproduced | Cell 27: every C-a and C-b p is between 0.45 and 0.90. |
| figs6-few-field-cells-uniform | partially_reproduced | Cell 29: P-a gives 0 of 5 groups significant. P-b gives 1 (the 4-field group, BH-adjusted p 0.038), which is "partially" by the criterion. |
| fig3b-overdispersion | reproduced | Cell 32: the criterion holds pooled and in 5 of 5 animals, under D-a, D-b, P-a and P-b. |
| figs7a-mean-fields-per-animal | partially_reproduced | Cell 34: P-b has 3 of 5 animals within 10% (the best is "under one reading"); P-a has only 1 of 5. F-b, the data set's own fields, matches 5 of 5 exactly. |
| fig3b-negbin-fit | reproduced | Cell 36: P-a gives r 0.559, p 0.152; P-b gives r 0.555, p 0.150. All are within tolerance. |
| fig3c-recruitment-fraction | reproduced | Cell 38: pooled 62.8%, animals 43.1–75.4% (inside 41.4–84.7), against an equal-rate prediction of 95.6%. |
| fig3c-lomax-recruitment | partially_reproduced | Cell 41: under P-b, KS is 0.0537 with p 0.38 (K-a) and 0.12 (K-b), which reproduces. Under P-a, KS is 0.0396, outside 0.05±0.005, with p 0.73 and 0.48. The Poisson curve's 0.956 lies above the observed 0.628 under both. |
| fig3c-extrapolation-500m | reproduced | Cell 43: 519 m (P-a) and 531 m (P-b). This is fragile: F-b gives 447 m, and the F-a pass rests on F-a's lower field count (problem 2). |
| fig3d-uniform-density | partially_reproduced | Cell 45: p is 0.088 (P-a) and 0.234 (P-b), but KS is 0.044 and 0.037, both outside 0.03±0.003. |
| figs10-no-track-or-speed-influence | partially_reproduced (depends on the reading) | Cell 48: under P-a, panel A fails T-a (3 of 12 bins outside, p 0.020). T-a is panel A's only reading, so under P-a the criterion gives "not reproduced". Under P-b every panel passes every reading, so it reproduces. |
| figs11-propensity-stationary | reproduced | Cell 51: rho 0.666 (P-a) and 0.634 (P-b). Every Q-a and Q-b p is 0.36 or higher. |
| figs11-no-boundary-remapping | partially_reproduced (depends on the reading) | Cell 53: under P-a, the sections 3/4 boundary has p 0.030–0.048 under every L and H reading, which means "not reproduced". Under P-b every p is 0.43 or higher, which means reproduced. |
| figs12-pairs-uncorrelated | not_reproduced | Cell 55: under both P readings, the observed mean r (0.009–0.031) lies outside the null 95% interval of means (U-b) at 48, 24, 12 and 6 bins. The U-a KS test also gives p < 0.005 at those scales. |
| fig3e-memoryless-recruitment | reproduced | Cell 57: 0 of 18 (V-a) and 0 of 10 (V-b) curves have BH-adjusted p < 0.05, under both P readings. |
| figs14-field-properties | not_reproduced | Cell 59: every F-a reading (P × M) has at least one Spearman p < 0.05 (size against location 0.004–0.027 in three readings, or size against other fields 0.031). The in-field rate SD (2.23–2.43) is out of tolerance in all four. |
| figs15-higher-threshold | partially_reproduced | Cell 61: only 38.1–44.0% of fields are kept, outside 50±5. Recruitment p is above 0.05 under K-a and K-b in every reading. |
| figs16-anatomy | reproduced | Cell 63: under Pearson (R-a) with P-a, ST is −0.210 and PD −0.204, both with p ≤ 0.001. N-a and N-b both hold. P-b also passes. |
| fig4a-pre-sleep-rate | reproduced | Cell 65: P-b with W-a gives r 0.455, p 2.6e-14. P-a with W-a gives r 0.445 and p 1.0e-13, a knife edge on the threshold. |
| fig4b-single-field-proportion | reproduced | Cell 67: the factor is 5.66 under X-a (5.0 needed) and 4.44 under X-b (3.9 needed). |
| fig4c-active-subsets | partially_reproduced (depends on the reading) | Cell 69: gamma-Poisson is lower than equal-rate under G-a (−0.008, −0.038) and higher under G-b (+0.019, +0.118). A 10-seed check confirms both signs. The criterion defers mixed results to "Author, step 1.6", which I do not have. |
| figs5-silent-cells-low-rate | partially_reproduced | Cell 71: cells without fields average 0.015–0.026 Hz (SD 0.028–0.066) under the F-a readings, against 0.006±0.01, so the values are out of tolerance. The Mann-Whitney and Spearman tests hold. The criterion defines no partial outcome; I record partial because the two tests pass. |
| figs8-silent-cells-form-fields | reproduced | Cell 73: 11–13 RUN1-silent cells have open-field fields; the data set's own count gives 10–11. |
| figs17-propensity-across-environments | reproduced | Cell 75: under P-a with O-a, within is 0.464, between 0.234 (at the edge of 0.22±0.015), and the ordering holds. |

### B. Problems

1. **[affects a conclusion]** Cell 0 and cell 16: the notebook takes P-a as the outcome wherever P-a and P-b disagree. That choice is not in the claims file, and the evidence for it is weak. The data set's own pass count (mean 6.03) agrees exactly with P-a for 47% of fields and with P-b for 39%, so it matches neither. It also counts passes that start inside the field in 23% of fields, which P-a cannot. This choice decides figs6, fig3c-lomax, figs10 and figs11-no-boundary-remapping, and makes fig4a and figs7a look worse.
2. **[affects a conclusion]** `_detect` with P-a: a field that touches either end of a novel section is dropped, because no pass can extend beyond the section's last bin edge. I confirmed this on synthetic laps: a field at 267–300 cm on a 0–300 cm section is found under P-b but not under P-a. That biases P-a against fields at section junctions and track ends. This bears directly on figs11-no-boundary-remapping (where only P-a is significant) and on fig3d.
3. **[affects a conclusion]** F-a finds about 11% fewer fields than the data set's own detection (791 against 887 fields; mean count 3.13 against 3.51), and F-b matches every Fig. S7A mean exactly. The notebook never diagnoses why. Candidates are problem 2, its 1 cm bins against the data set's 1 inch bins, and the pass rule. This drives figs7a, figs15 (fraction kept), figs5 (silent-cell rates), fig3d (KS) and the agreement in fig3c-extrapolation.
4. **[affects a conclusion]** Cell 48, `passes_Tb`: panel A has no T-b test, but a NaN is scored as a pass. Under the claims file, panel A under P-a therefore fails every reading it has.
5. **[does not affect a conclusion]** Cell 46, `corners`: the reconstructed track has 33–37 corners of 45° or more in 48 m, and 10–21 of 90° or more. The counts differ between rats, so this is probably tracking noise. Panel B's 1 m bins then hold almost all distances in 2–3 bins: rho is ±0.5 with p 0.667, which means about 4 bins. The test has almost no power, though it is not what decides the outcome.
6. **[does not affect a conclusion]** Cell 55: the U-a KS test treats the roughly 2,800 overlapping pairs as independent, which overstates significance. U-b handles this correctly and also fails, so the outcome stands. The small positive mean r could come from uneven field density within an animal (ANM228900 has a per-animal KS p of 0.001) or from pairs on the same tetrode; neither was checked.
7. **[affects a conclusion]** `load_animals`: L-ratio and isolation distance are read only from `spAll[c].clustInf`. The claim concerns RUN1, and `spEpochSep[c,1].clustInf` (RUN1's own cluster info) was never inspected, so the blocked status may be premature.
8. **[does not affect a conclusion]** Cells 7–8 and `open_field_fields`: the open-field extent after conversion (100–119 × 72–97 cm) disagrees with the paper's ~40 × 100 cm. The 100 cm² field threshold and the O-a speed units (assumed analogous to the track's) depend on that scale. figs8 is robust anyway, since the data set's own RUN3 count gives 10 cells.
9. **[does not affect a conclusion]** Cell 51: the stationarity simulation uses 22 m and 26 m, while the data's section ends are 21.2 m and 26.9 m. Negligible.
10. **[does not affect a conclusion]** The helpers pass synthetic tests: `nbinfit` (recovers r 0.570, p 0.140 at n = 200,000), `bh` (matches statsmodels), `censored_ks` (matches a fine grid), `lomax_cdf` (matches a gamma-Poisson simulation), and the AD Monte Carlo p-values (calibrated; E-b is very conservative, about 0.3% type I error at n = 7, which is inherent to that reading). The KS tolerance of ±0.005 for fig3c is much tighter than the null's spread (median 0.049, 95th percentile 0.083), so passing or failing it is largely chance.

### C. What I could not check

- **Whether RUN1 cluster quality exists:** needs a printout of `spEpochSep[c,1].clustInf` field names and their finite L-ratio and isolation distance counts.
- **Size of the P-a edge loss (problem 2):** needs the number of F-a fields per reading that touch the first or last bin of their novel section, and figs11 and fig3d re-run with P-a passes counted up to the section edges.
- **Cause of the F-a deficit:** needs a per-field match of F-a against F-b, listing fields missed by F-a and the step that rejected each (width, 2 Hz threshold, or pass fraction), plus a run with 1 inch bins.
- **figs12 confounds:** needs U-a and U-b restricted to pairs on different tetrodes, and a null that keeps each animal's field density.
- **Corner reconstruction:** needs a plot of the reconstructed centreline with the detected corners against the track layout in Fig. 1. I could not render the figures myself (no PDF renderer).
- **figs5 rate definition:** needs the silent-cell rate computed over all RUN1 time with no speed filter, to see whether the paper's 0.006 Hz comes from a different denominator.
