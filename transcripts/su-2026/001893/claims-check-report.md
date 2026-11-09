I checked the claims file for 001893 and it is ready for an attempt.

**Checker:** `claims/001893/10.1038-s41586-026-11026-0.yaml: 29 claims, 29 quotes, 29 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim**
- **Sources (18 claims):** most paragraph numbers were wrong. The stored text has no paragraph breaks, so I counted paragraphs in the publisher's web page for the paper.
  - The six Patch-seq claims (`patchseq-sample`, `patchseq-ne-identity`, both `patchseq-ap-waveform-*`, both `patchseq-tau-*`) move from paragraph 3 to paragraph 5.
  - `extracellular-waveform-spatial` 3→4, `behaviour-history-dependence` 2→3, `go-cue-response` 4→6, `ventral-respond-ignore` 5→7, `dorsal-switch-stay` 6→8, `cortex-input-switch` 7→9.
  - `mapseq-consistent` 4→5; `dorsal-ventral-projection-targets` and `retrograde-dorsal-cortex-ventral-spinal` 5→6.
  - `outcome-responses-spatial` paragraphs 1 and 3 → 1 and 2; `outcome-coefficients-cluster` 3→2; `frontal-axons-rpe` 4→3.
- **Both `patchseq-ap-waveform-*` claims:** the Methods give a rule for which sweeps to include, and the paper's code does not apply it. The protocol says to follow the Methods when the two disagree, so the Methods' rule is now the main reading and the code's (no sweep rule) is the variant. Both are still run. I cloned LCNE-patchseq-figures at 79fa20a and the code matches the criterion as written: how the sweep is chosen, the -10 mV spike detection, the -5 to 10 ms average, the normalisation, PC1 and the Welch test. Time constants are missing for 14 of 96 cells, as the file says.
- **`snrnaseq-single-cluster`:** I removed "with a large drop from 1 to 2" from the criterion. The paper does not say this; the Methods say only that the silhouette score was always highest with a single cluster.
- **`axon-density`:** the criterion's "level-2 CCF regions" does not come from the paper for axon density. The set of regions is now marked open, with two readings named.

Everything else checks out against the text: statements, statistics (no counting thresholds were recorded as results), expected values and tolerances, and the other Methods details (for example k = 50 for imputing pseudospace onto the MERFISH cells, the kNN settings, and the 0.75 s, 2 s and 0.5 s windows). The paper's main findings each have a claim, and every claim comes from this paper.

**Open:** for `dorsal-ventral-projection-targets`, `retrograde-dorsal-cortex-ventral-spinal` and `mapseq-consistent`, the paper reports no test, so the criteria's comparisons of medians or shares are not taken from it. None of these three can be tested on this dataset, so I left them as written and recorded this under `checks`.

**Ready:** yes (`ready: true`). Nothing was committed or pushed.
