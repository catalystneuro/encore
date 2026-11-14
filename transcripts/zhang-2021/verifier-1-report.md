**A. Outcomes** (11 claims in the claims file)

| claim | outcome | reason |
|---|---|---|
| fig1-csi-s2 | reproduced | Cell 15: with the code's positions (R3) S2 gives 0.740, 0.718 and 0.676, all within tolerance and above every null value under both permutation readings (p ≤ 1/1001). The R2 reading also passes. The 2-D variant fails only on attend-humans (0.664 against 0.675). |
| att-csi-group | reproduced | Cell 18, R3: the means are 0.665, 0.729 and 0.525, all within tolerance. Reading (b), the group mean above every mean null value, passes for all three conditions. Reading (a) fails for passive because S3 passive (0.061) does not exceed every null value. |
| supp-csi-per-subject | reproduced | Cell 20: R3 has 10 of 12 values within tolerance, R2 has 11 of 12, and all 12 are significant at p < 0.01 under null (a). The misses are S3 passive (0.061 against 0.05 ± 0.005) and S5 attend-humans (0.767). |
| att-passive-lower | not_reproduced | Cell 22: at most 3 of 5 subjects count at the bound (R3, matched, ii, reading b), and 4 of 5 are needed. S1 and S6 have passive CSI at or above attend-humans, so d_mean is about 0 (p 0.38 to 0.53), and this holds under every reading. The 4 of 5 in the R1/matched/i row at p < 0.05 is the variant that does not decide. |
| att-classification | reproduced | Cell 24: contiguous folds give 44.4% (Euclidean) and 53.4% (density), and random folds with Euclidean give 46.6%, all within 48.4 ± 7.6 and above every null mean. Chance under the procedure is 7.8 to 9.1%, against the paper's 8.3%. |
| att-weights-cortex | blocked (data_missing) | Cell 25: the paper's per-subject ROIs from localizers are not deposited. Part of the claim could still be tested with an fsaverage atlas (see B3). |
| game-csi | reproduced | Cell 28, reading (b): S1 0.702 and S7 0.581, both within tolerance and above every null value. Reading (a) misses for S7 (0.549 against a lower bound of 0.558), and reading (c) misses for both. The pass therefore depends on one reading, with 7 and 6 clusters. |
| game-mutual-negative-projection | reproduced | Cell 30: with the dataset column order, both projections are negative at p = 5e-5 in both subjects, under both sign rules. With the Table 1 order, S7's safe-explore on engage-close is -0.018 (p = 0.94), so the result depends on the order. |
| fig3b-state-relations | reproduced | Cell 32: under every reading each subject has many significant off-diagonal pairs (S1 45 or 48, S7 32 or 20), some pairs are significant in one direction only, and the two subjects' sets differ. |
| game-classification | partially_reproduced | Cell 34: every reading is significant (p = 0.001). S1 lies above tolerance under all readings (42.8 to 54.6% against 32.8 ± 3.8), so no reading puts both subjects within tolerance. S7 is within tolerance only with contiguous folds. Chance matches the paper's 11% where all 9 classes are kept (11.1%). |
| game-weights-two-groups | blocked (data_missing) | Cell 35: the region definitions are not deposited, and S1's game data match no mapper. Only S7 could be tested in part, with an atlas. |

**B. Problems**

1. [does not affect a conclusion] Attention third axis (cells 6 and 7; `att_positions`). In the deposited deconvolved files each attentive condition is z-scored per voxel. Because of that, the OLS weight of the attention variable is about 1e-14, and the code's third axis is set by rounding noise (its correlation with the rewrite is only 0.08 to 0.40). The R3 CSIs therefore depend on the machine, and the noise axis adds about 0.03 to 0.08 over the 2-D plane. The notebook found this and bracketed it with R2 (100 random axes). For S2 the R2 5 to 95% range stays within tolerance, so fig1, att-csi-group and supp do not hinge on it. The paper's data may not have had this property.
2. [does not affect a conclusion] att-passive-lower, refit null (i) for R3 (cell 22). In the null, mixing conditions gives the attention axis a real weight, while the observed third axis is noise, so the observed value and its null are not computed the same way. Separately, the observed CSIs average 10 Monte Carlo seeds while each null draw uses one seed. Null (ii) has neither issue and gives the same counts. The outcome is also fixed by S1 and S6, whose raw differences are about 0 or negative.
3. [affects a conclusion] Both blocked claims (cells 25 and 35). The claims file leaves the choice of an outside ROI source to the author and names "an fsaverage atlas through the data set's mappers". I checked the archive myself:
   - The current mappers match the voxel counts of all five attention subjects (S1 51,608; S2 48,819; S3 47,512; S5 52,044; S6 52,349) and of S7's game data (87,000).
   - S1's game data (73,594 voxels) match neither the current S1 mapper (51,608) nor `Mappers/old/S1.hdf`, which I read: 81,137 voxels.
   
   So att-weights-cortex could have been tested in part on all five subjects with atlas ROIs (for example FFA, PPA, EBA, RSC, OPA parcels on fsaverage), and game-weights-two-groups on S7 alone. "data_missing" is accurate for the paper's own ROIs, but the claims file also offered the atlas route, and the notebook gives no reason against it beyond "a substitute". The notebook also never checked the old mappers.
