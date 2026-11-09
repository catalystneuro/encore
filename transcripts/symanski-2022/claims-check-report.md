The claims file is ready for an attempt: I set `ready: true`. I changed 23 claims and left five problems open, listed below. Only `claims/001539/10.7554-elife.79545.yaml` changed, and nothing is committed.

**Checker result:** `47 claims, 47 quotes, 101 statistical values, 1 problems`. The one problem is a false alarm. The checker can't find 1.80e-4 for `fig2d-beta-power-increase` because it only looks for "1.8e-4". The paper prints "PFC p=1.80e-4" three times.

**Changes, by claim**
- **Outcome rule across readings (17 claims).** These criteria counted a claim as reproduced if it matched under any one reading. Here the readings are method choices that can change the result: LFP pipelines, time windows, how the selectivity index is computed, thresholds, chance levels, window alignment, cell sets. The protocol says the outcome must be the one every reading gives, and the claim is blocked as `methods_underspecified` when they disagree. The criteria now say this:
  - `fig2d-beta-power-increase`
  - `fig2e-beta-coherence-increase` (and `fig2e-rr-coherence-increase` by reference)
  - `fig2e-beta-coherence-odor-vs-reward` (and `fig2e-rr-coherence-odor-vs-reward`, `fig2d-power-odor-vs-reward`)
  - `fig2g-air-beta-coherence`, `fig2s2d-phase-offsets`, `fig2s1e-run-theta-shift`
  - `fig3ij-si-anticorrelated` (and `fig4c-interneuron-si`)
  - `fig4d-ccg-lags`, `fig5d-cross-region-beta`, `fig5-rr-more-than-beta`
  - `fig6e-glm-choice-prediction`, `fig6e-glm-with-interneurons`, `fig7f-spatial-decoder-all-quintiles`
- **Methods before code.** In `fig6d-discrimination-time` and `fig7e-odor-decoder-first-quintile`, the code's choice of cells had been treated as a reading. The paper's text states which cells, so the code's choice is now a variant.
- **`fig2s1f-rr-beta-coupling`.** Using correct trials only had no source, so it is now one reading beside all completed trials. I removed an invented "majority of sessions" rule: the legend shows one pooled modulation index per region, so that is the test.
- **`fig7s1f-ensemble-rate-near-port`.** I removed an invented "more than half the marked positions" rule. The criterion now tests what the Results say: the rate peaks within 20 cm of the odor port and is lower beyond.
- **Statements that said more than the paper:**
  - `fig1s1f-air-performance`: dropped "near chance".
  - `fig3s1c-odor-vs-reward-rate`: dropped "strongly in CA1, weakly in PFC".
  - `fig7b-odor-active-more-fields`: the 65% was computed (the legend prints 66%), so the statement now gives the counts.
- **`fig4d-ccg-lags`.** The paper never says whether its x = -0.028 is a median or a mean. The file had assumed median; both are now named and compared.
- **`fig1c-sampling-duration`.** The code line reference was wrong (65, not 61).

I fetched the paper's code at the cited commit and spot-checked about ten of its citations. Apart from that one line number, they match. I did not re-read the rest.

**Still open**
- **`fig5d-cross-region-beta`:** the paper's p = 1.7e-20 for 9 of 83 cells fits neither chance level (0.0167 or 0.05). This claim will probably block.
- **`fig3s1e-nonselective-si`:** the Results and the legend contradict each other. With both accepted, the claim fails only when p < 0.05 and r is far from -0.34.
- **`fig5c-local-locking`, `fig5gh-phase-preference`:** the interneuron counts differ between the Results (83 CA1, 28 PFC) and the legends (96, 36). Both are reported.
- **`fig6e-glm-choice-prediction`:** the Methods align the time windows to odor onset, while the Results give times before odor-port exit. The two readings may disagree, which would now block the claim.
- **`fig2d-beta-power-increase`:** the checker's false alarm above, recorded as a problem I could not settle.

I found no main finding without a claim, and no claim that draws on anything outside this paper.
