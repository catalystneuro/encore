**A. Outcomes (21 claims in the claims file; the notebook tests 19 and marks 2 blocked)**

| Claim | My outcome | Reason |
|---|---|---|
| cohort-sessions | partially_reproduced | Cell 16 matches 15 participants, median age 29, range 18–56 and 7 male. It finds 68 sessions instead of 71, only 53 of 68 sessions have 50 trials, and there are 3353 trials instead of 3550. The criterion requires exact counts. |
| fig1b-accuracy | reproduced | Cell 18: all three readings fall within tolerance and decrease with set size. Pooled: 91.3, 97.7, 90.3 and 84.5%. IN is 89.0% and OUT 93.5%. |
| capacity-cowan-k | reproduced | Cell 20, reading (a): mean 6.59 and median 6.63, both within 6.1 ± 0.61. Reading (c) gives 5.43, which is outside. |
| fig1c-response-time | reproduced | Cell 22, reading p2 with the median: 1.13, 1.07, 1.14 and 1.21 s, slope 48.1 ms/item, incorrect 1.39 s. This is marginal. Pool p1 has exactly the paper's 3045 trials, and there the slope (47.69) misses the 47.7 lower bound. Means (1.30 s) are out of tolerance. |
| fig2bc-gamma-encoding-p1 | not_reproduced | Cell 26: H3 rises 179% (passes), but C2 rises only 17% as a mean and 61% at its maximum, both below 100%. |
| fig2d-cortical-beta-maintenance-p1 | reproduced | Cell 29: the significant contacts include temporal (2) and occipital (1). The largest values are at H3, H4, H2, F8 and G3. This is weak: 5 of 64 contacts are significant without correction, against about 3 expected by chance. |
| hipp-beta-maintenance | not_reproduced | Cell 31: no participant set reaches 100% in 3 or 4 participants under any of the 24 readings. |
| fig2fg-plv-theta-p1 | not_reproduced | Cell 33: theta PLV at C3 is 0.164 to 0.240, against 0.4 ± 0.04. The fixation test is not significant (p 0.35 to 0.72), and no auditory contact is significant against fixation. |
| fig2h-gc-reversal-p1 | reproduced | Cell 36, reading h1 with c1: encoding is significant at 6.75–7.2 Hz and maintenance at 7.0–7.45 Hz, both overlapping [4 8] Hz. This is fragile: c2 fails for maintenance under every reading, and so does the code's variant (cell 37). See problem 2. |
| fig2ijk-spatial-spread-p1 | not_reproduced | Cell 39: the most negative encoding contact is G6, H5 or A3, never an auditory contact, under any reading. Cell 40: the spatial test fails under both s1 and s2. |
| fig3-gc-reversal-p2-p3 | partially_reproduced | Cell 42: Participant 3 shows the reversal with the right-hippocampus bipolar reading (h2, c1). Participant 2 shows it under no reading. |
| fig3no-p4-right-no-gc | not_reproduced | Cell 44: per-frequency significance appears in 69 of 72 contact × period × reading tests, and c2 clusters in 50 of 72. |
| table1-left-hemisphere-sources | blocked (other) | No source grid is deposited. The notebook's reason, "not_runnable", is not one of the allowed categories, and its argument is weak (problem 7). |
| fig4a-group-gc-reversal | not_reproduced | Cell 49: no frequency is significant after FDR under any of the 6 readings. The mean theta ΔGranger in encoding is positive, the opposite sign to the paper. |
| scalp-temporal-laplacian | not_reproduced | Cell 51: in 0 of 18 readings is the effect significant with the mastoid reference and absent after the Laplacian, under either test. Under d2 every derivation is significant; under d1 none is. |
| fig4bc-auditory-strongest | not_reproduced | Cell 53: every part of the criterion holds in 0 of 36 readings. The Kruskal-Wallis test is below 0.05 in both periods in none, and auditory cortex is the extreme area in both periods in none. |
| fig4d-reversal-all | not_reproduced | Cell 55: the medians are out of tolerance in all 18 readings; the largest encoding median is −0.035 against −0.049. The 15/15 sign pattern appears only under d2, which produces that pattern without any directional effect (cell 56; problem 1). |
| table1-heschl-dgranger-correct | partially_reproduced (by the criterion, but uninformative) | Cell 59: all 30 signs match in 5 readings, all of them d2. At most 3 of 30 cells are within tolerance, and the correlations with Table 1 run from −0.33 to 0.20. The sign agreement comes from d2 by construction. |
| fig4e-lpfc-no-reversal | reproduced | Cell 61: for lateral prefrontal cortex (DLPFC) with t1 and d1, p200 is 0.065, 0.269 and 0.060, all ≥ 0.05. All the t2 readings with d1 are also ≥ 0.05. |
| fig4f-incorrect-no-reversal | blocked (data_missing) | I agree. The archive's file list (921 files) holds one LCMV `.mat` per subject and nothing else under derivatives. Its trial counts equal the correct trials (cell 9). A partial route exists (section C). |
| balanced-correct-subset | reproduced (by the criterion, but not evidence) | Cell 65: 6 of 12 t2 readings pass, all of them d2, with p = 0.005 and the sign pattern in 13 to 15 participants. No d1 reading passes (p 0.38 to 0.86). The pass rests entirely on d2's built-in sign. |

**B. Problems**

