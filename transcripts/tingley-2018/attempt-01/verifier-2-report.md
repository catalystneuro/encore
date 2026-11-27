**Round 2 verification: Tingley & Buzsáki 2018 on dandiset 000213 (0.250624.0438)**

The claims file holds 25 claims, and the attempt record gives an outcome for each:

| Outcome | Count |
|---|---|
| Reproduced | 3 |
| Partially reproduced | 8 |
| Not reproduced | 9 |
| Blocked | 5 |

I saved the paper text (PMC6605060) under `paper/`. I also read three source files at the commits the notebook cites: `bz_firingMap1D.m` and `bz_getPlaceFields1D.m` (buzcode e615663), and `scratch_07_11_17_spatialBinnedMaxCorr.m` and `scratch_07_25_17_calc_firingMaps.m` (scratch 2f80453).

### 1. Agreement with the stated outcomes

I agree with 23 of the 25 outcomes as the criteria are written. Several of them carry a caveat.

- **ls-neuron-count, hpc-unit-count, ls-active-neurons, fig2-ls-phase-vs-shuffle, fig2-ls-phase-beats-rate, fig2e, fig2fg, fig1e, fig1g, fig6c, fig6d, figs7, speed-independent, figs6, fig7:** I agree with all of these.
- **fig1i (not reproduced):** I agree, but the result is fragile.
  - The fields test gives KS p = 0.044 over 531 fields, which is 29% of the paper's 1,820.
  - The sessions test gives p = 0.61.
  - The box-map variant gives p = 0.097 (cell 36).
- **ls-few-place-fields and hpc-place-field-properties (partial):** I agree. The hippocampal field fraction is still a third of the paper's.
- **ls-place-fields-unstable (not reproduced):** I agree.
- **fig4d (partial) and fig4e (not reproduced):** I agree, on the condition that the first depth in the session name is the LS depth (problem 6).
- **fig5-assemblies (not reproduced):** I agree as computed. The GLM covariate coding biases the result downward, as described in section 3.
- **ls-information-lower (partial):** I agree. Only the direction of the comparison is meaningful, because the scale is uncertain.
- **fig5g and fig6e (blocked as not_runnable): I accept these with a reservation.** Both could be tested by sampling neurons and running all of their pairs, in place of sampling pairs:
  - 70,898 pair-conditions over 793 LS neurons is about 89 per neuron. At 1.17 s per pair (cell 72), 100 LS neurons take about 3 process-hours.
  - I cannot check whether `not_runnable` is on the protocol's list of reasons.

### 2. Sentences the printed outputs do not support

- **Cell 73, and the fig5-assemblies notes:** "The real gain beats all ten shuffles in 35.4% of the pairs, where 9.1% would without coupling, so hippocampal spikes predict LS spikes beyond the shuffles in many pairs."
  - The 9.1% (1/11) is hard-coded in cell 72; it is not computed.
  - It also assumes the real fit and the shuffles are exchangeable. They are not: the window is chosen to maximise the real fit, and the shuffles run only at that window (`_pair_strength`). The no-coupling rate is therefore above 1/11, and the comparison overstates the evidence.
- **fig1g notes in the attempt record:** "at 3 bins too (+0.006, p = 0.16)". Cell 54 shows that difference is not significant.
- **fig1g deviation:** "Spans of 3 and 4 bins give the same smoothing, as MATLAB smooth reduces even spans by one." That holds for rate only. For phase the cause is circ_smoothTS's 2·ceil(w/2)+1. Spans 5 and 6 are also identical (cell 54).
- **Figures from the first run that this notebook does not print:**
  - ls-place-fields-unstable: "box map … reading (b) gave LS higher (88.7% against 84.6%, p = 3.4e-04)".
  - hpc-place-field-properties: "In the first version … 14.6% and the peak 12.5 Hz". The variant printed now is 0.147 (cell 45).
  - Cells 36 and 37 call the box variant "before revision", but it now gives 318 fields and p = 0.097. The first run gave 315 fields and p = 0.115.
- **README:** "holds 67 sessions of simultaneous hippocampal and lateral septum (LS) recordings". Only 62 sessions hold LS units (cell 18). One file has no hippocampal channel (cell 11), and 19 files have no hippocampal units (cell 63).
- **fig5 deviation:** "the paper may count each pair once". The Methods say "Each neuron pair has a single assembly strength value, determined by all spikes that occur during a single block of trials", which supports counting per condition, as done here.
- **Cell 70 and the figs7 notes:** at 25 units the claim reads "LS phase beats hippocampal phase … one-sided p = 0.0075". This rests on 3 conditions. Cell 69 pools the ensemble draws within a condition as independent samples, so the p values are pseudo-replicated. The conclusion is unaffected because the direction is wrong at 15 and 20 units.

Every other sentence I checked matches the printed outputs, including all the per-rat figures, counts and p values. That covers the "**Result:" cells, the Summary, the README table and the other notes.

**My round-1 reasons are recorded faithfully,** in close to my own words. Some reasons have my numbered problems folded in (for example problems 4 and 5 under fig2-ls-phase-vs-shuffle, and problem 9 under hpc-place-field-properties), and nothing is misstated. Problems 8 and 10 are not attached to any claim, which is reasonable. For fig5, "agrees: true" is right for the outcome (blocked), but I disputed the reason.

### 3. Round-1 points

**Resolved**

1. **Problem 1:** fixed. `rate_map` and `place_fields` now match `bz_firingMap1D` `rateMaps` (FMAToolbox Smooth, tau = round(nBins/50)) and `bz_getPlaceFields1D` (fastrms peak, and the mean < SD exclusion). I checked these against the source.
2. **Problems 2, 3 and 9:** resolved.
3. **Problem 4 for the fig2 claims:** resolved. The theta-ratio > 1 variant changes nothing material.
4. **Problem 5:** resolved. I confirmed `rr = randperm(length(r))` over the pooled trial-by-bin samples in scratch_07_11_17_spatialBinnedMaxCorr.m.
5. **Problem 7:** resolved. It matches the paper's code (`rateMaps_box` with `smooth`, and `circ_smoothTS`).
6. **Problem 8:** resolved. Cell 14 now states the clock check is weak.
7. **Problem 10:** resolved.

**What remains that bears on a conclusion**

- **Hippocampal place-field yield.** Now that the place-field code matches the paper's, the gap of 10.5% against 31.7% of maps (and 22.9% against 49.9% of neurons) is unexplained. It most likely comes from the rebuilt linearization: about one position sample per bin makes the mean < SD rule strict. This affects ls-few-place-fields, hpc-place-field-properties, ls-place-fields-unstable, fig1i, fig1e, fig1g and the hippocampal part of fig2fg. fig1i is the most exposed, because its outcome turns on p = 0.044.
- **Problem 6 (depth assumption) is still unresolved.** fig4d holds with either depth, but fig4e and fig4d both depend on the assumption. For fig4e there is also a confound: in DT9 the theta reference switches to a ca3 channel in exactly the deepest sessions (828–900 µm), and DT5 alternates between hpc and ca3 references. Shifts in the reference phase between sessions can mask, or create, an onset-depth correlation.
- **fig5 GLM covariates.** Position enters `_assemblies` as a single linear term in bin index, and theta phase as a linear angle. Shared spatial tuning is therefore not regressed out. Trial shuffles within a condition keep that shared tuning, which raises the null maximum and lowers the strength, so the 5.2% is biased downward. Coding position as bin indicators or splines would fix this, and so would running the shuffles at every window and taking each shuffle's best.
- **fig5g and fig6e** could be tested on a sample of neurons with all of their pairs, as described in section 1.
