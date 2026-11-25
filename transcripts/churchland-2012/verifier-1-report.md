**Verifier report, round 1: Churchland et al. 2012 on DANDI:000070 (0.261122.2046)**

The claims file has 22 claims. The notebook tests 16 and treats 6 as blocked. No attempt record was among my materials, so these counts come from the claims file and the notebook's cell 0.

I tested the helper functions on synthetic inputs, and they behave correctly:
- **`jpca` / `freq_hz`:** a planted 2 Hz rotation came back as 1.95 Hz, with an R2 ratio of 0.95.
- **Orientation:** it is forced counter-clockwise for both senses of rotation, and 100% of conditions then rotate counter-clockwise.
- **`fit_Mskew`:** it recovers a known skew-symmetric matrix to within 1e-15.
- **`gamma_spikes`:** it gives 40.1 spikes/s for a 40 spikes/s input.
- **`shuffle_reassign`:** activity stays continuous at the dividing point.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| array-dataset-composition | partially_reproduced | Both sessions are present with 108 conditions each. Each has 192 units against 146 ± 14.6 and 218 ± 21.8 (cell 13). The units are unsorted threshold crossings, one per electrode (cell 6), not the paper's isolations. |
| fig3ef-same-direction | reproduced | 103/108 (95.4%) and 107/108 (99.1%) of conditions rotate counter-clockwise, and every reading clears 90% (cell 15). Caveat: under shuffles 2 and 3 the median is still 93–98% counter-clockwise (cell 34), so this measure does not separate real from shuffled data. |
| fig3-independent-of-curvature | partially_reproduced | Main reading: J-array clockwise-curving class is 30/34 = 88.2% counter-clockwise, below the 90% bar. Every class in both datasets is at least 75% (cell 17). The `move_begins_time` readings give reproduced, so the outcome rests on the onset column. In J-array, rotation direction depends on curvature in the logistic fit (p = 0.029). |
| fig3-phase-from-prep-state | partially_reproduced | Cross-validated R2 is 0.568 (J) and 0.676 (N), both ≥ 0.5. J falls below its shuffle-3 median of 0.686; N is above its 0.600. All four readings agree (cell 19). See problem 2: the shuffle-3 reference is not a valid null here. |
| var-captured-jpc-plane | not_reproduced | Main reading: 14.9% and 22.9%, mean 18.9%. That misses 28 ± 2.8, and J is outside 18–38.5 (cell 21). The `move_begins_time` readings pass reading (b) with J at 18.7–19.0%, so this depends on the onset column. |
| pc23-variance | not_reproduced | PC2+PC3 capture 19.2% (J) and 28.3% (N), mean 23.8%, outside 29 ± 2.9. The jPCA/PC2+3 ratio for J is 0.78, below 0.8 (cell 23). The `move_begins_time` readings give partial (ratio part only). |
| suppfig4-j-array-planes | not_reproduced | J-array planes: 13.3, 13.3 and 12.2%, total 38.8% against 54 ± 5.4. Top six PCs: 51.9% against 64 ± 6.4. All readings agree (cell 25). |
| suppfig4-planes-range | partially_reproduced | N-array passes (47.7%, first two planes 97% and 100% counter-clockwise). J-array fails at 38.8%, below 45. All readings agree (cell 26). |
| fig6a-angle-peak | reproduced | Peaks at 0.528π (J) and 0.639π (N) under the main reading, all readings within 0.3–0.7π (cell 28). |
| fig6b-skew-fit | reproduced | 6-D ratios 0.918 and 0.909; plane ratios 0.946 and 0.953. All readings and the 24 ms variant pass (cell 30). |
| rotation-frequency | reproduced | 1.344 Hz (J) and 1.402 Hz (N), within 1.26–2.75 Hz (cell 32). With `move_begins_time`, J drops to 1.06–1.10 Hz, which would give partial, so this rests on the onset column. |
| suppfig3-shuffle-controls | partially_reproduced | J-array meets the criterion for all three shuffles: shuffle 3 median is 0.745 of the original, against a 0.75 limit, and holds over 5 seeds. N-array meets it for shuffle 1 only: shuffle 2 is 0.76 and shuffle 3 is 0.87 of the original (cell 34). The `move_begins_time` readings give not_reproduced (J shuffle 3 at 0.77–0.79). This is borderline and partly a criterion problem (see problem 3). |
| suppfig5-areas-variance | not_reproduced | J PMd 21.6% and M1 20.2% (expected 29), N PMd 17.7% (expected 32), N M1 27.1% (expected 28). N PMd is also below the 18% floor for partial. All readings agree (cell 36). |
| suppfig5-m1-faster | reproduced | M1 is faster than PMd in both datasets under all readings: J 2.02 vs 0.84 Hz, N 1.49 vs 0.97 Hz (cell 37). The gap is large, not "slight" as the paper says. |
| fig6-velocity-model | not_reproduced (assumption-driven) | The 6-D ratio passes everywhere (0.08–0.44). Under the main model reading the angle peaks are 0.417π and 0.639π, above π/4, and N rotates 87% counter-clockwise (cell 39). With a 0 ms lead it reproduces. The outcome is set by unstated model choices (problem 4), not by the data. |
| fig6-complex-kinematic-model | not_reproduced | The notebook gets partial only because J's angle peak of −0.972π counts as "below π/4". A peak near ±π is not "slightly above zero" (problem 1). Corrected, both datasets fail on the angle peak under the main reading, though the 6-D ratios are low (0.095 and 0.144) as the paper predicts (cell 40). |
| fig1-leech-and-walking | blocked (data_missing) | The archive metadata lists 2 subjects (Jenkins, Nitschke) and 10 Utah-array files. There are no leech or walking-monkey data. |
| fig2-single-neuron-responses | blocked (data_missing) | The single-electrode datasets (469 isolations, monkeys A, B, J, N) are not in the archive. The array units are unsorted channels, so the claim's population cannot be tested. |
| fig3abcd-single-electrode-datasets | blocked (data_missing) | The extra 27-condition Jenkins and Nitschke sessions are array recordings, not the single-electrode J1–J4, A, B or N datasets. |
| fig4-emg-no-rotation | blocked (data_missing) | The archive's variableMeasured lists ProcessingModule, SpatialSeries, Position, Units, ElectrodeGroup and ElectricalSeries. There is no EMG. |
| fig5-generator-model | blocked (data_missing) | No EMG, as above. The paper itself says the generator model could not be built for the array datasets. |
| fig6cd-speed-independent-frequency | blocked (data_missing) | The speed-task monkeys A and B are absent; both archived subjects did the maze task. |

