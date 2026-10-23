**Checker result, after my edits:** `46 claims, 46 quotes, 130 statistical values, 0 problems`. Before them it was the same with 123 values; the 7 new values are statistics I added.

**Changes, by claim:**
- **fig1b-dominants-more-rewards:** I removed "rank 1 mice won the largest share of competitions" from the statement and the criterion. No sentence of the paper says it; the legend only names the panel.
- **ed1g-distance-by-outcome-not-rank:** I dropped the "win closer" direction. The legend gives no direction for trial type.
- **ed5d-subordinates-slower-latency:** The criterion cited Methods 6 for a latency counted from reward delivery, but Methods 6 defines no such latency. I reworded it to say that, and that Methods 5 and ED Fig. 1a count latency from tone onset. I also added the legend's one-way RM-ANOVA, F(1,24) = 2.06, p = 0.002, as printed. It is marked as not judged because that F and that p do not agree.
- **fig2a-win-lose-segregated-before-cue:** The 95th-percentile threshold was made up. The criterion now gives two readings (beats the mean random-half distance; beats its 95th percentile). If they disagree, the claim is `methods_underspecified`.
- **ed7hij-random-halves-no-group-effect:** The criterion said sessions were split into halves, which the paper does not say. What gets split is now open: (a) sessions, (b) neurons.
- **fig3a-functional-clusters:** The chi-square test was made up; the paper reports no test of the rank difference across clusters. That part is now shown but not judged, and the outcome rests on the cell counts.
- **ed9b-alone-no-rank-difference:** I added the six rank-sum p-values on response magnitudes from the legend. The criterion already judged those tests.
- **ed9cd-self-entry-cells-competition:** The statement now says the intermediate-rank ITI test was not significant (p = 0.06). The criterion reports that test without judging it.

**Open (recorded under `checks`, not settled):**
- **ed5j-six-states:** The criterion assumes 1 to 10 states were tried and counts 5 or 7 states as a partial result. Neither comes from the paper.
- **ed7de-trajectories-close-far:** The legend prints the same F and p (F(1,35) = 588, p = 3e-20) for "win far" and "lose close". This may be a copying error in the paper.
- **ed10c-lh-responsive-proportions:** The printed Fisher p = 0.011 matches no event in the legend. Recomputing from the printed counts gives 0.006 and 0.06.
- **Coverage:** Three control panels (ED Fig. 1c, 1h, 5a) have no claim. Every main finding has one, and all claims come from this paper.

**Ready:** yes. The last check is marked `ready: true`. Nothing is committed.