4. [does not affect a conclusion] S1 game data (cell 9) hold 1,950 TRs, which is 65 min at a 2.0045 s TR. Both the paper and the data description say one subject played 90 min and the other 45 min, and S1's voxel count matches no mapper. The deposited S1 game data may not be the exact input the paper used. The notebook reports this but does not draw it into game-classification, where S1 is far above the paper's value.
5. [does not affect a conclusion] Label timing for the game (cell 10). The game CSI peaks at a lag of +1 TR in both subjects (S1 0.729 against 0.691 at lag 0). The notebook calls this "within one TR" and uses lag 0 without examining the shift. For non-deconvolved BOLD a delay would be expected, and at lag +1 reading (a) for S7 would fall within tolerance. Since game-csi passes under reading (b), the outcome stands, but the alignment of the game labels was assumed and not established.
6. [does not affect a conclusion] Leakage from random folds (cells 24 and 34). Shuffled TR folds put autocorrelated neighbouring TRs in both training and test sets. Random-fold accuracies are higher than contiguous ones: S7 33→41%, and attention with the density rule 53→56%. Contiguous folds also have no gap at their edges. The attention outcome is decided under contiguous folds, and S1 in the game is above tolerance under both fold schemes.
7. [does not affect a conclusion] game-classification, reading (a) with the density rule (cell 34). `cl` can drop a class within a fold while `H` still scores it, which gives that class a recall of 0 and biases the result downward. The values are already above tolerance.
8. [does not affect a conclusion] fig3b (cell 32). The two-sided p uses |null| ≥ |M| centred on zero, not on the null's centre. Because rows are permuted together, mutually exclusive states keep a shifted null. Significance is so widespread that the outcome does not change.
9. [does not affect a conclusion] With 1000 permutations the smallest attainable p is 0.001, not the paper's 1e-5. The claims file accepts "exceeds every null value" as the stand-in, and the notebook applies it consistently. The game projection tests use 20,000 permutations (p = 5e-5).

I checked the helper functions on synthetic inputs, and they are correct:
- `jsd` gives 0 for identical normals, 1 for far-apart ones, and 0.3185 for a 1-D case whose analytic value is 0.3191.
- `pca_scores` matches scikit-learn's full PCA to 1e-12, including held-out projection with the training mean.
- `positions` equals `code_positions` (|r| = 1).
- `shuffle_conditions("matched")` gives each condition every frame exactly once.
- `balanced_accuracy` is correct on a toy case.

The claims file's reading of the paper agrees with the passages I checked: the Methods paragraph on classification and the permutation test, and the legends of Figures 1 and 3 and Supplementary Figure 1.

**C. Not checked, and what would have let me check it**

- Whether the code's own third axis on the full data (R3) is also noise on the code path. The notebook prints the attention weight only from the PC-space rewrite. Printing the code's `coeffs` norm for the attention row would settle it.
- The full null distributions for att-passive-lower, for example S2's d_mean null quantiles. With them I could judge how close S2 is to counting.
- The S1 game run structure. Run boundaries or per-run TR counts would show whether 65 min is a subset of the 90-min session.
- The game CSI and classification with labels shifted by +1 TR. This would show whether the label alignment affects game-csi reading (a) and the game accuracies.
- Atlas-based ROI mean weights for the five attention subjects and for S7. With these, the two blocked claims could have been tested at least in part.
- I did not look at the cell 16 image of S2's state space. It is not needed for any criterion.
