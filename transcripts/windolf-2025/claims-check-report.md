The claims file for DANDI:001290 is ready for an attempt. It is at `claims/001290/10.1038-s41592-025-02614-5.yaml`, and nothing was committed.

**Checker result:** `34 claims, 34 quotes, 14 statistical values, 0 problems`. Before my changes it read 22 claims and 13 values, also with 0 problems.

**Changes, by claim:**
- **Opening comment, pipeline step 1:** spike detection and localization were listed as a "standard choice" with a variant. The Methods leave this open for each data source, and it sets every spike position used later, so these are now readings (i) and (ii), and every combination of readings includes both.
- **edf3a-ap-dredge-slow-trend:** the criterion now requires the result to hold under the step 1 readings as well as the step 2 ones.
- **edf3c-spline-subsecond:** the criterion called its scrambled-trace control "the paper's own". The paper uses that control only for ISI violations in Fig. 2e. The 0.4 s permutation bin, 100 permutations and 5% level are now stated as the file's own choices.
- **edf3de-spline-improves-registration:** the panel e measure (spread of corrected depth within each cluster) is not in the paper. I said so and noted that the spline is fit to minimize it. The paper's 1 s raster bins cannot show sub-second motion, so I added a 0.1 s variant that only gets reported and does not decide the outcome.
- **fig2-sorted-units:** the data location named only ref. 13. The paper puts this result in an unnamed one of its N > 20 human recordings, so all human deposits are now named. I also added a criterion for the bound "more than 500".
- **fig6e-chronic-jumps:** the paper does not say whether the 0.5 to 22.2 range is over datasets or sessions, so both readings are named.
- **12 claims added** for findings in the Results that had none. All of them use data held elsewhere: fig2c-lfp-tracking-clusters, edf4a-nonrigid-human, supp2-rat-spike-tracking, fig2fg-unit-spatial-spread, edf6-128-channel, fig3gh-iids, fig4f-insertion-anatomy, fig5a-imposed-zigzag, edf4d-nonrigid-ibl, supp10-11-simulated-drift, supp12-subsetted-channels, fig6cd-chronic-clusters.

The pipeline parameters in the opening comment, the quotes, the statistics and the expected values of the other claims match the paper.

**Still open (recorded in `checks`):**
- **Which recording:** the Results and the Fig. 2b legend place the spline method in a human recording. The Methods and Data availability place Extended Data Fig. 3 in the macaque recording held in this dandiset. The file follows the Methods and Data availability.
- **Extended Data Fig. 3 claims:** the paper gives no number or test for these panels. The thresholds for the spline steps are the file's own readings, and two of the measures are close to circular, so they will tend to pass by construction.
- **Fig. 3e p-value:** the legend and the Results disagree (< 1e-7 against < 1e-6). The Results value is recorded.
- **Not read:** the Extended Data figure images and the supplement PDF, so panel details such as the cluster count in Fig. 3b and the snippet length could not be checked.

The `checks` entry is set to `ready: true`.
