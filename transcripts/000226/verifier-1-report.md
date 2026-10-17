**A. Outcomes (28 claims in the claims file: 14 reproduced, 3 partially reproduced, 11 blocked)**

| Claim | Outcome | Reason |
|---|---|---|
| table-s1-link | reproduced | Cell 18: all 60 files match a distinct Table S1 recording (2 matched by number and mouse), and 60 of 60 agree on mouse, sex, line and date. |
| video-frames | reproduced | Cell 21: 54,660,000 frames against 54,647,500. Reading (a) gives 65,710,000 against 65,257,500 (ratio 1.007). |
| merkel-minutes | reproduced | Cell 23: 823.8, 998.2 and 846.4 min (reading a), against 823, 999 and 846. |
| fig2c-baseline-rate | reproduced | Cell 25: median 0.03 Hz with IQR 0.20, against 0.0 ± 0.2. |
| fig2c-touch-rate | reproduced | Cell 25: median 47.9 Hz with IQR 94.8, against 48.0. All 33 afferents are touch-sensitive with bootstrap CIs, and also with Poisson CIs. |
| fig2c-wt-star | reproduced | Cell 26, reading (b): 13 WT*, median 19.0 Hz (IQR 57.4), classes agree with Table S1 for 31 of 33, and the WT* set is the same as Table S1's. Reading (a) gives 15 WT*, which fails the count tolerance. |
| fig3a-direction-selective | partially_reproduced | Cell 28: 17 of 26 Merkel/SA afferents (65%) have an index of 0.5 or more. That is at least half but below the 80% needed for reproduced. |
| fig3d-gam-full | reproduced | Cell 30: mean r 0.708 (SD 0.141), against 0.71 ± 0.16. |
| fig3d-gam-single | reproduced | Cell 31: M0 0.441 and M0' 0.415, against 0.45 and 0.42. |
| fig3d-gam-best-pair | partially_reproduced | Cell 31: M0+M0' has r 0.622 and ranks 2nd of 45 behind M0+omega (0.633). Both values are within tolerance and it is above M0,Fax,Flat (0.475). |
| fig4c-viscoelastic | reproduced | Cell 34: mean r 0.657 for the viscoelastic model against 0.686 for the M0,M0' model over 25 afferents, a difference of -0.029. The threshold is -0.1. |
| fig5-phase-modulation | reproduced | Cell 36: medians 2.43 and 51.1 Hz, within the claim's tolerances of 3.4 and 105.7. All 15 afferents have a preferred/non-preferred ratio of at least 2. The cell's own "False" uses a 10% tolerance instead of the claim's (B1). |
| fig5e-phase-span | partially_reproduced | Cell 37: all four quarters are occupied, but the Rayleigh test gives p = 0.047. I confirmed p by Monte Carlo (0.045), so it is below 0.05. |
| figs3-phase-invariance | reproduced | Cell 38: median circular differences of 0.37, 0.59 and 0.48 rad, all below pi/4 (0.785). |
| figs6-kinematic-gam | reproduced | Cell 40: full model r 0.975 ± 0.013 on the 15 afferents the criterion names. Every single-variable model is lower by 0.25 or more. |
| fig7g-phase-span-28 | blocked (metadata_insufficient) | Cells 5 and 42: every trial is labelled `intact` and MOI has one value per file, so the intact condition of the 13 progressive cutting recordings cannot be isolated. |
| fig6-cut-eliminated | blocked (metadata_insufficient) | Same reason. The Methods say sessions were split into intact, sham and Cut n, and the deposit collapses this to `intact`. The fifths table (cell 42) shows a decline but cannot test the claim. |
| fig6-cut-remained | blocked (metadata_insufficient) | Same as above. |
| fig6a-final-length | blocked (data_missing) | Trial columns are MOI, cuttingGroup and barCoor/barRadii/barAzim, with one MOI per file. No whisker length is deposited. |
| fig7d-cut-emg | blocked (metadata_insufficient) | Needs the cut condition, and the intrinsic protractor EMG is absent (see figs4-intrinsic-protractor). |
| fig7e-lost-rate-kinematics | blocked (metadata_insufficient) | Needs intact against cut trials. |
| fig7f-precut-emg | blocked (data_missing) | Intrinsic protractor EMG is absent. A partial test is possible but not done: the 5 cut-only afferents and the nasolabialis curve (11A) are in the archive, and their r gives a lower bound on the best match. |
| figs4-nasolabialis | reproduced | Cell 44: r = 0.924 with negative velocity and -0.716 with positive velocity, both within tolerance. |
| figs4-intrinsic-protractor | blocked (data_missing) | 7A, 8A and 9A have no units and no acquisition data (cells 5, 44). Their asset `variableMeasured` lists only BehavioralTimeSeries and ProcessingModule. Their size per trial (0.31 MB) equals 11A's, which has only behaviour and spikes, so no EMG is stored. |
| sigma-kappa | reproduced | Cell 46: mean 10.01%, within 7.8 ± 5.0. The SD is 6.97, driven by 243B (39.9%) and 265A (28.5%). |
| figs1-optotag-latency | blocked (data_missing) | No asset lists an OptogeneticSeries or stimulus times, and the 3 optotagging-only recordings hold only Units and behaviour. |
| figs1-labelling-specificity | blocked (data_missing) | Histology counts are not in the dandiset. |
| contact-classifier | blocked (data_missing) | The manual contact labels are not deposited. |

