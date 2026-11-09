I checked the claims file for DANDI:001773 against the paper, corrected 11 claims and the header notes, and judged it ready for an attempt. Nothing was committed or pushed.

**Checker result:** `32 claims, 31 quotes, 54 statistical values, 8 problems`. There are no schema errors and every quote is found word for word. The 8 problems are all "VALUE NOT FOUND" reports for p-values the paper prints in a form the checker does not match, such as `7.70E-06`, `0.999909913`, a garbled `9.10 × 10 −1 3`, and `6.20 × 10−7` with no space. I found each one by reading Supplementary Table 9 or the figure legends, and all are correct. The checker will keep reporting these 8 because the values themselves are right.

**Changes, by claim**
- **Opening comment:**
  - Which comparisons the Tukey-Kramer post hoc test covers was presented as fixed; the paper only says "post hoc Tukey–Kramer test". It is now marked as a reading.
  - Removed the statement that two ways of computing sums of squares "cannot differ much"; the voxel counts per cell are unequal, so they can.
  - Added the protocol rule that a claim is blocked as `methods_underspecified` when its readings give different outcomes.
- **fig4b-roi-changes-counts:** removed the statistics entry (rank-sum, P < 0.01 Bonferroni). It is the threshold used to count significant ROIs, which the protocol treats as a method, not a result. It stays in the criterion.
- **ed5-cc1-count-dapi-unchanged:** added the reported effect size for the CC1 count (partial eta squared 0.054) as an expected value, with 10% tolerance.
- **ed6-dacc-ufm-no-oligodendrocyte-change:** the statement and criterion now cover the CC1 and DAPI counts as well as the ratio. The paper reports all three as not significant, and the claim already listed all six tests.
- **fig3f-g-ratio-decrease:** noted that the legend calls the 350 units per hemisphere "fields". The degrees of freedom and the Methods show they are axons.
- **fig4c-network-sorted-reduction:** replaced "negative in the majority of blocks", a threshold the paper never gives, with the sentence's own terms: mean change within networks and mean change across networks, both negative.
- **fig5a-nonsurgical-no-reduction:** added the P < 0.05 map threshold of Extended Data Fig. 8, which the claim cites, next to the P < 0.01 of Fig. 5a.
- **fig5c-vis-no-change:** the visual network is now judged on both hemispheres, since the legend lists no difference on either side. The individual areas are judged on the stimulated side, and the reason is now stated: Table 9 shows a significant change in control-side MT, against the paper's own sentence.
- **fig5c-san-rebalanced:** the statement is now limited to the stimulated hemisphere. The legend gives a significant control-side salience network change (P = 6.20e-7).
- **fig6b-monkey-d-dacc-cb-decrease:** added the paper's caveat, "diffuse reductions were seen across the CB".

**Still open** (recorded under `checks`)
- **fig4b counts:** the 69 and 44 are counts of P values in the extracted Supplementary Tables 1 and 2. The extraction drops at least one value (area_8B), so a count off by one or two can't be excluded without the PDF tables.
- **fig6d:** "very little alteration" has no test in the paper, so the criterion is a reading. Extended Data Fig. 10d also reports a significant sham-side vmFC change of unstated direction.
- **ed1-monkey-d-no-change:** the paper reports no test for monkey D. The criterion applies the Methods' ANOVA to one animal, which is a reading.
- **Analysis code:** the paper's MATLAB code is deposited in the dandiset, so neither reader has read it. It may settle the Tukey comparisons, how runs are combined for the seed maps, the limbic network membership and the Fig. 4c network assignment.

**Ready:** yes (`ready: true`). The paper's main findings each have a claim, and every claim comes from this paper.
