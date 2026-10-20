There was one question, and its answer changed the text of six claims but none of their outcomes. That's because this attempt had already run all three readings the answer names. `tools/entry.py lock` and `all` pass (0 check errors, notebook runs in 251 s), and the handover is built in `executed/crcns-ret-1-lefebvre-2008/handover/`. Nothing is committed, and I did not verify my own work.

## The question and its answer

**Question (fig9d-rf-size-similar, also fig9e, fig9f, fig9g, fig9h and s3):** which flickering-bar recording of a retina gives a cell's spike-triggered average, its firing rate and its model fit? The claims file named the bar widths (8.3 or 16.6 um) but not their orientation, nor what to do when a retina has more than one such recording.

**Answer:** the paper does not say. The claims file now names three readings in the fig9d criterion:
- **A:** the first vertical-bar recording.
- **B:** all vertical-bar recordings pooled, with spikes and frames together. For the firing rate, B uses the pooled spike count and the pooled duration.
- **C:** the horizontal-bar recording where the retina has one, otherwise as A.

Each of the six claims must now be judged under all three readings.

**What it changed:** the first run had used exactly these readings, and computed the rate under B from the pooled count and duration. So the re-run gives the same numbers. The changes are to wording only:
- **Attempt record:** each of the six claims' notes says what the answer changed, and the deviation that said "the bar recording is not fixed by the claims file" is gone.
- **Notebook:** the header, the Measures section and the criterion text for s3, fig9f and fig9h now cite the readings as the claims file's, not as this attempt's own choice. The summary's line on how the analysis differs from the paper is updated to match.
- **Helper:** the docstring of `bar_recordings` in `ret1.py` says the same.

## Outcome per affected claim

| Claim | Before | Now |
|---|---|---|
| fig9d-rf-size-similar | not reproduced | not reproduced (bands separate in 18 of 18 combinations; mutant centres smaller, 116 against 156 um under A) |
| s3-receptive-field-surrounds | reproduced (by the criterion; noise also meets it) | reproduced (12 of 12; null STAs meet the rule in 194 to 198 of 200 mutant units, so it is still no evidence) |
| fig9e-slower-time-course | reproduced | reproduced (36 of 36 separate with the mutant curve at longer times; in 8 of them the bands also separate the other way, the deviation already recorded) |
| fig9f-lower-firing-rate | reproduced | reproduced (9 of 9; median rate ratio 0.42 under A, 0.45 under B, 0.38 under C) |
| fig9g-threshold-unaltered | not reproduced | not reproduced (36 of 36 separate, mutant thresholds higher) |
| fig9h-gain-reduced | blocked, methods_underspecified | blocked, methods_underspecified (printed form: 18 of 18 separate with lower mutant gains; continuous form: 14 of 18 overlap) |

The entry's README needed no change, since no outcome moved.
