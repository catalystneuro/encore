The claims file is ready for an attempt. I fixed seven claims; nothing was committed or pushed.

**Checker result** (the same before and after my edits): `claims/000140/10.1016-j.neuron.2010.09.015.yaml: 20 claims, 20 quotes, 9 statistical values, 0 problems`

**Changes, by claim**
- **fig4-broad-near-zero:** The test for "no cluster at either end" was joined with "or", so a cluster at one end would still pass. It now uses "and". I also added a check for "most neurons have weakly correlated tuning" (more than half of units with |r| below 0.5). The statement made that claim but the criterion never judged it; the 0.5 cut-off is mine, not the paper's.
- **fig6-perimovement-best-each-dimensionality:** The range k = 1 to 12 does not come from the paper. It now uses the dimensionalities from fig6d's readings: 1 to 14, which the Results give, and 1 to 20.
- **fig6-dimensionality-trend:** The old rule accepted a decline that starts only after k = 14. The paper says performance declined above 10 dimensions, so the rule now requires performance at k = 20 to be lower than at k = 10. It also now says its thresholds are set here, not by the paper.
- **fig6e-summary-rank:** The statement said every other space was significantly worse and that the ranking held at every dimensionality limit. I reworded it to match the paper: the asterisks mark only some spaces as worse (p < 0.001), task spaces were "largely" outperformed, and the advantage grows with dimensionality.
- **prep-dimensionality-7-to-10:** The expected value 8.5 ± 2.5 gave 6 to 11. The protocol's widened range, which the criterion itself states, is 6.3 to 11, so it is now 8.65 ± 2.35.
- **fig7a-shuffled-space-poor:** The rule for judging it is now labelled as set here, not taken from the paper.
- **fig7c-anterior-posterior-performance:** The criterion let the anterior half score lower than the posterior half. The paper says performance was slightly better at anterior sites, so it is now required to be higher.

**Still open**
- The paper names no test behind the Figure 4 p-values or the Figure 6E asterisks. The claims list possible readings.
- The paper gives no significance threshold for the regressions on anterior-posterior location. The claims use p ≥ 0.05, which is a standard choice.
- Many judging thresholds were set by the reader who wrote the file, because the paper states those findings only in words. The main-paper figures aren't available as text, so I couldn't check the thresholds against them.

The paper's main findings each have a claim, and no claim draws on any other paper.
