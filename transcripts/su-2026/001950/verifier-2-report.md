**Verifier report, round 2: Su et al. 2026 on DANDI:001950 (version 0.260928.2230)**

The claims file has 39 claims. The attempt record has 39 outcomes: 13 reproduced, 10 partially_reproduced, 5 not_reproduced and 11 blocked. I agree with all 39.

### 1. Outcomes and assumptions

**Outcomes I agree with, unchanged since round 1**
- **Blocked (11):** the ten anatomy, transcriptomics and slice claims, and fig6f-cortex-projecting-rpe-biased.
  - The record's reason `other` for the ten anatomy claims, which the claims file marks as data held elsewhere, is acceptable.
  - The record's reason `data_missing` for fig6f-cortex-projecting-rpe-biased is acceptable. My round-1 reason was metadata_insufficient.
- **Reproduced:** figs12-trials-per-session, fig5a-engagement-reward-history, fig5e-switch-history, fig6c-choice-change-rpe, fig4g-go-cue-excitation, fig4h-tonic-phasic-anticorrelation, fig5b-baseline-predicts-ignore, fig6-outcome-responsive-fraction, figs18d-outcome-not-on-anatomy-axes, fig6g-rpe-vs-no-reward-populations, fig6i-axons-rpe, fig6j-cortical-input-more-positive.
- **Partially reproduced:** iti-mean, fig5h-switch-on-anatomy-axes, fig5k-cortical-input-switch, figs17i-baseline-axons-vs-spiking, fig6a-outcome-space, fig6f-outcome-angles-nonuniform, figs14-waveform-space, figs15q-spontaneous-vs-task-licks, figs16-pupil-spiking.
- **Not reproduced:** figs15f-tonic-modulation-vs-engagement, fig5c-ignore-ventral, fig5d-ignore-on-anatomy-axes, fig5g-switch-dorsal, fig6h-opposing-behavior.

**Outcomes I disagreed with in round 1 and now accept**
- **fig4c-choice-history, reproduced.** The criterion requires only R², the fraction predicted, and positive, decaying rewarded coefficients. All three hold (cell 16). The decay constant, 1.39 trials, is reported as failing. That the claims file lists 3.95 as a decay constant "in trials" remains a possible misreading, which I report rather than correct.
- **figs15t-crosscorrelogram-outcome-axis, partially_reproduced.** Under the label-permutation null, neither placement of a pair meets the criterion. Under the within-session null with differences, the main variants show the paper's pattern (cell 99). Calling the outcome-axis part held and the absences dependent on the null is a reasonable judgment.

**Assumptions (13 outcomes are marked `assumed: true`)**
- **The ten that rest on the Q-learning model** (fig6c, fig6-outcome-responsive-fraction, fig6a, figs18d, fig6f-outcome-angles-nonuniform, fig6g, fig6h, fig6i, fig6j, figs15t): the assumption is stated, and it is reasonable now that the recovery check and the pooled-fit variant are in. The worst-case chosen-value recovery is r = 0.190 (cell 66). The record cites only the median, 0.991.
- **fig5d-ignore-on-anatomy-axes:** the population assumption is stated explicitly, and it is reasonable. The 207-unit population that reproduces the claim uses the per-session aN, which is poorly recovered (r = 0.78). The pooled fit, closer to the paper's hierarchical fit, gives 229 units, on which the claim is not reproduced.
- **Marked but not stated:**
  - fig5k-cortical-input-switch: the record does not say what is assumed. Presumably it is the window of the quality threshold, which is given only as a deviation.
  - figs15q-spontaneous-vs-task-licks: no statement either. The outcome holds under every variant (r is 0.58 to 0.62).
  - figs15t: the assumption its outcome actually rests on, the null and the pair placement, sits in the notes, not in a stated "Assumed:" line.
- **Population dependence not marked:**
  - fig6f-outcome-angles-nonuniform: on the 207- and 226-unit populations the unscaled z is within tolerance (cell 102).
  - fig5b-baseline-predicts-ignore: on the draft's units the fraction is 51.3%, outside tolerance (cell 102).
  
  Neither outcome is marked as resting on the population, as fig5d is.

### 2. Sentences the printed numbers do not support

1. **fig5e-switch-history, cell 23 and the record's notes.**
   - Cell 23 says "15 lags 0.677 to 1.983".
   - The record says "15 lags 1.330 (0.677 to 1.983)".
   - Cell 22 prints, for 15 lags, a mean of 1.641, 95% CI 1.458 to 1.823, over 40 mice.
   
   Both texts are stale. The outcome is unaffected.
2. **fig6f-outcome-angles-nonuniform, the record's notes.** The notes read "103 with a negative outcome coefficient (sectors -45 to 0 deg with 87 neurons and 135 to 180 deg with 37)".
   - The angle is arctan2(chosen value, outcome), so −45° to 0° is positive outcome with negative chosen value. Those 87 neurons are in the RPE quadrant, not the negative-outcome half.
   - The negative-outcome sectors are ±135° to 180°, 31 + 37 = 68 neurons, with more beyond ±90° (cell 84).
3. **Run time, entry README and cell 0.** Both say "about 32 minutes, 12 of them streaming the files". The notebook prints loading in 369 s (cell 1) and a total of 24.9 min (cell 105).
4. **Minor: entry README.** It says the notebook "follows the paper's code more closely for the … waveform … analyses". The waveform change applies the Methods' filter; it does not port more of the code.

Everything else in the conclusions, the Summary (cell 104), the README table (13 / 10 / 5 / 11, which matches the record) and the record's notes agrees with the printed outputs.

The attempt record states my round-1 reasons faithfully and in my own words, with my problem numbers attached. Its count of 37 agreements out of 39, with fig4c and figs15t disagreeing, is correct.

### 3. Round-1 points

**Resolved**
- **B1, population:** a sensitivity section was added (cell 102).
- **B2, drift regressor:** the trial-index stand-in is now in the switch and outcome regressions. The real regressor remains absent from the dataset.
- **B3, Q-learning model:** a recovery check and a partially pooled refit were added, and no Q-dependent outcome changes.
- **B4, ITI range:** `ITI_duration` is shown not to hold the generated intervals.
- **B5, figs15t:** every t variant and a within-session null were run.
- **B6, figs15q:** the analysis now follows the code's procedure.
- **B7, figs14:** the band-pass filter and the waveform amplitude check were added.
- **B8, pupil:** the code's fit, detrending and a per-mouse breakdown were added.
- **B9 to B13:** no change was needed.
- **B14, possible misreadings:** both are raised as questions to a reader.

**What remains that bears on a conclusion**
- **fig5d:** the outcome flips between populations. It is stated, but it is fragile.
- **figs15t:** the outcome rests on a null chosen after the result was seen. Under that null:
  - the midpoint placement loses the outcome axis (p = 0.18);
  - one switch variant fails the absence (p = 0.048).
- **fig6f-outcome-angles-nonuniform and fig5b:** their population dependence is not marked as an assumption.
- **fig5k and figs15q:** marked `assumed` with no stated assumption.
- **The four text errors in Section 2,** above all the stale 15-lag CI for fig5e.
- **Pinned files hold no antidromic stimulation events:** this is asserted from an inspection outside the notebook, so I cannot check it from the printed outputs. It supports the fig6f-cortex-projecting-rpe-biased block and the untested halves of fig5k, figs17i and fig6j.
- **iti-mean and fig4c:** the possible claims-file misreadings stay open until a reader answers. If the answers go the other way, these outcomes could change.
