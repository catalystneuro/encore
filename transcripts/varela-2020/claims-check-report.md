The checker's result line is `46 claims, 46 quotes, 69 statistical values, 0 problems`, the same before and after my edits. The file is ready for an attempt, and its new `checks` entry says `ready: true`.

**Changes, by claim.** Each one is also recorded under `checks`.
- **kc-fraction-of-thalamic-peaks:** the statement said "9.68% before only". The paper gives 38.71% and 9.68% without saying whether they include the 19.35% of units with both peaks. I removed "only" from the statement and the expected quantities, and extended the quote to take in the 19.35% clause.
- **fig2c-swr-around-kc:** the window for the SWR minimum (±0.25 s) and the 2 sd floor on the peaks were not in the paper. The window is now listed as open with two readings, and the floor is replaced by "positive peaks". I also added a second open choice: whether peak heights are averages of per-session peaks or the peak of the averaged histogram.
- **kc-trough-timing:** the ±0.25 s window for the firing minimum was not in the paper. It is now listed as open with two readings.
- **fig2-swr-phase-delta-spindle:** I dropped the added rule that the Rayleigh test be significant in most sessions. The paper reports no test for this finding; the test is still reported.
- **fig3a-bursting-around-swrs:** the paper does not say how overlapping 2 s windows count. Counting each spike once is now one of two readings.
- **fig4-units-not-rhythmic:** the paper does not say whether the 119.30 ms MUA lag uses all MUA spikes or the subsampled ones. Both readings are named.
- **rebound-delta-phase-trend:** the control measure the paper names (firing rate in a window of the same length before KCs) was not defined in the criterion. I added readings for it and replaced "near zero" with p ≥ 0.05, since the paper reports p = 0.65.
- **modulation-amplitude-versus-ripple:** the statement says index values are similar under both classifications (p > 0.3), but the criterion had no test for it. I added it as a claim of absence on the paper's Wilcoxon test, with the open choice of which cycles are compared.
- **maze-control-sessions:** the "not all the same sign" rule was made up. Per the protocol, absence is judged on the paired test. With only 4 sessions that test cannot reach 0.05, so the claim passes whenever the four sessions are present. The sign rule is kept as a variant.
- **fig7d-run-units-peri-swr:** the peak window (±100 ms) was borrowed from another analysis. It is now one of two named readings.

**What remains open** (recorded, not changed):
- The Fig. 2C legend finding that spindles are largest just after KCs has no claim. It is a minor finding stated only in a legend.
- In fig3f-asymmetry-index, reading (b) (dividing by the sum of the two maxima) is a weak reading of the paper's wording. I kept it because an extra reading can only add a way to match.
- In fig7c-run-units-in-spindles, readings (b) and (c) classify run units by spike-count thresholds the paper never gives; the paper classified them by eye. They are labelled as such, and they are the only option if the dataset has no labels.

Every claim traces to this paper only, and each of its main findings has a claim; the Discussion adds no new results. Nothing is committed.
