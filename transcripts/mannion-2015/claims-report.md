I wrote `claims/crcns-vim-3/10.7717-peerj.1038.yaml`. The quote checker passes: 16 claims, 16 quotes, 10 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record (PMC4485252, from the Europe PMC XML): main text, Methods, Results and Discussion, the legends of Figures 1 to 5, and the legends of Figures S2 and S3. There was no PDF, so I could not read values printed only inside figures (the psc differences in Fig. 4, the points in Fig. 5). The supplementary files themselves are not under `paper/`: Fig. S1, Table S1 (complete ANOVA output) and the S2 and S3 images. No claim needs Table S1, because the text states both ANOVA effects the results rest on.

**Code.** The paper's Bitbucket link is dead. The same repository is on GitHub as mannion-lab/ul_sens_fmri_analysis; I read commit 571e931 (2015-05-22). For design constants only, I also read the experiment code, mannion-lab/ul_sens_fmri at 5e98dd8. The three-way ANOVA was run in SPSS, so no code for it exists.

**Claims.**
- **Coverage:** 16 claims, all with quotes. 10 carry statistics, and 10 have expected values (only the presentation-by-source and three-way interaction F values are in both). 7 are claims of absence.
- **fMRI results:**
  - The presentation-by-source interaction: F(1,6) = 11.19.
  - The three-way interaction is not significant: F(1.9,11.4) = 1.52, p = 0.260.
  - Lower visual field, below versus above fixation: 0.80 versus 0.72 psc, t(6) = 5.17.
  - Upper visual field shows no difference: t(6) = 0.38.
  - The two Fig. 4 counts (4 of the top 5 patch pairs match their source in each direction).
- **Image statistics (Fig. 5):** six Spearman correlations, plus the null results for the other pixel and filter measures and for radial bias.
- **Other:** localiser masks lie ventral for upper and dorsal for lower; no task-performance difference (Fig. S2); no residual-error difference (Fig. S3); residual error larger for upper than lower presentation (S3 legend).
- **Data:** the 7 image-statistics claims are marked `with_inputs`. They need the stimulus screenshots and the monitor's CIE calibration. The calibration is not given in the paper or the code, and neither is the DKL conversion function, which comes from an unlinked helper package.

**Details left open, and the readings named:**
- **Spatial-frequency correlations:** the paper says Spearman; the code uses Pearson. Spearman is the main test and Pearson is a variant.
- **Fig. S2 (task performance):** the paper reports no test. The code runs a two-way repeated-measures ANOVA on lags 0.4 to 0.9 s, which I used, with 0.05 as the threshold because the paper prints none. The code assigns targets to conditions with a 32 s offset that doesn't match how it bins them. Readings: (a) the code as written; (b) assignment in absolute run time, which the legend describes.
- **Fig. S3 (residual error):** no test in the paper or the code. Readings: (a) paired t-tests at each time point; (b) a two-way repeated-measures ANOVA on the window average.
- **Radial bias:** the paper names no test. The code runs 12 uncorrected paired t-tests; testing the luminance channel alone is a variant.
- **Judgements with no measure in the paper:** "largely confined" (localiser masks) is judged by majority of nodes in the ventral or dorsal half. The Fig. 4 content (uniform sky versus variegated ground) is a visual judgement, and its outcome is marked as resting on it.

**Settled by the code where the Methods are silent:** the localiser threshold (t > 2.58, positive only), averaging across hemispheres, one GLM regressor per image and source, the circular masks for the pixel statistics (radius 0.8) and filters (0.9), averaging left and right patches, and the SE normalisation.

**Missing:**
- From the paper: the monitor calibration and the DKL conversion, which the image claims need.
- From the archive, per its data descriptor: anatomical images and V1 to V3 definitions. Every fMRI claim needs these.
