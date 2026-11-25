**Verifier report, round 2: Churchland et al. 2012 (doi:10.1038/nature11129) on dandiset 000070 @ 0.260528.0919**

The claims file lists 22 claims and the attempt record gives 22 outcomes: 5 reproduced, 7 partially reproduced, 4 not reproduced and 6 blocked (data_missing). The notebook's Summary table and the README table match these. I did not download the paper this round. The sentences below that depend on the paper (what the SI expects of shuffles 2 and 3, and the velocity model's near-zero peak) were checked against the paper in round 1.

### 1. Outcomes

I agree with all 22 stated outcomes; none changed from round 1. The extra analyses added since round 1 change none of them:
- **fig3-phase-from-prep-state:** with jPCA fully refitted per held-out condition, J-array is 0.614 against a shuffle 3 median of 0.630, and N-array is 0.726 against 0.648 (cell 33). The pattern is the same as under the criterion's measure.
- **fig3-independent-of-curvature:** the J-array clockwise class stays between 0.868 and 0.878 under every heading definition and threshold (cell 29).
- **fig6 models:** the main models fail the angle bound under every seed with the 100 ms lead (cell 64).

### 2. Sentences the printed outputs do not support

1. **Cell 34 and the attempt record (fig3-phase-from-prep-state notes, and the response to round 1):** "With jPCA refitted leaving each condition out, the R2 is 0.615 and 0.727, and the pattern is the same: 8 of 10 shuffle 3 runs reach the J-array value".
   - Cell 33 prints 0.614 and 0.726.
   - Cell 33 also prints "J-array: shuffle 3 runs at or above the data, cross-validated R2 6 of 10".
   - The record repeats "0.615 and 0.727" and "reached by 8 of 10 shuffle 3 runs in J-array" in both places. These look like numbers from an earlier run. The outcome does not change.
2. **Cell 54:** "J-array reaches the range only with the -100 to +100 ms window (1.45 Hz) or 10 PCs (1.68 Hz)". Cell 53 prints 1.305 Hz for the -150 to +50 ms window, which is also in range, and a later sentence of the same cell cites it. The "only" holds for the cell 52 variants alone. The record's version of this sentence omits "only" and is fine.
3. **Attempt record, response for fig6-velocity-model:** "The failure of the angle part thus comes from choices made here". Cell 64 shows the peak near zero in both datasets only when the preparatory tuning is removed and there is no lead. The claim's model includes preparatory tuning. With preparatory tuning and no lead, N-array still peaks at 0.36 to 0.42π, above π/4. The data show that the peak depends on the model's open choices, which is how the record's notes and cell 65 put it. They do not show that the failure comes only from those choices.
4. **README:** "It takes about 13 minutes". Cell 68 prints "Total run time 14.4 min". This is minor.

Every other sentence of the Result conclusions, the Summary, the README and the record's notes and findings matches the printed outputs. I checked every number in cells 23 to 66 and in the findings, including:
- the variant ranges;
- the M1/PMd ratios of 1.5 to 2.4;
- the six-run lists in cell 29 and the "five loops" sentence, against the hand-path plot;
- the angular speed of about 1.3 Hz from -60 to +20 ms, against the cell 53 plot;
- the 6-D ratio ranges of 0.08 to 0.55 and 0.06 to 0.61;
- the hand offsets of 35 to 53 mm;
- the 2094 overlapping trial pairs.

**Round-1 reasons in the record:** they state my round-1 reasons faithfully and in my terms, for all 22 claims. Two small omissions:
- fig3-phase-from-prep-state leaves out my remark that shuffle 2 also scores high.
- My B8 (no PC smoothing) is not attached to any claim. It did not bear on a conclusion.

### 3. Round-1 points

**Resolved:**
- **B1 (units are not the paper's isolations):** each variance-fraction conclusion now carries the caveat (cells 37, 40, 43, 44, 60), and cell 23 says that all claims use the 192 units.
- **B4 (prep-prediction metric):** the full leave-one-out refit and the phase score were added. The leakage I raised does not change the outcome.
- **B5 (orientation inflates the counter-clockwise fraction):** cell 26 and the notes now say so.
- **B6 (curvature classes):** the hand-path plot and the alternative classifications were added. The classes match the paths.
- **B9 and C (J-array frequency):** it is not the static-onset effect. Windows starting at 0 or +50 ms give 1.04 and 1.13 Hz, and the angular speed is higher around onset (cell 53).
- **B3 and C (model decay):** the step and no-tuning envelopes, the extra seeds and the histograms were added (cell 64).

**What remains that bears on a conclusion:**
1. **fig3-phase-from-prep-state:** the stale figures in cell 34 and the record (item 2.1). They are reported results, though the outcome stands.
2. **suppfig3-shuffle-controls:** not_reproduced follows the criterion's R²(M_skew), which the SI does not predict shuffles 2 and 3 to reduce. On the phase score, which does measure the link to the preparatory state, shuffle 3 matches the data in J-array (9 of 10 runs at or above it) and falls below it in N-array. The outcome is disclosed as tied to the criterion's measure. It should not be read as the paper's controls failing.
3. **fig6-velocity-model and fig6-complex-kinematic-model:** not_reproduced describes the models as simulated here (lead, preparatory time course, modulation depths). No configuration that keeps the endpoint-tuned preparatory activity the claim specifies peaks within π/4 of zero in both datasets. The record should state the cause no more strongly than that (item 2.3).
4. **rotation-frequency:** partially_reproduced rests on the fixed -50 to +150 ms window. The paper chose a window per dataset, and J-array is in range with windows starting at -100 or -150 ms. This is disclosed.
5. **Variance-fraction claims** (var-captured-jpc-plane, pc23-variance, suppfig4-j-array-planes, suppfig4-planes-range, suppfig5-areas-variance) **and array-dataset-composition:** the per-electrode units cannot be resolved from the files. This is disclosed. Lower variance fractions are expected from noisier channel-level units, but this was not tested.
6. **Not affecting a conclusion:** the single dividing time for the shuffles (B7) and the missing PC smoothing (B8) remain stated deviations.
