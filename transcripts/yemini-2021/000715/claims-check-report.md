I checked the claims file against the paper and made five corrections. It is ready for an attempt. Nothing was committed or pushed.

**Checker result (after my edits):** `claims/000715/10.1016-j.cell.2020.12.012.yaml: 32 claims, 32 quotes, 5 statistical values, 0 problems`. Before the edits it was the same except for 7 statistical values.

**Changes, by claim**
- **ms1-calibration:** The 10-percentage-point bound had been justified as "the protocol's default tolerance". The protocol's default is 10% of a reported value, not 10 points, so it is now named as a standard choice that does not come from the paper. The criterion had required both readings to hold; it now follows the protocol's rule: if the two readings agree, that decides the claim, and if they disagree it is blocked as methods_underspecified. The class-level scoring of left/right pairs is now cited to footnote 1 of Methods S1 section 6.4, where the footnote actually sits, not to the Figure 6.8 legend.
- **ms2-neuropal-color-violations:** The file said the paper does not state whether head and tail are pooled. Methods S2 section 4.2 runs the solver on the 235 head and tail neurons together, and Methods S2 Figure 1A gives a single value for both. Pooled is now the main reading, with head and tail apart as variants.
- **fig7de-optimal-coloring-violations:** Added the source for "3 colors at 3 intensities" in both solutions (the Figure 7 legend and the Methods S2 Figure 1 panel labels).
- **fig6ef-nacl-novel-interneurons** and **tables6-tail-pvq-and-post-stimulus:** I removed the statistics entries. In both, the q ≤ 0.05 test decides which neurons count as responding, so it is a threshold for counting units, not a result. The test is now described in each criterion.

All other quotes, statements, sources, expected values and tolerances match the paper. Every main finding has a claim, and all claims come from this paper.

**Still open**
- The three remaining statistics entries (fig5ab, fig5efg, fig6d-ase) record the paper's significance standard, "p or q ≤ 0.05". They are written as `p 0.05` with `"<"` because the schema has no "≤" option. The actual p-values are in Tables S5 and S6, which are not in the text read.
- **fig2cd-variability-differs:** The paper gives no test. The pass rule, a factor of two between the most and least variable neuron, comes from the OLLR/OLLL example in the Figure 2C legend. It is a reading of the paper, and it will be passed easily.
- **ms1-calibration** and **ms1-uncertain-first-faster:** The paper says "largely in good agreement" and "much faster" without giving any measure. The readings used to judge them are named in the criteria, but they are not the paper's own.

All of this is recorded in a `checks` entry at the end of the file, with `ready: true`.
