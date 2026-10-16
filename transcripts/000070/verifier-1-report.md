**Verifier report, round 1: Churchland et al. 2012 (doi:10.1038/nature11129) on dandiset 000070 @ 0.260528.0919**

The claims file lists 22 claims. The notebook tests 16 and treats 6 as blocked. My outcomes: 5 reproduced, 7 partially reproduced, 4 not reproduced, 6 blocked.

I read the paper from the PMC author manuscript (`paper/PMC3393826.txt`) and the publisher's Supplementary Information (`paper/nature11129_SI.pdf`, text in `paper/nature11129_SI.txt`).

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| array-dataset-composition | partially_reproduced | Both sessions are present with 108 conditions each (cell 22). The dandiset holds 192 units per session, one per electrode, against the paper's 146 and 218 isolations. Both counts are outside the 10% tolerance. |
| fig3ef-same-direction | reproduced | 102 of 108 conditions (0.944) rotate counter-clockwise in J and 108 of 108 in N (cell 24), and this holds ≥0.94 under every variant. The metric does not separate the controls well, though: shuffles 2 and 3 also give 0.96 to 0.99 (cell 42; see B5). |
| fig3-independent-of-curvature | partially_reproduced | In J the clockwise-curving class (38 conditions) rotates counter-clockwise in 0.868 of cases, below 0.9. Every class in both datasets is at least 0.75 (cell 26). The Spearman correlation of curvature with net rotation is weak but significant in both datasets, with opposite signs (J ρ=0.23, p=0.018; N ρ=−0.21, p=0.026). |
| fig3-phase-from-prep-state | partially_reproduced | The leave-one-out R² is 0.632 in J, below the shuffle-3 median of 0.671 (and below every shuffle-3 run). In N it is 0.748, above 0.656 (cell 28). The metric itself is weak (B4). |
| var-captured-jpc-plane | reproduced | The first plane captures 20.0% (J) and 23.1% (N); the mean of 21.6% fails reading (a), but both values fall in 18 to 38.5%, so reading (b) passes (cell 30). Both values are near the low end of the paper's typical 20 to 35%. |
| pc23-variance | partially_reproduced | PC2+PC3 capture 21.6% (J) and 27.0% (N), mean 24.3%; neither reading passes. The jPC plane captures 0.93 and 0.86 of PC2+PC3, so that part holds (cell 32). |
| suppfig4-j-array-planes | not_reproduced | J planes capture 12.3, 14.8 and 12.8%, total 40.0%, against 22/19/12/54. The top six PCs capture 60.5% against 64. The three-plane total fails, so even the partial criterion is not met (cell 34). |
| suppfig4-planes-range | partially_reproduced | N's three planes capture 50.1%, inside 45 to 77%; J's capture 40.0%, outside it. Planes 1 and 2 are ≥0.95 counter-clockwise in both datasets (cell 34). |
| fig6a-angle-peak | reproduced | The angle peak is 0.528π (J) and 0.639π (N), both inside 0.3π to 0.7π, and stable across bin counts and variants (cell 36). |
| fig6b-skew-fit | reproduced | The 6-D ratio is 0.905 (J) and 0.845 (N); the plane ratio is 0.957 and 0.881 (cell 38). All variants are ≥0.82 and ≥0.88. |
| rotation-frequency | partially_reproduced | The first-plane frequency is 1.03 Hz in J, below 1.26 Hz, and 1.38 Hz in N, inside the range (cell 40). J only enters the range under the 10-PC and −100 to +100 ms variants. |
| suppfig3-shuffle-controls | not_reproduced | Shuffle 1 removes the structure in both datasets (median/original 0.01). Shuffle 2 passes in J (0.714) and fails in N (0.938). Shuffle 3 fails in both (0.814 and 0.937), and in N its maximum run (0.524) exceeds the original (0.517). N therefore meets the criterion for one shuffle only (cell 42). |
| suppfig5-areas-variance | partially_reproduced | None of the four values is within tolerance: J PMd 23.7, J M1 22.8, N PMd 18.1, N M1 25.0. All lie in 18 to 38.5% with ≥0.92 counter-clockwise (cell 44). N PMd passes by 0.07 points. |
| suppfig5-m1-faster | reproduced | M1 is faster than PMd in both datasets: 1.82 vs 0.83 Hz (J) and 1.54 vs 1.02 Hz (N), under all variants (cell 44). The gap is 1.5 to 2.2 times, which is larger than the paper's "slightly higher". |
| fig6-velocity-model | not_reproduced | The R² ratio part holds (6-D ratio 0.361 and 0.255, below 0.6 and below the neural values). The angle peak is 0.806π (J) and 0.361π (N), so it fails the <π/4 bound in both (cell 46). The model's construction likely drives this (B3). |
| fig6-complex-kinematic-model | not_reproduced | The R² ratio part holds (0.082 and 0.132). The angle peak is 0.861π and 0.750π, failing the <π/4 bound in both (cell 46). Same cause as the velocity model (B3). |
| fig1-leech-and-walking | blocked (data_missing) | The archive's 10 assets are maze-task array sessions of the monkeys Jenkins and Nitschke only, with no leech or walking data. |
| fig2-single-neuron-responses | blocked (data_missing) | The 469 single-electrode isolations are absent. Array units could show multiphasic responses, but that would not test this claim. |
| fig3abcd-single-electrode-datasets | blocked (data_missing) | Monkeys A and B are absent. The 27-condition 2009 J and N sessions are array recordings, not the J1 to J4 and N single-electrode datasets. |
| fig4-emg-no-rotation | blocked (data_missing) | Asset `variableMeasured` lists only Position and Units, plus ElectricalSeries for the 2010 file. I opened that file: the ElectricalSeries are 96-channel LFP per array and segment, not EMG. The paper says EMG was not recorded for the 108-condition sessions. |
| fig5-generator-model | blocked (data_missing) | It requires EMG (see above). |
| fig6cd-speed-independent-frequency | blocked (data_missing) | The speed-task data of monkeys A and B are absent; no file has an instructed-speed condition. |