1. [affects a conclusion] **d2 has its sign built in** (`band_value` with `how="ext"`; this comes from the claims file and the paper's code). Taking the minimum over 4–8 Hz in encoding and the maximum in maintenance gives a negative and a positive value by construction.
   - The notebook's own control (cell 56) gives the pattern in 15 of 15 participants on the direction-swap null. Taking the opposite extremes gives the mirror pattern, also with p = 0.005.
   - I confirmed this on synthetic uncoupled AR data with `wmflow.granger`: d2 came out at −0.017, −0.030 and −0.005 in encoding and +0.025, +0.032 and +0.051 in maintenance, while d1 stayed near 0.
   - As a result, the passes for table1-heschl (signs) and balanced-correct-subset, and every d2 result in scalp-temporal-laplacian (s1) and fig4e, carry no evidence. The claims file should have flagged this; I report it as a claims-file problem.
2. [affects a conclusion] **The per-frequency test (c1) is uncontrolled across 4–20 Hz** (`significant_bands`). It tests 0.05 Hz bins with no multiplicity control, and the direction-swap null is not calibrated anywhere.
   - In Participant 4 it flags 69 of 72 tests (cell 44).
   - The positive results for fig2h (runs of 0.45 Hz) and fig3 (Participant 3, h2) come from the same test, so with this test a "reversal" in Participant 1 cannot be told apart from Participant 4's "no GC".
3. [does not affect a conclusion] **Hemisphere of the white-matter reference** (`hippocampal_channels`). For sub-03, sub-11, sub-13 and sub-15, h1 and h3 are referenced to a contact in the opposite hemisphere (for example sub-11: PHL1 − AHR5). For Participant 3, the right-hippocampus readings use the left contact AHL3 (cell 42).
   - The ECoG reference for sub-10 and sub-12 is AHL4, next to the LFP reference AHL3. This breaks the function's own stated rule ("any other depth electrode"); it falls back to the second white-matter contact on the hippocampal electrodes.
   - h2, which is bipolar and free of this, gives the same outcomes, so no outcome changes.
4. [does not affect a conclusion] **Participant mapping** (cell 59). participants.tsv swaps the pathology of eLife participants 5 and 6 relative to Table 1, and participant 15 differs (DNET against hippocampal sclerosis). The notebook prints this and then uses the mapping without stating it as an assumption, as the criterion requires. Only per-row comparisons in table1-heschl are affected.
5. [does not affect a conclusion] **Spatial test** (cell 40, `spatial_test`). It was run only for h1 in maintenance. Its null mixes 1 s fixation and 2 s task cross-spectra, which have different scales under the same 20 s padding. fig2ijk fails anyway on the encoding-contact condition under every reading.
6. [does not affect a conclusion] **fig4e p-values** (cell 61). The DLPFC p200 values of 0.060 and 0.065 are Monte Carlo estimates with a standard error of about 0.017, and no exact sign-flip p is given, although cell 55 computes one for auditory cortex. The outcome still holds on h2 (p 0.27).
7. [does not affect a conclusion] **Reason for blocking table1-left-hemisphere-sources** (cell 45).
   - "not_runnable" is not an allowed category.
   - The interactive `ft_electroderealign` step is a manual check. With a template 10-20 montage on a template head, an approximation can be run without it (MNE LCMV on fsaverage).
   - MATLAB being unavailable is a limitation of the environment, not of the data. The block should be "other", with an approximate run possible. Several subjects have only 8 EEG channels, which limits any beamforming.
8. [does not affect a conclusion] **Significance count in fig2d** (cell 29). 64 contacts are tested without correction, and the significant contacts are reported only by region, not by name.
9. [does not affect a conclusion] **Response-time pool** (cell 22). The pass depends on pool p2, although the paper's 3045 trials match p1 exactly. The incorrect-trial pool is not artifact-filtered under p2.
10. [does not affect a conclusion] **iEEG clock check** (cell 13). It fails in 4 of 15 subjects (sub-02, sub-03, sub-11, sub-14). The EDFs have exactly 8 one-second records per trial, so the alignment is very likely correct.

**C. What I could not check, and the output that would settle it**

- **fig4f.** I could not tell whether the derivative `.mat` files hold more than `LCMV_encoding` and `LCMV_maintenance` (filters or incorrect trials). A printed variable list per file (`scipy.io.whosmat`) would settle it. I also could not tell whether the LCMV filter can be recovered. A least-squares fit of each virtual sensor on the derivative's own scalp channels, with its R² per period, would show this. If R² ≈ 1, the filter could be applied to the raw EEG of the 254 incorrect trials, which makes part of fig4f testable.
- **c1 and c2 calibration.** I could not check the false-positive rate of these tests. GC run on mismatched-trial pairs (hippocampus of trial i paired with cortex of trial j), giving the fraction of tests flagged, would decide whether the fig2h and fig3 passes and the fig3no failure are artifacts of the test.
- **Contact names.** The names of the significant contacts in fig2d and fig2bc (cells 27 and 29) are not printed.
- **Exact p for fig4e.** The exact sign-flip p for DLPFC in fig4e is not computed.
- **Unrun readings.** The per-contact tests for h2 and h3 and the spatial test for h3 and for encoding (fig2ijk) were not run. Nor were the fig2h and fig3 readings with a same-hemisphere reference.
- **Hemisphere of sub-11's PHL.** Its PHL contacts lie at positive x (cell 14), and I could not resolve whether they are left or right. Plotting their MNI coordinates would show it.

I did not re-run anything on the real data. My checks were the helper functions on synthetic input (GC matches time-domain GC, 0.287 against 0.275; the sign-flip p and `runs` are correct), the paper text, and the archive's file list and README.
