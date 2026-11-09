**A. Outcomes**

The claims file has 30 claims. The attempt record was not among my materials, so the count comes from the claims file only.

| Claim | Outcome | Reason |
|---|---|---|
| unit-count | partially_reproduced | 627 cells is within 633 ± 63.3 (cell 9). The match is probably coincidental: rat H and the 142-neuron layer 5 session are missing, and the processed files appear filtered (EE188 has 105 cells in Behavior_PFC against 117 in the example file; the data description defines `Cells` as units over 1 Hz in trials). |
| task-performance | blocked (data_missing) | `SessionNP` lists correct trials only. See Section C for the raw session files. |
| fig2c-synchrony-by-layer | partially_reproduced | Pooled layer 5 is 20.3% (within 20 ± 2). Layer 2/3 is 11.8% for EE188 and 12.6% pooled, both outside 10 ± 1. Every tenth of the maze is within 50% of the mean. The layer 5 session for reading (a) is absent. |
| fig2-population-uniform | not_reproduced | EE188 peaks per tenth are [17,0,2,2,16,7,7,5,0,61], chi-square p < 0.001. Population rate per tenth is 0.57 to 2.33 of the mean (cell 15). |
| lifetime-width | reproduced | 4 of 12 combinations meet both values, for example a/i/y 0.209 ± 0.154 and b/ii/y 0.267 ± 0.171 (cell 17). |
| trajectory-divergence | not_reproduced | EE188 path diverges at 0.47 (a) or 0.43 (b); head direction at 0.01. Targets are 0.30 and 0.24 (cell 19). |
| side-arm-selectivity-by-layer | not_reproduced | Layer 5 is 62.3% or 61.6% (target 40), layer 2/3 is 54.3% or 51.8% (target 22). The shuffled-label null is 0.051, so the test is calibrated (cell 11). |
| central-arm-selectivity | not_reproduced | Layer 2/3 is 31.4% or 28.7% (target 16), layer 5 is 26.7% or 22.6% (target 18). |
| odor-selective-fraction | not_reproduced | EE188 is 45.3% (Student) or 42.7% (Welch) against 26 ± 2.6. The nose-poke window is in doubt (problem 5). |
| odor-unrelated-to-stem | reproduced (by the criterion's wording) | No positive (same-sign) association at p < 0.05. However, the stem shows a significant opposite-sign relation (Spearman r = −0.18, p = 0.047; Pearson r = −0.41, p < 0.001; cell 27), which sits poorly with "no reliable relationship" (problem 11). |
| retrospective-coding-rare | reproduced | Previous-trial labels give 4.3% (EE188), 7.3% (layer 2/3) and 8.9% (layer 5), against 66 to 78% for current-trial labels. These are close to the test's 5% null rate. |
| connection-counts | not_reproduced | 40,240 pairs against 62,408. Excitatory 0.73 to 1.09% and inhibitory 0.11 to 0.47% under all 8 combinations; none fits all three directed values. |
| cell-type-fractions | not_reproduced | Interneurons are 2.2 to 6.4% (target 12.5), targets that are interneurons 18 to 33% (target 50.7), and the pyramidal/interneuron ratio 6.5 to 19 (target 2.82). |
| pyr-pyr-connections | not_reproduced | Layer 2/3 is 0.164 to 0.176% and layer 5 0.191 to 0.246% of all pairs, both out of tolerance under every combination. |
| fig3b-session-connections | not_reproduced | EE188 connections are 84 to 86 from pyramidal references and 5 to 21 from interneurons (targets 48 and 30). The layer 5 session is not in the data. |
| fig3d-hub | not_reproduced | The notebook's detection gives 64 to 86 cells against 39. The authors' own `pairs_all` graph gives exactly 39 (cell 45), so the shortfall comes from the detection step (problems 1 and 2). |
| fig3f-distance | partially_reproduced | Same shank 396 against 234 on other shanks; same-shank probability 6.98% [6.13, 7.89] against 1.44% [1.14, 1.78] at 200 µm. The largest separation with a connection is 1,400 µm, not 1,200, and rests on 4 connections among 504 pairs. |
| nearby-pyr-int-probability | not_reproduced | 34 to 61% against 1 to 2%. |
| connected-cells-trajectory-specific | partially_reproduced | Under B-a W-a reading (b), 3 of 4 values are in tolerance (layer 2/3: 70.2% and 55.6%; layer 5 interneurons 85.7%). Layer 5 pyramidal is 72.0% against 84.7 ± 8.47. |
| no-spatial-clustering | reproduced | EE188 chi-square p = 0.577, V = 0.23. In the all-sessions variant one of 12 other sessions has p = 0.047 (FF130). |
| position-dependent-transmission | not_reproduced | 31 to 36 of 387 to 439 connections (7.3 to 9.3%) against 67 of 343 (19.5%). |
| fig5a-session-selective-connections | not_reproduced | 6 to 10 of 88 to 105 connections against 15 of 36. `pairs_all` gives 5 to 6 of 43. |
| fig4-pair-156-136 | partially_reproduced | There is a single significant region on left trials, ending at 0.645 (in tolerance). It starts at 0.325 (outside 0.4 ± 0.04), and cell 136 varies by 59% between 0.2 and 0.5, so it is not steady. |
| fig5b-example-pairs | not_reproduced | 197-201 starts at 0.355 (just outside 0.36). 49-52 has no region on either side. 186-201's pointwise region starts at 0.715, before 0.75. No pair holds under a consistent extent rule. |
| thinning-preserves-dependence | reproduced (weak) | Reading (a): 2 pairs hold, with 10/10 and 6/10 repetitions. Whether the thinned rates were actually flat is not shown (problem 6). |
| fig6-depression-facilitation | not_reproduced | Depression 4.8 to 9.1% and facilitation 3.0 to 8.2% under every combination. The test itself is flawed (problem 3). |
| fig6b-convergent-examples | partially_reproduced | 186-201 is facilitating under reading y (P = 0.000 and 0.012). 197-201 has first spikes above later ones (d = 4.7 to 8.1) but P = 0.45 to 0.65, which the flawed test makes uninterpretable. |
| fig7-supralinear-coincidence | not_reproduced | 15 satellites (within 14 ± 1.4), but no satellite exceeds either linear prediction at any window (cell 71). |
| speed-not-correlated | reproduced | Median r = −0.018. The Wilcoxon p = 0.00036 is for a shift below zero, not above. |
| population-vector-width | reproduced | With z-scored or peak-normalised rates, EE188 is 0.18 to 0.27 and layer 5 pooled 0.20 to 0.34, all in tolerance. Raw rates give about 1.0. The s.d. over positions (about 0.03) is far below the paper's 0.087 and 0.13, but the criterion does not test it. |

**B. Problems**

1. [affects a conclusion] **Global band split** (`detect_connections`, cell 35). The notebook says the Methods leave open how the 99% level splits between the two sides. They do not: the Methods define the global acceptance level as the share of datasets lying entirely within both bounds. That makes the 0.5%-per-side split (G-b) the literal reading. The notebook used the 1%-per-side split (G-a) for every downstream claim and ran G-b only for connection-counts and cell-type-fractions. Two outcomes could change under G-b: fig3f-distance, whose 1,400 µm maximum rests on 2 excitatory and 2 inhibitory connections, and the layer 5 pyramidal value of connected-cells-trajectory-specific.
2. [affects a conclusion] **No false-positive check on the connection detector** (cell 35). I ran `ccg_jitter` and `detect_connections` on 45 uncoupled synthetic cells with slow rate modulation (1,980 directed pairs, 300 surrogates). At 1 ms bins they flagged 0.45% excitatory and 0.20% inhibitory pairs under G-a, and 0.25% and 0.10% under G-b. That is close to the paper's whole connection rate. In EE188 the detector finds 105 excitatory pairs against the authors' 43 in `pairs_all`. The surplus feeds fig3b, fig3d-hub, nearby-pyr-int-probability, cell-type-fractions, the fig7 satellites and the denominator of position-dependent-transmission. The authors' `pairs_all` and `CellsInfo` types for EE188 reproduce the hub of 39 but were not used as a variant for these claims.
3. [affects a conclusion] **`order_effect` p-value**. The test takes p = mean(|d_perm| ≥ |d0|), which assumes the permutation null is centred on 0. It is not: the z-scores grow with the square root of spike count, so first and later groups of different sizes shift the null. On synthetic trains with equal efficacy (4,217 first and 516 later spikes), mean d = +45. A synapse whose later spikes are four times as effective gave d = +18.6 and was never significant or called facilitating in 10 runs. This undermines fig6-depression-facilitation and fig6b-convergent-examples; for example 197-201 has n = 2,311 against 252. Using fewer surrogates and permutations than 1,000 is stated and minor by comparison.
4. [affects a conclusion] **Unit count** (cell 9). The comparison ignores that `CellsInfo` in `behaviors.zip` may be the data description's `Cells` set (max rate over 1 Hz in trials), while EE188 enters unfiltered at 117. Rat H and the 142-neuron session are missing. The match to 633 therefore says little, so I downgraded the outcome.
5. [affects a conclusion] **Odor window** (`nosepoke_rates`, cell 25). It runs from the first poke onset to the last poke offset (median 4.6 s, up to 29 s), so it includes the gaps between pokes. The paper uses the sensor-detected poke duration. The notebook does not flag this as an assumption, and it could account for 45% against 26%.
6. [affects a conclusion] **`thin()` can stop early**. It exits when no spike remains within ±s of the peak, which can happen before the 10% flatness target is met. Cell 65 never reports whether the two surviving pairs were actually flattened.
7. [does not affect a conclusion] **Path axis** (`trial_paths`, cell 19). The x coordinate is assumed to be lateral without checking the maze's orientation. The orientation-free reading (b) gives a similar 0.43.
8. [does not affect a conclusion] **Pre-only jitter not run** (cell 55). The claims-file variant of position-dependent-transmission that jitters only the presynaptic cell was not run. It is unlikely to roughly double the count (32 to 36 against 67 ± 6.7).
9. [does not affect a conclusion] **Speed cell types** (cell 31). The text promises cell types from the connection analysis, but the code uses only the files' `CellsInfo` types.
10. [does not affect a conclusion] **Pair count printout** (cell 63). `c1 + c2 + c3` on NumPy booleans is a logical OR, so it prints "False" where a count is meant.
11. Claims-file reading, reported and not corrected. odor-unrelated-to-stem counts only associations with the same sign, but the paper's "no reliable relationship" would exclude any association, and the stem shows Pearson r = −0.41. Separately, the data description lists separate optic-sensor channels for right and left trials (channels 97 and 98). Position 0 may therefore differ physically by side, which would explain head direction diverging at 0.01. The claims file assumes one odor sampling location.
12. Chance level. The paper states none. The notebook's left-right test has a null rate of 0.051 at level 0.05, and the previous-trial fractions (4 to 9%) sit at about that level.

**C. What I could not check**

- **task-performance.** The archive listing has a `.tar.gz` of up to 2.4 GB for every session (described as all files except large raw data or movies), plus raw `.dat` files. Raw data carry the nose-poke sensor channels 97 and 98, and per the description the archives include the 1,250 Hz `.eeg` files that hold all channels. Together with the position file, these could plausibly give every trial, errors included. I did not open a tar. A listing of the members of one session's tar in the notebook would settle whether a partial test is possible.
- **Unit filtering.** I could not confirm whether `CellsInfo` equals `Cells` in `behaviors.zip`. A printout comparing the two per session would show it.
- **Detector false positives on the real data.** Detections on time-shifted or cross-session spike trains would measure this directly.
- **Downstream claims under alternatives.** The claims after connection-counts were not run under G-b or with the authors' `pairs_all` and `CellsInfo` types for EE188. Those outputs would show whether fig3f-distance and connected-cells-trajectory-specific change.
- **Thinning.** The maximum/minimum ratio of each thinned PSTH would show whether flatness was reached.
- **Order test.** The mean of the permuted d per pair would show how far the null is off-centre.
- **Maze geometry.** A plot of the mean left and right paths would confirm the orientation and whether there is one nose-poke port or two.
