**Round 2 verification: Peterson et al. 2021 on DANDI:000055**

**1. Outcomes and assumptions**

The claims file has 25 claims and the attempt record has 25 outcomes, one per claim. I agree with all 25:

- 15 reproduced: subject-days, roi-projection-link, fig2-features-differ-across-subjects, fig2-bimanual-skew, extfig2-1c-contralateral-larger, fig3-group-lfb-decrease-hfb-increase, fig3-sensorimotor-largest, fig4-precentral-subject-variability, fig5-band-power-differs-across-subjects, fig5-recording-day-effects, extfig5-1-baseline-reduces-day-variability, discussion-day-changes-small, fig6-r2-at-most-025, fig6b-best-models-sensorimotor, fig6c-angle-and-day-most-informative.
- Also reproduced: fig6d-upward-reaches-enhance-pattern and fig6d-angle-and-day-largest-coefficients (17 in all).
- 6 partially reproduced: cohort, fig2-reach-shape, extfig2-2-feature-correlations, fig2-days-and-waking, table1-subject-band-power-ci, extfig6-2-angle-most-retained.
- 1 not reproduced: fig2-event-counts.
- 1 blocked as methods_underspecified: fig3-lfb-more-widespread.

The six regression outcomes now rest on outputs (cells 88–106) and each matches its criterion:
- **fig6-r2-at-most-025:** largest R2 is 0.189, against a limit of 0.275.
- **fig6b-best-models-sensorimotor:** in LFB, 22 of 22 electrodes with R2 > 0.05 are in the five frontoparietal regions. In HFB it is 13 of 14. The projected top three are all frontoparietal.
- **fig6c-angle-and-day-most-informative:** angle and day have the two largest median Delta R2 in LFB under every variant.
- **extfig6-2-angle-most-retained:** the angle part holds; the order of the next four fails under both readings.
- **fig6d-upward-reaches-enhance-pattern:** median angle coefficient is −1.027 in LFB and +0.535 in HFB.
- **fig6d-angle-and-day-largest-coefficients:** angle and the day SD are the two largest under both readings in both bands.

Eleven outcomes are marked `assumed: true`: fig3-group, fig3-sensorimotor, fig4, extfig5-1, discussion-day-changes-small and the six regression claims. Each assumption is stated in the deviations and is reasonable:
- the reading of the bad-segment rule, which cell 107 shows changes no outcome;
- the fig4 tie-break, with the strict reading (partial) recorded;
- the microvolt unit;
- the batched Huber fit, which agrees with sklearn to 4.4e-05 in R2 (cell 87);
- refits only where R2 > 0.05, the only electrodes the criteria use.

I checked `huber_fit`, `forward_select`, `day_balanced_splits` and `electrode_model` against sklearn's Huber objective and statsmodels' rank-based adjusted R2, and found no error.

Two small points, neither of which changes an outcome:
- The day and time-of-day coefficient is taken as the mean over splits of the per-split SD (`coef_all[:, ci].std(1).mean()`), not the SD of the split-averaged coefficients. The record does not state this. It can only raise the day value a little, and the margins are large (day 0.660 against the next feature at 0.188 in LFB).
- Every ECoG outcome, not only the regressions, includes the false-positive events the files do not mark. This is stated under fig2-event-counts and fig6, not under fig3 or fig5.

**2. Sentences against printed outputs**

Every number in the Result cells, the Summary, the README and the record notes matches the outputs. I found no sentence the numbers contradict. Two small points:
- Cell 59 says "Middle frontal and supramarginal show the same pattern". Cell 57 also lists middle temporal, with −0.005 and +0.003 dB. Supramarginal's high-frequency value at the onset bin is 0.000, so the pattern holds there only over 0 to 0.5 s. The record says so; cell 59 does not.
- Cell 0 (not a conclusion) says the ECoG step takes "about 22 minutes". Cell 19 prints 19.8 min.

The record's 17.8% false-positive figure is in the paper (Methods), and 6931 events and 8 male / 4 female are in the data descriptor, as stated. I could not check the reference to `questions/000055.yaml`.

The record's round-1 entries give my reasons faithfully, in close paraphrase:
- the agreement count of 19 is correct (25 minus the 6 regression claims);
- B6 is merged into cohort, and B7–B9 into fig3-group;
- B2 is kept as a criterion problem, reported and not corrected.

**3. Round-1 points**

- **B1 (regressions not run): resolved.** All six were run with all their variants, in 2.2 min.
- **B2 (KDE boundary bias): resolved as a sensitivity check.** A boundary-reflected KDE puts the peaks within 15° of ±90 in 6 of 12 subjects, not more than half, so the partial outcome holds under either KDE. The bias remains in the criterion and is reported there.
- **B3 (false positives not marked): resolved as far as the data allow.** Cell 6 shows the same nine columns in all 55 files and no false-positive mark. The notes now qualify the outcome.
- **B4 (one bootstrap seed): resolved.** Under ten seeds the readings give 7 against 7 regions and 35.0–35.6 against 25.5–25.8 bins per frequency every time (cell 65).
- **B5 (fig4 tie-break): resolved by disclosure.** The outcome is marked assumed and the strict reading is recorded as partial.
- **B6 (depth classification): resolved.** Cell 7 lists the groups and cell 31 gives the descriptor's counts. The "five" fails either way.
- **B7 (bad electrodes from the first file):** the record now cites tfr_utils.py. I cannot check the code, and no conclusion depends on it.
- **B8 and B9:** unchanged; neither affects a conclusion.

What remains that bears on a conclusion:

1. **fig6b-d: the attempt's per-electrode R2 matches the paper's only moderately.** The R2 values stored in the files are the paper's own. Their Spearman correlation with the attempt's R2 is 0.718 in LFB and 0.643 in HFB, and the HFB maximum is 0.189 here against 0.255 stored (cell 90). Claims fig6b, fig6c and both fig6d claims rest on small sets above R2 0.05: 22 LFB electrodes from 4 subjects (11 from S01) and 14 HFB electrodes from 6 subjects. The notebook does not show how far these sets overlap the paper's. Two outputs would settle it: the overlap with the stored R2 > 0.05 sets, and the fig6b-d criteria applied to electrodes selected by the stored R2. The outcomes stand on present evidence.
2. **fig2-event-counts** is judged on reading a in full, and on reading b without its false-positive step, which the files make impossible. This is a data limitation and is disclosed.
3. **fig4 part 4** depends on the tie-break. Under the strict bin-count reading the claim would be partially reproduced; this is disclosed.
4. **fig2-reach-shape's angle criterion** has a KDE without boundary correction. This is in the claims file, reported and not corrected. The sensitivity check shows the outcome does not depend on it.
