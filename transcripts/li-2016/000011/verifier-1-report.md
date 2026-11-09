**Verifier report: Li et al. 2016 (doi:10.1038/nature17643) on DANDI:000011 v0.220126.1907, round 1**

The claims file has 38 claims, and the notebook's table also lists 38. Cell indices below refer to `reproduce_li_2016.ipynb`.

### A. Outcomes

| claim | my outcome | reason |
|---|---|---|
| unit-classification | partially_reproduced | Cell 22: units 979, sessions 58, fast-spiking 74, pyramidal 890 are all within tolerance. Intermediate units are 15 against 50±5, which fails. The criterion has no partial clause, so a strict reading gives not_reproduced. |
| selective-fraction | not_reproduced | Cell 24: none of the 16 reading combinations has all four counts within tolerance, with lick-early trials dropped (K1) or kept (K2). The sample-epoch count is 132–156 against a floor of 158.4. This is borderline: see B1. |
| fig1d-late-delay-ipsilateral-bias | blocked: data_missing | The condition ending at the go cue is not in the data (cell 11: light onsets are only −2.1, −1.3 and −0.8 s). |
| fig1d-earlier-photoinhibition-minimal | blocked: data_missing | The 5-mouse behaviour sessions are not in the archive. A substitute is possible (see A4 below). |
| ed3-behaviour-recovery-interval | blocked: data_missing | There is no 1.3 s light and no variable delay (cell 11: durations are only 0.5 and 0.8 s; delays are fixed at 1.3 or 1.7 s). |
| ed4-return-to-trajectory | not_reproduced | Cell 29: the time-matched and end-point RMS do not differ under any of the 16 rows (p = 0.30–0.98). The selection gives 47–67 neurons from 4 mice, against 27 from 6. |
| fig1f-spike-rate-recovery | reproduced (fragile) | Cell 31: pooled fraction is 0.101 (K1) and 0.097 (K2) under one reading (pooled, centre label, no exclusion). That reading has n = 248 per condition, against the paper's 168/168/175. The reading that matches the paper's n (172) gives 0.112–0.165, outside tolerance. |
| fig1g-selectivity-recovery | blocked: methods_underspecified | Cells 33–34: the 24 combinations of lick-early handling, preference window, bin label and search end give 12 reproduced, 9 partial and 3 not. Included neurons are 138–173 against 55±5.5. |
| ed5-photoactivation-recovery | blocked: data_missing | No Tlx_PL56-cre × Ai32 subject; I confirmed this on the archive (19 subjects, all VGAT or PV×ReaChR). |
| ed5-photoactivation-rate-changes | blocked: data_missing | Same reason. |
| ed2b-silencing-strength | not_reproduced | Cell 36: VGAT ipsilateral normalised rate is 0.177–0.356 (needs < 0.1) under every reading. PV (0.035–0.052), bilateral and contralateral pass under K1. The 299 neurons match the legend's 300. |
| ed2d-spatial-extent | blocked: data_missing | No untrained or non-behaving recordings: all 91 ecephys files hold task sessions. |
| ed2e-no-rebound | not_reproduced | Cell 38: the mean rate is not higher, but increases outnumber decreases in both windows (n_up 27–31 against n_down 3–10), under K1 and K2. The paper claims the opposite balance. |
| fig2b-unilateral-performance | blocked: data_missing | The 13-mouse behaviour sessions are absent. A partial proxy exists (see A4 below). |
| fig2b-bilateral-performance | blocked: data_missing | Same reason. |
| ed6a-bilateral-inconsistent-bias | reproduced | Cell 40, experiment 2: 12 or 13 sessions significant under either Fisher table. Each sign occurs in 4 mice. |
| fig2-recordings-recovery | partially_reproduced | Cells 45–46: spike rates recover (ratio ≥ 0.9; ipsilateral fraction significant 0.08–0.10), and bilateral selectivity stays low (0.22–0.33). Two parts fail: ipsilateral selectivity at 600 ms is 0.45–0.72 of control, and contralateral reaches 0.15–0.19 of neurons significant. |
| fig2e-selectivity-recovery-times | not_reproduced | Cell 43: fails in all 24 combinations. Ipsilateral selectivity never recovers before the go cue (the paper says 538 ms after offset). Neurons 260–293 against 143. |
| ed7-larger-photoinhibition | blocked: methods_underspecified | Cell 71: 10 combinations reproduced and 14 not, depending on bin label and lick-early handling. Neurons 58–62 against 40±4. |
| ed7e-roc-larger-photoinhibition | not_reproduced | Cell 69: control ROC is 0.680–0.689, below the floor of 0.72. |
| cd-stable-over-epochs | reproduced (marginal) | Cell 50: 0.563 (K1) and 0.588 (K2) against 0.56–0.66. It depends on an author choice: see B5. |
| cd-captures-selectivity | blocked: methods_underspecified | Cell 56: with training trials (v1) the cd values fail in every row (selectivity 73.7–88%). With all correct trials (v2) they pass, but only under the H2/pre-sample/squared reading. Modes 1–5 are never within tolerance. |
| fig3c-cd-recovery-roc | not_reproduced | Cell 52: control 0.649–0.677, ipsilateral 0.63–0.65 and contralateral 0.67–0.70 are outside tolerance; only bilateral (0.558) passes. The partial rule also fails. |
| ed8-roc-during-photoinhibition | not_reproduced | Cell 54: control 0.649–0.685 against 0.72±0.02 in every reading. |
| fig3c-cd-predicts-movement | reproduced | Cell 58: fraction predicted 0.63–0.69, binomial p ≈ 0, Spearman signs correct under every reading. |
| fig3d-persistent-mode | not_reproduced | Cell 60: the mode predicts control trials above chance (fraction 0.59–0.62, p ≈ 0) in all readings. |
| fig3e-ramping-mode | not_reproduced | Cell 60: fraction predicted 0.55–0.58 (p ≈ 0) in all readings. Under the positive-weight-sum orientation with K2, the delay rise is also negative. |
| fig4-bilateral-cd-predicts-movement | reproduced | Cell 58: bilateral trials, fraction 0.59–0.64, p ≈ 0, Spearman signs correct. |
| ed6b-session-bias-predicted | not_reproduced | Cell 62: 13–15 of 24 sessions agree, binomial p = 0.15–0.42. |
| ed9f-reaction-time | blocked: data_missing | Cell 64: the experiment-2 lick traces are flat (median peak above baseline 0.002; detection is the same on correct and no-response trials). The 3 of 20 threshold rows that "hold" in cell 65 rest on 3–10 trials and are noise. |
| ed9c-cd-window-robust | reproduced | Cell 67: both cd windows hold under K1 and K2 for some split size (H2 holds under both). |
| fig5b-callosotomy-control-performance | blocked: data_missing | There are no sessions before the cut; the archive metadata has no surgery annotation. |
| fig5b-callosotomy-unilateral-sensitivity | blocked: metadata_insufficient | Photoinhibition trials in these sessions are unlabelled (cell 19). |
| ed10-callosotomy-preparatory-activity | blocked: metadata_insufficient | Partly testable (see A4 below). |
| fig5-callosotomy-no-recovery | blocked: metadata_insufficient | Needs control and photoinhibition trials told apart. |
| fig5f-callosotomy-cd-reduced | blocked: metadata_insufficient | Same reason. |
| ed1-monolithic-models-fail | reproduced | Cell 73: all 10 networks of each model differ by more than 10% at 2 s (FORCE minimum 0.13). |
| fig6-modular-models-recover | partially_reproduced | Cell 75: the modular integrator fails on lick-left trials (relative difference 0.50) at both step sizes, which follows from the printed matrix with rectified rates. The attractor passes with noise drawn per step (n2). With Euler–Maruyama noise (n1) even the unperturbed attractor is at chance (0.49–0.51). |

