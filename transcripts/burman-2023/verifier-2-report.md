**Verifier report, round 2: Burman et al. 2023 on DANDI:000458**

The claims file has 35 claims and the attempt record has 35 outcomes: 5 reproduced, 5 partially_reproduced and 25 blocked (24 data_missing, 1 methods_underspecified). Below, "main" means `reproduce_burman_2023.ipynb` and "model" means `network_model.ipynb`. Cell numbers are for the re-executed notebooks, so they differ from round 1.

### 1. Outcomes and assumptions

I agree with all 35 outcomes:
- **dataset-sessions-link:** reproduced.
- **fig4c-sample, fig4d-synchrony-lower-awake, fig4d-entropy-higher-awake:** partially_reproduced under A1F1, with the A1F2 exact match recorded as a deviation.
- **fig4-rate-higher-awake and figs6-rate-regressed:** reproduced.
- **fig4f-model-hyperpolarizing-less-activity:** reproduced.
- **fig4h-model-synchrony and fig4h-model-entropy:** partially_reproduced.
- **figs7-model-decoding:** reproduced. This holds even with the corrected statistic in §2a.
- **figs4-intrinsic-properties:** blocked, methods_underspecified.
- **The 24 patch-clamp claims:** blocked, data_missing.

No outcome sets `assumed: true`, so there is no assumption to assess.

One small gap in the claims file. For fig4c-sample, A1F1 keeps 721, which is inside 662 ± 66.2, and excludes 144, which is outside 203 ± 20.3 (main cell 19). The criterion's partial case, "only the total (865) is within 10%", does not literally cover this: the kept count is within tolerance too. Partial is still the sensible reading.

### 2. Sentences the printed numbers do not support

**a. figs7-model-decoding: wrong t and p (bears on how the conclusion is reported, not on the outcome).**
- Model cell 20 says "D1 paired t = 16.42, p = 1.11e-12". Model cell 19 prints `D1 paired t = 16.92, p = 6.52e-13`, and the printed per-run accuracies give t = 16.92 when I recompute it.
- The figs7 notes in the attempt record give the same wrong "t = 16.42, p = 1.11e-12".
- The response to round 1 says the notes were changed to "the printed t = 16.42, p = 1.11e-12". That matches the earlier run, not this one.
- So the accuracies differ between executions. The cross-validation is seeded (`network.py:203`) and the other model numbers repeat exactly. That does not fit the deviation's implication that the seeding makes the run deterministic.
- The outcome does not change: 20 of 20 runs, p ≈ 1e-12 either way.

**b. Start-time deviation claimed where it was not run.** The deviation text on fig4c-sample, fig4-rate-higher-awake and figs6-rate-regressed says timing from start_time "is shown as a variant and keeps the direction".
- The start_time variant is run only for synchrony (main cell 24) and entropy (main cell 28).
- Cell 24 prints only n = 734 for it. No kept or excluded counts, rate test or regression are printed for start_time.

**c. Main cell 37, Summary: clocks overstated.** "their labels and clocks pass the checks above" is too strong. Main cell 8 passes 33 of 34 pairs; sub-569069 awake fails (ratio 1.07, p = 0.591). Main cell 9 and the attempt notes do state this correctly.

**d. Main cell 37, Summary: "means" covers counts.** "with means a little off under the Methods' rate" also covers fig4c-sample. That outcome is about counts, not means: 144 excluded against 203.

**e. README: run times.**
- "about 20 minutes" for the model notebook: model cell 6 prints "20 runs in 40.6 min", and cell 19 prints a total run time of 43.0 min.
- "About two minutes" for the main notebook: cell 4 took 196 s to load, and cell 35 prints 3.5 min.

**f. README: tolerance misses.** "hyperpolarizing means 0.001 to 0.002 outside tolerances" does not match model cells 11 and 14, which give misses of 0.0011 and 0.0024.

Every other sentence checks against the printed outputs: the Result conclusions in main cells 17, 21, 26, 29, 32 and 36 and model cells 11, 14 and 17, the Summary of model cell 21, the other README sentences, and the attempt notes and findings.

**My round-1 reasons in the attempt record:** they are stated faithfully and in substance in my own words. They cover B1, B2, B3, B4, B5 and the section C limits. The one omission, the per-recording minimum of 7 against 1 in fig4c-sample, is immaterial. Points B6 to B9 are not attached to any claim, which is appropriate.

### 3. Round-1 points

**Resolved:**
- **B1 (attempt side).** Main cell 13 runs the gist unmodified: 865 of 865 units match with 0 differing values, it gives 662 kept and 203 excluded, and it reproduces the paper's Figure 4D means. The deviation is recorded and a question for a reader has been added.
- **B2 (attempt side).** Model cells 10 and 13 print the run-to-run standard error (SE) and how many SEs each mean is from the paper's value, and a question for a reader has been added.
- **B3.** blocked_by is now methods_underspecified, and the reasoning is given in main cell 0 and the notes.
- **B4.** p is formatted before rounding in main cells 23, 24 and 31.
- **B5.** The clock check now covers all 17 files, and the one failing pair is named.
- **Section C, gist transcriptions.** The analysis gist (main cell 13) and the simulation gist (model cell 5: 19,093 identical spikes, and 800 of 800 neurons equal) are now checked directly.
- **Section C, learning rate.** It is now printed directly from the compiled synapse code (model cell 6: 0.1 while balancing, 0 during the test).
- **B6 to B9.** No action was needed.

**What remains that bears on a conclusion:**
- **B1, for the claims file.** Should fig4c-sample and the two fig4d claims be judged under the gist's rate? The question is pending with a reader in `questions/burman-2023.yaml`, which I could not see. Until it is answered, the three partial outcomes stand.
- **B2, for the claims file.** Should the fig4h tolerances allow for differences between seeds? This is also pending with a reader. Until it is answered, the two partial model outcomes stand.
- **New: figs7's reported statistic.** Model cell 20 and the attempt notes should give the printed t = 16.92 and p = 6.52e-13. The reason accuracy varies between executions despite the seeded cross-validation should be explained, or the deviation's wording changed. The outcome is not affected.
- **Unchanged: the supplement.** The legends of Figures S4, S6 and S7 are still unavailable. The outcomes of figs6 and figs7 do not depend on them, since every reading agrees; the block on figs4 does.
