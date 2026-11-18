**Verifier report, round 1: Tingley & Buzsáki 2018 on DANDI:000213 (0.261109.2219)**

The claims file has 32 claims. The notebook tests 26 and treats 6 as blocked. I ran synthetic tests on `tingley.py` (decoder, information measure, best-smoothing selection), with results in B1–B5. I also queried the DANDI API for the metadata of all 67 assets.

Cell 0 of the notebook still contains an outcome table even though the summary was meant to be removed. I did not use it.

### A. Outcomes

| claim | my outcome | reason |
|---|---|---|
| ls-neuron-count | reproduced | Cell 6: 1,696 LS units (1,647 ± 164.7), 62 sessions, 5 animals. |
| hpc-unit-count | not_reproduced | Cell 8: unit labels give CA1 2,636 (outside 2,297 ± 229.7) and CA3 624 (inside). The session reading gives CA1 2,261 (inside) and CA3 999 (outside). No reading has both inside tolerance. |
| ls-active-neurons | reproduced | Cell 10, reading (a): 829 (840 ± 84). |
| fig2-ls-phase-vs-shuffle | not_reproduced | Within tolerance only under ba0 (0.890) and bb0 (0.830). Those readings drop undefined phase, and the synthetic test shows that test is invalid (B1, B2). With undefined phase set to 0 the fractions are 0.578 (aa1) and 0.462 (ba1), outside 0.89 ± 0.089. |
| fig2-ls-phase-beats-rate | not_reproduced | Under the calibrated readings aa1/ba1, neurons are 0.18/0.25, conditions 0.045–0.069 by test and 0.44–0.46 by lower mean, sessions 0.40/0.32; none is over half. The "left out" readings would give partially_reproduced, but they are confounded (B1). |
| fig2e-ls-phase-lower-mse | not_reproduced | aa1: phase MSE 7,738 is above rate 7,597. The very small p values under aa0/ba0 come from the confound in B1. |
| fig2fg-mse-difference | not_reproduced | Cell 19: no reading has all four values within tolerance. Hippocampal values are −2,900 to −5,500 (or +177 to +240 when undefined phase = 0) against −33. |
| fig1i-hpc-rate-phase-equivalent | reproduced (fragile) | Cell 21: both KS tests are not significant under aa1/b (p = 0.21, 0.82) and ba1/b (p = 0.24, 0.82), with 1,924 fields and 45 sessions. They fail under Gaussian field maps (aa1/a p = 0.044; ba1/a p = 0.008) and under every "left out" reading. |
| ls-lower-peak-info | partially_reproduced | Cell 34: LS is lower at p < 1e-100 under every reading. No reading has both averages within tolerance (e.g. LS 0.416 but HPC 1.045; or HPC 1.659 but LS 0.965). |
| ls-few-place-fields | partially_reproduced | Cell 24: LS 0.064 or 0.100 (outside 0.053 ± 0.0053); HPC 0.287 or 0.336 (inside). Both map counts are within tolerance. LS is lower. |
| hpc-place-field-properties | partially_reproduced | Cell 26, reading a/a: 677/1,420 = 0.477 and 1.27 fields per neuron are within tolerance. The median peak of 7.3 Hz and median width of 43 bins are not. |
| ls-place-fields-unstable | partially_reproduced | Cell 28: the CV reading has LS higher (82 vs 72 %; p = 1e-12 or 4e-24), but the medians are far from 41.5 and 10. The SD reading has LS lower. |
| fig1e-phase-info-smaller-scale | partially_reproduced (by the criterion's wording) | Cell 30, fields b, levels b: phase 21 and rate 28 bins, p = 1.7e-52; the phase median is outside tolerance. The small phase scale is what random phases also produce (B3, B4). |
| fig1g-phase-more-info-fine-scale | partially_reproduced (by the criterion's wording) | Cell 32: phase is above rate at 2 and 3 bins, and rate is above phase at none of the smoothings from 7 to 50. The part that holds is an estimator artefact (B3). |
| fig3-ls-phase-reliable | reproduced | Cell 36: LS phase 0.036/0.070 is lower than HPC rate (0.868/0.891) and HPC phase (0.227/0.231) under both measures. |
| fig4d-depth-gradient | partially_reproduced (by the criterion's wording) | Cell 38: across animals the direction is opposite to the claim (all per-animal r > 0; pooled r = +0.33, p = 0.009). Within sessions r < 0 in 24/47, a majority by one session (median r −0.005). Run only under aa0 (B6). |
| fig4e-onset-depth | not_reproduced | Cell 40: no animal reaches p < 0.001 under any reading. The best is DT2, r = 0.257, p = 1.5e-3. |
| fig4e-onset-mediolateral | reproduced (fragile) | Cell 42, onset_map: \|r\| = 0.92/0.94 and Kruskal-Wallis p = 0.017. The onset_spikes reading fails the Kruskal-Wallis test (p = 0.37). The neuron set comes from the invalid aa0 test (B1); three of the five animals share ML 0.5 (B7). |
| speed-independent | partially_reproduced | Cell 44: 0.005–0.008 and 0.051–0.076, both under 20 % but outside tolerance. |
| fig5-assemblies | blocked, too_large (disputed) | The cost estimate does not support blocking (B9); a sampled test was feasible. |
| fig5g-assembly-neurons-stronger-phase | blocked (depends on fig5) | Same as fig5. |
| figs5-assembly-independent-of-locking | blocked (depends on fig5) | Same as fig5. |
| fig6-session-counts | partially_reproduced | Cell 48: CA3 19 and LFP 14 match. CA1 by units is 25 or 33 against 63 ± 6.3; only the LFP-channel variant (57) is within tolerance. |
| fig6c-ca3-coherence-increases | reproduced | Cell 50: CA3 slope > 0 and > CA1 per trial and per session (p ≤ 6e-3). CA1 end−start 0.030 against CA3 0.321. |
| fig6d-cfc-stronger-ca3 | reproduced | Cell 52: CA1 and CA3 slopes > 0 at both levels; raw CA3 > CA1 (p = 7e-8 per session). |
| fig6e-assembly-position | blocked (depends on fig5) | Same as fig5. |
| figs7-ensemble-ls-phase-best | not_reproduced | Cell 54: LS phase MSE (~6,000, near chance) is higher than HPC phase (~5,600) and HPC rate (~1,500–2,000) at every size from 15 to 25. |
| figs2-rate-phase-independent | not_reproduced | Cell 56: hippocampal fraction 0.143 (a) or 0.207 (b), against < 0.022. That is also above the 5 % expected by chance under reading (b). |
| figs3-ls-major-target | blocked, other | Allen data is outside this archive (`data: elsewhere`). It is testable through the Allen API. |
| figs6-reference-frame | blocked, metadata_insufficient | Confirmed: none of the 67 asset session descriptions mention a rotation. Tasks are only linear, central, wheel or both alternation. |
| figs1f-trial-counts | not_reproduced | Cell 58: with all trials, 3,987 / 5,219 / 701; none is within tolerance. Restricted to LS sessions (the author's choice), central 5,219 is still outside 6,608 ± 661. The criterion has no partial rule. The ballistic fraction cannot be tested. |
| fig7-dynamic-weighting-model | blocked, other | The model lives on GitHub, not in the archive. It was not run. |

### B. Problems

1. **[affects a conclusion]** `decode_unit`/`decode` with `fill=None` (adopted reading "0"). Dropping samples whose smoothed phase is undefined (67–73 % of samples, cell 4) lets the phase decoder read where the cell fires. Synthetic place-field cell with uniformly random phase:
   - Phase MSE 1,317 against rate MSE 9,596.
   - Null cells passing "phase beats chance" at p < 0.01: 47 % with the trial split, 91 % with the sample split.
   - Null cells passing "phase beats rate": 76 % / 98 %.
   - With undefined phase set to 0, both rates are about 1 %.
   
   Affected claims: fig2-ls-phase-vs-shuffle, fig2-ls-phase-beats-rate, fig2e, fig2fg, fig1i, fig4d, and fig4e / fig4e-ML (their neuron set is `aa0_sig_chance`). The notebook states this choice as an assumption but never checks it.
2. **[affects a conclusion]** Split reading (b) with 20-bin smoothing puts adjacent, nearly identical samples from the same trial into both training and test. It raised the null false-positive rate from 47 % to 91 % in item 1. The reproduced value of fig2-ls-phase-vs-shuffle (ba0 0.890) rests on it.
3. **[affects a conclusion]** `olypher_peak` on phase. P(k|x) is estimated from the few trials that are defined at a bin, and the maximum is then taken over bins. Random phases score about 3.1 bits at every smoothing from 1 to 20, more than a real rate field (0.5–1.2). This decides fig1g (phase above rate everywhere) and the phase median in fig1e. A minimum sample count or a shuffle-subtracted information would fix it.
4. **[affects a conclusion]** `best_scale` in cell 30 uses a zero-padded `np.convolve(..., "same")`. A monotonically rising curve returns 48, so the "drop ≥ 49" rule can never fire (1,640 of 1,640 kept), and rate scales are pulled low. Random phases give a median best scale of 7.5, close to the notebook's 7.0.
5. **[affects a conclusion]** `_nearest` breaks ties toward the lowest bin. Rate templates of exactly 0 send zero-rate test samples to bin 0. As a result the hippocampal rate MSE (median 7,760, cell 4) is worse than uniform guessing (about 6,733 for 201 bins). This inflates rate MSE, and so the phase-minus-rate values in fig2e, fig2fg and fig1i. It is not stated as an assumption.
6. **[affects a conclusion]** Cells 38 and 40 (fig4d, fig4e) run only under aa0. The split and bin readings and the "undefined = 0" alternative were not run, although item 1 shows the outcome depends on them.
7. **[affects a conclusion]** Cell 42 applies Kruskal-Wallis to angles. That ignores wrap-around (DT2's mean is about 2.6–2.75 rad, near ±π). The criterion allows Kruskal-Wallis, but Watson-Williams was not run, and the reproduced outcome rests on p = 0.017.
8. **[affects a conclusion]** In fig4d/fig4e depth, the archive descriptions say "which probe each depth belongs to … not stored". The first depth is taken as the LS depth, as the claims file says, but this is never checked against the data. The direction of the 10 µm-per-site increment along the shank is also unchecked. Either could flip the sign of fig4d.
9. **[affects a conclusion]** In cell 46 (fig5 cost), the count of 619,934 pairs uses every hippocampal × LS unit pair, not included units, and ignores the >100-spike rule. At the notebook's own 15.3 s per pair, the paper's 11,264 pairs come to about 48 CPU-h. A random sample of about 500 pairs (about 2 CPU-h) would have tested the assembly fraction and the median timescale. The too_large blocking of 4 claims is therefore not established.
10. **[does not affect a conclusion]** ls-lower-peak-info: the criterion's makeFig1.m divides peak information by the trial count. This is neither applied nor mentioned. The outcome is partial either way.
11. **[does not affect a conclusion]** Cell 54 uses `ENS_DRAWS = 3`, where criterion reading (a) says 10 draws. The differences are large.
12. **[does not affect a conclusion]** Cell 58: "only ballistic runs, by its description" is a hard-coded string, not derived from the data. The LS-session subset in figs1f is the author's choice, not the criterion's.
13. **[does not affect a conclusion]** Cell 4: DT8 has 0 hippocampal units in the files, though the paper gives every rat a CA1 probe. This probably explains the CA1 shortfall in fig6-session-counts, and the notebook does not flag it.
14. **[does not affect a conclusion]** speed-independent: the precession test flags 0.5–0.8 % of conditions at p < 0.01, below its own 1 % false-positive rate. The test (one r against shuffles) may be conservative.
15. **[does not affect a conclusion]** Cell 0 still carries an outcome table, although the summary was supposed to be removed.

I found no place where the claims file misreads the paper.

### C. What I could not check

- **Whether item 1 holds in the real data, not just in simulation.** Needed: a real-data null, such as phase decoding after circularly shifting each trial's spike phases (positions kept) under aa0/ba0. Also per-condition counts of defined phase samples per bin.
- **Whether item 5's tie-breaking drives the rate MSE.** Needed: the rate MSE with random tie-breaking, and the chance rate MSE (`chance_rate`, computed but never printed).
- **fig4d and fig4e under the other readings.** Needed: both cells run under aa1/ba1/ba0, plus a check of site-number direction against `max_waveform_channel` depth order.
- **Whether figs6 is fully blocked.** Needed: conditions per session and maze, and the columns of `head_position` (orientation present or not). API metadata does not show these, and I did not open the files.
- **Unit-label semantics** ('hpc' vs CA1/CA3 in sessions with CA3 sites) and **clock alignment** beyond the 1-s-shift checks in cell 4.
- **The fig5 cluster.** Needed: a pilot run of `bz_peerPrediction`-style fits on a random sample of included pairs.
