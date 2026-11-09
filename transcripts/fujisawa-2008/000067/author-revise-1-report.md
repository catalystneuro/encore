I've worked through all 12 problems in the verifier's report and changed two outcomes. The final clean run of `python tools/entry.py all` passes in 685 s, `check` reports 0 errors, and every number in the conclusions matches the executed notebook. Nothing is committed.

**Outcome changes**
- **fig4-position-dependence: not reproduced → blocked (methods underspecified).** The calibration the verifier asked for shows the test flags 30.0% and 75.0% of synthetic pairs with constant efficacy, against the paper's P < 0.01. The protocol's rule on stated false-positive rates then makes it a block. A constant-efficacy null, added as a variant, finds 0 of 285 real pairs. It has little power, though: it flags only 6.7% of a positive control.
- **traj-diverge: blocked → partially reproduced.** I wrote a criterion before comparing x1 between sides. x1 runs along the maze, and the sides differ in the side arms of all 9 sessions by 7 to 57 px. The median divergence point is 0.49, above 0.33, which the criterion rates as partial. In five sessions x1 also differs slightly in the central arm (5 to 17 px); the notes say so.

**Kept as the criteria give them, with new variants**
- **Reverse-direction troughs (fig3-connection-rates, fig3-cell-classes, fig3-trajectory-by-class):** 34 of the 74 inhibitory connections mirror a peak in the other direction. A synthetic check finds such a trough in 21 of 30 purely excitatory pairs. Without them the rates are 1.023%, 0.898% and 0.126%, none within tolerance, and the cell classes move further from the paper. The record calls the inhibitory match fragile.
- **fig7-supralinear:** I added a linear-prediction test that is unbiased on synthetic data. Only 4 of 40 satellites are above the linear prediction (p = 1), so neither measure finds supralinearity.
- **fig3f-distance:** a check of the shank order (47.7% neighbours against 25.0% for a random order) is consistent with the channel groups being in spatial order. A pair-level test gives p = 2.3e-87, but the outcome stays with the Spearman test fixed in the criterion.
- **rats-and-units:** placing EE.088's units by the conversion's block order adds 214 units, giving 631, which is within tolerance. That rule matches the waveform placement only in rat EE, and the dandiset still has three rats, so the outcome stays not reproduced.
- **task-performance:** stays blocked. 100 laps and 147 nose-poke bouts fall outside the 335 listed trials. That bounds performance at 77% or more but cannot test the paper's 91.9%.
- **fig2b and odor-nosepoke:** McNemar tests added beside the criterion's Fisher tests; neither outcome changes.

**Fixes with no effect on outcomes**
- `field_size` now returns NaN for a map without spikes; no such side occurred, so reading (b) is unchanged.
- The side decoder now z-scores with the training trials only.
- The linearized position's `starting_time` is read and used; it is 0 in every file.
- The markdown about the rank band is corrected (it cannot reach 0.01 in 183 of 285 pairs).
- The untracked value of x1 is -1, which I added to the position finding.

The round is recorded under `verifications`, with the verifier's reasons in its own words and my responses. Files changed: the claims file (new criterion and a header note), `pfc.py`, the notebook and the README.

**Not done**
- The full paper text still could not be downloaded; PMC and Europe PMC answered with bot-check pages. A web fetch returned Methods excerpts, saved in `paper/pmc2562676_excerpts.txt`. The supplement, which defines the paper's thinning step and the Figure 6 and 7 measures, remains unavailable.
- I left the fig3 criteria's literal rule (which counts mirrored troughs) as the basis of their outcomes, because the criterion fixed it.
- The multi-unit split was not changed beyond adding the count that also leaves out the first unit of each block (416 units).
