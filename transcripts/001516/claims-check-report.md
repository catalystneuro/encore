The claims file is ready for an attempt. The checker's result before and after my edits: `32 claims, 32 quotes, 9 statistical values, 0 problems`.

The statements, quotes, sources, statistics and tolerances match the paper. The recorded p-values are results, not thresholds used to count cells. Every main finding in the abstract and Results has a claim, and nothing comes from outside the paper. The file closely follows the already checked 001517 file and adds one claim for Fig. 7A.

**Changes, by claim** (all in the criteria; no ids, statements or expected values changed):
- **fig4a-fluovolt-limits and fig4b-di8-limits:** each named a paired and an unpaired t-test reading but did not say what happens when they disagree. Both readings must now agree, or the claim is blocked as methods_underspecified.
- **fig4c-equator-follows-cosine:** the two arc widths (±15°, ±30°) were left out of the outcome rule. The rule now covers every combination of arc width and test.
- **fig6a-ca-single-pulse:** the "no significant rise at 780 V/cm" part was judged on the peak-frame window alone, a choice the paper doesn't make. It is now judged under both windows, and blocked if they disagree.
- **fig5a-gd-differences:** the Fig. 5A legend says the Gd3+ and control groups have different calculated IMP. Which group's value places a datapoint against the −700 and 1200 mV bounds could change the outcome. Three readings are now named: the Gd3+ group's, the control group's, and the mean of the two.

**What remains open** (recorded in the new `checks` entry):
- **fig5a-gd-cathodic:** the one-s.e. margin used for "prevented the progressive decline" is not from the paper.
- **fig7c-fast-conductivity-drop:** the paired t-test between the poles is borrowed from the Fig. 7 legend; the paper names no test for that comparison.
- **0.3-µs pulses:** the abstract says charging weakens at 1000 V/cm, but no Results sentence states it, so I added no claim.
- **fig6b-ca-train-responders:** the paper doesn't define a "strong response", and the "nearly all" threshold is not from the paper. The Fig. 6B cell counts could not be read because no PDF renderer is installed here.
- **fig5b-conductivity-calibration:** I computed Eq. (2) with the Methods constants. It gives about 1.2 to 1.3% IMP reduction for a 10-fold rise, against the paper's ~2%. The claim is kept as the paper states it, but it will probably fail its tolerance.
- **Carried over from the 001517 check:**
  - fig3-fluovolt-nonlinear: the departure band and smoothing spans are not from the paper.
  - fig2d-lasting-reduction: the text says "about 20%" while the legend says "≤20%".
  - fig1-pole-dimming: the paper doesn't say the Fig. 1 cell is among the Fig. 4B cells.

Nothing was committed or pushed.
