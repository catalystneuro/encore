**Round 2 verifier report: lesica-2007-01 (doi:10.1016/j.neuron.2007.07.013, DANDI:002028 version 0.261102.1631)**

The claims file has 38 claims. The attempt record gives 38 outcomes: 16 reproduced, 7 partially reproduced, 15 not reproduced and none blocked. Nine outcomes carry `assumed: true`. The README and the Summary (cell 109) give the same counts and flags.

## 1. Outcomes and assumptions

**I agree with these outcomes, and their assumptions are stated and reasonable:**
- sample-composition. It fails under all three penalties: 111, 29 and 0 cells, against 68.
- firing-rate-contrast and firing-rate-lc-ns-wn-similar (assumes reading P2a).
- ln-prediction-accuracy and fig3b-spatial-width-contrast.
- fig3c-surround-contrast. White noise fails under both penalties.
- fig3d-temporal-width-correlations and figs1-property-correlations.
- fig4b-gain-contrast and fig4b-gain-correlations. The second is marked assumed because the gain change flips sign at 1000× variance.
- fig4c-offset-contrast, and fig4c-offset-correlations-none (assumes the per-animal adjustment is applied within the set compared, which is the natural reading of P5).
- fig4d-normalized-offset-contrast and fig4d-normalized-offset-correlations.
- fig6a and fig6b (all four claims), fig7c, fig8-model-sparseness-shuffle and fig8b.
- Both disc claims.
- methods-latency-biphasic (assumes the 128 Hz RFs and the p < 0.05 reading).
- methods-offset-varies-across-animals and the four celltype claims.

**I disagree with these outcomes:**
- **fig3b-spatial-width-correlations and fig3c-surround-correlations (reproduced, assumed).** I don't think the assumption is reasonable.
  - In round 1, my synthetic check gave a narrower RF centre and a weaker surround for noise than for the movie under this penalty, even when the true RF was the same for both. So the estimator produces this effect with no real difference behind it.
  - The new variant agrees. At 1000× variance the effects are 5.1% (p = 0.11) and 2.7% (p = 0.67) (cell 107).
  - The selection rule does not separate the two penalties. Held-out r is 0.420, 0.434 and 0.437 at 1000×, 3000× and 10000× (cell 9), on only 8 cases from 4 units.
  - I would record both as not reproduced, or at least not as reproduced.
- **fig3d-temporal-width-contrast (partially reproduced).** The criterion defines "partial" as "the tests hold and the sizes do not". Here the white-noise test fails (p = 0.011 against p < 0.001, cell 37), so by the criterion this is not reproduced. The record says it departs from the criterion.
- **surround-temporal-correlation (partially reproduced).** The criterion has no partial outcome.
  - The main reading pairs the frame-rate surround with the 128 Hz width and gives r = −0.366, outside the tolerance of −0.55 to −0.45.
  - Taking both measures from the 128 Hz RF gives −0.466 and −0.480, inside the tolerance (cell 42). This is closer to the paper, which takes both from the same RF.
  - The record should adopt one reading as the stated assumption. That gives reproduced (both 128 Hz) or not reproduced (main), not partially reproduced.

**Outcomes I accept under the criterion, but which rest on assumptions that are not marked:**
- **methods-spherical-asymmetry (not reproduced).** The strict "every point" criterion fails.
  - Two movie simulations also differ from each other at 1 to 3 points, so the criterion is barely attainable even when nothing differs.
  - The "beyond chance" conclusion rests on the chosen penalty. The penalty is fixed relative to stimulus variance, but the movie estimate uses 14,203 to 19,589 frames and the noise estimate about 54,000 (cell 104). The movie estimate is therefore regularized about 3 to 4 times more heavily relative to its data, which confounds the comparison.
  - It should be marked `assumed: true`.
