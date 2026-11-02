# Round 3 verifier report: SHIELD reproduction on DANDI:001051 (attempt 001051-bennett-2024-01)

The attempt record has two proposed outcome changes, under `proposed` on `fig7cd-mop-coupling` and `fig8d-response-latencies`. I agree with both. Cell numbers are 0-based indices in the re-executed notebook, which has 110 cells.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig7cd-mop-coupling | blocked (methods_underspecified) | Yes | — | See (1) below. |
| fig8d-response-latencies | blocked (methods_underspecified) | Yes | — | See (2) below. |

**(1) fig7cd-mop-coupling**

- **The numbers come from the data.** Cell 78 builds its table from `PAIRS`, which is the pair test run on the data under each of the claims file's 16 reading combinations. A part is marked `absent` when the pair table has no row for that area (`area_state`, cell 73), meaning the pair had fewer than 25 events and so was not tested.
- **The criterion is not met under any E1 combination.** The criterion's "reproduced" needs MOp–PO to be significant with positive coherence. In all 8 E1 combinations PO is `absent`, and `coherence_part` is False.
- **The E2 combinations meet it.**
  - PO is significant at +0.147 to +0.195 (q from 1.5e-3 down to 5.3e-6).
  - SSp is significant at +0.187 to +0.259.
  - LP is not significant in any of the 16 combinations.
  - The CCGs of PO and SSp peak at 0 to 20 ms with heights 0.199 to 0.329, against 0.029 to 0.062 for LP and VISl.
- **So the readings disagree.** The claims file's header says that when they do, the claim is methods_underspecified. The record's own argument, that "no tested part contradicts the claim", is not the test the criterion sets.
- **The record overstates the E2 count.** The proposal says all 8 E2 combinations give "reproduced". But cell 78's `coherence_part` treats VISl being `absent` as passing (`st["VISl"] != "sig"`), while treating PO being absent as failing. Under L1 E2, VISl is never tested, so "MOp–VISl not significant" is not shown there. Every part is tested and holds only under L2 E2, which is 4 of the 16 combinations (cell 78's final printout). This does not change the outcome; it strengthens the case for blocking.
- **No choice was tuned to the result.** The 25-event minimum, the readings and the Benjamini-Hochberg family are applied the same way here as in fig7cd-visp-coupling.

**(2) fig8d-response-latencies**

- **The numbers come from the data.**
  - Cell 96 builds the population means: unit responses are baseline-subtracted, smoothed, and split into CP-RF and CP-noRF at RF p < 0.01.
  - Cell 99 takes both latency measures in a 0 to 250 ms window, under both unit filters.
  - (a) Time of the population peak: VISp 48 ms, CP-RF 82 ms, CP-noRF 91 ms. The lags are 34 and 9 ms, both outside 20 ± 5 ms.
  - (b) Time the mean first reaches half its peak: VISp 38 ms, CP-RF 54 ms, CP-noRF 74 ms. The lags are 16 and 20 ms, both inside 20 ± 5 ms.
  - The results are identical under the Methods' QC filter and the code's filter.
- **The paper does not pick a measure.** Its only wording is "the response time course of these two populations was different: CP-RF lagged behind VISp responses by ~20 ms, whereas CP-noRF had slower responses" (paper text, lines 900–903). A search of the paper text finds no latency definition: "latenc" occurs only once, as "short-latency" in the optogenetics result.
- **The claims file leaves it open.** It lists readings (a) and (b) without preferring either.
- **The chosen reading was picked to match.** Half-peak was adopted after it was seen to be the reading that matches. The two readings give opposite outcomes, so under the claims file's rule the claim is methods_underspecified, not reproduced on an assumption.

I found no place in either claim's criterion where the claims file misreads the paper.
