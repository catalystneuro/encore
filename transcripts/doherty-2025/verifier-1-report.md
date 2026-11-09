**A. Outcomes** (the claims file has 40 claims)

| Claim | Outcome | Reason |
|---|---|---|
| fig1-network-size | partially_reproduced | Under the criterion as written, the unit count is 4,480, 3,231, 2,919 and 2,917, not 10,073 (cell 16), because the files store only cells that fired (cells 5, 7). The gids support 10,073: the M1 gids lie in 0–10,072, inputs start at gid 10,073 and all 15 populations are present. |
| model-pt5b-excitability-decrease | blocked (data_missing) | The archive holds 17 assets, all network simulations (I checked the API). There are no current-injection runs, and the protocol is also open (claims file). |
| robustness-four-sets | blocked (methods_underspecified) | The claims file has no measures or expected values for it. The per-set measures are in cell 20. |
| fig2-control-rest-beta | reproduced | The SCH peak is 19 Hz both above 0 Hz and above 5 Hz (cell 22). |
| fig2-control-activated-gamma | reproduced | The SCH peak is 44 Hz under both readings. |
| fig5-pd-rest-beta | reproduced | The SCH peak is 15 Hz under both readings. |
| fig5-pd-activated-gamma | not_reproduced | The SCH peak is 27 Hz under both readings, against 43 ± 4.3. The other three sets give 28–31 Hz (cell 20). |
| fig2c-control-pt5b-rate-activated | reproduced | R1 and R3 give 11.69/9.40 and 26.76/18.17. All four tests give p < 1e-98 (cell 24). |
| fig2c-control-it23-rate-activated | not_reproduced | R3 values are all within tolerance (1.20/1.65, 6.66/8.86). The paired tests fail: T1 p = 0.016 and T2 p = 0.011, on only 25 cells kept in both files (cell 26). This depends on the pairing choice in problem 1. |
| fig2c-control-it6-rate-activated | reproduced | R3 values 5.82/5.78 and 3.47/5.19; every test gives p < 1e-11 (cell 28). |
| control-it5-silenced-activated | reproduced | R3 gives 3.26, 3.08, 0, 0 (cell 30). |
| control-it4-rate-activated | reproduced | R3 gives 2.57 and 4.74 (cell 32). |
| pt5b-highest-rate | blocked (methods_underspecified) | Over all 15 populations PV5A is highest in every file. Over the excitatory types PT5B is highest in every file. The readings disagree, so the criterion's block rule applies (cell 34). |
| control-cv-isi | reproduced | Window W with ≥1 ISI gives 0.59/0.365/47.8% and 0.61/0.30/25.7% (cell 36). |
| pd-cv-isi | reproduced | Window W with ≥1 ISI gives 0.339/0.267/80.6% and 0.184/0.191/93.8%. |
| control-subthreshold-oscillations | blocked (methods_underspecified) | The membrane potentials exist (20 traces per file in the paper's set), but there is no detection rule. 57.4% of 20 cells is not a whole number (cell 38). |
| pd-no-subthreshold-oscillations | blocked (methods_underspecified) | Depends on the claim above. |
| pd-activated-vm-more-negative | reproduced | All 20 of 20 cells are lower in the parkinsonian file: mean −5.6 mV, median −7.1 mV. The other three sets agree (cell 40). |
| control-duty-cycle | not_reproduced | No combination of readings puts both values in tolerance (cell 42). |
| pd-duty-cycle | not_reproduced | Same as above. |
| fig3a-control-rest-spectrogram | not_reproduced | S1 shows no local maximum in 1–3 Hz and a burst rate of 1.30 Hz against 1.7 (cell 46). |
| fig3b-control-activated-spectrogram | not_reproduced | Under S1 the 15 Hz burst rate is 1.30, the 25–35 Hz rate 1.30, the median 25–35 Hz duration 66.9 ms, and the 15 Hz durations are out of range (cell 48). |
| fig6a-pd-rest-spectrogram | not_reproduced | The 25–35 Hz burst rate is 1.74 Hz (S1) and 1.45 Hz (S2), against 5.0 (cell 50). |
| fig6b-pd-activated-spectrogram | not_reproduced | The burst rate is 2.6 Hz (S1) and 2.9 Hz (S2), against 9–22 Hz (cell 52). |
| control-coincident-spikes | not_reproduced | Under every reading in the claims file, 99.99–100% of spikes are coincident, against 1% and 3% (cell 54). See problem 3. |
| pd-coincident-spikes | not_reproduced | Same: about 100%, against 2% and 3%. |
| fig4-control-unitary-events | blocked (methods_underspecified) | The helper's coincidence count saturates: every 1 ms bin holds ≥2 spikes, and the median observed count equals the expected count, 100 of 100 (cell 56). The test cannot find significance, and only one count reading was run (problem 2). |
| fig7-pd-unitary-events | blocked (methods_underspecified) | Same as fig4. |
| rest-synchrony-increase | blocked (methods_underspecified) | It rests on the saturated unitary-event output: 0 s against 0 s (cell 58). |
| fig5c-pd-pt5b-rate-activated | reproduced | All readings are within tolerance; every test gives p < 1e-200 (cell 60). |
| fig5c-pd-it23-rate-activated | not_reproduced | R3 values are within tolerance, but even the unpaired T3 fails (p = 0.0018), and T1 gives p = 0.60 (cell 62). This holds whatever pairing is used. |
| pd-it5-silenced-activated | reproduced | R3 gives 2.17, 1.25, 0, 0 (cell 64). |
| pd-it6-rate-unchanged | reproduced | R3 means are 6.00 and 5.99, and no test gives p < 0.05 under R3 (cell 66). R1 tests do find a difference (p 0.0002–0.019). The outcome depends on problem 1. |
| rest-pt5b-rate-pd-vs-control | reproduced | Values within tolerance, every test gives p < 1e-10, and the parkinsonian standard deviation is lower (cell 68). |
| rest-it4-rate-pd-vs-control | not_reproduced | R3 means 2.57 and 14.13 match the paper, but the parkinsonian value rests on n = 2 cells. T3 gives p = 0.077 and T4 p = 0.31 (cell 70). |
| rest-it5a-rate-pd-vs-control | reproduced | R3 means 3.25 and 2.16. Every test gives p ≤ 0.0027 (cell 72). |
| activated-pt5b-rate-pd-vs-control | not_reproduced | Values within tolerance under R1/R3, but Mann-Whitney gives p = 0.0052, which is not below 0.001 (cell 74). Under R2 no test reaches p < 0.05, which is what the Discussion says. |
| activated-it6-rate-pd-vs-control | reproduced | R3 means 3.47 and 5.99. Every test gives p < 1e-7 (cell 76). |
| rest-beta-power-order-of-magnitude | partially_reproduced | The increase is there, but the ratio is 111–129 under S1 and 65 under S2, above the claims file's 3.16–31.6 range under every reading (cell 78). The criterion does not say what outcome a ratio above 31.6 gets. The other sets give 7–65 (cell 20). |
| activated-20-35hz-power-pd-vs-control | reproduced | Parkinsonian power is higher under every reading: S1 4.6×, S2 4.7×, SCH 11.8× (cell 80). |

**B. Problems**

1. **[affects a conclusion]** `compare` (cell 13) runs the paired tests T1 and T2 under R3 (and R2) only on cells present in both files. The notebook states this but treats it as settled. Pairing the union of cells, with 0 where a cell is absent, fits R3 equally well, and it was not run.
   - For fig2c-control-it23 only 25 cells are paired, and T1/T2 are what fails.
   - For pd-it6-rate-unchanged, the union pairing is close to R1, which does find a difference (p ≈ 0.002).
   - Either outcome could flip.
2. **[affects a conclusion]** `m1sim.unitary_events` counts 1 ms bins holding ≥2 distinct cells, a yes/no per bin. With 1,435 cells firing about 17–42 spikes per ms, every bin qualifies, so the count is capped at the window length and can never exceed the expectation. I checked this on synthetic data:
   - With 20 cells at 2 Hz it detects injected synchrony.
   - With 100 cells at 10 Hz carrying 20 injected pair events, it finds nothing.
   - With 20 cells all firing together 11 times, it reports 12 observed against 70 expected.

   The claims file says only "2 or more PT5B spikes within 1 ms"; counting coincident spikes or pairs instead is equally allowed and was not run. Grün's unitary events work on patterns across a small set of neurons. The 0 s results are an artefact of the method, not evidence against the claims.
3. **[affects a conclusion; claims-file reading]** For control-coincident-spikes and pd-coincident-spikes, the claims file takes the share of all PT5B spikes that have another PT5B spike within 1 ms. At the population's spike density that share is about 100% under any window, so the paper's 1–3% cannot have come from this measure over all 1,435 cells. The paper's neuron subset or denominator is unstated. I report not_reproduced per the criterion, but the reading looks like a misreading of the paper.
4. **[affects a conclusion]** `stft_spec` (S2) uses a 250 ms window, which gives 4 Hz bins and none between 1 and 3 Hz. Under S2 the 2 Hz test can therefore never pass for fig3a and always passes for fig3b. fig3a still fails under S1, so its outcome is not_reproduced either way; but if a valid S2 passed, the readings would disagree and the claims file's rule would make it blocked. The window is the author's own choice, stated as an assumption.
5. **[does not affect a conclusion]** `band_bursts` with S2 divides by the span of the frame centres, 2.075 s instead of 2.3 s, which raises S2 burst rates by about 11%. The fig3b S2 25–35 Hz rate of 0.96 would become 0.87 and fail. fig3b fails on other parts anyway.
6. **[does not affect a conclusion]** E2 (the mean over 11 electrodes) cannot be computed because the files hold one trace, "LFP 0". The notebook takes it to be E1 without checking which depth it is. Every LFP-based outcome rests on E1 alone.
7. **[does not affect a conclusion; claims-file note]** The burst definition (half-height of the band power between its minimum and maximum) and the 14–16 Hz band are the reader's own, not the paper's. The four spectrogram not_reproduced outcomes test that convention more than the paper. The same goes for the duty cycle on the unsmoothed SCH: the median period in W is 10 ms (cell 42), so the periods are noise crossings, not the 15–20 Hz cycles.
8. **[does not affect a conclusion]** In the paper's set, the membrane-potential traces stop matching the stored spikes after about 0.5 s (cell 9); in set sM1-04-22-2024 they match 100%. pd-activated-vm-more-negative uses the potentials only, and the other sets agree, so the outcome stands. But the potentials and the spikes in the paper's set come from different runs.
9. **[does not affect a conclusion]** The archive description says the files hold "spike train data from all 10,073 neurons" and 400 potential traces. The data hold only cells that fired, and the paper's set has 20 traces. R3 equals "the cells in the file" only if every cell that fired was stored. This was checked only indirectly: no unit has zero spikes, all 1,435 PT5B cells are present, and R3 matches the paper's numbers to 2–3 digits throughout.
10. **[does not affect a conclusion]** `pd-it6-rate-unchanged`: the claims file does not say whether "a test finds a difference" means only the tests under the rate reading whose means match. I took R3; under R1 the tests are significant but R1's means are far off.

**C. What I could not check, and the output that would settle it**

- **Union pairing.** T1/T2 p-values under R3 and R2 with the union of cells, zeros where absent, for IT2 (−01 vs −03), IT6 (−02 vs −04), IT5A and IT6 (problem 1).
- **Unitary events.** Re-run with coincidences counted as spikes or pairs in coincident bins (Grün complexity), and with each window's observed count printed against its maximum possible count (problem 2).
- **Electrode of "LFP 0".** Its electrode or depth attribute in the NWB, if any (problem 6).
- **S2 at 2 Hz.** The S2 2 Hz check with a window of at least 1 s (problem 4).
- **Time offsets.** The `starting_time` of the LFP and potential series. The notebook slices at index 2.0 × FS, assuming 0; the cross-correlation in cell 11 suggests the clocks are aligned.
- **Stored cells.** Whether any unit-level field (for example electrodes or cell metadata) lists silent cells, which would let R1 and fig1 be checked directly rather than through gid bounds.
- **Attempt record.** It was not available to me; claim counts come from the claims file (40).