The paper states no chance levels for these claims.

**B. Problems**

1. [affects a conclusion] Cell 36 checks fig5 against 10% of the paper's medians and prints False for the non-preferred rate (2.43 against 2.1). The claim's tolerance is the IQR (3.4), under which it passes. An outcome taken from this printout would wrongly be partial. Cell 25 has the same 10% check but passes either way.
2. [affects a conclusion] fig5e depends on a Rayleigh p of 0.047, next to the 0.05 threshold (cell 37). Each preferred phase is the argmax of 30 noisy bins, so another reasonable estimator, such as the circular mean of the tuning curve, could move the outcome to reproduced.
3. [affects a conclusion] For fig3d-gam-best-pair, M0+M0' trails M0+omega by 0.011 and wins in only 19 of 33 recordings. 4th place (Flat+M0', 0.606) is 0.016 behind. The lambda = 100 check (cell 32) was not run on the 45 pairs, and r is in-sample, so the "top three" rank is untested for robustness.
4. [does not affect a conclusion] Cells 11 and 12: the `mean_position` column is all NaN. `reduce()` passes position with NaNs to `bin_means`. So "position peaks near phase 0" is unsupported. `phase_direction` correlates sines, which cannot tell a negated phase from a pi-shifted one. The phase convention is therefore unresolved. This affects only the "retraction" reading in cell 37 and fig7g. The tested statistics (quarter occupancy, Rayleigh, circular differences, curve correlations) are invariant to both.
5. [does not affect a conclusion] Cell 34's "parameters at a bound" is wrong. It checks E against 1000 while `fit_visco` bounds E at 100, and it compares the converted eta (eta_u/sdot) with the normalized bound. On synthetic data `fit_visco` recovers predictions (r 0.998) but not the parameters, so the parameter values in cell 34 should not be interpreted.
6. [does not affect a conclusion] In `fit_r` and cell 34, GAM and viscoelastic r are computed on the fitted frames. The claims file asks for this, and the paper reports cross-validation made little difference. With 60,000 frames and at most 101 coefficients, overfitting is small.
7. [does not affect a conclusion] In `categories`, contact requires whisking (amplitude above 2.5 degrees), which the Glossary's "Contact" definition does not. This follows the claims file.
8. [does not affect a conclusion] Cell 11 shows unexplained data in cut-only recordings: 209A has contact = 1 frames with `distanceToPoleCenter` around 6, and 199B has pole data. Per the Methods, recordings tracked on a surrogate whisker should have no pole in reach. This matters only for a future fig7f test.
9. [does not affect a conclusion] Several tests do not discriminate between readings. All four readings of video-frames pass, and sigma-kappa's readings (a) and (b) are identical.
10. [does not affect a conclusion] fig6a, fig7d, fig7e, fig7f, figs4-intrinsic-protractor, figs1-* and contact-classifier have no notebook cell showing what was checked in the archive.

Synthetic tests passed for `phase_tuning` (recovers preferred phase and peak), `spike_counts` (frame assignment and out-of-frame accounting), `classify`, `circ_diff`, `SplineModel` (r 0.999 with the true probability), and the derivative inside `visco_predict`, which matches Eq. M1.

**C. Not checked**

- **Table S1 transcription (`merkel.TABLE_S1`).** The supplement PDF could not be downloaded here. The text counts are consistent: 14 Merkel, 12 SA and 7 RA among the 33; 5/7/1 WT*; 17/28/8 overall; 15 = 5 Merkel, 9 SA, 1 RA; 13 progressive = 12 SA, 1 RA; 25 of 26 fitted. The type, Merkel, class and viscoelastic columns could only be checked against the PDF. Those columns drive merkel-minutes, fig3a, fig4c and the class agreement in fig2c-wt-star.
- **Full contents of the EMG and progressive files.** h5py is not available here, and the notebook never prints `series_present` or the processing-module names for 7A/8A/9A and the 13 progressive files. Printing them would settle whether any EMG or whisker-length series exists.
- **Phase convention.** A position-by-phase curve computed with nanmean would distinguish a negated phase from a pi shift.
- **Robustness of the borderline outcomes.** These outputs would settle B2 and B3: the 45-pair ranking at another lambda or on held-out frames, and fig5e with a second preferred-phase estimator.
- **fig7f lower bound.** The r between the phase tuning of the 5 cut-only afferents and the 11A nasolabialis curve would give the partial test that the notebook omits.

The paper text I used is saved under `paper/` (from the PMC accepted manuscript, PMC5528144).
