The claims file for martinez-conde-2019 is ready for an attempt. I made four small corrections and left four open points that only the missing supplement could settle.

**Checker:** after my edits it still reports `claims/martinez-conde-2019.yaml: 19 claims, 14 quotes, 2 statistical values, 0 problems`.

**Changes, by claim:**
- **fig7d-nonlinear:** the statement said the relation is "not linear". The abstract and Introduction say "apparently non-linear", and the Discussion (paragraph 5) says the authors cannot be certain, given how few angles they tested. I added both. I also marked the criterion's SEM rule as an assumption, since the paper reports no test.
- **spikes-per-condition:** the criterion fixed the spike count as the total of the spike count map, but the paper does not say which spikes its 35,998 counts. I named two readings: the map total, or all spikes recorded in the condition.
- **fig7c-fold-edge-equivalence:** the "within one step" margin and the rule for P180 under the RMS-contrast reading were the writer's own. I marked them as assumptions; the paper gives no margin for "roughly equivalent" or "close".
- **fig5-average-maps:** both measures of the maps are now marked as assumptions. I also noted that the midpoint reading gives the same means as fig4b-spike-rate-difference (averaging is linear), so it is not an independent test.

Everything else checked out against the paper, including all Table 1 values and SEM tolerances, the block sizes, the neuron counts, the sources and quotes, and the data kinds. Each main finding has a claim, and no claim draws on anything but this paper.

**Still open (recorded under `checks`):**
- S1 and S2 Tables are not in the text, so the comparison families, corrections and exact p-values behind Fig 4B and Fig 7C stay open as readings.
- The paper does not name the test behind the S4 Fig claim that baselines do not differ. The three readings and the tie rule stay.
- The paper does not say whether the Corners S40 midpoint averages the two S40 folds, as it does for the Square and the Star.
- The definition of RMS contrast comes from reference [21], which is not in the text. One of the two readings (standard deviation of luminance scaled to 0 to 1) cannot exceed 0.5, so it cannot give the paper's range of 0.61 to 0.943. I kept it but noted it as unlikely.

**Ready:** yes, entered as `ready: true`. Nothing was committed or pushed.
