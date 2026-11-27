I answered both questions and amended both claims. `python tools/claims_check.py` passes the quotes. It reports one problem, the value -1655.776 in `fig1e-blood-pco2`, which was already there: Supplementary Table 2 prints that number but the checker looks for -1655.78. Only `claims/allen-2026.yaml` and `questions/allen-2026.yaml` changed, and nothing was committed.

1. **fig4b-shared-down-sets: changed.** The Results sentence says 2 of "36 GO gene sets" were down in both treatments, and cites "the intersect GSEA ridgeplot (Fig. 4C)". So the most natural reading of 36 is the sets significant in both treatments, in either direction. That is now reading (a) in the criterion, and the two old readings become (b) and (c). The expected value of 2 and the rule "within 10% of 36 under one reading" are unchanged.

2. **fig4fgh-chronic-up: changed.** The Fig. 4 legend gives 82, 308 and 128 as the counts of the "clustered and simplified terms" in the heatmaps. The paper does not say which up-regulated sets go into the heatmaps. The criterion now has two readings:
   - (a) every chronic-OA set with positive NES;
   - (b) only those not down-regulated under acute-OA, which is what the deposited script uses.

   A count passes if it is within tolerance under either reading. The statement now says the heatmaps hold these sets. The expected values and the named gene-set families are unchanged. I did not open the Dryad deposit, so reading (b) relies on how the question describes the script, and the answer says so.