**A4. Blocked claims, checked against the archive.** The archive API shows 92 assets, 19 subjects, genotypes VGAT-ChR2-EYFP and PV×ReaChR only, and one behaviour-only file that holds metadata only.
- **Confirmed fully blocked:** fig1d-late, ed3, both ed5 claims, ed2d, fig5b-control.
- **Partly testable, as substitutes on the recording sessions** (40% light trials, a different set of mice from the paper's behaviour cohort):
  - fig1d-earlier: experiment 1, 4 mice. Cell 27 already gives p = 0.16–0.38 for the 0.8 s and 0.3 s conditions, which is consistent with the claim.
  - fig2b: all four protocols are present (experiment 2: one spot left or right, eight spots bilateral; experiment 3: four spots unilateral, two spots bilateral), but in 7 and 3 mice, not 13. Cell 27 shows one-spot left at 70.3% and right at 72.6%, and eight-spot bilateral at 58.0% against the paper's 51.4. Experiment 3 behaviour was never tabulated.
  - ed9f: the experiment-3 lick trace does carry licks (cell 64: session 257636 detects licks on 100% of correct trials). Convention A runs on 6 experiment-3 sessions (cell 69), so a partial test was possible.
  - ed10: the putative pyramidal count, 519 against 496±49.6, is within tolerance, provided these 7 mice are the callosotomy mice (which is inferred, not documented). Sample-epoch selectivity could be counted on all trials. The "any epoch" selective count still needs control trials.

### B. Problems

1. **[affects a conclusion]** selective-fraction, cell 24. The 44 putative pyramidal units of the three unlabelled experiment-1 sessions are dropped, so the analysis tests 846 units, not 890. Cell 25's variant that includes them reproduces under K1 (sample 162–165) and misses under K2 by about 1.5 units (157). That would make the outcome methods_underspecified rather than not_reproduced.
2. **[affects a conclusion]** fig1f, cell 31. The only passing reading (no exclusion, n = 248) contradicts the paper's n of 168–175. The exclusion reading reproduces the paper's n (172) and fails.
3. **[affects a conclusion]** Every convention-D and convention-A claim (cells 29, 33, 43, 48, 71) uses a population far larger than the paper's:
   - ed4: 47–67 neurons against 27.
   - fig1g: 138–173 against 55.
   - fig2e: 260–293 against 143.
   - ed7: 58–62 against 40.
   - activity space: 24 sessions with 6–37 neurons (mean 17), against 16 sessions with 6–20 (mean 11).

   The selection follows the claims file as answered, but these outcomes test a different population from the paper's.
4. **[affects a conclusion]** K2 reading, all cells using `trial_mask(..., "keep")`. Cell 13 shows that in early-lick trials the photostimulus event is logged up to 1.6 s after the light. Windows aligned to the go cue therefore miss the light in those trials, which dilutes the effects (e.g. ed2b under K2: 0.14–0.36). Under the "both K readings must agree" rule this pushes fig1g and ed7 to methods_underspecified. The claims file mandates "events at their logged times", so this is also a claims-file issue; I report it and have not corrected it.
5. **[affects a conclusion]** cd-stable, cell 50 / `activity_session`. Computing w from all correct control trials, rather than the training subset, is the author's own choice. The training subset gives 0.534–0.554 (fail), and counting trials per condition and type (T2) with K1 gives 0.559 (fail).
6. **[affects a conclusion]** cd-captures, `activity_session` (`captured`). Captured selectivity is measured on the same trials used to fit cd (fully in v1, partly in v2), so it is inflated in-sample. This plausibly explains why v1 and v2 disagree.
7. **[affects a conclusion; claims-file issue]** fig1g, convention D search end (E1). With the late-delay offset at −0.3 s, the paper's own 327 ms lies after the go cue, so the search that stops at the go cue (E1) with end-labelled bins returns NaN by construction (cell 33). E1 cannot reproduce the paper's value, yet it is required to agree.
8. **[does not affect a conclusion; claims-file issue]** fig3d/fig3e, cell 60. A per-session mean ROC against 0.5 is insensitive for modes whose sign is arbitrary per session (positive-weight-sum orientation), so the "ROC near 0.5" part passes trivially. The binomial prediction test is the informative one. I checked it is calibrated: an uninformative projection run through the same split and boundary code gives 0.49.
9. **[does not affect a conclusion]** ed9f, `lick_onsets`. The level thresholds 0.10–0.14 sit below the trace baseline (about 0.18), so they can never register an upward crossing.
10. **[does not affect a conclusion]** fig2-recordings (cell 46) and fig6 (cell 75) are labelled "partially" although neither criterion defines a partial outcome.
11. **[does not affect a conclusion]** ed4, cell 29. Centre-labelled windows just after offset include spikes from during the light. ed2b and ed2e (cells 36, 38) use a "≥ 2 trials" rule, which is an author choice. The outcomes hold across these.
12. **[does not affect a conclusion]** Helper functions checked on synthetic inputs: `spike_width_ms`, `counts_in`, `window_counts`/`labels`, `recovery_time`, `decision_boundary` and `auc` all gave the expected values. There is no train/test leakage in the cd projections or the ROC (`held = ~train & ~ipsi_train`). Units are consistent (counts and Hz).

### C. What I could not check, and the output that would have let me
- **Too few intermediate units:** I can't tell whether the shortfall is caused by sampling at 19.5 kHz. A width histogram from upsampled (interpolated) waveforms would show it.
- **Flat experiment-2 lick traces:** I could only see summary detection rates. Raw-trace summaries and example traces for several experiment-2 and experiment-3 trials would show whether those traces are truly flat or the reader misread them.
- **Population sizes 2–3× the paper's:** listing per-neuron trial counts per condition, and selectivity counts per epoch (delay-only selective neurons), would help find the paper's selection.
- **Size of the K2 artefact:** I could not measure it. Counts of early-lick trials per condition, with their light-to-go-cue offsets, would.
- **fig2b proxies:** experiment-3 behaviour per mouse, and a per-mouse test of one-spot performance with the two hemispheres pooled, would complete them.
- **fig3d/fig3e mode orientation:** per-session ROC values for modes 2 and 4 (and |ROC − 0.5|) are not printed.
- **Data loading:** without re-running, I could not verify how trial events and photostimulus records are assigned to trials. I rely on the notebook's clock checks (cells 17–18), which look sound.
