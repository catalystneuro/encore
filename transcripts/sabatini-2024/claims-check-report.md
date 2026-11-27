The checker passes after my edits: `claims/sabatini-2024.yaml: 34 claims, 34 quotes, 22 statistical values, 0 problems`. It also passed before them, with 21 statistical values.

**Changes, by claim**
- **fig3a-eigenvalue-clusters:** the criterion required at least three rotation pairs. A 5-dimensional fit, which fig2c allows, can hold only two. Pairs are now judged as far as each dataset's dimensionality allows.
- **fig3c-eigenvalue-distance-auc:** the code's vector-norm distance was the main measure. The Figure 3b legend and the Methods both average over corresponding eigenvalues, so that is now the main measure and the code's norm is the variant.
- **fig4b-plane-alignment** (and **suppfig6a**, which follows it): the criterion replaced the paper's signed-rank test with the code's rank-sum test. The signed-rank test can be run by pairing per condition, so that is now reading (a) and rank-sum is reading (b). The Methods' 36 repeats now decide, with the code's 200 as a variant.
- **fig4d-jpca-variance-correlation:** the criterion could never pass. With 72 conditions, any correlation above about 0.23 is significant, so every plane in 0.39–0.46 contradicts only 66% of planes being significant. I named two readings for what the range covers.
- **fig6e-kinematics-predict-location:** the 1000 permutations are not in the paper. They are now marked as a standard choice.
- **fig7f-ldr-decoding:** I removed the requirement to beat a shuffled null at p < 0.001. The paper reports no result for that comparison, so it is now reported but does not decide.
- **suppfig8-no-output-potent-dependence:** the file recorded "p > 0.04", which the paper does not say. The paper gives p = 0.04 to 0.96, now recorded as those two values.

**Still open** (logged in `checks`)
- **suppfig3:** the main reading compares a cross-validated value for the paper's model with in-sample values for jPCA and the single-condition models. The legend says the comparison is cross-validated, but the Methods give no cross-validated value for those two.
- **suppfig8:** the pass threshold of p ≥ 0.036 is the file's own choice; the paper gives none.
- **fig6c:** the paper's finding is qualitative. The circular-correlation test is the file's own choice.
- **The analysis code:** many details (windows, folds, penalties) come from it, and I did not re-read it. I took those details as the writer reported them.

**Ready:** yes. All 34 claim ids are unchanged, every main finding has a claim, and none comes from outside this paper. Nothing was committed or pushed.
