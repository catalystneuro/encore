I've written `claims/zhang-2021.yaml`. The quote checker passes it: 11 claims, 11 quotes, 9 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record (PMC8145286), full text with Methods, figure legends and Table 1. The supplement (Data_Sheet_1.DOCX) has the legends of Supplementary Figures 1 to 5. No PDF was supplied. The per-subject CSIs for the attention task are printed only inside the images of Supplementary Figures 1 and 2, so I read them from those images. The code is gallantlab/state-space at commit 6ffb3c30. It covers the state space, the HRF deconvolution and the JSD, but has no CSI averaging, no classifier, no permutation tests and no video game analysis.

**Claims:** all 11 have quotes and none uses `inferred`.
- 9 have statistics. All are permutation tests: seven at p < 1e-5, one at p < 0.01, and Figure 3B at p < 0.01 with Bonferroni correction.
- 7 have expected values: the S2 CSIs, the group CSIs, the per-subject CSIs from the supplement, the "5 of 6 subjects" count, attention classification, the video game CSIs and video game balanced accuracy.
- All 11 have criteria.
- The cortical-weights claim for the attention task is `with_inputs`, because it needs ROIs (regions of interest). The paper drew them from localizer data that it does not deposit and that the dataset's description does not list.

**Details the paper leaves open, with the readings named:**
- **Permutations:** the number is not given (p < 1e-5 needs at least 1e5); I set at least 1000. Labels are either shuffled freely or circularly shifted within each condition.
- **Group p for the CSIs:** either every subject is significant, or the mean CSI is compared against the mean of the null CSIs.
- **Passive against attentive test:** passive is compared against each attentive condition or against their mean. The null either refits the state space each time or keeps it fixed and reassigns TRs to conditions.
- **Cross-validation folds:** contiguous tenths of the data or random TRs. Held-out positions are z-scored with the training statistics.
- **Nearest cluster:** Euclidean distance to the cluster mean, or the highest density under the fitted normal distribution.
- **Video game clusters for the CSI:** one cluster per state with TRs in every state they have, one per state using only TRs with a single state, or the three groups of Figure 3A.
- **Video game classification labels:** TRs with exactly one state only, or every labelled TR counted correct for each of its states.
- **Weights mapped onto the cortex:** the regression weights B, the denoised weights B_L, or the state directions Q_S.
- **Video game grouping:** the paper gives no measure, so I fixed one: correlations between weight maps with two-group clustering.

**Things missing or inconsistent that claims needed:**
- **Figure 3B:** the main-text figure images were not available, so the pattern of significant state relations is unknown. That claim's criterion is structural only.
- **ROI definitions:** not deposited. The ROI parts of both cortical-weights claims depend on an outside source the author has to choose.
- **Subject S4:** not in the dataset, so the attention-task claims across subjects are tested on 5 of 6 subjects.
- **Group means:** the per-subject CSIs in the figures average to 0.64, 0.72 and 0.51, not the 0.66, 0.74 and 0.53 the Results print.
- **Figure 1 colours:** the legend swaps blue and green compared with the supplement legend and the plotted positions.
- **"Five of six" count:** on the raw figure values, S1 and S6 do not have a passive CSI below both attentive ones. The test the paper used is unstated.
