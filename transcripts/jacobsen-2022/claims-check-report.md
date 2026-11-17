I checked the claims file against the paper, made seven changes, and marked it ready for an attempt (`ready: true`).

**Checker result:** `claims/jacobsen-2022.yaml: 28 claims, 25 quotes, 4 statistical values, 2 problems`. Every quote matches. The two problems are the p-values 0.0036 and 0.0317, which are in the Figure S2A legend. That legend is an image, so it is missing from the text. I read it in the PDF and both values are right, as are r = 0.54, n = 27, and the 5 and 4 animals.

I also checked these against the PDF and found them correct: the "Conclusive (days 26-30)" axis label, the pie-chart percentages in Figures 3B, 3D, 4B and 4C, and every value printed in Figures 5C, S3B and S4. Every count taken from Table S1 matches the table, including the starter-cell spread 4/5/2/2/2/16 and the input totals 7, 26, 35, 34 and 4.

**Changes, by claim:**
- **fig2a-four-or-fewer-starters:**
  - The expected value is now the paper's printed 48%. It was 48.4, which the writer had worked out from 15 of 31.
  - The criterion now says the 31 animals in Table S1 are what remains after the exclusions in the Methods.
  - It also notes that the 15 "conclusive" animals include the 4 with zero starter cells. The Methods' definition of "inconclusive" would not count those as conclusive.
- **Opening comment, fig5c-responsive-grid-cell, figs4-nonresponsive-cells, responsive-cells-at-19-days, mec-inputs-from-two-weeks:** I removed the second way of deciding whether a cell responds to the laser (reading R-b). It compared spikes before and after each pulse with a paired test, which the paper never does. The author can still show it as a variant, but it no longer decides any claim.
- **fig5c-example-cells:** If a unit is picked because its firing rate is closest to the printed one, it is now judged on latency and fidelity only. Scoring it on the rate used to pick it would be circular.
- **figs3-stable-input-cell:** The rule "15 of 18 values within tolerance" did not come from the paper. Full reproduction now needs all 18 values.
- **figs1b-sparse-cre:** Labelling along the injection track is left out, because the Figure S1B legend marks the track with arrows.
- **New claim, population-targeting-mec-labelling:** A main finding had no claim. Using more virus, the authors targeted whole populations of hippocampal cells, and this labelled many input cells in the superficial MEC (Figures 5B, 6A, S1A and S3A).

**Still open (recorded under `checks`):**
- **Laser responsiveness:** The paper gives no threshold. The one remaining rule (R-a) takes its cutoff from the lowest fidelity among the Figure 5C examples, 11.64%. The paper makes no comparison with chance, so a fast-firing cell could pass by accident.
- **Cell types:** Grid, head direction and border cells are defined by the scores and thresholds in Rowland et al. (2018), which the Methods cite. Neither the first reader nor I have read that paper.

The file is not committed.
