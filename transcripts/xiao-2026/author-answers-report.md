The reader's answer has been applied to the attempt. The notebook ran end to end from a clean environment in 29 minutes, and `entry.py check` reports no errors. I built the handover in `executed/001687-xiao-2026/handover/`. Nothing is committed or pushed.

## The question

There was one question, filed on `fig2-wall-responsive-counts`. It asked whether the main test for deciding that a unit responds to the wall should be the one corrected across the nine distances (BH-FDR). The claims file had made the Methods' uncorrected p < 0.05 the main test.

The reader changed the claims file. The Methods' "p < 0.05" does not rule out a correction, and the paper's code (Fig2DEF_Pop_Heatmap_Hist_Pie.m) applies BH-FDR, so the code settles the point. The claims file now makes the corrected test the main reading and the uncorrected test the variant. This applies to every claim that uses this classification of units. The expected values did not change.

## What I changed

- **Notebook:** the corrected test is now labelled as the main reading and the uncorrected test as the variant, and every conclusion is judged on the corrected test. The computation order is unchanged, so every number from the earlier run comes out the same.
- **Two analyses added:**
  - the linear-decoder claim (`figs5de-svm-robust`) is now also run with 10-fold cross-validation under the corrected classification;
  - the 15-split accuracy and error tables per distance are now printed.
- **Helper module (`prv.py`):** docstrings updated to match.
- **Notebook header:** a stale row still listed `figs4j-ventral-location` as blocked; it is tested, and the row now says so.
- **`entry.yaml`:** runtime raised from 25 to 30 minutes.
- **Attempt record:** each affected claim's notes say what the answer changed. The `measured` values now come from the corrected test.
- **Findings:** the finding that said the Methods and the code disagree is now kind `other`. It now says the Methods do not state whether the test is corrected.

## Outcomes per affected claim (earlier outcome in brackets)

| claim | now | before |
|---|---|---|
| fig2-wall-responsive-counts | reproduced (782, 541, 337, 96) | not_reproduced |
| fig2-distance-tuned-counts | partially_reproduced (600, 478, 214 within tolerance; 92 "both" against 29 ± 2.9) | not_reproduced |
| fig2f-tuning-categories | reproduced (271, 120, 87, 122, 182) | not_reproduced |
| figs4a-baseline-activated-lower | reproduced | reproduced |
| figs4a-baseline-suppressed-similar | reproduced (p = 0.643) | reproduced |
| figs4b-activated-increase-suppressed-decrease | partially_reproduced (activated baseline 5.36 or 5.40, outside 6.36 ± 0.704) | partially_reproduced |
| figs4c-untuned-no-change | reproduced | reproduced |
| fig2de-preferred-distances-span | reproduced | reproduced |
| figs4ef-crossvalidated-stability | partially_reproduced (the correlation reading fails, 0.815 against 0.831) | reproduced |
| figs4j-ventral-location | reproduced | reproduced |
| figs4l-temporal-windows-map | partially_reproduced (sustained and onset counts now within tolerance; offset 68 or 42 against 34) | partially_reproduced |
| fig3a-decoding-above-controls | reproduced | reproduced |
| fig3-overall-decoding-accuracy | reproduced (now matches under 10-fold, 3 to 11 s) | reproduced |
| fig3c-decoding-by-distance | partially_reproduced (now fails at 9 mm, where proximity 79.4 is below map 81.5; proximity at 15 mm 32.0 is out of tolerance) | partially_reproduced (for a different reason before) |
| fig3c-decoding-error | reproduced (0.737, 0.830, 0.894, 1.822 mm) | partially_reproduced |
| figs5c-single-neuron-decoders | reproduced (q = 0.0158 at 7 mm; all four values within tolerance) | partially_reproduced |
| figs5de-svm-robust | partially_reproduced (combined group 61.87 is above 54.43 ± 5.44) | partially_reproduced |
| fig4-cut-baseline-unchanged, fig4b-cut-wall-firing-reduced, fig4b-cut-per-unit-changes | blocked, metadata_insufficient; the notes now report the corrected-test unit sets (283 and 175 units) | blocked |
| figs2-tungsten-responsiveness, figs2-tungsten-tuning, telc-unit-yield | blocked, data_missing; the criterion changed but the data are not in the dandiset | blocked |

Three judgement calls need the verifier's attention, because their criteria have no partial rule:

- **`fig2-distance-tuned-counts`:** three of four counts hold, so I recorded it as partially reproduced instead of not reproduced.
- **`figs4ef-crossvalidated-stability`:** one of the two readings fails, so I recorded it as partially reproduced. The two correlation values overlap widely across the 100 splits.
- **`figs5de-svm-robust`:** the ranking holds and one of four values is out of tolerance; I recorded it as partially reproduced, as in the earlier run.
