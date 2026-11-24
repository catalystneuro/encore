The file is now ready for an attempt. I made 17 changes and left four points open, each named with its readings. I only edited `claims/gonzalez-2024.yaml`, and nothing is committed or pushed.

**Checker result:** `claims/gonzalez-2024.yaml: 30 claims, 30 quotes, 39 statistical values, 1 problems`. The one problem is `VALUE NOT FOUND fig3g-decoder-tracks-behaviour 3.61e-10`. The text prints that p as "3.61 − 10", without the "e", so the checker can't match it; I confirmed it by reading, and the file notes it.

To check the code citations I cloned the paper's code repository (alexgonzl/TMA) at the cited commit into a temporary folder. Most of the earlier reader's citations held up. The code also settled several details that the file had either left open or filled with guesses.

**Changes, by claim**
- **fig1d, fig1-switch:** the code takes the median of the subjects' medians, and its printed output matches the paper (72.6%, 110.25, 76.9%, 54). The median over all sessions pooled is now a variant. The 10-point "similar" threshold is now marked as an assumption that the outcome rests on.
- **fig2e, fig2f:** the Kendall entries carried the p-value of the likelihood ratio test. The tau values now sit in the test's own entry.
- **fig2h:** added the code that computes the per-subject bootstrap.
- **fig3e:** the file had guessed the unit groups (≤8, 9 to 19, ≥20 units). The code uses thirds of the sessions ranked by unit count. The models are now taken from the paper's notebook, whose printed test results match the paper (17.05 and 214.31).
- **fig3f:** the Results say the session counts are for the stem, so I removed the invented "last zone" reading and the statement now says stem. I also replaced the invented label-shuffle reading of "above chance" with the notebook's rule, which reproduces exactly 19/42 and 23/36.
- **fig3g:** the model now comes from the notebook, and the null model is named as open (see below).
- **fig4c:** the code counts units within one unit type only, so the counts are read on isolated units, with MUA alone as a variant.
- **fig4ef:** the statement now says "negatively", matching the paper's values. Added a note on the printed p of "3.06 − 20".
- **fig6cd:** added a note on the printed p of "3.44 − 190".
- **fig4s6:** the |U_Z| > 1.96 threshold was made up. I replaced it with the code's definitions of correct and incorrect coding.
- **fig7b:** added the code's default UMAP settings for waveform matching.
- **fig7f:** removed the "p < 0.05" entry. It is the legend's star key, not a reported result.
- **fig7g:** the statement says remapping stays significant on matched units, but the criterion didn't test that. I added the test.
- **fig7h:** named which encoders count as "rate" and "global", and added the code's rule that R² values beyond ±1 are left out.
- **New claims:**
  - `fig4gh-reward-remap-population-subject` covers Figure 4g and 4h, which the Results and Discussion report and no claim covered.
  - `fig4-reward-remap-behaviour-controls` covers the reward control analyses in Figure 4, supplements 3 and 4.

**Open**
- **fig1-switch:** the paper gives no test or threshold for "similar", so the threshold stays an assumption.
- **fig3d:** the Methods say 5 cross-validation folds and the code uses 10. Both are run.
- **fig3g:** I couldn't find which null model gives the paper's chi2(2) = 43.48. The notebook's printed test has 4 degrees of freedom and gives 65.91. Both readings are run.
- **fig3g:** the p-value is printed in a garbled form, read as 3.61e-10.

The main findings are all covered, and every claim comes from this paper.
