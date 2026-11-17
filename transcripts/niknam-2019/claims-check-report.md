I checked `claims/niknam-2019.yaml` against the paper and made six corrections. It is ready for an attempt, though four problems stay open (listed below). Nothing is committed.

**Checker:** `claims/niknam-2019.yaml: 34 claims, 33 quotes, 28 statistical values, 0 problems` (the same before and after my edits).

**Verified, unchanged:** every quoted number, standard error used as a tolerance, p-value and neuron count matches the Results, Methods and legends. The percentage changes in fig5c-percent-changes follow from the slopes by the Methods' formulas, up to rounding. I cloned the code repository at commit 1438dde and confirmed the settings the opening comment takes from it: the time and delay ranges, the condition-wise 35/35/30 split, the 1.5 SD selection threshold, r_max = 1000, the F-model bounds and smoothing, and how the null model and pooling work.

**Changes, by claim:**
- **fig1c-ff-remapping:** I removed "at a longer latency than the RF response" and the word "late" from the statement. The quoted sentence says neither, and its criterion doesn't test latency; fig1-remapping-longer-latency already covers that.
- **O1, the shared note on how the signed-rank test pairs counts** (it affects the fig1, fig5b and fig6 claims): reading (c), an unpaired rank-sum test, is not the test the Methods name for recorded responses. It is now a variant that is shown but cannot decide an outcome.
- **fig5a-n-model-no-perisaccadic-gain:** the criterion called the paper's test two-sided, but the paper doesn't say. It now says sidedness isn't stated, uses two-sided as a standard choice, and shows the one-sided p.
- **fig5c-f-higher-ratio-than-s:** the same sidedness fix. I also noted that the paper doesn't say how neurons with zero or negative fixation performance enter the per-neuron ratio, so the test is shown with and without them.
- **fig8c-example-neuron-detectability:** limiting the search for the example neuron to neurons with both remapping effects is not in the paper. It is now marked as an assumption, and all 41 neurons are searched as a reported variant.
- **fig8e-population-ff-detectability** (fig8e-population-st-detectability follows it): aligning each neuron's Gaussian centres to its FF probe before averaging is not in the Methods. It is now marked as an assumption.

**Still open** (each recorded in the `checks` entry):
- **fig1-remapping-longer-latency:** the paper names no measure, so the claim uses peak latency of the population curve. The 50-75 and 80-150 ms ranges in the paper may just be the analysis windows from Methods.
- **No claim for one finding:** the paper says the F-model "performs as well as the S-model" for Fig 5B but reports no test of F against S.
- **N-model claims:** these rely on ref [48], which the text doesn't list. They are blocked if the attempt can't identify it.
- **Example neurons:** the paper doesn't identify which neurons are the examples in Figs 1, 6 and 8, so those claims search all neurons and are weak tests.

**Ready:** yes. The check entry is appended under `checks` with `ready: true`.
