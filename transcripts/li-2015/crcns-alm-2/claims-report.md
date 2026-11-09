I wrote `claims/crcns-alm-2/10.1038-nature14178.yaml`. The quote checker reports 23 claims, 23 quotes, 11 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (a PDF extracted to text), with the main text, figure legends, Methods and the legends of Extended Data Figs 1 to 7. The paper has no other supplement. No PDF renderer is installed here, so I could not view any figure as an image. Values printed only inside figure panels, such as the stars in Figs 1d and 5b, are not claimed as numbers. The paper links no code. The data descriptor mentions MATLAB scripts said to reproduce Fig. 4e, g and h, but they are among the dataset's files, so I did not open them.

**Claims:**
- **Count:** 23. All 23 have quotes and none needed an `inferred` note.
- **Statistics:** 11 statistics entries on 9 claims.
- **Expected values:** 13 claims have them, with a 10% tolerance by default. The reaction time uses the paper's s.d., and the counts of fields of view and mice must match exactly.
- **Criteria:** 18 claims have one.
- **Imaging, testable on this dataset (10 claims):** the task-related fraction (58%), the trial-type-selective fraction (57%), the overall contra majority (61%), both preferences in every one of the 59 fields of view, the two spatial-clustering results (P = 0.34 and P = 0.61), selective PT and IT counts in layer 5 (182/534 and 174/542), PT contra preference (122/182, binomial P < 0.001), no IT bias (83/174), and PT against IT (chi2 P < 0.001).
- **Other experiments (13 claims):** electrophysiology, photoinhibition, photostimulation, anatomy and reaction time are marked `elsewhere`. For the anatomy claim no deposit is given. The rest point to the one deposit the paper names, doi:10.6080/K0RF5RZT, though the paper does not say which of its data that deposit holds.

**Details the paper leaves open, with the readings named:**
- **Length of the response epoch:** 1.3 s, or 1.5 s (the lick window).
- **Trials used for imaging:** correct trials only, as in the electrophysiology, or all responded trials grouped by pole position.
- **Contra or ipsi preference:** mean ΔF/F over the three epochs together, or the epoch with the largest difference.
- **Window for the Kruskal-Wallis "task" test:** from sample onset, or from trial start.
- **Response compared by the Wilcoxon test:** the mean over all epochs, any single epoch, or any 0.33 s bin.
- **Nearest-neighbour test:** the neighbour pool is either selective cells only or all cells. The label shuffle is done within each field of view or across all of them.
- **Distance test:** mean or median distance, and the same two shuffle readings.
- **Binomial test for PT:** two-sided or one-sided. For the absence claim on IT, the two-sided test is primary and the one-sided test is a variant.
- **Chi-squared test:** with or without the Yates correction.
- **Standard choices that should not change the outcome:** the 5% brightness comparison (mean ROI against mean neuropil), 10,000 shuffles, and centroid distances.

**Missing:** nothing that the imaging claims need is missing from the paper. The paper gives no explicit significance level for the spatial-clustering tests, so I used 0.05, the level it uses in the Fig. 4h legend.