For all six blocked claims I checked the archive itself (API version and asset metadata), not just the notebook's statement. No part of any of them can be tested.

**B. Problems**

1. **[affects a conclusion]** `sim_ok` (cell 39, used in cell 40) tests `peak_over_pi < 0.25` without wrapping, so any negative peak passes. Peaks of −0.972π (complex model, main reading, J) and −0.917π (0 ms lead, persistent preparatory term, J) lie next to ±π, which means contraction, not a peak just above zero. This alone turns fig6-complex-kinematic-model from not_reproduced into partially_reproduced. The test should be 0 ≤ peak < π/4, or |peak| < π/4.

2. **[affects a conclusion; claims-file design]** The shuffle-3 reference for fig3-phase-from-prep-state (cell 19) cannot work as a null. The dividing point is −268 to −320 ms, so the whole analysis window (−50 to +150 ms) lies after it. The states at −50 and +150 ms then both carry the same reassigned movement pattern, plus one constant offset. Predictability from −50 to +150 ms survives by construction: J's shuffle median of 0.686 exceeds the real 0.568. The notebook follows the criterion, but the comparison does not test what the paper says, which is that the preparatory state predicts the phase.

3. **[affects a conclusion; claims file misreads the paper]** suppfig3-shuffle-controls measures rotation strength as R2(M_skew). The Supp. Fig. 2 legend says shuffles 2 and 3 are "not expected to remove all rotational structure (most such structure is merely sign-inverted)". What they should disrupt is consistency and the link between phase and initial state. N-array fails on exactly those two shuffles, so the criterion tests something the paper does not predict.

4. **[affects a conclusion]** `simulate_population` uses a preparatory term that ramps from preparatory to movement tuning between −50 and +50 ms (`prep="switch"`). That transition sits inside the analysis window. Combined with the 100 ms lead, it can manufacture a sweep of the state through the plane. Both are the author's own choices (stated as assumptions), and the outcome flips with the lead (0 ms gives reproduced). The factor weighting (unit-SD factors times uniform weights) is also the author's own. For fig6-velocity-model, the conclusion is decided by these assumptions.

5. **[affects a conclusion]** The onset column (`offline_move_onset_time` or `move_begins_time`) changes the outcome of four claims: fig3-independent-of-curvature, var-captured-jpc-plane, rotation-frequency and suppfig3-shuffle-controls (pc23-variance moves from not to partial). The notebook takes the main reading as an assumption, which is reasonable: the paper stresses precise offline alignment, and the column is described as "calculated offline". But those four outcomes are conditional on it, and the notebook never prints the two columns' NWB descriptions.

6. **[affects a conclusion; claims file]** For var-captured-jpc-plane, reading (b) uses "typically 20–35%". In the paper that range comes from the Supp. Fig. 5 legend, about the per-area analysis, not the first plane of the full population. Under the `move_begins_time` readings the claim passes only through (b).

7. **[does not affect a conclusion]** `fig3-independent-of-curvature` (cell 17): with the `move_begins_time` readings the hand paths stay aligned on `offline_move_onset_time`, so the curvature window is shifted 25–52 ms from the neural alignment.

8. **[does not affect a conclusion]** `jpca` (reach.py): the polarity check `sign(v1.real.sum()) != sign(v2.real.sum())` never fires, because `v2 = conj(v1)`. The later orientation step makes it harmless.

9. **[does not affect a conclusion, unresolved]** Cell 8: in N-array, M1 lags PMd by 25–32 ms in every block, and by 58 ms in the rise of across-condition spread; in J-array the lag is about 5 ms. It is stable over the session, so there is no clock drift. Whether it is physiological or a fixed offset between the arrays is not established. A fixed offset would distort the N-array whole-population and per-area results.

**C. What I could not check, and the output that would let me**

- **Onset column definitions:** the NWB descriptions of `offline_move_onset_time` and `move_begins_time` were not printed; printing them would settle problem 5.
- **Shuffle-3 phase test:** shuffled data projected onto the original jPC plane, and phase R2 predicted from the state at the dividing point, are not shown. Either would show whether problem 2 changes the conclusion.
- **Model angle histograms:** the histograms for the simulated models, the share of angles within π/4 of zero, and the 0 ms lead with the persistent preparatory term over 5 seeds.
- **Non-counter-clockwise conditions:** which conditions rotate clockwise in J-array, with their curvature values, to see whether the 4 clockwise-curving exceptions are driven by curvature.
- **Inter-array lag:** an N-array check that does not rely on neural timing, such as aligning both arrays on the go cue or target onset and comparing latencies, would resolve problem 9.
- **Figures:** I could not view the images; my judgements rest on the printed outputs.
- **Attempt record:** it was not provided, so the claim count (22, with 16 tested and 6 blocked) comes from the claims file and notebook cell 0.