- **fig5-within-trial-contrast (not reproduced).**
  - Contrast reading (a) runs from 0 to 1.24–2.46, nowhere near the paper's 0.27–0.43. Its thirds are therefore sorted largely by mean luminance and clipping.
  - Reading (b) separates the thirds only between 0.35 and 0.38.
  - Each third's RF uses the full-data penalty on one third of the frames.
  - The result that the top third never has the lower gain (0 of 24) may come from these choices. It should be marked assumed.
- **fig7d against fig8a, fig8b and fig8de.** The criteria allow "one reading" per claim, but the passing readings are opposite.
  - fig7d passes only with the 12 s clips (cell 79).
  - fig8a, fig8b and fig8de pass only with the long segments (cells 81, 85, 87).
  - No single stimulus reading passes all four. fig7d and fig8de should be marked assumed, and the record should state this.
- **fig8de is now reproduced, and I agree** under stimulus reading (a), with all five seeds (cell 87).

**Claims-file reading.** The header says the monitor's 120 Hz refresh, updated every other refresh, gives "50 Hz frames". That is 60 Hz, and the files show 59.96 Hz. This affects no criterion.

## 2. Checking text against outputs

I checked every "**Result:" cell from 19 to 108, the Summary in cell 109, the README and the notes and responses in the attempt record against the printed outputs. I found no sentence that the numbers contradict. Spot checks that hold:
- Tolerance bounds such as 30.6–37.4, 48.6–59.4, 133–163, 0.774–0.946 and 3.65–4.47.
- Cell 108's variant figures: 5.1% at p = 0.11, 2.7% at p = 0.67, 17.5%, p = 0.30, p = 0.31 to 0.91, 149.8% and 126.2%.
- The fig5 counts (5 of 24; directions 0/10/0/15 and 8/4/0/22) and the spherical-asymmetry ranges (32–66, 357–422, 1–3 and 68–113).

The README counts and the Summary flags match the record.

The record's verification section states my round-1 reasons essentially in my words. One small point: those reasons cite round-1 cell indices (for example "cell 19" and "cell 54"), which no longer point to the right cells in the current notebook.

## 3. Round-1 points

**Resolved:**
- **Problem 2:** the offset is now adjusted evenly; the uneven version is kept as a variant.
- **Problem 3:** RFs at 128 Hz with 24 lags of 8 ms are now used. One deviation remains: a 15×15 window in place of 21×21.
- **Problem 4:** the fig8de scan now runs under both stimulus readings.
- **Problem 5:** the units whose RFs change sign are counted (13 of 111), and variants leave them out where it matters. No included unit has an outlying 128 Hz latency.
- **Problem 7:** the docstring is fixed. Problems 6, 8 and 9 needed no change.
- **Could-not-check items:** cell 3 now inventories the trials (600 s HC and 901 s LC noise are used; a12 and b12 hold only the 100 s test), and both previously blocked claims were tested.

**Partly resolved:**
- **Problem 1, the penalty.** The variants are now run, the dependence is documented and four outcomes are flagged. But the main penalty is still 1.9 times the mean eigenvalue of X'X.

**Still open, and bearing on a conclusion:**
1. Under the chosen penalty, fig3b-spatial-width-correlations and fig3c-surround-correlations are explained by estimator bias, so they should not be recorded as reproduced (section 1).
2. The penalty dependence is untested or unflagged in several places:
   - The 128 Hz RFs use the same penalty, about 1.9 times the mean eigenvalue, and no penalty variant was run for them. This affects fig3d, surround-temporal-correlation and methods-latency-biphasic.
   - methods-spherical-asymmetry, which also has the frame-count confound.
   - fig5, whose thirds use one third of the frames with the full-data penalty.
3. fig3d-temporal-width-contrast should be not reproduced under its own criterion.
4. surround-temporal-correlation needs one stated reading in place of an undefined "partial".
5. fig5, fig7d and fig8de should carry `assumed: true`, and the opposite stimulus readings for fig7d and fig8a/b/de should be stated in the record.
