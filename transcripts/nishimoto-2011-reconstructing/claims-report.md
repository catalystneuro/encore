I wrote `claims/nishimoto-2011-reconstructing.yaml`. The quote checker passes: 10 claims, 10 quotes, 5 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record (main text, figure legends, Experimental Procedures) and its Supplemental Information (Figures S1 and S2 with legends, Supplemental Experimental Procedures). Rendering the PDF pages failed, so I read no values off figures; every number comes from the text. The paper links no code and names none, so I read no code.

**Claims:** 10 claims, all with quotes. Five carry statistics entries (Wilcoxon signed-rank, Wilcoxon rank-sum, and the t test for a correlation coefficient, all p < 0.0001). Three have expected values:
- prediction accuracy of 0.24, 0.39 and 0.40 for the static, nondirectional and directional models;
- identification of 464 of 486 volumes for subject S1;
- reconstruction correlation of about 0.3.

Every claim has a criterion. Six can be tested on the dataset:
- prediction accuracy;
- the small gain of the directional model over the nondirectional one;
- motion models beat the static model in every area, with V1 best;
- optimal speed rises with eccentricity;
- identification for S1;
- color adds nothing (from the Discussion, with no data shown).

Four claims need outside data (`with_inputs`):
- the retinotopic maps, which the paper compares with multifocal mapping data;
- identification with 1,000,000 clips;
- the reconstructions;
- reconstruction accuracy.

**Details left open, and the readings named:**
- **Gabor envelope sizes and filter length:** a standard constant-bandwidth choice with about 10 frames, plus variants at half and double size. Smaller items (the log offset, how 15 frames become one sample, the z-score data) get standard choices.
- **How the L1 penalty or stopping point is chosen:** (a) a held-out 10% of training data in 50 s blocks; (b) cross-validation over the training data.
- **Observed test signal:** (a) the mean of the ten repeats; (b) correlation with each repeat, averaged.
- **Voxels averaged for accuracy:** (a) all ROI voxels; (b) the 2,000 selected voxels. Subjects are either (i) pooled or (ii) averaged as subject means.
- **Which pairs the signed-rank test covers:** both comparisons in the Fig. 2 legend are run.
- **What V1 is compared with in the rank-sum test:** (a) each other area in turn; (b) the other four areas pooled.
- **The p-value for "accuracy p > 0.01":** (a) on the test data; (b) on the held-out training data.
- **How peak frequencies are taken:** (a) the maximum of the joint map; (b) the maximum of each marginal curve.
- **Model used for identification:** (a) four delays; (b) the single 4 s delay.
- **Tikhonov penalty:** chosen on held-out training data, with a range shown.
- **What "about 0.3" refers to:** (a) the AHP mean per subject; (b) the larger of the MAP and AHP means.
- **The color model:** read as the same filter bank applied to the A* and B* channels as well. The paper names no test, so I set one.

Two thresholds are set by me, not the paper, and each criterion says so: "small" for the directional gain is taken as less than a tenth of the nondirectional gain, and the retinotopy thresholds are mine because the paper only shows the maps.

**Missing from the paper:**
- **Outside data:** the sampled movie prior (about 18,000,000 s of YouTube clips), the 1,000,000-clip identification set and the multifocal mapping data are neither deposited nor located. The four claims that need them may have to be blocked.
- **Data mismatch:** the paper gives sample counts of 7,128 and 486, while the data description lists 7,200 and 540 timepoints. Matching the two is left to the author.
