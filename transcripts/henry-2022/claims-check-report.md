I checked `claims/henry-2022.yaml` against the paper and corrected it. It is ready for an attempt, with three open points recorded below.

**Checker result after the edits:** `claims/henry-2022.yaml: 32 claims, 32 quotes, 30 statistical values, 0 problems`. The first run, before any edits, also reported 0 problems, with 31 claims.

**Changes, by claim:**
- **fig2f-v1-threshold-elevation:** the "variant" form, Φ(x/σ) bounded at 0.5, is the same function as the main form for x ≥ 0, so it was no variant. I removed it and tied the form to the Figure S2 legend: the curves start at 0.5, and threshold elevation scales σ.
- **fig3c-shuffled-threshold-elevation:** the open detail on shuffling was garbled. It now reads: training trials only, against training and test trials.
- **fig4b-v4-modulation-indices:** the statement says "most V4 neurons" are facilitated, but the criterion did not test it. It now requires more than half of V4 neurons to have an index above 1 at the closest spacing.
- **figs4-rf-alignment:** the file allowed up to 5 V4 target-only neurons with no reason. The Figure S4 legend gives n = 0, so the count is now exact.
- **figs5-additive-vs-multiplicative:** the statement says each single form reduces discriminability, which was untested. The criterion now also requires the simulated slopes to be below 1.
- **fig5bc-tuning-model-terms:** added the per-animal fitted counts from Figure S7 for the attempt to report: V1 89 and 57, V4 93 and 105. That is the only split that sums to 146 and 198.
- **fit-quality:** the source was the wrong paragraph (the 7th, not the 6th). It now names the paragraph by its opening words.
- **fig6-well-isolated:** the source paragraph was likewise wrong and is now named by its opening words. I also named as open whether the top third of SNR is taken per area or over all units.
- **fig1b-v4-rf-larger:** the file now says that reading "many-fold" as at least twice is its own reading, not the paper's.
- **New claim, fig5-negative-multiplicative:** the paper reports that negative multiplicative terms occur rarely in V1 and more often in V4 (Results, paragraph 12), and no claim covered this finding. Its test (a Fisher exact test) and its "rarely" threshold (V1 below 10%) are labelled as my readings, since the paper gives neither.

No claim ids were changed. All other claims matched the paper in statement, source, statistics, expected values and method.

**Still open (recorded under `checks`):**
- **fig5de-simulated-discriminability:** the paper calls the simulated loss "similar but slightly stronger" than the measured one and gives no bound. The criterion tests only "stronger"; "similar" and "depended weakly on spacing" are not tested.
- **figs6-common-neuron-pool:** the 0.8 threshold for the fraction of neurons still driven is read off the Figure S6B axis range. The paper never states it.
- **fig2c-v4-worse-all-spacings:** reproduction requires the two 95% CIs not to overlap at every spacing. The paper names no test, so this stricter reading is the file's choice.

The check entry has date 2026-11-10, `kind: agent`, `ready: true`, and 13 lines under `changes`. The file parses as YAML. Nothing is committed or pushed.
