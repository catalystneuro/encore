I answered the one question (fig4b-roi-changes-counts), and the claims file changed.

**Question 1: should the criterion use the Fig. 4 script's test and threshold, and is "of the 122 ROIs" right?** Yes to both, so I amended the claim.

- **Test and threshold:** I read the deposited script `code/Fig4 Fujimoto_NatNeuro_2026_FCmatrix.m` from the DANDI archive (the code only, no data). It does what the question says: a rank-sum of each ROI's changes against zeros, `ranksum(sbj_data_mean,zeros(length(sbj_data_mean),1))>=0.05/nrois`. This matches the Extended Data Fig. 10c legend wording, "changes ... from zero ... rank-sum test". The paper's own tables support the script's threshold over the Methods' "P < 0.01 with Bonferroni correction". The largest P in Supplementary Tables 1 and 2 is 3.9e-4, which is above 0.01/123 (8.1e-5) and below 0.05/123 (4.1e-4). Those two tables list 69 and 44 ROIs.
- **New criterion:** each ROI's 122 changes, with the diagonal excluded, are tested against zeros by rank-sum, and an ROI counts when P < 0.05/123. Only this reading is judged. The Methods' threshold, the pre-against-post rank-sum and the signed-rank test are now reported as variants.
- **ROI count:** Supplementary Table 3 lists 123 ROIs, so the statement now says "of the 123". The legend's n = 122 is the number of values per ROI.
- **Also changed:** I corrected the same 122 vs 123 misreading in the header notes and in fig4c-network-sorted-reduction.
- **Unchanged:** the expected counts stay at 69 and 44.

`answered: 2026-11-03` is set on the question.

`tools/claims_check.py` reports the same 8 "value not found" items the file's earlier check already recorded as confirmed by reading; it found nothing new.

Only `claims/001773/` and `questions/001773.yaml` are modified. Nothing is committed or pushed.
