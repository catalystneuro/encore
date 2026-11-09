The claims file for 000773 is ready for an attempt. I made two small changes to criteria and found nothing wrong in the recorded numbers.

**Checker result:** `21 claims, 21 quotes, 50 statistical values, 28 problems`. All 21 quotes are word for word. The 28 problems are all "VALUE NOT FOUND": p-values that are printed only inside the supplement figures (Figures S2B, S3B, S4A, S4B, S4D), so they are not in the text file. I rendered those pages from the PDF and every one matches. The per-glomerulus sample sizes in the opening comment match the figures too. The behavior numbers (Table S1 parameters, F statistics, p-values, CI-based tolerances, and trial counts worked out from the degrees of freedom) also match the paper.

I also downloaded the behavior code (Zenodo 10.5281/zenodo.11151756, commit 1aef6bc). It confirms what the file says about how the behavioral proportions are computed: the proportion of young ants outside the nest is out of the colony's young ants, and the same for old ants.

**Changes, by claim:**
- **figs1-heptanone-separate-curves:** The Figure S1 legend doesn't say which age responds faster for this stimulus. The criterion now says the direction comes from Table S1. There the old ants' starting and maximum proportions are higher, but the rate constant K is nearly the same (0.097 against 0.095). So of the two readings of "faster", Table S1 supports "the old curve lies above the young one", not "K is higher". The fitted parameters are now to be reported.
- **fig2e-heptanone-breadth-falls:** The paper drew its glomerulus regions by hand. The criterion's automatic way of finding them is the previous reader's own choice, not the paper's. I added a rule: if its result disagrees with the result from the paper's own counts in Data S2, the claim is blocked as `methods_underspecified` and not decided.

**Still open** (recorded under `checks`):
- The paper never says how each ant's three trials are combined, except for Figure S4C, where they are averaged. The other claims average them by analogy.
- The p-values in main Figures 2D, 2E, 3D and 4 can only be recorded as bounds (p < 0.05 or p > 0.05), because the main figure images aren't in the text. Which pairs Figure 3D marks as significant is handled as two readings in fig3d-pg-stronger-old.
- fig2-alarm-sparse ("only a small fraction" of about 500 glomeruli) has no threshold in the paper. Its 5% and 10% cut-offs are the previous reader's choice.

Every main finding has a claim, and every claim comes from this paper. Claim ids are unchanged, and nothing is committed.
