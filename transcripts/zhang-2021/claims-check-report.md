I checked `claims/zhang-2021.yaml`, corrected six claims and the opening comment, and the file is ready for an attempt. Nothing is committed.

**Checker:** `claims/zhang-2021.yaml: 11 claims, 11 quotes, 8 statistical values, 0 problems`. It reported 9 statistical values before my edits; the count dropped because I removed one entry (see att-passive-lower).

**What already held up:**
- The 15 per-subject CSIs in the file match the images of Supplementary Figures 1 and 2, and so do their p bounds.
- I cloned the paper's code (gallantlab/state-space, commit 6ffb3c3). It matches what the file says about it: the intercept column, the 24-component PCA denoising, the QR step, the z-scoring, the JSD estimate and the axis sign flip in the plots.

**Changes, by claim:**
- **att-passive-lower:** I removed the statistics entry. The paper's p < 1e-5 is the threshold at which it counts subjects ("five out of six"), so it is a method, not a result. The criterion counted subjects at p < 0.05, which the paper never uses; it now counts at p < 1e-5. If fewer than 1e5 permutations can be run, the bound reached is reported, with the p < 0.05 count shown as a variant.
- **att-classification:** z-scoring the held-out TRs with the training statistics is now labelled a standard choice. It follows the code; the paper does not fix it.
- **att-weights-cortex:** the file had dropped the voxel threshold from the semantic encoding model in Figure 2, saying the model's performance was not given. The data set holds the semantic labels and the preprocessed BOLD, so the threshold can be computed. It is now one reading, with no threshold as the other. I also added the regions the Figure 2 legend names on top of the Results (SEF for humans, FO for vehicles).
- **game-mutual-negative-projection:** the file credited its sign rule to the code, but the code has no video game analysis. Two open details are now named, with readings:
  - the sign of each dimension;
  - the order of the nine variables going into the QR step, which changes every dimension after the first.
- **fig3b-state-relations:** now uses those sign and order readings. The number of tests the Bonferroni correction covers is named as open: the off-diagonal pairs (72, or 56 for S7) or every cell (81, or 64).
- **game-weights-two-groups:** the deciding test was a correlation clustering of the weight maps, which the paper never uses. The paper groups dimensions by the regions they project onto, so the test is now the mean weight per region, marked `data: with_inputs` because the regions need an outside definition.
  - The Figure 4 voxel threshold is named as open.
  - The clustering stays as a variant that does not decide the outcome.
  - The measure for "largely consistent across subjects" is marked as the earlier reader's own choice.
- **Opening comment:** the paper does not say which video game subject played 90 minutes and which 45; the comment had assigned 90 to S1. I also added the new open details to its list.

**Still open:**
- The paper's group CSI means (0.66, 0.74, 0.53) are not the means of its own per-subject values (0.64, 0.72, 0.51). The paper disagrees with itself here; att-csi-group already notes this.
- There is no PDF, so Figure 3B and the main-text figures could not be read. fig3b-state-relations therefore fixes no per-pair result.
- In att-passive-lower, the paper does not say which subject is the exception. On the figure values, S1 or S6 fails the passive-against-each-condition reading.

Every main finding has a claim, and no claim comes from anywhere but this paper.

**Ready:** yes (`ready: true` in the new `checks` entry).
