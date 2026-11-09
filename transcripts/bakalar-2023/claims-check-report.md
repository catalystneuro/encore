I've finished checking the claims file. I made four small corrections and noted four inconsistencies in the paper that I could not settle; the file is ready for an attempt.

**Checker:** `claims/001362/10.1111-jne.13286.yaml: 27 claims, 26 quotes, 59 statistical values, 0 problems`, both before and after my edits.

I compared every claim against the main text, the legends for Figures 1 to 13, Tables 1 to 4 and the Supplemental Methods. All the recorded numbers match the paper: the Table 4 U values and percentages, the PCA variances and loadings, and the test results in the legends. The c-Fos method (431 regions, 1.5 IQR outliers, Mann-Whitney, `fdr_tsbky`) is the one the Supplemental Methods give. The reasoning that the test is exact and two-sided holds: 2/C(19,8) = 2.65e-05, which is Table 4's raw p for DG-sg. Each main finding has a claim, and none comes from outside the paper.

**Changes, by claim:**
- **fig2b-pc-index-behaviours:** the statement said PACAPko mice "spend more time" in these behaviours. I changed it to "score higher (time, or distance for travel)", because travel distance is a distance, not a time.
- **table3-pca-loadings:** I added a note to the criterion. Table 3 gives "Climbing on cage bottom" a PC1 loading of 0.9, above cage-top hanging at 0.88, so the paper's "top two" does not follow from its own table. The criterion now says the rank is not judged.
- **fig2a-two-trajectories:** the paper reports no test for this pattern. The criterion now says its rule (comparing spreads, and mice above the control range on one component only) is the reader's own.
- **fig13a-sim1-tb-unchanged, and fig13c-pac1ko-tb-unchanged, which follows it:** the Figure 13 F-tests have whole-number degrees of freedom (F(2,30), F(2,24)), so no Geisser-Greenhouse correction was applied there. The criterion had carried that correction over from Figure 12B.

**Still open** (recorded in `checks`):
- **Figure 12 mouse count:** the legend gives 37 mice (20 WT, 17 PACAPko), but the degrees of freedom imply 38.
- **Figure 13A mouse count:** the legend gives 19 mice, but F(2,30) implies 17.
- **Second test day:** Figure 3A calls it p29 and Figure 3B calls it p28.
- **Figure reference:** the text cites Figure 12c for the drop in body temperature on fasting, but the legend puts it in 12B. The claim follows the legend.

**Ready:** yes, recorded as `ready: true`. Nothing was committed or pushed.
