I checked the claims file for DANDI:000579 and fixed what the paper shows was wrong; the file is ready for an attempt. Nothing was committed or pushed.

**Checker:** `43 claims, 43 quotes, 47 statistical values, 0 problems`. The first run, before my edits, gave 41 claims, 41 quotes, 45 statistical values, 0 problems.

**Changes, by claim** (claim ids unchanged):
- **Opening comment:** the paper does not say how a value for a whole epoch is built from its 36 trial-phase bins. The file had stated a simple mean over bins as if the Methods gave it. It now lists two readings: the simple mean and the mean weighted by frames.
- **fig1d-switch-performance:** the 0.7 bound is now credited to the Methods' definition of a recovered switch.
- **lstm-choice-accuracy:** how accuracy is scored is marked as a standard reading, since the paper does not give it.
- **fig1l-photoinhibition-performance:** the statement said RSC and PPC "do not differ". The paper only reports p = 0.058, so the statement now says that.
- **fig2g-choice-commitment:** the "a tenth of the bias coefficient" test for "near zero" is marked as a bound the file sets; the paper says only "near zero".
- **cue-biased-running-uncorrelated:** the statement had dropped the paper's "and the time course of dynamic choice". It is back in. That part rests on Figure S2G alone, which has no test, so it is reported and not judged.
- **fig3q-cue-decoding:** which of the 11 position bins count is now listed as open, with two readings (the stem bins, or all bins).
- **figs4p-previous-outcome:** the criterion required the effect in every area, which the paper does not claim. It is now judged over all well-fit neurons, with per-area results reported.
- **fig4h-activity-by-epoch:** "RSC was most active in the maze stem" can mean RSC against other areas, or RSC across its own epochs. Both readings are now run. The z-score window is named as a standard reading.
- **fig5e-cue-movement-distributed:** the paper's rule for picking active neurons selects no one for a whole-trial variable such as movement. All well-fit neurons and all neurons are now the readings.
- **fig6b-location-from-profiles:** the measure (share of decoded location falling inside the neuron's own area) is marked as the file's own choice.
- **fig7g-area-decoding-strength-vs-correlation:** the paper does not say what the Wilcoxon test pairs; the 8 held-out mice are marked as the reading.
- **fig8cd-position-specific-decoders:** the measures are now named from the Figure 8C and 8D legends (log likelihood for cue, Spearman correlation for dynamic choice).
- **fig8g-shattering-dimensionality:** "equal" changed to the paper's "nearly identical".
- **Added figs5l-dynamic-choice-over-cue-biased-running** (Figure S5L): part of the main-text finding that dynamic choice encoding is not explained by more complex movement.
- **Added fig6h-embedding-overlap** (Figure 6H): a main finding that had no claim. The bound for "many" (more than a quarter of each area's neurons) is the file's own and marked as such.

**Still open** (recorded in `checks`):
- The linked GLM code lacks the predictor grouping and the analyses. So how the regularization strength is chosen, and when the drift exclusion is applied, each stay as two readings.
- Figure S5N, Figure 3P and Figure S4C have no claim; they are secondary to claims already in the file.
- Figure 1D gives 513 switches and Figure S1B gives 506 for the same sessions. No criterion depends on the count.

**Ready:** yes. The `checks` entry has `ready: true`.