### B. Problems

1. **[affects a conclusion]** `load_session` and the data check (cells 6, 10): the units are per-electrode multi-unit or threshold-crossing channels (192, with rates up to 300 spikes/s), not the paper's sorted 146 and 218 isolations. Every variance-fraction claim compares different populations: var-captured, pc23, suppfig4, suppfig5. The notebook states this, but the claims are judged on these units without a caveat on each.
2. **[affects a conclusion]** `shuffle_rates` matches SI Fig. 2 as written: the split is 50 ms after the go cue, shuffle 1 is per neuron, shuffle 3 uses one permutation for all neurons with a continuity offset. However, the SI says shuffles 2 and 3 are "not expected to remove all rotational structure" and are meant to disrupt the link between phase and initial state. Judging them by R²(M_skew) tests something the SI does not predict for them. The outcome above follows the criterion as written.
3. **[affects a conclusion]** `simulate_population` adds a preparatory component that decays with τ = 100 ms from movement onset, plus a 100 ms lead; neither is in the Methods. On a synthetic pure-decay population, `angle_peak` returns ≈π (3.05 rad), so a decaying preparatory component pushes the model peaks toward π (0.75π to 0.86π observed). The angle part of both fig6 model claims therefore depends on an unstated choice.
4. **[affects a conclusion]** `prep_prediction_r2` scores any consistent linear map from the −50 ms state to the +150 ms state, rotation or not. Shuffle 1, which has no rotation (R²_skew 0.003), scores 0.87 to 0.89, higher than the data. Shuffle 2 (a linear inversion) also scores high. As a test of "phase follows from the preparatory state" it does not discriminate. There is also mild leakage: the plane, its orientation and the normalisation are fitted on all conditions, and only the gain is left out.
5. **[does not affect a conclusion]** `jpca` orients each plane so that net rotation is counter-clockwise, which is what the paper does. As a result, `frac_ccw` is high for many non-neural inputs: shuffles 2 and 3 give 0.96 to 0.99 and the velocity model at lead 0 gives 0.93 to 0.97. This is reported as a reference only.
6. **[affects a conclusion, marginally]** `heading_change` unwraps heading only over samples above 10% of peak speed, across gaps, and reports turns up to 291°. No hand-path plot verifies the curvature classes. In J, the clockwise class sits at 0.868 against a 0.9 threshold, so moving one or two conditions between classes could change the outcome.
7. **[does not affect a conclusion]** Cell 20 and `shuffle_rates`: rates are aligned on movement only, and the go-cue split uses the median go-cue time, whereas the paper computes go-cue-locked rates separately.
8. **[does not affect a conclusion]** `jpca` omits the Methods' extra "PC smoothing"; the SI says it has little effect. The 20 ms vs 24 ms smoothing choice does not change any outcome (cell 19).
9. **Helper checks that passed:**
   - `skew_fit` recovers a known skew-symmetric matrix (error 5e-4).
   - On synthetic steady rotations of 1, 2 and 2.5 Hz, `jpca` returns 1.01, 1.96 and 2.45 Hz.
   - `angle_peak` gives 0.53π for a pure rotation.
   - Orientation flips correctly for clockwise input.
   - `heading_change` returns 90° for a 90° arc.

   One caveat from the same tests: when the rotation starts at movement onset, the −50 to 0 ms static segment biases the frequency down (2 Hz is read as 1.49 Hz). This may partly explain J's 1.03 Hz.

### C. What I could not check

- **Isolation counts:** whether any file carries sorted isolations matching 146 and 218. Per-unit isolation quality, or the lab's sort labels, would settle this, but the files hold neither.
- **Hand-path classification:** whether the curvature classes are right. A plot of condition-mean hand paths coloured by class (cell 26) would show it.
- **Why J's frequency is low:** whether the 1.03 Hz is a real slower rotation or the static-onset effect in B9. Plane projections against time for −50 to +150 ms, and frequency over a window starting at the onset of the rapid change, would separate the two.
- **The decay effect in the models:** a re-run of `simulate_population` without the preparatory decay (a step envelope), with the angle histograms, would show how much the decay drives the fig6 angle failure.
- **Shuffle 3 against shuffle 1:** the prep-prediction R² of shuffle 3 against shuffle 1 per run, plus a rotation-specific score such as the mean phase advance predicted from the initial state, would test fig3-phase-from-prep-state properly.
- **Unit counts in N-0910:** I could not confirm them against the paper's N-9-10-2010 dataset because the SI gives no unit count for it.
